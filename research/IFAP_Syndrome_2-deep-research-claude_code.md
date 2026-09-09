---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-02T02:26:33.263906'
end_time: '2026-09-02T02:31:22.693541'
duration_seconds: 289.43
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: IFAP Syndrome 2
  mondo_id: ''
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
  web_search_requests: 13
  num_turns: 20
  total_cost_usd: 1.2507346
  session_id: 94fd9ae5-d663-5ad6-bcc2-c2b5a7cf608a
  stop_reason: end_turn
  assistant_text_blocks: 5
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
citation_count: 3
reference_validation:
  total_references: 5
  verified: 5
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 5
  on_topic: 3
  validator_version: 0.2.1
term_validation:
  total_terms: 45
  verified: 41
  not_found: 0
  obsolete: 2
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 38
  labels_matching: 20
  labels_mismatched: 13
  mislabelled_terms:
  - term_id: HP:0007431
    reported_labels:
    - Lamellar-ichthyosis-like scaling (alternative presentation)
    ontology_label: Congenital ichthyosiform erythroderma
  - term_id: HP:0100025
    reported_labels:
    - angular cheilitis
    ontology_label: Overfriendliness
  - term_id: HP:0002298
    reported_labels:
    - atrichia
    ontology_label: Absent hair
  - term_id: HP:0000966
    reported_labels:
    - "Moderate\u2013severe hypotrichosis (sparse, thin hair)"
    ontology_label: Hypohidrosis
  - term_id: HP:0011364
    reported_labels:
    - hair shaft abnormality
    ontology_label: White hair
  - term_id: HP:0012207
    reported_labels:
    - Trichorrhexis nodosa (hair shaft defect on SEM)
    ontology_label: Reduced sperm motility
  - term_id: HP:0100708
    reported_labels:
    - Meibomian gland dysfunction
    ontology_label: Abnormal microglia morphology
  - term_id: HP:0008058
    reported_labels:
    - Punctate corneal epithelial defects
    ontology_label: Aplasia/Hypoplasia of the optic nerve
  - term_id: GO:0045543
    reported_labels:
    - regulation of fatty acid biosynthetic process
    ontology_label: gibberellin 2-beta-dioxygenase activity
  - term_id: CL:1000428
    reported_labels:
    - outer root sheath cell of hair follicle, if available
    ontology_label: stem cell of epidermis
  - term_id: CL:0002261
    reported_labels:
    - sebaceous gland cell, for meibocyte-analog reasoning
    ontology_label: endothelial cell of viscerocranial mucosa
  - term_id: UBERON:0006238
    reported_labels:
    - meibomian gland
    ontology_label: future brain
  - term_id: NCIT:C61004
    reported_labels:
    - Acitretin
    ontology_label: Tablet for Solution Dosage Form
  labels_variant: 5
  obsolete_terms:
  - term_id: HP:0100637
    ontology_label: obsolete Neoplasia of the nose
    replaced_by: HP:0012720
  - term_id: GO:0044255
    ontology_label: obsolete cellular lipid metabolic process
    replaced_by: GO:0006629
  unresolvable_prefixes:
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** IFAP Syndrome 2
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **IFAP Syndrome 2** covering all of the
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

I'll research IFAP Syndrome 2 using web search and primary literature sources to build this comprehensive report.

Let me fetch the primary PMC article for full mechanistic and clinical detail, plus check GeneCards/GTR for additional data.

Now let me get the full PMC article and the recent medRxiv meibum paper for additional mechanistic detail.

I now have sufficient primary-source detail to compile the full report.

I now have comprehensive primary-source material to compile the full report.

# IFAP Syndrome 2 (SREBF1-Associated Autosomal-Dominant IFAP Syndrome): Comprehensive Research Report

## 1. Disease Information

**Overview.** IFAP syndrome 2 (IFAP2) is one of two known genetic forms of Ichthyosis Follicularis, Atrichia, and Photophobia (IFAP) syndrome, a rare ectodermal dysplasia/syndromic ichthyosis characterized by the classic triad of non-inflammatory follicular hyperkeratosis (ichthyosis follicularis), congenital or near-congenital hair loss (atrichia/hypotrichosis), and photophobia with corneal disease. Unlike the originally described X-linked form (IFAP syndrome 1, caused by *MBTPS2* mutations), IFAP2 is **autosomal dominant**, caused by heterozygous, largely *de novo* missense/small in-frame deletion variants in **SREBF1** (Sterol Regulatory Element Binding Transcription Factor 1), reported in 2020 by Wang et al. (PMID: [32497488](https://pmc.ncbi.nlm.nih.gov/articles/PMC7332643/)) — "Mutations in *SREBF1*, Encoding Sterol Regulatory Element Binding Transcription Factor 1, Cause Autosomal-Dominant IFAP Syndrome," *American Journal of Human Genetics*.

**Key identifiers:**
- **OMIM:** #619016 — IFAP SYNDROME 2; IFAP2 (gene: SREBF1, *184756*, chr 17p11.2)
- **MONDO:** MONDO:0100221 (IFAP syndrome 2); parent term MONDO:0100212 (IFAP syndrome, general)
- **Orphanet:** ORPHA2273 (IFAP syndrome, umbrella entry covering both molecular subtypes)
- **MedGen:** C5436607
- **GTR:** C5436607
- Distinguish from **IFAP syndrome 1** (OMIM #308205, X-linked, *MBTPS2*) and **BRESHECK syndrome** (a severe *MBTPS2*-allelic disorder with additional CNS/skeletal/genital anomalies)

**Synonyms:** Ichthyosis follicularis–atrichia–photophobia syndrome, type 2; autosomal-dominant IFAP syndrome; SREBF1-related IFAP syndrome.

**Evidence basis:** This is aggregated disease-level knowledge derived from a founding molecular-genetics cohort study (11 unrelated individuals, 2 families + 9 simplex cases) plus subsequent single-patient/small case-series reports — not large-scale EHR/registry data, reflecting the extreme rarity of the condition (well under 100 reported IFAP2 cases worldwide as of 2025).

## 2. Etiology

**Causal factor:** Purely monogenic/genetic. Heterozygous missense substitutions or small in-frame deletions in *SREBF1* disrupt site-1-protease (S1P) recognition and cleavage of the SREBP1 transcription factor, producing a dominant loss-of-function/dominant-negative effect on SREBP-target lipogenic and keratinization gene programs (PMID: 32497488).

**Genetic risk factors:**
- Virtually all reported pathogenic variants cluster in a **4-residue hotspot (residues 527–530)** forming the arginine-X-X-leucine (RXXL) S1P recognition motif of SREBP1:
  - **c.1579C>T, p.Arg527Cys** — the dominant recurrent variant, found in 9 of 11 individuals (82%) in the founding cohort, arising independently (mostly *de novo*, confirmed segregating in two families)
  - **c.1582_1584del, p.Asn528del** — 2/11 individuals, segregated in Family 1
  - **c.1589T>C, p.Leu530Pro** — 1/11 individuals, confirmed *de novo*
  - Additional variants reported subsequently: **p.Arg557Cys** (chr17:17720597G>A, Ambarchyan et al. 2024, *de novo*, confirmed absent in both parents) and **c.1670G>A** (associated with an atypical phenotype lacking photophobia; Zhu et al., PMID: 39912473)
- All founding-cohort variants were **absent from gnomAD and ExAC**, and the key residues (Arg527, Leu530) are highly conserved across species — consistent with pathogenicity (PMID: 32497488).
- **Inheritance:** Autosomal dominant, predominantly arising as **de novo** mutations in simplex cases, though vertical transmission was documented within two multigenerational families in the founding study (mother-daughter pairs, both surviving to adulthood, indicating compatibility with reproduction and non-lethality of the heterozygous state).

**Environmental/other risk factors:** None identified — no epidemiological or toxin/exposure association has been reported; this is a purely Mendelian condition.

**Protective factors:** None reported in the literature.

**Gene-environment interactions:** Not established; disease expression appears driven by the germline variant itself rather than by environmental modifiers, though phenotypic severity (e.g., presence/absence of photophobia, degree of skin plaque involvement) varies even among carriers of the same recurrent variant (p.Arg527Cys), suggesting stochastic or unidentified modifying factors.

## 3. Phenotypes

Phenotype data below are drawn from the founding 11-patient cohort (PMID: 32497488) and subsequent case reports (Ambarchyan et al. 2024; Zhu et al. 2025, PMID: 39912473; Zhu et al. 2025 meibum study, PMID: 40778116).

### Cutaneous
| Phenotype | HPO suggestion | Frequency/notes |
|---|---|---|
| Ichthyosis follicularis / follicular hyperkeratosis | HP:0007431 (Ichthyosis follicularis, atrichia, photophobia) or HP:0100637 (follicular hyperkeratosis) | Present in essentially all patients; onset soon after birth |
| Lamellar-ichthyosis-like scaling (alternative presentation) | HP:0007431 | Some patients present with lamellar rather than purely follicular scale, with/without psoriasiform plaques |
| Psoriasiform / hyperkeratotic plaques, extremities | HP:0007550 (or HP:0031059 psoriasiform dermatitis) | Onset early childhood; one atypical variant (c.1670G>A) produces severe psoriasis-like plaques limited to extensor lower limbs, with IL-17A/S100A8 upregulation on immunohistochemistry |
| Nail dystrophy | HP:0008404 | Reported in cohort |
| Periorificial erythema, angular cheilitis | HP:0100025 (angular cheilitis) | Reported |

### Hair
| Phenotype | HPO suggestion | Frequency |
|---|---|---|
| Congenital/near-congenital atrichia (complete) | HP:0002298 (atrichia) | 5/11 patients |
| Moderate–severe hypotrichosis (sparse, thin hair) | HP:0000966 | 4/11 patients |
| Hair depigmentation with caliber variation | HP:0011364 (hair shaft abnormality) | 1/11 patients |
| Trichorrhexis nodosa (hair shaft defect on SEM) | HP:0012207 | Cuticle warping/detachment documented by scanning electron microscopy |
| Eyebrow/eyelash/axillary/pubic hair loss | HP:0009806 (sparse eyebrow), HP:0000653-adjacent | Multi-site involvement |

### Ocular (near-universal and often the most functionally disabling feature)
| Phenotype | HPO suggestion | Frequency |
|---|---|---|
| Photophobia | HP:0000613 | Nearly universal (though notably absent in the atypical c.1670G>A cases) |
| Meibomian gland dysfunction | HP:0100708 (Meibomian gland dysfunction) | 10/11 patients; lipidomic study (PMID: 40778116) links abnormal meibum composition directly to defective SREBP1-driven lipogenesis |
| Punctate corneal epithelial defects | HP:0008058 | Common |
| Corneal pannus / progressive corneal opacification | HP:0007957 (corneal neovascularization) | Severe cases can progress to vision loss |
| Cataract (complicated) | HP:0000518 | 9/11 patients; childhood onset |

### Onset, severity, progression
- **Onset:** Ichthyosis follicularis, photophobia, and atrichia manifest **soon after birth**; cataract, meibomian gland dysfunction, and hyperkeratotic plaques emerge **during early childhood**.
- **Severity/progression:** Variable — generally chronic and slowly progressive for skin and hair; ocular disease can progress to significant visual impairment without aggressive management. Severity does not correlate simply with genotype (identical p.Arg527Cys variant produces a range of severities; the c.1670G>A variant produces an atypical, milder-appearing but psoriasiform phenotype without photophobia).
- **Quality of life impact:** Photophobia and progressive corneal disease are frequently the most disabling features; chronic skin hyperkeratosis and alopecia carry psychosocial burden. No formal EQ-5D/SF-36 disease-specific QOL studies were identified in the literature (data gap).

## 4. Genetic/Molecular Information

- **Causal gene:** *SREBF1* (HGNC:11289; OMIM *184756*), chromosome 17p11.2, encoding sterol regulatory element-binding protein 1 (SREBP1), a basic helix-loop-helix leucine zipper (bHLH-Zip) transcription factor with two isoforms (SREBP-1a and SREBP-1c) generated by alternative promoter usage.
- **Variant classification:** All reported IFAP2 variants are missense substitutions or small in-frame deletions, clustering within a 4-amino-acid hotspot (residues 527–530) that forms the RXXL recognition motif required for site-1-protease (S1P) cleavage. Under ACMG/AMP criteria these would be classified pathogenic/likely pathogenic based on *de novo* occurrence, absence from gnomAD/ExAC, cross-species conservation, and confirmatory functional data.
- **Allele frequency:** Not present in gnomAD, ExAC, or 1000 Genomes — consistent with a highly penetrant, reproductively compatible but rare dominant disorder maintained largely by recurrent de novo mutation.
- **Functional consequences (from PMID: 32497488):**
  - In sterol-free (activating) conditions, wild-type SREBP1 is cleaved by S1P then S2P in the Golgi, releasing a 71-kD transcriptionally active nuclear fragment.
  - Transfection of HEK293 cells with the p.Arg527Cys, p.Asn528del, or p.Leu530Pro variants **abolished detection of the 71-kD cleaved nuclear fragment**.
  - Immunofluorescence showed **impaired nuclear translocation** — mutant SREBP1 signal remained cytoplasmic rather than nuclear.
  - SRE-luciferase reporter assays showed markedly reduced transcriptional activity for mutant vs. wild-type SREBP1: reduced to 33% (p.Arg527Cys), 41% (p.Asn528del), 28% (p.Leu530Pro), and 47% (p.Arg527Ala) of wild-type activity.
  - Mechanistically this is a **loss-of-function/dominant-negative** effect on S1P-mediated proteolytic activation (functional_impact_category candidates: `LOSS_OF_FUNCTION` or `DOMINANT_NEGATIVE`).
- **Downstream transcriptomic effects (RNA-seq, scalp skin, 4 affected individuals vs. controls):** 72 significantly differentially expressed genes (FDR<0.05), including:
  - **LDLR** (low-density lipoprotein receptor) — significantly downregulated in all affected individuals (classic SREBP target)
  - **SCD** (stearoyl-CoA desaturase, sebaceous-gland-enriched) — markedly reduced
  - **KRT6A, KRT6C, KRT16** (outer root sheath keratins) — significantly reduced
  - Gene-set enrichment: keratin filament, keratinization, intermediate filament cytoskeleton, epidermal cell differentiation, skin development, cornification pathways
- **Modifier genes:** None established.
- **Epigenetic information:** No disease-specific epigenetic (methylation/histone) studies identified — data gap.
- **Chromosomal abnormalities:** None reported; IFAP2 is caused by point mutation/small indel, not large structural variation.

**Suggested ontology terms:** HGNC:11289 (SREBF1); GO:0032933 (SREBP signaling pathway); GO:0016126 (sterol biosynthetic process); GO:0006695 (cholesterol biosynthetic process); GO:0045543 (regulation of fatty acid biosynthetic process).

## 5. Environmental Information

No environmental, lifestyle, or infectious contributing factors have been identified or reported for IFAP2 — it is a purely germline monogenic disorder. No gene-environment interaction data exist.

## 6. Mechanism / Pathophysiology

**Ordered causal chain:**

1. A heterozygous missense variant or small in-frame deletion in *SREBF1* (residues 527–530, or occasionally elsewhere, e.g., p.Arg557Cys, c.1670G>A) disrupts the RXXL motif required for site-1-protease (S1P) recognition of the SREBP1 precursor protein → **leads to** failure of proteolytic cleavage of SREBP1 in the Golgi.
2. Failure of S1P (and consequently S2P) cleavage **results in** retention of SREBP1 in an inactive, membrane-tethered/cytoplasmic form and loss of the transcriptionally active nuclear bHLH-Zip fragment (demonstrated directly by immunoblot/immunofluorescence in transfected cells) — this is a dominant-negative/loss-of-function mechanism, since one mutant allele suppresses net SREBP1 transcriptional output even in the presence of a normal allele.
3. Reduced nuclear SREBP1 activity **leads to** transcriptional downregulation of SREBP-target lipogenic genes (demonstrated by SRE-luciferase reporter assays showing 28–47% residual activity, and by RNA-seq showing reduced *LDLR* and *SCD* expression in patient scalp skin) → impaired cholesterol/fatty-acid biosynthesis in skin, hair follicle, and meibomian gland tissue.
4. Impaired lipogenesis in sebaceous/meibomian glands **results in** abnormal meibum lipid composition (directly documented by lipidomic analysis, PMID: 40778116), driving meibomian gland dysfunction, ocular surface lipid-layer instability, tear-film disruption, and consequent photophobia, punctate keratopathy, corneal pannus, and (via a less well-defined pathway involving chronic ocular surface inflammation) cataract formation.
5. In parallel, disrupted SREBP1 signaling in the epidermis and hair follicle **leads to** reduced expression of outer-root-sheath keratins (KRT6A, KRT6C, KRT16) and dysregulated epidermal differentiation/cornification gene programs → follicular hyperkeratosis (ichthyosis follicularis) and structurally abnormal hair shafts (trichorrhexis nodosa, seen on SEM as cuticle warping/detachment), **resulting in** hair fragility and atrichia/hypotrichosis.
6. Independently, disrupted lipid/sterol homeostasis in keratinocytes is associated with **increased in situ keratinocyte apoptosis** (demonstrated by TUNEL staining of patient scalp biopsies vs. controls), which the authors propose as an additional contributor to hyperkeratosis and hypotrichosis (this apoptosis-mediation step is explicitly noted by the authors as inferred/associative rather than mechanistically fully demonstrated).
7. In a subset of patients carrying particular variants (e.g., c.1670G>A), reduced nuclear SREBP1 translocation in lesional skin is instead associated with **enhanced IL-17A/S100A8 staining**, suggesting a branch toward a psoriasiform inflammatory phenotype rather than (or in addition to) classic follicular ichthyosis — this branch and its relationship to the canonical lipogenic-deficiency mechanism above is not yet fully resolved and represents a knowledge gap.

**Molecular pathways:** SREBP/SCAP/Insig sterol-sensing pathway (KEGG/Reactome: SREBP signaling); under sterol-replete conditions SCAP-SREBP is retained in the ER by Insig; upon sterol depletion, the SCAP-SREBP complex traffics via COPII vesicles to the Golgi where sequential S1P then S2P cleavage releases the active nuclear transcription factor — the step disrupted in IFAP2 is the S1P cleavage step (the analogous S2P step is disrupted in X-linked IFAP1/*MBTPS2*, making IFAP1 and IFAP2 mechanistically parallel/convergent disorders of the same proteolytic cascade).

**Cellular processes:** epidermal differentiation, cornification, hair follicle keratinization, sebocyte/meibocyte lipogenesis, keratinocyte apoptosis.

**Protein dysfunction:** SREBP1 loss-of-function via blocked intramembrane proteolysis (a "regulated intramembrane proteolysis," RIP, defect), analogous mechanistically to *MBTPS2*-related IFAP1/BRESHECK/keratosis follicularis spinulosa decalvans.

**Tissue damage mechanisms:** lipid-deficiency-driven barrier dysfunction (skin, meibomian gland), chronic follicular keratin plugging, oxidative/apoptotic keratinocyte stress.

**Suggested GO terms:** GO:0032933 (SREBP signaling pathway); GO:0006694 (steroid biosynthetic process); GO:0044255 (cellular lipid metabolic process); GO:0031424 (keratinization); GO:0008544 (epidermis development); GO:0006915 (apoptotic process).
**Suggested CL terms:** CL:0000312 (keratinocyte); CL:1000428 (outer root sheath cell of hair follicle, if available) or hair follicle-associated keratinocyte; CL:0002261 (sebaceous gland cell, for meibocyte-analog reasoning).

## 7. Anatomical Structures Affected

- **Organ level (primary):** Skin (epidermis, hair follicle, sebaceous apparatus) and eye (cornea, conjunctiva, meibomian glands, lens).
- **Secondary:** Nails (dystrophy); oral commissures (angular cheilitis).
- **Body systems:** Integumentary system (primary); ocular/visual system (primary); no cardiovascular, renal, or CNS involvement has been reported in IFAP2 (in contrast to *MBTPS2*-related BRESHECK syndrome, which does involve additional systems).
- **Tissue/cell level:** Follicular infundibular epithelium (keratotic plugging), outer root sheath keratinocytes, meibomian gland acinar cells, corneal epithelium, lens epithelium (cataract).
- **Subcellular:** Golgi apparatus (site of defective S1P cleavage) and nucleus (failure of SREBP1 translocation) — GO Cellular Component: GO:0005794 (Golgi apparatus), GO:0005634 (nucleus), GO:0005783 (endoplasmic reticulum, site of SCAP-SREBP1 pre-processing).
- **Localization/laterality:** Bilateral and symmetric for both cutaneous and ocular disease; the reported psoriasiform-variant plaques were bilateral but localized to extensor lower limbs.

**Suggested UBERON terms:** UBERON:0001003 (skin epidermis); UBERON:0002073 (hair follicle); UBERON:0006238 (meibomian gland); UBERON:0000964 (cornea); UBERON:0000965 (lens of camera-type eye).

## 8. Temporal Development

- **Onset:** Congenital/perinatal for the core triad (follicular ichthyosis, photophobia, atrichia); early childhood for cataract, meibomian gland dysfunction, and hyperkeratotic plaques.
- **Onset pattern:** Insidious/congenital rather than acute.
- **Progression:** Chronic, generally slowly progressive; ocular disease (corneal pannus, opacification) can progress toward significant visual impairment if unmanaged. No formal staging system exists.
- **Disease course:** Persistent/lifelong — documented survival to adulthood (mothers aged 47–48 years in the founding cohort still affected and able to have transmitted the condition to their daughters), indicating a non-lethal, chronic course, distinct from the more severe *MBTPS2*-BRESHECK spectrum.
- **Remission:** No spontaneous remission reported; symptomatic treatments (below) can partially stabilize cutaneous and corneal manifestations but do not resolve the underlying process.
- **Critical periods:** Early childhood ocular surveillance is critical given progression to cataract and corneal pannus if unmanaged.

## 9. Inheritance and Population

- **Epidemiology:** IFAP syndrome overall (both molecular subtypes combined) is exceedingly rare, with the literature describing well under 100 total published cases; IFAP2 specifically has been confirmed in a total of roughly 11–15+ published individuals across the founding cohort and subsequent case reports (2020–2025). No formal prevalence/incidence estimate (per 100,000) exists in Orphanet or GBD-type registries — data gap; prevalence_class would be best coded `ULTRA_RARE`/`NOT_YET_DOCUMENTED`.
- **Inheritance pattern:** Autosomal dominant.
- **Penetrance:** Appears complete/high in reported cases (all carriers manifest the core phenotype), though expressivity is markedly variable (e.g., presence/absence of photophobia, psoriasiform vs. classic follicular ichthyosis presentation).
- **Expressivity:** Variable, even for the identical recurrent p.Arg527Cys variant.
- **Genetic anticipation:** Not reported/applicable (not a repeat-expansion disorder).
- **Germline mosaicism:** Not specifically documented but plausible given the *de novo* mutation pattern typical of dominant disorders with this mutational mechanism; not directly studied.
- **Founder effects:** None — the founding cohort spanned Chinese, Indian, European (German, Italian, Austrian), Congolese, and African American individuals, with the p.Arg527Cys variant recurring independently across these diverse backgrounds, consistent with mutational hotspot recurrence rather than a shared ancestral founder haplotype.
- **Consanguinity:** Not implicated (dominant, not recessive, disorder).
- **Sex ratio:** The founding cohort's two multiplex families were mother-daughter pairs (both affected members female in each family), but simplex cases spanned both sexes; no formal male:female ratio has been established, and there is no known biological basis (e.g., X-linkage) for a sex skew in this autosomal dominant disorder.
- **Age distribution:** Cohort ages ranged 3–48 years at time of reporting, consistent with lifelong persistence from infancy into adulthood.

## 10. Diagnostics

- **Clinical criteria:** Recognition of the classic triad — congenital follicular ichthyosis, atrichia/hypotrichosis, and photophobia — should prompt genetic testing; the diagnosis cannot be made on clinical grounds alone given phenotypic overlap with X-linked IFAP1, BRESHECK syndrome, and hereditary mucoepithelial dysplasia (which shares a "common clinical spectrum" with IFAP per Irurzun et al., PMID referenced in search results).
- **Genetic testing:** Whole-exome sequencing (WES) is the diagnostic modality used in essentially all reported IFAP2 cases (founding cohort and subsequent case reports), given the absence of a clinically distinguishing feature that would point specifically to *SREBF1* over *MBTPS2*. Targeted Sanger sequencing of *SREBF1* (particularly the residue 527–530 hotspot) can be used for rapid confirmation/segregation testing once a proband variant is known, as performed via parental Sanger validation in the Ambarchyan et al. case. No specific gene panel name was identified in available sources; ichthyosis/genodermatosis NGS panels including *SREBF1* and *MBTPS2* would be the practical approach.
- **Biopsy/histopathology:** Scalp skin biopsy showing orthohyperkeratosis, acanthosis, dilated infundibulum filled with keratotic plugs, and perivascular lymphocytic infiltration in the superficial dermis (documented in the founding cohort's Family 1 patient).
- **Hair shaft microscopy:** Scanning electron microscopy showing cuticle warping/detachment and trichorrhexis nodosa is a useful ancillary diagnostic clue.
- **Ophthalmologic exam:** Slit-lamp evaluation for meibomian gland dysfunction, punctate corneal epithelial defects, corneal pannus, and cataract; meibum lipidomic analysis has been explored as a research tool linking the ocular phenotype directly to the molecular lesion (PMID: 40778116).
- **Differential diagnosis:** X-linked IFAP syndrome 1 (*MBTPS2*, distinguishable definitively only by molecular testing, though X-linked inheritance pattern/male predominance and more severe multisystem involvement in BRESHECK-spectrum cases are clues); hereditary mucoepithelial dysplasia; other syndromic ichthyoses (e.g., Netherton syndrome, KID syndrome); congenital atrichia with papular lesions.
- **Screening:** No population or newborn screening program exists for this ultra-rare dominant disorder; prenatal/preimplantation testing could be offered in families with a known pathogenic variant, given the dominant inheritance and documented vertical transmission.

**Suggested NCIT/LOINC/diagnostic-workflow terms:** NCIT:C15709 (Genetic Testing); a WES-based diagnostic term is most appropriate given no single confirmatory lab biomarker exists.

## 11. Outcome/Prognosis

- **Survival/mortality:** No mortality has been reported to be directly attributable to IFAP2; documented adult survivors (mothers aged 47–48 in the founding cohort) indicate a normal or near-normal life expectancy, in contrast to some MBTPS2-BRESHECK-spectrum presentations which can be more severe.
- **Morbidity:** Primarily visual (progressive corneal disease, cataract, if unmanaged) and dermatologic/psychosocial (chronic scaling, alopecia).
- **Complications:** Progressive corneal opacification and vision loss are the most significant reported complication if ocular disease is inadequately managed; recurrent corneal epithelial breakdown risks secondary infection.
- **Recovery potential:** The underlying molecular lesion is not correctable with current therapy; symptomatic treatments can improve but not normalize skin and corneal findings (see Treatment, below).
- **Prognostic factors:** No formal prognostic biomarkers have been established; phenotype severity does not clearly track with a specific variant beyond the general observation that the p.Arg527Cys hotspot variant produces a broad severity spectrum and at least one distinct variant (c.1670G>A) produces an atypical, photophobia-negative, psoriasiform-predominant course.
- **Quality-of-life data:** No disease-specific quality-of-life instrument data identified in the literature — a notable data gap for a chronic, visible, and vision-threatening condition.

## 12. Treatment

No disease-modifying or curative therapy exists; management is symptomatic and multidisciplinary (dermatology + ophthalmology), extrapolated largely from broader IFAP-syndrome and ichthyosis management literature (much of it published for IFAP1/MBTPS2 cases, but applied analogously to IFAP2):

- **Pharmacotherapy — systemic retinoids:** Oral **acitretin** (dosing reported in the range ~0.3–1 mg/kg/day) produces moderate improvement in cutaneous hyperkeratosis and corneal erosions but does **not** improve alopecia or photophobia (PMID: 16268889, and corroborated in subsequent reviews). NCIT suggestion: NCIT:C61004 (Acitretin) as `therapeutic_agent` under a `treatment_term` of NCIT:C15986 (Pharmacotherapy).
- **Topical therapy:** Emollients and keratolytics for symptomatic scale reduction; topical retinoids are generally poorly tolerated due to irritation.
- **Ocular management:** Intensive ocular surface lubrication is the mainstay for corneal protection; prophylactic topical antibiotics are used to reduce infection risk from epithelial breakdown; topical corticosteroids are generally ineffective for the corneal complications. In severe, recalcitrant corneal epithelial defects, **bilateral lateral tarsorrhaphy** has been performed (reported as early as 7 months of age in a severe case) to protect the ocular surface. NCIT suggestion: NCIT:C15329 (Surgical Procedure) for tarsorrhaphy.
- **Meibomian gland-directed therapy:** Given the mechanistic link between defective SREBP1-driven lipogenesis and abnormal meibum composition (PMID: 40778116), lid hygiene and warm compresses (standard meibomian gland dysfunction management) are a rational, though not yet formally trial-tested, adjunct.
- **Experimental/theoretical approaches:** The founding molecular paper (PMID: 32497488) proposes, as an untested theoretical strategy, **topical cholesterol or lipid supplementation** to bypass the SREBP1 lipogenic defect and stimulate hair growth/improve skin and ocular abnormalities, drawing an analogy to related lipid-synthesis-disorder case reports and mouse studies — this has not been clinically validated in IFAP2 patients and represents an open therapeutic research question.
- **No gene therapy, RNA-based therapy, cell therapy, or targeted molecular therapy** has been reported or is in clinical trials for IFAP2 specifically (searched ClinicalTrials.gov equivalent terms — none identified; this is a clinical-trial data gap consistent with the disorder's extreme rarity).
- **Supportive/rehabilitative care:** Genetic counseling is indicated given autosomal dominant inheritance and documented vertical transmission; psychosocial support for visible skin/hair differences is a reasonable component of comprehensive care, though not specifically studied in this population.

## 13. Prevention

- **Primary prevention:** Not applicable — this is a germline, largely *de novo* dominant condition with no known modifiable risk factor.
- **Secondary prevention:** Early ophthalmologic surveillance and aggressive management of corneal epithelial defects to prevent progression to vision-threatening pannus/opacification is the most actionable "secondary prevention" measure identified in the literature.
- **Genetic counseling:** Recommended for identified families given autosomal dominant inheritance, ~50% transmission risk to offspring of an affected parent, and the observed compatibility of the condition with reproduction; prenatal or preimplantation genetic testing could be offered once a familial variant is known.
- **Screening:** No population-level or newborn screening program exists.
- **Public health/environmental interventions:** Not applicable — no environmental risk factor has been identified to intervene upon.

## 14. Other Species / Natural Disease

- No naturally occurring IFAP-syndrome-like disease in non-human species (companion animals, livestock, or wildlife) has been identified in the literature searched (no OMIA entry found for an SREBF1-linked ichthyosis/atrichia/photophobia phenotype).
- **Orthologous gene:** *Srebf1* is highly conserved across vertebrates (mouse Srebf1, MGI:107606; NCBI Gene). Comparative biology relevance is limited to the conserved SREBP-SCAP-Insig sterol-sensing pathway rather than a documented natural veterinary disease counterpart.
- **Zoonotic potential:** Not applicable (non-infectious, monogenic disorder).

## 15. Model Organisms

- **Mouse:** Complete *Srebf1* germline knockout in mice causes substantial **embryonic lethality (reported ~50–85%)**, reflecting the gene's essential role in lipid metabolism during development; this severe embryonic phenotype has limited the use of full knockouts to model the human heterozygous IFAP2 phenotype, and no published mouse model specifically recapitulating the IFAP2 hotspot missense variants (p.Arg527Cys etc.) was identified in the literature searched — a clear **model-system gap** (candidate `HUMAN_MODEL_MISMATCH` consideration for future curation: no animal model has yet been shown to recapitulate the specific S1P-cleavage-resistant IFAP2 allele).
- **Related pathway models:** Tissue-specific/conditional *Srebf1* or SREBP-pathway perturbation studies exist for skin/sebaceous-gland lipid biology more broadly (e.g., glycerol kinase 5 (GK5)-mediated skin-specific regulation of SREBP processing and lipid biosynthesis, PNAS 2017) and support the general mechanistic link between SREBP signaling and epidermal/sebaceous lipogenesis invoked to explain IFAP2 pathophysiology, but these are pathway-level models, not IFAP2-specific disease models.
- **Cellular models:** The founding study's own functional work (HEK293 transfection with mutant *SREBF1* constructs) constitutes the principal "model system" evidence for IFAP2 — an *in vitro*, heterologous overexpression system demonstrating loss of S1P-mediated cleavage, nuclear translocation, and SRE-driven transcriptional activity for each of the three founding variants (PMID: 32497488). This is strong direct mechanistic evidence but is not a whole-organism/tissue-context model, and translational fidelity to intact human skin/hair-follicle/meibomian-gland biology has not been independently confirmed beyond the patient-derived scalp-skin RNA-seq and histopathology data described above.
- **Resources:** MGI:107606 (mouse *Srebf1*); International Mouse Phenotyping Consortium (IMPC) entry for *Srebf1* (mousephenotype.org) — reports embryonic-lethal/subviable status precluding standard adult phenotyping pipelines for the null allele.

---

## Summary of Key Evidence Sources

| Citation | Type | Key contribution |
|---|---|---|
| Wang X et al., *Am J Hum Genet* 2020 (PMID: [32497488](https://pmc.ncbi.nlm.nih.gov/articles/PMC7332643/)) | Human clinical + in vitro functional + transcriptomic | Founding description of *SREBF1*-related IFAP2: 11 patients, 3 hotspot variants, functional cleavage/nuclear-translocation/reporter assays, scalp RNA-seq, histopathology, TUNEL apoptosis data |
| Ambarchyan et al., *Current Pediatrics* 2024 | Human clinical case report | Novel p.Arg557Cys de novo variant in a 2-year-old girl; WES-based diagnosis |
| Zhu et al., 2025 (PMID: [39912473](https://pubmed.ncbi.nlm.nih.gov/39912473/)) | Human clinical, IHC | c.1670G>A variant causing atypical, photophobia-negative, psoriasiform-predominant phenotype; IL-17A/S100A8 immunohistochemistry |
| Zhu et al., 2025 medRxiv (PMID: [40778116](https://pubmed.ncbi.nlm.nih.gov/40778116/)) | Human clinical, lipidomics | Meibum lipid abnormality directly linked to *SREBF1* mutation/IFAP2 ocular phenotype |
| OMIM #619016 | Curated clinical synopsis/database | Canonical disease/gene identifiers and clinical synopsis |
| PMID: 16268889 | Human clinical (IFAP syndrome, not variant-specified) | Acitretin treatment response data |

**Notable data gaps for KB curation:** no formal prevalence estimate; no IFAP2-specific animal model; no disease-specific quality-of-life instrument data; no completed or ongoing clinical trials (NCT) specific to IFAP2; mechanistic link between the apoptosis finding and hyperkeratosis/hypotrichosis phenotype is explicitly stated by the primary authors as associative rather than causally demonstrated; the c.1670G>A "atypical/psoriasiform" phenotype's relationship to the canonical lipogenic-deficiency mechanism is unresolved and would be a good candidate for a `HUMAN_MODEL_MISMATCH`/knowledge-gap discussion node if curated into dismech.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 5 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 45 |
| Resolved | 41 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 2 |
| Terms whose name was checked | 38 |
| Terms named correctly | 20 |
| Terms named as a **different** term | 13 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0007431` (2 mentions) - the report calls it "Lamellar-ichthyosis-like scaling (alternative presentation)"; HP calls it **Congenital ichthyosiform erythroderma**
- `HP:0100025` (1 mention) - the report calls it "angular cheilitis"; HP calls it **Overfriendliness**
- `HP:0002298` (1 mention) - the report calls it "atrichia"; HP calls it **Absent hair**
- `HP:0000966` (1 mention) - the report calls it "Moderate–severe hypotrichosis (sparse, thin hair)"; HP calls it **Hypohidrosis**
- `HP:0011364` (1 mention) - the report calls it "hair shaft abnormality"; HP calls it **White hair**
- `HP:0012207` (1 mention) - the report calls it "Trichorrhexis nodosa (hair shaft defect on SEM)"; HP calls it **Reduced sperm motility**
- `HP:0100708` (1 mention) - the report calls it "Meibomian gland dysfunction"; HP calls it **Abnormal microglia morphology**
- `HP:0008058` (1 mention) - the report calls it "Punctate corneal epithelial defects"; HP calls it **Aplasia/Hypoplasia of the optic nerve**
- `GO:0045543` (1 mention) - the report calls it "regulation of fatty acid biosynthetic process"; GO calls it **gibberellin 2-beta-dioxygenase activity**
- `CL:1000428` (1 mention) - the report calls it "outer root sheath cell of hair follicle, if available"; CL calls it **stem cell of epidermis**
- `CL:0002261` (1 mention) - the report calls it "sebaceous gland cell, for meibocyte-analog reasoning"; CL calls it **endothelial cell of viscerocranial mucosa**
- `UBERON:0006238` (1 mention) - the report calls it "meibomian gland"; UBERON calls it **future brain**
- `NCIT:C61004` (1 mention) - the report calls it "Acitretin"; NCIT calls it **Tablet for Solution Dosage Form**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0100637` (obsolete Neoplasia of the nose) (1 mention) - replaced by `HP:0012720`
- `GO:0044255` (obsolete cellular lipid metabolic process) (1 mention) - replaced by `GO:0006629`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0100212` (1 mention) - the report calls it "IFAP syndrome, general"; MONDO calls it **IFAP syndrome**
- `HP:0007957` (1 mention) - the report calls it "corneal neovascularization"; HP calls it **Corneal opacity**, and lists "Corneal opacities" among its other names
- `HP:0000518` (1 mention) - the report calls it "Cataract (complicated)"; HP calls it **Cataract**
- `GO:0044255` (1 mention) - the report calls it "cellular lipid metabolic process"; GO calls it **obsolete cellular lipid metabolic process**
- `GO:0005783` (1 mention) - the report calls it "endoplasmic reticulum, site of SCAP-SREBP1 pre-processing"; GO calls it **endoplasmic reticulum**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`.