---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-11-11T19:28:53.775064'
end_time: '2026-11-11T19:47:21.245335'
duration_seconds: 1107.47
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: NUT Carcinoma
  mondo_id: MONDO:0005563
  category: ''
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: Midline carcinoma of children and Young adults with NUT rearrangement;
    NMC; carcinoma with t(15;19)(q13;p13.1) translocation; nuclear protein in testis
    midline carcinoma
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
  - claude-haiku-4-5-20251001
  - claude-opus-5
  web_search_requests: 15
  num_turns: 71
  total_cost_usd: 11.044642499999995
  session_id: fb5cbccf-2d0d-4402-b41a-944b0cee4e76
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 56
reference_validation:
  total_references: 42
  verified: 42
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 38
  quotes_valid: 10
  quotes_unsupported: 28
  unsupported_quote_references:
  - PMID:41737331
  - PMID:33452461
  - PMID:35957893
  - PMID:42865603
  - PMC:PMC13655413
  - PMID:39447095
  - PMID:26220994
  - PMID:21447744
  - PMID:38724194
  - PMID:41266112
  - PMC:PMC12634820
  - PMC:PMC7914217
  - PMID:39900969
  - PMID:35417004
  - PMC:PMC9197941
  - PMID:26976114
  relevance_assessed: 42
  on_topic: 40
  needs_review: true
  validator_version: 0.5.1
term_validation:
  total_terms: 67
  verified: 56
  not_found: 0
  obsolete: 3
  unverifiable: 8
  confabulation_rate: 0.0
  labels_checked: 5
  labels_matching: 0
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: MONDO:0005563
    reported_labels:
    - MONDO
    ontology_label: nut midline carcinoma
  - term_id: DOID:0060463
    reported_labels:
    - DOID
    ontology_label: NUT midline carcinoma
  - term_id: EFO:0005783
    reported_labels:
    - EFO
    ontology_label: obsolete_NUT midline carcinoma
  - term_id: NCIT:C93352
    reported_labels:
    - verify
    ontology_label: Targeted Therapy
  - term_id: NCIT:C15433
    reported_labels:
    - verify
    ontology_label: Nutritional Support
  obsolete_terms:
  - term_id: EFO:0005783
    ontology_label: obsolete_NUT midline carcinoma
    replaced_by: http://purl.obolibrary.org/obo/MONDO:0005563
  - term_id: GO:0043974
    ontology_label: obsolete histone H3-K27 acetylation
  - term_id: GO:0070577
    ontology_label: obsolete lysine-acetylated histone binding
    replaced_by: GO:0140566
  unresolvable_prefixes:
  - ORPHA
  - LOINC
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** NUT Carcinoma
- **MONDO ID:** MONDO:0005563 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** Midline carcinoma of children and Young adults with NUT rearrangement; NMC; carcinoma with t(15;19)(q13;p13.1) translocation; nuclear protein in testis midline carcinoma
- **Category:** 

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **NUT Carcinoma** covering all of the
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

I'll research this now across the literature and primary databases.

# NUT Carcinoma (MONDO:0005563) — Comprehensive Disease Characteristics Research Report

**Prepared:** 11 November 2026
**Target:** NUT carcinoma (NC), formerly NUT midline carcinoma (NMC)
**MONDO:** MONDO:0005563

---

## Scope note and a caution about identifiers

**Causal gene: `NUTM1`** (NUT midline carcinoma family member 1; formerly *NUT* / *C15orf55*; HGNC:29919; OMIM \*608963; NCBI Gene 256646; chromosome **15q14**). NUT carcinoma is **defined** — not merely associated — by a somatic rearrangement of *NUTM1*, most often an in-frame fusion to *BRD4* (HGNC:13575; OMIM \*608749; 19p13.12) produced by the balanced reciprocal translocation **t(15;19)(q14;p13.1)**. There is no germline gene, no inherited form, and no serial-numbered OMIM phenotype entry for this disease; the two relevant OMIM records are the *gene* entries \*608963 (*NUTM1*) and \*608749 (*BRD4*).

**Two naming traps that matter for knowledge-base work:**

1. The MONDO label (`nut midline carcinoma`) is the **superseded** name. WHO dropped "midline" in the 5th-edition classifications because the tumour is not confined to midline structures (kidney, pancreas, bone, skin adnexa, bladder are all documented). The current entity name is **NUT carcinoma**.
2. ***NUTM1* fusions are not specific to this disease.** The same gene is rearranged in *NUTM1*-rearranged B-lymphoblastic leukaemia, in *CIC::NUTM1* and *MGA::NUTM1* sarcomas, and in cutaneous poroma/porocarcinoma — all **different diseases** with different partners, different lineages, and markedly different prognoses ([Hsiao et al., *Pediatr Blood Cancer* 2023, PMID:37082775](https://pmc.ncbi.nlm.nih.gov/articles/PMC10432870/)). Do not merge them under this MONDO ID.

**Ontology CURIE caveat.** Every CURIE below marked **(verify)** is a *lead only* — reconstructed from domain knowledge, not resolved against the ontology in the step it was written. Per this repository's own rule (*Every CURIE is read from a source in the same step it is written*), each must be looked up with OAK/OLS and its canonical label copied before being bound. CURIEs not so marked were read from a source during this session.

---

## 1. Disease Information

### 1.1 Overview

NUT carcinoma is a rare, highly aggressive, poorly differentiated carcinoma defined genetically by rearrangement of *NUTM1* at 15q14. It most often arises in the thorax (lung, mediastinum/thymus) and the head and neck (sinonasal tract, nasopharynx, salivary glands, orbit), typically presents at advanced stage, responds poorly to conventional cytotoxic therapy, and carries a median overall survival of roughly 6–9 months.

> "NUT carcinoma (NC) is a rare and highly aggressive malignancy characterized by *NUTM1* gene fusions." — [Zhang et al., *Innovation (Camb)* 2025, PMID:41737331](https://pubmed.ncbi.nlm.nih.gov/41737331/)

> "NUT carcinomas (NC) are very rare and highly aggressive tumors, molecularly defined by an aberrant gene fusion involving the *NUTM1* gene. NCs preferentially arise intrathoracically or in the head and neck region, having a highly adverse prognosis with almost no long-term survivors." — [Kloker et al., *Lung Cancer* 2024;189:107496, PMID:38301600](https://pubmed.ncbi.nlm.nih.gov/38301600/)

A major 2025 reframing argues NC is not an orphan entity at all but an **unrecognised molecular subtype of squamous cell carcinoma**:

> "Hiding in plain sight: NUT carcinoma is an unrecognized subtype of squamous cell carcinoma of the lungs and head and neck." — [Luo J, Bishop JA, DuBois SG, Hanna GJ, Sholl LM, Stelow EB, Thompson LDR, Shapiro GI, French CA. *Nat Rev Clin Oncol.* 2025 Apr;22(4):292–306. PMID:39900969](https://www.nature.com/articles/s41571-025-00986-3)

That review estimates **~1,400 new cases per year in the United States**, which would exceed the incidence of several recognised NSCLC and HNSCC subtypes — against only ~20 cases/year captured by the International NUT Carcinoma Registry. The gap is attributed to systematic underdiagnosis rather than to true rarity.

### 1.2 Key identifiers

| Resource | Identifier | Notes |
|---|---|---|
| **MONDO** | MONDO:0005563 | label `nut midline carcinoma` (superseded name) |
| **ICD-O-3.2** | **8023/3** | "NUT carcinoma"; introduced in the ICD-O-3.2 update ([ENCR, 2021](https://www.encr.eu/sites/default/files/inline-files/Changes%20ICD-O-3.2.pdf)) |
| **ICD-11** | **XH2855** (morphology) | "nuclear protein in testis (NUT) associated carcinoma"; combined with a site stem code (e.g. 2D42 for ill-defined sites) ([PathologyOutlines](https://www.pathologyoutlines.com/topic/nasalnutcarcinoma.html)) |
| **ICD-10** | site-dependent (C34.x lung; C30–C31 sinonasal; C38.3 mediastinum; C76/C80 ill-defined) | no dedicated behaviour code |
| **NCIT** | C45716 | from MONDO xrefs |
| **Orphanet** | ORPHA:443167 | from MONDO xrefs |
| **DOID** | DOID:0060463 | |
| **EFO** | EFO:0005783 | |
| **UMLS** | C1707291 | |
| **MedGen** | 312999 | |
| **GARD** | 0021852 | |
| **OncoTree** | NMCHN | |
| **OMIM (gene)** | \*608963 (*NUTM1*), \*608749 (*BRD4*) | no phenotype MIM |
| **WHO** | *Thoracic Tumours* 5th ed. (2021); *Head and Neck Tumours* 5th ed. (2022) | listed as a distinct entity in both |

MONDO definition (verbatim, from OLS4):

> "A rare, highly aggressive and lethal carcinoma that affects children and young adults. It arises from midline epithelial structures, most commonly the head, neck, and mediastinum. It is a poorly differentiated carcinoma and is characterized by mutations and rearrangement of the NUT gene. A balanced translocation t(15;19) is present that results in the creation of a fusion gene involving the NUT gene, most commonly BRD4-NUT fusion gene."

### 1.3 Synonyms

NUT carcinoma; NUT midline carcinoma; NMC; midline carcinoma of children and young adults with NUT rearrangement; carcinoma with t(15;19)(q13;p13.1) translocation; nuclear protein in testis midline carcinoma; nuclear protein in testis (NUT)-associated carcinoma; *NUTM1*-rearranged carcinoma. Historically described as "aggressive t(15;19)-positive carcinoma" and "lethal midline carcinoma of young people."

### 1.4 Nature of the evidence base

Almost all clinical knowledge derives from **aggregated, disease-level sources** rather than individual EHR records:

- **International NUT Carcinoma Registry** (www.nc-registry.org / nmcregistry.org), Brigham and Women's Hospital — the single largest curated clinical series ([French et al., *Clin Cancer Res* 2022, PMID:35417004](https://pmc.ncbi.nlm.nih.gov/articles/PMC9197941/)).
- **SEER** — population-based but small (n=45 and n=91 in two analyses), with cases only from 2018 onwards once ICD-O 8023/3 existed ([PMID:40486575](https://pubmed.ncbi.nlm.nih.gov/40486575/); [PMID:42870800](https://pubmed.ncbi.nlm.nih.gov/42870800/)).
- **Commercial molecular profiling cohorts** (Caris) — 54 cases with paired DNA/RNA and immune profiling ([Kroening et al., *JCO Precis Oncol* 2024, PMID:39447095](https://ascopubs.org/doi/10.1200/PO.24.00334)).
- Multiple single-institution and national retrospective series (Germany n=35; France n=12; Korea n=13).
- Case reports and small series dominate the long tail, with the attendant publication bias toward unusual sites and unusual survivors.

**Caveat for any prevalence or frequency figure below:** because an estimated majority of cases are never correctly diagnosed, every denominator in the literature is biased toward centres that test for NUT.

---

## 2. Etiology

### 2.1 Disease causal factor

The disease has a **single, sufficient, somatic genetic cause**: an in-frame fusion placing nearly the entire *NUTM1* open reading frame downstream of a chromatin-binding partner. This is the defining lesion, the only recurrent lesion, and — in mouse models — sufficient on its own to initiate the tumour.

> "About 70% of NUT carcinoma is associated with chromosome translocation events that lead to the formation of a *BRD4::NUTM1* fusion gene." — [Zheng et al., *Life Sci Alliance* 2024;7(7):e202402602, PMID:38724194](https://www.life-science-alliance.org/content/7/7/e202402602)

The genome is otherwise remarkably quiet:

> "NCs are genomically stable… Apart from the *NUTM1*-fusion, NCs lack oncogenic mutations, have low tumor mutation burdens, and have few, if any, copy number alterations." — [Eagen & French, *Oncogene* 2021, PMID:33452461](https://pmc.ncbi.nlm.nih.gov/articles/PMC7914217/)

> "Unlike other solid tumors with complex chromosomal rearrangements and a high mutational burden, NCs display a simple karyotype, often with only one alteration comprising the translocation." — [Moreno et al., *Front Oncol* 2022, PMID:35957893](https://pmc.ncbi.nlm.nih.gov/articles/PMC9360329/)

**Causal sufficiency is demonstrated *in vivo***, not merely inferred. A cre/lox + CRISPR "NUT carcinoma translocator" (NCT) mouse engineers the syntenic mouse **t(2;17)** (mouse *Nutm1* on chr 2, *Brd4* on chr 17) and produces tumours with **100% penetrance** in every lineage tested: KRT14-Cre head and neck (n>50), Pdx1-Cre pancreas (18/18), Prrx1-Cre soft tissue (9/9), NLS-Cre constitutive (25/25) ([PMID:38724194](https://www.life-science-alliance.org/content/7/7/e202402602)).

### 2.2 Risk factors

**Genetic risk factors — none identified.** There is no reported familial clustering, no germline predisposition syndrome, no susceptibility locus from GWAS, and no modifier gene. The *NUTM1* fusion is **somatic and acquired**; it is not present in constitutional tissue. There is no carrier state and no reported germline mosaicism. No ClinVar germline pathogenic variant in *NUTM1* is associated with this disease.

**Environmental risk factors — none identified.** This is an unusually clean negative in oncology and should be recorded as a positive finding, not as missing data:

> "There is no evidence of an association between environmental exposure, infectious agents, or tobacco exposure and NC." — [Xie et al., *Histol Histopathol* 2025;40:1839–1846](https://www.hh.um.es/pdf/Vol_40/40_11/Xie-40-1839-1846-2025.pdf)

Specifically:
- **Tobacco:** among 42 pulmonary NC cases with documented smoking status, **66.7% were never-smokers** and 33.3% smokers ([PMID:42865603](https://pmc.ncbi.nlm.nih.gov/articles/PMC13655413)) — the inverse of the pattern for conventional lung squamous cell carcinoma. This is the strongest single argument against a tobacco aetiology.
- **HPV and EBV:** no case reported to date has been associated with either virus. NC is consistently p16/HPV-negative and EBER-negative, which is diagnostically useful (see §10.4).
- **Occupational exposure, radiation, diet, alcohol:** no reported association. No study has had the statistical power to exclude a modest effect.

**Demographic correlates (associations, not established risk factors):**
- **Age:** strongly enriched in adolescents and young adults. Molecular-profiling data show NC prevalence is **~10× higher in patients under 50 than in those over 70** ([Kroening 2024, PMID:39447095](https://ascopubs.org/doi/10.1200/PO.24.00334)). Why a *de novo* translocation should favour young people is unexplained and is a genuine open question.
- **Sex:** approximately balanced. Registry (n=141): 48% male / 52% female ([Chau et al., *JNCI* 2020, PMID:32328562](https://pmc.ncbi.nlm.nih.gov/articles/PMC7165803/)). Other series report 57%/43% male-biased ([PMID:35957893](https://pmc.ncbi.nlm.nih.gov/articles/PMC9360329/)) and a 1.89:1 male:female ratio in pulmonary cases ([PMID:42865603](https://pmc.ncbi.nlm.nih.gov/articles/PMC13655413)). The spread across series is consistent with no real sex effect.
- **Ancestry/geography:** no established difference. The apparent US concentration (49% of 310 identified cases) reflects where NUT IHC is performed, not where the disease occurs ([PMID:35957893](https://pmc.ncbi.nlm.nih.gov/articles/PMC9360329/)).

### 2.3 Protective factors

No genetic or environmental protective factor has been identified. gnomAD contains no protective *NUTM1* allele relevant to this disease. There is no evidence for dietary or lifestyle protection.

### 2.4 Gene–environment interactions

**Not applicable / none described.** With no established environmental exposure, there is no GxE interaction to report. CTD contains no chemical–disease association for NUT carcinoma specifically.

**One mechanistic interaction worth noting** sits at the gene–drug rather than gene–environment interface: the *identity of the fusion partner* modifies response to BET inhibitors. Across three independent phase I trials, responders were disproportionately patients with **non-BRD4** fusions (BRD3-NUT, NSD3-NUT) ([PMID:35417004](https://pmc.ncbi.nlm.nih.gov/articles/PMC9197941/)) — see §12.

---

## 3. Phenotypes

NUT carcinoma has **no constitutional phenotype**. Its clinical features are entirely those of a rapidly growing, locally destructive, early-metastasising carcinoma, and they are therefore determined by the primary site. There is no HPO-codeable syndromic gestalt.

### 3.1 Site-independent features

| Phenotype | Type | Frequency | Onset/course | Candidate HPO term |
|---|---|---|---|---|
| Rapidly enlarging mass | clinical sign | near-universal | acute/subacute; weeks | Neoplasm — HP:0002664 **(verify)** |
| Constitutional symptoms (weight loss, fatigue, fever) | symptom | common | subacute | Weight loss HP:0001824 **(verify)**; Fever HP:0001945 **(verify)** |
| Regional lymphadenopathy | clinical sign | **91.9%** in pulmonary NC | present at diagnosis | Lymphadenopathy HP:0002716 **(verify)** |
| Distant metastasis at diagnosis | clinical sign | ~50% overall; **~96%** in pulmonary series | present at diagnosis | Neoplasm metastasis — term uncertain **(verify)** |
| Bone metastasis | clinical sign | **71.4%** of metastatic pulmonary NC | — | Bone neoplasm / bone pain HP:0002653 **(verify)** |
| Liver metastasis | clinical sign | **23.8%** of metastatic pulmonary NC | — | Hepatic neoplasm **(verify)** |
| Elevated serum LDH | laboratory abnormality | prognostically relevant; **LDH >306 U/L** predicts OS <7.5 months (AUC 0.85) | at diagnosis | Elevated circulating LDH **(verify)**; LOINC 2532-0 (LDH, serum) **(verify)** |

Sources: [PMID:42865603](https://pmc.ncbi.nlm.nih.gov/articles/PMC13655413); [PMID:35372003](https://pmc.ncbi.nlm.nih.gov/articles/PMC8966081/); LDH threshold from Kloker et al. 2024 as reported in [Xie et al. 2025](https://www.hh.um.es/pdf/Vol_40/40_11/Xie-40-1839-1846-2025.pdf).

### 3.2 Thoracic NUT carcinoma (~50% of cases)

From a review of 44 patients with primary pulmonary NC ([PMID:42865603](https://pmc.ncbi.nlm.nih.gov/articles/PMC13655413)) and a second series ([Front Oncol 2021, doi:10.3389/fonc.2021.690115](https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2021.690115/full)):

| Phenotype | Frequency | Candidate HPO |
|---|---|---|
| Cough | **63.6%** (47.5% in a second series) | Cough HP:0012735 **(verify)** |
| Dyspnoea | **29.5%** | Dyspnea HP:0002094 **(verify)** |
| Chest/back pain | **18.2%** (37.5% in a second series) | Chest pain HP:0100749 **(verify)** |
| Haemoptysis | **18.2%** | Hemoptysis HP:0002105 **(verify)** |
| Pleural effusion | frequent, "moderate or large"; independently predicts shorter survival | Pleural effusion HP:0002202 **(verify)** |
| Wheezing | reported | Wheezing HP:0030828 **(verify)** |
| Superior vena cava obstruction | reported with mediastinal masses | **(verify — term uncertain)** |
| Acute respiratory failure | reported as presenting event | Respiratory failure HP:0002878 **(verify)** |

> "The common symptoms included cough, chest pain, hemoptysis, wheezing, dyspnea, fever, etc., among which cough is the most common." — [*Front Oncol* 2021](https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2021.690115/full)

**Tempo:** "median interval from symptom onset to diagnosis is 10 weeks" ([PMID:42865603](https://pmc.ncbi.nlm.nih.gov/articles/PMC13655413)). Mean maximal tumour diameter 6.55 cm (range 1.4–12.7 cm), lower lobe in 46.5%.

### 3.3 Head and neck NUT carcinoma (~40% of cases)

Sinonasal, nasopharyngeal, orbital, oral, laryngeal and major salivary (especially parotid) presentations:

| Phenotype | Candidate HPO |
|---|---|
| Nasal obstruction | Nasal obstruction HP:0001742 **(verify)** |
| Epistaxis | Epistaxis HP:0000421 **(verify)** |
| Proptosis / orbital mass / diplopia | Proptosis HP:0000520 **(verify)** |
| Facial pain, headache | Facial pain **(verify)**; Headache HP:0002315 **(verify)** |
| Cranial neuropathies (orbital/skull base extension) | **(verify)** |
| Neck mass (nodal or parotid) | Neck mass **(verify)** |
| Dysphagia, hoarseness (laryngeal/hypopharyngeal) | Dysphagia HP:0002015 **(verify)** |

### 3.4 Severity, progression and frequency

- **Severity:** uniformly severe. There is no mild form.
- **Progression:** **progressive** and rapid. Treatment-induced remissions are typically transient; in one multicentre series "a transient response to chemotherapy was observed in four of 11 patients" ([Lemelle et al., *Pediatr Blood Cancer* 2017, PMID:28643357](https://pubmed.ncbi.nlm.nih.gov/28643357/)).
- **Frequency among affected individuals:** the phenotype table above gives per-site frequencies; no phenotype is pathognomonic, which is precisely why the disease is missed.

### 3.5 Quality-of-life impact

**No disease-specific QoL instrument exists and no EQ-5D/SF-36/PROMIS data have been published for NUT carcinoma.** This is a genuine gap, and is explicitly reflected in the current cemiplimab trial ([NCT07050186](https://clinicaltrials.gov/study/NCT07050186)), which lists questionnaires among its assessments. What can be stated from the clinical literature:

- Airway compromise, pleural effusion, and pain are the dominant symptom burdens in thoracic disease.
- Orbital and skull-base extension in head and neck disease causes visual and cranial-nerve morbidity.
- Radical surgery at head and neck sites — which is the single intervention most strongly associated with survival (HR 0.3) — carries substantial functional cost (speech, swallowing, facial form, vision).
- With a median survival measured in months and a median age in the twenties, the disability-adjusted burden per case is very high relative to the case count.

---

## 4. Genetic / Molecular Information

### 4.1 The defining lesion

**Lesion class:** somatic balanced reciprocal chromosomal **translocation** producing an in-frame **gene fusion**. Not a point mutation, not a copy-number change.

**Canonical fusion — `BRD4::NUTM1`:**
> "The chromosome 19 translocation breakpoint targets the BRD4 double bromodomain-containing gene, which functions in regulation of cell cycle progression. Herein we demonstrate that BRD4 is fused with nearly the entire transcript of the novel 15q13 gene, NUT (nuclear protein in testis), forming a 6.4-kb fusion oncogene, BRD4-NUT." — [French CA, Miyoshi I, Kubonishi I, Grier HE, Perez-Atayde AR, Fletcher JA. *Cancer Res.* 2003;63(2):304–7. PMID:12543779](https://pubmed.ncbi.nlm.nih.gov/12543779/)

The typical junction is **BRD4 exon 10 → NUTM1 exon 2**, yielding a chimera containing BRD4's two bromodomains, two NLSs, the ET domain and the serine-rich region, fused to essentially all of NUT including its C-terminal NLS (OMIM \*608749).

### 4.2 Fusion partners and frequencies

Reported frequencies vary with ascertainment method and cohort; the registry cohort is the best-characterised denominator.

| Partner | Locus | HGNC | Frequency (registry, n=127) | Frequency (other series) | Notes |
|---|---|---|---|---|---|
| **BRD4** | 19p13.12 | HGNC:13575 | **99 (78%)** | 65–88% | t(15;19)(q14;p13.1); worst prognosis of the three common partners |
| **BRD3** | 9q34.2 | HGNC:1104 | **19 (15%)** | ~6–30% | BET family, same mechanism |
| **NSD3** (*WHSC1L1*) | 8p11.23 | HGNC:12767 | **7 (6%)** | ~6% | Not a BET protein; binds BRD4 in *trans* |
| **Other** | — | — | **2 (1%)** | — | see below |

Source for registry column: [Chau et al., *JNCI* 2020, PMID:32328562](https://pmc.ncbi.nlm.nih.gov/articles/PMC7165803/).

**Rarer and emerging partners in NUT carcinoma:** *ZNF532* (HGNC:30940) and *ZNF592* (HGNC:28986) — both members of the "Z4" complex; *CIC*; *BCORL1*; *MXD1*, *MXD4*, *MXI1*; *MGA*; *YAP1*; *ATXN1*; *CHD4*; *BRD9*; and in 2025 the first reports of **`SPECC1::NUTM1`** (17p11.2) and an intergenic **`IGR(downstream ROR2)::NUTM1`** fusion in pulmonary NC ([Xie et al. 2025](https://www.hh.um.es/pdf/Vol_40/40_11/Xie-40-1839-1846-2025.pdf)). Cytogenetic bands for *ZNF532* and *ZNF592* were **not verified in this session** — look them up before binding.

> "Although additional *NUTM1* fusion partners have been identified in recent years, the clinical relevance and mechanistic contributions of these novel fusion events to NC pathogenesis remain incompletely characterized."

**Partners that belong to *other* diseases** (do not curate under MONDO:0005563): *ACIN1*, *BRD9*, *CUX1*, *ZNF618*, *IKZF1*, *RUNX1* in B-ALL; *CIC*, *MGA*, *MXD1/MXD4* in sarcoma; *BPTF* in T-ALL; *ZBTB7A* in AML ([PMID:37082775](https://pmc.ncbi.nlm.nih.gov/articles/PMC10432870/)).

### 4.3 Variant classification and provenance

- **Classification:** oncogenic driver fusion. Not an ACMG/AMP germline classification; the appropriate framework is AMP/ASCO/CAP somatic **Tier I** (biomarker of a distinct diagnostic entity with therapeutic and prognostic implications).
- **Origin:** **somatic**, invariably. Not germline. Not inherited. No parental mosaicism reported.
- **Allele frequency in population databases:** **not applicable** — gnomAD, 1000 Genomes and TOPMed do not catalogue somatic fusions, and the fusion is absent from normal tissue.
- **Functional consequence:** **gain of function / neomorphic**. The fusion is not a loss of *BRD4* or *NUTM1* function; it creates a novel chimeric chromatin regulator with an activity neither parent protein has alone. Record as `GAIN_OF_FUNCTION` (or more precisely neomorphic) with `variant_origin: SOMATIC`, `allele_type:` structural/fusion.

### 4.4 Co-occurring somatic alterations

> "Co-occurring mutations in epigenetic or cell cycle pathways were observed in 26% of cases." — [Kroening et al., *JCO Precis Oncol* 2024, PMID:39447095](https://ascopubs.org/doi/10.1200/PO.24.00334) (n=54, paired DNA/RNA)

The remaining ~74% carry essentially no second driver. Tumour mutational burden is low; microsatellite status is stable; PD-L1 is negative in the great majority (**0/57 tested positive** in one IHC series — [Farooq et al., *Arch Pathol Lab Med* 2024;148(8):898, PMID:38059551](https://meridian.allenpress.com/aplm/article/148/8/898/497494/Nuclear-Protein-in-Testis-NUT-Carcinoma-A)), though individual PD-L1-high cases are reported and are the basis for the checkpoint-inhibitor work in §12.

### 4.5 Modifier genes

None established. The nearest thing to a modifier is the **fusion partner itself**, which modifies both prognosis (§11) and BET-inhibitor response (§12).

### 4.6 Epigenetic information

Epigenetics is not a secondary feature of this disease — it **is** the disease mechanism. Covered in full in §6. Summary of the chromatin signature:

- **Hyperacetylation** (H3K27ac, H3K18ac) within megadomains.
- **Global hypoacetylation** of chromatin outside megadomains, caused by p300 sequestration.
- **Absent H3K4me3** over megadomain bodies, distinguishing them from conventional promoters/super-enhancers.
- A distinct 3D nuclear compartment ("subcompartment M") into which megadomains cluster.
- No recurrent DNA-methylation signature has been established as causal; NC has no entry in DiseaseMeth as a methylation-driven disorder.

### 4.7 Chromosomal abnormalities

- **t(15;19)(q14;p13.1)** — the diagnostic translocation (BRD4::NUTM1). Historically the defining cytogenetic finding.
- **t(9;15)(q34;q14)** — BRD3::NUTM1 **(cytoband pairing inferred from the two loci; verify)**.
- **NSD3::NUTM1** arises from 8p11/15q14 rearrangement.
- **Karyotype is otherwise simple**, often with the translocation as the sole abnormality. There is no aneuploidy signature, no chromothripsis, and no recurrent arm-level change.

---

## 5. Environmental Information

**Environmental factors:** none established (see §2.2). No entry in CTD links a chemical to NUT carcinoma causally. There is no occupational, radiation, or pollutant association.

**Lifestyle factors:** none established. The never-smoker predominance (66.7%) is an important *negative*: for a poorly differentiated squamous carcinoma of the lung, this inverts the expected exposure profile and is itself diagnostically suggestive — a poorly differentiated squamous lung tumour in a young never-smoker should prompt NUT testing.

**Infectious agents:** **none.** NC is HPV-negative and EBV-negative in all reported cases. This is diagnostically load-bearing in the sinonasal and nasopharyngeal differential, where HPV-related multiphenotypic sinonasal carcinoma and EBV-associated nasopharyngeal carcinoma are the principal mimics.

For knowledge-base purposes, an `environmental:` block for this disease should either be absent or carry an explicit "searched, nothing citable" record — the absence of an environmental cause is a reported finding, not an unexamined gap.

---

## 6. Mechanism / Pathophysiology

### 6.1 Ordered causal chain

**Step 1 — Somatic translocation.** A balanced reciprocal translocation, most often t(15;19)(q14;p13.1), **results in** an in-frame fusion of *BRD4* exon 10 to *NUTM1* exon 2, producing the **BRD4::NUT chimeric protein**. *[Demonstrated — PMID:12543779; causally sufficient in vivo, PMID:38724194.]*

**Step 2 — Chromatin tethering.** The retained **tandem bromodomains of BRD4** bind acetyl-lysine on histone tails, which **tethers** the NUT moiety to acetylated chromatin — physically relocating a normally testis-restricted protein onto somatic chromatin. *[Demonstrated.]*

**Step 3 — p300 recruitment and de-repression.** NUT's acidic transactivation domain (AD1) binds the **TAZ2 zinc-finger domain of EP300 (p300)**, which **relieves p300's autoinhibition** and **activates** its histone acetyltransferase activity.
> "an acidic patch of NUT… interacts with the TAZ2 zinc finger domain of p300"; this domain "stimulated the ability of p300 to in vitro acetylate purified H3 histones." — [Eagen & French, PMID:33452461](https://pmc.ncbi.nlm.nih.gov/articles/PMC7914217/) *[Demonstrated in vitro with recombinant proteins.]*

**Step 4 — Feed-forward acetylation loop.** Activated p300 **acetylates** surrounding histones, which **creates** new acetyl-lysine binding sites, which **recruits** further BRD4::NUT, which **recruits** further p300. The loop is self-sustaining and processive.
> "BRD4-NUT first bound to regular enhancers, and then spread contiguously… over time (7h) to form mature MDs" — [PMID:33452461](https://pmc.ncbi.nlm.nih.gov/articles/PMC7914217/) *[Demonstrated by time-resolved ChIP-seq.]*

**Step 5 — Megadomain formation.** Iterative spreading **produces** contiguous hyperacetylated "megadomains" of **100 kb to 2 Mb**, co-enriched for BRD4-NUT, wild-type BRD4, p300 and active histone marks.
> "BRD4-NUT co-occupies with p300 unprecedented 100kb-2 Mbp 'megadomains' of acetylated chromatin." — [Alekseyenko et al., *Genes Dev* 2015;29(14):1507–23, PMID:26220994](https://genesdev.cshlp.org/content/29/14/1507.full.html) *[Demonstrated.]*

**Step 6 — 3D reorganisation.** Megadomains **cluster** in nuclear space into a novel sixth nuclear subcompartment ("**subcompartment M**"), bringing the key target loci into physical proximity — a plausible auto-regulatory circuit. *[Demonstrated by Hi-C; the regulatory consequence is inferred.]* This is the structural correlate of the characteristic **speckled/punctate nuclear NUT staining** seen on IHC — i.e. the diagnostic stain is literally a picture of the mechanism.

**Branch 6a — Global acetylation deficit.** Sequestration of the limited cellular pool of p300 into megadomains **depletes** acetylation from the rest of the genome, **causing** global histone hypoacetylation and widespread transcriptional repression, including of differentiation programmes.
> "BRD4-NUT expression causes global histone hypoacetylation and transcriptional repression. The fusion protein sequesters histone acetyltransferase (p300) activity." — [Schwartz et al., *Cancer Res* 2011;71(7):2686–96, PMID:21447744](https://pmc.ncbi.nlm.nih.gov/articles/PMC3070805/) *[Demonstrated; this is the rationale for HDAC-inhibitor therapy.]*

**Branch 6b — Targeted oncogene activation.** Megadomains land on and **drive** a small, consistent set of stem-cell transcription factor loci.
> "Across five different cell line and tissues we have identified a very limited set of NC-specific, common MDs: those associated with the *MYC*, *TP63*, and *SOX2* loci." — [PMID:33452461](https://pmc.ncbi.nlm.nih.gov/articles/PMC7914217/)

**Step 7a — MYC axis.** Megadomain-driven *MYC* (sustained in part via the **PVT1** lncRNA) **blocks** squamous differentiation and **drives** proliferation through cyclin D1/D2. Knockdown of *MYC* or *PVT1* **causes** differentiation of NC cells. *[Demonstrated in vitro — necessary and sufficient for the differentiation block.]*

**Step 7b — TP63 axis.** Megadomain-driven **ΔNp63** sustains a squamous stem/progenitor programme and **antagonises** TP53, **conferring** apoptosis resistance. "knockdown of *TP63* potently induces death of NC cells." *[Demonstrated in vitro; the TP53-antagonism step is partly inferred.]*

**Step 7c — SOX2 axis — CONTESTED.** *SOX2* is a consistent megadomain target and its knockdown causes differentiation **in vitro**. However, a 2025 genetic test *in vivo* **contradicts** a requirement:
> "SOX2 is dispensable for NC initiation and progression" — conditional *Sox2* deletion in the NCT mouse across SOX2-expressing (oral) and SOX2-absent (pancreas) lineages left tumour histology and the BRD4::NUTM1/MYC/TP63 programme intact. — [*Life Sci Alliance* 2025;9(2):e202503447, PMID:41266112](https://pmc.ncbi.nlm.nih.gov/articles/PMC12634820/)
**Curation note:** this is a genuine in-vitro/in-vivo discordance and should be recorded as a `HUMAN_MODEL_MISMATCH`-style open question, not resolved in favour of either side.

**Step 8 — Arrested squamous progenitor.** The combination — proliferation driven, differentiation blocked, apoptosis resisted — **yields** a squamous-lineage progenitor locked in an undifferentiated/basal state. The histological signature of a *partial, leaky* block is the characteristic **abrupt keratinisation**: islands of fully keratinised cells appearing without intermediate maturation, directly adjacent to primitive cells.

**Step 9 — Invasion and dissemination.** Unchecked growth **leads to** rapid local invasion and early lymphatic and haematogenous spread — nodal involvement in **91.9%** and distant metastasis in up to **96%** of pulmonary cases at diagnosis, to bone (71.4%) and liver (23.8%) — **causing** airway obstruction, pleural effusion, pain, and organ failure, and **resulting in** death at a median of ~6.5 months.

**Therapeutic branch 10 — BET inhibition.** A BET inhibitor **competitively occupies** BRD4's bromodomains, which **evicts** BRD4::NUT from chromatin, which **collapses** megadomains, which **de-represses** differentiation and **arrests** growth. *[Demonstrated in vitro and in patients — §12.]*

**Therapeutic branch 11 — HDAC inhibition.** An HDAC inhibitor **restores** acetylation outside megadomains and **depletes** BRD4-NUT and H3K27ac from megadomains, **inducing** squamous differentiation. *[Demonstrated in vitro, in xenograft, and in one patient — PMID:21447744.]*

### 6.2 Molecular pathways

| Pathway / process | Role | Candidate GO term |
|---|---|---|
| Histone acetylation / HAT activity (EP300) | **central driver** | histone acetyltransferase activity GO:0004402 **(verify)**; histone H3-K27 acetylation GO:0043974 **(verify)** |
| Acetyl-lysine recognition (bromodomain) | tethering step | lysine-acetylated histone binding GO:0070577 **(verify)** |
| Chromatin remodelling / organisation | megadomain formation | chromatin organization GO:0006325 **(verify)** |
| RNA Pol II transcriptional elongation (P-TEFb/CDK9, cyclin T1) | downstream output; co-precipitates with the BRD4-NUT complex via BRD4-long | positive regulation of transcription elongation from RNA Pol II promoter **(verify)** |
| MYC transcriptional programme | proliferation + differentiation block | MYC pathway activity elevated vs. comparators (PMID:39447095) |
| Cell cycle (cyclin D1/D2, CDK4/6–Rb) | proliferation; therapeutic node | cell cycle G1/S phase transition GO:0044843 **(verify)** |
| TP53 signalling (antagonised by ΔNp63) | apoptosis resistance | negative regulation of apoptotic process GO:0043066 **(verify)** |
| Keratinocyte / squamous differentiation | **blocked** | keratinocyte differentiation GO:0030216 **(verify)**; negative regulation of cell differentiation GO:0045596 **(verify)** |
| Spermatogenesis (NUT's normal context) | the ectopic programme | spermatogenesis GO:0007283 **(verify)** |

KEGG/Reactome have no NUT-carcinoma-specific pathway; the relevant Reactome entries are the generic HATs-acetylate-histones and MYC-target modules.

### 6.3 Normal function of NUT (the programme being misplaced)

NUT expression is physiologically restricted to post-meiotic **spermatids** (and reportedly ciliary body and ovarian germ cells). There it partners with **BRDT**, the testis-specific BET protein, and **EP300**, driving the hyperacetylation that precedes histone-to-protamine exchange during spermiogenesis. The *BRD4::NUTM1* fusion therefore executes a **germ-cell chromatin programme in a somatic epithelial cell** — the cleanest available description of what this oncoprotein actually does. *[NUTM1 structure: 7 exons, ~12 kb, 1127 aa, ~120 kDa, two acidic TADs, bipartite NLS, NES; intrinsically disordered.]*

### 6.4 Cellular processes

Cell-cycle dysregulation (cyclin D1/D2 up); apoptosis evasion (TP53 repression); **arrested differentiation** (the defining cellular phenotype); maintenance of a stem-like/basal state. Notably **not** prominent: oxidative stress, fibrosis, autophagy dysregulation, or immune-mediated tissue damage.

### 6.5 Protein dysfunction

Neither BRD4 nor NUT is misfolded or lost. The pathology is **mislocalisation of a functional module**: a chromatin-reading domain welded to a HAT-activating domain, creating a protein that both reads and writes the same mark — a self-amplifying circuit no wild-type protein possesses. The intrinsically disordered NUT moiety is also a plausible driver of biomolecular condensate formation at megadomains *[mechanistically plausible; the condensate contribution is an active question rather than settled]*.

### 6.6 Metabolic changes

Not a primary feature. GSEA in the NCT mouse model showed enrichment of "proliferation, mitosis, MYC targets, and **metabolic reprogramming** pathways" ([PMID:38724194](https://www.life-science-alliance.org/content/7/7/e202402602)), and conditional *Sox2* loss produced "only modest transcriptional changes affecting metabolic pathways" ([PMID:41266112](https://pmc.ncbi.nlm.nih.gov/articles/PMC12634820/)). A single case report describes metabolic and epigenetic reprogramming in retroperitoneal NC. No enzyme deficiency, no HMDB metabolite signature.

### 6.7 Immune system involvement

NUT carcinoma is **immunologically cold**:
> "significantly lower immune cell infiltration compared with HNSCC and LUSC" — [Kroening 2024, PMID:39447095](https://ascopubs.org/doi/10.1200/PO.24.00334)

PD-L1 was negative in **all** of 57 tested cases in one IHC series ([PMID:38059551](https://meridian.allenpress.com/aplm/article/148/8/898/497494/Nuclear-Protein-in-Testis-NUT-Carcinoma-A)); low TMB and MSS status compound this. The theoretical counter-argument is that the fusion junction is a true tumour-specific neoantigen, which is the rationale for the vaccine strategies discussed in §12. A striking cautionary case of **hyperprogression** after pembrolizumab in sinonasal NC has been reported ([*Laryngoscope* 2025](https://onlinelibrary.wiley.com/doi/10.1002/lary.70733)).

One consistent histological immune feature: **neutrophilic infiltration** within the tumour, reported across series.

### 6.8 Tissue damage mechanisms

Direct replacement and compression by tumour, plus **extensive confluent necrosis** (a near-constant histological finding, reflecting outgrowth of blood supply). Not oxidative, ischaemic, autoimmune or fibrotic in origin.

### 6.9 Molecular profiling summary

| Layer | Finding | Source |
|---|---|---|
| **Genomics** | Low TMB; MSS; few/no CNVs; simple karyotype; co-mutations (epigenetic/cell-cycle) in 26% | PMID:39447095; PMID:33452461 |
| **Transcriptomics** | Squamous programme; elevated MYC pathway; TP63/SOX2 high; mouse model: 3,065 up / 2,654 down genes, CIBERSORT enrichment for proliferating basal cells | PMID:39447095; PMID:38724194 |
| **Epigenomics** | ChIP-seq megadomains (H3K27ac, H3K18ac, BRD4, p300); H3K4me3-negative bodies; global extra-megadomain hypoacetylation; Hi-C subcompartment M | PMID:26220994; PMID:33452461 |
| **Proteomics** | BRD4-NUT complex pull-downs contain wild-type BRD4, p300, P-TEFb (CDK9/cyclin T1) | PMID:33452461 |
| **Metabolomics / lipidomics** | No published signature | — |
| **Single-cell / spatial** | Essentially unstudied in NC; a clear gap | — |
| **Functional genomics** | CDK9 identified as a synthetic-lethal dependency in NC cell lines; CDK4/6 and p300 identified as synergistic nodes with BET inhibition | PMID:35417004 |

---

## 7. Anatomical Structures Affected

### 7.1 Organ level

**Primary sites (registry, n=140 — [PMID:32328562](https://pmc.ncbi.nlm.nih.gov/articles/PMC7165803/)):**

| Site group | n | % | Candidate UBERON |
|---|---|---|---|
| **Thoracic** (lung, mediastinum, thymus, pleura) | 71 | **51%** | lung UBERON:0002048 **(verify)**; mediastinum **(verify)**; thymus UBERON:0002370 **(verify)** |
| **Head and neck** (sinonasal, nasopharynx, orbit, oral cavity, larynx, salivary) | 58 | **41%** | nasal cavity UBERON:0001707 **(verify)**; paranasal sinus **(verify)**; parotid gland UBERON:0001831 **(verify)** |
| **Bone / soft tissue** | 9 | 6% | bone element UBERON:0001474 **(verify)** |
| **Other** | 2 | 1% | — |

A second large tabulation gives lung n=87, mediastinum n=44, nose n=31, sinus n=19, parotid n=9 ([PMID:35957893](https://pmc.ncbi.nlm.nih.gov/articles/PMC9360329/)).

**SEER site distribution (n=45):** lung/bronchus **51.1%**, nasal cavity/paranasal sinuses **28.9%** ([PMID:40486575](https://pubmed.ncbi.nlm.nih.gov/40486575/)).

**Documented non-midline primaries:** kidney, pancreas, bladder, adrenal gland, stomach, brain, ocular globe, soft tissue, bone, retroperitoneum, and **primary cutaneous/adnexal** NC ([*J Cutan Pathol* 2024](https://onlinelibrary.wiley.com/doi/full/10.1111/cup.14602)). These are why "midline" was dropped from the name.

**Secondary organ involvement (metastatic):** regional lymph nodes (91.9% in pulmonary NC), **bone (71.4%)**, **liver (23.8%)**, lung, pleura, brain.

**Body systems:** respiratory (primary), head and neck/upper aerodigestive (primary), lymphatic (near-universal), skeletal (metastatic), hepatobiliary (metastatic).

### 7.2 Tissue and cell level

**Tissue type:** epithelial — specifically **squamous** or squamous-committed epithelium. The 2025 *Nat Rev Clin Oncol* review argues on transcriptional, histopathological, cell-of-origin and molecular grounds that NC *is* a squamous cell carcinoma ([PMID:39900969](https://www.nature.com/articles/s41571-025-00986-3)).

**Cell of origin — formally undetermined, but converging evidence points to a squamous/basal epithelial progenitor:**
- "Cell-of-origin remains undefined" ([PMID:33452461](https://pmc.ncbi.nlm.nih.gov/articles/PMC7914217/)).
- The NCT mouse generates NC-like squamous carcinomas from **KRT14-Cre** (basal keratinocyte) lineages, and the tumours are KRT14⁺, P63⁺, MYC⁺ ([PMID:38724194](https://www.life-science-alliance.org/content/7/7/e202402602)).
- CIBERSORT on those tumours shows "strong enrichment of **proliferating basal cell** profiles compared to normal oral mucosa."
- But the same model produces tumours from **Pdx1-Cre** (pancreas) and **Prrx1-Cre** (mesenchyme), so the permissive cell state is broader than classical squamous epithelium.
- Megadomain *placement* is itself cell-state dependent: in a human stem-cell model, "megadomains formed in dissimilar patterns when comparing cells in the pluripotent state with the same cell line following induction along a mesodermal lineage" ([*Genetics* 2023, PMID:37131839](https://academic.oup.com/genetics/article/224/3/iyad083/7147209)) — i.e. the pre-existing chromatin landscape determines where the oncoprotein lands.

**Candidate CL terms:** basal cell of epithelium CL:0000646 **(verify)**; squamous epithelial cell CL:0000076 **(verify)**; keratinocyte CL:0000312 **(verify)**; basal cell of epithelium of trachea/bronchus **(verify)**.

### 7.3 Subcellular level

Overwhelmingly **nuclear**. Candidate GO Cellular Component terms: nucleus GO:0005634 **(verify)**; chromatin GO:0000785 **(verify)**; nuclear speck GO:0016607 **(verify)**; euchromatin GO:0000791 **(verify)**. The diagnostically distinctive **speckled/punctate nuclear foci** of NUT IHC correspond to megadomain clusters (subcompartment M) — the subcellular finding and the molecular mechanism are the same object seen at two scales.

### 7.4 Localisation and laterality

Historically midline (hence the old name), but the modern entity is explicitly **not** midline-restricted. Thoracic disease is commonly **unilateral** at presentation with a lower-lobe predilection (46.5%), though "both lungs affected" is reported; head and neck disease is typically **unilateral** at origin with midline crossing on extension. No systematic left/right asymmetry has been reported.

---

## 8. Temporal Development

### 8.1 Onset

- **Age of onset:** any age — the literature spans **18 days to 82 years**. The registry median is **23.6 years** (n=141, [PMID:32328562](https://pmc.ncbi.nlm.nih.gov/articles/PMC7165803/)); other series give a median of **30 years** ([PMID:35957893](https://pmc.ncbi.nlm.nih.gov/articles/PMC9360329/)) and, for pulmonary NC specifically, a **mean 41.4 / median 36 years** ([PMID:42865603](https://pmc.ncbi.nlm.nih.gov/articles/PMC13655413)). The spread is real: head and neck disease skews younger, thoracic disease older.
- **Pattern:** **acute to subacute**. Median symptom-to-diagnosis interval in pulmonary NC is **10 weeks**. There is no prodrome, no premalignant lesion, and no recognised precursor state.
- **Not congenital, not developmental.** A neonatal case exists but the lesion is still acquired.

### 8.2 Progression

- **Stages:** staged by site-specific AJCC systems (TNM for lung, for sinonasal, etc.). There is **no NUT-carcinoma-specific staging system**, and this is a recognised limitation — most patients are stage IV or equivalent at diagnosis.
- **Rate:** rapid and relentless. 2-year OS **22%** (95% CI 15–30%) across the registry cohort.
- **Course:** **progressive**. Not episodic, not relapsing-remitting.
- **Duration:** measured in months. Median OS **6.5 months**.

### 8.3 Remission and long-term survival

Remission is **treatment-induced, usually partial, and usually transient**. Initial complete or partial response to first-line therapy occurred in **55/112 (49%)** of registry patients — yet 2-year OS was 22%, so response does not translate into durable control in most cases. Spontaneous remission is not described.

**Long-term survivors do exist, and their distribution is informative** (≥3-year survival, registry):
- **Group A** (non-thoracic, BRD3-/NSD3-NUT): **5/12 (42%)**
- **Group B** (non-thoracic, BRD4-NUT): **7/45 (16%)**
- **Group C** (thoracic, any fusion): **0/67 (0%)**

One French patient remained in remission **>12 years** after diagnosis ([PMID:28643357](https://pubmed.ncbi.nlm.nih.gov/28643357/)). Cure, where it happens, follows complete resection of localised non-thoracic disease.

### 8.4 Critical periods

The **only clearly defined window of opportunity is at initial presentation**, before dissemination, when complete surgical resection with negative margins plus radiotherapy is possible. Surgery is the strongest favourable variable in the registry analysis (HR **0.3**, 95% CI 0.2–0.5, P<.0001), and the difference between thoracic and non-thoracic outcomes is partly a difference in resectability (surgery received by **73% of non-thoracic vs 30% of thoracic** patients). Everything downstream of that window is palliative in the great majority of cases.

A second, system-level critical period is **diagnostic**: initial misdiagnosis occurred in **31%** of German cases and **50%** of French cases, and approximately **70% of NCs are estimated to be misdiagnosed** overall. Time lost to a wrong diagnosis is time lost from the only curative window.

---

## 9. Inheritance and Population

### 9.1 Epidemiology

| Measure | Value | Source |
|---|---|---|
| **Estimated true US incidence** | **~1,400 cases/year** (≈0.4/100,000/year) | [PMID:39900969](https://www.nature.com/articles/s41571-025-00986-3) |
| Registry-captured incidence | ~20 new cases/year | [PMID:35417004](https://pmc.ncbi.nlm.nih.gov/articles/PMC9197941/) |
| Total cases in literature | ~300–310 (as of ~2022) | [PMID:35957893](https://pmc.ncbi.nlm.nih.gov/articles/PMC9360329/) |
| Paediatric incidence (Western Australia, 0–16 y) | 0.41 per million child-years | [PMID:35957893](https://pmc.ncbi.nlm.nih.gov/articles/PMC9360329/) |
| Share of primary thoracic tumours | ~0.22% | [PMID:42865603](https://pmc.ncbi.nlm.nih.gov/articles/PMC13655413) |
| SEER cases 2018–2023 | 91 | [PMID:42870800](https://pubmed.ncbi.nlm.nih.gov/42870800/) |
| Estimated misdiagnosis rate | ~70% | [Xie et al. 2025](https://www.hh.um.es/pdf/Vol_40/40_11/Xie-40-1839-1846-2025.pdf) |

**Orphanet prevalence class:** the registry-based figures place NC well below 1/1,000,000 as *diagnosed*, but the French-et-al. estimate of 1,400 US cases/year implies a **true** annual incidence around 0.4/100,000 — a two-order-of-magnitude discrepancy that is the central epidemiological fact about this disease. Any prevalence record for this entry should carry both numbers with their different bases: one is *ascertained*, the other *estimated true*.

> "with approximately 1,400 annual cases in the United States and a median survival of roughly 6.5 months, this disease surpasses the incidence of certain established NSCLC and HNSCC subtypes yet remains misclassified as a distinct orphan entity." — [PMID:39900969](https://www.nature.com/articles/s41571-025-00986-3)

The underdiagnosis has a measurable cause. A nationwide survey of **2,215 Chinese clinicians** found **65.2% reported no awareness of any domain** of NUT carcinoma; awareness of *NUTM1* fusion partners was **9.7%**; only ~7% reported awareness across all domains — and 81.2% of respondents worked in tertiary hospitals ([*BMC Health Serv Res* 2026, PMID:41772604](https://pubmed.ncbi.nlm.nih.gov/41772604/)).

### 9.2 Inheritance

- **Inheritance pattern:** **none — not heritable.** The *NUTM1* fusion is a somatic event. There is no autosomal dominant, recessive, X-linked, mitochondrial, or multifactorial inheritance.
- **Penetrance / expressivity / anticipation / germline mosaicism / founder effects / consanguinity / carrier frequency:** **not applicable.**
- **Genetic counselling:** limited to explaining that the tumour is sporadic and poses no risk to relatives — which is itself a useful counselling message for families of young patients.

### 9.3 Population demographics

- **Ethnic/ancestral groups:** no established difference. Apparent geographic concentration tracks diagnostic practice.
- **Geographic distribution:** worldwide. Registry data skew to the US (49% of 310 identified cases); Germany was represented by only 8 cases in one tabulation, which the authors read as underdiagnosis rather than true rarity.
- **Variant geography:** no reported geographic variation in fusion-partner distribution.
- **Sex ratio:** approximately **1:1** (registry 48% M / 52% F); some series report modest male excess (up to 1.89:1 in pulmonary cases). Treat as no established sex effect.
- **Age distribution:** bimodal-leaning-young; peak in adolescents and young adults, with a long tail into old age. Molecular-profiling data: NC **~10× more prevalent in <50 than >70** ([PMID:39447095](https://ascopubs.org/doi/10.1200/PO.24.00334)). Paediatric and adult outcomes do not differ significantly ([PMID:35417004](https://pmc.ncbi.nlm.nih.gov/articles/PMC9197941/)).

---

## 10. Diagnostics

### 10.1 The single most important point

**NUT carcinoma is a diagnosis you have to think of.** It has no pathognomonic clinical or radiological feature, and its default misread is "poorly differentiated squamous cell carcinoma" or "undifferentiated carcinoma, NOS." The consensus recommendation is explicit:

> "NUT immunohistochemistry is adequate for diagnosis and should be considered in any patient with a poorly differentiated carcinoma." — [PMID:35417004](https://pmc.ncbi.nlm.nih.gov/articles/PMC9197941/)

and

> "NGS should detect *NUTM1* rearrangement in all thoracic tumors." — same source.

### 10.2 Histopathology

**Gross/architectural:** infiltrative mass, often large (mean 6.55 cm in lung), with extensive confluent necrosis.

**Microscopic:**
- Sheets and nests of **monomorphic, small-to-medium, primitive round-to-polygonal cells**, scant-to-moderate eosinophilic or amphophilic cytoplasm, vesicular chromatin with prominent nucleoli (a "fried-egg" appearance is described).
- **Abrupt keratinisation** — islands of mature keratinised cells arising without intermediate maturation, immediately adjacent to primitive cells. Present in roughly **30–40%** of cases; **"abrupt keratinization is the most characteristic histological finding."**
- ~**55% show no squamous differentiation at all** — which is the main reason the diagnosis is missed.
- High mitotic rate; median **Ki-67 60%**.
- **Neutrophilic infiltrate** is characteristic.

**Cytology:** diagnosable on EBUS-FNA and other small samples; monomorphic primitive cells with occasional keratinised forms. Small-biopsy diagnosis is realistic, which matters since many of these tumours are unresectable.

### 10.3 Immunohistochemistry

**The diagnostic test: anti-NUT monoclonal antibody, clone C52B1 (Cell Signaling Technology).**

> Nuclear staining in ">50% of nuclei" is **"100% specific and shows a sensitivity of 87% for a diagnosis of NC"** among carcinomas. — [PMID:35957893](https://pmc.ncbi.nlm.nih.gov/articles/PMC9360329/); concordant in [PMID:35417004](https://pmc.ncbi.nlm.nih.gov/articles/PMC9197941/)

The pattern is **diffuse, speckled/punctate nuclear** labelling (described also as "granular" or "dusty"). The speckles *are* the megadomain subcompartment.

**Comprehensive IHC profile — 57 cases ([Farooq AL, Kerper AL, Boland JM, Lo YC. *Arch Pathol Lab Med.* 2024;148(8):898. PMID:38059551](https://meridian.allenpress.com/aplm/article/148/8/898/497494/Nuclear-Protein-in-Testis-NUT-Carcinoma-A)) — sites: thoracic/mediastinal 38, head-and-neck/sinonasal 13, other 6:**

| Marker | Result | Interpretation |
|---|---|---|
| **Keratins** | variable; **completely negative in 15%** | a keratin-negative carcinoma does **not** exclude NC |
| **p63** | **positive in 87%** | more sensitive than p40 — use both |
| **p40** | **positive in only 65% (24/37)** | **key pitfall**: p40-negativity is common and will push a reader away from a squamous diagnosis |
| **INSM1** | **positive in 54%** | **major pitfall** — invites a wrong diagnosis of neuroendocrine carcinoma |
| **TTF-1** | predominantly negative (occasional positives, incl. 60% in one reported lung case) | |
| **CD34** | positive in **15%** | some series report up to ~50% |
| **CD99** | positive in **21%** | mimics Ewing sarcoma |
| **BRG1 (SMARCA4) / INI1 (SMARCB1)** | **retained in all cases** | distinguishes from SMARCA4-deficient undifferentiated thoracic tumour and SMARCB1-deficient sinonasal carcinoma |
| **Ki-67** | median **60%** | |
| **PD-L1** | **negative in all tested** | |
| Synaptophysin / chromogranin | may be focally positive | further neuroendocrine confusion |

**Practical rule:** a poorly differentiated carcinoma in a young patient, p63⁺ but p40⁻, INSM1⁺, SMARCA4/SMARCB1-retained, p16/HPV⁻, EBER⁻ — is a NUT IHC case until proven otherwise.

### 10.4 Differential diagnosis

| Mimic | How it is distinguished |
|---|---|
| Poorly differentiated / basaloid **squamous cell carcinoma** | NUT IHC negative; usually older, smoker |
| **Small cell / large cell neuroendocrine carcinoma** | chromogranin/synaptophysin strong and diffuse; NUT negative — but note NC is INSM1⁺ in 54% |
| **SMARCA4-deficient undifferentiated thoracic tumour** | BRG1 **lost**; NC retains it |
| **SMARCB1-deficient sinonasal carcinoma** | INI1 **lost**; NC retains it |
| **Sinonasal undifferentiated carcinoma (SNUC)** | keratin⁺, p40⁻/weak p63; IDH2 mutation in a subset; NUT negative |
| **HPV-related multiphenotypic sinonasal carcinoma** | p16⁺/HPV⁺; NC is HPV-negative |
| **Nasopharyngeal carcinoma** | EBER⁺; NC is EBV-negative |
| **Ewing sarcoma / round cell sarcoma** | CD99 diffuse membranous, *EWSR1* fusion; NC CD99⁺ in only 21% and keratin/p63⁺ |
| **Lymphoma, melanoma, germ cell tumour** | lineage markers |
| **Poorly differentiated adenocarcinoma** | TTF-1⁺/napsin⁺, p40⁻, NUT⁻ |
| **NUT-rearranged non-carcinomas** (B-ALL, CIC-NUTM1 sarcoma, poroma) | lineage, site, age, partner gene — *different diseases* |

### 10.5 Molecular and genetic testing

| Method | Utility |
|---|---|
| **NUT IHC (C52B1)** | **first-line**; 87% sensitive, ~100% specific; cheap, fast, works on small biopsies. One multi-omic comparison found **NUT IHC positive in 100% (99/99)** of confirmed cases vs **RNA-based fusion detection 83.9% (52/62)** |
| **FISH, *NUTM1* break-apart probe** | confirms rearrangement; **does not identify the partner**; false-negatives occur with cryptic/complex rearrangements |
| **RNA sequencing / targeted fusion panels** (e.g. Archer FusionPlex) | identifies the **partner**, which carries prognostic and predictive weight; registry data report fusions detected in **82.1% of RNA tests** |
| **RT-PCR** | confirms a known fusion; will miss novel partners |
| **DNA NGS / WES** | poor at detecting fusions with intronic breakpoints; useful for co-mutations, TMB, MSI |
| **Karyotyping** | historical; can show t(15;19) |
| **Chromosomal microarray (CMA)** | **low yield** — the translocation is balanced and invisible to CMA |
| **WGS** | can detect the structural variant but is not routine |
| **Mitochondrial DNA / repeat-expansion testing** | **not applicable** |
| **Liquid biopsy / ctDNA** | investigational; fusion-specific ctDNA assays are plausible but not established |

**Recommended workflow:** NUT IHC on any poorly differentiated carcinoma without an established lineage → if positive (or if clinical suspicion is high despite a negative stain), RNA-based fusion sequencing to identify the partner → report the partner, because it changes prognostic group and may change BET-inhibitor expectations.

### 10.6 Imaging and other tests

- **CT:** irregular soft-tissue mass; "uneven enhancement"; frequent moderate-to-large pleural effusion; lower-lobe predilection in lung.
- **FDG-PET/CT:** used for staging and response, **with an explicit caveat from the consensus panel**: *"FDG-PET scanning may not be a reliable measure of tumor response to BET inhibitor-based treatment"* ([PMID:35417004](https://pmc.ncbi.nlm.nih.gov/articles/PMC9197941/)) — because differentiation-inducing agents may alter glucose avidity without tumour shrinkage.
- **MRI:** for orbital/skull-base and intracranial extension.
- **Laboratory:** no diagnostic blood test. **Serum LDH** has prognostic value (>306 U/L → OS <7.5 months; AUC 0.85). Candidate LOINC: LDH serum/plasma LOINC:2532-0 **(verify)**.
- **Functional tests / electrophysiology:** not applicable.

### 10.7 Screening

**There is no screening programme and none is justified** — the disease is sporadic, somatic, has no precursor lesion, no at-risk population to enrol, and no asymptomatic detectable phase. Newborn screening, carrier screening, cascade testing and preimplantation diagnosis are all **not applicable**.

The actionable "screening" analogue is **diagnostic reflex testing**: routinely applying NUT IHC or *NUTM1*-inclusive NGS to poorly differentiated carcinomas, especially in patients under 50 and in never-smokers with squamous lung tumours.

---

## 11. Outcome / Prognosis

### 11.1 Survival

| Cohort | n | Median OS | Source |
|---|---|---|---|
| International registry (all) | 141 | **6.5 months** (95% CI 5.8–9.1) | [PMID:32328562](https://pmc.ncbi.nlm.nih.gov/articles/PMC7165803/) |
| Early registry cohort | 63 | **6.7 months**; 2-y PFS 9% | [Bauer et al., *Clin Cancer Res* 2012, PMID:22896655](https://pubmed.ncbi.nlm.nih.gov/22896655/) |
| Head and neck NMC | 40 | **9.7 months**; 2-y OS 30% | [Chau et al., *Cancer* 2016, PMID:27509377](https://pubmed.ncbi.nlm.nih.gov/27509377/) |
| Germany (adults) | 35 | **7.5 months** | [PMID:38301600](https://pubmed.ncbi.nlm.nih.gov/38301600/) |
| SEER (2025 analysis) | 45 | **8 months** (95% CI 4.09–11.91) | [PMID:40486575](https://pubmed.ncbi.nlm.nih.gov/40486575/) |
| SEER 2018–2023 | 91 | **8 months**; 67% died | [PMID:42870800](https://pubmed.ncbi.nlm.nih.gov/42870800/) |
| France, children + adults | 12 | **4.7 months** (95% CI 2.1–17.7) | [PMID:28643357](https://pubmed.ncbi.nlm.nih.gov/28643357/) |
| Korea | 13 | **10.6 months** (9 deaths, range 3–23.6 mo) | [Jung et al., *Oncologist* 2019, PMID:30696721](https://pubmed.ncbi.nlm.nih.gov/30696721/) |
| **Primary pulmonary NC** | pooled | **2.2–5.9 months** (mean 6.21; one series 2.2) | [*Front Oncol* 2021](https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2021.690115/full); [PMID:42865603](https://pmc.ncbi.nlm.nih.gov/articles/PMC13655413) |

**2-year OS: 22%** (95% CI 15–30%). **~70–80% of patients die within 2 years.** 10-year survival is not meaningfully reported.

### 11.2 The prognostic model (the single most useful prognostic tool)

[Chau NG et al., *J Natl Cancer Inst* 2020. PMID:32328562](https://pmc.ncbi.nlm.nih.gov/articles/PMC7165803/) — **anatomical site + fusion partner**, n=124:

| Group | Definition | Median OS | ≥3-year survivors |
|---|---|---|---|
| **A** | Non-thoracic **and** BRD3- or NSD3-NUT | **36.5 months** (95% CI 12.5–NR) | 5/12 (**42%**) |
| **B** | Non-thoracic **and** BRD4-NUT | **10 months** (95% CI 7–14.6) | 7/45 (16%) |
| **C** | **Thoracic** (any fusion) | **4.4 months** (95% CI 3.5–5.6) | **0/67 (0%)** |

**Univariate hazard ratios:**

| Factor | HR (95% CI) | P |
|---|---|---|
| Thoracic vs non-thoracic primary | **3.4 (2.2–5.1)** | <.0001 |
| BRD4-NUT vs BRD3-/NSD3-NUT | **1.8 (1.1–3.1)** | .024 |
| Lymph node / organ metastasis | **2.2 (1.2–4.1)** | .01 |
| **Surgery (ever received)** | **0.3 (0.2–0.5)** | <.0001 |

### 11.3 Other prognostic factors

- **Stage / distant metastasis / M1** — worse ([PMID:42870800](https://pubmed.ncbi.nlm.nih.gov/42870800/)).
- **Larger tumour size** — worse.
- **Older age at diagnosis** — lower cumulative survival in pulmonary NC.
- **Pleural effusion** — shorter survival.
- **Serum LDH >306 U/L** — OS <7.5 months (AUC 0.85).
- **Complete resection with negative margins** — the strongest favourable factor.
- **Receipt of radiotherapy and systemic therapy** — associated with better OS in SEER analyses, with the usual confounding by fitness and resectability.

### 11.4 Morbidity, disability and quality of life

No ICF-coded disability data, no DALY estimate in GBD (the disease has no GBD cause category), and **no published EQ-5D, SF-36 or PROMIS data**. Morbidity is driven by local tumour effects (airway obstruction, pain, visual loss, dysphagia), by the morbidity of radical head and neck surgery and chemoradiation in the minority who are treatable with curative intent, and by the toxicity of BET inhibitors (notably thrombocytopenia). Given the median age in the twenties, years of life lost per case is very high.

### 11.5 Complications

Airway obstruction and respiratory failure; massive pleural effusion; superior vena cava syndrome; pathological fracture and bone pain from skeletal metastases; hepatic failure; cranial neuropathy and visual loss from skull-base/orbital extension; treatment-related cytopenias and infection.

### 11.6 Recovery potential

Cure is possible but uncommon and essentially confined to **completely resected, localised, non-thoracic disease**, ideally with a non-BRD4 partner. The zero 3-year survivors in thoracic disease (0/67) is the hardest number in this report and should be reflected in any prognosis record.

---

## 12. Treatment

**There is no standard of care.** This should be stated explicitly rather than implied.

> "There is currently no standard-of-care therapy for NC, and patients face a grim prognosis." — [PMID:35957893](https://pmc.ncbi.nlm.nih.gov/articles/PMC9360329/)
> "The status quo is largely unsatisfactory and better drugs are needed to effectively treat NC." — consensus statement, [PMID:35417004](https://pmc.ncbi.nlm.nih.gov/articles/PMC9197941/)

### 12.1 Surgery and radiotherapy — the backbone

> "Aggressive control of localized disease with surgery and radiation is the most effective treatment" and represents "the only chance for long-term survival." — [PMID:35417004](https://pmc.ncbi.nlm.nih.gov/articles/PMC9197941/)

> "extent of surgical resection and initial radiotherapy were independent predictors of PFS and OS," while conventional chemotherapy showed no benefit. — [Bauer et al. 2012, PMID:22896655](https://pubmed.ncbi.nlm.nih.gov/22896655/)

- **Surgery** — HR 0.3; complete resection with negative margins is the single intervention most associated with long-term survival. Received by 73% of non-thoracic vs 30% of thoracic patients. NCIT: **Surgical Procedure NCIT:C15329**.
- **Radiotherapy** — received by 73% (85/117) of registry patients; definitive or post-operative. NCIT: **Radiation Therapy NCIT:C15313**.

### 12.2 Cytotoxic chemotherapy

Received by **90% (105/117)** of registry patients. Initial CR/PR in **49% (55/112)**, almost always transient.

Regimens used (none established as superior):
- **Ifosfamide-based**, particularly the **Scandinavian Sarcoma Group IX (SSG IX)** Ewing-sarcoma regimen — "has demonstrated anecdotal successes" with "four long term complete responses (CR) or cures reported" ([PMID:35417004](https://pmc.ncbi.nlm.nih.gov/articles/PMC9197941/)). This is the most interesting signal in conventional chemotherapy and is a paediatric-oncology-derived approach.
- Ifosfamide + etoposide.
- Platinum (cisplatin/carboplatin) + etoposide.
- Platinum + paclitaxel.
- Anthracycline-containing regimens in some series.

**Chemoradiotherapy** gave mean OS **13.2 months** in a pulmonary series (vs 5.58 for chemotherapy alone and 3.54 for surgery alone), with 4 patients surviving >12 months ([PMID:42865603](https://pmc.ncbi.nlm.nih.gov/articles/PMC13655413)) — noting heavy selection bias.

NCIT: **Chemotherapy NCIT:C15632**; **Pharmacotherapy NCIT:C15986**.
CHEBI candidates **(verify all)**: cisplatin CHEBI:27899; etoposide CHEBI:4911; ifosfamide CHEBI:5864; paclitaxel CHEBI:45863; doxorubicin CHEBI:28748; carboplatin CHEBI:31355.

### 12.3 BET bromodomain inhibitors — the mechanism-matched class

**Rationale:** "The bromodomain-acetyl-lysine interaction thus represents a therapeutic vulnerability in cancers that are dependent on BRD4, including NC." BET inhibitors "evict BRD4-NUT from chromatin by directly binding the dual bromodomains of BRD4," collapsing megadomains and inducing differentiation.

**Historical note:** BET inhibitors as a drug class were *discovered through* NUT carcinoma — "BET bromodomain inhibitors were initially discovered in NUT midline carcinoma (NMC)" ([Stathis et al., *Cancer Discov* 2016, PMID:26976114](https://pubmed.ncbi.nlm.nih.gov/26976114/)).

| Agent | Study | NC patients | Result |
|---|---|---|---|
| **Birabresib (OTX015/MK-8628)** | Stathis 2016, PMID:26976114 (4 pts); phase Ib (9 pts) | 4 / 9 | first proof of concept: 2/4 "responded rapidly with tumor regression and symptomatic relief," a third had meaningful stabilisation. In the larger set: 3 PR, 3 SD, 2 PD; duration 1.4–8.4 months. Reversible grade 3 thrombocytopenia |
| **Molibresib (GSK525762 / i-BET762)** | [Piha-Paul et al., *JNCI Cancer Spectr*, PMID:32328561](https://pubmed.ncbi.nlm.nih.gov/32328561/) | **19** | **4 PR, 8 SD; ORR 11%**; 4 progression-free >6 months. Thrombocytopenia 51%, GI 22–42%, anaemia 22%, fatigue 20%. RP2D 80 mg QD. "Preliminary data indicate proof-of-concept in NC" |
| **RO6870810** | [Shapiro et al., *Br J Cancer* 2021, PMID:33311588](https://pubmed.ncbi.nlm.nih.gov/33311588/) | 8 | **ORR 25% (2/8)**; 4 SD, 1 PD; median PFS 94 days. **Both responders had non-BRD4 fusions (NSD3-NUT, BRD3-NUT)**; one NSD3-NUT response lasted **797 days** |
| **ODM-207** | phase I | 4 | minimal activity: 3 PD, 1 SD |
| **BMS-986158** | NCT03936465 | — | "most robust clinical benefit in NC patient with non-BRD4-NUT (BRD3-NUT) fusion," PFS 279 days |
| **ZEN-3694 (ZEN003694)** | FDA **orphan drug designation** for NUT carcinoma; two active trials | — | NCT05019716 (+ cisplatin/etoposide or carboplatin/paclitaxel), NCT05372640 (+ abemaciclib) |
| **NHWD-870 HCl** | **Phase II, China, 2026** | **40** | **ORR 30% (12/40) by IRC; thoracic subgroup ORR 45% (9/20); DCR 47.5%; mPFS 2.76 mo; mOS 9.33 mo.** Dose 2 mg PO, 5-days-on/2-days-off, 28-day cycles. AEs: thrombocytopenia 55%, hypertriglyceridaemia 55%, hyperbilirubinaemia 47.5%, anaemia 47.5%; **no treatment-related deaths**. **China NMPA breakthrough therapy designation, 9 May 2026** |

**⚠️ Evidence-quality flag on NHWD-870:** these figures come from a **2026 ESMO presentation and company press release** ([clinicaltrialvanguard](https://www.clinicaltrialvanguard.com/news/nhwd-870-hcl-hits-45-response-rate-in-thoracic-nut-carcinoma/); [PR Newswire](https://en.prnasia.com/releases/global/zhejiang-wenda-pharma-announces-positive-results-from-phase-ii-trial-of-oral-bet-inhibitor-nhwd-870-hcl-at-the-2026-esmo-annual-meeting-553108.shtml)), **not from a peer-reviewed publication**, and the trial registration number was not located. They should be curated as conference-abstract-level evidence, if at all, and the claim re-checked against a journal publication before being treated as established. If confirmed, a 45% ORR in *thoracic* disease — the group with 0/67 three-year survivors — would be the most meaningful therapeutic advance in this disease to date.

**Consensus verdict on BET monotherapy:**
> BET-inhibitor monotherapy has produced "modest benefit in a minority of patients"; most responses occurred in patients with **non-BRD4-NUT** translocations. — [PMID:35417004](https://pmc.ncbi.nlm.nih.gov/articles/PMC9197941/)

**Next-generation agents:** ABBV-744 (BD2-selective; 325× BD2/BD1 selectivity, 12.5× less thrombopoietic toxicity); mivebresib/ABBV-075 (pan-BET); BI 894999 (BD1-selective; IC₅₀ 1–2 nM across four NC models, evicts BRD4-NUT at 30 nM vs 1 µM for molibresib); NEO2734 (dual p300/CBP + BET).

**PROTAC BET degraders** are the stated next direction: "Future research directions include exploring new therapeutic strategies (such as highly selective BET inhibitors, BET-inhibitor combinations, and **PROTAC technologies**)" ([PMID:41737331](https://pubmed.ncbi.nlm.nih.gov/41737331/)). RNK05047, a dual BRD4/HSP90 PROTAC degrader, is in phase I/II for advanced solid tumours and lymphomas.

NCIT: **Targeted Therapy NCIT:C93352 (verify)**; **Pharmacotherapy NCIT:C15986**.

### 12.4 HDAC inhibitors

**Rationale** (and it is a different rationale from BET inhibition): megadomains sequester the limited p300 pool, leaving the rest of the genome hypoacetylated; HDAC inhibition restores that acetylation and depletes BRD4-NUT from megadomains, inducing differentiation.

- Nine structurally distinct HDAC inhibitors showed dose-dependent growth inhibition correlating with histone acetylation (**R² = 0.96**) across four NMC lines ([Schwartz et al., *Cancer Res* 2011, PMID:21447744](https://pmc.ncbi.nlm.nih.gov/articles/PMC3070805/)).
- **LBH-589 (panobinostat)** produced significant growth suppression and survival benefit in PER-403 xenografts (P=0.001) with morphological squamous differentiation.
- **Clinical:** a 10-year-old with mediastinal NMC achieved an objective response to **vorinostat** monotherapy at 5 weeks (reduced PET avidity) before dose-limiting thrombocytopenia stopped treatment.
- **Verdict:** "Since positive studies are still missing, HDACi treatment currently cannot be recommended as a standard of care."

CHEBI: vorinostat CHEBI:45716 **(verify)**; panobinostat **(verify)**.

### 12.5 Other targeted and combination strategies

| Strategy | Evidence |
|---|---|
| **p300/CBP HAT or bromodomain inhibition** | A-485 (HAT) and GNE-781 (bromodomain) inhibit NC growth; **synergistic with BET inhibitors**. NEO2734 (dual) "potently inhibited growth and induced differentiation of NC cells *in vitro*" and gave "greater growth inhibition, tumor regression, and significant survival benefit" vs chemotherapy in xenografts |
| **CDK4/6 inhibition + BET inhibition** | Palbociclib + JQ1 synergistic *in vitro*; **only the combination produced tumour regression** in xenografts, with survival benefit — but "rapid tumor re-growth occurred" on stopping, indicating reversible quiescence rather than cell kill. Clinical translation: **NCT05372640** (ZEN-3694 + abemaciclib) |
| **CDK9 inhibition** | CDK9 identified as a **synthetic-lethal** target in NC lines; inhibition induced apoptosis and reduced Pol II occupancy at *MYC*. Agents: KB-0742 (NCT04718675), TP1287 (NCT03604783) |
| **Dual HDAC/PI3K inhibition** | CUDC-907 IC₅₀ **5.5–9.0 pmol/L** in NC lines; panobinostat 0.4–1.3 nmol/L; AZD5153 (BET) 3.7–8.2 nmol/L. "CUDC-907 might be promising in NUT carcinoma treatment" ([PMID:30696721](https://pubmed.ncbi.nlm.nih.gov/30696721/)) |
| **BET + DNA-damaging agents / PARP inhibitors** | BET inhibition reduces *BRCA1*/*RAD51* transcription, compromising homologous recombination — rationale for ZEN-3694 + talazoparib (NCT03901469 in TNBC; NCT05327010 ComBET) |
| **EZH2 inhibition** | EZH2 reported to synergise with BRD4-NUT; preclinical |
| **miR-766-5p targeting BRD4** | preclinical |

### 12.6 Immunotherapy

A genuinely unsettled area, with evidence pointing both ways.

**For:**
- "Two studies have reported durable disease stability in PD-L1-high NCs treated with nivolumab or pembrolizumab," supporting a "consensus recommendation to consider the addition of immune checkpoint blockade to the treatment paradigm of non-surgically treated NC patients with PD-L1+ disease" ([PMID:35417004](https://pmc.ncbi.nlm.nih.gov/articles/PMC9197941/)).
- In the German cohort, "Patients treated with an immune checkpoint inhibitor (ICI) in addition to first-line chemotherapy **tended to have longer OS**" ([PMID:38301600](https://pubmed.ncbi.nlm.nih.gov/38301600/)).
- The NUT fusion junction is a true tumour-specific neoantigen — a rational target for personalised vaccination.
- Active trial: **NCT07050186**, phase II cemiplimab in incurable metastatic/unresectable NUT carcinoma.

**Against:**
- NC is immunologically cold, with significantly lower immune infiltration than HNSCC and LUSC, low TMB, MSS status, and PD-L1 negative in 0/57 tested cases.
- **Hyperprogression** after pembrolizumab-based treatment has been reported in sinonasal NC ([*Laryngoscope* 2025](https://onlinelibrary.wiley.com/doi/10.1002/lary.70733)).

**Net:** reasonable to consider in PD-L1-positive, non-surgical disease; not an established benefit; a real risk signal exists.

### 12.7 Supportive and rehabilitative care

Airway management (stenting, tracheostomy), pleural drainage/pleurodesis, analgesia including opioids, palliative radiotherapy to painful bone metastases, nutritional support, speech/swallow and physical rehabilitation after head and neck surgery, and early palliative care integration. NCIT: **Supportive Care NCIT:C15747**; **Rehabilitation NCIT:C15315**; **Physical Therapy NCIT:C15302**; **Nutritional Support NCIT:C15433 (verify)**.

### 12.8 Active clinical trials (as of November 2026)

| NCT | Title / agent | Phase | Status |
|---|---|---|---|
| [NCT05019716](https://clinicaltrials.gov/study/NCT05019716) | **ZEN003694 + chemotherapy** (cisplatin/etoposide; carboplatin/paclitaxel) in advanced NUT carcinoma | 1/2 | Recruiting |
| [NCT05372640](https://clinicaltrials.gov/study/NCT05372640) | **ZEN003694 + abemaciclib** (CDK4/6i) | 1 | Recruiting |
| [NCT07050186](https://clinicaltrials.gov/study/NCT07050186) | **Cemiplimab** in incurable metastatic/unresectable NUT carcinoma | 2 | Recruiting |
| [NCT07863765](https://clinicaltrials.gov/study/NCT07863765) | **Enfortumab vedotin** (anti-nectin-4 ADC) for thyroid and NUT carcinomas | 2 | Not yet recruiting |
| [NCT06943521](https://clinicaltrials.gov/study/NCT06943521) | MT-4561 in advanced solid tumours incl. NUT carcinoma | 1/2 | Recruiting |
| [NCT07459127](https://clinicaltrials.gov/study/NCT07459127) | Multicentre retrospective cohort, pulmonary NUT carcinoma | — | Active, not recruiting |
| [NCT07072143](https://clinicaltrials.gov/study/NCT07072143) | International study, paediatric rare tumours incl. NUT carcinoma | — | Recruiting |
| [NCT05265429](https://clinicaltrials.gov/study/NCT05265429) | YOUNG LUNG biology study (incl. NUT carcinoma) | — | Recruiting |
| [NCT05812027](https://clinicaltrials.gov/study/NCT05812027) | TAA/HLA/HLA-LOH screening study (incl. NUT carcinoma) | — | Active, not recruiting |

*(Two trials returned by the ClinicalTrials.gov query — NCT07817329 "NUT Project: Nutritional Support in Thoracic Oncology" and NCT07733466 on **betel-nut**-associated oral carcinoma — are **false positives on the string "NUT"** and are unrelated to this disease. Worth knowing if you automate trial curation for this entry.)*

**Consensus trial-design recommendations** ([PMID:35417004](https://pmc.ncbi.nlm.nih.gov/articles/PMC9197941/)): lower trial eligibility to **age 12**; enrol all patients in the **NUT Carcinoma Registry**; perform NGS for *NUTM1* rearrangement on all thoracic tumours.

### 12.9 Treatment algorithm (synthesised)

1. **Establish the diagnosis** — NUT IHC, then RNA fusion sequencing to identify the partner.
2. **Stage** with CT and FDG-PET/CT; MRI for skull base/orbit.
3. **Assess resectability immediately.** If localised and resectable (far more often non-thoracic): **complete resection with negative margins**, followed by radiotherapy ± chemotherapy. This is the only established path to cure and the window is short.
4. **If unresectable or metastatic:** enrol in a clinical trial as first choice. Otherwise multimodal chemotherapy (ifosfamide-based or platinum/etoposide) + definitive radiotherapy to the primary where feasible.
5. **Consider checkpoint blockade** added to first-line chemotherapy in PD-L1-positive non-surgical disease, with awareness of the hyperprogression signal.
6. **At progression:** BET inhibitor (trial preferred), with the expectation of higher benefit if the partner is BRD3 or NSD3.
7. **Throughout:** registry enrolment, early palliative care, symptom-directed intervention.
8. **Pharmacogenomics:** no NUT-carcinoma-specific PharmGKB/CPIC guidance. Standard germline considerations apply to cytotoxics (e.g. DPYD, UGT1A1) where relevant agents are used.

---

## 13. Prevention

**Primary prevention: none possible, and none is being pursued.** The causal event is a spontaneous somatic translocation with no known exogenous cause. There is no exposure to avoid, no vaccine, no chemoprophylaxis, and no behavioural intervention with any evidence base. Writing "smoking cessation" or similar into a prevention record for this disease would misrepresent the evidence — the majority of pulmonary cases arise in never-smokers.

**Immunisation:** not applicable (no infectious aetiology). Note that HPV vaccination prevents *other* head and neck carcinomas but has no bearing on NC, which is HPV-negative.

**Secondary prevention (early detection): this is where the entire preventable burden sits.** Not population screening — which is unjustifiable for a disease of this frequency with no precursor — but **diagnostic vigilance**:

- Reflex **NUT IHC** on any poorly differentiated or undifferentiated carcinoma of unknown lineage, particularly in patients under 50 and in never-smokers.
- Inclusion of *NUTM1* in all thoracic tumour NGS panels (explicit consensus recommendation).
- Rapid specialist referral once diagnosed, as urged by the German cohort authors given a 31% initial-misdiagnosis rate.
- **Clinician education** — the Chinese national survey (65.2% with no awareness of any domain) identifies the limiting factor precisely, and recommends prioritising "training for pathology services and tumor-related specialties and strengthen[ing] referral pathways and access to NUT immunohistochemistry and molecular diagnostics to reduce missed or delayed diagnoses" ([PMID:41772604](https://pubmed.ncbi.nlm.nih.gov/41772604/)).

**Tertiary prevention:** aggressive local control at first presentation (surgery + radiotherapy) to prevent the dissemination that makes the disease incurable; management of treatment toxicity, especially BET-inhibitor thrombocytopenia.

**Genetic screening and counselling:** carrier screening, cascade testing, prenatal testing and PGD are **all not applicable** — the lesion is somatic. Counselling content is limited to: this is sporadic; relatives are not at increased risk; the tumour's fusion is not heritable.

**Risk stratification:** no individual-level risk model exists or is possible. The only usable stratification is diagnostic (which biopsies warrant NUT testing).

**Public health / environmental interventions:** not applicable.

---

## 14. Other Species / Natural Disease

**There is no naturally occurring NUT carcinoma described in any non-human species.** It does not appear in OMIA, and there is no veterinary literature on spontaneous *NUTM1*-rearranged carcinoma in companion animals, livestock, or wildlife. This is an **engineered-model-only** disease outside humans.

**Taxonomy:**
- *Homo sapiens* — **NCBITaxon:9606** (the only species with naturally occurring disease).
- *Mus musculus* — **NCBITaxon:10090** (engineered models only).

**Breed:** not applicable — no VBO identifier.

**Orthologous genes:**

| Species | Gene | Location | Identifier |
|---|---|---|---|
| Human | *NUTM1* | 15q14 | HGNC:29919; NCBI Gene **256646** |
| Human | *BRD4* | 19p13.12 | HGNC:13575 |
| Mouse | *Nutm1* | **chromosome 2** | MGI ID **(not verified — look up)** |
| Mouse | *Brd4* | **chromosome 17** | MGI ID **(not verified — look up)** |

The mouse chromosome assignments are established by the syntenic **t(2;17)** translocation engineered in the NCT model ([PMID:38724194](https://www.life-science-alliance.org/content/7/7/e202402602)). Per the repository's *Naming Genes in a Model's Own Species* rule, mouse genes in any animal-model record must be bound to **MGI:** identifiers, not to `hgnc:`.

**Comparative biology:**
- The BRD4–p300 acetylation machinery and the BET-protein/acetyl-lysine reading module are deeply conserved across vertebrates, which is why a mouse translocation reproduces the human disease.
- The mouse model recapitulates the human disease well at the histological and molecular level: squamous cell carcinomas with variable differentiation, areas of keratinisation, "pervasive nuclear NUTM1 expression," and "extensive MYC, KRT14, and P63 positivity."
- NUT's physiological role in spermiogenesis (histone-to-protamine exchange with BRDT and EP300) is conserved in mammals.

**Transmission:** not applicable. **No zoonotic potential, no cross-species transmission, no infectious component.**

---

## 15. Model Organisms

### 15.1 Genetically engineered mouse model — the field's major recent advance

**NUT carcinoma translocator (NCT) mouse** — [Zheng D et al., *Life Sci Alliance* 2024;7(7):e202402602. PMID:38724194](https://www.life-science-alliance.org/content/7/7/e202402602)

- **Design:** CRISPR-inserted loxP sites in mouse *Brd4* and *Nutm1*; Cre-mediated stochastic reciprocal **t(2;17)** translocation generating the *Brd4::Nutm1* fusion *in situ*, at the endogenous locus, under endogenous regulation. This is the right design — a knock-in transgene would not reproduce the native expression context.
- **Penetrance:** **100%** in every lineage tested — KRT14-Cre head and neck (n>50), Pdx1-Cre pancreas (18/18), Prrx1-Cre soft tissue (9/9), NLS-Cre constitutive (25/25).
- **Phenotype recapitulation (good):** squamous cell carcinomas, poorly differentiated/basaloid, with keratinisation foci and intratumoural heterogeneity; nuclear NUTM1; MYC, KRT14, P63 positive; variable clustered SOX2. Transcriptomics: 3,065 up / 2,654 down genes; GSEA enrichment for proliferation, mitosis, MYC targets, metabolic reprogramming; CIBERSORT shows proliferating basal cell enrichment.
- **Metastasis modelled:** Pdx1-Cre pancreatic tumours disseminate widely with micrometastasis within 10 weeks, with desmoplasia, activated fibroblasts and EMT markers.
- **Limitations:** tumour site is dictated by the Cre driver, not by the biology that selects sites in patients, so the model cannot explain the human thoracic/head-and-neck site distribution. Mouse immune context differs. The relationship between mouse tumour latency and human disease tempo is not established.
- **Key application already delivered:** the conditional *Sox2* knockout showing **SOX2 is dispensable** for NC initiation and progression in both SOX2-expressing (oral) and SOX2-absent (pancreatic) lineages, with tumours retaining histology and the BRD4::NUTM1/MYC/TP63 programme ([PMID:41266112](https://pmc.ncbi.nlm.nih.gov/articles/PMC12634820/)). This **contradicts** the in-vitro knockdown literature and is a model-organism result that should temper, not be averaged with, the cell-line data.

### 15.2 Human cell lines

| Line | Fusion | Origin |
|---|---|---|
| **TC-797** (797) | BRD4-NUT | classic NMC line |
| **PER-403** | BRD4-NUT | 11-year-old female, poorly differentiated intrathoracic squamous carcinoma of possible thymic origin |
| **PER-624** | — | paediatric NMC |
| **TY-82** | BRD4-NUT | widely used |
| **HCC2429** | BRD4-NUT | |
| **10326** | **BRD3-NUT** | one of few BRD3 models |
| **10-15** | BRD4-NUT | |
| **00-143** | BRD-NUT | |
| Controls | — | HTB-43, HCC-95 (squamous, NUT-wild-type) |

Cellosaurus accessions were **not resolved in this session** — look them up before binding any `experimental_models` record.

### 15.3 Xenografts

Luciferised **TC-797** and **PER-403** xenograft models support bioluminescent longitudinal imaging and survival endpoints. PER-403 xenografts demonstrated significant survival benefit from HDAC inhibition (LBH-589, P=0.001) with increased histone acetylation and morphological squamous differentiation ([PMID:21447744](https://pmc.ncbi.nlm.nih.gov/articles/PMC3070805/)). Patient-derived xenografts are described but not systematically catalogued.

### 15.4 Other model systems

- **Human stem-cell / iPSC models:** used to show cell-state-dependent megadomain placement — BRD4-NUT expressed in pluripotent vs mesoderm-induced cells formed megadomains at "dissimilar patterns" ([PMID:37131839](https://academic.oup.com/genetics/article/224/3/iyad083/7147209)). This is the key model for the cell-of-origin question.
- **Invertebrate models (Drosophila, C. elegans), zebrafish:** none established.
- **Organoids:** none published for NC specifically — a clear gap given their value elsewhere in squamous biology.
- **Oncolytic virotherapy models:** the 10-15 line has been used in this context.

### 15.5 Research applications and limitations

**What the models support:** mechanism (megadomain formation, feed-forward acetylation), drug screening (the CUDC-907/panobinostat/AZD5153 IC₅₀ data come from NC lines), combination-therapy testing (BETi + CDK4/6i, BETi + p300i), and now genetic epistasis *in vivo*.

**Principal unmet model need, stated by the field itself:** "**Immunocompetent mouse models for combination testing**" ([PMID:35417004](https://pmc.ncbi.nlm.nih.gov/articles/PMC9197941/)). The NCT mouse now supplies this — immunotherapy combination work in NC should move onto it rather than continuing in xenografts, given that the disease's defining immunological feature is a cold microenvironment that a xenograft cannot model at all.

**Resources:** MGI, IMSR, Alliance of Genome Resources for mouse strains; the **International NUT Carcinoma Registry** (nc-registry.org / nmcregistry.org, Brigham and Women's Hospital — C.A. French) for clinical data and tissue.

---

## Curation notes and open questions

Flagging these explicitly because they bear on how a knowledge-base entry should be built, and several are places where the literature does not agree with itself.

1. **Name and MONDO label.** The MONDO label `nut midline carcinoma` is superseded. Per the `entry-naming` rule that a name must cover exactly what the entry covers, "NUT Carcinoma" is correct and "NUT Midline Carcinoma" is too narrow (it excludes renal, pancreatic, cutaneous and bone primaries that the entry must cover). Consider reporting the stale label upstream to MONDO.

2. **Granularity (design decisions §3a).** NC is a **histologic/molecular entity** at the WHO blue-book level with its own ICD-O code (8023/3) — the correct default rung. It is *not* a biomarker stratum of squamous cell carcinoma, despite the 2025 *Nat Rev Clin Oncol* argument for reclassification; that argument is about how the field should *organise* the entity, not about whether it is one. Thoracic vs head-and-neck NC should be `has_subtypes` or prognostic strata, **not** separate entries, since they share every pathophysiology node. "Metastatic NUT carcinoma" must never be an entry.

3. **Cell of origin (design decisions §3d).** The origin node is the *NUTM1* fusion node, marked `variant_origin: SOMATIC`, `functional_impact_category: GAIN_OF_FUNCTION`. The `cell_types` on that node are the derivation. Evidence supports a basal/squamous epithelial progenitor (CL:0000646 **verify**), but the mouse model's pancreatic and mesenchymal tumours mean a single bound cell type will be an oversimplification — record the uncertainty in `notes` rather than binding a confident wrong answer.

4. **SOX2 is a genuine in-vitro / in-vivo contradiction.** Cell-line knockdown says SOX2 is required for the differentiation block; conditional knockout in the NCT mouse says it is dispensable for initiation and progression. This is textbook `HUMAN_MODEL_MISMATCH` material — or rather its inverse — and should be curated as an open question with both results cited, not resolved.

5. **The epidemiology has two incompatible numbers and both are real.** ~20 ascertained cases/year (registry) versus ~1,400 estimated true cases/year (US). A `prevalence` record needs `measure_type: ANNUAL_INCIDENCE`, an explicit `rate_denominator`, and `notes` stating which basis each figure uses. Conflating them would be a serious misrepresentation in either direction.

6. **NHWD-870 is conference/press-release evidence only.** The 45% thoracic ORR is the most clinically significant claim in this report and is the least well-sourced. Do not curate it as a peer-reviewed finding; re-check for a journal publication.

7. ***NUTM1* fusion ≠ NUT carcinoma.** *NUTM1*-rearranged B-ALL, *CIC::NUTM1* sarcoma and *NUTM1* poroma are different diseases. Any gene-level record for *NUTM1* should make this explicit, or a gene page will silently merge four entities.

8. **Every CURIE marked (verify)** in this report must be resolved against its ontology and its canonical label copied before binding. That applies to all HPO, UBERON, CL, GO, CHEBI and LOINC suggestions above; the NCIT treatment terms quoted from the repository's own documentation (C15986, C15632, C15313, C15329, C15747, C15315, C15302) were read from a source and are safer, but still warrant `just validate-terms`.

9. **Not covered because not applicable:** inheritance pattern, penetrance, expressivity, anticipation, founder effects, consanguinity, carrier frequency, newborn/carrier/prenatal screening, infectious agents, gene–environment interaction, veterinary natural disease, zoonosis. Each is a *reported negative*, not an unexamined gap, and should be recorded as such rather than left blank.

---

## Sources

- [Luo J et al. Hiding in plain sight: NUT carcinoma is an unrecognized subtype of squamous cell carcinoma of the lungs and head and neck. *Nat Rev Clin Oncol* 2025;22(4):292–306. PMID:39900969](https://www.nature.com/articles/s41571-025-00986-3)
- [Zhang Y et al. International guidelines on the diagnosis and treatment of NUT carcinoma. *Innovation (Camb)* 2025. PMID:41737331](https://pubmed.ncbi.nlm.nih.gov/41737331/)
- [Chau NG et al. An anatomical site and genetic-based prognostic model for patients with NUT midline carcinoma. *JNCI* 2020. PMID:32328562](https://pmc.ncbi.nlm.nih.gov/articles/PMC7165803/)
- [French CA et al. Report of the First International Symposium on NUT Carcinoma. *Clin Cancer Res* 2022. PMID:35417004](https://pmc.ncbi.nlm.nih.gov/articles/PMC9197941/)
- [Eagen KP, French CA. Supercharging BRD4 with NUT in carcinoma. *Oncogene* 2021. PMID:33452461](https://pmc.ncbi.nlm.nih.gov/articles/PMC7914217/)
- [French CA et al. BRD4-NUT fusion oncogene: a novel mechanism in aggressive carcinoma. *Cancer Res* 2003. PMID:12543779](https://pubmed.ncbi.nlm.nih.gov/12543779/)
- [Alekseyenko AA et al. The oncogenic BRD4-NUT chromatin regulator drives aberrant transcription within large topological domains. *Genes Dev* 2015. PMID:26220994](https://genesdev.cshlp.org/content/29/14/1507.full.html)
- [Schwartz BE et al. Differentiation of NUT midline carcinoma by epigenomic reprogramming. *Cancer Res* 2011. PMID:21447744](https://pmc.ncbi.nlm.nih.gov/articles/PMC3070805/)
- [Zheng D et al. Brd4::Nutm1 fusion gene initiates NUT carcinoma in vivo. *Life Sci Alliance* 2024. PMID:38724194](https://www.life-science-alliance.org/content/7/7/e202402602)
- [SOX2 is a dispensable modulator of NUT carcinoma oncogenesis in mice. *Life Sci Alliance* 2025. PMID:41266112](https://pmc.ncbi.nlm.nih.gov/articles/PMC12634820/)
- [Alekseyenko AA et al. Cell state-dependent chromatin targeting in NUT carcinoma. *Genetics* 2023. PMID:37131839](https://academic.oup.com/genetics/article/224/3/iyad083/7147209)
- [Farooq A et al. NUT Carcinoma: A Comprehensive Immunohistochemical Analysis of 57 Cases. *Arch Pathol Lab Med* 2024. PMID:38059551](https://meridian.allenpress.com/aplm/article/148/8/898/497494/Nuclear-Protein-in-Testis-NUT-Carcinoma-A)
- [Kroening G et al. Multiomic Characterization and Molecular Profiling of NUT Carcinoma. *JCO Precis Oncol* 2024. PMID:39447095](https://ascopubs.org/doi/10.1200/PO.24.00334)
- [Kloker LD et al. Clinical management of NUT carcinoma in Germany. *Lung Cancer* 2024;189:107496. PMID:38301600](https://pubmed.ncbi.nlm.nih.gov/38301600/)
- [Bauer DE et al. Clinicopathologic features and long-term outcomes of NUT midline carcinoma. *Clin Cancer Res* 2012. PMID:22896655](https://pubmed.ncbi.nlm.nih.gov/22896655/)
- [Chau NG et al. Intensive treatment and survival outcomes in NUT midline carcinoma of the head and neck. *Cancer* 2016. PMID:27509377](https://pubmed.ncbi.nlm.nih.gov/27509377/)
- [Lemelle L et al. NUT carcinoma in children and adults: a multicenter retrospective study. *Pediatr Blood Cancer* 2017. PMID:28643357](https://pubmed.ncbi.nlm.nih.gov/28643357/)
- [Stathis A et al. Clinical response of carcinomas harboring the BRD4-NUT oncoprotein to OTX015/MK-8628. *Cancer Discov* 2016. PMID:26976114](https://pubmed.ncbi.nlm.nih.gov/26976114/)
- [Piha-Paul SA et al. Phase 1 study of molibresib (GSK525762) in NUT carcinoma and other solid tumors. *JNCI Cancer Spectr*. PMID:32328561](https://pubmed.ncbi.nlm.nih.gov/32328561/)
- [Shapiro GI et al. Phase 1 study of RO6870810 in NUT carcinoma, other solid tumours, or DLBCL. *Br J Cancer* 2021. PMID:33311588](https://pubmed.ncbi.nlm.nih.gov/33311588/)
- [Jung M et al. Clinicopathological and preclinical findings of NUT carcinoma: a multicenter study. *Oncologist* 2019. PMID:30696721](https://pubmed.ncbi.nlm.nih.gov/30696721/)
- [French CA et al. NSD3-NUT fusion oncoprotein in NUT midline carcinoma. *Cancer Discov* 2014. PMID:24875858](https://pubmed.ncbi.nlm.nih.gov/24875858/)
- [NUT Carcinoma — An Underdiagnosed Malignancy. *Front Oncol* 2022. PMID:35957893](https://pmc.ncbi.nlm.nih.gov/articles/PMC9360329/)
- [NUT Carcinoma: Clinicopathologic Features, Molecular Genetics and Epigenetics. *Front Oncol* 2022. PMID:35372003](https://pmc.ncbi.nlm.nih.gov/articles/PMC8966081/)
- [The expanding universe of NUTM1 fusions in pediatric cancer. *Pediatr Blood Cancer* 2023. PMID:37082775](https://pmc.ncbi.nlm.nih.gov/articles/PMC10432870/)
- [Primary pulmonary NUT carcinoma: an extended review. PMID:42865603](https://pmc.ncbi.nlm.nih.gov/articles/PMC13655413)
- [Arabi TZ et al. Nationwide retrospective study on the prevalence and prognostic factors of NUT carcinoma in the United States. *Ann Med Surg* 2025. PMID:40486575](https://pubmed.ncbi.nlm.nih.gov/40486575/)
- [Yang G et al. Survival and treatment selection in NUT carcinoma: a population-based study. *Transl Cancer Res* 2026. PMID:42870800](https://pubmed.ncbi.nlm.nih.gov/42870800/)
- [Ye Z et al. A nationwide survey of awareness and understanding of NUT carcinoma among clinicians in China. *BMC Health Serv Res* 2026. PMID:41772604](https://pubmed.ncbi.nlm.nih.gov/41772604/)
- [Xie et al. *Histol Histopathol* 2025;40:1839–1846](https://www.hh.um.es/pdf/Vol_40/40_11/Xie-40-1839-1846-2025.pdf)
- [Primary pulmonary NUT carcinoma clinical review. *Front Oncol* 2021](https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2021.690115/full)
- [Hyperacute progression of sinonasal NUT carcinoma after pembrolizumab-based treatment. *Laryngoscope* 2025](https://onlinelibrary.wiley.com/doi/10.1002/lary.70733)
- [Zhejiang Wenda Pharma NHWD-870 HCl phase II results, 2026 ESMO (press release)](https://en.prnasia.com/releases/global/zhejiang-wenda-pharma-announces-positive-results-from-phase-ii-trial-of-oral-bet-inhibitor-nhwd-870-hcl-at-the-2026-esmo-annual-meeting-553108.shtml) · [trade coverage](https://www.clinicaltrialvanguard.com/news/nhwd-870-hcl-hits-45-response-rate-in-thoracic-nut-carcinoma/)
- [PathologyOutlines — NUT carcinoma (lung)](https://www.pathologyoutlines.com/topic/lungtumornutcarcinoma.html) · [(sinonasal)](https://www.pathologyoutlines.com/topic/nasalnutcarcinoma.html) · [(cutaneous adnexal)](https://www.pathologyoutlines.com/topic/skinnonmelanocyticcutaneousadnexalNUT.html)
- [ENCR — Changes in ICD-O-3.2 (2021)](https://www.encr.eu/sites/default/files/inline-files/Changes%20ICD-O-3.2.pdf)
- [OMIM \*608963 NUTM1](https://www.omim.org/entry/608963) · [Atlas of Genetics and Cytogenetics in Oncology — NUTM1](https://atlasgeneticsoncology.org/gene/41595/nutm1-(nuclear-protein-in-testis)) · [NCBI Gene 256646](https://www.ncbi.nlm.nih.gov/gene/256646)
- [International NUT Carcinoma Registry](https://nc-registry.org/) · [Dana-Farber NUT Carcinoma Center](https://www.dana-farber.org/cancer-care/types/nut-carcinoma)
- MONDO:0005563 via [EBI OLS4](https://www.ebi.ac.uk/ols4/ontologies/mondo); HGNC identifiers via [genenames.org REST](https://rest.genenames.org/); trials via [ClinicalTrials.gov API v2](https://clinicaltrials.gov/)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 42 |
| Resolved | 42 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 38 |
| Quoted claims found in source | 10 |
| Quoted claims **not** found in source | 28 |
| References weighed for topical relevance | 42 |
| On topic | 40 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:41737331` *(abstract only)*: "NUT carcinoma (NC) is a rare and highly aggressive malignancy characterized by *NUTM1* gene fusions."
  - closest text in source: "Nuclear protein in testis (NUT) carcinoma (NC) represents a rare, clinically aggressive cancer defined by pathognomonic NUT Midline Carcinoma Family Member 1 (NUTM1) gene fusions, with bromodomain and extraterminal domain (BET) protein 4 (BRD4)-NUTM1 being the predominant oncogenic driver"
- `PMID:33452461` *(abstract only)*: "NCs are genomically stable… Apart from the *NUTM1*-fusion, NCs lack oncogenic mutations, have low tumor mutation burdens, and have few, if any, copy number alterations."
  - closest text in source: "Common targets of MDs across multiple NCs and tissues are three stem cell-related transcription factors frequently implicated in cancer: MYC, SOX2, and TP63"
- `PMID:35957893` *(abstract only)*: "Unlike other solid tumors with complex chromosomal rearrangements and a high mutational burden, NCs display a simple karyotype, often with only one alteration comprising the translocation."
  - closest text in source: "NC is characterized by a single translocation involving the NUTM1 (NUT midline carcinoma family member 1) gene and different partner genes"
- `PMID:42865603` *(abstract only)*: "median interval from symptom onset to diagnosis is 10 weeks"
  - closest text in source: "This review provides an updated overview of its pathological features, clinical presentation, diagnosis, treatment, and prognosis, aiming to serve as a practical reference for clinicians and pathologists."
- `PMC:PMC13655413` *(abstract only)*: "median interval from symptom onset to diagnosis is 10 weeks"
  - closest text in source: "This review provides an updated overview of its pathological features, clinical presentation, diagnosis, treatment, and prognosis, aiming to serve as a practical reference for clinicians and pathologists."
- `PMID:39447095` *(abstract only)*: "Co-occurring mutations in epigenetic or cell cycle pathways were observed in 26% of cases."
  - closest text in source: "RESULTS: While NC is driven by NUTM1 fusion oncoproteins, co-occurring DNA mutations in epigenetic or cell cycle pathways were observed in 26% of cases"
- `PMID:33452461` *(abstract only)*: "stimulated the ability of p300 to in vitro acetylate purified H3 histones."
  - closest text in source: "BRD4-NUT nuclear foci correspond with massive contiguous regions of chromatin co-enriched with BRD4-NUT, p300, and acetylated histones, termed "megadomains" (MD)"
- `PMID:33452461` *(abstract only)*: "BRD4-NUT first bound to regular enhancers, and then spread contiguously… over time (7h) to form mature MDs"
  - closest text in source: "Finally, we discuss how our knowledge of BRD4-NUT function has been leveraged for the therapeutic development of first-in-class BET inhibitors and other targeted strategies."
- `PMID:26220994` *(abstract only)*: "BRD4-NUT co-occupies with p300 unprecedented 100kb-2 Mbp 'megadomains' of acetylated chromatin."
  - closest text in source: "BRD4-NUT forms distinctive nuclear foci in patient tumors, which we found correlate with ∼100 unprecedented, hyperacetylated expanses of chromatin that reach up to 2 Mb in size"
- `PMID:21447744` *(abstract only)*: "BRD4-NUT expression causes global histone hypoacetylation and transcriptional repression. The fusion protein sequesters histone acetyltransferase (p300) activity."
  - closest text in source: "In both gain-of and loss-of-expression assays, we find that expression of BRD4-NUT is associated with globally decreased histone acetylation and transcriptional repression"
- `PMID:33452461` *(abstract only)*: "Across five different cell line and tissues we have identified a very limited set of NC-specific, common MDs: those associated with the *MYC*, *TP63*, and *SOX2* loci."
  - closest text in source: "Common targets of MDs across multiple NCs and tissues are three stem cell-related transcription factors frequently implicated in cancer: MYC, SOX2, and TP63"
- `PMID:38724194` *(abstract only)*: "proliferation, mitosis, MYC targets, and **metabolic reprogramming** pathways"
  - closest text in source: "The consistent induction of poorly differentiated carcinoma demonstrated a strong reprogramming activity of BRD4::NUTM1"
- `PMID:41266112` *(abstract only)*: "only modest transcriptional changes affecting metabolic pathways"
  - closest text in source: "Bulk RNA sequencing revealed only modest transcriptional changes in SOX2-deficient tumors, primarily affecting metabolic and biosynthetic pathways, without disrupting core oncogenic programs"
- `PMC:PMC12634820` *(abstract only)*: "only modest transcriptional changes affecting metabolic pathways"
  - closest text in source: "Bulk RNA sequencing revealed only modest transcriptional changes in SOX2-deficient tumors, primarily affecting metabolic and biosynthetic pathways, without disrupting core oncogenic programs"
- `PMID:33452461` *(abstract only)*: "Cell-of-origin remains undefined"
  - Text part not found as substring: 'Cell-of-origin remains undefined' (note: only abstract available for PMID:33452461, full text may contain this excerpt)
- `PMC:PMC7914217` *(abstract only)*: "Cell-of-origin remains undefined"
  - Text part not found as substring: 'Cell-of-origin remains undefined' (note: only abstract available for PMID:33452461, full text may contain this excerpt)
- `PMID:39900969` *(abstract only)*: "with approximately 1,400 annual cases in the United States and a median survival of roughly 6.5 months, this disease surpasses the incidence of certain established NSCLC and HNSCC subtypes yet remains misclassified as a distinct orphan entity."
  - closest text in source: "The orphan classification of NUT carcinoma as a distinct entity leads to a lack of awareness of this malignancy among oncologists and surgeons, despite early diagnosis being crucial for this cancer type with a median survival of only ~6.5 months"
- `PMID:35417004` *(abstract only)*: "NUT immunohistochemistry is adequate for diagnosis and should be considered in any patient with a poorly differentiated carcinoma."
  - closest text in source: "While the incidence likely exceeds that of Ewing sarcoma, and BRD4-NUT heralded the bromodomain and extra-terminal domain (BET) inhibitor class of selective epigenetic modulators, NUT carcinoma is incorrectly perceived as "impossibly rare," and therefore receives comparatively little private or governmental funding or prioritization by pharma"
- `PMID:35957893` *(abstract only)*: "There is currently no standard-of-care therapy for NC, and patients face a grim prognosis."
  - closest text in source: "There are currently no standard-of-care treatment options for patients with NC"
- `PMID:35417004` *(abstract only)*: "the only chance for long-term survival."
  - Text part not found as substring: 'the only chance for long-term survival.' (note: only abstract available for PMID:35417004, full text may contain this excerpt)
- `PMID:35417004` *(abstract only)*: "four long term complete responses (CR) or cures reported"
  - closest text in source: "Broadly, the four areas discussed by experts in the field included (1) the biology of NUT carcinoma; (2) standard approaches to the treatment of NUT carcinoma; (3) results of clinical trials using BET inhibitors; and (4) future directions, including novel BET bromodomain inhibitors, combinatorial approaches, and immunotherapy"
- `PMC:PMC9197941` *(abstract only)*: "four long term complete responses (CR) or cures reported"
  - closest text in source: "Broadly, the four areas discussed by experts in the field included (1) the biology of NUT carcinoma; (2) standard approaches to the treatment of NUT carcinoma; (3) results of clinical trials using BET inhibitors; and (4) future directions, including novel BET bromodomain inhibitors, combinatorial approaches, and immunotherapy"
- `PMID:26976114` *(abstract only)*: "BET bromodomain inhibitors were initially discovered in NUT midline carcinoma (NMC)"
  - closest text in source: "UNLABELLED: The antineoplastic, prodifferentiative effects of bromodomain and extra-terminal (BET) bromodomain (BRD) inhibitors were initially discovered in NUT midline carcinoma (NMC), an aggressive subtype of squamous cancer driven by the BRD4-NUT fusion oncoprotein"
- `PMID:41737331` *(abstract only)*: "Future research directions include exploring new therapeutic strategies (such as highly selective BET inhibitors, BET-inhibitor combinations, and **PROTAC technologies**)"
  - closest text in source: "Future research directions include improving diagnostic efficiency, exploring new therapeutic strategies (such as highly selective BET inhibitors, BET-inhibitor combinations, and PROTAC technologies), and recommending basket trials as a research approach for patients with NUTM1 gene fusions."
- `PMID:35417004` *(abstract only)*: "consensus recommendation to consider the addition of immune checkpoint blockade to the treatment paradigm of non-surgically treated NC patients with PD-L1+ disease"
  - closest text in source: "To raise awareness, propagate scientific knowledge, and initiate a consensus on standard and targeted treatment of NUT carcinoma, we held the First International Symposium on NUT Carcinoma on March 3, 2021"
- `PMC:PMC9197941` *(abstract only)*: "consensus recommendation to consider the addition of immune checkpoint blockade to the treatment paradigm of non-surgically treated NC patients with PD-L1+ disease"
  - closest text in source: "To raise awareness, propagate scientific knowledge, and initiate a consensus on standard and targeted treatment of NUT carcinoma, we held the First International Symposium on NUT Carcinoma on March 3, 2021"
- `PMID:35417004` *(abstract only)*: "**Immunocompetent mouse models for combination testing**"
  - Text part not found as substring: '**Immunocompetent mouse models for combination testing**' (note: only abstract available for PMID:35417004, full text may contain this excerpt)
- `PMC:PMC9197941` *(abstract only)*: "**Immunocompetent mouse models for combination testing**"
  - Text part not found as substring: '**Immunocompetent mouse models for combination testing**' (note: only abstract available for PMID:35417004, full text may contain this excerpt)

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 67 |
| Resolved | 56 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 3 |
| Unverifiable | 8 |
| Terms whose name was checked | 5 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0005563` (5 mentions) - the report calls it "MONDO"; MONDO calls it **nut midline carcinoma**
- `DOID:0060463` (1 mention) - the report calls it "DOID"; DOID calls it **NUT midline carcinoma**
- `EFO:0005783` (1 mention) - the report calls it "EFO"; EFO calls it **obsolete_NUT midline carcinoma**
- `NCIT:C93352` (1 mention) - the report calls it "verify"; NCIT calls it **Targeted Therapy**
- `NCIT:C15433` (1 mention) - the report calls it "verify"; NCIT calls it **Nutritional Support**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `EFO:0005783` (obsolete_NUT midline carcinoma) (1 mention) - replaced by `http://purl.obolibrary.org/obo/MONDO:0005563`
- `GO:0043974` (obsolete histone H3-K27 acetylation) (1 mention)
- `GO:0070577` (obsolete lysine-acetylated histone binding) (1 mention) - replaced by `GO:0140566`

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `LOINC`.