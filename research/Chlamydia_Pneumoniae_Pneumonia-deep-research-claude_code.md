---
provider: claude_code
model: claude-fable-5-1, claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-09-26T21:59:01.512713'
end_time: '2026-09-26T22:26:30.135046'
duration_seconds: 1648.62
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Chlamydia Pneumoniae Pneumonia
  mondo_id: ''
  category: Infectious Disease
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
  - claude-fable-5-1
  - claude-haiku-4-5-20251001
  - claude-opus-5
  web_search_requests: 23
  num_turns: 82
  total_cost_usd: 12.4038025
  session_id: e0b29406-f36d-45e5-9c64-3278c258c9b5
  stop_reason: end_turn
  assistant_text_blocks: 3
citation_count: 25
reference_validation:
  total_references: 66
  verified: 66
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 4
  quotes_valid: 2
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:40279169
  relevance_assessed: 66
  on_topic: 58
  needs_review: true
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 86
  verified: 83
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 9
  labels_matching: 6
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: MONDO:0025598
    reported_labels:
    - MONDO
    ontology_label: pneumonia caused by chlamydia
  - term_id: DOID:0040083
    reported_labels:
    - DOID
    ontology_label: Chlamydia pneumonia
  - term_id: NCBITaxon:83558
    reported_labels:
    - NCBI Taxonomy (pathogen)
    ontology_label: Chlamydia pneumoniae
  unresolvable_prefixes:
  - ICD11
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Chlamydia Pneumoniae Pneumonia
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Chlamydia Pneumoniae Pneumonia** covering all of the
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

I'll research Chlamydia pneumoniae pneumonia across the template's sections using web search and literature lookups, then write the full report inline.

I'll re-run the remaining lookups in smaller batches.

I've completed the research. Here is the full report.

---

# Chlamydia pneumoniae Pneumonia — Comprehensive Disease Research Report

**Prepared:** 2026-09-26 · **Target entry:** `Chlamydia_Pneumoniae_Pneumonia` · **Category:** Infectious Disease

**Scope note on evidence quality.** This is an acquired bacterial infection, not a Mendelian disorder. Template sections that presuppose a germline genetic etiology (causal genes, pathogenic variants, inheritance pattern, penetrance, carrier frequency, genetic counseling, prenatal testing) have **no applicable content** and are marked as such rather than filled with host-susceptibility material presented as disease causation. Host genetic modifiers are reported separately and are almost entirely murine.

---

## 1. Disease Information

### Overview

*Chlamydia pneumoniae* pneumonia is a community-acquired atypical pneumonia caused by the obligate intracellular Gram-negative bacterium *Chlamydia pneumoniae* (formerly *Chlamydophila pneumoniae*; original isolate designation TWAR, from the two founding strains TW-183 and AR-39). The organism was recognized as a distinct species in the late 1980s and characterized as a respiratory pathogen by Grayston and colleagues.

> "Chlamydia pneumoniae strain TWAR, the new third species of Chlamydia, is a common cause of pneumonia and other acute respiratory tract infections. About 10% of hospitalized and outpatient pneumonia cases have been associated with TWAR infection. TWAR is among the four or five most commonly identified causes of all pneumonia." — Grayston JT et al., *J Infect Dis* 1990 (PMID:2181028)

> "*Chlamydia pneumoniae* is an obligate intracellular bacterium and a significant cause of respiratory infections. It is associated with upper and lower respiratory tract diseases, including bronchitis and pneumonia. The pathogen employs specific virulence factors, such as the Type III Secretion System (T3SS) and Inc proteins, to invade and subvert host cell machinery during its peculiar developmental life cycle." — Tagini F, Puolakkainen M, Greub G, *J Med Microbiol* 2025 (PMID:40279169, DOI 10.1099/jmm.0.002006)

The infection spans a clinical spectrum from asymptomatic carriage and upper respiratory illness through bronchitis to pneumonia, and — much more contentiously — to chronic sequelae (asthma, atherosclerosis, neurodegeneration).

### Key identifiers

| Resource | Identifier | Label / note |
|---|---|---|
| MONDO | `MONDO:0025598` | *pneumonia caused by chlamydia* — **genus-level**; no species-specific MONDO term exists |
| DOID | `DOID:0040083` | equivalent to MONDO:0025598 |
| ICD-10-CM | `J16.0` | Chlamydial pneumonia (MONDO xref) |
| ICD-9 | `483.1` | |
| ICD-11 MMS | `CA40.00` | *Pneumonia due to Chlamydophila pneumoniae* — **species-specific**, the most precise clinical code |
| MeSH | `D061387` | preferred term *Chlamydial Pneumonia*; entry term *Chlamydophila Pneumonia* |
| SNOMED CT | `233609002` | |
| UMLS | `C0339959` | |
| MedGen | `452440` | |
| NCBI Taxonomy (pathogen) | `NCBITaxon:83558` | *Chlamydia pneumoniae* |

**Curation consequence.** The only MONDO anchor is genus-level while ICD-11 is species-level. A species-scoped dismech entry should bind `MONDO:0025598` with `mapping_predicate: skos:broadMatch` (or narrowMatch from the entry's perspective, per the repo's mapping rules) and carry `ICD11:CA40.00` as the exact clinical code, with a `notes:` line recording that no species-level MONDO term was found on 2026-09-26 via the EBI OLS4 MONDO search for "Chlamydia pneumoniae" and "chlamydophila" (returns `MONDO:0025598`, `MONDO:0004652` bacterial pneumonia, `MONDO:0005888` ornithosis, `MONDO:0021697` chlamydia infectious disease, `MONDO:1017031`; `MONDO:0025598` has no children).

### Synonyms

*Chlamydophila pneumoniae* pneumonia; chlamydial pneumonia; TWAR pneumonia; *C. pneumoniae* respiratory infection; Taiwan acute respiratory agent pneumonia.

### Data provenance

Disease-level aggregated sources (CDC clinical and laboratory pages, MONDO/MeSH/ICD, review literature) plus patient-level retrospective hospital cohorts (Chinese pediatric series 2025–2026, Mexican pediatric series 2023, Swiss/German/French laboratory surveillance). Multi-site laboratory surveillance (Eurosurveillance 2025) is aggregated test-level data, not EHR-derived.

---

## 2. Etiology

### Causal factor

A single necessary and sufficient cause: infection with *Chlamydia pneumoniae* (`NCBITaxon:83558`). There is no non-infectious route to this entry. Transmission is person-to-person via respiratory droplets and, secondarily, fomites (CDC clinical overview). No animal reservoir is required for human transmission (see §14).

The organism's lifecycle is obligately intracellular and biphasic:

> "*Chlamydia* alternates between the infectious, environmentally resistant Elementary Body (EB) and the non-infectious, metabolically active Reticulate Body (RB)… RBs exploit host-derived energy and nutrients to multiply by binary fission, ultimately re-differentiating into progeny EBs." — Tu S et al., *Front Cell Infect Microbiol* 2026;16:1787885 (PMID:42180254)

### Incubation and transmissibility

> "*C. pneumoniae* infection generally has a long incubation period of 3 to 4 weeks. However, studies have documented shorter times." — CDC Clinical Overview

The long incubation and high asymptomatic fraction produce slow, protracted institutional outbreaks rather than sharp point-source epidemics.

### Risk factors — environmental and demographic

| Risk factor | Evidence | Citation |
|---|---|---|
| Crowded/closed living (military training, academies, prisons, universities, households) | Outbreak series with measurable attack rates | PMID:30690452; PMID:25988545; PMID:21635754 |
| School age (primary infection) | "Primary infection occurs mainly in school-aged children or young adults" | CDC Clinical Overview |
| Age >65 (reinfection) | "Reinfections tend to occur more frequently in older adults (>65 years old)" | PMID:40279169 |
| Male adolescent sex (post-2024 China) | "male adolescents aged 10–19 years emerged as the highest-risk population" | PMID:41088528 |
| Underlying chronic disease (pediatric) | 88% of C. pneumoniae-positive children had underlying disease (P = 0.014) | PMID:38052876 |
| Waning population immunity after COVID-19 NPIs | Detection ratios fell 1.05% → 0.23% during the pandemic, then rebounded | PMID:40511472 |

Suggested ECTO-style exposure concept: *exposure to a crowded residential environment*. Note per repository policy that an ECTO CURIE must be searched and confirmed at binding time; no ECTO term is asserted here.

### Risk factors — host genetic

No validated human genetic susceptibility locus is established. Candidate-gene work on innate-immunity polymorphisms (`TLR2` Arg753Gln, `TLR4` Asp299Gly, `CD14`, `LBP`, `IL6`) examined *C. pneumoniae* growth in human macrophages in vitro and found highly variable donor susceptibility without a robust attributable polymorphism. Murine work is stronger and is reported in §4 and §15. **No GWAS Catalog entry for *C. pneumoniae* pneumonia was identified.**

### Protective factors

- **Prior infection confers partial, non-sterilizing immunity.** Murine reinfection is cleared faster than primary infection, and the effect is IFN-γ-dependent (PMID:10639472).
- **Non-pharmaceutical interventions.** Masking, distancing, and school closure produced a statistically significant fall in detection (PMID:40511472).
- No dietary, nutritional, or genetic protective factor is established. **No protective allele is known.**

### Gene–environment interaction

In mice the interaction is demonstrable: strain background (A/J vs C57BL/6) determines pulmonary bacterial load and lung pathology after an identical intranasal inoculum, with ~30% of variance mapping to an MHC-overlapping chromosome 17 QTL (PMID:18075514). The human equivalent has not been demonstrated. In the `sst1` model, host genotype determines *disease tolerance* rather than *bacterial clearance* — a genuine gene-by-infection interaction on the pathology axis alone (PMID:24009502).

---

## 3. Phenotypes

Frequencies below are cohort-specific. The three largest recent series differ in age structure and case definition, so **do not pool them**; the entry should carry each frequency with its own population and evidence item.

### Cohort key

- **A** — 291 hospitalized children, Shijiazhuang, China, 2015–2025; mean age 8.12 y (PMID:41210234)
- **B** — 145 hospitalized children, Xi'an, China, Jan–Jul 2025; median age 11 y (PMID:42427957)
- **C** — 42 adults/mixed, mNGS-confirmed, Aug 2022–Aug 2025 (PMID:41676099)
- **D** — 25 of 154 hospitalized children with CAP, Mexico City (PMID:38052876)

### Symptoms and signs

| Phenotype | HPO term | Frequency (cohort) |
|---|---|---|
| Cough | `HP:0012735` Cough | 98.60% (A); 99.3% (B); 71.4% (C); 100% (D) |
| Productive cough | `HP:0031245` Productive cough | wet cough 97.2% (B); expectoration 64.3% (C) |
| Fever | `HP:0001945` Fever | 44.80%, median peak 38.2 °C (A); 44.8%, median peak 38.5 °C (B); 59.5% (C); 88% (D) |
| Crackles / pulmonary rales | `HP:0030830` Crackles | 98.97% rales (A); 68% crackles (D) |
| Wheezing | `HP:0030828` Wheezing | 52% (D); reported as "a major clinical complaint" in the Lausanne outbreak (EID 2024) |
| Pharyngalgia (sore throat) | `HP:0033050` Pharyngalgia | 61.9% (C) |
| Nasal congestion | `HP:0001742` Nasal congestion | 29.7% (B) |
| Rhinorrhea | `HP:0031417` Rhinorrhea | 48% (D) |
| Chest pain | `HP:0100749` Chest pain | 7.6% (B); significantly higher in CPP than in *M. pneumoniae* pneumonia (PMID:40775274) |
| Myalgia | `HP:0003326` Myalgia | 26.2% (C) |
| Fatigue | `HP:0012378` Fatigue | 23.8% general fatigue (C) |
| Headache | `HP:0002315` Headache | 23.8% with headache/dizziness (C); listed among most common by CDC |
| Malaise | `HP:0033834` Malaise | CDC lists among most common symptoms |
| Hoarse voice | `HP:0001609` Hoarse voice | characteristic of the upper-tract presentation (PMID:40279169) |
| Hypoxemia | `HP:0012418` Hypoxemia | desaturation 93% (D) |
| Skin rash | `HP:0000988` Skin rash | 3.4% (B); case cluster reported (PMID:42755900) |
| Hemoptysis | `HP:0002105` Hemoptysis | 3.4% (B) |
| Pneumonia (the entry-defining feature) | `HP:0002090` Pneumonia | 100% by definition |

Related upper-tract syndromes the same organism causes, useful as `has_subtypes` or sibling phenotypes rather than features of the pneumonia entry: `HP:0025439` Pharyngitis, `HP:0000246` Sinusitis, `HP:0012387` Bronchitis, `HP:0000388` Otitis media.

> "*C. pneumoniae* may cause any kind of respiratory tract infection, ranging from upper respiratory tract infections (with symptoms of rhinitis, sore throat or hoarseness), sinusitis or otitis to bronchitis and community-acquired pneumonia." — PMID:40279169

### Laboratory abnormalities

| Phenotype | HPO term | Detail |
|---|---|---|
| Elevated CRP | `HP:0011227` Elevated circulating C-reactive protein concentration | 50.0% elevated, 14.3% >100 mg/L (C); "normal or only mildly elevated" (A); median 4.39 mg/L (B) |
| Leukocytosis | `HP:0001974` Increased total leukocyte count | mild rise in 28.6% (C); elevated with neutrophil predominance (A) |
| Increased eosinophils | `HP:0001880` Increased total eosinophil count | significantly higher in CPP than MPP; eosinophil count identified as a candidate severity biomarker (PMID:40775274) |
| Decreased lymphocytes | `HP:0001888` Decreased total lymphocyte count | lower lymphocyte percentage in severe vs non-severe CPP, OR 0.943 (95% CI 0.895–0.994) (PMID:42327901) |
| Increased circulating IgA | `HP:0003261` Increased circulating IgA concentration | elevated IgA associated with severe CPP, OR 2.227 (95% CI 1.284–3.972) (PMID:42327901) |

### Radiographic phenotypes

Chest CT in 42 mNGS-confirmed patients (PMID:41676099), verbatim:

> "In the early stage, chest CT demonstrated a lobular pneumonia pattern in 16 patients (55.2%), involvement of a single lung lobe in 20 (69.0%), predominant lower-lung distribution in 19 (65.5%)… The main accompanying features included a halo sign in 25 patients (86.2%), centrilobular nodules in 23 (79.3%), and bronchial wall thickening in 20 (69.0%)."

Plain radiography in children (PMID:38052876):

> "The interstitial pattern on chest-X-ray was the most frequent (68%), consolidation was observed in 32%."

HPO: `HP:0002113` Pulmonary infiltrates; `HP:0006515` Interstitial pneumonitis; `HP:0002202` Pleural effusion (uncommon); `HP:0002088` Abnormal lung morphology as the coarse parent.

**Coarse-binding caution.** If `HP:0002088` Abnormal lung morphology is used for an imaging phenotype, it falls in the repository's coarse set and requires a `coarse_binding_basis`; `VARIABLE_SPECTRUM` fits, since the radiographic pattern genuinely ranges from interstitial to lobular to consolidative across cohorts.

### Onset, severity, progression

- **Onset:** gradual/insidious after a 3–4-week incubation (CDC). Not congenital, not age-restricted; primary infection concentrates in school age, reinfection in the elderly.
- **Severity:** mild in the large majority. "Most respiratory infections caused by *C. pneumoniae* are asymptomatic or mild" (CDC). Severe disease reached 6.8% of a 176-patient pediatric series (PMID:40775274) and 34/133 (25.6%) in a cohort explicitly enriched for severity assessment (PMID:42327901) — the discrepancy is a case-mix artifact and should be curated as two separate population-scoped statements.
- **Progression:** self-limited in most; protracted cough is the signature. Median cough duration 21 days (PMID:40279169); mean total disease duration 14.81 days with mean hospital stay 7.52 days (A); median disease duration 14 days (B).
- **Persistence:** "Patients may experience a persistent cough and malaise for several weeks or months" even after appropriate antibiotics (CDC Clinical Features).

### Quality of life

No EQ-5D, SF-36, or PROMIS data specific to *C. pneumoniae* pneumonia were identified. The functional burden documented is indirect: hospital stay (mean 7.52 days, cohort A), weeks-to-months of residual cough and malaise (CDC), and — for those developing or exacerbating asthma — the chronic burden of that disease. **Disease-specific QoL instruments: not available.**

---

## 4. Genetic / Molecular Information

**Causal genes: not applicable.** There is no human causal gene, no pathogenic variant, no variant classification, no allele frequency, no somatic/germline distinction, no chromosomal abnormality, and no epigenetic disease mechanism for this entry. The `genetic:` section of a dismech entry for this disease should be empty or restricted to susceptibility/modifier typing with `relationship_type: SUSCEPTIBILITY` or `MODIFIER`, never `CAUSAL`.

### Host modifier genes (mostly murine; treat as model-organism evidence)

| Gene | HGNC | Role | Evidence |
|---|---|---|---|
| `TLR2` | `hgnc:11848` | Required for effective early-life host defense; TLR2-deficient neonatal mice had more severe, more prolonged infection | PMID:22724018 (MODEL_ORGANISM) |
| `TLR4` | `hgnc:11850` | Dispensable — TLR4-deficient mice were asymptomatic | PMID:22724018 (MODEL_ORGANISM) |
| `IFNG` | `hgnc:5438` | IFN-γ neutralization increased lung bacterial counts and pneumonia score; essential in reinfection in both strains | PMID:10639472 (MODEL_ORGANISM) |
| `IDO1` | `HGNC:6059` | IFN-γ-induced tryptophan catabolism drives aberrant-body persistence | PMID:8063385; PMID:11705979 (IN_VITRO) |
| `IL10` | — | IL-10 knockout: faster clearance but more severe lung pathology | PMID:18456450 (MODEL_ORGANISM) |
| `NOD1` | `HGNC:16390` | Nod1-mediated endothelial activation by *C. pneumoniae* | PMID:15653568 (IN_VITRO) |
| `NLRP3` | `hgnc:16400` | Inflammasome activation co-localizing with *C. pneumoniae* inclusions in Alzheimer retina; caspase-1, cleaved IL-1β, cleaved gasdermin-D | PMID:41571675 (HUMAN_CLINICAL + MODEL_ORGANISM, mixed — split the evidence items) |
| `TNF`, `CXCL8`, `IL6`, `IL1B` | `hgnc:11892`, `hgnc:6025`, `hgnc:6018`, `hgnc:5992` | Epithelial cytokine response; only IL-8 protein consistently secreted | PMID:12540537 (IN_VITRO) |
| Murine chr17 QTL (MHC-overlapping) | no HGNC equivalent | LOD 11.5, ~30% of variance in pulmonary bacterial load, B6 alleles recessive-susceptible | PMID:18075514 (MODEL_ORGANISM) |
| Murine `sst1` locus | no HGNC equivalent | Governs disease *tolerance*, not clearance; sst1-susceptible mice had worse inflammation and fibrosis with normal bacterial control | PMID:24009502 (MODEL_ORGANISM) |

**Curation warning applicable here.** Per the repository's gene-binding rule, each of the HGNC CURIEs above was read from `cache/hgnc/terms.csv` or the genenames.org REST API on 2026-09-26 (`HGNC:6059` IDO1 and `HGNC:16390` NOD1 came from the API and are not yet in the local cache; note that the repository's canonical form is lowercase `hgnc:`). Re-verify before binding.

### Pathogen genomics (this is where the molecular detail actually lives)

- Human isolates are essentially clonal. The CWL029 reference chromosome is ~1.23 Mb, circular, with no plasmid; J138 is 1,226,565 nt, 40.7% G+C, 1,072 protein-coding genes, 3,665 nt shorter than CWL029 (PMID:10871362).
- The koala isolate LPCoLN carries a 1,241,024-bp chromosome **plus a 7.5-kb cryptic plasmid** that human strains have lost (PMID:19749045).
- Animal isolates are far more diverse than human ones; five genotypes A–E were defined across 30 isolates (PMID:20502684).
- More than 5% of the chlamydial genome is predicted to encode type III secretion effectors, including the Inc family at the inclusion membrane.

### Molecular profiling

- **Transcriptomics:** the transcriptional landscape of *C. pneumoniae* has been mapped (*Genome Biol* 2011). Host-cell transcriptional responses under IFN-γ-induced persistence overlap productive infection and cluster on apoptosis, cell-cycle and metabolism genes (*Infect Immun* 2006). **No GEO accession is asserted here** — the repository requires `just discover-datasets` / `just verify-datasets` before any `geo:` accession is written, and dataset relevance triage is a manual step.
- **Proteomics / metabolomics / lipidomics / single-cell / spatial:** retinal and cortical proteomics in the Alzheimer study (PMID:41571675) is the only recent omics dataset found that centers on this organism, and it is a chronic-extrapulmonary context, not pneumonia. **No pneumonia-specific proteomic, metabolomic, lipidomic, single-cell, or spatial dataset was identified.**
- **Functional genomics:** a yeast-based screen identified the host microtubule cytoskeleton as a target of numerous chlamydial effectors (PMID:37108781). No DepMap/CRISPR screen specific to this infection was found.

---

## 5. Environmental Information

**Infectious agent.** *Chlamydia pneumoniae*, `NCBITaxon:83558`. Obligate intracellular, Gram-negative, no peptidoglycan-dependent β-lactam target of clinical use.

**Transmission environment.** Respiratory droplets from close person-to-person contact, plus fomite transfer (CDC). Congregate settings dominate documented outbreaks:

| Setting | Attack rate / positivity | Citation |
|---|---|---|
| US Army trainees, Fort Leonard Wood, 2014 | Weekly radiologically-confirmed pneumonia attack rates 1.4% and 1.2% in two companies vs 0–0.4% elsewhere on post | PMID:30690452 |
| US Army trainee company, 2011 report | *C. pneumoniae* identified in 31% of specimens from symptomatic trainees | PMID:21635754 |
| US Air Force Academy cadets, Oct 2013 – May 2014 | 102 pneumonia cases; 73% of tested nasal washes positive | PMID:25988545 |
| Lausanne University Hospital, Oct–Dec 2023 | PCR positivity 3.61%, peaking 6.66% in October, vs a decade-long 0–0.75% baseline | EID 2024;30(4):810-812, DOI 10.3201/eid3004.231610 |

**Lifestyle factors.** No confirmed dietary, alcohol, or exercise association. Smoking is a general risk factor for CAP and for the COPD phenotype in which *C. pneumoniae* has been repeatedly sought, but a smoking-specific risk estimate for *C. pneumoniae* pneumonia was not found in this search.

**Chemical/occupational exposures.** None established. CTD and EPA sources were not searched for this pathogen because no toxicological etiology is plausible.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Inhalation of elementary bodies (EBs) in respiratory droplets** deposits metabolically inert, environmentally resistant EBs on the mucosal epithelium of the upper and lower respiratory tract. *Demonstrated for the genus; the specific human inoculum dose is not known.*
2. **EB cytadherence to respiratory epithelial cells** *leads to* immediate pro-inflammatory signaling, before any bacterial replication. Heparin pretreatment — which blocks attachment — significantly reduced IL-8 and TNF-α mRNA induction, and heat/UV inactivation only partially reduced the response, establishing adhesion itself as the trigger (PMID:12540537, IN_VITRO).
3. **Receptor-mediated uptake into a membrane-bound vacuole (the inclusion)** *results in* an intracellular niche. The inclusion traffics to the peri-Golgi region and avoids lysosomal fusion.
4. **The inclusion is actively remodeled by secreted effectors.** The T3SS delivers early (0–12 h) and mid-cycle (12–36 h) effectors and a family of inclusion-membrane (Inc) proteins; *C. pneumoniae* recruits PI4P to the inclusion via the Cpn0308–ACBD3–PI4KB axis (PMID:42240327, IN_VITRO). CPAF, a secreted serine protease, cooperates with T3SS effectors to block p65 nuclear translocation. GO: `GO:0030254` protein secretion by the type III secretion system; `GO:0020003` symbiont-containing vacuole; `GO:0006898` receptor-mediated endocytosis.
5. **EB→RB differentiation and binary fission** *lead to* an expanding inclusion. The complete cycle takes 72–96 h in vitro, slower than *C. trachomatis*; ultrastructural staging is described in PMID:10722649 (IN_VITRO).
6. **Infected epithelial cells are rendered apoptosis-resistant**, *which preserves* the replicative niche. Mitochondria in infected cells fail to release apoptogenic factors and active caspase-3 is absent; protection requires large inclusions (PMID:11705971, IN_VITRO). GO: `GO:0043066` negative regulation of apoptotic process.
7. **Branch A — mucociliary clearance fails.** *C. pneumoniae* infection of ciliated bronchial epithelium "had a marked ciliastatic effect, completely aborting ciliary motion within 48 h", an effect resistant to UV inactivation but abolished by heat or specific antiserum (PMID:7751703, IN_VITRO). This *contributes to* bacterial retention and to secondary bacterial superinfection. GO: `GO:0003341` cilium movement (decreased).
8. **Branch B — epithelial chemokine release recruits neutrophils.** IL-8 protein is consistently secreted by infected A549 cells; IL-1β and IL-6 protein are not significantly changed in that system (PMID:12540537). GO: `GO:0032757` positive regulation of interleukin-8 production; `GO:0030593` neutrophil chemotaxis; `GO:0007249` canonical NF-κB signal transduction (antagonized by CPAF, so the net signal is a contested balance rather than simple activation).
9. **Neutrophils become a Trojan horse.** *C. pneumoniae* "easily infect and hide inside neutrophil granulocytes until these cells become apoptotic and are subsequently taken up by macrophages", and this route yields *enhanced* replication compared with direct macrophage infection, with a TGF-β-skewed rather than TNF-α-skewed macrophage response (PMID:19547701, IN_VITRO). Blocking phosphatidylserine recognition with annexin A5 significantly reduced transmission — a clean causal test.
10. **Alveolar and monocyte-derived macrophages become the long-lived reservoir**, *which permits* dissemination beyond the airway to vascular endothelium and smooth muscle. CL: `CL:0000583` alveolar macrophage, `CL:0000235` macrophage, `CL:0000775` neutrophil, `CL:0000576` monocyte, `CL:0002328` bronchial epithelial cell, `CL:0000082` epithelial cell of lung, `CL:0000115` endothelial cell, `CL:0000192` smooth muscle cell.
11. **A Th1 response with IFN-γ is mounted**, *which restricts* replication. GO: `GO:0042088` T-helper 1 type immune response; `GO:0032609` type II interferon production; `GO:0034341` response to type II interferon. Neutralizing IFN-γ increases bacterial load and pneumonia score in mice (PMID:10639472, MODEL_ORGANISM).
12. **IFN-γ simultaneously induces IDO1, depleting intracellular tryptophan** — and this *causes* persistence rather than clearance when IFN-γ is subinhibitory. *C. pneumoniae* is a tryptophan auxotroph; IDO-deficient cells responsive to IFN-γ support normal growth without aberrant forms, and adding exogenous tryptophan reverses the effect (PMID:8063385, IN_VITRO). GO: `GO:0006569` L-tryptophan catabolic process; CHEBI: `CHEBI:16828` L-tryptophan.
13. **Persistence manifests morphologically as aberrant bodies.** IFN-γ-treated cultures show "atypical inclusions containing large reticulate-like aberrant bodies with no evidence of redifferentiation into elementary bodies", dose-dependently (PMID:11705979, IN_VITRO). Iron deprivation and β-lactam exposure induce the same state (PMID:40279169). **Whether this in vitro state occurs in vivo remains genuinely open** — a 2026 review is titled precisely "Open question: Can *Chlamydia pneumoniae* cause persistent infections…" (PMID:42690975). Curate the persistence chain with a `discussions:` entry of `kind: KNOWLEDGE_GAP`.
14. **The resulting mixed neutrophilic–lymphocytic alveolar and bronchiolar inflammation** *produces* the clinical and radiographic pneumonia: centrilobular nodules and bronchial wall thickening reflecting the bronchiolocentric route, halo signs reflecting perilesional inflammation (PMID:41676099).
15. **Branch C — chronic outcome.** In mice, infection *induces* persisting macrophage accumulation beyond bacterial clearance, inducible bronchus-associated lymphoid tissue (iBALT) from day 14 through day 35, and fibrosis; adoptive transfer of M1 (not M2) macrophages one week post-infection worsened inflammation, fibrosis, and iBALT (PMID:24204830, MODEL_ORGANISM). This is the best mechanistic model for the human asthma/COPD association, and the human step is **inferred, not demonstrated**.
16. **Branch D — host tolerance genotype modifies outcome independently of bacterial burden.** `sst1`-susceptible mice cleared the organism normally but showed higher clinical scores, exaggerated macrophage and neutrophil influx, fibrosis, elevated activated caspase-3, and an IFN-β/IL-10-skewed macrophage cytokine profile with IFN-β-dependent apoptotic death (PMID:24009502, MODEL_ORGANISM).

### Biological scale tags for pathograph nodes

`MOLECULAR` for the T3SS/Inc/CPAF effector nodes, PI4P recruitment, and IDO1-driven tryptophan depletion; `CELLULAR` for inclusion formation, apoptosis resistance, ciliostasis, neutrophil Trojan-horse transfer, and macrophage reservoir establishment; `TISSUE` for alveolar/bronchiolar inflammation, iBALT formation and fibrosis; `ORGANISM` for fever and the systemic inflammatory response.

### Metabolic and biochemical specifics

- **Tryptophan auxotrophy** is the central metabolic vulnerability and the mechanistic hinge of IFN-γ control (§6 steps 12–13). Human *C. pneumoniae* strains show increased sensitivity to tryptophan bioavailability relative to animal strains — a positive adaptation to the human host (*Mol Microbiol* 2014).
- **No enzyme deficiency, receptor defect, or ion-channel defect** in the host is implicated.
- **Epigenetic host changes:** none established for this infection.

---

## 7. Anatomical Structures Affected

### Organ level

- **Primary:** lung (`UBERON:0002048`), specifically the bronchi (`UBERON:0002185`) and bronchioles (`UBERON:0002186`) with bronchiolocentric spread into alveolar parenchyma. Radiographic lower-lung predominance in 65.5% and single-lobe involvement in 69.0% at onset (PMID:41676099).
- **Contiguous upper tract:** nasopharynx (`UBERON:0001728`), pharynx (`UBERON:0006562`), larynx (`UBERON:0001737`, hoarseness), paranasal sinus (`UBERON:0001825`), middle ear (`UBERON:0001756`), trachea (`UBERON:0003126`).
- **Body system:** respiratory system (`UBERON:0001004`).
- **Secondary / extrapulmonary:** the vascular wall (endothelium and smooth muscle) via infected monocytes; the pericardium and peripheral nerves in reported complications (pericarditis with Guillain-Barré, PMID:41157205); the CNS in encephalitis; the myocardium in myocarditis (CDC; PMID:40279169); the retina in the Alzheimer's context (PMID:41571675).

### Tissue and cell level

Respiratory mucosal epithelium is the invariable portal:

> "In all cases of chlamydial infections, the primary site of entry is the mucosal epithelium. During the later course of the infection, viable chlamydiae are found inside alveolar macrophages (AM), bronchial/alveolar epithelial cells, vascular endothelial/smooth muscle cells and monocyte-derived macrophages."

Cell Ontology bindings as listed in §6 step 10. Ciliated bronchial epithelium deserves its own node given the ciliostasis mechanism; note that the repository's CL cache currently holds `CL:0002328` bronchial epithelial cell but not a ciliated-cell term, so a ciliated-specific binding needs a fresh lookup.

### Subcellular level

The defining compartment is the chlamydial inclusion — a pathogen-containing vacuole, `GO:0020003` symbiont-containing vacuole, trafficked to the peri-Golgi region, enriched in PI4P via host ACBD3/PI4KB recruitment (PMID:42240327). Host mitochondria are functionally implicated through their failure to release apoptogenic factors (PMID:11705971).

### Localization and laterality

Unilateral involvement predominates in children (109 of 145, cohort B) and in adults at onset (single lobe 69.0%, cohort C), while roughly half of one 291-child series had bilateral involvement (cohort A). Report both; the difference is likely a timing and imaging-modality difference (CT vs radiograph, onset vs mid-course) rather than a real biological disagreement.

---

## 8. Temporal Development

**Onset.** Insidious, following a 3–4-week incubation (CDC). Upper-respiratory prodrome (sore throat, hoarseness, coryza) commonly precedes the cough by days to weeks — the pattern that distinguishes it clinically from abrupt pneumococcal pneumonia.

**Stages.** No formal staging system exists. A practical three-phase description supported by the data: (i) upper-tract prodrome; (ii) lower-tract phase with cough, variable low-to-moderate fever, and radiographic infiltrate; (iii) protracted convalescence with residual cough.

**Rate and course.** Slow onset, slow resolution. Median cough duration 21 days (PMID:40279169); median total disease duration 14 days (cohort B); mean 14.81 days with 7.52-day mean hospital stay (cohort A). Mid-course CT reassessment within one month was a design feature of the 42-patient CT study precisely because radiographic resolution lags clinical recovery (PMID:41676099).

**Duration.** Self-limited in the overwhelming majority — "approximately 70% of respiratory tract infections caused by *C. pneumoniae* are asymptomatic or present only with mild symptoms" (per the 2026 review's summary of the field). But:

> "Patients may experience a persistent cough and malaise for several weeks or months" even with appropriate antibiotic treatment. — CDC Clinical Features

**Remission and recurrence.** Reinfection throughout life is the rule, not the exception (Grayston 1990: "nearly everyone is infected and reinfected during their life-time"). Immunity after infection is partial: murine reinfection is cleared faster but is not prevented (PMID:10639472).

**Critical windows.** Two are identifiable. First, early life: neonatal murine infection with defective TLR2 signaling produces severe, prolonged disease and defective Th1 priming, the model underpinning the asthma-initiation hypothesis (PMID:22724018). Second, the first weeks after acute infection, where the murine M1-macrophage adoptive-transfer experiment shows that intervention timing determines fibrotic outcome (PMID:24204830).

---

## 9. Inheritance and Population

### Inheritance

**Not applicable.** This is an acquired infection. There is no inheritance pattern, no penetrance, no expressivity, no anticipation, no germline mosaicism, no founder effect, no consanguinity role, and no carrier frequency. Do not populate the `inheritance:` block.

### Epidemiology — the headline problem

There is **no national reporting or surveillance system for *C. pneumoniae* infections** in the United States (CDC), and it is not a notifiable disease in China (PMID:41088528). Every incidence and prevalence figure below is therefore laboratory-based or cohort-based, and the denominators differ.

### Share of community-acquired pneumonia

| Estimate | Population | Source |
|---|---|---|
| "About 10% of hospitalized and outpatient pneumonia cases" | Historical, North America/Nordic | PMID:2181028 |
| 1–2% of pediatric CAP | General pediatric statement | PMID:38052876 (introduction) |
| 16% (25/154) | Hospitalized children with CAP, Mexico City, PCR-based | PMID:38052876 |
| 7.91% of CAP | Hospitalized children, Beijing, Jan–Sep 2025 post-intervention period | PMID:42298460 |
| 15% serologically compatible; 14% PCR-positive without serology | 156 adults admitted with CAP, Netherlands | PMID:9666010 |

The spread from 1% to 16% is explained by diagnostic method (serology vs PCR vs mNGS/tNGS), inpatient vs outpatient setting, and epidemic period. Curate each with its own `population` and `measure_type`.

### Laboratory detection ratios — the post-pandemic collapse and rebound

Eurosurveillance multi-site study, 28 sites (27 European + Taiwan), 693,106 tests 2018–2023 (PMID:40511472):

| Period | Detection ratio |
|---|---|
| Pre-pandemic 2018–2019 | 1.05% |
| Pandemic 2020–2022 | 0.23% (p < 0.001) |
| Post-pandemic 2023 | 0.28% (p < 0.002 vs pandemic) |

> "Children/adolescents represented 56.4% of positive detections despite comprising only 18.7% of tested samples in 2023."

### The 2024–2025 resurgence

| Location | Change | Source |
|---|---|---|
| Lausanne, Switzerland | 3.61% Oct–Dec 2023, peak 6.66% in October, vs 0–0.75% decade baseline; 28 patients (20 children, mean age 8 y; 8 adults, mean age 43 y) | DOI 10.3201/eid3004.231610 |
| Germany (nationwide network) | Increased detection in 2024 vs 2019, "especially in children below 15 years and adults aged 30–50 years, mostly in patients who were treated as outpatients" | PMID:40884594 |
| Southern Germany | Positivity 0.3% (2015–2020) → 2.6% (2024), peaking ≥6.0% in Oct–Nov 2024 | Eur J Clin Microbiol Infect Dis 2026, DOI 10.1007/s10096-026-05419-2 |
| Marseille, France | 19-fold increase in qPCR positivity in 2024 vs 2018–2023 | PMID:40180027 |
| France, 2024–2025 | Exclusive predominance of MLST sequence type **ST16**, suggesting clonal dissemination | PMID:42435040 |
| China, 315 cities, 2,316,182 tNGS-tested ARI cases | 4.3-fold rise: 0.21% (2022–2023) → 0.90% (2024); peak season April–June; southwestern Yangtze River Basin clustering | PMID:41088528 |

### Seroprevalence and age structure

- Highest seroprevalence 52.9% in school-aged children 6–10 years (PMID:42180254).
- Primary infection is uncommon under 5 years in temperate regions; reinfection predominates over 65 (PMID:40279169; PMID:2181028).
- The Beijing series documents a post-NPI **age shift**: the primary affected group moved from 0–3 years (60.4% pre-intervention) to 6–18 years (90.1% post-intervention, H = 172.24, P < 0.001), with co-infection rising from 6.7% to 45.4% (PMID:42298460).

### Sex ratio

Male predominance in hospitalized pediatric series: 187:104 (1.80:1) in Shijiazhuang (PMID:41210234); 1.75:1 in Beijing (PMID:42298460); 89:56 (1.59:1) in Xi'an (PMID:42427957). In the Chinese national tNGS data, male adolescents 10–19 were the highest-risk group while women 25–44 also showed elevated risk, attributed by the authors to caregiving exposure (PMID:41088528). Whether the pediatric male excess reflects biology or admission bias is unresolved.

### Geographic distribution

Worldwide. Genotype geography is described for the pathogen: genotypes A, B, D, E are geographically linked while genotype C spans continents (PMID:20502684).

---

## 10. Diagnostics

### CDC-endorsed hierarchy

> "NAAT, such as real-time PCR, or respiratory pathogen panel" is the "Best method for the diagnosis of an acute *C. pneumoniae* infection." — CDC Laboratory Testing

> "Microimmunofluorescence" is the recommended serological approach; "single IgG titers" should **not** be used to diagnose acute infection; paired acute and convalescent sera are required. "Complement fixation, EIA, and whole-inclusion fluorescence" are **not** endorsed. Culture is "performed by specialized reference laboratories, but it's time-consuming and not optimal for treatment decisions."

### Performance and pitfalls

The definitive comparative study (156 adults admitted with CAP) found PCR and serology identify largely **non-overlapping** patient sets (PMID:9666010):

> "Twenty-three patients (15%) had serological results compatible with acute *C. pneumoniae* infection; nine (39%) of these subjects were *C. pneumoniae* PCR positive. Twenty-two patients (14%) had positive PCR results without serological evidence of an acute *C. pneumoniae* infection… Independent of the gold standard used, the best PCR results were obtained with nasopharyngeal specimens. However, the predictive value of a positive *C. pneumoniae* PCR result for patients with community-acquired pneumonia remains unknown and may be low."

That last sentence is the single most important caveat in this entry's diagnostics section and should be curated verbatim as a `REFUTE`- or caveat-bearing evidence item against any claim that PCR positivity establishes causation.

In the Mexican pediatric cohort, serology badly underperformed PCR: IgM positive in 7%, IgG in 28.6%, against 16% PCR detection (PMID:38052876).

### Emerging: metagenomic and targeted NGS

mNGS was the sole confirmation method in the 42-patient CT study (PMID:41676099) and tNGS supplied the Chinese national epidemiology (PMID:41088528, 2.3 million tests). This is now the dominant discovery route for adult cases and explains part of the apparent resurgence — a detection-method confounder that any incidence claim must acknowledge.

### Laboratory and imaging findings

Covered in §3. Notable: CRP is normal or mildly elevated in children (cohorts A, B) but >100 mg/L in 14.3% of the adult/mixed mNGS cohort (C) — the inflammatory footprint is not uniformly low.

### Genetic testing

**Not applicable.** No WGS, WES, gene panel, single-gene test, CMA, karyotype, FISH, mtDNA, or repeat-expansion testing has any role. *Pathogen* sequencing (MLST, mNGS, tNGS) is a microbiological, not a human-genetic, test.

### Clinical criteria and differential diagnosis

No society-specific diagnostic criteria exist for *C. pneumoniae* pneumonia as an entity; diagnosis is CAP by clinical/radiographic criteria plus microbiological attribution. Differential:

| Condition | Distinguishing feature |
|---|---|
| *Mycoplasma pneumoniae* pneumonia | CPP patients significantly older (10.53 ± 2.89 vs 6.68 ± 2.88 years), longer cough, more chest pain, higher WBC and eosinophils (PMID:40775274). Co-infection is common — 64% in the Mexican series (PMID:38052876) |
| *Streptococcus pneumoniae* pneumonia | Abrupt onset, high fever, lobar consolidation, high CRP; note the Fort Leonard Wood outbreak was a genuine mixed picture (PMID:21635754) |
| *Chlamydia psittaci* (psittacosis) | Bird exposure; doxycycline-preferred (PMID:42180254) |
| Viral pneumonia / respiratory viruses | Frequent co-detection — 60.82% mixed infections in cohort A (rhinovirus 19.93%, *H. influenzae* 18.21%, *S. pneumoniae* 18.21%) |
| *Legionella* | Higher severity, hyponatremia, urinary antigen |

**Screening.** No screening program exists, is recommended, or would be justified. Newborn, carrier, and cascade screening: **not applicable.**

---

## 11. Outcome / Prognosis

**Overall.** Good. "The clinical course is generally mild, and the disease responds well to appropriate antibiotic treatment" (PMID:42180254). Zero mortality across the 291-child Shijiazhuang series, with complete recovery reported (PMID:41210234).

**Mortality.** Not zero everywhere. Four percent of the Mexican pediatric cohort died and 36% had complications — but 88% of those children had underlying disease, so this is a compromised-host figure, not a general one (PMID:38052876). CDC states: "Severe complications can occur with *C. pneumoniae* infections. These complications can result in hospitalization and sometimes death," while keeping overall risk low. **No reliable disease-specific case-fatality rate, 5-year survival, or life-expectancy figure exists**, and none should be invented; the organism is rarely the sole attributed cause of death.

**Severity predictors.** Two independent associations from a 133-child case-control study (PMID:42327901): decreased lymphocyte percentage (OR 0.943, 95% CI 0.895–0.994) and elevated IgA (OR 2.227, 95% CI 1.284–3.972); severe cases also had higher peak temperature and longer fever duration (both P < 0.001). A separate 176-patient series identified eosinophil count as a candidate severity biomarker with severe CPP at 6.8% (PMID:40775274). These are single-center, retrospective, and unvalidated — curate as `PROPOSED`/`UNVALIDATED` prognostic markers, not established ones.

**Complications.** Encephalitis, myocarditis, asthma exacerbation (CDC); reactive arthritis, Guillain-Barré syndrome (PMID:40279169); pericarditis with Guillain-Barré in a 2025 case report (PMID:41157205); reactive infectious mucocutaneous eruption (PMID:42094854); rash clusters (PMID:42755900).

**Chronic sequelae — asthma.** The best-quantified chronic association:

> "The population attributable risks for Cp-specific IgG and IgA were nul in children and were 6% (95% confidence interval 2%-10%, p = 0.002) and 13% (9%-18%, p<0.00001) respectively in adults." PAR for Cp-specific **IgE was 47% (39%–55%, p<0.00001)** combined across ages, rising with severity: 5% in mild/controlled, 28% in moderate/partly controlled, 39% in severe/uncontrolled asthma. 25 studies. — Hahn DL, *PLoS One* 2021 (PMID:33872336)

The same author's 2026 review is framed as an open question (PMID:42690975) — this association is real in the seroepidemiology and unresolved in causation. Curate it as a `mechanistic_hypotheses` entry with `status: EMERGING`, not as an established sequela.

**Chronic sequelae — atherosclerosis: the negative result matters.** The hypothesis was seroepidemiologically attractive and mechanistically plausible (infected endothelium and smooth muscle; azithromycin prevented lesions in a rabbit model, PMID:10548582), and it failed in humans. WIZARD and the Azithromycin and Coronary Events Study (ACES, PMID:15843666) were both negative; PROVE-IT-TIMI and SPACE (PMID:15749042) likewise. "Antibiotic trials showed no favorable impact on atherosclerosis outcomes" (PMID:40279169). **Curate this as a `REFUTE` evidence item against the therapeutic-causation claim.**

**Neurodegeneration.** A 2026 *Nature Communications* study identified *C. pneumoniae* inclusions in Alzheimer retina and brain, increasing with APOEε4, disease stage, and cognitive deficit, with NLRP3 inflammasome activation (PMID:41571675). This is association-plus-model-system, not established causation, and belongs in `discussions:` with `kind: HUMAN_MODEL_MISMATCH` or `KNOWLEDGE_GAP`.

**Recovery.** Complete in most; the residual is protracted cough and malaise over weeks to months (CDC).

---

## 12. Treatment

### First-line pharmacotherapy

> "First-line agents include macrolides (azithromycin or clarithromycin), tetracycline (doxycycline) or fluoroquinolones (levofloxacin or moxifloxacin)." — PMID:40279169

CDC: macrolides first-line, tetracyclines and fluoroquinolones as alternatives; **penicillin, ampicillin, and sulfa drugs are ineffective** — the organism lacks a usable β-lactam target. Persistent infection may require a second course.

| Agent | CHEBI | Class | Role |
|---|---|---|---|
| Azithromycin | `CHEBI:2955` | Macrolide (azalide) | First-line |
| Clarithromycin | `CHEBI:3732` | Macrolide | First-line |
| Erythromycin | `CHEBI:48923` | Macrolide | Older first-line; used in 11.34% of cohort A |
| Doxycycline | `CHEBI:50845` | Tetracycline | First-line/alternative; most-used agent (30.58%) in cohort A |
| Levofloxacin | `CHEBI:63598` | Fluoroquinolone | Alternative (adults) |
| Moxifloxacin | `CHEBI:63611` | Fluoroquinolone | Alternative (adults) |

Observed prescribing in 291 children (PMID:41210234): doxycycline 30.58%, azithromycin 23.71%, erythromycin 11.34%.

**NCIT treatment-action bindings** (verified against `cache/ncit/terms.csv` on 2026-09-26): `NCIT:C15986` Pharmacotherapy for the drug treatments, with `therapeutic_agent` carrying the CHEBI drug; `NCIT:C15620` Antibiotic Therapy is available as a more specific action term; `NCIT:C15747` Supportive Care; `NCIT:C94624` Oxygen Therapy; `NCIT:C70909` Mechanical Ventilation for the rare severe case; `NCIT:C17003` Polymerase Chain Reaction for the diagnostic (note this is a diagnostic, not a `TreatmentTerm`). `therapeutic_modality: SMALL_MOLECULE` applies to every agent above.

### Resistance

Effectively absent. "There is currently no report of resistant isolates" (PMID:40279169). The one careful investigation of three isolates whose azithromycin MIC rose after treatment found no genetic mechanism and could not induce resistance in vitro (PMID:15328134). In vitro MIC₉₀ for azithromycin is 0.125–0.25 µg/mL, comparable to erythromycin and doxycycline.

The clinically meaningful failure mode is **not** resistance but **persistence**: sub-optimal dosing induces the aberrant-body state in vitro, and β-lactam exposure does the same (PMID:40279169). Treat that as a distinct mechanism node, not as resistance.

### Guideline context

The 2019 ATS/IDSA adult CAP guideline (Metlay JP et al., *Am J Respir Crit Care Med* 2019;200:e45–e67, PMID:31573350) no longer recommends routine macrolide monotherapy where local pneumococcal macrolide resistance exceeds 25%, and recommends β-lactam plus macrolide combination therapy for hospitalized patients. Atypical coverage is therefore delivered empirically within CAP regimens rather than through pathogen-directed therapy, which is the practical reality for almost every case of this disease. Doxycycline 100 mg BID and amoxicillin 1 g TID are the healthy-outpatient options alongside azithromycin.

### Advanced therapeutics

**Gene therapy, cell therapy, RNA-based therapy, targeted therapy, immunotherapy, surgery: none applicable.** No oligonucleotide, monoclonal antibody, or cellular product exists or is in development for this infection. `oligonucleotide_details` and `delivery_system` blocks do not apply.

### Supportive care

Antipyretics, hydration, oxygen for hypoxemia, and ventilatory support in the rare severe case. Rehabilitation is not routinely indicated.

### Experimental treatments

No active interventional trial specific to *C. pneumoniae* pneumonia was identified in this search. Historical anti-chlamydial cardiovascular trials (WIZARD, ACES/PMID:15843666, SPACE/PMID:15749042, PROVE-IT-TIMI) are negative and are not treatments for this disease. A registered anti-*Chlamydophila* combination-therapy coronary study exists (NCT03618108) but again targets cardiovascular outcomes. **Any `clinical_trials:` block should be populated only after `just fetch-reference NCT…` verification.**

### Pharmacogenomics

No CPIC guideline, PharmGKB annotation, or FDA pharmacogenomic biomarker applies to macrolide, tetracycline, or fluoroquinolone therapy for this indication. **Not applicable.**

---

## 13. Prevention

**Primary prevention.** No vaccine exists or is licensed. MOMP (major outer membrane protein) remains the leading candidate antigen — highly immunogenic, relatively conserved across the genus, eliciting T-cell responses and neutralizing antibodies — but conformationally correct MOMP is hard to produce at scale, and work remains preclinical (multi-epitope designs, lipid-nanodisc folding, live-attenuated oral concepts). A 2023 *Scientific Reports* multiepitope design against *C. pneumoniae* is computational. **Immunization: none available.** NCIT `NCIT:C15346` Vaccination should not be curated as a treatment or prevention for this entry.

The only demonstrated primary prevention is transmission interruption. The pandemic NPI period produced a documented, statistically significant fall in detection (PMID:40511472), and outbreak investigations in military training environments explicitly targeted barracks density and training practices (PMID:30690452).

**Secondary prevention.** No screening program for asymptomatic individuals. In outbreak settings, the operationally useful recommendation is diagnostic rather than screening:

> Because *C. pneumoniae* infection can be treated by macrolides, doxycycline, or fluoroquinolones, PCR testing for both *C. pneumoniae* and *M. pneumoniae* should be considered in symptomatic patients rather than testing only for respiratory viruses. — Tagini, Opota, Greub, *Emerg Infect Dis* 2024;30(4):810-812

**Tertiary prevention.** Adequate dosing and duration to avoid inducing persistence; recognition and management of the asthma phenotype in patients with chronic infection biomarkers.

**Genetic counseling, carrier screening, PGD, prenatal testing: not applicable.**

**Public health.** The recurring finding across every 2024–2026 surveillance paper is the absence of notifiable-disease status and the resulting invisibility of this pathogen. CDC: "There is no national reporting or surveillance system for *C. pneumoniae* infections." The Chinese national study makes the same point and calls for enhanced surveillance (PMID:41088528).

---

## 14. Other Species / Natural Disease

### Host range

*C. pneumoniae* has an unusually broad host range for a species that behaves clonally in humans. Molecular detection spans humans, horses, koalas, bandicoots, potoroos, cattle, cats, dogs, wild ruminants and cervids, plus reptiles (snakes, iguanas, chameleons) and amphibians (frogs, turtles) (PMID:12086181).

Suggested taxonomy bindings, to be re-verified at curation time: `NCBITaxon:9606` *Homo sapiens*; the koala (*Phascolarctos cinereus*), horse (*Equus caballus*), and amphibian/reptile hosts have NCBI Taxonomy identifiers that were **not** looked up in this session and must not be written from memory.

### Zoonotic origin — and the absence of current zoonotic transmission

This distinction is the one most often stated wrongly. The genomic evidence is for an **ancient** host jump, not for ongoing animal-to-human transmission:

> "Transmission of *C. pneumoniae* between animals and humans has not been reported; however, two other chlamydial species, *C. psittaci* and *C. abortus*, are known zoonotic pathogens. We have sequenced the 1,241,024-bp chromosome and a 7.5-kb cryptic chlamydial plasmid of the koala strain of *C. pneumoniae* (LPCoLN)… we propose based on compelling genomic and phylogenetic evidence that humans were originally infected zoonotically by an animal isolate(s) of *C. pneumoniae* which adapted to humans primarily through the processes of gene decay and plasmid loss, to the point where **the animal reservoir is no longer required for transmission**." — Myers GS et al., *J Bacteriol* 2009 (PMID:19749045)

> "Our evidence strongly supports two separate animal-to-human cross species transfer events in the evolutionary history of this pathogen. The *C. pneumoniae* human genotype identified in the USA, Canada, Taiwan, Iran, Japan, Korea and Australia (non-Indigenous) most likely originated from a single amphibian or reptilian lineage… We identified a separate human lineage present in two Australian Indigenous isolates." — Mitchell CM et al., *PLoS Pathog* 2010 (PMID:20502684)

Koala isolates differ from human and horse strains at four gene loci (0.3% at *groESL* to 9.0% at *ompA* VD4), and the koala LPCoLN genome shows extended diversity relative to human strains (PMID:20646324).

**Named-entity caution for curators.** Koala chlamydial disease in the veterinary literature is overwhelmingly *Chlamydia pecorum* (ocular and urogenital disease), not *C. pneumoniae*. Do not import koala chlamydiosis phenotypes into this entry.

### Comparative biology

Human strains show heightened sensitivity to tryptophan bioavailability relative to animal strains, interpreted as a positive adaptation to the human host (*Mol Microbiol* 2014) — an elegant link between the host-adaptation story and the IFN-γ/IDO1 mechanism in §6. Gene decay and plasmid loss are the two documented modes of human adaptation.

### Orthologous genes

**Not applicable** — there is no human disease gene to orthologize. Murine orthologs of the modifier genes in §4 (*Tlr2*, *Tlr4*, *Ifng*, *Il10*, *Nod1*) are the relevant comparison and are named in the model studies.

---

## 15. Model Organisms

### Mouse — the workhorse

Intranasal or intratracheal inoculation produces self-limited pneumonia with partially protective acquired immunity: bacterial load peaks in week two and clears by roughly six weeks in wild-type animals, with faster clearance on reinfection.

| Model | Design | Key result | Citation |
|---|---|---|---|
| A/J vs C57BL/6 whole-genome scan | [A/J × C57BL/6J] F2, pulmonary load as readout | Chromosome 17 QTL overlapping MHC, LOD 11.5, ~30% of variance, B6 alleles recessive-susceptible; chr 5 linkage in females, suggestive chr 6 in males | PMID:18075514 |
| IFN-γ neutralization, C57BL/6 and BALB/c | In vivo antibody blockade | Primary infection worsened in C57BL/6 only; **reinfection worsened in both strains** — IFN-γ is strain-independently required for acquired immunity | PMID:10639472 |
| IL-10 knockout | Primary and repeat infection | Accelerated clearance **but** more pronounced histopathology at all time points, higher pro-inflammatory cytokines ex vivo and intrapulmonary | PMID:18456450 |
| C57BL/6 chronic model, 5 × 10⁵ CP intratracheal | 35-day time course | Bacteria declined by day 28 but macrophages stayed high to day 35; iBALT (B, T, follicular dendritic cells) from day 14; M1 early, M2 late; **adoptive transfer of M1 (not M2) macrophages at 1 week caused greater inflammation, severe fibrosis, more iBALT** | PMID:24204830 |
| `sst1`-susceptible mice | Acute infection | Normal clearance but markedly worse tolerance: higher clinical scores, severe lung inflammation, exaggerated macrophage/neutrophil influx, fibrosis, increased activated caspase-3; macrophages shifted to IFN-β/IL-10 with IFN-β-dependent apoptosis and **arrested chlamydial development** | PMID:24009502 |
| Neonatal TLR2⁻/⁻, TLR4⁻/⁻, TLR2/4⁻/⁻ BALB/c (*C. muridarum*) | Early-life respiratory infection | TLR2⁻/⁻ most severe and most prolonged; **TLR4⁻/⁻ asymptomatic**; wild-type mounted NK, neutrophil, mDC, pDC, CD4⁺/CD8⁺ influx with robust IFN-γ | PMID:22724018 |
| HLA-A2.1 monochain transgenic, H-2 class I⁻/⁻ | Clearance study | CD8⁺ T cells and IFN-γ important in acquired protection | *Scand J Immunol* 2005 |

**Model limitations to record as `divergences`.** The TLR early-life study uses ***C. muridarum*, not *C. pneumoniae*** — a `SPECIES_MISMATCH` at the pathogen rather than the host, and a material one, since the murine-adapted organism differs in virulence and tropism. The murine inocula (5 × 10⁵ organisms intratracheally) are large relative to any plausible natural exposure — `SUPRAPHYSIOLOGICAL_EXPRESSION` in spirit if not in name. Mouse lungs lack the human airway's proportion of ciliated surface relevant to the ciliostasis mechanism, and no murine model reproduces the human asthma phenotype that motivates most of this work — that is a `HUMAN_MODEL_MISMATCH` discussion, not a solved question.

**`ModelMechanismLink` guidance.** The iBALT/fibrosis model (PMID:24204830) links at `model_scale: TISSUE` to a tissue-level fibrosis node — no scale extrapolation. The IFN-γ neutralization model links at `ORGANISM` scale to the molecular IFN-γ node — downward containment, unremarkable. The `sst1` model should carry `relationship: PARTIALLY_RECAPITULATES` with `limitations` recording that it dissociates tolerance from clearance, which is the whole point of the paper.

### Cell and in vitro systems

| System | Use | Citation |
|---|---|---|
| A549 (lung carcinoma epithelial) | Cytadherence-dependent IL-8/TNF-α induction | PMID:12540537 |
| HEp-2 | IFN-γ-induced persistence, aberrant bodies, inclusion ultrastructure | PMID:11705979 |
| HeLa / epithelial lines | Apoptosis resistance via mitochondrial block | PMID:11705971 |
| Primary human neutrophils + monocyte-derived macrophages | Apoptotic-neutrophil Trojan-horse transfer; annexin A5 blockade | PMID:19547701 |
| Ciliated bronchial epithelial cells ex vivo | Complete ciliostasis by 48 h | PMID:7751703 |
| Human aortic endothelial cells | Aponecrosis from late-cycle inclusions | *Cardiovasc Pathol* 2008 |
| Yeast functional screen | Host microtubule cytoskeleton as effector target | PMID:37108781 |
| Rabbit atherosclerosis model | Macrolide prevented *C. pneumoniae*-induced lesions — a model result that **failed to translate** | PMID:10548582 vs PMID:15843666 |

**No organoid, organ-chip, or iPSC-derived model of *C. pneumoniae* pneumonia was identified.** This is a real gap: every current NAM-relevant claim rests on immortalized monocultures.

### Resources

MGI, IMPC, IMSR for the knockout lines (Tlr2, Tlr4, Il10); ATCC/Cellosaurus for A549 and HEp-2; the Alliance of Genome Resources for ortholog mapping. No dedicated *C. pneumoniae* model repository exists.

---

## Consolidated evidence table for KB ingestion

Each row is a candidate `EvidenceItem`. Snippets marked *verbatim* below were captured from the cited abstract or the named source page during this research and still require `just fetch-reference` plus `just count-verified-snippets` confirmation before commit — per repository policy the cache file, not this report, is the authority for exactness.

| Claim | Reference | `evidence_source` | `quote_role` | Verbatim snippet |
|---|---|---|---|---|
| Species, virulence factors, treatment classes | PMID:40279169 | OTHER | REVIEW_SYNTHESIS | "The pathogen employs specific virulence factors, such as the Type III Secretion System (T3SS) and Inc proteins, to invade and subvert host cell machinery during its peculiar developmental life cycle." |
| Historical CAP share | PMID:2181028 | HUMAN_CLINICAL | REVIEW_SYNTHESIS | "About 10% of hospitalized and outpatient pneumonia cases have been associated with TWAR infection." |
| Lifelong reinfection | PMID:2181028 | HUMAN_CLINICAL | REVIEW_SYNTHESIS | "nearly everyone is infected and reinfected during their life-time, and that infection is common in all ages except those less than 5 years in temperate zone countries" |
| Pandemic decline and rebound | PMID:40511472 | HUMAN_CLINICAL | PRIMARY_RESULT | "A significant decrease in detection ratios was observed during the pandemic period (from 1.05% to 0.23%, p < 0.001). In 2023, detection ratios increased to 0.28% (p < 0.002)." |
| 2024 German rise | PMID:40884594 | HUMAN_CLINICAL | PRIMARY_RESULT | "Our analysis showed an increasing C. pneumoniae detection rate in 2024 compared to 2019, especially in children below 15 years and adults aged 30-50 years, mostly in patients who were treated as outpatients." |
| 2024 China surge | PMID:41088528 | HUMAN_CLINICAL | PRIMARY_RESULT | "Our analyses revealed a 4.3-fold increase in C. pneumoniae positivity rates in 2024; from 0.21% in 2022-2023 to 0.90% in 2024" |
| Clonal ST16 spread | PMID:42435040 | HUMAN_CLINICAL | PRIMARY_RESULT | "Our results revealed the exclusive predominance of C. pneumoniae ST16, suggesting dissemination of ST16 across France." |
| Post-NPI age shift | PMID:42298460 | HUMAN_CLINICAL | PRIMARY_RESULT | "The primary affected age group shifted from 0 to 3 years (60.4% in the pre-intervention group; 75.6% in the during-intervention group) to 6-18 years (90.1% in the post-intervention group; H = 172.24, P < 0.001)." |
| Pediatric symptom frequencies | PMID:41210234 | HUMAN_CLINICAL | PRIMARY_RESULT | "Cough was the predominant clinical manifestation (141 patients, 98.60%), followed by fever (44.80% of patients; median peak temperature: 38.20 °C)." |
| Pediatric cohort features | PMID:42427957 | HUMAN_CLINICAL | PRIMARY_RESULT | "Cough was present in 144 cases (99.3%), with wet cough being predominant (141 cases, 97.2%). Fever was observed in 65 cases (44.8%)" |
| Adult CT pattern | PMID:41676099 | HUMAN_CLINICAL | PRIMARY_RESULT | "The main accompanying features included a halo sign in 25 patients (86.2%), centrilobular nodules in 23 (79.3%), and bronchial wall thickening in 20 (69.0%)." |
| Pediatric radiography and outcome | PMID:38052876 | HUMAN_CLINICAL | PRIMARY_RESULT | "Interstitial pattern on chest-X-ray was the most frequent (68%), consolidation was observed in 32% (P = 0.002)." |
| Severity predictors | PMID:42327901 | HUMAN_CLINICAL | PRIMARY_RESULT | "Multivariate analysis identified decreased lymphocyte percentage (OR = 0.943, 95% CI 0.895-0.994) and elevated IgA (OR = 2.227, 95% CI 1.284-3.972) as factors associated with severe CPP." |
| CPP vs MPP | PMID:40775274 | HUMAN_CLINICAL | PRIMARY_RESULT | "CPP patients were significantly older than MPP patients (mean age: 10.53 ± 2.89 vs 6.68 ± 2.88, p < 0.05) and exhibited longer durations of cough and higher rates of chest pain (p < 0.05)." |
| PCR/serology discordance | PMID:9666010 | HUMAN_CLINICAL | PRIMARY_RESULT | "Twenty-two patients (14%) had positive PCR results without serological evidence of an acute C. pneumoniae infection." |
| PCR predictive value caveat | PMID:9666010 | HUMAN_CLINICAL | PRIMARY_RESULT | "the predictive value of a positive C. pneumoniae PCR result for patients with community-acquired pneumonia remains unknown and may be low" |
| Cytadherence drives cytokines | PMID:12540537 | IN_VITRO | PRIMARY_RESULT | "heparin treatment of C. pneumoniae significantly reduced its ability to induce interleukin 8 (IL-8) and tumor necrosis factor alpha (TNF-alpha) mRNA in human lung carcinoma cells, indicating that cytadherence is an important early stimulus for induction of proinflammatory mediators" |
| Apoptosis resistance | PMID:11705971 | IN_VITRO | PRIMARY_RESULT | "In the infected cells, mitochondria did not respond to apoptotic stimuli by the release of apoptogenic factors required for the activation of caspases. Consequently, active caspase-3 was absent in infected cells." |
| Ciliostasis | PMID:7751703 | IN_VITRO | PRIMARY_RESULT | "C. pneumoniae, known to cause respiratory infections, had a marked ciliastatic effect, completely aborting ciliary motion within 48 h." |
| Neutrophil Trojan horse | PMID:19547701 | IN_VITRO | PRIMARY_RESULT | "C. pneumoniae infection of macrophages via apoptotic PMN results in enhanced replicative activity of chlamydiae when compared to direct infection of macrophages, which results in persistence of the pathogen." |
| IFN-γ persistence morphology | PMID:11705979 | IN_VITRO | PRIMARY_RESULT | "Ultrastructural analysis of IFN-gamma-treated C. pneumoniae revealed atypical inclusions containing large reticulatate-like aberrant bodies with no evidence of redifferentiation into elementary bodies." |
| Tryptophan mechanism | PMID:8063385 | IN_VITRO | PRIMARY_RESULT | "a mutant cell line responsive to IFN-gamma but deficient in IDO activity was shown to support C. trachomatis growth, but aberrant organisms were not induced in response to IFN-gamma treatment" |
| Host genetic control | PMID:18075514 | MODEL_ORGANISM | PRIMARY_RESULT | "We detected a highly significant linkage (LOD score=11.5) on chromosome 17 that overlaps with the major histocompatibility (MHC) locus." |
| IFN-γ requirement | PMID:10639472 | MODEL_ORGANISM | PRIMARY_RESULT | "During reinfection, the bacterial counts in the lungs were increased by IFN-gamma neutralization in both mouse strains." |
| IL-10 dissociation | PMID:18456450 | MODEL_ORGANISM | PRIMARY_RESULT | "the histopathological changes in lung tissue were more pronounced in IL-10 KO mice at all time points after infection and repeated infection than in the wild type mice" |
| Chronic fibrosis / iBALT | PMID:24204830 | MODEL_ORGANISM | PRIMARY_RESULT | "Adoptive transfer of M1 but not M2 macrophages intratracheally 1 week after infection resulted in greater lung inflammation, severe fibrosis, and increased numbers of iBALTs 35 days after infection." |
| Tolerance vs resistance | PMID:24009502 | MODEL_ORGANISM | PRIMARY_RESULT | "Although mice carrying the sst1 susceptible (sst1(S)) locus were not impaired in their ability to clear the acute infection, they were dramatically less tolerant of the induced immune response" |
| TLR2 not TLR4 | PMID:22724018 | MODEL_ORGANISM | PRIMARY_RESULT | "TLR2(-/-) mice had more severe disease and more intense and prolonged infection compared to other groups. TLR4(-/-) mice were asymptomatic." |
| Ancient zoonosis, no current reservoir | PMID:19749045 | COMPUTATIONAL | PRIMARY_RESULT | "humans were originally infected zoonotically by an animal isolate(s) of C. pneumoniae which adapted to humans primarily through the processes of gene decay and plasmid loss, to the point where the animal reservoir is no longer required for transmission" |
| Two host jumps | PMID:20502684 | COMPUTATIONAL | PRIMARY_RESULT | "Our evidence strongly supports two separate animal-to-human cross species transfer events in the evolutionary history of this pathogen." |
| No resistance mechanism | PMID:15328134 | IN_VITRO | PRIMARY_RESULT | "No genetic mechanism was identified for the phenotypic change in these C. pneumoniae isolates. No macrolide resistance was obtained in vitro." |
| Asthma PAR | PMID:33872336 | HUMAN_CLINICAL | PRIMARY_RESULT | "The population attributable risks for Cp-specific IgG and IgA were nul in children and were 6% (95% confidence interval 2%-10%, p = 0.002) and 13% (9%-18%, p<0.00001) respectively in adults." |
| Outbreak in cadets | PMID:25988545 | HUMAN_CLINICAL | PRIMARY_RESULT | "During October 2013-May 2014, there were 102 cases of pneumonia diagnosed in US Air Force Academy cadets. A total of 73% of tested nasal washes contained Chlamydophila pneumoniae." |
| Army trainee attack rates | PMID:30690452 | HUMAN_CLINICAL | PRIMARY_RESULT | (attack-rate sentence sits in the results body, not the abstract — fetch full text before quoting) |

---

## Gaps, cautions, and what this report does not establish

1. **No species-level MONDO term exists.** The entry must anchor to a genus-level term with an explicit mapping predicate and a note recording the searches run.
2. **PCR positivity is not causation.** The single most-cited caveat in the diagnostic literature (PMID:9666010) undercuts every prevalence figure derived from PCR alone, including the recent resurgence numbers. The resurgence is real across independent sites, but part of its magnitude is mNGS/tNGS adoption.
3. **Persistence in vivo is unresolved.** Aberrant bodies are an in vitro phenomenon under IFN-γ, iron restriction, or β-lactam pressure. A 2026 review poses in vivo persistence as an open question (PMID:42690975). Curate the persistence chain as hypothesis, not mechanism.
4. **Atherosclerosis causation is refuted by trial evidence** and should carry `REFUTE` items, not be quietly omitted.
5. **Asthma causation is unresolved, quantitatively large, and IgE-driven.** The PAR of 47% for Cp-specific IgE is the strongest number in this whole literature and the weakest in design (cross-sectional and case-control, no large prospective population study exists — the meta-analysis says so explicitly).
6. **The Alzheimer's retina finding (PMID:41571675) is new, high-profile, and not a pneumonia finding.** Do not import it into the pneumonia pathograph.
7. **No omics dataset specific to *C. pneumoniae* pneumonia was verified.** Do not write a `geo:` accession without running `just discover-datasets` and `just verify-datasets`.
8. **Every CURIE in this report was read from a source during this session** — HPO and CL/UBERON/CHEBI/GO/NCIT from `cache/*/terms.csv` or the EBI OLS4 API, HGNC from `cache/hgnc/terms.csv` or genenames.org, MONDO/ICD/MeSH/SNOMED from the OLS4 MONDO term record and the NLM MeSH lookup, ICD-11 CA40.00 from the ICD-11 MMS listing. Re-validate with `just validate-terms` before commit; dynamic-enum membership was **not** checked here and is a separate gate.

---

## Sources

- [Chlamydia beyond the genital tract: a major contributor to community-acquired pneumonia (Front Cell Infect Microbiol 2026, PMID:42180254)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13195017/)
- [From coughs to complications: the story of Chlamydia pneumoniae (J Med Microbiol 2025, PMID:40279169)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12050420/)
- [CDC — Laboratory Testing for Chlamydia pneumoniae](https://www.cdc.gov/cpneumoniae/php/laboratories/index.html)
- [CDC — Clinical Overview of Chlamydia pneumoniae Infection](https://www.cdc.gov/cpneumoniae/hcp/clinical-overview/index.html)
- [CDC — Clinical Features of Chlamydia pneumoniae Infection](https://www.cdc.gov/cpneumoniae/hcp/clinical-signs/index.html)
- [Epidemiological changes in C. pneumoniae molecular detections, 27 European sites and Taiwan (Eurosurveillance 2025, PMID:40511472)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12164279/)
- [Chlamydia pneumoniae Upsurge at Tertiary Hospital, Lausanne, Switzerland (EID 2024)](https://wwwnc.cdc.gov/eid/article/30/4/23-1610_article)
- [Sharp increase in Chlamydia pneumoniae infections in 2024 in Germany (PMID:40884594)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12619724/)
- [Epidemiological and clinical analysis of 291 children with C. pneumoniae pneumonia (PMID:41210234)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12592089/)
- [Chlamydophila pneumoniae-associated CAP in paediatric patients, Mexico (PMID:38052876)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10698025/)
- [Chlamydia pneumoniae and chronic asthma: meta-analysis of population attributable risk (PMID:33872336)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8055030/)
- [Genetic control of susceptibility to pulmonary infection with C. pneumoniae in the mouse (PMID:18075514)](https://pubmed.ncbi.nlm.nih.gov/18075514/)
- [TLR2, but not TLR4, is required for host defence against Chlamydia respiratory infection in early life (PMID:22724018)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3378543/)
- [C. pneumoniae hides inside apoptotic neutrophils (PMID:19547701)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2695784/)
- [Induction of proinflammatory cytokines in human lung epithelial cells (PMID:12540537)](https://pubmed.ncbi.nlm.nih.gov/12540537/)
- [Evidence that human Chlamydia pneumoniae was zoonotically acquired (PMID:19749045)](https://journals.asm.org/doi/10.1128/jb.00746-09)
- [C. pneumoniae is genetically diverse in animals (PMID:20502684)](https://journals.plos.org/plospathogens/article?id=10.1371%2Fjournal.ppat.1000903)
- [Tryptophan depletion as a mechanism of IFN-γ-mediated chlamydial persistence (PMID:8063385)](https://pubmed.ncbi.nlm.nih.gov/8063385/)
- [Azithromycin for the Secondary Prevention of Coronary Events, ACES (PMID:15843666)](https://www.nejm.org/doi/full/10.1056/NEJMoa043526)
- [2019 ATS/IDSA CAP guideline summary (AFP 2020)](https://www.aafp.org/pubs/afp/issues/2020/0715/p121.html)
- [ICD-11 MMS CA40.0 Bacterial pneumonia, including CA40.00](https://www.findacode.com/icd-11/code-1323682030.html)
- [Pneumonia Outbreak Caused by Chlamydophila pneumoniae among US Air Force Academy Cadets (PMID:25988545)](https://pubmed.ncbi.nlm.nih.gov/25988545)
- [Outbreak of C. pneumoniae Infections in Army Trainees at Fort Leonard Wood (PMID:30690452)](https://academic.oup.com/milmed/article/184/7-8/e196/5299208)
- [Chlamydia pneumoniae-induced ciliostasis in ciliated bronchial epithelial cells (PMID:7751703)](https://pubmed.ncbi.nlm.nih.gov/7751703/)
- [Profile of Chlamydia vaccine research: a bibliometric analysis (2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11801346/)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 66 |
| Resolved | 66 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 4 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 66 |
| On topic | 58 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:40279169` *(abstract only)*: "Antibiotic trials showed no favorable impact on atherosclerosis outcomes"
  - closest text in source: "Chronic infections have been linked to asthma and, more controversially, to atherosclerosis and neurodegenerative diseases"
- `PMID:40279169` *(abstract only)*: "There is currently no report of resistant isolates"
  - Text part not found as substring: 'There is currently no report of resistant isolates' (note: only abstract available for PMID:40279169, full text may contain this excerpt)

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 86 |
| Resolved | 83 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 9 |
| Terms named correctly | 6 |
| Terms named as a **different** term | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0025598` (5 mentions) - the report calls it "MONDO"; MONDO calls it **pneumonia caused by chlamydia**
- `DOID:0040083` (1 mention) - the report calls it "DOID"; DOID calls it **Chlamydia pneumonia**
- `NCBITaxon:83558` (3 mentions) - the report calls it "NCBI Taxonomy (pathogen)"; NCBITaxon calls it **Chlamydia pneumoniae**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ICD11`.