---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-31T16:35:21.898036'
end_time: '2026-10-31T16:38:57.121021'
duration_seconds: 215.22
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: STAT3-Related Early-Onset Multisystem Autoimmune Disease
  mondo_id: MONDO:0014414
  category: Mendelian
  causal_genes: STAT3
  omim_id: OMIM:615952
  synonyms: STAT3 gain-of-function disease; infantile-onset multisystem autoimmune
    disease 1; ADMIO1
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
  web_search_requests: 15
  num_turns: 28
  total_cost_usd: 2.5314051
  session_id: 2ccff955-20d8-5bb4-8e86-b52d55e2a947
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  assistant_text_blocks: 2
citation_count: 16
reference_validation:
  total_references: 19
  verified: 19
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 4
  quotes_valid: 3
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:29477724
  relevance_assessed: 19
  on_topic: 17
  needs_review: true
  validator_version: 0.4.0
term_validation:
  total_terms: 53
  verified: 52
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: NCIT:C15986
    reported_labels:
    - Endocrine organ failure
    ontology_label: Pharmacotherapy
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** STAT3-Related Early-Onset Multisystem Autoimmune Disease
- **MONDO ID:** MONDO:0014414 (if available)
- **Causal gene(s):** STAT3
- **OMIM:** OMIM:615952
- **Synonyms:** STAT3 gain-of-function disease; infantile-onset multisystem autoimmune disease 1; ADMIO1
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **STAT3-Related Early-Onset Multisystem Autoimmune Disease** covering all of the
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

Looking for existing STAT3 material in the repo, then running web searches for the report.

I have enough sourced material and am writing the report now.

# STAT3-Related Early-Onset Multisystem Autoimmune Disease (STAT3 gain-of-function syndrome): Research Report

**Target:** MONDO:0014414 · OMIM #615952 (ADMIO1) · ORPHA:438159 · MedGen C4014795 · **Causal gene: *STAT3*** (signal transducer and activator of transcription 3; HGNC symbol STAT3, lowercase `hgnc:11364` in this repository, to be confirmed against `cache/hgnc/terms.csv`)

> **About this report.** The repository already holds a skeleton entry, `kb/disorders/STAT3-Related_Early-Onset_Multisystem_Autoimmune_Disease.yaml`. It is 16 lines long and cites no references. A queue stub, `stubs/STAT3-related_Early-onset_Multisystem_Autoimmune_Disease.yaml`, also still exists.
>
> - **Quotes.** The PubMed tooling would not return full verbatim abstracts. Short quoted fragments below come from abstracts as shown in search results. Fetch each one with `just fetch-reference` before using it as a `snippet:`.
> - **Ontology CURIEs** (HP, GO, CL, NCIT) are *leads written from memory*, marked †. Under the repository's term contract, each must be looked up with OAK or the term caches before it is bound.
> - **PMIDs** marked ‡ were not confirmed against PubMed in this session. All other PMIDs were.

---

## 1. Disease Information

**Overview.** This disease is caused by **heterozygous germline gain-of-function (GOF) variants in *STAT3***. It belongs to the inborn errors of immunity in the immune-dysregulation group. Typical features are:
- early-onset lymphoproliferation (lymphadenopathy, hepatosplenomegaly);
- autoimmune cytopenias;
- autoimmunity in solid organs: early-onset type 1 diabetes, enteropathy, autoimmune thyroid disease, hepatitis, interstitial lung disease, arthritis;
- short stature;
- a variable susceptibility to infection.

It is the mirror image of *STAT3* loss-of-function / dominant-negative disease (autosomal dominant hyper-IgE syndrome, Job syndrome). Those are different MONDO and OMIM entities and must not be conflated with this one (Flanagan 2014, PMID:25038750; Milner 2015, PMID:25359994).

- The founding paper (Flanagan et al., *Nat Genet* 2014) reported five people with **de novo germline activating *STAT3* mutations** and early-onset autoimmunity including type 1 diabetes. It contrasted them with "inactivating STAT3 mutations" that cause hyper-IgE syndrome. The abstract opens: "Monogenic causes of autoimmunity provide key insights into the complex regulation of the immune system." (PMID:25038750)
- Milner et al. (*Blood* 2015) described 13 individuals from 10 families carrying 9 heterozygous germline *STAT3* mutations. All had lymphoproliferation and early-onset autoimmunity in solid organs, and haematologic autoimmunity was a dominant feature. (PMID:25359994)

**Identifiers:**

| System | ID |
|---|---|
| MONDO | MONDO:0014414 "STAT3-related early-onset multisystem autoimmune disease" |
| OMIM | #615952 Autoimmune disease, multisystem, infantile-onset, 1 (ADMIO1) |
| Orphanet | ORPHA:438159 |
| MedGen/UMLS | C4014795 |
| ICD-10 | No specific code; usually coded D89.8/D89.9 (other or unspecified immune-mechanism disorders) or D84.8 |
| ICD-11 | No specific code (falls under inborn errors of immunity, 4A0x/4B0x groupings) |
| IUIS classification | Table 4, "Diseases of immune dysregulation": autoimmunity with or without lymphoproliferation (*STAT3* GOF) |

**Synonyms:** STAT3 gain-of-function disease or syndrome; STAT3 GOF; infantile-onset multisystem autoimmune disease 1; ADMIO1; early-onset multi-organ autoimmune disease due to STAT3 GOF.

**Source of the data:** almost entirely aggregated case reports and series, plus one large international registry-style cohort (Leiding 2023, n=191). There is no EHR-derived population data.

---

## 2. Etiology

- **Primary cause:** heterozygous germline *STAT3* missense or in-frame variants that raise STAT3 transcriptional activity, either constitutively or after cytokine stimulation. Many are **de novo**. Others are inherited in an autosomal dominant pattern with **incomplete penetrance** (PMID:25038750; PMID:25359994; PMID:36228738).
- **Genetic risk and modifiers:**
  - **Penetrance depends on the variant.** Jägle et al. (*Clin Immunol* 2020, PMID:31770611) profiled 17 GOF variants and grouped them into three response patterns. The cluster with altered phosphorylation kinetics and strong basal activity was linked to the highest penetrance of lymphoproliferation and autoimmunity.
  - **MHC haplotype modifies diabetes risk** in the K392R knock-in mouse: diabetes was MHC-dependent and absent on a protective MHC background (Warshauer 2021, PMID:34115115). That is a mouse result; in humans, HLA modification is inferred.
- **Environmental risk factors:** none established. Infections can trigger HLH-like flares and cytopenia exacerbations, but this is anecdotal.
- **Protective factors:** none established in humans. In mice, a protective MHC haplotype and the absence of lymphocytes (Rag-deficient background) prevent diabetes (PMID:34115115; MODEL_ORGANISM evidence).
- **Gene–environment interaction:** not studied.

---

## 3. Phenotypes

The frequencies below come from the largest cohort (Leiding 2023, n=191, PMID:36228738) and the systematic review (2019, PMID:30825606). Onset is in early childhood: median **2.3 years** at onset, versus a median of **12 years** at diagnosis (PMID:36228738); the systematic review gives a mean onset of about 3 years (PMID:30825606).

| Phenotype | Type | Frequency / notes | HPO lead† |
|---|---|---|---|
| Lymphoproliferation (lymphadenopathy, splenomegaly, hepatomegaly) | sign | **73%**, the most common feature ("lymphoproliferation was the most common manifestation (73%)", PMID:36228738) | HP:0002716 Lymphadenopathy; HP:0001744 Splenomegaly; HP:0002240 Hepatomegaly |
| Autoimmune cytopenias (AIHA, ITP, autoimmune neutropenia; Evans syndrome) | lab/sign | **67%**, the second most common feature (PMID:36228738) | HP:0001890 Autoimmune hemolytic anemia; HP:0001973 Autoimmune thrombocytopenia; HP:0001875 Neutropenia |
| Infections (bacterial, viral, fungal, mycobacterial) | sign | **72%** (PMID:36228738); disseminated mycobacterial disease reported (PMID:25349174) | HP:0002719 Recurrent infections |
| Enteropathy / chronic diarrhoea, coeliac-like disease | symptom | Among the three most common features (PMID:30825606) | HP:0002028 Chronic diarrhea; HP:0002608 Celiac disease |
| Short stature / growth failure | sign | Common; partial GH insensitivity (PMID:25359994; PMID:29378236) | HP:0004322 Short stature |
| Early-onset (often neonatal) insulin-dependent diabetes | sign/lab | Frequent in the original series; T1D was the index phenotype (PMID:25038750) | HP:0100651 Type I diabetes mellitus |
| Autoimmune thyroid disease (mostly hypothyroidism) | sign/lab | Common (PMID:30825606) | HP:0000821 Hypothyroidism |
| Interstitial lung disease (LIP, organising pneumonia, fibrotic/cystic ILD) | sign | Common and a leading cause of death; can be fatal in infancy (PMC9169891; Gothe 2021 *Pediatr Pulmonol*) | HP:0006530 Interstitial pulmonary abnormality |
| Autoimmune hepatitis / hepatopathy | sign/lab | Reported in multiple series (PMID:25359994) | HP:0200123 Chronic hepatitis (to check) |
| Eczema / dermatitis | sign | Nonspecific dermatitis (Orphanet) | HP:0000964 Eczema |
| Arthritis | sign | Occasional | HP:0001369 Arthritis |
| Hypogammaglobulinaemia with low switched memory B cells | lab | Present in all three of Haapaniemi's patients (PMID:25349174) | HP:0004313 Decreased circulating antibody level |
| Low Treg, NK, Th17 and plasmacytoid DC counts; eosinopenia; raised double-negative T cells | lab | PMID:25349174; PMID:25359994 | HP:0002846 Abnormal B cell count (lead); HP:0031392 Increased double-negative T cells (to check) |
| HLH | sign | Rare (Forbes 2018‡ PMID:29477724) | HP:0001873 Thrombocytopenia (component); HLH term to look up |
| Large granular lymphocytic (T-LGL) leukaemia, lymphoma | sign | Rare; T-LGL at age 14 in a K392R carrier (PMID:25349174); malignancy rare (Vogel 2023 review) | — |
| Neurological disease, vasculopathy | sign | Rare (Vogel 2023, doi:10.3389/fped.2022.770077) | — |

**Severity and course.** Severity is variable but often severe. Manifestations accumulate over time: the disease is progressive and multisystem, and patients usually need intensive immunosuppression (PMID:30825606; Vogel 2023).

**Quality of life.** No disease-specific QoL instrument data were found. Morbidity comes from chronic cytopenias, insulin dependence, oxygen dependence in ILD, growth failure and the burden of immunosuppression.

---

## 4. Genetic/Molecular Information

- **Gene:** *STAT3* at 17q21.2; OMIM gene *102582. The protein has an N-terminal domain, coiled-coil, DNA-binding domain (DBD), linker, SH2 domain (Y705 phosphorylation site) and transactivation domain.
- **Variant spectrum:** heterozygous missense variants plus a few in-frame deletions, spread across all domains. The 2023 cohort had 72 unique variants (PMID:36228738); the 2019 review counted 28 (PMID:30825606). Examples:

  | Variant | Domain | Source |
  |---|---|---|
  | p.K392R | DBD; T-LGL case | PMID:25349174; mouse model in PMID:34115115 |
  | p.M394T | DBD | PMID:25349174 |
  | p.K658N | SH2 | PMID:25349174 |
  | p.T716M | TAD; recurrent, functionally shown to increase transcriptional activity | PMID:25038750; PMID:25359994 |
  | p.P715L | TAD | Hormone Res Paediatr 2017, doi:10.1159/000456544 |
  | p.E616del, p.C426R | — | PMID:29378236 |
  | p.P330R | Fatal infant ILD | PMC9169891 |

- **Classification:** most published variants are Pathogenic or Likely pathogenic in ClinVar (for example, the ClinVar records for T716M). Because GOF and LOF variants can sit at the same residue, **a functional assay is needed**: a STAT3-responsive luciferase reporter, or pSTAT3 kinetics (Chandrasekaran 2016 *JACI*, "Distinct mutations at the same positions of STAT3 cause either loss or gain of function").
- **Allele frequency:** pathogenic GOF variants are absent from gnomAD or ultra-rare. *STAT3* is highly constrained against missense variation.
- **Origin:** germline, often de novo. **Somatic** *STAT3* SH2-domain GOF mutations (for example Y640F and D661Y) are a different context: they drive T-LGL leukaemia and are linked to autoimmune cytopenias. That shows the same pathway at work (Masle-Farquhar 2022, *Immunity* 55:2386, doi:10.1016/j.immuni.2022.11.001).
- **Functional consequence:** GAIN_OF_FUNCTION or hypermorphic. Some variants act through increased basal activity, others through prolonged or delayed dephosphorylation, and others through stronger DNA binding (PMID:31770611).
- **Modifier genes:** MHC/HLA (mouse evidence). No human modifier has been established.
- **Epigenetics and chromosomal abnormalities:** none reported or not applicable.

---

## 5. Environmental Information

There are no established environmental, lifestyle or infectious *causes*. Infections are complications, made worse by hypogammaglobulinaemia and immunosuppression; mycobacterial, viral (EBV/CMV) and fungal infections are all reported (PMID:25349174; PMID:36228738). There is no ECTO exposure to bind.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Germline heterozygous *STAT3* GOF variant** → STAT3 shows increased or prolonged tyrosine-705 phosphorylation, dimerisation, DNA binding and/or transactivation after IL-6, IL-21, IL-23, IL-10 or IL-27 stimulation (PMID:31770611; PMID:25038750). *Demonstrated in vitro.*
2. → **Raised STAT3 target transcription, including the negative regulator SOCS3** → which **leads to reduced STAT5 and STAT1 phosphorylation** in response to IL-2 and interferons. The abstract states the mutations cause "secondary defects in STAT5 and STAT1 phosphorylation" (PMID:25359994). *Demonstrated in patient cells. That SOCS3 is the link is an inference.*
3. The chain then branches:
   - **3a. Treg branch.** Weaker IL-2/STAT5 signalling plus STAT3-driven RORγt programming → **fewer and less functional FOXP3⁺ regulatory T cells, and Th17 skewing** → loss of peripheral tolerance (PMID:25359994; PMID:25349174; in vitro Th17↑/Treg↓ in PMID:34115115).
   - **3b. CD8⁺ effector branch.** STAT3 GOF that is intrinsic to CD8⁺ T cells → **resistance to terminal exhaustion**, and clonal expansion of highly cytotoxic NKG2D^hi effector CD8⁺ T cells. Their accumulation depends on NKG2D and IL-2RB/IL-15 → tissue-destructive autoimmunity; in mice this is islet β-cell killing causing T1D (PMID:34115115; Masle-Farquhar 2022). *Shown in mice and supported by patient immunophenotyping.*
   - **3c. B-cell branch.** Dysregulated IL-21/STAT3 signalling → **arrest of terminal B-cell maturation, low switched memory B cells, hypogammaglobulinaemia**, while autoantibodies are still produced (PMID:25349174).
   - **3d. Lymphoproliferation.** Lymphocytes survive and proliferate more (STAT3 targets such as BCL2 family and MYC; double-negative T-cell expansion) → **lymphadenopathy and hepatosplenomegaly**, which in a few patients progress to **T-LGL leukaemia** (PMID:25349174).
   - **3e. Growth branch.** STAT3 hyperactivity **reduces GH-induced STAT5b transcriptional activity** → **partial GH insensitivity and low IGF-1** → **short stature** (PMID:29378236). This may persist after HSCT, which suggests a non-haematopoietic, cell-intrinsic component (Consonni 2024, *J Clin Immunol*). *Partly inferred.*
4. → **Effector-organ outcomes:**
   - autoantibody- and T-cell-mediated cytopenias (AIHA, ITP, neutropenia);
   - β-cell destruction (T1D);
   - thyroiditis;
   - autoimmune enteropathy;
   - lymphocytic/fibrotic **ILD**;
   - hepatitis.
5. → Immunosuppressive treatment plus the intrinsic B-cell and NK defects → **infections**, which together with ILD and HSCT complications are the main causes of death (overall survival 88%; PMID:36228738).

### Checklist detail

- **Pathways:** JAK–STAT (IL-6/gp130, IL-21, IL-23, IL-10 receptors); cross-inhibition of IL-2/STAT5 and IFN/STAT1; GH–STAT5b–IGF-1. KEGG hsa04630; Reactome "Interleukin-6 signaling" and "Growth hormone receptor signaling".
- **GO leads†:**
  - GO:0007259 cell surface receptor signaling pathway via JAK-STAT; check the current GO label, which was recently renamed (modifier INCREASED);
  - GO:0070106 interleukin-27-mediated signaling pathway (optional);
  - GO:0072540 T-helper 17 cell lineage commitment (INCREASED);
  - GO:0045066 regulatory T cell differentiation (DECREASED);
  - GO:0002377 immunoglobulin production (DECREASED);
  - GO:0060397 growth hormone receptor signaling pathway via JAK-STAT (DECREASED).
- **Cell types (CL leads†):**
  - CL:0000815 regulatory T cell;
  - CL:0000899 T-helper 17 cell;
  - CL:0000625 CD8-positive, alpha-beta T cell;
  - CL:0000236 B cell;
  - CL:0000787 memory B cell;
  - CL:0000169 type B pancreatic cell (target of damage);
  - CL:0000623 natural killer cell;
  - CL:0000784 plasmacytoid dendritic cell.
- **Protein dysfunction:** GAIN_OF_FUNCTION transcription factor (GO:0001228 DNA-binding transcription activator activity, RNA polymerase II-specific†).
- **Metabolic:** secondary insulin-deficient diabetes; low IGF-1.
- **Omics:** single-cell RNA-seq of patient and mouse CD8⁺ T cells shows a cytotoxic NKG2D^hi effector signature (granzymes, perforin, IFN-γ, CCL5) (Masle-Farquhar 2022). No public GEO dataset was confirmed in this session; `just discover-datasets` is the route to check.

---

## 7. Anatomical Structures Affected

- **Haematolymphoid:** lymph nodes, spleen, bone marrow (UBERON:0000029 lymph node; UBERON:0002106 spleen; UBERON:0002371 bone marrow†).
- **Endocrine:** pancreatic islets (UBERON:0000006 islet of Langerhans†); thyroid (UBERON:0002046†); growth axis.
- **Gastrointestinal:** small and large intestine (enteropathy); liver (UBERON:0002107†).
- **Respiratory:** lung interstitium (UBERON:0002048 lung†).
- **Skin; joints.**
- **Subcellular:** cytoplasm-to-nucleus shuttling of phosphorylated STAT3 (GO:0005634 nucleus, GO:0005737 cytoplasm†).
- **Laterality:** systemic or bilateral; not applicable.

---

## 8. Temporal Development

- **Onset:** infancy or early childhood (median 2.3 years). Neonatal diabetes and enteropathy can appear in the first months. Occasionally onset is in adolescence: Haapaniemi's third patient developed late-onset autoimmunity and mycobacterial disease in late adolescence (PMID:25349174).
- **Course:** chronic, lifelong and progressive. New organ involvement accumulates. There is no spontaneous remission.
- **Diagnostic delay:** long, about 10 years from median onset to median diagnosis (PMID:36228738). This is the clearest intervention window: early genetic diagnosis lets targeted therapy start before irreversible β-cell loss and lung fibrosis.

---

## 9. Inheritance and Population

- **Inheritance:** autosomal dominant (HP:0000006†). Many cases are de novo; familial cases show **incomplete penetrance and variable expressivity**, which depend on the variant (PMID:31770611).
- **Prevalence:** unknown. The disease is ultra-rare, with about 191 genotyped patients reported worldwide by 2022 from 33 countries (PMID:36228738). A suitable record would be `measure_type: CASES_IN_LITERATURE`.
- **Founder effects, consanguinity, carrier frequency:** not applicable or none reported.
- **Sex ratio:** roughly equal (no sex bias reported).
- **Anticipation and germline mosaicism:** not reported, though parental mosaicism should be considered for apparent de novo cases.

---

## 10. Diagnostics

- **Genetic testing:** an IEI/primary immune dysregulation NGS panel, or exome/genome sequencing. *STAT3* is on all major IEI panels. **A functional assay is needed for a novel variant**: a STAT3 luciferase reporter, or basal and stimulated pSTAT3 by phospho-flow or western blot. This is because GOF and LOF variants co-locate (PMID:31770611).
- **Immunophenotyping:**
  - low Treg (CD4⁺CD25⁺FOXP3⁺);
  - low NK cells;
  - raised TCRαβ⁺ double-negative T cells;
  - low switched memory B cells;
  - hypogammaglobulinaemia;
  - expanded effector CD8⁺ / NKG2D^hi cells;
  - eosinopenia (PMID:25349174; PMID:25359994).
- **Laboratory tests:**
  - Coombs test, platelet and neutrophil antibodies;
  - islet autoantibodies (GAD65, IA-2, ZnT8), HbA1c and C-peptide;
  - TSH, free T4, anti-TPO;
  - liver enzymes;
  - IGF-1 and IGFBP3 (low);
  - for HLH: ferritin and soluble IL-2R (sIL-2R).
- **LOINC leads (to be seeded with `just loinc-seed-cache`):** immunoglobulin G serum level; IGF-1 serum level; HbA1c. None of these is disease-specific, so only the measurement identity should be bound.
- **Imaging and pathology:**
  - chest HRCT for ILD (ground-glass, nodular or cystic change; lymphocytic interstitial pneumonia);
  - lymph-node biopsy, which shows reactive follicular hyperplasia and excludes lymphoma;
  - gut biopsy, which shows villous atrophy or autoimmune enteropathy.
- **Differential diagnosis:**
  - ALPS (FAS pathway; distinguished by raised DNTs plus biomarkers);
  - IPEX (*FOXP3*);
  - CTLA4 haploinsufficiency;
  - LRBA deficiency;
  - CD25 deficiency;
  - STAT5B deficiency;
  - **STAT1 GOF** (chronic mucocutaneous candidiasis predominates);
  - APS-1 (*AIRE*);
  - *PIK3CD* GOF (APDS);
  - *STAT3* LOF hyper-IgE syndrome (high IgE, eczema, pneumatoceles; the opposite molecular mechanism).
- **Screening:** no newborn screening. Cascade testing of relatives is recommended because penetrance is incomplete.

---

## 11. Outcome / Prognosis

- **Overall survival:** 88% in the 191-patient cohort (PMID:36228738).
- **Main causes of death:** infection, ILD and complications of HSCT.
- **After HSCT:** survival 62% (23 transplanted patients, PMID:36228738); 4 of 5 died in the 2019 review (PMID:30825606). In the ESID/EBMT JAKi cohort, 11 patients were bridged to HSCT, and overall survival there was 91% (PMID:37935260).
- **Morbidity:** lifelong insulin dependence, oxygen-dependent ILD, chronic cytopenias, growth failure, and the toxicity of long-term immunosuppression.
- **Prognostic factors:** the variant's molecular cluster correlates with penetrance (PMID:31770611). ILD and early-onset severe disease are adverse features. There are no validated biomarkers.

---

## 12. Treatment

| Treatment | Rationale / evidence | NCIT lead† | Modality |
|---|---|---|---|
| **JAK inhibitors** (ruxolitinib, tofacitinib, baricitinib) | Block signalling upstream of STAT3. Forbes 2018: 17 STAT1/STAT3-GOF patients, "most exhibited profound symptomatic improvement" (PMID:29477724‡). ESID/EBMT (Fischer 2024): 21 STAT3-GOF patients, **90% improved** (partial or complete remission); ruxolitinib used in 80% of all patients; adverse events in 38%, mostly mild (PMID:37935260). Leiding 2023: "clinical symptoms dramatically improved in patients treated with JAK inhibitors" (PMID:36228738) | Pharmacotherapy NCIT:C15986; agent: ruxolitinib (CHEBI or NCIT), tofacitinib | SMALL_MOLECULE |
| **IL-6 receptor blockade** (tocilizumab), often combined with a JAKi | IL-6 is a major STAT3 activator. The first patient to improve on cytokine blockade (PMID:25359994). Anti-IL-6R and JAKi called "promising" (PMID:30825606) | NCIT:C15986 + tocilizumab | MONOCLONAL_ANTIBODY |
| Conventional immunosuppression (corticosteroids, sirolimus, MMF, rituximab for cytopenias, abatacept) | Often only partly effective (PMID:36228738) | NCIT:C15986; corticosteroid CHEBI:50858 | SMALL_MOLECULE / MONOCLONAL_ANTIBODY |
| Immunoglobulin replacement | For hypogammaglobulinaemia | Human Immunoglobulin G NCIT:C80829 (as agent) | PROTEIN_REPLACEMENT |
| Insulin; thyroid hormone replacement | Endocrine organ failure | NCIT:C15986 | PROTEIN_REPLACEMENT / SMALL_MOLECULE |
| Recombinant GH | Partial GH insensitivity, so response may be limited (PMID:29378236) | NCIT:C15986 | PROTEIN_REPLACEMENT |
| **Allogeneic HSCT** | The only potentially curative option; survival 62% (PMID:36228738). May not correct the growth defect (Consonni 2024) | Hematopoietic cell transplantation NCIT:C15431 | CELL_THERAPY |
| Anti-infective prophylaxis | Supportive | Supportive Care NCIT:C15747 | — |

- **Experimental approaches:** direct STAT3 inhibitors (Stattic-class compounds; antisense such as danvatirsen in oncology) have been proposed but not tested in this disease (PMC9169891). Search ClinicalTrials.gov for JAKi trials in IEI.
- **Pharmacogenomics:** none specific. JAKi dosing in children is not standardised (PMID:37935260).
- **Strategy:** early molecular diagnosis, then a targeted JAKi with or without anti-IL-6R. HSCT is reserved for refractory disease or malignancy, ideally done after disease control on a JAKi used as a bridge.

---

## 13. Prevention

- **Primary prevention:** none. Options are genetic counselling (50% recurrence risk for a heterozygous parent, adjusted for incomplete penetrance) and prenatal or preimplantation testing in known familial variants.
- **Secondary prevention:** cascade testing of relatives. Clinically, early JAKi treatment before irreversible organ damage is proposed, though not proven.
- **Tertiary prevention:**
  - antimicrobial prophylaxis and IVIG;
  - vaccination with inactivated vaccines (live vaccines are contraindicated on immunosuppression);
  - surveillance for ILD, diabetes, thyroid disease and LGL leukaemia.

---

## 14. Other Species / Natural Disease

- No naturally occurring germline *STAT3*-GOF disease is recorded in OMIA (not confirmed in this session).
- *STAT3* is highly conserved (mouse *Stat3*, NCBI Gene 20848; NCBITaxon:10090).
- In dogs, somatic *STAT3* mutations are described in canine LGL leukaemia, which is an oncological analogue rather than a germline model.

---

## 15. Model Organisms

| Model | Recapitulation | Limitations | Ref |
|---|---|---|---|
| **Stat3^K392R/+ knock-in mouse (NOD background)** | Accelerated autoimmune diabetes in both sexes. CD8⁺-intrinsic GOF is sufficient (IGRP TCR transgenic); CD8⁺ cells resist exhaustion; disease depends on MHC and lymphocytes | Done on the diabetes-prone NOD background; less of the multisystem picture | Warshauer 2021, PMID:34115115 (MODEL_ORGANISM) |
| **Stat3 GOF knock-in mice (T716M, K658N), leukocyte-restricted** | Lymphoproliferation, accumulation of NKG2D^hi effector CD8⁺ T cells, lethal pathology. CD8⁺ T cells are required; NKG2D and IL-2RB are needed for accumulation | Species-specific differences in LGL biology | Masle-Farquhar 2022, *Immunity* 55:2386 |
| Patient-derived cells / reporter assays (HEK293 STAT3-luciferase) | Variant classification and response clusters | In vitro only; no tissue context | PMID:31770611; PMID:29378236 (IN_VITRO) |

Resources: MGI (*Stat3* alleles), JAX/MMRRC.

---

## Key references

| PMID | Citation | Evidence type |
|---|---|---|
| 25038750 | Flanagan SE et al. Activating germline mutations in STAT3 cause early-onset multi-organ autoimmune disease. *Nat Genet* 2014;46:812 | Human clinical + in vitro |
| 25359994 | Milner JD et al. Early-onset lymphoproliferation and autoimmunity caused by germline STAT3 gain-of-function mutations. *Blood* 2015;125:591 | Human clinical |
| 25349174 | Haapaniemi EM et al. Autoimmunity, hypogammaglobulinemia, lymphoproliferation, and mycobacterial disease in patients with activating mutations in STAT3. *Blood* 2015;125:639 | Human clinical |
| 30825606 | Clinical aspects of STAT3 gain-of-function germline mutations: a systematic review. *J Allergy Clin Immunol Pract* 2019;7:1958 | Review / human |
| 31770611 | Jägle S et al. Distinct molecular response patterns of activating STAT3 mutations associate with penetrance of lymphoproliferation and autoimmunity. *Clin Immunol* 2020;210:108316 | In vitro + human |
| 29378236 | Gutiérrez M et al. Partial growth hormone insensitivity and dysregulatory immune disease associated with de novo germline activating STAT3 mutations. *Mol Cell Endocrinol* 2018;473:166 | In vitro + human |
| 34115115 | Warshauer JT et al. A human mutation in STAT3 promotes type 1 diabetes through a defect in CD8+ T cell tolerance. *J Exp Med* 2021;218:e20210759 | Model organism |
| 36228738 | Leiding JW et al. Monogenic early-onset lymphoproliferation and autoimmunity: natural history of STAT3 gain-of-function syndrome. *JACI* 2023;151:1081 (PMC10081938) | Human clinical |
| 37935260 | Fischer M et al. JAK inhibitor treatment for inborn errors of JAK/STAT signaling: an ESID/EBMT-IEWP retrospective study. *JACI* 2024;153:275 | Human clinical |
| 29477724‡ | Forbes LR et al. Jakinibs for the treatment of immune dysregulation in patients with gain-of-function STAT1 or STAT3 mutations. *JACI* 2018 | Human clinical |
| — (PMID not retrieved) | Masle-Farquhar E et al. STAT3 gain-of-function mutations connect leukemia with autoimmune disease by pathological NKG2Dhi CD8+ T cell dysregulation and accumulation. *Immunity* 2022;55:2386, doi:10.1016/j.immuni.2022.11.001 | Model organism + human |
| — | Vogel TP, Leiding JW, Cooper MA, Forbes Satter LR. STAT3 gain-of-function syndrome. *Front Pediatr* 2023, doi:10.3389/fped.2022.770077 | Review |
| — | A novel STAT3 gain-of-function mutation in fatal infancy-onset ILD. *Front Immunol* 2022, doi:10.3389/fimmu.2022.866638 (PMC9169891) | Human case |

**Sources:**
- [PubMed 25038750](https://pubmed.ncbi.nlm.nih.gov/25038750/) · [PubMed 25359994](https://pubmed.ncbi.nlm.nih.gov/25359994/) · [PMC4304109 (Haapaniemi)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4304109)
- [PubMed 36228738 / PMC10081938](https://pmc.ncbi.nlm.nih.gov/articles/PMC10081938) · [PubMed 30825606](https://pubmed.ncbi.nlm.nih.gov/30825606/) · [PubMed 31770611](https://pubmed.ncbi.nlm.nih.gov/31770611/)
- [PMC6143347 (Gutiérrez)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6143347) · [PubMed 34115115](https://pubmed.ncbi.nlm.nih.gov/34115115/) · [PubMed 37935260](https://pubmed.ncbi.nlm.nih.gov/37935260/)
- [Masle-Farquhar 2022 (JHU record)](https://pure.johnshopkins.edu/en/publications/stat3-gain-of-function-mutations-connect-leukemia-with-autoimmune/) · [Vogel 2023 Front Pediatr](https://www.frontiersin.org/articles/10.3389/fped.2022.770077/full) · [PMC9169891](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9169891/)
- [Gothe 2021 ILD (LMU)](https://epub.ub.uni-muenchen.de/98516) · [MedGen C4014795](https://ncbi.nlm.nih.gov/medgen/C4014795) · [OMIM 615952 mirror](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/615952) · [PMC6322659 (Forbes 2018)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6322659)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 19 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 4 |
| Quoted claims found in source | 3 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 19 |
| On topic | 17 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMID:29477724`: "most exhibited profound symptomatic improvement"
  - Text part not found as substring: 'most exhibited profound symptomatic improvement'

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 53 |
| Resolved | 52 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `NCIT:C15986` (5 mentions) - the report calls it "Endocrine organ failure"; NCIT calls it **Pharmacotherapy**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.