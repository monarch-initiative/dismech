---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-05T04:56:52.172262'
end_time: '2026-11-05T05:00:16.465411'
duration_seconds: 204.29
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: NKX2-5-Related Congenital, Conduction and Myopathic Heart Disease
  mondo_id: MONDO:0800441
  category: Mendelian
  causal_genes: NKX2-5
  omim_id: not recorded
  synonyms: NKX2-5-related congenital heart disease; atrial septal defect 7 with or
    without atrioventricular conduction defects; CSX-related congenital heart disease
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
  web_search_requests: 8
  num_turns: 18
  total_cost_usd: 2.3073486
  session_id: 971020a5-5f7d-4da2-800a-932369c3c4f5
  stop_reason: end_turn
  permission_denials: 5
  denied_tools:
  - Bash
  assistant_text_blocks: 2
citation_count: 12
reference_validation:
  total_references: 15
  verified: 15
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 11
  quotes_valid: 10
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMC:PMC4773750
  relevance_assessed: 15
  on_topic: 8
  needs_review: true
  validator_version: 0.5.1
term_validation:
  total_terms: 56
  verified: 54
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 13
  labels_matching: 6
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: GO:0000978
    reported_labels:
    - DNA binding, molecular function
    ontology_label: RNA polymerase II cis-regulatory region sequence-specific DNA
      binding
  - term_id: NCIT:C15986
    reported_labels:
    - Anticoagulation for atrial fibrillation; anticoagulation in LVNC with LV dysfunction
    ontology_label: Pharmacotherapy
  labels_variant: 5
  unresolvable_prefixes:
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** NKX2-5-Related Congenital, Conduction and Myopathic Heart Disease
- **MONDO ID:** MONDO:0800441 (if available)
- **Causal gene(s):** NKX2-5
- **OMIM:** not recorded
- **Synonyms:** NKX2-5-related congenital heart disease; atrial septal defect 7 with or without atrioventricular conduction defects; CSX-related congenital heart disease
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **NKX2-5-Related Congenital, Conduction and Myopathic Heart Disease** covering all of the
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

I'm pulling in more primary literature beyond what the repo already caches. The four PMIDs already cached here are 9651244, 20932824, 22534315 and 29979676, plus the ClinGen record.

I couldn't run PubMed lookups from this sandbox, so the report below rests on the four papers and ClinGen record already cached in the repo, plus web searches. Any PMID I couldn't confirm is marked, and some papers are cited by DOI or PMC ID instead.

# NKX2-5-Related Congenital, Conduction and Myopathic Heart Disease: Research Report

**Target:** MONDO:0800441 · **Causal gene:** *NKX2-5* (HGNC:2488, written `hgnc:2488` in this repository; OMIM gene \*600584) · **Category:** Mendelian, autosomal dominant

The disease is caused by heterozygous variants in *NKX2-5*, the homeobox transcription factor gene at chromosome 5q35.1. It is the human counterpart of the *Drosophila* gene *tinman*. Everything below is about that gene. It is a different gene from *NKX2-1* (thyroid and lung disease), which the repo also holds as `NKX2-1_Related_Choreoathetosis...`.

**What the repo already holds.** `kb/disorders/NKX2-5-Related_Congenital_Conduction_and_Myopathic_Heart_Disease.yaml` already exists (834 lines). There is also a leftover stub, `stubs/NKX2.5-related_Congenital_Conduction_And_Myopathic_Heart_Disease.yaml`, for the same MONDO ID. `just tidy-stubs` should list it as `already_curated`. The quotes marked ✔ below are snippets that entry already cites against the local reference cache. Quotes marked ◇ come from search-result abstracts and still need `just fetch-reference` before use.

---

## 1. Disease information

**Overview.** This is an autosomal dominant cardiac disorder with variable features that can appear together:
- congenital heart defects, mostly secundum atrial septal defect (ASD), and also VSD, tetralogy of Fallot (TOF), other conotruncal defects and hypoplastic left heart syndrome (HLHS);
- atrioventricular (AV) conduction disease that gets worse over time, often reaching complete heart block;
- later-onset myocardial disease: left ventricular noncompaction (LVNC, also called hypertrabeculation) or dilated cardiomyopathy (DCM);
- atrial and ventricular arrhythmias, and a markedly raised risk of sudden cardiac death (SCD).

ClinGen's Congenital Heart Disease Gene Curation Expert Panel merged several separate OMIM entities into this one disease ("lumping"). They reasoned that:

> ✔ "more than 26 unique variants (missense, nonsense, frameshift, deletions) across 18 papers have reported cases of a similar phenotype including congenital heart disease (predominantly ASD), AV block and later onset dilated cardiomyopathy and/or hypertrabeculation with predisposition to atrial and ventricular arrhythmias" (ClinGen CGGV:assertion_c429ebe5…, 2024-11-07)

> ✔ "Phenotype is variable within families and individuals may have only some of these features." (same record)

**Identifiers**

| System | ID | Note |
|---|---|---|
| MONDO | MONDO:0800441 "NKX2.5-related congenital, conduction and myopathic heart disease" | Parents: MONDO:0000992 heart conduction disease; MONDO:0005217 familial cardiomyopathy |
| ClinGen GDV | CGGV:assertion_c429ebe5-43ec-40e7-9d73-55bbbb44f6d1-2024-11-07T170000.000Z | AD, **Definitive**, SOP9 |
| OMIM (entities lumped by ClinGen) | 108900 ASD7 with or without AV conduction defects; 614432 VSD3; 217095 Conotruncal heart malformations, variable; 187500 TOF; 614435 HLHS2 | 614432, 217095, 187500 and 614435 are quoted in the ClinGen record ✔. I recalled 108900 from memory, so check it. |
| OMIM gene | 600584 *NKX2-5* | Check it |
| Orphanet / ICD-10 / ICD-11 / MeSH | No disease-specific code found | The closest broad codes are ICD-10 Q21.1 (ASD), I44.2 (complete AV block), I42.0 (DCM) and I42.8 / ICD-11 BC43.4 (LVNC). Check any of these before use. |

**Synonyms:** NKX2-5-related congenital heart disease; atrial septal defect 7 with or without AV conduction defects (ASD7); CSX-related congenital heart disease; familial ASD with progressive AV block; "Holt–Oram-like ASD with heart block" (historical). (*CSX* is an old name for the gene; *NKX2E* is an alias.)

**Source type.** The evidence is aggregated disease-level knowledge (ClinGen, OMIM, literature reviews) built on family-based linkage, case series and case reports. No EHR-derived cohort exists for it.

## 2. Etiology

**Cause.** Germline heterozygous *NKX2-5* variants. The founding linkage paper said:

> ✔ "A dominant disease locus associated with cardiac malformations and atrioventricular conduction abnormalities was mapped to chromosome 5q35, where NKX2-5, a Drosophila tinman homolog, is located." … "Mutations in the gene encoding the homeobox transcription factor NKX2-5 were found to cause nonsyndromic, human congenital heart disease." (Schott et al. 1998, *Science*, **PMID:9651244**)

**Genetic risk factors and modifiers**
- Variant class affects the phenotype. Truncating variants and homeodomain missense variants carry the full syndrome:
  > ✔ "Variants causing this phenotype appear to be either truncating or missense within the homeodomain." (ClinGen)

  Missense variants outside the homeodomain, found in sporadic CHD, are mostly *not* associated with AV block. McElhinney et al. (2003, *JACC* 42:1650–1655; PMID unconfirmed) found NKX2-5 variants in 18 of 608 CHD patients (3%), and most were missense variants outside the homeodomain without AV block ◇.
- Genetic background changes penetrance in mice:
  > ✔ "We assessed the role of genetic and environmental factors on the incidence of ventricular septal defects (VSDs) caused by a heterozygous Nkx2-5 knockout mutation." (Winston et al., **PMID:22534315**)

  That study found that inbred strain background and maternal age both changed VSD incidence. This is evidence from mice.
- Interacting cardiac transcription factors (GATA4, TBX5, TBX20, HAND2) are biologically plausible modifiers. No human modifier locus has been established.

**Environmental and protective factors.** None are established in humans. The mouse maternal-age effect (PMID:22534315) is the only gene–environment interaction described, and it is model-organism evidence only. No protective variants are known.

## 3. Phenotypes

| Phenotype | Suggested HPO | Onset | Course | Frequency or evidence |
|---|---|---|---|---|
| Secundum atrial septal defect | HP:0001684 Secundum atrial septal defect | Congenital | Stable | Most common lesion. In Ellesøe et al.'s review, 74% of mutation carriers had ASD with conduction disease ◇ |
| Patent foramen ovale / ASD | HP:0001631 Atrial septal defect | Congenital | Stable | Common |
| Ventricular septal defect | HP:0001629 | Congenital | Stable | Occasional (VSD3) |
| Tetralogy of Fallot / conotruncal defects | HP:0001636; HP:0001710 Conotruncal defect | Congenital | Needs surgery | Occasional (Benson 1999) |
| Hypoplastic left heart | HP:0004383 | Congenital | Severe | Rare |
| Ebstein anomaly, double-outlet right ventricle, subvalvar aortic stenosis | HP:0010316, HP:0001718, HP:0001682 | Congenital | Variable | Case-level |
| First-degree AV block | HP:0011705 | Childhood to adulthood | Progressive | Very frequent in carriers of truncating or homeodomain variants |
| Second-degree / complete AV block | HP:0011706 Second degree AV block; HP:0001678 Atrioventricular block | Adolescence to adulthood | Progressive | Frequent. Often appears after ASD repair, and does not depend on surgery |
| Atrial fibrillation / supraventricular arrhythmia | HP:0005110; HP:0004308 Ventricular arrhythmia | Adult | Progressive | ✔ "predisposition to atrial and ventricular arrhythmias" (ClinGen) |
| Left ventricular noncompaction | HP:0032662 Left ventricular noncompaction cardiomyopathy (check label) | Childhood to adult | Progressive | ✔ "This study for the first time identifies association between a NKX2.5 mutation and ventricular noncompaction." (Ouyang et al. 2011, **PMID:20932824**) |
| Dilated cardiomyopathy | HP:0001644 | Adult | Progressive, can reach heart failure | Hanley et al. 2016 (*BMC Med Genet*, PMC5114776) ◇ |
| Syncope | HP:0001279 | Variable | Episodic | ✔ PMID:20932824 |
| Sudden cardiac death | HP:0001645 | Any age; usually adult | — | 19 of 120 (15%) in families with ASD plus conduction disease (Ellesøe 2016, **PMID:26679770**) ◇ |

The defining family report is:

> ✔ "We identified a CHD family with atrial septal defects (ASDs), atrioventricular block, ventricular noncompaction, syncope and sudden death." (PMID:20932824)

**Quality of life.** No disease-specific QoL data exist. The burden comes from repeated surgery, lifelong pacing, ICD shocks and heart failure.

## 4. Genetic and molecular information

- **Gene:** *NKX2-5*, two exons, encoding a 324-amino-acid NK-2 class homeodomain protein. Its domains are an N-terminal tinman (TN) domain, the homeodomain (about residues 138–197), the NK2-specific domain and a C-terminal transactivation domain. Check the residue boundaries against UniProt P52952.
- **Variant spectrum:** missense (concentrated in the homeodomain, e.g. T178M, Q181P, I184M, R190C), nonsense, frameshift (e.g. c.512insGC) and whole-gene deletions. Ellesøe's review counted 59 distinct mutations in 202 patients ◇. Most are private to a family. ClinVar classifications should be pulled at curation time.
- **Functional consequence:** mostly **loss of function / haploinsufficiency**. Some alleles may be **dominant-negative**, and some may gain DNA-binding activity:
  > ✔ "Two are predicted to impair binding of NKX2-5 to target DNA, resulting in haploinsufficiency, and a third potentially augments target-DNA binding." (PMID:9651244)

  > ✔ "Functional studies indicate that the c.512insGC mutation impedes nuclear localization of NKX2.5 and causes a total loss of transactivation activity of NKX2.5." (PMID:20932824)
- **Origin:** germline. A de novo origin is reported in some sporadic cases.
- **Population frequency:** pathogenic homeodomain and truncating variants are absent or ultra-rare in gnomAD.
- **Chromosomal:** deletions at 5q35 that include *NKX2-5* (some overlapping the Sotos region around *NSD1*) can cause CHD with conduction disease as part of a contiguous-gene syndrome.
- **Epigenetics:** no disease-specific data.

## 5. Environmental information

No exposures, lifestyle factors or infectious agents are known to cause or trigger this disease. Mouse data show maternal age affects penetrance (PMID:22534315).

## 6. Mechanism and pathophysiology

**Causal chain**

1. A heterozygous truncating or homeodomain *NKX2-5* variant **leads to** reduced functional NKX2-5 protein (haploinsufficiency; sometimes dominant-negative), through impaired DNA binding, nuclear import or transactivation ✔ (PMIDs 9651244, 20932824).
2. Reduced NKX2-5 dosage **results in** misregulated cardiac transcriptional networks. Normally NKX2-5 works with GATA4, TBX5 and TBX20, drives *NPPA*, *GJA5* (Cx40) and *MYL2*, and represses *BMP10* and atrial genes in the ventricles. This regulatory detail is from mouse and in vitro work; in humans it is inferred.
3. **Branch A, septation:** abnormal atrial septum development and abnormal endocardial-cushion and outflow-tract morphogenesis **lead to** secundum ASD, VSD and conotruncal defects.
   > ✔ "NKX2-5 is important for regulation of septation during cardiac morphogenesis" (PMID:9651244)
4. **Branch B, conduction system:** dose-dependent hypoplasia of the AV node and His–Purkinje system, followed by progressive loss of conduction cells after birth, **leads to** progressive AV block. In Jay et al. 2004 (*JCI*, DOI 10.1172/JCI19846), heterozygous mice had about half the normal number of conduction-system cells ◇. In Pashmforoush et al. 2004 (*Cell* 117:373, DOI 10.1016/S0092-8674(04)00405-2), ventricle-restricted knockout mice had a hypoplastic AV node at birth, then "selective dropout" of conduction cells and complete heart block ◇.
   > ✔ "…for maturation and maintenance of atrioventricular node function throughout life." (PMID:9651244)

   > ✔ "Nkx2-5+/- haploinsufficient mice have an abnormal electrocardiogram, with a prolonged QRS and progressive elongation of the PR interval" (PMID:29979676)
5. **Branch C, myocardium:** failure of trabecular compaction and loss of ventricular myocyte lineage identity (ectopic BMP10, atrial and conduction-system gene expression in the ventricle) **lead to** hypertrabeculation/LVNC with subendocardial fibrosis. Over time this **progresses to** strain defects, DCM and heart failure.
   > ✔ "Conditional deletion of Nkx2-5 at embryonic stages, during trabecular formation, provokes a severe hypertrabeculated phenotype associated with subendocardial fibrosis and Purkinje fiber hypoplasia." … "in 50% of mutant mice, to heart failure." (Choquet et al. 2018, **PMID:29979676**)
6. Branches B and C together (conduction block, a hypoplastic Purkinje network and a fibrotic, noncompacted myocardium) **result in** ventricular arrhythmia and **sudden cardiac death**. SCD has been reported even in people with a working pacemaker. That points to a ventricular arrhythmic substrate, not bradycardia alone. This step is inferred from clinical series.

**Suggested GO terms:** GO:0003290 atrial septum secundum morphogenesis; GO:0060413 atrial septum morphogenesis; GO:0060412 ventricular septum morphogenesis; GO:0003162 atrioventricular node development; GO:0003161 cardiac conduction system development; GO:0060982 coronary artery morphogenesis / GO:0060993 kidney morphogenesis (*not* relevant, avoid); GO:0003222 ventricular trabecula myocardium morphogenesis; GO:0061384 heart trabecula morphogenesis; GO:0007507 heart development; GO:0006357 regulation of transcription by RNA polymerase II; GO:0000978 (DNA binding, molecular function).

**Suggested CL terms:** CL:0002068 Purkinje myocyte; CL:1000409 / CL:1000410 (AV node and His bundle cells; check labels); CL:0002131 regular ventricular cardiac myocyte; CL:0002129 regular atrial cardiac myocyte; CL:0002548 fibroblast of cardiac tissue (check).

**Molecular profiling.** Transcriptomics of conditional *Nkx2-5* mutant mouse hearts is available. GEO:GSE113251 is already cited in the entry ✔ ("identifies Six1 as a marker upregulated in hypertrabeculated hearts"). Patient-iPSC cardiomyocyte studies exist but are small. No human single-cell, spatial or proteomic disease datasets were found.

## 7. Anatomical structures affected

- **Organ:** heart (UBERON:0000948). Specifically: interatrial septum (UBERON:0002085), interventricular septum (UBERON:0002094), AV node (UBERON:0002352), bundle of His (UBERON:0002064), Purkinje fibers (UBERON:0002354, check the CURIE), left ventricular myocardium / trabeculae carneae (UBERON:0002084, UBERON:0002513, check). The cardiovascular system is the only system involved, and the disease is non-syndromic.
- **Subcellular:** nucleus (GO:0005634). Some variants mislocalize the protein to the cytoplasm (PMID:20932824).
- **Lateralization:** not applicable. The myopathy mainly affects the left ventricle.

## 8. Temporal development

- **Onset:** structural defects are congenital. AV conduction delay may be present early, and first-degree block often appears in childhood or adolescence. Higher-grade block, atrial fibrillation, LVNC/DCM and SCD usually appear in adolescence to middle age.
- **Course:** lifelong and progressive for conduction and myocardial disease. Conduction disease progresses whether or not the ASD is repaired. The disease does not remit.
- **Critical window:** the gap between diagnosis of an ASD or first-degree AV block and the onset of high-grade block or SCD. This is when ECG/Holter surveillance and timely pacing or ICD decisions matter.

## 9. Inheritance and population

- **Inheritance:** autosomal dominant (HP:0000006), with high penetrance for truncating and homeodomain variants. Expressivity is variable even within one family.
- **Prevalence:** not established. *NKX2-5* variants are found in about 1–4% of unselected CHD cohorts (≈3% in McElhinney 2003 ◇). Rates are higher in familial ASD with AV block. A conservative estimate is `prevalence_class: NOT_YET_DOCUMENTED` or `RARE`, with `measure_type: UNKNOWN`.
- No anticipation, founder effects or ancestry bias are known. Both sexes are affected equally. Germline mosaicism is possible but rarely reported.

## 10. Diagnostics

- **ECG:** PR prolongation, progressive AV block, QRS widening (LOINC 8626-4 PR interval, 8633-0 QRS duration; check these codes with `just loinc-seed-cache`). Use Holter or ambulatory monitoring.
- **Imaging:** transthoracic or transesophageal echocardiography for septal defects. Cardiac MRI for LVNC (noncompacted-to-compacted ratio above 2.3 in diastole, Petersen criteria), LV function and late gadolinium enhancement (fibrosis).
- **Genetic testing:** single-gene *NKX2-5* sequencing plus deletion/duplication analysis. Alternatively, a CHD, cardiomyopathy or conduction-disease panel, or exome sequencing. CMA if syndromic features suggest a 5q35 deletion. Cascade testing of relatives.
- **Clinical clue:** **ASD plus AV block in a family** should prompt *NKX2-5* testing.
- **Differential diagnosis:**
  - Holt–Oram syndrome (*TBX5*; upper-limb defects);
  - *GATA4*-related CHD (usually no AV block);
  - *LMNA* cardiomyopathy (AV block plus DCM; no ASD; raised CK);
  - *SCN5A* progressive cardiac conduction disease;
  - *TBX20*;
  - *MYH6*-related ASD;
  - *TBX5*;
  - post-surgical heart block.

## 11. Outcome and prognosis

- **SCD** is the main cause of death. In the Ellesøe review it occurred in 15% of individuals in families with ASD plus conduction disease (9 confirmed and 10 possible carriers) ◇ (PMID:26679770), and some deaths happened despite a pacemaker.
- Other burdens: heart failure from DCM/LVNC, and atrial fibrillation with thromboembolic risk.
- **Prognostic factors:** truncating or homeodomain variant; family history of SCD; LV dysfunction; ventricular arrhythmia; fibrosis on MRI. Formal risk models are not available.

## 12. Treatment

There is no disease-modifying therapy, so management is symptomatic and preventive.

| Intervention | NCIT suggestion | Modality |
|---|---|---|
| Surgical or transcatheter ASD/VSD closure; TOF repair | NCIT:C15329 Surgical Procedure | SURGERY |
| Permanent pacemaker for high-grade AV block | NCIT:C15329 (procedure); device as a qualifier (NCIT:C16830 Medical Device; check NCIT pacemaker device term) | DEVICE |
| ICD for primary prevention in carriers (proposed by Ellesøe; follow the HRS/AHA cardiomyopathy and conduction guidelines) | NCIT:C15329, plus device qualifier | DEVICE |
| Guideline-directed heart-failure drugs (ACE inhibitor/ARB/ARNI, β-blocker, MRA, SGLT2 inhibitor) for DCM/LVNC | NCIT:C15986 Pharmacotherapy + `therapeutic_agent` (CHEBI) | SMALL_MOLECULE |
| Anticoagulation for atrial fibrillation; anticoagulation in LVNC with LV dysfunction | NCIT:C15986 | SMALL_MOLECULE |
| Heart transplantation (end stage) | NCIT:C15289 Organ Transplantation | SURGERY |
| Genetic counseling | NCIT:C15240 | — |

Pacing (prefer physiologic, conduction-system pacing) and ICDs carry lifelong device risks. No pharmacogenomic issues, gene therapy or registered disease-specific trials were found.

## 13. Prevention

- **Primary:** no primary prevention exists apart from reproductive options: prenatal testing or preimplantation genetic testing for a known familial variant.
- **Secondary:** cascade genotyping of relatives. Serial ECG, Holter, echocardiography and MRI in carriers, including those with a repaired or absent ASD.
- **Tertiary:** pacing at the onset of high-grade block, and a low threshold for an ICD.
- No vaccines or public-health measures apply.

## 14. Other species

No naturally occurring animal disease is recorded in OMIA (check before citing). The gene is highly conserved: mouse *Nkx2-5* (MGI:97350, check), zebrafish *nkx2.5*, *Drosophila* *tin*.

## 15. Model organisms

| Model | Phenotype | How well it matches human disease | Reference |
|---|---|---|---|
| *Nkx2-5*⁻/⁻ mouse | Embryonic lethal; looping failure; no MLC2V expression | Too severe; developmental only | Lyons et al. 1995, *Genes Dev* 9:1654 (DOI 10.1101/gad.9.13.1654) ◇; Tanaka et al. 1999 *Development* ◇ |
| *Nkx2-5*⁺/⁻ mouse | ASD/PFO and VSD (penetrance depends on strain); PR/QRS prolongation; AV-node/His–Purkinje hypoplasia | Partial match: septal and conduction features are reproduced | Jay 2004 ◇; PMID:22534315 ✔; PMID:29979676 ✔ |
| Ventricle-restricted knockout (MLC2v-Cre) | Progressive complete heart block, trabecular overgrowth, ectopic BMP10 | Matches the conduction and myopathy features; no septal defects | Pashmforoush 2004 ◇ |
| Inducible trabecular knockout (*Cx40-creERT2*) | Hypertrabeculation, subendocardial fibrosis, Purkinje hypoplasia, heart failure in 50% | Strong LVNC model | PMID:29979676 ✔ |
| Patient iPSC-derived cardiomyocytes; zebrafish *nkx2.5* morphants/mutants | Cellular electrophysiology and differentiation defects | In vitro or non-mammalian | Literature exists; not checked here |

**Limits of the mouse models:** mice show the septal and conduction features at a mouse heart rate. Human-like adult SCD and atrial fibrillation are not modelled well, and the strain-dependent penetrance argues for a `HUMAN_MODEL_MISMATCH` discussion.

---

## Curation notes for the existing entry

- The stub is stale: the KB already holds this MONDO ID. `just tidy-stubs --apply` should delete it.
- The entry relies on only four PMIDs. These papers are worth adding with `just fetch-reference`:
  - Benson et al. 1999 (*JCI* 104:1567; DOI 10.1172/JCI8154; PMID 10587520 from a third-party mirror, so confirm it). This covers the TOF, VSD and conotruncal spectrum.
  - Ellesøe et al. 2016 (**PMID:26679770**). This covers SCD frequency and the ICD recommendation.
  - Pashmforoush et al. 2004 (*Cell*). This covers conduction-cell dropout and BMP10.
  - Jay et al. 2004 (*JCI*). This covers dose-dependent conduction-system hypoplasia.
  - Morlanes-Gracia et al. 2021 (*Front Cardiovasc Med*, PMC8280289; p.Gln181Pro with LVNC and SCD).
  - Hanley et al. 2016 (*BMC Med Genet*, PMC5114776; DCM).
  - McElhinney et al. 2003 and Elliott et al. 2003 (*JACC*). These cover genotype–phenotype data in sporadic CHD and HLHS.
- Run `just check-genereviews` on the entry. I found no GeneReviews chapter specific to NKX2-5.
- Every HPO, GO, CL, UBERON, NCIT and LOINC CURIE suggested above is a lead I recalled, not something I looked up. Verify each one in `cache/<prefix>/terms.csv`, with `runoak`, or in OLS before binding it.

## Sources
- Schott JJ et al. 1998 *Science* — PMID:9651244 (cached in repo)
- Ouyang P et al. 2011 — PMID:20932824 (cached)
- Winston JB et al. 2012 — PMID:22534315 (cached)
- Choquet C et al. 2018 — PMID:29979676 (cached)
- ClinGen GDV CGGV:assertion_c429ebe5-43ec-40e7-9d73-55bbbb44f6d1-2024-11-07T170000.000Z (cached)
- [Benson et al. 1999, JCI (PMC409868)](https://pmc.ncbi.nlm.nih.gov/articles/PMC409868) · [JCI PDF](https://jci.org/articles/view/8154/files/pdf)
- [Ellesøe et al. 2016, Congenit Heart Dis — PubMed 26679770](https://pubmed.ncbi.nlm.nih.gov/26679770/) · [record](https://test01.ku.dk/:obvius/pureproxy/3974268/da/publications/familial-atrial-septal-defect-and-sudden-cardiac-death-identifica)
- [Pashmforoush et al. 2004, Cell (Scilit)](https://scilit.com/publications/3a3311871440b8b17ab99152be0322a0)
- [Jay et al. 2004, JCI](https://www.jci.org/articles/view/19846/version/1/pdf/render.pdf)
- [Lyons et al. 1995, Genes Dev](https://genesdev.cshlp.org/content/9/13/1654.abstract)
- [Tanaka et al. 1999, Development (via JCI references)](https://www.jci.org/references/scholar/21782/B12)
- [Morlanes-Gracia et al. 2021, Front Cardiovasc Med (PMC8280289)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8280289/)
- [Hanley et al. 2016, BMC Med Genet (PMC5114776)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5114776/)
- [Chung & Rajakumar 2016, "Genetics of CHD: the NKX2-5 gene, a key player" (PMC4773750)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4773750/)
- [McElhinney / Elliott 2003 JACC records](https://insight.jci.org/references/scholar/2339/B51)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 11 |
| Quoted claims found in source | 10 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 15 |
| On topic | 8 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMC:PMC4773750` *(abstract only)*: "Genetics of CHD: the NKX2-5 gene, a key player"
  - closest text in source: "The mutant NKX2-5 factor can regulate a number of off-targets downstream to facilitate CHD development"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 56 |
| Resolved | 54 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 13 |
| Terms named correctly | 6 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `GO:0000978` (1 mention) - the report calls it "DNA binding, molecular function"; GO calls it **RNA polymerase II cis-regulatory region sequence-specific DNA binding**
- `NCIT:C15986` (2 mentions) - the report calls it "Anticoagulation for atrial fibrillation; anticoagulation in LVNC with LV dysfunction"; NCIT calls it **Pharmacotherapy**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0004383` (1 mention) - the report calls it "Hypoplastic left heart"; HP calls it **Hypoplastic left ventricle**
- `HP:0011705` (1 mention) - the report calls it "First-degree AV block"; HP calls it **First degree atrioventricular block**
- `CL:1000410` (1 mention) - the report calls it "AV node and His bundle cells; check labels"; CL calls it **myocyte of atrioventricular node**, and lists "AV node cardiac muscle cell" among its other names
- `UBERON:0000948` (1 mention) - the report calls it "Organ:** heart"; UBERON calls it **heart**, and lists "branchial heart" among its other names
- `GO:0005634` (1 mention) - the report calls it "Subcellular:** nucleus"; GO calls it **nucleus**, and lists "cell nucleus" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`.