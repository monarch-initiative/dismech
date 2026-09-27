---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-23T15:00:30.919063'
end_time: '2026-09-23T15:05:50.437623'
duration_seconds: 319.52
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Townes-Brocks Syndrome 1
  mondo_id: MONDO:0054581
  category: Genetic
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
  num_turns: 18
  total_cost_usd: 1.4067906
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
citation_count: 27
reference_validation:
  total_references: 19
  verified: 19
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 19
  on_topic: 13
  validator_version: 0.2.1
term_validation:
  total_terms: 59
  verified: 57
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 24
  labels_matching: 19
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: HP:0002251
    reported_labels:
    - imperforate anus / anal stenosis
    ontology_label: Aganglionic megacolon
  - term_id: UBERON:0004907
    reported_labels:
    - anal canal
    ontology_label: lower digestive tract
  - term_id: UBERON:0002544
    reported_labels:
    - thumb
    ontology_label: digit
  - term_id: NCIT:C101294
    reported_labels:
    - approx. "Genetic Testing
    ontology_label: Whole Genome Sequencing
  labels_variant: 1
  obsolete_terms:
  - term_id: GO:0005720
    ontology_label: GO_0005720
    replaced_by: GO:0000792
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Townes-Brocks Syndrome 1
- **MONDO ID:** MONDO:0054581 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Townes-Brocks Syndrome 1** covering all of the
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

I'll research Townes-Brocks Syndrome 1 now and produce the full report inline.

# Townes-Brocks Syndrome 1 (TBS1) — Comprehensive Research Report

## 1. Disease Information

**Overview.** Townes-Brocks syndrome 1 (TBS1) is a rare, autosomal dominant multiple-congenital-anomaly disorder classically defined by a triad of imperforate anus/anal stenosis, dysplastic external ears, and thumb malformations (preaxial polydactyly and/or triphalangeal thumbs), caused by heterozygous pathogenic variants in **SALL1** (16q12.1). It was first delineated by Townes and Brocks in 1972 and molecularly linked to SALL1 by Kohlhase et al. in 1998 (Nat Genet 18:81–83) [PMID not separately retrieved but DOI 10.1038/ng0198-81 confirmed]. Expressivity is markedly variable — from an isolated ear/hearing phenotype to severe multiorgan disease including progressive kidney failure — while penetrance is reported as essentially complete once the mild end of the spectrum is included.

**Key identifiers:**
- **OMIM:** #107480 (Townes-Brocks syndrome 1); gene locus *602218 SALL1
- **Orphanet:** ORPHA857
- **MONDO:** MONDO:0054581 (per task); note a distinct **Townes-Brocks syndrome 2 (TBS2)**, caused by biallelic/dominant *DACT1* variants, lacks thumb anomalies and is a genetically and clinically separate entry (dismech CLAUDE.md's lump/split guidance applies — do not conflate TBS1/SALL1 with TBS2/DACT1)
- **MeSH:** D054970 (Townes-Brocks Syndrome)
- **ICD-10/11:** No dedicated code; typically coded under Q87.8 (other specified congenital malformation syndromes)
- **Gene/HGNC:** SALL1, hgnc:10524

**Synonyms:** Townes-Brocks syndrome; TBS; Townes syndrome; Imperforate anus with hand, foot, and ear anomalies; Renal-ear-anal-radial (REAR) syndrome (older, less accurate label given absence of true radial hypoplasia).

**Evidence basis:** Information is derived overwhelmingly from **aggregated case series/registries** (largest published cohorts ~40–150 patients; GeneReviews estimates ~200 total reported cases) rather than large-scale EHR data, reflecting the disease's rarity — this should be flagged as a `HUMAN_CLINICAL` evidence base of modest cohort size throughout curation, with wide confidence intervals on any reported frequency.

Sources: [SALL1-Related Townes-Brocks Syndrome – GeneReviews](https://www.ncbi.nlm.nih.gov/sites/books/NBK1445/), [OMIM #107480](https://omim.org/entry/107480), [Orphanet](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Lng=GB&Expert=857), [Townes-Brocks syndrome genotype-phenotype correlations, EJHG 2025](https://www.nature.com/articles/s41431-025-01855-4)

---

## 2. Etiology

**Disease causal factor:** Purely **genetic/monogenic** — heterozygous pathogenic (predominantly truncating) variants in *SALL1*. There is no known environmental, infectious, or toxic etiology; TBS1 is a primary developmental-genetic disorder.

**Genetic risk factors:**
- Virtually all reported pathogenic variants are **truncating** (nonsense, frameshift, small indels) clustered in **exon 2** (the second, and largest, coding exon) or occasionally intron 2, predicted to remove all C2H2 zinc-finger DNA-binding domains distal to the truncation point.
- **p.Arg276Ter (R276X)**, from a recurrent c.826C>T hotspot, is the most frequently reported single variant, found preferentially in **sporadic** rather than familial cases and associated with a more severe phenotype (94% classic triad; ~50% congenital heart disease, including the only reported SALL1-associated tetralogy of Fallot cases) (PMID:14627694, Botzenhart et al. 2007 hotspot-refinement study).
- Genotype-phenotype trend: variants toward the **5′ end** of the truncated protein and the canonical hotspot region tend to associate with more severe/complete phenotypes; **whole-gene or large deletions removing only SALL1** tend to produce a **milder** phenotype than hotspot truncating point variants — evidence favoring a **dominant-negative** mechanism for truncating alleles rather than pure haploinsufficiency (see Mechanism section) (PMC9956891; PMC12583617/PMID:40348827).
- ~50% of cases are **de novo**, with a strong parent-of-origin skew toward the **paternally derived allele (~87.5%)** per GeneReviews.
- **Somatic/gonadal mosaicism** has been documented in at least 4 families, relevant to recurrence-risk counseling even when parents appear clinically unaffected.
- A distinguishing genotype-phenotype note: **p.Arg1054Ter** causes a severe phenotype only in **homozygosity**; heterozygous carriers are reportedly unaffected — an exception to the general dominant/truncating rule and worth flagging explicitly if curated (do not generalize haploinsufficiency/dominant-negative claims across all truncating alleles without this caveat).

**Environmental/lifestyle risk factors:** None established. This is not a multifactorial or exposure-modulated disease in the current literature.

**Protective factors:** None described in humans. In the **mouse model** (see Mechanism/Model Organisms), the truncated Sall1 protein has been reported to confer *protection* from acute kidney injury (ischemia-reperfusion, aristolochic-acid nephrotoxicity) relative to wild-type — an intriguing but purely model-organism finding that should not be extrapolated to human protective factors (MODEL_ORGANISM evidence only; AJP-Renal 2015, doi 10.1152/ajprenal.00222.2015).

**Gene-environment interactions:** None reported; not applicable for this disorder.

Sources: [Botzenhart 2007 hot spot refinement (PMID:17221874)](https://pubmed.ncbi.nlm.nih.gov/17221874/), [High incidence of R276X (PMID:14627694)](https://pubmed.ncbi.nlm.nih.gov/14627694), [EJHG 2025 genotype-phenotype (PMID:40348827)](https://pubmed.ncbi.nlm.nih.gov/40348827/), [CMA-identified deletion, milder phenotype (PMC9956891)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9956891/)

---

## 3. Phenotypes

Frequencies below are drawn from GeneReviews' synthesis of the published cohort literature (~200 reported cases); treat these as pooled case-series estimates, not population-representative rates, and always attribute per-source when curating individual evidence items.

| Phenotype | Frequency | Onset | Suggested HPO term |
|---|---|---|---|
| Imperforate anus / anal stenosis | ~70–84% | Congenital | HP:0002251 (Imperforate anus) / HP:0002032 (Atresia of the small intestine — not this; use HP:0002028? — prefer **HP:0002251** Imperforate anus, and **HP:0025286** Anal stenosis if graded) |
| Dysplastic/malformed ears (overfolded superior helix, "lop ear," preauricular tags) | ~87% | Congenital | HP:0000411 (Protruding ear) / HP:0009909 (Overfolded helix) / HP:0000384 (Preauricular skin tag) |
| Sensorineural and/or conductive hearing loss | ~62% | Congenital, may progress | HP:0000407 (Sensorineural hearing impairment), HP:0000405 (Conductive hearing impairment), HP:0000365 (Hearing impairment, unspecified type) |
| Thumb malformation: triphalangeal thumb, preaxial polydactyly, rarely thumb hypoplasia | ~76–89% | Congenital | HP:0001199 (Triphalangeal thumb), HP:0001177 (Preaxial polydactyly), HP:0009601 (Thumb hypoplasia) |
| Renal structural/functional anomaly (hypoplasia/dysplasia, agenesis, multicystic/polycystic kidney, malrotation, ectopia, horseshoe kidney, VUR) — with or without progressive functional impairment to ESKD | ~40% reported structural/functional; renal **failure** specifically 29.3–39.6% across series | Congenital structural; functional decline can present from infancy through adulthood | HP:0000121 (Nephropathy) / HP:0000107 (Renal cyst) / HP:0000104 (Renal agenesis) / HP:0012622 (Chronic kidney disease) / HP:0000083 (Renal insufficiency) |
| Foot malformations (flat feet, overlapping toes, clubfoot) | Common, exact % variable | Congenital | HP:0001883 (Preaxial foot polydactyly) / HP:0001762 (Talipes equinovarus) |
| Genitourinary anomalies (hypospadias, bifid uterus, vaginal aplasia, cryptorchidism, bifid scrotum) | ~22% | Congenital | HP:0000047 (Hypospadias), HP:0000130 (Vaginal atresia/aplasia), HP:0000028 (Cryptorchidism) |
| Congenital heart disease (VSD, tetralogy of Fallot) | ~15% overall (~50% in R276X carriers) | Congenital | HP:0001629 (Ventricular septal defect), HP:0001636 (Tetralogy of Fallot) |
| Developmental delay / learning difficulty | ~15% | Childhood | HP:0001263 (Global developmental delay) |
| Hypothyroidism | Rare, reported in case series | Any age | HP:0000821 (Hypothyroidism) |
| Ocular anomalies (iris/chorioretinal coloboma, Duane anomaly) | Rare | Congenital | HP:0000612 (Iris coloboma), HP:0007803 (Chorioretinal coloboma), HP:0009921 (Duane anomaly) |
| Chiari I malformation | Rare | Any age (may be later-recognized) | HP:0007099 (Chiari type I malformation) |
| Growth deficiency (short stature; occasionally growth hormone deficiency) | Rare-occasional | Childhood | HP:0004322 (Short stature) |
| Umbilical hernia, dorsal corpus callosum hypoplasia (Botzenhart 2005 rare-feature list) | Rare | Congenital | HP:0001537 (Umbilical hernia), HP:0002079 (Hypoplasia of the corpus callosum) |

**Severity/progression pattern is a critical curation point.** Hearing loss and renal function are explicitly noted in the literature as **able to worsen at any age** — several patients are diagnosed in **adulthood**, sometimes only after presenting with unexplained end-stage renal disease (ESRD) and retrospective recognition of the ear/thumb triad (PMID:33438842 "Adult diagnosis of Townes-Brocks syndrome with renal failure"; PMID:9072124 "Townes-Brocks syndrome presenting as end stage renal failure"; PMID:17910067 "Kidney failure in Townes-Brocks syndrome: an under-recognized phenomenon?"). This argues for **lifelong** audiologic and renal surveillance rather than a childhood-only screening model, and for coding onset/course qualifiers (progressive, variable) on the renal and auditory phenotype nodes rather than treating them as static congenital findings only.

**Quality of life impact:** Not separately quantified with validated instruments (EQ-5D/SF-36) in the literature reviewed; qualitative impact is driven mainly by (1) hearing loss affecting speech/language development if unaddressed, (2) surgical burden and long-term bowel/continence function after anorectal malformation repair, and (3) burden of chronic kidney disease/dialysis/transplantation in the subset that progresses to ESKD.

Sources: [GeneReviews NBK1445](https://www.ncbi.nlm.nih.gov/sites/books/NBK1445/), [Kidney failure under-recognized (PMID:17910067)](https://pubmed.ncbi.nlm.nih.gov/17910067/), [Adult diagnosis with renal failure (PMID:33438842)](https://onlinelibrary.wiley.com/doi/abs/10.1002/ajmg.a.62050), [ESRF presentation (PMID:9072124)](https://pubmed.ncbi.nlm.nih.gov/9072124)

---

## 4. Genetic/Molecular Information

**Causal gene:** *SALL1* (Spalt-Like Transcription Factor 1), HGNC:10524, chromosome 16q12.1, OMIM *602218. Ortholog of *Drosophila* homeotic gene *spalt (sal)*. Encodes a **C2H2 double-zinc-finger transcriptional repressor** with four zinc-finger clusters, localizing predominantly to **pericentromeric heterochromatin/heterochromatic foci**.

**Variant spectrum:**
- Nearly all pathogenic variants are **truncating** — nonsense, frameshift-causing small insertions/deletions — clustering within **exon 2** (or intron 2 splice-affecting variants), predicted to eliminate all or most of the C-terminal zinc-finger domains.
- Missense variants and variants outside this hotspot region are rare and, when reported, should be interpreted cautiously per ACMG/AMP criteria (PVS1 typically applies for the truncating hotspot class; missense variants require stronger orthogonal evidence).
- Large **whole-gene deletions** (detected by chromosomal microarray/CNV analysis) also cause TBS1 but are associated with a **milder** phenotype than the recurrent truncating point variants — a genotype-phenotype dissociation directly supporting a dominant-negative (not simple loss-of-function/haploinsufficiency) mechanism for the truncating class (PMC9956891).
- A technical caveat for molecular diagnosis: a highly homologous **pseudogene, SALL1P1**, can confound capture-based NGS panel interpretation of SALL1 variants (GeneReviews).

**Functional consequence / mechanism classification:** Best modeled in `functional_impact_category` as **DOMINANT_NEGATIVE** for the truncating hotspot class (not simple LOSS_OF_FUNCTION), based on converging human genotype-phenotype and mouse genetic evidence (see Mechanism section below) — though GeneReviews itself hedges as "loss of function and possible dominant-negative effect," so this should be curated as the leading but not fully settled model, with the haploinsufficiency-only alternative explicitly noted (design-decisions §3a-style lump/split discipline: don't quietly resolve an open mechanistic question).

**Population/allele frequency:** SALL1 loss-of-function variants are appropriately rare/absent as common polymorphisms in population databases (gnomAD) consistent with a highly penetrant dominant disease mechanism; no specific pooled gnomAD constraint metric was independently verified in this pass and should be confirmed against gnomAD directly before citation (`pLI`/`LOEUF` for SALL1 is a plausible high-constraint value but was not verified here — flag as unverified rather than asserting a specific number).

**Modifier genes:** None firmly established; phenotypic variability even within families carrying the identical variant (documented in multiple case reports) suggests stochastic/epigenetic or unidentified modifier effects, but no specific modifier locus has been validated.

**Somatic vs. germline:** TBS1 is exclusively a **germline** disorder; SALL1 truncating variants are not established somatic cancer drivers in the way some other developmental genes are, so COSMIC/somatic databases are not relevant here.

**Chromosomal abnormalities:** Reported causal mechanism also includes **contiguous gene deletions/CNVs** spanning SALL1 at 16q12.1 (detectable by CMA), distinct from the more common intragenic truncating point variants.

**Epigenetics:** SALL1's own protein product functions partly through recruitment of the **NuRD (nucleosome remodeling and deacetylase) chromatin-remodeling complex** to regulate nephron progenitor gene expression (Development 2017, "A Sall1-NuRD interaction regulates multipotent nephron progenitors and is required for loop of Henle formation") — this is a mechanistic/epigenetic-regulator role of the gene product itself, not a reported disease-associated DNA methylation signature in patients; no patient-derived EWAS/methylation study for TBS1 was identified in this search.

Suggested ontology bindings: gene `hgnc:10524` (SALL1); GO molecular function GO:0003700 (DNA-binding transcription factor activity), GO:0001227 (DNA-binding transcription repressor activity, RNA polymerase II-specific).

Sources: [OMIM *602218 SALL1](https://omim.org/entry/602218), [Netzer et al. 2001, SALL1 TRF1/PIN2 pericentromeric heterochromatin (PMID:11751684)](https://academic.oup.com/hmg/article-abstract/10/26/3017/573522), [Sall1-NuRD nephron progenitors (Development 2017)](https://journals.biologists.com/dev/article/144/17/3080/47975/)

---

## 5. Environmental Information

Not applicable. TBS1 is a monogenic disorder with no known environmental toxin, lifestyle, or infectious contributor to disease causation. (Contrast with the "protective in an induced-injury mouse model" finding above, which is a downstream physiological observation about the mutant protein, not an environmental etiologic factor.) No entry should be created in `environmental:` unless a genuinely disease-modifying exposure (e.g., a specific nephrotoxin accelerating renal decline in a SALL1 carrier) is identified in future literature; none was found here.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (numbered, with inference flagged)

1. A **de novo or inherited heterozygous truncating variant in SALL1** (predominantly clustered in exon 2, most commonly the recurrent c.826C>T / p.Arg276Ter hotspot) removes the C-terminal zinc-finger DNA-binding/protein-interaction domains of the SALL1 repressor, while typically **sparing translation and stable expression of an N-terminal truncated protein** — demonstrated directly in patient-derived cells (PMID:18470945, Kiefer et al. 2008, Human Mutation).
2. This truncated protein **retains a self-association/heterochromatin-targeting domain** and, rather than being simply absent (haploinsufficiency), **co-aggregates with the wild-type SALL1 protein product of the normal allele**, mislocalizing it away from its normal pericentromeric heterochromatic foci — this is the biochemical basis proposed for a **dominant-negative** mechanism (built on SALL1's normal heterochromatin-targeting behavior described in Netzer et al. 2001, PMID:11751684; direct dominant-negative transcriptional consequence shown in Kiefer et al. 2008, PMID:18470945, where truncated SALL1 caused **ectopic activation of downstream target genes** rather than mere loss of repression).
3. Loss of correct SALL1-mediated transcriptional repression, at the wrong dose and/or at the wrong nuclear location, **leads to ectopic/dysregulated expression of SALL1 target genes** in the tissues where SALL1 is normally expressed during embryogenesis — this step is demonstrated in patient cell lines and knock-in mouse models but the full identity of relevant human target genes in each affected tissue remains incompletely characterized (an explicit knowledge gap).
4. Downstream, **tissue-specific consequences result from disruption of three principal SALL1-dependent embryonic programs, each contributing a branch of the phenotype**:
   - **4a. Anorectal/cloacal development branch** → disruption of normal hindgut/cloacal septation and anal canal formation → **imperforate anus / anal stenosis** (HP:0002251). Mechanistic detail in humans is incompletely resolved; supportive evidence is largely from mouse Sall1/Sall4 double-mutant studies showing cooperative roles in anorectal, cardiac, and CNS development (Development 2006, "murine homolog of SALL4... cooperates with Sall1 in anorectal, heart, brain and kidney development").
   - **4b. Limb (thumb/first digit) development branch** → SALL1 (with functional redundancy from SALL4) is expressed in the posterior limb bud and near the apical ectodermal ridge (AER), where it participates in patterning the anterior (preaxial) limb field → disruption **leads to** duplication (preaxial polydactyly, triphalangeal thumb) rather than the *loss*-of-structure pattern (radial hypoplasia) characteristic of the SALL4-related Okihiro/Duane-radial-ray spectrum — a key phenotypic distinguisher supported directly by a transgenic mouse expressing the truncated protein alone, which was **sufficient to reproduce the limb phenotype** (Kohlhase group, Hum Mol Genet 2003, "Expression of a truncated Sall1 transcriptional repressor is responsible for Townes–Brocks syndrome birth defects," PMID not independently re-verified numerically here but DOI academic.oup.com/hmg/article/12/17/2221).
   - **4c. Ear/hearing branch** → disrupted SALL1-dependent patterning of the developing external and possibly inner ear structures → **leads to** dysplastic pinna morphology (overfolded helix, preauricular tags) and, independently or in parallel, sensorineural and/or conductive **hearing impairment** — the precise inner-ear cellular mechanism for the sensorineural component is not fully elucidated in the literature surveyed here (flag as a knowledge gap; candidate mechanism by analogy to other developmental hearing-loss genes would be a cochlear/otic-vesicle patterning defect, but this is inferred, not directly demonstrated for SALL1).
   - **4d. Kidney (nephron progenitor) branch** → SALL1 is required, together with NuRD-complex recruitment, to **maintain the multipotent nephron progenitor pool**, balancing progenitor self-renewal versus premature differentiation, and (independently) is required in the **metanephric mesenchyme to attract ureteric bud outgrowth**, plausibly via mesenchyme-derived GDNF signaling → disruption **leads to** a spectrum from mild renal hypoplasia/dysplasia/malrotation through multicystic dysplastic kidney to (in the mouse null) complete renal agenesis; this same progenitor-pool/nephron-number deficit is proposed to **underlie later, progressive loss of renal function/CKD-to-ESKD** in patients even when the kidney appears only mildly structurally abnormal at birth — this progression step (structural anomaly/reduced nephron endowment → oligonephronic hyperfiltration → progressive CKD → ESKD) is a plausible but **partially inferred** mechanistic bridge in humans, built on (i) the mouse developmental biology (Nishinakamura et al. 2001, PMID:11688560, *Development*; Kobayashi 2017 Sall1-NuRD paper) and (ii) the clinical observation that renal failure can present or progress **independent of severe structural anomaly** and at any age (PMID:17910067; a 2026 case report using serial kidney biopsies to document progressive glomerular pathology, "Serial Kidney Biopsies Reveal Progressive Pathology in Townes-Brocks Syndrome," Kidney Medicine).
5. Homozygous/biallelic loss of SALL1 (not the human disease genotype, but informative for mechanism) causes **complete bilateral renal agenesis** in mice, establishing that SALL1 dosage is on a **severity gradient** from mild heterozygous dysplasia (human TBS1) to complete agenesis (biallelic loss) — consistent with, though not proof of, a dosage-graded pathway in which the dominant-negative truncated allele behaves functionally "worse than" a simple null heterozygote for some tissues, explaining why truncating variants can be more severe than whole-gene deletions (point 4d converges with the genotype-phenotype data in Etiology).

### Category detail

- **Molecular pathways:** SALL1 acts as a transcriptional repressor recruiting the **NuRD chromatin remodeling/deacetylase complex**; interacts with **TRF1/PIN2** and localizes to pericentromeric heterochromatin (PMID:11751684). No canonical signaling pathway (Wnt/MAPK/mTOR) has been established as the direct SALL1 mechanism in TBS1 itself, though SALL genes intersect with limb-patterning networks (Shh/Gremlin1/Tbx2 signaling context) via their role in AER-adjacent limb bud gene expression.
- **Cellular processes:** Nephron progenitor self-renewal vs. differentiation balance (Sall1 in mouse metanephric mesenchyme); heterochromatin organization/gene silencing; apoptosis of metanephric mesenchyme in the SALL1-null state.
- **Protein dysfunction:** Premature-truncation → stable but mislocalizing/aggregating repressor protein → dominant-negative sequestration of wild-type SALL1 (and possibly co-repressor complex components) away from correct heterochromatic targets.
- **Tissue damage mechanisms:** In the kidney, the proposed chronic-injury mechanism is **reduced functional nephron mass/oligonephronic state → compensatory hyperfiltration → progressive glomerulosclerosis** (consistent with, though not proven identical to, the pattern documented by the serial-biopsy case report referenced above); this should be curated as `INFERRED`/model-supported rather than fully human-mechanism-proven.
- **Cell types involved (CL):** metanephric mesenchymal cell (nephron progenitor), CL:0002520 (or CL:1000384 nephron progenitor cell) and ureteric bud epithelial cell (CL:1001430) for the kidney branch; limb bud mesenchymal cell for the digit branch; otic/auricular precursor cell for the ear branch (exact CL term for auricular cartilage precursor not verified — flag as needing dismech-terms lookup rather than asserting one from memory).
- **Molecular profiling / omics:** No large-scale patient transcriptomic, proteomic, or single-cell dataset specific to TBS1 patient tissue was identified in this search; mouse Sall1-GFP knock-in and microarray studies have been used to define the kidney mesenchymal gene expression program downstream of Sall1 (PMID:15172686), which is the closest available "omics" resource and is model-organism, not patient, data.

Suggested GO biological process terms: GO:0072164 (mesonephric tubule development)/GO:0001656 (metanephros development), GO:0090190 (positive regulation of branching involved in ureteric bud morphogenesis) — negatively regulated in disease, GO:0072028 (nephron morphogenesis).

Sources: [Kiefer 2008 ectopic gene expression (PMID:18470945)](https://pubmed.ncbi.nlm.nih.gov/18470945/), [Netzer 2001 heterochromatin/TRF1-PIN2 (PMID:11751684)](https://academic.oup.com/hmg/article-abstract/10/26/3017/573522), [Nishinakamura 2001 Sall1 kidney agenesis (PMID:11688560)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4625151), [Sall1-NuRD nephron progenitors, Development 2017](https://journals.biologists.com/dev/article/144/17/3080/47975/), [Truncated Sall1 sufficient for limb phenotype, HMG 2003](https://academic.oup.com/hmg/article/12/17/2221/692156)

---

## 7. Anatomical Structures Affected

**Organ level (primary):**
- **Anorectum/hindgut** — imperforate anus, anal stenosis
- **External and middle/inner ear** — pinna dysplasia; sensorineural and conductive hearing apparatus
- **Upper limb (thumb/first ray)** and, less prominently, **lower limb/foot**
- **Kidney and urinary tract** — dysplasia, hypoplasia, cystic disease, agenesis, vesicoureteral reflux
- **Genital tract** (secondary/associated): hypospadias, bifid uterus, vaginal aplasia, cryptorchidism

**Secondary/complication-level organ involvement:**
- **Heart** — septal defects, tetralogy of Fallot (notably enriched in R276X carriers)
- **Thyroid** — occasional hypothyroidism
- **Eye** — iris/chorioretinal coloboma (rare)
- **CNS** — Chiari I malformation, corpus callosum hypoplasia (rare); developmental delay/learning difficulty in a minority
- **Musculoskeletal (foot)** — clubfoot, overlapping toes, flat feet

**Body systems involved:** digestive (anorectal), auditory/otic, musculoskeletal (limb), renal/urinary, reproductive/genital, cardiovascular, endocrine (thyroid), ophthalmologic, neurologic (minor subset).

**Tissue/cell level:**
- Metanephric mesenchyme and nephron progenitor cells (kidney)
- Ureteric bud epithelium (kidney collecting system)
- Cochlear/vestibular and middle-ear ossicular structures (hearing)
- Auricular cartilage and skin (ear dysplasia, preauricular tags)
- Limb bud mesenchyme, apical ectodermal ridge-adjacent tissue (digit patterning)
- Cloacal membrane/hindgut endoderm and surrounding mesenchyme (anorectal)

**Subcellular level:** SALL1 protein localizes to **pericentromeric heterochromatin** within the nucleus (GO:0005720 pericentric heterochromatin) — this is the key subcellular compartment implicated mechanistically, since the truncated protein's mislocalization/aggregation there is central to the proposed dominant-negative model.

**Localization/laterality:** Renal, ear, limb, and cardiac anomalies can each be unilateral, bilateral, or asymmetric between sides in an individual patient (e.g., unilateral renal agenesis with contralateral normal kidney is reported); imperforate anus is midline by definition. No consistent, obligate lateralization pattern is described.

Suggested UBERON terms: UBERON:0000059 (large intestine)/UBERON:0004907 (anal canal), UBERON:0001690 (ear), UBERON:0002113 (kidney), UBERON:0002544 (thumb).

---

## 8. Temporal Development

**Onset:** Congenital for the core structural triad (anorectal, ear, thumb anomalies) — present and typically recognized at birth or in early infancy given the visible nature of imperforate anus and ear dysplasia. High-resolution prenatal ultrasound can detect phenotypic features (limb anomalies, some renal anomalies) from approximately **16 weeks' gestation** onward once a familial pathogenic variant is known (GeneReviews).

**Onset pattern:** Structural anomalies are present at birth (congenital, not acquired); functional manifestations — most importantly **hearing loss and renal function decline** — can have delayed or progressive onset, occurring at essentially any age from infancy through adulthood. This is explicitly emphasized in the literature ("renal failure and deafness can occur at any age, making follow-up essential") and is supported by multiple **adult-onset diagnostic** case reports where TBS1 was first recognized because of unexplained ESRD in adulthood (PMID:33438842, PMID:9072124).

**Progression:**
- Anorectal, limb, and ear structural anomalies are **static/non-progressive** once formed (surgical correction addresses function, not an evolving structural process).
- **Renal disease course** ranges from stable mild structural anomaly with normal lifelong function, to slowly **progressive chronic kidney disease**, to **end-stage kidney disease** requiring dialysis/transplantation — reported in a substantial minority (~29–40% across series). A 2026 case report using serial biopsies specifically documents progressive glomerular pathology over time in an affected individual, directly supporting a genuinely progressive (not merely static-congenital) renal phenotype in at least some patients.
- **Hearing loss** can range from mild and stable to severe and may itself be progressive in some patients (GeneReviews; exact proportion progressive vs. stable not separately quantified in the sources reviewed here).

**Disease course pattern:** Best characterized as a **stable congenital malformation complex with a superimposed, variably progressive organ-functional component** (renal, auditory) rather than either a purely static syndrome or a uniformly progressive disease — this composite pattern should be reflected in `progression:` entries that separate structural (stable) from functional (progressive/variable) phenotypes rather than assigning one course descriptor to the whole entry.

**Critical periods:** The main clinically actionable "critical period" is the **immediate neonatal period**, when imperforate anus requires urgent surgical correction, and **early childhood**, when timely identification and management of hearing loss is critical to avoid secondary speech/language impairment.

---

## 9. Inheritance and Population

**Epidemiology:**
- Estimated frequency **~1 in 250,000 live births** (commonly cited figure, e.g., NORD/Orphanet-derived); a more recent estimate from monogenic-kidney-disease-panel testing data reported the SALL1 pathogenic variant carrier prevalence as **1 in ~238,000–342,000** in the general population depending on the specific study/denominator used, and notably **1 in 1,592** among individuals ascertained for monogenic kidney disease testing, and **1 in 2,952** among hearing-loss cohorts — reflecting substantial ascertainment bias toward these two organ-specific testing pathways (GeneReviews synthesis of multiple cohort-testing studies).
- Only **~200 patients** are reported in the medical literature to date per GeneReviews, underscoring the rarity and the wide uncertainty around any single prevalence figure.

**Inheritance pattern:** **Autosomal dominant.**

**Penetrance:** Reported as **~100%** once the full mild-to-severe phenotypic spectrum is considered (i.e., essentially no asymptomatic obligate carriers when comprehensively examined), though individual features (e.g., renal failure, hearing loss) are incompletely penetrant/variable in timing.

**Expressivity:** **Highly variable**, even within the same family and among carriers of the identical pathogenic variant — ranging from isolated dysplastic-ear/hearing-loss presentations (mimicking branchio-oto-renal syndrome) to the full multi-organ triad-plus phenotype with ESKD and congenital heart disease.

**Genetic anticipation:** Not described/not applicable — TBS1 is not a repeat-expansion disorder.

**Germline mosaicism:** Documented in at least 4 reported instances, relevant to recurrence-risk counseling for apparently unaffected parents of an affected child.

**Founder effects:** No specific population founder variant is established; the R276X hotspot arises recurrently (mutational hotspot at a CpG-type site) rather than reflecting a single ancestral founder haplotype, and is seen preferentially in **sporadic** cases (arguing against a shared-ancestry founder explanation and for recurrent independent mutation at this site).

**Consanguinity:** Not a relevant risk factor for this autosomal dominant disorder (consanguinity is relevant to recessive disease; TBS1 risk is driven by de novo mutation rate or transmission from an affected/mosaic dominant carrier, not parental relatedness).

**Carrier frequency:** Not meaningfully applicable in the traditional AR-disease sense; the relevant population parameter is de novo mutation rate plus a small pool of affected/transmitting individuals given reduced reproductive fitness in more severely affected cases.

**Population demographics:**
- No specific ethnic or geographic enrichment is established in the literature surveyed; cases have been reported from multiple populations (e.g., Chinese, Brazilian, European cohorts appear repeatedly in the case-report literature retrieved here), consistent with a pan-ethnic disorder driven by recurrent de novo mutation rather than population-specific founder effects.
- **Sex ratio:** No sex predilection is reported; autosomal dominant inheritance is consistent with equal male:female occurrence.
- **Age distribution:** Bimodal ascertainment pattern in practice — most patients are diagnosed in **infancy/early childhood** because of the visible anorectal/ear/limb triad, but a clinically important subset is diagnosed only in **adulthood**, typically via unexplained renal failure or hearing-loss/kidney gene panel testing.

Sources: [GeneReviews NBK1445](https://www.ncbi.nlm.nih.gov/sites/books/NBK1445/), [Kidney Gene Panel Testing reveals TBS (ScienceDirect)](https://www.sciencedirect.com/science/article/pii/S2468024924016176)

---

## 10. Diagnostics

**Clinical diagnostic criteria:** No single formal consensus scoring system (akin to DSM/ICD criteria) is standardized in the literature; diagnosis is clinically suspected from the **triad** (imperforate anus/anal stenosis + dysplastic ears ± hearing loss + thumb malformation) and confirmed molecularly. GeneReviews-cited series report the individual triad components at roughly 70–89% each (see Phenotypes table), meaning **not all three need be present** for clinical suspicion, particularly given the mild end of the spectrum (isolated ear/hearing phenotype).

**Genetic testing (primary diagnostic modality):**
- **First-tier gene-targeted testing:** SALL1 sequence analysis — detects >90% of pathogenic variants — followed by deletion/duplication (CNV) analysis (chromosomal microarray or MLPA/targeted CNV assay) if sequencing is negative but clinical suspicion remains high, given the described whole-gene-deletion allelic class.
- **Multigene panel:** SALL1 plus SALL4 and other differential-diagnosis genes (e.g., EYA1/SIX1, TBX5), useful when the phenotype is atypical or overlaps a differential category.
- **Comprehensive genomic testing:** Exome/genome sequencing appropriate for atypical presentations without a clear triad.
- **Technical pitfall:** the SALL1P1 pseudogene can interfere with capture-based NGS panel variant calling at the SALL1 locus — worth flagging in any `notes:` field discussing testing methodology.
- **Chromosomal microarray (CMA):** Specifically useful for detecting the whole-gene-deletion allelic class associated with the milder phenotype.

**Imaging/functional/laboratory workup** (used for phenotype characterization and management rather than primary diagnosis):
- **Renal ultrasound** at diagnosis and longitudinally (structural anomaly detection: hypoplasia, cysts, agenesis, malrotation, horseshoe kidney, VUR).
- **Renal function laboratory monitoring** (serum creatinine/eGFR) — explicitly recommended **annually in all individuals regardless of baseline normalcy**, given the risk of functional decline independent of structural anomaly.
- **Audiology (behavioral/objective hearing testing)** at diagnosis and **annually** thereafter given the risk of progressive loss.
- **Echocardiogram** at diagnosis, particularly emphasized for R276X carriers given the elevated congenital-heart-disease rate.
- **Skeletal/orthopedic examination** of hands and feet.
- **Ophthalmologic examination** as clinically indicated.
- **Thyroid function testing** given occasional hypothyroidism.
- **Developmental/behavioral assessment**, annually.

**Prenatal diagnosis:** Once a familial SALL1 pathogenic variant is identified, prenatal molecular testing (chorionic villus sampling/amniocentesis) or preimplantation genetic testing is possible; high-resolution ultrasound can also detect structural features (limb, some renal) from mid-second trimester (~16 weeks) onward. Notably, GeneReviews states that except for the R276X genotype (which reliably predicts a severe phenotype), **genotype cannot reliably predict the severity of specific manifestations** for prenatal counseling purposes — an important caveat against over-promising prognostic precision from prenatal genetic results alone.

**Differential diagnosis** (critical for correct curation — do not conflate these distinct entities):
- **SALL4-related Duane-radial ray syndrome (Okihiro syndrome)** — distinguished by radial/forearm involvement (true radial hypoplasia, absent in TBS1) and Duane anomaly; test SALL4 if radial or Duane features present.
- **Branchiootorenal (BOR) spectrum disorder** (EYA1/SIX1/SIX5) — branchial fistulae/cysts characteristic; lacks thumb malformations. Particularly relevant because mild TBS1 (isolated ear/hearing/renal phenotype without triad) can closely mimic BOR.
- **Holt-Oram syndrome** (TBX5) — carpal bone anomalies and cardiac septal defects but no typical ear dysplasia or anorectal anomaly.
- **VACTERL association** — important differential especially for sporadic/simplex presentations; severe vertebral anomalies and tracheoesophageal fistula are not features of SALL1-related TBS1 and their presence argues against this diagnosis.
- **Townes-Brocks syndrome 2 (DACT1-related)** — lacks thumb anomalies; a genetically distinct entity that must be kept separate in curation per the dismech lump/split discipline.
- **Goldenhar syndrome/hemifacial microsomia spectrum** — ear anomaly overlap; a specific paper (Genetics in Medicine, "Townes-Brocks syndrome versus expanded spectrum hemifacial microsomia") documents diagnostic overlap and the SALL1 hotspot's relevance to this differential.

Suggested NCIT term for genetic testing modality: NCIT:C101294 (approx. "Genetic Testing") — verify exact CURIE via OAK before binding.

Sources: [GeneReviews NBK1445](https://www.ncbi.nlm.nih.gov/sites/books/NBK1445/), [TBS vs. hemifacial microsomia (Genetics in Medicine)](https://www.nature.com/articles/gim200157), [SALL4-Related Disorders GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK1373/)

---

## 11. Outcome/Prognosis

**Survival/mortality:** No population-level survival statistics (5-/10-year survival curves, SEER-style data) exist for this ultra-rare disorder. Mortality risk, where it exists, is driven primarily by the minority of patients who progress to **end-stage kidney disease** and its associated morbidity, and — much less commonly — by significant congenital heart disease (tetralogy of Fallot) in the R276X subgroup. With modern surgical and renal-replacement management, overall life expectancy for most TBS1 patients (those without severe renal/cardiac involvement) is not reported as significantly reduced.

**Morbidity/functional outcomes:**
- **Renal:** the dominant driver of long-term morbidity in the more severely affected subset; **29–40% of reported patients develop renal failure**, some progressing to dialysis-dependent ESKD and requiring **kidney transplantation**.
- **Auditory:** untreated/undiagnosed progressive hearing loss carries risk of speech-language developmental impact if not identified and managed (hearing aids, early intervention) promptly.
- **Bowel/continence:** long-term function after anorectal malformation repair varies with the severity of the original anomaly and surgical outcome, as in anorectal malformations generally; TBS1-specific continence outcome data were not separately identified in this search.
- **Musculoskeletal:** hand function after thumb anomaly correction is generally favorable with appropriate surgical management.
- **Developmental:** ~15% experience developmental delay/learning difficulty, a minority but a real burden for those affected.

**Complications:** Recurrent/progressive CKD-to-ESKD; hypothyroidism (if undiagnosed, systemic metabolic consequences); congenital heart disease-related complications in the R276X subgroup; secondary complications of chronic hearing loss if unmanaged.

**Prognostic factors:**
- **Genotype** is the single most informative prognostic factor identified: the **R276X hotspot variant** predicts a high likelihood of the full classic triad (94%) and a markedly elevated risk of congenital heart disease (~50%), useful for anticipatory cardiac screening.
- **Whole-gene deletion** genotype predicts a comparatively **milder** overall phenotype than hotspot truncating variants.
- Beyond these two genotype classes, GeneReviews explicitly notes that specific manifestation severity **cannot be reliably predicted from genotype** for prenatal/genetic counseling purposes — an important, honestly-stated limitation rather than an unqualified genotype-phenotype prediction claim.
- Presence of **any** renal structural anomaly at diagnosis, and baseline renal function, are the most direct clinical prognostic indicators for future kidney trajectory, which is why annual renal function monitoring (regardless of baseline normalcy) is specifically recommended — implying that even a "normal-appearing" baseline does not exclude later decline.

Sources: [GeneReviews NBK1445](https://www.ncbi.nlm.nih.gov/sites/books/NBK1445/), [Delayed diagnosis with kidney failure (PMC12779858)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12779858/), [Serial Kidney Biopsies, Progressive Pathology in TBS, Kidney Medicine](https://www.kidneymedicinejournal.org/article/S2590-0595(26)00096-8/fulltext)

---

## 12. Treatment

There is **no disease-modifying or gene-targeted therapy** for TBS1; management is entirely **surgical, supportive, and surveillance-based**, directed at each organ-system manifestation.

**Surgical/interventional:**
- **Anorectal malformation repair** — urgent/early surgical correction of imperforate anus in the neonatal period (staged anoplasty/colostomy approach as per standard anorectal malformation surgical protocols). *Suggested NCIT term:* NCIT:C15329 (Surgical Procedure) as the general treatment_term, with `preferred_term` specifying anorectoplasty.
- **Thumb/hand surgical correction** for severe polydactyly or triphalangeal thumb impairing function, per standard hand-surgery approach. NCIT:C16186 (Orthopedic Surgical Procedure).
- **Cardiac surgery** for structural congenital heart disease (VSD closure, tetralogy of Fallot repair) as clinically indicated, particularly relevant to screen for/anticipate in R276X carriers. NCIT:C15329.
- **Kidney transplantation** for individuals progressing to ESKD. NCIT:C15289 (Organ Transplantation).
- **Cochlear implantation or other otologic surgical procedures** may be relevant for select severe/conductive hearing-loss cases (general principle for severe congenital hearing loss; TBS1-specific cochlear implant outcome data were not separately identified in this search — flag as inferred from general otologic practice, not TBS1-specific evidence, if curated).

**Supportive/medical:**
- **Constipation management** — stool softeners, laxatives, osmotic agents — a recurring post-anorectoplasty and general GI management need, per GeneReviews management table. NCIT:C15747 (Supportive Care) as general category; `therapeutic_agent` for specific laxative classes as needed.
- **Hearing aids** and early audiologic intervention for identified hearing loss. No specific NCIT device term was independently verified for hearing-aid fitting; per dismech convention, bind the clinical action (e.g., NCIT:C15747 Supportive Care, or an appropriate rehabilitation term) and carry device specificity in `preferred_term`, verifying the exact CURIE via OAK before binding.
- **Renal replacement therapy** — dialysis (hemodialysis/peritoneal) as a bridge to or alternative for kidney transplantation in ESKD.
- **Growth hormone therapy** for the subset with documented growth hormone deficiency, per GeneReviews management recommendations. NCIT:C15986 (Pharmacotherapy) + `therapeutic_agent` (recombinant human growth hormone, somatropin — CHEBI/NCIT CURIE to be verified before binding).
- **Levothyroxine replacement** for documented hypothyroidism (inferred standard-of-care management for a reported associated finding; not separately verified as TBS1-specific literature in this pass).
- **Rehabilitative therapy** (physical/occupational/speech therapy) as clinically indicated for musculoskeletal or hearing-related functional impact. NCIT:C15302 (Physical Therapy) / NCIT:C159273 (Speech Therapy).

**Medications to avoid:** GeneReviews specifically flags avoidance of medications with **nephrotoxic or ototoxic potential** in TBS1 patients, given the baseline vulnerability of both organ systems — an important, disease-specific pharmacologic caution worth capturing explicitly (e.g., in `notes:` on relevant treatment or pathophysiology nodes) rather than only as a generic statement.

**Experimental/investigational therapies:** No SALL1-targeted molecular therapy (gene therapy, ASO, small molecule correcting the dominant-negative mechanism) has reached clinical development based on this search; no relevant ClinicalTrials.gov-registered interventional trial specific to TBS1 was identified. This is consistent with the disease's rarity and the current absence of a mechanism-specific pharmacologic target beyond standard organ-supportive care.

**Treatment strategy:** Best modeled as a **lifelong, multidisciplinary surveillance-and-management algorithm** (genetics, urology/nephrology, otolaryngology/audiology, cardiology, orthopedics/hand surgery, colorectal surgery, endocrinology, ophthalmology, developmental pediatrics) rather than a single linear treatment pathway, reflecting the multi-organ and variably progressive nature of the disease.

Sources: [GeneReviews NBK1445](https://www.ncbi.nlm.nih.gov/sites/books/NBK1445/) (management/surveillance table), [NORD Townes-Brocks Syndrome](https://rarediseases.org/rare-diseases/townes-brocks-syndrome/)

---

## 13. Prevention

**Primary prevention:** Not applicable in the traditional sense (no environmental/behavioral risk-factor modification exists for this monogenic, largely de novo disorder). The relevant "primary prevention" tool is **genetic counseling and reproductive options** for known carrier families (prenatal diagnosis, preimplantation genetic testing) rather than population-level risk-factor reduction.

**Secondary prevention (early detection):**
- **Newborn/early recognition** of the visible triad (imperforate anus, ear dysplasia, thumb anomaly) is itself the practical "screening" mechanism that triggers confirmatory genetic testing and the subsequent surveillance cascade (renal ultrasound, audiology, echocardiogram) — early recognition is explicitly emphasized in the literature as key to preventing downstream morbidity (e.g., catching progressive hearing loss or renal decline before it causes irreversible harm).
- **Cascade/family screening**: once a proband's SALL1 variant is known, testing at-risk relatives (including apparently unaffected parents, given variable expressivity) is recommended to identify mildly affected family members who might otherwise be missed and to inform recurrence risk.

**Genetic counseling:** Central to prevention/family planning in TBS1 — explaining the ~50% transmission risk per pregnancy for an affected parent, the possibility of germline mosaicism (and therefore non-negligible recurrence risk even with two apparently unaffected parents), the general inability to predict specific manifestation severity from genotype (except the R276X-severe association), and the availability of prenatal or preimplantation genetic testing once a familial variant is identified.

**Tertiary prevention (preventing complications in affected individuals):** This is where most of the disorder's "prevention" activity actually concentrates, per the GeneReviews surveillance table — **annual renal function monitoring** to catch and manage CKD progression before ESKD, **annual audiology** to catch progressive hearing loss early, **avoidance of nephrotoxic/ototoxic medications**, and routine cardiac, developmental, growth/thyroid, and ophthalmologic surveillance to catch and manage associated complications proactively rather than reactively.

**Screening programs:** No population-based newborn screening test exists (or would be expected, given the disorder's visible congenital presentation and extreme rarity); screening in practice is clinical (recognition-triggered) rather than a laboratory-based population screen.

**Public health/environmental interventions:** Not applicable — no environmental determinant to intervene upon.

---

## 14. Other Species / Natural Disease

**Taxonomy:** No naturally occurring TBS1-equivalent disease has been described in a non-human species in the literature surveyed here (i.e., this does not appear in OMIA as a veterinary/naturally occurring disease entity based on this search). TBS1 modeling in other species is exclusively via **engineered/induced genetic models** (see Model Organisms, below), not naturally occurring disease.

**Orthologous gene:** Mouse *Sall1* (MGI ortholog of human SALL1) is the principal comparative-genetics resource; *Sall1* and its paralog *Sall4* show partial functional redundancy in several developmental contexts (hindlimb initiation, anorectal/cardiac/renal/CNS development), which is directly informative for understanding the human TBS1 (SALL1) vs. Okihiro/Duane-radial-ray syndrome (SALL4) phenotypic contrast — SALL4 human disease is predominantly a haploinsufficiency/radial-ray-loss phenotype whereas SALL1 human disease (TBS1) is predominantly a dominant-negative/digit-duplication phenotype, and comparative mouse genetics is the primary evidentiary bridge for this distinction (PNAS 2015 Sall4-Gli3 limb paper; Genetics 2024 "Sall genes regulate hindlimb initiation in mouse embryos," PMC11075541).

**Comparative biology/evolutionary conservation:** The requirement for a Sall1 ortholog in kidney (ureteric bud/nephron progenitor) development is explicitly described as **"conserved over species"** in comparative developmental biology literature (ScienceDirect, "Kidney development conserved over species: essential roles of Sall1"), spanning mouse and Xenopus pronephros induction systems, supporting cross-species conservation of the core SALL1 kidney-developmental mechanism even though disease itself is not naturally observed outside humans.

**Zoonotic potential/transmission:** Not applicable — TBS1 is a non-transmissible, purely genetic developmental disorder.

---

## 15. Model Organisms

**Mouse (primary and best-characterized model):**

- **Conventional Sall1-null (knockout) mice** (Nishinakamura et al. 2001, *Development* 128:3105–3115, PMID:11688560): homozygous null mice die perinatally with **kidney agenesis or severe dysgenesis** due to **failure of ureteric bud invasion/outgrowth** into the metanephric mesenchyme, with mesenchymal apoptosis and failed tubule formation. This establishes SALL1's essential, dosage-graded role in early nephrogenesis and is the mechanistic anchor for the human renal phenotype, though it models **biallelic** loss, which is more severe than (and mechanistically distinct in degree from) the human heterozygous disease state.
- **Sall1 knock-in mouse expressing a truncated protein (Sall1ΔZn2-10 and related alleles)** (Hum Mol Genet 2003, "Expression of a truncated Sall1 transcriptional repressor is responsible for Townes–Brocks syndrome birth defects"): this is the **most disease-relevant model**, as **heterozygous** knock-in mice recapitulate key human TBS features — **high-frequency sensorineural hearing loss, renal cystic hypoplasia, and wrist/limb bone abnormalities** — directly supporting the dominant-negative mechanism, since expressing the truncated protein alone (not simple SALL1 loss) is sufficient to cause the TBS-like phenotype. **Homozygous** truncated-protein mice show a more severe phenotype than Sall1-null homozygotes (complete renal agenesis, exencephaly, limb and anal deformities) — direct genetic evidence that the truncated protein is not behaving as a simple null allele.
- **Sall1TBS mouse model in induced acute kidney injury** (AJP-Renal 2015, doi:10.1152/ajprenal.00222.2015): the same truncated-protein heterozygous model shows **relative protection from ischemia-reperfusion injury and aristolochic-acid-induced nephrotoxicity** compared to wild-type — an unexpected, model-organism-only finding whose translational relevance to human TBS1 kidney-injury susceptibility is undetermined and should be curated as a `HUMAN_MODEL_MISMATCH`-flavored open question rather than assumed to apply to patients.
- **Sall1-GFP knock-in mice** (PMID:15172686) — used to isolate and transcriptionally profile the Sall1-expressing kidney mesenchymal cell population, informing the "molecular profiling" resource base for kidney-branch mechanism (see Section 6).
- **Sall1 in renal stromal progenitors** (Scientific Reports, PMC4625151) — demonstrates a **non-cell-autonomous** role: Sall1 in the renal stromal progenitor compartment restrains excessive nephron progenitor expansion, adding nuance that SALL1's kidney role is not confined to the nephron progenitor/ureteric bud compartments alone.
- **Sall1-NuRD complex interaction and loop-of-Henle formation** (Development 2017) — mechanistic dissection showing Sall1 acts as **both an activator and a repressor** via distinct interactions (including NuRD) to maintain nephron progenitors and enable normal nephron segmentation (loop of Henle formation specifically).
- **Sall1 role in cortical neurogenesis** (PMC3339829, "Sall1 regulates cortical neurogenesis and laminar fate specification in mice: implications for neural abnormalities in Townes-Brocks syndrome") — a mouse-model-derived candidate mechanism for the CNS-related findings (developmental delay, Chiari I malformation) occasionally reported in TBS1 patients; this extends the model's relevance beyond the classic triad+kidney axis but remains model-organism inferential evidence for the human CNS phenotype.
- **Sall1/Sall4 double-mutant mice** (Development 2006) — demonstrate genetic cooperation between the two paralogs in **anorectal, cardiac, brain, and kidney development**, directly relevant to understanding both the TBS1 (SALL1) anorectal/cardiac phenotype and its mechanistic overlap with/distinction from SALL4-related disease.
- **Sall genes and hindlimb initiation** (Genetics 2024, PMC11075541) — T-Cre-mediated Sall1/Sall4 conditional double knockouts fail to initiate hindlimbs at all (loss of Isl1/Pitx1/Tbx4 expression), establishing redundant essential function in limb-field specification broadly, with Sall1 alone (in the heterozygous truncated-protein model above) instead producing the milder, disease-relevant digit-duplication phenotype.

**Phenotype recapitulation and limitations:** The heterozygous truncated-protein knock-in mouse is judged the most **faithful** available model for the core TBS1 features (hearing loss, renal cystic hypoplasia, limb/wrist abnormality), directly supporting the human dominant-negative mechanistic hypothesis. Its principal **limitations** as a human-disease model include: (1) it does not reproduce every human-reported feature (e.g., anorectal/imperforate-anus phenotype recapitulation specifically in the heterozygous model was not confirmed as robust in the sources reviewed here — the anorectal phenotype is better documented in the Sall1/Sall4 double-mutant and homozygous truncated-protein contexts, which are not the direct heterozygous human-genotype equivalent); (2) the unexpected AKI-protective phenotype has no established human correlate and its translational meaning is unresolved; (3) as with any mouse model, species differences in nephron endowment, ear anatomy, and digit number/patterning limit one-to-one extrapolation of severity or timing.

**Other model systems:** No Drosophila, zebrafish, C. elegans, yeast, or human iPSC/organoid model specific to SALL1/TBS1 disease modeling was identified in this search (Drosophila *spalt* is the evolutionary ortholog underlying the gene family's discovery and naming, but was not found here as a disease-modeling platform for TBS1 specifically; Xenopus pronephros work is developmental-biology mechanism research rather than a TBS1 disease model per se). This is a plausible research gap worth flagging rather than asserting resources that were not found.

**Resources:** MGI (Mouse Genome Informatics) is the relevant repository for the Sall1 knockout and knock-in alleles described above; specific IMPC/KOMP allele identifiers were not independently retrieved in this pass and should be looked up directly in MGI before citing a specific allele ID.

Sources: [Nishinakamura 2001 (PMID:11688560)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4625151), [Truncated Sall1 knock-in, HMG 2003](https://academic.oup.com/hmg/article/12/17/2221/692156), [Sall1TBS AKI protection, AJP-Renal 2015](https://journals.physiology.org/doi/full/10.1152/ajprenal.00222.2015), [Sall1-NuRD, Development 2017](https://journals.biologists.com/dev/article/144/17/3080/47975/), [Sall1 cortical neurogenesis, PMC3339829](https://pmc.ncbi.nlm.nih.gov/articles/PMC3339829/), [Sall genes hindlimb initiation, Genetics 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11075541/), [Sall1/Sall4 cooperation, Development 2006](https://journals.biologists.com/dev/article/133/15/3005/43414/)

---

## Summary of Notable Curation Cautions for This Entry

1. **Mechanism is genuinely unsettled between dominant-negative and haploinsufficiency** — GeneReviews itself hedges ("loss of function and possible dominant-negative effect"). Curate `functional_impact_category` reflecting this as the best-supported-but-not-fully-resolved model, and surface (don't silently pick) the competing haploinsufficiency framing, per the dismech evidence-policy discipline on open mechanistic questions.
2. **Renal and auditory phenotypes are progressive/variable-onset, not purely congenital-static** — model `onset`/`clinical_course` qualifiers accordingly and do not code them as fixed congenital-only findings.
3. **Keep TBS1 (SALL1) rigorously separate from TBS2 (DACT1)** and from the SALL4-related Okihiro/Duane-radial-ray spectrum — these are genetically distinct entries with an important differentiating clinical feature (radial hypoplasia present in SALL4-related disease, absent in TBS1).
4. **All prevalence figures are pooled small-case-series/panel-ascertainment estimates**, not population-registry data — cite with appropriate caveats and avoid over-precise point estimates.
5. **The mouse AKI-protection finding is model-organism-only** and should not be represented as a human protective factor without explicit `evidence_source: MODEL_ORGANISM` and directness caveats.
6. Several specific PMIDs above (e.g., Kohlhase 1998 original Nat Genet report, Kiefer 2008 HMG paper's exact identifier beyond the confirmed PMID:18470945, and the HMG 2003 truncated-protein knock-in paper) should have their exact PMIDs independently re-verified via PubMed/`just fetch-reference` before being written into KB evidence items, per the dismech rule that a deep-research or web-search-derived citation is a **lead**, not a checked binding, until fetched and quote-verified through the repository's own reference pipeline.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 19 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 19 |
| On topic | 13 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 59 |
| Resolved | 57 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 24 |
| Terms named correctly | 19 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002251` (3 mentions) - the report calls it "imperforate anus / anal stenosis"; HP calls it **Aganglionic megacolon**
- `UBERON:0004907` (1 mention) - the report calls it "anal canal"; UBERON calls it **lower digestive tract**
- `UBERON:0002544` (1 mention) - the report calls it "thumb"; UBERON calls it **digit**
- `NCIT:C101294` (1 mention) - the report calls it "approx. "Genetic Testing"; NCIT calls it **Whole Genome Sequencing**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005720` (GO_0005720) (1 mention) - replaced by `GO:0000792`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `NCIT:C159273` (1 mention) - the report calls it "Speech Therapy"; NCIT calls it **Speech Language Therapy**