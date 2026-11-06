---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-27T19:52:33.714632'
end_time: '2026-10-27T19:59:31.014333'
duration_seconds: 417.3
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Hereditary Folate Malabsorption
  mondo_id: MONDO:0009238
  category: Mendelian
  causal_genes: SLC46A1
  omim_id: not recorded
  synonyms: Congenital folate malabsorption; PCFT deficiency
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
  web_search_requests: 5
  num_turns: 34
  total_cost_usd: 2.9856467
  session_id: 0bfb328d-96db-5dca-803a-342a247b0264
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  assistant_text_blocks: 4
citation_count: 16
reference_validation:
  total_references: 40
  verified: 40
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 11
  quotes_valid: 10
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:28687492
  relevance_assessed: 40
  on_topic: 37
  off_topic: 1
  off_topic_references:
  - PMID:28687492
  needs_review: true
  validator_version: 0.4.0
term_validation:
  total_terms: 67
  verified: 64
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 0
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0009238
    reported_labels:
    - MONDO
    ontology_label: hereditary folate malabsorption
  - term_id: DOID:0111678
    reported_labels:
    - DOID
    ontology_label: hereditary folate malabsorption
  unresolvable_prefixes:
  - OMIM
  - Orphanet
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hereditary Folate Malabsorption
- **MONDO ID:** MONDO:0009238 (if available)
- **Causal gene(s):** SLC46A1
- **OMIM:** not recorded
- **Synonyms:** Congenital folate malabsorption; PCFT deficiency
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Hereditary Folate Malabsorption** covering all of the
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

I'm pulling primary-literature abstracts from PubMed to cite in the report.

Still collecting abstracts. The fetch tool won't return full abstracts verbatim, so I'm pulling short exact quotes paper by paper.

Gathering the last few sources: intramuscular-dosing studies and recent reviews. The report follows.

# Hereditary Folate Malabsorption (HFM; MONDO:0009238): Disease Characteristics Research Report

**Causal gene: *SLC46A1*** (HGNC `hgnc:30521`). The gene encodes the proton-coupled folate transporter (PCFT), which was originally annotated as heme carrier protein 1 (HCP1). HFM is an autosomal recessive disease caused by biallelic loss-of-function variants in *SLC46A1*. Its MONDO cross-references (OMIM:229050, Orphanet:90045) all point to this gene. It is a different disease from FOLR1-related cerebral folate transport deficiency, which is caused by *FOLR1* and confined to the brain; see the differential diagnosis.

**About the sources:**
- Every quotation below comes from the PubMed abstract text served by the Europe PMC REST API on 2026-10-27. The quotes are short clauses, not whole abstracts.
- None of them has been put through `just fetch-reference` or the dismech snippet validator. Treat each one as a lead to check before using it as a KB snippet.
- I could not open the GeneReviews chapter (NBK1673) or the OMIM and Orphanet pages because they block automated access. Statements attributed to those sources are marked as indirect.
- Ontology IDs marked ✔ were read from the repository's `cache/*/terms.csv` files. IDs marked ⚠ come from memory and must be looked up before use.

---

## 1. Disease Information

**Overview.** HFM is an inherited defect of folate transport. Without functional PCFT, folate cannot be absorbed in the proximal small intestine and cannot be transported from blood into the cerebrospinal fluid (CSF). The result is a syndrome of systemic and cerebral folate deficiency that begins in early infancy. Typical features are megaloblastic anemia or pancytopenia, failure to thrive, diarrhea, oral mucositis, and an immunodeficiency that can look like SCID, with opportunistic infections such as *Pneumocystis jirovecii* pneumonia. Untreated or late-treated children develop developmental delay, seizures, and sometimes cerebral calcification.

- Zhao et al. 2017 review (PMID:27664775): loss of PCFT "results in a syndrome characterized by severe systemic and cerebral folate deficiency."
- PMID:20724482: "The proton-coupled folate transporter (PCFT/SLC46A1) mediates obligatory intestinal folate absorption."

**Identifiers** (from the MONDO cross-references, read through OLS4):

| Resource | ID |
|---|---|
| MONDO | MONDO:0009238 |
| OMIM (phenotype) | 229050 |
| Orphanet | ORPHA:90045 |
| MeSH | C562799 (supplementary concept) |
| UMLS | C0342705 |
| DOID | DOID:0111678 |
| NCIT | C156424 |
| GARD | 0012983 |
| SNOMED CT | 62578003 |
| ICD-11 (foundation URI) | 773545237 |
| ICD-10 | none listed in MONDO. Coders often use D52.8 or E53.8 (⚠ not verified). |
| Gene | *SLC46A1*, `hgnc:30521` ✔ (in the stub); NCBI Gene 113235 ⚠; UniProt Q96NT5 ⚠; OMIM gene 611672 ⚠ |

**Synonyms:** congenital folate malabsorption; congenital defect of folate absorption; folic acid transport defect (all from MONDO); PCFT deficiency; hereditary folate malabsorption syndrome.

**Nature of the evidence.** The literature consists of individual case reports and small family series. There are no registries or EHR cohorts. A 2017 review summarized "thirty-seven known cases with the clinical syndrome, of which thirty have been verified by genotype" (PMID:27664775). Case reports have continued since then, from China, India, Japan, Palestine, Argentina and Morocco, among others.

---

## 2. Etiology

- **Cause.** The disease is purely genetic: biallelic pathogenic *SLC46A1* variants. Most are homozygous and occur in consanguineous families or founder populations.
  - Founding paper, Qiu et al. 2006 (PMID:17129779): "a loss-of-function mutation in this gene is the molecular basis for hereditary folate malabsorption".
- **Genetic risk factors.**
  - Parental consanguinity, for example the Pakistani family in PMID:20005757 and the Turkish siblings in PMID:20795774.
  - Puerto Rican ancestry, which carries a founder splice variant (PMID:21489556).
  - Japanese ancestry, which carries a founder deep-intronic variant (PMID:31494288).
- **Environmental modifiers.** No environmental factor causes HFM. However, folate stores at birth come from the mother through the placenta, and other carriers handle this, so neonates are protected at first: "Newborns with this condition have initially normal folate stores" (PMID:28687492 is wrong; the correct PMID is 28685492). Symptoms appear as those stores run out, usually in the first months of life.
  - Inference, not demonstrated in HFM: a low-folate diet, or drugs that compete for PCFT, would plausibly hasten decompensation. PMID:23609145 reports that bicarbonate and other anions inhibit PCFT.
- **Protective factors.** No protective genetic variants are known. Missense variants that leave residual activity, such as N411K (PMID:29344585), may produce milder disease. Early parenteral folinic acid is protective against neurological sequelae (see §12).
- **Gene–environment interaction.** The best-documented interaction is between genotype and treatment: patients who receive high-dose reduced folate early can develop normally (PMID:18718264, PMID:20795774). No other gene–environment interactions have been documented.

---

## 3. Phenotypes

Onset is typically between the first weeks and the first few months of life. Frequencies are qualitative because cohorts are small.

| Phenotype | HPO | Type / onset / course | Frequency and notes | Key citation and quote |
|---|---|---|---|---|
| Megaloblastic anemia | HP:0001889 ✔ | Laboratory/clinical; infancy; reverses with folate | Nearly universal at presentation | PMID:27938595: "presented with megaloblastic anemia from their infant period" |
| Macrocytic anemia (alternative term) | HP:0001972 ✔ | — | Mouse model | PMID:21346251 (mouse): "severe macrocytic normochromic anemia and pancytopenia" |
| Pancytopenia | HP:0001876 ✔ | Infancy | Frequent | PMID:25504888: "early-onset pancytopenia and secondary immunodeficiency"; PMID:40937236 |
| Thrombocytopenia | HP:0001873 ✔ | Infancy | Occasional; can cause hemorrhage | PMID:35773682: "megaloblastic anemia and occasionally thrombocytopenia" |
| Neutropenia / leukopenia | HP:0001875 / HP:0001882 ⚠ | Infancy | Common; can present as neutropenic fever | PMID:36045837: "HFM can present as neutropenic fever." |
| Combined immunodeficiency | HP:0005387 ✔ | Infancy; reverses | Frequent; can mimic SCID | PMID:19740703: "Clinical presentation of PCFT deficiency may mimic severe combined immune deficiency (SCID)." |
| Hypogammaglobulinemia / panhypogammaglobulinemia | HP:0004313 ⚠ / HP:0003139 ✔ | Infancy | Frequent | PMID:24691418: "with an impaired T cell proliferation response, pan-hypogammaglobulinemia" |
| *Pneumocystis jirovecii* pneumonia | HP:0020102 ✔ | Infancy | Recurring opportunistic infection | PMID:19740703: "failure to thrive, normocytic anemia, Pneumocystis jirovecii pneumonia and systemic cytomegalovirus infection" |
| Recurrent infections | HP:0002719 ✔ | Infancy and childhood | Common | PMID:33146883: "recurrent pneumonia, diarrhea, and mouth ulcers" |
| Failure to thrive | HP:0001508 ✔ | Infancy | Common | PMID:19740703 (above) |
| Diarrhea | HP:0002014 ✔ | Infancy | Common | PMID:40937236: "pancytopenia, diarrhea, hypogammaglobulinemia, and neurological regression" |
| Oral mucositis / stomatitis / mouth ulcers | HP:0010280 Stomatitis ✔ | Infancy | Common | PMID:33146883 (above) |
| Global developmental delay | HP:0001263 ✔ | Late infancy onward; may be permanent | Frequent when treatment is delayed | PMID:25504888: "frequently present with neurodevelopmental delay and megaloblastic anemia" |
| Developmental regression | HP:0002376 ✔ | Infancy | Seen in untreated cases | PMID:40937236 |
| Seizures (including refractory epilepsy) | HP:0001250 ✔ | Infancy, sometimes later onset | Frequent when untreated; may resist folic acid | PMID:21333572: "late-onset seizures"; PMID:42809880: "Early-onset refractory epilepsy and hyperhomocysteinemia were key diagnostic clues." |
| Cerebral (occipital/cortical) calcification | HP:0002514 ✔ | Progressive in childhood | Characteristic in late-diagnosed cases | PMID:27938595: "progressive bilateral symmetrical calcification"; PMID:31371121: "bilateral occipital, cortical calcifications characteristic of hereditary folate malabsorption" |
| Microcephaly, spastic tetraplegia | HP:0000252 ✔, HP:0002510 ✔ | Childhood | Late-treated cases | PMID:33146883: "microcephaly with spastic quadriparesis" |
| Cognitive impairment / intellectual disability | HP:0001249 ✔ | Childhood | Variable | PMID:26006721: "seizures, and cognitive impairment" |
| Ataxia, peripheral neuropathy, movement disorder | HP:0001251 ✔, HP:0009830 ✔ | Childhood | Reported in reviews (⚠ secondary; not taken from a quote) | — |
| Low serum and very low CSF folate / 5-MTHF | Use an HP CSF-folate term ⚠ | Laboratory | Defining feature | PMID:19740703: "Serum and cerebrospinal fluid folate levels were undetectable."; PMID:27938595: CSF folate and 5-MTHF "were both zero" |
| Hyperhomocysteinemia | HP:0002160 Hyperhomocystinemia ✔ | Laboratory | Common | PMID:42809880 |
| Pulmonary hemorrhage | HP:0040223 ✔ | Rare, catastrophic | Single case | PMID:35773682: "the patient suddenly went into cardiac arrest due to pulmonary hemorrhage" |

**Impact on quality of life.** No HFM-specific EQ-5D, SF-36 or PROMIS data exist.
- The burden falls on lifelong daily or intermittent parenteral (intramuscular) therapy and repeated lumbar punctures for CSF monitoring (PMID:28685492, PMID:26006721).
- When treatment starts late, neurodisability can be permanent (PMID:33146883: "a partial improvement in neurological symptoms").
- When treatment starts early, outcome can be completely normal. One woman reached age 27 "normal in all respects having completed higher education" (PMID:18718264).

---

## 4. Genetic and Molecular Information

**The gene.** *SLC46A1* sits at 17q11.2, has 5 exons, and is a member of the major facilitator superfamily (MFS).
- Qiu 2006 described it as "a human proton-coupled, high-affinity folate transporter". The paper also notes it "was previously reported to be a lower-affinity, pH-independent heme carrier protein, HCP1."
- Transcription is regulated by NRF-1 (PMID:20724482).

**Spectrum of pathogenic variants.** All reported variants are germline, and most are homozygous.

| Variant (as published) | Type | Population | Effect | PMID |
|---|---|---|---|---|
| c.1082-1G>A; exon 3 skipping, p.Y362_G389del (Mahadeo 2011 writes it as "c.1082G>A; p.Y362_G389 del") | Splice acceptor | **Puerto Rican founder** | No functional protein | 19740703, 21489556 |
| c.1166-285T>G | Deep intronic; creates a cryptic donor; 168-bp intron 3 insertion and premature stop | **Japanese founder (proposed)** | Loss of function | 31494288 |
| c.204_205delCC (N68Kfs) | Frameshift | Turkish; compound heterozygous in another family | Loss of function | 20795774, 21333572 |
| c.194dupG, p.Cys66LeufsX99 | Frameshift | Pakistani (consanguineous) | Truncation | 20005757 |
| c.17_18insC (E9Gfs) | Frameshift | — | Loss of function | 21333572 |
| c.558–588del (at I188) | Frameshift deletion | Nicaraguan | Premature stop | 23816405 |
| c.620dupG | Frameshift | Indian | Loss of function | 33146883 |
| c.981_982del, p.Tyr327Ter | Nonsense | Argentine | Loss of function | 42809880 |
| A335D (c.1004C>A), G338R (c.1012G>C) | Missense | — | Loss of function | 21333572, 22843796 |
| R113S / R113C | Missense | — | Arg113 is required for folate binding | 18559978, 19508863 |
| D156Y | Missense | — | Loss of function | 20805364 |
| R376Q | Missense | — | Altered substrate binding | 20686069 |
| P425R | Missense | — | Highly selective loss of folate binding | 22345511 |
| N411K (external gate) | Missense with residual activity | — | Protein is stable and traffics normally; largest loss is for 5-MTHF | 29344585 |
| F392V | Missense | — | Locks the transporter in an inward-open conformation | 32893190 |
| S196L | Missense | — | Inactive | 32893190 |
| c.1127G>A (consequence not confirmed here) | Missense | Indian | Reported alongside β-thalassemia trait | 41459184 |

**Mechanism of loss of function** (PMID:17446347):
- "4 of the mutated transporters resulted in a complete loss of transport function". This was "primarily due to decreased protein stability and/or defects in membrane trafficking".
- "Mutations involved 4 of the 5 exons, all at highly conserved amino acid residues."
- Some missense variants cause conformational trapping instead (F392V, PMID:32893190). A 2025 molecular-dynamics study of a disease mutation found "an enlarged and distorted pore accompanied by loss of long-range contacts" (PMID:39924111).

**Functional class:** LOSS_OF_FUNCTION for most variants; PARTIAL_LOSS_OF_FUNCTION for N411K.

**Classification:** ACMG classifications are listed in ClinVar but were not retrieved here. GenCC has a submission for this gene–disease pair (SGC-180490.1, found in search; tier not verified).

**Population frequencies.**
- Puerto Rico (PMID:21489556): "Three heterozygote carriers were identified from the 1582 newborn samples randomly selected." The carrier frequency was "0.2% island-wide", with a higher, regionally clustered figure "in Villalba" (the abstract reads 6.3%; check this against the source).
- gnomAD frequencies were not retrieved.

**Other genetic layers:**
- Modifier genes: none known.
- Epigenetics: no disease-specific data. NRF-1 drives the promoter (PMID:20724482).
- Chromosomal abnormalities: none reported. Large deletions are possible but undocumented.

---

## 5. Environmental Information

- **Exposures and lifestyle.** Not causal. Dietary folate cannot compensate at physiological doses. At pharmacological doses, reduced folates are absorbed by other, low-efficiency routes (PMID:24512081 discusses "the mechanism of intestinal folate absorption in the absence of PCFT").
- **Infectious agents.** None are causal. Opportunistic infections (*Pneumocystis jirovecii*, cytomegalovirus) are complications of the folate-deficient immunodeficiency (PMID:19740703).
- **Maternal folate.** Folate transferred to the fetus is the "exposure" that delays onset.

---

## 6. Mechanism and Pathophysiology

### Ordered causal chain

1. **Germline biallelic *SLC46A1* loss-of-function variants** (splice, frameshift, nonsense, or destabilizing or conformation-locking missense) **lead to** absent or non-functional PCFT protein (PMID:17446347, 32893190). *Demonstrated.*
2. **Loss of PCFT at the apical brush border of proximal small-intestinal enterocytes** (duodenum and jejunum), where PCFT uses the acidic microclimate to co-transport folate with protons, **results in** failure of intestinal folate absorption (PMID:24512081: "its critical role in folate transport across the apical brush-border membrane of the proximal small intestine"; PMID:17129779). *Demonstrated in humans, and in mice in PMID:21346251.*
   - **Branch 2b. Loss of PCFT in the choroid plexus epithelium leads to** failure of folate transport from blood into the CSF. PCFT works with folate receptor α (FRα), probably by exporting folate from acidified endosomes after FRα-mediated endocytosis (PMID:27664775: PCFT is "required for transport of folates into the cerebrospinal fluid"; PMID:19074442: "FRalpha and PCFT co-localized to the endosomal compartment"). *The endosomal-export model is supported in vitro. The CSF transport defect is demonstrated clinically, because CSF folate stays low even when serum folate has been corrected.*
3. Once **placentally derived neonatal folate stores** are exhausted (PMID:28685492), **systemic folate deficiency** follows: very low serum and red-cell folate, plus hyperhomocysteinemia from impaired remethylation (PMID:42809880).
4. **Depletion of reduced folate cofactors (THF, 5,10-methylene-THF, 10-formyl-THF) leads to** impaired thymidylate and purine synthesis and impaired one-carbon (methyl) metabolism. *This step is inferred from folate biochemistry, not measured in HFM tissue.*
5. **Defective DNA synthesis in rapidly dividing cells results in:**
   - **5a. Bone marrow.** Ineffective erythropoiesis with megaloblastic maturation arrest causes megaloblastic or macrocytic anemia, neutropenia, thrombocytopenia and pancytopenia. In mice: "Immature erythroblasts accumulated in the bone marrow and spleen of PCFT(-/-) mice and failed to differentiate further" (PMID:21346251). Severe thrombocytopenia can cause hemorrhage (PMID:35773682).
   - **5b. Lymphocytes.** Impaired T-cell proliferation and hypogammaglobulinemia cause combined immunodeficiency that mimics SCID, with opportunistic infections. The immunodeficiency reverses with folate (PMID:24691418, 19740703).
   - **5c. Gut epithelium.** Mucosal turnover fails, causing diarrhea and oral mucositis, which may worsen malnutrition and failure to thrive. *Inferred; this vicious cycle is proposed but not demonstrated.*
6. **Cerebral folate deficiency** (from step 2b plus systemic deficiency) **results in** impaired neuronal and glial one-carbon metabolism and myelination. Clinically this appears as developmental delay or regression, seizures, and progressive occipital and cortical calcification (PMID:27938595, 31371121). *The causal mechanism from low CSF 5-MTHF to calcification is not known.*
7. **Response to treatment:**
   - The hematological and immune defects correct readily with pharmacological reduced folate.
   - The neurological defect needs CSF 5-MTHF to be restored. That requires high doses, often intramuscular (PMID:31371121), and late-treated neurological damage may persist (PMID:33146883).
   - Folic acid itself is inappropriate. It "is responsive" for anemia but neurological signs "are refractory to folic-acid treatment" (PMID:26006721). The usual explanation is that folic acid binds FRα at the choroid plexus with high affinity and competes with 5-MTHF. *This explanation comes from reviews and is not a demonstrated human finding.*

### Checklist detail

- **Pathway.** Folate transport, then one-carbon metabolism: thymidylate synthesis, de novo purine synthesis, and the methionine cycle.
- **Protein dysfunction.** PCFT is an MFS-fold transporter with 12 transmembrane helices and functions as a homo-oligomer (PMID:22179615). Disease variants cluster in transmembrane segments, the substrate-binding pocket (R113, D156, R376), the GXXG motif (G338, PMID:22785121) and the external gate (N411). Cryo-EM structures of chicken PCFT have been published (reviewed in PMID:35061292); the primary structure paper was not retrieved here.
- **Immune involvement.** Secondary, folate-deficient combined immunodeficiency. Abnormalities include "an imbalanced pro-inflammatory cytokine profile" (PMID:24691418).
- **Omics, single-cell, CRISPR.** No HFM patient omics datasets were identified.

**Suggested GO terms** (✔ = cached in the repository):
- GO:0098838 folate transmembrane transport ✔
- GO:1904447 folate import across plasma membrane ✔
- GO:0008517 folic acid transmembrane transporter activity ✔ (a proton-symporter-specific child term may exist ⚠)
- GO:0050892 intestinal absorption ✔
- GO:0006730 one-carbon metabolic process ✔
- GO:0046653 tetrahydrofolate metabolic process ✔
- GO:0050667 homocysteine metabolic process ✔
- GO:0006260 DNA replication ✔
- GO:0006164 purine nucleotide biosynthetic process ✔
- GO:0043249 erythrocyte maturation ✔ (modifier DECREASED)
- Cellular component: GO:0031526 brush border membrane ✔, GO:0016324 apical plasma membrane ✔, GO:0010008 endosome membrane ✔

**Suggested CL terms:**
- CL:0000584 enterocyte ✔
- CL:0000706 choroid plexus epithelial cell ✔
- CL:0000765 erythroblast ✔
- CL:0000775 neutrophil ✔
- CL:0000556 megakaryocyte ✔
- CL:0000084 T cell ✔
- CL:0000236 B cell ✔

**Suggested CHEBI terms:**
- CHEBI:15641 5-methyltetrahydrofolic acid ✔
- CHEBI:15640 5-formyltetrahydrofolic acid ✔
- CHEBI:63606 (6S)-5-formyltetrahydrofolic acid ✔ (levoleucovorin)
- CHEBI:748997 leucovorin ✔
- Folic acid: CHEBI:27470 ⚠

---

## 7. Anatomical Structures Affected

- **Primary:**
  - Proximal small intestine: UBERON:0002114 duodenum ✔, UBERON:0002115 jejunum ✔, UBERON:0002108 small intestine ✔
  - Choroid plexus: UBERON:0001886 ✔
  - CSF compartment: UBERON:0001359 ✔
- **Secondary:**
  - Bone marrow: UBERON:0002371 ✔
  - Brain: UBERON:0000955 ✔, especially occipital cortex and subcortical regions, where calcification occurs (bilateral and symmetrical, PMID:27938595)
  - Immune system
  - Oral mucosa
  - Lung (opportunistic infection, hemorrhage)
- **Subcellular:** apical/brush-border plasma membrane; endosomes (folate export after FRα endocytosis).
- **Body systems:** digestive, hematopoietic, immune, nervous.
- **Lateralization:** brain lesions are bilateral and symmetric.

---

## 8. Temporal Development

- **Onset.** Usually in the first months of life, after neonatal folate stores are depleted (PMID:28685492). Onset ranges from neonatal neutropenic fever (PMID:36045837) to diagnosis in later childhood when presentation is mild or missed, as with the five-year-old in PMID:33146883.
- **Onset pattern.** Subacute: progressive pallor, diarrhea and infections over weeks.
- **Course.** Without treatment the disease is progressive and can be fatal. One sibling in PMID:40937236 had "a fatal outcome" after delayed diagnosis and stopped treatment. With treatment the disease remits but persists for life. Hematological and immune remission is driven by treatment; neurological remission depends on how early treatment starts.
- **Critical period.** Early infancy, before neurological injury. Early treatment can give a normal developmental outcome (PMID:20795774: "resulted in normal development now at ages 3 and 1 year"). Stopping treatment leads to relapse.
- **Stages.** No formal staging exists.

---

## 9. Inheritance and Population

- **Inheritance:** autosomal recessive, HP:0000007 ✔ (PMID:20724482: "an autosomal recessive disorder").
- **Penetrance:** appears complete for biallelic null variants.
- **Expressivity:** variable, driven mainly by how early treatment starts and possibly by residual activity of the variant.
- **Not reported:** anticipation; mosaicism.
- **Prevalence:**
  - Unknown; Orphanet-derived summaries give <1/1,000,000 (indirect).
  - Reported cases: 37 by 2017, of which 30 were genotyped (PMID:27664775). Later sources mention "~15 families" (MedlinePlus, dated) and around 60 individuals reported worldwide (MedlinePlus snapshot, indirect).
  - The disease is likely underdiagnosed.
- **Founder effects:**
  - Puerto Rico: carrier frequency 0.2% island-wide, clustered in Villalba (PMID:21489556). The authors concluded "newborn screening should be considered in high-risk populations".
  - Japan: c.1166-285T>G, which "could be a founder mutation in the Japanese population" (PMID:31494288).
- **Consanguinity:** frequent in reported families.
- **Geography:** worldwide. Reports come from the USA/Puerto Rico, Japan, China, Turkey, Pakistan, India, Nicaragua, Palestine, Argentina, Morocco and several European countries.
- **Sex ratio:** no sex bias expected; the reported numbers are too small to estimate one.

---

## 10. Diagnostics

**Laboratory findings:**
- Very low serum and red-cell folate.
- Megaloblastic anemia or pancytopenia; bone marrow shows megaloblastic changes.
- Elevated homocysteine.
- Hypogammaglobulinemia and abnormal lymphocyte proliferation.
- **Low or undetectable CSF folate (5-MTHF), and a low CSF-to-serum folate ratio.** Normally CSF folate is higher than blood folate. In HFM, CSF folate stays low even after blood folate has been corrected. This is the key discriminator (reviewed in PMID:27664775; specific numeric thresholds are in GeneReviews, not retrieved).
- A historical oral folate absorption test exists but has been replaced by genetic testing.
- Vitamin B12 must be checked to exclude cobalamin disorders.

**Imaging:** CT or MRI showing bilateral occipital and cortical calcifications (PMID:31371121, 27938595).

**Genetic testing:**
- Per GeneReviews (revised 15 Feb 2024; quoted indirectly through search), diagnosis requires "biallelic pathogenic (or likely pathogenic) variants in SLC46A1".
- Targeted founder-variant testing comes first in Puerto Rican or Japanese patients. Standard sequencing can miss the Japanese founder variant, which is deep intronic; it needs RNA studies or genome sequencing (PMID:31494288).
- Exome sequencing commonly makes the diagnosis (PMID:42809880, 41459184).
- CMA, karyotype, FISH, mtDNA and repeat testing are not relevant, except a deletion/duplication assay for a suspected exonic deletion.

**Differential diagnosis:**
- Nutritional folate or B12 deficiency.
- Inborn errors of cobalamin metabolism (transcobalamin II deficiency, cblC and related).
- MTHFR deficiency.
- DHFR deficiency.
- Glutamate formiminotransferase deficiency.
- **FOLR1-related cerebral folate transport deficiency.** CSF folate is low but serum folate and blood counts are normal, and onset is later.
- SCID and other primary immunodeficiencies. Counts and immunity in HFM normalize with folate.
- Congenital malabsorption or celiac disease.
- Aicardi–Goutières syndrome, because of the cerebral calcification.
- Antifolate drug exposure.

**Screening:** no newborn screening programme exists. Targeted carrier or newborn screening has been proposed for high-risk Puerto Rican populations (PMID:21489556). Cascade testing of siblings is advisable, because affected siblings treated presymptomatically do well (PMID:20795774, 40937236).

---

## 11. Outcome and Prognosis

- **Untreated:** fatal infections, hemorrhage or neurological deterioration are reported (PMID:40937236, 35773682).
- **Treated early:** normal survival and development, documented up to adulthood (PMID:18718264).
- **Treated late:** hematological and immune recovery is complete (PMID:19740703: "normalization of anemia, humoral and cellular immunity"), but neurological sequelae may persist: epilepsy, intellectual disability, spasticity (PMID:33146883).
- **Prognostic factors:**
  - Age at starting treatment.
  - Whether CSF 5-MTHF reaches the normal range. PMID:26006721 suggests "CSF levels of 5-methyltetrahydrofolate between 18 and 46 nmol/L may be sufficient to eradicate CNS disease."
  - Adherence.
  - Route of administration (intramuscular is better than oral for CSF levels).
- **Quantitative data:** no QoL or survival statistics exist.

---

## 12. Treatment

| Treatment | Description | NCIT / CHEBI suggestion |
|---|---|---|
| **Parenteral (IM) 5-formyltetrahydrofolate (folinic acid, leucovorin) or levoleucovorin**, the mainstay | High-dose reduced folate restores systemic folate and, at enough dose, CSF 5-MTHF. IM is better than oral for CSF: "intramuscular treatment resulted in higher folate levels in blood" with "normalization of folate levels in cerebrospinal fluid" (PMID:31371121). Daily IM levofolinate stabilized CSF 5-MTHF "within normal range" (PMID:28685492). Patients have been treated "with parenteral 5-formyltetrahydrofolate since infancy" (PMID:18718264). | `treatment_term` NCIT:C15986 Pharmacotherapy (⚠ confirm); `therapeutic_agent` NCIT:C71631 Leucovorin ✔ / CHEBI:748997 ✔ / CHEBI:63606 ✔ (levoleucovorin); `therapeutic_modality: SMALL_MOLECULE` |
| High-dose oral folinic acid | Corrects hematological and immune disease. May not normalize CSF folate, so CSF must be monitored. One secondary source gives oral 10–28 mg/kg/day versus IM 0.5–3 mg/kg/day (⚠ unverified; GeneReviews holds the authoritative dosing). | As above |
| Levofolinic acid vs racemic leucovorin | One case reported "superior clinical and biochemical efficacy" for levofolinic acid (PMID:42809880). | CHEBI:63606 ✔ |
| 5-methyltetrahydrofolate | Proposed as an adjunct in reviews; HFM-specific evidence was not retrieved here. | CHEBI:15641 ✔ |
| **Avoid folic acid** | Neurological signs are "refractory to folic-acid treatment" (PMID:26006721). The proposed reason is competition with 5-MTHF at choroid-plexus FRα. | — |
| Supportive care | Antimicrobials and *Pneumocystis* prophylaxis until immune recovery; transfusions; IVIG where hypogammaglobulinemia is present (management principle, not a trial result); antiseizure medication; nutrition. | NCIT:C15747 Supportive Care ⚠ |
| Rehabilitation | Physical, occupational and speech therapy for children with established neurological deficits. | NCIT:C15315 Rehabilitation ⚠ |

**Monitoring:** serial CSF 5-MTHF to adjust dose (PMID:26006721: serial CSF monitoring was used to guide dosing; PMID:42809880: "Monitoring of CSF 5-MTHF proved essential"). Also blood counts, serum and red-cell folate, homocysteine and immunoglobulins.

**Advanced therapies:** none in development. No gene therapy, cell therapy, RNA therapy or clinical trials were found. HSCT would not address the intestinal and choroid-plexus defect.

**Pharmacogenomics:** PCFT transports antifolates such as pemetrexed and methotrexate (PMID:17340171, 34619546). Patients may therefore handle these drugs differently. This is theoretical only, with no clinical data.

---

## 13. Prevention

- **Primary:** genetic counseling, carrier testing in families and founder populations, and prenatal or preimplantation diagnosis once the familial variants are known.
- **Secondary:** presymptomatic testing of siblings and newborns at risk, with treatment from birth. Targeted newborn screening has been proposed in Puerto Rico (PMID:21489556).
- **Tertiary:** lifelong high-dose reduced-folate therapy with CSF-guided titration, avoidance of folic acid, and infection prophylaxis during the immunodeficient phase.
- **Not applicable:** vaccination, public-health and environmental measures.

---

## 14. Other Species and Natural Disease

- No naturally occurring animal disease was found; OMIA was not searched successfully.
- Orthologs:
  - Mouse *Slc46a1*, NCBI Gene 52466 (seen in a gene-database URL; ⚠ confirm).
  - Rat *Slc46a1*, studied in alcohol-related folate malabsorption (PMID:21861943, 21069807).
  - Chicken PCFT (used for structural studies).
- PCFT-mediated proton-coupled folate uptake is conserved across vertebrates.
- No zoonotic relevance.

---

## 15. Model Organisms

- **Pcft⁻/⁻ mouse** (Salojin et al. 2011, *Blood*, PMID:21346251):
  - Construction: targeted disruption of the first 3 coding exons.
  - Phenotype: by about 4 weeks, "severe macrocytic normochromic anemia and pancytopenia"; erythroblast maturation arrest; and "a systemic folate deficiency caused by disruption of PCFT-mediated intestinal folate uptake".
  - Fidelity: HIGH for the hematological and intestinal-absorption mechanism (RECAPITULATES).
  - Limitations: the abstract reports neither CNS or CSF folate data nor immunodeficiency, and survival and rescue were not stated in the abstract. Use FAILS_TO_RECAPITULATE or UNKNOWN for the cerebral phenotype until checked against the full text.
  - `evidence_source: MODEL_ORGANISM`.
- **In vitro systems:**
  - Transfected HeLa-derived and other PCFT-null cell lines for functional testing of variants (PMID:17446347, 21602279).
  - Patient-derived transformed lymphocytes. PMID:17446347: "Folate transport at low pH was markedly impaired in transformed lymphocytes from 2 patients."
  - Substituted-cysteine accessibility mapping (PMID:20225891).
  - Cell-free expression in nanodiscs (PMID:35773596).
  - Molecular dynamics (PMID:39924111, COMPUTATIONAL).
- **Not found:** iPSC or organoid models; zebrafish, *Drosophila* and nematode models of HFM.
- **Resources:** MGI and IMPC should list *Slc46a1* alleles; not retrieved here.

---

## Key References

| PMID | Citation | Evidence type |
|---|---|---|
| 17129779 | Qiu A et al. *Cell* 2006. Identification of an intestinal folate transporter and the molecular basis for HFM | HUMAN_CLINICAL + IN_VITRO |
| 17446347 | Zhao R et al. *Blood* 2007. Spectrum of mutations in the PCFT gene | HUMAN_CLINICAL + IN_VITRO |
| 18718264 | Min SH et al. *J Pediatr* 2008. A 27-year-old woman with HFM | HUMAN_CLINICAL |
| 19740703 | Borzutzky A et al. *Clin Immunol* 2009. Reversible SCID phenotype | HUMAN_CLINICAL |
| 19074442 | Zhao R et al. *JBC* 2009. PCFT in FR-mediated endocytosis | IN_VITRO |
| 20005757 | Meyer E et al. *Mol Genet Metab* 2010. p.Cys66LeufsX99 | HUMAN_CLINICAL |
| 20795774 | Atabay B et al. *Pediatr Hematol Oncol* 2010. Turkish siblings | HUMAN_CLINICAL |
| 20724482 | Gonen N et al. *JBC* 2010. NRF-1 regulation | IN_VITRO |
| 21333572 | Shin DS et al. *Mol Genet Metab* 2011. Novel mutations | HUMAN_CLINICAL + IN_VITRO |
| 21346251 | Salojin KV et al. *Blood* 2011. Pcft⁻/⁻ mouse | MODEL_ORGANISM |
| 21489556 | Mahadeo KM et al. *J Pediatr* 2011. Puerto Rico founder variant and carrier frequency | HUMAN_CLINICAL |
| 23816405 | Diop-Bove N et al. *Gene* 2013. Nicaraguan deletion | HUMAN_CLINICAL |
| 24512081 | Visentin M et al. *Annu Rev Physiol* 2014. Intestinal absorption of folates | Review |
| 24691418 | Kishimoto K et al. *Clin Immunol* 2014. Immunodeficiency and folate therapy | HUMAN_CLINICAL |
| 25504888 | Erlacher M et al. *Pediatr Blood Cancer* 2015. Reversible pancytopenia | HUMAN_CLINICAL |
| 26006721 | Torres A et al. *JIMD Rep* 2015. Serial CSF 5-MTHF monitoring | HUMAN_CLINICAL |
| 27664775 | Zhao R, Aluri S, Goldman ID. *Mol Aspects Med* 2017. Review | Review |
| 27938595 | Zhang Y et al. *Zhonghua Er Ke Za Zhi* 2016. Intracranial calcification | HUMAN_CLINICAL |
| 28685492 | Manea E et al. *JIMD Rep* 2018. IM levofolinate | HUMAN_CLINICAL |
| 29344585 | Aluri S et al. *Blood Adv* 2018. N411K external-gate variant | HUMAN_CLINICAL + IN_VITRO |
| 31371121 | *Pediatr Neurol* 2020. IM vs oral folinic acid | HUMAN_CLINICAL |
| 31494288 | Tozawa Y et al. *Clin Immunol* 2019. Japanese deep-intronic founder variant | HUMAN_CLINICAL |
| 32893190 | Zhan HQ et al. *JBC* 2020. F392V inward-open lock | IN_VITRO |
| 33146883 | Gowda VK et al. *Indian J Pediatr* 2021. c.620dupG | HUMAN_CLINICAL |
| 35061292 | Hou Z et al. *FASEB J* 2022. Structure and regulation review | Review |
| 35773682 | Sakurai Y et al. *J Med Case Rep* 2022. Pulmonary hemorrhage | HUMAN_CLINICAL |
| 36045837 | Sarhan FMA et al. *Ann Med Surg* 2022. Neonatal neutropenic fever | HUMAN_CLINICAL |
| 39924111 | Nandigrami P et al. *JBC* 2025. Mutation mechanism by MD | COMPUTATIONAL |
| 40937236 | N'joumi C et al. *Cureus* 2025. Siblings, one fatal | HUMAN_CLINICAL |
| 42809880 | Grosso CL et al. *Rev Fac Cienc Med* 2026. Argentina, p.Tyr327Ter | HUMAN_CLINICAL |
| 20301716 | Goldman ID (and co-authors). GeneReviews: Hereditary Folate Malabsorption (NBK1673), revised 2024 | Baseline (not retrieved) |
| 11807405 | Geller J et al. *Medicine (Baltimore)* 2002. Family report and literature review | HUMAN_CLINICAL (no abstract available) |

---

## Next steps before curating the entry

1. **Puerto Rican variant name.** Check the HGVS name against the full text and ClinVar. Borzutzky writes it as "1082-1G>A", while the Mahadeo abstract writes "c.1082G>A".
2. **Villalba carrier frequency.** Check the 6.3% figure against the paper.
3. **Fetch and validate references.** Run `just fetch-reference` on each PMID used, then `just count-verified-snippets` and `just validate-disorders`. GeneReviews (PMID:20301716) must be cited as the phenotype baseline (`just check-genereviews`).
4. **Look up the ⚠ ontology IDs.** Neutropenia, leukopenia, hypogammaglobulinemia, the CSF-folate HPO term, folic acid in CHEBI, the NCIT treatment terms, and the gene and protein IDs all need a lookup. Use `runoak`, OLS, or `just validate-terms`.
5. **Confirm the IM dosing ranges against GeneReviews** before recording any number.

**Web sources consulted:**
- [GeneReviews: HFM (PubMed record)](https://pubmed.ncbi.nlm.nih.gov/20301716/)
- [GeneReviews NBK1673](https://www.ncbi.nlm.nih.gov/books/NBK1673/)
- [MedlinePlus: HFM](https://medlineplus.gov/genetics/condition/hereditary-folate-malabsorption)
- [OMIM #229050](https://www.omim.org/entry/229050)
- [KEGG H01252](https://www.kegg.jp/entry/H01252)
- [GenCC submission](https://thegencc.org/submissions/SGC-180490.1)
- [Physiological Society abstract on PCFT](https://www.physoc.org/abstracts/the-proton-coupled-folate-transporter-pcft-slc46a1-and-hereditary-folate-malabsorption/)
- [Successful treatment with IM folinic acid (PubMed)](https://pubmed.ncbi.nlm.nih.gov/31371121/)
- [Cureus sibling case (PMC12422168)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12422168/)
- [Child Neurology: HFM](https://www.neurology.org/doi/10.1212/WNL.0000000000012083)
- [Puerto Rico prevalence (CienciaPR)](https://www.cienciapr.org/es/prevalence-loss-function-mutation-proton-coupled-folate-transporter-gene-pcft-slc46a1-causing)
- [LOVD SLC46A1/HFM](https://databases.lovd.nl/shared/diseases/01789)
- [Qiu 2006 Cell PDF](https://www.ttuhsc.edu/medicine/cell-physiology-molecular-biophysics/documents/Cell2006.pdf)
- [EBI OLS4 MONDO:0009238](https://www.ebi.ac.uk/ols4/ontologies/mondo/classes?obo_id=MONDO:0009238)
- [Europe PMC REST API](https://www.ebi.ac.uk/europepmc/webservices/rest/)
- [NCBI E-utilities](https://eutils.ncbi.nlm.nih.gov/)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 40 |
| Resolved | 40 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 11 |
| Quoted claims found in source | 10 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 40 |
| On topic | 37 |
| Off topic | 1 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:28687492` *(abstract only)*: "Newborns with this condition have initially normal folate stores"
  - Text part not found as substring: 'Newborns with this condition have initially normal folate stores' (note: only abstract available for PMID:28687492, full text may contain this excerpt)

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:28687492` (1 mention) - Molecular characterization of the hydroxylase HmtN at 1.3 Å resolution.
  - shared terms: acid

Weighed against this report's own most characteristic terms: `folate`, `pcft`, `variant`, `disease`, `acid`, `hfm`, `csf`, `treatment`, `slc46a1`, `gene`, `transport`, `carrier`, `infection`, `oral`, `mthf`, `puerto`, `cell`, `folic`, `immune`, `immunodeficiency`.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 67 |
| Resolved | 64 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 2 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0009238` (5 mentions) - the report calls it "MONDO"; MONDO calls it **hereditary folate malabsorption**
- `DOID:0111678` (1 mention) - the report calls it "DOID"; DOID calls it **hereditary folate malabsorption**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `Orphanet`, `ORPHA`.