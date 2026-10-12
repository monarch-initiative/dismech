---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-08T14:29:07.901784'
end_time: '2026-10-08T14:35:31.645118'
duration_seconds: 383.74
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Hypertrophic Cardiomyopathy 28
  mondo_id: MONDO:0030317
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
  web_search_requests: 2
  num_turns: 50
  total_cost_usd: 2.8380520999999996
  session_id: d78e6458-537f-42ea-8537-75d16836a4ce
  stop_reason: end_turn
  permission_denials: 5
  denied_tools:
  - Bash
  assistant_text_blocks: 4
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
citation_count: 6
reference_validation:
  total_references: 23
  verified: 23
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 25
  quotes_valid: 24
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:29158260
  relevance_assessed: 23
  on_topic: 22
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 54
  verified: 53
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 3
  labels_matching: 0
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0005045
    reported_labels:
    - HCM in general
    ontology_label: hypertrophic cardiomyopathy
  - term_id: NCIT:C15986
    reported_labels:
    - Verapamil
    - Disopyramide (obstructive HCM)
    - Cardiac myosin inhibitors
    - Antiarrhythmic (AF)
    ontology_label: Pharmacotherapy
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hypertrophic Cardiomyopathy 28
- **MONDO ID:** MONDO:0030317 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hypertrophic Cardiomyopathy 28** covering all of the
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

I'm searching PubMed for the main FHOD3 papers so I can pull exact abstract quotes.

I'm caching the key FHOD3 papers with the repo's fetcher so I can quote their abstracts word for word.

I'm reading the cached abstracts for the mechanism and model papers now. Next I'll check the ontology terms, then write the report.

# Hypertrophic Cardiomyopathy 28 (CMH28; FHOD3-related HCM): research report

**Target:** cardiomyopathy, familial hypertrophic, 28, MONDO:0030317
**Prepared:** 2026-10-08 for the `kb/disorders/Hypertrophic_Cardiomyopathy_28.yaml` entry

**How the evidence was gathered.** I fetched 17 PubMed records into `references_cache/` with `just fetch-reference`. Every quotation below was copied from those cache files or from an existing structured record. A few points come only from web search and are marked **[unverified lead]**; check them before citing.

**Housekeeping:** this run added 17 new `references_cache/PMID_*.md` files. They are untracked in the worktree. One of them, `PMID_30442289.md` (the Pinto & Reckman JACC editorial), came back with no quotable text. Remove it unless a retry with `--force` returns an abstract.

---

## 1. Disease information

**Overview.** CMH28 is autosomal dominant hypertrophic cardiomyopathy caused by heterozygous variants in *FHOD3*. FHOD3 is a formin, a protein that assembles actin filaments, and it organises the sarcomere in heart muscle. FHOD3 is not itself a sarcomere protein; it is one of the main "non-sarcomeric" HCM genes. The disease typically appears in adulthood, penetrance is incomplete, and expression is variable. Most patients have asymmetric septal hypertrophy, and some also have left ventricular hypertrabeculation or noncompaction.

The gene was established by Ochoa et al. 2018, which studied 3,189 HCM probands:
> "FHOD3 is a novel disease gene in hypertrophic cardiomyopathy, accounting for approximately 1% to 2% of cases." (PMID:30442288)

**Identifiers**

| System | ID | Status |
|---|---|---|
| MONDO | MONDO:0030317 "cardiomyopathy, familial hypertrophic, 28" | In the repo cache |
| OMIM | 619402 (CMH28); FHOD3 gene *609691 | 619402 confirmed by web search. 609691 **[unverified lead]** |
| HGNC | `hgnc:26178` FHOD3 | In the repo cache |
| MedGen | 1779612 | **[unverified lead]** (DrugMap record) |
| ICD-10 | I42.1 / I42.2 | Generic HCM codes, not specific to this subtype |
| Orphanet | No FHOD3-specific disorder. It falls under familial isolated HCM | Code not verified |
| Parent MONDO | MONDO:0005045 hypertrophic cardiomyopathy | — |

**Synonyms:** CMH28; FHOD3-related hypertrophic cardiomyopathy; familial hypertrophic cardiomyopathy 28.

**Data provenance.** The knowledge comes from aggregated disease-level resources (OMIM, ClinGen) and from cohort and family studies. No EHR data were used.

---

## 2. Etiology

**Primary cause.** The cause is a heterozygous germline *FHOD3* variant. The variants are mostly non-truncating: missense, in-frame indels, splice-site changes and exon deletions.

**ClinGen.** FHOD3 is classified **Definitive** for HCM:
- Expert panel paper: "Five genes recently reported to cause HCM were curated: RPS6KB1 and RBM20 (limited), KLHL24 and MT-TI (moderate), and FHOD3 (definitive)." (PMID:39971408)
- ClinGen record row: `FHOD3 | HGNC:26178 | hypertrophic cardiomyopathy | MONDO:0005045 | AD | Definitive` (CGGV:assertion_c31027fe-8143-4022-8bbb-867eb1692c51-2023-09-29T160000.000Z)

**Curation caveat:** that ClinGen assertion is filed against MONDO:0005045 (HCM in general), not MONDO:0030317. Under the repo's gene-validity rules it is an `other_disease` case. Record it in `gene_disease_validity` only if the entry carries a MONDO:0005045 `exactMatch` mapping, which would be wrong for a numbered subtype. Otherwise cite it as ordinary evidence, or explain in `notes`.

**Review context (PMID:34526680):**
> "variants in several additional genes (ACTN2, ALPK3, CSRP3, FHOD3, FLNC, JPH2, KLHL24, PLN and TRIM63), encoding non-sarcomeric proteins with diverse functions, have been shown to be disease-causing in a small number of patients."

**Genetic risk and modifier factors**

- **Intermediate-effect allele p.Arg637Gln (PMID:38160043).** This variant was enriched in HCM: "284 of 9668 probands; 2.94%" against "0.58%" in gnomAD controls, an OR of about 5.2. In heterozygotes it "can act as a predisposing factor (intermediate-effect variant) for HCM, with an estimated penetrance of around 1%." Homozygotes are more severe (see Section 9). This makes p.Arg637Gln a `RISK_FACTOR` or `SUSCEPTIBILITY` allele, not a simple Mendelian one.
- **Intermediate-effect variants in general (PMID:40879562).** FHOD3 is among the five non-sarcomeric genes included. Across genes, "IEVs are present in 6.1% of HCM cases and account for 4.8% of HCM genetic burden. IEVs also influence disease severity and outcomes, particularly when combined with monogenic disease-causing variants."
- **Common variants (PMID:23255317).** A GWAS found "an intronic FHOD3 variant (rs516514) associated with HCM (odds ratio, 2.45…)". It also found that the missense variant FHOD3-V1151I (rs2303510) gave "an even stronger association with HCM (P=1.76×10(-9))". These are susceptibility or modifier variants, not CMH28-causing alleles.
- **Possible cosegregating modifiers in one family (PMID:31742804).** "RNF207 (p.Q268P), CCM2 (p. E233K) and SGCZ (p.Q134X) may be related to the clinical heterogeneity of the family." This is weak evidence from a single family.

**Environmental, protective and gene-environment factors.** None is documented specifically for CMH28. A large HCM GWAS (PMID:33495597, not fetched) links diastolic blood pressure mainly to *sarcomere-negative* HCM. That makes hypertension a plausible but **unestablished** modifier for FHOD3 carriers. No protective factors are reported.

---

## 3. Phenotypes

The main quantitative source is the Ochoa 2018 cohort of 70 carriers of (likely) pathogenic variants (PMID:30442288):

> "Of the patients, 82% had asymmetric septal hypertrophy (mean 18.8 ± 5 mm); left ventricular ejection fraction <50% was present in 14% and hypertrabeculation in 16%. Events were rare before age 30 years, with an annual cardiovascular death incidence of 1% during follow-up."

| Phenotype | Suggested HPO term (in repo cache) | Frequency / notes | Evidence |
|---|---|---|---|
| Hypertrophic cardiomyopathy | HP:0001639 Hypertrophic cardiomyopathy | Defining feature, adult onset | PMID:30442288 |
| Asymmetric septal hypertrophy | HP:0001670 Asymmetric septal hypertrophy | 82%; mean thickness 18.8 mm | PMID:30442288 |
| Left ventricular hypertrophy | HP:0001712 Left ventricular hypertrophy | Near-universal among affected carriers | — |
| Hypertrabeculation / LV noncompaction | HP:0030682 Left ventricular noncompaction | 16% hypertrabeculation | PMID:30442288 |
| Noncompaction as the main phenotype | HP:0012817 Noncompaction cardiomyopathy | One family with a splice variant, with "arrhythmic and thrombotic complications, myocardial fibrosis and heart failure" | PMID:35205353 |
| Reduced LVEF / systolic dysfunction | HP:0012664 Reduced left ventricular ejection fraction | 14% have LVEF <50% | PMID:30442288 |
| Myocardial fibrosis | HP:0001685 Myocardial fibrosis | Case-level evidence | PMID:35205353 |
| Thromboembolism | HP:0001907 Thromboembolism | Case-level evidence (LVNC family) | PMID:35205353 |
| Heart failure | HP:0001635 Congestive heart failure | Variable | PMID:35205353; PMID:41540467 (in vitro) |
| Cardiovascular / sudden death | HP:0001645 Sudden cardiac death | About 1%/yr CV death in one cohort. Higher risk for candidate-variant carriers in a Chinese cohort | PMID:30442288; PMID:33586461 |
| Atrial fibrillation | HP:0005110 Atrial fibrillation | From the OMIM summary | **[unverified lead]** — no quotable PMID found |
| Nonsustained VT | HP:0004756 Ventricular tachycardia | From the OMIM summary | **[unverified lead]** |
| Dyspnea | HP:0002094 Dyspnea | OMIM says it is the most common symptom and that more than half of patients are asymptomatic | **[unverified lead]** |
| Mode of inheritance | HP:0000006 Autosomal dominant inheritance; HP:0003828 Variable expressivity; HP:0003581 Adult onset | — | — |

**Mortality in the Chinese cohort (PMID:33586461):**
> "the FHOD3 candidate variant experienced significantly more risk of cardiovascular death and all-cause death (adjusted hazard ratio [HR], 3.71 …"

**Severity and progression:** variable, ranging from asymptomatic to heart failure. The Ochoa cohort's event rates are "similar to those reported in unselected cohorts" (PMID:30442288).

**Quality of life:** no CMH28-specific data (EQ-5D, SF-36 or similar) were found.

---

## 4. Genetic and molecular information

**Gene:** *FHOD3* (formin homology 2 domain containing 3), chromosome 18q12.2 (gene table), `hgnc:26178`.

**Structure and isoforms.** The domains are GBD, DID, coiled-coil, FH1, FH2 and DAD. The heart-enriched long isoform (FHOD3L) includes exon 12. That exon encodes the region that binds cMyBP-C (cardiac myosin-binding protein C) and targets FHOD3 to the sarcomere C-zone (PMID:29686099; PMID:38051749 introduction).

**Variant spectrum and clustering (PMID:30442288):**
> "One-half of the disease-causing variants were clustered in a small conserved coiled-coil domain (amino acids 622 to 655); odds ratio for hypertrophic cardiomyopathy was 21.8 versus disease control subjects"

| Variant | Class | Population / evidence | Reference |
|---|---|---|---|
| Coiled-coil cluster (aa 622–655), e.g. p.Arg637Gln | Missense | Hotspot. p.Arg637Gln is an intermediate-effect, low-penetrance allele | PMID:30442288; PMID:38160043 |
| Deletion of exons 15–16 | CNV (in-frame) | Found in 3 HCM families and 0 controls. "These exons are part of the diaphanous inhibitory domain of FHOD3 protein, considered a cluster of mutations for HCM." | PMID:32335906 |
| c.1646+2T>C (NM_001281740.3) | Splice donor | Balkan founder variant, "arisen 58 generations ago". Present in "16% of probands with a known genetic cause of HCM" in a Slovenian cohort. Onset 4–63 years | PMID:38051749 |
| c.1286+2delT | Splice | Causal by segregation in 4 Chinese patients | PMID:33586461 |
| p.S527del | In-frame deletion | One Chinese family | PMID:31742804 |
| Splice-altering variant | Splice | LVNC family | PMID:35205353 |

**Burden test (PMID:30442288).** Candidate variants were found in 2.32% of HCM probands, against 0.65% of disease controls and 0.76% in gnomAD. Cosegregation in 17 families gave a combined LOD score of 7.92.

**Somatic or germline:** germline.

**Functional consequence.** The functional consequence is **unresolved**, and this is the key open question for curation:
- Pathogenic HCM variants "seem to be restricted to non-truncating variants (missense, splice-site, and in-frame deletions/insertions variants)" and cluster in the DID domain, exon 12 and the coiled-coil (PMID:38051749 introduction, a background statement).
- This pattern argues against simple haploinsufficiency. It is consistent with dominant-negative or altered-regulation (DID/DAD autoinhibition) mechanisms, but that is an inference.
- **Recommendation:** leave `functional_impact_category` unset, or explain in `notes` why it is not set, rather than asserting GAIN_OF_FUNCTION or LOSS_OF_FUNCTION.

**Other phenotypes reported with FHOD3.** LVNC (PMID:35205353). FHOD3 variants have also been reported in dilated cardiomyopathy (PMID:24088304, Arimura 2013; **not fetched**), but the DCM association "remains as yet unproven" (PMID:38051749 introduction).

**Epigenetics and chromosomal abnormalities:** nothing reported. RBM20 and PTBP1 regulate alternative splicing of *FHOD3* (PMID:30468920, **not fetched**). This is relevant to isoform balance but has not been linked to CMH28.

---

## 5. Environmental information

There are no known environmental, lifestyle or infectious causes. General HCM lifestyle advice applies (Section 13). Leave `environmental:` empty, or add a "Left deliberately uncited." waiver only if an exposure is listed.

---

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Heterozygous germline *FHOD3* variant**, most often non-truncating and clustered in the DID or coiled-coil region (aa 622–655, exons 15–16), **leads to** an altered FHOD3 protein.
   *Demonstrated genetically:* PMID:30442288, PMID:32335906.
   *Inferred:* how a coiled-coil or DID change alters protein function has not been shown biochemically for patient alleles.
2. **Normal role of FHOD3L:** it nucleates and, critically, **elongates** actin filaments, and it is recruited to the sarcomere C-zone by cMyBP-C. Its elongation activity is needed for sarcomere formation and contraction.
   *Demonstrated in vitro:* PMID:40663059 ("FHOD3L's elongation activity, but not its nucleation, capping, or bundling activity, is necessary for proper sarcomere formation and contractile function in neonatal rat ventricular myocytes"); PMID:19706596; PMID:29686099.
3. A disturbed FHOD3 function **results in** defective thin-filament (actin) organisation and impaired sarcomere and myofibril maintenance in cardiomyocytes.
   *Demonstrated for loss of FHOD3 (knockdown or knockout), not for patient alleles:* "RNA interference-mediated depletion of Fhod3 results in a marked reduction in filamentous actin and disruption of the sarcomeric structure" (PMID:19706596). In FHOD3-/- human embryonic stem cell–derived cardiomyocytes, "marked sarcomere disorganization and degradation, impaired calcium handling and compromised mitochondrial function, ultimately leading to reduced contractility" (PMID:41540467).
   - **Branch A (mislocalisation, dominant effect):** wrongly placed FHOD3 is harmful. In cMyBP-C-null mice, "Fhod3 has a deleterious effect on cardiac function under cMyBP-C-null conditions where Fhod3 is aberrantly mislocalized" (PMID:29686099). This is a mouse model and *inferred* to apply to CMH28.
   - **Branch B (deficiency):** loss of FHOD3 activates CaMKII. "FHOD3 deficiency triggered the phosphorylation of CaMKII (Thr286), a key regulator of cardiac hypertrophy and remodeling" (PMID:41540467). This is a knockout model; patient variants are mostly non-truncating.
4. Sarcomere dysfunction and stress signalling **lead to** a maladaptive hypertrophic response of cardiomyocytes, with fetal gene reactivation.
   *Model evidence:* in adult Fhod3-deleted mice, phenylephrine "induced expression of fetal cardiac genes that was more pronounced … suggesting that Fhod3 modulates hypertrophic changes in the adult heart" (PMID:29158260). The step from this to human septal hypertrophy is *inferred*.
5. Cardiomyocyte hypertrophy **results in** left ventricular and asymmetric septal hypertrophy (82%). Disturbed myocardial development or maintenance may account for hypertrabeculation or LVNC (16%).
   *Clinical:* PMID:30442288.
   *Link to trabeculation:* Fhod3-/- embryos show aborted "chamber formation and myocardial development with trabeculation" (PMID:23213483). This is a developmental knockout; the link to adult hypertrabeculation is *inferred*.
6. Downstream, myocardial fibrosis, systolic dysfunction (14% LVEF <50%), arrhythmia and thromboembolism **lead to** heart failure and cardiovascular or sudden death (about 1%/yr).
   *Sources:* PMID:30442288; PMID:35205353; PMID:33586461.

### Suggested ontology terms

All of these are in the repo caches.

- **GO biological process:** GO:0045214 sarcomere organization; GO:0055003 cardiac myofibril assembly; GO:0030239 myofibril assembly; GO:0030041 actin filament polymerization; GO:0045010 actin nucleation; GO:0003300 cardiac muscle hypertrophy; GO:0014898 cardiac muscle hypertrophy in response to stress; GO:0060048 cardiac muscle contraction; GO:0055117 regulation of cardiac muscle contraction; GO:0048738 cardiac muscle tissue development.
- **GO cellular component:** GO:0030017 sarcomere; GO:0031672 A band (the C-zone sits within it); GO:0005884 actin filament; GO:0030016 myofibril.
- **Cell types:** CL:0000746 cardiac muscle cell; CL:0002131 regular ventricular cardiac myocyte; CL:0002548 fibroblast of cardiac tissue (for the fibrosis node).

**Scale tags:** steps 1–2 are MOLECULAR, 3 is CELLULAR, 4–5 are TISSUE, and 6 is ORGANISM.

**Molecular profiling.** The only omics data are bulk transcriptomics of FHOD3-KO human cardiomyocytes, which showed "significant downregulation of sarcomere-related genes and calcium-handling genes" (PMID:41540467). FHOD3 expression "is increased in the setting of HCM" in myectomy tissue (PMID:23255317). No single-cell, spatial, proteomic or metabolomic data specific to CMH28 were found.

**Reproducibility caveat.** `PMID_23213483.md` caches the full-text body without a separate abstract block. Quotes from its "Here we show…" introduction paragraph are the authors' own results, so record `quote_role: PRIMARY_RESULT`.

---

## 7. Anatomical structures affected

- **Organ:** heart (UBERON:0000948). Cardiovascular system only; there are no reported extracardiac features.
- **Sites:** interventricular septum (UBERON:0002094; asymmetric septal hypertrophy), heart left ventricle (UBERON:0002084), myocardium (UBERON:0002349), cardiac muscle tissue (UBERON:0001133).
- **Cells:** ventricular cardiomyocytes. FHOD3L is "predominantly expressed in striated muscle" (PMID:40663059).
- **Subcellular:** sarcomere C-zone in the A band, and actin thin filaments. Fhod3 also localises near the M-line (PMID:22509354).
- **Lateralisation:** asymmetric, septum-predominant hypertrophy.

---

## 8. Temporal development

- **Onset:** mainly adult. Carriers "were diagnosed after age 30 years (mean 46.1 ± 18.7 years)" (PMID:30442288). The Balkan founder variant shows "a wide range of ages at onset of the disease (4-63 years)" (PMID:38051749). Homozygous p.Arg637Gln gives "an early presentation" (PMID:38160043).
- **Course:** chronic and lifelong, insidious, and slowly progressive. "Events were rare before age 30 years" (PMID:30442288).
- **Stages:** the generic HCM progression applies (preclinical carrier → hypertrophy → possible systolic dysfunction or heart failure). No CMH28-specific staging exists.
- **Remission:** none.
- **Window for intervention:** before age 30, when cascade screening of relatives can identify carriers before events.

---

## 9. Inheritance and population

- **Inheritance:** autosomal dominant (ClinGen AD Definitive). Incomplete penetrance is noted repeatedly (PMID:38051749). Expressivity is variable.
- **Biallelic dosage effect:** homozygous p.Arg637Gln causes more severe disease. "Seven homozygous carriers of p.Arg637Gln in FHOD3 were identified. All but one (unaffected) showed an early presentation and a severe HCM phenotype." (PMID:38160043) This suggests semidominant behaviour for that allele. **Do not** encode it as recessive inheritance.
- **Frequency within HCM:** about 1–2% of HCM cases (PMID:30442288). Background HCM prevalence is "∼1 in 500" (PMID:39971408). That implies a CMH28 prevalence of roughly 1–4 per 100,000. This is **derived, not measured**; do not record it as a sourced `rate_per_100000`.
- **Founder effects:** Balkan c.1646+2T>C (PMID:38051749). The Iberian cohorts carry p.Arg637Gln at 2.94% of probands (PMID:38160043).
- **Sex ratio:** "two-thirds (66%) were males" (PMID:30442288).
- **Ancestry:** cohorts from Spain/UK, China (3.3% of HCM vs 1.6% of controls; PMID:33586461), the Balkans and Russia.
- **Not reported:** consanguinity, anticipation and germline mosaicism.

---

## 10. Diagnostics

- **Imaging:** echocardiography and cardiac MRI showing LV wall thickness ≥15 mm, which is the standard HCM criterion (PMID:38051749 introduction). CMR also assesses hypertrabeculation or LVNC and fibrosis (late gadolinium enhancement).
- **ECG and Holter:** for AF, NSVT and T-wave abnormalities (NCIT:C38053 Electrocardiography).
- **Genetic testing:** a multigene HCM panel that **includes FHOD3**. "The FHOD3 gene should be routinely included in hypertrophic cardiomyopathy genetic testing panels." (PMID:30442288)
- **CNV analysis is required:** "This study highlights the importance of performing CNV analysis systematically in NGS genetic testing panels for HCM" (PMID:32335906).
- **Exome or genome sequencing** is useful for panel-negative cases (PMID:31742804; PMID:33586461).
- **Variant interpretation:** pay attention to intermediate-effect alleles such as p.Arg637Gln. "Evaluation of IEVs should be considered when HCM genetic testing is performed." (PMID:40879562)
- **Not applicable:** karyotype, FISH, mtDNA testing and repeat-expansion testing.
- **Biomarkers:** none specific to CMH28. Generic HCM markers are NT-proBNP and high-sensitivity troponin. A troponin I GWAS hit near FHOD3 (PMID:33961016) is not established as diagnostic.
- **Differential diagnosis:**
  - sarcomeric HCM (MYH7, MYBPC3 and others)
  - other non-sarcomeric HCM (ALPK3, FLNC, TRIM63, CSRP3)
  - phenocopies: Fabry disease, PRKAG2, Danon disease, transthyretin amyloidosis, RASopathies
  - isolated LVNC
  - hypertensive heart disease
  - athlete's heart
- **Screening:** cascade genetic and clinical screening of first-degree relatives. No newborn screening exists.

---

## 11. Outcome and prognosis

- **Mortality:** annual cardiovascular death incidence of 1% (PMID:30442288). In a Chinese cohort, FHOD3 candidate variants were "an independent risk for cardiovascular death and all-cause death in HCM" (PMID:33586461). In contrast, the Balkan founder carriers had "No adverse cardiac events" (PMID:38051749). The literature conflicts here, so record both.
- **Prognostic modifiers:** an intermediate-effect variant added to a monogenic variant gives a more aggressive course. Major adverse cardiac event–free survival at 70 years was 93.3% vs 69.3% (PMID:40879562; this is a pooled finding across genes). Homozygosity for p.Arg637Gln also worsens prognosis (PMID:38160043).
- **Complications:** heart failure, systolic dysfunction, arrhythmia, thromboembolism (LVNC) and sudden death.
- **Not found:** CMH28-specific survival curves and quality-of-life data.

---

## 12. Treatment

No FHOD3-specific therapy exists, so management follows HCM guidelines. Suggested bindings, all in the repo caches:

| Treatment | `treatment_term` | `therapeutic_agent` | Modality |
|---|---|---|---|
| Beta-blockers (e.g. metoprolol) | NCIT:C15986 Pharmacotherapy | CHEBI:35530 beta-adrenergic antagonist; CHEBI:6904 metoprolol | SMALL_MOLECULE |
| Verapamil | NCIT:C15986 | CHEBI:9948 verapamil | SMALL_MOLECULE |
| Disopyramide (obstructive HCM) | NCIT:C15986 | CHEBI:4657 disopyramide | SMALL_MOLECULE |
| Cardiac myosin inhibitors | NCIT:C15986 | CHEBI:756998 mavacamten; CHEBI:747213 aficamten | SMALL_MOLECULE |
| Antiarrhythmic (AF) | NCIT:C15986 | CHEBI:2663 amiodarone | SMALL_MOLECULE |
| ICD for sudden-death prevention | NCIT:C80435 Implantable Cardioverter-Defibrillator Placement | — | DEVICE |
| Septal myectomy / alcohol septal ablation | No NCIT term verified; bind NCIT:C15329 Surgical Procedure only after a lookup | — | SURGERY |
| Heart transplantation (end-stage) | NCIT:C15246 Heart Transplantation | — | SURGERY |
| Genetic counselling | NCIT:C15240 Genetic Counseling | — | OTHER |

**Caveat on myosin inhibitors.** Their trials enrolled obstructive HCM regardless of genotype. There are no FHOD3-stratified efficacy data.

**Experimental.** The only FHOD3-specific therapeutic signal is in vitro. In FHOD3-KO human cardiomyocytes, "Treatment with the myosin activator Omecamtiv mecarbil (OM) partially restored contractility without affecting calcium handling" (PMID:41540467). This is IN_VITRO evidence, based on a loss-of-function model and not on patient alleles. It is a hypothesis, not a treatment. I found no CMH28 trials, gene therapy or RNA-based programmes.

**Pharmacogenomics:** mavacamten dosing depends on CYP2C19 genotype (generic, not FHOD3-specific) **[unverified lead; source it before use]**.

---

## 13. Prevention

- **Primary:** none is possible. Genetic counselling covers the 50% transmission risk, and preimplantation or prenatal testing is possible when a pathogenic variant is known. Incomplete penetrance complicates counselling.
- **Secondary:** cascade genotyping of relatives followed by serial echocardiography and ECG of carriers.
- **Tertiary:** sudden-death risk stratification and ICD; anticoagulation for AF or LVNC thrombus; managing hypertension as a possible modifier (inferred).
- **Not applicable:** immunisation and public-health or environmental measures.

---

## 14. Other species and natural disease

- **Naturally occurring FHOD3 cardiomyopathy:** none found in OMIA during this search. Feline and canine HCM are mainly MYBPC3-associated.
- **Orthologues:** mouse *Fhod3*, rat *Fhod3*, and *Drosophila* **fhos**. "its fly homolog fhos is required for normal adult heart systolic contraction" (PMID:23255317).
- **Zebrafish:** *fhod3* paralogues are involved in skeletal myofibril stability (PMID:41416849, not fetched).
- **Not verified:** NCBI Gene IDs for the orthologues.

---

## 15. Model organisms and systems

| Model | Type | Recapitulation | Key quote | Ref |
|---|---|---|---|---|
| Fhod3-/- mouse | Germline knockout | Embryonic lethal. Fails to recapitulate adult HCM | "knock out of the Fhod3 gene in mice confers lethality by embryonic day (E) 11.5"; trabeculation and chamber formation "aborted" | PMID:23213483 |
| Perinatal cardiac Fhod3 cKO mouse | Conditional knockout | Juvenile cardiomegaly | "juvenile lethality at around day 10 after birth with enlarged hearts composed of severely impaired myofibrils" | PMID:29158260 |
| Adult inducible cardiac Fhod3 cKO mouse | Tamoxifen-induced cKO | Partial: "slight cardiomegaly and mild impairment of cardiac function"; exaggerated fetal gene response to phenylephrine | — | PMID:29158260 |
| α-MHC Fhod3 transgenic, I1127A mutant | Transgenic overexpression | Mutant that cannot assemble actin; the paper reports cardiomyopathic changes | — | PMID:23213483 |
| cMyBP-C-null × Fhod3 dosage mouse | Compound genetic | Fhod3 overexpression exacerbates HCM; reducing it partially ameliorates | — | PMID:29686099 |
| FHOD3-/- human ESC-derived cardiomyocytes | iPSC/ESC, CRISPR | Sarcomere disorganisation, Ca²⁺ handling defect, CaMKII activation | — | PMID:41540467 |
| Neonatal rat ventricular myocytes with function-separating FHOD3L mutants | In vitro | Shows that elongation activity is the required function | — | PMID:40663059 |
| Drosophila *fhos* | Invertebrate | Systolic dysfunction | — | PMID:23255317 |

**Limitations.** Every in vivo model is a knockout or overexpression model. No knock-in of a patient allele exists, for example a coiled-coil missense variant, p.Arg637Gln, or the exon 15–16 deletion. A complete knockout is embryonic lethal, while the human disease is heterozygous, non-truncating and adult-onset.

This is a good candidate for a `HUMAN_MODEL_MISMATCH` discussion: the models remove or overexpress FHOD3, whereas patients carry heterozygous non-truncating alleles. The proposed experiment is a patient-allele knock-in in mice or iPSC-derived cardiomyocytes.

**Model divergence typing** for `modeled_mechanisms`:
- `BOUNDARY_OMISSION` — no patient allele is modelled.
- `PROXY_QUANTITY` — knockout loss stands in for altered function of a variant protein.
- `SPECIES_MISMATCH` — mouse and rat models.

---

## Curation notes for the entry

1. **Fill in the stub fields.** The existing draft has a one-line description and a single phenotype. The evidence above supports roughly 6–7 pathophysiology nodes, about 10 phenotypes with frequencies, 3–5 genetic rows and the treatments in Section 12.
2. **Do not write `functional_impact_category`** for the causal alleles, because the mechanism is unresolved. Record that reasoning in `notes`.
3. **Model p.Arg637Gln** as a separate `genetic` row with `relationship_type: RISK_FACTOR`, plus a homozygous-severity note.
4. **ClinGen:** the Definitive tier is against MONDO:0005045, so use it as evidence rather than as a `gene_disease_validity` assertion for this entry (see Section 2).
5. **Unverified leads:** the AF, NSVT and dyspnoea frequencies come only from the OMIM/MalaCards text. They need an exact quotable source before they go into the entry. A GeneReviews chapter specific to FHOD3 is unlikely; run `just check-genereviews` to confirm.

---

### Sources (all PMIDs cached in `references_cache/` unless marked)
- PMID:30442288 Ochoa 2018 JACC
- PMID:39971408 Hespe 2025 JACC (ClinGen)
- CGGV:assertion_c31027fe-… (ClinGen FHOD3/HCM Definitive)
- PMID:34526680 Walsh 2022 Nat Rev Cardiol
- PMID:38160043 Piqueras-Flores 2024 J Med Genet
- PMID:40879562 García Hernández 2025 Circulation
- PMID:32335906 Ochoa 2020 Clin Genet
- PMID:38051749 Vodnjov 2023 PLoS One
- PMID:33586461 Wu 2021 JAHA
- PMID:31742804 Huang 2020 J Gene Med
- PMID:35205353 Myasnikov 2022 Genes
- PMID:23255317 Wooten 2013 Circ Cardiovasc Genet
- PMID:19706596 Taniguchi 2009 JBC
- PMID:23213483 Kan-o 2012 Biol Open
- PMID:22509354 Kan-o 2012 PLoS One
- PMID:29158260 Ushijima 2018 JBC
- PMID:29686099 Matsuyama 2018 PNAS
- PMID:40663059 Valencia 2025 eLife
- PMID:41540467 Wei 2026 Stem Cell Res Ther
- **Not fetched:** PMID:24088304, PMID:30468920, PMID:33495597, PMID:33961016, PMID:41416849
- Web: [PubMed 30442288](https://pubmed.ncbi.nlm.nih.gov/30442288/), [MalaCards CMH28](https://malacards.org/card/cardiomyopathy_familial_hypertrophic_28), [DrugMap DISIHJ7B](https://drugmap.idrblab.net/data/disease/details/DISIHJ7B), [Gene Table ref 30442288](https://musclegenetable.fr/4DACTION/disease_cherche_ref/1205_30442288), [Mayo Clinic Wooten 2013](https://mayoclinic.elsevierpure.com/en/publications/formin-homology-2-domain-containing-3-variants-associated-with-hy), [UCL Discovery](https://discovery.ucl.ac.uk/id/eprint/10062000/)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 23 |
| Resolved | 23 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 25 |
| Quoted claims found in source | 24 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 23 |
| On topic | 22 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMID:29158260`: "induced expression of fetal cardiac genes that was more pronounced … suggesting that Fhod3 modulates hypertrophic changes in the adult heart"
  - closest text in source: "In addition to these age-related changes, systemic stimulation with the α1-adrenergic receptor agonist phenylephrine, which induces sustained hypertension and hypertrophy development, induced expression of fetal cardiac genes that was more pronounced in adult Fhod3-deleted mice than in the control mice, suggesting that Fhod3 modulates hypertrophic changes in the adult heart"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 54 |
| Resolved | 53 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 3 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0005045` (5 mentions) - the report calls it "HCM in general"; MONDO calls it **hypertrophic cardiomyopathy**
- `NCIT:C15986` (5 mentions) - the report calls it "Verapamil", "Disopyramide (obstructive HCM)", "Cardiac myosin inhibitors", "Antiarrhythmic (AF)"; NCIT calls it **Pharmacotherapy**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0000948` (1 mention) - the report calls it "Organ:** heart"; UBERON calls it **heart**, and lists "branchial heart" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `NCIT:C15986` - called "Verapamil", "Disopyramide (obstructive HCM)", "Cardiac myosin inhibitors", "Antiarrhythmic (AF)"