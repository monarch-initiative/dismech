---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-10-21T14:47:08.091474'
end_time: '2026-10-21T15:08:14.581940'
duration_seconds: 1266.49
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Ganglioneuroblastoma
  mondo_id: MONDO:0005035
  category: ''
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
  web_search_requests: 19
  num_turns: 76
  total_cost_usd: 10.707445500000004
  session_id: 7f8c8a3a-29e4-49ed-a95d-f5d2bd99cc58
  stop_reason: end_turn
  permission_denials: 1
  denied_tools:
  - Bash
  assistant_text_blocks: 2
citation_count: 79
reference_validation:
  total_references: 151
  verified: 148
  not_found: 0
  unverifiable: 3
  confabulation_rate: 0.0
  quotes_checked: 31
  quotes_valid: 24
  quotes_unsupported: 7
  unsupported_quote_references:
  - PMID:9788610
  - PMID:15488758
  - PMID:38774105
  - PMID:40065424
  - PMID:38154064
  - PMID:38039964
  - PMID:28674118
  relevance_assessed: 148
  on_topic: 30
  off_topic: 2
  off_topic_references:
  - PMID:40065424
  - DOI:10.1186/s12957-023-02967-1
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 93
  verified: 88
  not_found: 0
  obsolete: 1
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 27
  labels_matching: 14
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: NCIT:C3790
    reported_labels:
    - NCI Thesaurus
    ontology_label: Ganglioneuroblastoma
  - term_id: DOID:4163
    reported_labels:
    - Disease Ontology
    ontology_label: ganglioneuroblastoma
  - term_id: EFO:0000502
    reported_labels:
    - EFO
    ontology_label: obsolete_ganglioneuroblastoma
  - term_id: NCIT:C124274
    reported_labels:
    - childhood
    ontology_label: Childhood Ganglioneuroblastoma, Nodular
  labels_variant: 9
  obsolete_terms:
  - term_id: EFO:0000502
    ontology_label: obsolete_ganglioneuroblastoma
    replaced_by: http://purl.obolibrary.org/obo/MONDO:0005035
  unresolvable_prefixes:
  - ORPHA
  - GARD
  - NANDO
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Ganglioneuroblastoma
- **MONDO ID:** MONDO:0005035 (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Ganglioneuroblastoma** covering all of the
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

I'll research this comprehensively now.

# Ganglioneuroblastoma (MONDO:0005035) — Comprehensive Disease Characteristics Research Report

**Prepared:** 21 October 2026
**Scope:** Literature and ontology survey for knowledge-base population
**Evidence-scope caveat (read first):** Ganglioneuroblastoma (GNB) is not an independently studied disease in most of the primary literature. It is one of four categories in a single nosological family — the **peripheral neuroblastic tumours (pNTs)** — and the overwhelming majority of mechanistic, genomic and therapeutic evidence is generated on *neuroblastoma* cohorts in which GNB cases are either pooled or excluded. Throughout this report, claims are labelled **[GNB-specific]** where the cited study separately analysed GNB, and **[pNT-wide / extrapolated]** where the evidence is from neuroblastoma and is applied to GNB by family membership. This distinction matters a great deal for a mechanism knowledge base: the two GNB subtypes sit at opposite ends of the clinical spectrum (one is a benign-behaving tumour managed by observation, the other is risk-stratified and treated exactly like neuroblastoma), and lumping them produces statements that are false of both.

---

## 1. Disease Information

### 1.1 Overview

Ganglioneuroblastoma is a **neuroblastic tumour of the developing sympathetic nervous system** occupying the middle of a maturational spectrum that runs from undifferentiated neuroblastoma (malignant, Schwannian stroma-poor) through to ganglioneuroma (benign, Schwannian stroma-dominant). It is defined histologically, not clinically or genetically: the diagnosis requires **neuroblastic cells, ganglion cells, and Schwannian stroma**, with the stromal component exceeding 50% of tumour volume.

MONDO's definition (verified via EBI OLS4, MONDO:0005035):

> "A neuroblastic tumor characterized by the presence of neuroblastic cells, ganglion cells, and a stroma with Schwannian differentiation constituting more than fifty-percent of the tumor volume."

**The single most important fact about this entry is that "ganglioneuroblastoma" names two biologically and clinically distinct entities**, and the WHO 5th-edition classification keeps them separate rather than as subtypes of one thing:

| Entity | ICD-O-3.2 | Schwannian stroma | Behaviour |
|---|---|---|---|
| Ganglioneuroma | 9490/0 | Stroma-dominant | Benign |
| **Ganglioneuroblastoma, intermixed (GNBi)** | **9490/3** | **Stroma-rich** | Favourable histology at **any** age |
| Neuroblastoma | 9500/3 | Stroma-poor | Age/MKI/grade-dependent |
| **Ganglioneuroblastoma, nodular (GNBn)** *(and other composite neuroblastic tumours)* | **9490/3** | **Composite: stroma-rich/dominant + stroma-poor** | Graded by the **highest-grade nodule**; can be fully malignant |

*Source: WHO Classification of Tumours Editorial Board (2023), Paediatric Tumours, WHO Classification of Tumours 5th edition, Volume 7, IARC, Lyon — reproduced in Table 1 of the ICCR Neuroblastoma Histopathology Reporting Guide, 1st ed. v1.0, November 2023 (ISBN 978-1-922324-39-9), https://www.iccr-cancer.org/wp-content/uploads/2023/11/ICCR-Neuroblastoma-1st-ed-v1.0-bookmark.pdf*

Verbatim definitions from the ICCR dataset (Note 7, Histological tumour type):

> **Ganglioneuroblastoma, intermixed (Schwannian stroma-rich) category** — "Tumours in this category are characterised by the presence of a ganglioneuromatous component with Schwannian stromal development (see below) exceeding 50% of the tissue, where microscopic nests of neuroblastoma are present in an intermixed or randomly distributed pattern. In those microscopic nests, the tumour cells are in various stages of differentiation (often predominantly differentiating neuroblasts) with clearly identifiable naked neuritic processes (neuropile, not covered by Schwann cells) around their cytoplasm. Grossly visible haemorrhagic/necrotic nodules suggestive of aggressive neuroblastomatous growth are absent. Tumours in this category are histologically one step behind the final stage of complete maturation towards ganglioneuroma."

> **Ganglioneuroblastoma, nodular (composite, Schwannian stroma-rich/stroma-dominant and stroma-poor) category** — "Tumours in this category are composed of multiple clones demonstrating distinct histologies: one or more Neuroblastoma (Schwannian stroma-poor) nodules set within a background of either Ganglioneuroblastoma, intermixed (Schwannian stroma-rich) or Ganglioneuroma (Schwannian stroma-dominant). The neuroblastoma nodules are usually grossly identifiable and often haemorrhagic/necrotic and fragile. In contrast, the Ganglioneuroblastoma, Intermixed/Ganglioneuroma component is tan-yellow and solid/elastic."

### 1.2 Key identifiers

Verified against EBI OLS4 (MONDO term record, 21 Oct 2026):

| Resource | Identifier |
|---|---|
| **MONDO** | **MONDO:0005035** (ganglioneuroblastoma) |
| NCI Thesaurus | NCIT:C3790 |
| HPO | HP:0006747 (Ganglioneuroblastoma) |
| Orphanet | ORPHA:251877 |
| MeSH | D018305 |
| UMLS | C0206718 |
| Disease Ontology | DOID:4163 |
| EFO | EFO:0000502 |
| GARD | GARD:0020719 |
| MedGen | 60218 |
| MedDRA | 10017708 |
| SNOMED CT | 116381000119105 |
| ICD-O-3 | 9490/3 |
| ICD-9 | 171.9 |
| OncoTree | GNBL |
| NANDO | NANDO:2200041 |
| birnlex | birnlex:12633 |

**Subtype and site-specific ontology terms** (all verified via OLS4):

| Concept | MONDO | NCIT |
|---|---|---|
| Intermixed (Schwannian stroma-rich) GNB | MONDO:0003326 | NCIT:C42057 |
| Nodular GNB | MONDO:0003325 | NCIT:C124274 (childhood) |
| Schwannian stroma-rich + stroma-poor composite | MONDO:0004408 | — |
| Stroma-dominant + stroma-poor composite | MONDO:0004407 | — |
| Adrenal gland GNB | MONDO:0004477 | NCIT:C7646 |
| Mediastinal GNB | MONDO:0001096 | NCIT:C6627 |
| Peripheral GNB | MONDO:0003327 | NCIT:C6594 |
| CNS GNB | — | NCIT:C92629 |
| Recurrent GNB | — | NCIT:C173531 |

**Not verified in this session (flagged for lookup before binding):** the ICD-11 morphology code reported by aggregator sources as `XH77W7` (ICD-11 Foundation 1916269207) was obtained from MalaCards/Wikidata-derived search summaries rather than from the WHO ICD-11 browser directly. Do not bind it without checking the ICD-11 MMS browser.

**A curation note:** NCIT:C92629 (Central Nervous System Ganglioneuroblastoma) and NCIT:C124272 name a *different* tumour — a CNS neuroepithelial neoplasm — that shares the word "ganglioneuroblastoma" but is not a peripheral neuroblastic tumour. Binding it into a pNT entry would be a Named Entity Confusion of exactly the kind this knowledge base's reference SOP warns about. Olfactory/esthesioneuroblastoma-associated "olfactory ganglioneuroblastoma" is likewise a separate entity.

### 1.3 Synonyms

From MONDO: *ganglioneuroblastoma (disease)*, *ganglioneuroblastoma, malignant*, *ganglioneuroblastoma (morphologic abnormality)*. In the literature: **GNB**, **GNBi** / **GNB-I** (intermixed), **GNBn** / **GNB-N** (nodular), *composite ganglioneuroblastoma*, *stroma-rich neuroblastoma* (historical, pre-INPC). The umbrella family term is **peripheral neuroblastic tumour (pNT)**; "neuroblastoma" is widely used generically for the whole family, which is a recurring source of data-extraction error.

### 1.4 Source of information

Predominantly **aggregated disease-level resources**: histopathology reference series (INPC committee reviews), international cooperative-group registries (INRG Data Commons, COG ANBL00B1 biology study), and population cancer registries (SEER). Individual-patient EHR-derived data are essentially absent from the GNB literature; the SEER-derived analyses are registry abstractions, not EHR phenotyping. A large fraction of the GNB-specific literature consists of **single case reports and small institutional case series**, which should be weighted accordingly.

---

## 2. Etiology

### 2.1 Disease causal factors

GNB is a **sporadic somatic neoplasm of embryonic origin** in the overwhelming majority of cases. There is no established environmental or infectious cause, and no single necessary-and-sufficient genetic lesion. The accepted model is that pNTs arise from **failure of developmentally programmed differentiation and/or death of sympathoadrenal progenitors derived from the neural crest**, with the degree of residual differentiation capacity determining where on the neuroblastoma → GNB → ganglioneuroma spectrum a tumour lands.

> "Neuroblastoma (NB), a heterogenous pediatric tumor of the sympathetic nervous system, is the most common and deadly extracranial solid malignancy diagnosed in infants." — Sainero-Alcolado L, Sjöberg Bexelius T, Santopolo G, et al. *Defining neuroblastoma: From origin to precision medicine.* Neuro Oncol. 2024. **PMID: 39101440**

### 2.2 Genetic risk factors

**Germline predisposition is rare and is shared with neuroblastoma rather than specific to GNB.** The authoritative recent statement is the 2023 AACR Childhood Cancer Predisposition Workshop update:

> "Genetic predisposition to neuroblastoma (NB) is relatively rare. Only 1% to 2% of patients have a family history of NB, 3% to 4% of cases present with bilateral or multifocal primary tumors, and occasional patients have syndromes that are associated with increased NB risk. Previously, a germline pathogenic variant (GPV) in PHOX2B was associated with Hirschsprung disease and congenital central hypoventilation syndrome. Recently, certain GPVs were shown to be responsible for congenital central hypoventilation syndrome and NB predisposition. Also, several groups determined that activating GPVs in ALK accounted for a substantial number of familial NB."
> — Kamihara J, Diller LR, Foulkes WD, et al. *Neuroblastoma Predisposition and Surveillance—An Update from the 2023 AACR Childhood Cancer Predisposition Workshop.* Clin Cancer Res. 2024;30(15):3137. **PMID: 38860978**; DOI: 10.1158/1078-0432.CCR-24-0237

The ICCR dataset states the same figure and names the broader syndrome set:

> "An inherited predisposition to neuroblastoma has been estimated in 1-2% of patients with newly diagnosed neuroblastic tumours... The genes most commonly altered in inherited neuroblastoma are *ALK* and *PHOX2B*. Other cancer predisposition syndromes (CPS) that may include neuroblastic tumours are RASopathy syndromes, Beckwith-Wiedemann syndrome, Li-Fraumeni syndrome and DNA repair disorders." (ICCR Note 1)

| Gene | HGNC | Role | Key evidence |
|---|---|---|---|
| **ALK** | hgnc:427 | Major familial NB gene; activating germline missense in tyrosine kinase domain (R1275Q, F1174L, R1192P, G1128A); autosomal dominant, **incomplete penetrance** | Mossé YP, et al. *Identification of ALK as a major familial neuroblastoma predisposition gene.* Nature. 2008;455(7215):930-935. **PMID: 18724359**; Janoueix-Lerosey I, et al. Nature. 2008;455(7215):967-970 |
| **PHOX2B** | hgnc:9143 | First gene shown to predispose to NB; homeodomain variants; co-segregates with Hirschsprung disease and CCHS | Trochet D, et al. Am J Hum Genet. 2004. **PMID: 15024693** — "PHOX2B, therefore, stands as the first gene for which germline mutations predispose to NB"; Mossé YP, et al. Am J Hum Genet. 2004. **PMID: 15338462**; Bourdeaut F, et al. Cancer Lett. 2005 (R100L). **PMID: 15949893** |
| **NF1** | hgnc:7765 | RASopathy; a GNB case with a heterozygous NF1 exon 1–58 deletion is reported | Zhang Q, et al. *Ganglioneuroblastoma associated with neurofibromatosis type 1: a case report with a systematic review.* Front Oncol. 2026. **PMID: 42311262** |
| **LMO1** | hgnc:6641 | Common-variant susceptibility via super-enhancer polymorphism rs2168101 G>T altering GATA binding | Oldridge DA, et al. *Genetic predisposition to neuroblastoma mediated by a LMO1 super-enhancer polymorphism.* Nature. 2015. **PMID: 26560027** |
| **LIN28B** | hgnc:32207 | GWAS susceptibility locus | Tonini GP, Capasso M. Cancer Metastasis Rev. 2020. **PMID: 31927719** |
| **BARD1** | hgnc:952 | GWAS susceptibility locus, genome-stability pathway | Tonini GP, Capasso M. 2020. **PMID: 31927719** |
| **TP53** (Li-Fraumeni, incl. p.R337H) | — | Associated syndrome; surveillance recommended | NCI PDQ, Neuroblastoma Treatment (Health Professional Version) |
| CASC15, CHEK2, AXIN2, BRCA1 | — | Reported susceptibility / genome-instability associations | Tonini GP, Capasso M. 2020. **PMID: 31927719** |

**ALKAL1 (hgnc:33775) / ALKAL2 (hgnc:27683)** encode the ALK ligands (ALKAL/FAM150/AUGβ) and are mechanistically relevant to ALK activation, though not established predisposition genes.

**[GNB-specific gap]** No study has tested whether germline predisposition is enriched, depleted, or differently distributed in GNBi versus GNBn versus neuroblastoma. The 1–2% figure is a pNT-wide estimate.

### 2.3 Environmental risk factors

**No environmental exposure has been established as causal.** Age (infancy/early childhood), and to a lesser degree ancestry, are the only consistently reported non-genetic risk associations for pNTs.

From NCI PDQ (Neuroblastoma Treatment, Health Professional Version): relative risks of neuroblastoma compared with White patients were **0.54 (Hispanic), 0.64 (Asian/Pacific Islander), 0.69 (American Indian/Alaska Native), and 0.73 (Black)**.

In the SEER GNB cohort (n = 1,194), racial distribution was **White 78.8%, Black 12.6%, other 8.5%** — a distribution that reflects both incidence and the underlying US population, and should not be read as a risk estimate (Li W, et al. Heliyon. 2024;10(9):e30891. **PMID: 38774105**).

**Not applicable / no evidence found:** occupational exposure, radiation, pollution, tobacco, diet, and alcohol have no established role in GNB specifically. Parental-exposure epidemiology for neuroblastoma has produced no replicated finding of the strength needed for a mechanism claim.

### 2.4 Protective factors

**Genetic:** No validated protective variant is reported for GNB. The protective end of the ALK allelic spectrum is simply absence of an activating variant, which is not a protective allele.

**Environmental/behavioural:** None established. **Population newborn screening is explicitly *not* protective** and the evidence is strong and negative — see §13.

### 2.5 Gene–environment interactions

**No established gene–environment interaction for GNB.** There is a conceptually important *gene–developmental-timing* interaction rather than a gene–environment one: the prognostic effect of histology is **age-dependent** (see §3 and §8), and the prognostic effect of MKI has distinct age cut-offs per MKI class (Teshiba R, et al. Pediatr Dev Pathol. 2014;17(6):441-449. **PMID: 25207821**). This is interaction between a tumour-intrinsic variable and host developmental stage, and should be modelled as such rather than as an environmental modifier.

---

## 3. Phenotypes

### 3.1 How GNB presents

Most phenotypes are **mass-effect phenotypes determined by anatomical site**, not by tumour biology. A second, smaller group are **secretory/paraneoplastic phenotypes**. This split is the right organising principle for a mechanism entry: the first group's causal parent is tumour growth at a site, the second's is a secreted product or an anti-neural immune response.

The ICCR dataset's statement of the paraneoplastic set (Note 1, verbatim):

> "Multiple paraneoplastic syndromes can be associated with neuroblastic tumours, including opsoclonus myoclonus ataxia, cerebellar ataxia, Horner syndrome, Hirschsprung disease/CCHS, rapid-onset obesity with hypoventilation, hypothalamic dysfunction, autonomic dysregulation (ROHHAD), and vasoactive intestinal peptide (VIP)-associated secretory diarrhoea or VIPoma syndrome."

### 3.2 Phenotype table with suggested HPO terms

HPO terms below marked ✅ were verified against EBI OLS4 in this session; those marked ⚠ are suggestions requiring lookup before binding.

| Phenotype | Type | HPO suggestion | Onset | Course | Frequency / notes |
|---|---|---|---|---|---|
| Abdominal mass | Clinical sign | **HP:0031500** Abdominal mass ✅ | Infancy–early childhood | Progressive | Most common presentation of abdominal pNT (NCI PDQ) |
| Abdominal pain / distension | Symptom | ⚠ HP:0002027 / HP:0003270 | Childhood | Variable | Common with retroperitoneal/adrenal primaries |
| Thoracic mass / respiratory distress | Clinical sign | ⚠ HP:0002094 Dyspnea | Childhood | Variable | Posterior mediastinal primaries; GNB is over-represented in thorax relative to NB (30% of GNBn vs 9% of NB, He 2017, **PMID: 28465480**) |
| **Horner syndrome** | Clinical sign | **HP:0002277** Horner syndrome ✅ (congenital form **HP:0006837** ✅; **HP:0007451** ipsilateral lack of facial sweating ✅) | Childhood | Often persistent | "Characterized by miosis, ptosis, and anhidrosis. It may be caused by neuroblastoma in the stellate ganglion" (NCI PDQ) |
| Spinal cord / nerve-root compression; paraparesis | Clinical sign | ⚠ HP:0002176 Spinal cord compression; HP:0002385 Paraparesis | Childhood | Can be acute, emergency | Dumbbell paraspinal tumours invading through neural foramina (NCI PDQ; Alioglu H, et al. Eur Spine J. 2026. **PMID: 42811141** — systematic review of 18 spinal-canal GNB cases) |
| **Opsoclonus–myoclonus–ataxia syndrome (OMAS)** | Behavioural/neurological | **HP:0010543** Opsoclonus ✅; ⚠ HP:0001336 Myoclonus; ⚠ HP:0001251 Ataxia | 6 months – 3 years | Relapsing; often persistent neurocognitive sequelae | "Of young children presenting with opsoclonus/myoclonus syndrome, about one-half are found to have neuroblastoma" (NCI PDQ); OMAS-associated tumours "tend to be low grade, thoracic in location, and have a more favorable outcome" |
| **VIP-mediated secretory diarrhoea (WDHA/VIPoma syndrome)** | Lab + symptom | ⚠ HP:0002028 Chronic diarrhea; ⚠ HP:0002900 Hypokalemia | Childhood | Resolves on resection | "On rare occasions, children may have severe, watery diarrhea caused by the secretion of vasoactive intestinal peptide by the tumor" (NCI PDQ). **Associated with more differentiated tumours** (GNB/GN) more than with undifferentiated NB |
| **Catecholamine-driven hypertension** | Clinical sign | ⚠ HP:0000822 Hypertension | Infancy–childhood | Reversible on resection | Shimizu H, et al. *Infantile Ganglioneuroblastoma Causing Growth Failure and Hypertensive Cardiomyopathy From Excessive Catecholamine Production.* J Pediatr Hematol Oncol. 2026. **PMID: 41891982** — a 3-year-old with excess epinephrine/norepinephrine and "hypertensive cardiomyopathy" |
| Growth failure | Clinical sign | ⚠ HP:0001510 Growth delay | Childhood | Reversible with tumour control | Same case (**PMID: 41891982**) |
| **Elevated urinary HVA** | Laboratory | **HP:0011977** Elevated urinary homovanillic acid ✅ | — | — | Chemical: homovanillic acid **CHEBI:545959** ✅ |
| **Elevated urinary VMA** | Laboratory | **HP:0011978** Elevated urinary vanillylmandelic acid ✅ | — | — | Chemical: vanillylmandelic acid **CHEBI:20106** ✅. VMA abnormal in only **21%** of GNBn and **19%** of GNBi vs **59%** of NB (He 2017, **PMID: 28465480**) |
| Bone pain, pancytopenia, proptosis, periorbital ecchymosis | Clinical signs | ⚠ HP:0002653, HP:0001876, HP:0000520 | Childhood | Progressive | Features of **metastatic (stage M)** disease — relevant to GNBn, essentially never GNBi |
| Constipation | Symptom | ⚠ HP:0002019 | Childhood | Variable | Reported in GNB paraneoplastic series alongside diarrhoea (Springer, Eur J Pediatr 2003, doi:10.1007/s00431-003-1212-0) |

### 3.3 Phenotype characteristics

- **Age of onset.** Early childhood. GNB subtypes are consistently **older at diagnosis than neuroblastoma**: median 28.9 months (NB) vs 38.4 months (GNBn) vs 47.5 months (GNBi) in a 279-patient single-centre series (He WG, et al. Oncotarget. 2017;8(23):37730-37739. **PMID: 28465480**). In the INRG GNBn cohort, **83% were older than 18 months** (Angelini P, et al. Eur J Cancer. 2012. **PMID: 22137163**).
- **Severity.** Bimodal by subtype. GNBi is almost uniformly indolent; GNBn spans the full range, with stage 4 GNBn carrying 35% ± 7% OS (**PMID: 22137163**).
- **Progression.** GNBi/GN grow slowly and may be static for years: "GN and GNB-I have a slow growth rate and resection can be associated with significant morbidity" (Alexander N, et al. Pediatr Blood Cancer. 2018. **PMID: 29369484**). GNBn behaves as the biology of its nodule dictates.
- **Frequency among affected individuals.** Reliable per-phenotype frequencies for GNB specifically are **not published**. The serum/urine marker frequencies in §3.2 (from **PMID: 28465480**) are the best available and are from a single centre with n = 20 GNBn and n = 31 GNBi; treat them as indicative, not as population frequencies.

### 3.4 Quality-of-life impact

No GNB-specific QoL instrument data exist. The relevant data are from **high-risk neuroblastoma survivors**, which applies to the GNBn stage-4 subgroup and not to GNBi:

- The COG **LEAHRN** cross-sectional cohort found moderate-to-severe hearing loss in **72%** of high-risk neuroblastoma survivors, with more than half underweight, and most participants carrying **at least two clinically important late effects** (Lancet Child Adolesc Health, 2025; https://www.sciencedirect.com/science/article/abs/pii/S235246422500241X).
- Flaadt T, et al. *Long-Term Outcomes and Quality of Life of High-Risk Neuroblastoma Patients Treated with a Multimodal Treatment Including Anti-GD2 Immunotherapy.* Cancers. 2025;17(1):149. **PMID: 39796776** — among 25 survivors at 25 years: ototoxicity 64%, cardiac toxicity 24%, endocrine effects 76%; "Quality-of-life scores exceeded matched general population comparators."
- Self-reported survivor data show **50% meeting anxiety/depression criteria versus a 25% population norm** (PubMed **37311662**).

Instruments in use: EQ-5D, SF-36, PROMIS, PedsQL. No disease-specific GNB instrument exists.

---

## 4. Genetic / Molecular Information

### 4.1 There is no causal gene for ganglioneuroblastoma

This is a structural point that should be recorded explicitly rather than left as an absence. GNB is a **somatic neoplasm defined by morphology**; it has driver lesions, not a causal gene, and a given GNB may carry none of the recurrent drivers at all. The diagnosis is made on a histology slide, and the molecular work-up is *prognostic* rather than diagnostic.

### 4.2 Recurrent somatic alterations

| Alteration | Gene / locus | Frequency | Origin | Functional consequence | Evidence |
|---|---|---|---|---|---|
| **MYCN amplification** (double minutes → HSRs) | **MYCN**, hgnc:7559, 2p24 | **GNBi 0%; GNBn 14%; NB 26%** in one series (**PMID: 28465480**); **2%** of GNBn in the INRG cohort (**PMID: 22137163**) | Somatic | Amplification ⇒ N-Myc overexpression; "a proto-oncogene which inhibits cell differentiation and apoptosis and promotes division" (ICCR Note 13). FISH: ratio **≥4 = amplified**; **>1 but <3 = "gain"**, clinical significance unclear | ICCR Note 13; **PMID: 28465480**; **PMID: 22137163** |
| **ALK point mutation** | **ALK**, hgnc:427, 2p23 | "mutated in 8-10% of sporadic neuroblastic tumours, amplified in about 2%" (ICCR Note 13). In 943 patients: **10.5% at diagnosis**, "highest frequencies in stage 4 patients <18 months"; at relapse the frequency rises **~70%**, mostly *de novo* R1275Q | Somatic (also germline — §2.2) | Gain of function: constitutive receptor tyrosine kinase activity. **ALK amplifications — but not mutations — correlated with poor outcome** | Rosswog C, et al. Br J Cancer. 2023. **PMID: 36807339**; ICCR Note 13 |
| **1p36 deletion** | 1p36 | Segmental; co-occurs with MYCN amplification | Somatic | Loss of tumour-suppressor region | Schleiermacher G, et al. Br J Cancer. 2012;107(8):1418-1422; Irwin MS, et al. J Clin Oncol. 2021;39(29):3229-3241 |
| **11q deletion** | 11q | Segmental; **rarely co-occurs with MYCN amplification**; marks a distinct poor-prognosis group | Somatic | Loss; strongly associated with ALT telomere maintenance | Nakazawa A. Pathol Int. 2021. **PMID: 33657257**; Djos A, et al. Genes Chromosomes Cancer. 2024, doi:10.1002/gcc.23260 |
| **17q gain** | 17q | Reported in **65% of 48** neuroblastomas; more frequent than either 1p deletion or MYCN amplification across all stages | Somatic | Dosage gain; poor prognosis | PMC2362984; ICCR Note 13 |
| **ATRX loss-of-function** | **ATRX**, hgnc:886 | ~11% of high-risk NB; **~40% in adolescents**, <20% in younger children, **0% in infants <1 year** | Somatic (and germline in syndromic cases) | Loss of function ⇒ ALT telomere maintenance | NCI PDQ; Djos A, et al. 2024 |
| **TERT rearrangement / overexpression** | **TERT**, hgnc:11730 | ~23% of high-risk NB | Somatic | Telomerase activation | ICCR Note 13; Djos A, et al. 2024 |
| **Whole-chromosome gains/losses (numerical only)** | genome-wide | The **favourable** genomic signature | Somatic | Hyperdiploidy; no segmental breakage | Nakazawa A, et al. Cancer Sci. 2015. **PMID: 25827934** |

Nakazawa's genomic-signature correlation is the most directly useful result for a mechanism entry, because it links the histological axis to the genomic axis:

> "Analysis of 92 neuroblastoma cases with INPC evaluation and genomic grouping showed significant correlation between unfavorable histology and partial gains/losses (GGP), and favorable histology with whole gains/losses (GGW). Unfavorable histology and GGP were late-onset (median 36 and 48 months) with poor prognosis (OS 43.1%, 42.4%). Favorable histology and GGW were early-onset (median 4, 9.5 months) with favorable prognosis (OS 88.6%, 87.1%)." — **PMID: 25827934**

### 4.3 The GNBn clonality question — a key GNB-specific result

The historical model of GNBn — stated explicitly in the original Shimada framework — was that the aggressive nodule and the benign stroma-rich background are **separate clones**. That model has been tested and does not hold:

> "Neuroblasts and ganglion cells in nodular ganglioneuroblastoma are genetically related and may arise from the same clone... the clinical behavior of nodular ganglioneuroblastoma cannot be explained by the presence of separate clones with distinct genetic signatures."
> — Angelini P, Baruchel S, Marrano P, Irwin MS, Thorner PS. *The neuroblastoma and ganglion components of nodular ganglioneuroblastoma are genetically similar: evidence against separate clonal origins.* Mod Pathol. 2015;28(1):96-103. **PMID: 25081755**; DOI: 10.1038/modpathol.2014.90

Method and key finding: eight paraffin-embedded GNBn cases analysed by SNP array and *in situ* hybridisation. **MYCN gain (4–10 gene copies/nucleus) was detected in 7/8 neuroblastoma samples**, and in the ganglioneuromatous regions, "gains were also detected in **ganglion cells but not in Schwann cells**."

Three mechanistic consequences follow, and they are the heart of a GNB pathophysiology model:

1. The neuroblasts and the ganglion cells are **the same tumour lineage at different differentiation states** — so GNBn represents *partial* differentiation of one clone, not two coincident tumours.
2. **The Schwannian stroma is genetically normal** — it is reactive, recruited host tissue, not neoplasm. Any claim that the stroma is "part of the tumour" in the neoplastic sense is wrong.
3. The INPC rule that GNBn is graded by its highest-grade nodule (ICCR Note 10) is therefore a statement about **intratumoural heterogeneity within one clone**, not about which of two clones dominates.

### 4.4 Telomere maintenance in GNB — the most recent GNB-specific molecular study

> "Analysis of 321 neuroblastic tumors revealed that TMM activation occurred in **48% of nodular ganglioneuroblastomas**, similar to **39%** of neuroblastomas, serving as a poor prognostic marker."
> — Sugawara M, Haruta M, Ohira M, et al. *Telomere maintenance mechanisms are activated in ganglioneuroblastoma and ganglioneuroma.* Oncol Lett. 2026. **PMID: 41858373**; DOI: 10.3892/ol.2026.15509

The paper's own framing: "TMM serves as a poor prognostic marker for high-risk NB and offers valuable insights for the risk classification of GNBs." This is an important and counterintuitive result: GNBn — a tumour whose benign-looking stromal majority can make it *look* indolent — activates telomere maintenance at a rate at least as high as neuroblastoma. It is direct molecular support for the clinical rule that GNBn must be risk-stratified as neuroblastoma.

### 4.5 Modifier genes

No validated modifier gene for GNB. The *de facto* modifiers in clinical use are **age at diagnosis** and **INPC histology**, which modify the prognostic effect of every other variable (see §8 and §11).

### 4.6 Epigenetic information

- **DNA methylation profiling** is emerging as a molecular classifier of neuroblastoma (PMC12297820, 2025). GNB-specific methylation classes have not been separately defined.
- **Cell-identity epigenetics is the central epigenetic mechanism in this family**: neuroblastoma cells exist in **noradrenergic** and **mesenchymal** identities defined by distinct super-enhancer landscapes and core regulatory circuitries, and can interconvert:
  > "We now document spontaneous and reversible plasticity between the two identities, associated with epigenetic reprogramming, in several neuroblastoma models... a subpopulation of these noradrenergic tumor cells presents with mesenchymal features that are shared with plasticity models, indicating that the plasticity described in these models has relevance in neuroblastoma patients. This work therefore emphasizes that intrinsic plasticity properties of neuroblastoma cells are dependent upon external cues of the environment to drive cell identity."
  — Thirant C, Peltier A, Durand S, et al. Nat Commun. 2023. **PMID: 37142597**
- **HDAC8** is a druggable epigenetic node for differentiation: selective HDAC8 inhibition induces differentiation and synergises with retinoic acid via CREB (Rettig I, et al. Cell Death Dis. 2015. **PMID: 25695609**).
- **ZNF423** is required for retinoic-acid-induced differentiation, and low expression predicts poor outcome (Huang S, et al. Cancer Cell. 2009. **PMID: 19345331**).

### 4.7 Chromosomal abnormalities

Covered in §4.2. For reporting purposes, the ICCR requires **MYCN status** as a core element and recommends **DNA index/ploidy** (near-diploid/tetraploid unfavourable; hyperdiploid favourable in infants <1 year) and segmental chromosomal aberration panel (1p, 11q, 17q). Detection platforms in current use: FISH (MYCN), SNP/CGH array, and NGS copy-number analysis.

---

## 5. Environmental Information

- **Environmental factors:** None established. No toxin, radiation source, pollutant, or occupational exposure is causally linked to GNB. **[No evidence found]** — this is a genuine negative, not a search gap: the pNT epidemiology literature has looked and has not produced a replicated association.
- **Lifestyle factors:** Not applicable. GNB is a tumour of infancy and early childhood; patient lifestyle factors have no role, and parental-exposure studies have produced no established association.
- **Infectious agents:** **Not applicable.** GNB has no infectious aetiology. There is no pathogen to record, no transmission route, and no `infectious_agent` entry is warranted.

A mechanism entry for GNB should carry **no `environmental:` block**, or should record the deliberate absence with the searches that were run.

---

## 6. Mechanism / Pathophysiology

### 6.1 Ordered causal chain

The chain below runs from the initiating lesion to clinical manifestation. Steps are numbered; branches are shown explicitly. **[D]** = demonstrated in human tumour tissue or a direct model; **[I]** = inferred, i.e. the step is a reasonable bridge between two demonstrated steps but has not itself been directly shown in GNB.

**Trunk — origin and initiation**

1. During embryogenesis, **neural crest cells** (CL:0011012) delaminate and migrate ventrally, giving rise to **sympathoadrenal progenitors** and, via a second route, to **Schwann cell precursors** (CL:0002375) that travel along nerves and themselves contribute to the sympathoadrenal cell pool. **[D]** — two successive neural-crest-derived progenitor states are now resolved by single-cell atlases (Hanemaaijer ES, et al. PNAS. 2021. **PMID: 33500353**; Olsen TK, et al., *Malignant Schwann cell precursors mediate intratumoral plasticity in human neuroblastoma*, bioRxiv 2020, doi:10.1101/2020.05.04.077057).
2. **PHOX2B** (hgnc:9143) specifies and maintains the noradrenergic sympathoadrenal programme. Reduced PHOX2B dosage or dominant-negative PHOX2B **leads to** a block in sympathetic neuronal precursor differentiation. **[D in zebrafish]** — "reduced dosage of PHOX2B during development, through either a heterozygous deletion or dominant-negative mutation, imposes a block in the differentiation of sympathetic neuronal precursors, resulting in a cell population that is likely to be susceptible to secondary transforming events" (Pei D, et al. PLoS Genet. 2013. **PMID: 23754957**). Mechanistically, "Patient-derived mutant PHOX2B constructs retained the ability to suppress cellular proliferation, but were not able to promote differentiation" (Raabe EH, et al. Oncogene. 2008. **PMID: 17637745**) — i.e. the lesion is specifically a **differentiation** defect, not a proliferation-brake defect.
3. A **transforming lesion** occurs in that arrested progenitor — most often MYCN amplification, an activating ALK variant, or a segmental chromosomal aberration — which **results in** sustained proliferation plus an additional, independent block on terminal differentiation. **[D]** — "MYCN induces the expansion of these progenitors by both promoting their proliferation and preventing their differentiation" (Alam G, et al. Am J Pathol. 2009. **PMID: 19608868**). PHOX2B and ALK are not independent inputs here: "PHOX2B drives ALK gene transcription by directly binding its promoter" (Bachetti T, et al. PLoS One. 2010. **PMID: 20957039**).
4. The transformed clone expands as a mass in a sympathetic-chain or adrenal-medullary site. **[D]**

**Branch point — the differentiation fork that defines GNB**

5. The expanded clone is exposed to **differentiation-promoting signals from Schwannian stroma**, which is recruited host (non-neoplastic) tissue. This step is the one that distinguishes GNB from neuroblastoma. **[D for the stroma being non-neoplastic:** Schwann cells carry no MYCN gain in GNBn, **PMID: 25081755**; **D for the stroma being instructive:** Schwann-cell-conditioned medium "induced extensive neurite outgrowth in all neuroblastoma cell lines, and these processes contained mature neurofilament in three of the cell lines" (Kwiatkowski JL, et al. Cancer Res. 1998. **PMID: 9788610**); PEDF is "the major factor responsible for Schwann cell's ability to induce tumor cell differentiation in vitro and recombinant PEDF had the same effect in vitro and in vivo" (Crawford SE, et al. J Cell Sci. 2001. **PMID: 11792807**).]
6. Reciprocally, the tumour cells **recruit and expand the stroma**: "Human NB tumours or cell lines unequivocally increased the proliferation of SCs in vitro" (Ambros IM, et al. Med Pediatr Oncol. 2001. **PMID: 11464875**). This closes a **positive feedback loop between tumour differentiation and stromal expansion** — the loop that produces the stroma-rich architecture by which GNB is defined. **[D in vitro; I in human tumour]**
7. Stromal signalling **results in** neuroblast maturation into **ganglion cells**, which lose proliferative capacity and acquire neuronal morphology (eccentric vesicular nucleus, prominent nucleolus, abundant cytoplasm, Nissl substance), with neuritic processes becoming fully ensheathed by Schwann cells. **[D — this is the defining morphological criterion in ICCR Note 7: naked neuritic processes identify differentiating neuroblasts; their absence identifies ganglion cells.]**

   - **Branch 5a → GNBi.** If this differentiation reaches >50% stromal volume with only microscopic residual neuroblastic nests and **no grossly visible haemorrhagic/necrotic nodule**, the tumour is **ganglioneuroblastoma, intermixed** — "histologically one step behind the final stage of complete maturation towards ganglioneuroma" (ICCR Note 7). Clinically: favourable histology at any age. **[D]**
   - **Branch 5b → ganglioneuroma.** If differentiation goes to completion, the tumour is a ganglioneuroma (9490/0). **[D]**
   - **Branch 5c → GNBn.** If **a subclone escapes the differentiation signal** and expands as a discrete stroma-poor nodule within the stroma-rich background, the tumour is **ganglioneuroblastoma, nodular**. The escaping subclone is genetically related to the differentiated component (**PMID: 25081755**), so this is clonal *divergence in differentiation state*, not two tumours. **[D for genetic relatedness; I for the "escape" framing — what drives one subclone to remain undifferentiated is not established.]**

**GNBn-specific continuation — the malignant arm**

8. The escaped nodule retains or acquires proliferative drivers (MYCN amplification in ~14% of GNBn, **PMID: 28465480**; segmental chromosomal aberrations; telomere maintenance in **48%**, **PMID: 41858373**), which **result in** a high mitosis–karyorrhexis index within the nodule. **[D]**
9. Unrestricted proliferation with telomere maintenance **leads to** local invasion and haematogenous/lymphatic dissemination, preferentially to **bone marrow, bone, liver and lymph node**. **[D]** — bone and liver are the two commonest isolated metastatic sites for neuroblastic tumours (Liu S, et al. World J Surg Oncol. 2023. **PMID: 37046344**).
10. In the bone-marrow niche, tumour cells **signal to monocytes via MIF and midkine**, rewiring them toward a tumour-associated-macrophage phenotype that supports the metastasis. **[D in neuroblastoma, pNT-wide]** — Fetahu IS, et al. Nat Commun. 2023. **PMID: 37365178**.
11. Marrow replacement **results in** cytopenias; bone metastases **result in** pain; orbital metastases **result in** proptosis and periorbital ecchymosis. **[D]**

**Parallel branch A — catecholamine secretion**

12. Because the tumour retains the sympathoadrenal programme, it expresses **tyrosine hydroxylase** and downstream catecholamine-synthetic enzymes, so it synthesises **dopamine, norepinephrine and epinephrine** (GO:0042423 catecholamine biosynthetic process ✅; GO:0006585 dopamine biosynthetic process from tyrosine ✅). **[D]**
13. Catecholamines are degraded to **homovanillic acid (CHEBI:545959 ✅)** and **vanillylmandelic acid (CHEBI:20106 ✅)**, which are excreted in urine and **result in** the diagnostic elevations HP:0011977 / HP:0011978. **[D]**
14. In a minority, systemic catecholamine excess **results in** hypertension and, if sustained, **hypertensive cardiomyopathy and growth failure**. **[D — PMID: 41891982]**

   *A quantitative asymmetry worth recording:* urinary VMA is abnormal in only **21% of GNBn and 19% of GNBi**, versus **59% of NB** (**PMID: 28465480**). The straightforward inference — that the more differentiated tumours secrete *less* measurable catecholamine metabolite, probably because a smaller fraction of tumour mass is metabolically active neuroblastic tissue — is **[I]**, not demonstrated; and it has a direct clinical consequence (catecholamine screening is a poor rule-out test for GNB).

**Parallel branch B — VIP secretion**

15. Some neuroblastic tumours, **preferentially the more differentiated ones**, secrete **vasoactive intestinal peptide**. **[D]**
16. VIP acting on intestinal epithelium **results in** profuse secretory diarrhoea with hypokalaemia and achlorhydria (WDHA syndrome), which **resolves on tumour resection**. **[D]** — NCI PDQ; ICCR Note 1.

**Parallel branch C — paraneoplastic autoimmunity (OMAS)**

17. Tumour antigens shared with CNS neurons **trigger** a cross-reactive immune response. **[I — the specific antigen is not established]**
18. That response **results in** opsoclonus (HP:0010543 ✅), myoclonus, ataxia and behavioural regression. **[D clinically]**
19. The same immune response is associated with **better tumour outcome** — OMAS tumours "tend to be low grade, thoracic in location, and have a more favorable outcome" (NCI PDQ). Whether the immune response *causes* the better outcome or merely co-marks favourable biology is **not established**; both readings are live in the literature. The ANBL00P3 randomised result (IVIG 81% vs non-IVIG 41% OMAS response) shows the neurological syndrome is immunomodulator-responsive, which supports the immune mechanism for the *neurological* arm without settling the tumour-control question.

**Parallel branch D — mass effect (site-determined)**

20. Tumour growth at a paraspinal site **leads to** extension through neural foramina (dumbbell morphology) and **results in** cord compression and paraparesis. **[D — PMID: 42811141]**
21. Tumour at the stellate/cervicothoracic ganglion (UBERON:0002441 ✅) **results in** Horner syndrome (HP:0002277 ✅). **[D]**

### 6.2 Molecular pathways

| Pathway | Role | Reference |
|---|---|---|
| **ALK receptor tyrosine kinase → RAS–MAPK and PI3K–AKT** | Primary oncogenic driver pathway; the one actionable target. ALK signalling also "phosphorylates ATR and CHK1, supporting effective DNA damage responses" | Borenäs M, et al. PNAS. 2024. **PMID: 38154064** |
| **MYCN transcriptional programme** | Proliferation + differentiation block; downstream of PHOX2B-specified lineage | **PMID: 19608868** |
| **PHOX2B → ALK transcriptional axis** | Lineage TF directly drives the RTK promoter | **PMID: 20957039** |
| **Retinoic acid receptor (RARα/RXRα) signalling** | The differentiation pathway; therapeutically exploited by isotretinoin. Requires ZNF423 | **PMID: 19345331**; **PMID: 3855502** |
| **NGF–TrkA (NTRK1)** | Developmentally programmed cell death / differentiation switch; "The most easily targeted mechanism is the delayed activation of developmentally programmed cell death regulated by the tropomyosin receptor kinase A (TrkA) pathway" (Brodeur GM. Cell Tissue Res. 2018. **PMID: 29305654**). The oncogenic TrkAIII splice variant "antagonizes NGF/TrkA/Ras/MAPK signaling, which is responsible for NB growth arrest and differentiation" (Tacconelli A, et al. Cancer Cell. 2004. **PMID: 15488758**) | — |
| **Delta–Notch (via MSX1, downstream of PHOX2B)** | "MSX1, NOTCH3 and HEY1 are more highly expressed in ganglioneuromas" — i.e. this axis marks the **differentiated** end of the spectrum | Revet I, et al. Exp Cell Res. 2008. **PMID: 18201699** |
| **Hedgehog signalling** | Implicated in ganglioneuroma pathogenesis via enteric neural crest differentiation | PMC2759000, *Enteric Neural Crest Differentiation in Ganglioneuromas Implicates Hedgehog Signaling in Peripheral Neuroblastic Tumor Pathogenesis* |
| **PEDF (SERPINF1) from Schwann cells** | Anti-angiogenic **and** pro-differentiation; the molecular mediator of Schwannian stromal benignity | **PMID: 11792807** |
| **MIF and midkine → monocyte rewiring** | Metastatic-niche pathway in bone marrow | **PMID: 37365178** |
| **Telomere maintenance — telomerase (TERT) and ALT (ATRX-associated)** | Immortalisation; active in **48% of GNBn** | **PMID: 41858373** |

### 6.3 Cellular processes and cell types

| Process | GO suggestion (✅ verified) | Cell types (CL, ✅ verified) |
|---|---|---|
| Neural crest cell differentiation | **GO:0014033** ✅ (regulation: **GO:1905292/1905293/1905294** ✅; fate determination **GO:0014035** ✅) | neural crest cell **CL:0011012** ✅ |
| Sympathetic nervous system development | **GO:0048485** ✅; NCC migration involved in SNS development **GO:1903045** ✅ | neural crest derived neuroblast **CL:0002676** ✅; neuroblast (sensu Vertebrata) **CL:0000031** ✅ |
| Autonomic nervous system development | **GO:0048483** ✅ | sympathetic neuron **CL:0011103** ✅ |
| Catecholamine biosynthetic process | **GO:0042423** ✅; dopamine **GO:0042416** ✅; from tyrosine **GO:0006585** ✅ | chromaffin cell **CL:0000166** ✅; adrenal medulla chromaffin cell **CL:0000336** ✅ |
| Schwann-cell-mediated differentiation support | ⚠ (no single GO term; consider GO terms for glial cell differentiation / positive regulation of neuron differentiation — **requires lookup**) | Schwann cell **CL:0002573** ✅; Schwann cell precursor **CL:0002375** ✅; non-myelinating Schwann cell **CL:0002376** ✅; myelinating Schwann cell **CL:0000218** ✅ |
| Cell cycle dysregulation / proliferation | ⚠ requires lookup | — |
| Telomere maintenance | ⚠ requires lookup | — |

### 6.4 Protein dysfunction

- **ALK**: activating missense in the kinase domain (R1275Q, F1174L, F1245V, R1192P, G1128A) → ligand-independent constitutive kinase activity. **Gain of function.** Note the ICCR caveat for curation: "ALK immunohistochemistry does not correlate well with gene mutation or amplification status, so sequencing of the kinase regions and/or known mutational hotspots is required."
- **N-Myc (MYCN)**: gene amplification → protein overabundance, not structural alteration. The ICCR notes genotype–phenotype discordant subsets in both directions: tumours with MYCN amplification but favourable histology that "appear to not produce functional N-myc protein despite having amplification of the gene", and tumours without amplification but unfavourable histology that "are often associated with C-myc protein expression or other molecular abnormalities instead."
- **PHOX2B**: homeodomain-disrupting variants → **selective loss of the differentiation-promoting function with retention of the anti-proliferative function** (**PMID: 17637745**). This is a true separation-of-function defect and should not be recorded simply as "loss of function".
- **ATRX**: loss of function → ALT.
- **TrkA (NTRK1)**: the TrkAIII splice variant (deletion of exons 6, 7, 9) is a **neomorphic** isoform — NGF-unresponsive, oncogenic, and actively antagonistic to the wild-type differentiation signal (**PMID: 15488758**).

### 6.5 Metabolic changes

The dominant metabolic feature is **catecholamine biosynthesis and turnover** (§6.1 branch A), which is a retained lineage programme rather than a tumour-acquired metabolic rewiring. Broader metabolic targets in neuroblastoma are an active area — "present and future directions for the identification of novel therapeutic metabolic targets, differentiation agents, as well as personalized combinatory therapies" (**PMID: 39101440**) — but no GNB-specific metabolomic signature is published. **[No GNB-specific data found.]**

### 6.6 Immune system involvement

- **Paraneoplastic autoimmunity (OMAS)** — §6.1 branch C.
- **GD2 as a tumour-surface target.** GD2 ganglioside is highly expressed on neuroblastic tumour cells and is the basis of all current immunotherapy. Dinutuximab is "A chimeric mouse/human monoclonal antibody with potential antineoplastic activity" that binds GD2 (NCIT:C1570 ✅).
- **Tumour-associated monocytes/macrophages in the marrow niche** — **PMID: 37365178**.
- **Chemotherapy–immunotherapy synergy**: standard induction agents enhanced dinutuximab beta efficacy up to **17-fold** in spheroid models (Troschke-Meurer S, et al. Cancers. 2023. **PMID: 36765861**).

### 6.7 Tissue damage mechanisms

Primarily **compression and invasion** rather than an intrinsic cytotoxic mechanism: cord compression, airway/vascular compression, marrow replacement. The GNBn nodule is characteristically **haemorrhagic and necrotic** (ICCR Note 7) — spontaneous intratumoural haemorrhage is a feature of the aggressive component and contributes to the gross distinction from the tan-yellow, solid/elastic stroma-rich background.

### 6.8 Molecular profiling

- **Transcriptomics / single cell.** The adrenergic–mesenchymal identity axis (**PMID: 37142597**), the SCP-like malignant subpopulation bridging the two compartments (Olsen TK, et al., doi:10.1101/2020.05.04.077057), and the developing-adrenal SCP signature, where "The SCP signature score anticorrelates with ALK and MYCN expression, two indicators of poor prognosis. Furthermore, a high SCP signature score is associated with better overall survival rates" (**PMID: 33500353**). **These are neuroblastoma studies**; the SCP-signature result is nevertheless the most mechanistically suggestive data point for GNB in the corpus, because GNB is by definition the SCP/Schwannian-rich end of the spectrum.
- **Proteomics / metabolomics / lipidomics:** **No GNB-specific dataset identified.**
- **Functional genomics screens:** the RNAi screen that identified ZNF423 as the RA-differentiation requirement (**PMID: 19345331**) is the clearest example. DepMap and CRISPR screens cover neuroblastoma cell lines; **no GNB-derived cell line exists**, which is itself a notable gap.

---

## 7. Anatomical Structures Affected

### 7.1 Organ level

**Primary sites.** Peripheral neuroblastic tumours arise anywhere along the sympathetic chain and in the adrenal medulla. **GNB's site distribution differs materially from neuroblastoma's**, and this is one of the few clean GNB-specific epidemiological facts:

| Site | NB | GNBn | GNBi | SEER GNB cohort (n=1,194) |
|---|---|---|---|---|
| Adrenal | 55.0% | 20.0% | 42.0% | 29.9% |
| Retroperitoneum (extra-adrenal) | 29.0% | 50.0% | 13.0% | 12.1% |
| Thorax / mediastinum | 9.0% | 30.0% | 26.0% | 14.5% (heart/mediastinum) |
| Soft tissue (SEER coding) | — | — | — | 37.4% |
| Other | 7.0% | 0% | 6.0% | 6.0% |

*Left columns: He WG, et al. Oncotarget. 2017. **PMID: 28465480**. Right column: Li W, et al. Heliyon. 2024;10(9):e30891. **PMID: 38774105**. The two site taxonomies are not aligned — SEER's "soft tissue" category absorbs paraspinal and other extra-adrenal sympathetic-chain sites that the clinical series splits out — so do not merge these rows.*

**Rare sites reported:** cervical (McGann EK, et al. Auris Nasus Larynx. 2022. **PMID: 33867181**), pelvic/organs of Zuckerkandl (Masrani N, et al. J Indian Assoc Pediatr Surg. 2025. **PMID: 41293519**), cervicothoracic dumbbell with spinal canal involvement (**PMID: 42811141**).

**Secondary organ involvement (GNBn / metastatic only):** bone marrow, bone, liver, distant lymph nodes, skin; rarely CNS and skull (Vandenhoudt W, et al. Front Oncol. 2026. **PMID: 42597467**).

**Body systems:** sympathetic/autonomic nervous system (primary); endocrine (adrenal medulla, catecholamine axis); gastrointestinal (VIP-mediated); haematopoietic (marrow metastasis); skeletal; cardiovascular (hypertension, hypertensive cardiomyopathy).

**UBERON suggestions** (all ✅ verified via OLS4):

| Structure | UBERON |
|---|---|
| adrenal medulla | **UBERON:0001236** |
| adrenal gland | **UBERON:0002369** |
| sympathetic nervous system | **UBERON:0000013** |
| sympathetic ganglion | **UBERON:0001806** |
| paravertebral ganglion | **UBERON:0001807** |
| thoracic ganglion | **UBERON:0000961** |
| cervical ganglion | **UBERON:0001991** |
| superior cervical ganglion | **UBERON:0001989** |
| cervicothoracic (stellate) ganglion | **UBERON:0002441** |
| lumbar ganglion | **UBERON:8600121** |
| sacral ganglion | **UBERON:8600122** |

⚠ **Requires lookup before binding:** UBERON terms for *posterior mediastinum*, *retroperitoneal space*, *organ of Zuckerkandl / para-aortic body*, *bone marrow*.

### 7.2 Tissue and cell level

- **Tissues:** nervous tissue (peripheral autonomic); connective/stromal tissue (the Schwannian stroma, which is *non-neoplastic*); adrenal medullary tissue.
- **Neoplastic cell populations:** neuroblasts at varying differentiation grades (CL:0000031 ✅, CL:0002676 ✅), ganglion cells (differentiated neoplastic progeny — ⚠ CL term for *ganglion cell* / *autonomic neuron* requires lookup; CL:0011103 sympathetic neuron ✅ is the closest verified term).
- **Non-neoplastic but definitional population:** Schwann cells (CL:0002573 ✅) and Schwann cell precursors (CL:0002375 ✅). **Recording these as "tumour cell types" would be an error** given **PMID: 25081755**; they should be recorded as stromal/microenvironment participants.

### 7.3 Subcellular level

No GNB-specific subcellular compartment is implicated. Relevant compartments by driver: **nucleus** (MYCN, PHOX2B, ATRX, telomeres), **plasma membrane** (ALK, TrkA, GD2), **neuritic processes/neuropil** (the morphological readout of differentiation). ⚠ GO Cellular Component terms for these require lookup before binding.

### 7.4 Localisation and lateralisation

Typically **unilateral and solitary**. Bilateral or multifocal primaries occur in **3–4% of neuroblastoma cases** and are a flag for germline predisposition (**PMID: 38860978**). A worked bifocal sporadic GNB case in which the two lesions had *different* histological subtypes (GNBi thoracic, GNBn abdominal) is reported and is directly relevant to curation: Montante C, et al. *The Pitfall of Ganglioneuroblastoma-Nodular Diagnosis.* Diagnostics. 2022. **PMID: 36553228**.

---

## 8. Temporal Development

### 8.1 Onset

- **Age.** Infancy to early childhood, with GNB subtypes diagnosed later than neuroblastoma (median 38.4 months GNBn, 47.5 months GNBi vs 28.9 months NB — **PMID: 28465480**). SEER GNB mean age **6.15 years** (SD ±9.65), with a long adult tail (**PMID: 38774105**). For neuroblastic tumours overall, "About 37% of patients are diagnosed as infants, and 90% are younger than 5 years at diagnosis, with a median age at diagnosis of 17 months" (NCI PDQ).
- **Onset pattern.** Usually **insidious** — an incidentally discovered or slowly enlarging mass. Acute presentations occur with cord compression, OMAS, or secretory diarrhoea.
- **Congenital/perinatal disease occurs** and is usually favourable: "The vast majority of the perinatal tumors exhibit favorable biologic features (<5% MYCN amplified, >95% favorable histology), and outcomes in these patients are excellent, with a four-year EFS of 92% and OS of 96%."

### 8.2 The age-linked prognostic framework (INPC)

This is the central temporal fact about GNB and should be modelled explicitly: **the same histology means different things at different ages.** Reproduced verbatim from ICCR Table 2 (International Neuroblastoma Pathology Committee Classification of neuroblastic tumours):

| Histologic type | Differentiation | MKI | Age | Histology |
|---|---|---|---|---|
| Neuroblastoma | Undifferentiated | Any | Any | **Unfavourable** |
| | Poorly differentiated | Low or Intermediate | <18 months | **Favourable** |
| | | | ≥18 months | **Unfavourable** |
| | | High | Any | **Unfavourable** |
| | Differentiating | Low | <5 years | **Favourable** |
| | | | ≥5 years | **Unfavourable** |
| | | Intermediate | <18 months | **Favourable** |
| | | | ≥18 months | **Unfavourable** |
| | | High | Any | **Unfavourable** |
| **Ganglioneuroblastoma, nodular** (and other composite neuroblastic tumours) | *Classify according to highest grade nodule or component of tumour* | | | |
| **Ganglioneuroblastoma, intermixed** | NA | NA | Any | **Favourable** |
| Ganglioneuroma | NA | NA | Any | **Favourable** |

**MKI definition (ICCR Note 9, verbatim):** "Mitotic-karyorrhectic index (MKI) is the number of mitotic nuclei and karyorrhectic nuclei per 5,000 neuroblastic cells." Classes: **Low MKI (<100/5,000 cells), Intermediate MKI (100–200/5,000 cells), High MKI (>200/5,000 cells)**.

Two procedural constraints that matter for data quality: "MKI determination on bone marrow metastases is discouraged, as it has not been shown to correlate with the MKI of the primary tumour nor to be prognostically useful," and "**MKI should not be determined for post-treatment tumours.**"

**Age cut-offs are empirically derived, not conventional.** Breslow and McCann's 365-day cut-off was superseded by London et al's analysis of 3,666 patients identifying **547 days**, and the INPC committee's 1999 review of 227 cases independently supported **1.5 years** plus a second cut-off at **5 years** (ICCR Note 1). The MKI-class-specific optima are different again: <60 months for low MKI, <18 months for intermediate, and possibly 3–4 months for high MKI (**PMID: 25207821**).

### 8.3 Progression and staging

**INRGSS** (pretreatment, image-based — Monclair T, et al. J Clin Oncol. 2009;27(2):298-303):

- **L1** — localised, no image-defined risk factors (IDRFs)
- **L2** — locoregional with ≥1 of 20 IDRFs
- **M** — metastatic
- **MS** — metastases confined to skin, liver and/or bone marrow in children **<18 months**

5-year EFS and OS by INRGSS stage (NCI PDQ): **L1 90% / 98%; L2 84% / 95%; M 52% / 64%; MS 86% / 92%.**

**Progression rate.** GNBi/GN are slow-growing; GNBn behaves per its nodule. In the German GN/GNBi series, "Five patients (3 GN, 2 GNBI) showed local progression; all had tumor residuals > 2 cm. No progression occurred after subtotal resection" (**PMID: 27465021**) — a result that reads oddly on first encounter and is worth stating carefully: progression occurred only in patients with *large* residua, not after subtotal resection generally.

**Disease course.** For GNBi: typically a single episode, cured or stably observed. For GNBn: the neuroblastoma course — risk-stratified, with relapse risk concentrated in stage 4 / ≥18 months.

### 8.4 Remission and maturation patterns

Three distinct phenomena must be kept apart:

1. **Spontaneous regression** — tumour disappearance, classically in infants with stage MS/4S disease. "The spontaneous regression usually consists of complete disappearance of the disease, but in some neuroblastomas, maturation to ganglioneuroma takes place" (Evans AE, Gerson J, Schnaufer L. Natl Cancer Inst Monogr. 1976. **PMID: 1030781**). Mechanism: "delayed activation of developmentally programmed cell death regulated by the tropomyosin receptor kinase A (TrkA) pathway" (**PMID: 29305654**), with HOXC9 induction of intrinsic apoptosis also implicated (Kocak H, et al. Cell Death Dis. 2013. **PMID: 23579273**).
2. **Spontaneous maturation** — progressive differentiation along NB → GNB → GN. This is the process that *creates* GNB.
3. **Therapy-induced maturation** — ICCR Note 1, verbatim: "Undifferentiated and poorly differentiated neuroblastomas, as well as ganglioneuroblastomas, may undergo maturation in response to therapy, with increased differentiation of neuroblasts, increased stromal content, and lower mitotic-karyorrhectic index (MKI). The INPC classification was designed to categorise and risk-stratify **pre-treatment** neuroblastic tumours and, because of the potential for therapy-induced changes, is not suitable for use with post-treatment tumours."

**This third point is a hard constraint on how GNB data may be used.** A post-chemotherapy specimen that looks like GNB may be a treated neuroblastoma, and must be reported as "neuroblastic tumour, post-treatment" — "Tumours should never be reclassified after treatment." A knowledge base that records a GNB diagnosis without recording whether the specimen was pre- or post-treatment is recording an ambiguous fact. The same trap exists outside the family: a periadrenal Ewing sarcoma has been reported with "chemotherapy-induced cytodifferentiation resembling ganglioneuroblastoma" (**PMID: 42138624**).

### 8.5 Critical periods

- **18 months** — the dominant risk-stratification threshold.
- **5 years** — the second INPC threshold, for differentiating tumours.
- **First 6 months of life** — the window in which expectant observation of small adrenal masses is validated (COG ANBL00P2 / NCT00445718).
- **Biopsy timing** — sampling error in GNBn is a critical-period problem of a different kind; see §10.

---

## 9. Inheritance and Population

### 9.1 Epidemiology

**Neuroblastic tumours overall (NCI PDQ):** "More than 650 cases are diagnosed each year in the United States"; prevalence ≈ **1 per 7,000 live births**; incidence **8.3 per 1,000,000 children under 15 per year**. A SEER analysis of 1,224 patients (2010–2018) reported an age-adjusted incidence of **8.2 per 1,000,000 children** (**PMID: 37046344**).

**GNB specifically.** No authoritative standalone incidence figure exists. Two anchors:

- GNB accounted for **15.86%** of childhood and **23.40%** of adolescent/adult neuroblastic tumours in SEER 1975–2013 (Yan P, et al. Med Sci Monit. 2020. **PMID: 33249420**).
- **Derived estimate (clearly labelled as derived, not cited):** 8.3/10⁶/yr × ~16% ≈ **1.3 per 1,000,000 children per year**. A frequently repeated secondary-source figure of "no more than 5 cases per million children" circulates without a traceable primary citation and **should not be used as a sourced claim**.

**SEER GNB cohort characteristics** (Li W, et al. Heliyon. 2024;10(9):e30891. **PMID: 38774105**; n = 1,194, SEER registries 1975–2019):

- Mean age **6.15 years** (SD ±9.65)
- Sex: **56.3% female / 43.7% male** — note this is the *reverse* of neuroblastoma's slight male predominance
- Race: White 78.8%, Black 12.6%, other 8.5%
- SEER stage: localised 48.1%, regional 31.7%, distant 20.2%
- Mean tumour size **68.6 mm** (SD ±38.0)
- Surgery 95.6%, chemotherapy 32.9%, radiotherapy 11.2%
- OS: **3-year 73.9%, 5-year 61.2%, 10-year 40.8%**

**Reconciling an apparent contradiction.** The SEER 5-year OS of 61.2% sits well below the 88% and 74.5–100% figures quoted elsewhere. The discrepancy is explained by cohort composition: the SEER cohort spans 1975–2019 (including the pre-modern-therapy era) and has a mean age of 6.15 years with a substantial adult component, whereas the clinical series are contemporary paediatric cohorts. **Do not average these numbers.** Record each with its cohort.

### 9.2 Inheritance

- **The disease itself is not inherited.** 98–99% of cases are sporadic somatic neoplasms.
- **Predisposition inheritance where present:** autosomal dominant with **incomplete penetrance** (ALK, PHOX2B).
- **Penetrance:** incomplete and not well quantified for either gene. ALK germline variants vary in penetrance by specific allele.
- **Expressivity:** variable — PHOX2B germline variants may present as isolated neuroblastic tumour, Hirschsprung disease, CCHS, or combinations. The Orphanet concept **Hirschsprung disease–ganglioneuroblastoma syndrome (ORPHA:2151)** names the combination explicitly and is a distinct entity from MONDO:0005035; do not merge them.
- **Genetic anticipation:** not applicable (no repeat expansion).
- **Germline mosaicism:** **no data found** for ALK or PHOX2B in a GNB context.
- **Founder effects:** **TP53 p.R337H** in the Brazilian population is a recognised neuroblastoma-risk founder allele for which PDQ recommends surveillance; no GNB-specific founder effect is described.
- **Consanguinity:** no established role.
- **Carrier frequency:** not established; germline ALK/PHOX2B variants are too rare for a meaningful population carrier estimate.

### 9.3 Population demographics

- **Ancestry:** neuroblastoma incidence highest in non-Hispanic White children (RRs in §2.3). **No GNB-specific ancestry analysis exists.**
- **Geographic distribution:** no endemic pattern. Regional variation reflects registry ascertainment. "Analysis of the SEER program database between 1975 to 2013 showed that in the U.S., the incidence of neuroblastoma in children increased, but the incidence decreased in adolescents and adults" (**PMID: 33249420**).
- **Sex ratio:** SEER GNB **0.78 M:F** (43.7% male) — female-predominant, in contrast to neuroblastoma, where metastatic cases are male-enriched (**PMID: 37046344**). This difference is reported but not explained; treat it as an observation, not a mechanism.
- **Age distribution:** see §8.1 and §9.1. Adults are a real if small group, and they do worse: adolescent/adult patients "demonstrated worse overall survival than pediatric cases" despite earlier stage (**PMID: 33249420**); "the prognosis of children with GNB was better than that of adolescents and adults with GNB" (**PMID: 38774105**).

---

## 10. Diagnostics

### 10.1 The diagnostic reality for GNB: histology decides, and sampling is the weak link

GNB cannot be diagnosed by imaging or biochemistry. It is a **resection-specimen diagnosis**, and the ICCR states the sampling hazard plainly (Note 10):

> "Ganglioneuroblastoma, nodular, and other composite neuroblastic tumours are classified by applying the INPC schema to the highest grade nodule or component of the tumour. When a biopsy or partial resection is performed, there exists a risk of failing to sample an unfavourable nodule or component of these two tumour types; thus, in such cases, a disclaimer about limited sampling should be made."

The published consequence of this is a documented failure mode: "areas of GNBI and GNBN can coexist in the same mass, leading to incorrect risk staging when only biopsy is performed" (**PMID: 36553228**). And it works in the other direction too — the UK CCLG national study found "a small proportion of patients in the observation group had their diagnosis revised to malignant at surgery" (**PMID: 39582110**). A serial-biopsy pattern is itself diagnostic evidence: "an initial biopsy that has mature ganglion cells in a stroma-rich background and a second biopsy with poorly differentiated neuroblasts and scant stroma would suggest a ganglioneuroblastoma, nodular" (ICCR Note 1).

### 10.2 Laboratory tests and biomarkers

| Test | Finding | Performance notes |
|---|---|---|
| Urinary **VMA** and **HVA** (per mg creatinine) | Elevated | "Urinary excretion of the catecholamine metabolites VMA and HVA per milligram of excreted creatinine is measured before therapy" (NCI PDQ). **But abnormal in only 21% of GNBn and 19% of GNBi** vs 59% of NB (**PMID: 28465480**) — a poor rule-out for GNB |
| Serum **NSE** | Elevated in 93% GNBn, 81% GNBi, 96% NB | **PMID: 28465480** |
| Serum **LDH** | Elevated in 90% GNBn, 85% GNBi, 97% NB | **PMID: 28465480** |
| Serum **ferritin** | Elevated in 40% GNBn, 12% GNBi, 60% NB | **PMID: 28465480** |
| Plasma/urine metanephrines | Usually normal | Relevant in distinguishing composite pheochromocytoma–GNB (**PMID: 42571973**; J Endocr Soc 2021, PMC8265703) |
| **VIP** | Elevated in the WDHA subset | Measured only when the syndrome is suspected |

⚠ **LOINC codes for VMA, HVA, NSE, LDH, ferritin and VIP were not looked up in this session** and must not be written from memory.

### 10.3 Imaging

| Modality | Role | Evidence |
|---|---|---|
| **CT / MRI with contrast** | Primary anatomical staging; determines the 20 image-defined risk factors that set L1 vs L2 | Monclair T, et al. JCO 2009 |
| **¹²³I-MIBG scintigraphy / SPECT** | Functional imaging; "About 90% of neuroblastoma cases are MIBG avid" (NCI PDQ). **GNB is frequently MIBG-negative** — e.g. an adrenal GNBi "negative at MIBG scintigraphy" (**PMID: 34306280**); a GNB diaphragmatic metastasis FDG-positive but "negative on MIBG scintigraphy" (**PMID: 40065424**) | — |
| **¹⁸F-FDG PET/CT** | Used where MIBG is negative; also predicts INPC class and MKI by radiomics (**PMID: 36620179**; **PMID: 35204353**) | — |
| **⁶⁸Ga-DOTATATE PET/CT** | Head-to-head prospective comparison in CNS metastases of NB and GNB: "⁶⁸Ga-DOTATATE PET/CT exhibited superior performance" and "led to changes in clinical management in 51% of patients" | Li S, et al. Eur J Nucl Med Mol Imaging. 2025. **PMID: 40637785** |
| **¹⁸F-MFBG PET/CT** | Emerging; a multiparametric model integrating ¹⁸F-MFBG parameters with clinical factors differentiated NB from GNB with **AUC 0.856** | Wang X, et al. Eur J Nucl Med Mol Imaging. 2026. **PMID: 42820950** |
| **CT radiomics + deep learning** | Differentiating NB from GNB preoperatively: **AUC 0.922 training / 0.913 validation** | Zhang G, et al. BMC Cancer. 2026. **PMID: 41652556** |

**A caution on the radiomics literature:** these are retrospective single-centre models without external validation, and the GNB arms are small. They are promising leads, not validated diagnostics, and the authors of **PMID: 42820950** say so ("external validation in larger cohorts remains necessary").

### 10.4 Histopathology and immunohistochemistry

**Gross:** the GNBn nodule is "grossly identifiable and often haemorrhagic/necrotic and fragile"; the GNBi/GN component is "tan-yellow and solid/elastic" (ICCR Note 7).

**Microscopic:** the defining discriminator between a differentiating neuroblast and a ganglion cell is whether neuritic processes are **naked** (neuropil visible on H&E, not covered by Schwann cells) or fully ensheathed. Degree of differentiation (ICCR Note 8): **undifferentiated** (no neuritic process, requires ancillary tests, sometimes "starry-sky"), **poorly differentiated** (<5% differentiating cells, Homer Wright rosettes may be present), **differentiating** (>5% of tumour cells with synchronous nuclear and cytoplasmic differentiation).

**Immunohistochemistry (ICCR Note 13, verbatim):**

> "Phox2B is one of the most sensitive and specific markers for neuroblastoma, although it is also positive in other neural crest-derived tumours such as paraganglioma/pheochromocytoma. Additional stains typically positive in neuroblastic tumours include PGP9.5, CD56, and NB84. The neuroblastic cells are usually positive for synaptophysin and neuron-specific enolase and the Schwannian stromal cells are usually positive for S100 (although these stains are of limited utility due to their nonspecific nature)."

Additional: chromogranin and tyrosine hydroxylase in neuroblasts; S100 in both Schwann cells and ganglion cells. **PHOX2B is positive across all of neuroblastoma, ganglioneuroblastoma and ganglioneuroma** — it establishes lineage, not category.

### 10.5 Genetic testing

- **Tumour testing (required):** MYCN amplification status by FISH on FFPE or frozen tissue (ratio ≥4 = amplified), DNA index/ploidy, segmental chromosomal aberrations at 1p and 11q (and 17q). "Determination of MYCN amplification status is a critical part of risk stratification for peripheral neuroblastic tumours" (ICCR Note 14).
- **ALK:** sequencing of the kinase domain/hotspots — **not** immunohistochemistry (ICCR Note 13).
- **Germline testing:** indicated where family history, bilateral/multifocal tumours, or associated features (Hirschsprung disease, CCHS) are present. Panel covering at minimum ALK and PHOX2B.
- **Platform-specific utility:** NGS panels and SNP/CGH arrays now commonly substitute for FISH for MYCN and cover SCAs in one assay. WGS/WES are research or refractory-case tools, not standard. CMA, karyotyping, mitochondrial DNA testing and repeat-expansion testing have **no role** in GNB.

### 10.6 Omics-based diagnostics

- **Liquid biopsy / ctDNA** is clinically validated for *ALK resistance tracking*, not for GNB diagnosis: serial ctDNA identified acquired resistance in 27% of patients on the lorlatinib trial, "predominantly off-target resistance mutations in the RAS-MAPK pathway," with secondary compound ALK mutations in 15% at progression (Berko ER, et al. Nat Commun. 2023. **PMID: 37147298**).
- Transcriptomic, proteomic, metabolomic and epigenomic diagnostics: **not in clinical use for GNB.**

### 10.7 Clinical criteria and differential diagnosis

There are no society "diagnostic criteria" in the DSM sense; the INPC *is* the criterion set. Reporting is standardised by the **ICCR Neuroblastoma Histopathology Reporting Guide (1st ed., Nov 2023)** and the CAP neuroblastoma protocols.

**Differential diagnosis:**

| Entity | Distinguishing features |
|---|---|
| Neuroblastoma (stroma-poor) | <50% Schwannian stroma |
| Ganglioneuroma | No neuroblastic foci with naked neuritic processes |
| Pheochromocytoma / paraganglioma | Also PHOX2B-positive; composite pheochromocytoma–GNB exists (**PMID: 42571973**) |
| Ewing sarcoma (esp. post-chemotherapy) | EWSR1 rearrangement; may mimic GNB morphologically after treatment (**PMID: 42138624**) |
| Other small round blue cell tumours (rhabdomyosarcoma, lymphoma, desmoplastic small round cell tumour, Wilms tumour) | PHOX2B, synaptophysin, NB84 panel; HuC/D is useful (ScienceDirect, Hum Pathol 2018) |
| MPNST arising in GN/GNB | A recognised malignant transformation (**PMID: 41490645**) |
| **Treated neuroblastoma** | Cannot be reclassified — see §8.4 |

### 10.8 Screening

See §13. **Population screening is not recommended.**

---

## 11. Outcome / Prognosis

### 11.1 Survival — by subtype, which is the only way these numbers mean anything

| Cohort | n | Outcome |
|---|---|---|
| **GNBi**, single-centre | 31 | **5-year OS 100%** (median survival 64.5 months) — **PMID: 28465480** |
| **GNBn**, single-centre | 20 | **5-year OS 74.5% ± 11.4%** — **PMID: 28465480** |
| Neuroblastoma, same centre | 228 | 5-year OS 50.8% ± 4.5% — **PMID: 28465480** |
| **GNBn**, INRG project | ~250 | **EFS 54% ± 5%, OS 68% ± 5%** — **PMID: 22137163** |
| GNBn <18 months, INRG | 39 | **OS 95% ± 5%** |
| GNBn stage 1/2/3/4s, INRG | 125 | **OS 95% ± 3%** |
| **GNBn stage 4, INRG** | 107 | **OS 35% ± 7%** |
| **GNBn favourable subset (FS)** | 22 | 5-year EFS **86.1%**, survival **95.0%** — **PMID: 10964346** |
| **GNBn unfavourable subset (US)** | 46 | 5-year EFS **29.0%**, survival **40.7%** — **PMID: 10964346** |
| GNBn FS vs US, revision study | 22 vs 45 | 8-year EFS **86.1% vs 32.2%** (P=0.0003); OS **90.5% vs 33.2%** (P=0.0003) — **PMID: 14601099** |
| **All GNB, SEER 1975–2019** | 1,194 | OS **3-yr 73.9%, 5-yr 61.2%, 10-yr 40.8%** — **PMID: 38774105** |

The verbatim conclusion of the INRG GNBn report is the single best summary statement available:

> "Patients with GNBn tumours are rare and have a very heterogeneous outcome. Except for LDH and MKI, the factors prognostic in the overall NB cohort are also prognostic in patients with GNBn. Similar to the overall NB cohort, patients with GNBn older than 18 months of age, with stage 4 disease represent a high-risk sub-group and should be considered for aggressive treatment upfront." — Angelini P, et al. Eur J Cancer. 2012. **PMID: 22137163**

And the finding that overturned the original Shimada position:

> "The current study demonstrates that the nodular components in GNBn tumors are **not always aggressive**. The prognosis of these patients can be determined by the analysis of age-linked histopathologic features." — Umehara S, et al. Cancer. 2000;89(5):1150. **PMID: 10964346**

### 11.2 Independent prognostic factors

From the SEER multivariable Cox model (n = 1,194; **PMID: 38774105**): "Five independent prognostic factors, including age, primary tumor site, SEER stage, surgery and chemotherapy, were screened out and included in the nomogram."

| Factor | HR (95% CI) | P |
|---|---|---|
| Age (per year) | 1.05 (1.04–1.06) | <0.001 |
| Soft tissue vs adrenal | 0.33 (0.17–0.65) | 0.001 |
| Heart/mediastinum vs adrenal | 0.49 (0.22–1.08) | 0.08 |
| Retroperitoneum vs adrenal | 0.62 (0.35–1.11) | 0.11 |
| Other site vs adrenal | 2.01 (1.15–3.50) | 0.01 |
| Localised vs distant | 0.19 (0.10–0.36) | <0.001 |
| Regional vs distant | 0.28 (0.16–0.49) | <0.001 |
| Surgery (yes vs no) | 0.51 (0.28–0.95) | 0.03 |
| **Chemotherapy (yes vs no)** | **2.14 (1.19–3.86)** | **0.01** |

Model performance: C-index 0.862 (development) / 0.827 (validation).

**The chemotherapy HR of 2.14 must not be read as harm from chemotherapy.** This is confounding by indication in a registry model: chemotherapy is given to the patients with worse disease. The correct reading is that chemotherapy receipt is a *marker* of adverse biology in this cohort. Any knowledge-base statement derived from this row needs that caveat attached, or it will be read as a treatment-effect claim.

Prognostic factors from the pathology side (Sokol E, et al. J Clin Oncol. 2020. **PMID: 32315273**, INRG Data Commons, cohorts of 10,104 and 8,761): "age, histologic category, MKI, and differentiation grade" are each **independently** prognostic, and the authors argue that "Replacing INPC with individual histologic features eliminates confounding and facilitates international harmonization of risk classification."

### 11.3 Prognostic biomarkers

- **MYCN amplification** — the single most important molecular marker in pNTs. **Its prognostic force in GNB is unsettled**: GNB series report either no clear adverse effect or an effect their sample size cannot resolve, and the authors say so explicitly. Record this as an open question, not as an established GNB prognostic marker.
- **Telomere maintenance mechanism activation** — active in 48% of GNBn and described as "a poor prognostic marker" (**PMID: 41858373**). The most promising GNB-specific prognostic biomarker currently available.
- **Segmental chromosomal aberrations** (1p, 11q, 17q) — prognostic pNT-wide (Schleiermacher G, et al. Br J Cancer. 2012;107(8):1418-1422).
- **ALK amplification** (not mutation) — adverse (**PMID: 36807339**).
- **SCP signature score** — "a high SCP signature score is associated with better overall survival rates" (**PMID: 33500353**).

### 11.4 Morbidity, complications, and recovery

**Complications of disease:** cord compression and permanent neurological deficit; hypertensive cardiomyopathy; chronic diarrhoea with electrolyte derangement; OMAS with long-term neurocognitive impairment.

**Complications of treatment:** major surgical morbidity, including vascular catastrophe — "Delayed rupture of the celiac trunk and superior mesenteric artery associated with pancreatic leakage after resection of a giant retroperitoneal ganglioneuroblastoma in a child" (Dai X, et al. Transl Pediatr. 2026. **PMID: 42158706**). Secondary malignancy: therapy-related AML with inv(16) after GNB chemotherapy (Yuan J, et al. Clin Lab. 2025. **PMID: 41078182**). Malignant transformation to MPNST from GN/GNB (**PMID: 41490645**). In the German GN/GNBi series, "two patients died of treatment, none of tumor progression" (**PMID: 27465021**) — the cleanest available statement of the risk–benefit case for observation.

**Recovery potential:** excellent for GNBi and for localised GNBn in young children; poor for stage-4 GNBn ≥18 months.

**Late effects:** see §3.4.

---

## 12. Treatment

### 12.1 Treatment is decided by subtype, not by the word "ganglioneuroblastoma"

This is the operational consequence of everything above and is the most important treatment fact to record.

### 12.2 Ganglioneuroma and ganglioneuroblastoma, intermixed

**Surgery, often conservative; observation is a validated option; chemotherapy does not work.**

- Decarolis B, et al. *Treatment and outcome of Ganglioneuroma and Ganglioneuroblastoma intermixed.* BMC Cancer. 2016. **PMID: 27465021** — "GN/GNBI account for one quarter of localized NT and differ from immature tumors in their clinical features. **Chemotherapy is not effective. Subtotal resection appears to be a sufficient treatment.**"
- Burnand KM, et al. *Management of Ganglioneuroma and Ganglioneuroblastoma Intermixed: A United Kingdom Children's Cancer and Leukaemia Group (UK CCLG) Nationwide Study Report.* Pediatr Blood Cancer. 2025. **PMID: 39582110** — "**Watchful active observation can be a safe approach, with surgical resection reserved for symptomatic patients**... a small proportion of patients in the observation group had their diagnosis revised to malignant at surgery."
- Alexander N, et al. Pediatr Blood Cancer. 2018. **PMID: 29369484** — "GN and GNB-I have a slow growth rate and resection can be associated with significant morbidity. **Watch and wait approaches should be considered** for some GN and GNB-I."
- Yang T, et al. Pediatr Surg Int. 2017. **PMID: 28608056** — "the residual tumor seems not to influence overall survival."
- Nourani M, et al. *Is There a Role for Chemotherapy in Unresectable Ganglioneuroblastoma Intermixed?* J Pediatr Hematol Oncol. 2026. **PMID: 41568977** — 12 patients; chemotherapy "offers limited benefit while posing significant risks"; "surgery should be prioritized."

### 12.3 Ganglioneuroblastoma, nodular

**Risk-stratified and treated exactly as neuroblastoma**, using the COG Revised Neuroblastoma Risk Classification (Irwin MS, et al. J Clin Oncol. 2021;39(29):3229-3241) — which uses INRGSS stage, age, MYCN status, INPC histology, ploidy, and segmental chromosomal aberrations at 1p and 11q, derived from 4,832 patients on ANBL00B1 (2007–2017).

**Low risk:** surgery alone, or observation. "Low-risk disease can frequently be observed without any treatment at all or cured with surgery alone." COG ANBL00P2 (NCT00445718) validated expectant observation in infants ≤6 months with solid adrenal masses <3.1 cm (or cystic <5 cm), INSS stage 1.

**Intermediate risk:** response- and biology-adapted chemotherapy of reduced intensity, plus surgery.

**High risk** — the full multimodal programme:

| Phase | Components | NCIT (✅ verified) |
|---|---|---|
| Induction | Multi-agent chemotherapy (cyclophosphamide, topotecan, cisplatin, etoposide, doxorubicin, vincristine) | ⚠ NCIT:C15632 Chemotherapy *requires lookup* |
| Local control | Gross total resection of the primary without mutilation; external-beam RT to the tumour bed | ⚠ requires lookup |
| Consolidation | High-dose myeloablative therapy + autologous stem-cell transplant (tandem) | ⚠ requires lookup |
| Post-consolidation | **Isotretinoin** (13-*cis*-retinoic acid) | **NCIT:C603** ✅ / **CHEBI:6067** ✅ |
| | **Anti-GD2 monoclonal antibody**: dinutuximab, dinutuximab beta, or naxitamab + GM-CSF (±IL-2) | **NCIT:C1570** Dinutuximab ✅ |
| Maintenance | **Eflornithine (DFMO)** — ODC inhibitor | **NCIT:C226** Eflornithine ✅ / **CHEBI:41948** ✅ (regimen: **NCIT:C202976** ✅) |

**Eflornithine** was approved by the FDA on **13 December 2023** (brand IWILFIN, USWM LLC) "to reduce the risk of relapse in adult and pediatric patients with high-risk neuroblastoma (HRNB) who have demonstrated at least a partial response to prior multiagent, multimodality therapy including anti-GD2 immunotherapy" — the first FDA approval of a relapse-risk-reduction therapy in paediatric HRNB. At four years post-immunotherapy, EFS was **84% (eflornithine) vs 73% (external control)**, OS **96% vs 84%** (FDA approval summary, PubMed **38917371**; prescribing information, accessdata.fda.gov/drugsatfda_docs/label/2024/215500s001lbl.pdf).

**Anti-GD2 immunotherapy** raised 2-year EFS in HRNB from **46% to 66%**. Cytokine support: "clinical data supporting the use of G-CSF are limited," with **GM-CSF** the preferred adjuvant (Mora J, et al. Int J Cancer. 2024. **PMID: 38108214**).

### 12.4 Relapsed / refractory disease

| Regimen | Outcome | Reference |
|---|---|---|
| Irinotecan/temozolomide/dinutuximab/GM-CSF | 49% objective response (29% CR, 14% PR); median PFS 13.1 months | Lerman BJ, et al. J Clin Oncol. 2023. **PMID: 36206505** |
| Dinutuximab beta + topotecan-cyclophosphamide vs temozolomide-based | ORR 42% vs 40% — "the importance of chemo-immunotherapy, **irrespective of the chemotherapy backbone**" | Raiser P, et al. Eur J Cancer. 2024. **PMID: 38489858** |
| Naxitamab + irinotecan/temozolomide + GM-CSF (HITS), **early** salvage | 47% CR (early) vs 12% (late); 3-year EFS 54.4% | Muñoz JP, et al. Cancers. 2023. **PMID: 37835531** |
| Dinutuximab beta monotherapy ± isotretinoin (systematic review, 442 patients) | Best response 28.6–54.8%; 3-year OS 54–86% | Wieczorek A, et al. Target Oncol. 2025. **PMID: 40459700** |

### 12.5 Targeted and advanced therapeutics

**ALK inhibition — the one genotype-directed therapy in this disease:**

> "This phase 1 trial evaluated lorlatinib monotherapy and combination treatment in children and adults with relapsed/refractory ALK-driven neuroblastoma. The study established recommended phase 2 doses and demonstrated response rates varying by age group (30% in children as monotherapy; 67% in adults; 63% with chemotherapy combination). Common adverse events included hypertriglyceridemia (90%), hypercholesterolemia (79%), and weight gain (87%). The findings supported 'rapid translation into active phase 3 trials for patients with newly diagnosed high-risk, ALK-driven neuroblastoma.'"
> — Goldsmith KC, Park JR, Kayser K, et al. *Lorlatinib with or without chemotherapy in ALK-driven refractory/relapsed neuroblastoma: phase 1 trial results.* Nat Med. 2023;29(5):1092-1102. **PMID: 37012551**

**Investigational / preclinical:**

- **ALK + ATR inhibition** — "Combined 14-day ALK/ATR inhibition produced robust and sustained response, with tumor cell reprogramming toward neuronal/Schwann cell differentiation" (Borenäs M, et al. PNAS. 2024. **PMID: 38154064**). *Mechanistically notable for GNB: this is a drug combination whose response phenotype is the GNB morphology.*
- **ALK + MDM2 (idasanutlin)** — "lorlatinib combined with idasanutlin resulted in complete tumor regression and significantly delayed tumor regrowth" in ALK-amplified PDX (Tucker ER, et al. Clin Cancer Res. 2023. **PMID: 36602782**)
- **ALK.CAR-T + ALK inhibitors** — ALK inhibitors upregulate ALK surface expression and "specifically potentiate ALK.CAR-T cells but not GD2.CAR-T cells" (Bergaggio E, et al. Cancer Cell. 2023. **PMID: 38039964**)
- **Anti-GD2 ADC M3554** (dinutuximab–exatecan conjugate; NCIT:C212045)

**Gene therapy, RNA-based therapy (ASO/siRNA/mRNA):** **no approved or late-phase agent for this disease.** This is a genuine absence, not a search gap.

**Pharmacogenomics:** no CPIC/PharmGKB guideline specific to neuroblastoma therapy. The clinically relevant pharmacogenomic issue is **cisplatin-induced ototoxicity** (TPMT/COMT variants have been proposed and contested) — flagged here as a lead requiring its own literature review before any claim is made.

### 12.6 Supportive, surgical, and rehabilitative care

- **Surgery.** The ICCR summarises current surgical philosophy precisely: "In most studies of advanced stage neuroblastoma, the degree of primary tumour resection has shown no impact on local control or long-term outcomes unless metastatic disease can be controlled. Thus, the aim should be gross total resection without mutilation and surgical sequelae. For these reasons, tumour presence at surgical margins is not usually assessed pathologically." (Note 2)
- **Supportive care:** pain control (particularly anti-GD2 infusion pain, which is substantial and expected), antihypertensives for catecholamine excess, electrolyte replacement in VIP syndrome, transfusion support.
- **Rehabilitation:** physiotherapy after cord compression; **audiological surveillance and hearing aids/cochlear devices** given 72% moderate-to-severe hearing loss in HRNB survivors; neurodevelopmental and educational support, especially after OMAS.
- **OMAS-directed immunotherapy:** in ANBL00P3, "21 of 26 patients (81%) in the IVIG group had an opsoclonus/myoclonus ataxia syndrome response" versus "11 of 27 patients (41%) in the non-IVIG group" (NCI PDQ).

### 12.7 Treatment strategy

Treatment algorithms are published by COG (RNRC-based), SIOPEN (HR-NBL1/SIOPEN), and in the NCCN/NCI PDQ. The decision tree for GNB specifically is:

1. Confirm subtype on **adequate** tissue, with a sampling disclaimer if biopsy-only.
2. **GNBi/GN** → observe or resect; **do not give chemotherapy**.
3. **GNBn** → assign a COG/INRG risk group using INRGSS stage, age, MYCN, INPC histology (graded on the **highest-grade nodule**), ploidy, and 1p/11q → treat per risk group.
4. At relapse → ALK sequencing; lorlatinib if ALK-driven; chemo-immunotherapy otherwise.

---

## 13. Prevention

### 13.1 Primary prevention

**None exists and none is plausible with current knowledge.** There is no modifiable risk factor for GNB. Any statement implying otherwise would be unsupported.

### 13.2 Secondary prevention — and a landmark negative result

**Population newborn/infant screening by urinary catecholamine metabolites does not work and is not recommended.** This is one of the better-evidenced negative results in paediatric oncology and deserves to be recorded as a positive fact rather than an absence:

> "Current data do not support neuroblastoma screening in the general public." Screening trials showed that although "most infants in Quebec, Canada, were screened at the ages of 3 weeks and 6 months," this "did not lead to a reduced incidence of advanced-stage neuroblastoma with unfavorable biological characteristics." — NCI PDQ

The mechanism of that failure is informative: screening detects the favourable-biology tumours that would have regressed or matured on their own (i.e. it overdiagnoses the GNB/GN end of the spectrum) without detecting the unfavourable-biology tumours earlier.

### 13.3 Surveillance for genetically predisposed individuals

This **is** recommended, and is the only validated screening in this disease. For carriers of germline **ALK** or **PHOX2B** pathogenic variants, and for Li-Fraumeni syndrome with TP53 p.R337H (NCI PDQ):

- **Abdominal ultrasonography**, and
- **Quantitative, normalized assessment of urinary catecholamines**
- **every 3 months until age 6, then every 6 months until age 10**

Updated recommendations are in Kamihara J, et al. Clin Cancer Res. 2024. **PMID: 38860978**, which "review[s] recommended surveillance for hereditary patients with NB, including minor updates to surveillance recommendations that were published previously in 2017" (the 2017 source being Kamihara J, et al. Clin Cancer Res. 2017;23(13):e98-e106. **PMID: 28674118**).

### 13.4 Tertiary prevention

- **Eflornithine maintenance** to reduce relapse risk in HRNB (§12.3) is formally a tertiary-prevention intervention.
- **Late-effects surveillance:** audiology, growth and endocrine monitoring, cardiac function, renal function, second-malignancy surveillance, and neurocognitive/educational assessment — justified by the LEAHRN prevalence data.

### 13.5 Immunization, genetic counselling, public health, prophylaxis

- **Immunization:** **not applicable** — GNB has no infectious aetiology. (Anti-GD2 antibody therapy is passive immunotherapy, not a vaccine.)
- **Genetic counselling:** indicated for familial, bilateral/multifocal, or syndromic presentations; should cover autosomal dominant inheritance with incomplete penetrance, cascade testing, and the surveillance protocol above.
- **Public health / environmental interventions:** **not applicable.**
- **Prophylaxis:** no prophylactic medication or procedure.

---

## 14. Other Species / Natural Disease

### 14.1 Taxonomy

| Species | NCBITaxon | Evidence of naturally occurring GNB |
|---|---|---|
| *Homo sapiens* | NCBITaxon:9606 | — |
| *Canis lupus familiaris* (dog) | ⚠ NCBITaxon:9615 *(requires lookup)* | **Yes** — multiple reports |
| *Bos taurus* (cattle) | ⚠ NCBITaxon:9913 *(requires lookup)* | **Yes** — IHC series of peripheral neuroblastoma, ganglioneuroblastoma, anaplastic ganglioglioma, schwannoma and neurofibroma in cattle |
| *Equus caballus* (horse) | ⚠ *requires lookup* | Ganglioneuroma and ganglioneuromatosis reported; GNB not clearly documented |
| *Felis catus* (cat), *Sus scrofa* (pig) | ⚠ *requires lookup* | Peripheral ganglioneuromas reported; GNB not clearly documented |

**All NCBITaxon CURIEs above are unverified and must be looked up before binding.**

### 14.2 Natural disease in other species

Ganglioneuroblastoma is **rare in veterinary medicine**, and the diagnostic criteria are the same as in humans: "diagnosis requires clear, obvious ganglion cell differentiation, neuroblasts, and some amount of Schwann cells and Schwannian stroma."

Documented canine cases:

- **Olfactory ganglioneuroblastoma** — Romano AM, Frank CB. *Olfactory ganglioneuroblastoma in a dog: case report and literature review.* J Vet Diagn Invest. 2021. DOI: 10.1177/10406387211022864; and a companion IHC comparison with olfactory neuroepithelia and olfactory neuroblastomas (PMC11300123). **Note:** olfactory GNB is a CNS/neuroepithelial tumour, not a peripheral neuroblastic tumour — it is a homonym, not a homologue.
- **Primary cutaneous (footpad) peripheral ganglioneuroblastoma** — the first such report in a dog. **PMID: 30950551**. *This one is a genuine peripheral neuroblastic tumour.*
- Further canine reports in brain, oral mucosa, and thorax.

Bovine: a cutaneous ganglioneuroma case report, and an immunohistochemical series of bovine peripheral neuroblastoma/ganglioneuroblastoma.

**OMIA:** no Mendelian inheritance entry for ganglioneuroblastoma was identified in the Online Mendelian Inheritance in Animals database. These are sporadic neoplasms, not heritable traits — consistent with the human picture.

### 14.3 Orthologous genes

⚠ **NCBI Gene IDs for the mouse/rat/zebrafish orthologs of MYCN, ALK, PHOX2B, ATRX and TERT were not looked up in this session** and must not be written from memory. Note that *Phox2b* function is conserved across mouse and zebrafish (demonstrated in both — **PMID: 23754957**, **PMID: 19608868**), and *MYCN* function is conserved in mouse and zebrafish models.

### 14.4 Comparative biology

- **Conserved:** the neural-crest → sympathoadrenal developmental programme, PHOX2B's role as its master regulator, MYCN's dual proliferative/anti-differentiative effect, and the morphological spectrum from neuroblastoma to ganglioneuroma all hold across mammals.
- **Divergent / unexplained:** the **Schwannian-stroma-rich phenotype that defines GNB is poorly reproduced in any animal model** (see §15). This is the central comparative gap.

### 14.5 Transmission

**Not applicable.** GNB is a non-transmissible neoplasm with no zoonotic potential and no cross-species susceptibility.

---

## 15. Model Organisms

### 15.1 The defining limitation: there is no good ganglioneuroblastoma model

Every widely used model in this field is a **neuroblastoma** model, and the two most-characterised ones explicitly fail to produce the differentiated, stroma-rich phenotype that *is* ganglioneuroblastoma. A mechanism knowledge base should record this as a `HUMAN_MODEL_MISMATCH`-type gap rather than as an absence of models: the models exist and are excellent for neuroblastoma, but they are **boundary-omitting** with respect to GNB because the stromal compartment and the differentiation endpoint are outside what they reproduce.

### 15.2 Available models

| Model | Type | Construction | Phenotype recapitulation | Limitation for GNB |
|---|---|---|---|---|
| **TH-MYCN mouse** | Transgenic mammalian | Human *MYCN* cDNA under the rat tyrosine-hydroxylase promoter | Neuroblast hyperplasia in paravertebral ganglia at E14; **tumours in 100% of homozygotes from postnatal week 6**; "now the most widely used transgenic model in neuroblastoma research" | **Fails to model GNB.** "Tumors displayed heterogeneity of differentiation but **no overt ganglionic differentiation** was seen, with **low levels of Schwannian stroma** and a high mitosis karyorrhexis index." Hyperplastic neuroblasts "did not express differentiation markers, such as beta-III-tubulin or tyrosine hydroxylase." Weiss WA, et al. EMBO J. 1997;16(11):2985; histological profile, **PMID: 18682419**; genetic aberrations, PMC3524187 |
| **TH-MYCN × ALK<sup>F1174L</sup>** | Compound transgenic | ALK activating allele on MYCN background | Accelerated, more aggressive tumours; the standard ALK-inhibitor preclinical platform | Same differentiation/stroma gap |
| **Zebrafish dβh-MYCN** | Transgenic | MYCN under dopamine-β-hydroxylase promoter | Sympathoadrenal tumours; amenable to genetic screens | Same gap; also lacks mammalian adrenal architecture |
| **Zebrafish PHOX2B models** | Transgenic / morphant | Heterozygous deletion or dominant-negative PHOX2B | Models the **differentiation block itself**: "imposes a block in the differentiation of sympathetic neuronal precursors, resulting in a cell population that is likely to be susceptible to secondary transforming events" (**PMID: 23754957**) | Models the predisposing lesion, not the tumour |
| **Patient-derived xenografts (PDX)** | Xenograft | Implanted human tumour | Preserve genomics; the lorlatinib/idasanutlin platform (**PMID: 36602782**) | Derived from **neuroblastoma**, not GNB; and "xenografts with cells from each identity eventually harbor a noradrenergic phenotype suggesting that the microenvironment provides a powerful pressure towards this phenotype" (**PMID: 37142597**) — i.e. the host environment itself selects away from the heterogeneity being studied |
| **Cell lines** (SH-SY5Y, LA-N-1, SK-N-SH, etc.) | In vitro | Established human neuroblastoma lines | The workhorse for retinoic-acid differentiation biology (**PMID: 6467378**, **PMID: 7040765**) and HDAC8/ZNF423 work | **No ganglioneuroblastoma-derived cell line exists.** A GNB line is arguably not constructible, since the defining feature is a two-compartment tissue architecture |
| **Neuroblastoma–Schwann cell co-culture / Schwann-cell-conditioned medium** | In vitro | Co-culture or conditioned medium | **The closest thing to a GNB model.** Reconstitutes the tumour–stroma differentiation loop: neurite outgrowth and mature neurofilament induction (**PMID: 9788610**); reciprocal Schwann cell proliferation (**PMID: 11464875**); PEDF as the mediator (**PMID: 11792807**) | Two-cell-type in vitro system; no tissue architecture, no immune compartment, no vasculature |
| **Human sympathoadrenal / adrenal organoids and iPSC models** | In vitro | Differentiated from iPSC | Emerging; used to map the SCP → sympathoblast decision | Not yet a GNB model |

### 15.3 Databases and resources

- **MGI** (mouse), **ZFIN** (zebrafish), **RGD** (rat), **Alliance of Genome Resources** — for allele and phenotype records
- **IMSR**, **MMRRC**, **EMMA**, **KOMP/IMPC** — strain availability
- **Cellosaurus**, **ATCC** — cell lines
- **DepMap** — CRISPR dependency data on neuroblastoma lines
- **R2 Genomics Analysis and Visualization Platform** — the de facto neuroblastoma expression-cohort resource
- **INRG Data Commons** (inrgdb.org) — the clinical-biological cohort resource, and the source of the GNBn-specific analyses

### 15.4 Research applications and the GNB-shaped hole

What the available models **can** study: MYCN- and ALK-driven transformation, ALK inhibitor pharmacology and resistance, anti-GD2 immunotherapy (immunocompetent TH-MYCN), retinoid differentiation pharmacology, metastatic niche biology.

What they **cannot** study, and what therefore remains open:
1. **Why one subclone of a GNBn escapes the differentiation signal while its siblings mature.** No model reproduces the composite architecture.
2. **What recruits and sustains the Schwannian stroma in vivo**, and whether it can be therapeutically induced. The co-culture systems show the loop exists; nothing shows how to drive it in a patient.
3. **Whether GNBi is a tumour that is maturing or a tumour that has stopped maturing** — i.e. whether it is a way-station to ganglioneuroma or a stable state. This distinction determines whether "watch and wait" is watching a resolving process or a static one, and it is not answerable from current models or from the natural-history data.

---

## Appendix A — Consolidated ontology term suggestions

**✅ = verified against the named authority during this session. ⚠ = suggestion only; must be looked up before binding.**

### Disease
`MONDO:0005035` ✅ ganglioneuroblastoma · `MONDO:0003326` ✅ intermixed · `MONDO:0003325` ✅ nodular · `MONDO:0004477` ✅ adrenal · `MONDO:0001096` ✅ mediastinal · `MONDO:0003327` ✅ peripheral · `NCIT:C3790` ✅ · `NCIT:C42057` ✅ intermixed · `NCIT:C124274` ✅ childhood nodular · `HP:0006747` ✅

### Phenotype (HP)
`HP:0031500` ✅ Abdominal mass · `HP:0002277` ✅ Horner syndrome · `HP:0006837` ✅ Congenital Horner syndrome · `HP:0007451` ✅ Ipsilateral lack of facial sweating · `HP:0010543` ✅ Opsoclonus · `HP:0011977` ✅ Elevated urinary homovanillic acid · `HP:0011978` ✅ Elevated urinary vanillylmandelic acid
⚠ Myoclonus, Ataxia, Hypertension, Chronic diarrhea, Hypokalemia, Spinal cord compression, Paraparesis, Dyspnea, Growth delay, Bone pain, Proptosis, Constipation

### Cell type (CL)
`CL:0011012` ✅ neural crest cell · `CL:0002375` ✅ Schwann cell precursor · `CL:0000031` ✅ neuroblast (sensu Vertebrata) · `CL:0002676` ✅ neural crest derived neuroblast · `CL:0002573` ✅ Schwann cell · `CL:0002376` ✅ non-myelinating Schwann cell · `CL:0000218` ✅ myelinating Schwann cell · `CL:0011103` ✅ sympathetic neuron · `CL:0000166` ✅ chromaffin cell · `CL:0000336` ✅ adrenal medulla chromaffin cell

### Anatomy (UBERON)
`UBERON:0001236` ✅ adrenal medulla · `UBERON:0002369` ✅ adrenal gland · `UBERON:0000013` ✅ sympathetic nervous system · `UBERON:0001806` ✅ sympathetic ganglion · `UBERON:0001807` ✅ paravertebral ganglion · `UBERON:0000961` ✅ thoracic ganglion · `UBERON:0001991` ✅ cervical ganglion · `UBERON:0001989` ✅ superior cervical ganglion · `UBERON:0002441` ✅ cervicothoracic ganglion · `UBERON:8600121` ✅ lumbar ganglion · `UBERON:8600122` ✅ sacral ganglion
⚠ posterior mediastinum, retroperitoneal space, organ of Zuckerkandl, bone marrow

### Biological process (GO)
`GO:0048485` ✅ sympathetic nervous system development · `GO:0048483` ✅ autonomic nervous system development · `GO:1903045` ✅ neural crest cell migration involved in sympathetic nervous system development · `GO:0014033` ✅ neural crest cell differentiation · `GO:0014035` ✅ neural crest cell fate determination · `GO:1905292/1905293/1905294` ✅ regulation of neural crest cell differentiation · `GO:0042423` ✅ catecholamine biosynthetic process · `GO:0042416` ✅ dopamine biosynthetic process · `GO:0006585` ✅ dopamine biosynthetic process from tyrosine
⚠ neuron differentiation, glial cell differentiation, telomere maintenance, protein tyrosine kinase activity, cell population proliferation

### Chemical (CHEBI)
`CHEBI:545959` ✅ homovanillic acid · `CHEBI:20106` ✅ vanillylmandelic acid · `CHEBI:133744` ✅ homovanillate · `CHEBI:27622` ✅ vanillylmandelate · `CHEBI:6067` ✅ isotretinoin · `CHEBI:41948` ✅ eflornithine

### Treatment (NCIT)
`NCIT:C1570` ✅ Dinutuximab · `NCIT:C226` ✅ Eflornithine · `NCIT:C202976` ✅ Eflornithine Regimen · `NCIT:C603` ✅ Isotretinoin · `NCIT:C174559` ✅ Dinutuximab/Irinotecan/Temozolomide Regimen · `NCIT:C15722` ✅ Patient Observation · `NCIT:C212045` ✅ Anti-GD2 ADC M3554
⚠ Surgical Procedure, Chemotherapy, Pharmacotherapy, Radiation Therapy, Hematopoietic Cell Transplantation, Genetic Counseling, Lorlatinib, Naxitamab, Dinutuximab beta, GM-CSF

### Gene (HGNC — all ✅ verified via rest.genenames.org)
`hgnc:7559` MYCN · `hgnc:427` ALK · `hgnc:9143` PHOX2B · `hgnc:886` ATRX · `hgnc:11730` TERT · `hgnc:7765` NF1 · `hgnc:32207` LIN28B · `hgnc:6641` LMO1 · `hgnc:952` BARD1 · `hgnc:33775` ALKAL1 · `hgnc:27683` ALKAL2

---

## Appendix B — Five things a curator should not get wrong

1. **"Ganglioneuroblastoma" is two diseases.** GNBi is favourable histology at any age and is managed by observation or conservative surgery; GNBn is graded by its worst nodule and can be stage-4 high-risk. A single entry that averages them is wrong about both. Consider `has_subtypes` with the INPC categories, and stratify phenotypes, prevalence and treatment by subtype.
2. **The Schwannian stroma is not neoplastic.** `PMID: 25081755` showed MYCN gain in neuroblasts and ganglion cells but **not** in Schwann cells. Model Schwann cells as microenvironment, not as a tumour cell type.
3. **The cell of origin derives from the node carrying the somatic lesion** — the transformed sympathoadrenal progenitor — and the recorded `cell_types` there should be the neuroblast lineage (`CL:0002676` / `CL:0000031`), not the Schwann cell.
4. **Post-treatment specimens cannot carry an INPC diagnosis.** "Tumours should never be reclassified after treatment" (ICCR Note 7). Any prevalence, frequency or phenotype figure sourced from a post-chemotherapy series is describing a different population.
5. **The SEER chemotherapy HR of 2.14 is confounding by indication, not a treatment effect.** Record it only with that caveat, or not at all.

---

## Sources

**Primary guideline / classification documents**
- [ICCR Neuroblastoma Histopathology Reporting Guide, 1st ed. v1.0, November 2023](https://www.iccr-cancer.org/wp-content/uploads/2023/11/ICCR-Neuroblastoma-1st-ed-v1.0-bookmark.pdf) — ISBN 978-1-922324-39-9 (the source of all verbatim INPC/WHO quotations above)
- [NCI PDQ® Neuroblastoma Treatment (Health Professional Version)](https://www.cancer.gov/types/neuroblastoma/hp/neuroblastoma-treatment-pdq)
- [CAP Protocol for the Examination of Resection Specimens From Patients With Neuroblastoma, v5.0.0.1](https://www.cap.org/wp-content/uploads/documents/New-Cancer-Protocols-June-2025/Neuroblastoma_5.0.0.1.REL_CAPCP.pdf?download=true)
- WHO Classification of Tumours Editorial Board (2023). *Paediatric Tumours*, WHO Classification of Tumours, 5th ed., Vol. 7. IARC, Lyon

**Ganglioneuroblastoma-specific literature**
- [Angelini P, et al. Characteristics and outcome of patients with ganglioneuroblastoma, nodular subtype: a report from the INRG project. Eur J Cancer 2012 — PMID 22137163](https://www.sciencedirect.com/science/article/abs/pii/S0959804911008720)
- [Angelini P, et al. The neuroblastoma and ganglion components of nodular ganglioneuroblastoma are genetically similar. Mod Pathol 2015 — PMID 25081755](https://www.nature.com/articles/modpathol201490)
- [Umehara S, et al. Histopathology defines prognostic subsets of ganglioneuroblastoma, nodular. Cancer 2000 — PMID 10964346](https://acsjournals.onlinelibrary.wiley.com/doi/full/10.1002/1097-0142(20000901)89:5%3C1150::AID-CNCR25%3E3.0.CO;2-7)
- [Peuchmaur M, et al. Revision of the INPC: confirmation of favorable and unfavorable prognostic subsets in ganglioneuroblastoma, nodular. Cancer 2003 — PMID 14601099](https://acsjournals.onlinelibrary.wiley.com/doi/full/10.1002/cncr.11773)
- [He WG, et al. Clinical and biological features of neuroblastic tumors: a comparison of neuroblastoma and ganglioneuroblastoma. Oncotarget 2017 — PMID 28465480](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5514944/)
- [Li W, et al. Development and validation of a prognostic nomogram for patients with ganglioneuroblastoma: a SEER-based study. Heliyon 2024 — PMID 38774105](https://pmc.ncbi.nlm.nih.gov/articles/PMC11107237/)
- Sugawara M, et al. Telomere maintenance mechanisms are activated in ganglioneuroblastoma and ganglioneuroma. Oncol Lett 2026 — PMID 41858373
- [Decarolis B, et al. Treatment and outcome of Ganglioneuroma and Ganglioneuroblastoma intermixed. BMC Cancer 2016 — PMID 27465021](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4964292/)
- Burnand KM, et al. Management of Ganglioneuroma and Ganglioneuroblastoma Intermixed: a UK CCLG Nationwide Study Report. Pediatr Blood Cancer 2025 — PMID 39582110
- [Alexander N, et al. Characteristics and management of ganglioneuroma and ganglioneuroblastoma-intermixed. Pediatr Blood Cancer 2018 — PMID 29369484](https://doi.org/10.1002/pbc.26964)
- [Yang T, et al. Surgical management and outcomes of ganglioneuroma and ganglioneuroblastoma-intermixed. Pediatr Surg Int 2017 — PMID 28608056](https://link.springer.com/article/10.1007/s00383-017-4100-9)
- Montante C, et al. The Pitfall of Ganglioneuroblastoma-Nodular Diagnosis. Diagnostics 2022 — PMID 36553228
- Shimizu H, et al. Infantile Ganglioneuroblastoma Causing Growth Failure and Hypertensive Cardiomyopathy. J Pediatr Hematol Oncol 2026 — PMID 41891982
- Alioglu H, et al. Cervicothoracic dumbbell ganglioneuroblastoma with spinal canal involvement. Eur Spine J 2026 — PMID 42811141
- Zhang Q, et al. Ganglioneuroblastoma associated with neurofibromatosis type 1. Front Oncol 2026 — PMID 42311262
- [Vassallo L, et al. A rare case of adrenal ganglioneuroblastoma-intermixed in an adult. Radiol Case Rep 2021 — PMID 34306280](https://doi.org/10.1016/j.radcr.2021.06.005)

**Classification, staging and risk**
- [Shimada H, et al. Terminology and morphologic criteria of neuroblastic tumors. Cancer 1999 — PMID 10421272](https://acsjournals.onlinelibrary.wiley.com/doi/full/10.1002/(SICI)1097-0142(19990715)86:2%3C349::AID-CNCR20%3E3.0.CO%3B2-Y)
- [Shimada H, et al. The International Neuroblastoma Pathology Classification (the Shimada system). Cancer 1999](https://acsjournals.onlinelibrary.wiley.com/doi/10.1002/(SICI)1097-0142(19990715)86:2%3C364::AID-CNCR21%3E3.0.CO%3B2-7)
- [Cohn SL, et al. The INRG Classification System: an INRG Task Force Report. J Clin Oncol 2009](https://pmc.ncbi.nlm.nih.gov/articles/PMC2650388/)
- [Monclair T, et al. The INRG Staging System: an INRG Task Force Report. J Clin Oncol 2009](https://inrgdb.org/neuroblastoma-information/staging-system/)
- [Irwin MS, et al. Revised Neuroblastoma Risk Classification System: a Report From the Children's Oncology Group. J Clin Oncol 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8500606/)
- [Sokol E, et al. Age, Diagnostic Category, Tumor Grade, and MKI Are Independently Prognostic in Neuroblastoma: an INRG Project. J Clin Oncol 2020 — PMID 32315273](https://doi.org/10.1200/jco.19.03285)
- [Teshiba R, et al. Age-dependent prognostic effect by MKI in neuroblastoma: a report from the COG. Pediatr Dev Pathol 2014 — PMID 25207821](https://doi.org/10.2350/14-06-1505-oa.1)
- [Nakazawa A, et al. Correlation between the INPC and genomic signature in neuroblastoma. Cancer Sci 2015 — PMID 25827934](https://doi.org/10.1111/cas.12665)
- [Nakazawa A. Biological categories of neuroblastoma based on the INPC for treatment stratification. Pathol Int 2021 — PMID 33657257](https://doi.org/10.1111/pin.13085)
- [The Evolution of Risk Classification for Neuroblastoma. Children (Basel) 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6406722/)

**Genetics and predisposition**
- [Kamihara J, et al. Neuroblastoma Predisposition and Surveillance—An Update from the 2023 AACR Childhood Cancer Predisposition Workshop. Clin Cancer Res 2024 — PMID 38860978](https://aacrjournals.org/clincancerres/article/30/15/3137/746580/)
- [Kamihara J, et al. Retinoblastoma and Neuroblastoma Predisposition and Surveillance. Clin Cancer Res 2017 — PMID 28674118](https://doi.org/10.1158/1078-0432.ccr-17-0652)
- [Mossé YP, et al. Identification of ALK as a major familial neuroblastoma predisposition gene. Nature 2008 — PMID 18724359](https://pubmed.ncbi.nlm.nih.gov/18724359/)
- Trochet D, et al. Germline mutations of PHOX2B in neuroblastoma. Am J Hum Genet 2004 — PMID 15024693
- Mossé YP, et al. Germline PHOX2B mutation in hereditary neuroblastoma. Am J Hum Genet 2004 — PMID 15338462
- [Raabe EH, et al. Prevalence and functional consequence of PHOX2B mutations in neuroblastoma. Oncogene 2008 — PMID 17637745](https://doi.org/10.1038/sj.onc.1210659)
- [Oldridge DA, et al. Genetic predisposition to neuroblastoma mediated by a LMO1 super-enhancer polymorphism. Nature 2015 — PMID 26560027](https://doi.org/10.1038/nature14319)
- [Tonini GP, Capasso M. Genetic predisposition and chromosome instability in neuroblastoma. Cancer Metastasis Rev 2020 — PMID 31927719](https://pubmed.ncbi.nlm.nih.gov/31927719/)
- [Rosswog C, et al. Genomic ALK alterations in primary and relapsed neuroblastoma. Br J Cancer 2023 — PMID 36807339](https://doi.org/10.1038/s41416-023-02208-y)
- [Djos A, et al. Loss of Chromosome Y in Neuroblastoma Is Associated With High-Risk Disease, 11q-Deletion, and Telomere Maintenance. Genes Chromosomes Cancer 2024](https://onlinelibrary.wiley.com/doi/full/10.1002/gcc.23260)
- [GeneReviews: ALK-Related Neuroblastic Tumor Susceptibility](https://www.ncbi.nlm.nih.gov/books/NBK24599/)

**Mechanism and developmental biology**
- [Sainero-Alcolado L, et al. Defining neuroblastoma: From origin to precision medicine. Neuro Oncol 2024 — PMID 39101440](https://pubmed.ncbi.nlm.nih.gov/39101440/)
- [Thirant C, et al. Reversible transitions between noradrenergic and mesenchymal tumor identities define cell plasticity in neuroblastoma. Nat Commun 2023 — PMID 37142597](https://www.nature.com/articles/s41467-023-38239-5)
- [Hanemaaijer ES, et al. Single-cell atlas of developing murine adrenal gland reveals relation of Schwann cell precursor signature to neuroblastoma phenotype. PNAS 2021 — PMID 33500353](https://doi.org/10.1073/pnas.2022350118)
- [Olsen TK, et al. Malignant Schwann cell precursors mediate intratumoral plasticity in human neuroblastoma. bioRxiv 2020](https://doi.org/10.1101/2020.05.04.077057)
- [Fetahu IS, et al. Single-cell transcriptomics and epigenomics unravel the role of monocytes in neuroblastoma bone marrow metastasis. Nat Commun 2023 — PMID 37365178](https://www.nature.com/articles/s41467-023-39210-0)
- [Crawford SE, et al. PEDF in neuroblastoma: a multifunctional mediator of Schwann cell antitumor activity. J Cell Sci 2001 — PMID 11792807](https://doi.org/10.1242/jcs.114.24.4421)
- Kwiatkowski JL, et al. Schwann cell-conditioned medium promotes neuroblastoma survival and differentiation. Cancer Res 1998 — PMID 9788610
- [Ambros IM, et al. Neuroblastoma cells provoke Schwann cell proliferation in vitro. Med Pediatr Oncol 2001 — PMID 11464875](https://doi.org/10.1002/1096-911x(20010101)36:1%3C163::aid-mpo1040%3E3.0.co;2-2)
- [Weiss WA, et al. Targeted expression of MYCN causes neuroblastoma in transgenic mice. EMBO J 1997](https://www.embopress.org/doi/full/10.1093/emboj/16.11.2985)
- [Alam G, et al. MYCN promotes the expansion of Phox2B-positive neuronal progenitors to drive neuroblastoma development. Am J Pathol 2009 — PMID 19608868](https://doi.org/10.2353/ajpath.2009.090019)
- [Pei D, et al. Distinct neuroblastoma-associated alterations of PHOX2B impair sympathetic neuronal differentiation in zebrafish models. PLoS Genet 2013 — PMID 23754957](https://doi.org/10.1371/journal.pgen.1003533)
- [Bachetti T, et al. PHOX2B-mediated regulation of ALK expression. PLoS One 2010 — PMID 20957039](https://doi.org/10.1371/journal.pone.0013108)
- [Brodeur GM. Spontaneous regression of neuroblastoma. Cell Tissue Res 2018 — PMID 29305654](https://doi.org/10.1007/s00441-017-2761-2)
- [Tacconelli A, et al. TrkA alternative splicing: a regulated tumor-promoting switch in human neuroblastoma. Cancer Cell 2004 — PMID 15488758](https://doi.org/10.1016/j.ccr.2004.09.011)
- [Huang S, et al. ZNF423 is critically required for retinoic acid-induced differentiation. Cancer Cell 2009 — PMID 19345331](https://doi.org/10.1016/j.ccr.2009.02.023)
- [Kocak H, et al. Hox-C9 activates the intrinsic pathway of apoptosis and is associated with spontaneous regression in neuroblastoma. Cell Death Dis 2013 — PMID 23579273](https://doi.org/10.1038/cddis.2013.84)
- [Revet I, et al. The MSX1 homeobox transcription factor is a downstream target of PHOX2B. Exp Cell Res 2008 — PMID 18201699](https://doi.org/10.1016/j.yexcr.2007.12.008)
- [Enteric Neural Crest Differentiation in Ganglioneuromas Implicates Hedgehog Signaling in Peripheral Neuroblastic Tumor Pathogenesis](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2759000/)
- [Schwann cell plasticity regulates neuroblastic tumor cell differentiation via EGFL8. Nat Commun 2021](https://www.nature.com/articles/s41467-021-21859-0)

**Treatment**
- [Goldsmith KC, et al. Lorlatinib with or without chemotherapy in ALK-driven refractory/relapsed neuroblastoma: phase 1 trial results. Nat Med 2023 — PMID 37012551](https://doi.org/10.1038/s41591-023-02297-5)
- [Berko ER, et al. Circulating tumor DNA reveals mechanisms of lorlatinib resistance. Nat Commun 2023 — PMID 37147298](https://doi.org/10.1038/s41467-023-38195-0)
- [Borenäs M, et al. ALK signaling primes the DNA damage response sensitizing ALK-driven neuroblastoma to therapeutic ATR inhibition. PNAS 2024 — PMID 38154064](https://doi.org/10.1073/pnas.2315242121)
- [Bergaggio E, et al. ALK inhibitors increase ALK expression and sensitize neuroblastoma cells to ALK.CAR-T cells. Cancer Cell 2023 — PMID 38039964](https://doi.org/10.1016/j.ccell.2023.11.004)
- [Tucker ER, et al. Combination Therapies Targeting ALK-aberrant Neuroblastoma in Preclinical Models. Clin Cancer Res 2023 — PMID 36602782](https://doi.org/10.1158/1078-0432.CCR-22-2274)
- [Lerman BJ, et al. PFS and Patterns of Response in Patients With Relapsed High-Risk Neuroblastoma Treated With Irinotecan/Temozolomide/Dinutuximab/GM-CSF. J Clin Oncol 2023 — PMID 36206505](https://doi.org/10.1200/jco.22.01273)
- [Raiser P, et al. Chemo-immunotherapy with dinutuximab beta: does chemotherapy backbone matter? Eur J Cancer 2024 — PMID 38489858](https://doi.org/10.1016/j.ejca.2024.114001)
- [Muñoz JP, et al. Early Salvage Chemo-Immunotherapy (HITS) for Primary Refractory High-Risk Neuroblastoma. Cancers 2023 — PMID 37835531](https://doi.org/10.3390/cancers15194837)
- [Wieczorek A, et al. Efficacy and Safety of Dinutuximab Beta in Relapsed/Refractory High-Risk Neuroblastoma. Target Oncol 2025 — PMID 40459700](https://doi.org/10.1007/s11523-025-01155-3)
- [Mora J, et al. GM-CSF, G-CSF or no cytokine therapy with anti-GD2 immunotherapy. Int J Cancer 2024 — PMID 38108214](https://doi.org/10.1002/ijc.34815)
- [US FDA Approval Summary: Eflornithine for High-Risk Neuroblastoma — PMID 38917371](https://pubmed.ncbi.nlm.nih.gov/38917371/)
- [IWILFIN (eflornithine) Prescribing Information, FDA 2024](https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/215500s001lbl.pdf)
- [Troschke-Meurer S, et al. Chemotherapeutics improve the efficacy of dinutuximab beta in preclinical spheroid models. Cancers 2023 — PMID 36765861](https://doi.org/10.3390/cancers15030904)

**Imaging and diagnostics**
- Wang X, et al. Multiparametric ¹⁸F-MFBG PET/CT model differentiating neuroblastoma from ganglioneuroblastoma. Eur J Nucl Med Mol Imaging 2026 — PMID 42820950
- Li S, et al. ⁶⁸Ga-DOTATATE PET/CT vs ¹²³I-MIBG SPECT/CT in CNS metastases of neuroblastoma and ganglioneuroblastoma. Eur J Nucl Med Mol Imaging 2025 — PMID 40637785
- Zhang G, et al. Enhanced CT radiomics and deep learning differentiating peripheral neuroblastoma from ganglioneuroblastoma. BMC Cancer 2026 — PMID 41652556
- [Wang H, et al. Radiomics analysis of contrast-enhanced CT in predicting the INPC. Insights Imaging 2023 — PMID 37316589](https://doi.org/10.1186/s13244-023-01418-5)
- [Qian LD, et al. ¹⁸F-FDG PET/CT combined model to predict the INPC. Quant Imaging Med Surg 2023 — PMID 36620179](https://doi.org/10.21037/qims-22-343)

**Epidemiology and outcomes**
- [Yan P, et al. Comparison of Incidence and Outcomes of Neuroblastoma in Children, Adolescents, and Adults in the United States: a SEER Population Study. Med Sci Monit 2020 — PMID 33249420](https://doi.org/10.12659/MSM.927218)
- [Liu S, et al. Metastasis pattern and prognosis in children with neuroblastoma. World J Surg Oncol 2023 — PMID 37046344](https://doi.org/10.1186/s12957-023-02967-1)
- [Late effects after high-risk neuroblastoma (LEAHRN): a multicentre, cross-sectional cohort study from the COG](https://www.sciencedirect.com/science/article/abs/pii/S235246422500241X)
- [Flaadt T, et al. Long-Term Outcomes and Quality of Life of High-Risk Neuroblastoma Patients Treated with Multimodal Treatment Including Anti-GD2 Immunotherapy. Cancers 2025 — PMID 39796776](https://doi.org/10.3390/cancers17010149)
- [Late Effects and Survivorship Issues in Patients with Neuroblastoma](https://pmc.ncbi.nlm.nih.gov/articles/PMC6111874/)
- [Comparison of mediastinal and non-mediastinal neuroblastoma and ganglioneuroblastoma associated with opsoclonus-myoclonus syndrome: a systematic review and meta-analysis](https://pmc.ncbi.nlm.nih.gov/articles/PMC9641106/)

**Veterinary / comparative**
- [Romano AM, Frank CB. Olfactory ganglioneuroblastoma in a dog: case report and literature review. J Vet Diagn Invest 2021](https://doi.org/10.1177/10406387211022864)
- [Footpad peripheral ganglioneuroblastoma in a dog — PMID 30950551](https://pubmed.ncbi.nlm.nih.gov/30950551/)
- [A case of olfactory ganglioneuroblastoma in a dog: immunohistochemical comparison with olfactory neuroepithelia and olfactory neuroblastomas](https://pmc.ncbi.nlm.nih.gov/articles/PMC11300123/)
- [OMIA — Online Mendelian Inheritance in Animals](https://www.omia.org/home/)

**Ontology authorities consulted directly**
- [EBI OLS4 API](https://www.ebi.ac.uk/ols4/) — MONDO, NCIT, HP, CL, UBERON, GO, CHEBI term records
- [HGNC REST service](https://rest.genenames.org/) — gene symbol/ID verification
- [Europe PMC REST API](https://www.ebi.ac.uk/europepmc/webservices/rest/) — abstract retrieval

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 151 |
| Resolved | 148 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 3 |
| Quoted claims checked | 31 |
| Quoted claims found in source | 24 |
| Quoted claims **not** found in source | 7 |
| References weighed for topical relevance | 148 |
| On topic | 30 |
| Off topic | 2 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

6 of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:9788610` *(abstract only)*: "induced extensive neurite outgrowth in all neuroblastoma cell lines, and these processes contained mature neurofilament in three of the cell lines"
  - closest text in source: "Schwann cell-conditioned medium induced extensive neurite outgrowth in all of the neuroblastoma cell lines, and these processes contained mature neurofilament in three of the cell lines"
- `PMID:15488758` *(abstract only)*: "antagonizes NGF/TrkA/Ras/MAPK signaling, which is responsible for NB growth arrest and differentiation"
  - closest text in source: "TrkAIII antagonizes NGF/TrkAI signaling, which is responsible for NB growth arrest and differentiation through Ras/MAPK, and its expression is promoted by hypoxia at the expense of NGF-responsive receptors, providing a mechanism for converting NGF/TrkA/Ras/MAPK antioncogenic signals to TrkAIII/IP3K/Akt/NF-kappaB tumor-promoting signals during tumor progression."
- `PMID:38774105` *(abstract only)*: "the prognosis of children with GNB was better than that of adolescents and adults with GNB"
  - closest text in source: "We constructed a nomogram based on the SEER database to predict the prognosis of GNB, but further optimization by adding more risk factors is needed for clinical application."
- `PMID:40065424` *(abstract only)*: "negative on MIBG scintigraphy"
  - Text part not found as substring: 'negative on MIBG scintigraphy' (note: only abstract available for PMID:40065424, full text may contain this excerpt)
- `PMID:38154064` *(abstract only)*: "Combined 14-day ALK/ATR inhibition produced robust and sustained response, with tumor cell reprogramming toward neuronal/Schwann cell differentiation"
  - closest text in source: "Finally, we show that the remarkable response to the 14-d combined ATR/ALK inhibition protocol reflects a robust differentiation response, reprogramming tumor cells to a neuronal/Schwann cell lineage identity"
- `PMID:38039964` *(abstract only)*: "specifically potentiate ALK.CAR-T cells but not GD2.CAR-T cells"
  - closest text in source: "For neuroblastoma with low ALK expression, combination with ALK inhibitors specifically potentiates ALK.CAR-T cells but not GD2.CAR-T cells"
- `PMID:28674118`: "review[s] recommended surveillance for hereditary patients with NB, including minor updates to surveillance recommendations that were published previously in 2017"
  - closest text in source: "In concert with previously published guidelines, these recommendations begin with intensive surveillance from birth with progressively spaced EUAs until age 5, although more frequent surveillance may be appropriate in individual cases"

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:40065424` (1 mention) - Positive 18 F-FDG PET/CT and Negative 123 I-MIBG SPECT/CT Imaging in an Unusual Diaphragmatic Metastasis From Ganglioneuroblastoma.
  - shared terms: ganglioneuroblastoma
- `DOI:10.1186/s12957-023-02967-1` (2 mentions) - Perioperative and oncologic outcomes of transperitoneal versus retroperitoneal laparoscopic radical nephrectomy for large-volume renal carcinoma (&gt; 7 cm): a systematic review and pooled analysis of comparative outcomes
  - shared terms: tumor

Weighed against this report's own most characteristic terms: `gnb`, `neuroblastoma`, `tumour`, `cell`, `gnbn`, `ganglioneuroblastoma`, `patient`, `disease`, `differentiation`, `neuroblastic`, `gnbi`, `alk`, `note`, `cancer`, `mycn`, `iccr`, `age`, `tumor`, `model`, `mechanism`.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 93 |
| Resolved | 88 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 4 |
| Terms whose name was checked | 27 |
| Terms named correctly | 14 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 9 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `NCIT:C3790` (2 mentions) - the report calls it "NCI Thesaurus"; NCIT calls it **Ganglioneuroblastoma**
- `DOID:4163` (1 mention) - the report calls it "Disease Ontology"; DOID calls it **ganglioneuroblastoma**
- `EFO:0000502` (1 mention) - the report calls it "EFO"; EFO calls it **obsolete_ganglioneuroblastoma**
- `NCIT:C124274` (2 mentions) - the report calls it "childhood"; NCIT calls it **Childhood Ganglioneuroblastoma, Nodular**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `EFO:0000502` (obsolete_ganglioneuroblastoma) (1 mention) - replaced by `http://purl.obolibrary.org/obo/MONDO:0005035`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0003326` (2 mentions) - the report calls it "Intermixed (Schwannian stroma-rich) GNB"; MONDO calls it **intermixed schwannian stroma-rich ganglioneuroblastoma**
- `MONDO:0003325` (2 mentions) - the report calls it "Nodular GNB"; MONDO calls it **nodular ganglioneuroblastoma**
- `MONDO:0004408` (1 mention) - the report calls it "Schwannian stroma-rich + stroma-poor composite"; MONDO calls it **schwannian stroma-rich and stroma-poor composite ganglioneuroblastoma**
- `MONDO:0004407` (1 mention) - the report calls it "Stroma-dominant + stroma-poor composite"; MONDO calls it **stroma-dominant and stroma-poor composite ganglioneuroblastoma**
- `MONDO:0004477` (2 mentions) - the report calls it "Adrenal gland GNB"; MONDO calls it **adrenal gland ganglioneuroblastoma**
- `MONDO:0001096` (2 mentions) - the report calls it "Mediastinal GNB"; MONDO calls it **mediastinum ganglioneuroblastoma**, and lists "mediastinal ganglioneuroblastoma" among its other names
- `MONDO:0003327` (2 mentions) - the report calls it "Peripheral GNB"; MONDO calls it **peripheral ganglioneuroblastoma**
- `CL:0011012` (3 mentions) - the report calls it "neural crest cells", "During embryogenesis, **neural crest cells"; CL calls it **neural crest cell**
- `UBERON:0002441` (3 mentions) - the report calls it "cervicothoracic (stellate) ganglion"; UBERON calls it **cervicothoracic ganglion**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0011012` - called "neural crest cells", "During embryogenesis, **neural crest cells"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `GARD`, `NANDO`.