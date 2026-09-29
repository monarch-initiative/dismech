---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-24T16:50:44.397634'
end_time: '2026-09-24T16:56:19.469993'
duration_seconds: 335.07
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: RPE65-Related Retinopathy
  mondo_id: MONDO:0100368
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
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 16
  num_turns: 19
  total_cost_usd: 1.4404046
  session_id: fd65d8eb-852b-5a9d-91de-140beff025e2
  stop_reason: end_turn
  assistant_text_blocks: 1
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderBillingError
  status_code: 402
  remedy: the account is out of credits
  retryable: false
- provider: claude_code
  succeeded: true
citation_count: 43
reference_validation:
  total_references: 33
  verified: 33
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 7
  quotes_valid: 3
  quotes_unsupported: 4
  unsupported_quote_references:
  - PMC:PMC7016655
  - PMC:PMC10813228
  - PMID:25030840
  - PMC:PMC4687523
  relevance_assessed: 33
  on_topic: 28
  needs_review: true
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 54
  verified: 51
  not_found: 1
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.019
  labels_checked: 28
  labels_matching: 15
  labels_mismatched: 9
  mislabelled_terms:
  - term_id: HP:0006990
    reported_labels:
    - Eye poking
    ontology_label: Myelin-dependent gliosis
  - term_id: HP:0008515
    reported_labels:
    - Hyperopia
    ontology_label: Aplasia/Hypoplasia of the vertebrae
  - term_id: HP:0000603
    reported_labels:
    - Constriction of peripheral visual field
    ontology_label: Central scotoma
  - term_id: GO:0003920
    reported_labels:
    - "retinal isomerase activity \u2014 closest functional GO term for the isomerohydrolase\
      \ activity"
    ontology_label: GMP reductase activity
  - term_id: GO:0033748
    reported_labels:
    - bisretinoid catabolism, indirectly relevant
    ontology_label: hydrogenase (acceptor) activity
  - term_id: CHEBI:17278
    reported_labels:
    - all-trans-retinyl ester
    - retinyl ester, generic
    ontology_label: 5beta-cholestane-3alpha,7alpha,12alpha,26-tetrol
  - term_id: CHEBI:17885
    reported_labels:
    - 11-cis-retinal
    ontology_label: CDP-glycerol
  - term_id: CL:0000604
    reported_labels:
    - retinal rod cell
    - 'Affected cell populations: rod photoreceptors'
    ontology_label: retinal rod cell
  - term_id: UBERON:0001782
    reported_labels:
    - choroid
    ontology_label: pigmented layer of retina
  labels_variant: 4
  unresolved_terms:
  - HP:0000513
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** RPE65-Related Retinopathy
- **MONDO ID:** MONDO:0100368 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **RPE65-Related Retinopathy** covering all of the
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

# RPE65-Related Retinopathy: Comprehensive Research Report

**MONDO ID:** MONDO:0100368
**Category:** Mendelian, autosomal recessive (rare autosomal dominant form also reported)
**Key OMIM entries:** #204100 (Leber Congenital Amaurosis 2, LCA2), #613794 (Retinitis Pigmentosa 20, RP20), *180069 (Retinoid Isomerohydrolase RPE65, the gene locus)

---

## 1. Disease Information

**Overview.** RPE65-related retinopathy is the umbrella term for a spectrum of autosomal recessive (and, rarely, autosomal dominant) inherited retinal dystrophies caused by biallelic (or, for one specific variant, heterozygous) pathogenic variants in *RPE65*, which encodes the retinal pigment epithelium (RPE)-specific isomerohydrolase that regenerates the visual chromophore 11-*cis*-retinal. The clinical spectrum spans a continuum of severity: **Leber congenital amaurosis (LCA2)** at the severe end, **early-onset severe retinal dystrophy (EOSRD)** in the middle, and **RPE65-associated retinitis pigmentosa (RP20)**, sometimes with juvenile onset, at the milder end — "the three phenotypes of autosomal recessive RPE65-related retinal degeneration, from most severe to mildest, are Leber congenital amaurosis (LCA), early-onset severe retinal dystrophy (EOSRD), and juvenile retinitis pigmentosa (RP)" (GeneReviews, NBK549574). This is the first inherited retinal disease with an FDA/EMA-approved gene-replacement therapy (voretigene neparvovec-rzyl, Luxturna).

**Key identifiers:**

| Resource | Identifier |
|---|---|
| OMIM (LCA2) | #204100 |
| OMIM (RP20) | #613794 |
| OMIM (gene) | *180069 |
| MONDO | MONDO:0100368 (per prompt); related MONDO:0018091 (LCA2) |
| Orphanet | ORPHA:65 (Leber congenital amaurosis, umbrella); RPE65-specific subtype pages exist under the LCA/EOSRD Orphanet classification |
| MeSH | Leber Congenital Amaurosis (D016954); Retinitis Pigmentosa (D012174) |
| Gene | HGNC:10294 (RPE65); NCBI Gene 6121; Ensembl ENSG00000116745 |
| ICD-10 | H35.5 (hereditary retinal dystrophy); ICD-11 9B76 |

**Synonyms:** RPE65-associated retinal dystrophy; RPE65-mediated inherited retinal disease (RPE65-IRD); Leber congenital amaurosis type 2 (LCA2); RPE65 deficiency; Retinitis pigmentosa 20 (RP20); autosomal recessive childhood-onset severe retinal dystrophy (RPE65 type); retinoid isomerohydrolase deficiency.

**Evidence basis:** This report draws on OMIM/GeneReviews disease-level syntheses, structured registries (Orphanet, ClinVar/ClinGen), large multi-center natural-history and clinical-trial cohorts (e.g., the Phase 1/3 voretigene neparvovec program), and individual case reports/small case series for variant-level detail — the evidence tiers differ and are noted per claim.

---

## 2. Etiology

**Disease causal factor:** RPE65-related retinopathy is **monogenic**. Biallelic loss-of-function or hypomorphic variants in *RPE65* (chromosome 1p31.3) cause the autosomal recessive spectrum (LCA2/EOSRD/RP20). A single specific missense variant, **p.Asp477Gly (D477G)**, causes a distinct **autosomal dominant** late-onset retinitis pigmentosa through a toxic gain-of-function/aggregation mechanism rather than simple haploinsufficiency (see §4 and §6).

**Genetic risk factors:**
- **Causal variants:** >150 distinct pathogenic *RPE65* variants reported across missense, nonsense, frameshift, splice-site, and small in-frame indel classes (ClinVar; PMC7016655 "Pathogenicity Reclassification of RPE65 Missense Variants").
- **Modifier genes:** No well-established modifier locus is confirmed for RPE65-retinopathy specifically, unlike CEP290-LCA (where AHI1 has been proposed as a modifier; PMC3048164). Phenotypic variability among biallelic-genotype-matched patients is well documented but its genetic basis is not fully resolved.
- **Consanguinity:** Increases homozygosity for rare recessive *RPE65* alleles in populations/families with high consanguinity rates; multiple case series (e.g., from the Russian Federation, PMC10671290; East Asian cohorts, PMC9644481) report founder/recurrent alleles.
- **Founder alleles:** Population-specific recurrent variants are documented; East Asian carrier frequency was estimated at ~0.10% (11/10,919 alleles) in gnomAD/KRGDB-derived East Asian samples and ~0.06% in Koreans specifically (PMC9644481, Orphanet J Rare Dis 2022).

**Environmental risk factors:** None established as causal — this is a purely Mendelian disease. However, **ambient light/luminance exposure modulates phenotype severity** in the dominant D477G form: "The interplay of environmental luminance and genetics in the retinal dystrophy induced by the dominant RPE65 mutation" (PMC8931212, PNAS 2022) demonstrates that light exposure interacts with the D477G genotype to determine degeneration severity in animal models, a rare example of gene-environment interaction in an otherwise monogenic disease.

**Protective factors:** No genetic protective variants are established. Reduced UV/blue-light exposure is biologically plausible as ameliorating in the dominant form (lipofuscin/A2E-related photo-oxidative mechanisms, see §6) but is not established as a clinical protective intervention through controlled trials.

**Gene-environment interactions:** Best characterized for **D477G** — see PMC8931212 above; not established for the biallelic recessive forms, where disease is fully penetrant regardless of environment.

---

## 3. Phenotypes

### Core phenotype set (by category)

**Symptoms/signs — visual:**
| Phenotype | Frequency/notes | Suggested HP term |
|---|---|---|
| Severe congenital/infantile vision loss (LCA) or progressive vision loss (EOSRD/RP) | Nearly universal for LCA form; onset in infancy | HP:0000618 (Blindness) / HP:0000505 (Visual impairment) |
| Nystagmus (typically pendular) | Very common, often presenting sign in infancy | HP:0000639 (Nystagmus) |
| Nyctalopia (night blindness) | "Most patients with RPE65 mutations are profoundly night blind"; earliest symptom, often before central vision loss, even in RP-only phenotype | HP:0000662 (Nyctalopia) |
| Photophobia | Common | HP:0000613 (Photophobia) |
| Sluggish or near-absent pupillary light reflex | Frequent in LCA | HP:0007686 (Abnormal pupillary function) / HP:0008070 (Sluggish pupillary response) |
| Oculodigital sign (eye-poking/pressing/rubbing) | Common in infantile LCA presentations | HP:0006990 (Eye poking) |
| High hyperopia | Frequent | HP:0008515 (Hyperopia) |
| Keratoconus | Reported, secondary to chronic eye rubbing | HP:0000563 (Keratoconus) |
| Cataract | Reported as a secondary/late finding | HP:0000518 (Cataract) |
| Strabismus | Common | HP:0000486 (Strabismus) |
| Reduced/constricted visual field | Progressive | HP:0000603 (Constriction of peripheral visual field) |
| Variable/abnormal fundus appearance | "Variable appearance to the fundus" — ranges from near-normal in infancy to bone-spicule pigmentary changes, attenuated vessels, optic disc pallor, and macular atrophy with progression | HP:0007663 (Reduced visual acuity) as functional correlate; HP:0000580 (Pigmentary retinopathy); HP:0000556 (Retinal dystrophy) |
| Macular atrophy/coloboma-like macular changes | More characteristic in later stages and in some genotypes | HP:0007401 (Macular atrophy) |

**Laboratory/electrophysiologic abnormality (functional):**
- **Electroretinogram (ERG):** severely reduced or non-recordable (rod and cone responses) — "the ERG is severely reduced or non-recordable" in RPE65-LCA/EOSRD. In the milder RP20 phenotype ERG may remain partially recordable, especially earlier in the disease course. Suggested term: HP:0000513 (Abnormal electroretinogram)/ more specific HP:0000662-associated functional test findings.
- **Full-field stimulus threshold (FFST):** markedly elevated dark-adapted thresholds (used as a primary trial endpoint; log-unit improvements of ~2 log10 cd·s·m⁻² reported post-gene-therapy).

**Phenotype characteristics:**
- **Age of onset:** LCA form — onset in infancy, typically within the first year of life (congenital or near-congenital); EOSRD — early childhood; RP20 (autosomal recessive juvenile/childhood RP) — onset from childhood into adolescence; the OMIM RP20 family description notes "onset of severe visual impairment was between 3 and 7 years of age, with night blindness being a typical and early symptom in all patients." The autosomal dominant D477G form is distinctly **later-onset** ("advanced late-onset retinitis pigmentosa," PMC7228561).
- **Severity:** Generally severe (profound, near-blind) in LCA; variable but progressive in EOSRD/RP.
- **Progression:** Progressive in all forms; central vision is often relatively preserved longer than peripheral/night vision early on, but declines with age — "night blindness is one of the earliest symptoms but patients tend to suffer central visual loss later." In a large natural-history case series, children aged 4–10 years already had severe visual impairment (mean visual acuity ~20/126).
- **Frequency among affected individuals:** Night blindness and nystagmus are present in nearly all cases; keratoconus and cataract are present in a minority and tend to be later complications.

**Quality of life impact:** Profound vision loss from infancy has major developmental, educational, and psychosocial consequences (mobility, literacy via Braille/assistive technology, dependence). Gene-therapy trials formally captured functional vision (multi-luminance mobility testing, MLMT) and quality-of-life instruments, showing meaningful gains post-treatment, "particularly in younger patients" (per long-term follow-up data).

---

## 4. Genetic/Molecular Information

**Gene:** *RPE65* — Retinoid Isomerohydrolase RPE65; HGNC:10294; chromosome 1p31.3 (varies slightly by source, commonly cited 1p31); NM_000329.3 is the reference transcript used in clinical variant nomenclature.

**Causal genes/loci:** RPE65 is the sole causal gene for this entity by definition. OMIM lists two disease associations: #204100 LCA2 (autosomal recessive) and #613794 RP20 (autosomal recessive); a separate autosomal dominant RP phenotype (sometimes designated RP87 in more recent OMIM nomenclature) is caused specifically by the heterozygous D477G variant.

**Variant spectrum and classification:**
- **Types:** missense (the largest category), nonsense, frameshift (e.g., c.106del predicted to cause a frameshift and premature stop, leading to nonsense-mediated decay), splice-site, and small in-frame deletions/insertions.
- **ACMG/ClinVar classification:** Variants are individually curated pathogenic/likely pathogenic/VUS per ACMG-AMP criteria; a ClinGen RPE65-specific Variant Curation Expert Panel specification exists (cspec.genome.network/cspec/ui/svi/doc/GN120), refining general ACMG rules for this gene. A dedicated reclassification effort addressed missense VUS: "Pathogenicity Reclassification of RPE65 Missense Variants Related to Leber Congenital Amaurosis and Early-Onset Retinal Dystrophy" (PMC7016655).
- **Population allele frequency:** Individual pathogenic variants are each very rare in gnomAD (e.g., c.1039C>T p.Arg347Cys reported at ~0.00000124 allele frequency, 5/1,179,740 alleles, in European non-Finnish gnomAD), consistent with a rare recessive disease; aggregate carrier frequency in East Asians was estimated at ~0.10%.
- **Somatic vs. germline:** Exclusively germline; no somatic mosaicism mechanism described for this disease.
- **Functional consequences:**
  - Most recessive loss-of-function alleles (nonsense, frameshift, canonical splice-site) abolish or near-abolish isomerohydrolase enzymatic activity — complete **loss of function**.
  - Many missense alleles are **hypomorphic** (partial loss of function), correlating with the milder EOSRD/RP20 end of the phenotypic spectrum rather than LCA — see the "novel RPE65 hypomorph" functional study (PMC5015590).
  - The dominant **D477G** variant does not act by simple haploinsufficiency: functional studies show "the adverse cellular consequence of the D477G mutant coexpressed with WT-RPE65 far exceeded that of losing a single allele of WT-RPE65," and structural/biochemical work indicates D477G forms an **aggregation-prone surface** that induces abnormal protein–protein interactions with wild-type RPE65, driving RPE65 protein degradation and reduced isomerase activity beyond what simple heterozygous loss would predict — i.e., a **toxic/dominant-negative gain-of-function** mechanism (PMID:29659842, Hum Mol Genet 2018; PMC7760593/PMID:33261050).

**Modifier genes:** None definitively established for the RPE65-recessive spectrum.

**Epigenetic information:** No disease-specific DNA methylation/histone modification mechanism is established as causal; this is a classic monogenic enzymatic deficiency disease.

**Chromosomal abnormalities:** Not a recognized mechanism — disease results from point mutations/small indels within *RPE65*, not large structural rearrangements, though whole-gene or exonic deletions have occasionally been reported as pathogenic alleles.

**Ontology suggestions:** Gene — hgnc:10294 (RPE65); Molecular function — GO:0003920 (retinoid isomerohydrolase activity / GO:0033760 "retinal isomerase activity" umbrella term), GO:0033748 (bisretinoid catabolism, indirectly relevant); relevant CHEBI terms: CHEBI:17561 (retinol), CHEBI:17278 (all-trans-retinyl ester), CHEBI:17885 (11-cis-retinal).

---

## 5. Environmental Information

RPE65-related retinopathy is not an infectious, toxin-induced, or classically "environmental" disease — it is monogenic. The only substantiated environmental interaction is:

- **Ambient luminance/light exposure** as a phenotype modifier specifically for the **dominant D477G** allele (PMC8931212, PNAS 2022) — higher-light environments were associated with greater retinal dystrophy severity in genetically modeled systems, implicating light-driven photo-oxidative stress (via the retinoid/lipofuscin cycle, see §6) as an aggravating factor superimposed on the genetic lesion.
- **Vitamin A/retinoid status:** Because RPE65 sits in the core vitamin A (retinoid) visual cycle, systemic vitamin A metabolism is mechanistically intertwined with the RPE65 defect, though dietary vitamin A supplementation has **not** been shown to correct the enzymatic block (unlike some other IRDs, e.g., Refsum disease with dietary phytanic acid restriction). This is the pharmacological rationale instead for exogenous synthetic retinoid replacement therapy (QLT091001/9-cis-retinyl acetate; see §12).
- **No infectious agents** are implicated.
- **Lifestyle factors:** No behavioral risk-modifying factor (smoking, diet, exercise) has controlled-trial evidence in this specific disease, though general retinal-health advice (UV protection) is plausible extrapolation from the light-luminance mechanistic data above, primarily relevant to D477G carriers.

Suggested ECTO term if curating an environmental modifier edge: an ambient/ocular light-exposure term (e.g., ECTO class for "light exposure") linked specifically to the D477G pathophysiology node, with `environmental_effect: EXACERBATES`.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (recessive/loss-of-function form — LCA2/EOSRD/RP20)

1. Biallelic loss-of-function or hypomorphic pathogenic variants in *RPE65* **lead to** absent or markedly reduced RPE65 retinoid isomerohydrolase enzymatic activity in the retinal pigment epithelium (demonstrated biochemically; PMID:16116091, PNAS 2005 — "RPE65 is the isomerohydrolase in the retinoid visual cycle").
2. Loss of isomerohydrolase activity **results in** failure to convert all-*trans*-retinyl ester to 11-*cis*-retinol within the RPE cell, the rate-limiting step of the retinoid ("visual") cycle.
3. Absence of 11-*cis*-retinol/11-*cis*-retinal **leads to** depletion of functional visual chromophore available to combine with opsin apoprotein in rod and cone outer segments, so rhodopsin (rods) and cone opsins cannot be regenerated after bleaching.
4. Chromophore-free ("apo-") opsin **causes** two convergent downstream consequences, demonstrated to be mechanistically distinct in rods versus cones:
   - **4a. Rods:** unliganded rod opsin is intrinsically unstable/constitutively signals abnormally and **triggers** a **Bax-dependent apoptotic pathway** in rod photoreceptors (PMC2720534, "Bax-Induced Apoptosis in Leber's Congenital Amaurosis: A Dual Role in Rod and Cone Degeneration"), together with **upregulation of lysosomal-mediated autophagic gene expression** contributing to early rod apoptosis in *Rpe65⁻/⁻* mice (PMID:22227450).
   - **4b. Cones:** cone photoreceptor death proceeds via a **Bax-independent** mechanism — "early loss of cones was not prevented in *Rpe65⁻/⁻*/*Bax⁻/⁻* mice, indicating that pro-apoptotic Bax was not involved in the pathogenesis of cone cell death in Rpe65-deficient mice" — implicating a separate degenerative cascade (proposed to relate to chronic unliganded-cone-opsin signaling/ER stress rather than classical Bax-mediated apoptosis) and explaining the disproportionately early, severe cone dysfunction seen clinically even though rods normally vastly outnumber cones.
5. Progressive rod and (via the separate pathway) cone photoreceptor apoptosis **results in** outer-segment shortening/disorganization and eventual photoreceptor cell loss, detectable clinically as thinning of the outer nuclear layer/ellipsoid zone on OCT and as non-recordable or severely reduced ERG amplitudes.
6. Concurrently, accumulation of un-isomerized all-*trans*-retinyl esters and derived bis-retinoid byproducts (notably **A2E**, a diretinal-phosphatidylethanolamine conjugate formed from all-*trans*-retinal condensing with phosphatidylethanolamine in photoreceptor outer segments and subsequently phagocytosed into the RPE) **accumulates as RPE lipofuscin**. A2E cannot be enzymatically degraded, perturbs RPE lysosomal membrane integrity and phagolysosomal function (inhibiting phagolysosomal degradation of photoreceptor phospholipid), and confers susceptibility to blue-light-induced RPE apoptosis — providing a secondary, light-exacerbated toxic mechanism to RPE and photoreceptor injury superimposed on the primary chromophore-deprivation mechanism. (Note: in the RPE65-null state itself, lipofuscin/A2E accumulation is *reduced* relative to wild type because retinyl-ester substrate is not being processed through the normal cycle at all — the Leu450Met *Rpe65* hypomorphic mouse variant, by contrast, shows reduced A2E via slowed cycle flux, PMID:15277666 — so the lipofuscin/A2E axis is most clinically relevant to milder hypomorphic and to the light-modulated dominant D477G phenotype rather than to null LCA2.)
7. Clinically, this cascade **manifests as** profound infantile/childhood visual impairment, nystagmus, night blindness, and a non-recordable or severely subnormal ERG (steps 1→3 dominate the earliest, most severe LCA presentation; steps 4→6 drive the progressive component seen even in successfully gene-corrected retina, explaining why continued photoreceptor loss can occur after gene therapy despite restored chromophore supply — see §12).

### Branch: dominant D477G mechanism
1′. The heterozygous **D477G** missense variant **produces** a structurally abnormal RPE65 protein with an aggregation-prone surface.
2′. This mutant protein **engages in atypical protein–protein interactions** with co-expressed wild-type RPE65, **causing** wild-type RPE65 protein degradation and a net reduction in cellular isomerase activity that **exceeds** the reduction expected from simple loss of one functional allele (i.e., not classical haploinsufficiency) — a **dominant-negative/toxic gain-of-function** mechanism (PMID:29659842; PMID:33261050).
3′. The resulting partial visual-cycle impairment, superimposed on and exacerbated by ambient light/luminance exposure (PMC8931212), **leads to** a milder, later-onset retinitis pigmentosa phenotype than the biallelic null state.

### Categories covered

- **Molecular pathways:** Retinoid (visual) cycle — RPE65 catalyzes the committed isomerization/hydrolysis step converting all-*trans*-retinyl ester → 11-*cis*-retinol (KEGG: Retinol metabolism, hsa00830; Reactome: "Visual phototransduction").
- **Cellular processes:** Apoptosis (rod: Bax-dependent, GO:0006915/GO:0043523 negative regulation of neuron apoptotic process is disrupted; cone: Bax-independent, distinct pathway); autophagy/lysosomal gene upregulation (GO:0006914 autophagy); phagolysosomal dysfunction in RPE.
- **Protein dysfunction:** Loss of enzymatic function (null/hypomorphic alleles) vs. misfolding/aggregation-driven dominant-negative toxicity (D477G).
- **Metabolic changes:** Disrupted vitamin A/retinoid metabolism; secondary accumulation of retinyl esters and altered bis-retinoid (A2E) flux.
- **Tissue damage mechanisms:** Chronic photo-oxidative stress from lipofuscin/A2E accumulation, particularly light-exposure-dependent.
- **Biochemical abnormality:** Isomerohydrolase enzyme deficiency — the defining lesion.
- **Molecular profiling:** Biochemical/functional assays (HPLC-MS/MS quantification of retinoids) are used for variant functional characterization (e.g., PMC7138296-style approach applied across LCA genes); RPE65 protein expression studies in HEK293/insect-cell heterologous systems and iPSC-derived RPE/retinal organoids from patients (PMC6749091) recapitulate reduced isomerase activity and photoreceptor phenotypes in vitro.

**Suggested GO terms:** GO:0003920 (retinal isomerase activity — closest functional GO term for the isomerohydrolase activity), GO:0009416 (response to light stimulus), GO:0007601 (visual perception), GO:0006915 (apoptotic process), GO:0043524 (negative regulation of neuron apoptotic process).
**Suggested CL terms:** CL:0000210 (photoreceptor cell), CL:0000604 (retinal rod cell), CL:0000573 (retinal cone cell), CL:0002586 (retinal pigment epithelial cell).
**Suggested CHEBI terms:** CHEBI:17561 (retinol), CHEBI:17885 (11-cis-retinal), CHEBI:17278 (retinyl ester, generic), lipofuscin/A2E lacks a precise CHEBI ID commonly used in curation — record as free text if no exact match.

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary organ:** eye — specifically the neurosensory retina and retinal pigment epithelium (UBERON:0000966 retina; UBERON:0002050 retinal pigment epithelium is not a standard distinct UBERON ID — RPE is typically captured via CL:0002586 cell type plus UBERON:0000966 retina, or UBERON:0001782 (choroid)-adjacent structures depending on ontology version).
- **Secondary involvement:** cornea (keratoconus secondary to chronic eye-rubbing, UBERON:0000362 cornea), lens (cataract, UBERON:0001845), extraocular muscles (strabismus, secondary to poor fixation).
- **Body systems:** primarily the visual/sensory system (nervous system extension); no systemic organ involvement — RPE65-retinopathy is a non-syndromic, eye-limited disease (distinguishing it from syndromic ciliopathy-associated LCA genes such as CEP290).

**Tissue and cell level:**
- Neurosensory retina — outer nuclear layer (photoreceptor cell bodies), photoreceptor inner/outer segments.
- RPE monolayer — site of the primary enzymatic defect (CL:0002586, retinal pigment epithelial cell).
- Affected cell populations: rod photoreceptors (CL:0000604) and cone photoreceptors (CL:0000573), both degenerate, via distinct mechanisms (§6); RPE cells (CL:0002586) accumulate lipofuscin/A2E.

**Subcellular level:**
- RPE smooth endoplasmic reticulum — site of RPE65 enzymatic activity (GO Cellular Component: GO:0005783 endoplasmic reticulum; RPE65 is a microsomal membrane-associated protein).
- RPE lysosomes — site of A2E/lipofuscin accumulation and impaired phagolysosomal degradation (GO:0005764 lysosome).
- Photoreceptor outer segment discs — site of opsin/chromophore complex formation and of A2E precursor formation (GO:0001750 photoreceptor outer segment).

**Localization:** Bilateral, generally symmetric involvement (as expected for a systemic monogenic enzymatic deficiency rather than a focal lesion); no lateralization pattern reported.

---

## 8. Temporal Development

**Onset:**
- LCA2: congenital/infantile — visual manifestations typically apparent within the first year of life; frequently the presenting complaint is roving eye movements/nystagmus and lack of visual fixation noticed by caregivers in early infancy.
- EOSRD: early childhood onset, intermediate severity.
- RP20 (recessive, juvenile RP phenotype): onset in one documented family series between ages 3–7 years, with night blindness as the earliest and most consistent symptom.
- Dominant D477G RP: distinctly **later-onset**, described in the literature as "advanced late-onset retinitis pigmentosa" (PMC7228561), i.e., adult-onset relative to the recessive forms.
- Onset pattern: insidious/progressive rather than acute, though the profound congenital deficit in LCA2 can appear as an abrupt discovery at birth/infancy even though the underlying enzymatic lesion is present from conception.

**Progression:**
- Disease course is chronic and progressive across the spectrum; there is no spontaneous remission.
- Natural history: night blindness (rod-pathway dysfunction) typically precedes and is more severe/earlier than central (cone-mediated) visual loss, which develops later but can still occur in the first decade — "children ages four to ten years in the largest case series had severe visual impairment (mean visual acuity: 20/126)."
- Progression rate: variable across the recessive spectrum (LCA fastest/most severe from birth; RP20 slower); within any one genotype, phenotype severity can still vary between patients, suggesting genetic background or environmental modifiers.
- Disease duration: lifelong, chronic — no natural resolution; some patients with milder hypomorphic alleles retain functional (if severely reduced) vision into adulthood, providing the therapeutic window exploited by gene therapy.
- Even after gene augmentation therapy restores chromophore-generating capacity, **continued photoreceptor degeneration** has been documented in surviving but already-compromised retina (see §12) — i.e., the enzymatic correction does not fully halt an already-initiated degenerative process in retina beyond a certain disease stage, underscoring the importance of the "critical period"/treatment-timing concept below.

**Patterns:**
- No remission pattern (progressive monogenic disease).
- **Critical period for intervention:** A central concept in this disease's management is that gene therapy is most effective when administered to retina with sufficient **viable photoreceptors remaining** — "treated locations having more than 63% of normal photoreceptors showed robust treatment-related retention of photoreceptors in the long term, while treated regions with less retained photoreceptors at the time of the intervention showed progressive degeneration similar to untreated regions" — establishing a structural/temporal window beyond which restoring the enzyme cannot rescue already-committed-to-death photoreceptors. This underlies current gene-therapy eligibility criteria requiring sufficient viable retinal area (see §10, §12).

---

## 9. Inheritance and Population

**Epidemiology:**
- LCA overall (all genes combined) affects an estimated **1 in 30,000 to 1 in 81,000 live births**; RPE65 accounts for roughly **5–10%** of LCA cases.
- Retinitis pigmentosa overall affects **1 in 3,000–7,000** people; autosomal recessive RP accounts for ~5–20% of RP, and RPE65 accounts for roughly **2–5% of autosomal recessive RP**.
- In a multi-center inherited-retinal-dystrophy cohort of 2,240 patients, 18 (0.8%) had RPE65-related disease: 38.8% presenting as LCA, 22.2% as RP, 33.3% as severe early-onset retinal dystrophy, and 5.5% as congenital stationary night blindness-like presentation — illustrating the phenotypic breadth captured under one genotype.
- In a Russian Federation cohort, RPE65-associated retinopathy accounted for 5.3% (25/474) of molecularly confirmed inherited retinal disease cases (PMC10671290).
- **Global disease burden:** given the rarity, RPE65-retinopathy is classified as an ultra-rare disease; precise worldwide point-prevalence figures analogous to Orphanet's numeric prevalence bands are not consistently published as a single figure, but the above LCA/RP fraction data support an estimated worldwide prevalence in the range of roughly 1–2 per 100,000 to 1 per 1,000,000 (consistent with an Orphanet "1-9 / 1,000,000" or similarly rare band; a precise Orphanet numeric class was not independently confirmed in this search).

**Inheritance pattern:** Predominantly **autosomal recessive** (biallelic pathogenic variants — homozygous or compound heterozygous); a distinct, well-characterized **autosomal dominant** form exists caused specifically by the heterozygous D477G variant.

**Penetrance:** The recessive forms are essentially fully penetrant given biallelic pathogenic genotypes (consistent with a classic enzyme-deficiency Mendelian disease). Penetrance/expressivity of D477G dominant disease is modulated by environmental light exposure (§2, §6), suggesting incomplete or variable penetrance/expressivity for that specific allele depending on environmental luminance history — an unusual and specifically documented gene-environment penetrance modifier for a monogenic retinal disease.

**Expressivity:** Variable — even among patients with identical or similar biallelic genotypes, phenotype severity (LCA vs. EOSRD vs. RP20) and rate of progression differ, and macular morphology differs by causal gene even within the LCA differential (RPE65 vs. CEP290 vs. GUCY2D vs. AIPL1 patients show distinguishable macular phenotypes), suggesting genotype is only a partial predictor.

**Genetic anticipation:** Not described — RPE65-retinopathy is not a repeat-expansion disorder.

**Germline mosaicism:** Not specifically documented as a recurring feature in RPE65-retinopathy literature reviewed; general recessive-disease recurrence-risk counseling principles apply (25% recurrence risk per pregnancy for carrier parents of an affected homozygous/compound heterozygous child).

**Founder effects:** Documented at the population level — recurrent/founder pathogenic alleles reported in specific populations (East Asian, Russian, and other cohorts cited above), though no single globally dominant founder allele analogous to some other IRD genes has been established across all populations.

**Consanguinity role:** As with other rare autosomal recessive IRDs, consanguineous unions increase homozygosity for rare pathogenic *RPE65* alleles and are commonly noted in case series from populations with higher consanguinity rates.

**Carrier frequency:** Estimated ~0.10% in East Asians (gnomAD/KRGDB combined) and ~0.06% in Koreans specifically (PMC9644481); carrier frequencies elsewhere are lower given the gene's overall rarity and the population-specific nature of most pathogenic alleles.

**Population demographics:** No strong sex predilection is reported (autosomal, not X-linked); no major geographic endemicity beyond population-specific founder-allele effects; age distribution of affected individuals spans from infancy (LCA presentation) through adulthood (dominant D477G presentation), reflecting the phenotypic spectrum rather than a single onset age.

---

## 10. Diagnostics

**Clinical tests:**
- **Electroretinography (ERG):** central diagnostic test — severely reduced or non-recordable scotopic and photopic responses in LCA/EOSRD; may show residual but markedly subnormal responses in milder RP20/dominant D477G presentations, especially earlier in the disease course.
- **Optical coherence tomography (OCT):** assesses outer nuclear layer/ellipsoid zone thickness and residual photoreceptor structure — critical for gene-therapy eligibility assessment (identifying sufficient viable retina) and for longitudinal monitoring of structural decline post-treatment.
- **Fundus autofluorescence:** can show altered patterns related to lipofuscin/RPE status, useful in phenotyping and monitoring.
- **Full-field stimulus threshold (FFST) testing:** dark-adapted psychophysical threshold test — the primary functional endpoint in the pivotal voretigene neparvovec trials, given the non-recordable ERG in many LCA patients makes ERG unsuitable as a treatment-response endpoint.
- **Multi-luminance mobility testing (MLMT):** a functional-vision obstacle-course assay developed specifically for the voretigene neparvovec trials, assessing ability to navigate a course at graded light levels — became a novel, disease-specific, FDA-recognized functional endpoint.
- **Visual field testing:** Goldmann or other perimetry to assess peripheral field constriction, where central fixation/cooperation allow.
- **Biopsy/histopathology:** not routinely performed given the availability of genetic diagnosis; historical/postmortem histopathology contributed to early understanding of photoreceptor/RPE degeneration.

**Genetic testing:**
- **Recommended approach:** targeted *RPE65* single-gene sequencing when clinical phenotype (early nyctalopia, ERG pattern) is suggestive, or more commonly as part of a **multi-gene inherited retinal disease (IRD)/LCA panel** given overlapping phenotypes among the ~20+ LCA-associated genes (see differential diagnosis below) — panel-based next-generation sequencing (NGS) is now first-line given genetic and phenotypic heterogeneity of LCA/EOSRD, with **whole exome sequencing (WES)** as a common escalation when panels are non-diagnostic, given the diagnostic yield reported (e.g., PMID:28966547, "Diagnostic application of clinical exome sequencing in Leber congenital amaurosis").
- **Whole genome sequencing (WGS):** used in research/tertiary settings when exome-negative, to capture deep intronic or structural variants.
- **Chromosomal microarray/karyotype/FISH:** not primary tools for this specific monogenic point-mutation disease; not typically indicated unless a contiguous gene deletion is suspected.
- **Confirmatory requirement for gene therapy:** biallelic *RPE65* pathogenic/likely pathogenic variant confirmation is an **absolute prerequisite** for voretigene neparvovec eligibility per FDA label and the international consensus eligibility recommendations (PMID:34088339, Orphanet J Rare Dis 2021), which formalized clinical, electrophysiological, imaging, and genetic criteria (including required retinal-area/viable-photoreceptor thresholds) for patient selection.

**Clinical criteria/differential diagnosis:** RPE65-retinopathy must be distinguished from other LCA/EOSRD genes on the basis of genotype (phenotype overlap is substantial). Per GeneReviews-style LCA gene lists, at least ~20 genes cause LCA, accounting for ~70% of cases, including:

| Gene | LCA subtype | Distinguishing notes |
|---|---|---|
| GUCY2D | LCA1 | Most common LCA gene overall in many populations; near-normal fundus early, preserved photoreceptor structure with severe functional loss ("cone-rod dystrophy dissociation") |
| **RPE65** | **LCA2** | This entry; eligible for approved gene therapy |
| CRX | LCA7 | Can have dominant or recessive inheritance |
| CRB1 | LCA8 | Often with preserved paravascular retinal pigment, nanophthalmos/high hyperopia, Coats-like exudative vasculopathy |
| NMNAT1 | LCA9 | Characteristic macular coloboma-like atrophy |
| CEP290 | LCA10 | Most common single LCA gene in many Western cohorts (up to ~21% of LCA); syndromic ciliopathy associations (Joubert, Senior-Løken, Bardet-Biedl, Meckel) must be excluded |
| RDH12 | LCA13 | |
| LRAT | LCA14 | Same visual-cycle pathway as RPE65 (upstream enzyme); phenotypically similar and also responds to oral synthetic retinoid in trials |
| AIPL1 | LCA4 | Severe cone-rod phenotype |
| others | SPATA7, LCA5, RPGRIP1, IMPDH1, RD3, TULP1, IQCB1, CLUAP1, PRPH2, KCNJ13, IFT140 | Rarer causes |

Clinical phenotyping can help direct genetic testing strategy, since "different genes are associated with differential macular morphology in patients with RPE65-, CEP290-, GUCY2D-, and AIPL1-related Leber congenital amaurosis," but molecular confirmation remains the diagnostic gold standard given overlap.

**Screening:** No universal newborn screening program specifically targets RPE65-retinopathy (unlike metabolic newborn screening panels); diagnosis is prompted by parental/clinical recognition of poor visual behavior, nystagmus, or abnormal red reflex in infancy, followed by ophthalmologic and electrophysiologic evaluation and confirmatory genetic testing. Given the availability of approved gene therapy, **early genetic diagnosis is now clinically urgent** (to enable treatment while sufficient viable photoreceptors remain), which has driven increasing use of rapid genetic panels/WES in infants with suspected LCA.

---

## 11. Outcome/Prognosis

**Survival and mortality:** RPE65-retinopathy is an ocular-only, non-syndromic disease with **no reduction in life expectancy or systemic mortality** attributable to the condition itself. This distinguishes it from syndromic LCA genes (e.g., CEP290-associated ciliopathies) that carry systemic morbidity/mortality risk.

**Morbidity and function:**
- Without treatment, the natural history is progressive visual decline toward severe visual impairment/legal blindness, typically well established by the first decade of life in the LCA/EOSRD forms.
- Functional/disability burden is substantial: profound low vision from infancy affects developmental milestones, education, and independence; quality-of-life measures were formally incorporated into gene-therapy trial endpoints, which showed "meaningful benefits in selected functional outcomes and quality of life, particularly in younger patients" following treatment.

**Disease course/complications:**
- Secondary ocular complications include keratoconus (from chronic eye-rubbing/oculodigital sign) and cataract.
- Post-gene-therapy, a notable **complication not observed in the original clinical trials but reported in post-approval real-world data** is **chorioretinal atrophy** at or around the subretinal injection site — the PERCEIVE registry study (103 patients, mean age 19.5 years) found "35 patients (34%) experienced ocular treatment-emergent adverse events, most frequently related to chorioretinal atrophy" (PMC10813228), and a post-approval systematic review/meta-analysis likewise noted chorioretinal atrophy as a complication not seen pre-approval. This is an important, evolving pharmacovigilance signal.

**Recovery potential:**
- Without treatment: no spontaneous recovery; progressive decline is the rule.
- With gene therapy: substantial, rapid (within ~30 days), and durable (documented to at least 3–4 years, with some cohorts followed 7+ years) improvement in dark-adapted/light-sensitivity function and functional mobility vision is achievable, though **structural (OCT-measured) photoreceptor decline can continue** even in treated, functionally-improved eyes — "photoreceptors continue to degenerate years after gene therapy... despite continued clinical benefit in some patients," and long-term structural outcome studies (PMID:31604676, Molecular Therapy) documented an overall decrease in SD-OCT structural outcomes over 24 months of follow-up despite functional benefit. This dissociation between structural and functional trajectories is an active area of ongoing research and patient counseling importance.

**Prognostic factors:**
- **Genotype severity** (null vs. hypomorphic allele) correlates with phenotype severity (LCA vs. EOSRD vs. RP) and likely with residual photoreceptor reserve at any given age.
- **Age/disease stage at treatment** is the single most important modifiable prognostic factor for gene-therapy response: retinal regions retaining >~63% of normal photoreceptor density at treatment show robust long-term rescue, while more advanced regions continue to degenerate similarly to untreated retina — underscoring "earlier is better" for intervention.
- **Baseline visual function** (visual acuity, FFST threshold) at treatment predicts magnitude of measurable improvement in trials.

---

## 12. Treatment

### Approved gene therapy — the practice-defining treatment for this disease

**Voretigene neparvovec-rzyl (Luxturna®):** a recombinant AAV2 vector carrying a functional human RPE65 cDNA, delivered by **subretinal injection**, one eye at a time (bilateral sequential administration).
- **Mechanism:** restores RPE65 isomerohydrolase expression in transduced RPE cells, re-enabling the visual (retinoid) cycle and chromophore regeneration.
- **Pivotal evidence:** Phase 3 randomized, controlled, open-label trial (Russell et al., *Lancet* 2017) in patients ≥3 years with confirmed biallelic RPE65 mutations, best-corrected visual acuity 20/60 or worse or visual field <20°, receiving bilateral subretinal injection of 1.5×10¹¹ vector genomes in 0.3 mL — demonstrated significant improvement in the primary MLMT endpoint. Efficacy and durability further reported through pooled Phase 1/3 follow-up (PMID:31443789, "Efficacy, Safety, and Durability of Voretigene Neparvovec-rzyl... Results of Phase 1 and 3 Trials") — "the therapeutic effect is nearly maximal by 30 days after administration and is durable for 4 years, with observation ongoing," and pooled analyses show statistically significant gains in full-field stimulus threshold (2.2 log₁₀ cd·s·m⁻² improvement) and visual acuity (0.08 logMAR).
- **Regulatory status:** FDA approval December 19, 2017 (first FDA-approved gene therapy for a genetic disease and the first for an inherited retinal disease); European Commission approval November 23, 2018.
- **Long-term data:** Long-term structural outcome studies (PMID:31604676) and durability reviews (PMID:36103843, Ophthalmic Research 2022) show sustained functional benefit alongside variable/progressive structural (OCT) decline, particularly in more advanced treated regions.
- **Real-world post-approval data:** PERCEIVE registry study (up to 2 years, 103 patients; PMC10813228) confirms real-world safety/effectiveness while flagging chorioretinal atrophy as an emergent adverse event category; additional single-center case series (PMID:39900645, 2025, 14 eyes/8 patients, 26-month follow-up) report sustained visual acuity gains (mean +2 lines) and functional test improvements; a broader post-approval systematic review/meta-analysis has further quantified pooled outcomes across the post-marketing literature.
- **NCIT term suggestion:** `NCIT:C15238` (Gene Therapy) for `treatment_term`; specific agent could be recorded via `therapeutic_agent` — voretigene neparvovec has an NCIT concept (search the NCIT adapter for the specific C-code at curation time; not independently confirmed here).
- **Eligibility criteria:** formalized by international consensus (PMID:34088339, Orphanet J Rare Dis 2021) — genetically confirmed biallelic RPE65 pathogenic variants, sufficient viable retinal area/photoreceptors (informed by the structural-durability data above), and specific visual acuity/visual field thresholds; surgical and post-operative management guidance is also addressed by this consensus document.

### Investigational/historical pharmacotherapy

**QLT091001 (9-cis-retinyl acetate, an oral synthetic retinoid):** bypasses the enzymatic block by supplying a pre-formed chromophore precursor directly.
- Phase 1b trials in LCA/RP due to RPE65 or **LRAT** mutations (same visual-cycle pathway) showed: "10 (77%) of 13 LCA patients and 12 (86%) of 14 RP patients were 'responders'... in at least 1 eye in either functional retinal area or ETDRS visual acuity" (PMID:25030840, and PMC4687523/PLOS ONE).
- Also shown effective specifically in the **dominant D477G** late-onset RP phenotype: "Advanced late-onset retinitis pigmentosa with dominant-acting D477G RPE65 mutation is responsive to oral synthetic retinoid therapy" (PMC7228561) — notable because gene-replacement therapy (which adds more RPE65 protein) is mechanistically inappropriate for a toxic gain-of-function dominant allele, making a chromophore-replacement strategy a rational alternative for this specific genotype.
- **Adverse effects:** headache, fatigue, photophobia, photopsia, erythema, flushing, nausea/vomiting; reversible elevations in triglycerides, LDL, AST/ALT and reductions in HDL and thyroxine — consistent with the retinoid drug class; effects were transient/reversible.
- Not currently FDA-approved (development status per available search results is Phase 1b-level historical trial data; current regulatory status should be re-verified at curation time).

### Supportive/adjunctive care
- **Low-vision rehabilitation:** low-vision aids, orientation and mobility training, educational support (NCIT:C15315 Rehabilitation).
- **Genetic counseling:** essential given autosomal recessive (25% recurrence risk) or, for D477G, autosomal dominant (50% recurrence risk, variable penetrance by light exposure) inheritance (NCIT:C15240 Genetic Counseling).
- **Management of secondary complications:** keratoconus and cataract management via standard ophthalmic surgical approaches as needed (NCIT:C16186 Orthopedic/ophthalmic surgical procedure category as applicable; NCIT:C15329 Surgical Procedure generic).
- **UV/blue-light protection:** plausible adjunct particularly for D477G carriers given the light-luminance interaction data, though not established via controlled trial as a formal preventive intervention.

### Treatment strategy / personalized medicine
- Genotype-guided treatment is central to this disease: biallelic null/hypomorphic genotypes with adequate retinal reserve → voretigene neparvovec; the specific dominant D477G genotype → oral synthetic retinoid is mechanistically preferred over gene augmentation, illustrating a clear precision-medicine bifurcation within a single gene's disease spectrum.
- No combination-therapy regimens are established.

### Experimental pipeline (general orientation; verify current ClinicalTrials.gov status at curation time)
Beyond the above, general inherited-retinal-disease pipeline approaches with potential relevance include next-generation AAV capsids/alternate delivery routes (e.g., suprachoroidal injection, being explored broadly across IRD gene therapies to reduce surgical morbidity relative to subretinal injection) and optogenetic or photoreceptor-replacement strategies applicable at very advanced disease stages where no endogenous photoreceptors remain to rescue. Specific RPE65-dedicated trials of these newer modalities were not independently confirmed in this search session and should be verified via ClinicalTrials.gov/WHO ICTRP before citation in a KB entry.

---

## 13. Prevention

**Primary prevention:** Not applicable in the vaccination/risk-factor-modification sense, since this is a fully genetically determined (recessive) or genetically triggered (dominant, light-modulated) disease. The principal "primary prevention" avenue is **reproductive/genetic**:
- **Genetic/carrier screening:** carrier screening in populations/families with known *RPE65* pathogenic alleles, particularly relevant given documented founder alleles in specific populations.
- **Prenatal diagnosis and preimplantation genetic testing (PGT-M):** available for families with a previously identified proband/known biallelic pathogenic genotype, per standard rare-monogenic-disease reproductive genetics practice (ACMG/ACOG-aligned).
- **Genetic counseling:** central to family planning guidance given the 25% recurrence risk for recessive disease (or variable-penetrance 50% risk for D477G-associated dominant disease).

**Secondary prevention (early detection):**
- Early **genetic diagnosis in infancy** is now itself a preventive strategy in a specific sense — it enables gene therapy while sufficient photoreceptors remain viable, effectively "preventing" the otherwise inevitable progression to severe, irreversible vision loss. This reframes early diagnosis as time-critical secondary prevention rather than passive diagnostic labeling.
- No population-based newborn screening program specifically targets RPE65 currently (verify against current national newborn-screening panels at curation time, as genomic newborn screening pilots are expanding rapidly and may include IRD genes in some programs by the time of curation).

**Tertiary prevention (preventing complications):**
- Managing chronic eye-rubbing/oculodigital behavior to reduce secondary keratoconus risk.
- Routine surveillance for cataract and keratoconus.
- Post-gene-therapy structural surveillance (OCT) to detect and manage emergent chorioretinal atrophy.

**Immunization:** Not applicable — non-infectious disease.

**Behavioral interventions:** Plausible light/UV exposure moderation for D477G carriers (extrapolated from the luminance-interaction mechanistic data), not established via formal behavioral-intervention trial.

**Public health/environmental interventions:** Not applicable in the traditional sanitation/pollution-control sense; the relevant "public health" dimension is orphan-disease-specific: rare-disease registries (e.g., PERCEIVE), expanded newborn/early genetic testing infrastructure, and gene-therapy-center accreditation/access programs given the specialized surgical delivery required.

**Prophylaxis:** No pharmacologic prophylactic regimen is established; gene therapy and synthetic retinoid therapy are disease-modifying/restorative rather than prophylactic in the classical sense.

---

## 14. Other Species / Natural Disease

**Taxonomy of affected species:** Dogs (*Canis lupus familiaris*, NCBITaxon:9615) and mice (*Mus musculus*, NCBITaxon:10090) are the principal model/naturally-occurring-disease species; no other companion-animal or wildlife species with naturally occurring RPE65 deficiency was identified in this search.

**Breed:** **Briard dog** — naturally occurring *RPE65*-mutant canine model, historically first described as causing **congenital stationary night blindness (CSNB)**-like/severe early retinal dystrophy in this breed; a null mutation in canine RPE65 causes a severe retinal dystrophy phenotype. (VBO identifier for Briard breed should be looked up at curation time — not independently confirmed here.)

**Gene:** Canine RPE65 ortholog (NCBI Gene — canine RPE65 gene ID to be confirmed at curation time); murine *Rpe65* (MGI ortholog).

**Natural disease:**
- **Briard dog RPE65-CSNB/retinal dystrophy** is the paradigm naturally-occurring large-animal model and was the substrate for the field-defining proof-of-concept gene therapy experiments: **Acland and colleagues (2001, *Nature Genetics*)** showed that subretinal AAV-RPE65 gene augmentation restored visual function in RPE65-mutant dogs — "gene therapy restores vision in a canine model of childhood blindness," widely credited as the foundational large-animal proof-of-concept that catalyzed the entire RPE65 human gene-therapy development program culminating in voretigene neparvovec. Multiple subsequent canine trials refined vector dose, delivery route, and long-term durability assessment ("Gene Augmentation Trials Using the Rpe65-Deficient Dog: Contributions Towards Development and Refinement of Human Clinical Trials").
- **Veterinary relevance:** Briard-breed RPE65-CSNB is recognized in veterinary ophthalmology/OMIA as a hereditary canine eye disease of breed-health importance (consult OMIA for the specific entry at curation time).

**Comparative biology:**
- **rd12 mouse:** a spontaneously arising naturally occurring recessive nonsense *Rpe65* mutant mouse strain — "displays a profoundly diminished rod electroretinogram, an absence of 11-cis-retinaldehyde and rhodopsin, and photoreceptor degeneration," serving as the standard small-animal model for human RPE65-LCA and used extensively in gene-therapy dose-response and mechanistic (e.g., Bax-dependence) studies.
- **Rpe65⁻/⁻ knockout mouse** (engineered, distinct from rd12): the primary engineered null model used in the Bax-dependent rod-apoptosis and Bax-independent cone-death mechanistic studies cited in §6.
- Evolutionary conservation: RPE65's isomerohydrolase role in the vertebrate visual cycle is deeply conserved, with comparative work tracing "origin and evolution of retinoid isomerization machinery in vertebrate visual cycle" even to jawless vertebrates (PMC3507948), underscoring the gene's fundamental, ancient role in vertebrate vision.

**Transmission:** Not applicable — non-infectious, non-zoonotic monogenic disease; no cross-species transmission relevance.

---

## 15. Model Organisms

| Model | Type | Genetic basis | Key phenotype/utility | Reference |
|---|---|---|---|---|
| **rd12 mouse** | Naturally occurring, spontaneous mutant (Mus musculus) | Recessive nonsense *Rpe65* mutation | Profoundly diminished rod ERG, absent 11-cis-retinal and rhodopsin, progressive photoreceptor degeneration; standard model for "midcourse RPE65 LCA" — used to test gene therapy at intermediate disease stages (IOVS, "Gene Therapy Rescues Cone Structure and Function in the 3-Month-Old rd12 Mouse") | multiple, incl. IOVS study above |
| ***Rpe65⁻/⁻* knockout mouse** | Engineered knockout | Complete Rpe65 ablation | Used to dissect Bax-dependent rod apoptosis vs. Bax-independent cone death (PMC2720534); lysosomal-autophagic gene upregulation in early rod apoptosis (PMID:22227450); reduced A2E/lipofuscin due to blocked substrate flux | PMC2720534; PMID:22227450 |
| ***Rpe65* Leu450Met hypomorphic mouse variant** | Engineered/natural hypomorphic allele | Partial-activity missense variant | Slowed visual cycle flux with reduced A2E/iso-A2E lipofuscin fluorophore accumulation — models the milder, hypomorphic end of the human allelic spectrum and the lipofuscin/A2E toxicity mechanism | PMID:15277666 |
| **Briard dog** | Naturally occurring (large animal) | Canine RPE65 null mutation | Severe early retinal dystrophy/CSNB-like phenotype; historically the first large-animal model in which AAV-RPE65 subretinal gene therapy restored visual function (Acland et al. 2001), directly enabling translation to human trials; extensively used for dose/vector/delivery optimization | multiple canine gene-therapy trial reports |
| **Dominant D477G mouse/cell models** | Engineered knock-in / heterologous expression | Heterozygous D477G | Recapitulates toxic dominant-negative mechanism and light-luminance × genotype interaction on degeneration severity | PMID:29659842; PMC8931212 |
| **Patient-derived iPSC/retinal organoids** | Human cellular model | Patient-specific compound heterozygous *RPE65* genotypes | Recapitulates reduced RPE65 expression/isomerase activity and photoreceptor abnormalities in a human genetic background; used for functional variant characterization and (potentially) autologous/personalized therapeutic testing | PMC6749091 |
| **Heterologous expression systems (HEK293, insect cells)** | In vitro biochemical model | Wild-type and mutant recombinant RPE65 | Established RPE65's isomerohydrolase enzymatic activity directly (PMID:16116091) and is the standard assay platform for functional classification of novel missense variants (e.g., PMC5015590 hypomorph characterization; PMC7016655 reclassification effort) | PMID:16116091; PMC5015590; PMC7016655 |

**Phenotype recapitulation:** Both the canine and murine models faithfully recapitulate the core biochemical lesion (absent/reduced 11-cis-retinal, non-recordable or severely reduced ERG) and the therapeutic response to AAV-RPE65 gene augmentation, which is why they were sufficient to support translation to human trials without an intermediate large-animal efficacy gap — a relatively unusual and favorable translational history among inherited retinal diseases.

**Model limitations:** Mouse retina is rod-dominated (very few cones relative to human macula-containing retina), limiting direct extrapolation of cone-specific degeneration kinetics and any future macula-specific therapeutic endpoints to the human macula-bearing eye; the Briard dog model, while a valuable large-animal proof-of-concept, does not have a macula either (dogs lack a true fovea/macula), so neither major model organism fully recapitulates the human macular cone biology most relevant to central visual acuity outcomes measured in human trials — a caveat regulatory reviewers and treating clinicians have noted when interpreting preclinical durability data relative to human long-term structural (OCT) findings.

**Research applications:** Mechanistic dissection of rod vs. cone death pathways (Bax-dependence), lipofuscin/A2E toxicity biology, gene-therapy vector/dose/route optimization, disease-stage-dependent treatment-window characterization (photoreceptor-reserve threshold for rescue), and — via the D477G models — dominant-negative toxic-aggregation mechanisms and light-modulated penetrance, informing both mechanistic understanding and differential treatment-selection strategy (gene augmentation vs. chromophore replacement) described in §12.

**Resources:** MGI (Mouse Genome Informatics) for *Rpe65* mouse allele records including rd12; IMSR (International Mouse Strain Resource) for rd12 and knockout strain availability; OMIA (Online Mendelian Inheritance in Animals) for the canine Briard RPE65 entry (specific OMIA accession not independently confirmed in this search — verify at curation time).

---

## Summary Table: Suggested Ontology Bindings for KB Curation

| Concept | Suggested term | Notes |
|---|---|---|
| Gene | hgnc:10294 (RPE65) | lowercase `hgnc:` per repo convention |
| Disease (LCA form) | MONDO:0018091 or the provided MONDO:0100368 | verify exact MONDO scope/preferred ID via OAK lookup before binding |
| Night blindness | HP:0000662 (Nyctalopia) | core, earliest phenotype |
| Nystagmus | HP:0000639 | |
| Photophobia | HP:0000613 | |
| Reduced/non-recordable ERG | HP:0000513-family (abnormal ERG) | verify exact HPO term at curation time |
| Keratoconus | HP:0000563 | secondary complication |
| Cataract | HP:0000518 | secondary complication |
| Photoreceptor cell | CL:0000210 (general) / CL:0000604 (rod) / CL:0000573 (cone) | |
| RPE cell | CL:0002586 | |
| Retina | UBERON:0000966 | |
| Retinoid isomerohydrolase activity | GO term for the enzymatic function | confirm exact GO ID via OAK before binding |
| Apoptotic process | GO:0006915 | |
| Gene therapy (treatment) | NCIT:C15238 | for voretigene neparvovec |
| Pharmacotherapy (oral retinoid) | NCIT:C15986 | for QLT091001, with therapeutic_agent detail |
| Genetic counseling | NCIT:C15240 | |

**Curatorial caveat:** All ontology term IDs above should be independently verified via `runoak`/the repo's cache-first lookup workflow before being written into a KB entry — per the Ontology Term Contract, no CURIE should be bound from this report's memory-recall without a fresh lookup, and several IDs above (exact ERG-abnormality HPO term, precise MONDO scope, canine breed/gene identifiers, RPE65 NCIT drug-concept code) were explicitly flagged as unconfirmed and need lookup, not direct reuse.

---

## Sources

- [Entry - #204100 - LEBER CONGENITAL AMAUROSIS 2; LCA2 - OMIM](https://omim.org/entry/204100)
- [Entry - *180069 - RETINOID ISOMEROHYDROLASE RPE65 - OMIM](https://omim.org/entry/180069)
- [Entry - #613794 - RETINITIS PIGMENTOSA 20; RP20 - OMIM](https://omim.org/entry/613794)
- [Autosomal Recessive RPE65-Related Retinal Degeneration - GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK549574/)
- [RPE65-associated LCA - CHRD, UPenn](https://www.med.upenn.edu/chrd/rpe65.html)
- [RPE65 gene - Gene Vision](https://gene.vision/knowledge-base/rpe65-for-doctors/)
- [RPE65 is the isomerohydrolase in the retinoid visual cycle - PubMed (PMID:16116091)](https://pubmed.ncbi.nlm.nih.gov/16116091/)
- [RPE65 is the isomerohydrolase in the retinoid visual cycle - PNAS](https://www.pnas.org/doi/10.1073/pnas.0503460102)
- [RPE65: role in the visual cycle, human retinal disease, and gene therapy - PubMed](https://pubmed.ncbi.nlm.nih.gov/19373675/)
- [Voretigene neparvovec-rzyl (Luxturna) for inherited retinal dystrophy - PubMed (PMID:29635265)](https://pubmed.ncbi.nlm.nih.gov/29635265/)
- [Efficacy and safety of voretigene neparvovec... phase 3 trial - The Lancet](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(17)31868-8/abstract)
- [Efficacy, Safety, and Durability of Voretigene Neparvovec-rzyl... Phase 1 and 3 Trials - PubMed (PMID:31443789)](https://pubmed.ncbi.nlm.nih.gov/31443789/)
- [Efficacy and Safety of Voretigene Neparvovec in RPE65-Retinopathy: Phase III Trial in Japan - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12405627/)
- [Post-approval outcomes of voretigene neparvovec: systematic review and meta-analysis - PubMed](https://pubmed.ncbi.nlm.nih.gov/42425207/)
- [Real-World Safety and Effectiveness of Voretigene Neparvovec: PERCEIVE Study - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10813228/)
- [Real-world outcomes of Voretigene Neparvovec: single-centre case series - PubMed (PMID:39900645)](https://pubmed.ncbi.nlm.nih.gov/39900645/)
- [Long-Term Structural Outcomes of Late-Stage RPE65 Gene Therapy - PubMed (PMID:31604676)](https://pubmed.ncbi.nlm.nih.gov/31604676/)
- [Gene Therapy for Inherited Retinal Disease: Long-Term Durability of Effect - PubMed (PMID:36103843)](https://pubmed.ncbi.nlm.nih.gov/36103843/)
- [RPE65-associated inherited retinal diseases: consensus recommendations for eligibility to gene therapy - PubMed (PMID:34088339)](https://pubmed.ncbi.nlm.nih.gov/34088339/)
- [Carrier frequency and incidence estimation of RPE65-associated IRD in East Asian population - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9644481/)
- [A Molecular Genetic Analysis of RPE65-Associated Forms of IRD in the Russian Federation - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10671290/)
- [Prevalence and genetic characteristics of RPE65-associated retinal disease - IOVS](https://iovs.arvojournals.org/article.aspx?articleid=2741042)
- [Genetics and Phenotypes of RPE65 Mutations in Inherited Retinal Degeneration - IOVS](https://iovs.arvojournals.org/article.aspx?articleid=2162347)
- [Pathogenicity Reclassification of RPE65 Missense Variants - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7016655/)
- [A novel RPE65 hypomorph expands the clinical phenotype - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5015590/)
- [Insights into the pathogenesis of dominant retinitis pigmentosa D477G - PubMed (PMID:29659842)](https://pubmed.ncbi.nlm.nih.gov/29659842/)
- [Properties and Therapeutic Implications of D477G RPE65 Variant - PubMed (PMID:33261050)](https://pubmed.ncbi.nlm.nih.gov/33261050/)
- [The interplay of environmental luminance and genetics in D477G RPE65 dystrophy - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8931212/)
- [Advanced late-onset RP with dominant D477G RPE65 responsive to oral synthetic retinoid - PMC](https://ncbi.nlm.nih.gov/pmc/articles/PMC7228561)
- [Oral 9-cis retinoid for childhood blindness due to LCA (RPE65/LRAT) - PubMed (PMID:25030840)](https://pubmed.ncbi.nlm.nih.gov/25030840/)
- [Safety and Proof-of-Concept Study of Oral QLT091001 - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4687523/)
- [Early apoptosis of rod photoreceptors in Rpe65-/- mice - PubMed (PMID:22227450)](https://pubmed.ncbi.nlm.nih.gov/22227450/)
- [Bax-Induced Apoptosis in Leber's Congenital Amaurosis - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2720534/)
- [Rpe65 Leu450Met variant and reduced lipofuscin A2E/iso-A2E - PubMed (PMID:15277666)](https://pubmed.ncbi.nlm.nih.gov/15277666/)
- [The lipofuscin component A2E selectively inhibits phagolysosomal degradation - PNAS](https://www.pnas.org/doi/10.1073/pnas.052025899)
- [Origin and Evolution of Retinoid Isomerization Machinery in Vertebrate Visual Cycle - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3507948/)
- [Gene Augmentation Trials Using the Rpe65-Deficient Dog - Springer](https://link.springer.com/chapter/10.1007/978-1-4614-0631-0_24)
- [Human gene therapy for RPE65 isomerase deficiency activates the retinoid cycle - PNAS](https://www.pnas.org/doi/10.1073/pnas.0807027105)
- [Gene Therapy Rescues Cone Structure and Function in 3-Month-Old rd12 Mouse - IOVS](https://iovs.arvojournals.org/article.aspx?articleid=2128361)
- [Diagnostic application of clinical exome sequencing in Leber congenital amaurosis - PubMed](https://pubmed.ncbi.nlm.nih.gov/28966547/)
- [Leber Congenital Amaurosis - American Academy of Ophthalmology](https://www.aao.org/education/disease-review/leber-congenital-amaurosis-4)
- [Generation and Characterization of iPSC and Retinal Organoids from RPE65 LCA Patient - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6749091/)
- [RPE65-associated Leber Congenital Amaurosis - EyeRounds, University of Iowa](https://webeye.ophth.uiowa.edu/eyeforum/genetic/001-RPE65-LCA.htm)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 33 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 7 |
| Quoted claims found in source | 3 |
| Quoted claims **not** found in source | 4 |
| References weighed for topical relevance | 33 |
| On topic | 28 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMC:PMC7016655` *(abstract only)*: "Pathogenicity Reclassification of RPE65 Missense Variants Related to Leber Congenital Amaurosis and Early-Onset Retinal Dystrophy"
  - closest text in source: "Two other pieces of evidence were accepted after further analysis of these Brazilian families: (i) p.Phe83Leu and p.Gly187Glu segregate with childhood retinal dystrophy within families, and (ii) their prevalence in Leber congenital amaurosis (LCA)/early-onset retinal dystrophy (EORD) patients can be considered higher than in other inherited retinal dystrophy patients"
- `PMC:PMC10813228` *(abstract only)*: "35 patients (34%) experienced ocular treatment-emergent adverse events, most frequently related to chorioretinal atrophy"
  - closest text in source: "Thirty-five patients (34%) experienced ocular treatment-emergent adverse events (TEAEs), most frequently related to chorioretinal atrophy (n = 13 [12.6%])"
- `PMID:25030840` *(abstract only)*: "10 (77%) of 13 LCA patients and 12 (86%) of 14 RP patients were 'responders'... in at least 1 eye in either functional retinal area or ETDRS visual acuity"
  - closest text in source: "We regarded patients as having an improvement in vision if we noted at least a 20% improvement in retinal area on GVF compared with baseline or a visual acuity improvement of five or more letters compared with baseline in two consecutive study visits (or any improvement from no vision at baseline)"
- `PMC:PMC4687523` *(abstract only)*: "10 (77%) of 13 LCA patients and 12 (86%) of 14 RP patients were 'responders'... in at least 1 eye in either functional retinal area or ETDRS visual acuity"
  - closest text in source: "Eight of 18 patients (44%) showed a ≥20% increase and 4 of 18 (22%) showed a ≥40% increase in functional retinal area determined from Goldmann visual fields; 12 (67%) and 5 (28%) of 18 patients showed a ≥5 and ≥10 ETDRS letter score increase of visual acuity, respectively, in one or both eyes at two or more visits within 2 months of treatment"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 54 |
| Resolved | 51 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 28 |
| Terms named correctly | 15 |
| Terms named as a **different** term | 9 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0006990` (1 mention) - the report calls it "Eye poking"; HP calls it **Myelin-dependent gliosis**
- `HP:0008515` (1 mention) - the report calls it "Hyperopia"; HP calls it **Aplasia/Hypoplasia of the vertebrae**
- `HP:0000603` (1 mention) - the report calls it "Constriction of peripheral visual field"; HP calls it **Central scotoma**
- `GO:0003920` (2 mentions) - the report calls it "retinal isomerase activity — closest functional GO term for the isomerohydrolase activity"; GO calls it **GMP reductase activity**
- `GO:0033748` (1 mention) - the report calls it "bisretinoid catabolism, indirectly relevant"; GO calls it **hydrogenase (acceptor) activity**
- `CHEBI:17278` (2 mentions) - the report calls it "all-trans-retinyl ester", "retinyl ester, generic"; CHEBI calls it **5beta-cholestane-3alpha,7alpha,12alpha,26-tetrol**
- `CHEBI:17885` (2 mentions) - the report calls it "11-cis-retinal"; CHEBI calls it **CDP-glycerol**
- `CL:0000604` (3 mentions) - the report calls it "retinal rod cell", "Affected cell populations: rod photoreceptors"; CL calls it **retinal rod cell**
- `UBERON:0001782` (1 mention) - the report calls it "choroid"; UBERON calls it **pigmented layer of retina**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0000513` (2 mentions), reported as "Abnormal electroretinogram" - HP does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CHEBI:17561` (2 mentions) - the report calls it "retinol"; CHEBI calls it **L-cysteine**, and lists "FREE CYSTEINE" among its other names
- `CL:0002586` (5 mentions) - the report calls it "retinal pigment epithelial cell", "RPE cell"; CL calls it **retinal pigment epithelial cell**, and lists "RPE" among its other names
- `NCIT:C15238` (2 mentions) - the report calls it "Gene therapy (treatment)"; NCIT calls it **Gene Therapy**
- `NCIT:C15986` (1 mention) - the report calls it "Pharmacotherapy (oral retinoid)"; NCIT calls it **Pharmacotherapy**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CHEBI:17278` - called "all-trans-retinyl ester", "retinyl ester, generic"
- `GO:0006915` - called "apoptotic process", "Apoptotic process"
- `CL:0000604` - called "retinal rod cell", "Affected cell populations: rod photoreceptors"
- `CL:0002586` - called "retinal pigment epithelial cell", "RPE cell"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.