---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-03T19:18:34.830193'
end_time: '2026-11-03T19:22:45.579634'
duration_seconds: 250.75
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Renal-Hepatic-Pancreatic Dysplasia 2
  mondo_id: MONDO:0014174
  category: Mendelian
  causal_genes: NEK8
  omim_id: OMIM:615415
  synonyms: renal-hepatic-pancreatic dysplasia type 2; NEK8 renal-hepatic-pancreatic
    dysplasia; renal-hepatic-pancreatic dysplasia caused by mutation in NEK8
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
  web_search_requests: 15
  num_turns: 25
  total_cost_usd: 2.5544200999999997
  session_id: 1f2f951a-c754-4a60-beba-18bf67c52283
  stop_reason: end_turn
  permission_denials: 4
  denied_tools:
  - Bash
  assistant_text_blocks: 3
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderAuthError
  status_code: 403
  remedy: the API key is missing, invalid, or lacks access to this endpoint
  retryable: false
- provider: claude_code
  succeeded: true
citation_count: 18
reference_validation:
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 18
  on_topic: 10
  validator_version: 0.5.1
term_validation:
  total_terms: 33
  verified: 30
  not_found: 0
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 4
  labels_matching: 1
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: GO:0072372
    reported_labels:
    - Subcellular:** primary cilium
    ontology_label: GO_0072372
  labels_variant: 2
  obsolete_terms:
  - term_id: GO:0072372
    ontology_label: GO_0072372
    replaced_by: GO:0005929
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Renal-Hepatic-Pancreatic Dysplasia 2
- **MONDO ID:** MONDO:0014174 (if available)
- **Causal gene(s):** NEK8
- **OMIM:** OMIM:615415
- **Synonyms:** renal-hepatic-pancreatic dysplasia type 2; NEK8 renal-hepatic-pancreatic dysplasia; renal-hepatic-pancreatic dysplasia caused by mutation in NEK8
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Renal-Hepatic-Pancreatic Dysplasia 2** covering all of the
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

Pulling the NEK8 literature from PubMed to check identifiers before I write the report.

Checking one more source, a review of NEK8 cases reported 2013–2020, then I'll write the report.

# Research report: Renal-Hepatic-Pancreatic Dysplasia 2 (RHPD2), caused by NEK8

> **Provenance.** This report was put together by an AI agent (Claude Code) on 2026-11-03. PubMed E-utilities needed approval in this session and I didn't have it, so citations come from web search plus memory, cross-checked against two committed repository sources (`cache/clingen/gene_validity.csv` and the dismech Nephronophthisis deep-research report). Each PMID is tagged by how it was checked:
> - **[confirmed]**: a PubMed URL, or a PMC/MGI/ZFIN record, matched title and PMID.
> - **[lead]**: the PMID was read off a secondary site and not opened on PubMed.
> - **[memory]**: I recalled it; it is unverified.
>
> **None of the "quotes" below are verified exact abstract strings.** They are paraphrases returned by the search tool. Before they become YAML evidence, fetch each with `just fetch-reference PMID:…` and take the snippet from `references_cache/`.

---

## 1. Disease information

RHPD2 is an autosomal recessive ciliopathy caused by **biallelic variants in *NEK8*** (NIMA-related kinase 8; HGNC:13387; also called NPHP9). Its core features are:
- enlarged cystic or dysplastic kidneys;
- ductal plate malformation and cysts in the liver;
- pancreatic cysts and dysplasia;
- frequent congenital heart disease and laterality defects.

Most reported cases are lethal before or around birth. The original report described three fetuses from one consanguineous family with "enlarged cystic kidneys, liver and pancreas" and developmental heart disease, carrying a homozygous *NEK8* nonsense variant (Frank et al. 2013, *Hum Mol Genet* 22:2177–85, doi:10.1093/hmg/ddt070; PMID 23418306 **[lead]**, from the GO annotation page for NEK8).

| Identifier | Value | Source / status |
|---|---|---|
| MONDO | MONDO:0014174 "renal-hepatic-pancreatic dysplasia 2" | repo entry and stub |
| OMIM | 615415 (RHPD2) | task brief; also the LOVD and Pharos records |
| Allelic OMIM | 613824, Nephronophthisis 9 (NPHP9) | **[memory]** for the number |
| Orphanet | ORPHA:294415, renal-hepatic-pancreatic dysplasia (umbrella term, also called Ivemark II) | **[lead]**, from an aggregator. Check on orpha.net. That aggregator maps the umbrella to MONDO:0017417. |
| ClinGen | NEK8 / RHPD2 / AR / **Definitive** (SOP8, Kidney Cystic and Ciliopathy Disorders GCEP, 2021-09-08). `CGGV:assertion_6888a91a-6589-42a9-9622-553b4918bed6-2021-09-08T160000.000Z` | **structured database, confirmed** in `cache/clingen/gene_validity.csv` |
| ClinGen (allelic, dominant) | NEK8 / ADPKD (MONDO:0004691) / AD / **Strong** (2024-01-08). `CGGV:assertion_32e19522-…-2024-01-08T170000.000Z` | **confirmed**, same CSV |
| ICD-10 / ICD-11 / MeSH | No specific code found. Probably falls under Q61.x (cystic kidney disease) or Q44.6 (cystic disease of the liver). | not checked |

**Synonyms:** RHPD type 2; NEK8-related RHPD; renal-hepatic-pancreatic dysplasia caused by mutation in NEK8. The umbrella term also goes by Ivemark II syndrome and renohepatopancreatic dysplasia.

**Source class:** case reports and small families only (aggregated disease level). There are no registries or EHR cohorts.

**Lump/split decisions to surface (not quietly resolved here):**
1. **Within the RHPD umbrella**, RHPD1 is the *NPHP3* form (Bergmann et al. 2008, *Am J Hum Genet*; PMID 18371931 **[memory]**). RHPD2 is the *NEK8* form. The two are separate gene-defined MONDO terms, so separate entries are consistent with design-decisions §3a/§18 Mendelian splitting. An umbrella grouping would be optional.
2. **Within the NEK8 allelic series:**
   - **RHPD2** (AR, severe, multi-organ);
   - **NPHP9** (AR, juvenile nephronophthisis; weak evidence: one homozygous case among 588 screened in Otto 2008);
   - **NEK8-related autosomal dominant PKD** (heterozygous kinase-domain missense, dominant negative; Claus 2023).

   Gunther et al. 2023 argue that RHPD2 is "a multisystemic disorder with variable expressivity" rather than always lethal, which leans toward lumping AR NEK8 disease into one spectrum. MONDO and OMIM still keep RHPD2 and NPHP9 apart. My recommendation: curate RHPD2 as the disease, with NPHP9 noted as an allelic, milder AR phenotype rather than a `has_subtypes` row, because NPHP9 has its own MONDO/OMIM term. AD-PKD should be its own entry or stay inside the existing ADPKD entry. This is a curator's call.

## 2. Etiology

- **Cause:** biallelic germline loss-of-function or hypomorphic *NEK8* variants. Monogenic, autosomal recessive.
- **Genetic risk factors:** consanguinity in several families (Frank 2013, plus Saudi cohorts in Al-Hamed 2016). Nothing else is known.
- **Environmental, protective, and gene-environment factors:** none reported. This is an evidence gap, not a negative finding.

## 3. Phenotypes

Sources are case series only, with about 17 reported patients by 2022 (Gunther et al. 2023, "Renal-hepatic-pancreatic dysplasia type 2: Perinatal lethal condition or a multisystemic disorder with variable expressivity", PMC10094071; PMID not retrieved). The HPO IDs below are **unverified leads**. Look each one up before binding.

| Phenotype | Onset | Frequency (qualitative) | HPO lead | Key source |
|---|---|---|---|---|
| Enlarged cystic or multicystic dysplastic kidneys | Fetal | Core feature | HP:0000107 Renal cyst; HP:0000003 Multicystic kidney dysplasia | Frank 2013; Grampa 2016 |
| Renal hypodysplasia (missense genotypes) | Fetal | Some cases | HP:0000089 Renal hypoplasia | Grampa 2016 |
| Oligohydramnios / Potter sequence | Fetal | Frequent in lethal cases | HP:0001562 Oligohydramnios | inferred from the perinatal-lethal course; check |
| Hepatic cysts, ductal plate malformation, fibrosis | Fetal to infancy | Core feature | HP:0001407 Hepatic cysts; HP:0001395 Hepatic fibrosis | Frank 2013 |
| Paucity of bile ducts | Fetal | Some cases | look up | Grampa 2016 ("reduced bile ducts") |
| Neonatal cholestasis progressing to end-stage liver disease | Neonatal | Survivors | HP:0001396 Cholestasis | 2020 sibling report (title only; PMID not retrieved) |
| Pancreatic cysts and dysplasia | Fetal | Core feature | HP:0001737 Pancreatic cysts | Frank 2013 |
| Congenital heart disease (septal defects, thickened septum) | Fetal | Frequent | HP:0001629 VSD; HP:0001631 ASD | Frank 2013; Grampa 2016; Rajagopalan 2016 |
| Situs inversus / heterotaxy | Fetal | Some cases | HP:0001696 Situs inversus totalis | Grampa 2016 |
| End-stage kidney disease in childhood | Childhood | Survivors | HP:0003774 Stage 5 CKD | Rajagopalan 2016; Gunther 2023 |

- **Quality of life:** there are no QoL data. In survivors, the burden comes from dialysis, transplant, and liver failure.
- **Pediatric framing:** this is a prenatal or neonatal entity. Variable expressivity separates fetal lethality from childhood survival with progressive kidney and liver failure. NPHP9 (juvenile nephronophthisis) and AD-PKD (neonatal-onset cystic kidneys without consistent extra-renal disease, per Claus 2023) are different clinical entities from the same gene.

## 4. Genetics and molecular information

- **Gene:** *NEK8*, 17q11.2, HGNC:13387 (`hgnc:13387` in repo form). The protein is a serine/threonine kinase: an N-terminal NIMA-like kinase domain followed by C-terminal RCC1 repeats.
- **Variant classes:**
  - Nonsense and truncating variants, often homozygous, give the enlarged-cystic-organ RHPD2 picture.
  - Missense variants give hypodysplasia (Grampa 2016: "missense and nonsense mutations were associated with hypodysplasia and enlarged cystic organs, respectively", paraphrase).
  - Compound-heterozygous variants were found in siblings who survived to ESRD with hepatic and cardiac anomalies (Rajagopalan et al. 2016, *Am J Med Genet A*; PMID not retrieved, **[memory]** 27530628).
  - NPHP9 variants sit in the RCC1 repeats, one in the same repeat as the mouse *jck* allele (Otto et al. 2008, *JASN* 19:587–92, **PMID 18199800 [confirmed]**). The search summary garbled the variant names, so take them from the abstract.
  - **Dominant:** heterozygous kinase-domain missense p.Arg45Trp (recurrent, often de novo, including mosaic cases), p.Ile150Met and p.Lys157Gln cause AD-PKD in 12 families through a proposed dominant-negative effect (Claus et al. 2023, *Kidney Int* 104:995–1007, doi:10.1016/j.kint.2023.07.021, PMC10592035; PMID **[memory]** 37598857).
  - Codon 45 is also, from memory, the site of the Frank 2013 nonsense variant (p.Arg45\*). This needs checking. If true, the same codon gives AR truncation and AD missense disease.
- **Functional effect in RHPD2:** loss of function. Missense versus truncating alleles affect YAP differently (Grampa 2016).
- **ACMG, gnomAD, ClinVar:** not checked in this session.
- **Somatic vs germline:** RHPD2 is germline. Mosaicism has been reported only for the dominant R45W allele (Claus 2023).
- **Modifier genes, epigenetic changes, chromosomal abnormalities:** none reported.
- **Second cohort source:** an "inferred novel variant in NEK8" (deduced from parental DNA only) in 44 Saudi families with antenatal cystic kidney disease (Al-Hamed et al. 2016, *J Med Genet* 53:338–47, PMC4853542; PMID **[memory]** 26862157). This is weak, indirect support.

## 5. Environmental information

Not applicable. No environmental, lifestyle, or infectious contributors are reported.

## 6. Mechanism and pathophysiology

**Causal chain.** Steps marked *(inferred)* are not demonstrated in human tissue.

1. Biallelic *NEK8* loss-of-function variants **lead to** absent or defective NEK8 kinase in the ciliary inversin compartment.
   - NEK8 is a core member of the INV complex with INVS (NPHP2), NPHP3 and ANKS6.
   - ANKS6 binds the NEK8 kinase domain to activate it, and needs NEK8 to reach that compartment (Czarnecki et al. 2015, *Nat Commun* 6:6023, PMID 25599650 **[lead]**; model organism and in vitro).
2. Loss of INV-complex kinase signaling **results in** Hippo pathway dysregulation.
   - NEK8 binds TAZ and drives it into the nucleus (Habbig et al. 2012, *Hum Mol Genet* 21:5528–38, **PMID 23026745 [confirmed]**; in vitro).
   - *NEK8* variants alter YAP regulation in patient fibroblasts, *Nek8*-null spheroids and *jck* kidneys (Grampa et al. 2016, *PLoS Genet* 12:e1005894, PMC4788435; PMID **[memory]** 26967905).
   - Patient fibroblasts showed lower *PKD1*/*PKD2* and higher c-MYC (Frank 2013).
3. **Branch A (kidney, liver, pancreas):** altered YAP/TAZ output and polycystin signaling **lead to** too much epithelial proliferation and failed tubule and duct differentiation, giving cystic dysplasia of kidney, biliary ductal plate and pancreatic ducts.
   - The polycystin link is supported: *Nek8*-null cells respond poorly to fluid shear, which suggests NEK8 mediates polycystin-2-dependent signaling (Manning et al. 2013).
   - Dominant R45W and K157Q reduce ciliary polycystin-2 (Claus 2023).
   - Verteporfin, a YAP inhibitor, partly rescued spheroid and zebrafish defects (Grampa 2016). That is pharmacological support for YAP as the mediator, so `directness: INDIRECT`.
4. **Branch B (laterality and heart):** NEK8 loss in node cilia **leads to** misexpression of left-sided markers, which causes heterotaxy and cardiac malformations. In *Nek8*-null mice cilia form normally but nodal signaling fails (Manning et al. 2013, *JASN* 24:100–12, **PMID 23274954 [confirmed]**; model organism).
5. **Branch C (in parallel; contribution to the human disease not yet shown):** NEK8 loss **leads to** replication stress, because without NEK8 the ATR pathway no longer holds back S-phase CDK activity. This causes DNA damage and disordered renal cell architecture, and ciliopathy alleles impair this function (Choi et al. 2013, *Mol Cell* 51:423–39, PMID 23973373 **[lead]**; model organism and in vitro).
6. Dysplasia and cysts **result in** clinical failure of the affected organs:
   - oligohydramnios and pulmonary hypoplasia lead to perinatal death *(inferred)*;
   - in survivors, ESKD, cholestatic liver failure, and heart disease.

**Ontology leads (all unverified):**
- **GO:**
  - GO:0097543 ciliary inversin compartment
  - GO:0004674 protein serine/threonine kinase activity
  - GO:0035329 hippo signaling
  - GO:0007368 determination of left/right symmetry
  - GO:0060271 cilium assembly
  - GO:0072001 renal system development
  - GO:0006974 DNA damage response
- **CL:**
  - kidney tubule epithelial cell
  - cholangiocyte (CL:1000488?)
  - pancreatic ductal cell
  - node cilia-bearing cells
- **Subcellular:** primary cilium (GO:0072372), centrosome (GO:0005813), nucleus (for TAZ/YAP).

**Omics:** none found for human RHPD2 (no GEO, single-cell or proteomics data).

## 7. Anatomical structures

- **Primary:** kidney (UBERON:0002113), liver and intrahepatic bile ducts, pancreas (UBERON:0001264).
- **Secondary:** heart (septa), body axis (situs).
- Organ involvement is bilateral and symmetric.
- The UBERON IDs are leads; look them up before binding.

## 8. Temporal development

- **Onset:** congenital. Most cases are seen on prenatal ultrasound.
- **Course:** usually perinatal death. Gunther 2023 reports, in the UTHealth abstract, that "13 [of 17] died within the perinatal period" (pregnancy to age 1).
- **Survivors** follow a progressive course:
  - death at 5 years from renal failure;
  - death at 30 months from liver and kidney failure;
  - two alive at 1 and 13 years.
- **Critical period:** the second trimester and earlier, when organ morphogenesis happens. No staging scheme exists.

## 9. Inheritance and population

- **Inheritance:** autosomal recessive (ClinGen: AR, Definitive).
- **Penetrance:** appears complete for biallelic null alleles, but expressivity varies widely.
- **Other genetic features:** no anticipation reported; consanguinity contributes. A founder effect has not been established (Saudi and other Middle Eastern families appear among the reports).
- **Prevalence:** fewer than 20 patients in the literature by 2022. Use `CASES_IN_LITERATURE` (about 17, Gunther 2023), class ULTRA_RARE. Incidence, carrier frequency and sex ratio are not reported.

## 10. Diagnostics

- **Prenatal ultrasound:** enlarged hyperechoic or cystic kidneys, oligohydramnios, cardiac defects, situs anomalies.
- **Pathology:** autopsy shows cystic dysplasia, ductal plate malformation, and pancreatic cysts and fibrosis.
- **Genetic testing:** exome or genome sequencing, or a ciliopathy / cystic-kidney gene panel. PanelApp lists *NEK8* on its Cystic kidney disease and Renal ciliopathies panels. Claus 2023 recommends including *NEK8* on PKD panels for children and adults.
- **Differential diagnosis:**
  - RHPD1 (*NPHP3*);
  - Meckel syndrome (looks for encephalocele and polydactyly);
  - ARPKD (*PKHD1*);
  - *ANKS6* and *INVS* ciliopathies;
  - Jeune / short-rib syndromes;
  - glomerulocystic disease.
- **Screening:** carrier testing and prenatal or preimplantation testing for known familial variants.
- **No GeneReviews chapter was found.** Confirm with `just check-genereviews`.

## 11. Outcome and prognosis

- **Mortality:** high perinatal mortality (13 of 17).
- **Survivors:** progress to ESKD and end-stage liver disease in childhood.
- **Prognostic factors:** a truncating versus missense genotype correlation is suggested (Grampa 2016) but not validated.
- **Biomarkers:** no prognostic biomarkers.

## 12. Treatment

There is no disease-specific therapy. Care is supportive. NCIT leads:
- dialysis;
- kidney transplantation and combined liver–kidney transplantation (NCIT:C15289 Organ Transplantation);
- cardiac surgery for structural heart defects (NCIT:C15329 Surgical Procedure);
- supportive or palliative perinatal care (NCIT:C15747 Supportive Care);
- genetic counseling (NCIT:C15240).

Verteporfin is preclinical only (spheroid and zebrafish; Grampa 2016). No clinical trials were found, though no registry search was run.

## 13. Prevention

- Genetic counseling for families: 25% recurrence risk.
- Cascade carrier testing.
- Prenatal or preimplantation genetic testing.
- Tertiary prevention: manage kidney and liver failure and refer for transplant.

## 14. Other species

No naturally occurring animal disease was found (OMIA not searched). *NEK8* is conserved in mouse (*Nek8*) and zebrafish (*nek8*).

## 15. Model organisms

| Model | Phenotype | Fidelity / limits | Source |
|---|---|---|---|
| *jck* mouse (spontaneous *Nek8* G448V missense in an RCC1 repeat) | Juvenile polycystic kidney disease; long cilia with more ciliary PC1/PC2 (secondary reports) | Kidney only; models a hypomorphic NPHP/PKD allele, not multi-organ RHPD2 | Liu et al. 2002, *Development* 129:5839, PMID 12421721 **[lead]**, from ZFIN |
| *Nek8*-null mouse | Dies at birth; randomized left-right asymmetry, heart anomalies, glomerular cysts | Reproduces laterality, heart and kidney features; liver and pancreas less described | Manning 2013, PMID 23274954 |
| *Nek8^Roc* (kinase-dead) and *Anks6^Strkr* mice | Heterotaxy, cardiopulmonary malformations, cystic kidneys | Shows that kinase activity is what matters | Czarnecki 2015 |
| Zebrafish *nek8* morphants / overexpression | Pronephric cysts; randomized heart looping; verteporfin-rescuable overexpression defects | Morpholino caveats | Liu 2002; Manning 2013; Grampa 2016 |
| Patient fibroblasts; *Nek8*-KO IMCD3 cells; 3D spheroids | Lower *PKD1*/*PKD2*, higher c-MYC; YAP imbalance; reduced ciliary PC2 (dominant alleles) | In vitro | Frank 2013; Grampa 2016; Claus 2023 |

Databases: MGI (*Nek8*), ZFIN.

---

### Gaps and to-dos before curation
- Confirm the PMIDs for Frank 2013, Grampa 2016, Claus 2023, Rajagopalan 2016, Al-Hamed 2016, Gunther 2023 and the 2020 cholestasis report. Confirm the variant nomenclature against the abstracts.
- No exact snippets have been verified yet.
- ORPHA and OMIM 613824 still need checking.
- An untracked placeholder `kb/disorders/Renal-Hepatic-Pancreatic_Dysplasia_2.yaml` (name, date and MONDO term only) is already in this worktree. I left it unchanged; no branch, commit or claim was made.

Sources:
- [Frank 2013 (CORE)](https://core.ac.uk/works/81571); [GO wiki, HUMAN:NEK8](https://gowiki.tamu.edu/wiki/index.php/HUMAN:NEK8)
- [Grampa 2016 (PMC4788435)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4788435)
- [Otto 2008 (PMC2391043)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2391043)
- [Claus 2023 (PMC10592035)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10592035)
- [Rajagopalan 2016 (Sapienza IRIS)](https://iris.uniroma1.it/handle/11573/955884)
- [Atlas of Genetics, NEK8](https://atlasgeneticsoncology.org/gene/43376/nek8)
- [Liu 2002 (ZFIN)](https://www.zfin.org/ZDB-PUB-021112-4)
- [Manning 2013 (PMC3537214)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3537214)
- [Choi 2013 (PMC3790667)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3790667)
- [Czarnecki 2015 (PMC4361001)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4361001)
- [Habbig 2012 (PubMed 23026745)](https://pubmed.ncbi.nlm.nih.gov/23026745/)
- [Al-Hamed 2016 (PMC4853542)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4853542)
- [Gunther 2023 (PMC10094071)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10094071); [UTHealth repository record](https://digitalcommons.library.tmc.edu/uthmed_docs/2211)
- [RHPD aggregator (DrugMAP)](https://drugmap.idrblab.net/data/disease/details/DIS3L6GZ)
- [PanelApp, NEK8](https://panelapp.genomicsengland.co.uk/panels/283/gene/NEK8)
- [LOVD RHPD2](https://databases.lovd.nl/shared/diseases/03935)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 18 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 33 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 4 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `GO:0072372` (1 mention) - the report calls it "Subcellular:** primary cilium"; GO calls it **GO_0072372**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0072372` (GO_0072372) (1 mention) - replaced by `GO:0005929`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0004691` (1 mention) - the report calls it "NEK8 / ADPKD"; MONDO calls it **autosomal dominant polycystic kidney disease**, and lists "ADPKD" among its other names
- `UBERON:0002113` (1 mention) - the report calls it "Primary:** kidney"; UBERON calls it **kidney**, and lists "reniculate kidney" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.