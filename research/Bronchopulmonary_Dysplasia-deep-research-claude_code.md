---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5-5
cached: false
start_time: '2026-10-03T23:29:02.900281'
end_time: '2026-10-03T23:30:24.439870'
duration_seconds: 81.54
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Bronchopulmonary Dysplasia
  mondo_id: MONDO:0019091
  category: Complex
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
  - claude-sonnet-5-5
  web_search_requests: 3
  num_turns: 5
  total_cost_usd: 0.8399449999999999
  session_id: 81562984-f39d-5787-be67-7015e0b1b678
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
citation_count: 4
reference_validation:
  total_references: 5
  verified: 5
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 5
  on_topic: 4
  off_topic: 1
  off_topic_references:
  - PMID:16943402
  needs_review: true
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 30
  verified: 30
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 14
  labels_matching: 8
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0019091
    reported_labels:
    - given in the template; verify
    ontology_label: bronchopulmonary dysplasia
  labels_variant: 5
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Bronchopulmonary Dysplasia
- **MONDO ID:** MONDO:0019091 (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Bronchopulmonary Dysplasia** covering all of the
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

# Bronchopulmonary Dysplasia (BPD): Research Report for dismech Curation

**Provenance and verification status.** Three web searches were run (definition, pathogenesis review, prevention). They confirmed the bibliographic identity of the sources listed in the next paragraph but did not return PMIDs or abstract text.

- All other facts come from model background knowledge.
- Every PMID below is recalled from memory and is **unverified**.
- No abstract quotes are supplied, because I did not retrieve the abstracts and will not invent them.
- Before any claim becomes an evidence item, run `just fetch-reference PMID:<id>` and quote from the cached file.
- Per the CLAUDE.md term-contract rule, every ontology CURIE below is a **lead** and must be looked up before binding.

**Sources confirmed by search**
- Thébaud et al., Nat Rev Dis Primers 2019;5:78, PMC6986462 (https://pmc.ncbi.nlm.nih.gov/articles/PMC6986462).
- Higgins et al., J Pediatr 2018;197:300–308, the NICHD 2018 workshop summary.
- Jensen et al., Am J Respir Crit Care Med 2019, "The diagnosis of bronchopulmonary dysplasia in very preterm infants: an evidence-based approach".
- Review of management evidence: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8069828/
- Pathogenesis review: https://pubmed.ncbi.nlm.nih.gov/37445242/

**PMIDs recalled from memory, to be verified**

| Paper | Recalled PMID |
|---|---|
| Jobe & Bancalari, NICHD/NHLBI workshop 2001 | 11401896 |
| Northway et al. 1967 | 5229934 |
| Thébaud et al. 2019 | 31727986 |
| Schmidt et al., CAP trial 2006 | 16943402 |

---

## 1. Disease Information

**Overview.** BPD is a chronic lung disease of prematurity. Injury to the immature lung, from oxygen, ventilation and inflammation, arrests alveolar and microvascular development ("alveolar simplification"). Thébaud 2019 frames it as an injury process occurring while the lung is still developing, then repairing and remodelling over months to years.

**Identifiers**
- MONDO:0019091 (given in the template; verify).
- ICD-10-CM P27.1 (BPD originating in the perinatal period). ICD-11 CA20.0, from memory, verify.
- MeSH D001997.
- OMIM: none, because the disease is multifactorial. Orphanet: not a rare Mendelian entry.

**Synonyms.** Chronic lung disease of prematurity (CLD); neonatal chronic lung disease; "old" (Northway) vs "new" BPD.

**Definition history**
- Northway 1967 described classic BPD in ventilated, larger preterm infants. Its histology showed fibrosis, squamous metaplasia and airway injury.
- NICHD 2001 (Jobe & Bancalari) defined BPD by oxygen need at 28 days, graded at 36 weeks postmenstrual age (PMA) as mild, moderate or severe.
- NICHD 2018 (Higgins) and Jensen 2019 (an evidence-based definition) grade severity by respiratory support at 36 weeks PMA. Jensen 2019 is Grade 1 = nasal cannula ≤2 L/min, Grade 2 = >2 L/min or NIPPV/CPAP, Grade 3 = invasive ventilation, with a "2A/3A" early-death category. Grade boundaries are from memory.

**Data source.** Disease-level aggregate, not EHR-derived.

## 2. Etiology

**Causal factors.** BPD is multifactorial, with prematurity as the necessary background. The main drivers are:
- Hyperoxia and oxidative stress.
- Mechanical ventilation (volutrauma and barotrauma).
- Antenatal and postnatal infection or inflammation (chorioamnionitis, sepsis).
- Pulmonary insufficiency of prematurity and a patent ductus arteriosus (PDA).

**Risk factors**
- Lower gestational age and birth weight are the dominant risk factors.
- Fetal growth restriction, male sex, chorioamnionitis, postnatal sepsis and prolonged ventilation also raise risk.
- Maternal smoking, preeclampsia and PDA are further associated factors.
- Genetic risk: twin studies report high heritability (on the order of 50–80%). I recall Bhandari 2006 and Lavoie 2008, with no confident PMIDs.
  - GWAS have found no robust locus.
  - Candidate genes, such as SPINK1 and surfactant protein genes (SFTPB), are inconsistent.
- Genetic note for curation: use `relationship_type: SUSCEPTIBILITY` or `MODIFIER`. Do not use `CAUSATIVE`.

**Protective factors**
- Antenatal corticosteroids and female sex.
- Caffeine (the CAP trial showed lower BPD).
- Breast milk.
- Gentle ventilation and noninvasive support.

**Gene–environment interaction.** Inferred rather than demonstrated: genetic susceptibility to oxidative injury, for example, interacts with hyperoxia exposure.

## 3. Phenotypes (HPO leads, verify)

Frequencies are not reliably sourced here. Reported BPD incidence depends on definition (see section 9).

| Phenotype | HPO lead | Notes |
|---|---|---|
| Tachypnea | HP:0002789 | Onset is neonatal; persists in severe BPD |
| Dyspnea / respiratory distress | HP:0002098 | Neonatal; often worsens in the first weeks |
| Hypoxemia | HP:0012418 | Oxygen dependence is the defining feature |
| Chronic lung disease / bronchopulmonary dysplasia | HP:0006528 or HP:0006529 | Verify the correct term |
| Wheezing | HP:0030828 | Common in infancy and childhood |
| Recurrent respiratory infections | HP:0002205 | Common in the first 2 years |
| Pulmonary hypertension | HP:0002092 | Complication in a subset |
| Failure to thrive | HP:0001508 | Increased work of breathing and caloric needs |
| Abnormal lung CT / emphysema | not verified | Structural abnormality in survivors |
| Reduced FEV1 | not verified | Persistent airflow obstruction into adulthood |

**Course.** Onset is neonatal. Severity ranges from mild to severe. Symptoms improve with lung growth but can persist. Quality-of-life data are not retrieved in this report.

## 4. Genetic / Molecular Information

- **Causal genes:** none established; BPD is non-Mendelian.
- **Susceptibility and modifier genes:** inconsistent candidate-gene results. Surfactant genes (SFTPB, ABCA3 and SFTPC) cause interstitial lung disease in neonates and are differentials, not BPD causes.
- **Epigenetics:** altered DNA methylation in cord blood and tracheal aspirates has been reported. This is not verified here.
- **Chromosomal abnormalities:** none characteristic. FOXF1 and TBX4 variants mimic BPD with pulmonary hypertension.

## 5. Environmental Information

- **Environmental:** supplemental oxygen (hyperoxia), mechanical ventilation, and postnatal steroids as a treatment confounder.
- **Lifestyle:** maternal smoking in pregnancy.
- **Infectious agents:** *Ureaplasma* species are associated with BPD. Causality is not demonstrated, and trials of azithromycin for *Ureaplasma* have been inconclusive.
- **ECTO leads** (verify): hyperoxia exposure and tobacco-smoke exposure.

## 6. Mechanism / Pathophysiology

**Causal chain** (steps marked "inferred" are not directly demonstrated in humans)

1. Preterm birth interrupts the canalicular/saccular stages of lung development. The lung has surfactant deficiency and few alveoli.
2. This leads to respiratory failure requiring ventilation and oxygen.
3. Hyperoxia and ventilation produce oxidative stress and mechanical stretch injury of the epithelium.
4. Prenatal or postnatal infection and inflammation add cytokine signaling (IL-1β, IL-6, IL-8, TNF-α) and neutrophil/macrophage recruitment.
5. This leads to epithelial injury, apoptosis and disrupted growth-factor signaling, including VEGF, in the immature lung. The loss of VEGF signaling in the alveolar capillary network is inferred largely from animal models.
6. This leads to arrested alveolarization and impaired microvascular development, giving alveolar simplification, fewer and larger alveoli, and a dysmorphic capillary bed.
7. This leads to reduced gas-exchange surface area, causing chronic hypoxemia and oxygen dependence.
8. Branch A: vascular remodelling and raised pulmonary vascular resistance lead to pulmonary hypertension and right heart strain.
9. Branch B: airway smooth muscle hypertrophy and remodelling lead to airway hyperreactivity and wheeze.
10. Long-term, incomplete lung growth leads to persistent airflow obstruction in adulthood (COPD-like trajectory, inferred).

**GO / CL leads (verify)**
- Processes: response to hyperoxia (GO:0055093), inflammatory response (GO:0006954), alveolar development (GO:0048286), angiogenesis (GO:0001525), apoptotic process (GO:0006915), response to oxidative stress (GO:0006979), extracellular matrix organization (GO:0030198).
- Cells: type II pneumocyte (CL:0002063), pulmonary alveolar epithelial cell, lung endothelial cell, alveolar macrophage (CL:0000583), fibroblast (CL:0000057), airway smooth muscle cell (CL:0002062).

**Molecular profiling.** Not retrieved here. Check GEO for neonatal lung and tracheal-aspirate transcriptomics before adding a `datasets:` block. Per CLAUDE.md, run `just verify-datasets` and manually check disease relevance. Single-cell lung atlases of hyperoxia-injured neonatal mouse lung exist, but were not verified.

## 7. Anatomical Structures Affected

- **Primary:** lung (UBERON:0002048), specifically the alveolus (UBERON:0002299) and the terminal airways and pulmonary vasculature.
- **Secondary:** heart (right ventricle, via pulmonary hypertension); brain (neurodevelopmental effects in severe BPD); growth and nutrition.
- **Localization:** bilateral and diffuse, with heterogeneous regional involvement on imaging.
- **Subcellular:** mitochondria (oxidative stress) and the endoplasmic reticulum (surfactant protein handling); not verified.

## 8. Temporal Development

- **Onset:** neonatal. The diagnosis is made at 36 weeks PMA (or at 28 days in the 2001 definition).
- **Stages:** the acute neonatal injury phase, then a chronic phase with repair and remodelling over months to years (Thébaud 2019). Do not curate phases as separate entries; list them under `progression:`.
- **Course:** most infants wean off oxygen in infancy, but a subset have severe disease with tracheostomy, home ventilation or pulmonary hypertension.
- **Critical periods:** the first postnatal days (ventilation, oxygen and early caffeine) and the late-gestation window (antenatal steroids).

## 9. Inheritance and Population

- **Inheritance:** multifactorial; no Mendelian pattern. Twin heritability is high.
- **Incidence and prevalence:** about 40% of infants born before 28 weeks, and 10,000–15,000 new US cases annually (from memory). Because the figure depends on the definition used, record the definition with each rate: `measure_type`, `rate_denominator: LIVE_BIRTHS`, and the cohort in `population`. Verify against the NICHD Neonatal Research Network (Stoll et al.).
- **Demographics:**
  - Affected infants are mostly those born extremely preterm; survival improvements have increased the number of survivors with BPD.
  - Boys are at higher risk.
  - Geographic variation reflects differences in NICU practice.

## 10. Diagnostics

- **Clinical criteria:** NICHD 2001, NICHD 2018 and Jensen 2019 (see section 1), all based on respiratory support at 36 weeks PMA.
- **Imaging:** chest X-ray (hazy lungs, cystic or fibrotic changes in classic BPD), lung ultrasound, and CT or MRI in selected cases.
- **Echocardiography:** screen for pulmonary hypertension.
- **Functional tests:** infant pulmonary function testing; later spirometry (reduced FEV1).
- **Biomarkers:** research only, with no validated clinical biomarker. Candidates include cytokines and endostatin; not verified.
- **Genetic testing:** not routine. Consider surfactant-gene and FOXF1/TBX4 testing in atypical or term-infant presentations.
- **Differential diagnosis:** surfactant protein deficiency, ILD of infancy, pulmonary vascular disease, congenital heart disease and aspiration.
- **Screening:** none for the disease itself. Risk stratification tools exist (the NICHD BPD outcome estimator); not verified.

## 11. Outcome / Prognosis

- Mortality is higher in severe BPD (see Jensen 2019 for outcome by grade).
- Survivors have more respiratory hospitalizations in early childhood, with persistent obstruction and reduced exercise capacity into adulthood.
- Neurodevelopmental impairment is more frequent.
- Complications include pulmonary hypertension, cor pulmonale, growth failure and airway malacia.
- Prognostic factors: gestational age, severity grade, pulmonary hypertension and ventilator dependence.
- No pooled survival numbers were verified for this report.

## 12. Treatment

NCIT treatment-term leads (verify): NCIT:C15986 (Pharmacotherapy), NCIT:C15747 (Supportive Care), NCIT:C15447 (Dietary Intervention).

- **Pharmacotherapy (prevention and treatment)**
  - Caffeine citrate (CHEBI:27732, verify). The CAP trial (Schmidt 2006, PMID 16943402 unverified) showed a lower BPD rate. Search results note that earlier initiation seems more effective; a 2025 meta-analysis reported lower BPD but higher mortality with early caffeine.
  - Antenatal corticosteroids: strong evidence for preventing BPD.
  - Low-dose hydrocortisone in the first days prevents BPD but was associated with more late-onset sepsis in infants born at 24–25 weeks (search-result summary of the management review).
  - Postnatal dexamethasone has benefits and neurodevelopmental risks; the timing and dose tradeoffs were not verified.
  - Intramuscular vitamin A reduces BPD but is painful, expensive and not widely used.
  - Diuretics and inhaled bronchodilators help symptoms; the evidence for long-term benefit is weak.
  - Pulmonary hypertension: sildenafil, for which the evidence is limited.
- **Respiratory support:** surfactant, less-invasive surfactant administration, noninvasive ventilation, volume-targeted ventilation, and oxygen saturation targeting.
- **Cell and gene therapy:** mesenchymal stromal cell trials are in phase I/II. I do not have NCT numbers; search ClinicalTrials.gov and fetch each record before citing it.
- **Supportive:** nutrition, growth support, infection avoidance and pulmonary rehabilitation.
- **Surgical:** tracheostomy for prolonged ventilator dependence.

## 13. Prevention

- **Primary:** prevention of preterm birth, antenatal corticosteroids, and avoidance of maternal smoking.
- **Respiratory strategy:** gentle ventilation, noninvasive support, and early caffeine.
- **Tertiary:** avoid respiratory infection (RSV prophylaxis, vaccination) and optimize growth.
- **Counseling:** parental counseling about outcomes; not verified further.

## 14. Other Species / Natural Disease

Naturally occurring BPD is not established in other species. Preterm lambs and baboons are used experimentally (see section 15). NCBITaxon leads (verify): Ovis aries (NCBITaxon:9940), Papio (NCBITaxon:9554), Mus musculus (NCBITaxon:10090).

## 15. Model Organisms

Use the `animal_models:` section (not `experimental_models`), and link each model to a pathophysiology node via `modeled_mechanisms` with `fidelity` and `limitations`.

- **Hyperoxia-exposed neonatal rodents** (mouse and rat). Postnatal hyperoxia gives alveolar simplification and impaired angiogenesis. Fidelity is limited because rodent lungs are saccular rather than alveolar at birth, so the developmental stage differs from that of a preterm human.
- **Preterm baboon** (the 125-day, ventilated model), which reproduces "new BPD" most closely. Practical limits are cost and availability.
- **Preterm lamb.** Similar fidelity strengths, with a larger-animal practical burden.
- **In vitro:** lung organoids and iPSC-derived lung models, plus hyperoxia-exposed cell culture. Evidence source is `IN_VITRO`.
- **Genetic models:** VEGF-pathway and related knockouts show the role of vascular signaling. The specific mouse lines and MGI identifiers were not verified.

---

## Curation Cautions (CLAUDE.md-specific)

1. **Granularity.** Treat BPD as a single disease entry, with severity grades as `has_subtypes` or `stages` only if the sources support it. The "old/new BPD" split can be a note.
2. **Genetic section.** No causative genes; use susceptibility or modifier typing, and leave `gene_disease_validity` absent because no external classification exists.
3. **Prevalence.** Use structured `Prevalence` slots with `measure_type` and `rate_denominator`, not free text.
4. **Evidence.** Quote only from cached references after `just fetch-reference`. Grade `evidence_source` by the cited study type: rodent, baboon and lamb evidence is `MODEL_ORGANISM`.
5. **Preterm-infant studies.** These are `HUMAN_CLINICAL`; guideline or review statements may need `quote_role: REVIEW_SYNTHESIS`.
6. **Causal wiring.** Connect the phenotypes (hypoxemia, wheeze, pulmonary hypertension) to pathophysiology nodes with bare-name `downstream` targets.
7. **Before the PR.** Run `just validate`, `just validate-terms`, `just count-verified-snippets`, and `just validate-disorders`. Add a `history/` record.

## Gaps Not Covered by This Research

- Verified PMIDs and abstract quotes for essentially every claim.
- Frequencies for each phenotype.
- Quality-of-life data.
- Transcriptomic and proteomic datasets.
- Clinical trial NCT identifiers.
- A GeneReviews baseline. None is expected, since BPD is not Mendelian; confirm with `just check-genereviews`.

**Sources**
- [Thébaud et al. 2019, PMC6986462](https://pmc.ncbi.nlm.nih.gov/articles/PMC6986462)
- [BPD: Pathogenesis and Pathophysiology](https://pubmed.ncbi.nlm.nih.gov/37445242/)
- [Evidence for the Management of BPD in Very Preterm Infants](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8069828/)
- [Definitions review, Frontiers in Pediatrics 2023](https://www.frontiersin.org/articles/10.3389/fped.2023.1108925/full)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 5 |
| On topic | 4 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:16943402` (1 mention) - A randomized trial of deep-brain stimulation for Parkinson's disease.
  - shared terms: disease

Weighed against this report's own most characteristic terms: `bpd`, `verified`, `pulmonary`, `hypertension`, `disease`, `lung`, `preterm`, `ventilation`, `verify`, `respiratory`, `infant`, `growth`, `lead`, `neonatal`, `oxygen`, `definition`, `postnatal`, `support`, `surfactant`, `week`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 30 |
| Resolved | 30 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 14 |
| Terms named correctly | 8 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0019091` (1 mention) - the report calls it "given in the template; verify"; MONDO calls it **bronchopulmonary dysplasia**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002098` (1 mention) - the report calls it "Dyspnea / respiratory distress"; HP calls it **Respiratory distress**
- `HP:0002092` (1 mention) - the report calls it "Pulmonary hypertension"; HP calls it **Pulmonary arterial hypertension**, and lists "Pulmonary artery hypertension" among its other names
- `GO:0055093` (1 mention) - the report calls it "Processes: response to hyperoxia"; GO calls it **response to hyperoxia**
- `CL:0002063` (1 mention) - the report calls it "Cells: type II pneumocyte"; CL calls it **pulmonary alveolar type 2 cell**, and lists "type II pneumocyte" among its other names
- `UBERON:0002048` (1 mention) - the report calls it "Primary:** lung"; UBERON calls it **lung**