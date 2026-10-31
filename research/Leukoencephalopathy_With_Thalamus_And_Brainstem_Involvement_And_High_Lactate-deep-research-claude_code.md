---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-28T01:29:53.117520'
end_time: '2026-10-28T01:35:25.917050'
duration_seconds: 332.8
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Leukoencephalopathy With Thalamus And Brainstem Involvement And High
    Lactate
  mondo_id: MONDO:0013971
  category: Mendelian
  causal_genes: EARS2
  omim_id: OMIM:614924
  synonyms: COXPD12; EARS2 combined oxidative phosphorylation deficiency; LTBL; combined
    oxidative phosphorylation defect type 12; combined oxidative phosphorylation deficiency
    caused by mutation in EARS2; combined oxidative phosphorylation deficiency type
    12
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
  web_search_requests: 7
  num_turns: 33
  total_cost_usd: 2.4511065000000007
  session_id: 0bfb328d-96db-5dca-803a-342a247b0264
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  assistant_text_blocks: 3
citation_count: 12
reference_validation:
  total_references: 27
  verified: 27
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 18
  quotes_valid: 17
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:31839000
  relevance_assessed: 27
  on_topic: 24
  needs_review: true
  validator_version: 0.4.0
term_validation:
  total_terms: 48
  verified: 46
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 17
  labels_matching: 10
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0013971
    reported_labels:
    - given in the brief
    ontology_label: leukoencephalopathy-thalamus and brainstem anomalies-high lactate
      syndrome
  labels_variant: 6
  unresolvable_prefixes:
  - ORPHA
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Leukoencephalopathy With Thalamus And Brainstem Involvement And High Lactate
- **MONDO ID:** MONDO:0013971 (if available)
- **Causal gene(s):** EARS2
- **OMIM:** OMIM:614924
- **Synonyms:** COXPD12; EARS2 combined oxidative phosphorylation deficiency; LTBL; combined oxidative phosphorylation defect type 12; combined oxidative phosphorylation deficiency caused by mutation in EARS2; combined oxidative phosphorylation deficiency type 12
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Leukoencephalopathy With Thalamus And Brainstem Involvement And High Lactate** covering all of the
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

PubMed web blocks; use E-utilities.

Pulling the remaining pieces now: identifiers, the late-onset case, model organisms, and the c.193A>G founder data. After that I'll write the report.

# Leukoencephalopathy with Thalamus and Brainstem Involvement and High Lactate (LTBL / COXPD12, *EARS2*): research report

**How the evidence was gathered (October 2026).** PubMed's web pages blocked automated access, so abstracts came from NCBI E-utilities through a fetch tool that summarizes pages. That tool would only return short verbatim excerpts (under about 125 characters each). Every quotation below is one of those excerpts, so each needs re-checking against the source with `just fetch-reference PMID:<n>` before it goes into a KB snippet.

All ontology CURIEs in this report are **unverified leads written from memory**. Under the repository's term contract, look each one up (`runoak`, the `cache/` files, or OLS) before binding it.

Several articles were reachable only as titles or metadata, with no abstract text: Talim 2013 (a letter), Prasun 2019, Akduman 2026, and Roux 2021. They are marked as such where they appear.

---

## 1. Disease information

**Overview.** LTBL is an autosomal recessive mitochondrial leukoencephalopathy. It is caused by biallelic pathogenic variants in ***EARS2***, which encodes mitochondrial glutamyl-tRNA synthetase (mtGluRS). The disease usually begins in infancy. The MRI pattern is distinctive:
- extensive, symmetrical abnormalities of the cerebral white matter that spare the periventricular rim;
- symmetrical signal change in the thalami, midbrain, pons, medulla oblongata and cerebellar white matter;
- raised lactate in body fluids and on proton MR spectroscopy (MRS).

Steenweg et al. defined the disease in 12 patients (PMID:22492562).

- "extensive symmetrical cerebral white matter abnormalities sparing the periventricular rim" (PMID:22492562)
- "All 12 patients shared an infantile onset and rapidly progressive disease" (PMID:22492562)
- "Proton magnetic resonance spectroscopy showed increased lactate." (PMID:22492562)

**Identifiers**

| Resource | ID |
|---|---|
| MONDO | MONDO:0013971 (given in the brief) |
| OMIM (disease) | 614924 (COXPD12) |
| OMIM (gene) | 612799 (EARS2). Lead; verify |
| Orphanet | ORPHA:314051, "Leukoencephalopathy-thalamus and brainstem anomalies-high lactate". Seen only on mirror sites ([MedGen](https://https.ncbi.nlm.nih.gov/medgen/1645614), [Qeios](https://www.qeios.com/read/8AU4UZ/pdf)); the Orphanet site itself blocked the fetch |
| MedGen | 1645614 |
| HGNC | EARS2, hgnc:29419. Lead; verify |
| UniProt | Q5JPH6 (SYEM_HUMAN), 523 aa, transit peptide at residues 1–41 |
| ICD-10 | E88.4x, mitochondrial metabolism disorders. Lead; verify |
| ICD-11 / MeSH | No disease-specific code found |

**Synonyms:** LTBL; COXPD12; combined oxidative phosphorylation deficiency 12; EARS2 deficiency; mitochondrial glutamyl-tRNA synthetase deficiency.

**Source type.** Everything here is disease-level synthesis built from case reports and small case series. There is no registry and no EHR cohort.

---

## 2. Etiology

- **Cause:** biallelic loss-of-function (mostly hypomorphic) variants in *EARS2*, either compound heterozygous or homozygous. Most patients are compound heterozygous (PMID:22492562).
- **Genetic risk factors:** consanguinity raises the chance of homozygous presentations; several Turkish homozygous cases have been reported (PMID:26893310, PMID:26619324). No susceptibility loci or GWAS signals are known for LTBL.
- **Separate digenic role.** In reversible infantile respiratory chain deficiency (RIRCD), heterozygous *EARS2* variants act as modifiers of the homoplasmic mtDNA variant m.14674T>C in *MT-TE* (the mitochondrial tRNA-Glu gene). This is a different disease from LTBL, but it is mechanistically relevant because it shows mtGluRS dosage interacting with the tRNA-Glu substrate.
  - "additional heterozygous mutations in nuclear genes interacting with mt-tRNAGlu including EARS2 and TRMU" (PMID:33128823)
  - "only ~ 1/100 carriers develop the disease" (PMID:33128823)
- **Environmental risk factors:** none known. Acute decompensations, such as metabolic acidosis with liver failure, are described (PMID:27875839). No trigger such as infection has been shown, although by analogy with other mitochondrial diseases one is plausible. That analogy is inference, not documented evidence.
- **Protective factors and gene–environment interaction:** no data. The digenic RIRCD finding is the only documented gene–gene interaction.

---

## 3. Phenotypes

The Pelayo 2024 systematic review counts fewer than 50 published cases and proposes **severe, moderate and mild** groups based on the initial presentation (PMID:39173847). The original cohort was split into "mild" and "severe" groups (PMID:22492562).

| Phenotype | Type | Onset / course | Frequency (qualitative) | Key PMIDs | HPO lead (verify) |
|---|---|---|---|---|---|
| Hypotonia | sign | infancy, often the presenting sign | very frequent | 22492562, 27571996, 33962821, 40176842 | HP:0001252 Hypotonia |
| Psychomotor delay or regression | sign | infancy; partial recovery in mild cases | very frequent | 22492562, 27117034 | HP:0001263 Global developmental delay; HP:0002376 Developmental regression |
| Raised blood lactate / lactic acidosis | lab | persistent in severe cases, falls in mild cases | very frequent | 22492562, 27571996, 40176842 | HP:0002151 Increased serum lactate; HP:0003128 Lactic acidosis |
| Raised lactate on MRS / in CSF | lab / imaging | infancy | frequent | 22492562, 33962821 | HP:0002490 Increased CSF lactate |
| Symmetrical cerebral leukoencephalopathy | imaging | infancy; can improve, stay static or progress to atrophy | defining | 22492562 | HP:0002415 Leukodystrophy / HP:0002352 Leukoencephalopathy |
| Thalamic involvement (including absent thalami) | imaging | antenatal to infancy | defining | 22492562, 26619324 | thalamus abnormality term (look up) |
| Brainstem signal change (midbrain, pons, medulla) | imaging | infancy | defining | 22492562, 27571996 | brainstem abnormality term (look up) |
| Cerebellar white matter involvement | imaging | infancy | frequent | 22492562, 33962821 | look up |
| Corpus callosum agenesis or hypogenesis; thin corpus callosum | imaging, congenital | neonatal (severe form) | occasional | 26780086, 27571996, 25854774 | HP:0001274 Agenesis of corpus callosum |
| Seizures | sign | infancy or childhood | occasional | 27117034, 27206875 | HP:0001250 Seizure |
| Spasticity (lower limbs), pyramidal signs | sign | later course, severe group | occasional | 27206875 | HP:0001257 Spasticity |
| Dystonia, visual impairment | sign | severe subgroup | occasional | severe-subgroup commentary (see §11) | look up |
| Feeding difficulty, failure to thrive | sign | infancy | frequent | 25854774, 27571996 | HP:0001508 Failure to thrive |
| Liver dysfunction / hepatopathy | lab / sign | infancy, sometimes during acute crisis | occasional | 27571996, 27875839 | HP:0001410 Decreased liver function |
| Recurrent hypoglycemia | lab | neonatal (severe form) | rare | 26780086 | HP:0001943 Hypoglycemia |
| COX-deficient and ragged-red muscle fibres | histology | infancy | reported in biopsied cases | 27571996 | look up |
| Facial dysmorphism (metopic ridge, ptosis, sparse eyebrows, bulbous nose, large ears) | physical | infancy | 2 patients only | 40176842 | look up per feature |
| Humoral immune defect, recurrent respiratory infections | sign / lab | childhood | 1 patient only | 40389993 | look up |
| Cardiac: critical aortic stenosis, supraventricular tachycardia (SVT) | sign | neonatal | 1 patient; title only | 42778161 | look up |

Supporting excerpts:
- "Patients in the 'mild' group partially recovered and regained milestones in the following years" (PMID:22492562)
- "those of the 'severe' group were characterized by clinical stagnation, brain atrophy on magnetic resonance imaging" (PMID:22492562)
- "Patients with EARS2 deficiency typically present within the first year of life" (PMID:39173847)
- "Brain MRI revealed hypogenesis of the corpus callosum, T2 signal abnormalities in the medulla oblongata" (PMID:27571996)
- "The thalami were absent with the configuration of a developmental anomaly, without evidence of a lesion." (PMID:26619324)
- "Muscle histochemistry showed cytochrome c oxidase (COX)-deficient and ragged-red fibres" (PMID:27571996)

**Quality of life.** No EQ-5D, SF-36 or disease-specific QoL data exist. Severe cases are profoundly disabled or die in infancy. Mild cases keep motor and cognitive deficits of varying degree.

---

## 4. Genetic and molecular information

**Gene and protein.** *EARS2* (16p12.2) encodes a non-discriminating mitochondrial GluRS. It charges both mt-tRNA^Glu and mt-tRNA^Gln with glutamate in an ATP-dependent reaction. The Glu-tRNA^Gln it makes is then converted to Gln-tRNA^Gln by the GatCAB amidotransferase. The enzyme is located in the mitochondrial matrix (UniProt Q5JPH6).

**Pathogenic missense variants listed in UniProt** (all annotated COXPD12). Most were first reported in PMID:22492562:

| Variant | First report |
|---|---|
| p.Arg55His | PMID:22492562 |
| p.Lys65Glu | Talim letter, PMID:23008233 |
| p.Glu96Lys | PMID:22492562 |
| p.Arg107Cys | UniProt ref PMID:26741492, not checked here |
| p.Arg107His | PMID:22492562 |
| p.Arg108Trp (c.322C>T) | PMID:22492562 |
| p.Gly110Ser | PMID:22492562 |
| p.Cys167Tyr | PMID:22492562 |
| p.Arg168Gly | PMID:22492562 |
| p.Gly204Ser | PMID:22492562 |
| p.Gly224Ser | PMID:22492562 |
| p.Gly317Cys | PMID:22492562 |
| p.Thr426_Arg427delinsLeu | PMID:22492562 |
| p.Arg489Gln | UniProt ref PMID:26741492, not checked here |
| p.Arg516Gln | PMID:22492562 |

**Other reported alleles**

| Variant | Context | PMID |
|---|---|---|
| c.1A>G (p.Met1?), start-loss | previously reported | 27571996 |
| c.184A>T (p.Ile62Phe) | | 27571996 |
| c.376C>T (p.Gln126\*) | | 32887222 |
| c.670G>A (p.Gly224Ser) | | 32887222 |
| c.164G>T (p.Arg55Leu) | | 33962821 |
| c.484C>T (p.Arg162Trp) | | 33962821 |
| c.1304T>A (p.Leu435Gln) | in trans with c.319C>T (p.Arg107Cys) | 40389993 |
| c.949G>T (p.Gly317Cys) | homozygous, neonatal | 33855712 |
| c.322C>T (p.Arg108Trp) | homozygous, mild early-onset | 26893310 |
| c.319C>T (p.Arg107Cys) | described as "common" in a Turkish report | 40176842 |
| c.1064A>G (p.Asn355Ser) + c.1488+2T>A | late-onset adult case; transcript NM_001083614 | 32802952 |

MedlinePlus Genetics says more than 23 LTBL variants are known; that count is out of date.

- **Variant classes:** mostly missense, with some nonsense, start-loss, splice and in-frame indel alleles. No patient has been reported with two null alleles. This fits an assumption that some residual activity is needed for viability; that is inferred, not demonstrated.
- **Origin:** germline.
- **Population frequency:** individual alleles are rare in gnomAD (gnomAD was not queried here). Disease prevalence is unknown.
- **Functional consequence:** loss of function, mostly reduced protein. Patient fibroblasts and muscle show markedly reduced EARS2 protein (PMID:26780086, 27571996). In the late-onset case, transcript levels were normal but protein was reduced, "suggesting an increased degradation rate of the mutated protein" (PMID:32802952).
- **Genotype–phenotype:** "no genotype-phenotype correlation has been identified" (PMID:39173847). Fibroblast metabolomics can separate milder from severe variants: "discriminate between EARS2 variants causing relatively mild and severe COXPD12" (PMID:33855712).
- **Caution on functional evidence.** A variant that impairs function in vitro does not establish causation in vivo. In McNeill 2017, a patient with *EARS2* variants that impaired mitochondrial function in cells was ultimately explained by a *SNORD118* variant (PMID:28748214).
- **Modifier genes, epigenetics, chromosomal abnormalities:** none described. As a modifier, *EARS2* appears only in RIRCD (§2).

---

## 5. Environmental information

No environmental, lifestyle or infectious cause is known. This section does not apply beyond the possibility of nonspecific metabolic decompensation.

---

## 6. Mechanism and pathophysiology

### Causal chain

1. **Biallelic *EARS2* variants** reduce the stability or abundance of mtGluRS, and in some alleles catalytic function. Reduced protein is demonstrated in patient cells (PMID:26780086, 27571996, 32802952). Reduced catalytic activity of specific mutants is inferred; no aminoacylation kinetics were found for any patient allele.
2. **This leads to less aminoacylation of mt-tRNA^Glu**, and also of mt-tRNA^Gln, because mtGluRS supplies the Glu-tRNA^Gln that is amidated to Gln-tRNA^Gln. The mt-tRNA^Gln effect is inferred from enzyme biology.
3. **This results in impaired mitochondrial translation** of the 13 mtDNA-encoded OXPHOS subunits (PMID:33855712, background).
4. **This leads to combined deficiency of respiratory-chain complexes I, III and IV**, which contain mtDNA-encoded subunits; complex II, entirely nuclear-encoded, is spared.
   - "multiple defects of mitochondrial DNA-related respiratory-chain complexes constitute a frequent biochemical signature" (PMID:22492562)
   - Muscle in one patient showed reduced complex I and IV activity and reduced subunit levels (PMID:27571996).
5. **This leads to bioenergetic failure and metabolic rewiring.** A shift to glycolysis drives lactate accumulation, and the TCA cycle, purine/pyrimidine and fatty-acid metabolism are disturbed (PMID:33855712). ROS rise and mitochondrial morphology changes (PMID:26780086). Mitochondrial membrane potential and respiration fall when cognate amino acids are depleted (PMID:42863838).
   - **Branch 5a: compensation.** Neuronal progenitors activate specific branches of the integrated stress response (ISR) and keep OXPHOS balanced, but mature neurons do this less well (PMID:37975900; in vitro, including *EARS2* lines). In the related RIRCD, recovery runs through FGF21/GDF15 stress signalling, then mTOR activation and mitochondrial biogenesis (PMID:33128823). Whether the same programme explains partial recovery in mild LTBL is a **hypothesis**.
6. **Region-specific vulnerability** of energy-demanding, actively myelinating white matter and of the thalamus and brainstem leads to the symmetrical leukoencephalopathy and deep grey matter and brainstem lesions. The selective tract and region pattern is not explained mechanistically. Oligodendrocyte and myelination vulnerability is inferred, consistent with the framing of mt-aaRS disorders as "developmental disorders of myelination" (Fine 2019; title only, PMID:31839000).
   - **Branch 6a: antenatal onset.** Injury during development produces corpus callosum agenesis and developmentally absent thalami (PMID:26780086, 26619324).
   - **Branch 6b: age-dependent dynamics.** Lesions can remit and then recur: lesions shrank at age 3, new lesions appeared at age 8, and lesions improved again later (PMID:33962821).
7. **Clinical outcome.** This leads to hypotonia, developmental delay or regression, seizures, spasticity and lactic acidosis. In the **severe** branch, systemic involvement adds liver dysfunction, hypoglycemia and death in infancy (PMID:26780086, 27571996, 27875839). In the **mild** branch, there is partial clinical and MRI recovery from the second year onward (PMID:22492562, 25854774).
8. **Possible extra-neural branch (single case).** Mitochondrial dysfunction in B cells reduced CD38, impaired B-cell differentiation and B-cell receptor signalling, and was associated with hypogammaglobulinemia-type humoral defects and infections (PMID:40389993).

### Suggested annotations (all leads; verify)

- **GO molecular function:** glutamate-tRNA ligase activity (GO:0004818); also look up the glutamyl-tRNA(Gln) amidotransferase-substrate role.
- **GO biological process:** tRNA aminoacylation for mitochondrial protein translation (GO:0070127); mitochondrial translation (GO:0032543); mitochondrial respiratory chain complex assembly or oxidative phosphorylation (GO:0006119); integrated stress response signaling (look up); myelination (GO:0042552); glycolytic process (GO:0006096, with modifier INCREASED).
- **GO cellular component:** mitochondrial matrix (GO:0005759).
- **CL:** oligodendrocyte (CL:0000128); neuron (CL:0000540); astrocyte (CL:0000127); skeletal muscle fiber (CL:0008002); hepatocyte (CL:0000182); B cell (CL:0000236).
- **CHEBI:** L-lactate (CHEBI:16651); L-glutamate (CHEBI:29985); L-glutamine (CHEBI:58359).

**Molecular profiling**
- Fibroblast metabolomics (PMID:33855712).
- iPSC-derived neuronal RNA-seq showing dysregulated neuronal differentiation and translation (PMID:37975900).
- Muscle stress-response profiling in RIRCD (PMID:33128823).
- No GEO dataset specific to LTBL was identified; GEO was not searched in depth.

---

## 7. Anatomical structures affected

- **Primary:** brain. This includes cerebral white matter (deep and subcortical, sparing the periventricular rim), thalamus, midbrain, pons, medulla oblongata, cerebellar white matter, corpus callosum, and sometimes the basal ganglia (caudate, pallidum; PMID:25854774) and dentate nucleus or tegmentum (PMID:40176842).
- **Secondary:**
  - skeletal muscle (COX-negative and ragged-red fibres);
  - liver (hepatopathy);
  - metabolism and the endocrine system (hypoglycemia);
  - immune system (B cells; one case);
  - heart (one neonatal case, title only).
- **Subcellular:** mitochondrial matrix and the mitochondrial ribosome / translation machinery.
- **Laterality:** characteristically bilateral and symmetrical. Asymmetric late lesions have been reported, for example new left caudate and pallidum lesions (PMID:25854774).
- **UBERON leads (verify):**

| Structure | UBERON lead |
|---|---|
| cerebral white matter | UBERON:0002437 |
| thalamus | UBERON:0001897 |
| midbrain | UBERON:0001891 |
| pons | UBERON:0000988 |
| medulla oblongata | UBERON:0001896 |
| cerebellar white matter | UBERON:0002317 |
| corpus callosum | UBERON:0002336 |
| liver | UBERON:0002107 |
| skeletal muscle tissue | UBERON:0001134 |

---

## 8. Temporal development

- **Onset:** usually within the first year of life (PMID:39173847). The neonatal form can begin antenatally, with corpus callosum agenesis and absent thalami (PMID:26619324, 26780086).
- **Late-onset outlier:** a single patient presented at about 63 years with mood change, then tremor, parkinsonism and cognitive decline. MRI showed confluent white matter disease without thalamic or brainstem lesions, and "The serum lactate level was within normal limits." (PMID:32802952). The authors themselves call causality uncertain; treat this case as provisional.
- **Course:**
  - Pelayo describes three patterns: a rapidly progressive neonatal form with early death; an early-onset severe form that progresses slowly; and an early-onset milder form with improvement (PMID:39173847).
  - Biphasic courses are described (PMID:27117034, 27875839).
  - Mild disease shows clinical and MRI improvement from the second year (PMID:25854774, 27206875).
  - Relapse can happen: new lesions appeared years later in PMID:25854774 and 33962821.
  - Severe disease leads to stagnation and atrophy (PMID:22492562).
- **Critical window:** infancy, which coincides with peak myelination. This is an inference.

---

## 9. Inheritance and population

- **Inheritance:** autosomal recessive (HP:0000007, lead). Penetrance appears complete for biallelic pathogenic genotypes. Expressivity varies widely, even between siblings (PMID:27206875).
- **Anticipation and mosaicism:** not applicable or not reported.
- **Epidemiology:** prevalence is unknown, with fewer than 50 published cases worldwide (PMID:39173847). Cases come from Europe (the Netherlands, Portugal, Italy, Spain), Turkey (several homozygous cases), Japan, China and North America.
- **Founder effect:** c.319C>T (p.Arg107Cys) is called a "common genetic variant" in a Turkish report (PMID:40176842). There is no formal founder analysis.
- **Sex ratio:** no bias expected; male predominance in the reported cases is likely chance.
- **Carrier frequency:** no estimate exists. One could be derived from gnomAD, but that was not done here.

---

## 10. Diagnostics

**Core diagnostic tests**
- **Brain MRI** showing the pattern is "the hallmark of the disease" (PMID:25854774).
- **MRS** showing a lactate doublet; myo-inositol peaks are also described (PMID:33962821).
- **Blood and CSF lactate** (PMID:27875839 stresses "the utility of blood lactate quantification"). The LOINC lead for lactate in blood is 2524-7 (verify; the repo's LOINC seeding workflow applies).
- **Exome or genome sequencing**, the usual route to diagnosis. Rapid genetic testing can make muscle biopsy unnecessary (PMID:27875839).

**Supporting tests**
- **Muscle biopsy:** COX-deficient and ragged-red fibres; reduced complex I and IV activity (PMID:27571996).
- **Fibroblasts:** reduced EARS2 protein on western blot, raised ROS, live-cell bioenergetics (PMID:26780086).
- **Fibroblast metabolomics** (PMID:33855712) and an amino-acid-depletion Seahorse assay proposed for interpreting variants (PMID:42863838).
- **Serum FGF21:** markedly raised in a mixed mt-aaRS cohort (n=6, mean about 882 pg/mL versus about 21 pg/mL in controls). The reported AUC of 1.0 is very likely optimistic given the sample size (PMID:41096790).

**Other testing**
- Gene panels: leukodystrophy, mitochondrial and mt-aaRS panels all include *EARS2*.
- Mitochondrial DNA testing helps exclude MT-TE / RIRCD.
- Karyotype, chromosomal microarray, FISH and repeat-expansion testing are not useful.

**Differential diagnosis**
- **DARS2-LBSL** (leukoencephalopathy with brainstem and spinal cord involvement and lactate elevation): spinal cord involvement, slower course.
- Other mt-aaRS leukoencephalopathies: AARS2, RARS2 (pontocerebellar hypoplasia), MARS2, FARS2.
- Leigh syndrome.
- RIRCD (m.14674T>C).
- Other causes of corpus callosum agenesis with lactic acidosis, such as PDH deficiency.
- Aicardi-Goutières syndrome or Labrune syndrome (*SNORD118*) when calcifications or cysts are present (PMID:28748214).
- MRI pattern comparison across mt-aaRS disorders: Roux 2021 (PMID:33972171; title only).

**Screening:** no newborn screening exists. Cascade carrier testing and prenatal or preimplantation testing are possible once the familial variants are known.

---

## 11. Outcome and prognosis

- **Severe or neonatal form:** death in infancy, for example at 5 months (PMID:27571996) or in the neonatal period (PMID:26780086, 33855712, Talim 2013).
- **Moderate form:** survival with stagnation, spasticity, dystonia, visual impairment and seizures. A journal commentary on McNeill et al. describes this "severe" subgroup (cited in search results; not checked at source).
- **Mild form:** survival with regained milestones and MRI improvement. Residual deficits are possible, and late lesions can appear.
- **Prognostic factors:** severity at presentation appears to predict later course (PMID:39173847). Persistent lactate elevation and atrophy go with the severe course (PMID:22492562).
- **Survival statistics:** none.

---

## 12. Treatment

There is **no approved disease-modifying therapy**. Management is supportive. NCIT leads below need verification.

| Approach | Evidence | NCIT lead |
|---|---|---|
| Oral cognate amino-acid supplementation (glutamate / glutamine for EARS2) | Preliminary open-label series of 9 mt-aaRS patients that included EARS2. Well tolerated; improvements in development, growth and/or cardiac function; 2 patients regressed after stopping. The EARS2-specific breakdown and doses are not in the abstract (PMID:42863838) | Pharmacotherapy (NCIT:C15986) or Dietary Intervention (NCIT:C15447); therapeutic_agent: L-glutamine (CHEBI lead) |
| Mitochondrial "cocktail" (coenzyme Q10, riboflavin, carnitine, etc.) | Used empirically; no LTBL-specific evidence found | Nutritional Support (NCIT:C15433). Per CLAUDE.md, assign the modality per agent, not as BEHAVIORAL |
| Correction of acute lactic acidosis and hypoglycemia; liver support | Case-level (PMID:27875839, 26780086) | Supportive Care (NCIT:C15747) |
| Antiseizure medication | Standard care | Pharmacotherapy (NCIT:C15986) |
| Physical, occupational and speech therapy; feeding support (gastrostomy) | Standard care | NCIT:C15302 / C121351 / C159273 |
| Levodopa (late-onset parkinsonian case) | Partial benefit for tremor (PMID:32802952) | Pharmacotherapy |
| Immunoglobulin replacement (B-cell defect case) | Not reported; would follow from the defect (PMID:40389993) | look up |

- **Experimental therapies:** no NCT trial specific to *EARS2* was found. Gene therapy and mRNA therapy are only preclinical concepts.
- **Drugs to avoid:** standard mitochondrial-disease cautions apply, such as valproate and prolonged propofol. These are general guidance, not LTBL-specific evidence.

---

## 13. Prevention

- **Primary:** genetic counselling. Recurrence risk is 25% for parents who are both carriers. Carrier testing of relatives, and prenatal or preimplantation genetic testing, are options once the variants are known.
- **Secondary:** early exome sequencing in any infant with the MRI pattern plus high lactate.
- **Tertiary:** avoid catabolic stress, manage intercurrent illness early, and monitor liver function and glucose in infants.
- **Vaccination, public-health and environmental measures:** not applicable.

---

## 14. Other species and natural disease

- No naturally occurring *EARS2* disease is known in OMIA; OMIA was not searched in depth.
- **Orthologs:** mouse *Ears2* (MGI:1914667) and zebrafish *ears2* (also known as zgc:153247). Glutamyl-tRNA synthetase function is conserved down to bacteria, where GluRS is often also non-discriminating.
- **Zoonotic potential:** not applicable.

---

## 15. Model organisms

| Model | What is known |
|---|---|
| Mouse *Ears2* knockout (IMPC) | The [IMPC page](https://www.mousephenotype.org/data/genes/MGI:1914667) showed no significant phenotypes across the 19 systems tested. The viability result did not render, so whether the null is embryonic lethal is unconfirmed. A vendor sells a conditional knockout; no published phenotype was found |
| Zebrafish | No published *ears2* mutant or morphant study found |
| Patient fibroblasts | Reduced EARS2 protein, raised ROS, altered morphology, metabolomic signatures, amino-acid-depletion respirometry (PMID:26780086, 33855712, 42863838, 32887222) |
| iPSC-derived neural progenitors and neurons with biallelic *EARS2* variants (alongside *AARS2* and *RARS2*) | Translation defect is compensated in progenitors but less so in mature neurons; ISR branches are mutation-specific (PMID:37975900) |

- **Biggest gap:** there is no in vivo model that reproduces the leukoencephalopathy. A conditional central-nervous-system or oligodendrocyte knockout, or a knock-in of patient alleles, would be the obvious next model.
- In a future KB entry this would fit a `HUMAN_MODEL_MISMATCH` or `KNOWLEDGE_GAP` discussion.

---

## Key gaps for curation

1. No aminoacylation kinetics for any patient allele; the loss of mechanism is inferred mainly from reduced protein.
2. The Talim 2013 letter, the Prasun 2019 "broad spectrum" paper, and the Roux 2021 MRI study are title or metadata only here. Fetch their full texts before citing details.
3. The Monfrini 2020 late-onset case may represent a broader phenotype, but its causality is uncertain.
4. No natural-history cohort, prevalence estimate or QoL data exist.

---

## Sources

- Steenweg 2012, PMID:22492562 ([VU record](https://research.vu.nl/en/publications/leukoencephalopathy-with-thalamus-and-brainstem-involvement-and-h/))
- Talim 2013, PMID:23008233 ([Newcastle eprints](https://eprints.ncl.ac.uk/191485))
- Biancheri 2015, PMID:25854774
- Kevelam 2016, PMID:26619324
- Danhauser 2016, PMID:26780086
- Taskin 2016, PMID:26893310
- Güngör 2016, PMID:27117034
- Şahin 2016, PMID:27206875
- Oliveira 2017, PMID:27571996
- Sellars 2017, PMID:27875839
- McNeill 2017, PMID:28748214
- Monfrini 2020, PMID:32802952 ([PMC7413628](https://pmc.ncbi.nlm.nih.gov/articles/PMC7413628/))
- Barbosa-Gouveia 2020, PMID:32887222
- Hathazi 2020, PMID:33128823
- Ni 2021, PMID:33855712
- Sawada 2021, PMID:33962821
- Podmanicky 2024, PMID:37975900
- Pelayo 2024, PMID:39173847 ([DOAJ](https://doaj.org/article/9fad257c3ea54ff6adaa664dad31f18f))
- Bahar Ister 2025, PMID:40176842
- Wen 2025, PMID:40389993
- Tekin Neijmann 2025, PMID:41096790
- Muffels 2026, PMID:42863838
- Akduman 2026, PMID:42778161 (title only)
- [UniProt Q5JPH6](https://rest.uniprot.org/uniprotkb/Q5JPH6.txt)
- [MedlinePlus Genetics: LTBL](https://ghr.nlm.nih.gov/condition/leukoencephalopathy-with-thalamus-and-brainstem-involvement-and-high-lactate)
- [MedlinePlus Genetics: EARS2 gene](https://ghr.nlm.nih.gov/gene/EARS2)
- [MedGen 1645614](https://https.ncbi.nlm.nih.gov/medgen/1645614)
- [Qeios (Orphanet mirror)](https://www.qeios.com/read/8AU4UZ/pdf)
- [MalaCards COXPD12](https://malacards.org/card/combined_oxidative_phosphorylation_deficiency_12)
- [IMPC Ears2](https://www.mousephenotype.org/data/genes/MGI:1914667)
- [LOVD EARS2](https://databases.lovd.nl/shared/transcripts/00006828)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 27 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 18 |
| Quoted claims found in source | 17 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 27 |
| On topic | 24 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMID:31839000`: "developmental disorders of myelination"
  - Text part not found as substring: 'developmental disorders of myelination'

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 48 |
| Resolved | 46 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 17 |
| Terms named correctly | 10 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0013971` (1 mention) - the report calls it "given in the brief"; MONDO calls it **leukoencephalopathy-thalamus and brainstem anomalies-high lactate syndrome**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0004818` (1 mention) - the report calls it "GO molecular function:** glutamate-tRNA ligase activity"; GO calls it **glutamate-tRNA ligase activity**
- `GO:0005759` (1 mention) - the report calls it "GO cellular component:** mitochondrial matrix"; GO calls it **mitochondrial matrix**
- `CL:0000128` (1 mention) - the report calls it "CL:** oligodendrocyte"; CL calls it **oligodendrocyte**
- `CHEBI:16651` (1 mention) - the report calls it "CHEBI:** L-lactate"; CHEBI calls it **(S)-lactate**, and lists "L(+)-lactate" among its other names
- `UBERON:0001897` (1 mention) - the report calls it "thalamus"; UBERON calls it **dorsal plus ventral thalamus**, and lists "thalamus" among its other names
- `UBERON:0002317` (1 mention) - the report calls it "cerebellar white matter"; UBERON calls it **white matter of cerebellum**, and lists "cerebellar white matter" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MGI:1914667` - called "Ears2", "Orthologs:** mouse *Ears2"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.