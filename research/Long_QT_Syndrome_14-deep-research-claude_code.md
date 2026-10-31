---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-15T20:02:11.178904'
end_time: '2026-10-15T20:03:47.150656'
duration_seconds: 95.97
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Long QT Syndrome 14
  mondo_id: MONDO:0014548
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
  - claude-sonnet-5-5
  web_search_requests: 3
  num_turns: 7
  total_cost_usd: 0.8321412000000001
  session_id: 1411d6e0-a3a9-57ef-a642-a756ff0785bd
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 7
reference_validation:
  total_references: 3
  verified: 3
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 0
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMC:PMC6748747
  relevance_assessed: 3
  on_topic: 3
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 13
  verified: 13
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 0
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0014548
    reported_labels:
    - MONDO
    ontology_label: long QT syndrome 14
  - term_id: DOID:0110655
    reported_labels:
    - Disease Ontology
    ontology_label: long QT syndrome 14
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Long QT Syndrome 14
- **MONDO ID:** MONDO:0014548 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Long QT Syndrome 14** covering all of the
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

# Research Report: Long QT Syndrome 14 (LQT14; CALM1-related long QT syndrome)

**Provenance and limits.** I could check some of this report directly. Other parts are my own background knowledge and are marked **[unverified]**.
- **Checked this session:**
  - The OMIM #616247 and MONDO:0014548 summaries, from search results.
  - The abstract and text of the International Calmodulinopathy Registry paper (Crotti 2019, PMC6748747). I read about the first 100,000 of its 114,926 characters.
- **Not checked:** PMIDs. I did not confirm any of them in this session, so check each one with `just fetch-reference` before it goes into the KB. I did not re-read any other paper this session.
- **Not read:** PMC4907364 (Boczek 2016) hit a CAPTCHA, so I know it only from search-result summaries.
- **Not looked up:** ontology CURIEs for HP, GO, CL, UBERON, NCIT and CHEBI. The CURIEs below come from memory, so look each one up before binding it.

---

## 1. Disease information

**Overview.** LQT14 is the form of long QT syndrome caused by heterozygous pathogenic variants in **CALM1**, which encodes calmodulin. CALM1 is one of three genes (CALM1, CALM2, CALM3) that encode an identical calmodulin protein.
- OMIM describes LQT14 as a cardiac arrhythmia disorder "characterized by ventricular arrhythmias, often life-threatening, occurring very early in life". It features T-wave alternans, markedly prolonged QTc and intermittent 2:1 AV block.
- The index case was an infant with ventricular fibrillation at 6 months.
- OMIM notes a more severe course than other LQTS genotypes: earlier onset, more profound QT prolongation, and a high predilection for cardiac arrest and sudden death. (Source: [OMIM #616247 mirror](https://https.ncbi.nlm.nih.gov/omim/616247).)

**Identifiers.**

| System | ID | Status |
|---|---|---|
| MONDO | MONDO:0014548 | Confirmed by search. Defined as a long QT syndrome caused by a CALM1 mutation, and sits under familial long QT syndrome ([PomBase term page](https://www.pombase.org/term/MONDO:0014548)). |
| OMIM | #616247 | Confirmed |
| UMLS | C4015671 | Confirmed |
| MedGen | 864108 | Confirmed |
| Disease Ontology | DOID:0110655 | Confirmed ([DO](https://disease-ontology.org/term/DOID:0110655)) |
| OMIM gene | 114180 (CALM1) | Confirmed |
| Orphanet | not found | **[unverified]** |
| ICD-10/ICD-11 | not found | **[unverified]**; expect the generic long QT code (I45.81 / LA... family) |

**Synonyms.** LQT14, CALM1 long QT syndrome, calmodulin-1-related LQTS, CALM1-LQTS. The wider group is "calmodulinopathy".

**Information source.** This is aggregated disease-level data from registries and case series, not EHR-derived. The key resource is the International Calmodulinopathy Registry (ICalmR).

**Sibling entries.** LQT15 is CALM2, and LQT16 is CALM3 (OMIM numbers 616249 and 618782, **[unverified]**). Many studies pool all three, so check which gene each statistic applies to before attributing it to CALM1.

---

## 2. Etiology

**Causal factors.** The cause is genetic: a heterozygous missense variant in CALM1. These are usually *de novo*, though some families show transmission (see §9).

**Risk and modifier factors.**
- The arrhythmias are adrenergically triggered. The registry authors call calmodulinopathies "mainly adrenergically triggered, life-threatening arrhythmias" (Crotti 2019, [PMC6748747](https://pmc.ncbi.nlm.nih.gov/articles/PMC6748747)).
- Fever, medicines that prolong QT, and electrolyte disturbance would be expected modifiers. I found no calmodulin-specific data on them **[unverified]**.

**Protective factors.** None established.

**Gene-environment interactions.** Not established beyond the adrenergic trigger. Do not infer any others.

---

## 3. Phenotypes

Registry data (Crotti 2019) cover CALM1–3 together, with 74 subjects: 36 CALM1, 23 CALM2 and 15 CALM3. Quotes are from the paper's abstract and text.

| Phenotype | Registry finding | HPO (look up first) |
|---|---|---|
| Prolonged QTc | CALM-LQTS QTc 594 ± 73 ms. Perinatal CALM-LQTS 628 ± 62 ms. | HP:0001657 Prolonged QT interval |
| Life-threatening arrhythmia / cardiac arrest | 78% of CALM-LQTS patients, median onset 1.5 years. | HP:0001279 Syncope; HP:0001645 Sudden cardiac death; ventricular tachycardia, ventricular fibrillation |
| T-wave alternans | OMIM; the index case had frequent episodes. | HP:0031546? **[unverified]** |
| 2:1 AV block | OMIM; intermittent. | HP:0011705? **[unverified]** |
| Late-onset peaked T waves | Seen on most CALM-LQTS ECGs. | (find the matching HPO term) |
| Neurological impairment | 13 subjects overall. 10 had LQTS and 9 had a CALM1 variant. Seven had deficits after cardiac arrest, probably anoxic, and six of those improved. The other six had intellectual disability, developmental delay, recurrent seizures or autism, unrelated to arrest. | HP:0001249 Intellectual disability; HP:0001250 Seizure; HP:0001263 Global developmental delay |
| Structural cardiac abnormality | 18 patients (all genes pooled). | Not specified in the text I read |

**Onset, severity, course.** Onset is in infancy to early childhood. It is severe, and it is episodic and adrenergically triggered. Frequency figures for individual features in CALM1-only patients were not given in the part of the paper I read.

**Quality of life.** No data found.

**Variants and phenotype (from the registry).**
- p.Asp130Gly (D130G) and p.Phe142Leu (F142L) were "always associated with LQTS".
- p.Asn98Ser (N98S) is a hot spot with variable phenotypes: LQTS, CPVT, idiopathic VF and sudden unexplained death.
- The text did not assign N98S to a specific gene.

---

## 4. Genetic and molecular information

- **Gene:** CALM1 (HGNC symbol, 14q32; OMIM 114180). Look up the HGNC ID and write it in the lowercase `hgnc:` form the KB uses. I have not looked it up, so I am not quoting a number.
- **Variants.**
  - Index report: Crotti et al. 2013, *Circulation* (**[unverified]** PMID; the registry paper shows this is where the first CALM1 cases appeared).
  - A later cohort: Boczek et al. 2016, which screened 39 genetically elusive LQTS cases. Non-synonymous calmodulin variants were found in 15.4% of them, against 0.04% in ExAC (p<0.0001). It also characterized a novel missense variant, **E141G**. Search-result summaries only; the PMC page was blocked ([PMC4907364](https://pmc.ncbi.nlm.nih.gov/articles/PMC4907364)).
  - Variants named in the registry text: D130G, F142L, N98S. Other recurrent variants such as D96V, D132E and D134H are unconfirmed here **[unverified]**.
- **Classification and gene validity.**
  - PanelApp England rates CALM1 green for LQTS and definitive for CPVT; Australian PanelApp lists penetrance as unknown.
  - The KB rule is to copy ClinGen tiers from the cached `CGGV:` record and never assign one. I did not find the ClinGen record in this session. Run `just check-gene-validity` after adding it.
- **Variant class and consequence.** All reported variants are missense changes clustered in the calcium-binding EF-hand loops. The functional consequence is **reduced Ca²⁺ affinity**, and effects on CaV1.2 (L-type calcium channel), RyR2 and NaV1.5 follow from it. In the KB this is a pathophysiology-level statement. Whether to tag each variant as a dominant-negative effect is not settled by the sources I read.
- **Origin:** germline, usually *de novo* **[unverified]**.
- **Modifier genes, epigenetics, chromosomal abnormalities:** none known.

---

## 5. Environmental information

No specific exposures are established. Adrenergic stress (exercise, emotion, startle) is the only recognized trigger, supported by the registry authors' conclusion above. No infectious agents are involved.

---

## 6. Mechanism / pathophysiology

**Causal chain.**
1. A heterozygous missense variant in one CALM1 allele alters an EF-hand calcium-binding loop (demonstrated for the variants studied: "reduce CaM affinity to Ca²⁺" per the Boczek 2016 summary).
2. Because calmodulin from the mutant allele coexists with wild-type protein, its binding partners receive a mixed pool. Mutant calmodulin therefore impairs the regulation of CaV1.2 (inferred from the summary of Boczek 2016; detail not checked).
3. Impaired calcium-dependent inactivation of the L-type calcium channel gives a larger, longer inward calcium current in the cardiomyocyte action potential (inferred from CaV1.2 data; not checked here).
4. That slows repolarization and prolongs the QT interval, producing the very long QTc seen on ECG (QTc 594 ± 73 ms in CALM-LQTS).
5. Under adrenergic stimulation, the prolonged repolarization leads to early afterdepolarizations, then torsades de pointes or ventricular fibrillation (step inferred, not demonstrated in the sources I read).
6. Cardiac arrest follows, usually in the first years of life (78% life-threatening arrhythmias, median onset 1.5 years).
7. A branch: hypoxic-ischemic injury after arrest explains some neurological deficits (7 of 13 patients). The other six had features unrelated to arrest, so a direct brain effect of calmodulin dysfunction is possible but unproven.

**Open points.**
- RyR2 and NaV1.5 effects (per the Boczek summary) probably explain the overlap with CPVT in some variants. I could not check how much each contributes to LQT14 specifically.
- The registry authors used patient iPSC-derived cardiomyocytes with F142L. That is a model system, not human tissue.

**Suggested ontology terms** (look up before binding). GO: regulation of calcium ion-transport/ L-type calcium channel activity, calcium ion binding, cardiac muscle cell action potential. CL: cardiac muscle cell (ventricular cardiomyocyte). Cellular component: sarcolemma, sarcoplasmic reticulum.

**Omics, single-cell, spatial, CRISPR screens:** none found.

---

## 7. Anatomical structures

- Heart, mainly the ventricular myocardium and the conduction system (AV node block).
- Brain, secondarily (neurological deficits).
- UBERON terms: heart, cardiac ventricle. Look these up.
- Distribution is bilateral. No lateralization is reported.

---

## 8. Temporal development

- Onset is perinatal or in infancy. Perinatal cases have the longest QTc (628 ± 62 ms).
- The course is lifelong. Events are triggered and recurrent.
- No remission pattern is described. The critical period is the first years of life.
- Registry 10-year cumulative mortality is **27%** (all three genes pooled).

---

## 9. Inheritance and population

- **Inheritance:** autosomal dominant. The HPO term is HP:0000006; look it up first.
- **Penetrance and expressivity:** PanelApp England records complete penetrance, but the Australian panel lists it as unknown. The registry shows variable phenotypes for a single variant (N98S), so expressivity is variable. Do not enter a single penetrance figure.
- **Germline mosaicism, founder effects, consanguinity, carrier frequency, geographic and sex distribution:** not found. Do not enter any of these.
- **Prevalence / incidence:** not found. Calmodulinopathy is described as "rare". Use `prevalence_class` `NOT_YET_DOCUMENTED` only if a source supports it; otherwise leave it out.

---

## 10. Diagnostics

- **ECG:** markedly prolonged QTc, T-wave alternans, 2:1 AV block, late-onset peaked T waves. The CALM-CPVT pattern includes prominent U waves.
- **Genetic testing:** include CALM1, CALM2 and CALM3 in LQTS/CPVT panels. Boczek 2016 found calmodulin variants in 15.4% of genetically elusive LQTS cases, which supports adding them to panels. Panel, exome and genome yields: no specific figures found.
- **Differential diagnosis:** other LQTS genes (KCNQ1, KCNH2, SCN5A), CPVT, and idiopathic VF. The registry notes that LQTS and CPVT features overlap.
- **Screening:** cascade testing in relatives. Specific guidance was not retrieved.
- **LOINC codes:** none verified. The KB rule is to seed them with `just loinc-seed-cache`.

---

## 11. Outcome / prognosis

- 10-year cumulative mortality is 27%. 86.5% of registry subjects were symptomatic.
- Registry authors: "Available therapies are disquietingly insufficient, especially in CALM-LQTS."
- Neurological sequelae affected 13 of 74. Seven were probably anoxic, and six of these improved.
- **Prognostic factors:** perinatal presentation with the longest QTc is the most severe group. No validated risk score exists.

---

## 12. Treatment

All figures below come from Crotti 2019 and pool CALM1–3.

| Treatment | Finding |
|---|---|
| Beta-blockers | Used in 54/69 (78%). Breakthrough events in 56% of those on them. |
| Sodium channel blockers (mexiletine, flecainide, ranolazine) | Used in 21 patients (30%). Mexiletine suppressed arrhythmias in 4 of 11 CALM-LQTS patients (36%). |
| Left cardiac sympathetic denervation (LCSD) | 4 patients. Arrhythmias recurred in all 3 CALM-LQTS patients with follow-up. |
| ICD | 25 patients. Pacemakers: 7. |
| Other | Verapamil in 3 patients, nicorandil in 1. |

- The authors recommend considering combination drug therapy, sympathectomy and devices.
- **Suggested NCIT terms** (look up first): Pharmacotherapy (NCIT:C15986, from the KB guidance), Surgical Procedure (NCIT:C15329). Agents: propranolol / nadolol and mexiletine, via CHEBI or NCIT.
- **Not found:** gene therapy, RNA-based therapy and clinical-trial data for CALM1. Genotype-guided therapy and pharmacogenomics are not covered by the sources I read. Do not add any.

---

## 13. Prevention

- Cascade genetic testing and genetic counseling for families.
- Avoid QT-prolonging drugs (general LQTS practice **[unverified]** for this subtype).
- No primary prevention exists. No vaccine applies.
- Prenatal and preimplantation testing: no specific data.

---

## 14. Other species / natural disease

Not researched. Calmodulin is highly conserved across species, but I found no OMIA entry or naturally occurring animal disease for it.

---

## 15. Model organisms

- **Human iPSC-derived cardiomyocytes** carrying F142L were used in the registry paper. Evidence type: IN_VITRO.
- Mouse, zebrafish and other animal models were not researched here. Do not list any until checked.

---

## Suggested next steps for curation

1. Confirm the PMIDs for Crotti 2013, Crotti 2019 (DOI 10.1093/eurheartj/ehz311) and Boczek 2016 with `just fetch-reference`.
2. Read the rest of PMC6748747, the final ~15,000 characters I did not read.
3. Search for CALM1-only data. Almost all the numbers above pool the three genes.
4. Look up every HP, GO, CL, UBERON, NCIT and CHEBI CURIE before binding it.
5. Check the ClinGen gene-disease validity record for CALM1 and LQTS.

## Sources
- [OMIM #616247 (mirror)](https://https.ncbi.nlm.nih.gov/omim/616247)
- [MONDO:0014548 on PomBase](https://www.pombase.org/term/MONDO:0014548)
- [Disease Ontology DOID:0110655](https://disease-ontology.org/term/DOID:0110655)
- [Crotti et al. 2019, International Calmodulinopathy Registry (PMC6748747)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6748747)
- [Boczek et al. 2016 (PMC4907364; summary only)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4907364)
- [Genomics England PanelApp, CALM1](https://panelapp.genomicsengland.co.uk/panels/76/gene/CALM1/)
- [PanelApp Australia, CALM1](https://panelapp-aus.org/panels/131/gene/CALM1/)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 3 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 3 |
| On topic | 3 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMC:PMC6748747`: "mainly adrenergically triggered, life-threatening arrhythmias"
  - closest text in source: "CONCLUSION: Calmodulinopathies are largely characterized by adrenergically-induced life-threatening arrhythmias"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 2 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014548` (6 mentions) - the report calls it "MONDO"; MONDO calls it **long QT syndrome 14**
- `DOID:0110655` (5 mentions) - the report calls it "Disease Ontology"; DOID calls it **long QT syndrome 14**