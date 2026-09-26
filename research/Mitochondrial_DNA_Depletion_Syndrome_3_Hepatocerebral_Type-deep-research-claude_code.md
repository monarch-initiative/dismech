---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-23T15:00:40.212710'
end_time: '2026-09-23T15:05:20.085847'
duration_seconds: 279.87
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Mitochondrial DNA Depletion Syndrome 3 (Hepatocerebral Type)
  mondo_id: MONDO:0009636
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
  web_search_requests: 18
  num_turns: 24
  total_cost_usd: 1.5838291999999998
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
citation_count: 32
reference_validation:
  total_references: 23
  verified: 22
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.043
  quotes_checked: 1
  quotes_valid: 0
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMC:PMC11043827
  relevance_assessed: 22
  on_topic: 17
  unresolved_references:
  - PMID:34167177
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 40
  verified: 38
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 28
  labels_matching: 19
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: MONDO:0009636
    reported_labels:
    - MONDO
    ontology_label: mitochondrial DNA depletion syndrome 3 (hepatocerebral type)
  - term_id: HP:0031982
    reported_labels:
    - Opsoclonus
    ontology_label: Abnormal putamen morphology
  - term_id: HP:0009053
    reported_labels:
    - limb-specific if documented
    ontology_label: Distal lower limb muscle weakness
  labels_variant: 6
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
- **Disease Name:** Mitochondrial DNA Depletion Syndrome 3 (Hepatocerebral Type)
- **MONDO ID:** MONDO:0009636 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Mitochondrial DNA Depletion Syndrome 3 (Hepatocerebral Type)** covering all of the
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

I'll research Mitochondrial DNA Depletion Syndrome 3 (Hepatocerebral Type / DGUOK-related) now, starting with foundational sources.

I now have comprehensive material to compile the full report.

# Mitochondrial DNA Depletion Syndrome 3, Hepatocerebral Type (DGUOK Deficiency) — Comprehensive Research Report

## Identifiers

| System | ID |
|---|---|
| OMIM (phenotype) | #251880 — MITOCHONDRIAL DNA DEPLETION SYNDROME 3 (HEPATOCEREBRAL TYPE); MTDPS3 |
| OMIM (gene) | *601465 — DEOXYGUANOSINE KINASE; DGUOK |
| MONDO | MONDO:0009636 |
| Orphanet | ORPHA:279934 — Mitochondrial DNA depletion syndrome, hepatocerebral form due to DGUOK deficiency |
| Gene symbol / HGNC | DGUOK, chromosome 2p13 |
| ICD-10 | E88.8 (other specified metabolic disorders) |
| ICD-11 | 5C53.20 |
| GeneReviews | "Deoxyguanosine Kinase Deficiency" (NBK7040; last updated Feb 9, 2023) |
| Inheritance | Autosomal recessive |

**Synonyms:** DGUOK deficiency; MTDPS3; hepatocerebral mitochondrial DNA depletion syndrome due to DGUOK deficiency; deoxyguanosine kinase deficiency; mtDNA depletion syndrome, hepatocerebral form. Not to be confused with other hepatocerebral MDDS caused by MPV17, POLG1, TWNK/C10orf2, or TFAM (genetically distinct, mechanistically related entries), nor with MDDS-6 (TK2, myopathic form), which has a different phenotype despite salvage-pathway overlap.

Most information below is aggregated, retrospective case-series/literature-review-level evidence (individual case reports and one large systematic pooled cohort), not prospective EHR/registry data — this is characteristic of an ultra-rare autosomal recessive disorder.

---

## 1. Disease Overview

DGUOK deficiency is an autosomal recessive mitochondrial DNA maintenance disorder caused by biallelic pathogenic variants in *DGUOK*, encoding mitochondrial deoxyguanosine kinase (dGK), the rate-limiting enzyme of the mitochondrial purine deoxyribonucleoside salvage pathway. Loss of enzyme activity starves replicating mitochondria of deoxynucleotide triphosphates (dNTPs), causing tissue-specific depletion of mitochondrial DNA copy number, predominantly in liver and, to a lesser and more variable extent, muscle and brain. The resulting oxidative phosphorylation (OXPHOS) failure produces a clinical spectrum ranging from a lethal neonatal hepatocerebral syndrome to isolated adult-onset myopathy.

> "The main supply of deoxyribonucleotides (dNTPs) for mtDNA synthesis comes from the salvage pathway initiated by deoxyguanosine kinase and thymidine kinase-2, and the association of mtDNA depletion with mutated DGUOK suggested that these salvage pathway enzymes are involved in the maintenance of balanced mitochondrial dNTP pools." — [OMIM #251880](https://omim.org/entry/251880)

A large pooled natural-history analysis (202 genetically confirmed patients, 36 unpublished + 166 from systematic literature review 2001–2023) is the largest available characterization and is the primary quantitative source below (Vantroys et al./co-authors, *Brain Communications* 2024, PMID:38756539; PMC11098040) — cite this as the source class throughout (structured aggregation of predominantly HUMAN_CLINICAL case reports).

---

## 2. Etiology

### 2a. Causal factor
Sole known cause: biallelic (homozygous or compound heterozygous) loss-of-function pathogenic variants in *DGUOK* (601465). No environmental, infectious, or purely mechanistic (non-genetic) cause is described. First reported by Mandel et al. 2001 (PMID:11687800), who identified a founder 1-bp deletion (c.204delA / historically "204delA") in three unrelated Israeli-Druze kindreds.

### 2b. Genetic risk factors
- Biallelic pathogenic *DGUOK* variants are necessary and sufficient.
- A second Israeli-Druze founder allele and other population-specific founder variants exist (see §9).
- No modifier genes have been established; the 2024 pooled cohort explicitly states **"no genotype–phenotype correlation"** could be established for variant type vs. phenotype class, although:
  - Truncating variants (nonsense, frameshift) trended toward association with the more severe neonatal/infantile hepatocerebral phenotype and higher mortality risk in the literature-review synthesis.
  - Missense variants comprised ~47% of the 82 distinct pathogenic variants catalogued in the cohort; truncating variants ~39%; rare small in-frame/large-scale deletions the remainder.
  - Three recurrent variants accounted for a substantial minority of alleles: c.255del (p.Ala86Profs*13, 10.4%), c.3G>A (p.Met1Ile, 9.9%), c.763_766dupGATT (p.Phe256*, 8.9%).

### 2c. Environmental/lifestyle risk or protective factors
None established — this is a purely monogenic disorder; there is no known environmental trigger, protective exposure, or gene-environment interaction reported in the literature.

### 2d. Gene-environment interaction
Not applicable/not reported.

---

## 3. Phenotypes

The 2024 pooled cohort (n=202, largest available) identified **four distinct clinical phenotype clusters**, replacing the older simple "hepatocerebral vs. isolated hepatic" dichotomy from GeneReviews with a finer four-way split:

| Phenotype | % of cohort | Typical onset |
|---|---|---|
| Hepatocerebral | 58.8% | Neonatal 65.1%, infantile 34.9% |
| Isolated hepatopathy | 21.9% | Neonatal 51.3%, infantile 43.6% |
| Hepatomyoencephalopathy | 9.6% | Neonatal 77.8%, infantile 22.2% |
| Isolated myopathy | 9.6% | Adult-onset 83.3% |

### Age-of-onset distribution (overall, n=158 with data)
- Neonatal (≤1 month): 55.7%
- Infantile (>1 month–1 year): 32.3%
- Pediatric (1–18 years): 2.5%
- Adult (>18 years): 9.5%

### Hepatic phenotypes (88.1% of patients overall)
| Feature | Frequency at onset |
|---|---|
| Elevated ALT/AST | 72.5% |
| Jaundice | 58.8% |
| Cholestasis | 57.5% |
| Hepatomegaly | 45.6% |
| Ascites | 16.3% |
Suggested HP terms: HP:0002240 (Hepatomegaly), HP:0000952 (Jaundice), HP:0001396 (Cholestasis), HP:0001392 (Abnormality of the liver)/HP:0001744 (Splenomegaly if present), HP:0001410 (Decreased liver function); progresses to HP:0001399 (Hepatic failure).

### CNS/neurologic phenotypes (68% of patients overall)
| Feature | Frequency at onset |
|---|---|
| Central hypotonia | 48.1% |
| Nystagmus (classically rotary, evolving to opsoclonus) | 32.6% |
| Psychomotor delay/regression | 23.8% |
| Lethargy | 7.7% |
Suggested HP terms: HP:0001290 (Generalized hypotonia), HP:0000639 (Nystagmus) — GeneReviews and multiple case series specifically describe **rotary nystagmus progressing to opsoclonus**, HP:0031982 (Opsoclonus) if a dedicated term is used, HP:0001263 (Global developmental delay) / HP:0002376 (Developmental regression).

### Neuromuscular phenotypes (23.9% at onset; dominates the adult "isolated myopathy" cluster)
| Feature | Frequency |
|---|---|
| Weakness/fatigue | 20.8% |
| Ptosis | 13.8% |
| Progressive external ophthalmoplegia (PEO/CPEO) | 8.8% |
Suggested HP terms: HP:0003324 (Generalized muscle weakness) or HP:0009053 (limb-specific if documented), HP:0000508 (Ptosis), HP:0000590 (Progressive external ophthalmoplegia). A separate case report documents CPEO with mtDNA multiple deletions in a compound-heterozygous adult (PMID not captured verbatim here — Montano et al. 2019, *Case Rep Neurol Med*).

### Laboratory abnormalities
| Finding | Frequency |
|---|---|
| Metabolic acidosis | 52.5% |
| Hypoglycemia | 49.5% |
| Elevated plasma tyrosine | 64% (creates diagnostic overlap/confusion with Tyrosinemia type I) |
| Creatine kinase elevation | 1.2–11.8× ULN (excluding rhabdomyolysis cases) |
Additional findings from case series (GeneReviews; Kalkan Uçar et al. 2021, PMID:34167177): hyperlactatemia, elevated alpha-fetoprotein (AFP), elevated alanine, coagulopathy. Notably, hyperlactatemia "may be absent or only mild in the early stages," and two patients in the 2021 case series mimicked neonatal hemochromatosis and tyrosinemia type I respectively, underscoring a real diagnostic pitfall. A 2025 report specifically documents DGUOK-MDDS **without marked hyperlactatemia** presenting as isolated neonatal cholestasis (PMC13141804), and separate reports document presentation with **hyperinsulinemic hypoglycemia** (PMC10646319).

### Neuroimaging
Of 65 patients with brain MRI reported, 38.5% had abnormalities:
- White matter abnormalities: 36%
- Cortical/subcortical atrophy: 32%
- Cerebellar atrophy: 12%
- Lactate peak on MR spectroscopy: 75% (6/8 tested)

### Severity/progression/quality of life
Symptom severity is highly variable and correlates strongly with age of onset (below). Neonatal/infantile hepatocerebral disease is rapidly progressive and typically fatal within the first year of life absent transplantation; adult-onset isolated myopathy is comparatively indolent (mean age at last follow-up 51.1 years, 85.7% alive). No formal QoL instrument (EQ-5D/SF-36/PROMIS) data specific to this disease were identified in the literature searched.

---

## 4. Genetic/Molecular Information

- **Causal gene:** DGUOK (HGNC symbol; OMIM *601465), chromosome 2p13, encoding mitochondrial deoxyguanosine kinase.
- **Protein function:** dGK catalyzes the first, rate-limiting step of the mitochondrial purine deoxyribonucleoside salvage pathway — phosphorylation of deoxyguanosine (dGuo) and deoxyadenosine (dAdo) to dGMP and dAMP, respectively, for downstream conversion to dGTP/dATP used in mtDNA replication. GO term suggestion: GO:0004137 (deoxyguanosine kinase activity); the broader process is GO:0006206 (pyrimidine nucleobase metabolic process)/more precisely GO:0009157 (deoxyribonucleoside monophosphate biosynthetic process) and GO:0006264 (mitochondrial DNA replication) as the downstream consequence.
- **Variant spectrum:** 82 distinct pathogenic variants catalogued across the DGUOK gene's 7 exons in the 2024 pooled cohort: missense 47%, truncating (nonsense/frameshift) 39%, rare small in-frame or large structural deletions the remainder. Recurrent/founder alleles: c.204delA (Israeli-Druze founder, original 2001 report, PMID:11687800); c.255del (p.Ala86Profs*13, 10.4% of cohort alleles); c.3G>A (p.Met1Ile, 9.9%); c.763_766dupGATT (p.Phe256*, 8.9%).
- **Classification:** ACMG/AMP classification is variant-specific (ClinVar entries exist per-variant, e.g., NM_080916.3 transcript-based nomenclature such as c.708-3T>C, c.366G>C p.Gln122His). Check ClinVar/ClinGen directly for a given variant before curating pathogenicity; a formal ClinGen Gene-Disease Validity curation specific to DGUOK–MDDS3 was not located in this search pass and should be independently confirmed (CGGV: prefix) before citation.
- **Genotype-phenotype correlation:** Explicitly **not established** for phenotype cluster; truncating variants "were associated with higher risk of death and the neonatal/infantile-onset hepatocerebral disease phenotype" per the 2024 cohort synthesis, but this is a trend from pooled literature review rather than a formally tested statistical genotype-phenotype model with the caveats that entails.
- **Somatic vs. germline:** Exclusively germline; no somatic DGUOK association with disease reported. (Note: a separate, unrelated oncology literature describes DGUOK's role in cancer cell stemness in lung adenocarcinoma — PMC6895611 — which is a distinct, non-Mendelian research area and not part of this disease entry.)
- **Epigenetic information:** No disease-specific DNA methylation/histone modification studies for MTDPS3 were identified. A 2025 mechanistic bioRxiv preprint (Deoxyguanosine Kinase Deficiency Couples Purine Metabolism to Innate Immune Activation and Lipid Accumulation in Hepatocytes) reports that acute DGUOK loss triggers **epigenetic remodeling and derepression of human endogenous retroviruses (HERVs) and interferon-stimulated genes (ISGs)**, upstream of overt mtDNA depletion — an emerging, not-yet-fully-validated mechanistic finding (preprint, not peer-reviewed at time of this report).
- **Chromosomal abnormalities:** None reported; this is a point-variant/small-indel disorder, not a structural genomic disorder.

---

## 5. Environmental Information

No environmental, lifestyle, or infectious contributing factors are described for this monogenic disorder. Not applicable.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. Biallelic loss-of-function variants in *DGUOK* **abolish or severely reduce** mitochondrial deoxyguanosine kinase (dGK) enzymatic activity.
2. Loss of dGK activity **eliminates the mitochondrial purine deoxyribonucleoside salvage pathway's** capacity to phosphorylate deoxyguanosine/deoxyadenosine to dGMP/dAMP, the precursors of dGTP/dATP.
3. Because postmitotic/quiescent and rapidly dividing hepatocytes rely heavily on this salvage route (rather than only on cytosolic de novo synthesis and nucleotide import) for mitochondrial dNTP supply, this **causes an imbalanced and insufficient mitochondrial dNTP pool**, disproportionately affecting liver.
4. Insufficient/unbalanced dNTP pools **impair mtDNA replication fidelity and copy-number maintenance**, leading to tissue-specific mtDNA depletion — most severe and consistent in liver (100% of 58 liver samples in the pooled cohort showed depletion, median 15.8% of control), more variable in muscle (66.7% of 30 samples depleted; median 30.7%) and less consistently affecting brain directly (brain mtDNA depletion is inferred rather than routinely biopsied).
5. Reduced mtDNA copy number **causes insufficient transcription/translation of the 13 mtDNA-encoded OXPHOS subunits**, producing combined respiratory chain complex deficiency — liver homogenates in the pooled cohort showed multiple OXPHOS defects in 92.2% of samples (isolated complex I, III, or IV deficiency each in only ~3.1%).
6. Combined OXPHOS failure in hepatocytes **leads to energy failure, oxidative stress, and (per recent mechanistic work) ferroptosis** — a 2021 iPSC-derived liver organoid/hepatocyte study (Guo et al., *Adv Sci* 2021; PMID:34026460) showed DGUOK-mutant hepatocyte-like cells and organoids are selectively sensitized to **iron-overload-induced ferroptosis**, mediated by NCOA4-dependent ferritinophagy and labile iron release, rescuable in vitro by N-acetylcysteine — proposed as the mechanistic bridge between mtDNA depletion and the iron-overload/liver failure phenotype seen clinically in many DGUOK-mutant patients.
7. In parallel (branch), a 2025 mechanistic study proposes an **upstream, mtDNA-depletion-independent branch**: acute DGUOK loss disrupts mitochondrial purine metabolism sufficiently to trigger **innate immune activation (type I interferon/ISG signaling via HERV derepression) and hepatocyte lipid accumulation (steatosis) even before overt mtDNA depletion or mitochondrial dysfunction develop** — suggesting the disease process begins as a purine-metabolic/innate-immune insult that precedes, and may compound, the classical bioenergetic mechanism (preprint; inferred, not yet independently replicated).
8. Combined bioenergetic failure, oxidative/ferroptotic hepatocyte injury, and steatosis/fibrosis **culminate clinically in progressive cholestatic liver disease → hepatocellular necrosis/fibrosis/cirrhosis → liver failure** (histology: steatosis 70.1%, cholestasis 59.8%, fibrosis 56.3%, cirrhosis 33.3% of 87 biopsies) — the leading cause of death (72.3% of 112 documented deaths).
9. In parallel in the CNS, mtDNA depletion/OXPHOS failure in neurons and oligodendrocytes is inferred (based on MRI findings of white-matter change/cortical-subcortical/cerebellar atrophy and lactate peaks on MRS) to **drive the neurologic manifestations** — hypotonia, nystagmus/opsoclonus, and developmental regression — though the tissue-level mechanistic data in brain is far less direct than in liver (brain biopsy is not performed clinically; mechanism here is more strongly inferred than demonstrated).
10. In skeletal muscle (the dominant tissue in the adult-onset "isolated myopathy" cluster), a chronic, lower-grade mtDNA depletion together with **secondary accumulation of multiple mtDNA deletions** (documented in 14/58 muscle samples, associated specifically with adult-onset myopathy) drives progressive external ophthalmoplegia, ptosis, and limb weakness via a slower, myopathy-predominant course — mechanistically analogous to other mtDNA-maintenance disorders (e.g., POLG, TWNK) that cause secondary multiple mtDNA deletions.

### Molecular pathways / cellular processes
- Mitochondrial purine deoxyribonucleoside salvage pathway (dGK/TK2 axis) — GO:0006206, GO:0009157.
- mtDNA replication/maintenance — GO:0006264.
- Oxidative phosphorylation/electron transport chain — GO:0006119, GO:0022904.
- Ferroptosis (iron-dependent lipid peroxidation cell death) — an emerging GO annotation would be GO:0097707 (ferroptosis).
- Type I interferon signaling / innate immune activation via HERV derepression (emerging mechanism, preprint-level evidence).
- Autophagy/ferritinophagy (NCOA4-mediated) contributing to labile iron pool expansion.

### Protein dysfunction
Loss-of-function (most missense and essentially all truncating variants) rather than dominant-negative or gain-of-function; enzymatic activity assays in patient fibroblasts/liver typically show markedly reduced or absent dGK activity.

### Cell types and tissues implicated
- **Hepatocyte** (CL:0000182) — primary target, site of most severe mtDNA depletion.
- Skeletal muscle fiber (CL:0000188/CL:0000187) — variable depletion, secondary mtDNA deletions in adult-onset disease; COX-deficient fibers in 42.2% and ragged red fibers in 28.9% of 45 muscle biopsies.
- Neuron (CL:0000540) — inferred CNS involvement (imaging-based, not biopsy-confirmed).
- Subcellular: mitochondrion (GO:0005739), mitochondrial matrix (GO:0005759) — site of dGK activity and mtDNA replication.

### Molecular/-omics profiling
- **iPSC-derived liver organoid/hepatocyte model**: demonstrates ferroptosis sensitization mechanistically (PMID:34026460).
- No large-scale disease-specific transcriptomic/proteomic/metabolomic dataset (GEO/PRIDE/MetaboLights) specific to MTDPS3 patient tissue was identified in this search; most molecular characterization to date is candidate-gene/pathway-focused (respiratory chain enzymology, mtDNA quantification) rather than unbiased multi-omics.

---

## 7. Anatomical Structures Affected

### Organ level
- **Primary:** Liver (UBERON:0002107) — dominant and most life-threatening involvement.
- **Secondary/CNS:** Brain (UBERON:0000955) — in the hepatocerebral and hepatomyoencephalopathy clusters.
- **Secondary/muscle:** Skeletal muscle (UBERON:0001134) — dominant in the isolated-myopathy adult cluster, variably present in other clusters.
- **Eye:** Extraocular muscles (ptosis, PEO, nystagmus) implicate oculomotor pathways/extraocular muscle (UBERON:0004807) as well as central vestibulo-ocular circuitry for nystagmus/opsoclonus.
- Body systems: hepatobiliary, nervous (central and, in myopathic cases, motor unit/neuromuscular), musculoskeletal (secondary via myopathy).

### Tissue/cell level
- Hepatocytes (CL:0000182) — primary affected population; steatotic, cholestatic, fibrotic/cirrhotic change on biopsy.
- Skeletal myofibers — COX-deficient and ragged-red fibers on histochemistry.
- CNS white matter (oligodendrocyte-associated) and cortical/cerebellar gray matter — implicated by MRI (atrophy, white-matter signal change) rather than direct histology.

### Subcellular level
- Mitochondria (GO:0005739) / mitochondrial matrix (GO:0005759) — the organelle compartment of the primary molecular defect (dGK enzyme localizes to the mitochondrial matrix).
- Lysosome — implicated secondarily via NCOA4-mediated ferritinophagy in the ferroptosis mechanism.

### Localization/lateralization
Bilateral, symmetric, systemic involvement — no lateralization reported (expected for a metabolic/mtDNA-maintenance disorder rather than a structural malformation).

---

## 8. Temporal Development

### Onset
- Neonatal (≤1 month): 55.7% of cohort — dominant in hepatocerebral (65.1%) and hepatomyoencephalopathy (77.8%) clusters.
- Infantile (1 month–1 year): 32.3%.
- Pediatric (1–18 years): 2.5% (rare).
- Adult (>18 years): 9.5% — dominant in the isolated-myopathy cluster (83.3% adult-onset).
- Onset pattern: typically acute/subacute in the neonatal-infantile hepatocerebral forms (rapid liver failure over days-to-weeks); chronic/insidious in the adult myopathic form.

### Progression
- **Neonatal-onset hepatocerebral/hepatomyoencephalopathy disease:** rapidly progressive, typically fatal — median survival 0.5 years (Kaplan-Meier, neonatal-onset subgroup); 93.4% mortality (99/106) in the hepatocerebral cluster specifically, at an average age of death of 6.79 months.
- **Infantile-onset disease:** median survival 1.17 years — somewhat better than neonatal-onset but still poor without transplantation.
- **Adult-onset isolated myopathy:** indolent, chronic, slowly progressive — median survival 67 years; 85.7% alive at last follow-up (mean age 51.1 years).
- Statistical comparison across onset-age groups: p<0.0001 (Kaplan-Meier log-rank), confirming age of onset as the dominant prognostic determinant.
- Disease course pattern: generally monotonically progressive rather than relapsing-remitting; no spontaneous remission described. Liver transplantation, where performed, alters (improves) the liver-failure trajectory specifically (see §12) but does not reverse pre-existing neurologic injury.

### Critical periods
The neonatal period is the critical window both for diagnosis (before irreversible liver failure/neurologic injury) and for the liver-transplantation decision, since **pre-transplant neurologic status (specifically nystagmus at onset) is a significant predictor of post-transplant survival** (p=0.0275) — i.e., early recognition before neurologic progression is a genuine intervention window.

---

## 9. Inheritance and Population

### Epidemiology
- DGUOK deficiency is described as **"one of the most common causes of the hepatocerebral form of mitochondrial DNA depletion syndromes"** ([Orphanet ORPHA:279934](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=279934)), with "more than 100 cases of MDS" described in the Orphanet summary (superseded quantitatively by the 202-patient pooled cohort above, which is the more current figure).
- No formal population-based incidence/prevalence rate (cases per 100,000) was located; this is consistent with dismech's `prevalence_class: NOT_YET_DOCUMENTED` or a `CASES_IN_LITERATURE` measure_type given the case-series/literature-review nature of the denominator.
- An early OMIM annotation states DGUOK mutations were found in 3/21 (14%) of a hepatocerebral MDDS cohort tested — illustrating that DGUOK is a significant but partial contributor to the broader hepatocerebral MDDS genetic-heterogeneity group (alongside MPV17, POLG1, TWNK, TFAM).

### Inheritance pattern
Autosomal recessive. At conception, each sibling of an affected individual has a 25% chance of being affected, 50% chance of being an asymptomatic carrier, 25% chance of being unaffected/non-carrier (standard AR recurrence risk, per GeneReviews-sourced counseling language).

### Penetrance/expressivity
Full penetrance is generally assumed for biallelic loss-of-function variants, but **expressivity is markedly variable** — the four-cluster phenotype classification (hepatocerebral / isolated hepatopathy / hepatomyoencephalopathy / isolated myopathy) spanning neonatal death to indolent adult myopathy in carriers of pathogenic biallelic DGUOK variants is itself evidence of wide phenotypic variability not fully explained by genotype.

### Genetic anticipation / germline mosaicism
Not reported for this disorder (not a repeat-expansion disease).

### Founder effects
- **Israeli-Druze founder variant** c.204delA (1-bp deletion, exon 2) — identified in the original 2001 description in three unrelated Druze kindreds (PMID:11687800), and Orphanet's Druze-population founder-variant resource independently catalogues DGUOK among Druze founder-variant disorders.
- No Ashkenazi Jewish founder variant for DGUOK specifically was identified in this search (in contrast to many other AR disorders in that population); do not assume AJ founder status without direct confirmation.
- Multiple additional population-specific recurrent variants are implied by the pooled cohort's top-3 recurrent alleles (c.255del, c.3G>A, c.763_766dupGATT), but their specific ethnic/geographic origins were not resolved in this pass and should be verified per-variant against ClinVar/gnomAD population data before curation.

### Consanguinity
Given the AR inheritance and founder-population pattern (Druze), consanguinity is a plausible risk-elevating factor in specific populations, consistent with general AR-disorder epidemiology, though not separately quantified in the sources reviewed here.

### Sex ratio / population demographics
Pooled cohort: 88 male, 96 female, 18 undisclosed — essentially equal sex distribution (as expected for autosomal, non-sex-linked inheritance).

---

## 10. Diagnostics

### Clinical/laboratory tests
- Liver function panel: ALT/AST, bilirubin (cholestasis), coagulation studies (coagulopathy is common and an important marker of hepatic synthetic failure).
- Lactate (may be normal or only mildly elevated early — a documented diagnostic pitfall) and lactate:pyruvate ratio.
- Plasma amino acids: elevated tyrosine (64% of cohort) — creates diagnostic overlap with Tyrosinemia type I; alpha-fetoprotein is also markedly elevated (shared with tyrosinemia and neonatal hemochromatosis, both documented as diagnostic mimics in case series).
- Creatine kinase — mildly to moderately elevated (1.2–11.8× ULN), a myopathy-adjacent clue.
- Newborn screening: elevated tyrosine/phenylalanine on NBS is a documented (non-specific) prompt for further work-up in at least one report, though DGUOK-MDDS3 is not itself a standard NBS-panel target condition.

### mtDNA copy-number quantification (tissue-based, central to diagnosis)
- Liver: **mtDNA copy number typically <20% of age-matched control** is the diagnostically suggestive threshold (Orphanet); pooled cohort shows depletion in 100% of 58 liver samples (median 15.8% of control, range 0–98%).
- Muscle: depletion less consistent — 66.7% of 30 samples (median 30.7%, range 6–89%); 33.3% had normal muscle mtDNA copy number, meaning a normal muscle result does not exclude the diagnosis (liver remains the more sensitive tissue).
- Muscle: secondary multiple mtDNA deletions in 14/58 samples — this finding is specifically associated with the adult-onset myopathic phenotype and can be a diagnostic clue in that presentation (may initially suggest a primary mtDNA-maintenance disorder of a different genetic class).

### Respiratory chain enzymology
- Liver homogenate (n=64): combined/multiple OXPHOS complex deficiency in 92.2%; isolated complex I, III, or IV deficiency in only ~3.1% each — i.e., a combined defect pattern is far more typical and more diagnostically suggestive of an mtDNA-maintenance disorder (as opposed to a single-complex-assembly defect).
- Muscle homogenate (n=44): multiple OXPHOS deficiency 31.8%; normal activity in 47.75% — again underscoring that a normal muscle respiratory-chain result does not exclude the diagnosis.

### Histopathology
- Liver biopsy (n=87): steatosis 70.1%, cholestasis 59.8%, fibrosis 56.3%, cirrhosis 33.3%.
- Muscle biopsy (n=45): COX-deficient fibers 42.2%, ragged red fibers 28.9%.

### Neuroimaging
Brain MRI abnormal in 38.5% of 65 imaged patients (white matter change 36%, cortical/subcortical atrophy 32%, cerebellar atrophy 12%); MR spectroscopy lactate peak in 75% (6/8) when performed.

### Molecular genetic testing
- **Confirmatory:** identification of biallelic pathogenic *DGUOK* variants (Sanger sequencing of the single gene, targeted hepatocerebral-MDDS multigene panel [DGUOK, MPV17, POLG, TWNK, TFAM], or whole-exome/genome sequencing).
- Per Orphanet: diagnosis is "suggested by clinicopathological correlation ... with the finding of reduced mtDNA copy numbers in liver or muscle ... and confirmed by the presence of biallelic pathogenic mutations in the DGUOK gene."
- Uniparental isodisomy has been documented as a mechanism producing apparent homozygosity in autosomal recessive MDDS more broadly (detectable by high-density SNP array; PMC7512120), relevant to interpreting an apparently homozygous DGUOK finding with only one carrier parent.

### Differential diagnosis
- Other hepatocerebral MDDS genes: **MPV17** (also causes severe early liver failure, often with peripheral neuropathy, distinguished genetically), **POLG1**, **TWNK/C10orf2**, **TFAM** — genetically and to some extent phenotypically overlapping; multigene panel or exome sequencing is the practical diagnostic approach given this overlap.
- **Tyrosinemia type I** — mimicked by elevated tyrosine and AFP; distinguished by succinylacetone (elevated in tyrosinemia, not in DGUOK deficiency) and by NTBC responsiveness.
- **Neonatal hemochromatosis/gestational alloimmune liver disease** — mimicked clinically; distinguished by iron studies, MRI, and (where performed) buccal mucosa biopsy for extrahepatic siderosis, plus DGUOK-negative molecular/mtDNA testing.
- Glycogen storage disease — at least one case report describes initial misdiagnosis as GSD before DGUOK-MDDS3 was recognized (PMID:22868686).
- TK2-related myopathic MDDS (MDDS-6) — genetically distinct salvage-pathway partner enzyme but a different (myopathic, not hepatocerebral) clinical phenotype; important to distinguish because TK2 deficiency now has an approved deoxynucleoside therapy (see §12) not indicated for DGUOK deficiency.

### Screening
- No population-based newborn-screening panel specifically targets DGUOK deficiency; recognition currently depends on clinical suspicion plus secondary NBS findings (tyrosine/phenylalanine elevation) or targeted work-up of unexplained neonatal cholestasis/liver failure.
- Prenatal/preimplantation genetic testing is available once familial pathogenic variants are known; targeted prenatal testing for known familial DGUOK variants has been performed in reported families.

---

## 11. Outcome/Prognosis

### Survival (Kaplan-Meier, pooled cohort, p<0.0001 across onset-age strata)
- Neonatal onset: median survival **0.5 years**.
- Infantile onset: median survival **1.17 years**.
- Pediatric onset: not estimable (too few cases).
- Adult onset: median survival **67 years**.
- Hepatocerebral cluster specifically: **93.4% mortality** (99/106), mean age at death 6.79 months.
- Isolated myopathy cluster: **85.7% alive** at last follow-up, mean age 51.1 years.

### Causes of death (n=112 documented deaths)
- Liver failure: 72.3% (dominant cause).
- Multi-organ failure: 10.7%.
- Encephalopathy: 4.5%.
- (Remainder unspecified/other in the source.)

### Morbidity/disability
Survivors of the neonatal/infantile hepatocerebral form who do not undergo (or do not survive) transplantation typically show progressive developmental regression, hypotonia, and evolving nystagmus/opsoclonus; no formal long-term neurodevelopmental outcome scale data were identified for untransplanted survivors specifically (the untransplanted natural-history group has very high early mortality, limiting long-term functional-outcome data collection).

### Prognostic factors
- **Age of onset** is the single strongest prognostic determinant (neonatal/infantile far worse than adult).
- **Nystagmus at disease onset** specifically predicts worse post-liver-transplant survival (p=0.0275) — a clinically actionable prognostic/selection marker.
- Truncating variant type trends toward association with the severe neonatal/infantile hepatocerebral phenotype and higher mortality (literature-review-level association, not a formally validated predictive model).
- No validated prognostic biomarker beyond the above clinical/genotype features was identified.

---

## 12. Treatment

### Liver transplantation (the major disease-modifying intervention available)
- **Historically controversial** given uncertainty about pre-existing or evolving CNS involvement, but the 2024 pooled analysis provides the first large-scale outcome data:
  - 26 transplanted patients (14 hepatocerebral, 9 isolated hepatopathy, 3 hepatomyoencephalopathy).
  - **Median post-transplant survival 1.92 years** (range 1 month–26 years) vs. **0.5 years untreated** (range 1.4–6 months) — p<0.0001, i.e., liver transplantation confers a statistically significant survival benefit at the population level even though outcomes remain heterogeneous.
  - Post-transplant neurological course: 6 patients developed additional mild neurological signs after transplant; 1 patient showed neurological improvement; most others were stable.
  - Post-transplant deaths (n=13) were most often due to pulmonary hypertension (30.8%) and direct transplant complications (15.4%) rather than recurrence of the underlying metabolic disease in the graft (liver-specific), consistent with DGUOK-MDDS3 being fundamentally a systemic mtDNA-maintenance disorder for which liver replacement addresses the hepatic component only.
  - Nystagmus at disease onset predicts worse post-transplant survival (p=0.0275) — supporting careful pre-transplant neurological assessment/selection, an emerging practical consensus echoed in several dedicated case reports/series (e.g., "Favorable Outcome after Liver Transplantation in an Infant with Liver Failure Due to Deoxyguanosine Kinase Deficiency," PMC11432294; "Considerations for liver transplantation in deoxyguanosine kinase deficiency," PMID:38149456; a living-donor pediatric series, PMID:32320107).
  - The literature explicitly frames this as an evolving, patient-selection-dependent decision rather than a uniformly indicated or contraindicated procedure — "outcomes posttransplantation are historically worse than average and the role of liver transplantation remains controversial," while the more recent pooled data support a more favorable framing for carefully selected patients with absent/mild neurologic involvement.
- Suggested NCIT term: `NCIT:C15289` (Organ Transplantation); a more specific liver-transplant term should be verified against the local NCIT cache before binding.

### Pharmacotherapy / supportive care
- **Nutritional/metabolic support:** uncooked cornstarch to reduce hypoglycemia (reported for DGUOK- and MPV17-related hepatocerebral MDDS); general management is "directed mainly toward providing symptomatic management" (nutritional support, cofactor supplementation) rather than a curative pharmacologic regimen.
- **Mitochondrial cofactor/antioxidant "cocktail"** therapies used empirically across mitochondrial disease broadly (coenzyme Q10, riboflavin, thiamine, dichloroacetate, creatine, vitamin C/E, lipoic acid, cysteine donors such as N-acetylcysteine) — general supportive strategies for mitochondrial disease rather than DGUOK-specific approved therapies; note the mechanistic in-vitro finding that **N-acetylcysteine rescues ferroptosis sensitivity** in DGUOK-mutant iPSC-hepatocyte models (PMID:34026460) provides at least preclinical rationale for NAC specifically in this disorder, though clinical efficacy in patients is not established.

### Experimental / investigational therapies (not yet clinically approved for DGUOK deficiency)
- **Deoxynucleoside bypass therapy:** In fibroblast models (including DGUOK-mutant lines), supplementation with all four deoxynucleosides "increased the rate of recovery... and rescued mtDNA recovery in TWNK and DGUOK cells" (PMC11043827, 2024). This class of therapy is already an FDA-approved product for TK2 deficiency (a different, myopathic MDDS) but remains investigational, not approved, for DGUOK deficiency specifically.
- **Zebrafish (dguok−/−) model:** nucleoside supplementation modulates mtDNA copy number — purine nucleoside (deoxyguanosine) supplementation alone paradoxically reduced mtDNA copy number in juveniles (nucleotide pool imbalance effect), while combined purine nucleoside supplementation increased liver mtDNA copy number in adult dguok−/− fish — illustrating that the therapeutic window/formulation is non-trivial and stage-dependent (PMID:30428046).
- **Nucleotide prodrug CERC-913:** improved mtDNA content in primary hepatocytes from a DGUOK-deficient rat model (Vanden Avond et al. 2021, *J Inherit Metab Dis*) — preclinical, rodent hepatocyte-level evidence only.
- **Gene therapy:** patent literature references gene-therapy approaches for mtDNA-depletion-syndrome-causing genes broadly (including DGUOK), and a 2024 bioRxiv preprint specifically describes gene therapy preventing hepatic mitochondrial dysfunction in a murine DGUOK model — early preclinical stage, not in human trials as of this report.

### Clinical trials
No DGUOK-deficiency-specific interventional trial (NCT identifier) was identified in this search pass; broader mitochondrial-disease trials (e.g., NCT00432744, Phase III CoQ10 in mitochondrial disease) are not disease-specific. A DGUOK-specific ClinicalTrials.gov search should be run directly (`just fetch-reference NCT...`) before curating any trial entry.

### Treatment strategy summary
There is currently **no approved disease-modifying pharmacotherapy** for DGUOK deficiency. Management is (1) intensive neonatal/infantile metabolic and hepatic supportive care, (2) careful, case-by-case consideration of liver transplantation with pre-transplant neurological assessment as a key selection criterion, and (3) an active preclinical pipeline (deoxynucleoside bypass therapy, nucleotide prodrugs, gene therapy) that has not yet reached approved clinical use for this specific gene.

---

## 13. Prevention

### Primary prevention
Not applicable in the population-health sense (monogenic AR disorder); the relevant "primary prevention" is genetic — carrier screening and reproductive genetic counseling in at-risk families/populations (notably Druze founder-variant carriers), preimplantation genetic testing, and prenatal diagnosis for known familial variants.

### Secondary prevention / early detection
- Early recognition of unexplained neonatal/infantile cholestasis or liver failure — even with normal or only mildly elevated lactate — as an indication for mitochondrial functional and molecular work-up is explicitly recommended in the literature ("mitochondrial functional analysis and genetic testing should be considered early in infants with unexplained cholestasis and liver failure, regardless of the lactate levels").
- No dedicated population newborn-screening assay exists for DGUOK deficiency; secondary NBS clues (elevated tyrosine/phenylalanine) are non-specific.

### Genetic counseling
Standard AR counseling: 25% recurrence risk per pregnancy for carrier parents; carrier testing for at-risk relatives once the familial variant(s) are known; prenatal/preimplantation genetic testing available when familial variants are identified.

### Public health / behavioral / prophylaxis
None applicable — no environmental or behavioral risk-factor modification is relevant to this purely genetic disorder.

---

## 14. Other Species / Natural Disease

No naturally occurring DGUOK-deficient disease has been reported in non-human species (companion animals, wildlife); all non-human data derive from **engineered/induced models** (see §15), not spontaneous veterinary disease. No OMIA entry or veterinary case series was identified in this search. The DGUOK ortholog is broadly conserved across vertebrates (mouse *Dguok*, MGI:1351602; zebrafish *dguok*; rat *Dguok*), consistent with the enzyme's fundamental role in mitochondrial dNTP supply, but no spontaneous natural disease phenotype in these species has been documented — all reported phenotypes are from targeted genetic knockout/knockdown.

---

## 15. Model Organisms

| Model | Type | Key findings |
|---|---|---|
| **Mouse (*Dguok*−/−)** | Genetic knockout | Severe mtDNA depletion in liver (<10% of wild-type), disrupted mitochondrial ultrastructure; weight loss, absent subcutaneous fat, oxidative stress, liver damage/regeneration signs, increased catabolic lipid metabolism. Progressive decline over first 8 weeks of life, then mtDNA level stabilizes at a low but survivable level for at least 5 months — suggested compensatory dNTP-synthesis pathway. Considered a good phenocopy of human hepatic disease (Human Molecular Genetics 2019, academic.oup.com/hmg). MGI:1351602. |
| **Mouse (F180S point mutant)** | Knock-in/point mutation | Associated with a **lean phenotype** rather than the severe null phenotype — illustrates hypomorphic-allele modeling and dose-dependence (*Int J Obes* 2023, PMC10023562). |
| **Zebrafish (*dguok*−/−, CRISPR/Cas9)** | Genetic knockout | Significantly reduced mtDNA levels vs. wild-type; used to test nucleoside-supplementation therapy — single purine nucleoside (dGuo) supplementation paradoxically reduced mtDNA copy number in juveniles (pool imbalance), while combined purine nucleoside supplementation increased adult liver mtDNA copy number, supporting stage/formulation-dependent therapeutic potential of nucleoside-salvage substrate enhancement (PMID:30428046; Human Molecular Genetics 2019). |
| **Rat (DGUOK-deficient)** | Genetic model | Primary hepatocytes used to test the nucleotide prodrug CERC-913, which improved mtDNA content — preclinical pharmacology model (Vanden Avond et al. 2021, *J Inherit Metab Dis*). |
| **Human iPSC-derived liver organoids/hepatocyte-like cells (patient-derived + CRISPR-corrected isogenic control)** | Cellular/organoid model | Demonstrated selective ferroptosis sensitization in DGUOK-mutant cells under iron overload, rescued by N-acetylcysteine; mechanistically linked to NCOA4-dependent ferritinophagy (Guo et al. 2021, *Adv Sci*, PMID:34026460). A strong translational model given human genetic background and isogenic correction. |
| **Cell culture (short-term DGUOK disruption in hepatocyte lines)** | Acute knockdown/knockout | Used in the 2025 mechanistic study to show that innate immune activation (interferon/HERV/ISG) and lipid accumulation precede overt mtDNA depletion and mitochondrial dysfunction — supports a distinct, earlier-acting mechanistic branch (bioRxiv preprint, 2025; not yet peer-reviewed). |

### Model recapitulation and limitations
- The mouse knockout most faithfully recapitulates the **hepatic** phenotype (severe mtDNA depletion, liver pathology, lipid/energy dysregulation) but the degree to which it recapitulates the **human neurologic phenotype** (nystagmus/opsoclonus, developmental regression) was not addressed in the sources reviewed — this represents a plausible **human-model mismatch** worth flagging explicitly in any curated entry (i.e., strong hepatic fidelity, unassessed/unclear CNS fidelity).
- The zebrafish model's paradoxical juvenile-stage response to single-nucleoside supplementation (mtDNA copy number *decrease*, not increase) is a notable translational caveat for interpreting nucleoside-bypass therapeutic rationale — a straightforward "more substrate is better" extrapolation from cell culture to whole organism does not hold uniformly.
- iPSC-organoid models capture ferroptosis susceptibility specifically and are of high genetic fidelity (patient-derived, isogenically corrected) but are necessarily a reductionist single-cell-type/organoid system without systemic (e.g., neurologic, immune) context.

---

## Summary of Key Ontology-Term Suggestions for Curation

| Category | Suggested terms |
|---|---|
| Gene | hgnc: (DGUOK symbol — verify exact HGNC ID via lookup before binding, not stated with certainty in sources reviewed) |
| MONDO | MONDO:0009636 |
| GO (molecular function) | GO:0004137 deoxyguanosine kinase activity |
| GO (biological process) | GO:0006264 mitochondrial DNA replication; GO:0009157 deoxyribonucleoside monophosphate biosynthetic process; GO:0097707 ferroptosis |
| GO (cellular component) | GO:0005739 mitochondrion; GO:0005759 mitochondrial matrix |
| CL | CL:0000182 hepatocyte; CL:0000187/CL:0000188 muscle cell; CL:0000540 neuron |
| UBERON | UBERON:0002107 liver; UBERON:0000955 brain; UBERON:0001134 skeletal muscle tissue |
| HP (phenotypes) | HP:0002240 Hepatomegaly; HP:0000952 Jaundice; HP:0001396 Cholestasis; HP:0001399 Hepatic failure; HP:0001290 Generalized hypotonia; HP:0000639 Nystagmus; HP:0001263 Global developmental delay; HP:0002376 Developmental regression; HP:0000508 Ptosis; HP:0000590 Progressive external ophthalmoplegia; HP:0001943 Hypoglycemia; HP:0003128 Lactic acidosis |
| CHEBI | CHEBI: deoxyguanosine, deoxyadenosine (verify exact CHEBI CURIEs before binding) |
| NCIT (treatment) | NCIT:C15289 Organ Transplantation (liver transplantation); NCIT:C15986 Pharmacotherapy (supportive/cofactor therapy) |

**Curation note:** All ontology CURIEs above are suggestions drawn from general domain knowledge of these ontologies' likely term coverage, not from a live OAK/runoak lookup performed in this research pass — per dismech's Ontology Term Contract, every CURIE must be independently verified against the actual ontology (`runoak`/`cache/<prefix>/terms.csv`) before being written into a KB entry; none should be copied from this report without that verification step.

---

## Sources

- [OMIM #251880 — MITOCHONDRIAL DNA DEPLETION SYNDROME 3 (HEPATOCEREBRAL TYPE); MTDPS3](https://omim.org/entry/251880)
- [OMIM *601465 — DEOXYGUANOSINE KINASE; DGUOK](https://omim.org/entry/601465)
- [Orphanet ORPHA:279934 — Mitochondrial DNA depletion syndrome, hepatocerebral form due to DGUOK deficiency](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=279934)
- [GeneReviews — Deoxyguanosine Kinase Deficiency (NBK7040)](https://www.ncbi.nlm.nih.gov/books/NBK7040/)
- [MedlinePlus Genetics — Deoxyguanosine kinase deficiency](https://medlineplus.gov/download/genetics/condition/deoxyguanosine-kinase-deficiency.pdf)
- [GARD — Mitochondrial DNA depletion syndrome 3 (hepatocerebral type)](https://rarediseases.info.nih.gov/diseases/13644/mitochondrial-dna-depletion-syndrome-3-hepatocerebral-type)
- Deoxyguanosine kinase deficiency: natural history and liver transplant outcome, *Brain Communications* 2024 — [PMC11098040](https://pmc.ncbi.nlm.nih.gov/articles/PMC11098040/) / [PubMed 38756539](https://pubmed.ncbi.nlm.nih.gov/38756539/)
- The clinical variations and diagnostic challenges of deoxyguanosine kinase deficiency: a descriptive case series — [PubMed 34167177](https://pubmed.ncbi.nlm.nih.gov/34167177/)
- Mandel et al., The deoxyguanosine kinase gene is mutated in individuals with depleted hepatocerebral mitochondrial DNA — [PubMed 11687800](https://pubmed.ncbi.nlm.nih.gov/11687800/)
- Taanman et al., A novel mutation in the deoxyguanosine kinase gene causing depletion of mitochondrial DNA — [PubMed 12210798](https://pubmed.ncbi.nlm.nih.gov/12210798/)
- Guo et al., A Combined Model of Human iPSC-Derived Liver Organoids and Hepatocytes Reveals Ferroptosis in DGUOK Mutant mtDNA Depletion Syndrome, *Advanced Science* 2021 — [PMC8132052](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8132052/) / [PubMed 34026460](https://pubmed.ncbi.nlm.nih.gov/34026460/)
- Deoxyguanosine Kinase Deficiency Couples Purine Metabolism to Innate Immune Activation and Lipid Accumulation in Hepatocytes (bioRxiv preprint, 2025) — [PMC13416635](https://pmc.ncbi.nlm.nih.gov/articles/PMC13416635/) / [bioRxiv PDF](https://www.biorxiv.org/content/10.1101/2025.11.18.688341.full.pdf)
- Severe mtDNA depletion and dependency on catabolic lipid metabolism in DGUOK knockout mice, *Human Molecular Genetics* 2019 — [academic.oup.com/hmg](https://academic.oup.com/hmg/article/28/17/2874/5498697?login=false)
- Deoxyguanosine kinase mutation F180S is associated with a lean phenotype in mice, *Int J Obesity* 2023 — [PMC10023562](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10023562/)
- Nucleoside supplementation modulates mitochondrial DNA copy number in the dguok−/− zebrafish, *Human Molecular Genetics* 2019 — [PMC6381312](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6381312/) / [PubMed 30428046](https://pubmed.ncbi.nlm.nih.gov/30428046/)
- Vanden Avond et al., The nucleotide prodrug CERC-913 improves mtDNA content in primary hepatocytes from DGUOK-deficient rats, *J Inherit Metab Dis* 2021 — [Wiley](https://onlinelibrary.wiley.com/doi/10.1002/jimd.12354)
- Nucleoside supplements as treatments for mitochondrial DNA depletion syndrome — [PMC11043827](https://pmc.ncbi.nlm.nih.gov/articles/PMC11043827/) / [PubMed 38665433](https://pubmed.ncbi.nlm.nih.gov/38665433/)
- Case report: Two unexpected cases of DGUOK-related mitochondrial DNA depletion syndrome presenting with hyperinsulinemic hypoglycemia — [PMC10646319](https://pmc.ncbi.nlm.nih.gov/articles/PMC10646319/)
- DGUOK-related mitochondrial DNA depletion syndrome presenting with neonatal cholestasis without marked hyperlactatemia: A diagnostic pitfall — [PMC13141804](https://pmc.ncbi.nlm.nih.gov/articles/PMC13141804/)
- Considerations for liver transplantation in deoxyguanosine kinase deficiency: A case series and review of the literature — [PubMed 38149456](https://pubmed.ncbi.nlm.nih.gov/38149456/)
- Favorable Outcome after Liver Transplantation in an Infant with Liver Failure Due to Deoxyguanosine Kinase Deficiency — [PMC11432294](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11432294/)
- Pediatric liver transplantation from a living donor in mitochondrial disease: Good outcomes in DGUOK deficiency? — [PubMed 32320107](https://pubmed.ncbi.nlm.nih.gov/32320107/)
- Acute liver failure due to DGUOK deficiency–is liver transplantation justified? — [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S2210740120300826)
- Detection of uniparental isodisomy in autosomal recessive mitochondrial DNA depletion syndrome by high-density SNP array analysis — [PMC7512120](https://pmc.ncbi.nlm.nih.gov/articles/PMC7512120/)
- CPEO and Mitochondrial Myopathy in a Patient with DGUOK Compound Heterozygous Pathogenetic Variant and mtDNA Multiple Deletions — [PMC6431376](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6431376/)
- Resources for Genetics Professionals — Genetic Disorders Associated with Founder Variants Common in the Druze Population — [NBK549466](https://www.ncbi.nlm.nih.gov/books/NBK549466/)
- MGI Mouse Gene Detail — Dguok — [MGI:1351602](https://www.informatics.jax.org/marker/MGI:1351602)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 23 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 22 |
| On topic | 17 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `PMID:34167177` (3 mentions) - Identifier did not resolve to a record

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMC:PMC11043827` *(abstract only)*: "increased the rate of recovery... and rescued mtDNA recovery in TWNK and DGUOK cells"
  - closest text in source: "ATGC nucleoside combination significantly increased the rate of mtDNA recovery in quiescent POLG1 cells following mtDNA depletion by ddC"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 40 |
| Resolved | 38 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 28 |
| Terms named correctly | 19 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0009636` (2 mentions) - the report calls it "MONDO"; MONDO calls it **mitochondrial DNA depletion syndrome 3 (hepatocerebral type)**
- `HP:0031982` (1 mention) - the report calls it "Opsoclonus"; HP calls it **Abnormal putamen morphology**
- `HP:0009053` (1 mention) - the report calls it "limb-specific if documented"; HP calls it **Distal lower limb muscle weakness**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001744` (1 mention) - the report calls it "Splenomegaly if present"; HP calls it **Splenomegaly**
- `GO:0004137` (2 mentions) - the report calls it "deoxyguanosine kinase activity"; GO calls it **deoxycytidine kinase activity**
- `GO:0005739` (3 mentions) - the report calls it "Subcellular: mitochondrion", "Mitochondria"; GO calls it **mitochondrion**
- `UBERON:0002107` (2 mentions) - the report calls it "Primary:** Liver"; UBERON calls it **liver**
- `UBERON:0000955` (2 mentions) - the report calls it "Secondary/CNS:** Brain"; UBERON calls it **brain**, and lists "the brain" among its other names
- `UBERON:0001134` (2 mentions) - the report calls it "Secondary/muscle:** Skeletal muscle"; UBERON calls it **skeletal muscle tissue**, and lists "skeletal muscle" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000182` - called "Hepatocyte", "Hepatocytes"
- `GO:0005739` - called "Subcellular: mitochondrion", "Mitochondria"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.