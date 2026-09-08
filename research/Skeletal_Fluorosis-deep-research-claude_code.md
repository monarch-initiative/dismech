---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-07T16:53:00.008109'
end_time: '2026-09-07T16:58:24.082009'
duration_seconds: 324.07
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Skeletal Fluorosis
  mondo_id: MONDO:0400003
  category: Environmental Osteopathy
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
  web_search_requests: 22
  num_turns: 27
  total_cost_usd: 1.5238636
  session_id: 4bf4a114-75db-54c3-885d-72412fe47716
  stop_reason: end_turn
  assistant_text_blocks: 1
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderNotConfiguredError
  remedy: the provider is not configured
  retryable: false
- provider: claude_code
  succeeded: true
citation_count: 50
reference_validation:
  total_references: 43
  verified: 43
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 43
  on_topic: 30
  off_topic: 1
  off_topic_references:
  - PMID:34769866
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 58
  verified: 54
  not_found: 0
  obsolete: 0
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 42
  labels_matching: 30
  labels_mismatched: 6
  mislabelled_terms:
  - term_id: MONDO:0400003
    reported_labels:
    - Skeletal fluorosis
    - Ontology Lookup Service
    ontology_label: skeletal fluorosis
  - term_id: HP:0100774
    reported_labels:
    - Osteosclerosis
    ontology_label: Hyperostosis
  - term_id: HP:0009758
    reported_labels:
    - Enamel hypoplasia
    ontology_label: Pyramidal skinfold extending from the base to the top of the nails
  - term_id: UBERON:0002298
    reported_labels:
    - vertebral column
    ontology_label: brainstem
  - term_id: UBERON:0002417
    reported_labels:
    - "posterior longitudinal ligament \u2014 if available"
    ontology_label: abdominal segment of trunk
  - term_id: UBERON:0004123
    reported_labels:
    - femur
    ontology_label: myocardial layer
  labels_variant: 6
  unresolvable_prefixes:
  - ICD10CM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Skeletal Fluorosis
- **MONDO ID:** MONDO:0400003 (if available)
- **Category:** Environmental Osteopathy

## Research Objectives

Please provide a comprehensive research report on **Skeletal Fluorosis** covering all of the
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

# Skeletal Fluorosis — Comprehensive Research Report

## 1. Disease Information

**Overview.** Skeletal fluorosis (SF) is a chronic metabolic bone and joint disease caused by long-term excessive systemic fluoride exposure, most often from fluoride-contaminated groundwater but also from occupational inhalation, brick tea, coal-smoke indoor air pollution, or fluoride-containing consumer products (toothpaste, inhalant abuse of fluorinated computer-cleaner propellants, methoxyflurane analgesia). Fluoride has a very high affinity for calcium and is progressively deposited in the mineral phase of bone, producing a syndrome of active osteogenesis and accelerated, disorganized bone turnover that manifests as diffuse osteosclerosis, osteopenia in some compartments, exostoses, ligament/tendon ossification, and — in advanced disease — mechanical compression of the spinal cord and nerve roots (PMID:3295994; MONDO:0400003 definition).

**Key identifiers:**
- **MONDO:** MONDO:0400003 — "Skeletal fluorosis," defined as *"A condition that results from excessive fluoride ingestion leading to fluoride accumulation in the bone progressively over many years. The early symptoms...include stiffness and pain in the joints"* (synonym: "Fluorosis of the skeleton") — cross-referenced to ICD10CM:M85.1 and WHO ICD-11 entity 1269698463 (https://www.ebi.ac.uk/ols4/ontologies/mondo).
- **ICD-10-CM:** M85.1– series ("Disorders of bone density and structure, fluorosis of bone"), with laterality/site-specific subcodes (e.g., M85.10 unspecified site, M85.15 thigh, M85.159 unspecified thigh, M85.162 left lower leg) (icd10data.com; aapc.com).
- **ICD-11:** Entity 1269698463 (WHO ICD API).
- A **separate, related but distinct** entity is *dental fluorosis* (MONDO:0006722), an enamel-formation disorder from fluoride exposure during odontogenesis (age <8 years) — do not conflate with skeletal fluorosis, which reflects lifetime cumulative bone fluoride burden.
- **MeSH:** Fluorosis, Dental (D005506) is indexed separately from bone-fluoride toxicity literature, which is typically indexed under "Fluorides/adverse effects" and "Fluorosis, Skeletal" is not a standalone current MeSH heading in all databases — most PubMed indexing uses "Fluorides/poisoning" + "Bone Diseases."
- **Synonyms/alternative names:** endemic skeletal fluorosis; osteofluorosis; crippling fluorosis; fluoride osteosclerosis; brick-tea-type fluorosis (a specific etiologic subtype); industrial/occupational fluorosis.
- **Evidence provenance:** The overwhelming majority of the literature is **aggregated disease-level** epidemiological, radiographic, and mechanistic data from endemic-region surveys (India, China) and animal studies, supplemented by individual case reports for atypical, non-endemic exposures (inhalant abuse, occupational, methoxyflurane, excessive toothpaste ingestion) rather than large EHR-derived cohorts.

## 2. Etiology

### 2a. Disease causal factors
Skeletal fluorosis is fundamentally an **environmental/toxicological** disease, not a Mendelian genetic disorder — the causal factor is chronic excess systemic fluoride intake exceeding the body's excretory (renal) capacity, leading to net fluoride retention in bone mineral. There is no single causal gene; genetic factors instead modulate individual **susceptibility** to a given fluoride dose (see below).

### 2b. Risk factors

**Environmental/exposure risk factors** (the dominant category):
- **Groundwater fluoride contamination** — geogenic fluoride from fluoride-bearing minerals (fluorite, apatite, mica) leaching into groundwater in arid/semi-arid regions with high evapotranspiration and alkaline, calcium-poor aquifers (Rift Valley belt — Ethiopia, Kenya, Tanzania, Uganda, Eritrea, Djibouti — plus India, China, Sri Lanka, Türkiye). WHO's drinking-water guideline value is **1.5 mg/L**; concentrations above this are associated with dental fluorosis, and total fluoride intake **>6 mg/day** is associated with crippling skeletal fluorosis (WHO guidance; search results above).
- **Brick tea / instant tea consumption** — tea plants bioaccumulate fluoride from soil/air (up to 98% of ambient fluoride can be sequestered in leaves), and brick tea (made from older leaves/stalks) is markedly higher in fluoride than leaf tea; "brick-tea-type fluorosis" is a distinct, well-described etiologic subtype endemic to Tibetan, Mongolian, and other pastoralist populations in China (PMID:39824337; PMC4728115).
- **Indoor coal-burning** — combustion of high-fluoride coal for cooking/heating in unventilated homes in southwestern China causes fluoride-laden smoke exposure and food contamination (crops dried over open coal fires), producing pediatric skeletal fluorosis (PMC2778178).
- **Occupational/industrial exposure** — aluminum smelting (cryolite/fluoride aerosols), phosphate fertilizer manufacturing, and other fluoride-emitting industries (PMC2993488, Czechoslovakia occupational cohort).
- **Iatrogenic/consumer sources** — chronic methoxyflurane analgesic use (metabolized to inorganic fluoride), excessive fluoridated toothpaste ingestion, and inhalant abuse of fluorinated hydrocarbon computer-cleaner propellants (difluoroethane) are documented non-endemic causes (PMC7336600, JBMR Plus 2024 ziae032).
- **Age, sex** — Radiographic changes are most pronounced in middle age (40–60 years); several Indian endemic-village surveys report higher prevalence in males (e.g., 56.9% male vs 43.1% female skeletal fluorosis in Vidharbha region, Maharashtra), likely reflecting greater outdoor water/occupational intake and possibly body-size/metabolic differences (PMC2940190).
- **Nutritional status** — low dietary calcium and protein-calorie malnutrition increase susceptibility to fluoride's skeletal effects by increasing fractional intestinal fluoride absorption and reducing competitive calcium binding.

**Genetic risk/modifier factors** (susceptibility, not causation):
- **ESR1** (estrogen receptor α) polymorphism **rs9340799**: the G allele is reported **protective** against brick-tea-type skeletal fluorosis in a multi-ethnic Chinese cohort (Tibetan, Kazakh, Mongolian, Russian) (PMID:39824337).
- **COL1A1** polymorphism **rs1800012**: the T allele confers **significantly higher risk** of skeletal fluorosis, an effect most pronounced in Russian men in the same cohort (PMID:39824337).
- Animal (mouse strain) data corroborate a genetic component: **A/J** mice are a "susceptible" strain and **129P3/J** a "resistant" strain for fluoride-induced skeletal/dental effects, with strain-dependent bone fluoride incorporation and proteomic responses even at low fluoride doses (PMID:16920415; PMC4263599).

### 2c. Protective factors
- Adequate **dietary calcium and vitamin D** intake reduces net skeletal fluoride uptake and, in mouse models, alleviates dental and skeletal fluorosis while preserving elemental (Ca/P) homeostasis (PMID:33057951).
- The **ESR1 rs9340799 G allele** (above) is a genetic protective variant in the tea-fluorosis context.
- Public-health **defluoridation of drinking water** (see Prevention) is the principal population-level protective intervention.

### 2d. Gene–environment interactions
The COL1A1/ESR1 findings above are explicitly framed as gene–environment interactions: susceptibility differs by ethnicity and appears to be **modified by tea fluoride intake, sex, and age** — i.e., the same genotype confers different risk depending on exposure route/dose (PMID:39824337). Mouse-strain data similarly show that a fixed environmental fluoride dose produces markedly different bone fluoride incorporation and proteomic/skeletal responses depending on genetic background (PMID:16920415).

## 3. Phenotypes

### Symptoms / clinical signs (with suggested HPO terms)
| Phenotype | Notes | Suggested HP term |
|---|---|---|
| Persistent joint/back pain, "resting pain," unaffected by weather | Early, hallmark symptom; ≥3 regions (major limb joints, neck, lower back) is a diagnostic criterion | HP:0002829 (Arthralgia) / HP:0003418 (Back pain) |
| Restricted joint mobility / stiffness | Progresses with disease stage | HP:0001376 (Limitation of joint mobility) / HP:0001387 (Joint stiffness) |
| Diffuse osteosclerosis | Radiographic hallmark | HP:0100774 (Osteosclerosis) |
| Skeletal exostoses / bony outgrowths | | HP:0100777 (Exostoses) |
| Ligamentous/tendon ossification (interosseous membrane, posterior longitudinal ligament, ligamentum flavum) | Drives neurologic compression | HP:0011800 (Midline sternotomy) *n/a* — better: HP:0002758 (Osteoarthritis) not exact; consider generic HP:0040068 (Abnormality of limb bone) plus free-text for ligament ossification (no precise HPO term for DISH-like ligament calcification exists; closest is HP:0002758-adjacent or ontology gap — record as free text/qualifier) |
| Spinal rigidity / kyphosis | | HP:0002808 (Kyphosis) |
| Genu valgum/varum (children) | Reported in pediatric coal-smoke fluorosis | HP:0002857 (Genu varum) / HP:0002857 |
| Spastic quadriparesis (advanced/neurologic disease) | Due to cervical cord compression | HP:0002510 (Spastic tetraparesis) |
| Radiculopathy / paresthesia | | HP:0009830 (Peripheral neuropathy) |
| Urinary incontinence (advanced neurologic disease) | Secondary to myelopathy | HP:0000020 (Urinary incontinence) |
| Muscle weakness | Reported on skeletal-muscle biopsy studies in endemic SF (PMID:10878791) | HP:0001324 (Muscle weakness) |
| Dental mottling (concurrent dental fluorosis) | Co-occurs when exposure begins before age 8 | HP:0009758 (Enamel hypoplasia) / dental fluorosis-specific term outside core HPO |

### Laboratory abnormalities
- **Elevated urinary fluoride** — the primary chemical biomarker; recent exposure reflected within 1–3 weeks, with reported values of ~15–20 ppm in affected humans/animals vs. 2–6 ppm normal (comparative veterinary literature; PMC search results).
- **Bone-ash fluoride concentration** (from biopsy) — considered the gold-standard definitive diagnostic measure, but invasive and rarely performed clinically.
- **Elevated serum PTH** with chronic fluoride exposure (secondary/tertiary hyperparathyroidism-like state; PMC8584317).
- **Alkaline phosphatase** elevation reflecting high bone turnover.
- Serum fluoride itself is **not reliably diagnostic** ("serum parameters rarely help in the diagnosis" — search synthesis above), because it reflects only very recent intake, not cumulative skeletal burden.

### Phenotype characteristics
- **Onset:** Adult-onset in most endemic (waterborne) cases after years to decades of cumulative exposure; pediatric-onset described in indoor coal-burning fluorosis in southwestern China (PMC2778178) and rare acute/subacute cases from inhalant abuse or methoxyflurane over months.
- **Severity/progression:** Progressive with cumulative dose and duration; graded by China's national standard **WS/T192-2021** into **Grade I** (symptoms, no radiographic/physical signs), **Grade II** (typical clinical/radiographic manifestations, retains some work capacity), and **Grade III** (loss of work capacity/crippling disease) (search synthesis).
- **Frequency of neurologic involvement:** Neurologic complications (myelopathy ± radiculopathy) occur in an estimated **5–10%** of skeletal fluorosis cases, typically after >4 ppm fluoride exposure for **>10 years**; among those with neurologic disease, myelopathy alone accounts for ~72% and myelopathy+radiculopathy ~28% (PMID:2172892, Neurology India review).

### Quality of life impact
Skeletal fluorosis causes "severe crippling disease which impairs the health-related quality of life in affected subjects," with case-report literature describing prolonged, sometimes decade-long, disability (search synthesis of ScienceDirect case-series review and JBMR "Recovery from Skeletal Fluorosis" case, PMID:17014382). No disease-specific EQ-5D/SF-36 dataset was identified in this search; QoL impact is documented narratively rather than via validated instrument scores in the literature surveyed.

## 4. Genetic/Molecular Information

Skeletal fluorosis is **not a monogenic Mendelian disease** — there is no single causal gene, OMIM entry, or pathogenic-variant classification analogous to a genetic disorder. Genetic information relevant to this entry is restricted to **susceptibility/modifier loci**:

- **ESR1** (estrogen receptor alpha; HGNC:3467) — variant rs9340799 (intron 1, "PvuII" site); G allele protective in brick-tea-type fluorosis (PMID:39824337). Functional consequence: modifies estrogen-responsive transcriptional regulation of osteoblast activity, consistent with estrogen's known role in bone remodeling.
- **COL1A1** (collagen type I alpha 1 chain; HGNC:2197) — variant rs1800012 (Sp1 binding site polymorphism, well known in osteoporosis genetics); T allele associated with increased skeletal fluorosis risk, especially in Russian men in the Chinese multi-ethnic cohort (PMID:39824337). This is the same polymorphism long studied for osteoporotic fracture risk, consistent with a shared collagen-matrix-quality mechanism.
- **COL1A2** (HGNC:2198) — polymorphism rs412777 studied in relation to **dental** (not skeletal) fluorosis in a Tunisian population (PMC10958825) — noted here as an adjacent finding but not directly established for the skeletal phenotype.
- No ClinVar/ClinGen pathogenic-variant curation applies (this is a toxic/environmental exposure disease, not a variant-driven disorder), so ACMG/AMP classification, allele-frequency-database (gnomAD), and somatic/germline-origin fields are **not applicable**.
- **Epigenetic changes** (directly mechanistic, see Section 6) are the most substantive "genetic/molecular" content specific to this disease: DNA hypermethylation of p16, BMP1, METAP2, MMP11, BACH1; hypomethylation of ERα; and dysregulation of microRNAs miR-486-3p, miR-4755-5p, Let-7c-5p, miR-29a, miR-27 (PMC8584317, detailed in Section 6).
- **Chromosomal abnormalities:** none reported; not a chromosomal disorder.

## 5. Environmental Information

- **Primary environmental factor:** chronic excess fluoride ingestion, principally via drinking water with geogenic fluoride contamination exceeding WHO's 1.5 mg/L guideline (search synthesis; PMID citations above). ECTO/ENVO-relevant exposure route: ingestion of fluoride-contaminated water.
- **Dietary/lifestyle factor:** habitual consumption of brick tea or instant tea concentrate (documented reversal after tea cessation/reduction — ScienceDirect S237606052030465X, "long-term follow-up after reduction and discontinuation of tea").
- **Occupational exposure:** aluminum electrolytic production, phosphate fertilizer manufacture, and other fluoride/hydrogen-fluoride-emitting industrial processes (PMC2993488).
- **Indoor air pollution:** fluoride-laden smoke from unventilated indoor coal-burning stoves, compounded by crop-drying practices over open coal fires that further contaminate food with fluoride (PMC2778178, southwestern China pediatric cohort).
- **Consumer product/iatrogenic exposure:** difluoroethane-propelled computer-duster inhalant abuse (PMC7336600); chronic methoxyflurane analgesic use (JBMR Plus ziae032); excessive fluoridated toothpaste ingestion.
- **Infectious agents:** not applicable — skeletal fluorosis has no infectious etiology.
- **Geographic/climatic modifiers:** arid and semi-arid climates with high evapotranspiration concentrate fluoride in groundwater; the East African Rift Valley, the Indian subcontinent, and northern/southwestern China are the classic endemic belts (search synthesis; PMC13275634 "Global groundwater contamination by geogenic fluoride").

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating exposure → clinical manifestation)

1. **Chronic excess fluoride intake** (contaminated water, brick tea, coal smoke, industrial exposure, or iatrogenic source) **leads to** sustained elevation of systemic fluoride ion (F⁻) levels beyond renal excretory capacity.
2. Elevated systemic F⁻ **results in** progressive fluoride deposition into the hydroxyapatite mineral lattice of bone, substituting for hydroxyl groups to form fluorapatite — fluoride's high calcium affinity drives this preferential skeletal sequestration (PMID:3295994).
3. Bone-incorporated fluoride, together with circulating fluoride acting on bone-lining cells, **triggers a shift in local signaling** in osteoblasts and osteocytes: fluoride activates **Wnt/β-catenin signaling** (by suppressing the inhibitors SOST and Dkk-1, allowing β-catenin nuclear accumulation) and **Hedgehog signaling** (via increased Indian Hedgehog → Smoothened → Gli2), both converging on upregulation of **Runx2**, the master osteoblast transcription factor, while fluoride simultaneously **suppresses Notch signaling** (decreased Notch-3/Jagged-1), removing an inhibitory brake on osteoblast proliferation (PMC8584317).
4. This signaling shift **leads to** excessive, disorganized osteoblast proliferation and matrix (collagen I, alkaline phosphatase, osteonectin) synthesis, mediated in part by fluoride-induced Akt/GSK-3β phosphorylation that stabilizes β-catenin (PMID:24300170).
5. In parallel, elevated **serum PTH** (a systemic response to chronic fluoride/calcium perturbation) **results in** further downregulation of SOST and upregulation of RANKL, coupling excess osteoblastic activity to increased osteoclastogenesis via the **osteocyte-driven RANK–JNK–NFATc1** pathway (PMID:32156525) — this is the mechanistic basis for the disease's hallmark of **accelerated bone turnover** rather than pure bone formation.
6. At high, sustained fluoride concentrations, cellular defenses are overwhelmed: fluoride **induces oxidative stress** (ROS accumulation overwhelming the Nrf2-ARE antioxidant response), **endoplasmic reticulum stress** (PERK-mediated unfolded protein response, upregulated BiP/GRP78, ATF4), and **mitochondria-mediated apoptosis with increased mitophagy in osteocytes** (Springer 2023 study), **leading to** disordered osteocyte viability and further dysregulated bone remodeling signals (PMC8584317; Springer/Biological Trace Element Research).
7. Concurrently, fluoride **inhibits vitamin D hydroxylation**, decreasing active vitamin D bioavailability and **impairing intestinal calcium/phosphorus absorption**, which — together with fluoride's direct calcium sequestration in bone — **disturbs systemic phosphorus/calcium balance** (search synthesis).
8. **Epigenetic reprogramming** accompanies and reinforces these changes: hypermethylation of the cell-cycle checkpoint gene **p16** (reducing its expression and removing G1/S checkpoint control) and of **BMP1, METAP2, MMP11, BACH1**, alongside hypomethylation of **ERα**, and dysregulation of microRNAs (**miR-486-3p↓, miR-4755-5p↓, Let-7c-5p↓** → increased Cyclin D1 → osteoblast proliferation; **miR-29a↑** → decreased Dkk-1 → enhanced Wnt signaling; **miR-27** positively correlated with β-catenin), collectively **sustaining** the pro-osteogenic, hyperproliferative osteoblast phenotype over years of chronic exposure (PMC8584317).
9. The net structural consequence — cumulative over years to decades — is **diffuse osteosclerosis, cortical thickening, exostoses, and ossification of ligaments/tendons (interosseous membranes, posterior longitudinal ligament, ligamentum flavum, entheses)**, radiographically the disease's defining feature (search synthesis; AJR PMID reference; Radiopaedia).
10. In the spine specifically, this ligamentous/vertebral ossification and osteophytosis **narrows the spinal canal and intervertebral foramina**, which **leads to (branch point)** either (a) **mechanical/compressive myelopathy and radiculopathy** via direct cord/root compression, occurring in ~5–10% of cases after >10 years of high (>4 ppm) exposure (PMID:2172892), progressing in advanced cases to **vascular/ischemic secondary injury** of the cord, manifesting clinically as spastic quadriparesis, spasms, and urinary incontinence; or (b) purely **peripheral musculoskeletal disease** — joint stiffness, restricted mobility, and chronic pain — without neurologic compromise, in the majority of affected individuals.
11. In cartilage, a **separate downstream branch** occurs in chondrocytes: fluoride-induced oxidative stress **suppresses the pentose phosphate pathway** (decreased NADPH/GSH) and **downregulates PI3K/Akt/mTOR** while activating autophagy (increased Beclin-1, LC3) and upregulating MMP-13/RANKL, **resulting in** chondrocyte apoptosis and matrix degradation, contributing to joint/cartilage pathology alongside the primary bone-driven mechanism (PMID:39959228, PMID:41601087).

### Detail by category

- **Molecular pathways (KEGG/Reactome-relevant):** Wnt signaling pathway (activated), Notch signaling pathway (suppressed), Hedgehog signaling pathway (activated in osteoblasts; pro-apoptotic in chondrocytes via Bax↑/Bcl-2↓), PI3K-Akt signaling pathway (activated in osteoblasts, suppressed in chondrocytes), RANK/RANKL/OPG axis (shifted toward increased RANKL), IL-17A pathway, MAPK/NQO1/HO1 pathway, PTH/PTHrP signaling, insulin/IGF-1 signaling (PMC8584317; PubMed synthesis).
- **Cellular processes (GO-relevant):** osteoblast proliferation and differentiation (GO:0002062 chondrocyte differentiation; GO:0030282 bone mineralization), osteoclast differentiation (GO:0030316), apoptosis (GO:0006915), autophagy (GO:0006914), mitophagy, oxidative stress response (GO:0006979), unfolded protein response/ER stress (GO:0030968), chronic inflammation.
- **Protein dysfunction:** no single misfolded protein; instead, fluoride acts as an enzymatic/ionic perturbant — inhibiting osteoblastic acid phosphatase (proposed mitogenic mechanism, ScienceDirect 0026049589902321), altering collagen (COL1A1) matrix quality, and disrupting vitamin-D-hydroxylase enzymatic activity.
- **Metabolic changes:** disturbed calcium-phosphorus homeostasis; impaired vitamin D activation; altered bone mineral (fluorapatite substitution for hydroxyapatite) reducing mechanical strength despite increased radiographic density.
- **Immune system involvement:** chronic low-grade inflammation and IL-17A pathway activation are implicated but are secondary/contributory rather than primary autoimmune mechanisms (PMC8584317).
- **Tissue damage mechanisms:** oxidative stress (ROS/MDA elevation), apoptosis, mitochondrial dysfunction/mitophagy in osteocytes, and secondary vascular/ischemic injury to compressed neural tissue.
- **Biochemical abnormalities:** elevated PTH, altered alkaline/acid phosphatase activity, disrupted calcium/phosphate/vitamin D axis, calcineurin (CaN) activation promoting osteoclastogenesis.
- **Epigenetic changes:** detailed above (DNA methylation of p16, BMP1, METAP2, MMP11, BACH1, ERα; miRNA dysregulation).
- **Molecular profiling:** proteomic studies (iTRAQ, Wistar rat serum) have identified candidate serum protein biomarkers of fluorosis (PMC5085677); murine bone proteomics show 36 differentially abundant proteins even at low-dose fluoride exposure in susceptible (A/J) mice (PMC4263599). No large-scale human transcriptomic/single-cell atlas specific to skeletal fluorosis was identified in this search.

### Suggested GO terms
- GO:0030282 (bone mineralization)
- GO:0001649 (osteoblast differentiation)
- GO:0030316 (osteoclast differentiation)
- GO:0060070 (canonical Wnt signaling pathway)
- GO:0007219 (Notch signaling pathway)
- GO:0007224 (smoothened signaling pathway, Hedgehog)
- GO:0043491 (protein kinase B signaling, PI3K/Akt)
- GO:0006915 (apoptotic process)
- GO:0006979 (response to oxidative stress)
- GO:0034976 (response to endoplasmic reticulum stress)
- GO:0006914 (autophagy)

### Suggested CL terms
- CL:0000062 (osteoblast)
- CL:0000137 (osteocyte)
- CL:0000092 (osteoclast)
- CL:0000138 (chondrocyte)

## 7. Anatomical Structures Affected

- **Organ level:** primary — the skeletal system (axial > appendicular skeleton, especially spine, pelvis, forearm), teeth (concurrent dental fluorosis when exposure begins before age 8). Secondary/complication involvement — spinal cord and peripheral nerve roots (compressive myelopathy/radiculopathy in advanced disease), skeletal muscle (biopsy studies document muscle changes in endemic SF, PMID:10878791), and, per some reviews, renal involvement contributing to fluoride retention itself (kidneys clear fluoride; impaired renal function reduces excretion and worsens skeletal accumulation).
- **Body systems:** skeletal, nervous (compressive), and to a lesser extent muscular systems; endocrine system implicated via PTH/vitamin D axis perturbation.
- **Tissue/cell level:** bone (cortical and trabecular), articular/enthesis connective tissue and ligaments (interosseous membrane, posterior longitudinal ligament, ligamentum flavum — sites of pathological ossification), cartilage (chondrocyte apoptosis/matrix degradation), and spinal neural tissue (secondary compression injury).
- **Cell populations targeted:** osteoblasts (hyperactivated), osteocytes (apoptosis/mitophagy), osteoclasts (RANK-pathway-driven differentiation), chondrocytes (apoptosis, autophagy).
- **Subcellular level:** mitochondria (ROS generation, mitophagy in osteocytes), endoplasmic reticulum (UPR/ER stress via PERK-ATF4), nucleus (β-catenin nuclear translocation, epigenetic/DNA methylation changes).
- **Localization (UBERON):** vertebral column (UBERON:0002298 vertebral column), pelvis, forearm bones, sacroiliac joint, spinal cord (UBERON:0002240), long bones. Ossification is generalized/bilateral rather than lateralized.

**Suggested UBERON terms:** UBERON:0001474 (bone element), UBERON:0002240 (spinal cord), UBERON:0002298 (vertebral column), UBERON:0002228 (rib), UBERON:0002417 (posterior longitudinal ligament — if available), UBERON:0004123 (femur), UBERON:0001103 (diaphragm — n/a, remove if not applicable).

## 8. Temporal Development

- **Onset:** Typically adult-onset (years to decades of cumulative exposure) in endemic waterborne fluorosis; pediatric-onset described specifically in indoor coal-smoke fluorosis in China (PMC2778178); rare subacute-onset (months) cases from inhalant abuse or high-dose methoxyflurane exposure.
- **Onset pattern:** Insidious/chronic in the overwhelming majority of cases; subacute in iatrogenic/abuse-related cases.
- **Progression / staging:** Chinese national standard WS/T192-2021 defines three grades — **Grade I** (symptomatic, no radiographic/physical signs), **Grade II** (typical clinical and radiographic manifestations, retains partial work capacity), **Grade III** (loss of work capacity, "crippling" disease) (search synthesis). Radiographically, changes are described along a spectrum: early sand-like/granular trabecular thickening → osteosclerosis, osteopenia in some regions, diaphyseal widening, intermittent growth-arrest lines, and soft-tissue/ligamentous ossification, with the most pronounced structural changes typically appearing in **middle age (40–60 years)** (search synthesis of radiographic reviews).
- **Progression rate:** Slow and dose/duration-dependent; neurologic complications generally require **>10 years** of exposure at **>4 ppm** fluoride.
- **Course pattern:** Chronic and generally progressive with continued exposure; not classically relapsing-remitting.
- **Reversibility:** Cessation of exposure can lead to gradual improvement/reversal of biochemical and even some radiographic abnormalities, but recovery is **extremely slow** — potentially requiring years to decades — consistent with fluoride's estimated ~**7-year half-life** in bone; a well-documented American case showed "considerable correction" only after **nearly a decade** of source removal (toothpaste) (PMID:17014382). No large systematic reversibility dataset exists; evidence is case-based.
- **Critical periods:** Exposure before ~age 8 additionally risks concurrent dental fluorosis (enamel formation window); no other defined critical developmental window is described for the skeletal phenotype beyond cumulative dose-duration.

## 9. Inheritance and Population

- **Inheritance pattern:** Not applicable in the Mendelian sense — skeletal fluorosis is an acquired toxic/environmental disease. "Inheritance" language does not apply; susceptibility is polygenic/multifactorial (see COL1A1/ESR1 modifiers, Section 4), analogous to a **gene-by-environment susceptibility trait** rather than a classic inherited disorder. Penetrance, expressivity, anticipation, germline mosaicism, founder effects, and carrier frequency are not meaningful concepts here except insofar as modifier-allele frequency (e.g., COL1A1 rs1800012, ESR1 rs9340799) differs by ethnicity, as documented in the Tibetan/Kazakh/Mongolian/Russian comparison cohort (PMID:39824337).

- **Epidemiology:**
  - **Global burden:** UNICEF estimates fluorosis (dental + skeletal combined) is **endemic in at least 25 countries**, with **approximately 200 million people at health risk** from elevated groundwater fluoride; some reviews cite over 100 affected countries (search synthesis, PMC13275634). India and China are described as the two largest-affected countries.
  - **India (regional surveys):** Kankar district, Chhattisgarh — dental fluorosis prevalence 24.8%, skeletal fluorosis 6.0%. Vidharbha region, Maharashtra — skeletal fluorosis prevalence 56.9% in males, 43.1% in females among the surveyed endemic population (PMC2940190).
  - **China:** Fluorosis affects **28 provincial-level administrative regions and over 70,000 villages**, via three main pathways — coal-burning, drinking-water contamination, and brick-tea consumption (PMC13128821).
  - **Geographic distribution:** Endemic belts include the Indian subcontinent, northern/southwestern China, the East African Rift Valley (Ethiopia, Kenya, Tanzania, Uganda, Eritrea, Djibouti), parts of the Middle East (Jordan, Lebanon, Israel), Sri Lanka, and Türkiye (search synthesis, ResearchGate distribution figure, PMC13275634).
  - **Sex ratio:** Male predominance reported in at least one Indian endemic-village study (see above); mechanistic basis (behavioral/occupational exposure vs. biological susceptibility) not fully resolved in the sources reviewed.
  - **Age distribution:** Peak radiographic severity in the 40–60 year age range, reflecting cumulative dose; pediatric cases occur specifically in the coal-smoke exposure pathway.

## 10. Diagnostics

- **Diagnostic criteria (composite):** (1) residence history in a fluorosis-endemic area or a documented alternative fluoride source; (2) characteristic clinical symptoms — persistent resting pain in ≥3 regions (major limb joints, neck, lower back) unaffected by season, and/or restricted joint mobility or secondary neurologic impairment; (3) characteristic radiographic findings; (4) elevated urinary (and/or bone) fluoride. Diagnosis rests on this combination with exclusion of radiographic mimics (search synthesis).
- **Imaging (primary diagnostic modality):**
  - Plain radiography remains the mainstay: hallmark findings are **generalized osteosclerosis, diffuse periostitis, entheso-/ligamentous ossification (interosseous membranes, posterior longitudinal ligament, ligamentum flavum), and sacroiliac changes without erosions** — distinguishing SF from inflammatory spondyloarthropathies (search synthesis; AJR classic series of 127 patients).
  - Early disease: sand-like/granular trabecular thickening at trabecular junctions.
  - A novel structured scoring system, **FI-RADS** (Fluorosis Imaging-Reporting and Data System), has been proposed (2026) combining imaging with clinical/biochemical analysis for standardized severity scoring (PMC13178315; PMID:42147921).
  - Advanced cases can radiographically mimic multiple myeloma on spinal MRI (PMC5117116).
- **Laboratory tests / biomarkers:**
  - **Urinary fluoride** — the principal chemical biomarker of recent/ongoing exposure (elevated to ~15–20 ppm vs. 2–6 ppm normal, cross-species comparative data).
  - **Bone-ash fluoride content** (biopsy) — gold-standard definitive test but invasive, rarely performed.
  - Serum fluoride is generally **not diagnostically useful** because it reflects only very recent intake.
  - Elevated **PTH**, elevated **alkaline phosphatase**, and disturbed calcium/phosphorus panels are supportive but nonspecific.
- **Genetic testing:** Not applicable as a diagnostic modality (no causal gene); COL1A1/ESR1 genotyping is a research tool for population-susceptibility studies, not clinical diagnosis.
- **Differential diagnosis:** Ankylosing spondylitis and diffuse idiopathic skeletal hyperostosis (DISH) are the principal radiographic mimics. Distinguishing features: AS shows complete sacroiliac joint fusion and "smooth-type" anterior spinal bony bridging; DISH shows anterior/posterior bony bridging around the SI joint without fusion and "candle-wax-type" bridging. The combination of diffuse osteosclerosis with periosteal reaction plus ligament/tendon mineralization should specifically prompt consideration of skeletal fluorosis and a focused exposure history (search synthesis, PMC9892029 comparative radiology study).
- **Other mimics** to exclude: renal osteodystrophy, osteopetrosis, Paget disease of bone, myelofibrosis, and (as noted) multiple myeloma on imaging alone.

## 11. Outcome / Prognosis

- **Mortality:** No direct disease-specific mortality/survival statistics (e.g., 5-year survival) were identified — skeletal fluorosis is not typically fatal per se, but severe neurologic complications (quadriparesis) carry major morbidity and disability risk.
- **Morbidity/disability:** Advanced (Grade III) disease causes loss of work capacity; the case-series literature explicitly frames the disease as a "continuing crippling challenge," with impaired health-related quality of life (search synthesis, ScienceDirect S2214624522000089).
- **Reversibility/recovery:** As detailed in Section 8, cessation of the fluoride source can allow gradual clinical, biochemical, and radiographic improvement, but recovery is slow (years, potentially matching bone fluoride's ~7-year half-life), and a well-documented case required nearly a decade for substantial correction after removing a toothpaste source (PMID:17014382). There are no systematic reversibility data across cohorts — this is characterized as an evidence gap in the literature itself.
- **Complications:** Compressive myelopathy/radiculopathy (5–10% of cases, see Section 3/6), joint ankylosis, secondary muscle changes, and (in the pediatric coal-smoke pathway) growth/limb deformities (e.g., genu varum/valgum).
- **Prognostic factors:** Total cumulative fluoride dose and duration of exposure are described as "the single most important factor" determining clinical course (search synthesis, PubMed abstract on endemic skeletal fluorosis); early removal of the fluoride source is the dominant modifiable prognostic factor, since no pharmacologic treatment reverses established disease.

## 12. Treatment

**There is no disease-modifying pharmacologic treatment for established skeletal fluorosis.** Management is source removal plus symptomatic/supportive care.

- **Primary intervention:** Identification and elimination of the fluoride source (switching water supply, discontinuing brick tea, ceasing occupational exposure, stopping inhalant abuse or methoxyflurane), which is the only intervention shown to allow gradual improvement (Section 8/11).
- **Pharmacotherapy (symptomatic):**
  - **NSAIDs** for pain and inflammation control (NCIT:C15986 Pharmacotherapy; specific agent class NCIT:C275/analgesic).
  - **Calcium and vitamin D supplementation** — mixed evidence in humans (largely minimal efficacy reported in clinical literature), but **effective in mouse models** at alleviating dental/skeletal fluorosis, reducing bone fluoride deposition, and normalizing elemental (Ca/P) homeostasis (PMID:33057951; evidence_source: MODEL_ORGANISM for the murine result vs. HUMAN_CLINICAL for the largely negative human experience).
- **Surgical/interventional:**
  - **Decompressive laminectomy** for relief of neurologic deficits from spinal cord/nerve root compression (NCIT:C15329 Surgical Procedure) — but note a documented case of **recurrent fluorotic cervical compressive myelopathy 20 years after laminectomy**, illustrating that surgery addresses mechanical compression without halting the underlying ossifying process if exposure continues (Surgical Neurology International case report).
  - **Osteoplasty** for ankylosis of appendicular joints.
- **Supportive/rehabilitative care:** Physical therapy (NCIT:C15302) and general symptomatic musculoskeletal pain management, particularly important during a prolonged "withdrawal phase" after source removal that may last many weeks.
- **Experimental/research-stage:** No specific ongoing registered clinical trials targeting skeletal fluorosis treatment were identified in this search (ClinicalTrials.gov search returned no disease-specific NCT records); a 2026 "China Fluorosis Cohort (CFC)" randomized trial explores drug–lifestyle interventions but targets **cardiovascular-metabolic outcomes** in fluorosis patients rather than the skeletal phenotype itself (Frontiers in Pharmacology, 2026).
- **Treatment outcomes:** Human calcium/vitamin D trials show minimal efficacy in established disease; surgical decompression provides mechanical relief but does not reverse the underlying osteosclerotic process.

**Suggested NCIT terms:** NCIT:C15986 (Pharmacotherapy), NCIT:C15329 (Surgical Procedure), NCIT:C15302 (Physical Therapy), NCIT:C15747 (Supportive Care).
**Suggested CHEBI terms for the causal/therapeutic agents:** CHEBI:17051 (fluoride ion, the causal agent), CHEBI:28741 (sodium fluoride), CHEBI:22984 (calcium(2+); for calcium supplementation), CHEBI:27300 (vitamin D).

## 13. Prevention

- **Primary prevention (population level):**
  - **Defluoridation of drinking water** to bring fluoride concentration to WHO's guideline ≤1.5 mg/L — via technologies such as octacalcium-phosphate/fluorapatite transformation systems and household-scale defluoridators (demonstrated in Tanzania to reduce 21 mg/L source water to below the WHO limit within 2 hours) (PMC7687156, PMC6706606).
  - **Alternative/safe water source provision** in endemic villages.
  - **Reduction/substitution of brick tea consumption** in high-risk pastoralist populations, with documented reversal of biochemical/clinical parameters after tea reduction or cessation (ScienceDirect S237606052030465X).
  - **Improved ventilation and alternative cooking fuel** to reduce indoor coal-smoke exposure, plus altered crop-drying practices (not drying food over open coal fires) in the southwestern China pediatric-fluorosis context.
  - **Occupational hygiene controls** (ventilation, personal protective equipment, exposure monitoring) in fluoride-emitting industries.
- **Secondary prevention:** Population screening in endemic areas via urinary fluoride testing and radiographic surveillance to detect early (Grade I) disease before irreversible skeletal changes accrue; public health surveys of the type reviewed above (e.g., Chhattisgarh, Vidharbha, Andhra Pradesh school-children studies) serve this function.
- **Tertiary prevention:** Early source removal upon diagnosis to halt disease progression and permit the slow reversal process described in Sections 8/11; symptomatic management to prevent secondary complications (e.g., early recognition of neurologic signs to prompt timely decompressive surgery before irreversible cord injury).
- **Counseling:** Public health education in endemic communities regarding water source safety and tea consumption patterns; occupational counseling in at-risk industries.
- **Regulatory/public health standards:** WHO drinking-water guideline value of 1.5 mg/L fluoride, adopted as national standard in most countries (some countries with particular challenges set different limits) (search synthesis).

## 14. Other Species / Natural Disease

- **Taxonomy of affected species:** Skeletal fluorosis occurs naturally in numerous species exposed to high-fluoride water, forage, or industrial contamination — most notably **cattle** (*Bos taurus*, NCBITaxon:9913), but also documented in horses, sheep, and other livestock, as well as wildlife in fluoride-contaminated environments (Merck Veterinary Manual; veterinaryworld.org review).
- **Natural disease in veterinary species (cattle):** Skeletal fluorosis in cattle presents with **hoof deformity, mandibular lesions, bone/joint enlargement, exostoses, ligament calcification, stiffness, and lameness**, at drinking-water fluoride concentrations of **≥2.8 mg/L** (search synthesis, veterinaryworld.org, cpdsolutions.co.za review). Diagnostic thresholds: bone fluoride concentration of **1605–2794 mg/kg** (age-dependent) for chronic fluorosis; urinary fluoride **<5 ppm normal**, **20–30 ppm borderline toxicity**, **>35 ppm** with systemic signs.
- **Causes in livestock:** deep-well/artesian bore water, industrial (e.g., aluminum smelter, phosphate fertilizer plant) contamination of pasture/forage, and high soil fluoride affecting fodder crops.
- **Veterinary relevance:** Fluorosis is an economically significant livestock disease in endemic regions (India, parts of Africa) causing reduced productivity, lameness, and premature culling; it is diagnosed via the same combination of history, clinical signs, radiography, and bone/urine fluoride analysis used in humans (Livesey, *In Practice*, 2011, doi:10.1136/inp.d6078).
- **Comparative pathology:** The core pathophysiology — fluoride substitution into hydroxyapatite, osteosclerosis, exostosis formation, ligament calcification — is conserved across mammalian species, supporting cattle and mice as translationally relevant natural/experimental models. Dental fluorosis is separately documented as co-occurring in livestock sharing contaminated water/pasture with human populations (e.g., Gihaya Island, Lake Kivu, Rwanda cohort, PMC8686390).
- **Zoonotic potential:** Not applicable — this is a shared environmental toxic exposure, not a transmissible infectious disease.
- **OMIA:** No specific OMIA (Online Mendelian Inheritance in Animals) entry was identified for fluorosis in this search, consistent with its non-Mendelian, acquired-toxicological nature; direct OMIA database consultation would be needed to confirm absence of an entry.

## 15. Model Organisms

- **Mouse (*Mus musculus*, NCBITaxon:10090)** — the dominant experimental model:
  - **Genetic/strain models:** Comparative dosing (0, 25, 50, 100 ppm F in food/water) across three inbred strains with differential enamel-fluorosis susceptibility — **A/J** (susceptible), **129P3/J** (resistant), **SWR/J** (intermediate) — shows strain-dependent, dose-concordant increases in femoral and vertebral fluoride concentration, establishing a genetic-background model for susceptibility (PMID:16920415).
  - **Proteomic follow-up:** 8-week exposure to 0/10/50 ppm F in A/J vs. 129P3/J mice shows bone proteomic changes (36 differentially abundant proteins) even at low dose in the susceptible strain (PMC4263599) — useful for identifying candidate mechanistic biomarkers.
  - **Intervention model:** Calcium/vitamin D supplementation in a fluorosis mouse model **effectively alleviates dental and skeletal fluorosis and retains elemental homeostasis** (PMID:33057951) — the strongest available "rescue" evidence for this intervention, notably stronger than the human clinical experience, an instructive human/model discrepancy for a `HUMAN_MODEL_MISMATCH`-type discussion.
  - **Method development:** A murine model using hexamethyldisiloxane-facilitated diffusion with ion-selective electrode measurement enables age- and dose-dependent fluoride quantification across serum, bone, and teeth (PMID:42667223), supporting future dose-response and toxicokinetic studies.
  - **Developmental-age model:** Classic studies (PMID:1058056, PMID:1060516, PMID:1067906) examined age-of-exposure effects on incisor/bone fluoride incorporation and the influence of dietary salt intake on fluoride uptake in mice.
- **Rat (*Rattus norvegicus*, NCBITaxon:10116):** Wistar rats treated with sodium fluoride used for iTRAQ-based serum proteomic biomarker discovery relevant to fluorosis mechanism/candidate biomarkers (PMC5085677); primary rat osteoblast cultures used to demonstrate fluoride-induced Wnt/β-catenin activation via Akt/GSK-3β (PMID:24300170).
- **Cattle (*Bos taurus*)** as a **natural disease model** (Section 14) — valuable for translational relevance given spontaneous, environmentally acquired disease closely paralleling the human condition, though whole-organism veterinary studies are largely observational rather than mechanistic/genetic.
- **Model limitations:** Rodent models require relatively high fluoride doses (tens to over 100 ppm) delivered over weeks to reproduce skeletal changes analogous to those developing over years to decades of low-level (~1.5–10 ppm water; higher via tea/coal) human exposure — a scale/dose-rate divergence to note explicitly when using rodent data to support human mechanism claims. No organoid, iPSC, zebrafish, or single-cell/spatial-transcriptomic fluorosis-specific model was identified in this search, representing an apparent gap in the current published model landscape relative to other skeletal disorders.
- **Resources:** MGI (Mouse Genome Informatics) for strain background data; no dedicated fluorosis-specific model registry was identified.

---

## Summary of Suggested Ontology Term Bindings

| Category | Term | ID |
|---|---|---|
| Disease | Skeletal fluorosis | MONDO:0400003 |
| Disease (related, distinct) | Dental fluorosis | MONDO:0006722 |
| Phenotype | Osteosclerosis | HP:0100774 |
| Phenotype | Exostoses | HP:0100777 |
| Phenotype | Limitation of joint mobility | HP:0001376 |
| Phenotype | Spastic tetraparesis | HP:0002510 |
| Phenotype | Kyphosis | HP:0002808 |
| Gene (modifier) | ESR1 | hgnc:3467 |
| Gene (modifier) | COL1A1 | hgnc:2197 |
| Gene (modifier, dental) | COL1A2 | hgnc:2198 |
| Chemical (causal agent) | fluoride | CHEBI:17051 |
| Chemical | sodium fluoride | CHEBI:28741 |
| GO (pathway) | canonical Wnt signaling pathway | GO:0060070 |
| GO (pathway) | Notch signaling pathway | GO:0007219 |
| GO (pathway) | response to oxidative stress | GO:0006979 |
| Cell type | osteoblast | CL:0000062 |
| Cell type | osteocyte | CL:0000137 |
| Cell type | osteoclast | CL:0000092 |
| Cell type | chondrocyte | CL:0000138 |
| Anatomy | vertebral column | UBERON:0002298 |
| Anatomy | spinal cord | UBERON:0002240 |
| Treatment | Pharmacotherapy | NCIT:C15986 |
| Treatment | Surgical Procedure | NCIT:C15329 |
| Treatment | Physical Therapy | NCIT:C15302 |
| Organism (model) | Mus musculus | NCBITaxon:10090 |
| Organism (natural disease) | Bos taurus | NCBITaxon:9913 |

## Notable Evidence Gaps (flagged for curation)

1. **Reversibility/prognosis** is documented almost entirely through single case reports (e.g., PMID:17014382), not cohort data — the literature itself states "there are no data regarding its reversibility" at a systematic level.
2. **No specific registered clinical trials** target skeletal-fluorosis treatment directly (ClinicalTrials.gov search returned none disease-specific); the one identified 2026 trial (China Fluorosis Cohort) targets cardiovascular-metabolic, not skeletal, endpoints.
3. **Human calcium/vitamin D efficacy is discordant with the mouse model result** (minimal human efficacy vs. clear murine rescue, PMID:33057951) — a candidate `HUMAN_MODEL_MISMATCH` discussion point.
4. **No QoL instrument (EQ-5D/SF-36) score data** specific to skeletal fluorosis were located; impact is described narratively only.
5. **OMIA entry status** for veterinary fluorosis was not confirmed/denied definitively and would need direct OMIA database consultation.

---

**Sources:**
- [Progress of Signaling Pathways, Stress Pathways and Epigenetics in the Pathogenesis of Skeletal Fluorosis (PMC8584317 / PMID:34769866)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8584317/)
- [Environmental fluoride exposure and bone metabolism: Molecular pathways and health implications (PMID:42336527)](https://pubmed.ncbi.nlm.nih.gov/42336527/)
- [The continuing crippling challenge of skeletal fluorosis – Case series and review of literature](https://www.sciencedirect.com/science/article/pii/S2214624522000089)
- [Skeletal fluorosis in humans: a review of recent progress (PMID:3295994)](https://pubmed.ncbi.nlm.nih.gov/3295994/)
- [MONDO:0400003 — Ontology Lookup Service](https://www.ebi.ac.uk/ols4/ontologies/mondo/entities/http:%2F%2Fpurl.obolibrary.org%2Fobo%2FMONDO_0400003)
- [ICD-10-CM M85.1 series — icd10data.com](https://www.icd10data.com/ICD10CM/Codes/M00-M99/M80-M85/M85-/M85.159)
- [Effect of fluoride on osteocyte-driven osteoclastic differentiation (PMID:32156525)](https://pubmed.ncbi.nlm.nih.gov/32156525/)
- [Different Effects of Fluoride Exposure on the Three Major Bone Cell Types](https://link.springer.com/article/10.1007/s12011-019-01684-9)
- [Apoptosis and Inflammation Involved with Fluoride-Induced Bone Injuries (PMC11313706)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11313706/)
- [Fluoride Exposure and Skeletal Fluorosis: a Systematic Review and Dose-response Meta-analysis](https://link.springer.com/article/10.1007/s40572-023-00412-9)
- [Child Skeletal Fluorosis from Indoor Burning of Coal in Southwestern China (PMC2778178)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2778178/)
- [Predicting skeletal fluorosis severity using machine learning across diverse fluoride-exposed populations in China (PMC13128821)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13128821/)
- [Assessment of Skeletal and Non-skeletal Fluorosis in Endemic Fluoridated Areas of Vidharbha Region, India (PMC2940190)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2940190/)
- [FI-RADS: an imaging-based scoring system for skeletal fluorosis (PMC13178315 / PMID:42147921)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13178315/)
- [Endemic fluorosis of the skeleton: radiographic features in 127 patients — AJR](https://www.ajronline.org/doi/abs/10.2214/ajr.162.1.8273699)
- [Neurological complications of endemic skeletal fluorosis, with special emphasis on radiculo-myelopathy (PMID:2172892)](https://pubmed.ncbi.nlm.nih.gov/2172892/)
- [Neurology of endemic skeletal fluorosis — Neurology India](https://journals.lww.com/neur/fulltext/2009/57010/neurology_of_endemic_skeletal_fluorosis.4.aspx)
- [Multiple Myeloma-Like Spinal MRI Findings in Skeletal Fluorosis (PMC5117116)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5117116/)
- [Fluorotic cervical compressive myelopathy, 20 years after laminectomy](https://surgicalneurologyint.com/surgicalint-articles/fluorotic-cervical-compressive-myelopathy-20-years-after-laminectomy-a-rare-event/)
- [Fluoride promotes osteoblastic differentiation through canonical Wnt/β-catenin signaling pathway (PMID:24300170)](https://pubmed.ncbi.nlm.nih.gov/24300170/)
- [Association between ESR1 and COL1A1 gene polymorphisms and skeletal fluorosis in Tibetan, Kazakh, Mongolian and Russian populations, China (PMID:39824337)](https://pubmed.ncbi.nlm.nih.gov/39824337/)
- [The genetic influence in fluorosis](https://www.sciencedirect.com/science/article/abs/pii/S1382668917302661)
- [The COL1A2 gene polymorphism among a Tunisian Population and Dental Fluorosis (PMC10958825)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10958825/)
- [Fluorosis in Cattle — veterinaryworld.org](https://veterinaryworld.org/Vol.3/November/Fluorosis%20in%20Cattle.pdf)
- [Diagnosis and investigation of fluorosis in livestock and horses — In Practice](https://bvajournals.onlinelibrary.wiley.com/doi/10.1136/inp.d6078)
- [Fluoride Poisoning in Animals — Merck Veterinary Manual](https://www.merckvetmanual.com/toxicology/fluoride-poisoning/fluoride-poisoning-in-animals)
- [Chronic Fluoride Exposure from Brick Tea Consumption Disrupts Bone Remodeling (PMID:42060046)](https://pubmed.ncbi.nlm.nih.gov/42060046/)
- [Skeletal Fluorosis Related to Habitual Tea Consumption: Long-Term Follow-Up](https://www.sciencedirect.com/science/article/pii/S237606052030465X)
- [Prevalence of Brick Tea-Type Fluorosis in the Tibet Autonomous Region (PMC4728115)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4728115/)
- [Skeletal fluorosis from the point of view of an occupational exposure in former Czechoslovakia (PMC2993488)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2993488/)
- [Skeletal Fluorosis: An Unusual Manifestation of Computer Cleaner Inhalant Abuse (PMC7336600)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7336600/)
- [Skeletal fluorosis secondary to methoxyflurane use for chronic pain — JBMR Plus](https://academic.oup.com/jbmrplus/article/8/5/ziae032/7624063)
- [Recovery From Skeletal Fluorosis (an Enigmatic, American Case) — JBMR (PMID:17014382)](https://onlinelibrary.wiley.com/doi/full/10.1359/jbmr.060912)
- [Calcium and Vitamin D Supplementation Effectively Alleviates Dental and Skeletal Fluorosis in Mice (PMID:33057951)](https://pubmed.ncbi.nlm.nih.gov/33057951/)
- [Treatment and Prevention of Skeletal Fluorosis](https://www.sciencedirect.com/science/article/pii/S0895398817300454)
- [Global groundwater contamination by geogenic fluoride (PMC13275634)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13275634/)
- [Application of Octacalcium Phosphate defluoridator prototype in East African Rift Valley communities (PMC7687156)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7687156/)
- [Defluoridation of water through transformation of octacalcium phosphate into fluorapatite (PMC6706606)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6706606/)
- [The genetic influence on bone susceptibility to fluoride (PMID:16920415)](https://pubmed.ncbi.nlm.nih.gov/16920415/)
- [Bone Response to Fluoride Exposure Is Influenced by Genetics (PMC4263599)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4263599/)
- [Quantification of Fluoride in Serum, Bone, and Teeth in a Murine Model (PMID:42667223)](https://pubmed.ncbi.nlm.nih.gov/42667223/)
- [iTRAQ-Based Proteomics Analysis of Serum Proteins in Wistar Rats Treated with Sodium Fluoride (PMC5085677)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5085677/)
- [Studies on skeletal muscle biopsies in endemic skeletal fluorosis (PMID:10878791)](https://pubmed.ncbi.nlm.nih.gov/10878791/)
- [Comparison of radiological characteristics between DISH and ankylosing spondylitis (PMC9892029)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9892029/)
- [Fluoride Exposure Provokes Mitochondria-Mediated Apoptosis and Increases Mitophagy in Osteocytes](https://link.springer.com/article/10.1007/s12011-022-03450-w)
- [Sodium fluoride accelerates apoptosis, oxidative stress and matrix degradation of condylar chondrocytes (PMID:39959228)](https://pubmed.ncbi.nlm.nih.gov/39959228/)
- [Pentose phosphate pathway regulates oxidative damage and apoptosis of chondrocytes induced by fluoride (PMID:41601087)](https://pubmed.ncbi.nlm.nih.gov/41601087/)
- [fluoride (CHEBI:17051)](https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:17051)
- [Dental fluorosis among people and livestock, Gihaya Island, Lake Kivu, Rwanda (PMC8686390)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8686390/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 43 |
| Resolved | 43 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 43 |
| On topic | 30 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:34769866` (1 mention) - How Did School Meal Access Change during the COVID-19 Pandemic? A Two-Step Floating Catchment Area Analysis of a Large Metropolitan Area.
  - shared terms: change

Weighed against this report's own most characteristic terms: `skeletal`, `fluoride`, `fluorosis`, `exposure`, `bone`, `disease`, `dental`, `endemic`, `synthesis`, `radiographic`, `clinical`, `year`, `chronic`, `change`, `tea`, `calcium`, `china`, `joint`, `water`, `via`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 58 |
| Resolved | 54 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 4 |
| Terms whose name was checked | 42 |
| Terms named correctly | 30 |
| Terms named as a **different** term | 6 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0400003` (4 mentions) - the report calls it "Skeletal fluorosis", "Ontology Lookup Service"; MONDO calls it **skeletal fluorosis**
- `HP:0100774` (2 mentions) - the report calls it "Osteosclerosis"; HP calls it **Hyperostosis**
- `HP:0009758` (1 mention) - the report calls it "Enamel hypoplasia"; HP calls it **Pyramidal skinfold extending from the base to the top of the nails**
- `UBERON:0002298` (3 mentions) - the report calls it "vertebral column"; UBERON calls it **brainstem**
- `UBERON:0002417` (1 mention) - the report calls it "posterior longitudinal ligament — if available"; UBERON calls it **abdominal segment of trunk**
- `UBERON:0004123` (1 mention) - the report calls it "femur"; UBERON calls it **myocardial layer**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002510` (2 mentions) - the report calls it "Spastic tetraparesis"; HP calls it **Spastic tetraplegia**
- `GO:0007224` (1 mention) - the report calls it "smoothened signaling pathway, Hedgehog"; GO calls it **smoothened signaling pathway**
- `GO:0043491` (1 mention) - the report calls it "protein kinase B signaling, PI3K/Akt"; GO calls it **phosphatidylinositol 3-kinase/protein kinase B signal transduction**, and lists "protein kinase B signaling" among its other names
- `UBERON:0001103` (1 mention) - the report calls it "diaphragm — n/a, remove if not applicable"; UBERON calls it **diaphragm**, and lists "diaphragm of thorax" among its other names
- `NCIT:C15302` (3 mentions) - the report calls it "Supportive/rehabilitative care:** Physical therapy", "Physical Therapy"; NCIT calls it **Physical Therapy**
- `CHEBI:17051` (5 mentions) - the report calls it "fluoride ion, the causal agent", "fluoride"; CHEBI calls it **fluoride**, and lists "FLUORIDE ION" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0400003` - called "Skeletal fluorosis", "Ontology Lookup Service"
- `MONDO:0006722` - called "dental fluorosis", "Dental fluorosis"
- `NCIT:C15302` - called "Supportive/rehabilitative care:** Physical therapy", "Physical Therapy"
- `CHEBI:17051` - called "fluoride ion, the causal agent", "fluoride"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ICD10CM`.