---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-04T13:05:15.211096'
end_time: '2026-09-04T13:11:24.854307'
duration_seconds: 369.64
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Immunodeficiency 15A
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
  web_search_requests: 15
  num_turns: 33
  total_cost_usd: 1.7170025999999996
  session_id: eaf6e7f6-c363-56c8-b267-6f60c89fc92d
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 3
reference_validation:
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 8
  on_topic: 5
  off_topic: 1
  off_topic_references:
  - PMID:10229185
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 41
  verified: 38
  not_found: 0
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 23
  labels_matching: 14
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: HP:0010976
    reported_labels:
    - Documented in functional assays
    ontology_label: Decreased total B cell count
  - term_id: HP:0002164
    reported_labels:
    - Rare/variable
    ontology_label: Nail dysplasia
  - term_id: HP:0001878
    reported_labels:
    - AIHA
    ontology_label: Hemolytic anemia
  - term_id: GO:0002741
    reported_labels:
    - positive regulation of cytokine secretion involved in immune response
    ontology_label: GO_0002741
  labels_variant: 5
  obsolete_terms:
  - term_id: GO:0002741
    ontology_label: GO_0002741
    replaced_by: GO:0002720
  unresolvable_prefixes:
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Immunodeficiency 15A
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Immunodeficiency 15A** covering all of the
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

Now I have sufficient primary-literature detail to compile the report.

I now have sufficient primary literature to compile the comprehensive report.

---

# Immunodeficiency 15A (IMD15A) — Comprehensive Research Report

## 1. Disease Information

**Overview.** Immunodeficiency 15A (IMD15A) is an ultra-rare, autosomal dominant inborn error of immunity caused by heterozygous, typically *de novo*, **gain-of-function (GOF)** missense variants in **IKBKB** (encoding IKKβ/IKK2, a core catalytic subunit of the IκB kinase complex that activates canonical NF-κB signaling). It was first delineated as a distinct clinical entity by Cardinez et al. (2018), who identified an identical heterozygous de novo *IKBKB* c.607G>A (p.Val203Ile) missense mutation in two unrelated kindreds presenting with immune dysregulation, combined T- and B-cell functional deficiency, systemic inflammation, and epithelial defects (PMID:30337470, *J Exp Med* 2018). Unlike classic combined immunodeficiencies, IMD15A is characterized by **relatively late onset** (childhood to adulthood), recurrent respiratory infections, progressive lymphopenia, and paradoxical immune activation/dysregulation despite (or because of) enhanced NF-κB signaling.

**Key identifiers:**
- **OMIM phenotype:** #618204 — IMMUNODEFICIENCY 15A; IMD15A
- **OMIM gene:** *603258 — IKBKB (Inhibitor of Nuclear Factor Kappa B Kinase Subunit Beta)
- **MONDO:** MONDO:0032599
- **Gene:** IKBKB, HGNC:5960, NCBI Gene ID 3551, chromosome 8p11.21 (chr8:42,271,302–42,332,460, GRCh38)
- **Inheritance:** Autosomal dominant (heterozygous, gain-of-function)
- **Related/contrasted entity:** Immunodeficiency 15B (IMD15B; OMIM #615592) — the **autosomal recessive**, biallelic **loss-of-function** IKBKB disorder (severe combined immunodeficiency with normal lymphocyte counts but impaired signaling; Pannicke et al. 2013, *N Engl J Med*, PMID:24369075)
- **Synonyms:** IKBKB gain-of-function immunodeficiency; IKK2 gain-of-function disease; IKBKB-related combined immune deficiency (autosomal dominant)

**Data provenance.** Nearly all current knowledge derives from aggregated case reports/small case series (individual-patient, family-based whole-exome sequencing studies) rather than large disease registries — consistent with an ultra-rare monogenic condition first described in 2018 and still comprising well under 50 published patients worldwide as of the most recent 2025 series.

## 2. Etiology

**Disease causal factor:** Purely genetic/monogenic. Heterozygous missense variants in the kinase or activation-loop domains of *IKBKB* that confer **gain of function** on IKK2 kinase activity, producing constitutive/enhanced canonical NF-κB pathway signaling.

**Genetic risk factors:**
- The prototypic variant is **c.607G>A, p.Val203Ile (V203I)**, located in the second lobe of the kinase domain active site (Cardinez et al. 2018, PMID:30337470). V203 is highly conserved; the mutant protein retains kinase activity but is predicted to adopt an unstable conformation that disrupts normal tetrameric IKK-complex interactions, producing constitutive activity.
- A second locus, the **activation-loop** region, was implicated by Abbott et al. (2021, *J Allergy Clin Immunol*, PMID:32554083), describing a heterozygous IKKβ activation-loop mutation causing a complex immunodeficiency syndrome.
- A 2025 multi-family series (Körholz et al., *J Allergy Clin Immunol*, PMID:40403933) reported **16 patients from 4 families** carrying missense variants clustered in the *IKBKB* kinase domain, including one novel GOF variant, establishing that the phenotype spans a spectrum broader than the original V203I report.
- All reported IMD15A variants to date arise **de novo** or segregate as autosomal dominant within affected kindreds; no common population polymorphism reproduces the phenotype (variant is absent/near-absent from gnomAD).
- A separate, mechanistically distinct pair of compound-heterozygous *IKBKB* variants (E518K/T559M, in *trans*) was reported by a 2022 case (PMID:36378426, *J Clin Immunol*) causing an autoinflammatory/autoimmune phenotype (recurrent fever, autoimmune hemolytic anemia, Sweet-syndrome-like skin lesions) rather than classical IMD15A — illustrating that different *IKBKB* GOF alleles produce a phenotypic continuum from autoinflammation to combined immunodeficiency.

**Modifier considerations:** No modifier genes have been established; phenotypic severity appears to depend on which residue is altered and the degree/duration of NF-κB hyperactivation, with clinical heterogeneity documented even within families carrying the identical variant (age of onset in the 2025 series ranged from infancy — mild nail dysplasia — to 48 years — severe CMV colitis).

**Environmental/risk-modifying factors:** None specifically established; as an intrinsic immune-signaling disorder, disease expression is likely modulated by cumulative pathogen exposure (viral, bacterial) over the patient's lifetime, consistent with the age-dependent progression documented in longitudinal series.

**Protective factors:** None reported in the literature to date.

**Gene-environment interactions:** Not formally studied; the progressive, age-related worsening of lymphopenia and hypogammaglobulinemia suggests a "second-hit" or cumulative-exposure model in which repeated antigen/pathogen encounters exhaust the dysregulated NF-κB-dependent lymphocyte activation/homeostasis machinery, but this remains inferential rather than directly demonstrated (PMID:40403933).

## 3. Phenotypes

Suggested **HP terms** are given per phenotype.

| Phenotype | Type | Onset/course | Frequency (qualitative) | HPO term |
|---|---|---|---|---|
| Recurrent sinopulmonary/respiratory infections | Symptom/sign | Childhood–adulthood; progressive | Common (majority of patients) | HP:0002205 (Recurrent respiratory infections) |
| Progressive lymphopenia | Laboratory abnormality | Emerges/worsens with age; normal in youth, reduced in adults | Frequent, age-dependent | HP:0001888 (Lymphopenia) |
| Reduced/dysfunctional CD8+ and CD4+ T cells | Laboratory abnormality | Progressive | Frequent | HP:0005415 (Decreased circulating total T cell count); HP:0032155 |
| Hypogammaglobulinemia / impaired specific-antibody responses | Laboratory abnormality | Progressive, adult-onset in milder cases | Frequent | HP:0002850 (Decreased circulating antibody level); HP:0002846 |
| Impaired B-cell differentiation into plasmablasts | Laboratory abnormality | Progressive | Documented in functional assays | HP:0010976 |
| Autoinflammatory skin manifestations (rash, abscesses, Sweet-syndrome-like plaques) | Clinical sign | Variable onset, can be earliest feature (infancy) | Variable | HP:0100785 (Recurrent skin infections); HP:0031372 |
| Nail dysplasia | Physical manifestation | Can present in first year of life | Rare/variable | HP:0002164 |
| Bronchiectasis | Clinical sign (complication) | Adult-onset, complication of recurrent infection | Reported in a subset | HP:0002110 |
| Splenomegaly | Physical sign | Variable | Reported in a subset | HP:0001744 |
| Cataracts | Physical sign | Variable | Reported in a subset | HP:0000518 |
| Hypodontia | Physical manifestation | Congenital/developmental | Reported in a subset | HP:0000668 |
| Recurrent cutaneous abscesses | Clinical sign | Variable | Reported in a subset | HP:0031292 |
| Autoimmune cytopenias (e.g., autoimmune hemolytic anemia) — seen in the related E518K/T559M phenotype | Clinical sign/lab | Infancy onset in that case | Case-specific | HP:0001878 (AIHA) |
| Severe/opportunistic infections (e.g., CMV colitis) in adulthood | Symptom | Adult-onset, can be severe | Reported | HP:0032101 |
| Epithelial defects | Physical manifestation | Variable | Reported (original 2018 description) | — |

**Quality-of-life impact:** No formal EQ-5D/SF-36 data exist for this ultra-rare condition. Qualitatively, disease burden accumulates with age — patients described as asymptomatic or mildly affected in childhood (e.g., isolated nail dysplasia, mild upper respiratory infections) can progress in adulthood to bronchiectasis, severe/opportunistic infection (CMV colitis), and clinically significant lymphopenia/hypogammaglobulinemia requiring immunoglobulin replacement (PMID:40403933), consistent with a progressive, life-course disease trajectory rather than a static congenital immunodeficiency.

## 4. Genetic/Molecular Information

**Causal gene:** IKBKB (HGNC:5960; OMIM *603258; NCBI Gene 3551; UniProt O14920).

**Reported pathogenic variants (heterozygous, gain-of-function):**
- **c.607G>A (p.Val203Ile)** — the founding IMD15A variant, kinase-domain active site, second lobe (Cardinez et al. 2018, PMID:30337470). Predicted to destabilize the normal tetrameric IKK holo-complex interaction while preserving/enhancing catalytic activity.
- **Activation-loop missense variant(s)** — Abbott et al. 2021 (PMID:32554083).
- Additional kinase-domain missense variants, including at least one novel GOF allele, reported across 4 families/16 patients (Körholz et al. 2025, PMID:40403933).
- **E518K / T559M in *trans*** — a distinct compound-heterozygous GOF genotype (between the leucine-zipper and NEMO-binding domains) producing an autoinflammatory/autoimmune-predominant phenotype rather than classic IMD15A (PMID:36378426); T559M was functionally validated as gain-of-function (≈1.5-fold increase in NF-κB luciferase reporter activity in Jurkat cells; increased basal IKKα/β and p65 phosphorylation), while E518K alone showed wild-type-like signaling.

**Variant classification (ACMG/AMP framework, as applied in the primary reports):** Pathogenic/likely pathogenic on the basis of de novo occurrence, functional (kinase activity, NF-κB reporter, phospho-flow) validation, and — for V203I — an orthologous CRISPR/Cas9 knock-in mouse model that reproduced the human immune-cellular and biochemical phenotype (PMID:30337470).

**Population frequency:** The causal missense alleles are absent or present only at extremely low frequency in gnomAD (e.g., the unrelated E518K/T559M alleles carried population minor allele frequencies of 8.43×10⁻⁶ and 5.24×10⁻⁵ respectively, per PMID:36378426), consistent with strong purifying selection against IKBKB coding variation generally.

**Functional consequence:** Gain of function — enhanced/constitutive IKK2 kinase activity, increased basal and stimulus-induced phosphorylation of IκBα and p65/RelA, and increased NF-κB transcriptional reporter activity, contrasted with the biallelic **loss-of-function** mechanism of IMD15B (complete absence of IKK2 protein; Pannicke et al. 2013, PMID:24369075).

**Somatic vs. germline:** All reported variants are germline (constitutional), heterozygous, and largely de novo; some kindreds show vertical (autosomal dominant) transmission with variable expressivity.

**Modifier genes:** None established.

**Chromosomal abnormalities:** None reported; IMD15A is a single-gene, missense-variant disorder, not a copy-number or structural chromosomal condition.

**Epigenetics:** No disease-specific epigenetic (DNA methylation/chromatin) studies have been published for IMD15A.

**Gene/protein structure relevant to mechanism:** IKBKB (chr8p11.21) encodes IKKβ/IKK2, a serine/threonine kinase and the principal catalytic subunit of the canonical IKK complex, together with IKKα (CHUK) and the regulatory scaffold IKKγ (NEMO/IKBKG). IKK2 contains an N-terminal kinase domain (site of the V203I and activation-loop mutations), a ubiquitin-like domain, a scaffold/dimerization (leucine-zipper) domain, and a C-terminal NEMO-binding domain (site of the E518K/T559M variants).

## 5. Environmental Information

No specific environmental toxin, occupational exposure, or lifestyle factor has been implicated as causal. As with other combined immunodeficiencies, standard childhood/community pathogen exposures (respiratory viruses, encapsulated bacteria, CMV) are the proximate triggers of the clinical infectious phenotype rather than disease causes. No infectious agent is causal to the underlying genetic lesion; CMV colitis has been reported as a severe complication in an affected adult, reflecting acquired opportunistic infection secondary to the immunodeficiency rather than an etiological agent (Körholz et al. 2025, PMID:40403933).

## 6. Mechanism / Pathophysiology

**Causal chain (ordered, from molecular lesion to clinical manifestation):**

1. A heterozygous *IKBKB* missense variant (e.g., V203I in the kinase domain, or an activation-loop/NEMO-binding-domain variant) **alters IKKβ protein conformation**, producing a kinase that is catalytically hyperactive or constitutively active while destabilizing normal IKK holo-complex tetramerization (demonstrated: PMID:30337470).
2. This **leads to** enhanced basal and stimulus-induced phosphorylation of IκBα (and of p65/RelA) by the mutant IKK complex (demonstrated in patient PBMCs and Jurkat reporter assays: PMID:30337470, PMID:36378426).
3. Increased IκBα phosphorylation **results in** accelerated IκBα ubiquitination/proteasomal degradation, releasing NF-κB dimers (p65/p50) from cytoplasmic sequestration (established canonical NF-κB biology, applied here as the disease mechanism).
4. Liberated NF-κB **leads to** constitutive/exaggerated nuclear translocation and transcription of NF-κB target genes governing lymphocyte activation, survival, and inflammatory cytokine/chemokine production (elevated MCP-1, MDC, MIP-1α/β, IL-18, IL-16, S100A8 reported in patient serum/PBMC supernatant: PMID:36378426) — **this step is directly demonstrated** by patient biomarker and mouse-model data.
5. Chronic/dysregulated NF-κB signaling in developing and mature lymphocytes **causes** defective T-cell receptor– and B-cell receptor–dependent activation (impaired CD70, CD25, CD40L induction at day 3 of stimulation) and **impaired B-cell differentiation into plasmablasts** despite preserved proliferative capacity (demonstrated functionally: PMID:40403933) — an apparent paradox in which pathway *hyperactivation* produces *functional lymphocyte hypofunction*, likely reflecting exhaustion of negative-feedback capacity (IκBα resynthesis) and/or activation-induced dysregulation rather than simple loss of signal. This link is **partly inferred**: the downstream mechanistic step from "chronic NF-κB activation" to "functional T/B-cell defect" is documented phenomenologically (the defect is measured) but its precise molecular route (e.g., activation-induced cell death, receptor desensitization, altered thymic/germinal-center selection) is not yet fully resolved in humans.
6. Over time, this signaling dysregulation **leads to** progressive peripheral lymphopenia (both T and B lineages) and impaired specific-antibody production/hypogammaglobulinemia, worsening from childhood into adulthood (longitudinal pattern documented: PMID:40403933) — a step that is **observed clinically** but whose cellular kinetics (rate of lymphocyte loss, compartment first affected) remain incompletely characterized.
7. The combined **T-cell functional deficiency + progressive antibody deficiency** **results in** recurrent sinopulmonary infections, susceptibility to opportunistic pathogens (e.g., CMV colitis in adulthood), and structural airway complications such as bronchiectasis (clinical endpoint, directly observed).
8. In parallel, and to some degree independently, chronic NF-κB-driven **inflammatory cytokine/chemokine production leads to** the autoinflammatory cutaneous phenotype (recurrent rash, cutaneous abscesses, Sweet-syndrome-like plaques) and, in variant-specific cases, organ-specific autoimmunity (e.g., autoimmune hemolytic anemia in the E518K/T559M case) — this **branch** of the causal chain diverges from the classic infection-predominant IMD15A course and appears to depend on which residue/domain is mutated (kinase active site vs. NEMO-binding region) (PMID:36378426).
9. The murine V203I knock-in model **recapitulates** reduced peripheral CD3+ T-cell percentage and abnormal splenocyte IκBα phosphorylation/degradation kinetics at baseline and after ex vivo activation, cross-validating that the human phenotype derives directly from the mutant kinase's biochemical behavior rather than from a confounding second variant (PMID:30337470) — this is **model-organism-demonstrated**, supporting but not itself proving each downstream human clinical step.

**Molecular pathways:** Canonical (classical) NF-κB signaling pathway — TNF-receptor/Toll-like-receptor/antigen-receptor-proximal signals → IKK complex (IKKα/IKKβ/NEMO) → IκBα phosphorylation/degradation → NF-κB (RelA/p50) nuclear translocation → transcription of pro-survival, pro-inflammatory, and lymphocyte-activation genes. (KEGG: NF-kappa B signaling pathway, hsa04064; Reactome: R-HSA-975138 TAK1-dependent IKK and NF-kappa-B activation; R-HSA-5602636 IKBKB deficiency causes SCID — the Reactome annotation for the *loss-of-function* IMD15B mechanism, useful as a contrasting pathway diagram.)

**Cellular processes:** Aberrant lymphocyte activation signaling; impaired T-cell receptor– and B-cell receptor–induced activation marker upregulation; defective plasmablast differentiation; likely dysregulated apoptosis/activation-induced cell death balance in lymphocytes (inferred from the paradox of hyperactive signaling causing functional lymphopenia, not yet directly measured for apoptotic rate in human IMD15A).

**Protein dysfunction:** Gain-of-function conformational/kinetic alteration of IKKβ — retained or enhanced catalytic activity combined with disrupted normal holo-complex assembly (V203I: disrupted tetrameric interaction; predicted loss of an inter-chain hydrogen bond for T559M).

**Immune system involvement:** Central and defining — this is a primary immune-signaling disorder combining features of combined immunodeficiency (T/B lymphopenia, hypogammaglobulinemia, infection susceptibility) with immune dysregulation/autoinflammation (cytokine/chemokine excess, autoimmune cytopenias in variant-specific presentations).

**Suggested GO terms:** GO:0007249 (I-kappaB kinase/NF-kappaB signaling), GO:0043123 (positive regulation of I-kappaB kinase/NF-kappaB signaling), GO:0002741 (positive regulation of cytokine secretion involved in immune response), GO:0042104 (positive regulation of activated T cell proliferation — for contrast/negative regulation defects), GO:0002322 (B cell proliferation involved in immune response).

**Suggested CL terms:** CL:0000084 (T cell), CL:0000798 (gamma-delta T cell), CL:0000236 (B cell), CL:0000980 (plasmablast), CL:0000625 (CD8-positive, alpha-beta T cell), CL:0000624 (CD4-positive, alpha-beta T cell).

**Molecular profiling:** No transcriptomic, proteomic, or single-cell datasets specific to human IMD15A patients are publicly deposited to date (searched GEO/ArrayExpress equivalents — not identified in available literature). Targeted biomarker panels (serum chemokine/cytokine profiling) have been used in individual case reports (PMID:36378426) rather than unbiased omics.

## 7. Anatomical Structures Affected

**Organ level:**
- Primary: immune system — thymus (T-cell selection/output), bone marrow/peripheral lymphoid organs (B-cell development and antibody production), spleen (splenomegaly reported), lymph nodes.
- Secondary/complication-related: respiratory system (recurrent infection, bronchiectasis), gastrointestinal tract (CMV colitis as an opportunistic complication), skin (autoinflammatory lesions, abscesses), eyes (cataracts reported), teeth (hypodontia), nails (dysplasia).
- Body systems involved: immune, respiratory, integumentary, ocular, dental/craniofacial.

**Tissue/cell level:** Lymphoid tissue — T lymphocytes (CD4+ and CD8+), B lymphocytes and plasmablasts, and likely monocyte/macrophage populations (implicated by elevated monocyte-recruiting chemokines MCP-1/MIP-1α/β in the E518K/T559M case). Suggested UBERON terms: UBERON:0002370 (thymus), UBERON:0002106 (spleen), UBERON:0002370, UBERON:0000029 (lymph node), UBERON:0002048 (lung — bronchiectasis).

**Subcellular level:** Cytoplasm (site of IKK complex assembly and IκBα degradation; GO:0005737), nucleus (site of NF-κB dimer translocation and transcriptional activity; GO:0005634).

**Localization:** Systemic/multi-organ rather than lateralized; no reported laterality pattern.

## 8. Temporal Development

**Onset:** Highly variable — reported ages at first symptom range from the first year of life (mild nail dysplasia, mild recurrent upper respiratory infections) to 48 years of age (severe CMV colitis as the presenting event) within the same genetically-defined cohort (Körholz et al. 2025, PMID:40403933). Most patients experience recurrent, mild-to-moderate upper respiratory tract infections beginning in early childhood, with more severe manifestations emerging later.

**Progression:** **Progressive** — a defining feature distinguishing IMD15A from classic congenital combined immunodeficiencies. Lymphocyte counts are typically normal in childhood/youth but decline significantly by adulthood; humoral immunity (specific antibody production) similarly deteriorates over time, and clinically significant complications (bronchiectasis, opportunistic infection) tend to manifest in adulthood.

**Disease course pattern:** Chronic and progressive rather than episodic, though the associated autoinflammatory/cutaneous component can present with flare-remission dynamics (as in the E518K/T559M case, which resolved by age 3 after IVIG prophylaxis, suggesting possible age-dependent penetrance for that particular presentation).

**Critical periods:** Adulthood appears to be a critical window for the most severe infectious/structural complications (bronchiectasis, opportunistic CMV disease), making longitudinal immunologic monitoring from childhood into adulthood clinically important even in mildly-affected pediatric carriers.

## 9. Inheritance and Population

**Epidemiology:** No population-based prevalence or incidence estimates exist; IMD15A is an ultra-rare condition described in a cumulative total of fewer than ~20 published kindreds (roughly 16 patients from 4 families in the largest series to date, plus the original 2-kindred report and additional single-case reports), consistent with a "cases in literature" tier disease. Suggested `prevalence_class`: ULTRA_RARE / NOT_YET_DOCUMENTED (Orphanet-style banding).

**Inheritance pattern:** Autosomal dominant (heterozygous), with documented de novo occurrence in index cases and vertical transmission with variable expressivity in some families (e.g., the 2025 four-family series).

**Penetrance:** Appears high but with markedly **variable expressivity** — clinical severity and organ involvement differ substantially even among relatives sharing an identical variant (nail dysplasia vs. bronchiectasis vs. CMV colitis at ages spanning infancy to the fifth decade).

**Genetic anticipation:** Not reported/established.

**Germline mosaicism:** Not specifically documented for IKBKB GOF variants in the literature reviewed; de novo origin has been confirmed by trio sequencing in index cases.

**Founder effects:** None identified for IMD15A itself. (Note: the contrasting, biallelic loss-of-function IMD15B disorder was described in a founder-like cluster of four families of Northern Cree ancestry — Pannicke et al. 2013 — but this is a distinct, autosomal-recessive entity and should not be conflated with IMD15A's founder status.)

**Consanguinity:** Not relevant to IMD15A's autosomal dominant/de novo genetics (relevant instead to the recessive IMD15B).

**Carrier frequency:** Not applicable (dominant, ultra-rare, largely de novo disorder; the causal alleles are essentially absent from population reference databases such as gnomAD).

**Population demographics:** No ethnic or geographic clustering has been reported for IMD15A; published kindreds are geographically and ethnically heterogeneous (reports from Japan/Australia [original description], the Netherlands and other European centers [2025 series], and the United States [E518K/T559M case, described as a Hispanic infant]).

**Sex ratio / age distribution:** No sex predilection reported; age distribution spans infancy through the fifth decade of life across the aggregate case literature.

## 10. Diagnostics

**Clinical/laboratory tests:**
- Lymphocyte immunophenotyping (flow cytometry): quantify CD3+, CD4+, CD8+ T cells and CD19+ B cells; may be normal in childhood and reduced in adulthood.
- Immunoglobulin levels (IgG, IgA, IgM) and specific-antibody responses (e.g., pneumococcal polysaccharide vaccine response) to detect evolving hypogammaglobulinemia/impaired humoral function.
- Lymphocyte activation assays: T-cell receptor– and B-cell receptor–stimulated upregulation of CD70, CD25, CD40L (reduced at day 3 in affected patients per PMID:40403933); B-cell differentiation into plasmablasts in vitro (impaired).
- Serum cytokine/chemokine panel (research-level): elevated MCP-1, MDC, MIP-1α/β, IL-18, IL-16, S100A8 reported in one variant-specific case (PMID:36378426).
- Phospho-flow cytometry of PBMCs: elevated basal phospho-IKKα/β and phospho-p65; blunted TNF-α–induced IκBα phosphorylation — a research/functional confirmatory assay used in published cases, not yet a standardized clinical test.
- Imaging: chest CT for bronchiectasis surveillance in patients with recurrent respiratory infection.

**Genetic testing:**
- Recommended approach: trio-based **whole exome sequencing (WES)** given the de novo origin of most reported variants and the lack of a defined phenotype-driven gene panel at initial presentation; this is how essentially all published cases have been diagnosed (Cardinez et al. 2018; Körholz et al. 2025).
- **Single-gene IKBKB sequencing** or an inborn-errors-of-immunity gene panel (including IKBKB) is reasonable when clinical suspicion (progressive lymphopenia + recurrent infection ± autoinflammatory skin disease) is high.
- Functional/orthogonal validation of variant pathogenicity (NF-κB luciferase reporter assay, phospho-flow) is advisable given how many IKBKB missense variants are of uncertain significance by sequence-based prediction alone; distinguishing a true GOF allele from a benign polymorphism or a loss-of-function allele (which instead causes the very different IMD15B phenotype) is essential.
- Chromosomal microarray/karyotype/FISH are not primary diagnostic modalities for this single-gene disorder.

**Clinical criteria:** No formal consensus diagnostic criteria have been published; diagnosis rests on the combination of (a) a compatible immunodeficiency/immune-dysregulation phenotype, (b) a heterozygous IKBKB kinase-domain (or NEMO-binding-domain) missense variant, and (c) ideally functional confirmation of gain-of-function activity.

**Differential diagnosis:** Other combined immunodeficiencies and immune dysregulation syndromes with progressive lymphopenia and infection susceptibility (e.g., CVID, other NF-κB pathway disorders such as NFKB1/NFKB2 haploinsufficiency, CARD11 gain-of-function disease, and — critically — **IMD15B** [biallelic IKBKB loss-of-function], which must be distinguished because it carries a very different inheritance pattern, earlier/more severe onset, and different molecular mechanism despite sharing the same gene).

**Screening:** No population or newborn screening program exists for this ultra-rare, typically de novo disorder; genetic counseling and cascade testing of first-degree relatives is appropriate once a proband is identified, given documented vertical transmission in some kindreds.

## 11. Outcome/Prognosis

No formal survival statistics, life-expectancy data, or standardized quality-of-life instrument results have been published, reflecting the rarity and recency of disease description. Qualitatively:
- The disease course is **progressive**, with worsening lymphopenia, hypogammaglobulinemia, and infection burden from childhood into adulthood.
- Reported complications include bronchiectasis (a marker of chronic/recurrent lower respiratory infection), severe opportunistic infection (e.g., life-threatening CMV colitis in a 48-year-old patient), splenomegaly, and cataracts.
- The disease is explicitly described by its most recent characterizers as "progressing toward combined immunodeficiency" over the life course (title of Körholz et al. 2025, PMID:40403933), implying a trajectory from a mild/subclinical pediatric phenotype toward a clinically significant adult combined immunodeficiency, with life-threatening complications possible in adulthood.
- Prognostic stratification by variant/domain is emerging: kinase active-site variants (V203I) and activation-loop variants appear to drive the classic progressive infection/lymphopenia phenotype, while NEMO-binding-domain variants (E518K/T559M) can instead produce a predominantly autoinflammatory/autoimmune course with potentially better long-term outcome (resolution of episodes by early childhood in the reported case).

## 12. Treatment

**Pharmacotherapy/supportive care:**
- **Immunoglobulin replacement therapy (IVIG)** for hypogammaglobulinemia/impaired specific-antibody production — used both prophylactically (in the autoinflammatory E518K/T559M case, initiated at 9 months of age, 0.5 g/kg, with resolution of febrile/AIHA flares and discontinuation by age 3) and as standard supportive management for evolving antibody deficiency in classic IMD15A. NCIT term: NCIT:C15302 is for physical therapy — appropriate treatment term here is **NCIT:C15986 (Pharmacotherapy)** with therapeutic agent bound to **NCIT** (immunoglobulin replacement has no single CHEBI small-molecule term; consider NCIT:C1518 or a supportive-care code).
- Prophylactic antimicrobials for recurrent sinopulmonary infection (standard combined-immunodeficiency supportive care), analogous to management of other CID entities.

**Advanced/targeted therapeutics:**
- **No approved targeted (small-molecule IKK2 inhibitor) therapy exists in routine clinical use.** The literature explicitly notes that systemic IKK2 inhibitors are not standard clinical practice, so selective pharmacologic blockade of the mutant kinase is **not currently a viable therapeutic option** for IKBKB-GOF patients (Körholz et al. 2025, PMID:40403933) — an important negative finding for treatment planning.
- **Hematopoietic stem cell transplantation (HSCT)** has been used in the more severe, infection-predominant end of the phenotypic spectrum, but the decision is described as "highly individualized" given the marked phenotypic variability of IKBKB-GOF disease; HSCT is better established for the distinct, more uniformly severe IMD15B (loss-of-function) phenotype (see PMC7106064, "Clinical presentation, immunologic features, and hematopoietic stem cell transplant outcomes for IKBKB immune deficiency"). NCIT term: NCIT:C15431 (Hematopoietic Stem Cell Transplantation).
- No published experience with JAK inhibitors, biologics, or gene therapy specific to IKBKB-GOF disease was identified in the current literature (unlike, for example, STAT1/STAT3 gain-of-function disorders, where JAK inhibition is now well established) — this represents an open therapeutic gap rather than an established modality.

**Surgical/interventional:** Not disease-specific beyond standard management of structural complications (e.g., bronchiectasis) per general pulmonology practice.

**Experimental treatments:** No disease-specific registered clinical trials (ClinicalTrials.gov) were identified for IMD15A specifically, consistent with its rarity and recent characterization.

**Treatment strategy considerations:** Because the phenotype spans infection-predominant (classic IMD15A) and autoinflammatory/autoimmune-predominant presentations depending on the specific variant/domain affected, treatment must be individualized — immunoglobulin replacement and infection prophylaxis for the classic phenotype, and immunomodulation (e.g., IVIG for autoimmune cytopenia) for the autoinflammatory variant-specific presentation — with HSCT reserved for the most severe, refractory infectious phenotype.

## 13. Prevention

No primary prevention (e.g., vaccination against the disease itself) is possible for this monogenic disorder. Relevant preventive measures are entirely secondary/tertiary:
- **Genetic counseling** for identified families, given autosomal dominant inheritance with variable expressivity — informing recurrence risk (up to 50% for offspring of an affected parent) and enabling predictive testing of at-risk relatives.
- **Prenatal/preimplantation genetic testing** could be considered for families with a known pathogenic variant, though no specific reports of its use for IMD15A were identified.
- **Standard immunization practices** (with attention to live-vaccine safety once T-cell dysfunction is identified) and **infection-prophylaxis measures** (e.g., antimicrobial prophylaxis, prompt treatment of infections) as tertiary prevention against complications such as bronchiectasis.
- **Surveillance screening**: periodic immunologic monitoring (lymphocyte subsets, immunoglobulin levels) is prudent in known carriers/affected individuals from childhood onward, given the documented progressive natural history, to enable early initiation of immunoglobulin replacement or other supportive therapy before severe complications (e.g., opportunistic CMV disease) develop.

## 14. Other Species / Natural Disease

No naturally occurring veterinary or wildlife disease orthologous to human IMD15A has been reported. IKBKB is broadly conserved (mouse ortholog *Ikbkb*, MGI:1338071; NCBI Gene — mouse), but no spontaneous animal disease phenocopy is documented (searched OMIA — no entry identified for this specific gain-of-function condition).

## 15. Model Organisms

**Genetically engineered mouse models:**
- **CRISPR/Cas9 orthologous knock-in mouse (Ikbkb p.V203Ile)**, generated by Cardinez et al. (2018, PMID:30337470) specifically to validate the human V203I variant as causal. Heterozygous and homozygous Ikbkb-V203I mice recapitulated key human findings: altered basal and activation-induced IκBα phosphorylation/degradation kinetics in splenocytes, and reduced peripheral blood CD3+ T-cell percentage, with the authors explicitly noting "mice and humans carrying this missense mutation exhibit remarkably similar cellular and biochemical phenotypes" — a high-fidelity model for this specific variant.
- **Germline Ikbkb (Ikk2) knockout mice** (unrelated to the GOF disease but mechanistically informative for the gene's baseline biology): homozygous null mice are **embryonic lethal (~E14.5)** due to massive hepatocyte apoptosis/liver degeneration, rescuable by concurrent Tnfr1 (Tnfrsf1a) inactivation, establishing IKKβ's essential role in NF-κB-mediated protection against TNF-induced apoptosis (Li et al. 1999, *Science*, PMID:10195897; Li et al. 1999, *Genes Dev*, PMID:10229185). These null-mouse studies are foundational general IKKβ biology rather than IMD15A-specific disease models, since complete loss of IKKβ in mice is not a phenocopy of the human gain-of-function IMD15A disorder (it more closely relates conceptually, though not identically, to the human loss-of-function IMD15B mechanism).
- No zebrafish, Drosophila, C. elegans, or iPSC-derived organoid models specific to IKBKB gain-of-function disease were identified in the literature reviewed.

**Model characteristics and limitations:** The V203I knock-in mouse is the only model directly engineered to recapitulate the human IMD15A-causing variant, and it reproduces immunophenotypic (T-cell percentage) and biochemical (IκBα kinetics) features. However, published data on this model emphasize young/baseline immunophenotyping; whether it recapitulates the *progressive*, age-dependent worsening (into adult bronchiectasis-level infection susceptibility or autoinflammatory skin disease) seen in the oldest human patients has not been reported, representing a translational gap between the mouse model's demonstrated fidelity for acute biochemical/T-cell-percentage phenotypes and the full, decades-long human natural history.

**Resources:** MGI:1338071 (Ikbkb mouse gene); no dedicated IMPC/KOMP conditional-allele phenotyping data specific to the V203I disease-associated allele were identified (standard IMPC records cover germline-null Ikbkb, which is embryonic lethal and thus not informative for adult immune phenotyping without conditional/inducible approaches).

---

## Summary of Ontology Term Suggestions

| Category | Suggested terms |
|---|---|
| Disease | MONDO:0032599 (Immunodeficiency 15A) |
| Gene | HGNC:5960 (IKBKB) |
| Phenotypes (HP) | HP:0002205, HP:0001888, HP:0002850, HP:0002110, HP:0001744, HP:0000518, HP:0000668, HP:0031292, HP:0001878, HP:0002164 |
| GO (biological process) | GO:0007249, GO:0043123, GO:0002322, GO:0002741 |
| CL (cell type) | CL:0000084, CL:0000625, CL:0000624, CL:0000236, CL:0000980 |
| UBERON | UBERON:0002370 (thymus), UBERON:0002106 (spleen), UBERON:0002048 (lung) |
| NCIT (treatment) | NCIT:C15986 (Pharmacotherapy), NCIT:C15431 (Hematopoietic Stem Cell Transplantation) |

## Key Citations (PMID)

1. Cardinez C, et al. "Gain-of-function IKBKB mutation causes human combined immune deficiency." *J Exp Med.* 2018. **PMID:30337470**
2. Pannicke U, et al. "Deficiency of innate and acquired immunity caused by an IKBKB mutation." *N Engl J Med.* 2013;369:2504–14. **PMID:24369075**
3. Abbott J, et al. "Heterozygous IKKβ activation loop mutation results in a complex immunodeficiency syndrome." *J Allergy Clin Immunol.* 2021. **PMID:32554083**
4. Körholz J, Tromp SAM, Dalm VASH, et al. "IKBKB gain of function: An inborn error with clinical heterogeneity progressing toward combined immunodeficiency." *J Allergy Clin Immunol.* 2025. **PMID:40403933**
5. [Case report] "A Heterozygous Gain-of-Function Variant in IKBKB Associated with Autoimmunity and Autoinflammation." *J Clin Immunol.* 2022. **PMID:36378426**
6. Li Q, et al. "Severe liver degeneration in mice lacking the IkappaB kinase 2 gene." *Science.* 1999. **PMID:10195897**
7. Li ZW, et al. "Embryonic lethality, liver degeneration, and impaired NF-kappa B activation in IKK-beta-deficient mice." *Genes Dev.* 1999. **PMID:10229185**
8. OMIM #618204 — IMMUNODEFICIENCY 15A; IMD15A — https://omim.org/entry/618204
9. OMIM #615592 — IMMUNODEFICIENCY 15B; IMD15B — https://www.omim.org/entry/615592
10. OMIM *603258 — IKBKB — https://www.omim.org/entry/603258

**Note on evidence gaps for KB curation:** This is an ultra-rare, recently-described (2018–2025) disorder. Quantitative epidemiology (prevalence/incidence), formal quality-of-life data, survival statistics, and dedicated omics datasets (transcriptomic/proteomic) are **not currently available** in the literature and should be recorded as `NOT_YET_DOCUMENTED`/absent rather than inferred. The mechanistic step linking "NF-κB pathway hyperactivation" to "T/B lymphocyte functional hypofunction and progressive lymphopenia" is empirically observed but not yet fully mechanistically resolved — this should be flagged as a knowledge gap in a curated pathophysiology entry.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 8 |
| On topic | 5 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:10229185` (2 mentions) - Embryonic lethality, liver degeneration, and impaired NF-kappa B activation in IKK-beta-deficient mice.
  - shared terms: none

Weighed against this report's own most characteristic terms: `disease`, `imd15a`, `ikbkb`, `variant`, `infection`, `phenotype`, `patient`, `gene`, `immunodeficiency`, `progressive`, `severe`, `disorder`, `autoinflammatory`, `clinical`, `recurrent`, `t559m`, `bronchiectasis`, `cmv`, `e518k`, `combined`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 41 |
| Resolved | 38 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 23 |
| Terms named correctly | 14 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0010976` (1 mention) - the report calls it "Documented in functional assays"; HP calls it **Decreased total B cell count**
- `HP:0002164` (2 mentions) - the report calls it "Rare/variable"; HP calls it **Nail dysplasia**
- `HP:0001878` (2 mentions) - the report calls it "AIHA"; HP calls it **Hemolytic anemia**
- `GO:0002741` (2 mentions) - the report calls it "positive regulation of cytokine secretion involved in immune response"; GO calls it **GO_0002741**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0002741` (GO_0002741) (2 mentions) - replaced by `GO:0002720`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001888` (2 mentions) - the report calls it "Lymphopenia"; HP calls it **Decreased total lymphocyte count**, and lists "Lymphopenia" among its other names
- `GO:0007249` (2 mentions) - the report calls it "I-kappaB kinase/NF-kappaB signaling"; GO calls it **canonical NF-kappaB signal transduction**, and lists "I-kappaB kinase/NF-kappaB signaling" among its other names
- `GO:0043123` (2 mentions) - the report calls it "positive regulation of I-kappaB kinase/NF-kappaB signaling"; GO calls it **positive regulation of canonical NF-kappaB signal transduction**, and lists "positive regulation of I-kappaB kinase/NF-kappaB signaling" among its other names
- `GO:0042104` (1 mention) - the report calls it "positive regulation of activated T cell proliferation — for contrast/negative regulation defects"; GO calls it **positive regulation of activated T cell proliferation**
- `UBERON:0002048` (2 mentions) - the report calls it "lung — bronchiectasis"; UBERON calls it **lung**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`.