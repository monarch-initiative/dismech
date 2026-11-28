---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-18T23:30:21.621851'
end_time: '2026-11-18T23:40:57.643328'
duration_seconds: 636.02
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Combined Oxidative Phosphorylation Deficiency 19
  mondo_id: MONDO:0014269
  category: Mendelian
  causal_genes: LYRM4
  omim_id: OMIM:615595
  synonyms: LYRM4 combined oxidative phosphorylation deficiency; combined oxidative
    phosphorylation deficiency caused by mutation in LYRM4; combined oxidative phosphorylation
    deficiency type 19
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
  web_search_requests: 4
  num_turns: 38
  total_cost_usd: 1.2379523000000001
  session_id: 9c45f0d4-e84d-4793-97e2-67dc63997f46
  stop_reason: end_turn
  permission_denials: 1
  denied_tools:
  - Bash
  tool_calls: 37
  retrieval_calls: 36
  assistant_text_blocks: 4
fell_back: true
requested_provider: antigravity
provider_attempts:
- provider: antigravity
  succeeded: false
  error_type: ProviderQuotaError
  remedy: the plan's usage limit is spent
  retryable: false
- provider: claude_code
  succeeded: true
citation_count: 5
reference_validation:
  total_references: 22
  verified: 22
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 14
  quotes_valid: 8
  quotes_unsupported: 6
  unsupported_quote_references:
  - PMID:23814038
  relevance_assessed: 22
  on_topic: 6
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 4
  verified: 1
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0014269
    reported_labels:
    - MONDO
    ontology_label: combined oxidative phosphorylation deficiency 19
  unresolvable_prefixes:
  - OMIM
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Combined Oxidative Phosphorylation Deficiency 19
- **MONDO ID:** MONDO:0014269 (if available)
- **Causal gene(s):** LYRM4
- **OMIM:** OMIM:615595
- **Synonyms:** LYRM4 combined oxidative phosphorylation deficiency; combined oxidative phosphorylation deficiency caused by mutation in LYRM4; combined oxidative phosphorylation deficiency type 19
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Combined Oxidative Phosphorylation Deficiency 19** covering all of the
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

Still researching: I've got the main LYRM4 case reports (Lim 2013, Coelho 2019) and the mechanism papers. Now I'm checking for newer patients, the ClinVar variants, and OMIM/Orphanet.

I'm now collecting model-organism and protein-annotation data (UniProt, mouse/yeast/fly/parasite studies) before writing the report.

Checking ClinVar for the two patient missense variants, then I'll write.

# Combined Oxidative Phosphorylation Deficiency 19 (COXPD19), caused by LYRM4: research report

**Scope:** This report covers the disease with MONDO:0014269 and OMIM:615595, caused by biallelic variants in **LYRM4** (LYR motif-containing 4, also called ISD11; HGNC:21365; gene MIM 613311). It is not about the other numbered COXPD types; for example, ClinVar files deletions that span both FARS2 and LYRM4 under COXPD14, which is caused by FARS2.

**Limits on what I could retrieve:**
- I could not open OMIM, Orphanet, UniProt or MGI/IMPC directly; they returned 403, connection-refused or empty results. Clinical data come from the primary papers (full text via PMC), MedGen's HPO list, ClinVar and NCBI E-utilities.
- The fetch tool limits verbatim quotes to about 125 characters, so quotes are short excerpts.
- I did not retrieve ontology IDs (HPO, GO, CL, UBERON, CHEBI, NCIT) in this session. Terms are given by **label only**, and IDs need a lookup before you load them into the knowledge base.

---

## 1. Disease information

**Overview.** COXPD19 is an ultra-rare autosomal recessive mitochondrial disease. Loss of function of ISD11 (encoded by LYRM4), a key part of the mitochondrial iron–sulfur (Fe–S) cluster assembly machinery, causes deficiency of the Fe–S-containing respiratory chain complexes I, II and III. It also affects other mitochondrial and cytosolic Fe–S enzymes such as the aconitases and ferrochelatase. It presents in the neonatal period or early childhood with lactic acidosis and respiratory failure. The outcome ranges from death in infancy to full recovery.
- Lim et al., Hum Mol Genet 2013, **PMID 23814038**: "Here, we report a homozygous mutation in LYRM4 in two patients with combined OXPHOS deficiency."
- MONDO definition, via MedGen 816385: "Any combined oxidative phosphorylation deficiency in which the cause of the disease is a mutation in the LYRM4 gene." (https://www.ncbi.nlm.nih.gov/medgen/816385)

**Identifiers**

| Resource | ID | Source |
|---|---|---|
| MONDO | MONDO:0014269 | MedGen 816385; ClinVar VCV000102450 |
| OMIM (phenotype) | 615595 | ClinVar VCV000102450 |
| OMIM (gene) | 613311 | HGNC REST; NCBI Gene 57128 |
| Orphanet | ORPHA:397593 | ClinVar VCV000102450 condition xref |
| UMLS / MedGen | C3810055 / 816385 | MedGen |
| MeSH | No disease-specific descriptor found (MedGen lists none) | MedGen |
| ICD-10 / ICD-11 | Not retrieved. A generic mitochondrial-disorder code would apply; check before use. | — |

**Synonyms:** COXPD19; combined oxidative phosphorylation defect type 19; LYRM4 combined oxidative phosphorylation deficiency; ISD11 deficiency; "Iron-sulfur cluster ISD11 deficiency" (Coelho 2019, PMID 31497476).

**Type of evidence:** All clinical knowledge comes from individual case reports: three published patients in two families (PMIDs 23814038, 31497476). No registry or EHR cohort data exist.

## 2. Etiology

- **Causal factor:** Biallelic (homozygous) loss-of-function missense variants in LYRM4. They impair the NFS1–ISD11 cysteine desulfurase complex, which leads to defective Fe–S cluster biogenesis (PMIDs 23814038, 26342079).
- **Genetic risk factors:** Consanguinity. The first family was "an extended consanguineous family" of Lebanese/Syrian ancestry, with first-cousin parents and at least two consanguineous loops (PMID 23814038). The third patient's parents were non-consanguineous Portuguese heterozygous carriers (PMID 31497476).
- **Environmental triggers.** None is known as a cause, but **intercurrent infection and catabolic stress trigger decompensation**. The Coelho patient's first cardiorespiratory arrest followed a viral respiratory infection (RSV in secretions, HHV-6 in CSF). Her second followed four days of fever, cough and poor intake (PMID 31497476). Group B Streptococcus was cultured from the neonatal gastric aspirate of Lim patient P2 (PMID 23814038).
- **Protective factors:** None established. Lim et al. propose that adequate cysteine supply may let residual NFS1 activity support viability: "NFS1 has a residual l-cysteine desulfurase activity which is sufficient to retain the viability of the patient" (PMID 23814038). This is a hypothesis and has not been tested.
- **Gene–environment interaction:** Infection or fever acting on reduced Fe–S/OXPHOS capacity precipitates crises (PMID 31497476). This is a clinical observation; the mechanism is inferred.
- **Other associations (not COXPD19):** Common LYRM4-region variants have been linked to ulcerative colitis susceptibility: "Additional novel UC susceptibility genes were LYRM4 and CDKAL1" (PMID 19068216). LYRM4 promoter polymorphisms have been linked to cognitive deficit in schizophrenia (PMID 21968932). Neither association is shown to bear on COXPD19.

## 3. Phenotypes

The cohort is three patients: P1 and P2 (Lim 2013) and P3 (Coelho 2019). Frequencies are raw counts. MedGen's HPO annotation list is the source of most term labels.

| Phenotype (suggested HPO label) | Type | Onset | n/3 | Details and source |
|---|---|---|---|---|
| Lactic acidosis; Metabolic acidosis | Lab | Neonatal to toddler | 3/3 | P1 blood lactate up to 14.4 mmol/L, pH 6.9–7.14; P2 9.3 mmol/L; P3 up to 5 mmol/L during crises and normal between them (PMIDs 23814038, 31497476) |
| Increased CSF lactate; Elevated brain lactate level by MRS | Lab/imaging | Neonatal | 2/2 tested | CSF 3.9 mmol/L in P1 and P2; large MRS lactate doublet in P2 (PMID 23814038) |
| Lacticaciduria; Ketosis | Lab | Neonatal/infancy | 3/3 | Severe ketosis in P2; ketonuria in P3 |
| Respiratory distress / respiratory insufficiency requiring ventilation | Sign | Day 1 to 3 y | 3/3 | P1 intubated twice; P2 ventilated, later respiratory arrest; P3 cardiorespiratory arrest ×2 |
| Stridor | Sign | Neonatal | 2/3 | P1 and P2 |
| Cardiorespiratory arrest | Sign | 2–3 y | 1/3 | P3, triggered by infection; echo and ECG normal |
| Hypotonia; Neonatal hypotonia; Persistent head lag; Poor head control | Sign | Neonatal | 1–2/3 | P1 at discharge; MedGen terms |
| Lower limb hyperreflexia | Sign | Neonatal | 1/3 | P1 |
| Feeding difficulties; Poor suck; Weak cry; Failure to thrive | Symptom | Neonatal | 2/3 | P1 poor weight gain; P2 weak cry, poor feeding, weight loss |
| Gastroesophageal reflux (with aspiration) | Sign | Neonatal | 1/3 | P1 on barium swallow |
| Elevated circulating AST/ALT; Elevated GGT | Lab | Neonatal/childhood | 2–3/3 | P1 AST 574, ALT 315, GGT 538; P3 3–4× upper limit, then normalized |
| Hepatomegaly; Micro- and macrovesicular hepatic steatosis | Sign/pathology | Infancy | 1/3 | P2, at autopsy |
| Increased variability in muscle fiber diameter; increased muscle lipid; Mitochondrial swelling | Pathology | — | 2/2 biopsied | P2 at autopsy; P3 deltoid with lipid droplets and occasional atrophy; no ragged-red or COX-negative fibers |
| Elevated CK | Lab | 2 y | 1/3 | P3 |
| 3-Methylglutaconic aciduria | Lab | 2 y | 1/3 | P3: 154 µmol/mmol creatinine (normal <19) during crisis, normal between crises; first report in this disease (PMID 31497476) |
| Low free carnitine | Lab | 2 y | 1/3 | P3: 6.5 µM (normal 19–48) |
| Seizure-like EEG (epileptiform changes) | Lab | Infancy | 1/3 | P2 |

- **Severity:** Variable, even within one family. "P1 is a healthy 20 year-old man whereas P2 died at 2 months of age" (PMID 23814038).
- **Course:** Episodic metabolic crises with recovery (P1, P3), or progressive fatal decline (P2).
- **Quality of life:** No EQ-5D, SF-36 or similar data. The survivors had normal development: P1 completed 12 years of school and plays sport; P3 at age 4 attended preschool and ballet. Burden falls mainly in the crises, which need ICU care and ventilation.

## 4. Genetic and molecular information

- **Gene:** LYRM4 (HGNC:21365; Ensembl ENSG00000214113; NCBI Gene 57128; 6p25.1; RefSeq NM_020408; UniProt Q9HD34). Aliases: ISD11, C6orf149, CGI-203 (HGNC REST; NCBI Gene).
- **Protein:** ISD11 is a small LYR-motif protein in the mitochondrial matrix. It binds the cysteine desulfurase NFS1 and acyl-ACP (NDUFAB1) (PMIDs 28634302, 29097656).

**Pathogenic and reported variants**

| Variant (NM_020408) | Protein | Zygosity / family | ClinVar | Population frequency | Evidence |
|---|---|---|---|---|---|
| c.203G>T | p.Arg68Leu (R68L); yeast equivalent R71L | Homozygous; Lebanese/Syrian consanguineous family (2 patients) | VCV000102450, **Pathogenic** (no assertion criteria; OMIM submission, 2013); rs587777218; GRCh38 chr6:5216622 | Absent from dbSNP v132, 1000 Genomes, EVS and 172 ethnically matched control chromosomes (PMID 23814038) | Partial yeast rescue; desulfurase activity strongly reduced; ISD11 undetectable in patient muscle and liver |
| c.92A>G | p.Tyr31Cys (Y31C) | Homozygous; non-consanguineous Portuguese family (1 patient) | VCV004748972, **Uncertain significance** (single submitter, evaluated 2025-02-14); GRCh38 chr6:5216733 | Absent from 100 Portuguese alleles, dbSNP, EVS and gnomAD (PMID 31497476) | In silico deleterious, conserved residue, parents carriers; no functional assay |

- **Classification discrepancy:** The p.Tyr31Cys variant was called "probably pathogenic" in the case report but is listed as VUS in ClinVar.
- **Variant class:** Only missense variants are known. Splicing of c.203G>T, which sits five bases from the exon 2/intron 2 boundary, was normal in fibroblasts (PMID 23814038). No truncating patient variants have been reported, which may mean complete loss is not viable; this is inferred from the essentiality of ISD11 in yeast (PMIDs 16341090; Wiedemann 2006, PMC1356349).
- **Origin and mechanism:** Germline; loss of function (hypomorphic) with recessive inheritance.
- **Large deletions:** ClinVar has many pathogenic 6p25.1 copy-number losses spanning LYRM4. These are heterozygous, are usually attributed to FARS2/COXPD14 or 6p deletion syndromes, and are not COXPD19 by themselves. A deletion in trans with a point variant is theoretically possible but has not been reported.
- **Candidate-gene caution:** A 2021 JIMD abstract reported a homozygous LYRM4 missense variant from trio exome sequencing that was ruled out. Mitochondrial function was rescued by wild-type CRLS1 but not by wild-type LYRM4 (https://onlinelibrary.wiley.com/doi/10.1002/jimd.12458). A LYRM4 variant needs functional support.
- **Modifier genes:** None established. P1 was also homozygous for COX10 p.Asp31Glu, which the authors judged "unlikely" to explain the phenotype. It cannot explain the P1/P2 difference, because P2 was heterozygous for it (PMID 23814038).
- **Epigenetics and chromosomal abnormalities:** No data are specific to COXPD19.

## 5. Environmental information

- **Toxins, lifestyle factors:** None known.
- **Infections:** Viral infections (RSV, HHV-6) and febrile illness act as triggers, not causes (PMID 31497476).

## 6. Mechanism and pathophysiology

**Causal chain**

1. **Homozygous LYRM4 missense variant** (p.R68L or p.Y31C) *results in* a destabilized or poorly interacting ISD11 protein. ISD11 was undetectable in patient muscle and liver (demonstrated for R68L; PMID 23814038). Alanine mutations at ISD11 helix-3 residues including Arg68 "leads to its compromised interaction with NFS1" (PMID 26342079). For Y31C the effect is inferred.
2. **ISD11 loss** *leads to* reduced NFS1 L-cysteine desulfurase activity. The ISD11–ACP pair has "regulatory rather than catalytic roles" (PMID 29097656), and without it NFS1 aggregates or is unstable (yeast, PMID 16341090; human cells, PMID 26342079). With R68L, desulfurase activity was grossly reduced, reaching about 13% of wild type with ISCU and frataxin added (in vitro, PMID 23814038).
3. **Reduced persulfide supply** *results in* impaired de novo [2Fe-2S] assembly on the ISCU scaffold within the NFS1–ISD11–ACP–ISCU–frataxin core complex (structural and biochemical work: PMIDs 27519411, 28634302, 29097656, 26016389). This early-step block affects **all downstream Fe–S proteins**.
4. **The Fe–S protein deficiency branches into:**
   - **4a.** Loss of Fe–S subunits of **complex I** (NDUFS/NDUFB8), **complex II** (SDHB) and **complex III** (Rieske UQCRFS1). These *lead to* combined CI/CII/CIII deficiency in muscle and liver (patient tissue, PMID 23814038). Complex IV is reduced secondarily in some tissues (P2 muscle 11%; P3 muscle 31%); the mechanism is inferred, possibly supercomplex or heme effects.
   - **4b.** Loss of **mitochondrial aconitase (ACO2)**, which *leads to* a TCA-cycle block (patient tissue; knockdown cells, PMID 19454487).
   - **4c.** Loss of **cytosolic aconitase/IRP1** activity and activation of IRP1 RNA binding, which *lead to* disordered cellular iron homeostasis. ISD11 knockdown caused "abnormal punctate ferric iron accumulations" (in vitro, PMID 19454487). Mitochondrial iron and ROS accumulated with R68L (PMID 26342079). Patient liver showed mildly increased iron (PMID 23814038).
   - **4d.** Loss of **ferrochelatase**, an Fe–S enzyme, which was undetectable in P2 muscle and liver; any effect on heme synthesis is inferred.
   - **4e.** Possible lipoate-dependent enzyme effects (PDH, 2-oxoglutarate dehydrogenase) were not measured. PDH was normal in fibroblasts.
5. **The OXPHOS and TCA block** *results in* a shift to glycolysis, raised NADH/NAD⁺ and **lactic acidosis**, with high lactate in blood, CSF and urine and on brain MRS. Ketosis and 3-MGA (P3) are downstream markers of mitochondrial dysfunction; their mechanism here is inferred.
6. **Energy failure in high-demand tissues** (liver, skeletal and respiratory muscle, brain) *leads to* hepatopathy and steatosis, hypotonia, respiratory insufficiency and stridor, and, under infection or catabolic stress, **acute decompensation** (cardiorespiratory arrest, P3). The tissue link is inferred from the biochemistry.
7. **Tissue specificity:** Fibroblasts were largely spared (CI–CIV mostly 45–181% of control; MyoD myotubes did not unmask a defect). Muscle and liver were severely affected. This explains why fibroblast testing can miss the diagnosis (PMID 23814038).

**Mechanism details**
- **Pathways:** Mitochondrial Fe–S cluster assembly (ISC pathway); respiratory electron transport; TCA cycle; cellular iron homeostasis (IRP/IRE). ACP binding ties ISD11 to mitochondrial fatty-acid synthesis: Cory 2017 describes "a lock-and-key model in which LYR proteins associate with acyl-ACP as a mechanism for fatty acid biosynthesis" (PMID 28634302).
- **Protein structure:** "a pair of ISD11 subunits form the dimeric core of the SDA complex" and "the 4'-phosphopantetheine-conjugated acyl-group of ACP occupies the hydrophobic core of ISD11" (PMID 28634302). The N-terminal 10 residues and the LYR motif are needed for mitochondrial targeting and a stable active complex with NFS1 (PMID 28271877).
- **Other roles of the NFS1–ISD11 complex:** Sulfur donation for tRNA thiolation (Trypanosoma, PMID 20442400) and for molybdenum cofactor synthesis via MOCS3 (PMID 18650437). Whether these are disturbed in patients is not known.
- **Immune involvement:** None described.
- **Omics, single-cell and CRISPR data:** None specific to COXPD19.
- **Suggested GO biological process labels:** iron-sulfur cluster assembly; cysteine desulfurase activity (molecular function); mitochondrial respiratory chain complex I assembly; cellular iron ion homeostasis; tRNA thio-modification.
- **Suggested CL labels:** hepatocyte; skeletal muscle fiber (myocyte); neuron.

## 7. Anatomical structures affected

- **Primary organs:** Skeletal muscle and liver, both with severe biochemical deficiency. Respiratory involvement (respiratory musculature and airway, with stridor and ventilatory failure) and brain (CSF and MRS lactate, EEG changes) are also seen.
- **Heart:** Clinically spared in the reported patients (normal echo and ECG in P2 and P3).
- **Body systems:** Metabolic, respiratory, hepatic/digestive, neuromuscular, nervous.
- **Tissue-level findings:** P2 autopsy liver showed micro- and macrovesicular steatosis, nodulation, reduced glycogen and mildly increased iron. Electron microscopy of muscle and liver showed "swollen, pleomorphic mitochondria with sparse cristae" (PMID 23814038).
- **Subcellular (suggested GO cellular component labels):** mitochondrial matrix; iron-sulfur cluster assembly complex; nucleus (NCBI Gene notes nuclear localization as well).
- **Suggested UBERON labels:** skeletal muscle tissue; liver; brain; cerebrospinal fluid; larynx/airway.
- **Lateralization:** Not applicable; the disease is systemic.

## 8. Temporal development

- **Onset:** Neonatal (day 1 to 8 weeks: P1, P2) or early childhood (2 years: P3). Onset is acute, as a metabolic or respiratory crisis.
- **Course:**
  - Episodic crises triggered by infection, with full recovery between episodes (P1, P3).
  - Progressive fatal deterioration in infancy (P2): "Her clinical condition progressively deteriorated and she succumbed at 12 weeks of age" (PMID 23814038).
- **Remission:** Spontaneous clinical recovery in two of three patients. P1 was healthy at age 20.
- **Critical periods:** The neonatal and infant period and intercurrent infections; this is the window for supportive and metabolic intervention.
- **Staging:** None defined.

## 9. Inheritance and population

- **Inheritance:** Autosomal recessive (homozygous patients, carrier parents; PMIDs 23814038, 31497476).
- **Prevalence and incidence:** Unknown. Three patients have been published; P3 was described as "the third case of LYRM4 deficiency worldwide" (PMID 31497476). No later patient reports were found in PubMed through November 2026.
- **Penetrance and expressivity:** Penetrance among homozygotes appears complete for a biochemical phenotype. Expressivity is highly variable, even within one family with the same genotype.
- **Anticipation and mosaicism:** None reported.
- **Founder effects:** None established. One variant per family: R68L in a Lebanese/Syrian family, Y31C in a Portuguese family.
- **Consanguinity:** A factor in the first family.
- **Carrier frequency:** Unknown; both variants were absent from population databases.
- **Sex:** 1 male (P1) and 2 females (P2, P3); too few to judge.

## 10. Diagnostics

- **Laboratory:**
  - Blood lactate and pyruvate (P2 pyruvate 0.13 mmol/L) and blood gases.
  - CSF lactate.
  - Urine organic acids: lactate, ketones, 3-MGA, 3-OH-isovalerate, 3-hydroxymethylglutarate.
  - Plasma carnitine; liver enzymes; CK (PMIDs 23814038, 31497476).
- **Imaging:** Brain MRI may be normal; **proton MRS shows a lactate doublet** (P2).
- **Electrophysiology:** EEG may show epileptiform changes (P2); ECG and echo were normal.
- **Biopsy and enzymology:** This is the key test. Measure respiratory chain enzymes in **skeletal muscle and liver**, relative to citrate synthase.

  | Patient / tissue | CI | CII | CIII | CIV | CS |
  |---|---|---|---|---|---|
  | P2 muscle (Lim 2013) | 4% | 8% | 5% | 11% | 166% |
  | P3 muscle (Coelho 2019) | 40% | 23% | 50% | 31% | Elevated |

  - **Fibroblasts can be normal**, so testing them alone may miss the diagnosis.
  - Western blot shows loss of NDUFS3/NDUFB8, SDHB, UQCRFS1 and ISD11, plus reduced aconitase 1/2 and ferrochelatase.
  - Histology shows lipid accumulation and fiber-size variability, without ragged-red or COX-negative fibers.
- **Genetic testing:**
  - Exome or genome sequencing (Lim used "MitoExome"), or mitochondrial/nuclear OXPHOS gene panels that include LYRM4. Genomics England PanelApp rates LYRM4 green on a "Likely inborn error of metabolism" panel (https://panelapp.genomicsengland.co.uk/panels/467/gene/LYRM4/).
  - Single-gene testing for cascade or familial testing.
  - Homozygosity mapping in consanguineous families: the shared 6p25 region pointed to LYRM4.
  - mtDNA testing serves only to exclude other causes.
  - CMA is relevant only for a possible deletion in trans.
- **Functional confirmation:** Yeast isd11Δ complementation, or NFS1–ISD11 desulfurase assays (PMID 23814038); also see the CRLS1 caution in Section 4.
- **Differential diagnosis:**
  - Other Fe–S assembly disorders: NFS1 (a recurring NFS1 variant causes "a mitochondrial disorder with variable intra-familial patient outcomes", PMID 33457206); ISCU, FXN, FDX2, NFU1/BOLA3/IBA57/ISCA2 (multiple mitochondrial dysfunction syndromes).
  - Other COXPD types, and complex I/II/III deficiencies.
  - Causes of 3-MGA aciduria, such as TAZ, SERAC1 and CLPB (inferred; not retrieved for this disease).
  - Sepsis and neonatal respiratory distress.
- **Diagnostic criteria:** No disease-specific criteria. General mitochondrial disease criteria apply; not retrieved here.
- **Screening:** No newborn screening. Carrier and cascade testing are possible in known families.

## 11. Outcome and prognosis

- **Mortality:** 1 of 3 died, at 12 weeks (P2). Survival rates and life expectancy cannot be estimated.
- **Long-term outcome in survivors:**
  - P1 had normal neurodevelopment and was healthy at 20 years.
  - P3 was normal at 4 years, with no neurological involvement "so far."
- **Complications:**
  - Recurrent lactic acidosis crises.
  - Respiratory failure needing ventilation; P3's first episode needed 5 days of mechanical ventilation.
  - Aspiration; hepatic steatosis; cardiorespiratory arrest.
- **Prognostic factors:** None validated. In the reported cases, deeper tissue deficiency (P2: CI–CIII ≤11% in muscle and liver, versus P1's milder liver values) went with death. This is an observation from n=2, not a validated predictor.
- **Quality-of-life measures:** No data.

## 12. Treatment

- **No disease-specific or approved therapy exists, and no clinical trials were found.**
- **Supportive and acute care:**
  - Ventilatory support and correction of acidosis.
  - IV glucose-containing fluids during catabolic states. Coelho advises caution and notes IV 5% dextrose in saline (PMID 31497476).
  - Antibiotics for infection.
  - Nutrition and anti-reflux care.
  - Avoiding fasting.
- **Cofactors:** Oral L-carnitine was given to P3 for low free carnitine and later stopped. No benefit beyond correcting the carnitine level was reported.
- **Proposed but untested:** Sulfur-donor supplementation, "providing a sulfur-donor such as cysteine or N-acetyl cysteine to patients" (PMID 23814038). Coelho also raised it but did not give it (PMID 31497476). There are no efficacy data.
- **Gene, cell and RNA therapy; pharmacogenomics:** None reported.
- **Suggested NCIT intervention labels:** mechanical ventilation; intravenous fluid therapy (dextrose); levocarnitine; acetylcysteine (investigational/hypothetical); supportive care.

## 13. Prevention

- **Primary:** Genetic counseling for families, carrier testing of relatives, and prenatal or preimplantation diagnosis once the familial variants are known. Recurrence risk for carrier couples is 25% per pregnancy (standard autosomal recessive).
- **Secondary:** Early metabolic evaluation of infants with unexplained lactic acidosis and stridor or respiratory distress, especially in consanguineous families.
- **Tertiary:**
  - Emergency "sick-day" protocols with early IV dextrose during infection or fever, and avoiding catabolism (PMID 31497476).
  - Prompt treatment of infections.
  - Routine immunization, inferred from the infection-triggered crises; no disease-specific vaccine data.
- **Public health and environmental measures:** Not applicable.

## 14. Other species and natural disease

- **Orthologs (NCBI Gene):**
  - Mouse *Lyrm4* (Gene ID 380840)
  - Cattle *LYRM4* (614011)
  - Chicken *LYRM4* (420874)
  - *Drosophila melanogaster* *bcn92*/Isd11 (31186)
  - *S. cerevisiae* *ISD11*/YER048W-A (856774)
  - *S. pombe* *isd11* (2539888)
- **Conservation:** ISD11 is eukaryote-specific, but it can bind bacterial IscS (PMID 27427956). R68 is conserved from yeast to vertebrates (PMID 23814038).
- **Natural animal disease:** No OMIA or veterinary disease reports found. A chicken immune-trait GWAS mentioned LYRM4 (PMID 26853217), but this is not a disease model.
- **Zoonotic or cross-species transmission:** Not applicable.

## 15. Model organisms

- **Yeast (*S. cerevisiae*):**
  - Isd11 is essential. Its loss blocks Fe–S assembly on Isu, and Nfs1 aggregates without Isd11 (Adam 2006, **PMID 16341090**; Wiedemann 2006, EMBO J, PMC1356349).
  - In the patient-variant model, isd11Δ cells carrying R71L (the yeast equivalent of R68L) showed reduced fitness on SC, SGal, SAce and YPD media (P<0.02); "the mutant protein only partially rescued the growth defect" (PMID 23814038).
  - This model recapitulates the respiratory and Fe–S defect.
- **Human cell lines:**
  - ISD11 RNAi inactivated both aconitases, activated IRP1 and caused iron deposits (PMID 19454487).
  - The R68L mutant in human cells raised mitochondrial iron and ROS and lowered respiratory complex activity (PMID 26342079).
- **E. coli:** The iscS-complementation and recombinant-complex system gave about 30% growth recovery with R68L versus about 85% with wild type (PMID 23814038). The NFS1–ISD11–ACP complex co-purifies from E. coli (PMID 28233492).
- **Trypanosoma brucei:** Isd11 is essential for cytosolic and mitochondrial tRNA thiolation (PMID 20442400).
- **Drosophila:** Fly Nfs1/Isd11/IscU core complex reconstituted biochemically (PMID 29491838). I found no in vivo Isd11 knockdown phenotype.
- **Mouse:** No Lyrm4 knockout or knock-in phenotype was retrievable; IMPC and MGI queries returned nothing. This is a gap, and an in vivo mammalian model has not been described in the retrieved literature.
- **Limitations:** None of the models reproduces the tissue specificity (muscle and liver affected, fibroblasts spared) or the variable, crisis-driven clinical course.

---

## Key sources

- Lim SC et al. Hum Mol Genet 2013;22:4460–73. PMID 23814038. https://pmc.ncbi.nlm.nih.gov/articles/PMC3888131/
- Coelho MP et al. JIMD Rep 2019;49:11–16. PMID 31497476. https://pmc.ncbi.nlm.nih.gov/articles/PMC6718106/
- Saha PP et al. J Biol Chem 2015. PMID 26342079
- Shi Y et al. Hum Mol Genet 2009. PMID 19454487
- Friemel M et al. Biochemistry 2017. PMID 28271877
- Cory SA et al. PNAS 2017. PMID 28634302
- Boniecki MT et al. Nat Commun 2017. PMID 29097656
- Gakh O et al. J Biol Chem 2016. PMID 27519411
- Adam AC et al. EMBO J 2006. PMID 16341090
- Paris Z et al. J Biol Chem 2010. PMID 20442400
- Hershkovitz T et al. Mol Genet Metab Rep 2021. PMID 33457206 (NFS1, differential diagnosis)
- MedGen 816385: https://www.ncbi.nlm.nih.gov/medgen/816385
- ClinVar VCV000102450 and VCV004748972
- HGNC LYRM4 record (genenames.org REST)
- Genomics England PanelApp: https://panelapp.genomicsengland.co.uk/panels/467/gene/LYRM4/
- JIMD 2021 abstracts (CRLS1/LYRM4 exclusion): https://onlinelibrary.wiley.com/doi/10.1002/jimd.12458

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 22 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 14 |
| Quoted claims found in source | 8 |
| Quoted claims **not** found in source | 6 |
| References weighed for topical relevance | 22 |
| On topic | 6 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:23814038` *(abstract only)*: "NFS1 has a residual l-cysteine desulfurase activity which is sufficient to retain the viability of the patient"
  - closest text in source: "Our in vitro studies showed that the l-cysteine desulfurase activity of NFS1 was barely present when co-expressed with mutant ISD11"
- `PMID:23814038` *(abstract only)*: "P1 is a healthy 20 year-old man whereas P2 died at 2 months of age"
  - closest text in source: "Sanger sequencing identified the same mutation in his similarly affected cousin, who had a more severe phenotype and died while a neonate"
- `PMID:23814038` *(abstract only)*: "swollen, pleomorphic mitochondria with sparse cristae"
  - closest text in source: "Proteins with ISCs (called iron-sulfur or Fe-S proteins) are present in mitochondria, the cytosol, the endoplasmic reticulum and the nucleus"
- `PMID:23814038` *(abstract only)*: "Her clinical condition progressively deteriorated and she succumbed at 12 weeks of age"
  - closest text in source: "The differences in biochemical and clinical features between the two patients may relate to limited availability of cysteine in the newborn period and suggest a potential approach to therapy."
- `PMID:23814038` *(abstract only)*: "providing a sulfur-donor such as cysteine or N-acetyl cysteine to patients"
  - closest text in source: "The differences in biochemical and clinical features between the two patients may relate to limited availability of cysteine in the newborn period and suggest a potential approach to therapy."
- `PMID:23814038` *(abstract only)*: "the mutant protein only partially rescued the growth defect"
  - closest text in source: "Mutant ISD11 only partially complemented for an ISD11 deletion in yeast"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 4 |
| Resolved | 1 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014269` (2 mentions) - the report calls it "MONDO"; MONDO calls it **combined oxidative phosphorylation deficiency 19**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `ORPHA`.