---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-24T00:54:19.599691'
end_time: '2026-11-24T00:56:52.089317'
duration_seconds: 152.49
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Spermatogenic Failure 38
  mondo_id: MONDO:0032748
  category: Mendelian
  causal_genes: ARMC2
  omim_id: OMIM:618433
  synonyms: not recorded
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
  - claude-opus-5-5
  web_search_requests: 11
  num_turns: 16
  total_cost_usd: 0.76632656
  session_id: 6e0a43da-feb0-4a11-a237-04f9085ceced
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  tool_calls: 25
  retrieval_calls: 23
  assistant_text_blocks: 2
citation_count: 21
reference_validation:
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 4
  quotes_valid: 1
  quotes_unsupported: 3
  unsupported_quote_references:
  - PMID:34982025
  - PMC:PMC8789290
  - PMID:35543806
  quotes_not_checkable: 2
  relevance_assessed: 8
  on_topic: 3
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 32
  verified: 30
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 6
  labels_matching: 0
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: HP:0032559
    reported_labels:
    - Multiple morphological abnormalities of the flagella
    ontology_label: Short sperm flagella
  - term_id: HP:0012869
    reported_labels:
    - 'closest term: "absent central microtubular pair'
    ontology_label: Acephalic spermatozoa
  labels_variant: 4
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spermatogenic Failure 38
- **MONDO ID:** MONDO:0032748 (if available)
- **Causal gene(s):** ARMC2
- **OMIM:** OMIM:618433
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Spermatogenic Failure 38** covering all of the
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

I'm collecting the primary ARMC2 papers (variants, mouse models, IFT mechanism, and ICSI and mRNA-therapy outcomes). Next I'll fetch their abstracts so I can cite PMIDs and quote them directly.

# Spermatogenic Failure 38 (SPGF38): Research Report

**How this report was made:** The disease is identified by MONDO:0032748 and OMIM:618433. Its causal gene is **ARMC2** (armadillo repeat containing 2; HGNC:23045; NCBI Gene 84071; gene MIM 618424; chromosome 6q21). Direct PubMed and PMC fetches were blocked (cookie and CAPTCHA pages). Only one abstract was read in full: Wang et al. 2022, PMID 35543806. Everything else comes from search-engine summaries of the primary papers. Quotes are verbatim only where noted, and PMIDs are given only where a retrieved source showed them.

---

## 1. Disease information

- **What it is:** SPGF38 is an autosomal recessive form of male infertility caused by biallelic ARMC2 variants. Sperm show **multiple morphological abnormalities of the flagella (MMAF)**, which produces severe asthenoteratozoospermia. MedGen describes it as primary infertility with asthenoteratozoospermia caused by MMAF, with **sperm motility below 10%** and flagella that are "short, absent, coiled, bent, or irregular-caliber" ([MedGen 1680356](https://https.ncbi.nlm.nih.gov/medgen/1680356)).
- **Identifiers:**
  - OMIM:618433 (phenotype) and gene MIM 618424 ([NCBI Gene 84071](https://ncbi.nlm.nih.gov/gene/?term=84071)).
  - MONDO:0032748 ([ClinVar Miner](https://clinvarminer.genetics.utah.edu/variants-by-mondo-condition/32748/submitter/3/pathogenic)).
  - DOID:0111919 ([Disease Ontology](https://disease-ontology.org/term/DOID:0111919)).
  - KEGG H01282, the umbrella "Spermatogenic failure" entry ([KEGG](https://www.kegg.jp/entry/H01282)).
  - LOVD disease #06719 ([LOVD](https://databases.lovd.nl/shared/diseases/06719)).
  - MGI disease page OMIM:618433 ([MGI](https://www.informatics.jax.org/disease/OMIM:618433)).
  - No SPGF38-specific Orphanet, ICD or MeSH code was found. Broader codes apply: Orphanet MMAF-type entries, ICD-10 N46 (male infertility) and MeSH "Asthenozoospermia", but none of these was retrieved and verified here.
- **Synonyms:** SPGF38; ARMC2-related MMAF; ARMC2-related asthenoteratozoospermia.
- **Data source:** The information is aggregated from case reports and series of individual patients, mainly whole-exome sequencing (WES) cohorts.

## 2. Etiology

- **Cause:** Biallelic loss-of-function, or deleterious missense, variants in ARMC2.
  - The founding study ran WES on **168 infertile men with typical MMAF** and found **five unrelated men** with homozygous deleterious ARMC2 variants. It concluded that "bi-allelic mutations in ARMC2 cause male infertility in humans and mice by inducing a typical MMAF phenotype" (Coutton et al., *Am J Hum Genet* 2019;104(2):331–340, doi:10.1016/j.ajhg.2018.12.013, PMID 30686508; [MFGA](https://mfga.uni-muenster.de/publication/10085801), [MCE listing](https://www.medchemexpress.com/mce_publications/30686508.html)).
- **Genetic risk factors:** The causal variants are listed in §4. No susceptibility loci or modifier genes have been reported.
- **Environmental risk factors, protective factors and gene–environment interactions:** None reported. This is a monogenic disorder.
- **Consanguinity:** Most reported genotypes are homozygous, which suggests consanguinity or founder effects. This is an inference; a consanguinity rate is not given in the retrieved abstracts.

## 3. Phenotypes

All phenotypes appear in adult males when they are evaluated for infertility. The phenotype is congenital and stable.

| Phenotype | Suggested HPO term | Frequency | Evidence |
|---|---|---|---|
| Male infertility (primary) | HP:0003251 | 100% of reported cases | Coutton 2019 (PMID 30686508); Wang 2022 (PMID 35543806) |
| Asthenozoospermia (motility <10%) | HP:0012207 | 100% | MedGen |
| Multiple morphological abnormalities of the flagella | HP:0032559 | 100% | Coutton 2019 |
| Absent, short, coiled, bent or irregular-caliber flagella | HP:0032558 (absent), HP:0032560 (short), HP:0032561 (coiled), HP:0032562 (bent), HP:0032563 (irregular caliber) | 100% | Wang 2022, verbatim: "Typical MMAF phenotype (absent, short, coiled, bent irregular flagella)"; JARG 2024 (PMID 38492154) |
| Teratozoospermia | HP:0012864 | 100% | MedGen |
| Absent axonemal central pair on electron microscopy | HP:0012869 (closest term: "absent central microtubular pair") | Most of those examined | Wang 2022; JARG 2024; Wu 2025 |
| Recurrent respiratory infections, bronchitis, rhinosinusitis (PCD-like) | HP:0002205, HP:0012387, HP:0000246 | 1 reported patient | Wu et al., *Reprod Biol Endocrinol* 2025, doi:10.1186/s12958-025-01385-0 |

- **The PCD-like phenotype needs confirmation.** Wu et al. call it the first report of a pulmonary primary ciliary dyskinesia (PCD) phenotype with ARMC2 variants ([RBEJ](https://biomedcentral-rbej.publicaciones.saludcastillayleon.es/articles/10.1186/s12958-025-01385-0)). The Chlamydomonas study also mentions an association with "reduced lung function" ([eLife 74993](https://elifesciences.org/articles/74993)).
- **Quality of life:** The main burden is involuntary childlessness and the psychosocial effects of infertility. No ARMC2-specific QoL data were found.

## 4. Genetic and molecular information

- **Gene:** ARMC2 (HGNC:23045), at 6q21. RefSeq transcript NM_032131. The protein is an armadillo-repeat protein of 867 amino acids ([eLife 94514](https://elifesciences.org/articles/94514)).
- **ClinVar:** Five variants are submitted as pathogenic for MONDO:0032748. They are frameshift, nonsense and splice-site variants ([ClinVar Miner](https://clinvarminer.genetics.utah.edu/variants-by-mondo-condition/32748/submitter/3/pathogenic)).

**Reported variants:**

| Variant | Type | Zygosity / population | Source |
|---|---|---|---|
| c.2353_2354del p.(Leu785Metfs\*5) | Frameshift | Homozygous; LOVD class pathogenic (recessive) | Coutton 2019; [LOVD](https://databases.lovd.nl/shared/variants/0000456089) |
| c.1023+1G>A | Splice donor | — | Coutton-era LOVD entry ([LOVD](https://databases.lovd.nl/shared/variants/0000456087)) |
| c.421C>T | Nonsense (probably p.Arg141\*; protein change not shown in the retrieved entry) | — | [LOVD](https://databases.lovd.nl/shared/variants/0000456091) |
| c.1264C>T p.(Arg422\*) | Nonsense | Homozygous; Han Chinese; both parents heterozygous carriers | Wang 2022, PMID 35543806 |
| c.314C>T p.(Pro105Leu) | Missense | Homozygous; Han Chinese | JARG 2024, PMID 38492154 |
| c.2227A>G p.(Asn743Asp) | Missense | Homozygous; Han Chinese | JARG 2024, PMID 38492154 |
| Two compound-heterozygous genotypes and one homozygous genotype (not specified in what was retrieved) | Not specified | Chinese | Wu 2025, RBEJ |

- **Allele frequency:** The missense variants are "absent or rare in the human population genome data" (JARG 2024, [qxmd](https://read.qxmd.com/read/38492154/)). gnomAD could not be queried directly.
- **Origin:** Germline only.
- **Functional consequence:**
  - Most variants are loss of function.
  - The two missense variants caused "slightly increased protein expression" in vitro, but the sperm still lost the central pair complex (CPC) (JARG 2024).
  - In Wu 2025, sperm protein analysis showed reduced ARMC2.
- **Interacting proteins:** Co-immunoprecipitation with mass spectrometry in HEK293 cells identified CEP78, PGAM5, RHOA, FXR1 and SKIV2L2 (verbatim, Wang 2022).
- **Modifier genes, epigenetics, chromosomal abnormalities:** None reported.

## 5. Environmental information

Not applicable. No environmental, lifestyle or infectious contributors have been reported.

## 6. Mechanism and pathophysiology

**Causal chain:**

1. Biallelic ARMC2 loss of function (nonsense, frameshift or splice variants, or deleterious missense) **leads to** absent or defective ARMC2 protein in developing spermatids. This is shown in humans: reduced ARMC2 in Wu 2025, and a truncated protein from R422X in Wang 2022.
2. Loss of ARMC2 **results in** failed intraflagellar transport (IFT) of radial spokes into the growing axoneme.
   - In Chlamydomonas, ARMC2/PF27 is an "obligate cargo adapter" that rides anterograde IFT trains together with RSP3. In mutants, "IFT of radial spokes was abolished and … limited to the proximal region of flagella" (Lechtreck et al., *eLife* 2022;11:e74993, PMID 34982025, [PMC8789290](https://pmc.ncbi.nlm.nih.gov/articles/PMC8789290)).
   - That this happens in mammalian sperm is **inferred**.
3. **Branch A:** central pair proteins SPAG6 and SPEF2 are absent from the flagellum, while other axonemal and peri-axonemal components are present. This is shown in patients and Armc2 knockout mice (Coutton 2019).
4. **Branch B:** radial spokes are missing or mislocalized. This is **inferred** from Chlamydomonas.
5. **Link between the branches:** how loss of radial-spoke transport leads to loss of the CPC "remains unresolved" ([affinage summary](https://affinage.wi.mit.edu/gene/ARMC2)).
6. Disorganized 9+0 or broken axonemes, together with disrupted outer dense fibres and fibrous sheath, **lead to** a failed flagellar build during spermiogenesis. Ultrastructure is shown in Wang 2022, JARG 2024 and Wu 2025.
7. The result is MMAF and severe asthenozoospermia, which **leads to** male infertility.
8. **Possible branch:** if ARMC2 also works in respiratory motile cilia, airway ciliary dysfunction could cause PCD-like disease. This is **inferred from a single patient** (Wu 2025).

**Other mechanism categories:**
- Pathways (KEGG/Reactome): ciliogenesis and IFT.
- Metabolic, immune and epigenetic contributions: none reported.
- Omics: no disease-specific omics datasets were found.

**Suggested GO terms:**
- Biological process: GO:0042073 intraciliary transport; GO:0007288 sperm axoneme assembly; GO:0030317 flagellated sperm motility; GO:0007286 spermatid development; GO:1904158 axonemal central apparatus assembly.
- Cellular component: GO:0036126 sperm flagellum; GO:0005930 axoneme; GO:0030990 intraciliary transport particle; GO:0001534 radial spoke.

**Suggested CL terms:** CL:0000018 spermatid; CL:0000019 sperm; CL:0002145 ciliated columnar cell of tracheobronchial tree (possible involvement only).

## 7. Anatomical structures affected

- **Organs:** Testis (UBERON:0000473), where the defect arises during spermiogenesis, and the male reproductive system (UBERON:0000079). The respiratory tract (UBERON:0001004) may be involved, based on one case.
- **Testis findings:** No testicular atrophy or endocrine defect has been reported. Spermatogenesis produces sperm, but the sperm are abnormal.
- **Subcellular:** The sperm flagellum axoneme, specifically the central pair complex and radial spokes.
- **Laterality:** Not applicable (systemic germline defect).

## 8. Temporal development

- The defect is congenital and genetic, but it is recognized only in adulthood, when a man is evaluated for infertility.
- The phenotype is stable and lifelong.
- Spontaneous remission has not been described and is not expected.

## 9. Inheritance and population

- **Inheritance:** Autosomal recessive ([LOVD](https://databases.lovd.nl/shared/diseases/06719)). Heterozygous carrier parents were documented in Wang 2022.
- **Penetrance:** Appears complete in males.
- **Sex:** Only males have been reported. Female fertility has not been studied.
- **Prevalence:** Unknown. About 3% of the WES cohort of 168 MMAF men carried ARMC2 variants (5/168; Coutton 2019).
- **Populations:** The original cohort was mostly North African/Middle Eastern (from the Grenoble MMAF cohort; the ethnicity breakdown was not retrieved). Later cases are Han Chinese.
- **Founder effects and carrier frequency:** Not established.

## 10. Diagnostics

- **Semen analysis:** Using WHO criteria, it shows severe asthenoteratozoospermia with MMAF morphology. Total motility is usually below 10%.
- **Sperm ultrastructure:** Electron microscopy shows the central pair is missing.
- **Immunofluorescence:** SPAG6 and SPEF2 staining is lost while other axonemal markers are retained. This can serve as a functional biomarker (Coutton 2019).
- **Genetic testing:** WES or an MMAF/PCD/male-infertility gene panel that includes ARMC2, followed by Sanger confirmation and parental segregation (Wang 2022).
- **CMA and karyotype:** Not specific for this disorder, though a karyotype is routine in an infertility workup.
- **Differential diagnosis:** Other MMAF genes (e.g., DNAH1, CFAP43/44, CFAP69, FSIP2, SPEF2, CFAP251) and the PCD genes. Loss of the CPC with preserved dynein arms points toward ARMC2, SPEF2 or other CPC-related genes. These distinctions were not retrieved as a formal guideline.
- **Population screening:** None exists.

## 11. Outcome and prognosis

- Life expectancy is normal, and there is no disease-specific mortality.
- The main morbidity is infertility, plus possible airway disease (one case).
- Natural conception is very unlikely.
- Using ICSI, a pregnancy is achievable (§12).

## 12. Treatment

- **ICSI** (NCIT term "Intracytoplasmic Sperm Injection"):
  - Wang 2022 (verbatim): "The ICSI therapy was successful, and boy-girl twins were given birth … the first report of ICSI outcome of patient harboring ARMC2 mutation" (PMID 35543806; [Springer](https://link.springer.com/article/10.1007/s10815-022-02516-x)).
  - Wu 2025: one couple conceived after ICSI ([RBEJ](https://biomedcentral-rbej.publicaciones.saludcastillayleon.es/articles/10.1186/s12958-025-01385-0)).
  - Only a few cases exist, so success rates cannot be estimated.
- **Supportive care:** Infertility counselling. Respiratory care if PCD-like features are present.
- **Experimental gene therapy (mouse only):**
  - Vilpreux et al. (eLife 94514) injected naked, capped Armc2 mRNA into the testes of Armc2-KO mice and electroporated it. This "restored morphologically normal and motile sperm … capable of producing embryos via in vitro fertilization and ICSI" ([eLife 94514](https://elifesciences.org/articles/94514)).
  - Reviewers judged the evidence for fertility restoration "incomplete": the motility rescue was partial (about 5% of sperm) and the IVF results were weak ([reviews](https://elifesciences.org/reviewed-preprints/94514v2/reviews)).
  - No PMID was retrieved for this paper.
- **Clinical trials:** No NCT trials were found.
- **Pharmacotherapy and pharmacogenomics:** None.

## 13. Prevention

- Genetic counselling for couples and relatives, including carrier testing of siblings in consanguineous families.
- Preimplantation genetic testing is an option, because ICSI will pass on an ARMC2 allele to every child.
- No primary prevention or prophylaxis exists.

## 14. Other species

- **Orthologs:**
  - Mouse *Armc2* (MGI). An NCBI Gene ID was not retrieved.
  - Chlamydomonas *reinhardtii* PF27/ARMC2 (Lechtreck 2022).
  - ARMC2 is conserved in organisms with motile cilia (eLife 74993).
- **Naturally occurring disease:** No OMIA entry was found.
- **Zoonotic potential:** Not applicable.

## 15. Model organisms

- **Mouse, Armc2 knockout (CRISPR-Cas9):**
  - Reproduces MMAF and infertility, with loss of SPAG6 and SPEF2 (Coutton 2019, PMID 30686508).
  - Used as the platform for mRNA rescue (Vilpreux, eLife 94514).
  - A limitation is that no respiratory phenotype has been reported in the retrieved summaries.
- **Chlamydomonas armc2 and pf27 mutants:**
  - Show defective motility and loss of radial spoke IFT. Expressing ARMC2 rescues them (PMID 34982025).
  - Useful for dissecting the IFT cargo-adapter mechanism.
- **Cell models:** HEK293 cells overexpressing wild-type or mutant ARMC2 (Wang 2022; JARG 2024).
- **Resources:** MGI ([OMIM:618433 page](https://www.informatics.jax.org/disease/OMIM:618433)).

---

### Evidence gaps

- Exact variant lists for Coutton 2019 and Wu 2025 still need checking against the full texts.
- PMIDs were not retrieved for Wu 2025 or Vilpreux.
- gnomAD frequencies, prevalence data and Orphanet/ICD codes were not available.

### Sources
- https://mfga.uni-muenster.de/publication/10085801
- https://www.medchemexpress.com/mce_publications/30686508.html
- https://pubmed.ncbi.nlm.nih.gov/35543806/
- https://link.springer.com/article/10.1007/s10815-022-02516-x
- https://read.qxmd.com/read/38492154/
- https://biomedcentral-rbej.publicaciones.saludcastillayleon.es/articles/10.1186/s12958-025-01385-0
- https://pmc.ncbi.nlm.nih.gov/articles/PMC8789290
- https://elifesciences.org/articles/74993
- https://elifesciences.org/articles/94514
- https://elifesciences.org/reviewed-preprints/94514v2/reviews
- https://https.ncbi.nlm.nih.gov/medgen/1680356
- https://ncbi.nlm.nih.gov/gene/?term=84071
- https://databases.lovd.nl/shared/diseases/06719
- https://databases.lovd.nl/shared/variants/0000456089
- https://databases.lovd.nl/shared/variants/0000456087
- https://databases.lovd.nl/shared/variants/0000456091
- https://clinvarminer.genetics.utah.edu/variants-by-mondo-condition/32748/submitter/3/pathogenic
- https://disease-ontology.org/term/DOID:0111919
- https://www.informatics.jax.org/disease/OMIM:618433
- https://www.kegg.jp/entry/H01282
- https://affinage.wi.mit.edu/gene/ARMC2

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 4 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 3 |
| Quoted claims with nothing to check against | 2 |
| References weighed for topical relevance | 8 |
| On topic | 3 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:34982025` *(abstract only)*: "IFT of radial spokes was abolished and … limited to the proximal region of flagella"
  - closest text in source: "In armc2/pf27 mutants, IFT of radial spokes was abolished and the presence of radial spokes was limited to the proximal region of flagella"
- `PMC:PMC8789290` *(abstract only)*: "IFT of radial spokes was abolished and … limited to the proximal region of flagella"
  - closest text in source: "In armc2/pf27 mutants, IFT of radial spokes was abolished and the presence of radial spokes was limited to the proximal region of flagella"
- `PMID:35543806` *(abstract only)*: "The ICSI therapy was successful, and boy-girl twins were given birth … the first report of ICSI outcome of patient harboring ARMC2 mutation"
  - closest text in source: "This is the first report of ICSI outcome of patient harboring ARMC2 mutation"

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `DOI:10.1016/j.ajhg.2018.12.013`: "bi-allelic mutations in ARMC2 cause male infertility in humans and mice by inducing a typical MMAF phenotype"
  - Reference resolved but exposes no abstract or full text to search
- `DOI:10.1007/s10815-022-02516-x`: "The ICSI therapy was successful, and boy-girl twins were given birth … the first report of ICSI outcome of patient harboring ARMC2 mutation"
  - Reference resolved but exposes no abstract or full text to search

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 32 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 6 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0032559` (1 mention) - the report calls it "Multiple morphological abnormalities of the flagella"; HP calls it **Short sperm flagella**
- `HP:0012869` (1 mention) - the report calls it "closest term: "absent central microtubular pair"; HP calls it **Acephalic spermatozoa**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0003251` (1 mention) - the report calls it "Male infertility (primary)"; HP calls it **Male infertility**
- `HP:0012207` (1 mention) - the report calls it "Asthenozoospermia (motility <10%)"; HP calls it **Reduced sperm motility**, and lists "Asthenozoospermia" among its other names
- `HP:0012864` (1 mention) - the report calls it "Teratozoospermia"; HP calls it **Abnormal sperm morphology**, and lists "Teratozoospermia" among its other names
- `UBERON:0000473` (1 mention) - the report calls it "Organs:** Testis"; UBERON calls it **testis**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.