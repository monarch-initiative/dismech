---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-27T16:59:04.724812'
end_time: '2026-10-27T17:00:09.064603'
duration_seconds: 64.34
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Dehydrated Hereditary Stomatocytosis 2
  mondo_id: MONDO:0014737
  category: Mendelian
  causal_genes: KCNN4
  omim_id: OMIM:616689
  synonyms: DHS2; Dehydrated hereditary stomatocytosis type 2; KCNN4 dehydrated hereditary
    stomatocytosis; dehydrated hereditary stomatocytosis 2; DHS2; dehydrated hereditary
    stomatocytosis caused by mutation in KCNN4
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
  web_search_requests: 2
  num_turns: 4
  total_cost_usd: 0.7781427999999999
  session_id: 365353bd-1c8b-55dd-9afa-fdb9e1b5ccf0
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 8
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 4
  validator_version: 0.4.0
term_validation:
  total_terms: 14
  verified: 13
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 4
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: HP:0001744
    reported_labels:
    - '[background knowledge, unverified]'
    ontology_label: Splenomegaly
  labels_variant: 3
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Dehydrated Hereditary Stomatocytosis 2
- **MONDO ID:** MONDO:0014737 (if available)
- **Causal gene(s):** KCNN4
- **OMIM:** OMIM:616689
- **Synonyms:** DHS2; Dehydrated hereditary stomatocytosis type 2; KCNN4 dehydrated hereditary stomatocytosis; dehydrated hereditary stomatocytosis 2; DHS2; dehydrated hereditary stomatocytosis caused by mutation in KCNN4
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Dehydrated Hereditary Stomatocytosis 2** covering all of the
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

# Dehydrated Hereditary Stomatocytosis 2 (DHS2; KCNN4 "Gardos channelopathy"): research report

**Method and caveats.** This report rests on two web searches that returned the PMC and journal pages linked in the Sources list at the end. It is not a systematic literature review. I did not open the full texts, so I give no abstract quotes and no PMIDs. Cited PMC articles are identified by PMC ID only. Items marked **[background knowledge, unverified]** come from general knowledge and need a `just fetch-reference` check and an exact snippet before they enter the KB. Several template sections returned nothing in the searches. Those sections say so rather than guessing.

## 1. Disease information

**Causal gene.** Dehydrated hereditary stomatocytosis 2 is caused by heterozygous activating variants in **KCNN4** (HGNC symbol KCNN4, OMIM 616689; the OMIM gene ID is not confirmed here). KCNN4 encodes the Ca²⁺-activated K⁺ channel KCa3.1, called the Gardos channel in red cells.

**Overview.** DHS2 is a dominant red-cell channelopathy. It causes chronic hemolytic anemia with red-cell dehydration. It is also called Gardos-type hereditary xerocytosis ("Gardos-HX"). It is the less common counterpart of PIEZO1-related DHS1.

**Identifiers and synonyms.** MONDO:0014737 and OMIM:616689 are taken from the task template and not independently re-checked. Orphanet, ICD-10/11 and MeSH IDs were not retrieved. Synonyms are as listed in the template. Related names are "Gardos channelopathy" and "Gardos-HX".

**Data source.** The literature is aggregated from family reports and small case series, not individual EHR data.

## 2. Etiology

- **Causal factor:** gain-of-function KCNN4 variants. Recurrent variants are **p.R352H** (the best documented) and **p.V282M/E**. Reports also include p.S314P and p.A279T. Searches describe recurrent mutations at R352 and V282 in 6 independent families, and one family report calls its case the 11th family with p.R352H ([PMC9175893](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9175893/), [PMC5431847](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5431847/)).
- **Risk factors:** none beyond the genotype were found. Possible environmental or gene-environment contributors, such as infection or oxidant stress, were not found in the searches. Modifier genes and protective factors were not identified.
- **Splenectomy as an iatrogenic risk:** splenectomy is generally avoided in dehydrated stomatocytosis because of thromboembolic risk. Four splenectomized KCNN4 patients had no thrombotic events over a mean of 26.5 years.

## 3. Phenotypes

Phenotype frequencies are not available from the searches.

| Phenotype | Notes | HPO suggestion (verify by lookup) |
|---|---|---|
| Chronic hemolytic anemia | Variable, from well compensated to transfusion-requiring. A V282M family had near-normal hemoglobin. | Hemolytic anemia HP:0001878 |
| Stomatocytosis / dehydrated red cells | | Stomatocytosis HP:0004447 |
| Reticulocytosis | | HP:0001923 |
| Hyperferritinemia / iron overload | Mean diagnostic ferritin was 1702 ng/mL in KCNN4 patients vs 656 ng/mL in PIEZO1 patients. | Iron overload HP:0011031 |
| Cholelithiasis | Most patients developed it and needed cholecystectomy. | Cholelithiasis HP:0001081 |
| Splenomegaly | **[background knowledge, unverified]** | HP:0001744 |
| Perinatal presentation | One p.R352H proband needed transfusion in utero and after preterm birth. Perinatal edema or hydrops was not confirmed in the searches. | |

- **Onset and course:** onset is congenital or neonatal. Transfusion needs tend to fall in adulthood (see section 11).
- **Quality-of-life data:** none found.

## 4. Genetic and molecular information

- **Inheritance:** autosomal dominant.
- **Variants:** R352H is in the C-terminal calmodulin-binding region. V282M/E is in the S6 transmembrane region. S314P and A279T are less well characterized. Domain placement is **[background knowledge, unverified]**. Classification and gnomAD frequencies were not retrieved.
- **Functional consequence:** gain of function. Studies show hyperactivated Gardos channels in circulating erythrocytes and erythroblasts. Three disease-linked mutations are all gain-of-function but "do not share a common mechanism", with different effects on Ca²⁺ sensitivity and gating. S314P is described as gain-of-function but milder than R352H ([PMC5431847](https://pmc.ncbi.nlm.nih.gov/articles/PMC5431847), [PMC7756992](https://pmc.ncbi.nlm.nih.gov/articles/PMC7756992)).
- **Genotype-phenotype:** the V282M/E variants give clear dehydration and a left-shifted ektacytometry curve resembling PIEZO1 disease. R352H does not systematically produce dehydration, and routine hematology may not diagnose it.
- **Epigenetics and chromosomal abnormalities:** not applicable or not found.

## 5. Environmental information

No environmental, lifestyle or infectious factors were found.

## 6. Mechanism / pathophysiology

1. A heterozygous activating KCNN4 variant (for example R352H or V282M) alters Ca²⁺ sensitivity or gating of the Gardos channel (demonstrated electrophysiologically).
2. The channel is hyperactive in erythrocytes and erythroblasts. This is demonstrated.
3. Enhanced K⁺ efflux, with accompanying Cl⁻ and water loss, leads to red-cell dehydration and cell shrinkage. This is the accepted model. Dehydration is not consistently observed with every variant.
4. Dehydrated, rigid cells with altered membrane properties are cleared by the spleen, which results in extravascular hemolysis and anemia (inferred).
5. Chronic hemolysis and ineffective erythropoiesis lead to iron overload, and bilirubin turnover leads to gallstones (inferred).
6. A branch: patient erythrocytes show a Ca²⁺-dependent link to PIEZO1, since PIEZO1 Ca²⁺ influx activates the Gardos channel. This is **[background knowledge, unverified]**.

**Suggested ontology terms** (verify by lookup before binding):
- GO: potassium ion export across plasma membrane (GO:0097623) and calcium-activated potassium channel activity (GO:0015269).
- Cell types: erythrocyte (CL:0000232) and erythroblast (CL:0000765).

No molecular profiling or omics findings were retrieved.

## 7. Anatomical structures affected

- **Blood and red cells:** primary site (UBERON:0000178 blood).
- **Spleen:** site of red-cell clearance.
- **Liver and gallbladder:** iron loading and pigment stones.
- **Subcellular:** plasma membrane (GO:0005886).

## 8. Temporal development

Congenital onset with a chronic lifelong course. Severity is variable. Transfusion needs may be high in the neonatal period or childhood and often decline in adulthood. This is based on a family series in which severe neonatal cases did not need ongoing transfusion in adulthood ([PMC9175893](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9175893/)).

## 9. Inheritance and population

Autosomal dominant. Incidence and prevalence were not found; the disease is described as very rare. I found no information on penetrance, founder effects, sex ratio or consanguinity. Reported families come from several ancestries.

## 10. Diagnostics

- **Laboratory:** CBC and indices, smear, reticulocytes, ferritin, and bilirubin.
- **Ektacytometry:** a left-shifted osmotic-gradient curve for V282M/E. R352H may not show clear dehydration.
- **Reticulocyte indices:** one study reported that these distinguished Gardos-HX and PIEZO1-HX from other conditions with 100% sensitivity and specificity ([PMC9393219](https://pmc.ncbi.nlm.nih.gov/articles/PMC9393219)).
- **Genetic testing:** targeted gene panels for hemolytic anemia or membrane disorders, or exome sequencing. This is the effective route because routine hematology often fails to diagnose.
- **Differential diagnosis:** PIEZO1 xerocytosis, other membrane disorders such as spherocytosis, and pyruvate kinase deficiency.

## 11. Outcome and prognosis

- **Complications:** iron overload, cholelithiasis requiring cholecystectomy in most patients, and perinatal complications in severe cases.
- **Survival data:** none found.
- **Splenectomy:** it did not correct anemia in one family. See the thromboembolic caution in section 2.

## 12. Treatment

- **Supportive care:** transfusion as needed and monitoring of iron status. Iron chelation is a reasonable option for iron overload. **[background knowledge, unverified]**
- **Targeted therapy under study:** senicapoc is a Gardos channel blocker, proposed for a subset of KCNN4 variants. Its sensitivity varies significantly between mutants ([PMC7756992](https://pmc.ncbi.nlm.nih.gov/articles/PMC7756992), [Frontiers 2020](https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2020.602109/pdf)). No patient clinical results were found, and I did not look up trials.
- **Splenectomy:** generally avoided because of thromboembolic risk.
- **Suggested NCIT terms** (verify by lookup): Pharmacotherapy (C15986) for senicapoc, Blood Transfusion for supportive care (look up the code), and Surgical Procedure (C15329).

## 13. Prevention

Genetic counseling for autosomal dominant inheritance, and family cascade testing. No screening program was identified.

## 14. Other species and natural disease

Not found in the searches. Check OMIA and the Alliance of Genome Resources.

## 15. Model organisms

No model-organism data were retrieved. Studies cited above used patient erythrocytes and heterologous expression in cell systems (in vitro and ex vivo, HUMAN_CLINICAL and IN_VITRO evidence sources). A search of MGI for Kcnn4 mutant mice is needed, since Kcnn4 knockout mice are **[background knowledge, unverified]**.

## Gaps to close before curation

- Primary PMIDs and exact abstract quotes for the R352H and V282M discovery papers.
- HPO frequencies.
- Epidemiology.
- Senicapoc trial data.
- Orphanet and GeneReviews checks.
- Animal models.

## Sources

- [Diagnosing DHSt due to a KCNN4 Gardos channel mutation: multi-generational family (PMC9175893)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9175893/)
- ['Gardos Channelopathy': a variant of hereditary stomatocytosis with complex molecular regulation (PMC5431847)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5431847/)
- [PMC7756992](https://pmc.ncbi.nlm.nih.gov/articles/PMC7756992)
- [PMC9393219](https://pmc.ncbi.nlm.nih.gov/articles/PMC9393219)
- [Frontiers in Physiology 2020 (fphys.2020.602109)](https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2020.602109/pdf)
- [Frontiers in Physiology 2022 (fphys.2022.918620)](https://www.frontiersin.org/articles/10.3389/fphys.2022.918620/pdf)
- [Gardos Channel Mutation Is Associated with Hereditary Dehydrate Stomatocytosis: a Complex Channelopathy](https://sonar.ch/global/documents/27904)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 14 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 4 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001744` (1 mention) - the report calls it "[background knowledge, unverified]"; HP calls it **Splenomegaly**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0097623` (1 mention) - the report calls it "GO: potassium ion export across plasma membrane"; GO calls it **potassium ion export across plasma membrane**
- `CL:0000232` (1 mention) - the report calls it "Cell types: erythrocyte"; CL calls it **erythrocyte**
- `GO:0005886` (1 mention) - the report calls it "Subcellular:** plasma membrane"; GO calls it **plasma membrane**, and lists "cellular membrane" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.