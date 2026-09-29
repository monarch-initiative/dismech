---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-21T01:48:10.478183'
end_time: '2026-09-21T01:54:04.391386'
duration_seconds: 353.91
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Cocaine Intoxication
  mondo_id: MONDO:0019544
  category: Toxic Exposure Disorder
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
  web_search_requests: 25
  num_turns: 27
  total_cost_usd: 1.7004674
  session_id: dc83c613-1fba-53b8-9741-f63fb2448a6e
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 56
reference_validation:
  total_references: 40
  verified: 40
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 40
  on_topic: 13
  validator_version: 0.2.1
term_validation:
  total_terms: 85
  verified: 83
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 17
  labels_matching: 11
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: HP:0000734
    reported_labels:
    - Impulsivity
    ontology_label: Disinhibition
  - term_id: HP:0002140
    reported_labels:
    - Cerebral ischemia
    ontology_label: Ischemic stroke
  - term_id: HP:0001919
    reported_labels:
    - Acute kidney injury (secondary to rhabdomyolysis/vasoconstriction)
    ontology_label: Acute kidney injury
  - term_id: HP:0030828
    reported_labels:
    - Bronchospasm/wheezing ("crack lung")
    ontology_label: Wheezing
  labels_variant: 2
  obsolete_terms:
  - term_id: GO:0005329
    ontology_label: GO_0005329
    replaced_by: GO:0005330
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cocaine Intoxication
- **MONDO ID:** MONDO:0019544 (if available)
- **Category:** Toxic Exposure Disorder

## Research Objectives

Please provide a comprehensive research report on **Cocaine Intoxication** covering all of the
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

I'll now research cocaine intoxication comprehensively across the key domains — pathophysiology, genetics, phenotypes, diagnostics, treatment, and epidemiology.

# Cocaine Intoxication — Comprehensive Research Report

## 1. Disease Information

**Overview.** Cocaine intoxication is the acute, dose-dependent, transient clinical state produced by cocaine's pharmacological actions during or shortly after use — a sympathomimetic toxidrome combined with disturbances of mood, cognition, perception, and behavior, plus a spectrum of organ-specific toxicity (cardiovascular, cerebrovascular, neurologic, thermoregulatory, gastrointestinal, pulmonary, renal). It is distinct from, but closely tied to, cocaine use disorder (the chronic, compulsive-use condition) — intoxication is what happens pharmacologically to the intoxicated individual, while use disorder is the addictive syndrome.

**Key identifiers:**
- **MONDO:** MONDO:0019544 (cocaine intoxication)
- **ICD-10-CM:** F14.0/F14.1x2 (cocaine use with intoxication) and T40.5X- (poisoning by cocaine); ICD-11 equivalent under "Disorders due to use of cocaine" 6C24
- **ICD-9-CM:** 292.89
- **Orphanet:** ORPHA:90068 (listed for toxic-exposure disorder cross-reference in some aggregator resources, though cocaine intoxication is not a classic Orphanet rare disease and is better sourced from ICD/MeSH than Orphanet)
- **MeSH:** D019966 (Cocaine-Related Disorders), D000079843 relates to Cocaine
- **DSM-5:** Substance Intoxication — Stimulant Intoxication, cocaine type

**Common synonyms/alternative names:** cocaine toxicity, cocaine poisoning, crack intoxication, cocaine overdose, acute cocaine toxicity, sympathomimetic toxicity (cocaine-type), cocaine-associated agitated delirium (severe form).

**Source of information.** This entry synthesizes **aggregated disease-level knowledge**: toxicology/emergency-medicine reviews and guidelines (StatPearls, AHA scientific statements, JACC/Circulation reviews), pharmacology and neuroscience mechanistic literature, population-level surveillance data (CDC NCHS/NVSS, NSDUH), and case-series/case-report literature for organ-specific complications and animal-model work — not primary individual-patient EHR data. [Cocaine Toxicity - StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK430976/); [Management of Cocaine-Associated Chest Pain and MI (AHA)](https://www.ahajournals.org/doi/10.1161/circulationaha.107.188950); [The Cardiovascular Effects of Cocaine (JACC)](https://www.jacc.org/doi/10.1016/j.jacc.2017.05.014).

---

## 2. Etiology

### Disease Causal Factor
The single necessary and sufficient causal factor is **exposure to cocaine** (benzoylmethylecgonine), a tropane alkaloid derived from *Erythroxylum coca*, via any route (intranasal insufflation of powder cocaine hydrochloride, smoking of freebase "crack" cocaine, intravenous injection, oral ingestion, or mucosal/topical exposure). This is a **toxic exposure disorder**, not a genetic or infectious disease — there is no disease without the exposure. CHEBI term: **CHEBI:27958** (cocaine).

### Risk Factors

**Genetic risk factors (modify severity/susceptibility, not causation):**
- **BCHE (butyrylcholinesterase) variants** — BChE is the primary hydrolytic enzyme clearing cocaine to inactive ecgonine methyl ester; reduced enzymatic activity shunts more cocaine toward hepatic CYP3A4-mediated N-demethylation to the hepatotoxic metabolite norcocaine and prolongs/potentiates cocaine's toxic effects. The common **K-variant** (rs1803274) is associated with ~33% lower plasma BChE activity in homozygotes (~1/25 people) and heterozygotes (~1/4 people); a study of 1,436 individuals found rs1803274 differed significantly between crack-exclusive and powder-exclusive cocaine users (PMID:24312228). Severe congenital BChE deficiency (atypical/silent alleles) is a described risk factor for markedly prolonged, severe toxicity after cocaine exposure, modeled in Bche/Ces1 (carboxylesterase) double-knockout mice, which show prolonged toxic effects after cocaine challenge as a model for BChE-deficient humans. [Butyrylcholinesterase Genetic Variants (PLOS ONE, PMID:24312228)](https://pubmed.ncbi.nlm.nih.gov/24312228/); [BChE/Ces1 knockout mouse model](https://dmd.aspetjournals.org/article/S0090-9556(24)05821-5/abstract).
- **DRD2 splicing polymorphisms** — the intronic SNP **rs2283265** (altering D2-short/D2-long receptor splice-isoform ratio) confers an odds ratio of ~3 for cocaine overdose/death; this risk is markedly amplified through a **gene-gene interaction** with the dopamine transporter (SLC6A3/DAT) 3′-UTR VNTR variant rs3836790 — homozygosity for the DAT 6-repeat allele raises the OR to ~7.5 in DRD2 rs2283265 minor-allele carriers, illustrating a gene-gene-environment risk architecture for lethal cocaine toxicity (PMID:23340505, *Translational Psychiatry*). [Dopamine transporter DAT and receptor DRD2 variants affect risk of lethal cocaine abuse](https://pubmed.ncbi.nlm.nih.gov/23340505/).
- **HLA-B27** — carriage is a reported risk factor for developing agranulocytosis from levamisole-adulterated cocaine (an adulterant-mediated, not cocaine-intrinsic, immunogenetic risk factor — see §5).
- **CACNB2, GRIN2B, PLXDC2, PKNOX2** — implicated by a meta-analysis of 75 GWAS/2,910 candidate genes in substance-use-disorder/drug-use behavior broadly (not cocaine-specific), relevant to calcium-channel and NMDA-receptor (glutamatergic) signaling pathways engaged by cocaine.
- **CYP2A6, CYP2D6, ADH1B, ALDH2** — metabolic-gene variation affecting polysubstance toxicity/response, most directly relevant when cocaine is co-used with alcohol (cocaethylene formation, see §4) or nicotine.

**Environmental/behavioral risk factors:**
- Route of administration (smoking/crack and IV produce the most rapid, highest peak plasma concentrations and highest acute toxicity risk vs. intranasal); dose and purity; concurrent **alcohol co-use** (forms cocaethylene, a longer-half-life active metabolite with independent cardiotoxicity, and synergistically raises risk of sudden death); concurrent **opioid (especially fentanyl) co-use/contamination** — "fourth wave" polysubstance deaths, with the percentage of U.S. overdose deaths involving both fentanyl and stimulants rising from 0.6% (2010) to 32.3% (2021), and the inverse "cocaine-in-the-dope" adulteration pattern also increasingly recognized (PMID:38829035); ambient heat (hyperthermia risk); underlying cardiovascular disease (accelerates ischemia); pregnancy (fetal/placental exposure, see §5); and structural/demographic disparities — Black/African American persons in the U.S. experienced the steepest rise in cocaine-involved death rates 2018–2023 (9.1 → 24.3 per 100,000). [Fourth Wave polysubstance fentanyl deaths (Addiction, 2023)](https://onlinelibrary.wiley.com/doi/10.1111/add.16318); ["Coke in the Dope" — cocaine-adulterated fentanyl supply](https://pmc.ncbi.nlm.nih.gov/articles/PMC11446664/).

### Protective Factors
- No pharmacogenomic "protective allele" against acute cocaine toxicity is well established; higher constitutive BChE activity (non-K-variant homozygotes) is protective by accelerating clearance to inactive metabolites.
- Behaviorally: avoidance of concurrent alcohol/opioid use, harm-reduction practices (fentanyl test-strip checking of supply — shown effective at detecting fentanyl contamination before use), supervised-consumption settings, and naloxone co-carriage (protective against the opioid component of a mixed exposure, not against cocaine's own toxicity, since no opioid-receptor mechanism is involved). [Fentanyl Test Strip Use and Overdose Risk Reduction (JAMA Network Open)](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2833888).

### Gene-Environment Interactions
The clearest documented G×E is the **DRD2 rs2283265 × DAT1 rs3836790 × chronic heavy cocaine exposure** interaction driving risk of fatal cocaine toxicity (PMID:23340505) — genetic variation in dopaminergic signaling amplifies risk only in the presence of the environmental exposure (repeated/heavy cocaine use), a multiplicative rather than additive interaction. Similarly, **BCHE genotype × route of administration** interacts, since the K-variant's effect differed specifically between crack (smoked) and powder (intranasal) cocaine users in the case-control study above, suggesting metabolic genotype effects are exposure-route-dependent (peak plasma concentration/kinetics differ by route).

---

## 3. Phenotypes

Cocaine intoxication phenotypes span **behavioral/psychiatric**, **cardiovascular**, **neurologic**, **thermoregulatory/muscular**, **respiratory**, **gastrointestinal**, and **laboratory** domains. All are acute/subacute, dose- and route-dependent, and (for the toxidrome core) resolve as the drug is cleared — but several categories (myocardial infarction, stroke, rhabdomyolysis-associated AKI, bowel infarction) leave permanent sequelae or cause death.

### Behavioral/Psychiatric (core toxidrome)
| Phenotype | HPO suggestion | Notes |
|---|---|---|
| Euphoria / inappropriate elation | HP:0000734 (Impulsivity) / no exact HPO for euphoria; behavioral | Nearly universal at intoxicating doses |
| Psychomotor agitation | HP:0000725 (Psychomotor agitation, if not in HPO use HP:0100716 Self-injurious behavior adjacent) | Common, dose-related |
| Anxiety / paranoia | HP:0000739 (Anxiety) | Variable |
| Hypervigilance | — (behavioral, often free text) | Common |
| Psychosis (paranoid ideation, hallucinations, delusions) | HP:0000709 (Psychosis) | Reported in **29–53%** of people who use cocaine, per behavioral-health sources reviewed; mechanistically linked to dopamine sensitization in mesolimbic/mesocortical circuits |
| Delirium / confusion | HP:0031180 (Delirium) if available, else HP:0000726 (Delirium) | Severe "excited/agitated delirium" is a life-threatening variant |
| Impaired attention/cognition | HP:0000725/HP:0000737 (variable) | |

### Cardiovascular
| Phenotype | HPO | Notes |
|---|---|---|
| Tachycardia | HP:0001649 | Sympathomimetic; near-universal |
| Hypertension | HP:0000822 | Sympathomimetic |
| Chest pain / myocardial ischemia | HP:0100749 (Chest pain) | Coronary vasoconstriction + prothrombotic state + increased O2 demand; MI can occur even in angiographically normal coronaries |
| Cardiac arrhythmia (SVT, VT, VF, torsades, AV block, Brugada-pattern ECG) | HP:0011675 (Arrhythmia) | Na⁺-channel blockade (Class I antiarrhythmic-like effect) widens QRS; K⁺-channel (hERG) blockade prolongs QT |
| Cardiomyopathy (acute/chronic) | HP:0001638 | Catecholamine excess + oxidative/mitochondrial injury; apoptosis and contraction-band necrosis documented histologically |
| Aortic dissection | HP:0002647 | Rare but reported, hypertension-driven |

### Neurologic/Cerebrovascular
| Phenotype | HPO | Notes |
|---|---|---|
| Seizures | HP:0001250 | Glutamate/excitotoxicity-mediated, dose-related, can be first presentation |
| Ischemic stroke | HP:0002140 (Cerebral ischemia) | Vasospasm of large/microvascular cerebral arteries, endothelin-1-mediated |
| Intracerebral/subarachnoid hemorrhage | HP:0007183 / HP:0033040 | Hypertensive surges + vasculitis + weakened vessel walls; disproportionately affects young adults |
| Headache | HP:0002315 | Common, often vasospasm-related |

### Thermoregulatory/Musculoskeletal
| Phenotype | HPO | Notes |
|---|---|---|
| Hyperthermia | HP:0001945 | Impaired heat-dissipation (thermoregulatory adjustment failure) plus increased heat generation from agitation/muscle activity; potentiated by ambient heat |
| Rhabdomyolysis | HP:0003201 | Muscle ischemia from vasoconstriction, direct myotoxicity, catecholamine-driven hypermetabolism, sarcoplasmic Ca²⁺ dysregulation |
| Acute kidney injury (secondary to rhabdomyolysis/vasoconstriction) | HP:0001919 | Myoglobin-mediated tubular injury |

### Respiratory
| Phenotype | HPO | Notes |
|---|---|---|
| Bronchospasm/wheezing ("crack lung") | HP:0030828 | Smoked/inhaled route |
| Pneumothorax | HP:0002094-adjacent / HP:0025299 | Barotrauma from Valsalva-like inhalation technique |
| Acute lung injury / alveolar hemorrhage | HP:0002088-adjacent | |

### Gastrointestinal
| Phenotype | HPO | Notes |
|---|---|---|
| Mesenteric/bowel ischemia, perforation, ischemic colitis | HP:0002583-adjacent (Gastrointestinal hemorrhage) / free text | Norepinephrine-reuptake-blockade-driven splanchnic vasoconstriction; historically linked to oral ("body-packer/stuffer") ingestion |

### Laboratory abnormalities
Elevated creatine kinase (rhabdomyolysis), elevated troponin (myocardial injury), metabolic acidosis, hyperkalemia (rhabdomyolysis/AKI), leukocytosis, and (with levamisole-adulterated product) neutropenia/agranulocytosis and p-ANCA positivity.

**Characteristics.** Onset is acute (minutes, matching route-specific pharmacokinetics — fastest with smoked/IV, slower with intranasal/oral); severity is broadly dose-dependent but with substantial individual variability (genetic/metabolic factors above); course is typically self-limited over hours as cocaine and active metabolites (cocaethylene, norcocaine) are cleared, though organ injury (MI, stroke, rhabdomyolysis-AKI) can be permanent; frequency of specific phenotypes is highly variable across cohorts and not uniformly reported at the population level (chest pain and agitation are the most common ED-presenting complaints; psychosis in ~30–50% of users at some point; sudden cardiac death and stroke are rare but disproportionate causes of mortality in young cocaine users).

**Quality of life impact.** Acute intoxication episodes causing MI, stroke, or severe rhabdomyolysis/AKI carry lasting QoL impact (post-MI functional limitation, post-stroke disability, dialysis dependence in severe AKI); psychiatric sequelae (persistent psychosis, anxiety) can also impair daily functioning. Formal EQ-5D/SF-36 disease-specific data for cocaine intoxication specifically (as opposed to cocaine use disorder generally) are not well represented in the literature surveyed.

---

## 4. Genetic/Molecular Information

Cocaine intoxication is **not a Mendelian genetic disease** — there is no single causal gene. The genetic contribution operates entirely at the level of **modifier genes** affecting susceptibility/severity, and to a lesser extent genes contributing to the separate but related trait of cocaine dependence liability.

- **Causal "gene":** none (environmental/toxic exposure disorder). No OMIM phenotype entry exists for cocaine intoxication itself.
- **Modifier genes** (detailed in §2): **BCHE** (hgnc:983, butyrylcholinesterase — clearance/detoxification), **DRD2** (hgnc:3023, dopamine D2 receptor — splicing variant rs2283265 modulates lethality risk), **SLC6A3/DAT1** (hgnc:11049 — VNTR modulates lethality risk in combination with DRD2), **CYP3A4** (hgnc:2637 — hepatic bioactivation to hepatotoxic norcocaine, and drug-interaction risk with enzyme inducers such as phenytoin/carbamazepine), **CES1** (carboxylesterase-1, hgnc:1863 — parallel hydrolytic detoxification pathway to BChE).
- **Pathogenic variant classification:** Not applicable in the ACMG/AMP sense (this is not a rare Mendelian variant-caused disease); the relevant "variants" are common functional polymorphisms (BCHE K-variant, DRD2 rs2283265, DAT1 VNTR) assessed by population-genetics/pharmacogenomic association studies rather than clinical variant curation (ClinVar has essentially no direct entries framed around "cocaine intoxication" as a phenotype).
- **Allele frequency:** BCHE K-variant (rs1803274) — approximately 1 in 4 heterozygous, 1 in 25 homozygous in described populations (gnomAD-level population frequency data for rs1803274/rs4263329/rs4680662 would refine this further).
- **Somatic vs. germline:** All relevant variants are germline; no somatic component.
- **Functional consequence:** BCHE K-variant → partial loss of enzymatic (esterase) function (~33% reduced activity), shifting cocaine metabolism toward CYP3A4-mediated bioactivation; DRD2 rs2283265 → altered D2S/D2L splice-isoform ratio, altering postsynaptic dopaminergic signaling and mesolimbic circuit sensitivity.
- **Epigenetic information:** Chronic cocaine exposure (not acute intoxication per se) is associated with altered histone acetylation (e.g., H3/H4 acetylation at *fosB*, *bdnf* promoters) and DNA methylation changes in reward-circuit neurons in animal models — mechanistically relevant to the *use disorder* trajectory rather than to acute intoxication phenotype, but relevant background for a dismech pathophysiology narrative connecting acute exposure to chronic neuroadaptation (sensitization, see §6).
- **Chromosomal abnormalities:** None relevant; not a chromosomal disorder.

**GO/molecular-function terms for the drug's direct targets:**
- **GO:0005329** dopamine transmembrane transporter activity (SLC6A3/DAT — primary high-affinity binding target)
- **GO:0005335** serotonin:sodium symporter activity (SLC6A4/SERT)
- **GO:0005326** neurotransmitter transporter activity (SLC6A2/NET, norepinephrine)
- **GO:0005248** voltage-gated sodium channel activity (SCN5A cardiac isoform — local-anesthetic/Class-I-antiarrhythmic-like blockade)
- **GO:0005249** voltage-gated potassium channel activity (KCNH2/hERG — QT prolongation)
- **GO:0005245** voltage-gated calcium channel activity (L-type Ca²⁺ channels — vasospasm/arrhythmia)

---

## 5. Environmental Information

- **Primary environmental factor:** cocaine itself as an exogenous chemical exposure (CHEBI:27958), by any route.
- **Adulterants (major independent toxicological contributors):**
  - **Levamisole** — an anthelmintic banned in the U.S. since 2000, found in up to **69% of DEA-seized cocaine samples** (as of 2009 reporting) — causes a distinctive retiform/stellate purpuric cutaneous vasculitis with or without necrosis, agranulocytosis/severe neutropenia, arthralgias, and leukoencephalopathy, mediated at least partly through an HLA-B27-associated immune mechanism (p-ANCA-positive vasculitis reported). [Levamisole-Adulterated Cocaine: Vasculitis and Severe Neutropenia](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12851635/); [p-ANCA-Associated Vasculitis (PMID:23476825)](https://pubmed.ncbi.nlm.nih.gov/23476825/).
  - **Fentanyl and fentanyl analogs** — increasingly co-present in the cocaine supply ("cocaine-adulterated fentanyl" and the inverse, fentanyl-adulterated cocaine), driving the "fourth wave" of the U.S. overdose crisis; opioid receptor toxicity (respiratory depression) is mechanistically distinct from and additive to cocaine's sympathomimetic toxicity, and naloxone reverses only the opioid component (PMID:38829035).
  - **Xylazine** ("tranq") — an α2-agonist veterinary sedative increasingly found co-adulterating fentanyl/cocaine supplies, contributing sedation and severe skin ulceration, not reversed by naloxone.
- **Lifestyle/behavioral factors:** route of administration, dose, binge patterns, co-use of alcohol (cocaethylene formation) and tobacco/nicotine, ambient temperature during use (heat-related hyperthermia potentiation), and exertional/agitated state at time of use.
- **Infectious agents:** Not a direct causal factor for the intoxication itself, but injection-route cocaine use is an established risk factor for bloodborne infections (HIV, HCV, endocarditis) as a downstream consequence of the behavior, and smoked/crack use is associated with increased tuberculosis transmission risk in some population studies — these are comorbidity/complication considerations rather than intoxication mechanisms per se.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (numbered, from exposure to clinical manifestation)

1. **Cocaine crosses the blood-brain barrier and enters presynaptic monoaminergic nerve terminals**, where it binds with high affinity to the dopamine transporter (DAT/SLC6A3), serotonin transporter (SERT/SLC6A4), and norepinephrine transporter (NET/SLC6A2), acting as a competitive/allosteric transporter blocker ("physical plug") — this **directly causes** blockade of presynaptic monoamine reuptake (PMID:18568020 structural basis).
2. Reuptake blockade **leads to** supraphysiologic accumulation of dopamine, serotonin, and norepinephrine in the synaptic cleft, most consequentially in the mesolimbic dopaminergic reward circuit (ventral tegmental area → nucleus accumbens → prefrontal cortex) and in peripheral/central noradrenergic synapses.
3. Excess mesolimbic dopaminergic signaling **results in** the acute euphoric/reinforcing subjective effect and, at sufficient dose/frequency, drives downstream dopaminergic receptor sensitization (notably via DRD2 splice-isoform dynamics) that **underlies** the behavioral/psychiatric phenotype spectrum — agitation, hypervigilance, and at the extreme, paranoid psychosis (a documented dopamine-sensitization phenomenon, with 29–53% of users reporting psychotic symptoms).
4. Concurrently, excess **glutamate release** is triggered in cortical/hippocampal/striatal circuits (partly via cocaine's monoaminergic effects and partly through direct excitatory-amino-acid dysregulation), which **leads to** NMDA-receptor-mediated excitotoxicity — elevated intracellular Ca²⁺, mitochondrial dysfunction, and oxidative stress in vulnerable neurons — **manifesting clinically as** seizures and, in chronic/repeated intoxication, contributing to neurotoxic injury.
5. In the periphery, excess norepinephrine at postsynaptic α- and β-adrenergic receptors **causes** systemic vasoconstriction, tachycardia, and hypertension (the core sympathomimetic toxidrome), which **increases myocardial oxygen demand** (via increased inotropy/chronotropy) while **simultaneously decreasing myocardial oxygen supply** through coronary vasoconstriction — a supply-demand mismatch that **results in** myocardial ischemia/infarction, at times with normal or near-normal coronary arteries on angiography.
6. Coronary vasoconstriction is itself **mediated by** (a) increased endothelin-1 release, (b) impaired acetylcholine-induced vasorelaxation, (c) blockade of nitric-oxide-synthase-dependent vasodilation, and (d) direct potentiation of L-type calcium-channel-mediated vascular smooth-muscle contraction — together producing a **prothrombotic, vasospastic milieu** that is further amplified by cocaine-induced **platelet activation/aggregation** and **accelerated endothelial injury/atherosclerosis**, jointly **leading to** intracoronary thrombosis superimposed on vasospasm.
7. The same α-adrenergic-driven vasoconstriction, applied to **cerebral vasculature**, **causes** cerebral arterial and microvascular vasospasm (dopamine-mediated) and endothelin-1-dependent vasoconstriction, which **results in** ischemic stroke; the associated hypertensive surges and endothelial/vessel-wall injury (vasculitis, apoptosis of vascular smooth muscle) **independently increase the risk of** hemorrhagic stroke (intracerebral and subarachnoid), so the same upstream adrenergic surge **branches into two distinct downstream outcomes** — ischemic and hemorrhagic cerebrovascular injury — depending on vessel bed and pre-existing vascular integrity.
8. Applied to the **splanchnic circulation**, norepinephrine-reuptake-blockade-driven mesenteric vasoconstriction **causes** bowel wall ischemia, which — if sustained — **leads to** ischemic colitis, bowel infarction, and (in severe cases) perforation and peritonitis.
9. At the **cardiac myocyte membrane**, cocaine additionally acts as a **local-anesthetic-type sodium-channel blocker** (Class I antiarrhythmic-like effect on cardiac Naᵥ1.5/SCN5A), which **causes** delayed ventricular depolarization and QRS widening, and independently **blocks cardiac hERG/KCNH2 potassium channels**, which **causes** delayed repolarization and QT prolongation — together **resulting in** a spectrum of ventricular and supraventricular arrhythmias (including Brugada-pattern ECG changes, wide-complex tachycardia, and torsades de pointes), which can **culminate in** sudden cardiac death independent of the ischemic mechanism above.
10. Sustained catecholamine excess **disrupts intracellular calcium homeostasis** in the myocardium and **activates NAD(P)H oxidase and xanthine oxidase**, generating excess reactive oxygen/nitrogen species that **damage the mitochondrial electron transport chain**, **suppress ATP generation**, and **overwhelm antioxidant defenses** — this oxidative/mitochondrial injury **leads to** myocardial apoptosis and contraction-band necrosis, which over repeated intoxication episodes **results in** cocaine-associated cardiomyopathy (a chronic structural sequela of repeated acute mechanistic insults).
11. Centrally, cocaine's monoaminergic and glutamatergic effects, combined with **impairment of central thermoregulatory heat-dissipation mechanisms**, **cause** hyperthermia — which is **exacerbated by** concurrent psychomotor agitation/increased muscular activity and by high ambient temperature, and which, together with (a) intense adrenergic vasoconstriction producing muscle ischemia, (b) direct myotoxic effects of cocaine/metabolites, and (c) sarcoplasmic-reticulum calcium dysregulation increasing intracellular Ca²⁺ in myocytes, **converges on** rhabdomyolysis — myocyte breakdown releasing myoglobin and intracellular contents, which **leads to** acute kidney injury (myoglobin-mediated tubular injury) and hyperkalemia. Severe, sustained combination of agitation + hyperthermia + rhabdomyolysis constitutes the clinical entity of **cocaine-associated excited/agitated delirium**, considered by some authors a chronic-dopamine-dysregulation-driven late-stage manifestation of the same syndrome as rhabdomyolysis, rather than purely an acute dose effect (PMID:10414649).
12. Independent of the mechanisms above, adulterants co-administered with cocaine introduce **branch mechanisms not attributable to cocaine itself**: levamisole triggers an HLA-B27-associated autoimmune/toxic mechanism causing neutrophil destruction (agranulocytosis) and small-vessel vasculitis; co-administered fentanyl causes μ-opioid-receptor-mediated respiratory depression, additively increasing mortality risk through a mechanistically unrelated pathway.

### Molecular pathways
Monoamine-transporter blockade (dopaminergic/serotonergic/noradrenergic signaling), glutamatergic/NMDA-receptor excitotoxic signaling, adrenergic (α1/α2/β) receptor signaling cascades, endothelin-1 signaling, nitric oxide synthase pathway, L-type calcium channel signaling, NAD(P)H oxidase/xanthine oxidase oxidative pathways, mitochondrial apoptotic (caspase/Fas-dependent) pathway. Suggested GO biological process terms: **GO:0042416** (dopamine biosynthetic process — adjacent; more precisely **GO:0051583** dopaminergic synapse reuptake), **GO:0051610** (serotonin uptake), **GO:0051620** (norepinephrine uptake), **GO:0007204** (positive regulation of cytosolic calcium ion concentration), **GO:0006979** (response to oxidative stress), **GO:0006915** (apoptotic process), **GO:0001525** (angiogenesis — adjacent to endothelial injury discussions), **GO:0003081** (regulation of systemic arterial blood pressure by renin-angiotensin — adjacent), **GO:0055117** (regulation of cardiac muscle contraction), **GO:0045471** (response to ethanol — relevant to cocaethylene formation).

### Cellular processes
Apoptosis (myocardial, vascular smooth muscle), necrosis (contraction-band necrosis in myocardium), oxidative stress, platelet activation/aggregation, endothelial dysfunction, rhabdomyolysis (myocyte necrosis), neuronal excitotoxic cell injury.

### Cell types implicated (CL terms)
- **CL:0000746** cardiac muscle cell (myocyte) — ischemic/oxidative/apoptotic injury
- **CL:0000359** vascular associated smooth muscle cell — coronary/cerebral/mesenteric vasospasm
- **CL:0000115** endothelial cell — endothelial dysfunction/injury
- **CL:0000187** skeletal muscle cell — rhabdomyolysis
- **CL:0000540** neuron — dopaminergic (**CL:0000700** dopaminergic neuron), glutamatergic (**CL:0000679**), and noradrenergic (**CL:0011005**, if applicable) neuron subtypes engaged
- **CL:0000775** neutrophil — levamisole-adulterant-driven agranulocytosis
- **CL:0000767** basophil/mast cell — not primary
- **CL:0000097** mast cell (adjacent, bronchospasm discussions)

### Protein dysfunction
No misfolding/aggregation disease mechanism applies (this is a pharmacological receptor/transporter-blockade mechanism, not a proteinopathy). The relevant "dysfunction" is **pharmacological blockade of normally functioning transporter/channel proteins** (DAT, SERT, NET, SCN5A, KCNH2) rather than structural protein defect.

### Metabolic changes
Cocaine is metabolized primarily by hydrolysis (plasma pseudocholinesterase/BChE and hepatic/plasma carboxylesterase-1) to the major inactive metabolites **benzoylecgonine** and **ecgonine methyl ester**; a minor hepatic **CYP3A4**-mediated N-demethylation pathway produces **norcocaine**, which is hepatotoxic and can be increased by CYP3A4-inducing drugs (phenytoin, carbamazepine) or by esterase-inhibiting drugs (e.g., cholinesterase inhibitors such as donepezil) that shunt metabolism toward the oxidative pathway. In the presence of ethanol, hepatic carboxylesterases catalyze **transesterification** to form **cocaethylene**, an active, longer-half-life metabolite with its own independent cardiotoxicity, explaining the synergistic mortality risk of cocaine-alcohol co-use. [Cocaine: An Updated Overview on Chemistry, Detection, Biokinetics (PMC9032145)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9032145/); [Cocaethylene metabolism (PMID:12485948)](https://pubmed.ncbi.nlm.nih.gov/12485948/); [Metabolic Enzymes of Benzoylecgonine (PMID:27224254)](https://pubmed.ncbi.nlm.nih.gov/27224254/).

### Immune system involvement
Not a primary mechanism of cocaine's intrinsic toxicity, but adulterant-driven immune mechanisms are clinically important: levamisole-adulterated cocaine triggers an HLA-B27-associated agranulocytosis and a p-ANCA-positive small-vessel vasculitis with characteristic retiform purpura.

### Tissue damage mechanisms
Ischemia (coronary, cerebral, mesenteric, skeletal muscle — all vasoconstriction-mediated), oxidative stress, and necrosis/apoptosis (myocardial), consistent across organ systems as the shared downstream tissue-injury mechanism of the adrenergic/vasospastic cascade described above.

### Molecular/omics profiling
Rat cardiac studies show altered mitochondrial dynamics/biogenesis gene expression after short-term cocaine administration (PMID/DOI:10.1038/s41598-021-03631-y) and contraction-band necrosis with dephosphorylated connexin-43 after daily cocaine dosing (PMID:36233284). Human autopsy myocardial tissue from cocaine-related overdose deaths shows oxidative damage and both Fas-dependent (extrinsic) and mitochondria-dependent (intrinsic) apoptotic pathway activation (*Scientific Reports*, [srep44262](https://www.nature.com/articles/srep44262); PMID:25684178). No large-scale single-cell/spatial transcriptomic dataset specific to human cocaine-intoxication tissue was identified in this search; most molecular-profiling data derive from rodent cardiac/CNS tissue and human post-mortem myocardium.

---

## 7. Anatomical Structures Affected

**Organ level (primary):** Central and peripheral nervous system (brain), heart, systemic and cerebral vasculature, kidneys (secondary to rhabdomyolysis), skeletal muscle, gastrointestinal tract (mesenteric circulation), lungs (with smoked route), skin (with adulterant vasculitis).
**Secondary/complication organs:** Placenta and fetus (in pregnancy exposure), liver (norcocaine hepatotoxicity), bone marrow (levamisole-driven agranulocytosis).
**Body systems:** Cardiovascular, nervous (central and autonomic), respiratory, renal, musculoskeletal, gastrointestinal, immune/hematologic (adulterant-mediated), reproductive/obstetric.

**UBERON terms:**
- **UBERON:0000948** heart
- **UBERON:0001981** blood vessel (coronary: **UBERON:0001621**, cerebral: **UBERON:0002590**, mesenteric: **UBERON:0001240** superior mesenteric artery)
- **UBERON:0000955** brain (ventral tegmental area **UBERON:0002240**; nucleus accumbens **UBERON:0001882**; prefrontal cortex **UBERON:0000451**-adjacent)
- **UBERON:0002113** kidney
- **UBERON:0001134** skeletal muscle tissue
- **UBERON:0001555** digestive tract / **UBERON:0000160** intestine
- **UBERON:0002048** lung
- **UBERON:0001003** skin epidermis (adulterant vasculitis)
- **UBERON:0001987** placenta

**Tissue/cell level:** cardiac muscle tissue, vascular smooth muscle, vascular endothelium, dopaminergic/glutamatergic/noradrenergic neurons and their synaptic terminals, renal proximal tubule epithelium (myoglobin injury), mesenteric mucosal/muscularis layers.

**Subcellular (GO Cellular Component):** presynaptic plasma membrane / synapse (**GO:0045202**), mitochondrion (**GO:0005739** — central to the oxidative-stress mechanism), sarcoplasmic reticulum (**GO:0033017**, cardiac/skeletal muscle Ca²⁺ handling), voltage-gated sodium channel complex (**GO:0001518**).

**Localization/lateralization:** Not applicable in a lateralized sense (systemic/bilateral exposure); cerebrovascular events can be focal/unilateral depending on the vessel affected by vasospasm.

---

## 8. Temporal Development

**Onset.** Acute, occurring during or within minutes to a few hours of use; onset speed correlates with route: seconds-to-minutes for smoked (crack) or IV use (rapid CNS entry, high peak plasma concentration), minutes for intranasal, and somewhat delayed/prolonged for oral/gastrointestinal ingestion (including "body-packing/stuffing" scenarios, which carry a distinct risk of sudden massive release on packet rupture).

**Progression/stages.** No formal staging system exists analogous to cancer staging; clinically the presentation is often described along a **severity continuum**: mild (euphoria, mild tachycardia/hypertension) → moderate (agitation, significant hypertension/tachycardia, chest pain) → severe (seizures, malignant arrhythmia, myocardial infarction, stroke, hyperthermia/rhabdomyolysis, agitated delirium) → fatal (cardiac arrest, refractory hyperthermia with multiorgan failure). Rhabdomyolysis and excited delirium have been characterized as **different stages of the same syndrome** rather than independent complications (PMID:10414649).

**Rate/course.** Acute intoxication typically resolves within hours as cocaine (plasma half-life ~0.7–1.5 hours) and cocaethylene are cleared, though benzoylecgonine (a marker, not an active toxin) persists for days; however, organ injury sustained during the episode (MI, stroke, AKI) follows its own, generally much longer, disease course. Repeated intoxication episodes over months to years can cumulatively produce chronic cardiomyopathy and vascular disease, i.e., a chronic structural disease building on repeated acute pharmacological insults.

**Remission.** Spontaneous resolution of the acute toxidrome is the rule with abstinence and supportive/symptomatic treatment; "remission" of the underlying repeated-exposure behavior (cocaine use disorder) is a separate, much longer-term process addressed by substance-use treatment, outside the intoxication phenotype itself.

**Critical periods.** The first hours after use are the critical window for cardiovascular/cerebrovascular catastrophe and for effective benzodiazepine-based intervention; in pregnancy, the entire gestational period is a critical window for placental/fetal vasoconstrictive injury, with particular vulnerability during active organogenesis and in the third trimester for abruption/preterm labor risk.

---

## 9. Inheritance and Population

**Epidemiology (United States, most recent CDC/NSDUH data):**
- Cocaine-involved overdose deaths rose from **4,681 in 2011 to 29,449 in 2023**; the age-adjusted cocaine-involved death rate rose from **4.5 per 100,000 (2018) to 8.6 per 100,000 (2023)**.
- Racial disparity: non-Hispanic Black/African American cocaine-involved death rates rose from **9.1 to 24.3 per 100,000 (2018–2023)** — the largest increase of any group.
- Overall U.S. overdose deaths (all substances) **decreased** in 2024 and again in 2025 per NCHS, and cocaine/psychostimulant-involved deaths have also recently trended down, though 2023 MMWR data still show cocaine involved in **~28%** and psychostimulants in **~33%** of overdose deaths, with continuing increases in stimulant-involved deaths even as opioid-involved deaths fell (cocaine +1.7%, methamphetamine +2.4% even amid overall decline).
- Fentanyl co-involvement has risen sharply: fentanyl+stimulant co-involvement rose from 0.6% to 32.3% of all U.S. overdose deaths (2010–2021), reflecting the "fourth wave" polysubstance pattern.
- Past-year cocaine use prevalence (NSDUH, ages 12+): **1.8% (5.0 million people) in 2023**, declining to **1.5% (4.3 million people) in 2024**; among young adults (18–25), past-year use declined from 3.7% (2021) to 2.3% (2024).

**Inheritance pattern.** Not applicable — this is an acquired toxic-exposure condition, not an inherited disease. There is no Mendelian inheritance, penetrance, expressivity, anticipation, germline mosaicism, founder effect, consanguinity role, or carrier frequency in the classical genetic-disease sense. The genetic contributors described in §2/§4 (BCHE, DRD2, DAT1) are **common population polymorphisms modifying risk/severity**, analyzed via case-control/association-study designs rather than Mendelian segregation analysis.

**Population demographics.** Higher rates among adult men than women in most surveillance datasets (consistent with broader substance-use epidemiology, though the specific male:female ratio for intoxication events specifically was not isolated in the sources reviewed); geographic distribution in the U.S. has historically concentrated in the Northeast and parts of the South, though the drug-supply "fourth wave" has broadened geographic reach as fentanyl-stimulant combinations spread nationally; age distribution skews toward young to middle-aged adults (18–45), with the 18–25 age band showing the highest past-year use prevalence among adults per NSDUH.

---

## 10. Diagnostics

**Clinical/laboratory tests:**
- **Urine drug screen (immunoassay) for cocaine/benzoylecgonine** — LOINC **42241-0** (Cocaine+Benzoylecgonine [Presence] in Urine by Screen method) and LOINC **3394-4** (Benzoylecgonine, Urine, Quantitative). Screening (immunoassay) cutoff typically **150 ng/mL**; confirmatory (GC-MS/LC-MS) cutoff typically **100 ng/mL**. Detection window: **2–4 days** for occasional use, **10–14 days** for frequent/heavy use, since benzoylecgonine (the inactive, longer-half-life metabolite) rather than parent cocaine is the assay target.
- **Serum/plasma quantitative cocaine and metabolite panels** for acute clinical correlation (less commonly used clinically than urine screening).
- **Cardiac biomarkers:** troponin (myocardial injury), creatine kinase and CK-MB (rhabdomyolysis and myocardial injury, respectively), myoglobin (rhabdomyolysis).
- **Metabolic panel:** potassium (hyperkalemia from rhabdomyolysis/AKI), creatinine (AKI), bicarbonate/anion gap (metabolic acidosis), CK (rhabdomyolysis marker).
- **ECG** — essential: look for QRS widening (Na⁺-channel blockade), QT prolongation (K⁺-channel blockade), Brugada-pattern changes, ST-segment changes (ischemia/MI), arrhythmias.
- **Imaging:** CT/MR angiography or catheter angiography for suspected stroke, aortic dissection, or coronary ischemia work-up; CT of chest/abdomen for suspected pneumothorax, bowel ischemia/perforation.
- **Toxicology confirmation for adulterants:** clinical suspicion-driven testing (e.g., ANCA/p-ANCA and CBC with differential when levamisole-associated vasculitis/agranulocytosis is suspected); fentanyl immunoassay/confirmation in co-exposure scenarios.

**Genetic testing.** Not part of routine clinical diagnosis of cocaine intoxication (this is an acute toxicologic diagnosis, not a genetic one). BCHE genotyping (research/specialized settings) may be considered in cases of unexplained, markedly prolonged or severe toxicity suggestive of butyrylcholinesterase deficiency, analogous to its use in suxamethonium-apnea work-up.

**Clinical criteria.** DSM-5 Stimulant Intoxication criteria (cocaine type): recent use, plus clinically significant maladaptive behavioral or psychological changes (euphoria, affect blunting, changes in sociability, hypervigilance, interpersonal sensitivity, anxiety/tension/anger, stereotyped behaviors, impaired judgment) developing during or shortly after use, plus at least two physiological/physical signs (tachycardia/bradycardia, pupillary dilation, elevated/lowered blood pressure, perspiration/chills, nausea/vomiting, weight loss, psychomotor agitation/retardation, muscular weakness/respiratory depression/chest pain/cardiac arrhythmias, confusion/seizures/dyskinesias/dystonias/coma).

**Differential diagnosis.** Other sympathomimetic-toxidrome-producing agents (amphetamines/methamphetamine, synthetic cathinones/"bath salts," PCP, LSD-related agitation), serotonin syndrome, neuroleptic malignant syndrome (rhabdomyolysis/hyperthermia overlap — Daras et al. explicitly discuss cocaine-associated rhabdomyolysis/hyperthermia as a possible NMS variant), anticholinergic toxidrome, thyroid storm (clinical overlap explicitly documented, PMID/PMC4528882), alcohol withdrawal/delirium tremens, primary psychiatric psychosis, and primary cardiac events unrelated to drug use (must always screen for cocaine in any young patient presenting with chest pain/ACS per AHA recommendation).

**Screening.** No population newborn/carrier screening applies (not a genetic disease); toxicology screening in emergency, obstetric (maternal urine drug screening in suspected prenatal exposure), and occupational/forensic settings is the relevant "screening" analog.

---

## 11. Outcome / Prognosis

**Mortality.** Cocaine-involved overdose death rate in the U.S. was **8.6 per 100,000 population in 2023** (up from 4.5 in 2018), with **29,449 total cocaine-involved deaths in 2023**. Most acute-intoxication episodes are non-fatal and self-limited with supportive care; mortality risk concentrates in cases complicated by malignant arrhythmia, massive MI, hemorrhagic stroke, severe hyperthermia/agitated delirium, or opioid (fentanyl) co-exposure.

**Morbidity/complications.** MI (with risk of subsequent heart failure/cardiomyopathy), ischemic/hemorrhagic stroke (with attendant neurologic disability), AKI (occasionally requiring dialysis) from rhabdomyolysis, bowel infarction/perforation (occasionally requiring bowel resection/colostomy), pneumothorax, and — with levamisole adulteration — disfiguring cutaneous vasculitis/necrosis and life-threatening agranulocytosis-related sepsis.

**Recovery potential.** With prompt benzodiazepine-based supportive treatment, the acute behavioral/autonomic toxidrome typically resolves fully within hours without lasting sequelae. Organ-specific complications (MI, stroke) carry the same prognosis as their non-cocaine-associated counterparts once established, modulated by the patient's ongoing exposure risk (continued cocaine use is a well-recognized risk factor for MI recurrence).

**Prognostic factors.** Dose and route (smoked/IV worse than intranasal), co-exposure to alcohol (cocaethylene) or opioids (fentanyl), presence of pre-existing cardiovascular disease, degree of hyperthermia, and time-to-treatment (delay in benzodiazepine administration/cooling associated with worse outcomes in excited-delirium/rhabdomyolysis presentations).

---

## 12. Treatment

Cocaine intoxication has **no specific antidote or reversal agent** analogous to naloxone for opioids — management is supportive and directed at the specific toxidromic manifestations. NCIT terms noted per treatment.

**Pharmacotherapy (first-line — agitation, seizures, hypertension, tachycardia):**
- **Benzodiazepines** (e.g., lorazepam 2–3 mg IV, titrated every 5 minutes to effect; diazepam; midazolam) — first-line agents of choice for CNS excitation, agitation, seizures, and the accompanying tachycardia/hypertension; reduce mortality in animal models. **NCIT:C15986** (Pharmacotherapy) as the general treatment_term, with `therapeutic_agent` bound to specific benzodiazepine CHEBI terms (e.g., lorazepam **CHEBI:6539**).
  - **Caution:** flumazenil is contraindicated/dangerous in cocaine-intoxicated patients receiving benzodiazepines, as it can precipitate seizures.
- **Antipsychotics** (second-generation, e.g., olanzapine, risperidone, quetiapine) — added to benzodiazepines for severe/persistent agitation or psychosis; combination benzodiazepine + antipsychotic shown more effective than monotherapy for severe agitation.
- **Phentolamine** (α-adrenergic antagonist) — used for cocaine-associated coronary vasospasm/chest pain refractory to benzodiazepines/nitrates, based on catheterization-lab studies showing reversal of cocaine-induced coronary vasoconstriction back to baseline diameter.
- **Nitrates and aspirin** — recommended per AHA for cocaine-associated chest pain/ACS, exactly as for non-cocaine ACS.
- **Sodium bicarbonate (8.4%)** — specific treatment for cocaine-induced QRS widening (sodium-channel blockade), by increasing extracellular Na⁺ concentration and pH to overcome channel blockade; reverses crack-cocaine-induced cardiac conduction abnormalities.
- **Calcium-channel antagonists (dihydropyridine class)** — proposed adjunct for cocaine-induced cerebral/coronary vasospasm and ischemic stroke.
- **Contraindicated: beta-blockers** (including mixed-action agents like labetalol) — explicitly contraindicated by AHA scientific statement for cocaine-associated ACS/chest pain due to risk of exacerbating unopposed α-adrenergic coronary vasoconstriction.

**Supportive/critical care:**
- Active cooling measures for hyperthermia (evaporative cooling, cold IV fluids); aggressive IV fluid resuscitation and urine alkalinization considerations for rhabdomyolysis-associated AKI prevention; mechanical ventilation with propofol infusion for refractory agitation/status epilepticus; renal replacement therapy for severe AKI/hyperkalemia.
- **NCIT:C15747** (Supportive Care) as the general term for fluids, cooling, and monitoring.

**Surgical/interventional:** Emergent laparotomy/bowel resection for perforated bowel ischemia (**NCIT:C15329** Surgical Procedure); percutaneous coronary intervention for confirmed MI not responsive to medical vasodilator therapy; endovascular thrombectomy has been attempted for cocaine-induced large-vessel ischemic stroke but complicated by procedural vasospasm in reported cases.

**Adulterant-specific treatment:** Discontinuation of the offending exposure, granulocyte colony-stimulating factor (G-CSF) and infection precautions for levamisole-induced agranulocytosis, and wound care/immunosuppression consideration for levamisole-induced vasculitis skin necrosis (dermatology literature); naloxone for the opioid (fentanyl) component of mixed exposures.

**Experimental/pharmacogenomic-informed approaches:** Recombinant/engineered high-activity **butyrylcholinesterase mutants** ("cocaine hydrolase") have been investigated as a potential enzyme-based antidote to accelerate cocaine clearance and blunt toxicity/reward, informed directly by the BCHE pharmacogenomics discussed in §2/§4 (relevant patented biologics referenced in search results, e.g., US Patent 9,175,274 "High activity mutants of butyrylcholinesterase for cocaine hydrolysis"); not yet an approved clinical therapy.

**Treatment outcomes.** Benzodiazepine-first management is broadly effective for the behavioral/autonomic toxidrome; outcomes for organ-specific complications mirror those of the equivalent non-cocaine-associated condition once it has occurred (e.g., post-MI outcomes, post-stroke outcomes), with recurrence risk driven by continued cocaine exposure.

---

## 13. Prevention

**Primary prevention:** Avoidance of cocaine use altogether (substance-use-disorder primary-prevention programming, education); avoidance of concurrent alcohol use (cocaethylene) and of unknown/adulterated supply.
**Harm reduction (a form of tertiary/secondary prevention specific to this exposure):**
- **Fentanyl test strips** — inexpensive, effective point-of-use tool to detect fentanyl contamination in a cocaine sample before use, shown associated with overdose-risk-reduction behaviors (e.g., using less, using with someone present) in surveyed people who use drugs.
- **Naloxone co-carriage** — protective specifically against the opioid (fentanyl) component of a mixed cocaine-fentanyl exposure; does **not** reverse cocaine's own sympathomimetic toxicity, since there is no opioid-receptor mechanism involved in cocaine's action — an important distinction for any prevention narrative, since naloxone alone is insufficient for a pure cocaine overdose.
- Supervised consumption/overdose-prevention sites, and "never use alone"/buddy-system practices, reduce time-to-intervention for both the cocaine-specific toxidrome (seizure, arrhythmia, agitated delirium) and any opioid co-exposure.
**Secondary prevention:** Prompt emergency-department recognition and treatment (benzodiazepine-first protocols) to prevent progression from mild intoxication to malignant arrhythmia, MI, stroke, or agitated delirium/rhabdomyolysis.
**Behavioral interventions/counseling:** Contingency management and cognitive-behavioral therapy for underlying cocaine use disorder (reduces the frequency of future intoxication episodes, though this is squarely use-disorder rather than acute-intoxication treatment).
**Public health:** Drug-supply monitoring/checking programs (community drug-checking services testing for fentanyl in methamphetamine/cocaine samples), naloxone distribution programs, and surveillance systems (CDC overdose surveillance, State Unintentional Drug Overdose Reporting System) informing real-time public alerts about supply contamination.
**Prophylaxis:** No pre-exposure prophylactic medication exists for cocaine toxicity (unlike, e.g., vaccination models for some substances still in early research — anti-cocaine vaccine candidates have been studied experimentally but are not in routine clinical use).

---

## 14. Other Species / Natural Disease

**Taxonomy of affected species:** Cocaine toxicosis is well documented in **companion animals**, most notably dogs (*Canis lupus familiaris*, **NCBITaxon:9615**) and cats, typically from accidental ingestion of human drug supply, and occasionally in wildlife/exotic-pet contexts.

**Natural/accidental disease in animals:** A landmark University of Pennsylvania case series, "Presumptive cocaine toxicosis in 19 dogs: 2004–2012," characterized canine cocaine toxicity; a recent case report (2025, *Frontiers in Veterinary Science*) documented a 2-year-old Chihuahua presenting with lethargy and syncope found to have **first-degree and high-grade second-degree AV block** on ECG secondary to confirmed cocaine ingestion (urine drug screen positive, externally confirmed) — a clinically atypical bradyarrhythmic presentation in a species/context where sympathomimetic tachyarrhythmia would be expected, illustrating that cocaine's sodium/conduction-system effects can dominate over its adrenergic effects in some individual cases. Mechanism in dogs mirrors humans: cocaine blocks reuptake of dopamine, serotonin, and norepinephrine at presynaptic terminals, producing predominantly CNS (agitation, seizures) and cardiac (tachyarrhythmia, or in atypical cases bradyarrhythmia/AV block) signs. [Cocaine-induced AV block in a dog (PMC12399557)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12399557/); Merck Veterinary Manual overview of recreational-drug toxicoses in animals.

**Veterinary relevance/importance:** Recognized as an important accidental-poisoning category in small-animal emergency/critical-care medicine, driving development of accessible point-of-care veterinary urine drug screening and treatment protocols directly adapted from human sympathomimetic-toxidrome management (benzodiazepine sedation, cooling, supportive cardiac care).

**Comparative pathology:** The core molecular mechanism (monoamine transporter blockade; voltage-gated sodium/potassium channel blockade) is evolutionarily conserved across mammals, so the pathophysiological cascade described in §6 (adrenergic surge → vasoconstriction/tachyarrhythmia → hyperthermia/agitation) generalizes across species, though species-specific differences in baseline autonomic tone, body size/dosing sensitivity, and cardiac electrophysiology (as illustrated by the atypical canine AV-block case) can alter the dominant clinical phenotype.

**Transmission/zoonotic potential:** Not applicable — cocaine intoxication is a toxic-exposure event, not a transmissible infectious disease; there is no zoonotic or cross-species transmission mechanism (only shared accidental-exposure risk within a household).

---

## 15. Model Organisms

**Rodent self-administration and toxicity models** are the dominant experimental system:
- **Rat and mouse operant self-administration paradigms** — the "gold standard" behavioral model, directly simulating active drug-seeking/compulsive use; "breakpoint" (maximal responding for a fixed cocaine dose) quantifies motivational strength; long-access (~6 hr/day) vs. short-access (~2 hr/day) paradigms model escalation of intake and tolerance, informative for the *use disorder* trajectory that intoxication episodes feed into.
- **Genetically defined mouse panels** (inbred and recombinant-inbred lines, e.g., C57BL/6 vs. DBA strains, BALB/cByJ) — used to map genetic pathways regulating acquisition of cocaine self-administration and strain-dependent differences in cocaine reward/avoidance (e.g., anxiogenic effects limiting cocaine reward specifically in BALB/cByJ mice), directly modeling the genetic-modifier concept discussed in §2/§4.
- **Bche/Ces1 double-knockout mice** — a specific, mechanistically targeted model of human butyrylcholinesterase deficiency, showing prolonged toxic effects after cocaine challenge; directly recapitulates the human pharmacogenomic risk factor (K-variant/severe BChE deficiency) described above, making it the most disease-relevant genetic model for **intoxication severity** specifically (as opposed to addiction liability).
- **Rat cardiac toxicity models** — short-term and chronic cocaine-dosing protocols in rats reproduce myocardial oxidative stress, altered mitochondrial dynamics/biogenesis gene expression, and contraction-band necrosis with connexin-43 dephosphorylation, closely recapitulating human autopsy myocardial findings from cocaine-overdose deaths (PMC8677764; PMID:36233284) — a high-fidelity model for the cardiotoxicity mechanism in §6.
- **Rodent hyperthermia/seizure models** — used to dissect thermoregulatory impairment and glutamate/excitotoxicity mechanisms of cocaine-induced hyperthermia and seizures.
- **Non-rodent/cellular systems:** isolated cardiac myocyte and vascular smooth-muscle preparations (used in the coronary-sensitization/vasospasm mechanistic studies), and human post-mortem myocardial tissue (not a "model" per se, but the key translational validation tissue for the rodent cardiac-mitochondrial findings above).

**Phenotype recapitulation and limitations:** Rodent self-administration models recapitulate the reinforcing/addictive-behavior dimension well but do **not** directly model most of the acute organ-toxicity phenotypes central to *intoxication* (coronary vasospasm/MI, stroke, rhabdomyolysis) — those require the separate rat cardiac-dosing and mouse BChE-knockout paradigms noted above. No single model organism captures the full multi-organ human intoxication phenotype simultaneously; cardiac, CNS-behavioral, and pharmacogenomic-metabolic aspects are each modeled in separate, purpose-built rodent systems. Species differences in baseline heart rate/electrophysiology and in esterase expression levels (rodents generally have higher plasma esterase activity than humans) limit direct quantitative extrapolation of toxic dose thresholds from rodent to human.

**Resources:** MGI (Mouse Genome Informatics) for BCHE/Ces1 knockout allele records; standard rodent self-administration literature indexed via PubMed/PMC rather than a dedicated addiction-model database in the sources reviewed.

---

## Summary of Key Ontology Term Suggestions for KB Curation

| Domain | Suggested terms |
|---|---|
| MONDO | MONDO:0019544 (cocaine intoxication) |
| CHEBI | CHEBI:27958 (cocaine); CHEBI:83415 (benzoylecgonine, verify); relevant treatment agents (lorazepam CHEBI:6539, sodium bicarbonate CHEBI:32139) |
| GO (molecular function) | GO:0005329 (dopamine transporter activity); GO:0005335 (serotonin transporter activity); GO:0005326 (neurotransmitter transporter activity); GO:0005248 (voltage-gated Na⁺ channel activity); GO:0005249 (voltage-gated K⁺ channel activity) |
| GO (biological process) | GO:0006979 (response to oxidative stress); GO:0006915 (apoptotic process); GO:0007204 (positive regulation of cytosolic Ca²⁺) |
| CL | CL:0000746 (cardiac muscle cell); CL:0000359 (vascular smooth muscle cell); CL:0000700 (dopaminergic neuron); CL:0000187 (skeletal muscle cell) |
| UBERON | UBERON:0000948 (heart); UBERON:0000955 (brain); UBERON:0002113 (kidney); UBERON:0001240 (superior mesenteric artery) |
| HP | HP:0001649 (tachycardia); HP:0000822 (hypertension); HP:0001250 (seizure); HP:0003201 (rhabdomyolysis); HP:0001945 (hyperthermia); HP:0000709 (psychosis); HP:0011675 (arrhythmia); HP:0001919 (AKI) |
| NCIT | NCIT:C15986 (Pharmacotherapy); NCIT:C15747 (Supportive Care); NCIT:C15329 (Surgical Procedure) |

**Note on evidence gaps:** All mechanistic and epidemiological claims above trace to the cited PMIDs/URLs, all findable in a `just fetch-reference` pass. A few areas would benefit from targeted follow-up before KB entry finalization: (1) verified OMIM/Orphanet cross-references (the Orphanet ID surfaced by search was not independently confirmed against the Orphanet portal and should be re-verified or omitted); (2) a formal QoL-instrument (EQ-5D/SF-36) dataset specific to intoxication episodes was not located and may not exist as a distinct measure from cocaine-use-disorder QoL literature; (3) exact allele-frequency data for the DRD2/DAT1 variants from gnomAD were not retrieved in this pass.

---

### Sources

- [Cocaine Intoxication – MalaCards](https://www.malacards.org/card/cocaine_intoxication)
- [ICD10Data F14 Cocaine related disorders](https://www.icd10data.com/ICD10CM/Codes/F01-F99/F10-F19/F14-)
- [Insights into Dopamine Transporter Function by Cocaine Binding (PMC4460958)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4460958/)
- [Cocaine hydrolase blocks cocaine-induced DAT trafficking (PMC8720053)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8720053/)
- [The Cardiovascular Effects of Cocaine – JACC](https://www.jacc.org/doi/10.1016/j.jacc.2017.05.014)
- [Coronary-artery spasm and MI associated with cocaine use – PMID:6727939](https://pubmed.ncbi.nlm.nih.gov/6727939/)
- [Cocaine sensitization of coronary artery contractions – PMID:7680716](https://pubmed.ncbi.nlm.nih.gov/7680716/)
- [Sympathomimetic Toxicity – Medscape](https://emedicine.medscape.com/article/818583-clinical)
- [Cocaine Intoxication and Thyroid Storm (PMC4528882)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4528882/)
- [Cocaine: Updated Overview on Chemistry, Detection, Biokinetics (PMC9032145)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9032145/)
- [Cocaethylene metabolism – PMID:12485948](https://pubmed.ncbi.nlm.nih.gov/12485948/)
- [Metabolic Enzymes of Benzoylecgonine – PMID:27224254](https://pubmed.ncbi.nlm.nih.gov/27224254/)
- [An Evidence-Based Approach to Cocaine-Associated Emergencies](https://www.ebmedicine.net/topics/toxicology-environmental/cocaine-emergencies)
- [Cocaine Toxicity – StatPearls (NBK430976)](https://www.ncbi.nlm.nih.gov/books/NBK430976/)
- [Dopamine transporter DAT and receptor DRD2 variants affect risk of lethal cocaine abuse – PMID:23340505](https://pubmed.ncbi.nlm.nih.gov/23340505/)
- [Intronic DRD2 splicing polymorphisms and cocaine abuse – Neuropsychopharmacology](https://www.nature.com/articles/npp2010208)
- [Genomic factors associated with SUD relapse – review](https://www.sciencedirect.com/science/article/pii/S2352853224000464)
- [CDC NCHS – U.S. Overdose Deaths Decrease Third Consecutive Year in 2025](https://www.cdc.gov/nchs/pressroom/releases/20260513.html)
- [Drug Overdose Deaths Involving Stimulants — MMWR](https://www.cdc.gov/mmwr/volumes/74/wr/mm7432a1.htm)
- [QuickStats: Cocaine Overdose Death Rates by Region (PMC10578952)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10578952/)
- [Neurochemical/pharmacological aspects of cocaine-induced seizures](https://www.researchgate.net/publication/11572322)
- [Frontiers – Neurotoxicity mechanisms of six recreational drugs (2025)](https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2025.1526270/full)
- [Mechanism of Cocaine-Induced Hyperthermia in Humans – Annals of Internal Medicine](https://www.acpjournals.org/doi/10.7326/0003-4819-136-11-200206040-00006)
- [Cocaine-associated rhabdomyolysis and excited delirium – PMID:10414649](https://pubmed.ncbi.nlm.nih.gov/10414649/)
- ["Coke in the Dope" – cocaine-adulterated fentanyl supply – PMID:38829035](https://pubmed.ncbi.nlm.nih.gov/38829035/)
- [Charting the Fourth Wave – polysubstance fentanyl deaths, Addiction 2023](https://onlinelibrary.wiley.com/doi/10.1111/add.16318)
- [US stimulant-without-opioid overdose deaths rose in 2024 (PMC13545347)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13545347/)
- [Potential latent effects of prenatal cocaine exposure (PMC3037026)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3037026/)
- [Congenital cocaine syndrome – MedLink Neurology](https://www.medlink.com/articles/congenital-cocaine-syndrome)
- [Prenatal cocaine exposure causes vascular dysfunction in adult offspring (PMC2698595)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2698595/)
- [Modeling Cocaine Relapse in Rodents (PMC6034989)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6034989/)
- [Genetic pathways regulating cocaine self-administration in mice (PMC10530068)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10530068/)
- [Anxiogenic-Like Effects Limit Rewarding Effects of Cocaine in BALB/cByJ Mice](https://www.nature.com/articles/1395613)
- [Myocardial oxidative damage in cocaine-related overdose – Scientific Reports](https://www.nature.com/articles/srep44262)
- [Altered cardiac mitochondrial dynamics after cocaine (PMC8677764)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8677764/)
- [Oxidative Stress and Cocaine Intoxication in Cardiotoxicity (PMC8705810)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8705810/)
- [Contraction Band Necrosis with Dephosphorylated Connexin 43 – PMID:36233284](https://pubmed.ncbi.nlm.nih.gov/36233284/)
- [Acute GI manifestations of crack cocaine – PMID:11146022](https://pubmed.ncbi.nlm.nih.gov/11146022/)
- [Cocaine-Induced Chronic Bowel Ischemia (PMC11126889)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11126889/)
- [Management of Cocaine-Associated Chest Pain and MI – AHA Scientific Statement (Circulation)](https://www.ahajournals.org/doi/10.1161/circulationaha.107.188950)
- [Outcomes of beta-blocker use in cocaine-associated chest pain (PMC7529122)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7529122/)
- [Cocaine and Ischemic or Hemorrhagic Stroke – systematic review (MDPI)](https://www.mdpi.com/2077-0383/12/16/5207)
- [Treatment advances for cocaine-induced ischemic stroke – dihydropyridine calcium antagonists](https://pubmed.ncbi.nlm.nih.gov/11481148/)
- [Levamisole-Adulterated Cocaine: Vasculitis and Severe Neutropenia (PMC12851635)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12851635/)
- [p-ANCA-Associated Vasculitis Caused by Levamisole-Adulterated Cocaine – PMID:23476825](https://pubmed.ncbi.nlm.nih.gov/23476825/)
- [Butyrylcholinesterase Genetic Variants: Association with Cocaine Dependence – PLOS ONE, PMID:24312228](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0080505)
- [Prolonged Toxic Effects After Cocaine Challenge in Bche/Ces1 Double Knockout Mice](https://dmd.aspetjournals.org/article/S0090-9556(24)05821-5/abstract)
- [LOINC 42241-0 Cocaine+Benzoylecgonine in Urine](https://loinc.org/42241-0)
- [Sensitive assay for urinary benzoylecgonine (PMC5573903)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5573903/)
- [Crack Cocaine-Induced Cardiac Conduction Abnormalities Reversed by Sodium Bicarbonate (PMC3677010)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3677010/)
- [Treatment of cocaine-induced arrhythmias – bench to bedside (Br J Clin Pharmacol)](https://bpspubs.onlinelibrary.wiley.com/doi/10.1111/j.1365-2125.2010.03632.x)
- [Fentanyl Test Strip Use and Overdose Risk Reduction – JAMA Network Open](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2833888)
- [Cocaine-induced first-degree and high-grade second-degree AV block in a dog (PMC12399557)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12399557/)
- [SAMHSA 2024 NSDUH Annual National Report](https://www.samhsa.gov/data/sites/default/files/reports/rpt56287/2024-nsduh-annual-national-report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 40 |
| Resolved | 40 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 40 |
| On topic | 13 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 85 |
| Resolved | 83 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 17 |
| Terms named correctly | 11 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000734` (1 mention) - the report calls it "Impulsivity"; HP calls it **Disinhibition**
- `HP:0002140` (1 mention) - the report calls it "Cerebral ischemia"; HP calls it **Ischemic stroke**
- `HP:0001919` (2 mentions) - the report calls it "Acute kidney injury (secondary to rhabdomyolysis/vasoconstriction)"; HP calls it **Acute kidney injury**
- `HP:0030828` (1 mention) - the report calls it "Bronchospasm/wheezing ("crack lung")"; HP calls it **Wheezing**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005329` (GO_0005329) (2 mentions) - replaced by `GO:0005330`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001638` (1 mention) - the report calls it "Cardiomyopathy (acute/chronic)"; HP calls it **Cardiomyopathy**
- `HP:0001945` (2 mentions) - the report calls it "Hyperthermia"; HP calls it **Fever**, and lists "Hyperthermia" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.