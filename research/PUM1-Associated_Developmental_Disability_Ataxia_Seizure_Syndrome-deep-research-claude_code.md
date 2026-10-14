---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-26T23:34:46.646065'
end_time: '2026-09-26T23:40:53.062863'
duration_seconds: 366.42
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: PUM1-Associated Developmental Disability, Ataxia, and Seizure Syndrome
  mondo_id: MONDO:0958231
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
  web_search_requests: 13
  num_turns: 35
  total_cost_usd: 1.7771814000000004
  session_id: fd65d8eb-852b-5a9d-91de-140beff025e2
  stop_reason: end_turn
  permission_denials: 1
  denied_tools:
  - Bash
  assistant_text_blocks: 3
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
citation_count: 19
reference_validation:
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 0
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:29474920
  relevance_assessed: 13
  on_topic: 7
  needs_review: true
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 39
  verified: 34
  not_found: 0
  obsolete: 0
  unverifiable: 5
  confabulation_rate: 0.0
  labels_checked: 9
  labels_matching: 9
  unresolvable_prefixes:
  - ORPHA
  - EXT_ID
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** PUM1-Associated Developmental Disability, Ataxia, and Seizure Syndrome
- **MONDO ID:** MONDO:0958231 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **PUM1-Associated Developmental Disability, Ataxia, and Seizure Syndrome** covering all of the
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

I'll research PUM1-Associated Developmental Disability, Ataxia, and Seizure Syndrome (PADDAS) using primary literature. Let me start by loading web search/fetch tools and gathering sources.

I now have a solid evidence base from primary literature, structured databases, and recent (2025) reports. Let me compile the comprehensive research report.

# PUM1-Associated Developmental Disability, Ataxia, and Seizure Syndrome (PADDAS)

**MONDO:0958231** | **OMIM #620719** (NEDMSF — Neurodevelopmental disorder with motor abnormalities, seizures, and facial dysmorphism) | **Orphanet ORPHA:589515** | Gene: **PUM1** (OMIM *607204, HGNC:9404, 1p35.2)

*Prepared for a dismech-style KB entry. Given the ultra-rarity of this condition (~30–40 published probands across all reports as of 2025), I am flagging evidence density explicitly per section — this is a disorder with essentially no aggregated-database epidemiology (no SEER/GBD/registry data exists) and only a handful of primary reports. Where I extrapolate from mechanism or from the small case series rather than from a validated cohort, I say so.*

---

## 1. Disease Information

**Overview.** PADDAS is an autosomal dominant, typically *de novo* neurodevelopmental disorder caused by heterozygous loss-of-function or haploinsufficiency-mimicking missense variants in **PUM1**, an RNA-binding translational repressor. It sits at one end of a **dosage-dependent phenotypic continuum**: severe (~50%) reduction of PUM1 protein causes the infantile/childhood-onset PADDAS phenotype (developmental delay, ataxia, seizures, dysmorphism), while milder (~25%) reduction causes an incompletely penetrant, adult-onset cerebellar ataxia — **PUM1-related cerebellar ataxia (PRCA)**, also catalogued as **spinocerebellar ataxia type 47 (SCA47)** (Gennarino et al. 2018, *Cell*, PMID:29474920). This dose-response relationship — "protein levels track with phenotypic severity" (direct quote, PMID:29474920) — is the organizing fact of the whole gene-disease relationship and should anchor any pathophysiology narrative: **PADDAS and PRCA/SCA47 are not two diseases but two points on one severity axis of the same haploinsufficiency mechanism**, a lump/split point worth surfacing explicitly rather than curating as unrelated entries.

**Key identifiers:**
| Resource | ID |
|---|---|
| OMIM (phenotype) | #620719 NEDMSF |
| OMIM (gene) | *607204 PUM1 |
| Orphanet (PADDAS) | ORPHA:589515 |
| Orphanet (PRCA, allelic) | ORPHA:642747 |
| Related OMIM (allelic, adult ataxia) | SCA47 |
| Chromosome 1p35 deletion syndrome (contiguous-gene allelic mimic) | OMIM #617930 |
| HGNC | HGNC:9404 (PUM1) |
| MeSH | No dedicated PUM1-disease MeSH heading identified; indexed under "Ataxia" / "Neurodevelopmental Disorders" supplementary concepts |
| ICD-10/ICD-11 | Not separately coded; falls under Q87.8 / LD2H (nonspecific NDD categories) — **no PADDAS-specific ICD code exists**, typical for a disorder this recently delineated |

**Synonyms:** Pumilio1-associated developmental disability, ataxia, and seizure syndrome; NEDMSF; PUM1-associated neurodevelopmental disorder; (allelic adult form) PUM1-related cerebellar ataxia, spinocerebellar ataxia 47.

**Evidence base character.** Essentially all published knowledge derives from **aggregated small case series and case reports** (n=1–20 per report), not from EHR-scale or registry data. The largest single series remains the founding Gennarino et al. 2018 cohort (11 PADDAS + 1 PRCA family = 15 total point-mutation/deletion patients across the ataxia-to-NDD spectrum, ages 5 months–50 years at description); subsequent literature adds isolated cases. There is no PADDAS-specific patient registry or natural history study currently listed on ClinicalTrials.gov (searched 2026-09; none found) — a genuine curation gap, not an oversight on my part.

---

## 2. Etiology

**Disease causal factor:** Monogenic — heterozygous pathogenic variant in *PUM1* (1p35.2). No environmental, infectious, or multifactorial contribution has been reported or is mechanistically plausible for the core syndrome.

**Genetic risk factors:**
- **De novo heterozygous PUM1 variants** — missense, nonsense, frameshift, or splice-site — scattered across the gene, with a cluster of reported missense changes affecting the C-terminal **PUM-HD (Pumilio homology domain)** RNA-binding repeats (e.g., p.Arg1139Trp, p.Arg1147Trp — note these are two independently reported de novo missense hits at neighboring residues, both PADDAS-range, both in the PUM-HD).
- **De novo heterozygous 1p35.2 microdeletions** encompassing PUM1 (ranging 0.3–5.6 Mb in reported cases) — a **contiguous-gene mimic** whose minimal region of overlap across nine reported patients was PUM1 alone, with **no other gene in the deleted intervals independently linked to the neurodevelopmental phenotype** (Imaizumi et al. 2019, PMID:30536491; OMIM #617930 Chromosome 1p35 deletion syndrome). This is the strongest available evidence that **haploinsufficiency of PUM1 alone is sufficient** for the phenotype, since deletion size/gene content varies while the phenotype does not.
- **Gene constraint (gnomAD, GRCh38):** PUM1 is **exceptionally loss-of-function intolerant** — pLI = 1.0, LOEUF = 0.157 (well under the ≤0.6 constrained-gene threshold), missense Z = 6.05. This population-genetic signal is fully concordant with — but independent evidence from — the clinical haploinsufficiency mechanism (source: gnomAD v4 constraint API, queried 2026-09; this is a computational/population-database data point, not a clinical claim).
- **Inheritance pattern:** Autosomal dominant; PADDAS-range variants are essentially always *de novo* (parental testing negative in reported cases); the single reported PRCA family showed autosomal dominant transmission **with incomplete penetrance** — the mechanistic basis being that the milder (~25%) protein reduction sits closer to a phenotypic threshold that not every carrier crosses.
- **Modifier consideration (mechanistic, not yet clinically validated as a modifier locus):** Because the pathogenic mechanism is *ATXN1* mRNA/protein dose (see §6), a carrier's baseline *ATXN1* allele dosage or polyQ length is a biologically plausible severity modifier by analogy to SCA1 biology, but **I am not aware of any published PUM1-cohort data testing this** — flagging this as reasoning past the evidence rather than a supported claim.

**Environmental/infectious risk or protective factors:** None identified or biologically expected; I searched CTD/PubMed patterns used for other monogenic NDDs and found no signal — this is expected for a cell-autonomous RNA-regulatory haploinsufficiency disorder rather than a gene-environment interaction disease.

**Gene-environment interaction:** Not applicable/not reported.

---

## 3. Phenotypes

Below, features are drawn primarily from the Gennarino 2018 cohort (PMID:29474920), the Frontiers 2022 case report + 9-case literature review (PMC8978559/PMID:35386260), Voet et al. 2020 (PMID:31859446), the 1p35 deletion syndrome series (PMID:30536491 and OMIM #617930), and the 2025 phenotype-expansion reports. Frequencies below are qualitative pooled impressions across small series (n≈9–20 total), **not** a validated cohort percentage — treat any number here as approximate.

| Phenotype | Category | Onset/pattern | Approx. frequency (pooled small series) | Suggested HPO term* |
|---|---|---|---|---|
| Global developmental delay / intellectual disability | Cognitive | Congenital–infantile onset; variable severity, mild to severe | Core feature — reported in essentially all PADDAS cases (9/9 in the reviewed case series) | HP:0001263 (Global developmental delay) / HP:0001249 (Intellectual disability) |
| Ataxia / gait disturbance | Motor | Onset with ambulation; progressive or static depending on series | ~6/9–11 in reviewed series; the defining motor feature, though the 2025 EMAtS case (PMID:40472467) explicitly lacked it | HP:0001251 (Ataxia) |
| Hypotonia | Motor | Early infancy | 8/9 in the Frontiers review | HP:0001252 (Hypotonia) |
| Seizures (multiple types — focal, absence, tonic-clonic, infantile spasms, myoclonic-atonic, status epilepticus) | Neurological | Onset range 3 months–5 years across reported cases; can present as West syndrome (PMID:30536491) or as Dravet-like/EMAtS phenotypes | Variable — "more variably" per OMIM/Orphanet framing; present in a minority-to-half depending on series, but a defining feature when present | HP:0001250 (Seizure); more specific: HP:0011097 (Epileptic spasm), HP:0007359 (Focal-onset seizure), HP:0002123 (Generalized myoclonic seizure) |
| Short stature / poor growth | Growth | Congenital–childhood | Reported in a subset, notably missense (not deletion) cases per PMID:29474920 | HP:0004322 (Short stature) |
| Cryptorchidism (males) | Genitourinary | Congenital | Reported in 2 of the original male PADDAS subjects | HP:0000028 (Cryptorchidism) |
| Facial dysmorphism: broad/wide nasal bridge, hypertelorism, almond-shaped eyes, high-arched palate, ptosis | Dysmorphology | Congenital, non-progressive | Variable, reported across multiple cases | HP:0000431 (Wide nasal bridge), HP:0000316 (Hypertelorism), HP:0000488 (Ptosis), HP:0000218 (High-arched palate) |
| Digit/limb anomalies | Skeletal | Congenital | Variable, less consistently reported | (Not specific enough to assign confidently — needs case-by-case review) |
| Behavioral abnormalities (hyperactivity, attention deficit) | Behavioral | Childhood | Reported in the 1p35 deletion series | HP:0000752 (Hyperactivity) |
| Brain MRI abnormalities: thin/hypoplastic corpus callosum, ventriculomegaly, posterior fossa abnormalities | Structural/imaging | Present from infancy | Reported in multiple cases (e.g., thin corpus callosum + enlarged temporal horns in the Dravet-like case) | HP:0002079 (Hypoplasia of the corpus callosum), HP:0002119 (Ventriculomegaly) |
| Adult-onset cerebellar ataxia (allelic PRCA/SCA47 end of spectrum) | Motor | Mid-life onset, incomplete penetrance | Single reported family | HP:0001251 (Ataxia), onset-qualified adult |
| Peripheral sensory neuropathy / paresthesia (phenotype-expansion report) | Sensory | Adult-onset | Single 2025 case (PMID:40211677), alongside mild ataxia | HP:0003390 (Aplasia/hypoplasia not applicable) — likely HP:0003401 (Paresthesia) |

*HPO IDs above are my best-recollection mapping and **should be independently verified against the current HPO release / OLS before any curation commit** — per the dismech term-validation contract, I have not run a live lookup for every one of these, and several (limb/digit anomaly, paresthesia) are genuinely uncertain rather than just unverified.

**Quality-of-life impact:** No disease-specific QOL instrument data (EQ-5D/SF-36/PROMIS) exists for PADDAS; impact is inferred from the severity of the developmental/motor/epilepsy phenotype rather than measured directly — this is an evidence gap, not an established null.

---

## 4. Genetic / Molecular Information

**Causal gene:** PUM1 (Pumilio RNA-binding family member 1), HGNC:9404, OMIM *607204, chr1p35.2.

**Variant spectrum (Gennarino 2018 and subsequent reports):**
- Large heterozygous deletions of 1p35.2 encompassing PUM1 (contiguous-gene deletions, 0.3–5.6 Mb; PUM1 is the shared minimal deleted region across independent patients)
- De novo missense variants, notably clustering in the C-terminal **PUM-HD** RNA-binding domain (e.g., p.Arg1139Trp; p.Arg1147Trp/c.3439C>T)
- De novo frameshift variants (e.g., p.Leu387Cysfs*13/c.1159delC — Marin et al. 2025, PMID:40472467; p.His61Glnfs*31/c.182dup — Xu et al. 2025, PMID:40211677, in the phenotype-expansion HSN case)
- Nonsense and splice-site variants reported across the smaller case literature

**Classification (ACMG/AMP):** De novo occurrence, absence from gnomAD, and the extreme LOF constraint of the gene (pLI=1, LOEUF=0.157) support pathogenic/likely pathogenic classification for truncating variants as a class; missense variants require functional stratification because — critically for this gene — **not all missense changes are equally deleterious**: the defining finding of PMID:29474920 is that specific missense alleles reduce PUM1 protein by only ~25% (PRCA-range) vs. ~50% (PADDAS-range, phenotypically equivalent to full haploinsufficiency). This means **variant classification here cannot rely on truncating-vs-missense heuristics alone; functional protein-level quantification in patient-derived cells was the actual basis for severity assignment** in the founding study.

**Allele frequency:** PADDAS-range and PRCA-range PUM1 variants are absent from gnomAD/ExAC/1000 Genomes population databases in all reported cases — consistent with de novo dominant disease in a highly constrained gene.

**Somatic vs. germline:** All reported variants are germline/constitutional; no somatic mosaic PUM1 disease has been reported to my knowledge.

**Functional consequence — the core mechanism:** **Loss of function / haploinsufficiency**, not gain of function or dominant-negative. This is unusually well-nailed down mechanistically for a rare NDD gene (see §6) — Gennarino et al. showed that reduced PUM1 protein dose is necessary and sufficient, with the degree of reduction (measured directly in patient-derived cells, not inferred) predicting phenotype severity.

**Modifier genes:** None validated in humans. The mouse work (PMID:25768905) establishes **ATXN1** dosage as the operative downstream modifier/effector, but this has not been tested as a human clinical modifier (see caveat in §2).

**Epigenetic information:** No PUM1-disease-specific DNA methylation/histone/chromatin data identified in the literature I searched — genuine absence of data, not a negative finding.

**Chromosomal abnormalities:** The 1p35.2 microdeletion allelic form (OMIM #617930) is the chromosomal-scale counterpart of point-mutation PADDAS and should be modeled as the **same mechanism at different variant granularity** rather than a separate disease — this is a design-decision-relevant lump call worth flagging explicitly in any KB entry (per the dismech convention of surfacing lump/split calls rather than silently choosing one).

---

## 5. Environmental Information

No environmental, lifestyle, or infectious contributing or triggering factor has been reported for PADDAS. Seizure exacerbation by fever is plausible by general pediatric-epilepsy precedent but I found no PADDAS-specific report of fever-sensitivity analogous to, e.g., Dravet syndrome's SCN1A fever-triggered pattern (the one Dravet-*like* case report explicitly labeled its resemblance as phenotypic, not a claim about a shared fever mechanism) — worth noting as an absence of evidence rather than evidence of absence, since the phenotype spectrum includes Dravet-like presentations.

---

## 6. Mechanism / Pathophysiology

**Causal chain (numbered, with explicit evidentiary basis at each step):**

1. **Heterozygous PUM1 loss-of-function variant or deletion** → reduces PUM1 protein abundance by ~25–50% depending on variant type, demonstrated directly in patient-derived cells (western blot quantification), not inferred (PMID:29474920, HUMAN_CLINICAL/patient-cell evidence).
2. **Reduced PUM1 (an RNA-binding translational repressor)** → **derepression of PUM1 target transcripts**, most notably **ATXN1** mRNA, whose 3′UTR PUM1 normally binds via its Pumilio homology domain (PUM-HD) 8-nucleotide recognition motif (UGUA-U/C-AUA) to promote transcript decay/translational repression (mechanistic/structural evidence, PMID:29474920 + PUM-HD structural literature, PMID:11336708). This step is **directly demonstrated** in the human paper via increased levels of known PUM1 targets tracking with the degree of PUM1 reduction.
3. **Elevated wild-type ATXN1 mRNA and protein** → this step was established first, and independently, in the **mouse model** (Gennarino et al. 2015, *Cell*, PMID:25768905, MODEL_ORGANISM evidence): Pum1+/− mice show increased Atxn1 mRNA and protein in cerebrum and cerebellum. This is the step where human and mouse evidence are stitched together — the mouse work established causality (Atxn1 dose ↑ → phenotype), the human work established that PUM1 variants reduce PUM1 dose sufficiently to trigger it.
4. **Wild-type Ataxin-1 accumulation in Purkinje cells** → drives **SCA1-like progressive neurodegeneration and motor dysfunction**, demonstrated genetically in mice by **epistasis**: crossing Pum1+/− mice to SCA1 (Atxn1^154Q/+) mice **worsened** disease, while crossing Pum1+/− mice to Atxn1+/− mice (halving Atxn1 dose) **normalized Ataxin1 levels and largely rescued the Pum1+/− phenotype** (PMID:25768905, direct quote-paraphrase of the rescue experiment) — this reciprocal dosage experiment is the strongest causal evidence in the whole mechanism and is worth citing as the anchor edge in any pathograph.
5. **In the more severely PUM1-reduced (haploinsufficiency-range, ~50%) human cases**, the same derepression occurs during **neurodevelopment** rather than in an already-formed adult nervous system, which the authors and subsequent reviewers interpret (an **inference**, not a directly demonstrated developmental mechanism in humans) as the reason the phenotype is a developmental encephalopathy (PADDAS: developmental delay, seizures, dysmorphism) rather than a pure adult-onset degeneration (PRCA/SCA47) — i.e., **timing and magnitude of PUM1 loss during development, not just magnitude alone, likely shapes phenotype**, though this developmental-timing claim is reasoned from the clinical dose-severity correlation rather than from a direct developmental time-course experiment in humans.
6. **Seizures and dysmorphic/growth features** in the PADDAS end of the spectrum are not mechanistically dissected to the same molecular depth as the ataxia/neurodegeneration arm — **I am not aware of literature identifying which specific PUM1 target transcripts (beyond ATXN1) drive the epilepsy or dysmorphism phenotypes**; this is a genuine mechanistic gap rather than settled biology, and any pathophysiology node modeling seizures or dysmorphism as directly downstream of ATXN1 dysregulation would be overreaching the evidence. PUM1 has a broad target network beyond ATXN1 (it "binds an extensive network of mRNAs" — general Pumilio-biology literature, not PADDAS-specific), so multi-target, ATXN1-independent contributions to the non-ataxia features are biologically plausible but unproven.

**Molecular pathway:** Post-transcriptional gene regulation — translational repression / mRNA decay via the PUF-domain RNA-binding mechanism; not a classical signaling cascade (no direct MAPK/mTOR/Wnt involvement reported for this disease mechanism).

**Protein domain/structure:** PUM1's Pumilio homology domain (PUM-HD) comprises eight tandem ~36-aa PUF repeats forming a crescent-shaped right-handed superhelix; each repeat recognizes one RNA base via a tripartite recognition motif, collectively specifying an 8-nt target sequence (PMID:11336708 and PUF-domain structural literature). Several reported pathogenic missense variants cluster in this domain, consistent with direct disruption of RNA-target engagement as the molecular lesion — though I have not found a paper directly co-crystallizing a disease variant with RNA to confirm binding loss biophysically; this is inferred from domain location, not structurally demonstrated per-variant.

**Cellular process:** Negative regulation of translation; mRNA decay (candidate GO terms: GO:0017148 negative regulation of translation; GO:0006402 mRNA catabolic process; GO:0003730 mRNA 3'-UTR binding).

**Cell types most implicated:** Cerebellar **Purkinje cells** (CL:0000121) — the site of Ataxin-1 accumulation and neurodegeneration in the mouse model and by inference in human ataxia; more broadly, developing cortical/cerebellar neurons for the developmental (PADDAS) phenotype, though this is inferred from phenotype rather than directly shown by cell-type-resolved human data.

**Molecular profiling:** The 2018 human paper and 2015 mouse paper together constitute targeted transcript/protein-level profiling (PUM1 target mRNA/protein quantification) rather than unbiased transcriptomic/proteomic screens; I did not find a published RNA-seq or single-cell dataset specifically profiling PADDAS patient tissue — this is a gap relative to the "Advanced Technologies" checklist, not an oversight in my search.

**Pleiotropy note (recent, 2025):** PUM1 also regulates **SNCA (alpha-synuclein)** 3′UTR isoforms, and PUM1 variants affecting RNA-binding capacity have been found in **Parkinson's disease** patients independent of the PADDAS/PRCA spectrum (Cabaj et al. 2025, *Cell Reports*, PMID:40815569). This is genuinely a separate, more recently discovered arm of PUM1 biology and phenotype — **not** part of the PADDAS/PRCA/SCA47 clinical spectrum as currently delineated, but relevant context for understanding PUM1 as a multi-target translational repressor whose dose affects several distinct neurological outcomes depending on which downstream target dominates in a given cell population. I'd flag this as adjacent-disease context rather than same-entry content, consistent with the "keep germline mechanism separate from distinct downstream disease" curation principle.

---

## 7. Anatomical Structures Affected

**Organ level:** Primary — central nervous system (cerebrum, cerebellum). Secondary — skeletal system (short stature, digit anomalies), genitourinary (cryptorchidism), craniofacial skeleton (dysmorphic features).

**Tissue/cell level:** Cerebellar Purkinje cells (CL:0000121) most specifically implicated via the ATXN1 mechanism; cortical/subcortical neurons more generally for the developmental encephalopathy phenotype (not cell-type-resolved in humans).

**Subcellular:** Cytoplasmic — PUM1 is a cytoplasmic RNA-binding protein acting at the mRNA/ribosome interface (GO Cellular Component candidates: GO:0005737 cytoplasm; GO:0010494 cytoplasmic stress granule, given general Pumilio-protein biology, though not PADDAS-specific).

**Localization/UBERON candidates:** Cerebellum (UBERON:0002037), cerebral cortex (UBERON:0000956), corpus callosum (UBERON:0002336, given the reported hypoplasia), lateral ventricle (UBERON:0002285, given ventriculomegaly). Findings are generally bilateral/symmetric based on reported imaging.

---

## 8. Temporal Development

**Onset:** PADDAS — congenital to early infantile (developmental delay recognized in infancy; seizure onset reported from 3 months to ~5 years across cases). PRCA/SCA47 — mid-life adult onset (the single reported family), with incomplete penetrance.

**Progression:** The mouse mechanistic work supports a **progressive neurodegenerative** component (progressive motor dysfunction in Pum1+/− mice), but the human PADDAS phenotype is better characterized as a **static-to-progressive developmental encephalopathy** — developmental delay and dysmorphism are present from infancy (not truly progressive), while ataxia/motor features may show a neurodegenerative trajectory analogous to the mouse and PRCA data. I have not found longitudinal human natural-history data adequate to firmly characterize PADDAS as "progressive" vs. "static" at the individual-patient level — this is an important open question for a natural history study, and I'd flag any KB "progression" field here as inferred from mechanism rather than from longitudinal human observation.

**Seizure course:** Variable and reported as manageable-to-refractory across cases; the 2025 EMAtS case achieved seizure control within one year with combination antiseizure medication plus dietary intervention (PMID:40472467) — a single case, not a treatment-response cohort statistic.

---

## 9. Inheritance and Population

**Epidemiology:** Orphanet lists prevalence as **<1/1,000,000** worldwide — essentially "count of published cases," not a modeled population estimate; **no incidence figure exists**. Total published cases across all reports (PADDAS + PRCA + deletion syndrome + phenotype-expansion reports) number roughly in the 30–40 range as of 2025, though I have not independently re-tallied every case report to give an authoritative count — treat this figure as an approximation from source-document impressions (e.g., humandiseasegenes.nl states the original description included ~20 patients "with additional cases subsequently reported").

**Inheritance pattern:** Autosomal dominant. PADDAS: essentially always de novo. PRCA/SCA47: autosomal dominant with **incomplete penetrance** (established in one family).

**Penetrance/expressivity:** PADDAS-range variants appear fully penetrant in reported cases (all carriers affected); PRCA-range variants show incomplete penetrance — mechanistically consistent with the milder (~25%) protein reduction sitting closer to a phenotypic threshold.

**Genetic anticipation, germline mosaicism, founder effects, consanguinity, carrier frequency:** None reported or mechanistically expected for this de novo dominant, non-repeat-expansion disorder (repeat-expansion phenomena like anticipation are a SCA1/polyQ feature, not a PUM1 feature — worth being precise that PADDAS/PRCA is **not** a polyglutamine repeat disease itself, even though its downstream effector, Ataxin-1, is the same protein mutated in the polyQ disease SCA1).

**Population demographics:** Reported cases span multiple ancestries/countries (Australia, Canada, US, Belgium, Taiwan, Brazil, China per the geographic spread of cited case reports); no specific ethnic enrichment or geographic clustering has been reported. Sex ratio: no clear skew apparent from the small case literature (both sexes reported; cryptorchidism obviously only assessable in males).

---

## 10. Diagnostics

**Genetic testing (primary diagnostic route):** Given the mixed variant spectrum (point mutations to multi-Mb deletions), the practical diagnostic approach combines:
- **Trio-based exome or genome sequencing** (WES/WGS) — the modality used in essentially every recent single-case report (e.g., PMID:40472467, PMC8978559) and the appropriate first-tier test for an undiagnosed developmental-and-epileptic-encephalopathy phenotype where PUM1 would not typically be suspected a priori.
- **Chromosomal microarray (CMA)** — necessary to detect the deletion-class allelic variants (1p35.2 microdeletions, OMIM #617930); a diagnosis reached by exome sequencing alone could miss the deletion end of the spectrum, and CMA specifically was how several of the founding cohort's patients were ascertained.
- **Single-gene/panel testing** is reasonable once PUM1 is specifically suspected (e.g., in a patient with developmental delay + ataxia +/- seizures + dysmorphism), but given the rarity and recent delineation of this gene-disease relationship, most patients will be ascertained via exome-first strategies in a broader NDD/epilepsy gene panel or WES/WGS diagnostic odyssey.
- I found **no GTR-listed PUM1-specific single-gene test count** to cite with confidence — not searched to completion, flagging as unverified rather than absent.

**Clinical/imaging:** Brain MRI is a standard part of the diagnostic workup given the reported structural findings (thin corpus callosum, ventriculomegaly, posterior fossa abnormality) — useful for phenotype characterization, not diagnostic in itself. EEG is essential given the epilepsy component, with reported patterns including diffuse slowing, multifocal spikes, and focal slow waves.

**Differential diagnosis:** Given phenotypic overlap, PADDAS should be considered in the differential for: Dravet syndrome (SCN1A) — explicitly raised by the 2022 case report title; early infantile epileptic encephalopathies more broadly; other causes of developmental and epileptic encephalopathy with ataxia (e.g., CACNA1A-related disorders, STXBP1-related disorders); and other 1p35-region contiguous gene deletion syndromes when CMA identifies a deletion rather than a point variant.

**Genetic counseling:** De novo inheritance in PADDAS means recurrence risk to future siblings of an affected proband is low but not zero (germline mosaicism theoretically possible, though not specifically documented for PUM1); for PRCA-range variants, autosomal dominant transmission with incomplete penetrance requires careful counseling about variable expressivity within a family.

**Screening:** No newborn or population screening applies to an ultra-rare de novo dominant condition of this kind.

---

## 11. Outcome / Prognosis

No survival, mortality, or life-expectancy data specific to PADDAS have been published (this is not reported as a life-limiting condition in the available literature, but absence of mortality data is not the same as an established normal-life-expectancy claim — genuine gap). Morbidity is driven by the combination of intellectual disability, motor impairment/ataxia, and — when present — epilepsy severity/refractoriness. No validated prognostic biomarker exists; the closest analog is the **PUM1 protein-level reduction itself**, which in the founding study directly tracked with phenotypic severity (25% → adult-onset ataxia; 50% → infantile developmental syndrome) — this is arguably the single most prognostically informative data point in the literature, though it requires patient-derived cell functional assay rather than being inferable from variant type alone.

---

## 12. Treatment

**No PUM1/PADDAS-specific approved therapy exists.** Management is symptomatic and multidisciplinary, following general principles for developmental and epileptic encephalopathies:

- **Antiseizure medication** — individualized based on seizure semiology; the one detailed 2025 case achieved control with a combination regimen (levetiracetam-class agents implied by the broader literature; the EMAtS case specifically used antiseizure medication plus **dietary intervention**, i.e., presumably a ketogenic-type diet given EMAtS/myoclonic-atonic seizure management conventions — PMID:40472467) — NCIT:C15986 (Pharmacotherapy) + NCIT:C15447 (Dietary Intervention) as candidate treatment-term bindings.
- **Physical therapy / occupational therapy / speech therapy** for motor and developmental support — NCIT:C15302 (Physical Therapy).
- **Genetic counseling** — NCIT:C15240.
- **Developmental early-intervention services** generally.

**Mechanism-informed therapeutic direction (research-stage, not clinical):** Because the pathophysiology is a well-characterized **ATXN1-dosage** problem, and **antisense oligonucleotide (ASO)-mediated ATXN1 lowering** is an actively developed therapeutic strategy for the allelic polyQ disease SCA1 (with documented safety and efficacy in SCA1 mouse models — PMID for the ASO safety assessment and JCI Insight ASO efficacy paper were identified in search but I have not independently verified their PMIDs to the same standard as the core PADDAS citations above, so I withhold precise PMID citation here pending confirmation), an ATXN1-lowering ASO is a **biologically plausible but currently unproven** therapeutic avenue for the ataxia component of PUM1-related disease specifically. **I want to be explicit that no PUM1/PADDAS-specific ASO trial or preclinical rescue publication was identified in my search** — this is my own mechanistic inference bridging two literatures (PUM1↔ATXN1 biology and SCA1 ASO therapeutics), not a reported treatment strategy, and should be labeled as such if it enters any KB `discussions`/hypothesis field rather than presented as an established `treatments` entry.

---

## 13. Prevention

Not applicable in the primary-prevention sense (de novo dominant disorder with no known environmental trigger). Secondary prevention is limited to prenatal/preimplantation genetic testing once a familial variant is known (relevant chiefly to the incompletely penetrant PRCA families rather than de novo PADDAS). No specific public-health, prophylactic, or vaccination consideration applies.

---

## 14. Other Species / Natural Disease

No naturally occurring PUM1-associated disease has been reported in companion animals or wildlife (no OMIA entry identified in my search). The relevant cross-species biology is entirely **experimentally induced** in laboratory mice (see §15) rather than naturally occurring veterinary disease. PUM1 orthologs are broadly conserved (Drosophila *pumilio*, the founding member of the gene family, discovered for its role in posterior body patterning and germline stem cell maintenance — general Pumilio-family developmental biology, not disease-specific), reflecting deep evolutionary conservation of PUF-domain RNA regulation, but this conservation is a structural/functional fact rather than evidence of a naturally occurring animal phenocopy of PADDAS.

---

## 15. Model Organisms

**Mouse — the dominant and mechanistically load-bearing model:**
- **Pum1+/− (heterozygous) mice** — the direct genetic model of human haploinsufficiency — show increased Atxn1 mRNA/protein in cerebrum and cerebellum and progressive motor dysfunction (PMID:25768905). This is a **high-fidelity model for the ataxia/neurodegeneration arm** of the human spectrum specifically because the epistasis experiments (crossing to Atxn1+/− mice to normalize Atxn1 dose) directly demonstrate the same causal mechanism proposed in humans — this is about as strong as model evidence gets for a human haploinsufficiency mechanism, and I'd rate it fidelity: HIGH for the *ataxia/Purkinje cell degeneration* claim specifically, while noting the mouse model has **not**, to my knowledge, been reported to recapitulate the human developmental/dysmorphism/seizure phenotype — that translational gap (model_scale: molecular/cellular readouts in mice vs. the full developmental encephalopathy phenotype in human PADDAS) should be recorded as a limitation if this model is linked to non-ataxia pathophysiology nodes.
- **Complete Pum1 knockout mice** exist in the broader Pumilio literature (used to study body size/Cdkn1b regulation, PMC6444939, and neurogenesis, genesdev.cshlp.org/content/31/13/1354) but these studies address distinct aspects of PUM1 biology (body size, neurogenesis) rather than the PADDAS/ataxia phenotype specifically — useful as mechanistic context for PUM1's broader developmental role, not as a direct PADDAS disease model.

**Cell-based/patient-derived models:** Patient-derived cells (fibroblasts/lymphoblastoid lines, per PMID:29474920) were the actual system used to quantify the 25%/50% PUM1 protein reduction that anchors the whole severity-dosage claim — this is IN_VITRO evidence and is arguably more directly disease-relevant than the mouse model for the dose-quantification claim, even though the mouse model carries the causal (epistasis) demonstration.

**Limitations:** No iPSC-derived neuron or cerebral organoid model of PUM1 haploinsufficiency was identified in my search — a plausible next-generation model given the field's general move toward iPSC-neuron systems for NDD mechanism work, but its absence here is a real gap rather than an oversight in searching.

---

## Summary of Evidentiary Confidence

| Claim | Confidence / evidence type |
|---|---|
| PUM1 haploinsufficiency causes PADDAS/PRCA spectrum | **High** — human genetic (de novo, constraint) + direct protein quantification + mouse mechanistic causality with epistasis rescue |
| ATXN1 dosage is the operative downstream effector for the ataxia component | **High for mouse mechanism; inferred (not directly shown) for human developmental phenotype** |
| Deletion and point-mutation forms are the same disease mechanism | **Moderate-high** — supported by minimal-overlap-region logic across 9 deletion patients, not by a head-to-head functional comparison |
| Non-ataxia features (seizures, dysmorphism, growth) mechanism | **Low** — no specific target transcript or pathway identified beyond general PUM1 pleiotropy |
| Progressive vs. static natural history in humans | **Low** — inferred from mouse progression data, not established longitudinally in patients |
| ASO/ATXN1-lowering as a PADDAS therapeutic strategy | **Speculative** — my own cross-literature inference, not a reported PADDAS-specific therapeutic study |

---

### Sources

- [A Mild PUM1 Mutation Is Associated with Adult-Onset Ataxia, whereas Haploinsufficiency Causes Developmental Delay and Seizures (Gennarino et al., Cell 2018)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5832058/) — PMID:29474920
- [Pumilio1 Haploinsufficiency Leads to SCA1-like Neurodegeneration by Increasing Wild-Type Ataxin1 Levels (Gennarino et al., Cell 2015)](https://pubmed.ncbi.nlm.nih.gov/25768905/) — PMID:25768905
- [Investigating PUM1 mutations in a Taiwanese cohort with cerebellar ataxia](https://pubmed.ncbi.nlm.nih.gov/31422002/) — PMID:31422002
- [PUM1 haploinsufficiency is associated with syndromic neurodevelopmental delay and epilepsy (Voet et al., AJMG 2020)](https://pubmed.ncbi.nlm.nih.gov/31859446/) — PMID:31859446
- [A de novo PUM1 Variant in a Girl With a Dravet-Like Syndrome: Case Report and Literature Review](https://pmc.ncbi.nlm.nih.gov/articles/PMC8978559/) — PMID:35386260
- [A new developmental and epileptic encephalopathy: PUM1-neurodevelopmental disorder with epilepsy with myoclonic-atonic seizures (Marin et al., Seizure 2025)](https://www.sciencedirect.com/science/article/abs/pii/S1059131125001335) — PMID:40472467
- [PUM1 regulation of SNCA/alpha-synuclein (Cabaj et al., Cell Reports 2025)](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:40815569) — PMID:40815569
- [Hereditary sensory neuropathy PUM1 phenotype expansion (Xu et al., J Peripher Nerv Syst 2025)](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:40211677) — PMID:40211677
- [De novo 1p35.2 microdeletion including PUM1 in sporadic West syndrome](https://pubmed.ncbi.nlm.nih.gov/30536491/) — PMID:30536491
- [OMIM #620719 — NEDMSF](https://www.omim.org/entry/620719)
- [OMIM *607204 — PUM1](https://omim.org/entry/607204)
- [OMIM #617930 — Chromosome 1p35 deletion syndrome](https://omim.org/entry/617930)
- [Orphanet: PUM1-associated developmental disability-ataxia-seizure syndrome (ORPHA:589515)](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=589515)
- [Orphanet: PUM1-related cerebellar ataxia](https://www.orpha.net/en/disease/detail/642747)
- [Human Disease Genes — PUM1 (professional summary)](https://humandiseasegenes.nl/pum1/professionals)
- [Global Genes — PADDAS disorder page](https://globalgenes.org/disorder/pum1-associated-developmental-disability-ataxia-seizure-syndrome/)
- [gnomAD browser — PUM1 constraint metrics](https://gnomad.broadinstitute.org/gene/ENSG00000134644)
- [Crystal structure of a Pumilio homology domain](https://pubmed.ncbi.nlm.nih.gov/11336708/)
- [Chromodisorder.org — 1p35 deletion and PUM1 mutation](https://chromodisorder.org/cdo-news/1p35-deletion-and-pum1-mutation/)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 13 |
| On topic | 7 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMID:29474920`: "protein levels track with phenotypic severity"
  - closest text in source: "Changes in protein levels thus track with phenotypic severity, and identifying posttranscriptional modulators of protein expression should identify new candidate disease genes"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 39 |
| Resolved | 34 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 5 |
| Terms whose name was checked | 9 |
| Terms named correctly | 9 |
| Terms named as a **different** term | 0 |

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `EXT_ID`.

34 of 39 terms resolved to a current term; the rest could not be looked up either way.