---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-14T13:42:57.838313'
end_time: '2026-10-14T13:45:18.979567'
duration_seconds: 141.14
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: AARS1-related Leukoencephalopathy
  mondo_id: MONDO:1010132
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
  web_search_requests: 4
  num_turns: 12
  total_cost_usd: 1.7951013
  session_id: d7ee1ff7-8ca7-4d79-af15-153107eb33b3
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  assistant_text_blocks: 2
citation_count: 13
reference_validation:
  total_references: 15
  verified: 15
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 7
  quotes_valid: 6
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:34446925
  relevance_assessed: 15
  on_topic: 7
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 54
  verified: 52
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 9
  labels_matching: 5
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: DOID:0080451
    reported_labels:
    - DOID
    ontology_label: developmental and epileptic encephalopathy 29
  - term_id: HP:0001257
    reported_labels:
    - Spasticity / hypertonia, hyperreflexia
    ontology_label: Spasticity
  labels_variant: 2
  unresolvable_prefixes:
  - ORPHA
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** AARS1-related Leukoencephalopathy
- **MONDO ID:** MONDO:1010132 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **AARS1-related Leukoencephalopathy** covering all of the
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

I'm writing the final report now. First, a quick check of one variant name in the cached 2023 paper.

# AARS1-related Leukoencephalopathy (MONDO:1010132): Research Report

**Prepared:** 2026-10-14
**How sources were checked.** Most claims below come from abstracts or full texts cached locally in `references_cache/` for the draft entry `kb/disorders/AARS1-related_Leukoencephalopathy.yaml`. I re-read each one this session. A few identifiers and recent papers came from web search only. Those are marked **[web, not cached]**, and they need `just fetch-reference` before anyone uses them as evidence. Where a quote is shown, it is copied from the cached text.

---

## 1. Disease Information

**Overview.** AARS1-related leukoencephalopathy is a disorder of the central nervous system's white matter. It is caused by defects in AARS1, the cytoplasmic alanyl-tRNA synthetase (AlaRS). This enzyme attaches alanine to tRNA^Ala and also proofreads the product, removing serine or glycine attached by mistake. The disease is a spectrum:

1. **Early-infantile form (DEE29).** Biallelic, autosomal recessive variants cause an epileptic encephalopathy that starts in early infancy. Features include deficient or persistently delayed myelination, progressive microcephaly, spasticity, peripheral neuropathy and clubfoot (PMID:25817015, PMID:28493438).
2. **Later-onset recessive form.** Onset is after the first year of life. MRI shows a progressive leukoencephalopathy that starts in the posterior white matter and later reaches the frontal white matter. Decline is rapid (PMID:34446925).
3. **Adult-onset forms with axonal spheroids.**
   - Swedish-type hereditary diffuse leukoencephalopathy with spheroids (HDLS-S) is autosomal dominant. It has been reported in a single large Swedish family and is attributed to AARS1 p.Cys152Phe (PMID:31775912).
   - One consanguineous Chinese family had recessive adult-onset leukoencephalopathy with axonal spheroids and pigmented glia (ALSP), homozygous for p.Thr606Ile (PMID:37106376).

> "Two phenotypic presentations emerged, one with early infantile-onset disease resembling the index cases of AARS1-related epileptic encephalopathy with deficient myelination (n = 7). The second (n = 4) was a later-onset disorder, where disease onset occurred after the first year of life and was characterized on neuroimaging by a progressive posterior predominant leukoencephalopathy evolving to include the frontal white matter." (PMID:34446925)

**Identifiers**

| Resource | ID | Notes |
|---|---|---|
| MONDO (umbrella) | MONDO:1010132 *AARS1-related leukoencephalopathy* | Label confirmed in `cache/mondo/terms.csv` |
| MONDO (DEE29) | MONDO:0014593 *developmental and epileptic encephalopathy, 29* | Cached |
| MONDO (HDLS-S) | MONDO:0030634 *leukoencephalopathy, hereditary diffuse, with spheroids 2* | Used in the draft entry |
| OMIM | 616339 (DEE29) | [web, not cached]; [LOVD](https://databases.lovd.nl/shared/diseases/04342), [ClinVar RCV000995470](https://https.ncbi.nlm.nih.gov/clinvar/RCV000995470.10) |
| Orphanet | ORPHA:442835 (DEE29) | [web, not cached]: seen only as a ClinVar cross-reference. Check with `just fetch-reference ORPHA:442835` |
| MedGen | C4225361 | [web, not cached] |
| DOID | DOID:0080451 | [web, not cached]; [glycosmos](https://glycosmos.org/diseases/DOID:0080451) |
| Gene | AARS1, `hgnc:20`, chromosome 16q22 | Draft binding |

**Synonyms.** AARS1-related white matter disease; AARS-related epileptic encephalopathy with deficient myelination; DEE29; EIEE29; HDLS-S (Swedish-type HDLS); AARS1-associated ALSP.

**Source type.** All data come from aggregated case reports and small cohorts. The largest series is 11 individuals (PMID:34446925). No EHR or registry data exist.

**Related conditions that are not this disease** (AARS1 allelic disorders):
- **CMT2N** (autosomal dominant axonal neuropathy). This is a separate peripheral nerve disease, not a leukoencephalopathy.
- **Trichothiodystrophy 8, nonphotosensitive** (MONDO:0030517). Here AARS1 variants make the protein unstable (PMID:33909043). The draft entry already lists it, and it should stay a separate or sibling concept rather than a subtype.

---

## 2. Etiology

- **Cause.** The disease is monogenic, caused by germline AARS1 variants.
  - The recessive forms come from biallelic loss of function: reduced aminoacylation, protein instability, and in some cases loss of editing.
  - The dominant HDLS-S form (p.Cys152Phe) is reported in a single family, and its mechanism is unproven.
- **Genetic risk factors.** Biallelic variants are causal. Consanguinity raises the risk of homozygosity: the homozygous p.Arg751Gly case (PMID:25817015) and the homozygous p.Thr606Ile family (PMID:37106376).
- **Environmental risk or protective factors.** None reported.
- **Gene–environment interactions.** None reported. Febrile or metabolic stress is a plausible trigger, since cellular stress worsens translation errors, but this has not been documented for AARS1. Treat it as a hypothesis only.
- **Protective genetic factors or modifiers.** None reported.

---

## 3. Phenotypes

Frequencies are qualitative, because the case series are very small. Counts come from the index reports (n = 3 + 2) and the Helman cohort (n = 11).

| Phenotype | Suggested HPO | Onset | Course | Frequency / notes | Source |
|---|---|---|---|---|---|
| Epileptic encephalopathy, refractory seizures (often myoclonic) | HP:0200134 Epileptic encephalopathy | Neonatal/early infancy | Refractory | Very frequent in the infantile form; less defined in the late form | PMID:25817015, 28493438 |
| Deficient / delayed myelination | HP:0003429 CNS hypomyelination | Infancy | Persistent | All index cases ("persistently deficient myelination on MRI") | PMID:25817015 |
| Progressive microcephaly | HP:0000253 | Infancy | Progressive | Index siblings | PMID:28493438 |
| Spasticity / hypertonia, hyperreflexia | HP:0001257 | Infancy (late form: childhood or adult) | Progressive | Frequent | PMID:28493438, 37106376 |
| Clubfoot | HP:0001762 Talipes equinovarus | Congenital | Static | Index cases | PMID:25817015 |
| Absent deep tendon reflexes | HP:0001284 Areflexia | Infancy | n/a | Index cases. Note this conflicts with the hyperreflexia seen in others. | PMID:25817015 |
| Peripheral neuropathy | HP:0009830 | Infancy/adult | Progressive | Index cases; axonal and demyelinating changes in the adult ALSP case | PMID:25817015, 37106376 |
| Extrapyramidal signs | HP:0002071 Abnormality of extrapyramidal motor function | Infancy | n/a | Index cases | PMID:25817015 |
| Global developmental delay | HP:0001263 | Infancy | n/a | Frequent | PMID:28493438 |
| Posterior-predominant leukoencephalopathy evolving frontally | HP:0002352 Leukoencephalopathy | >1 year | Rapidly progressive | 4/11 in the Helman cohort | PMID:34446925 |
| Frontal-lobe/behavioral syndrome, then cognitive decline | HP:0000751 Personality changes; HP:0001268 Mental deterioration | Adult | Rapid | HDLS-S family | PMID:31775912 |
| Cognitive impairment (MMSE 12/30, MoCA 3/30) | HP:0100543 Cognitive impairment | Adult | Progressive | ALSP case | PMID:37106376 |
| Dysarthria | HP:0001260 | Adult | Progressive | ALSP case | PMID:37106376 |
| Visual impairment / optic tract involvement | HP:0000505 Visual impairment | Infant (poor fixation) / adult | Progressive | DEE29 (OMIM summary); HDLS-S; ALSP case | PMID:31775912, 37106376 |
| Axonal spheroids (neuropathology) | HP:0034381 Central nervous system axonal spheroid | Adult | n/a | HDLS-S autopsies | PMID:31775912 |
| Cachexia, very low BMI (13.4) | HP:0004326 Cachexia | Adult | n/a | Single ALSP case | PMID:37106376 |
| Poor growth | HP:0001510 Growth delay | Infancy | n/a | DEE29 summary (OMIM, [web]) | — |

**HPO caveat.** These HPO IDs are suggestions from memory, except where they match bindings already in the draft entry (HP:0003429, HP:0200134, HP:0000253, HP:0001257, HP:0001762, HP:0001284, HP:0009830, HP:0002352, HP:0034381). Under the repository's term contract, look up every other ID before binding it.

**Quality of life.** No formal instrument data exist.
- The infantile form leaves children profoundly dependent.
- In the ALSP case the patient was wheelchair-dependent by age 25, two years after onset (PMID:37106376).
- HDLS-S has a median survival under 10 years (PMID:31775912).

---

## 4. Genetic and Molecular Information

**Gene.** AARS1 (alanyl-tRNA synthetase 1, cytoplasmic). `hgnc:20`; OMIM *601065 [web]. The protein has four parts: an aminoacylation domain, a tRNA-recognition domain, an editing domain and a C-terminal domain (C-Ala).

**Reported disease variants** (all germline)

| Variant (NM_001605) | Zygosity | Domain | Functional consequence | Phenotype | PMID |
|---|---|---|---|---|---|
| p.Lys81Thr | compound heterozygous with p.Arg751Gly | aminoacylation | Reduced function | Infantile DEE | 25817015 |
| p.Arg751Gly | homozygous; compound heterozygous | editing region / C-terminal half | Reduced function | Infantile DEE | 25817015 |
| c.2067dupC p.Tyr690Leufs*3 | compound heterozygous | editing | Protein loss, editing abolished | Progressive microcephaly, hypomyelination, DEE | 28493438 |
| c.2738G>A p.Gly913Asp | compound heterozygous | C-Ala | Reduced aminoacylation | same | 28493438 |
| c.455G>T p.Cys152Phe (HGVS c. as reported; verify) | heterozygous (AD) | aminoacylation | Not established; no splicing or brain expression change | HDLS-S | 31775912 |
| c.1817C>T p.Thr606Ile | homozygous | tRNA recognition/editing boundary | Deficient aminoacylation (reported) | Adult ALSP | 37106376 |
| Further variants in 11 individuals | biallelic | various | AlaRS activity reduced in 5 tested | Infantile and late forms | 34446925 |

> "The mutations decrease aminoacylation efficiency by 70%-90%. The p.Tyr690Leufs*3 mutation also abolished editing activity required for hydrolyzing misacylated tRNAs, thereby increasing errors during aminoacylation." (PMID:28493438)

> "...trio analysis did not find any mutations related to CSF1R or AARS2, but revealed a homozygous nonsynonymous variant AARS1:NM_001605:exon14:c.1817C > T:p.Thr606Ile" (PMID:37106376, full text)

**Variant classification.**
- ClinVar lists p.Gly913Asp with **conflicting interpretations** (3 submissions) [web].
- GenCC carries AARS1 submissions [web: [SGC-107335](https://thegencc.org/submissions/SGC-107335.2), [SGC-179765](https://thegencc.org/submissions/SGC-179765.1)]. A curation summary seen in search results says the dominant HDLS-S form has **no additional unrelated cases**. The tiers themselves were not read. Per repository policy they must be copied from the source, never assigned.

**Not supporting evidence.** PMID:38689878 reports a heterozygous AARS1 p.Arg695* inherited together with a CACNA1A variant in two sisters with epileptic encephalopathy. It shows neither biallelic AARS1 disease nor a leukoencephalopathy. At most it is `NO_EVIDENCE` for this entry and should not be cited as support.

**Other genomic findings.**
- Allele frequencies: the reported variants are rare or absent in gnomAD. Exact figures were not retrieved; check gnomAD.
- Modifier genes: none reported.
- Epigenetic findings: none reported.
- Chromosomal abnormalities: none reported. AARS1 sits within 16q22, but deletions of the region are not described as producing this phenotype.

---

## 5. Environmental Information

There are no known environmental, lifestyle or infectious contributors. This should be stated as **not applicable**.

---

## 6. Mechanism / Pathophysiology

### Causal chain (numbered; inferred steps flagged)

1. **Biallelic AARS1 loss-of-function variants** lead to **reduced AlaRS abundance or catalytic efficiency**. Evidence: protein destabilization in patient lymphoblastoid cells and a 70–90% loss of aminoacylation (PMID:28493438); reduced fibroblast AlaRS activity (PMID:34446925, PMID:25817015). *Demonstrated.*
2. **The disease branches at this step.**
   - **2a. Reduced aminoacylation** leads to a **lower supply of charged tRNA^Ala and slower translation** in cells with high protein-synthesis demand. *Inferred* from enzyme kinetics; direct human cell data on translation are limited.
   - **2b. Loss of editing** (p.Tyr690Leufs*3; mouse *sticky*) leads to **misacylated tRNA (Ser-tRNA^Ala)** and **serine wrongly inserted at alanine codons**. *Demonstrated* in vitro (PMID:28493438) and in mouse (PMID:16906134).
3. Branch 2b leads to **misfolded proteins accumulating, chaperones increasing, and the unfolded protein response switching on** in neurons. *Demonstrated in the mouse sti model only* (PMID:16906134).
   > "low levels of mischarged transfer RNAs (tRNAs) can lead to an intracellular accumulation of misfolded proteins in neurons. These accumulations are accompanied by upregulation of cytoplasmic protein chaperones and by induction of the unfolded protein response."
4. Loss of translational capacity or fidelity in oligodendrocytes, which need large amounts of myelin protein, leads to **failure of CNS myelination**. This explains the hypomyelination (infantile form) or the progressive white matter degeneration (late forms). *Inferred*: no oligodendrocyte-specific AARS1 model has been reported.
5. In neurons, the same defects lead to **neuronal or axonal degeneration**: Purkinje cell loss in the mouse (PMID:16906134) and axonal spheroids in adult human brains (PMID:31775912, PMID:37106376). *Demonstrated in mouse; human pathology is correlative.*
6. Cortical network dysfunction plus failed myelination produce **epileptic encephalopathy, developmental delay and progressive microcephaly** (PMID:25817015, PMID:28493438). *Mechanistic link inferred.*
7. Loss of white matter and long tracts leads to **spasticity, extrapyramidal signs and visual pathway loss**. Peripheral axon involvement leads to **neuropathy and areflexia**.
8. The adult-onset forms progress to **diffuse white matter liquefaction** ("widespread liquefaction of the white matter leaving only some macrophages and glial cells behind the centrifugally progressing front", PMID:31775912), and to **dementia and death**.

**Unresolved branch: the dominant form.** It is not established how a heterozygous p.Cys152Phe causes HDLS-S. Possibilities include a dominant-negative effect on the AlaRS dimer, as proposed for CMT2N, but this is untested for this variant. Record it as a `KNOWLEDGE_GAP`.

**Emerging non-canonical biology [web, not cached].** AARS1 also senses lactate and acts as a lactyltransferase:
- It lactylates p53 (Zong et al., *Cell* 2024, PMID:38653238).
- AARS1 and AARS2 lactylate cGAS (Li et al., *Nature* 2024, PMID:39322678).

No one has shown that this matters in the leukoencephalopathy. It is a hypothesis to note, not a node to curate.

### Checklist items

- **Molecular function:** GO:0004813 *alanine-tRNA ligase activity*. Editing activity: suggested GO:0002196 *Ser-tRNA(Ala) hydrolase activity* (verify before binding).
- **Biological processes:** GO:0006419 *alanyl-tRNA aminoacylation*; GO:0106074 *aminoacyl-tRNA metabolism involved in translational fidelity*; GO:0006986 *response to unfolded protein*; GO:0022010 *central nervous system myelination*. All four are in the draft. GO:0030968 *endoplasmic reticulum unfolded protein response* is a more specific candidate; verify it.
- **Cell types:**
  - CL:0000128 oligodendrocyte, CL:0000121 Purkinje cell (mouse); both in the draft.
  - Suggested, to verify: CL:0000540 neuron; CL:0000129 microglial cell and CL:0000235 macrophage (end-stage pathology).
- **Metabolic and immune involvement:** no primary metabolic defect or immune mechanism is reported. The macrophages and pigmented glia are best read as a downstream reaction to tissue destruction.
- **Molecular profiling** (transcriptomics, proteomics, single-cell, CRISPR screens): no disease-specific datasets were found.

---

## 7. Anatomical Structures Affected

| Level | Structure | Suggested term |
|---|---|---|
| Primary organ | Brain, cerebral white matter | UBERON:0002316 white matter (draft); UBERON:0011299 white matter of telencephalon (verify) |
| Regional pattern | Posterior-first (parieto-occipital), then frontal (late form); periventricular and corpus callosum (ALSP) | UBERON:0002336 corpus callosum (verify) |
| Secondary | Peripheral nerves; optic pathway/retina (thin RNFL on OCT in the ALSP case); cerebellum (mouse) | UBERON:0001021 nerve; UBERON:0000941 cranial nerve II (verify); UBERON:0002037 cerebellum |
| Cells | oligodendrocytes, neurons/axons, microglia/macrophages | see §6 |
| Subcellular | cytosol (translation); ER (UPR); axon (spheroids) | GO:0005829 cytosol; GO:0005783 endoplasmic reticulum; GO:0030424 axon |
| Lateralization | Bilateral, symmetric | — |

---

## 8. Temporal Development

- **Onset.**
  - Infantile form: neonatal to early infancy, with clubfoot already present at birth.
  - Late form: after 12 months, including childhood (PMID:34446925).
  - Adult forms: about age 23 in ALSP (PMID:37106376) and in adulthood in HDLS-S (PMID:31775912).
- **Course.**
  - Infantile form: static-to-progressive (progressive microcephaly, refractory epilepsy).
  - Late and adult forms: rapidly progressive. In ALSP the patient lost walking within about 2 years. In HDLS-S, frontal symptoms come first, followed by "a rapidly advancing encephalopathy with pyramidal, deep sensory, extrapyramidal and optic tract symptoms" (PMID:31775912).
- **Stages.** No formal staging exists. Suggested `progression:` phases: infantile/presymptomatic onset; progressive leukoencephalopathy; end-stage white matter liquefaction.
- **Remission.** None reported.
- **Critical periods.** Developmental myelination in infancy (inferred).

---

## 9. Inheritance and Population

- **Inheritance.**
  - Autosomal recessive (HP:0000007) for DEE29 and the late and ALSP forms.
  - Autosomal dominant (HP:0000006) for HDLS-S, in a single family.
- **Penetrance and expressivity.**
  - The recessive form appears fully penetrant. Expressivity varies widely, from infantile to adult onset.
  - In HDLS-S, the dominant segregation suggests high penetrance, but this rests on one pedigree.
- **Prevalence.** Not known; ultra-rare. Fewer than about 20 recessive cases are published. Use `measure_type: CASES_IN_LITERATURE`, `prevalence_class: ULTRA_RARE` or `NOT_YET_DOCUMENTED`.
  - For context only: leukodystrophy incidence overall has been estimated at "approximately 1/50,000 to 1/7663" (PMID:42650065). That figure is not specific to AARS1 and should not be used as AARS1 prevalence.
- **Founder effects.** None established. The only possible example is the HDLS-S family's western Swedish origin.
- **Consanguinity.** Documented in homozygous cases (PMID:37106376).
- **Anticipation and germline mosaicism.** Neither is reported.
- **Carrier frequency.** Not established.
- **Demographics.** Cases reported from the USA, Europe (Italy, Germany, Hungary, UK, Sweden), China and Ecuador. Both sexes are affected.

---

## 10. Diagnostics

- **Imaging (MRI).** This is the main clue.
  - Infantile form: deficient or persistently delayed myelination with atrophy.
  - Late form: leukoencephalopathy that begins posteriorly and spreads frontally.
  - Adult forms: symmetric periventricular and corpus callosum FLAIR hyperintensity. In ALSP, diffusion restriction is described as resembling CSF1R-ALSP (PMID:37106376).
- **EEG.** Epileptiform activity in the infantile form. The EEG was normal in the adult ALSP case.
- **Nerve conduction studies.** Axonal and demyelinating neuropathy.
- **Functional assay.** AlaRS aminoacylation activity in fibroblasts or lymphoblastoid cells supports pathogenicity (PMID:34446925, PMID:28493438). This is a research test rather than a routine clinical one.
- **Pathology.** Axonal spheroids, pigmented glia and macrophages; end-stage white matter liquefaction (PMID:31775912).
- **Genetic testing.**
  - Exome or genome sequencing found every reported case.
  - Leukodystrophy and epilepsy gene panels should include AARS1.
  - In adult CSF1R-negative spheroid leukoencephalopathy, test AARS1 and AARS2 (PMID:31775912, PMID:37106376).
  - CMA, karyotype, FISH and repeat-expansion testing are not indicated.
- **Differential diagnosis.**
  - CSF1R-ALSP and AARS2-ALSP (mitochondrial AlaRS).
  - Other hypomyelinating leukodystrophies: POLR3-related, PMD/PLP1, and other aminoacyl-tRNA synthetase disorders (RARS1, DARS1, EPRS1, KARS1).
  - Other DEEs.
  - Nonphotosensitive TTD due to AARS1, which has brittle hair (PMID:33909043).
- **Screening.** No newborn screening exists. Cascade carrier testing within families is appropriate.

---

## 11. Outcome / Prognosis

- **Infantile form.** Severe, lifelong disability. Survival data are not systematically reported.
- **Late form.** "a similarly rapid progressive clinical decline" (PMID:34446925).
- **HDLS-S.** Median survival is under 10 years from onset (PMID:31775912).
- **Prognostic factors and biomarkers.** None validated. Age at onset is the main determinant of phenotype.
- **Complications.** Refractory epilepsy, feeding difficulty or cachexia (PMID:37106376), contractures, visual loss.

---

## 12. Treatment

No disease-modifying therapy and no clinical trials were found. Management is supportive:

| Treatment | Suggested NCIT | `therapeutic_modality` |
|---|---|---|
| Antiseizure pharmacotherapy (refractory epilepsy) | NCIT:C15986 Pharmacotherapy | SMALL_MOLECULE (agent-specific) |
| Physical therapy for spasticity and contractures | NCIT:C15302 Physical Therapy | BEHAVIORAL |
| Orthopedic management of clubfoot | NCIT:C16186 Orthopedic Surgical Procedure | SURGERY |
| Nutritional support or gastrostomy | NCIT:C15433 Nutritional Support (check the actual intervention before tagging a modality) | — |
| Genetic counseling | NCIT:C15240 Genetic Counseling | — |
| Supportive and palliative care | NCIT:C15747 Supportive Care | — |

**Experimental and speculative approaches** (none tested in AARS1 disease):
- Amino acid supplementation, which has been tried in other cytoplasmic tRNA synthetase disorders (e.g., IARS1, LARS1).
- Gene replacement.

The 2026 review discusses "emerging therapeutic perspectives" (PMID:42650065), but none are clinically validated. Any such content would at most fit a `KNOWLEDGE_GAP` discussion, not a treatment.

---

## 13. Prevention

- **Primary prevention.** Not applicable.
- **Reproductive options.** Genetic counseling (25% recurrence risk for the recessive forms; 50% for the dominant HDLS-S form), carrier testing of relatives, prenatal diagnosis or PGT once the familial variants are known.
- **Tertiary prevention.** Seizure control, prevention of contractures and nutritional management.
- **Vaccination, public health and environmental measures.** Not applicable.

---

## 14. Other Species / Natural Disease

- No naturally occurring animal disease was found; OMIA was not searched.
- AlaRS editing is conserved down to bacteria; the *sticky* paper used *E. coli* experiments (PMID:16906134).
- Mouse ortholog: *Aars1* (MGI; verify the identifier before use).

---

## 15. Model Organisms

| Model | Genotype | Recapitulates | Limitations | PMID |
|---|---|---|---|---|
| Mouse *sticky* (*sti*) | Homozygous *Aars* p.Ala734Glu, editing-domain missense | Purkinje cell loss, ataxia, neuronal misfolded-protein accumulation, UPR | Editing-specific. It does not model the hypomyelination or epilepsy of the human disease. It shows cerebellar rather than white matter disease. | 16906134 |
| Patient LCL / fibroblasts | Biallelic patient variants | Low AlaRS abundance and activity | No CNS context | 28493438, 34446925 |
| Yeast complementation | Patient alleles | Functional loss (as used in AARS-CMT and recessive studies) | Single-cell, not neural | 25817015 (full text; verify) |

**Notes on the *sti* mouse.**
- The p.Ala734Glu genotype is from my memory of the paper. The cached abstract does not state it, so verify it from the full text.
- For curation, the *sti* mouse should be a `PARTIALLY_RECAPITULATES` link to the misfolding/UPR node, with `fidelity: LOW` against the hypomyelination node. This is a case for a `HUMAN_MODEL_MISMATCH` discussion.

**Missing models.** No oligodendrocyte-specific or knock-in model of the recessive human variants was found. This is a clear knowledge gap.

---

## Evidence Summary and Curation Notes

1. **Strongest human evidence:**
   - PMID:25817015 (index DEE; loss of function)
   - PMID:28493438 (aminoacylation and editing loss; progressive microcephaly)
   - PMID:34446925 (spectrum; late-onset form)
2. **Adult forms rest on one family each:** PMID:31775912 (AD, HDLS-S) and PMID:37106376 (AR, ALSP). Use `directness`/`notes` to say that these assertions come from a single family.
3. **Mechanistic evidence is mainly mouse** (PMID:16906134, `MODEL_ORGANISM`). Keep it separate from human evidence.
4. **PMID:35168888** (Leidi et al. correspondence) has no cached content, so it cannot provide snippets.
5. **PMID:38689878** should not be cited as support (§4).
6. **PMID:33909043** (TTD8) belongs to an allelic, distinct disease. Do not merge its phenotypes into this entry.
7. **Identifiers not cached:** run `just fetch-reference` for every **[web]**-tagged identifier (ORPHA:442835, PMID:38653238, PMID:39322678) before citing it. Look up every HPO, GO, CL and UBERON term not already in the draft before binding it.

---

## Sources

**Cached locally (`references_cache/`):** PMID:16906134, 25817015, 28493438, 31775912, 33909043, 34446925, 35168888, 37106376, 38689878, 42650065.

**Web (not cached):**
- [MedGen C4225361 mirror](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/commit/16b4b23030b9c25e5a647a69ebd82dc9aecccaad/www.ncbi.nlm.nih.gov/medgen/C4225361/index.html)
- [ClinVar RCV000995470 (p.Gly913Asp)](https://https.ncbi.nlm.nih.gov/clinvar/RCV000995470.10)
- [LOVD DEE29 (OMIM:616339)](https://databases.lovd.nl/shared/diseases/04342)
- [DOID:0080451](https://glycosmos.org/diseases/DOID:0080451)
- [MONDO:1010132 node](https://phenotypes.healthdatagateway.org/api/v1/ontology/node/MONDO:1010132/)
- [GenCC SGC-107335](https://thegencc.org/submissions/SGC-107335.2), [GenCC SGC-179765](https://thegencc.org/submissions/SGC-179765.1)
- [Wu et al. 2023, PMC10142409](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10142409/)
- [CeGaT summary of Helman 2021](https://www.cegat.de/expanded-phenotype-of-aars1-related-white-matter-disease/)
- [AARS1/AARS2 lactate-sensor review, PMC12373605](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12373605/)
- [Zong 2024 Cell (PMID 38653238)](https://www.medchemexpress.com/publications/38653238.html)
- [Li 2024 Nature (PMID 39322678)](https://www.medchemexpress.com/publications/39322678.html)
- [Neurogenetics 2026 article (not reviewed)](https://link.springer.com/article/10.1007/s10048-026-00885-4)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 7 |
| Quoted claims found in source | 6 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 15 |
| On topic | 7 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:34446925` *(abstract only)*: "a similarly rapid progressive clinical decline"
  - closest text in source: "However, a subgroup of affected individuals manifests with late-onset disease and similarly rapid progressive clinical decline"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 54 |
| Resolved | 52 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 9 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `DOID:0080451` (5 mentions) - the report calls it "DOID"; DOID calls it **developmental and epileptic encephalopathy 29**
- `HP:0001257` (2 mentions) - the report calls it "Spasticity / hypertonia, hyperreflexia"; HP calls it **Spasticity**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000007` (1 mention) - the report calls it "Autosomal recessive"; HP calls it **Autosomal recessive inheritance**, and lists "Autosomal recessive" among its other names
- `HP:0000006` (1 mention) - the report calls it "Autosomal dominant"; HP calls it **Autosomal dominant inheritance**, and lists "Autosomal dominant" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `OMIM`.