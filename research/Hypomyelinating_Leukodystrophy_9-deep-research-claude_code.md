---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-28T01:28:11.066770'
end_time: '2026-10-28T01:33:01.675410'
duration_seconds: 290.61
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Hypomyelinating Leukodystrophy 9
  mondo_id: MONDO:0014506
  category: Mendelian
  causal_genes: RARS1
  omim_id: OMIM:616140
  synonyms: HLD9; RARS leukodystrophy; RARS-related autosomal recessive hypomyelinating
    leukodystrophy; hypomyelinating leukodystrophy type 9; leukodystrophy caused by
    mutation in RARS; leukodystrophy, hypomyelinating, type 9
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
  web_search_requests: 6
  num_turns: 37
  total_cost_usd: 2.877539
  session_id: 0bfb328d-96db-5dca-803a-342a247b0264
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  assistant_text_blocks: 4
citation_count: 17
reference_validation:
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 8
  quotes_valid: 8
  relevance_assessed: 13
  on_topic: 10
  validator_version: 0.4.0
term_validation:
  total_terms: 65
  verified: 62
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 6
  labels_matching: 1
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0014506
    reported_labels:
    - MONDO
    ontology_label: leukodystrophy, hypomyelinating, 9
  - term_id: MONDO:0010714
    reported_labels:
    - Parent grouping
    ontology_label: Pelizaeus-Merzbacher spectrum disorder
  labels_variant: 3
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
- **Disease Name:** Hypomyelinating Leukodystrophy 9
- **MONDO ID:** MONDO:0014506 (if available)
- **Causal gene(s):** RARS1
- **OMIM:** OMIM:616140
- **Synonyms:** HLD9; RARS leukodystrophy; RARS-related autosomal recessive hypomyelinating leukodystrophy; hypomyelinating leukodystrophy type 9; leukodystrophy caused by mutation in RARS; leukodystrophy, hypomyelinating, type 9
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Hypomyelinating Leukodystrophy 9** covering all of the
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

Fetching key abstracts.

Cached abstracts exist locally; reading them for exact quotes.

I've confirmed the identifiers and read the main papers from the local cache. Next I'm checking the 2025 mouse preprint and the structural study before writing the report.

# Hypomyelinating Leukodystrophy 9 (HLD9; RARS1-related hypomyelinating leukodystrophy): Research Report

**Target:** MONDO:0014506 "leukodystrophy, hypomyelinating, 9" · OMIM #616140 · **Causal gene: *RARS1*** (HGNC:9870, previously *RARS*, 5q34, OMIM *107820, UniProt P54136, Entrez 5917, Ensembl ENSG00000113643)

HLD9 is caused by biallelic variants in ***RARS1***, which encodes the cytoplasmic arginyl-tRNA synthetase (ArgRS). It should not be confused with ***RARS2***, which encodes the mitochondrial enzyme and causes pontocerebellar hypoplasia type 6. *RARS2* is a differential diagnosis only.

### How this report was sourced

- **Abstracts and quotes.** Exact abstract quotes come from the repository's own `references_cache/` files. Those files were fetched by the project tooling and can be checked with snippet validation.
  - PMIDs 24777941, 28905880, 30791064, 31737794, 33515434 and 33190326 are cached as abstract only.
  - PMIDs 31814314, 37186453 and 38618971 are cached as PMC full text.
- **Ontology terms.** Each CURIE was checked against the committed `cache/*/terms.csv` files, and labels are copied from those files. A few GO terms had no cache row. They are marked **[unverified – look up before binding]**.
- **Not reached.** PubMed and bioRxiv pages could not be fetched directly: PubMed returned a CAPTCHA and bioRxiv returned HTTP 429. Claims about the 2025 mouse preprint therefore come from search-result summaries only and are flagged.

---

## 1. Disease information

**Overview.** HLD9 is an autosomal recessive hypomyelinating leukodystrophy, meaning a permanent shortfall of myelin deposited in the central nervous system (CNS).

- **Classic form.** It resembles Pelizaeus-Merzbacher disease (PMD), with onset in infancy, nystagmus, spasticity, ataxia and developmental delay.
- **Wider range.** It is now known to run from a severe neonatal or early-infantile developmental and epileptic encephalopathy (DEE) with brain atrophy and simplified gyration, to a mild form with independent walking and relatively preserved myelin. One mild case presented in adulthood.

**Identifiers**

| Resource | ID | Label |
|---|---|---|
| MONDO | MONDO:0014506 | leukodystrophy, hypomyelinating, 9 |
| OMIM | 616140 | Leukodystrophy, hypomyelinating, 9; HLD9 |
| Orphanet | ORPHA:438114 | RARS-related autosomal recessive hypomyelinating leukodystrophy (ID confirmed only through secondary sites: MedGen, Qeios, Global Genes) |
| MedGen | 863760 | — |
| Gene | *RARS1*, HGNC:9870, OMIM 107820 | — |
| Parent grouping | MONDO:0010714 | Pelizaeus-Merzbacher spectrum disorder (a relevant "PMD-like" grouping; check MONDO for the actual is_a parent) |

No ICD-10 or ICD-11 code is specific to HLD9. Hereditary CNS demyelinating disease codes such as ICD-10 E75.29 or G37.x are used non-specifically, so check them before mapping. No disease-specific MeSH heading exists; PubMed indexes it under "Hereditary Central Nervous System Demyelinating Diseases" and "Arginine-tRNA Ligase/genetics."

**Synonyms:** HLD9; RARS leukodystrophy; RARS-related autosomal recessive hypomyelinating leukodystrophy; RARS1-related hypomyelinating leukodystrophy; hypomyelinating leukodystrophy type 9; Pelizaeus-Merzbacher-like disease due to RARS1.

**Source type.** All knowledge comes from aggregated case reports and case series, roughly 35 or more published patients by 2024. There are no EHR cohorts and no registries.

---

## 2. Etiology

**Cause.** The disease is purely genetic: biallelic germline loss-of-function or hypomorphic variants in *RARS1*.

> "Biallelic variants in RARS1, encoding the cytoplasmic tRNA synthetase for arginine (ArgRS), cause a hypomyelinating leukodystrophy." — PMID:31814314 (Mendes et al., 2020)

> "Using magnetic resonance imaging (MRI) pattern recognition and whole exome sequencing, we could ascertain compound heterozygous mutations in RARS in 4 patients with hypomyelination." — PMID:24777941 (Wolf et al., 2014; the founding paper)

**Genetic risk factors**
- The only established risk factor is having two pathogenic *RARS1* alleles.
- Consanguinity increases risk. Homozygous cases come from consanguineous Iranian families (PMID:38618971, PMID:30791064).
- No modifier genes or susceptibility loci have been reported.

**Environmental, protective and gene–environment factors**
- None are known.
- One in-vitro observation hints at a substrate-dependence interaction: patient fibroblasts proliferate poorly when arginine is limited, at 30 °C and at 40 °C (PMID:28905880). This is in vitro only and has no clinical correlate. Do not treat it as an established environmental modifier.

---

## 3. Phenotypes

The best quantitative sources are three pooled reviews:
- **Wan et al. 2023** (PMID:37186453): n = 29.
- **Mendes et al. 2020** (PMID:31814314): n = 20.
- **Biglari et al. 2024** (PMID:38618971): n = 33.

| Phenotype | HPO (verified in cache) | Frequency | Notes and evidence |
|---|---|---|---|
| CNS hypomyelination | HP:0003429 CNS hypomyelination | 24/29 (83%); 12/12 in the epilepsy subgroup | MRI hallmark. "T2‑weighted images demonstrated supratentorial white matter hyperintensity with corresponding T1 hypointensity, in keeping with myelin deficit" (PMID:31814314) |
| Delayed myelination (young infants) | HP:0012448 Delayed myelination | common | "even the youngest patients showed deficient myelination" (PMID:31814314) |
| Intellectual disability / developmental delay | HP:0001249; HP:0001263 | 27/29 (93%) | Mendes: 13 of 15 survivors had ID (6 mild–moderate, 7 severe) |
| Motor delay | HP:0001270 Motor delay | 25/29 (86%) | only 8/29 walked without support |
| Language delay / absent speech | HP:0000750; HP:0001344 | 22/29; 17 with absent speech | absent speech in 100% of the epilepsy group vs 46% (p = 0.006) |
| Nystagmus | HP:0000639 Nystagmus | 21/29 (72%); 12/20 (Mendes) | classic sign; transient in the mildest patient |
| Spasticity | HP:0001257 Spasticity | 13/20 (Mendes) | "Clinical features included severe spasticity and nystagmus" (PMID:24777941) |
| Microcephaly | HP:0000252 Microcephaly | 17/29 (59%); 13/13 with epilepsy vs 6/15 without (p = 0.001) | marker of the severe form |
| Seizures / epileptic encephalopathy | HP:0001250; HP:0200134 | 13/29 (45%); 10/20 (Mendes) | onset 1–13 months; drug-resistant in 11/12 (Wan) and 8/10 (Mendes) |
| Infantile/epileptic spasms, hypsarrhythmia | HP:0012469; HP:0011097; HP:0002521 | individual cases | Wan patient 1: spasms at 5 months, hypsarrhythmia, refractory to ACTH and vigabatrin |
| Ataxia | HP:0001251 Ataxia | 12/29; 7/20 | — |
| Dystonia | HP:0001332 Dystonia | 11/29 | also in the Rezaei cases (PMID:30791064) |
| Hypotonia | HP:0001252 Hypotonia | 8/29 | — |
| Feeding difficulties | HP:0011968 Feeding difficulties | 12/29 | severe form |
| Failure to thrive | HP:0001508 Failure to thrive | presenting sign in 1/20 | — |
| Cerebral atrophy | HP:0002059 Cerebral atrophy | 9/17 imaged (Mendes); 11/12 with epilepsy vs 6/14 without (p = 0.014) | tracks with severity |
| Cerebellar atrophy | HP:0001272 Cerebellar atrophy | single cases | Mendes P5 |
| Simplified gyral pattern | HP:0009879 Simplified gyral pattern | rare (Mendes P19; Wan P1) | malformation of cortical development in DEE |
| Dysarthria / pseudobulbar signs | HP:0001260 Dysarthria | some | Orphanet definition; Rezaei "pseudo-bulbar palsy"; Biglari case 1 |
| Tremor | HP:0001337 Tremor | Orphanet ("intentional tremor") | — |
| Developmental regression | HP:0002376 Developmental regression | occasional | Rezaei patient lost head control at 7 months (Mendes Table 1) |
| Ventrolateral thalamic T2 hyperintensity | (no specific HPO term checked) | 1/17 | shared with EPRS1 disease |
| Spinal cord involvement | (no specific HPO term checked; consider HP:0002500 only for the brain) | 1 reported patient | PMID:30791064 |

**Onset.** Biglari: mean 5.8 months (SD 8.1), IQR 0–10 months. Mendes: 18 of 20 presented in the first year, 11 of those under 3 months; two presented after 12 months. Suggested onset terms: HP:0003623 Neonatal onset, HP:0003593 Infantile onset, and rarely HP:0003621 Juvenile onset.

**Severity classes** (Mendes 2020, PMID:31814314):

> "Clinical presentation ranged from severe (onset in the first 3 months, usually with refractory epilepsy and early brain atrophy), to intermediate (onset in the first year with nystagmus and spasticity), and mild (onset around or after 12 months with minimal cognitive impairment and preserved independent walking)."

**Quality of life.** No EQ-5D, SF-36 or other validated QoL data exist. The burden can be inferred from non-ambulation, absent speech, refractory epilepsy and feeding problems.

---

## 4. Genetic and molecular information

**Gene and protein.** *RARS1* encodes a class I aminoacyl-tRNA synthetase that attaches arginine to tRNA^Arg. One transcript produces two isoforms through alternative start codons:
- **Long isoform (~660 aa).** Its 72-residue N-terminal extension (NTE) contains leucine-zipper motifs that anchor ArgRS to AIMP1 and GlnRS (QARS1) inside the multi-tRNA synthetase complex (MSC).
- **Short isoform.** It lacks the NTE and stays free in the cytosol.

> "ArgRS exists in a short and a long isoform, both translated from the same transcript… This isoform is found free in the cytosol, whereas the long isoform is found in a subcomplex together with … AIMP1 and … GlnRS, within a larger multisynthetase complex" — PMID:31814314

Structural work shows how the complex is built: RARS1 LZ1 forms a three-stranded coiled coil with AIMP1 LZ1 and AIMP2, and RARS1 LZ2 pairs with AIMP1 LZ2 (Kim et al., J Mol Biol 2024, PMID:39542129; PDB 8J9S).

**Variant spectrum.** About 25 distinct variants are known. Wan et al. (PMID:37186453) classify them as:
- missense: 13
- start-codon loss: 4
- splice: 4
- frameshift: 3

| Variant (NM_002887) | Type | Recurrence | Phenotype association | Functional data |
|---|---|---|---|---|
| c.5A>G p.(Asp2Gly) | missense in the NTE (long isoform only) | Most common: 7/20 (Mendes), 10/29 (Wan), 11/33 (Biglari) | mild (homozygous) or intermediate; never severe | normal catalytic activity, but reduced translation of the long isoform; an upstream ORF is involved (PMID:33515434) |
| c.5A>T p.(Asp2Val) | missense | 1 (homozygous) | severe DEE | reduced protein stability (PMID:37186453) |
| c.1A>G, c.2T>C, c.2T>A, c.3G>T p.(Met1?) | start loss | ≥4 families; c.2T>C homozygous in Iranian (Bakhtiari) families | severe | only the short isoform is made (Mendes P4: normal fibroblast activity, but long isoform nearly absent) |
| c.1535G>A p.(Arg512Gln); c.1534C>T p.(Arg512Trp) | missense near the active site | 3+ families | always severe | R512Q impairs structure and activity (PMID:33515434) and reduces stability (PMID:37186453) |
| c.1316C>A p.(Ala439Asp) | missense | 1 consanguineous family | severe | — |
| c.1367C>T p.(Ser456Leu) | missense, catalytic domain | 2 families | severe or mild, depending on the second allele | lysosomal aggregation and reduced S6 phosphorylation (PMID:31737794); reduced aminoacylation |
| c.1846_1847del p.(Tyr616Leufs*6) | frameshift (ΔC-terminus), de novo on one allele | 1 | severe | impairs structure and activity (PMID:33515434) |
| c.173T>C p.(Leu58Pro) | missense at the GlnRS interface | 2 families | mild (with D2G) or severe (with L597P) | predicted to disrupt the GlnRS interaction |
| c.1382G>A p.(Arg461His) | missense | 1 | severe (with R512Q) | reduced stability |
| c.96_97del p.(Cys32Trpfs*39); c.67_70del p.(Thr23Leufs*6) | frameshift | several | severe or intermediate | — |
| c.45+1G>T, c.1452+1G>A, c.1625+2T>G, c.1874-9_1874-5del | splice | several | intermediate or severe | — |

Genotype–phenotype rule (PMID:31814314):

> "The most frequent RARS1 variant, c.5A>G, led to mild or intermediate phenotypes, whereas truncating variants and variants affecting amino acids close to the ArgRS active centre led to severe phenotypes."

**Other genetic details**
- **ACMG classification.** Biglari et al. called c.2T>C *pathogenic* (PVS1, PS1, PM2, PP1, PP4). Wan et al. called R461H, R512Q and D2V *VUS* by ACMG but pathogenic by functional assay.
- **ClinVar and ClinGen.** Not checked. No ClinGen gene–disease validity record is in the local cache, so do not record one.
- **Population frequency.** Variants are very rare. c.2T>C is absent from ExAC, 1000 Genomes and Iranome (PMID:38618971). gnomAD frequencies were not retrieved.
- **Origin.** Germline throughout. The mother of the Nafisinia compound-heterozygous patient did not carry the frameshift (a de novo allele), but the result is still germline biallelic.
- **Functional consequence.** Loss of function or hypomorphism. Some missense alleles (S456L) may add toxicity through aggregation; this was proposed but not shown in vivo.
- **Modifier genes, epigenetics, chromosomal abnormalities.** None reported.

---

## 5. Environmental information

There are no known environmental, lifestyle or infectious factors. The arginine-limitation finding in fibroblasts (Section 2) is an in-vitro stress test, not an exposure. This section does not apply.

---

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic *RARS1* variants** (missense, start-loss, frameshift, splice) **lead to** less functional cytoplasmic ArgRS. The route depends on the allele:
   - **1a. Catalytic or near-active-site missense and truncating alleles** (R512Q/W, A439D, ΔC-terminus) **result in** lower aminoacylation activity and/or unstable protein (PMID:33515434; PMID:37186453). ArgRS activity was "significantly reduced in three patients with intermediate and severe phenotypes" (PMID:31814314).
   - **1b. NTE and start-codon alleles** (D2G, Met1 loss) **result in** selective loss of the long, MSC-anchoring isoform, while short-isoform activity can be normal. D2G "acted in a different manner without impairing hArgRS activity. The nucleotide substitution c.5A>G reduced translation of hArgRS mRNA" (PMID:33515434).
   - **1c. Some missense alleles** (S456L) **lead to** protein aggregation and lysosomal mislocalisation (in vitro, PMID:31737794).
2. **Loss of ArgRS, especially the long isoform, leads to** less RARS1 inside the multi-tRNA synthetase complex and destabilisation of the complex. In fibroblasts, RARS protein and the multi-synthetase complex were "significantly reduced by 80 and 90% by western blotting and Blue native-PAGE respectively" (PMID:28905880).
3. **Reduced charging of tRNA^Arg and an impaired MSC lead to** inefficient cytoplasmic protein synthesis under demand, shown as reduced fibroblast proliferation under arginine limitation, "suggestive of inefficiency of protein synthesis in the patient cells" (PMID:28905880). *This is inferred for brain cells and shown only in fibroblasts.*
   - A 2025 bioRxiv preprint (not peer-reviewed; abstract-level only) reports that removing RARS1 from the MSC in HEK293T cells left bulk translation and Arg-codon decoding intact. If confirmed, this argues against step 3 as the sole mechanism and points to a non-canonical, MSC-dependent role (step 3b).
   - **3b. Branch, hypothetical.** Defective ArgRS may also impair supply of Arg-tRNA to arginyl-transferase (ATE1) for the N-degron (N-end rule) protein-degradation pathway, damaging proteostasis. Mendes et al. propose this explicitly as speculation (PMID:31814314).
   - **3c. Branch, in vitro.** S456L aggregates **lead to** lower lysosome-associated mTOR output (S6 phosphorylation) in oligodendroglial FBD-102b cells (PMID:31737794).
4. **Steps 3/3c lead to** failed oligodendrocyte morphological differentiation and myelin formation. Cells carrying S456L "fail to exhibit phenotypes with myelin web-like structures following differentiation in FBD-102b cells" (PMID:31737794; in vitro mouse cell line).
5. **Step 4 results in** a permanent CNS myelin deficit, seen as hypomyelination on MRI (T2 hyperintense, T1 hypo-/isointense white matter) and clinically as nystagmus, spasticity, ataxia and motor delay.
6. **Branch: severe alleles (near-null activity or loss of the long isoform) lead to** disrupted neurodevelopment beyond white matter. This shows as microcephaly, simplified gyral pattern (malformation of cortical development), early cerebral and cerebellar atrophy and refractory infantile epilepsy, i.e. DEE.
   - Mendes et al. note that severe cases "resemble early‑onset grey matter disorders rather than primary leukodystrophies."
   - The preprint's forebrain-conditional mouse with RARS1 excluded from the MSC reportedly develops microcephaly and behavioural deficits (unreviewed).
   - Whether hypomyelination in severe cases is primary (oligodendroglial) or secondary to neuronal loss is unresolved; Mendes et al. pose this as an open question.
7. **Steps 5 and 6 result in** the clinical outcome: ID or global developmental delay, absent speech, non-ambulation and feeding difficulty. In the severe form, death occurs at 21–42 months (5/20 in Mendes).

### Mechanism checklist

- **Molecular pathways and processes.** Arginyl-tRNA aminoacylation, cytoplasmic translation, MSC assembly, mTORC1–S6 signalling (in vitro), and possibly the N-degron/arginylation pathway (hypothetical).
- **Protein dysfunction.** Reduced catalysis (R512Q, ΔC), instability (D2V, R461H, R512Q), loss of the long isoform (D2G, Met1 loss), and aggregation (S456L).
- **Metabolic.** No systemic biochemical marker. Plasma arginine is not reported as abnormal.
- **Immune, epigenetic, omics, single-cell, spatial, CRISPR.** No disease-specific data.
- **Notable comparison.** HLD9 shares a phenotype with other MSC-synthetase leukodystrophies: DARS1 (HLD with brainstem and spinal cord involvement and leg spasticity), EPRS1 (HLD15), and severe QARS1/AIMP1/AIMP2 encephalopathies.

### Suggested GO and CL terms

| Process or cell | Term | Status |
|---|---|---|
| CNS myelination | GO:0022010 central nervous system myelination | verified |
| Myelination | GO:0042552 myelination | verified |
| Oligodendrocyte differentiation | GO:0048709 oligodendrocyte differentiation | verified |
| Cytoplasmic translation | GO:0002181 cytoplasmic translation | verified |
| Translation | GO:0006412 translation | verified |
| TOR signaling (S6 output) | GO:0031929 TOR signaling | verified |
| Cerebral cortex development (DEE/MCD branch) | GO:0021987 cerebral cortex development | verified |
| Arginyl-tRNA aminoacylation | GO:0006420 | **[unverified – look up]** |
| Arginine-tRNA ligase activity (molecular function) | GO:0004814 | **[unverified – look up]** |
| Aminoacyl-tRNA synthetase multienzyme complex (CC) | GO:0017101 | **[unverified – look up]** |
| Cytosol (CC) | GO:0005829 cytosol | verified |
| Oligodendrocyte | CL:0000128 oligodendrocyte | verified |
| Oligodendrocyte precursor cell | CL:0002453 oligodendrocyte precursor cell | verified |
| Neuron (severe branch) | CL:0000540 neuron | verified |
| Chemical: substrate | CHEBI:16467 L-arginine | verified |

---

## 7. Anatomical structures affected

- **Primary.** CNS white matter of the cerebral hemispheres, supratentorial and infratentorial (Orphanet).
  - Terms: UBERON:0002316 white matter; UBERON:0001869 cerebral hemisphere; UBERON:0000955 brain.
- **Secondary.**
  - Cerebral cortex in the severe form (atrophy, simplified gyration): UBERON:0000956 cerebral cortex.
  - Cerebellum (atrophy, one patient): UBERON:0002037 cerebellum.
  - Spinal cord (one patient): UBERON:0002240 spinal cord.
  - Ventrolateral thalamus (one patient).
- **Body systems.** Central nervous system. There is no peripheral nerve or systemic organ involvement.
- **Cells.** Oligodendrocytes and precursors (myelin deficit); neurons (severe form).
- **Subcellular.** Cytosol and the MSC; lysosome for the S456L aggregates (in vitro).
- **Lateralisation.** Bilateral and symmetric.

---

## 8. Temporal development

- **Onset.** Congenital or neonatal to infantile in most patients (mean 5.8 months). Rarely around 2–3 years. In one adult (Mendes P10), transient nystagmus at age 3 was followed by cognitive decline from the 30s and spasticity from the mid-40s.
- **Pattern.** Insidious developmental delay, or early refractory seizures in the severe form.
- **Progression.**
  - Hypomyelination is largely static.
  - Severe cases show early progressive atrophy and death in early childhood.
  - Spasticity may progress, and mild cases can decline slowly in adulthood. Mendes P10 became symptomatic again in mid-adulthood, and one patient became wheelchair-dependent later in life.
  - Regression has occurred in single cases.
- **Course.** Chronic, lifelong; no remission.
- **Critical periods.** The first year (myelination and cortical development) is the presumed window. No intervention trials exist.

---

## 9. Inheritance and population

- **Inheritance.** Autosomal recessive (HP:0000007 Autosomal recessive inheritance). Patients are homozygous or compound heterozygous.
- **Penetrance and expressivity.** Penetrance appears complete in biallelic carriers. Expressivity is highly variable and largely set by allele class.
- **Anticipation and mosaicism.** No anticipation. No germline mosaicism reported.
- **Founder effects.**
  - c.2T>C occurs homozygous in several Iranian families, including Bakhtiari families and two unrelated Tehran patients. This suggests a regional founder allele, but no haplotype study has been done.
  - c.5A>G recurs across European, Australian and Chinese families.
- **Consanguinity.** Present in the homozygous families.
- **Epidemiology.** Unknown and ultra-rare: about 35 patients published worldwide by 2024. Suggested `prevalence_class`: NOT_YET_DOCUMENTED, with measure type CASES_IN_LITERATURE (around 33 reported cases, per PMID:38618971).
- **Carrier frequency.** Not reported.
- **Sex ratio.** About 1:1 (13 F / 15 M of 29; PMID:37186453).
- **Geography.** Netherlands, Australia, USA, Italy, Germany, UK, UAE, Iran, China.
- **Adult cases.** One *RARS1* case was found among 25 adult hypomyelination cases (PMID:33190326).

---

## 10. Diagnostics

- **MRI** is the key test. It shows a hypomyelination pattern: diffuse mild T2 hyperintensity of the supratentorial white matter, with T1 hyperintense, iso- or hypointense signal.
  - In the severe form, add early cerebral and cerebellar atrophy and simplified gyration.
  - Wolf et al. reached the diagnosis by MRI pattern recognition followed by WES (PMID:24777941).
- **EEG** shows hypsarrhythmia in spasms (HP:0002521) and abnormal EEG in DEE.
- **Laboratory.** No specific blood or urine biomarker.
  - Research test: ArgRS aminoacylation activity in fibroblasts, measured by stable-isotope LC-MS/MS with ValRS and GlyRS as controls (PMID:31814314).
  - Western blot for the long versus short isoform.
  - Caveat: normal activity does not exclude disease. Start-loss alleles can show normal activity because the short isoform remains.
- **Genetic testing.**
  - First line: WES/WGS or a leukodystrophy/hypomyelination NGS panel that includes *RARS1*.
  - Confirm segregation with Sanger sequencing.
  - Check whether start-codon (c.1–c.3) and NTE variants are covered, because they are frequent.
  - CMA, karyotype, FISH, mtDNA testing and repeat-expansion testing do not apply.
- **No GeneReviews chapter** for HLD9 was found in the cached Bookshelf index (grep returned no hit; check with `just check-genereviews`).
- **Differential diagnosis.**
  - PMD (*PLP1*; HLD1) and PMLD (*GJC2*; HLD2).
  - POLR3-related leukodystrophy (dental and endocrine signs) and *TUBB4A* H-ABC (basal ganglia atrophy).
  - Other synthetase leukodystrophies: *DARS1* (spinal cord and brainstem), *EPRS1*, *AARS1*, *VARS1*, *QARS1*.
  - *AIMP1/AIMP2*, *HSPD1* (HLD4), *FAM126A* (HLD5).
  - *RARS2* (pontocerebellar hypoplasia).
  - Severe DEE causes with microcephaly.
- **Screening.** No newborn screening. Carrier and cascade testing are possible once familial variants are known.

---

## 11. Outcome and prognosis

- **Mortality.** In the Mendes cohort, 5 of 20 died, all with onset before 3 months, at ages 21–42 months. Intermediate and mild patients survive into adolescence and adulthood (P3 was 26 years old; P10 was older than 50).
- **Function.**
  - Only 8 of 29 walked without support (Wan).
  - Of 15 survivors in Mendes, 6 walked: 2 with support, 4 independently, and 1 later became wheelchair-dependent.
  - Absent speech in 17 of 29.
- **Prognostic factors.**
  - Onset before 3 months, epilepsy, microcephaly, early atrophy, truncating, start-loss or active-site (Arg512) alleles: poor.
  - c.5A>G: mild or intermediate.
  - Epilepsy predicts absent speech and inability to walk (p < 0.01; PMID:37186453).
- **Complications.** Refractory epilepsy, feeding difficulty or failure to thrive, aspiration risk (inferred), and progressive spasticity.
- **QoL instruments.** None used.

---

## 12. Treatment

There is **no disease-modifying therapy and no clinical trial**. A search of ClinicalTrials.gov via the literature found no *RARS1*/HLD9 trials. Care is supportive.

| Intervention | NCIT (verified) | Notes |
|---|---|---|
| Antiseizure medications (vigabatrin, ACTH, polytherapy) | NCIT:C15986 Pharmacotherapy (+ therapeutic_agent for specific drugs) | usually refractory (PMID:37186453); no RARS1-specific efficacy data |
| Physical therapy for spasticity and motor delay | NCIT:C15302 Physical Therapy | standard; no outcome data |
| Occupational therapy | NCIT:C121351 Occupational Therapy | — |
| Speech and language therapy / feeding support | NCIT:C159273 Speech Language Therapy | — |
| Supportive and palliative care | NCIT:C15747 Supportive Care | — |
| Genetic counselling | NCIT:C15240 Genetic Counseling | — |

**Theoretical ideas, none tested in patients**
- Arginine supplementation, suggested by the fibroblast arginine-limitation phenotype. In analogous synthetase disorders (e.g. IARS1, LARS1), cognate amino-acid supplementation has been tried, but no HLD9 data exist.
- mTOR/S6 pathway modulation, suggested by the S456L in-vitro data (PMID:31737794).
- AAV gene replacement, as for other leukodystrophies. Nothing has been reported for *RARS1*.

**Pharmacogenomics.** Not applicable.

---

## 13. Prevention

- **Primary prevention.** Genetic counselling; carrier testing of relatives; prenatal diagnosis or preimplantation genetic testing for families with known variants (25% recurrence risk per pregnancy). This is especially relevant in consanguineous communities with recurrent alleles (Iranian c.2T>C).
- **Secondary prevention.** No screening programme. Early WES in infants with hypomyelination or refractory infantile epilepsy shortens the diagnostic odyssey.
- **Tertiary prevention.** Seizure control, prevention of contractures, nutrition and aspiration management.
- **Vaccines, prophylaxis, public health measures.** Not applicable.

---

## 14. Other species / natural disease

- No naturally occurring *RARS1* disease is recorded in animals. OMIA was not checked directly, so state "not found" rather than "absent."
- Orthologs:
  - Mouse *Rars1* (MGI:1914297; NCBITaxon:10090 Mus musculus)
  - Rat *Rars1* (NCBI Gene 287191)
  - Zebrafish *rars1* (NCBITaxon:7955 Danio rerio)
- ArgRS is conserved from bacteria to humans. The N-terminal MSC-anchoring extension is a vertebrate/metazoan feature, which matters when choosing models.
- Zoonotic transmission: not applicable.

---

## 15. Model organisms

| Model | Type | Findings | Fidelity and limitations | Source |
|---|---|---|---|---|
| Patient fibroblasts (Nafisinia) | IN_VITRO, primary human cells | 80% less RARS, 90% less MSC; reduced proliferation under limited arginine | non-neural; tests translational capacity only | PMID:28905880 |
| Patient fibroblasts (Mendes) | IN_VITRO | reduced ArgRS aminoacylation (P1, P3, P5); long→short isoform switch (P4) | in-vitro activity may not reflect in-vivo MSC-dependent function | PMID:31814314 |
| HEK293T overexpression | IN_VITRO | D2V, R461H, R512Q lower ArgRS levels and speed degradation (cycloheximide chase) | overexpression; non-neural | PMID:37186453 |
| Recombinant hArgRS biochemistry and reporter translation | IN_VITRO | R512Q and ΔC reduce activity and structure; D2G lowers translation through a uORF | cell-free / heterologous | PMID:33515434 |
| FBD-102b mouse oligodendroglial line and COS-7 | IN_VITRO | S456L aggregates in lysosomes, reduces pS6, blocks myelin-web formation | GFP-tagged overexpression on a wild-type background, so it does not model biallelic loss; enzymatic effect not measured | PMID:31737794 |
| Conditional *Rars1* exon-2 floxed mouse (removes most of the NTE leucine zipper and excludes RARS1 from the MSC), forebrain Cre | MODEL_ORGANISM (preprint) | reportedly severe microcephaly, behavioural deficits, dysregulated neurodevelopmental and ribosomal gene programmes, altered RARS1–ribosome localisation in neurons | **not peer-reviewed** (bioRxiv 10.1101/2025.09.08.674979, Sept 2025); search summaries describe a brain-development/microcephaly phenotype, with no hypomyelination reported; full text not accessed | bioRxiv |
| Germline *Rars1* knockout | — | not characterised in the literature found; complete ArgRS loss is expected to be lethal | — | — |

**Gaps**
- There is no published, peer-reviewed in-vivo model of HLD9 hypomyelination.
- There are no iPSC-derived oligodendrocyte or organoid models, and no zebrafish model.

These gaps are a reasonable basis for a `KNOWLEDGE_GAP` or `HUMAN_MODEL_MISMATCH` discussion on the oligodendrocyte-differentiation node.

---

## Key references

| PMID | Citation | Evidence type |
|---|---|---|
| 24777941 | Wolf NI et al. Mutations in RARS cause hypomyelination. *Ann Neurol* 2014;76:134–139 | HUMAN_CLINICAL |
| 28905880 | Nafisinia M et al. Mutations in RARS cause a hypomyelination disorder akin to Pelizaeus-Merzbacher disease. *Eur J Hum Genet* 2017 | HUMAN_CLINICAL + IN_VITRO (split items) |
| 30791064 | Rezaei Z et al. Hypomyelinating leukodystrophy with spinal cord involvement caused by a novel variant in RARS. *Neuropediatrics* 2019 | HUMAN_CLINICAL |
| 31737794 | Matsumoto N et al. HLD-associated mutation of RARS leads it to the lysosome… *Biochem Biophys Rep* 2019 | IN_VITRO |
| 31814314 | Mendes MI et al. RARS1-related hypomyelinating leukodystrophy: Expanding the spectrum. *Ann Clin Transl Neurol* 2020 | HUMAN_CLINICAL + IN_VITRO |
| 33190326 | Di Bella D et al. Hypomyelinating leukodystrophies in adults. *Eur J Neurol* 2021 | HUMAN_CLINICAL |
| 33515434 | Li G et al. Distinct pathogenic mechanisms of various RARS1 mutations in PMLD. *Sci China Life Sci* 2021 | IN_VITRO |
| 37186453 | Wan L et al. RARS1-related developmental and epileptic encephalopathy. *Epilepsia Open* 2023 | HUMAN_CLINICAL + IN_VITRO + COMPUTATIONAL |
| 38618971 | Biglari S et al. RARS1-related HLD-9 in two distinct Iranian families. *Mol Genet Genomic Med* 2024 | HUMAN_CLINICAL |
| 39542129 | Kim DK et al. Assembly of the human multi-tRNA synthetase complex through leucine zipper motifs. *J Mol Biol* 2024 | IN_VITRO (structural); not in the local cache |
| 29451896 | Ji H et al. Hypomyelinating disorders in China (119 patients). *PLoS One* 2018 | HUMAN_CLINICAL; one *RARS1* patient (c.5A>G/c.1625+2T>G); not in the local cache |
| — | bioRxiv 10.1101/2025.09.08.674979 (2025), RARS1 MSC integration mouse | preprint; not citable as KB evidence |

**For curation.** The existing `kb/disorders/Hypomyelinating_Leukodystrophy_9.yaml` holds only a disease term and one phenotype. Nine of the references above are already in `references_cache/`. PMIDs 39542129 and 29451896 would need `just fetch-reference` before they can be cited.

Sources:
- [PMC11017294 – Biglari 2024](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11017294/)
- [PMC10472388 – Wan 2023](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10472388/)
- [MedGen 863760](https://https.ncbi.nlm.nih.gov/medgen/863760)
- [Nemours HLD9 summary](https://nemours.org/pediatric-research/labservices/diagnostic/molecular-diagnostics-lab/hypomyelinating-leukodystrophy-9.html)
- [LOVD HLD9](https://databases.lovd.nl/shared/diseases/04640)
- [VU Research – Wolf 2014](https://research.vu.nl/en/publications/mutations-in-rars-cause-hypomyelination/)
- [DOAJ – Mendes 2020](https://doaj.org/article/0451d47dda844ada9b1700050648a958)
- [bioRxiv preprint 2025.09.08.674979](https://www.biorxiv.org/content/10.1101/2025.09.08.674979.full.pdf)
- [MGI Rars1](https://www.informatics.jax.org/go/marker/MGI:1914297)
- [Frontiers Cell Neurosci 2020](https://www.frontiersin.org/journals/cellular-neuroscience/articles/10.3389/fncel.2020.625879/full)
- [PSK 2026 conference abstract](https://conference.psk.or.kr/page/poster_view.php?num=14848)
- [Global Genes – ORPHA:438114](https://globalgenes.org/?p=613738)
- [Qeios entry](https://www.qeios.com/read/GNGSXZ/pdf)
- [RCSB 8J9S](https://www.rcsb.org/structure/8J9S)
- [KNU – Kim 2024 JMB](https://research.knu.ac.kr/en/publications/assembly-of-the-human-multi-trna-synthetase-complex-through-leuci/)
- [HGNC REST – RARS1](https://rest.genenames.org/fetch/symbol/RARS1)
- [PubMed search](https://pubmed.ncbi.nlm.nih.gov/?term=RARS1+OR+RARS+hypomyelination&size=50)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 8 |
| Quoted claims found in source | 8 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 13 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 65 |
| Resolved | 62 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 6 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014506` (2 mentions) - the report calls it "MONDO"; MONDO calls it **leukodystrophy, hypomyelinating, 9**
- `MONDO:0010714` (1 mention) - the report calls it "Parent grouping"; MONDO calls it **Pelizaeus-Merzbacher spectrum disorder**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002521` (2 mentions) - the report calls it "EEG** shows hypsarrhythmia in spasms"; HP calls it **Hypsarrhythmia**
- `GO:0004814` (1 mention) - the report calls it "Arginine-tRNA ligase activity (molecular function)"; GO calls it **arginine-tRNA ligase activity**
- `GO:0017101` (1 mention) - the report calls it "Aminoacyl-tRNA synthetase multienzyme complex (CC)"; GO calls it **aminoacyl-tRNA synthetase multienzyme complex**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.