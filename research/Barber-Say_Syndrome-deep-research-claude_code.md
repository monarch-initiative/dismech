---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-23T15:22:31.352337'
end_time: '2026-09-23T15:28:00.482229'
duration_seconds: 329.13
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Barber-Say Syndrome
  mondo_id: MONDO:0008853
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
  web_search_requests: 22
  num_turns: 29
  total_cost_usd: 1.7585618
  session_id: fd65d8eb-852b-5a9d-91de-140beff025e2
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
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 0
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:26119818
  relevance_assessed: 12
  on_topic: 10
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 50
  verified: 45
  not_found: 0
  obsolete: 2
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 14
  labels_matching: 8
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: HP:0000656
    reported_labels:
    - Ectropion (bilateral, of both upper and lower eyelids)
    ontology_label: Ectropion
  - term_id: UBERON:0004085
    reported_labels:
    - eyelid
    ontology_label: labium majora
  - term_id: UBERON:0000151
    reported_labels:
    - nasal region
    ontology_label: pectoral fin
  - term_id: UBERON:0000202
    reported_labels:
    - mouth region
    ontology_label: glial blood brain barrier
  labels_variant: 2
  obsolete_terms:
  - term_id: HP:0007756
    ontology_label: obsolete Slitlike anterior chamber angles in children
    replaced_by: HP:0000594
  - term_id: GO:0043433
    ontology_label: obsolete negative regulation of DNA-binding transcription factor
      activity
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
- **Disease Name:** Barber-Say Syndrome
- **MONDO ID:** MONDO:0008853 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Barber-Say Syndrome** covering all of the
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

I'll research Barber-Say Syndrome now using web search and fetch tools, then produce the full report inline.

# Barber-Say Syndrome (BBRSAY) — Comprehensive Research Report

**MONDO:0008853 | OMIM #209885 | Orphanet ORPHA:1231 | ICD-10 Q87.0 | SNOMED CT 408537003 | Gene: TWIST2 (HGNC:20670, NCBI Gene 117581, 2q37.3)**

---

## Important disambiguation up front

**Barber-Say syndrome (BSS, this report) must not be confused with Say-Barber-Biesecker-Young-Simpson syndrome (SBBYSS)**, also called the SBBYS variant of Ohdo syndrome. Despite the overlapping eponym ("Say," "Barber"), SBBYSS is a distinct, unrelated disorder caused by *KAT6B* haploinsufficiency, featuring severe intellectual disability, blepharophimosis (narrow palpebral fissures — the *opposite* of BSS's macrostomia/ectropion pattern), and patellar anomalies. Several general search indices and even some clinical summaries conflate the two names. This report addresses **only** TWIST2-related Barber-Say syndrome. This is exactly the kind of named-entity confusion dismech's curation guidance warns about, and any future curation of this entry should not import KAT6B/SBBYSS content.

---

## 1. Disease Information

Barber-Say syndrome is an ultra-rare congenital malformation syndrome first delineated by Barber et al. in 1982 (*Syndrome Identification* VIII(1):6–9), describing a 3.5-year-old girl with "macrostomia, ectropion, atrophic skin, marked hypertrichosis, and growth retardation" (as summarized in later literature). It is now understood as an autosomal dominant disorder — virtually always arising **de novo**, occasionally transmitted by a mosaic parent — caused by recurrent heterozygous missense substitutions at a single codon (p.Glu75) in the basic DNA-binding domain of the bHLH transcription factor TWIST2 (Marchegiani et al. 2015, PMID:26119818).

**Key identifiers:**
- OMIM: #209885 (phenotype), *607556 (TWIST2 gene)
- Orphanet: ORPHA:1231
- MONDO: 0008853
- ICD-10: Q87.0 (congenital malformation syndromes predominantly affecting facial appearance)
- SNOMED CT: 408537003
- Gene: TWIST2 / DERMO1, HGNC:20670, NCBI Gene 117581, chr2:238,848,032–238,910,534 (GRCh38), 2q37.3

**Synonyms:** none widely used beyond "Barber-Say syndrome" / "BBRSAY"; occasionally listed with the informal descriptive label "hypertrichosis-atrophic skin-ectropion-macrostomia syndrome."

**Source basis:** Information is derived almost entirely from **aggregated individual case reports and small case series** (fewer than 20–25 published probands as of the most recent literature identified in this search), plus one pivotal multi-family molecular genetics study (Marchegiani et al. 2015) that pooled 11 BSS-affected families with 7 ablepharon-macrostomia syndrome (AMS) families. There is **no GeneReviews chapter** for Barber-Say syndrome (none was found in this search), and no disease registry or EHR-aggregated cohort exists — this is a disease known only from the case-report literature, which should be reflected in any `evidence_source: HUMAN_CLINICAL` grading as individual-patient rather than population-level evidence.

---

## 2. Etiology

**Disease causal factor:** Purely genetic/molecular. BSS is caused by heterozygous, essentially always de novo, missense mutations in the basic domain of TWIST2, most recurrently **p.Glu75Gln (E75Q)** and less commonly **p.Glu75Ala (E75A)** (Marchegiani et al. 2015, PMID:26119818: "a lysine at TWIST2 residue 75 resulted in AMS, whereas a glutamine or alanine yielded BSS," with 9 of 11 BSS families carrying p.Glu75Gln and 2 carrying p.Glu75Ala).

**Genetic risk factors:**
- The causal locus is TWIST2 itself; there is no known population-level susceptibility variant — this is a fully penetrant, single-gene, single-codon dominant disorder, not a complex/multifactorial trait.
- **Germline/parental mosaicism** is the specific recurrence-risk factor identified in the literature: Marchegiani et al. 2015 report "three disease-transmitting fathers with mild AMS or BSS and variable skin pigmentation were mosaic for a TWIST2 mutation," and Singh et al. 2016 (PMID:27092433) document transmission of the p.E75Q mutation from a somatically/gonadally mosaic, mildly affected father to a severely affected daughter in an Indian family — establishing that an apparently unaffected or minimally affected parent can still confer significant recurrence risk via germline mosaicism, relevant for genetic counseling.
- No modifier genes have been reported.

**Environmental risk factors:** None identified or plausible for a single-gene bHLH transcription-factor disorder; no association with parental age, teratogen exposure, or periconceptional factors was found in this search.

**Protective factors:** None described; not applicable to this class of fully penetrant dominant missense disorder.

**Gene-environment interactions:** None reported; not applicable.

---

## 3. Phenotypes

BSS phenotypes cluster into craniofacial/ocular, integumentary (the dominant and defining system), and lesser genitourinary/dental/auditory findings. Onset is **congenital** in all cases (present at birth); there is no reported postnatal-onset phenotype, and the facial gestalt and skin findings are typically described as static/non-progressive rather than degenerative, though the aged, redundant-skin appearance can be mistaken for a progeroid process.

| Phenotype | HPO term (suggested) | Frequency (qualitative, per case-series literature) | Onset | Notes |
|---|---|---|---|---|
| Generalized/congenital hypertrichosis (esp. back, forehead, limbs) | HP:0007497 (Generalized hypertrichosis) / HP:0000998 (Hypertrichosis) | Core/near-universal — defining feature distinguishing BSS from AMS | Congenital | Fine, long lanugo-like hair |
| Atrophic, thin, redundant/hyperlax skin ("cutis-laxa-like") | HP:0007756 (Atrophic skin) / HP:0000973 (Cutis laxa) | Core/near-universal | Congenital | Histologically thin dermis, decreased elastic fibers, hypocollagenosis (see §6) |
| Ectropion (bilateral, of both upper and lower eyelids) | HP:0000656 | Core/near-universal (present in most, absent in some "milder" reported cases) | Congenital | Underdeveloped anterior lamella of eyelid; a documented milder BSS variant lacks ectropion (Pomili et al., PMID:9415700) |
| Macrostomia (wide mouth) | HP:0000154 | Core/near-universal | Congenital | |
| Absent/sparse eyebrows and eyelashes | HP:0045075 (Sparse eyebrow) / HP:0000653 (Sparse eyelashes) | Very common | Congenital | |
| Telecanthus / hypertelorism | HP:0000506 / HP:0000316 | Very common | Congenital | |
| Broad, bulbous nasal tip with hypoplastic alae nasi | HP:0000414 / HP:0000430 | Very common | Congenital | |
| Low-set, misshapen/dysplastic ears | HP:0000369 / HP:0000377 | Common | Congenital | Narrow ear canals reported |
| Low anterior hairline | HP:0000294 | Common | Congenital | |
| Nipple hypoplasia / absent or widely spaced nipples; hypo-/aplastic mammary glands | HP:0002557 (Hypoplastic nipples) / HP:0000006-adjacent | Common | Congenital | |
| Genital anomalies (male: hypospadias, shawl scrotum, occasional cryptorchidism; female: prominent/enlarged labia majora) | HP:0000047 (Hypospadias) / HP:0000047-adjacent | Variable, minority | Congenital | |
| Delayed dental eruption; small/malformed teeth; gingival overgrowth | HP:0000684 (Delayed eruption of teeth) | Common | Childhood | |
| High-arched or cleft palate | HP:0002705 (High palate) / HP:0000175 (Cleft palate) | Occasional | Congenital | |
| Conductive hearing loss | HP:0000405 | Occasional/minority | Variable | |
| Mild psychomotor/developmental delay | HP:0001263 | Minority — most reports emphasize normal cognition | Infancy/childhood | Contrasts with the more severe developmental delay of KAT6B/SBBYSS — see disambiguation above |
| Corneal exposure keratopathy (secondary to ectropion/lagophthalmos) | HP:0025684-adjacent / exposure keratopathy | Complication, common where ectropion is severe | Any age | Drives ophthalmologic/surgical urgency |
| Growth retardation | HP:0001510 | Reported in the original 1982 index case and others | Congenital/postnatal | |

**Severity/progression:** Facial and integumentary features are present at birth and are generally described as static rather than progressive; the main progression concern is **secondary, acquired complications** — corneal exposure and ulceration from chronic ectropion/lagophthalmos, which can worsen over time without surgical correction and represent the principal ophthalmologic threat to vision.

**Quality-of-life impact:** No formal EQ-5D/SF-36/QOL instrument data were found for this ultra-rare condition. Documented impacts described qualitatively in case reports and at least one patient-perspective publication (Küry et al./De Maria, "A Patient's View," PMID:28690482) include: disfigurement-related psychosocial burden, feeding difficulty related to macrostomia in infancy, need for repeated reconstructive surgeries (eyelid, oral commissure, craniofacial), and corneal/visual morbidity from exposure keratopathy. Cognitive/motor development is reported as **normal in the majority of cases**, a key point distinguishing BSS from many other multiple-congenital-anomaly syndromes and specifically from SBBYSS.

---

## 4. Genetic/Molecular Information

**Causal gene:** TWIST2 (OMIM *607556), HGNC:20670, chr2:238,848,032-238,910,534 (2q37.3).

**Pathogenic variants (BSS-specific):**
- p.Glu75Gln (E75Q) — the recurrent, most common BSS allele (9/11 families in Marchegiani et al. 2015)
- p.Glu75Ala (E75A) — the second recognized BSS allele (2/11 families)
- Both fall within the **basic domain** of the bHLH protein — the DNA-contacting region — and were shown by ChIP-seq/EMSA-type analyses in the Marchegiani study to alter TWIST2's DNA-binding pattern: "All identified mutations fell in the basic domain of TWIST2 and altered the DNA-binding pattern of Flag-TWIST2 in HeLa cells," with the mutant proteins sharing only a fraction of their genomic binding peaks with wild-type TWIST2 and gaining new, non-wild-type binding sites.

**Variant classification:** These recurrent missense substitutions are classified pathogenic under ACMG/AMP criteria in the primary literature (recurrent de novo occurrence across unrelated families, functional evidence of altered DNA binding, precise genotype-phenotype correlation). No formal ClinVar aggregate statistics were retrieved in this search; curators should independently confirm current ClinVar classification for p.Glu75Gln/p.Glu75Ala before citing a specific pathogenicity tier.

**Allele frequency:** Not present in population databases (gnomAD/1000 Genomes/TOPMed) at meaningful frequency — consistent with a fully penetrant, severe, essentially always-de-novo dominant disorder; no specific gnomAD constraint metrics (e.g., pLI, missense Z-score) for TWIST2 were retrieved in this search and should be pulled directly from gnomAD if needed for curation.

**Somatic vs. germline origin:** Germline (constitutional), with the specific and clinically important caveat of **parental somatic/germline mosaicism** as the recurrence mechanism in familial transmission (see §2 and §9).

**Functional consequences — the central mechanistic ambiguity:** The literature explicitly frames the E75Q/E75A (BSS) and E75K (AMS) substitutions as producing **both dominant-negative and gain-of-function (neomorphic) effects simultaneously**, rather than a clean loss- or gain-of-function classification:
> "The mutations are located in the basic domain of the protein, and molecular analyses suggested that the mutations alter the DNA-binding activity of TWIST2, leading to both dominant-negative and gain-of-function effects" (Marchegiani et al. 2015, PMID:26119818, as reported in secondary summaries of the primary text).

Mechanistically this is attributed to (a) partial loss of binding to TWIST2's normal E-box target sites (dominant-negative component) combined with (b) acquisition of binding to abnormal, non-wild-type genomic sites (neomorphic/gain-of-function component) — "a dominant-negative effect due to loss of binding to the normal contingent of TWIST2 DNA binding sites or a neomorphic mechanism due to binding of the mutant TWIST2 to extraneous promoter sites." **This dual mechanism is the key curatorial subtlety**: a `GeneticContext.functional_impact_category` of a single enum value (e.g., `DOMINANT_NEGATIVE`) would understate what the primary literature actually claims; curators should consider whether the schema's controlled vocabulary can capture both components or whether free text is needed alongside the closest enum value.

**Modifier genes:** None established.

**Epigenetic information:** No disease-specific DNA methylation/histone data for BSS were found. Note, however, that TWIST2 itself functions partly through chromatin remodeling in dermal fibroblast maturation more broadly (Twist2-driven chromatin remodeling in postnatal dermal fibroblasts, ScienceDirect/iScience-type source found in search) — this is basic TWIST2 developmental biology, not BSS-specific pathological epigenetic data, and should not be conflated with disease-causing epigenetic changes.

**Chromosomal abnormalities:** Not applicable to BSS itself (a single-gene point-mutation disorder). Note for differential/related-locus awareness: TWIST2 sits within the region implicated in **2q37 deletion syndrome**, and TWIST2 has been "proposed as a candidate gene for 2q37 deletion syndrome due to its localization in the smallest deleted chromosome region" — this is a distinct, contiguous-gene-deletion condition and should not be merged with BSS in curation.

---

## 5. Environmental Information

No environmental, lifestyle, or infectious contributing factors were identified in this search, consistent with BSS being a fully genetically determined, single-gene disorder with no reported gene-environment interaction. This section is not applicable beyond noting its inapplicability.

---

## 6. Mechanism / Pathophysiology

### Causal chain (ordered, with inference flagged)

1. A de novo (or paternally/maternally transmitted-via-mosaicism) heterozygous missense substitution — most often p.Glu75Gln, less often p.Glu75Ala — arises in the **basic DNA-binding domain** of TWIST2, a basic helix-loop-helix (bHLH) transcription factor. *(Demonstrated: recurrent mutation identification across 11 independent families, PMID:26119818.)*
2. This alters the amino-acid sequence of the DNA-contacting basic domain, changing TWIST2's DNA-binding specificity: the mutant protein **partially loses binding at wild-type TWIST2 target sites** and **gains binding at abnormal, non-wild-type genomic sites**, as shown by comparative binding-peak analysis of mutant vs. wild-type TWIST2 in cell-based assays. *(Demonstrated in vitro, PMID:26119818.)*
3. This dual DNA-binding disruption leads downstream to a **combined dominant-negative and neomorphic (gain-of-function) transcriptional effect** on TWIST2's normal target gene network — rather than simple TWIST2 haploinsufficiency. *(Inferred from binding data and genotype-phenotype correlation; direct downstream transcriptomic confirmation in human tissue is limited.)*
4. TWIST2 is normally a heterodimeric partner (with E-box-binding partners such as the ubiquitous bHLH protein E12/TCF3) that, during embryogenesis, is **highly expressed in craniofacial mesenchyme and chondrogenic/dermal precursor cells**, where it inhibits terminal differentiation of mesenchymal lineages (myogenic, osteogenic) and directs dermal fibroblast and chondrogenic tissue development. *(Established developmental biology of wild-type TWIST2; PMID:26119818 and general TWIST2 literature.)*
5. Disrupted TWIST2 transcriptional output in these mesenchymal precursor populations leads to **abnormal craniofacial mesenchymal and periocular (eyelid) tissue development**, manifesting as underdevelopment of the eyelid anterior lamella (→ ectropion), abnormal maxillary/oral mesenchyme patterning (→ macrostomia), and abnormal nasal/auricular cartilage and soft-tissue development (→ bulbous nose, dysplastic ears). *(Inferred from the tissue-expression pattern and the clinical phenotype; directly demonstrated in a zebrafish model, see below.)*
6. In parallel, disrupted TWIST2 function in **dermal fibroblast precursors** impairs normal extracellular matrix (elastic fiber and collagen) deposition, producing the histologically documented thin epidermis, markedly reduced dermal elastic fibers, and hypocollagenosis. *(Demonstrated histologically in patient skin biopsies; mechanistic link to TWIST2's fibroblast-differentiation role is inferred by analogy to TWIST2's known role in postnatal dermal fibroblast chromatin regulation, not directly shown in BSS patient fibroblast transcriptomics in the sources retrieved here.)* This produces the clinical triad of atrophic, hyperlax, redundant ("cutis-laxa-like") skin.
7. Independently, disrupted TWIST2 function in **hair-follicle-associated mesenchyme** is associated with the striking congenital generalized hypertrichosis that clinically distinguishes BSS from its allelic neighbor AMS (which shares the eyelid/mouth phenotype but lacks prominent hypertrichosis). *(Correlative/inferred — the precise mechanistic link between the E75Q/E75A substitution and follicular hair-cycle dysregulation, as opposed to the E75K/AMS substitution, has not been experimentally dissected in the sources found here; this is a genuine knowledge gap.)*
8. Chronic ectropion/lagophthalmos secondary to the eyelid mesenchymal defect (step 5) leads, as a **downstream secondary/acquired complication rather than a primary developmental defect**, to chronic corneal exposure and exposure keratopathy, which is the principal driver of long-term ophthalmologic morbidity and surgical urgency. *(Well-documented clinical complication, e.g., PMID:29329175, PMID:30455119.)*

### Supporting mechanistic detail by category

- **Molecular pathway / transcription factor biology:** TWIST2 is a class II bHLH transcription factor that binds E-box motifs (5′-CANNTG-3′) as a heterodimer with widely expressed bHLH partners (e.g., E12); it classically **inhibits** transcriptional activation driven by myogenic (MYOD1, MYOG) and osteogenic/MEF2-family (MEF2A, MEF2C) factors, and represses pro-inflammatory cytokine gene expression via inhibition of NF-κB-mediated transactivation (general TWIST2 biology, GeneCards/NCBI Gene summary, and PMID:26119818 background). GO terms of interest: **GO:0000981** (DNA-binding transcription factor activity, RNA polymerase II-specific), **GO:0046983** (protein dimerization activity), **GO:0043433** (negative regulation of DNA-binding transcription factor activity), **GO:0045892** (negative regulation of DNA-templated transcription).
- **Cellular processes:** Mesenchymal stem/progenitor cell differentiation is the central affected process — TWIST2 normally "mediates mesenchymal stem cell self-renewal by maintaining the immature phenotype and inhibiting osteogenesis and chondrogenesis" (search-derived synthesis of TWIST2 biology). Relevant GO biological process terms: **GO:0030278** (regulation of ossification), **GO:0045668** (negative regulation of osteoblast differentiation), **GO:0060324** (face development), **GO:0043010** (camera-type eye development)/eyelid-specific terms as available.
- **Protein dysfunction:** Altered/gained DNA-binding specificity of a bHLH basic-domain mutant, rather than classical misfolding or aggregation — a **sequence-specificity switch** mechanism (PMID:26119818).
- **Tissue damage mechanisms:** Skin — decreased elastic fiber content and hypocollagenosis (a developmental extracellular-matrix deficiency present from birth, not an acquired degenerative process) underlie the atrophic/redundant skin phenotype. Cornea — chronic mechanical exposure from ectropion/lagophthalmos (a biomechanical, not primary molecular, injury mechanism) underlies exposure keratopathy.
- **Molecular/target-gene profiling:** In the allelic Setleis syndrome (TWIST2 loss-of-function; see below), expression profiling of patient fibroblasts identified **dysregulation of periostin (POSTN)**, an extracellular-matrix protein gene, among TWIST2 target genes ("Nonsense mutations of the bHLH transcription factor TWIST2 found in Setleis Syndrome patients cause dysregulation of periostin" — title/summary level only; the primary text could not be directly retrieved in this session due to a bot-check wall, so this should be treated as a **lead to verify against the primary source**, not a confirmed quote). A **zebrafish model** expressing mutant TWIST2 showed "severe head hypoplasia" and downregulation of extracellular matrix, membrane, and cytoskeleton gene categories (PMID:26119818), directly supporting the craniofacial-mesenchyme mechanism above.
- **Single-cell / advanced omics:** No single-cell, spatial transcriptomic, or multi-omic BSS-specific dataset was identified in this search — this is a clear gap consistent with the disease's extreme rarity.

### Allelic mechanistic contrast (important for lump/split and mechanism curation)

The TWIST2 basic-domain locus at codon 75 shows a clean **genotype-phenotype-mechanism correlation** across three distinct disorders, useful for framing BSS's mechanism against its allelic neighbors:

| Disorder | Variant(s) | Zygosity | Mechanism | Key discriminating phenotype |
|---|---|---|---|---|
| **Ablepharon-macrostomia syndrome (AMS)**, OMIM #200110 | p.Glu75Lys (E75K) | Heterozygous, de novo | Altered DNA binding (dominant-negative + gain-of-function) | Severe/absent eyelids (ablepharon), minimal hypertrichosis |
| **Barber-Say syndrome (BSS)**, OMIM #209885 | p.Glu75Gln (E75Q), p.Glu75Ala (E75A) | Heterozygous, de novo (or mosaic-transmitted) | Altered DNA binding (dominant-negative + gain-of-function) | Prominent generalized hypertrichosis, less severe eyelid findings, near-normal hands/genitalia |
| **Setleis syndrome / focal facial dermal dysplasia 3 (FFDD3)**, OMIM #227260 | Nonsense/frameshift (e.g., p.Gln65X, p.Gln119X, c.168delC) | **Homozygous or compound heterozygous** | Truncated, unstable protein — **loss-of-function** | Bitemporal "forceps-mark-like" atrophic scarring; **autosomal recessive** |

This contrast is directly useful for the dismech mechanism module: it shows that the *same gene, same protein domain* produces a **dominant gain-of-function/dominant-negative phenotype spectrum (AMS/BSS)** when heterozygous missense, versus a **recessive loss-of-function phenotype (Setleis)** when biallelic null — a textbook illustration of the allelic-series concept, and a caution against treating "TWIST2-related disorder" as a single mechanism.

---

## 7. Anatomical Structures Affected

**Organ level:**
- Primary: skin/integument (whole-body, most severe on back/trunk and forehead); periocular structures/eyelids; craniofacial skeleton and soft tissue (nose, mouth, ears); mammary tissue (hypoplasia); dentition.
- Secondary/complication: cornea (exposure keratopathy secondary to eyelid dysfunction).
- Body systems: integumentary system (primary), ophthalmologic/ocular adnexal system, craniofacial/musculoskeletal (mesenchymal patterning), reproductive/genitourinary (minority), auditory system (minority — conductive hearing loss), and, per some reports, mild central nervous system/developmental involvement in a minority of cases.
- Suggested UBERON terms: UBERON:0002097 (skin of body), UBERON:0004085 (eyelid), UBERON:0000151 (nasal region), UBERON:0000202 (mouth region), UBERON:0001690 (ear), UBERON:0001911 (mammary gland).

**Tissue and cell level:**
- Dermal fibroblasts and dermal connective tissue (atrophy, reduced elastic fiber and collagen content) — Cell Ontology **CL:0000057** (fibroblast) / dermal fibroblast subtype if available.
- Craniofacial mesenchyme / neural-crest-derived mesenchymal precursors — **CL:0002092** (mesenchymal cell) or neural-crest-derived cell terms.
- Hair follicle mesenchyme/dermal papilla (hypertrichosis) — **CL:1001608**-type dermal papilla terms if curating that level of detail.
- Corneal epithelium (secondary exposure injury).

**Subcellular level:** Not a subcellular-pathology disease in the classical sense (no organelle-specific storage or trafficking defect reported); the core molecular lesion is nuclear — altered sequence-specific DNA binding of a transcription factor (GO Cellular Component: **GO:0005634**, nucleus; **GO:0000785**, chromatin).

**Localization:**
- Skin findings are **generalized/bilateral**, with the back and forehead emphasized for hypertrichosis.
- Facial/eyelid findings are essentially always **bilateral and symmetric** (bilateral ectropion, bilateral telecanthus) — no lateralization or asymmetry pattern was reported in this search.

---

## 8. Temporal Development

**Onset:** Congenital in essentially all reported features — the full facial gestalt, skin findings, hypertrichosis, and genital/nipple anomalies are present and recognizable at birth. No postnatal-onset primary features were identified.

**Onset pattern:** Not applicable in the acute/subacute/chronic sense used for acquired disease — this is a structural/developmental congenital malformation syndrome.

**Progression:**
- The primary developmental phenotype (facial gestalt, skin texture, hypertrichosis) is generally **stable/non-progressive** after birth rather than degenerative, though the skin's aged/redundant appearance can create a superficial resemblance to a progressive progeroid process (see §6 differential).
- The principal **progressive element is secondary**: chronic ectropion/lagophthalmos can lead to worsening corneal exposure, keratopathy, and potential visual compromise over time if uncorrected — this is the clearest example in BSS of a disease-stage trajectory (mild exposure → chronic keratopathy → risk of corneal scarring/vision loss), and the rationale for early and often repeated surgical intervention.
- Growth retardation was noted in the original index case and some subsequent reports but is not universally emphasized as progressive.

**Disease course pattern:** Static congenital malformation with a superimposed chronic, potentially progressive ocular-surface complication; no remitting-relapsing pattern; lifelong condition (self-limited vs. chronic-lifelong: **chronic lifelong**, given permanence of the structural anomalies, though with normal life expectancy reported in most cases — no BSS-specific mortality data were found, and the disorder does not appear associated with reduced survival based on the case-report literature searched).

**Critical periods:** Neonatal/infant period is clinically critical for feeding support (macrostomia can complicate latch/feeding) and for early ophthalmologic assessment to prevent corneal complications; early childhood is the window for the major staged reconstructive surgical program (see §12).

---

## 9. Inheritance and Population

**Epidemiology:** Orphanet lists prevalence as **<1/1,000,000**, describing BSS as "a rare entity described in eleven patients to date" as of the Orphanet entry consulted; more recent case-report literature searched here suggests the total number of published probands has grown to roughly 15–25+ by the late 2010s (exact current total not independently re-tallied in this search — a precise current count should be obtained by a fresh literature search or GeneReviews-equivalent source at curation time rather than taken from this report as a fixed number). No incidence, national-registry, or GBD-level burden data exist for a disorder this rare.

**Inheritance pattern:** **Autosomal dominant.** Nearly all reported cases are simplex/de novo. Vertical (parent-to-child) transmission has been documented in at least two family reports and is explained mechanistically by **parental mosaicism** for the causative TWIST2 mutation rather than typical full heterozygosity in an overtly/typically-affected parent — i.e., recurrence in offspring of an apparently mildly affected or subtly affected parent reflects germline (and often somatic) mosaicism, not simple full penetrance with variable expressivity alone. *(Note: some aggregator search snippets described BSS's inheritance as potentially "autosomal dominant or autosomal recessive" — this almost certainly reflects conflation with the separate, genuinely autosomal-recessive allelic disorder Setleis syndrome at the same locus, per §6, rather than a true AR form of BSS itself. Curators should not import an AR inheritance record for Barber-Say syndrome proper without independently verifying it against a primary source, as this looks like a database-level entity confusion rather than an established fact about BSS.)*

**Penetrance:** Appears fully penetrant for the core facial/skin gestalt in every reported heterozygous carrier of a full (non-mosaic) E75Q/E75A mutation; formal penetrance estimates (e.g., from ClinGen) were not found in this search.

**Expressivity:** Variable — the mosaic-transmission family reports describe a **mild-to-severe expressivity gradient tracking with mosaic vs. full germline mutation status** (mosaic/mildly affected parent → severely affected, fully heterozygous child), and at least one report describes a distinctly milder BSS phenotype lacking ectropion (Pomili et al., PMID:9415700), indicating that even among fully heterozygous individuals there is a recognized phenotypic range.

**Genetic anticipation:** Not reported/not applicable (not a repeat-expansion disorder).

**Germline mosaicism:** Directly documented and clinically important (see §2, §9 above) — PMID:26119818 and PMID:27092433 are the primary sources.

**Founder effects:** None reported; the causal mutations (E75Q, E75A) are recurrent-de-novo across genetically diverse, geographically dispersed families (reports span European, Indian, Japanese, and other populations in the literature retrieved), consistent with a mutational hotspot rather than a population-specific founder allele.

**Consanguinity:** Not a relevant risk factor for BSS itself (dominant, de novo); consanguinity **is** relevant for the allelic recessive disorder Setleis syndrome, where homozygous/compound-heterozygous null alleles require biparental transmission of a rare variant, and consanguineous families (e.g., the Mexican-Nahua sibship reported) are overrepresented in the Setleis literature — this should be kept clearly on the Setleis side of any dismech entry, not attributed to BSS.

**Carrier frequency:** Not applicable/not meaningful for a fully penetrant, essentially always-de-novo dominant disorder with no population carrier reservoir.

**Population demographics:** No specific ethnic or geographic enrichment was identified for BSS; reported cases span multiple continents/ethnicities. No sex-ratio skew was identified in this search (both male and female probands reported, including father-to-daughter and father-to-child transmissions). Age distribution at recognition is uniformly **neonatal/early infancy**, since the defining features are present at birth.

---

## 10. Diagnostics

**Clinical recognition:** BSS is primarily a **clinical/gestalt diagnosis** made at birth from the combination of congenital generalized hypertrichosis, atrophic/redundant ("cutis laxa-like") skin, bilateral ectropion, and macrostomia, supported by the accessory facial features (telecanthus, bulbous nose, dysplastic ears, low anterior hairline) — molecular confirmation is then sought.

**Laboratory/genetic tests:**
- **Single-gene TWIST2 sequence analysis** (targeted Sanger or NGS sequencing of TWIST2 coding exons) is the definitive confirmatory test, given the strong genotype-phenotype correlation at a single recurrent codon; an NCBI GTR-listed clinical test specifically targets "TWIST2 gene (Sequence Analysis-All Coding Exons)" for Barber-Say syndrome (postnatal testing), confirming this is an established, commercially available single-gene test rather than requiring exome-first strategies in a clinically classic case.
- **Whole-exome/whole-genome sequencing** is appropriate when the clinical gestalt is atypical or overlaps with AMS/other differentials, or in the diagnostic-odyssey setting before the phenotype is recognized as TWIST2-related — this is in fact how the causal gene was originally identified (Marchegiani et al. 2015 used exome and candidate-gene sequencing).
- **Chromosomal microarray/karyotype** may be used to exclude a 2q37 deletion or other structural chromosomal cause in atypical presentations, given TWIST2's location within the 2q37 deletion-syndrome critical region, though this is a differential-exclusion step rather than the primary diagnostic route for classic BSS.
- **Skin biopsy/histopathology** is a supportive (not gene-confirmatory) diagnostic tool, showing atrophic epidermis with mild orthohyperkeratosis, a thin reticular dermis, markedly decreased elastic fibers, and hypocollagenosis — a distinctive but non-specific pattern that supports the clinical diagnosis and helps distinguish BSS from other cutis-laxa-spectrum conditions on biopsy.
- **Ophthalmologic examination** (slit-lamp, corneal surface assessment) is an essential diagnostic/monitoring test given the risk of exposure keratopathy, not for syndrome diagnosis per se but for morbidity surveillance.
- **Audiology** is indicated given the minority occurrence of conductive hearing loss.
- No BSS-specific circulating biomarker, imaging signature, or electrophysiologic test was identified.

**Differential diagnosis (key entities to exclude/distinguish, per this search):**
- **Ablepharon-macrostomia syndrome (AMS)**, OMIM #200110 — the closest allelic differential; distinguished by more severe/absent eyelids and lack of prominent hypertrichosis (see §6 table). Some authors argue AMS and BSS (and Setleis) may represent "a continuum" rather than fully distinct entities (PMID:19760652, "Case report supporting that the Barber-Say and ablepharon macrostomia syndromes could represent one disorder") — a lump/split consideration directly relevant to dismech's granularity guidance, since the molecular data (distinct, non-overlapping codon-75 substitutions with a clean genotype-phenotype split) currently support keeping them as **distinct but closely related allelic entries** rather than a single lumped disorder, while flagging the continuum argument in notes.
- **Setleis syndrome (FFDD3)** — distinguished by autosomal recessive inheritance, homozygous/compound-het loss-of-function TWIST2 alleles, and a localized bitemporal scarring phenotype rather than the generalized skin/hypertrichosis pattern of BSS.
- **Progeroid/cutis laxa spectrum disorders** — Wiedemann-Rautenstrauch syndrome (neonatal progeroid syndrome), congenital cutis laxa syndromes (including the arterial tortuosity/emphysema-associated recessive form), De Barsy syndrome (distinguished by corneal clouding and pseudoathetoid movements), Costello syndrome, and Ehlers-Danlos syndrome are cited generically in the differential-diagnosis literature for the "prematurely aged appearance + cutis laxa" phenotype cluster that BSS superficially resembles; none of these share the TWIST2 molecular basis.
- **Say-Barber-Biesecker-Young-Simpson syndrome (SBBYSS/KAT6B)** — critically, **not a true differential in the biological sense but a name-collision risk** (see disambiguation section at top); should be explicitly excluded by clinicians/curators on the basis of gene (KAT6B, not TWIST2) and phenotype (blepharophimosis + severe developmental delay, not macrostomia/ectropion + typically normal cognition).

**Screening:** No population or newborn screening program exists or would be applicable (private, ultra-rare, non-metabolic single-gene disorder); prenatal diagnosis by targeted TWIST2 sequencing is possible in families with a known mutation (including at-risk mosaic-parent families), and detailed prenatal ultrasound might in principle detect macrostomia/facial anomalies, though no specific prenatal-ultrasound detection report was retrieved in this search.

---

## 11. Outcome/Prognosis

**Survival/mortality:** No BSS-specific survival statistics, life-expectancy figures, or mortality-rate data were identified in this search. The case-report literature does not describe BSS as a life-limiting condition; growth retardation has been noted in some cases, but reports emphasize surgical/reconstructive and ophthalmologic management rather than mortality risk. This should be recorded as an **absence of evidence** rather than evidence of normal survival — no formal natural-history or registry-based survival study exists for a disorder this rare.

**Morbidity/function:** The dominant morbidity is related to (a) chronic ocular surface disease from ectropion-driven exposure, with risk of keratopathy, corneal scarring, and potential vision impairment if uncorrected, and (b) the disfigurement and functional (feeding, speech, dental) impact of macrostomia and craniofacial anomalies, generally managed with staged reconstructive surgery. Cognitive/motor function is reported as normal in the majority of documented cases; a minority describe mild developmental delay, but this is not a defining or universal feature (again in contrast to SBBYSS/KAT6B, which is essentially always associated with significant developmental disability — a further reason the two names must not be conflated when recording prognosis).

**Complications:** Exposure keratopathy (most significant, potentially sight-threatening); feeding difficulty in infancy from macrostomia; dental crowding/malocclusion from macrostomia and delayed eruption; psychosocial impact of facial disfigurement; hearing impairment in a minority.

**Recovery potential:** With surgical intervention (staged eyelid reconstruction, oral commissuroplasty, orthognathic/rhinoplasty/genioplasty procedures as needed — see §12), functional and cosmetic outcomes are reported as favorable in the case literature, though repeated procedures over childhood are typical and the underlying tissue laxity/atrophy (a developmental connective-tissue deficiency, not merely a positional deformity) can complicate surgical durability.

**Prognostic factors:** Severity of ectropion (driving ocular risk) and macrostomia/craniofacial involvement are the main clinically tracked severity axes; whether a patient has a full heterozygous mutation versus arose from a mosaic-parent transmission has been suggested (in the mosaicism case reports) to correlate with phenotypic severity, but this has not been formalized into a validated prognostic scoring system.

**Prognostic biomarkers:** None identified.

---

## 12. Treatment

There is **no disease-modifying or gene-targeted therapy** for Barber-Say syndrome; management is entirely **supportive and reconstructive/surgical**, aimed at correcting the anatomic anomalies and preventing/treating secondary complications (chiefly corneal exposure).

**Surgical/interventional (the primary treatment modality):**
- **Staged eyelid reconstruction** for ectropion/lagophthalmos — techniques reported include lateral tarsorrhaphy, full-thickness skin grafting (donor sites reported: volar forearm, retroauricular area, supraclavicular fossa), and autologous fat (lipo)grafting for periorbital volume restoration (multidisciplinary case report, PMID:30455119, "Multidisciplinary eyelid reconstruction in Barber-Say syndrome"). Suggested NCIT term: **NCIT:C15329** (Surgical Procedure), or a more specific oculoplastic reconstruction term if the KB's NCIT mapping supports it.
- **Mid-face lift and eyelid repositioning**, sometimes combined with **botulinum toxin** adjunct treatment, reported for symptomatic corneal exposure management in an adult BSS patient, with resolution of signs/symptoms of exposure keratopathy.
- **Macrostomia correction (commissuroplasty/cheiloplasty)** — lip/oral commissure reconstruction to narrow the mouth. NCIT: a specific cheiloplasty/reconstructive oral surgery term.
- **Orthognathic surgery** for jaw correction, **rhinoplasty** for nasal reconstruction, **genioplasty** for chin correction, and **malar (cheek) implants** for facial contour — reported as part of the broader staged craniofacial reconstructive program in one comprehensive surgical case series retrieved in this search.
- **Anesthetic management considerations** are themselves a documented topic in the literature — a case report specifically addresses "General anesthesia of a Japanese infant with Barber-Say syndrome," presumably reflecting airway/feeding-related considerations relevant to macrostomia and craniofacial anatomy (specific anesthetic findings were not independently extracted in this search and should be pulled directly from that source if curating perioperative-risk content).

**Supportive/rehabilitative care:**
- Ophthalmologic surveillance and **lubrication/ocular surface protection** (artificial tears, ointments, protective measures against exposure) as first-line, non-surgical management of ectropion-related dryness, presumably standard-of-care though not separately quoted from a specific source in this search — this should be verified against a primary ophthalmology reference before being cited as an evidence-backed BSS-specific recommendation rather than general exposure-keratopathy management extrapolated to this condition.
- **Feeding support** in infancy given macrostomia.
- **Dental/orthodontic management** for delayed eruption, malocclusion, and gingival overgrowth.
- **Audiology follow-up and hearing support** where conductive hearing loss is present.
- **Genetic counseling** (NCIT:C15240) is clearly indicated given the demonstrated risk of parental germline mosaicism affecting recurrence-risk counseling, distinct from the low recurrence risk that would be quoted for a purely simplex de novo dominant disorder.

**Pharmacotherapy:** No BSS-specific pharmacologic treatment exists; botulinum toxin is used adjunctively for periocular/eyelid positioning in at least one reported case (see above) rather than as disease treatment per se.

**Experimental/advanced therapeutics:** None — no gene therapy, cell therapy, or targeted molecular therapy has been reported or is currently applicable given the transcription-factor, developmental-malformation nature of the disease; no active ClinicalTrials.gov or WHO ICTRP trial was identified for Barber-Say syndrome in this search (consistent with its extreme rarity and the absence of a modifiable downstream pathway analogous to, e.g., an enzyme-replacement target).

**Treatment strategy:** Management follows a **staged, multidisciplinary reconstructive algorithm** beginning in infancy (ophthalmologic protection, feeding support) and continuing through childhood/adolescence with sequential craniofacial and periocular surgeries, coordinated across ophthalmology/oculoplastics, craniofacial/plastic surgery, dentistry/orthodontics, audiology, and clinical genetics — rather than a single-specialty or drug-based algorithm.

---

## 13. Prevention

**Primary prevention:** Not applicable in the population sense — BSS arises from de novo or mosaic-transmitted dominant mutation and has no modifiable environmental risk factor to intervene on.

**Secondary prevention:** Early neonatal ophthalmologic assessment and initiation of ocular-surface protection is the key secondary-prevention measure, aimed at forestalling progression to corneal scarring/vision loss from chronic exposure keratopathy — this is the clearest tertiary/secondary-prevention opportunity documented in the literature reviewed.

**Genetic counseling/reproductive prevention:** For families with a previously affected child (especially where a parent shows even mild/subtle features suggestive of mosaicism), **prenatal or preimplantation genetic testing** using the known familial TWIST2 mutation is the applicable reproductive risk-reduction strategy, directly motivated by the documented germline mosaicism transmission cases (PMID:26119818, PMID:27092433). Recurrence risk counseling should explicitly account for the possibility of parental mosaicism rather than assuming a negligible recurrence risk purely because both parents appear clinically unaffected.

**Screening:** No population, newborn, or carrier screening program is applicable, as discussed in §10.

**Public health/behavioral/immunization/prophylaxis:** Not applicable to this disorder.

---

## 14. Other Species / Natural Disease

**No naturally occurring TWIST2-related disease analogous to Barber-Say syndrome was identified in other species** in this search (no OMIA entry, veterinary case series, or companion-animal report was found). This appears to be a human-specific clinical entity in the literature surveyed, though this absence should be read as "not found in this search" rather than a confirmed negative — a dedicated OMIA search was not exhaustively performed here.

**Orthologous gene:** Twist2 is highly conserved; the mouse ortholog is *Twist2* (MGI:104685, "twist basic helix-loop-helix transcription factor 2"), and zebrafish possess a *twist2/dermo1* ortholog used experimentally (see below and §6). No natural/spontaneous disease-causing Twist2 variant has been reported in these model species outside of engineered/knockout research models.

**Comparative biology:** TWIST2's role in inhibiting mesenchymal (myogenic/osteogenic) differentiation and in dermal fibroblast/scale development is evolutionarily conserved from fish to mammals — e.g., zebrafish *twist2/dermo1* "regulates scale shape and scale organization during skin development and regeneration" (search-identified ScienceDirect source), a functional parallel to its role in mammalian dermal development, though scales are not a direct model for human skin pathology.

---

## 15. Model Organisms

**Mouse (Mus musculus):**
- **Twist2-null (knockout) mice** are the best-characterized mammalian model of TWIST2 loss-of-function, though they model a phenotype closer to the biology relevant to the *recessive* Setleis end of the allelic spectrum (complete loss of function) rather than the dominant-negative/gain-of-function BSS mutations. Reported phenotype: "The Twist2-KO mouse presents relatively normal embryonic development and no notable bone abnormalities, but typically dies 2–3 days after birth due to cachexia, failure to thrive and high levels of pro-inflammatory cytokines," with the mechanism attributed to loss of TWIST2's normal repression of NF-κB-driven pro-inflammatory cytokine expression across multiple tissues, producing apoptosis, cachexia, and neonatal lethality, described as resembling TNFα-induced cachexia models. **This is an important model-fidelity caveat for dismech curation**: the null mouse's dominant, life-limiting phenotype (neonatal lethal systemic cytokine-driven cachexia) is **not** the human BSS phenotype (a viable, non-lethal craniofacial/dermal malformation syndrome) — consistent with the human disease being caused by a dominant dual dominant-negative/gain-of-function missense mechanism rather than simple biallelic loss of function, and any `AnimalModel.modeled_mechanisms` link from a Twist2-null mouse to a BSS pathophysiology node should likely be `PARTIALLY_RECAPITULATES` or `FAILS_TO_RECAPITULATE` at best, with explicit `limitations` describing this genotype mismatch (null vs. dominant-negative/gain-of-function missense) rather than `RECAPITULATES`.
- **No knock-in mouse model carrying the human BSS-specific p.Glu75Gln or p.Glu75Ala substitution was identified in this search** — this appears to be a genuine gap in the literature (an E75K/E75Q/E75A knock-in mouse, which would far more faithfully model the dominant human mutation mechanism, does not appear to have been published as of the sources retrieved here). This is an explicit, actionable knowledge gap worth flagging in a `HUMAN_MODEL_MISMATCH` discussion if this entry is curated in dismech.

**Zebrafish (Danio rerio):**
- Used directly in the pivotal Marchegiani et al. 2015 study to functionally test the human BSS/AMS mutant TWIST2 proteins: expression of mutant TWIST2 produced "severe head hypoplasia" and downregulation of extracellular-matrix, membrane, and cytoskeleton gene expression programs — this is the **most disease-relevant model system identified** for the dominant-negative/gain-of-function mechanism specifically, since it used the actual human disease-causing substitutions rather than a null allele, and directly supports the craniofacial-mesenchyme step of the causal chain in §6.
- Separately, wild-type zebrafish *twist2/dermo1* has been used as a normal-development model for dermal/scale formation, informing general TWIST2 developmental biology rather than disease modeling per se.

**Cell-based/in vitro models:**
- HeLa cell transfection with Flag-tagged wild-type and mutant TWIST2 constructs, used for the ChIP-seq/DNA-binding-pattern comparison described in §6 (PMID:26119818) — an in vitro molecular model of the mechanistic lesion, not a tissue/organismal disease model.
- Patient-derived fibroblasts have been used in the allelic Setleis syndrome literature for expression profiling of TWIST2 target genes (including the periostin/POSTN finding noted in §6) — no equivalent BSS (dominant-negative/gain-of-function allele) patient-fibroblast transcriptomic study was identified in this search, representing a further gap: the mechanistic downstream-target data that exists is largely from the loss-of-function (Setleis) side of the allelic series, not from BSS's own gain-of-function/dominant-negative alleles.

**Model limitations, summarized:** No model organism currently available (null mouse, zebrafish mutant-TWIST2 embryo, or in vitro assay) fully recapitulates the complete human BSS phenotype (combined hypertrichosis + cutis-laxa-like skin + ectropion + macrostomia + normal viability/typically normal cognition) in a single system; the null mouse models a different (lethal, cytokine-driven) end of the TWIST2 loss-of-function spectrum, and the zebrafish data — while using the correct disease-causing mutation — captures gross craniofacial hypoplasia and gene-expression changes rather than the specific eyelid/dermal/hair-follicle phenotypes that define the human clinical picture.

---

## Summary of Key Citations

| PMID/DOI | Citation | Relevance |
|---|---|---|
| PMID:26119818 | Marchegiani S, et al. "Recurrent Mutations in the Basic Domain of TWIST2 Cause Ablepharon Macrostomia and Barber-Say Syndromes." *Am J Hum Genet.* 2015;97(1):99-110. | Primary molecular-genetics/mechanism paper; genotype-phenotype correlation; zebrafish and HeLa functional data; mosaicism |
| PMID:20691403 | Kowalczyk C, et al. "Homozygous Nonsense Mutations in TWIST2 Cause Setleis Syndrome." *Am J Hum Genet.* 2010;87(2):289-96. | Allelic recessive/loss-of-function disorder; mechanistic contrast |
| PMID:27092433 | Singh A, et al. "Transmission of Barber-Say syndrome from a mosaic father to his child in an Indian family." *Clin Dysmorphol.* 2016;25(4):181-185. | Germline mosaicism transmission, phenotype severity gradient |
| PMID:19760652 | Case report supporting that the Barber-Say and ablepharon macrostomia syndromes could represent one disorder. | Lump/split argument for BSS/AMS continuum |
| PMID:29329175 | "Clinical Description, Molecular Analysis of TWIST2 Gene, and Surgical Treatment in a Patient With Barber-Say Syndrome." *Ophthalmic Plast Reconstr Surg.* | Surgical/ophthalmologic management |
| PMID:30455119 | "Multidisciplinary eyelid reconstruction in Barber-Say syndrome: A case report." | Detailed eyelid reconstructive technique |
| PMID:28680619 / PMC5494409 | Yohannan et al. "Barber-say syndrome: a confirmed case of TWIST2 gene mutation." *Clin Case Rep.* 2017. | Molecular confirmation case report |
| PMID:8368246 | "Hypertrichosis, atrophic skin, ectropion, and macrostomia (Barber-Say syndrome): report of a new case." 1993. | Early clinical case delineation |
| PMID:9415700 | "Macrostomia, hypertelorism, atrophic skin, severe hypertrichosis without ectropion: milder form of Barber-Say Syndrome." | Phenotypic spectrum/expressivity |
| PMID:28690482 | "Barber-Say Syndrome and Ablepharon-Macrostomia Syndrome: A Patient's View." *Mol Syndromol.* 2017. | Patient-perspective/QOL-adjacent content |
| ORPHA:1231 | Orphanet entry, Barber-Say syndrome | Prevalence, synonym/definition source |
| OMIM #209885 / *607556 | OMIM phenotype and gene entries | Clinical synopsis, nomenclature (note: full OMIM text could not be directly fetched in this session — HTTP 403 — so OMIM content above is drawn from indexed secondary summaries and should be re-verified against the live OMIM entry before formal curation) |

---

## Explicit gaps and caveats for curation

1. **OMIM full-text access failed** (HTTP 403) during this research session; the OMIM-attributed statements above come from search-engine-indexed excerpts of the OMIM entry/clinical synopsis, not a direct read of the primary source, and should be re-fetched and re-verified before being cited as OMIM content in a KB entry.
2. **The periostin/POSTN target-gene finding** is reported here at title/abstract-summary level only (PMC7922891 could not be fetched past a bot-check page); treat as an unverified lead, not a quotable finding, and it concerns Setleis syndrome (loss-of-function) fibroblasts, not BSS's dominant-negative/gain-of-function alleles specifically.
3. **The apparent "autosomal recessive" inheritance tag for BSS** surfaced in one aggregator search result and is very likely a database-level conflation with the genuinely recessive allelic disorder Setleis syndrome; do not curate BSS itself as having AR inheritance without independent primary-source verification.
4. **No current, precise total case count** was obtained (most specific figures found ranged from "11" (Orphanet, pre-2015) to "~15" (2017) to "<20" (2019); a fresh count was not independently performed here).
5. **No GeneReviews chapter** and **no formal natural-history, registry, or QOL-instrument study** exist for this condition — all clinical-course, prognosis, and QOL content in this report is aggregated from individual case reports, which should be reflected in evidence grading (individual human clinical case-report evidence, not cohort-level).
6. **No knock-in mouse model of the human BSS mutation** was found — an explicit, worth-flagging translational gap between the available Twist2-null mouse (a different, lethal loss-of-function phenotype) and the human dominant-negative/gain-of-function disease.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 12 |
| On topic | 10 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMID:26119818`: "The mutations are located in the basic domain of the protein, and molecular analyses suggested that the mutations alter the DNA-binding activity of TWIST2, leading to both dominant-negative and gain-of-function effects"
  - closest text in source: "Molecular analyses suggest that these mutations alter the DNA-binding activity of TWIST2, leading to both dominant-negative and gain-of-function effects"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 50 |
| Resolved | 45 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 3 |
| Terms whose name was checked | 14 |
| Terms named correctly | 8 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000656` (1 mention) - the report calls it "Ectropion (bilateral, of both upper and lower eyelids)"; HP calls it **Ectropion**
- `UBERON:0004085` (1 mention) - the report calls it "eyelid"; UBERON calls it **labium majora**
- `UBERON:0000151` (1 mention) - the report calls it "nasal region"; UBERON calls it **pectoral fin**
- `UBERON:0000202` (1 mention) - the report calls it "mouth region"; UBERON calls it **glial blood brain barrier**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0007756` (obsolete Slitlike anterior chamber angles in children) (1 mention) - replaced by `HP:0000594`
- `GO:0043433` (obsolete negative regulation of DNA-binding transcription factor activity) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000154` (1 mention) - the report calls it "Macrostomia (wide mouth)"; HP calls it **Wide mouth**
- `HP:0001263` (1 mention) - the report calls it "Mild psychomotor/developmental delay"; HP calls it **Global developmental delay**, and lists "Psychomotor developmental delay" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.