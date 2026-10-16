---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-15T15:31:19.262535'
end_time: '2026-10-15T15:35:50.637185'
duration_seconds: 271.37
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Visceral Heterotaxy 7
  mondo_id: MONDO:0014762
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
  - claude-haiku-5-5
  - claude-opus-5-5
  web_search_requests: 11
  num_turns: 27
  total_cost_usd: 2.1482095999999995
  session_id: 0acb721b-adaa-4714-a17b-1319f3ae064f
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - mcp__pubmed__search_articles
  assistant_text_blocks: 2
citation_count: 13
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 14
  on_topic: 10
  validator_version: 0.3.0
term_validation:
  total_terms: 37
  verified: 34
  not_found: 0
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 27
  labels_matching: 11
  labels_mismatched: 12
  mislabelled_terms:
  - term_id: MONDO:0014762
    reported_labels:
    - MONDO
    ontology_label: heterotaxy, visceral, 7, autosomal
  - term_id: HP:0011536
    reported_labels:
    - verify the label
    ontology_label: Right atrial isomerism
  - term_id: HP:0006695
    reported_labels:
    - verify
    ontology_label: Atrioventricular canal defect
  - term_id: HP:0001669
    reported_labels:
    - verify
    ontology_label: Transposition of the great arteries
  - term_id: HP:0004935
    reported_labels:
    - verify
    ontology_label: Pulmonary artery atresia
  - term_id: HP:0001642
    reported_labels:
    - verify
    ontology_label: Pulmonic stenosis
  - term_id: HP:0001750
    reported_labels:
    - verify
    ontology_label: Single ventricle
  - term_id: HP:0005160
    reported_labels:
    - verify
    ontology_label: Total anomalous pulmonary venous return
  - term_id: HP:0005301
    reported_labels:
    - verify
    ontology_label: Persistent left superior vena cava
  - term_id: HP:0012020
    reported_labels:
    - verify
    ontology_label: Right aortic arch
  - term_id: NCIT:C15329
    reported_labels:
    - Ladd procedure for symptomatic malrotation
    ontology_label: Surgical Procedure
  - term_id: NCBITaxon:8355
    reported_labels:
    - verify
    ontology_label: Xenopus laevis
  labels_variant: 4
  obsolete_terms:
  - term_id: GO:0005615
    ontology_label: obsolete extracellular space
    replaced_by: GO:0005576
  unresolvable_prefixes:
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Visceral Heterotaxy 7
- **MONDO ID:** MONDO:0014762 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Visceral Heterotaxy 7** covering all of the
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

I'm reading the main MMP21 papers; next I'll check the DDD study, OMIM, and the mouse ENU mutant.

# Visceral Heterotaxy 7 (HTX7; *MMP21*-related heterotaxy): Research Report

**Target:** Visceral Heterotaxy 7, autosomal (MONDO:0014762, OMIM #616749)
**Category:** Mendelian (autosomal recessive)
**Date:** 2026-10-15

## How this report was compiled

- **Sources:**
  - Primary papers, read through PMC full text or abstract pages: Perles 2015 (PMC4936483), Guimier 2015 (PMC5620017), Qin 2022 (PMC9484203) and Yuan 2020 (Frontiers).
  - A summary of the OMIM entry for #616749, via FindZebra.
  - Web-search metadata for Akawi 2015, Szenker-Ravi 2022, Pasquetti 2025 and Ott 2024/2025.
- **PubMed tools were not available in this session.** PubMed pages also returned cookie and CAPTCHA walls.
- **What to verify before citing:** Run `just fetch-reference` on every PMID, and copy evidence snippets only from the generated cache files. Look up every ontology CURIE below before binding it; each is a candidate, not a validated binding.
- **PMID status:**

| PMID | Paper | Status |
|---|---|---|
| 26429889 | Perles 2015 | Confirmed from the PMC record |
| 26437028 | Guimier 2015 | Confirmed from the PMC record |
| 36123719 | Qin 2022 | Confirmed from the PMC record |
| 26437029 | Akawi 2015 | Confirmed from the PubMed URL |
| 33240936 | Yuan 2020 | From a third-party listing only |
| 25807483 | Li 2015 | From memory, unverified |
| 34903892 | Szenker-Ravi 2022 | From memory, unverified; a search for it found nothing |
| — | Pasquetti 2025 | Not found; DOI 10.3390/genes16010062 is known |
| — | Ott 2024/2025 | Not a PubMed article; a bioRxiv preprint (10.1101/2024.10.13.618030) and eLife reviewed preprint RP104430 |

---

## 1. Disease information

**Overview.** HTX7 is an autosomal recessive laterality disorder caused by biallelic loss-of-function variants in *MMP21*, which encodes matrix metallopeptidase 21. Normal left–right (L-R) asymmetry fails to form in early embryonic development. The result is complex congenital heart disease (CHD) and/or abnormal placement of the abdominal and thoracic organs. Expression is variable: the range runs from situs inversus totalis without symptoms to lethal complex CHD with right atrial isomerism and asplenia. OMIM describes HTX7 as "a developmental disorder characterized by complex congenital heart malformations and/or situs inversus."

**Identifiers**

| Resource | ID |
|---|---|
| MONDO | MONDO:0014762 |
| OMIM (phenotype) | #616749, "Heterotaxy, visceral, 7, autosomal; HTX7" |
| OMIM (gene) | *608416 *MMP21* |
| HGNC | *MMP21*, candidate `hgnc:14357` (from memory; verify) |
| Orphanet | No HTX7-specific ORPHA code was found. The parent concept is heterotaxy / situs ambiguus; verify the ORPHA mapping through MONDO xrefs. |
| ICD-10 | Q89.3 (situs inversus) and Q20.6 (isomerism of atrial appendages) at the grouping level |
| LOVD | Diseases #05733 / #06071 |

**Synonyms:** HTX7; heterotaxy, visceral, autosomal, type 7; *MMP21*-related heterotaxy.

**Data provenance:** All knowledge comes from case and family reports and small cohorts. There are no registry or EHR data.

---

## 2. Etiology

- **Cause:** Biallelic germline *MMP21* variants (homozygous or compound heterozygous): frameshift, nonsense, exon deletion and missense. Two founding reports in 2015 (Perles; Guimier), plus the DDD study (Akawi 2015).
- **Contribution to heterotaxy:** In the Guimier cohort, *MMP21* explained about **5.9% of non-syndromic heterotaxy**. Of 264 index cases with heterotaxy or other CHD, 9 carried rare biallelic predicted-damaging variants (PMID:26437028).
- **Heterozygous risk (contested):** Qin et al. 2022 reported **de novo heterozygous** *MMP21* missense variants in 3 of 81 (3.7%) Chinese Han children with heterotaxy and complex CHD (p.G244E, p.L277F, p.K487E). The authors call them "potential predisposing genetic risk factors." This is not established monoallelic disease:
  - Expression assays showed that none of the variants changed mRNA or protein levels.
  - p.L277F rescued the zebrafish morphant phenotype as well as wild-type mRNA did.
  - Only p.G244E and p.K487E rescued poorly. The paper calls these both "dominant-negative" and "loss-of-function" and does not reconcile the two terms.
  - Treat these as heterozygous-susceptibility leads (`relationship_type: RISK_FACTOR`), not as evidence of causation (PMID:36123719).
- **Environmental, protective and gene–environment factors:** None reported for HTX7 specifically. Maternal diabetes is a recognised non-genetic risk factor for heterotaxy in general, but it is not documented for *MMP21*.
- **Modifiers and incomplete penetrance:** In Guimier family 8, three individuals were homozygous. One had situs inversus totalis and one was reported asymptomatic. This points to incomplete penetrance and variable expressivity, a known property of L-R randomisation (PMID:26437028). No modifier genes have been identified.

---

## 3. Phenotypes

The ontology candidates below must be verified with `runoak` or OLS before binding. Frequency figures come from small case series, so only qualitative bands are justified.

| Phenotype | HPO candidate (verify) | Notes and evidence |
|---|---|---|
| Heterotaxy / situs ambiguus | HP:0030853 Heterotaxy | Defining feature. In the mouse knock-in model, 61% of mutant embryos had situs inversus or heterotaxy (PMID:26437028). |
| Situs inversus totalis | HP:0001696 | Perles sib II-6 (asymptomatic); one homozygote in Guimier family 8 (PMID:26429889; 26437028) |
| Dextrocardia, including mirror-image | HP:0001651 | Perles II-3; Yuan 2020; Qin P58 and P7 |
| Right atrial isomerism | HP:0011536 (verify the label) | Qin P7 and P61; "cardiosplenic syndrome" |
| Atrial situs inversus | — (find a term) | Perles II-3 and II-7 |
| Asplenia | HP:0001746 | Perles II-3 |
| Atrioventricular septal defect / complete AV canal | HP:0006695 (verify) | Perles II-3 and II-7; Qin P61 |
| Transposition of the great arteries | HP:0001669 (verify) | Perles II-3 and II-7; Yuan; Qin P58. In mouse, CHD including TGA appeared in 32 of 33 mutant embryos. |
| Pulmonary atresia | HP:0004935 (verify) | Perles II-3 and II-7 |
| Pulmonary stenosis | HP:0001642 (verify) | Yuan; Qin P58 and P7 |
| Single ventricle | HP:0001750 (verify) | Yuan; Qin P7 and P61 |
| Ventricular septal defect | HP:0001629 | Qin P58 |
| Single atrium | — (verify) | Qin P7 |
| Total anomalous pulmonary venous return | HP:0005160 (verify) | Qin P7 |
| Persistent left / bilateral superior vena cava | HP:0005301 (verify) | Perles II-7; Qin P7 |
| Right aortic arch | HP:0012020 (verify) | Qin P7 |
| Double-outlet right ventricle, intestinal malrotation, polysplenia | HP:0001718, HP:0002566, HP:0001748 (verify) | Reported across the HTX spectrum. Per-patient *MMP21* data are in the Guimier supplementary tables and Pasquetti 2025 Table 1, which were not read. |
| Seizures | HP:0001250 | One Perles sib (II-7); probably incidental |
| Global developmental delay, dysmorphism | HP:0001263 | One Akawi patient; may be a coincidental or DDD-cohort effect |
| **Absent:** primary ciliary dyskinesia features | — | No respiratory or ciliary phenotype in any reported patient (Perles; Yuan). This separates HTX7 from PCD-associated situs anomalies. |

- **Onset:** All structural features are congenital and often detected prenatally.
- **Course:** Static anatomy. Morbidity depends on the CHD and its surgical palliation.
- **Quality of life:** No HTX7-specific data. It is driven by single-ventricle physiology, Fontan outcome, and asplenia-related infection risk.
- **Literature review (Pasquetti 2025, *Genes* 16:62):** 18 missense variants across 26 patients, mostly with CHD. Recurrent p.(Met301Ile) appeared in two unrelated heterotaxy patients. Homozygous and compound-heterozygous missense carriers did not differ in phenotype.

---

## 4. Genetic and molecular information

- **Gene:** *MMP21* at 10q26.2 (OMIM *608416). It encodes a secreted zinc-dependent metallopeptidase with a signal peptide, a propeptide, a catalytic domain and a hemopexin-like domain.

**Key variants (OMIM allelic variants .0001–.0012)**

| Variant (NM_147191 unless noted) | Type | Zygosity | Source |
|---|---|---|---|
| c.1024_1025delAA, p.K342fs (.0001) | Frameshift; escapes NMD and is predicted to truncate before the hemopexin domain | Homozygous (consanguineous family; absent from ExAC) | Perles 2015, PMID:26429889 |
| c.677T>C p.(Ile226Thr) + c.1203G>A p.(Trp401*) | Missense + nonsense | Compound heterozygous (dizygotic twins; one died on day 1) | Guimier 2015, PMID:26437028 |
| Exon 1–3 deletion + c.365delT p.(Met122Serfs*55) | Structural + frameshift | Compound heterozygous | Guimier 2015 |
| p.(Arg360Cys), p.(Arg375His), p.(Arg408Gly), p.(Ala321Pro), p.(Glu215…) | Missense / truncating | Biallelic | Guimier 2015 |
| Four alleles (.0009–.0012) | Mixed | Compound heterozygous (2 families) | Akawi 2015, PMID:26437029 |
| c.496G>T p.(Gly166*) | Nonsense; truncates after the propeptide | Homozygous; ACMG pathogenic; CADD 35; absent from 1000G, ExAC and EVS | Yuan 2020, *Front Cardiovasc Med* 7:582350 |
| p.(Met301Ile) | Missense | Biallelic; 2 unrelated patients | Pasquetti 2025 |
| p.G244E, p.L277F, p.K487E | Missense | De novo heterozygous (see §2 caveat) | Qin 2022, PMID:36123719 |

- **Functional consequence:** Loss of function. The variants are spread along the gene; catalytic-domain missense variants are proposed to abolish activity (Pasquetti 2025). Record as `functional_impact_category: LOSS_OF_FUNCTION`.
- **Allele frequency caveat:** In two Guimier families, one of the variants had been seen homozygous in ExAC, so those variants are unlikely to be causal in those families.
- **Origin:** Germline. No somatic or mosaic cases.
- **ClinGen:** No gene-disease validity curation was found in this search. Check with `just list-gene-validity` and the `CGGV:` cache before asserting a tier; do not assign one.
- **Epigenetics and chromosomal abnormalities:** None reported. A small intragenic deletion (exons 1–3) is the only structural variant known.

---

## 5. Environmental information

None reported. Not infectious. Leave `environmental` empty, or add a waiver noting that searches found nothing.

---

## 6. Mechanism and pathophysiology

### Causal chain

1. **Biallelic *MMP21* loss-of-function variants** remove MMP21 protein, or leave a truncated or catalytically defective protein. Shown in patients and in cell expression assays.
2. During early somitogenesis (zebrafish), *MMP21* is **expressed and secreted at the left-right organiser (LRO)**: the node in mouse, Kupffer's vesicle in zebrafish, the gastrocoel roof plate in *Xenopus*. Expression is restricted to Kupffer's vesicle from the 8- to 23-somite stage (PMID:26429889; 26437028).
3. **Motile cilia and leftward nodal flow are preserved.** Node cilia motility was normal in the ENU mice (Akawi 2015), and flow was unaltered in *mmp21*-null *Xenopus* (Ott 2024/25). The defect is therefore downstream of flow generation, which fits the absence of a PCD phenotype in patients.
4. **The flow response fails.** Without MMP21, the left-sided, flow-dependent repression of ***dand5*** (the Nodal antagonist Cerl2/Coco) does not occur. *nodal1* expression at the LRO is not reduced (Xenopus; Ott 2024/25, preprint).
   - **Proposed model (preprint, contested by eLife reviewers):** MMP21 acts as a flow-transported extracellular signal. It spreads over LRO cells and acts upstream of **CIROP**, a membrane metallopeptidase on LRO cilia. *MMP21*, *CIROP*, *PKD1L1*, *DAND5* and *C1orf127/CIROZ* form a co-evolving module. This module was lost in vertebrate lineages whose LROs lack motile cilia, which is why *MMP21* is absent or decaying in birds, reptiles and cetartiodactyls (Szenker-Ravi 2022; Guimier 2015).
   - **Alternative or additional branch:** MMP21 negatively regulates **Notch signalling**. *MMP21* knockdown raised CBF1-luciferase activity about 4.7-fold in HEK293 cells, and Notch targets (*her2*, *her6*, *her9*, *hey1*, *hes5*) were upregulated in morphants (PMID:26429889). How this relates to the *dand5* step has not been resolved.
5. **Left-sided Nodal cascade in the lateral plate mesoderm is lost or randomised.** In zebrafish, *spaw* is right-sided, bilateral or absent in 34% of morphants versus 5% of controls (PMID:26429889). *Pitx2* asymmetry is inferred to be affected (not measured in mouse in the papers read).
6. **Randomised organ laterality.** This produces randomised heart looping (zebrafish: 28–44% of morphants depending on dose; 63.5% in Qin 2022) and randomised visceral situis (mouse: 61% situs inversus or heterotaxy). It leads to:
   - 6a. **Complex CHD**: TGA, AVSD, pulmonary atresia or stenosis, single ventricle, anomalous systemic and pulmonary venous return. Present in 32 of 33 mouse mutant embryos.
   - 6b. **Visceral heterotaxy**: dextrocardia, atrial isomerism, asplenia or polysplenia, situs inversus.
   - 6c. **Situs inversus totalis**, which is clinically benign when concordant.
7. **Clinical outcomes** follow from 6a and 6b: neonatal haemodynamic failure, single-ventricle palliation, and infection risk from asplenia.

### Candidate GO and CL terms (verify)

- **GO:**
  - determination of left/right symmetry (GO:0007368)
  - heart looping (GO:0001947)
  - metalloendopeptidase activity (GO:0004222)
  - negative regulation of Notch signaling pathway (GO:0045746)
  - extracellular matrix disassembly (GO:0022617)
  - nodal signaling pathway (GO:0038092)
- **CL:** Find the CL term for the node / LRO pit cell. Crown cells are the cells that sense flow.

### Scale tags

| Step | `biological_scale` |
|---|---|
| Steps 1–2 | MOLECULAR |
| Steps 3–5 | CELLULAR / TISSUE |
| Steps 6–7 | ORGANISM |

### Omics and screens

None disease-specific. *MMP21* was recovered among 61 genes in the ENU forward-genetic CHD screen (Li 2015).

---

## 7. Anatomical structures affected

- **Primary site (embryonic):** the LRO.
  - UBERON candidates: "embryonic node" / "primitive node"; Kupffer's vesicle for zebrafish.
- **Organs:** heart (cardiac chambers, septa, outflow tract, great arteries), systemic and pulmonary veins, spleen, lungs (bronchial and lobar isomerism), liver, stomach, intestine.
- **Subcellular level:** extracellular space and secreted protein (GO:0005615). Under the preprint model, CIROP acts at the ciliary membrane.
- **Laterality:** Randomised; mirror-image or ambiguous arrangements.

---

## 8. Temporal development

- **Onset:** Embryonic, at L-R specification (about E7.5–8.5 in mouse). Clinically congenital, often detected prenatally by fetal echocardiography.
- **Course:** Not progressive. Outcomes depend on CHD complexity and staged surgery.
- **Critical window:** LRO function in early somitogenesis. There is no postnatal window to modify the developmental defect.

---

## 9. Inheritance and population

- **Inheritance:** Autosomal recessive (HP:0000007), with incomplete penetrance and variable expressivity. Consanguinity appears in the Perles family and some Guimier families.
- **Prevalence:**
  - No HTX7-specific figure. Heterotaxy overall occurs in roughly 1 in 10,000 births (figure from the A*STAR press material; cite a primary epidemiology source instead).
  - *MMP21* accounts for about 5.9% of non-syndromic heterotaxy in one cohort.
  - Approximate published case count: about 17 families by 2020 (Yuan Table 2). The 26 missense-carrying patients in Pasquetti 2025 overlap with these.
  - Suggested `prevalence_class: NOT_YET_DOCUMENTED` or `CASES_IN_LITERATURE`.
- **Populations:** European/French, Israeli (consanguineous), British (DDD), Han Chinese. No founder variant is established.
- **Sex ratio, anticipation, mosaicism, carrier frequency:** Not reported. No anticipation is expected.

---

## 10. Diagnostics

- **Imaging:** fetal and postnatal echocardiography; cardiac CT/MRI; abdominal ultrasound for spleen, liver and stomach position.
- **Spleen function:** blood smear for Howell-Jolly bodies, and splenic scintigraphy in suspected asplenia.
- **Genetic testing:** exome or heterotaxy/CHD panels that include *MMP21* alongside *ZIC3*, *NODAL*, *CFC1*, *PKD1L1*, *CIROP*, *DAND5* and *MMP21*'s other module partners. CNV analysis is needed to detect intragenic deletions such as the exon 1–3 deletion.
- **Differential diagnosis:** Primary ciliary dyskinesia must be excluded with nasal nitric oxide and ciliary studies. Normal ciliary function together with heterotaxy points towards *MMP21* or *CIROP*. Other differentials are *ZIC3* X-linked heterotaxy (HTX1), *PKD1L1*, *CIROP* and chromosomal causes.
- **Screening:** Prenatal diagnosis or PGT is possible once familial variants are known. No newborn screening.

---

## 11. Outcome and prognosis

- **Range:** from a normal lifespan (isolated situs inversus totalis) to neonatal death. One Guimier twin died on day 1 from haemodynamic failure.
- **Treated outcome:** the Yuan patient did well after a total cavopulmonary connection (Fontan).
- **Prognostic factors:** right atrial isomerism with asplenia, single-ventricle physiology, and TAPVR.
- **No *MMP21*-specific survival data exist.**

---

## 12. Treatment

All treatment is supportive or surgical. No gene-specific therapy exists, and no clinical trials were found.

| Intervention | NCIT candidate (verify) | `therapeutic_modality` |
|---|---|---|
| Cardiac surgery: biventricular repair, arterial switch, staged single-ventricle palliation (Glenn/Fontan) | NCIT:C15329 Surgical Procedure (look for a more specific cardiac-surgery term) | SURGERY |
| Antibiotic prophylaxis and vaccination (pneumococcal, Hib, meningococcal) for asplenia | NCIT:C15986 Pharmacotherapy with `therapeutic_agent`; NCIT:C15346 vaccination | SMALL_MOLECULE / VACCINE |
| Ladd procedure for symptomatic malrotation | NCIT:C15329 | SURGERY |
| Genetic counselling | NCIT:C15240 | — |

---

## 13. Prevention

- **Primary prevention:** genetic counselling, with a 25% recurrence risk for carrier couples.
- **Prenatal options:** prenatal diagnosis or PGT for known familial variants.
- **Secondary prevention:** fetal echocardiography in later pregnancies.
- **Tertiary prevention:** asplenia prophylaxis and Fontan surveillance.

---

## 14. Other species and natural disease

- No naturally occurring animal disease was found in OMIA.
- **Evolutionary note:** *MMP21* is absent or pseudogenised in birds, reptiles and cetartiodactyls (e.g. pig). This matches the absence of motile-cilia LROs in those lineages and the co-loss of *CIROP*, *PKD1L1* and *DAND5* (Guimier 2015; Szenker-Ravi 2022).
- **Ortholog NCBITaxon IDs:** mouse NCBITaxon:10090, zebrafish NCBITaxon:7955, *Xenopus laevis* NCBITaxon:8355 (verify).

---

## 15. Model organisms

| Model | Genotype | Phenotype | Fidelity / limitations | Source |
|---|---|---|---|---|
| Mouse, ENU "Miri" and "Koli" | *Mmp21* W177L and Y325N missense, homozygous (MGI:5311376, MGI:5554438) | Visceral heterotaxy and CHD (d-TGA, tricuspid atresia, VSD); **normal node cilia motility** | High fidelity for CHD plus heterotaxy | Akawi 2015 (PMID:26437029); Li 2015 Nature (PMID 25807483, unverified) |
| Mouse, CRISPR knock-in of human p.Ile226Thr | Mutation-positive E13.5 embryos | 32/33 had CHD including TGA; 20 (61%) had situs inversus or heterotaxy; 0/14 wild-type affected | `RECAPITULATES` | Guimier 2015 (PMID:26437028) |
| Zebrafish morphants and CRISPR F0/F1 | Splice- and translation-blocking morpholinos; Cas9 deletions | Heart-looping defects in 28–44% (dose-dependent) and 20–40% of F1 progeny; abnormal *spaw* in 34%; Notch targets upregulated; other cilia-dependent organs unaffected | Partial recapitulation (looping and LPM markers); morpholino specificity caveats | Perles 2015 (PMID:26429889); Guimier 2015; Qin 2022 (63.5% looping defects, used for variant rescue) |
| *Xenopus* F0 crispants | *mmp21* null | Heterotaxy; normal leftward flow; failed left-sided *dand5* repression; Mmp21 acts upstream of Cirop | Phenocopies human HTX; morphogen model not yet peer-review-settled | Ott et al. 2024/25 bioRxiv / eLife RP104430 |

---

## Key references

1. Perles Z et al. A human laterality disorder caused by a homozygous deleterious mutation in *MMP21*. *J Med Genet* 2015;52(12):840–847. **PMID:26429889** ([PMC4936483](https://pmc.ncbi.nlm.nih.gov/articles/PMC4936483))
   - Quotes: "We identified a homozygous 2 bp deletion in MMP21, encoding matrix metalloproteinase-21, as the sole coding mutation that segregated with the phenotype." / "Our data implicate loss of MMP21 as a cause of heterotaxy in humans with concomitant defects in Notch signaling."
2. Guimier A et al. MMP21 is mutated in human heterotaxy and is required for normal left-right asymmetry in vertebrates. *Nat Genet* 2015;47(11):1260–1263. **PMID:26437028** ([PMC5620017](https://pmc.ncbi.nlm.nih.gov/articles/PMC5620017); [Nature](https://www.nature.com/articles/ng.3376))
   - Quote: "Heterotaxy results from a failure to establish normal left-right asymmetry early in embryonic development."
3. Akawi N et al. Discovery of four recessive developmental disorders using probabilistic genotype and phenotype matching among 4,125 families. *Nat Genet* 2015;47:1363–1369. **PMID:26437029** ([PubMed](https://pubmed.ncbi.nlm.nih.gov/26437029/))
4. Li Y et al. Global genetic analysis in mice unveils central role for cilia in congenital heart disease. *Nature* 2015. PMID 25807483 (unverified).
5. Yuan ZZ et al. A Novel Nonsense *MMP21* Variant Causes Dextrocardia and Congenital Heart Disease in a Han Chinese Patient. *Front Cardiovasc Med* 2020;7:582350. doi:10.3389/fcvm.2020.582350. PMID 33240936 (third-party listing only) ([Frontiers](https://www.frontiersin.org/articles/10.3389/fcvm.2020.582350/full))
6. Qin XJ et al. De novo disruptive heterozygous *MMP21* variants are potential predisposing genetic risk factors in Chinese Han heterotaxy children. *Hum Genomics* 2022;16:41. **PMID:36123719** ([PMC9484203](https://pmc.ncbi.nlm.nih.gov/articles/PMC9484203))
7. Szenker-Ravi E et al. Discovery of a genetic module essential for assigning left-right asymmetry in humans and ancestral vertebrates. *Nat Genet* 2022;54:62–72. PMID 34903892 (unverified) ([HAL](https://www.hal.inserm.fr/inserm-03752860))
8. Pasquetti D et al. Expanding the Molecular Spectrum of *MMP21* Missense Variants: Clinical Insights and Literature Review. *Genes* 2025;16(1):62. doi:10.3390/genes16010062 ([PMC11764533](https://pmc.ncbi.nlm.nih.gov/articles/PMC11764533/))
9. Ott T et al. MMP21 behaves as a fluid flow transported morphogen to impart laterality during development. bioRxiv 2024 (doi:10.1101/2024.10.13.618030); eLife reviewed preprint RP104430 ([eLife](https://elifesciences.org/reviewed-preprints/104430)) — preprint; reviewers called the morphogen conclusion premature.
10. OMIM #616749 summary via [FindZebra](https://www.findzebra.com/details/jjK8pDK-heterotaxy-visceral-7-autosomal); [MalaCards HTX7](https://malacards.org/card/heterotaxy_visceral_7_autosomal); [LOVD #06071](https://databases.lovd.nl/shared/diseases/06071); [Victor Chang CHDgene: MMP21](https://chdgene.victorchang.edu.au/gene/118856)

---

## Gaps and curation leads

- **Per-patient phenotype tables:** the Guimier supplement and Pasquetti Table 1 were not read. Frequency estimates need them.
- **Akawi 2015 human phenotypes and alleles** need to be read from the full text.
- **Mouse molecular readouts:** no mouse Nodal/*Pitx2*/*Dand5* readouts were found in the sources read. The *dand5* step rests on *Xenopus* preprint data, so mark it `directness: INDIRECT` / model-organism, and consider a `HUMAN_MODEL_MISMATCH` or `KNOWLEDGE_GAP` discussion on the morphogen hypothesis.
- **Notch and the *dand5* flow response:** how these two mechanisms relate is unresolved and is a natural `KNOWLEDGE_GAP`.
- **Existing module:** check `just list-modules` for a left-right patterning / heterotaxy module before writing the cascade nodes from scratch.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 14 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 37 |
| Resolved | 34 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 27 |
| Terms named correctly | 11 |
| Terms named as a **different** term | 12 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014762` (2 mentions) - the report calls it "MONDO"; MONDO calls it **heterotaxy, visceral, 7, autosomal**
- `HP:0011536` (1 mention) - the report calls it "verify the label"; HP calls it **Right atrial isomerism**
- `HP:0006695` (1 mention) - the report calls it "verify"; HP calls it **Atrioventricular canal defect**
- `HP:0001669` (1 mention) - the report calls it "verify"; HP calls it **Transposition of the great arteries**
- `HP:0004935` (1 mention) - the report calls it "verify"; HP calls it **Pulmonary artery atresia**
- `HP:0001642` (1 mention) - the report calls it "verify"; HP calls it **Pulmonic stenosis**
- `HP:0001750` (1 mention) - the report calls it "verify"; HP calls it **Single ventricle**
- `HP:0005160` (1 mention) - the report calls it "verify"; HP calls it **Total anomalous pulmonary venous return**
- `HP:0005301` (1 mention) - the report calls it "verify"; HP calls it **Persistent left superior vena cava**
- `HP:0012020` (1 mention) - the report calls it "verify"; HP calls it **Right aortic arch**
- `NCIT:C15329` (2 mentions) - the report calls it "Ladd procedure for symptomatic malrotation"; NCIT calls it **Surgical Procedure**
- `NCBITaxon:8355` (1 mention) - the report calls it "verify"; NCBITaxon calls it **Xenopus laevis**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005615` (obsolete extracellular space) (1 mention) - replaced by `GO:0005576`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001651` (1 mention) - the report calls it "Dextrocardia, including mirror-image"; HP calls it **Dextrocardia**
- `HP:0001263` (1 mention) - the report calls it "Global developmental delay, dysmorphism"; HP calls it **Global developmental delay**
- `GO:0005615` (1 mention) - the report calls it "Subcellular level:** extracellular space and secreted protein"; GO calls it **obsolete extracellular space**
- `NCIT:C15240` (1 mention) - the report calls it "Genetic counselling"; NCIT calls it **Genetic Counseling**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`.