---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-29T18:37:12.201652'
end_time: '2026-10-29T18:39:54.934580'
duration_seconds: 162.73
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Ectopia Lentis 1, Isolated, Autosomal Dominant
  mondo_id: MONDO:0007514
  category: Mendelian
  causal_genes: FBN1
  omim_id: OMIM:129600
  synonyms: ectopia lentis, familial; ECTOL1; FBN1 isolated ectopia lentis; isolated
    ectopia lentis caused by mutation in FBN1
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
  web_search_requests: 4
  num_turns: 14
  total_cost_usd: 1.9507615999999994
  session_id: d766227f-70b4-5440-ab6b-6f5a6ed9d934
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  assistant_text_blocks: 2
citation_count: 11
reference_validation:
  total_references: 24
  verified: 24
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 24
  on_topic: 22
  off_topic: 1
  off_topic_references:
  - PMID:12446361
  needs_review: true
  validator_version: 0.4.0
term_validation:
  total_terms: 30
  verified: 27
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 13
  labels_matching: 7
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: MONDO:0009152
    reported_labels:
    - ADAMTSL4
    ontology_label: ectopia lentis 2, isolated, autosomal recessive
  - term_id: HP:0000501
    reported_labels:
    - Glaucoma (pupillary-block / secondary)
    ontology_label: Glaucoma
  - term_id: HP:0003829
    reported_labels:
    - Penetrance:** high, but non-penetrance is documented
    ontology_label: Typified by incomplete penetrance
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
- **Disease Name:** Ectopia Lentis 1, Isolated, Autosomal Dominant
- **MONDO ID:** MONDO:0007514 (if available)
- **Causal gene(s):** FBN1
- **OMIM:** OMIM:129600
- **Synonyms:** ectopia lentis, familial; ECTOL1; FBN1 isolated ectopia lentis; isolated ectopia lentis caused by mutation in FBN1
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Ectopia Lentis 1, Isolated, Autosomal Dominant** covering all of the
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

I'm checking the local reference cache for mouse zonule studies, then running a few web searches to fill the gaps in models and epidemiology.

# Ectopia Lentis 1, Isolated, Autosomal Dominant (ECTOL1; MONDO:0007514; OMIM 129600): research report

**Causal gene: *FBN1*** (fibrillin‑1; HGNC:3603, written `hgnc:3603` in this repo; 15q21.1). This report covers the dominant *FBN1* form only. It does not cover recessive *ADAMTSL4*-related ectopia lentis 2 (MONDO:0009152).

**How this was assembled.** The worktree already contains a curated entry, `kb/disorders/Ectopia_Lentis_1_Isolated_Autosomal_Dominant.yaml`, created today (718 lines, 26 PMIDs). All of its evidence quotes come from cached PubMed records under `references_cache/`. Most direct quotes below are taken from that entry; I did not re-run snippet validation in this session. Material from new web searches is labelled as such. Where a PMID came from memory or could not be confirmed, it is marked **[verify]**.

---

## 1. Disease information

**Overview.** ECTOL1 is a displaced crystalline lens caused by a heterozygous germline *FBN1* variant, without the aortic and systemic features needed for a Marfan syndrome (MFS) diagnosis. It is usually bilateral and familial. Age at recognition runs from early childhood to late adulthood. All of its morbidity comes from the eye: refractive error, glaucoma and retinal detachment.

The revised Ghent nosology (2010) places *FBN1*-related ectopia lentis on the type‑1 fibrillinopathy continuum with MFS. It names the isolated form **"ectopia lentis syndrome" (ELS)**: ectopia lentis with an *FBN1* variant **not** previously associated with aortic dilation or dissection. The quote below is from the PMID:20591885 abstract as cached:
- "aortic root aneurysm and ectopia lentis are the cardinal clinical features"

**Identifiers**

| Resource | ID |
|---|---|
| MONDO | MONDO:0007514 (ectopia lentis 1, isolated, autosomal dominant) |
| OMIM | 129600 |
| Orphanet | ORPHA:1885, "Isolated ectopia lentis". This node covers both AD and AR inheritance, so it is broader than ECTOL1 ([Phenodis mirror](https://iegext02.helmholtz-munich.de/phenodis/disease/show/1698)) |
| MedGen | C1851286 ([MedGen](https://https.ncbi.nlm.nih.gov/medgen/C1851286)) |
| ICD‑10 | Q12.1, congenital displaced lens **[verify]** |
| ICD‑11 | Not confirmed in this session |
| MeSH | Ectopia Lentis, D004479 **[verify]** |

**Synonyms.** ECTOL1; ectopia lentis, familial; FBN1 isolated ectopia lentis; isolated ectopia lentis caused by mutation in FBN1; ectopia lentis syndrome (ELS, the Ghent term).

**Data provenance.** Everything here is aggregated from published literature: family pedigrees, case series and cohorts. None of it comes from EHR data.

## 2. Etiology

- **Cause:** a heterozygous germline *FBN1* variant. There is no known environmental, infectious or immune cause.
- **Genetic risk:**
  - **PMID:20564469** (British series): "Causative FBN1 mutations were identified in 23/36 (64%) of probands while homozygous or compound heterozygous ADAMTSL4 mutations were identified in 6/12 (50%) of the remaining probands." The probands had ectopia lentis but did not meet Ghent criteria.
  - **PMID:33576469:** "The seven pathogenic variants were identified in 8/12 (66.7%) probands with IEL."
  - **PMID:38190127** (156 Chinese ectopia lentis families, not restricted to non-syndromic cases): "97.4% resulted from variants in FBN1, whereas the remaining were caused by variants in ADAMTSL4 (1.3%) and LTBP2 (1.3%)."
- **Modifier genes:** none established.
- **Protective factors and gene–environment interactions:** none reported. Section left empty.
- **Non-genetic risk factors:** none established. Ocular trauma can precipitate lens dislocation in general, but there is no ECTOL1-specific evidence for it.

## 3. Phenotypes

| Phenotype | HPO (validated in KB entry) | Frequency / characteristics | Key evidence |
|---|---|---|---|
| Ectopia lentis, usually bilateral | HP:0001083 | Obligate. Median age at diagnosis was 3 y in a Chinese series and 35 y in a British FBN1 series; late-onset families also exist | PMID:33576469: "all had bilateral EL with a median age at diagnosis of three years." PMID:22736615: "Median age of diagnosis of EL was 35 years in patients with FBN1 mutations and 2 years in patients with ADAMTSL4 mutations" |
| High myopia | HP:0011003 | 83.3% (10/12). Partly lenticular: mean axial length was normal (22.74 mm) in FBN1 carriers | PMID:33576469: "High myopia was the most common feature among the probands (83.3%; 10/12 cases)." |
| Astigmatism (irregular) | HP:0000483 | Common | PMID:38190127: "Aberrant astigmatism is a suggestive sign of EL." |
| Glaucoma (pupillary-block / secondary) | HP:0000501 | Variable. Can be the presenting feature in late-onset families | PMID:18615205: "late-onset lens dislocation and secondary glaucoma but had no signs of cardiovascular abnormality or abnormal skeletal features". PMID:36946977: "All 3 probands presented with EL and pupillary-blocking glaucoma." |
| Rhegmatogenous retinal detachment | HP:0012230 | Seen in every adult of one FBN1 pedigree, often after vitreolensectomy | PMID:32685406: "Macula-on RRD was present in all individuals >18y, 64% (7/11 eyes) presenting post-vitreolensectomy" |
| Pupillary abnormality; progressive hyperopia (aphakic/lens-related) | Candidates: HP:0000615 abnormal pupil morphology; HP:0000540 hypermetropia **[verify terms]** | Reported in one p.Arg62Cys family | PMID:22950452 |
| Amblyopia; iridodonesis/phacodonesis | Candidate HPO terms **[verify]** | Common in pediatric ectopia lentis generally. Not quantified for ECTOL1 | none |

**Quality of life.** I found no ECTOL1-specific EQ‑5D or SF‑36 data. The burden is visual: refractive amblyopia in children, contact-lens dependence after aphakia, and the risk of blindness from glaucoma or retinal detachment. PMID:33576469: "IEL can lead to blindness as result of severe complications, such as retinal detachment and secondary glaucoma."

**Explicitly absent.** By definition there is no aortic root dilation and the systemic score is below the Ghent threshold.

## 4. Genetic and molecular information

- **Gene:** *FBN1* (OMIM *134797; HGNC:3603). Fibrillin‑1 is a ~350 kDa extracellular matrix glycoprotein built from 47 EGF-like domains (43 calcium-binding, cbEGF) and 7 TB/8‑Cys domains. It polymerizes into 10–12 nm microfibrils.
- **Variant spectrum (key distinguishing feature):**
  - **PMID:19353630** (146 adults with FBN1 variants who did not meet MFS criteria, from a 1,009‑proband consortium): "In patients with isolated EL, missense mutations involving a cysteine were predominant, mutations in exons 24-32 were underrepresented, and no mutations leading to a premature truncation were found."
  - **PMID:41409312** (literature review): "approximately 66.7% of reported variants involve missense substitutions affecting cysteine residues".
  - **Splice variants with in-frame skipping (PMID:39939800):** "skipping of exon 11, which results in an in-frame deletion of 60 amino acids corresponding to the 'hinge' region of FBN1 protein, was confirmed in a minigene experiment." This is IN_VITRO evidence.
  - **Recurrent variants:**
    - p.Arg62Cys, Chinese families (PMID:16765689, PMID:22950452).
    - Indian 27-member, four-generation family with a recurrent variant; LOD 5.74 at D15S1024 (PMID:18079676).
    - p.Arg974Cys (c.2920C>T): "C>T transition at nucleotide position c.2920" changing arginine to cysteine at codon 974 (PMID:22539873, from web search). [Mol Vis 2012](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3335778/)
    - p.Cys587Arg (c.1759T>C), Chinese family ([PMC3249434](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3249434/); PMID not retrieved).
    - p.Gly1344Glu (c.4031G>A), late-onset Chinese family ([BJO 2021;105:341](https://bjo.bmj.com/content/105/3/341); PMID not retrieved).
  - **Older series:** in patients with ectopia lentis and marfanoid habitus, 7/11 (63%) carried FBN1 variants, with Arg→Cys substitutions over-represented. This is Comeglio et al. 2002 (PMID:12446361 **[verify]**).
- **Classification:** most variants are reported as pathogenic or likely pathogenic in families. **ClinGen has no gene–disease validity curation for FBN1 against MONDO:0007514.** FBN1–Marfan syndrome is Definitive in ClinGen.
- **Allele frequency:** the reported variants are absent from or ultra-rare in controls. For example, PMID:41409312 found them absent "in WES data from 200 ophthalmologically normal in-house controls".
- **Origin:** germline. No somatic-origin cases are known.
- **Functional consequence:** a dominant-negative or qualitative defect in microfibril assembly, *inferred* from the cysteine-missense pattern and the absence of truncating (haploinsufficient) alleles. The functional data are not demonstrated for most variants.
- **Epigenetics and chromosomal abnormalities:** none reported. Large 15q21 deletions cause MFS-like phenotypes, not isolated EL.

## 5. Environmental information

There are no environmental, lifestyle or infectious contributors. Not applicable.

## 6. Mechanism and pathophysiology

**Causal chain**

1. A heterozygous germline *FBN1* variant, usually cysteine-altering missense in a cbEGF or TB domain, or in-frame exon skipping, **results in** an abnormal fibrillin‑1 monomer. *Demonstrated in genetics; the protein-level effect is inferred.*
2. The mutant monomer, co-assembled with wild-type protein, **leads to** defective or reduced microfibril assembly (GO:0160054 microfibril assembly, decreased). *Inferred for ECTOL1 alleles; shown in vitro for related cbEGF variants.*
3. Microfibrils secreted by the **non-pigmented ciliary epithelium** (CL:0002304) form the ciliary zonule (UBERON:0006762, suspensory ligament of lens). Defective microfibrils **result in** thinner, weaker zonular fibres. *Demonstrated in mouse (Jones 2019, below).*
4. The weak zonule stretches and ruptures under accommodative and inertial load, which **leads to** lens subluxation (ectopia lentis). *Demonstrated in mouse; observed clinically.*
5. Branches from the displaced lens:
   - **5a.** Lens tilt and decentration produce irregular astigmatism and lenticular myopia. In children this **converts to** axial myopia and amblyopia. PMID:38190127: "Early-stage EL manifests refractive error but gradually converts to axial myopia through defocus introduced by lens dislocation."
   - **5b.** An anteriorly displaced lens causes pupillary block, which **leads to** angle-closure or secondary glaucoma, then optic neuropathy.
   - **5c.** Vitreous traction, and surgery to remove the lens, **predispose to** rhegmatogenous retinal detachment. *Association; intermediates not established.*
6. **Unexplained tissue restriction.** The aortic wall and skeleton are clinically spared. Why the zonule is preferentially vulnerable to these alleles is **not established**. It may reflect the zonule's near-pure microfibril composition with no elastin core, or allele-specific effects on assembly rather than haploinsufficiency (hypothesis). The TGF‑β dysregulation thought to drive MFS aortopathy is not implicated in ECTOL1.

**Model-organism support (from web search):**
- **Jones, Rodriguez & Bassnett 2019** (*Dis Model Mech*, PMID:30642872): "Conditional knockout of Fbn1 in NPCE, but not lens, profoundly affected the ciliary zonule." In my words, the rest of the abstract says the fibres were thinner and weaker, ruptured by 3 months, and the mice developed ectopia lentis, then cataract and globe elongation. [PMC6361150](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6361150/)
- **Shi et al. 2013:** fibrillin‑1 is a prominent constituent of the mouse zonule, and Fbn2 expression in NPCE falls after birth while Fbn1 rises. This suggests postnatal Fbn1 dependence. [PMC3621578](https://pmc.ncbi.nlm.nih.gov/articles/PMC3621578) (PMID not retrieved).

**Suggested terms**

| Kind | Terms |
|---|---|
| GO | GO:0160054 microfibril assembly; GO:0001527 microfibril (CC) **[verify]**; GO:0031012 extracellular matrix (CC) **[verify]**; GO:0005509 calcium ion binding (MF) **[verify]** |
| CL | CL:0002304 non-pigmented ciliary epithelial cell |
| UBERON | UBERON:0006762 suspensory ligament of lens; crystalline lens UBERON:0000965 **[verify]**; ciliary body UBERON:0001775 **[verify]** |

**Omics.** There are no transcriptomic, proteomic, metabolomic, single-cell or CRISPR-screen datasets specific to ECTOL1. Not available.

## 7. Anatomical structures

- **Primary:** ciliary zonule and crystalline lens, bilateral.
- **Secondary:** iris and anterior chamber angle (glaucoma), retina (detachment), optic nerve (glaucomatous damage).
- **Tissue level:** extracellular microfibrillar matrix of the zonule.
- **Cell level:** the NPCE cells that secrete it.
- **Subcellular:** extracellular space / microfibril (GO CC).
- **Lateralization:** usually bilateral; the degree of displacement may be asymmetric.
- **Excluded by definition:** aortic root and skeleton. MFS-type systemic findings below threshold may be present.

## 8. Temporal development

- **Onset:** congenital or early childhood in many families (median 3 y, PMID:33576469). Diagnosis can be in adulthood (median 35 y, PMID:22736615), and late-onset families are reported (PMID:18615205; Gly1344Glu family).
- **Course:** slowly progressive subluxation that may advance to complete dislocation. Complications such as glaucoma and RD accumulate with age.
- **Critical period:** the amblyogenic window in childhood. Early optical correction or lens surgery matters most then.
- **Remission:** none. Surgery removes the displaced lens but not the underlying zonular defect.

## 9. Inheritance and population

- **Inheritance:** autosomal dominant (HP:0000006). PMID:25900864: "Isolated ectopia lentis is usually autosomal dominant and commonly due to the mutations of FBN1 gene."
- **Penetrance:** high, but non-penetrance is documented (HP:0003829). PMID:25900864: "The child's mother presumably represents a rare case of nonpenetrance." No penetrance estimate exists.
- **Expressivity:** variable in age at onset and in complications. Some families sit on the continuum with MFS. PMID:19353630: "Studies of recurrent mutations and affected family members of propositi with only one major clinical criterion argue for a clinical continuum between such phenotypes and classical MFS."
- **Anticipation:** none. **Germline mosaicism:** not specifically reported.
- **Founder effects:** p.Arg62Cys is recurrent in Chinese families, but no proven founder haplotype has been shown.
- **Consanguinity:** not relevant for an AD condition. It is relevant for the AR *ADAMTSL4* differential.
- **Prevalence and incidence:** **no published population estimate.** Orphanet gives no data for ORPHA:1885 ([MalaCards](https://www.malacards.org/card/isolated_ectopia_lentis)). Ectopia lentis of all causes is often quoted at around 6.4/100,000 (Danish data), but that is not ECTOL1-specific and I did not confirm it in this session. The prevalence slot should be left empty or set to `NOT_YET_DOCUMENTED`.
- **Sex ratio:** expected 1:1. **Geography:** reported worldwide, with Chinese, Indian, Turkish, European and Australian families.

## 10. Diagnostics

**Ophthalmic examination.** Dilated slit-lamp examination (NCIT:C75583) to document lens position, plus refraction, axial length, IOP, gonioscopy, UBM and fundus examination. The full work-up is listed in PMID:22950452.

**Excluding Marfan syndrome.** Echocardiography (NCIT:C16525) and a systemic score are needed. PMID:25900864: "His echocardiogram was normal and he did not meet the revised Ghent criteria for Marfan syndrome."

**Genetic testing (NCIT:C15709)**

- Use an ectopia lentis / connective-tissue NGS panel: *FBN1, ADAMTSL4, LTBP2, ADAMTS10, ADAMTS17, ADAMTSL2/ASB10, CBS, CPAMD8, COL4A5*. Exome or genome sequencing is a reasonable alternative. PMID:37107549: "panel-based genetic testing pointed to a molecular diagnosis in >90% of paediatric ectopia lentis cases requiring surgery."
- If panel or exome sequencing is negative, consider testing for intronic or splice variants (PMID:39939800).
- CMA, karyotype, FISH, mitochondrial DNA and repeat-expansion testing are not indicated.

**Classification rule.** PMID:24635535: "patients with EL and a FBN1 mutation are now categorically diagnosed with MFS, if their mutation has previously been described with aortic dilation/dissection." In the same study, "57/123 probands (46.3%) are now classified as MFS ... and 37/96 mutations (38.5%) reported to cause isolated EL have also been found in patients with aortic dilation/dissection."

**Laboratory test.** Plasma total homocysteine, to exclude CBS deficiency.

**Differential diagnosis**

| Condition | Distinguishing features |
|---|---|
| Marfan syndrome (MONDO:0007947) | Aortic root dilation, systemic score ≥7, or a variant previously reported with aortic disease |
| ECTOL2, *ADAMTSL4* (MONDO:0009152) | AR inheritance; earlier onset; long axial length (27.5 vs 22.7 mm) (PMID:22736615) |
| Weill–Marchesani syndrome (MONDO:0018096) | Microspherophakia, short stature, brachydactyly; genes *ADAMTS10, ADAMTS17, LTBP2, FBN1* |
| Classic homocystinuria (MONDO:0009352) | Raised homocysteine; inferonasal lens displacement; thrombosis |
| Ectopia lentis et pupillae (*ADAMTSL4*) | Corectopia |
| Others | Sulfite oxidase / molybdenum cofactor deficiency, Stickler syndrome, trauma |

**Screening.** Cascade testing of first-degree relatives with an eye examination and an echocardiogram. There is no newborn screening.

## 11. Outcome and prognosis

- **Survival:** life expectancy is presumed normal, provided the condition truly is ELS and not MFS. There are no mortality data specific to ECTOL1.
- **Morbidity:** amblyopia, glaucoma, RD and blindness.
- **Main prognostic uncertainty:** reclassification to MFS (46.3% of historical probands, PMID:24635535). For aortic involvement outside strict ECTOL1:
  - Mild aortic root changes were found in 7 of 8 children with bilateral EL who did not meet Ghent criteria (2011 series, PMID not retrieved).
  - In 320 children with FBN1 variants, 71% had ascending aortic dilation and 55% had ectopia lentis, but surgery (5%) and dissection (1%) were rare ([Montpellier record](https://esploro.umontpellier.fr/esploro/outputs/journalArticle/Clinical-and-molecular-study-of-320/99153287309311)).
- **Visual outcome after surgery:** good in one pedigree. The prognosis depends on timely treatment of amblyopia and glaucoma.

## 12. Treatment

**Optical correction.** Spectacles or contact lenses, often aphakic or phakic correction. Treat amblyopia with occlusion therapy.

**Surgery.** Lensectomy or pars plana vitreolensectomy (NCIT:C50837, Vitrectomy) with a secondary IOL: iris-claw, scleral-fixated, or capsular tension ring / segment–supported.
- PMID:32685406: "refractive management with iris-claw IOLs provided superior outcomes to contact lenses"
- This rests on one pedigree of 8 patients.

**Glaucoma.** Laser peripheral iridotomy for pupillary block, IOP-lowering drugs, or lens extraction. Specific NCIT procedure terms would need lookup **[verify]**.

**Retinal detachment.** Vitreoretinal repair.

**Systemic surveillance.** Periodic echocardiography. PMID:24635535 and PMID:19353630 support this; the KB entry currently binds it to NCIT:C15747 Supportive Care. The entry gives no surveillance interval. Starting an angiotensin-receptor blocker or β‑blocker is indicated only if the patient converts to MFS.

**Pharmacogenomics, gene, cell or RNA therapy:** none. **Clinical trials:** I found no NCT trials specific to ECTOL1.

## 13. Prevention

- **Primary prevention:** genetic counselling. There is a 50% recurrence risk to offspring, and PGT or prenatal testing is available once the familial variant is known.
- **Secondary prevention:** cascade ophthalmic screening of relatives and early childhood eye examinations.
- **Tertiary prevention:** prevent amblyopia, monitor IOP, give RD warning symptoms, and carry out lifelong aortic surveillance. Advising against contact sports is commonly recommended, but no evidence was found for it.
- **Vaccines and public-health measures:** not applicable.

## 14. Other species

- **Fibrillin-related lens luxation:** no naturally occurring *FBN1*-isolated lens luxation is documented. Bovine Marfan-like syndrome with *FBN1* variants includes ocular involvement (OMIA, **[verify]**).
- **Canine primary lens luxation:** caused by *ADAMTS17* (terriers; OMIA 001492‑9615 **[verify]**). This is a mechanistic analogue of the zonular disorders, not an *FBN1* orthologue disease.
- **Orthologues:** mouse *Fbn1* (MGI:95489 **[verify]**); NCBI Gene for human *FBN1* is 2200.
- **Zoonotic potential:** none.

## 15. Model organisms

| Model | Recapitulation | Limitations |
|---|---|---|
| *Fbn1* conditional knockout in NPCE (Jones 2019, PMID:30642872) | Weak, thin zonular fibres; ruptured by 3 months; ectopia lentis; then cataract and globe elongation | A null allele, not a cysteine-missense dominant-negative; aortic phenotype not assessed in this model |
| *Fbn1* lens-specific knockout (same study) | No zonular phenotype; a negative control that localizes the source to NPCE | none listed |
| *Fbn1* mgΔlpn (dominant-negative, 2021 *Exp Eye Res*) | Ocular structures largely maintained | Fibrillin‑2 may compensate in mouse, so likely `FAILS_TO_RECAPITULATE` or `PARTIAL` for ectopia lentis (ectopia findings not confirmed) |
| *Fbn1* C1039G/+ and mgR/mgR (MFS models) | Aortic disease models | Ocular phenotype mild or inconsistent. Not models of ECTOL1 |

Repositories: MGI, IMSR, MMRRC. Patient iPSC-derived ciliary epithelium is not reported.

---

## Gaps for KB curation
1. **No prevalence data.** Leave the slot empty or set it to `NOT_YET_DOCUMENTED`.
2. **No ClinGen validity curation** for FBN1–MONDO:0007514. Leave `gene_disease_validity` absent.
3. **Mouse NPCE model (PMID:30642872) is not yet in the KB entry.** It is a strong `animal_models` candidate with `RECAPITULATES` against "Defective Fibrillin-1 Microfibrils of the Ciliary Zonule". Run `just fetch-reference PMID:30642872` first.
4. **The tissue-restriction mechanism is an open question.** It is a candidate for a `KNOWLEDGE_GAP` discussion.
5. **Unconfirmed items.** Several PMIDs (Comeglio 2002, Shi 2013, the 2011 pediatric series) and some ontology terms marked **[verify]** were not confirmed in this session. Look them up before binding.

## Sources
- Existing curated entry: `kb/disorders/Ectopia_Lentis_1_Isolated_Autosomal_Dominant.yaml`. Its quotes come from cached abstracts: PMIDs 20591885, 24635535, 19353630, 20564469, 22736615, 33576469, 38190127, 34818515, 37107549, 25900864, 18079676, 16765689, 22950452, 18615205, 36946977, 32685406, 39939800, 41409312, 36670079.
- [Jones et al. 2019, Dis Model Mech (PMC6361150)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6361150/)
- [Shi et al. 2013 (PMC3621578)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3621578)
- [Yang et al. 2012, Mol Vis, PMID:22539873 (PMC3335778)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3335778/)
- [Novel FBN1 mutation, Chinese IEL family (PMC3249434)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3249434/)
- [Late-onset IEL, p.Gly1344Glu, BJO](https://bjo.bmj.com/content/105/3/341)
- [Phenodis / Orphanet mirror, ORPHA:1885](https://iegext02.helmholtz-munich.de/phenodis/disease/show/1698)
- [MalaCards, Isolated Ectopia Lentis](https://www.malacards.org/card/isolated_ectopia_lentis)
- [MedGen C1851286](https://https.ncbi.nlm.nih.gov/medgen/C1851286)
- [Arizona Hereditary Ocular Disease database](https://disorders.eyes.arizona.edu/taxonomy/term/688)
- [320-children FBN1 study (Montpellier record)](https://esploro.umontpellier.fr/esploro/outputs/journalArticle/Clinical-and-molecular-study-of-320/99153287309311)
- [NEI news, Marfan eye research](https://www.nei.nih.gov/about/news-and-events/news/new-research-marfan-syndrome-focuses-eyes)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 24 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 24 |
| On topic | 22 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:12446361` (1 mention) - Prevalence and risk factors associated with dry eye symptoms: a population based study in Indonesia.
  - shared terms: none

Weighed against this report's own most characteristic terms: `fbn1`, `ectopia`, `lentis`, `lens`, `variant`, `aortic`, `verify`, `mfs`, `mutation`, `ectol1`, `glaucoma`, `isolated`, `gene`, `family`, `found`, `serie`, `disease`, `familie`, `model`, `mondo`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 30 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 13 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0009152` (2 mentions) - the report calls it "ADAMTSL4"; MONDO calls it **ectopia lentis 2, isolated, autosomal recessive**
- `HP:0000501` (1 mention) - the report calls it "Glaucoma (pupillary-block / secondary)"; HP calls it **Glaucoma**
- `HP:0003829` (1 mention) - the report calls it "Penetrance:** high, but non-penetrance is documented"; HP calls it **Typified by incomplete penetrance**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001083` (1 mention) - the report calls it "Ectopia lentis, usually bilateral"; HP calls it **Ectopia lentis**
- `HP:0000483` (1 mention) - the report calls it "Astigmatism (irregular)"; HP calls it **Astigmatism**
- `CL:0002304` (2 mentions) - the report calls it "non-pigmented ciliary epithelium", "Microfibrils secreted by the **non-pigmented ciliary epithelium"; CL calls it **non-pigmented ciliary epithelial cell**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0002304` - called "non-pigmented ciliary epithelium", "Microfibrils secreted by the **non-pigmented ciliary epithelium"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.