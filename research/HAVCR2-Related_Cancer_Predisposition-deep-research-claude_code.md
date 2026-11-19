---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-03T19:18:34.635953'
end_time: '2026-11-03T19:21:20.657275'
duration_seconds: 166.02
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: HAVCR2-Related Cancer Predisposition
  mondo_id: MONDO:1060169
  category: Mendelian
  causal_genes: HAVCR2
  omim_id: not recorded
  synonyms: HAVCR2-related SPTCL and/or HLH predisposition; HAVCR2-related subcutaneous
    panniculitis-like T-cell lymphoma and/or hemophagocytic lymphohistiocytosis predisposition
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
  web_search_requests: 6
  num_turns: 13
  total_cost_usd: 2.0120071
  session_id: fc2fc303-17fd-4674-997d-d801c0a7522b
  stop_reason: end_turn
  permission_denials: 1
  denied_tools:
  - Bash
  assistant_text_blocks: 2
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderAuthError
  status_code: 403
  remedy: the API key is missing, invalid, or lacks access to this endpoint
  retryable: false
- provider: claude_code
  succeeded: true
citation_count: 12
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 16
  on_topic: 10
  validator_version: 0.5.1
term_validation:
  total_terms: 19
  verified: 17
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_variant: 1
  unresolvable_prefixes:
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** HAVCR2-Related Cancer Predisposition
- **MONDO ID:** MONDO:1060169 (if available)
- **Causal gene(s):** HAVCR2
- **OMIM:** not recorded
- **Synonyms:** HAVCR2-related SPTCL and/or HLH predisposition; HAVCR2-related subcutaneous panniculitis-like T-cell lymphoma and/or hemophagocytic lymphohistiocytosis predisposition
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **HAVCR2-Related Cancer Predisposition** covering all of the
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

Found the ClinGen row (Moderate, AR, 2025-06-10). Now searching the literature for the remaining sections.

# HAVCR2-Related Cancer Predisposition (MONDO:1060169): research report

> **What this is.** This report was put together from three sources: the evidence snippets already quoted in this repository (`kb/disorders/Subcutaneous_Panniculitis-like_T-cell_Lymphoma.yaml`, whose references are cached and verified), the committed ClinGen export, and a short web search. **Every ontology CURIE below except MONDO:1060169, hgnc:18437 and the ClinGen assertion is a lead written from memory.** None has been looked up. Each needs a `runoak` or cache lookup before it goes into YAML. PMIDs marked **[unverified]** were not checked against PubMed in this session.

---

## 1. Disease information

**Definition.** This is an autosomal recessive germline predisposition caused by loss-of-function missense variants in **HAVCR2** (hgnc:18437), which encodes the inhibitory immune checkpoint receptor TIM-3. Carriers are predisposed to two conditions:
- **subcutaneous panniculitis-like T-cell lymphoma (SPTCL)**
- **hemophagocytic lymphohistiocytosis (HLH)**, which can occur with SPTCL or without any lymphoma.

**Key identifiers**

| Resource | Identifier | Status |
|---|---|---|
| MONDO | MONDO:1060169 "HAVCR2-related cancer predisposition" | Confirmed (stub plus scaffolded entry). MONDO parent: MONDO:0015356 *hereditary neoplastic syndrome* |
| HGNC | hgnc:18437 HAVCR2 | Confirmed (`cache/hgnc/terms.csv`) |
| ClinGen | `CGGV:assertion_1ea863f9-c3e9-4b1a-95c4-ef2eb2444bbd-2025-06-10T160000.000Z` | Confirmed. Structured database row: "HAVCR2 \| HGNC:18437 \| HAVCR2-related cancer predisposition \| MONDO:1060169 \| AR \| … Moderate". Curated by the Childhood, Adolescent and Young Adult Cancer Predisposition GCEP on 2025-06-10 |
| OMIM (phenotype) | None recorded (matches the template) | The gene MIM is believed to be 606652 **[unverified]** |
| Orphanet, ICD-10/11, MeSH | No predisposition-specific code found | SPTCL has ICD-O 9708/3 (lead) |

**Synonyms:** HAVCR2-related SPTCL and/or HLH predisposition; germline TIM-3 deficiency; "HLH-SPTCL" (the term proposed by Gayden et al.).

**Source class.** All of this is aggregated from cohort and case-series literature and from ClinGen. None of it comes from EHR data.

**Lump/split call to surface.** `kb/disorders/Subcutaneous_Panniculitis-like_T-cell_Lymphoma.yaml` already exists and already carries the HAVCR2 evidence.
- Under design decisions §3a, the germline syndrome (this entry) should stay separate from the somatic neoplasm entry.
- This entry should own: the germline genotype, inheritance, penetrance, lymphoma-free HLH, and surveillance.
- The SPTCL entry should own: tumor histology and somatic drivers.
- Whether "HAVCR2-related idiopathic HLH" should be a `has_subtypes` row here or a separate primary-HLH entry is still an open question. I recommend a subtype row here. The stub's `entry_type` is UNDECIDED, and it should be set to `DISEASE`.

## 2. Etiology

**Cause.** Germline biallelic (and, less clearly, monoallelic) HAVCR2 missense variants.
- Primary literature, Gayden et al., Nat Genet 2018, **PMID:30374066**: *"We identify in ~60% of SPTCL cases germline, loss-of-function, missense variants altering highly conserved residues of TIM-3, c.245A>G (p.Tyr82Cys) and c.291A>G (p.Ile97Met), each with specific geographic distribution."*
- Primary literature, Polprasert et al., Blood Adv 2019, **PMID:30792187**: *"individuals harboring biallelic HAVCR2 (TIM3) germline mutations were highly susceptible to sporadic SPTCL, which was also associated with clonal somatic mutations."*

**Genetic modifiers of the HLH phenotype.**
- Multicenter cohort plus individual-patient-data meta-analysis, **PMID:37051767** (Moonla et al., Haematologica 2023, per the web search): *"male sex, heterozygous and homozygous/compound heterozygous HAVCR2 mutations were associated with HLH by the adjusted odds ratio of 2.93 (95% CI: 1.22-7.06), 4.77 (95% CI: 1.05-21.63) and 8.48 (95% CI: 2.98-24.10), respectively."*
- So genotype dosage and male sex both modify HLH risk.

**Environmental triggers.** No exposure has been shown to cause disease. EBV has been reported alongside HAVCR2-associated EBV+ PTCL-NOS with HLH (Frontiers in Oncology 2022, doi:10.3389/fonc.2022.870676, case report). That is a lead and does not establish a trigger.

**Protective factors and gene–environment interactions:** none documented.

## 3. Phenotypes

All of the HPO IDs in this table are leads and must be looked up.

| Phenotype | HPO lead | Frequency / characteristics | Source |
|---|---|---|---|
| Subcutaneous nodules / plaques (trunk, limbs) | HP:0001482 Subcutaneous nodule | Typical presenting sign of SPTCL | PMID:35509196: *"painless subcutaneous and erythematous nodules over the trunk or extremities"*. PMID:30126736: *"multiple nodular or plaque-like lesions preferentially affecting the legs and/or trunk"* (these describe SPTCL in general, not genotyped cohorts) |
| Lobular panniculitis with adipocyte rimming | HP:0012490 Panniculitis | Defining histology | PMID:34535012: *"CD8-positive T cells infiltrating into subcutaneous adipose tissue, with rimmed individual fat cells in a lace-like pattern"* |
| T-cell lymphoma (SPTCL) | HP:0012190 T-cell lymphoma | ~60% of SPTCL carry germline variants (Gayden). 86.4% in a 22-patient cohort (PMID:39538229: *"86.4% harbored germline HAVCR2 mutation, either homozygous (77.3%) or heterozygous (9.1%) p.Y82C variant"*) | PMID:30374066, PMID:39538229 |
| HLH / HLH-like systemic illness (fever, cytopenias, ferritin ≥500, BM hemophagocytosis) | HP:0012156 Hemophagocytosis; HP:0001945 Fever; HP:0001876 Pancytopenia; HP:0003281 Increased serum ferritin; HP:0001433 Hepatosplenomegaly | 68.2% in PMID:39538229. Homozygous Y82C: 75.0% with HLH vs 44.4% without (PMID:37051767) | PMID:37051767, PMID:39538229 |
| HLH without lymphoma ("idiopathic HLH") | as above | 4 of 65 adult HLH cases in a Thai series (Boonyabaramee et al., Exp Hematol 2023; PMID **[unverified]**) | web lead |
| Recurrent myocarditis (single homozygous patient) | HP:0012819 Myocarditis | Case-level | lead from PMC6452640 (TIM-3 review), not checked against the primary source |

**Onset (pediatric framing).**
- In a Korean cohort, Y82C was associated with younger age. PMID:34535012: *"HAVCR2Y82C was associated with younger age (P = .001), development of hemophagocytic lymphohistiocytosis or hemophagocytic lymphohistiocytosis-like systemic illness (P < .001), and short relapse-free survival"*.
- In that cohort the median age was 32 (range 8–74). The genotype-unstratified series PMID:30126736 had a median age of 46.5.
- Childhood and adolescent onset is reported, which is consistent with ClinGen's CAYA GCEP scope. I found no age-specific penetrance curve.

**Severity and course.** SPTCL alone runs an indolent, relapsing course. HLH is the main source of severity and death.

**Quality of life:** no instrument-based data found.

## 4. Genetic / molecular information

**Recurrent variants**

| Variant | Notes |
|---|---|
| **p.Tyr82Cys (c.245A>G)** | Founder-type allele in East Asian and Polynesian populations (Gayden: "specific geographic distribution"). Polprasert: *"Ten patients harbored homozygous p.Y82C mutations, and 1 showed compound heterozygous mutations (p.Y82C and p.T101I)"* (PMID:30792187) |
| **p.Ile97Met (c.291A>G)** | Reported mainly in patients of European ancestry (Gayden) |
| p.Thr101Ile | Seen in compound heterozygosity with Y82C (PMID:30792187) |

**Variant type and mechanism.** Missense, loss of function, through misfolding and loss of TIM-3 from the cell surface. PMID:30374066: *"Both variants induce protein misfolding and abrogate TIM-3's plasma membrane expression."* Y82 and I97 lie in the IgV domain.

**Origin.** Germline. The tumors also acquire somatic mutations. PMID:30792187: *"SPTCL cells also harbored somatic mutations (6.2 per patient) … in genes associated with epigenetic regulation and signal transduction."*

**Inheritance.** ClinGen records AR. Heterozygotes are over-represented in HLH (OR 4.77), so a dosage effect or incomplete penetrance in heterozygotes is unresolved. The ClinVar classifications and gnomAD allele frequencies for Y82C and I97M **were not retrieved**.

**Epigenetics and chromosomal abnormalities:** none disease-specific.

## 5. Environmental information

No established environmental, lifestyle or infectious cause. EBV co-occurrence is a single case-level lead (see §2).

## 6. Mechanism / pathophysiology

**Causal chain**

1. Biallelic germline HAVCR2 missense variant (Y82C / I97M) **leads to** misfolding of the TIM-3 IgV domain. *(Demonstrated, PMID:30374066, in vitro.)*
2. Misfolded TIM-3 **results in** loss of its plasma membrane expression on T cells and myeloid cells. *(Demonstrated, PMID:30374066.)*
3. Loss of the inhibitory checkpoint **leads to** persistent T-cell and macrophage activation. *(Demonstrated in patient cells, PMID:30374066.)*
4. Persistent activation **results in** excess TNF-α and IL-1β. PMID:30374066: *"persistent immune activation and increased production of inflammatory cytokines, including tumor necrosis factor-α and interleukin-1β, promoting HLH and SPTCL."*
5. **Branch A, HLH:** the cytokine excess **leads to** macrophage activation and hemophagocytosis, which causes fever, cytopenias, hyperferritinemia and organomegaly. *(Supported by association data, PMID:37051767. Each step to the clinical picture is inferred.)*
6. **Branch B, lymphoma:** chronic activation of CD8+ αβ T cells in subcutaneous fat, combined with acquired somatic hits in epigenetic and signaling genes (PMID:30792187), **leads to** clonal SPTCL. *(Ordering the germline and somatic events this way is an inference.)* Y82C tumors show IL6-JAK-STAT3 and TNF-α/NF-κB signatures. PMID:34535012: *"HAVCR2Y82C SPTCLs were enriched in genes involved in IL6-JAK-STAT3 signaling and in tumor necrosis factor-α signaling via NF-κB."*

**Ontology leads (unverified)**
- GO: negative regulation of T cell activation (loss of); tumor necrosis factor production; interleukin-1 beta production; inflammatory response; protein folding.
- CL: CD8-positive, alpha-beta T cell (CL:0000625); macrophage (CL:0000235); adipocyte (CL:0000136).

## 7. Anatomical structures

- **Primary:** subcutaneous adipose tissue (trunk, limbs).
- **Systemic (HLH):** bone marrow, liver, spleen.
- **Subcellular:** plasma membrane (TIM-3 is lost from it) and endoplasmic reticulum (where misfolded protein is retained; this is inferred).

UBERON leads, unverified: subcutaneous adipose tissue, bone marrow, liver, spleen.

## 8. Temporal development

- Onset ranges from childhood to adulthood and is earlier with Y82C (PMID:34535012).
- SPTCL tends to relapse. Y82C is associated with shorter relapse-free survival (PMID:34535012).
- HLH flares are episodic.
- I found no data on critical periods.

## 9. Inheritance and population

- **Inheritance:** AR (ClinGen). HLH risk scales with genotype dosage.
- **Founder effects:** Y82C in East Asia and Polynesia; I97M in Europeans (PMID:30374066).
- **Population frequencies:**
  - About 85% of sporadic Asian SPTCL versus 25% of French cases. This figure comes from a secondary review found in the web search, not from a primary source.
  - 77.3% Y82C homozygous in a Thai/Asian cohort (PMID:39538229).
- **Sex:** SPTCL shows female predominance: *"37 (69.8%) patients were women"* (PMID:34535012). Male sex, however, raises HLH risk (PMID:37051767).
- **Prevalence:** not established. SPTCL itself is *"<1% of all NHL cases worldwide"* (PMID:39538229).

## 10. Diagnostics

- **Histology** of a skin or subcutaneous biopsy: lobular panniculitis with adipocyte rimming by CD3+CD8+CD56− TIA-1+ βF1+ cells (PMID:30126736, PMID:17934071).
- **HLH workup:** HLH-2004 criteria, ferritin, bone-marrow examination. PMID:37051767 defines "HLH-like systemic illness" for cases that only partly meet the criteria.
- **Genetic testing:** targeted HAVCR2 sequencing (Y82C/I97M) or an HLH/immune-dysregulation panel. HAVCR2 should be on primary-HLH panels for adults with idiopathic HLH (Boonyabaramee 2023 lead). Exome or genome sequencing is appropriate when panels are negative.
- **Differential diagnosis:** lupus panniculitis; primary cutaneous γδ T-cell lymphoma (poor prognosis; PMID:17934071 split SPTL-AB from γδ cases); familial HLH genes (PRF1, UNC13D, STX11, STXBP2).
- **Cascade testing** of siblings is reasonable under AR inheritance. No guideline was found.

## 11. Outcome / prognosis

- SPTCL with αβ phenotype has a 5-year OS of 82%, or 91% without HPS versus 46% with HPS (PMID:17934071, genotype-unstratified).
- PMID:15368328: *"The presence of HPS at diagnosis … associated with poor survival."*
- Conflicting signal: a Thai series reports that HLH associated with germline HAVCR2 had better survival than other adult HLH ("Good prognosis…", Exp Hematol 2023; PMID **[unverified]**).

## 12. Treatment

Evidence here is case-series level only. NCIT term leads, unverified: Pharmacotherapy NCIT:C15986, Chemotherapy NCIT:C15632, Hematopoietic Cell Transplantation NCIT:C15431.

- **Immunosuppression first:** corticosteroids plus cyclosporine (Blood Adv letter on a compound-heterozygous patient, found in the web search). In the 22-patient cohort, 36.4% received immunosuppressive therapy first line (PMID:39538229).
- **JAK inhibition:** ruxolitinib, alone or with the DEP regimen, in HLH (5-case series, Front Immunol 2023, doi:10.3389/fimmu.2023.1271324).
- **IL-6 blockade:** reported in that same series.
- **IL-1 blockade (anakinra):** biologically plausible given excess IL-1β, but **I found no case data**.
- **Chemotherapy (CHOP-like) and allo-HSCT:** used for refractory disease. No comparative data.
- **Clinical trials:** no HAVCR2-specific NCT was found.
- **Iatrogenic concern:** anti-TIM-3 checkpoint antibodies (e.g., sabatolimab, cobolimab) would phenocopy the defect. That is an inference; no reported cases.

## 13. Prevention

There is no primary prevention. Possible measures:
- Genetic counseling and cascade testing of siblings (AR, 25% recurrence risk).
- Clinical surveillance for panniculitis and HLH in genotype-positive relatives.
- Avoiding TIM-3 blockade in carriers.

All of these are inferred. No published surveillance protocol was found.

## 14. Other species

No naturally occurring HAVCR2 disease was found in OMIA (OMIA was not searched directly). The mouse ortholog is Havcr2 (MGI allele record MGI:2680763 exists).

## 15. Model organisms

- **Havcr2-null mice:** viable. Earlier work showed TIM-3 inhibits Th1 auto- and alloimmunity and is needed for tolerance (Sanchez-Fueyo et al., Nat Immunol 2003, PMID:14556005, per a Proteopedia citation **[unverified]**). A vendor page says the null mouse has no spontaneous autoimmunity. That is uncited and would need checking.
- **No Y82C or I97M knock-in mouse was found.** A TIM-3 review (PMC6452640) says such mice still need to be studied.
- **Human-model mismatch:** knockout mice are not reported to develop SPTCL or HLH spontaneously. That fits a `HUMAN_MODEL_MISMATCH` discussion.
- **In vitro:** variant overexpression and folding/trafficking assays, plus patient T cells and monocytes (PMID:30374066).

---

### Gaps (acknowledged, not smoothed over)
- Not retrieved: gnomAD frequencies, ClinVar classifications, penetrance in Y82C homozygotes from population data.
- PMIDs not checked: Sonigo et al. (Blood 2020, "HAVCR2 mutations are associated with severe hemophagocytic syndrome in SPTCL"; found only as a HAL record) and Boonyabaramee et al. (Exp Hematol 2023).
- No data found on anakinra treatment, Y82C knock-in models, or surveillance guidelines.

Sources:
- [Frontiers in Oncology 2022, HAVCR2 EBV+ PTCL-NOS with HLH](https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2022.870676/full)
- [Haematologica: Moonla et al.](https://haematologica.org/article/view/haematol.2022.282419/76103)
- [Polprasert et al., Blood Adv 2019 (PMC6391671)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6391671)
- [Good prognosis of adult HLH with germline HAVCR2 (Exp Hematol 2023)](https://prod.sdgresources.relx.com/node/18884)
- [Case report: HAVCR2-associated HLH (Front Immunol 2023)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10701531/)
- [OJRD 2024 SPTCL cohort](https://biomedcentral-ojrd.publicaciones.saludcastillayleon.es/articles/10.1186/s13023-024-03438-w)
- [TIM-3 review (PMC6452640)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6452640)
- [MGI Havcr2 allele](https://informatics.jax.org/allele/MGI:2680763)
- [Sanchez-Fueyo 2003, Nat Immunol](https://www.nature.com/articles/ni987)
- [Proteopedia citation for PMID:14556005](https://proteopedia.org/w/5f71)
- [HAL record: Sonigo et al.](https://integ04-cnspfv.archimed.fr/doc/OAI_1/oai-HAL-hal-02882288v1)
- [Institut Imagine summary of Gayden et al.](https://www.institutimagine.org/en/germline-havcr2-mutations-altering-tim-3-characterize-subcutaneous-panniculitis-t-cell-lymphomas)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 16 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 19 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 1 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000625` (1 mention) - the report calls it "CL: CD8-positive, alpha-beta T cell"; CL calls it **CD8-positive, alpha-beta T cell**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`.

17 of 19 terms resolved to a current term; the rest could not be looked up either way.