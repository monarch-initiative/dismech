---
provider: claude_code
model: claude-haiku-5-5, claude-opus-4-8, claude-opus-5-5
cached: false
start_time: '2026-11-26T15:45:58.006914'
end_time: '2026-11-26T15:49:51.936767'
duration_seconds: 233.93
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Miliary Tuberculosis
  mondo_id: MONDO:0005848
  category: Infectious Disease
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: acute miliary tuberculosis; disseminated tuberculosis; generalised tuberculosis;
    generalized tuberculosis
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
  web_search_requests: 20
  num_turns: 25
  total_cost_usd: 1.4856069000000005
  session_id: 2627a4d9-7b0f-48c8-a13b-61418d35235f
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  tool_calls: 23
  retrieval_calls: 20
  assistant_text_blocks: 3
citation_count: 44
reference_validation:
  total_references: 24
  verified: 24
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 4
  quotes_valid: 1
  quotes_unsupported: 3
  unsupported_quote_references:
  - PMC:PMC3544391
  - PMID:22771605
  - PMC:PMC201048
  relevance_assessed: 24
  on_topic: 16
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 61
  verified: 24
  not_found: 0
  obsolete: 0
  unverifiable: 37
  confabulation_rate: 0.0
  labels_checked: 7
  labels_matching: 3
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: HP:0034287
    reported_labels:
    - suggested term
    ontology_label: Afibrinogenemia
  - term_id: UBERON:0002048
    reported_labels:
    - Primary organ:** lung
    ontology_label: lung
  labels_variant: 2
  service_unreachable: 34
  obsolescence_unchecked: 8
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Miliary Tuberculosis
- **MONDO ID:** MONDO:0005848 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** acute miliary tuberculosis; disseminated tuberculosis; generalised tuberculosis; generalized tuberculosis
- **Category:** Infectious Disease

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Miliary Tuberculosis** covering all of the
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

Bash is unavailable; I'll use WebSearch.

I have the core sources I need and am writing the report now.

# Miliary Tuberculosis (MONDO:0005848): Disease Characteristics Report

**How this was researched:** Miliary tuberculosis is an infectious disease caused by *Mycobacterium tuberculosis* complex bacteria. No human causal gene is recorded for it, and none exists in the Mendelian sense. Host genes appear in this report only as susceptibility factors.

The PubMed E-utilities shell access was denied in this session, so all sources were found by web search. A PMID is given only where a retrieved record showed it. Otherwise the citation is a PMC or other URL. Abstract quotes are reproduced only where search results returned the text. Several template fields have no data for an infectious disease, and those are marked "Not applicable".

---

## 1. Disease Information

**Overview.**
- MeSH defines miliary tuberculosis as "an acute form of tuberculosis in which minute tubercles are formed in a number of organs of the body due to dissemination of the bacilli through the blood stream" ([MeSH D014391](https://meshb.nlm.nih.gov/record/ui?ui=D014391)).
- It results from a "massive lymphohematogenous spread of *M. tuberculosis*" ([PMC3544391](https://pmc.ncbi.nlm.nih.gov/articles/PMC3544391)).
- The name comes from the 1–5 mm lesions, which look like millet seeds ([Wikipedia](https://en.wikipedia.com/wiki/Miliary_TB)).
- It is classified as both pulmonary and extrapulmonary TB ([StatPearls NBK562300](https://ncbi.nlm.nih.gov/books/NBK562300)).
- Untreated, it is almost always fatal. "Untreated miliary TB [has] a fatal outcome within one year" (Sharma & Mohan, Indian J Med Res 2012, [PMID 22771605](https://pubmed.ncbi.nlm.nih.gov/22771605/)). See also [PMID 28281441](https://pubmed.ncbi.nlm.nih.gov/28281441/).

**Identifiers**

| System | ID |
|---|---|
| MONDO | MONDO:0005848. Parent is extrapulmonary tuberculosis, MONDO:0000368; no child terms ([SAIL concept library](https://conceptlibrary.saildatabank.com/api/v1/ontology/node/MONDO:0005848/)) |
| DOID | DOID:9861 ([MGI](https://www.informatics.jax.org/disease/DOID:9861)) |
| UMLS | C0041321 |
| SNOMED CT | 47604008 |
| ICD-10 | A19. Subcodes: A19.0 single specified site, A19.1 multiple sites, A19.2 unspecified, A19.8 other, A19.9 unspecified ([gesund.bund.de](https://gesund.bund.de/en/icd-code-suche/a19)) |
| MeSH | D014391 "Tuberculosis, Miliary" |
| ICD-11 | Not verified (1B12.x was not confirmed by search) |
| OMIM / Orphanet | None. This is an infectious disease. |

**Synonyms:** acute miliary tuberculosis; disseminated tuberculosis; generalized (generalised) tuberculosis. In clinical usage, "disseminated TB" is broader than "miliary" and includes non-miliary multi-site disease ([PMID 30819659](https://pubmed.ncbi.nlm.nih.gov/30819659/)).

**Data provenance:** The information comes from aggregated disease-level resources (ontologies, reviews and surveillance) and from retrospective hospital and administrative cohorts, such as the Japanese DPC database ([PMID 38636244](https://pesquisa.bvsalud.org/portal/resource/e/mdl-38636244)).

**Key reviews**
- Sharma SK, Mohan A, Sharma A, Mitra DK. *Lancet Infect Dis* 2005;5:415–30, [PMID 15978528](https://read.qxmd.com/read/15978528/miliary-tuberculosis-new-insights-into-an-old-disease)
- Sharma & Mohan. *J Clin Tuberc Other Mycobact Dis* 2016, [PMID 31723681](https://pubmed.ncbi.nlm.nih.gov/31723681/)
- Sharma & Mohan. *Microbiol Spectr* 2017, [PMID 28281441](https://pubmed.ncbi.nlm.nih.gov/28281441/)

## 2. Etiology

**Cause.** The disease is caused by infection with *M. tuberculosis* complex bacteria (NCBITaxon:1773). Zoonotic *M. bovis* (NCBITaxon:1765) can also cause it. Disease follows hematogenous dissemination, either during primary infection or on reactivation of a latent focus ([PMC3544391](https://pmc.ncbi.nlm.nih.gov/articles/PMC3544391)).

**Environmental and host risk factors (human clinical evidence)**
- A Portuguese cohort of disseminated TB ([PMID 30819659](https://pubmed.ncbi.nlm.nih.gov/30819659/)) found these independent predictors:
  - pharmacological immunosuppression: OR 5.6 (95% CI 2.8–11.3)
  - HIV infection: OR 5.1 (3.1–8.3)
  - chronic liver failure or cirrhosis: OR 2.3 (1.4–4.1)
  - longer symptom duration: OR 2.3 (1.4–3.8)
- **TNF-α antagonists.** Keane et al. (*NEJM* 2001;345:1098–1104; PMID 11596589 per [record](https://searchworks.jioinstitute.edu.in/articles/cmedm__11596589)) analysed 70 TB cases reported after infliximab.
  - 40 of the 70 cases were extrapulmonary, and 17 of those were disseminated.
  - Median onset was 12 weeks after starting treatment, and 48 patients developed TB after three or fewer infusions.
  - The estimated incidence in rheumatoid arthritis patients on infliximab was over 24 per 100,000, against about 6 per 100,000 without it ([Science News](https://www.sciencenews.org/article/anti-inflammatory-drug-may-unleash-tb)).
- **Corticosteroids.** Inappropriate glucocorticoid use has been linked to unmasking of cryptic miliary TB and to HLH ([J Infect Dev Ctries, PMID 38064397](https://jidc.org/index.php/journal/article/view/38064397)).
- **Age.** Infants and young children are at higher risk ([BMC Pediatr 2023](https://doi.org/10.1186/s12887-023-04427-x)). Older adults are also at higher risk ([PMC3544391](https://pmc.ncbi.nlm.nih.gov/articles/PMC3544391)).
- **Smoking** predicted adverse outcome in a West China cohort of 313 patients ([Ann Med 2024](https://doaj.org/article/ba7d65b8e2e54ce1baaa9936dbe00ffc)).
- Diabetes, malnutrition, renal failure and malignancy are cited as classical predisposing conditions in the reviews above. This is review-level evidence, and no specific primary estimates were retrieved for them.

**Genetic risk factors (host susceptibility, not causal genes)**
- Mendelian susceptibility to mycobacterial disease (MSMD) is caused by inborn errors of IFN-γ immunity and presents with disseminated BCG or environmental mycobacterial disease ([PMID 40656276](https://pubmed.ncbi.nlm.nih.gov/40656276/)).
  - *IL12RB1* is the most common cause. In one cohort it accounted for 80% of patients, with *IFNGR1* at 12% ([PMC7275902](https://pmc.ncbi.nlm.nih.gov/articles/PMC7275902)).
- **TYK2 P1104A (rs34536443) homozygosity**
  - It "selectively disrupts the induction of IFN-γ by IL-23 and is a common monogenic etiology of tuberculosis" (Boisson-Dupuis et al., *Sci Immunol* 2018, [PMID 30578352](https://research.pasteur.fr/en/b/ZUw)).
  - In UK Biobank, homozygotes made up 6/620 (1%) of TB patients against 0.2% of controls (OR 5.0). The variant therefore underlies about 1% of TB in people of European ancestry (Kerner et al., *PNAS* 2019, PMID 31068474, [UK Biobank page](https://www.ukbiobank.ac.uk/publications/homozygosity-for-tyk2-p1104a-underlies-tuberculosis-in-about-1-of-patients-in-a-cohort-of-european-ancestry)).
  - Penetrance is low for MSMD (probably under 1%) but high for TB in endemic areas (probably over 80%).
- No GWAS locus specific to miliary TB was retrieved.

**Protective factors**
- **BCG vaccination in infancy.**
  - Protection against meningeal and miliary TB is high in infants (RR 0.1, 95% CI 0.01–0.77) and in stringently tuberculin-tested children (RR 0.08, 0.03–0.25) (Mangtani et al., *Clin Infect Dis* 2014;58:470–80, [PMID 24336911](https://researchonline.lshtm.ac.uk/1440348)).
  - Modelling estimated that infant BCG given in 2002 would prevent about 11,486 miliary TB cases (7,304–16,280) in the first five years of life (Trunz, Fine & Dye, *Lancet* 2006; PMID not verified).
- **Genetic protective variants:** none retrieved.

**Gene–environment interaction**
- Host IFN-γ/IL-12/IL-23 axis defects combined with exposure to mycobacteria lead to disseminated disease (MSMD, TYK2 P1104A).
- Iatrogenic blockade of the same axis, for example by anti-TNF drugs, produces a similar phenocopy.

## 3. Phenotypes

The presentation is "protean and nonspecific", and atypical presentations delay diagnosis ([PMID 31723681](https://pubmed.ncbi.nlm.nih.gov/31723681/)). Retrieved frequency data are limited.

| Phenotype | HPO | Type / notes |
|---|---|---|
| Fever (often prolonged, of unknown origin) | HP:0001945 | Symptom; very common (review-level) |
| Weight loss | HP:0001824 | Symptom |
| Cough | HP:0012735 | Symptom |
| Dyspnea | HP:0002094 | Symptom |
| Anorexia / fatigue | HP:0002039 / HP:0012378 | Symptom |
| Hepatomegaly, splenomegaly | HP:0002240, HP:0001744 | Sign; among the most common signs in children ([BMC Pediatr 2023](https://doi.org/10.1186/s12887-023-04427-x)) |
| Lymphadenopathy | HP:0002716 | Sign; common in children |
| Seizures, diarrhea (children) | HP:0001250, HP:0002014 | Pediatric presentation |
| Choroid tubercles | HP:0000554 (uveitis; closest available term) | Sign; described as pathognomonic ([PMID 22771605](https://pubmed.ncbi.nlm.nih.gov/22771605/)) |
| Diffuse miliary pulmonary nodules (1–5 mm, random distribution) | HP:0033104 (pulmonary nodules; suggested term) | Imaging; seen in 24/25 patients on HRCT ([PMID 9530383](https://pubmed.ncbi.nlm.nih.gov/9530383/)) |
| Coexisting tuberculous meningitis | HP:0001287 (meningitis) | About 25% of children and 23% of adults in a Turkish series ([dergipark](https://dergipark.org.tr/en/download/article-file/61746)) |
| ARDS / respiratory failure | HP:0033677 (ARDS), HP:0002878 | Reported in about 7–18% of cases ([PMC9937678](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9937678/)) |
| Leukocytosis, lymphopenia, raised ALT | HP:0001974, HP:0001888, HP:0031964 | Laboratory findings; prognostic in the West China cohort |
| Hemophagocytic lymphohistiocytosis | HP:0034287 (suggested term) | Rare severe complication ([PMC8787627](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8787627/)) |
| Adrenal insufficiency / shock | HP:0000846 | Should be suspected in refractory shock ([PMC10507688](https://pmc.ncbi.nlm.nih.gov/articles/PMC10507688)) |

- **Onset and course:** subacute over weeks; acute and fulminant forms also occur, such as ARDS presentations.
- **Severity:** variable, ranging up to life-threatening.
- **Quality of life:** no EQ-5D or SF-36 data specific to miliary TB were found.

## 4. Genetic / Molecular Information

- **Causal genes:** not applicable, because this is an infection.
- **Host susceptibility genes:**

| Gene | Variant | Effect | Inheritance |
|---|---|---|---|
| *IL12RB1* (HGNC:5971) | Biallelic loss-of-function variants | Main MSMD gene | AR |
| *IFNGR1* (HGNC:5439) | Loss-of-function variants | MSMD | AR, or AD dominant-negative |
| *TYK2* (HGNC:12440) | P1104A missense, catalytically inactive | Common monogenic TB risk | AR |

  The table summarises the MSMD reviews cited in section 2 ([PMID 40656276](https://pubmed.ncbi.nlm.nih.gov/40656276/), [PMC6469360](https://pmc.ncbi.nlm.nih.gov/articles/PMC6469360)). All variants are germline. The HGNC IDs come from prior knowledge and were not retrieved in this session, so they need verifying.
- **Pathogen genes:**
  - The ESX-1 (RD1) secretion system and ESAT-6 (*esxA*) drive macrophage recruitment and spread ([PMC524251](https://pmc.ncbi.nlm.nih.gov/articles/PMC524251)).
  - Variants of the ESX-5 effector EsxM increase macrophage egress from granulomas and dissemination ([PNAS 2022, HAL](https://hal-pasteur.archives-ouvertes.fr/pasteur-03648366/file/pnas.2122161119.pdf)).
- **Epigenetic findings and chromosomal abnormalities:** none specific to miliary TB were found.

## 5. Environmental Information

- **Infectious agents:** *M. tuberculosis* (NCBITaxon:1773) and *M. bovis* (NCBITaxon:1765). *M. caprae*, *M. orygis*, *M. pinnipedii* and *M. microti* can also infect humans ([CFSPH](https://www.cfsph.iastate.edu/Factsheets/pdfs/bovine_tuberculosis.pdf)). BCG (*M. bovis* BCG) causes disseminated disease in people with MSMD.
- **Iatrogenic and other exposures:** TNF inhibitors and other immunosuppressants (NCIT "TNF inhibitor"), and corticosteroids. The relevant ChEBI terms are infliximab, CHEBI:… (not retrieved), and glucocorticoid, CHEBI:24261.
- **Lifestyle:** smoking was associated with adverse outcome ([Ann Med 2024](https://doaj.org/article/ba7d65b8e2e54ce1baaa9936dbe00ffc)).

## 6. Mechanism / Pathophysiology

**Causal chain.** Steps 1–3 are human-clinical; step 4 is from model organisms and is inferred for humans; steps 5–7 are human-clinical.

1. Inhaled *M. tuberculosis* infects alveolar macrophages (CL:0000583), which **leads to** intracellular replication and an early granuloma.
2. ESX-1/ESAT-6 phagosomal damage **results in** recruitment of new macrophages to the granuloma and their infection. This was shown in zebrafish with *M. marinum* and is inferred for human *M. tuberculosis

Continuing the report from section 6.

## 6. Mechanism / Pathophysiology (continued)

**Causal chain** (steps 1–3 human-clinical; step 4 from model organisms, inferred for humans; steps 5–7 human-clinical):

1. Inhaled bacilli infect alveolar macrophages (CL:0000583) → intracellular replication and early granuloma formation.
2. The ESX-1 secretion system and ESAT-6 damage the phagosome → recruitment and infection of additional macrophages (Volkman et al., [PMC524251](https://pmc.ncbi.nlm.nih.gov/articles/PMC524251); Davis & Ramakrishnan).
3. Infected macrophages egress from the primary granuloma → seeding of secondary granulomas, which the zebrafish work frames as the granuloma promoting early dissemination.
4. In the host, inadequate IFN-γ/IL-12/IL-23 signalling → failure to activate macrophages and control bacilli. IFN-γ-knockout mice show "disseminated tuberculosis" with widespread necrosis and very high bacterial loads (Cooper et al.; Flynn et al., *J Exp Med* 1993;178:2243–47 and 2249–54, [rupress](https://rupress.org/jem/article/178/6/2249/25121/An-essential-role-for-interferon-gamma-in)).
5. Bacilli enter the bloodstream (lymphohematogenous spread) → simultaneous seeding of many organs ([PMC3544391](https://pmc.ncbi.nlm.nih.gov/articles/PMC3544391)).
6. Innumerable small granulomas form across lung, liver, spleen, bone marrow, meninges and other organs → organ dysfunction.
7. In severe cases, a systemic inflammatory response → ARDS, septic shock, HLH or adrenal insufficiency ([PMC9937678](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9937678/), [PMC8787627](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8787627/)).

**Checklist coverage.**
- *Molecular pathways / immune involvement:* the IL-12/IL-23–IFN-γ–STAT1 axis is central (GO:0032609 interferon-gamma production; GO:0042832 defense response to protozoan is not apt — use GO:0051607 defense response to virus as a related example only). Relevant GO terms: GO:0006952 defense response, GO:0002286 T cell activation involved in immune response.
- *Cellular processes:* granuloma formation (GO:0002432), macrophage activation (GO:0042116), apoptosis of infected macrophages (GO:0006915).
- *Protein dysfunction:* loss of TYK2 kinase activity; loss-of-function of IL12RB1/IFNGR1 receptors.
- *Tissue damage:* caseating necrosis within granulomas; the IFN-γ-KO model showed excess necrosis.
- *Molecular profiling (transcriptomics, proteomics, metabolomics, single-cell, spatial):* no miliary-TB-specific omics datasets were retrieved in this session; stated as not available here.

**Cell types (CL):** alveolar macrophage CL:0000583, macrophage CL:0000235, epithelioid cell, multinucleated giant cell (Langhans), CD4+ T cell CL:0000492.

## 7. Anatomical Structures Affected

- **Primary organ:** lung (UBERON:0002048), with diffuse bilateral miliary nodules.
- **Secondary/multi-organ:** liver (UBERON:0002107), spleen (UBERON:0002106), bone marrow (UBERON:0002371), lymph nodes (UBERON:0000029), meninges/brain (UBERON:0002360 / UBERON:0000955), kidney (UBERON:0002113), adrenal gland (UBERON:0002369), choroid of the eye (UBERON:0001776), intestine (UBERON:0000160). Multi-organ seeding is the defining feature ([PMC3544391](https://pmc.ncbi.nlm.nih.gov/articles/PMC3544391)); bovine disease shows the same organ distribution ([Merck Vet Manual](https://www.merckvetmanual.com/generalized-conditions/tuberculosis-and-other-mycobacterial-infections/overview-of-tuberculosis-and-other-mycobacterial-infections)).
- **Body systems:** respiratory, reticuloendothelial/hematopoietic, central nervous, hepatobiliary, endocrine.
- **Tissue/cell level:** granulomas in parenchyma; macrophages and T lymphocytes (CL terms above).
- **Subcellular (GO cellular component):** phagosome GO:0005768/GO:0045335 (where bacilli reside); the ESX-1 system damages the phagosomal membrane.
- **Localization:** bilateral, diffuse, random distribution on HRCT ([PMID 9530383](https://pubmed.ncbi.nlm.nih.gov/9530383/)).

## 8. Temporal Development

- **Onset:** any age; higher risk in infants/young children and older or immunosuppressed adults. Pattern is usually subacute (weeks), occasionally acute/fulminant.
- **Progression:** untreated disease is progressive and fatal within about one year ([PMID 22771605](https://pubmed.ncbi.nlm.nih.gov/22771605/)).
- **Course:** continuous rather than relapsing-remitting. "Cryptic" miliary TB is an insidious form in older adults.
- **Critical window:** early anti-TB therapy is life-saving; delay worsens outcome ([PMID 28281441](https://pubmed.ncbi.nlm.nih.gov/28281441/)).
- **Remission:** treatment-induced; no spontaneous remission.

## 9. Inheritance and Population

- **Share of TB cases:** about 1–2% of all TB and up to ~20% of extrapulmonary TB ([StatPearls](https://www.statpearls.com/point-of-care/25159)). In a 2010 US analysis, miliary disease was 299/11,182 incident cases (~2.7%); extrapulmonary TB was ~22% of cases ([typeset US EPTB epidemiology](https://typeset.io/pdf/epidemiology-of-extrapulmonary-tuberculosis-in-the-united-1bobmyoy4t.pdf)).
- **CDC 2024 site-of-disease split (all TB):** ~71% pulmonary only, 17% extrapulmonary only, 12% both; commonest extrapulmonary sites lymphatic 28% and pleural 24% ([CDC 2024](https://www.cdc.gov/tb-surveillance-report-2024/data/site-of-disease.html)).
- **Inheritance:** not applicable (infectious). Host susceptibility is AR/AD for the MSMD genes and AR for TYK2 P1104A homozygosity (section 2).
- **Geography:** burden tracks global TB — highest in South/Southeast Asia and sub-Saharan Africa; HIV co-infection raises the disseminated fraction.
- **Sex and age:** no reliable miliary-specific sex ratio retrieved. Bimodal age risk (young children; older/immunosuppressed adults).

## 10. Diagnostics

- **Imaging.** HRCT is more sensitive than chest radiography and shows randomly distributed 1–5 mm nodules ([PMID 9530383](https://pubmed.ncbi.nlm.nih.gov/9530383/)); the radiograph can be normal early. About 10% of cases may be missed on initial CT ([PMC3473551](https://pmc.ncbi.nlm.nih.gov/articles/PMC3473551)).
- **Microbiology.** In miliary TB, AFB smear sensitivity is ~20–40% and PCR ~60–80% ([StatPearls NBK562300](https://ncbi.nlm.nih.gov/books/NBK562300)). Culture of sputum, blood, bone marrow, liver or other tissue remains important. (Specific Xpert MTB/RIF and bone-marrow/liver-biopsy yield figures were not retrieved in this session.)
- **Fundoscopy** for choroid tubercles, described as pathognomonic ([PMID 22771605](https://pubmed.ncbi.nlm.nih.gov/22771605/)).
- **Histopathology:** caseating granulomas with AFB on tissue biopsy (SNOMED/LOINC terms applicable).
- **Supporting labs:** leukocytosis, lymphopenia, raised ALT, pancytopenia (with bone-marrow involvement or HLH).
- **Genetic testing** is relevant only for suspected host immunodeficiency (MSMD gene panels via GTR), not for routine diagnosis.
- **Differential diagnosis:** disseminated fungal infection, sarcoidosis, metastatic malignancy, pneumoconiosis, hypersensitivity pneumonitis, other causes of miliary nodules.

## 11. Outcome / Prognosis

- **Mortality.** In the Japanese DPC cohort, 2,817 patients had 637 (22.6%) in-hospital deaths ([PMID 38636244](https://pesquisa.bvsalud.org/portal/resource/e/mdl-38636244)). A UK cohort of 52 reported 1-year mortality of 2%, attributed to timely critical care, anti-TB therapy and possibly corticosteroids ([PMC6850233](https://pmc.ncbi.nlm.nih.gov/articles/PMC6850233)).
- **Prognostic factors.** In a West China cohort of 313 (2010–2022), independent predictors of adverse outcome were current smoking, leukocytosis, elevated ALT, and lymphopenia combined with bone-marrow TB or TB lymphadenitis ([Ann Med 2024](https://doaj.org/article/ba7d65b8e2e54ce1baaa9936dbe00ffc)). Pediatric mortality is ~15–20% ([BMC Pediatr 2023](https://doi.org/10.1186/s12887-023-04427-x)).
- **Complications:** ARDS (~7–18%, high mortality), HLH, septic shock, adrenal insufficiency, drug-induced liver injury, coexisting TB meningitis.
- **Recovery:** with timely treatment, most immunocompetent patients recover; without treatment, almost uniformly fatal within a year.

## 12. Treatment

- **First-line anti-TB therapy (NCIT: Antitubercular Agent).** Standard regimen: isoniazid (CHEBI:6030), rifampicin (CHEBI:28077), pyrazinamide (CHEBI:45285) and ethambutol (CHEBI:4877) for a 2-month intensive phase, then isoniazid + rifampicin continuation. Total duration ~6 months for drug-susceptible miliary TB, extended to ~9–12 months when TB meningitis coexists ([Nahid et al., ATS/CDC/IDSA 2016, Clin Infect Dis 63(7):e147–95](https://academic.oup.com/cid/article/63/5/e61/2196792); regimen table [PMC6850233 tbl0004](https://pmc.ncbi.nlm.nih.gov/articles/PMC6850233/table/tbl0004)). HIV patients not on ART may need an extended continuation phase.
- **Corticosteroids (NCIT: Corticosteroid).** Adjunctive use is standard for coexisting TB meningitis/pericarditis and used for life-threatening disease (ARDS, adrenal insufficiency), but routine use in miliary TB without those indications is debated ([PMC9937678](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9937678/)).
- **Supportive/ICU care** for ARDS, shock and organ failure. For MSMD-related disease, adjunctive IFN-γ and treating the underlying immune defect are relevant ([PMID 40656276](https://pubmed.ncbi.nlm.nih.gov/40656276/)).
- **Monitoring:** hepatotoxicity and drug–drug interactions, especially rifampicin with antiretrovirals ([PMID 31723681](https://pubmed.ncbi.nlm.nih.gov/31723681/)).
- Randomized trial data specific to miliary TB regimen/duration are sparse ([PMID 31723681](https://pubmed.ncbi.nlm.nih.gov/31723681/)).

## 13. Prevention

- **Primary:** infant BCG vaccination gives high protection against miliary and meningeal TB in young children (Mangtani 2014, [PMID 24336911](https://researchonline.lshtm.ac.uk/1440348)); it is ineffective in adolescents/adults ([JAMA Pediatr IPD meta-analysis](https://jamanetwork.com/journals/jamapediatrics/fullarticle/2716800)). General TB control (case finding, treating infectious cases) reduces transmission.
- **Secondary:** screening and treating latent TB infection before immunosuppression. "Before prescribing [infliximab], physicians should screen patients for latent tuberculosis" (Keane 2001, [record](https://searchworks.jioinstitute.edu.in/articles/cmedm__11596589)).
- **Tertiary:** early treatment and monitoring to prevent ARDS, DILI and death.
- **Bovine/zoonotic:** milk pasteurisation and cattle control programs reduce *M. bovis* spillover ([CFSPH](https://www.cfsph.iastate.edu/Factsheets/pdfs/bovine_tuberculosis.pdf)).

## 14. Other Species / Natural Disease

- **Cattle (NCBITaxon:9913):** *M. bovis* causes bovine TB; "the acute generalized form, known as miliary tuberculosis, is often rapidly fatal", with lesions in lungs, lymph nodes, intestine and kidney ([Merck Vet Manual](https://www.merckvetmanual.com/generalized-conditions/tuberculosis-and-other-mycobacterial-infections/overview-of-tuberculosis-and-other-mycobacterial-infections); [CFSPH](https://www.cfsph.iastate.edu/Factsheets/pdfs/bovine_tuberculosis.pdf)).
- **Zoonosis:** *M. bovis*, *M. caprae*, *M. orygis*, *M. pinnipedii* and *M. microti* can infect humans ([WOAH](https://woah.org/?p=253)).
- **Nonhuman primates:** low-dose *M. tuberculosis* in cynomolgus macaques reproduces the human spectrum; TNF blockade before infection produced "fulminant and disseminated disease by 8 weeks" ([PMC201048](https://pmc.ncbi.nlm.nih.gov/articles/PMC201048)).
- **Comparative:** disseminated disease across species consistently follows failure of macrophage/T-cell containment.

## 15. Model Organisms

- **Mouse (NCBITaxon:10090).** IFN-γ gene-disrupted mice develop disseminated TB with widespread necrosis and very high bacillary loads, establishing IFN-γ as essential for containment (Cooper, Flynn et al. 1993, [rupress](https://rupress.org/jem/article/178/6/2249/25121/An-essential-role-for-interferon-gamma-in)). Resource: MGI.
- **Zebrafish (NCBITaxon:7955) / *M. marinum*.** Intravital imaging showed ESX-1/RD1-driven macrophage recruitment, apoptosis and egress seeding secondary granulomas — a model of early dissemination (Davis & Ramakrishnan; Volkman et al., [PMC524251](https://pmc.ncbi.nlm.nih.gov/articles/PMC524251)). Resource: ZFIN.
- **Nonhuman primate** models (section 14) best recapitulate human granuloma pathology and disseminated disease under TNF blockade.
- **Recapitulation / limitations:** mouse and zebrafish capture dissemination mechanisms and host-factor dependence but differ from human caseating granuloma architecture; macaques recapitulate pathology best but are resource-intensive. *M. marinum* is a surrogate for *M. tuberculosis*.

---

### Notes on gaps and reliability
- Bash/PubMed E-utilities were blocked this session; PMIDs are given only where a retrieved page showed them. Several (Trunz/Fine/Dye 2006; Keane 2001 PMID 11596589; HGNC IDs) rest on secondary records and should be verified against PubMed/HGNC directly.
- ICD-11 code, miliary-TB-specific omics data, EQ-5D/SF-36 quality-of-life measures, and HIV-infant-specific phenotype frequencies were not located and are marked not available.
- "Disseminated TB" cohort estimates (e.g. Portugal) are broader than strictly miliary disease and are labelled as such.

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 24 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 4 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 3 |
| References weighed for topical relevance | 24 |
| On topic | 16 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

2 of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMC:PMC3544391` *(abstract only)*: "massive lymphohematogenous spread of *M. tuberculosis*"
  - closest text in source: "Miliary TB is a potentially fatal form of TB that results from massive lymphohematogenous dissemination of Mycobacterium tuberculosis bacilli"
- `PMID:22771605`: "Untreated miliary TB [has] a fatal outcome within one year"
  - closest text in source: "Although several prognostic markers have been described which predict mortality, yet untreated miliary TB has a fatal outcome within one year"
- `PMC:PMC201048` *(abstract only)*: "fulminant and disseminated disease by 8 weeks"
  - closest text in source: "Active-chronic infection, observed in 50 to 60% of monkeys, was characterized by clear signs of infection or disease on serial thoracic radiographs and in other tests and was typified by eventual progression to advanced disease"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 61 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 37 |
| Terms whose name was checked | 7 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0034287` (1 mention) - the report calls it "suggested term"; HP calls it **Afibrinogenemia**
- `UBERON:0002048` (1 mention) - the report calls it "Primary organ:** lung"; UBERON calls it **lung**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `NCBITaxon:1765` (2 mentions) - the report calls it "M. bovis"; NCBITaxon calls it **Mycobacterium tuberculosis variant bovis**, and lists "Mycobacterium bovis" among its other names
- `CL:0000583` (3 mentions) - the report calls it "Inhaled bacilli infect alveolar macrophages"; CL calls it **alveolar macrophage**

### Terms the ontology service could not be reached for

34 term(s) could not be checked because the ontology service was unreachable (a timeout, 5xx, 408 or 429), not because anything looks wrong with them. Re-run when the service is reachable -- the label cache resumes, so only the unresolved terms are retried:

- `NCBITaxon:1773` (2 mentions)
- `HP:0001945` (1 mention)
- `HP:0012735` (1 mention)
- `HP:0002094` (1 mention)
- `HP:0012378` (1 mention)
- `HP:0002240` (1 mention)
- `HP:0001744` (1 mention)
- `HP:0001250` (1 mention)
- `HP:0033104` (1 mention)
- `HP:0002878` (1 mention)
- `HP:0001974` (1 mention)
- `HP:0031964` (1 mention)
- `HP:0000846` (1 mention)
- `CHEBI:24261` (1 mention)
- `GO:0032609` (1 mention)
- `GO:0002286` (1 mention)
- `GO:0002432` (1 mention)
- `GO:0042116` (1 mention)
- `UBERON:0000029` (1 mention)
- `UBERON:0002360` (1 mention)
- `UBERON:0000955` (1 mention)
- `UBERON:0002113` (1 mention)
- `UBERON:0002369` (1 mention)
- `UBERON:0001776` (1 mention)
- `UBERON:0000160` (1 mention)
- `GO:0005768` (1 mention)
- `GO:0045335` (1 mention)
- `CHEBI:6030` (1 mention)
- `CHEBI:28077` (1 mention)
- `CHEBI:45285` (1 mention)
- `CHEBI:4877` (1 mention)
- `NCBITaxon:9913` (1 mention)
- `NCBITaxon:10090` (1 mention)
- `NCBITaxon:7955` (1 mention)

### Terms whose obsolescence could not be checked

8 term(s) resolved, so they exist, but the ontology service was unreachable for the deprecation check -- treat their obsolescence as unknown rather than clean, and re-run to confirm:

- `MONDO:0000368` (1 mention)
- `HP:0002039` (1 mention)
- `HP:0000554` (1 mention)
- `GO:0006952` (1 mention)
- `GO:0006915` (1 mention)
- `CL:0000492` (1 mention)
- `UBERON:0002107` (1 mention)
- `UBERON:0002106` (1 mention)