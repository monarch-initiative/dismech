---
provider: claude_code
model: claude-fable-5-1, claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-09-28T03:37:01.514416'
end_time: '2026-09-28T03:46:36.904977'
duration_seconds: 575.39
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Astrakhan spotted fever
  mondo_id: MONDO:0024473
  category: Infectious Disease
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
  - claude-fable-5-1
  - claude-haiku-4-5-20251001
  - claude-opus-5
  web_search_requests: 8
  num_turns: 66
  total_cost_usd: 6.314647750000002
  session_id: 5c6b1f79-6110-4c8f-abca-82b0788cfdf8
  stop_reason: end_turn
  assistant_text_blocks: 6
citation_count: 16
reference_validation:
  total_references: 38
  verified: 38
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 31
  quotes_valid: 25
  quotes_unsupported: 6
  unsupported_quote_references:
  - PMID:16223955
  - PMID:12498120
  quotes_not_checkable: 2
  relevance_assessed: 38
  on_topic: 19
  needs_review: true
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 54
  verified: 53
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 8
  labels_matching: 2
  labels_mismatched: 6
  mislabelled_terms:
  - term_id: MONDO:0024473
    reported_labels:
    - Monarch
    ontology_label: Astrakhan spotted fever
  - term_id: DOID:0050041
    reported_labels:
    - DOID
    ontology_label: Astrakhan spotted fever
  - term_id: NCBITaxon:302011
    reported_labels:
    - caspia
    ontology_label: Rickettsia conorii subsp. caspia
  - term_id: CHEBI:50845
    reported_labels:
    - First line
    ontology_label: doxycycline
  - term_id: CHEBI:28077
    reported_labels:
    - Used in Russian series, less effective than doxycycline
    ontology_label: rifampicin
  - term_id: CHEBI:17698
    reported_labels:
    - Historical alternative for SFG rickettsioses
    ontology_label: chloramphenicol
  unresolvable_prefixes:
  - GARD
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Astrakhan spotted fever
- **MONDO ID:** MONDO:0024473 (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Astrakhan spotted fever** covering all of the
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

I'll research Astrakhan spotted fever using web search and PubMed, then write the full report inline.

Independent lookups I need now: PubMed hits for the disease and its agent, the taxonomy paper, MONDO/Orphanet identifiers, and vector/epidemiology sources. Firing them together.

Retrying the two interrupted abstract fetches and running the ontology cache lookups in simpler form.

One last lookup, the Karachay-Cherkessia tick study abstract, and then I'll write the report.

# Astrakhan Spotted Fever: Disease Characteristics Research Report

**Target:** Astrakhan spotted fever (MONDO:0024473) · Category: Infectious Disease · Report date: 2026-09-28

**Scope note on sources.** Astrakhan spotted fever (ASF) has a small literature, much of it Russian-language with English abstracts only. The surveillance numbers below come from one 1983–1988 prospective series (as summarized in the Parola 2005 review), one 2000–2020 registry summary (a 2021 conference abstract), and a 2022 serology study that quotes official annual counts. Quotations marked *verbatim* were copied from PubMed abstracts retrieved during this research; figures attributed to the 2024 China letter and the 2021 IJID abstract were read from indexed summaries because the publisher pages were paywalled, and should be re-verified against the full text before being used as evidence snippets.

---

## 1. Disease Information

**Overview.** Astrakhan spotted fever is a tick-borne spotted-fever-group (SFG) rickettsiosis caused by *Rickettsia conorii* subsp. *caspia*, a member of the *R. conorii* complex. It is endemic to the lower Volga delta and Caspian littoral (Astrakhan oblast and Kalmykia, Russia), transmitted chiefly by *Rhipicephalus pumilio* and the brown dog tick *Rhipicephalus sanguineus*, and presents as a summer febrile exanthem that resembles Mediterranean spotted fever (MSF) but with a notably lower frequency of inoculation eschar. The Kosovo tick study describes it as "a summer spotted fever resembling Mediterranean spotted fever, endemic in Astrakhan, a region of Russia located by the Caspian sea" (*verbatim*, PMID:12860620).

The disease was first noticed in the 1970s as a "viral exanthema of unknown etiology" and shown to be a rickettsiosis in the early 1990s: "The acute febrile disease with characteristic rash seen in Astrakhan region and named as 'viral exanthema of unknown etiology' was proved to be a spotted fever group rickettsiosis" (*verbatim*, Tarasevich 1991, PMID:1884783). Russian surveillance dates recognition to 1983: "Astrakhan spotted fever, caused by R. conorii subsp. caspia has been recognized since 1983" (*verbatim*, Tarasevich 2006, PMID:17114680).

**Identifiers**

| Resource | Identifier | Source |
|---|---|---|
| MONDO | MONDO:0024473 "Astrakhan spotted fever" | Monarch API (parent MONDO:0005677, *Rickettsia conorii* infectious disease) |
| DOID | DOID:0050041 | MONDO xref via Monarch |
| GARD | GARD:0025401 | MONDO xref via Monarch |
| MedGen / UMLS | MedGen 1814171 / UMLS C5574872 | MONDO xref via Monarch |
| Orphanet | No ORPHA xref present on the MONDO record | Monarch API |
| OMIM | Not applicable (infectious disease) | — |
| ICD-10 | A77.1 "Spotted fever due to *Rickettsia conorii*" is the applicable parent code; no ASF-specific code exists | Not verified against WHO this session; treat as a lead |
| MeSH | No dedicated descriptor found; indexed under "Boutonneuse Fever" / "Rickettsia Infections" | Inferred from PubMed indexing of the retrieved records |
| NCBI Taxonomy (agent) | NCBITaxon:302011 *Rickettsia conorii* subsp. *caspia* (rank: subspecies) | NCBI esummary |
| NCBI Taxonomy (parent species) | NCBITaxon:781 *Rickettsia conorii* | repo cache + NCBI |

**Synonyms:** Astrakhan fever; Astrakhan rickettsial fever (ARF, used by Russian and Chinese authors); Astrakhan fever rickettsiosis; historically "viral exanthema of unknown etiology" (Astrakhan). Agent synonyms: Astrakhan fever rickettsia (AFR); *R. conorii* Astrakhan strain; type strain A-167.

**Nature of the information.** All data are aggregated disease-level resources and case series, not individual EHR records.

---

## 2. Etiology

**Causal factor.** Infection with *R. conorii* subsp. *caspia* following the bite of an infected *Rhipicephalus* tick. Taxonomy: Zhu et al. (2005) proposed "R. conorii subspecies caspia subsp. nov. (type strain = A-167)" on the basis of multilocus sequence typing, multi-spacer typing and mouse serotyping, noting that "strains within the R. conorii species show MST genotypic, serotypic, and epidemio-clinical dissimilarities" (*verbatim*, PMID:15766388). Earlier work had found the agent antigenically indistinguishable from the Israeli spotted fever rickettsia: "Astrakhan fever rickettsiae were found to be serologically and antigenically similar to Israeli spotted fever rickettsiae. Both of them probably belong to a single Rickettsia conorii pathotype complex. Only PFGE pattern analysis could clearly discriminate Astrakhan fever rickettsiae from other isolates" (*verbatim*, Eremeeva 1994, PMID:7985764; see also Drancourt 1992, PMID:1583342, a letter titled "Astrakhan fever rickettsia is identical to Israel tick typhus rickettsia").

**Risk factors (environmental / behavioural).**
- **Tick exposure and dog contact.** In the 1983–1988 series, "Most of the patients had dogs and reported having contact with *Rhipicephalus sanguineus* dog ticks" (Parola 2005 review, PMID:16223955, summarizing Tarasevich). Tarasevich (1991) detected SFG rickettsiae "in 8 of 104 Rhipicephalus sanguineus ticks removed from dogs" (*verbatim*, PMID:1884783).
- **Season.** 85% of cases occurred in summer, 43% in August alone (PMID:16223955). The 2019 serology cohort was collected May–October (PMID:35467375); the four Chinese cases all began in July 2023 (PMID:38462076).
- **Rural residence in the Volga delta / Caspian steppe.** Early cases were "in patients of rural areas" (PMID:16223955). The 2021 registry abstract reports spread from Astrakhan city plus 3 districts in 1993 to all 11 districts of the oblast by 2013 (IJID 2021 abstract, PII S1201-9712(21)01194-2).
- **Age and sex.** Adults (94%) and males (61%) predominated in 1983–1988 (PMID:16223955). The 2019 cohort spanned ages 1–88 (mean 45) (PMC9241626).
- **Vector abundance.** The 2021 abstract states the rise in incidence "begins when the abundance index of R. pumilio ticks reaches its maximum" (indexed summary; verify against full text).

**Genetic risk / protective factors.** None reported for ASF. No GWAS, ClinVar, or ClinGen data exist. This is expected for an acute zoonotic infection.

**Protective factors.** Tick avoidance and prompt tick removal (generic to SFG rickettsioses; CDC 2016 guidance, PMID:27172113). No vaccine exists (PMID:24059918: "No suitable vaccines for human use are currently available to prevent rickettsial diseases", *verbatim*).

**Gene–environment interactions.** Not studied.

---

## 3. Phenotypes

Frequencies are from the 1983–1988 prospective series of 321 cases (as summarized in PMID:16223955) unless stated otherwise. HPO identifiers below were read from the repository's HP term cache (`cache/hp/terms.csv`) during this session.

| Phenotype | Type | Frequency | Onset / course | HPO suggestion |
|---|---|---|---|---|
| Fever, high (39–40 °C), prolonged | Sign | 94% | Acute, sustained over days to ~2 weeks | HP:0001945 Fever |
| Maculopapular rash, disseminated, may be roseolous-papular-hemorrhagic | Sign | 94% (with fever) | Appears early, generalized incl. extremities | HP:0040186 Maculopapular exanthema; HP:0000988 Skin rash |
| Hemorrhagic/petechial component of rash | Sign | Reported ("papular-hemorrhagic", PMID:9324803); % not given | — | HP:0000967 Petechiae |
| Inoculation eschar (tache noire), usually single | Sign | 23% | At bite site, precedes fever | HP:0200042 Skin ulcer (closest available; no HPO eschar term) |
| Conjunctivitis | Sign | 32% | Early | HP:0000509 Conjunctivitis |
| Regional lymphadenitis / adenopathy | Sign | Reported; % not given | Early, near bite site | HP:0002716 Lymphadenopathy |
| Hepatomegaly | Sign | Reported; % not given | — | HP:0002240 Hepatomegaly |
| Arterial hypotension | Sign | Reported; % not given | Acute phase | HP:0002615 Hypotension |
| "Intoxication" (malaise, headache, myalgia) | Symptom | Reported qualitatively | Acute phase | HP:0012378 Fatigue; HP:0002315 Headache; HP:0003326 Myalgia |
| Chills | Symptom | Typical of SFG rickettsioses; not quantified for ASF | — | HP:0025143 Chills |
| Transient T- and B-lymphocyte suppression | Laboratory | Observed in 75 patients | 2 weeks (moderate) / 3 weeks (severe) | No specific HPO term; describe in `biochemical:` |

Supporting quotes (*verbatim*):
- "The disease presented with long-term fever (body temperature 39-40 degrees C), intoxication, conjunctivitis, hepatomegaly, regional lymphadenitis, disseminated roseolous papular-hemorrhagic rash, arterial hypotension." (Galimzianov 1996, PMID:9324803)
- "the

# Astrakhan Spotted Fever: Disease Characteristics Research Report

**Target:** Astrakhan spotted fever (MONDO:0024473) · Category: Infectious Disease · Report date: 2026-09-28

**Scope note on sources.** Astrakhan spotted fever (ASF) has a small literature, much of it Russian-language with English abstracts only. The surveillance numbers below come from one 1983–1988 prospective series (as summarized in the Parola 2005 review), one 2000–2020 registry summary (a 2021 conference abstract), and a 2022 serology study that quotes official annual counts. Quotations marked *verbatim* were copied from PubMed abstracts retrieved during this research; figures attributed to the 2024 China letter and the 2021 IJID abstract were read from indexed summaries because the publisher pages were paywalled, and should be re-verified against the full text before being used as evidence snippets.

---

## 1. Disease Information

**Overview.** Astrakhan spotted fever is a tick-borne spotted-fever-group (SFG) rickettsiosis caused by *Rickettsia conorii* subsp. *caspia*, a member of the *R. conorii* complex. It is endemic to the lower Volga delta and Caspian littoral (Astrakhan oblast and Kalmykia, Russia), transmitted chiefly by *Rhipicephalus pumilio* and the brown dog tick *Rhipicephalus sanguineus*, and presents as a summer febrile exanthem that resembles Mediterranean spotted fever (MSF) but with a notably lower frequency of inoculation eschar. The Kosovo tick study describes it as "a summer spotted fever resembling Mediterranean spotted fever, endemic in Astrakhan, a region of Russia located by the Caspian sea" (*verbatim*, PMID:12860620).

The disease was first noticed in the 1970s as a "viral exanthema of unknown etiology" and shown to be a rickettsiosis in the early 1990s: "The acute febrile disease with characteristic rash seen in Astrakhan region and named as 'viral exanthema of unknown etiology' was proved to be a spotted fever group rickettsiosis" (*verbatim*, Tarasevich 1991, PMID:1884783). Russian surveillance dates recognition to 1983: "Astrakhan spotted fever, caused by R. conorii subsp. caspia has been recognized since 1983" (*verbatim*, Tarasevich 2006, PMID:17114680).

**Identifiers**

| Resource | Identifier | Source |
|---|---|---|
| MONDO | MONDO:0024473 "Astrakhan spotted fever" | Monarch API (parent MONDO:0005677, *Rickettsia conorii* infectious disease) |
| DOID | DOID:0050041 | MONDO xref via Monarch |
| GARD | GARD:0025401 | MONDO xref via Monarch |
| MedGen / UMLS | MedGen 1814171 / UMLS C5574872 | MONDO xref via Monarch |
| Orphanet | No ORPHA xref present on the MONDO record | Monarch API |
| OMIM | Not applicable (infectious disease) | — |
| ICD-10 | A77.1 "Spotted fever due to *Rickettsia conorii*" is the applicable parent code; no ASF-specific code exists | Not verified against WHO this session; treat as a lead |
| MeSH | No dedicated descriptor found; indexed under "Boutonneuse Fever" / "Rickettsia Infections" | Inferred from PubMed indexing of the retrieved records |
| NCBI Taxonomy (agent) | NCBITaxon:302011 *Rickettsia conorii* subsp. *caspia* (rank: subspecies) | NCBI esummary |
| NCBI Taxonomy (parent species) | NCBITaxon:781 *Rickettsia conorii* | repo cache + NCBI |

**Synonyms:** Astrakhan fever; Astrakhan rickettsial fever (ARF, used by Russian and Chinese authors); Astrakhan fever rickettsiosis; historically "viral exanthema of unknown etiology" (Astrakhan). Agent synonyms: Astrakhan fever rickettsia (AFR); *R. conorii* Astrakhan strain; type strain A-167.

**Nature of the information.** All data are aggregated disease-level resources and case series, not individual EHR records.

---

## 2. Etiology

**Causal factor.** Infection with *R. conorii* subsp. *caspia* following the bite of an infected *Rhipicephalus* tick. Taxonomy: Zhu et al. (2005) proposed "R. conorii subspecies caspia subsp. nov. (type strain = A-167)" on the basis of multilocus sequence typing, multi-spacer typing and mouse serotyping, noting that "strains within the R. conorii species show MST genotypic, serotypic, and epidemio-clinical dissimilarities" (*verbatim*, PMID:15766388). Earlier work had found the agent antigenically indistinguishable from the Israeli spotted fever rickettsia: "Astrakhan fever rickettsiae were found to be serologically and antigenically similar to Israeli spotted fever rickettsiae. Both of them probably belong to a single Rickettsia conorii pathotype complex. Only PFGE pattern analysis could clearly discriminate Astrakhan fever rickettsiae from other isolates" (*verbatim*, Eremeeva 1994, PMID:7985764; see also Drancourt 1992, PMID:1583342, a letter titled "Astrakhan fever rickettsia is identical to Israel tick typhus rickettsia").

**Risk factors (environmental / behavioural).**
- **Tick exposure and dog contact.** In the 1983–1988 series, "Most of the patients had dogs and reported having contact with *Rhipicephalus sanguineus* dog ticks" (Parola 2005 review, PMID:16223955, summarizing Tarasevich). Tarasevich (1991) detected SFG rickettsiae "in 8 of 104 Rhipicephalus sanguineus ticks removed from dogs" (*verbatim*, PMID:1884783).
- **Season.** 85% of cases occurred in summer, 43% in August alone (PMID:16223955). The 2019 serology cohort was collected May–October (PMID:35467375); the four Chinese cases all began in July 2023 (PMID:38462076).
- **Rural residence in the Volga delta / Caspian steppe.** Early cases were "in patients of rural areas" (PMID:16223955). The 2021 registry abstract reports spread from Astrakhan city plus 3 districts in 1993 to all 11 districts of the oblast by 2013 (IJID 2021 abstract, PII S1201-9712(21)01194-2).
- **Age and sex.** Adults (94%) and males (61%) predominated in 1983–1988 (PMID:16223955). The 2019 cohort spanned ages 1–88 (mean 45) (PMC9241626).
- **Vector abundance.** The 2021 abstract states the rise in incidence "begins when the abundance index of R. pumilio ticks reaches its maximum" (indexed summary; verify against full text).

**Genetic risk / protective factors.** None reported for ASF. No GWAS, ClinVar, or ClinGen data exist. This is expected for an acute zoonotic infection.

**Protective factors.** Tick avoidance and prompt tick removal (generic to SFG rickettsioses; CDC 2016 guidance, PMID:27172113). No vaccine exists (PMID:24059918: "No suitable vaccines for human use are currently available to prevent rickettsial diseases", *verbatim*).

**Gene–environment interactions.** Not studied.

---

## 3. Phenotypes

Frequencies are from the 1983–1988 prospective series of 321 cases (as summarized in PMID:16223955) unless stated otherwise. HPO identifiers below were read from the repository's HP term cache (`cache/hp/terms.csv`) during this session.

| Phenotype | Type | Frequency | Onset / course | HPO suggestion |
|---|---|---|---|---|
| Fever, high (39–40 °C), prolonged | Sign | 94% | Acute, sustained over days to ~2 weeks | HP:0001945 Fever |
| Maculopapular rash, disseminated, may be roseolous-papular-hemorrhagic | Sign | 94% (with fever) | Appears early, generalized incl. extremities | HP:0040186 Maculopapular exanthema; HP:0000988 Skin rash |
| Hemorrhagic/petechial component of rash | Sign | Reported ("papular-hemorrhagic", PMID:9324803); % not given | — | HP:0000967 Petechiae |
| Inoculation eschar (tache noire), usually single | Sign | 23% | At bite site, precedes fever | HP:0200042 Skin ulcer (closest available; no HPO eschar term) |
| Conjunctivitis | Sign | 32% | Early | HP:0000509 Conjunctivitis |
| Regional lymphadenitis / adenopathy | Sign | Reported; % not given | Early, near bite site | HP:0002716 Lymphadenopathy |
| Hepatomegaly | Sign | Reported; % not given | — | HP:0002240 Hepatomegaly |
| Arterial hypotension | Sign | Reported; % not given | Acute phase | HP:0002615 Hypotension |
| "Intoxication" (malaise, headache, myalgia) | Symptom | Reported qualitatively | Acute phase | HP:0012378 Fatigue; HP:0002315 Headache; HP:0003326 Myalgia |
| Chills | Symptom | Typical of SFG rickettsioses; not quantified for ASF | — | HP:0025143 Chills |
| Transient T- and B-lymphocyte suppression | Laboratory | Observed in 75 patients | 2 weeks (moderate) / 3 weeks (severe) | No specific HPO term; describe in `biochemical:` |

Supporting quotes (*verbatim*):
- "The disease presented with long-term fever (body temperature 39-40 degrees C), intoxication, conjunctivitis, hepatomegaly, regional lymphadenitis, disseminated roseolous papular-hemorrhagic rash, arterial hypotension." (Galimzianov 1996, PMID:9324803)
- "the presence of a tache noire was reported in only 23% of the patients" (Parola 2005, PMID:16223955).
- "Examination of immunocompetent cells has revealed suppression of T- and B-immunity for 2 weeks in moderate AF and 3 weeks in severe AF. The number of T-helpers was low for 3 weeks while of T-suppressors rose beginning from week 2." (Kasimova 2002, PMID:12498120)

**Distinguishing feature vs MSF.** The low eschar rate (23%) is the clinically important contrast with Mediterranean spotted fever, where the tache noire is usual. This shifts differential weight toward rash-plus-fever presentations without a findable bite site.

**Severity and quality of life.** Severe disease accounted for 5.3% of Russian cases and case fatality is stated as approximately 1–2%, with a first reported death in 2013 (figures cited in the 2024 China letter, PMID:38462076; read from indexed summaries, not the full text). No EQ-5D, SF-36 or PROMIS data exist for ASF; as a self-limited acute illness it has no documented chronic quality-of-life burden.

---

## 4. Genetic / Molecular Information

**Host genetics: not applicable.** ASF has no causal genes, pathogenic variants, modifier genes, epigenetic signature or chromosomal abnormality. No ClinVar, HGMD, gnomAD or DECIPHER content pertains.

**Pathogen genomics.** The genome of *R. conorii* subsp. *caspia* strain A-167 was sequenced in 2012 (Sentausa et al., PMID:22887666, J Bacteriol): draft genome of 1,260,331 bases in 25 contigs at ~20× coverage, "a total complement of 1,210 genes (1,636 open reading frames [ORFs])" (*verbatim*), 33% GC, deposited as GenBank **AJUR00000000**. Among predicted genes, "820 (67.8%) are complete genes, 229 (18.9%) are split into two to 12 ORFs, and 78 (6.5%) are present only as fragments" (*verbatim*) — the split/fragmented pattern is the genome-reduction signature typical of *Rickettsia*.

**Typing loci used for identification.** 16S rDNA, *gltA* (citrate synthase), *ompA* (rOmpA), *ompB*, *sca4*, and the 23S–5S intergenic spacer. Pairwise similarity across the four *R. conorii* subspecies ranged 98.2–100% depending on locus, with *ompA* and *ompB* the most discriminating (PMID:15766388). Historic methodology: Roux 1997 (*gltA*, PMID:9103608), Fournier 1998 (rOmpA, PMID:9734038), Roux 1995 (16S rDNA, PMID:8525055).

Suggested annotations: the surface adhesins rOmpA and rOmpB (UniProt *R. conorii* entries; Sca family autotransporters) and Sca2/RickA for actin-based motility are the functionally characterized proteins, all studied in *R. conorii* sensu lato rather than in subsp. *caspia* specifically.

---

## 5. Environmental Information

**Infectious agent.** *Rickettsia conorii* subsp. *caspia* (NCBITaxon:302011), an obligate intracellular Gram-negative alphaproteobacterium of the spotted fever group.

**Vectors.**
- *Rhipicephalus pumilio* (NCBITaxon:127007) — the principal Astrakhan vector; infection prevalence 3% in Astrakhan-region ticks: "Rh. pumilio from the Astrakhan region were infected with ... the Astrakhan fever agent (3%)" (*verbatim*, Rydkina 1999, PMID:10603217). The primary-lesion study attributes the bite to *R. pumilio* (PMID:9324803).
- *Rhipicephalus sanguineus* (NCBITaxon:34632), the brown dog tick — vector in Kosovo, France and Zambia; also implicated by dog contact in Astrakhan.

**Reservoirs and hosts.** Domestic dogs (*Canis lupus familiaris*, NCBITaxon:9615) are the principal tick host linking vector to humans. I found no published evidence for a hedgehog or rodent reservoir specific to *R. conorii* subsp. *caspia*; a Kazakhstan rodent survey detected *R. raoultii*, *R. slovaca* and *R. conorii* but did not report subsp. *caspia* in rodents (PMID:36050456).

**Geographic distribution beyond Astrakhan.**

| Location | Finding | Citation |
|---|---|---|
| Astrakhan oblast and Kalmykia, Russia | Endemic focus, Caspian/Volga delta | PMID:17114680; PMID:12860620 |
| Kosovo | Detected in 4 *R. sanguineus* (3 from dogs, 1 from a soldier); "Our study demonstrates, for the first time, the presence of Astrakhan fever rickettsia in ticks outside Russia" (*verbatim*) | PMID:12860620 |
| Chad | Isolate from a febrile traveller, 99.5–99.7% identical across 16S/*gltA*/*ompA*; "The Chad isolate should be considered a variant of Astrakhan fever rickettsia" (*verbatim*) | PMID:12860619 |
| Southern France | 9 of 22 household *R. sanguineus* positive, "marking the first documentation of this subspecies in France" (*verbatim*), in an urban family cluster also involving *R. massiliae* | PMID:23140893 |
| Zambia | One tick of 1,465 (0.06%); one of 1,254 *Rh. sanguineus* (0.07%) | PMID:28986641 |
| Kazakhstan | Reported as circulating, per secondary statement in a rodent survey; not detected by that study itself | PMID:36050456 |
| Xinjiang, China | Four laboratory-confirmed human cases, July 2023, first *R. conorii* subsp. *caspia* infections reported in East Asia; *Rh. sanguineus* and *Rh. pumilio* present at 1.7% and 0.6% prevalence | PMID:38462076 (read from indexed summaries) |

**Non-infectious environmental and lifestyle factors.** None established beyond outdoor/rural exposure, dog ownership and season. No toxicological (CTD, EPA) contribution.

---

## 6. Mechanism / Pathophysiology

**Important caveat.** No mechanistic study has been performed on *R. conorii* subsp. *caspia* itself apart from cell-culture growth experiments. The chain below is the established SFG rickettsiosis mechanism, documented mainly for *R. conorii* sensu lato and *R. rickettsii*, applied to ASF by subspecies membership. Every step from 3 onward should be curated as `directness: INDIRECT` for ASF, or cited to the pan-rickettsial reviews (Walker 2008, PMID:18414502; Sahni 2013, PMID:24059918) with `evidence_source: OTHER` or `IN_VITRO` as appropriate. The two ASF-specific mechanistic observations are the primary-lesion histology (PMID:9324803) and the cytokine/cellular-immunity studies (PMID:12459842, PMID:12498120).

**Ordered causal chain**

1. An infected *Rhipicephalus pumilio* or *Rh. sanguineus* nymph or adult attaches and feeds on human skin, **which leads to** inoculation of *R. conorii* subsp. *caspia* into the dermis with tick saliva. *(Demonstrated for ASF by vector isolation and bite-site histology, PMID:9324803, PMID:7985764.)*
2. Local replication in the dermis **results in** a focal necrotizing lesion at the bite site, the primary affect or tache noire, with regional lymphatic drainage **leading to** regional lymphadenitis. *(ASF-specific: PMID:9324803. Note this step completes in only ~23% of ASF patients, PMID:16223955 — a genuine branch point, and an unexplained one.)*
3. Rickettsiae adhere to and invade vascular endothelial cells via Sca-family outer-membrane adhesins (rOmpA/rOmpB) engaging host receptors, **which results in** induced-phagocytosis entry. *(Pan-rickettsial; Walker 2008, PMID:18414502; Sahni 2013, PMID:24059918. Inferred for subsp. caspia.)*
4. Phagosomal escape into the cytosol **leads to** intracytoplasmic replication and actin-based motility, **which results in** cell-to-cell spread without extracellular exposure. *(Pan-rickettsial; Sahni 2013 names "intracytoplasmic niche within the host cell, predilection for infection of microvascular endothelium in mammalian hosts" (verbatim) and "motility" among the field's characterized mechanisms.)*
5. Haematogenous and lymphatic dissemination **leads to** multifocal infection of microvascular endothelium in skin, liver, lymph node and other organs.
6. Endothelial infection **results in** endothelial activation, cytokine release (IL-1, TNF) and leukocyte recruitment. *(ASF-supporting: "Comparative study of interleukin-1 and tumor necrosis factor production under conditions of experimental rickettsial infection caused by agents of Astrakhan spotted fever and North Asian scrub typhus showed that therapy with galavit reduced manifestations of the disease, decreased mortality of experimental animals, and decreased the concentrations of interleukin-1 and tumor necrosis factor to normal values" — verbatim, PMID:12459842, evidence_source MODEL_ORGANISM.)*
7. **Branch A — cutaneous.** Dermal microvascular injury and perivascular lymphohistiocytic infiltration **produce** the disseminated maculopapular and, where injury is greater, petechial/hemorrhagic rash. *(ASF: PMID:9324803.)*
8. **Branch B — systemic.** Widespread endothelial injury with increased vascular permeability **leads to** hypotension, and in a minority **to** severe multi-organ disease. *(ASF: arterial hypotension, PMID:9324803; severe disease 5.3%, PMID:38462076 as indexed.)*
9. **Branch C — hepatic/reticuloendothelial.** Infection of hepatic and splenic microvasculature and reticuloendothelial activation **result in** hepatomegaly. *(ASF: PMID:9324803.)*
10. **Branch D — immunological.** Acute infection **is accompanied by** transient suppression of T- and B-cell compartments lasting 2 weeks in moderate and 3 weeks in severe disease, with depressed T-helper numbers and a persistently low helper/suppressor index. *(ASF-specific human data, PMID:12498120.)*
11. Effective antirickettsial therapy (doxycycline) **arrests** intracellular replication, **leading to** defervescence and resolution; in its absence severe disease and death occur in a small fraction.

**Ontology suggestions** (identifiers verified against the repository term caches this session)

| Concept | Term |
|---|---|
| Host-cell invasion by the bacterium | GO:0046718 symbiont entry into host cell |
| Inflammatory response | GO:0006954 inflammatory response |
| Innate immune response | GO:0045087 innate immune response |
| Cytokine production | GO:0001816 cytokine production |
| IL-1 production | GO:0032612 interleukin-1 production |
| TNF production | GO:0032640 tumor necrosis factor production |
| Response to bacterium | GO:0009617 response to bacterium |
| Apoptosis (endothelial) | GO:0006915 apoptotic process |
| Coagulation activation | GO:0007596 blood coagulation |
| Primary target cell | CL:0000115 endothelial cell; CL:0000071 blood vessel endothelial cell; CL:0002139 endothelial cell of vascular tree |
| Recruited cells | CL:0000775 neutrophil; CL:0000235 macrophage; CL:0000576 monocyte |

**Molecular profiling.** No transcriptomic, proteomic, metabolomic, lipidomic, single-cell or spatial data exist for ASF. No GEO, PRIDE, MetaboLights or DepMap datasets were found for *R. conorii* subsp. *caspia*. This is a real and total gap, not an omission of this report.

---

## 7. Anatomical Structures Affected

- **Primary target tissue:** vascular endothelium of the microcirculation — UBERON:0001981 blood vessel; cell type CL:0000115 endothelial cell.
- **Skin:** the bite-site primary lesion and the generalized exanthem — UBERON:0002097 skin of body; UBERON:0002067 dermis.
- **Lymphatic:** regional lymphadenitis draining the bite site — UBERON:0000029 lymph node.
- **Liver:** hepatomegaly — UBERON:0002107 liver. Spleen involvement (UBERON:0002106) is plausible by analogy with MSF but was not named in the ASF abstracts retrieved.
- **Eye:** conjunctivitis in 32% — UBERON:0001811 conjunctiva.
- **Body systems:** cardiovascular (primary), integumentary, lymphatic/immune, hepatobiliary.
- **Subcellular:** the bacterium occupies the host cytosol (GO:0005829 cytosol) after phagosomal escape; no organelle-specific pathology is described.
- **Lateralization:** the eschar and its regional adenopathy are unilateral, at the bite site; the exanthem is bilateral and generalized, described as involving the extremities.

---

## 8. Temporal Development

- **Onset:** acute, in previously healthy adults of any age (1–88 years in the 2019 cohort, mean 45; PMC9241626). No congenital or pediatric-specific form. 94% of the historical series were adults.
- **Incubation:** not stated in the ASF abstracts retrieved; SFG rickettsioses generally run 2–14 days from tick bite. Treat as unverified for ASF.
- **Course:** a self-limited acute febrile illness of roughly 1–2 weeks with treatment. Fever is described as "long-term" at 39–40 °C (PMID:9324803). The primary lesion precedes or accompanies fever onset where present.
- **Stages:** no formal staging system exists. Severity is graded clinically as moderate versus severe in the Russian literature (63 moderate vs 12 severe of 75 patients, PMID:12498120).
- **Immunological recovery lags clinical recovery:** lymphocyte suppression persists 2–3 weeks and the helper/suppressor index "remains low till the end of the disease" (*verbatim*, PMID:12498120).
- **Critical intervention window:** early empiric doxycycline. The CDC states this generally for tickborne rickettsial disease: "early empiric antibacterial therapy can prevent severe disease and death" (*verbatim*, PMID:27172113).
- **Chronicity / relapse:** no chronic or relapsing form is reported. Serological IgM and IgA are detectable from day 1 to day 16 of illness (PMC9241626).

---

## 9. Inheritance and Population

**Inheritance:** not applicable. ASF is an acquired infection with no heritable component, no penetrance/expressivity/anticipation/mosaicism/founder-effect/carrier-frequency parameters.

**Epidemiology**

| Measure | Value | Source |
|---|---|---|
| Registered cases, Astrakhan region, 2000–2020 | 4,894 | IJID 2021 abstract, PII S1201-9712(21)01194-2 (indexed summary) |
| Average long-term incidence, Astrakhan region | 23.18 ± 1.5 per 100,000 population | Same |
| Annual national cases, Russia | ~200–300 | PMC9241626 |
| Cases by year (Russia) | 295 (2014), 314 (2015), 299 (2016), 176 (2017), 290 (2018) | PMC9241626 |
| Severe disease fraction | 5.3% | Cited in PMID:38462076 (indexed summary) |
| Case fatality | ~1–2%; first reported death 2013 | Cited in PMID:38462076 (indexed summary) |
| Seroprevalence, healthy residents of endemic areas (1991) | 5.1% of 429 sera positive at titre 20–40 | PMID:1884783 (*verbatim*) |

For dismech `Prevalence` records, the 23.18 per 100,000 figure is a regional `ANNUAL_INCIDENCE` averaged over 2000–2020 and needs `rate_denominator: POPULATION_PER_YEAR`; the ~200–300 national annual counts are `CASES_IN_LITERATURE`-adjacent registry counts, not a rate.

**Demographics.** Male predominance (61%) and adult predominance (94%) in the 1983–1988 series (PMID:16223955) most plausibly reflect exposure rather than susceptibility. Sex ratio ≈ 1.6:1 male:female.

**Geographic trend.** Endemic area expanded within Astrakhan oblast from the city plus 3 districts (1993) to 9 rural districts plus the city (1999) to all 11 districts (2013), with incidence peaks in 2000, 2002, 2005–2007 and a maximum in 2013 tracking *R. pumilio* abundance (IJID 2021 abstract, indexed summary).

---

## 10. Diagnostics

**Serology (the mainstay).**
- Microimmunofluorescence (MIF) against SFG antigens. ASF sera react to the homologous Astrakhan strain and to the Israeli isolate similarly, and differently from *R. conorii* Malish: "The serologic response to specific rickettsial agent and to Israelian isolate has been found to be similar, but was different of that to R. conorii. Immunoglobulin G (IgG) and IgM antibodies were detected in most sera and were directed against the lipopolysaccharide" (*verbatim*, PMID:8549703).
- **ELISA IgM alone is insufficient.** In 185 patients, "the determination of IgM alone allows for serological confirmation of diagnosis in only 46.5% of cases but ... the determination of both IgM and IgA increases this rate to 66.5%" (*verbatim*, PMID:35467375). IgM recognized both LPS and proteins; IgA predominantly proteins. This is the most actionable recent diagnostic finding for ASF and argues for adding IgA to the panel.
- Complement fixation was used historically, cross-reacting across *R. conorii*, *R. akari* and *R. sibirica* at titres 20–640 (PMID:1884783) — insufficiently specific by modern standards.
- Retrospective serosurveillance in high-risk areas: Chekanova 2019, PMID:31200408.

**Molecular.**
- PCR amplification and sequencing of *gltA*, *ompA*, 16S rDNA, *ompB*, *sca4* and the 23S–5S spacer distinguishes subspecies (PMID:12860619, PMID:12860620, PMID:28986641).
- Suicide PCR on skin biopsy specimens is validated for rickettsioses generally (Fournier 2004, PMID:15297478) and is the route to a diagnosis from an eschar or rash biopsy.
- Real-time pan-*Rickettsia* PCR for screening, with MLST confirmation.

**Culture.** Isolation in cell culture or guinea pigs is possible but slow, low-yield and biosafety-restricted; early attempts recovered rickettsiae in 2 of 12 cell-culture samples and seroconverted 4 of 8 guinea pigs (PMID:1884783). Strains A-108 and A-167 came from *R. pumilio* haemolymph (PMID:7985764).

**Laboratory findings.** Cellular immunology shows transient lymphopenia-like suppression with neutrophil increase from week 2–3 (PMID:12498120). Routine haematological and hepatic abnormality frequencies for ASF were not available in the retrieved abstracts.

**Imaging, electrophysiology, functional tests:** no role.

**Genetic testing:** not applicable (host).

**Differential diagnosis.** Mediterranean spotted fever (*R. conorii* subsp. *conorii*), Israeli spotted fever (subsp. *israelensis*, serologically near-identical — the key laboratory pitfall), Siberian tick typhus (*R. sibirica*), *R. massiliae* and *R. aeschlimannii* infection, Crimean-Congo hemorrhagic fever (co-circulating in the Caspian region and a critical rule-out given the hemorrhagic rash), West Nile fever, hemorrhagic fever with renal syndrome, and non-rickettsial viral exanthems. The 2022 study makes the general point: "The symptoms of this bacterial infection are similar to those of viral infection, and thus, diagnostic accuracy has special clinical importance" (*verbatim*, PMID:35467375). Butenko 1995 (PMID:7476689) treats arbovirus infections, HFRS and Astrakhan fever together as the regional differential.

**Screening.** No population screening. Surveillance is clinician-reported case notification plus tick-abundance monitoring.

---

## 11. Outcome / Prognosis

- **Mortality:** approximately 1–2%, with severe cases 5.3% of those infected and a first reported death in 2013 (cited in PMID:38462076; verify in full text before use as an evidence snippet).
- **Recovery:** the great majority recover fully with antibiotic therapy; ASF is self-limited and leaves no documented chronic sequelae.
- **Prognostic factors:** delay to effective antibiotic therapy is the dominant modifiable factor across SFG rickettsioses (PMID:27172113). Severity correlates with depth and duration of cellular immunosuppression (PMID:12498120), though that is an association in a small series, not a validated prognostic marker.
- **Prognostic biomarkers:** none validated. IL-1 and TNF concentrations tracked disease manifestations in an animal model (PMID:12459842) but have not been evaluated prognostically in patients.
- **Survival statistics, DALYs, disability outcomes, QOL instruments:** no ASF-specific data in SEER-equivalent, GBD or ICF sources.

---

## 12. Treatment

**Doxycycline is the treatment of choice.** The CDC recommendation for tickborne rickettsial disease is explicit: "doxycycline is the treatment of choice for suspected tickborne rickettsial diseases in adults and children" (*verbatim*, PMID:27172113). For ASF specifically, a comparative Russian series concluded "Doxycycline efficiency was higher than that of rifampicin" (*verbatim*, PMID:12498120) — a direct head-to-head observation in ASF patients and the strongest disease-specific therapeutic evidence available.

| Agent | Role | CHEBI (repo cache) | NCIT |
|---|---|---|---|
| Doxycycline | First line | CHEBI:50845 | Pharmacotherapy NCIT:C15986 with `therapeutic_agent` bound to doxycycline |
| Rifampicin | Used in Russian series, less effective than doxycycline | CHEBI:28077 | NCIT:C15986 |
| Chloramphenicol | Historical alternative for SFG rickettsioses | CHEBI:17698 | NCIT:C15986 |
| Azithromycin / ciprofloxacin | Alternatives in MSF literature; no ASF-specific data | CHEBI:2955 / CHEBI:100241 | NCIT:C15986 |
| Supportive care | Fluids for hypotension, antipyresis | — | NCIT:C15747 Supportive Care |

The NCIT identifiers above were **not** resolvable in this worktree's `cache/ncit/terms.csv` during this session (the grep returned nothing), so each must be verified with `just validate-terms` before being written into a KB entry. Per the repository's term contract, do not commit an NCIT CURIE from this table without that lookup.

**Adjunctive interferon — historical, and not recommended.** Galimzianov 1996 reported that "Adjuvant use of interferons in basic treatment of Astrakhan fever elevates its efficacy" with alpha-2 at 15,000–25,000 IU/kg/day and gamma at 1,500–2,500 IU/kg/day, while noting that "Interferons induce side effects early in the course: intensification of hyperthermia and pains" (*verbatim*, PMID:8771664). This is a single uncontrolled 1996 report and has no modern support; curate it as historical practice, not current therapy.

**Immunomodulation in animals.** Galavit reduced IL-1/TNF and mortality in experimental ASF infection (PMID:12459842) — `evidence_source: MODEL_ORGANISM`, no human translation.

**In vitro antimicrobial work.** Wild thyme and bergamot essential oils inhibited *R. conorii caspia* growth in Vero cells (PMID:30316918); chitosan, selenium and silver nanoparticles showed anti-rickettsial activity in Vero cells (PMID:41011786, 2025). Both are `IN_VITRO` and pre-clinical.

**Not applicable:** gene therapy, cell therapy, RNA therapeutics, targeted therapy, immunotherapy, surgery, rehabilitation. No registered clinical trials for ASF were found; a ClinicalTrials.gov query was not run this session and the absence should be confirmed before asserting it in an entry.

**Pharmacogenomics:** none described.

---

## 13. Prevention

- **Primary prevention:** tick-bite avoidance — protective clothing, repellents, prompt full-body tick checks and early removal after outdoor exposure in the endemic season (May–October, peak August). Dog-directed measures matter disproportionately here because *Rh. sanguineus* is a domestic, peridomestic and indoor-capable tick: acaricidal collars and treatments for dogs, and control of tick infestations inside dwellings. The French urban family cluster is the cautionary case — ticks were "collected from the floor from behind the furniture" inside the home (*verbatim*, PMID:23140893).
- **Immunization:** no vaccine exists for any *Rickettsia* in human use (PMID:24059918).
- **Chemoprophylaxis:** not recommended after tick bite for SFG rickettsioses; the CDC approach is watchful waiting with early empiric treatment on symptom onset (PMID:27172113).
- **Secondary prevention:** clinician awareness in endemic areas so that fever plus rash in summer triggers empiric doxycycline before serological confirmation, since early treatment prevents severe outcomes. The Kazakhstan surveillance work makes the analogous point for its own region: "Kazakh physicians should be aware of rickettsioses after tick bites in both regions studied" (*verbatim*, PMID:31053085).
- **Public health:** vector surveillance tied to *R. pumilio* abundance indices, which the Astrakhan registry analysis links to incidence peaks; stray-dog population management; health education before the summer season.
- **Genetic counseling / carrier or prenatal screening:** not applicable.

---

## 14. Other Species / Natural Disease

- **Vectors (not diseased hosts):** *Rhipicephalus pumilio* NCBITaxon:127007; *Rhipicephalus sanguineus* NCBITaxon:34632.
- **Dogs** (*Canis lupus familiaris*, NCBITaxon:9615) are the key tick-maintenance host. Whether dogs develop clinical disease from *R. conorii* subsp. *caspia* was not addressed in any retrieved source; canine infection with *R. conorii* sensu lato is documented generally. Treat canine clinical disease as **unestablished** for this subspecies.
- **Zoonotic status:** ASF is a tick-borne zoonosis with no human-to-human transmission.
- **No OMIA record** applies — this is an infectious disease, not an inherited animal disorder.
- **Comparative pathology:** the endothelial tropism of SFG rickettsiae is conserved across mammalian hosts (Walker 2008, PMID:18414502).
- **Incidental tick findings in other taxa:** *R. conorii* subsp. *caspia* has been detected in *Rh. sanguineus* on dogs in Kosovo, France and Zambia; a Formosan pangolin tick survey (PMID:27426438) and a Turkish cattle tick survey (PMID:35631021) appear in the same literature searches but the retrieved abstracts do not establish subsp. *caspia* detection in those studies.

---

## 15. Model Organisms

- **Cell culture (principal system).** Vero cells are the standard host for *R. conorii caspia* propagation and antimicrobial testing (PMID:30316918; PMID:41011786). Historic isolation used cell cultures with immunofluorescence detection (PMID:1884783). `evidence_source: IN_VITRO`.
- **Guinea pig** (*Cavia porcellus*, NCBITaxon:10141). Used for isolation and seroconversion in the original ASF characterization: 4 of 8 inoculated animals developed SFG antibodies (PMID:1884783). A classical rickettsial isolation host, not a fidelity model of human disease.
- **Mouse** (*Mus musculus*, NCBITaxon:10090). Used for **serotyping**, not pathogenesis: mouse serotyping distinguished the Chad isolate from other *R. conorii* complex members by a specificity difference of 2 (PMID:12860619) and underpinned the subspecies proposal (PMID:15766388).
- **Experimental infection for immunopathology.** The IL-1/TNF and galavit work used unspecified "experimental animals" (PMID:12459842); the species is not stated in the abstract and should be read from the full text before curation.
- **Genetic models:** none. No knockout, transgenic, humanized, organoid or iPSC model exists for ASF, and none is expected — the relevant genetics is bacterial, and *Rickettsia* is genetically intractable relative to free-living bacteria.
- **Limitations.** No animal model reproduces the human ASF clinical picture, including the eschar-poor rash phenotype that distinguishes ASF from MSF. Any `modeled_mechanisms` link for these systems should carry `fidelity: LOW` or `UNKNOWN`, `model_scale: MOLECULAR` or `CELLULAR` for the Vero work, and an explicit `divergences` entry of type `SPECIES_MISMATCH` (guinea pig, mouse) or `BOUNDARY_OMISSION` (Vero cells contain no vasculature, no immune compartment, and cannot report rash or hypotension).

---

## Evidence Inventory for Curation

Verified PMIDs with abstracts retrieved this session, suitable for `just fetch-reference`:

| PMID | Short description | Best use |
|---|---|---|
| 15766388 | Zhu 2005, subspecies proposal, type strain A-167 | Taxonomy, agent identity |
| 1884783 | Tarasevich 1991, first characterization, seroprevalence 5.1%, ticks on dogs | History, epidemiology, vector |
| 1670806 | Tarasevich 1991 Lancet letter (no abstract) | Historical citation only |
| 7985764 | Eremeeva 1994, A-108/A-167 from *R. pumilio*, identity with ISF | Agent, vector |
| 1583342 | Drancourt 1992 letter (no abstract) | Historical |
| 8549703 | Eremeeva 1995, MIF/immunoblot, anti-LPS IgG/IgM | Diagnostics |
| 9324803 | Galimzianov 1996, primary lesion and clinical picture | Phenotypes, pathophysiology |
| 8771664 | Galimzianov 1996, interferon adjuvant | Treatment (historical) |
| 12498120 | Kasimova 2002, cellular immunity, doxycycline > rifampicin | Treatment, immunopathology |
| 12459842 | Nelyubov 2002, IL-1/TNF, galavit, animal model | Mechanism (MODEL_ORGANISM) |
| 10603217 | Rydkina 1999, 3% infection in *R. pumilio* | Vector |
| 12860619 | Fournier 2003, Chad isolate | Geography |
| 12860620 | Fournier 2003, Kosovo ticks | Geography, vector |
| 23140893 | Renvoisé 2012, French urban family cluster | Geography, prevention |
| 28986641 | Chitimia-Dobler 2017, Zambia, 0.06% | Geography |
| 22887666 | Sentausa 2012, genome A-167, AJUR00000000 | Pathogen genomics |
| 35467375 | Smirnova 2022, IgA raises confirmation 46.5% → 66.5% | Diagnostics |
| 17114680 | Tarasevich 2006, recognized since 1983 | History, Russian surveillance |
| 17266709 | Brouqui 2007, European SFG overview | Context |
| 33143199 | Malkhazova 2020, Russian natural-focal EID mapping | Epidemiology context |
| 27172113 | CDC 2016, doxycycline is treatment of choice | Treatment |
| 18414502 | Walker 2008, endothelial infection and early events | Mechanism (indirect) |
| 24059918 | Sahni 2013, rickettsial pathogenesis and immunity | Mechanism (indirect) |
| 16223955 | Parola 2005, review carrying the 321-case series figures | Phenotype frequencies |
| 38462076 | Teng 2024, four cases in Xinjiang, first in East Asia | Geography, severity figures |
| 31053085 | Turebekov 2019, Kazakhstan ticks (caspia **not** found) | Negative/context |
| 36050456 | Kazakhstan rodents (caspia **not** found in rodents) | Negative/context |
| 39065062 | Karachay-Cherkessia ticks (caspia **not** found) | Negative/context |

**Figures needing full-text verification before use as snippets:** the 321-case series percentages (94% adults, 61% male, 85% summer, 43% August, 94% fever with rash, 23% eschar, 32% conjunctivitis) read from the Parola 2005 review rather than the primary Russian source; the 4,894 cases and 23.18 ± 1.5 per 100,000 from the 2021 IJID conference abstract; and the 5.3% severe / 1–2% mortality / first-death-2013 figures cited in the 2024 China letter. The last three publisher pages returned 403 or CAPTCHA this session.

---

## Sources

- [Proposal to create subspecies of Rickettsia conorii (PMID:15766388)](https://pubmed.ncbi.nlm.nih.gov/15766388/)
- [Detection of Astrakhan fever rickettsia from ticks in Kosovo (PMID:12860620)](https://pubmed.ncbi.nlm.nih.gov/12860620/)
- [Isolation of a rickettsia related to Astrakhan fever rickettsia in Chad (PMID:12860619)](https://pubmed.ncbi.nlm.nih.gov/12860619/)
- [Diagnostic Value of IgA Antibody Measurement in ARF (PMID:35467375)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9241626/)
- [Genome Sequence of R. conorii subsp. caspia (PMID:22887666)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3415478/)
- [Tick-Borne Rickettsioses around the World (PMID:16223955)](https://pmc.ncbi.nlm.nih.gov/articles/PMC1265907/)
- [Update on Tick-Borne Rickettsioses: a Geographic Approach](https://pmc.ncbi.nlm.nih.gov/articles/PMC3811236/)
- [Emergence of Astrakhan rickettsial fever in China (PMID:38462076)](https://pubmed.ncbi.nlm.nih.gov/38462076)
- [Epidemiological monitoring of the natural focus of Astrakhan spotted fever (IJID 2021)](https://www.ijidonline.com/article/S1201-9712(21)01194-2/fulltext)
- [Urban family cluster linked to Rh. sanguineus infected with R. conorii subsp. caspia (PMID:23140893)](https://pubmed.ncbi.nlm.nih.gov/23140893/)
- [First detection of R. conorii ssp. caspia in Zambia (PMID:28986641)](https://pubmed.ncbi.nlm.nih.gov/28986641/)
- [CDC Diagnosis and Management of Tickborne Rickettsial Diseases (PMID:27172113)](https://pubmed.ncbi.nlm.nih.gov/27172113/)
- [Prevalence of Rickettsia species in ticks in Kazakhstan (PMID:31053085)](https://pubmed.ncbi.nlm.nih.gov/31053085/)
- [Incidence of SFG Rickettsia in rodents in Kazakhstan (PMID:36050456)](https://www.nature.com/articles/s41598-022-19145-0)
- [Astrakhan spotted fever — MONDO:0024473 (Monarch)](https://api.monarchinitiative.org/v3/api/entity/MONDO:0024473)
- [Astrakhan spotted fever — NORD rare disease page](https://rarediseases.org/mondo-disease/astrakhan-spotted-fever/)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 38 |
| Resolved | 38 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 31 |
| Quoted claims found in source | 25 |
| Quoted claims **not** found in source | 6 |
| Quoted claims with nothing to check against | 2 |
| References weighed for topical relevance | 38 |
| On topic | 19 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:16223955` *(abstract only)*: "Most of the patients had dogs and reported having contact with *Rhipicephalus sanguineus* dog ticks"
  - closest text in source: "Of these agents, seven were initially isolated from ticks, often years or decades before a definitive association with human disease was established"
- `PMID:16223955` *(abstract only)*: "in patients of rural areas"
  - Text part not found as substring: 'in patients of rural areas' (note: only abstract available for PMID:16223955, full text may contain this excerpt)
- `PMID:16223955` *(abstract only)*: "Most of the patients had dogs and reported having contact with *Rhipicephalus sanguineus* dog ticks"
  - closest text in source: "Of these agents, seven were initially isolated from ticks, often years or decades before a definitive association with human disease was established"
- `PMID:16223955` *(abstract only)*: "in patients of rural areas"
  - Text part not found as substring: 'in patients of rural areas' (note: only abstract available for PMID:16223955, full text may contain this excerpt)
- `PMID:16223955` *(abstract only)*: "the presence of a tache noire was reported in only 23% of the patients"
  - Text part not found as substring: 'the presence of a tache noire was reported in only 23% of the patients' (note: only abstract available for PMID:16223955, full text may contain this excerpt)
- `PMID:12498120` *(abstract only)*: "Doxycycline efficiency was higher than that of rifampicin"
  - closest text in source: "CONCLUSION: Doxicycline efficiency was higher than that of rifampicin"

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `PMID:1583342`: "Astrakhan fever rickettsiae were found to be serologically and antigenically similar to Israeli spotted fever rickettsiae. Both of them probably belong to a single Rickettsia conorii pathotype complex. Only PFGE pattern analysis could clearly discriminate Astrakhan fever rickettsiae from other isolates"
  - Reference resolved but exposes no abstract or full text to search
- `PMID:1583342`: "Astrakhan fever rickettsiae were found to be serologically and antigenically similar to Israeli spotted fever rickettsiae. Both of them probably belong to a single Rickettsia conorii pathotype complex. Only PFGE pattern analysis could clearly discriminate Astrakhan fever rickettsiae from other isolates"
  - Reference resolved but exposes no abstract or full text to search

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 54 |
| Resolved | 53 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 8 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0024473` (7 mentions) - the report calls it "Monarch"; MONDO calls it **Astrakhan spotted fever**
- `DOID:0050041` (2 mentions) - the report calls it "DOID"; DOID calls it **Astrakhan spotted fever**
- `NCBITaxon:302011` (3 mentions) - the report calls it "caspia"; NCBITaxon calls it **Rickettsia conorii subsp. caspia**
- `CHEBI:50845` (1 mention) - the report calls it "First line"; CHEBI calls it **doxycycline**
- `CHEBI:28077` (1 mention) - the report calls it "Used in Russian series, less effective than doxycycline"; CHEBI calls it **rifampicin**
- `CHEBI:17698` (1 mention) - the report calls it "Historical alternative for SFG rickettsioses"; CHEBI calls it **chloramphenicol**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `GARD`.