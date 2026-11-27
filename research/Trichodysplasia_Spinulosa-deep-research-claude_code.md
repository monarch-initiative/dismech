---
provider: claude_code
model: claude-haiku-5-5, claude-opus-4-8, claude-opus-5-5
cached: false
start_time: '2026-11-25T22:37:19.271623'
end_time: '2026-11-25T22:43:43.490689'
duration_seconds: 384.22
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Trichodysplasia Spinulosa
  mondo_id: MONDO:0016455
  category: ''
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: Cyclosporine-induced folliculodystrophy; TS; VATS; pilomatrix dysplasia
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
  - claude-opus-4-8
  - claude-opus-5-5
  web_search_requests: 8
  num_turns: 16
  total_cost_usd: 1.23159509
  session_id: 9ca0fbe5-6dc9-466a-a94d-bf54956678cb
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  tool_calls: 38
  retrieval_calls: 36
  assistant_text_blocks: 5
citation_count: 9
reference_validation:
  total_references: 52
  verified: 52
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 19
  quotes_valid: 18
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:35482045
  quotes_not_checkable: 1
  relevance_assessed: 52
  on_topic: 39
  off_topic: 1
  off_topic_references:
  - PMID:41458272
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 34
  verified: 27
  not_found: 0
  obsolete: 0
  unverifiable: 7
  confabulation_rate: 0.0
  labels_checked: 16
  labels_matching: 12
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0016455
    reported_labels:
    - MONDO
    ontology_label: virus-associated trichodysplasia spinulosa
  labels_variant: 3
  service_unreachable: 4
  obsolescence_unchecked: 4
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Trichodysplasia Spinulosa
- **MONDO ID:** MONDO:0016455 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** Cyclosporine-induced folliculodystrophy; TS; VATS; pilomatrix dysplasia
- **Category:** 

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Trichodysplasia Spinulosa** covering all of the
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

I'm pulling up more primary abstracts from PubMed, which a background fetch is doing now. While it runs, I'm running extra searches on epidemiology, the animal model and the mechanism.

The 40 abstracts are all read verbatim. The two PubMed-website fetches were partly unusable, so I used the E-utilities host for the 1999 Haycox record.

**1. PMID list for "trichodysplasia spinulosa" (Count = 168, all 168 retrieved)**

Retmax=150 returned the first 150 by recency. A second request with retstart=150 returned the other 18.

- First 150: 42811524, 42715570, 42260996, 42172084, 41965049, 41458272, 41259037, 40661115, 40616235, 40200820, 39612622, 39563858, 38831469, 38493799, 38434466, 38406624, 38293082, 38090399, 37799360, 37557154, 37440192, 37168025, 34662051, 37009033, 36846188, 36809091, 36577746, 36298837, 35997483, 35659843, 35573099, 35482045, 35216020, 35000075, 34835424, 34746353, 34001481, 33999949, 33895421, 33729628, 33595122, 33559344, 33364280, 33354613, 33146676, 32995002, 32785992, 32748541, 32723915, 32475005, 32060513, 31909132, 31787742, 31505316, 31450276, 31233669, 31219640, 31209897, 31190328, 31008165, 30916861, 30884172, 30632206, 30624811, 30585627, 30537287, 30531297, 30489551, 30470393, 30407150, 30390301, 30352098, 30328951, 30124403, 29806684, 29778875, 29573272, 29568287, 29028114, 28731909, 28654466, 28500640, 28326649, 28199663, 28108298, 28019062, 27990673, 27726799, 27578847, 27536719, 27510735, 27317512, 27055259, 27051806, 27034991, 27013741, 26809132, 26663358, 26630080, 26620059, 26602950, 26538801, 26519899, 26479880, 26338086, 26302170, 26239840, 26230706, 26136575, 25968129, 25809796, 25775666, 25766994, 25670407, 25471598, 25471402, 25389794, 25387582, 25348766, 25291363, 25197415, 25188537, 25059864, 25054782, 24943872, 24888895, 24887966, 24816721, 24655410, 24583997, 24481784, 24476010, 24421113, 24322674, 24315796, 24261736, 23928454, 23781946, 23650080, 23621738, 23593936, 23357733, 23330716, 23302741, 23270528, 23255626, 23076257, 23029236, 22882314, 22803598
- Last 18: 22801635, 22461085, 22351786, 22196870, 22006143, 21993271, 21941687, 21926381, 21801610, 21680290, 21251037, 21050621, 20796236, 20686659, 18186853, 17535200, 15644782, 10674379

The list includes non-TS items such as 38090399 (sebaceous filaments) and 21050621 (multiple minute digitate hyperkeratosis).

**2. Review-filtered search (Count = 119; first 60 returned; first 40 fetched)**

Fetched 40 by efetch, in the order listed. The efetch text was truncated at about 39.5k characters. I read on with the offset parameter to get the verbatim text for entries 21 to 40. Quotes are kept to 125 characters or fewer, and long titles are shortened with "...".

1. **42172084**. Oliveira JM, 2026, Rev Med Virol. "Human Polyomaviruses of Clinical Relevance: Modes of Transmission and Associated Pathologies." Review. Quote: "MCPyV with Merkel Cell Carcinoma and TSPyV with Trichodysplasia spinulosa." No case data.
2. **41965049**. Moore L, 2026, Rev Med Virol. "Updates on Trichodysplasia Spinulosa Disease." Review. Quotes: "To date, fewer than 100 cases have been reported in the literature"; "Roughly 75% of adults have IgG antibodies to TSPyV."
3. **41458272**. Hasan R, 2025, Oxf Med Case Reports. "Sorafenib-associated Trichodysplasia Spinulosa versus Follicular Hyperkeratosis: a case report." Quote: "we highlight the role of sorafenib in disrupting skin keratinization process." No age or sex in abstract.
4. **40616235**. Pande N, 2025, Pediatr Transplant. "Polyomavirus Associated Trichodysplasia Spinulosa in a Pediatric Kidney Transplant Recipient." Quotes: "a case of TS in a 10-year-old girl who underwent a deceased donor kidney transplant"; "successfully treated with a reduction in immunosuppression and the addition of leflunomide and valganciclovir." Skin biopsy positive; small T antigen gene detected in paraffin scrolls.
5. **40200820**. Hansen AM, 2025, Pediatr Transplant. "Management of Trichodysplasia Spinulosa in a Pediatric Kidney Transplant Patient With Topical Cidofovir and Oral Leflunomide." Quote: "10-year-old male with a history of kidney transplantation"; "leading to significant clinical improvement over several months."
6. **39612622**. Saribas AS, 2025, Virology. "Recent advances in discovery and functional analysis of the small proteins and microRNA expressed by polyomaviruses." Review. TS is listed among polyomavirus diseases. No case data.
7. **39563858**. Cabeza Rivera F, 2024, Clin Case Rep. "Trichodysplasia spinulosa post kidney transplant." Quote: "Early diagnosis can facilitate treatment and help avoid disease progression and complications." Case report; no details in abstract.
8. **38831469**. Thevenin KR, 2024, Virol J. "The small tumor antigen of Merkel cell polyomavirus accomplishes cellular transformation..." (shortened). Cell-line study, not patients. Quotes: "HPyV7 and TSPyV ST proteins were incapable of nuclear translocation"; "TSPyV) and Human Polyomavirus 7 (HPyV7) were not transforming when similarly assessed."
9. **38493799**. Burningham KM, 2024, J Dermatolog Treat. "Resolution of painful trichodysplasia spinulosa with topical cidofovir: case report." Quotes: "A 19-year-old immunosuppressed female presented with widespread painful, itchy bumps on the nose and face"; "symptoms resolved completely after 4 weeks of therapy with topical cidofovir 1% cream." Biopsy plus PCR confirmation.
10. **38434466**. Khalili AA, 2024, Sultan Qaboos Univ Med J. "Trichodysplasia Spinulosa." Quotes: "a biopsy-proven case of TS in a male renal transplant patient"; "managed with valgancyclovir with no obvious response."
11. **38293082**. Thevenin KR, 2024, bioRxiv preprint of PMID 38831469. Same findings as #8.
12. **38090399**. Mineroff JP, 2023, Cureus. "A Case Report of Sebaceous Filaments." Not TS. A 16-year-old with facial white spicules, treated with topical tretinoin. Listed only as a differential.
13. **37799360**. Rosa-Nieves PM, 2023, Skin Health Dis. "A case of trichodysplasia spinulosa related to ruxolitinib treated successfully with oral acitretin." Quotes: "oral acitretin showed significant improvement after 3 months"; "suppressing the JAK-signal transducer and activator of the transcription pathway's antiviral functions." Patient: 67-year-old female, post allogeneic bone marrow transplant.
14. **36809091**. Ji-Xu A, 2022, Dermatol Online J. "Trichodysplasia spinulosa: a presentation of polyomavirus infection in immunosuppressed patients." Quotes: "did not respond to topical imiquimod but improved upon treatment with valganciclovir"; "hyperproliferating inner root sheath cells containing large eosinophilic trichohyaline granules." Renal transplant recipient.
15. **36577746**. Bartley BR, 2023, Int J Dermatol. "Current treatments and emerging therapies of human polyomavirus-associated skin diseases: a comprehensive review." Quote: "the use of antivirals such as cidofovir (CDV) or valganciclovir (VGCV)." Review of treatments.
16. **36298837**. Jeles K, 2022, Viruses. "Seroprevalence of Four Polyomaviruses Linked to Dermatological Diseases..." (shortened). Quotes: "A total of 552 serum samples were analysed"; "The adulthood seroprevalence was 69.3%, 87.7%, 83.8% and 85% for MCPyV, HPyV6, HPyV7 and TSPyV, respectively." Also noted: elevated TSPyV seropositivity in the >60 group.
17. **35659843**. King JF, 2022, Cutis. "Facial Follicular Spicules: A Rare Cutaneous Presentation of Trichodysplasia Spinulosa." No abstract in the PubMed record.
18. **35482045**. Silling S, 2022, Hautarzt. "[Human polyomavirus-associated skin diseases]." German-language article with English text in the record. Quotes: "primary infection with trichodysplasia spinulosa-associated polyomavirus (TSPyV) can cause the very rare skin disease"; "Keratin spines (spicules), mainly in the center of the face, clinically characterize this disease."
19. **35000075**. Narayanan D, 2022, Virus Genes. "Trichodysplasia spinulosa polyomavirus small T antigen synergistically modulates S6 protein translation and DNA damage response pathways..." (shortened). Mechanism, cell-based. Quotes: "TSPyV sT expression exploits the DNA damage response pathway, by inducing hyperphosphorylation of ATM and 53BP1"; "sT dysregulates the S6 protein translation pathway via hyperphosphorylation of CDC2, p70 S6 kinase, S6, and PP1α."
20. **34001481**. Verlinden L, 2021, Eur J Dermatol. "Trichodysplasia spinulosa, a challenging skin disorder successfully treated with camellia sinensis 10% ointment." No abstract in the PubMed record.
21. **33999949**. Yang R, 2021, PLoS Pathog. "Characterization of ALTO-encoding circular RNAs expressed by Merkel cell polyomavirus and trichodysplasia spinulosa polyomavirus." Quotes: "circALTOs are stable, predominantly located in the cytoplasm, and N6-methyladenosine (m6A) modified"; "TSPyV) also expresses a circALTO that can be detected in infected tissues." Mechanism, not patients.
22. **33729628**. Wu Z, 2021, Rev Med Virol. "Antivirals against human polyomaviruses: Leaving no stone unturned." Review. Quotes: "Proven HPyV diseases with documented histopathology affect primarily immunocompromised hosts"; "Current clinical studies are limited by small case numbers."
23. **33559344**. Curman P, 2021, J Eur Acad Dermatol Venereol. "Trichodysplasia spinulosa: a comprehensive review of the disease and its treatment." Quotes: "The seroprevalence of TSPyV in immunocompetent adults is high"; "include topical cidofovir 3%, reduction of immunosuppression and oral valganciclovir." Review of all published cases.
24. **33354613**. Liew YCC, 2020, JAAD Case Rep. "Photodynamic therapy for the treatment of trichodysplasia spinulosa in an Asian renal transplant recipient..." (shortened). No abstract in the PubMed record.
25. **33146676**. Sonstegard A, 2021, JAMA Dermatol. "Trichodysplasia Spinulosa in a Kidney Transplant Recipient." No abstract in the PubMed record.
26. **32995002**. Pennou C, 2020, SAGE Open Med Case Rep. "Trichodysplasia spinulosa in a renal transplant patient: A case report of successful treatment." Quotes: "who rapidly responded to a reduction of his immunosuppressive therapy"; "It occurs more frequently in immunocompromised patients, particularly in solid organ transplants."
27. **32785992**. Rusk AM, 2020, Pediatr Dermatol. "Pediatric trichodysplasia spinulosa: A report of 2 cases and review of the literature." Quotes: "Although seroprevalence reaches up to 70% in adult populations"; "Decreasing or discontinuing immunosuppression has also been shown to improve or alleviate clinical manifestations."
28. **32748541**. Narayanan D, 2020, Transpl Infect Dis. "Recent developments in trichodysplasia spinulosa disease." Review. Quotes: "TS is characterized by uncontrolled inner root sheath cell proliferation and folliculocentric papular eruption"; "can progress to disfiguring leonine facies when left untreated."
29. **32475005**. Jose A, 2020, Transpl Infect Dis. "Trichodysplasia spinulosa: Case reports and review of literature." Two cases plus review. Quotes: "It affects immunosuppressed patients, and <50 cases have been reported"; "Oral valganciclovir and topical cidofovir have been found to give the best results."
30. **32060513**. Alvarez Orellana J, 2021, J Infect Dis. "Sirolimus and Other Mechanistic Target of Rapamycin Inhibitors Directly Activate Latent Pathogenic Human Polyomavirus Replication." Mechanism, in vitro. Quotes: "mTOR inhibition increased LT protein expression for all 5 pathogenic polyomaviruses tested"; "directly activate polyomavirus replication through a Skp2-dependent mechanism."
31. **31787742**. Nako T, 2020, Jpn J Infect Dis. "Functional Analysis of Trichodysplasia Spinulosa-Associated Polyomavirus-Encoded Large T Antigen." Mechanism, in vitro. Quotes: "Immunoprecipitation assays revealed that TSPyV LT bound to retinoblastoma 1, but not to p53 in transfected cells"; "Expression of TSPyV LT in NIH3T3 cells induced colony formation in soft agar."
32. **31505316**. Wang Y, 2019, J Clin Virol. "Multiplex analysis of Human Polyomavirus diversity in kidney transplant recipients with BK virus replication." Quotes: "were detected in 11 blood and 21 urine samples from 21 patients"; "In one individual with PVAN, continuous long-term shedding of MCPyV in urine was observed." TSPyV is one of three HPyVs detected.
33. **31233669**. Pierrotti LC, 2019, Transpl Infect Dis. "Viremia and viruria of trichodysplasia spinulosa-associated polyomavirus before the development of clinical disease..." (shortened). Quotes: "We report a case of TS 6 months after kidney transplantation in a 65 years-old woman"; "detected TSPyV DNA in some of those samples two months before the TS clinical development." Also noted: "Staining for SV40 was positive."
34. **31219640**. Stephan C, 2020, Clin Exp Dermatol. "Viral-associated trichodysplasia spinulosa in a paediatric cardiac transplant recipient." No abstract in the PubMed record.
35. **31209897**. Borgogna C, 2019, J Med Virol. "Primary trichodysplasia spinulosa polyomavirus infection in a kidney transplant child displaying virus-infected decoy cells in the urine." Quotes: "We report a case of primary trichodysplasia spinulosa (TS) infection in a kidney transplant child"; "the presence of degenerated TS-associated polyomavirus (TSPyV)-infected cells in a TS patient's urine."
36. **31008165**. Frigerio A, 2019, JAAD Case Rep. "Widespread keratosis pilaris-like eruption in an immunocompromised child." No abstract in the PubMed record.
37. **30916861**. Barone H, 2019, Pediatr Transplant. "Trichodysplasia spinulosa mimicking lichen nitidus in a renal transplant patient." Quotes: "We report a case of widespread TS in a 9-year-old girl with a history of renal transplantation"; "complicated by BK viremia, which is also caused by a polyomavirus, BKPyV."
38. **30632206**. Wang Y, 2019, Transpl Int. "Occurrence of newly discovered human polyomaviruses in skin of liver transplant recipients..." (shortened). Quotes: "TSPyV DNA was found in a single skin lesion."; "MCPyV DNA was detected in 5/14 (35.7%) premalignant vs. 32/127 (25.2%) benign skin of LiTRs."
39. **30624811**. van Rijn AL, 2019, J Med Virol. "Impact of HPyV9 and TSPyV coinfection on the development of BK polyomavirus viremia and associated nephropathy after kidney transplantation." Quotes: "Seropositivity for HPyV9 (19%) and TSPyV (89%) was comparable between donors and recipients"; "Two recipients developed TSPyV viremia and none HPyV9 viremia."
40. **30585627**. Sheu JC, 2019, Br J Dermatol. "Polyomaviruses of the skin: integrating molecular and clinical advances in an emerging class of viruses." Review. Quotes: "TSPyV is one of the aetiological factors of trichodysplasia spinulosa."; "HPyV6 and HPyV7 have been recently linked to pruritic skin eruptions."

Other PMIDs in the 2nd search that were not fetched: 30537287, 30531297, 30489551, 30470393, 30407150, 30390301, 30352098, 30328951, 29806684, 29568287, 29028114, 28731909, 28654466, 28500640, 28326649, 28108298, 28019062, 27990673, 27726799, 27317512.

**3. Original 1999 description (Haycox)**

The PubMed search page (https://pubmed.ncbi.nlm.nih.gov/?term=trichodysplasia+spinulosa+Haycox) returned HTTP 203 with a cookie-enable page and no results. I did not try other variants of that URL.

The same record was found in the E-utilities list and retrieved from efetch:

- **PMID 10674379**. Haycox CL, et al. 1999 Dec, J Investig Dermatol Symp Proc 4(3):268-71. "Trichodysplasia spinulosa--a newly described folliculocentric viral infection in an immunocompromised host."
- Quote: "This is a case report of an immunocompromised individual who presented with progressive alopecia, friable follicular spinous processes..."
- Retrieved from https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=22801635,22461085,22351786,22196870,22006143,21993271,21941687,21926381,21801610,21680290,21251037,21050621,20796236,20686659,18186853,17535200,15644782,10674379&rettype=abstract&retmode=text

**Useful related PMIDs seen in the 168-list**

- 20686659: van der Meijden E, 2010, PLoS Pathog. Discovery of the TS-associated polyomavirus (TSV). Heart transplant patient, viral load 10^5 copies per cell, lesions resolved after topical cidofovir.
- 21801610: van der Meijden E, 2011, Emerg Infect Dis. Seroprevalence 70% in 528 Dutch healthy persons; 89% in 80 renal transplant patients.
- 21251037: Matthews MR, 2011, J Cutan Pathol. A 7-year-old with Down syndrome and pre-B ALL; reviews 19 additional reported cases.
- 22351786: Fischer MK, 2012, Arch Dermatol. TSPyV DNA detected in renal allograft tissue (first such report).

# Trichodysplasia Spinulosa (MONDO:0016455): Disease Knowledge-Base Research Report

**How I read the request:** Trichodysplasia spinulosa (TS) is an infectious skin disease, not a Mendelian one. Its causal agent is the **trichodysplasia spinulosa-associated polyomavirus** (TSPyV, also written TSV), which infects people whose immune systems are suppressed. **No human causal gene exists**, and the template correctly lists none. In this report the "causal gene" slots are filled with the **viral genes**: large T antigen (LT), small T antigen (sT), middle T antigen (mT) and the VP1 capsid gene. Most of the template's Mendelian fields do not apply, and I mark them as such.

**Sources and limits:** Evidence comes from PubMed abstracts retrieved this session through NCBI E-utilities, plus a few full-text pages. PubMed returned 168 records for "trichodysplasia spinulosa". The PMC full-text pages for the key virology papers were blocked by a bot check, so those claims rest on their PubMed abstracts. I did not retrieve ICD-10/ICD-11, MeSH or NCBI Taxonomy identifiers, and I give none of them. All suggested ontology terms (HPO, GO, CL, UBERON, NCIT, CHEBI) are my own mappings and need checking against the ontologies before use.

---

## 1. Disease Information

**Overview.** TS is a rare skin disease of immunosuppressed people. It shows up as follicular papules carrying keratin spines ("spicules"), mostly on the central face, often with hair loss of the eyebrows and eyelashes.
- Orphanet (as reproduced on Qeios) describes it as a rare infectious skin disease with follicular papules and keratin spicules "predominantly in the face (e.g. nose, eyebrows, auricles), that is due to polyomavirus infection in immunocompromized patients" (https://www.qeios.com/read/NXBAYF/pdf).
- Silling 2022, Hautarzt (PMID 35482045): "Keratin spines (spicules), mainly in the center of the face, clinically characterize this disease."
- Narayanan 2020, a review (PMID 32748541): "TS is characterized by uncontrolled inner root sheath cell proliferation and folliculocentric papular eruption."

**History.**
- **1999, first description.** Haycox et al. described the condition and named it (PMID 10674379): "an immunocompromised individual who presented with progressive alopecia, friable follicular spinous processes, and erythematous, indurated papules." Electron microscopy showed "intracellular viral particles."
- **2010, virus found.** Van der Meijden et al. discovered TSPyV in "plucked facial spines of a heart transplant patient with trichodysplasia spinulosa" (PMID 20686659, PLoS Pathog 2010; PMC2912394).

**Identifiers**

| Resource | ID | Status |
|---|---|---|
| MONDO | MONDO:0016455 | Given in the template; not checked independently |
| Orphanet | ORPHA:228379 ("Virus-associated trichodysplasia spinulosa") | From the Qeios reproduction of Orphanet and from Global Genes (https://globalgenes.org/?p=610272) |
| OMIM | None | Expected, since this is not a Mendelian disease |
| ICD-10 / ICD-11 / MeSH | Not retrieved | Look these up directly |

**Synonyms:**
- Virus-associated trichodysplasia spinulosa (VATS)
- Viral-associated trichodysplasia (Wanat 2012, PMID 22351821)
- Cyclosporine-induced folliculodystrophy
- Pilomatrix dysplasia
- TS

The NORD/GARD listing gives these synonyms (https://rarediseases.org/?p=266288). The name "cyclosporine-induced folliculodystrophy" reflects early cases in people taking cyclosporine. The disease is now known to be viral and not specific to cyclosporine.

**Type of evidence.** Almost all knowledge comes from individual case reports and small case series. The largest data sets are:
- Curman 2021, a review of all published cases (PMID 33559344).
- Kazem 2012, a case-control virology study of 11 patients and 249 controls (PMID 22196870).
- Seroepidemiology cohorts (PMIDs 21801610, 36298837).

---

## 2. Etiology

**Cause (infectious).** The cause is active, productive TSPyV infection of hair follicles.
- **Discovery paper** (PMID 20686659): the virus was found at "a viral load of 10(5) copies per cell"; "After topical cidofovir treatment, the lesions largely resolved coinciding with a reduction in TSV load."
- **Case-control study** (Kazem 2012, PMID 22196870): "Findings obtained in TS patients (n=11) were compared to those obtained in healthy controls (n=249)." Lesions were positive "with 100% positivity of the lesional and 2% of the control samples," with "high TSPyV DNA loads in the lesional samples (∼10(6)copies/cell)."
- **Kazem 2013 review** (PMID 23593936): "viral load measurements indicate an etiological role of active TSPyV infection in the development of this disease."
- **Primary infection vs. reactivation:** Primary infection can cause TS. Borgogna 2019 describes "primary trichodysplasia spinulosa (TS) infection in a kidney transplant child" (PMID 31209897). Silling 2022 notes that "primary infection with … TSPyV can cause the very rare skin disease" (PMID 35482045). Reactivation of latent virus is also proposed (see the sirolimus data below), but I found no direct proof of it in patients.

**Risk factors (acquired and environmental)**

- **Solid-organ transplantation with immunosuppression.** This is the main setting: kidney, heart, liver and pancreas recipients (PMIDs 10674379, 20686659, 22351786, 28326649). Pennou 2020: "It occurs more frequently in immunocompromised patients, particularly in solid organ transplants" (PMID 32995002).
- **Blood cancers in children on chemotherapy.**
  - Pre-B acute lymphoblastic leukaemia (ALL) in a 7-year-old with Down syndrome (PMID 21251037).
  - Lymphoblastic leukaemia in a 5-year-old (PMID 24887966).
  - Pre-B-cell lymphoblastic leukaemia in a 7-year-old (PMID 26338086).
  - "a 6-year-old male child who presented with a generalized papular eruption during chemotherapy" (PMID 28654466).
- **Chronic lymphocytic leukaemia** in adults (PMC9949812).
- **Allogeneic bone-marrow transplant with ruxolitinib (a JAK inhibitor):** a 67-year-old woman. The authors proposed that ruxolitinib suppresses "the JAK-signal transducer and activator of the transcription pathway's antiviral functions" (PMID 37799360).
- **mTOR inhibitors (sirolimus and related drugs), proposed.** This is in-vitro evidence only. "mTOR inhibition increased LT protein expression for all 5 pathogenic polyomaviruses tested." Sirolimus, "but not the calcineurin inhibitor tacrolimus, at levels routinely achieved in patients," activated replication. The proposed route is "a Skp2-dependent mechanism" (Alvarez Orellana 2021, PMID 32060513). Whether this raises TS risk in patients has not been shown.
- **Sorafenib.** One reported case causes confusion: "Sorafenib-associated Trichodysplasia Spinulosa versus Follicular Hyperkeratosis" (PMID 41458272). It may be a drug-induced look-alike rather than viral TS.

**Genetic risk factors.** None found. There are no GWAS, ClinVar or candidate-gene data for host susceptibility. One reported child had Down syndrome together with ALL (PMID 21251037), but the immunosuppression explains the risk.

**Protective factors.**
- **Not stated in the literature:** I found no data on protective genes or lifestyle factors.
- **Proposed, not demonstrated:** Prior immunity from childhood infection may protect. Seroprevalence is high (70–89%), yet disease is rare. A review suggests that "the high rate of childhood primary infection might explain why TS is a very rare disease among immunocompromised patients" (Hungarian review, https://dea.lib.unideb.hu/bitstreams/294d86da-9b0c-494e-bc87-c5e42ea3ae80/download).

**Gene-environment interaction.** The relevant interaction is between the virus and the host's immune status. Drugs that impair T-cell or interferon/JAK-STAT antiviral control (calcineurin inhibitors, mTOR inhibitors, antimetabolites, chemotherapy, JAK inhibitors) allow productive infection. There are no host-genetic data.

---

## 3. Phenotypes

Nobody has published frequency data across a cohort. The qualitative frequencies below are from case-series descriptions and reviews, and Curman 2021 (PMID 33559344) has the full case tabulation.

| Phenotype | Type | HPO suggestion (verify) | Frequency / notes | Source |
|---|---|---|---|---|
| Follicular papules with keratin spines/spicules (central face: nose, eyebrows, ears) | Sign | Follicular hyperkeratosis HP:0007502; Papule HP:0200034 | Defining feature; essentially all cases | PMID 35482045; Orphanet |
| Alopecia of eyebrows, eyelashes and scalp | Sign | Alopecia HP:0001596; Sparse eyebrow HP:0045075; Sparse eyelashes HP:0000653 | Common; in the first description ("progressive alopecia") | PMID 10674379; hair regrowth after cidofovir, PMID 22351821 |
| Erythematous, indurated papules | Sign | Erythema HP:0010783 | Frequent | PMID 10674379 |
| Facial thickening / "leonine facies" | Sign | Coarse facial features HP:0000280 | Advanced, untreated disease | PMID 32748541: "progress to disfiguring leonine facies when left untreated" |
| Generalized spread (trunk, limbs) | Sign | — | Occasional | PMID 28326649: "spiny follicular papules on the face, ears, extremities, and trunk"; PMID 30916861: "widespread TS"; 28654466 |
| Itching / pain | Symptom | Pruritus HP:0000989; Pain HP:0012531 | Occasional | PMID 38493799: "widespread painful, itchy bumps on the nose and face" |
| Lichen nitidus-like or keratosis pilaris-like eruption | Sign | — | Atypical presentations | PMIDs 30916861, 31008165 |
| TSPyV DNA in blood and urine (viraemia, viruria) | Lab | — | Occasional; can precede skin disease | PMID 31233669: "detected TSPyV DNA … two months before the TS clinical development"; PMID 22351786; urinary decoy cells, PMID 31209897 |

**Age at onset:**
- **Children:** ages 5–10 (PMIDs 24887966, 21251037, 30916861, 40616235, 40200820).
- **Adults:** ages 19–67 (PMIDs 38493799, 22351786, 31233669, 37799360).

**Timing and course:** Onset follows immunosuppression, for example "6 months after kidney transplantation" (PMID 31233669). The disease is chronic and progressive while immunosuppression continues.

**Quality of life:** No formal measures (DLQI, EQ-5D) have been published. The main burden is disfigurement and hair loss on the face, plus itching or pain in some patients.

---

## 4. Genetic / Molecular Information

**Human causal genes, ClinVar variants, gnomAD frequencies, modifier genes, epigenetics and chromosomal abnormalities:** none of these apply, and none have been reported.

**Viral genome.**
- TSPyV is a circular double-stranded DNA polyomavirus of 5,232 nucleotides. It was recovered by rolling-circle amplification and has the typical polyomavirus organization (PMID 20686659).
- Its early region encodes LT, sT, mT and ALTO. Its late region encodes the VP1 and VP2 capsid proteins.
- TSPyV makes an ALTO circular RNA (circALTO) that "can be detected in infected tissues." These RNAs are "stable, predominantly located in the cytoplasm, and N6-methyladenosine (m6A) modified" (Yang 2021, PMID 33999949).

**Viral protein functions**

| Viral protein | Function | Evidence | PMID |
|---|---|---|---|
| Large T (LT) | "TSPyV LT bound to retinoblastoma 1, but not to p53"; "induced colony formation in soft agar" in NIH3T3 cells | In vitro | 31787742 |
| Small T (sT) | Binds PP2A; "inducing hyperphosphorylation of ATM and 53BP1"; "dysregulates the S6 protein translation pathway via hyperphosphorylation of CDC2, p70 S6 kinase, S6, and PP1α" | In vitro | 35000075; PP2A binding reported by Nguyen et al. 2014 (JAMA Dermatol; PMID not retrieved) |
| Small T (sT) | Not transforming in assays; "TSPyV ST proteins were incapable of nuclear translocation" | In vitro | 38831469 |
| Middle T (mT) | "hyperactivation of MEK, ERK and MNK1," which "depends upon TSPyV mT antigen interaction with protein phosphatase 2A (PP2A)" | In vitro | 28500640 |

**Relevant human host genes (as targets, not causal genes):**
- RB1 (HGNC:9884)
- CDKN2A/p16 (HGNC:1787)
- CDKN1A/p21 (HGNC:1784)
- PPP2 (PP2A) subunits
- MAP2K1/2, MAPK3/1, MKNK1
- ATM, TP53BP1, RPS6KB1, RPS6

**Coinfection:** One child had "concomitant productive HPV and TSPyV infection" (PMID 28654466).

---

## 5. Environmental Information

- **Infectious agent.** Trichodysplasia spinulosa-associated polyomavirus (family Polyomaviridae). Its NCBI Taxonomy ID was not retrieved.
- **Seroprevalence in Dutch cohorts** (PMID 21801610):
  - 70% overall in 528 healthy people, "range 10% in small children to 80% in adults."
  - 89% in 80 renal transplant patients.
  - The authors conclude that infection "is common and occurs primarily at a young age."
- **Seroprevalence in other cohorts:**
  - Hungary, 552 sera: adult TSPyV seroprevalence 85% (Jeles 2022, PMID 36298837).
  - Kidney transplant donors and recipients: 89% (PMID 30624811).
  - About 75% of adults, according to Moore 2026 (PMID 41965049).
- **Primary infection in children.** A Finnish cohort of 144 children found that 39 (27%) seroconverted for TSPyV, with no symptoms linked to seroconversion. Viraemia was rare: 2 children had less than 10⁴ copies/mL (https://wwwnc.cdc.gov/eid/article/20/4/13-1015).
- **Route of transmission:** not established. It is reviewed in Oliveira 2026 (PMID 42172084).
- **Drug exposures:** immunosuppressive drugs (Section 2). TS is not linked to any toxin, occupational or lifestyle exposure, and I found no reports of such links.

---

## 6. Mechanism / Pathophysiology

### Causal chain

1. **Primary infection**, usually silent and in childhood (PMID 21801610; Finnish cohort). It **leads to** latent or persistent carriage of TSPyV. Where the virus persists in the body is not established.
2. **Immunosuppression** (transplant drugs, chemotherapy, JAK inhibitors) **results in** loss of immune control of the virus. This can be primary infection in a person who has never met the virus (PMID 31209897) or reactivation (inferred). mTOR inhibitors may also directly **increase** LT expression and viral replication (in vitro, PMID 32060513).
3. **Productive infection** of hair-follicle inner root sheath keratinocytes **results in** very high viral loads: about 10⁵–10⁶ copies per cell, with virions seen by electron microscopy (PMIDs 20686659, 22196870, 22351821).
4. **Early viral proteins act on the cell cycle and signalling**, in three branches:
   - **4a. LT–pRB.** LT binds pRB (PMID 31787742). This **leads to** pRB hyperphosphorylation, release of E2F and S-phase entry. Patient biopsies show phosphorylated pRB at the follicle margins next to LT staining (PMID 25291363). The link from binding to phosphorylation is inferred from co-localization.
   - **4b. mT–PP2A.** mT engages PP2A, which **leads to** hyperactivation of MEK/ERK/MNK1 (in vitro, PMID 28500640).
   - **4c. sT.** sT **drives** DNA-damage-response signalling (ATM, 53BP1) and S6/p70S6K translation signalling (in vitro, PMID 35000075). This supports viral replication.
5. **Cell-cycle push** **results in** hyperproliferation of inner root sheath cells. Staining shows "Intense Ki-67 staining … especially in the margins of TS hair follicles." p16^INK4a and p21^WAF rise as a failed brake. The authors call the data "compatible with a scenario of TSPyV T-antigen-mediated cell cycle progression" (PMID 25291363).
6. **Expanded, abnormally differentiating inner root sheath cells** packed with trichohyalin granules **lead to** a dysplastic follicle that makes a keratin spicule instead of a normal hair shaft. Histology shows "increased cellularity of the nucleated eosinophilic inner root sheath cells with trichohyalin granules" (PMID 27051806). This is the step from histology to the clinical sign.
7. **Clinical result:** spiny follicular papules and alopecia. If immunosuppression continues, the disease progresses to facial thickening or leonine facies (PMID 32748541). Lowering immunosuppression or giving antivirals **leads to** a fall in viral load and resolution of lesions (PMID 20686659). This is evidence that the chain is reversible.
8. **Branch, outside the skin:** viraemia and viruria, and TSPyV DNA in a renal allograft (PMIDs 22351786, 31233669, 31209897). No organ disease other than skin has been proven.

### Category checklist

- **Pathways:** RB–E2F cell-cycle control; PP2A-regulated MAPK (MEK/ERK/MNK1); mTOR/S6K translation; ATM DNA-damage response; JAK-STAT antiviral signalling (host defence, inferred from the ruxolitinib case).
- **Immune role:** The disease depends on suppressed cell-mediated immunity. Lesions get better when immunosuppression is reduced (PMIDs 32995002, 40616235).
- **Not studied:** metabolomics, lipidomics, proteomics, single-cell, spatial, CRISPR or GEO transcriptomic data. I found no studies.
- **Suggested GO terms (verify):**
  - viral genome replication (GO:0019079)
  - positive regulation of cell population proliferation (GO:0008284)
  - G1/S transition of mitotic cell cycle (GO:0000082)
  - ERK1 and ERK2 cascade (GO:0070371)
  - hair follicle development (GO:0001942)
  - keratinization (GO:0031424)
  - DNA damage response (GO:0006974)
- **Suggested CL terms (verify):**
  - keratinocyte (CL:0000312)
  - inner root sheath cell, hair follicle (search CL for the exact term)
  - T cell (CL:0000084), as the immune control that is lost

---

## 7. Anatomical Structures Affected

- **Organ:** skin (UBERON:0002097), specifically the hair follicle (UBERON:0002073). There is no proven secondary organ disease. Viral DNA has been found in blood, urine and kidney allograft (PMID 22351786).
- **Tissue and cell:**
  - Inner root sheath of the hair follicle (UBERON, search "inner root sheath").
  - Keratinocytes making up the inner root sheath, with cellular inclusions seen on middle T immunostaining (PMID 22351821).
- **Subcellular:**
  - Nucleus (GO:0005634): the site of viral replication and of LT action.
  - Intracellular virions of 35.6 nm (PMC3346264) or 38 nm (Haycox).
  - Cytoplasm (GO:0005737): where circALTO RNAs sit.
- **Sites:** face (UBERON:0001456), especially the nose, eyebrows (UBERON:0001702), eyelids and eyelashes, and ears (auricle, UBERON:0001757). In generalized disease, also the trunk and limbs.
- **Laterality:** symmetrical and bilateral, by the clinical descriptions.

---

## 8. Temporal Development

- **Onset:** months after immunosuppression starts, for example 6 months after kidney transplant (PMID 31233669). Onset is subacute to chronic.
- **Course:** progressive while immunosuppression continues. It can advance to leonine facies (PMID 32748541).
- **Stages:** none formally defined. Informally: localized facial papules and spines, then confluent or generalized disease, then facial thickening.
- **Remission:**
  - *After treatment:* reduced immunosuppression, cidofovir or valganciclovir (Section 12).
  - *Spontaneous:* "resolved spontaneously after completing the antineoplastic medication" (PMID 24887966).
- **Windows to act early:** Viraemia or viruria can precede skin lesions by about 2 months (PMID 31233669). This suggests a window for earlier detection, but nobody has tested it prospectively.

---

## 9. Inheritance and Population

- **Inheritance, penetrance, anticipation, founder effects, consanguinity and carrier frequency:** these do not apply, because the disease is infectious and not inherited.
- **Case counts:**
  - "fewer than 100 cases have been reported in the literature" (Moore 2026, PMID 41965049).
  - An earlier review gave fewer than 50 (PMID 32475005).
- **Prevalence and incidence:** no population estimates exist. In unaffected immunosuppressed patients, TSPyV DNA was found by PCR in 4% (PMID 20686659).
- **Demographics:**
  - Both children and adults are affected.
  - Cases come from Europe, the Americas, Asia (PMID 33354613, an Asian renal transplant recipient) and the Middle East (PMID 38434466).
  - Infection is widespread worldwide, judging by seroprevalence.
  - No sex ratio has been published. The case reports I retrieved include both sexes.

---

## 10. Diagnostics

**Diagnosis rests on clinical appearance plus histology, confirmed by virology.**

- **Histopathology.** Biopsy shows:
  - enlarged hair bulbs and an expanded inner root sheath (PMID 26338086);
  - "hyperproliferating inner root sheath cells containing large eosinophilic trichohyaline granules" (PMID 36809091);
  - strong Ki-67 positivity (PMID 25291363; PMC4809585).
- **Immunohistochemistry:**
  - Polyomavirus middle T antigen staining is positive in inner root sheath keratinocytes (PMID 22351821).
  - LT antigen staining is positive (PMID 25291363).
  - SV40 antibody cross-reacts and stains positive (PMID 31233669).
- **Electron microscopy:** intracellular, icosahedral virions of 35–38 nm (PMIDs 10674379, 22351821, 21251037).
- **Molecular testing.** PCR or qPCR for TSPyV on biopsy tissue or plucked spicules:
  - Lesional loads are about 10⁵–10⁶ copies per cell, against 2% positivity in controls (PMIDs 20686659, 22196870).
  - PCR for Merkel cell polyomavirus is negative, which helps separate the two (PMID 21251037).
  - Blood and urine PCR can show viraemia or viruria (PMID 31233669).
  - Urine cytology may show decoy cells (PMIDs 31209897, 22351786).
- **Serology:** of limited use for diagnosis, because adult seroprevalence is high. Serology is preferred for detecting primary infection in children (Finnish cohort).
- **Dermoscopy:** a "Dermatoscopy case of the month" exists (PMID 34746353). I did not read its details.
- **Human genetic tests (WES, WGS, panels, CMA, karyotype and so on):** not applicable.
- **Formal diagnostic criteria:** none.
- **Differential diagnosis:**
  - Lichen nitidus (PMID 30916861)
  - Keratosis pilaris and keratosis pilaris-like eruptions (PMID 31008165)
  - Sebaceous filaments (PMID 38090399)
  - Multiple minute digitate hyperkeratosis (PMID 21050621)
  - Drug-induced follicular hyperkeratosis, for example from sorafenib (PMID 41458272)
  - Pilomatrix and other follicular dysplasias
  - Spiny keratoses linked to other polyomaviruses (HPyV6 and HPyV7 cause itchy eruptions; PMID 30585627)
- **Screening:** no programme exists.

---

## 11. Outcome / Prognosis

- **Mortality:** TS itself has not been reported to cause death. The prognosis depends on the underlying transplant or cancer.
- **Morbidity:** disfigurement, alopecia, itching or pain, and leonine facies when untreated (PMID 32748541). No formal quality-of-life data exist.
- **Recovery:**
  - Lesions often resolve when immunosuppression is reduced or with antivirals.
  - Hair regrowth has been documented (PMID 22351821).
  - Improvement may not last after treatment stops. This comes from the Wikipedia summary and is unverified.
- **Prognostic factors (inferred):** how deep the immunosuppression is and whether it can be reduced; viral load falls with resolution (PMID 20686659).
- **Complications:** coexisting BK polyomavirus viraemia has been reported (PMID 30916861). In one kidney recipient with TS, "The patient had three rejections" (PMID 31233669). Lowering immunosuppression carries a risk of graft rejection.

---

## 12. Treatment

**Evidence comes only from case reports and series. There are no randomized trials and no NCT trials were found.**

The Curman 2021 review (PMID 33559344) says: "The few treatments reported in case reports to be effective include topical cidofovir 3%, reduction of immunosuppression and oral valganciclovir." It adds that "a majority of reported cases have consequently received ineffective therapies."

| Intervention | Suggested NCIT / CHEBI (verify) | Evidence |
|---|---|---|
| Reduce or modify immunosuppression | — | "rapidly responded to a reduction of his immunosuppressive therapy" (PMID 32995002). Paediatric reviews agree (PMID 32785992). |
| Topical cidofovir 1–3% | Cidofovir (NCIT C1159; CHEBI:3696) | Lesions resolved with fall in viral load (PMID 20686659). Dramatic improvement and hair regrowth (PMID 22351821). 3% worked after 1% failed in 2 kidney recipients (PMID 27051806). 1% cleared lesions in 4 weeks in a 19-year-old (PMID 38493799). |
| Oral valganciclovir | Valganciclovir (CHEBI:63635) | Improvement reported (PMID 36809091; CLL case PMC9949812, 450 mg twice daily plus topical cidofovir). "no obvious response" in another case (PMID 38434466). |
| Leflunomide | Leflunomide (CHEBI:6402) | "generalized TS treated successfully with leflunomide" in a liver transplant recipient (PMID 28326649). Combined with valganciclovir or cidofovir and reduced immunosuppression in children (PMIDs 40616235, 40200820). |
| Oral acitretin | Acitretin (CHEBI:50173) | "significant improvement after 3 months" in a ruxolitinib-associated case (PMID 37799360). |
| Other single reports | — | Photodynamic therapy (PMID 33354613); Camellia sinensis (green tea) 10% ointment (PMID 34001481); manual extraction of spines. |
| Usually ineffective | — | Topical retinoids, topical steroids, imiquimod. This summary is from a secondary slide deck based on Curman 2021 (https://www.ohsu.edu/sites/default/files/2023-05/Trichodysplasia%20spinulosa%20in%20SOT%20%284.5.2023%29.pdf). Imiquimod failure is also reported in PMIDs 36809091 and 27051806. |

- **Practical algorithm (synthesized from the reviews, not a guideline):** confirm the diagnosis by biopsy and PCR; reduce immunosuppression where the graft allows; give topical cidofovir 3%; add oral valganciclovir or leflunomide for widespread or resistant disease.
- **Antiviral development:** reviewed by Wu 2021 (PMID 33729628): "Current clinical studies are limited by small case numbers."
- **Gene therapy, cell therapy, RNA therapy, targeted therapy and pharmacogenomics:** none apply or have been reported.

---

## 13. Prevention

- **Primary prevention:** no vaccine. It is not feasible, given that infection is nearly universal in childhood.
- **Secondary prevention:** recognize the disease early in transplant recipients. Monitoring blood and urine PCR has been suggested by the case of viraemia before lesions (PMID 31233669), but it has not been validated.
- **Tertiary prevention:** choose immunosuppressive drugs with care. In vitro, sirolimus activated polyomavirus replication while tacrolimus did not (PMID 32060513); clinical relevance is unproven.
- **Genetic counselling:** not applicable.

---

## 14. Other Species / Natural Disease

- **Naturally occurring TS in animals:** I found no reports. OMIA was not searched.
- **Context:** Polyomaviruses are generally species-specific. A TS-like disease in animals has not been documented in anything I retrieved.
- **Zoonotic potential:** none reported.

---

## 15. Model Organisms

- **Animal models:** I found no animal model of TS, and none has been reported in the literature I retrieved.
- **Cell-based models used so far:**
  - NIH3T3 mouse fibroblasts expressing LT, for transformation assays (PMID 31787742).
  - Cells transfected with sT or mT, for signalling studies (PMIDs 28500640, 35000075, 38831469).
  - In-vitro polyomavir

**Note:** The end of Section 15 above was cut off and is not repeated here. Below is a short replacement for the rest of that section, followed by the report

The report is essentially complete; it was cut off mid-sentence at the end of Section 15. Here is the remainder:

---

## 15. Model Organisms (continued)

- **Cell-based models used so far:**
  - NIH3T3 mouse fibroblasts expressing TSPyV LT, used in transformation assays — "induced colony formation in soft agar" (PMID 31787742).
  - Cells transfected with sT or mT antigen, used for signalling studies (PMIDs 28500640, 35000075, 38831469).
  - In-vitro systems showing that mTOR inhibition drives LT expression and viral replication across pathogenic human polyomaviruses (PMID 32060513).
- **Genetic animal models (knockout, transgenic, humanized), phenotype recapitulation, model limitations:** none reported.
- **Resources (MGI, RGD, ZFIN, etc.):** not applicable — no organism model exists.
- **Key limitation:** TS research depends almost entirely on patient biopsies and on in-vitro expression of individual viral proteins. There is no system that reproduces the whole disease (follicle infection → inner root sheath hyperproliferation → spicule formation), which is a recognized gap.

---

## Summary of key evidence gaps
- No human causal gene, no host-genetic risk data, no inherited component — the disease is viral.
- No prevalence/incidence estimates, no formal diagnostic criteria, no QoL data, no randomized treatment trials, no animal model.
- Core mechanistic steps (LT→pRB phosphorylation, mT→PP2A→MAPK, sT→DDR/S6K) are supported by in-vitro and immunohistochemical correlation, not by in-vivo causal proof.
- Full-text of the pivotal virology papers (PMC2912394, PMC3381547, PMC4188587) was blocked this session; those claims rest on their PubMed abstracts and should be verified against full text.

**Primary sources cited (PMIDs):** 10674379, 20686659, 21251037, 21801610, 22196870, 22351786, 22351821, 23593936, 24887966, 25291363, 26338086, 27051806, 28326649, 28500640, 28654466, 30585627, 30624811, 30916861, 31008165, 31209897, 31233669, 31787742, 32060513, 32475005, 32748541, 32785992, 32995002, 33354613, 33559344, 33729628, 33999949, 35000075, 35482045, 36298837, 36809091, 37799360, 38090399, 38434466, 38493799, 38831469, 40200820, 40616235, 41458272, 41965049, 42172084.

**Non-PubMed sources:** Orphanet via [Qeios](https://www.qeios.com/read/NXBAYF/pdf) (ORPHA:228379); [Global Genes](https://globalgenes.org/?p=610272); [NORD](https://rarediseases.org/?p=266288); [CDC EID Finnish cohort](https://wwwnc.cdc.gov/eid/article/20/4/13-1015); [OHSU treatment summary deck](https://www.ohsu.edu/sites/default/files/2023-05/Trichodysplasia%20spinulosa%20in%20SOT%20%284.5.2023%29.pdf); [PMC9949812 (CLL case)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9949812/).

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 52 |
| Resolved | 52 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 19 |
| Quoted claims found in source | 18 |
| Quoted claims **not** found in source | 1 |
| Quoted claims with nothing to check against | 1 |
| References weighed for topical relevance | 52 |
| On topic | 39 |
| Off topic | 1 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:35482045` *(abstract only)*: "primary infection with … TSPyV can cause the very rare skin disease"
  - closest text in source: "In immunocompromised individuals, primary infection with trichodysplasia spinulosa-associated polyomavirus (TSPyV) can cause the very rare skin disease trichodysplasia spinulosa (TS)"

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:41458272` (2 mentions) - Sorafenib-associated Trichodysplasia Spinulosa versus Follicular Hyperkeratosis: a case report.
  - shared terms: skin

Weighed against this report's own most characteristic terms: `disease`, `cell`, `tspyv`, `viral`, `transplant`, `infection`, `patient`, `found`, `polyomavirus`, `hair`, `immunosuppression`, `skin`, `kidney`, `dna`, `lesion`, `recipient`, `gene`, `inner`, `primary`, `root`.

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `PMID:27051806`: "increased cellularity of the nucleated eosinophilic inner root sheath cells with trichohyalin granules"
  - Reference resolved but exposes no abstract or full text to search

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 34 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 7 |
| Terms whose name was checked | 16 |
| Terms named correctly | 12 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0016455` (2 mentions) - the report calls it "MONDO"; MONDO calls it **virus-associated trichodysplasia spinulosa**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0002097` (1 mention) - the report calls it "Organ:** skin"; UBERON calls it **skin of body**, and lists "skin organ" among its other names
- `UBERON:0001456` (1 mention) - the report calls it "Sites:** face"; UBERON calls it **face**
- `CHEBI:50173` (1 mention) - the report calls it "Acitretin"; CHEBI calls it **all-trans-acitretin**, and lists "acitretin" among its other names

### Terms the ontology service could not be reached for

4 term(s) could not be checked because the ontology service was unreachable (a timeout, 5xx, 408 or 429), not because anything looks wrong with them. Re-run when the service is reachable -- the label cache resumes, so only the unresolved terms are retried:

- `ORPHA:228379` (2 mentions)
- `HP:0000653` (1 mention)
- `HP:0000989` (1 mention)
- `GO:0008284` (1 mention)

### Terms whose obsolescence could not be checked

4 term(s) resolved, so they exist, but the ontology service was unreachable for the deprecation check -- treat their obsolescence as unknown rather than clean, and re-run to confirm:

- `HP:0200034` (1 mention)
- `HP:0010783` (1 mention)
- `HP:0000280` (1 mention)
- `HP:0012531` (1 mention)