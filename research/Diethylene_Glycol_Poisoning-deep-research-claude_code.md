---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-19T13:42:51.021370'
end_time: '2026-09-19T13:48:26.864089'
duration_seconds: 335.84
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Diethylene Glycol Poisoning
  mondo_id: ''
  category: Environmental
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
  web_search_requests: 20
  num_turns: 19
  total_cost_usd: 1.5437734
  session_id: dc83c613-1fba-53b8-9741-f63fb2448a6e
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 62
reference_validation:
  total_references: 31
  verified: 31
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 31
  on_topic: 18
  off_topic: 1
  off_topic_references:
  - PMC:PMC11841886
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 59
  verified: 57
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 28
  labels_matching: 17
  labels_mismatched: 7
  mislabelled_terms:
  - term_id: CHEBI:46807
    reported_labels:
    - parent compound
    - diethylene glycol
    ontology_label: diethylene glycol
  - term_id: HP:0012647
    reported_labels:
    - Autonomic dysfunction
    ontology_label: Abnormal inflammatory response
  - term_id: CL:0000182
    reported_labels:
    - site of ADH/ALDH-mediated bioactivation and secondary hepatotoxicity
    ontology_label: hepatocyte
  - term_id: CL:0002064
    reported_labels:
    - site of DEG-associated pancreatitis
    ontology_label: pancreatic acinar cell
  - term_id: NCIT:C1421
    reported_labels:
    - Fomepizole
    ontology_label: Oxygen Radical
  - term_id: NCIT:C15571
    reported_labels:
    - Hemodialysis
    ontology_label: Differentiation Therapy
  - term_id: NCIT:C15329
    reported_labels:
    - "Surgical/Interventional Procedure category is not correct \u2014 hemodialysis\
      \ maps under NCIT renal replacement therapy terms"
    ontology_label: Surgical Procedure
  labels_variant: 4
  obsolete_terms:
  - term_id: GO:0070265
    ontology_label: obsolete necrotic cell death
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Diethylene Glycol Poisoning
- **MONDO ID:**  (if available)
- **Category:** Environmental

## Research Objectives

Please provide a comprehensive research report on **Diethylene Glycol Poisoning** covering all of the
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

I'll research diethylene glycol (DEG) poisoning across multiple angles now.

# Diethylene Glycol Poisoning: Comprehensive Research Report

## 1. Disease Information

**Overview.** Diethylene glycol (DEG) poisoning is an acute (and, in survivors, subacute-to-chronic) toxic syndrome caused by ingestion of diethylene glycol — an industrial solvent, humectant, and antifreeze/brake-fluid component chemically similar to, but distinct from, ethylene glycol. DEG is not itself intended for human consumption; poisoning occurs almost exclusively through unintentional exposure (most catastrophically, as an adulterant substituting for pharmaceutical-grade glycerin or propylene glycol in liquid medicines) or, less commonly, deliberate ingestion. The clinical syndrome evolves through a predictable sequence: an early gastrointestinal/inebriation phase, a renal failure phase (acute tubular necrosis), and — in survivors, roughly 1–3 weeks later — a delayed neurologic phase with cranial and peripheral neuropathies and encephalopathy ([Saudi J Kidney Dis Transplant, 2016](https://journals.lww.com/sjkd/fulltext/2016/27060/diethylene_glycol_poisoning_induced_acute_kidney.28.aspx); [emDocs ToxCard](https://www.emdocs.net/toxcard-diethylene-glycol/)).

**Chemical identity.**
- IUPAC name: 2,2′-oxydiethanol; CAS 111-46-6
- ChEBI: **CHEBI:46807** (diethylene glycol); classified as a hydroxyether/diol ([ZFIN CHEBI:46807](https://zfin.org/CHEBI:46807))
- PubChem CID: 8117; KEGG: C14689
- Formula: C4H10O3, MW 106.12 g/mol

**Key identifiers for the disease entity:**
- No dedicated OMIM entry exists (DEG poisoning is an acquired toxic/environmental disease, not Mendelian).
- Orphanet lists the closely related entity "Ethylene glycol poisoning" (ORPHA:31826) but has no distinct DEG entry ([Orphanet](https://www.orpha.net/en/disease/detail/31826)); DEG poisoning is generally grouped under toxic-alcohol/glycol poisoning nosology alongside ethylene glycol.
- ICD-10-CM: T52.8X1– (Toxic effect of other organic solvents, accidental) is used in practice for DEG, since DEG has no dedicated subcode distinct from the ethylene-glycol code T51.8 family; MeSH: "Ethylene Glycols" (DEG is indexed as a related glycol; no separate MeSH heading exists for DEG poisoning specifically).
- MONDO ID: not established as a distinct MONDO term at the time of this report; DEG poisoning would most naturally be curated as a toxic/environmental poisoning entity analogous to the existing ethylene glycol poisoning framework.

**Synonyms/alternative names:** DEG; diglycol; 2,2′-dihydroxydiethyl ether; bis(2-hydroxyethyl) ether; digol; 3-oxa-1,5-pentanediol; "DEG poisoning"; in the epidemiologic literature also referred to under the umbrella terms "diethylene glycol mass poisoning," "toxic syrup poisoning," and (colloquially in the 2022–2025 outbreaks) "contaminated cough syrup deaths."

**Data provenance.** Nearly all clinical knowledge of human DEG poisoning derives from **aggregated outbreak/disease-level resources** — case series and outbreak investigations published by health ministries, WHO, and the US CDC (MMWR) — rather than individual longitudinal EHR cohorts, because poisoning events are epidemic, geographically clustered in low- and middle-income countries, and typically investigated retrospectively. The single largest evidence base comes from outbreak investigations in Haiti (1995–96), Bangladesh/Nigeria (1990), Panama (2006), and The Gambia/Indonesia/Uzbekistan (2022) and the 2025 India (Madhya Pradesh) cluster ([CDC MMWR Haiti](https://www.cdc.gov/mmwr/pdf/wk/mm4530.pdf); [MMWR Gambia 2023](https://www.cdc.gov/mmwr/volumes/72/wr/mm7209a1.htm)). Mechanistic detail is drawn from rodent studies and in vitro human proximal-tubule-cell experiments.

---

## 2. Etiology

### Disease causal factor
DEG poisoning is **exclusively an environmental/toxic exposure disease** — there is no genetic or infectious cause. The causal agent is oral (occasionally intravenous, in adulterated injectable products) ingestion of diethylene glycol, either as the pure industrial chemical or, far more commonly at the population level, as an unlabeled contaminant of pharmaceutical excipients (glycerin, propylene glycol, sorbitol solution, or polyethylene glycol) or, in some cases, of unregulated recreational/counterfeit alcohol products ([Clin Toxicol PMC4616334](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4616334/)).

### Risk factors

**Environmental/exposure risk factors (dominant):**
- Consumption of DEG/ethylene-glycol–contaminated liquid pharmaceuticals — the mechanism behind every major epidemic (Haiti 1995–96, Bangladesh/Nigeria 1990, Panama 2006, India-manufactured syrups exported to The Gambia/Indonesia/Uzbekistan 2022, and the Coldrif/Sresan Pharmaceuticals cluster in Madhya Pradesh, India, 2025) ([2025 India cough syrup crisis, Wikipedia](https://en.wikipedia.org/wiki/2025_India_cough_syrup_crisis); [CNN, Oct 2025](https://www.cnn.com/2025/10/14/world/who-warning-contaminated-cough-syrup-india-deaths-intl-hnk)).
- Occupational/industrial exposure to DEG-containing solvents, antifreeze, and brake fluid.
- Ingestion of counterfeit/adulterated alcoholic beverages.
- Recreational or self-harm ingestion of DEG-containing consumer products (correctional-facility case clusters have been reported: [Clin Toxicol PMC4616334](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4616334/)).
- **Age (young children)**: the overwhelming majority of deaths in every mass-poisoning event have been in children under 5, likely reflecting both higher exposure per kg body weight from syrup dosing and possibly greater physiologic vulnerability.
- Concentration/dose of contaminant: the 2025 Coldrif product reportedly contained DEG at levels "hundreds of times above" the pharmacopeial limit of 0.1% (up to ~45% DEG reported) ([CPSP](https://centrepsp.org/media/blog/poison-in-a-bottle-how-a-contaminated-cough-syrup-in-madhya-pradesh-killed-children-and-why-the-world-should-be-outraged/)).
- Number of contaminated medicines ingested — in The Gambia outbreak, exposure to a **single** contaminated medicine (rather than ≥2) was associated with markedly *higher* AKI risk (aOR = 4.21 for ≥2 vs 1 medicine, direction as reported), a counterintuitive dose-related finding under investigation ([PLOS Global Public Health, case-case-control analysis](https://journals.plos.org/globalpublichealth/article?id=10.1371%2Fjournal.pgph.0005512)).

**Genetic risk/susceptibility factors:** No confirmed human genetic risk variant has been established. However, mechanistic and rodent data strongly implicate variability in expression/activity of:
- **Alcohol dehydrogenase (ADH) / aldehyde dehydrogenase (ALDH)** — the enzymes that bioactivate DEG into its toxic metabolites; individuals or populations with higher ADH/ALDH activity would be predicted to generate more toxic metabolite, analogous to established ADH1B/ALDH2 polymorphism effects on ethanol/methanol/ethylene-glycol metabolism (inferred by analogy; not yet directly demonstrated for DEG in humans).
- **NaDC-1 (SLC13A2)**, the renal proximal-tubule sodium-dicarboxylate transporter responsible for diglycolic acid (DGA) uptake: a 2023 rat study found that only ~60% of rats developed AKI after identical DEG/DGA dosing, and that AKI occurrence correlated with **1.6–2-fold higher renal NaDC-1 mRNA expression**, proposing that inter-individual variability in this transporter may explain the variable human sensitivity documented across historical outbreaks ([PMC10263375](https://pmc.ncbi.nlm.nih.gov/articles/PMC10263375/)).

### Protective factors
- **Older age**: each additional year of age reduced AKI risk in exposed children (adjusted OR = 0.58 per year) in the Gambia case-case-control analysis ([PLOS GPH](https://journals.plos.org/globalpublichealth/article?id=10.1371%2Fjournal.pgph.0005512)).
- **Multivitamin supplementation**: associated with markedly reduced AKI risk (aOR = 0.24) in the same analysis — the leading environmental/nutritional protective factor identified to date, though the biological mechanism (general nutritional status vs. a specific micronutrient effect on ADH/ALDH activity or renal transporter expression) is not established.
- **Genetic/pharmacologic protective factor (mechanistic, not epidemiologic)**: inhibition of ADH — pharmacologically achieved with fomepizole or ethanol — prevents bioactivation of DEG to its toxic metabolites and is the basis of antidotal therapy; a rat study demonstrated that inhibiting DEG metabolism (via ADH blockade) prevents target-organ toxicity entirely, confirming that the parent compound itself is not the proximate toxicant ([Toxicol Sci 117:25, PMID:20530232](https://pubmed.ncbi.nlm.nih.gov/20530232/)).
- Low NaDC-1 transporter expression (inferred protective factor from the rat model above).

### Gene–environment interactions
The clearest documented gene(enzyme)–environment interaction is pharmacologic: **ADH/ALDH activity level determines how much toxic metabolite is generated from a given DEG dose**, and **NaDC-1 transporter expression level determines how much of the toxic metabolite (DGA) accumulates in target renal tubule cells** once formed. Both interactions have been demonstrated in animal/in vitro systems and are the rationale for antidotal ADH blockade in humans; direct human genotype-outcome data (e.g., linking ADH1B or SLC13A2 variants to clinical severity) have not yet been published from the outbreak cohorts.

---

## 3. Phenotypes

DEG poisoning phenotypes cluster into three temporally distinct clinical phases ([Saudi J Kidney Dis Transplant 2016](https://journals.lww.com/sjkd/fulltext/2016/27060/diethylene_glycol_poisoning_induced_acute_kidney.28.aspx); [Int Urol Nephrol 2023, PMID:37186212](https://pubmed.ncbi.nlm.nih.gov/37186212/)):

### Phase 1 (hours, gastrointestinal/inebriation) — onset within hours of ingestion
| Phenotype | Suggested HP term |
|---|---|
| Nausea | HP:0002018 |
| Vomiting | HP:0002013 |
| Abdominal pain | HP:0002027 |
| Diarrhea | HP:0002014 |
| Inebriation/CNS depression | HP:0007270 (Cerebral palsy - not exact); more precisely "Lethargy" HP:0001254 or "Ataxia" HP:0001251 depending on presentation |
| Metabolic acidosis (high or normal anion gap) | HP:0001942 |

### Phase 2 (1–3 days post-exposure, renal/systemic) — hallmark: acute renal failure
| Phenotype | Suggested HP term | Notes |
|---|---|---|
| Acute kidney injury / acute tubular necrosis | HP:0001919 (Acute kidney injury) | Biopsy hallmark: proximal tubular necrosis with epithelial vacuolization/edema |
| Oliguria progressing to anuria | HP:0100519 (Oliguria) / HP:0100518 (Anuria) | Obstructive vacuolization reduces urine flow |
| Refractory metabolic acidosis | HP:0001942 | |
| Hyperkalemia | HP:0002153 | |
| Hypertension | HP:0000822 | |
| Cardiac dysrhythmia / tachycardia | HP:0001662 / HP:0001649 | |
| Pulmonary edema | HP:0100598 | |
| Acute pancreatitis | HP:0001733 | |
| Hepatitis/elevated transaminases | HP:0002240 (Hepatomegaly) / HP:0002910 (Elevated hepatic transaminase) | |
| Fever | HP:0001945 | Especially in pediatric AKI outbreaks (The Gambia) |

### Phase 3 (5–20 days post-exposure, delayed neurologic) — occurs mainly in survivors of AKI
| Phenotype | Suggested HP term | Frequency (from case series) |
|---|---|---|
| Encephalopathy | HP:0001298 | Present in severe delayed cases; can progress to cerebral edema and death |
| Facial nerve palsy/diplegia (classic finding) | HP:0010628 (Facial palsy) | 68% in one case series of neurologic survivors ([PMC4616334](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4616334/)) |
| Multiple cranial neuropathies / bulbar palsy | HP:0007311 or HP:0002015 (Bulbar palsy) | Described as "classic" in delayed syndrome |
| Limb weakness (flaccid paralysis) | HP:0003324 (Generalized muscle weakness) / HP:0002078 (Motor delay - not exact) | 77% limb weakness among neurologic cases |
| Sensorimotor peripheral neuropathy | HP:0007141 | Demonstrated in 90% of those tested by nerve conduction studies |
| Areflexia | HP:0001284 | |
| CSF albuminocytologic dissociation (Guillain-Barré–like) | — (laboratory finding, no direct HP phenotype term; closest: HP:0025314 CSF protein elevation) | |
| Optic neuritis | HP:0100653 | Reported in a subset |
| Seizures | HP:0001250 | Reported in severe cases |
| Coma | HP:0001259 | In fatal/near-fatal cases |
| Autonomic dysfunction (delayed) | HP:0012647 (Autonomic dysfunction) | Case reports of delayed autonomic neuropathy |

**Age of onset:** Phase 1 begins within hours; Phase 2 (renal) at 1–3 days; Phase 3 (neurologic) at 5–20 days ("delayed" progressive neurologic syndrome), with some series describing onset in the second week post-ingestion.

**Severity/progression:** Highly dose-dependent and variable between individuals (see NaDC-1 discussion above). In the 2022 Gambia outbreak, AKI carried ~80% case-fatality among affected children, while ~30% of documented DEG-exposed children did **not** develop AKI at all ([MMWR](https://www.cdc.gov/mmwr/volumes/72/wr/mm7209a1.htm); [PMC9997663](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9997663/)). Among survivors of renal failure who develop the delayed neurologic syndrome, motor signs may improve over 4–6 months but dialysis-dependence can persist ([Clin Toxicol PMC4616334](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4616334/)). A 2026 latent-class analysis of the Gambia outbreak formally stratified clinical phenotype severity classes ([Pediatric Nephrology, in press](https://link.springer.com/article/10.1007/s00467-026-07148-2)).

**Quality of life impact:** Survivors with residual chronic kidney disease and/or peripheral neuropathy face long-term disability; specific EQ-5D/SF-36 data for DEG poisoning survivors were not identified in the literature — this is a recognized gap, most outbreak follow-up has focused on mortality and short-term renal recovery rather than standardized QoL instruments.

---

## 4. Genetic/Molecular Information

DEG poisoning is **not a genetic disease** — there are no causal genes, pathogenic variants, or chromosomal abnormalities to report in the classic Mendelian sense. The "genetic/molecular" content relevant here concerns the enzymes and transporters governing individual susceptibility:

- **ADH (alcohol dehydrogenase)** — HGNC gene family ADH1A/ADH1B/ADH1C etc. — catalyzes the first bioactivation step (DEG → 2-hydroxyethoxyacetaldehyde). No DEG-specific human polymorphism data published; extrapolated from the general toxic-alcohol metabolism literature.
- **ALDH (aldehyde dehydrogenase)**, e.g., ALDH2 — catalyzes the second step (aldehyde → 2-hydroxyethoxyacetic acid, 2-HEAA). Same caveat as above.
- **SLC13A2 (NaDC-1)** — sodium-dicarboxylate cotransporter on the renal proximal tubule apical membrane; mediates cellular uptake of diglycolic acid (DGA), the nephrotoxic metabolite, via molecular mimicry of the Krebs-cycle intermediate succinate. Rat data show renal NaDC-1 mRNA expression correlates with AKI susceptibility ([PMC10263375](https://pmc.ncbi.nlm.nih.gov/articles/PMC10263375/); [Toxicol Sci 190:1, PMID:36087010](https://pubmed.ncbi.nlm.nih.gov/36087010/)).
- **OAT1/OAT3 (SLC22A6/SLC22A8)** — basolateral organic anion transporters. Contrary to initial hypotheses, a 2023 study found OAT1/OAT3 stimulation does **not** promote efflux of DGA from proximal tubule cells — DGA accumulates intracellularly regardless, ruling out OAT-targeted efflux as a therapeutic strategy ([PMID:36958672](https://pubmed.ncbi.nlm.nih.gov/36958672/)).

**Functional consequence:** the pathway is a **toxic gain of a novel metabolite-mediated cytotoxic function** rather than a loss-of-function/gain-of-function genetic mechanism — DGA depletes cellular ATP and chelates calcium, producing mitochondrial dysfunction and necrosis ([Clin Toxicol 54:6, PMID:27002734](https://pubmed.ncbi.nlm.nih.gov/27002734/)).

**Epigenetics, somatic variants, chromosomal abnormalities:** Not applicable/not reported — no epigenetic or chromosomal mechanism has been described for this acquired toxic disease.

---

## 5. Environmental Information

### Environmental (chemical/toxin) factors — the primary etiologic category
- **Pharmaceutical adulteration** is the dominant environmental cause at the population level: DEG or ethylene glycol substituted (deliberately, by fraud, or accidentally through mislabeled industrial-grade chemical supply chains) for pharmaceutical glycerin, propylene glycol, sorbitol solution, or PEG excipients in liquid medicines (cough syrups, acetaminophen elixirs) ([CDC/PMC10081810](https://pmc.ncbi.nlm.nih.gov/articles/PMC10081810/); [WHO news](https://www.who.int/news/item/23-01-2023-who-urges-action-to-protect-children-from-contaminated-medicines)).
- **Industrial/occupational exposure**: DEG is a widely used solvent in antifreeze, brake fluid, printing inks, plasticizers, and as a humectant.
- **Counterfeit alcohol**: DEG has been used to adulterate bootleg spirits in several countries.
- **Consumer product ingestion** (accidental pediatric exposure to household antifreeze-type products, and recreational ingestion in adults, including reported correctional-facility clusters).

### Lifestyle factors
Not directly disease-modifying in the classic sense (e.g., diet/exercise), though nutritional status (multivitamin use) modified outcome risk in the Gambia cohort (see Section 2).

### Infectious agents
Not applicable — DEG poisoning is a pure chemical toxicity, not an infectious disease. (Note: differential diagnosis in pediatric outbreaks initially considered infectious causes of AKI before the toxic etiology was confirmed.)

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Ingestion of diethylene glycol** (via contaminated pharmaceutical excipient, industrial solvent, or counterfeit alcohol) → rapid, near-complete gastrointestinal absorption (rat data: absorption rate constants 2.95–4.24 h⁻¹) and distribution to tissues in order kidney > brain > spleen > liver > muscle > fat, tracking blood flow ([toxicokinetics study, PMID:8135655](https://pubmed.ncbi.nlm.nih.gov/8135655/)) → **leads to** systemic exposure of the liver and kidney to unmetabolized DEG.
2. **Hepatic oxidation by alcohol dehydrogenase (ADH)** converts DEG to **2-hydroxyethoxyacetaldehyde** → **leads to** generation of a reactive aldehyde intermediate ([Toxicol Sci 117:25](https://academic.oup.com/toxsci/article/117/1/25/1680549)).
3. **Oxidation by aldehyde dehydrogenase (ALDH)** converts the aldehyde to **2-hydroxyethoxyacetic acid (2-HEAA)** → **results in** the first major circulating toxic metabolite, which is renally eliminated and itself contributes to neurotoxicity and, per some models, general systemic toxicity.
4. **Further/alternate oxidation generates diglycolic acid (DGA)**, structurally analogous to the Krebs-cycle dicarboxylate succinate → **leads to** DGA being a substrate for the sodium-dicarboxylate cotransporter **NaDC-1 (SLC13A2)** on the apical membrane of renal proximal tubule cells, driving preferential renal accumulation ([PMC10263375](https://pmc.ncbi.nlm.nih.gov/articles/PMC10263375/); mechanistic uptake study [PMID:36087010](https://pubmed.ncbi.nlm.nih.gov/36087010/)).
5. **Intracellular DGA is poorly effluxed** (OAT1/OAT3 stimulation does not rescue efflux) → **results in** progressive intracellular DGA accumulation in proximal tubule cells ([PMID:36958672](https://pubmed.ncbi.nlm.nih.gov/36958672/)).
6. **Accumulated DGA chelates calcium and produces mitochondrial dysfunction**, with severe depletion of cellular ATP → **leads to** proximal tubule cell necrosis (this step is directly demonstrated in vitro in human proximal tubule cells: [Toxicol Sci 124:35, PMID:21856646](https://pubmed.ncbi.nlm.nih.gov/21856646/); [Clin Toxicol 54:6, PMID:27002734](https://pubmed.ncbi.nlm.nih.gov/27002734/)).
7. **Tubular epithelial necrosis, vacuolization, and edema obstruct the tubular lumen** → **results in** reduced urine flow, progressing to oliguria/anuria (**acute tubular necrosis**) → **causes** acute kidney injury, uremia, and the systemic Phase 2 clinical syndrome (metabolic acidosis, hyperkalemia, pulmonary edema).
8. **Concurrently**, hepatocyte and pancreatic acinar cell exposure to circulating metabolites (mechanism less well defined than the renal pathway) → **contributes to** hepatitis (transaminase elevation) and pancreatitis observed in Phase 2.
9. **In patients who survive the acute renal insult, and particularly those with more severe renal impairment**, a delayed process — hypothesized to involve either persistent low-level metabolite exposure, immune-mediated peripheral nerve injury (supported by CSF albuminocytologic dissociation resembling Guillain-Barré syndrome), or direct neurotoxicity of 2-HEAA/DGA on peripheral and cranial nerve myelin/axons — **leads to**, 5–20 days post-ingestion, a **delayed progressive neurologic syndrome**: encephalopathy plus multiple cranial neuropathies (classically bilateral facial palsy) and sensorimotor peripheral neuropathy ([Neurology, PMID:15824363](https://pubmed.ncbi.nlm.nih.gov/15824363/); [Clin Toxicol, PMID:15902788](https://pubmed.ncbi.nlm.nih.gov/15902788/)).
10. **Established renal impairment predicts subsequent delayed neurotoxicity**, suggesting the renal and neurologic injury pathways are linked (possibly via reduced clearance of neurotoxic metabolites in AKI, prolonging systemic exposure) ([PMC4616334](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4616334/)).
11. **Severe cases** progress to cerebral edema and death, typically from a combination of refractory metabolic derangement, cardiovascular collapse, and/or progressive encephalopathy.

**Key branch point:** it is the *metabolites* (2-HEAA and DGA), not DEG itself, that drive target-organ toxicity — demonstrated by the fact that pharmacological ADH inhibition (fomepizole/ethanol) blocks metabolite formation and **prevents** target-organ toxicity entirely in rat models ([PMID:20530232](https://pubmed.ncbi.nlm.nih.gov/20530232/)). This is the central mechanistic rationale for antidotal therapy in humans.

### Molecular pathways / cellular processes
- ADH/ALDH-mediated oxidative metabolism (xenobiotic biotransformation pathway).
- Sodium-dicarboxylate cotransport (NaDC-1/SLC13A2) — physiologically a succinate/dicarboxylate reabsorption pathway hijacked by the structurally mimetic toxin DGA.
- Mitochondrial dysfunction / ATP depletion — GO:0001836 (release of cytochrome c from mitochondria) and related apoptosis/necrosis pathways are plausible GO annotations; the literature specifically emphasizes **necrosis** (not classic apoptosis) as the dominant proximal tubule cell death mode (GO:0070265, necrotic cell death).
- Calcium chelation by DGA, disrupting calcium-dependent mitochondrial and cellular signaling.

### Cell types and tissue involvement (suggested CL/UBERON terms)
- **Renal proximal tubule epithelial cell** — CL:1001016 (kidney proximal convoluted tubule epithelial cell) — primary target, site of NaDC-1-mediated DGA uptake and necrosis.
- **Hepatocyte** — CL:0000182 — site of ADH/ALDH-mediated bioactivation and secondary hepatotoxicity.
- **Peripheral/cranial motor and sensory neurons** — CL:0000540 (neuron), with axonal/myelin involvement — site of delayed neurotoxicity (facial nerve, other cranial nerves, peripheral nerves).
- **Pancreatic acinar cell** — CL:0002064 — site of DEG-associated pancreatitis.
- Anatomical sites (UBERON): kidney (UBERON:0002113), renal proximal tubule (UBERON:0004134 or similar), liver (UBERON:0002107), pancreas (UBERON:0001264), facial nerve (UBERON:0001654), peripheral nervous system (UBERON:0000010), brain/cerebral cortex for encephalopathy (UBERON:0000955).

### Biochemical abnormalities
- Increased anion-gap metabolic acidosis (accumulation of 2-HEAA and DGA as unmeasured anions).
- Osmolar gap may be minimally elevated or normal — DEG's larger molecular weight compared to methanol/ethylene glycol makes the osmolar gap a **less sensitive** diagnostic marker than for other toxic alcohols ([EMCrit IBCC](https://emcrit.org/ibcc/alcohols/); [PMC7785502](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7785502/)).
- Hyperkalemia, elevated BUN/creatinine, elevated hepatic transaminases, lipase/amylase elevation in pancreatitis.

### Chemical entities (CHEBI)
- Diethylene glycol — CHEBI:46807 (parent compound)
- 2-hydroxyethoxyacetaldehyde — intermediate metabolite (no widely indexed CHEBI ID identified in this search)
- 2-hydroxyethoxyacetic acid (2-HEAA) — toxic metabolite
- Diglycolic acid (DGA) — the principal nephrotoxic metabolite

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary target: kidney** — proximal tubules specifically, producing acute tubular necrosis and AKI.
- **Secondary: liver** (hepatitis, transaminase elevation), **pancreas** (acute pancreatitis), **peripheral and cranial nervous system** (delayed neuropathy/palsies), **central nervous system** (encephalopathy, seizures, coma, cerebral edema), **cardiovascular system** (dysrhythmias, hypotension/hypertension), **respiratory system** (pulmonary edema).
- Body systems: renal, hepatobiliary, gastrointestinal (pancreas), nervous (both central and peripheral), cardiovascular, respiratory.

**Tissue/cell level:**
- Renal proximal tubule epithelium (specific target of DGA-mediated necrosis).
- Hepatocytes.
- Peripheral nerve axons/Schwann cells (myelin), cranial nerve motor fibers (especially facial nerve — bilateral facial diplegia is the classic finding).
- Pancreatic acinar tissue.

**Subcellular level:**
- Mitochondria (ATP depletion, calcium dysregulation — GO Cellular Component: GO:0005739 mitochondrion).
- Renal apical/basolateral membrane transporters (NaDC-1, OAT1/OAT3) — GO:0005886 plasma membrane.

**Localization/lateralization:**
- Renal injury is typically bilateral/diffuse (both kidneys).
- Cranial neuropathy is characteristically **bilateral** (bilateral facial palsy is described as the "classic" finding in delayed DEG neurotoxicity), distinguishing it from many other causes of facial palsy which are typically unilateral.

---

## 8. Temporal Development

**Onset:** Acute, occurring in previously healthy individuals following a discrete toxic ingestion event; no congenital or age-restricted susceptibility beyond the empirical predominance of severe outcomes in young children in outbreak settings.

**Onset pattern and staging (well-defined three-phase natural history):**
1. **Phase 1 (hours):** Acute GI/inebriation phase.
2. **Phase 2 (1–3 days):** Renal failure phase — hallmark of the disease; may include cardiac, pulmonary, hepatic, and pancreatic involvement.
3. **Phase 3 (5–20 days, up to ~2 weeks classically):** Delayed neurologic phase in survivors.

**Progression rate:** Can be rapid and fulminant (death within days in severe pediatric cases) or, in survivors of the renal phase, slowly evolving over weeks (neurologic phase) with further slow partial recovery over 4–6 months.

**Disease course pattern:** Monophasic in fatal cases; in survivors, a triphasic pattern (acute–renal–delayed neurologic) with potential for chronic sequelae (dialysis-dependence, residual neuropathy).

**Duration:** Acute poisoning is self-limited in mild cases with supportive care; severe cases can result in chronic kidney disease requiring long-term dialysis and persistent neurologic deficits.

**Remission patterns:** Neurologic signs in survivors have been reported to improve over 4–6 months, though renal dialysis-dependence may persist beyond that window ([PMC4616334](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4616334/)).

**Critical intervention window:** Early presentation (within ~12 hours) may precede the development of overt metabolic acidosis, meaning early cases can be missed on initial labs — antidotal treatment initiated before extensive metabolite generation (i.e., before ADH has converted much of the ingested DEG) is mechanistically the most effective window, paralleling the treatment logic for ethylene glycol/methanol.

---

## 9. Inheritance and Population

**Not a genetic disease** — there is no inheritance pattern, penetrance, expressivity, anticipation, mosaicism, or carrier frequency to report; this is an acquired environmental/toxic disease.

**Epidemiology (prevalence/incidence):** DEG poisoning has no baseline "prevalence" in the sense of an endemic disease; it occurs in discrete, source-attributable outbreaks. Documented major outbreaks and their scale:

| Outbreak | Year | Location | Deaths (approx.) | Source | Citation |
|---|---|---|---|---|---|
| Sulfanilamide elixir | 1937 | USA | >100 | Sulfanilamide elixir vehicle | (historical; foundational to US drug regulation) |
| Paracetamol syrup | 1990 | Nigeria (Jos) | 47 children | Contaminated glycerin | [PMID:1280035](https://pubmed.ncbi.nlm.nih.gov/1280035/) |
| Acetaminophen elixir | 1990 | Bangladesh | dozens | DEG-contaminated syrup | [ScienceDirect overview](https://www.sciencedirect.com/topics/medicine-and-dentistry/diethylene-glycol) |
| Acetaminophen syrup | 1995–96 | Haiti | ≥76 children (most confirmed deaths; near-total mortality in Haiti-based cases) | DEG-contaminated glycerin | [PMID:8769471](https://pubmed.ncbi.nlm.nih.gov/8769471/); [CDC MMWR](https://www.cdc.gov/mmwr/pdf/wk/mm4530.pdf) |
| Cough syrup | 2006 | Panama | 219 | DEG mislabeled as glycerin from Chinese manufacturer via European trader | [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0196064413016557) |
| Nigeria (paracetamol) | 2008–2009 | Nigeria | dozens (fatal poisoning cluster) | Contaminated acetaminophen | [PMID:20010509](https://pubmed.ncbi.nlm.nih.gov/20010509/) |
| Pediatric cough/cold syrups | 2022 | The Gambia | 66 deaths of 82 AKI cases (80% case-fatality among AKI cases) | Maiden Pharmaceuticals (India) exported syrups | [MMWR/CDC](https://www.cdc.gov/mmwr/volumes/72/wr/mm7209a1.htm) |
| Cough syrup | 2022 | Indonesia | >200 children | DEG/EG-contaminated syrup | [Chemistry World](https://www.chemistryworld.com/news/contaminated-cough-syrups-death-toll-passes-300-in-four-months/4016993.article) |
| Cough syrup | 2023 | Uzbekistan | 19 children | DEG/EG-contaminated syrup | [WHO](https://www.who.int/news/item/23-01-2023-who-urges-action-to-protect-children-from-contaminated-medicines) |
| Coldrif and related syrups | 2025 | India (Madhya Pradesh/Rajasthan) | ≥24 children (19 in Madhya Pradesh alone) | Sresan Pharmaceuticals; DEG up to ~45% of product | [CNN](https://www.cnn.com/2025/10/14/world/who-warning-contaminated-cough-syrup-india-deaths-intl-hnk); [Wikipedia](https://en.wikipedia.org/wiki/2025_India_cough_syrup_crisis) |

Cumulatively, WHO issued six global Medical Product Alerts between October 2022 and 2023 for DEG/EG-contaminated OTC medicines, with over 300 pediatric deaths across the Gambia, Indonesia, and Uzbekistan outbreaks alone ([WHO](https://www.who.int/news/item/23-01-2023-who-urges-action-to-protect-children-from-contaminated-medicines)).

**Population demographics:**
- **Age**: Overwhelmingly young children (median age 19 months in the Gambia outbreak, range 5 months–7 years) in the pharmaceutical-contamination outbreaks; adult cases occur predominantly via occupational, recreational, or self-harm ingestion.
- **Sex ratio**: No strong sex predilection has been reported specifically for DEG poisoning; exposure follows medication administration patterns rather than biological sex differences.
- **Geographic distribution**: Disproportionately affects low- and middle-income countries with weaker pharmaceutical regulatory/testing infrastructure — India (as a manufacturing source implicated in multiple outbreaks), The Gambia, Indonesia, Uzbekistan, Panama, Haiti, Bangladesh, Nigeria. This reflects supply-chain and regulatory failure rather than any biological geographic susceptibility.
- **Founder effects/consanguinity/ethnic susceptibility**: Not applicable (non-genetic disease).

---

## 10. Diagnostics

**Clinical/laboratory tests:**
- **Basic metabolic panel**: elevated anion gap, metabolic acidosis, elevated BUN/creatinine (AKI), hyperkalemia.
- **Osmolar gap**: may be measured but is a **less sensitive** marker for DEG than for methanol/ethylene glycol due to DEG's higher molecular weight; a normal osmolar gap does **not** exclude DEG poisoning ([EMCrit](https://emcrit.org/ibcc/alcohols/); [PMC7785502](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7785502/)).
- **Liver function tests**: elevated transaminases.
- **Lipase/amylase**: elevated in pancreatitis.
- **Urinalysis**: may show tubular injury markers; oliguria/anuria clinically.
- **Direct DEG/metabolite quantification**: gas chromatography (GC) or GC-mass spectrometry can measure serum DEG, 2-HEAA, and DGA directly and is the definitive diagnostic and forensic/outbreak-investigation tool; also used for pre-/post-hemodialysis clearance monitoring ([WHO analytical methods, Dec 2023](https://www.who.int/news/item/01-12-2023-diethylene-glycol-%28deg%29-and-ethylene-glycol-%28eg%29-contamination---analytical-methods-developed-for-testing-paediatric-medicines)).
- **Renal biopsy/histopathology**: acute tubular necrosis with epithelial vacuolization; documented in the Panama 2006 outbreak investigation as a defining histopathologic feature ([ScienceDirect Panama](https://www.sciencedirect.com/science/article/abs/pii/S0196064413016557)).
- **Nerve conduction studies/EMG**: in the delayed neurologic phase, demonstrates severe sensorimotor peripheral neuropathy (90% of tested cases in one series).
- **CSF analysis**: albuminocytologic dissociation in the delayed neurologic (Guillain-Barré–mimicking) presentation.

**Genetic testing:** Not applicable — DEG poisoning is not diagnosed via genetic testing. (Research-stage transporter/enzyme genotyping — e.g., SLC13A2/NaDC-1 expression — remains investigational and is not part of clinical diagnostic practice.)

**Clinical/diagnostic criteria:** No formal DSM/ICD diagnostic criteria exist beyond history of exposure plus the clinical/laboratory triad of metabolic acidosis, AKI, and (if present) delayed neuropathy. Differential diagnosis includes methanol and ethylene glycol poisoning (toxic alcohol syndromes), sepsis-associated AKI, and Guillain-Barré syndrome (for the delayed neurologic phase) — the latter distinguished by exposure history and the temporal association with preceding AKI.

**Screening:** Population-level "screening" for DEG poisoning takes the form of **regulatory testing of pharmaceutical excipients** rather than individual patient screening:
- USP-NF finished-dosage-form testing methods for DEG/EG ([USP-NF, Feb 2025](https://www.uspnf.com/notices/deg-eg-method-for-finished-dosage-forms-gen-annc-20250228))
- FDA Guidance for Industry (May 2023) mandating DEG/EG testing of glycerin, propylene glycol, maltitol solution, hydrogenated starch hydrolysate, sorbitol solution, and other high-risk components ([Federal Register, May 2023](https://www.federalregister.gov/documents/2023/05/10/2023-09973/testing-of-glycerin-propylene-glycol-maltitol-solution-hydrogenated-starch-hydrolysate-sorbitol); [FDA guidance PDF](https://www.fda.gov/media/174243/download?attachment=))
- WHO-developed two-tier analytical screening approach (TLC screening → GC confirmation) for the International Pharmacopoeia (December 2023) ([WHO](https://www.who.int/news/item/01-12-2023-diethylene-glycol-%28deg%29-and-ethylene-glycol-%28eg%29-contamination---analytical-methods-developed-for-testing-paediatric-medicines))

---

## 11. Outcome/Prognosis

**Mortality:** Case-fatality is highly dependent on dose and access to care. In the 2022 Gambia outbreak, **80% of children who developed AKI died** (66 of 82 cases) ([MMWR](https://www.cdc.gov/mmwr/volumes/72/wr/mm7209a1.htm)). In the 1995–96 Haiti outbreak, of the 76 affected children who remained in Haiti (i.e., were not evacuated for advanced care), only **one is known to have survived** ([PMID:8769471](https://pubmed.ncbi.nlm.nih.gov/8769471/)) — underscoring how outcome is strongly modified by access to dialysis and antidote.
**Overall case-fatality across historical mass-poisoning events has generally exceeded 50% without early antidotal/dialysis treatment**, and can approach near-total mortality in resource-limited settings without dialysis access.

**Morbidity in survivors:**
- Chronic kidney disease / ongoing dialysis dependence, particularly in those who develop the delayed neurologic syndrome.
- Persistent peripheral/cranial neuropathy, though partial improvement over 4–6 months has been documented in some survivors.
- Long-term neurodevelopmental impact in young children who survive AKI is plausible but not well characterized in formal follow-up cohorts — a recognized evidence gap.

**Complications:** Secondary infections (from prolonged dialysis access), cerebral edema (in fulminant encephalopathy, can be directly fatal), chronic renal failure, permanent neurologic deficits.

**Prognostic factors:**
- **Time to treatment** — earlier fomepizole/ethanol administration and earlier hemodialysis initiation both improve survival and reduce long-term damage ([tandfonline, PMID review](https://www.tandfonline.com/doi/full/10.1080/15563650903086444)).
- **Degree of established renal impairment** — predicts subsequent delayed neurotoxicity, i.e., more severe AKI predicts a higher likelihood of the delayed neurologic syndrome ([PMC4616334](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4616334/)).
- **Dose/concentration ingested.**
- **Age** — younger children fare worse in outbreak data, though this partly reflects dosing/exposure patterns rather than purely biological vulnerability.
- **Nutritional status** (multivitamin use, as noted) — protective in the Gambia cohort.

---

## 12. Treatment

**Pharmacotherapy (antidotal, primary treatment):**
- **Fomepizole** (4-methylpyrazole) — competitive ADH inhibitor; blocks DEG bioactivation to toxic metabolites. This is now the preferred first-line antidote given superior safety profile (fewer medication errors/adverse events) compared to ethanol ([Univ. Utah Poison Control](https://poisoncontrol.utah.edu/news/2023/09/fomepizole-antidote)).
  - Dosing: loading dose 15 mg/kg IV, then 10 mg/kg every 12 hours for 4 doses; after 48 hours, dose increases to 15 mg/kg every 12 hours (reflecting fomepizole's autoinduction of its own CYP450-mediated metabolism); dosing/interval must be adjusted during hemodialysis (fomepizole is dialyzable) — continuous or supplemented dosing during HD sessions is required.
  - NCIT term: NCIT:C1421 (Fomepizole) or generic Pharmacotherapy NCIT:C15986 with therapeutic_agent bound to fomepizole.
- **Ethanol** — alternative ADH inhibitor where fomepizole is unavailable; target serum concentration 100–125 mg/dL; requires more intensive monitoring (risk of hypoglycemia, CNS depression, medication errors) than fomepizole ([NEJM fomepizole trial, PMID reference](https://www.nejm.org/doi/full/10.1056/NEJM199903183401102)).
- **Activated charcoal** — considered for early GI decontamination if presentation is within the appropriate window post-ingestion (limited evidence specific to DEG, extrapolated from general toxicology practice).

**Extracorporeal treatment (renal replacement):**
- **Hemodialysis (intermittent, IHD)** — preferred modality; clears both DEG and its toxic metabolites (2-HEAA, DGA), and is essential in patients with significant acidosis, AKI, or large ingestions. Pre-/post-dialysis DEG level monitoring supports effective clearance ([EXTRIP workgroup guidance for the ethylene glycol series, extrapolated to DEG](https://link.springer.com/article/10.1186/s13054-022-04227-2)).
- **CRRT** — recommended when IHD is unavailable.
- Extraction Corporeal Treatments in Poisoning (EXTRIP) criteria for the structurally related ethylene glycol (used analogously for DEG in practice, since no DEG-specific EXTRIP guideline exists): initiate ECTR for severe acidosis (anion gap >27 mmol/L), AKI, coma/seizures, or when standard antidote alone is insufficient; discontinue once anion gap normalizes.
- NCIT term: NCIT:C15571 (Hemodialysis) or broader NCIT:C15329 (Surgical/Interventional Procedure category is not correct — hemodialysis maps under NCIT renal replacement therapy terms).

**Supportive care:**
- Correction of metabolic acidosis (sodium bicarbonate as needed), electrolyte management (hyperkalemia), fluid management, blood pressure support, mechanical ventilation for pulmonary edema/respiratory failure, nutritional/pancreatitis supportive care.
- Rehabilitation (physical/occupational therapy) for survivors with peripheral neuropathy/motor deficits (NCIT:C15302 Physical Therapy; NCIT:C15315 Rehabilitation).

**Experimental/investigational:**
- **NaDC-1 (SLC13A2) inhibition** — proposed as a potential future therapeutic target based on rat transporter data, to block cellular DGA uptake in the kidney and thereby prevent nephrotoxicity independent of ADH blockade timing; not yet in human trials ([PMC10263375](https://pmc.ncbi.nlm.nih.gov/articles/PMC10263375/)).
- No DEG-specific registered clinical trials (NCT) were identified; management is derived by analogy from the ethylene glycol/methanol toxic-alcohol treatment literature and outbreak case-series experience.

**Treatment outcomes:** Fomepizole is associated with reduced medication errors and adverse events relative to ethanol; combined antidote + hemodialysis strategy, initiated early, is associated with markedly improved survival compared with supportive care alone or delayed presentation (as starkly illustrated by the Haiti vs. evacuated-patient outcome contrast).

**Treatment algorithm (general approach):**
1. Recognize elevated anion gap metabolic acidosis with history/suspicion of glycol exposure.
2. Initiate fomepizole (or ethanol if unavailable) as soon as poisoning is suspected — do not wait for confirmatory GC testing.
3. Assess for hemodialysis indications (severe acidosis, AKI, large ingestion, clinical deterioration); initiate IHD/CRRT as indicated.
4. Provide supportive/organ-specific care (renal, hepatic, pancreatic, cardiovascular, respiratory).
5. Monitor for delayed neurologic syndrome in the 1–3 weeks following recovery from the acute renal phase; institute neurologic supportive care/rehabilitation as needed.

---

## 13. Prevention

DEG poisoning is almost entirely **preventable**, and prevention is overwhelmingly a **regulatory/pharmacovigilance** matter rather than a clinical/medical one, since the disease results from a supply-chain contamination failure rather than an intrinsic host risk process.

**Primary prevention (dominant strategy):**
- **Pharmacopoeial testing mandates**: revised USP-NF excipient monographs now require DEG/EG limit testing for glycerin, propylene glycol, sorbitol solution, maltitol solution, hydrogenated starch hydrolysate, and PEG ([USP-NF notice, 2025](https://www.uspnf.com/notices/deg-eg-method-for-finished-dosage-forms-gen-annc-20250228); [FDA guidance, 2023](https://www.fda.gov/media/167974/download)).
- **FDA Guidance for Industry (May 2023)**: mandates testing of high-risk drug components for DEG/EG before use in finished pharmaceutical products ([Federal Register](https://www.federalregister.gov/documents/2023/05/10/2023-09973/testing-of-glycerin-propylene-glycol-maltitol-solution-hydrogenated-starch-hydrolysate-sorbitol)).
- **WHO global alerts and analytical methods**: six WHO Medical Product Alerts (2022–2023) and a validated two-tier TLC-screening/GC-confirmation testing protocol developed for the International Pharmacopoeia, intended for use by national regulatory laboratories, especially in LMICs with limited GC capacity ([WHO, Dec 2023](https://www.who.int/news/item/01-12-2023-diethylene-glycol-%28deg%29-and-ethylene-glycol-%28eg%29-contamination---analytical-methods-developed-for-testing-paediatric-medicines)).
- **Supply-chain/manufacturer oversight**: stricter certificate-of-analysis verification for each batch of glycerin/propylene glycol/sorbitol, rather than relying on supplier certification alone — a repeated root cause across Panama (2006), Haiti (1996), and the 2022–2025 outbreaks was acceptance of falsified or unverified certificates of analysis from chemical intermediaries.
- **Regulatory license revocation/enforcement**: e.g., suspension of Sresan Pharmaceuticals' manufacturing license following the 2025 Madhya Pradesh cluster.

**Secondary prevention (early detection/outbreak response):**
- Rapid epidemiologic investigation and product recall once clusters of unexplained pediatric AKI are recognized (the pattern-recognition approach that identified the causative product in each of the historical outbreaks).
- Sentinel surveillance for pediatric AKI clusters as an early-warning signal for potential DEG/EG contamination events.

**Tertiary prevention:** Early antidotal treatment and dialysis access (see Treatment section) to prevent complications once exposure has occurred.

**Public health interventions:**
- WHO Medical Product Alerts distributed globally to national regulators upon detection of a contaminated product.
- International information-sharing and rapid recall coordination between manufacturing-country and importing-country regulators (a persistent weak point, since several outbreaks involved products exported from one country and causing deaths in another before recall).

**Counseling/behavioral:** Public and prescriber education discouraging use of unregulated/informally sourced liquid medicines, particularly in outbreak-affected regions during active recalls.

**Immunization/prophylactic medication:** Not applicable (non-infectious disease).

---

## 14. Other Species / Natural Disease

- **Taxonomy of affected species**: Primarily a human poisoning syndrome via pharmaceutical/industrial exposure; among animals, **dogs and cats** are the most commonly reported veterinary victims of glycol poisoning, though the veterinary literature overwhelmingly concerns **ethylene glycol** (antifreeze) rather than DEG specifically, reflecting differential product exposure patterns (antifreeze is predominantly ethylene glycol-based) (NCBI Taxon: Canis lupus familiaris NCBITaxon:9615; Felis catus NCBITaxon:9685).
- **Natural/accidental veterinary disease**: DEG-specific veterinary poisoning case reports exist but are far less common in the literature than ethylene glycol veterinary toxicosis; when it occurs, the pathophysiology (ADH/ALDH bioactivation, renal DGA accumulation, proximal tubular necrosis) is believed to be conserved across mammals, consistent with the rat experimental model data forming the bulk of the mechanistic evidence base.
- **Comparative pathology**: The rat is the dominant experimental model and recapitulates the核心 renal pathophysiology (proximal tubular necrosis via DGA/NaDC-1) and, in more recent studies, neurotoxic effects as well ([Clin Toxicol 60:3, PMID female rat neurotoxicity study](https://doi.org/10.1080/15563650.2021.1953049); [Clin Toxicol 59:9, neurotoxic effects](https://www.tandfonline.com/doi/abs/10.1080/15563650.2021.1874403)).
- **Evolutionary conservation**: ADH/ALDH-mediated glycol bioactivation and dicarboxylate-transporter-mediated renal toxicant uptake are conserved biochemical pathways across mammals, underpinning the translational validity of the rat model for human mechanism (though not necessarily for exact dose thresholds — rat LD50 for DEG is far higher on a per-kg basis, 20–25 g/kg, than doses causing severe toxicity in human children, reflecting toxicokinetic/toxicodynamic differences and the smaller absolute margin of safety in small children receiving syrup-dosed medication).
- **Zoonotic potential**: Not applicable — this is a direct chemical toxicity, not a transmissible infectious disease.

---

## 15. Model Organisms

**Primary model: Rat (Rattus norvegicus)** — by far the best-characterized animal model for DEG toxicity.
- **Strains used**: Wistar, Fischer-344, and Wistar-Han rats ([threshold dose-response study, PMID:25545985](https://pubmed.ncbi.nlm.nih.gov/25545985/); [PMC5237385](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5237385/)).
- **Model type**: Chemically induced (acute or repeated-dose oral gavage), not genetic.
- **Key findings**:
  - LD50 in male Wistar rats: 20–25 g/kg body weight.
  - Sharp **threshold dose-response**: at 2 and 5 g/kg DEG, no kidney diglycolic acid (DGA) accumulation or renal/hepatic toxicity occurred in either Wistar or Fischer-344 strains; at 10 g/kg, DGA accumulated markedly and toxicity was observed — establishing that toxicity requires metabolite accumulation past a threshold, not simple dose-linear injury.
  - Toxicokinetics: rapid, near-complete GI absorption; tissue distribution kidney > brain > spleen > liver > muscle > fat ([PMID:8135655](https://pubmed.ncbi.nlm.nih.gov/8135655/)).
  - Nephrotoxicity model recapitulates human findings well: hydropic degeneration of renal tubules, anuria, azotemia, death at 2–7 days post-dosing in high-dose groups.
  - **Neurotoxicity model** (newer, 2021–2022): repeated-dose studies in female rats demonstrated both nephrotoxic and neurotoxic effects of DEG, extending the model beyond the classic acute nephrotoxicity paradigm to capture the delayed neurologic phenotype seen in human survivors ([Clin Toxicol 60:3](https://doi.org/10.1080/15563650.2021.1953049); [Clin Toxicol 59:9](https://www.tandfonline.com/doi/abs/10.1080/15563650.2021.1874403)).
  - **Variable individual susceptibility model** (2023): identical DEG/DGA dosing produced AKI in only ~60% of rats; susceptibility correlated with renal NaDC-1 (SLC13A2) mRNA expression level, providing a candidate mechanistic explanation for the well-documented variable human susceptibility across outbreaks ([PMC10263375](https://pmc.ncbi.nlm.nih.gov/articles/PMC10263375/)).
- **Model limitations**: Rat LD50 (20–25 g/kg) is far higher per unit body weight than doses causing fatal human pediatric poisoning, and rats do not spontaneously develop the classic human delayed cranial-neuropathy/facial-diplegia syndrome in most protocols — the neurotoxicity models capture peripheral neurotoxic endpoints but have not been shown to fully recapitulate the bilateral facial palsy/bulbar syndrome that is the human hallmark. Translational fidelity for the acute nephrotoxicity mechanism (DGA/NaDC-1) is considered high; fidelity for the full human delayed neurologic syndrome is lower/still being established.

**In vitro / cellular models:**
- **Human proximal tubule cells (HPT cells) and RPTEC/TERT1 cell line** — used extensively to establish DGA as the direct nephrotoxic metabolite, to characterize NaDC-1-mediated apical uptake, and to demonstrate that OAT1/OAT3-mediated basolateral efflux does not rescue cells from DGA accumulation ([PMID:21856646](https://pubmed.ncbi.nlm.nih.gov/21856646/); [PMID:36087010](https://pubmed.ncbi.nlm.nih.gov/36087010/); [PMID:36958672](https://pubmed.ncbi.nlm.nih.gov/36958672/)). These in vitro human-cell models are actually a **higher-fidelity human-relevant system** for the core nephrotoxic mechanism than the whole-animal rat model, since they directly use human renal tubule cells.

**Other model systems:** No zebrafish, Drosophila, C. elegans, or iPSC-derived model systems specific to DEG toxicity were identified in this search — this is a notable gap relative to the depth of rat and human-cell-line data, and could represent an opportunity area for future model development (e.g., an iPSC-derived proximal tubule organoid model to further probe individual human variability in NaDC-1 expression/DGA sensitivity).

---

## Summary Table: Suggested Ontology Bindings for KB Curation

| Concept | Suggested term |
|---|---|
| Disease/chemical entity | CHEBI:46807 (diethylene glycol) |
| Related disease entity (nosological neighbor) | ORPHA:31826 (Ethylene glycol poisoning) — no dedicated DEG MONDO/Orphanet term identified |
| Causal gene/enzyme family | ADH1A/ADH1B/ADH1C (hgnc:...), ALDH2 (hgnc:404) — mechanistic, not causal-variant |
| Key transporter | SLC13A2/NaDC-1 (hgnc:11035) |
| Key phenotype (renal) | HP:0001919 Acute kidney injury; HP:0100518 Anuria |
| Key phenotype (neuro) | HP:0010628 Facial palsy; HP:0007141 Peripheral neuropathy; HP:0001298 Encephalopathy |
| Biological process | GO:0006066 alcohol metabolic process; renal dicarboxylate transport |
| Cell type | CL:1001016 kidney proximal tubule epithelial cell |
| Anatomical site | UBERON:0002113 kidney |
| Treatment (antidote) | NCIT — Fomepizole/therapeutic_agent under NCIT:C15986 Pharmacotherapy |
| Treatment (renal replacement) | Hemodialysis / CRRT |

---

## Notable Evidence Gaps

1. **No human genotype-outcome study** has directly tested ADH1B/ALDH2 or SLC13A2 variant effects on DEG poisoning severity, despite strong mechanistic rat/in-vitro rationale.
2. **No standardized quality-of-life outcome data** for DEG poisoning survivors (chronic kidney disease burden, residual neuropathy disability) using EQ-5D/SF-36 or pediatric equivalents.
3. **No DEG-specific EXTRIP consensus guideline** exists; clinical extracorporeal-treatment practice is extrapolated from the ethylene glycol EXTRIP recommendations.
4. **No dedicated MONDO/OMIM identifier** for DEG poisoning as a distinct entity from ethylene glycol poisoning was identified — a candidate curation gap for the disorder ontology.
5. Long-term neurodevelopmental follow-up of young pediatric survivors (the population most affected in the 2022–2025 outbreaks) is not yet published in the peer-reviewed literature.

---

### Sources
- [Solvent Toxicity – Diethylene Glycol](https://u.osu.edu/pesticide/2019/07/01/solvent-toxicity-diethylene-glycol/)
- [Inhibition of Metabolism of Diethylene Glycol Prevents Target Organ Toxicity in Rats (Toxicol Sci, PMID:20530232)](https://pubmed.ncbi.nlm.nih.gov/20530232/)
- [California Poison Control System — DEG Poisoning](https://calpoison.org/content/diethylene-glycol-poisoning)
- [Diethylene glycol poisoning, Clinical Toxicology 47:6](https://www.tandfonline.com/doi/full/10.1080/15563650903086444)
- [Diglycolic Acid Is the Nephrotoxic Metabolite (Toxicol Sci, PMID:21856646)](https://pubmed.ncbi.nlm.nih.gov/21856646/)
- [Global and national actions to prevent trade in substandard and adulterated medicines (PMC11841886)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11841886/)
- [Industrial solvents in medicated syrups (Partnership for Safe Medicines, 2025)](https://www.safemedicines.org/2025/04/cough-syrup.html)
- [Contaminated cough syrups death toll passes 300 (Chemistry World)](https://www.chemistryworld.com/news/contaminated-cough-syrups-death-toll-passes-300-in-four-months/4016993.article)
- [WHO urges action to protect children from contaminated medicines](https://www.who.int/news/item/23-01-2023-who-urges-action-to-protect-children-from-contaminated-medicines)
- [2025 India cough syrup crisis — Wikipedia](https://en.wikipedia.org/wiki/2025_India_cough_syrup_crisis)
- [WHO issues warning over contaminated cough syrup in India (CNN, Oct 2025)](https://www.cnn.com/2025/10/14/world/who-warning-contaminated-cough-syrup-india-deaths-intl-hnk)
- [Poison in a bottle: Madhya Pradesh cough syrup deaths (CPSP)](https://centrepsp.org/media/blog/poison-in-a-bottle-how-a-contaminated-cough-syrup-in-madhya-pradesh-killed-children-and-why-the-world-should-be-outraged/)
- [Clinical, Laboratory, Diagnostic, and Histopathologic Features—Panama, 2006](https://www.sciencedirect.com/science/article/abs/pii/S0196064413016557)
- [Renal toxicity caused by diethylene glycol: an overview (Int Urol Nephrol, PMID:37186212)](https://pubmed.ncbi.nlm.nih.gov/37186212/)
- [Delayed neurologic sequelae resulting from epidemic DEG poisoning (PMID:15902788)](https://pubmed.ncbi.nlm.nih.gov/15902788/)
- [Fomepizole for the Treatment of Ethylene Glycol Poisoning (NEJM)](https://www.nejm.org/doi/full/10.1056/NEJM199903183401102)
- [Childhood DEG poisoning treated with fomepizole and hemodialysis (PMID:10793034)](https://pubmed.ncbi.nlm.nih.gov/10793034/)
- [Fomepizole Antidote — University of Utah Poison Control](https://poisoncontrol.utah.edu/news/2023/09/fomepizole-antidote)
- [EMCrit IBCC — Ethylene glycol & methanol poisoning](https://emcrit.org/ibcc/alcohols/)
- [Extracorporeal treatment for ethylene glycol poisoning: EXTRIP workgroup (Critical Care)](https://link.springer.com/article/10.1186/s13054-022-04227-2)
- [Epidemic of pediatric deaths from acute renal failure caused by DEG (PMID:9555756)](https://pubmed.ncbi.nlm.nih.gov/9555756/)
- [CDC MMWR — Haiti DEG fatalities](https://www.cdc.gov/mmwr/pdf/wk/mm4530.pdf)
- [Fatalities associated with ingestion of DEG-contaminated glycerin — Haiti (PMID:8769471)](https://pubmed.ncbi.nlm.nih.gov/8769471/)
- [DEG poisoning in Nigerian children (PMID:1280035)](https://pubmed.ncbi.nlm.nih.gov/1280035/)
- [Neurological Manifestation of Recreational Fatal and Near-Fatal DEG Poisonings (PMC4616334)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4616334/)
- [Fatal poisoning among young children — Nigeria 2008-2009 (PMID:20010509)](https://pubmed.ncbi.nlm.nih.gov/20010509/)
- [Acute Kidney Injury Among Children — The Gambia, 2022 (MMWR)](https://www.cdc.gov/mmwr/volumes/72/wr/mm7209a1.htm)
- [Hiding in Plain Sight: Catastrophic DEG Poisoning in Children (PMC10695641)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10695641/)
- [Cough syrups: silent killer of Gambian children (PMC10389612)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10389612/)
- [Encephalopathy and peripheral neuropathy following DEG ingestion (Neurology, PMID:15824363)](https://pubmed.ncbi.nlm.nih.gov/15824363/)
- [Diethylene glycol-induced toxicities show marked threshold dose response in rats (PMID:25545985)](https://pubmed.ncbi.nlm.nih.gov/25545985/)
- [Human health assessment for long-term oral ingestion of diethylene glycol](https://www.sciencedirect.com/science/article/pii/S0273230017300806)
- [Neurotoxic effects of nephrotoxic compound diethylene glycol (Clin Toxicol 59:9)](https://www.tandfonline.com/doi/abs/10.1080/15563650.2021.1874403)
- [DEG produces nephrotoxic and neurotoxic effects in female rats (Clin Toxicol 60:3)](https://doi.org/10.1080/15563650.2021.1953049)
- [Toxicokinetics of diethylene glycol (DEG) in the rat (PMID:8135655)](https://pubmed.ncbi.nlm.nih.gov/8135655/)
- [USP-NF — DEG/EG Testing Method for Finished Dosage Forms](https://www.uspnf.com/notices/deg-eg-method-for-finished-dosage-forms-gen-annc-20250228)
- [FDA — Testing of Glycerin, Propylene Glycol, Maltitol](https://www.fda.gov/media/167974/download)
- [FDA Guidance Outlines Expectations (Sidley Austin)](https://www.sidley.com/en/insights/newsupdates/2023/08/fda-guidance-outlines-expectations-to-mitigate-the-risk-of-contamination-of-drug-products)
- [Federal Register — Testing of High-Risk Drug Components (May 2023)](https://www.federalregister.gov/documents/2023/05/10/2023-09973/testing-of-glycerin-propylene-glycol-maltitol-solution-hydrogenated-starch-hydrolysate-sorbitol)
- [FDA — Testing of High-Risk Drug Components for DEG and EG](https://www.fda.gov/media/174243/download?attachment=)
- [WHO — DEG/EG analytical methods for paediatric medicines (Dec 2023)](https://www.who.int/news/item/01-12-2023-diethylene-glycol-%28deg%29-and-ethylene-glycol-%28eg%29-contamination---analytical-methods-developed-for-testing-paediatric-medicines)
- [Molecular basis for selective uptake and elimination of organic anions by OAT1 (Nat Struct Mol Biol)](https://www.nature.com/articles/s41594-023-01039-y)
- [Lack of efflux of diglycolic acid from proximal tubule cells (PMID:36958672)](https://pubmed.ncbi.nlm.nih.gov/36958672/)
- [Role of Plasma Membrane Dicarboxylate Transporters in DGA Uptake (Toxicol Sci 190:1, PMID:36087010)](https://academic.oup.com/toxsci/article/190/1/1/6695230?login=false)
- [Diglycolic acid chelates calcium and produces renal mitochondrial dysfunction (Clin Toxicol 54:6, PMID:27002734)](https://www.tandfonline.com/doi/full/10.3109/15563650.2016.1162312)
- [Variable sensitivity to DEG poisoning related to NaDC-1 uptake transporter differences (PMC10263375)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10263375/)
- [Protective factors against AKI in children exposed to DEG-contaminated medicines — The Gambia (PLOS GPH)](https://journals.plos.org/globalpublichealth/article?id=10.1371%2Fjournal.pgph.0005512)
- [Causes and risk factors for AKI outbreak — The Gambia (PLOS ONE)](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0324931)
- [Clinical phenotypes and severity stratification — Gambia AKI outbreak latent class analysis (Pediatr Nephrol)](https://link.springer.com/article/10.1007/s00467-026-07148-2)
- [Medication-Associated DEG Mass Poisoning — A Preventable Cause of Illness and Death (PMC10081810)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10081810/)
- [ZFIN — CHEBI:46807 diethylene glycol](https://zfin.org/CHEBI:46807)
- [Orphanet — Ethylene glycol poisoning (ORPHA:31826)](https://www.orpha.net/en/disease/detail/31826)
- [Diethylene glycol — Wikipedia](https://en.wikipedia.org/wiki/Diethylene_glycol)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 31 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 31 |
| On topic | 18 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMC:PMC11841886` (3 mentions) - Global and national actions to prevent trade in substandard and adulterated medicines.
  - shared terms: none

Weighed against this report's own most characteristic terms: `deg`, `poisoning`, `renal`, `glycol`, `outbreak`, `aki`, `kidney`, `toxic`, `dga`, `nadc-1`, `disease`, `delayed`, `metabolite`, `exposure`, `peripheral`, `human`, `acute`, `ethylene`, `proximal`, `adh`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 59 |
| Resolved | 57 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 28 |
| Terms named correctly | 17 |
| Terms named as a **different** term | 7 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `CHEBI:46807` (8 mentions) - the report calls it "parent compound", "diethylene glycol"; CHEBI calls it **diethylene glycol**
- `HP:0012647` (1 mention) - the report calls it "Autonomic dysfunction"; HP calls it **Abnormal inflammatory response**
- `CL:0000182` (1 mention) - the report calls it "site of ADH/ALDH-mediated bioactivation and secondary hepatotoxicity"; CL calls it **hepatocyte**
- `CL:0002064` (1 mention) - the report calls it "site of DEG-associated pancreatitis"; CL calls it **pancreatic acinar cell**
- `NCIT:C1421` (1 mention) - the report calls it "Fomepizole"; NCIT calls it **Oxygen Radical**
- `NCIT:C15571` (1 mention) - the report calls it "Hemodialysis"; NCIT calls it **Differentiation Therapy**
- `NCIT:C15329` (1 mention) - the report calls it "Surgical/Interventional Procedure category is not correct — hemodialysis maps under NCIT renal replacement therapy terms"; NCIT calls it **Surgical Procedure**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0070265` (obsolete necrotic cell death) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001942` (2 mentions) - the report calls it "Metabolic acidosis (high or normal anion gap)", "Refractory metabolic acidosis"; HP calls it **Metabolic acidosis**
- `HP:0001733` (1 mention) - the report calls it "Acute pancreatitis"; HP calls it **Pancreatitis**
- `HP:0007141` (2 mentions) - the report calls it "Sensorimotor peripheral neuropathy"; HP calls it **Sensorimotor neuropathy**, and lists "Sensorimotor peripheral neuropathy" among its other names
- `CL:1001016` (2 mentions) - the report calls it "kidney proximal convoluted tubule epithelial cell"; CL calls it **kidney loop of Henle ascending limb epithelial cell**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CHEBI:46807` - called "parent compound", "diethylene glycol"
- `HP:0001942` - called "Metabolic acidosis (high or normal anion gap)", "Refractory metabolic acidosis"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.