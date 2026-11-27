---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-11-20T20:17:14.867572'
end_time: '2026-11-20T20:42:48.527677'
duration_seconds: 1533.66
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Perineurioma
  mondo_id: MONDO:0019404
  category: '>-'
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: not recorded
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
  - claude-opus-5[1m]
  web_search_requests: 5
  num_turns: 125
  total_cost_usd: 6.9749815000000055
  session_id: d8e639fe-d313-4e93-b15b-5488444eb1c0
  stop_reason: end_turn
  tool_calls: 124
  retrieval_calls: 124
  assistant_text_blocks: 2
citation_count: 90
reference_validation:
  total_references: 81
  verified: 81
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 4
  quotes_valid: 3
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:29148537
  relevance_assessed: 81
  on_topic: 54
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 56
  verified: 53
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 34
  labels_matching: 25
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: DOID:4697
    reported_labels:
    - DOID
    ontology_label: perineurioma
  - term_id: NCIT:C207066
    reported_labels:
    - Malignant Perineurioma
    - high mitotic activity, hypercellularity, hyperchromasia, and pleomorphism
    - Malignant:** *"high mitotic activity, hypercellularity, hyperchromasia, and
      pleomorphism
    ontology_label: Malignant Perineurioma
  - term_id: UBERON:0000123
    reported_labels:
    - Endoneurium** (where INP proliferates)
    ontology_label: endoneurium
  labels_variant: 6
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Perineurioma
- **MONDO ID:** MONDO:0019404 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** not recorded
- **Category:** >-

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Perineurioma** covering all of the
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

I'll research this now, starting with the identifiers and core disease definitions.

# Comprehensive Disease Research Report: Perineurioma (MONDO:0019404)

## Interpretation note and scope

**MONDO:0019404 is the umbrella term "perineurioma"** — a benign neoplasm of perineurial cells, the specialised flattened cells that form the perineurium of peripheral nerves. The template records "causal gene(s): not recorded," and this is substantively correct rather than a gap: perineurioma is **not a Mendelian germline disorder**. It is a sporadic, clonal somatic neoplasm. The gene that functions as its principal driver — and the gene a knowledge-base entry should carry as the causal gene for the intraneural form — is **TRAF7** (TNF receptor associated factor 7; HGNC:20456; 16p13.3; NCBI Gene 84231; UniProt Q6Q0C0; OMIM 606692), mutated somatically in the C-terminal WD40 repeat domain in ~60% of intraneural perineuriomas ([Klein et al., *Ann Neurol* 2017;81(2):316–321, PMID 28019650](https://pmc.ncbi.nlm.nih.gov/articles/PMC5725965/); [HGNC REST](https://rest.genenames.org/fetch/symbol/TRAF7)). A genetically distinct second driver set — **NF2** (HGNC:7773; 22q12.2; NCBI Gene 4771; UniProt P35240; OMIM 607379) and **NF1** (17q) — accounts for the soft-tissue (extraneural) form and a minority of intraneural cases ([Carter et al., *Am J Surg Pathol* 2018;42(12):1708–1714, PMID 30303818](https://pubmed.ncbi.nlm.nih.gov/30303818/); [Lasota et al., *Am J Pathol* 2001;158(4):1223–1229, PMID 11290539](https://pubmed.ncbi.nlm.nih.gov/11290539/)).

Because MONDO:0019404 is the parent term, this report covers the whole entity family — intraneural, soft-tissue/extraneural (including sclerosing, reticular and pseudolipoblastic variants), gastrointestinal mucosal, hybrid, and malignant forms — and flags throughout which subtype each piece of evidence applies to. **All identifiers, statistics and quotations below were retrieved in this session**; sections where retrieval failed are marked explicitly.

---

## 1. Disease Information

### 1.1 Overview

Perineurioma is a rare benign peripheral nerve sheath tumour (PNST) composed exclusively or predominantly of neoplastic **perineurial cells**. It is defined by a characteristic immunophenotype (EMA⁺ / claudin-1⁺ / GLUT1⁺ / S-100⁻) and by perineurial ultrastructure. Macarenco et al. described perineuriomas as "benign peripheral nerve sheath neoplasms composed of perineurial cells with characteristic immunohistochemical and ultrastructural features," stressing that "correct identification of perineuriomas is important to avoid unnecessary overtreatment" ([*Arch Pathol Lab Med* 2007;131(4):625–636, PMID 17425397](https://pubmed.ncbi.nlm.nih.gov/17425397/)).

Two principal clinicopathological families are recognised, and current molecular data show they are **pathogenetically distinct**:

| Family | Location | Typical presentation | Driver genetics |
|---|---|---|---|
| **Intraneural perineurioma (INP)** | Within the endoneurium of a single nerve/fascicle | Painless, slowly progressive, **motor-predominant** focal mononeuropathy in youth | Somatic **TRAF7** WD40 missense (~60%); rarely 22q/**NF2** loss |
| **Soft-tissue (extraneural) perineurioma** | Dermis, subcutis, deep soft tissue, viscera; no recognisable parent nerve | Painless slow-growing mass | Large chromosomal deletions: 22q (**NF2**) or 17q (**NF1**), mutually exclusive; **no TRAF7** |

A "modern" synthesis of the intraneural form: "IN perineuriomas are rare, benign peripheral nerve sheath tumors, most frequently coming to clinical attention when patients present with painless, progressive weakness or sensory loss in adolescence or young adulthood. The gold standard of diagnosis has traditionally been with targeted tissue biopsy demonstrating 'pseudo-onion bulb' formation with positive epithelial membrane antigen (EMA) staining. However, modern magnetic resonance imaging is allowing some patients to forgo biopsy. Recent genetic studies of IN perineuriomas have demonstrated common TRAF7 point mutations and rare NF2 mutations" ([Acta Neurochir (Wien) 2023;165(11):3539–3547, PMID 37684428](https://pubmed.ncbi.nlm.nih.gov/37684428/)).

### 1.2 Key identifiers (retrieved from the EBI OLS4 MONDO API)

| Resource | Identifier |
|---|---|
| **MONDO** | MONDO:0019404 — label "Perineurioma" |
| **OMIM** | *Not listed* (no OMIM entry; consistent with a non-Mendelian somatic neoplasm) |
| **Orphanet** | ORPHA:85102 (MONDO-asserted xref; **not independently verified** — Orphanet pages were not retrievable this session) |
| **ICD-9** | 215.9 |
| **ICD-11** | Foundation ID 456459236 (**foundation ID, not a verified stem code**; ICD-11 browser could not be retrieved) |
| **ICD-O-3** | **9571/0** (benign behaviour code) |
| **NCIT** | C4973 — "A rare, usually benign tumor composed entirely of neoplastic perineurial cells." |
| **UMLS CUI** | C0751691 |
| **DOID** | DOID:4697 |
| **MedGen** | 199712 |
| **GARD** | 0012698 |
| **SNOMED CT** | 404036006 |
| **MeSH** | *No MeSH xref returned by MONDO* |

Source: [EBI OLS4 MONDO term record for MONDO_0019404](https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMONDO_0019404).

> **⚠ Curation issue worth recording in the knowledge base.** The MONDO definition text retrieved for MONDO:0019404 is *"A usually benign perineurioma not associated with a nerve, arising from the soft tissues."* That is the definition of the **soft-tissue/extraneural subtype** (identical in substance to NCIT:C6912, "Soft Tissue Perineurioma: A perineurioma not associated with a nerve, arising from the soft tissues"), yet the term's label is the generic "Perineurioma" and its xrefs (NCIT:C4973, ICD-O 9571/0, SNOMED 404036006) are the generic ones. MONDO also carries separate child entries for extraneural, intraneural and malignant perineurioma ([NORD MONDO disease pages](https://rarediseases.org/mondo-disease/intraneural-perineurioma/)). **The definition on MONDO:0019404 should be generalised**, or the entry will mis-annotate intraneural cases.

### 1.3 Subtype / variant terminology with NCIT identifiers

Retrieved from [OLS4 NCIT search](https://www.ebi.ac.uk/ols4/api/search?q=perineurioma&ontology=ncit&rows=10):

| NCIT ID | Term | NCIT definition (verbatim) |
|---|---|---|
| NCIT:C4973 | Perineurioma | "A rare, usually benign tumor composed entirely of neoplastic perineurial cells." |
| NCIT:C6911 | Intraneural Perineurioma | "A WHO grade I perineurioma that arises within the endoneurium. It is characterized by the formation of pseudo-onion bulbs." |
| NCIT:C6912 | Soft Tissue Perineurioma | "A perineurioma not associated with a nerve, arising from the soft tissues." |
| NCIT:C172621 | Skin Perineurioma | "A rare perineurioma arising from the skin." |
| NCIT:C188997 | Childhood Perineurioma | "A perineurioma that occurs during childhood." |
| NCIT:C207064 | Reticular Perineurioma | "...anastomosing cords of elongated spindle cells that form a reticular pattern." |
| NCIT:C207065 | Sclerosing Perineurioma | "...strands of small epithelioid to spindle cells in a collagenous stroma." |
| NCIT:C207066 | Malignant Perineurioma | "...high mitotic activity, hypercellularity, hyperchromasia, and pleomorphism." |
| NCIT:C207081 | Hybrid Perineurioma-Schwannoma | hybrid nerve sheath tumour |
| NCIT:C207082 | Hybrid Perineurioma-Neurofibroma | hybrid nerve sheath tumour |

### 1.4 Synonyms and alternative names (from retrieved literature)

- Intraneural perineurioma; **localized hypertrophic (mono)neuropathy** — the historical designation for INP, "initial description of intraneural (IN) perineurioma in 1964" (PMID 37684428)
- Extraneural perineurioma; soft-tissue perineurioma; **storiform perineurial fibroma** ([Zámecník & Gomolcák, *Cesk Patol* 1997;33(1):28–30, PMID 9221216](https://pubmed.ncbi.nlm.nih.gov/9221216/))
- Cutaneous fibrous perineurioma ([Smith & Skelton, *J Cutan Pathol* 1998;25(6):333–337, PMID 9694624](https://pubmed.ncbi.nlm.nih.gov/9694624/))
- **Benign fibroblastic polyp** / intramucosal perineurioma / "hybrid hyperplastic polyp–mucosal perineurioma" (colorectal form) ([Agaimy et al., *Am J Surg Pathol* 2010;34(11):1663–1671, PMID 20962618](https://pubmed.ncbi.nlm.nih.gov/20962618/))
- Perineurial cell tumour (PNT) (PMID 11290539)
- "Perineurial MPNST" / malignant perineurioma ([Hirose et al., *Am J Surg Pathol* 1998;22(11):1368–1378, PMID 9808129](https://pubmed.ncbi.nlm.nih.gov/9808129/); [Rosenberg et al., *J Cutan Pathol* 2002;29(6):362–367, PMID 12135468](https://pubmed.ncbi.nlm.nih.gov/12135468/))

### 1.5 Nature of the evidence base

**Disease-level aggregated, not EHR/individual-patient.** No population registry, SEER-type or EHR-derived cohort for perineurioma was retrievable. The entire evidence base consists of (a) single-institution surgical/pathology series (largest: 81 soft-tissue cases, PMID 15958848; 112 INP patients screened, PMID 32529330), (b) two systematic reviews pooling published cases (172 cases/72 studies, PMID 34284162; 77 cases/22 articles, PMID 32054523), and (c) case reports. This is an important caveat for every frequency figure quoted below: **all percentages are from referral-centre or literature-pooled series and are subject to ascertainment bias.**

---

## 2. Etiology

### 2.1 Disease causal factors

Perineurioma is a **clonal somatic neoplasm**. No environmental, infectious, dietary or occupational cause has been identified in any retrieved source. The established causal factors are acquired somatic genomic alterations in perineurial cells, which segregate by subtype:

**(a) Intraneural perineurioma — somatic TRAF7 WD40 missense mutation (principal driver).**
Klein et al. performed whole-exome sequencing on intraneural perineuriomas and found: *"10 of 16 (60%) tumor cases had mutations in the WD40 domain of TRAF7,"* the same domain harbouring causal meningioma mutations. Three recurrent hotspot substitutions were identified — **p.L519P** (3 cases), **p.H521R** (3 cases) and **p.S561R** (4 cases). Two further non-TRAF7 cases showed large chromosomal abnormalities: *"Both cases have large deletions on chromosome 22q."* The authors concluded the mutations *"are predicted to inactivate the interaction of TRAF7 with other proteins or destabilize the WD40 domain,"* revealing *"an unexpected shared pathogenesis with intracranial meningiomas"* (PMID 28019650).

**(b) Intraneural perineurioma — NF2 / chromosome 22q loss (minority pathway, mutually exclusive with TRAF7).**
White et al. reported INP in a 20-year-old man with NF2 showing *"loss of the long arm of chromosome 22 including NF2, SMARCB1, and LZTR1,"* and reviewed evidence for *"two mutually exclusive pathways involving NF2 and TRAF7 mutations"* in INP development ([*Clin Neuropathol* 2020;39(4):167–171, PMID 32271143](https://pubmed.ncbi.nlm.nih.gov/32271143/)). Pendleton et al. found 2 NF2-associated cases among 112 INP patients at a single institution plus one external case, noting genetic evidence for *"a potential link between the NF2 gene and the development of intraneural perineurioma,"* while cautioning that perineuriomas remain **unclassified** as part of the NF2 tumour spectrum ([*Acta Neurochir (Wien)* 2020;162(8):1891–1897, PMID 32529330](https://pubmed.ncbi.nlm.nih.gov/32529330/)).

**(c) Soft-tissue perineurioma — large deletions involving NF2 (22q) or NF1 (17q), mutually exclusive; TRAF7 wild-type.**
Carter et al. applied whole-exome sequencing and SNP array to 14 soft-tissue perineuriomas: *"thirteen cases showed 2 or more chromosomal abnormalities, composed primarily of large deletions,"* with *"chr22q deletions, containing the NF2 locus (n=6)"* and *"chr17q deletions, with the NF1 locus (n=4),"* which were mutually exclusive. Additional losses involved chr2, chr6 and chr10; one case showed **chr7 chromothripsis**. Critically, *"no TRAF7 mutations or alterations were identified in any case,"* and the authors concluded *"alterations in NF1 or NF2 likely contribute to perineurioma pathogenesis"* (PMID 30303818).

Earlier work anticipated this: Lasota et al. sequenced NF2 in 8 perineurial cell tumours (conventional, retiform and sclerosing) and found five point mutations in four cases (**50%**) — in the 5′-UTR and exons 3, 6 and 8, producing amino-acid changes at codons 83, 182 and 241 — with loss-of-heterozygosity at the NF2 locus, concluding *"the NF2 tumor suppressor gene is altered in PNTs by the two-hit mechanism"* (PMID 11290539). Giannini et al. had demonstrated chromosome 22 deletion by FISH with an M-bcr (22q11) probe in two soft-tissue perineuriomas, with 44% and 96% single-signal nuclei, proposing that soft-tissue and intraneural perineuriomas constitute *"a spectrum of perineurial neoplasia"* ([*Am J Surg Pathol* 1997;21(2):164–173, PMID 9042282](https://pubmed.ncbi.nlm.nih.gov/9042282/)).

**(d) Colorectal mucosal perineurioma / benign fibroblastic polyp — BRAF V600E confined to the epithelium.**
Agaimy et al. examined 29 fibroblastic polyps and found *"V600E BRAF mutation in 14 cases (63%) and KRAS mutation in 1 (4%),"* concluding these lesions *"represent a unique type of mixed epithelial-stromal polyps"* (hybrid hyperplastic polyp/mucosal perineurioma) with the perineurial component possibly derived from modified pericryptic fibroblasts (PMID 20962618). The critical localisation was established by Erlenbach-Wünsch et al.: *"BRAF V600E mutation was detected in 54% of the epithelial but in none of the stromal components"* ([*Ann Diagn Pathol* 2018;35:48–52, PMID 29747061](https://pubmed.ncbi.nlm.nih.gov/29747061/)), echoed by van Wyk et al.: *"BRAF mutations are limited to the serrated crypt epithelium"* ([*Diagn Pathol* 2018;13(1):16, PMID 29463272](https://pubmed.ncbi.nlm.nih.gov/29463272/)). **Implication: in the GI form the perineurial proliferation may be reactive/secondary to a BRAF-driven serrated epithelial lesion rather than itself the driven clone.**

**(e) Hybrid schwannoma–perineurioma — VGLL3 rearrangement (a genetically separate entity).**
Dickson et al. performed RNA sequencing on 18 hybrid schwannoma-perineuriomas and identified *"VGLL3 rearrangement in 14 of these cases,"* with partners CHD7 (10), CHD9 (2) and MAMLD1 (2); two had unrelated fusions (DST–BRAF, SQSTM1–CDX1). They concluded these tumours represent *"an altogether pathologically distinct entity"* unrelated to conventional schwannoma or perineurioma ([*Mod Pathol* 2021;34(6):1116–1124, PMID 33649458](https://pubmed.ncbi.nlm.nih.gov/33649458/)).

**(f) Emerging "perineurioma-like" entities (2026).** A novel perineurioma-like soft-tissue tumour with **SETD1A::FOSB** fusion was reported ([Wilsher et al., *Pathology* 2026;58(4):493–495, PMID 41927362](https://pubmed.ncbi.nlm.nih.gov/41927362/)), and eight "perineurioma-like EMA-positive calvarial neoplasms" with *"uniform, bland spindle cells"* were characterised as a possibly separate category ([Rizwan et al., *Histopathology* 2026;89(3):544–553, PMID 42216621](https://pubmed.ncbi.nlm.nih.gov/42216621/)). These should be tracked as distinct from MONDO:0019404 pending further data.

### 2.2 Risk factors

**Genetic risk factors**

| Factor | Evidence | Strength |
|---|---|---|
| **Germline NF2 pathogenic variant (neurofibromatosis type 2 / NF2-related schwannomatosis)** | 2/112 INP patients at Mayo had NF2 (PMID 32529330); one NF2 patient with INP and 22q loss including NF2/SMARCB1/LZTR1 (PMID 32271143) | Established association; **perineurioma is not yet an accepted NF2 diagnostic tumour** |
| **Germline NF1 pathogenic variant (neurofibromatosis type 1)** | 6.7 cm soft-tissue perineurioma of the lower leg in a 51-year-old man with proven NF-1 and a germline NF1 deletion (c.449_502delTGTT); authors concluded *"perineurioma may rarely be NF-1 related and should be included in the spectrum of neoplasms occurring in this disorder"* ([Schaefer et al., *Int J Clin Exp Pathol* 2013;6(12):3003–3008, PMID 24393170](https://pubmed.ncbi.nlm.nih.gov/24393170/)). In 2026, a pediatric superficial malignant perineurioma of the groin in a 12-year-old boy showed *"17q loss with focal homozygous NF1 deletion"* ([Raetsch et al., *J Cutan Pathol* 2026, PMID 42755235](https://pubmed.ncbi.nlm.nih.gov/42755235/)) | Rare but reported; mechanistically coherent with somatic 17q/NF1 deletions in sporadic cases |
| **Somatic TRAF7 WD40 hotspot variants** | Driver, not a susceptibility allele (PMID 28019650) | Established (somatic) |
| **Germline TRAF7 variants** | Germline TRAF7 missense causes **CAFDADD** (cardiac, facial and digital anomalies with developmental delay; MIM 618164): 45 patients with *"a recognizable facial gestalt (characterized in particular by blepharophimosis), short neck, pectus carinatum, digital deviations, and patent ductus arteriosus,"* most variants clustering in WD40 repeats ([Castilla-Vallmanya et al., *Genet Med* 2020;22(7):1215–1226, PMID 32376980](https://pubmed.ncbi.nlm.nih.gov/32376980/); [Paprocka et al., *Front Med* 2021;8:708717, PMID 34513876](https://pubmed.ncbi.nlm.nih.gov/34513876/)). **No perineurioma was reported in the retrieved CAFDADD literature** | Germline TRAF7 is a *different* disease, not a perineurioma risk factor on retrieved evidence |
| **Age ≤40 / youth (INP)** | Median age at diagnosis 18 years across 172 pooled cases (PMID 34284162); age ≤40 is one of the 8 Perineurioma Diagnostic Criteria (PMID 29192862) | Strong demographic association |
| **Sex (female, modest)** | 54.4% female of 172 pooled INP cases (PMID 34284162); 54.5% female of 77 (PMID 32054523); 59.46% female in 148 GI cases (PMID 40225020) | Weak-to-modest |
| **Family history** | No familial clustering of isolated perineurioma retrieved | No evidence |

**Environmental, lifestyle, occupational and infectious risk factors**
**None identified.** Across all retrieved primary literature and systematic reviews there is **no reported association with toxins, radiation, pollution, occupational exposure, smoking, alcohol, diet, exercise, trauma, or any bacterial, viral, fungal or parasitic agent**. A search of CTD/TOXNET-type content yielded no perineurioma entries. This should be recorded as an explicit negative, not as missing data.

One intriguing, unexplained clinical observation: Howe et al. documented *"a biopsy-proven intraneural perineurioma involving the left lumbosacral and brachial plexus with prominent hemi-body port wine stains in the associated dermatomes,"* noting the relationship *"remains unclear but may provide insights into understanding perineurioma pathogenesis"* ([*Skeletal Radiol* 2014;43(3):393–397, PMID 24092235](https://pubmed.ncbi.nlm.nih.gov/24092235/)) — suggestive of a possible shared somatic-mosaic developmental field effect, though this is a single observation.

Similarly, a 2026 report describes sclerosing perineurioma arising **within a nevus sebaceous** ([Zuniga Gamboa et al., *Dermatol Online J* 2026;32(5), PMID 43040817](https://pubmed.ncbi.nlm.nih.gov/43040817/)) — another possible mosaic-lesion co-occurrence.

### 2.3 Protective factors

**No genetic or environmental protective factors have been identified or studied.** No GWAS, gnomAD-based protective-allele analysis, nutritional study or Cochrane review of perineurioma was retrievable. Given the tumour's rarity and somatic aetiology, such studies are unlikely to exist.

### 2.4 Gene–environment interactions

**No gene–environment interaction has been reported or investigated.** No CTD, PheGenI or GxE database entries for perineurioma were retrievable. The disease model is purely somatic-genetic.

---

## 3. Phenotypes

Phenotype expression differs fundamentally by subtype: **INP produces a neurological deficit syndrome; soft-tissue perineurioma produces a painless mass.** Frequencies below are drawn from the specific cohorts named.

### 3.1 Intraneural perineurioma — neurological phenotype

| Phenotype | Type | Frequency | Onset / severity / course | Suggested HPO term |
|---|---|---|---|---|
| **Focal motor deficit in one nerve territory** | Clinical sign | **100%** (10/10, PERISCOPE, PMID 41657107); **100%** (30/30, PMID 34030186); **100%** (19/19, PMID 30637060); "motor predominant" (32 patients, PMID 19567701) | Adolescence/young adulthood; *"All patients presented with progressive motor deficits, and each exhibited at least one muscle group with severe weakness (MRC ≤ 2)"*; slowly progressive then static | **HP:0009831** Mononeuropathy |
| **Focal sensory loss / sensory symptoms** | Symptom + sign | **80%** (8/10, PERISCOPE); 10/19 = **52.6%** (PMID 30637060); *"mild sensory involvement"* in 27/32 (PMID 19567701) | Milder than motor; may be subclinical | HP:0009831; **HP:0003401** Paresthesia (**HP:0033660** if hand) |
| **Pain** | Symptom | **40%** (4/10, PERISCOPE) — notably, the classic description is *painless* progressive weakness (PMID 37684428) | Variable | (no verified perineurioma-specific HP term retrieved) |
| **Foot drop / dorsiflexor weakness** (common fibular, sciatic or lumbosacral plexus involvement) | Clinical sign | Implied by nerve distribution: sciatic 41.9%, common fibular prominent (PMID 34284162; PERISCOPE n=3 common fibular) | Progressive then static | **HP:0009027** Foot dorsiflexor weakness |
| **Focal muscle atrophy** | Physical manifestation | Implied by chronic denervation; PERISCOPE notes *"the complexity of restoring function after chronic denervation"* | Late, irreversible | **HP:0003202** Skeletal muscle atrophy |
| **Fusiform nerve enlargement** | Imaging/physical | **100%** (10/10 PERISCOPE); 16/19 "aspecific nerve enlargement," 5/19 "typical fusiform tumor" (PMID 30637060) | Present at diagnosis | **HP:0003382** Hypertrophic nerve changes |
| **Pseudo-onion bulb formation on biopsy** | Histopathology | **100%** of biopsied cases (10/10 PERISCOPE); diagnostic in 17/18 biopsied (PMID 30637060) | — | **HP:0003383** Onion bulb formation; **HP:0003400** Basal lamina onion bulb formation (closest available; note pseudo-onion bulbs are *perineurial*, not Schwann-cell, whorls — a true HPO term for "pseudo-onion bulb" does **not** exist and could be proposed) |
| **Axonal loss on nerve biopsy** | Laboratory/histology | Expected; PERISCOPE notes S-100 focal positivity in 30% *"consistent with residual Schwann cells"* | Progressive | **HP:0003447** Axonal loss |
| **Multifocal / multiple-nerve disease** | Clinical sign | **Rare** — unifocal disease is a diagnostic criterion (PMID 29192862); 15/56 (27%) had proximal lumbosacral or brachial plexus involvement but *"none extended proximal to the dorsal root ganglia"* (PMID 28173435) | — | **HP:0032018** Multiple mononeuropathy (for rare multifocal cases) |

**Onset, severity, progression and time-to-diagnosis.** Onset is in youth: PERISCOPE median symptom-onset age **21 years** (range 9–37), median age at first evaluation **26.5 years** (13–48). Pooled median age at diagnosis was **18 years** (PMID 34284162). Diagnostic delay is substantial — **median 34.5 months from symptom onset to first intervention (range 12–173 months)** (PERISCOPE, PMID 41657107); Pisapia et al. note INP *"frequently result[s] in diagnostic delay due to their uncommon presentation"* ([*Surg Neurol Int* 2025;16:129, PMID 40353166](https://pubmed.ncbi.nlm.nih.gov/40353166/)).

Course is **slowly progressive, then static**: Mauermann et al. found the condition *"static or slowly progressive"* with minimal disability change over median 36 months' follow-up (PMID 19567701). Wilson et al. followed 20 biopsy-proven patients with ≥2-year imaging intervals: lesions were *"on average larger on repeat imaging"* and *"longer on repeat imaging,"* yet *"no lesions grew to involve a new nerve or division of a nerve,"* and radiological expansion **did not correlate** with clinical deterioration ([*Neurosurgery* 2019;85(6):786–792, PMID 30481319](https://pubmed.ncbi.nlm.nih.gov/30481319/)).

### 3.2 Soft-tissue (extraneural) perineurioma — mass phenotype

| Phenotype | Frequency / detail | Source |
|---|---|---|
| **Painless soft tissue / subcutaneous mass** | Typical presentation; 81 cases, mean age 46 y, size **0.3–20 cm**, "painless masses across varied anatomic sites" | PMID 15958848 |
| **Acral mass (fingers/palms), sclerosing variant** | 19 cases, "painless mass," **0.7–3.3 cm**, median age **24.5 y**, male predominance, predilection for fingers and palms | PMID 9414186 |
| **Upper-extremity subcutaneous mass, reticular variant** | 6 cases, asymptomatic, **1.5–10 cm**, ages 34–61, 4 F / 2 M | PMID 11257623 |
| **Hybrid schwannoma/perineurioma** | 42 cases, *"a solitary painless nodule,"* mean age 38 y, 22 F / 20 M, limbs > head/neck > trunk > colon | PMID 19623031 |
| Suggested HPO | No HPO term for perineurioma exists. Nearest structural analogues: **HP:0100698** Subcutaneous neurofibroma; **HP:0100008** Schwannoma; **HP:0001067** Neurofibroma; **HP:0100697** Malignant peripheral nerve sheath tumor (for perineurial MPNST). **A new HPO term "Perineurioma" is warranted** | — |

### 3.3 Gastrointestinal perineurioma / benign fibroblastic polyp

From the systematic review of 148 cases (25 publications, 2004–2024; [Alenezi et al., *Case Rep Gastrointest Med* 2025;2025:1636142, PMID 40225020](https://pmc.ncbi.nlm.nih.gov/articles/PMC11991822/)):

- **Asymptomatic / screening-detected: 80.24%**; symptomatic: 19.75%
- Submucosal lesions far more often symptomatic (**66.67%** vs 18.92% for mucosal)
- Mean age **51 years** (SD ±14.87; range 24–87); **59.46% female**
- Mean size **4.18 mm** (range 2–50 mm); non-colonic polyps significantly larger (16.18 mm vs 4.09 mm colonic)
- Symptomatic presentations in individual reports: chronic abdominal pain and constipation with a *"5 cm, multilobulated polyp"* ([PMID 42677309](https://pubmed.ncbi.nlm.nih.gov/42677309/)); **adult ileal intussusception** ([PMID 42351541](https://pubmed.ncbi.nlm.nih.gov/42351541/)); recurrent **GI bleeding** from an *"ulcerated, space-occupying lesion"* in the ileum (hybrid schwannoma/perineurioma, 19-year-old male, [PMID 42112490](https://pubmed.ncbi.nlm.nih.gov/42112490/))

### 3.4 Unusual anatomical presentations (2023–2026 reports)

- **Orbit**: unilateral progressive painless **proptosis**, 45-year-old male, myxoid changes ([PMID 42578239](https://pubmed.ncbi.nlm.nih.gov/42578239/)); orbital soft-tissue perineurioma ([PMID 41412874](https://pubmed.ncbi.nlm.nih.gov/41412874/)); sclerosing perineurioma of the orbit in a **7-week-old infant** mimicking dacryocystocele — *"rare soft tissue tumor previously unreported in the orbit"* ([Siktberg et al., *Ophthalmic Plast Reconstr Surg* 2024;40(6):e217–e220, PMID 39028107](https://pubmed.ncbi.nlm.nih.gov/39028107/))
- **Oral cavity / tongue**: mandibular extraneural perineurioma, 68-year-old female — *"Perineuriomas are a rare form of peripheral nerve sheath tumors, with occurrences in the oral cavity being exceptionally uncommon"* ([PMID 41010284](https://pubmed.ncbi.nlm.nih.gov/41010284/)); sclerosing perineurioma of the tongue, an *"uncommon variant"* in an *"unusual and never described site"* ([PMID 34074156](https://pubmed.ncbi.nlm.nih.gov/34074156/))
- **Stomach**: only **twelve** gastric cases in the literature ([PMID 41954346](https://pubmed.ncbi.nlm.nih.gov/41954346/))
- **Face/skin**: medial superciliary arch, *"slowly enlarging papule"*, 36-year-old woman ([PMID 41798498](https://pubmed.ncbi.nlm.nih.gov/41798498/)); perioral benign cutaneous **plexiform hybrid tumour of perineurioma and cellular neurothekeoma**, 82-year-old woman ([PMID 41547237](https://pubmed.ncbi.nlm.nih.gov/41547237/))
- **Anterior chest wall**, toddler (sclerosing variant) ([PMID 41502903](https://pubmed.ncbi.nlm.nih.gov/41502903/))
- **Finger** sclerosing perineurioma in a patient with prior unilateral vestibular schwannoma, flagged as *"a diagnostic pitfall in the differential diagnosis of peripheral nerve sheath tumours"* ([PMID 43020599](https://pubmed.ncbi.nlm.nih.gov/43020599/))

### 3.5 Quality-of-life impact

**No study using a validated QoL instrument (EQ-5D, SF-36, PROMIS, or a disease-specific tool) was retrievable for perineurioma of any subtype.** This is a genuine evidence gap.

The best available functional proxies, all from INP cohorts:
- PERISCOPE: every patient had at least one muscle group at **MRC ≤2** (i.e., unable to move against gravity); **7/10 required tendon transfer** for functional restoration, and *"outcomes were heterogeneous,"* reflecting *"the complexity of restoring function after chronic denervation."* The authors conclude: *"despite an indolent imaging appearance, INP frequently causes severe functional impairment requiring reconstructive surgery"* (PMID 41657107).
- Mauermann et al., conversely, reported minimal change in disability scores over median 36 months in 32 patients (PMID 19567701).

These two findings are not contradictory but reflect different cohort ascertainment (a reconstructive-surgery-referral cohort vs a neurology natural-history cohort) and are worth recording as a **stated tension in the literature**: the deficit is often severe and fixed, but it does not typically worsen once established.

For soft-tissue and GI perineurioma, QoL impact is presumptively minimal (painless mass; 80% of GI cases asymptomatic), but this has not been measured.

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes

| Gene | HGNC | Locus | NCBI Gene | UniProt | OMIM | Role in perineurioma | Subtype |
|---|---|---|---|---|---|---|---|
| **TRAF7** | HGNC:20456 | 16p13.3 | 84231 | Q6Q0C0 | 606692 | Somatic WD40 hotspot missense; principal driver, ~60% | Intraneural |
| **NF2** | HGNC:7773 | 22q12.2 | 4771 | P35240 | 607379 | Biallelic inactivation (point mutation + LOH) or 22q deletion | Soft-tissue (n=6/14) and minority of intraneural |
| **NF1** | — (locus 17q) | 17q | — | — | — | Large 17q deletions containing NF1 (n=4/14), mutually exclusive with NF2 deletions | Soft-tissue; also malignant perineurioma (focal homozygous NF1 deletion) |
| **BRAF** | — | 7q34 | — | — | — | V600E — **in the serrated epithelium only, not the perineurial stroma** | Colorectal mucosal (benign fibroblastic polyp) |
| **VGLL3** | — | — | — | — | — | Rearrangement (CHD7/CHD9/MAMLD1 partners) | **Hybrid** schwannoma–perineurioma (distinct entity) |

HGNC/UniProt identifiers retrieved from [HGNC REST](https://rest.genenames.org/fetch/symbol/TRAF7), [HGNC REST NF2](https://rest.genenames.org/fetch/symbol/NF2) and [UniProt Q6Q0C0](https://rest.uniprot.org/uniprotkb/Q6Q0C0.txt). HGNC IDs for NF1, BRAF and VGLL3 were not retrieved this session and should be filled in from HGNC before annotation.

### 4.2 Pathogenic variants — TRAF7

**Recurrent somatic hotspots (intraneural perineurioma):**

| Protein change | Domain (UniProt Q6Q0C0) | Cases (Klein 2017, n=16) | cDNA as reported |
|---|---|---|---|
| **p.Leu519Pro (L519P)** | WD4 repeat (515–554) | 3 | c.1555T>C, exon 17 (as extracted from PMC) |
| **p.His521Arg (H521R)** | WD4 repeat (515–554) | 3 | c.1561A>G, exon 17 (Klein 2017); **c.1562A>G** (PERISCOPE 2026) |
| **p.Ser561Arg (S561R)** | WD5 repeat (557–594) | 4 | c.1682A>C, exon 18 |

> **⚠ Data-quality flag for curation.** The cDNA coordinates extracted for these variants are **internally inconsistent and could not be reconciled** against a stated reference transcript during this session: p.H521R is given as c.1561A>G by Klein et al. and c.1562A>G by the PERISCOPE cohort, and the reported positions for p.L519P and p.S561R do not align with the expected codon positions. **Record the protein-level changes (p.L519P, p.H521R, p.S561R) as the confident claims and verify every cDNA coordinate against the source PDFs and a declared RefSeq/Ensembl transcript before entering HGVS nomenclature into a knowledge base.**

**Variant classification (ACMG/AMP).** These are **somatic** oncogenic hotspot variants. No ClinVar germline classification for these specific changes was retrievable this session (NCBI ClinVar E-utilities queries did not return usable records). ACMG/AMP germline criteria are not the applicable framework; AMP/ASCO/CAP somatic tiering would be appropriate. PERISCOPE describes *"a pathogenic heterozygous missense variant c.1562A>G (p.His521Arg)"* (PMID 41657107).

**Variant type/class.** Exclusively **heterozygous missense** substitutions clustering in a few hotspots. This pattern is shared across all TRAF7-driven neoplasms: *"TRAF7 mutations in adenomatoid tumors, meningiomas, and intraneural perineuriomas are all heterozygous missense mutations that cluster within a few mutational hotspots in the WD40 repeat domains at the C-terminus of the TRAF7 protein"* (Goode et al., paraphrased in search synthesis; see [*Mod Pathol* 2018;31(4):660–673, PMID 29148537](https://pubmed.ncbi.nlm.nih.gov/29148537/)).

**Somatic vs germline origin.** **Somatic.** Germline TRAF7 missense variants — also clustering in WD40 repeats — cause a *different*, non-neoplastic developmental disorder (CAFDADD / TRAF7 syndrome; MIM 618164), with no perineurioma reported in the retrieved literature (PMID 32376980; PMID 34513876). This germline/somatic dichotomy at the same protein domain is a notable and clinically important distinction.

**Allele frequency in population databases.** **Not retrieved.** gnomAD constraint metrics (pLI, LOEUF, missense o/e) for TRAF7 could not be obtained — gnomAD's browser is a JavaScript application that returned no data to WebFetch. This should be filled in directly from gnomAD. The hotspot variants are somatic and would not be expected at appreciable population frequency.

**Functional consequences.** Klein et al.: the mutations *"are predicted to inactivate the interaction of TRAF7 with other proteins or destabilize the WD40 domain"* (PMID 28019650) — i.e., **loss of a protein–protein interaction surface**, computationally inferred. Functionally, Goode et al. showed in adenomatoid tumours (same WD40 hotspots) that *"mutant TRAF7 expression increased NF-kB phosphorylation and L1CAM expression"* (PMID 29148537), i.e. a **gain** of NF-κB output. Reconciling these: because wild-type TRAF7 *suppresses* NF-κB (see §6), loss-of-interaction at the WD40 domain would de-repress NF-κB — making these variants most plausibly **loss-of-function with respect to NF-κB restraint, and therefore gain-of-function with respect to downstream pathway output**. This interpretation is **inferred, not directly demonstrated in perineurioma tissue.**

### 4.3 Pathogenic variants — NF2

- Point mutations in 4/8 (50%) perineurial cell tumours: 5′-UTR, exons 3, 6, 8; amino-acid changes at codons **83, 182, 241**; LOH at the NF2 locus with documented allele deletion in one case; classical **two-hit tumour-suppressor** mechanism (PMID 11290539)
- Whole-arm or large **22q deletions** containing NF2 in 6/14 soft-tissue perineuriomas (PMID 30303818) and in 2/16 intraneural perineuriomas (PMID 28019650); FISH 22q11 deletion in soft-tissue perineurioma (PMID 9042282)
- PERISCOPE: interphase FISH (EWSR1 probe as a chr22 surrogate) showed signal loss in **3/5** evaluable cases, *"though results were limited by tissue availability"* (PMID 41657107)
- Germline NF2 context: 22q loss including **NF2, SMARCB1 and LZTR1** (PMID 32271143)

### 4.4 Modifier genes

**None identified.** No modifier-gene study for perineurioma was retrievable.

### 4.5 Epigenetic information

Direct methylation profiling of perineurioma was **not retrievable** (no ENCODE, Roadmap, MethBase or DiseaseMeth entry found). The only adjacent datum: a related TRAF7-mutated mesenchymal entity was profiled — *"On methylation profiling, the tumors clustered with the undifferentiated sarcoma and myxofibrosarcoma methylation classes and were distinct from morphologic mimics"* — but these were **TRAF7-mutated fibromyxoid spindle cell tumours, not perineuriomas** ([*Am J Surg Pathol* 2023;47(2):270–277, PMID 36395468](https://pubmed.ncbi.nlm.nih.gov/36395468/)). **A perineurioma methylation class has not been defined in any retrieved source — this is a clear research gap.**

### 4.6 Chromosomal abnormalities

This is the dominant genomic feature of the **soft-tissue** form. Carter et al. (14 cases, WES + SNP array; PMID 30303818):

- *"Thirteen cases showed 2 or more chromosomal abnormalities, composed primarily of large deletions"*
- **22q deletion (NF2 locus): n=6**
- **17q deletion (NF1 locus): n=4** — mutually exclusive with 22q deletion
- Additional losses: **chr2, chr6, chr10**
- **chr7 chromothripsis: n=1**
- *"No TRAF7 mutations or alterations were identified in any case"*

Intraneural perineurioma, by contrast, is largely **chromosomally quiet**, with 22q deletion as the alternative driver in TRAF7-wild-type cases (PMID 28019650). Malignant perineurioma: *"17q loss with focal homozygous NF1 deletion"* (PMID 42755235). No aneuploidy, translocation or inversion syndromes are associated with perineurioma. No DECIPHER/ECARUCA entries were retrieved.

---

## 5. Environmental Information

- **Environmental factors (toxins, radiation, pollution, occupational exposure): none identified.** No retrieved study, review or toxicogenomic resource associates any exposure with perineurioma of any subtype.
- **Lifestyle factors (smoking, diet, exercise, alcohol): none identified.** No CDC, WHO, NHANES or PubMed source links any behavioural factor to perineurioma.
- **Infectious agents: none; not applicable.** No bacterial, viral, fungal or parasitic trigger has been proposed. No entries in infectious-disease resources.

This is a disease where "not applicable" is the correct annotation for the entire environmental domain, and recording it as such is more useful than leaving it blank.

---

## 6. Mechanism / Pathophysiology

### 6.1 Ordered causal chain

**Branch A — Intraneural perineurioma, TRAF7 pathway (~60% of cases; the dominant mechanism)**

1. A **somatic heterozygous missense mutation** arises in a single perineurial cell within the endoneurium of one peripheral nerve fascicle, at one of three hotspots in the C-terminal WD40 repeat region of **TRAF7** (p.L519P / p.H521R in WD4, residues 515–554; p.S561R in WD5, residues 557–594) — **leads to** a structurally altered WD40 β-propeller. *Demonstrated: Klein 2017, PMID 28019650; domain boundaries from UniProt Q6Q0C0.*
2. The altered WD40 propeller **results in** loss of TRAF7's protein–protein interaction surface, or destabilisation of the domain itself — the mutations *"are predicted to inactivate the interaction of TRAF7 with other proteins or destabilize the WD40 domain."* *Computationally inferred, not structurally demonstrated (PMID 28019650).*
3. Loss of that interaction surface **leads to** failure of TRAF7's normal E3-ligase-dependent restraint of NF-κB: wild-type TRAF7 *"promotes K29-linked ubiquitination of NEMO and RELA, targeting them for lysosomal degradation and suppressing NF-κB activity"* (UniProt Q6Q0C0). **Mechanistically inferred for perineurioma.**
4. De-repression **results in** aberrant canonical NF-κB pathway activation. *Demonstrated in the analogous TRAF7-mutant lesion (adenomatoid tumour): "mutant TRAF7 expression increased NF-kB phosphorylation and L1CAM expression" (PMID 29148537). **Inferred, not shown in perineurioma tissue** — flagged as the single largest mechanistic gap for this disease.*
   - *Parallel/possible branch at this node:* TRAF7 also *"potentiates MAP3K3-mediated JUN/AP1 and DDIT3 activation"* and is described as *"a proapoptotic E3 ubiquitin ligase"* (UniProt Q6Q0C0; [Clark et al., *Science* 2013;339(6123):1077–1080, PMID 23348505](https://pubmed.ncbi.nlm.nih.gov/23348505/)). Whether WD40 hotspot mutants act by losing pro-apoptotic function, losing NF-κB restraint, or neomorphically, **remains unresolved**. A 2025 review states TRAF7 *"activates MEKK3 and KLF2/4 signaling, inhibits MEK1/2 and c-Myb along with an NF-κβ-modulator, and stabilizes VE-cadherins in cell junctions"* ([*Mol Med* 2025;32(1):4, PMID 41372821](https://pubmed.ncbi.nlm.nih.gov/41372821/)).
5. Altered NF-κB/MAP3K3 signalling **leads to** clonal expansion of the mutant perineurial cell **inside the endoneurial compartment**, rather than from the perineurium outward. *Demonstrated by lesion architecture and lineage markers.*
6. The expanding perineurial clone **results in** the pathognomonic **pseudo-onion bulb**: concentric whorls of EMA⁺ perineurial cells wrapped around residual nerve fibres. Electron microscopy in 8 PERISCOPE patients revealed *"interdigitating perineurial processes, pinocytotic vesicles and discontinuous basal lamina"* (PMID 41657107). *Demonstrated.* **Note this is mechanistically distinct from a true onion bulb (HP:0003383), which is supernumerary Schwann cells after repeated de/remyelination; here the whorls are perineurial.*
7. Pseudo-onion bulb proliferation **leads to** fusiform enlargement of the affected fascicle(s) within a relatively inextensible connective-tissue sheath — **resulting in** mechanical compression, distortion and strangulation of the contained axons. *Inferred from architecture and imaging (fusiform enlargement in 10/10, PMID 41657107); cross-sectional area *"at least twice as large as that of the contralateral side"* on ultrasound (PMID 40302315).*
8. Chronic axonal compromise **results in** axonal loss and secondary Schwann-cell/myelin changes — focal S-100 positivity in 30% of PERISCOPE cases was *"consistent with residual Schwann cells"* (PMID 41657107); neurofilament protein positivity in 50% confirms entrapped axons.
9. Axonal loss **leads to** a **motor-predominant** focal mononeuropathy. *Why motor fibres suffer disproportionately is not explained in any retrieved source — an unanswered mechanistic question.* Clinically: motor deficits in 100% of cases, sensory in 52–80% (PMIDs 41657107, 30637060, 19567701, 34030186).
10. Progressive denervation **results in** target-muscle weakness (MRC ≤2) and atrophy; chronic denervation **leads to** fixed functional loss that is poorly reversible — PERISCOPE: tendon-transfer *"outcomes were heterogeneous,"* reflecting *"the complexity of restoring function after chronic denervation."*
11. The lesion then **plateaus**: it enlarges radiologically without extending to new nerves (*"no lesions grew to involve a new nerve or division of a nerve"*; growth *did not* correlate with clinical worsening, PMID 30481319) and does **not** transform to malignancy in any retrieved series — **resulting in** a static or very slowly progressive, non-lethal but functionally disabling end state.

**Branch B — Intraneural perineurioma, NF2 pathway (minority; mutually exclusive with Branch A)**

1. Loss of chromosome 22q (or biallelic NF2 point mutation + LOH) **leads to** loss of merlin/schwannomin. *Demonstrated: PMID 32271143 (22q loss including NF2, SMARCB1, LZTR1); PMID 11290539 (two-hit NF2 inactivation in 50% of perineurial cell tumours).*
2. Merlin loss **results in** loss of contact-dependent growth inhibition in the perineurial cell. *Inferred by analogy to schwannoma/meningioma biology; not demonstrated in perineurioma.*
3. From here the chain **converges on Branch A step 5** (clonal perineurial proliferation → pseudo-onion bulbs → axonal compromise). The two pathways are described as *"two mutually exclusive pathways involving NF2 and TRAF7 mutations"* (PMID 32271143), mirroring the mutual exclusivity of TRAF7 and NF2 in meningioma ([Reuss et al., *Acta Neuropathol* 2013;125(3):351–358, PMID 23404370](https://pubmed.ncbi.nlm.nih.gov/23404370/); PMID 23348505).

**Branch C — Soft-tissue (extraneural) perineurioma**

1. Large-scale **chromosomal deletion** occurs in a perineurial-lineage cell outside a recognisable nerve: **either** 22q including NF2 (6/14) **or** 17q including NF1 (4/14) — mutually exclusive — commonly with additional losses on chr2/6/10, and occasionally catastrophic rearrangement (chr7 chromothripsis) — **leads to** haploinsufficiency/loss of merlin **or** neurofibromin. *Demonstrated: PMID 30303818.*
2. Neurofibromin loss **results in** failure of RAS-GAP activity and consequent **RAS–MAPK activation** (the canonical NF1 mechanism; *inferred here by analogy — RAS-MAPK activation has not been measured in perineurioma*). Merlin loss instead **results in** loss of contact inhibition. *Branch point.*
3. Either path **leads to** clonal proliferation of extraneural perineurial cells forming *"a storiform and focally whorled growth pattern"* (PMID 15958848) — **resulting in** a circumscribed, unencapsulated, painless soft-tissue mass with no nerve deficit.
4. Variant morphology emerges by stromal/cytological modulation — **resulting in** sclerosing (dense collagen, epithelioid cords: PMID 9414186), reticular (*"a predominantly lace-like or reticular growth pattern composed of anastomosing cords of fusiform cells"*: PMID 11257623), or pseudolipoblastic (*"bland, epithelioid cells with striking intracytoplasmic vacuolization"*: [PMID 27395366](https://pubmed.ncbi.nlm.nih.gov/27395366/)) phenotypes. *The determinants of variant morphology are unknown.*

**Branch D — Colorectal mucosal perineurioma / benign fibroblastic polyp (mechanistically inverted)**

1. **BRAF V600E** arises in colonic **crypt epithelium** — **leads to** constitutive MAPK activation and a serrated/hyperplastic epithelial phenotype. *Demonstrated: BRAF V600E in 63% of 29 polyps (PMID 20962618); 54% of epithelial components (PMID 29747061).*
2. The serrated epithelial lesion **results in** an accompanying pericryptic stromal proliferation that acquires a perineurial immunophenotype — **but the stroma does not carry the BRAF mutation**: *"BRAF V600E mutation was detected in 54% of the epithelial but in none of the stromal components"* (PMID 29747061); *"BRAF mutations are limited to the serrated crypt epithelium"* (PMID 29463272).
3. Therefore the perineurial component is best modelled as **reactive or secondarily neoplastic**, plausibly from *"modified pericryptic fibroblasts"* (PMID 20962618) — **resulting in** a *"true mixed epithelial-stromal polyp."* **This inverts the causal direction relative to Branches A–C and means colorectal "perineurioma" may not belong under the same mechanistic annotation as nerve-associated perineurioma.** This is an important distinction for a knowledge base.

**Branch E — Hybrid schwannoma–perineurioma (separate entity)**

1. **VGLL3 rearrangement** (fusing VGLL3 to CHD7, CHD9 or MAMLD1) **leads to** a biphasic tumour of ~60–70% Schwann cells and 30–40% perineurial cells, arranged as *"parallel layers of alternating S100 and EMA-positive cells"* (PMID 19623031; PMID 33649458). These are *"an altogether pathologically distinct entity"* and **should not be annotated under MONDO:0019404's mechanism.**

### 6.2 Molecular pathways

| Pathway | Involvement | Suggested GO term | Evidence |
|---|---|---|---|
| **Canonical NF-κB signalling** | Central inferred node for TRAF7-mutant INP; wild-type TRAF7 restrains it via K29-linked ubiquitination of NEMO/RELA | **GO:0007249** canonical NF-kappaB signal transduction; **GO:0043122** regulation of; **GO:0043123** positive regulation of | UniProt Q6Q0C0; PMID 29148537 (demonstrated in adenomatoid tumour) |
| Non-canonical NF-κB | Possible, unstudied | **GO:0038061** non-canonical NF-kappaB signal transduction | — |
| **MAP3K3 (MEKK3) → JUN/AP-1, DDIT3** | TRAF7 potentiates; consequence of mutation unstudied in perineurioma | (GO term not verified this session) | UniProt Q6Q0C0; PMID 41372821 |
| **RAS–MAPK** | Inferred for NF1-deleted soft-tissue perineurioma; **demonstrated (via BRAF V600E) in the epithelial component of colorectal polyps** | (GO term not verified this session) | PMID 30303818 (inferred); PMID 20962618 (BRAF, epithelium) |
| **Merlin / Hippo–contact inhibition** | Inferred for NF2-altered cases | (GO term not verified this session) | PMID 11290539; PMID 30303818 |
| **Ubiquitin–proteasome / E3 ligase activity** | Direct biochemical function of TRAF7 (EC 2.3.2.27); also SUMO-ligase activity | (GO term not verified this session) | UniProt Q6Q0C0 |
| KEGG/Reactome/WikiPathways perineurioma-specific maps | **Not retrieved** — no pathway-database entry for perineurioma was found | — | — |

### 6.3 Cellular processes

- **Clonal cell proliferation** of perineurial cells (the core process)
- **Loss of contact-dependent growth inhibition** (NF2-altered cases; inferred)
- **Apoptosis dysregulation** — TRAF7 is *"a proapoptotic E3 ubiquitin ligase"* (PMID 23348505); whether WD40 mutants impair apoptosis in perineurial cells is **untested**
- **Cell-junction biology** — TRAF7 *"stabilizes VE-cadherins in cell junctions"* (PMID 41372821); perineurial cells themselves depend on **tight junctions** (claudin-1 expression; PMID 12459629), making junctional dysregulation a mechanistically attractive but unstudied axis
- **Barrier function loss** — the perineurium forms part of the blood–nerve barrier; EM shows *"discontinuous basal lamina"* in INP (PMID 41657107)
- **Inflammation / immune involvement: no evidence.** No autoimmune, immunodeficiency or chronic-inflammatory mechanism was reported in any retrieved source. NF-κB involvement here is a proliferative, not an inflammatory, mechanism.

### 6.4 Protein dysfunction

**TRAF7** (UniProt Q6Q0C0; 670 aa):
- **RING-type zinc finger**: residues 131–165 (E3 ligase catalytic)
- **TRAF-type zinc finger**: residues 222–276
- **Seven WD40 repeats**: 394–669 — WD1 394–433, WD2 437–474, WD3 477–513, **WD4 515–554**, **WD5 557–594**, WD6 597–638, WD7 641–669
- **All three perineurioma hotspots fall in WD4 (L519, H521) and WD5 (S561)** — i.e., in adjacent blades of the β-propeller, consistent with disruption of a single interaction face
- Activity: E3 ubiquitin and SUMO ligase (EC 2.3.2.27); homodimeric; interacts with MAP3K3, GRIP1/2, DLG and multiple PDZ-domain proteins
- Localisation: cytoplasm, cytoplasmic vesicles, nucleus; colocalises with MAP3K3 in vesicle-like cytoplasmic structures
- **No experimental structure of the mutant WD40 domain, and no AlphaFold-based or PDB-based structural analysis of the perineurioma hotspots, was retrieved.** This is a tractable gap.

**NF2/merlin** (UniProt P35240): inactivated by truncating/point mutations and 22q loss; the two-hit mechanism was documented in perineurial cell tumours (PMID 11290539).

### 6.5 Metabolic and biochemical changes

- **GLUT1 (SLC2A1)** is constitutively expressed by normal and neoplastic perineurial cells — *"perineuriums were positive for Glut1 as well as for epithelial membrane antigen (EMA)"* and *"Glut1 as well as EMA are specific to perineurial cells"* ([Hirose et al., *Mod Pathol* 2003;16(4):293–298, PMID 12692193](https://pubmed.ncbi.nlm.nih.gov/12692193/)). **This is a lineage marker, not evidence of metabolic reprogramming.** CHEBI: glucose is the relevant transported entity (specific CHEBI ID not verified this session).
- **Glucose metabolism in vivo is low.** FDG PET in 8 INP patients showed *"mildly increased FDG uptake relative to the contralateral nerve"* with **mean SUVmax 1.5** — low-level metabolic activity, and the authors note *"unexpectedly elevated uptake warrant[s] diagnostic reconsideration"* ([Amrami et al., *J Neurosurg Case Lessons* 2026;12(13):CASE26698, PMID 42804796](https://pubmed.ncbi.nlm.nih.gov/42804796/)). This is a clean, clinically useful demonstration that despite GLUT1 positivity, perineurioma is metabolically indolent.
- **No enzyme deficiency, receptor dysfunction or ion-channel defect is implicated.** No HMDB, BRENDA, lipid or amino-acid metabolic abnormality was retrieved.

### 6.6 Tissue damage mechanisms

The damage mechanism is **mechanical/compressive and chronic**, not oxidative, ischaemic, inflammatory or necrotic. Pseudo-onion-bulb proliferation within the endoneurium compresses axons, producing axonal loss and chronic denervation of target muscle. Malignant perineurioma is the exception, where invasive growth and metastasis occur (PMID 9808129). No fibrosis, necrosis or oxidative-stress mechanism was reported for benign perineurioma.

### 6.7 Epigenetic changes

**Not characterised** (see §4.5). No perineurioma methylation class exists in any retrieved source.

### 6.8 Molecular profiling

| Modality | Status |
|---|---|
| **Genomics** | Well characterised: WES + SNP array (soft tissue, n=14, PMID 30303818); WES + PatternCNV + array CGH (intraneural, n=16, PMID 28019650); targeted Sanger of TRAF7 exons 17–18 + chr22 FISH (n=10, PMID 41657107) |
| **Transcriptomics** | **No perineurioma transcriptome retrieved.** RNA-seq has been applied to the *hybrid* schwannoma-perineurioma (fusion detection, PMID 33649458) and used negatively in TRAF7-mutant fibromyxoid tumours. For germline TRAF7 disease, *"Transcriptome studies of patient fibroblasts revealed altered gene expression profiles"* (PMID 32376980) — **a different disease, but a possible methodological template.** No GEO/ArrayExpress perineurioma dataset was identified |
| **Proteomics** | **None retrieved.** No PRIDE/ProteomeXchange perineurioma dataset |
| **Metabolomics / lipidomics** | **None retrieved** |
| **Epigenomics** | **None retrieved** (see §4.5) |
| **Single-cell / spatial transcriptomics** | **None retrieved.** Given that the lesion's defining feature is a *spatial* architecture (concentric perineurial whorls around residual axons with interspersed residual Schwann cells), spatial transcriptomics is an obviously well-matched unexploited technology |
| **Multi-omics integration** | **None retrieved.** No TCGA/ICGC/cBioPortal perineurioma cohort |
| **Functional genomics (CRISPR/RNAi)** | **No perineurioma screen retrieved.** No DepMap perineurioma model line identified |

### 6.9 Cell types and ontology suggestions

| Entity | Ontology term | Verified source |
|---|---|---|
| **Perineurial cell** (the neoplastic cell) | **CL:0002576** — "a glial cell component of the perineurium with... thin long bipolar cytoplasmic processes and specialized junctions that distinguish it from fibroblasts" | [OLS4 CL](https://www.ebi.ac.uk/ols4/api/search?q=perineurial%20cell&ontology=cl&rows=10) |
| Schwann cell (residual, entrapped; S-100⁺ in 30% of INP) | (CL term not verified this session) | PMID 41657107 |
| Pericryptic fibroblast (proposed origin of colorectal mucosal perineurial stroma) | (CL term not verified this session) | PMID 20962618 |
| Canonical NF-κB signal transduction | **GO:0007249** (BP) | [OLS4 GO](https://www.ebi.ac.uk/ols4/api/search?q=I-kappaB+kinase+NF-kappaB+signaling&ontology=go&rows=8) |
| Positive regulation of canonical NF-κB signal transduction | **GO:0043123** (BP) | same |
| Regulation of canonical NF-κB signal transduction | **GO:0043122** (BP) | same |
| Non-canonical NF-κB signal transduction | **GO:0038061** (BP) | same |

---

## 7. Anatomical Structures Affected

### 7.1 Organ / system level

- **Primary system: peripheral nervous system.** Intraneural perineurioma affects a single peripheral nerve or nerve fascicle. Prasad et al. established an anatomical boundary: among 56 cases, 15 (27%) involved the proximal lumbosacral or brachial plexus, yet *"none extended proximal to the dorsal root ganglia,"* and they concluded *"the occurrence of classic intraneural perineuriomas intradurally is exceedingly rare, if at all present,"* attributing this to **the paucity of perineurial cells at nerve-root level** ([*Neurosurgery* 2017;80(2):226–234, PMID 28173435](https://pubmed.ncbi.nlm.nih.gov/28173435/)). **This is a mechanistically elegant anatomical constraint: the tumour cannot occur where its cell of origin is absent.**
- **Secondary (downstream) involvement: musculoskeletal system** — denervation weakness and atrophy of target muscles; secondary joint contracture and gait impairment are implied by the need for tendon transfer in 7/10 PERISCOPE patients.
- **Soft-tissue form: integumentary and musculoskeletal systems** (dermis, subcutis, deep soft tissue of extremities and trunk).
- **Visceral involvement: digestive system** — colon (93.24% of 148 GI cases), rectum (14.86%), stomach (4.73%), ileum, oesophagus (PMID 40225020; PMIDs 41954346, 42351541, 42112490).
- **Other reported organ sites:** orbit (PMIDs 42578239, 41412874, 39028107), oral cavity/tongue (PMIDs 41010284, 34074156), calvarium (perineurioma-like, PMID 42216621), chest wall (PMID 41502903).
- **No cardiovascular, respiratory, endocrine, renal or CNS-parenchymal involvement** is reported.

### 7.2 Tissue and cell level

- **Tissue types affected: nervous tissue (peripheral nerve) and connective tissue.** The perineurium is a specialised connective-tissue/glial-hybrid sheath.
- **Target cell population: perineurial cell (CL:0002576)** — EMA⁺, claudin-1⁺, GLUT1⁺, collagen IV⁺, S-100⁻, SOX10⁻.
- **Bystander populations:** residual Schwann cells (S-100 focally⁺ in 3/10 PERISCOPE cases), residual axons (neurofilament protein⁺ in 5/10), endoneurial collagen.
- Canine data corroborate the perineurial immunophenotype: tumours with perineurial differentiation were *"strongly immunoreactive for claudin-1 and negative for Sox10 and GFAP"* ([Tekavec et al., *Vet Sci* 2022;9(5):204, PMID 35622732](https://pmc.ncbi.nlm.nih.gov/articles/PMC9144584/)).

### 7.3 Subcellular level

Ultrastructural features define the lineage. PERISCOPE EM in 8 patients showed *"interdigitating perineurial processes, pinocytotic vesicles and discontinuous basal lamina"* (PMID 41657107). Relevant compartments:

- **Plasma membrane / tight junctions** — claudin-1, a *"tight junction-associated protein"* (PMID 12459629); GLUT1 is a plasma-membrane transporter
- **Pinocytotic (plasmalemmal) vesicles** — hallmark of perineurial cells
- **Basal lamina / external lamina** — discontinuous in neoplastic cells; collagen IV⁺ by IHC (PMID 12836021)
- **Cytoplasm, cytoplasmic vesicles, nucleus** — TRAF7 localisation, colocalising with MAP3K3 in vesicle-like cytoplasmic structures (UniProt Q6Q0C0)

*Specific GO Cellular Component IDs were not verified in this session and should be looked up before annotation (candidates: tight junction, basement membrane, plasma membrane, pinocytic vesicle).*

### 7.4 Localisation with UBERON terms

| Structure | UBERON ID | Verified |
|---|---|---|
| **Perineurium** (the lesional compartment of origin) | **UBERON:0000121** — "A layer of thin, concentrically arranged cells with interspersed collagen" | [OLS4](https://www.ebi.ac.uk/ols4/api/search?q=epineurium&ontology=uberon&rows=5) |
| **Endoneurium** (where INP proliferates) | **UBERON:0000123** | [OLS4](https://www.ebi.ac.uk/ols4/api/search?q=endoneurium&ontology=uberon&rows=5) |
| **Epineurium** | **UBERON:0000124** | OLS4 |
| **Nerve fibre** (compressed element) | **UBERON:0006134** | OLS4 |
| **Sciatic nerve** (most frequent INP site) | **UBERON:0001322** | [OLS4](https://www.ebi.ac.uk/ols4/api/search?q=sciatic+nerve&ontology=uberon&rows=5&exact=true) |
| **Common fibular (peroneal) nerve** | **UBERON:0001324** | [OLS4](https://www.ebi.ac.uk/ols4/api/search?q=common+peroneal+nerve&ontology=uberon&rows=6) |
| Tibial nerve | UBERON:0001323 | OLS4 |
| Deep fibular nerve | UBERON:0035207 | OLS4 |
| Superficial fibular nerve | UBERON:0035526 | OLS4 |
| **Median nerve** | **UBERON:0001148** | [OLS4](https://www.ebi.ac.uk/ols4/api/search?q=median%20nerve&ontology=uberon&rows=4) |
| **Brachial nerve plexus** | **UBERON:0001814** | [OLS4](https://www.ebi.ac.uk/ols4/api/search?q=brachial%20plexus&ontology=uberon&rows=4) |
| Radial, ulnar nerve, lumbosacral plexus, sigmoid colon, rectum, orbit, tongue | *UBERON IDs not verified this session* | — |

**Nerve-site frequency (intraneural perineurioma):**

| Series | Distribution |
|---|---|
| Lenartowicz 2021, 172 pooled cases (PMID 34284162) | **Sciatic 41.9%**, then median and radial |
| Uerschels 2020, 77 cases (PMID 32054523) | Sciatic 16 (20.8%), peroneal 11 (14.3%), median 11 (14.3%) |
| PERISCOPE 2026, 10 cases (PMID 41657107) | Common fibular 3, ulnar 2, sciatic 2, lumbosacral plexus 1, median 1, radial 1 |
| Brand 2022, 30 cases (PMID 34030186) | **Sciatic and radial** most common |
| Mauermann 2009, 32 cases (PMID 19567701) | **Sciatic** most frequent |
| Alkhaili 2018, 19 cases (PMID 30637060) | Upper limb 11 (4 brachial plexus); lower limb 8 (5 peroneal, 3 sciatic) |

**Lateralisation: unilateral and unifocal.** Unifocal disease is one of the 8 Perineurioma Diagnostic Criteria (PMID 29192862), and lesions do not spread to new nerves over time (PMID 30481319). Bilateral or multifocal disease is exceptional.

---

## 8. Temporal Development

### 8.1 Onset

| Subtype | Typical age of onset | Pattern |
|---|---|---|
| **Intraneural** | **Adolescence / young adulthood.** Median symptom onset **21 y** (range 9–37) (PERISCOPE); median age at diagnosis **18 y** across 172 cases (PMID 34284162); mean **21.0 ± 13.9 y** (PMID 32054523); median **31.2 y** (range 15–64) (PMID 30637060); Mauermann's cohort was exactly half children, half adults (16/16, PMID 19567701). Paediatric onset occurs down to **age 4** (PMID 40353166) | **Insidious, chronic** — painless, slowly progressive weakness |
| **Soft tissue, conventional** | Mean **46 y** (81 cases, PMID 15958848) | Insidious painless mass |
| **Sclerosing variant** | Median **24.5 y**; young adults, fingers/palms, male predominance (PMID 9414186) | Insidious |
| **Reticular variant** | 34–61 y (PMID 11257623) | Insidious |
| **Hybrid schwannoma/perineurioma** | Mean **38 y** (PMID 19623031) | Insidious |
| **GI (colorectal)** | Mean **51 y** (SD 14.87; range 24–87) (PMID 40225020) | Usually **asymptomatic**, screening-detected (80.24%) |
| **Perineurial MPNST** | **11–83 y** (PMID 9808129) | Variable; can be rapid |
| **Congenital/neonatal** | Exceptional: sclerosing perineurioma of the orbit in a **7-week-old** (PMID 39028107) | — |

### 8.2 Progression

- **No formal staging system exists** for benign perineurioma; ICD-O behaviour code **9571/0** denotes benign, and intraneural perineurioma is designated **WHO grade I** (NCIT:C6911).
- **Progression rate: slow.** *"It is a benign, very slow growing peripheral nerve sheath tumor"* (PMID 34030186). *"Static or slowly progressive"* (PMID 19567701).
- **Course: progressive then plateauing.** Radiological growth continues modestly without clinical correlation and without recruitment of new nerves (PMID 30481319). Brand et al.: *"Seventy percent of the patients (n = 21) received a magnetic resonance imaging (MRI) within 5 years postoperatively, in which no progress was shown"* (PMID 34030186). Lenartowicz: among conservatively managed patients, **67.7% were neurologically stable** (PMID 34284162).
- **Duration: chronic, lifelong lesion**, but the *neurological deficit* typically stabilises rather than continuing to deteriorate.
- **Not self-limited, not relapsing-remitting, not episodic.** The deficit is fixed once established, which is why timing of intervention matters.

### 8.3 Patterns

- **Spontaneous remission: never reported** in any retrieved series.
- **Treatment-induced remission:** a minority improve neurologically after decompression/neurolysis (see §12), but complete neurological restitution is uncommon.
- **Critical period / window of opportunity.** This is arguably the most clinically actionable temporal fact. Because the deficit results from chronic denervation and becomes irreversible, and because the median delay from onset to intervention is **34.5 months** (PERISCOPE), the authors advocate *"early recognition, structured functional monitoring and risk-adapted intervention"* (PMID 41657107). The counter-consideration is that the lesion itself does not spread, so **the window is for functional rescue, not for oncological control** — hence Mauermann's conclusion that these tumours *"probably should not be resected routinely"* (PMID 19567701).

---

## 9. Inheritance and Population

### 9.1 Epidemiology

**No population-based incidence or prevalence estimate for perineurioma was retrievable** from Orphanet, SEER, GBD, WHO, CDC or any national registry in this session. This is a genuine and important gap; any prevalence figure entered into a knowledge base should be flagged as unavailable rather than estimated.

What *is* retrievable are proportional frequencies:

| Measure | Value | Source |
|---|---|---|
| Intraneural perineurioma as a share of peripheral nerve tumours | *"approximately 1% of peripheral nerve tumors"* | Pisapia et al., *Surg Neurol Int* 2025;16:129, [PMID 40353166](https://pubmed.ncbi.nlm.nih.gov/40353166/) |
| Perineurial differentiation among MPNST | *"4% of MPNST show perineurial cell differentiation"* (5 previously unreported cases found in a registry of **121** MPNST) | Hirose et al., [PMID 9808129](https://pubmed.ncbi.nlm.nih.gov/9808129/) |
| INP among NF2 patients (institutional) | 2 of **112** INP patients had NF2 | Pendleton et al., [PMID 32529330](https://pubmed.ncbi.nlm.nih.gov/32529330/) |
| Total published INP cases (as of 2021 review) | **172 cases across 72 studies** | Lenartowicz et al., [PMID 34284162](https://pubmed.ncbi.nlm.nih.gov/34284162/) |
| Total published GI perineuriomas/benign fibroblastic polyps | **148 cases across 25 publications (2004–2024)** | Alenezi et al., [PMID 40225020](https://pmc.ncbi.nlm.nih.gov/articles/PMC11991822/) |
| Published gastric perineuriomas | *"Only twelve gastric perineurioma cases exist in literature"* | Girolami et al., [PMID 41954346](https://pubmed.ncbi.nlm.nih.gov/41954346/) |
| Largest single-institution soft-tissue series | **81 cases** | Hornick & Fletcher, [PMID 15958848](https://pubmed.ncbi.nlm.nih.gov/15958848/) |
| PubMed literature volume | **343** publications with "perineurioma" in the title (query run 2026-11-20) | [PubMed esearch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=perineurioma%5BTitle%5D) |

### 9.2 Genetic etiology parameters

Because perineurioma is a **sporadic somatic neoplasm**, most classical Mendelian parameters are **not applicable**. Recording them as "not applicable" is correct:

| Parameter | Status |
|---|---|
| **Inheritance pattern** | **Not applicable — sporadic/somatic.** No OMIM entry exists. Exception: rare occurrence in individuals with germline **NF2** (autosomal dominant) or germline **NF1** (autosomal dominant), where the perineurioma is a tumour arising on a dominantly inherited predisposing background (PMIDs 32529330, 32271143, 24393170, 42755235) |
| **Penetrance** | Not applicable for the tumour itself. For NF2/NF1 carriers, perineurioma is a **very low-penetrance** manifestation (2/112 INP had NF2; a single soft-tissue case in NF1 at time of that report, PMID 24393170) |
| **Expressivity** | Not applicable in the Mendelian sense. Phenotypic variability is substantial across subtypes and anatomical sites |
| **Genetic anticipation** | Not applicable — not a repeat-expansion disorder |
| **Germline mosaicism** | Not reported. (The hemi-body port-wine-stain + territorial perineurioma case, PMID 24092235, and the perineurioma-within-nevus-sebaceous case, PMID 43040817, raise the untested possibility of **somatic mosaicism** in a developmental field) |
| **Founder effects** | None reported |
| **Consanguinity** | No role reported |
| **Carrier frequency** | Not applicable |

### 9.3 Population demographics

**Sex ratio:**

| Cohort | Sex distribution |
|---|---|
| INP, 172 pooled cases (PMID 34284162) | **54.4% female** |
| INP, 77 cases (PMID 32054523) | 42 F (54.5%) / 35 M (45.5%) |
| INP, 10 cases (PERISCOPE, PMID 41657107) | 6 F / 4 M |
| INP, 19 cases (PMID 30637060) | 10 M / 9 F (essentially equal) |
| Soft tissue, 81 cases (PMID 15958848) | 43 F / 38 M |
| Hybrid schwannoma/perineurioma, 42 cases (PMID 19623031) | 22 F / 20 M |
| **Sclerosing variant**, 19 cases (PMID 9414186) | **Predominantly young males** |
| GI, 148 cases (PMID 40225020) | **59.46% female** |

**Net: a mild female excess overall (~1.2:1), with the sclerosing acral variant being the exception (male-predominant).**

**Age distribution:** bimodal across the entity family — intraneural clusters in the **second and third decades** (median 18–21 y), soft-tissue in **middle age** (mean 46 y), GI later still (mean 51 y), sclerosing in **young adults** (median 24.5 y).

**Ethnic / geographic distribution:** **no ethnic predilection or geographic clustering has been reported**, and no variant-specific geographic distribution exists. Published cases span Europe, North America, South America (Brazil — PERISCOPE), Asia (Japan, China, Taiwan), the Middle East and Africa (PMID 30637060, Pan Afr Med J), consistent with a globally distributed sporadic tumour. One case explicitly describes a *"Caucasian toddler"* (PMID 41502903), but single-case ethnicity reporting carries no epidemiological weight.

---

## 10. Diagnostics

### 10.1 Imaging — the modern diagnostic centrepiece for intraneural perineurioma

**MRI.** PERISCOPE established a highly consistent triad: **fusiform nerve enlargement in 10/10 (100%)**, **T2-weighted hyperintensity in 9/10 (90%)**, and **homogeneous gadolinium enhancement in 10/10 (100%)**; lesions extended **>10 cm in 40%** of cases. The authors conclude that the *"MRI triad of fusiform enlargement, T2 hyperintensity and homogeneous enhancement strongly supports INP diagnosis"* (PMID 41657107). Alkhaili et al. reported *"an aspecific nerve enlargement... in 16 cases. Five patients presented with a typical fusiform tumor,"* hypo- to isointense on T1, hyperintense on T2, size 1–10 cm (PMID 30637060).

**Perineurioma Diagnostic Criteria (Wilson et al., 2018)** — the validated set that can **replace biopsy**:

1. No cancer history
2. Unifocal disease
3. Moderate-to-severe hyperintensity on T2-weighted MRI
4. Moderate-to-severe contrast enhancement
5. **Homogeneous** contrast enhancement
6. Fusiform shape
7. Enlargement of the involved nerve(s)
8. **Age ≤40 years**

When all eight are present, specificity and positive predictive value were both **1.0**, and tissue diagnosis becomes unnecessary ([Wilson et al., *J Neurosurg* 2018;129(4):1034–1040, PMID 29192862](https://pubmed.ncbi.nlm.nih.gov/29192862/); criteria list corroborated via [thejns.org](https://thejns.org/view/journals/j-neurosurg/129/4/article-p1034.xml)). **This is the single most important practical advance in perineurioma diagnosis and should be a headline entry in any knowledge base.**

**Technical caveat — MRI can miss it.** Restrepo et al. titled their paper "The almost-invisible perineurioma," noting perineuriomas remain underdiagnosed due to unfamiliarity and *"technical limitations with conventional MRI,"* and recommending **high-resolution 3-T MRI with gadolinium** to resolve internal nerve anatomy ([*Neurosurg Focus* 2015;39(3):E13, PMID 26323815](https://pubmed.ncbi.nlm.nih.gov/26323815/)). In a 4-year-old, *"MRI failed to visualize the pathology"* while ultrasound found it (PMID 40353166).

**High-resolution ultrasound.** Wang et al. studied 11 surgically/biopsy-confirmed INP cases (June 2015–June 2022): findings were fusiform nerve enlargement, hypoechogenicity, internal heterogeneity, centralised location, and *"blurred inner epineurium with continuous fascicular structure."* Critically, *"The cross-sectional area of the affected nerves was at least twice as large as that of the contralateral side,"* with consistent Doppler blood flow ([*Muscle Nerve* 2025;72(1):107–113, PMID 40302315](https://pubmed.ncbi.nlm.nih.gov/40302315/)). In the paediatric case above, ultrasound showed *"a well-defined fusiform hypoechoic mass"* 1.5 × 0.5 × 0.8 cm with the nerve traversing it (PMID 40353166).

**FDG PET.** Mean **SUVmax 1.5**, *"mildly increased FDG uptake relative to the contralateral nerve"*; PET is best used as a complementary modality, and unexpectedly high uptake should prompt reconsideration of the diagnosis (PMID 42804796).

**General peripheral-nerve-tumour imaging context:** *"Direct continuity with a neural structure or location along a typical nerve distribution, shape, and intrinsic magnetic resonance (MR) signal characteristics represent the most important signs"*; however *"benign and malignant neoplasms of peripheral nerves can usually not be distinguished with confidence"* on imaging alone ([Woertler, *Semin Musculoskelet Radiol* 2010;14(5):547–558, PMID 21072731](https://pubmed.ncbi.nlm.nih.gov/21072731/)).

**Endoscopic appearance (colorectal).** A 5-mm sigmoid lesion showed *"dilated round pits, reduced crypt density, and arborizing vessels"* ([PMID 42283027](https://pubmed.ncbi.nlm.nih.gov/42283027/)).

*RadLex/DICOM/Radiopaedia identifiers were not retrievable this session (Radiopaedia returned HTTP 402).*

### 10.2 Biopsy, histopathology and immunohistochemistry — the diagnostic reference standard

**Technique: targeted fascicular biopsy.** Brand et al. conclude *"biopsy of enlarged fascicles is essential for diagnosis and that complete resection is inadvisable for preserving nerve function"* (PMID 34030186). PERISCOPE performed diagnostic targeted fascicular biopsy in 9 patients **without postoperative neurological worsening** (PMID 41657107) — important safety evidence.

**Histology.**
- **Intraneural:** **pseudo-onion bulb** formation — concentric perineurial-cell whorls around nerve fibres within the endoneurium. Present in 100% of PERISCOPE cases; *"Morphological pseudo-onion bulb shape and/or specific immunohistochemical assay"* confirmed diagnosis in **17/18** biopsied patients (PMID 30637060).
- **Soft tissue, conventional:** *"a storiform and focally whorled growth pattern"* with variable cellularity and stroma (PMID 15958848); *"generally small, well-circumscribed but not encapsulated tumors"* with elongated, wavy cells (PMID 9042282).
- **Sclerosing:** *"abundant dense collagen and variable numbers of small, epithelioid, and spindled cells"* (PMID 9414186); *"thick collagen and variable numbers of small, epithelioid cells exhibiting corded, trabecular and whorled growth patterns"* (PMID 12836021).
- **Reticular:** *"a predominantly lace-like or reticular growth pattern composed of anastomosing cords of fusiform cells"* (PMID 11257623).
- **Pseudolipoblastic:** *"bland, epithelioid cells with striking intracytoplasmic vacuolization"* in *"net-like"* or *"microreticular"* patterns — submitted with *"concern that they represented high-grade liposarcomas"* (PMID 27395366). **A recognised diagnostic trap.**
- **Hybrid schwannoma/perineurioma:** well-circumscribed, unencapsulated, **lacking Antoni A/B zonation**; ~60–70% Schwann cells and 30–40% perineurial cells in *"parallel layers of alternating S100 and EMA-positive cells"* (PMID 19623031).
- **Malignant:** *"high mitotic activity, hypercellularity, hyperchromasia, and pleomorphism"* (NCIT:C207066); *"atypical spindle cells arranged in sweeping fascicles embedded in a myxoid matrix"* (PMID 12135468).

**Electron microscopy** (confirmatory, still used): *"interdigitating perineurial processes, pinocytotic vesicles and discontinuous basal lamina"* (PMID 41657107); EM confirmed diagnosis in the NF1-associated case (PMID 24393170).

**Immunohistochemistry panel.** This is the diagnostic linchpin.

| Marker | Expected result | Reported sensitivity / frequency | Source |
|---|---|---|---|
| **EMA (MUC1)** | **Positive** (may be focal/faint) | **100%** of 81 soft-tissue cases; **strong positivity in 10/10** INP; 75% of GI cases (84% in the three-marker subgroup) | PMIDs 15958848, 41657107, 40225020 |
| **Claudin-1** | Positive | **92%** of perineuriomas vs 0% in DFSP, low-grade fibromyxoid sarcoma, desmoplastic fibroblastoma, fibromatosis; 5/10 in PERISCOPE; 44.59% of GI cases (88% in three-marker subgroup) | PMIDs 12459629, 41657107, 40225020 |
| **GLUT1 (SLC2A1)** | Positive | Perineurium and perineurial tumours positive; 56.76% of GI cases (94% in three-marker subgroup) | PMIDs 12692193, 12836021, 40225020 |
| **Collagen type IV** | Positive (pericellular) | 44.59% of GI cases; positive in sclerosing variant and pseudolipoblastic variant | PMIDs 40225020, 12836021, 27395366 |
| **CD10** | Positive in sclerosing variant | 5/5 sclerosing cases | PMID 12836021 |
| **S-100 protein** | **Negative** (focal positivity = residual Schwann cells) | Negative in perineurioma; focally positive in 3/10 INP *"consistent with residual Schwann cells"* | PMIDs 12459629, 12692193, 41657107 |
| **SOX10** | **Negative** | Negative (canine perineurial-differentiated tumours: claudin-1⁺, SOX10⁻, GFAP⁻) | PMID 35622732 |
| **Neurofilament protein** | Positive in entrapped axons | 5/10 INP | PMID 41657107 |
| **CD34** | Variable/usually negative in tumour cells (marks fibroblastic cells) | Expressed in one NF1-associated case; negative in sclerosing variant | PMIDs 24393170, 12836021, 12692193 |
| **MUC4** | Negative (positive in low-grade fibromyxoid sarcoma — key discriminator) | — | PMID 29314300 |
| Cytokeratin, desmin | Negative | — | PMID 12836021 |

Why the panel matters: *"an immunophenotype that includes S-100 negativity and EMA positivity"* is the core, but *"EMA expression may be focal and/or faint,"* which is precisely why claudin-1 *"may play a valuable adjunctive role in difficult cases"* (PMID 12459629). Macarenco et al. likewise highlight EMA and S-100 with *"newer markers like claudin-1 and GLUT1 also valuable"* (PMID 17425397).

*LOINC and SNOMED CT codes for these specific IHC assays were not retrieved this session.*

### 10.3 Electrophysiology

**Nerve conduction studies and EMG** are used to localise and characterise the mononeuropathy, but are **not diagnostic of perineurioma specifically**. Alkhaili et al. noted NCS was performed but that *"imaging was more helpful than electrodiagnostic data,"* while still regarding *"a typical clinical presentation with appropriate MRI and nerve conduction study"* as suggestive (PMID 30637060). Wang et al. recommend ultrasound *"combined with MRI and electrophysiological studies for clinical decision-making and monitoring"* (PMID 40302315). **No perineurioma-specific electrodiagnostic signature was retrievable** — a targeted search returned no relevant studies.

### 10.4 Laboratory tests and biomarkers

- **No blood, urine, CSF or enzyme-assay test is diagnostic.** No circulating biomarker exists.
- **No FDA-recognised biomarker** for perineurioma was retrieved from biomarker resources.
- The only "biomarkers" are **tissue immunohistochemical lineage markers** (§10.2) and the **somatic TRAF7 mutation** (§10.5).

### 10.5 Genetic testing

**Current status: genetic testing is confirmatory/research-grade, not required for diagnosis.** No GTR-registered clinical gene panel for perineurioma was retrievable.

| Modality | Utility in perineurioma | Evidence |
|---|---|---|
| **Targeted single-gene sequencing (TRAF7 exons 17–18)** | The most practical assay; **but sensitivity is method-dependent and modest.** PERISCOPE used targeted Sanger sequencing of TRAF7 exons 17–18 (successful in 9/10) and detected the hotspot in only **2/9 (22.2%)** — *"lower than the approximately 60% reported in the largest prior series,"* attributed to *"methodological limitations and probable genetic heterogeneity"* | PMID 41657107 vs PMID 28019650 |
| **Whole-exome sequencing (WES)** | The discovery modality in both landmark studies (16 intraneural; 14 soft tissue). Clinically useful where hotspot assays are negative | PMIDs 28019650, 30303818 |
| **Whole-genome sequencing (WGS)** | Not reported in perineurioma | — |
| **SNP array / chromosomal microarray (CMA)** | **High yield in soft-tissue perineurioma** — 13/14 cases showed ≥2 chromosomal abnormalities (22q/NF2, 17q/NF1). Should be the first-line molecular test for the soft-tissue form | PMID 30303818 |
| **Array CGH** | Used to validate CNVs in the intraneural series | PMID 28019650 |
| **FISH** | Chromosome 22 assessment: EWSR1-probe signal loss in 3/5 PERISCOPE cases; M-bcr (22q11) probe showed 44% and 96% single-signal nuclei in soft-tissue perineurioma. Also used to exclude mimics (**FUS rearrangement** identifies low-grade fibromyxoid sarcoma) | PMIDs 41657107, 9042282, 29314300 |
| **Targeted RNA sequencing** | Negative for fusions in conventional perineurioma; **positive and diagnostic for VGLL3 rearrangement in hybrid schwannoma-perineurioma** (14/18) and for SETD1A::FOSB in a perineurioma-like tumour | PMIDs 36395468, 33649458, 41927362 |
| **BRAF V600E testing** | Relevant only to colorectal lesions, and only in the **epithelial** component | PMIDs 20962618, 29747061 |
| **Karyotyping, mtDNA testing, repeat-expansion testing** | **Not applicable** | — |
| **Methylation profiling** | Not established for perineurioma (see §4.5); has distinguished a TRAF7-mutant *mimic* | PMID 36395468 |

**Germline testing consideration:** in a patient with perineurioma plus features of NF2 or NF1, germline NF2/NF1 testing is justified (PMIDs 32529330, 32271143, 24393170). Perineurioma alone is **not** an indication for germline testing on current evidence.

### 10.6 Clinical criteria and differential diagnosis

**Standardised criteria:** The **Perineurioma Diagnostic Criteria** (§10.1) are the only validated clinical/radiological criterion set. Classification follows **WHO** (ICD-O 9571/0; intraneural = WHO grade I) ([Pathology Outlines WHO classification](https://www.pathologyoutlines.com/topic/softtissuewhoclassification.html); NCIT:C6911). No DSM involvement; ICD-11 coding is uncertain (see §1.2).

**Differential diagnosis — intraneural perineurioma:**

| Mimic | Distinguishing features |
|---|---|
| Schwannoma | S-100⁺/SOX10⁺, EMA⁻; eccentric mass, Antoni A/B zonation; may coexist (PMIDs 19623031, 31870821) |
| Localised/plexiform neurofibroma | S-100⁺, mixed cell population (PMID 21072731) |
| **Chronic inflammatory demyelinating polyneuropathy (CIDP) / MADSAM** | True onion bulbs (Schwann-cell, HP:0003383); multifocal; immunoresponsive. A 17-year-old with INP was *"initially suspected of having inflammatory disease or ALS"* (PMID 41822653) |
| **Motor neuron disease / ALS** | Same report (PMID 41822653) |
| Intraneural ganglion cyst | Cystic, non-enhancing; can coexist (PMID 31870821) |
| Fibrolipomatous hamartoma | Fat signal on MRI (PMID 21072731) |
| MPNST | Rapid growth, pain, heterogeneous enhancement, high FDG uptake |
| **Low-grade fibromyxoid sarcoma (LGFMS) arising in a nerve** | **MUC4⁺, GLUT-1⁺, but EMA⁻, claudin-1⁻, S-100⁻, with FUS rearrangement** — a genuinely dangerous trap, described in the median nerve of a 31-year-old presenting as carpal tunnel syndrome (PMID 29314300) |

**Differential diagnosis — soft-tissue perineurioma:**

| Mimic | Discriminator |
|---|---|
| Dermatofibrosarcoma protuberans, desmoplastic fibroblastoma, fibromatosis | **Claudin-1-negative** (PMID 12459629) |
| Myoepithelial tumours, certain sarcomas (vs reticular variant) | PMID 11257623 |
| **Liposarcoma** (vs pseudolipoblastic variant) | PMID 27395366 |
| Fibroma of tendon sheath (vs sclerosing variant) | PMID 9414186 |
| Superficial acral fibromyxoma | CD34⁺; PMID 11486169 explicitly lists sclerosing perineurioma in its differential |
| **Epithelioid sarcoma** | Shares GLUT-1/claudin-1/EMA, but **CD34⁺ (all cases) and Fli-1⁺**, whereas meningiomas were CD34⁻; Smith et al. suggest *"epithelioid sarcoma may be a form of malignant perineurioma... reflecting the close relationship between perineurium and meningothelium"* (PMID 16324194). **A conceptually important and unresolved boundary** |
| GIST (vs gastric perineurioma) | Requires *"targeted immunohistochemical investigations for perineurial markers"* (PMID 41954346) |
| Cavernous haemangioma (vs orbital perineurioma) | PMID 42578239 |
| Cellular neurothekeoma | Can form hybrid lesions (PMID 41547237) |
| Meningioma | Shares TRAF7 WD40 hotspots and perineurial markers — the *"unexpected shared pathogenesis"* (PMIDs 28019650, 23348505, 16324194) |

### 10.7 Screening

- **No newborn screening, carrier screening, or population screening exists or is indicated.** Perineurioma is a sporadic somatic tumour with no germline carrier state.
- **Cascade screening: not applicable.**
- **Incidental screening detection does occur** in one setting: **80.24%** of 148 GI perineuriomas/benign fibroblastic polyps were *"asymptomatic/screening-detected"* during routine colonoscopy (PMID 40225020) — i.e., colorectal cancer screening is the de facto detection route for the GI form.
- **Case-finding, not screening, is the real opportunity for INP**: the median 34.5-month diagnostic delay (PMID 41657107) and the "almost-invisible" problem (PMID 26323815) mean the practical intervention is raising clinician awareness so that a young patient with painless progressive focal weakness receives high-resolution nerve imaging early.

---

## 11. Outcome / Prognosis

### 11.1 Survival and mortality

- **Benign perineurioma (intraneural and soft-tissue) is not a cause of death.** No disease-specific mortality was reported in any retrieved series. ICD-O behaviour code 9571/0 (benign). No 5-year or 10-year survival statistics exist because the question does not arise.
- **Life expectancy is not reduced** on available evidence (no series reported a death from benign perineurioma).
- **Malignant perineurioma / perineurial MPNST is the exception** — yet even here outcomes were comparatively favourable. In 7 cases followed a mean of **66.9 months**: 4 recurred, 2 metastasised, and *"no deaths of disease"* were documented; the authors concluded perineurial MPNST appear *"more favorable"* than conventional MPNST (PMID 9808129). Counterexample: for the related **TRAF7-mutated fibromyxoid spindle cell tumour**, *"2 patients died of disease following aggressive chemotherapeutic regimens"* on 5–36-month follow-up (PMID 36395468) — but these are **not** perineuriomas.
- *No CDC WONDER, WHO, GBD or national mortality data for perineurioma was retrievable (and none would be expected for a benign ICD-O 9571/0 lesion).*

### 11.2 Recurrence and local control

| Setting | Recurrence | Source |
|---|---|---|
| **Soft-tissue perineurioma, 81 cases, mean follow-up 41 months** | **2 recurrences, 0 metastases** — *"soft tissue perineuriomas behave in a benign fashion and rarely recur"* | PMID 15958848 |
| **Intraneural perineurioma after resection, 172 pooled cases** | *"No lesion recurred after surgical resection"* | PMID 34284162 |
| **Sclerosing perineurioma, 19 cases, mean follow-up 12 years 7 months** | **No recurrences** after local excision | PMID 9414186 |
| **Pseudolipoblastic variant, follow-up 5–52 months** | No recurrence or metastasis; *"benign tumors respond well to simple excision"* | PMID 27395366 |
| **Hybrid schwannoma/perineurioma, 42 cases** | *"rarely recurred after complete excision"* | PMID 19623031 |
| **Oral cavity, 1 case** | No recurrence at 1 year | PMID 41010284 |
| **Calvarial perineurioma-like lesions, 8 cases, median 15.5 months** | Progressive growth preoperatively, **no recurrence after surgical removal** | PMID 42216621 |
| **GI perineurioma** | No direct recurrence evidence; review notes *"follow-up endoscopy might be considered to assess for recurrence"* | PMID 40225020 |
| **Perineurial MPNST, 7 cases** | **4/7 recurred, 2/7 metastasised** | PMID 9808129 |

### 11.3 Morbidity and function — where the real burden lies

The prognostic paradox of intraneural perineurioma: **excellent oncological outcome, often poor functional outcome.**

- PERISCOPE: every patient had at least one muscle group at **MRC ≤2**; **7/10 underwent tendon transfer** for functional restoration with *"heterogeneous"* results. Conclusion: *"despite an indolent imaging appearance, INP frequently causes severe functional impairment requiring reconstructive surgery"* (PMID 41657107).
- Conversely, in a neurology natural-history cohort of 32 patients over median 36 months, disability change was **minimal** and the course *"static or slowly progressive"* (PMID 19567701).
- Lenartowicz: among the 52.9% managed conservatively, **67.7% were neurologically stable** (PMID 34284162).
- Brand: motor deficits were universal (30/30), and 21/30 (70%) had postoperative MRI within 5 years showing **no progression** (PMID 34030186).
- Radiological growth **does not predict** clinical deterioration (PMID 30481319).

**Disability outcomes:** focal weakness, muscle atrophy, foot drop or hand/forearm weakness in a single nerve territory, with gait or grip impairment. *No ICF-coded disability data or disability-registry data for perineurioma was retrievable.*

**Quality of life measures: none reported** (see §3.5).

### 11.4 Complications

- Chronic denervation → fixed muscle atrophy and poor response to reconstruction (PMID 41657107)
- Iatrogenic deficit from inappropriate resection — the reason Brand et al. state that *"complete resection is inadvisable for preserving nerve function"* (PMID 34030186) and why *"decompression and neurolysis"* is preferred over resection in many series (PMID 32054523). Note that targeted fascicular biopsy itself was safe in 9/9 PERISCOPE patients
- GI form: intussusception (PMID 42351541), GI bleeding from an ulcerated lesion (PMID 42112490), obstruction-type symptoms (PMID 42677309)
- Orbital form: proptosis (PMID 42578239), misdiagnosis as dacryocystocele with delayed treatment (PMID 39028107)
- Diagnostic misadventure: misdiagnosis as liposarcoma (PMID 27395366), as inflammatory neuropathy or ALS (PMID 41822653), as high-grade sarcoma — leading to overtreatment, which the literature repeatedly warns against (PMIDs 17425397, 34074156, 41010284)

### 11.5 Recovery potential

- **Recovery of the neurological deficit is limited and unpredictable.** From the pooled treatment data (PMID 32054523): complete resection + graft improved 35.7%, left 46.4% unchanged, worsened 17.9%; biopsy alone improved 18.8%, unchanged 53.1%, worsened 28.1%; neurolysis improved 41.6%, unchanged 41.6%, worsened 16.8%. **Fascicular biopsy + neurolysis improved 5/5 (100%)** — a striking but very small-n result.
- **Local tumour control after excision is essentially complete** (see §11.2).

### 11.6 Prognostic factors

Retrieved evidence supports these as prognostically relevant, though none has been formally modelled:

- **Duration of deficit before intervention** — the key modifiable factor; chronic denervation underlies poor reconstruction outcomes (PMID 41657107)
- **Severity of deficit at presentation** (MRC grade)
- **Treatment choice** (decompression/neurolysis vs resection; PMIDs 32054523, 19567701, 34030186)
- **Nerve involved and lesion length** (>10 cm in 40% of PERISCOPE cases)
- **Histological subtype** — benign vs malignant perineurioma is the dominant prognostic split (PMID 9808129)
- **Prognostic molecular biomarkers: none established.** There is **no evidence that TRAF7 vs NF2 genotype affects prognosis** in perineurioma. (For context, TRAF7 altered expression correlates with poorer prognosis in hepatocellular, breast and prostate cancer — *"Additionally, TRAF7 altered expression is associated with poorer prognoses in hepatocellular carcinoma, breast cancer, and prostate cancer"* (PMID 41372821) — but **this does not transfer to perineurioma**.)
- *No prognostic model, clinical calculator or FDA-listed prognostic biomarker for perineurioma was retrievable.*

---

## 12. Treatment

### 12.1 Overall strategy — treatment algorithm

The retrieved literature supports a **risk-adapted, function-first, oncologically conservative** algorithm for intraneural perineurioma:

1. **Recognise early.** Young patient (≤40 y) with painless, progressive, motor-predominant focal mononeuropathy → high-resolution 3-T MRI with gadolinium (± high-frequency ultrasound) (PMIDs 26323815, 40302315).
2. **Apply the 8 Perineurioma Diagnostic Criteria.** If all eight are met, **tissue diagnosis is unnecessary** (specificity 1.0, PPV 1.0) (PMID 29192862).
3. **If criteria are not met, perform targeted fascicular biopsy** of the enlarged fascicle (safe: no postoperative worsening in 9/9, PMID 41657107) — *"biopsy of enlarged fascicles is essential for diagnosis"* (PMID 34030186).
4. **Default to observation + rehabilitation.** *"Probably should not be resected routinely"* (PMID 19567701). Majority (52.9%) are managed conservatively, with 67.7% remaining stable (PMID 34284162). PERISCOPE managed 3 patients conservatively with physiotherapy over 34–85 months, *"clinically stable."*
5. **Consider decompression / external neurolysis** for symptomatic compression — *"decompression and neurolysis may improve neurological deficits"* (PMID 32054523).
6. **Reserve resection + nerve graft** for selected cases; *"complete resection is inadvisable for preserving nerve function"* in general (PMID 34030186).
7. **Offer reconstructive tendon transfer** for established, fixed functional deficit — the mainstay of functional restoration in severely affected patients (7/10 in PERISCOPE), with *"heterogeneous"* outcomes.
8. **For soft-tissue / GI / cutaneous perineurioma: simple complete excision** is definitive — *"complete excision is deemed adequate management"* (PMID 34074156); *"benign tumors respond well to simple excision"* (PMID 27395366); endoscopic cold snare polypectomy for colorectal lesions (PMID 40225020).

### 12.2 Pharmacotherapy

**There is no pharmacological treatment for perineurioma.** No drug, drug class or targeted agent has been reported as a treatment in any retrieved source. No DrugBank/RxNorm/ATC/DailyMed/FDA entry for perineurioma therapy was found.

**Pharmacogenomics: not applicable** — no PharmGKB or CPIC guideline exists for perineurioma, since no drug therapy exists.

### 12.3 Advanced therapeutics

| Modality | Status in perineurioma |
|---|---|
| **Targeted therapy** | **None in clinical use.** The only forward-looking statement retrieved: TRAF7 point mutations and rare NF2 mutations *"may present targets for diagnosis or therapy in the future"* (PMID 37684428). A TRAF7 review calls for work to *"potentially identify novel therapeutic targets to expand our treatment options"* (PMID 41372821). **These are aspirations, not therapies.** If NF-κB activation is confirmed downstream of mutant TRAF7, NF-κB-pathway inhibition would be the rational candidate — **this is my inference, not a retrieved claim** |
| **Gene therapy** | None reported; no clinical trial |
| **Cell therapy** | None reported |
| **RNA-based therapy (ASO, siRNA, mRNA)** | None reported |
| **Immunotherapy** | None reported; no immune mechanism identified |
| **Radiotherapy / chemotherapy** | Not indicated for benign perineurioma. Relevant only to malignant perineurioma/perineurial MPNST, managed per MPNST/sarcoma protocols |

### 12.4 Surgical and interventional treatments with outcomes

Pooled outcomes by procedure, from the systematic review of 77 patients (22 articles 1990–2019 plus 3 institutional cases; [Uerschels et al., *BMC Neurol* 2020;20(1):55, PMID 32054523](https://pmc.ncbi.nlm.nih.gov/articles/PMC7017529/)):

| Procedure | Worsened | Unchanged | Improved | NCIT suggestion |
|---|---|---|---|---|
| **Fascicular biopsy + neurolysis** | 0 | 0 | **5 (100%)** | NCIT:C15232 Excision (biopsy term not verified) |
| **Neurolysis (alone)** | 2 (16.8%) | 5 (41.6%) | 5 (41.6%) | — |
| **Complete resection + nerve graft** | 5 (17.9%) | 13 (46.4%) | 10 (35.7%) | — |
| **Biopsy alone** | 9 (28.1%) | 17 (53.1%) | 6 (18.8%) | — |

Mean follow-up 35.2 months; mean age 21.0 ± 13.9 y; 54.5% female.

From Lenartowicz et al. (172 pooled cases, PMID 34284162): **52.9% managed conservatively** (67.7% stable); of 64 surgical cases, **62.5% underwent resection with repair**, and *"No lesion recurred after surgical resection."*

Other documented interventions:
- **Tendon transfer** for functional restoration — 7/10 PERISCOPE patients; outcomes *"heterogeneous"* (PMID 41657107)
- **Tumour resection with sural nerve grafting** — 1/10 PERISCOPE patients; also used in the 4-year-old radial nerve case (PMID 40353166)
- **Gross total resection** for orbital sclerosing perineurioma (PMID 39028107)
- **Laser-assisted biopsy and surgical excision** for oral perineurioma (PMID 41010284)
- **Endoscopic resection / cold snare polypectomy** for colorectal lesions (PMID 40225020)
- **Laparoscopic resection** for ileal hybrid schwannoma/perineurioma (PMID 42112490)

*CPT codes and surgical-registry data for perineurioma were not retrieved.*

### 12.5 Supportive and rehabilitative care

- **Physiotherapy** — explicitly used as the conservative management arm: 3 PERISCOPE patients received *"conservative management with physiotherapy (follow-up: 34–85 months, clinically stable)"* (PMID 41657107). Suggested term: **NCIT:C15302 Physical Therapy**.
- **Structured functional monitoring** — PERISCOPE advocates *"early recognition, structured functional monitoring and risk-adapted intervention."* Suggested term: **NCIT:C15722 Patient Observation**.
- **Occupational therapy, orthotics (e.g. ankle-foot orthosis for foot drop), speech therapy, pain management, nutrition** — **no perineurioma-specific evidence was retrieved**, although orthotic management of foot drop would be standard care. Recorded as an evidence gap, not as a recommendation from the literature.
- *No Cochrane review of perineurioma rehabilitation exists.*

### 12.6 Experimental treatments and clinical trials

A ClinicalTrials.gov API query by condition returned **exactly one study**, and it is not perineurioma-specific:

- **NCT06239272** — "NRSTS2021, A Risk Adapted Study Evaluating Maintenance Pazopanib, Limited Margin, Dose-Escalated Radiation Therapy and Selinexor in Non-Rhabdomyosarcoma Soft Tissue Sarcoma (NRSTS)"; **Recruiting**; covers ~44–47 soft-tissue sarcoma histologies including malignant peripheral nerve sheath tumour; interventions: surgical resection, proton beam radiation therapy, pazopanib, ifosfamide, doxorubicin, selinexor ([ClinicalTrials.gov API v2](https://clinicaltrials.gov/api/v2/studies?query.cond=perineurioma)).

**Conclusion: there is no interventional clinical trial targeting perineurioma.** The single match is a paediatric sarcoma umbrella trial whose eligibility list includes malignant nerve sheath histologies. This should be recorded explicitly — it is a meaningful fact about the state of the field.

### 12.7 Combination and personalised approaches

- **Combination therapy: not applicable** — no systemic agents exist to combine.
- **Personalised/genotype-guided treatment: not available.** Neither TRAF7 nor NF2/NF1 genotype currently alters management. No My Cancer Genome, OncoKB or CIViC actionable entry for perineurioma was retrieved.
- The genuine "personalisation" in current practice is **anatomical and functional**, not molecular: Alkhaili et al. describe a strategy *"emphasiz[ing] functional optimization based on patient age and lesion size"* (PMID 30637060).

### 12.8 NCIT clinical-intervention terms (verified this session)

| Intervention | NCIT ID | Note |
|---|---|---|
| Excision | **NCIT:C15232** | Core treatment for soft-tissue/cutaneous/GI forms |
| Patient Observation | **NCIT:C15722** | Default strategy for intraneural form |
| Physical Therapy | **NCIT:C15302** | Conservative arm |
| Wide Skin Excision | NCIT:C48608 | Possibly relevant to cutaneous lesions |
| Excision of Subcutaneous Tumor of Extremities | NCIT:C219930 | Well matched to soft-tissue perineurioma of the limbs |

Terms retrieved from [OLS4 NCIT](https://www.ebi.ac.uk/ols4/api/search?q=surgical+excision&ontology=ncit&rows=6) and related queries. **NCIT terms for neurolysis, nerve graft, tendon transfer and targeted fascicular biopsy were not verified this session** and should be looked up before annotation.

---

## 13. Prevention

**Summary: perineurioma is not preventable, and no prevention programme exists at any level.** This section is largely a set of justified negatives, which is the correct content for a sporadic somatic neoplasm with no known environmental cause.

### 13.1 Primary prevention

**None available and none plausible.** No modifiable risk factor has been identified (§2.2, §5), so there is no exposure to avoid and nothing to modify. No USPSTF, CDC, WHO or Cochrane recommendation addresses perineurioma.

### 13.2 Secondary prevention (early detection)

This is the **only level at which meaningful prevention of harm is possible** — not prevention of the tumour, but prevention of irreversible functional loss.

- The target is the **median 34.5-month delay** from symptom onset to intervention (PMID 41657107), compounded by the lesion's "almost-invisible" appearance on conventional MRI (PMID 26323815) and *"diagnostic delay due to their uncommon presentation"* (PMID 40353166).
- The mechanism of harm is **chronic denervation**, which is why PERISCOPE calls for *"early recognition, structured functional monitoring and risk-adapted intervention"* (PMID 41657107).
- Practical levers: clinician awareness of the "young patient, painless progressive motor-predominant mononeuropathy" phenotype; early high-resolution 3-T MRI with gadolinium and/or high-frequency ultrasound; application of the Perineurioma Diagnostic Criteria to avoid both diagnostic delay and unnecessary biopsy.
- For the **GI form**, routine colorectal cancer screening colonoscopy already functions as incidental detection (80.24% screening-detected, PMID 40225020) — detection is not the problem there; **avoiding misdiagnosis as GIST** is (PMID 41954346).

### 13.3 Tertiary prevention (preventing complications)

- **Avoid inappropriate radical resection.** The strongest preventive statements in the retrieved literature are about iatrogenic harm: *"complete resection is inadvisable for preserving nerve function"* (PMID 34030186); these tumours *"probably should not be resected routinely"* (PMID 19567701).
- **Avoid overtreatment of benign soft-tissue lesions.** *"Correct identification of perineuriomas is important to avoid unnecessary overtreatment"* (PMID 17425397); *"accurate recognition of EPNs in the oral cavity is crucial to prevent unnecessary aggressive surgical interventions"* (PMID 41010284); *"the importance of accurate histological recognition to prevent unnecessary aggressive treatment"* (PMID 34074156). The pseudolipoblastic variant's misidentification as high-grade liposarcoma (PMID 27395366) and the LGFMS-in-nerve trap (PMID 29314300) are the concrete failure modes in both directions.
- **Preserve and restore function:** physiotherapy, structured monitoring, timely tendon transfer before irreversible atrophy (PMID 41657107).
- **Consider follow-up endoscopy** after GI resection (PMID 40225020).

### 13.4 Immunisation

**Not applicable.** No infectious aetiology; no vaccine.

### 13.5 Genetic screening and counselling

- **Carrier screening, preimplantation genetic diagnosis, prenatal testing: not applicable.** Perineurioma arises from somatic mutation; there is no transmissible risk.
- **Genetic counselling** is appropriate **only** when perineurioma occurs in a patient with features of **NF2-related schwannomatosis** or **NF1**, in which case counselling addresses the underlying dominant syndrome, not the perineurioma (PMIDs 32529330, 32271143, 24393170). Clinicians should note that perineurioma is **not currently part of the NF2 diagnostic tumour spectrum** (PMID 32529330) and so should not by itself trigger an NF2 diagnosis.
- A separate counselling consideration: a **germline** TRAF7 WD40 variant signifies **CAFDADD/TRAF7 syndrome** (MIM 618164) — a developmental disorder with no reported perineurioma risk (PMID 32376980) — and must not be conflated with the somatic tumour hotspots. **This germline/somatic distinction at the same domain is the single most important counselling pitfall for this gene.**
- *No ACMG, ACOG, NSGC or GeneReviews guidance specific to perineurioma was retrievable.*

### 13.6 Risk stratification, behavioural interventions, public health and prophylaxis

- **Risk stratification models: none exist** for perineurioma occurrence. The only risk stratification in practice is *functional* (which patient needs reconstruction, and when).
- **Behavioural / lifestyle interventions: none** — no modifiable behavioural risk factor exists.
- **Public health and environmental interventions: not applicable** — no environmental cause, no vector, no transmission.
- **Prophylactic medication or procedure: none.**

---

## 14. Other Species / Natural Disease

### 14.1 Taxonomy (NCBI Taxon IDs verified this session)

| Species | NCBI Taxon ID | Relevance |
|---|---|---|
| *Homo sapiens* | **9606** | The disease species |
| *Canis lupus familiaris* (dog) | **9615** | Naturally occurring perineurial-differentiated nerve sheath tumours |
| *Mus musculus* (mouse) | **10090** | Traf7 and Dhh/Nkx2.2 perineurial biology models |
| *Danio rerio* (zebrafish) | **7955** | Perineurial glia development/injury models |

Retrieved from [NCBI Taxonomy esearch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=taxonomy&term=Canis+lupus+familiaris+OR+Homo+sapiens+OR+Mus+musculus+OR+Danio+rerio).

### 14.2 Orthologous genes

| Species | Gene | NCBI Gene ID | Notes |
|---|---|---|---|
| Human | **TRAF7** | 84231 | HGNC:20456; 16p13.3 |
| Mouse | **Traf7** | **224619** | "TNF receptor-associated factor 7"; **chromosome 17, 12.4 cM** |
| Dog | **TRAF7** | **609824** | Single *Canis lupus familiaris* entry |
| Human | **NF2** | 4771 | HGNC:7773; 22q12.2 |

Verified via [NCBI Gene esearch/esummary](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=gene&id=224619&retmode=json). *Mouse Nf2, Nf1 and zebrafish traf7 orthologue IDs were not retrieved this session.*

### 14.3 Natural disease in other species

**Dog (*Canis lupus familiaris*, NCBI Taxon 9615) — the only species with retrieved natural-disease evidence.**

Tekavec et al. examined **79 canine nerve sheath tumours** and proposed an updated classification aligned to the human scheme ([*Vet Sci* 2022;9(5):204, PMID 35622732](https://pmc.ncbi.nlm.nih.gov/articles/PMC9144584/)):

- **12 benign (15.2%)**: 6 neurofibromas, 1 schwannoma, **2 hybrid tumours**, 3 nerve sheath myxomas
- **67 malignant (84.8%)**: 56 conventional, 6 with divergent differentiation, **4 perineurial**, 1 epithelioid
- **Perineurioma-relevant findings:** the 2 hybrid tumours were a *"perineurioma/neurofibroma and perineurioma/schwannoma"*; and **4 malignant tumours showed perineurial differentiation**, *"strongly immunoreactive for claudin-1 and negative for Sox10 and GFAP"*
- IHC panel: SOX10, claudin-1, GFAP, CNPase, Ki-67 (EMA and GLUT1 were **not** used in this study)
- The authors recommend adopting the human classification for canine tumours

**Breed distribution** (of the 79 canine NSTs overall, not perineurioma specifically): predominantly **mixed-breed (36.7%)**, then **German Shepherd (11.4%)** and **Labrador Retriever (10.1%)**. *No Vertebrate Breed Ontology (VBO) identifiers were retrieved; no breed predisposition for perineurial-differentiated tumours specifically can be claimed from these numbers.*

**OMIA: no entry.** A search of the Online Mendelian Inheritance in Animals database for perineurioma/nerve sheath tumour returned **no matching phene** ([OMIA search](https://www.omia.org/results?search_type=advanced&search_term=perineurioma)) — consistent with perineurioma being a somatic tumour rather than an inherited animal trait. *No VetCompass data was retrieved.*

**Veterinary relevance:** modest. Canine nerve sheath tumours are overwhelmingly malignant (84.8% in this series), and pure benign perineurioma was **not** reported — only hybrid lesions and perineurial differentiation within malignant tumours. **A naturally occurring canine homologue of human benign perineurioma has not been established.**

**Other species: no natural perineurioma reported** in any retrieved source (no cat, horse, bovine, or wildlife cases).

### 14.4 Comparative biology

- **Comparative pathology:** the perineurial immunophenotype is conserved across human and dog (claudin-1⁺, SOX10⁻) (PMID 35622732 vs PMIDs 12459629, 12692193), supporting cross-species marker transferability. However, the **benign/malignant ratio is inverted** between species as sampled (human perineurioma is predominantly benign; canine perineurial-differentiated tumours in this series were predominantly malignant) — an important caveat for using dogs as a comparative model.
- **Evolutionary conservation of mechanism:** TRAF7 is conserved from human to mouse to dog (orthologues above), and the perineurium itself is a conserved vertebrate structure whose development depends on conserved Schwann-cell-derived hedgehog signalling (§15). *No HomoloGene/OrthoMCL/Alliance of Genome Resources ortholog-set identifiers were retrieved this session.*
- **No cross-species study of TRAF7 mutation in animal nerve sheath tumours exists** — i.e., we do not know whether canine perineurial tumours share the human driver.

### 14.5 Transmission

- **Zoonotic potential: none.** Perineurioma is a non-transmissible neoplasm.
- **Cross-species susceptibility: not applicable** in an infectious sense; the shared susceptibility is developmental (all vertebrates with a perineurium possess the cell of origin).

---

## 15. Model Organisms

### 15.1 Overall status — the central finding

**No animal or cellular model of perineurioma exists.** No retrieved source describes a mouse, rat, zebrafish, fly, worm, organoid, iPSC or immortalised cell line that develops or recapitulates perineurioma, and no DepMap perineurioma model line was identified. **This is the single largest gap in the field and directly explains why the mechanism remains partly inferred** (§6.1, step 4).

What *does* exist are two separable categories of adjacent model: (a) models of **normal perineurial-cell development**, which establish the biology of the cell of origin, and (b) models of **Traf7 loss**, which characterise the gene but produce no nerve tumour.

### 15.2 Models of perineurial cell development (cell-of-origin biology)

| Model | Type | Finding | Relevance |
|---|---|---|---|
| ***Dhh* (desert hedgehog) knockout mouse** | Mammalian, germline KO | Desert hedgehog, expressed in Schwann cell precursors, signals via Patched on surrounding mesenchyme. Dhh-null mice have *"almost no epineurium, and the perineurium is thin and highly abnormal."* Schwann-cell-to-mesenchyme signalling establishes proper perineurial structure and the diffusion barrier *"that protects nerves from unwanted molecular and cellular infiltration"* ([Mirsky et al., *Ann N Y Acad Sci* 1999;883:196–202, PMID 10586245](https://pubmed.ncbi.nlm.nih.gov/10586245/)) | **The foundational model for how the perineurium forms.** Establishes that perineurial identity is *induced* by Schwann cells — raising the untested question of whether Schwann-cell signalling modulates perineurioma growth |
| ***Nkx2.2* knockout mouse + Nkx2.2:EGFP reporter** | Mammalian, transgenic reporter + KO | *"Created a Nkx2.2:EGFP transgenic reporter line"*; Nkx2.2⁺ cells line peripheral motor nerves throughout development and in adults, **originate from the CNS**, and *"Nkx2.2(+) perineurial glia are essential for motor nerve development and Schwann cell differentiation"* ([Clark et al., *Dev Dyn* 2014;243(9):1116–1129, PMID 24979729](https://pubmed.ncbi.nlm.nih.gov/24979729/)) | **Directly relevant to the motor-predominance puzzle:** perineurial glia are specifically required for *motor* nerve development. If perineurial cells have a privileged relationship with motor axons, that could explain why INP produces motor-predominant deficits — **an explicit, testable hypothesis this report flags as unexplored** |
| **Zebrafish (*Danio rerio*) perineurial glia** | Non-mammalian vertebrate, in vivo imaging | β-cell-ablation hyperglycaemia model showed *"defasciculated"* motor axons, reduced myelination, and *"disrupted"* tight junctions along motor nerves, with *"structural changes occurr[ing] in the absence of behavioral changes"* ([Rocker et al., *Am J Physiol Regul Integr Comp Physiol* 2019;316(4):R395–R405, PMID 30726116](https://pubmed.ncbi.nlm.nih.gov/30726116/)) | Not a perineurioma model, but demonstrates **tractable live imaging of perineurial tight-junction integrity in a transparent vertebrate** — the obvious platform on which a *traf7*-mutant perineurial model could be built |

### 15.3 Genetic models of the causal gene (Traf7)

**IMPC *Traf7*^em1(IMPC)Tcp** (C57BL/6NCrl background, phenotyped by TCP) — **11 genotype–phenotype associations** retrieved from the [IMPC genotype-phenotype API](https://www.ebi.ac.uk/mi/impc/solr/genotype-phenotype/select?q=marker_symbol:Traf7):

| Genotype | Phenotype | MP term | p-value |
|---|---|---|---|
| Homozygous | Embryonic lethality prior to tooth bud stage | MP:0013293 | 0.0 |
| Homozygous | Prenatal lethality prior to heart atrial septation | MP:0013294 | 0.0 |
| Homozygous | Preweaning lethality, complete penetrance | MP:0011100 | 0.0 |
| Heterozygous | Cataract | MP:0001304 | 2.93×10⁻⁹ |
| Heterozygous | Abnormal lens morphology | MP:0001303 | 3.06×10⁻⁵ |
| Heterozygous | Abnormal retina morphology | MP:0001325 | 1.08×10⁻⁵ |

**Interpretation and limitations.** *Traf7* homozygous null is **embryonic lethal**, which means a conventional constitutive knockout **cannot be used to model perineurioma**. Heterozygotes develop ocular, not neural or neoplastic, phenotypes — **no nerve sheath tumour phenotype is reported.** Two implications follow:

1. Perineurioma requires a **conditional, perineurial-cell-restricted, mutation-specific (knock-in) allele** — e.g. a Cre-driver active in perineurial cells (Nkx2.2 and Dhh-responsive lineages suggest candidate drivers) crossed to a *Traf7*^L519P or *Traf7*^H521R knock-in. **No such allele was retrieved.** This is the clearest, most actionable experimental recommendation that follows from the retrieved evidence.
2. Because the human variants are **missense hotspots, not nulls**, a knockout is the wrong genetic model regardless of lethality — consistent with the unresolved LOF/GOF question in §6.2.

*MGI accession for mouse Traf7 could not be retrieved (the MGI quick-search page did not return data); NCBI Gene 224619 is the verified mouse identifier. No RGD (rat), ZFIN, FlyBase, WormBase, SGD, ATCC, Cellosaurus, IMSR, EMMA, MMRRC or KOMP perineurioma-relevant entry was retrieved.*

### 15.4 Models of related TRAF7-driven neoplasms

Not models of perineurioma, but the closest functional systems available:

- **Mutant-TRAF7 overexpression in mesothelial cells** (adenomatoid tumour study): *"Functional analysis demonstrated that mutant TRAF7 expression increased NF-kB phosphorylation and L1CAM expression"* (PMID 29148537). **This in vitro system is the only direct functional evidence for the downstream consequence of a WD40 hotspot mutation, and it is in the wrong cell type** — which is precisely why step 4 of the causal chain in §6.1 is marked as inferred.
- **Germline TRAF7 patient fibroblasts**: *"Transcriptome studies of patient fibroblasts revealed altered gene expression profiles"* (PMID 32376980) — a human cellular system, but for the germline developmental disorder, not the tumour.
- **Dab1^−/− (yotari) mouse**: Traf7 protein expression peaked at E13.5 and declined postnatally; linked Reelin–Dab1 signalling to TRAF7 and suggested TRAF7 *"may play a critical role in disease mechanisms"* of congenital kidney/urinary anomalies ([Komić et al., *Int J Mol Sci* 2025;26(13):6421, PMID 40650197](https://pubmed.ncbi.nlm.nih.gov/40650197/)). **Developmental expression data only; no neoplasia and no perineurial relevance.**

### 15.5 Induced and in vitro models

**None reported.** No drug-induced, surgically induced or environmentally induced perineurioma model exists — unsurprising given that no environmental cause of the human disease is known (§5). No organoid or iPSC-derived perineurial model was retrieved.

### 15.6 Research applications and recommended model development

Given what the models can and cannot do:

| Question | Tractable with existing models? |
|---|---|
| How does the perineurium form, and from which lineage? | **Yes** — Dhh KO mouse, Nkx2.2:EGFP reporter mouse, zebrafish |
| Is Traf7 essential for development? | **Yes** — IMPC: homozygous embryonic lethal |
| Do WD40 hotspot mutants activate NF-κB in *perineurial* cells? | **No** — requires a new cell-type-appropriate system. **This is the critical missing experiment** |
| Why is the deficit motor-predominant? | **Not yet** — but Nkx2.2⁺ perineurial glia being *"essential for motor nerve development"* (PMID 24979729) makes this a well-posed hypothesis |
| Does a mutant clone produce pseudo-onion bulbs *in vivo*? | **No model exists** |
| Can the growth be pharmacologically arrested? | **No model exists**; no trial exists (§12.6) |

---

## Consolidated ontology annotation summary

All terms below were retrieved and verified in this session.

**Disease:** MONDO:0019404 (perineurioma); NCIT:C4973; DOID:4697; UMLS C0751691; SNOMED CT 404036006; ICD-O 9571/0; ICD-9 215.9; MedGen 199712; GARD 0012698; ORPHA:85102 (MONDO-asserted, unverified); ICD-11 foundation 456459236 (unverified stem code); **no OMIM entry**
**Subtypes (NCIT):** C6911, C6912, C172621, C188997, C207064, C207065, C207066, C207081, C207082
**Genes:** TRAF7 HGNC:20456 / NCBI 84231 / UniProt Q6Q0C0 / OMIM 606692 / 16p13.3; NF2 HGNC:7773 / NCBI 4771 / UniProt P35240 / OMIM 607379 / 22q12.2; mouse Traf7 NCBI 224619 (Chr 17, 12.4 cM); dog TRAF7 NCBI 609824
**Phenotypes (HPO):** HP:0009831 Mononeuropathy; HP:0032018 Multiple mononeuropathy; HP:0009027 Foot dorsiflexor weakness; HP:0003202 Skeletal muscle atrophy; HP:0003401 Paresthesia; HP:0033660 Hand paresthesia; HP:0003382 Hypertrophic nerve changes; HP:0003383 Onion bulb formation; HP:0003400 Basal lamina onion bulb formation; HP:0003447 Axonal loss; HP:0100697 Malignant peripheral nerve sheath tumor (for perineurial MPNST); HP:0100008 Schwannoma and HP:0001067 Neurofibroma (structural analogues only). **No HPO term for perineurioma or pseudo-onion bulb formation exists — both are warranted new-term requests.**
**Cell type (CL):** CL:0002576 perineurial cell
**Anatomy (UBERON):** UBERON:0000121 perineurium; UBERON:0000123 endoneurium; UBERON:0000124 epineurium; UBERON:0006134 nerve fibre; UBERON:0001322 sciatic nerve; UBERON:0001324 common fibular nerve; UBERON:0001323 tibial nerve; UBERON:0035207 deep fibular nerve; UBERON:0035526 superficial fibular nerve; UBERON:0001148 median nerve; UBERON:0001814 brachial nerve plexus
**Biological process (GO):** GO:0007249 canonical NF-κB signal transduction; GO:0043122 regulation of canonical NF-κB signal transduction; GO:0043123 positive regulation of canonical NF-κB signal transduction; GO:0038061 non-canonical NF-κB signal transduction
**Interventions (NCIT):** C15232 Excision; C15722 Patient Observation; C15302 Physical Therapy; C48608 Wide Skin Excision; C219930 Excision of Subcutaneous Tumor of Extremities
**Taxa (NCBI):** 9606 human; 9615 dog; 10090 mouse; 7955 zebrafish
**Mouse phenotypes (MP, IMPC Traf7):** MP:0013293; MP:0013294; MP:0011100; MP:0001303; MP:0001304; MP:0001325
**Clinical trial:** NCT06239272 (the only ClinicalTrials.gov match; not perineurioma-specific)

---

## Explicit statement of what could not be retrieved

In the interest of not letting absence read as silence, these items were searched for and **not** obtained in this session, and should not be filled in from memory:

1. **Population-based incidence or prevalence** for perineurioma (Orphanet, SEER, GBD, WHO, CDC, national registries). Orphanet's own page for ORPHA:85102 was unreachable (anti-bot protection), so the MONDO-asserted Orphanet xref and any Orphanet prevalence class remain unverified.
2. **gnomAD constraint metrics for TRAF7** (pLI, LOEUF, missense/LoF o/e) — gnomAD's JavaScript browser returned no data.
3. **ClinVar records** for the TRAF7 perineurioma hotspots; **COSMIC** somatic frequencies.
4. **Verified cDNA/HGVS coordinates** against a declared reference transcript — the retrieved coordinates are internally inconsistent (§4.2) and must be checked against source PDFs.
5. **ICD-11 stem code** (only the MONDO-asserted foundation ID 456459236 was obtained).
6. **Any methylation, transcriptomic, proteomic, metabolomic, lipidomic, single-cell or spatial dataset** for perineurioma; **no GEO/ArrayExpress/PRIDE/MetaboLights/DepMap entry**; no KEGG/Reactome/WikiPathways perineurioma map.
7. **Any validated quality-of-life measurement** (EQ-5D, SF-36, PROMIS or disease-specific) in any perineurioma cohort.
8. **Any perineurioma-specific electrodiagnostic (EMG/NCS) signature study.**
9. **LOINC/SNOMED CT codes** for the specific IHC assays; **CPT codes**; **RadLex** imaging descriptors (Radiopaedia returned HTTP 402).
10. **MGI accession ID** for mouse Traf7; HGNC IDs for NF1, BRAF, VGLL3; GO Cellular Component IDs; CL terms for Schwann cell and pericryptic fibroblast; UBERON IDs for radial/ulnar nerve and lumbosacral plexus; VBO breed identifiers.
11. **Any animal or cellular model of perineurioma** — this one appears not to exist, rather than merely to have eluded retrieval (§15.1).

**Sources:**
- [EBI OLS4 — MONDO:0019404](https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMONDO_0019404) · [OLS4 NCIT perineurioma terms](https://www.ebi.ac.uk/ols4/api/search?q=perineurioma&ontology=ncit&rows=10) · [OLS4 CL perineurial cell](https://www.ebi.ac.uk/ols4/api/search?q=perineurial%20cell&ontology=cl&rows=10) · [OLS4 UBERON nerve sheath layers](https://www.ebi.ac.uk/ols4/api/search?q=epineurium&ontology=uberon&rows=5) · [OLS4 GO NF-κB](https://www.ebi.ac.uk/ols4/api/search?q=I-kappaB+kinase+NF-kappaB+signaling&ontology=go&rows=8)
- [HGNC TRAF7](https://rest.genenames.org/fetch/symbol/TRAF7) · [HGNC NF2](https://rest.genenames.org/fetch/symbol/NF2) · [UniProt Q6Q0C0](https://rest.uniprot.org/uniprotkb/Q6Q0C0.txt) · [NCBI Gene 224619](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=gene&id=224619&retmode=json) · [IMPC Traf7 genotype-phenotype](https://www.ebi.ac.uk/mi/impc/solr/genotype-phenotype/select?q=marker_symbol:Traf7) · [OMIA search](https://www.omia.org/results?search_type=advanced&search_term=perineurioma) · [ClinicalTrials.gov API](https://clinicaltrials.gov/api/v2/studies?query.cond=perineurioma)
- Key primary literature: [Klein 2017 PMID 28019650](https://pmc.ncbi.nlm.nih.gov/articles/PMC5725965/) · [Carter 2018 PMID 30303818](https://pubmed.ncbi.nlm.nih.gov/30303818/) · [PERISCOPE 2026 PMID 41657107](https://pmc.ncbi.nlm.nih.gov/articles/PMC12884198/) · [Lasota 2001 PMID 11290539](https://pubmed.ncbi.nlm.nih.gov/11290539/) · [Giannini 1997 PMID 9042282](https://pubmed.ncbi.nlm.nih.gov/9042282/) · [Hornick & Fletcher 2005 PMID 15958848](https://pubmed.ncbi.nlm.nih.gov/15958848/) · [Mauermann 2009 PMID 19567701](https://pubmed.ncbi.nlm.nih.gov/19567701/) · [Lenartowicz 2021 PMID 34284162](https://pubmed.ncbi.nlm.nih.gov/34284162/) · [Uerschels 2020 PMID 32054523](https://pmc.ncbi.nlm.nih.gov/articles/PMC7017529/) · [Wilson 2018 PMID 29192862](https://thejns.org/view/journals/j-neurosurg/129/4/article-p1034.xml) · [Wilson 2019 PMID 30481319](https://pubmed.ncbi.nlm.nih.gov/30481319/) · [Prasad 2017 PMID 28173435](https://pubmed.ncbi.nlm.nih.gov/28173435/) · [Folpe 2002 PMID 12459629](https://pubmed.ncbi.nlm.nih.gov/12459629/) · [Hirose 2003 PMID 12692193](https://pubmed.ncbi.nlm.nih.gov/12692193/) · [Hirose 1998 PMID 9808129](https://pubmed.ncbi.nlm.nih.gov/9808129/) · [Fetsch & Miettinen 1997 PMID 9414186](https://pubmed.ncbi.nlm.nih.gov/9414186/) · [Agaimy 2010 PMID 20962618](https://pubmed.ncbi.nlm.nih.gov/20962618/) · [Dickson 2021 PMID 33649458](https://pubmed.ncbi.nlm.nih.gov/33649458/) · [Goode 2018 PMID 29148537](https://pubmed.ncbi.nlm.nih.gov/29148537/) · [Clark 2013 PMID 23348505](https://pubmed.ncbi.nlm.nih.gov/23348505/) · [Alenezi 2025 PMID 40225020](https://pmc.ncbi.nlm.nih.gov/articles/PMC11991822/) · [Tekavec 2022 PMID 35622732](https://pmc.ncbi.nlm.nih.gov/articles/PMC9144584/) · [Mirsky 1999 PMID 10586245](https://pubmed.ncbi.nlm.nih.gov/10586245/) · [Clark 2014 PMID 24979729](https://pubmed.ncbi.nlm.nih.gov/24979729/)
- Reference/overview pages: [Pathology Outlines WHO classification](https://www.pathologyoutlines.com/topic/softtissuewhoclassification.html) · [NORD MONDO: intraneural perineurioma](https://rarediseases.org/mondo-disease/intraneural-perineurioma/) · [NORD MONDO: extraneural perineurioma](https://rarediseases.org/mondo-disease/extraneural-perineurioma/)

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 81 |
| Resolved | 81 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 4 |
| Quoted claims found in source | 3 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 81 |
| On topic | 54 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:29148537` *(abstract only)*: "mutant TRAF7 expression increased NF-kB phosphorylation and L1CAM expression"
  - closest text in source: "Functional studies in vitro revealed that expression of mutant but not wild-type TRAF7 led to increased phosphorylation of nuclear factor-kappa B (NF-kB) and increased expression of L1 cell adhesion molecule (L1CAM), a marker of NF-kB pathway activation"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 56 |
| Resolved | 53 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 34 |
| Terms named correctly | 25 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `DOID:4697` (2 mentions) - the report calls it "DOID"; DOID calls it **perineurioma**
- `NCIT:C207066` (2 mentions) - the report calls it "Malignant Perineurioma", "high mitotic activity, hypercellularity, hyperchromasia, and pleomorphism", "Malignant:** *"high mitotic activity, hypercellularity, hyperchromasia, and pleomorphism"; NCIT calls it **Malignant Perineurioma**
- `UBERON:0000123` (2 mentions) - the report calls it "Endoneurium** (where INP proliferates)"; UBERON calls it **endoneurium**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0019404` (10 mentions) - the report calls it "label "Perineurioma", "perineurioma"; MONDO calls it **perineurioma**
- `NCIT:C6911` (3 mentions) - the report calls it "Intraneural Perineurioma", "WHO grade I"; NCIT calls it **Intraneural Perineurioma**, and lists "Intraneural Perineurioma (WHO Grade I)" among its other names
- `CL:0002576` (3 mentions) - the report calls it "Target cell population: perineurial cell"; CL calls it **perineurial cell**
- `UBERON:0006134` (2 mentions) - the report calls it "Nerve fibre** (compressed element)"; UBERON calls it **nerve fiber**, and lists "nerve fibre" among its other names
- `UBERON:0001322` (2 mentions) - the report calls it "Sciatic nerve** (most frequent INP site)"; UBERON calls it **sciatic nerve**
- `UBERON:0001324` (2 mentions) - the report calls it "Common fibular (peroneal) nerve"; UBERON calls it **common fibular nerve**, and lists "common peroneal nerve" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0019404` - called "label "Perineurioma", "perineurioma"
- `ORPHA:85102` - called "MONDO-asserted xref; **not independently verified** — Orphanet pages were not retrievable this session", "MONDO-asserted, unverified"
- `NCIT:C6911` - called "Intraneural Perineurioma", "WHO grade I"
- `NCIT:C207066` - called "Malignant Perineurioma", "high mitotic activity, hypercellularity, hyperchromasia, and pleomorphism", "Malignant:** *"high mitotic activity, hypercellularity, hyperchromasia, and pleomorphism"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.