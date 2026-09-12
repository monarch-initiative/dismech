---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-01T10:44:09.871340'
end_time: '2026-09-01T10:48:01.515064'
duration_seconds: 231.64
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Late-Onset Pompe Disease
  mondo_id: ''
  category: Mendelian
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
  - claude-sonnet-5
  web_search_requests: 17
  num_turns: 19
  total_cost_usd: 1.263194
  session_id: d5cd765e-d271-5e5a-b130-47a579a26048
  stop_reason: end_turn
  assistant_text_blocks: 3
citation_count: 70
reference_validation:
  total_references: 47
  verified: 47
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 0
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMC:PMC11638199
  quotes_not_checkable: 1
  relevance_assessed: 47
  on_topic: 38
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 44
  verified: 34
  not_found: 0
  obsolete: 1
  unverifiable: 9
  confabulation_rate: 0.0
  labels_checked: 30
  labels_matching: 18
  labels_mismatched: 6
  mislabelled_terms:
  - term_id: HP:0002996
    reported_labels:
    - Wheelchair dependence, if modeled
    ontology_label: Limited elbow movement
  - term_id: HP:0001680
    reported_labels:
    - WPW pattern
    ontology_label: Coarctation of aorta
  - term_id: HP:0001712
    reported_labels:
    - LVH
    ontology_label: Left ventricular hypertrophy
  - term_id: GO:0004339
    reported_labels:
    - "glycogen debranching enzyme activity \u2014 comparator pathway"
    ontology_label: glucan 1,4-alpha-glucosidase activity
  - term_id: CL:0000540
    reported_labels:
    - "neuron \u2014 motor neuron/phrenic pathway involvement"
    ontology_label: neuron
  - term_id: UBERON:0001086
    reported_labels:
    - diaphragm
    ontology_label: obsolete articular cartilage
  labels_variant: 6
  obsolete_terms:
  - term_id: UBERON:0001086
    ontology_label: obsolete articular cartilage
  unresolvable_prefixes:
  - OMIM
  - ORPHA
  - PubMed
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Late-Onset Pompe Disease
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Late-Onset Pompe Disease** covering all of the
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

Now let me gather more detail on molecular mechanism, phenotypes, treatment specifics, animal models, and other relevant sections.

Good progress. Let me gather a few more targeted details — molecular pathway/mTOR mechanism, cardiac involvement in LOPD, diagnostic criteria/differential diagnosis, and population/genetic risk factors.

I now have comprehensive material across all major sections. Let me compile the full research report.

# Late-Onset Pompe Disease (LOPD): Comprehensive Research Report

## 1. Disease Information

**Overview.** Late-onset Pompe disease (LOPD) is a progressive, treatable metabolic (lysosomal storage) myopathy caused by partial deficiency of acid α-glucosidase (GAA, acid maltase), the enzyme that hydrolyzes lysosomal glycogen to glucose. It is a subtype of Pompe disease (glycogen storage disease type II, acid maltase deficiency), distinguished from infantile-onset Pompe disease (IOPD) by residual enzyme activity (typically 3–30% of normal, vs. <3% in IOPD) and by later, more slowly progressive presentation. Convention defines LOPD as onset after 12 months of age, or onset under 12 months **without cardiomyopathy** ([PMC10526932](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10526932/); [MDPI 13:1279](https://www.mdpi.com/2218-273X/13/9/1279)). Clinically it presents as a progressive limb-girdle and axial myopathy with respiratory muscle involvement, often mimicking other neuromuscular disorders, which historically delayed diagnosis by years ([NeurologyLive](https://www.neurologylive.com/view/evolution-pompe-disease-fatal-infantile-disorder-treatable-myopathy)).

**Key identifiers:**
- OMIM: Pompe disease (GSD II) #232300; Late-onset Pompe disease specifically has its own OMIM phenotype entry, **#621314 "POMPE DISEASE, LATE-ONSET; LOPD"** ([OMIM:621314](https://www.omim.org/entry/621314))
- Gene: GAA, OMIM *606800, chromosome 17q25.3
- Orphanet: ORPHA:365667 (Late-onset Pompe disease), part of ORPHA:365 (Glycogen storage disease due to acid maltase deficiency)
- Synonyms: Acid maltase deficiency (AMD), glycogenosis type II, GSD II, adult/childhood/juvenile-onset acid maltase deficiency, alpha-1,4-glucosidase deficiency
- Evidence base is largely aggregated (registries — the Pompe Registry, French National Pompe Registry, ADVANCE study cohort) supplemented by individual case reports/series and single-center retrospective cohorts (e.g., 68-patient single-center Chinese cohort, [Frontiers 2026](https://www.frontiersin.org/journals/nutrition/articles/10.3389/fnut.2026.1797345/full)).

## 2. Etiology

**Causal factor:** LOPD is monogenic and autosomal recessive, caused by biallelic pathogenic variants in *GAA*. Over 400–800+ pathogenic/likely pathogenic variants have been catalogued; a large international retrospective study of >30,000 samples from 57 countries identified 723 confirmed cases with 283 distinct GAA alterations, 98 of them novel ([PMC10526932](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10526932/)).

**Genetic risk factors:**
- The dominant LOPD-associated allele is the intronic splice variant **c.-32-13T>G**, located 13 nucleotides upstream of the intron 1 acceptor site of GAA. It is a "leaky" splice mutation — it permits a reduced amount of correctly spliced (normal) mRNA alongside aberrantly spliced transcripts lacking exon 2, yielding residual enzyme activity sufficient to avoid the infantile phenotype. It is present on at least one allele in ~90% of LOPD patients and accounts for roughly two-thirds of LOPD alleles overall ([PubMed:36401034](https://pubmed.ncbi.nlm.nih.gov/36401034/); [ATM Peruzzo](https://atm.amegroups.org/article/view/25187/html)).
- Population-specific alleles: **c.2560C>T (p.Arg854Ter)** is the most common pathogenic variant in individuals of African/African-American ancestry, with a documented founder effect traced to North/Central Africa via the transatlantic slave trade (MAF ≈0.0019 in African/African-American gnomAD subpopulation) ([Rare Disease Advisor](https://www.rarediseaseadvisor.com/disease-info-pages/pompe-disease-etiology/)).
- Genotype-phenotype correlation: clinical severity correlates broadly with residual GAA activity — <3% normal activity → classic infantile phenotype; 3–30% → late-onset phenotype ([PMC7467391](https://pmc.ncbi.nlm.nih.gov/articles/PMC7467391/); [PMC8228169](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8228169/)).
- Pseudodeficiency alleles (e.g., common in Asian populations) reduce measured GAA enzymatic activity on screening assays without causing disease, complicating newborn screening and dried-blood-spot (DBS) interpretation and requiring confirmatory genetic testing ([Neurology Genetics](https://www.neurology.org/doi/10.1212/NXG.0000000000000623)).

**Environmental/other risk factors:** No environmental, infectious, or lifestyle causal factors are established; LOPD is purely a monogenic disorder. Age and cumulative disease duration are the principal modifiers of severity/functional decline rather than external exposures.

**Protective factors:** No specific protective genetic or environmental factors have been robustly established; higher residual enzyme activity (a function of genotype) is the primary attenuating factor.

## 3. Phenotypes

The hallmark phenotype is a **slowly progressive limb-girdle and axial myopathy with disproportionate respiratory muscle weakness** ([PMC6642938](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6642938/)).

| Phenotype | Frequency/Notes | Suggested HPO term |
|---|---|---|
| Proximal/limb-girdle muscle weakness | Core, near-universal finding; pelvic girdle > shoulder girdle | HP:0003325 (Limb-girdle muscle weakness) |
| Axial (paraspinal/abdominal) weakness → lumbar hyperlordosis, rigid spine | Common, often early | HP:0003713 (Axial muscle weakness); HP:0002943 (Lumbar hyperlordosis) |
| Exercise intolerance / exertional dyspnea | Common presenting symptom | HP:0003546 (Exercise intolerance) |
| Respiratory muscle weakness / diaphragmatic weakness → chronic respiratory insufficiency | Major driver of morbidity/mortality; occurs disproportionately relative to limb weakness in a subset | HP:0002093 (Respiratory insufficiency); HP:0009027 (Diaphragmatic weakness) |
| Scapular winging | ~1/3 of patients | HP:0003691 (Scapular winging) |
| Ptosis (often asymmetric/unilateral) | ~1/4 of patients | HP:0000508 (Ptosis) |
| Bulbar weakness — dysphagia, dysarthria, tongue weakness | Present in a minority, tongue weakness may be early | HP:0002015 (Dysphagia); HP:0001260 (Dysarthria) |
| HyperCKemia | Very common lab finding | HP:0003236 (Elevated CK) |
| Wheelchair dependence | ~50% by long-term follow-up (mean 16 years) | HP:0002996 (Wheelchair dependence, if modeled) |
| Ventilator dependence | ~19% at long-term follow-up | HP:0040270 (or descriptive) |
| Cerebral/intracranial arteriopathy (dolichoectasia, aneurysm, stenosis) | ~77% (23/30) had abnormal MRA/CTA in one Chinese cohort; 7/30 had stroke/hemorrhage | HP:0002617 (Aneurysm); vascular dolichoectasia terms |
| Cardiac conduction abnormalities (WPW, short PR) | Present in both IOPD and LOPD, more common in IOPD but reported in LOPD | HP:0001680 (WPW pattern) |
| Left ventricular hypertrophy | Uncommon/mild in LOPD (~11.5% in one series), unlike IOPD | HP:0001712 (LVH) |

Sources: [PMC6642938](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6642938/), [ATM 27142](https://atm.amegroups.org/article/view/27142/html), [PMC5085764](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5085764/), [Orphanet J Rare Dis 2024 intracranial vasculopathy](https://link.springer.com/article/10.1186/s13023-024-03282-y).

**Onset/progression:** Onset ranges from early childhood through late adulthood; median age at diagnosis in one large cohort was 38 years. Progression is typically slow, starting with trunk/lower-limb weakness and progressing to respiratory decline; course is progressive rather than episodic, though rate is variable across patients ([PMC3135500](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3135500/)).

**Quality of life:** LOPD substantially impairs mobility, occupational function, and psychosocial well-being; qualitative interviews and EQ-5D-based utility studies (UK) document meaningful QoL decrements tied to mobility loss and respiratory support dependence ([PMC9985911](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9985911/)).

## 4. Genetic/Molecular Information

- **Causal gene:** GAA (HGNC:4065; OMIM *606800), chromosome 17q25.3; encodes a 110-kDa precursor polypeptide undergoing extensive ER/Golgi post-translational proteolytic processing to mature lysosomal forms (76 and 70 kDa) ([PMC10526932](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10526932/)).
- **Variant classification:** ClinGen's Lysosomal Diseases Variant Curation Expert Panel has published ACMG/AMP specifications for GAA variant classification ([PMC10872922](https://pmc.ncbi.nlm.nih.gov/articles/PMC10872922/)).
- **Predominant LOPD allele:** c.-32-13T>G (IVS1, leaky splice site variant), typically compound heterozygous with a second, more severe (often null/frameshift/nonsense) allele.
- **Variant types:** missense, nonsense (e.g., c.2560C>T/p.Arg854Ter), frameshift, splice-site (c.-32-13T>G being the classic example), and structural variants.
- **Allele frequency:** Population carrier frequency data derived from gnomAD/general population databases have been used to estimate genetic prevalence, generally exceeding clinically ascertained prevalence, implying underdiagnosis ([ScienceDirect S2214426921000288](https://www.sciencedirect.com/science/article/pii/S2214426921000288)).
- **Somatic vs. germline:** Exclusively germline (autosomal recessive Mendelian disease); no somatic mosaicism disease mechanism reported.
- **Functional consequence:** Loss-of-function (partial) — reduced but non-zero residual GAA enzymatic activity in LOPD, contrasted with near-complete loss in IOPD.
- **Modifier genes:** No robust modifier genes are established, though variability in phenotype among patients with identical genotypes (including twins) suggests undefined modifiers/epigenetic or stochastic factors.
- **Epigenetics:** Not a primary described disease mechanism in LOPD; no major DiseaseMeth/ENCODE-cataloged epigenetic driver identified in the literature reviewed.
- **Chromosomal abnormalities:** Not applicable — LOPD is not associated with aneuploidy or large chromosomal rearrangements; it is a single-gene point-mutation/small-indel disorder.

## 5. Environmental Information

LOPD has no established environmental, infectious, or toxin-related causal or risk factors — it is a purely genetic (Mendelian) disease. Environmental interaction is largely limited to disease-modifying activity: physical exertion can unmask/exacerbate exercise intolerance, and intercurrent respiratory infections can precipitate acute decompensation given underlying respiratory muscle weakness, but neither modifies underlying genetic risk (Gene-environment interaction: not established in the literature searched).

## 6. Mechanism / Pathophysiology

**Ordered causal chain:**

1. Biallelic pathogenic *GAA* variants (e.g., c.-32-13T>G + a severe null allele) → leads to reduced synthesis/processing of functional lysosomal acid α-glucosidase enzyme, yielding **residual activity of ~3–30% of normal** (as opposed to <3% in IOPD).
2. Reduced GAA activity → results in **impaired lysosomal hydrolysis of glycogen**, causing progressive **lysosomal glycogen accumulation** predominantly in skeletal (and to a lesser extent cardiac and smooth) muscle ([PMC10419125](https://pmc.ncbi.nlm.nih.gov/articles/PMC10419125/)).
3. Glycogen-laden, enlarged lysosomes → leads to **lysosomal membrane rupture/leakage** and mechanical/structural disruption of myofibrillar architecture, contributing directly to muscle fiber damage.
4. Concurrently, lysosomal acidification defects and dysregulated **AMPK–TSC2 signaling** suppress mTORC1 activity at the lysosome (mTORC1 is normally lysosome-recruited and activated by Rheb-GTP) → results in **failure to inhibit autophagy initiation** (loss of mTORC1-mediated ULK1/TFEB suppression) while simultaneously **impairing autophagosome–lysosome fusion** ("autophagic block") → leads to massive **accumulation of autophagic debris (autophagic buildup)**, which independently displaces contractile elements and worsens fiber damage. This is inferred largely from mouse/cell models but corroborated by human muscle biopsy pathology ([EMBO Mol Med](https://www.embopress.org/doi/full/10.15252/emmm.201606547); [PMC11118179](https://pmc.ncbi.nlm.nih.gov/articles/PMC11118179/)).
5. In parallel, disrupted lysosomal glucose/glycogen handling triggers **cytoplasmic (extralysosomal) glycogen metabolism dysregulation** — upregulation of glycogenin (GYG1), glycogen synthase (GYS1), GLUT4, GBE1, and UGP2 — leading to additional **cytoplasmic glycogen accumulation** that further disrupts myofibrillar structural organization (demonstrated in Pompe mouse muscle and human LOPD biopsies) ([PMC10092494](https://pmc.ncbi.nlm.nih.gov/articles/PMC10092494/)).
6. Chronic ER stress and unfolded protein response activation from proteostasis dysregulation → contributes to ongoing **muscle proteostasis failure**, active membrane remodeling, and p62/SQSTM1 accumulation, indicating imbalance in autophagic clearance (predominantly in mid-to-late disease stages, while glycogenin elevation is an earlier marker) ([PMC10419125](https://pmc.ncbi.nlm.nih.gov/articles/PMC10419125/)).
7. Cumulative myofiber structural disruption, autophagic buildup, and secondary inflammation → leads to **progressive muscle fiber atrophy/necrosis and replacement fibrosis**, clinically manifesting as **limb-girdle and axial muscle weakness**.
8. Independently, glycogen accumulation in **diaphragmatic and other respiratory muscle fibers, and in motor neurons/phrenic nerve pathways**, contributes to **progressive respiratory insufficiency**, a partly independent (branching) pathway from limb weakness, with etiology described as multifactorial (muscle + possible motor neuron pathology) ([PMC5085764](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5085764/)).
9. Separately, glycogen accumulation in **vascular smooth muscle cells** of cerebral arteries, arterioles, and capillaries (demonstrated at autopsy) → leads to progressive **arterial wall remodeling and dilative arteriopathy** (dolichoectasia, fusiform dilation, aneurysm formation) → can result in **cerebral infarction or hemorrhage** in a subset of LOPD patients, and separately **thoracic aortic dilation**, representing a distinct vascular branch of the pathophysiology largely independent of skeletal myopathy severity ([Orphanet J Rare Dis 2024](https://link.springer.com/article/10.1186/s13023-024-03282-y); [J Neurol 2010](https://link.springer.com/article/10.1007/s00415-010-5618-0)).

**Molecular pathways:** mTORC1/AMPK/TSC2 nutrient-sensing signaling axis (dysregulated); autophagy-lysosome pathway (ULK1, TFEB/TFE3); UPR/ER stress pathway.

**Cellular processes:** autophagy (defective flux/fusion), lysosomal dysfunction, cytoplasmic glycogen metabolism dysregulation, myofiber atrophy, chronic low-grade inflammation.

**Suggested GO terms:** GO:0005980 (glycogen catabolic process), GO:0006914 (autophagy), GO:0016236 (macroautophagy), GO:0007041 (lysosomal transport), GO:0034976 (response to endoplasmic reticulum stress), GO:0004339 (glycogen debranching enzyme activity — comparator pathway), GO:0004558 (alpha-1,4-glucosidase activity).

**Suggested CL terms:** CL:0000188 (skeletal muscle cell/myofiber), CL:0000746 (cardiac muscle cell), CL:0000192 (smooth muscle cell — vascular), CL:0000540 (neuron — motor neuron/phrenic pathway involvement).

**Molecular profiling:** A muscle proteomic study comparing pre- and post-ERT tissue in LOPD patients found treatment-associated shifts in proteins related to glycolysis, oxidative stress, and cytoskeletal organization ([PMC8001152](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8001152/)). iPSC-derived skeletal muscle models have been used to model infantile-onset disease and study proteostasis ([PMC5647434](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5647434/)).

## 7. Anatomical Structures Affected

- **Primary organs:** skeletal muscle (proximal limb-girdle, axial/paraspinal, diaphragm/respiratory muscles), with cardiac muscle involvement typically mild/absent in LOPD (contrasting sharply with IOPD's severe hypertrophic cardiomyopathy).
- **Secondary/complication-level involvement:** cerebral and thoracic aortic vasculature (dilative arteriopathy, aneurysm, stroke); peripheral/central motor neuron pathways potentially contributing to respiratory muscle dysfunction.
- **Body systems:** musculoskeletal, respiratory, cardiovascular (conduction system and vasculature), and to a lesser degree nervous system (motor pathways, cerebrovascular).
- **Tissue/cell level:** skeletal myofibers (type I/II), diaphragmatic muscle fibers, vascular smooth muscle cells of cerebral/aortic arteries, cardiac conduction tissue (accessory pathways implicated in WPW).
- **Subcellular level:** lysosomes (primary site of glycogen accumulation and dysfunction; GO Cellular Component GO:0005764), autophagosomes, sarcoplasm/myofibrillar apparatus, endoplasmic reticulum (UPR activation).
- **Anatomical terms (UBERON):** UBERON:0001134 (skeletal muscle tissue), UBERON:0001086 (diaphragm), UBERON:0000948 (heart), UBERON:0001981 (blood vessel — cerebral/aortic).
- **Laterality:** Predominantly bilateral/symmetric muscle weakness, though ptosis is frequently asymmetric/unilateral.

## 8. Temporal Development

- **Onset:** LOPD spans onset from early childhood through late adulthood by definition (after 12 months of age, or infantile-onset without cardiomyopathy); onset pattern is typically insidious/subacute rather than acute.
- **Progression:** Chronic, generally slowly progressive; longitudinal follow-up (mean 16 years) in Dutch cohorts showed pulmonary function decline of ~1.6%/year and gradual proximal weakness progression ([PubMed:15659425](https://pubmed.ncbi.nlm.nih.gov/15659425/); referenced in [PMC3135500](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3135500/)).
- **Course pattern:** Progressive (not relapsing-remitting or episodic); rate is variable between individuals even with similar genotypes.
- **Disease duration:** Chronic, lifelong.
- **Remission:** No spontaneous remission; enzyme replacement therapy (ERT) can stabilize or slow — but generally not reverse — established damage; presymptomatic treatment (newborn-screening-identified) is being explored as a critical window to prevent irreversible myopathy ([ScienceDirect S0035378725006083](https://www.sciencedirect.com/science/article/pii/S0035378725006083)).
- **Critical period:** Early (presymptomatic) initiation of ERT — enabled by newborn screening — is increasingly recognized as a critical intervention window before irreversible muscle damage accrues.

## 9. Inheritance and Population

**Epidemiology:**
- Global birth prevalence of Pompe disease overall: ~2.0 per 100,000 live births (95% CI 1.5–2.4); infantile-onset ~1.0/100,000; **late-onset ~2.4/100,000 (95% CI 1.8–3.0)** ([PMC12057045](https://pmc.ncbi.nlm.nih.gov/articles/PMC12057045/)).
- Newborn screening birth-prevalence estimates for LOPD vary geographically: 1 in 82,914 in Taiwan vs. 1 in 17,133 in Pennsylvania, reflecting both true population variation and pseudodeficiency-allele confounding ([PMC7712483](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7712483/); [Neurology Genetics](https://www.neurology.org/doi/10.1212/NXG.0000000000000623)).
- French National Pompe Registry: diagnosis rate rose from 2.6/year (pre-2001) to 12.8/year (2011–2015), reflecting improved diagnostic awareness/DBS testing rather than true incidence change.

**Inheritance pattern:** Autosomal recessive.
**Penetrance:** Complete for biallelic pathogenic (non-pseudodeficiency) genotypes, though expressivity (age of onset, rate of progression) is highly variable.
**Expressivity:** Markedly variable, even among patients sharing the c.-32-13T>G/severe-allele genotype.
**Genetic anticipation:** Not described as a feature of LOPD (no repeat-expansion mechanism).
**Founder effects:** c.2560C>T (p.Arg854Ter) — African/African-American founder allele traced to North/Central Africa; other population-specific founder variants reported in isolated populations (e.g., French Guiana Maroon population for infantile disease, [PubMed:29637184](https://pubmed.ncbi.nlm.nih.gov/29637184/)).
**Carrier frequency:** Estimated from population genomic databases (gnomAD-based); genetic-prevalence modeling suggests carrier frequency and "genetic prevalence" figures often exceed clinically ascertained prevalence, implying underdiagnosis ([ScienceDirect S2214426921000288](https://www.sciencedirect.com/science/article/pii/S2214426921000288)).
**Population demographics:** Higher LOPD prevalence reported in populations of African descent; higher frequency of pseudodeficiency alleles in Asian populations affecting screening specificity. No strong sex-ratio skew is characteristically reported for LOPD (autosomal disease).

## 10. Diagnostics

- **First-line test:** GAA enzyme activity assay on **dried blood spot (DBS)**, using lysosomal enzyme testing at pH 3.8 with/without specific inhibition ([Nature EJHG](https://www.nature.com/articles/s41431-020-00752-2)). Sensitivity limitations exist: in one cohort, reduced DBS activity was found in 7.6% of patients with elevated CK/limb-girdle weakness, but LOPD was molecularly confirmed in only 2.4%, indicating DBS alone can be inconclusive ([PubMed:29742245](https://pubmed.ncbi.nlm.nih.gov/29742245/)).
- **Confirmatory testing:** Molecular/genetic sequencing of all *GAA* coding exons and flanking intronic regions (to detect c.-32-13T>G and other variants) is required to confirm diagnosis and exclude pseudodeficiency.
- **Biomarkers:** Urinary/plasma glucose tetrasaccharide (Hex4/Glc4) and creatine kinase (CK) are used as disease-activity/treatment-response biomarkers (elevated pre-treatment, decline with effective ERT) ([PMC10834735](https://pmc.ncbi.nlm.nih.gov/articles/PMC10834735/)).
- **Electromyography:** Myopathic changes with characteristic (though not universal) fibrillations/myotonic-like discharges especially in paraspinal muscles.
- **Muscle biopsy/histopathology:** Vacuolar myopathy with PAS-positive glycogen accumulation, though biopsy can be falsely normal in some LOPD patients given patchy involvement — a key diagnostic pitfall.
- **Pulmonary function testing:** Upright and supine forced vital capacity (FVC) — a critical functional biomarker for respiratory muscle involvement and treatment response, used as a primary endpoint in ERT trials.
- **Genetic testing overview:** Single-gene *GAA* sequencing plus deletion/duplication analysis is generally sufficient (only one causal gene); broader neuromuscular gene panels or WES are used when GAA testing is negative but suspicion remains, and have identified previously unexplained LOPD cases among cohorts referred for "unexplained limb-girdle weakness" (e.g., 606-patient WES cohort, [Orphanet J Rare Dis](https://ojrd.biomedcentral.com/articles/10.1186/s13023-017-0722-1); global NGS cohort, [PMC11638199](https://pmc.ncbi.nlm.nih.gov/articles/PMC11638199/)).
- **Differential diagnosis:** limb-girdle muscular dystrophies, Becker muscular dystrophy, facioscapulohumeral muscular dystrophy, scapuloperoneal syndromes, rigid spine syndrome, myasthenia gravis, spinal muscular atrophy, polymyositis, other glycogen storage diseases (III, IV, V, VII), Danon disease, mitochondrial myopathies ([PMC7467391](https://pmc.ncbi.nlm.nih.gov/articles/PMC7467391/)).
- **Screening:** Newborn screening for Pompe disease (via DBS GAA activity, now implemented in many US states — Pennsylvania, Illinois, California, and internationally including Taiwan) identifies both IOPD and (presymptomatically) LOPD cases, raising management questions about when to initiate treatment in asymptomatic screen-positive infants/children ([PMC7422979](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7422979/); [PMC7422983](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7422983/)).
- **Imaging:** Muscle MRI shows characteristic patterns of fatty infiltration/edema in paraspinal, gluteal, and thigh musculature, useful for diagnosis and monitoring, though not detailed further in the sources reviewed here.

## 11. Outcome/Prognosis

- **Survival (natural history, pre-ERT):** In a cohort of 268 untreated adults, median survival after diagnosis was 27 years, with median age at diagnosis 38 years. Median age at death was ~56 years, with **respiratory failure accounting for >70% of deaths** ([PMC3135500](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3135500/)).
- **Functional decline:** In a 16-year longitudinal follow-up of 16 LOPD patients, 50% became wheelchair-bound and 19% became ventilator-dependent; pulmonary function (FVC) declined ~1.6%/year at the group level.
- **Prognostic stratification:** 5-year survival was 95% in patients without wheelchair/respiratory support at baseline vs. 74% in those who were wheelchair-bound and on respiratory support — mobility/respiratory status is a major prognostic factor.
- **Complications:** chronic respiratory insufficiency/failure (leading cause of death), cerebrovascular events (aneurysm rupture, stroke), scoliosis/rigid spine, dysphagia-related aspiration risk, and cardiac conduction abnormalities in a minority.
- **Quality of life:** Substantially reduced with disease progression, correlating strongly with mobility and respiratory-support dependence ([PMC9985911](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9985911/); [PMC4015278](https://pmc.ncbi.nlm.nih.gov/articles/PMC4015278/) discusses limitations of current LOPD outcome measures).

## 12. Treatment

**Pharmacotherapy — Enzyme Replacement Therapy (ERT), the mainstay of treatment:**

| Agent | Brand | Mechanism/notes | Suggested NCIT term |
|---|---|---|---|
| Alglucosidase alfa | Myozyme/Lumizyme | First-generation recombinant human GAA (rhGAA); FDA-approved 2006 | NCIT:C15986 (Pharmacotherapy) + therapeutic_agent |
| Avalglucosidase alfa | Nexviazyme/Nexviadyme (Sanofi) | Second-generation; engineered with enhanced bis-mannose-6-phosphate glycan content for improved cellular/M6P-receptor-mediated uptake; superior to alglucosidase alfa on upright FVC% and 6-minute walk test in the Phase 3 **COMET** trial (treatment-naïve LOPD adults, 49–97 weeks) ([PubMed:37036722](https://pubmed.ncbi.nlm.nih.gov/37036722/); [PMC10087094](https://pmc.ncbi.nlm.nih.gov/articles/PMC10087094/)) | NCIT:C15986 |
| Cipaglucosidase alfa + miglustat | Pombiliti + Opfolda (Amicus) | Cipaglucosidase alfa uses naturally enriched bis-phosphorylated high-mannose glycans for uptake; miglustat is a small-molecule stabilizer preventing enzyme degradation in circulation; approved combination regimen ([Frontiers 2024](https://www.frontiersin.org/journals/neurology/articles/10.3389/fneur.2024.1451512/full)) | NCIT:C15986 |

Real-world switch studies (alglucosidase alfa → avalglucosidase alfa) show statistically significant improvement in CK, Hex4, and AST biomarkers post-switch ([PMC10834735](https://pmc.ncbi.nlm.nih.gov/articles/PMC10834735/)). Network meta-analyses comparing avalglucosidase alfa vs. cipaglucosidase+miglustat (no head-to-head RCT exists) have been published to guide relative positioning ([Becaris CER-2024-0045](https://becarispublishing.com/doi/10.57264/cer-2024-0045)).

**Immunogenicity management:** ERT is limited by anti-drug antibody (ADA) development, more prominent and clinically consequential in CRIM-negative infantile patients but also observed in LOPD (antibody titers typically peak within first ~1000 days of ERT then decline with long-term exposure, generally without major efficacy loss). Immune tolerance induction (ITI) regimens — including bortezomib/rituximab/methotrexate/IVIG-based protocols — are used for patients with high-sustained anti-rhGAA titers ([Frontiers 2024](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2024.1360369/full); [PMC10526476](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10526476/)).

**Advanced/experimental therapeutics — Gene therapy:**
- **ACTUS-101 (AAV2/8-LSPhGAA)** (AskBio) — liver-directed gene therapy establishing a hepatic GAA-secretion depot to potentially replace chronic ERT; Phase 1/2 trial in LOPD showed all participants met ERT-withdrawal criteria at week 24 and remained off ERT through week 104 ([AskBio](https://www.askbio.com/first-patient-dosed-with-gene-therapy-in-phase-1-2-study-of-actus-101-in-patients-with-pompe-disease/); [PMC10494494](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10494494/)).
- **SPK-3006** (Roche/Spark, AAVRh74-based liver-directed GAA gene therapy, RESOLUTE trial NCT04093349) — program **discontinued** by Roche ([CGTlive](https://www.cgtlive.com/view/roche-drops-pompe-gene-therapy-program)).
- Muscle-directed AAV approaches (e.g., AAVMYO3-Gaa) remain preclinical, showing normalized glycogen pathology, restored strength/mass, and normalized survival in mouse models (2024 study) ([ScienceDirect S2212877824000309](https://www.sciencedirect.com/science/article/pii/S2212877824000309)).
- As of February 2025, approximately 41 active/recruiting Pompe disease clinical trials span ERT, gene therapy, and substrate-reduction approaches ([Rare Disease Advisor](https://www.rarediseaseadvisor.com/hcp-resource/pompe-disease-clinical-trials/)).

**RNA-based/experimental splice-correction therapy:**
- Antisense oligonucleotides (splice-modulating phosphorodiamidate morpholino oligomers) designed to enhance GAA exon 2 inclusion in patients heterozygous for c.-32-13T>G, restoring some acid α-glucosidase activity in patient-derived cells — an approach specific to the dominant LOPD splice variant ([PubMed:36401034](https://pubmed.ncbi.nlm.nih.gov/36401034/); [PMC7174337](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7174337/)).

**Supportive/rehabilitative care:** Non-invasive/invasive ventilatory support for respiratory insufficiency, physical/occupational therapy for mobility preservation, dietary/nutritional management, and mobility aids (wheelchairs) as disease progresses — NCIT:C15302 (Physical Therapy), NCIT:C15747 (Supportive Care).

**Treatment strategy:** Early diagnosis and presymptomatic/early initiation of ERT (facilitated by newborn screening) is emphasized as key to preserving muscle mass/function before irreversible fibrotic replacement occurs; case reports document improved muscle strength/respiratory function with early ERT initiation ([J Med Case Reports 2024](https://link.springer.com/article/10.1186/s13256-024-04837-0)).

## 13. Prevention

- **Primary prevention:** Not applicable in the traditional sense (monogenic recessive disease) — carrier screening and genetic counseling for at-risk families/populations (e.g., known founder-variant communities) is the main preventive lever, alongside prenatal/preimplantation genetic diagnosis for known-carrier couples.
- **Secondary prevention (screening/early detection):** **Newborn screening** for GAA activity via DBS is implemented in numerous jurisdictions (Pennsylvania, Illinois, California, Taiwan, and others), enabling presymptomatic identification of both IOPD and LOPD cases and earlier treatment initiation ([PMC7712483](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7712483/); [PMC7422988](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7422988/)). Five-year outcomes of NBS-identified Pennsylvania patients have been reported ([PMC11943203](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11943203/)).
- **Tertiary prevention:** Regular pulmonary function monitoring, cardiac/vascular surveillance (given cerebral/aortic arteriopathy risk), and proactive rehabilitative care to prevent/delay complications (contractures, aspiration, respiratory failure) in diagnosed patients.
- **Genetic counseling:** Recommended for families of affected individuals, particularly relevant given autosomal recessive inheritance and documented founder-effect populations.
- **Disparities:** Documented gaps exist in following up NBS-identified LOPD patients, particularly across sociodemographic groups, highlighting a public-health/pediatric-practice challenge in translating screening into timely care ([ScienceDirect S1096719223002639](https://www.sciencedirect.com/science/article/abs/pii/S1096719223002639)).

## 14. Other Species / Natural Disease

No naturally occurring veterinary/companion-animal Pompe disease (spontaneous GAA-deficiency) was identified in this search; available information concerns engineered laboratory models (see Section 15). No OMIA entries or veterinary case series for spontaneous canine/feline GSD II were surfaced by the queries run.

## 15. Model Organisms

| Model | Type | Notes |
|---|---|---|
| **Gaa knockout mouse** (B6;129-Gaatm1Rabn/J, Jackson Labs) | Genetic knockout | Full deletion of exon 6 (lacks human ortholog exon); classic Pompe mouse model widely used in preclinical ERT/gene therapy studies |
| **Gaa c.1826dupA transgenic mouse** | Patient-derived pathogenic variant knock-in, preserving endogenous Gaa gene structure | Orthologous to human IOPD variant; recapitulates cardiac, myopathic, and biochemical phenotypes longitudinally ([Dis Model Mech](https://journals.biologists.com/dmm/article/19/3/dmm052611/371074/Longitudinal-characterization-of-Gaac-1826dupA)) |
| **Gaa c.1935C>A (p.D645E) CRISPR knock-in mouse** | CRISPR-Cas9 HDR knock-in | Recapitulates multiple features of human infantile-onset Pompe disease ([PMC9751086](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9751086/); [Sci Rep](https://www.nature.com/articles/s41598-022-25914-8)) |
| **Novel early-onset mouse model with spinal cord/respiratory defects** | Genetic | Used to demonstrate rescue via secreted-GAA gene therapy ([eBioMedicine](https://www.thelancet.com/journals/ebiom/article/PIIS2352-3964(20)30428-X/fulltext)) |
| **Rat model (muscle-directed AAV studies)** | Genetic/induced | Used for infantile-onset Pompe muscle-directed AAV gene therapy testing ([ScienceDirect S2212877824000309](https://www.sciencedirect.com/science/article/pii/S2212877824000309)) |
| **Zebrafish, quail** | Genetic models (referenced) | Noted as additional animal models used in the field, though detail was not retrieved in this search |
| **Patient-derived iPSC skeletal muscle model** | Cellular/in vitro | Modeling infantile-onset Pompe disease with patient-specific iPS cells, capturing proteostasis and structural phenotypes ([PMC5647434](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5647434/)) |

**Model limitations:** Most published genetic mouse models best recapitulate the **infantile-onset** phenotype (severe/near-null activity); models specifically calibrated to reproduce the partial (leaky) residual-activity genotype characteristic of LOPD are less well represented in the literature surveyed, and cardiac hypertrophy (prominent in IOPD mouse models) is not a major LOPD feature, limiting direct translational relevance for the LOPD cardiac question. The exon-6-deletion knockout allele in the standard Jackson Labs model lacks a direct human orthologous mutation, which is a noted limitation for variant-specific modeling.

**Applications:** These models have been central to development and validation of ERT (alglucosidase/avalglucosidase alfa), muscle- and liver-directed AAV gene therapy (ACTUS-101 precursor studies, AAVMYO3-Gaa), and mechanistic studies of autophagy/mTORC1 dysregulation and cytoplasmic glycogen metabolism.

---

## Summary of Suggested Ontology Bindings for KB Curation

- **Gene:** hgnc:4065 (GAA)
- **Disease terms:** MONDO (LOPD-specific term, if available) with OMIM #621314 (specific), #232300 (parent GSD II); ORPHA:365667
- **Key HP terms:** HP:0003325 (Limb-girdle muscle weakness), HP:0003713 (Axial muscle weakness), HP:0002093 (Respiratory insufficiency), HP:0003691 (Scapular winging), HP:0000508 (Ptosis), HP:0002015 (Dysphagia), HP:0003236 (Elevated CK), HP:0002617 (Aneurysm)
- **Key GO terms:** GO:0005980 (glycogen catabolic process), GO:0006914 (autophagy), GO:0004558 (alpha-1,4-glucosidase activity)
- **Key CL terms:** CL:0000188 (skeletal muscle myofiber), CL:0000192 (vascular smooth muscle cell)
- **Key UBERON terms:** UBERON:0001134 (skeletal muscle tissue), UBERON:0001086 (diaphragm)
- **Treatment NCIT terms:** NCIT:C15986 (Pharmacotherapy) + therapeutic_agent bindings for alglucosidase alfa / avalglucosidase alfa / cipaglucosidase alfa; therapeutic_modality: PROTEIN_REPLACEMENT (ERT) or GENE_THERAPY (ACTUS-101/AAV programs)

---

### Sources
- [OMIM #621314 — Pompe Disease, Late-Onset](https://www.omim.org/entry/621314)
- [OMIM *606800 — GAA](https://www.omim.org/entry/606800)
- [A Comprehensive Update on Late-Onset Pompe Disease (PMC10526932)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10526932/) / [MDPI version](https://www.mdpi.com/2218-273X/13/9/1279)
- [Lysosomal glycogen accumulation in Pompe disease results in disturbed cytoplasmic glycogen metabolism (PMC10092494)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10092494/)
- [Clinical, pathological and genetic features of 68 patients with LOPD (Frontiers 2026)](https://www.frontiersin.org/journals/nutrition/articles/10.3389/fnut.2026.1797345/full)
- [Developing Therapeutic Splice-Correcting ASOs for Adult-Onset Pompe with c.-32-13T>G (PubMed:36401034)](https://pubmed.ncbi.nlm.nih.gov/36401034/)
- [Splice modulating ASOs restore GAA activity (PMC7174337)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7174337/)
- [Molecular genetics of Pompe disease overview (ATM/Peruzzo)](https://atm.amegroups.org/article/view/25187/html)
- [Pompe Disease Etiology — Rare Disease Advisor](https://www.rarediseaseadvisor.com/disease-info-pages/pompe-disease-etiology/)
- [Investigating Late-Onset Pompe Prevalence in Neuromuscular Practices (Neurology Genetics)](https://www.neurology.org/doi/10.1212/NXG.0000000000000623)
- [Global variations in diagnostic methods and epidemiological estimates in Pompe disease (PMC12057045)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12057045/)
- [Newborn Screening for Pompe Disease: Pennsylvania Experience (PMC7712483)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7712483/)
- [Five-Year Outcomes of NBS-Identified Pompe Patients, PA (PMC11943203)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11943203/)
- [Newborn Screening for Pompe Disease in Illinois (PMC7422983)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7422983/)
- [First Year Newborn Screening in California (PMC7422988)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7422988/)
- [Disparities in follow-up after NBS for Pompe disease (ScienceDirect)](https://www.sciencedirect.com/science/article/abs/pii/S1096719223002639)
- [Cipaglucosidase alfa plus miglustat mechanism-outcome linkage (Frontiers 2024)](https://www.frontiersin.org/journals/neurology/articles/10.3389/fneur.2024.1451512/full)
- [Real-world switch to avalglucosidase alfa (PMC10834735)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10834735/)
- [Avalglucosidase alfa PRO outcomes vs alglucosidase, COMET trial (ScienceDirect)](https://www.sciencedirect.com/science/article/pii/S1096719223007515)
- [Efficacy/Safety of Avalglucosidase Alfa, 97-week Phase 3 RCT (PubMed:37036722)](https://pubmed.ncbi.nlm.nih.gov/37036722/) / [PMC10087094](https://pmc.ncbi.nlm.nih.gov/articles/PMC10087094/)
- [Network meta-analysis, cipaglucosidase vs other ERTs (Becaris)](https://becarispublishing.com/doi/10.57264/cer-2024-0045)
- [Identification of GAA variants via WES in limb-girdle weakness cohort (PMC5693551)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5693551/) / [Orphanet J Rare Dis](https://ojrd.biomedcentral.com/articles/10.1186/s13023-017-0722-1)
- [LOPD limb-girdle presentation prevalence (PubMed:29742245)](https://pubmed.ncbi.nlm.nih.gov/29742245/)
- [Enzymatic diagnosis of Pompe disease, 28-year experience (Nature EJHG)](https://www.nature.com/articles/s41431-020-00752-2)
- [Presymptomatic LOPD: Optimizing timing of treatment (ScienceDirect)](https://www.sciencedirect.com/science/article/pii/S0035378725006083)
- [Newborn-screened presymptomatic LOPD infant case report (PMC7422979)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7422979/)
- [Early diagnosis/treatment case report, J Med Case Reports 2024](https://link.springer.com/article/10.1186/s13256-024-04837-0)
- [AAV9 gene therapy for IOPD, NEJM 2024](https://www.nejm.org/doi/full/10.1056/NEJMoa2407766)
- [Phase I liver depot gene therapy in LOPD, Molecular Therapy 2023](https://www.cell.com/molecular-therapy-family/molecular-therapy/fulltext/S1525-0016(23)00077-1)
- [Screening data for AAV8 Phase I gene therapy trial (PMC10494494)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10494494/)
- [ACTUS-101 first patient dosed (AskBio)](https://www.askbio.com/first-patient-dosed-with-gene-therapy-in-phase-1-2-study-of-actus-101-in-patients-with-pompe-disease/)
- [Roche drops SPK-3006 gene therapy program (CGTlive)](https://www.cgtlive.com/view/roche-drops-pompe-gene-therapy-program)
- [Muscle-directed AAV gene therapy in rat model (ScienceDirect 2024)](https://www.sciencedirect.com/science/article/pii/S2212877824000309)
- [Longitudinal Gaa c.1826dupA mouse model (Dis Model Mech)](https://journals.biologists.com/dmm/article/19/3/dmm052611/371074/Longitudinal-characterization-of-Gaac-1826dupA)
- [Gaa c.1935C>A CRISPR knock-in mouse model (PMC9751086)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9751086/) / [Sci Rep](https://www.nature.com/articles/s41598-022-25914-8)
- [Multisystem LOPD clinical update (PMC6642938)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6642938/) / [ATM](https://atm.amegroups.org/article/view/27142/html)
- [Respiratory muscle weakness management recommendations (PMC5085764)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5085764/)
- [Survival/prognostic factors, 268 untreated adults (PMC3135500)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3135500/)
- [Quality of Life in LOPD, UK utility study (PMC9985911)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9985911/)
- [Clinical relevance of LOPD outcome measures (PMC4015278)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4015278/)
- [Intracranial vasculopathy in young LOPD adults, Orphanet J Rare Dis 2024](https://link.springer.com/article/10.1186/s13023-024-03282-y) / [PMC11250947](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11250947/)
- [Dilated arteriopathy of thoracic aorta in LOPD (ScienceDirect)](https://www.sciencedirect.com/science/article/abs/pii/S1096719211001247)
- [Cerebral arterial abnormalities frequent in LOPD, J Neurol 2010](https://link.springer.com/article/10.1007/s00415-010-5618-0)
- [Genetic-radiological correlation, cerebral vascular anomalies, J Neurol 2017](https://link.springer.com/article/10.1007/s00415-017-8601-1)
- [From Acid Alpha-Glucosidase Deficiency to Autophagy (PMC10419125)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10419125/)
- [Modulation of mTOR signaling in Pompe disease (EMBO Mol Med)](https://www.embopress.org/doi/full/10.15252/emmm.201606547)
- [Failure of Autophagy in Pompe Disease (PMC11118179)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11118179/)
- [Cardiovascular abnormalities in LOPD and ERT response (ScienceDirect)](https://www.sciencedirect.com/science/article/pii/S1098360021045974)
- [Cardiovascular Pathologies in Non-Classic Pompe Disease (Rare Disease Advisor)](https://www.rarediseaseadvisor.com/insights/cardiovascular-pathologies-non-classic-pompe-disease/)
- [Detection of GAA variants via NGS in global limb-girdle cohort (PMC11638199)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11638199/)
- [GAA genotype-enzyme activity correlation, Hungarian cohort (PMC8228169)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8228169/)
- [Pompe disease pathogenesis, molecular genetics, diagnosis review (PMC7467391)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7467391/)
- [Carrier frequency and genetic prevalence modeling (ScienceDirect)](https://www.sciencedirect.com/science/article/pii/S2214426921000288)
- [Incidence of infantile Pompe in French Guiana Maroon population (PubMed:29637184)](https://pubmed.ncbi.nlm.nih.gov/29637184/)
- [ClinGen ACMG/AMP variant classification specifications for Pompe disease (PMC10872922)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10872922/)
- [Anti-rhGAA antibody management, bortezomib ITI (Frontiers 2024)](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2024.1360369/full)
- [Are anti-rhGAA antibodies a determinant of treatment outcome in LOPD? Systematic review (PMC10526476)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10526476/)
- [Long-term Myozyme exposure decreases anti-drug antibodies in LOPD (PMC5096052)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5096052/)
- [Muscle proteomic profile before/after ERT in LOPD (PMC8001152)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8001152/)
- [iPS cell skeletal muscle model of infantile Pompe disease (PMC5647434)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5647434/)
- [The Evolution of Pompe Disease — clinical review (NeurologyLive)](https://www.neurologylive.com/view/evolution-pompe-disease-fatal-infantile-disorder-treatable-myopathy)
- [Pompe Disease Clinical Trials landscape (Rare Disease Advisor)](https://www.rarediseaseadvisor.com/hcp-resource/pompe-disease-clinical-trials/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 47 |
| Resolved | 47 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 1 |
| Quoted claims with nothing to check against | 1 |
| References weighed for topical relevance | 47 |
| On topic | 38 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMC:PMC11638199` *(abstract only)*: "unexplained limb-girdle weakness"
  - Text part not found as substring: 'unexplained limb-girdle weakness' (note: only abstract available for PMID:39678382, full text may contain this excerpt)

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `DOI:10.1186/s13023-017-0722-1`: "unexplained limb-girdle weakness"
  - Reference resolved but exposes no abstract or full text to search

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 44 |
| Resolved | 34 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 9 |
| Terms whose name was checked | 30 |
| Terms named correctly | 18 |
| Terms named as a **different** term | 6 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002996` (1 mention) - the report calls it "Wheelchair dependence, if modeled"; HP calls it **Limited elbow movement**
- `HP:0001680` (1 mention) - the report calls it "WPW pattern"; HP calls it **Coarctation of aorta**
- `HP:0001712` (1 mention) - the report calls it "LVH"; HP calls it **Left ventricular hypertrophy**
- `GO:0004339` (1 mention) - the report calls it "glycogen debranching enzyme activity — comparator pathway"; GO calls it **glucan 1,4-alpha-glucosidase activity**
- `CL:0000540` (1 mention) - the report calls it "neuron — motor neuron/phrenic pathway involvement"; CL calls it **neuron**
- `UBERON:0001086` (2 mentions) - the report calls it "diaphragm"; UBERON calls it **obsolete articular cartilage**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `UBERON:0001086` (obsolete articular cartilage) (2 mentions)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0003713` (2 mentions) - the report calls it "Axial muscle weakness"; HP calls it **Muscle fiber necrosis**
- `HP:0003236` (2 mentions) - the report calls it "Elevated CK"; HP calls it **Elevated circulating creatine kinase activity**, and lists "Elevated serum CPK" among its other names
- `HP:0002617` (2 mentions) - the report calls it "Aneurysm"; HP calls it **Vascular dilatation**, and lists "Aneurysm" among its other names
- `CL:0000188` (2 mentions) - the report calls it "skeletal muscle cell/myofiber", "skeletal muscle myofiber"; CL calls it **cell of skeletal muscle**, and lists "skeletal muscle cell" among its other names
- `CL:0000192` (2 mentions) - the report calls it "smooth muscle cell — vascular", "vascular smooth muscle cell"; CL calls it **smooth muscle cell**
- `UBERON:0001981` (1 mention) - the report calls it "blood vessel — cerebral/aortic"; UBERON calls it **blood vessel**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000188` - called "skeletal muscle cell/myofiber", "skeletal muscle myofiber"
- `CL:0000192` - called "smooth muscle cell — vascular", "vascular smooth muscle cell"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `ORPHA`, `PubMed`.