---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-02T02:26:32.893555'
end_time: '2026-09-02T02:31:07.477624'
duration_seconds: 274.58
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Developmental Delay, Hypotonia, Musculoskeletal Defects, and Behavioral
    Abnormalities
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
  web_search_requests: 14
  num_turns: 27
  total_cost_usd: 1.2739027999999997
  session_id: 94fd9ae5-d663-5ad6-bcc2-c2b5a7cf608a
  stop_reason: end_turn
  assistant_text_blocks: 2
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
citation_count: 7
reference_validation:
  total_references: 4
  verified: 4
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 4
  on_topic: 4
  validator_version: 0.2.1
term_validation:
  total_terms: 66
  verified: 62
  not_found: 0
  obsolete: 2
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 17
  labels_matching: 1
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: HP:0034274
    reported_labels:
    - Chronic pain
    ontology_label: Gastrointestinal ulcer
  - term_id: HP:0000768
    reported_labels:
    - "Phenotype \u2014 pectus deformity"
    ontology_label: Pectus carinatum
  - term_id: UBERON:0001130
    reported_labels:
    - scoliosis
    ontology_label: vertebral column
  - term_id: UBERON:0001491
    reported_labels:
    - pectus deformity
    ontology_label: wrist joint
  - term_id: NCIT:C15302
    reported_labels:
    - Developmental/rehabilitative therapies:** Physical therapy
    ontology_label: Physical Therapy
  labels_variant: 11
  obsolete_terms:
  - term_id: GO:0043486
    ontology_label: obsolete histone exchange
  - term_id: GO:0031498
    ontology_label: obsolete chromatin disassembly
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Developmental Delay, Hypotonia, Musculoskeletal Defects, and Behavioral Abnormalities
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Developmental Delay, Hypotonia, Musculoskeletal Defects, and Behavioral Abnormalities** covering all of the
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

I'll research this condition now using web search and fetch tools.

I have sufficient data to compile a comprehensive report now.

# Developmental Delay, Hypotonia, Musculoskeletal Defects, and Behavioral Abnormalities (DEHMBA)

## Executive Summary

DEHMBA is a recently delineated (2021), autosomal dominant, early-onset neurodevelopmental disorder caused by de novo heterozygous truncating (and occasionally other loss-of-function) variants in **SRCAP** (SNF2-related CREBBP activator protein), the same gene that — when truncated within a specific "hotspot" (exons 33–34) — causes the clinically distinct **Floating-Harbor syndrome (FLHS)**. DEHMBA is characterized by global developmental delay/intellectual disability, speech delay, hypotonia, behavioral/psychiatric abnormalities (including autism spectrum features in roughly half of patients), and variable, non-diagnostic musculoskeletal and facial features. It is genotypically and epigenetically distinguishable from FLHS by variant location and a distinct genome-wide DNA methylation ("episignature") profile.

---

## 1. Disease Information

**Overview:** DEHMBA (also styled "SRCAP-related neurodevelopmental disorder," non-FLHS-locus type) is an early-onset, autosomal dominant neurodevelopmental disorder first delineated by Rots et al. (2021), who reported 33 unrelated individuals with de novo heterozygous truncating *SRCAP* variants that mapped either proximal (n=28) or distal (n=5) to the *FLHS* mutational hotspot in exons 33–34. Affected individuals share global developmental delay (with or without intellectual disability), speech/language delay, hypotonia, behavioral/psychiatric problems, non-specific facial dysmorphism, and variable musculoskeletal findings, but they conspicuously **lack** the short stature, brachydactyly, delayed bone age, and characteristic gestalt facies that define FLHS — the original disorder associated with *SRCAP*.

**Key identifiers:**
- **OMIM:** #619595 — "DEVELOPMENTAL DELAY, HYPOTONIA, MUSCULOSKELETAL DEFECTS, AND BEHAVIORAL ABNORMALITIES; DEHMBA" [OMIM entry](https://www.omim.org/entry/619595)
- **Gene locus (OMIM):** *611421 — SRCAP (SNF2-related CBP activator protein) [OMIM gene entry](https://omim.org/entry/611421)
- **MONDO:** MONDO:0859202
- **MedGen:** UID 1794222 / Concept ID C5562012 [MedGen](https://www.ncbi.nlm.nih.gov/medgen/1794222)
- **Gene:** SRCAP, chromosome 16p11.2 (GRCh38 ~16:30,698,209–30,741,409)
- **Inheritance:** Autosomal dominant, typically de novo
- **Related/allelic disorder:** Floating-Harbor syndrome (OMIM #136140), caused by truncating variants restricted to exons 33–34 of the same gene
- **Also allelic to:** an emerging developmental and epileptic encephalopathy (DEE) phenotype (Liang et al., 2026, *Epilepsia*) associated with more severely damaging de novo *SRCAP* variants (truncating or damaging missense) — see Section 6/8 below

**Synonyms:** DEHMBA; SRCAP-related neurodevelopmental disorder (non-Floating-Harbor); "developmental delay, hypotonia, musculoskeletal defects, and behavioral abnormalities syndrome"

**Data provenance:** The disease was delineated from an aggregated, multi-institution research cohort (international collaborative case series compiled via GeneMatcher-type networks and clinical/research exome sequencing), not from a single EHR-based population — i.e., this is a rare-disease gene-discovery cohort of 33+ individuals rather than an aggregated administrative/claims dataset.

---

## 2. Etiology

**Disease causal factor:** DEHMBA is caused by **de novo heterozygous truncating variants in SRCAP** (nonsense, frameshift, canonical splice-site) located outside (proximal or distal to) the FLHS exon 33–34 hotspot. A subsequent report (Yamamoto et al., 2024, *J Hum Genet*) identified a **de novo intronic SRCAP variant** detected only by combined exome plus whole-transcriptome sequencing, causing DEHMBA with a severe sleep disorder — illustrating that some causal variants are missed by exome sequencing alone and require RNA-level confirmation of aberrant splicing. A separate case report (2022) described a **de novo SVA retrotransposon insertion in exon 13 of SRCAP** producing a DEHMBA-like neurodevelopmental phenotype, expanding the mutational mechanism spectrum beyond simple SNVs/indels.

**Genetic risk factors:**
- All reported pathogenic variants are **truncating, splice-altering, or structural (retrotransposon insertion)** loss-of-function-type changes in *SRCAP*, essentially all occurring **de novo** (not inherited from unaffected parents).
- Nonsense-mediated decay (NMD) location relative to the FLHS hotspot appears to determine phenotype: truncations proximal or distal to exons 33–34 → DEHMBA; truncations restricted to exons 33–34 (escaping NMD, producing a stable truncated protein retaining an N-terminal ATPase/helicase domain) → FLHS. This is the accepted allelic mechanism model.
- A 16p11.2 microdeletion encompassing *SRCAP* has separately been reported in a patient with speech impairment, global developmental delay, and behavioral problems — indicating haploinsufficiency of *SRCAP* (rather than a specific truncated-protein dominant-negative/gain-of-function effect) is sufficient to produce a DEHMBA-like phenotype, consistent with the loss-of-function/haploinsufficiency model.
- *SRCAP* is independently recognized as a **high-confidence autism spectrum disorder (ASD) risk gene**: de novo loss-of-function variants were identified in ASD probands in the Simons Simplex Collection (Iossifov et al. 2014) and The Autism Simplex Collection (Stessman et al. 2017), predating and converging with the DEHMBA delineation.

**Environmental risk factors:** None established; DEHMBA is a purely monogenic disorder with no reported environmental, infectious, or lifestyle contributory factors.

**Protective factors:** None reported in the literature to date.

**Gene-environment interactions:** Not studied/reported for this ultra-rare, recently described disorder.

---

## 3. Phenotypes

Frequencies below reflect the Rots et al. (2021) cohort (n=33, unless noted) and subsequent case reports; percentages should be treated as approximate given cohort size.

**Neurodevelopmental / cognitive:**
- Global developmental delay — core, essentially universal feature. HP:0001263
- Mild to severe intellectual disability (variable severity across the cohort). HP:0001249
- Speech and language delay, often disproportionately affected. HP:0000750
- Progression: generally **stable, non-regressive** developmental impairment rather than a degenerative course (consistent with a chromatin-remodeling neurodevelopmental disorder), though the sleep-disorder case report noted an unusually severe secondary sleep phenotype.

**Behavioral / psychiatric (a defining, name-bearing category):**
- Autism spectrum disorder / autistic features — reported in roughly half of patients. HP:0000717
- Challenging/disruptive behavior, anger. HP:0000708 (Aggressive behavior)
- Anxiety. HP:0000739
- ADHD / attention-deficit/hyperactivity disorder. HP:0007018
- Tics / Tourette syndrome — reported in a subset (4 of 33). HP:0100033 / HP:0100022
- Psychosis — reported in a subset (4 of 33). HP:0000709

**Neurological:**
- Hypotonia — core, name-bearing feature, generally axial/central. HP:0001252
- Seizures — reported in a minority (~3 of 33, ~9%). HP:0001250
- Severe sleep disturbance highlighted as a prominent feature in at least one intronic-variant case (Yamamoto et al. 2024). HP:0002360

**Musculoskeletal (a defining, name-bearing category — notably variable/non-diagnostic, unlike FLHS):**
- Joint hypermobility. HP:0001382
- Chronic musculoskeletal pain. HP:0034274 (Chronic pain) / generalized musculoskeletal pain
- Scoliosis. HP:0002650
- Pectus deformities (excavatum/carinatum). HP:0000768
- Delayed skeletal maturation (bone age delay), reported in MedGen feature list but **not** the severe, near-universal delayed bone age characteristic of FLHS. HP:0002750
- Short stature reported in a subset — again notably **less consistent/severe** than in FLHS, an important differentiator. HP:0004322

**Craniofacial (non-specific — explicitly distinguishes DEHMBA from FLHS, which has a highly recognizable gestalt):**
- Macrocephaly or microcephaly (variable, not unidirectional). HP:0000256 / HP:0000252
- Long face, prominent forehead. HP:0000276 / HP:0011220
- Wide nasal bridge, wide mouth. HP:0000431 / HP:0000154
- Long philtrum. HP:0000343
- Epicanthus, narrow palpebral fissures. HP:0000286 / HP:0045025
- Everted lower lip vermilion, thin upper lip vermilion. HP:0000232 / HP:0000219
- Mandibular prognathia, retrognathia. HP:0000303 / HP:0000278
- Periorbital fullness. HP:0000629
- Protruding ears. HP:0000411

**Other systemic/organ features:**
- Gastroesophageal reflux. HP:0002020
- Cryptorchidism (males). HP:0000028
- Ocular abnormalities: hypermetropia, myopia, strabismus. HP:0000540 / HP:0000545 / HP:0000486

**Quality-of-life impact:** No disease-specific QoL instrument data have been published given the disorder's recent delineation (2021) and rarity; QoL burden is inferred from the combination of intellectual disability, behavioral/psychiatric comorbidity (anxiety, aggression, psychosis in a subset), and chronic musculoskeletal pain, which together are expected to substantially affect adaptive functioning, education, and family caregiving burden, consistent with other SRCAP-related and chromatinopathy neurodevelopmental disorders.

---

## 4. Genetic / Molecular Information

**Gene:** SRCAP (HGNC:16974; also known as SNF2-related CREBBP activator protein, DOM1, FLHS gene), chromosome 16p11.2.

**Causal variant classes:**
- **Truncating variants** (nonsense, frameshift) located proximal or distal to the FLHS hotspot (exons 33–34) — the predominant mechanism in the founding Rots et al. 2021 cohort (28 proximal, 5 distal of 33 patients).
- **Canonical splice-site variants.**
- **Deep intronic variant** causing aberrant splicing/pseudoexon inclusion, detectable only via combined exome + whole transcriptome sequencing (Yamamoto et al., 2024, PMID:38448605) — this case underscores a diagnostic-methodology point relevant to curation: standard exome sequencing can produce false-negative results in SRCAP-suspected DEHMBA, and RNA-based confirmation may be required.
- **Structural variant / retrotransposon insertion:** a de novo SVA element insertion in exon 13 of SRCAP produced a DEHMBA-like neurodevelopmental phenotype (2022 case report, PMID:35768521), expanding recognized mutational mechanisms beyond point mutations/indels.
- **16p11.2 microdeletion encompassing SRCAP** — a contiguous-gene/whole-gene deletion also reported to produce a DEHMBA-like presentation, supporting a haploinsufficiency mechanism.

**Variant origin and zygosity:** Essentially all reported DEHMBA variants are **de novo** and **heterozygous**; the disorder is not described as recessive or biallelic (contrast with the Liang et al. 2026 DEE/focal-epilepsy report, which found biallelic, milder-damage variants in a distinct focal-epilepsy subgroup — see Section 8).

**Functional consequence / mechanism:** Loss-of-function/haploinsufficiency of SRCAP. Truncating variants proximal or distal to exons 33–34 are presumed to trigger nonsense-mediated decay or otherwise abolish functional SRCAP protein, in contrast to FLHS-causing truncations restricted to exons 33–34, which escape NMD and produce a stable, likely dominant-negative or altered-function truncated protein retaining the N-terminal ATPase/helicase domain but lacking C-terminal regulatory sequence. This variant-position-dependent mechanism (NMD-escape hotspot vs. NMD-triggering elsewhere in the gene) is the accepted molecular explanation for the phenotypic divergence between FLHS and DEHMBA from the same gene.

**Epigenetic signature:** Rots et al. (2021) demonstrated that DEHMBA-causing (non-hotspot) truncating SRCAP variants produce a **distinct, disorder-specific genome-wide DNA methylation ("episignature") profile**, separable from the FLHS episignature and from controls, now incorporated into the clinically validated **EpiSign** DNA methylation array diagnostic platform as one of the growing set (~70+) of chromatinopathy episignatures used to resolve variants of uncertain significance and support diagnosis in genetically unresolved cases.

**Population frequency / constraint:** SRCAP is a large, evolutionarily conserved gene; independent evidence of strong loss-of-function intolerance comes from its established status as a **high-confidence ASD risk gene** in large de novo variant burden studies (Iossifov et al. 2014; Stessman et al. 2017), consistent with a highly constrained gene where de novo LoF variants are pathogenic rather than population polymorphisms.

**Modifier genes:** None specifically established for DEHMBA.

**Chromosomal abnormalities:** A 16p11.2 microdeletion encompassing SRCAP has been reported with an overlapping phenotype (speech impairment, developmental delay, behavioral problems), distinct from the well-known recurrent 16p11.2 BP4–BP5 CNV syndrome (which is a different, more proximal/larger interval); curators should take care to distinguish SRCAP-specific deletions from the classic 16p11.2 microdeletion/microduplication syndrome.

---

## 5. Environmental Information

No environmental, toxin, occupational, dietary, or lifestyle factors are implicated in DEHMBA; it is a purely monogenic, de novo disorder. No infectious triggers are reported. This section is essentially "not applicable" for this Mendelian chromatin-remodeling disorder, analogous to other de novo dominant neurodevelopmental syndromes.

---

## 6. Mechanism / Pathophysiology

**Causal chain (numbered, from molecular lesion to clinical manifestation):**

1. A de novo heterozygous loss-of-function variant (truncating SNV/indel, canonical splice variant, deep intronic splice-altering variant, or retrotransposon insertion) arises in *SRCAP*, located outside the FLHS exon 33–34 hotspot — **leads to** production of a non-functional or absent SRCAP protein from one allele (via nonsense-mediated decay or structural disruption).
2. Reduced functional SRCAP dosage (haploinsufficiency) **results in** impaired assembly/activity of the **SRCAP chromatin-remodeling complex** (SRCAP, DMAP1, YL1/VPS72, RUVBL1, RUVBL2, ACTL6A, ARP6/ACTR6, ACTIN, GAS41, ZNHIT1), the human ortholog of the yeast SWR1 complex.
3. Impaired SRCAP complex activity **leads to** deficient ATP-dependent exchange of canonical histone H2A/H2B dimers for **histone variant H2A.Z**-containing dimers at target nucleosomes (this is the complex's core catalytic function; direct structural biology confirms SRCAP and its paralog TIP60/EP400 as the principal human H2A.Z-depositing remodelers, distinguishing them mechanistically from the related INO80 complex, which removes rather than deposits H2A.Z).
4. Genome-wide mis-deposition of H2A.Z **results in** dysregulated chromatin accessibility and altered transcriptional output at SRCAP target loci — this step is directly evidenced in humans by the reproducible, disorder-specific genome-wide DNA methylation episignature detected in DEHMBA patients (Rots et al. 2021), a downstream chromatin/epigenomic correlate of SRCAP dysfunction.
5. In model systems, one specific and mechanistically well-characterized downstream consequence is **reduced expression of *Satb2*** (a chromatin-organizing transcription factor itself causal for a distinct neurodevelopmental disorder, SATB2-associated syndrome), shown in *Srcap+/-* mice to result from **diminished H2A.Z occupancy at the Satb2 promoter** — this is a mouse/model-organism finding, inferred to be translationally relevant but not yet directly confirmed in human SRCAP-DEHMBA brain tissue (a candidate `HUMAN_MODEL_MISMATCH`-type gap for KB curation).
6. Reduced Satb2 (and dysregulation of ~27 additional ASD-implicated genes identified by RNA sequencing in the mouse model) **leads to** downstream neurodevelopmental cellular abnormalities: in *Srcap+/-* mice, a decreased number of parvalbumin (PV)-expressing interneurons in the retrosplenial cortex and dentate gyrus, and altered dendritic structure, synaptic density, and synaptic transmission in the dentate gyrus.
7. These cellular/circuit-level abnormalities **result in** the behavioral phenotype observed in the mouse model — impaired social novelty, repetitive/stereotyped behaviors, anxiety-like behavior, and learning/memory deficits — mirroring, at a model-organism level, the human behavioral/psychiatric domain of DEHMBA (autism spectrum features, anxiety, ADHD, aggression).
8. In parallel (branch point), haploinsufficiency-driven chromatin dysregulation during development **leads to** the human clinical phenotype of global developmental delay, intellectual disability, speech/language delay, and hypotonia — the core neurodevelopmental triad — through mechanisms presumed analogous to (7) but not yet directly dissected in human neural tissue.
9. A separate, less-characterized branch: SRCAP dysfunction also **contributes to** variable musculoskeletal (joint hypermobility, scoliosis, pectus deformity, delayed bone maturation) and craniofacial dysmorphic features, presumably reflecting a broader developmental role of SRCAP/H2A.Z chromatin regulation in mesenchymal/skeletal lineages, though the specific cell types and pathways involved in this branch have not been mechanistically dissected (a knowledge gap).
10. **Rescue evidence supporting the causal chain:** AAV-mediated delivery of Satb2 into *Srcap+/-* mice ameliorated both the cellular abnormalities (interneuron/synaptic deficits) and the behavioral phenotype, providing interventional (not merely correlative) support that the Srcap→H2A.Z→Satb2 axis is mechanistically load-bearing for at least the behavioral/autistic component of the model phenotype.

**Molecular pathways:** SWR1/SRCAP chromatin-remodeling pathway; H2A.Z histone variant deposition/exchange pathway; downstream transcriptional regulation of neurodevelopmental genes including *SATB2*. GO terms: **GO:0043486** (histone exchange), **GO:0031498** (chromatin disassembly), **GO:0006338** (chromatin remodeling), **GO:0035102** (PRC1/SWI-SNF-type — not directly applicable, more precisely GO:0000812 Swr1 complex).

**Cellular processes:** Chromatin remodeling; transcriptional regulation; neuronal differentiation and interneuron specification (parvalbumin+ interneuron development); synaptogenesis/synaptic density regulation; dendritic morphogenesis.

**Protein dysfunction:** Loss of function via truncation/NMD (haploinsufficiency) rather than a stable dominant-negative or gain-of-function product (contrast with the FLHS-causing truncations, which retain the N-terminal ATPase domain and are hypothesized to act via a distinct mechanism producing a different, growth-restriction-dominated phenotype).

**Cell types implicated:** Excitatory and inhibitory (parvalbumin-expressing GABAergic interneuron; Cell Ontology **CL:0000850** or more specifically CL:0002273 for PV+ interneurons) neurons in cortex (retrosplenial cortex) and hippocampal dentate gyrus (granule neurons, CL:0000870), based on mouse model data.

**Epigenetic changes:** A genome-wide, disorder-specific DNA methylation episignature is the best-established human molecular biomarker of SRCAP-DEHMBA pathophysiology, now used diagnostically via the EpiSign platform.

**Molecular profiling:** RNA sequencing in the *Srcap+/-* mouse model identified dysregulation of 27 ASD-associated genes; no published human transcriptomic, proteomic, or single-cell profiling of DEHMBA patient tissue was identified in this search (a gap — most cellular/molecular mechanistic data derive from the mouse model, an important `HUMAN_MODEL_MISMATCH` consideration for curation given that direct human neural-tissue confirmation of the Satb2/H2A.Z axis is not yet available).

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Central nervous system (brain — cognition, behavior, tone regulation); musculoskeletal system (joints, spine, chest wall, long bones).
- **Secondary:** Gastrointestinal (reflux); genitourinary (cryptorchidism); ophthalmologic (refractive errors, strabismus); craniofacial skeleton.
- **Body systems:** Nervous system, musculoskeletal system, behavioral/psychiatric domain, digestive system, genitourinary system, sensory (ocular) system.

**Tissue/cell level:** Neuronal tissue (cortical and hippocampal neurons; parvalbumin-positive GABAergic interneurons per mouse model — Cell Ontology CL:0000850/CL:0002273); connective tissue and joint structures (hypermobility); skeletal/osseous tissue (delayed maturation, scoliosis, pectus deformity).

**Subcellular level:** Nucleus/nucleoplasm and chromatin (site of SRCAP complex activity); nucleosome (site of H2A.Z exchange). GO Cellular Component: **GO:0000812** (Swr1 complex), **GO:0000786** (nucleosome), **GO:0005634** (nucleus).

**Localization (UBERON):** Brain (UBERON:0000955), cerebral cortex (UBERON:0000956), hippocampus/dentate gyrus (UBERON:0001885/UBERON:0001885), skeletal system generally (UBERON:0001434), vertebral column (UBERON:0001130 — scoliosis), thoracic wall/sternum (UBERON:0001491 — pectus deformity). Findings are generally **bilateral/systemic** rather than lateralized, consistent with a chromatin-remodeling disorder affecting global developmental programs.

---

## 8. Temporal Development

**Onset:** Congenital/early childhood onset — developmental delay and hypotonia are typically apparent in infancy/early childhood; the disorder is classified as an early-onset neurodevelopmental disorder.

**Onset pattern:** Insidious/developmental rather than acute; behavioral/psychiatric features (ADHD, anxiety, tics, psychosis) may emerge or become more apparent later in childhood or adolescence.

**Progression:** Neurodevelopmental impairment is generally **static/stable** rather than degenerative (consistent with a congenital chromatin-regulatory disorder), though individual comorbidities (musculoskeletal pain, scoliosis, psychiatric symptoms) may evolve or worsen with growth and age. No formal staging system exists given the disorder's rarity and recent delineation.

**Disease course pattern:** Chronic, lifelong; not episodic or relapsing-remitting in its core neurodevelopmental features, though seizures (in the minority who have them) and psychiatric symptoms may be episodic.

**Recently expanded phenotypic spectrum:** A 2026 *Epilepsia* study (Liang et al., PMID:41144712) reports that **more severely damaging de novo SRCAP variants** (truncating or missense variants predicted to cause significant hydrophobicity/stability disruption) are associated with a **developmental and epileptic encephalopathy (DEE)** phenotype in a subset of patients (n=5), while **milder-damage, biallelic variants** were found in a separate group with **focal epilepsy** (n=6, including refractory cases) — suggesting a genotype-severity-phenotype gradient across the SRCAP-related disease spectrum from focal epilepsy → DEHMBA → DEE, and that variant "damage" (structural/hydrophobicity impact) may correlate with epilepsy severity and outcome. This is a very recent, still-emerging finding that meaningfully broadens the SRCAP-related disease spectrum beyond the 2021 DEHMBA and classic FLHS entries and merits close attention for future curation/entry-scope decisions.

**Critical periods:** Not formally established; as with most neurodevelopmental chromatinopathies, early childhood is presumed to be the critical window for developmental/behavioral intervention, though no DEHMBA-specific intervention-timing studies exist.

---

## 9. Inheritance and Population

**Epidemiology:** DEHMBA is an ultra-rare, recently delineated disorder; no formal population prevalence or incidence estimate has been published. Fewer than ~50 individuals have been reported in the literature to date (33 in the founding Rots et al. 2021 cohort, plus subsequent case reports — the intronic-variant case, the SVA-insertion case, and the newly reported DEE/focal-epilepsy expansion cohort). Given its very recent recognition (2021) and ongoing case ascertainment (as recently as 2026), prevalence is almost certainly under-ascertained.

**Inheritance pattern:** Autosomal dominant, virtually always de novo. No inherited transmission has been reported in the founding cohort (consistent with a severe, LoF-intolerant gene under strong purifying selection against inherited transmission of pathogenic variants, though the 2026 Epilepsia paper's report of biallelic variants in a distinct focal-epilepsy subgroup suggests inheritance patterns may be more heterogeneous across the full SRCAP phenotypic spectrum than in DEHMBA alone).

**Penetrance:** Presumed complete/high given exclusively de novo occurrence and consistent phenotype across unrelated probands, though formal penetrance estimates are not available for such a rare disorder.

**Expressivity:** Markedly variable — this is one of the disorder's defining features, especially in the musculoskeletal/craniofacial domain (in contrast to the tightly stereotyped FLHS gestalt). Severity of intellectual disability, presence/absence of seizures, and psychiatric comorbidity all vary substantially across reported patients.

**Genetic anticipation:** Not applicable (not a repeat-expansion disorder).

**Germline mosaicism:** Not specifically reported for DEHMBA, though it is a theoretical consideration for recurrence risk counseling in any de novo dominant disorder.

**Founder effects / consanguinity:** No founder mutations reported; disorder is de novo and pan-ethnic in the cases reported to date.

**Carrier frequency:** Not applicable to a de novo dominant disorder without population carrier screening data.

**Population demographics:** No specific ethnic, geographic, or sex-ratio enrichment has been reported in the literature reviewed; the founding cohort was assembled through international collaboration (implying broad geographic representation across contributing centers, likely predominantly Europe/North America given the authorship and GeneMatcher-style ascertainment, though exact per-country breakdown was not retrieved in this search).

---

## 10. Diagnostics

**Clinical/genetic testing:**
- **First-tier:** Exome sequencing (trio, proband + parents) to identify de novo heterozygous truncating/LoF *SRCAP* variants — the primary diagnostic approach used in the founding cohort.
- **Second-tier / when exome is non-diagnostic despite strong clinical suspicion:** Combined exome + whole transcriptome (RNA) sequencing, which identified a deep intronic splice-altering variant missed by DNA-only exome analysis (Yamamoto et al. 2024) — an important diagnostic-methodology point for genetically unresolved suspected cases.
- **Structural variant detection:** Standard short-read exome/genome pipelines may miss retrotransposon (e.g., SVA) insertions; specialized structural-variant-calling algorithms or long-read sequencing may be required, as illustrated by the 2022 exon-13 SVA insertion case.
- **Chromosomal microarray (CMA):** relevant to exclude/detect a 16p11.2 deletion encompassing SRCAP, which can produce an overlapping phenotype.
- **DNA methylation episignature testing (EpiSign):** A validated, clinically available adjunct diagnostic tool — DEHMBA (non-hotspot truncating SRCAP variants) has a distinct genome-wide methylation signature separable from FLHS and from unaffected controls, useful for resolving variants of uncertain significance in SRCAP and for supporting diagnosis in genetically undiagnosed individuals with a compatible phenotype.

**Clinical criteria / differential diagnosis:** No formal consensus diagnostic criteria (DSM/ICD-style) exist given the disorder's recent delineation; diagnosis rests on molecular confirmation of a qualifying de novo SRCAP variant in the appropriate clinical context. Key differential diagnoses include:
- **Floating-Harbor syndrome** (same gene, different variant location; distinguished by short stature, brachydactyly, delayed bone age, and characteristic facial gestalt, which are absent or much milder in DEHMBA).
- Classic **16p11.2 BP4–BP5 recurrent microdeletion/duplication syndrome** (a different, larger CNV interval; distinguish from focal SRCAP-only deletions).
- Other SATB2-related and chromatin-remodeling neurodevelopmental disorders (SATB2-associated syndrome, given the mechanistic Satb2 link) and other autism-associated chromatinopathies more broadly, given overlapping ID/ASD/hypotonia phenotypes.
- The newly described **SRCAP-related DEE / focal epilepsy** phenotypic extremes (Liang et al. 2026) should be considered part of a broader SRCAP-related spectrum when epilepsy is a prominent early feature.

**Screening:** No population or newborn screening program exists (not applicable to this ultra-rare, individually ascertained disorder); diagnosis is case-by-case via clinical exome/genome sequencing.

---

## 11. Outcome / Prognosis

No formal survival, mortality, or long-term natural-history/longitudinal outcome data have been published for DEHMBA given its 2021 delineation and small reported cohort; there is no indication in the literature reviewed that DEHMBA is associated with reduced life expectancy or life-threatening organ involvement — the disorder's morbidity burden is dominated by neurodevelopmental (intellectual disability, speech delay), behavioral/psychiatric (autism, anxiety, aggression, tics, psychosis), and musculoskeletal (chronic pain, scoliosis) impacts on function and quality of life rather than by mortality risk. Prognostic factors (e.g., variant type/location, presence of seizures) have not been systematically studied; the emerging genotype-severity correlation reported in the 2026 Epilepsia SRCAP-DEE/focal-epilepsy expansion (variant "damage" correlating with epilepsy severity/outcome) may represent an early prognostic signal relevant to the broader SRCAP spectrum, but has not yet been validated specifically within DEHMBA.

---

## 12. Treatment

There is **no disease-specific, mechanism-targeted therapy** for DEHMBA; management is supportive/symptomatic, following general neurodevelopmental-disorder care models:

- **Developmental/rehabilitative therapies:** Physical therapy (NCIT:C15302), occupational therapy (NCIT:C121351), and speech-language therapy (NCIT:C159273) for developmental delay, hypotonia, and speech impairment.
- **Behavioral/psychiatric management:** Behavioral therapy/counseling (NCIT:C181743) for autism spectrum features, ADHD, anxiety, and aggressive behavior; pharmacotherapy (NCIT:C15986) as clinically indicated for ADHD, anxiety, tics/Tourette syndrome, or psychosis (specific agents not systematically reported in the SRCAP-DEHMBA literature; management follows standard psychiatric practice for the specific comorbid symptom).
- **Musculoskeletal/orthopedic care:** Monitoring and, where indicated, orthopedic surgical procedure (NCIT:C16186) for scoliosis or symptomatic pectus deformity; supportive care for chronic musculoskeletal pain (NCIT:C15747).
- **Seizure management:** Standard antiseizure pharmacotherapy for the minority with epilepsy; the 2026 Epilepsia report's finding that focal-epilepsy-associated (biallelic, milder-damage) variants were "correlated with... outcomes" suggests genotype may eventually inform antiseizure treatment response expectations within the broader SRCAP spectrum, though this is not yet an actionable clinical guideline.
- **Genetic counseling** (NCIT:C15240): recommended given the de novo autosomal dominant inheritance pattern, with recurrence risk to future pregnancies generally low (baseline germline mosaicism risk) absent evidence of parental mosaicism.
- **Experimental/preclinical:** AAV-mediated Satb2 gene delivery ameliorated cellular and behavioral phenotypes in the *Srcap+/-* mouse model (Ding et al., 2023/2024) — a proof-of-concept, preclinical (mouse) finding suggesting a potential future targeted molecular strategy, but with **no human clinical translation, trial, or NCT-registered study** identified to date. This should be curated strictly as model-organism/computational-adjacent preclinical evidence, not as an available or emerging human treatment.

No clinical trials (ClinicalTrials.gov) specific to DEHMBA or SRCAP-related disorders were identified in this search.

---

## 13. Prevention

No primary, secondary, or tertiary prevention strategies exist for this de novo, non-preventable Mendelian disorder. Given its de novo, non-heritable-in-the-typical-sense pattern, **prenatal/preimplantation genetic diagnosis is not routinely applicable** except in the rare setting of documented parental germline mosaicism, and no such case has been reported. Genetic counseling remains the primary "preventive" intervention offered to families, focused on recurrence-risk discussion for future pregnancies (low, baseline de novo/mosaicism risk) rather than population-level prevention.

---

## 14. Other Species / Natural Disease

No naturally occurring veterinary/companion-animal disease attributable to spontaneous SRCAP variants has been reported (searched OMIA-type resources were not directly queried in this pass but no such reports surfaced in general literature search); DEHMBA-relevant animal data are limited to **engineered mouse models** (see Section 15). SRCAP is evolutionarily conserved (present with clear orthologs across vertebrates given its essential chromatin-remodeling function), consistent with the mouse ortholog *Srcap* (chromosome 7 F3 in mouse) being usable as a faithful genetic model.

---

## 15. Model Organisms

**Mouse (Mus musculus):**
- ***Srcap+/-* haploinsufficient mouse** (Ding et al., 2023 bioRxiv preprint / 2024 published): the principal, best-characterized model. Recapitulates autism-relevant behavioral domains — impaired social novelty, repetitive/stereotyped behavior, anxiety-like behavior, and learning/memory deficits — plausibly modeling the ASD/behavioral-abnormalities component of the human DEHMBA phenotype, though it has **not** been evaluated for the musculoskeletal, craniofacial, or broader developmental-delay/intellectual-disability domains, and its fidelity to the full human DEHMBA phenotype (versus the narrower ASD component) is an open question — a candidate `HUMAN_MODEL_MISMATCH` consideration for curation.
- Mechanistically, this model links Srcap haploinsufficiency → reduced H2A.Z occupancy at the *Satb2* promoter → reduced Satb2 expression → parvalbumin+ interneuron loss (retrosplenial cortex, dentate gyrus) and dentate gyrus synaptic/dendritic abnormalities → behavioral phenotype, with **AAV-Satb2 rescue** of both cellular and behavioral phenotypes providing causal (interventional) support for this pathway.
- **Human iPSC-derived or organoid models:** none identified in this search specific to SRCAP-DEHMBA.
- **Other species (zebrafish, Drosophila, C. elegans):** no SRCAP/DEHMBA-specific disease models identified in this search, though SRCAP/SWR1-complex biology is studied more generally in yeast (Swr1, the SRCAP ortholog) and Drosophila (Domino) as basic chromatin-biology models rather than disease models per se.

**Model limitations:** The mouse model captures behavioral/ASD-relevant and interneuron/synaptic phenotypes but has not been reported to recapitulate the musculoskeletal (joint hypermobility, scoliosis, pectus deformity), craniofacial, or broader somatic growth features of human DEHMBA; translational fidelity for the full human syndrome (beyond the behavioral/ASD axis) remains unestablished.

---

## Summary Table: Key Ontology Term Suggestions for KB Curation

| Domain | Suggested term(s) |
|---|---|
| Disease | MONDO:0859202; OMIM:619595 |
| Gene | hgnc:16974 (SRCAP) |
| Phenotype — DD/ID | HP:0001263, HP:0001249 |
| Phenotype — hypotonia | HP:0001252 |
| Phenotype — speech delay | HP:0000750 |
| Phenotype — autism | HP:0000717 |
| Phenotype — ADHD | HP:0007018 |
| Phenotype — anxiety | HP:0000739 |
| Phenotype — psychosis | HP:0000709 |
| Phenotype — seizures | HP:0001250 |
| Phenotype — joint hypermobility | HP:0001382 |
| Phenotype — scoliosis | HP:0002650 |
| Phenotype — pectus deformity | HP:0000768 |
| Biological process | GO:0006338 (chromatin remodeling), GO:0043486 (histone exchange) |
| Cellular component | GO:0000812 (Swr1/SRCAP complex), GO:0000786 (nucleosome) |
| Cell type (model) | CL:0002273 (parvalbumin interneuron), CL:0000870 (dentate gyrus granule neuron) |
| Anatomy | UBERON:0000955 (brain), UBERON:0001885 (hippocampal formation) |

---

## Key Primary References

1. Rots D, Chater-Diehl E, Dingemans AJM, et al. "Truncating SRCAP variants outside the Floating-Harbor syndrome locus cause a distinct neurodevelopmental disorder with a specific DNA methylation signature." *Am J Hum Genet.* 2021;108(6):1053-1068. PMID: [33909990](https://pubmed.ncbi.nlm.nih.gov/33909990/). — Founding paper delineating DEHMBA in 33 patients, establishing the episignature.
2. Yamamoto S, et al. "Combined exome and whole transcriptome sequencing identifies a de novo intronic SRCAP variant causing DEHMBA syndrome with severe sleep disorder." *J Hum Genet.* 2024. PMID: [38448605](https://pubmed.ncbi.nlm.nih.gov/38448605/).
3. "A neurodevelopmental disorder caused by a novel de novo SVA insertion in exon 13 of the SRCAP gene." 2022. PMID: [35768521](https://pubmed.ncbi.nlm.nih.gov/35768521/).
4. Liang, et al. "De novo SRCAP variants cause developmental and epileptic encephalopathy and the phenotypic spectrum." *Epilepsia.* 2026;67:846-861. PMID: [41144712](https://pubmed.ncbi.nlm.nih.gov/41144712/). — Expands the SRCAP-related phenotypic spectrum to DEE and focal epilepsy.
5. Ding C, Zhou W, Shi Y, et al. "Srcap haploinsufficiency induced autistic-like behaviors in mice through disruption of Satb2 expression." bioRxiv 2023.07.03.547590 / published 2024. — Mouse model mechanistic study.
6. Hood RL, et al. "Mutations in SRCAP, encoding SNF2-related CREBBP activator protein, cause Floating-Harbor syndrome." (foundational FLHS/SRCAP paper, ~2012).
7. OMIM #619595 (DEHMBA); OMIM *611421 (SRCAP); MedGen C5562012; MalaCards DVL013.

**Notes for curation:** Nearly all mechanistic (Satb2/H2A.Z/interneuron) data derive from a single mouse model and have not been directly confirmed in human tissue — flag as `HUMAN_MODEL_MISMATCH` if incorporated into a pathophysiology node. The 2026 Epilepsia paper substantially broadens the SRCAP-related phenotypic spectrum beyond DEHMBA/FLHS and may warrant a scope discussion (has_subtypes vs. related-entry) before curation.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 4 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 66 |
| Resolved | 62 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 2 |
| Terms whose name was checked | 17 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 11 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0034274` (1 mention) - the report calls it "Chronic pain"; HP calls it **Gastrointestinal ulcer**
- `HP:0000768` (2 mentions) - the report calls it "Phenotype — pectus deformity"; HP calls it **Pectus carinatum**
- `UBERON:0001130` (1 mention) - the report calls it "scoliosis"; UBERON calls it **vertebral column**
- `UBERON:0001491` (1 mention) - the report calls it "pectus deformity"; UBERON calls it **wrist joint**
- `NCIT:C15302` (1 mention) - the report calls it "Developmental/rehabilitative therapies:** Physical therapy"; NCIT calls it **Physical Therapy**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0043486` (obsolete histone exchange) (2 mentions)
- `GO:0031498` (obsolete chromatin disassembly) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000750` (2 mentions) - the report calls it "Phenotype — speech delay"; HP calls it **Delayed speech and language development**, and lists "Speech delay" among its other names
- `HP:0000717` (2 mentions) - the report calls it "Phenotype — autism"; HP calls it **Autism**
- `HP:0000708` (1 mention) - the report calls it "Aggressive behavior"; HP calls it **Atypical behavior**
- `HP:0000739` (2 mentions) - the report calls it "Phenotype — anxiety"; HP calls it **Anxiety**
- `HP:0007018` (2 mentions) - the report calls it "Phenotype — ADHD"; HP calls it **Attention deficit hyperactivity disorder**, and lists "ADHD" among its other names
- `HP:0000709` (2 mentions) - the report calls it "Phenotype — psychosis"; HP calls it **Psychosis**
- `HP:0001252` (2 mentions) - the report calls it "Phenotype — hypotonia"; HP calls it **Hypotonia**, and lists "Central hypotonia" among its other names
- `HP:0001250` (2 mentions) - the report calls it "Phenotype — seizures"; HP calls it **Seizure**, and lists "Epileptic seizure" among its other names
- `HP:0001382` (2 mentions) - the report calls it "Phenotype — joint hypermobility"; HP calls it **Joint hypermobility**
- `HP:0002650` (2 mentions) - the report calls it "Phenotype — scoliosis"; HP calls it **Scoliosis**
- `NCIT:C181743` (1 mention) - the report calls it "Behavioral/psychiatric management:** Behavioral therapy/counseling"; NCIT calls it **Behavioral Counseling**, and lists "Behavioral Psychotherapy" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.