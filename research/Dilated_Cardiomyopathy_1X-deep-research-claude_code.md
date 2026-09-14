---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-04T02:42:05.478175'
end_time: '2026-09-04T02:46:42.496123'
duration_seconds: 277.02
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Dilated Cardiomyopathy 1X
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
  web_search_requests: 16
  num_turns: 20
  total_cost_usd: 1.230977
  session_id: fab9582c-86c5-587f-8c13-07e30530b023
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 21
reference_validation:
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 2
  relevance_assessed: 8
  on_topic: 5
  validator_version: 0.2.1
term_validation:
  total_terms: 25
  verified: 21
  not_found: 0
  obsolete: 1
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 14
  labels_matching: 3
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: MONDO:0012704
    reported_labels:
    - MONDO
    - Dilated cardiomyopathy 1X
    ontology_label: dilated cardiomyopathy 1X
  - term_id: HP:0001635
    reported_labels:
    - Dilated cardiomyopathy
    - Dilated cardiomyopathy phenotype
    ontology_label: Congestive heart failure
  - term_id: HP:0001639
    reported_labels:
    - "Hypertrophic cardiomyopathy \u2014 not applicable here but relevant to FKTN\
      \ mutational screens that included HCM cohorts"
    ontology_label: Hypertrophic cardiomyopathy
  - term_id: HP:0001636
    reported_labels:
    - Tachycardia
    ontology_label: Tetralogy of Fallot
  labels_variant: 7
  obsolete_terms:
  - term_id: GO:0006486
    ontology_label: obsolete protein glycosylation
    replaced_by: GO:0009101
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
- **Disease Name:** Dilated Cardiomyopathy 1X
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Dilated Cardiomyopathy 1X** covering all of the
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

I now have enough primary-source material to compile the full report.

I have sufficient primary-source material now. Here is the comprehensive research report.

# Dilated Cardiomyopathy 1X (CMD1X): Comprehensive Research Report

## 1. Disease Information

### Overview
Dilated Cardiomyopathy 1X (CMD1X) is a rare, genetically defined form of dilated cardiomyopathy (DCM) caused by biallelic (typically compound heterozygous, occasionally homozygous) pathogenic variants in the **FKTN** gene (fukutin), which sits within the broader **secondary alpha-dystroglycanopathy** spectrum. It is clinically distinctive because it presents with **prominent, sometimes isolated cardiac muscle involvement with minimal or absent limb-girdle skeletal myopathy and normal intelligence** — a striking dissociation from the severe, multisystem phenotype (brain malformation, eye anomalies, profound muscle weakness) classically associated with *FKTN* mutations in Fukuyama congenital muscular dystrophy (FCMD). The original description characterized six patients from four families with "dilated cardiomyopathy with no or minimal limb girdle muscle involvement" (Murakami et al., *Annals of Neurology* 2006;60(5):597-602, PMID:17036286).

**Important nomenclature note:** Despite the "X" suffix, CMD1X is **not X-linked**. OMIM's dilated cardiomyopathy series uses sequential letters after "CMD1" (autosomal dominant/undetermined series) — CMD1A through CMD1BB and beyond — purely as an enumeration; "1X" is simply the 24th letter reached in that numbering scheme, not a locus designation. This is a genuine, well-documented curator pitfall: FKTN is autosomal (chromosome 9q31.2), and inheritance is **autosomal recessive**. (True X-linked dilated cardiomyopathy caused by *DMD*/dystrophin mutations is a *separate* entity, OMIM designated CMD3B/#302045, which should not be conflated with CMD1X.)

### Key Identifiers
| Database | ID |
|---|---|
| OMIM (phenotype) | **#611615** — CARDIOMYOPATHY, DILATED, 1X; CMD1X |
| OMIM (gene) | *607440 — FUKUTIN; FKTN |
| MONDO | MONDO:0012704 |
| Orphanet | ORPHA:154 (subsumed under the alpha-dystroglycanopathy/Fukuyama spectrum entries) |
| MedGen | C1969024 |
| Gene | FKTN, HGNC:3622, chromosome 9q31.2 |
| Inheritance | Autosomal recessive |
| Related allelic disorders (same gene, MDDG spectrum) | MDDGA4 (severe, congenital, brain/eye anomalies — includes classic Fukuyama CMD, Walker-Warburg syndrome, muscle-eye-brain disease; OMIM #253800), MDDGB4 (intermediate, congenital, no brain/eye involvement), MDDGC4/LGMD2M/LGMDR13 (limb-girdle form, OMIM #611588) |

Sources: [OMIM #611615](https://www.omim.org/entry/611615) (via search), [NCBI GTR C1969024](https://www.ncbi.nlm.nih.gov/gtr/conditions/C1969024/), [OMIM #253800](https://omim.org/entry/253800), [OMIM #611588](https://omim.org/entry/611588)

### Synonyms
- CMD1X
- Cardiomyopathy, dilated, 1X
- FKTN-related dilated cardiomyopathy
- Fukutin-associated dilated cardiomyopathy with minimal muscle weakness

### Evidence basis
The condition is characterized almost entirely from **aggregated case-series and case-report literature** (not large cohort/EHR registries) — the founding series (n=6, 4 families), subsequent single-patient reports from Europe (Italian, German cases), and a recent JACC case series pairing FKTN with LMNA-associated DCM. This is consistent with its rarity: it is an "orphan" subtype even within the rare-disease space of genetic DCM.

---

## 2. Etiology

### Disease Causal Factors
CMD1X is caused by **biallelic loss-of-function/hypomorphic variants in FKTN**, encoding fukutin, a Golgi-resident ribitol-5-phosphate transferase required for functional glycosylation of alpha-dystroglycan (α-DG). The mechanism is **genetic/enzymatic** (a glycosylation defect), not environmental or infectious in origin, though pregnancy and hemodynamic stress can precipitate decompensation in an already-compromised heart (see below).

### Genetic Risk Factors
- **Causal variants**: Point mutations (missense, nonsense) and small indels in *FKTN*, typically as **compound heterozygotes**, with the cardiac-restricted phenotype associated with **hypomorphic** (partial function-retaining) alleles rather than the severe null combinations seen in Fukuyama CMD or Walker-Warburg syndrome.
  - The originally reported German/European compound heterozygote carried **p.Ser299Arg** and **p.Asn442Ser** (PMC9223741, MDPI *Int J Mol Sci* 2022).
  - A separate Chinese case reported a **de novo p.Asp3368Gly**-type dystrophin variant in a different gene context (this is a DMD-XLDC case, illustrating how the two entities are frequently co-indexed in literature searches and must be disambiguated).
  - The **Japanese founder allele** — a ~3-kb SVA-type retrotransposal insertion in the 3′-UTR of *FKTN* — is the classic severe Fukuyama-associated allele (present in ~87% of FCMD alleles in Japan); CMD1X patients typically carry this founder allele **in trans with a second, milder point mutation**, producing a "compound heterozygote with one hypomorphic and one severe allele" genotype-phenotype pattern that under-expresses the severe brain/eye phenotype while sparing enough fukutin activity to avoid overt limb-girdle myopathy but not enough to protect the heart.
  - A **deep-intronic variant of FKTN** has also been reported as a prevalent point-mutation-class allele in Japanese FCMD/dystroglycanopathy patients (*J Hum Genet* 2017).
- **Susceptibility/modifier genes**: None specifically established for CMD1X; however, the JACC case-series literature (2026) documents co-occurring or phenocopy overlap with **LMNA**-associated DCM/LGMD in the differential for "cardiomyopathy-first" presentations later found to have limb-girdle disease.
- **Founder effects**: Strong founder effect in the Japanese population via the FCMD retrotransposal insertion (age estimated at ~102 generations by haplotype analysis); most published CMD1X cases are of Japanese ancestry, though European cases have now been reported.

### Environmental / Non-genetic Risk Factors
- **Pregnancy** is a well-documented precipitant of clinical decompensation in patients with pre-existing CMD1X, due to the hemodynamic volume/afterload burden of gestation (see Section 8/Case report below) — this is a secondary exacerbating factor, not a causal one.
- No toxin, occupational, infectious, or lifestyle causal factor has been established; standard DCM risk-modifying exposures (alcohol, cardiotoxic chemotherapy) are not part of the CMD1X literature and would represent phenocopies/comorbid triggers rather than part of the primary mechanism.

### Protective Factors
None specifically reported for FKTN-related disease. General DCM disease-modifying factors (guideline-directed medical therapy adherence) apply once diagnosed but are not preventive at the genetic level.

### Gene-Environment Interactions
The clearest documented interaction is the **cardiac hemodynamic stress of pregnancy** unmasking or worsening subclinical/mild CMD1X (see pregnancy case report, PMC4630494), analogous to peripartum cardiomyopathy but genetically determined rather than idiopathic.

---

## 3. Phenotypes

### Cardiac phenotype (primary)
- **Dilated cardiomyopathy** — left ventricular dilatation with hypokinesis/reduced ejection fraction (HP:0001635 Dilated cardiomyopathy)
  - Reported LVEF as low as 47% at presentation in the pregnancy case, with LV diastolic dimension (LVDd) of 53 mm (PMC4630494)
  - Progressive over time in most cases; two originally reported patients died (age 12, rapid progression) or required cardiac transplantation (age 18)
- **Congestive heart failure / reduced NYHA functional class** (HP:0001635 / HP:0001642 Reduced left ventricular ejection fraction) — NYHA class II reported at baseline in the pregnancy case, worsening with hemodynamic stress
- **Arrhythmia** (HP:0011675 Arrhythmia) — a general dystroglycanopathy-cardiac feature, though the primary literature emphasizes pump failure over primary electrical disease
- **Cardiomegaly** (HP:0001640)

### Skeletal muscle phenotype (minimal/mild — defining feature distinguishing CMD1X from the rest of the FKTN spectrum)
- **Mild or absent limb-girdle muscle weakness** (HP:0003749 Limb-girdle muscle weakness) — present in some but not all patients; several index patients had *no* clinically detectable weakness
- **Elevated serum creatine kinase (CK)** (HP:0003236 Elevated CK) — a laboratory abnormality frequently present even in the absence of overt weakness; broader FKTN-dystroglycanopathy literature documents serial CK from 298–11,900 U/L
- **Minimal dystrophic changes on skeletal muscle biopsy** — histologically near-normal or minimally dystrophic muscle despite biochemically abnormal (hypoglycosylated) α-dystroglycan and reduced laminin-binding activity (Murakami et al. 2006)

### CNS/cognitive phenotype
- **Normal intelligence** (explicitly documented as a distinguishing negative finding — contrasts with the mental retardation/brain malformation of classic FCMD)
- **No history of seizures** (explicit negative finding in the founding case series)

### Phenotype characteristics
- **Age of onset**: Variable — pediatric/adolescent onset (one fatal case at age 12) through young adulthood (transplant at 18; a 25-year-old diagnosed at 19 in the pregnancy case; a JACC-reported 22-year-old woman with biallelic FKTN requiring transplant)
- **Severity**: Highly variable, from indolent/subclinical disease unmasked by pregnancy to rapidly progressive fatal disease in childhood
- **Progression**: Generally progressive; some patients stable for years before decompensation under physiologic stress (pregnancy, illness)
- **Frequency data**: Not established at a population level — this is an ultra-rare entity known chiefly from case reports/small series, so phenotype frequencies (e.g., "X% have LGMD features") are not quantifiable with confidence; qualitative descriptors ("mildest," "no or minimal") are used in the literature rather than percentages.

### Quality of life impact
Not formally studied with QoL instruments (EQ-5D/SF-36) in the literature identified; qualitatively, the disease burden is dominated by heart-failure symptoms and, for a subset, progressive limb-girdle weakness postpartum (one patient reported "persistent worsening of muscular weakness" after delivery, PMC4630494).

Suggested HP terms: HP:0001635 (Dilated cardiomyopathy), HP:0001644 (Dilated cardiomyopathy — note overlapping codes across HPO releases), HP:0003749 (Limb-girdle muscle weakness), HP:0003236 (Elevated CK), HP:0001639 (Hypertrophic cardiomyopathy — not applicable here but relevant to FKTN mutational screens that included HCM cohorts), HP:0001636 (Tachycardia), HP:0011675 (Arrhythmia).

---

## 4. Genetic/Molecular Information

### Causal Gene
- **FKTN** (fukutin), HGNC:3622, chromosome **9q31.2**, OMIM gene entry **\*607440**
- Encodes a 461-amino-acid **type II transmembrane, Golgi-resident enzyme**

### Pathogenic Variants
- **Variant types**: Missense (e.g., p.Ser299Arg, p.Asn442Ser), the Japanese founder 3-kb retrotransposal (SVA-type) insertion in the 3′-UTR, deep-intronic variants affecting splicing, and other point mutations/small indels — heterogeneous across the allelic series
- **Classification**: Reported ClinVar submissions for "Dilated cardiomyopathy 1X" include multiple FKTN variants (e.g., c.*954T>A, c.*2902C>T, c.1297A>G [p.Thr433Ala], c.1106del [p.Phe369fs], and the retrotransposal insertion c.*4392_*4393ins) — see [ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/) records cross-referenced above
- **Zygosity**: Compound heterozygous in essentially all reported CMD1X cases (biallelic, two different variants) — consistent with autosomal recessive inheritance and the genotype-phenotype model of "one severe + one hypomorphic allele → cardiac-predominant phenotype"
- **Functional consequence**: **Loss/reduction of function** — reduced ribitol-5-phosphate transferase activity, causing **hypoglycosylation of α-dystroglycan** and **reduced laminin-binding capacity**, demonstrable by Western blot with N-terminal dystrophin/glycosylated-α-DG-specific antibodies (e.g., IIH6) on muscle biopsy
- **Somatic vs. germline**: Germline (Mendelian, autosomal recessive) — not a somatic/acquired disease

### Modifier Genes
None formally established for CMD1X specifically; the 2026 JACC case series highlights that **LMNA** variants can produce an overlapping "DCM-first, LGMD-later" clinical trajectory, useful as a differential-diagnosis consideration rather than a true modifier of FKTN penetrance.

### Molecular Pathway Context
FKTN operates in the **CDP-ribitol / matriglycan biosynthesis pathway**:
- **ISPD** (isoprenoid synthase domain-containing protein) synthesizes CDP-ribitol
- **FKTN** and **FKRP** (fukutin-related protein) sequentially transfer ribitol-5-phosphate (RboP) from CDP-ribitol onto the core M3 O-mannosyl glycan of α-dystroglycan, generating a **tandem ribitol-phosphate unit** essential for subsequent matriglycan polymerization by LARGE1
- This tandem RboP structure is required for α-DG to bind laminin-α2, agrin, and perlecan in the extracellular matrix
- FKTN and FKRP are the only mammalian proteins bearing a bacterial-type **LicD domain** used for CDP-conjugate substrate chemistry

Primary sources: [ISPD produces CDP-ribitol used by FKTN and FKRP (Nat Commun 2016, PMID:27194101)](https://www.nature.com/articles/ncomms11534)

### Chromosomal Abnormalities
Not applicable — CMD1X is caused by sequence-level variants/indels/retrotransposal insertion, not large structural/chromosomal rearrangements.

### Epigenetic Information
No disease-specific epigenetic (DNA methylation/histone) literature was identified for CMD1X; not a known mechanism in this disorder.

---

## 5. Environmental Information

- **Environmental factors**: None causally implicated; this is a monogenic, autosomal recessive disorder.
- **Lifestyle factors**: Not established as causal; standard cardiomyopathy comorbidity considerations (deconditioning, volume status) apply symptomatically but are not disease-causing.
- **Infectious agents**: Not implicated.
- **Key modifiable physiologic stressor**: **Pregnancy**, which is well-documented to precipitate/worsen decompensation (see Section 8) — this should be modeled as a triggering/exacerbating physiologic exposure rather than a classic toxin/infection.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain
1. **Biallelic hypomorphic *FKTN* variants** (typically compound heterozygous — one severe allele, e.g., the retrotransposal insertion, in trans with a milder missense allele) → **reduces, but does not abolish, fukutin ribitol-5-phosphate transferase activity** in the Golgi apparatus.
2. Reduced fukutin activity → **impaired sequential transfer of ribitol-5-phosphate from CDP-ribitol (synthesized by ISPD) onto the core M3 O-mannosyl glycan of α-dystroglycan**, in cooperation with FKRP → **incomplete/aberrant tandem ribitol-phosphate glycan structure** on α-dystroglycan. *This step is directly demonstrated biochemically* (Western blot with glycoepitope-specific antibodies such as IIH6 shows reduced/absent signal; PMID:27194101, PMC9223741).
3. Aberrant α-dystroglycan glycosylation → **loss of downstream matriglycan polymerization and reduced α-dystroglycan binding affinity for laminin-α2, agrin, and perlecan** in the extracellular matrix → **weakened linkage between the sarcolemmal dystrophin-glycoprotein complex (DGC) and the basement membrane** in cardiomyocytes and (to a lesser, tissue-dependent extent) skeletal myofibers. *Demonstrated in patient muscle biopsy and cardiac Fktn-knockout mouse models* (Murakami et al. 2006; Kanagawa/Beedle-type models reviewed via Nat Commun 2019, PMID:31848331).
4. Weakened DGC-ECM linkage in the myocardium → **two convergent, partly dissociable downstream consequences**, based on the cardiac-specific *Fktn* mouse knockout literature:
   - **Branch A (membrane fragility route)**: reduced α-DG glycosylation and DGC protein content at the sarcolemma at all developmental stages → *increased susceptibility to contraction-induced sarcolemmal microdamage*, analogous to the mechanism in dystrophinopathy-associated cardiomyopathy — though the mouse data indicate this alone is **not sufficient** to cause overt dysfunction in early life, implying an inferred, only partially demonstrated causal step in humans.
   - **Branch B (signaling/hypertrophic-stress route, better supported mechanistically)**: during young adulthood, Fktn-deficient cardiomyocytes show **increased vulnerability to pathological hypertrophic stress**, with **downregulation of Akt signaling and disruption of the MEF2–histone deacetylase (HDAC) transcriptional axis** → maladaptive hypertrophic/remodeling transcriptional program. Acute *Fktn* elimination in adult mouse hearts produces **severe contractile dysfunction, disordered Golgi-microtubule networks, and accelerated mortality**, indicating fukutin also has an ECM-glycosylation-independent role in myocyte structural/organellar integrity (Nat Commun 2019, PMID:31848331 — model-organism evidence; translational fidelity to the milder, chronic human CMD1X phenotype is not fully established and represents a genuine human-model gap).
5. Branch A + Branch B converge on **progressive cardiomyocyte dysfunction, myocardial fibrotic remodeling, and chamber dilatation** → clinical **dilated cardiomyopathy with reduced ejection fraction**, which in turn leads to → **congestive heart failure symptoms, arrhythmia risk, and (in severe cases) death or need for cardiac transplantation**.
6. In parallel, but largely **uncoupled** from the cardiac trajectory in CMD1X specifically (this dissociation is the entry's defining biological puzzle), the same glycosylation defect in skeletal muscle produces only **minimal histological/dystrophic change**, despite biochemically demonstrable hypoglycosylation and reduced laminin-binding — i.e., skeletal muscle appears more tolerant of the same molecular lesion than cardiac muscle in this genotype range, an unresolved cardiac-vs-skeletal-muscle tissue-vulnerability question in the literature.
7. **Pregnancy-associated hemodynamic load** (increased circulating volume, afterload/preload shifts) acts as an **exacerbating step superimposed on the underlying structural cardiomyopathy** (step 5) → acute-on-chronic decompensation, generally reversible postpartum for the cardiac component but sometimes associated with a step-change worsening of the skeletal myopathy (per the pregnancy case report), suggesting the hemodynamic stress event may also unmask/accelerate the peripheral muscle phenotype — a mechanistically unexplained observation, not yet causally dissected.

### Molecular Pathways
CDP-ribitol/matriglycan biosynthesis pathway (ISPD → FKTN/FKRP → LARGE1) — see Section 4. Suggested GO terms: **GO:0035269** (protein O-linked mannosylation), a fukutin-specific ribitol-phosphate transferase activity term, and **GO:0007009** (plasma membrane organization) for downstream DGC effects.

### Cellular Processes
- Golgi glycosylation/protein trafficking dysfunction
- Maladaptive cardiomyocyte hypertrophic signaling (Akt/MEF2-HDAC axis downregulation)
- Sarcolemmal membrane fragility (secondary/contributory)

### Protein Dysfunction
Loss-of-function/hypomorphic enzymatic activity of fukutin (a Golgi ribitol-5-phosphate transferase) — not a classic misfolding/aggregation disease.

### Tissue Damage Mechanisms
Myocardial remodeling/fibrosis secondary to chronic contractile dysfunction and impaired ECM-cytoskeletal linkage; minimal comparable damage in skeletal muscle in the CMD1X-specific genotype range.

### Cell types and biological processes involved
Suggested CL terms: **CL:0000746** (cardiac muscle myocyte), **CL:0000188** (skeletal muscle myoblast/fiber, for the milder, secondary skeletal involvement). Suggested GO: protein glycosylation (GO:0006486), O-mannosylation, and hypertrophic-signaling-related terms (PI3K-Akt signaling, GO:0043491).

### Molecular Profiling / Advanced Technologies
No transcriptomic, proteomic, or single-cell datasets specific to human CMD1X myocardium were identified in this search; the mechanistic evidence base is predominantly (a) patient muscle-biopsy immunohistochemistry/Western blot and (b) mouse cardiac-specific *Fktn* knockout models (constitutive and inducible/acute), which is a **model-organism evidence gap** worth flagging for a `HUMAN_MODEL_MISMATCH`-type discussion: the mouse models capture the glycosylation defect and downstream Akt/MEF2 signaling faithfully but do not fully explain why human skeletal muscle is comparatively spared in the CMD1X allele combination.

---

## 7. Anatomical Structures Affected

### Organ level
- **Primary organ**: Heart (myocardium) — left ventricle predominantly, per echocardiographic dilatation/hypokinesis pattern
- **Secondary/minor organ involvement**: Skeletal muscle (limb-girdle distribution), minimally
- **Body systems**: Cardiovascular system (primary); musculoskeletal system (secondary, mild)
- **Not involved**: Central nervous system (explicitly normal intelligence, no seizures) — distinguishing CMD1X from the rest of the FKTN/MDDG spectrum

Suggested UBERON terms: **UBERON:0000948** (heart), **UBERON:0002082** (cardiac ventricle), **UBERON:0001630** (skeletal muscle tissue, limb-girdle group).

### Tissue and cell level
- Cardiomyocytes (CL:0000746) — primary affected population
- Skeletal myofibers — secondarily, mildly affected
- Extracellular matrix (basement membrane) surrounding both tissue types — site of the functional lesion (laminin-binding failure)

### Subcellular level
- **Golgi apparatus** — site of fukutin's enzymatic activity (GO Cellular Component: GO:0005794, Golgi apparatus)
- **Sarcolemma** — site of the dystrophin-glycoprotein complex (DGC) whose ECM linkage is compromised
- **Microtubule/Golgi network** — disrupted in the acute mouse knockout model

### Localization
Bilateral, diffuse left ventricular involvement (not focal/segmental) per the echocardiographic description ("diffused left ventricular hypokinesis").

---

## 8. Temporal Development

### Onset
- **Age of onset**: Variable — pediatric (fatal case, age 12) through young adulthood (diagnosis at 19, transplant at 18 or 22); no neonatal/congenital cardiac presentation reported for the CMD1X subtype specifically (distinguishing it from the congenital MDDGA4/B4 forms)
- **Onset pattern**: Insidious/subclinical in several reported cases, only unmasked by a physiologic stressor (pregnancy)

### Progression
- **Disease course**: Generally progressive dilated cardiomyopathy; rate is variable — from rapid/fatal in childhood to an indolent course persisting into adulthood
- **Stages**: Not formally staged in a disease-specific system; general heart-failure staging (NYHA class) applies — NYHA II documented at baseline in the pregnancy case, with worsening under hemodynamic load
- **Duration**: Chronic, lifelong once manifest; can require heart transplantation

### Patterns
- **Reversibility**: The pregnancy case demonstrated that pregnancy-associated cardiac decompensation (EF drop, LV dilatation) **returned to baseline (pre-pregnancy) status approximately one month postpartum**, indicating the cardiac component of an acute decompensation can be reversible even though the underlying cardiomyopathy is not cured; however, the **skeletal myopathy** in the same patient showed **persistent worsening** postpartum, suggesting differential reversibility between the cardiac and skeletal muscle compartments.
- **Critical period**: Pregnancy is identified as a specific window of vulnerability requiring closer surveillance in known/suspected CMD1X patients.

---

## 9. Inheritance and Population

### Epidemiology
- **Prevalence/incidence**: Not established at a population level — CMD1X is known from isolated case reports and one small case series (6 patients/4 families in the founding report); it should be regarded as an **ultra-rare** subtype within the broader genetic-DCM landscape (general nonischemic DCM prevalence is estimated at roughly 1/2500, for context, but FKTN-attributable cases are a vanishingly small fraction of that).

### Inheritance Pattern
- **Autosomal recessive** (biallelic FKTN variants required) — not X-linked despite the "1X" name (see Section 1 nomenclature note).
- **Penetrance**: Appears high for the cardiac phenotype once the specific hypomorphic compound-heterozygous genotype is present, though formal penetrance estimates are not available given the small case numbers.
- **Expressivity**: Highly variable — ranging from asymptomatic-until-pregnancy to fatal childhood disease — consistent with the allelic-severity model (specific combination of the two inherited alleles determines phenotype across the whole FKTN/MDDG spectrum).
- **Genetic anticipation**: Not reported/applicable (not a repeat-expansion disorder in the classic sense, though the founder allele is itself a large insertion).
- **Founder effects**: Strong — the ~3-kb SVA-type retrotransposal insertion in the FKTN 3′-UTR is a well-characterized Japanese founder mutation (present in ~87% of FCMD alleles; estimated age ~102 generations), and most published CMD1X patients are of Japanese descent, carrying this founder allele in trans with a second, milder FKTN variant. European cases (German, Italian) have since been reported with different, non-founder compound-heterozygous genotypes.
- **Carrier frequency**: The FCMD founder allele carrier frequency in the Japanese population has been estimated in the range consistent with FCMD being the second most common muscular dystrophy in Japan (~1/90 carrier frequency has been cited historically for the founder insertion in the general Japanese population in FCMD literature, though this figure was not independently re-verified in this search and should be confirmed against a primary source before use in curation).
- **Consanguinity**: Not specifically emphasized in the CMD1X case literature (compound heterozygosity, not homozygosity, is the predominant genotype reported).

### Population Demographics
- **Affected populations**: Predominantly Japanese (founder-allele-driven), with additional cases now reported in European (German, Italian) patients with non-founder genotypes — indicating the disorder is not population-restricted, only enriched by founder effect in Japan.
- **Sex ratio**: No specific male:female skew has been established (consistent with autosomal recessive inheritance); both male and female patients are reported, including the female pregnancy case.
- **Age distribution**: Concentrated in childhood-through-young-adult presentation in the literature identified.

---

## 10. Diagnostics

### Clinical Tests
- **Echocardiography**: Diagnostic mainstay for demonstrating LV dilatation, hypokinesis, and reduced EF (LVEF 47%, LVDd 53 mm reported in the pregnancy case)
- **Serum creatine kinase (CK)**: Frequently elevated even without overt weakness (broader FKTN-dystroglycanopathy literature: 298–11,900 U/L range); an important diagnostic clue prompting genetic workup in a patient presenting with "DCM plus unexplained CK elevation"
- **Muscle biopsy**: Histopathology often shows only minimal dystrophic change in CMD1X (contrasting with more severe dystrophic histology in classic FCMD/LGMD2M), but **immunohistochemistry/Western blot for glycosylated α-dystroglycan** (e.g., using the IIH6 monoclonal antibody) reveals reduced/aberrant glycosylation and reduced laminin-binding — this is the key confirmatory functional assay
- **Cardiac biopsy**: Abnormalities of cardiac dystrophin-associated glycoprotein complex demonstrable by Western blot with N-terminal antibodies in some reports, while skeletal muscle dystrophin/DGC remains comparatively preserved

### Genetic Testing
- **Recommended approach**: Targeted *FKTN* sequencing or a dystroglycanopathy/cardiomyopathy gene panel, given the clinical suspicion is usually raised by unexplained DCM plus mild CK elevation
- **Whole exome/genome sequencing**: Appropriate when panel testing is non-diagnostic, given phenotypic overlap with other genetic DCM genes (LMNA, TTN, DMD, RPL3L, TNNC1, etc., all of which appear in the differential-diagnosis literature retrieved)
- **Japanese founder mutation testing**: A specific, targeted clinical test exists for the FKTN 3′-UTR retrotransposal insertion (offered commercially, e.g., PreventionGenetics' "Fukuyama Congenital Muscular Dystrophy via the FKTN Japanese Founder Mutation Test"), relevant when one allele is suspected to be the founder insertion
- **Deep-intronic variant testing**: A specific deep-intronic FKTN variant has been reported as a prevalent point-mutation-class cause of FKTN-related disease in Japan and may require specialized splicing-variant assays not captured by standard exome sequencing

### Clinical Criteria
- No CMD1X-specific consensus diagnostic criteria exist; diagnosis rests on the combination of (1) DCM phenotype, (2) absent/minimal overt myopathy, (3) elevated CK, (4) biallelic FKTN variants, and (5) confirmatory α-DG glycosylation studies on muscle biopsy where available.
- **Differential diagnosis**: Other genetic DCM causes with occult skeletal myopathy — notably **LMNA**-associated DCM/LGMD (explicitly discussed as a mimicking/co-occurring entity in the 2026 JACC case series), X-linked dystrophinopathy-associated DCM (DMD gene — the entity often confused by name with CMD1X), TTN-truncating variant DCM, RPL3L-associated DCM, TNNC1-associated familial DCM, and idiopathic/peripartum cardiomyopathy (particularly relevant given the pregnancy-associated presentation).

### Screening
No population or newborn screening program specific to CMD1X was identified; case-finding is reactive (via unexplained DCM + CK elevation workup) rather than proactive, given the extreme rarity.

---

## 11. Outcome/Prognosis

- **Survival/mortality**: Highly variable — the founding case series documented one death at age 12 from rapidly progressive disease and one heart transplant at age 18; a more recent case series (JACC 2026) documents additional transplant cases (including a 22-year-old woman with biallelic FKTN variants). No population-level survival statistics (5-/10-year survival) exist given the rarity.
- **Morbidity**: Dominated by heart-failure-related functional limitation; a subset of patients develop progressive limb-girdle weakness over time, sometimes accelerated by pregnancy.
- **Complications**: Progression to end-stage heart failure requiring transplantation is a recurring theme across the literature; arrhythmia risk is presumed (general DCM risk) but not specifically quantified for this subtype.
- **Recovery potential**: The cardiac component can show substantial reversibility after an acute precipitant (pregnancy) resolves, but the underlying cardiomyopathy and any skeletal myopathy are not curable and tend to persist/progress long-term.
- **Prognostic factors**: Genotype severity (specific allele combination), presence/degree of skeletal muscle involvement, and physiologic stressors (pregnancy, intercurrent illness) appear to modulate short-term trajectory, though systematic prognostic-factor analysis has not been performed given small case numbers.

---

## 12. Treatment

No CMD1X-specific pharmacotherapy exists; management follows **standard guideline-directed medical therapy (GDMT) for heart failure with reduced ejection fraction**, as used for genetic and non-genetic DCM broadly, per 2022 ACC/AHA/HFSA and 2023 ESC cardiomyopathy guidelines:

### Pharmacotherapy
- **ACE inhibitors / ARBs / ARNI (sacubitril-valsartan)** — NCIT:C15986 (Pharmacotherapy); sacubitril-valsartan shown superior to enalapril for reducing cardiovascular mortality/HF hospitalization in HFrEF generally
- **Beta-blockers** — significant benefit on LVEF in nonischemic DCM management
- **Mineralocorticoid receptor antagonists (MRAs)**
- **SGLT2 inhibitors** — now part of standard 4-pillar HFrEF GDMT
- **Diuretics** — symptomatic volume management

### Device Therapy
- **Implantable cardioverter-defibrillator (ICD)** for primary prevention — evidence nuanced in nonischemic DCM generally (DANISH trial: no overall mortality benefit, but reduced sudden cardiac death; younger patients <59 years showed mortality benefit) — NCIT term: device/procedure, not a drug-class NCIT clinical-action term (see dismech convention: bind the implantation procedure as the clinical action, with the device carried as a qualifier)

### Advanced Therapeutics / Surgical
- **Cardiac transplantation** — definitive treatment for end-stage disease; explicitly used in multiple reported CMD1X/FKTN-DCM patients (age 18 in the founding series; a 22-year-old in the JACC case series) — NCIT:C15289 (Organ Transplantation)
- **No gene therapy, cell therapy, or RNA-based therapy specific to FKTN-related cardiomyopathy** was identified as approved or in trials; the ribitol-supplementation strategy explored for **ISPD**-related dystroglycanopathy (partial restoration of α-DG glycosylation with dietary ribitol in cell/mouse models) is a related experimental approach in the broader pathway but has not been specifically reported for FKTN-attributable disease in this search.

### Supportive Care
- Standard heart-failure supportive management; monitoring during pregnancy is specifically emphasized in the literature (elective early delivery, e.g., cesarean section at 35 weeks, was used in the reported case to preempt further cardiac deterioration)
- Multidisciplinary cardiology–neuromuscular collaboration is explicitly recommended in the recent case-series literature once a dual cardiac/skeletal-muscle genetic diagnosis (FKTN or LMNA) is confirmed, to support transplant planning and lifelong neuromuscular surveillance

### Experimental
No CMD1X-specific registered clinical trials (ClinicalTrials.gov/NCT) were identified in this search.

---

## 13. Prevention

- **Primary prevention**: Not applicable in the classic sense (monogenic recessive disorder); **genetic counseling** for carrier parents (both parents of an affected child are obligate carriers) is the relevant preventive intervention, with reproductive options including carrier testing of at-risk relatives and prenatal/preimplantation genetic diagnosis where familial variants are known — particularly salient given the Japanese founder-allele carrier population.
- **Secondary prevention**: Early diagnostic suspicion in any patient with DCM plus unexplained CK elevation, enabling earlier initiation of GDMT and surveillance before advanced heart failure develops.
- **Tertiary prevention**: Close cardiac surveillance during pregnancy in known female patients/carriers of the disease-causing genotype, given the demonstrated risk of pregnancy-associated decompensation; consideration of elective early delivery when cardiac function deteriorates in the third trimester (as performed in the reported case).
- **Genetic counseling**: Standard autosomal recessive counseling — 25% recurrence risk for full siblings of an affected proband, carrier risk assessment for extended family, with special attention to the high carrier frequency of the FCMD founder allele in Japanese populations.

---

## 14. Other Species / Natural Disease

- No naturally occurring FKTN-associated dilated cardiomyopathy has been reported in companion animals or wildlife (OMIA search not specifically performed for FKTN homologs in this pass, but no domestic-animal disease literature surfaced organically in this search).
- **Orthologous gene**: Mouse *Fktn* (MGI:2179507), used extensively in engineered knockout/conditional-knockout models (see below) — this is the primary comparative-biology resource, not a naturally occurring veterinary disease.

---

## 15. Model Organisms

### Mouse models
- **Cardiac-specific *Fktn* conditional/constitutive knockout mice** — the key model system for CMD1X mechanism, described in "Elimination of fukutin reveals cellular and molecular pathomechanisms in muscular dystrophy-associated heart failure" (*Nat Commun* 2019, PMID:31848331):
  - Constitutive cardiac *Fktn* elimination: markedly reduced α-DG glycosylation and DGC protein content at the sarcolemma at all developmental stages, but **cardiac dysfunction manifests only in later adulthood** — indicating membrane fragility alone is insufficient for the phenotype
  - Young-adult *Fktn*-deficient hearts: increased vulnerability to pathological hypertrophic stress, with **downregulated Akt signaling and disrupted MEF2-HDAC transcriptional axis**
  - **Acute/inducible *Fktn* elimination** in adult hearts: severe cardiac dysfunction and accelerated mortality, myocyte contractile dysfunction, disordered Golgi-microtubule networks
- **FKRP P448L mutant mice** (a related dystroglycanopathy gene in the same pathway) — model progressive dystrophic pathology in diaphragm and impaired cardiac function, useful as a comparative dystroglycanopathy-cardiac model (PMC5053477)

### Model Characteristics
- **Phenotype recapitulation**: The mouse cardiac-specific knockout models faithfully reproduce the biochemical lesion (α-DG hypoglycosylation, DGC reduction) and capture a genuinely age-dependent, stress-sensitized cardiac dysfunction pattern broadly consistent with the human disease's variable-onset, stress-precipitated course (e.g., pregnancy).
- **Model limitations**: The mouse constitutive/acute knockouts represent essentially **complete loss of Fktn function**, which more closely models the severe end of the FKTN allelic spectrum (Fukuyama/Walker-Warburg-type null combinations) rather than the specific **hypomorphic compound-heterozygous genotype** that produces the human CMD1X phenotype (cardiac-predominant, skeletal-muscle-sparing). This is a meaningful **human-model fidelity gap**: no current mouse model precisely recapitulates the tissue-selective (cardiac >> skeletal) vulnerability that defines CMD1X, since the knockouts used are typically complete nulls rather than partial-function hypomorphic alleles. This gap would be well-suited to a `HUMAN_MODEL_MISMATCH` discussion in a curated entry, since the mouse data support the general FKTN-cardiac-dysfunction mechanism (Akt/MEF2-HDAC pathway) but cannot yet explain the specific cardiac-vs-skeletal tissue dissociation central to the human phenotype.
- **Applications**: These models have been used to dissect the relative contributions of membrane-fragility versus stress-signaling mechanisms in dystroglycanopathy-associated cardiomyopathy, and to identify the Akt/MEF2-HDAC axis as a candidate therapeutic target.

### Resources
Mouse Genome Informatics: **Fktn**, MGI:2179507.

---

## Summary Table of Suggested Ontology Bindings

| Concept | Suggested term |
|---|---|
| Disease | MONDO:0012704 (Dilated cardiomyopathy 1X) |
| Gene | HGNC:3622 (FKTN) |
| Dilated cardiomyopathy phenotype | HP:0001635 |
| Elevated CK | HP:0003236 |
| Limb-girdle muscle weakness | HP:0003749 |
| Cardiac muscle cell | CL:0000746 |
| Heart | UBERON:0000948 |
| Golgi apparatus (site of enzymatic defect) | GO:0005794 |
| Protein O-linked mannosylation / glycosylation | GO:0035269 / GO:0006486 |
| Organ transplantation (treatment) | NCIT:C15289 |
| Pharmacotherapy (general) | NCIT:C15986 |

---

## Notes on Evidence Gaps for Curation

1. **No large cohort/registry data** exist — all clinical characterization derives from case reports/small series (n≤6), so frequency/percentage-type claims (e.g., "X% have limb-girdle weakness") cannot be well supported and should be phrased qualitatively per the source language ("mild or no," "minimal").
2. **Carrier frequency figure** for the Japanese FCMD founder allele needs primary-source verification before inclusion in a KB entry (a commonly cited ~1/90 figure was not independently re-confirmed in this pass).
3. **Human-model mismatch**: mouse *Fktn* cardiac knockout models are complete nulls and do not recapitulate the hypomorphic, tissue-selective human CMD1X genotype-phenotype relationship — flag explicitly if citing the Nat Commun 2019 mouse mechanism data to support human pathophysiology claims.
4. **Nomenclature disambiguation is critical**: "CMD1X"/FKTN (autosomal recessive, chr9) must not be conflated with "X-linked dilated cardiomyopathy"/DMD (X-linked, Xp21, OMIM CMD3B #302045) — both terms appear interchangeably in search indices and even in some secondary literature, but they are genetically and mechanistically distinct entities.

---

### Sources
- [Entry - #611615 - CARDIOMYOPATHY, DILATED, 1X; CMD1X - OMIM](https://www.omim.org/entry/611615)
- [Dilated cardiomyopathy 1X - NIH Genetic Testing Registry (GTR) - NCBI](https://www.ncbi.nlm.nih.gov/gtr/conditions/C1969024/)
- Murakami T, et al. "Fukutin gene mutations cause dilated cardiomyopathy with minimal muscle weakness." *Ann Neurol* 2006;60(5):597-602. [PubMed PMID:17036286](https://pubmed.ncbi.nlm.nih.gov/17036286/)
- [Compound Heterozygous FKTN Variants in a Patient with Dilated Cardiomyopathy Led to an Aberrant α-Dystroglycan Pattern - PMC9223741](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9223741/)
- [A case of pregnancy complicated with dilated cardiomyopathy 1X - PMC4630494](https://pmc.ncbi.nlm.nih.gov/articles/PMC4630494/) / [Oxford Medical Case Reports](https://academic.oup.com/omcr/article/2015/11/351/2362277)
- [Elimination of fukutin reveals cellular and molecular pathomechanisms in muscular dystrophy-associated heart failure - Nature Communications](https://www.nature.com/articles/s41467-019-13623-2) (PMID:31848331)
- [ISPD produces CDP-ribitol used by FKTN and FKRP to transfer ribitol phosphate onto α-dystroglycan - Nature Communications](https://www.nature.com/articles/ncomms11534) (PMID:27194101)
- [Entry - *607440 - FUKUTIN; FKTN - OMIM](https://omim.org/entry/607440)
- [Entry - #253800 - MUSCULAR DYSTROPHY-DYSTROGLYCANOPATHY (CONGENITAL WITH BRAIN AND EYE ANOMALIES), TYPE A, 4; MDDGA4 - OMIM](https://omim.org/entry/253800)
- [Entry - #611588 - MUSCULAR DYSTROPHY-DYSTROGLYCANOPATHY (LIMB-GIRDLE), TYPE C, 4; MDDGC4 - OMIM](https://omim.org/entry/611588)
- [Fukuyama Congenital Muscular Dystrophy - GeneReviews - NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/NBK1206/)
- [Deep-intronic variant of fukutin is the most prevalent point mutation of Fukuyama congenital muscular dystrophy in Japan - Journal of Human Genetics](https://www.nature.com/articles/jhg201771)
- [Dilated Cardiomyopathy and Later Onset Limb-Girdle Muscular Dystrophy Associated With Fukutin and Lamin A/C Mutations - JACC: Case Reports](https://www.jacc.org/doi/full/10.1016/j.jaccas.2026.107038)
- [Fukuyama Congenital Muscular Dystrophy via the FKTN Japanese Founder Mutation Test - PreventionGenetics](https://www.preventiongenetics.com/testInfo?val=Fukuyama-Congenital-Muscular-Dystrophy-via-the-FKTN-Japanese-Founder-Mutation)
- [Progressive Dystrophic Pathology in Diaphragm and Impairment of Cardiac Function in FKRP P448L Mutant Mice - PMC5053477](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5053477/)
- [Fktn MGI Mouse Gene Detail - MGI:2179507](https://www.informatics.jax.org/marker/MGI:2179507)
- [X-Linked Dilated Cardiomyopathy: A Cardiospecific Phenotype of Dystrophinopathy - PMC4491663](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4491663/) (context/disambiguation source for CMD3B/DMD-related XLDC, distinct from CMD1X)
- Dilated Cardiomyopathy (DCM) Guidelines — [Medscape: 2022 ACC/AHA/HFSA, 2023 ESC Cardiomyopathies](https://emedicine.medscape.com/article/152696-guidelines)
- [Current Management and Treatment - Dilated Cardiomyopathy - NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/NBK553842/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 8 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 25 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 3 |
| Terms whose name was checked | 14 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0012704` (2 mentions) - the report calls it "MONDO", "Dilated cardiomyopathy 1X"; MONDO calls it **dilated cardiomyopathy 1X**
- `HP:0001635` (4 mentions) - the report calls it "Dilated cardiomyopathy", "Dilated cardiomyopathy phenotype"; HP calls it **Congestive heart failure**
- `HP:0001639` (1 mention) - the report calls it "Hypertrophic cardiomyopathy — not applicable here but relevant to FKTN mutational screens that included HCM cohorts"; HP calls it **Hypertrophic cardiomyopathy**
- `HP:0001636` (1 mention) - the report calls it "Tachycardia"; HP calls it **Tetralogy of Fallot**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0006486` (obsolete protein glycosylation) (2 mentions) - replaced by `GO:0009101`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0003749` (3 mentions) - the report calls it "Limb-girdle muscle weakness"; HP calls it **Pelvic girdle muscle weakness**, and lists "Hip girdle muscle weakness" among its other names
- `HP:0003236` (3 mentions) - the report calls it "Elevated CK"; HP calls it **Elevated circulating creatine kinase activity**, and lists "Elevated serum CPK" among its other names
- `HP:0001644` (1 mention) - the report calls it "Dilated cardiomyopathy — note overlapping codes across HPO releases"; HP calls it **Dilated cardiomyopathy**
- `CL:0000746` (3 mentions) - the report calls it "Cardiomyocytes", "Cardiac muscle cell"; CL calls it **cardiac muscle cell**, and lists "cardiomyocyte" among its other names
- `GO:0005794` (2 mentions) - the report calls it "Golgi apparatus (site of enzymatic defect)"; GO calls it **Golgi apparatus**
- `NCIT:C15986` (2 mentions) - the report calls it "Pharmacotherapy", "Pharmacotherapy (general)"; NCIT calls it **Pharmacotherapy**
- `NCIT:C15289` (2 mentions) - the report calls it "Organ Transplantation", "Organ transplantation (treatment)"; NCIT calls it **Organ Transplantation**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0012704` - called "MONDO", "Dilated cardiomyopathy 1X"
- `HP:0001635` - called "Dilated cardiomyopathy", "Dilated cardiomyopathy phenotype"
- `CL:0000746` - called "Cardiomyocytes", "Cardiac muscle cell"
- `NCIT:C15986` - called "Pharmacotherapy", "Pharmacotherapy (general)"
- `NCIT:C15289` - called "Organ Transplantation", "Organ transplantation (treatment)"
- `MGI:2179507` - called "Fktn", "Orthologous gene**: Mouse *Fktn"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.