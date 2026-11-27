---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-23T12:14:03.789715'
end_time: '2026-11-23T12:19:32.976868'
duration_seconds: 329.19
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: COG6-Congenital Disorder of Glycosylation
  mondo_id: MONDO:0013810
  category: Mendelian
  causal_genes: COG6
  omim_id: OMIM:614576
  synonyms: CDG syndrome type IIL; CDG-IIL; CDG2L; COG6-CDG; congenital disorder of
    glycosylation type 2l; congenital disorder of glycosylation type IIL
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
  web_search_requests: 9
  num_turns: 17
  total_cost_usd: 0.9669547750000002
  session_id: c1c03386-e29c-4d77-8758-6910b9f13f00
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  tool_calls: 43
  retrieval_calls: 41
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
  total_references: 20
  verified: 20
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 19
  quotes_valid: 19
  relevance_assessed: 20
  on_topic: 17
  validator_version: 0.8.0
term_validation:
  total_terms: 7
  verified: 3
  not_found: 0
  obsolete: 0
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 0
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0013810
    reported_labels:
    - MONDO
    ontology_label: COG6-congenital disorder of glycosylation
  - term_id: DOID:0070264
    reported_labels:
    - DOID
    ontology_label: congenital disorder of glycosylation type IIl
  unresolvable_prefixes:
  - OMIM
  - ORPHA
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** COG6-Congenital Disorder of Glycosylation
- **MONDO ID:** MONDO:0013810 (if available)
- **Causal gene(s):** COG6
- **OMIM:** OMIM:614576
- **Synonyms:** CDG syndrome type IIL; CDG-IIL; CDG2L; COG6-CDG; congenital disorder of glycosylation type 2l; congenital disorder of glycosylation type IIL
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **COG6-Congenital Disorder of Glycosylation** covering all of the
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

Gathering the key COG6-CDG papers now; next I'll pull exact PubMed IDs and abstract quotes.

Quotes below are copied from the `abstractText` fields I fetched earlier, with HTML tags removed. Each is under 125 characters. Where a source is missing one category, I say so.

**20605848** (2010, Hum Mol Genet)
- "a homozygous mutation (c.G1646T), leading to amino acid exchange p.G549V in the COG6 protein."
- "led to normalization of the COG complex-depending retrograde protein transport after Brefeldin A treatment"
- "fatal outcome in early infancy."

**26260076** (2015, Mol Genet Metab)
- "So far, 3 families with a total of 10 individuals with biallelic COG6 mutations have been described"
- "Here we present 7 additional patients with 4 novel COG6 mutations."
- "liver involvement (9/10), microcephaly (8/10), developmental disability (8/10), recurrent infections (7/10),"
- "loss-of-function mutations leading to early lethal CDG phenotypes."

**23606727** (2013, J Med Genet)
- "a deep intronic (NM_020751.2:c.1167-24A>G) variant in COG6 that largely replaces the consensus acceptor site"
- "resulting in pronounced reduction of the normal transcript and consequent deficiency of COG6 protein."
- "none of the patients displayed any detectable abnormality in the glycosylation pattern of transferrin"

**36636598** (2023, JIMD Rep)
- "we present the first two Swedish cases of Conserved Oligomeric Golgi complex subunit 6-congenital"
- "(c.785A>G; p.Tyr262Cys) has previously been described in patients of Moroccan descent"
- "a previously undescribed homozygous duplication (c.1793_1795dup) was deemed the cause of the disease."
- "patient cells manifest a significantly slower anterograde and retrograde ER-Golgi transport."
- Patients reviewed: the abstract gives no count for the literature review. It only says "a comprehensive literature review" in the title, so no number is available from the abstract.

**35068072** (2022, Birth Defects Res)
- "Eighteen patients with COG6-CDG (COG6 mutations) were reported to date."
- "a deletion of 1 bp mutation c.823delA creating a shift in the reading frame and a premature stop codon"
- "a 3 bp deletion (c.1141_1143delCTC) producing an in-frame deletion of 1 amino acid."

**32683677** (2020, Clin Genet)
- "a novel homozygous deletion of 26 bp in COG6, creating a splicing variant (c.518_540 + 3del)"
- "To-date, 12 variants causing COG6-CDG in less than 20 patients have been reported."
- "bowel malrotation and ambiguous genitalia, directing attention to the role of glycoprotein metabolism"

**32905044** (2020, JIMD Rep)
- "the homozygous nonsense mutation c.511C>T, p.(Arg171*) in the COG6 gene."
- "have been reported in only five out of the 21 reported COG6-CDG cases so far"
- "severe arthrogryposis, respiratory insufficiency and a rapid fatal course"

**29709711** (2019, Eur J Med Genet)
- "compound heterozygous variants (c.1A > G, p.? and c.388C > T, p.(Gln 130*)) of the COG6 gene"
- "Only eight mutations causing COG6 deficiencies have been described since the first report in 2010."
- "growth retardation, developmental disability, microcephaly, liver and gastrointestinal disease,"

**29445937** (2018, JIMD Rep)
- "a 5-year-old girl diagnosed with a Component of Oligomeric Golgi Complex 6 (COG6) gene defect"
- "characterized by prolonged fever, hepatosplenomegaly, hypertriglyceridemia, hypofibrinogenemia, pancytopenia"

**35048409** (2022, Pediatr Dermatol)
- "previously reported in another three individuals of Greek, Bulgarian and Turkish descent."
- "a lethal case of the ultra-rare COG6-congenital disorder of glycosylation (CDG) presenting with skin manifestations"
- "The presence of a founder mutation in the geographical area is possible."

**40213872** (2025, Mol Genet Genomic Med)
- "We identified a novel homozygous pathogenic variant in exon 9 of COG6 (NM_020751.2): c.821del, p.(Arg274Lysfs*32)."
- "Only 8 of the 28 published patients have had prenatal ultrasound anomalies reported"
- "a maldevelopmental cascade due to a neurodegenerative process of metabolic origin"

**41362306** (2025, Hum Mutat)
- "a novel homozygous variant in the COG6 gene: c.906_907delinsA, p.(His302GlnfsTer4)"
- "the complete absence of the COG6 subunit, impairment of two other cooperating subunits, and delayed retrograde transport."

**27066481** (2016, Front Cell Dev Biol)
- "all KO cell lines were uniformly deficient in cis/medial-Golgi glycosylation"
- "every subunit is essential for COG complex function in Golgi trafficking, though to varying extents."
- "Lobe A and Cog6 subunit KOs displayed a more severely distorted Golgi structure"

**40225945** (2024, Hum Mutat)
- "a paternal variant c.1672C>T (p.Gln558Ter) and a maternal variant c.153+392A>G (p.?)."
- "The paternal variant resulted in nonsense-mediated mRNA decay."
- "growth retardation, intellectual disability, frequent infections, and enamel hypoplasia."

**34331832** (2021, Mol Genet Genomic Med)
- "two novel heterozygous mutations: c.428G>T (p.S143I) and c.1843C>T (p.Q615X) in the COG6 gene"
- "To date, only 19 patients with COG6-CDG have been reported."
- "development delay, facial dysmorphism, growth retardation, skin abnormalities (hypohidrosis),"

**42269412** (2026, Mol Genet Metab)
- "All three patients experienced recurrent febrile episodes associated with biological features of HLH."
- "identified recurrent, unexplained, and poorly tolerated febrile episodes in approximately 40% of reported patients."
- "Early or prophylactic corticosteroid therapy during febrile episodes appeared to mitigate both the severity"

**33394555** (2021, Am J Med Genet A)
- "a novel variant of COG6 gene found in homozygosity in a Moroccan patient with severe presentation"
- "We hypothesize that the severe COG6 gene mutation interferes with glycosylation of a disintegrin and metalloprotease family members"
- Note: the title says "nonsense mutation", but the abstract says only "a novel variant". I quote the abstract, not the title.

**39528286** (2024, Zhonghua Yi Xue Yi Chuan Xue Za Zhi, Chinese-language journal)
- "compound heterozygous variants of the COG6 gene, namely c.807delT (p.F269Lfs*37) and c.1746+1G>C (p.Gly565_Met582del)"
- "the c.1746+1G>C variant could affect the mRNA splicing and produce a truncated protein"
- "the c.807delT variant could significantly reduce gene expression at both mRNA and protein levels."

# COG6‑Congenital Disorder of Glycosylation (COG6‑CDG; CDG2L): research report

**Scope and limits.** This report covers MONDO:0013810 / OMIM:614576. The causal gene is **COG6**, which encodes subunit 6 of the conserved oligomeric Golgi (COG) complex. The milder allelic condition, **Shaheen syndrome** (OMIM 615328), is covered as part of the same COG6 spectrum where relevant. It is not the target entity.

How sources were obtained:
- **PubMed:** abstract pages were blocked by a cookie wall. Abstract text was therefore taken from Europe PMC records, and quotes are limited to verbatim fragments of 125 characters or fewer.
- **Database queries not done:** I did not query ClinVar, gnomAD, HPO, GO, CL, UBERON or NCIT directly in this session.
- **Ontology suggestions:** these are therefore given as **term labels only, with no IDs**. Validate them before ingestion, for example with the `MS_linkml-term-validator` skill.
- **Statements with no source:** any statement without a citation is marked as not retrieved.

---

## 1. Disease information

**Overview.** COG6‑CDG is an ultra‑rare autosomal recessive multisystem disorder caused by biallelic **COG6** variants. COG6 is a lobe‑B subunit of the COG complex, which tethers vesicles at the Golgi. Losing it disrupts Golgi trafficking and the positioning of glycosylation enzymes. The result is combined N‑ and O‑glycosylation defects.
- The first patient had "a new combined N‑ and O‑glycosylation deficiency" with "fatal outcome in early infancy" (Lübbehusen et al., 2010, *Hum Mol Genet*, PMID 20605848).
- COG6 "plays a crucial role in Golgi trafficking and positioning of glycosylation enzymes" (Rymen et al., 2015, *Mol Genet Metab*, PMID 26260076).

**Identifiers**

| Resource | ID | Source |
|---|---|---|
| MONDO | MONDO:0013810 | GARD record ([rarediseases.info.nih.gov](https://rarediseases.info.nih.gov/assets/singles/10944.json)) |
| OMIM (phenotype) | 614576 (CDG2L) | MedGen ([C3553230](https://https.ncbi.nlm.nih.gov/medgen/C3553230)); LOVD ([03681](https://databases.lovd.nl/shared/diseases/03681)) |
| OMIM (gene) | *606977 COG6 | [OMIM mirror](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/606977) |
| Orphanet | ORPHA:464443 | MedGen and GARD. A PhenoDis mirror leaves the field blank, so confirm on orpha.net. |
| DOID | DOID:0070264 | [disease-ontology.org](https://disease-ontology.org/term/DOID:0070264/owl) |
| Related allelic entity | Shaheen syndrome, OMIM 615328, ORPHA:363523, MONDO:0014131 | [CISMeF](https://www.cismef.org/page/detail/en/MIM_PH_615328); [KEGG H03097](https://www.kegg.jp/entry/H03097) |
| ICD‑10 / ICD‑11 / MeSH | Not retrieved | — |

- **Gene location:** 13q14.11 (MedGen).
- **Synonyms:** CDG2L; CDG‑IIL; congenital disorder of glycosylation type IIL / type 2L; COG6‑CDG; "deficiency of subunit 6 of the conserved oligomeric Golgi complex".
- **Source of information:** all evidence is aggregated case reports and small series of individual patients. There is no EHR or registry‑scale data.

## 2. Etiology

- **Cause:** biallelic germline loss‑of‑function or hypomorphic COG6 variants. This is purely genetic.
- **Genetic risk factors:**
  - Consanguinity is the main risk factor. Most reported families are consanguineous (Saudi, Moroccan, Turkish; see Section 9).
  - Regional founder alleles are suspected (see Section 9).
- **Modifier genes:** none identified. Patients homozygous for the same allele (p.G549V) "present a markedly different clinical picture" (Huybrechts et al., 2012, *JIMD Rep*, PMID 23430903), which suggests modifiers or environmental factors, but none are known.
- **Environmental, protective and gene‑environment factors:** none documented.
  - Febrile illness acts as a *trigger for decompensation*, not a cause. Hypohidrosis predisposes to hyperthermia (PMID 26260076), and recurrent febrile and HLH episodes occur (PMID 42269412).

## 3. Phenotypes

Frequencies come from the review of 10 previously described patients in Rymen et al. 2015 (PMID 26260076). That paper notes: "So far, 3 families with a total of 10 individuals with biallelic COG6 mutations have been described." Its core features: "liver involvement (9/10), microcephaly (8/10), developmental disability (8/10), recurrent infections (7/10), early lethality (6/10), and hypohidrosis predisposing for hyperthermia (6/10) and hyperkeratosis (4/10)".

By 2025, 28 patients had been published (PMID 40213872).

| Phenotype | Type | Onset / course | Frequency | Suggested HPO label | Evidence (PMID) |
|---|---|---|---|---|---|
| Liver disease (hepatopathy, elevated transaminases, cholestasis) | sign / lab | infancy | 9/10 | Abnormality of the liver; Cholestasis; Elevated hepatic transaminase | 26260076; 34331832; 39528286 |
| Microcephaly (often progressive/acquired) | sign | postnatal, progressive | 8/10 | Microcephaly; Progressive microcephaly | 26260076; 23606727; 36636598 |
| Developmental delay / intellectual disability | neurodevelopmental | infancy | 8/10 | Global developmental delay; Intellectual disability | 26260076; 23606727 |
| Recurrent infections | sign | infancy | 7/10 | Recurrent infections | 26260076; 40225945 |
| Hypohidrosis with episodic hyperthermia | sign | childhood | 6/10 | Hypohidrosis; Episodic hyperthermia | 26260076; 23606727; 34331832 |
| Hyperkeratosis (palmoplantar) | sign | childhood | 4/10 | Palmoplantar hyperkeratosis | 26260076; OMIM 615328 |
| Enamel hypoplasia / dental caries | sign | childhood | frequent in milder forms | Enamel hypoplasia; Carious teeth | 23606727; 36636598; 40225945 |
| Growth retardation | sign | infancy | common | Growth delay | 29709711; 34331832; 40225945 |
| Gastrointestinal disease (diarrhoea, bowel malrotation) | sign | infancy | some | Chronic diarrhea; Intestinal malrotation | 29709711; 39528286; 32683677 |
| Vitamin K deficiency, coagulopathy, intracranial bleeding, seizures | sign / lab | neonatal | index case | Intracranial hemorrhage; Seizure; Abnormal coagulation | 20605848 |
| Neonatal skin phenotype (restrictive‑dermopathy‑like, scaling, erosions) with arthrogryposis or contractures | sign | neonatal, lethal | "only five out of the 21 reported" | Arthrogryposis multiplex congenita; Ichthyosis; Arachnodactyly | 32905044; 35048409 |
| Male disorder of sex development (ambiguous genitalia) | malformation | congenital | several | Ambiguous genitalia | 32683677; 33394555 |
| Recto‑vaginal fistula; corpus callosum dysgenesis | malformation | congenital | single case | Rectovaginal fistula; Abnormality of the corpus callosum | 35068072 |
| Prenatal anomalies (fetal) | prenatal | fetal | "Only 8 of the 28 published patients" | — | 40213872 |
| Hemophagocytic lymphohistiocytosis (HLH) / recurrent febrile episodes | sign / lab | childhood | ~40% have recurrent febrile episodes | Hemophagocytic lymphohistiocytosis; Recurrent fever | 29445937; 42269412 |
| Delayed myelination, ADHD, joint laxity | neuro / behaviour | childhood | Swedish cases | Delayed CNS myelination; ADHD; Joint laxity | 36636598 |
| Abnormal transferrin glycosylation (type II pattern) | lab | — | most; **absent in Shaheen syndrome** | Abnormal protein glycosylation | 20605848; 23606727 |

Supporting quotes:
- HLH in a 5‑year‑old: "characterized by prolonged fever, hepatosplenomegaly, hypertriglyceridemia, hypofibrinogenemia, pancytopenia" (PMID 29445937).
- Recurrent febrile episodes: "identified recurrent, unexplained, and poorly tolerated febrile episodes in approximately 40% of reported patients" (PMID 42269412).
- Male DSD and bowel malrotation: "bowel malrotation and ambiguous genitalia, directing attention to the role of glycoprotein metabolism" (PMID 32683677).
- Neonatal lethal form: "severe arthrogryposis, respiratory insufficiency and a rapid fatal course" (PMID 32905044).

**Quality of life:** no formal QoL instruments (EQ‑5D, SF‑36) have been reported. The main burdens are severe intellectual disability, hyperthermic episodes and recurrent infections.

## 4. Genetic and molecular information

**Gene**
- COG6, component of oligomeric Golgi complex 6. OMIM *606977; locus 13q14.11. Reference transcript: NM_020751.2 (cited in PMIDs 23606727 and 40213872).
- HGNC ID, UniProt accession and NCBI Gene ID were not retrieved in this session.

**Reported pathogenic variants** (all germline, biallelic)

| Variant | Type | Zygosity / population | Phenotype | PMID |
|---|---|---|---|---|
| c.1646G>T, p.G549V | missense | homozygous; Moroccan / consanguineous | fatal infantile CDG; second patient milder. Pathogenicity was later questioned by Shaheen et al. (per OMIM). | 20605848; 23430903 |
| c.1167‑24A>G | deep intronic, creates a new acceptor site | homozygous; Saudi tribal founder | **Shaheen syndrome** (mild; normal transferrin) | 23606727 |
| c.785A>G, p.Tyr262Cys | missense | Swedish patient (allele "previously described in patients of Moroccan descent") | intermediate | 36636598 |
| c.1793_1795dup | in‑frame duplication | homozygous; Swedish | intermediate | 36636598 |
| c.511C>T, p.(Arg171*) | nonsense | homozygous; Greek; also seen in Greek, Bulgarian, Turkish and Albanian patients (possible SE‑European founder) | lethal neonatal, skin phenotype | 32905044; 35048409 |
| c.518_540+3del (26 bp) | splice | homozygous | male DSD, malrotation | 32683677 |
| c.1A>G (p.?) / c.388C>T p.(Gln130*) | start‑loss / nonsense | compound heterozygous; Chinese | growth retardation, liver/GI disease | 29709711 |
| c.428G>T p.(S143I) / c.1843C>T p.(Q615X) | missense / nonsense | compound heterozygous; Chinese | growth retardation, liver dysfunction, hypohidrosis | 34331832 |
| c.823delA / c.1141_1143delCTC | frameshift / in‑frame deletion | compound heterozygous | lethal neonatal, recto‑vaginal fistula | 35068072 |
| c.807delT p.(F269Lfs*37) / c.1746+1G>C | frameshift / splice | compound heterozygous; Chinese | cholestasis, death | 39528286 |
| c.1672C>T p.(Gln558Ter) / c.153+392A>G | nonsense (NMD) / deep intronic | compound heterozygous; Chinese | milder | 40225945 |
| c.821del p.(Arg274Lysfs*32) | frameshift | homozygous; Turkish | prenatal / fetal phenotype | 40213872 |
| c.906_907delinsA p.(His302GlnfsTer4) | frameshift | homozygous | complete loss of COG6 protein | 41362306 |
| Novel homozygous variant (described as nonsense in the title) | — | Moroccan | severe CDG with DSD | 33394555 |

**Functional consequence:** loss of function, ranging from hypomorphic to null.
- Shaheen allele: "resulting in pronounced reduction of the normal transcript and consequent deficiency of COG6 protein" (PMID 23606727).
- c.1672C>T: "The paternal variant resulted in nonsense‑mediated mRNA decay" (PMID 40225945).
- c.906_907delinsA: "the complete absence of the COG6 subunit, impairment of two other cooperating subunits, and delayed retrograde transport" (PMID 41362306).
- Genotype-phenotype gradient: from "deep intronic mutations found in Shaheen syndrome as the mildest form" to "loss‑of‑function mutations leading to early lethal CDG phenotypes" (PMID 26260076).

**Not retrieved or not applicable**
- ACMG classifications from ClinVar and gnomAD allele frequencies were not retrieved.
- Somatic origin: not applicable.
- Epigenetic changes: none reported.
- Chromosomal abnormalities: none reported as causal.

## 5. Environmental information

- No environmental, lifestyle or infectious *cause* is known.
- Infections and fever precipitate complications: recurrent infections in 7/10 (PMID 26260076), and febrile HLH episodes (PMIDs 29445937, 42269412).
- Heat exposure is a hazard because of hypohidrosis (PMID 23606727).

## 6. Mechanism and pathophysiology

**Causal chain**

1. **Biallelic COG6 variants** (null, missense or splice‑hypomorphic) lead to reduced or absent COG6 protein. *Demonstrated in humans* (PMIDs 23606727, 40225945, 41362306).
2. **Loss of COG6** destabilises the COG lobe‑B subcomplex and impairs cooperating COG subunits. *Demonstrated in patient cells* (PMID 41362306).
3. **Defective COG‑mediated vesicle tethering** results in impaired retrograde intra‑Golgi and Golgi‑to‑ER transport, plus slower anterograde ER‑to‑Golgi transport.
   - Wild‑type COG6 "led to normalization of the COG complex‑depending retrograde protein transport after Brefeldin A treatment" (PMID 20605848).
   - Patient cells show "a significantly slower anterograde and retrograde ER‑Golgi transport" (PMID 36636598).
4. **Mislocalisation and instability of Golgi glycosyltransferases**, plus distorted Golgi architecture.
   - In COG6 knockout HEK293T cells: "Lobe A and Cog6 subunit KOs displayed a more severely distorted Golgi structure" (PMID 27066481). *In vitro.*
   - All COG knockout lines were "uniformly deficient in cis/medial‑Golgi glycosylation" (PMID 27066481).
5. **Combined N‑ and O‑glycosylation defects** affect secreted, membrane and lysosomal glycoproteins. These appear as abnormal transferrin isoforms (a type II CDG pattern).
   - Branch A (null or severe alleles): marked hypoglycosylation (PMIDs 20605848, 41362306).
   - Branch B (Shaheen deep‑intronic hypomorph): "none of the patients displayed any detectable abnormality in the glycosylation pattern of transferrin" (PMID 23606727). Partial residual function is enough for transferrin but not for other substrates. One substrate candidate is STX6, which the same study found to be markedly deficient.
6. **Multi‑organ dysfunction** follows from hypoglycosylated substrates.
   - Liver: hepatopathy and coagulation‑factor deficiency, leading to bleeding (PMID 20605848). The link is *inferred*.
   - Brain: microcephaly, intellectual disability, delayed myelination. Mechanism *inferred*.
   - Skin and adnexa: hypohidrosis, hyperkeratosis, enamel hypoplasia. Mechanism *inferred*. Sweat gland numbers are reportedly normal (OMIM 615328 summary).
   - Gonadal development: proposed defective glycosylation of ADAM metalloproteases leads to male DSD. This is a *hypothesis*: "We hypothesize that the severe COG6 gene mutation interferes with glycosylation of a disintegrin and metalloprotease family members" (PMID 33394555).
   - Immune system: recurrent infections and dysregulated inflammation leading to HLH. Mechanism *not established* (PMIDs 29445937, 42269412).

**Molecular pathways:** Golgi vesicle tethering (COG–SNARE interaction); N‑linked and mucin‑type O‑linked glycosylation; retrograde Golgi transport.

**Suggested GO terms (labels only)**
- Biological process: retrograde vesicle‑mediated transport, Golgi to endoplasmic reticulum; intra‑Golgi vesicle‑mediated transport; protein N‑linked glycosylation; protein O‑linked glycosylation; Golgi organization.
- Cellular component: Golgi transport complex; Golgi apparatus; Golgi membrane.

**Suggested CL terms (labels only):** hepatocyte; fibroblast (the diagnostic cell model); keratinocyte; eccrine sweat gland cell; neuron; oligodendrocyte; ameloblast; natural killer cell / macrophage (HLH).

**Omics findings**
- Glycoproteomic and glycomic profiling identified candidate glycobiomarkers (Pakanová et al., 2025, *Hum Mutat*, PMID 41362306).
- No transcriptomic, single‑cell, spatial or CRISPR‑screen data are specific to the disease. Generic COG knockout panels exist (PMID 27066481).

## 7. Anatomical structures affected

- **Primary organs:** liver, brain (central nervous system), skin and sweat glands, teeth (enamel), immune and hematopoietic system.
- **Secondary organs:** gastrointestinal tract (diarrhoea, malrotation); external genitalia/gonads; joints (contractures, laxity); coagulation system.
- **Subcellular:** Golgi apparatus (primary), ER–Golgi intermediate compartment, ER.
- **Lateralisation:** systemic and bilateral.
- **Suggested UBERON labels:** liver; brain; skin of body; eccrine sweat gland; tooth enamel; external genitalia; intestine.

## 8. Temporal development

- **Onset:** prenatal to neonatal for severe alleles (prenatal anomalies in 8 of 28 patients, PMID 40213872). Infancy or early childhood for milder forms.
- **Course:**
  - Microcephaly is often progressive (PMIDs 23606727, 36636598).
  - Severe forms progress rapidly to death in infancy (6/10 early lethality, PMID 26260076).
  - Milder forms (Shaheen syndrome) are chronic and lifelong, with episodic hyperthermic and febrile crises.
- **Remission:** none.
- **Critical periods:** the neonatal period (bleeding, skin barrier failure) and febrile illnesses (HLH; PMID 42269412).

## 9. Inheritance and population

- **Inheritance:** autosomal recessive. Penetrance appears complete for biallelic variants. Expressivity is highly variable even for the same genotype (PMID 23430903).
- **Number of published patients:**
  - 18 by 2022 (PMID 35068072).
  - "less than 20" with 12 variants by 2020 (PMID 32683677).
  - 21 (PMID 32905044).
  - 28 by 2025 (PMID 40213872).
  - Shaheen syndrome adds 12 patients from 3 Saudi families (OMIM summary).
- **Prevalence and incidence:** unknown (ultra‑rare). Orphanet prevalence was not retrieved.
- **Founder effects:**
  - Saudi tribal founder for c.1167‑24A>G (PMID 23606727).
  - Possible Southeastern European founder for p.(Arg171*): "The presence of a founder mutation in the geographical area is possible" (PMID 35048409).
- **Consanguinity:** frequent.
- **Populations reported:** Moroccan, Saudi, Turkish, Greek, Bulgarian, Albanian, Swedish, Chinese, Israeli/Arab. The last attribution is inferred from Mandel et al.; the abstract does not specify it.
- **Sex ratio:** both sexes are affected. The male DSD phenotype has drawn attention to males.
- **Not retrieved:** carrier frequency, germline mosaicism and anticipation (anticipation is not expected for this disease).

## 10. Diagnostics

**Biochemical testing**
- Serum transferrin isoelectric focusing (type II pattern) and apolipoprotein C‑III IEF (O‑glycosylation).
- A normal transferrin result **does not exclude** the disease, because transferrin is normal in Shaheen syndrome (PMID 23606727).
- Glycomic and glycoproteomic profiling (PMID 41362306).

**Functional cell studies**
- Fibroblast Brefeldin A retrograde‑transport assay (PMID 20605848).
- ER–Golgi transport kinetics (PMID 36636598).
- Western blot for COG subunits (PMID 41362306).

**Genetics**
- Exome or genome sequencing is the main route.
  - The Shaheen allele was found by exome sequencing (PMID 23606727).
  - Trio genome sequencing plus RT‑PCR resolved a deep intronic variant (c.153+392A>G) that exome sequencing would miss (PMID 40225945).
- RNA studies (RT‑PCR) help classify splice variants (PMIDs 39528286, 40225945).
- CDG gene panels that include COG genes are also used.
- CMA, karyotype, FISH, mtDNA and repeat‑expansion testing: not relevant.

**Routine labs and imaging**
- Labs: liver enzymes, coagulation (vitamin K deficiency), and ferritin, triglycerides and fibrinogen when HLH is suspected (PMID 29445937).
- Brain MRI: delayed myelination (PMID 36636598); corpus callosum dysgenesis (PMID 35068072).

**Differential diagnosis**
- Other COG‑CDGs (COG1, 2, 4, 5, 7, 8).
- Other type II CDGs (e.g., ATP6V0A2, TMEM165).
- Restrictive dermopathy (neonatal skin form, PMID 32905044).
- Ectodermal dysplasias (hypohidrosis with enamel defects).
- Primary HLH.

**Screening:** no newborn screening exists. Prenatal diagnosis is feasible once familial variants are known (PMID 34331832).

## 11. Outcome and prognosis

- **Mortality:** early lethality in 6/10 of the early cohort (PMID 26260076). Neonatal‑lethal forms are linked to null alleles and skin/arthrogryposis presentations (PMIDs 32905044, 35048409, 35068072).
- **Survival:** milder genotypes, such as Shaheen syndrome and some compound heterozygotes, survive into childhood or beyond with severe intellectual disability (PMIDs 23606727, 40225945).
- **Prognostic factors:** genotype severity (null vs hypomorphic, PMID 26260076); neonatal skin involvement; liver failure.
- **Complications:** HLH, sepsis, hyperthermia, bleeding.
- **Not available:** formal survival statistics and QoL data.

## 12. Treatment

There is **no disease‑specific therapy**. Management is supportive.

| Intervention | Rationale / evidence | Suggested NCIT label |
|---|---|---|
| Vitamin K supplementation, management of coagulopathy | index case with vitamin K deficiency (PMID 20605848) | Vitamin K |
| Early or prophylactic corticosteroids during febrile episodes | "Early or prophylactic corticosteroid therapy during febrile episodes appeared to mitigate both the severity" (PMID 42269412). Observational, 3 patients. | Corticosteroid therapy |
| HLH‑directed therapy | case report (PMID 29445937) | Immunosuppressive therapy |
| Temperature control and avoiding overheating | hypohidrosis (PMID 23606727) | Supportive care |
| Nutrition and gastrointestinal support; infection prophylaxis or treatment | supportive | Nutritional support; Antibiotic therapy |
| Physical, occupational and speech therapy; dental care | supportive | Physical therapy; Speech therapy; Dental care |
| Liver transplantation | a 2026 systematic review covers CDGs generally (Lipiński, *J Pediatr Gastroenterol Nutr*, PMID 43010644). I did not retrieve COG6‑specific outcomes. | Liver transplantation |

- **Gene, RNA or cell therapy:** none. Retroviral COG6 complementation corrected the phenotype in patient fibroblasts *in vitro only* (PMID 20605848).
- **Clinical trials:** I found no COG6‑specific NCT trials. ClinicalTrials.gov was not queried directly.
- **Pharmacogenomics:** not applicable.

## 13. Prevention

- **Primary:** genetic counselling. Recurrence risk is 25% per pregnancy for carrier couples.
- **Reproductive options:** prenatal diagnosis (PMID 34331832) or preimplantation genetic testing once familial variants are known. Cascade carrier testing in consanguineous or founder populations (Saudi; Southeastern Europe).
- **Tertiary:** prevent hyperthermia; treat infections promptly; monitor for HLH, with early steroids where appropriate (PMID 42269412); monitor liver and coagulation.
- **Vaccination, public‑health and environmental measures:** not specifically applicable. Routine immunisation is assumed; no source was retrieved.

## 14. Other species and natural disease

- **Naturally occurring disease in animals:** none reported. OMIA was not queried.
- **Orthologues:** COG6 is conserved from yeast (Cog6p) to mammals. Yeast COG complex interaction studies exist (Ishii et al., 2018, *Cell Struct Funct*, PMID 29899178).
- **Taxon and Gene IDs:** not retrieved.
- **Zoonotic potential:** none.

## 15. Model organisms

- **Mouse (Cog6, MGI:1914792)**
  - IMPC phenotyped the *Cog6^tm1a* allele.
  - Annotations span 7 of 24 physiological systems: homeostasis/metabolism, immune (NK and NKT cell numbers), pigmentation, integument, eye, hematopoietic and skeleton ([IMPC](https://mousephenotype.org/data/genes/MGI:1914792)).
  - MGI lists about 71 phenotype annotations ([MGI](https://www.informatics.jax.org/marker/MGI:1914792)).
  - Recapitulation: partial. Integument and immune findings parallel the human disease. Neurological and liver recapitulation has not been characterised.
- **Human cells**
  - HEK293T COG6 knockout via CRISPR (Bailey Blackburn et al., 2016, *Front Cell Dev Biol*, PMID 27066481): severe Golgi distortion and cis/medial glycosylation defects.
  - Patient fibroblasts are the standard model, used in PMIDs 20605848, 36636598 and 41362306.
- **Zebrafish, Drosophila, iPSCs and organoids:** no COG6‑specific models were retrieved.
- **Limitations:** no whole‑organism model reproduces the human neurodevelopmental, hepatic and ectodermal triad.

---

## Key references (PMIDs)

| PMID | First author, year | Content |
|---|---|---|
| 20605848 | Lübbehusen 2010 | first patient |
| 23430903 | Huybrechts 2012 | second patient |
| 23606727 | Shaheen 2013 | Shaheen syndrome |
| 26260076 | Rymen 2015 | key features and review |
| 27066481 | Bailey Blackburn 2016 | HEK293T COG knockouts |
| 29445937 | Althonaian 2018 | HLH |
| 29709711 | Li 2019 | first Chinese patient |
| 32683677 | Mandel 2020 | male DSD |
| 32905044 | Komlosi 2020 | neonatal skin phenotype |
| 33394555 | Lugli 2021 | DSD |
| 34331832 | Zhao 2021 | prenatal diagnosis |
| 35048409 | Ververi 2022 | possible founder allele |
| 35068072 | Cirnigliaro 2022 | novel malformation |
| 36636598 | Xia 2023 | Swedish cases and review |
| 39528286 | Zhang 2024 | Chinese case |
| 40225945 | Zhang 2024 | milder phenotype |
| 40213872 | Guterman 2025 | prenatal phenotype |
| 41362306 | Pakanová 2025 | glycosylation profiling |
| 42269412 | de Laitre 2026 | recurrent HLH |
| 43010644 | Lipiński 2026 | liver transplant in CDG |

**Web sources:**
- [MedGen C3553230](https://https.ncbi.nlm.nih.gov/medgen/C3553230)
- [GARD](https://rarediseases.info.nih.gov/assets/singles/10944.json)
- [OMIM 606977 mirror](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/606977)
- [KEGG H03097](https://www.kegg.jp/entry/H03097)
- [CISMeF 615328](https://www.cismef.org/page/detail/en/MIM_PH_615328)
- [IMPC Cog6](https://mousephenotype.org/data/genes/MGI:1914792)
- [MGI Cog6](https://www.informatics.jax.org/marker/MGI:1914792)
- [Rymen 2015](https://www.pubmed.gov/26260076/)
- [Huybrechts 2012 (PMC3509899)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3509899)
- [Disease Ontology DOID:0070264](https://disease-ontology.org/term/DOID:0070264/owl)

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 20 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 19 |
| Quoted claims found in source | 19 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 20 |
| On topic | 17 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 7 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 4 |
| Terms whose name was checked | 2 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0013810` (2 mentions) - the report calls it "MONDO"; MONDO calls it **COG6-congenital disorder of glycosylation**
- `DOID:0070264` (5 mentions) - the report calls it "DOID"; DOID calls it **congenital disorder of glycosylation type IIl**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `ORPHA`, `MGI`.