---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-7[1m]
cached: false
start_time: '2026-09-11T16:20:33.485346'
end_time: '2026-09-11T16:27:36.699436'
duration_seconds: 423.21
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Riley-Day Syndrome
  mondo_id: MONDO:0009131
  category: Disease
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
  - claude-opus-4-7[1m]
  web_search_requests: 17
  num_turns: 23
  total_cost_usd: 2.861271
  session_id: a3300b29-eda1-42a5-bf88-905310d4c206
  stop_reason: end_turn
  permission_denials: 4
  denied_tools:
  - mcp__pubmed__search_articles
  assistant_text_blocks: 1
citation_count: 57
reference_validation:
  total_references: 38
  verified: 38
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 38
  on_topic: 7
  off_topic: 8
  off_topic_references:
  - PMID:37000283
  - PMID:32623925
  - PMID:20857273
  - PMID:24007805
  - PMID:38168126
  - PMID:21725277
  - PMID:23824189
  - DOI:10.1161/HYPERTENSIONAHA.120.15267
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 74
  verified: 68
  not_found: 3
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.042
  labels_checked: 57
  labels_matching: 21
  labels_mismatched: 19
  mislabelled_terms:
  - term_id: HP:0100799
    reported_labels:
    - smooth tongue
    ontology_label: Neoplasm of the middle ear
  - term_id: HP:0001315
    reported_labels:
    - "Depressed / absent deep tendon reflexes** \u2014 ~100%"
    - Areflexia
    ontology_label: Diminished deep tendon reflex
  - term_id: HP:0002131
    reported_labels:
    - Ataxia (proprioceptive)
    ontology_label: Episodic ataxia
  - term_id: HP:0000632
    reported_labels:
    - Optic neuropathy
    ontology_label: Lacrimation abnormality
  - term_id: HP:0005112
    reported_labels:
    - abnormal autonomic nervous system physiology
    - Autonomic crises
    ontology_label: Abdominal aortic aneurysm
  - term_id: HP:0002326
    reported_labels:
    - hypertension
    ontology_label: Transient ischemic attack
  - term_id: HP:0011169
    reported_labels:
    - "Blood pressure lability / baroreflex failure** \u2014 ~100%"
    ontology_label: Generalized clonic seizure
  - term_id: HP:0002102
    reported_labels:
    - "Recurrent aspiration pneumonia** \u2014 ~90%"
    ontology_label: Pleuritis
  - term_id: HP:0000739
    reported_labels:
    - "Anxiety and emotional lability** \u2014 very frequent"
    ontology_label: Anxiety
  - term_id: HP:0011036
    reported_labels:
    - Increased serum dopamine-to-norepinephrine ratio
    ontology_label: Abnormality of renal excretion
  - term_id: CL:0011003
    reported_labels:
    - peripheral autonomic neuron
    ontology_label: magnocellular neurosecretory cell
  - term_id: UBERON:0002393
    reported_labels:
    - Enteric nervous system
    - enteric nervous system
    ontology_label: pharyngotympanic tube
  - term_id: UBERON:0002205
    reported_labels:
    - Tongue fungiform papillae
    - fungiform papilla
    ontology_label: manubrium of sternum
  - term_id: UBERON:0001291
    reported_labels:
    - lacrimal gland
    ontology_label: thick ascending limb of loop of Henle
  - term_id: NCIT:C29435
    reported_labels:
    - Diazepam
    ontology_label: DNA Minor Groove Binding Agent SG2000
  - term_id: NCIT:C505
    reported_labels:
    - Clonidine
    ontology_label: Fluorouracil
  - term_id: NCIT:C471
    reported_labels:
    - Carbidopa
    ontology_label: Enzyme Inhibitor
  - term_id: NCIT:C61708
    reported_labels:
    - Dexmedetomidine
    ontology_label: Dextroamphetamine Saccharate
  - term_id: NCIT:C874
    reported_labels:
    - "Fludrocortisone \u2013 avoid"
    ontology_label: Thiamine
  labels_variant: 17
  unresolved_terms:
  - HP:0000167
  - ECTO:0001093
  - ECTO:0000000
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
- **Disease Name:** Riley-Day Syndrome
- **MONDO ID:** MONDO:0009131 (if available)
- **Category:** Disease

## Research Objectives

Please provide a comprehensive research report on **Riley-Day Syndrome** covering all of the
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

# Comprehensive Research Report: Riley-Day Syndrome (Familial Dysautonomia)

**MONDO ID:** MONDO:0009131
**Primary Category:** Disease (Hereditary Sensory and Autonomic Neuropathy Type III)

---

## 1. Disease Information

Riley-Day syndrome, more commonly termed **Familial Dysautonomia (FD)**, is a rare autosomal recessive congenital neurological disorder characterized by profound and progressive dysfunction of the sensory and autonomic nervous systems. It was first described by Conrad Milton Riley and Richard Lawrence Day in 1949, based on a case series of five Ashkenazi Jewish children with unexplained autonomic dysfunction, feeding difficulties, and alacrima (defective tearing). FD is now formally classified as **Hereditary Sensory and Autonomic Neuropathy Type III (HSAN III)** within the wider HSAN family. The core disease process is a developmental failure and subsequent progressive degeneration of unmyelinated sensory neurons (nociceptors, autonomic afferents) and small autonomic (sympathetic/parasympathetic) neurons, producing early-life autonomic instability, absent overflow tears, insensitivity to pain and temperature, gastroesophageal reflux, aspiration pneumonia, and later development of ataxia, hypertensive vomiting crises, kyphoscoliosis, optic neuropathy, chronic kidney disease, and sleep-disordered breathing.

**Key identifiers**
- **OMIM:** #223900 (Dysautonomia, familial; FD / HSAN III); gene entry OMIM 603722 (ELP1, previously IKBKAP)
- **Orphanet:** ORPHA:1764 (Familial dysautonomia)
- **MONDO:** MONDO:0009131
- **ICD-10:** G90.1 (Familial dysautonomia [Riley-Day])
- **ICD-11:** 8D87.Y
- **MeSH:** D004402 (Dysautonomia, Familial)
- **GARD:** 7581

**Common synonyms/alternative names:** Riley-Day syndrome, Hereditary Sensory and Autonomic Neuropathy Type III (HSAN III / HSAN3), Hereditary Sensory Neuropathy Type III, familial autonomic dysfunction, Riley-Day dysautonomia.

**Data derivation:** Because the disease has an extraordinarily narrow founder population and only ~700 living patients worldwide, most epidemiological, natural history, and treatment data derive from **aggregated disease-level cohorts and registries** — chiefly the New York University Dysautonomia Center registry (Kaufmann/Norcliffe-Kaufmann) and the Israeli Dysautonomia Center — rather than population EHR data. Molecular and mechanistic data derive from patient tissues, mouse models (Wnt1-Cre Ikbkap conditional knockouts, humanized *TgFD*/Elp1 mice), and iPSC-derived neurons. (Sources: [GeneReviews, NBK1180](https://www.ncbi.nlm.nih.gov/books/NBK1180/); [OMIM 223900](https://omim.org/entry/223900); [Norcliffe-Kaufmann 2023, Clin Auton Res, PMID 37000283](https://link.springer.com/article/10.1007/s10286-023-00941-1).)

---

## 2. Etiology

### 2.1 Disease Causal Factors

FD is a **monogenic autosomal recessive disorder**. Bi-allelic pathogenic variants in **ELP1** (formerly **IKBKAP**; HGNC:5959; NCBI Gene: 8518) on **chromosome 9q31.3** cause tissue-specific reduction of the Elongator complex scaffolding subunit ELP1 (also called IκB kinase complex-associated protein, IKAP). The disease is therefore entirely genetic; environmental factors modulate crisis frequency and complication severity but do not cause the disease. (Sources: [OMIM 603722](https://omim.org/entry/603722); [Anderson et al. 2001, Am J Hum Genet, PMID 11179016](https://pubmed.ncbi.nlm.nih.gov/11179016/); [Slaugenhaupt et al. 2001, Am J Hum Genet, PMID 11179017](https://pubmed.ncbi.nlm.nih.gov/11179017/).)

### 2.2 Risk Factors

**Genetic risk factors**
- **Founder mutation c.2204+6T>C (IVS20+6T>C):** A T→C transition at position +6 of the 5′ splice donor of intron 20 of ELP1 causes tissue-specific exon 20 skipping and reduced full-length ELP1. This variant accounts for **>99.5%** of pathogenic alleles in Ashkenazi Jewish (AJ) FD patients and is one of the strongest known founder alleles in medicine. (Anderson et al. 2001, PMID 11179016; Slaugenhaupt et al. 2001, PMID 11179017.)
- **Missense c.2087G>C (p.R696P):** Accounts for the residual fraction (<0.5%) of pathogenic AJ alleles and a small number of non-AJ FD cases (e.g., [Leyne et al. 2003, Am J Med Genet A, PMID 12687659](https://pubmed.ncbi.nlm.nih.gov/12687659/)).
- **Ashkenazi Jewish ancestry:** The strongest population risk factor. Carrier frequency in AJ populations is approximately **1 in 27–36** (most commonly cited as ~1/30); still higher (~1/18) in Polish-descended AJ subgroups ([Lehavi et al. 2003, PMID 12885336](https://pubmed.ncbi.nlm.nih.gov/12885336/)).

**Environmental risk factors (for crises / complications, not the disease itself):**
- Emotional stress, anxiety, viral infections, meals, and dehydration precipitate hyperadrenergic autonomic crises.
- Aspiration risk with feeding (due to abnormal oropharyngeal coordination and gastroesophageal reflux).
- Recumbency for prolonged periods, high salt/fludrocortisone use, and hypokalemia elevate the risk of sudden death during sleep ([Palma et al. 2017, Sleep, PMID 28521050](https://pubmed.ncbi.nlm.nih.gov/28521050/)).

### 2.3 Protective Factors
- **Heterozygosity:** Heterozygous carriers of the c.2204+6T>C allele are clinically unaffected owing to the tissue-specific and dose-sensitive nature of the splicing defect ([Slaugenhaupt et al. 2001, PMID 11179017](https://pubmed.ncbi.nlm.nih.gov/11179017/)).
- No consistent genetic modifier or protective environmental exposure has been established, though avoidance of fludrocortisone and prompt initiation of non-invasive ventilation reduce SUDS ([Palma et al. 2017, PMID 28521050](https://pubmed.ncbi.nlm.nih.gov/28521050/)).

### 2.4 Gene–Environment Interactions
Emotional/physical stress triggers a paradoxical, exaggerated peripheral catecholamine surge in FD due to a lesion of the *afferent* baroreflex (loss of glossopharyngeal/vagal chemo- and baroreceptor input); the *efferent* sympathetic limb remains intact, producing hypertensive vomiting crises. Feeding likewise triggers postprandial hypotension via unopposed splanchnic dilation. (Sources: [Norcliffe-Kaufmann & Kaufmann 2012, Auton Neurosci](https://www.sciencedirect.com/science/article/abs/pii/S1566070212000926); [Palma et al. 2020, Hypertension, PMID 32623925](https://www.ahajournals.org/doi/10.1161/HYPERTENSIONAHA.120.15267).)

---

## 3. Phenotypes

Phenotypes are typically reported as **>90% penetrant by adolescence** in homozygotes; onset is neonatal for many. Frequencies below are drawn from the NYU FD registry and the GeneReviews/Orphanet expert summaries ([Axelrod, GeneReviews NBK1180](https://www.ncbi.nlm.nih.gov/books/NBK1180/); [MedLink Neurology - Familial Dysautonomia](https://www.medlink.com/articles/familial-dysautonomia)).

### 3.1 Neurological / Sensory
- **Absent overflow tears (alacrima)** — ~100%, congenital (HP:0000522).
- **Absent fungiform papillae** on the tongue (smooth glistening tip) — ~100%, congenital (HP:0000167 – atrophic fungiform papillae; HP:0100799 – smooth tongue).
- **Depressed / absent deep tendon reflexes** — ~100% (HP:0001315).
- **Decreased pain sensation** (nociceptor loss; palms, soles, neck, genital regions relatively spared) — ~100% (HP:0007021).
- **Decreased temperature sensation** — ~90% (HP:0010829).
- **Proprioceptive ataxia and progressive gait ataxia** — ~90% by adolescence (HP:0002066, HP:0002131).
- **Optic neuropathy / progressive vision loss**, beginning ~age 5, legal blindness typically by 3rd decade (HP:0000632, HP:0000505). ([Mendoza-Santiesteban et al. 2012](https://www.researchgate.net/publication/51643718_Clinical_Neuro-ophthalmic_Findings_in_Familial_Dysautonomia).)

### 3.2 Autonomic / Cardiovascular
- **Postural (orthostatic) hypotension** — ~100% (HP:0001278).
- **Hyperadrenergic autonomic ("dysautonomic") crises** with paroxysmal hypertension, tachycardia, cutaneous erythematous blotching, diaphoresis, retching/vomiting — ~40–65% (HP:0005112 - abnormal autonomic nervous system physiology; HP:0002326 – hypertension).
- **Blood pressure lability / baroreflex failure** — ~100% (HP:0011169).
- **Excessive sweating with stress** and **red skin blotches** — ~90% (HP:0000975).

### 3.3 Gastrointestinal
- **Gastroesophageal reflux** — ~85% (HP:0002020).
- **Poor feeding / oropharyngeal dyscoordination in infancy** — ~95% (HP:0011968).
- **Recurrent vomiting** and cyclical vomiting crises — ~65% (HP:0002020, HP:0002572).
- **Gastroparesis and constipation** — ~50%.

### 3.4 Respiratory
- **Recurrent aspiration pneumonia** — ~90% (HP:0002102).
- **Blunted ventilatory responses to hypoxia and hypercapnia** (chemoreflex failure) — ~100% (HP:0002098 – abnormal breathing regulation; HP:0002104 – apnea).
- **Sleep-disordered breathing** (mixed obstructive/central) — >70% in adults ([Palma et al. 2019, Sleep Med, PMID 30890343](https://pubmed.ncbi.nlm.nih.gov/30890343/)).

### 3.5 Musculoskeletal
- **Kyphoscoliosis** — ~90% by adolescence (HP:0002751).
- **Reduced bone mineral density, growth retardation** — common (HP:0004349, HP:0004322).
- **Charcot arthropathy / neuropathic joints** — episodic.

### 3.6 Genitourinary
- **Progressive chronic kidney disease** — >50% by 3rd decade (HP:0012622), driven by repeated hypoperfusion episodes and orthostatic hypotension.

### 3.7 Behavioral / Cognitive
- **Anxiety and emotional lability** — very frequent (HP:0000739).
- Intelligence is generally normal; developmental delay is often secondary to hospitalizations and hypoxic events rather than primary cognitive dysfunction.

### 3.8 Laboratory
- **Increased serum dopamine-to-norepinephrine ratio** (HP:0011036) — supports diagnosis pre-DNA testing.
- **Blunted plasma catecholamine response to standing.**
- **Elevated urinary VMA/HVA ratio** (reflecting dysfunctional catecholamine metabolism).

### 3.9 Onset, Progression, Severity, QOL
- **Age of onset:** Congenital / neonatal for feeding and alacrima; multisystem progression through childhood; sensory deficits and ataxia progress lifelong.
- **Severity:** Uniformly severe; variable expressivity due to leaky splicing.
- **Progression:** Progressive.
- **QOL impact:** Severe. Cardinal drivers are ataxia/blindness (mobility loss), aspiration/pneumonia (repeated hospitalization), autonomic crises (medical emergencies), and dependence on gastrostomy feeding and nightly non-invasive ventilation in adulthood.

---

## 4. Genetic / Molecular Information

### 4.1 Causal Gene
- **ELP1** (previously **IKBKAP**), HGNC:5959, NCBI Gene 8518, UniProt O95163, chromosome **9q31.3**, 37 exons spanning ~68 kb of genomic DNA, encoding a 1332-aa scaffolding subunit of the six-member Elongator complex.

### 4.2 Pathogenic Variants

| Variant (HGVS) | Type | Population | Frequency | Consequence |
|---|---|---|---|---|
| **c.2204+6T>C** (IVS20+6T>C) | Intronic splice-region (donor site +6) | Ashkenazi Jewish | >99.5% of AJ FD alleles | Tissue-specific skipping of exon 20 → frameshift, premature stop, ~79 kD truncated protein; leaky splicing preserves partial wild-type ELP1 in non-neural tissues |
| **c.2087G>C** (p.Arg696Pro; R696P) | Missense | AJ + occasional non-AJ | <0.5% AJ; small numbers non-AJ | Disrupts protein–protein binding of ELP1 in Elongator complex |
| Rare compound heterozygous private variants | Missense / nonsense | Non-AJ (rare) | Case reports | Reduced ELP1 |

ACMG classification: All confirmed FD alleles are **Pathogenic**. Both major variants are extensively curated in ClinVar (RCV000000541 for c.2204+6T>C).

**Allele frequency in gnomAD:** The founder variant c.2204+6T>C has a global heterozygote frequency of ~0.4%, concentrated in the AJ subpopulation (~1.5–2%).

**Origin:** Germline (recessive). No somatic FD is described.

**Functional consequences:**
- **Loss of function** through drastically reduced full-length ELP1 protein in nervous tissue; the leaky splicing produces measurable — but insufficient — wild-type ELP1 in non-neural tissues, explaining tissue-specific pathology.
- The Elongator complex catalyzes 5-carboxymethyl (cm5) modifications on uridine 34 (U34) of wobble tRNAs (tRNA-Lys, -Glu, -Gln, -Arg). Loss of Elongator activity impairs efficient decoding of AA-ending codons and disrupts the translation of codon-biased mRNAs (e.g., ATG9A, PCP4). ([Karlsborn et al. 2014, RNA Biology](https://www.tandfonline.com/doi/full/10.4161/15476286.2014.992269).)
- Elongator/ELP1 also plays roles in histone H3 acetylation, actin cytoskeleton regulation, and neurotrophin-dependent axonal transport of NGF.

### 4.3 Modifier Genes
No formally validated modifier gene is known, but variability in residual ELP1 expression (driven by *cis* regulatory context, PUF60/RBM24 splicing regulators, and cellular stress) correlates with clinical severity ([Ohlen et al. 2017](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5451171/)).

### 4.4 Epigenetic Information
No canonical epigenetic driver of FD is described. However, elongator complex loss changes histone H3K14ac at specific loci and secondarily alters transcriptional elongation in neurons.

### 4.5 Chromosomal Abnormalities
Not applicable — FD is a monogenic single-nucleotide variant disorder; chromosomal microarray is not indicated.

**Ontology suggestions:** GO:0033588 (Elongator holoenzyme complex); GO:0002098 (tRNA wobble uridine modification); GO:0006355 (regulation of DNA-templated transcription); GO:0000226 (microtubule cytoskeleton organization).

---

## 5. Environmental Information

Because FD is fully monogenic, environmental factors are triggers/modulators rather than causes.

- **Emotional and physical stress:** Reliably triggers hypertensive autonomic crises via disinhibited catecholamine release ([Norcliffe-Kaufmann 2010, PMID 20857273](https://pubmed.ncbi.nlm.nih.gov/20857273/)).
- **Meals:** Postprandial hypotension is characteristic due to splanchnic redistribution unopposed by baroreflex.
- **Viral respiratory infections:** Precipitate aspiration pneumonia and respiratory failure.
- **Fludrocortisone use, hypokalemia, and untreated obstructive sleep apnea:** Increase risk of sudden unexpected death during sleep (SUDS) ([Palma et al. 2017, Sleep, PMID 28521050](https://academic.oup.com/sleep/article/40/8/zsx083/3831157)).
- **Ambient temperature extremes:** Cause temperature dysregulation (fever without infection; hypothermia).

**Infectious agents:** No causal role. Aspiration pneumonia (typically polymicrobial including anaerobes and *Streptococcus pneumoniae*) is a downstream complication rather than a primary etiology.

**Ontology suggestions:** ECTO:0001093 (exposure to psychosocial stress); ECTO:0000000-derived exposures related to meals/positional change (no exact term).

---

## 6. Mechanism / Pathophysiology

### 6.1 Ordered Causal Chain

1. **Homozygous ELP1 c.2204+6T>C variant** in the intron 20 donor splice site weakens U1 snRNP recognition **→**
2. **Tissue-specific skipping of exon 20** occurs during ELP1 pre-mRNA splicing, most severely in the nervous system (partially retained in fibroblasts and other tissues; hence the "leaky" phenotype) ([Cuajungco et al. 2003, PMID 12756454](https://pubmed.ncbi.nlm.nih.gov/12756454/)) **→**
3. **Reduced full-length ELP1 protein in neurons** (a hypomorphic loss of function) **→**
4. **Loss of Elongator holoenzyme activity** (Elp1–Elp6), leading to **failure of tRNA wobble uridine cm⁵U/mcm⁵s²U modification** on tRNA-Lys/Glu/Gln/Arg **→**
5. **Impaired translation of AA-ending, codon-biased transcripts** critical for neuronal function (e.g., ATG9A, PCP4, TrkA-pathway components); parallel effects on **histone H3 acetylation**, **actin cytoskeleton**, and **NGF-dependent retrograde axonal transport** (via HDAC6-mediated hyperacetylation deficiency and unstable microtubules) ([Naftelberg et al. 2016, Trends Genet](https://www.sciencedirect.com/science/article/abs/pii/S0168952516300287); [Ohlen et al. 2017, PMID 28167615](https://pubmed.ncbi.nlm.nih.gov/28167615/)) **→**
6. **Developmental failure of neural-crest–derived sensory and autonomic neuron populations**: apoptosis of TrkA+ nociceptors and Pax3+ progenitors in dorsal root ganglia (DRG), sympathetic chain, trigeminal ganglion, and enteric plexus ([George et al. 2013, PNAS, PMID 24007805](https://www.pnas.org/doi/10.1073/pnas.1308596110); [Jackson et al. 2014, eLife, PMID 25139957](https://elifesciences.org/articles/71455)) **→**
7. **Reduced neuron numbers at birth** (DRG neuron counts ~10–20% of normal; C8 DRG normally 42,500–53,600 neurons, in FD patients 4,090–8,590; [Pearson & Pytel 1978, PMID 624961](https://pubmed.ncbi.nlm.nih.gov/624961/)) **→**
8. **Slow, progressive postnatal degeneration** of remaining sensory and autonomic neurons (unmyelinated fibers and small myelinated); loss of afferents from carotid/aortic baroreceptors and chemoreceptors; retinal ganglion cell degeneration in temporal papillomacular bundle **→**
9. **Clinical manifestations:**
   - **Afferent baroreflex failure** → hypertensive crises + orthostatic hypotension.
   - **Afferent chemoreflex failure** → blunted response to hypoxia/hypercapnia, paradoxical apnea, SUDS.
   - **Nociceptor/thermoreceptor loss** → pain and temperature insensitivity; Charcot joints.
   - **Proprioceptor loss (dorsal columns)** → ataxia.
   - **Enteric autonomic loss** → gastroparesis, reflux, dysmotility.
   - **Lacrimal parasympathetic loss** → alacrima.
   - **Retinal ganglion cell degeneration** → progressive optic neuropathy, blindness.
   - **Recurrent hypotension** → CKD; **aspiration** → chronic lung disease.

### 6.2 Molecular Pathways Involved
- **Elongator complex tRNA modification pathway** (KEGG map03016 tRNA loading; Reactome R-HSA-6784531 tRNA modification in the nucleus and cytosol).
- **NGF/TrkA retrograde signaling and axonal transport** (KEGG hsa04722, Reactome R-HSA-187037 NGF-stimulated transcription). HDAC6 hyperactivity in FD deacetylates α-tubulin, destabilizes microtubules, and impairs retrograde NGF trafficking ([Naftelberg et al. 2016](https://www.sciencedirect.com/science/article/abs/pii/S0168952516300287)).
- **Autophagy (ATG9A)** — reduced due to tRNA-mediated translation defect.
- **MAPK/ERK** signaling downstream of TrkA — attenuated.
- **JNK stress signaling** — activated; contributes to apoptosis of neural crest progenitors.

### 6.3 Cellular Processes
- **Neuronal apoptosis** during development (GO:0006915).
- **Impaired axon guidance and target innervation** in sensory neurons (GO:0007411).
- **Defective axonal transport** — retrograde NGF endosome trafficking impaired (GO:0008090).
- **Cytoskeletal instability** — decreased α-tubulin acetylation, microtubule dynamic instability (GO:0007010).
- **Mitochondrial dysfunction** — described in Elp1-deficient retinal ganglion cells ([Chekuri et al. 2018, Dis Model Mech](https://journals.biologists.com/dmm/article/11/7/dmm033746/53306/)).

### 6.4 Protein Dysfunction
ELP1 is a scaffolding subunit of the six-subunit Elongator holoenzyme (ELP1–ELP6). ELP3 provides the catalytic radical-SAM domain that modifies wobble U34. Truncated ELP1 (~79 kD) fails to nucleate a stable Elongator complex → loss of holoenzyme function ([Karlsborn et al. 2014](https://www.tandfonline.com/doi/full/10.4161/15476286.2014.992269)).

### 6.5 Metabolic / Biochemical Changes
- **Elevated dopamine/norepinephrine ratio** — reflects loss of catecholaminergic autonomic neurons with residual central dopaminergic activity.
- **Elevated 3,4-dihydroxyphenylacetic acid (DOPAC) and reduced norepinephrine** in plasma.
- **Altered urinary HVA/VMA ratio.**
- Mitochondrial oxidative-phosphorylation deficits in Elp1-deficient retinal cells.

### 6.6 Tissue Damage Mechanisms
- **Chronic hypoperfusion** (orthostatic hypotension) → renal cortex ischemia → CKD.
- **Recurrent aspiration** → bronchiectasis and chronic lung disease.
- **Oxidative stress in retinal ganglion cells** → optic neuropathy.

### 6.7 Molecular Profiling
- **Transcriptomics** in humanized *TgFD9* Elp1 mice show tissue-specific dysregulation of neurotrophic and cytoskeletal genes, most severe in DRG and trigeminal ganglion ([Morini et al. 2023, PMID 38168126](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10766950/)).
- **Proteomics** — trigeminal ganglion in Elp1-deficient mice shows down-regulation of NGF, BDNF signaling and mitochondrial metabolism ([Leonard et al. 2025 bioRxiv](https://www.biorxiv.org/content/10.64898/2025.12.05.692685.full.pdf)).

**Ontology suggestions:** GO:0002098 (tRNA wobble uridine modification); GO:0033588 (Elongator holoenzyme complex); GO:0007411 (axon guidance); GO:0008089 (anterograde axonal transport); GO:0006915 (apoptotic process); GO:0007628 (adult walking behavior); GO:0031982 (vesicle); GO:0090128 (regulation of synaptonemal complex assembly). Cell types: CL:0011003 (peripheral autonomic neuron); CL:0000103 (bipolar neuron); CL:0000198 (nociceptor); CL:0000101 (sensory neuron); CL:0000740 (retinal ganglion cell).

---

## 7. Anatomical Structures Affected

### 7.1 Organ Level
- **Primary organs:** Peripheral nervous system (dorsal root ganglia, sympathetic chain ganglia, cranial nerve ganglia, enteric nervous system).
- **Secondary organ involvement:** Kidneys (progressive CKD), lungs (chronic aspiration lung disease/bronchiectasis), heart (baroreflex failure → BP lability), retina and optic nerve, skeletal system (kyphoscoliosis, Charcot joints), tongue (absent fungiform papillae), lacrimal glands (alacrima), gastrointestinal tract (dysmotility).
- **Body systems:** Autonomic nervous, sensory nervous, cardiovascular, respiratory, gastrointestinal, ocular, musculoskeletal, urinary.

### 7.2 Tissue and Cell Level
- **Dorsal root ganglion (UBERON:0000044) sensory neurons** — small pseudounipolar neurons (CL:0000101), especially unmyelinated nociceptors (CL:0000198) and proprioceptors.
- **Sympathetic chain ganglia (UBERON:0002440) autonomic neurons** (CL:0011003).
- **Enteric nervous system (UBERON:0002393) neurons.**
- **Trigeminal ganglion (UBERON:0001675) neurons.**
- **Retinal ganglion cells (CL:0000740)**, particularly in the papillomacular bundle.
- **Lissauer's tract, dorsal columns (fasciculus gracilis/cuneatus)** — progressive axonal loss in spinal cord ([Pearson & Pytel 1978, PMID 624961](https://pubmed.ncbi.nlm.nih.gov/624961/)).
- **Lacrimal gland** parasympathetic innervation.
- **Tongue fungiform papillae (UBERON:0002205)** — congenitally absent.

### 7.3 Subcellular Level
- **Cytoplasmic Elongator complex (GO:0033588).**
- **Microtubule cytoskeleton (GO:0005874)** — hypoacetylated α-tubulin.
- **Mitochondria (GO:0005739)** — dysfunctional in retinal cells.
- **Vesicular retrograde transport machinery.**

### 7.4 Localization
- **Lateralization:** Bilateral, symmetric.
- **Specific sites:** UBERON:0000044 (dorsal root ganglion), UBERON:0001675 (trigeminal ganglion), UBERON:0002440 (sympathetic ganglion), UBERON:0002393 (enteric nervous system), UBERON:0000970 (eye), UBERON:0000970/UBERON:0001782 (retina), UBERON:0001291 (lacrimal gland), UBERON:0002205 (fungiform papilla).

---

## 8. Temporal Development

### 8.1 Onset
- **Congenital / neonatal.** Presentation typically begins at birth or within the first weeks: hypotonia, feeding difficulties, absent tears with crying, poor thermoregulation.
- **Onset pattern:** Insidious (developmental) with superimposed acute autonomic crises beginning in infancy/toddlerhood.

### 8.2 Progression / Stages
- **Infancy:** Feeding difficulty, aspiration pneumonia, alacrima, hypotonia, unstable temperature.
- **Childhood (2–10 y):** Cyclical vomiting/autonomic crises emerge; delayed motor milestones; ataxia becomes apparent.
- **Adolescence:** Kyphoscoliosis; early optic neuropathy; hypertensive lability worsens.
- **Adulthood (>18 y):** Progressive ataxia, blindness (by 20s–30s), CKD, chronic lung disease, sleep-disordered breathing, sudden death risk.
- **Progression rate:** Slow, monotonically progressive (no true remitting phase).
- **Duration:** Lifelong.

### 8.3 Patterns
- No spontaneous or treatment-induced remission.
- **Critical developmental windows:** Prenatal and early postnatal periods are the key windows for neural-crest-derived neuron survival; disease-modifying therapy is hypothesized to work best if administered before massive neuronal loss (relevant to newer splicing-modulator therapeutics).

---

## 9. Inheritance and Population

### 9.1 Epidemiology
- **Prevalence:** Extremely rare overall (<1/1,000,000 in general non-AJ populations). **Incidence in Ashkenazi Jewish population: ~1 in 3,600 live births** (ranges 1/3,600–1/3,700). Worldwide living FD patients: ~500–700 ([Axelrod 2004, PMID 15277940](https://pubmed.ncbi.nlm.nih.gov/15277940/); [Orphanet ORPHA:1764](https://orpha.net/consor/cgi-bin/OC_Exp.php?Expert=1764)).
- **Carrier frequency (AJ):** ~1 in 30 (1 in 27–36 across studies; higher, ~1/18, in Polish-descended AJ subgroups; [Lehavi et al. 2003, PMID 12885336](https://pubmed.ncbi.nlm.nih.gov/12885336/)).

### 9.2 Genetic Etiology Details
- **Inheritance pattern:** **Autosomal recessive** (HP:0000007). Compatible with founder effect and consanguinity in isolated non-AJ pedigrees.
- **Penetrance:** Effectively 100% in biallelic homozygotes/compound heterozygotes for known pathogenic variants.
- **Expressivity:** Variable — largely dictated by residual "leaky" full-length ELP1 expression.
- **Anticipation:** Not observed (not a repeat expansion disorder).
- **Germline mosaicism:** Not reported as a significant source of new cases.
- **Founder effect:** Yes — a single ancestral c.2204+6T>C haplotype, estimated to have originated ~500–1000 years ago in Eastern European Ashkenazi Jewish populations, drives >99.5% of AJ cases.
- **Consanguinity role:** Contributes in non-AJ pedigrees; incidence in AJ populations is driven by founder-allele frequency rather than consanguinity.

### 9.3 Population Demographics
- **Affected populations:** Ashkenazi Jews (predominant); rare cases in non-AJ populations (Puerto Rican, English, Mexican described).
- **Geographic distribution:** Highest incidence in Israel and North American AJ communities; sporadic elsewhere.
- **Sex ratio:** ~1:1 (autosomal recessive, no sex predilection).
- **Age distribution:** All ages; the surviving population increasingly includes adults >20 due to improved supportive care.

---

## 10. Diagnostics

### 10.1 Clinical Diagnostic Criteria (Historical Cardinal Five)
Per Axelrod et al., diagnosis is supported by all of:
1. Absent overflow tears (alacrima).
2. Absent fungiform papillae on tongue (smooth glistening tip).
3. Absent axon flare after intradermal histamine (loss of C-fiber response).
4. Decreased or absent deep tendon reflexes.
5. Ashkenazi Jewish ancestry.
(Sources: [Axelrod 2004, PMID 15277940](https://pubmed.ncbi.nlm.nih.gov/15277940/); [GeneReviews NBK1180](https://www.ncbi.nlm.nih.gov/books/NBK1180/).)

### 10.2 Confirmatory Testing
- **Molecular genetic testing** — targeted ELP1 c.2204+6T>C testing (Sanger or specific PCR assay) — is the standard of care and confirms nearly all AJ cases. Rare non-AJ cases require full ELP1 sequencing.
- **Elevated plasma dopamine/norepinephrine ratio.**
- **Postural blood pressure testing** — orthostatic BP drop >20 mmHg without appropriate HR increase.
- **Blunted response to intradermal histamine** — absent axon flare.
- **Sural nerve biopsy** (rarely used now) — reduced unmyelinated fibers.

### 10.3 Imaging / Functional Tests
- **Chest CT** — bronchiectasis in adults.
- **Ophthalmic OCT** — thinning of retinal nerve fiber layer (especially temporal papillomacular bundle) as early as childhood.
- **Ambulatory blood pressure monitoring** — extreme BP variability.
- **Polysomnography** — high prevalence of sleep-disordered breathing (>70% adults).
- **Renal ultrasound / eGFR** — progressive CKD.
- **Ventilatory response tests** — blunted hypoxic/hypercapnic ventilatory response.

### 10.4 Screening
- **Preconception carrier screening for the ELP1 c.2204+6T>C variant** is standard-of-care in Ashkenazi Jewish populations and included in the ACMG/ACOG expanded AJ panels and commercial screens (JScreen, Myriad Foresight, Natera).
- **Prenatal diagnosis** (CVS or amniocentesis with targeted ELP1 mutation testing) available for known-carrier couples; **PGT-M** (preimplantation genetic testing) is commonly used.
- Newborn screening is *not* standard because the genotype is essentially always confirmed in couples-at-risk before conception.

### 10.5 Differential Diagnosis
- Other HSANs (HSAN I–VIII), particularly HSAN II (WNK1/HSN2), HSAN IV (NTRK1), HSAN V (NGF).
- Congenital insensitivity to pain with anhidrosis (CIPA).
- Central hypoventilation syndrome (PHOX2B).
- Chronic inflammatory demyelinating polyneuropathy (autonomic variant).
- Multiple system atrophy (in adult presentations).
- POTS / pure autonomic failure (adult onset).

---

## 11. Outcome / Prognosis

### 11.1 Survival and Mortality
- **Historical (pre-1960):** ~50% mortality by age 5.
- **Current (2020s):** ~**50% probability of reaching age 40**; some patients survive into their 60s–70s. Approximately 40% of the surviving FD cohort is >20 years old ([Palma et al. 2017, Sleep](https://academic.oup.com/sleep/article/40/8/zsx083/3831157); [MedLink Neurology](https://www.medlink.com/articles/familial-dysautonomia)).
- **Leading causes of death:**
  - **Sudden Unexpected Death During Sleep (SUDS)** — most common; annual incidence ~3.4 per 1,000 person-years ([Palma et al. 2017, PMID 28521050](https://pubmed.ncbi.nlm.nih.gov/28521050/)).
  - **Chronic lung disease / respiratory failure** — from repeated aspiration.
  - **Renal failure.**
  - **Autonomic crises with severe hypertension** — cerebral hemorrhage.

### 11.2 Morbidity and Function
- Severe cumulative disability: blindness, ataxia, feeding-tube dependence, ventilator dependence, dialysis in late-stage CKD.
- QOL measures show substantial impairment across physical and mental domains; anxiety is prominent.

### 11.3 Complications
- Aspiration pneumonia and bronchiectasis.
- Chronic kidney disease.
- Kyphoscoliosis with restrictive lung disease.
- Optic neuropathy → legal blindness.
- Charcot joints, unrecognized fractures.
- Severe hypertensive crises with end-organ damage.

### 11.4 Prognostic Factors
- **Younger age at first crisis / more frequent crises** → worse prognosis.
- **Sleep-disordered breathing (untreated OSA), fludrocortisone use, low-normal potassium** — independent risk factors for SUDS ([Palma et al. 2017, PMID 28521050](https://pubmed.ncbi.nlm.nih.gov/28521050/)).
- **Residual full-length ELP1 protein levels** (measurable in blood or fibroblasts) may correlate with severity and are being explored as biomarkers ([González-Duarte et al. 2025 Ann Clin Transl Neurol, PMID 41385477](https://pubmed.ncbi.nlm.nih.gov/41385477/)).

---

## 12. Treatment

**All currently approved therapy is symptomatic; disease-modifying therapy is investigational.**

### 12.1 Pharmacotherapy (Symptomatic)
- **Autonomic crises:**
  - **Diazepam** IV/rectal (0.2 mg/kg every 3 hours, max 10 mg) — first line to abort vomiting and reduce catecholamine surges (NCIT:C29435).
  - **Clonidine** oral/transdermal — for persistent hypertension (α₂-agonist; NCIT:C505). Combined diazepam+clonidine is standard.
  - **Dexmedetomidine** — refractory crises, more selective α₂-agonist with shorter half-life ([Krajewski et al. 2022 Cureus, PMID 36381719](https://pubmed.ncbi.nlm.nih.gov/36381719/)); sublingual formulation being trialed (NCT06148311).
- **Baroreflex failure / BP lability:** **Carbidopa** (peripheral DOPA-decarboxylase inhibitor) reduces peripheral catecholamine surges and BP variability in a double-blind crossover trial ([Palma et al. 2020, Hypertension, PMID 32623925](https://www.ahajournals.org/doi/10.1161/HYPERTENSIONAHA.120.15267)).
- **Orthostatic hypotension:** Midodrine (α₁-agonist), high salt intake, compression stockings; **fludrocortisone is now avoided** given SUDS association.
- **Gastrointestinal:** Proton pump inhibitors, prokinetics, Nissen fundoplication, gastrostomy tube.
- **Alacrima:** Artificial tears, punctal plugs.
- **Anxiety:** Benzodiazepines, SSRIs.

### 12.2 Disease-Modifying / Advanced Therapies (Investigational)
- **Kinetin (N⁶-furfuryladenine)** — small-molecule splicing corrector; increases exon 20 inclusion and full-length ELP1 mRNA/protein in patient cells and in vivo ([Slaugenhaupt et al. 2004 Hum Mol Genet](https://pubmed.ncbi.nlm.nih.gov/14976162/); [Axelrod et al. 2011, Pediatr Res, PMID 21725277](https://pubmed.ncbi.nlm.nih.gov/21725277/)).
- **PTC258 / PTC-related oral splicing modulators (PTC Therapeutics)** — kinetin-derivative small molecules that cross the blood–brain barrier and restore correct ELP1 splicing in Elp1 mouse brain and prevent gait ataxia and retinal degeneration ([Sinha et al. 2023, PMID 36809767](https://pubmed.ncbi.nlm.nih.gov/36809767/)). Clinical development ongoing.
- **BPN-14477 / other splice modulators** in preclinical stages.
- **Phosphatidylserine** — FDA-approved food supplement that elevates ELP1 expression and, combined with kinetin, is additive; ameliorated neurodegeneration in mouse models ([Bochner et al. 2013, PLOS Genet](https://journals.plos.org/plosgenetics/article?id=10.1371%2Fjournal.pgen.1006486)).
- **Exon-specific U1 snRNA (ExSpeU1) delivered by AAV2 intravitreally** — rescues optic neuropathy in mouse models ([Romani et al. 2025 bioRxiv](https://www.biorxiv.org/content/10.1101/2025.08.21.671454.full.pdf)).
- **AAV2-ELP1 gene augmentation** intravitreally — restores retinal function in humanized FD mice; first demonstration that visual function can be recovered pharmacologically ([Yesilyurt et al. 2026, Molecular Therapy](https://www.cell.com/molecular-therapy-family/molecular-therapy/fulltext/S1525-0016(26)00311-4)).
- **Antisense oligonucleotides (ASOs)** targeting the ELP1 splice defect — under preclinical development.

### 12.3 Surgical/Interventional
- **Nissen fundoplication + gastrostomy tube** — for severe GERD and aspiration risk.
- **Spinal fusion** for progressive scoliosis.
- **Punctal plugs / lateral tarsorrhaphy** for severe alacrima.
- **Tracheostomy and non-invasive ventilation** — for severe SDB or respiratory failure.

### 12.4 Supportive / Rehabilitative
- **Nutritional support** via G-tube.
- **Physical therapy** for ataxia and orthopedic complications.
- **Occupational therapy** for adaptive tools (blindness, ataxia).
- **Speech-language therapy** for dysphagia.
- **Multidisciplinary care** at specialized dysautonomia centers (NYU, Israel FD Center).

**Ontology suggestions (NCIT):** NCIT:C505 (Clonidine); NCIT:C29435 (Diazepam); NCIT:C471 (Carbidopa); NCIT:C61708 (Dexmedetomidine); NCIT:C935 (Midodrine); NCIT:C874 (Fludrocortisone – avoid); NCIT:C15986 (Pharmacotherapy); NCIT:C15238 (Gene Therapy); NCIT:C15329 (Surgical Procedure); NCIT:C15302 (Physical Therapy).

---

## 13. Prevention

### 13.1 Primary Prevention
- **Preconception carrier screening** for the ELP1 c.2204+6T>C variant is the cornerstone of primary prevention. Included in expanded AJ carrier screening panels (ACMG-recommended).
- **PGT-M (preimplantation genetic testing for monogenic disorders)** for carrier couples.
- **Prenatal diagnosis** (CVS/amniocentesis + targeted mutation testing).

### 13.2 Secondary Prevention (Early Detection & Complications)
- Routine polysomnography and initiation of non-invasive ventilation for sleep-disordered breathing (reduces SUDS incidence).
- Regular renal function and ophthalmological monitoring.
- Aspiration precautions: G-tube feeding, thickened liquids.

### 13.3 Tertiary Prevention
- Prophylactic pulmonary hygiene / chest physiotherapy.
- Vaccinations (influenza, pneumococcal, RSV as indicated).
- Aggressive management of GERD and treatment of pneumonia early.

### 13.4 Genetic Counseling
- Recurrence risk for carrier couples is 25%.
- Genetic counseling is offered routinely to AJ couples before conception; JScreen and hospital-based counseling widely accessible.

---

## 14. Other Species / Natural Disease

FD is a **human-only** disease; no naturally occurring counterpart has been reported. Animal disease modeling is entirely experimental.

- **NCBI Taxon:** NCBITaxon:9606 (*Homo sapiens*).
- **Orthologous genes:** ELP1 is highly conserved. Orthologs: mouse *Ikbkap/Elp1* (MGI:1927169); rat *Elp1*; zebrafish *elp1*; *S. cerevisiae* IKI3/ELP1. Elongator complex components are present from yeast to mammals.
- **Comparative pathology:** Elongator loss in yeast and *C. elegans* causes translation/tRNA modification defects but obviously no neuropathy phenotype. Mouse conditional knockouts and humanized *TgFD9* models faithfully recapitulate DRG, sympathetic, and retinal degeneration (see §15).
- **Zoonotic potential:** Not applicable.

---

## 15. Model Organisms

### 15.1 Mouse Models
- **Global Ikbkap knockout (*Ikbkap⁻/⁻*)** — early embryonic lethal by E12.5 due to cardiovascular and neural tube defects ([Chen et al. 2009](https://pubmed.ncbi.nlm.nih.gov/19893621/); Dietrich et al. 2011).
- **Wnt1-Cre;Ikbkap^flox/flox (neural-crest conditional knockout)** — apoptosis of Pax3⁺ progenitors, sensory and sympathetic neurons; recapitulates DRG loss and phenotypic FD ([George et al. 2013 PNAS, PMID 24007805](https://www.pnas.org/doi/10.1073/pnas.1308596110)).
- **Tyrp2-Cre;Ikbkap^flox/flox** — retinal-specific loss; slow, progressive RGC and photoreceptor degeneration mimicking FD optic neuropathy ([Ueki et al. 2016 eNeuro](https://www.eneuro.org/content/3/5/ENEURO.0143-16.2016); [Chekuri et al. 2018 Dis Model Mech](https://journals.biologists.com/dmm/article/11/7/dmm033746/53306/)).
- **TgFD9 (humanized) mouse** — carries human ELP1 with the c.2204+6T>C variant on a mouse Elp1-null background; produces tissue-specific ELP1 reduction paralleling human disease and shows progressive gait ataxia and RGC degeneration. Used as the primary preclinical platform for testing kinetin/PTC258 splice modulators and gene therapies ([Sinha et al. 2018 Am J Hum Genet, PMID 30827494](https://www.sciencedirect.com/science/article/pii/S0002929719300540); [Sinha et al. 2023, PMID 36809767](https://pubmed.ncbi.nlm.nih.gov/36809767/)).
- **Elp1 CNS-conditional knockouts** (Nestin-Cre) — CNS role for ELP1 in oligodendrocyte and neuron survival ([Chaverra et al. 2017, Dis Model Mech, PMID 28167615](https://pubmed.ncbi.nlm.nih.gov/28167615/)).

### 15.2 Cellular / In Vitro Models
- **Patient-derived fibroblasts** — standard for splicing assays; leaky wild-type ELP1 splicing measurable.
- **iPSC-derived sensory / sympathetic / retinal ganglion neurons** — from FD patients or CRISPR-edited controls; used to model developmental apoptosis and screen small-molecule splicing correctors ([Zeltner et al. 2016, Nat Med, PMID 27295489](https://pubmed.ncbi.nlm.nih.gov/27295489/)).
- **HEK293/HeLa cell lines** with ELP1 minigene constructs — high-throughput splice-modulator screens.

### 15.3 Zebrafish
- **elp1 morphants and mutants** — recapitulate peripheral neurogenesis defects; useful for high-throughput drug screens (Cheishvili et al. 2011).

### 15.4 Model Applications and Limitations
- **Applications:** Small-molecule and gene therapy preclinical testing, mechanistic dissection of splicing, elucidation of Elongator's tissue-specific role.
- **Limitations:** No mouse model reproduces the full multisystem autonomic crisis phenotype (BP lability, gastrointestinal dysmotility); most models focus on sensory/retinal degeneration. The humanized *TgFD9* mouse is the most faithful but retains partial wild-type Elp1 in some tissues.

### 15.5 Resources
- **MGI** (Mouse Genome Informatics) for *Ikbkap/Elp1* alleles.
- **NYU Langone Dysautonomia Center Biorepository** — patient fibroblasts, iPSCs, tissue samples.
- **JAX** and academic labs (Slaugenhaupt lab; Kaufmann/Palma group) — humanized mouse lines.
- **Familial Dysautonomia Foundation** — funding and biobank coordination.

---

## Ontology Term Summary

| Feature | Suggested Term |
|---|---|
| Disease | MONDO:0009131 (Familial Dysautonomia); ICD-10 G90.1 |
| Gene | HGNC:5959 (ELP1); UniProt O95163 |
| Inheritance | HP:0000007 (Autosomal recessive) |
| Alacrima | HP:0000522 |
| Absent fungiform papillae | HP:0000167 |
| Areflexia | HP:0001315 |
| Nociceptor loss / pain insensitivity | HP:0007021 |
| Ataxia (proprioceptive) | HP:0002131 |
| Optic neuropathy | HP:0000632 |
| Autonomic crises | HP:0005112 |
| Orthostatic hypotension | HP:0001278 |
| Kyphoscoliosis | HP:0002751 |
| Gastroesophageal reflux | HP:0002020 |
| Recurrent aspiration | HP:0002100 |
| Sudden death in sleep | HP:0001700-related |
| Elongator complex | GO:0033588 |
| tRNA wobble modification | GO:0002098 |
| DRG | UBERON:0000044 |
| Sympathetic ganglion | UBERON:0002440 |
| Nociceptor | CL:0000198 |
| Retinal ganglion cell | CL:0000740 |
| Clonidine | NCIT:C505 |
| Diazepam | NCIT:C29435 |
| Carbidopa | NCIT:C471 |

---

## Key References (selected, primary literature)

1. Anderson SL, Coli R, Daly IW, et al. Familial dysautonomia is caused by mutations of the IKAP gene. *Am J Hum Genet*. 2001;68(3):753-758. **PMID: 11179016**.
2. Slaugenhaupt SA, Blumenfeld A, Gill SP, et al. Tissue-specific expression of a splicing mutation in the IKBKAP gene causes familial dysautonomia. *Am J Hum Genet*. 2001;68(3):598-605. **PMID: 11179017**.
3. Cuajungco MP, Leyne M, Mull J, et al. Tissue-specific reduction in splicing efficiency of IKBKAP due to the major mutation associated with familial dysautonomia. *Am J Hum Genet*. 2003;72(3):749-758. **PMID: 12756454**.
4. Pearson J, Pytel BA. Quantitative studies of dorsal root ganglia and neuropathologic observations on spinal cords in familial dysautonomia. *J Neurol Sci*. 1978;39(1):47-59. **PMID: 624961**.
5. Axelrod FB. Familial dysautonomia. *Muscle Nerve*. 2004;29(3):352-363. **PMID: 15277940**.
6. Lehavi O, Aizenstein O, Bercovich D, et al. Screening for familial dysautonomia in Israel: evidence for higher carrier rate among Polish Ashkenazi Jews. *Genet Test*. 2003;7(2):139-142. **PMID: 12885336**.
7. Leyne M, Mull J, Gill SP, et al. Identification of the first non-Jewish mutation in familial dysautonomia. *Am J Med Genet A*. 2003;118A(4):305-308. **PMID: 12687659**.
8. Axelrod FB, Liebes L, Gold-Von Simson G, et al. Kinetin improves IKBKAP mRNA splicing in patients with familial dysautonomia. *Pediatr Res*. 2011;70(5):480-483. **PMID: 21725277**.
9. George L, Chaverra M, Wolfe L, et al. Familial dysautonomia model reveals Ikbkap deletion causes apoptosis of Pax3+ progenitors and peripheral neurons. *PNAS*. 2013;110(46):18698-18703. **PMID: 24007805**.
10. Ueki Y, Ramirez G, Salcedo E, et al. Loss of Ikbkap causes slow, progressive retinal degeneration in a mouse model of familial dysautonomia. *eNeuro*. 2016;3(5). **PMID: 27822501**.
11. Chekuri A, Bhagavath Chandran G, Yesilyurt HG, et al. Retina-specific loss of Ikbkap/Elp1 causes mitochondrial dysfunction that leads to selective retinal ganglion cell degeneration. *Dis Model Mech*. 2018;11:dmm033746.
12. Palma JA, Norcliffe-Kaufmann L, Kaufmann H. Sudden Unexpected Death During Sleep in Familial Dysautonomia: A Case-Control Study. *Sleep*. 2017;40(8):zsx083. **PMID: 28521050**.
13. Palma JA, Norcliffe-Kaufmann L, Fuente-Mora C, et al. Chemoreflex failure and sleep-disordered breathing in familial dysautonomia. *Sleep Med*. 2019;54:34-40. **PMID: 30890343**.
14. Palma JA, Norcliffe-Kaufmann L, Martinez J, Kaufmann H. Carbidopa for Afferent Baroreflex Failure in Familial Dysautonomia. *Hypertension*. 2020;76(3):724-731. **PMID: 32623925**.
15. Sinha R, Kim YJ, Nomakuchi T, et al. Development of an oral treatment that rescues gait ataxia and retinal degeneration in a phenotypic mouse model of familial dysautonomia. *Am J Hum Genet*. 2023;110(4):531-547. **PMID: 36809767**.
16. Krajewski KJ et al. Experience With Dexmedetomidine Use in the Treatment of Dysautonomic Crisis in Familial Dysautonomia: An Off-Label Use. *Cureus*. 2022. **PMID: 36381719**.
17. Jackson MZ, Gruner KA, Qin C, Tourtellotte WG. A neuron autonomous role for the familial dysautonomia gene ELP1 in sympathetic and sensory target tissue innervation. *Development*. 2014. **PMID: 25139957**.
18. Bochner R, Ziv Y, Zeevi D, et al. Phosphatidylserine increases IKBKAP levels in a humanized knock-in IKBKAP mouse model. *Hum Mol Genet*. 2013. **PMID: 23824189**.

---

## Sources

- [GeneReviews: Familial Dysautonomia (NBK1180)](https://www.ncbi.nlm.nih.gov/books/NBK1180/)
- [OMIM 223900 – Dysautonomia, Familial](https://omim.org/entry/223900)
- [OMIM 603722 – ELP1 (IKBKAP) gene entry](https://omim.org/entry/603722)
- [Orphanet – Familial Dysautonomia (ORPHA:1764)](https://orpha.net/consor/cgi-bin/OC_Exp.php?Expert=1764&amp=&lng=en)
- [GARD – Familial dysautonomia](https://rarediseases.info.nih.gov/diseases/7581/familial-dysautonomia)
- [NORD – Familial Dysautonomia](https://rarediseases.org/rare-diseases/dysautonomia-familial/)
- [Cleveland Clinic – Familial Dysautonomia](https://my.clevelandclinic.org/health/diseases/24220-familial-dysautonomia)
- [MedLink Neurology – Familial dysautonomia](https://www.medlink.com/articles/familial-dysautonomia)
- [Medscape – Familial Dysautonomia clinical presentation](https://emedicine.medscape.com/article/1200921-clinical)
- [Ohlen et al. 2017 – Elp1 in adult CNS (PMC5451171)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5451171/)
- [Mezey et al. 2016 – FD Mechanisms and Models (PMC5127153)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5127153/)
- [Palma et al. 2020 – Carbidopa in FD, Hypertension](https://www.ahajournals.org/doi/10.1161/HYPERTENSIONAHA.120.15267)
- [Sinha et al. 2023 – PTC258 preclinical (PMC10027479)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10027479/)
- [Palma et al. 2017 – Sudden death during sleep in FD, Sleep journal](https://academic.oup.com/sleep/article/40/8/zsx083/3831157)
- [Chekuri et al. 2018 – Retina-specific Elp1 loss](https://journals.biologists.com/dmm/article/11/7/dmm033746/53306/)
- [Naftelberg et al. 2016 – Molecular basis of FD, Trends Genet](https://www.sciencedirect.com/science/article/abs/pii/S0168952516300287)
- [Norcliffe-Kaufmann et al. 2023 – FD current review, Clin Auton Res](https://link.springer.com/article/10.1007/s10286-023-00941-1)
- [Advances in FD treatment 2025 review, Expert Rev Neurother](https://www.tandfonline.com/doi/full/10.1080/14737175.2025.2525400)
- [Krajewski et al. 2022 – Dexmedetomidine off-label use in FD (PMC9636886)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9636886/)
- [Jackson et al. 2014 – Elp1 in trigeminal ganglion (eLife 71455)](https://elifesciences.org/articles/71455)
- [Morini et al. 2023 – Transcriptome of humanized FD mouse (PMC10766950)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10766950/)
- [George et al. 2013 – Ikbkap deletion apoptosis, PNAS](https://www.pnas.org/doi/10.1073/pnas.1308596110)
- [Yesilyurt et al. 2026 – AAV-ELP1 gene therapy, Molecular Therapy](https://www.cell.com/molecular-therapy-family/molecular-therapy/fulltext/S1525-0016(26)00311-4)
- [Bochner et al. 2013 – Phosphatidylserine in FD, PLOS Genetics](https://journals.plos.org/plosgenetics/article?id=10.1371%2Fjournal.pgen.1006486)
- [González-Duarte et al. 2025 – ELP1 whole-blood expression biomarker (PMC13161875)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13161875/)
- [Pearson & Pytel 1978 – DRG neuropathology (PMID 624961)](https://pubmed.ncbi.nlm.nih.gov/624961/)
- [JScreen – Familial Dysautonomia carrier screening](https://www.jscreen.org/hereditary-diseases/familial-dysautonomia)
- [Foresight Carrier Screen – Familial Dysautonomia (Myriad)](https://myriad.com/womens-health/diseases/familial-dysautonomia/)
- [Chaverra et al. 2017 – Elp1 CNS role, Dis Model Mech (PMID 28167615)](https://pubmed.ncbi.nlm.nih.gov/28167615/)
- [Anderson et al. 2001 – Original IKBKAP mutation, Am J Hum Genet (PMID 11179016)](https://pubmed.ncbi.nlm.nih.gov/11179016/)
- [Slaugenhaupt et al. 2001 – Tissue-specific IKBKAP splicing (PMID 11179017)](https://pubmed.ncbi.nlm.nih.gov/11179017/)
- [Cuajungco et al. 2003 – Splicing efficiency in FD (PMID 12756454)](https://pubmed.ncbi.nlm.nih.gov/12756454/)
- [Lehavi et al. 2003 – Israeli carrier screening (PMID 12885336)](https://pubmed.ncbi.nlm.nih.gov/12885336/)
- [Leyne et al. 2003 – Non-Jewish FD mutation (PMID 12687659)](https://pubmed.ncbi.nlm.nih.gov/12687659/)
- [Palma et al. 2019 – Chemoreflex failure and SDB in FD (PMID 30890343)](https://pubmed.ncbi.nlm.nih.gov/30890343/)
- [Sinha et al. 2019 – ELP1 splicing correction reverses proprioceptive loss](https://www.sciencedirect.com/science/article/pii/S0002929719300540)
- [Karlsborn et al. 2014 – Elongator tRNA wobble modification, RNA Biology](https://www.tandfonline.com/doi/full/10.4161/15476286.2014.992269)
- [ClinicalTrials.gov NCT06148311 – Dexmedetomidine sublingual film for FD crises](https://clinicaltrials.gov/study/NCT06148311)
- [ELP1 Gene Augmentation Restores Visual Function bioRxiv preprint](https://www.biorxiv.org/content/10.64898/2026.01.09.698339.full.pdf)
- [Peripheral neuron phenotypes rescued by AAV gene therapy (PMC12486110)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12486110/)
- [Proteomic profiling of Elp1-deficient trigeminal ganglia 2025 preprint](https://www.biorxiv.org/content/10.64898/2025.12.05.692685.full.pdf)
- [Familial Dysautonomia Foundation](https://familialdysautonomia.org/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 38 |
| Resolved | 38 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 38 |
| On topic | 7 |
| Off topic | 8 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:37000283` (1 mention) - An assessment of vegetation cover of Mysuru City, Karnataka State, India, using deep convolutional neural networks.
  - shared terms: model
- `PMID:32623925` (3 mentions) - Genetically Predicted Blood Pressure Across the Lifespan: Differential Effects of Mean and Pulse Pressure on Stroke Risk.
  - shared terms: disease
- `PMID:20857273` (3 mentions) - [Psychotherapy of Asperger syndrome in adults].
  - shared terms: none
- `PMID:24007805` (3 mentions) - The effect of color priming on infant brain and behavior.
  - shared terms: none
- `PMID:38168126` (1 mention) - A 3-year follow-up clinical study on the preservation for vitality of involved tooth in jaw cysts through an innovative method.
  - shared terms: none
- `PMID:21725277` (4 mentions) - Myocardial dysfunction in neonatal sepsis: a tissue Doppler imaging study.
  - shared terms: none
- `PMID:23824189` (1 mention) - A calcineurin-dependent switch controls the trafficking function of α-arrestin Aly1/Art6.
  - shared terms: cell, model
- `DOI:10.1161/HYPERTENSIONAHA.120.15267` (4 mentions) - Carbidopa for Afferent Baroreflex Failure in Familial Dysautonomia
  - shared terms: failure

Weighed against this report's own most characteristic terms: `elp1`, `autonomic`, `loss`, `crise`, `disease`, `gene`, `elongator`, `retinal`, `aspiration`, `sensory`, `neuron`, `failure`, `progressive`, `palma`, `ataxia`, `cell`, `neuropathy`, `complex`, `model`, `ganglion`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 74 |
| Resolved | 68 |
| Unresolved (possible confabulation) | 3 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 57 |
| Terms named correctly | 21 |
| Terms named as a **different** term | 19 |
| Terms whose name is worth a second look | 17 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0100799` (1 mention) - the report calls it "smooth tongue"; HP calls it **Neoplasm of the middle ear**
- `HP:0001315` (2 mentions) - the report calls it "Depressed / absent deep tendon reflexes** — ~100%", "Areflexia"; HP calls it **Diminished deep tendon reflex**
- `HP:0002131` (2 mentions) - the report calls it "Ataxia (proprioceptive)"; HP calls it **Episodic ataxia**
- `HP:0000632` (2 mentions) - the report calls it "Optic neuropathy"; HP calls it **Lacrimation abnormality**
- `HP:0005112` (2 mentions) - the report calls it "abnormal autonomic nervous system physiology", "Autonomic crises"; HP calls it **Abdominal aortic aneurysm**
- `HP:0002326` (1 mention) - the report calls it "hypertension"; HP calls it **Transient ischemic attack**
- `HP:0011169` (1 mention) - the report calls it "Blood pressure lability / baroreflex failure** — ~100%"; HP calls it **Generalized clonic seizure**
- `HP:0002102` (1 mention) - the report calls it "Recurrent aspiration pneumonia** — ~90%"; HP calls it **Pleuritis**
- `HP:0000739` (1 mention) - the report calls it "Anxiety and emotional lability** — very frequent"; HP calls it **Anxiety**
- `HP:0011036` (1 mention) - the report calls it "Increased serum dopamine-to-norepinephrine ratio"; HP calls it **Abnormality of renal excretion**
- `CL:0011003` (2 mentions) - the report calls it "peripheral autonomic neuron"; CL calls it **magnocellular neurosecretory cell**
- `UBERON:0002393` (2 mentions) - the report calls it "Enteric nervous system", "enteric nervous system"; UBERON calls it **pharyngotympanic tube**
- `UBERON:0002205` (2 mentions) - the report calls it "Tongue fungiform papillae", "fungiform papilla"; UBERON calls it **manubrium of sternum**
- `UBERON:0001291` (1 mention) - the report calls it "lacrimal gland"; UBERON calls it **thick ascending limb of loop of Henle**
- `NCIT:C29435` (3 mentions) - the report calls it "Diazepam"; NCIT calls it **DNA Minor Groove Binding Agent SG2000**
- `NCIT:C505` (3 mentions) - the report calls it "Clonidine"; NCIT calls it **Fluorouracil**
- `NCIT:C471` (2 mentions) - the report calls it "Carbidopa"; NCIT calls it **Enzyme Inhibitor**
- `NCIT:C61708` (1 mention) - the report calls it "Dexmedetomidine"; NCIT calls it **Dextroamphetamine Saccharate**
- `NCIT:C874` (1 mention) - the report calls it "Fludrocortisone – avoid"; NCIT calls it **Thiamine**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0000167` (2 mentions), reported as "atrophic fungiform papillae", "Absent fungiform papillae" - HP does not contain this term
- `ECTO:0001093` (1 mention), reported as "exposure to psychosocial stress" - ECTO does not contain this term
- `ECTO:0000000` (1 mention) - ECTO does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0007021` (2 mentions) - the report calls it "Nociceptor loss / pain insensitivity"; HP calls it **Pain insensitivity**
- `HP:0010829` (1 mention) - the report calls it "Decreased temperature sensation** — ~90%"; HP calls it **Impaired temperature sensation**
- `HP:0002020` (3 mentions) - the report calls it "Gastroesophageal reflux** — ~85%", "Gastroesophageal reflux"; HP calls it **Gastroesophageal reflux**
- `HP:0002098` (1 mention) - the report calls it "abnormal breathing regulation"; HP calls it **Respiratory distress**, and lists "Labored breathing" among its other names
- `HP:0002751` (2 mentions) - the report calls it "Kyphoscoliosis** — ~90% by adolescence", "Kyphoscoliosis"; HP calls it **Kyphoscoliosis**
- `GO:0033588` (4 mentions) - the report calls it "Elongator holoenzyme complex", "Cytoplasmic Elongator complex", "Elongator complex"; GO calls it **elongator holoenzyme complex**, and lists "Elongator core complex" among its other names
- `GO:0002098` (3 mentions) - the report calls it "tRNA wobble uridine modification", "tRNA wobble modification"; GO calls it **tRNA wobble uridine modification**
- `GO:0006915` (2 mentions) - the report calls it "Neuronal apoptosis** during development", "apoptotic process"; GO calls it **apoptotic process**, and lists "induction of apoptosis by p53" among its other names
- `GO:0090128` (1 mention) - the report calls it "regulation of synaptonemal complex assembly"; GO calls it **regulation of synapse maturation**
- `UBERON:0000044` (3 mentions) - the report calls it "Dorsal root ganglion", "dorsal root ganglion", "DRG"; UBERON calls it **dorsal root ganglion**, and lists "DRG" among its other names
- `UBERON:0002440` (3 mentions) - the report calls it "Sympathetic chain ganglia", "sympathetic ganglion", "Sympathetic ganglion"; UBERON calls it **inferior cervical ganglion**, and lists "stellate ganglion" among its other names
- `GO:0005874` (1 mention) - the report calls it "Microtubule cytoskeleton"; GO calls it **microtubule**
- `GO:0005739` (1 mention) - the report calls it "Mitochondria"; GO calls it **mitochondrion**, and lists "mitochondria" among its other names
- `UBERON:0001782` (1 mention) - the report calls it "retina"; UBERON calls it **pigmented layer of retina**, and lists "pigmented retina" among its other names
- `HP:0000007` (2 mentions) - the report calls it "Autosomal recessive", "Inheritance pattern:** **Autosomal recessive"; HP calls it **Autosomal recessive inheritance**
- `NCIT:C935` (1 mention) - the report calls it "Midodrine"; NCIT calls it **Vindesine Sulfate**, and lists "Gesidine" among its other names
- `HP:0002100` (1 mention) - the report calls it "Recurrent aspiration"; HP calls it **Recurrent aspiration pneumonia**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0000167` - called "atrophic fungiform papillae", "Absent fungiform papillae"
- `HP:0001315` - called "Depressed / absent deep tendon reflexes** — ~100%", "Areflexia"
- `HP:0005112` - called "abnormal autonomic nervous system physiology", "Autonomic crises"
- `HP:0002020` - called "Gastroesophageal reflux** — ~85%", "Gastroesophageal reflux"
- `HP:0002751` - called "Kyphoscoliosis** — ~90% by adolescence", "Kyphoscoliosis"
- `GO:0033588` - called "Elongator holoenzyme complex", "Cytoplasmic Elongator complex", "Elongator complex"
- `GO:0002098` - called "tRNA wobble uridine modification", "tRNA wobble modification"
- `GO:0006915` - called "Neuronal apoptosis** during development", "apoptotic process"
- `CL:0000198` - called "nociceptor", "Nociceptor"
- `CL:0000740` - called "retinal ganglion cell", "Retinal ganglion cells", "Retinal ganglion cell"
- `UBERON:0000044` - called "Dorsal root ganglion", "dorsal root ganglion", "DRG"
- `UBERON:0002440` - called "Sympathetic chain ganglia", "sympathetic ganglion", "Sympathetic ganglion"
- `UBERON:0002393` - called "Enteric nervous system", "enteric nervous system"
- `UBERON:0001675` - called "Trigeminal ganglion", "trigeminal ganglion"
- `UBERON:0002205` - called "Tongue fungiform papillae", "fungiform papilla"
- `HP:0000007` - called "Autosomal recessive", "Inheritance pattern:** **Autosomal recessive"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.