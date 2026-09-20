---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-10T18:23:46.785531'
end_time: '2026-09-10T18:29:24.396260'
duration_seconds: 337.61
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Resistance to Thyroid Hormone Alpha
  mondo_id: MONDO:0013757
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
  num_turns: 23
  total_cost_usd: 1.4222024
  session_id: 0ecd1216-33cc-58da-968d-9ba73b5b4eb1
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 25
reference_validation:
  total_references: 20
  verified: 20
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 20
  on_topic: 18
  validator_version: 0.2.1
term_validation:
  total_terms: 48
  verified: 44
  not_found: 1
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.022
  labels_checked: 41
  labels_matching: 32
  labels_mismatched: 6
  mislabelled_terms:
  - term_id: HP:0010701
    reported_labels:
    - Skin tags
    ontology_label: Abnormal circulating immunoglobulin concentration
  - term_id: HP:0001923
    reported_labels:
    - Normocytic anemia
    ontology_label: Reticulocytosis
  - term_id: GO:0004887
    reported_labels:
    - thyroid hormone receptor activity
    ontology_label: GO_0004887
  - term_id: GO:0007416
    reported_labels:
    - synapse assembly, for GABAergic interneuron defect
    ontology_label: synapse assembly
  - term_id: CL:0000216
    reported_labels:
    - "Sertoli cell \u2014 relevant to gonadal expression studies"
    ontology_label: Sertoli cell
  - term_id: UBERON:0001968
    reported_labels:
    - skeletal system
    ontology_label: semen
  labels_variant: 3
  unresolved_terms:
  - HP:0008977
  obsolete_terms:
  - term_id: GO:0004887
    ontology_label: GO_0004887
    replaced_by: GO:0004879
  unresolvable_prefixes:
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Resistance to Thyroid Hormone Alpha
- **MONDO ID:** MONDO:0013757 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Resistance to Thyroid Hormone Alpha** covering all of the
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

# Resistance to Thyroid Hormone Alpha (RTHα) — Comprehensive Research Report

**MONDO:0013757** | **OMIM #614450** (listed as *Hypothyroidism, Congenital, Nongoitrous, 6; CHNG6*) | **Gene:** THRA (HGNC:11796, OMIM *190120, 17q21.1) | **Orphanet:** ORPHA 566231 | **ICD-10:** E07.8 (Other specified disorders of thyroid) | **Category:** Mendelian, autosomal dominant

---

## 1. Disease Information

**Overview.** Resistance to thyroid hormone alpha (RTHα) is a rare autosomal dominant disorder caused by heterozygous, dominant-negative loss-of-function variants in *THRA*, the gene encoding thyroid hormone receptor alpha (TRα). Unlike classic "generalized" resistance to thyroid hormone (RTHβ, caused by *THRB* mutations), RTHα produces **tissue-specific hypothyroidism** confined largely to TRα1-expressing tissues (CNS, heart, gut, skeletal muscle, bone, erythroid precursors), while thyroid function tests remain near-normal because the hypothalamic-pituitary-thyroid feedback axis is governed by TRβ, which is unaffected. The first case was reported by Bochukova et al. in 2012 (PMID:22168587, *N Engl J Med*), describing a child with classic clinical features of hypothyroidism (growth retardation, developmental delay, skeletal dysplasia, severe constipation) but only borderline-abnormal thyroid function tests; whole-exome sequencing identified a de novo heterozygous nonsense variant (c.1207G>T, p.Glu403X) that "generated a mutant protein that inhibited wild-type receptor action in a dominant negative manner."

Only **~41 cases from ~28 families** had been published in the literature as of the most recent comprehensive review period (2020–2024), making it an ultra-rare condition that is likely substantially underdiagnosed because, unlike RTHβ, standard thyroid function tests are not distinctive (van Mullem et al., *Best Pract Res Clin Endocrinol Metab* 2015, PMID:26303090).

**Identifiers:**
- OMIM #614450 (CHNG6)
- OMIM gene *190120 (THRA)
- Orphanet ORPHA566231
- MONDO:0013757
- HGNC:11796 (THRA)
- ICD-10: E07.8
- MeSH: THRA is indexed under "Thyroid Hormone Resistance Syndrome" (no disease-specific MeSH heading yet exists for RTHα specifically; it is typically captured under the RTH parent term)

**Synonyms:** Resistance to thyroid hormone due to a mutation in thyroid hormone receptor alpha; RTHα; THRA-related resistance to thyroid hormone; Congenital nongoitrous hypothyroidism 6 (CHNG6); Thyroid hormone resistance, alpha.

**Evidence base:** Nearly all data derive from individual case reports and small case series (aggregated in narrative and systematic reviews) rather than large epidemiologic cohorts or EHR-derived data, reflecting the condition's rarity (~41 published cases worldwide).

---

## 2. Etiology

**Disease Causal Factors.** RTHα is a purely genetic, monogenic disorder: heterozygous dominant-negative variants in *THRA* are both necessary and sufficient to cause the phenotype. There is no known environmental, infectious, or purely mechanistic (non-genetic) causal pathway.

**Genetic risk factors:**
- Heterozygous *THRA* variants affecting the ligand-binding domain (LBD) (most reported variants) or, less commonly, variants affecting both TRα1 and the non-hormone-binding TRα2 isoform.
- De novo occurrence is common; ~6 of the reported variants have been inherited from an affected parent, consistent with autosomal dominant transmission with full penetrance but markedly variable expressivity (van Mullem 2015, PMID:26303090; JCRPE clinical spectrum review 2021, PMC7947725).
- Genotype severity correlates loosely with variant class: **frameshift/premature-stop variants → more severe phenotype**; **missense variants → generally milder phenotype**, though there is documented intrafamilial variability even with an identical missense variant (Nauwynck et al., *Horm Res Paediatr* 2026, PMID:42301959 — a mother and two daughters sharing c.1207G>A showed markedly different severity, "cannot be predicted by genotype alone").

**Environmental risk factors:** None established. There is no evidence that toxins, diet, occupational exposure, or perinatal factors modify risk of developing RTHα (it is not multifactorial).

**Protective Factors:** No protective genetic or environmental factors have been identified in the literature (the disease is fully penetrant for at least some phenotypic feature once the causal variant is present).

**Gene-Environment Interactions:** Not applicable/not reported; no GxE interaction data exist for this ultra-rare Mendelian disorder.

---

## 3. Phenotypes

The clinical picture is one of selective, tissue-specific hypothyroidism. Frequencies below are drawn from the JCRPE 2021 systematic clinical-spectrum review of published cases (PMC7947725) unless noted.

### Neurodevelopmental / Behavioral
- **Delayed motor and speech milestones** — ~85% (34/40 cases). HPO: *Motor delay* (HP:0001270), *Delayed speech and language development* (HP:0000750)
- **Dyspraxia / ataxic, broad-based gait**, slow dysarthric speech — described as a major source of disability across ages. HPO: *Dysdiadochokinesis*/ *Gait ataxia* (HP:0002066), *Dysarthria* (HP:0001260)
- **Intellectual disability**, variably reduced IQ — HPO: *Intellectual disability* (HP:0001249)
- **Autism spectrum features / ASD-associated variants** — 6 *THRA* variants identified among 30 children screened in ASD cohorts (Kalikiri et al., *Autism Res* 2017, PMID:28856816). HPO: *Autistic behavior* (HP:0000729)
- **Seizures** — reported in a minority of cases. HPO: *Seizure* (HP:0001250)

### Growth / Skeletal
- **Short stature / growth retardation** — ~60% (12/20 children), lowest height SD score −3.1. HPO: *Short stature* (HP:0004322)
- **Relative macrocephaly** — ~70% (23/33). HPO: *Macrocephaly* (HP:0000256)
- **Delayed bone age / skeletal dysplasia / epiphyseal dysgenesis** (childhood-specific; resolves in adulthood). HPO: *Delayed skeletal maturation* (HP:0002750), *Epiphyseal dysplasia* (HP:0002656)
- **Wormian bones** (serpiginous cranial sutures, delayed fontanelle closure) — 32% (10/31). HPO: *Wormian bones* (HP:0002645)
- **Delayed tooth eruption** — 44% (8/18 children). HPO: *Delayed eruption of teeth* (HP:0000684)
- **Short/broad facies, hypertelorism, flattened nose, macroglossia, thick lips** (coarse facial gestalt) in ~one-third. HPO: *Coarse facial features* (HP:0000280), *Macroglossia* (HP:0000158)
- **Thickened calvarium / cortical hyperostosis / increased bone mineral density** — characteristic in adults. HPO: *Cranial hyperostosis* (HP:0004437)
- Short limbs, disproportionate short stature — reported in untreated adults (Bauer Westbye et al., *J Endocr Soc* 2023, PMID for bvad089 not captured in this pass)

### Gastrointestinal
- **Chronic constipation** — 84% (26/31) — one of the most consistent findings across the lifespan, attributed to decreased colonic peristalsis (documented by manometry). HPO: *Constipation* (HP:0002019)
- Umbilical/inguinal hernias reported.

### Dermatologic
- **Skin tags and moles** (acrochordons), more prominent in adults — 21% (7/33). HPO: *Skin tags* (HP:0010701)
- Rough, dry, thickened skin, particularly in children.

### Hematologic
- **Mild, usually normocytic anemia** — 77% (23/30); near-universal feature, unresponsive to hematinics, with normal iron/B12/folate (van Gucht et al., *J Clin Endocrinol Metab* 2017, PMID:28911146). HPO: *Normocytic anemia* (HP:0001923)

### Cardiovascular / Metabolic
- **Bradycardia**, abnormal sympathovagal balance, cardiac contractility indices in the hypothyroid range. HPO: *Bradycardia* (HP:0001662)
- Rare cardiomyopathy (3 cases) and pericardial effusion (1 case) reported.
- **Low resting metabolic rate**. HPO: *Decreased basal metabolic rate* (HP:0008977, if applicable — verify against enum)
- Hepatic steatosis reported in adult cases (Nauwynck 2026).
- Elevated LDL cholesterol. HPO: *Hypercholesterolemia* (HP:0003124)

### Laboratory abnormalities
- **Elevated muscle creatine kinase** — 73% (8/11 untreated children), range 218–981 U/L; proposed as a pediatric diagnostic biomarker.
- Characteristic thyroid profile (see Section 4/biochemistry).

**Phenotype characteristics:**
- **Age of onset:** Typically present from infancy/early childhood (growth faltering, developmental delay noted in first years of life); a subset of adult-onset features (tachycardia, hepatic steatosis, social/learning difficulties) may only become apparent or be recognized retrospectively in adulthood.
- **Severity:** Highly variable — ranges from severely affected children (frameshift variants) to adults with mild learning difficulties who attended university untreated.
- **Progression:** The "clinical picture or laboratory findings becom[e] less remarkable with age" in several domains (e.g., epiphyseal dysgenesis present in childhood is absent in adult imaging), but anemia, constipation, and cognitive effects can persist into adulthood.
- **Frequency:** See percentages above (JCRPE 2021 review, n≈40 cases).

**Quality-of-life impact:** Motor dyspraxia, dysarthric speech, chronic constipation, fatigue, low mood, social dysfunction, and learning disabilities requiring educational support are reported to meaningfully affect daily functioning in both children (school performance) and untreated adults (concentration problems, excessive daytime sleepiness, social dysfunction) (Bauer Westbye/JES 2023 untreated-adult cohort).

---

## 4. Genetic/Molecular Information

**Causal gene:** *THRA* (HGNC:11796; OMIM *190120), chromosome 17q21.1.

**Gene structure/isoforms:** *THRA* produces two principal splice isoforms:
- **TRα1** — the biologically active, T3-binding nuclear receptor; high expression in CNS, myocardium, GI tract, skeletal muscle, bone. Molecular function: GO:0004887 (thyroid hormone receptor activity).
- **TRα2** — lacks a functional ligand-binding domain due to alternative C-terminal splicing; does not bind T3 but retains DNA-binding capacity and may act as an endogenous inhibitor of TRα1 signaling. RNA-seq data indicate **TRα2 strongly predominates over TRα1 in the developing and adult human brain**, a point relevant to interpreting variants that differentially affect the two isoforms.

**Pathogenic variant spectrum (as of 2024 review, ~25 distinct variants across ~28 families):**
- **Missense variants** — most common class; generally milder phenotype; concentrated in the ligand-binding domain.
  - Examples with published functional characterization:
    - **p.Glu403X** (c.1207G>T) — the index Bochukova 2012 nonsense variant (PMID:22168587).
    - **p.Ala263Val (A263V)** — affects both TRα1 and TRα2; homologous to the RTHβ-causing *THRB* A317V variant; transcriptionally impaired at low T3 but function was restorable at higher hormone concentrations, "revers[ing] its dominant negative inhibitory activity" — a nuance relevant to high-dose therapy rationale.
    - **p.Asn359Tyr (N359Y)** — de novo, affects both isoforms; dominant-negative for TRα1, weaker dominant-negative effect for TRα2, especially when co-expressed with normal TRβ1.
    - **p.Arg384Cys (R384C)** — identified via whole-genome sequencing in an autism cohort; shown to be functionally deleterious in murine TRα1; transgenic mice exhibited aberrant GABAergic interneuron development and behavioral abnormalities that were reversible with thyroid hormone treatment initiated even in adulthood.
    - **p.Asp268Asn** — reported with early levothyroxine treatment and outcome data (*J Pediatr Endocrinol Diabetes*, recent case report).
    - **p.Arg417Ter** (c.1249C>T) and **p.Glu173Gly** (c.518A>G) — both logged in ClinVar under "Congenital nongoitrous hypothyroidism 6."
  - A **synonymous substitution** (c.1044G>T) was found in one autism cohort case, of uncertain pathogenicity for classic RTHα.
- **Frameshift variants** — 3 reported variants affecting 4 cases, associated with the most severe phenotypes.
- **Nonsense/premature stop variants** — 3 distinct variants.

**Variant classification (ACMG/AMP):** Per ClinVar, reported variants are generally classified Pathogenic/Likely Pathogenic for "Congenital nongoitrous hypothyroidism 6." Functional (in vitro transactivation/dominant-negative) assays are typically required to confirm pathogenicity of novel missense variants given the absence of a distinctive biochemical signature.

**Variant origin:** All reported RTHα cases are **germline**, heterozygous. No somatic *THRA* RTHα has been described (contrast with oncology literature in which *THRA*/TRα dysregulation — not classic RTHα missense variants — has been separately studied in some cancers; not relevant to this germline syndrome).

**Allele frequency in population databases:** *THRA* is under strong purifying selection for loss-of-function in gnomAD (constrained gene); reported RTHα pathogenic missense/truncating variants are essentially absent from population databases (gnomAD/ExAC/1000 Genomes), consistent with de novo origin and dominant pathogenicity — precise per-variant gnomAD frequencies were not captured in this pass and should be verified directly in gnomAD/ClinVar at curation time.

**Functional consequence — mechanism:** **Dominant-negative loss of function.** The mutant TRα1 protein retains DNA-binding and corepressor-binding capacity but fails to release corepressor complexes (NCoR1/SMRT + histone deacetylase, HDAC) upon T3 binding, resulting in "constitutive binding of mutant TR to corepressors, with failure of corepressor dissociation and coactivator recruitment following T3 occupancy," which "likely mediates dominant negative inhibition" over the co-expressed wild-type allele and, where relevant, TRβ (van Mullem 2015, PMC4559105).

**Modifier genes:** None formally established; authors speculate that "additional factors, possibly cofactor proteins" (e.g., corepressor/coactivator stoichiometry) contribute to the marked phenotypic variability seen even among carriers of an identical variant (intrafamilial variability, Nauwynck 2026).

**Epigenetic information:** No disease-specific DNA methylation/histone studies of patient tissue have been published; however, the core molecular mechanism is itself an epigenetic one at target-gene promoters — mutant TRα1 causes "constant HDAC-induced chromatin remodeling" that sustains transcriptional repression of T3 target genes even when hormone is present (mechanistic basis for HDAC-inhibitor experimental therapy, see Section 12).

**Chromosomal abnormalities:** No large structural/chromosomal (aneuploidy, translocation, CNV) etiology has been reported for RTHα; all reported cases are point variants (missense, nonsense, frameshift) within *THRA*.

---

## 5. Environmental Information

RTHα is a purely monogenic disorder. No environmental toxins, occupational exposures, lifestyle factors, or infectious agents have been implicated as causal or disease-modifying in the literature reviewed. This section is not applicable beyond noting that iodine status and maternal thyroid status during pregnancy are not reported to influence phenotype expression in *THRA* variant carriers (distinct from acquired thyroid disease).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. A heterozygous *THRA* variant (missense in the ligand-binding domain, or frameshift/nonsense) **leads to** expression of a mutant TRα1 protein (and, for variants upstream of the TRα2-specific exon, mutant TRα2) that retains DNA- and corepressor-binding activity but cannot release corepressor upon T3 binding.
2. This mutant receptor **results in** a dominant-negative effect: it competes with and suppresses the transcriptional activity of the co-expressed wild-type TRα1 allele (demonstrated mechanism) in TRα1-predominant tissues.
3. Constitutive corepressor (NCoR1/SMRT) and HDAC binding **leads to** persistent chromatin compaction at T3-responsive target gene promoters, i.e., a state of molecular/cellular hypothyroidism at the target-gene transcription level, **despite** near-normal circulating T3/T4 — this is the "tissue-specific hypothyroidism" hallmark of RTHα (inferred primarily from animal/in vitro reporter and chromatin studies, extrapolated to human disease).
4. Because the hypothalamic-pituitary-thyroid axis senses hormone levels predominantly via **TRβ** (which is unaffected), the pituitary/hypothalamus do **not** perceive tissue hypothyroidism, so **TSH fails to rise compensatorily** — **explaining** the near-normal-to-low-normal TSH and the diagnostic pitfall of relying on standard thyroid function tests.
5. In parallel, peripheral deiodinase handling is shifted (reduced TRα-mediated negative regulation of deiodinase activity is hypothesized), **resulting in** the characteristic biochemical signature: low/low-normal free T4, high/high-normal free T3, low/low-normal reverse T3, and an abnormally low FT4/FT3 ratio (directly demonstrated biochemically in patients; deiodinase-level mechanism is partly inferred).
6. In the **CNS** (where TRα1 — and especially TRα2 — predominates developmentally), impaired T3 target gene activation **leads to** abnormal neuronal/glial maturation, including — in the R384C mouse model — "aberrant development of GABAergic inhibitory interneurons," which **manifests clinically** as delayed motor/speech milestones, dyspraxia, ataxic gait, intellectual disability, and (in some cases) ASD features and seizures. This step is directly demonstrated in a murine model and inferred to extend to humans by phenotypic analogy.
7. In the **growth plate/skeleton**, dominant-negative TRα1 signaling **causes** delayed chondrocyte maturation and epiphyseal dysgenesis in childhood, **resulting in** short stature, delayed bone age, delayed tooth eruption, and the wormian-bone/cranial-suture phenotype; with skeletal maturation proceeding anomalously into adulthood as thickened calvarium/cortical hyperostosis and increased bone mineral density (demonstrated in both human imaging series and the Thra1^PV/+ mouse model).
8. In the **gastrointestinal tract**, impaired TRα1 signaling in enteric smooth muscle/neurons **leads to** decreased colonic peristalsis, **manifesting as** the near-universal chronic constipation.
9. In **bone marrow erythroid progenitors**, TRα1 dysfunction **impairs the balance between proliferation and differentiation**: patient-derived human erythroid progenitor cells (HEPs) show delayed spontaneous differentiation (~2 days later than controls), larger cell size, reduced glycophorin A (CD235a, a terminal differentiation marker) and increased c-Kit (CD117, a proliferation marker); exogenous T3 still accelerates differentiation in both control and patient cells, implying reduced (not absent) hormone sensitivity rather than complete unresponsiveness — **resulting in** the near-universal mild normocytic anemia (van Gucht 2017, PMID:28911146, direct human cell evidence).
10. In **cardiac and skeletal muscle**, TRα1 dysfunction **results in** reduced basal metabolic rate, bradycardia with abnormal sympathovagal balance, and elevated muscle creatine kinase — indices consistent with a tissue-level hypothyroid state that is relatively **resistant to correction** by standard-dose levothyroxine (see Treatment, Section 12), suggesting either incomplete T3 delivery/activation or genuinely reduced receptor responsiveness even at higher local hormone levels in these tissues.
11. **Hepatic involvement** (steatosis, elevated LDL/HDL ratio) has been reported in adult cases and is consistent with TRα1's role in lipid/metabolic regulation, though the liver is traditionally considered more TRβ-dominant — this cross-tissue effect is less well mechanistically characterized and should be considered a partially inferred branch of the pathway.

### Molecular pathways
- Canonical **thyroid hormone receptor signaling** (nuclear receptor transcriptional regulation): GO:0006355 (regulation of DNA-templated transcription) downstream of GO:0004887 (thyroid hormone receptor activity).
- **NCoR1/SMRT-HDAC corepressor pathway**: central to the dominant-negative mechanism — GO:0035035 (histone acetyltransferase binding) / corepressor-related GO terms.

### Cellular processes
- Impaired **erythroid progenitor proliferation/differentiation balance** (GO:0030218, erythrocyte differentiation).
- Impaired **chondrocyte/osteoblast maturation** in growth plate (relevant to skeletal dysplasia).
- Altered **GABAergic interneuron development** in cortex (murine R384C model).

### Protein dysfunction
- Loss-of-function/dominant-negative missense or truncating changes in the TRα1 ligand-binding domain (helix 12 disruption in the mouse PV model prevents T3 binding/coactivator recruitment) or DNA-binding domain; UniProt P10827 (THRA/TRα). No protein aggregation/misfolding mechanism — this is a transcription-factor dominant-negative disorder, not a proteopathy.

### Biochemical abnormalities
- Characteristic pattern: low/low-normal FT4, high/high-normal FT3, low FT4/FT3 ratio, low/low-normal reverse T3, normal TSH, elevated CK (children especially), mild normocytic anemia, elevated LDL/total cholesterol, low/low-normal IGF-1, elevated IL-8 (pro-inflammatory).

### Molecular profiling / advanced technologies
- RNA-seq data show TRA2 isoform predominance over TRα1 in developing/adult human brain (relevant to interpreting CNS phenotype severity by variant location).
- No large-scale patient transcriptomic, proteomic, or single-cell atlases specific to RTHα patient tissue were identified in this search pass; most molecular data derive from reporter-gene assays, patient-derived erythroid progenitor cultures, and murine/zebrafish models rather than from GEO/ArrayExpress patient cohorts.

**Suggested ontology terms:**
- GO biological processes: GO:0006355 (regulation of transcription), GO:0030218 (erythrocyte differentiation), GO:0001501 (skeletal system development), GO:0007416 (synapse assembly, for GABAergic interneuron defect)
- GO molecular function: GO:0004887 (thyroid hormone receptor activity)
- Cell types (CL): CL:0000765 (erythroblast), CL:0000038 (erythroid progenitor cell), CL:0000138 (chondrocyte), CL:0000617 (GABAergic interneuron), CL:0000187 (myocyte), CL:0000216 (Sertoli cell — relevant to gonadal expression studies)

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Central nervous system (brain), skeletal system (growth plate, calvarium, teeth), gastrointestinal tract (colon), hematopoietic system (bone marrow/erythroid lineage), cardiovascular system (heart).
- **Secondary:** Liver (steatosis, lipid abnormalities reported in adults), skin (skin tags, dry/thickened skin).
- **Body systems:** Endocrine, nervous, musculoskeletal, digestive, hematologic, cardiovascular.

**Tissue/cell level:**
- Colonic smooth muscle/enteric neurons (constipation).
- Growth-plate chondrocytes, osteoblasts/osteoclasts (skeletal dysplasia, increased cortical bone).
- Erythroid progenitor cells in bone marrow (anemia).
- Cortical GABAergic interneurons (murine model; presumptive human analog).
- Cardiac myocytes (bradycardia, reduced contractility indices).
- Skeletal muscle (elevated CK).

**Subcellular level:**
- Nucleus — GO:0005634 (nucleus); TRα1 acts as a nuclear hormone receptor/transcription factor at target-gene promoters, with corepressor complexes recruiting HDAC to chromatin (GO:0000118, histone deacetylase complex).

**Localization (UBERON):**
- UBERON:0000955 (brain), UBERON:0001968 (skeletal system), UBERON:0001155 (colon), UBERON:0002371 (bone marrow), UBERON:0000948 (heart), UBERON:0002107 (liver).
- Lateralization: Not applicable; RTHα is a systemic, bilateral/symmetric disorder with no laterality pattern reported.

---

## 8. Temporal Development

**Onset:** Congenital/early-childhood onset for most features (growth faltering, developmental delay, delayed bone age typically recognized in infancy–early childhood); some features (hepatic steatosis, learning/social difficulties, tachycardia) are reported or first characterized in adulthood, either as persistence/evolution of the childhood phenotype or as later recognition in previously undiagnosed mild cases (e.g., the mother in the Nauwynck 2026 kindred).

**Onset pattern:** Insidious/chronic rather than acute — there is no described acute crisis presentation (contrast with, e.g., thyroid storm in Graves disease).

**Progression:**
- Several skeletal features (epiphyseal dysgenesis) that are prominent in childhood are **not** present in adult imaging — i.e., some aspects of the phenotype attenuate with growth-plate closure.
- Conversely, thickened calvarium/cortical hyperostosis and increased bone mineral density become **more** prominent in adults.
- Anemia, constipation, and neurocognitive effects can persist through adulthood.
- Overall the disease course is **stable-to-slowly-evolving** rather than progressive/degenerative; it is not described as a relapsing-remitting condition.

**Disease duration:** Chronic, lifelong — there is no spontaneous remission described, though the clinical and biochemical picture tends to become "less remarkable" with age in several (not all) domains.

**Critical periods:** Early childhood appears to be a critical window for neurodevelopmental intervention — case reports emphasize that "early treatment initiation yields more distinguishable developmental benefits," paralleling the R384C mouse data showing some interneuron/behavioral abnormalities are reversible with T3 treatment even in adulthood but presumably with better outcomes if treated early.

---

## 9. Inheritance and Population

**Epidemiology:**
- **Prevalence:** Orphanet lists RTHα as prevalence <1 in 1,000,000 (ultra-rare). Approximately 41 cases across ~28 families have been published in the literature as of the most recent reviews (2021–2024), though the disorder is considered underdiagnosed given the non-distinctive standard thyroid panel.
- **Incidence:** Not formally estimated in any population-based registry; no birth-prevalence studies exist.

**Inheritance pattern:** Autosomal dominant, with dominant-negative molecular mechanism. Most cases are **de novo**; at least 6 of the published variants have been transmitted from an affected parent, confirming vertical transmission is possible and documented.

**Penetrance:** Appears to be high/complete for at least some phenotypic feature (all reported heterozygous carriers show some abnormality), but with markedly **incomplete and variable expressivity** — severity is not predictable from genotype alone, as demonstrated by intrafamilial variability with an identical variant (Nauwynck 2026).

**Expressivity:** Highly variable, even within families carrying the identical missense variant — documented biochemical attenuation in an affected mother compared to her more severely affected daughters, and clinical heterogeneity (only one of two affected sisters had constipation and delayed dentition).

**Genetic anticipation:** Not reported/described for RTHα (not a repeat-expansion disorder).

**Germline mosaicism:** Not specifically documented in the literature reviewed, though it remains a theoretical consideration for any de novo dominant disorder when counseling families with an apparently de novo proband.

**Founder effects:** None reported; variants identified to date are private/family-specific rather than recurrent founder alleles in specific populations.

**Consanguinity:** Not implicated — consistent with a dominant (not recessive) mechanism.

**Carrier frequency:** Not applicable in the traditional sense (autosomal dominant, not a recessive carrier state); population databases (gnomAD) show the gene to be constrained, with disease-causing variants essentially absent from the general population.

**Population demographics:**
- No specific ethnic or geographic enrichment has been established; cases have been reported from Europe (UK, Netherlands, Belgium, Scandinavia), the Middle East/North Africa (first MENA case report, PMC7897355), and elsewhere — consistent with a panethnic, privately-occurring de novo disorder rather than one with population-specific founder variants.
- **Sex ratio:** Not clearly skewed in the literature; both males and females are affected (the described kindreds include affected mother-daughter pairs and isolated cases of both sexes).
- **Age distribution:** Spans neonatal/infantile presentation through adulthood (documented adult cohort up to at least the 4th–5th decade, e.g., the untreated-adult *J Endocr Soc* cohort and 17-year follow-up case report).

---

## 10. Diagnostics

**Clinical/laboratory tests:**
- **Thyroid function panel** (FT4, FT3, TSH, reverse T3) — the key diagnostic clue is **low/low-normal FT4 + high/high-normal FT3 + normal TSH**, yielding a **low FT4/FT3 ratio** and a **high T3/rT3 ratio**; reverse T3 is characteristically low/low-normal. Crucially, TSH is **not** elevated (distinguishing it from primary hypothyroidism and from RTHβ, where TSH is typically elevated/inappropriately normal with high T4). LOINC analytes: Free T4, Free T3, TSH, Reverse T3.
- **Creatine kinase (CK)** — elevated in the majority of untreated children (73%, range 218–981 U/L); proposed as a pediatric screening/diagnostic biomarker, though normal in most untreated adults.
- **Complete blood count** — mild normocytic (occasionally macrocytic) anemia with normal iron/B12/folate.
- **Lipid panel** — elevated total/LDL cholesterol, elevated LDL/HDL ratio.
- **Imaging** — skeletal survey/plain films for wormian bones, delayed bone age (childhood), thickened calvarium/cortical hyperostosis, increased bone mineral density (adulthood); dental films for delayed tooth eruption.
- **Colonic manometry** has been used in at least one case to document decreased peristalsis underlying constipation.

**Genetic testing:**
- **Targeted *THRA* sequencing** (single-gene test) is the most direct confirmatory test once RTHα is clinically suspected given a compatible biochemical pattern. Available through the NIH Genetic Testing Registry (GTR) for *THRA* (NCBI GTR Gene ID 7067).
- **Exome or genome sequencing** has been the primary discovery route for nearly all reported cases (including the index Bochukova 2012 case and the R384C autism-cohort case), and remains appropriate given the nonspecific/attenuated biochemical phenotype that often does not trigger a targeted single-gene order.
- **Panel testing**: RTHα should be considered in broader "thyroid hormone resistance" or "congenital hypothyroidism" NGS panels, and in intellectual-disability/neurodevelopmental gene panels given the overlap with developmental-delay presentations.
- **Chromosomal microarray/karyotype/FISH**: Not relevant — RTHα is caused by point variants (missense/nonsense/frameshift), not copy-number or structural chromosomal changes; CMA/karyotype would be expected to be normal and is not a primary diagnostic tool for this condition.

**Clinical criteria:** No formal consensus diagnostic criteria (e.g., DSM/ICD-style) have been published; diagnosis rests on the combination of compatible phenotype + characteristic (if subtle) thyroid-hormone pattern + confirmatory *THRA* genetic testing.

**Differential diagnosis:** Primary congenital hypothyroidism, RTHβ (THRB-mediated generalized thyroid hormone resistance — distinguished by elevated TSH and high total T4/T3), other causes of short stature/developmental delay with skeletal dysplasia (e.g., skeletal dysplasia syndromes, other syndromic intellectual disability), and isolated chronic constipation of other etiology. Autism spectrum disorder of other genetic cause should also be considered, given the overlap with *THRA* variants found in ASD sequencing cohorts.

**Screening:** No newborn-screening program currently screens for RTHα (unlike primary congenital hypothyroidism, which is detected by TSH-based newborn screening — a modality that would **miss** RTHα because TSH is normal). Cascade family screening (biochemical + genetic) is recommended once a proband is identified, given documented intrafamilial transmission and variable expressivity (Nauwynck 2026 explicitly recommends "family-based genetic evaluation and cascade screening across lifespans").

---

## 11. Outcome/Prognosis

**Survival/mortality:** No excess mortality has been reported; RTHα is not described as life-limiting in published cases. No survival-rate or life-expectancy data exist (consistent with a non-lethal, chronic disorder), though systematic long-term outcome data are sparse given the small number of cases.

**Morbidity/function:**
- Chronic constipation, dyspraxia/motor incoordination, dysarthric speech, variable intellectual disability, and social/learning difficulties are the dominant sources of disease-related disability.
- Fertility appears **unaffected**: regular pregnancies have been reported in untreated affected females.
- One untreated adult attended university despite mild childhood developmental delays, illustrating the wide severity range.

**Disease course:**
- Complications include persistent anemia (often treatment-refractory), possible hepatic steatosis in adulthood, and — rarely — cardiomyopathy or pericardial effusion.
- Recovery/improvement potential with treatment is domain-specific (see Section 12): neurodevelopmental/behavioral and GI symptoms respond better than growth, cardiac, and hematologic parameters.

**Prognostic factors:**
- **Variant type** (frameshift/truncating → more severe) is the most consistently cited prognostic factor.
- **Age at treatment initiation** — earlier initiation of levothyroxine is associated with more distinguishable developmental benefit.
- Tissue-specific TRα expression and (speculative) cofactor/corepressor stoichiometry differences likely contribute to the unexplained intrafamilial variability.

**Prognostic biomarkers:** Elevated CK in childhood has been proposed as a biomarker correlating with disease activity/severity, though this is not validated as a formal prognostic tool; no molecular prognostic biomarker panel currently exists.

---

## 12. Treatment

**Pharmacotherapy — Levothyroxine (LT4):**
- LT4 has been "the first choice to date" and is the mainstay of treatment, typically dosed above what would be used for standard primary hypothyroidism to attempt to overcome TRα resistance in affected tissues, producing a biochemical pattern resembling central-hypothyroidism treatment (rise in FT3/FT4 with TSH suppression). NCIT term: NCIT:C15986 (Pharmacotherapy); therapeutic agent — CHEBI levothyroxine, or NCIT drug term for Levothyroxine.
- **Clinical benefits documented:** improvement in constipation (majority of cases), motor coordination, alertness, school performance, concentration, motivation, hypotonia, accelerated neuromotor development in children treated early, improved dyspraxia and social interaction in adults, reduction in elevated LDL cholesterol and muscle CK, and increases in IGF-1 and SHBG.
- **Limited/no response:** Anemia is largely **unresponsive** to LT4. Linear growth shows only limited benefit. Cardiac parameters (heart rate, contractility indices) and resting energy expenditure/muscle CK are comparatively poorly responsive relative to the degree of biochemical (FT3/FT4) correction achieved — i.e., tissues show **differential sensitivity** to exogenous hormone even at supraphysiologic FT3 exposure.
- **Safety concern:** Because TSH readily suppresses with LT4 while some TRα-dependent tissues remain resistant, patients can develop supraphysiologic FT3 levels — raising concern for "unwanted toxicities in normal TRβ-containing tissues" (e.g., theoretical cardiac/bone risk from chronic T3 excess in tissues where TRβ signaling is intact), a safety tension unique to treating a receptor-specific resistance syndrome with a non-selective hormone.
- **Liothyronine (T3):** used in at least one atypical case, associated with cardiac/metabolic response; generally considered a second-line or individualized option given the already-elevated endogenous FT3 in most patients.

**Pharmacogenomics:** No *THRA*-specific pharmacogenomic (drug-metabolism) data were identified; this is a receptor-resistance disorder rather than a drug-metabolism disorder, so conventional PharmGKB-style variant-drug interaction data are not applicable in the usual sense.

**Advanced therapeutics (experimental / preclinical):**
- **TRα1-selective thyromimetics** are proposed as the ideal future approach — compounds that would selectively activate residual normal TRα1 (or partially-functional mutant TRα1) in TRα-predominant tissues while sparing TRβ-dominant tissues from toxicity. None are yet in human trials for RTHα specifically; existing thyromimetic development (e.g., **sobetirome**, a TRβ-selective agonist developed for dyslipidemia/demyelinating disease, and **resmetirom**, approved for MASH) is **TRβ-selective** and thus not directly applicable/may be the wrong receptor target for RTHα.
- **Corepressor/HDAC-pathway targeting:** Because the core molecular lesion is failure to release the NCoR/SMRT-HDAC corepressor complex, genetic disruption of NCoR-TR interaction or pharmacologic HDAC inhibition has been tested in the murine Thra1^PV/+ model with **conflicting results across studies** — an earlier study (Subramanian et al., *Hum Mol Genet* 2014, PMID:24381310) reported the HDAC inhibitor **SAHA (vorinostat)** improved growth and bone development in Thra1^PV/+ mice, while a later, more detailed skeletal-phenotyping study (Freudenthal et al., *Thyroid* 2019, PMC6533791) found SAHA had "no beneficial or detrimental effects on bone structure, mineralization, or strength" and concluded SAHA treatment was "unlikely to improve the skeletal manifestations of RTHα" — an explicit model-divergence worth flagging in any curated entry (conflicting computational/animal-model evidence on the same pharmacologic strategy).
- **Gene therapy / RNA-based therapy / cell therapy / immunotherapy:** None reported or in development specific to RTHα (not relevant given the dominant-negative, gain-of-repressive-function mechanism, which would require allele-selective silencing rather than simple gene replacement — no such approach has been published for this condition).

**Surgical/interventional:** Not applicable — RTHα has no surgical treatment indication.

**Supportive/rehabilitative:**
- Physical/occupational/speech therapy for dyspraxia, gross/fine motor incoordination, and dysarthric speech (NCIT:C15302 Physical Therapy).
- Dietary/laxative management of chronic constipation.
- Educational support for learning disabilities.

**Experimental treatment registries:** A deep genotyping/phenotyping patient registry, **DEEPTYPE — "Register for Patients With Thyroid Hormone Resistance"** (ClinicalTrials.gov NCT06566066), is an active, ongoing registry study (estimated primary completion ~2029) intended to better characterize thyroid hormone resistance syndromes (including presumably RTHα) — full protocol detail (sponsor, eligibility specifics) could not be retrieved in this research pass and should be verified directly on ClinicalTrials.gov before citing as evidence.

**Treatment outcomes / adverse events:** No FAERS-level pharmacovigilance data exist specific to LT4 use in RTHα (too rare); adverse-event concerns are inferred mechanistically (supraphysiologic FT3 exposure risk) rather than empirically demonstrated in large cohorts.

**Treatment algorithm / personalized medicine:** No formal clinical practice guideline exists; management is individualized, typically involving endocrinology-led titration of LT4 (sometimes supplemented with T3) guided by clinical response (growth, constipation, developmental progress) more than by strict biochemical targets, given the blunted/variable biochemical-to-clinical correlation described above.

---

## 13. Prevention

Because RTHα is caused by de novo or inherited dominant germline variants with no known environmental trigger, classic primary prevention (risk-factor modification, vaccination) and public-health/environmental interventions are **not applicable**.

- **Secondary prevention (early detection):** Cascade genetic/biochemical screening of first-degree relatives of an identified proband is explicitly recommended in the literature (Nauwynck 2026) given documented familial transmission and variable expressivity — early identification in an asymptomatic/mildly symptomatic relative could in principle allow earlier initiation of supportive and thyroid-hormone interventions, though no formal screening protocol or outcome data for this strategy were identified.
- **Genetic counseling:** Recommended for identified families — autosomal dominant inheritance with a ~50% transmission risk to offspring of an affected parent, but with emphasis on the unpredictability of phenotypic severity (NCIT:C15240, Genetic Counseling).
- **Prenatal/preimplantation genetic testing:** Not specifically reported as used for RTHα in the literature reviewed, though it would be technically available once a familial pathogenic variant is known (standard for autosomal dominant single-gene disorders).
- **Newborn screening:** Current TSH-based newborn congenital-hypothyroidism screening programs will **not** detect RTHα (TSH is normal), which is explicitly identified in the literature as a major reason for underdiagnosis; no RTHα-specific newborn screening assay currently exists.
- **Prophylaxis:** Not applicable (no known preventable trigger).

---

## 14. Other Species / Natural Disease

**Taxonomy:** No naturally-occurring (spontaneous) RTHα has been reported in companion animals or wildlife (e.g., no OMIA entry for spontaneous *THRA* RTHα disease was identified in this pass). All non-human data derive from **engineered/induced genetic models** (see Section 15), not naturally occurring veterinary disease.

**Gene orthology:** *Thra* is highly conserved; mouse *Thra* (MGI:98743) and zebrafish *thraa*/*thrab* (duplicated paralogs, reflecting teleost genome duplication) are the principal orthologs exploited for modeling.

**Comparative biology:** The corepressor-release mechanism of TRα1 dominant-negative action is conserved from fish to mammals, supporting cross-species extrapolation of mechanistic findings, though the existence of a duplicated *thra* locus in zebrafish (thraa/thrab) is a structural divergence from the single-copy human/mouse gene that must be considered when interpreting zebrafish dominant-negative results (a single thra paralog's mutation may be partially compensated by the other).

**Zoonotic/transmission relevance:** Not applicable — this is a non-infectious, non-transmissible genetic disorder.

---

## 15. Model Organisms

**Mouse models:**
- **Thra1^PV/+ knock-in mouse** — the principal, most extensively characterized model. The PV mutation is a C-insertion causing a frameshift that disrupts helix 12 of the TRα1 ligand-binding domain, abolishing T3 binding and coactivator recruitment while preserving (indeed enhancing) corepressor binding — producing a potent dominant-negative receptor closely analogous to human disease-causing truncating variants.
  - **Phenotype recapitulation:** Near-normal standard thyroid function tests (mirroring the human diagnostic challenge), growth retardation, delayed bone development, reduced fat mass and liver size, abnormal (grossly abnormal) bone morphology with paradoxically preserved/high bone mass and normal bone strength in adult females, short stature, and short limbs — closely recapitulating the human skeletal phenotype.
  - **Erythroid phenotype:** Thra1^PV/+ mice show abnormal red blood cell indices similar to patients, with decreased expression of the erythroid master regulator **Gata-1** and its target genes in bone marrow, proposed as the mechanism by which mutant TRα1PV impairs erythropoiesis (mouse-model mechanistic claim — note this Gata1-repression mechanism was **not** corroborated in the human erythroid-progenitor study by van Gucht et al. 2017, which instead emphasized a proliferation/differentiation-balance defect without mention of GATA1 — a human/model divergence worth flagging when curating the erythropoiesis mechanism).
  - **Corepressor rescue experiment:** Introducing a mutation in NCoR1 that abrogates its interaction with TR, in the Thra1^PV/+ background, ameliorates growth and bone-development phenotypic abnormalities — direct genetic evidence for the corepressor-centered dominant-negative mechanism.
  - **Pharmacologic rescue (HDAC inhibition):** Conflicting results between two independent studies (Subramanian 2014 positive; Freudenthal 2019 negative for skeletal endpoints specifically) — see Section 12 for detail on this model divergence.
  - **Behavioral/CNS models:** Neuronal-specific expression of a dominant-negative TRα mutant alters mouse behavior (anxiety/depressive-like behaviors noted); relevant to the human neurocognitive/psychiatric phenotype but an extrapolation from a targeted-expression model rather than the global knock-in.
  - **Gonadal expression models:** Expression of dominant-negative TRα1 in Leydig and Sertoli cells demonstrated no additional reproductive defect compared with Sertoli-cell-only expression, suggesting TRα1 dysfunction in Leydig cells does not compound the male reproductive phenotype beyond the Sertoli-cell effect — consistent with the clinical observation that fertility is largely preserved in human RTHα.
- **Limitations of the mouse model:** No fully "amendable" (i.e., easily genetically/embryologically manipulable) mouse model exists for studying very early embryonic/developmental consequences of TRα1 dominant-negative mutations — this gap motivated development of the zebrafish models below.

**Zebrafish models:**
- CRISPR/Cas9-generated dominant-negative mutations in the duplicated zebrafish *thra* paralogs (**thraa**, **thrab**) allow study of THRA variant consequences during early embryonic development, which is experimentally inaccessible in mammalian models.
- Human *THRA* variants have been functionally tested in vivo by expression in zebrafish, demonstrating "in vivo functional consequences of human THRA variants" and validating zebrafish as a variant-classification/functional-assay platform.
- A specific **thraa mutant line carrying an 8-bp insertion** (truncating Thraa, impairing TH signaling) has been separately characterized for its effect on **cardiac regeneration**, finding that thraa loss-of-function **enhances** zebrafish heart regenerative capacity through metabolic/hypoxic regulation — an intriguing but mechanistically distinct line of investigation (cardiac regeneration biology) rather than a direct RTHα disease model, and should not be conflated with the human cardiac hypothyroid phenotype (bradycardia/reduced contractility) without further validation.
- THRA mutant zebrafish also show **heart defects**, directly supporting a TRα-dependent cardiac developmental role relevant to human cardiac findings.

**Cellular/in vitro models:**
- **Patient-derived human erythroid progenitor cells (HEPs)** cultured from peripheral blood of RTHα patients — used to directly demonstrate the human erythropoiesis defect (van Gucht 2017), representing a direct human cellular model rather than an animal surrogate.
- **Reporter-gene transactivation assays** (transfected cell lines expressing mutant TRα1/TRα2 constructs) — the standard functional-characterization approach for essentially every novel missense variant reported (e.g., A263V, N359Y, R384C functional studies cited above).

**Resources:** MGI (mouse *Thra* models), ZFIN (zebrafish *thraa*/*thrab* lines); no dedicated IMPC/KOMP conditional RTHα allele set was identified in this pass beyond the PV knock-in lineage.

---

## Summary of Key Evidence Gaps (for curation awareness)

- Precise per-variant gnomAD/ClinVar allele-frequency and ACMG classification detail was not individually verified for every reported variant in this pass and should be confirmed directly against ClinVar/gnomAD before binding specific variant records.
- The erythropoiesis mechanism shows a **model-organism/human divergence**: mouse data implicate Gata1 repression; the direct human progenitor-cell study instead emphasizes a proliferation/differentiation kinetic defect without invoking Gata1 — this is a genuine discrepancy, not merely a gap, and should be modeled as such (e.g., via `divergences`/`HUMAN_MODEL_MISMATCH` framing) rather than harmonized.
- The HDAC-inhibitor (SAHA) therapeutic strategy has **directly conflicting** preclinical results (positive in Subramanian 2014; negative on skeletal endpoints in Freudenthal 2019) and should not be curated as a settled positive therapeutic lead.
- Exact PMIDs for the JCRPE clinical-spectrum review and the *J Endocr Soc* untreated-adult cohort paper were not definitively captured during this search pass (PMC identifiers were obtained; PMID lookup should be completed at curation time).
- The DEEPTYPE registry (NCT06566066) protocol detail (explicit RTHα inclusion, sponsor) could not be retrieved and should be verified directly on ClinicalTrials.gov.

---

### Sources

- [A Mutation in the Thyroid Hormone Receptor Alpha Gene (Bochukova et al., NEJM 2012)](https://www.nejm.org/doi/full/10.1056/NEJMoa1110296) — PMID:22168587
- [The Clinical Spectrum of Resistance to Thyroid Hormone Alpha in Children and Adults (JCRPE)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7947725/)
- [Resistance to thyroid hormone due to defective thyroid receptor alpha (van Mullem et al.)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4559105/) — PMID:26303090
- [Clinical and Biochemical Characteristics of Untreated Adult Patients With Resistance to Thyroid Hormone Alpha (J Endocr Soc)](https://academic.oup.com/jes/article/7/8/bvad089/7219170)
- [Intrafamilial and Age-Dependent Variability in Resistance to Thyroid Hormone Alpha: A Case Report (Horm Res Paediatr, 2026)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13427315/) — PMID:42301959
- [Anemia in Patients With Resistance to Thyroid Hormone α (van Gucht et al., JCEM)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5587074/) — PMID:28911146
- [Thyroid Hormone Receptor α Mutation Causes a Severe and Thyroxine-Resistant Skeletal Dysplasia in Female Mice](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4138578/)
- [NCOR1 modulates erythroid disorders caused by mutations of thyroid hormone receptor α1](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5741760/)
- [Defective erythropoiesis caused by mutations of the thyroid hormone receptor α gene (PLOS Genetics)](https://journals.plos.org/plosgenetics/article?id=10.1371%2Fjournal.pgen.1006991)
- [Orphanet: Resistance to thyroid hormone due to a mutation in thyroid hormone receptor alpha](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=566231)
- [OMIM #614450 — Hypothyroidism, Congenital, Nongoitrous, 6; CHNG6](https://omim.org/entry/614450)
- [OMIM *190120 — Thyroid Hormone Receptor, Alpha-1; THRA](https://omim.org/entry/190120)
- [ClinVar: THRA c.1249C>T (p.Arg417Ter) / Congenital nongoitrous hypothyroidism 6](https://www.ncbi.nlm.nih.gov/clinvar/RCV000490316/)
- [ClinVar: THRA c.518A>G (p.Glu173Gly) / Congenital nongoitrous hypothyroidism 6](https://www.ncbi.nlm.nih.gov/clinvar/RCV001281098.1/)
- [Genetic and Pharmacological Targeting of Transcriptional Repression in Resistance to Thyroid Hormone Alpha (Freudenthal et al., Thyroid 2019)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6533791/)
- [A histone deacetylase inhibitor improves hypothyroidism caused by a TRα1 mutant (Subramanian et al., Hum Mol Genet 2014)](https://academic.oup.com/hmg/article-abstract/23/10/2651/614693) — PMID:24381310
- [Analysis and functional characterization of sequence variations in ligand binding domain of thyroid hormone receptors in autism spectrum disorder (ASD) patients (Kalikiri et al., Autism Research 2017)](https://onlinelibrary.wiley.com/doi/10.1002/aur.1838) — PMID:28856816
- [Generation of Novel Genetic Models to Dissect Resistance to Thyroid Hormone Receptor α in Zebrafish](https://pubmed.ncbi.nlm.nih.gov/31952464/)
- [In vivo Functional Consequences of Human THRA Variants Expressed in the Zebrafish](https://pubmed.ncbi.nlm.nih.gov/27809680/)
- [Thyroid Hormone Receptor α Mutations Cause Heart Defects in Zebrafish](https://pubmed.ncbi.nlm.nih.gov/32762296/)
- [Knockout of thyroid hormone receptor alpha a (thraa) enhances cardiac regeneration in zebrafish](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12265366/)
- [THRA Gene — GeneCards](https://www.genecards.org/cgi-bin/carddisp.pl?gene=THRA)
- [Thyroid Hormone Resistance due to a Novel De Novo Mutation in Thyroid Hormone Receptor Alpha: First Case Report from the Middle East and North Africa](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7897355/)
- [Register for Patients With Thyroid Hormone Resistance (DEEPTYPE, NCT06566066)](https://clinicaltrials.gov/study/NCT06566066)
- [GARD: Resistance to thyroid hormone due to a mutation in thyroid hormone receptor alpha](https://rarediseases.info.nih.gov/diseases/22275/resistance-to-thyroid-hormone-due-to-a-mutation-in-thyroid-hormone-receptor-alpha)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 20 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 20 |
| On topic | 18 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 48 |
| Resolved | 44 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 41 |
| Terms named correctly | 32 |
| Terms named as a **different** term | 6 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0010701` (1 mention) - the report calls it "Skin tags"; HP calls it **Abnormal circulating immunoglobulin concentration**
- `HP:0001923` (1 mention) - the report calls it "Normocytic anemia"; HP calls it **Reticulocytosis**
- `GO:0004887` (3 mentions) - the report calls it "thyroid hormone receptor activity"; GO calls it **GO_0004887**
- `GO:0007416` (1 mention) - the report calls it "synapse assembly, for GABAergic interneuron defect"; GO calls it **synapse assembly**
- `CL:0000216` (1 mention) - the report calls it "Sertoli cell — relevant to gonadal expression studies"; CL calls it **Sertoli cell**
- `UBERON:0001968` (1 mention) - the report calls it "skeletal system"; UBERON calls it **semen**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0008977` (1 mention) - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0004887` (GO_0004887) (3 mentions) - replaced by `GO:0004879`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0006355` (2 mentions) - the report calls it "regulation of DNA-templated transcription", "regulation of transcription"; GO calls it **regulation of DNA-templated transcription**
- `CL:0000617` (1 mention) - the report calls it "GABAergic interneuron"; CL calls it **GABAergic neuron**
- `CL:0000187` (1 mention) - the report calls it "myocyte"; CL calls it **muscle cell**, and lists "myocyte" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0006355` - called "regulation of DNA-templated transcription", "regulation of transcription"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`.