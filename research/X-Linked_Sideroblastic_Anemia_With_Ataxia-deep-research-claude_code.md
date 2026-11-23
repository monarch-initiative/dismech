---
provider: claude_code
model: claude-fable-5-2, claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-18T23:30:21.453169'
end_time: '2026-11-18T23:44:20.451068'
duration_seconds: 839.0
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: X-Linked Sideroblastic Anemia With Ataxia
  mondo_id: MONDO:0010524
  category: Mendelian
  causal_genes: ABCB7
  omim_id: OMIM:301310
  synonyms: ASAT; Pagon-Bird-Detter syndrome; X-linked sideroblastic anaemia with
    spinocerebellar ataxia; X-linked sideroblastic anemia with spinocerebellar ataxia;
    XLSA-A; anaemia sideroblastic and spinocerebellar ataxia; anemia, sideroblastic,
    with ataxia, X-linked recessive; sideroblastic anaemia with spinocerebellar ataxia
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
  - claude-fable-5-2
  - claude-haiku-5-5
  - claude-opus-5-5
  web_search_requests: 4
  num_turns: 41
  total_cost_usd: 2.620197
  session_id: d0f9a20f-d3cb-4ca2-b129-04d7d5a0d749
  stop_reason: end_turn
  permission_denials: 1
  denied_tools:
  - Bash
  tool_calls: 40
  retrieval_calls: 39
  assistant_text_blocks: 4
fell_back: true
requested_provider: antigravity
provider_attempts:
- provider: antigravity
  succeeded: false
  error_type: ProviderQuotaError
  remedy: the plan's usage limit is spent
  retryable: false
- provider: claude_code
  succeeded: true
citation_count: 9
reference_validation:
  total_references: 33
  verified: 32
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.03
  quotes_checked: 17
  quotes_valid: 11
  quotes_unsupported: 6
  unsupported_quote_references:
  - PMID:10196363
  - PMID:34354969
  - PMID:33157103
  - PMID:17192393
  quotes_not_checkable: 1
  relevance_assessed: 32
  on_topic: 26
  unresolved_references:
  - PMID:38743629
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 76
  verified: 72
  not_found: 0
  obsolete: 0
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 40
  labels_matching: 38
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0010524
    reported_labels:
    - MONDO
    ontology_label: X-linked sideroblastic anemia with ataxia
  labels_variant: 1
  unresolvable_prefixes:
  - OMIM
  - ORPHA
  service_unreachable: 1
  obsolescence_unchecked: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** X-Linked Sideroblastic Anemia With Ataxia
- **MONDO ID:** MONDO:0010524 (if available)
- **Causal gene(s):** ABCB7
- **OMIM:** OMIM:301310
- **Synonyms:** ASAT; Pagon-Bird-Detter syndrome; X-linked sideroblastic anaemia with spinocerebellar ataxia; X-linked sideroblastic anemia with spinocerebellar ataxia; XLSA-A; anaemia sideroblastic and spinocerebellar ataxia; anemia, sideroblastic, with ataxia, X-linked recessive; sideroblastic anaemia with spinocerebellar ataxia
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **X-Linked Sideroblastic Anemia With Ataxia** covering all of the
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

Still researching: I have the core PubMed list for ABCB7/XLSA-A and am now pulling the key abstracts.

Still gathering sources — now checking for post-2021 case reports and the D'Hooghe variant.

Pulling ClinVar pathogenic ABCB7 variant details now.

# X-Linked Sideroblastic Anemia with Ataxia (XLSA/A; MONDO:0010524): ABCB7-related disease

**How I scoped this.** This report covers MONDO:0010524 / OMIM:301310, which is caused by hemizygous variants in **ABCB7** (HGNC:48; UniProt O75027). ABCB7 is a mitochondrial inner-membrane ATP-binding cassette transporter at Xq13. This disease is distinct from ALAS2-related X-linked sideroblastic anemia, which has no ataxia.

**Which sources I could and could not reach:**
- **Reached:** PubMed records through NCBI E-utilities, the UniProt flat file, ClinVar summaries, the Monarch and JAX HPO APIs, MedlinePlus, ClinicalTrials.gov, and the full text of PMID 34354969 and of PMC1852240.
- **Not reached:** the OMIM, Orphanet and PubMed web pages and the GeneReviews (NBK1321) page were blocked (403, CAPTCHA or cookie walls). I did not query gnomAD.

**How identifiers are handled.** I only give identifiers I retrieved in this session. Where I could not retrieve an ontology ID (CL, UBERON, CHEBI, NCIT), I give the label and mark it "ID not retrieved". All direct quotes are short strings returned verbatim by my fetch tools.

---

## 1. Disease Information

**Overview.** XLSA/A is a very rare X-linked recessive syndrome. It combines:
- early-onset, mostly non-progressive or slowly progressive cerebellar ataxia;
- mild, usually asymptomatic hypochromic/microcytic sideroblastic anemia.

Monarch/MONDO defines it as "A rare syndromic, inherited form of sideroblastic anemia" caused by ABCB7 mutations, with "mild to moderate anemia" and early-onset spinocerebellar ataxia ([Monarch MONDO:0010524](https://api.monarchinitiative.org/v3/api/entity/MONDO:0010524)).

Allikmets et al. described it as "a recessive disorder with infantile to early-childhood onset of nonprogressive cerebellar ataxia and mild anemia with hypochromia and microcytosis" (PMID 10196363, paraphrased from the abstract). UniProt says the disease involves "non-progressive cerebellar ataxia and mild anemia" ([UniProt O75027](https://rest.uniprot.org/uniprotkb/O75027.txt)).

D'Hooghe et al. call it "a rare cause of early onset ataxia, which may be overlooked due to the usually mild asymptomatic anemia" (PMID 22398176).

**Identifiers** (from Monarch/MONDO unless noted):

| Resource | ID |
|---|---|
| MONDO | MONDO:0010524 |
| OMIM | 301310 (MedlinePlus and UniProt also label 301310 as "SCAX6", spinocerebellar ataxia X-linked 6 with or without sideroblastic anemia) |
| Orphanet | ORPHA:2802 |
| UMLS / MedGen | C1845028 / 335078 |
| MeSH (supplementary concept) | C536358 |
| GARD | 0000668 |
| DOID | 0050554, 0060064 |
| SNOMED CT | 719816006 |
| ICD-10 / ICD-11 | Not listed in the MONDO record and not retrieved. The Orphanet page was blocked. |
| GTR | C1845028 ([MedlinePlus](https://medlineplus.gov/genetics/condition/x-linked-sideroblastic-anemia-and-ataxia/)) |

**Synonyms.** ASAT; XLSA/A; XLSA-A; SCAX6; Pagon-Bird-Detter syndrome; X-linked sideroblastic anemia (anaemia) with spinocerebellar ataxia; sideroblastic anemia with spinocerebellar ataxia; anemia, sideroblastic, with ataxia, X-linked recessive; X-linked spinocerebellar ataxia-6 with or without sideroblastic anemia.

**Type of evidence.** Everything here comes from aggregated, disease-level resources and published case or family reports. There are about 6–7 families in total, and no EHR or registry cohorts.

---

## 2. Etiology

**Causal factors.**
- The cause is genetic: hemizygous germline missense variants in ABCB7 (Xq13).
- Mouse work concludes that "XLSA/A is due to partial loss of function mutations in Abcb7" that "directly or indirectly inhibit heme biosynthesis" (Pondarré 2007, PMID 17192398).
- Every human variant reported so far is missense. Complete loss is lethal in mice (PMID 16467350), which fits a hypomorphic disease mechanism. That link is an inference.

**Genetic risk factors.**
- **Sex:** affected individuals are male. Xiong et al. state "All affected patients were male" (PMID 34354969).
- **Family history:** the main risk factor is a carrier mother. Fathers cannot pass the condition to sons ([MedlinePlus](https://medlineplus.gov/genetics/condition/x-linked-sideroblastic-anemia-and-ataxia/)).
- **No susceptibility loci or GWAS signals** were found.
- **Possible modifier or confounder:** in the Buryat family with the ABCB7 p.Gly682Ser variant, affected males also carried a deletion including ATP7A exon 2 and a complete PGAM4 deletion, but had no signs of Menkes disease (PMID 26242992). Whether these contribute is unknown.

**Environmental risk factors.** None documented.

**Protective factors.** None documented, genetic or environmental.

**Gene–environment interactions.** None documented. CTD and PheGenI were not specifically queried.

---

## 3. Phenotypes

The main sources are:
- the HPO annotation for OMIM:301310, with frequencies, from [JAX HPO API](https://ontology.jax.org/api/network/annotation/OMIM:301310);
- the literature review in Xiong et al. 2021 (PMID 34354969; full text at [Frontiers](https://www.frontiersin.org/journals/pediatrics/articles/10.3389/fped.2021.692459/full)).

The HPO frequency counts are small-denominator literature tallies.

### Neurological

| Phenotype | HPO | Frequency | Onset / course | Notes |
|---|---|---|---|---|
| Nonprogressive cerebellar ataxia | HP:0002470 | 11/11 (HPO) | Infancy to early childhood; Xiong: onset before age 2 | Core feature. Mainly truncal ataxia ([MedlinePlus](https://medlineplus.gov/genetics/condition/x-linked-sideroblastic-anemia-and-ataxia/)) |
| Ataxia | HP:0001251 | 3/3 | Early | Xiong: ataxic gait 7/7 |
| Gait disturbance | HP:0001288 | 7/7 | Childhood | Delayed walking in nearly all patients (PMID 34354969) |
| Postural instability | HP:0002172 | 9/9 | — | — |
| Dysarthria | HP:0001260 | 15/15 | Childhood | — |
| Dysmetria | HP:0001310 | 3/3 | — | — |
| Dysdiadochokinesis | HP:0002075 | 4/4 | — | — |
| Intention tremor | HP:0002080 | 1/1 | — | — |
| Nystagmus | HP:0000639 | 9/9 (HPO); 9/16 (Xiong) | Can start in infancy (nystagmus at 1 month in the Chinese proband) | — |
| Strabismus | HP:0000486 | 3/3 (HPO); 5/8 (Xiong) | — | — |
| Ophthalmoplegia | HP:0000602 | 5/5 | — | — |
| Abducens palsy | HP:0006897 | 1/1 | — | — |
| Global developmental delay | HP:0001263 | 15/15 | Infancy | Delayed language in 8 patients (Xiong) |
| Language impairment | HP:0002463 | 3/3 | — | — |
| Hypotonia | HP:0001252 | 3/3 | Infancy | — |
| Hyperreflexia | HP:0001347 | 3/3 | — | Pyramidal signs |
| Babinski sign | HP:0003487 | 3/3 | — | — |
| Clonus | HP:0002169 | 2/2 | — | — |
| Diminished deep tendon reflex | HP:0001315 | 3/3 | — | Seen in the Chinese proband |
| Cerebellar hypoplasia | HP:0001321 | 7/7 | Congenital/early | "Striking selective cerebellar hypoplasia" on CT at age 18 in one patient (Xiong review) |
| Cerebellar atrophy | HP:0001272 | 2/2 | Later life | Atrophy at age 50 in two patients. "Cerebellum atrophy probably occurs in the later stages of the disease" (PMID 34354969) |
| Seizure | HP:0001250 | 1/1 | 11 months | Single case (PMID 34354969) |
| Interictal EEG abnormality | HP:0025373 | 1/1 | — | Single case |
| Cognitive impairment / Dementia | HP:0100543 / HP:0000726 | 1/1 each | Adult | Single patients |
| Autism | HP:0000717 | 1/1 | Childhood | Screening scores in one case only |
| Depression / Schizophrenia | HP:0000716 / HP:0100753 | 1/1 each | Adult | Isolated reports, causal link unclear |
| Myoclonus | HP:0001336 | 1/1 | — | — |
| Basal ganglia gliosis / abnormal basal ganglia MRI signal | HP:0006999 / HP:0012751 | 1/1 | — | Single case with a left basal ganglia lacunar infarct |
| Abnormal brainstem morphology | HP:0002363 | 2/2 | — | — |
| Dysphonia | HP:0001618 | 2/2 | — | — |

### Hematological and laboratory

| Phenotype | HPO | Frequency | Notes |
|---|---|---|---|
| Sideroblastic anemia | HP:0001924 | 3/3 (HPO). Ring sideroblasts in all 4 patients and 2 carriers who had marrow exams (Xiong) | — |
| Anemia | HP:0001903 | 5/5 (HPO). Mild anemia in 8/12 patients and 1/7 carriers (Xiong) | Usually mild and asymptomatic |
| Hypochromic microcytic anemia | HP:0004840 | 4/4 | The Chinese proband instead had normocytic indices (Hb 11.3 g/dL, MCV 85.2 fL) |
| Increased erythrocyte protoporphyrin concentration | HP:0012187 | 8/8 patients and 4/6 carriers (Xiong) | A sensitive biochemical marker |
| Pappenheimer bodies | HP:0020081 | 3/3 | Iron-positive stippling, also seen in a carrier mother (PMID 11843825) |
| Anisocytosis / Poikilocytosis | HP:0011273 / HP:0004447 | 3/3 each | Dimorphic smear in carriers (PMID 4045952) |
| Target cells / Howell-Jolly bodies | HP:0034280 / HP:0032550 | 1/1 each | — |
| Erythroid hyperplasia / Bone marrow hypercellularity | HP:0012132 / HP:0031020 | 1/1, 2/2 | — |
| Pallor | HP:0000980 | 1/1 | — |
| Organic aciduria | HP:0001992 | 1/1 | Single case, with unexplained raised 2-hydroxyisobutyric, glycolic and oxalic acids (PMID 34354969) |

### Growth and other

| Phenotype | HPO | Frequency | Notes |
|---|---|---|---|
| Short stature | HP:0004322 | 3/3 | — |
| Intrauterine growth retardation | HP:0001511 | 3/3 | — |
| Weight loss | HP:0001824 | 2/2 | — |
| Cryptorchidism | HP:0000028 | 1/1 | Newly reported in a single case (PMID 34354969) |

**Severity and course.** The ataxia is described as early-onset and non-progressive (PMIDs 4045952, 10196363). Late cerebellar atrophy has been seen, so slow progression in adulthood cannot be excluded (PMID 34354969). The anemia is mild, and "No patient needed transfusion" according to Xiong's review. Xiong concludes: "Patients with XLSA/A always present striking ataxia and mild anemia at the early age."

**Quality of life.** No EQ-5D, SF-36 or other quality-of-life studies were found. From the clinical descriptions, the burden comes mainly from motor disability (delayed walking, ataxic gait, dysarthria) and from developmental delay where it is present. The anemia adds little burden.

---

## 4. Genetic / Molecular Information

### Gene

- **Gene:** ABCB7, ATP-binding cassette subfamily B member 7 (HGNC:48; UniProt O75027). The protein is 752 aa and has a 22-residue mitochondrial transit peptide.
- **Location:** Xq13.1–q13.3 (PMID 9621516). GRCh38 chrX:~75.06–75.07 Mb (ClinVar).
- **Protein:** "a putative half-type transporter, consists of 752 amino acids", 48.9% identical to yeast Atm1p (PMID 9621516).
- **Gene structure:** 16 exons (PMID 11050011).
- **Domains:** Pfam PF00664 (ABC_membrane) and PF00005 (ABC_tran).
- **Structures:** cryo-EM PDB 7VGF (AMP-PNP-bound, 3.3 Å; PMID 35041979), plus 23PG, 23PH and 23PI (up to 2.3 Å, CoPP/GSH-bound; PMID 42103889) ([UniProt](https://rest.uniprot.org/uniprotkb/O75027.txt)).

### Reported disease variants

Legacy cDNA positions differ from current ClinVar numbering on NM_001271696.3. Several isoforms explain the shifted protein numbering; for example, ClinVar lists V411L also as V412L.

| Protein | ClinVar HGVS (NM_001271696.3) | Legacy description | Family / phenotype | ClinVar classification | PMID |
|---|---|---|---|---|---|
| p.Ile400Met | c.1200T>G | I400M in a predicted transmembrane segment. Absent from "at least 600 chromosomes" of controls | Original Pagon/Raskind kindred, 5 affected males; Xq13 linkage, LOD ≥2.60 (PMID 1671320) | Pathogenic (VCV000011574) | 10196363 |
| p.Glu433Lys | c.1297G>A | Legacy "G→A at nt 1305", exon 10 | Two brothers. Mutant protein poorly complemented yeast Δatm1 for cytosolic Fe/S maturation | Pathogenic (VCV000011575) | 11050011, 33157103 |
| p.Val411Leu | c.1231G>C | Legacy "G→C transversion at position 1299". Predicts V411L "at the beginning of the last of six putative transmembrane regions". Absent from 200 normal alleles | Two brothers, a carrier mother and an affected uncle | Pathogenic (VCV000011576). A different allele, c.1231G>T, giving the same p.Val411Leu, is Likely pathogenic (VCV003235083) | 11843825 |
| p.Glu208Asp | c.624A>T | — | Fourth family (Belgian report) | Pathogenic (VCV000126455) | 22398176 |
| p.Gly682Ser | c.2044G>A | "glycine to serine at position 682" | Large Buryat family with X-linked congenital cerebellar ataxia "who had no evidence of sideroblastic anemia" | Likely pathogenic (VCV000208533) | 26242992 |
| p.Asp675Gly (paper) | Paper: c.2024A>G. ClinVar has c.2021A>G (p.Asp674Gly; VCV003248639) at chrX:75060245, with **conflicting** classifications and the trait XLSA/A | Absent from gnomAD and ClinVar at publication. PolyPhen 0.996, SIFT 0.001, PROVEAN −6.41. ACMG **likely pathogenic** per the authors | First Chinese family | Whether the ClinVar record is the same variant under another transcript is **unconfirmed**. ClinVar's isoform list includes D674G but not D675G | 34354969 |

**Other ClinVar Likely pathogenic records** with no stated condition: p.Thr184Ile (c.551C>T; VCV003234629), p.Gly388Ser (c.1162G>A; VCV000450083) and p.Met412Thr (c.1235T>C; VCV000372878).

**ClinVar counts.** ClinVar lists 399 single-gene ABCB7 records. Most are VUS, and a filtered query returned many VUS. Only the rows above are P/LP. p.Gly290Ser (VCV000213988) is also conflicting.

**Variant class.** All disease-associated variants confirmed so far are missense, and they cluster in or near transmembrane helices and the C-terminal nucleotide-binding domain. Yan et al. mapped four disease missense mutations onto the structure as a "hotspot map" (PMID 35041979). In the 2026 structure, E433K is explained by the substrate cavity. "The conserved residue F426 controls substrate entrapment and release as a molecular gate" (PMID 42103889).

**Allele frequency.** gnomAD was not queried. Several founder variants were described as absent from hundreds of control chromosomes (PMIDs 10196363, 11843825), and p.Asp675Gly was absent from gnomAD (PMID 34354969).

**Origin.** All variants are germline. In the Chinese family, the authors inferred grandmaternal germline mosaicism: "The proband's grandmother was very likely to harbor germline mosaicism for the ABCB7 gene variant" (PMID 34354969). This is an inference, not a demonstration.

Somatic ABCB7 involvement is a separate topic. In acquired MDS with ring sideroblasts, SF3B1 mutation causes ABCB7 mis-splicing: "Coordinated missplicing of TMEM14C and ABCB7 causes ring sideroblast formation in SF3B1-mutant myelodysplastic syndrome" (PMID 34861039; also 27211273, 23070040, 18398482). Loss of ABCB7 through idic(X)(q13) has also been reported in RARS (PMID 21380928). These are relevant to mechanism but are not XLSA/A.

**Functional consequence.** The variants cause partial loss of function, i.e. they are hypomorphic. In yeast, I400M caused partial loss of Atm1 function (PMID 10196363), and "E433 is important for cluster transport" (PMID 33157103, paraphrase). There is no evidence of gain of function or a dominant-negative effect.

**Modifier genes.** None established. The ATP7A/PGAM4 deletions in the Buryat family are a possible confounder (PMID 26242992).

**Epigenetics.** No disease-specific data. X-inactivation in carrier females has not been systematically reported in humans. In mice, X-inactivation assays showed that Abcb7 is required in many tissues, with "an X-linked parent-of-origin lethality effect" (PMID 16467350).

**Chromosomal abnormalities.** Large X-chromosome CNVs spanning ABCB7 appear in ClinVar but are not a recognized cause of XLSA/A. The acquired idic(X)(q13) in myeloid neoplasms removes or disrupts ABCB7 (PMIDs 20093295, 21380928).

---

## 5. Environmental Information

- **Environmental factors, lifestyle factors and infectious agents:** none are known or applicable. XLSA/A is a monogenic disorder.
- **Iron overload:** unlike other sideroblastic anemias, XLSA/A is reported not to cause significant systemic iron overload ([MedlinePlus](https://medlineplus.gov/genetics/condition/x-linked-sideroblastic-anemia-and-ataxia/), as summarized via search).

---

## 6. Mechanism / Pathophysiology

### Causal chain

1. **Hemizygous missense variant in ABCB7** (Xq13) in a male **leads to** a partially functional ABCB7 homodimer in the mitochondrial inner membrane.
   - Demonstrated: yeast complementation (PMIDs 10196363, 11050011) and mouse genetics (PMID 17192398).
2. **Reduced ATP-dependent export of a mitochondrial substrate** from the matrix to the cytosol **results from** step 1.
   - **Branch 2a, Fe-S export (best supported):** ABCB7 "Exports glutathione-coordinated iron-sulfur clusters such as [2Fe-2S]-(GS)4" (UniProt O75027). Supporting work: Pearson & Cowan (PMID 33157103); yeast Atm1 structures (PMIDs 24604199, 35896548). Braymer et al. found that cytosolic [2Fe-2S] protein assembly needs ISC machinery, Atm1/ABCB7 and GSH, and that "the most critical GSH requirement was assigned to Atm1-dependent export" (PMID 38743629).
   - **Branch 2b, metalloporphyrin/heme export (newer, single in vitro study):** "ATPase activity of ABCB7 is stimulated by iron and cobalt protoporphyrin IX" with GSH. The cavity "accommodates two stacked CoPP molecules conjugated by two GSH cysteine thiols" (Ju 2026, PMID 42103889). How much this matters in vivo is not established.
3. **Defective cytosolic Fe-S protein maturation leads to** loss of cytosolic aconitase activity and constitutive IRP1 RNA-binding activity. In other words, the cell falsely senses cytosolic iron deficiency.
   - Demonstrated in HeLa knockdown cells, which showed an "iron-deficient phenotype with mitochondrial iron overload" (PMID 17192393), and in mouse liver (PMID 16467350).
4. **IRP activation results in** a branch:
   - **4a.** More iron uptake (transferrin receptor) **leads to** mitochondrial iron accumulation (PMIDs 17192393, 30765471).
   - **4b.** IRP binding to the ALAS2 5′-IRE **represses ALAS2 translation**, so heme synthesis falls in erythroid cells (PMID 30765471).
5. **Impaired heme synthesis at the ferrochelatase step**. ABCB7 physically interacts with ferrochelatase (FECH), an Fe-S enzyme. "A dimeric ferrochelatase physically bridged ABCB7 and ABCB10 homodimers" (PMID 30765471). ABCB7 binds "the carboxy-terminal region containing the iron-sulfur cluster of ferrochelatase" (PMID 12480705).
   - ABCB7 loss **leads to** lower FECH stability and less iron insertion into protoporphyrin. This **results in** raised erythrocyte (zinc) protoporphyrin. In mice, the ZPP:heme ratio rose in proportion to E433K mutant red cells (PMID 17192398).
6. **In erythroblasts, mitochondrial iron overload plus heme deficiency leads to** ring sideroblast formation, defective hemoglobinization, oxidative-stress-triggered apoptosis and ineffective erythropoiesis (PMID 30765471, knockdown cells). The clinical result is **mild hypochromic/microcytic sideroblastic anemia with raised protoporphyrin**.
7. **Neurological branch (inferred, not demonstrated):** reduced Fe-S cluster and heme supply in developing cerebellar neurons is proposed to impair neuronal function. MedlinePlus says the shortage "likely" impairs nerve cell function. Kaplan proposed that "the biochemical feature common to these ataxias is increased oxidant damage" (PMID 11850112, paraphrased quote). Chiabrando reviews heme and Fe-S biogenesis in hereditary ataxias (PMID 32466579). Together these **result in** cerebellar hypoplasia, with possible later atrophy, and early-onset non-progressive ataxia.
   - No neuronal model of XLSA/A has demonstrated this. E433K chimeric mice showed no ataxia (PMID 17192398).
8. **Complete loss-of-function is incompatible with life.** In mice, Abcb7 is essential in extra-embryonic tissue (PMID 16467350), and induced deletion causes rapidly fatal pancytopenic marrow failure (PMID 17192398). This explains why only hypomorphic missense alleles are seen in patients (inferred).

**Upstream vs downstream.** The upstream steps are steps 1–2, the transport defect. The midstream steps are steps 3–5: the IRP1/iron-regulon disruption and FECH/heme synthesis. Downstream are steps 6–7, the cell-type-specific outcomes in erythroblasts and cerebellar neurons.

### Molecular pathways

- Mitochondrial iron-sulfur cluster (ISC) export and cytosolic iron-sulfur assembly (CIA).
- Heme biosynthesis (ALAS2 → FECH).
- The IRP/IRE iron regulon.
- KEGG and Reactome pathway IDs were not retrieved.

### Cellular processes

| Process | Evidence |
|---|---|
| Apoptosis due to oxidative stress (erythroid) | PMID 30765471 |
| Replication-induced DNA damage and a pro-B-cell developmental block, without increased ROS or ferroptosis | Conditional mouse, PMID 34762046 |
| Embryonic morphogenesis defects, premature apoptosis, ferric iron accumulation and oxidative stress | *C. elegans* abtm-1, PMID 21464130 |

### Protein dysfunction

Missense variants in transmembrane helices (I400M, V411L, E433K) affect the substrate-gating cavity. Variants such as E208D, G682S and D675G lie elsewhere; G682S and D675G are near or in the NBD region. The result is reduced transport, with the protein retained (partial loss of function).

### Immune involvement

ABCB7 "is required for bone marrow B cell development, proliferation, and class switch recombination" in mice (PMID 34762046). No immunodeficiency has been reported in XLSA/A patients.

### GO terms (from UniProt O75027)

- **Biological process:**
  - GO:0140466 iron-sulfur cluster export from the mitochondrion
  - GO:0016226 iron-sulfur cluster assembly
  - GO:1903331 positive regulation of iron-sulfur cluster assembly
  - GO:0006879 intracellular iron ion homeostasis
  - GO:0034755 iron ion transmembrane transport
  - GO:0006783 heme biosynthetic process
  - GO:0070455 positive regulation of heme biosynthetic process
  - GO:1903427 negative regulation of reactive oxygen species biosynthetic process
  - GO:0055085 transmembrane transport
- **Molecular function:**
  - GO:0140481 ABC-type iron-sulfur cluster transporter activity
  - GO:0015232 heme transmembrane transporter activity
  - GO:0005524 ATP binding
  - GO:0016887 ATP hydrolysis activity
  - GO:0042626 ATPase-coupled transmembrane transporter activity
  - GO:0042803 protein homodimerization activity
- **Cellular component:**
  - GO:0005743 mitochondrial inner membrane
  - GO:0005739 mitochondrion
  - GO:0043190 ATP-binding cassette (ABC) transporter complex

### Cell Ontology (labels only; CL IDs not retrieved)

Erythroblast (polychromatic and orthochromatic), sideroblast, reticulocyte, cerebellar Purkinje cell and granule cell (inferred), hematopoietic stem cell and pro-B cell (mouse), hepatocyte (mouse).

### Molecular profiling

No XLSA/A patient transcriptomic, proteomic, metabolomic, single-cell or CRISPR datasets were found.

- Medaka abcb7 mutant liver microarrays showed altered iron and lipid metabolism genes (PMID 19046159).
- Transcriptomic data exist for the acquired SF3B1-MDS analog (PMIDs 25428262, 27211273).

### Metabolic changes and CHEBI (labels; CHEBI IDs not retrieved)

Raised protoporphyrin IX / zinc protoporphyrin, mitochondrial iron, glutathione (a co-substrate), heme, and [2Fe-2S] cluster.

---

## 7. Anatomical Structures Affected

UBERON IDs were not retrieved, so labels only are given here.

- **Primary organs:**
  - Cerebellum (hypoplasia, later atrophy; PMID 34354969).
  - Bone marrow, specifically the erythroid lineage (ring sideroblasts, erythroid hyperplasia).
- **Secondary:**
  - Blood (hypochromic RBCs, Pappenheimer bodies).
  - Brainstem: abnormal brainstem morphology (HPO, 2/2).
  - Eye movement system: nystagmus, ophthalmoplegia, strabismus.
  - Testis: cryptorchidism, a single case. E433K mouse chimeras had testicular atrophy with iron deposition, which has not been seen in humans (PMID 17192398).
- **Body systems:** nervous system and hematopoietic system.
- **Tissue and cell level:** cerebellar cortex neurons (inferred) and bone marrow erythroid precursors.
- **Subcellular level:** mitochondrial inner membrane (GO:0005743). The cytosol and nucleus are affected secondarily, as the sites of Fe-S protein assembly. Perinuclear mitochondrial iron deposits form the "ring" in ring sideroblasts.
- **Lateralization:** the ataxia is bilateral and symmetric (truncal and gait). The basal ganglia infarct in one case was left-sided and is likely incidental.

---

## 8. Temporal Development

- **Onset:**
  - Congenital, infantile or early childhood. HPO lists congenital onset (HP:0003577, 3/6), infantile onset (HP:0003593, 2/4) and childhood onset (HP:0011463, 3/6). Xiong reports onset before age 2.
  - The onset is insidious, showing as motor delay. The Chinese proband sat at 1 year and walked at about 4 years (PMID 34354969).
- **Progression:**
  - The original kindred had a "non-progressive spinocerebellar syndrome" (PMID 4045952, paraphrase).
  - Monarch says "non-progressive or slowly progressive".
  - Cerebellar atrophy has been seen at age 50 (PMID 34354969).
  - This is an unresolved discrepancy between the sources. The anemia appears stable and lifelong.
- **Stages:** no formal staging.
- **Remission:** none. The condition is lifelong.
- **Critical periods:** cerebellar development in infancy and early childhood is the presumed window of vulnerability (inferred). Early diagnosis enables physical therapy and genetic counselling.

---

## 9. Inheritance and Population

- **Inheritance:** X-linked recessive (HP:0001419).
- **Prevalence:**
  - Unknown. MedlinePlus calls it a "rare disorder" with unknown prevalence.
  - **Family counts conflict between sources:**
    - 3 families before 2012 (PMID 22398176).
    - 4 families (GeneReviews, retired chapter).
    - 5 families (Orphanet, via the [PhenoDis mirror](https://iegext02.helmholtz-munich.de/phenodis/disease/show/3705); Xiong abstract).
    - 6 families with ABCB7 missense variants (Xiong text).
    - About 7 families if you include the Buryat family with ataxia but no anemia (PMID 26242992).
  - Xiong's patient count is itself inconsistent: 16 confirmed in the text versus 18 in the table.
  - GeneReviews (retired) notes prevalence is probably underestimated because the mild anemia goes unrecognized.
- **Incidence:** not available.
- **Penetrance:** appears complete for ataxia in hemizygous males. The anemia is variable (8/12 patients had anemia) and was absent in the Buryat family. This is variable expressivity.
- **Carrier females:**
  - No ataxia in carriers. Pagon: heterozygous women had normal neurological exams, but some had ring sideroblasts, dimorphic smears or raised protoporphyrin (PMID 4045952).
  - In Xiong's review, protoporphyrin was raised in 4/6 carriers and anemia was present in 1/7.
  - MedlinePlus says carriers may have small, pale RBCs.
  - Genomics England PanelApp reportedly allows that monoallelic females may be affected. That was seen only in a search summary and not verified.
- **Anticipation:** none (not a repeat disorder).
- **Germline mosaicism:** suspected in one family (PMID 34354969).
- **Founder effects:** none described. Each family has a private variant.
- **Consanguinity:** not relevant.
- **Carrier frequency:** unknown.
- **Geography:** families have been reported from the USA (Pagon/Raskind), Europe (Bekri; Maguire; D'Hooghe, Belgium), Russia/Buryatia (Mongolian ancestry) and China.
- **Sex ratio:** all reported affected patients are male (PMID 34354969).

---

## 10. Diagnostics

**Laboratory tests:**
- CBC and indices: mild anemia, low MCV/MCH, hypochromia; can be normocytic.
- Peripheral smear: dimorphic picture, Pappenheimer bodies or iron-positive basophilic stippling (PMIDs 11843825, 4045952).
- **Erythrocyte (zinc) protoporphyrin is raised.** This is a key discriminator from ALAS2-XLSA, where protoporphyrin is low. The ALAS2 comparison is a general hematology principle that I did not retrieve in this session. In XLSA/A, protoporphyrin was raised in 8/8 patients (PMID 34354969).
- Iron stores: normal (PMID 11843825).
- Bone marrow aspirate with Perls (Prussian blue) stain: ring sideroblasts.

**Imaging.** Brain MRI or CT may show cerebellar hypoplasia or atrophy. It can be normal, especially in childhood (normal in 3 patients and in the Chinese proband; PMID 34354969).

**Electrophysiology.** EEG only if there are seizures (single case). No specific EMG or nerve conduction findings have been reported.

**Genetic testing:**
- Single-gene ABCB7 sequencing (GTR C1845028).
- Multigene panels: ABCB7 is on congenital sideroblastic anemia and hereditary ataxia panels, and on Genomics England PanelApp "Possible mitochondrial disorder – nuclear genes" ([PanelApp](https://panelapp.genomicsengland.co.uk/panels/539/gene/ABCB7/)).
- Exome or genome sequencing: the Chinese case was found by WES (PMID 34354969) and the Buryat family by WGS (PMID 26242992). WES/WGS is the practical first-line test for unexplained early ataxia.
- CMA: limited role. Karyotype, FISH and repeat-expansion testing: not indicated except to exclude differentials.
- mtDNA testing: was normal in the Chinese case, and helps exclude Pearson syndrome.
- Carrier testing of mothers and female relatives: targeted variant testing, supported by raised protoporphyrin and ring sideroblasts.

**Omics-based diagnostics.** None established.

**Diagnostic criteria.** There are no formal criteria. Diagnosis rests on:
- early-onset non-progressive ataxia in a male;
- mild hypochromic sideroblastic anemia with raised erythrocyte protoporphyrin;
- an X-linked pedigree;
- a hemizygous ABCB7 variant.

**Differential diagnosis:**

| Condition | Distinguishing features |
|---|---|
| ALAS2-XLSA | No ataxia; pyridoxine-responsive; iron overload (PMID 12382202) |
| Other congenital sideroblastic anemias (SLC25A38, GLRX5, PUS1, YARS2, TRNT1, mtDNA/Pearson) | Different inheritance and features (PMIDs 24003969, 19786205) |
| Friedreich ataxia (FXN) | Autosomal recessive; progressive; no sideroblastic anemia (PMID 11850112) |
| PCARP (FLVCR1) and other heme/Fe-S ataxias | See PMID 32466579 |
| Other X-linked congenital ataxias, e.g. ATP2B3, OPHN1 | Not retrieved in this session |
| Acquired MDS-RS (SF3B1) | Adult onset; no ataxia |

**Screening.** No newborn screening. Cascade carrier testing of female relatives is appropriate.

---

## 11. Outcome / Prognosis

- **Survival:** no formal data. Reported patients have reached at least age 50 (PMID 34354969), which suggests survival into adulthood with a mild hematological course. No disease-specific mortality data exist.
- **Morbidity:**
  - Lifelong motor disability: ataxic gait, dysarthria, delayed walking.
  - Variable developmental, cognitive and psychiatric comorbidity.
  - The anemia is mild and needs no transfusion.
  - Iron overload is reportedly not a feature.
- **Quality-of-life measures:** none published.
- **Complications:** possible later cerebellar atrophy and epilepsy (single case). A surveillance target such as iron overload is not established.
- **Recovery potential:** none. Motor milestones are delayed but eventually achieved; the Chinese proband walked at about 4 years.
- **Prognostic factors and biomarkers:** none established.

---

## 12. Treatment

NCIT IDs were not retrieved, so labels only are given here.

- **There is no disease-modifying therapy.**
- **Pyridoxine (vitamin B6):** tried in 2 patients with "no change in hematologic parameters" (PMID 34354969). Not effective in reported XLSA/A.
- **Transfusion:** not required in reported patients (PMID 34354969).
- **Iron chelation:** not indicated, because there is no systemic overload. Deferiprone redistributes mitochondrial iron in frataxin-deficient cells (PMID 18796625), and "iron redistribution" has been proposed for diseases of localized iron accumulation (PMID 20393584). Neither has been tested in XLSA/A, so this is speculative.
- **Antiseizure medication when needed:** levetiracetam plus topiramate controlled seizures in one case (PMID 34354969).
- **Supportive care and rehabilitation:** physical, occupational and speech therapy for ataxia and dysarthria, and developmental support. This is standard care for ataxia; no XLSA/A-specific outcome studies exist.
- **Gene, cell, RNA and targeted therapies:** none reported. HSCT is not reported.
- **Clinical trials:** a ClinicalTrials.gov API query ("ABCB7" OR "sideroblastic anemia with ataxia") returned **zero studies** ([ClinicalTrials.gov](https://clinicaltrials.gov/api/v2/studies?query.term=ABCB7+OR+%22sideroblastic+anemia+with+ataxia%22)).
- **Pharmacogenomics:** none.
- **Adjacent (acquired disease, not XLSA/A):** luspatercept and chelation are used in acquired sideroblastic anemia and MDS-RS (PMID 39644054). They are not relevant to XLSA/A management.

The retired GeneReviews chapter (PMID 20301496) likely holds management and surveillance guidance, but I could not retrieve its text.

---

## 13. Prevention

- **Primary prevention:** not applicable, beyond reproductive options.
- **Genetic counselling:**
  - X-linked recessive inheritance. Each son of a carrier mother has a 50% chance of being affected, and each daughter a 50% chance of being a carrier.
  - An affected male passes the variant to all daughters and to no sons ([MedlinePlus](https://medlineplus.gov/genetics/condition/x-linked-sideroblastic-anemia-and-ataxia/)).
  - Possible germline mosaicism should be considered when the variant appears de novo in a mother (PMID 34354969).
- **Prenatal testing and PGT:** feasible once the familial variant is known. No published experience was found.
- **Secondary prevention:** early recognition in boys with ataxia by checking CBC, smear and protoporphyrin, followed by ABCB7 testing.
- **Tertiary prevention:** rehabilitation; avoid unnecessary iron supplementation (inferred clinical reasoning).
- **Not applicable:** immunization, public-health or environmental interventions, and prophylaxis.

---

## 14. Other Species / Natural Disease

- **Naturally occurring disease:** none found in animals. OMIA was not queried.
- **Orthologs:**
  - Yeast *ATM1* (48.9% identical; PMID 9621516). Human ABC7 complements Δatm1 (PMID 10196363).
  - Mouse *Abcb7*.
  - Medaka *abcb7*.
  - *C. elegans* *abtm-1*.
  - *Drosophila* ABCB7 ortholog (PMIDs 42852025, 39638273).
  - Apicomplexan ATM1/ABCB7L, which is essential in *Toxoplasma* (PMIDs 39207139, 39348385).
  - NCBI Gene and Taxon IDs were not retrieved.
- **Evolution:** ABCB7 has an endosymbiotic origin from bacterial metal-glutathione transporters (PMID 33157103). The Fe-S export function is conserved from yeast to human.
- **Zoonotic potential:** not applicable.

---

## 15. Model Organisms

| Model | Type | Phenotype | Recapitulation and limitations | PMID |
|---|---|---|---|---|
| Mouse *Abcb7* floxed (exons 9–10), constitutive or tissue-specific deletion | Conditional knockout | Essential in extra-embryonic tissue; X-linked parent-of-origin lethality. Liver deletion impairs cytosolic Fe-S assembly and IRP1 control but is not lethal | Shows essentiality. A null does not model the hypomorphic human disease | 16467350 |
| Mouse *Abcb7*fl × Mx1-Cre | Inducible knockout | Transient siderocytes (peak day 5), then "uniform and rapidly fatal" pancytopenic marrow failure; median survival 16 days | **No marrow ringed sideroblasts.** Brain not deleted | 17192398 |
| Mouse E433K knock-in chimeras | Knock-in (human variant) | ZPP:heme rose with the mutant fraction; siderocytes; male infertility with testicular iron | **No ataxia.** Testicular phenotype not seen in humans | 17192398 |
| Mouse Mb1-cre / CD23-cre deletion | B-cell conditional | Pro-B-cell block, raised iron, replication-induced DNA damage, class-switch defect | Immune role, not reported in patients | 34762046 |
| Medaka *abcb7* mutant | Forward-genetic mutant | Larval fatty liver; abnormal erythrocyte iron metabolism | Erythroid iron phenotype partly modelled | 19046159 |
| *C. elegans* *abtm-1* mutant/RNAi | Loss-of-function | Arrested embryos, morphogenetic defects, ferric iron accumulation, oxidative stress, longer lifespan via DAF-16/SOD-3 | Oxidative-stress mechanism | 21464130 |
| Yeast Δ*atm1* | Complementation | Mitochondrial iron accumulation with cytosolic iron starvation (PMID 16120268); used to test human variants | Simple functional assay | 10196363, 11050011 |
| HeLa ABCB7 siRNA | Cellular | Iron-deficient phenotype, mitochondrial iron overload, low cytosolic aconitase | Mechanistic | 17192393 |
| Inducible ABCB7 knockdown, including erythroid cells | Cellular | Loss of mitochondrial Fe-S proteins, then cytosolic defects; hemoglobinization defect; ALAS2 repression; FECH instability | Mechanistic | 30765471 |
| MEL cells (antisense ABC7) | Cellular | Less heme; ABC7–FECH interaction | Mechanistic | 12480705 |
| Rat ABCB7 overexpression | Gain-of-expression | Did not prevent doxorubicin cardiac injury; partly preserved diaphragm function | Not a disease model | 42441500 |

**Overall limitation.** No model reproduces both human ring sideroblasts and cerebellar ataxia from a patient allele. No iPSC-derived neuronal or erythroid XLSA/A model was found. Model databases (MGI, IMPC, ZFIN, WormBase) were not directly queried.

---

## Key references (PMIDs)

**Clinical and genetic:**
- 4045952 (Pagon 1985)
- 1671320 (Raskind 1991)
- 9621516 (Shimada 1998)
- 10196363 (Allikmets 1999)
- 11050011 (Bekri 2000)
- 11843825 (Maguire 2001)
- 22398176 (D'Hooghe 2012)
- 26242992 (Protasova 2016)
- 34354969 (Xiong 2021)
- 20301496 (GeneReviews, retired)

**Mechanistic:**
- 16467350 and 17192398 (Pondarré 2006, 2007)
- 17192393 (Cavadini 2007)
- 12480705 (Taketani 2003)
- 30765471 (Maio 2019)
- 33157103 (Pearson 2021)
- 34762046 (Lehrke 2021)
- 35041979 (Yan 2022)
- 38743629 (Braymer 2024)
- 42103889 (Ju 2026)
- 21464130 (González-Cabo 2011)
- 19046159 (Miyake 2008)

**Reviews:** 11850112, 12382202, 19786205, 24003969, 32466579, 38929857.

**Database sources:** [UniProt O75027](https://rest.uniprot.org/uniprotkb/O75027.txt) · [Monarch MONDO:0010524](https://api.monarchinitiative.org/v3/api/entity/MONDO:0010524) · [HPO OMIM:301310](https://ontology.jax.org/api/network/annotation/OMIM:301310) · [MedlinePlus](https://medlineplus.gov/genetics/condition/x-linked-sideroblastic-anemia-and-ataxia/) · [Xiong 2021 full text](https://www.frontiersin.org/journals/pediatrics/articles/10.3389/fped.2021.692459/full) · [Pondarré 2007, PMC1852240](https://pmc.ncbi.nlm.nih.gov/articles/PMC1852240) · [PhenoDis/Orphanet mirror](https://iegext02.helmholtz-munich.de/phenodis/disease/show/3705) · [PanelApp ABCB7](https://panelapp.genomicsengland.co.uk/panels/539/gene/ABCB7/) · [ClinicalTrials.gov query](https://clinicaltrials.gov/api/v2/studies?query.term=ABCB7+OR+%22sideroblastic+anemia+with+ataxia%22) · ClinVar VCV000011574, VCV000011575, VCV000011576, VCV000126455, VCV000208533, VCV003248639, VCV003235083

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 33 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| Quoted claims checked | 17 |
| Quoted claims found in source | 11 |
| Quoted claims **not** found in source | 6 |
| Quoted claims with nothing to check against | 1 |
| References weighed for topical relevance | 32 |
| On topic | 26 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `PMID:38743629` (1 mention) - Identifier did not resolve to a record

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:10196363` *(abstract only)*: "a recessive disorder with infantile to early-childhood onset of nonprogressive cerebellar ataxia and mild anemia with hypochromia and microcytosis"
  - closest text in source: "X-linked sideroblastic anemia and ataxia (XLSA/A) is a recessive disorder characterized by an infantile to early childhood onset of non-progressive cerebellar ataxia and mild anemia with hypochromia and microcytosis"
- `PMID:34354969` *(abstract only)*: "Cerebellum atrophy probably occurs in the later stages of the disease"
  - closest text in source: "X-linked sideroblastic anemia with ataxia (XLSA/A) is a rare X-liked inherited disease, which was linked to the ABCB7 gene mutations"
- `PMID:34354969` *(abstract only)*: "The proband's grandmother was very likely to harbor germline mosaicism for the ABCB7 gene variant"
  - closest text in source: "X-linked sideroblastic anemia with ataxia (XLSA/A) is a rare X-liked inherited disease, which was linked to the ABCB7 gene mutations"
- `PMID:33157103` *(abstract only)*: "E433 is important for cluster transport"
  - closest text in source: "In addition, a functional comparison of native human protein, versus a disease-causing mutant, demonstrates a key role for residue E433 in promoting cluster transport"
- `PMID:17192393` *(abstract only)*: "iron-deficient phenotype with mitochondrial iron overload"
  - closest text in source: "The phenotype of the ABCB7-deficient cells was characterized by a strong reduction in proliferation rate that was not rescued by iron supplementation, by evident signs of iron deficiency, and by a large approximately 6-fold increase of iron accumulation in the mitochondria that was poorly available to mitochondrial ferritin"
- `PMID:34354969` *(abstract only)*: "no change in hematologic parameters"
  - Text part not found as substring: 'no change in hematologic parameters' (note: only abstract available for PMID:34354969, full text may contain this excerpt)

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `PMID:38743629`: "the most critical GSH requirement was assigned to Atm1-dependent export"
  - Reference did not resolve, so the quote could not be checked

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 76 |
| Resolved | 72 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 4 |
| Terms whose name was checked | 40 |
| Terms named correctly | 38 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0010524` (8 mentions) - the report calls it "MONDO"; MONDO calls it **X-linked sideroblastic anemia with ataxia**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0005743` (2 mentions) - the report calls it "Subcellular level:** mitochondrial inner membrane"; GO calls it **mitochondrial inner membrane**

### Terms the ontology service could not be reached for

1 term(s) could not be checked because the ontology service was unreachable (a timeout, 5xx, 408 or 429), not because anything looks wrong with them. Re-run when the service is reachable -- the label cache resumes, so only the unresolved terms are retried:

- `HP:0002463` (1 mention)

### Terms whose obsolescence could not be checked

1 term(s) resolved, so they exist, but the ontology service was unreachable for the deprecation check -- treat their obsolescence as unknown rather than clean, and re-run to confirm:

- `HP:0001263` (1 mention)

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `ORPHA`.