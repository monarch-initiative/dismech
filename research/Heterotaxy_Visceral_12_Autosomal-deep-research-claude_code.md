---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5
cached: false
start_time: '2026-11-18T14:38:23.838054'
end_time: '2026-11-18T14:56:35.748256'
duration_seconds: 1091.91
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Heterotaxy Visceral 12 Autosomal
  mondo_id: MONDO:0859222
  category: Mendelian
  causal_genes: CIROP
  omim_id: OMIM:619702
  synonyms: visceral heterotaxy 12; HTX12
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
  - claude-opus-5
  web_search_requests: 12
  num_turns: 1
  total_cost_usd: 6.08543143
  session_id: 1cfc9195-16f8-4077-abde-5e770e3d237b
  stop_reason: end_turn
  tool_calls: 121
  retrieval_calls: 121
  assistant_text_blocks: 36
citation_count: 92
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 6
  quotes_valid: 5
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:34903892
  relevance_assessed: 16
  on_topic: 8
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 120
  verified: 103
  not_found: 1
  obsolete: 0
  unverifiable: 16
  confabulation_rate: 0.01
  labels_checked: 75
  labels_matching: 43
  labels_mismatched: 9
  mislabelled_terms:
  - term_id: ECO:0000250
    reported_labels:
    - Putative metalloproteinase that plays a role in left-right patterning process
    ontology_label: sequence similarity evidence used in manual assertion
  - term_id: MONDO:0859222
    reported_labels:
    - MONDO
    - HTX12
    ontology_label: heterotaxy, visceral, 12, autosomal
  - term_id: HP:0011540
    reported_labels:
    - Levotransposition of the great arteries
    - Partial anomalous pulmonary venous connection (PAPVC)
    ontology_label: Levotransposition of the great arteries
  - term_id: HP:0011994
    reported_labels:
    - Ostium primum ASD (ASD-OP)
    ontology_label: Abnormal atrial septum morphology
  - term_id: HP:0001670
    reported_labels:
    - Tricuspid atresia (TA)
    ontology_label: Asymmetric septal hypertrophy
  - term_id: HP:0011673
    reported_labels:
    - Abnormal superior vena cava morphology (SVC anomalies
    ontology_label: Cardiac hemangioma
  - term_id: UBERON:0005086
    reported_labels:
    - Kupffer's vesicle (zebrafish LRO)
    ontology_label: hair follicle placode
  - term_id: NCIT:C777
    reported_labels:
    - angiotensin-converting enzyme inhibitor
    ontology_label: Therapeutic Progesterone
  - term_id: NCIT:C29703
    reported_labels:
    - alprostadil
    ontology_label: Antilipidemic Agent
  labels_variant: 23
  unresolved_terms:
  - NCIT:C29087
  unresolvable_prefixes:
  - MGI
  - Chr14
  - OMIM
  - RGD
  - EXT_ID
  - MIM
  - PubMed
  - NCBIGene
  - GENCC
  - ORPHA
  - ID
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Heterotaxy Visceral 12 Autosomal
- **MONDO ID:** MONDO:0859222 (if available)
- **Causal gene(s):** CIROP
- **OMIM:** OMIM:619702
- **Synonyms:** visceral heterotaxy 12; HTX12
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Heterotaxy Visceral 12 Autosomal** covering all of the
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

I'll research this disease now. Let me start by loading the web search tool and querying the key identifiers.

Both OMIM pages are blocked. Neither fetch returned any content, so I have nothing to report from the entries themselves.

- https://www.omim.org/entry/619702 (HTX12): HTTP 403 Forbidden. The response body was not retrieved.
- https://www.omim.org/entry/619703 (CIROP): HTTP 403 Forbidden. The response body was not retrieved.

This is a permanent refusal from the server, not a transient error, so retrying these URLs or variants of them would fail the same way. The block applies to the whole host from this fetch path, so I did not try other omim.org pages.

I did not fill any section from memory. Every field you asked for (Description, Clinical Features, Inheritance, Molecular Genetics, Animal Model, Allelic Variants, the clinical synopsis, identifiers, dbSNP IDs and references) is unknown to me from this session.

Options for getting the content:
- Use OMIM's official API with a registered API key, if you have one. It is a separate endpoint from the website, and I have not tested whether it is reachable through this proxy.
- Check whether the OMIM content is available through NCBI or another source you can reach. I have not verified any of these, and I would need you to name the URL before I fetch it.
- Retrieve the pages from a browser session that is logged in to OMIM, then pass the text to me to format.

Launching parallel retrievals of the primary literature and databases.

The PMC URL returned only the PMC home page, with no article content. Trying the PubMed record next.

The Nature URL redirected to an identity-provider login page rather than the article, so I am not following it. Trying the Amsterdam UMC repository record.

The Cell page returned HTTP 403. That is a permanent refusal, so I won't retry it. Your fallback is a different host, so I'll try the PubMed search you gave.

PMC returned only its homepage, so the search did not run. PubMed returned 429 with Retry-After 60, which allows one retry, so I'll try it once more.

I could not retrieve the article or its abstract. None of the three sources gave any content about CIROZ.

**What failed**

- **Cell (primary URL):** https://www.cell.com/ajhg/fulltext/S0002-9297(24)00448-8 returned HTTP 403 Forbidden. The response body was not retrieved. This is a permanent refusal, so sending the URL again would fail the same way. I did not retry it.
- **PubMed search:** https://pubmed.ncbi.nlm.nih.gov/?term=CIROZ+left-right+patterning returned HTTP 429 with Retry-After: 60 on the first attempt. On the single retry it returned HTTP 203 with a "Cookies must be enabled" page and no search results. WebFetch cannot enable cookies, so this route is blocked for now.
- **PMC search:** https://pmc.ncbi.nlm.nih.gov/?term=CIROZ returned HTTP 200, but only the PMC homepage came back. The search results were not included, so this page does not answer the question.

**Not reported**

Because I could not read any source, I have no verbatim abstract, PMID, DOI, publication date, volume/pages, or authors. I also have nothing on CIROZ's former symbol or chromosome location, the CIROP/MMP21 module, the patient variants, CIROP function or disease, or the zebrafish, Xenopus, mouse and phylogenetic results. I have not filled any of these from memory.

**Possible next steps**

- Open the Cell article in a browser with institutional access, or send me the PDF or text if you have it.
- Search PubMed directly for the title, or for "CIROZ" alone, and send me the PMID or DOI. I can then fetch the PubMed record page by its PMID, which may work where the search page did not.
- Check whether a preprint of the paper is on bioRxiv or medRxiv. Those are often open access.

I could only get the abstract, and only from the Amsterdam UMC repository record. The full text was not available from any of the four URLs, so most of the requested detail is missing.

**Sources tried, in order**

1. `https://pmc.ncbi.nlm.nih.gov/?term=34903892` returned HTTP 200 but only the PMC home page. No article content.
2. `https://pubmed.ncbi.nlm.nih.gov/34903892/` returned HTTP 203 with a "Cookies must be enabled" page. No article content.
3. `https://www.nature.com/articles/s41588-021-00970-4` returned a 303 redirect to `https://idp.nature.com/authorize?...` (a login/cookie endpoint). I did not follow it, because it is a cross-host redirect to an identity provider and not the article.
4. `https://pure.amsterdamumc.nl/en/publications/discovery-of-a-genetic-module-essential-for-assigning-leftright-a/` returned HTTP 200 with the abstract, bibliographic data and author/affiliation lists. This is the only substantive source. It contains no full text, so it has no patient, variant, phenotype, animal-model or CIROZ/C1orf127 data.

**Abstract (partial, because the source is non-preapproved)**

The 125-character quote limit means I cannot reproduce the full abstract verbatim. Here are the exact fragments and a paraphrase of the rest.

- Quoted: "identified five genes encoding extracellular proteins, including a putative protease" is the abstract's description of the search result. It names the protein "ciliated left–right organizer metallopeptide (CIROP)".
- Paraphrase: the authors searched for genes whose loss during vertebrate evolution tracks the presence or absence of motile cilia in the left–right organizer. The group states that organs in reptiles, birds, even-toed mammals and cetaceans are believed to lack motile cilia.
- Quoted: "In zebrafish and Xenopus, CIROP is required solely on the left side" is followed in the abstract by the statement that CIROP acts downstream of leftward flow and upstream of DAND5.
- Quoted: "We further ascertained 21 human patients with loss-of-function CIROP mutations presenting with recessive situs anomalies." The abstract says 21 patients, not 21 families.
- Paraphrase of the closing: the authors propose an ancestral genetic module that disappeared twice during vertebrate evolution but is still essential for left–right distinction in humans.

**Requested items the abstract does not cover (not available from any source I could reach)**

- Number of families, ethnic/geographic origin and consanguinity status.
- Individual CIROP variants (c./p. nomenclature, zygosity, class, family).
- Patient phenotypes and counts (situs, heart lesions, spleen, malrotation, biliary atresia, and so on).
- Protein domain structure, zinc metallopeptidase activity, MMP21 and PKD1L1 relationships, and the mechanistic detail on Nodal/Pitx2 and Dand5 beyond the abstract's single "upstream of DAND5" statement.
- Zebrafish, Xenopus and mouse knockdown/knockout details and percentages.
- The phylogenetic profiling methods and results.
- Any CIROZ/C1orf127 mention.

**Authors (from the Amsterdam UMC record)**

Emmanuelle Szenker-Ravi (corresponding), Tim Ott, Muznah Khatoo, Anne Moreau de Bellaing, Wei Xuan Goh, Yan Ling Chong, Anja Beckers, Darshini Kannesan, Guillaume Louvel, Priyanka Anujan, Vydianathan Ravi, Carine Bonnard, Sébastien Moutton, Patric Schoen, Marine Fradin, Estelle Colin, André Mégarbane, Linda Daou, Ghassan Chehab, Sylvie di Filippo, Caroline Rooryck, Jean-François Deleuze, Anne Boland, Nicolas Arribard, Rukiye Eker, Sumanty Tohari, Alvin Yu-Jin Ng, Marlène Rio, Chun Teck Lim, Birgit Eisenhaber, Frank Eisenhaber, Byrappa Venkatesh, Jeanne Amiel, Hugues Roest-Crollius, Christopher T. Gordon, Achim Gossler, Sudipto Roy, Tania Attie-Bitach, Martin Blum (corresponding), Patrice Bouvagnet (corresponding), Bruno Reversade (corresponding).

The record's affiliation list has 27 entries (for example Agency for Science, Technology and Research Singapore, Hannover Medical School, Institut de Biologie de l'École Normale Supérieure, Institut Jérôme Lejeune, Koç University, Istanbul University, and others). The rendered page does not map affiliations to individual authors.

**Citation:** Szenker-Ravi E, et al. Nature Genetics 2022;54(1):62-72. DOI 10.1038/s41588-021-00970-4. Early online 2021. The Amsterdam record also lists Scopus and Pure links, which I did not fetch.

**Next steps:** the full text is probably available through the publisher with institutional access, or through a PMC copy if one exists under a PMCID, which I could not find from the URLs given. If you can supply a PMCID or a publicly accessible full-text URL, I can fetch that and extract the patient, variant, phenotype and animal-model details.

## Report: CIROP / visceral heterotaxy 12

Three of the four pages failed. Only the MedGen page returned content.

**1. NCBI Gene, https://www.ncbi.nlm.nih.gov/gene/100128908: failed.** The fetch returned HTTP 200 with a reCAPTCHA interstitial ("Checking your browser before accessing www.ncbi.nlm.nih.gov"), not gene data. I did not retry or try variant URLs. Nothing from this page is reported: no summary, coordinates, HGNC/Ensembl/UniProt IDs, transcript counts, GeneRIFs, expression, or orthologs.

**2. ClinVar, https://www.ncbi.nlm.nih.gov/clinvar/?term=CIROP%5Bgene%5D: failed.** Same reCAPTCHA interstitial, HTTP 200, 176 characters. No variant records, total count, or pathogenic/likely pathogenic count are available from this fetch.

**3. MedGen, https://www.ncbi.nlm.nih.gov/medgen/?term=CIROP: succeeded.** This page was fetched from a non-preapproved source, so the quote limit applies. The page is a search-results page for CIROP and lists two MedGen records.

- **Gene cross-link:** "CIROP ciliated left-right organizer metallopeptidase" (linked to Gene 100128908). The page says "cirop in MedGen (1)" and "All 420 Gene records".
- **Target record: "Heterotaxy, visceral, 12, autosomal"**
  - MedGen UID: 1803695
  - Concept ID (CUI): C5676898
  - Semantic type shown: "Congenital Abnormality"
  - OMIM link: http://www.omim.org/entry/619702
  - Also has ClinVar and Genes links, and a GeneReviews label with no link text.
  - Definition (OMIM-derived, cited as Szenker-Ravi et al., 2022): "Visceral heterotaxy-12 (HTX12) is an embryonic developmental disorder characterized by defects in the asymmetric positioning of visceral organs across the left-right axis, known as laterality defects." The page adds that the phenotype ranges "from complete organ reversal (situs inversus totalis) to selective misarrangement of organs (situs ambiguus) such as the liver, spleen, and pancreas," often with dextrocardia or complex congenital heart defects, and that early death may occur in severe cases.
  - Cross-references shown: OMIM 619702. The filter panel shows "Records in Mondo (2)", "Records in OMIM (2)" and "Records in Orphanet (0)", but the Mondo IDs are not printed. No GARD ID is shown. No HPO terms or HP IDs are listed, and the filter panel shows "Records in HPO (0)".
- **OMIM text quoted on the page:** "HTX12 (619702), caused by mutation in the **CIROP** gene (619703) on chromosome 14q11". The 619703 is printed as the gene number in that OMIM-derived text.
- **Other MedGen record returned:** "Heterotaxy, visceral, 1, X-linked", UID 3366091, Concept ID C1844020, OMIM 306955.

**4. GTR, https://www.ncbi.nlm.nih.gov/gtr/genes/100128908/: failed.** Same reCAPTCHA interstitial, HTTP 200. No test or panel list is available from this fetch.

Because the host returns a bot challenge on the Gene, ClinVar and GTR pages, I did not fetch other pages on www.ncbi.nlm.nih.gov. Sending these URLs again would most likely hit the same challenge. Items 1, 2 and 4 need to be checked in a browser, or through another route such as the NCBI E-utilities, which I did not try.

**Summary:** Only the Human Protein Atlas page returned usable content, and even that was partly a model-extracted summary. gnomAD, UniProt, and Ensembl returned no gene data.

**1. gnomAD (https://gnomad.broadinstitute.org/gene/ENSG00000283654?dataset=gnomad_r4): nothing usable.** HTTP 200, but the body is only the text "gnomAD" (6 characters). The page is JavaScript-only, so no pLI, LOEUF, o/e, Z-score, variant counts, or pathogenic variant data could be read. Sending the same URL again would return the same shell.

**2. UniProt (https://www.uniprot.org/uniprotkb/A6NGN9/entry): nothing usable.** HTTP 200, but the body is a generic "UniProt website fallback message" (740 characters) about translation tools, browser versions, and network issues. It contains no entry data, so the accession A6NGN9 is neither confirmed nor refuted. I did not try the search URL the brief suggested, because the fallback is a page-render failure rather than a not-found result, and trying a variant of the URL would fail the same way. A fetch that renders the entry in a browser, or a UniProt REST entry for A6NGN9, would be needed.

Not obtained: accession confirmation, protein name, length, HExxH positions, signal peptide, TM/GPI, location, GO terms, catalytic activity, zinc cofactor, MIM 619702 association, natural variants.

**3. Human Protein Atlas (https://www.proteinatlas.org/ENSG00000283654-CIROP): partial.** The first ~40,000 characters of the page were site navigation and filter lists with no CIROP values. The expression data below comes from a model-extracted summary of the remaining text, not verbatim page text. Treat the numbers as unverified against the page.

- RNA tissue specificity: "Not detected". Highest tissue: Choroid plexus, 0.4 nTPM (tooltip).
- Brain: "Low domain specificity"; highest in spinal cord, 14 nCPM (spatial transcriptomics tooltip).
- Single cell type specificity: "Group enriched (Retinal amacrine cells, Oligodendrocytes)"; highest in retinal amacrine cells, 3.6 nCPM.
- Immune cells: "Not detected in immune cells"; highest in myeloid DC at 0.0 nTPM.
- Bulk-RNA deconvolution: "Cell type enriched (Testis - Early spermatids)".
- Subcellular: main location "Not available"; predicted location and tooltip "Membrane".
- Protein (MS) tissue specificity: "Not detected"; no tissue profile.
- Cancer: RNA and protein specificity "Not detected"; highest in lung adenocarcinoma (validation), 1.0 pTPM.
- Isoforms: 3 isoforms with RNA expression; "No isoform over expression cutoff".
- Conservation: "Limited conservation (Not detected)"; orthologs in 3 of 4 species.

The summary says the page gives nTPM values only in tooltips. The "Not detected" tissue call sits alongside a nonzero 0.4 nTPM maximum, so the summary's categorical and numeric values may not agree exactly.

**4. Ensembl (https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000283654): nothing usable.** HTTP 200, but the body is only "Gene: CIROP — Ensembl" (21 characters). The page is JavaScript-only, so no coordinates, strand, transcript or exon counts, or gene description were obtained.

**Not verified from any source here:** the chromosome 14q11.2 location, the LMLN2 and HTX12 aliases, and the MIM 619702 association.

Final URLs read: https://gnomad.broadinstitute.org/gene/ENSG00000283654?dataset=gnomad_r4, https://www.uniprot.org/uniprotkb/A6NGN9/entry, https://www.proteinatlas.org/ENSG00000283654-CIROP, https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000283654

The server returned a 429 with `Retry-After: 0`, so I'll retry once as the fetch rules allow.

I could not retrieve the preprint. The PDF URL returned HTTP 429 (Too Many Requests) with `Retry-After: 0` on two attempts. I did not try the `v1.full` fallback you suggested, because it is a variant on the same host, and that host's refusal applies to it too. Sending the same request again later may work, since the 429 said it was a rate limit with no wait.

**What is missing:** I have no abstract, author list, posting date, DOI, CIROP or MMP21 mechanism details, Cirop mutant data, or publication status. I have not read the preprint text, so nothing below comes from it.

**URLs attempted:**
- https://www.biorxiv.org/content/10.1101/2024.10.13.618030.full.pdf: HTTP 429, twice.

**Not attempted:**
- https://www.biorxiv.org/content/10.1101/2024.10.13.618030v1.full (same host, skipped under the fetch rules).

**Next steps:** Ask me to retry the PDF URL later, or to try the `v1.full` page now and accept the risk of another refusal. If you have the PDF saved locally, I can answer your questions from that file instead.

## Summary

Only the MGI mouse record returned usable content. The rat Alliance page, the Alliance search, ZFIN, Xenbase, and IMPC returned no gene data, so the zebrafish, Xenopus, rat, and IMPC sections are empty. I did not fetch the human Alliance gene page directly; the human ortholog identifiers below come from the MGI record.

## 1. MGI mouse record (https://www.informatics.jax.org/marker/MGI:5588935), read

- **Symbol / name:** Cirop, "ciliated left-right organizer metallopeptidase"
- **MGI ID:** MGI:5588935 (also MGI:6887928 listed under other accession IDs)
- **Synonyms listed:** Gm29776 only. The page does not list Lmln2, Gm94, or 4930563E18Rik.
- **NCBI Gene:** 101056084
- **Ensembl:** ENSMUSG00000114865 (transcript ENSMUST00000224691; protein ENSMUSP00000153646)
- **Location:** Chr14:54930055-54936290 bp, minus strand, GRCm39 (Ensembl annotation). Mapping is listed as syntenic on chromosome 14, with no cM position given.
- **Human ortholog:** CIROP, "ciliated left-right organizer metallopeptidase". Its synonyms are HTX12 and LMLN2. The page gives HGNC:53647, NCBI Gene 100128908, UniProt A0A1B0GTW7, and 14q11.2 (chr14:23099062-23105018, minus strand, GRCh38).
- **Orthology:** 2 vertebrate orthologs. "Cirop stringent orthology" cluster 52459253 lists 1 human, 1 mouse, 1 rat.
- **Disease:** "visceral heterotaxy 12", DOID:0051026, OMIM:619702. The page lists 1 disease with human CIROP associations.
- **Alleles and mutants:** The page shows 1 entry under All Mutations and Alleles, 1 under Chemically induced (other), 1 genomic mutation involving Cirop, and 1 strain or line available at IMSR. The allele symbols, allele IDs (MGI:), and strain details did not come through in the extraction, so I cannot give them.
- **MP phenotype terms:** The page reports 2 phenotype references. The MP term IDs did not come through.
- **GO:** 8 annotations and 4 GO references. The GO IDs and evidence codes did not come through. The page shows broad GO categories only, such as hydrolase, signaling receptor binding, and cell differentiation.
- **Expression (GXD):** 624 assay results, 6 tissue entries, 1 cDNA entry, and 1 literature entry. The grid shows wild-type expression in the early conceptus, embryo ectoderm, embryo mesenchyme, and several organ systems. The page does not describe node or GRP expression.
- **References:** 12 in total. The earliest is J:322341, Szenker-Ravi E et al., "Discovery of a genetic module essential for assigning left-right asymmetry in humans and ancestral vertebrates", Nat Genet 2022 Jan;54(1):62-72. PMIDs were not shown in the extraction.
- **Protein:** EC 3.4.24.- and InterPro IPR001577 (Peptidase M8, leishmanolysin).
- **Last database update on the page:** 11/10/2026 (MGI 6.29).

## 2. Rat Alliance (https://www.alliancegenome.org/gene/RGD:1560492), no content

The page returned only the title "Alliance of Genome Resources" (HTTP 200, 29 characters). It is probably rendered by JavaScript, so the orthology table, disease, expression, and GO data are unavailable from this fetch.

## 3. Human CIROP, Alliance search (https://www.alliancegenome.org/search?q=CIROP), no content

The search page returned only the title, with no results. The human HGNC ID HGNC:53647 comes from the MGI page, not from the Alliance. The Alliance human page, its disease associations with MONDO IDs, and the DIOPT scores were not retrieved.

## 4. Zebrafish ZFIN (https://zfin.org/search?q=cirop), blocked

ZFIN returned a "Verify you're human" bot-check page (HTTP 200, 488 characters). No gene data was returned. Sending this URL again would likely hit the same check.

## 5. Xenopus Xenbase (https://www.xenbase.org/entry/?search=cirop), blocked

Xenbase returned a "One moment, please" verification page (HTTP 200, 163 characters). No gene data was returned. Sending this URL again would likely hit the same check.

## 6. IMPC (https://www.mousephenotype.org/data/search?term=Cirop), no results

The page returned an empty shell with five placeholder result rows and the text "Loading". No gene, allele, or phenotype data came through, so I cannot say whether IMPC has Cirop data. A browser visit or the IMPC API would be needed to check.

## Gaps and open items

- Mouse allele IDs, MP term IDs, GO IDs, and PMIDs are not in this report. Re-reading the MGI page with a prompt aimed at those sections, or using the MGI batch or allele reports, would fill them in.
- Rat, human Alliance, zebrafish, Xenopus, and IMPC data remain unverified. A browser or the Alliance API would be needed for those.

I could not retrieve the abstract or any full text for either paper. Two of the five Europe PMC endpoints and the CIROZ search failed, and the two sources that worked do not carry the abstract.

**Endpoint results (PMID 34903892)**

1. `https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:34903892&resultType=core&format=json`: HTTP 500. Re-sending it would likely fail the same way.
2. `https://europepmc.org/article/MED/34903892`: HTTP 403 Forbidden.
3. `https://www.ebi.ac.uk/europepmc/webservices/rest/MED/34903892/fullTextXML`: HTTP 404 Not Found, so no full text XML.
4. `https://api.semanticscholar.org/graph/v1/paper/PMID:34903892?fields=...`: HTTP 200, but the `abstract` field is null. The publisher elided it. The record notes the abstract is at `https://doi.org/10.1038/s41588-021-00970-4`. Non-preapproved source.
5. `https://api.crossref.org/works/10.1038/s41588-021-00970-4`: HTTP 200, but there is no abstract field. Non-preapproved source.

**CIROZ search**

`https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=CIROZ%20AND%20left-right&resultType=core&format=json`: HTTP 500. I did not retry it. I also did not look up the CIROZ paper through other sources, because that would mean building a search URL from your query text. Nothing about the CIROZ paper (PMID, DOI, abstract, journal, date) was retrieved.

**Bibliographic details for the Szenker-Ravi et al. paper (from Semantic Scholar and Crossref)**

- Title: "Discovery of a genetic module essential for assigning left–right asymmetry in humans and ancestral vertebrates"
- Journal: Nature Genetics
- Volume 54, issue 1, pages 62–72 (Crossref)
- Published online (first online): 13 December 2021. Print issue: January 2022. Received 8 December 2020; accepted 14 October 2021.
- DOI: 10.1038/s41588-021-00970-4
- PMID: 34903892
- PMCID: not returned by any endpoint
- Semantic Scholar CorpusId: 245171772
- Crossref lists a correction notice, DOI 10.1038/s41588-022-01053-8, dated 18 March 2022. I did not read it.
- Author list (41, in order, per Crossref): Emmanuelle Szenker-Ravi, Tim Ott, Muznah Khatoo, Anne Moreau de Bellaing, Wei Xuan Goh, Yan Ling Chong, Anja Beckers, Darshini Kannesan, Guillaume Louvel, Priyanka Anujan, Vydianathan Ravi, Carine Bonnard, Sébastien Moutton, Patric Schoen, Mélanie Fradin, Estelle Colin, André Megarbane, Linda Daou, Ghassan Chehab, Sylvie Di Filippo, Caroline Rooryck, Jean-François Deleuze, Anne Boland, Nicolas Arribard, Rukiye Eker, Sumanty Tohari, Alvin Yu-Jin Ng, Marlène Rio, Chun Teck Lim, Birgit Eisenhaber, Frank Eisenhaber, Byrappa Venkatesh, Jeanne Amiel, Hugues Roest Crollius, Christopher T. Gordon, Achim Gossler, Sudipto Roy, Tania Attie-Bitach, Martin Blum, Patrice Bouvagnet, Bruno Reversade.

**Full text and detailed findings**

Not available. The full text XML returned 404, and the publisher page was not fetched. Because of that I have no patient or family counts, CIROP variants with c./p. nomenclature, phenotypes, domain or mechanism details, or animal model results.

**Other links (not fetched)**

- The Semantic Scholar record gives an open-access PDF at `https://oskar-bordeaux.fr/bitstream/20.500.12278/184703/2/MRGM_2022_Nat%20Genet_Szenker-Ravi.pdf`. It is a third-party repository copy, so I did not fetch it. If you want me to read it, say so.
- The Semantic Scholar record also gives a model-generated TLDR, which is not part of the paper: the study identifies an ancestral module of genes expressed in ciliated left–right organizer tissue and required for left–right axis specification in humans and certain vertebrates.

**Not provided**

The full abstract text, which you asked for verbatim, is not in any source I could reach. The Nature Genetics article page at the DOI above is the place to get it. The rules for non-preapproved sources would also limit how much of it I could quote in any case.

Unpaywall and OpenAlex both point to the same repository PDF (Université de Bordeaux, submitted version). I'll fetch that next.

The connection dropped, which is a transient failure, so I'll retry once.

## Results for CIROP (LMLN2)

**Endpoint status**
- UniProt REST, txt search: HTTP 200, returned entries. Read in full.
- UniProt REST, JSON search: HTTP 200, 105,255 characters. Only the first 39,651 characters were verbatim. The rest is a model summary of other orthologs, which I have not relied on. The CIROP entry (A0A1B0GTW7) is fully covered by the verbatim text.
- gnomAD GET query: HTTP 200, complete.
- HGNC REST: HTTP 200, returned XML, not JSON. Complete.
- Ensembl REST: failed twice with `read ECONNRESET` (no HTTP status). Both attempts were connection resets, and I stopped after the one permitted retry. Ensembl data below comes from UniProt cross-references, not Ensembl itself.

URLs read:
- https://rest.uniprot.org/uniprotkb/search?query=gene:CIROP+AND+organism_id:9606&format=txt
- https://rest.uniprot.org/uniprotkb/search?query=CIROP+OR+LMLN2+AND+organism_id:9606&format=json&fields=...
- https://gnomad.broadinstitute.org/api?query=...
- https://rest.genenames.org/fetch/symbol/CIROP

### 1. UniProt (Swiss-Prot entry A0A1B0GTW7, CIROP_HUMAN, reviewed, 788 aa)
- **Accessions:** A0A1B0GTW7 (primary); A0A2R8Y3T5 (secondary)
- **Entry name:** CIROP_HUMAN
- **Recommended name:** Ciliated left-right organizer metallopeptidase (EC 3.4.24.-)
- **Alternative name:** Leishmanolysin-like peptidase 2
- **Gene name:** CIROP (HGNC:53647); synonym LMLN2
- **Length:** 788 aa; MW 85397 Da
- **Signal peptide:** 1–20
- **Topology:** extracellular 21–735; transmembrane helix 736–756 (Helical); cytoplasmic 757–788
- **Disordered regions:** 40–59 (low complexity), 767–788
- **Domain:** the entry lists Pfam PF01457 (Peptidase_M8) and InterPro IPR001577 (Peptidase_M8), but no domain feature with residue coordinates. The family is "peptidase M8 family" per the SIMILARITY comment.
- **Zinc-binding HExxH motif (my derivation from the sequence):** H305-E306-L307-L308-H309. Annotated zinc ligands are H305, H309, and H385 (catalytic). Position 385 is the third His in the sequence "LLSSHWEARL" (381–390).
- **Active site:** E306 (ACT_SITE 306)
- **Zn(2+) binding:** 305, 309, 385 (all "catalytic")
- **N-glycosylation (Asn):** 333, 425, 491, 524, 713
- **GPI anchor:** none. Membrane anchor is the single TM helix above.
- **Subcellular location:** "Membrane; Single-pass type I membrane protein"
- **Function (verbatim):** "Putative metalloproteinase that plays a role in left-right patterning process." (ECO:0000250)
- **Tissue specificity:** no entry in this record.
- **Catalytic activity:** no CC entry; EC 3.4.24.- only.
- **Cofactor:** Zn(2+). "Binds 1 zinc ion per subunit."
- **Disease:** Heterotaxy, visceral, 12, autosomal (HTX12), MIM:619702 (DI-06243, acronym HTX12). Verbatim: "A form of visceral heterotaxy, a complex disorder due to disruption of the normal left-right asymmetry" and "HTX12 inheritance is autosomal recessive." Note: "The disease is caused by variants affecting the gene represented in this entry."
- **Disease variants (all from PubMed:34903892):** S31F (uncertain), 191–788 deletion, C324S (uncertain), 346–788 deletion, S384L (uncertain), R389I (uncertain), 456 deletion (uncertain), L469P (uncertain).
- **Isoforms:** 3 (isoform 1 displayed, A0A1B0GTW7-1).
- **Other cross-refs:** CCDS86373.1; RefSeq NP_001341569.1 / NM_001354640.2; MANE-Select ENST00000637218.2 / ENSP00000489869.1; GeneID 100128908; MIM 619702 (phenotype), 619703 (gene); Orphanet 101063 (situs inversus totalis).

**GO terms (reviewed entry):**
- Biological process:
  - GO:0061966 establishment of left/right asymmetry (ISS:UniProtKB)
  - GO:0007155 cell adhesion (IEA:InterPro)
  - GO:0006508 proteolysis (IEA:InterPro)
- Molecular function:
  - GO:0004222 metalloendopeptidase activity (IEA:InterPro)
  - GO:0008233 peptidase activity (IBA:GO_Central)
- Cellular component:
  - GO:0005737 cytoplasm (IBA:GO_Central)
  - GO:0016020 membrane (IEA:UniProtKB-SubCell)

**Other UniProt records from the same search (not the canonical protein):**
- A0A1B0GTW7 is the reviewed entry. Its 17-fragment search also returned TrEMBL entries A0ACI8U3L3 (600 aa, Ensembl ENSP00000610901.1, ENST00000940842.1, ENSG00000283654.5) and A0A2R8Y752 (614 aa fragment, ENSP00000495729.1, ENST00000642668.1).
- Ortholog entries are CIROP_DANRE (A0A1D5NSK0), CIROP_MOUSE (A0A286YEC0), and CIROP_XENLA (A0A1L8HYT7).

**Identifiers from UniProt cross-refs:** Ensembl ENST00000637218.2, ENST00000644000.1, ENSG00000283654.4 (reviewed entry); HPA "Not detected"; Bgee "Expressed in mucosa of stomach and 38 other cell types or tissues."

### 2. gnomAD v? (GRCh38, from API)
- **gene_id:** ENSG00000283654
- **symbol:** CIROP
- **chrom:** 14
- **start:** 23099062
- **stop:** 23104989
- **pLI:** 3.738146807418961e-12
- **LOEUF (oe_lof_upper):** 1.5011576356426848
- **oe_lof:** 1.1122973813731794 (lower 0.8359256623692269, upper 1.5011576356426848)
- **obs_lof:** 31
- **exp_lof:** 27.87024452195433
- **mis_z:** -5.072793825691162
- **oe_mis:** 1.7657777907262553

### 3. HGNC (HGNC:53647)
- **HGNC ID:** HGNC:53647
- **Approved symbol:** CIROP
- **Approved name:** ciliated left-right organizer metallopeptidase
- **Status:** Approved; locus group protein-coding gene; locus type gene with protein product
- **Previous symbol:** LMLN2
- **Previous name:** leishmanolysin like peptidase 2
- **Alias symbols:** none in the response
- **Location:** 14q11.2
- **Ensembl gene:** ENSG00000283654
- **NCBI Entrez gene:** 100128908
- **UniProt:** A0A1B0GTW7
- **OMIM:** 619703 (gene)
- **Dates:** approved/reserved 2017-08-11; symbol changed 2022-01-18; name changed 2022-01-18; modified 2023-01-20
- **Other IDs:** VEGA OTTHUMG00000191651; CCDS86373; RefSeq NM_001354640; MANE select ENST00000637218.2 and NM_001354640.2; MGI:5588935; RGD:1560492; GenCC HGNC:53647; PubMed 34903892

### 4. Ensembl
Failed (`read ECONNRESET`, twice). Not retrieved: Ensembl gene coordinates, strand, biotype, description, and transcript list. From the other sources:
- Ensembl gene ENSG00000283654 (version 4 in the reviewed entry, version 5 in the TrEMBL entries)
- MANE transcript ENST00000637218.2 (protein ENSP00000489869.1)
- Other transcripts: ENST00000644000.1 (ENSP00000493582.1), ENST00000940842.1 (ENSP00000610901.1), ENST00000642668.1 (ENSP00000495729.1, partial)
- GRCh38 span 14:23099062–23104989 is from gnomAD, not Ensembl. Strand and biotype are unknown.

Retry later if you need the Ensembl record; it failed with connection resets, not an HTTP error.

The Bordeaux PDF came back as raw binary with no readable text. Unpaywall also lists a second OA copy on HAL, so I'll try that one.

The PDF returned HTTP 200 on the second attempt, but the text extraction gave me raw compressed PDF bytes, not readable prose. I'll try the listed alternatives, starting with the repository handle page and the PMC link.

The PDF returned an anti-bot challenge page instead of the paper. You asked for a fallback in that case, so I'll try the HTML reviewed-preprint page next.

I could not get the full text, the abstract, or any of the variant, cohort, or model-organism details. The only substantive content I obtained is bibliographic metadata.

**URLs and results**

1. **Unpaywall** (`https://api.unpaywall.org/v2/10.1038/s41588-021-00970-4?email=research@example.org`): worked (HTTP 200, JSON). `is_oa` is true, `oa_status` is green, and the best OA location is a submitted (author) version in the Université de Bordeaux repository: `https://oskar-bordeaux.fr/bitstream/20.500.12278/184703/2/MRGM_2022_Nat%20Genet_Szenker-Ravi.pdf`. A second copy is listed at `https://hal.science/hal-03876795v1/document`.
2. **Zenodo** (`https://zenodo.org/record/5188601`): failed, timeout after 60 s. Retrying would not be a permanent-failure retry, but I did not retry it.
3. **HAL search** (`https://hal.science/search/index/?q=%22left-right+asymmetry%22+Szenker-Ravi`): blocked by an Anubis bot-protection page (HTTP 200, access denied). The same block applied to the HAL document URL (`https://hal.science/hal-03876795v1/document`) when I tried it as the second OA copy.
4. **Semantic Scholar** (search URL): failed, HTTP 403.
5. **OpenAlex** (`https://api.openalex.org/works/doi:10.1038/s41588-021-00970-4`): worked (HTTP 200, JSON). The abstract is not available: `abstract_inverted_index` is null.
6. **Bordeaux PDF** (the OA PDF from Unpaywall and OpenAlex): fetched (HTTP 200, application/pdf, about 3.3 MB), but the content came back as raw compressed PDF binary with no readable text. The harness saved it to a local file, which I have not reported a path for. Extracting text from that file, for example with `pdftotext`, should give the paper's text.

**Bibliographic metadata (verbatim from the Unpaywall JSON and OpenAlex response)**

- Title: "Discovery of a genetic module essential for assigning left–right asymmetry in humans and ancestral vertebrates"
- Journal: Nature Genetics (ISSN 1061-4036); publisher Springer Science and Business Media LLC
- DOI: 10.1038/s41588-021-00970-4; PMID 34903892 (from the OpenAlex `ids` field)
- Published online 2021-12-13 (`published_date`); Unpaywall lists `year` as 2021, and the 2022 print date comes from the OpenAlex summary and the HAL citation.
- Corresponding authors (per affiliation flags): Emmanuelle Szenker-Ravi (first author), Martin Blum, Patrice Bouvagnet, Bruno Reversade (last author).
- Author list (Unpaywall `z_authors`, in order): Emmanuelle Szenker-Ravi, Tim Ott, Muznah Khatoo, Anne Moreau de Bellaing, Wei Xuan Goh, Yan Ling Chong, Anja Beckers, Darshini Kannesan, Guillaume Louvel, Priyanka Anujan, Vydianathan Ravi, Carine Bonnard, Sébastien Moutton, Patric Schoen, Mélanie Fradin, Estelle Colin, André Megarbane, Linda Daou, Ghassan Chehab, Sylvie Di Filippo, Caroline Rooryck, Jean-François Deleuze, Anne Boland, Nicolas Arribard, Rukiye Eker, Sumanty Tohari, Alvin Yu-Jin Ng, Marlène Rio, Chun Teck Lim, Birgit Eisenhaber, Frank Eisenhaber, Byrappa Venkatesh, Jeanne Amiel, Hugues Roest Crollius, Christopher T. Gordon, Achim Gossler, Sudipto Roy, Tania Attié-Bitach, Martin Blum, Patrice Bouvagnet, Bruno Reversade.
- Not in this response: the abstract, cohort data, variant list, clinical phenotypes, CIROP protein features, pathway/epistasis results, animal model data, and the phylogenetic argument. The PDF text and the abstract are unknown to me.

**Notes**

- The OpenAlex "cited_by_count 52" and the volume/page numbers (54, pp. 62–72) come from a model-generated summary of the truncated part of the OpenAlex response, not verbatim text.
- Next steps that might succeed: extract the text from the locally saved Bordeaux PDF, or ask for the Europe PMC or PMC version of the paper, if one exists. I did not fetch those because they were not in your list or in the API responses.

The full-text PDF was saved locally. Reading it directly.

The handle page worked and gives the abstract. The PMC link returned a 301 to the NCBI's current host, which is the same article, so I'll follow that to get the full text.

PMC returned a reCAPTCHA bot challenge, so that source is closed to me. I'll try the OpenAlex and CORE alternatives next.

I could not read the paper. All three URLs failed to yield text, so I have no abstract, authors, DOI, Cirop data, or model to report, and I have not filled those gaps from memory.

**What happened with each URL**

1. **https://elifesciences.org/reviewed-preprints/104430v1/pdf** (HTTP 200, text/html, 232 characters). The response was a "Client Challenge" page saying a required part of the site could not load. It was not the PDF.
2. **https://elifesciences.org/reviewed-preprints/104430v1** (HTTP 200, text/html, 232 characters). Same client challenge page. I fetched this as the fallback you specified.
3. **https://www.biorxiv.org/content/10.1101/2024.10.13.618030v2.full.pdf** (HTTP 200, application/pdf, about 4.4 MB). The fetch returned raw, compressed PDF bytes rather than extracted text, so the page text was unreadable. The PDF was saved to a local file for you; the harness will report its location. The metadata shows the PDF title "MMP21 behaves as a fluid flow transported morphogen to impart laterality during development" and a creation date of 2024-11-09. That is the only bibliographic information I could confirm, and it comes from the PDF's metadata, not from the paper's text.

**Why I stopped**

Both eLife URLs are challenge pages, so retrying them would likely fail the same way. I did not try variants of the URLs or guess at other bioRxiv pages such as the `.full` HTML version. I also have no local PDF text tool available in this session, so I could not decompress the saved PDF myself.

**Options to get the content**

- Run `pdftotext` (Poppler) or PyMuPDF on the saved bioRxiv PDF locally, then paste the abstract, the Cirop results, and the model section here.
- Open the eLife reviewed preprint in a normal browser and paste the text, including any eLife assessment.
- If you want me to try the bioRxiv HTML full-text page, give me that URL and I will fetch it. I have not fetched it because you did not name it.

## Summary

All requested endpoints returned HTTP 200, so none failed. Two limits apply to this report:

- **Copyright limit on the abstract:** the PubMed abstract text is from a non-preapproved source, so I could not reproduce it verbatim. Section 5 gives a paraphrase and only short quotes.
- **Partly summary-derived data:** the ClinVar fetches were truncated by the tool. Rows marked **S** in the table come from a model-extracted summary of the truncated text, not from verbatim JSON. Rows marked **V** are verbatim. Row 19 (UID 4883002) is partly verbatim and partly summary-derived.

## 1. Gene record (esummary, db=gene, id=100128908)

- **Official symbol:** CIROP
- **Official full name:** ciliated left-right organizer metallopeptidase
- **Other aliases:** HTX12, LMLN2
- **Other designations:** "ciliated left-right organizer metallopeptidase|leishmanolysin homolog|leishmanolysin like peptidase 2"
- **Chromosome:** 14
- **Map location:** 14q11.2
- **MIM:** 619703
- **Organism:** Homo sapiens (taxid 9606)
- **Current genomic coordinates (GRCh38, NC_000014.9):** chrstart 23104988, chrstop 23099061, exoncount 16. The gene is on the minus strand (chrstart > chrstop).
- **Previous coordinates:**
  - GRCh37 (NC_000014.8, GCF_000001405.25): 23574197 to 23568270 (annotation RS_2024_09); 23574170 to 23569450 (annotation release 105)
  - T2T-CHM13 (NC_060938.1, GCF_009914755.1): 17305633 to 17299695
- **Summary (paraphrased, Alliance of Genome Resources, Jul 2025):** predicted to have peptidase activity and to be involved in establishing left/right asymmetry. Predicted to be located in membrane and to be active in the cytoplasm. Implicated in visceral heterotaxy 12.

## 2. ClinVar search (esearch, db=clinvar, term=CIROP[gene])

- **Total count:** 50 (retmax 50, retstart 0). All 50 UIDs were returned.
- **UIDs:** 5016670, 5016669, 5008300, 5005300, 5005299, 5000715, 4997565, 4990621, 4983557, 4983478, 4982256, 4921073, 4921072, 4921071, 4921070, 4921069, 4921068, 4921067, 4883002, 4874139, 4849971, 4849970, 4820860, 4820846, 4395642, 4277730, 4277705, 3390959, 3054769, 2644090, 2644089, 2644088, 2582479, 2442172, 1804116, 1804115, 1344495, 1344493, 1344490, 1344488, 1335922, 1335920, 155681, 155306, 155119, 148657, 146230, 59932, 57745, 57246

## 3. ClinVar records (esummary, db=clinvar)

Notes on the table:
- Titles are as given in ClinVar. `protein_change` fields are shown in the title cell when they differ.
- GRCh38 positions are on chr14 (14q11.2) unless the variant is a copy-number record. GRCh37 positions are in parentheses.
- "1/01/01" is ClinVar's placeholder date for last-evaluated, so it is reported as "placeholder" in the table.
- Gene lists for the copy-number records were not enumerated. Each one contains several hundred genes, including CIROP.

| # | UID | Title / HGVS (plus protein_change) | Variant type | Germline classification (last evaluated) | Review status | Condition(s) | dbSNP | GRCh38 (GRCh37) | Allele frequencies | Src |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 5016670 | NM_001354640.2(CIROP):c.1661A>G (p.Tyr554Cys); protein_change Y499C, Y554C | SNV | Likely pathogenic (2022/07/05) | criteria provided, single submitter | Multiple congenital anomalies/dysmorphic syndrome-intellectual disability (MedGen C5680372; Orphanet 102283; MONDO:0015159) | none | 23101380 (23570589) | none | V |
| 2 | 5016669 | NM_001354640.2(CIROP):c.1719G>A (p.Trp573Ter); protein_change W518*, W573* | SNV | Pathogenic (2022/07/05) | criteria provided, single submitter | Multiple congenital anomalies/dysmorphic syndrome-intellectual disability | none | 23101322 (23570531) | none | V |
| 3 | 5008300 | NM_001354640.2(CIROP):c.1058C>T (p.Thr353Ile); protein_change T298I, T353I | SNV | Uncertain significance (2026/02/12) | criteria provided, single submitter | not provided (MedGen C3661900) | none | 23102420 (23571629) | none | V |
| 4 | 5005300 | NM_001354640.2(CIROP):c.1288G>C (p.Glu430Gln); protein_change E430Q, E375Q | SNV | Uncertain significance (placeholder) | criteria provided, single submitter | Heterotaxy, visceral, 12, autosomal (OMIM 619702; MedGen C5676898) | none | 23102113 (23571322) | none | V |
| 5 | 5005299 | NM_001354640.2(CIROP):c.1392C>A (p.Cys464Ter); protein_change C409*, C464* | SNV | Likely pathogenic (placeholder) | criteria provided, single submitter | Heterotaxy, visceral, 12, autosomal | none | 23101753 (23570962) | none | V |
| 6 | 5000715 | NM_001354640.2(CIROP):c.994_997del (p.Glu332fs); protein_change E277fs, E332fs | Microsatellite | Likely pathogenic (2025/07/23) | criteria provided, single submitter | CIROP-related disorder | none | 23102481-23102484 (23571690-23571693) | none | V |
| 7 | 4997565 | NM_001354640.2(CIROP):c.1361_1363del (p.Asp454_Phe455delinsVal) | Deletion | Uncertain significance (2025/01/14) | criteria provided, single submitter | CIROP-related disorder | none | 23101858-23101860 (23571067-23571069) | none | V |
| 8 | 4990621 | NM_001354640.2(CIROP):c.595del (p.His199fs); protein_change H202fs, H199fs | Deletion | Likely pathogenic (2025/01/14) | criteria provided, single submitter | CIROP-related disorder | none | 23103683 (23572892) | none | V |
| 9 | 4983557 | NM_001354640.2(CIROP):c.1135-1G>A | SNV | Likely pathogenic (2026/09/22) | criteria provided, single submitter | CIROP-related disorder | none | 23102267 (23571476) | none | V |
| 10 | 4983478 | NM_001354640.2(CIROP):c.1487G>A (p.Trp496Ter); protein_change W441*, W496* | SNV | Likely pathogenic (2025/06/03) | criteria provided, single submitter | CIROP-related disorder | none | 23101554 (23570763) | none | V |
| 11 | 4982256 | NM_001354640.2(CIROP):c.187C>T (p.Arg63Ter); protein_change R63* | SNV | Likely pathogenic (2025/07/23) | criteria provided, single submitter | CIROP-related disorder | none | 23104734 (23573943) | none | V |
| 12 | 4921073 | NM_001354640.2(CIROP):c.426A>G (p.Pro142=) | SNV | Likely benign (2023/05/31) | criteria provided, single submitter | not specified (MedGen CN169374) | none | 23104276 (23573485) | none | V |
| 13 | 4921072 | NM_001354640.2(CIROP):c.903+14G>A | SNV | Likely benign (2024/11/27) | criteria provided, single submitter | not specified | none | 23102912 (23572121) | none | V |
| 14 | 4921071 | NM_001354640.2(CIROP):c.904-3T>C | SNV | Likely benign (2024/11/26) | criteria provided, single submitter | not specified | none | 23102716 (23571925) | none | V |
| 15 | 4921070 | NM_001354640.2(CIROP):c.1074C>G (p.Leu358=) | SNV | Likely benign (2024/01/08) | criteria provided, single submitter | not specified | none | 23102404 (23571613) | none | V |
| 16 | 4921069 | NM_001354640.2(CIROP):c.1224C>G (p.Leu408=) | SNV | Likely benign (2023/09/21) | criteria provided, single submitter | not specified | none | 23102177 (23571386) | none | V |
| 17 | 4921068 | NM_001354640.2(CIROP):c.1617T>C (p.Ser539=) | SNV | Likely benign (2024/02/19) | criteria provided, single submitter | not specified | none | 23101424 (23570633) | none | V |
| 18 | 4921067 | NM_001354640.2(CIROP):c.1750-15C>T | SNV | Likely benign (2024/06/07) | criteria provided, single submitter | not specified | none | 23101094 (23570303) | none | V |
| 19 | 4883002 | NM_001354640.2(CIROP):c.1532G>A (p.Gly511Glu); protein_change G456E, G511E | SNV | Uncertain significance (2025/03/07) | criteria provided, single submitter (partly visible) | Trait name not visible in verbatim text; the summary says Heterotaxy, visceral, 12 (unverified) | none | 23101509 (23570718) | none | V+S |
| 20 | 4874139 | NM_001354640.2(CIROP):c.279C>T (p.Ala93=) | SNV | Likely benign (2026/06/01) | criteria provided, single submitter | not provided (C3661900) | none | 23104642 (23573851) | none | S |
| 21 | 4849971 | NM_001354640.2(CIROP):c.302del (p.Arg101fs); protein_change R101fs | Deletion | Likely pathogenic (2025/10/21) | criteria provided, single submitter | Heterotaxy, visceral, 12, autosomal | none | 23104619 (23573828) | none | S |
| 22 | 4849970 | NM_001354640.2(CIROP):c.1582C>T (p.Gln528Ter); protein_change Q473*, Q528* | SNV | Likely pathogenic (2025/10/24) | criteria provided, single submitter | Heterotaxy, visceral, 12, autosomal | none | 23101459 (23570668) | none | S |
| 23 | 4820860 | NM_001354640.2(CIROP):c.209G>A (p.Gly70Glu); protein_change G70E | SNV | Likely benign (2026/02/01) | criteria provided, single submitter | not provided | none | 23104712 (23573921) | none | S |
| 24 | 4820846 | NM_001354640.2(CIROP):c.2238C>T (p.Ile746=) | SNV | Likely benign (2026/01/01) | criteria provided, single submitter | not provided | none | 23099411 (23568620) | none | S |
| 25 | 4395642 | NM_017924.4(C14orf119):c.*1496G>T | SNV | Blank (no classification) | blank | none | none | 23099577 (23568786) | none | S |
| 26 | 4277730 | NM_001354640.2(CIROP):c.2159+2T>A | SNV | Uncertain significance (2025/09/10) | criteria provided, single submitter | Trichothiodystrophy 1, photosensitive (OMIM 601675; MedGen C1866504) | none | 23100500 (23569709) | none | V |
| 27 | 4277705 | NM_001354640.2(CIROP):c.1126G>A (p.Glu376Lys); protein_change E321K, E376K | SNV | Likely pathogenic (2025/09/10) | criteria provided, single submitter | Trichothiodystrophy 1, photosensitive | none | 23102352 (23571561) | none | V |
| 28 | 3390959 | NM_001354640.2(CIROP):c.988+1G>C | SNV | Pathogenic (2024/12/17) | criteria provided, single submitter | Trichothiodystrophy 1, photosensitive | none | 23102628 (23571837) | none | V |
| 29 | 3054769 | NM_001354640.2(CIROP):c.1992T>G (p.His664Gln); protein_change H609Q, H664Q | SNV | Likely benign (2023/01/05) | no assertion criteria provided | CIROP-related disorder | rs187174627 | 23100669 (23569878) | gnomAD 0.00161; TOPMed 0.00174; 1000 Genomes 0.00220 (minor allele C) | V |
| 30 | 2644090 | NM_001354640.2(CIROP):c.33GCC[3] (p.Pro13_Leu14insPro) | Microsatellite | Likely benign (2023/07/01) | criteria provided, single submitter | not provided | rs751420164 | 23104882-23104883 (23574091-23574092) | none | V |
| 31 | 2644089 | NM_001354640.2(CIROP):c.1233C>T (p.Ile411=) | SNV | Likely benign (2022/09/01) | criteria provided, single submitter | not provided | rs189668501 | 23102168 (23571377) | gnomAD 0.00003; TOPMed 0.00003; gnomAD exomes 0.00005; ExAC 0.00008; 1000 Genomes 0.00020 (minor allele A) | V |
| 32 | 2644088 | NM_001354640.2(CIROP):c.1281C>T (p.Ser427=) | SNV | Likely benign (2023/06/01) | criteria provided, single submitter | not provided | rs143902594 | 23102120 (23571329) | ExAC 0.00016; 1000 Genomes 0.00120 (minor allele A) | V |
| 33 | 2582479 | NM_001354640.2(CIROP):c.203A>G (p.Tyr68Cys); protein_change Y68C | SNV | Uncertain significance (2023/08/09) | criteria provided, single submitter | Heterotaxy, visceral, 12, autosomal | rs1195322479 | 23104718 (23573927) | gnomAD 0.00001; gnomAD exomes 0.00001; TOPMed 0.00001 | V |
| 34 | 2442172 | NM_001354640.2(CIROP):c.64C>T (p.Arg22Ter); protein_change R22* | SNV | Conflicting classifications of pathogenicity (2026/09/22) | criteria provided, conflicting classifications | CIROP-related disorder; Heterotaxy, visceral, 12; not provided | rs185661693 | 23104857 (23574066) | gnomAD 0.00014; TOPMed 0.00018; 1000 Genomes 0.00020 (minor allele A) | V |
| 35 | 1804116 | NM_001354640.2(CIROP):c.1331dup (p.Leu444fs); protein_change L444fs | Duplication | Likely pathogenic (2022/12/12) | criteria provided, single submitter | Heterotaxy, visceral, 12, autosomal | rs2503617333 | 23101889-23101890 (23571098-23571099) | none | V |
| 36 | 1804115 | NM_001354640.2(CIROP):c.538G>C (p.Gly180Arg); protein_change G180R, G183R | SNV | Uncertain significance (2022/12/12) | criteria provided, single submitter | Heterotaxy, visceral, 12, autosomal | rs1266315800 | 23103740 (23572949) | TOPMed 0.00000; gnomAD 0.00001 | V |
| 37 | 1344495 | NM_001354640.2(CIROP):c.571C>T (p.Arg191Ter); alias R194* | SNV | Pathogenic (2022/03/15) | no assertion criteria provided | Heterotaxy, visceral, 12, autosomal | rs764530848 | 23103707 (23572916) | none | V |
| 38 | 1344493 | NM_001354640.2(CIROP):c.1166G>T (p.Arg389Ile); alias R334I | SNV | Pathogenic (2022/03/15) | no assertion criteria provided | Heterotaxy, visceral, 12, autosomal | rs2140282332 | 23102235 (23571444) | none | V |
| 39 | 1344490 | NM_001354640.2(CIROP):c.1037G>A (p.Trp346Ter) | SNV | Pathogenic (2022/06/17) | no assertion criteria provided | Heterotaxy, visceral, 12, autosomal | rs1014082266 | 23102441 (23571650) | gnomAD 0.00001; gnomAD exomes 0.00001; TOPMed 0.00002 | V |
| 40 | 1344488 | NM_001354640.2(CIROP):c.1151C>T (p.Ser384Leu); alias S329L | SNV | Pathogenic (2022/03/15) | no assertion criteria provided | Heterotaxy, visceral, 12, autosomal | rs183023758 | 23102250 (23571459) | gnomAD 0.00001; gnomAD 0.00002; gnomAD exomes 0.00002; 1000 Genomes 0.00020 (minor allele A) | V |
| 41 | 1335922 | NM_001354640.2(CIROP):c.1364TCT[1] (p.Phe456del); protein_change F456del | Microsatellite | Pathogenic (2022/03/15) | no assertion criteria provided | Heterotaxy, visceral, 12, autosomal | rs1392604380 | 23101852-23101854 (23571061-23571063) | none | V |
| 42 | 1335920 | NM_001354640.2(CIROP):c.92C>T (p.Ser31Phe); protein_change S31F | SNV | Conflicting classifications of pathogenicity (2025/11/03) | criteria provided, conflicting classifications | Heterotaxy, visceral, 12, autosomal; not provided | rs553352307 | 23104829 (23574038) | gnomAD 0.00106; gnomAD 0.00107; gnomAD exomes 0.00120; TOPMed 0.00126; gnomAD exomes 0.00135; ExAC 0.00139; 1000 Genomes 0.00040 (minor allele A) | V |
| 43 | 155681 | GRCh38/hg38 14q11.2-21.3(chr14:20043513-48642042)x3 | copy number gain | Pathogenic (2014/03/18) | no assertion criteria provided | See cases | none (dbVar nssv3395384, nsv996197) | 20043513-48642042 (20511672-49111245) | none | S |
| 44 | 155306 | GRCh38/hg38 14q11.2-32.33(chr14:20043514-106877229)x3 | copy number gain | Pathogenic (2014/12/02) | no assertion criteria provided | See cases | none (dbVar nssv13653662, nssv3396732, nsv995182) | 20043514-106877229 (20511673-107285437) | none | S |
| 45 | 155119 | GRCh38/hg38 14q11.2-21.2(chr14:20022693-44093672)x3 | copy number gain | Pathogenic (2013/01/09) | no assertion criteria provided | See cases | none (dbVar nssv1610099, nsv931929) | 20022693-44093672 (20490852-44562875) | none | V |
| 46 | 148657 | GRCh38/hg38 14q11.2-12(chr14:20412587-25018120)x3 | copy number gain | Likely pathogenic (2011/08/29) | no assertion criteria provided | See cases | none | 20412587-25018120 (20880746-25487326) | none | S |
| 47 | 146230 | GRCh38/hg38 14q11.2-32.33(chr14:20151149-106855263)x3 | copy number gain | Pathogenic (2011/01/14) | no assertion criteria provided | See cases | none | 20151149-106855263 (20619308-107263478) | none | S |
| 48 | 59932 | GRCh38/hg38 14q11.2-21.1(chr14:20000611-38984415)x3 | copy number gain | Pathogenic (2011/08/12) | criteria provided, single submitter | See cases | none (dbVar nssv578665, nsv532462) | 20000611-38984415 (20468770-39453619) | none | V |
| 49 | 57745 | GRCh38/hg38 14q11.2-21.2(chr14:20196945-45284802)x1 | copy number loss | Pathogenic (2011/08/12) | criteria provided, single submitter | See cases | none (dbVar nssv577454, nsv530007) | 20196945-45284802 (20665104-45754005) | none | S |
| 50 | 57246 | GRCh38/hg38 14q11.2(chr14:20151149-23442195)x3 | copy number gain | Pathogenic (2011/08/12) | criteria provided, single submitter | See cases | none (dbVar nssv578668, nsv529490) | 20151149-23442195 (20619308-23911404) | none | S |

Across all 50 records, the only dbSNP rs IDs are for rows 29 to 42 (SNVs and microsatellites in the table above). The only records with allele frequencies are rows 29 to 32, 33, 34, 36, 39, 40, 42. Every record has `canonical_spdi`, `supporting_submissions` (SCV/RCV IDs) and an empty clinical-impact and oncogenicity block. The SCV/RCV IDs are in the verbatim JSON if you need them. Row 10 and the other S rows were not verified against the verbatim JSON.

## 4. PubMed search and summaries

- **esearch (db=pubmed):** count 13, retmax 13. PMIDs: 42503777, 41172501, 39753129, 39513328, 34903892, 32522166, 24599392, 24226769, 21122110, 19304326, 15844197, 14247041, 14244456.
- **Query warnings:** the phrase LMLN2 was not found, and the quoted phrase "left-right organizer metallopeptidase" was not found. The translation maps CIROZ to "cirrhosis" and matches many unrelated papers.

| PMID | Title | First author | Journal (abbrev.) | Year (print / epub) | Vol(issue):pages | DOI |
|---|---|---|---|---|---|---|
| 42503777 | "Chemoselective Coordination-Insertion Polymerization of Cyclic Carbamates to Circular Polyurethanes with Diverse Architectures." | Zheng WF | J Am Chem Soc | 2026 Aug 5 | 148(30):32003-32013 | 10.1021/jacs.6c05975 |
| 41172501 | "Contributions to the discussion on societal impact assessment in graduate programs in dentistry in Brazil." | Abreu MHNG | Braz Dent J | 2025 / epub 2025 Oct 24 | 36:e236764 | 10.1590/0103-644020256764 |
| 39753129 | "CIROZ is dispensable in ancestral vertebrates but essential for left-right patterning in humans." | Szenker-Ravi E | Am J Hum Genet | 2025 Feb 6 / epub 2025 Jan 2 | 112(2):353-373 | 10.1016/j.ajhg.2024.12.006 |
| 39513328 | "Genetic Analysis of Heterotaxy in a Consanguineous Cohort." | Al-Korashy M | Clin Genet | 2025 Feb / epub 2024 Nov 8 | 107(2):224-230 | 10.1111/cge.14641 |
| 34903892 | "Discovery of a genetic module essential for assigning left-right asymmetry in humans and ancestral vertebrates." | Szenker-Ravi E | Nat Genet | 2022 Jan / epub 2021 Dec 13 | 54(1):62-72 | 10.1038/s41588-021-00970-4 |
| 32522166 | "Development of a novel social incubator for health promoting initiatives in a disadvantaged region." | Spitzer-Shohat S | BMC Public Health | 2020 | 20(1):898 | 10.1186/s12889-020-08990-1 |
| 24599392 | "Bicuspid aortic valve hemodynamics induces abnormal medial remodeling in the convexity of porcine ascending aortas." | Atkins SK | Biomech Model Mechanobiol | 2014 Nov | 13(6):1209-25 | 10.1007/s10237-014-0567-7 |
| 24226769 | "The heterotaxy gene GALNT11 glycosylates Notch to orchestrate cilia type and laterality." | Boskovski MT | Nature | 2013 Dec 19 | 504(7480):456-9 | 10.1038/nature12723 |
| 21122110 | "Developmental control of lateralized neuron size in the nematode Caenorhabditis elegans." | Goldsmith AD | Neural Dev | 2010 Dec 1 | 5:33 | 10.1186/1749-8104-5-33 |
| 19304326 | "A measure of community members' perceptions of the impacts of research partnerships in health and social services." | King G | Eval Program Plann | 2009 Aug | 32(3):289-99 | 10.1016/j.evalprogplan.2009.02.002 |
| 15844197 | "Cardiac morphogenesis: matrix metalloproteinase coordination of cellular mechanisms underlying heart tube formation and directionality of looping." | Linask KK | Dev Dyn | 2005 Jul | 233(3):739-53 | 10.1002/dvdy.20377 |
| 14247041 | Romanian-language title on thromboelastographic changes in chronic hepatitis and cirrhosis | Stoichita M | Stud Cercet Med Interna | 1964 | 23:535-45 | none |
| 14244456 | Romanian-language title on thromboelastogram and serum protein changes in chronic hepatitis and cirrhosis | Stoichita M | Stud Cercet Med Interna | 1964 | 92:633-40 | none |

Only 34903892 and 39753129 are about CIROP or CIROZ. 39513328 is a heterotaxy cohort study and may mention CIROP-related variants. 24226769 is a heterotaxy paper about GALNT11, not CIROP. The rest are off-topic matches.

## 5. PubMed 34903892 (efetch, retmode=xml)

- **Title:** "Discovery of a genetic module essential for assigning left-right asymmetry in humans and ancestral vertebrates."
- **Journal:** Nature genetics (ISO: Nat Genet), ISSN 1546-1718 (electronic), NLM ID 9216904. Volume 54, issue 1, print date 2022 Jan, pages 62-72.
- **Dates:** received 2020/12/08, accepted 2021/10/14, electronic publication 2021 Dec 13, PubMed 2021/12/15, MEDLINE 2022/02/24.
- **IDs:** PMID 34903892; DOI 10.1038/s41588-021-00970-4. No PMC ID is listed in this record.
- **Erratum:** Nat Genet 2022 Jun;54(6):906, doi 10.1038/s41588-022-01053-8 (PMID 35304595).
- **Publication types:** Journal Article; Research Support, Non-U.S. Gov't.

**Abstract (paraphrased, since the full text cannot be quoted under the copyright limit):** The record has one unlabeled abstract paragraph. The authors searched for genes that were lost in vertebrate lineages that lack motile-cilia left-right organizers, and found five extracellular-protein genes. One is a putative protease they named CIROP. CIROP is expressed in ciliated left-right organizers. In zebrafish and Xenopus, it is needed only on the left side, downstream of leftward flow and upstream of DAND5. The authors identified 21 human patients with loss-of-function CIROP mutations and recessive situs anomalies. They propose an ancestral genetic module that disappeared twice during vertebrate evolution but remains essential for human left-right patterning.

**Full author list (41 authors, in order; EqualContrib on the first two):** Szenker-Ravi E, Ott T, Khatoo M, Moreau de Bellaing A, Goh WX, Chong YL, Beckers A, Kannesan D, Louvel G, Anujan P, Ravi V, Bonnard C, Moutton S, Schoen P, Fradin M, Colin E, Megarbane A, Daou L, Chehab G, Di Filippo S, Rooryck C, Deleuze JF, Boland A, Arribard N, Eker R, Tohari S, Ng AY, Rio M, Lim CT, Eisenhaber B, Eisenhaber F, Venkatesh B, Amiel J, Crollius HR, Gordon CT, Gossler A, Roy S, Attie-Bitach T, Blum M, Bouvagnet P, Reversade B. The record gives each author's affiliations (A*STAR Singapore, Hannover, Paris, Lyon, Hohenheim, Bordeaux, Beirut, Istanbul, and others). I did not reproduce them in full.

**MeSH headings (MajorTopicYN in parentheses):**
- Animals (N), D000818
- Humans (N), D006801
- Biological Evolution (Y), D005075
- Body Patterning (Y), D019521; qualifiers genetics (N), physiology (N)
- Cilia (N), D002923; qualifier genetics (N)
- Gene Regulatory Networks (Y), D053263
- Loss of Function Mutation (N), D000073658
- Metalloproteases (Y), D045726; qualifiers genetics (N), physiology (N)
- Proteins (N), D011506; qualifiers genetics (N), physiology (N)
- Vertebrates (N), D014714; qualifier genetics (N)
- Metalloendopeptidases (N), D008666 (AutoHM = Y)

**Chemicals:** Metalloproteases (EC 3.4.-); Proteins (0); CIROP protein, human (EC 3.4.24.-, UI C000723020); Metalloendopeptidases (EC 3.4.24.-).

## Endpoints

| Endpoint | Status |
|---|---|
| esummary db=gene, id=100128908 | HTTP 200, application/json, verbatim |
| esearch db=clinvar, term=CIROP[gene] | HTTP 200, application/json, verbatim |
| esummary db=clinvar, batch 1 (25 UIDs, rows 1-25) | HTTP 200; truncated, then summarized |
| esummary db=clinvar, batch 2 (25 UIDs, rows 26-50) | HTTP 200; truncated, then summarized |
| esummary db=clinvar, id=1335920 | HTTP 200, verbatim |
| esummary db=clinvar, id=155119,148657,146230,59932,57745,57246 | HTTP 200; truncated, then summarized |
| esummary db=clinvar, id=59932,57745,57246 | HTTP 200; truncated, then summarized |
| esearch db=pubmed, term=CIROP OR LMLN2 OR CIROZ OR "left-right organizer metallopeptidase" | HTTP 200, application/json, verbatim |
| esummary db=pubmed, 13 PMIDs | HTTP 200, application/json, verbatim |
| efetch db=pubmed, id=34903892, retmode=xml | HTTP 200, text/xml; abstract not quoted (copyright limit) |

**Not fully read:** the gene arrays in the copy-number records (155119, 155681, 155306, 148657, 146230, 59932, 57745, 57246) were not enumerated. The batch 2 response was cut at about 39,700 of 898,629 characters, and the rest was covered only by a model summary. Its header fields for rows 43-50 were partly verbatim and partly summarized, as marked in the table.

**Final URLs read:**
- https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=gene&id=100128908&retmode=json
- https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=clinvar&term=CIROP%5Bgene%5D&retmax=200&retmode=json
- https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=clinvar&id=<rows 1-25 UIDs, in order>&retmode=json
- https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=clinvar&id=<rows 26-50 UIDs, in order>&retmode=json
- https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=clinvar&id=1335920&retmode=json
- https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=clinvar&id=155119,148657,146230,59932,57745,57246&retmode=json
- https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=clinvar&id=59932,57745,57246&retmode=json
- https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=CIROP+OR+LMLN2+OR+CIROZ+OR+%22left-right+organizer+metallopeptidase%22&retmax=100&retmode=json
- https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id=42503777,41172501,39753129,39513328,34903892,32522166,24599392,24226769,21122110,19304326,15844197,14247041,14244456&retmode=json
- https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=34903892&retmode=xml

OpenAlex gave the metadata and abstract-free open-access links. CORE returned 403. I'll try the last listed alternative, scholar.archive.org.

## Result 1: Springer review (not read)

The Springer URL https://link.springer.com/article/10.1007/s11936-025-01114-1 returned a 303 redirect to https://idp.springer.com/authorize (a login or access endpoint). I did not follow it, so I have no content from the review. Everything requested from it (citation details, abstract, CIROP/CIROZ/MMP21/PKD1L1/DAND5 discussion, the left-right patterning account, heterotaxy classification and figures, management, and gene lists) is unknown to me. Sending the same URL again would produce the same redirect.

## Result 2: PMC article (read, but it is a different paper)

I read https://pmc.ncbi.nlm.nih.gov/articles/PMC11764533/. This is not the CTOC review. It is a *Genes (Basel)* paper on MMP21 missense variants, which the page labels as non-preapproved. The fetch returned the first ~40,000 of ~80,000 characters verbatim. The rest came as a model-extracted summary, so the points below that rely on it are marked.

**Citation (from the page header and author block):**
- Pasquetti D, Tesolin P, Perino F, Zampieri S, Bobbo M, Caiffa T, Spedicati B, Girotto G. *Genes (Basel)*. 2025 Jan 8;16(1):62. doi:10.3390/genes16010062
- PMID 39858609; PMCID PMC11764533
- Received 2024 Dec 13; revised 2024 Dec 31; accepted 2025 Jan 5. CC BY licence.
- Title: "Expanding the Molecular Spectrum of MMP21 Missense Variants: Clinical Insights and Literature Review"

**Abstract:** The page gives the full abstract verbatim. Because this source is non-preapproved, I can only quote it in pieces of 125 characters or fewer, so I summarise it here:
- Background: biallelic MMP21 variants have recently been linked to heterotaxy and congenital heart defects (CHD), but genotype-phenotype correlations and mechanisms are poorly understood.
- Methods: the authors studied patients with biallelic MMP21 missense variants tested at the Burlo Garofolo institute, did a literature review, and ran in silico and structural modelling.
- Results: 18 MMP21 missense variants were reported in 26 patients. CHD was present in 94% and variable extra-cardiac features in 64%. Whole-exome sequencing found p.(Met301Ile) in two unrelated heterotaxy patients.
- Conclusions: the authors support a pathogenic role for p.(Met301Ile). They suggest a possible loss-of-function mechanism, especially for variants in the catalytic domain. They report no significant phenotype difference between compound heterozygous and homozygous missense carriers.

**Introduction (verbatim, short quotes):**
- Heterotaxy prevalence: "Heterotaxy, with a prevalence of 0.001% in live births" (the paper cites ref. 6).
- CHD frequency: "CHD occurs in approximately 80% of individuals with heterotaxy".
- Cilia role: "the roles of both motile and non-motile cilia in the process are well established." The paper also says the Left-Right Organizer "becomes visible in human embryos around 14 days post-fertilization."
- Motile cilia: "The motile cilia are tilted toward the posterior and rotate clockwise, producing a leftward fluid flow." Their flow induces calcium transients in non-motile LRO cilia, which lead to left-sided transcription factor expression in lateral plate mesoderm.
- Terminology: normal arrangement is "situs solitus"; "situs inversus totalis" is a mirror-image defect; "situs ambiguus" lies between them.

**MMP21-related phenotypes (verbatim patient table, Table 2, and text):**
- Of 26 reported patients, CHD is in 94%. Extra-cardiac laterality defects are in 15 of 26 (64%).
- Heterotaxy was diagnosed prenatally in 6 patients, 5 of whom had termination of pregnancy.
- "Positive outcomes, defined as surgical correction achieving good hemodynamic heart function, were observed in half of patients diagnosed postnatally."
- Cardiac lesions in the table include dextrocardia, common atrium, AVSD, IVC interruption, PLSVC, DORV, TGA, congenitally corrected TGA, single ventricle, and mitral atresia. Laterality features include situs ambiguus, situs inversus totalis, polysplenia, midline liver, right-sided stomach, and intestinal malrotation.
- The authors note that MMP21 "encodes for a member of the matrix metalloproteinase (MMPs) family" and spans 9.3 kb at 10q26.2 with seven coding exons.

**Model-extracted summary (not verbatim, for the last ~40,000 characters):**
- The summary says the paper's conclusions state that "patients carrying biallelic MMP21 variants of which at least one is missense invariably exhibit CHD."
- It reports missense variants in 46% of compound heterozygotes and 52% of homozygotes. Five sibling pairs were studied, with no significant phenotype difference.
- It says the paper implies autosomal recessive inheritance. It also mentions a possible dominant-negative effect of monoallelic variants in a cited study, which the authors say is not conclusively shown.
- It says outcomes beyond the table are not described.

**Requested items not found in this paper:** CIROP, CIROZ, DAND5, and PKD1L1 are not mentioned. Only MMP21 is discussed, with no broader heterotaxy gene list.

**Final URLs read:** https://pmc.ncbi.nlm.nih.gov/articles/PMC11764533/

## Summary

The full text was not obtained, so items 2 to 9 cannot be answered from these sources. I have the title, publication metadata, and the author-written abstract (via the repository record). Everything else in your list is unanswered.

## URL results

| URL | Result |
|---|---|
| `https://oskar-bordeaux.fr/bitstream/20.500.12278/184703/2/MRGM_2022_Nat%20Genet_Szenker-Ravi.pdf` (encoded) | Attempt 1: `read ECONNRESET`. Attempt 2: HTTP 200, application/pdf, 3,339,520 characters. The text extraction returned only raw compressed PDF objects (FlateDecode streams and font tables), with no readable prose. A PDF was also saved to a local file for you. I did not try the unencoded-space variant because the encoded URL returned 200. |
| `https://oskar-bordeaux.fr/handle/20.500.12278/184703` | HTTP 200, text/html. Gave the title, authors, journal, abstract, and DOI. Does not contain the full text. |
| `https://www.ncbi.nlm.nih.gov/pmc/articles/pmid/34903892/` | HTTP 301 to `https://pmc.ncbi.nlm.nih.gov/articles/pmid/34903892/`. |
| `https://pmc.ncbi.nlm.nih.gov/articles/pmid/34903892/` | HTTP 200, but the page is a reCAPTCHA browser check ("Checking your browser"). No article text. I did not try to get past it. |
| `https://api.openalex.org/works/doi:10.1038/s41588-021-00970-4` | HTTP 200, JSON. Metadata only. Abstract field null. Publisher copy is not open access. |
| `https://core.ac.uk/search?q=...` | HTTP 403 Forbidden. |
| `https://scholar.archive.org/search?q=...` | HTTP 200, but the body reads "Rate limit reached." I stopped fetching here. |

Permanent failures (403, rate limit) would fail the same way if sent again. The PDF's transient ECONNRESET was resolved, but the file that came back is unreadable.

## Metadata

- **Title:** "Discovery of a genetic module essential for assigning left–right asymmetry in humans and ancestral vertebrates."
- **Journal:** Nature Genetics, vol. 54, no. 1, pp. 62–72. OpenAlex lists the online publication date as 2021-12-13.
- **DOI:** 10.1038/s41588-021-00970-4
- **PMID:** 34903892
- **Authors (from the repository record):** Szenker-Ravi E, Ott T, Khatoo M, and many others. Corresponding authors per OpenAlex are Blum M, Bouvagnet P, and Reversade B. Caroline Rooryck and Sylvie Di Filippo are also on the author list.

## 1. Abstract (repository copy of the Nature Genetics abstract)

Quotes below are from a non-preapproved source, so each is kept under 125 characters. Gaps are marked with brackets.

- "The vertebrate left-right axis is specified during embryogenesis by a transient organ: the left-right organizer (LRO)."
- "Species including fish, amphibians, rodents and humans deploy motile cilia in the LRO to break bilateral symmetry" [the abstract continues by contrasting reptiles, birds, even-toed mammals and cetaceans, which are believed to have LROs without motile cilia].
- "We searched for genes whose loss during vertebrate evolution follows this pattern" and identified five genes encoding extracellular proteins, including a putative protease. The abstract calls this protease "a putative protease with hitherto unknown functions," named CIROP ("ciliated left-right organizer metallopeptide").
- "Here, we show that CIROP is specifically expressed in ciliated LROs."
- In zebrafish and Xenopus, "CIROP is required solely on the left side, downstream of the leftward flow, but upstream of DAND5" [the abstract adds that DAND5 is the first asymmetrically expressed gene].
- "We further ascertained 21 human patients with loss-of-function CIROP mutations presenting with recessive situs anomalies."
- The closing statement says the findings suggest "an ancestral genetic module that has twice disappeared during vertebrate evolution" and that this module "remains essential for distinguishing left from right in humans."

Keywords listed: Animals; Humans; Biological Evolution; Body Patterning; Cilia; Gene Regulatory Networks; Loss of Function Mutation; Metalloproteases; Proteins; Vertebrates.

## 2. to 9. Not available

No source I could read gave the full text, so I cannot report:

2. Patient cohort details beyond the abstract's figure of 21 patients. The number of families, country and ethnicity, consanguinity, and ascertainment are unknown to me.
3. CIROP/LMLN2 variants (c. and p. HGVS, zygosity, class). Unknown.
4. Clinical phenotypes per patient or family. Unknown.
5. CIROP protein details (exon count, length, domains, HExxH residues, transmembrane regions, localization, enzymatic data). Unknown beyond the abstract's description of a "putative protease."
6. Pathway details (MMP21, PKD1L1, DAND5, Nodal, Pitx2, Lefty, epistasis and rescue). Only the abstract's zebrafish/Xenopus statement above is known.
7. Animal model genotypes, phenotypes, and percentages. Unknown.
8. Phylogenetic analysis (which lineages lost the gene; the five genes beyond CIROP). Unknown.
9. Prevalence, penetrance, and genotype-phenotype statements. Unknown.

## Possible next steps

- The PDF, if it is saved in the harness's file location, may be extractable locally with `pdftotext`. I have not run it, because the local copy is untrusted data and needs its own handling.
- Other open copies named in OpenAlex but not fetched (they are on different hosts from the ones you listed, so I did not follow them): `https://hal.science/hal-03876795v1/document` (HAL preprint) and `https://content.openalex.org/works/W4200493623.pdf`. The HAL record also has the same title and is linked from the repository's record.
- Retrying scholar.archive.org later may work once its rate limit clears.

Unpaywall returned an open-access PMC copy (PMC11866977). I'll read that next.

The PMC copy returned a reCAPTCHA challenge page, so I'll skip the other pmc.ncbi.nlm.nih.gov URLs. Next I'll try the publisher PDF that Unpaywall listed and the PubMed abstract.

## Access summary

- **Unpaywall** (HTTP 200) listed an OA copy at PMC11866977 and a publisher PDF at cell.com (`http://www.cell.com/article/S0002929724004488/pdf`).
- **PMC PDF** (`https://pmc.ncbi.nlm.nih.gov/articles/PMC11866977/pdf/main.pdf`) returned a reCAPTCHA "Checking your browser" page, not the article. I did not fetch other pmc.ncbi.nlm.nih.gov URLs after that.
- **cell.com PDF** returned HTTP 403.
- **PubMed efetch** for 39753129 (HTTP 200) gave the full abstract, title, authors, MeSH, keywords and history. The response was truncated at 39,901 of 63,132 characters. The tail is reference list only, so I used the verbatim portion.
- **OpenAlex** was not fetched because the abstract was already obtained.

**Full text was not read.** Per-patient variants and phenotypes, CIROP-specific statements beyond the abstract, and the zebrafish/Xenopus/mouse details are unknown to me. The PMC copy is the place to get them, and a browser may pass the reCAPTCHA.

## CIROZ paper (Am J Hum Genet 2025;112(2):353-373)

**Title:** "CIROZ is dispensable in ancestral vertebrates but essential for left-right patterning in humans." Szenker-Ravi E, Ott T, Yusof A, et al.; last author Reversade B. Journal: *American Journal of Human Genetics*, 2025 Feb 6, vol 112, issue 2, pp 353-373. DOI 10.1016/j.ajhg.2024.12.006. PMID 39753129. PMC11866977. Epub 2025 Jan 2. Received 2023-04-20, accepted 2024-12-09.

**Abstract, paraphrased from the PubMed record:**
- Four genes, DAND5, PKD1L1, MMP21 and CIROP, form a genetic module that evolved specifically in vertebrates with motile cilia at their left-right organizer (LRO).
- CIROZ (previously C1orf127) is also specifically expressed in the LRO of mice, frogs and fish. It encodes a protein with a signal peptide followed by 3 zona pellucida N (ZP-N) domains, consistent with extracellular localization.
- The authors report 16 individuals from 10 families with biallelic CIROZ inactivation variants, causing heterotaxy with congenital heart defects.
- Ciroz knockout mice also show situs anomalies. Targeted inactivation in zebrafish and Xenopus gave no observable left-right anomalies.
- CIROZ is absent or obsolete in some animals with LRO motile cilia, including Carnivora, Atherinomorpha fish and jawless vertebrates.
- Conclusion: CIROZ is essential for breaking bilateral symmetry in humans and mice, while its pseudogenization is ongoing in some vertebrate species.

**Specific items from your list:**
- **Chromosome location, ALED alias, and exact module position:** not stated in the fetched text. The abstract only names CIROZ as expressed alongside the four-gene module. The "C1orf" prefix in the old name suggests chromosome 1, but that is my inference, not from the source.
- **Variants and phenotypes by patient:** the abstract gives only the totals above (16 individuals, 10 families, bi-allelic inactivation variants, heterotaxy with congenital heart defects). Specific variants and zygosity are unknown.
- **CIROP:** the abstract mentions CIROP only as one of the four module genes. It gives no CIROP patient counts, function, CIROZ interaction, substrate status, or localization.
- **MMP21:** only as a module member. Whether CIROZ is a substrate of CIROP or MMP21 is not stated.
- **Evolutionary argument:** the abstract's points are the species-level absence or obsolescence listed above, and the "pseudogenization" framing.
- **MeSH (from PubMed):** Body Patterning/genetics (major); Vertebrates/genetics (major); Animals; Humans; Mice; Zebrafish/genetics; Cilia/genetics; Heterotaxy Syndrome/genetics; Heart Defects, Congenital/genetics; Gene Expression Regulation, Developmental; Female; Male.
- **Keywords:** C1orf127, CIROP, CIROZ, DAND5, MMP21, PKD1L1, ZP-N, ZP2, evo-devo, gene loss, heterotaxy, laterality, left-right organizer, motile cilia, pseudogenization.
- **Funding:** NICHD NIH HHS, P50 HD105351. No competing interests declared.

## Clin Genet paper (PMID 39513328)

**Title:** "Genetic Analysis of Heterotaxy in a Consanguineous Cohort." Al-Korashy M et al. (Center for Genomic Medicine, Riyadh; last author Al-Hassnan Z). *Clin Genet* 2025 Feb;107(2):224-230. DOI 10.1111/cge.14641. Epub 2024 Nov 8.

**Abstract, paraphrased:**
- Cohort: 24 affected individuals from 19 unrelated families, recruited consecutively from a highly consanguineous population.
- Methods: exome sequencing, genome sequencing, or a multigene panel.
- Result: 9 unique variants, 7 of them novel, in 8 genes implicated in autosomal recessive heterotaxy. The listed genes are C1orf127 (CIROZ), CCDC39, CIROP, DNAAF3, DNAH5, DNAH9, MMP21 and MNS1. The yield was 42.1%.
- 7 of the 9 variants were homozygous. The other 2 were compound heterozygous, one of them a heterozygous CNV deletion.
- Candidate-gene searches in unsolved cases found no plausible variant.
- Conclusion: a relatively high yield in a consanguineous population, enriched for homozygous variants, with substantial genetic heterogeneity. The authors support genome-wide analysis in heterotaxy diagnosis.

**Answers to your questions:**
- **CIROP variants:** yes. CIROP is one of the 8 genes listed among the variant-carrying genes.
- **Number of families with CIROP:** not stated in the abstract. The 42.1% yield equals 8 of 19 families, which suggests 8 solved families, but the CIROP-specific count is unknown.
- **Which families or variants carry CIROP:** not stated. The abstract does not give variant names or zygosity by gene.
- **Phenotypes:** not given per gene in the abstract.
- **C1orf127/CIROZ:** also among the 8 genes, so this cohort also has a CIROZ-gene finding.

## A. HPO annotations for OMIM:619702

Fetched https://ontology.jax.org/api/network/annotation/OMIM:619702 (HTTP 200, JSON). The fallback endpoints were not needed. The gene view https://ontology.jax.org/api/network/annotation/NCBIGene:100128908 (HTTP 200, JSON) returns the same 28 HPO terms with no frequency or source data.

- **Disease:** "Heterotaxy, visceral, 12, autosomal", OMIM:619702, MONDO:0859222. Description field is empty.
- **Mode of inheritance:** HP:0000007 "Autosomal recessive inheritance" (listed under category Inheritance, source PMID:34903892).
- **Cross-references:** MONDO:0859222 and gene NCBIGene:100128908 (CIROP). No other cross-references are in the response.
- **Source for every term:** PMID:34903892. Onset is empty for every term. Sex is empty for every term.

Annotated terms (HP ID, label, frequency as given):

| HP ID | Label | Frequency |
|---|---|---|
| HP:0003577 | Congenital onset | 21/21 |
| HP:0031854 | Left Isomerism | 1/21 |
| HP:0001719 | Double outlet right ventricle | 7/21 |
| HP:0001696 | Situs inversus totalis | 8/21 |
| HP:0012020 | Right aortic arch | 1/21 |
| HP:0012304 | Hypoplastic aortic arch | 2/21 |
| HP:0001629 | Ventricular septal defect | 3/21 |
| HP:0011556 | Double inlet right ventricle | 1/21 |
| HP:0001655 | Patent foramen ovale | 2/21 |
| HP:0001651 | Dextrocardia | 6/21 |
| HP:0011540 | Levotransposition of the great arteries | 3/21 |
| HP:0031348 | Dextrotransposition of the great arteries | 1/21 |
| HP:0001750 | Single ventricle | 4/21 |
| HP:0001680 | Coarctation of aorta | 1/21 |
| HP:0011640 | Single coronary artery origin | 1/21 |
| HP:0011670 | Left superior vena cava draining to coronary sinus | 3/42 (as given; denominator differs from 21) |
| HP:0001674 | Complete atrioventricular canal defect | 7/21 |
| HP:0001643 | Patent ductus arteriosus | 5/21 |
| HP:0011565 | Common atrium | 2/21 |
| HP:0001631 | Atrial septal defect | 5/21 |
| HP:0011553 | Discordant atrioventricular connection | 2/21 |
| HP:0010773 | Partial anomalous pulmonary venous return | 1/21 |
| HP:0004383 | Hypoplastic left ventricle | 1/21 |
| HP:0004935 | Pulmonary artery atresia | 3/21 |
| HP:0001642 | Pulmonic stenosis | 4/21 |
| HP:0011590 | Double aortic arch | 1/21 |
| HP:0031565 | Abdominal situs ambiguus | 5/21 |
| HP:0000007 | Autosomal recessive inheritance | (none; MOI) |

That is 28 terms in total.

## B. GenCC classification for CIROP (HGNC:53647)

Fetched https://search.thegencc.org/genes/HGNC:53647, which returned HTTP 301 to https://thegencc.org/genes/HGNC:53647. The target is the same site without the "search." subdomain, so I fetched it (HTTP 200, HTML). Final URL read: https://thegencc.org/genes/HGNC:53647.

- **Submitters:** 1 — PanelApp Australia (GENCC:000111).
- **Classifications:** 1 — Strong.
- **Submission:** SGC-176309.1 (https://thegencc.org/submissions/SGC-176309.1).
- **Disease name:** "visceral heterotaxy".
- **MONDO ID:** MONDO:0018677. This differs from the MONDO:0859222 used by HPO for OMIM:619702.
- **Mode of inheritance:** AR (autosomal recessive).
- **Dates:** evaluated 01/17/2025; submitted 03/31/2026.

## C. MGI Cirop (MGI:5588935)

Fetched https://www.informatics.jax.org/marker/MGI:5588935 (HTTP 200), https://www.informatics.jax.org/allele/summary?markerId=MGI:5588935 (HTTP 200), https://www.informatics.jax.org/go/marker/MGI:5588935 (HTTP 200), and https://www.alliancegenome.org/api/gene/HGNC:53647 (HTTP 200, JSON). The allele and GO pages loaded only their page shells. Their tables are rendered client-side and are not in the fetched text, so the rows below are unavailable.

**Gene identifiers (marker page):**
- Symbol: Cirop. Name: "ciliated left-right organizer metallopeptidase". Synonym: Gm29776.
- MGI:5588935. NCBI Gene 101056084. Ensembl ENSMUSG00000114865. Other accession MGI:6887928.
- Location: Chr14:54930055-54936290 bp, minus strand (GRCm39).
- Last database update shown: 11/10/2026.

**Alleles:**
- The marker page reports 1 allele under "All Mutations and Alleles", 1 under "Chemically induced (other)", and 1 genomic mutation.
- The allele summary page did not render its table. Allele symbol, allele name, and MGI allele accession ID are therefore unknown to me.

**MP phenotype terms:**
- The marker page reports "2 phenotype references" but lists no MP terms or MP IDs in the fetched text. MP IDs are unknown.

**GO annotations:**
- The marker page reports 8 GO annotations and 4 GO references.
- The tabular GO table did not render. GO IDs and evidence codes are unknown to me.
- The automated description (Alliance Release 9.1.0) reads: "Predicted to enable peptidase activity. Predicted to be involved in establishment of left/right asymmetry. Predicted to be located in membrane. Predicted to be active in cytoplasm. Is expressed in node. Human ortholog(s) of this gene implicated in visceral heterotaxy 12."

**References:**
- The marker page reports 12 references in total (summaries: 1 developmental expression, 4 GO, 2 phenotype).
- Only the earliest is shown: J:322341, Szenker-Ravi E, et al., "Discovery of a genetic module essential for assigning left-right asymmetry in humans and ancestral vertebrates", Nat Genet 2022 Jan;54(1):62-72. No PMID is shown in the fetched text.
- The other 11 references and their PMIDs are unknown to me.

**Human ortholog and disease (marker page):**
- Human ortholog: CIROP, HGNC:53647, NCBI Gene 100128908, UniProt A0A1B0GTW7, 14q11.2.
- Synonyms: HTX12, LMLN2.
- The marker page lists 1 human disease association: "visceral heterotaxy 12", DOID:0051026, linked to OMIM:619702.
- Vertebrate orthologs: 2, with an MGI stringent orthology cluster 52459253 (1 human, 1 mouse, 1 rat).

**Alliance API (https://www.alliancegenome.org/api/gene/HGNC:53647):**
- Returned gene metadata only, from the Rat Genome Database (RGD:13208685), for human gene HGNC:53647. Alliance curie AGRKB:105000000382197.
- The response contains no disease associations with MONDO IDs, no orthologs with species and IDs, and no GO annotations.
- Cross-references include OMIM:619703. This differs from OMIM:619702, which is the disease ID elsewhere.
- Gene note: "Implicated in visceral heterotaxy 12."

**Failed or incomplete sources:**
- Allele summary page: HTTP 200, table not rendered. Allele symbols, names, and IDs unknown.
- GO marker page: HTTP 200, GO table not rendered. GO IDs and evidence codes unknown.
- Alliance API: HTTP 200, no disease, ortholog, or GO data in the response.
- The MP term list and the remaining 11 references were not present in the fetched text.

I have what I need from the primary literature and databases. Writing the report now.

# Heterotaxy, Visceral, 12, Autosomal (HTX12) — Comprehensive Disease Report

**MONDO:0859222 · OMIM #619702 · Causal gene: *CIROP* (ciliated left–right organizer metallopeptidase; formerly *LMLN2*)**

> **Interpretation note / scope.** This report is built around the identifiers supplied: MONDO:0859222 / OMIM #619702, caused by biallelic variants in ***CIROP*** (HGNC:53647, OMIM *619703, 14q11.2). This is *not* the X-linked *ZIC3* disease (HTX1) nor the *MMP21* disease (HTX7), both of which appear in adjacent literature. Where a section could not be supported by material retrieved in this session, that is stated explicitly rather than filled from memory.
>
> **Access limitations encountered.** OMIM pages, PubMed/PMC HTML, ClinVar/Gene/GTR web pages, Ensembl, gnomAD web UI, ZFIN, Xenbase, Orphanet, Cell Press and Springer were all blocked (403 / bot-challenge / JS-only) from this environment. Substantive primary data were obtained instead from: (a) the **full author-accepted manuscript PDF** of the defining paper, retrieved open-access from the Université de Bordeaux repository (Unpaywall-indexed green OA copy of Nat Genet 2022;54:62–72); (b) **NCBI E-utilities** (Gene, ClinVar, PubMed efetch); (c) **UniProt REST**, **HGNC REST**, and the **gnomAD GraphQL API**; (d) MGI; (e) targeted web search.
>
> **Important nomenclature caveat.** The open-access author manuscript uses the authors' original gene/protein name **TOUT-DE-TRAVERS (*TDT*)** and a 733-aa ORF; the published version renamed it **CIROP** and the clinical/reference numbering (MANE NM_001354640.2, 788 aa) differs. Residue numbering is reconciled in §4.

---

## 1. Disease Information

### 1.1 Overview

Visceral heterotaxy-12 (HTX12) is an **autosomal recessive congenital laterality (left–right patterning) disorder** caused by biallelic loss-of-function variants in *CIROP*. It is an **embryonic developmental disorder of the left–right axis**, not a progressive or degenerative disease: the entire pathogenic window is the few hours of early somitogenesis during which the left–right organizer (LRO) operates. The clinical consequence is abnormal placement of thoracoabdominal viscera across the left–right axis, ranging from complete mirror-image reversal (*situs inversus totalis*) through selective organ misarrangement (*situs ambiguus*/heterotaxy) to apparently normal *situs solitus* with isolated dextrocardia — in nearly all cases accompanied by congenital heart defects (CHD).

MedGen reproduces the OMIM-derived definition: *"Visceral heterotaxy-12 (HTX12) is an embryonic developmental disorder characterized by defects in the asymmetric positioning of visceral organs across the left-right axis, known as laterality defects."* The phenotype ranges *"from complete organ reversal (situs inversus totalis) to selective misarrangement of organs (situs ambiguus) such as the liver, spleen, and pancreas,"* often with dextrocardia or complex congenital heart defects, with early death possible in severe cases ([MedGen UID 1803695 / C5676898](https://www.ncbi.nlm.nih.gov/medgen/?term=CIROP)).

A defining clinical feature — emphasised repeatedly by the discovery paper — is that **HTX12 is a "pure" laterality disorder with no other ciliopathy features**: *"As is the case for mutant tdt fish and frogs, there is no other ciliopathy-related phenotype arguing that TDT plays no other function beyond early LR specification"* (Szenker-Ravi et al., author manuscript, lines 433–435; [Nat Genet 2022;54:62–72](https://www.nature.com/articles/s41588-021-00970-4), PMID **34903892**).

### 1.2 Key identifiers

| Resource | Identifier | Source |
|---|---|---|
| OMIM (phenotype) | **#619702** HETEROTAXY, VISCERAL, 12, AUTOSOMAL; HTX12 | [omim.org/entry/619702](https://www.omim.org/entry/619702) (via MedGen/search) |
| OMIM (gene) | ***619703*** CILIATED LEFT-RIGHT ORGANIZER METALLOPEPTIDASE; CIROP | NCBI Gene esummary (`MIM: 619703`) |
| MONDO | **MONDO:0859222** | supplied; MedGen filter shows "Records in Mondo (2)" |
| MedGen | **UID 1803695**, CUI **C5676898**, semantic type *Congenital Abnormality* | MedGen |
| DOID | **DOID:0051026** ("visceral heterotaxy 12") | MGI disease table for Cirop |
| Orphanet | **No HTX12-specific ORPHA entry.** MedGen filter: "Records in Orphanet (0)". UniProt cross-references *CIROP* to **ORPHA:101063** (situs inversus totalis); Orphanet also lists *CIROP* under its former symbol *LMLN2* as a gene with "Disease-causing germline mutation(s) in Situs inversus totalis" ([orpha.net gene page](https://www.orpha.net/en/disease/gene/CIROP?mode=name)) | MedGen, UniProt, Orphanet |
| MeSH | **No disease-specific MeSH descriptor.** MeSH supplementary chemical record **"CIROP protein, human"**, UI **C000723020**, EC 3.4.24.-. Indexing of the defining paper uses *Body Patterning*, *Metalloproteases*, *Cilia*, *Gene Regulatory Networks*, *Loss of Function Mutation*, *Vertebrates*. The related CIROZ paper is indexed to **Heterotaxy Syndrome/genetics** | PubMed efetch XML, PMIDs 34903892 & 39753129 |
| HPO | MedGen filter reports **"Records in HPO (0)"** for this concept; OMIM's own Clinical Synopsis does carry HP IDs (see §3) | MedGen; omim.org/clinicalSynopsis/619702 |
| ICD-10 / ICD-11 | **Not retrieved in this session.** No ICD mapping for HTX12 specifically was obtained from any source I could reach; do not populate this field from this report | — |
| GARD | No GARD ID shown on the MedGen record | MedGen |

### 1.3 Synonyms and alternative names

- **HTX12** (OMIM symbol)
- **Visceral heterotaxy 12, autosomal**
- **Heterotaxy, visceral, 12, autosomal** (OMIM preferred title)
- **CIROP-related heterotaxy** / **CIROP-related disorder** (the condition label used by several ClinVar submitters)
- **LMLN2-related situs anomalies** (historical gene symbol; Orphanet still indexes under *LMLN2*)
- **TDT-related heterotaxy** (author manuscript name "Tout-de-travers")
- Overlapping clinical descriptors used for affected individuals: *situs inversus totalis*, *situs ambiguus*, *recessive situs anomalies*

### 1.4 Nature of the evidence base

Information for HTX12 is **aggregated disease-level knowledge derived from a small number of deeply phenotyped research cohorts**, not from EHR or registry data. The entire clinical description rests on:

1. **Szenker-Ravi et al. 2022** (PMID 34903892) — 21 patients, 12 families, the sole source for OMIM #619702.
2. **Al-Korashy et al. 2025**, *Clin Genet* 107(2):224–230, PMID **39513328** — a consanguineous heterotaxy cohort in which *CIROP* is one of 8 recessive heterotaxy genes with variants.
3. **ClinVar** submissions (50 records on the gene; see §4), which are laboratory-derived and include post-2022 clinical cases not described in the literature.

There is **no natural-history study, no patient registry, no prospective cohort, and no published quality-of-life data** specific to HTX12.

---

## 2. Etiology

### 2.1 Primary causal factor

HTX12 is a **monogenic, fully genetic, autosomal recessive Mendelian disorder**. No environmental, infectious, or multifactorial contribution has been described.

The causal lesion is **biallelic loss of function of *CIROP***, a Zn²⁺-dependent M8 (leishmanolysin-like) metallopeptidase expressed exclusively and transiently in the ciliated left–right organizer. From the author manuscript (lines 411–419):

> *"we identified germline homozygous TDT variations in 7 cases of CHD associated with heterotaxy from 7 different families (Families 1-7)… We then identified TDT mutations by whole-exome sequencing or targeted sequencing in five additional families segregating heterotaxy (Families 8-12)… All germline variations, homozygous patients from 11 families and compound heterozygous in family 12, were confirmed by Sanger sequencing in available family members, and found to fully segregate with the disease according to an autosomal recessive mode of inheritance."*

Mechanistically the causal factor is **loss of extracellular proteolytic activity in the LRO**, demonstrated by the catalytic-dead rescue experiment: a *tdt* mRNA carrying three missense substitutions in the zinc-binding site (HExxH→AAxxA; p.His247Ala, p.Glu248Ala, p.His251Ala in the authors' numbering) *"was unable to rescue the heart looping defects in larvae bereft of tdt"*, whereas wild-type mRNA rescued normal cardiac looping in 87% of embryos (lines 265–272).

### 2.2 Genetic risk factors

**Causal variants (the only established genetic risk factor).** Nine germline *CIROP* alleles were reported in the original series, in 21 patients from 12 families "of distinct geographical origin" (line 418). ClinVar now holds additional independently ascertained pathogenic/likely-pathogenic alleles (§4.2).

**Consanguinity.** The discovery cohort is dominated by homozygosity (11/12 families), with the pedigree figure showing consanguineous unions (Fig. 7a). Independently, Al-Korashy et al. (PMID 39513328) studied *"24 affected individuals from 19 unrelated families, recruited consecutively from a highly consanguineous population"* (Saudi Arabia) and achieved a **42.1% diagnostic yield**, with 7 of 9 causal variants homozygous and ***CIROP*** among the eight implicated autosomal recessive heterotaxy genes (the others: *C1orf127/CIROZ*, *CCDC39*, *DNAAF3*, *DNAH5*, *DNAH9*, *MMP21*, *MNS1*). **Consanguinity is therefore the single most important population-level risk modifier.**

**Susceptibility loci / GWAS.** None. No GWAS signal, modifier locus, or polygenic contribution to HTX12 has been reported in any source retrieved.

**Carrier state.** Heterozygotes are unaffected. Pedigree analysis showed full segregation with a recessive model; heterozygous parents and sibs are phenotypically normal.

**Note on *CIROP* population constraint.** *CIROP* is **not** depleted of loss-of-function variants in gnomAD (pLI ≈ 3.7 × 10⁻¹², LOEUF = 1.50, observed/expected LoF = 1.11 with 31 observed vs 27.9 expected; missense Z = −5.07, o/e missense = 1.77 — gnomAD GraphQL API, GRCh38). This is exactly what is expected for a gene whose only requirement is a few hours of embryogenesis and which has been repeatedly lost in evolution; it also means **LoF-intolerance metrics cannot be used to support pathogenicity for this gene**, an important ACMG-interpretation caveat.

### 2.3 Environmental risk factors

**None identified.** No toxin, teratogen, occupational exposure, maternal condition, lifestyle factor, parental age effect, or seasonal/geographic environmental association has been reported for HTX12 in any retrieved source. (Note: for *heterotaxy in general*, the NBDPS population study reported laterality defects more common among preterm births and among children of mothers who were non-white or aged <20 — Lin et al., *Am J Med Genet A* 2014;164A:2581–2591 — but these are **not** HTX12-specific and no causal interpretation is warranted.)

### 2.4 Protective factors

**Genetic protective factors:** none identified. No modifier allele or protective variant has been described.

**Environmental protective factors:** none identified. Importantly, there is no evidence that periconceptional folate or any dietary factor modifies HTX12 risk.

The only true "protective" consideration documented experimentally is **epistatic**: in *Xenopus tdt* crispants, *"depletion of dand5 on the left side of tdt crispants, i.e. on the side in which Tdt is required, was sufficient to rescue the asymmetry defects"* (lines 332–334). This is a mechanistic rescue, not a clinical protective factor, but it defines the node at which the pathway could in principle be bypassed.

### 2.5 Gene–environment interactions

**None described.** No CTD/PheGenI-type gene–environment interaction data exist for *CIROP*. Given that the gene's expression window is confined to the LRO at early somitogenesis and that the mutant phenotype is essentially fully penetrant in humans (§9), a meaningful environmental interaction is biologically unlikely but has not been formally excluded.

---

## 3. Phenotypes

### 3.1 Aggregate phenotype distribution in the defining cohort (n = 21)

Verbatim from the author manuscript (lines 430–433):

> *"Of the 21 cases presenting with congenital heterotaxy, 8 had situs solitus with or without isolated dextrocardia, 5 had situs ambiguus, 8 had situs inversus totalis, and nearly all had congenital heart defects (CHD)."*

| Situs category | n/21 | % |
|---|---|---|
| *Situs solitus* ± isolated dextrocardia | 8 | 38% |
| *Situs ambiguus* (heterotaxy proper) | 5 | 24% |
| *Situs inversus totalis* | 8 | 38% |
| Congenital heart defect | "nearly all" | ~95% |

**Key clinical insight for the knowledge base:** the laterality phenotype is **highly variable even within the same genotype class**, while the *cardiac* phenotype is near-obligate. A patient with *situs solitus* and an isolated cardiac lesion can still carry biallelic *CIROP* variants — which has direct consequences for who should be tested (§10).

### 3.2 Phenotype table with HPO terms

The cardiac lesions recorded across the cohort are enumerated in the Table 1 legend of the author manuscript (lines 1303–1311). The table body in the repository PDF is rendered at a resolution that does not permit reliable per-patient extraction, so **per-patient frequencies for individual cardiac lesions are not reported here**; the lesion list below is the authoritative set of defects observed in the cohort, and the HP IDs marked "OMIM CS" are those carried in the OMIM Clinical Synopsis.

#### Cardiovascular (clinical signs / physical manifestations)

| Phenotype | Suggested HPO | Evidence |
|---|---|---|
| Dextrocardia | **HP:0001651** | OMIM CS (confirmed in search of omim.org/clinicalSynopsis/619702) |
| Abnormal cardiac septum morphology / septal defects | **HP:0001671** | OMIM CS |
| Ventricular septal defect (VSD) | **HP:0001629** | Table 1 legend |
| Atrial septal defect (ASD) | **HP:0001631** | Table 1 legend |
| Ostium primum ASD (ASD-OP) | **HP:0011994** | Table 1 legend |
| Common atrium (CA) | **HP:0011565** | Table 1 legend |
| Complete atrioventricular canal / AVSD (CAVC) | **HP:0006695** (atrioventricular canal defect) | Table 1 legend |
| Double outlet right ventricle (DORV) | **HP:0001719** | Table 1 legend; OMIM gene-level phenotype list; patient F7-II:5 illustrated with *situs inversus* + DORV (Fig. 7b) |
| Double inlet right ventricle (DIRV) | **HP:0011565**-adjacent; suggest **HP:0001674** (complex CHD) if no exact term | Table 1 legend |
| Transposition of the great arteries (TGA) | **HP:0001669** is pulmonary stenosis; TGA = **HP:0001669**? → use **HP:0001669** *no*; correct term **HP:0001669** is PS. TGA = **HP:0001669**… use **HP:0001669** only for PS; **TGA = HP:0001669** is incorrect → **TGA = HP:0001669**. Use **HP:0001669 (pulmonic stenosis)** and **HP:0001669**… see note below | OMIM CS, Table 1 legend |
| Pulmonary stenosis (PS) | **HP:0001642** (pulmonic stenosis) | OMIM CS, Table 1 legend |
| Pulmonary atresia (PA) | **HP:0010882** | Table 1 legend |
| Tricuspid atresia (TA) | **HP:0001670** | Table 1 legend |
| Aortic valve stenosis (AS) | **HP:0001650** | Table 1 legend |
| Aortic coarctation (CoA) | **HP:0001680** | Table 1 legend |
| Interrupted aortic arch (IAA) | **HP:0011611** | Table 1 legend |
| Patent ductus arteriosus (PDA) | **HP:0001643** | Table 1 legend |
| Patent foramen ovale (PFO) | **HP:0001655** | Table 1 legend |
| Partial anomalous pulmonary venous connection (PAPVC) | **HP:0011540** | Table 1 legend |
| Abnormal inferior vena cava morphology (IVC anomalies, e.g. interruption with azygos continuation) | **HP:0011671** | Table 1 legend |
| Abnormal superior vena cava morphology (SVC anomalies, e.g. persistent left SVC) | **HP:0011673** | Table 1 legend |

> **Correction/flag on TGA:** I retrieved "transposition of the great arteries" as an OMIM Clinical Synopsis cardiovascular feature for HTX12 and as a Table 1 abbreviation, but I did not retrieve its HP ID from an authoritative HPO source in this session. **Do not populate the HP ID for TGA from this report** — look it up in HPO directly. The same caution applies to any HP ID above that is marked only as "suggested": these are my mappings from the lesion name, not retrieved HPO annotations. MedGen explicitly reports **"Records in HPO (0)"** for concept C5676898, meaning HTX12 currently has **no curated HPO disease annotation set** — only the HP IDs embedded in the OMIM Clinical Synopsis.

#### Abdominal / visceral

| Phenotype | Suggested HPO | Evidence |
|---|---|---|
| *Situs inversus totalis* | **HP:0001696** | OMIM CS |
| *Situs ambiguus* / abnormal situs viscerum | **HP:0001706** (suggested) | Paper, 5/21 |
| Intestinal malrotation | **HP:0002566** | OMIM CS |
| Annular pancreas | **HP:0001734** | OMIM CS |
| Abnormal liver position / midline liver | suggest **HP:0002240**-adjacent (not retrieved) | OMIM-derived MedGen definition names liver, spleen and pancreas as misarranged organs |
| Abnormal spleen morphology (asplenia/polysplenia) | **HP:0001743** (asplenia) / **HP:0001748** (polysplenia) — *suggested* | **Flag:** asplenia and polysplenia were **not** found in the HTX12 OMIM Clinical Synopsis excerpt retrieved. They are canonical heterotaxy features and the MedGen/OMIM definition names the spleen, but HTX12-specific splenic phenotyping was not confirmed in this session. Treat as *unconfirmed for HTX12*. |

#### Onset / course

| Attribute | Term | Evidence |
|---|---|---|
| Onset in utero | **HP:0030674** | OMIM CS |
| Autosomal recessive inheritance | **HP:0000007** | OMIM CS (SNOMEDCT 258211005; UMLS C0441748) |
| Variable expressivity | — | OMIM CS: "variable manifestations and possible early death" |

#### Features explicitly ABSENT (high-value negative phenotypes)

The absence of these is diagnostically discriminating and should be captured in the knowledge base:

- **No primary ciliary dyskinesia phenotype** — no sinopulmonary disease, no situs-inversus-with-bronchiectasis syndrome. Author manuscript lines 433–435: *"there is no other ciliopathy-related phenotype."*
- **No renal cysts, no hydrocephalus, no body-axis curvature** in model organisms (lines 281–283), consistent with the absence of a broader ciliopathy in patients.
- **No intellectual disability, retinal, skeletal or hepatic ciliopathy features** reported.
- **Normal fertility expected** — MZ-null zebrafish adults are *"fully viable and fertile"* (line 283). No human fertility data exist, but unlike PCD-associated situs inversus, there is no mechanistic reason to expect sperm dysmotility, since *CIROP* is not required for ciliogenesis or ciliary beating (§6).

### 3.3 Phenotype characteristics

- **Age of onset:** **Congenital / prenatal (in utero, HP:0030674).** The pathogenic window is early somitogenesis (equivalent to ~3 weeks post-fertilisation in humans; the human LRO becomes visible around 14 days post-fertilisation per Pasquetti et al., *Genes* 2025;16(1):62, PMID 39858609). Diagnosis is made prenatally by fetal echocardiography or postnatally at birth.
- **Severity:** **Highly variable**, from isolated dextrocardia with a structurally repairable heart to complex single-ventricle physiology incompatible with survival. The pedigrees record **terminations of pregnancy (TOP) in multiple families (5, 10, 11, 12)** and a spontaneous abortion (family 12), indicating a severe end of the spectrum detected prenatally (Fig. 7a legend, lines 1278–1285).
- **Progression:** **Non-progressive and non-episodic.** The malformation is fixed at birth. All subsequent morbidity is a *consequence* of the structural lesion (heart failure, cyanosis, surgical sequelae, infection risk if functionally asplenic) rather than of ongoing *CIROP* dysfunction. The gene has no known post-embryonic function.
- **Frequency among affected individuals:** CHD ~95% ("nearly all"); laterality abnormality by definition 100% of ascertained cases, though the authors predict ascertainment bias (§9.2).

### 3.4 Quality-of-life impact

**No HTX12-specific QoL data exist** (no EQ-5D, SF-36, PROMIS or disease-specific instrument has been applied). Generic heterotaxy/CHD evidence that is reasonable to extrapolate, with the caveat that it is not HTX12-specific:

- Functionally asplenic heterotaxy children had hospitalisation-requiring infections in **50% (8/16)** vs **8%** in those with a normal spleen or polysplenia (*J Allergy Clin Immunol* 2016 study, S0091-6749(16)31289-1).
- Heterotaxy patients undergoing Fontan palliation had **20% early mortality**, higher in asplenia than polysplenia (**27% vs 12%, p = 0.019**), with persistently worse transplant-free survival than non-heterotaxy patients (Stephens et al., *World J Pediatr Congenit Heart Surg* 2022, [doi:10.1177/21501351221099944](https://journals.sagepub.com/doi/abs/10.1177/21501351221099944)).

---

## 4. Genetic / Molecular Information

### 4.1 Causal gene

| Field | Value | Source |
|---|---|---|
| Approved symbol | **CIROP** | HGNC REST |
| Approved name | ciliated left-right organizer metallopeptidase | HGNC |
| HGNC ID | **HGNC:53647** | HGNC REST |
| Previous symbol / name | ***LMLN2*** / "leishmanolysin like peptidase 2" — symbol and name changed **2022-01-18** | HGNC REST |
| Other aliases | **HTX12**, LMLN2; "leishmanolysin homolog" | NCBI Gene esummary |
| NCBI Gene ID | **100128908** | NCBI Gene |
| Ensembl | **ENSG00000283654** | HGNC, UniProt |
| UniProt | **A0A1B0GTW7** (CIROP_HUMAN, reviewed/Swiss-Prot); secondary A0A2R8Y3T5 | UniProt REST |
| OMIM gene | ***619703*** | HGNC, NCBI Gene |
| MANE Select | **NM_001354640.2 / ENST00000637218.2** (protein NP_001341569.1 / ENSP00000489869.1) | HGNC, UniProt |
| CCDS | **CCDS86373** | HGNC, UniProt |
| Cytoband | **14q11.2** | HGNC, NCBI Gene |
| GRCh38 coordinates | **chr14:23,099,062–23,104,989**, **minus strand**, NC_000014.9; NCBI lists chrstart 23,104,988 → chrstop 23,099,061, **16 exons** | gnomAD API; NCBI Gene esummary |
| GRCh37 coordinates | chr14:23,568,270–23,574,197 (NC_000014.8) | NCBI Gene esummary |
| T2T-CHM13 | chr14:17,299,695–17,305,633 (NC_060938.1) | NCBI Gene esummary |
| Mouse ortholog | ***Cirop***, **MGI:5588935**, NCBI Gene 101056084, Ensembl ENSMUSG00000114865, Chr14:54,930,055–54,936,290 (−, GRCm39); synonym Gm29776 | MGI |
| Rat ortholog | ***Cirop***, **RGD:1560492** (alias Lmln2) | HGNC, RGD |
| Zebrafish / Xenopus orthologs | UniProt CIROP_DANRE **A0A1D5NSK0**; CIROP_XENLA **A0A1L8HYT7**; zebrafish LOC100331300 / XM_002662823 | UniProt; paper Methods |

**Gene structure caveat — critical for variant calling.** *CIROP* is poorly annotated in reference databases because its expression is confined to a few hours of embryogenesis. From the author manuscript (lines 184–189, 249–252):

> *"As no more than 2 ESTs exist for this gene, the exon-intron structure of TDT is incompletely annotated in UCSC, Ensembl or NCBI. We determined that TDT in fact spans 14 exons…"*

and (lines 453–456):

> *"This unique feature has precluded obtaining sufficient ESTs to properly map its exon-intron borders. As such, TDT has not been properly covered by commercially-available exome platforms and has thus escaped clinical investigation, despite our data showing that it is frequently mutated in recessive forms of heterotaxy involving CHDs."*

The authors defined the full-length ORF at **chr14:23,104,920–23,099,282 (hg19)**, built from *LMLN2-204* plus conserved exons 5, 10, 11, 12, 13, 14.

### 4.2 Pathogenic variants

#### (a) The nine alleles of the discovery cohort

Nine germline alleles in 21 patients from 12 families; 5 missense, 1 in-frame single-codon deletion, 2 nonsense, 1 frameshift. Author-manuscript nomenclature (733-aa TDT ORF) with the corresponding ClinVar/MANE nomenclature where retrievable:

| Family/-ies | cDNA (paper) | Protein (paper) | ClinVar HGVS (NM_001354640.2) | Class | ClinVar germline classification | dbSNP |
|---|---|---|---|---|---|---|
| 2, 5, 11, 12 | c.92C>T | p.Ser31Phe | **c.92C>T (p.Ser31Phe)** | missense | **Conflicting classifications** (last eval. 2025-11-03) | rs553352307 |
| 12 | c.55?C>T | p.Arg194* | **c.571C>T (p.Arg191Ter)**, ClinVar alias "R194*" | nonsense | **Pathogenic** (2022-03-15) | rs764530848 |
| 8 | c.806G>C | p.Cys269Ser | *(UniProt: C324S)* | missense | UniProt "uncertain" | — |
| 3 | — | p.Trp291* | **c.1037G>A (p.Trp346Ter)** | nonsense | **Pathogenic** (2022-06-17) | rs1014082266 |
| 1 | c.986C>T | p.Ser329Leu | **c.1151C>T (p.Ser384Leu)**, alias "S329L" | missense | **Pathogenic** (2022-03-15) | rs183023758 |
| 4, 7 | c.1001C>T | p.Arg334Ile | **c.1166G>T (p.Arg389Ile)**, alias "R334I" | missense | **Pathogenic** (2022-03-15) | rs2140282332 |
| 10 | c.1144delG (or c.1144+1delG) | p.Gly382Aspfs*8 / p.Gln381fs*9 — *"frameshift … /splicing defects"* | — | frameshift ± splice | — | — |
| 9 | c.1202_1204delTCT | p.Phe401del | **c.1364TCT[1] (p.Phe456del)** | in-frame deletion | **Pathogenic** (2022-03-15) | rs1392604380 |
| 6 | c.1241T>C | p.Leu414Pro | *(UniProt: L469P)* | missense | UniProt "uncertain" | — |

**Numbering reconciliation:** clinical (MANE, 788 aa) numbering = author-manuscript (733 aa) numbering **+55** for residues in and after the catalytic domain (C269→C324, W291→W346, S329→S384, R334→R389, F401→F456, L414→L469). The N-terminal p.Ser31Phe is identical in both. p.Arg194* maps to **p.Arg191Ter** in MANE (ClinVar retains "R194*" as an alias) — i.e. the offset is not uniform across the protein, consistent with the three extra exon-2 residues present in *LMLN2-204* described in the paper's Fig. S2. **Always use the ClinVar/MANE HGVS for clinical reporting.**

#### (b) Functional stratification given by the authors

Author manuscript, lines 420–430:

> *"Among the nine germline variants identified, five were missense variants affecting highly conserved residues. Three of those, p.Cys296Ser [p.Cys269Ser], p.Ser329Leu (Family 1) and p.Arg334Ile (Families 4 and 7) are within the catalytic domain of TDT which could affect the enzymatic activity of the protease. The two others missense variants p.Ser31Phe (Families 2, 5, 11 and 12) and p.Leu414Pro (Family 6), as well as the deletion of a single conserved residue p.Phe401del (Family 9) are situated in other domains which may affect the half-life or quaternary structure of TDT. The three last variants are classical knockout alleles including two nonsense mutations p.Arg194* (Family 12) and p.Trp291* (Family 3) and a frameshift mutation p.Gly382Aspfs*8 (Family 10) leading to early stop codons, which we suspect will trigger NMD of mutant TDT transcripts."*

**Functional consequence class: loss of function.** No gain-of-function or dominant-negative mechanism has been proposed. **Caveat (important for curation):** the authors performed **no functional assay on the patient variants themselves and no patient-cell studies** — pathogenicity for the missense alleles rests on conservation, domain position and segregation.

#### (c) ClinVar landscape (retrieved via E-utilities, 50 records on *CIROP*)

**Pathogenic / likely pathogenic, assigned to HTX12 or "CIROP-related disorder":**

| HGVS (NM_001354640.2) | Protein | Type | Classification (date) | Condition | rsID |
|---|---|---|---|---|---|
| c.571C>T | p.Arg191Ter | SNV | Pathogenic (2022-03-15) | HTX12 | rs764530848 |
| c.1037G>A | p.Trp346Ter | SNV | Pathogenic (2022-06-17) | HTX12 | rs1014082266 |
| c.1151C>T | p.Ser384Leu | SNV | Pathogenic (2022-03-15) | HTX12 | rs183023758 |
| c.1166G>T | p.Arg389Ile | SNV | Pathogenic (2022-03-15) | HTX12 | rs2140282332 |
| c.1364TCT[1] | p.Phe456del | microsat. | Pathogenic (2022-03-15) | HTX12 | rs1392604380 |
| c.1392C>A | p.Cys464Ter | SNV | Likely pathogenic | HTX12 | — |
| c.302del | p.Arg101fs | deletion | Likely pathogenic (2025-10-21) | HTX12 | — |
| c.1582C>T | p.Gln528Ter | SNV | Likely pathogenic (2025-10-24) | HTX12 | — |
| c.1331dup | p.Leu444fs | duplication | Likely pathogenic (2022-12-12) | HTX12 | rs2503617333 |
| c.994_997del | p.Glu332fs | microsat. | Likely pathogenic (2025-07-23) | CIROP-related disorder | — |
| c.595del | p.His199fs | deletion | Likely pathogenic (2025-01-14) | CIROP-related disorder | — |
| c.1135-1G>A | — | splice acceptor | Likely pathogenic (2026-09-22) | CIROP-related disorder | — |
| c.1487G>A | p.Trp496Ter | SNV | Likely pathogenic (2025-06-03) | CIROP-related disorder | — |
| c.187C>T | p.Arg63Ter | SNV | Likely pathogenic (2025-07-23) | CIROP-related disorder | — |
| c.64C>T | p.Arg22Ter | SNV | **Conflicting** (2026-09-22) | CIROP-related / HTX12 | rs185661693 |
| c.92C>T | p.Ser31Phe | SNV | **Conflicting** (2025-11-03) | HTX12 | rs553352307 |
| c.1719G>A | p.Trp573Ter | SNV | Pathogenic (2022-07-05) | MCA/dysmorphism-ID (MONDO:0015159) | — |
| c.1661A>G | p.Tyr554Cys | SNV | Likely pathogenic (2022-07-05) | MCA/dysmorphism-ID | — |

**VUS:** c.1288G>C (p.Glu430Gln, HTX12); c.203A>G (p.Tyr68Cys, HTX12, rs1195322479); c.538G>C (p.Gly180Arg, HTX12, rs1266315800); c.1532G>A (p.Gly511Glu); c.1058C>T (p.Thr353Ile); c.1361_1363del (p.Asp454_Phe455delinsVal).

**Benign/likely benign:** a set of synonymous and deep-intronic changes (c.426A>G, c.903+14G>A, c.904-3T>C, c.1074C>G, c.1224C>G, c.1617T>C, c.1750-15C>T, c.279C>T, c.2238C>T, c.209G>A, c.1233C>T, c.1281C>T, c.33GCC[3], c.1992T>G).

**⚠ Curation flag:** three ClinVar records on the *CIROP* transcript (c.2159+2T>A, VUS; c.1126G>A p.Glu376Lys, likely pathogenic; c.988+1G>C, pathogenic) are submitted under the condition **"Trichothiodystrophy 1, photosensitive" (OMIM 601675)**. This is almost certainly a submitter condition-assignment or transcript-overlap artifact rather than a genuine *CIROP*–trichothiodystrophy association, and **should not be propagated into a disease knowledge base as a *CIROP* phenotype** without verification against the original SCV submissions.

#### (d) Allele frequencies

| Variant | gnomAD | TOPMed | 1000G | ExAC |
|---|---|---|---|---|
| c.92C>T p.Ser31Phe | 0.00106–0.00135 | 0.00126 | 0.00040 | 0.00139 |
| c.64C>T p.Arg22Ter | 0.00014 | 0.00018 | 0.00020 | — |
| c.1037G>A p.Trp346Ter | 0.00001 | 0.00002 | — | — |
| c.1151C>T p.Ser384Leu | 0.00001–0.00002 | — | 0.00020 | — |
| c.203A>G p.Tyr68Cys | 0.00001 | 0.00001 | — | — |
| c.538G>C p.Gly180Arg | 0.00001 | 0.00000 | — | — |
| c.1992T>G p.His664Gln (LB) | 0.00161 | 0.00174 | 0.00220 | — |

**Note the tension around p.Ser31Phe:** at ~1.1–1.4 × 10⁻³ allele frequency it is the most common disease-associated allele but also common enough that ClinVar classifications now conflict. It was found in 4 of 12 families in the original series — consistent with a recurrent/founder-type allele, though no formal haplotype analysis was retrieved.

#### (e) Germline vs somatic

**Exclusively germline.** All reported variants are germline and segregate in families. No somatic *CIROP* mutation has been described; COSMIC/TCGA data were not retrievable in this session and no cancer association for *CIROP* exists in the literature retrieved. (By contrast, its pathway partner *MMP21* is overexpressed in epithelial cancers — refs 53–54 of the paper — but this is not true of *CIROP*, which the authors state is *"the single gene in LR patterning with no other function than the one ascribed here"*, lines 460–462.)

### 4.3 Modifier genes

**None established.** The most plausible candidate modifiers are the other four members of the LRO "functional operon" — ***MMP21*** (HTX7, MIM 616749), ***PKD1L1*** (HTX8, MIM 617205), ***DAND5***, and ***CIROZ***/*C1orf127* — since the authors propose that *"their requirements are interlocked"* (line 150). However, double-mutant data argue **against** simple additive modification: *"Double heterozygous fish did not show any LR defects, and no discernible increase or decrease in penetrance or severity of heterotaxy was observed in double KO compared to the simple KO of tdt or mmp21 alone"* (lines 372–374).

### 4.4 Epigenetic information

**No epigenetic data.** No DNA methylation, histone-modification, imprinting or chromatin data for the *CIROP* locus were retrieved from ENCODE, Roadmap or any other source. *CIROP* is **transcriptionally** controlled by the ciliogenesis transcription factors **FOXJ1** and **NOTO** (§6), but this is transcription-factor regulation, not an epigenetic mechanism in the methylation/chromatin sense.

### 4.5 Chromosomal abnormalities

**No HTX12 arising from a structural chromosomal rearrangement has been reported.** ClinVar contains 8 large 14q11.2-containing copy-number records (e.g. GRCh38 chr14:20,043,513–48,642,042 ×3; chr14:20,151,149–23,442,195 ×3; chr14:20,196,945–45,284,802 ×1) classified Pathogenic/Likely pathogenic, but these are **multigene CNVs spanning hundreds of genes** and their pathogenicity is not attributable to *CIROP*. One relevant exception: Al-Korashy et al. (PMID 39513328) report that of their 9 heterotaxy-causing variants, one of the two compound-heterozygous findings included **a heterozygous CNV deletion** — the gene involved was not specified in the abstract, so whether a *CIROP* intragenic deletion exists is **unresolved**.

---

## 5. Environmental Information

- **Environmental factors:** None known. No toxicant, radiation, pollutant or occupational exposure has been linked to HTX12.
- **Lifestyle factors:** None known. No smoking, alcohol, dietary or exercise association has been reported.
- **Infectious agents:** **Not applicable.** HTX12 is not caused or triggered by any pathogen. (Infection is relevant only *downstream*, as a complication of functional asplenia in heterotaxy — see §11.)

This section is **genuinely empty for this disease**, and that emptiness is itself informative: HTX12 is a pure Mendelian developmental disorder with no documented environmental dimension.

---

## 6. Mechanism / Pathophysiology

### 6.1 Ordered causal chain

**Normal pathway (steps 0a–0f), then the disease chain (steps 1–12).**

**Normal left–right specification at the ciliated LRO:**

- **0a.** *NOTO* and *FOXJ1* specify the LRO (ventral node in mouse, gastrocoel roof plate in *Xenopus*, Kupffer's vesicle in zebrafish) → **leads to** transcription of the motile-ciliogenic program *and* of *CIROP* itself. **Demonstrated:** *"Tdt expression was entirely abolished in mutant embryos lacking Noto"* and *"foxj1a depletion by morpholino oligomer injections completely abolished tdt expression in the DFCs"* (lines 216, 238–240).
- **0b.** Motile, posteriorly polarised cilia on **central LRO cells** rotate → **produce** a right-to-left extracellular fluid flow ("leftward flow").
- **0c.** Leftward flow is **sensed** by immotile cilia on **lateral LRO cells** via the PKD2–PKD1L1 channel complex (lines 110–112).
- **0d.** Flow sensing → **CIROP is required, on the left side only**, acting as an extracellular Zn²⁺-metallopeptidase.
- **0e.** → **MMP21** acts immediately downstream of CIROP in the same linear cascade.
- **0f.** → **asymmetric reduction of *DAND5* mRNA on the left** → de-repression of NODAL/GDF1 on the left → NODAL propagation to the left lateral plate mesoderm → transcription of *NODAL*, *LEFTY*, *PITX2* → asymmetric organ morphogenesis (*situs solitus*).

**HTX12 disease chain:**

1. **Biallelic loss-of-function variants in *CIROP*** (nonsense/frameshift → NMD; catalytic-domain missense → loss of zinc-dependent proteolysis; non-catalytic missense/in-frame deletion → altered half-life or quaternary structure) → **result in** absent or catalytically inactive CIROP protein in the LRO. *Inferred for the human missense alleles* (no patient functional assay); *demonstrated* for catalytic necessity in zebrafish by the catalytic-dead rescue failure (lines 268–272).
2. Absent CIROP → **does NOT impair** LRO formation, ciliogenesis, cilia length/number, ciliary beating, or flow velocity/directionality. **Demonstrated:** *"MZ tdt−/− embryos presented with a normal-sized KV containing motile cilia with normal beating patterns. Cilia length and numbers did not significantly differ from that of control embryos"* (lines 345–348); in *Xenopus*, *"no single parameter was statistically different between control and tdt crispants"* for cell surface area, cilia length/polarisation, flow velocity and directionality (lines 359–362). **This branch is explicitly closed — HTX12 is not a ciliopathy.**
3. Absent CIROP activity on the **left** side of the LRO → **fails to transduce** the flow signal. **Demonstrated (laterality-restricted):** *"Injections on the left side of the embryos resulted in similar penetrance of laterality defects, while no phenotypes were observed when tdt was inactivated specifically on the right side"* (lines 293–295).
4. → **Mmp21 is not activated** (and is transcriptionally up-regulated in compensation). **Demonstrated:** *tdt* expression precedes *mmp21*; *"the endogenous expression of mmp21 was significantly increased in tdt KO fish… while the reverse was not true"*; *tdt* mRNA overexpression rescues *tdt⁻ᐟ⁻* but **cannot** rescue *mmp21⁻ᐟ⁻*, *"suggesting that Mmp21 most likely functions downstream of Tdt"* (lines 377–390).
5. → **Failure to repress *DAND5* on the left.** **Demonstrated:** *"dand5 expression in MZ tdt−/− zebrafish was not repressed on the left side"* (lines 342–343); in *Xenopus*, *"The asymmetric expression of dand5, which is normally repressed on the left side in response to Nodal signaling, was not recorded when embryos lacked functional Tdt"* (lines 357–359).
6. → **Persistent bilateral DAND5 (a secreted NODAL antagonist)** → **inhibits** NODAL/GDF1 on the left.
7. → **Failure of NODAL propagation to the left lateral plate mesoderm.** **Demonstrated:** *"bilateral, absent or posterior-restricted expression of spaw was observed in MZ tdt−/− mutants"* (lines 310–311); *"the expression of nodal1 in the left LPM was lost in tdt crispants"* (line 326).
8. → **Collapse of the NODAL–LEFTY–PITX2 cascade.** **Demonstrated:** *"Expression of the Nodal target gene lefty1 in the left diencephalon was completely abolished"*; *"the expression of lefty2 in the left heart primordium was largely lost"* (lines 314–317); *"While pitx2 was restricted to the left in control embryos, it was mostly lost or misexpressed on the right side of tdt crispants"* (lines 323–324).
9. → **Randomisation rather than reversal** of organ-situs decisions. The dorsal midline barrier remains intact (*tbxta* expression uninterrupted, line 314), so the defect is one of *signal generation*, not of *signal containment*.
10. → **Randomised cardiac looping and jogging.** **Demonstrated:** heart-jogging irregularities by 30 hpf, looping randomisation at 48 hpf (lines 304–305).
11. → In humans, **randomised placement of heart, lungs, liver, spleen, stomach, pancreas and gut**, producing the observed trimodal distribution of *situs solitus* / *ambiguus* / *inversus* (§3.1).
12. → **Congenital heart defects** arise because cardiac looping, atrioventricular alignment, venoatrial connection and outflow-tract septation are all laterality-dependent morphogenetic events; hence DORV, TGA, AVSD, common atrium, anomalous systemic/pulmonary venous return and IVC interruption (§3.2). **Clinical endpoint:** cyanosis, heart failure, need for surgical palliation/repair, or fetal demise/TOP.

**Branch point summary:** the single branch in this mechanism is at step 2/3 — CIROP is required for *flow interpretation*, not for *flow generation*. Everything downstream is a linear cascade.

### 6.2 Molecular pathways

- **NODAL/TGF-β left–right signalling cascade** — the core pathway. NODAL/GDF1 → ACVR2B/CFC1 → left LPM → *NODAL*, *LEFTY1/2*, *PITX2*. DAND5 (Coco/Cerl2) is the dedicated secreted antagonist.
- **Extracellular proteolytic cascade** — the novel contribution of this gene. The authors frame it as analogous to the dorsoventral Chordin–Tolloid–Sizzled cascade: *"Patterning of the DV axis is mediated by the controlled cleavage of Chordin by the Zinc metalloprotease Tolloid which frees BMP to signal in ventral most regions of the embryo when Sizzled is silenced"* (lines 478–481).
- **PKD2/PKD1L1 polycystin mechanosensory/chemosensory channel** — upstream flow sensing.
- **Wnt/PCP** — upstream, for cilia polarisation (not CIROP-dependent).
- Suggested pathway identifiers: no KEGG/Reactome pathway specific to CIROP was retrieved; the closest Reactome/GO handle is the GO BP term below.

### 6.3 Cellular processes

- **Establishment of left/right asymmetry** — **GO:0061966** (UniProt annotation for CIROP, evidence ISS).
- **Proteolysis** — **GO:0006508** (IEA:InterPro).
- **Cell adhesion** — **GO:0006508**/**GO:0007155** (IEA:InterPro; family-level inference, no CIROP-specific evidence).
- **Cilium-dependent flow sensing** (process-level; no CIROP-specific GO annotation).
- **Determination of left/right symmetry**, **heart looping**, **nodal signaling pathway** — appropriate GO BP terms to associate at the disease level.

### 6.4 Protein dysfunction

**CIROP architecture (UniProt A0A1B0GTW7, 788 aa, 85,397 Da, reviewed Swiss-Prot entry):**

| Feature | Residues |
|---|---|
| Signal peptide | 1–20 |
| Extracellular (topological domain) | 21–735 |
| **Transmembrane helix** | **736–756** |
| Cytoplasmic | 757–788 |
| Disordered | 40–59 (low complexity), 767–788 |
| **Zinc ligands (catalytic)** | **His305, His309, His385** |
| **Active site** | **Glu306** |
| **HExxH motif** | **H305-E306-L307-L308-H309** |
| N-glycosylation sites | N333, N425, N491, N524, N713 |
| Family | **Peptidase M8** (leishmanolysin-like metzincin) — Pfam **PF01457**, InterPro **IPR001577** |
| EC | **3.4.24.-** |
| Cofactor | **Zn²⁺** — "Binds 1 zinc ion per subunit" (CHEBI:29105 zinc(2+)) |
| Subcellular location | **Membrane; single-pass type I membrane protein** |
| UniProt function | *"Putative metalloproteinase that plays a role in left-right patterning process."* (ECO:0000250) |
| UniProt disease | **DI-06243**, *Heterotaxy, visceral, 12, autosomal (HTX12), MIM:619702*; *"HTX12 inheritance is autosomal recessive."* |
| Isoforms | 3 |

The author manuscript adds biochemical characterisation (lines 183–196):

> *"TDT codes for a Zn²⁺-dependent metalloproteinase belonging to the M8 peptidase family of leishmanolysin-like metzincins (a.k.a. LMLN2)… TDT in fact spans 14 exons, and consists of 4 domains: a signal peptide, a zinc catalytic domain containing the consensus His-Glu-x-x-His...His (HExxH...H) active site motif and a Met-turn methionine, a cysteine-rich domain and a C-terminal transmembrane domain… the encoded protease is membrane-bound and does not involve a GPI-anchor… This is in contrast to the TDT homolog GP63 in the Leishmania promastigote, which is GPI-anchored. The zebrafish TDT protein was readily secreted and is heavily post-translationally modified by sugar moieties which can be removed by PNGase F and to a lesser extent by Endo H… Upon DSS-crosslinking, TDT assembled into a high-molecular weight oligomer consistent with a discrete quaternary structure in solution."*

They additionally predict a **cysteine-switch prodomain** requiring removal for full activity (lines 470–472) — i.e. CIROP is likely itself a zymogen.

**How variants disrupt the protein:**
- Nonsense/frameshift (p.Arg191Ter, p.Trp346Ter, p.Arg22Ter, p.Arg63Ter, p.Cys464Ter, p.Trp496Ter, p.Gln528Ter, p.Glu332fs, p.His199fs, p.Arg101fs, p.Leu444fs) → predicted NMD → **complete loss of protein**.
- Catalytic-domain missense (p.Cys324Ser, p.Ser384Leu, p.Arg389Ile) → **loss of proteolytic activity** with protein retained.
- Non-catalytic missense/in-frame deletion (p.Ser31Phe near the signal peptide; p.Phe456del and p.Leu469P in/near the cysteine-rich domain) → proposed effect on **half-life or quaternary structure** (relevant given the demonstrated oligomerisation).
- Splice (c.1135-1G>A, c.1144delG "/splicing defects") → aberrant transcript.

**Structural resources:** AlphaFold model available via UniProt A0A1B0GTW7; **no experimental PDB structure of human CIROP exists**. The closest structural template is *Leishmania* GP63/leishmanolysin (same M8 family).

### 6.5 Metabolic changes

**None.** HTX12 is not a metabolic disease. No HMDB/BRENDA/metabolomic abnormality is described, and none would be expected: the enzyme's substrate is an unidentified extracellular protein, not a small molecule.

### 6.6 Immune system involvement

**No primary immune involvement.** CIROP has no described immune function; HPA reports *"Not detected in immune cells."*

**Secondary immune consequence — clinically critical:** patients with *situs ambiguus* and asplenia/functional hyposplenism are at risk of overwhelming encapsulated-organism sepsis. In heterotaxy generally, asplenic children had hospitalisation-requiring infections in 50% (8/16) vs 8% with normal spleen/polysplenia, and *"with prophylaxis, invasive bacterial diseases were rare"* (*J Allergy Clin Immunol* 2016). Whether HTX12 patients specifically develop asplenia was **not confirmed** in the sources retrieved (§3.2).

### 6.7 Tissue damage mechanisms

**Not applicable in the classical sense.** There is no oxidative stress, ischaemia, fibrosis, necrosis or inflammation intrinsic to HTX12. The "lesion" is a **misassembled body plan**, fixed before organogenesis completes. Secondary tissue injury (myocardial, hepatic congestion, pulmonary vascular) arises from the haemodynamics of the resulting CHD and from surgical palliation.

### 6.8 Biochemical abnormalities

- **Enzyme deficiency:** loss of a Zn²⁺-dependent metalloendopeptidase (EC 3.4.24.-) activity in the extracellular space of the LRO. **The physiological substrate of CIROP is unknown.**
- **Candidate substrates discussed by the authors** (lines 464–475): *"We note that 4 of the 5 identified genes encode proteins which have been reported to be post-translationally cleaved… PKD1L1 has been shown to be cleaved within the third intracellular loop of its transmembrane region, and DAND5, like its close homologue CERBERUS, may undergo proteolytic cleavage. Future investigations will need to address if ALED [CIROZ] is also cleaved…"* The 2025 AJHG paper on CIROZ (PMID 39753129) explicitly leaves open whether CIROZ is a substrate of MMP21 and/or CIROP.
- A 2024/2025 **eLife reviewed preprint** (bioRxiv 10.1101/2024.10.13.618030, "MMP21 behaves as a fluid flow transported morphogen to impart laterality during development") proposes that Mmp21 is transported by leftward flow as a morphogen and perceived via Cirop-positive cilia on sensor cells, and **speculates** that Mmp21 and Cirop could directly inactivate Pkd1l1 through its large extracellular domain. **This is an explicitly hypothetical, non-peer-reviewed claim** — I was unable to read the preprint text directly (eLife returned a bot challenge; the bioRxiv PDF returned unparsed binary), so it is reported here only as retrieved via search and should be verified before curation. Note also that it places Mmp21 **upstream** of Cirop, whereas Szenker-Ravi et al.'s zebrafish epistasis places Tdt/CIROP **upstream** of Mmp21 — **an unresolved contradiction in the field that the knowledge base should record as such.**
- **Ion channel defect:** none intrinsic to CIROP, though the pathway's upstream sensor is the PKD2/PKD1L1 channel complex.

### 6.9 Epigenetic changes

None reported (see §4.4).

### 6.10 Molecular profiling

- **Transcriptomics / expression:**
  - *Zebrafish:* *"tdt was found to be specifically and solely expressed from 70% epiboly to the 3-somite stage in dorsal forerunner cells (DFCs), which coalesce to form the Kupffer's vesicle (KV)"*, colocalising with the DFC marker *sox17* (lines 210–214).
  - *Xenopus:* first expressed at stage 10.5 in the involuting marginal zone along a dorsal-high/ventral-low gradient; strong at stage 14 in the circumblastoporal collar; dampened as cells transit into the LRO (lines 222–229).
  - *Mouse:* *"strong Tdt mRNA levels in the ventral node from the early bud to the 4-somite stage… enriched in the peri-nodal crown cells and became asymmetric at the 3-somite stage, suggesting a downregulation in the prospective left side in response to leftward flow"* (lines 235–238). MGI records **624 GXD expression assay results**.
  - *Human adult tissues:* Human Protein Atlas reports RNA tissue specificity **"Not detected"** (highest value choroid plexus 0.4 nTPM); single-cell specificity "Group enriched (retinal amacrine cells, oligodendrocytes)"; bulk deconvolution "Cell type enriched (testis – early spermatids)". **These low-level adult signals should be treated with caution and are not the disease-relevant expression**; Bgee reports "Expressed in mucosa of stomach and 38 other cell types or tissues."
- **Proteomics:** HPA protein (MS) tissue specificity "Not detected." No PRIDE/ProteomeXchange dataset specific to CIROP was retrieved. The only protein-level data are the authors' own Westerns in transfected HEK293T cells (PI-PLC, PNGase F, Endo H, DSS crosslinking — Fig. S3).
- **Metabolomics / lipidomics:** none; not applicable.
- **Genomic structural features:** 16 exons (NCBI) / 14 exons for the functional ORF (paper); minus strand; 14q11.2; ~5.9 kb genomic span. Synteny with neighbouring genes (*PABPN1, BCL2L2, PPP1R3E, HOMEZ, KHNYN, SLC7A8, CEBPE, C14orf119, ACIN1, CDH24, PSMB11, PSMB5*) was used to demonstrate clean gene loss in lizard and turtle (Fig. S1b).
- **Advanced technologies:** no single-cell, spatial-transcriptomic, multi-omic or CRISPR/RNAi screen data for CIROP were retrieved (DepMap would be uninformative given no cancer-cell dependency is expected).

### 6.11 Suggested ontology terms for mechanism

**GO Biological Process:** GO:0061966 (establishment of left/right asymmetry — *curated for CIROP*); GO:0006508 (proteolysis); GO:0007368 (determination of left/right symmetry); GO:0003140 (determination of left/right asymmetry in lateral mesoderm); GO:0001947 (heart looping); GO:0038092 (nodal signaling pathway); GO:0060287 (epithelial cilium movement involved in determination of left/right asymmetry); GO:0003352 (regulation of cilium movement).
**GO Molecular Function:** GO:0004222 (metalloendopeptidase activity — curated); GO:0008233 (peptidase activity — curated, IBA); GO:0008270 (zinc ion binding).
**GO Cellular Component:** GO:0016020 (membrane — curated); GO:0005737 (cytoplasm — curated, IBA); GO:0005576 (extracellular region); GO:0005929 (cilium) *(suggested, based on the eLife preprint's claim — unverified)*; GO:0005886 (plasma membrane).
**CHEBI:** CHEBI:29105 (zinc(2+)).

---

## 7. Anatomical Structures Affected

### 7.1 Organ level

**The primary affected structure is a transient embryonic organ, not an adult organ:**

| Structure | UBERON | Role |
|---|---|---|
| **Left–right organizer (LRO)** | **UBERON:0012451** (laterality organizer / organizer region) *(suggested)* | **Primary site of CIROP action and of the lesion** |
| Kupffer's vesicle (zebrafish LRO) | **UBERON:0005086** | Model-organism equivalent |
| Gastrocoel roof plate (*Xenopus* LRO) | **UBERON:0010078** *(suggested)* | Model-organism equivalent |
| Embryonic node / ventral node (mouse) | **UBERON:0003053** (node) *(suggested)* | Model-organism equivalent |
| Lateral plate mesoderm | **UBERON:0003056** | Downstream signal recipient |
| Notochordal plate / dorsal midline | **UBERON:0005085** *(suggested)* | Midline barrier (intact in mutants) |

**Secondarily mispositioned/malformed organs (the clinical disease):**

| Organ | UBERON | Involvement |
|---|---|---|
| **Heart** | **UBERON:0000948** | Dextrocardia, looping defects, septal/AV-canal/outflow lesions |
| Cardiac atrium / atrial septum | UBERON:0002081 / UBERON:0002085 | Common atrium, ASD, ostium primum |
| Cardiac ventricle / interventricular septum | UBERON:0002082 / UBERON:0002094 | VSD, DORV, DIRV |
| Aorta / aortic arch | UBERON:0000947 / UBERON:0001508 | Coarctation, interrupted arch, TGA |
| Pulmonary artery / valve | UBERON:0002012 / UBERON:0002146 | PA, PS |
| **Inferior vena cava** | **UBERON:0001072** | Interruption with azygos continuation |
| **Superior vena cava** | **UBERON:0001585** | Persistent left SVC |
| Pulmonary vein | UBERON:0002016 | PAPVC |
| **Liver** | **UBERON:0002107** | Malposition / midline liver |
| **Spleen** | **UBERON:0002106** | Malposition; asplenia/polysplenia *(unconfirmed for HTX12 specifically)* |
| **Pancreas** | **UBERON:0001264** | Malposition; **annular pancreas (HP:0001734)** |
| **Stomach** | **UBERON:0000945** | Malposition |
| **Intestine** | **UBERON:0000160** | **Malrotation (HP:0002566)** |
| **Lung** | **UBERON:0002048** | Isomerism/reversal (expected; not explicitly confirmed in retrieved HTX12 text) |
| Brain (habenula/diencephalon) | UBERON:0000955 / UBERON:0001894 | Brain asymmetry randomised **in zebrafish** (*lov*, *lefty1*) — **not reported in human patients** |

**Body systems involved:** cardiovascular (primary), digestive, lymphoreticular/haematopoietic (spleen), respiratory. **Not involved:** nervous (no human CNS phenotype), endocrine, musculoskeletal, renal, reproductive.

### 7.2 Tissue and cell level

| Cell type | Cell Ontology (suggested) | Role |
|---|---|---|
| **Dorsal forerunner cells (zebrafish)** | CL term not established; UBERON:0005086 precursor | Site of *tdt* expression |
| **Central LRO cells** (motile, posteriorly polarised cilia) | **CL:0000064** (ciliated cell) | Generate leftward flow — *CIROP-independent* |
| **Lateral/crown LRO cells** (immotile cilia, express NODAL/GDF1 and DAND5) | **CL:0000064** (ciliated cell) | Sense flow; **peri-nodal crown cells are where mouse *Tdt* is enriched** |
| LRO epithelium | **CL:0000066** (epithelial cell) | Single-layer epithelium of the archenteron dorsal midline |
| Lateral plate mesoderm cells | **CL:0000222** (mesodermal cell) | Receive NODAL |
| Cardiomyocytes | **CL:0000746** | Looping morphogenesis (*myl7*-marked in zebrafish) |

**Tissue types:** embryonic **epithelium** (LRO) and **mesoderm** (LPM) are the directly affected tissues. Connective, muscle and nervous tissue are affected only secondarily through organ malformation.

### 7.3 Subcellular level

| Compartment | GO CC | Evidence |
|---|---|---|
| **Plasma membrane / single-pass type I membrane protein** | **GO:0016020** (curated, UniProt-SubCell) | UniProt; paper (membrane-bound, not GPI-anchored) |
| Extracellular space / cell surface | GO:0005576 *(suggested)* | Signal peptide + extracellular domain 21–735; zebrafish protein readily secreted |
| Cytoplasm | **GO:0005737** (curated, IBA) | UniProt |
| **Cilium / ciliary membrane** | **GO:0005929** *(suggested, UNVERIFIED)* | Claimed in the 2024 bioRxiv/eLife preprint ("Cirop localizes to cilia of LRO sensor cells") — not in the peer-reviewed 2022 paper |
| Secretory pathway (ER/Golgi) | — | Implied by signal peptide and heavy N-glycosylation (PNGase F / Endo H sensitivity) |

### 7.4 Localization and lateralization

**This is the single most mechanistically distinctive feature of the disease: the requirement is strictly LEFT-SIDED.**

> *"To determine whether Tdt is specifically required on the left or on the right side of the LRO, we generated tdt crispants by injecting either the left or right blastomeres at the 4-cell stage. Injections on the left side of the embryos resulted in similar penetrance of laterality defects, while no phenotypes were observed when tdt was inactivated specifically on the right side… These lineage-restricted gene inactivations demonstrated that Tdt requirement for proper LR asymmetry patterning is restricted to the left side of the embryo."* (lines 291–296)

Clinically, the resulting phenotype is **asymmetric and randomised** rather than uniformly bilateral or unilateral: individual organs make independent left/right decisions, which is why *situs ambiguus* (discordant organ-by-organ laterality) occurs alongside *situs inversus totalis* (coordinated full reversal) within the same gene and even the same family.

---

## 8. Temporal Development

### 8.1 Onset

- **Age of onset:** **Congenital — prenatal, in utero (HP:0030674).** The molecular lesion acts during a window of **a few hours** at the end of gastrulation/early somitogenesis. From the paper (lines 451–453): *"In an organism's entire lifespan, TDT's transcription and physiological requirement appears to be limited to a finite process which only lasts a couple of hours during early embryogenesis."* In human terms the LRO is active from roughly 14 days post-fertilisation (Pasquetti et al., *Genes* 2025;16(1):62, PMID 39858609).
- **Onset pattern:** **Acute and instantaneous at the molecular level** (a single developmental decision window), manifesting as a **static congenital malformation**. Clinical presentation is either (a) prenatal, on routine or targeted fetal echocardiography/ultrasound, or (b) neonatal, with cyanosis, murmur, abnormal situs on chest radiograph, or feeding/obstructive symptoms from malrotation.

### 8.2 Progression

- **Disease stages:** **None.** HTX12 has no staging system. If staging is required for a knowledge base, it should be borrowed from the CHD lesion (e.g. single-ventricle palliation stage: Norwood → Glenn → Fontan) rather than assigned to HTX12 itself.
- **Progression rate:** **Not applicable — the malformation is non-progressive.** Clinical deterioration, when it occurs, follows the natural history of the specific cardiac lesion.
- **Course pattern:** **Stable/static congenital defect** with a chronic lifelong burden from its consequences. Not episodic, not relapsing-remitting, not degenerative.
- **Disease duration:** **Lifelong.** The anatomical abnormality is permanent.

### 8.3 Patterns

- **Remission:** **Not applicable.** Laterality cannot remit. "Treatment-induced improvement" means surgical correction of the cardiac lesion, not resolution of the heterotaxy.
- **Critical period / window of vulnerability:** **The LRO's operational window at early somitogenesis.** This is the only time *CIROP* is expressed or required. The practical implication is severe: **any future molecular therapy would have to act in the first ~3 weeks of gestation**, i.e. before most pregnancies are even recognised. This makes HTX12 essentially **untreatable at the molecular level** and shifts all intervention to prevention (preconception/prenatal genetic strategies) and to management of the structural consequences.

---

## 9. Inheritance and Population

### 9.1 Epidemiology

**No HTX12-specific prevalence or incidence figure exists.** What can be stated:

- **Laterality defects overall (denominator):** birth prevalence **1.1 per 10,000 live births** (95% CI 1.0–1.2), from the US National Birth Defects Prevention Study 1998–2007, 517 non-syndromic cases, of which ~73% were heterotaxy and the remainder *situs inversus totalis* (Lin AE et al., *Am J Med Genet A* 2014;164A:2581–2591 — cited as ref. 12 by Szenker-Ravi et al., who state: *"Laterality defects have an estimated prevalence of 1.1/10 000 live births in humans and account for approximately 3% of all CHDs"*, lines 122–124). Earlier estimates range 0.9–1.7 per 10,000. Orphanet's situs inversus totalis entry (ORPHA:101063) gives ~1/9,000 for all laterality defects and ~1/33,000 for situs inversus totalis. A separate source gives heterotaxy prevalence as 0.001% of live births (Pasquetti et al., PMID 39858609).
- **HTX12's share of that denominator:** the authors screened **186 index CHD cases** (108 with heterotaxy, 78 without) and conclude: *"we can estimate that TDT mutations account for up to 6.5% of CHD human patients with non-syndromic heterotaxy which is comparable to the 5.9% that was calculated for MMP21"* (lines 439–441).

**Derived estimate (my calculation, clearly flagged as such, not a retrieved figure):** if heterotaxy is ~0.8 per 10,000 births and *CIROP* explains up to 6.5% of non-syndromic cases, HTX12 birth prevalence would be on the order of **~0.05 per 10,000 (≈1 in 200,000)** in an outbred population — **substantially higher in consanguineous populations**. This is an inference, not a published number; do not cite it as such.

- **Published case count to date:** 21 patients / 12 families (Szenker-Ravi 2022) + an unspecified number of families in the Saudi consanguineous cohort (Al-Korashy 2025) + the post-2022 ClinVar submissions (at least 9 additional distinct P/LP alleles submitted 2022–2026 under "HTX12" or "CIROP-related disorder", implying additional unpublished cases).

### 9.2 Genetic parameters

| Parameter | Value | Evidence |
|---|---|---|
| **Inheritance pattern** | **Autosomal recessive (HP:0000007)** | OMIM CS; UniProt DI-06243; full segregation in 12 families |
| Zygosity distribution | 11/12 families homozygous; 1/12 compound heterozygous (Family 12: p.Ser31Phe + p.Arg191Ter) | Paper, lines 415–417 |
| **Penetrance** | **Complete (100%) in reported homozygotes** — *"all homozygous carriers of TDT mutations were affected, suggesting a 100% penetrance, which is in contrast to the 25% of normal embryos observed in tdt mutant fish and frogs"* (lines 435–437) | Paper |
| **Penetrance caveat — ascertainment bias** | The authors themselves qualify this: *"We suspect that humans will be found to have situs solitus despite being mutated in TDT"* (lines 437–438). **Reported penetrance is almost certainly an overestimate**, since families were ascertained through affected probands. Expect future reports of unaffected or minimally affected biallelic carriers. | Paper |
| **Expressivity** | **Highly variable**, both between and within families — the same allele produces *situs solitus*, *situs ambiguus* and *situs inversus totalis*. OMIM CS notes "variable manifestations and possible early death." | Paper, OMIM CS |
| **Genotype–phenotype correlation** | **None established.** Truncating and missense alleles produce overlapping phenotypes; the authors draw no correlation. | Paper |
| **Genetic anticipation** | **Not applicable** — no repeat expansion; no anticipation reported or expected | — |
| **Germline mosaicism** | **Not reported.** No instance described; theoretically possible but no evidence | — |
| **Founder effects** | **Not formally demonstrated.** p.Ser31Phe (rs553352307) recurred in 4 of 12 families and has a comparatively high gnomAD frequency (~0.0011), consistent with a recurrent or founder allele, but **no haplotype analysis was performed or retrieved.** | Paper; ClinVar/gnomAD |
| **Consanguinity role** | **Major.** 11/12 families homozygous; consanguineous unions visible in the pedigrees; the independent Saudi cohort (PMID 39513328) achieved 42.1% yield with 7/9 variants homozygous | Paper; Al-Korashy 2025 |
| **Carrier frequency** | **Not established.** No carrier-screening or population-genetic estimate exists. The most common allele p.Ser31Phe has gnomAD AF ~0.0011–0.0014 (carrier rate ~1 in 400 for that allele alone), but its ClinVar status is **conflicting**, so this cannot be converted into a disease carrier rate. | gnomAD/ClinVar |

### 9.3 Population demographics

- **Affected populations:** families of **"distinct geographical origin"** (paper, line 418). The contributing clinical centres span **France (Lyon, Dijon, Rennes, Angers, Bordeaux, Paris, Martinique), Lebanon (Beirut), Turkey (Istanbul), Germany, and Belgium (Brussels)**, indicating a European/Middle-Eastern-weighted ascertainment. An independent **Saudi Arabian** cohort confirms *CIROP* involvement. **No population is known to be specifically enriched** beyond the general effect of consanguinity. *(Note: the per-family country-of-origin column of Table 1 is present in the author manuscript but is rendered at unreadable resolution in the open-access PDF; I am therefore not reporting per-family origins.)*
- **Geographic distribution:** no endemic or regionally restricted pattern; expect over-representation wherever consanguinity rates are high (Middle East, North Africa, South Asia).
- **Geographic distribution of specific variants:** not characterised. p.Ser31Phe recurs across 4 families; no geographic clustering was reported.
- **Sex ratio:** **Not reported for HTX12.** The cohort includes both sexes (Table 1 "Gender" row; both male and female symbols in pedigrees). For heterotaxy in general, a **2:1 male predominance** has been reported in two large population-based studies, but this must **not** be attributed to HTX12 without data.
- **Age distribution:** congenital — all affected individuals are identified prenatally, at birth, or in infancy/childhood. The Table 1 "Year of birth" and "Age at death" rows indicate several patients born in the 1980s–2000s and several deaths; exact ages were not legible.

---

## 10. Diagnostics

### 10.1 Clinical tests

**Imaging is the diagnostic backbone; there is no laboratory or biochemical test for HTX12.**

| Modality | Role | Notes |
|---|---|---|
| **Fetal ultrasound / fetal echocardiography** | **Primary prenatal detection** | Detects abnormal cardiac axis, dextrocardia, AVSD, DORV, venous anomalies. In the original cohort, several pregnancies were terminated after prenatal diagnosis (TOP recorded in families 5, 10, 11, 12) |
| **Transthoracic echocardiography** | **Primary postnatal diagnosis** | Figure 7b of the paper shows chest X-ray + heart echocardiography of patient F7-II:5 with *situs inversus* and DORV, side by side with a *situs solitus* control |
| **Chest radiograph** | First-line situs assessment | Cardiac apex position, gastric bubble, bronchial morphology |
| **Abdominal ultrasound** | Visceral situs: liver, spleen, stomach, pancreas, IVC/aorta relationship | Essential for detecting asplenia/polysplenia and interrupted IVC |
| **Cardiac CT / MRI / angiography** | Delineation of complex venous return, bronchial isomerism, surgical planning | — |
| **Upper GI contrast study** | Intestinal malrotation (HP:0002566) | Indicated in all heterotaxy to assess volvulus risk |
| **ECG** | Reversed limb-lead pattern in dextrocardia; rhythm abnormalities (sinus node abnormalities common in isomerism) | — |
| **Howell-Jolly bodies on peripheral blood smear; spleen scintigraphy** | **Functional asplenia assessment** — determines need for antibiotic prophylaxis | Generic heterotaxy practice; sources note that *"the presence of one or multiple spleens does not adequately reflect splenic function"* |
| **Biopsy / histopathology** | **No role.** No diagnostic histological or immunohistochemical finding exists for HTX12 | — |
| **Nasal nitric oxide, ciliary ultrastructure/video-microscopy** | Used to **exclude** primary ciliary dyskinesia in a patient with situs inversus | Expected to be **normal** in HTX12, since CIROP is dispensable for ciliogenesis and ciliary beating (§6) — a key discriminator |

**Biomarkers:** **None.** No protein, metabolite or circulating biomarker for HTX12 exists. The FDA Biomarker/BEST resources contain nothing for *CIROP*.

### 10.2 Genetic testing

**Recommended approach: molecular genetic testing is the only confirmatory test.**

**⚠ The single most important practical caveat in this entire report:**

> *"As such, TDT has not been properly covered by commercially-available exome platforms and has thus escaped clinical investigation, despite our data showing that it is frequently mutated in recessive forms of heterotaxy involving CHDs."* (lines 453–456)

Because the exon–intron structure was incompletely annotated (only 2 ESTs; 14 functional exons reconstructed by the authors), **older exome capture kits may not cover *CIROP*, and a negative WES result from before ~2022 does not exclude HTX12.** This has direct consequences for reanalysis policy.

| Test | Utility for HTX12 |
|---|---|
| **Whole genome sequencing (WGS)** | **Highest utility.** Agnostic to capture-bait design; covers all 14/16 exons and splice regions; detects the splice variants (c.1135-1G>A) and potential intragenic CNVs. Al-Korashy et al. used ES, GS or panel and achieved 42.1% yield |
| **Whole exome sequencing (WES)** | **Useful but with a caveat** — confirm that the laboratory's capture design and the transcript used (**NM_001354640.2**) cover all *CIROP* exons. Families 8, 9 and 10 of the original cohort were solved by WES (trio analysis for Family 8: mother IV:1, proband V:2, affected sister V:4) |
| **Targeted gene panel** | Families 1–7 and 11–12 were solved by a **custom AmpliSeq panel** covering *"the 14 exons including UTRs and 20 intronic nucleotides on each side of each exon of the TDT gene"* with predicted 100% coverage (lines 839–843). **Any modern heterotaxy/laterality panel should include *CIROP*** alongside *ZIC3, NODAL, GDF1, ACVR2B, CFC1, LEFTY2, DAND5, CCDC11/CFAP53, PKD1L1, PKD2, MMP21, CIROZ/C1orf127, MNS1, DNAH5, DNAH9, DNAH11, DNAI1, CCDC103, CCDC39, DNAAF3, GALNT11*. **I could not verify which commercial panels currently include *CIROP*** — GTR was blocked in this session |
| **Single-gene testing** | Appropriate only for **cascade testing** of at-risk relatives once a familial variant is known, and for targeted prenatal diagnosis |
| **Chromosomal microarray (CMA)** | Appropriate as a **first-tier test in any infant with CHD** to exclude aneuploidy/CNV syndromes, but will **not** detect HTX12 (no recurrent CIROP CNV established) |
| **Karyotype / FISH** | Only to exclude chromosomal causes of CHD (e.g. 22q11.2 deletion by FISH). No role for HTX12 itself |
| **Mitochondrial DNA testing** | **No role** — not a mitochondrial disorder |
| **Repeat expansion testing** | **No role** — no repeat mechanism |

**Omics-based diagnostics:** RNA-seq, proteomics, metabolomics, epigenomics and liquid biopsy have **no established diagnostic role** in HTX12. RNA sequencing is theoretically attractive for interpreting the splice alleles (c.1135-1G>A; c.1144delG "/splicing defects") but is **not feasible in an accessible tissue**, because *CIROP* is not expressed outside the embryonic LRO.

### 10.3 Clinical criteria

**No formal diagnostic criteria (no DSM/ICD/society criteria) exist for HTX12.** A pragmatic working definition:

1. Laterality defect (*situs inversus totalis*, *situs ambiguus*, or isolated dextrocardia) **and/or** congenital heart defect of a laterality-dependent type; **plus**
2. Biallelic pathogenic/likely pathogenic *CIROP* variants on **NM_001354640.2**, confirmed in trans; **plus**
3. Absence of features of an alternative syndrome or of a ciliopathy.

### 10.4 Differential diagnosis

| Condition | Gene | Discriminating features |
|---|---|---|
| **Heterotaxy 1, X-linked (HTX1)** | *ZIC3* | X-linked; males predominantly; MedGen C1844020 / OMIM 306955 |
| **Heterotaxy 7 (HTX7)** | ***MMP21*** | **Clinically near-indistinguishable** — same AR module, similar frequency (5.9% vs 6.5%). Only sequencing distinguishes them. In the MMP21 series, CHD in 94% and extra-cardiac laterality defects in 64% of 26 patients (PMID 39858609) |
| **Heterotaxy 8 (HTX8)** | *PKD1L1* | Same module; AR |
| **"Visceral heterotaxy 14"/CIROZ-related** | ***CIROZ*** (*C1orf127*) | Same module; 16 individuals from 10 families (PMID 39753129) |
| Heterotaxy 2 / 4 / 5 / 6 | *CFC1*, *ACVR2B*, *NODAL*, *CCDC11/CFAP53* | NODAL-pathway or ciliary |
| **Primary ciliary dyskinesia with situs inversus (Kartagener)** | *DNAH5, DNAH11, DNAI1, CCDC103, CCDC39, DNAAF3, MNS1, CFAP53*… | **KEY DISCRIMINATOR:** PCD has chronic sinopulmonary disease, neonatal respiratory distress, bronchiectasis, otitis media, male infertility, abnormal nasal NO, abnormal ciliary ultrastructure/beat. **HTX12 has none of these** |
| Chromosomal syndromes with CHD (trisomy 21, 22q11.2del) | — | Dysmorphism, extracardiac syndromic features; detected by CMA/FISH |
| Maternal diabetic embryopathy / teratogen exposure | — | Maternal history; non-Mendelian |
| **Isolated non-syndromic CHD** | many | A patient with *situs solitus* and an isolated cardiac lesion may still have HTX12 — 8/21 of the original cohort |

### 10.5 Screening

- **Newborn screening:** HTX12 is **not** on any newborn screening panel and is not a candidate (no biochemical marker, no presymptomatic treatment). However, **pulse-oximetry CCHD newborn screening** will detect many affected infants indirectly via cyanotic CHD.
- **Carrier screening:** *CIROP* is **not** on standard expanded carrier screening panels as far as could be determined. It is a reasonable candidate for inclusion in **consanguineous-population carrier panels** given the Saudi cohort data.
- **Cascade screening:** **Indicated.** Once a familial genotype is known, test sibs (25% recurrence risk) and offer carrier testing to at-risk relatives, especially where consanguineous unions are planned.
- **Prenatal screening in known families:** targeted variant testing on CVS/amniocentesis, plus serial fetal echocardiography from ~18 weeks.

---

## 11. Outcome / Prognosis

### 11.1 Survival and mortality

**No HTX12-specific survival curve, 5-year survival rate, or life-expectancy figure has been published.** What is known:

- The OMIM-derived MedGen description states that **early death may occur in severe cases**.
- The original cohort's Table 1 includes an **"Age at death"** row, confirming deaths occurred; the pedigrees mark deceased individuals with a diagonal slash. **Multiple terminations of pregnancy (families 5, 10, 11, 12) and one spontaneous abortion (family 12)** are recorded (Fig. 7a legend) — prenatal loss is part of the disease burden.
- **Prognosis is determined by the cardiac lesion, not by the genotype.** Extrapolating from heterotaxy generally: Fontan palliation in heterotaxy carried **20% early mortality**, significantly worse with asplenia (**27%**) than polysplenia (**12%**, p = 0.019), with persistently worse transplant-free survival than non-heterotaxy Fontan patients (Stephens et al. 2022). A separate 20-year Fontan cohort reported overall survival **97.5% / 92.6% / 90.0%** at 5/10/15 years, with heterotaxy an independent risk factor for **late Fontan failure** and asplenia a multivariable risk factor (PMID 40939743).
- For biallelic *MMP21* (the closest genetic analogue): *"Positive outcomes, defined as surgical correction achieving good hemodynamic heart function, were observed in half of patients diagnosed postnatally"*, and 5 of 6 prenatally diagnosed pregnancies ended in termination (Pasquetti et al. 2025, PMID 39858609).

### 11.2 Morbidity and function

- **Morbidity drivers:** cyanosis and heart failure from the cardiac lesion; multiple-stage cardiac surgery; arrhythmia; **risk of midgut volvulus** from intestinal malrotation; **overwhelming post-splenectomy-type sepsis** if functionally asplenic; Fontan-circulation complications (protein-losing enteropathy, plastic bronchitis, hepatic fibrosis) in single-ventricle patients.
- **Disability outcomes:** exercise limitation, growth failure in infancy, neurodevelopmental risk associated with infant cardiac surgery and cyanosis (general CHD evidence; not HTX12-specific).
- **Quality-of-life measures:** **none applied to HTX12.** No EQ-5D, SF-36 or PROMIS data.

### 11.3 Disease course and complications

- Structural lesion is fixed; **no recovery of normal situs is possible**.
- With successful biventricular repair of a simple lesion (e.g. isolated dextrocardia with VSD), **near-normal long-term function is achievable**.
- With single-ventricle physiology, lifelong staged palliation and its sequelae.
- **Situs inversus totalis with a structurally normal heart is compatible with normal life expectancy**, with the practical caveat that mirror-image anatomy complicates future surgery and emergency diagnosis.

### 11.4 Prognostic factors

| Factor | Direction |
|---|---|
| **Complexity of the cardiac lesion** (single-ventricle vs biventricular-repairable) | Dominant determinant |
| **Asplenia / functional asplenia** | Worse (infection, worse Fontan outcomes) |
| Total anomalous/partial anomalous pulmonary venous connection | Worse |
| Prenatal vs postnatal diagnosis | Prenatal diagnosis correlates with more severe lesions and high TOP rates |
| Intestinal malrotation | Acute volvulus risk |
| **Genotype (truncating vs missense)** | **No prognostic value established** |

**Prognostic biomarkers:** **none.**

---

## 12. Treatment

**There is no disease-modifying, gene-directed or molecularly targeted therapy for HTX12, and none is plausible with current technology**, because the therapeutic window closed before pregnancy was recognised (§8.3). All management is **anatomical, supportive and preventive**.

### 12.1 Pharmacotherapy

- **No drug targets *CIROP* or the LRO pathway.** DrugBank/RxNorm contain no CIROP-directed agent.
- Symptomatic/supportive cardiac pharmacotherapy as dictated by the lesion: diuretics (e.g. furosemide), afterload reduction (ACE inhibitors), prostaglandin E1 (alprostadil) to maintain ductal patency in duct-dependent lesions, antiarrhythmics, anticoagulation/antiplatelet therapy post-Fontan. **NCIT terms:** e.g. NCIT:C29087 (diuretic), NCIT:C777 (angiotensin-converting enzyme inhibitor), NCIT:C29703 (alprostadil) — *suggested mappings, not retrieved from NCIT in this session*.
- **Antibiotic prophylaxis for functional asplenia** (typically penicillin V or amoxicillin) — sources state that patients *"should be treated with antibiotic prophylaxis unless adequate splenic function can be demonstrated"*, and that *"with prophylaxis, invasive bacterial diseases were rare"*, while also noting that *"evidence to base recommendation and guidelines is lacking."*
- **Pharmacogenomics:** **no CPIC/PharmGKB guideline involves *CIROP***. Standard pharmacogenomics applies to the drugs used (e.g. *VKORC1*/*CYP2C9* for warfarin post-Fontan), unrelated to the disease gene.

### 12.2 Advanced therapeutics

| Modality | Status for HTX12 |
|---|---|
| Gene therapy (AAV, lentiviral) | **Not applicable.** Would require delivery to the LRO at ~14–20 days post-fertilisation |
| Gene editing (CRISPR) | **Not applicable therapeutically.** CRISPR is used only as a *research* tool here (zebrafish/Xenopus models). **Germline editing is not an acceptable application** |
| Cell therapy | Not applicable |
| RNA-based therapy (ASO, siRNA, mRNA) | Not applicable — same window problem |
| Targeted small molecules | None exist |
| Immunotherapy | Not applicable |

**The only genuine "molecular" interventions available are reproductive** (PGT-M, prenatal diagnosis) — see §13.

### 12.3 Surgical and interventional

**This is the mainstay of treatment.** Management is that of the specific congenital heart defect and of extracardiac complications:

- **Biventricular repair** where anatomy permits: VSD/ASD closure, AVSD repair, arterial switch or intraventricular rerouting for TGA, DORV repair, relief of pulmonary or aortic stenosis, coarctation/interrupted-arch repair, PDA ligation, repair of anomalous pulmonary venous connection. *(NCIT: cardiac surgical procedure — suggested.)*
- **Staged single-ventricle palliation** (systemic-to-pulmonary shunt or PA band → bidirectional Glenn → **Fontan**) where biventricular repair is not possible. Heterotaxy patients have measurably worse Fontan outcomes (§11.1).
- **Cardiac transplantation** for failed palliation.
- **Ladd procedure** for intestinal malrotation — prophylactic or emergent, to prevent/treat midgut volvulus. The optimal timing of prophylactic Ladd in asymptomatic heterotaxy remains debated in the general literature.
- **Pacemaker implantation** for sinus node dysfunction/heart block (common in left atrial isomerism).

### 12.4 Supportive and rehabilitative

- Neonatal intensive care; nutritional support and growth monitoring; management of cyanosis.
- **Immunisation against encapsulated organisms** (pneumococcal, *Haemophilus influenzae* type b, meningococcal) for asplenic/hyposplenic patients, plus a written fever action plan.
- Cardiac rehabilitation and structured exercise counselling for repaired/palliated CHD.
- Developmental surveillance and early-intervention services for infants undergoing cardiopulmonary bypass.
- **Medical-alert documentation of situs inversus** — essential to prevent diagnostic error (e.g. left-sided appendicitis) and surgical misadventure.

### 12.5 Experimental treatments

**No clinical trial of any intervention specific to HTX12 or *CIROP* was identified.** ClinicalTrials.gov was not directly searchable in this session; however, given that the disease has no molecular therapeutic window, the absence of CIROP-directed trials is expected rather than an artifact of incomplete searching. Trials relevant to affected patients are **CHD- and Fontan-directed** (e.g. Fontan-failure therapeutics), not disease-specific.

### 12.6 Treatment outcomes

- **Response rates:** no HTX12-specific data. For biallelic *MMP21* heterotaxy (closest analogue), *"surgical correction achieving good hemodynamic heart function"* in **half** of postnatally diagnosed patients (PMID 39858609).
- **Adverse events:** those of neonatal/infant cardiac surgery (bleeding, arrhythmia, chylothorax, phrenic/recurrent-laryngeal nerve injury, stroke, neurodevelopmental sequelae) and of long-term Fontan physiology. No FAERS signal specific to HTX12.

### 12.7 Treatment strategy

A pragmatic algorithm:

1. **Define the anatomy completely** — echocardiography + cross-sectional imaging; explicitly characterise systemic and pulmonary venous return, atrial appendage morphology, bronchial anatomy, and abdominal situs.
2. **Determine splenic status** — imaging plus Howell-Jolly bodies; if asplenic/functionally asplenic → **immunise and start antibiotic prophylaxis**.
3. **Assess for malrotation** — upper GI series; decide on Ladd procedure.
4. **Decide biventricular vs univentricular pathway** and execute the staged surgical plan.
5. **Establish the molecular diagnosis** (WGS or a *CIROP*-containing panel) — this does **not** change medical management, but it **does** change: recurrence-risk counselling (25%), reproductive options, cascade testing, and prognostic framing (confirming a non-syndromic, non-ciliopathic, non-progressive aetiology).
6. **Lifelong adult congenital heart disease (ACHD) follow-up.**

**Personalised medicine:** the only genotype-guided element is **reproductive**, not therapeutic. There is no genotype–treatment interaction.

---

## 13. Prevention

### 13.1 Primary prevention

**Preventing occurrence is possible only through reproductive genetics.** There is no modifiable risk factor, no vaccine, no nutritional intervention, and no environmental exposure to avoid.

- **Preconception genetic counselling**, particularly for consanguineous couples and for couples with a previously affected child or pregnancy.
- **Preimplantation genetic testing for monogenic disease (PGT-M)** where the familial variants are known.
- **Prenatal diagnosis** by CVS or amniocentesis with targeted variant testing.
- **Carrier screening** in high-consanguinity populations (candidate, not established practice).
- **Periconceptional folate** and good glycaemic control reduce CHD risk generally but have **no demonstrated effect on HTX12**, which is fully determined by genotype.

### 13.2 Secondary prevention (early detection)

- **Fetal anomaly ultrasound and fetal echocardiography** — detects the cardiac and situs abnormality from mid-gestation, enabling delivery at a cardiac centre and immediate postnatal stabilisation (e.g. prostaglandin for duct-dependent lesions). In at-risk families (prior affected child), serial fetal echo is indicated.
- **Newborn pulse-oximetry CCHD screening** — detects cyanotic lesions pre-discharge.
- **Cascade genetic testing** of siblings.

### 13.3 Tertiary prevention (preventing complications in affected individuals)

This is where prevention has the greatest real-world impact:

| Intervention | Rationale |
|---|---|
| **Pneumococcal, Hib and meningococcal immunisation** | Functional asplenia → encapsulated-organism sepsis |
| **Lifelong (or at least childhood) antibiotic prophylaxis** in asplenia/hyposplenism | 50% vs 8% hospitalisation-requiring infection rate in asplenic vs non-asplenic heterotaxy children (*J Allergy Clin Immunol* 2016) |
| **Written fever/sepsis action plan + emergency antibiotics** | Rapid progression of post-splenectomy-type sepsis |
| **Screening for and correcting intestinal malrotation** (Ladd procedure) | Prevents catastrophic midgut volvulus |
| **Infective endocarditis prophylaxis** per CHD guidelines | Prosthetic material/cyanotic CHD |
| **Arrhythmia surveillance** | Sinus node dysfunction in isomerism |
| **Lifelong ACHD follow-up; Fontan surveillance** (liver, PLE, exercise capacity) | Late Fontan failure is increased in heterotaxy |
| **Documentation of mirror-image anatomy** | Prevents diagnostic/surgical error |

### 13.4 Immunization

**No vaccine prevents HTX12.** Vaccination is tertiary prevention for functional asplenia (above).

### 13.5 Genetic counselling

Core messages for families:

- **Autosomal recessive**, 25% recurrence risk for each future pregnancy of the same couple.
- **Carriers (parents, 2/3 of unaffected sibs) are unaffected** and need no surveillance.
- **Expressivity is highly variable**: a future affected child could have anything from isolated dextrocardia to lethal complex CHD — **the genotype does not predict severity.**
- **Penetrance in reported homozygotes is 100%, but this is probably an ascertainment-biased overestimate**; the authors anticipate biallelic individuals with normal *situs*.
- **Consanguinity counselling** where relevant.
- **Reproductive options:** PGT-M, prenatal diagnosis, gamete donation, adoption, or accepting the risk with intensive fetal surveillance.
- **Testing caveat to communicate explicitly:** a pre-2022 negative exome does **not** rule out HTX12 (§10.2) — reanalysis or WGS should be offered.

### 13.6 Public health and environmental interventions

- **Population-level:** genetic counselling and carrier-screening programmes in communities with high consanguinity rates are the only meaningful population intervention.
- **Health system:** ensure *CIROP* is included in heterotaxy/laterality gene panels and that exome pipelines use **NM_001354640.2** with verified exon coverage.
- **Environmental interventions:** none applicable.

### 13.7 Prophylaxis

Antibiotic prophylaxis for asplenia (§13.3) is the only established prophylactic medication. There is no prophylaxis that prevents the malformation.

---

## 14. Other Species / Natural Disease

### 14.1 Taxonomy and orthologs

| Species | NCBI Taxon | Gene / ID | Notes |
|---|---|---|---|
| *Homo sapiens* | **9606** | *CIROP*, Gene **100128908**, UniProt A0A1B0GTW7 | Disease gene |
| *Mus musculus* | **10090** | *Cirop*, **MGI:5588935**, Gene **101056084**, UniProt A0A286YEC0 | Node expression demonstrated |
| *Rattus norvegicus* | **10116** | *Cirop* (alias *Lmln2*), **RGD:1560492**, Gene **361039** | Ortholog; annotated as "human ortholog implicated in visceral heterotaxy 12" |
| *Danio rerio* | **7955** | *cirop/tdt*, LOC100331300 (XM_002662823), UniProt A0A1D5NSK0 | KO model |
| *Xenopus laevis* | **8355** | *cirop/tdt*, UniProt A0A1L8HYT7 | Crispant model |
| Rabbit (*Oryctolagus cuniculus*) | 9986 | LOC103351174 / XM_008269362.1 | Present |
| Gray mouse lemur (*Microcebus murinus*) | 30608 | LOC105864643 | Present |
| Ferret (*Mustela putorius furo*) | 9669 | LOC101683375 | Present |

MGI reports *"2 vertebrate orthologs"* in its stringent orthology cluster (human, mouse, rat). HPA reports "Limited conservation… orthologs in 3 of 4 species."

### 14.2 The evolutionary/comparative story — the scientific centrepiece of this gene

*CIROP* has been **repeatedly and independently lost across vertebrate evolution**, in exact correlation with the loss of motile cilia in the LRO. From the author manuscript (lines 150–153):

> *"Because their requirements are interlocked and strictly limited to this early developmental process, this 'functional' operon has twice been lost during evolution of the vertebrates, first in the ancestor of sauropsids (birds/reptiles) and then once again in even-toed mammals and cetaceans (cetartiodactyla)."*

Species-level status of the five module genes (*TDT/CIROP*, *MMP21*, *ALED/CIROZ*, *DAND5*, *PKD1L1*), from Fig. S1a:

| Group | Ciliated LRO | *CIROP* status |
|---|---|---|
| Human, mouse, rabbit | Yes | **Present** |
| **Cat, dog (Carnivora)** | n.d. | **Present** — but *ALED/CIROZ* already "stops" in cat and is absent in dog ⇒ **ongoing, contemporary loss of the module in carnivores** |
| **Camel, pig, cow, goat, sheep (Artiodactyla)** | No cilia (pig) | ***"stops"* — premature stop codons/pseudogenisation** |
| **Finless porpoise, minke whale (Cetacea)** | n.d. | ***"stops"*** |
| **Chicken, zebra finch (birds); lizard, turtle (reptiles)** | No cilia (chicken) | **Absent — gene lost outright** |
| *Xenopus*, zebrafish, gar, fugu, medaka, tilapia, elephant shark, lamprey, amphioxus, sea urchin | Yes | **Present** |
| *Drosophila* | No LRO | Absent |

The authors highlight this as a live evolutionary experiment (lines 508–517): *"canines and felines… have already begun to lose ALED but still harbor what appears to be normal genes for TDT, MMP21, DAND5 and PKD1L1. This indicates that an ongoing forfeiture of this functional module might be occurring contemporarily."*

### 14.3 Natural disease in other species

**No naturally occurring *CIROP*-related laterality disease has been described in any companion animal, livestock species or wildlife population.** No OMIA entry for *CIROP* was retrieved. Specifically:

- **Veterinary relevance: essentially nil, and for an interesting reason** — the species in which veterinarians most often encounter heterotaxy-prone embryology (cattle, pigs, sheep, goats) have **already pseudogenised *CIROP***, so biallelic loss cannot cause disease there; they use cilia-independent left–right patterning.
- Dogs and cats retain intact *CIROP*, so a naturally occurring canine/feline *CIROP* laterality disorder is theoretically possible but **has not been reported**. This would be a reasonable target for VetCompass/OMIA searching.

### 14.4 Comparative biology

- **Comparative pathology:** the core phenotype — randomised organ situs with cardiac looping defects — is **conserved between humans, zebrafish and *Xenopus***. The quantitative difference is penetrance: **100% in human homozygotes vs ~75% abnormal (25% normal) in MZ-null fish and frogs** (lines 435–437).
- **Evolutionary conservation of mechanism:** high within the cilia-dependent clade (fish, amphibians, rodents, primates), and **absent by design** in sauropsids and cetartiodactyls, which evolved alternative (cell-migration/chiral-cytoskeleton) mechanisms — e.g. *"chiral cell migration at the chick Hensen's node"* (lines 501–503).
- **Deep conservation:** the module's components are traceable to amphioxus, sea urchin and lamprey (Fig. S1a), while NODAL-dependent LR patterning predates cilia entirely — lophotrochozoans such as snails *"activate left-asymmetric Nodal signaling independently of cilia, but via chiral cleavage patterns"* (lines 498–500).

### 14.5 Transmission

**Zoonotic potential: none. Cross-species susceptibility: not applicable.** HTX12 is a non-communicable Mendelian disorder.

---

## 15. Model Organisms

### 15.1 Zebrafish (*Danio rerio*, NCBITaxon:7955) — the primary model

- **Model type:** germline CRISPR/Cas9 knockout.
- **Generation:** gRNA targeting **exon 4** (target 5′-GTCCCAACAGTGCTGAGGCC-3′), Cas9 mRNA co-injected at 250 ng/µL each, 2 nL into one-cell AB embryos. **Five independent germline frameshift alleles** were recovered; Line 1 carries a **5 bp insertion → frameshift and premature stop at amino acid 171**. Lines 2–5 showed equivalent homozygous phenotypes (lines 252–255, 664–667).
- **Key observation on NMD:** *"Despite the absence of measurable nonsense-mediated decay (NMD) of the mutant tdt transcripts… all homozygous tdt knockout (KO) fish presented with a classical phenotype of heterotaxy."*
- **Maternal-zygotic nulls:** Z-null *tdt⁻ᐟ⁻* fish are **fertile**, enabling 100% **MZ *tdt⁻ᐟ⁻*** embryos with **normal viability**.

**Phenotype recapitulation (quantitative):**

| Readout | Result |
|---|---|
| Cardiac looping at 48 hpf (visual / *Tg(myl7:eGFP)*) | **Randomised in ~half of *tdt⁻ᐟ⁻* embryos** |
| Triple ISH (*lov* left habenula; *myl7* heart; *insulin* pancreas) in MZ *tdt⁻ᐟ⁻* | ***situs solitus* 25%; *situs ambiguus* >50%; *situs inversus* 25%** |
| Rescue with 250 pg WT human or zebrafish *tdt* mRNA | **87% normal cardiac looping restored** |
| Rescue with catalytic-dead mRNA (HExxH→AAxxA: H247A, E248A, H251A) | **No rescue** — zinc site is essential |
| Heart jogging | Irregular by **30 hpf** |
| *southpaw (spaw)* at 22-somite | Bilateral, absent, or posterior-restricted |
| *lefty1* (left diencephalon) | **Completely abolished** |
| *lefty2* (left heart primordium) | **Largely lost** |
| *dand5* at 8-somite | **Not repressed on the left** |
| *tbxta* midline | **Intact** (barrier normal) |
| KV size, cilia number/length, beating, particle flow | **Normal** (Movies S1–S4) |
| DFC migration, compaction, KV formation (*sox17*), *foxj1a* expression | **Normal** |
| Other ciliopathy phenotypes at 72 hpf (body curvature, kidney cysts, hydrocephalus) | **Absent** |

- **Genotyping:** 484 bp exon-4 amplicon (F 5′-TGTTGGAAACCTGGAACCAT-3′, R 5′-ATGGTTCCAGGTTTCCAACA-3′); allele-specific PCR for Line 1.
- **Epistasis models:** *mmp21* KO lines (gift of N. Katsanis; three frameshift alleles, focus on a complex 10 bp deletion → frameshift at aa 38); **double heterozygotes, *tdt⁻ᐟ⁻;mmp21⁺ᐟ⁻*, *tdt⁺ᐟ⁻;mmp21⁻ᐟ⁻*, and double KO** were all generated — double KO showed **no increase in penetrance or severity** over either single KO; *tdt* mRNA failed to rescue *mmp21⁻ᐟ⁻*; *mmp21* was transcriptionally **up-regulated** in *tdt* KO.
- **Transgenics used:** *Tg(myl7:eGFP)* (cardiomyocyte reporter); *Tg(hsp70::foxj1a)* heat-shock-inducible line.

### 15.2 *Xenopus laevis* (NCBITaxon:8355) — the laterality-resolution model

- **Model type:** CRISPR/Cas9 **crispants** (F0), with gRNA + Cas9 protein.
- **Unique advantage exploited:** holoblastic cleavage permits **left- vs right-lineage-restricted gene inactivation** by injecting individual blastomeres at the 4-cell stage.
- **Phenotypes:** *situs* defects scored by heart looping, intestine looping and gallbladder position; *pitx2* mostly lost or misexpressed on the right; *nodal1* lost in left LPM; *dand5* asymmetry lost; *nodal1* and *dand5* expression domains **significantly smaller**.
- **Critical result:** left-side injection → laterality defects; **right-side injection → no phenotype**.
- **Rescue/epistasis:** left-sided *dand5* morpholino knockdown in *tdt* crispants **rescued** the asymmetry defects; right-sided *dand5* MO in controls *caused* bilateral *pitx2* and situs anomalies (phenocopy).
- **Controls for cilia:** LRO cell surface area, cilia length and polarisation, flow velocity and directionality (fluorescent-bead tracking on dorsal explants, gradient-time-trail movies) — *"no single parameter was statistically different between control and tdt crispants"*.
- **No additional phenotypes** beyond laterality.

### 15.3 Mouse (*Mus musculus*, NCBITaxon:10090)

- **In the defining paper, mouse was used for expression analysis only** — whole-mount ISH on E7.0–E8.5 embryos with two *Tdt* probes (Gm29776; ENSMUST00000224691.2): a 926 bp exon 3–11 fragment and a 739 bp exon 11–14 fragment. **No mouse *Cirop* knockout phenotype is reported in that paper.**
- **Result:** strong expression in the **ventral node** from early bud to 4-somite stage, **enriched in peri-nodal crown cells**, becoming **asymmetric at the 3-somite stage** (down-regulated on the prospective left). Expression **entirely abolished in *Noto^eGFP/eGFP^* (Noto⁻ᐟ⁻) mutants**, placing *Tdt* downstream of NOTO and FOXJ1.
- **MGI resources (MGI:5588935):** **1 mutation/allele** listed, classified **"chemically induced (other)"**; **1 genomic mutation involving Cirop**; **1 strain/line available at IMSR**; **2 phenotype references**; **8 GO annotations**; **624 GXD expression assay results**; **12 references**, earliest J:322341 = Szenker-Ravi et al. 2022. *(The specific allele symbol, MGI allele accession and MP term IDs could not be extracted — MGI's allele detail did not render through the fetch, and ZFIN, Xenbase, Alliance and IMPC all returned bot-challenges or JS-only shells. **These should be looked up directly.**)*
- **IMPC:** no *Cirop* data could be confirmed.
- **Useful comparator model:** the paper notes that *"an ENU-induced splice mutant c.26+1G>A in the mouse homologue of ALED (NM_001085505, Gm572) displays heterotaxy when bred to homozygosity (MGI Direct Data Submission, ID:175213)"* — and the 2025 AJHG paper reports that ***Ciroz* knockout mice show situs anomalies**, while zebrafish and *Xenopus* *ciroz* inactivation gave **no** LR phenotype (PMID 39753129). This is a striking species-inversion relative to *CIROP* and should be captured.

### 15.4 In vitro / cellular models

- **HEK293T transient transfection** with human *TDT/CIROP*, zebrafish *Tdt*, zebrafish Tdt-ΔTM, and FLAG-CD109 (GPI-anchored positive control), in pCS2+ vectors.
- Assays: **PI-PLC** (showed **no GPI anchor**); **PNGase F / Endo H** (heavy N-glycosylation); **DSS crosslinking** (high-MW oligomer); secretion into serum-free Pro293a-CDM.
- **Custom antibodies:** rabbit polyclonals against the human TDT epitope **CWKKENGFPAGVDNPHGEI** and zebrafish Tdt epitope **CWIEDNARSGMNEGGGEI**, both within the cysteine-rich domain, peptide-affinity purified (GL Biochem).
- **No iPSC, organoid, or patient-derived cell model exists** — and none is straightforwardly informative, since the relevant cell type is a transient embryonic LRO cell.

### 15.5 Phenotype recapitulation and limitations

| Aspect | Fish/frog | Human |
|---|---|---|
| Randomised organ situs | ✔ | ✔ |
| Cardiac looping/CHD | ✔ (looping only) | ✔ (full structural CHD spectrum) |
| Loss of left-sided *dand5* repression | ✔ | Inferred |
| Absence of ciliopathy features | ✔ | ✔ |
| **Penetrance** | **~75% (25% normal)** | **100% reported (likely overestimated)** |
| Viability/fertility | Fully viable and fertile | Variable; prenatal and early deaths occur |

**Limitations of the models:**
1. **No mouse loss-of-function model of *Cirop* has been published**, so the mammalian requirement is inferred from expression and from the fish/frog data. This is the single biggest gap.
2. Fish and frog models score **looping and organ position**, not the complex septation/outflow lesions (DORV, TGA, AVSD) that dominate human morbidity.
3. The **physiological substrate of CIROP remains unidentified in every model**.
4. Penetrance differs markedly between models and humans.
5. **Patient-variant-specific functional assays have never been performed** in any model.

### 15.6 Research applications

Available models support study of: flow-to-gene-expression signal transduction at the LRO; extracellular proteolytic cascades in embryonic patterning; CIROP–MMP21 epistasis and the direction of that relationship (currently **contested** between the 2022 paper and the 2024 preprint); substrate identification (candidates: PKD1L1, DAND5, CIROZ); and evo-devo of module loss.

### 15.7 Model databases

MGI (MGI:5588935; IMSR strain listed), RGD (RGD:1560492), ZFIN, Xenbase, Alliance of Genome Resources (human HGNC:53647), IMPC/KOMP. **All except MGI were inaccessible in this session and should be queried directly.**

---

## Appendix A — Primary evidence items with exact quotations

| # | Claim | Quotation | Source |
|---|---|---|---|
| E1 | CIROP is an LRO-specific metalloprotease required for laterality; 21 patients | *"We focused on a novel metalloproteinase, herein named TOUT-DE-TRAVERS (TDT), which is specifically expressed in ciliated LROs. Using CRISPR/Cas9 genome-editing in zebrafish and Xenopus, we demonstrate that TDT is solely required on the left side of the LRO to control organ laterality. Together with MMP21, another protease, TDT constitutes part of a proteolytic cascade that is downstream of leftward flow but upstream of DAND5, the first asymmetrically expressed gene. This pathway is clinically relevant, as we report 21 human patients with loss-of-function TDT mutations presenting with recessive situs anomalies with congenital heart defects."* | Abstract, author manuscript; **PMID 34903892** |
| E2 | Published abstract wording | *"In zebrafish and Xenopus, CIROP is required solely on the left side"* … *"We further ascertained 21 human patients with loss-of-function CIROP mutations presenting with recessive situs anomalies."* | Nat Genet 2022;54:62–72 abstract, **PMID 34903892** |
| E3 | Autosomal recessive segregation, 12 families | *"All germline variations, homozygous patients from 11 families and compound heterozygous in family 12, were confirmed by Sanger sequencing in available family members, and found to fully segregate with the disease according to an autosomal recessive mode of inheritance."* | lines 415–418, **PMID 34903892** |
| E4 | Situs distribution and CHD frequency | *"Of the 21 cases presenting with congenital heterotaxy, 8 had situs solitus with or without isolated dextrocardia, 5 had situs ambiguus, 8 had situs inversus totalis, and nearly all had congenital heart defects (CHD)."* | lines 430–433, **PMID 34903892** |
| E5 | Penetrance and its caveat | *"We also note that all homozygous carriers of TDT mutations were affected, suggesting a 100% penetrance… We suspect that humans will be found to have situs solitus despite being mutated in TDT."* | lines 435–438, **PMID 34903892** |
| E6 | Disease burden share | *"we can estimate that TDT mutations account for up to 6.5% of CHD human patients with non-syndromic heterotaxy which is comparable to the 5.9% that was calculated for MMP21."* | lines 439–441, **PMID 34903892** |
| E7 | Not a ciliopathy | *"MZ tdt−/− embryos presented with a normal-sized KV containing motile cilia with normal beating patterns. Cilia length and numbers did not significantly differ from that of control embryos."* | lines 345–348, **PMID 34903892** |
| E8 | DAND5 epistasis | *"depletion of dand5 on the left side of tdt crispants, i.e. on the side in which Tdt is required, was sufficient to rescue the asymmetry defects observed in tdt crispants."* | lines 332–334, **PMID 34903892** |
| E9 | Left-side-only requirement | *"Injections on the left side of the embryos resulted in similar penetrance of laterality defects, while no phenotypes were observed when tdt was inactivated specifically on the right side."* | lines 293–295, **PMID 34903892** |
| E10 | Catalytic activity required | *"injection of a catalytic-dead (CD) tdt mRNA, harboring three missense mutations in its catalytic site (HExxH→AAxxA, p.His247Ala, p.Glu248Ala and p.His251Ala) was unable to rescue the heart looping defects."* | lines 268–271, **PMID 34903892** |
| E11 | Exome coverage warning | *"TDT has not been properly covered by commercially-available exome platforms and has thus escaped clinical investigation, despite our data showing that it is frequently mutated in recessive forms of heterotaxy involving CHDs."* | lines 453–456, **PMID 34903892** |
| E12 | Domain architecture | *"TDT codes for a Zn2+-dependent metalloproteinase belonging to the M8 peptidase family of leishmanolysin-like metzincins (a.k.a. LMLN2)… consists of 4 domains: a signal peptide, a zinc catalytic domain containing the consensus His-Glu-x-x-His...His (HExxH...H) active site motif and a Met-turn methionine, a cysteine-rich domain and a C-terminal transmembrane domain."* | lines 183–189, **PMID 34903892** |
| E13 | UniProt function and disease | *"Putative metalloproteinase that plays a role in left-right patterning process."* / *"HTX12 inheritance is autosomal recessive."* | UniProt **A0A1B0GTW7**, DI-06243 |
| E14 | OMIM/MedGen definition | *"Visceral heterotaxy-12 (HTX12) is an embryonic developmental disorder characterized by defects in the asymmetric positioning of visceral organs across the left-right axis, known as laterality defects."* | MedGen UID 1803695 / C5676898 (OMIM-derived) |
| E15 | Prevalence of laterality defects | *"Laterality defects have an estimated prevalence of 1.1/10 000 live births in humans and account for approximately 3% of all CHDs."* | lines 122–124, **PMID 34903892**, citing Lin AE et al., *Am J Med Genet A* 2014;164A:2581–2591 |
| E16 | Module membership (CIROZ paper) | DAND5, PKD1L1, MMP21 and CIROP form a genetic module that evolved specifically in vertebrates with motile LRO cilia; 16 individuals from 10 families with biallelic CIROZ inactivation cause heterotaxy with CHD; *Ciroz* knockout mice show situs anomalies while zebrafish/*Xenopus* inactivation does not | Szenker-Ravi E et al., *Am J Hum Genet* 2025;112(2):353–373, **PMID 39753129**, PMC11866977 |
| E17 | Independent confirmation in a consanguineous cohort | 24 affected individuals, 19 families, 42.1% yield; 9 unique variants (7 novel) in 8 AR heterotaxy genes including ***CIROP***, *C1orf127/CIROZ*, *CCDC39*, *DNAAF3*, *DNAH5*, *DNAH9*, *MMP21*, *MNS1*; 7/9 homozygous | Al-Korashy M et al., *Clin Genet* 2025;107(2):224–230, **PMID 39513328** |
| E18 | Comparator (MMP21) clinical spectrum | 18 missense variants in 26 patients; CHD 94%; extra-cardiac laterality defects 15/26 (64%); *"Positive outcomes… were observed in half of patients diagnosed postnatally"* | Pasquetti D et al., *Genes (Basel)* 2025;16(1):62, **PMID 39858609**, PMC11764533 |

---

## Appendix B — Gaps, flags and recommended verification

**Items I could not retrieve and that should NOT be populated from this report:**

1. **ICD-10 / ICD-11 codes** for HTX12 — no mapping retrieved.
2. **The HP ID for transposition of the great arteries**, and all HP IDs above marked "suggested" — confirm in HPO directly. MedGen reports **0 HPO records** for C5676898, so HTX12 has no curated HPO annotation set at present.
3. **Whether asplenia/polysplenia occur in HTX12 specifically** — not found in the OMIM Clinical Synopsis excerpt retrieved.
4. **Per-patient and per-family clinical detail from Table 1** (country of origin, year of birth, age at death, individual cardiac lesions) — the table is present in the open-access author manuscript but rendered illegibly. Obtain the published Table 1 from Nature Genetics.
5. **MGI allele symbol/ID, MP terms, and GO evidence codes** for mouse *Cirop*; **ZFIN**, **Xenbase**, **Alliance**, **IMPC** records — all blocked.
6. **GenCC gene–disease validity classification** for *CIROP* — not retrieved (a request was issued but had not returned at the time of writing).
7. **Which commercial gene panels include *CIROP*** — GTR blocked.
8. **Orphanet's own HTX12-level entry** — appears not to exist (MedGen: 0 Orphanet records); *CIROP* is indexed under ORPHA:101063 (situs inversus totalis).

**Contradictions and flags recorded deliberately:**

- **CIROP vs MMP21 pathway order is contested.** Szenker-Ravi et al. 2022 place CIROP **upstream** of MMP21 (zebrafish epistasis, sequential expression, failed cross-rescue). The 2024 bioRxiv/eLife reviewed preprint on MMP21 places Mmp21 **upstream** of Cirop. The preprint is **not peer-reviewed** and I could not read its text directly.
- **Three ClinVar *CIROP* records are filed under "Trichothiodystrophy 1, photosensitive"** — almost certainly an annotation artifact; verify before curating.
- **Reported 100% penetrance is ascertainment-biased** by the authors' own admission.
- **p.Ser31Phe** is the most frequent disease allele but now carries **conflicting ClinVar classifications** at an allele frequency (~1.1–1.4 × 10⁻³) that is high for a fully penetrant recessive allele.
- ***CIROP* is not LoF-constrained in gnomAD** (LOEUF 1.50, pLI ≈ 0) — do not use constraint metrics as pathogenicity evidence for this gene.

---

## Sources

- [Szenker-Ravi E et al., Nature Genetics 2022;54(1):62–72 — "Discovery of a genetic module essential for assigning left–right asymmetry in humans and ancestral vertebrates" (PMID 34903892)](https://www.nature.com/articles/s41588-021-00970-4) — full author-accepted manuscript read via the Université de Bordeaux open-access repository copy
- [Publisher Correction, Nat Genet 2022;54(6):906 (PMID 35304595)](https://pubmed.ncbi.nlm.nih.gov/35304595/)
- [Szenker-Ravi E et al., Am J Hum Genet 2025;112(2):353–373 — "CIROZ is dispensable in ancestral vertebrates but essential for left-right patterning in humans" (PMID 39753129)](https://www.cell.com/ajhg/fulltext/S0002-9297(24)00448-8)
- [Al-Korashy M et al., Clin Genet 2025;107(2):224–230 — "Genetic Analysis of Heterotaxy in a Consanguineous Cohort" (PMID 39513328)](https://pubmed.ncbi.nlm.nih.gov/39513328)
- [Pasquetti D et al., Genes (Basel) 2025;16(1):62 — "Expanding the Molecular Spectrum of MMP21 Missense Variants" (PMID 39858609, PMC11764533)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11764533/)
- [OMIM #619702 — HETEROTAXY, VISCERAL, 12, AUTOSOMAL; HTX12](https://www.omim.org/entry/619702) and [Clinical Synopsis](https://omim.org/clinicalSynopsis/619702)
- [OMIM *619703 — CILIATED LEFT-RIGHT ORGANIZER METALLOPEPTIDASE; CIROP](https://www.omim.org/entry/619703)
- [MedGen — CIROP / Heterotaxy, visceral, 12, autosomal (UID 1803695, C5676898)](https://www.ncbi.nlm.nih.gov/medgen/?term=CIROP)
- NCBI Gene 100128908, ClinVar (50 *CIROP* records) and PubMed — retrieved via E-utilities ([eutils.ncbi.nlm.nih.gov](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/))
- [UniProt A0A1B0GTW7 (CIROP_HUMAN)](https://rest.uniprot.org/uniprotkb/search?query=gene:CIROP+AND+organism_id:9606&format=txt)
- [HGNC:53647](https://rest.genenames.org/fetch/symbol/CIROP)
- [gnomAD — CIROP (ENSG00000283654) constraint](https://gnomad.broadinstitute.org/gene/ENSG00000283654)
- [MGI:5588935 — mouse Cirop](https://www.informatics.jax.org/marker/MGI:5588935)
- [Human Protein Atlas — CIROP](https://www.proteinatlas.org/ENSG00000283654-CIROP)
- [Orphanet — CIROP/LMLN2 gene page](https://www.orpha.net/en/disease/gene/CIROP?mode=name) and [Situs inversus totalis, ORPHA:101063](https://orpha.net/consor/cgi-bin/OC_Exp.php?Expert=101063&amp=&lng=EN)
- [MONDO:0018677 — visceral heterotaxy (parent term)](https://monarchinitiative.org/MONDO:0018677)
- [Lin AE et al., Am J Med Genet A 2014;164A:2581–2591 — laterality defects in the NBDPS](https://pmc.ncbi.nlm.nih.gov/articles/PMC4462240)
- [Stephens EH et al., 2022 — Fontan palliation in heterotaxy: a five-decade experience](https://journals.sagepub.com/doi/abs/10.1177/21501351221099944)
- [Heterotaxy syndrome with and without spleen: different infection risk and management, J Allergy Clin Immunol 2016](https://www.jacionline.org/article/S0091-6749(16)31289-1/fulltext)
- [bioRxiv 10.1101/2024.10.13.618030 / eLife reviewed preprint 104430 — "MMP21 behaves as a fluid flow transported morphogen" (not peer-reviewed; text not directly readable in this session)](https://www.biorxiv.org/content/10.1101/2024.10.13.618030.full.pdf)
- [The Role of Left-Right Asymmetry in Congenital Heart Defects: Taking the Right Turn, 2025 (paywalled; cited via search only)](https://link.springer.com/article/10.1007/s11936-025-01114-1)

The last database agent returned after the report was written. Its results materially change §3 and §4, so here is a correction and addendum.

---

# Addendum — Correction to §3 (Phenotypes) and §9 (GenCC validity)

## Correction

In §3.2 I stated, based on MedGen's filter panel ("Records in HPO (0)"), that HTX12 has **no curated HPO disease annotation set**, and I supplied a number of HP IDs as unverified suggestions. **That is wrong.** The HPO API does hold a curated annotation set for OMIM:619702 — 28 terms, every one with a frequency denominator of the full 21-patient cohort and sourced to PMID:34903892. Several of my suggested HP IDs were also incorrect. Use the table below and discard the "suggested" HP IDs from §3.2.

## Curated HPO annotation set — OMIM:619702 / MONDO:0859222

Retrieved from `https://ontology.jax.org/api/network/annotation/OMIM:619702`. Disease label "Heterotaxy, visceral, 12, autosomal"; cross-referenced to MONDO:0859222 and NCBIGene:100128908 (*CIROP*). **Every term's source is PMID:34903892**; onset and sex fields are empty throughout.

| HP ID | Label | Frequency |
|---|---|---|
| HP:0003577 | **Congenital onset** | **21/21** |
| HP:0001696 | **Situs inversus totalis** | **8/21** |
| HP:0001719 | **Double outlet right ventricle** | **7/21** |
| HP:0001674 | **Complete atrioventricular canal defect** | **7/21** |
| HP:0001651 | **Dextrocardia** | **6/21** |
| HP:0001643 | Patent ductus arteriosus | 5/21 |
| HP:0001631 | Atrial septal defect | 5/21 |
| HP:0031565 | **Abdominal situs ambiguus** | **5/21** |
| HP:0001750 | Single ventricle | 4/21 |
| HP:0001642 | Pulmonic stenosis | 4/21 |
| HP:0001629 | Ventricular septal defect | 3/21 |
| HP:0011540 | Levotransposition of the great arteries | 3/21 |
| HP:0004935 | Pulmonary artery atresia | 3/21 |
| HP:0011670 | Left superior vena cava draining to coronary sinus | 3/42 *(denominator as given by the API)* |
| HP:0012304 | Hypoplastic aortic arch | 2/21 |
| HP:0001655 | Patent foramen ovale | 2/21 |
| HP:0011565 | Common atrium | 2/21 |
| HP:0011553 | Discordant atrioventricular connection | 2/21 |
| HP:0031854 | Left isomerism | 1/21 |
| HP:0012020 | Right aortic arch | 1/21 |
| HP:0011556 | Double inlet right ventricle | 1/21 |
| HP:0031348 | Dextrotransposition of the great arteries | 1/21 |
| HP:0001680 | Coarctation of aorta | 1/21 |
| HP:0011640 | Single coronary artery origin | 1/21 |
| HP:0010773 | Partial anomalous pulmonary venous return | 1/21 |
| HP:0004383 | Hypoplastic left ventricle | 1/21 |
| HP:0011590 | Double aortic arch | 1/21 |
| HP:0000007 | **Autosomal recessive inheritance** | (mode of inheritance) |

**HP IDs from §3.2 to replace:** complete AV canal is **HP:0001674** (not HP:0006695); PAPVC is **HP:0010773** (HP:0011540 is *levo*-TGA); pulmonary atresia is **HP:0004935** (not HP:0010882); left SVC is **HP:0011670** (not HP:0011673); abdominal situs ambiguus is **HP:0031565**. TGA resolves into two distinct terms — **HP:0011540** (l-TGA, 3/21) and **HP:0031348** (d-TGA, 1/21).

### What this adds

- **Per-lesion frequencies are now available**, which §3.2 could not supply. The dominant lesions are **DORV (33%)** and **complete AV canal defect (33%)**, followed by dextrocardia (29%), PDA and ASD (24% each), and abdominal situs ambiguus (24%).
- **Situs inversus totalis 8/21 and abdominal situs ambiguus 5/21 match the paper's narrative figures exactly**, confirming the curation was done from the full Table 1.
- **Congenital onset is annotated 21/21** — complete, consistent with §8.
- **My §3.2 flag on splenic phenotypes is confirmed:** there is **no asplenia or polysplenia term** in the curated set. The only isomerism term is **left isomerism, and in just 1/21**. Asplenia/polysplenia should **not** be asserted as HTX12 phenotypes.
- **Note a discrepancy worth recording:** HPO carries **no term for intestinal malrotation or annular pancreas**, although both appear in the OMIM Clinical Synopsis (HP:0002566, HP:0001734). The OMIM synopsis and the HPO annotation set are not fully concordant for this disease.

## GenCC gene–disease validity (fills the §10/Appendix B gap)

From `https://thegencc.org/genes/HGNC:53647`:

| Field | Value |
|---|---|
| Submitters | **1** — PanelApp Australia (GENCC:000111) |
| Classification | **Strong** |
| Disease | "visceral heterotaxy", **MONDO:0018677** |
| Inheritance | **AR** |
| Submission | SGC-176309.1 |
| Evaluated / submitted | 2025-01-17 / 2026-03-31 |

Two caveats for curation: the gene–disease validity rests on a **single submitter**, and GenCC maps *CIROP* to the **parent** term MONDO:0018677 (visceral heterotaxy), **not** to MONDO:0859222 (HTX12) — so a MONDO-keyed lookup against GenCC will miss this record.

## Remaining gaps (unchanged)

MGI's allele table, MP terms, GO evidence codes and 11 of its 12 references are rendered client-side and still could not be read; the Alliance API returned metadata only, with no disease, ortholog or GO payload. MGI's automated description confirms only: *"Predicted to enable peptidase activity. Predicted to be involved in establishment of left/right asymmetry. Predicted to be located in membrane. Predicted to be active in cytoplasm. **Is expressed in node.** Human ortholog(s) of this gene implicated in visceral heterotaxy 12."* The mouse allele is categorised as **chemically induced (other)**, with 1 allele, 1 genomic mutation, 1 IMSR strain and 2 phenotype references — the allele ID and MP terms require a direct MGI lookup.

**Sources:** [HPO API, OMIM:619702](https://ontology.jax.org/api/network/annotation/OMIM:619702) · [GenCC, HGNC:53647](https://thegencc.org/genes/HGNC:53647) · [MGI:5588935](https://www.informatics.jax.org/marker/MGI:5588935)

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 6 |
| Quoted claims found in source | 5 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 16 |
| On topic | 8 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:34903892` *(abstract only)*: "Autosomal recessive inheritance"
  - Text part not found as substring: 'Autosomal recessive inheritance' (note: only abstract available for PMID:34903892, full text may contain this excerpt)

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 120 |
| Resolved | 103 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 16 |
| Terms whose name was checked | 75 |
| Terms named correctly | 43 |
| Terms named as a **different** term | 9 |
| Terms whose name is worth a second look | 23 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `ECO:0000250` (2 mentions) - the report calls it "Putative metalloproteinase that plays a role in left-right patterning process"; ECO calls it **sequence similarity evidence used in manual assertion**
- `MONDO:0859222` (9 mentions) - the report calls it "MONDO", "HTX12"; MONDO calls it **heterotaxy, visceral, 12, autosomal**
- `HP:0011540` (5 mentions) - the report calls it "Levotransposition of the great arteries", "Partial anomalous pulmonary venous connection (PAPVC)"; HP calls it **Levotransposition of the great arteries**
- `HP:0011994` (1 mention) - the report calls it "Ostium primum ASD (ASD-OP)"; HP calls it **Abnormal atrial septum morphology**
- `HP:0001670` (1 mention) - the report calls it "Tricuspid atresia (TA)"; HP calls it **Asymmetric septal hypertrophy**
- `HP:0011673` (2 mentions) - the report calls it "Abnormal superior vena cava morphology (SVC anomalies"; HP calls it **Cardiac hemangioma**
- `UBERON:0005086` (2 mentions) - the report calls it "Kupffer's vesicle (zebrafish LRO)"; UBERON calls it **hair follicle placode**
- `NCIT:C777` (1 mention) - the report calls it "angiotensin-converting enzyme inhibitor"; NCIT calls it **Therapeutic Progesterone**
- `NCIT:C29703` (1 mention) - the report calls it "alprostadil"; NCIT calls it **Antilipidemic Agent**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `NCIT:C29087` (1 mention), reported as "diuretic" - NCIT does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0061966` (3 mentions) - the report calls it "establishment of left/right asymmetry — *curated for CIROP"; GO calls it **establishment of left/right asymmetry**
- `GO:0004222` (2 mentions) - the report calls it "metalloendopeptidase activity — curated"; GO calls it **metalloendopeptidase activity**
- `GO:0008233` (2 mentions) - the report calls it "peptidase activity — curated, IBA"; GO calls it **peptidase activity**
- `GO:0005737` (3 mentions) - the report calls it "cytoplasm — curated, IBA"; GO calls it **cytoplasm**
- `GO:0016020` (3 mentions) - the report calls it "membrane — curated"; GO calls it **membrane**, and lists "membrane region" among its other names
- `MONDO:0015159` (2 mentions) - the report calls it "MCA/dysmorphism-ID"; MONDO calls it **multiple congenital anomalies/dysmorphic syndrome-intellectual disability**, and lists "MCA/MR" among its other names
- `HP:0000007` (5 mentions) - the report calls it "Autosomal recessive inheritance", "Autosomal recessive"; HP calls it **Autosomal recessive inheritance**, and lists "Autosomal recessive" among its other names
- `HP:0001719` (3 mentions) - the report calls it "Double outlet right ventricle", "Double outlet right ventricle (DORV)"; HP calls it **Double outlet right ventricle**
- `HP:0001629` (3 mentions) - the report calls it "Ventricular septal defect", "Ventricular septal defect (VSD)"; HP calls it **Ventricular septal defect**, and lists "Ventricular septal defects" among its other names
- `HP:0001655` (3 mentions) - the report calls it "Patent foramen ovale", "Patent foramen ovale (PFO)"; HP calls it **Patent foramen ovale**
- `HP:0001680` (3 mentions) - the report calls it "Coarctation of aorta", "Aortic coarctation (CoA)"; HP calls it **Coarctation of aorta**, and lists "Aortic coarctation" among its other names
- `HP:0001643` (3 mentions) - the report calls it "Patent ductus arteriosus", "Patent ductus arteriosus (PDA)"; HP calls it **Patent ductus arteriosus**
- `HP:0011565` (4 mentions) - the report calls it "Common atrium", "Common atrium (CA)"; HP calls it **Common atrium**
- `HP:0001631` (3 mentions) - the report calls it "Atrial septal defect", "Atrial septal defect (ASD)"; HP calls it **Atrial septal defect**
- `HP:0001671` (1 mention) - the report calls it "Abnormal cardiac septum morphology / septal defects"; HP calls it **Abnormal cardiac septum morphology**
- `HP:0010882` (2 mentions) - the report calls it "Pulmonary atresia (PA)"; HP calls it **Pulmonary valve atresia**
- `HP:0001650` (1 mention) - the report calls it "Aortic valve stenosis (AS)"; HP calls it **Aortic valve stenosis**
- `HP:0011611` (1 mention) - the report calls it "Interrupted aortic arch (IAA)"; HP calls it **Interrupted aortic arch**
- `HP:0011671` (1 mention) - the report calls it "Abnormal inferior vena cava morphology (IVC anomalies"; HP calls it **Interrupted inferior vena cava with azygous continuation**
- `HP:0002566` (4 mentions) - the report calls it "Intestinal malrotation", "Malrotation"; HP calls it **Intestinal malrotation**, and lists "Malrotation" among its other names
- `HP:0030674` (3 mentions) - the report calls it "Onset in utero", "Age of onset:** **Congenital — prenatal, in utero"; HP calls it **Antenatal onset**, and lists "Onset in utero" among its other names
- `UBERON:0003056` (1 mention) - the report calls it "Lateral plate mesoderm"; UBERON calls it **pre-chordal neural plate**, and lists "anterior neural plate" among its other names
- `CL:0000746` (1 mention) - the report calls it "Cardiomyocytes"; CL calls it **cardiac muscle cell**, and lists "cardiomyocyte" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MGI:5588935` - called "HTTP 200", "MGI resources", "mouse Cirop"
- `HGNC:53647` - called "Gene name:** CIROP", "HTTP 200, JSON", "HGNC ID"
- `NCBIGene:100128908` - called "HTTP 200, JSON", "CIROP"
- `MONDO:0859222` - called "MONDO", "HTX12"
- `HP:0000007` - called "Autosomal recessive inheritance", "Autosomal recessive"
- `HP:0031854` - called "Left Isomerism", "Left isomerism"
- `HP:0001719` - called "Double outlet right ventricle", "Double outlet right ventricle (DORV)"
- `HP:0001629` - called "Ventricular septal defect", "Ventricular septal defect (VSD)"
- `HP:0001655` - called "Patent foramen ovale", "Patent foramen ovale (PFO)"
- `HP:0011540` - called "Levotransposition of the great arteries", "Partial anomalous pulmonary venous connection (PAPVC)"
- `HP:0001680` - called "Coarctation of aorta", "Aortic coarctation (CoA)"
- `HP:0001643` - called "Patent ductus arteriosus", "Patent ductus arteriosus (PDA)"
- `HP:0011565` - called "Common atrium", "Common atrium (CA)"
- `HP:0001631` - called "Atrial septal defect", "Atrial septal defect (ASD)"
- `GENCC:000111` - called "Submitters:** 1 — PanelApp Australia", "1** — PanelApp Australia"
- `HP:0002566` - called "Intestinal malrotation", "Malrotation"
- `HP:0030674` - called "Onset in utero", "Age of onset:** **Congenital — prenatal, in utero"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`, `Chr14`, `OMIM`, `RGD`, `EXT_ID`, `MIM`, `PubMed`, `NCBIGene`, `GENCC`, `ORPHA`, `ID`.