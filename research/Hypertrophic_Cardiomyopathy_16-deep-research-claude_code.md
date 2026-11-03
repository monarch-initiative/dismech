---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-13T14:03:17.055077'
end_time: '2026-10-13T14:05:27.590146'
duration_seconds: 130.54
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Hypertrophic Cardiomyopathy 16
  mondo_id: MONDO:0013455
  category: Genetic
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
  web_search_requests: 1
  num_turns: 11
  total_cost_usd: 1.6652696000000002
  session_id: 4d93de47-ca51-4048-ba06-db86bfcf704a
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  assistant_text_blocks: 2
citation_count: 10
reference_validation:
  total_references: 15
  verified: 15
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 15
  on_topic: 9
  off_topic: 1
  off_topic_references:
  - PMID:7618393
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 35
  verified: 31
  not_found: 0
  obsolete: 0
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 10
  labels_matching: 4
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: MONDO:0013455
    reported_labels:
    - MONDO
    ontology_label: hypertrophic cardiomyopathy 16
  - term_id: HP:0031645
    reported_labels:
    - verify
    ontology_label: Saccular abdominal aortic aneurysm
  - term_id: HP:0025168
    reported_labels:
    - verify
    ontology_label: Left ventricular diastolic dysfunction
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
- **Disease Name:** Hypertrophic Cardiomyopathy 16
- **MONDO ID:** MONDO:0013455 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Hypertrophic Cardiomyopathy 16** covering all of the
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

I'm pulling the primary MYOZ2/CMH16 sources (Osio 2007, the Posch 2008 screen, ClinGen) and will then write the report.

# Hypertrophic Cardiomyopathy 16 (CMH16; MYOZ2-related HCM): research report

**Bottom line for curation.** CMH16 is a single-gene subtype of autosomal-dominant hypertrophic cardiomyopathy (HCM) attributed to heterozygous missense variants in **MYOZ2**. MYOZ2 encodes myozenin-2, also called calsarcin-1. It is a sarcomeric Z-disc protein that binds calcineurin and α-actinin. The human genetic evidence is thin:

- **One linkage family:** a family with six affected members, carrying the S48P variant (Osio et al. 2007, PMID:17347475).
- **One sporadic missense:** I246M, found by screening 516 probands in the same study.
- **A negative replication:** a screen of 438 European familial-HCM patients found no disease-causing MYOZ2 mutations (PMID:18591919).
- **A large burden study** that does not support most minor HCM genes (PMID:27532257).

**ClinGen moved MYOZ2–HCM from Limited to Disputed on 2022-10-27.** A KB entry should state this up front. Most mechanistic content comes from mice and cell culture.

The verbatim quotes below come from the abstracts already cached in this worktree's `references_cache/` (7 PMIDs plus the ClinGen record). PMIDs that are not yet cached are marked **[not cached]**. Run `just fetch-reference` on those before quoting them.

---

## 1. Disease information

**What it is.** CMH16 is left ventricular hypertrophy (LVH) caused by a MYOZ2 mutation, without another explanation for the hypertrophy. MedGen defines it as "hypertrophic cardiomyopathy in which the cause of the disease is a mutation in the MYOZ2 gene."

| Identifier | Value | Status |
|---|---|---|
| MONDO | MONDO:0013455 | given in the prompt; also listed by DrugMap |
| OMIM (phenotype) | 613838 "Cardiomyopathy, familial hypertrophic, 16" | confirmed via LOVD |
| MedGen | 462554 / UMLS C3151204 | MedGen search result |
| Gene | MYOZ2, 4q26; HGNC:1330 (written `hgnc:1330` in this repo); NCBI Gene 51778 | HGNC from the ClinGen record; Gene ID from GenScript |
| Gene OMIM | 605602 | from memory — verify |
| UniProt | Q9NPC6 | from memory — verify |
| Orphanet | no CMH16-specific ORPHA code found; the parent is familial isolated HCM (ORPHA:217569, from memory — verify) | |
| ICD-10 / ICD-11 | parent only: I42.1 / I42.2 (obstructive / other HCM); BC43.1 in ICD-11 | |
| Parent MONDO (used by ClinGen) | MONDO:0005045 hypertrophic cardiomyopathy | ClinGen record |

**Synonyms:** CMH16; familial hypertrophic cardiomyopathy 16; MYOZ2-related HCM; calsarcin-1-related HCM.

**Source of the information:** aggregated disease-level resources (OMIM, MedGen, ClinGen, LOVD, PanelApp) plus a handful of family and cohort reports. There are no EHR or registry data specific to MYOZ2.

## 2. Etiology

**Cause.** Heterozygous germline missense variants in MYOZ2 (autosomal dominant).
- Osio et al. 2007 (Circ Res, PMID:17347475 **[not cached]**): genome-wide linkage in a family with six affected members, after four known sarcomere genes had been excluded, mapped HCM to 4q26–q27. Sequencing MYOZ2 there found **p.Ser48Pro (S48P)**, which segregated with disease and was absent from several hundred control chromosomes. Screening 516 HCM probands found a second missense, **p.Ile246Met (I246M)**. The authors concluded: "We conclude MYOZ2 is a novel causal gene for human HCM."

**Contrary and diluting evidence.**
- Posch et al. 2008 (Med Sci Monit, PMID:18591919 **[not cached]**): MYOZ2 sequencing in 438 European familial-HCM patients found only two non-synonymous polymorphisms and no disease-causing mutations. The authors concluded MYOZ2 mutations are a rare cause of familial HCM.
- Walsh et al. 2017 (Genet Med, PMID:27532257 **[not cached]**) compared 7,855 cardiomyopathy cases with 60,706 ExAC reference samples. Rare variants in many previously reported "minor" HCM genes showed no case excess. Use this as background for the ClinGen downgrade; check the supplement before claiming a MYOZ2-specific result.
- Guo et al. 2017 (PMID:28296734): a five-generation Chinese family carried both **MYH7-A719H** and **MYOZ2-L169G**. Quote: "The sarcomere gene mutations MYH7-A719H and MYOZ2-L169G were detected in the HCM individuals in this pedigree." ClinGen excluded L169G as causative because of the co-occurring MYH7 variant. The paper's own framing is that "Multiple gene mutations may contribute to genetic anticipation in HCM."
- Cecconi et al. 2016 (PMID:27600940): a targeted 19-gene NGS panel in Italian HCM patients reported a MYOZ2 variant among non-thick/thin-myofilament genes. Quote: "mutations in genes encoding only the non-TTm proteins are identifiable in patients with a milder HCM status."
- Tran et al. 2024 (PMID:39682617): exome sequencing of Vietnamese cardiomyopathy patients reported a MYOZ2 **variant of uncertain significance**. The cohort was mainly dilated cardiomyopathy (DCM). Quote: "four were variants of uncertain significance in the ACTA2, ANK2, MYOZ2, and PRKAG2 genes." This is weak evidence and is not about HCM.

**ClinGen** (cached record `CGGV:assertion_d74395ba-…-2022-10-27T160000.000Z`): "MYOZ2 | HGNC:1330 | hypertrophic cardiomyopathy | MONDO:0005045 | AD | Disputed". Curation summary: "The MYOZ2 gene has been related with HCM in 7 probands across 4 publications… The mechanism for disease is unknown." In KB terms this is `gene_disease_validity: DISPUTED, classified_by: CLINGEN`. **PanelApp** (Genomics England HCM panel) lists MYOZ2 as Red, low evidence.

**Risk factors.** None are specific to MYOZ2. General HCM modifiers apply, with low certainty: hypertension, obesity, and co-occurring sarcomere variants (digenic or compound states, as in Guo 2017).

**Protective factors and gene–environment interactions.** None documented in humans. The mouse data below show that MYOZ2 loss sensitizes the heart specifically to pressure overload, which suggests an interaction with afterload in principle. This has not been shown in patients.

## 3. Phenotypes

Patient-level data are limited to the Osio family and a few probands. Frequencies are therefore not available. HP IDs below are **suggestions to verify with `runoak`**; they are not checked bindings.

| Phenotype | Suggested HPO (verify) | Notes |
|---|---|---|
| Left ventricular hypertrophy / asymmetric septal hypertrophy | HP:0001712 LVH; HP:0001670 asymmetric septal hypertrophy | defining feature |
| Hypertrophic cardiomyopathy | HP:0001639 | disease-level |
| LV outflow tract obstruction | HP:0031645 (verify) | not reported specifically for MYOZ2 |
| Diastolic dysfunction | HP:0025168 (verify) | |
| Myocardial interstitial fibrosis | HP:0031319? (verify) | seen in mice (Ruggiero 2013) |
| Arrhythmia / atrial fibrillation | HP:0011675 / HP:0005110 | general HCM |
| Sudden cardiac death | HP:0001645 | reported in the Guo family, but confounded by MYH7 |
| Dyspnea, chest pain, syncope, palpitations | HP:0002094, HP:0100749, HP:0001279, HP:0001962 | general HCM symptoms |

- **Onset:** adolescence to adulthood; age-dependent, as in HCM generally.
- **Severity:** the Cecconi data suggest milder disease for non-myofilament genes.
- **Quality of life:** no MYOZ2-specific data. HCM in general reduces exercise capacity, and quality of life is measured with the KCCQ in trials.

## 4. Genetic and molecular information

- **Gene:** MYOZ2 (myozenin-2 / calsarcin-1 / FATZ-related protein 2), 264 aa. It belongs to the calsarcin family together with MYOZ1 (calsarcin-2) and MYOZ3. In adults it is expressed in heart and slow-twitch muscle. Frey 2000 (PMID:11114196): "calsarcin-1 is expressed specifically in adult cardiac and slow-twitch skeletal muscle." The same paper describes the binding role: calsarcins "tether calcineurin to alpha-actinin at the z-line of the sarcomere."
- **Variants:**
  - S48P — segregating in the linkage family
  - I246M — single proband
  - L169G — co-occurs with MYH7, excluded by ClinGen
  - further missense variants from panel studies, with no functional support
- **Variant class and origin:** germline heterozygous missense. No LoF, CNV or structural variants have been reported as causal. ClinVar entries are predominantly VUS or conflicting (check ClinVar live).
- **Mechanism of variant action:** unknown. ClinGen states it explicitly. The mouse data suggest a dominant structural (Z-disc) effect rather than simple haploinsufficiency (see §6). Note that Myoz2⁻/⁻ mice do not develop spontaneous hypertrophy.
- **Modifiers, epigenetics, chromosomal abnormalities:** none reported.

## 5. Environmental information

No toxins, infections or lifestyle factors are specific to CMH16. In general HCM, strenuous exertion is a historical trigger for sudden cardiac death; current guidelines permit individualised exercise. Pressure overload is the experimentally relevant stressor in mice (§6).

## 6. Mechanism and pathophysiology

**Ordered causal chain.** The provisional parts are labelled.
1. A heterozygous MYOZ2 missense variant (S48P, I246M) **produces** a mutant myozenin-2 that still incorporates into the Z-disc, co-localising with α-actinin. *Mouse data.*
2. The mutant protein **leads to** Z-disc disruption and misalignment. *Shown by electron microscopy in transgenic mice.*
3. Z-disc mechanosensing and signalling are altered, which **results in** changes in ERK1/2 and JNK MAPK phosphorylation. *Mouse data; that this step causes hypertrophy is inferred.*
   - **Branch, not supported for mutants:** loss of calcineurin inhibition → NFAT activation. Shown for *knockout* mice, but calcineurin activity was **unchanged** in mutant-transgenic mice.
4. Activation of the hypertrophic gene programme (ANF, BNP) **leads to** cardiomyocyte hypertrophy.
5. Cardiomyocyte hypertrophy plus interstitial fibrosis **result in** LVH with preserved systolic function, and then the clinical HCM phenotype. Diastolic dysfunction and arrhythmia are *inferred from HCM in general*.

**Key evidence.**
- **Ruggiero et al. 2013 (PMID:22987565, cached, full text):** the authors generated transgenic mice expressing MYOZ2 S48P or I246M on a hemizygous endogenous background (Myoz2+/−).
  - "Mutant MYOZ2 mice showed molecular, cellular, and gross cardiac hypertrophy, preserved systolic function, and interstitial fibrosis."
  - "Electron microscopy showed disrupted and mal-aligned Z disks in the mutant mice."
  - Calcineurin activity "was unchanged in the mutant transgenic mice. However, levels of phospho-ERK1/2 and JNK54/46 were altered."
  - Conclusion: "the cardiac phenotype in HCM caused by MYOZ2 mutations might be independent of calcineurin activity… Z disk abnormalities might provide the stimulus for the induction of cardiac hypertrophy."
- **Frey et al. 2004 (PMID:15543153, cached):** in Myoz2 knockout mice, "calsarcin-1 negatively modulates the functions of calcineurin." Loss "activated a hypertrophic gene program, despite the absence of hypertrophy, and enhanced the cardiac growth response to pressure overload."
- **Frank et al. 2007 (PMID:18025526, cached):** with overexpression, "CS1 prevents Ang-II-induced cardiomyocyte hypertrophy at least in part via inhibition of calcineurin signaling."

**Interpretation.** Loss-of-function biology (knockout → calcineurin disinhibition) and the disease-variant biology (Z-disc disruption, calcineurin-independent) **disagree**. This is a good place for a `KNOWLEDGE_GAP` or `HUMAN_MODEL_MISMATCH` discussion. Human tissue, iPSC-cardiomyocyte, transcriptomic and proteomic data specific to MYOZ2 variants do not appear to exist; I found no GEO or PRIDE datasets.

**Suggested ontology terms (verify every one):**
- **GO biological processes:** calcineurin-NFAT signaling cascade (GO:0033173); negative regulation of calcineurin-NFAT signaling (GO:0070884); cardiac muscle hypertrophy (GO:0003300); ERK1 and ERK2 cascade (GO:0070371); JNK cascade (GO:0007254); Z disc (CC, GO:0030018).
- **CL cell types:** cardiac muscle cell (CL:0000746); fibroblast of cardiac tissue (CL:0002548).

## 7. Anatomical structures

- **Organ:** heart. Left ventricle (UBERON:0002084) and interventricular septum (UBERON:0002094); verify both IDs.
- **Secondary involvement:** left atrium, through AF and dilation.
- **Tissue:** myocardium (UBERON:0002349).
- **Subcellular:** sarcomeric Z-disc.
- **Skeletal muscle:** slow-twitch fibres express MYOZ2, and knockout mice have excess slow fibres. No skeletal myopathy has been reported in patients.
- **Lateralization:** asymmetric LV and septal hypertrophy.

## 8. Temporal development

Onset in adolescence or adulthood, insidious and age-dependent. Disease is slowly progressive or stable, with stages from preclinical genotype-positive through to the uncommon end-stage burnt-out form. The Guo family showed anticipation (median onset 63.5 → 38.5 → 18 years over three generations), but this is confounded by the MYH7 variant and accumulating variants. It **should not be attributed to MYOZ2**.

## 9. Inheritance and population

- **Inheritance:** autosomal dominant (HP:0000006). Penetrance is incomplete and age-dependent, as inferred for HCM generally; no MYOZ2-specific estimate exists. Expressivity is variable.
- **Prevalence:** HCM overall is about 1 in 500 (Maron 1995 CARDIA, PMID:7618393 **[not cached]**). The MYOZ2 share is too small to estimate: 1 of 516 probands in Osio, 0 of 438 in Posch.
- **Prevalence class:** ultra-rare, effectively cases in the literature (fewer than 10 probands).
- **Founder effects, sex ratio:** none known.

## 10. Diagnostics

- **Imaging:** echocardiography or cardiac MRI showing wall thickness ≥15 mm, or ≥13 mm in relatives. Late gadolinium enhancement shows fibrosis.
- **Other tests:** ECG, Holter, exercise testing, NT-proBNP.
- **Genetic testing:** a multigene HCM panel or exome. MYOZ2 is not in the ClinGen-curated core HCM genes; with a Disputed classification, a MYOZ2 variant generally should **not** be used for cascade testing (2023 ESC and 2024 AHA/ACC guidance on genes with limited evidence).
- **Differential diagnosis:**
  - other sarcomeric HCM (MYH7, MYBPC3)
  - Fabry disease (GLA)
  - PRKAG2 disease
  - Danon disease (LAMP2)
  - TTR amyloid
  - RASopathies
  - athlete's heart
  - hypertensive heart disease

## 11. Outcome and prognosis

No MYOZ2-specific data exist. For HCM generally, annual mortality is under 1% with contemporary care. The main complications are AF, heart failure, stroke and sudden cardiac death. SCD risk is assessed with the HCM Risk-SCD calculator or the AHA risk factors.

## 12. Treatment

All of this is generic HCM management, from the 2024 AHA/ACC guideline (PMID:38718139) and the 2023 ESC cardiomyopathy guideline (PMID:37622657); both **[not cached]**.

- **Pharmacotherapy** (NCIT:C15986 Pharmacotherapy):
  - beta-blockers and non-dihydropyridine calcium-channel blockers
  - disopyramide
  - cardiac myosin inhibitors: mavacamten (EXPLORER-HCM, PMID:32871100) and aficamten (SEQUOIA-HCM, PMID:38739079), both **[not cached]**
  - anticoagulation for AF
- **Procedures:**
  - septal myectomy (NCIT:C15329 Surgical Procedure; carry the detail in `preferred_term`)
  - alcohol septal ablation
  - ICD implantation for SCD prevention (device-qualifier pattern)
  - transplantation (NCIT:C15289 Organ Transplantation) for end-stage disease
- **Genetic counseling** (NCIT:C15240).
- **No gene-specific or advanced therapy:** none exists for MYOZ2. Calcineurin modulation was proposed from mouse work (Frank 2007), but it is experimental only and has no trials.

## 13. Prevention

- **Primary prevention:** none.
- **Secondary prevention:** clinical screening of first-degree relatives with ECG and echo, regardless of genotype. Because MYOZ2 is Disputed, use clinical surveillance rather than predictive genotyping.
- **Tertiary prevention:** SCD risk stratification and ICD; AF anticoagulation.

## 14. Other species

- **Natural disease:** feline HCM is common, but it is linked to MYBPC3 (Maine Coon, Ragdoll) and not to MYOZ2. No natural MYOZ2 disease is known in animals (check OMIA).
- **Orthologs:** Myoz2 in mouse; ZFIN has a myoz2 record (ZDB-GENE-040426-1853).

## 15. Model organisms

| Model | Phenotype | Fidelity |
|---|---|---|
| Myoz2⁻/⁻ mouse (Frey 2004) | calcineurin hyperactivity, excess slow fibres, fetal gene programme without hypertrophy; exaggerated hypertrophy after pressure overload (TAC) | partial: models loss of function, not the disease variants |
| Transgenic MYOZ2 S48P / I246M on Myoz2+/− (Ruggiero 2013; MGI alleles MGI:5581488 and MGI:5581489) | LVH, interstitial fibrosis, preserved EF, Z-disc disruption, altered ERK/JNK, calcineurin unchanged | moderate; caveat that transgene levels were 15–48% of total MYOZ2 |
| Calsarcin-1 transgenic overexpression (Frank 2007) | protected against angiotensin-II-induced hypertrophy | mechanistic only |
| Neonatal rat cardiomyocytes, adenoviral or lentiviral expression | anti-hypertrophic effect of WT CS1; I246M did not change RCAN1.4 | in vitro |

No iPSC-cardiomyocyte or zebrafish models for MYOZ2 variants were found.

---

### Recommendations for the dismech entry
- **Record the ClinGen tier verbatim** in `gene_disease_validity` (DISPUTED, CLINGEN, cached CGGV id). `relationship_type: CAUSATIVE` would trigger the `overstated` audit class; consider a weaker type or a note.
- **Fetch before citing:** run `just fetch-reference` for PMID:17347475, 18591919, 27532257 and the guideline and trial PMIDs before quoting them. The abstracts were not retrievable verbatim in this session.
- **Model the calcineurin discordance** as a `HUMAN_MODEL_MISMATCH` or `KNOWLEDGE_GAP` discussion.
- **Re-check every HPO, GO, CL, UBERON and NCIT CURIE above.** Several were written from memory and are flagged as such.

### Sources
- [LOVD disease 03458 (CMH16, OMIM 613838)](https://databases.lovd.nl/shared/diseases/03458)
- [MedGen 462554](https://https.ncbi.nlm.nih.gov/medgen/462554)
- [DrugMap DISWMHYX (MONDO_0013455)](https://drugmap.idrblab.net/data/disease/details/DISWMHYX)
- [PanelApp HCM – MYOZ2](https://panelapp.genomicsengland.co.uk/panels/49/gene/MYOZ2/)
- [MGI alleles MGI:5581488](https://www.informatics.jax.org/allele/allgenoviews/MGI:5581488) and [MGI:5581489](https://www.informatics.jax.org/allele/allgenoviews/MGI:5581489)
- [ZFIN myoz2](https://zfin.org/ZDB-GENE-040426-1853)
- [GenScript MYOZ2 gene page](https://genscript.jp/gene/homo-sapiens/51778/myoz2.html)
- [PubMed efetch: PMIDs 17347475, 18591919, 27532257](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=17347475,18591919,27532257&rettype=abstract&retmode=text)
- Cached in this worktree: PMID:11114196, 15543153, 18025526, 22987565, 27600940, 28296734, 39682617, and the ClinGen CGGV record. ClinGen report: https://search.clinicalgenome.org/kb/gene-validity/CGGV:assertion_d74395ba-66ee-43c6-8d3c-c353bd8e5e82-2022-10-27T160000.000Z

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 15 |
| On topic | 9 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:7618393` (1 mention) - Importance of an early tissue transfer in the treatment of complicated injuries of lower extremities.
  - shared terms: none

Weighed against this report's own most characteristic terms: `myoz2`, `hcm`, `gene`, `disease`, `variant`, `clingen`, `cached`, `cardiac`, `hypertrophy`, `calcineurin`, `mice`, `family`, `mouse`, `cardiomyopathy`, `hypertrophic`, `found`, `z-disc`, `cmh16`, `i246m`, `proband`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 35 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 4 |
| Terms whose name was checked | 10 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0013455` (1 mention) - the report calls it "MONDO"; MONDO calls it **hypertrophic cardiomyopathy 16**
- `HP:0031645` (1 mention) - the report calls it "verify"; HP calls it **Saccular abdominal aortic aneurysm**
- `HP:0025168` (1 mention) - the report calls it "verify"; HP calls it **Left ventricular diastolic dysfunction**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0033173` (1 mention) - the report calls it "GO biological processes:** calcineurin-NFAT signaling cascade"; GO calls it **calcineurin-NFAT signaling cascade**
- `CL:0000746` (1 mention) - the report calls it "CL cell types:** cardiac muscle cell"; CL calls it **cardiac muscle cell**
- `UBERON:0002349` (1 mention) - the report calls it "Tissue:** myocardium"; UBERON calls it **myocardium**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.