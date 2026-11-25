---
provider: claude_code
model: claude-haiku-5-5, claude-opus-4-8, claude-opus-5-5
cached: false
start_time: '2026-11-24T04:43:50.327084'
end_time: '2026-11-24T04:49:41.223024'
duration_seconds: 350.9
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Ross River Fever
  mondo_id: MONDO:0000344
  category: Infectious
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: Ross River virus disease or disorder; Ross River virus infectious disease;
    Ross River virus caused disease or disorder; Ross River virus disease
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
  - claude-opus-4-8
  - claude-opus-5-5
  web_search_requests: 13
  num_turns: 26
  total_cost_usd: 1.3827738800000002
  session_id: b3cac40b-a9b7-4eba-81f0-4ac20aeb20b1
  stop_reason: end_turn
  permission_denials: 5
  denied_tools:
  - Bash
  tool_calls: 30
  retrieval_calls: 24
  assistant_text_blocks: 6
citation_count: 21
reference_validation:
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 8
  quotes_valid: 7
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:33802851
  relevance_assessed: 13
  on_topic: 13
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 42
  verified: 40
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 15
  labels_matching: 12
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: HP:0100504
    reported_labels:
    - Tenosynovitis
    ontology_label: Decreased circulating vitamin B2 concentration
  - term_id: UBERON:0002544
    reported_labels:
    - joint
    ontology_label: digit
  labels_variant: 1
  unresolvable_prefixes:
  - Taxon
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Ross River Fever
- **MONDO ID:** MONDO:0000344 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** Ross River virus disease or disorder; Ross River virus infectious disease; Ross River virus caused disease or disorder; Ross River virus disease
- **Category:** Infectious

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Ross River Fever** covering all of the
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

Bash network access is blocked, so I'll do the research through web search.

I'll gather the remaining specifics — PMIDs for key reviews, pathogenesis, identifiers, and clinical details.

I have strong coverage. Let me confirm identifiers and a few pathogenesis details, then write the report.

Let me fetch two key sources to lock down PMIDs and mechanistic detail.

I have what I need for the review. Let me get PMIDs for the key mechanism/trial papers via search.

I have enough verified, retrieved material to write the report. Writing it now.

---

# Comprehensive Research Report: Ross River Fever (Ross River Virus Disease)

**MONDO:0000344 · Category: Infectious**

**Interpretation note:** This report covers the human arboviral illness caused by Ross River virus (RRV), a mosquito-borne *Alphavirus*. The template's "Causal gene(s): not recorded" is correct and expected — **this is an infectious (viral) disease, not a monogenic disorder**. There is no human causal gene. Where the template asks for causal genes, pathogenic variants, inheritance, penetrance, etc., the answer is **not applicable**; I instead report the relevant viral genetics and the host genes implicated in susceptibility/pathogenesis (most prominently the entry-mediator gene *MXRA8*). I flag throughout which evidence is human-clinical vs. mouse-model vs. in vitro, because a central caveat in the field is that much mechanistic knowledge "is mainly inferred from a murine model that only partially resembles clinical signs and pathology in human and horses" (Yuen & Bielefeldt-Ohmann 2021, PMID 33802851).

---

## 1. Disease Information

**Overview.** Ross River fever is an acute, often self-limiting but frequently prolonged arthritogenic illness caused by Ross River virus, an RNA virus of the genus *Alphavirus* (family *Togaviridae*). The disease is characterized by polyarthralgia/polyarthritis, fever, fatigue, myalgia and a maculopapular rash, and is the most common and widespread mosquito-borne disease in Australia. It is endemic and enzootic in Australia, Papua New Guinea and the Solomon Islands (Yuen & Bielefeldt-Ohmann 2021, PMID 33802851; Harley, Sleigh & Ritchie 2001, *Clin Microbiol Rev* 14(4):909–932, DOI 10.1128/CMR.14.4.909-932.2001, [PMC89008](https://pmc.ncbi.nlm.nih.gov/articles/PMC89008)). The virus was first isolated in 1959 from *Aedes vigilax* mosquitoes trapped beside the Ross River in Townsville, North Queensland ([PMC89008](https://pmc.ncbi.nlm.nih.gov/articles/PMC89008); [CDC](https://www.cdc.gov/ross-river-virus/hcp/clinical-diagnosis-treatment/index.html)).

**Key identifiers (retrieved):**
- **MONDO:** MONDO:0000344 (per template)
- **MeSH:** The virus has descriptor **D012398** ("Ross River virus"); scope note: "A species of ALPHAVIRUS associated with epidemic EXANTHEMA and polyarthritis in Australia" ([MeSH record](https://meshb.nlm.nih.gov/record/ui?ui=D012398))
- **ICD-11:** **1D4D** "Ross River disease" (synonyms: Ross River fever; RR fever; epidemic polyarthritis) ([CISMeF/ICD-11](https://www.cismef.org/page/detail/en/ICD11_CA_1085418398))
- **ICD-10:** **A92.8** ("Other specified mosquito-borne viral fevers") — this is the conventional code but was **not confirmed** in a retrieved authoritative crosswalk; verify in the WHO ICD-10 browser.
- **OMIM / Orphanet:** None found/not applicable (infectious disease; no OMIM entry retrieved; no Orphanet record appeared).

**Synonyms / alternative names (retrieved):** Ross River virus disease; Ross River virus infection; Ross River disease; **epidemic polyarthritis** (historical term). ⚠️ Mapping caveat: "epidemic polyarthritis" historically denotes disease caused by **either RRV or Barmah Forest virus (BFV)**, so term-based lookups may conflate the two ([PMC89008](https://pmc.ncbi.nlm.nih.gov/articles/PMC89008)).

**Information source type.** The knowledge base is derived from **aggregated disease-level resources** — national notifiable-disease surveillance (Australian NNDSS), published cohort/outbreak studies, cross-disciplinary reviews, mouse-model experimental studies, and in vitro work — rather than from individual EHR records.

---

## 2. Etiology

**Primary cause (infectious).** The disease is caused by infection with **Ross River virus**, transmitted to humans through the bite of infected mosquitoes. RRV is maintained in nature in a **mosquito–vertebrate–mosquito enzootic cycle**, with native macropods (kangaroos, wallabies) regarded as the primary reservoir hosts (Yuen & Bielefeldt-Ohmann 2021, PMID 33802851; [PMC89008](https://pmc.ncbi.nlm.nih.gov/articles/PMC89008)). Humans are generally considered dead-end/spillover hosts, though human-to-mosquito-to-human transmission may contribute in urban outbreaks (notably the 1979–80 Pacific Islands epidemic).

**Risk factors (environmental/behavioral):**
- **Residence/exposure in endemic areas**, particularly coastal saltmarsh and inland riverine/irrigation regions of Australia.
- **High rainfall and flooding / high tides**, which expand mosquito breeding habitat. Reviews report "a 0 to 3 month lag period between increased rainfall and RRV infections" (Yuen & Bielefeldt-Ohmann 2021, PMID 33802851).
- **Season:** peak transmission in the Australian summer–autumn (notifications peak around March).
- **Age and sex:** disease incidence is highest in **adults aged ~30–64 years**, and regional studies report **higher rates in females** ([South Australia incidence study, CDI](https://www1.health.gov.au/internet/main/Publishing.nsf/Content/cda-cdi2903i.htm)). Symptomatic/chronic disease is uncommon in young children.
- **Outdoor occupational/recreational exposure** to mosquitoes.
- **Blood transfusion** is a rare transmission route ([CDC](https://www.cdc.gov/ross-river-virus/hcp/clinical-diagnosis-treatment/index.html)).

**Genetic (host) risk factors.** No validated human Mendelian susceptibility gene is established. ⚠️ I did not retrieve robust human GWAS/HLA association data within this session; HLA associations have been proposed historically for alphaviral arthritides but I could not confirm a specific allele from retrieved sources, so this is reported as **not established/unretrieved**. The strongest mechanistic host-gene link is the entry mediator **MXRA8** (see §4, §6), demonstrated in mouse models rather than as a human susceptibility allele.

**Protective factors.** **Prior natural infection confers immunity** (RRV is antigenically stable; lifelong immunity after infection is generally assumed). No dietary or pharmacologic protective factor is established. Vector-avoidance behaviors (repellent, protective clothing, avoiding dusk/dawn exposure) reduce risk.

**Gene–environment interactions.** Not characterized in humans. In mouse models, host genetic background and immune-pathway genes (complement, *MXRA8*) modulate the severity of disease produced by the environmental agent (the virus) — effectively an experimental gene–"environment" (infection) interaction (Morrison et al. 2007, PMID 17314163; MXRA8 study, [PMC10128017](https://pmc.ncbi.nlm.nih.gov/articles/PMC10128017)).

---

## 3. Phenotypes

Frequencies below are from the cross-disciplinary review (Yuen & Bielefeldt-Ohmann 2021, PMID 33802851) and Australian clinical guidance; they describe **symptomatic** patients (only ~25–45% of infected people are symptomatic).

| Phenotype | Type | Frequency (symptomatic patients) | Suggested HPO |
|---|---|---|---|
| **Arthralgia / polyarthralgia** (knee, ankle, wrist, small joints of hands/feet; often symmetrical) | Symptom/sign | ~70–90% | HP:0002829 (Arthralgia); HP:0005059 (Polyarthritis) |
| **Arthritis** (joint swelling/effusion) | Clinical sign | Common | HP:0001369 (Arthritis) |
| **Fatigue / lethargy** | Symptom | ~70–90% | HP:0012378 (Fatigue) |
| **Joint stiffness** | Symptom | ~70–90% | HP:0001387 (Joint stiffness) |
| **Myalgia** | Symptom | ~50–70% | HP:0003326 (Myalgia) |
| **Maculopapular rash** (trunk/limbs) | Physical manifestation | ~50% (absent in ~⅓) | HP:0000988 (Skin rash); HP:0000509 broad |
| **Fever** | Sign | ~50% | HP:0001945 (Fever) |
| **Flu-like/constitutional illness, headache** | Symptom | ~50% | HP:0002315 (Headache) |
| **Lymphadenopathy** (incl. cervical) | Sign | Variable | HP:0002716 (Lymphadenopathy) |
| **Tenosynovitis / enthesitis** (esp. Achilles tendon) | Sign | Variable | HP:0100504 (Tenosynovitis) |
| **Paraesthesia / tender palms and soles** | Symptom | Variable | HP:0003401 (Paresthesia) |

Direct quotes (PMID 33802851): "around 70–90% of patients experienced arthralgia (most commonly knee, ankle and wrist joints), lethargy or tiredness, and joint stiffness"; "50–70% had myalgia"; "~50% had skin rash, fever, and flu-like illness."

**Phenotype characteristics:**
- **Age of onset:** acute, occurring days after mosquito bite; clinical disease predominantly in **adults** (rare/mild in children).
- **Severity:** mild to moderate in most; **severe/debilitating arthralgia** in a subset; no fatal course documented.
- **Progression:** typically **episodic/fluctuating then slowly resolving**; arthralgia can be migratory. Acute illness lasts "from a few weeks to a few months."
- **Rare sequelae:** "uncommon sequelae, such as encephalitis, have been reported" (PMID 33802851); glomerulonephritis and hematologic abnormalities are occasionally described.

**Quality-of-life impact.** The arthralgia/fatigue complex substantially impairs work capacity and daily functioning during the prolonged phase; the pentosan trial used **hand-grip strength, RAPID3, and SF-36** as QoL/functional endpoints, indicating meaningful functional impairment in RRV arthralgia (Krishnan et al. 2021, PMID 33711991). Formal population EQ-5D/SF-36 norms specific to RRV were not retrieved beyond this trial.

---

## 4. Genetic / Molecular Information

**Not applicable as a human heritable disorder.** There are **no human causal genes, pathogenic germline variants, inheritance pattern, penetrance, modifier genes, chromosomal abnormalities, or disease-specific epigenetic changes** — RRV fever is an acquired viral infection.

**Viral genetics (the etiologic agent):** RRV has a positive-sense single-stranded RNA genome (~11.8 kb) encoding four non-structural proteins (nsP1–nsP4) and the structural polyprotein (capsid C; envelope glycoproteins **E3, E2, 6K, E1**) ([PMC89008](https://pmc.ncbi.nlm.nih.gov/articles/PMC89008); MeSH D012398). E2 mediates receptor binding and E1 mediates membrane fusion (alphavirus biology). ⚠️ One detailed query on RRV molecular virology was blocked by a safety classifier in this session, so some structural-biology specifics are reported at the level the reviews support rather than from a dedicated primary structural paper.

**Host entry gene — *MXRA8* (HGNC: MXRA8).** A genome-wide CRISPR screen identified **Mxra8** as an entry mediator for multiple arthritogenic alphaviruses including RRV, chikungunya (CHIKV), Mayaro and o'nyong-nyong; Mxra8 knockout reduced RRV infection in cells (Zhang et al. 2018, *Nature* 557:570–574, [s41586-018-0121-3](https://www.nature.com/articles/s41586-018-0121-3.pdf); [PMC5970976](https://pmc.ncbi.nlm.nih.gov/articles/PMC5970976)). In vivo, RRV-infected **MXRA8-knockout mice showed reduced viral replication and less weight loss**, with titers falling below detection by day 5, indicating MXRA8 contributes to RRV pathogenesis, not only cell entry (2023, [PMC10128017](https://pmc.ncbi.nlm.nih.gov/articles/PMC10128017)). Note most direct binding mechanism was demonstrated for CHIKV.

**Allele frequency / somatic-vs-germline / ACMG classification:** Not applicable (no pathogenic human variants to classify).

---

## 5. Environmental Information

- **Infectious agent:** **Ross River virus**, genus *Alphavirus*, family *Togaviridae* (NCBI Taxonomy: *Ross River virus*; CHEBI not applicable). The sole necessary cause.
- **Vectors (>40 competent mosquito species):** Key vectors are the freshwater **_Culex annulirostris_** (inland, widespread across mainland Australia), and the saltmarsh **_Aedes vigilax_** (northern/coastal) and **_Aedes camptorhynchus_** (southern/coastal); **_Aedes notoscriptus_** in metropolitan areas (PMID 33802851; [PMC89008](https://pmc.ncbi.nlm.nih.gov/articles/PMC89008)).
- **Reservoir/amplifying hosts:** Macropods (kangaroos, wallabies) are the believed primary reservoirs; brushtail possums, horses, flying foxes and humans may act as hosts in some settings; dogs and cats remained aviraemic (PMID 33802851).
- **Environmental drivers:** Rainfall, flooding, tidal inundation of saltmarsh, temperature, and irrigation — all modulating mosquito abundance. Seroprevalence in blood donors ranged **22% (Townsville) to 4% (Sydney)**, reflecting latitudinal/climatic gradient (PMID 33802851).
- **Lifestyle factors:** Outdoor exposure in endemic regions; no smoking/diet/alcohol association established.

---

## 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating infection → clinical manifestation).** Evidence type noted per step; several steps are **inferred primarily from mouse models and in vitro work**.

1. An infected mosquito inoculates **RRV into skin/subcutaneous tissue** during blood feeding. → *leads to* local infection of permissive cells. (Established.)
2. RRV virions **engage the entry mediator MXRA8** (and other attachment factors) on target cells → *results in* receptor-mediated internalization and cytoplasmic RNA replication. (Mouse/cell evidence: Zhang 2018; [PMC10128017](https://pmc.ncbi.nlm.nih.gov/articles/PMC10128017).)
3. Viral replication and viremia → *leads to* dissemination to **musculoskeletal tissues (skeletal muscle, joints/synovium, bone)**, the tropism underlying arthritis/myositis. (Mouse model; viremia detectable days 2–9 p.i. in mice — PMID 33802851.)
4. Infection of/trafficking to **monocytes and macrophages** → *results in* recruitment of inflammatory **monocyte/macrophage infiltrates** into muscle and joint tissue; these cells dominate the infiltrate. (Mouse; macrophage depletion by silica before infection "resulted in diminished acute disease" — PMID 33802851.) ⚠️ Branch/caveat: human monocytes "could not be infected with RRV, except in the presence of subneutralising levels of antibody," raising the possibility of **antibody-dependent enhancement** as a contributor.
5. Infected/activated cells **upregulate proinflammatory mediators** — e.g., MCP-1/CCL2 and IL-8 upregulated in human synovial fibroblasts in vitro (IL-8 up 8.2-fold in human fibroblasts) → *leads to* amplification of leukocyte recruitment and local inflammation. (In vitro + mouse; PMID 33802851.)
6. **Complement activation** — specifically the **mannose-binding lectin (MBL) pathway**, triggered by viral envelope N-glycans on infected cells → *leads to* C3 activation and deposition in inflamed muscle. (Mouse; glycan→MBL→complement: [PubMed 29324290](https://pubmed.ncbi.nlm.nih.gov/29324290/).)
7. Complement (via **C3**) acts in the **effector phase** → *results in* **inflammatory destruction of skeletal muscle and joint tissue**. C3-deficient mice develop "much less severe disease" and "far less severe destruction of skeletal muscle tissue" **despite similar inflammatory infiltrates**, placing complement downstream of cell recruitment in the causal chain (Morrison et al. 2007, PMID 17314163). Human corroboration: "complement activation was also detected in synovial fluid from RRV-infected patients" (PMID 17314163).
8. Tissue inflammation/damage → *produces* the **clinical polyarthritis, myalgia, and rash**. (Human-clinical outcome.)
9. **Resolution/repair branch:** during recovery a CD11b^hi Ly6C^lo **CX3CR1+ macrophage** population appears in muscle and supports tissue repair (mouse, mBio), while **persistently infected macrophages** are proposed to drive chronic/relapsing symptoms — but persistent productive infection was shown "only ... in a murine macrophage cell line (RAW 264.7)," so chronicity mechanism is **inferred, not demonstrated in humans** (PMID 33802851).

**Upstream vs downstream:** Viral entry (MXRA8) and replication are **upstream**; monocyte/macrophage recruitment and cytokine/chemokine induction are **intermediate**; **complement (MBL→C3) effector activity and tissue destruction are downstream**. Immune complexes are "probably not involved" (normal neutrophils and C3/C4 in that context) (PMID 33802851).

**Molecular pathways / processes & ontology suggestions:**
- Complement cascade — Reactome R-HSA-166658 (Complement cascade); lectin pathway. GO:0006956 (complement activation); GO:0001867 (complement activation, lectin pathway).
- Inflammatory response — GO:0006954; chemokine signaling (CCL2/MCP-1) GO:0070098.
- Type I interferon response (RIG-I/MAVS in monocytes — summary-level) GO:0060337; viral entry/receptor binding GO:0046718 (viral entry into host cell).
- **Cell types (CL):** monocyte CL:0000576; macrophage CL:0000235; inflammatory monocyte CL:0002057; synovial fibroblast CL:0000210; skeletal muscle myocyte/cell CL:0000187/CL:0008002.

**Molecular profiling / omics / single-cell / CRISPR:** A genome-wide **CRISPR screen** identified MXRA8 (functional genomics; Zhang 2018). Single-cell/flow characterization of muscle macrophage populations in mouse recovery is reported (mBio). Human multi-omic transcriptomic/proteomic disease signatures specific to RRV were not retrieved in depth; the pentosan trial reported **circulating biomarkers** (COMP, CTX-II, CCL1, CXCL12, CXCL16, CCL17) modulated by therapy (Krishnan 2021, PMID 33711991).

---

## 7. Anatomical Structures Affected

**Organ/system level:**
- **Musculoskeletal system (primary):** peripheral **joints** — knee, ankle, wrist, small joints of hands/feet (metacarpophalangeal, interphalangeal); **skeletal muscle** (myositis in models); tendons/entheses (Achilles tenosynovitis). UBERON: UBERON:0002544 (joint)? → UBERON:0001474 skeletal element; UBERON:0002385 (muscle tissue); UBERON:0000211 (ligament)/tendon UBERON:0000043.
- **Integumentary system:** skin — maculopapular rash (UBERON:0002097 skin of body).
- **Lymphatic:** lymph nodes — lymphadenopathy (UBERON:0000029 lymph node).
- **Secondary/rare involvement:** CNS (encephalitis, rare), kidney (glomerulonephritis, rare).

**Tissue/cell level:** synovium (synovial membrane, UBERON:0002018) and synovial fibroblasts (CL:0000210); skeletal muscle myofibers (CL:0000187) with infiltrating monocytes/macrophages (CL:0000576/CL:0000235).

**Subcellular level:** RRV replicates in the **cytoplasm** on modified membranes (GO:0005737 cytoplasm; GO:0016020 membrane); envelope glycoproteins transit the **ER/Golgi** secretory pathway (GO:0005783 endoplasmic reticulum; GO:0005794 Golgi).

**Localization/laterality:** Arthritis is characteristically **polyarticular and often symmetrical/bilateral**, affecting peripheral joints ([CDC](https://www.cdc.gov/ross-river-virus/healthcareproviders/)); may be migratory.

---

## 8. Temporal Development

- **Onset:** **Acute**, following an incubation period of **3–21 days (usually 7–9 days)** (PMID 33802851; WA/Vic guidance).
- **Acute phase:** fever, rash, fatigue, and the abrupt onset of polyarthralgia/arthritis, lasting weeks.
- **Course:** Often **episodic/relapsing-remitting** during convalescence; arthralgia may wax and wane and migrate.
- **Duration / chronicity:** Acute illness resolves over "a few weeks to a few months." A substantial minority have **prolonged disease**: Australian guidance reports ~15–66% with ongoing arthralgia at 3 months, with resolution in the majority by **5–7 months**, and about **one-quarter** with rheumatic symptoms persisting ≥12 months ([WA GP guide](https://www.health.wa.gov.au/~/media/Files/Corporate/Reports%20and%20publications/PDF/RRVdiseasemanagementguideforGPs2010.pdf)). The review states "more than 50% of patients continue to experience symptoms 12 months after initial presentation" (PMID 33802851) — figures vary by cohort/definition.
- **Remission:** Generally **spontaneous** over months; no documented progression to destructive chronic arthritis in most patients. Reinfection is unusual (immunity).
- **Critical window:** No defined therapeutic window established; symptomatic management throughout.

---

## 9. Inheritance and Population

**Inheritance / genetics:** **Not applicable** — infectious, not heritable. No inheritance pattern, penetrance, expressivity, anticipation, mosaicism, founder effect, consanguinity role, or carrier frequency.

**Epidemiology:**
- RRV is the **most common arboviral disease in Australia**, with **~5,000 cases notified annually** on average; annual notifications ranged from **5,653 (2010–11) to 10,074 (2014–15)**, totaling 28,768 over 2010–15 (PMID 33802851). National notification **rate ~18.6–26.4 per 100,000/year** in reported years (e.g., 22.6 per 100,000 in 2014; 18.6 in 2013) ([Australian CDI NNDSS reports](https://www1.health.gov.au/internet/main/publishing.nsf/Content/cda-cdi3101a14.htm)).
- **Geographic distribution:** Endemic/enzootic in **all Australian states, Papua New Guinea and the Solomon Islands** (PMID 33802851); a major epidemic occurred in the Pacific (Fiji, Samoa, Cook Islands) in 1979–80. Rates highest in the **Northern Territory** (e.g., 124.4 per 100,000 in 2013) and northern/coastal Queensland and Western Australia ([CDI](https://www1.health.gov.au/internet/main/Publishing.nsf/Content/cda-cdi3101a14.htm)).
- **Age/sex:** Predominantly adults **30–64 years**; regional data show **slight female predominance**; rare in young children ([SA incidence study](https://www1.health.gov.au/internet/main/Publishing.nsf/Content/cda-cdi2903i.htm)).

---

## 10. Diagnostics

**Clinical/laboratory tests:**
- **Serology (mainstay):** RRV-specific **IgM and IgG**. Definitive recent infection requires **IgG seroconversion or ≥4-fold rise in paired sera ~10–14 days apart**, or detection of RRV-specific IgM in the presence of RRV IgG ([Victoria guidance](https://health.vic.gov.au/infectious-diseases/ross-river-virus-disease)). ⚠️ **IgM alone is unreliable** — it can persist for months/years; "IgM serology cannot be relied upon to conclusively diagnose RRV disease" ([WA GP guide](https://www.health.wa.gov.au/~/media/Files/Corporate/Reports%20and%20publications/PDF/RRVdiseasemanagementguideforGPs2010.pdf)). A single IgM+ within 7 days of onset gives a **presumptive** diagnosis to be confirmed ([DVA guidance](https://clik.dva.gov.au/book/export/html/75522)).
- **Nucleic acid detection (RT-PCR):** useful early (brief viremia) — LOINC-codable RRV RNA assays.
- **Virus isolation:** possible but rarely used clinically.
- **Nonspecific labs:** often normal; mild lymphocytosis/raised ESR/CRP variably; synovial fluid is inflammatory but non-purulent (complement activation detectable — PMID 17314163).

**Genetic testing:** **Not applicable** (no WGS/WES/panel/karyotype/repeat-expansion/mtDNA role).

**Imaging/electrophysiology:** No specific findings; imaging used mainly to exclude alternatives.

**Clinical criteria / differential diagnosis:** Diagnosis integrates compatible clinical syndrome + epidemiologic exposure + serology. **Differentials:** Barmah Forest virus disease (very similar — key reason term "epidemic polyarthritis" is ambiguous), chikungunya and other alphaviral arthritides, dengue, parvovirus B19, rubella, rheumatoid arthritis, reactive/seronegative arthritis, and other viral arthritides ([CDC](https://www.cdc.gov/ross-river-virus/hcp/clinical-diagnosis-treatment/index.html); [PMC89008](https://pmc.ncbi.nlm.nih.gov/articles/PMC89008)).

**Screening:** No population or newborn screening (acquired infectious disease). Blood-donor relevance noted (rare transfusion transmission).

---

## 11. Outcome / Prognosis

- **Mortality:** Essentially **nil** — "To date, there is no death reported that is directly attributed to RRV infection" (PMID 33802851). No survival-rate metric applies.
- **Morbidity / disability:** The dominant burden is **prolonged arthralgia, fatigue and reduced function** lasting months in a substantial minority (see §8). Most recover fully.
- **Recovery:** High likelihood of complete recovery; majority resolve by 5–7 months, with ~25% experiencing symptoms ≥12 months.
- **Complications:** Rare encephalitis, glomerulonephritis; chronic fatigue-like syndromes have been debated.
- **Prognostic factors:** Older age and greater initial symptom severity are associated with more prolonged illness (clinical guidance); no validated molecular prognostic biomarker, though inflammatory/cartilage markers (COMP, CTX-II, chemokines) track disease activity in trial settings (PMID 33711991).
- **QoL measures used:** SF-36, RAPID3, grip strength (PMID 33711991).

---

## 12. Treatment

**No approved antiviral or disease-specific therapy exists.** Management is **supportive/symptomatic** (PMID 33802851; [CDC](https://www.cdc.gov/ross-river-virus/hcp/clinical-diagnosis-treatment/index.html)).

**Pharmacotherapy (symptomatic):**
- **NSAIDs** (e.g., ibuprofen, naproxen) and simple analgesics (paracetamol/acetaminophen) for arthralgia/arthritis — mainstay (NCIT: Nonsteroidal Anti-inflammatory Agent, NCIT:C198; Acetaminophen NCIT:C198? use NCIT C561 Ibuprofen, C62649 Acetaminophen).
- **DMARDs/corticosteroids:** not established; reviews note other treatments "such as disease-modifying antirheumatic drugs (DMARDs) ... have not been proven effective in RRV clinical trials" and can carry serious adverse effects (PMID 33711991).
- **Pharmacogenomics:** Not applicable.

**Experimental / investigational:**
- **Pentosan polysulfate sodium (PPS):** Phase 2a randomized, double-blind, placebo-controlled trial (PARA-004, **ACTRN12617000893303**; 20 subjects, 2 mg/kg SC twice weekly × 6 weeks). Reported **improved grip strength (+6.99 kg, p=0.0189 at Day 15)**, RAPID3 pain/total improvements (p=0.0197/0.0101), and near-remission of joint symptoms in **61.5% (PPS) vs 14.3% (placebo)**; main AE was injection-site reactions. Authors concluded the results "warrant further evaluation" — but the trial is small/exploratory (Krishnan et al. 2021, PMID 33711991). NCIT: Pentosan Polysulfate Sodium (NCIT:C47707).
- **PG545 (pixatimod)** and related heparan-sulfate mimetics: efficacy shown in **mouse** RRV/CHIKV disease (reduced infiltrates and proinflammatory factors) (PMID 33802851 summary).
- **Complement/MBL-pathway inhibition** is a mechanistically rational but not yet clinical target (Morrison 2007, PMID 17314163; glycan/MBL work, [PubMed 29324290](https://pubmed.ncbi.nlm.nih.gov/29324290/)).

**Advanced therapeutics (gene/cell/RNA/targeted/immunotherapy):** None approved or in routine use for RRV.

**Surgical/rehabilitative:** No surgery; **physiotherapy and graded exercise** support recovery of joint function (supportive care).

---

## 13. Prevention

- **Primary prevention = vector/bite avoidance** (the mainstay): insect repellent (DEET/picaridin), protective clothing, avoiding peak mosquito activity, screening/netting, and **mosquito control** — larval source reduction, management of saltmarsh/wetland breeding sites, and public health education ([NSW control guideline](https://www.health.nsw.gov.au/Infectious/controlguideline/Pages/ross_river.aspx); PMID 33802851). Prevention "relies entirely" on bite prevention and breeding-site management.
- **Vaccine (investigational, none licensed):** An **inactivated, Vero cell-derived, alum-adjuvanted RRV vaccine** completed a **Phase 3 trial** (2011–2012, 17 Australian sites, three 2.5 µg doses; 1,755 adults 16–59 y + 209 older adults), reported safe/well-tolerated and inducing "antibody titers associated with protection ... in the majority of individuals" ([Phase 3, 2015, PMC4340901](https://pmc.ncbi.nlm.nih.gov/articles/PMC4340901); Phase 1/2, [PubMed 22001875](https://www.pubmed.gov/22001875/)). As of the retrieved sources, **no RRV vaccine is licensed/available** (PMID 33802851). NCIT: not applicable (investigational).
- **Secondary/tertiary prevention:** Early symptomatic management; no screening program. Genetic counseling **not applicable**.
- **Public-health/environmental interventions:** Integrated mosquito management, surveillance (sentinel chicken flocks/mosquito trapping), and climate/rainfall-based early-warning given the 0–3 month rainfall lag (PMID 33802851).

---

## 14. Other Species / Natural Disease

- **Natural disease — horses (*Equus caballus*, NCBI Taxon:9796):** RRV causes naturally occurring, **non-fatal** arthritic/lethargic illness in horses; "most horses recovered several months after initial presentation"; equine signs include lethargy, muscle pain/stiffness, lameness, and submandibular lymphadenopathy; equine seroprevalence 21–91% (PMID 33802851). Horses are proposed as both a possible reservoir/amplifier and a natural disease model. ⚠️ Experimental infection was mild (1/11 horses showed clinical signs; to be "interpreted cautiously" owing to use of the old T48 prototype strain).
- **Reservoir hosts:** Macropods (kangaroos/wallabies) — subclinical amplifying hosts; possums, flying foxes possibly involved. Dogs/cats remain aviraemic.
- **Zoonotic/transmission:** The disease is **mosquito-borne arboviral zoonosis**; transmission to humans is via mosquitoes amplified on vertebrate hosts, not direct animal-to-human contact.
- **Comparative biology:** RRV belongs to the arthritogenic alphavirus group (with CHIKV, Mayaro, o'nyong-nyong, Sindbis/Barmah Forest) sharing **MXRA8-mediated entry** and complement/monocyte-driven arthritis — a conserved pathogenic theme across these viruses (Zhang 2018; Morrison 2007).
- **Breed (VBO):** No breed-specific predisposition identified.

---

## 15. Model Organisms

- **Mouse (*Mus musculus*, NCBI Taxon:10090) — principal model.** RRV infection of mice (notably using strain **T48**) reproduces **myositis and arthritis** with monocyte/macrophage-dominated infiltrates; viremia detectable days 2–9 p.i.; severe disease can include **hindlimb paralysis and death** — outcomes **not seen in humans/horses**, a key limitation (PMID 33802851). The model established the roles of **complement/C3** (C3⁻/⁻ mice: much milder disease, less muscle destruction despite similar infiltrates — Morrison et al. 2007, PMID 17314163), the **MBL lectin pathway** and **viral N-glycans** ([PubMed 29324290](https://pubmed.ncbi.nlm.nih.gov/29324290/)), and **MXRA8** (MXRA8-KO mice: reduced replication/disease — [PMC10128017](https://pmc.ncbi.nlm.nih.gov/articles/PMC10128017)).
- **Genetic models used:** gene-knockout mice — **C3⁻/⁻**, MBL-deficient, classical/alternative-pathway-component-deficient (retained severe disease), **MXRA8-knockout**, and chemokine-receptor (CCR2) studies.
- **In vitro models:** murine macrophage line **RAW 264.7** (persistent RRV infection), human synovial fibroblast lines (MCP-1/IL-8 induction), and CRISPR-screen cell lines (MXRA8 discovery).
- **Phenotype recapitulation:** Good for **acute arthritis/myositis and immunopathology**; **poor** for (a) chronicity/relapse mechanisms in humans, (b) the lethal/paralytic outcomes that are mouse-specific, and (c) direct human monocyte infection (which requires sub-neutralizing antibody in vitro). The field's explicit caveat: human/equine immunopathogenesis "is mainly inferred from a murine model that only partially resembles clinical signs and pathology" (PMID 33802851).
- **Resources:** MGI (mouse), ATCC (RAW 264.7, Cellosaurus CVCL_0493).

---

## Key References (retrieved this session)

1. **Yuen KY, Bielefeldt-Ohmann H.** Ross River Virus Infection: A Cross-Disciplinary Review with a Veterinary Perspective. *Pathogens.* 2021;10(3):357. **PMID: 33802851**; DOI 10.3390/pathogens10030357. [PMC8002670](https://pmc.ncbi.nlm.nih.gov/articles/PMC8002670)
2. **Harley D, Sleigh A, Ritchie S.** Ross River virus transmission, infection, and disease: a cross-disciplinary review. *Clin Microbiol Rev.* 2001;14(4):909–932. DOI 10.1128/CMR.14.4.909-932.2001. [PMC89008](https://pmc.ncbi.nlm.nih.gov/articles/PMC89008) (PMID not independently verified this session)
3. **Morrison TE, Fraser RJ, Smith PN, Mahalingam S, Heise MT.** Complement Contributes to Inflammatory Tissue Destruction in a Mouse Model of Ross River Virus-Induced Disease. *J Virol.* 2007;81(10):5132–5143. **PMID: 17314163**; [PMC1900244](https://pmc.ncbi.nlm.nih.gov/articles/PMC1900244)
4. RRV envelope glycans activate the host complement system. [PubMed 29324290](https://pubmed.ncbi.nlm.nih.gov/29324290/)
5. **Zhang R, et al.** Mxra8 is a receptor for multiple arthritogenic alphaviruses. *Nature.* 2018;557:570–574. [article](https://www.nature.com/articles/s41586-018-0121-3.pdf); [PMC5970976](https://pmc.ncbi.nlm.nih.gov/articles/PMC5970976)
6. Role of MXRA8 in Ross River Virus Disease Pathogenesis. 2023. [PMC10128017](https://pmc.ncbi.nlm.nih.gov/articles/PMC10128017)
7. **Krishnan et al.** Pentosan polysulfate sodium for Ross River virus-induced arthralgia: a phase 2a, randomized, double-blind, placebo-controlled study. *BMC Musculoskelet Disord.* 2021;22:271. **PMID: 33711991**; [PMC7955617](https://pmc.ncbi.nlm.nih.gov/articles/PMC7955617)
8. Inactivated RRV vaccine Phase 3. 2015. [PMC4340901](https://pmc.ncbi.nlm.nih.gov/articles/PMC4340901); Phase 1/2 [PubMed 22001875](https://www.pubmed.gov/22001875/)
9. Australian NNDSS notification data, *Communicable Diseases Intelligence*. [CDI reports](https://www1.health.gov.au/internet/main/publishing.nsf/Content/cda-cdi3101a14.htm)
10. CDC Ross River virus clinical pages. [CDC HCP](https://www.cdc.gov/ross-river-virus/hcp/clinical-diagnosis-treatment/index.html); MeSH [D012398](https://meshb.nlm.nih.gov/record/ui?ui=D012398); ICD-11 [1D4D](https://www.cismef.org/page/detail/en/ICD11_CA_1085418398)

---

### Caveats on completeness
- **Genetics sections (4, 9) are "not applicable" by design** — RRV fever is infectious, with no human causal gene; the template's "Causal gene(s): not recorded" is correct. The nearest host-gene story is *MXRA8* (mouse/cell evidence).
- One molecular-virology search was **blocked by a safety classifier**, so some structural-protein specifics are reported only at review level.
- Several PMC primary PDFs returned CAPTCHA/rate-limit blocks; where I could not retrieve a primary source I cited the retrieved review/abstract/registry and flagged unverified identifiers (e.g., Harley 2001 PMID; ICD-10 A92.8).
- Human GWAS/HLA susceptibility, detailed human omics signatures, and formal QoL population norms were **not retrieved** and are marked as not established/unretrieved rather than filled from memory.

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 8 |
| Quoted claims found in source | 7 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 13 |
| On topic | 13 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMID:33802851`: "uncommon sequelae, such as encephalitis, have been reported"
  - closest text in source: "However, it is worth noting that uncommon sequalae, such as encephalitis, have been reported [ 23 ]"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 42 |
| Resolved | 40 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 15 |
| Terms named correctly | 12 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0100504` (1 mention) - the report calls it "Tenosynovitis"; HP calls it **Decreased circulating vitamin B2 concentration**
- `UBERON:0002544` (1 mention) - the report calls it "joint"; UBERON calls it **digit**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0046718` (1 mention) - the report calls it "viral entry into host cell"; GO calls it **symbiont entry into host cell**, and lists "viral entry into host cell" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `Taxon`.