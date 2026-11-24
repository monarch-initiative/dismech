---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-11-23T17:32:20.106421'
end_time: '2026-11-23T17:52:10.346617'
duration_seconds: 1190.24
template_file: templates/disease_pathophysiology_research.md
template_sha: f452f0a9c7e3536175154b9683c45663f686f283
template_variables:
  disease_name: Desmoplastic Myxoid Tumor of the Pineal Region, SMARCB1-Mutant
  mondo_id: MONDO:1060253
  category: Cancer
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: desmoplastic myxoid tumor, SMARCB1-mutant
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
  web_search_requests: 8
  num_turns: 100
  total_cost_usd: 6.411479499999997
  session_id: 6e2e6c1e-68e3-4859-ba8c-5b42e2d4ee25
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  tool_calls: 99
  retrieval_calls: 97
  assistant_text_blocks: 1
citation_count: 23
term_validation:
  total_terms: 51
  verified: 50
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:1060253
    reported_labels:
    - if available
    - desmoplastic myxoid tumor of the pineal region, SMARCB1-mutant
    - MONDO
    ontology_label: desmoplastic myxoid tumor of the pineal region, SMARCB1-mutant
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Desmoplastic Myxoid Tumor of the Pineal Region, SMARCB1-Mutant
- **MONDO ID:** MONDO:1060253 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** desmoplastic myxoid tumor, SMARCB1-mutant
- **Category:** Cancer

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Desmoplastic Myxoid Tumor of the Pineal Region, SMARCB1-Mutant** covering all of the
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

# Desmoplastic Myxoid Tumor of the Pineal Region, *SMARCB1*-Mutant (MONDO:1060253)
## Comprehensive Disease Characteristics Research Report

**Report date:** 23 November 2026
**Target entity:** MONDO:1060253 — desmoplastic myxoid tumor of the pineal region, SMARCB1-mutant
**Causal gene:** ***SMARCB1*** (HGNC:11103; NCBI Gene 6598; OMIM *601607; 22q11.23)

**Interpretation / scope statement.** The disease template listed "causal gene(s): not recorded." Retrieval confirms the entity is defined by biallelic inactivation of **SMARCB1** (also called *INI1*, *SNF5*, *BAF47*), and the entity name itself carries the gene. This report therefore treats *SMARCB1* as the causal gene throughout. Because this is an extremely rare tumor type first delineated in 2020 (~15–19 published cases worldwide), many template fields (prevalence, 5-year survival, quality-of-life instruments, gene–environment interaction, protective factors, animal models of the specific disease) **have no retrievable primary evidence**. Those sections state the gap explicitly rather than extrapolating. Where I rely on mechanism demonstrated in the closely related *SMARCB1*-deficient rhabdoid tumors rather than in DMT itself, this is labeled as **inferred/extrapolated**.

---

## 1. Disease Information

### 1.1 Overview

Desmoplastic myxoid tumor (DMT) of the pineal region, *SMARCB1*-mutant is a rare, newly recognized central nervous system neoplasm of adolescents and adults that arises in the pineal region and is defined by inactivation of *SMARCB1* with loss of nuclear SMARCB1/INI1 protein, in the setting of **low-grade histology** — spindled and epithelioid cells in a desmoplastic (densely collagenized) stroma alternating with loose myxoid matrix — and a generally (but not uniformly) more indolent course than atypical teratoid/rhabdoid tumor (AT/RT).

The entity was established by a multi-institutional series of seven tumors reported by **Thomas et al., *Acta Neuropathologica* 2020;139(2):277–286 (PMID 31732806; DOI 10.1007/s00401-019-02094-w)**, whose abstract states verbatim:

> "Here we report seven SMARCB1-deficient intracranial tumors sharing distinct clinical, histopathological and molecular features. Median age of the four females and three males was 40 years (range 15-61 years). All tumors were located in the pineal region. Histopathologically, these tumors displayed spindled and epithelioid cells embedded in a desmoplastic stroma alternating with a variable extent of a loose myxoid matrix… We propose the designation desmoplastic myxoid tumor (DMT), SMARCB1-mutant, for these tumors."
> — https://pubmed.ncbi.nlm.nih.gov/31732806/

It was incorporated into the **fifth edition of the WHO Classification of Tumours of the Central Nervous System (WHO CNS5, 2021)** as one of five pineal tumour types. **Louis DN, Perry A, Wesseling P, et al. *Neuro-Oncology* 2021;23(8):1231–1251 (PMID 34185076; DOI 10.1093/neuonc/noab106)** states verbatim:

> "An addition to WHO CNS5 is *Desmoplastic myxoid tumor of the pineal region, SMARCB1-mutant*, a rare *SMARCB1*-mutant tumor lacking histopathological signs of malignancy."
> — https://pmc.ncbi.nlm.nih.gov/articles/PMC8328013/

The five WHO CNS5 pineal tumour types are pineocytoma; pineal parenchymal tumour of intermediate differentiation (PPTID); pineoblastoma; papillary tumour of the pineal region (PTPR); and desmoplastic myxoid tumour of the pineal region, *SMARCB1*-mutant (Louis 2021, PMC8328013; corroborated by **Lombardi G, et al. EURACAN overview, *Cancers* 2022;14(15):3646; PMID 35954310; DOI 10.3390/cancers14153646**).

### 1.2 Key identifiers (all retrieved this session)

| Resource | Identifier | Label / notes |
|---|---|---|
| **MONDO** | MONDO:1060253 | "desmoplastic myxoid tumor of the pineal region, SMARCB1-mutant"; IRI http://purl.obolibrary.org/obo/MONDO_1060253; term tracker https://github.com/monarch-initiative/mondo/issues/10359 (EBI OLS4) |
| **NCIT** | C178507 | "Desmoplastic Myxoid Tumor of the Pineal Region, SMARCB1-Mutant" (EBI OLS4) |
| **UMLS CUI** | C5555093 | MONDO xref (EBI OLS4) |
| **MedGen** | 1791534 | MONDO xref (EBI OLS4) |
| **Causal gene** | HGNC:11103 / Gene 6598 / Ensembl ENSG00000099956 / OMIM *601607 | *SMARCB1*, 22q11.23, GRCh38 chr22:23,786,965–23,838,008 (+) (NCBI Gene efetch) |
| **OMIM (disease)** | **None for DMT itself.** Related: #609322 rhabdoid tumor predisposition syndrome 1 (RTPS1), MONDO:0012252, GTR GTRT000005873 (NCBI MedGen UID 322892) |
| **Orphanet** | No DMT-specific ORPHA code retrieved in this session |
| **ICD-O** | **No ICD-O code assigned** in WHO CNS5 per secondary sources; *not independently verified* against the WHO blue book in this session. Comparator pineal codes cited by the same secondary sources: pineocytoma 9361/1, pineoblastoma 9362/3 |
| **ICD-11** | No DMT-specific code retrieved; secondary web sources suggest coding under the pineal gland neoplasm category (2A00.2x) — **unverified** |
| **MeSH** | No dedicated MeSH descriptor. Thomas 2020 is indexed under *Pineal Gland*, *Rhabdoid Tumor (genetics, pathology)*, *Brain Neoplasms (genetics)*, *SMARCB1 Protein (genetics)*, *Mutation* (Europe PMC core record for PMID 31732806) |
| **CNS WHO grade** | **Not assigned.** Tauziède-Espariat et al. 2026 state verbatim: "no grading has been established so far" (PMID 42445896; PMC13359088) |

**MONDO definition (verbatim, EBI OLS4):**
> "A pineal body neoplasm that is a SMARCB1-deficient tumor of the brain, characterized by the presence of spindled and epithelioid cells with low-grade morphology that are embedded in a desmoplastic stroma alternating with various extents of loose myxoid matrix."

**NCIT C178507 definition (verbatim, EBI OLS4):**
> "A SMARCB1-deficient tumor of the brain arising in the pineal region. It is characterized by the presence of spindled and epithelioid cells with low-grade morphology that are embedded in a desmoplastic stroma alternating with various extents of loose myxoid matrix."

### 1.3 Synonyms and alternative names (retrieved)

- desmoplastic myxoid tumor, *SMARCB1*-mutant (MONDO exact synonym; original designation of Thomas et al. 2020)
- desmoplastic myxoid tumour of the pineal region, *SMARCB1*-mutant (WHO CNS5 British spelling; Louis 2021)
- **DMT, *SMARCB1* mutant** / **DMT-SMARCB1** (abbreviation used by Chang et al. 2026, PMID 42467229; Manoranjan et al. 2021, PMID 37284622)
- **DMTPR** — "desmoplastic myxoid tumor of the pineal region" (Kinoshita Y, et al. *Ann Clin Lab Sci* 2026;56(2):232–238; PMID 42259547)
- "SMARCB1-mutant desmoplastic myxoid tumour" (Bakhshi SK, et al. *J Pak Med Assoc* 2024;74(3 Suppl-3):S135–S144; PMID 39262074)

### 1.4 Provenance of information (individual-patient vs aggregated)

**Essentially all knowledge is individual patient-level**, from one 7-patient multi-institutional retrospective series (PMID 31732806) plus ~10–12 single-patient or two-patient reports. There is **no EHR-derived cohort, no registry entry, and no population-based (SEER/CBTRUS) breakout for this entity** — the CBTRUS 2017–2021 statistical report (Price M, et al. *Neuro-Oncology* 2024;26(Suppl 6):vi1–vi85; PMID 39371035; DOI 10.1093/neuonc/noae145) contains no pineal-region-specific or DMT-specific incidence data. MONDO and NCIT entries are literature-curated, not patient-derived.

---

## 2. Etiology

### 2.1 Disease causal factors

**Primary cause: biallelic somatic inactivation of *SMARCB1*** (genetic/epigenetic-mechanistic). Thomas et al. 2020 (PMID 31732806) documented, verbatim:

> "All cases showed loss of nuclear SMARCB1/INI1 protein expression… Three cases displayed heterozygous SMARCB1 deletions and two cases a homozygous SMARCB1 deletion. On sequencing, one tumor showed a 2 bp deletion in exon 4 (c.369_370del) and one a short duplication in exon 3 (c.237_276dup) both resulting in frameshift mutations."

The review by **Pasquinelli E, Guidi M, Sardi I. *Neuro-Oncology Advances* 2026;8(1):vdag086 (PMID 42058762; DOI 10.1093/noajnl/vdag086; PMC13124280)** summarizes this as "consistent with biallelic inactivation of *SMARCB1*," with "Loss of chromosome 22q, observed as a focal deletion in the majority of evaluable cases."

No infectious, radiation, chemical, or other exogenous cause has been proposed or tested for this entity (no retrievable evidence either way).

### 2.2 Risk factors

**Genetic:**
- *SMARCB1* loss-of-function alterations are the obligate driver (somatic in all cases where origin was addressed). *SMARCB1* is extremely intolerant of loss of function in the population: gnomAD constraint **pLI = 0.99999998, o/e LoF = 0.102 (upper bound 0.214)** (gnomAD API, GRCh38, ENSG00000099956).
- **Germline predisposition:** rhabdoid tumor predisposition syndrome 1 (RTPS1; OMIM #609322, MONDO:0012252) is caused by heterozygous germline *SMARCB1* pathogenic variants (NCBI MedGen 322892). **However, no germline *SMARCB1* variant has been reported in a DMT patient in any source retrieved here.** A dedicated PubMed search ("desmoplastic myxoid" AND germline OR predisposition) returned a single record — the Pasquinelli review — in which "No germline predisposition established for DMT specifically" (PMC13124280). This is an **evidence gap, not evidence of absence**: the SIOPE Host Genome Working Group recommends that "patients with 'SMARCB1-deficient non-RT neoplasms' should be offered genetic testing on a research basis and, if positive for a PV, cancer surveillance" (**Frühwald MC, Nemes K, Boztug H, et al. *Fam Cancer* 2021;20(4):305–316; PMID 33532948; DOI 10.1007/s10689-021-00229-1; PMC8484234**).

**Demographic (age, sex):**
- Age is a risk/distribution factor: all reported patients are adolescents or adults, **15–61 years**; medians reported across censuses are 40 years (n=7; PMID 31732806), 33 years (PMID 42445896), mean 36.6 years (n=10; PMID 35195707), mean 39 years (n=11; PMID 39586083), mean 34.9 years (n=11; PMID 38527786). Zhou et al. note "**No pediatric cases reported**" (PMC11605529).
- Modest **female predominance**: 7F:4M across the first 11 cases (PMID 39586083/PMC11605529); "a slight female predominance (F: 7; M: 4)" (Robinson et al., PMC11007021).

**Environmental / lifestyle / occupational / infectious:** **No retrievable evidence.** No study has examined toxins, radiation, diet, smoking, alcohol, occupation, or infectious agents in relation to DMT. CTD/TOXNET-type exposure associations for this entity were not found.

### 2.3 Protective factors

**None identified.** No protective genetic variants, modifier alleles, dietary, or lifestyle factors have been reported for DMT. (Note: one *iatrogenic risk* signal exists — see §11, aggressive recurrence after ventriculoperitoneal shunting and Gamma Knife radiosurgery, PMID 42467229 — but this is a single observation, not an established causal factor.)

### 2.4 Gene–environment interactions

**No data.** No gene–environment interaction has been studied or proposed for DMT-SMARCB1.

---

## 3. Phenotypes

All phenotype data come from individual case reports. Frequencies below are counts over the small published literature and should be read as **qualitative**, not epidemiologic rates.

### 3.1 Presenting symptoms and signs

| Phenotype | Suggested HPO term (verified via OLS4) | Type | Evidence / frequency | Onset, severity, course |
|---|---|---|---|---|
| **Headache** | HP:0002315 Headache | Symptom | Reported in most cases: 33M "headaches, dizziness, nausea, vomiting, and blurred vision" (PMID 32901946); 50F "sudden headache and dizziness" (PMID 39586083); 24F "headaches, nausea, and emesis" (PMID 37284622); 18F "subacute, progressive headaches" (PMC11007021) | Adult onset; subacute to acute; progressive until decompression |
| **Nausea / vomiting** | HP:0002018 (nausea) / HP:0002013 (vomiting) — *note: these two IDs were not individually verified in this session; "Headache" HP:0002315 was* | Symptom | PMID 32901946; PMID 37284622 | Secondary to raised ICP |
| **Noncommunicating (obstructive) hydrocephalus** | **HP:0010953 Noncommunicating hydrocephalus** (verified) | Clinical sign / imaging | Very frequent — "Imaging studies showed a pineal region mass with obstructive hydrocephalus" (PMID 39586083); "obstructive hydrocephalus requiring ventriculoperitoneal shunt placement" (PMC11007021); "space-occupying lesion in the pineal region with obstructive hydrocephalus" (PMC13359088); ETV performed in 2/10 cases (PMID 35195707) | Subacute; moderate-to-severe; reversible with CSF diversion |
| **Increased intracranial pressure** | **HP:0002516 Increased intracranial pressure** (verified) | Clinical sign | "symptoms consistent with raised intracranial pressure" (PMC13359088) | Progressive; can be life-threatening |
| **Parinaud / dorsal midbrain syndrome — vertical supranuclear gaze palsy** | **HP:0000511 Vertical supranuclear gaze palsy** (verified; OLS4 returns this for "Parinaud syndrome") | Clinical sign | "paralysis of upward gaze… clinically combined with typical Parinaud's syndrome" (PMID 39586083); a dedicated report: **Koren TJ, Back M, Chen J, Ahmad K. "Desmoplastic myxoid tumor of the pineal region presenting with Parinaud syndrome." *J Neuropathol Exp Neurol* 2026;85(3):303–305 (PMID 40834270; DOI 10.1093/jnen/nlaf096)** | Subacute; partially reversible — "mild improvement in eye movement abnormalities" at 6 months post-resection (PMC11605529) |
| **Blurred vision / visual loss** | HP:0000622 Blurred vision (ID not verified this session) | Symptom | "blurred vision" (PMID 32901946); "an acute episode of sudden vision loss" (PMC11007021) | Acute or subacute |
| **Vertigo / dizziness** | HP:0002321 Vertigo (ID not verified this session) | Symptom | PMID 32901946; PMID 39586083 | — |
| **Drowsiness / somnolence** | HP:0002329 Somnolence (ID not verified this session) | Behavioral/neurologic | "progressive drowsiness" (PMC11605529) | Progressive; a red flag for decompensating hydrocephalus |
| **Pineal region mass** | **HP:0010799 Pinealoma** / **HP:0012680 Abnormality of the pineal gland** / **HP:0030693 Supratentorial neoplasm** (all verified) | Imaging/structural | 100% by definition — "All tumors were located in the pineal region" (PMID 31732806) | — |
| **Intratumoral hemorrhage** | — | Pathology/imaging | "extensive hemorrhage, necrosis, and inflammatory infiltration" on histology; "intraventricular hemorrhage" on imaging (PMC11605529; PMC13359088) | Variable |
| **Leptomeningeal / CSF dissemination** | — | Complication | Minority: CSF dissemination in 1 case (PMID 35195707); "focal leptomeningeal dissemination" (PMID 42467229); "subependymal nodule and corpus callosum infiltration" at late relapse (PMC13359088) | Late; severe; progressive |
| **Papilledema** | **HP:0001085 Papilledema** (verified) | Clinical sign | Expected with raised ICP but **not explicitly documented** in the retrieved case descriptions — listed as plausible, not evidenced |

### 3.2 Phenotype characteristics (aggregate)

- **Age of onset:** adolescent to late-adult (15–61 y). No congenital, neonatal, or childhood cases (PMC11605529).
- **Onset pattern:** subacute-to-acute, driven by aqueductal obstruction rather than by tumor infiltration. One case had symptom onset over "three days" (PMC11605529).
- **Severity:** moderate-to-severe at presentation (hydrocephalus, gaze palsy, drowsiness), but **usually fully or largely reversible** after resection and CSF diversion.
- **Progression:** mass-related symptoms are progressive until decompressed; disease course thereafter ranges from years of stability to late dissemination and death (see §8, §11).

### 3.3 Quality-of-life impact

**No disease-specific QoL data exist.** No EQ-5D, SF-36, PROMIS, or neuro-oncology-specific (e.g., EORTC QLQ-BN20) measurements have been reported for DMT-SMARCB1 in any retrieved source. Functional impact must be inferred from the phenotype set: durable diplopia/upgaze palsy affects reading and driving; shunt dependence imposes lifelong device-failure risk; and the two patients with dissemination required craniospinal irradiation or chemotherapy with their attendant morbidity (PMID 35195707; PMC13359088). This is an explicit **gap**.

---

## 4. Genetic / Molecular Information

### 4.1 Causal gene

**SMARCB1** — "SWI/SNF related BAF chromatin remodeling complex subunit B1" (NCBI Gene 6598; HGNC:11103; Ensembl ENSG00000099956; OMIM *601607; chromosome **22q11.23**, GRCh38 chr22:23,786,965–23,838,008, plus strand). Aliases retrieved from NCBI Gene: **RDT, CSS3, INI1, SNF5, Snr1, BAF47, INI-1, MRD15, RTPS1, Sfh1p, hSNFS, SNF5L1, SWNTS1, PPP1R144**.

NCBI Gene summary (verbatim):
> "The protein encoded by this gene is part of a complex that relieves repressive chromatin structures, allowing the transcriptional machinery to access its targets more effectively. The encoded nuclear protein may also bind to and enhance the DNA joining activity of HIV-1 integrase. This gene has been found to be a tumor suppressor, and mutations in it have been associated with malignant rhabdoid tumors."

No second causal gene is known. (By contrast, AT/RT can be driven by *SMARCA4/BRG1* — "biallelic inactivation of SWI/SNF chromatin remodeling complex members SMARCB1/INI1 or (rarely) SMARCA4/BRG1" — **Hasselblatt M, Kool M, Frühwald MC. *Clin Neuropathol* 2024;43(1):2–9; PMID 37969088; DOI 10.5414/NP301594**. No *SMARCA4*-driven DMT has been reported.)

### 4.2 Pathogenic variants reported in DMT (complete list retrieved)

| Variant / alteration | Type | Zygosity | Case | Source |
|---|---|---|---|---|
| *SMARCB1* **heterozygous deletion** | Structural / CNV loss | Het (3 cases) | Thomas series | PMID 31732806 |
| *SMARCB1* **homozygous deletion** | Structural / CNV loss | Hom (2 cases) | Thomas series | PMID 31732806 |
| **c.369_370del** (exon 4, 2 bp deletion) | Frameshift indel | not stated | 1 Thomas case | PMID 31732806 |
| **c.237_276dup** (exon 3, 40 bp duplication) | Frameshift duplication | described as homozygous by Pasquinelli | 1 Thomas case | PMID 31732806; PMC13124280 |
| *SMARCB1* **deletion** (copy-number) | CNV loss | not specified | 24F Calgary case | PMID 37284622 |
| *SMARCB1* **homozygous deletion** | CNV loss | Hom | 33M Paris case | PMC13359088 |
| **c.91G>A (p.Glu31Lys; "E31K")** | **Missense** | not stated | 18F Utah case; classified as **variant of unknown clinical significance** | PMC11007021 |

**Variant classification:** none of the DMT-specific variants has a published ACMG/AMP 5-tier classification apart from the E31K missense, explicitly reported as a **VUS** ("a variant of unknown clinical significance involving the SMARCB1 gene c.91G>A (p.Glu31Lys) E31K", PMC11007021). Robinson et al. emphasize the novelty of a point mutation in this entity: "previous reported DMTs were mainly inactivated by homozygous or heterozygous deletions or indels rather than point mutations" (PMC11007021). For context, ClinVar holds **1,600 records** for *SMARCB1*[gene] (NCBI eSearch, db=clinvar, retrieved this session); I did not retrieve per-variant ClinVar classifications for the DMT variants above, and **none of them was confirmed to be present in ClinVar in this session.**

**Allele frequency in population databases:** these are **somatic tumor variants**; no population allele frequencies apply. Gene-level population constraint (gnomAD, GRCh38): pLI 0.99999998, o/e LoF 0.102 (90% upper 0.214) — i.e., *SMARCB1* LoF is essentially absent from the general population, consistent with a haploinsufficient tumor suppressor.

**Somatic vs germline:** all documented alterations are **somatic/tumor-restricted**; no germline *SMARCB1* alteration has been reported in DMT (see §2.2). COSMIC/TCGA/ICGC do not contain a DMT tumor type (not retrievable as a distinct cohort).

**Functional consequence:** **loss of function** (complete loss of nuclear SMARCB1/INI1 protein by IHC in 100% of reported cases — PMID 31732806; PMID 33420834; PMID 41259279; PMID 42467229; PMC13359088). Mechanistically this is a loss-of-function of a core SWI/SNF subunit rather than a gain-of-function or dominant-negative event (see §6).

### 4.3 Modifier genes

**None identified.** No modifier locus has been reported. Candidate prognostic co-factors in DMT are phenotypic (Ki-67, rhabdoid cytology, extent of resection), not genetic.

### 4.4 Epigenetic information

This entity is, in effect, **epigenetically defined**:

- **DNA methylation class.** Thomas et al. 2020 (verbatim): "Most DNA methylation profiles were not classifiable using the Heidelberg Brain Tumor Classifier (version v11b4). By unsupervised t-SNE analysis and hierarchical clustering analysis, however, all tumors grouped closely together and showed similarities with ATRT-MYC" (PMID 31732806).
- Later classifier development: Tauziède-Espariat et al. 2026 report their case was "classified as DMT using **NIH classifier v2.0 with calibrated score of 0.84**" while "Not classified by **DKFZ classifier v12.8** (as DMT is absent from this classifier)" (PMID 42445896; PMC13359088). Robinson et al.'s case was confirmed by "**Methylation profiling… with 0.99 confidence score**" (PMC11007021).
- Pasquinelli et al. 2026 (verbatim): "Desmoplastic myxoid tumor of the pineal region, SMARCB1-mutant forms a **distinct and compact methylation cluster, clearly separated from established CNS tumor entities**" and such tumors "**segregate away from the major AT/RT methylation subgroups**" (PMC13124280).
  - **Note a real discrepancy in the literature:** the index series emphasized epigenetic *similarity* to ATRT-MYC (PMID 31732806), whereas the 2026 review emphasizes *separation* from AT/RT subgroups (PMC13124280), and the 2026 aggressive case reported "molecular proximity to other SMARCB1-deficient central nervous system neoplasms" (PMID 42467229). The best current reading: DMT forms its own tight methylation cluster that sits nearest the SMARCB1-deficient neighborhood (with ATRT-MYC and poorly differentiated chordoma as the closest neighbors — the latter similarity noted by **Wang YE, et al. *Neuropathology* 2021;41(1):37–41; PMID 32901946**: "epigenetic features similar to those of atypical teratoid/rhabdoid tumors (AT/RT)-MYC and poorly differentiated chordomas").
- **Downstream chromatin consequences** (extrapolated from rhabdoid tumor models — see §6): loss of SWI/SNF-mediated enhancer H3K27 acetylation and a reciprocal gain of PRC2/EZH2-mediated H3K27 trimethylation at polycomb targets.
- No ENCODE/Roadmap/DiseaseMeth entry exists for DMT; and a GEO dataset search ("desmoplastic myxoid SMARCB1") returned **zero** datasets this session.

### 4.5 Chromosomal abnormalities

- **Focal 22q loss encompassing the *SMARCB1* locus** — "Loss of chromosome 22q, observed as a focal deletion in the majority of evaluable cases" (PMC13124280, summarizing PMID 31732806).
- Additional copy-number losses reported on **2q, 12q, 16, 17, and 9q**; "gains uncommon" (PMC13124280).
- Genomes are otherwise quiet; one case had "no pathogenic mutations or fusions" on a brain tumor panel beyond the *SMARCB1* VUS (PMC11007021). This mirrors rhabdoid tumors, which "are among the most genomically stable" (**Wang X, et al. *Nat Genet* 2017;49(2):289–295; PMID 27941797**).
- No recurrent translocation or aneuploidy pattern. No DECIPHER/ECARUCA entry for DMT.

---

## 5. Environmental Information

- **Environmental factors:** **No evidence.** No toxin, radiation, pollution, or occupational exposure has been linked to DMT-SMARCB1 in any retrieved source; no CTD association exists for this entity.
- **Lifestyle factors:** **No evidence.** No smoking, diet, exercise, or alcohol association has been studied.
- **Infectious agents:** **Not applicable / no evidence.** No pathogen has been implicated. (Of note, SMARCB1/INI1 was originally identified as an HIV-1 integrase-interacting protein — "may also bind to and enhance the DNA joining activity of HIV-1 integrase," NCBI Gene 6598 — but this is a biochemical property, **not** an etiologic link to DMT.)
- **One iatrogenic observation:** aggressive recurrence with leptomeningeal dissemination occurred "following ventriculoperitoneal shunt placement and Gamma Knife radiosurgery" in a 47-year-old woman (PMID 42467229). Whether this reflects shunt-mediated seeding, radiosurgical failure, or intrinsically aggressive biology is **not established** — the authors frame it as expanding the biological spectrum, not as a causal exposure.

---

## 6. Mechanism / Pathophysiology

### 6.1 Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic inactivation of *SMARCB1* at 22q11.23** occurs in a precursor cell within or adjacent to the pineal region — via focal 22q/`SMARCB1` deletion (heterozygous then second hit, or homozygous), frameshift indel (c.369_370del; c.237_276dup), or rarely missense (c.91G>A p.Glu31Lys) — **which leads to** complete absence of functional SMARCB1/INI1/BAF47 protein. *Demonstrated in human tumors*: 100% loss of nuclear SMARCB1 by IHC plus concordant copy-number/sequencing data (PMID 31732806; PMC13359088; PMID 41259279).
2. Absence of SMARCB1 **results in** loss of integrity and altered targeting of residual SWI/SNF (BAF) chromatin-remodeling complexes. *Demonstrated in SMARCB1-deficient rhabdoid tumor models (extrapolated to DMT)*: "SMARCB1 is required for the integrity of SWI/SNF complexes and… its loss alters enhancer targeting" (Wang X, et al. *Nat Genet* 2017;49(2):289–295; PMID 27941797; DOI 10.1038/ng.3746).
3. Altered targeting **leads to** collapse of typical, lineage-specific enhancers while super-enhancers are retained — "markedly impairing SWI/SNF binding to typical enhancers, particularly those required for differentiation, while maintaining SWI/SNF binding at super-enhancers" (PMID 27941797). SWI/SNF normally "interact[s] with p300 to modulate histone H3 lysine 27 acetylation" at distal lineage enhancers (**Alver BH, et al. *Nat Commun* 2017;8:14648; PMID 28262751; DOI 10.1038/ncomms14648**). *Inferred for DMT* — no DMT-specific ChIP-seq exists.
4. Collapse of differentiation enhancers **results in** a differentiation block and retention of "remnants of differentiation programs" (PMID 27941797), which in DMT manifests as an ambiguous, **polyphenotypic** immunophenotype (EMA+, CD34+, SMA+, with inconsistent synaptophysin/GFAP) rather than a clean lineage signature (PMID 31732806; PMID 41259279).
5. **Branch — epigenetic de-repression arm:** loss of SWI/SNF antagonism of Polycomb **leads to** elevated EZH2 and broad H3K27 trimethylation/repression of Polycomb target genes and activation of stem-cell programs. *Demonstrated in mouse/fibroblast models*: "loss of the SNF5 tumor suppressor leads to elevated expression of the Polycomb gene EZH2 and… Polycomb targets are broadly H3K27-trimethylated and repressed in SNF5-deficient fibroblasts and cancers… inactivation of Ezh2 blocks tumor formation driven by Snf5 loss" (**Wilson BG, et al. *Cancer Cell* 2010;18(4):316–328; PMID 20951942; DOI 10.1016/j.ccr.2010.09.006**). *Inferred for DMT.*
6. Steps 3–5 **result in** cell-cycle entry and clonal proliferation, i.e., transformation with a **genomically stable** genome (PMID 27941797; concordant with the quiet DMT copy-number profiles, PMC13124280).
7. **Branch — acquired dependency arm (therapeutically relevant):** SMARCB1 loss **leads to** increased incorporation of BRD9 into residual SWI/SNF, creating a non-canonical (ncBAF) sub-complex on which the tumor cell becomes dependent — "SMARCB1 loss causes increased BRD9 incorporation into SWI/SNF thus providing insight into BRD9 vulnerability in RTs" (**Wang X, et al. *Nat Commun* 2019;10(1):1881; PMID 31015438; DOI 10.1038/s41467-019-09891-7**; genome-wide CRISPR-Cas9 screen). *Inferred for DMT.*
8. The transformed cells **produce** abundant extracellular matrix — a loose, Alcian-blue-positive myxoid matrix alternating with dense collagenous/desmoplastic stroma, including "collagen fibers arranged in amianthoid patterns and crystalloids" and "irregular anastomosing collagenous structures" (PMC13359088; PMID 42259547; "abundant, Alcian-blue positive myxoid matrix," PMID 37284622). **The molecular basis of this matrix phenotype is unknown** — no mechanistic study exists; the morphology "may suggest a potential mesenchymal origin," yet "no cell of origin has been identified to date" (PMC13359088).
9. Low proliferative output (median Ki67/MIB1 **3%**, range <1% to 15.4%; PMID 31732806; PMC11605529) **results in** slow, expansile rather than infiltrative growth confined to the pineal region.
10. Expansion within the pineal recess **compresses the midbrain cerebral aqueduct**, which **leads to** noncommunicating hydrocephalus and raised intracranial pressure — "a space-occupying lesion in the pineal region with obstructive hydrocephalus" (PMC13359088; PMC11605529), **which causes** headache, nausea/vomiting, drowsiness, and visual obscuration.
11. In parallel, compression of the **dorsal midbrain/pretectal region leads to** Parinaud (dorsal midbrain) syndrome — upgaze paralysis (PMID 39586083; PMID 40834270).
12. **Branch — aggressive subset:** in a minority, tumors with rhabdoid cytology and/or higher Ki-67 **progress to** local recurrence and CSF/leptomeningeal dissemination, **leading to** death — "discohesive rhabdoid cells embedded within a prominent myxoid stroma… highlights the potential for aggressive biological behavior despite relatively low-grade histologic features" (PMID 42467229); late relapse with "subependymal nodule and corpus callosum infiltration" after 11 stable years (PMC13359088).

### 6.2 Category-by-category detail

**Molecular pathways.** The lesion is a **chromatin-remodeling pathway** defect, not a classical signaling-pathway defect. Pasquinelli et al. group DMT among pineal tumors whose oncogenic mechanisms include "**chromatin remodeling defects**," alongside "MYC/FOXR2-driven transcriptional amplification, PI3K/AKT/mTOR pathway activation" in other pineal entities (PMC13124280). Suggested GO terms (verified via OLS4): **GO:0006338 chromatin remodeling**; **GO:0016514 SWI/SNF complex**; **GO:0070603 SWI/SNF superfamily-type complex**; **GO:0140658 ATP-dependent chromatin remodeler activity**. The Polycomb arm (EZH2/PRC2, H3K27me3) is the principal downstream effector pathway (PMID 20951942). No Wnt, MAPK, mTOR, or PI3K-AKT alteration has been reported in DMT. No KEGG/Reactome pathway map is specific to this entity.

**Cellular processes.** Differentiation block and enhancer-landscape failure (PMID 27941797; PMID 28262751); de-repression of stem-cell-associated programs (PMID 20951942); cell-cycle dysregulation inferred from proliferation despite a quiet genome. Low apoptotic/necrotic activity is typical, though one case showed "extensive hemorrhage, necrosis, and inflammatory infiltration" (PMC11605529). Mitoses are characteristically absent or rare — "oval nuclei without atypia or mitosis" (PMC13359088); "Mitotic index was <1/10 high-power fields; necrosis was absent" (PMC11007021).

**Protein dysfunction.** Pure **loss of function** of SMARCB1/INI1/BAF47, a core BAF subunit. Deletions and frameshifts abolish the protein; the single reported missense (p.Glu31Lys) also produced IHC loss of nuclear expression in "many of the tumor cells" (PMC11007021), implying destabilization rather than a dominant-negative mechanism — though this was not functionally assayed. No misfolding/aggregation mechanism is implicated. Relevant GO cellular component: **GO:0016514 SWI/SNF complex** (nuclear).

**Metabolic changes.** **No data.** No metabolomic, lipidomic, or energy-metabolism study of DMT exists (MetaboLights/Metabolomics Workbench/HMDB searches not applicable to an entity with no profiled cohort).

**Immune system involvement.** **Minimal data.** One case described "inflammatory infiltration" within the tumor (PMC11605529); another showed "patchy CD163… positivity," a macrophage marker (PMC11007021), which may indicate a histiocytic component. No autoimmunity or immunodeficiency link. Immune checkpoint trials in SMARCB1-deficient tumors (e.g., NCT05286801 tiragolumab+atezolizumab; NCT05407441 tazemetostat+nivolumab/ipilimumab) reflect a hypothesis, not established immunobiology in DMT.

**Tissue damage mechanisms.** Damage is predominantly **mechanical/compressive** (mass effect, aqueductal obstruction, raised ICP, tonsillar herniation in one case — "8 mm tonsillar herniation," PMC11007021) plus **desmoplastic matrix deposition** and, in the aggressive subset, **leptomeningeal seeding**. There is no evidence for oxidative stress, ischemia, or classical fibrotic signaling as studied mechanisms here.

**Biochemical abnormalities.** None specific — no enzyme deficiency, receptor, or ion-channel defect. No serum/CSF biochemical marker is abnormal in a disease-specific way (CSF germ-cell tumor markers AFP/β-hCG are *negative*, which is diagnostically useful; see §10).

**Epigenetic changes.** See §4.4 — a distinct, compact DNA methylation class; inferred global H3K27me3 gain at Polycomb targets with loss of enhancer H3K27ac.

**Molecular profiling.**
- *Transcriptomics:* **none published for DMT.** No GEO/ArrayExpress dataset (GEO search returned 0).
- *Proteomics:* **none for DMT.** (A proteomics study exists for ATRT — NCT04868799 "Finding New Targets by Proteomic Approaches (InnovRT1)" — but not DMT.)
- *Metabolomics / lipidomics:* **none.**
- *Genomic structural features:* focal 22q loss; additional 2q/9q/12q/16/17 losses; few gains (PMC13124280).
- *Ultrastructure (electron microscopy)* — the one modality with DMT-specific data: "large nuclei with prominent nucleoli, scant cytoplasm containing small vacuoles and intermediate filaments," plus "intercellular junctions, vesicular endocytosis and finger-like cytoplasmic extensions corresponding to microvilli" (PMC13359088) — features consistent with the EMA positivity and with an epithelial-like/mesenchymal ambiguity.

**Advanced technologies.**
- *Single-cell / spatial transcriptomics:* **no DMT study.** (Single-cell work exists for rhabdoid tumors generally — NCT04987476 "Rhabdoid Tumors Cellular Architecture by Single-cell Analyses (InnovRT-2)".)
- *Multi-omics integration:* no TCGA/ICGC/cBioPortal cohort for DMT. The closest integrated work is on AT/RT: **Torchia J, Golbourn B, Feng S, et al. "Integrated (epi)-Genomic Analyses Identify Subgroup-Specific Therapeutic Targets in CNS Rhabdoid Tumors." *Cancer Cell* 2016;30(6):891–908 (PMID 27960086; DOI 10.1016/j.ccell.2016.11.003)**, which found three epigenetic subgroups with "distinct genomic profiles, SMARCB1 genotypes, and chromatin landscape that correlated with differential cellular responses to a panel of signaling and epigenetic inhibitors," including that "differential methylation of a PDGFRB-associated enhancer confers specific sensitivity of group 2 ATRT cells to dasatinib and nilotinib." *Applicability to DMT is unknown.*
- *Functional genomics screens:* the BRD9 dependency was identified "using a genome-wide CRISPR-Cas9 screen" in SMARCB1-mutant rhabdoid tumors (PMID 31015438). **No DMT cell line or DepMap entry exists**, so this dependency is inferred.

### 6.3 Cell types and cell-of-origin

**Unknown.** Tauziède-Espariat et al. state plainly that the histomorphology and immunophenotype "may suggest a potential mesenchymal origin," yet "no cell of origin has been identified to date," and caution that "loss of expression of INI1/SMARCB1 is not typical of a specific origin" (PMC13359088). Candidate CL terms are therefore **hypothetical**, not evidenced:
- **CL:0000057 fibroblast** (ID not verified this session) — for the desmoplastic/mesenchymal hypothesis
- **CL:0000652 pinealocyte**, CL:0010013 type I pinealocyte, CL:0010014 type II pinealocyte, **CL:0002220 interstitial cell of pineal gland** (all verified via OLS4) — anatomically resident candidates; note that GFAP and CRX (cone-rod homeobox, a pineal/retinal lineage marker) are **negative** in DMT (PMID 41259279; PMC11605529), which argues *against* a pinealocyte lineage.
- Non-neoplastic bystanders with **retained** INI1: "Immunohistochemistry revealed loss of nuclear INI1 expression by the myxoid component but its **retention in the vascular elements**" (PMID 37284622) — i.e., endothelial/pericytic and neuropil-glial elements are entrapped, not transformed.

---

## 7. Anatomical Structures Affected

### 7.1 Organ level

- **Primary site (100% of reported cases): pineal region / pineal gland.** "All tumors were located in the pineal region" (PMID 31732806); "all cases occurred in the pineal region" (PMID 35195707).
  - **UBERON:0001905 pineal body** (verified); **UBERON:0022283 pineal recess of third ventricle**; **UBERON:0034907 pineal parenchyma**; **UBERON:0015238 pineal complex**; **UBERON:0001899 epithalamus** (all verified via OLS4).
- **Secondary / contiguous involvement:**
  - **UBERON:0002289 midbrain cerebral aqueduct** (verified) — compressed/effaced: "cerebral aqueduct effacement" (PMC11007021).
  - **UBERON:0002286 third ventricle** (verified) and lateral ventricles — "dilated third and lateral ventricles" (PMC11605529); "extension into the third and right lateral ventricles" (PMC11007021).
  - Thalamus — "bilateral thalamic splaying" (PMC11007021).
  - Cerebellar tonsils — "8 mm tonsillar herniation" (PMC11007021).
  - **UBERON:0000391 leptomeninx** / **UBERON:0000315 subarachnoid space** (verified) — leptomeningeal dissemination in the aggressive subset (PMID 42467229; PMID 35195707).
  - **UBERON:0002336 corpus callosum** (verified) — late infiltration in one long-followed case (PMC13359088), together with a subependymal nodule.
- **Body systems involved:** **nervous system** (central); **endocrine** by virtue of the organ of origin (pineal gland) — although **no pineal endocrine dysfunction (melatonin abnormality, HP:0012689) has been reported** in any DMT case retrieved. Secondary CSF-dynamics involvement (ventricular system).

### 7.2 Tissue and cell level

- **Tissue types:** nervous tissue (pineal parenchyma, adjacent midbrain), **connective tissue** (the defining desmoplastic collagenous stroma and myxoid matrix), and vasculature ("numerous hyalinized vessels," PMC13359088).
- **Histologic architecture:** "spindled and epithelioid cells embedded in a desmoplastic stroma alternating with a variable extent of a loose myxoid matrix" (PMID 31732806); "thin cords of spindle cells, presenting oval nuclei without atypia or mitosis" (PMC13359088); "an admixture of small to medium-sized spindle cells embedded in a heavily collagenized and myxoid matrix" (PMC11007021); "discohesive rhabdoid cells embedded within a prominent myxoid stroma and focal collagenous matrix" in the aggressive case (PMID 42467229). Rhabdoid cells are generally rare: "rhabdoid cells are rare" (PMID 33420834).
- **Cell populations:** neoplastic SMARCB1-deficient spindled/epithelioid (occasionally rhabdoid) cells of undetermined lineage (see §6.3), with entrapped "non-neoplastic neuropil-glial-vascular elements" retaining INI1 (PMID 37284622).

### 7.3 Subcellular level

- **Nucleus** — site of the primary defect (loss of nuclear SMARCB1/INI1 staining is the diagnostic readout). GO cellular component: **GO:0016514 SWI/SNF complex** (verified); nucleus (GO:0005634, ID not verified this session).
- **Cell membrane / junctions and microvilli** — "intercellular junctions, vesicular endocytosis and finger-like cytoplasmic extensions corresponding to microvilli" (PMC13359088); concordant with EMA (membranous) positivity.
- **Cytoplasmic intermediate filaments** and small vacuoles on EM (PMC13359088).
- **Extracellular matrix** (not strictly subcellular but mechanistically central): Alcian-blue-positive myxoid ground substance and collagen with amianthoid fibers and crystalloids (PMID 37284622; PMC13359088).

### 7.4 Localization and lateralization

**Midline, single lesion.** Every reported case is a solitary pineal-region midline mass; the infratentorial supracerebellar approach is favored "for midline lesions" (**Mandera M, Antkowiak L. *Adv Tech Stand Neurosurg* 2026;56:165–182; PMID 42393447**). Lateralization applies only to secondary extension (e.g., "extension into the third and **right** lateral ventricle," PMC11007021) and to bilateral consequences (bilateral thalamic splaying; bilateral ventriculomegaly). Tumor sizes reported: 21 × 17 mm (PMC11605529) up to 6.6 × 6.1 × 5.7 cm (PMC11007021).

---

## 8. Temporal Development

### 8.1 Onset

- **Age:** adolescent-to-adult only. Range **15–61 years** across all series; medians/means 33–40 years (PMID 31732806; PMID 35195707; PMC11605529; PMC13359088). "DMT 'affects young adults (median age: 33 years-old, from 15 to 61 years-old)'" with female predominance (PMC13359088). **No congenital, neonatal, or pediatric (<15 y) case has been reported** (PMC11605529) — a sharp contrast with AT/RT, "a highly malignant brain tumor predominantly occurring in infants" (PMID 31732806).
- **Onset pattern:** **subacute to acute**, dominated by hydrocephalus. Examples: 3 days of headache/dizziness with upgaze palsy and progressive drowsiness (PMC11605529); "subacute, progressive headaches, and an acute episode of sudden vision loss" (PMC11007021). The underlying growth is presumably insidious (low Ki-67), with abrupt clinical decompensation when the aqueduct obstructs — *inferred*.

### 8.2 Progression

- **Staging:** **no staging system and no CNS WHO grade** exist. Tauziède-Espariat et al.: "no grading has been established so far" (PMC13359088). There is no AJCC equivalent. Practical risk stratification in reports relies on **extent of resection**, **Ki-67**, **rhabdoid cytology**, and **presence of CSF/leptomeningeal dissemination**.
- **Progression rate: highly variable.** Documented courses include:
  - *Stable for years after GTR* — "the patient remained well… Postoperative imaging confirmed complete tumor resection" at 6 months (PMC11605529); "three patients were alive with stable disease" after a median 48-month observation (PMID 31732806).
  - *Early recurrence* — recurrence **8 months** after partial resection, then stability for **11 years** after re-resection plus focal radiotherapy, then late dissemination (PMC13359088).
  - *Aggressive recurrence with dissemination* — "developed aggressive recurrence and focal leptomeningeal dissemination following ventriculoperitoneal shunt placement and Gamma Knife radiosurgery" (PMID 42467229).
  - *Death from disease* — 3/7 (PMID 31732806), 3/10 (PMID 35195707), 3/11 (PMC11605529), 3/12 (PMC13359088).
- **Course pattern:** best described as **indolent-but-relapsing**, i.e., slowly progressive with long latency to relapse in some patients and rapid progression in a minority. Published characterizations: "a relatively indolent clinical course with low proliferative activity and no radiologically documented disseminated disease" (PMID 42467229, describing prior literature) versus "intermediate behavior" (PMID 42115465).
- **Duration:** **chronic**; after resection patients require indefinite surveillance. The longest documented follow-up is "more than 10 years," described as "the longest follow-up period, in terms of years, following the initial diagnosis" (PMC13359088). Published median follow-ups are short: 29.5 months (range 0–84; PMID 35195707) and 27.6 months (PMC11605529).

### 8.3 Patterns

- **Remission:** **treatment-induced only.** Gross-total resection achieves radiographic complete remission (PMC11605529; PMC11007021). Craniospinal irradiation produced "significant reduction in tumor size with no signs of intracranial CSF dissemination" in the disseminated case (PMID 35195707). **No spontaneous remission reported.**
- **Critical periods / windows of intervention:**
  1. *At presentation* — relief of obstructive hydrocephalus (ETV or external/VP drainage) is the time-critical intervention.
  2. *At first operation* — achieving **gross total resection** appears to be the main modifiable prognostic lever: "Gross total resection remains the optimal surgical goal when safe" for pineal parenchymal tumors generally (PMID 42393447); the one documented progressor in the 11-case census had "subtotal resection, Ki-67 15%" (PMC11605529).
  3. *Long-term* — because relapse can occur after >10 years of stability (PMC13359088), surveillance imaging should not be discontinued early. This is a recommendation implied by, not formally studied in, the literature.

---

## 9. Inheritance and Population

### 9.1 Epidemiology

- **Prevalence:** **unknown; no estimate exists.** Not in Orphanet with a prevalence figure, not in GBD, not in SEER or CBTRUS as a separate histology (PMID 39371035 contains no DMT or pineal-region breakout).
- **Incidence:** **unknown.** The only quantitative anchor is the cumulative case count: "DMT-SMARCB1 is a rare central nervous system neoplasm, with only approximately **15 reported cases**" (PMID 42467229, July 2026). My own census of retrieved primary reports (below) totals ~**17–19 published patients worldwide since 2020**, implying an incidence on the order of a few cases per year globally — i.e., well under 1 per 10,000,000 per year. *This is my arithmetic from the case list, not a published rate.*
- **Context:** pineal region tumours overall "are rare and heterogeneous, accounting for **less than 1% of intracranial neoplasms**" (PMID 42115465); "less than 1% of all adult intracranial tumor lesions" (PMID 35954310); and "approximately 3%-11% of all pediatric brain tumors, compared to less than 1% in adults" (PMC13124280). DMT is the rarest of the five WHO pineal types.

**Published case census (retrieved this session):**

| Report | n | Age/sex | Key features | PMID |
|---|---|---|---|---|
| Thomas C, et al. *Acta Neuropathol* 2020;139:277–286 | 7 | 4F/3M, median 40 (15–61) | Index series; 3 alive stable, 1 progressed, 3 died at median 48 mo | 31732806 |
| Matsumura N, et al. *Virchows Arch* 2021;479:835–839 | 1 | not stated in abstract | "no myxoid stroma and slightly elevated proliferating activity" | 33420834 |
| Wang YE, et al. *Neuropathology* 2021;41:37–41 | 1 | 33 M | "the first case reported in China"; initially suspected germinoma | 32901946 |
| Manoranjan B, et al. *Free Neuropathol* 2021;2:14 | 1 | 24 F | INI1 loss in myxoid component, retained in vessels; *SMARCB1* deletion; methylation grouped with DMT | 37284622 |
| Manoranjan B, et al. *Neuro Oncol* 2022;24:847–848 | (review of 10) | 6F/4M, mean 36.6 | CSF dissemination case; CSI 36 Gy/20 fx + 19.8 Gy/11 fx boost; 3/10 died | 35195707 |
| Robinson LJ, et al. *Brain Pathol* 2024;34:e13258 | 1 | 18 F | 6.6 cm mass; novel **p.Glu31Lys** missense VUS; CD163/CD99+, CD34−; methylation 0.99 | 38527786 (PMC11007021) |
| Zhou C, et al. *J Neurosurg Case Lessons* 2024;8:CASE24419 | 1 (+review of 11) | 50 F | Parinaud; Ki-67 <1% (lowest reported); GTR, no adjuvant therapy | 39586083 (PMC11605529) |
| Koren TJ, et al. *J Neuropathol Exp Neurol* 2026;85:303–305 | 1 | not retrieved | Presentation with Parinaud syndrome | 40834270 |
| Goyal A, et al. *Int J Surg Pathol* 2026;34:776–781 | 2 | 22 F, 45 F | SMA/EMA/CD34+, GFAP/desmin/CRX/brachyury−; "Both tumors showed increased Ki67" | 41259279 |
| Chang YW, et al. *Virchows Arch* 2026 (online 17 Jul) | 1 | 47 F | Aggressive recurrence + **first radiologically documented leptomeningeal dissemination** | 42467229 |
| Kinoshita Y, et al. *Ann Clin Lab Sci* 2026;56:232–238 | 1 | 38 F | Intraoperative touch-imprint cytology description | 42259547 |
| Tauziède-Espariat A, et al. *Free Neuropathol* 2026;7:16 | 1 | 33 M | Longest follow-up (>10 y); recurrence at 8 mo, stable 11 y, then dissemination; NIH classifier v2.0 score 0.84 | 42445896 (PMC13359088) |

### 9.2 Genetic etiology parameters

- **Inheritance pattern:** **not inherited / sporadic somatic.** DMT is a somatic *SMARCB1*-driven neoplasm; no familial DMT and no germline *SMARCB1* alteration in a DMT patient has been reported (§2.2). For completeness, the related germline syndrome RTPS1 is **autosomal dominant** (heterozygous germline *SMARCB1*; MedGen 322892 / OMIM #609322).
- **Penetrance:** not applicable to DMT. For RTPS1: "In patients with RTPS1 penetrance may be extremely high (e.g. > 90% by 5 years)" (PMID 33532948).
- **Expressivity:** not applicable (somatic). Phenotypic variability within DMT (Ki-67, rhabdoid cytology, myxoid content, immunophenotype) is tumor-intrinsic, not an inherited expressivity phenomenon — e.g., a case with "no myxoid stroma and slightly elevated proliferating activity" (PMID 33420834).
- **Genetic anticipation:** not applicable (no repeat expansion, no inherited transmission).
- **Germline mosaicism:** **no data for DMT.**
- **Founder effects:** **none reported.**
- **Consanguinity:** **no reported role.**
- **Carrier frequency:** not applicable to DMT. Germline *SMARCB1* pathogenic variants are rare in the population (gnomAD pLI 0.99999998). For context, among malignant rhabdoid tumor patients, "Among newly diagnosed cases of MRT 25–35% carry a germline PV in *SMARCB1* (RTPS1)" (PMID 33532948) — this figure applies to MRT/AT/RT, **not** to DMT.

### 9.3 Population demographics

- **Affected populations / ethnicity:** no ethnic predilection identified; no population-genetic enrichment known. Case numbers are far too small for any inference.
- **Geographic distribution:** cases have been reported from multiple continents. Specific, source-verifiable anchors: the index series was a **multi-national European/North American** collaboration (author affiliations spanning Germany, Denmark, Ireland, UK, France, and the USA, per the Thomas et al. author list); Wang et al. report "the first case reported in **China**" (PMID 32901946); the Manoranjan case came from the **University of Calgary, Canada** (PMC9071305); Tauziède-Espariat et al. from **Sainte-Anne Hospital, Paris, France** (PMC13359088); Robinson et al. from **Utah, USA** (PMC11007021). Other reports originate in Japan (PMID 33420834), India (PMID 41259279), and Taiwan (PMID 42467229) — *country attributions for these three are inferred from the reports' institutional context and were not individually verified in this session.* **There is no endemic area and no regional variation; the geographic spread simply reflects where the entity has been recognized.**
- **Geographic distribution of specific variants:** none — variants are sporadic somatic events.
- **Sex ratio:** modest **female excess**, ~**7F:4M** (≈1.75:1) in the 11-case census (PMC11605529); "a slight female predominance (F: 7; M: 4)" (PMC11007021); Thomas series 4F:3M (PMID 31732806); Manoranjan review 6F:4M (PMID 35195707). Tauziède-Espariat et al. likewise describe "female predominance" (PMC13359088).
- **Age distribution:** unimodal in the third-to-fifth decades; 15–61 years with no pediatric and no geriatric (>61 y) cases reported.

---

## 10. Diagnostics

### 10.1 Imaging

Imaging is the first diagnostic step for any pineal mass — "Different subtypes of pineal region tumours exhibit distinct radiological characteristics, thus imaging remains the primary diagnostic tool" (PMID 39262074) — but DMT has **no pathognomonic imaging signature**; appearances in the retrieved cases are notably heterogeneous:

| Case | CT | MRI |
|---|---|---|
| 50 F (PMC11605529) | "space-occupying lesion in the pineal area with obstructive hydrocephalus" | 21 × 17 mm round mass, **T1 isointense**, "mixed low signal on T2–FLAIR, and low signal on DWI and ADC sequences, **with no obvious enhancement**"; dilated 3rd/lateral ventricles |
| 24 F (PMID 37284622) | "hypodense lesion" | **T1-hypointense, T2 and FLAIR hyperintense, displayed gadolinium enhancement** |
| 18 F (PMC11007021) | — | "a large, heterogenous **enhancing** mass (6.6 × 6.1 × 5.7 cm) centered in the pineal region with extension into the third and right lateral ventricles"; aqueduct effacement; thalamic splaying; 8 mm tonsillar herniation |
| 22 F & 45 F (PMID 41259279) | — | "heterogeneously **enhancing** pineal region masses" |
| 33 M (PMC13359088) | "markedly hypodense with a pseudo-cystic appearance," 3-mm macrocalcification, intraventricular hemorrhage | — |
| 33 M (PMID 32901946) | — | "initially found to have a suspicious **germinoma** on imaging" |

**Practical implication:** enhancement ranges from absent to marked; pseudo-cystic/hypodense and calcified appearances occur; radiology cannot distinguish DMT from germinoma, PTPR, or pineal parenchymal tumours. RadLex/Radiopaedia entries were not retrievable in this session (Radiopaedia returned HTTP 402).

### 10.2 Laboratory tests and biomarkers

- **CSF/serum germ-cell tumour markers (AFP, β-hCG)** are the key *exclusionary* tests for any pineal mass: germ cell tumours "can be identified through elevated levels of tumour markers like alpha-fetoprotein (AFP) and human chorionic gonadotropin (HCG) in both cerebrospinal fluid (CSF) and serum" (PMID 39262074). In DMT these are expected to be **negative** — note that "Histologic diagnosis necessitates biopsy, unless in cases of germ cell tumours" (PMID 39262074). *No DMT report documented marker values; negativity is inferred from the requirement for histologic diagnosis.* LOINC codes were not retrieved.
- **CSF cytology** can be positive in disseminating cases: "A cerebrospinal fluid cytologic preparation had several cells morphologically similar to those in routine and electron microscopy" (PMID 37284622).
- **No blood, urine, enzyme, metabolite, or circulating biomarker is diagnostic.** No FDA-recognized biomarker exists for this entity.

### 10.3 Biopsy / histopathology — the diagnostic core

**Essential histology:** low-grade spindled and epithelioid (occasionally rhabdoid) cells in alternating desmoplastic-collagenous and loose myxoid matrix, with absent or rare mitoses (PMID 31732806; PMC11007021; PMC13359088). Myxoid matrix is Alcian-blue positive (PMID 37284622). Amianthoid collagen fibers and crystalloids may be present (PMC13359088).

**Intraoperative assessment.** Frozen-section/imprint cytology is feasible and characteristic: "The imprint preparations were composed of bland, relatively monomorphic oval-to-spindled tumor cells with delicate fibrillary processes embedded in a myxoid background. Small fibrillary acellular zones with variably collagenous areas were also identified, closely mirroring the tumor's characteristic myxoid to myxofibrillary histology with irregular anastomosing collagenous structures" (PMID 42259547). The same authors warn that "its rarity and morphologic overlap with other pineal region neoplasms may pose significant diagnostic challenges, particularly during intraoperative consultation when tissue is limited" (PMID 42259547). Fresh intraoperative smear in another case showed "a poorly cellular tumor composed of spindle cells, in a myxoid background with numerous hyalinized vessels" (PMC13359088).

**Immunohistochemistry — the single most important test is SMARCB1/INI1:**

| Marker | Result in DMT | Source |
|---|---|---|
| **SMARCB1 / INI1 (nuclear)** | **LOST** — defining feature; 100% of reported cases. Retained in entrapped vessels/non-neoplastic elements | PMID 31732806; PMID 37284622; PMID 41259279; PMID 42467229; PMC13359088 |
| **EMA (epithelial membrane antigen)** | Frequently **positive** ("expression of EMA and CD34 was frequent") | PMID 31732806; PMID 41259279; PMC13359088 |
| **CD34** | Frequently **positive** (strong in one case); but **negative** in two reported cases | PMID 31732806; PMC11605529 (strong); negative: PMC11007021, PMC13359088 |
| **SMA (smooth muscle actin)** | **Positive** in 2/2 Indian cases; negative in the Paris case | PMID 41259279; PMC13359088 |
| **GFAP** | Usually **negative**; "positive in minor cell populations" in one case | PMID 41259279 (neg); PMC11605529 (focal pos) |
| **OLIG2 / Oligo-2** | **Negative** | PMC11605529; PMC13359088 |
| **Desmin** | **Negative** (focal positivity in one case) | PMID 41259279 (neg); PMC11007021 (focal pos) |
| **CRX (cone-rod homeobox)** | **Negative** — argues against pineal parenchymal lineage | PMID 41259279 |
| **Brachyury** | **Negative** — excludes chordoma | PMID 41259279 |
| **Synaptophysin** | Variable — "positive in one tumor"; negative in another | PMID 41259279; PMC13359088 |
| **Pan-cytokeratin, S100, neurofilament, SSTR2a** | **Negative** | PMC13359088; PMC11007021 (SSTR2 neg) |
| **CD163, CD99** | Patchy **positive** (unusual; one case only) | PMC11007021 |
| **Ki-67 / MIB1** | **Low in most** — "median 3%"; range **<1% to 15.4%**; only 2/11 exceeded 10% | PMID 31732806; PMC11605529 |

Goyal et al. summarize the diagnostic difficulty: "The histology and **polyphenotypic** nature pose diagnostic dilemmas" (PMID 41259279); Matsumura et al. note "Tumor cells with low-grade morphology show polyphenotypic immunoreactivity, and rhabdoid cells are rare" (PMID 33420834).

**Electron microscopy** (adjunct, not required): see §6.2.

### 10.4 Genetic and epigenetic testing

**Recommended diagnostic approach (synthesized from the retrieved reports; no formal guideline exists for this entity):**

1. **SMARCB1/INI1 immunohistochemistry** on the resection/biopsy specimen — the practical screening test; loss of nuclear expression triggers the differential of SMARCB1-deficient CNS tumors.
2. **DNA methylation profiling** — effectively the confirmatory test. Important caveats retrieved: "Most DNA methylation profiles were not classifiable using the Heidelberg Brain Tumor Classifier (version v11b4)" (PMID 31732806); the entity is still "absent from" **DKFZ classifier v12.8**, whereas **NIH classifier v2.0** does contain a DMT class (calibrated score 0.84 in the reported case) (PMC13359088). Another case was confirmed at 0.99 confidence (PMC11007021). **If methylation profiling returns "no match," this does not exclude DMT — the classifier version matters.**
3. **Copy-number analysis** (from the methylation array or CMA) — to document *SMARCB1*/22q focal deletion (PMC13359088: "Copy number profile confirmed SMARCB1 homozygous deletion").
4. **Targeted *SMARCB1* sequencing / NGS panel** — to detect frameshift indels (c.369_370del; c.237_276dup) or the rare missense (c.91G>A) not captured by CNV analysis (PMID 31732806; PMC11007021).
5. **Fusion testing** when the differential includes intracranial mesenchymal tumour, FET::CREB-fused — in one case this "was excluded by negative **EWSR1 and FUS** testing" (PMC11007021).
6. **Germline *SMARCB1* testing:** not standard for DMT, but the SIOPE Host Genome Working Group position is that "patients with 'SMARCB1-deficient non-RT neoplasms' should be offered genetic testing **on a research basis** and, if positive for a PV, cancer surveillance" (PMID 33532948). Discussing germline testing is reasonable, particularly in the youngest patients.

**Modality-specific utility:**
- *WGS:* no published role in DMT; would capture CNV + SNV + structural events in one assay (inferred utility).
- *WES:* used implicitly via "brain tumor profiling" panels; detected the p.Glu31Lys VUS (PMC11007021).
- *Gene panels:* CNS/brain tumour panels including *SMARCB1* are the practical route; Genomics England PanelApp lists *SMARCB1* on the "Familial rhabdoid tumours" (panel 600) and "Embryonal tumour of possible germline origin" (panel 1636) panels (panelapp.genomicsengland.co.uk).
- *Single-gene testing:* *SMARCB1* sequencing + deletion/duplication analysis; a GTR entry exists for RTPS1 (GTRT000005873; MedGen 322892).
- *CMA:* useful for the focal 22q11.23 deletion.
- *Karyotyping:* low yield — these genomes are near-diploid with focal losses; not recommended.
- *FISH:* *SMARCB1* (22q11.2) FISH can confirm deletion; no DMT-specific FISH study was retrieved.
- *mtDNA testing, repeat-expansion testing:* **not applicable.**

### 10.5 Omics-based diagnostics

- **Epigenomics (DNA methylation array):** the only omics modality in clinical diagnostic use for DMT (see above) — this is a genuine example of methylation profiling defining a WHO entity: "most of these have been offshoots of the deoxyribonucleic acid (DNA) methylation profiling of CNS tumors with distinct profiling such as desmoplastic myxoid tumor (DMT) of the pineal region, SMARCB1-mutant" (**Chatterjee D, Gupta K. *Indian J Pathol Microbiol* 2022;65(Suppl):S94–S98; PMID 35562139**).
- **RNA-seq / transcriptomics, proteomics, metabolomics, liquid biopsy:** **no established or reported diagnostic role for DMT.** No circulating-tumour-DNA or CSF cell-free DNA assay has been described. Emerging, non-DMT-specific: "rapid intraoperative sequencing technologies" are flagged as a translational direction for pineal tumours generally (PMC13124280).

### 10.6 Clinical criteria and differential diagnosis

**There are no standardized clinical diagnostic criteria** (no DSM/ICD-criteria analogue). Diagnosis is **integrated histopathologic + molecular**, per WHO CNS5 practice: pineal-region location + low-grade spindled/epithelioid cells in desmoplastic/myxoid matrix + loss of nuclear SMARCB1 + compatible methylation class.

**Differential diagnosis (with distinguishing features — all from retrieved sources):**

| Entity | How to distinguish |
|---|---|
| **AT/RT (atypical teratoid/rhabdoid tumour)** | Also SMARCB1-deficient, but "a highly malignant brain tumor predominantly occurring in infants," high-grade histology, high Ki-67; DMT "contrast[s] sharply" with it clinically and pathologically (PMID 31732806; PMID 42259547). Methylation separates them (PMC13124280) |
| **Poorly differentiated chordoma** | SMARCB1-deficient and epigenetically adjacent (PMID 32901946), but **brachyury-positive**; brachyury is negative in DMT (PMID 41259279) |
| **Pineal parenchymal tumours (pineocytoma, PPTID, pineoblastoma)** | **CRX-negative** and synaptophysin usually negative/focal in DMT; INI1 retained in pineal parenchymal tumours (PMID 41259279) |
| **Papillary tumour of the pineal region (PTPR)** | Papillary architecture, cytokeratin-positive; DMT is pan-CK negative (PMC13359088) |
| **Germinoma** | Radiologically mimics DMT ("a suspicious germinoma on imaging," PMID 32901946); distinguished by CSF/serum AFP/β-hCG and by germ-cell IHC |
| **Intracranial mesenchymal tumour, FET::CREB-fused** | Morphologic/immunophenotypic overlap; excluded by negative **EWSR1/FUS** testing (PMC11007021) |
| **Myxoid / chordoid / metaplastic meningioma of the pineal region** | The hardest differential — Tauziède-Espariat et al. go so far as to propose that DMT and "metaplastic meningioma, myxoid meningioma or chordoid meningioma of the pineal region, **may represent the same tumoral entity**" (PMC13359088). EMA positivity is shared; SSTR2a was negative in their DMT case |
| **Low-grade diffusely infiltrative tumour, *SMARCB1*-mutant (LDIT-SMARCB1)** | A separate recently described low-grade SWI/SNF-deficient entity; "other recently described tumor types such as desmoplastic myxoid tumor, SMARCB1-mutant, and low-grade diffusely infiltrative tumor, SMARCB1-mutant, may even manifest as low-grade lesions" (PMID 37969088). Distinguished by diffuse infiltrative growth and non-pineal location |
| **Cribriform neuroepithelial tumour (CRINET)** | SMARCB1-deficient, non-rhabdoid, cribriform architecture, clusters within **ATRT-TYR**, favourable outcome (**Johann PD, et al. *Brain Pathol* 2017;27(4):411–418; PMID 27380723; DOI 10.1111/bpa.12413**) |

### 10.7 Screening of asymptomatic individuals

**No screening is indicated or available for DMT** — it is sporadic, somatic, and far too rare. No newborn screening, carrier screening, or cascade screening applies. The only adjacent screening framework is RTPS surveillance for carriers of germline *SMARCB1* pathogenic variants (see §13).

---

## 11. Outcome / Prognosis

### 11.1 Survival and mortality

**No 5-year or 10-year survival estimate exists** (no registry data, n too small, follow-up too short). What is documented:

| Census | n | Deaths | Follow-up | Source |
|---|---|---|---|---|
| Thomas 2020 | 7 | **3 died** (plus 1 progression, 3 stable) | median observation **48 months** | PMID 31732806 |
| Manoranjan 2022 | 10 | **3/10 (30%)** | median **29.5 months** (range 0–84) | PMID 35195707 |
| Zhou 2024 | 11 | **3 died**, 1 progressed | median **27.6 months** | PMC11605529 |
| Tauziède-Espariat 2026 | 12 | **3/12 died of disease** | up to >10 years in index case | PMC13359088 |

Pasquinelli et al. (verbatim): DMT shows a "less aggressive course than atypical teratoid/rhabdoid tumors" but "disease-related mortality has been observed in 3 of 7 patients after a median follow-up of approximately 48 months" (PMC13124280).

**Interpretation:** case-fatality in the published literature is roughly **25–30%** at ~2.5–4 years. Because case reports preferentially publish the instructive extremes, both the "indolent" framing and this mortality figure should be treated as unstable estimates.

- **Life expectancy:** unquantified. Survivors with GTR have had unremarkable short-to-intermediate-term courses; one patient is alive on chemotherapy >10 years from diagnosis (PMC13359088).
- **Mortality rate / disease-specific mortality (population level):** not calculable; no CDC/WHO/GBD data.

### 11.2 Morbidity and function

- Shunt dependence and persistent oculomotor deficits are the main residual morbidities documented; one patient had "mild improvement in eye movement abnormalities" at 6 months (PMC11605529), another was "discharged with no new neurologic deficits" (PMC11007021).
- **Disability outcomes:** no ICF-coded or formally measured disability data.
- **Quality-of-life measures:** **none reported** (no EQ-5D, SF-36, PROMIS, or EORTC instruments) — explicit gap.

### 11.3 Disease course and complications

- **Obstructive hydrocephalus** — the commonest complication; may require ETV or VP shunt (PMID 35195707; PMC11007021).
- **CSF / leptomeningeal dissemination** — the critical adverse event. Chang et al. 2026 established it radiologically for the first time: "**Literature review revealed no previous reports of radiologically documented leptomeningeal dissemination.** This case expands the clinicopathologic spectrum of DMT-SMARCB1 and highlights the potential for aggressive biological behavior despite relatively low-grade histologic features" (PMID 42467229). Tauziède-Espariat et al. independently report, "for the first time radiological evidence of dissemination," with a subependymal nodule and corpus callosum infiltration (PMC13359088).
- **Local recurrence** — documented as early as 8 months after partial resection (PMC13359088).
- **Tonsillar herniation / acute decompensation** — one case (PMC11007021).
- **Recovery potential:** good for the compressive/hydrocephalic component after resection + CSF diversion; variable for the neoplasm itself. GTR with low Ki-67 has been managed without any adjuvant therapy, with no recurrence at 6 months (PMC11605529).

### 11.4 Prognostic factors

Derived from case-level observations (no multivariable analysis exists):

- **Extent of resection** — the one documented progressor in the 11-case census had "subtotal resection, Ki-67 15%, treated with radiotherapy" (PMC11605529). "Prognostic outcomes are strongly influenced by tumor subtype, **extent of resection**, and use of adjuvant therapy" for pineal parenchymal tumours generally (PMID 42393447).
- **Ki-67/MIB1 proliferation index** — low in most (median 3%); "Only 2 patients exceeded 10% (15% and 15.4%), indicating generally non-aggressive biology" (PMC11605529). Both high-Ki-67 cases in the Goyal report "showed increased Ki67 proliferative index" (PMID 41259279).
- **Rhabdoid cytology** — present in the aggressively behaving case: "discohesive rhabdoid cells" (PMID 42467229); rhabdoid cells are otherwise rare (PMID 33420834).
- **CSF/leptomeningeal dissemination at or after presentation** — adverse (PMID 35195707; PMID 42467229; PMC13359088).

**Prognostic biomarkers (molecular):** **none validated.** Neither the specific *SMARCB1* alteration type (deletion vs indel vs missense) nor the methylation score has been shown to predict outcome. **Note the key caveat repeated across reports: low-grade histology does NOT reliably predict indolent behavior** — "DMT, SMARCB1-mutant seems to be relatively benign, but careful attention is necessary because SMARCB1/INI1 deficiency is generally a genetic signature of concern" (PMID 33420834).

---

## 12. Treatment

**There is no standard of care, no clinical practice guideline, and no prospective trial for this entity.** Zhou et al. state verbatim: "clinical diagnosis and treatment measures are still in the exploratory stage and need to be further studied" (PMC11605529), and Manoranjan et al. "emphasize the need for case curation to establish prognostic factors and develop standardized therapeutic protocols for this newly recognized tumor entity" (PMID 35195707).

### 12.1 Surgical and interventional (the mainstay)

| Intervention | Evidence | Suggested NCIT (verified via OLS4) |
|---|---|---|
| **Gross total resection (GTR)** | 6/10 cases (PMID 35195707); "Gross total resection remains the optimal surgical goal when safe" (PMID 42393447) | **NCIT:C131672 Gross Total Resection** |
| **Subtotal resection (STR)** | 4/10 cases (PMID 35195707); associated with the documented progressor (PMC11605529) | — |
| **Infratentorial supracerebellar approach** | Used for GTR with lateral ventricular drainage (PMC11605529); "favored for midline lesions" (PMID 42393447) | — |
| **Endoscopic third ventriculostomy (ETV)** | 2/10 cases for obstructive hydrocephalus (PMID 35195707); "ETV offers an effective minimally invasive solution for hydrocephalus management" (PMID 42393447) | **NCIT:C182204 Third Ventriculostomy** |
| **Ventriculoperitoneal shunt** | Used in the 18F case (PMC11007021) and the 47F aggressive case (PMID 42467229) | **NCIT:C168483 Ventriculoperitoneal Shunt Placement** |
| **External/lateral ventricular drainage** | PMC11605529 | — |

### 12.2 Radiotherapy

| Approach | Evidence | Suggested NCIT |
|---|---|---|
| **Focal/involved-field radiotherapy** | 4/10 cases received postoperative RT (PMID 35195707; PMC11605529); "The recently described desmoplastic myxoid tumor, SMARCB1-mutant shows intermediate behavior, with **limited data supporting focal RT ≥54 Gy**" (**Tanguy R. *Adv Tech Stand Neurosurg* 2026;54:269–294; PMID 42115465**) | — |
| **Craniospinal irradiation (CSI)** for CSF dissemination | "36 Gy was delivered to the neuraxis in 20 fractions and an additional 19.8 Gy was given to the primary tumor volume in 11 fractions," with "significant reduction in tumor size with no signs of intracranial CSF dissemination" (PMID 35195707) | **NCIT:C116437 Craniospinal Irradiation**; NCIT:C150522 Proton Beam Craniospinal Irradiation; NCIT:C209869 Photon Beam Craniospinal Irradiation |
| **Stereotactic radiosurgery (Gamma Knife)** | Used in the 47F case, which nonetheless "developed aggressive recurrence and focal leptomeningeal dissemination following ventriculoperitoneal shunt placement and Gamma Knife radiosurgery" (PMID 42467229) — a cautionary single observation | **NCIT:C15358 Stereotactic Radiosurgery** |
| **Proton therapy** | Not reported in DMT; "Proton therapy is increasingly employed to limit long-term neurocognitive and secondary cancer risks" in pineal region tumours generally (PMID 42115465) | NCIT:C150522 |

**Observation without adjuvant therapy** is documented as a reasonable option after GTR of a low-Ki-67 tumor: "No adjuvant therapy was administered given gross-total resection, well-differentiated morphology, and very low proliferation index" (PMC11605529). Lombardi et al. note that for pineal tumours other than germinomas/pineoblastoma, "the role of radiotherapy remains poorly studied and it is usually reserved for aggressive (grade 3) or recurrent tumors" (PMID 35954310).

### 12.3 Pharmacotherapy and chemotherapy

- **Conventional chemotherapy:** used in only **1/10** published cases (PMID 35195707); 1/11 received "chemotherapy plus radiotherapy" (PMC11605529). The Paris patient is "currently undergoing chemotherapy" for late disseminated relapse (PMC13359088). **No regimen, response, or toxicity data for DMT are published.** Regimens for pineal tumours generally are alkylator/platinum-based (PMID 35954310) but are not validated here.
- **Pharmacogenomics:** **no DMT-specific pharmacogenomic data**; no PharmGKB/CPIC guidance applies to this entity.

### 12.4 Targeted and advanced therapeutics (all investigational for DMT)

**EZH2 inhibition is the most biologically grounded targeted strategy.** Pasquinelli et al. state verbatim that for DMT, "**EZH2 inhibition has emerged as a rational therapeutic strategy**" and "**tazemetostat has demonstrated clinical activity in SMARCB1-deficient malignancies**," while cautioning that "**dedicated clinical evidence in DMT-SMARCB1 is currently lacking**" (PMC13124280). The mechanistic basis is the SWI/SNF–Polycomb antagonism: "inactivation of Ezh2 blocks tumor formation driven by Snf5 loss" in conditional mouse models (PMID 20951942). The clinical benchmark in another INI1-deficient tumor: **Gounder M, et al. "Tazemetostat in advanced epithelioid sarcoma with loss of INI1/SMARCB1: an international, open-label, phase 2 basket study." *Lancet Oncol* 2020;21(11):1423–1432 (PMID 33035459; DOI 10.1016/S1470-2045(20)30451-4)** — "9 (15% [95% CI 7–26]) of 62 patients had an objective response" and "median progression-free survival was 5·5 months (95% CI 3·4–5·9)," with the drug "well tolerated."
- Suggested terms: **NCIT:C107506 Tazemetostat**; NCIT:C166954 Tazemetostat Hydrobromide; NCIT:C186499 Tazemetostat Regimen; **CHEBI:231598 tazemetostat** (all verified).

**BRD9 / ncBAF targeting** — strong preclinical rationale: "BRD9 is a specific vulnerability in pediatric malignant rhabdoid tumors (RTs), which are driven by inactivation of the SMARCB1 subunit of SWI/SNF… a BRD9-containing SWI/SNF subcomplex is required for the survival of SMARCB1-mutant RTs" (PMID 31015438). Two clinical-stage BRD9 agents were tested in SMARCB1-perturbed cancers and **both programs are now listed as terminated**: **NCT04965753** (FHD-609, Phase 1, "Advanced Synovial Sarcoma or Advanced SMARCB1-Loss Tumors" — **Terminated**) and **NCT05355753** (CFT8634 degrader, Phase 1, "SMARCB1-Perturbed Cancers" — **Terminated**) (ClinicalTrials.gov API, retrieved 23 Nov 2026).

**Immunotherapy** — hypothesis-stage for SMARCB1-deficient tumors; see trials below.

**Gene therapy, cell therapy (CAR-T, stem cell transplant), RNA-based therapies (ASO/siRNA/mRNA):** **none exist or are in development for DMT.** Restoring a deleted tumor-suppressor gene is not currently a tractable clinical strategy.

### 12.5 Experimental treatments / open and recent trials (ClinicalTrials.gov, retrieved 23 Nov 2026)

**None of these trials names DMT-SMARCB1 specifically**, but several have eligibility criteria ("INI1-deficient primary CNS malignant tumors," "SMARCB1-deficient malignancies") that a DMT patient could plausibly meet. Enrollment eligibility must be confirmed with each study.

| NCT ID | Title / regimen | Phase | Status |
|---|---|---|---|
| **NCT05407441** | "Tazemetostat+Nivo/Ipi in INI1-Neg/SMARCA4-Def Tumors" — tazemetostat + nivolumab + ipilimumab; conditions include **"INI1-deficient primary CNS malignant tumors"** | 1/2 | Active, not recruiting |
| **NCT05286801** | Tiragolumab + atezolizumab for relapsed/refractory **SMARCB1- or SMARCA4-deficient tumors** (AT/RT, epithelioid sarcoma, chordoma, rhabdoid tumor) | 1/2 | Active, not recruiting |
| **NCT03213665** | Tazemetostat in relapsed/refractory solid tumors, NHL, or histiocytic disorders with **EZH2, SMARCB1, or SMARCA4** alterations (Pediatric MATCH) | 2 | Completed |
| **NCT03155620** | Pediatric MATCH screening trial (genotype-directed assignment, incl. tazemetostat) | 2 | Active, not recruiting |
| **NCT06444880** | Ubamatamab ± cemiplimab in MUC16-expressing **SMARCB1-deficient malignancies** | 2 | Recruiting |
| **NCT06853080** | Bortezomib ± chemotherapy in atypical teratoid/rhabdoid tumors | 2 | Active, not recruiting |
| **NCT05151588** | Induction chemotherapy + tazemetostat, locally advanced SMARCB1-deficient sinonasal carcinoma | 2 | Not yet recruiting |
| **NCT04965753** | FHD-609 (BRD9 inhibitor), SMARCB1-loss tumors | 1 | **Terminated** |
| **NCT05355753** | CFT8634 (BRD9 degrader), SMARCB1-perturbed cancers | 1 | **Terminated** |
| **NCT03739827** | Natural history and biospecimen acquisition, rare solid tumors (children and adults) | n/a | Recruiting |

### 12.6 Treatment outcomes

- **Response rates:** not reported for any modality in DMT. The only quantitative response datum is radiographic: "significant reduction in tumor size with no signs of intracranial CSF dissemination" after CSI (PMID 35195707).
- **Side effects / adverse events:** no DMT-specific toxicity data. Expected surgical risks (pineal region approach), RT-related neurocognitive and secondary-malignancy risk (motivating proton therapy interest, PMID 42115465), and tazemetostat's reported tolerability in epithelioid sarcoma (PMID 33035459). No FAERS signal specific to this population.

### 12.7 Treatment strategy / algorithm (synthesized; no formal guideline)

1. **Present with pineal mass + hydrocephalus** → relieve CSF obstruction (ETV preferred where feasible; EVD/VP shunt as needed) and obtain tissue. Check serum/CSF AFP and β-hCG first to avoid operating on a germinoma (PMID 39262074).
2. **Maximal safe resection**, preferably GTR via infratentorial supracerebellar approach (PMID 42393447; PMC11605529). Request intraoperative imprint cytology/frozen section with awareness of the DMT morphology (PMID 42259547).
3. **Integrated diagnosis:** SMARCB1 IHC → methylation profiling (use a classifier version containing the DMT class) → *SMARCB1* sequencing/CNV; exclude brachyury+ chordoma and FET::CREB-fused mesenchymal tumour (PMID 41259279; PMC11007021; PMC13359088).
4. **After GTR with low Ki-67 and no dissemination:** observation with serial MRI is supported by practice (PMC11605529).
5. **After STR, and/or Ki-67 >10%, and/or rhabdoid morphology:** consider focal radiotherapy ≥54 Gy (PMID 42115465); 4/10–5/11 published patients received adjuvant RT (PMID 35195707; PMC11605529).
6. **With CSF/leptomeningeal dissemination:** craniospinal irradiation with boost (36 Gy/20 fx neuraxis + 19.8 Gy/11 fx boost as published) (PMID 35195767 → PMID 35195707); chemotherapy as salvage (PMC13359088).
7. **Relapse/refractory:** consider referral to a SMARCB1-deficient-tumor trial (EZH2 inhibitor ± checkpoint blockade); molecular tumor board review.
8. **Lifelong surveillance imaging** — relapse has occurred after 11 years of stability (PMC13359088).

**Combination therapies:** only chemo+RT (1 case, PMID 35195707/PMC11605529) and trial-based combinations (tazemetostat+nivo/ipi; tiragolumab+atezolizumab).
**Personalized medicine:** limited to molecular-profile-based trial eligibility (INI1/SMARCB1 loss). No CIViC/OncoKB/My Cancer Genome DMT-specific actionability entry was retrieved.

---

## 13. Prevention

- **Primary prevention:** **none possible or established.** The driver is a sporadic somatic event with no known modifiable exposure. No vaccination or risk-factor modification applies.
- **Secondary prevention (early detection):** **no screening program is justified** for a tumor with ~15–19 reported cases worldwide. There is no asymptomatic detectable phase of known duration. The practical analogue of secondary prevention is **prompt imaging of new headache plus upgaze palsy** in a young adult — i.e., clinical vigilance, not screening.
- **Tertiary prevention (preventing complications in affected patients):**
  - Timely CSF diversion to prevent herniation/visual loss (PMC11007021).
  - Maximal safe resection to reduce recurrence risk (PMID 42393447).
  - **Long-interval, long-duration surveillance MRI** including spine, given documented late and disseminated relapse (PMID 42467229; PMC13359088). *This is a reasoned recommendation from the case evidence, not a published guideline.*
- **Immunization:** not applicable.
- **Genetic screening / counseling:** DMT is not an inherited disease and does not by itself indicate germline testing. However, because the driver gene is the RTPS1 gene, offering **genetic counseling and research-basis germline *SMARCB1* testing** is consistent with the SIOPE position: "patients with 'SMARCB1-deficient non-RT neoplasms' should be offered genetic testing on a research basis and, if positive for a PV, cancer surveillance" (PMID 33532948). If a germline pathogenic variant were found, the SIOPE RTPS1 surveillance schedule applies (verbatim): "MRI CNS incl. spine or CNS ultrasound or WBMRI… Every 4 weeks, not less than every 2–3 months" (0–6 months of age); "Every 2–3 months" (7–18 months); "Every 3 months" (19 months–5 years); then "Yearly" whole-body MRI with physical examination "Every 6 months" — relevant to the patient's offspring/relatives rather than to the adult proband (PMID 33532948). Penetrance counseling point: "In patients with RTPS1 penetrance may be extremely high (e.g. > 90% by 5 years)" (PMID 33532948). Prenatal/preimplantation testing is relevant only in a confirmed-germline family.
- **Risk stratification:** no validated model. The de facto post-diagnosis stratifiers are extent of resection, Ki-67, rhabdoid cytology, and dissemination status (§11.4).
- **Behavioral interventions, public health interventions, environmental interventions, prophylaxis:** **none applicable** — no modifiable risk factor is known.

---

## 14. Other Species / Natural Disease

- **Taxonomy of affected species:** **Homo sapiens (NCBI:txid9606) only.** No DMT-SMARCB1 analogue has been described in any other species.
- **Breed (VBO):** **not applicable** — no animal breed predisposition exists for this entity.
- **Orthologous genes** (NCBI Gene, retrieved this session):

| Species | Gene symbol | NCBI Gene ID | Taxid | Chromosome |
|---|---|---|---|---|
| *Homo sapiens* | SMARCB1 | **6598** | 9606 | 22 (22q11.23) |
| *Mus musculus* | Smarcb1 | **20587** | 10090 | 10 |
| *Rattus norvegicus* | Smarcb1 | **361825** | 10116 | 20 |
| *Danio rerio* | smarcb1b | **30731** | 7955 | 21 |
| *Xenopus tropicalis* | smarcb1 | **448543** | 8364 | 1 |
| *Bos taurus* | SMARCB1 | **537412** | 9913 | 17 |

(A total of 627 `Smarcb1[sym]` gene records exist across species in NCBI Gene, indicating broad conservation.)

- **Natural disease in other species:** **none documented.** An OMIA advanced search by gene symbol SMARCB1 returned "**No phene records found**" (omia.org, retrieved this session) — i.e., no naturally occurring *SMARCB1*-associated Mendelian phene or tumor syndrome is catalogued in any domestic or companion animal species.
- **Veterinary relevance:** **none.** No veterinary importance for this entity.
- **Comparative pathology:** no cross-species comparison is possible for DMT itself. For the *gene*, comparative biology is informative and well documented in engineered models (§15): Snf5/Ini1 is essential for early development in mouse (embryonic/peri-implantation lethality in nulls) and is a *bona fide* tumor suppressor in mouse as in human (PMID 11095756; PMID 11313485; PMID 12450796).
- **Evolutionary conservation of mechanism:** high. The SWI/SNF–Polycomb antagonism underlying SMARCB1-loss oncogenesis was first inferred from *Drosophila* genetics — "Analysis of Drosophila mutants suggests that Polycomb and SWI/SNF complexes can serve antagonistic developmental roles" — and then validated in mouse and human (PMID 20951942). Note that *SMARCB1* aliases include the yeast/fly orthologue names *Snf5*, *Snr1*, and *Sfh1p* (NCBI Gene 6598), reflecting conservation from yeast to human.
- **Zoonotic potential / cross-species susceptibility:** **not applicable** (non-infectious neoplasm).

---

## 15. Model Organisms

**Bottom line: there is no model of DMT-SMARCB1.** No cell line, organoid, iPSC, xenograft, or genetically engineered animal reproduces a pineal-region desmoplastic myxoid tumor. All available models are *SMARCB1*-loss models that produce rhabdoid tumors or lymphoma, and DepMap contains no DMT line. The models below are useful for the **mechanism** (§6) but not for the **entity**.

### 15.1 Available genetic models of *Smarcb1* loss (mouse)

| Model | Design | Phenotype (verbatim where quoted) | Citation |
|---|---|---|---|
| ***Snf5*** **heterozygous knockout** | Germline het null | "Homozygous knockout of Snf5 results in embryonic lethality by embryonic day 7, whereas heterozygous mice are born at the expected frequency and appear normal. However, beginning as early as 5 weeks of age, heterozygous mice develop tumors consistent with MRT. The majority of tumors arise in soft tissues derived from the first branchial arch." | **Roberts CW, Galusha SA, McMenamin ME, Fletcher CD, Orkin SH. *PNAS* 2000;97(25):13796–13800; PMID 11095756; DOI 10.1073/pnas.250492697** |
| ***Ini1*** **knockout** | Germline null / het | "Ini1-null embryos die between 3.5 and 5.5 days postcoitum… approximately **15% of Ini1-heterozygous mice present with tumors**, mostly undifferentiated or poorly differentiated sarcomas. Tumor formation is associated with a loss of heterozygocity at the Ini1 locus" | **Guidi CJ, Sands AT, Zambrowicz BP, et al. *Mol Cell Biol* 2001;21(10):3598–3603; PMID 11313485; DOI 10.1128/MCB.21.10.3598-3603.2001** |
| ***Snf5*** **conditional (reversible inversion) allele** | Conditional/reversible inactivation | "loss of Snf5/Ini1/Baf47/SmarcB1… results in highly penetrant cancer predisposition with **100% of mice developing mature CD8(+) T cell lymphoma or rare rhabdoid tumors with a median onset of only 11 weeks**. Notably, while loss of Snf5 predisposes to aggressive cancers, it is also **required for survival of virtually all nonmalignant cells in vivo**" | **Roberts CW, Leroux MM, Fleming MD, Orkin SH. *Cancer Cell* 2002;2(5):415–425; PMID 12450796; DOI 10.1016/s1535-6108(02)00185-x** |
| ***Snf5*** **× *Ezh2*** **compound conditional** | Genetic epistasis | "using conditional mouse models, we show that **inactivation of Ezh2 blocks tumor formation driven by Snf5 loss**" | **Wilson BG, et al. *Cancer Cell* 2010;18(4):316–328; PMID 20951942** |

### 15.2 In vitro / cellular models

- **SMARCB1-deficient rhabdoid tumor cell lines** and mouse embryonic fibroblasts were the substrate for the enhancer-biology work (PMID 27941797; PMID 28262751) and for the CRISPR screen that identified the BRD9 dependency (PMID 31015438).
- **AT/RT primary tumors and cell lines** (191 primary ATRTs + 10 cell lines) underpin the subgroup-specific drug-sensitivity findings (PMID 27960086).
- **No DMT-derived line, organoid, or iPSC model exists** — this is the single largest translational bottleneck for the entity.

### 15.3 Induced (non-genetic) models

None relevant — there is no drug-, surgery-, or exposure-induced model of pineal DMT.

### 15.4 Phenotype recapitulation and limitations

| Human DMT feature | Recapitulated in existing models? |
|---|---|
| SMARCB1/INI1 protein loss | **Yes** (all models) |
| Tumor formation from Smarcb1 loss | **Yes** (MRT, sarcoma, T-cell lymphoma) |
| Polycomb/EZH2-dependent transformation | **Yes** (Snf5×Ezh2 epistasis) |
| BRD9/ncBAF dependency | **Yes** (rhabdoid lines) |
| **Pineal region localization** | **No** |
| **Desmoplastic + myxoid matrix morphology** | **No** |
| **Low Ki-67 / indolent course** | **No** — mouse models are rapidly lethal (median 11 weeks) |
| **Adolescent/adult onset** | **No** — mouse tumors arise within weeks |
| **Polyphenotypic EMA/CD34/SMA immunoprofile** | **No** |
| **DMT methylation class** | **No** |

**Interpretation:** existing models are adequate for testing *SMARCB1*-loss-directed therapeutics (EZH2 inhibitors, BRD9 degraders) that might be repurposed to DMT, but they cannot address DMT's defining features — its anatomical restriction, its matrix phenotype, its indolence, or its cell of origin.

### 15.5 Research applications and resources

- **Applications supported by current models:** SWI/SNF complex integrity and enhancer targeting; SWI/SNF–Polycomb antagonism; synthetic-lethal dependency discovery; preclinical testing of epigenetic inhibitors.
- **Resources:** MGI (mouse *Smarcb1*, Gene 20587), RGD (rat *Smarcb1*, 361825), ZFIN (*smarcb1b*, 30731), Xenbase (*smarcb1*, 448543), Alliance of Genome Resources; IMSR/KOMP/EMMA/MMRRC for mouse line availability. **Specific MGI allele IDs and IMSR stock numbers were not retrieved in this session** — these should be looked up directly before ordering lines.

---

## Appendix A — Ontology term suggestions (consolidated)

Terms marked **(v)** were verified by direct ontology lookup in this session; unmarked terms are suggestions whose IDs were **not** verified here and should be confirmed before ingestion.

**Disease:** MONDO:1060253 **(v)**; NCIT:C178507 **(v)**; UMLS C5555093 **(v)**; MedGen 1791534 **(v)**. Related: MONDO:0012252 / OMIM #609322 RTPS1 **(v)**.

**Gene/protein:** HGNC:11103 **(v)**; NCBI Gene 6598 **(v)**; Ensembl ENSG00000099956 **(v)**; OMIM *601607 **(v)**. UniProt Q12824 (not verified).

**HPO (phenotypes):** HP:0010799 Pinealoma **(v)**; HP:0012680 Abnormality of the pineal gland **(v)**; HP:0030693 Supratentorial neoplasm **(v)**; HP:0010953 Noncommunicating hydrocephalus **(v)**; HP:0002516 Increased intracranial pressure **(v)**; HP:0000511 Vertical supranuclear gaze palsy (Parinaud) **(v)**; HP:0002315 Headache **(v)**; HP:0001085 Papilledema **(v)**. Not verified: HP:0002018 Nausea, HP:0002013 Vomiting, HP:0000622 Blurred vision, HP:0002321 Vertigo, HP:0002329 Somnolence, HP:0000238 Hydrocephalus.

**UBERON (anatomy):** UBERON:0001905 pineal body **(v)**; UBERON:0022283 pineal recess of third ventricle **(v)**; UBERON:0034907 pineal parenchyma **(v)**; UBERON:0015238 pineal complex **(v)**; UBERON:0001899 epithalamus **(v)**; UBERON:0002286 third ventricle **(v)**; UBERON:0002289 midbrain cerebral aqueduct **(v)**; UBERON:0000391 leptomeninx **(v)**; UBERON:0000315 subarachnoid space **(v)**; UBERON:0002336 corpus callosum **(v)**.

**CL (cell types — all hypothetical for this disease):** CL:0000652 pinealocyte **(v)**; CL:0010013 type I pinealocyte **(v)**; CL:0010014 type II pinealocyte **(v)**; CL:0002220 interstitial cell of pineal gland **(v)**. Not verified: CL:0000057 fibroblast.

**GO (processes / components):** GO:0006338 chromatin remodeling **(v)**; GO:0016514 SWI/SNF complex **(v)**; GO:0070603 SWI/SNF superfamily-type complex **(v)**; GO:0140658 ATP-dependent chromatin remodeler activity **(v)**.

**CHEBI:** CHEBI:231598 tazemetostat **(v)**; CHEBI:757766 tazemetostat hydrobromide **(v)**.

**NCIT (interventions):** NCIT:C131672 Gross Total Resection **(v)**; NCIT:C116437 Craniospinal Irradiation **(v)**; NCIT:C150522 Proton Beam Craniospinal Irradiation **(v)**; NCIT:C209869 Photon Beam Craniospinal Irradiation **(v)**; NCIT:C15358 Stereotactic Radiosurgery **(v)**; NCIT:C182204 Third Ventriculostomy **(v)**; NCIT:C168483 Ventriculoperitoneal Shunt Placement **(v)**; NCIT:C107506 Tazemetostat **(v)**; NCIT:C166954 Tazemetostat Hydrobromide **(v)**; NCIT:C186499 Tazemetostat Regimen **(v)**.

---

## Appendix B — Explicit evidence gaps (for knowledge-base curation)

The following template fields have **no retrievable evidence** for this disease and should be left null rather than imputed:

1. Prevalence and incidence rates (any denominator).
2. 5-year / 10-year survival; life expectancy; population mortality rate.
3. Quality-of-life measurements (any instrument).
4. Environmental, lifestyle, occupational, infectious, and radiation risk factors.
5. Protective factors (genetic or environmental).
6. Gene–environment interactions.
7. Modifier genes.
8. Germline *SMARCB1* alterations in DMT patients (searched; none reported).
9. Transcriptomic, proteomic, metabolomic, lipidomic, and single-cell/spatial profiles (no GEO dataset).
10. CNS WHO grade; ICD-O code; ICD-11 code; Orphanet code (grade and ICD-O explicitly "not assigned" per secondary sources and "no grading has been established so far" per PMID 42445896).
11. Validated prognostic or predictive biomarkers.
12. Any prospective trial, response rate, or toxicity profile in DMT.
13. Any animal, cell-line, organoid, or iPSC model of DMT.
14. Any naturally occurring animal counterpart (OMIA: no *SMARCB1* phene records).
15. Cell of origin (explicitly unknown — "no cell of origin has been identified to date," PMC13359088).

---

## Sources

**Primary literature on the entity**
- Thomas C, Wefers A, Bens S, et al. Desmoplastic myxoid tumor, SMARCB1-mutant: clinical, histopathological and molecular characterization of a pineal region tumor encountered in adolescents and adults. *Acta Neuropathol.* 2020;139(2):277–286. PMID 31732806. DOI 10.1007/s00401-019-02094-w — https://pubmed.ncbi.nlm.nih.gov/31732806/
- Matsumura N, Goda N, Yashige K, et al. Desmoplastic myxoid tumor, SMARCB1-mutant: a new variant of SMARCB1-deficient tumor of the central nervous system preferentially arising in the pineal region. *Virchows Arch.* 2021;479(4):835–839. PMID 33420834. DOI 10.1007/s00428-020-02978-3 — https://link.springer.com/article/10.1007/s00428-020-02978-3
- Wang YE, Chen JJ, Wang W, et al. A case of desmoplastic myxoid tumor, SMARCB1 mutant, in the pineal region. *Neuropathology.* 2021;41(1):37–41. PMID 32901946. DOI 10.1111/neup.12695 — https://pubmed.ncbi.nlm.nih.gov/32901946/
- Manoranjan B, Starreveld YP, Nordal RA, et al. Desmoplastic myxoid tumor of pineal region, SMARCB1-mutant, in young adult. *Free Neuropathol.* 2021;2:14. PMID 37284622. DOI 10.17879/freeneuropathology-2021-3340
- Manoranjan B, et al. Clinical management of desmoplastic myxoid tumor, SMARCB1-mutant. *Neuro Oncol.* 2022;24(5):847–848. PMID 35195707. DOI 10.1093/neuonc/noac016 — https://pmc.ncbi.nlm.nih.gov/articles/PMC9071305/
- Robinson LJ, Goold E, Anderson D, et al. A mass in the pineal region of a young woman. *Brain Pathol.* 2024;34(3):e13258. PMID 38527786. DOI 10.1111/bpa.13258 — https://pmc.ncbi.nlm.nih.gov/articles/PMC11007021/
- Zhou C, Zhang B, Wang B, et al. Desmoplastic myxoid tumor of the pineal region, SMARCB1 mutant: illustrative case. *J Neurosurg Case Lessons.* 2024;8(22):CASE24419. PMID 39586083. DOI 10.3171/CASE24419 — https://pmc.ncbi.nlm.nih.gov/articles/PMC11605529/
- Koren TJ, Back M, Chen J, Ahmad K. Desmoplastic myxoid tumor of the pineal region presenting with Parinaud syndrome. *J Neuropathol Exp Neurol.* 2026;85(3):303–305. PMID 40834270. DOI 10.1093/jnen/nlaf096
- Goyal A, Chawla P, Rajeswarie RT, et al. Desmoplastic Myxoid Tumor of the Pineal Region, SMARCB1-Mutant: Report of 2 Examples of an Extremely Rare Entity. *Int J Surg Pathol.* 2026;34(3):776–781. PMID 41259279. DOI 10.1177/10668969251389014
- Chang YW, Li YF, Chen YA, et al. Aggressive clinical behavior of desmoplastic myxoid tumor of the pineal region, SMARCB1-mutant. *Virchows Arch.* 2026 (online 17 Jul). PMID 42467229. DOI 10.1007/s00428-026-04652-6
- Kinoshita Y, Zhang XR, Esquenazi Y, Takei H. Intraoperative Imprint Cytology of SMARCB1-Mutant Desmoplastic Myxoid Tumor of the Pineal Region. *Ann Clin Lab Sci.* 2026;56(2):232–238. PMID 42259547
- Tauziède-Espariat A, Duchesne M, Rouchaud A, et al. Desmoplastic myxoid tumor, SMARCB1-mutant: a case with late recurrence after long-term follow-up. *Free Neuropathol.* 2026;7:16. PMID 42445896. DOI 10.17879/freeneuropathology-2026-9701 — https://pmc.ncbi.nlm.nih.gov/articles/PMC13359088/

**Classification, reviews and context**
- Louis DN, Perry A, Wesseling P, et al. The 2021 WHO Classification of Tumors of the Central Nervous System: a summary. *Neuro Oncol.* 2021;23(8):1231–1251. PMID 34185076 — https://pmc.ncbi.nlm.nih.gov/articles/PMC8328013/
- Hasselblatt M, Kool M, Frühwald MC. SWI/SNF-deficient tumors of the central nervous system: An update. *Clin Neuropathol.* 2024;43(1):2–9. PMID 37969088
- Pasquinelli E, Guidi M, Sardi I. Genetic landscape and molecular targets in pediatric pineal tumors. *Neurooncol Adv.* 2026;8(1):vdag086. PMID 42058762 — https://pmc.ncbi.nlm.nih.gov/articles/PMC13124280/
- Lombardi G, Poliani PL, Manara R, et al. Diagnosis and Treatment of Pineal Region Tumors in Adults: A EURACAN Overview. *Cancers.* 2022;14(15):3646. PMID 35954310 — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9367474/
- Tanguy R. Pineal Tumors and Pineal Region Tumors. *Adv Tech Stand Neurosurg.* 2026;54:269–294. PMID 42115465
- Mandera M, Antkowiak L. Pineal Gland Parenchyma Tumors. *Adv Tech Stand Neurosurg.* 2026;56:165–182. PMID 42393447
- Chatterjee D, Gupta K. Miscellaneous newly recognized types of CNS tumors in the WHO CNS5 classification. *Indian J Pathol Microbiol.* 2022;65(Suppl):S94–S98. PMID 35562139
- Prajapati HP, Kannaujia SK. A simplified overview of the WHO classification of CNS tumors 2021. *Surg Neurol Int.* 2022;13:252. PMID 35855126
- Bakhshi SK, et al. Consensus guidelines for the management of pineal region tumours for low- and middle-income countries. *J Pak Med Assoc.* 2024;74(3 Suppl-3):S135–S144. PMID 39262074
- Samkari A, et al. A bibliometric analysis of the top 100 most cited articles on pineal parenchymal tumors. *Brain Spine.* 2025;5:105608. PMID 41126818
- Price M, Ballard C, Benedetti J, et al. CBTRUS Statistical Report… 2017–2021. *Neuro Oncol.* 2024;26(Suppl 6):vi1–vi85. PMID 39371035
- Pathology Outlines — Desmoplastic myxoid tumor of the pineal region, SMARCB1 mutant — https://www.pathologyoutlines.com/topic/cnstumorSMARCB1mutant.html *(page returned HTTP 429 and could not be read directly; cited only for the ICD-O/grade "n/a" snippet surfaced in search results, flagged as unverified)*

**Mechanism, models and related SMARCB1-deficient tumors**
- Wang X, Lee RS, Alver BH, et al. SMARCB1-mediated SWI/SNF complex function is essential for enhancer regulation. *Nat Genet.* 2017;49(2):289–295. PMID 27941797
- Alver BH, Kim KH, Lu P, et al. The SWI/SNF chromatin remodelling complex is required for maintenance of lineage specific enhancers. *Nat Commun.* 2017;8:14648. PMID 28262751
- Wilson BG, Wang X, Shen X, et al. Epigenetic antagonism between polycomb and SWI/SNF complexes during oncogenic transformation. *Cancer Cell.* 2010;18(4):316–328. PMID 20951942
- Wang X, Wang S, Troisi EC, et al. BRD9 defines a SWI/SNF sub-complex and constitutes a specific vulnerability in malignant rhabdoid tumors. *Nat Commun.* 2019;10(1):1881. PMID 31015438
- Torchia J, Golbourn B, Feng S, et al. Integrated (epi)-Genomic Analyses Identify Subgroup-Specific Therapeutic Targets in CNS Rhabdoid Tumors. *Cancer Cell.* 2016;30(6):891–908. PMID 27960086
- Johann PD, Hovestadt V, Thomas C, et al. Cribriform neuroepithelial tumor: molecular characterization of a SMARCB1-deficient non-rhabdoid tumor with favorable long-term outcome. *Brain Pathol.* 2017;27(4):411–418. PMID 27380723
- Roberts CW, Galusha SA, McMenamin ME, et al. Haploinsufficiency of Snf5 (integrase interactor 1) predisposes to malignant rhabdoid tumors in mice. *PNAS* 2000;97(25):13796–13800. PMID 11095756
- Guidi CJ, Sands AT, Zambrowicz BP, et al. Disruption of Ini1 leads to peri-implantation lethality and tumorigenesis in mice. *Mol Cell Biol.* 2001;21(10):3598–3603. PMID 11313485
- Roberts CW, Leroux MM, Fleming MD, Orkin SH. Highly penetrant, rapid tumorigenesis through conditional inversion of the tumor suppressor gene Snf5. *Cancer Cell* 2002;2(5):415–425. PMID 12450796
- Gounder M, Schöffski P, Jones RL, et al. Tazemetostat in advanced epithelioid sarcoma with loss of INI1/SMARCB1. *Lancet Oncol.* 2020;21(11):1423–1432. PMID 33035459
- Frühwald MC, Nemes K, Boztug H, et al. Current recommendations for clinical surveillance and genetic testing in rhabdoid tumor predisposition: a report from the SIOPE Host Genome Working Group. *Fam Cancer* 2021;20(4):305–316. PMID 33532948 — https://pmc.ncbi.nlm.nih.gov/articles/PMC8484234/
- GeneReviews — Rhabdoid Tumor Predisposition Syndrome — https://www.ncbi.nlm.nih.gov/books/NBK469816/ *(blocked by CAPTCHA this session; penetrance/surveillance claims above are cited to PMID 33532948 instead)*

**Databases queried directly this session**
- MONDO via EBI OLS4 — https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?obo_id=MONDO:1060253
- NCI Thesaurus, HPO, UBERON, Cell Ontology, GO, ChEBI via EBI OLS4 — https://www.ebi.ac.uk/ols4/
- NCBI Gene / PubMed / ClinVar / MedGen E-utilities — https://eutils.ncbi.nlm.nih.gov/entrez/eutils/
- NCBI MedGen UID 322892 (RTPS1)
- Europe PMC REST (MeSH indexing for PMID 31732806) — https://www.ebi.ac.uk/europepmc/webservices/rest/
- gnomAD GraphQL API (SMARCB1 constraint, GRCh38) — https://gnomad.broadinstitute.org/
- ClinicalTrials.gov API v2 (query term "SMARCB1", retrieved 23 Nov 2026) — https://clinicaltrials.gov/
- OMIA (advanced search, gene_symbol SMARCB1 → no phene records) — https://omia.org/
- Genomics England PanelApp (SMARCB1 on panels 600, 1636) — https://panelapp.genomicsengland.co.uk/

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 51 |
| Resolved | 50 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:1060253` (7 mentions) - the report calls it "if available", "desmoplastic myxoid tumor of the pineal region, SMARCB1-mutant", "MONDO"; MONDO calls it **desmoplastic myxoid tumor of the pineal region, SMARCB1-mutant**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:1060253` - called "if available", "desmoplastic myxoid tumor of the pineal region, SMARCB1-mutant", "MONDO"

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 70 |
| Resolved | 70 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 103 |
| Quoted claims found in source | 62 |
| Quoted claims **not** found in source | 41 |
| Quoted claims with nothing to check against | 19 |
| References weighed for topical relevance | 70 |
| On topic | 33 |
| Off topic | 1 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

19 of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMC:PMC13124280` *(abstract only)*: "No germline predisposition established for DMT specifically"
  - closest text in source: "This review provides a comprehensive overview of the current molecular landscape of pineal region tumors, with a particular focus on genetic predisposition, somatic driver alterations, DNA methylation profiles, and transcriptional programs across pineocytoma, pineal parenchymal tumor of intermediate differentiation (PPTID), pineoblastoma, papillary tumor of the pineal region (PTPR), and desmoplastic myxoid tumor, SMARCB1-mutant"
- `PMID:33532948` *(abstract only)*: "patients with 'SMARCB1-deficient non-RT neoplasms' should be offered genetic testing on a research basis and, if positive for a PV, cancer surveillance"
  - closest text in source: "Beyond RT, the tumor spectrum may be larger than initially suspected, and cancer surveillance offered to unaffected carriers (siblings or parents) and long-term survivors of RT is still a matter of discussion"
- `DOI:10.1007/s10689-021-00229-1` *(abstract only)*: "patients with 'SMARCB1-deficient non-RT neoplasms' should be offered genetic testing on a research basis and, if positive for a PV, cancer surveillance"
  - closest text in source: "Beyond RT, the tumor spectrum may be larger than initially suspected, and cancer surveillance offered to unaffected carriers (siblings or parents) and long-term survivors of RT is still a matter of discussion"
- `PMC:PMC8484234` *(abstract only)*: "patients with 'SMARCB1-deficient non-RT neoplasms' should be offered genetic testing on a research basis and, if positive for a PV, cancer surveillance"
  - closest text in source: "Beyond RT, the tumor spectrum may be larger than initially suspected, and cancer surveillance offered to unaffected carriers (siblings or parents) and long-term survivors of RT is still a matter of discussion"
- `PMC:PMC11605529`: "**No pediatric cases reported**"
  - Text part not found as substring: '**No pediatric cases reported**'
- `PMC:PMC13359088`: "space-occupying lesion in the pineal region with obstructive hydrocephalus"
  - closest text in source: "Brain computed tomography (CT) and magnetic resonance imaging (MRI) (Figure 1A–I) demonstrated a space-occupying lesion in the pineal region associated with obstructive hydrocephalus"
- `PMC:PMC13359088`: "symptoms consistent with raised intracranial pressure"
  - closest text in source: "The current observation concerns a previously healthy 33-year-old man who presented with symptoms of intracranial hypertension"
- `PMID:39586083`: "paralysis of upward gaze… clinically combined with typical Parinaud's syndrome"
  - closest text in source: "LESSONS: This case showed a patient with DMT, SMARCB1 mutant with a relatively low Ki-67 proliferation index (less than 1%), clinically combined with typical Parinaud's syndrome"
- `PMC:PMC11605529`: "progressive drowsiness"
  - Text part not found as substring: 'progressive drowsiness'
- `PMID:42445896`: "Not classified by **DKFZ classifier v12.8** (as DMT is absent from this classifier)"
  - closest text in source: "DNA-methylation profiling classified the sample as DMT (using the NIH classifier v2.0 with a calibrated score of 0.84, whereas it was not classified using the DKFZ classifier v12.8, as expected, given that DMT is not included in this last classifier)"
- `PMC:PMC13359088`: "Not classified by **DKFZ classifier v12.8** (as DMT is absent from this classifier)"
  - closest text in source: "DNA-methylation profiling classified the sample as DMT (using the NIH classifier v2.0 with a calibrated score of 0.84, whereas it was not classified using the DKFZ classifier v12.8, as expected, given that DMT is not included in this last classifier)"
- `PMC:PMC13124280` *(abstract only)*: "**segregate away from the major AT/RT methylation subgroups**"
  - closest text in source: "This review provides a comprehensive overview of the current molecular landscape of pineal region tumors, with a particular focus on genetic predisposition, somatic driver alterations, DNA methylation profiles, and transcriptional programs across pineocytoma, pineal parenchymal tumor of intermediate differentiation (PPTID), pineoblastoma, papillary tumor of the pineal region (PTPR), and desmoplastic myxoid tumor, SMARCB1-mutant"
- `PMID:31732806` *(abstract only)*: "Loss of chromosome 22q, observed as a focal deletion in the majority of evaluable cases"
  - closest text in source: "All cases showed loss of nuclear SMARCB1/INI1 protein expression, expression of EMA and CD34 was frequent and the Ki67/MIB1 proliferation index was low in the majority of cases (median 3%)"
- `PMC:PMC13124280` *(abstract only)*: "Loss of chromosome 22q, observed as a focal deletion in the majority of evaluable cases"
  - Text part not found as substring: 'Loss of chromosome 22q, observed as a focal deletion in the majority of evaluable cases' (note: only abstract available for PMID:42058762, full text may contain this excerpt)
- `PMID:27941797` *(abstract only)*: "SMARCB1 is required for the integrity of SWI/SNF complexes and… its loss alters enhancer targeting"
  - closest text in source: "We show that SMARCB1 is required for the integrity of SWI/SNF complexes and that its loss alters enhancer targeting-markedly impairing SWI/SNF binding to typical enhancers, particularly those required for differentiation, while maintaining SWI/SNF binding at super-enhancers"
- `PMID:20951942`: "loss of the SNF5 tumor suppressor leads to elevated expression of the Polycomb gene EZH2 and… Polycomb targets are broadly H3K27-trimethylated and repressed in SNF5-deficient fibroblasts and cancers… inactivation of Ezh2 blocks tumor formation driven by Snf5 loss"
  - closest text in source: "Mechanistically, we show that loss of the SNF5 tumor suppressor leads to elevated expression of the Polycomb gene EZH2 and that Polycomb targets are broadly H3K27-trimethylated and repressed in SNF5-deficient fibroblasts and cancers"
- `PMID:37284622`: "irregular anastomosing collagenous structures"
  - Text part not found as substring: 'irregular anastomosing collagenous structures'
- `PMC:PMC13359088`: "irregular anastomosing collagenous structures"
  - Text part not found as substring: 'irregular anastomosing collagenous structures'
- `PMC:PMC13359088`: "a space-occupying lesion in the pineal region with obstructive hydrocephalus"
  - closest text in source: "Brain computed tomography (CT) and magnetic resonance imaging (MRI) (Figure 1A–I) demonstrated a space-occupying lesion in the pineal region associated with obstructive hydrocephalus"
- `PMC:PMC11605529`: "a space-occupying lesion in the pineal region with obstructive hydrocephalus"
  - closest text in source: "Imaging studies showed a pineal region mass with obstructive hydrocephalus"
- `PMID:42467229` *(abstract only)*: "discohesive rhabdoid cells embedded within a prominent myxoid stroma… highlights the potential for aggressive biological behavior despite relatively low-grade histologic features"
  - closest text in source: "This case expands the clinicopathologic spectrum of DMT-SMARCB1 and highlights the potential for aggressive biological behavior despite relatively low-grade histologic features."
- `PMC:PMC11605529`: "extensive hemorrhage, necrosis, and inflammatory infiltration"
  - closest text in source: "The pathological results showed extensive hemorrhage, necrosis, and inflammatory cell infiltration in the tissues"
- `PMC:PMC13359088`: "intercellular junctions, vesicular endocytosis and finger-like cytoplasmic extensions corresponding to microvilli"
  - closest text in source: "Several intercellular junctions are present (C, white arrow), as well as vesicular endocytosis (C, white arrow) and finger-like cytoplasmic extensions corresponding to microvilli (D, white arrow)"
- `PMID:35195707`: "all cases occurred in the pineal region"
  - closest text in source: "Of note, all prior cases have been in the pineal region"
- `PMC:PMC11605529`: "dilated third and lateral ventricles"
  - closest text in source: "Magnetic resonance imaging (MRI) demonstrated a type of round abnormal mass in the pineal area, measuring about 21 mm × 17 mm, isointense on T1-weighted imaging, mixed low signal on T2–fluid-attenuated inversion recovery (FLAIR), and low signal on diffusion-weighted imaging (DWI) and apparent diffusion coefficient (ADC) sequences, with no obvious enhancement within the mass; the third ventricle and lateral ventricles were dilated (Fig"
- `PMC:PMC13359088`: "intercellular junctions, vesicular endocytosis and finger-like cytoplasmic extensions corresponding to microvilli"
  - closest text in source: "Several intercellular junctions are present (C, white arrow), as well as vesicular endocytosis (C, white arrow) and finger-like cytoplasmic extensions corresponding to microvilli (D, white arrow)"
- `PMC:PMC13124280` *(abstract only)*: "approximately 3%-11% of all pediatric brain tumors, compared to less than 1% in adults"
  - closest text in source: "Pineal region tumors are rare and biologically heterogeneous central nervous system neoplasms that occur predominantly in the pediatric population and are associated with significant morbidity and mortality"
- `PMID:33532948` *(abstract only)*: "In patients with RTPS1 penetrance may be extremely high (e.g. > 90% by 5 years)"
  - closest text in source: "The penetrance of RTPS1 early in life is high and associated with a poor survival"
- `PMID:33532948` *(abstract only)*: "Among newly diagnosed cases of MRT 25–35% carry a germline PV in *SMARCB1* (RTPS1)"
  - closest text in source: "In contrast to other genetic disorders related to PVs in SMARCB1 and SMARCA4 such as Coffin-Siris Syndrome, RTPS1&2 are characterized by a predominance of truncating PVs, terminating transcription thus explaining a specific cancer risk"
- `PMID:41259279` *(abstract only)*: "The histology and **polyphenotypic** nature pose diagnostic dilemmas"
  - closest text in source: "The histology and polyphenotypic nature of the tumor pose diagnostic dilemmas"
- `PMID:33532948` *(abstract only)*: "patients with 'SMARCB1-deficient non-RT neoplasms' should be offered genetic testing **on a research basis** and, if positive for a PV, cancer surveillance"
  - closest text in source: "Beyond RT, the tumor spectrum may be larger than initially suspected, and cancer surveillance offered to unaffected carriers (siblings or parents) and long-term survivors of RT is still a matter of discussion"
- `PMC:PMC13124280` *(abstract only)*: "disease-related mortality has been observed in 3 of 7 patients after a median follow-up of approximately 48 months"
  - closest text in source: "Pineal region tumors are rare and biologically heterogeneous central nervous system neoplasms that occur predominantly in the pediatric population and are associated with significant morbidity and mortality"
- `PMC:PMC11605529`: "subtotal resection, Ki-67 15%, treated with radiotherapy"
  - closest text in source: "Under the selected treatment, 1 patient developed tumor progression (subtotal resection, Ki-67 15%, treated with postoperative radiotherapy), 3 patients died of the disease, and the remaining patients had stable disease or no evidence of recurrence, with a median follow-up period of 27.6 months"
- `PMC:PMC11605529`: "Only 2 patients exceeded 10% (15% and 15.4%), indicating generally non-aggressive biology"
  - closest text in source: "In terms of malignant and aggressive clinical manifestations, only 2 patients had a Ki-67 proliferation index higher than 10% (15% and 15.4%, respectively), and 1 patient with cerebrospinal fluid spread was reported"
- `PMID:35195707`: "emphasize the need for case curation to establish prognostic factors and develop standardized therapeutic protocols for this newly recognized tumor entity"
  - closest text in source: "Collectively, this report highlights the importance of recognizing this new tumor entity and curation of cases to determine prognosis and the optimal therapeutic protocol for patients diagnosed with DMT, SMARCB1-mutant"
- `PMC:PMC11605529`: "No adjuvant therapy was administered given gross-total resection, well-differentiated morphology, and very low proliferation index"
  - closest text in source: "Considering that the patient’s tumor was removed by gross-total resection, tissue morphology was well differentiated, and the Ki-67 proliferation index was less than 1%, which is the lowest in all the literature, no further treatment was given and regular follow-up was recommended"
- `PMC:PMC11605529`: "chemotherapy plus radiotherapy"
  - Text part not found as substring: 'chemotherapy plus radiotherapy'
- `PMC:PMC13124280` *(abstract only)*: "**dedicated clinical evidence in DMT-SMARCB1 is currently lacking**"
  - closest text in source: "Recent advances in genomic, epigenomic, and transcriptomic profiling have fundamentally reshaped the understanding of these tumors, moving beyond purely histological classification toward molecularly defined subgroups with distinct biological behavior and clinical outcomes"
- `PMID:31015438` *(abstract only)*: "BRD9 is a specific vulnerability in pediatric malignant rhabdoid tumors (RTs), which are driven by inactivation of the SMARCB1 subunit of SWI/SNF… a BRD9-containing SWI/SNF subcomplex is required for the survival of SMARCB1-mutant RTs"
  - closest text in source: "Here, using a genome-wide CRISPR-Cas9 screen, we show that BRD9 is a specific vulnerability in pediatric malignant rhabdoid tumors (RTs), which are driven by inactivation of the SMARCB1 subunit of SWI/SNF"
- `PMID:33532948` *(abstract only)*: "patients with 'SMARCB1-deficient non-RT neoplasms' should be offered genetic testing on a research basis and, if positive for a PV, cancer surveillance"
  - closest text in source: "Beyond RT, the tumor spectrum may be larger than initially suspected, and cancer surveillance offered to unaffected carriers (siblings or parents) and long-term survivors of RT is still a matter of discussion"
- `PMID:33532948` *(abstract only)*: "In patients with RTPS1 penetrance may be extremely high (e.g. > 90% by 5 years)"
  - closest text in source: "The penetrance of RTPS1 early in life is high and associated with a poor survival"

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:35195767` (1 mention) - Etiologies and treatments of chronic intestinal failure-short bowel syndrome (SBS) in Japanese adults: a real-world observational study.
  - shared terms: patient, year

Weighed against this report's own most characteristic terms: `tumor`, `dmt`, `smarcb1`, `pineal`, `pmc13359088`, `rhabdoid`, `pmc11605529`, `loss`, `myxoid`, `pmc11007021`, `ini1`, `cell`, `entity`, `region`, `desmoplastic`, `gene`, `patient`, `csf`, `year`, `dissemination`.

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `PMC:PMC11007021`: "a slight female predominance (F: 7; M: 4)"
  - Reference resolved but exposes no abstract or full text to search
- `PMC:PMC11007021`: "subacute, progressive headaches"
  - Reference resolved but exposes no abstract or full text to search
- `PMC:PMC11007021`: "obstructive hydrocephalus requiring ventriculoperitoneal shunt placement"
  - Reference resolved but exposes no abstract or full text to search
- `PMC:PMC11007021`: "an acute episode of sudden vision loss"
  - Reference resolved but exposes no abstract or full text to search
- `PMC:PMC11007021`: "previous reported DMTs were mainly inactivated by homozygous or heterozygous deletions or indels rather than point mutations"
  - Reference resolved but exposes no abstract or full text to search
- `PMC:PMC11007021`: "**Methylation profiling… with 0.99 confidence score**"
  - Reference resolved but exposes no abstract or full text to search
- `DOI:10.1038/ng.3746`: "SMARCB1 is required for the integrity of SWI/SNF complexes and… its loss alters enhancer targeting"
  - Reference resolved but exposes no abstract or full text to search
- `DOI:10.1016/j.ccr.2010.09.006`: "loss of the SNF5 tumor suppressor leads to elevated expression of the Polycomb gene EZH2 and… Polycomb targets are broadly H3K27-trimethylated and repressed in SNF5-deficient fibroblasts and cancers… inactivation of Ezh2 blocks tumor formation driven by Snf5 loss"
  - Reference resolved but exposes no abstract or full text to search
- `PMC:PMC11007021`: "Mitotic index was <1/10 high-power fields; necrosis was absent"
  - Reference resolved but exposes no abstract or full text to search
- `PMC:PMC11007021`: "many of the tumor cells"
  - Reference resolved but exposes no abstract or full text to search
- `PMC:PMC11007021`: "cerebral aqueduct effacement"
  - Reference resolved but exposes no abstract or full text to search
- `PMC:PMC11007021`: "extension into the third and right lateral ventricles"
  - Reference resolved but exposes no abstract or full text to search
- `PMC:PMC11007021`: "bilateral thalamic splaying"
  - Reference resolved but exposes no abstract or full text to search
- `PMC:PMC11007021`: "8 mm tonsillar herniation"
  - Reference resolved but exposes no abstract or full text to search
- `PMC:PMC11007021`: "an admixture of small to medium-sized spindle cells embedded in a heavily collagenized and myxoid matrix"
  - Reference resolved but exposes no abstract or full text to search
- `PMC:PMC11007021`: "subacute, progressive headaches, and an acute episode of sudden vision loss"
  - Reference resolved but exposes no abstract or full text to search
- `PMC:PMC11007021`: "a slight female predominance (F: 7; M: 4)"
  - Reference resolved but exposes no abstract or full text to search
- `PMC:PMC11007021`: "was excluded by negative **EWSR1 and FUS** testing"
  - Reference resolved but exposes no abstract or full text to search
- `PMC:PMC11007021`: "discharged with no new neurologic deficits"
  - Reference resolved but exposes no abstract or full text to search
