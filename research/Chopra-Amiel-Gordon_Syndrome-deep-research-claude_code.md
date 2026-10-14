---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-23T19:53:02.310539'
end_time: '2026-09-23T19:57:31.984237'
duration_seconds: 269.67
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Chopra-Amiel-Gordon Syndrome
  mondo_id: MONDO:0859186
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
  num_turns: 28
  total_cost_usd: 1.5690132
  session_id: fd65d8eb-852b-5a9d-91de-140beff025e2
  stop_reason: end_turn
  assistant_text_blocks: 7
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
citation_count: 15
reference_validation:
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 7
  on_topic: 6
  validator_version: 0.2.1
term_validation:
  total_terms: 66
  verified: 63
  not_found: 0
  obsolete: 2
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 39
  labels_matching: 25
  labels_mismatched: 6
  mislabelled_terms:
  - term_id: MONDO:0859186
    reported_labels:
    - matches the target ID given
    ontology_label: Chopra-Amiel-Gordon syndrome
  - term_id: HP:0004325
    reported_labels:
    - Postnatal growth failure
    ontology_label: Decreased body weight
  - term_id: GO:0032495
    reported_labels:
    - NOD1/NOD2 response
    ontology_label: response to muramyl dipeptide
  - term_id: CL:0002608
    reported_labels:
    - Cell types implicated:** radial glial progenitors
    - radial glial cell
    ontology_label: hippocampal neuron
  - term_id: UBERON:0002037
    reported_labels:
    - cerebellum, relevant to the cerebellar hypoplasia noted in the 2025 fetal case
    - cerebellum
    ontology_label: cerebellum
  - term_id: UBERON:0002316
    reported_labels:
    - prefrontal cortex region approximation
    ontology_label: white matter
  labels_variant: 8
  obsolete_terms:
  - term_id: GO:0039528
    ontology_label: GO_0039528
    replaced_by: GO:0002753
  - term_id: CL:0008030
    ontology_label: obsolete excitatory neuron
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Chopra-Amiel-Gordon Syndrome
- **MONDO ID:** MONDO:0859186 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Chopra-Amiel-Gordon Syndrome** covering all of the
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

I'll research Chopra-Amiel-Gordon Syndrome using web search tools to ensure accuracy, since this is a rare, recently-described syndrome.

Good, MONDO:0859186 confirmed matches the target. Let me now fetch primary sources for detailed data — the landmark AJHG paper, OMIM, GeneReviews (if any), ClinGen, and the 2025 genotype-phenotype update.

There's a GeneReviews chapter — that's excellent, it's the most authoritative source. Let me fetch it plus the 2025 novel-variants paper and the original AJHG paper abstract via alternate access.

Let me get the GeneReviews content via a different approach and pull the Wikipedia summary plus the founding AJHG paper's abstract, and the 2025 genotype-phenotype update abstract.

Good data accumulating. Let me get more detail on GeneReviews specifics (diagnosis, management, differential diagnosis), the 2025 genotype-phenotype conference abstract, the case report with the Chinese patient, ANKRD17 gene function/mechanism, and animal model details.

Good, comprehensive data is coming together. Let me now get information on GeneReviews management/surveillance and differential diagnosis, and check for HPO terms, plus mouse model original paper (embryonic lethality/cardiovascular).

I have sufficient primary and secondary source material now. Compiling the comprehensive report.

# Chopra-Amiel-Gordon Syndrome (ANKRD17-Related Neurodevelopmental Syndrome): Comprehensive Research Report

## 1. Disease Information

**Overview.** Chopra-Amiel-Gordon syndrome (CAGS) — the preferred nosological name is now **ANKRD17-related neurodevelopmental syndrome** — is an autosomal dominant, ultra-rare Mendelian neurodevelopmental disorder caused by heterozygous loss-of-function variants in *ANKRD17* (Ankyrin Repeat Domain 17). It was first delineated as a distinct clinical entity in 2021 by Chopra, McEntagart, Clayton-Smith, Gordon, and colleagues in the *American Journal of Human Genetics* (PMID: 33909992), based on 34 individuals from 32 families identified through GeneMatcher-style international collaboration and exome/genome sequencing. The syndrome is characterized by global developmental delay/intellectual disability with disproportionate speech impairment, variable facial dysmorphism, and a range of associated neurological, ophthalmological, growth, and immune features.

**Key identifiers:**
- **OMIM (phenotype):** 619504 — CHOPRA-AMIEL-GORDON SYNDROME; CAGS
- **OMIM (gene):** *615929 — ANKYRIN REPEAT DOMAIN-CONTAINING PROTEIN 17; ANKRD17
- **MONDO:** MONDO:0859186 (matches the target ID given)
- **MedGen:** C5561975 / UID 1794185
- **Orphanet:** an ORPHA entry exists for this disorder (search aggregators return ORPHA:717823, but I was unable to directly verify this number against the live Orphanet page during this session — a redirect blocked automated fetch — so treat this specific ORPHA code as a **lead requiring direct confirmation**, not a verified citation)
- **Gene location:** 4q13.3 (chromosome 4)
- **Reference transcript:** NM_032217.5 (also cited as NM_001286771.3 in some reports)
- **GeneReviews chapter:** "ANKRD17-Related Neurodevelopmental Syndrome," NCBI Bookshelf NBK588029 (initial posting December 2022)

**Synonyms:** ANKRD17-related neurodevelopmental syndrome (current preferred term); CAGS; Chopra–Amiel–Gordon syndrome.

**Evidence basis:** This is a **structured, aggregated cohort disease** — nearly all published knowledge derives from multi-institutional case-series/cohort studies (the founding 2021 AJHG cohort of 34/32 families; a 2025 follow-up cohort reported to include up to 47–55 individuals for genotype-phenotype and epilepsy-specific analyses) plus individual case reports, rather than large-scale registry or EHR-derived data. A dedicated natural history study is actively recruiting (ClinicalTrials.gov NCT05528744, Boston Children's Hospital, "CAGS NHS," started 2022-08-27, estimated completion 2030), which will generate prospective, individual-patient-level clinical, imaging, and iPSC/neuronal-phenotyping data going forward.

---

## 2. Etiology

**Disease causal factor — genetic.** CAGS is caused by heterozygous **loss-of-function (LOF)** variants in *ANKRD17*, occurring predominantly *de novo*. The founding cohort's mutational spectrum (PMID: 33909992):
- 21 truncating/essential splice-site variants (7 nonsense, 12 frameshift, 2 splice-site)
- 9 missense variants affecting highly conserved ankyrin-repeat residues
- 1 in-frame indel
- 1 de novo 1.16 Mb microdeletion at 4q13.3

A subsequent case (Xia et al., 2025, PMID: 40604385) added a 1.247 Mb microdeletion (exons 2–34) and a nonsense variant c.1252C>T (p.Arg418*). A Chinese cohort report (Frontiers in Genetics, 2024, DOI: 10.3389/fgene.2024.1422469) added a canonical splice variant c.7248+1G>A causing exon 32 skipping.

**Genetic risk factors.** No modifier genes have been established. *ANKRD17* is extremely intolerant of loss-of-function variation in the general population (**gnomAD pLI = 1.0**), which is cited by the original authors as strong supportive evidence for haploinsufficiency as the disease mechanism, independent of the clinical cohort data itself.

**Environmental/other risk factors.** None reported; this is a purely monogenic disorder with essentially complete de novo origin (see §9 for the one reported familial transmission and monozygotic twin pair).

**Protective factors.** None identified or plausible for a haploinsufficiency Mendelian disorder of this kind; not addressed in the literature.

**Gene-environment interactions.** Not studied/applicable — no published data.

---

## 3. Phenotypes

The two largest cohorts (the 2021 founding study, n=34, and a 2025 follow-up genotype-phenotype study presented as a conference abstract, apparently n≈47, plus a separate epilepsy-focused analysis of n=55) give the most reliable frequency estimates. Figures below combine both, cited separately where sourced differently.

### Neurodevelopmental (most penetrant domain)
- **Developmental delay / intellectual disability:** 31/34 (91%) in the founding cohort; in the 2025 update, 40/47 (85%), with severity distribution reported as ~25% borderline, ~65% mild-moderate, ~10% severe-profound. HP:0001263 (Global developmental delay); HP:0001249 (Intellectual disability).
- **Speech/expressive language delay or apraxia:** the single most penetrant feature — 29/32 (91%) in the founding cohort; 42/47 (91%) in the 2025 update, including some individuals with absent speech. HP:0000750 (Delayed speech and language development); consider HP:0011922 for speech apraxia if documented.
- **Motor delay:** 20/29 (69%). HP:0001270 (Motor delay).
- **Autism spectrum disorder / ASD features:** reported as a recurrent feature. HP:0000717.
- **ADHD:** reported. HP:0007018.
- **Gait/balance disturbance:** emerging feature in later cohorts (2025 update names "gait difficulties" as a newly recognized manifestation). HP:0001288 (Gait disturbance).
- **Epilepsy:** 9/33 (27%) in the founding cohort; a dedicated epilepsy-phenotype analysis (AESnet abstract) in a larger cohort of 55 found **24/55 (43%)** with confirmed epilepsy — absence seizures most common (13/24), then generalized tonic-clonic (11/24), then epileptic spasms (5/24); 7 patients had multiple seizure types. Mean age at onset 4.4 years (range neonatal–15 years). EEG: ictal abnormalities in 9, interictal in 7. Treatment response generally favorable — 10/24 achieved seizure control on monotherapy, 13/24 (54%) had seizures less than annually, though 5/24 met drug-resistant criteria; overall the authors characterize epilepsy in CAGS as "relatively benign and generally controlled with medication." HP:0001250 (Seizure); HP:0002121 (Generalized absence seizure); HP:0002069 (Generalized tonic-clonic seizure); HP:0011097 (Epileptic spasm).

### Craniofacial dysmorphism
- Triangular face shape: 10/24 (~42%). HP:0000325.
- High anterior hairline: 19/24 (~79%). HP:0009890.
- Almond-shaped/deep-set eyes with periorbital fullness: 8/24. HP:0007655 / HP:0000601 (deep-set eyes) — descriptor may need custom mapping.
- Thin upper lip vermilion: 12/24 (50%). HP:0000219.
- Full cheeks: reported. HP:0000293.
- Thick nasal alae / flared nostrils: reported. HP:0009928 or HP:0000463 (anteverted nares).
- Low-set ears: reported. HP:0000369.
- Less common: cleft palate with Pierre Robin sequence (HP:0000201 / HP:0000278 for micrognathia component), cleft lip (HP:0410030/HP:0100333), scoliosis (HP:0002650), renal agenesis (HP:0000104, unilateral form HP:0000122).

### Ophthalmological
- Strabismus and refractive errors: 13/23 (57%) had ophthalmological abnormalities in the founding cohort. HP:0000486 (Strabismus); HP:0000539 (Abnormality of refraction).

### Growth
- Growth failure/short stature (height <−2SD): 12/31 (39%). HP:0004325 (Postnatal growth failure) / HP:0003510 (Short stature).
- Feeding difficulties: recurrent feature across cohorts, including selective food aversion in the Chinese case report. HP:0011968.
- **Overweight/obesity** — emerging feature noted in the 2025 genotype-phenotype update. HP:0001513.

### Musculoskeletal
- Joint hypermobility: 9/29 (31%). HP:0001382.
- **Dysphagia** — emerging feature (2025 update). HP:0002015.

### Immune
- Recurrent (bacterial) infections: 11/33 (33%); recurrent pulmonary infections specifically reported in individual cases. HP:0002719 (Recurrent infections).

### Rare/emerging (2025 update; not yet quantified with confidence)
- Cerebral hemorrhage — reported as a rare, newly emerging feature.
- Tic disorder / involuntary vocalization and blinking — proposed as a possible phenotypic expansion in one case report (not yet an established core feature; treat as a single-case lead, not a cohort-confirmed association).
- Urinary frequency, self-resolving — single case.

**Quality of life impact.** No dedicated QOL instrument (EQ-5D, SF-36, PROMIS) study has been published for CAGS specifically; the natural history study (NCT05528744) plans standardized neurobehavioral assessment but QOL-specific outcome data are **not yet available** in the literature.

**Severity/progression pattern:** Severity is broadly stable/non-progressive for the core neurodevelopmental phenotype (a static encephalopathy-type course), consistent with a haploinsufficiency developmental gene; epilepsy, when present, tends to be non-progressive and often well controlled. No natural history data yet describe regression.

---

## 4. Genetic/Molecular Information

- **Causal gene:** ANKRD17 (HGNC symbol ANKRD17; OMIM *615929), encoding Ankyrin Repeat Domain-Containing Protein 17, a large multi-ankyrin-repeat scaffold protein with nuclear localization/export signals, localizing to nucleus, cytoplasm, and membrane compartments (per GeneCards).
- **Variant classification/type:** Predominantly pathogenic/likely-pathogenic per ACMG/AMP criteria in ClinVar (e.g., RCV001593058 c.2623G>T p.Glu875Ter; RCV001843437 c.833G>T p.Gly278Val). Types: nonsense, frameshift, canonical splice-site, missense (clustering in conserved ankyrin-repeat core residues, "invariant in all 25 repeats"), in-frame indel, and multi-exon/whole-gene microdeletions (1.16–1.25 Mb at 4q13.3).
- **Variant origin:** Overwhelmingly *de novo*/germline; essentially no somatic CAGS reports exist (this is a developmental, not neoplastic, disorder).
- **Allele frequency in population databases:** Not applicable for pathogenic variants (private/de novo); the relevant population-genetics statistic is **gnomAD pLI = 1.0**, i.e., near-complete intolerance to predicted LOF variation in the general population — this constraint metric is itself cited as supporting evidence for a haploinsufficiency mechanism, independent of the clinical cohort.
- **Functional consequence:** **Loss of function / haploinsufficiency** is the proposed and best-supported mechanism (per the founding AJHG paper and ClinGen Dosage Sensitivity curation, which lists ANKRD17 with sufficient evidence for haploinsufficiency, consistent with the truncating-variant-dominant mutational spectrum). Missense variants are proposed to act via structural destabilization of the ankyrin-repeat fold (disrupting core structural residues invariant across all 25 repeats) rather than via a distinct dominant-negative or gain-of-function route, though a dominant-negative contribution for some missense alleles cannot be formally excluded and has not been functionally tested.
- **Modifier genes:** None established.
- **Epigenetic information:** No CAGS-specific DNA methylation/histone data published to date (unlike some other neurodevelopmental disorders, no "episignature" has yet been reported for ANKRD17).
- **Chromosomal abnormalities:** Two microdeletions at 4q13.3 reported (encompassing ANKRD17, 1.16 Mb and 1.247 Mb), functionally equivalent to gene-level haploinsufficiency.
- **Cell-cycle interaction:** ANKRD17 interacts with the **cyclin E/CDK2 complex** and promotes cell-cycle progression — proposed relevance to neural progenitor proliferation, supported by single-cell RNA-seq co-expression of ANKRD17 and CDK2 in human telencephalic neuronal progenitors (from the founding paper's reanalysis of published scRNA-seq data, not new functional data).
- **Innate immunity interaction:** ANKRD17 has been separately characterized (outside the CAGS-specific literature, in general molecular biology studies) as a positive regulator of innate immune signaling — enhancing antiviral responses via DDX58 (RIG-I)/IFIH1 (MDA5) pathways and antibacterial defense via NOD1/NOD2 signaling — proposed by the CAGS authors as a plausible explanation for the recurrent-infection phenotype, though this link is inferential/extrapolated rather than demonstrated in patient samples.

---

## 5. Environmental Information

No environmental, lifestyle, or infectious contributory factors have been identified or are biologically plausible for this monogenic developmental disorder; the literature contains no such claims. This section is not applicable beyond noting that recurrent infections are a **phenotypic manifestation** of the immune dysregulation hypothesis above, not an environmental *cause* of the syndrome.

---

## 6. Mechanism / Pathophysiology

### Proposed causal chain (largely inferential; direct patient-derived functional data are still forthcoming from NCT05528744's iPSC program)

1. A heterozygous truncating, splice-disrupting, or structurally destabilizing missense variant in *ANKRD17* (or a 4q13.3 microdeletion spanning the gene) **leads to** reduced/absent functional ANKRD17 protein from one allele.
2. Because the population is highly intolerant of ANKRD17 LOF (pLI=1.0), this **results in** insufficient total ANKRD17 dosage (**haploinsufficiency**) rather than a compensable loss — the proposed primary disease mechanism.
3. In neural progenitor cells, reduced ANKRD17 dosage **is inferred to disrupt** its interaction with the cyclin E/CDK2 complex, potentially **impairing** normal cell-cycle progression of radial glial progenitors and excitatory/inhibitory neuron populations that co-express ANKRD17 during human telencephalic development (inference from scRNA-seq co-expression, not direct functional proof).
4. In parallel, via the conserved Mask/ANKRD17–Yorkie/YAP axis of the Hippo signaling pathway (demonstrated in the *Drosophila* ortholog *Mask*, not yet functionally confirmed in human/mammalian ANKRD17-deficient neural tissue), reduced ANKRD17 **is proposed to dysregulate** YAP1-dependent tissue-growth signaling, which **may contribute to** the growth-failure and dysmorphic craniofacial phenotype (this step is explicitly flagged by the original authors as "yet to be understood").
5. Downstream of steps 3–4, disrupted progenitor proliferation and neurodevelopmental gene-expression programs **lead to** the core clinical phenotype: global developmental delay, disproportionate speech/language impairment, and variable structural brain findings.
6. Independently, a 2025 mouse AAV-knockdown study (Xia et al., PMID: 40604385) demonstrates that ANKRD17 knockdown in medial prefrontal cortex and hippocampal CA1 **causes** decreased expression of the NMDAR subunit GluN2A, the AMPAR subunit GluA1, the excitatory synaptic scaffold protein PSD-95, and Synapsin I — i.e., a **synaptic protein deficit** — which **results in** measurable social, anxiety, and spatial-memory/learning deficits in mice, directly modeling the ASD/anxiety/cognitive component of the human phenotype.
7. The same mouse/human-embryonic-brain-proteomics study found that 21.1% of differentially expressed proteins after ANKRD17 knockdown localize to mitochondria, with significant downregulation of mitochondrial matrix, respiratory chain complex II, and electron-transfer-activity pathways (confirmed by qPCR for *Sdha/Sdhb/Sdhc*) — indicating a **mitochondrial dysfunction** branch of the mechanism, potentially contributing to neuronal energetic failure and compounding the synaptic deficit.
8. Separately, at the whole-organism level, complete *Ankrd17* ablation in mice **causes embryonic lethality at E10.5–E11.5 due to cardiovascular defects** (hemorrhage, vascular smooth muscle cell deficiency, PMID from Hou et al. 2009 FEBS Letters), establishing that ANKRD17 is essential for vascular integrity during embryogenesis — this defines the biological floor of complete loss (relevant to why CAGS patients, who retain one functional allele, survive, whereas biallelic loss would likely be embryonic lethal) and is consistent with renal agenesis and other structural anomalies occasionally observed in the human syndrome as partial phenocopies of this vascular/developmental role.
9. Finally, ANKRD17's separately characterized role as a positive regulator of NOD1/NOD2-mediated antibacterial signaling and DDX58/IFIH1-mediated antiviral signaling **is proposed to explain** (though not directly demonstrated in patients) the recurrent bacterial/viral infection phenotype observed in roughly a third of the cohort.

### Summary by category
- **Molecular pathways:** Hippo/Yorkie–YAP1 (via *Drosophila* Mask ortholog homology — GO:0035329, hippo signaling); cyclin E/CDK2 cell-cycle pathway (GO:0000082, G1/S transition of mitotic cell cycle); NOD1/NOD2 innate immune signaling (GO:0032495); RIG-I/MDA5 (DDX58/IFIH1) antiviral signaling (GO:0039528).
- **Cellular processes:** neural progenitor proliferation (GO:0022008, neurogenesis); synaptic protein complex assembly/maintenance (GO:0007416, synapse assembly); mitochondrial respiratory chain function (GO:0022904, respiratory electron transport chain).
- **Protein dysfunction:** loss/destabilization of the ankyrin-repeat scaffold structure; the encoded protein is not enzymatic itself but a scaffold/co-factor, so functional consequence is loss of protein-protein interaction capacity rather than catalytic loss.
- **Cell types implicated:** radial glial progenitors (CL:0002608), excitatory neurons (CL:0008030 or more specific cortical excitatory neuron terms), interneurons (CL:0000099), hippocampal CA1 pyramidal neurons, and vascular smooth muscle cells (CL:0000359) in the mouse embryonic-lethality model.
- **Tissue damage mechanisms:** vascular hemorrhage/maturation failure (embryonic mouse model only — not documented as an ongoing pathology in surviving human heterozygotes beyond the rare "cerebral hemorrhage" case noted in the 2025 update).
- **Metabolic changes:** mitochondrial/oxidative-phosphorylation gene downregulation (complex II components).
- **Molecular profiling:** proteomics (5D label-free) on postmortem human embryonic brain tissue and mouse cortex/hippocampus after knockdown (Xia et al. 2025); single-cell RNA-seq reanalysis of published human telencephalon datasets (Chopra et al. 2021) — no CAGS patient-derived transcriptomic/proteomic dataset has yet been deposited in GEO/PRIDE as a dedicated disease-cohort resource; the closest is the ongoing iPSC program under NCT05528744.
- **Advanced technologies:** no single-cell, spatial transcriptomic, or CRISPR functional-genomics screen has been performed specifically on ANKRD17/CAGS patient material to date; the AAV-knockdown mouse model (Xia et al. 2025) is the most advanced functional perturbation model currently published.

---

## 7. Anatomical Structures Affected

- **Organ level (primary):** Central nervous system (brain — nonspecific structural abnormalities reported on MRI, not yet systematically characterized; a dedicated imaging arm is part of NCT05528744); craniofacial skeleton/soft tissue.
- **Secondary/associated:** Eyes (strabismus, refractive error); ears (low-set position); kidneys (rare renal agenesis); skeletal system (scoliosis, joint hypermobility); immune system (recurrent infection susceptibility); cardiovascular system (implicated in the mouse null model but not established as an ongoing human phenotype); growth/endocrine axis (short stature, feeding difficulty, and — per the 2025 update — obesity/overweight).
- **Body systems:** Nervous system, craniofacial/skeletal system, ophthalmological system, immune system, growth/endocrine system, and (in the null-mouse model only) cardiovascular system.
- **Tissue/cell level:** cortical excitatory and inhibitory neurons, radial glial neural progenitors, hippocampal CA1 neurons, medial prefrontal cortex neurons (mouse knockdown model), vascular smooth muscle (mouse null model).
- **Subcellular level:** synapse (postsynaptic density — PSD-95/GluN2A/GluA1 reduction); mitochondria (respiratory chain complex II downregulation); nucleus/cytoplasm/membrane (ANKRD17's own subcellular localization per GeneCards/UniProt).
- **Suggested ontology terms:** UBERON:0000955 (brain); UBERON:0002037 (cerebellum, relevant to the cerebellar hypoplasia noted in the 2025 fetal case); UBERON:0001954 (Ammon's horn/CA1); UBERON:0002316 (prefrontal cortex region approximation); CL:0002608 (radial glial cell); CL:0000359 (vascular smooth muscle cell); GO:0005739 (mitochondrion, cellular component); GO:0045211 (postsynaptic membrane).
- **Lateralization:** Not applicable/no pattern reported — this is a systemic developmental disorder without lateralized organ involvement.

---

## 8. Temporal Development

- **Onset:** Prenatal/congenital in the broadest sense (germline de novo mutation present from conception), but clinically **apparent from infancy/early childhood** as developmental delay becomes evident; one severe prenatal-onset case (fetus with multiple congenital anomalies including cerebellar hypoplasia and growth retardation) has been reported (Xia et al. 2025), indicating the phenotypic range extends to prenatally lethal/severe presentations.
- **Onset pattern:** Insidious/developmental rather than acute — a static developmental encephalopathy pattern is most consistent with the described natural history, though epilepsy onset can occur any time from the neonatal period to age 15 (mean 4.4 years).
- **Progression:** No evidence of a degenerative/progressive course for the core neurodevelopmental phenotype; described features are stable developmental differences rather than regression. Epilepsy, when present, is generally non-progressive and often becomes well controlled with monotherapy over time.
- **Disease course pattern:** Chronic, lifelong, non-remitting developmental disability of variable severity (borderline to severe-profound); epilepsy course is described as "relatively benign."
- **Critical periods:** Neurodevelopmental vulnerability is inferred to center on early corticogenesis (based on ANKRD17/CDK2/YAP1 co-expression in radial glial progenitors during human telencephalic development), but no clinical intervention-timing data yet exist.
- **Age range reported in the literature:** founding cohort spanned 4 months to 34 years, indicating the phenotype is recognizable and has been documented from infancy through adulthood.

---

## 9. Inheritance and Population

- **Epidemiology:** CAGS is an **ultra-rare disorder**; fewer than 40 individuals were reported in the literature by 2023, with more recent aggregate cohorts (2025 conference presentations) citing up to ~47–55 characterized individuals and lay/registry sources suggesting >100 total diagnoses worldwide by 2025 as awareness and diagnostic sequencing access have increased. No formal population-based prevalence or incidence estimate (cases per 100,000) has been published; this is consistent with a condition still being ascertained primarily through clinical exome/genome sequencing in developmental-delay cohorts rather than through population screening.
- **Inheritance pattern:** Autosomal dominant (AD).
- **De novo rate:** The overwhelming majority of cases are de novo. The founding cohort documented one **familial transmission** (an affected mother and her affected son) and one pair of **monozygotic female twins**, demonstrating that germline/gonadal transmission and full penetrance in an identical genetic background are both possible, though rare in the reported cohort.
- **Penetrance:** Appears to be high/complete for the core developmental-delay/speech phenotype based on reported cases (no confirmed non-penetrant carriers have been described in the literature to date, though ascertainment bias toward symptomatic probands limits this conclusion).
- **Expressivity:** Markedly variable — severity ranges from borderline/mild intellectual disability to severe-profound disability, and dysmorphic/systemic features (epilepsy, infections, growth, ophthalmological, skeletal) are present in only a subset of cases, indicating substantial variable expressivity even among carriers of similar (truncating) variant types.
- **Genetic anticipation:** Not applicable/not reported — this is not a repeat-expansion disorder.
- **Germline mosaicism:** GeneReviews explicitly notes that if the proband's variant is not found in either parent's blood, sibling recurrence risk remains slightly elevated above general population risk due to the possibility of parental germline mosaicism — standard AD de novo genetic-counseling guidance.
- **Founder effects:** None reported; variants identified to date are private (unique per family) rather than recurrent founder alleles.
- **Consanguinity:** Not implicated (AD, predominantly de novo mechanism).
- **Carrier frequency:** Not applicable in the traditional sense for an AD de novo disorder (there is no "carrier" state distinct from being affected, given the described high penetrance).
- **Genotype-phenotype correlation (2025 update):** A statistically significant difference in mean phenotype/hemi-severity score (HSS) was found across four variant classes (splice-site, other LOF, missense, multi-gene deletion); **missense variants trended toward greater severity**, reaching statistical significance specifically against splice-site variants. Within missense variants, those affecting the C-terminus or invariant ankyrin-repeat residues trended toward greater severity than other missense variants. **No sex-based difference in severity was found.**
- **Population demographics:** No ethnic, geographic, or ancestry-specific enrichment has been reported; cases have been described from North America, Europe, and East Asia (e.g., the Georgian case report, PMID: 37456926, and the Chinese case report, DOI: 10.3389/fgene.2024.1422469), consistent with a pan-ethnic de novo disorder.
- **Sex ratio:** Founding cohort was 19 females:15 males; the 2025 genotype-phenotype study found no severity difference by sex — overall the disorder appears to affect both sexes roughly equally, consistent with autosomal (not X-linked) inheritance.

---

## 10. Diagnostics

- **Primary diagnostic modality:** Molecular genetic testing — **exome sequencing (ES) or genome sequencing (GS)**, typically as a trio (proband + parents) to establish de novo status, is the standard diagnostic approach given the lack of a single characteristic "gestalt" sufficient for clinical diagnosis alone and the private nature of each variant. **Chromosomal microarray (CMA)** can detect the rarer 4q13.3 microdeletion cases. Single-gene sequencing of *ANKRD17* is possible once suspected but is not typically the first-tier test given the nonspecific overlapping phenotype.
- **Clinical/laboratory tests:** No specific biomarker, enzyme assay, or metabolic screening test exists; this is not a biochemically detectable disorder.
- **Imaging:** Brain MRI is recommended as part of the diagnostic workup given nonspecific structural brain abnormalities reported in some patients (formal MRI phenotyping is a stated objective of the ongoing NCT05528744 natural history study, but a systematized neuroimaging phenotype has not yet been published in detail).
- **Electrophysiology:** EEG indicated for patients with seizures; ictal abnormalities were found in 9/24 and interictal in 7/24 of the epilepsy sub-cohort.
- **Genetic testing hierarchy:** ES/GS trio-based analysis (first-tier for undiagnosed developmental delay in current practice generally, applicable here); CMA for deletion detection; targeted single-gene *ANKRD17* sequencing once a phenotype-driven suspicion exists (e.g., via the GeneReviews chapter's suggested clinical criteria).
- **Standardized diagnostic criteria:** No formal consensus clinical diagnostic criteria (akin to DSM/ICD operational criteria) have been published; diagnosis is molecular, confirmed by identification of a heterozygous pathogenic/likely pathogenic *ANKRD17* variant in the context of a compatible phenotype.
- **Differential diagnosis:** Given the phenotypic overlap with numerous other neurodevelopmental syndromes, GeneReviews lists differential considerations including Down syndrome, Pierre Robin sequence (isolated), and other genetically distinct developmental-delay/dysmorphism syndromes; broadly, CAGS sits within the large differential of "exome-first" neurodevelopmental disorders and is distinguished definitively only by molecular confirmation.
- **Screening:** No population or newborn screening program exists or is applicable (private de novo variants, no biochemical screening analyte).

---

## 11. Outcome / Prognosis

- **Survival/mortality:** No formal survival statistics (5-year/10-year survival, standardized mortality ratio) have been published; the disorder as characterized in living cohorts is not associated with premature mortality in the literature to date, though the reported prenatal/fetal case with multiple severe congenital anomalies (Xia et al. 2025) illustrates that the severe end of the phenotypic spectrum can be life-limiting in utero.
- **Morbidity/function:** Variable, ranging from borderline learning difficulties to severe-profound intellectual disability with need for lifelong multidisciplinary care; gait/balance disturbance and dysphagia (2025 update) suggest functional mobility and feeding-related morbidity in a subset.
- **Quality of life measures:** No published disease-specific or generic (EQ-5D/SF-36/PROMIS) QOL data yet.
- **Complications:** Recurrent bacterial/viral infections in roughly a third of patients; rare renal agenesis; rare cerebral hemorrhage (2025 update, not yet quantified); epilepsy (managed medically in the majority).
- **Recovery potential:** As a static developmental disorder, "recovery" in the traditional sense is not expected; developmental therapies aim to maximize functional trajectory rather than reverse an underlying degenerative process.
- **Prognostic factors:** The 2025 genotype-phenotype analysis suggests variant type (missense, especially C-terminal or invariant-repeat-residue missense) trends toward a more severe phenotype than truncating/splice-site variants, offering an early basis for genotype-informed prognostic counseling, though this remains a trend rather than a validated predictive model.
- **Prognostic biomarkers:** None established.

---

## 12. Treatment

There is **no disease-modifying or curative therapy**; management is entirely supportive/symptomatic and multidisciplinary, consistent with GeneReviews guidance.

- **Pharmacotherapy:** Anti-seizure medications for the subset with epilepsy — the epilepsy phenotype study found the majority achieve control with monotherapy (10/24), and seizures are generally infrequent (54% experience seizures less than annually), with only ~21% (5/24) meeting drug-resistant epilepsy criteria. No CAGS-specific pharmacogenomic guidance exists. Suggested NCIT term: NCIT:C15986 (Pharmacotherapy) as the general action term, with specific anti-seizure agents added as `therapeutic_agent` per individual case reports (agent-level detail not systematically reported in aggregate).
- **Advanced therapeutics:** No gene therapy, cell therapy, RNA-based therapy, targeted therapy, or immunotherapy has been developed or trialed for CAGS; given the haploinsufficiency mechanism, an allele-restoring approach (e.g., AAV-mediated gene supplementation) is theoretically conceivable but has not been reported even preclinically for this specific gene/disorder.
- **Surgical/interventional:** Cleft palate repair for the subset with Pierre Robin sequence/cleft palate (NCIT:C15329, Surgical Procedure category); management of renal agenesis as clinically indicated in rare cases.
- **Supportive/rehabilitative care (core of management):** Physical therapy (NCIT:C15302), occupational therapy (NCIT:C121351), and speech-language therapy (NCIT:C159273) are central given the disproportionate speech impairment and motor/gait involvement; nutritional/feeding support (NCIT:C15447, Dietary Intervention) for feeding difficulties; ophthalmological monitoring and correction (glasses/strabismus surgery) for refractive error and strabismus; genetic counseling (NCIT:C15240) for families.
- **Experimental/clinical trials:** No therapeutic clinical trials exist. The only registered study is the **observational natural history study NCT05528744** (Boston Children's Hospital, "Delineating the Molecular Spectrum and the Clinical, Imaging and Neuronal Phenotype of Chopra-Amiel-Gordon Syndrome"), which is a registry/biosample (including iPSC generation) study, not an interventional trial — important to distinguish when curating `clinical_trials` entries (phase would be `NOT_APPLICABLE`, an observational study).
- **Surveillance (per GeneReviews):** At each visit — assessment of developmental progress, educational needs, seizure activity, tone/movement changes, growth, nutrition/feeding status, and family psychosocial needs; annual or as-needed assessment of behavioral and musculoskeletal manifestations (e.g., scoliosis, joint hypermobility).
- **Treatment algorithms/combination therapy/personalized medicine:** None established beyond general developmental-disorder multidisciplinary care pathways; the emerging genotype-severity correlation (missense vs. truncating) could eventually inform anticipatory/personalized surveillance intensity, but this is not yet formalized into any published algorithm.

---

## 13. Prevention

As a predominantly de novo monogenic disorder, primary prevention in the population-health sense is not applicable.

- **Primary prevention:** Not applicable (de novo mutation, not preventable by lifestyle/exposure modification).
- **Secondary prevention:** Prenatal diagnosis is possible once a familial variant is known (relevant for the rare familial transmission case and for recurrence-risk counseling after germline mosaicism); no population-based screening program exists given the ultra-rare, non-recurrent (private-variant) nature of the disorder.
- **Genetic counseling:** Central prevention/planning tool — recurrence risk to siblings of a proband with an apparently de novo variant is low but slightly above general-population risk (germline mosaicism); risk to offspring of an affected individual is 50% (autosomal dominant), as demonstrated by the one reported affected mother-son transmission.
- **Screening/risk stratification:** Not applicable at a population level; clinically, ES/GS-based diagnosis in children presenting with developmental delay and the described dysmorphism functions as the practical "detection" pathway.
- **Prophylaxis:** No specific prophylactic medications indicated; management of recurrent infection susceptibility follows general pediatric infectious-disease supportive care rather than a CAGS-specific prophylactic regimen (not described in the literature).

---

## 14. Other Species / Natural Disease

- **Taxonomy of model/comparative species used:** Mouse (*Mus musculus*, NCBITaxon:10090); *Drosophila melanogaster* (NCBITaxon:7227, ortholog studies of *Mask*); human (NCBITaxon:9606).
- **Orthologous gene:** *Ankrd17* (mouse, MGI ortholog); *Mask* (*Drosophila* ortholog — "Multiple Ankyrin repeats Single KH domain").
- **Natural disease in other species:** No naturally occurring veterinary/companion-animal disease attributable to spontaneous *ANKRD17* loss-of-function has been reported (unlike many single-gene disorders with recognized breed-specific veterinary counterparts in OMIA); all animal data derive from engineered (knockout/knockdown) models rather than naturally occurring disease.
- **Comparative biology:** The vascular-integrity role of ANKRD17 (embryonic lethality with hemorrhage in complete mouse knockout) and the Hippo-pathway growth-regulatory role of *Drosophila* Mask indicate deep evolutionary conservation of ANKRD17/Mask function in tissue growth and vascular development across bilaterians, providing mechanistic continuity between invertebrate growth-control biology and the human neurodevelopmental phenotype (though the human disorder is a heterozygous partial-loss state, not the complete loss modeled in these systems).
- **Zoonotic potential/transmission:** Not applicable — this is a non-infectious, non-transmissible genetic disorder.

---

## 15. Model Organisms

| Model | Type | Key findings | Citation |
|---|---|---|---|
| Complete *Ankrd17* knockout mouse | Genetic (constitutive KO) | Embryonic lethal E10.5–E11.5; severe hemorrhage; drastically reduced vascular smooth muscle cells surrounding vessels; incomplete vascular maturation | Hou et al., FEBS Lett 2009 |
| AAV-mediated *Ankrd17* knockdown mouse (mPFC and hippocampal CA1) | Induced/regional knockdown (haploinsufficiency-mimicking) | Reduced GluN2A (NMDAR subunit), GluA1 (AMPAR subunit), PSD-95, Synapsin I in cortex/hippocampus; behavioral deficits in three-chamber social test, open-field (anxiety), Y-maze (spatial learning/memory); mitochondrial respiratory chain complex II gene downregulation (*Sdha/Sdhb/Sdhc*) confirmed by qPCR; proteomics (5D label-free) on mouse tissue and postmortem human embryonic brain showing 21.1% of differentially expressed proteins mitochondrially localized | Xia et al., J Neurodev Disord 2025 (PMID: 40604385) |
| *Drosophila* Mask (ortholog) mutant/RNAi | Genetic (invertebrate) | *Mask* functions as a co-factor of Yorkie in the Hippo pathway; required for tissue growth, specifically eye and wing growth in loss-of-function studies (cited by Chopra et al. 2021 as supportive homology evidence, not newly generated data in that paper) | Cited in Chopra et al., AJHG 2021 (original Mask functional studies predate the CAGS description) |
| Human patient iPSC-derived neurons | Planned/in-progress human cellular model | Patient-specific iPSC lines and isogenic controls for neuronal reprogramming and phenotyping — explicitly planned to "bridge the knowledge gap on the biological underpinnings of the disorder" | NCT05528744 (Boston Children's Hospital natural history study, ongoing) |

**Model limitations:** No published model to date fully recapitulates the heterozygous, partial-loss-of-function human genotype in a way that captures the full spectrum of human craniofacial dysmorphism, speech-specific impairment, or immune phenotype; the complete-knockout mouse models total absence (embryonic lethal, not directly comparable to the surviving heterozygous human state), while the AAV-knockdown model targets only two adult brain regions rather than the developmental, whole-organism haploinsufficiency state present from conception in patients. No zebrafish model of ANKRD17 loss was identified in the literature search performed for this report — this appears to be a genuine gap rather than an omission (worth noting explicitly per the reporting instructions for unavailable information).

---

## Summary of Ontology Term Suggestions

- **MONDO:** MONDO:0859186 (as given/confirmed)
- **OMIM:** 619504 (phenotype), *615929 (gene)
- **HGNC:** ANKRD17 (verify exact HGNC ID via direct HGNC lookup before binding — not independently confirmed in this session)
- **Key HP terms:** HP:0001263, HP:0001249, HP:0000750, HP:0001270, HP:0000717, HP:0007018, HP:0001288, HP:0001250, HP:0002121, HP:0002069, HP:0011097, HP:0000325, HP:0009890, HP:0000219, HP:0000486, HP:0000539, HP:0004325, HP:0003510, HP:0011968, HP:0001382, HP:0002719, HP:0002650, HP:0000104, HP:0001513, HP:0002015
- **GO terms (biological process):** GO:0035329 (hippo signaling), GO:0000082 (G1/S transition of mitotic cell cycle), GO:0032495 (NOD1/NOD2 response), GO:0022008 (neurogenesis), GO:0007416 (synapse assembly), GO:0022904 (respiratory electron transport chain)
- **CL terms:** CL:0002608 (radial glial cell), CL:0000359 (vascular smooth muscle cell), CL:0000099 (interneuron)
- **UBERON terms:** UBERON:0000955 (brain), UBERON:0002037 (cerebellum), UBERON:0001954 (Ammon's horn)
- **NCIT treatment terms:** NCIT:C15986 (Pharmacotherapy), NCIT:C15302 (Physical Therapy), NCIT:C121351 (Occupational Therapy), NCIT:C159273 (Speech Therapy), NCIT:C15329 (Surgical Procedure), NCIT:C15447 (Dietary Intervention), NCIT:C15240 (Genetic Counseling)

**All ontology term suggestions above are model-generated leads only — per this repository's Ontology Term Contract, each must be independently looked up (via `runoak`/OAK or the relevant `cache/<prefix>/terms.csv`) at the moment it is written into KB YAML; none should be bound from this report without a fresh verification step.**

---

## Key Sources

- [Chopra M et al., "Heterozygous ANKRD17 loss-of-function variants cause a syndrome with intellectual disability, speech delay, and dysmorphism," Am J Hum Genet 2021;108(6):1138-1150, PMID 33909992 (PMC8206162)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8206162/)
- [OMIM 619504 — CHOPRA-AMIEL-GORDON SYNDROME; CAGS](https://omim.org/entry/619504)
- [OMIM *615929 — ANKRD17](https://www.omim.org/entry/615929)
- [GeneReviews — ANKRD17-Related Neurodevelopmental Syndrome, NBK588029](https://www.ncbi.nlm.nih.gov/books/NBK588029/)
- [MedGen C5561975 / Chopra-Amiel-Gordon syndrome](https://www.ncbi.nlm.nih.gov/medgen/1794185)
- [Xia D et al., "Novel ANKRD17 variants implicate synaptic and mitochondrial disruptions in intellectual disability and autism spectrum disorder," J Neurodev Disord 2025;17:36, PMID 40604385 (PMC12219137)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12219137/)
- [Tkemaladze T et al., "A case of Chopra-Amiel-Gordon syndrome with a novel heterozygous variant in the ANKRD17 gene," SAGE Open Med Case Rep 2023, PMID 37456926](https://pubmed.ncbi.nlm.nih.gov/37456926/)
- [Case report: novel ANKRD17 splicing variant, tic disorder, Front Genet 2024, DOI 10.3389/fgene.2024.1422469](https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2024.1422469/full)
- [O32: ANKRD17-related neurodevelopmental syndrome — further characterization and genotype-phenotype correlations, 2025 conference abstract](https://www.sciencedirect.com/science/article/pii/S2949774425001475)
- [Epilepsy Phenotypes in Chopra-Amiel-Gordon Syndrome, AES abstract](https://aesnet.org/abstractslisting/epilepsy-phenotypes-in-chopra-amiel-gordon-syndrome)
- [NCT05528744 — Delineating the Molecular Spectrum and the Clinical, Imaging and Neuronal Phenotype of Chopra-Amiel-Gordon Syndrome, ClinicalTrials.gov](https://clinicaltrials.gov/study/NCT05528744)
- [Hou et al., "Ankrd17...is essential for vascular integrity during embryogenesis," FEBS Lett 2009 (via Wiley summary)](https://febs.onlinelibrary.wiley.com/doi/10.1016/j.febslet.2009.07.025)
- [ClinVar RCV001593058 — NM_032217.5(ANKRD17):c.2623G>T (p.Glu875Ter)](https://www.ncbi.nlm.nih.gov/clinvar/RCV001593058/)
- [ClinVar RCV001843437 — NM_032217.5(ANKRD17):c.833G>T (p.Gly278Val)](https://www.ncbi.nlm.nih.gov/clinvar/RCV001843437/)
- [Wikipedia — Chopra–Amiel–Gordon syndrome](https://en.wikipedia.org/wiki/Chopra%E2%80%93Amiel%E2%80%93Gordon_syndrome)

**Flagged gaps/uncertainties for curator follow-up:** (1) exact Orphanet ORPHA code unverified directly; (2) no zebrafish model found; (3) no episignature/epigenetic study published; (4) no dedicated QOL instrument data; (5) full GeneReviews percentage table (Table 2) could not be directly fetched (blocked by bot verification) — the frequencies cited above were cross-validated from the primary AJHG paper and the 2025 follow-up abstract instead.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 7 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 66 |
| Resolved | 63 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 1 |
| Terms whose name was checked | 39 |
| Terms named correctly | 25 |
| Terms named as a **different** term | 6 |
| Terms whose name is worth a second look | 8 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0859186` (3 mentions) - the report calls it "matches the target ID given"; MONDO calls it **Chopra-Amiel-Gordon syndrome**
- `HP:0004325` (2 mentions) - the report calls it "Postnatal growth failure"; HP calls it **Decreased body weight**
- `GO:0032495` (2 mentions) - the report calls it "NOD1/NOD2 response"; GO calls it **response to muramyl dipeptide**
- `CL:0002608` (3 mentions) - the report calls it "Cell types implicated:** radial glial progenitors", "radial glial cell"; CL calls it **hippocampal neuron**
- `UBERON:0002037` (2 mentions) - the report calls it "cerebellum, relevant to the cerebellar hypoplasia noted in the 2025 fetal case", "cerebellum"; UBERON calls it **cerebellum**
- `UBERON:0002316` (1 mention) - the report calls it "prefrontal cortex region approximation"; UBERON calls it **white matter**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0039528` (GO_0039528) (1 mention) - replaced by `GO:0002753`
- `CL:0008030` (obsolete excitatory neuron) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002121` (2 mentions) - the report calls it "Generalized absence seizure"; HP calls it **Generalized non-motor (absence) seizure**
- `HP:0002069` (2 mentions) - the report calls it "Generalized tonic-clonic seizure"; HP calls it **Bilateral tonic-clonic seizure**
- `HP:0000601` (1 mention) - the report calls it "deep-set eyes"; HP calls it **Hypotelorism**, and lists "Closely spaced eyes" among its other names
- `HP:0003510` (2 mentions) - the report calls it "Short stature"; HP calls it **Severe short stature**
- `CL:0000359` (3 mentions) - the report calls it "vascular smooth muscle cell"; CL calls it **vascular associated smooth muscle cell**, and lists "vascular smooth muscle cell" among its other names
- `UBERON:0001954` (2 mentions) - the report calls it "Ammon's horn/CA1", "Ammon's horn"; UBERON calls it **Ammon's horn**
- `GO:0005739` (1 mention) - the report calls it "mitochondrion, cellular component"; GO calls it **mitochondrion**
- `NCIT:C159273` (2 mentions) - the report calls it "Speech Therapy"; NCIT calls it **Speech Language Therapy**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0002608` - called "Cell types implicated:** radial glial progenitors", "radial glial cell"
- `UBERON:0002037` - called "cerebellum, relevant to the cerebellar hypoplasia noted in the 2025 fetal case", "cerebellum"
- `UBERON:0001954` - called "Ammon's horn/CA1", "Ammon's horn"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.