---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-24T16:13:07.673856'
end_time: '2026-11-24T16:20:34.674417'
duration_seconds: 447.0
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Genitourinary and/or Brain Malformation Syndrome
  mondo_id: MONDO:0032934
  category: Mendelian
  causal_genes: PPP1R12A
  omim_id: OMIM:618820
  synonyms: genitourinary and/or/brain malformation syndrome; GUB syndrome; UBM syndrome;
    UBMS; Urogenital and/or brain malformation syndrome
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
  web_search_requests: 12
  num_turns: 22
  total_cost_usd: 1.4767125500000005
  session_id: 00d11817-ac93-40a6-a6b2-299aeaf5e366
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  tool_calls: 38
  retrieval_calls: 36
  assistant_text_blocks: 2
citation_count: 9
reference_validation:
  total_references: 25
  verified: 25
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 2
  relevance_assessed: 25
  on_topic: 13
  validator_version: 0.8.0
term_validation:
  total_terms: 93
  verified: 91
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 4
  labels_matching: 0
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: MONDO:0032934
    reported_labels:
    - MONDO
    ontology_label: genitourinary and/or brain malformation syndrome
  - term_id: HP:0001250
    reported_labels:
    - Rare; neonatal seizures (Tong 2024, PMID 39334371); hypersynchronous EEG in
      MIHV-HPE (Pandya 2025, PMID 40448330)
    ontology_label: Seizure
  - term_id: HP:0001643
    reported_labels:
    - Rare (GeneReviews; Horn 2026)
    ontology_label: Patent ductus arteriosus
  - term_id: HP:0000407
    reported_labels:
    - 1 case (Pianigiani 2026, PMID 42650049)
    ontology_label: Sensorineural hearing impairment
  obsolete_terms:
  - term_id: HP:0000057
    ontology_label: obsolete Clitoromegaly
    replaced_by: HP:0008665
  unresolvable_prefixes:
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Genitourinary and/or Brain Malformation Syndrome
- **MONDO ID:** MONDO:0032934 (if available)
- **Causal gene(s):** PPP1R12A
- **OMIM:** OMIM:618820
- **Synonyms:** genitourinary and/or/brain malformation syndrome; GUB syndrome; UBM syndrome; UBMS; Urogenital and/or brain malformation syndrome
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Genitourinary and/or Brain Malformation Syndrome** covering all of the
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

I'm still collecting sources. I have the founding 2020 paper and a 2025 twin report, and I'm now looking for the later case reports, Orphanet IDs and the animal-model papers.

I found the core literature: the 2020 founding cohort, the GeneReviews chapter (read through a mirror), and about 15 later case reports and model-organism papers. The report follows.

---

# Genitourinary and/or Brain Malformation Syndrome (GUBS / UBMS), caused by PPP1R12A: Research Report

**How I scoped this:** The report covers the autosomal dominant syndrome OMIM #618820, caused by heterozygous loss-of-function (LoF) variants in ***PPP1R12A*** (MYPT1, the myosin phosphatase targeting subunit 1). I used MONDO:0032934 as given but could not check it against the MONDO site.

**Limits on what I could read:**
- **Blocked pages:** PubMed, PMC and Wiley pages often returned bot-check or 403 pages.
- **Where the content came from instead:** the Hughes 2020 full text on PMC (only the first half was read verbatim), the GeneReviews chapter via a mirror, Europe PMC REST records, a Translational Pediatrics full text, and search-engine abstracts.
- **Short quotes:** many publisher abstracts could only be quoted in short excerpts. Points I had only second-hand are marked "(abstract summary)".
- **Unverified identifiers:** HGNC, NCBI Gene and Orphanet IDs could not be retrieved this session and are marked.

---

## 1. Disease Information

**Overview.** GUBS is a rare congenital multiple-malformation syndrome caused by heterozygous, usually de novo, LoF variants in *PPP1R12A* (chromosome 12q21.2–q21.31). GeneReviews (Alkhunaizi & Chitayat; first posted 9 Sep 2021, last revised 7 Mar 2024; PMID 34499436; https://www.ncbi.nlm.nih.gov/books/NBK573670/) says affected individuals "usually present with multiple congenital anomalies, most commonly involving the brain and/or urogenital systems." The most severe brain abnormalities lie on the holoprosencephaly (HPE) spectrum. Regardless of brain findings, 46,XY individuals may have a difference of sex development (DSD).

OMIM #618820 describes variable genital and urinary anomalies, including disorders of sex differentiation, with brain malformations "ranging from absence of the corpus callosum to anencephaly" (OMIM via mirror: https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/618820).

**Founding report.** Hughes JJ et al., "Loss-of-Function Variants in PPP1R12A: From Isolated Sex Reversal to Holoprosencephaly Spectrum and Urogenital Malformations," *Am J Hum Genet* 2020;106:121–128, doi:10.1016/j.ajhg.2019.12.004, **PMID 31883643** (https://pmc.ncbi.nlm.nih.gov/articles/PMC7042489).
- Abstract: "This gene has not been previously reported in association with human disease."
- The authors propose "the association of PPP1R12A pathogenic variants with a congenital malformations syndrome affecting the embryogenesis of the brain and genitourinary systems and including disorders of sex development."

**Identifiers**

| Resource | ID | Status |
|---|---|---|
| OMIM (phenotype) | 618820 (GUBS) | Retrieved |
| OMIM (gene) | 602021 | Retrieved (GeneReviews) |
| MONDO | MONDO:0032934 | As supplied; not independently checked |
| KEGG DISEASE | H02523 | Retrieved (https://www.kegg.jp/entry/H02523) |
| ICD-11 | LD2Y (other specified multiple developmental anomalies, a non-specific cross-reference listed by KEGG) | Retrieved via KEGG |
| MedGen | C5394158 | Retrieved (search result) |
| GeneReviews | NBK573670 / PMID 34499436 | Retrieved |
| UniProt | O14974 (MYPT1_HUMAN) | Retrieved (GeneReviews) |
| Orphanet | Not found in searches | Not verified |
| ICD-10 / MeSH | No specific code or descriptor found; ICD-10 Q89.7 (multiple congenital malformations, NEC) would be a reasonable fallback | Not verified |

**Synonyms:** genitourinary and/or brain malformation syndrome (GUBS); urogenital and/or brain malformation syndrome (UBMS); PPP1R12A-related urogenital and/or brain malformation syndrome (GeneReviews title).

**Source type:** All knowledge comes from aggregated published case reports and small case series of individual patients. There are no registries and no EHR-scale cohorts.

---

## 2. Etiology

**Causal factor.** The cause is heterozygous germline LoF of *PPP1R12A*: nonsense, frameshift, canonical and non-canonical splice, and stop-loss variants.
- Hughes 2020 found 6 stop-gain, 5 frameshift and 1 splice-acceptor variants among 12 individuals (PMID 31883643).
- Reported mechanism: haploinsufficiency. GeneReviews states the condition is "autosomal dominant," typically caused by a "de novo" pathogenic variant.

**Genetic risk factors.**
- *PPP1R12A* is highly LoF-intolerant: gnomAD shows 3 observed vs 59.8 expected LoF variants (o/e = 0.05), which is "within the range associated with genes intolerant to LoF" (Hughes 2020).
- Contiguous 12q21 deletions that include *PPP1R12A* cause an overlapping phenotype, including cryptorchidism and corpus callosum hypoplasia (Hughes 2020). GeneReviews notes 14 such individuals and excludes them from its frequency counts.
- No modifier genes have been identified.

**Environmental risk, protective factors, gene–environment interactions:** none reported. Monozygotic 46,XY twins with the same de novo c.1551-2A>G variant had discordant genital phenotypes (Prader III vs IV) and gonadal function (Tian H et al., *Transl Pediatr* 2025;14:1708–1716, doi:10.21037/tp-2025-166, PMID 40800196; https://tp.amegroups.org/article/view/140867/html). This implies stochastic or non-genetic developmental factors in expressivity, but none has been named.

---

## 3. Phenotypes

**Frequency data.**
- GeneReviews Table 2 (n = 12, Hughes 2020): 46,XY DSD and/or GU anomalies 9/12 (75%); developmental delay 7/12 (58%); brain malformation 5/12 (42%), "typically along the holoprosencephaly spectrum"; eye/vision problems 3/12 (25%).
- Hughes 2020: both brain and GU anomalies in 2–3 individuals (the abstract says 2; Table 1 shows individuals 3, 6 and 7 with both).
- Later reviews:
  - Tian 2025 (about 20 individuals): brain malformations in 7, developmental delay in 8, eye anomalies in 4, "digestive tract atresia" in 4. Among 46,XY individuals, 9/14 had persistent Müllerian derivatives and 11/14 had under-masculinized genitalia, with testicular dysgenesis in 6 of those 11.
  - Gomes 2025 (PMID 40770999; 22 cases): gastrointestinal anomalies in about 32%, mostly jejunal or ileal atresia, with one esophageal atresia (search-result summary).
  - Bland 2026 (PMID 42178607): "To date, 22 affected individuals have been reported."

Onset of all structural features is congenital or prenatal, and the malformations are static. Severity ranges from isolated 46,XY DSD with normal intelligence to anencephaly.

| Phenotype | Type | Frequency (best estimate) | Suggested HPO |
|---|---|---|---|
| 46,XY DSD / atypical genitalia | Physical sign | 9/12 (Hughes); 11/14 46,XY (Tian) | HP:0000062 Ambiguous genitalia; HP:0008730 Female external genitalia in individual with 46,XY karyotype |
| Hypospadias | Sign | ≥4/12 (Hughes individuals 5, 6, 7, 10) | HP:0000047 Hypospadias |
| Cryptorchidism | Sign | ≥3/12 (5, 7, 10) | HP:0000028 Cryptorchidism |
| Micropenis, chordee | Sign | Individuals 5 and 6; Diao 2023 | HP:0000054 Micropenis; HP:0000041 Chordee |
| Persistent Müllerian structures (uterus/tubes) in 46,XY | Imaging/surgical | 9/14 46,XY (Tian); 5/24 PMDS cohort (Picard) | HP:0000130 Abnormal uterus morphology (Müllerian remnants) |
| Gonadal dysgenesis / streak gonads | Sign/lab | 6/11 (Tian); individuals 8 and 11 | HP:0000133 Gonadal dysgenesis |
| Urogenital sinus, posterior labial fusion, clitoromegaly | Sign | Individuals 9, 11, 12 | HP:0000057 Clitoromegaly |
| Holoprosencephaly (alobar, semilobar, MIHV) | Imaging | 2/12 (individuals 1 and 2) plus later cases | HP:0001360 Holoprosencephaly; HP:0002507 Semilobar HPE; HP:0006872 Middle interhemispheric variant of HPE |
| Corpus callosum agenesis/dysgenesis | Imaging | 3/12 | HP:0001274 Agenesis of corpus callosum |
| Anencephaly/acrania/exencephaly; encephalocele | Prenatal imaging | 1/12; NTD fetuses (Botvinik 2026) | HP:0002323 Anencephaly; HP:0002084 Encephalocele |
| Polymicrogyria / cortical dysplasia / heterotopia | Imaging | Individuals 1 and 6 | HP:0002126 Polymicrogyria; HP:0002282 Gray matter heterotopia |
| Chiari malformation; absent septum pellucidum | Imaging | Individuals 1 and 6 | HP:0002308; HP:0001331 |
| Developmental delay / ID | Behavioral | 7/12; 8/~20 | HP:0001263; HP:0001249 |
| Autistic features; ADHD | Behavioral | Rare (GeneReviews; individual 3) | HP:0000729; HP:0007018 |
| Seizures | Neurologic | Rare; neonatal seizures (Tong 2024, PMID 39334371); hypersynchronous EEG in MIHV-HPE (Pandya 2025, PMID 40448330) | HP:0001250 |
| Micro- or macrocephaly | Sign | Individuals 1 and 2 | HP:0000252; HP:0000256 |
| Strabismus, nystagmus, retinal dystrophy, microphthalmia/anophthalmia | Sign | 3/12; 4/~20 | HP:0000486; HP:0000639; HP:0000568 |
| Jejunal/ileal atresia; esophageal atresia/TEF | Sign | ~32% (Gomes); 3 ileal and 1 esophageal in 5 PMDS cases (Picard) | HP:0005235 Duodenal atresia (closest available); HP:0002575 TEF; HP:0002032 Esophageal atresia |
| Anorectal malformation / imperforate anus / anterior anus | Sign | Case reports (Wehrli/Harris 2023; Gomes 2025; Horn 2026) | HP:0002023 Anal atresia |
| Omphalocele | Sign | 1/12 | HP:0001539 |
| Renal anomalies (asymmetry, pyelectasis, duplicated collecting system) | Imaging | Rare | HP:0000077 Abnormality of the kidney |
| Kyphoscoliosis; finger clinodactyly; toe syndactyly | Skeletal | Rare | HP:0002751; HP:0004209; HP:0001770 |
| Facial dysmorphism (hypertelorism, epicanthus inversus, deformed pinnae) | Sign | ~6/20 | HP:0000316; HP:0000377 |
| PDA and other cardiac defects | Sign | Rare (GeneReviews; Horn 2026) | HP:0001643 |
| Sensorineural hearing loss with inner-ear malformation | Sign | 1 case (Pianigiani 2026, PMID 42650049) | HP:0000407 |
| GH deficiency, ectopic posterior pituitary, short stature | Endocrine | 1 case (Saul 2026, PMID 41626296) | HP:0000824; HP:0011755; HP:0004322 |
| Growth restriction (IUGR, postnatal) | Sign | Rare | HP:0001511; HP:0008897 |
| Feeding difficulties | Symptom | With severe HPE (GeneReviews) | HP:0011968 |

**Quality of life:** No QoL instrument data (EQ-5D, SF-36, PROMIS) exist. Expected impacts:
- Severe HPE causes major neurodevelopmental disability, seizures and feeding dependence.
- DSD affects sex-of-rearing decisions, need for surgery, fertility (dysgenetic gonads) and psychosocial wellbeing; GeneReviews recommends gender-identity surveillance.
- Isolated DSD may be compatible with normal intelligence.

---

## 4. Genetic/Molecular Information

**Gene.** *PPP1R12A* (protein phosphatase 1 regulatory subunit 12A; alias MYPT1, MBS); OMIM 602021; UniProt O14974; locus 12q21.2–q21.31; reference transcript NM_002480.3 (Hughes 2020). HGNC ID and NCBI Gene ID were not retrieved this session.

**Protein function.** MYPT1 targets PP1cδ (PPP1CB) to myosin II and, with M20/M21, forms myosin phosphatase (MP), which dephosphorylates myosin regulatory light chain (MRLC). MP regulates cell shape, migration, adhesion and morphogenesis (Hughes 2020; Kiss et al., review, PMID 30076859). Hughes 2020: pathogenic variants "prevent PPP1R12A from binding to PP1c and result in a non-functional MP."

**Reported pathogenic variants** (NM_002480.3 unless noted; all heterozygous; de novo where parents were tested):
- **Hughes 2020:** c.223_224delAC p.(Thr75Cysfs\*8); c.681dupT p.(Lys228\*); c.793-1G>A (splice); c.960dupA p.(Glu321Argfs\*6); c.1189delA p.(Thr397Hisfs\*42); c.1415C>G p.(Ser472\*); c.1510C>T p.(Arg504\*); c.2033_2034delCT p.(Ser678\*); c.2073dupA p.(Ser692Ilefs\*2); c.2573G>A p.(Trp858\*); c.2698C>T p.(Arg900\*); c.2739_2740delCT p.(Leu914Argfs\*14).
- **Later reports:**
  - c.2666+3A>G: exon 20 skipping → p.Thr884IleTer2 by minigene assay (Diao 2023, *Mol Genet Genomic Med*, PMID 37272772).
  - c.1551-2A>G (Tian 2025, PMID 40800196).
  - c.1880delC (Contreras-Capetillo 2025, PMID 39257322).
  - c.2533C>T p.(Arg845Ter): the truncated protein no longer interacts with PPP1CB (Tong 2024, PMID 39334371).
  - Stop-loss c.3092A>T p.(Ter1031LeuextTer71), recurrent in two individuals with intestinal atresia (Gomes 2025, PMID 40770999).
  - A separate stop-loss variant with anorectal malformation and DSD (Wehrli/Harris, *J Pediatr Surg Case Rep* 2023; 95; https://doaj.org/article/0a1621b6cf7044a285f88c537e66b74d).
  - c.2629del p.(Ser877Profs\*38), with VACTERL-like features (Horn 2026, PMID 43001012).
  - p.(Lys197IlefsTer13), with PMDS (Voide 2026, PMID 42846858).
  - c.792+3A>C: exon 5 skipping (Pianigiani 2026, PMID 42650049).
  - An intronic variant creating an out-of-frame transcript (Bland 2026, PMID 42178607).
  - A splice-site variant in a female fetus with perineal hamartoma (Chen 2026, PMID 42165277).
  - The missense c.38A>G p.(Gln13Arg), reported as likely pathogenic (NM_002480.2; Saul 2026, PMID 41626296). This is the only reported missense; its mechanism is uncertain.

**Classification:** The Tian twin variant was classified as pathogenic under ACMG 2015. Most others are reported as pathogenic or likely pathogenic; I did not retrieve ClinVar records.

**Allele frequency:** The variants are absent or ultra-rare in gnomAD (constraint above).

**Origin:** germline. *PPP1R12A* somatic CNVs and fusions in cancer (colorectal cancer; bladder rhabdomyosarcoma) are not heritable and are unrelated (GeneReviews).

**Functional consequence:** LoF / haploinsufficiency. Nonsense-mediated decay is predicted for premature-stop variants, not tested (Hughes 2020). Hughes 2020 also notes that loss of either MP subunit can reduce the other's expression.

**Genotype–phenotype correlation:** "No genotype-phenotype correlations have been identified" (GeneReviews). Hughes 2020: "a clear genotype-phenotype correlation was not seen."

**Modifier genes and epigenetics:** none reported.

**Chromosomal abnormalities:** 12q21 microdeletions including *PPP1R12A* overlap the phenotype (Hughes 2020; GeneReviews).

---

## 5. Environmental Information

No environmental, lifestyle or infectious contributors have been reported. Not applicable for this monogenic developmental disorder.

---

## 6. Mechanism / Pathophysiology

**Causal chain**

1. A heterozygous germline LoF variant in *PPP1R12A* (usually de novo) → premature stop / NMD or aberrant splicing (*demonstrated by minigene assay for c.2666+3A>G and c.792+3A>C; NMD predicted, not shown*) → **leads to** about 50% MYPT1 protein (haploinsufficiency; *inferred* from variant spectrum and constraint).
2. Reduced MYPT1, or a truncated protein unable to bind PP1cδ (*shown in vitro for p.Arg845Ter*, PMID 39334371) → **results in** reduced myosin phosphatase activity.
3. Reduced MP activity → **leads to** sustained MRLC phosphorylation and excess actomyosin contractility (*demonstrated in zebrafish*: overactive myosin in the *mypt1* mutant, rescued by blebbistatin, PMID 20147380; ectopic F-actin and phospho-MRLC in the intestinal atresia model, PMID 41805950).
4. Excess contractility → **disrupts** cell shape change, epithelial relaxation, collective cell migration and convergent extension in embryonic tissues (*model organisms*; human relevance *inferred*). From here the mechanism branches:
   - **4a. Forebrain:** *PPP1R12A* is expressed in head mesenchyme of the prosencephalic neural folds (mouse, about GD 8.25; Hughes 2020). Defective migration of prechordal plate / anterior midline cells (zebrafish morpholino cyclopia and gastrulation defects cited by Hughes) → **leads to** failed forebrain midline division → HPE spectrum and corpus callosum agenesis. Separately, failed neural tube closure → anencephaly/encephalocele. *Inferred*. SHH-pathway involvement is unproven; HPE individuals screened negative for SHH, ZIC2, SIX3 and TGIF1.
   - **4b. Urogenital:** MYPT1 is present in genital tubercle epithelium, urethra, bladder and urogenital sinus mesenchyme (mouse E13–13.75; human embryos at week 10; Hughes 2020). Impaired morphogenesis → **leads to** hypospadias and urogenital sinus anomalies. Impaired testis cord formation → gonadal dysgenesis → low testosterone/AMH → under-virilization (*inferred*; low AMH and inhibin B in Twin A, Tian 2025). Failed Müllerian duct regression despite normal AMH → PMDS. Picard 2022 proposed that MP-dependent cell motility is required for Müllerian regression, or that it affects AMH transduction, and acknowledged a "lack of experimental validation" (PMID 36331510). Voide 2026 suggests "abnormal duct development rather than primary gonadal failure" in some cases (PMID 42846858).
   - **4c. Gut:** abnormal epithelial organization and smooth-muscle myosin hyperactivity → **leads to** jejunal/ileal atresia. In the model, "Inhibition of myh11a, encoding smooth muscle (SM) myosin heavy chain, ameliorated the IA phenotype" (Kobayashi 2026, *Dis Model Mech*, PMID 41805950).
5. These structural malformations are fixed before birth and **result in** the clinical picture: developmental delay or ID, seizures and feeding problems (with HPE); DSD and infertility; obstruction needing neonatal surgery.

**Checklist**
- **Pathways:** RhoA/ROCK–MLCK–myosin II contractility (Reactome "RHO GTPases activate ROCK"; "Smooth Muscle Contraction"). Kiss 2019 also describes non-contractile MP roles in the cell cycle and gene expression (PMID 30076859).
- **Cellular processes:** cell migration, epithelial morphogenesis, convergent extension, cell shape regulation.
- **Not reported:** immune, metabolic or epigenetic mechanisms; transcriptomic, proteomic or single-cell profiling.
- **Suggested GO terms:** GO:0017018 myosin phosphatase activity (MF); GO:0072357 PTW/PP1 phosphatase complex (CC); GO:0016477 cell migration; GO:0060027 convergent extension involved in gastrulation; GO:0021987 cerebral cortex development / GO:0030900 forebrain development; GO:0001843 neural tube closure; GO:0030539 male genitalia development; GO:0001880 Müllerian duct regression; GO:0008584 male gonad development; GO:0048565 digestive tract development; GO:0031032 actomyosin structure organization.
- **Suggested CL terms:** CL:0000066 epithelial cell; CL:0000134 mesenchymal stem cell (urogenital sinus/head mesenchyme, approximate); CL:0000192 smooth muscle cell; CL:0000216 Sertoli cell (inferred for gonadal dysgenesis); CL:0000133 neurectodermal cell.

---

## 7. Anatomical Structures Affected

**Primary organs (with UBERON terms)**
- Forebrain/telencephalon: UBERON:0001890, UBERON:0001893
- Corpus callosum: UBERON:0002336
- Neural tube: UBERON:0001049
- External genitalia: UBERON:0004176
- Penis/urethra: UBERON:0000989, UBERON:0000057
- Genital tubercle: UBERON:0005876
- Urogenital sinus: UBERON:0000164
- Gonad/testis: UBERON:0000991, UBERON:0000473
- Müllerian duct: UBERON:0003890
- Kidney: UBERON:0002113
- Small intestine/jejunum/ileum: UBERON:0002108, UBERON:0002115, UBERON:0002116
- Esophagus: UBERON:0001043
- Anus/rectum: UBERON:0001245, UBERON:0001052
- Eye: UBERON:0000970
- Inner ear: UBERON:0001846
- Pituitary: UBERON:0000007

**Body systems:** nervous, reproductive, urinary, digestive, visual and auditory, skeletal (kyphoscoliosis), with rare cardiovascular and endocrine involvement.

**Tissues and cells:** embryonic epithelia (genital tubercle, urethra, gut), urogenital sinus and head mesenchyme, and detrusor smooth muscle (human week-10 embryo; Hughes 2020).

**Subcellular (GO CC):** cytoplasm and actomyosin cytoskeleton (GO:0042641 actomyosin), stress fibers (GO:0001725), PP1 holoenzyme complex.

**Laterality:** midline defects predominate (HPE, hypospadias). Gonadal findings may be bilateral or asymmetric, for example left cryptorchidism in Twin B and renal asymmetry in Hughes individual 3.

---

## 8. Temporal Development

- **Onset:** congenital. Many cases are detected prenatally, for example dilated bowel and polyhydramnios (Saul 2026), anencephaly at 12 weeks (Hughes 2020), and neural tube defects or encephalocele (Botvinik 2026, PMID 41714291).
- **Course:** non-progressive structural malformations, lifelong. Neurodevelopmental impairment is static; seizures may be chronic. Puberty is a critical window: hormone replacement may be needed for dysgenetic gonads, and gender identity should be assessed.
- **Critical periods:** embryonic forebrain division (gastrulation and neurulation) and urogenital or gonadal differentiation around weeks 6–12. Minipuberty (about 2 weeks to 3 months) is a diagnostic window for gonadal hormone testing (GeneReviews; Voide 2026).
- **Remission:** not applicable.

---

## 9. Inheritance and Population

- **Prevalence/incidence:** "The prevalence has not been determined" (GeneReviews). About 22–25 individuals have been published as of 2026 (Bland 2026; plus the 2026 reports above).
- **Inheritance:** autosomal dominant. Every proband whose parents were tested had a de novo variant. Parental mosaicism has not been reported; GeneReviews estimates about 1% sibling recurrence risk for possible germline mosaicism, and 50% risk to the offspring of an affected individual.
- **Penetrance and expressivity:** expressivity is highly variable, even between monozygotic twins (Tian 2025). Penetrance has not been formally estimated. No anticipation, founder effects, consanguinity role or carrier frequency is relevant.
- **Sex:** DSD manifests in 46,XY individuals, and 46,XY individuals predominate among reported cases. This likely reflects ascertainment through DSD cohorts: 9 of 12 in Hughes were 46,XY. 46,XX individuals present with brain malformations, and sometimes with intestinal or vaginal atresia (Gomes 2025) or perineal hamartoma (Chen 2026).
- **Geography:** reported from North America, Europe, China, Mexico and Israel. No population enrichment.

---

## 10. Diagnostics

- **Diagnostic criteria:** "No consensus clinical diagnostic criteria … have been published." Diagnosis requires suggestive findings plus a heterozygous pathogenic or likely pathogenic *PPP1R12A* variant (GeneReviews).
- **Genetic testing:**
  - Exome or genome sequencing, or a multigene DSD, HPE or ciliopathy/brain-malformation panel. *PPP1R12A* is on the Genomics England PanelApp HPE panel: https://panelapp.genomicsengland.co.uk/panels/78/gene/PPP1R12A.
  - Sequence analysis detected 12/12 in Hughes 2020. The yield of deletion/duplication analysis is unknown.
  - Chromosomal microarray detects 12q21 contiguous deletions.
  - Karyotype with SRY FISH or microarray is needed to establish chromosomal sex.
  - RNA or minigene studies can resolve intronic and splice variants (Diao 2023; Pianigiani 2026; Bland 2026).
  - Trio prenatal exome identified *PPP1R12A* variants in fetuses with neural tube defects (Botvinik 2026: diagnostic yield 6/23; *PPP1R12A* in 2 of the 23 fetuses).
- **Laboratory tests:** AMH, inhibin B, LH, FSH and testosterone (including an hCG stimulation test) during minipuberty and at puberty (GeneReviews). Example: Twin A had AMH 0.02 ng/mL, inhibin B 10 pg/mL and post-hCG testosterone below detection (Tian 2025).
- **Imaging:** brain MRI (HPE subtypes, corpus callosum, cortical dysplasia); pelvic and renal ultrasound or MRI (Müllerian remnants, gonads, collecting system); prenatal ultrasound.
- **EEG:** for seizures. Hypersynchronous patterns have been reported (PMID 40448330).
- **Pathology:** gonadal biopsy or gonadectomy may show dysgenetic or streak gonads.
- **Omics diagnostics:** none established beyond RNA or splicing assays.
- **Differential diagnosis** (GeneReviews Table 3):

| Group | Conditions |
|---|---|
| Genitourinary | Androgen insensitivity syndrome (*AR*), ATR-X syndrome (*ATRX*), Denys-Drash syndrome (*WT1*), IMAGe syndrome (*CDKN1C*) |
| Genitourinary plus brain | Smith-Lemli-Opitz syndrome (*DHCR7*), X-linked lissencephaly with ambiguous genitalia (*ARX*), Warburg micro syndrome (*RAB18*) |
| Other | Trisomy 13; pseudotrisomy 13 |
| Additional entities from the literature | Classic HPE genes (*SHH*, *ZIC2*, *SIX3*, *TGIF1*, *GLI2*); PMDS (*AMH*/*AMHR2*); VACTERL association |

- **Screening:** no newborn or carrier screening applies.

---

## 11. Outcome/Prognosis

- **Survival:** no survival data exist. The spectrum runs from lethality in pregnancy (anencephaly; termination at 12 weeks) to survival into adulthood (a 45-year-old 46,XY female in Hughes 2020).
- **Prognosis by severity:** prognosis depends mainly on brain malformation severity. Severe HPE is associated with significant ID, seizures and feeding difficulties (GeneReviews). Individuals without brain involvement may have normal intelligence.
- **Morbidity:** DSD-related infertility, a possible gonadal tumor risk in dysgenetic gonads (by analogy, not documented), surgical burden (genitoplasty, atresia repair, PSARP), visual and hearing impairment, and scoliosis.
- **Prognostic biomarkers:** none.

---

## 12. Treatment

No disease-specific or disease-modifying therapy exists. GeneReviews states "There may not be clinical trials for this disorder."

**Supportive and multidisciplinary management** (GeneReviews Tables 4–6), with suggested NCIT terms:
- **DSD team care:** endocrinology, urology/gynecology and psychology (NCIT: Multidisciplinary Care).
- **Gonadectomy** for dysgenetic gonads (NCIT C15302-type "Orchiectomy"/"Gonadectomy").
- **Sex hormone replacement** at puberty (NCIT: Hormone Replacement Therapy; CHEBI:17347 testosterone, CHEBI:16469 estradiol).
- **Surgery:**
  - Hypospadias repair, orchidopexy and hernia repair (Twin B).
  - Vaginoplasty and urethroplasty (Twin A, at 30 months).
  - Jejunal atresia repair and stoma; posterior sagittal anorectoplasty for anorectal malformation (Wehrli/Harris 2023).
  - TEF repair.
- **Seizures:** standard antiseizure medication; none has been shown specifically effective.
- **Growth hormone** for documented GH deficiency (Saul 2026; CHEBI somatotropin).
- **Feeding therapy** and gastrostomy when needed.
- **Developmental:** early intervention, physical, occupational and speech therapy, and an IEP.
- **Sensory:** ophthalmology and audiology care; hearing aids or cochlear evaluation where relevant (Pianigiani 2026).
- **Orthopedics:** for kyphoscoliosis.

**Pharmacogenomics, gene, cell or RNA therapies:** none. The zebrafish rescue with blebbistatin, a myosin II inhibitor (PMID 20147380), and the *myh11a* knockdown rescue (PMID 41805950) are preclinical observations only.

**Surveillance:** growth and feeding at each visit; developmental and neurologic monitoring; puberty and gender identity from late childhood; spine until growth ends; eyes and hearing yearly.

---

## 13. Prevention

- **Primary prevention:** not applicable. Most cases are de novo.
- **Genetic counseling:**
  - Recurrence risk for siblings is about 1% when parents test negative, and 50% for offspring of an affected individual.
  - Prenatal or preimplantation testing may be considered (GeneReviews).
  - Prenatal exome is useful when ultrasound shows HPE, neural tube defects, bowel dilatation or ambiguous genitalia.
- **Tertiary prevention:**
  - Early hormonal evaluation during minipuberty.
  - Timely management of gonadal dysgenesis.
  - Surgical correction of atresias.
  - Hearing and vision screening.
  - Scoliosis surveillance.
- No vaccines, behavioral, public-health or prophylactic measures apply.

---

## 14. Other Species / Natural Disease

- No naturally occurring animal disease due to *PPP1R12A* orthologs has been identified; I did not find an OMIA entry.
- **Orthologs:** mouse *Ppp1r12a*, zebrafish *mypt1* (*ppp1r12a*), *Drosophila* DMYPT/*Mbs*, *C. elegans* *mel-11* (Hughes 2020). NCBI Gene IDs were not retrieved.
- **Conservation:** MP-dependent control of embryonic morphogenesis is deeply conserved.
  - DMYPT is required for dorsal closure in *Drosophila*.
  - MEL-11 is required for embryonic elongation in *C. elegans*.
  - Mypt1 is required for convergent extension, kidney and liver formation, and brain ventricle morphogenesis in zebrafish.
- **Zoonotic potential:** not applicable.

---

## 15. Model Organisms

| Model | Phenotype | Reference |
|---|---|---|
| Mouse *Ppp1r12a* targeted null (*Ppp1r12a<sup>tm1Mito</sup>*, MGI:3586994) | Homozygous embryos die before E7.5; heterozygotes show no distinct phenotype and normal MYPT1 expression | Okamoto R et al., *Transgenic Res* 2005;14:337–340, doi:10.1007/s11248-005-3453-3 (PMID not retrieved); MGI https://www.informatics.jax.org/allele/MGI:3586994 |
| Zebrafish *mypt1* mutant | Small brain ventricle and abnormal rhombomere morphology from myosin overactivity. Rescued by blebbistatin (79% of mutants, n = 33/42); "A mutation in the myosin phosphatase regulator mypt1 results in a small ventricle" | Gutzman & Sive, *Development* 2010;137:795–804, PMID 20147380 |
| Zebrafish *mypt1* mutant | Disrupted mesoderm and endoderm cell movement mispositions Bmp2a-producing cells, giving a liverless phenotype (abstract summary) | Huang H et al., *Development* 2008, PMID 18776143 |
| Zebrafish morphants (cited by Hughes) | Gastrulation and prechordal plate migration defects, cyclopia | Cited in PMID 31883643 |
| Intestinal atresia genetic model (zebrafish nomenclature, *myh11a*) | "Mutant embryos exhibited ectopic accumulation of F-actin and phosphorylated myosin regulatory light chain (Mrlc)"; rescued by *myh11a* inhibition | Kobayashi D et al., *Dis Model Mech* 2026, PMID 41805950 |
| Mouse/human embryo expression | *Ppp1r12a* in prosencephalic neural-fold head mesenchyme (GD 8.25); protein in genital tubercle, urethra and bladder epithelium (GD 13), and in human week-10 urogenital tissues | Hughes 2020 |
| *Drosophila* DMYPT; *C. elegans* *mel-11* | Dorsal closure and embryonic elongation defects | Cited in Hughes 2020 |
| Cellular | HEK-type overexpression co-IP: p.Arg845Ter loses PPP1CB binding; minigene splicing assays | Tong 2024 (PMID 39334371); Diao 2023 (PMID 37272772) |

**Limitations and gaps:**
- The mouse null is early-lethal, and mouse heterozygotes are phenotypically normal, so neither reproduces the human haploinsufficient phenotype.
- There are no conditional (forebrain-, genital tubercle- or gonad-specific) knockouts, and no iPSC or organoid models.
- Zebrafish homozygous mutants model hyper-contractility but not dosage sensitivity.
- **Resources:** MGI, ZFIN (ZDB-PUB-100223-7), IMPC.

---

## Key references (PMIDs)

**Case reports and series**
- 31883643: Hughes 2020, *AJHG*, founding cohort
- 36331510: Picard 2022, *Hum Reprod*, PMDS; "Five patients out of 24 (21%) harbored deleterious truncation mutations of PP1R12A"
- 37272772: Diao 2023, splice variant c.2666+3A>G
- 39334371: Tong 2024, nonsense variant with infantile epilepsy
- 39257322: Contreras-Capetillo 2025, expanded sex-reversal phenotype
- 40770999: Gomes 2025, intestinal atresia; recurrent c.3092A>T
- 40800196: Tian 2025, discordant monozygotic twins
- 40448330: Pandya 2025, EEG in holoprosencephaly
- 41626296: Saul 2026, jejunal atresia and GH deficiency
- 42178607: Bland 2026, intronic variant; 22 individuals reviewed
- 42650049: Pianigiani 2026, hearing loss and inner-ear malformation
- 42846858: Voide 2026, minipuberty hormone profile in PMDS
- 43001012: Horn 2026, VACTERL overlap
- 42165277: Chen 2026, fetus with perineal hamartoma
- 41714291: Botvinik 2026, prenatal exome in neural tube defects
- Wehrli/Harris, *J Pediatr Surg Case Rep* 2023, anorectal malformation with a stop-loss variant (PMID not retrieved)

**Clinical review**
- 34499436: GeneReviews (Alkhunaizi & Chitayat, rev. 2024)

**Mechanism and models**
- 30076859: Kiss 2019, myosin phosphatase review
- 20147380: Gutzman & Sive 2010, zebrafish brain ventricle
- 18776143: Huang 2008, zebrafish liver
- 41805950: Kobayashi 2026, intestinal atresia model

**Online sources:** GeneReviews https://www.ncbi.nlm.nih.gov/books/NBK573670/ · Hughes 2020 https://pmc.ncbi.nlm.nih.gov/articles/PMC7042489 · KEGG https://www.kegg.jp/entry/H02523 · Tian 2025 https://tp.amegroups.org/article/view/140867/html · PanelApp https://panelapp.genomicsengland.co.uk/panels/78/gene/PPP1R12A · MGI https://www.informatics.jax.org/allele/MGI:3586994 · Zebrafish model https://pmc.ncbi.nlm.nih.gov/articles/PMC2827689

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 25 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 25 |
| On topic | 13 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 93 |
| Resolved | 91 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 4 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0032934` (2 mentions) - the report calls it "MONDO"; MONDO calls it **genitourinary and/or brain malformation syndrome**
- `HP:0001250` (1 mention) - the report calls it "Rare; neonatal seizures (Tong 2024, PMID 39334371); hypersynchronous EEG in MIHV-HPE (Pandya 2025, PMID 40448330)"; HP calls it **Seizure**
- `HP:0001643` (1 mention) - the report calls it "Rare (GeneReviews; Horn 2026)"; HP calls it **Patent ductus arteriosus**
- `HP:0000407` (1 mention) - the report calls it "1 case (Pianigiani 2026, PMID 42650049)"; HP calls it **Sensorineural hearing impairment**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0000057` (obsolete Clitoromegaly) (1 mention) - replaced by `HP:0008665`

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`.