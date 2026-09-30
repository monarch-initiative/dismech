---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5-5
cached: false
start_time: '2026-09-25T20:39:46.602970'
end_time: '2026-09-25T20:44:11.523234'
duration_seconds: 264.92
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Hypomyelinating Leukodystrophy 14
  mondo_id: MONDO:0033486
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
  - claude-opus-5-5
  web_search_requests: 4
  num_turns: 30
  total_cost_usd: 3.2644936000000007
  session_id: 373d33b9-9499-4351-9ceb-ed0756aa74c2
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  assistant_text_blocks: 3
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
citation_count: 11
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 27
  quotes_valid: 26
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:27545674
  relevance_assessed: 16
  on_topic: 10
  needs_review: true
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 75
  verified: 74
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 27
  labels_matching: 18
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: DOID:0080296
    reported_labels:
    - DOID
    ontology_label: hypomyelinating leukodystrophy 14
  - term_id: HP:0001332
    reported_labels:
    - Dystonia, extrapyramidal signs
    ontology_label: Dystonia
  - term_id: CL:1001474
    reported_labels:
    - striatum; inferred from caudate/putamen atrophy
    ontology_label: medium spiny neuron
  - term_id: UBERON:0000955
    reported_labels:
    - Primary organ:** brain
    ontology_label: brain
  labels_variant: 5
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hypomyelinating Leukodystrophy 14
- **MONDO ID:** MONDO:0033486 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hypomyelinating Leukodystrophy 14** covering all of the
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

I've read the ten cached references for HLD14. Next I'm confirming identifiers and the mouse-model papers online, then I'll write the report.

Term lookups are done. Last, I'm checking the NCIT treatment and CHEBI drug IDs in the local caches before writing.

# Hypomyelinating Leukodystrophy 14 (HLD14; UFM1-related H-ABC): research report

**Prepared:** 2026-09-25, for the dismech entry `kb/disorders/Hypomyelinating_Leukodystrophy_14.yaml`. Most quotes come from the cached references in `references_cache/`, which are PubMed abstracts or PMC full texts. The rest come from database pages, and those sources are named where used.

**Sources.** Ten PubMed/PMC items were read in full or as abstracts: PMID:28931644, 29868776, 34573312, 35189806, 39470296, 39846712, 41731076, 42195294, 30626644 and 40315331. Web lookups covered MONDO (via OLS), HGNC REST, Orphanet, ClinicalTrials.gov and PubMed.

**How identifiers were checked.** Every ontology CURIE below was read from a lookup, never written from memory. Most came from the repo caches (`cache/hp`, `cl`, `go`, `uberon`, `ncit`, `chebi`). UFM1 and UFC1 came from the HGNC REST API, and the MONDO cross-references from OLS. A term marked **[lookup needed]** had no cached match and has not been verified; it must be searched before it is bound.

---

## Summary of evidence limits

1. **The oligodendrocyte defect is inferred.** In the only functional test of the founder promoter deletion, the variant reduced promoter activity in neuroblastoma and astroglioma cells. It did **not** reduce it in the oligodendrocytoma line (PMID:28931644). No study has measured UFM1 or UFMylation in patient oligodendrocytes, or in patient cells carrying the promoter deletion.
2. **No human neuropathology exists** for UFM1-related disease.
3. **Studies disagree on ER stress.** Overexpressing UFM1 p.R81C in cell lines did not change ER-stress markers (PMID:29868776). UFM1-knockout mouse neurons do activate the PERK arm of the unfolded protein response (PMID:41731076).
4. **One paper assigns a UFC1 variant to "HLD14".** PMID:39846712 describes UFC1 p.Arg23Gln as "HLD14-related". OMIM 617899 is the UFM1 disorder; the UFC1 disease is a separate entry. Treat that paper as evidence about the shared pathway, not as evidence on HLD14 itself.
5. **It is unconfirmed whether the R81C missense patients are HLD14.** The p.Arg81Cys cases (PMID:29868776) had no basal-ganglia abnormality (0/4) but did have delayed myelination (3/4). Before merging them into the entry, check whether OMIM 617899 lists them. A `has_subtypes` split, or a note, may be the better fit.

---

## 1. Disease information

**Overview.** HLD14 is an autosomal recessive, infantile-onset hypomyelinating leukodystrophy caused by biallelic *UFM1* variants. UFM1 is the ubiquitin-like modifier of the UFMylation pathway. Almost all reported patients are homozygous for a 3-bp deletion in the *UFM1* promoter, a founder variant in the Roma population. On MRI the disease meets the criteria for **hypomyelination with atrophy of the basal ganglia and cerebellum (H-ABC)**, and patients sit at the most severe end of that spectrum.

> "Sixteen patients from 14 families from different countries fulfilling the MRI criteria for H-ABC exhibited a similar, severe clinical phenotype, including lack of development and a severe epileptic encephalopathy." (PMID:28931644)

> "Hypomyelinating leukodystrophy type 14 (MIM # 617899) is caused by mutations in the UFM1 gene and is inherited in an autosomal recessive manner. It is characterized by hypotonia, an almost complete lack of motor or cognitive skills, absent language development, spasticity, and intractable seizures." (PMID:34573312)

**Identifiers**

| Resource | ID | Source / note |
|---|---|---|
| MONDO | MONDO:0033486 "leukodystrophy, hypomyelinating, 14" | OLS |
| OMIM | 617899 | MONDO xref |
| DOID | DOID:0080296 | MONDO xref |
| UMLS / MedGen | C4693535 / 1635255 | MONDO xref |
| GARD | 0016266 | MONDO xref |
| Orphanet | ORPHA:139441, *Hypomyelination with atrophy of basal ganglia and cerebellum* | Covers **both** TUBB4A and UFM1 forms, so it is broader than HLD14. Map as `skos:broadMatch`, not exactMatch. |
| ICD-10/ICD-11, MeSH | No disease-specific code found | MeSH indexing uses "Hereditary Central Nervous System Demyelinating Diseases" |
| GeneReviews | **No UFM1 chapter** | Checked against the offline Bookshelf index (`cache/bookshelf/genereviews.csv`). The only related chapter is *TUBB4A-Related Neurologic Disorders* (NBK395611, PMID:27809427), which does not cover UFM1. |

**Synonyms:** HLD14; UFM1-related H-ABC; recessive H-ABC (Hamilton et al. title: "recessive variant of H-ABC"); leukodystrophy, hypomyelinating, 14.

**Data provenance:** aggregated case series and cohorts. There are no EHR-derived data.

---

## 2. Etiology

- **Cause.** Biallelic hypomorphic variants in *UFM1* (hgnc:20597; 13q13.3; OMIM gene 610553). The disease is monogenic.
- **Genetic risk.**
  - Roma ancestry, which carries the founder allele.
  - Parental consanguinity or endogamy: "Parental consanguinity was reported in 7 families and 2 families were related" (PMID:28931644).
- **Environmental risk factors:** none described.
- **Protective factors:** none described. No modifier genes have been reported.
- **Gene–environment interaction:** none described.

## 3. Phenotypes

Onset is early infantile, with medical attention drawn between the neonatal period and about 6 months. Across all cohorts the course is progressive and usually fatal in infancy or early childhood.

**Frequency sources.** Hamilton 2017 (n=16; frequencies from Nahorski 2018 Table 2), Szűcs 2021 (n=4), Ivanov 2023 (n=9) and Drobňaková 2026 (n=17). Drobňaková states that "All patients presented with" its listed signs.

| Phenotype | HPO term (cache-verified) | Frequency / notes | Key PMID |
|---|---|---|---|
| Global developmental delay, profound | HP:0012736 Profound global developmental delay (parent HP:0001263) | 100% (16/16; 4/4). "typically without intentional movements and language development" | 28931644, 34573312 |
| Absent speech | HP:0001344 | Universal in Hamilton | 28931644 |
| CNS hypomyelination | HP:0003429 CNS hypomyelination | 16/16. Szűcs reports "Delayed/absent myelination" in 4/4; Ivanov reports "reduced myelination" in 6/6 | 28931644, 34573312, 35189806 |
| Small or absent putamen | HP:0031982 Abnormal putamen morphology | MRI criterion: "None of the patients showed a normal putamen" | 28931644 |
| Caudate atrophy with high T2 signal in the lateral caudate head | HP:0002340 Caudate atrophy | 16/16. Proposed as "pathognomonic for UFM1-related H-ABC" | 28931644 |
| Cerebellar atrophy (vermis) | HP:0001272 | 56% on the first MRI; 81% overall (13/16); 4/4 in Szűcs | 28931644, 29868776, 34573312 |
| Cerebral atrophy | HP:0002059 | Progressive; 7/9 in Ivanov (cortical); 4/4 in Szűcs | 35189806, 34573312 |
| Thin corpus callosum | HP:0033725 | Corpus callosum atrophy 3/6 | 35189806 |
| Microcephaly, postnatal and progressive | HP:0000253 Progressive microcephaly | 16/16; 6/9; 3/4; most of 17. Head size is normal at birth | 28931644, 35189806, 34573312, 42195294 |
| Seizures / epilepsy | HP:0001250; drug-resistant epilepsy **[lookup needed]** | 75% (12/16), and in all patients ≥18 months; West syndrome reported. **Lower elsewhere:** 4/9 in Ivanov, 1/4 in Szűcs | 28931644, 35189806, 34573312 |
| Infantile spasms / hypsarrhythmia | HP:0012469 / HP:0002521 | West syndrome in Hamilton | 28931644 |
| Non-epileptic tonic spells; EEG abnormality | HP:0002353 EEG abnormality | 4/4 had diffuse cortical dysfunction on EEG | 34573312 |
| Inspiratory stridor (laryngeal) | HP:0005348 Inspiratory stridor | 9/9 in Ivanov; 3/4 in Szűcs; "All patients" in the 17-patient cohort. Attributed to impaired laryngeal innervation or tone | 35189806, 34573312, 42195294 |
| Axial hypotonia | HP:0008936 | 4/9; 3/4; all 17 | 35189806, 34573312, 42195294 |
| Spasticity / spastic tetraparesis | HP:0001285 Spastic tetraparesis | "Almost all" in Hamilton; 9/9 hypertonia in Ivanov; 4/4; all 17 | 28931644, 35189806, 42195294 |
| Dystonia, extrapyramidal signs | HP:0001332 | "mostly dystonia"; dystonic posturing in 5/9 | 28931644, 35189806 |
| Opisthotonus | HP:0002179 | 6/9 | 35189806 |
| Pseudobulbar signs | HP:0002200 | All 17 in Drobňaková | 42195294 |
| Dysphagia and feeding difficulty (tube feeding) | HP:0002015 / HP:0011968 | 7/9; 3/4 | 35189806, 34573312 |
| Bradypnea, apnea, abnormal breathing pattern | bradypnea **[lookup needed]**; HP:0002104 Apnea; HP:0002793 Abnormal pattern of respiration | Bradypnea 5/9 and 3/4; apnea 2/9 | 35189806, 34573312 |
| Respiratory insufficiency | HP:0002093 | The most common cause of death; 6/16 needed tracheostomy | 28931644 |
| Visual impairment | HP:0000505 | "Vision and hearing were never achieved or lost by 4-8 mo"; hypoplastic optic nerves in one case | 35189806, 34573312 |
| Hearing impairment | HP:0000365 (HP:0000407 if sensorineural is confirmed) | Ivanov: severe. Szűcs: absent brainstem auditory evoked responses in one case | 35189806, 34573312 |
| Nystagmoid eye movements | HP:0000639 Nystagmus | 6/9; horizontal nystagmus in 3/17 | 35189806, 42195294 |
| Failure to thrive | HP:0001508 | 63% (10/16); 3/4 | 29868776, 34573312 |
| Short stature | HP:0004322 | 75% (12/16); 2/4 | 29868776, 34573312 |
| Developmental regression | HP:0002376 | "absent or minimal with subsequent regression after 2-5 mo"; 4/4 | 35189806, 34573312 |
| Death in infancy | HP:0001522 | See section 11 | 28931644, 42195294 |

**Quality of life.** No EQ-5D, SF-36 or PROMIS data have been published. Patients are totally dependent, many with a tracheostomy, gastrostomy or ventilation.

**CSF.** One Szűcs patient had low CSF protein (138 mg/L). This is a single observation and should not be curated as a phenotype.

## 4. Genetic and molecular information

**Causal gene:** *UFM1* (hgnc:20597; Entrez 51569; ENSG00000120686; UniProt P61960). The protein is a 9.1-kDa type I ubiquitin-like modifier.

**Pathogenic variants**

| Variant | Type | Zygosity / population | Evidence |
|---|---|---|---|
| **c.-273_-271delTCA** (NM_001286704.1) = **c.-155_-153delTCA** (NM_016617.4); GRCh38 chr13:38349765–38349767 del; rs747359907; ClinVar VCV 495149; HGMD CD1715768 | 3-bp promoter (5′ regulatory) deletion; hypomorphic | Homozygous; Roma founder haplotype. Also found in Pakistani and Indian patients | PMID:28931644, 34573312, 39470296 |
| **c.241C>T p.(Arg81Cys)** (NM_016617.3) | Missense in the C-terminal tail that binds UBA5; hypomorphic | Homozygous; two Sudanese families from one village sharing an ancestral haplotype | PMID:29868776 |

- **The two transcript numberings name the same variant.** Szűcs states that the NM_016617.4 c.-155_-153delTCA was "reported as NM_001286704.1: c.-273_-271delTCA" (PMID:34573312). Pick one form for the KB and give the other in `notes`.
- **Classification.**
  - Szűcs 2021 called it likely pathogenic under ACMG.
  - Kaur 2025 classified it "P (PS3, PS4_M, PM2, PP5)" (PMID:39470296).
  - Drobňaková 2026 reports it as pathogenic in ClinVar. Confirm the current ClinVar status before citing.
- **Population frequency.** Absent from gnomAD (PMID:34573312). Among Roma: "Screening of 670 Roma controls revealed 30 carriers with an overall carrier rate of 4.5% ... An additional panel of Eastern Slovak Roma samples revealed a carrier frequency of 3.3% (9 out of 273) ... a carrier rate of approximately 25% (14 out of 57 individuals)" in one endogamous community (PMID:28931644).
- **Linkage.** "LOD score calculations for the UFM1 variant showed a maximum LOD score of 9.18" (PMID:28931644).
- **Functional consequence.** Both variants are partial loss of function (hypomorphic).
  - "Our results show a reduction rather than abrogation of ufmylation with the activity of UFM1 and UFC1 mutants at 60–75% of their wild-type counterparts" (PMID:29868776).
  - R81C may also have non-loss-of-function effects: "UFM1-deficient and UFM1-R81C-expressing neurons display distinct responses to ER stress, indicating that UFM1-R81C is not merely a loss-of-function variant" (PMID:41731076).
  - Suggested `functional_impact_category`: `PARTIAL_LOSS_OF_FUNCTION` for both; `variant_origin: GERMLINE`; `zygosity`: homozygous.
- **Biallelic null variants are depleted.** "the conspicuous depletion of biallelic null mutations in the components of this pathway in human genome databases suggest that it is necessary for embryonic survival" (PMID:29868776).
- **Modifier genes, epigenetics, chromosomal abnormalities:** none reported.
- **Other genes in the same pathway** (differential diagnosis, not HLD14): *UBA5* (E1; hgnc:23230) and *UFC1* (E2; hgnc:26941). They give overlapping encephalopathies (PMID:29868776). *TUBB4A* (hgnc:20774) causes dominant H-ABC, which is HLD6.

## 5. Environmental information

No environmental, lifestyle or infectious contributors are described. This section is not applicable.

## 6. Mechanism and pathophysiology

### Causal chain

1. A **homozygous *UFM1* promoter deletion** (or the R81C missense variant) **leads to reduced UFM1 function**. The deletion reduces *UFM1* transcription, measured in neural cell lines only: "The deletion significantly reduced promoter activity in SY-5Y and U373 but not in HeLa and HOG-F2 cell lines" (PMID:28931644). R81C instead weakens UFM1's binding to UBA5 and its thioester transfer to UFC1 (PMID:29868776).
   - *Caveat:* HOG-F2 is the oligodendroglial line, so a neuron- or astrocyte-selective effect is what was shown. Reduced UFM1 in patient tissue has **not** been measured for the promoter variant.
2. Reduced UFM1 **results in reduced protein UFMylation** (GO:0071569 protein ufmylation, DECREASED). This was shown for R81C in patient lymphoblasts: "the level of two UFM1-conjugates with cellular proteins in patient-derived lymphoblasts was significantly reduced" (PMID:29868776). For the promoter variant it is inferred.
3. Reduced UFMylation **leads to loss of ribosomal uL24/RPL26 UFMylation at the ER**. This step is inferred from cell biology in non-neural cells. "a largely uncharacterized ribosomal protein, RPL26, is the principal target of UFM1 conjugation ... UFMylated RPL26 and the UFMylation machinery are in close proximity to the SEC61 translocon" (PMID:30626644; HEK/K562 cells). Branches:
   - **3a. Failed ER ribosome-associated quality control (ER-RQC)** at stalled translocon-bound 60S subunits: "ER-RQC differs from cytosolic RQC by requiring covalent conjugation of the ubiquitin-like protein UFM1 (UFMylation) to uL24" (PMID:40315331). Arrest peptides are then released into the ER lumen instead of being degraded: "In the absence of RQC or UFMylation machinery, ER-APs are not properly extracted into the cytosol for degradation but are instead released into the ER lumen" (PMID:40315331; HEK293). See also PMID:36945571 (PNAS 2023) and PMID:31595041 (Cell Res 2020); both were found by search and are not yet cached.
   - **3b. ER stress with PERK-branch UPR activation and reduced global translation** in neurons. This was demonstrated in mouse *Ufm1*-KO neurons: "UFM1 loss is associated with induction of ER stress, activation of the unfolded protein response (UPR) pathway, and reduced protein translation" (PMID:41731076). The paper shows PERK specifically, with ATF6 and IRE1α unchanged. Suggested GO terms: GO:0036499 PERK-mediated unfolded protein response (INCREASED); GO:0006412 translation (DECREASED).
     - *Conflicting evidence:* overexpressing R81C in HeLa or SH-SY5Y cells did not change CHOP/BiP or tunicamycin-induced apoptosis (PMID:29868776).
4. Steps 3a/3b **lead to impaired neuronal development and synapse formation**, demonstrated in mouse. "UFM1-deficiency confounds neuron development and synapse function" (PMID:41731076). Dendrite complexity (GO:0016358) and synapse number (GO:0007416) were reduced, excitatory transmission was reduced, and R81C rescued these only partially.
5. **Selective neuron loss.** This is demonstrated in mouse; in humans it is inferred from MRI. "CNS-specific knockout of Ufm1 in mice caused neonatal death with microcephaly and apoptosis of neurons in specific brain regions" (PMID:28931644, citing Muona 2016, PMID:27545674). GO:0051402 neuron apoptotic process (INCREASED).
   - In patients this appears as **progressive atrophy of the caudate, putamen, cerebellar vermis and cortex**, and as **postnatal progressive microcephaly**.
   - The authors infer apoptosis from imaging: "signal abnormality of the lateral part of the head of the caudate nucleus suggestive of local apoptosis" (PMID:28931644).
6. **Hypomyelination**, the step with the weakest evidence. **The mechanism is unresolved**: it may be a primary oligodendrocyte defect or secondary to neuronal and axonal failure.
   - The only oligodendroglial data come from a *UFC1* R23Q variant in the mouse FBD-102b line. There, mutant UFC1 aggregated in lysosomes, Akt phosphorylation fell, and MBP/PLP1 expression and morphological differentiation were reduced (PMID:39846712; IN_VITRO, a different gene).
   - Suggested GO terms: GO:0022010 central nervous system myelination (DECREASED); GO:0048709 oligodendrocyte differentiation (DECREASED, and label it *hypothesis*).
7. Steps 4–6 **result in the clinical picture**:
   - basal-ganglia and cortical failure → dystonia, opisthotonus, spastic tetraparesis;
   - cortical dysfunction → epileptic encephalopathy and absent development;
   - brainstem and bulbar involvement → inspiratory stridor, dysphagia, bradypnea and apnea, leading to respiratory insufficiency and death (clinical inference);
   - sensory pathway failure → visual and hearing loss.

### Branch-point summary

| Step | Evidence type | Demonstrated in |
|---|---|---|
| Reduced promoter activity | IN_VITRO | Neuroblastoma and astroglioma cell lines |
| Reduced UFMylation | IN_VITRO | R81C patient lymphoblasts, HEK293T |
| RPL26 UFMylation / ER-RQC | IN_VITRO | HEK293, K562 |
| PERK-UPR activation, reduced translation, fewer synapses | MODEL_ORGANISM / IN_VITRO | Mouse *Ufm1*-cKO primary neurons, in utero electroporation |
| Neuronal apoptosis, microcephaly | MODEL_ORGANISM | *Ufm1*^f/f;nestin-Cre mouse |
| Oligodendrocyte differentiation defect | IN_VITRO, **UFC1 not UFM1** | FBD-102b |
| Hypomyelination, basal-ganglia and cerebellar atrophy | HUMAN_CLINICAL (MRI) | Patients |

**Cell types (CL, cache-verified):**
- neuron CL:0000540
- medium spiny neuron CL:1001474 (striatum; inferred from caudate/putamen atrophy)
- oligodendrocyte CL:0000128
- oligodendrocyte precursor cell CL:0002453
- astrocyte CL:0000127 (the promoter effect was seen in the U373 astroglioma line)
- Purkinje cell CL:0000121 and cerebellar granule cell CL:0001031 are possible but not demonstrated.

**Other GO terms:** GO:0071566 UFM1 activating enzyme activity (UBA5 step). Terms for ribosome-associated quality control, rescue of stalled ribosomes, and UFM1 conjugating/transferase activity are **[lookup needed]**.

**Omics.** Bulk RNA-seq of *Ufm1*-KO mouse neurons found 539 differentially expressed genes. Synaptic genes went down, and translation and RNA-processing genes went up (PMID:41731076). There are no human transcriptomic, proteomic, metabolomic, single-cell or spatial data.

## 7. Anatomical structures affected

- **Primary organ:** brain (UBERON:0000955) and CNS (UBERON:0001017).
- **Structures on imaging:**
  - cerebral white matter (white matter UBERON:0002316)
  - putamen (UBERON:0001874)
  - caudate nucleus (UBERON:0001873)
  - basal ganglion (UBERON:0002420)
  - cerebellum, mainly the vermis (UBERON:0002037)
  - corpus callosum (UBERON:0002336)
  - cerebral cortex (UBERON:0000956)
  - medulla oblongata, thin in one case (UBERON:0001896)
  - optic nerves, hypoplastic in one case
- **Secondary:** larynx (UBERON:0001737), through abnormal tone or innervation producing stridor (PMID:34573312); respiratory control; growth.
- **Subcellular:** the endoplasmic reticulum membrane (cytosolic face) and ER-bound ribosomes / the 60S subunit at the SEC61 translocon (PMID:30626644, 40315331). GO CC terms: **[lookup needed]**.
- **Lateralization:** bilateral and symmetric.

## 8. Temporal development

- **Onset:** neonatal to early infantile.
  - "Presentation is no later than 2 months" (PMID:35189806).
  - Median age at first symptoms is 2 months (Hamilton, as summarized in PMID:34573312).
  - Szűcs gives an average of 2.5 months (range 1 week–6 months).
- **Course:** progressive and neurodegenerative. Minimal development is followed by regression at 2–5 months. MRI shows progressive cerebral atrophy and cerebellar atrophy developing over 3–15 months (PMID:28931644). Myelination stays severely deficient, with only slight gains in 3/5 patients on follow-up scans.
- **Remission:** none.
- **Critical period:** the prenatal and early postnatal window. Carrier testing and prenatal diagnosis are the only interventions that change outcome.

## 9. Inheritance and population

- **Inheritance:** autosomal recessive. Penetrance was assumed complete in the linkage analysis, and segregation was "in perfect agreement".
- **Expressivity:** fairly uniform and severe for the promoter variant.
- **Anticipation and germline mosaicism:** not reported.
- **Founder effect:** a Roma founder haplotype (PMID:28931644) and a separate Sudanese R81C founder haplotype (PMID:29868776).
- **Geography:** Slovakia, Hungary, Bulgaria, and other European Roma communities. The promoter variant has also been reported in Pakistani and Indian patients (PMID:34573312, 39470296).
  - The shared South Asian ancestry of the Roma (PMID:42195294) may explain the Indian and Pakistani cases, but no haplotype study has shown this.
- **Carrier frequency:** 4.5% across European Roma panels, 3.3% in Eastern Slovak Roma, and about 25% in one endogamous community.
- **Prevalence and incidence:** no published estimate.
  - *My own derivation, not a sourced figure:* Hardy–Weinberg with 4.5% carriers (q ≈ 0.0225) gives an expected birth prevalence of about 5 per 10,000 among Roma if mating were random. Endogamy would raise it locally.
  - For the KB, use `prevalence_class: NOT_YET_DOCUMENTED` or `RARE` with `measure_type: UNKNOWN`, and record the carrier data as `CARRIER_FREQUENCY` (PMID:28931644).
- **Case count:** Szűcs counted 23 published patients in 2021. Adding Ivanov's 9 (2023), Kaur's 2 (2025) and Drobňaková's 17 (2026) gives more than 50. That total is my own tally, and the cohorts may overlap.
- **Sex ratio:** 11 males to 6 females in the Slovak cohort (PMID:42195294) and 1:1 in Szűcs. There is no evidence of a sex effect.

## 10. Diagnostics

- **MRI pattern recognition** is the key clinical clue:
  - hypomyelination
  - a very small or absent putamen
  - a small caudate with high T2 signal in the lateral part of the caudate head (distinguishes it from TUBB4A H-ABC)
  - cerebellar vermis atrophy
  - progressive cerebral atrophy (PMID:28931644)
- **MR spectroscopy:** "almost equally high peaks of choline, creatine, and N-acetyl-aspartate" in one advanced case (PMID:34573312).
- **EEG:** diffuse cortical dysfunction and hypsarrhythmia.
- **Genetic testing:**
  - **Targeted Sanger testing of the founder variant** is fast and suited to Roma infants with the phenotype (PMID:34573312). The Slovak center diagnosed most patients this way, with a mean of 5.7 months from symptom onset to diagnosis (PMID:42195294).
  - **Exome sequencing can miss the variant:** "As the coverage of the promoter region of the UFM1 gene is generally poor in the case of exome sequencing data, and in many cases only the coding region of the genes are analyzed, this pathogenic founder variant could be easily missed" (PMID:34573312). Solo exome sequencing did detect it in two Indian patients (PMID:39470296).
  - Genome sequencing covers the promoter.
  - Chromosomal microarray, karyotype, FISH, mtDNA and repeat testing are not relevant.
- **Clinical rule of thumb:** "Roma patients with severe encephalopathy in early infancy with stridor, opisthotonus, bradypnea, severe hearing and visual impairment should be tested for the Roma founder mutation" (PMID:35189806).
- **Biomarkers:** none validated. UFM1-conjugate immunoblots of lymphoblasts are research-only (PMID:29868776).
- **Differential diagnosis:**
  - TUBB4A H-ABC / HLD6 (dominant, de novo; normal caudate signal)
  - UBA5- and UFC1-related encephalopathies (same pathway)
  - PCH1B (*EXOSC3*, also a Roma founder variant, also with stridor)
  - Pelizaeus–Merzbacher disease
  - POLR3-related leukodystrophy
  - other HLDs (PMID:39470296, 42195294)
- **Screening:** there is no newborn screening. Carrier and cascade testing in Roma communities is recommended (PMID:28931644, 42195294).

## 11. Outcome and prognosis

| Cohort | Survival |
|---|---|
| Hamilton 2017 (n=16) | "Median survival was 2 years. Nine patients died at ages between 7 months and 7 years, most often due to respiratory insufficiency." |
| Szűcs 2021 (n=4) | Median survival 28 months |
| Ivanov 2023 (n=9) | "The age at death was between 8 and 18 mo." |
| Drobňaková 2026 (n=17) | "The average age at death was 11.8 months, and the longest-surviving patient lived to be 30 months old"; 1 alive |
| Nahorski 2018, R81C (n=4) | 100% mortality in Table 2; two deaths are described in the text, at 9 months and 8.5 years |

- **Causes of death:** respiratory insufficiency, apnea, cardiopulmonary arrest.
- **Morbidity:** total dependence; no motor or cognitive milestones; need for tracheostomy, tube feeding or ventilation.
- **Recovery potential:** none.
- **Prognostic factors:** none established. The later-surviving Hamilton patients (up to 7 years) suggest some variability.

## 12. Treatment

**No disease-modifying therapy exists.** A ClinicalTrials.gov search for "UFM1" (API query, 2026-09-25) returned **zero studies**.

**Supportive care**

| Intervention | NCIT (cache-verified) | Evidence |
|---|---|---|
| Anticonvulsants, e.g. carbamazepine (CHEBI:3387); levetiracetam (CHEBI:6437) and vigabatrin (CHEBI:63638) are plausible for West syndrome but not documented in HLD14 | NCIT:C15986 Pharmacotherapy + `therapeutic_agent` | Carbamazepine given to one patient (PMID:34573312); epilepsy is often "drug-resistant" (PMID:28931644) |
| Baclofen for spasticity (CHEBI:2972) | NCIT:C15986 | One patient (PMID:34573312) |
| Gastrostomy / tube feeding | NCIT:C52006 Gastrostomy; NCIT:C15433 Nutritional Support | PMID:34573312 |
| Tracheostomy | **[lookup needed]** (no cached NCIT term) | 6/16 tracheostomy (PMID:28931644) |
| Ventilatory support | NCIT:C70909 Mechanical Ventilation | "4 of whom were on intermittent or permanent ventilation" (PMID:28931644) |
| Supportive and palliative care | NCIT:C15747 Supportive Care | General |
| Physical therapy / rehabilitation | NCIT:C15302 / NCIT:C15315 | General; not documented in HLD14 sources |
| Genetic counseling | NCIT:C15240 | PMID:28931644, 42195294 |

**Preclinical only (not for `treatments`; better as a discussion or hypothesis):**
- **Trazodone** (UPR/PERK inhibitor): "Trazodone, an inhibitor of the UPR, restores protein translation solely in UFM1-R81C-expressing neurons, and increases synapse numbers in both UFM1-KO and UFM1-R81C-expressing neurons" (PMID:41731076; mouse neurons). It did not rescue dendrite complexity. The trazodone CHEBI ID is **[lookup needed]**.
- **Hesperetin:** restored oligodendroglial differentiation in UFC1-R23Q FBD-102b cells (PMID:39846712). It is a different gene, and the authors themselves call the effect "limited".

There is no gene therapy, ASO or cell therapy, and no pharmacogenomic data.

## 13. Prevention

- **Primary prevention:** carrier screening and preconception or prenatal testing in at-risk Roma communities.
  - "The identification of the disease-causing variant enables better clinical and genetic counseling, the possibility of prenatal testing, and the option of carrier testing in populations with a high carrier frequency" (PMID:28931644).
  - "Prenatal and newborn screening, along with voluntary carrier testing for couples, is essential" (PMID:42195294).
- **Secondary prevention:** early targeted testing of symptomatic Roma infants shortens the diagnostic delay.
- **Tertiary prevention:** airway management, nutrition and seizure control.
- **Not applicable:** immunization, behavioral interventions, prophylaxis.

## 14. Other species and natural disease

- No naturally occurring UFM1 disease was found. OMIA was not searched directly.
- *UFM1* orthologs are conserved across metazoans: "each of its components having a corresponding orthologue in all multicellular organisms" (PMID:29868776). UFMylation is metazoan-specific (PMID:30626644).
- Mouse and human UFM1 proteins are identical (PMID:41731076).
- No zoonotic or transmission relevance.

## 15. Model organisms

| Model | Recapitulation | Limitations | Source |
|---|---|---|---|
| *Ufm1*^f/f;nestin-Cre mouse (CNS cKO) | Microcephaly, neuronal apoptosis, neonatal death | Complete loss rather than hypomorph; death within a day limits study of myelination | Muona 2016, PMID:27545674 (not yet cached; described in PMID:28931644, 29868776) |
| *Ufm1* whole-body KO mouse | Embryonic lethal | Cannot model postnatal disease | Unpublished, cited in PMID:29868776 |
| *Ufm1*-cKO primary hippocampal/striatal neurons ± WT or R81C rescue; in utero CRISPR KO | Reduced dendrites and synapses, PERK-UPR activation, reduced translation; R81C only partially rescues | Neurons only, no oligodendrocytes; mouse; no promoter-variant model | PMID:41731076 (MODEL_ORGANISM / IN_VITRO) |
| *Ufl1*/*Ufbp1* forebrain KO mouse | Microcephaly, seizures, neuron loss | E3 rather than UFM1 | Zhang 2022, *Mol Neurobiol*, doi:10.1007/s12035-022-02979-0 (PMID not verified) |
| *Drosophila* Ufm1 knockdown | Reduced motor activity, shortened lifespan (most severe of the pathway knockdowns) | Invertebrate; no myelin | Duan 2016, cited in PMID:28931644 |
| UFM1/UFC1-KO HEK293T; patient lymphoblasts (R81C) | Reduced UFMylation | Non-neural | PMID:29868776 |
| FBD-102b oligodendroglial line expressing UFC1-R23Q | Differentiation defect | Different gene; overexpression | PMID:39846712 |

**Gaps in models:**
- No animal or iPSC model carries the founder promoter deletion.
- No oligodendrocyte-specific *Ufm1* model exists.
- No model reproduces hypomyelination together with the basal-ganglia pattern.

In the KB, the `modeled_mechanisms` links for the mouse cKO should record `model_scale` and a `limitations` or `SPECIES_MISMATCH`/`BOUNDARY_OMISSION` divergence. Hypomyelination is outside every current model.

---

## Curation notes for the entry

- **Mappings:**
  - `disease_term`: MONDO:0033486
  - Orphanet ORPHA:139441 as `skos:broadMatch` (H-ABC includes TUBB4A)
  - The TUBB4A GeneReviews chapter is not a baseline for this entry
- **Gene:** hgnc:20597 (UFM1). It is **not yet in `cache/hgnc/terms.csv`**, so run `just validate-terms` after binding it.
- **Before binding, look up:** drug-resistant epilepsy, bradypnea, tracheostomy (NCIT), trazodone (CHEBI), ER-RQC and ER-membrane GO terms.
- **Fetch before citing:** PMID:27545674 (Muona), PMID:36945571 and PMID:31595041 (RPL26 ER-RQC). None of the three is cached yet.
- **Evidence grading for PMID:34573312:** its opening paragraph quoting Hamilton's statistics restates another paper, so mark it `quote_role: BACKGROUND`. The same applies to the Drobňaková discussion paragraphs that restate Hamilton.

---

### Sources
- Local cache: `references_cache/PMID_28931644.md`, `PMID_29868776.md`, `PMID_30626644.md`, `PMID_34573312.md`, `PMID_35189806.md`, `PMID_39470296.md`, `PMID_39846712.md`, `PMID_40315331.md`, `PMID_41731076.md`, `PMID_42195294.md`; `cache/bookshelf/genereviews.csv`
- [OLS MONDO:0033486](https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?obo_id=MONDO:0033486)
- [HGNC UFM1](https://rest.genenames.org/fetch/symbol/UFM1) · [HGNC UFC1](https://rest.genenames.org/fetch/symbol/UFC1)
- [Orphanet ORPHA:139441 (H-ABC)](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=en&Expert=139441)
- [Muona et al. 2016, PMID:27545674](https://pubmed.ncbi.nlm.nih.gov/27545674/) · [AJHG full text](https://www.cell.com/ajhg/fulltext/S0002-9297(16)30224-5)
- [Wang et al. 2020 Cell Res, PMID:31595041](https://pubmed.ncbi.nlm.nih.gov/31595041/) · [Scavone et al. 2023 PNAS, PMID:36945571](https://pubmed.ncbi.nlm.nih.gov/36945571/)
- [Zhang et al. 2022 Mol Neurobiol](https://link.springer.com/article/10.1007/s12035-022-02979-0)
- [Perdigão et al. 2026 EMBO Mol Med](https://link.springer.com/article/10.1038/s44321-026-00389-6)
- [ClinicalTrials.gov API query "UFM1"](https://clinicaltrials.gov/api/v2/studies?query.term=UFM1)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 27 |
| Quoted claims found in source | 26 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 16 |
| On topic | 10 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:27545674` *(abstract only)*: "CNS-specific knockout of Ufm1 in mice caused neonatal death with microcephaly and apoptosis of neurons in specific brain regions"
  - closest text in source: "Finally, we show that the CNS-specific knockout of Ufm1 in mice causes neonatal death accompanied by microcephaly and apoptosis in specific neurons, further suggesting that the UFM1 system is essential for CNS development and function"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 75 |
| Resolved | 74 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 27 |
| Terms named correctly | 18 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `DOID:0080296` (1 mention) - the report calls it "DOID"; DOID calls it **hypomyelinating leukodystrophy 14**
- `HP:0001332` (1 mention) - the report calls it "Dystonia, extrapyramidal signs"; HP calls it **Dystonia**
- `CL:1001474` (1 mention) - the report calls it "striatum; inferred from caudate/putamen atrophy"; CL calls it **medium spiny neuron**
- `UBERON:0000955` (1 mention) - the report calls it "Primary organ:** brain"; UBERON calls it **brain**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001272` (1 mention) - the report calls it "Cerebellar atrophy (vermis)"; HP calls it **Cerebellar atrophy**
- `UBERON:0002037` (1 mention) - the report calls it "cerebellum, mainly the vermis"; UBERON calls it **cerebellum**
- `UBERON:0001896` (1 mention) - the report calls it "medulla oblongata, thin in one case"; UBERON calls it **medulla oblongata**
- `UBERON:0001737` (1 mention) - the report calls it "Secondary:** larynx"; UBERON calls it **larynx**
- `CHEBI:2972` (1 mention) - the report calls it "Baclofen for spasticity"; CHEBI calls it **baclofen**, and lists "baclofeno" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.