---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-27T22:02:52.830112'
end_time: '2026-10-27T22:08:38.485545'
duration_seconds: 345.66
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Spinocerebellar Ataxia, Autosomal Recessive, With Axonal Neuropathy
    3
  mondo_id: MONDO:0020770
  category: Mendelian
  causal_genes: COA7
  omim_id: OMIM:618387
  synonyms: SCAN3; COA7-related spinocerebellar ataxia with axonal neuropathy
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
  web_search_requests: 10
  num_turns: 34
  total_cost_usd: 2.6207459999999996
  session_id: 0bfb328d-96db-5dca-803a-342a247b0264
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  assistant_text_blocks: 4
citation_count: 16
reference_validation:
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 6
  quotes_valid: 6
  relevance_assessed: 18
  on_topic: 17
  validator_version: 0.4.0
term_validation:
  total_terms: 77
  verified: 74
  not_found: 0
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 3
  labels_matching: 0
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0020770
    reported_labels:
    - MONDO
    ontology_label: spinocerebellar ataxia, autosomal recessive, with axonal neuropathy
      3
  - term_id: DOID:0070465
    reported_labels:
    - DOID
    ontology_label: autosomal recessive spinocerebellar ataxia with axonal neuropathy
      3
  labels_variant: 1
  obsolete_terms:
  - term_id: GO:0005751
    ontology_label: obsolete mitochondrial respiratory chain complex IV
    replaced_by: GO:0045277
  unresolvable_prefixes:
  - GARD
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spinocerebellar Ataxia, Autosomal Recessive, With Axonal Neuropathy 3
- **MONDO ID:** MONDO:0020770 (if available)
- **Causal gene(s):** COA7
- **OMIM:** OMIM:618387
- **Synonyms:** SCAN3; COA7-related spinocerebellar ataxia with axonal neuropathy
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Spinocerebellar Ataxia, Autosomal Recessive, With Axonal Neuropathy 3** covering all of the
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

Stub-like entry. Let me fetch primary sources.

I'm pulling abstracts for the remaining COA7 papers from Europe PMC, because the PMC pages are blocked behind a verification check.

I have the core papers. One last check for animal models, then I'll write the report.

# Spinocerebellar Ataxia, Autosomal Recessive, With Axonal Neuropathy 3 (SCAN3; COA7-related disorder): research report

**Causal gene: *COA7*** (cytochrome c oxidase assembly factor 7; formerly C1orf163 / RESA1; HGNC:25716; OMIM gene *615623; UniProt Q96BR5; chromosome 1p32.3). All findings below are tied to MONDO:0020770 and OMIM #618387. SCAN1 (*TDP1*) and SCAN2 (*SETX*/AOA2) are different diseases caused by different genes. They are not covered here.

> **Note on ontology IDs.** The HP, GO, CL, UBERON, NCIT and CHEBI identifiers in this report are **candidates to check with a lookup** (runoak, OLS or `cache/*/terms.csv`) before they are written into the KB. Several were suggested from memory. The disease identifiers (MONDO xrefs, OMIM, PMIDs) and the quoted abstract text were checked against Europe PMC or OLS in this session.

---

## 1. Disease information

**Overview.** SCAN3 is an autosomal recessive mitochondrial disease. It usually starts in the first or second decade and has two main features:
- an axonal sensorimotor polyneuropathy that looks like Charcot-Marie-Tooth disease;
- cerebellar ataxia with cerebellar atrophy.

Some patients also have leukoencephalopathy, spinal cord atrophy, mild intellectual disability, subclinical mitochondrial myopathy, and later dystonia or parkinsonism. The cause is biallelic loss-of-function variants in *COA7*, which lead to cytochrome c oxidase (complex IV) deficiency.

The disease was named in 2018: "this new entity of disease would be referred to as spinocerebellar ataxia with axonal neuropathy type 3" (Higuchi et al., *Brain* 2018, **PMID:29718187**).

The field now treats it as a broader **COA7-related disorder** spectrum: "COA7-related disorders typically encompass a spectrum of conditions characterized by a variety of major (cerebellar ataxia and axonal polyneuropathy) and minor (leukoencephalopathy, dystonia, and parkinsonism) symptoms" (Higuchi et al., *J Neurol* 2024, **PMID:37750949**).

**Identifiers** (from the MONDO record via OLS):

| Resource | ID |
|---|---|
| MONDO | MONDO:0020770 |
| OMIM (phenotype) | 618387 |
| OMIM (gene) | 615623 |
| DOID | DOID:0070465 |
| GARD | GARD:0025244 |
| MedGen | 1673607 |
| UMLS | C5193070 |
| Orphanet | No disease-specific ORPHA code found. MONDO lists no Orphanet xref. It probably sits under a broader Orphanet grouping; check before citing. |
| ICD-10/ICD-11 | No specific code. The best available is G11.x (hereditary ataxia) or G60.x (hereditary neuropathy). |
| MeSH | No specific descriptor. |

**Synonyms.** SCAN3; spinocerebellar ataxia with axonal neuropathy type 3; COA7-related spinocerebellar ataxia with axonal neuropathy; COA7-related disorder; COA7-related mitochondrial leukoencephalopathy with COX deficiency (the first-reported presentation).

**Nature of the data.** All knowledge comes from individual case reports and small case series, roughly 11–13 published individuals. There are no registries, no natural-history cohorts and no EHR-derived data.

---

## 2. Etiology

- **Cause.** The disease is genetic and monogenic. It requires biallelic (homozygous or compound heterozygous) pathogenic *COA7* variants.
- **Genetic risk factors.** The only established risk factor is the *COA7* genotype. The recurrent missense **c.17A>G p.(Asp6Gly)** appears in most Japanese patients and in one Chinese patient. It was rare in ExAC (1/120,268 alleles, PMID:29718187). It may be an East Asian founder or recurrent allele, but no haplotype analysis has been published.
- **Modifier genes.** None reported.
- **Environmental risk or protective factors.** None reported, and none expected for a Mendelian loss-of-function disorder.
  - One possible trigger: in the Ban et al. 2021 patient, regression worsened after an episode of diarrhea and fever (PMID:34322155). This is anecdotal. It fits the general pattern of metabolic decompensation in mitochondrial disease, but has not been shown specifically for COA7.
- **Gene–environment interactions.** None documented.

---

## 3. Phenotypes

The frequencies below are drawn from about 12 published individuals. Denominators are small and the reporting is uneven.

| Phenotype | Candidate HP term | Type | Onset | Course | Approx. frequency | Key evidence |
|---|---|---|---|---|---|---|
| Axonal sensorimotor polyneuropathy | HP:0003477 Peripheral axonal neuropathy (consider HP:0007141 sensorimotor axonal polyneuropathy, verify) | sign / electrophysiology | early childhood to adolescence (one adult onset at 30 y) | slowly progressive | ~10/12 (absent in the infantile-encephalopathy and pure-dystonia cases) | PMID:29718187; PMID:35603692; PMID:42182620 |
| Cerebellar ataxia (limb, truncal, gait) | HP:0001251 Ataxia; HP:0001252? (verify) / HP:0002066 Gait ataxia | sign | childhood | progressive | ~9/12 | PMID:29718187 |
| Sensory ataxia | HP:0010871 Sensory ataxia (verify) | sign | childhood | progressive | reported (Higuchi patient 1) | PMID:29718187 |
| Cerebellar atrophy (MRI) | HP:0001272 Cerebellar atrophy | imaging | — | — | all 4 index Japanese patients; Tang patient; absent in Cicala siblings | PMID:29718187; PMID:35603692 |
| Spinal cord atrophy / thin cord | HP:0002251? → **verify**; candidate "Spinal cord atrophy" | imaging | — | — | ~3 (Higuchi patient 3, Martinez Lyons, Tang) | PMID:27683825; PMID:35603692 |
| Leukoencephalopathy / cavitating white-matter disease | HP:0002352 Leukoencephalopathy; HP:0002415 Leukodystrophy | imaging | infancy–childhood | progressive | ~4/12 | PMID:27683825; PMID:29718187; PMID:34322155 |
| Distal muscle weakness and atrophy | HP:0002460 Distal muscle weakness; HP:0003693 Distal amyotrophy | sign | childhood | progressive; wheelchair by age 9 in one patient | most | PMID:29718187 |
| Distal sensory loss | HP:0002936 Distal sensory impairment | sign | childhood | progressive | most | PMID:29718187 |
| Areflexia / hyporeflexia | HP:0001284 Areflexia; HP:0001265 Hyporeflexia | sign | — | — | most | PMID:29718187; PMID:42182620 |
| Steppage gait | HP:0003376 Steppage gait | sign | early childhood (presenting sign) | — | ≥1 | PMID:29718187 |
| Pes cavus / foot deformity | HP:0001761 Pes cavus | physical | <5 y (presenting sign) | — | several | PMID:29718187; PMID:42182620 |
| Dysarthria | HP:0001260 Dysarthria | sign | — | — | several | PMID:29718187; PMID:27683825 |
| Tremor | HP:0001337 Tremor | sign | — | — | several | PMID:27683825; PMID:42182620 |
| Dysmetria | HP:0001310 Dysmetria | sign | — | — | ≥1 | PMID:27683825 |
| Mild intellectual disability / cognitive difficulty | HP:0001256 Intellectual disability, mild | behavioral/cognitive | childhood | stable | ~4/12 (IQ 68 and 75 in two patients) | PMID:27683825; PMID:29718187; PMID:42182620 |
| Psychomotor / motor delay | HP:0001263 Global developmental delay; HP:0001270 Motor delay | developmental | infancy | — | 2 | PMID:27683825; PMID:34322155 |
| Developmental regression | HP:0002376 Developmental regression | behavioral | 3 mo | rapidly progressive | 1 | PMID:34322155 |
| Spasticity / hypertonia / hyperreflexia | HP:0001257 Spasticity; HP:0001276 Hypertonia | sign | infancy | progressive | 1 (atypical) | PMID:34322155 |
| Generalized dystonia | HP:0007325 Generalized dystonia (verify) / HP:0001332 Dystonia | sign | infancy | — | 1–2 | PMID:37750949; PMID:34322155 (tonic dystonia) |
| Parkinsonism (levodopa-responsive) | HP:0001300 Parkinsonism | sign | late adult (58 y) | progressive | 2 (possible overlap, see §9) | PMID:37264311; PMID:37750949 |
| Severe weakness, respiratory failure, feeding difficulty | HP:0002093 Respiratory insufficiency (verify); HP:0011968 Feeding difficulties | sign | — | — | 1 | PMID:37750949 |
| Scoliosis | HP:0002650 Scoliosis | physical | adolescence | — | ≥1 | PMID:27683825 |
| Elevated serum or CSF lactate | HP:0002151 Increased serum lactate; HP:0002490 Increased CSF lactate | lab | — | — | ~4 | PMID:27683825; PMID:29718187; PMID:34322155 |
| Mildly elevated CK | HP:0003236 Elevated circulating creatine kinase concentration | lab | — | — | ≥2 (189–577 IU/L; 488 U/L) | PMID:29718187; PMID:34322155 |
| Ragged-red fibres, COX-negative fibres, SDH-increased fibres | HP:0003200 Ragged-red muscle fibers; HP:0003688 Cytochrome C oxidase-negative muscle fibers | lab/biopsy | — | subclinical | ≥1; "mitochondrial abnormalities" in the Tang patient | PMID:29718187; PMID:35603692 |
| Decreased complex IV activity (fibroblasts, muscle, skin) | HP:0008347 Decreased activity of mitochondrial complex IV | lab | — | — | nearly all tested (Tang fibroblasts normal) | PMID:27683825; PMID:29718187; PMID:34322155; PMID:42182620 |
| Decreased complex I activity | HP:0011923 Decreased activity of mitochondrial complex I | lab | — | — | 1 | PMID:29718187 |
| Cardiac hypertrophy (septal/LV wall thickening) | HP:0001639 Hypertrophic cardiomyopathy (verify; a softer term may fit better) | sign | infancy | — | 1 (atypical) | PMID:34322155 |

**Absent features.** Higuchi et al. state there was **no nystagmus or oculomotor apraxia**, which separates SCAN3 from AOA1/AOA2. Both Cicala siblings had normal brain MRI (PMID:42182620): "Brain MRI findings were unremarkable in both siblings."

**Quality of life.** No formal QoL instruments (EQ-5D, SF-36) have been reported. The functional burden is mostly mobility:
- one patient used a wheelchair from age 9 (PMID:29718187);
- one walked only with ankle-foot orthoses at age 19 (PMID:27683825).

Dysarthria, mild cognitive impairment and, in severe cases, feeding difficulty and respiratory failure add to the burden.

**Key quotes**
- "all four patients had characteristic neurological features of peripheral neuropathy and ataxia with cerebellar atrophy" (PMID:29718187)
- "Both presented with early-onset, slowly progressive axonal sensorimotor neuropathy" (PMID:42182620)
- "infantile-onset generalized dystonia without cerebellar ataxia" (PMID:37750949)
- "Levodopa administration improved parkinsonism in this patient." (PMID:37264311)

---

## 4. Genetic and molecular information

**Gene.** *COA7*, HGNC:25716 (repository form `hgnc:25716`). It encodes a small (~231 aa) cysteine-rich protein (13 Cys) with five Sel1-like repeats, a subclass of the TPR fold.

**Published pathogenic variants** (NM_023077.2):

| Variant | Protein | Type | Zygosity / patient | Source |
|---|---|---|---|---|
| c.17A>G | p.Asp6Gly (D6G) | missense, recurrent | homozygous (Higuchi P1; Ouchi 2023); compound het with S149I, G144fs (Higuchi 2018), W185* (Tang 2022), C150Y (Higuchi 2023) | PMID:29718187; PMID:37264311; PMID:35603692; PMID:37750949 |
| c.115C>T | p.Arg39Trp (R39W) | missense | in trans with exon 2 deletion (Higuchi P2); also in Higuchi 2023 | PMID:29718187; PMID:37750949 |
| exon 2 deletion | in-frame loss of 47 aa | CNV, detected by MLPA | Higuchi P2 | PMID:29718187 |
| c.287+1G>T | exon 2 skipping (141 bp, in-frame) | splice donor | Martinez Lyons patient, maternal allele | PMID:27683825 |
| c.410A>G | p.Tyr137Cys (Y137C) | missense | Martinez Lyons patient, paternal allele | PMID:27683825 |
| c.430delG | p.Gly144fs | frameshift | Higuchi P4 | PMID:29718187 |
| c.446G>T | p.Ser149Ile | missense | Higuchi P3 | PMID:29718187 |
| c.449G>A | p.Cys150Tyr (novel 2023) | missense (loses a cysteine) | dystonia patient, with D6G | PMID:37750949 |
| c.457C>T | p.Leu153Phe (novel 2026) | missense | Cicala siblings; the second allele is not named in the abstract | PMID:42182620 |
| c.511G>A | p.Ala171Thr | missense | Ban 2021, maternal | PMID:34322155 |
| c.554G>A | p.Trp185* (novel 2022) | nonsense | Tang 2022, with D6G | PMID:35603692 |
| c.566A>G | p.Asn189Ser | missense (3 gnomAD alleles) | Ban 2021, paternal | PMID:34322155 |

- **Variant classes.** Mostly missense, plus a frameshift, a nonsense, a splice-site variant and an exon deletion. The exon deletion means **MLPA/CNV analysis is needed** when only one variant is found.
- **ACMG classification.** The ClinVar status of each variant was not retrieved here; check ClinVar before entering a `clinical_significance`. PanelApp (Genomics England) lists *COA7* with biallelic inheritance.
- **ClinGen / GenCC.** A GenCC submission exists (SGC-107318.2, which lists PMID:37750949 among six publications). No ClinGen CGGV record for *COA7* is cached locally, so do not assign a validity tier (CLAUDE.md: a tier is copied from a source, never assigned).
- **Population frequency.** D6G was 1/120,268 in ExAC (PMID:29718187). N189S has 3 alleles in gnomAD and A171T is absent (PMID:34322155).
- **Origin.** All variants are germline. There are no somatic or mosaic reports.
- **Functional consequence.** Loss of function / hypomorphic (`functional_impact_category: LOSS_OF_FUNCTION`; partial LOF is plausible for the missense alleles).
  - Wild-type COA7 re-expression rescued COX assembly and activity in patient fibroblasts (PMID:27683825).
  - Y137C and the exon-2-deleted protein are imported into mitochondria less efficiently (about 50% and 70% lower) and are degraded by the cytosolic proteasome (PMID:30885959).
- **Modifier genes, epigenetics, chromosomal abnormalities.** None reported. Not applicable.

---

## 5. Environmental information

No environmental, lifestyle or infectious causes are known. The intercurrent febrile or diarrheal illness before regression in one infant (PMID:34322155) should be recorded at most as a possible exacerbating factor (`environmental_effect: EXACERBATES`, with low confidence). Otherwise this section is **not applicable**.

---

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic *COA7* loss-of-function variants** (missense, truncating, splice, exon deletion) **lead to** reduced levels of functional COA7 protein. COA7 was undetectable by western blot in Martinez Lyons patient cells (PMID:27683825).
   - *Branch 1a (shown for missense and in-frame alleles):* the mutant precursors are imported more slowly through the **MIA40/CHCHD4 disulfide-relay (MIA) pathway**. COA7 forms a disulfide intermediate with MIA40 through Cys55. The unimported protein **is degraded by the cytosolic ubiquitin–proteasome system** (PMID:30885959): "mislocalized proteins are degraded in the cytosol by the proteasome."
   - *Branch 1b:* truncating alleles (G144fs, W185*) probably cause loss of protein outright. This is inferred; NMD and protein loss were not tested.
2. **Loss of COA7 in mitochondria results in** failure of its proposed **heme-dependent disulfide-reductase activity**. COA7 binds heme with His/Met axial ligation (reduction potential −353 mV), interacts transiently with the copper metallochaperones **SCO1 and SCO2**, and reduces the disulfides in their copper-binding sites. This regenerates the copper relay to **COX2** (Formosa et al., *PNAS* 2022, **PMID:35210360**): "COA7 interacts transiently with the copper metallochaperones SCO1 and SCO2."
   - Shown biochemically and in knockout cells. That patient variants act through this route is **inferred**.
3. **Impaired Cu_A delivery stalls complex IV assembly** after the COX1 module forms and before COX2/COX3 are added (PMID:35210360): "loss of COA7 blocks complex IV assembly after the initial step where the COX1 module is built." The result is lower levels of MT-CO2 and MT-CO3 and of assembled CIV and the III₂+IV supercomplex (PMID:27683825). Assembled CIV fell to 3.8–9.9% of control in Higuchi fibroblasts (PMID:29718187).
4. **Complex IV deficiency results in** reduced mitochondrial oxygen consumption and OXPHOS capacity. Maximal respiration was about 46% of control (PMID:34322155). Secondary complex I reduction was seen in one patient (PMID:29718187). Elevated lactate shows the shift to glycolysis.
5. **Bioenergetic failure in high-demand, long-axon neurons (inferred)** leads to length-dependent **axonal degeneration** of motor and sensory peripheral nerves. Sural nerve biopsy showed loss of large and medium myelinated fibres, with no onion bulbs or inflammation (PMID:29718187).
   - Drosophila neuron-specific *dCOA7* knockdown shortens neuromuscular-junction synaptic branches by about 50% and impairs climbing (PMID:29718187). This **supports a cell-autonomous neuronal requirement**.
6. **In parallel (branching), energy failure in CNS neurons and glia (inferred)** produces:
   - **6a** cerebellar atrophy, leading to cerebellar ataxia and dysarthria;
   - **6b** degeneration of the spinal cord long tracts and dorsal columns, leading to spinal cord atrophy and sensory ataxia;
   - **6c** white-matter injury and cavitating leukoencephalopathy (the oligodendrocyte or myelin vulnerability is inferred), leading to cognitive impairment and spasticity;
   - **6d** nigrostriatal dopaminergic involvement, leading to dystonia or levodopa-responsive parkinsonism. Striatal hypo-uptake on DaT SPECT is shown (PMID:37264311); the mechanism is inferred.
7. **Skeletal muscle (mild)** shows ragged-red, COX-negative and SDH-increased fibres and mildly raised CK, i.e. a subclinical mitochondrial myopathy (PMID:29718187). Neurogenic atrophy adds to the distal weakness.
8. **Clinical result:** a progressive axonal sensorimotor neuropathy plus cerebellar ataxia (SCAN3), with variable CNS features.

**Unresolved controversy (subcellular location).** Martinez Lyons et al. found COA7 behaving "as the soluble matrix protein Citrate Synthase," which suggests a matrix location (PMID:27683825). Mohanraj et al. 2019 (PMID:30885959) and Formosa et al. 2022 (PMID:35210360) place it in the **intermembrane space (IMS)**, imported by MIA. The IMS location also fits the SCO1/SCO2 function. Curate the IMS location as the better-supported current view and record the earlier matrix report in a note.

**Genotype–biochemistry discordance.** The Tang 2022 patient had normal respiratory-chain activity in fibroblasts despite pathogenic variants and abnormal muscle (PMID:35603692). Fibroblast testing can therefore give false-negative results, which is a useful diagnostic caveat.

### Ontology suggestions (verify)

- **GO biological process:** GO:0033617 mitochondrial cytochrome c oxidase assembly; GO:0045333 cellular respiration; GO:0006123 mitochondrial electron transport, cytochrome c to oxygen; GO:0045041 protein import into mitochondrial intermembrane space; GO:0008090? (check for a "retrograde/axonal transport" term only if justified; not shown for COA7).
- **GO molecular function:** GO:0020037 heme binding; a disulfide oxidoreductase activity term (for example GO:0015036 disulfide oxidoreductase activity, verify).
- **GO cellular component:** GO:0005758 mitochondrial intermembrane space; GO:0005759 mitochondrial matrix (historical report); GO:0005751 mitochondrial respiratory chain complex IV.
- **Cell types (CL):** CL:0000100 motor neuron; CL:0000101 sensory neuron; CL:0000121 Purkinje cell (inferred from cerebellar atrophy; not directly shown); CL:0000128 oligodendrocyte (inferred); CL:0000700 dopaminergic neuron; CL:0000057 fibroblast (assay system); CL:0000188 cell of skeletal muscle.
- **Molecular profiling.** No transcriptomic, proteomic, metabolomic, single-cell or spatial datasets are reported for COA7 disease. A future `datasets:` search (`just discover-datasets`) is likely to return none.

---

## 7. Anatomical structures affected

- **Primary.** Peripheral nervous system: peripheral nerves, length-dependent and lower limbs first (UBERON:0001021 nerve; sural nerve, verify the UBERON ID). Cerebellum (UBERON:0002037).
- **Secondary or variable.** Spinal cord (UBERON:0002240); cerebral white matter (UBERON:0002437); striatum / basal ganglia (UBERON:0002435 striatum); skeletal muscle (UBERON:0001134 skeletal muscle tissue); heart in one atypical infant (UBERON:0000948).
- **Body systems.** Nervous (central and peripheral), neuromuscular, and possibly cardiovascular.
- **Subcellular.** Mitochondrial intermembrane space and inner membrane, specifically respiratory complex IV.
- **Lateralization.** Bilateral and symmetric. DaT hypo-uptake was bilateral (PMID:37264311).

---

## 8. Temporal development

- **Onset.** Usually <5 years: foot deformity, steppage gait or poor dexterity. The range runs from **3 months** (encephalopathic form) through adolescence (15 y) to **30 years** (adult-onset D6G homozygote, PMID:37264311). Cicala siblings: 5 y and 12 y.
- **Pattern.** Insidious onset, then a chronic, slowly progressive course. The infantile form progressed rapidly (PMID:34322155).
- **Progression.**
  - Wheelchair from age 9 in one patient.
  - Ankle-foot orthoses at 19 in another.
  - The oldest reported patient was 63 years old and still described as alive.
  - Parkinsonism can appear decades after onset (age 58).
- **Stages, remission and critical periods.** No staging system exists and no remission has been reported. Possible vulnerability to intercurrent illness in infancy.

---

## 9. Inheritance and population

- **Inheritance.** Autosomal recessive, HP:0000007. Consanguinity was present in Higuchi patient 1, who was homozygous.
- **Penetrance and expressivity.**
  - Penetrance appears complete in biallelic individuals. Heterozygous parents are unaffected, with normal CIV in parents' fibroblasts (PMID:34322155).
  - Expressivity is **highly variable**, from isolated axonal neuropathy with a normal MRI to infantile encephalopathy, generalized dystonia, or adult-onset ataxia with parkinsonism.
  - Some genotypes recur: D6G homozygosity was seen with both childhood onset (Higuchi patient 1) and adult onset (Ouchi).
- **Anticipation and mosaicism.** None.
- **Prevalence.** Unknown, ultra-rare. Prevalence would be `measure_type: CASES_IN_LITERATURE` with `prevalence_class: ULTRA_RARE` or `RARE`.
  - Published count: Martinez Lyons 1; Higuchi 2018 4; Ban 2021 1; Tang 2022 1; Ouchi 2023 1; Higuchi 2023 3 new (giving 7 Japanese patients in that series); Cicala 2026 2 siblings. That is **about 11–13 individuals**, plus an unknown number in a 2026 Turkish hereditary-polyneuropathy cohort (Avcı et al., PMID:42552261).
  - **Possible double count:** the Ouchi 2023 patient (homozygous D6G, levodopa-responsive parkinsonism) and Higuchi 2023 patient 2 (ataxia, neuropathy and parkinsonism with a slight levodopa response) are both Japanese. Check whether they are the same person before counting.
  - **Sex discrepancy in the literature:** Martinez Lyons describe their patient as a 19-year-old **woman**, but Ban et al.'s summary table lists that patient as **M**. Use the primary report.
- **Diagnostic yield.** 4 of 1,396 in a Japanese inherited-neuropathy / CMT series (~0.3%) (PMID:29718187): "identified four unrelated patients with recessive mutations in COA7 among a Japanese case series of 1396 patients."
- **Populations.** Japanese (most patients, recurrent D6G), Chinese (2), Italian (Martinez Lyons; Cicala siblings), Turkish (2026 cohort).
- **Carrier frequency and sex ratio.** Carrier frequency is unknown. The sex ratio is roughly balanced (M ≈ F).

---

## 10. Diagnostics

- **Genetic testing (first line).** Exome or genome sequencing, or ataxia/CMT gene panels that include *COA7*.
  - Add **CNV/MLPA** when only one heterozygous variant is found, because the exon 2 deletion was missed by sequencing (PMID:29718187).
  - Trio sequencing helps establish phase.
  - Sequence mtDNA to exclude mtDNA COX defects (done in PMID:34322155).
- **Electrophysiology.** Nerve conduction studies show an axonal sensorimotor neuropathy. Lower-limb CMAPs and SNAPs are absent or severely reduced, and median motor conduction velocity is near normal (49.6–51.5 m/s). One patient had a mixed axonal-demyelinating picture (PMID:27683825).
- **Imaging.**
  - Brain MRI: cerebellar atrophy; ± white-matter T2 hyperintensity or cavitation; ± cerebral atrophy.
  - Spinal MRI: cord atrophy.
  - DaT SPECT (¹²³I-ioflupane) when parkinsonism is present; MIBG was normal in the reported case.
- **Biochemistry.**
  - Respiratory-chain enzyme assays in fibroblasts, muscle or skin show isolated complex IV deficiency.
  - BN-PAGE shows reduced assembled CIV.
  - Fibroblast results can be normal (PMID:35603692), so muscle is preferred.
  - Serum and CSF lactate; CK.
  - Relevant LOINC targets: lactate in serum/plasma and CSF, creatine kinase. Bind the LOINC Part or panel codes after a lookup.
- **Pathology.**
  - Sural nerve: chronic axonal degeneration with loss of large and medium myelinated fibres.
  - Muscle: ragged-red, COX-negative and SDH-increased fibres.
- **Differential diagnosis.**
  - SCAN1 (*TDP1*); AOA1 (*APTX*); AOA2/SCAN2 (*SETX*), which have oculomotor apraxia and raised AFP, both absent in SCAN3.
  - Friedreich ataxia (*FXN*); ataxia-telangiectasia.
  - *POLG*-related ataxia-neuropathy; other COX-assembly disorders (*SCO2*, *COA8*/APOPT1 cavitating leukoencephalopathy, *COX18*-related neuropathy, PMID:40830826).
  - Axonal CMT types; *SACS* (ARSACS); *PNPLA6*.
- **Clinical criteria.** None standardized.
- **Screening.** No newborn screening. Carrier and cascade testing are possible in families with known variants.

---

## 11. Outcome and prognosis

- Survival into the 7th decade is documented (Higuchi patient 1, aged 63).
- The infantile encephalopathic form (Ban 2021, last seen at 2 y) and the form with respiratory failure and feeding difficulty (Higuchi 2023 patient 3) suggest worse outcomes at the severe end. No mortality data exist.
- Morbidity comes from progressive loss of mobility (wheelchair or orthoses), falls, dysarthria and mild cognitive impairment.
- No prognostic biomarkers or validated QoL data exist.
- Possible negative prognostic signs, from anecdote only: infantile onset, leukoencephalopathy, cardiac involvement.

---

## 12. Treatment

**There is no disease-modifying therapy.** Management is supportive.

| Intervention | Candidate NCIT | Evidence |
|---|---|---|
| Physical therapy and rehabilitation; orthoses (AFOs) | NCIT:C15302 Physical Therapy; NCIT:C15315 Rehabilitation | standard care; AFO use reported (PMID:27683825) |
| Orthopedic management of foot deformity and scoliosis | NCIT:C16186 Orthopedic Surgical Procedure (only if surgery is documented) | not specifically reported |
| Levodopa for parkinsonism | NCIT:C15986 Pharmacotherapy + `therapeutic_agent` levodopa (CHEBI:15765, verify) | improved parkinsonism (PMID:37264311); slight improvement (PMID:37750949) |
| Baclofen for spasticity | NCIT:C15986 + baclofen (CHEBI, verify) | partial control (PMID:34322155) |
| Protirelin tartrate (TRH analogue) for ataxia | NCIT:C15986 + agent (verify) | slight, transient improvement, then decline (PMID:29718187) |
| Mitochondrial "cocktail" (CoQ10, riboflavin, etc.) | NCIT:C15747 Supportive Care | no COA7-specific data; do not assert efficacy |
| Genetic counseling | NCIT:C15240 Genetic Counseling | standard |

**Experimental and preclinical.**
- Proteasome inhibitors (MG132 in HEK293; **bortezomib, carfilzomib** in patient fibroblasts) rescued COA7 mitochondrial localization and raised complex IV activity by about 35% (PMID:30885959): "proteasome inhibition rescued both the mitochondrial localization of COA7 and complex IV activity."
- This is **IN_VITRO only**. Clinical use is limited by proteasome-inhibitor toxicity, including bortezomib-induced peripheral neuropathy, which is a direct concern in this disease. No clinical trials were found.
- Gene therapy, ASO, cell therapy: none.
- Pharmacogenomics: none.

---

## 13. Prevention

- **Primary.** Genetic counseling for carrier couples; preimplantation or prenatal diagnosis once familial variants are known.
- **Secondary.** Early genetic diagnosis in children with axonal neuropathy plus ataxia.
- **Tertiary.**
  - Physical therapy and orthotics.
  - Avoid neurotoxic drugs, especially those that cause neuropathy. This is general mitochondrial-disease advice and not COA7-specific evidence.
  - Prompt management of intercurrent illness.
- **Vaccines, prophylaxis and public-health measures:** not applicable.

---

## 14. Other species and natural disease

- **Natural animal disease.** None reported. No OMIA entry was found.
- **Orthologs.** COA7 is conserved across metazoans but **absent from yeast** (PMID:27683825). Orthologs: mouse *Coa7*; Drosophila *dCOA7* (CG?, check the FlyBase ID; FlyBase FBrf0238967 refers to the Higuchi 2018 paper).

---

## 15. Model organisms

| Model | Type | Phenotype | Recapitulation | Source |
|---|---|---|---|---|
| *Drosophila melanogaster* neuron- or eye-specific *dCOA7* RNAi knockdown (NCBITaxon:7227) | invertebrate genetic knockdown | rough eye (ommatidial fusion, bristle loss); median lifespan 43/40 d vs 51 d; age-dependent climbing defect; larval NMJ branch length 38 vs 77 µm | PARTIALLY_RECAPITULATES the motor-neuron/axonal degeneration node. Limitations: knockdown, not patient alleles; no cerebellum homologue; complex IV not measured in flies | PMID:29718187 ("showed rough eye phenotype, reduced lifespan, impaired locomotive ability") |
| Patient fibroblasts (immortalized mt4229i; others) | IN_VITRO | isolated CIV deficiency, reduced assembly, rescue by WT COA7 and by proteasome inhibition | RECAPITULATES the biochemical node; no neuronal context (BOUNDARY_OMISSION) | PMID:27683825; PMID:30885959; PMID:34322155 |
| COA7-knockout human cell lines (HEK293-derived) | IN_VITRO | CIV assembly stalled after the COX1 module | MEASURES the assembly node | PMID:35210360 |
| Mouse / zebrafish | — | **No published Coa7 knockout phenotype found.** Only commercial catalogue lines exist. | knowledge gap | — |

**Suggested knowledge gaps.** No vertebrate model; no iPSC-derived motor-neuron or cerebellar model; the basis of the selective neuronal vulnerability; why fibroblast CIV is normal in some patients. A `HUMAN_MODEL_MISMATCH` discussion is not warranted yet because there is no model that diverges from the human picture.

---

## Key references (verified in this session via Europe PMC/PMC)

| PMID | Citation | Evidence type |
|---|---|---|
| 27683825 | Martinez Lyons A et al. COA7 (C1orf163/RESA1) mutations associated with mitochondrial leukoencephalopathy and cytochrome c oxidase deficiency. *J Med Genet* 2016;53:846–849 | HUMAN_CLINICAL + IN_VITRO |
| 29718187 | Higuchi Y et al. Mutations in COA7 cause spinocerebellar ataxia with axonal neuropathy. *Brain* 2018;141:1622–1636 | HUMAN_CLINICAL + IN_VITRO + MODEL_ORGANISM (split items) |
| 30885959 | Mohanraj K et al. Inhibition of proteasome rescues a pathogenic variant of respiratory chain assembly factor COA7. *EMBO Mol Med* 2019;11:e9561 | IN_VITRO |
| 34322155 | Ban R et al. Biallelic COA7-variants leading to developmental regression with progressive spasticity and brain atrophy in a Chinese patient. *Front Genet* 2021;12:685035 | HUMAN_CLINICAL + IN_VITRO |
| 35210360 | Formosa LE et al. Mitochondrial COA7 is a heme-binding protein with disulfide reductase activity, which acts in the early stages of complex IV assembly. *PNAS* 2022;119:e2110357119 | IN_VITRO |
| 35603692 | Tang Y et al. A novel compound heterozygous mutation in the COA7 gene… SCAN3. *Clin Neuropathol* 2022;41:202–210 | HUMAN_CLINICAL |
| 37264311 | Ouchi S et al. Parkinsonism in spinocerebellar ataxia with axonal neuropathy caused by adult-onset COA7 variants. *BMC Neurol* 2023;23:211 | HUMAN_CLINICAL |
| 37750949 | Higuchi Y et al. Dystonia and parkinsonism in COA7-related disorders: expanding the phenotypic spectrum. *J Neurol* 2024;271:419–430 | HUMAN_CLINICAL |
| 42182620 | Cicala G et al. Compound heterozygous COA7 variants presenting with childhood-onset axonal neuropathy in 2 siblings. *Neurol Genet* 2026;12(3):e200394 | HUMAN_CLINICAL |
| 40830826 | Armirola-Ricaurte C et al. Biallelic variants in COX18 cause a mitochondrial disorder primarily manifesting as peripheral neuropathy. *Brain* 2026 (differential diagnosis or related complex IV assembly neuropathy) | HUMAN_CLINICAL |
| 42552261 | Avcı Ş et al. Hereditary polyneuropathy experience of a tertiary single-center in Türkiye. *Clin Genet* 2026 (includes COA7 case(s); details not retrieved) | HUMAN_CLINICAL |

**Curation notes**
- The quoted strings above come from abstracts as returned by Europe PMC, but some were relayed through a summarizing fetch tool. **Run `just fetch-reference` and `just count-verified-snippets` on each before using it as an exact snippet.**
- The existing `kb/disorders/Spinocerebellar_Ataxia_Autosomal_Recessive_With_Axonal_Neuropathy_3.yaml` is a 25-line stub with only MONDO and one HP term, so almost everything here is new content.

Sources:
- [Higuchi 2018, Brain (PMC5972596)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5972596)
- [Martinez Lyons 2016, J Med Genet (PMC5264227)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5264227)
- [Mohanraj 2019, EMBO Mol Med (PMC6505684)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6505684/)
- [Ban 2021, Front Genet (PMC8312223)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8312223)
- [Formosa 2022, PNAS (PMC8892353)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8892353)
- [Formosa bioRxiv preprint](https://www.biorxiv.org/content/10.1101/2021.06.10.447992.full.pdf)
- [Higuchi 2023, J Neurol (PMC10769979)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10769979/)
- [Ouchi 2023, BMC Neurol (PMC10234071)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10234071/)
- [Europe PMC search results (Cicala 2026, Tang 2022, Avcı 2026, COX18 2026)](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=COA7%20AND%20(ataxia%20OR%20dystonia%20OR%20neuropathy%20OR%20leukoencephalopathy%20OR%20heme%20OR%20proteasome)&resultType=core&format=json&pageSize=30)
- [MONDO:0020770 via OLS](https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?obo_id=MONDO:0020770)
- [MalaCards SCAN3](https://www.malacards.org/card/spinocerebellar_ataxia_autosomal_recessive_with_axonal_neuropathy_3)
- [KEGG H02573](https://www.kegg.jp/entry/H02573)
- [GenCC submission](https://thegencc.org/submissions/SGC-107318.2)
- [PanelApp COA7](https://e2e-nhsgms-panelapp.genomicsengland.co.uk/entities/COA7)
- [Alliance COA7](https://alliancegenome.org/gene/HGNC:25716)
- [RCSB 7MQZ](https://www.rcsb.org/structure/7MQZ)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 6 |
| Quoted claims found in source | 6 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 18 |
| On topic | 17 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 77 |
| Resolved | 74 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 3 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0020770` (5 mentions) - the report calls it "MONDO"; MONDO calls it **spinocerebellar ataxia, autosomal recessive, with axonal neuropathy 3**
- `DOID:0070465` (1 mention) - the report calls it "DOID"; DOID calls it **autosomal recessive spinocerebellar ataxia with axonal neuropathy 3**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005751` (obsolete mitochondrial respiratory chain complex IV) (1 mention) - replaced by `GO:0045277`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `NCBITaxon:7227` (1 mention) - the report calls it "Drosophila melanogaster* neuron- or eye-specific *dCOA7* RNAi knockdown"; NCBITaxon calls it **Drosophila melanogaster**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `GARD`.