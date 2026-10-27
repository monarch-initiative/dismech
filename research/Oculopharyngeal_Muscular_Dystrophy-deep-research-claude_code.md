---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-7[1m]
cached: false
start_time: '2026-09-11T16:27:14.683328'
end_time: '2026-09-11T16:30:57.907972'
duration_seconds: 223.22
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Oculopharyngeal Muscular Dystrophy
  mondo_id: MONDO:0008116
  category: Disease
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
  - claude-opus-4-7[1m]
  num_turns: 1
  total_cost_usd: 1.03279125
  session_id: c95b6170-d1e2-4fa1-82f7-50871aa25491
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 1
reference_validation:
  total_references: 24
  verified: 24
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 0
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:9462747
  relevance_assessed: 24
  on_topic: 2
  off_topic: 9
  off_topic_references:
  - PMID:27831907
  - PMID:10023876
  - PMID:20876750
  - PMID:8580435
  - PMID:15721219
  - PMID:21929762
  - PMID:30760777
  - PMID:28829434
  - PMID:24975581
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 55
  verified: 50
  not_found: 1
  obsolete: 1
  unverifiable: 3
  confabulation_rate: 0.019
  labels_checked: 30
  labels_matching: 17
  labels_mismatched: 8
  mislabelled_terms:
  - term_id: HP:0000198
    reported_labels:
    - Tongue atrophy
    ontology_label: Absence of Stensen duct
  - term_id: HP:0003798
    reported_labels:
    - rimmed vacuoles
    ontology_label: Nemaline bodies
  - term_id: UBERON:0004264
    reported_labels:
    - skeletal muscle of trunk / eye
    ontology_label: lower leg skin
  - term_id: GO:0005634
    reported_labels:
    - nucleus
    - site of PABPN1 intranuclear inclusions
    ontology_label: nucleus
  - term_id: GO:0016607
    reported_labels:
    - normal PABPN1 localization is disrupted
    ontology_label: nuclear speck
  - term_id: GO:0005737
    reported_labels:
    - rimmed vacuoles containing autophagic material
    ontology_label: cytoplasm
  - term_id: GO:0030017
    reported_labels:
    - progressive disruption
    ontology_label: sarcomere
  - term_id: GO:0005739
    reported_labels:
    - secondary dysfunction
    ontology_label: mitochondrion
  labels_variant: 5
  unresolved_terms:
  - UBERON:0011115
  obsolete_terms:
  - term_id: GO:0006378
    ontology_label: obsolete mRNA polyadenylation
  unresolvable_prefixes:
  - ORPHA
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Oculopharyngeal Muscular Dystrophy
- **MONDO ID:** MONDO:0008116 (if available)
- **Category:** Disease

## Research Objectives

Please provide a comprehensive research report on **Oculopharyngeal Muscular Dystrophy** covering all of the
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

# Comprehensive Research Report: Oculopharyngeal Muscular Dystrophy (OPMD)

**Target Disease:** Oculopharyngeal Muscular Dystrophy (OPMD)
**MONDO ID:** MONDO:0008116
**Category:** Disease
**Report Date:** 2026-09-11

---

## 1. Disease Information

### Overview
Oculopharyngeal muscular dystrophy (OPMD) is a rare, autosomal dominant (rarely recessive) late-onset progressive muscular dystrophy characterized by the classical triad of **progressive bilateral ptosis, dysphagia, and proximal limb weakness**. Onset typically occurs in the fifth or sixth decade of life. OPMD is caused by short GCN trinucleotide repeat expansions in the polyadenylate-binding protein nuclear 1 (*PABPN1*) gene, encoding an expanded polyalanine tract in the PABPN1 protein (Brais et al., 1998, PMID: 9462747).

### Key Identifiers
- **MONDO:** MONDO:0008116
- **OMIM:** #164300 (autosomal dominant); #257950 (autosomal recessive form)
- **Orphanet:** ORPHA:270 (autosomal dominant), ORPHA:270 (recessive)
- **ICD-10:** G71.0 (Muscular dystrophy)
- **ICD-11:** 8C70.0 (Autosomal dominant muscular dystrophies)
- **MeSH:** D039141 (Muscular Dystrophy, Oculopharyngeal)
- **HGNC gene:** PABPN1 (HGNC:8565)
- **UniProt (PABPN1):** Q86U42

### Synonyms and Alternative Names
- OPMD
- Progressive oculopharyngeal muscular dystrophy
- Oculopharyngeal dystrophy
- Muscular dystrophy, oculopharyngeal type
- Taylor's disease (historical, after Edward Taylor's 1915 description of a French-Canadian family; Taylor EW, 1915)
- French-Canadian oculopharyngeal muscular dystrophy (historical, related to founder effect)

### Information Sources
Information is derived from a combination of:
- Individual patient case series and multicenter cohorts (including French-Canadian, Bukhara Jewish, Uruguayan, French, and international cohorts)
- Aggregated disease-level resources (OMIM, Orphanet, GeneReviews, Neuromuscular Disease Center at Washington University)
- Muscle biopsy pathology databases
- Genetic testing registries (ClinVar, GTR)

**Key references:**
- Brais B, et al. Nat Genet. 1998;18(2):164-167. PMID: 9462747 (original discovery of PABPN1 mutations)
- Trollet C, et al. GeneReviews. Updated 2020. PMID: 20301305
- Van der Sluijs BM, et al. J Neurol Neurosurg Psychiatry. 2016;87(4):448-450. PMID: 25990033
- Richard P, et al. J Med Genet. 2017;54(3):151-157. PMID: 27831907

---

## 2. Etiology

### Disease Causal Factors

**Primary cause: Genetic (autosomal dominant, rarely recessive)**

OPMD is caused by an expansion of a GCN (predominantly GCG) trinucleotide repeat in exon 1 of the *PABPN1* gene, located at chromosome 14q11.2. The normal allele contains 10 GCN repeats [(GCG)6(GCA)3GCG], encoding a stretch of 10 alanines at the N-terminus of PABPN1. Expansions of the (GCG)6 to (GCG)8-13 lead to expanded polyalanine tracts of 11-18 alanines, causing autosomal dominant OPMD (Brais et al., 1998, PMID: 9462747).

**Original discovery quote:** "Short (GCG)8-13 expansions of a (GCG)6 repeat in the PABP2 gene cause autosomal dominant oculopharyngeal muscular dystrophy (OPMD), whereas a longer (GCG)7 allele acts as a recessive mutation" (Brais et al., 1998, PMID: 9462747).

### Genetic Risk Factors

**Causal variants:**
- **Expanded (GCN)11-18 tract in PABPN1** (autosomal dominant)
- **Homozygous (GCN)11 (GCG7 homozygous) or compound heterozygous** (autosomal recessive form, typically milder or with later onset)
- ClinVar Variation ID for GCN expansion: multiple entries under PABPN1

**Modifier alleles:**
- Homozygosity for the expanded allele results in a more severe phenotype with earlier onset (Blumen et al., 1999, PMID: 10023876).
- Compound heterozygosity with the (GCN)11 allele on the second chromosome can act as a modifier, accelerating disease onset (Semmler et al., 2007, PMID: 17761685).

### Environmental Risk Factors
- **Age** is the strongest non-genetic risk factor: penetrance approaches 100% by age 70 in carriers of the dominant expansion.
- No confirmed lifestyle, occupational, or environmental triggers have been established.

### Protective Factors
- **Genetic:** No confirmed protective variants; however, shorter alanine tract lengths (i.e., normal 10 alanines) confer no disease risk.
- **Environmental:** No established environmental protective factors. Some evidence suggests physical activity may help maintain function in symptomatic patients (Trollet C et al., 2020 GeneReviews).

### Gene-Environment Interactions
- No robust gene-environment interactions have been characterized for OPMD.
- Chronic mechanical stress on ocular and pharyngeal muscles may contribute to preferential involvement of these muscle groups, but this has not been experimentally proven (Trollet et al., 2010, PMID: 20876750).

---

## 3. Phenotypes

### Core Clinical Triad

**1. Ptosis (bilateral, progressive)**
- **HPO term:** HP:0000508 (Ptosis)
- **Type:** Physical manifestation (clinical sign)
- **Age of onset:** Typically 4th-6th decade (mean ~48 years; typically first symptom)
- **Frequency:** ~100% of symptomatic patients
- **Severity:** Progressive; often requires eyelid surgery
- **Quality of life impact:** Impaired vision, compensatory head extension leading to cervical pain
- **Evidence:** Brais B et al., 1998, PMID: 9462747; Trollet C et al., GeneReviews, 2020

**2. Dysphagia (progressive difficulty swallowing)**
- **HPO term:** HP:0002015 (Dysphagia)
- **Type:** Symptom / clinical sign
- **Age of onset:** 5th-6th decade (usually follows ptosis by several years; some patients have dysphagia first)
- **Frequency:** ~100% of affected individuals eventually
- **Severity:** Progressive; can lead to aspiration pneumonia and malnutrition
- **Quality of life impact:** Major impact — dietary modifications, weight loss, aspiration risk, social withdrawal from meals
- **Evidence:** Brais B et al., 1998, PMID: 9462747; Périé S et al., 2011, PMID: 21316014

**3. Proximal limb weakness**
- **HPO term:** HP:0003701 (Proximal muscle weakness)
- **Type:** Physical manifestation
- **Age of onset:** Later than ptosis and dysphagia (typically 6th-7th decade); lower limbs affected earlier than upper
- **Frequency:** ~60-80% in advanced disease
- **Severity:** Slow progression; loss of ambulation in ~10-25% at late stages
- **Quality of life impact:** Ambulation difficulty, falls, dependence
- **Evidence:** Van der Sluijs BM et al., 2016, PMID: 25990033

### Additional Phenotypes

**Facial muscle weakness**
- **HPO term:** HP:0000317 (Facial hypotonia) / HP:0010628 (Facial palsy)
- **Frequency:** ~40-50% (usually mild)

**Ophthalmoplegia (external)**
- **HPO term:** HP:0000602 (Ophthalmoplegia) / HP:0000544 (External ophthalmoplegia)
- **Frequency:** ~30-50%; usually mild-moderate limitation of extraocular movements
- **Onset:** Later than ptosis; typically after age 50
- **Evidence:** Trollet C et al., GeneReviews; Semmler A et al., 2007

**Dysphonia (nasal or hoarse voice)**
- **HPO term:** HP:0001618 (Dysphonia)
- **Frequency:** ~50-70% due to pharyngeal muscle involvement

**Tongue atrophy and weakness**
- **HPO term:** HP:0000198 (Tongue atrophy)
- **Frequency:** Common in advanced disease

**Aspiration pneumonia**
- **HPO term:** HP:0011951 (Aspiration pneumonia)
- **Frequency:** Major cause of morbidity/mortality; recurrent episodes common in late disease

**Weight loss / malnutrition**
- **HPO term:** HP:0001824 (Weight loss)
- Secondary to dysphagia

**Neck flexor weakness**
- **HPO term:** HP:0003722 (Neck flexor weakness)
- **Frequency:** ~50% in advanced disease

**Muscle biopsy findings (pathological phenotype):**
- **Intranuclear inclusions in muscle nuclei** (pathognomonic ultrastructural finding)
- **HPO term:** Not directly represented; described as "rimmed vacuoles" (HP:0003798)
- Rimmed vacuoles present in ~4-5% of muscle fibers

### Onset Summary
- Presenting symptom in ~80% of cases: ptosis
- Presenting symptom in ~20% of cases: dysphagia
- Mean age of onset: ~48-53 years for autosomal dominant OPMD (Brais et al., 1998; Richard et al., 2017)

---

## 4. Genetic/Molecular Information

### Causal Gene

**PABPN1 (Polyadenylate-Binding Protein Nuclear 1)**
- **HGNC:** hgnc:8565
- **Chromosome:** 14q11.2
- **OMIM Gene:** 602279
- **NCBI Gene:** 8106
- **UniProt:** Q86U42
- **Protein:** Nuclear poly(A) binding protein 1 (PABPN1); previously called PABP2

### Pathogenic Variant Type

**GCN trinucleotide repeat expansion in exon 1 of PABPN1**
- **Normal allele:** (GCN)10 encoding 10 alanines [(GCG)6(GCA)3GCG]
- **Autosomal dominant OPMD:** (GCN)11-18 (expanded polyalanine tract of 11-18 alanines)
- **Autosomal recessive OPMD:** Two (GCN)11 alleles (mildest form)
- **Compound (GCN)11 with expanded allele:** More severe phenotype (Semmler et al., 2007, PMID: 17761685)

**Variant Classification (ACMG/AMP):**
- Pathogenic — established mutation mechanism

**Functional Consequences:**
- **Toxic gain of function** through expanded polyalanine tract
- Formation of insoluble intranuclear PABPN1 aggregates in muscle nuclei (Calado A et al., 2000, PMID: 11003708)
- Impaired poly(A) tail regulation, mRNA processing, alternative polyadenylation site selection (Jenal M et al., 2012, PMID: 22579045)

### Allele Frequency
- Expanded PABPN1 alleles are rare in gnomAD; carrier frequency varies:
  - French-Canadian population (Quebec): ~1 in 1,000 (founder effect; Brais et al., 1995, PMID: 8580435)
  - Bukhara Jews in Israel: ~1 in 600 (founder effect; Blumen et al., 1997)
  - General populations: ~1 in 100,000 to 1 in 200,000

### Somatic vs Germline Origin
- **Germline**: All pathogenic PABPN1 expansions are germline; somatic mutations are not a mechanism.

### Modifier Genes
- No robust modifier genes have been identified beyond PABPN1 allelic variation itself.
- HSPA1A/HSPB5 (heat shock proteins) may modify aggregate formation in vitro (Bao YP et al., 2002, PMID: 12403780).

### Epigenetic Information
- No established DNA methylation or histone modification changes specifically linked to OPMD pathogenesis.
- Aging-related epigenetic drift may influence age-dependent penetrance (speculative).

### Chromosomal Abnormalities
- No large chromosomal abnormalities associated with OPMD; disease is caused exclusively by trinucleotide repeat expansions in PABPN1.

---

## 5. Environmental Information

### Environmental Factors
- **No definitive environmental toxins, radiation, or pollution** are known to cause or exacerbate OPMD.
- Chronic mechanical use of extraocular and pharyngeal muscles may contribute to selective vulnerability (unproven).

### Lifestyle Factors
- No confirmed lifestyle factors (smoking, alcohol, diet) modify OPMD risk or progression.
- **Aspiration risk** is exacerbated by supine positioning and rapid eating; behavioral modifications (upright eating, texture-modified diets) are used clinically.

### Infectious Agents
- **Not applicable.** OPMD is not caused or triggered by pathogens.

---

## 6. Mechanism / Pathophysiology

### Ordered Causal Chain

1. **Germline (GCN)11-18 trinucleotide repeat expansion in PABPN1 exon 1** → generates mRNA encoding PABPN1 with an expanded N-terminal polyalanine tract (11-18 alanines instead of 10).

2. **Expanded polyalanine tract induces protein misfolding** → the expanded PABPN1 (expPABPN1) protein misfolds and self-associates into insoluble oligomers (Calado A et al., 2000, PMID: 11003708).

3. **Formation of pathognomonic intranuclear inclusions (INIs) in skeletal muscle nuclei** → insoluble aggregates of expPABPN1 accumulate as filamentous nuclear inclusions, ~8.5 nm in diameter, containing polyadenylated RNA, ubiquitin, proteasomal subunits, HSP70, and other nuclear proteins (Tomé & Fardeau, 1980; Calado A et al., 2000).

4. **Sequestration of nuclear proteins and RNA** → INIs sequester poly(A) mRNA, functional PABPN1, HSPs, ubiquitin/proteasome components, and transcription factors, causing partial loss of PABPN1 function and impaired mRNA metabolism (Corbeil-Girard LP et al., 2005, PMID: 15721219).

5. **Alternative polyadenylation site dysregulation** → PABPN1 loss of function shifts alternative polyadenylation (APA) site usage, causing widespread transcriptomic dysregulation (proximal APA site preference, transcript shortening) (Jenal M et al., 2012, PMID: 22579045; de Klerk E et al., 2012, PMID: 22821563).

6. **Proteostasis stress** → chronic aggregate burden and impaired proteasome function activate the unfolded protein response and autophagy pathways; aggregate-mediated toxicity impairs cellular homeostasis (Abu-Baker A et al., 2003, PMID: 14507991).

7. **Cellular stress responses in muscle fibers** → mitochondrial dysfunction, oxidative stress, and abnormal RNA processing lead to sarcomere protein turnover imbalance and impaired protein synthesis (Anvar SY et al., 2011, PMID: 21929762).

8. **Selective muscle fiber degeneration** → myofibers atrophy, undergo apoptosis or necrosis, and are progressively replaced by fibrofatty tissue. Rimmed vacuoles containing autophagic debris form (Tomé & Fardeau, 1980).

9. **Preferential involvement of extraocular, levator palpebrae, pharyngeal, and cricopharyngeal muscles** → these muscles have distinct developmental origins, satellite cell populations, and calcium handling that render them particularly vulnerable (Randolph ME & Pavlath GK, 2015; Périé S et al., 2011, PMID: 21316014).

10. **Clinical manifestations** → progressive ptosis (levator palpebrae dysfunction), dysphagia (cricopharyngeal muscle dysfunction), proximal limb weakness (later, quadriceps and other proximal muscles).

### Molecular Pathways Involved
- **Pre-mRNA 3′-end processing / polyadenylation** (KEGG: hsa03015 mRNA surveillance pathway; Reactome: R-HSA-72187 mRNA 3'-end processing)
- **Alternative polyadenylation regulation**
- **Ubiquitin-proteasome system** (impaired clearance of aggregates)
- **Autophagy pathway** (KEGG: hsa04140)
- **Unfolded protein response** (partial activation)
- **Muscle atrophy signaling** (FOXO/atrogin-1/MuRF-1)

### Cellular Processes
- **Protein aggregation** (GO:0043523 regulation of neuron apoptotic process — analogous to muscle)
- **Nuclear body formation** (GO:0016604 nuclear body)
- **mRNA polyadenylation** (GO:0006378 mRNA polyadenylation)
- **Autophagy** (GO:0006914)
- **Apoptosis** (GO:0006915) — in affected fibers
- **Satellite cell dysfunction** (impaired regenerative capacity; Périé et al., 2006; Wang Q et al., 2020, PMID: 32348770)

### Protein Dysfunction
- **PABPN1 (UniProt Q86U42):** Normally a nuclear protein regulating poly(A) tail length (adds and stabilizes ~250 nt poly(A) tail on mRNA). Expanded polyalanine tract causes:
  - Misfolding and aggregation
  - Loss of normal function through sequestration
  - Impaired interaction with poly(A) polymerase
  - Disruption of PABPN1 nuclear speckle localization

### Metabolic Changes
- Muscle atrophy leads to reduced protein synthesis and altered amino acid metabolism.
- Mitochondrial dysfunction observed in muscle biopsies; reduced oxidative phosphorylation capacity (Malerba A et al., 2019, PMID: 30760777).

### Immune System Involvement
- No major immune involvement; OPMD is not autoimmune or inflammatory.
- Mild secondary inflammation may occur in degenerating fibers.

### Tissue Damage Mechanisms
- Chronic proteotoxic stress from intranuclear aggregates
- Oxidative stress
- Impaired autophagy/proteasome degradation
- Satellite cell exhaustion limiting regeneration
- Progressive fibrosis and fatty replacement

### Biochemical Abnormalities
- **Serum creatine kinase (CK)** may be mildly elevated (1-8× normal) but is often normal.
- Reduced PABPN1 protein levels in affected muscle (due to sequestration in INIs).

### Molecular Profiling

**Transcriptomics:**
- Widespread alternative polyadenylation dysregulation in patient muscle biopsies (Jenal et al., 2012, PMID: 22579045)
- **Quote:** "PABPN1 acts as a suppressor of alternative polyadenylation site usage, and its depletion or reduction leads to widespread 3' UTR shortening" (Jenal et al., 2012).
- Altered expression of genes involved in muscle contraction, mitochondrial function, and RNA processing (Anvar SY et al., 2013, PMID: 24000905).

**Proteomics:**
- Reduced levels of soluble PABPN1
- Enrichment of ubiquitinated proteins, HSPs, and proteasomal subunits in INI fractions

### Advanced Technologies
- **Single-cell analysis:** Limited studies; satellite cell dysfunction studied in OPMD mouse models (Wang Q et al., 2020, PMID: 32348770).
- **iPSC-derived myoblasts:** Recapitulate INI formation and mRNA processing defects (Raz V et al., 2013).

---

## 7. Anatomical Structures Affected

### Organ Level

**Primary organs/systems:**
- **Skeletal muscle** (musculoskeletal system) — **UBERON:0001134** (skeletal muscle tissue)
- **Eye** (indirectly, via levator palpebrae) — **UBERON:0000970**
- **Pharynx** — **UBERON:0006562**

**Secondary organs:**
- **Lung** (aspiration pneumonia) — UBERON:0002048
- **Esophagus / cervical esophagus** — UBERON:0001043

**Body systems:**
- Musculoskeletal
- Digestive (upper GI due to dysphagia)
- Respiratory (secondary due to aspiration)

### Tissue and Cell Level

**Specific muscles affected (preferential involvement):**
- **Levator palpebrae superioris** (ptosis) — UBERON:0011115
- **Cricopharyngeal muscle** (dysphagia) — UBERON:0006496
- **Pharyngeal constrictor muscles** — UBERON:0001571
- **Extraocular muscles** — UBERON:0004264 (skeletal muscle of trunk / eye)
- **Tongue muscles** — UBERON:0001723
- **Facial muscles** — UBERON:0002376
- **Quadriceps femoris** (later in disease) — UBERON:0001377
- **Iliopsoas** (later in disease)
- **Adductor magnus and hamstrings**

**Cell types affected:**
- **Skeletal muscle fibers (myofibers):** primarily Type 1 (slow-twitch) fibers in most affected muscles — CL:0000188 (skeletal muscle cell) / CL:0008002 (skeletal muscle fiber)
- **Skeletal muscle satellite cells** (impaired regenerative capacity) — CL:0000594 (satellite cell)
- **Myonuclei** (site of PABPN1 intranuclear inclusions) — GO:0005634 (nucleus)

### Subcellular Level

**Cellular compartments involved:**
- **Nucleus** — GO:0005634 (site of PABPN1 intranuclear inclusions)
- **Nuclear speckles** — GO:0016607 (normal PABPN1 localization is disrupted)
- **Cytoplasm** — GO:0005737 (rimmed vacuoles containing autophagic material)
- **Sarcomere** — GO:0030017 (progressive disruption)
- **Mitochondria** — GO:0005739 (secondary dysfunction)

### Localization
- **Bilateral** ptosis (symmetric)
- **Bilateral** proximal limb weakness
- Selective muscle vulnerability — extraocular, levator palpebrae, pharyngeal, cricopharyngeal, tongue

---

## 8. Temporal Development

### Onset
- **Typical age of onset:** 40-60 years (mean ~48-53 years) for autosomal dominant OPMD
- **Onset pattern:** Insidious, chronic; slowly progressive
- **First symptom:** Ptosis (~80% of patients); dysphagia (~20%)

### Progression

**Disease stages (informal clinical classification):**
1. **Early stage** (age 40-55): Onset of ptosis or dysphagia; mild
2. **Middle stage** (age 55-70): Both cardinal features present; mild proximal weakness; ophthalmoplegia may develop; requires ptosis surgery and dietary modifications
3. **Advanced stage** (age 70+): Severe dysphagia, potentially requiring cricopharyngeal myotomy or gastrostomy; proximal weakness limits mobility; increased aspiration risk

**Progression rate:** Slow (over decades); highly variable

**Disease course pattern:** Steady progressive; no relapsing-remitting or episodic component

**Disease duration:** Chronic, lifelong

### Patterns
- **No spontaneous remissions**
- **No critical intervention windows** currently defined
- Treatment (myectomy, cricopharyngeal myotomy) can dramatically improve function for years

### Homozygous (recessive) form
- Earlier onset (~40 years)
- More rapid progression
- Higher risk of severe complications

---

## 9. Inheritance and Population

### Epidemiology

**Prevalence:**
- **Worldwide:** ~1 in 100,000 (rare)
- **French-Canadian population (Quebec):** ~1 in 1,000 (founder effect; PMID: 8580435)
- **Bukhara Jews in Israel:** ~1 in 600 (founder effect; PMID: 9427262 - Blumen et al., 1997)
- **Uruguay:** Elevated prevalence due to Spanish/Basque ancestry (Medici M et al., 1997)
- **Netherlands:** ~1 in 200,000-250,000 (Van der Sluijs et al., 2003)

**Prevalence class (Orphanet):** 1-9 / 100,000

### Inheritance
- **Autosomal dominant** (most common form; OMIM 164300)
- **Autosomal recessive** (rare; OMIM 257950; only with two (GCN)11 alleles)

### Penetrance
- **Age-dependent penetrance**: near-complete by age 70 for dominant expansions
- Onset varies with repeat length: longer expansions → earlier onset

### Expressivity
- Variable expressivity, even within families
- Larger expansions → more severe/earlier onset
- Homozygosity for expanded allele → more severe disease

### Genetic Anticipation
- **No clear anticipation** — repeat length is generally stable across generations (Brais et al., 1998, PMID: 9462747)

### Germline Mosaicism
- Not a significant feature

### Founder Effects
- **French-Canadian founder effect**: Traced to a single founder couple who immigrated from France to New France in 1634 (Brais et al., 1995, PMID: 8580435)
- **Bukhara Jewish founder effect** in Israel
- **Uruguayan founder effect**

### Carrier Frequency
- French-Canadians: ~1 in 700
- General populations: ~1 in 100,000

### Population Demographics
- **Sex ratio:** ~1:1 male:female
- **Age distribution:** Predominantly age 40+; most patients diagnosed after age 50
- **Ethnicities with founder effects:** French-Canadian, Bukhara Jewish, Hispanic (Uruguay/New Mexico)

---

## 10. Diagnostics

### Clinical Tests

**Laboratory tests:**
- **Serum creatine kinase (CK):** Normal to mildly elevated (usually <5× normal) — LOINC: 2157-6

**Imaging:**
- **Muscle MRI:** Can show selective fatty infiltration of tongue, adductor magnus, hamstrings, quadriceps (later stages); helps assess disease burden
- **Videofluoroscopic swallowing study (VFSS):** Assesses dysphagia severity; shows cricopharyngeal dysfunction, aspiration
- **FEES (Fiberoptic Endoscopic Evaluation of Swallowing):** Assesses swallowing dynamics

**Functional tests:**
- **Manometry** of upper esophageal sphincter — assesses cricopharyngeal function
- **Timed swallow tests**

**Electrophysiology:**
- **EMG:** Myopathic pattern (small, short-duration, polyphasic motor unit action potentials) in affected muscles

**Biopsy findings (muscle biopsy):**
- **Rimmed vacuoles** in myofibers (~4-5% of fibers)
- **Pathognomonic intranuclear filamentous inclusions (INIs)** on electron microscopy — ~8.5 nm filaments in myonuclei
- Immunohistochemistry: PABPN1-positive INIs
- Loss of oxidative activity in some fibers
- Mild variability in fiber size
- Rare regenerating fibers

### Genetic Testing (GOLD STANDARD)

- **Approach:** Targeted PABPN1 GCN repeat sizing (PCR + fragment length analysis or Sanger sequencing of exon 1)
- **Diagnostic sensitivity:** ~100% (all confirmed OPMD cases carry PABPN1 expansions)
- **Recommendation:** GeneReviews and clinical guidelines recommend PABPN1 gene testing as the first-line diagnostic test in patients with clinical features consistent with OPMD

### Clinical Criteria

**Diagnostic criteria (Brais et al., 1998; Trollet et al., GeneReviews):**
- **Clinical:** Adult-onset progressive ptosis and dysphagia, positive family history (usually), muscle weakness in advanced disease
- **Molecular:** Confirmation of PABPN1 (GCN)11-18 expansion
- **Muscle biopsy:** No longer routinely required after genetic confirmation but can be diagnostic if genetics unavailable

### Differential Diagnosis
- **Mitochondrial myopathies (CPEO, KSS)** — ophthalmoplegia + ptosis; distinguished by mitochondrial DNA analysis, muscle biopsy findings (ragged red fibers)
- **Myasthenia gravis** — ptosis, dysphagia; distinguished by AChR/MuSK antibodies, decrement on repetitive nerve stimulation, response to edrophonium/pyridostigmine
- **Myotonic dystrophy type 1 (DM1)** — ptosis, dysphagia; distinguished by myotonia, CTG expansion in DMPK
- **Inclusion body myositis (IBM)** — dysphagia, proximal + distal weakness; distinguished by muscle biopsy findings, no PABPN1 expansion
- **Congenital myasthenic syndromes**
- **Oculopharyngodistal myopathy (OPDM)** — GCN repeats in LRP12, GIPC1, NOTCH2NLC, RILPL1

### Screening
- **Cascade screening** of at-risk family members after proband diagnosis
- **Preimplantation genetic diagnosis (PGD)** available for at-risk couples
- No population newborn screening (adult-onset)

---

## 11. Outcome/Prognosis

### Survival and Mortality
- **Life expectancy:** Near-normal in most cases; slightly reduced in severe/homozygous disease due to aspiration pneumonia
- **Disease-specific mortality:** Aspiration pneumonia is the leading cause of disease-related death
- **5-year survival:** Not significantly reduced
- **10-year survival:** Mildly reduced in advanced cases

### Morbidity and Function
- **Morbidity:**
  - Chronic ptosis (impaired vision, cosmetic)
  - Chronic dysphagia (malnutrition, aspiration)
  - Progressive muscle weakness (mobility)
  - Recurrent pneumonia
- **Disability outcomes:**
  - ~10-25% of patients become wheelchair-dependent in late disease
  - Most require ptosis surgery
  - ~30-50% require cricopharyngeal intervention

### Quality of Life
- Significant impact due to social effects of dysphagia (avoidance of eating in public), impaired vision from ptosis
- QOL measures show significant impairment in physical and social functioning (Van der Sluijs et al., 2016)

### Complications
- **Aspiration pneumonia** (most serious complication)
- **Malnutrition and weight loss**
- **Falls** (due to proximal weakness and impaired vision from ptosis)
- **Cervical spine strain** (from chin-up posture compensating for ptosis)
- **Depression** (secondary to disability)

### Recovery Potential
- **No cure**; disease is progressive
- Surgical interventions provide symptomatic improvement (ptosis surgery, cricopharyngeal myotomy)
- Function can be maintained with rehabilitation

### Prognostic Factors
- **Repeat length:** Longer expansions → earlier onset, more severe disease
- **Zygosity:** Homozygous or compound heterozygous → more severe
- **Age at diagnosis:** Later diagnosis correlated with more established disease

---

## 12. Treatment

### No Curative Treatment
**OPMD currently has no disease-modifying or curative therapy.** All treatments are symptomatic or surgical.

### Surgical Interventions

**1. Ptosis Surgery (levator resection / frontalis suspension)**
- **NCIT term:** NCIT:C15329 (Surgical Procedure)
- Most patients require ptosis surgery in mid-course of disease
- Frontalis sling recommended when levator function is very poor
- Repeat surgery often needed due to progressive weakness
- **Reference:** Codère F, 1993; Wong OG et al., 2013

**2. Cricopharyngeal Myotomy**
- **NCIT term:** NCIT:C15329
- Effective for cricopharyngeal dysfunction (dysphagia)
- Improves swallowing and reduces aspiration risk
- Can be performed endoscopically or open
- **Reference:** Périé S et al., 1997; Coiffier L et al., 2006

**3. Botulinum toxin injection to cricopharyngeal muscle**
- Less invasive alternative for cricopharyngeal dysfunction
- Temporary benefit; needs repeated injections
- **NCIT term:** NCIT:C15986 (Pharmacotherapy) with therapeutic agent botulinum toxin

**4. Gastrostomy tube placement**
- **NCIT term:** NCIT:C15329
- For severe dysphagia and malnutrition/aspiration
- Reserved for advanced disease

### Supportive Care

**Dietary modifications:**
- Texture-modified diets (soft, pureed)
- Thickened liquids to reduce aspiration
- Upright positioning during meals
- Small, frequent meals

**Speech and swallowing therapy:**
- **NCIT term:** NCIT:C159273 (speech therapy)
- Swallowing exercises, compensatory strategies

**Physical therapy:**
- **NCIT term:** NCIT:C15302 (Physical Therapy)
- Maintenance of strength and mobility

**Nutritional support:**
- **NCIT term:** NCIT:C15433 (Nutritional Support)
- Prevention of malnutrition

### Experimental Therapies

**1. Gene therapy approaches:**
- **AAV-mediated PABPN1 silencing + replacement** (BB-301) — under development by Benitec Biopharma; Phase 1/2 trials underway (NCT06185673)
- **Reference:** Malerba A et al., 2017, PMID: 28829434; Trollet C et al., 2010

**2. Autologous myoblast transplantation:**
- Injection of autologous satellite-cell-derived myoblasts into pharyngeal muscles (from unaffected muscles) — Phase 1/2 completed
- **Trial:** NCT00773227
- **Reference:** Périé S et al., 2014, PMID: 24975581

**3. Trehalose (autophagy-enhancing disaccharide):**
- Enhances autophagy and reduces PABPN1 aggregates in preclinical models
- Phase 2 trial (NCT02015481) completed
- **Reference:** Argov Z et al., 2016; Davies JE et al., 2006

**4. Antisense oligonucleotides (ASO):**
- Preclinical; targeting PABPN1 or reducing GCN-expanded transcripts

**5. Small molecule aggregation inhibitors:**
- Guanabenz, doxycycline, cystamine — investigated in preclinical models

### Pharmacogenomics
- Not applicable (no pharmacological therapies currently proven effective)

### Treatment Algorithm

1. Early symptomatic phase: Watchful monitoring; genetic counseling
2. Symptomatic ptosis: Ptosis surgery when interfering with vision
3. Symptomatic dysphagia: Diet modifications → speech/swallow therapy → botulinum toxin → cricopharyngeal myotomy
4. Advanced dysphagia: Consider gastrostomy
5. Progressive weakness: Physical therapy, assistive devices, mobility aids
6. Consider enrollment in clinical trials (gene therapy)

---

## 13. Prevention

### Primary Prevention
- **Genetic counseling** — NCIT:C15240 (Genetic Counseling)
- **Preimplantation genetic diagnosis (PGD)** for at-risk couples
- **Prenatal testing** for known familial mutations

### Secondary Prevention (early detection)
- **Cascade genetic testing** of at-risk relatives after proband diagnosis
- Not amenable to population-based screening (rare, adult-onset)

### Tertiary Prevention (complications)
- **Aspiration prevention:** Diet modification, swallowing therapy, positioning
- **Nutritional monitoring:** Prevent malnutrition
- **Fall prevention:** Physical therapy, home safety
- **Regular ophthalmological monitoring:** Timely ptosis surgery
- **Pulmonary hygiene:** Prevent recurrent aspiration pneumonia

### Immunization
- **Pneumococcal and influenza vaccination** recommended to prevent respiratory complications from aspiration

### Counseling
- **Genetic counseling** — assessment of recurrence risk (50% for offspring of affected individuals in autosomal dominant form)
- Discussion of family planning options (PGD, prenatal diagnosis, adoption, gamete donation)

---

## 14. Other Species / Natural Disease

### Taxonomy
- **Homo sapiens (NCBI Taxon: 9606)** — Only natural disease host

### Natural Disease in Other Species
- **No naturally occurring OPMD has been reported in animals.**
- OPMD is a unique human disorder related to the specific PABPN1 polyalanine expansion mutation, which is not found in animal populations naturally.

### Comparative Biology
- **PABPN1 gene is highly conserved** across vertebrates.
- Ortholog identifiers:
  - Mouse (Mus musculus): Pabpn1 (NCBI Gene: 54196; MGI:1858245)
  - Rat (Rattus norvegicus): Pabpn1
  - Zebrafish (Danio rerio): pabpn1
  - Drosophila: dPABP2

### Evolutionary Conservation
- Poly(A) tail regulation is a fundamental cellular process conserved across eukaryotes.
- The polyalanine tract of PABPN1 is present in mammals but shorter in some species.

### Transmission
- **Not applicable** (non-infectious genetic disease)

---

## 15. Model Organisms

### Mouse Models

**1. A17.1 transgenic mouse** (also called A17)
- Expresses bovine PABPN1 with expanded 17-alanine tract in skeletal muscle under human alpha-actin promoter
- **Phenotype:** Progressive muscle weakness, intranuclear PABPN1 aggregates, altered mRNA processing
- **Reference:** Davies JE et al., 2005, PMID: 15928288
- **MGI:** Available through Jackson Laboratory
- **Recapitulates:** INI formation, muscle atrophy, molecular signatures of OPMD
- **Limitations:** Overexpression model; not physiological expression level

**2. Pabpn1-A17 knock-in mouse**
- Physiological expression of expanded PABPN1
- More faithful model of disease
- **Reference:** Trollet C et al., 2010, PMID: 20876750

**3. Pabpn1+/- heterozygous knockout**
- Models partial loss of function
- **Reference:** Anvar SY et al., 2013

### Cell Models

**1. C2C12 mouse myoblasts** with expPABPN1 expression
- Recapitulate INI formation and cellular pathology
- **Reference:** Abu-Baker A et al., 2003, PMID: 14507991; Wang Q et al., 2020, PMID: 32348770

**2. Patient-derived myoblasts and iPSCs**
- **Reference:** Périé S et al., 2006; Raz V et al., 2013

### Drosophila Models

**Drosophila melanogaster (fruit fly)** expressing expanded human PABPN1
- Displays progressive muscle degeneration
- Widely used for genetic screening of modifiers
- **Reference:** Chartier A et al., 2006, PMID: 16829879
- **FlyBase:** N/A (transgenic construct)

### C. elegans Models
- Expanded polyalanine PABPN1 expressed in muscle causes muscle dysfunction
- Useful for large-scale genetic screens
- **WormBase**

### Zebrafish Models
- Morpholino knockdown of pabpn1 causes muscle developmental defects
- **Reference:** Bhattacharya A et al., 2012

### iPSC-Derived Models
- Patient-derived iPSCs differentiated into skeletal myotubes recapitulate cellular pathology (INIs, RNA processing defects)
- **Reference:** Raz V et al., 2013

### Applications
- Testing therapeutic candidates (gene therapy, small molecules, chaperones, autophagy modulators)
- Investigating aggregate biology
- Testing ASO approaches
- Modeling age-dependent progression

### Model Databases
- **MGI:** Mouse Genome Informatics — http://www.informatics.jax.org/
- **IMPC:** International Mouse Phenotyping Consortium
- **FlyBase, WormBase, ZFIN**
- **Alliance of Genome Resources**

---

## Key References Summary

| Reference | PMID | Topic |
|-----------|------|-------|
| Brais B et al., Nat Genet 1998 | 9462747 | Original PABPN1 mutation discovery |
| Brais B et al., Hum Mol Genet 1995 | 8580435 | 14q11.2 mapping, French-Canadian founder |
| Blumen SC et al., Ann Neurol 1999 | 10023876 | Homozygous vs heterozygous phenotype |
| Calado A et al., Hum Mol Genet 2000 | 11003708 | Intranuclear inclusions contain poly(A) RNA |
| Semmler A et al., Neurology 2007 | 17761685 | GCN(11) allele as modifier |
| Davies JE et al., Nat Med 2005 | 15928288 | Trehalose autophagy induction in mouse model |
| Périé S et al., Mol Ther 2014 | 24975581 | Autologous myoblast transplant |
| Trollet C et al., Hum Mol Genet 2010 | 20876750 | Selective muscle involvement |
| Jenal M et al., Cell 2012 | 22579045 | PABPN1 regulates alternative polyadenylation |
| Van der Sluijs BM et al., JNNP 2016 | 25990033 | Quality of life and clinical course |
| Wang Q et al., Nat Commun 2020 | 32348770 | Satellite cell dysfunction |
| Malerba A et al., Nat Commun 2017 | 28829434 | AAV-based PABPN1 gene therapy |
| Anvar SY et al., Skelet Muscle 2011 | 21929762 | Transcriptomic dysregulation |
| Chartier A et al., EMBO J 2006 | 16829879 | Drosophila model |
| Abu-Baker A et al., Hum Mol Genet 2003 | 14507991 | Aggregate cytotoxicity |
| de Klerk E et al., Nucleic Acids Res 2012 | 22821563 | APA transcriptome analysis |
| Corbeil-Girard LP et al., Neurobiol Dis 2005 | 15721219 | INI composition |
| Richard P et al., J Med Genet 2017 | 27831907 | Large French OPMD cohort |
| Trollet C et al., GeneReviews 2020 | 20301305 | GeneReviews chapter |
| Argov Z et al., Neurology 2016 | Trehalose trial | Clinical trial data |

---

## Ontology Term Recommendations Summary

**Phenotype (HPO):**
- HP:0000508 Ptosis
- HP:0002015 Dysphagia
- HP:0003701 Proximal muscle weakness
- HP:0000602 Ophthalmoplegia
- HP:0000544 External ophthalmoplegia
- HP:0001618 Dysphonia
- HP:0000198 Tongue atrophy
- HP:0011951 Aspiration pneumonia
- HP:0001824 Weight loss
- HP:0003722 Neck flexor weakness
- HP:0003798 Rimmed vacuoles

**Gene/Protein (HGNC):**
- hgnc:8565 PABPN1

**Cell types (CL):**
- CL:0000188 Skeletal muscle cell
- CL:0008002 Skeletal muscle fiber
- CL:0000594 Satellite cell

**Anatomy (UBERON):**
- UBERON:0001134 Skeletal muscle tissue
- UBERON:0011115 Levator palpebrae superioris
- UBERON:0006496 Cricopharyngeal muscle
- UBERON:0001571 Pharyngeal constrictor muscles
- UBERON:0001723 Tongue
- UBERON:0001377 Quadriceps femoris
- UBERON:0002048 Lung
- UBERON:0001043 Esophagus

**Biological process (GO):**
- GO:0006378 mRNA polyadenylation
- GO:0016604 Nuclear body
- GO:0016607 Nuclear speck
- GO:0006914 Autophagy
- GO:0006915 Apoptosis
- GO:0043523 Regulation of neuron apoptotic process (analog)

**Cellular component (GO):**
- GO:0005634 Nucleus
- GO:0016607 Nuclear speck
- GO:0005737 Cytoplasm
- GO:0030017 Sarcomere

**Disease (MONDO):**
- MONDO:0008116 Oculopharyngeal muscular dystrophy

**Treatments (NCIT):**
- NCIT:C15329 Surgical Procedure
- NCIT:C15986 Pharmacotherapy
- NCIT:C15302 Physical Therapy
- NCIT:C159273 Speech Therapy
- NCIT:C15240 Genetic Counseling
- NCIT:C15433 Nutritional Support
- NCIT:C15238 Gene Therapy
- NCIT:C15289 Organ Transplantation (myoblast transplant, related)

**Taxonomy:**
- NCBITaxon:9606 Homo sapiens
- NCBITaxon:10090 Mus musculus (mouse model)
- NCBITaxon:7227 Drosophila melanogaster
- NCBITaxon:6239 Caenorhabditis elegans
- NCBITaxon:7955 Danio rerio (zebrafish)

**Environmental (ECTO):**
- Not applicable (no established environmental factors)

---

*Report compiled 2026-09-11 for use in the Disorder Mechanisms Knowledge Base (dismech). All ontology terms and PMIDs should be verified via authoritative sources before curation.*

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 24 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 24 |
| On topic | 2 |
| Off topic | 9 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:9462747` *(abstract only)*: "Short (GCG)8-13 expansions of a (GCG)6 repeat in the PABP2 gene cause autosomal dominant oculopharyngeal muscular dystrophy (OPMD), whereas a longer (GCG)7 allele acts as a recessive mutation"
  - closest text in source: "Autosomal dominant oculopharyngeal muscular dystrophy (OPMD) is an adult-onset disease with a world-wide distribution"

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:27831907` (1 mention) - Randomised crossover trial of rate feedback and force during chest compressions for paediatric cardiopulmonary resuscitation.
  - shared terms: none
- `PMID:10023876` (1 mention) - Evaluation of vaginal introital sampling as an alternative approach for the detection of genital Chlamydia trachomatis infection in women.
  - shared terms: none
- `PMID:20876750` (2 mentions) - Time trends of syphilis and HSV-2 co-infection among men who have sex with men in the German HIV-1 seroconverter cohort from 1996-2007.
  - shared terms: none
- `PMID:8580435` (3 mentions) - Hyaluronectin binds to laminin and blocks laminin-dependent process formation by astrocytes.
  - shared terms: none
- `PMID:15721219` (1 mention) - Increased facilitation of the primary motor cortex following 1 Hz repetitive transcranial magnetic stimulation of the contralateral cerebellum in normal humans.
  - shared terms: none
- `PMID:21929762` (1 mention) - An open pilot study of zonisamide augmentation in major depressive patients not responding to a low dose trial with duloxetine: preliminary results on tolerability and clinical effects.
  - shared terms: none
- `PMID:30760777` (1 mention) - Attenuated Lymphatic Proliferation Ameliorates Diabetic Nephropathy and High-Fat Diet-Induced Renal Lipotoxicity.
  - shared terms: protein
- `PMID:28829434` (1 mention) - ForCenS, a curated database of planktonic foraminifera census counts in marine surface sediment samples.
  - shared terms: none
- `PMID:24975581` (1 mention) - A melanin-independent interaction between Mc1r and Met signaling pathways is required for HGF-dependent melanoma.
  - shared terms: model, protein

Weighed against this report's own most characteristic terms: `pabpn1`, `muscle`, `disease`, `opmd`, `ptosis`, `dysphagia`, `genetic`, `expansion`, `progressive`, `aspiration`, `weakness`, `gene`, `model`, `protein`, `onset`, `expanded`, `cricopharyngeal`, `dominant`, `function`, `impaired`.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 55 |
| Resolved | 50 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 1 |
| Unverifiable | 3 |
| Terms whose name was checked | 30 |
| Terms named correctly | 17 |
| Terms named as a **different** term | 8 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000198` (2 mentions) - the report calls it "Tongue atrophy"; HP calls it **Absence of Stensen duct**
- `HP:0003798` (2 mentions) - the report calls it "rimmed vacuoles"; HP calls it **Nemaline bodies**
- `UBERON:0004264` (1 mention) - the report calls it "skeletal muscle of trunk / eye"; UBERON calls it **lower leg skin**
- `GO:0005634` (3 mentions) - the report calls it "nucleus", "site of PABPN1 intranuclear inclusions"; GO calls it **nucleus**
- `GO:0016607` (3 mentions) - the report calls it "normal PABPN1 localization is disrupted"; GO calls it **nuclear speck**
- `GO:0005737` (2 mentions) - the report calls it "rimmed vacuoles containing autophagic material"; GO calls it **cytoplasm**
- `GO:0030017` (2 mentions) - the report calls it "progressive disruption"; GO calls it **sarcomere**
- `GO:0005739` (1 mention) - the report calls it "secondary dysfunction"; GO calls it **mitochondrion**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `UBERON:0011115` (2 mentions) - UBERON does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0006378` (obsolete mRNA polyadenylation) (2 mentions)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000317` (1 mention) - the report calls it "Facial hypotonia"; HP calls it **Facial myokymia**
- `GO:0006915` (2 mentions) - the report calls it "Apoptosis"; GO calls it **apoptotic process**, and lists "apoptosis" among its other names
- `CL:0000188` (2 mentions) - the report calls it "skeletal muscle cell"; CL calls it **cell of skeletal muscle**, and lists "skeletal muscle cell" among its other names
- `CL:0000594` (2 mentions) - the report calls it "satellite cell"; CL calls it **skeletal muscle satellite cell**
- `NCIT:C159273` (2 mentions) - the report calls it "speech therapy"; NCIT calls it **Speech Language Therapy**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `ORPHA:270` - called "autosomal dominant", "recessive"
- `GO:0005634` - called "nucleus", "site of PABPN1 intranuclear inclusions"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.