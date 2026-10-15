---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-23T15:49:44.245412'
end_time: '2026-09-23T15:54:45.895498'
duration_seconds: 301.65
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: RECON Progeroid Syndrome
  mondo_id: MONDO:0957266
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
  web_search_requests: 10
  num_turns: 18
  total_cost_usd: 1.3234696000000001
  session_id: fd65d8eb-852b-5a9d-91de-140beff025e2
  stop_reason: end_turn
  assistant_text_blocks: 1
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderBillingError
  status_code: 402
  remedy: the account is out of credits
  retryable: false
- provider: claude_code
  succeeded: true
citation_count: 15
reference_validation:
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 7
  on_topic: 4
  off_topic: 1
  off_topic_references:
  - PMID:36907310
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 44
  verified: 41
  not_found: 0
  obsolete: 2
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0957266
    reported_labels:
    - MONDO
    ontology_label: RECON progeroid syndrome
  obsolete_terms:
  - term_id: HP:0009062
    ontology_label: obsolete Infantile axial hypotonia
    replaced_by: HP:0008936
  - term_id: GO:0000784
    ontology_label: GO_0000784
    replaced_by: GO:0000781
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** RECON Progeroid Syndrome
- **MONDO ID:** MONDO:0957266 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **RECON Progeroid Syndrome** covering all of the
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

# RECON Progeroid Syndrome — Research Report

**Target:** RECON Progeroid Syndrome | OMIM #620370 | MONDO:0957266 | HGNC gene RECQL (HGNC:9948) | NCBI Gene 5965

**Note on ontology term suggestions throughout this report:** Every HP/GO/CL/CHEBI/NCIT identifier below is a *proposed* binding based on phenotype/mechanism descriptions in the literature, not a verified lookup against the live ontology. Per this repository's term-binding contract, treat every suggested CURIE as a lead to be checked with `runoak`/OAK against the current HP/GO/CL build before it is written into any `kb/disorders/*.yaml` file — do not copy an ID from this report directly into a binding.

---

## 1. Disease Information

**Overview.** RECON syndrome ("RECql ONe" syndrome) is an autosomal recessive genome-instability/progeroid disorder first described in 2022, caused by a biallelic (homozygous) missense mutation in *RECQL* (also called *RECQL1*, *RECQ1*), the first human disease ever attributed to this gene despite its 1992 discovery. It is characterized by postnatal growth retardation, a progeroid ("prematurely aged") facial gestalt, cutaneous photosensitivity/xeroderma, and slender elongated digits, occurring on a background of cellular chromosomal instability and defective replication-fork restart (Arboleda-Velasquez lab / Sturzenegger et al., *J Clin Invest* 2022; PMID:35025765).

> "RECON syndrome (for RECQ ONe) ... is a genome instability disorder caused by mutations in the DNA helicase RECQL1." — PMC8884905 abstract.

**Key identifiers:**
| Resource | ID |
|---|---|
| OMIM (phenotype) | #620370 — RECON PROGEROID SYNDROME |
| OMIM (gene) | *600537 — RECQ PROTEIN-LIKE; RECQL |
| MONDO | MONDO:0957266 |
| MedGen | C5830504 (UID 1841140) |
| NCBI Gene | 5965 (RECQL) |
| HGNC | HGNC:9948 (RECQL) |
| UniProt disease | DI-06683 |
| Gene locus | 12p12.1 |
| Reference transcript | NM_032941.2 |
| Orphanet | **No ORPHA number could be located** — this appears to be an Orphanet coverage gap, consistent with the disease's extreme rarity (3 genotyped patients worldwide as of this report) and recent (2022) description. Confirm during curation rather than assuming absence is permanent.
| GeneReviews chapter | None found — too recently described / too few families for a dedicated chapter.

**Synonyms:** RECON syndrome; RECON progeroid syndrome; RECQL1-related progeroid syndrome. No historical/eponymous synonyms exist since this is a molecularly-defined, recently named entity.

**Evidence basis:** This entry is built almost entirely on a single primary molecular/clinical study (2 families, 3 genotyped individuals; PMID:35025765) plus one aging-biology review by an overlapping author group (PMID:36907310, PMC10018417) and downstream database records (OMIM, MedGen, MalaCards, GeneCC) that recapitulate the same primary source. This is aggregated disease-level curation from structured databases plus the two original literature reports — not EHR/individual-patient-level data.

---

## 2. Etiology

**Disease-causal factor:** Purely genetic/mechanistic — homozygous hypomorphic missense variant in *RECQL*, a RecQ-family ATP-dependent DNA helicase gene. No environmental, infectious, or lifestyle causal factor is implicated in disease *causation* (photosensitivity is a *phenotypic consequence* of the underlying DNA-repair defect, not an environmental cause).

**Genetic risk factors:**
- **Causal variant:** *RECQL* NM_032941.2:c.1375G>T, p.(Ala459Ser) (p.A459S), homozygous, located in the zinc-binding domain (ZBD) of the helicase core. Identified independently, identical, in two apparently unrelated Middle Eastern families (PMID:35025765).
- **In silico pathogenicity:** CADD 25.9; PolyPhen-2 0.846 (probably damaging); MutationTaster 1.0; DANN 0.9977; GERP conservation score 6.04 (highly conserved alanine).
- **Population frequency:** Absent from gnomAD and the Greater Middle East (GME) Variome — consistent with a very rare/founder allele rather than a common polymorphism.
- **Linkage support:** LOD score Z = 3.311 at θ = 0 in Family A (consanguineous pedigree), supporting causality by segregation.
- **Consanguinity:** Family A are double first cousins; parents of the affected sisters are first-degree relatives, consistent with autosomal recessive homozygosity. Family B had no reported consanguinity, raising the possibility of a shared regional founder haplotype for the identical variant, though this was not explicitly confirmed by haplotype analysis in the primary report as summarized here.
- **Modifier genes:** None reported or investigated.

**Environmental risk factors:** None identified as disease-causing. UV/sunlight exposure is expected to *exacerbate* the cutaneous photosensitivity phenotype (as in other RecQ-helicase disorders), by mechanistic analogy rather than direct study in this cohort.

**Protective factors:** None reported. Heterozygous carrier parents and 8 healthy siblings across both families were phenotypically normal, indicating the pathogenic mechanism requires biallelic loss of function/hypomorphic activity (recessive), i.e., a single wild-type allele is fully protective in this Mendelian sense.

**Gene-environment interaction:** Not formally studied. By mechanistic inference (impaired replication-fork restart after genotoxic/replicative stress — camptothecin [TOP1 poison], etoposide [TOP2 poison], hydroxyurea [replication stress], MMS [alkylation]), affected individuals' cells are hypothesized to be hypersensitive to genotoxic environmental/pharmacologic exposures, though this has only been demonstrated in vitro in patient-derived lymphoblastoid cell lines (LCLs) and fibroblasts, not shown clinically as altered exposure sensitivity in the patients themselves.

**Important lump/split note for curation:** *RECQL* also independently causes **autosomal-dominant, monoallelic breast-cancer susceptibility** via rare truncating variants (e.g., c.643C>T/p.Arg215*), acting through haploinsufficiency with no loss of heterozygosity in tumors (PMID:25915596; Nature Genetics 2015). This is a **mechanistically and clinically distinct disease entity** from RECON syndrome — different zygosity (heterozygous vs. homozygous), different variant class (truncating/LOF vs. hypomorphic missense), different phenotype (adult-onset cancer predisposition vs. pediatric progeroid syndrome), and no overlap reported between the two patient populations. Keep separate dismech entries; do not conflate "RECQL-related disease" as a single node.

---

## 3. Phenotypes

Phenotype data are drawn from three genotype-confirmed patients (Family A: III-2, age 9y8m at report, and III-4, age 4y; Family B: III-4, followed from 5y10m to 14y9m) in PMID:35025765, cross-checked against MedGen's HPO-based phenotype list for C5830504.

| Phenotype | Type | Onset/course | Frequency (n/3 genotyped) | Suggested HP term (unverified — confirm before binding) |
|---|---|---|---|---|
| Postnatal growth retardation / short stature | Physical sign | Noted by ~18 months; progressive (Family B height z-score fell from baseline to −3.59 by age 14) | 3/3 | HP:0004322 Short stature (or HP:0008897 Postnatal growth retardation) |
| Severe wasting / reduced subcutaneous fat | Physical sign | Progressive (Family B weight z-score −8.47 at age 14) | 3/3 | HP:0001508 Failure to thrive; HP:0009062 Decreased subcutaneous fat |
| Progeroid ("prematurely aged," mask-like/senile) facial appearance | Physical sign | Present from early childhood | 3/3 | HP:0002185 Neurodegeneration (NOT applicable) → correct candidate: HP:0002777 Progeroid facial appearance |
| Hypoplastic/tiny pinched nose, underdeveloped nasal alae, anteverted nares | Physical sign | Congenital/early | 3/3 | HP:0000437 Depressed nasal bridge / HP:0000463 Anteverted nares / HP:0009928 Hypoplastic nasal alae |
| Prominent premaxilla, smooth philtrum, thin lips | Physical sign | Early childhood | Variable (reported in Family A) | HP:0010804 Prominent premaxilla |
| Slender, elongated ("arachnodactyly-like") thumbs with hyperconvex nails | Physical sign | Congenital | 3/3 | HP:0009237 Long thumb; HP:0100807 Long fingers; HP:0001596 Hyperconvex nail |
| Xeroderma / dry, scaling skin, desquamation on sun-exposed areas | Physical sign | Early onset, chronic | 3/3 | HP:0000958 Dry skin (xeroderma) |
| Cutaneous photosensitivity | Physical sign | Early onset | 3/3 | HP:0000992 Cutaneous photosensitivity |
| Xerophthalmia / keratoconjunctivitis sicca, red eyes, absent lower eyelid lashes | Physical sign | Early | Present in both families | HP:0001097 Dry eye; HP:0000232 Absent eyelashes |
| Livedo reticularis, keratosis pilaris | Physical sign | Childhood | Family A | HP:0100641 Livedo reticularis; HP:0032599 Keratosis pilaris (verify exact HPO term) |
| Delayed eruption of permanent teeth, dental crowding | Physical sign | Childhood | Family A | HP:0000684 Delayed eruption of teeth |
| Thrombocytopenia | Laboratory abnormality | Reported in Family B (progressive course) | 1/3 documented | HP:0001873 Thrombocytopenia |
| Anemia | Laboratory abnormality | MedGen-listed | Not detailed per-patient in extracted text | HP:0001903 Anemia |
| Recurrent chest/respiratory infections | Clinical sign | Family B, later course | 1/3 documented | HP:0002205 Recurrent respiratory infections |
| Joint hypermobility | Physical sign | MedGen-listed | Not detailed per-patient | HP:0001382 Joint hypermobility |
| Microcephaly | Physical sign | MedGen-listed as associated | Conflicts somewhat with primary paper's "no microcephaly" framing in the comparison table generated above — **flag for curator verification against primary source**, do not assume presence without re-checking the original clinical description |
| Hirsutism | Physical sign | MedGen-listed | Not detailed per-patient | HP:0001007 Hirsutism |

**Severity/progression pattern:** Family B illustrates a clearly progressive course — the same patient followed from age ~6 to ~15 years showed worsening growth failure and wasting (height z-score −1.98-equivalent range declining toward −3.59; weight z-score reaching −8.47), i.e., this is not a static congenital malformation syndrome but an accumulating, progeroid degenerative trajectory, consistent with the "genome instability accrual over time" mechanism proposed by the authors.

**Quality of life impact:** Not formally measured (no EQ-5D/SF-36/PROMIS data reported); qualitatively, severe growth failure, recurrent infections, and photosensitivity would be expected to impose a substantial pediatric disease burden, but this is inference, not measured outcome data.

**Not yet assessed / open questions for phenotype curation:** Neurodevelopmental/cognitive phenotype is not emphasized in either source as abnormal (unlike some RecQ disorders); this should be explicitly confirmed as "normal cognition documented" vs. "not assessed" rather than left silent, since the distinction matters for downstream users comparing to Bloom/Werner syndrome, which also generally spare cognition.

---

## 4. Genetic/Molecular Information

**Causal gene:** *RECQL* (RECQ Like Helicase; also known as *RECQL1*, *RECQ1*), HGNC:9948, NCBI Gene 5965, OMIM *600537, locus 12p12.1.

**Pathogenic variant:**
- Genomic: chr12:21,626,557 (hg19)
- cDNA: NM_032941.2:c.1375G>T
- Protein: p.Ala459Ser (p.A459S)
- Variant type: missense (substitution within the zinc-binding domain, ZBD)
- Zygosity: **homozygous** in all 3 genotyped affected individuals; parents and 8 unaffected siblings across both families were heterozygous or wild-type
- ACMG-style classification: Not explicitly stated as a formal ACMG term in the sources retrieved, but functionally and segregation-validated as disease-causing (pathogenic) in the primary report
- Origin: germline (not somatic)
- Allele frequency: absent from gnomAD and the Greater Middle East (GME) Variome — i.e., not present in any population reference database retrieved
- Functional consequence: **hypomorphic** loss-of-function — the mutant retains partial activity rather than being a complete null (distinguishing RECON from the complete-null disease model)

**Gene-disease validity note:** GenCC/ClinGen submitter records show a **"Disputed Evidence"** classification from Labcorp Genetics (formerly Invitae), evaluated 2023-11-30, for the RECQL–RECON progeroid syndrome relationship. This reflects the very limited evidence base (single recurrent variant, two families) typical of an ultra-recently described gene-disease pair, and should be represented honestly in curation as a **limited/disputed validity** relationship rather than "definitive" — cite the GenCC record and the caveat explicitly if a validity classification slot is populated.

**Functional/biochemical consequences of p.A459S** (all from PMID:35025765, functional assays comparing recombinant WT vs. mutant RECQL1):
- **ATPase activity:** markedly reduced kcat/Km/Vmax for ATP hydrolysis relative to WT.
- **Helicase (DNA unwinding) activity:** substantially reduced — e.g., WT unwound ~60% of a forked-duplex substrate at 2.5 nM protein vs. ~20% for mutant; 2.6- to 4.8-fold reduction in unwinding rate depending on substrate/concentration.
- **Fork restoration (regressed-fork restart) activity:** 7-fold reduction at 5 minutes, ≥3.5-fold at later time points; ATP-dependent.
- **DNA binding:** modestly reduced affinity (~1.5-fold higher apparent Kd) for forked-duplex DNA.
- **Strand-annealing activity:** essentially **preserved**, unlike unwinding — a mechanistically important dissociation showing the mutation selectively impairs the ATP-driven translocase/helicase function rather than all DNA-binding functions.
- **Oligomerization:** normal (assessed by size-exclusion chromatography).
- **Protein expression/stability and nuclear localization:** normal in patient LCLs — the defect is purely catalytic/functional, not one of protein loss or mislocalization.

**Structural mechanism:** p.A459S disrupts a hydrophobic cluster within the ZBD core (involving residues W466, M458 in the ZBD; M395, Y359 in the helicase-C domain; F281 in the helicase linker). Because the ZBD is spatially juxtaposed to the ATP-binding cleft, this perturbation is proposed to impair allosteric coupling between ATP binding/hydrolysis and DNA unwinding, explaining the combined ATPase/helicase defect from a single point substitution.

**Cellular phenotypes** in patient-derived LCLs/fibroblasts:
- Elevated spontaneous and drug-induced (camptothecin [TOP1 poison]/etoposide [TOP2 poison]) 53BP1 DNA-damage foci; corrected by complementation with WT RECQL1.
- Increased spontaneous and drug-induced chromosome breakage, phenotypically comparable in degree to an ataxia-telangiectasia-like disorder (ATLD) patient LCL used as comparator.
- Mildly increased spontaneous and DNA-damage-induced sister chromatid exchange (SCE) — notably a much milder SCE phenotype than in Bloom syndrome, where SCE elevation is a diagnostic hallmark.
- Increased spontaneous replication-fork stalling, consistent with baseline endogenous replication stress.
- Failure to efficiently replicate through TOP1/TOP2-induced lesions (camptothecin/etoposide) and failure to restart forks after hydroxyurea (nucleotide depletion) or MMS (alkylation) exposure, with increased chromosome breakage after MMS.
- Mildly increased replication-fork degradation after prolonged hydroxyurea exposure, correctable by WT complementation.
- Robust ATM-dependent DNA-damage-response (DDR) signaling activation despite the underlying repair defect — i.e., the sensor/signaling arm of the DDR is intact; the defect is specifically in the helicase-mediated repair/restart step.
- No aberrant MLL/ENL locus translocations after etoposide exposure (distinguishing the mechanism from TDP2-deficiency-associated translocations).

**Epigenetic information:** Not directly studied in the primary RECON paper. The companion review (PMC10018417) frames genome-wide transcriptional/epigenetic alteration as one of three "hallmarks of aging" hypothesized to be relevant (alongside genomic instability and telomere attrition) but does not report direct patient epigenomic data for RECON syndrome specifically.

**Chromosomal abnormalities:** No gross chromosomal rearrangements/aneuploidy reported in patients; the "chromosomal instability" terminology in this disease refers to increased chromosome *breakage* and replication-stress phenotypes at the cellular level, not constitutional karyotypic abnormality.

**Suggested GO terms (leads, verify before binding):**
- GO:0003678 DNA helicase activity
- GO:0006269 DNA replication, synthesis of RNA primer / GO:0000731 DNA synthesis involved in DNA repair
- GO:0031297 replication fork processing
- GO:0006281 DNA repair
- GO:0000724 double-strand break repair via homologous recombination

---

## 5. Environmental Information

No causal environmental, lifestyle, or infectious factor has been reported for RECON syndrome; it is monogenic. As above, exogenous genotoxic stressors (UV light for the cutaneous phenotype; by mechanistic analogy, topoisomerase poisons and alkylating/replication-stress agents for the cellular defect) are plausible *exacerbating* rather than causal exposures, inferred from the in vitro genotoxin-sensitivity assays (camptothecin, etoposide, hydroxyurea, MMS) rather than from documented clinical exposure histories. No infectious trigger is described. This section is essentially "not applicable" for a purely Mendelian ultra-rare disorder with no reported gene-environment study.

---

## 6. Mechanism / Pathophysiology

### Causal chain (ordered, with inference flagged)

1. Homozygous *RECQL* c.1375G>T (p.A459S) **leads to** a structurally destabilized zinc-binding-domain/ATP-binding-cleft interface in the RECQL1 helicase protein (demonstrated: structural/biochemical analysis, PMID:35025765).
2. This structural change **results in** markedly reduced ATPase and DNA-unwinding (helicase) catalytic activity, and impaired fork-restoration activity, while DNA binding and strand-annealing remain largely intact (demonstrated: recombinant protein biochemistry).
3. Reduced RECQL1 helicase/fork-restoration activity **leads to** impaired restart of replication forks that stall or regress — particularly forks stalled by topoisomerase I/II poisons (camptothecin, etoposide), nucleotide depletion (hydroxyurea), or alkylation damage (MMS) (demonstrated: patient LCL replication assays).
4. Impaired fork restart **results in** accumulation of unresolved/collapsed replication forks and persistent replication stress, evidenced by increased spontaneous fork stalling and increased fork degradation after prolonged replication stress (demonstrated: DNA fiber assays in patient cells).
5. Persistent replication stress and fork collapse **lead to** increased DNA double-strand breaks — marked by elevated spontaneous and drug-induced 53BP1 foci and chromosome breakage — despite intact upstream ATM-dependent damage-signaling activation, i.e., the sensing/signaling machinery works but the repair/restart step downstream of it is defective (demonstrated: patient LCL/fibroblast assays).
6. Chronic low-level genomic instability (chromosome breakage, mildly elevated sister chromatid exchange) at the cellular level **is proposed to result in** (inferred, not directly demonstrated longitudinally in patients) progressive cellular attrition/senescence in proliferative and genome-maintenance-dependent tissues (skin, connective tissue, growth plate, hematopoietic compartment).
7. This cellular-level genome-instability burden **is hypothesized to underlie** (inferred; the authors explicitly frame this as a hallmarks-of-aging model rather than a proven tissue-level mechanism) the clinical progeroid phenotype: postnatal growth failure/short stature, progeroid facial appearance, xeroderma/photosensitivity, and slender-digit skeletal features, by analogy to the general model that replication-stress/genome-instability disorders (Bloom, Werner, Rothmund-Thomson) manifest as premature-aging phenotypes.
8. Independently and in parallel (branch point, not sequential to steps 6–7): the cytopenias reported in one patient (thrombocytopenia, anemia) and recurrent infections **may reflect** (inferred) a hematopoietic-compartment consequence of chronic replication stress in a highly proliferative stem/progenitor cell population, analogous to bone-marrow-failure phenotypes in other genome-instability syndromes (e.g., Fanconi anemia), though this specific causal link is **not demonstrated** for RECON syndrome and should be flagged as speculative/unconfirmed in any curated pathograph edge.

### Molecular pathways
RECQL1 functions within the **replication-stress response / homologous-recombination-adjacent fork-protection pathway**, distinct from but overlapping the canonical HR machinery (RAD51, BRCA1/2) and from the Fanconi anemia pathway. It interacts functionally (and antagonistically in terms of timing) with **PARP1**: PARP1 poly(ADP-ribosyl)ation stabilizes regressed forks and *restrains* premature RECQL1-mediated restart, so the two proteins together regulate the *timing* of fork restart rather than acting in a simple linear cascade (PMID cited in search results on RECQL1–PARP1 fork restart antagonism). No canonical developmental signaling pathway (Wnt/MAPK/mTOR/PI3K-AKT) has been implicated; this is a DNA-metabolism/genome-maintenance pathway disorder, not a classical signal-transduction disease.

### Cellular processes
- DNA replication-fork protection and restart (central, demonstrated defective)
- DNA double-strand break repair / genome stability maintenance (demonstrated defective downstream consequence)
- Possible transcriptional regulation: newer data (cited in the aging review, PMC10018417) indicate RECQL1 "preferentially binds to guanine (G)-rich sequences in target promoter elements that it directly regulates," including genes such as *SHOX* (a key growth-plate/stature gene) — an emerging, less-established (basic-research-stage) mechanism potentially directly linking RECQL1 to the short-stature phenotype via gene regulation rather than solely via genome-instability/senescence. This should be flagged as an emerging hypothesis, not an established causal mechanism for the human phenotype.
- Cellular senescence (inferred/hypothesized downstream consequence, not directly measured with senescence markers — e.g., no p16/SA-β-gal data reported — in the retrieved sources)

### Protein dysfunction
Loss-of-function is **hypomorphic and selective**: catalytic (ATPase/helicase/fork-restoration) impairment with preserved DNA-binding and strand-annealing — a partial, function-selective loss rather than complete null or a dominant-negative/gain-of-function mechanism. No protein misfolding/aggregation phenotype is reported (protein expression and localization are normal).

### Metabolic changes
None reported; this is not a primary metabolic disease.

### Immune system involvement
Not a primary immunodeficiency, but recurrent chest infections were reported in one patient (Family B) — mechanism unestablished; could reflect general frailty/wasting rather than a specific immune defect, and this ambiguity should be preserved in curation notes rather than resolved without a source.

### Tissue damage mechanisms
Replication-stress-driven genomic instability is the proposed unifying tissue-damage mechanism, analogous to other RecQ-helicase progeroid disorders, but tissue-specific histopathology has not been reported for RECON syndrome specifically (no biopsy/pathology data in the retrieved sources).

### Biochemical abnormalities
Core biochemical defect = reduced RECQL1 ATPase/helicase/fork-restoration enzymatic activity (quantified above in Section 4).

### Molecular profiling
No transcriptomic, proteomic, metabolomic, lipidomic, single-cell, or spatial-omics datasets for RECON-syndrome patient tissue were identified in this search. This is an important, honestly-reportable gap — given the disease's rarity and recency, no GEO/ArrayExpress/PRIDE/MetaboLights datasets appear to exist yet.

---

## 7. Anatomical Structures Affected

**Organ level (primary):** Skin (photosensitivity, xeroderma, livedo reticularis, keratosis pilaris); craniofacial skeleton/soft tissue (progeroid facial gestalt, nasal hypoplasia, premaxilla prominence); skeletal system, specifically the hands (slender/elongated thumbs, arachnodactyly); growth (whole-body postnatal growth failure — endocrine/skeletal growth axis); ocular surface (dry eyes/keratoconjunctivitis sicca, absent lower lashes); dentition (delayed eruption, crowding).

**Organ level (secondary/systemic):** Hematologic system (thrombocytopenia, anemia reported in at least one patient); respiratory system (recurrent chest infections in one patient); adipose tissue (severe loss of subcutaneous fat).

**Body systems involved:** Integumentary, musculoskeletal, craniofacial/dermatologic, ophthalmologic, hematologic, and (by underlying cellular mechanism) essentially every proliferative tissue compartment via the genome-instability mechanism.

**Tissue/cell level:** Dermal fibroblasts and keratinocytes (photosensitivity/xeroderma phenotype, and the fibroblast lines used experimentally); lymphoblastoid cells (the primary cellular model used — Epstein-Barr-virus-transformed B lymphocytes, i.e., patient-derived LCLs); by extension, any rapidly-dividing progenitor population (hematopoietic stem/progenitor cells, growth-plate chondrocytes) is mechanistically implicated but not directly biopsied/profiled in the retrieved literature.

**Suggested UBERON/CL terms (leads, verify before binding):**
- UBERON:0002097 skin of body
- UBERON:0001456 face
- UBERON:0002389 skeleton of manus / UBERON:0002389-adjacent thumb-specific term
- CL:0000057 fibroblast
- CL:0000542 lymphocyte (patient LCLs specifically derive from CL:0000236 B cell)
- CL:0000138 chondrocyte (inferred relevance to growth-plate mechanism, not directly studied)

**Subcellular level:** Nucleus — RECQL1 is a nuclear protein acting at replication forks and sites of DNA damage; normal nuclear localization is preserved in the mutant. Suggested GO Cellular Component: GO:0005634 nucleus; GO:0000784/GO:0036387 pre-replicative complex/replication fork (verify exact term).

**Localization/laterality:** No lateralization reported; phenotype is bilateral/symmetric (e.g., bilateral arachnodactyly explicitly noted in Family B).

---

## 8. Temporal Development

**Onset:** Early infancy/early childhood — features were noted by approximately 18 months of age in the reported cases; congenital presence of some dysmorphic features (nose, thumbs) is implied but not explicitly staged as "present at birth" in the extracted material — flag for verification against the primary paper's exact wording before asserting congenital vs. early-postnatal onset in a curated `onset` field.

**Onset pattern:** Insidious/progressive rather than acute.

**Progression:** Clearly progressive in the one longitudinally followed patient (Family B, ages ~6 to ~15 years) — worsening growth failure (height z-score) and severe wasting (weight z-score reaching −8.47 by age 14). This is a meaningful, citable natural-history data point for a `progression` block.

**Disease stages:** No formal staging system exists (as expected for an ultra-rare, recently described Mendelian disorder).

**Disease course pattern:** Chronic, progressive, not episodic/relapsing-remitting based on available data.

**Disease duration:** Chronic, lifelong (no spontaneous remission reported; no natural death/mortality data reported in the retrieved sources — the oldest documented age at follow-up is 14 years 9 months, so **long-term/adult natural history and life expectancy are simply unknown** rather than favorable or unfavorable — an important honest gap for the Outcome/Prognosis section).

**Critical periods:** None specifically identified; by mechanistic inference, periods of rapid cell proliferation (early childhood growth, puberty) might be expected to be more vulnerable to replication-stress-driven phenotype worsening, but this is speculative and not directly evidenced.

---

## 9. Inheritance and Population

**Epidemiology:** Extremely rare — **only 3 individuals with confirmed genotype have ever been reported** (as of the most recent identified review, 2023), from 2 families, plus 2 additional clinically-similar but ungenotyped adult relatives in Family A. No formal prevalence or incidence estimate exists or is calculable; this is a "cases in literature" measure only (n≈3–5), not a population-based prevalence.

> "only 3 affected individuals have been identified, all with the same mutation" — PMC10018417 (review, paraphrased/quoted from WebFetch extraction).

**Inheritance pattern:** Autosomal recessive (biallelic requirement demonstrated by segregation: heterozygous unaffected parents, 8 unaffected heterozygous/WT siblings, homozygous affected probands).

**Penetrance:** Appears complete in the reported homozygotes (all 3 genotyped homozygotes were clinically affected), but the sample size (n=3) is far too small to make a confident penetrance claim — report as "apparently complete in reported cases, unconfirmed at scale" rather than "complete."

**Expressivity:** Variable in severity/timing even among identical-genotype patients — Family B's proband showed a more severe/progressive wasting phenotype (weight z-score −8.47) than described for Family A's patients, despite the identical p.A459S homozygous genotype, indicating variable expressivity (possible modifier-gene or environmental contribution, unstudied).

**Genetic anticipation:** Not applicable/not reported (not a repeat-expansion disorder).

**Germline mosaicism:** Not addressed in retrieved sources.

**Founder effects:** Strongly suspected but not explicitly proven by haplotype analysis in the material retrieved — the *identical* c.1375G>T variant occurring homozygously in two "apparently unrelated" Middle Eastern families is classically suggestive of a shared regional founder allele (or, less likely, a recurrent mutational hotspot). Flag this as an inference for curation notes rather than a stated fact unless the primary paper's haplotype data is separately confirmed.

**Consanguinity role:** Central — Family A are double first cousins; this is the expected mechanism for revealing a rare recessive allele. Family B's consanguinity status is less clear from the retrieved material and should be re-checked against the primary source.

**Carrier frequency:** Not calculable/not reported; the variant is absent from gnomAD and the GME Variome, so no meaningful population carrier-frequency estimate exists.

**Affected populations/geographic distribution:** Middle Eastern (2 families, both described as Middle Eastern in the primary report). No other ethnic/geographic groups reported.

**Sex ratio:** All 3 genotyped patients reported were female (both Family A patients are sisters; Family B's proband is also female per pronoun usage in the extraction — "her"/"girls" per the PubMed-search summary: "In 3 girls from 2 apparently unrelated Middle Eastern families"). With n=3, this could reflect ascertainment rather than a true sex-linked effect (the gene is autosomal, so no biological expectation of sex skew exists) — report the observed sex distribution but explicitly caveat that it is not evidence of sex-specific risk given the small, possibly ascertainment-biased sample.

**Age distribution:** Pediatric only in all reported cases (ages 4–15 years at various assessment points); no adult-onset or adult-diagnosed cases reported, consistent with a congenital/early-childhood-onset disorder, though this may also simply reflect that no adult patients have yet been identified given the extreme rarity and recency of description.

---

## 10. Diagnostics

**Clinical/laboratory tests:**
- Complete blood count — for thrombocytopenia/anemia (reported in at least one patient)
- No disease-specific biochemical/enzymatic biomarker exists; diagnosis is clinical-plus-molecular

**Genetic testing (primary diagnostic modality):**
- Single-gene *RECQL* sequencing or exome/genome sequencing is the de facto diagnostic approach, as demonstrated in both reported families (identified via presumably exome/targeted sequencing plus homozygosity mapping/linkage, given the LOD score reported for Family A).
- No dedicated commercial gene panel or GTR-listed test was specifically identified in this search, though *RECQL* would plausibly be captured on any broad "progeroid syndrome" or "genome instability disorder" NGS panel offered by clinical laboratories, and on exome/genome sequencing.
- Chromosomal microarray/karyotype: not specifically diagnostic (no gross chromosomal rearrangement reported), though may be used to exclude other progeroid-differential diagnoses.
- Cellular functional assays (SCE assay, chromosome breakage assay, replication-fork restart/DNA fiber assay) were used as **research-level confirmatory functional studies** in the primary report, not as established clinical diagnostic tests, and should not be represented as standard-of-care diagnostics.

**Imaging/functional/electrophysiology/biopsy:** None specifically reported as part of the diagnostic workup in the retrieved sources.

**Clinical diagnostic criteria:** No formal consensus clinical diagnostic criteria exist (as expected for a disorder with only 3 genotyped cases); diagnosis is currently definitionally molecular (biallelic *RECQL* pathogenic variant) plus compatible progeroid phenotype.

**Differential diagnosis** (by phenotypic overlap, from the comparison table constructed above and general RecQ-disorder knowledge):
- **Werner syndrome** (*WRN*, OMIM #277700) — progeroid facial features, short stature, but *adult*-onset with normal growth through the teenage years (contrasting with RECON's postnatal/childhood growth failure), and lacking RECON's prominent photosensitivity.
- **Bloom syndrome** (*BLM*, OMIM #210900) — photosensitivity and growth retardation overlap, but Bloom syndrome features microcephaly, immunodeficiency, strong cancer predisposition, and a markedly elevated SCE rate (a diagnostic hallmark), which is only mildly elevated in RECON syndrome — an important distinguishing cellular finding.
- **Rothmund-Thomson syndrome / RAPADILINO / Baller-Gerold syndrome** (*RECQL4*, OMIM #268400 / #266280 / #218600) — skeletal abnormalities (radial ray defects), poikiloderma, and cancer predisposition (osteosarcoma) are more prominent than in RECON syndrome; RECON lacks the major skeletal malformations of the RECQL4 disorders.
- Other progeroid/genome-instability syndromes not directly compared in the retrieved sources but relevant by general category: Cockayne syndrome, Hutchinson-Gilford progeria syndrome (LMNA), ataxia-telangiectasia-like disorder (used as a chromosome-breakage comparator cell line in the primary paper, not a clinical differential per se).

**Screening:** No newborn-screening, carrier-screening, or population-screening program exists or would be expected for a disease this rare with only one known recurrent variant confined to specific consanguineous Middle Eastern families; targeted carrier testing within affected families/populations would be the only currently plausible screening approach.

---

## 11. Outcome/Prognosis

**Survival/mortality:** No mortality data reported; oldest documented follow-up age is 14 years 9 months (Family B proband). Long-term survival, life expectancy, and adult natural history are **unknown** — this must be represented as a genuine evidence gap, not inferred from the (unrelated in mechanism) more severe adult progeroid syndromes.

**Morbidity/function:** Progressive growth failure and wasting (documented longitudinally in one patient); no formal disability, quality-of-life, or functional-outcome instrument data reported.

**Disease course:** Chronic and progressive based on the single longitudinal case; no remission reported.

**Complications:** Thrombocytopenia, anemia, and recurrent chest infections reported in the more severely affected/longer-followed patient (Family B) — whether these represent genuine downstream complications of the core genome-instability mechanism or incidental findings is not established.

**Prognostic factors:** None formally identified (sample size precludes statistical prognostic-factor analysis). By observation, the degree of wasting/growth failure appears to progress with age in the one followed patient, suggesting age/disease-duration itself may correlate with severity, but this is a single-patient observation, not a validated prognostic factor.

**Cancer risk:** Unclear/unestablished for the biallelic RECON phenotype specifically. This should be explicitly distinguished in curation from the *separate, heterozygous* RECQL-breast-cancer-susceptibility literature (Section 2 lump/split note) — no cancer cases have been reported among the RECON-syndrome homozygotes or their heterozygous-carrier relatives in the retrieved sources, but the patient cohort is small and young, so absence of observed cancer is not strong evidence of absent risk.

---

## 12. Treatment

**No disease-specific, mechanism-targeted, or disease-modifying therapy has been reported or trialed for RECON syndrome.** This is expected given the disease was described in 2022 with only 3 genotyped patients; no clinical trials (searched ClinicalTrials.gov context indirectly via search — none surfaced), no FDA-approved indication, and no gene/cell/RNA therapy program were identified.

**Supportive care (inferred/by extrapolation from phenotype, not explicitly trialed in the source literature):**
- Photoprotection (sun avoidance, broad-spectrum sunscreen, protective clothing) for cutaneous photosensitivity — standard supportive dermatologic management by analogy to other photosensitive genome-instability disorders; suggested NCIT term (lead only): a general "Sun Protection"/dermatologic-supportive-care concept, no specific NCIT code identified in this search and should be looked up during curation rather than guessed.
- Emollients for xeroderma — general dermatologic supportive care.
- Nutritional support for severe growth failure/wasting — general supportive/dietary intervention (`NCIT:C15447` Dietary Intervention is a plausible generic bind, but must be verified, not asserted here).
- Monitoring for cytopenias/infection given the thrombocytopenia/anemia/recurrent-infection findings in one patient — routine hematologic surveillance, not a formal published protocol.

**Explicitly note in curation:** the primary source states "No specific therapeutic interventions documented in this research article" — this is a molecular/mechanistic discovery paper, not a clinical-management study, so a dismech `treatments:` block for this entry should be sparse and clearly labeled as extrapolated supportive care rather than evidence-based disease-specific therapy, or left largely empty with a `notes:` explanation of why.

---

## 13. Prevention

No primary, secondary, or tertiary prevention strategy is established. Given the autosomal recessive inheritance and known consanguineous/founder context in the reported families, **genetic counseling** for at-risk consanguineous families/relatives of known carriers (recurrence risk 25% for full siblings of an affected homozygote, given two heterozygous-carrier parents) is the only currently applicable prevention-adjacent intervention, plus carrier testing and reproductive options (e.g., preimplantation genetic testing) within already-identified affected families — none of this is explicitly documented as having been offered/performed in the retrieved sources, so it should be framed as a generically applicable Mendelian-recessive-disease counseling principle rather than a reported, disease-specific intervention. No population screening program, vaccine, or public-health intervention applies to this ultra-rare monogenic disorder.

---

## 14. Other Species / Natural Disease

**Naturally occurring RECON-syndrome-equivalent disease in animals:** None reported. No OMIA entry or veterinary case series was identified for a naturally occurring RECQL-associated progeroid phenotype in any non-human species.

**Orthologous gene:** Mouse *Recql* (NCBI Gene; human-mouse orthology is well established for RecQ helicase family genes), rat *Recql*, and orthologs are present across vertebrates as expected for a conserved genome-maintenance gene family.

**Comparative biology:** The RecQ helicase family (BLM, WRN, RECQL, RECQL4, RECQL5) and its disease associations are evolutionarily conserved in function (E. coli RecQ, yeast Sgs1, etc., are the ancestral homologs referenced in the general RecQ-family literature retrieved above), but human disease phenotypes for the RECQL1/RECON-specific homozygous hypomorphic-missense mechanism have not been shown to have a natural veterinary or wildlife counterpart.

---

## 15. Model Organisms

**Mouse:** *Recql*-knockout mice are reported as **phenotypically grossly normal** at the whole-organism level — a notable and important contrast to the human progeroid phenotype:

> "Mice devoid of this enzyme are phenotypically normal" (as extracted from PMC8884905), despite showing clear cellular abnormalities.

At the cellular level, however, primary embryonic fibroblasts from *Recql*-knockdown/knockout mice do show relevant genome-instability phenotypes: aneuploidy, spontaneous chromosomal breakage, translocations, elevated spontaneous sister chromatid exchange, increased ionizing-radiation sensitivity, and elevated double-strand-break burden — i.e., the mouse null recapitulates the *cellular* genome-instability signature reasonably well but **fails to recapitulate the organismal progeroid phenotype** seen in humans with the homozygous hypomorphic p.A459S variant.

**Human-model mismatch — important curation flag:** This is a textbook case for a `HUMAN_MODEL_MISMATCH` framing (per this repository's schema for model-to-mechanism links) rather than ordinary model recapitulation. Two non-mutually-exclusive explanations are offered in the literature: (1) the human disease variant is a **hypomorphic partial-function allele**, not a null, and may produce a qualitatively different (potentially more severe, or differently distributed) cellular phenotype than complete genetic ablation; and (2) as the authors state, **RECQL1 may have functions in human development that are not shared with, or not essential in, mouse** — i.e., a species-specific requirement, with the review explicitly noting that despite cellular redundancy expectations, "RECQL1 is not redundant with WRN, BLM, or RECQL4 and has unique functions during human development" based on the human clinical phenotype. Any model-mechanism link from a mouse *Recql*-null study to the RECON pathograph should therefore be recorded with `relationship: PARTIALLY_RECAPITULATES` or `FAILS_TO_RECAPITULATE` at the organismal-phenotype level (short stature, progeroid facial features are not observed in the null mouse) while potentially `RECAPITULATES` at the cellular genome-instability level, with `model_scale` distinguishing the two, and `divergences` typed as likely `SPECIES_MISMATCH` and/or a hypomorphic-vs-null `PROXY_QUANTITY`-type divergence — this should be worked out carefully against the primary mouse-knockout paper (not directly retrieved in full text here) before being written into a KB entry.

**Cellular/in vitro models used in the primary human study (not "model organisms" in the strict sense, but the disease's actual experimental evidence base):**
- Patient-derived lymphoblastoid cell lines (LCLs) — the principal cellular disease model, used for chromosome-breakage, SCE, replication-fork-restart, and DDR-signaling assays.
- Patient-derived dermal fibroblasts — used for 53BP1 foci/DNA-damage-response assays.
- Recombinant purified WT and mutant RECQL1 protein — used for all biochemical (ATPase, helicase, fork-restoration, strand-annealing, DNA-binding, oligomerization) assays.
- Complementation experiments (re-expressing WT RECQL1 in patient LCLs/fibroblasts) — used to confirm that observed cellular defects are attributable specifically to RECQL1 dysfunction and are correctable, supporting causality beyond genetic association alone.

**No zebrafish, Drosophila, C. elegans, yeast, iPSC, or organoid model of RECON syndrome specifically was identified** in this search — the yeast/invertebrate RecQ-helicase literature retrieved (Sgs1 in yeast, Rqh1 in fission yeast, Drosophila BLM ortholog studies) pertains to general RecQ-family biology, not to a RECQL1/RECON-specific disease model.

---

## Summary of Key Evidence Gaps for Curation

1. **No ORPHA code located** — confirm this is a genuine coverage gap rather than a search miss before curating `mappings.mondo_mappings`/cross-references.
2. **GenCC/ClinGen "Disputed Evidence"** classification exists — represent gene-disease validity honestly as limited, not definitive.
3. **No long-term natural history data** (oldest patient documented to age ~15) — do not extrapolate adult prognosis/mortality from other, mechanistically-related but genetically-distinct progeroid syndromes (Werner, Bloom).
4. **Keep the biallelic RECON-syndrome entry structurally separate** from the monoallelic *RECQL* breast-cancer-susceptibility literature — different zygosity, variant class, and phenotype (see Section 2).
5. **Mouse knockout model is a phenotype mismatch at the organismal level** — flag explicitly rather than treating as a validating animal model of the human disease (Section 15).
6. **Microcephaly** appears in MedGen's phenotype list but was not emphasized as present in the WebFetch-extracted clinical description of the primary paper — verify directly against PMID:35025765 full text before including/excluding in a curated phenotype list.
7. **Formal onset staging** (congenital vs. ~18-month postnatal onset) should be re-verified against exact wording in the primary source before populating an `onset` field.

---

### Sources

- [RECON syndrome is a genome instability disorder caused by mutations in the DNA helicase RECQL1 — PMC8884905](https://pmc.ncbi.nlm.nih.gov/articles/PMC8884905/) (primary report; PMID:35025765; J Clin Invest 2022)
- [RECON syndrome is a genome instability disorder caused by mutations in the DNA helicase RECQL1 — PubMed](https://pubmed.ncbi.nlm.nih.gov/35025765/)
- [JCI full article](https://www.jci.org/articles/view/147301)
- [Entry - #620370 - RECON PROGEROID SYNDROME — OMIM](https://omim.org/entry/620370)
- [Entry - *600537 - RECQ PROTEIN-LIKE; RECQL — OMIM](https://omim.org/entry/600537)
- [RECON progeroid syndrome (Concept ID: C5830504) — MedGen/NCBI](https://ncbi.nlm.nih.gov/medgen/1841140)
- [Recon Progeroid Syndrome — MalaCards](https://www.malacards.org/card/recon_progeroid_syndrome)
- [RECON progeroid syndrome — UniProt Diseases (DI-06683)](https://www.uniprot.org/diseases/DI-06683)
- [Discovery of a new hereditary RECQ helicase disorder RECON syndrome positions the replication stress response and genome homeostasis as centrally important processes in aging and age-related disease — PMC10018417](https://pmc.ncbi.nlm.nih.gov/articles/PMC10018417/)
- [RECQL gene with submissions organized by classifications — GenCC](https://search.thegencc.org/genes/HGNC:9948)
- [RECQL Gene — GeneCards](https://www.genecards.org/cgi-bin/carddisp.pl?gene=RECQL)
- [Germline RECQL mutations are associated with breast cancer susceptibility — PubMed (PMID:25915596)](https://pubmed.ncbi.nlm.nih.gov/25915596/)
- [RECQ1 Promotes Stress Resistance and DNA Replication Progression Through PARP1 Signaling Pathway in Glioblastoma — PMC8350743](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8350743/)
- [Human RecQ Helicases in DNA Double-Strand Break Repair — PMC7947261](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7947261/)
- [RECQL4 — Wikipedia](https://en.wikipedia.org/wiki/RECQL4) (comparator disorder background)
- Frontiers Pediatrics case report (10.3389/fped.2026.1695356) — checked and confirmed **not relevant** to RECON syndrome (it concerns RECQL4/Rothmund-Thomson type 2, a distinct gene and disease; included here only to document that this search lead was checked and excluded).

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 7 |
| On topic | 4 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:36907310` (1 mention) - Mitochondrial targeted fluorescent nitrite peroxide probe for dynamic monitoring of cellular lung injury.
  - shared terms: cellular

Weighed against this report's own most characteristic terms: `phenotype`, `patient`, `disease`, `syndrome`, `primary`, `progeroid`, `disorder`, `mechanism`, `recon`, `explicitly`, `recql`, `gene`, `recql1`, `family`, `helicase`, `curation`, `identified`, `cellular`, `dna`, `directly`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 44 |
| Resolved | 41 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 1 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0957266` (2 mentions) - the report calls it "MONDO"; MONDO calls it **RECON progeroid syndrome**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0009062` (obsolete Infantile axial hypotonia) (1 mention) - replaced by `HP:0008936`
- `GO:0000784` (GO_0000784) (1 mention) - replaced by `GO:0000781`