---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-25T17:15:38.342333'
end_time: '2026-09-25T17:21:29.470163'
duration_seconds: 351.13
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Immunodeficiency 62
  mondo_id: MONDO:0032763
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
  web_search_requests: 19
  num_turns: 39
  total_cost_usd: 2.0375426
  session_id: fd65d8eb-852b-5a9d-91de-140beff025e2
  stop_reason: end_turn
  assistant_text_blocks: 2
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
citation_count: 24
reference_validation:
  total_references: 10
  verified: 10
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 10
  on_topic: 5
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 27
  verified: 24
  not_found: 0
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 6
  labels_matching: 4
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0032763
    reported_labels:
    - MONDO
    ontology_label: immunodeficiency 62
  - term_id: GO:0005089
    reported_labels:
    - Rho guanyl-nucleotide exchange factor activity
    ontology_label: GO_0005089
  obsolete_terms:
  - term_id: GO:0005089
    ontology_label: GO_0005089
    replaced_by: GO:0005085
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Immunodeficiency 62
- **MONDO ID:** MONDO:0032763 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Immunodeficiency 62** covering all of the
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

I'll research Immunodeficiency 62 (MONDO:0032763) now and produce the complete report directly in this response.

# Immunodeficiency 62 (ARHGEF1 Deficiency) — Research Report

**Target disease:** Immunodeficiency 62 (IMD62)
**MONDO:** MONDO:0032763 | **OMIM:** #618459 (phenotype), *601855 (gene, *ARHGEF1*) | **Orphanet:** ORPHA:696942 | **Gene:** *ARHGEF1* (HGNC:681, chr19q13.2) | **Category:** Mendelian, autosomal recessive primary immunodeficiency

**Note on sourcing:** Full-text access to the primary literature (JCI, PMC, PubMed, OMIM) was blocked by bot-detection/paywall gates during this research session; content below is drawn from indexed abstracts, structured-database summaries (OMIM/GTR/MalaCards/ClinGen/GeneCards mirrors), and search-engine-returned abstract text, cross-checked across independent sources where possible. Quoted fragments are reproduced as returned by these secondary retrievals and should be re-verified against primary full text (e.g., via `just fetch-reference PMID:30521495`) before being used as exact-quote evidence in a KB entry. This is an ultra-rare condition (literature to date describes essentially one kindred), so several template sections below have little or no disease-specific data — this is stated explicitly rather than papered over.

---

## 1. Disease Information

**Overview.** Immunodeficiency 62 (IMD62) is an autosomal recessive primary antibody deficiency caused by biallelic loss-of-function variants in *ARHGEF1* (Rho Guanine Nucleotide Exchange Factor 1, also known as *GEF1*, *LBCL2*, *LSC*, *P115-RHOGEF*, *SUB1.5*). It was first delineated in 2019 in two affected sisters from a single non-consanguineous French family, identified by whole-exome sequencing (WES) as part of a primary-antibody-deficiency cohort study (Bouafia et al., 2019, PMID:[30521495](https://pubmed.ncbi.nlm.nih.gov/30521495/); companion mechanistic study, PMID:[30714991](https://pubmed.ncbi.nlm.nih.gov/30714991/)). *ARHGEF1* encodes a RhoA-specific guanine nucleotide exchange factor (GEF) that transduces signals from Gα13-coupled GPCRs (e.g., sphingosine-1-phosphate receptors, LPA receptors, CXCR4) into RhoA activation, controlling actin cytoskeleton dynamics and confining/positioning B lymphocytes and myeloid cells within lymphoid compartments. Loss of ARHGEF1 impairs antibody responses through defective B-cell positioning/maturation and dysregulated PI3K/AKT signaling rather than through a primary defect in immunoglobulin gene machinery.

**Key identifiers:**

| Resource | Identifier |
|---|---|
| OMIM phenotype | #618459 IMMUNODEFICIENCY 62; IMD62 |
| OMIM gene | *601855 RHO GUANINE NUCLEOTIDE EXCHANGE FACTOR 1; ARHGEF1 |
| MONDO | MONDO:0032763 |
| Orphanet | ORPHA:696942 |
| HGNC | HGNC:681 (ARHGEF1) |
| GTR condition | C5193109 |
| Gene synonyms | GEF1, LBCL2, LSC, P115-RHOGEF, SUB1.5 |

**Synonyms/alternative names:** ARHGEF1 deficiency; Rho-GEF1 deficiency; p115RhoGEF deficiency. No distinct historical eponym exists; the entity is referred to in the literature simply by its OMIM number (IMD62) or by gene name.

**Evidence basis.** All clinical information available to date derives from **aggregated case-series/primary-literature description of a single reported kindred** (2 affected siblings), not from EHR-derived or registry/population data. There is no disease registry, no GeneReviews chapter, and (as of this search) no published expansion cohort beyond the original 2019 report.

---

## 2. Etiology

**Disease causal factor:** Monogenic — biallelic (compound heterozygous) loss-of-function variants in *ARHGEF1*, autosomal recessive. This is a purely genetic/mechanistic etiology; no infectious or environmental trigger is implicated as causal (though the disease *manifests* as susceptibility to infection).

**Genetic risk factors (causal variants).** The index family carried compound heterozygous variants (ClinGen Antibody Deficiencies GCEP curation, approved 2021-01-19, classification **Limited** — [ClinGen record](https://search.clinicalgenome.org/kb/gene-validity/CGGV:assertion_9547c192-135d-48b3-a1c0-2eca5e2608c5-2021-01-19T214711.722Z)):
- **c.853C>T, p.(Arg285Ter)** — nonsense variant
- **c.1624-1G>T** — splice-acceptor-site variant, reported to cause a frameshift with likely nonsense-mediated decay of the transcript; immunoblot of patient cells showed complete absence of ARHGEF1 protein (loss-of-function/null mechanism, PMID:30521495).

ClinGen's classification is explicitly capped at "Limited" because "SOP requires at least 3 unrelated probands from at least 2 independent reports to get above the Limited classification" and only a single sibling pair/family has been reported to date. This is a load-bearing caveat for curation: gene-disease validity here is genuinely thin, not merely under-cited.

**Modifier/susceptibility genes:** None reported.

**Environmental/lifestyle risk factors:** None specific reported; disease expression is intrinsic to the genetic lesion. Recurrent infections (see Phenotypes) are a consequence, not a cause.

**Protective factors:** None reported (genetic or environmental) specific to this ultra-rare disorder.

**Gene-environment interactions:** Not studied for this specific gene-disease pair. However, the broader biology of *ARHGEF1* (see Mechanism, below) suggests that infectious challenge (viral/bacterial) precipitates the clinically apparent antibody-deficiency phenotype in carriers of biallelic null alleles, consistent with a "silent until challenged" pattern typical of antibody deficiencies.

---

## 3. Phenotypes

Phenotype data derive from OMIM's clinical synopsis (#618459) and the Bouafia et al. 2019 report, describing the two affected sisters (P1 and P2).

| Phenotype (category) | Onset/frequency | Notes | Suggested HPO term (lead — verify) |
|---|---|---|---|
| Recurrent upper respiratory tract infections | Onset "late in the first decade of life"; frequent | Presenting feature | HP:0002205 Recurrent respiratory infections |
| Recurrent lower respiratory tract infections | Same onset | Presenting feature | HP:0002205 (or narrower "Recurrent pneumonia," lead only) |
| Bronchiectasis | Sequela of recurrent infection, reported in both sibs | Structural airway damage | HP:0002110 Bronchiectasis |
| Increased susceptibility to VZV (varicella zoster virus) | Reported | Viral susceptibility despite predominantly antibody-deficiency phenotype | HP:0004429-type viral-susceptibility term (lead) |
| Increased susceptibility to HSV (herpes simplex virus) | Reported | As above | lead — verify |
| Impaired antibody response to vaccination | Laboratory finding | Functional humoral defect | HP:0002846 Impaired T-cell independent antibody response / general "Abnormal antibody response to vaccination" (lead) |
| Low circulating memory B cells | Laboratory | Flow cytometry finding | HP term for decreased memory B cells (lead) |
| Deficiency of marginal-zone and memory B cells; increased transitional B cells | Laboratory (immunophenotyping) | Core immunophenotype per PMID:30521495 | leads only |
| Almost undetectable serum antibodies | Laboratory | Severe hypogammaglobulinemia | HP:0002850 Decreased circulating IgG / related terms (lead) |
| Secondary T-cell dysfunction | Laboratory | Described as "secondary," i.e., downstream of the primary B-cell/myeloid defect rather than a primary T-cell lesion | lead |
| Immature myeloid cells in circulation | Laboratory (blood smear/flow) | Consistent with disturbed myeloid egress/retention from marrow, mirroring mouse Arhgef1 knockout phenotype | lead |
| Small germinal centers with increased plasma cells (lymph node histology) | Histopathology | Reported on lymph node biopsy in at least one patient | lead |

**Severity/progression:** Reported as progressive with cumulative airway damage (bronchiectasis) from recurrent infection over childhood into the reported observation period; qualitative descriptors (mild/moderate/severe) are not systematically graded in the source material because the cohort is n=2.

**Frequency among affected individuals:** Because only 2 patients are reported, "percentage" frequency statistics are not meaningful/available — every listed phenotype above is present in the only reported cases (2/2), which is not generalizable.

**Quality-of-life impact:** Not formally measured (no EQ-5D/SF-36/QOL instrument data identified for this condition).

**Not available / not yet reported:** age-specific growth/developmental data, neurologic phenotype, autoimmune manifestations, malignancy risk, gastrointestinal involvement — none of these are described in the source literature located, and their absence should be read as "not reported" rather than "excluded."

---

## 4. Genetic / Molecular Information

**Causal gene:** *ARHGEF1* (Rho Guanine Nucleotide Exchange Factor 1), OMIM *601855, HGNC:681, chromosome **19q13.2**. Gene product: guanine nucleotide exchange factor for RhoA (also called p115RhoGEF/Lsc), acting downstream of Gα12/Gα13; contains a canonical RGS-homology (RH) domain that also confers GTPase-activating-protein (GAP) activity toward Gα12/Gα13, plus tandem DH (Dbl-homology) and PH (pleckstrin-homology) domains that catalyze GDP→GTP exchange on RhoA.

**Pathogenic variants (index family, both affected sisters, compound heterozygous):**
- c.853C>T; p.(Arg285Ter) — nonsense, predicted premature truncation
- c.1624-1G>T — canonical splice-acceptor variant, shown experimentally to cause a frameshift with likely nonsense-mediated mRNA decay

**Variant classification:** Reported functionally as loss-of-function/null alleles — immunoblotting on patient lymphocytes showed **complete absence of ARHGEF1 protein**, i.e., a biallelic null genotype (PMID:30521495). Formal ACMG/AMP classification strings (Pathogenic/Likely Pathogenic) were not located in the accessible sources but the functional null result is consistent with Pathogenic.

**Allele frequency:** No population allele-frequency data specific to these two variants were retrieved in this session (gnomAD lookup blocked); given the extreme rarity of the phenotype and the null functional effect, both variants are expected to be very rare/private, consistent with a genuinely novel private-family finding rather than a founder allele. This should be verified directly against gnomAD before citation.

**Somatic vs. germline:** Germline — constitutional variants inherited from unaffected heterozygous parents (non-consanguineous), consistent with autosomal recessive transmission.

**Functional consequence:** Loss of function (protein-null). No gain-of-function, dominant-negative, or hypomorphic alleles have been reported for this phenotype.

**Modifier genes:** None reported.

**Epigenetic information:** None reported specific to IMD62/ARHGEF1 deficiency.

**Chromosomal abnormalities:** None reported; this is a single-gene point-mutation/splice-variant disorder, not a copy-number or structural chromosomal disease.

**Gene constraint (gnomAD pLI/LOEUF):** Not retrieved in this session — flag as a gap; useful for arguing haploinsufficiency intolerance but not independently verified here.

---

## 5. Environmental Information

- **Environmental factors:** None identified as disease-causal; the disorder is monogenic.
- **Lifestyle factors:** Not applicable/not reported.
- **Infectious agents:** Infection is a *manifestation* rather than a *cause* — recurrent bacterial upper/lower respiratory pathogens (unspecified species in the accessible abstracts) drive the bronchiectasis phenotype, and the patients show heightened susceptibility to two specific herpesviruses, **varicella zoster virus (VZV)** and **herpes simplex virus (HSV)** (OMIM clinical synopsis, mirrored via GTR). No specific bacterial species, serotype, or viral strain data were retrieved.

---

## 6. Mechanism / Pathophysiology

### Causal chain (ordered, with inference flagged)

1. Biallelic loss-of-function variants in *ARHGEF1* (nonsense + splice-acceptor) → **absence of ARHGEF1 protein** in hematopoietic cells (demonstrated directly by immunoblot in patient lymphocytes, PMID:30521495).
2. Loss of ARHGEF1 → **failure to couple Gα13-associated GPCR signals (S1P receptors, LPA receptors, thromboxane receptor, CXCR4) to RhoA activation** in lymphocytes (demonstrated directly by ligand-stimulation assays on patient cells, PMID:30714991).
3. Reduced RhoA-GTP loading → **decreased steady-state and stimulus-induced actin polymerization (F-actin)** in patient T and B lymphocytes (demonstrated directly).
4. Disturbed RhoA→ROCK (Rho-associated kinase I/II) signaling → **failure to restrain PI3K/AKT phosphorylation** (i.e., loss of a RhoA/ROCK-dependent brake on AKT) — demonstrated directly, and pharmacologic RhoA activation or restoring ARHGEF1 expression rescued both the actin and AKT phenotypes in vitro, supporting causality rather than mere correlation.
5. Combined actin-cytoskeleton and GPCR-signaling defects → **impaired lymphocyte and myeloid-cell migration/positioning and integrin-dependent adhesion** (demonstrated directly by migration assays on integrin ligands and by circulating immature myeloid cells in patient blood; inferred by analogy from extensive mouse Arhgef1/Lsc knockout data — see Model Organisms, below — that this reflects a failure to retain/position marginal-zone B cells and control lymphocyte egress).
6. Mispositioning/failure of marginal-zone and germinal-center B-cell compartments → **abnormal B-cell immunophenotype**: deficiency of marginal-zone and memory B cells, increased transitional B cells, small germinal centers with increased plasma-cell content on lymph-node histology (demonstrated directly in patient blood/tissue).
7. Defective B-cell maturation/positioning → **failure to mount T-cell-dependent and T-cell-independent antibody responses to vaccination and pathogens**, i.e., primary/predominant antibody deficiency with near-undetectable circulating antibody (demonstrated directly; mechanistically this step is supported both by direct human data and by strong concordance with the mouse Lsc-knockout literature, where loss of the ortholog produces near-identical humoral defects — inferred generalization from a well-established animal model to the human case, i.e., **directness: INDIRECT** support from the mouse literature, **DIRECT** support from the human functional studies).
8. Concomitantly, secondary T-cell dysfunction is observed (mechanism less well resolved — likely downstream/secondary to the shared actin/AKT signaling defect rather than an independent primary T-cell lesion; this step is **inferred**, not mechanistically dissected in the source papers).
9. Combined humoral failure + secondary T-cell dysfunction → clinical phenotype of **recurrent bacterial sinopulmonary infection with bronchiectasis, and increased susceptibility to VZV/HSV**.

### Detail by category

- **Molecular pathways:** Gα13(GNA13)–ARHGEF1(p115RhoGEF)–RhoA–ROCK I/II axis; downstream negative regulation of PI3K/AKT. GO terms to consider (leads, verify before binding): GO:0005089 (Rho guanyl-nucleotide exchange factor activity), GO:0035023 (regulation of Rho protein signal transduction), GO:0007266 (Rho protein signal transduction).
- **Cellular processes:** actin cytoskeleton polymerization/remodeling, integrin-dependent adhesion, chemotactic/lysophospholipid-receptor-directed cell migration, lymphocyte positioning within secondary lymphoid organs, B-cell class-switch/maturation support (via indirect maturation-niche effects rather than a direct AID/CSR defect — not reported as a direct class-switch recombination enzyme defect).
- **Protein dysfunction:** complete loss of protein (null) rather than a structural misfolding/dominant-negative mechanism; both a nonsense truncation and a splice-defect–driven NMD converge on absence of functional ARHGEF1.
- **Immune system involvement:** This is fundamentally an immune-cell-intrinsic signaling disorder — predominantly antibody deficiency with a B-cell/myeloid positioning defect, plus secondary T-cell dysfunction; no evidence of autoimmunity or autoinflammation reported.
- **Tissue damage mechanisms:** Recurrent infection → chronic airway inflammation → bronchiectasis (structural, secondary to infection burden rather than a primary structural lung defect).
- **Biochemical abnormalities:** Loss of RhoA-GTP loading capacity in lymphocytes; failure of ROCK-dependent restraint on AKT phosphorylation.
- **Single-cell/omics/advanced technologies:** No single-cell, spatial transcriptomic, or multi-omics dataset specific to human ARHGEF1 deficiency was located. The 2019 papers used targeted flow cytometry, immunoblotting, and functional cell-based assays (migration, adhesion, RhoA-GTP pulldown), not unbiased omics profiling.

**Suggested cell types (CL, leads):** CL:0000236 B cell; CL:0000844 marginal zone B cell; CL:0000969 memory B cell; CL:0000818 transitional stage B cell; CL:0000542 lymphocyte (T cell involvement, secondary); CL:0000766 myeloid cell (immature circulating forms).

---

## 7. Anatomical Structures Affected

- **Organ level (primary):** Respiratory system — upper and lower airways (recurrent infection); lungs specifically via bronchiectasis. Secondary/immune organs: lymph nodes (abnormal germinal-center architecture), spleen (inferred site of marginal-zone B-cell dysfunction, by strong analogy to the mouse spleen phenotype — not directly biopsied/reported in the human cases), bone marrow (site of myeloid egress dysregulation, inferred from circulating immature myeloid cells).
- **Body systems involved:** Immune system (primary); respiratory system (secondary, consequence of immune failure).
- **Tissue/cell level:** Lymphoid tissue (germinal centers, marginal zone); circulating B lymphocytes, T lymphocytes, myeloid cells.
- **Subcellular level:** Cytoskeleton/cortical actin (GO Cellular Component candidate: GO:0015629 actin cytoskeleton); plasma membrane-proximal GPCR signaling complexes.
- **Localization/UBERON leads (verify before binding):** UBERON:0002048 lung; UBERON:0000029 lymph node; UBERON:0002106 spleen (inferred, not directly reported); UBERON:0002371 bone marrow (inferred).
- **Laterality:** Not specifically reported (bronchiectasis distribution not detailed in accessible abstracts).

---

## 8. Temporal Development

- **Onset:** Described specifically as "late in the first decade of life" (OMIM clinical synopsis) — i.e., childhood onset, insidious/subacute rather than neonatal or acute.
- **Progression:** Chronic and apparently progressive with respect to structural airway damage (bronchiectasis accrues with recurrent infection); the underlying immunologic defect itself is presumably lifelong/static (germline, constitutively null gene), but its clinical expression accumulates over time.
- **Disease course pattern:** Chronic with recurrent infective episodes rather than a single-episode or fully remitting course; consistent with other predominant antibody deficiencies (e.g., CVID-like course).
- **Duration:** Chronic/lifelong (genetic, biallelic null).
- **Remission patterns / critical periods:** Not reported; no data on spontaneous or treatment-induced remission for this specific gene defect. By analogy with other antibody deficiencies, immunoglobulin replacement (if used) would be expected to reduce but not eliminate infection frequency — this is an **inference**, not a reported outcome for this specific disease.

---

## 9. Inheritance and Population

- **Inheritance pattern:** Autosomal recessive (confirmed compound heterozygous state in both affected sisters, unaffected heterozygous-carrier parents implied by non-consanguineous transmission).
- **Penetrance:** Presumed complete for the null genotype based on both reported sibs being affected, but n=2 is far too small to estimate penetrance rigorously; **not formally established**.
- **Expressivity:** Both reported sisters share overlapping but not necessarily identical clinical detail (exact concordance not resolved in the accessible abstracts) — insufficient data to characterize variable expressivity.
- **Genetic anticipation / germline mosaicism / founder effect:** None reported; not applicable to a two-patient nonsense/splice compound-heterozygote family.
- **Consanguinity:** Explicitly **not** present — parents described as non-consanguineous, each presumably a heterozygous carrier of one of the two variants.
- **Carrier frequency:** Not established/reported; the two specific variants are private-family findings as far as located sources indicate.
- **Epidemiology (prevalence/incidence):** No formal prevalence or incidence estimate exists. Orphanet classifies rarity descriptively rather than numerically for entities with only isolated case reports; the honest statement is: **only one family (2 affected siblings) has been published to date**, so a population prevalence cannot be calculated. This should be curated as `prevalence_class: NOT_YET_DOCUMENTED` (or `CASES_IN_LITERATURE` with n=2) rather than any numeric band.
- **Population demographics:** No specific ethnic, geographic, or sex-ratio data beyond the fact that both reported patients are female siblings; two data points are insufficient to infer a sex bias, and no biological rationale for X-linked or sex-skewed autosomal-recessive expression is suggested by the mechanism (ARHGEF1 is autosomal).

---

## 10. Diagnostics

**Laboratory/immunologic tests reported as diagnostically informative:**
- Serum immunoglobulin quantification — profound hypogammaglobulinemia ("almost undetectable antibodies")
- Post-vaccination antibody titers — impaired/absent response
- Peripheral blood B-cell immunophenotyping by flow cytometry — deficient marginal-zone and memory B cells, increased transitional B cells
- Peripheral blood myeloid assessment — circulating immature myeloid forms
- Lymph node biopsy/histopathology — small germinal centers, increased plasma cells

**Genetic testing:** Whole-exome sequencing (WES) was the diagnostic method that identified the causal variants in the index family; this remains the recommended approach for suspected novel/ultra-rare primary antibody deficiencies where a gene panel would not include *ARHGEF1* by default. As of this search, some commercial primary-immunodeficiency exome/genome panels and the Genomics England PanelApp "Primary immunodeficiency or monogenic inflammatory bowel disease" panel do list *ARHGEF1* (per PanelApp search result), so **targeted PID gene panels including ARHGEF1** and **single-gene Sanger confirmation of familial variants** are also reasonable once a candidate variant is found. GTR lists 5 clinical tests available for IMD62 (sequence analysis of the entire coding region, deletion/duplication analysis, and targeted variant testing among them).

**Functional/research assays used to confirm pathogenicity (not yet standard clinical tests):** ARHGEF1 immunoblot (protein-null confirmation), RhoA-GTP pulldown activity assay, F-actin polymerization assay (phalloidin-based, resting and post-GPCR-agonist stimulation), lymphocyte migration/adhesion assays on integrin ligands, AKT phosphorylation assay.

**Differential diagnosis:** Other predominant/primary antibody deficiencies with childhood-onset recurrent sinopulmonary infection and bronchiectasis, notably common variable immunodeficiency (CVID) of other genetic causes, X-linked agammaglobulinemia (if male — not applicable here given female sibs and AR inheritance), and other genetically defined antibody deficiencies in the IUIS "Predominantly Antibody Deficiencies" category. The specific combination of **VZV/HSV susceptibility with a B-cell (not primarily T-cell) predominant defect, marginal-zone/memory B-cell deficiency, and increased transitional B cells** is a distinguishing immunophenotypic clue, though not disease-specific on its own.

**Screening:** No newborn-screening or population carrier-screening program exists for this ultra-rare condition; standard newborn TREC-based SCID screening would not be expected to detect a predominant-antibody-deficiency phenotype of this kind.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** No mortality data reported; both index patients are described in terms of chronic morbidity (recurrent infection, bronchiectasis) rather than reported deaths.
- **Morbidity:** Chronic bronchiectasis with attendant risk of progressive lung function decline if infections are not adequately controlled (standard bronchiectasis natural history, extrapolated — not specifically quantified for this cohort).
- **Complications:** Bronchiectasis is the principal structural complication reported; recurrent VZV/HSV reactivation/infection is a specific infectious complication.
- **Recovery potential / treatment response:** Not formally reported as an outcome metric in the located abstracts; the mechanistic rescue experiments (restoring ARHGEF1 expression or pharmacologically activating RhoA corrects the cellular defects in vitro) suggest biological reversibility of the cellular phenotype, which is a rationale for gene-addition/small-molecule approaches but is **not** evidence of a clinical treatment outcome in patients.
- **Prognostic factors/biomarkers:** None specifically validated; by general PID principles, degree of antibody deficiency and lung damage at diagnosis would be expected prognostic factors, but this is inference, not disease-specific reported data.

---

## 12. Treatment

No disease-specific treatment trial or approved therapy exists for IMD62; treatment is inferred/extrapolated from standard primary-antibody-deficiency management, as is typical for a two-patient, recently described monogenic disease.

- **Pharmacotherapy (standard-of-care extrapolation, not disease-specific trial evidence):**
  - Immunoglobulin replacement therapy (IVIG or subcutaneous immunoglobulin) — standard for antibody deficiency with near-undetectable antibody levels; NCIT:C15986 (Pharmacotherapy) as the generic action term, with `therapeutic_agent` bound to immune globulin if curated.
  - Prophylactic antibiotics for recurrent respiratory infection and bronchiectasis management — standard bronchiectasis supportive care (NCIT:C15747 Supportive Care).
  - Antiviral prophylaxis/treatment (e.g., for VZV/HSV) given the specific reported viral susceptibility — inferred standard-of-care, not reported as a trial outcome in this disease.
- **Advanced therapeutics:** No gene therapy, cell therapy, or targeted small-molecule trial specific to ARHGEF1 deficiency was identified. The demonstrated in-vitro rescue of the cellular phenotype by re-expressing ARHGEF1 or pharmacologically activating RhoA is proof-of-concept research, not a clinical therapeutic.
- **Surgical/interventional:** Bronchiectasis management may include standard pulmonary interventions (airway clearance, and in severe localized disease, surgical resection) per general bronchiectasis guidelines — not specifically reported for this disease.
- **Supportive/rehabilitative:** Pulmonary rehabilitation/airway clearance therapy, standard for bronchiectasis (NCIT:C15302 Physical Therapy / pulmonary-specific variants) — extrapolated.
- **Experimental treatments/clinical trials:** No ClinicalTrials.gov-registered trial specific to ARHGEF1 deficiency or IMD62 was identified in this search.
- **Treatment outcomes / response rates / adverse events:** Not reported for this disease specifically.
- **Personalized medicine:** None specific; the mechanistic finding that RhoA-activating compounds correct cellular defects in vitro is a research lead for a targeted approach but has not progressed to any reported patient-level intervention.

**Everything in this section beyond the bare fact "no specific treatment trial exists" is inference from general PID/bronchiectasis standard of care, and should be flagged as such (not disease-specific evidence) if curated into a KB entry.**

---

## 13. Prevention

No disease-specific primary, secondary, or tertiary prevention program exists.
- **Primary prevention:** Standard childhood immunization is presumably still administered though expected to be ineffective (impaired antibody response to vaccination is itself part of the phenotype) — inference, not directly reported.
- **Secondary prevention:** Early recognition via genetic testing in siblings of an index case (given autosomal recessive inheritance, 25% recurrence risk per pregnancy) — standard Mendelian-disease genetic-counseling logic, not disease-specific published guidance.
- **Screening:** No population or genetic screening program exists; carrier screening for these private-family variants would only be relevant within the reported kindred.
- **Genetic counseling:** Standard autosomal-recessive counseling applies (25% recurrence risk for future affected offspring of two carrier parents; not disease-specific literature, but a direct consequence of the confirmed inheritance pattern).
- **Prophylaxis:** Antimicrobial/antiviral prophylaxis as extrapolated in Treatment, above, would constitute tertiary prevention of infection-related morbidity (bronchiectasis progression), not disease-specific published guidance.

---

## 14. Other Species / Natural Disease

No naturally occurring veterinary disease (spontaneous companion-animal or wildlife *Arhgef1*-deficiency phenotype) was identified in this search — all animal data derive from engineered knockout mice (see Model Organisms, below), not natural disease. No OMIA entry or veterinary case series was located.

- **Taxonomy:** Human disease NCBITaxon:9606; mouse ortholog studies NCBITaxon:10090 (Mus musculus).
- **Orthologous gene:** Mouse *Arhgef1* (historically called *Lsc*), NCBI Gene (mouse) — the literature explicitly equates murine Lsc with human p115RhoGEF/ARHGEF1.
- **Comparative biology:** The RhoA-GEF function and its role in marginal-zone B-cell retention/motility and lymphocyte GPCR signaling is conserved between mouse and human, and the human patient phenotype (marginal-zone/memory B-cell deficiency, impaired T-dependent antibody response) closely mirrors the mouse *Arhgef1*-knockout phenotype, providing strong cross-species mechanistic concordance (see next section).
- **Zoonotic potential / cross-species transmission:** Not applicable — this is a non-infectious monogenic immune disorder, not a transmissible disease.

---

## 15. Model Organisms

This is the best-developed section of the evidence base for this gene, because *Arhgef1* (Lsc) knockout mice were studied for two decades before the human disease was described, giving strong (if indirect/model-first) mechanistic support.

| Model | Type | Key phenotype | Fidelity to human disease | Citation |
|---|---|---|---|---|
| *Arhgef1*⁻ᐟ⁻ (Lsc-deficient) mouse | Constitutive knockout, mammalian in vivo | Lack/near-absence of marginal-zone B cells; impaired antibody responses to T-independent and T-dependent antigens; impaired S1P-directed migration and integrin-mediated release of marginal-zone B lymphocytes in vitro and in vivo | High concordance with the human marginal-zone/memory B-cell deficiency and impaired antibody-response phenotype; mouse work substantially predates and predicts the human mechanism | Girkontaite et al., *Nat Immunol* 2001;2:855-862, PMID:[11526402](https://pubmed.ncbi.nlm.nih.gov/11526402/) |
| *Arhgef1*⁻ᐟ⁻ mouse, B-cell-focused follow-up | Constitutive knockout | Lsc required for marginal-zone B-cell migration and adhesion; required for the IgM T-dependent antibody response specifically | Directly recapitulates human impaired-antibody-response and marginal-zone B-cell-deficiency phenotype | Francis et al., *Immunity* 2005;23:527-538, PMID:[16286020](https://pubmed.ncbi.nlm.nih.gov/16286020/) |
| *Arhgef1*⁻ᐟ⁻ mouse, T-cell/airway focus | Constitutive/conditional knockout | Arhgef1 required by T cells for development of airway hyperreactivity and inflammation in an asthma model | Relevant to airway/pulmonary immune biology broadly; not a direct model of the human bronchiectasis-via-antibody-deficiency mechanism — illustrates a **different** (T-cell/airway-inflammatory) role of the same gene, so should not be conflated with the human PAD mechanism without qualification | Chen et al./cited work, *Am J Respir Crit Care Med* 2007;176:10, PMID:[17463415](https://pubmed.ncbi.nlm.nih.gov/17463415/) |
| *Arhgef1*⁻ᐟ⁻ mouse, pulmonary leukocyte review | Review of knockout data | Summarizes Arhgef1's role in pulmonary macrophage/leukocyte function | Background/synthesis, not new primary data | *Immunol Res* 2012, PMID:[22941563](https://pubmed.ncbi.nlm.nih.gov/22941563/) |
| *Arhgef1*⁻ᐟ⁻ mouse, vascular/atherosclerosis | Constitutive knockout | Leukocyte Arhgef1 mediates Ang II-induced vascular inflammation/atherosclerosis via integrin activation | Off-target relative to the immunodeficiency phenotype — evidence for a distinct cardiovascular role of ARHGEF1 in leukocytes, useful only as broader gene-biology background, not disease modeling | *J Clin Invest* 2017;127:4516-4526, PMID:[29130930](https://pubmed.ncbi.nlm.nih.gov/29130930/) |
| *Arhgef1*⁻ᐟ⁻ mouse, platelet | Constitutive knockout | Arhgef1 plays a role in platelet function/thrombogenesis | Off-target relative to immunodeficiency; not disease-relevant modeling | *J Am Heart Assoc* 2018/2019 |

**Model limitations:** All available "modeling" for this human disease is a **constitutive whole-body mouse knockout**, not a human-variant knock-in, iPSC-derived, or conditional hematopoietic-lineage-specific model. No model has been engineered to carry the exact human c.853C>T or c.1624-1G>T alleles. The concordance between mouse and human phenotypes (marginal-zone B-cell loss, impaired T-dependent antibody response) is strong for the B-cell/antibody axis but the mouse literature also documents prominent T-cell/airway-inflammatory and vascular/platelet phenotypes of Arhgef1 loss that have **not** been reported as clinical features in the two human patients — this divergence should be flagged as a scale/translational caveat (`BOUNDARY_OMISSION`-type divergence) rather than assumed to extend to humans. No organoid, iPSC-derived, zebrafish, or computational model of ARHGEF1 deficiency was identified.

---

## Summary of Key Gaps (for curation planning)

1. **No prevalence/incidence data** beyond "one reported family, two affected siblings" — must be curated as literature-case-count, not a population rate.
2. **No GeneReviews chapter** identified for this condition.
3. **No treatment trial or disease-specific outcome data** — all treatment content above is extrapolated from general PID/bronchiectasis standard of care and must be labeled as such if curated.
4. **No confirmed additional published cases since the 2019 index report** were found in this search (searched explicitly for 2023-2025 literature; none located) — the evidence base has apparently not grown since the original description.
5. **gnomAD constraint metrics (pLI/LOEUF) for ARHGEF1** were not retrieved — worth fetching directly before curation.
6. **Full-text primary-source access was blocked** in this session (PubMed/PMC/JCI/OMIM all returned bot-check or 403/503 errors through the available fetch tooling); every quote/detail above should be re-verified against the primary full text via the dismech reference-fetching workflow (`just fetch-reference PMID:30521495`, `PMID:30714991`, `PMID:11526402`, `PMID:16286020`) before being used as an exact-quote `snippet` in a KB entry, per the dismech evidence-discipline rules.
7. **Ontology term IDs suggested throughout (HPO, GO, CL, UBERON) are unverified leads**, offered per the template's request, and must be run through `just validate-terms` / OAK lookup rather than bound directly from this report.

---

### Sources

- [Entry - #618459 - IMMUNODEFICIENCY 62; IMD62 - OMIM](https://omim.org/entry/618459)
- [Entry - *601855 - RHO GUANINE NUCLEOTIDE EXCHANGE FACTOR 1; ARHGEF1 - OMIM](https://omim.org/entry/601855)
- [Immunodeficiency 62 - NIH Genetic Testing Registry (GTR) - NCBI](https://www.ncbi.nlm.nih.gov/gtr/conditions/C5193109/)
- [immunodeficiency 62 Disease External Resources - ClinGen](https://search.clinicalgenome.org/kb/conditions/MONDO:0032763/external-resources)
- [ClinGen Gene-Disease Validity Curation: ARHGEF1 / Immunodeficiency 62](https://search.clinicalgenome.org/kb/gene-validity/CGGV:assertion_9547c192-135d-48b3-a1c0-2eca5e2608c5-2021-01-19T214711.722Z)
- [Immunodeficiency 62 - MalaCards](https://www.malacards.org/card/immunodeficiency_62)
- [Curate immunodeficiency 62 (MONDO:0032763) · Issue #12797 · monarch-initiative/dismech](https://github.com/monarch-initiative/dismech/issues/12797)
- [Loss of ARHGEF1 causes a human primary antibody deficiency - PubMed (PMID:30521495)](https://pubmed.ncbi.nlm.nih.gov/30521495/)
- [Loss of ARHGEF1 causes a human primary antibody deficiency - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6391114/)
- [JCI - Loss of ARHGEF1 causes a human primary antibody deficiency](https://www.jci.org/articles/view/120572)
- [ARHGEF1 deficiency reveals Gα13-associated GPCRs are critical regulators of human lymphocyte function - PubMed (PMID:30714991)](https://pubmed.ncbi.nlm.nih.gov/30714991/)
- [ARHGEF1 deficiency reveals Gα13-associated GPCRs are critical regulators of human lymphocyte function - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6391110/)
- [JCI - ARHGEF1 deficiency reveals Gα13-associated GPCRs are critical regulators of human lymphocyte function](https://www.jci.org/articles/view/125893)
- [Loss of ARHGEF1 causes a human primary antibody deficiency | Semantic Scholar](https://www.semanticscholar.org/paper/Loss-of-ARHGEF1-causes-a-human-primary-antibody-Bouafia-Lofek/4aacee211837bc4b80dd7f85fbe30b6733288125)
- [Lsc is required for marginal zone B cells, regulation of lymphocyte motility and immune responses - PubMed (PMID:11526402)](https://pubmed.ncbi.nlm.nih.gov/11526402/)
- [Lsc Regulates Marginal-Zone B Cell Migration and Adhesion and Is Required for the IgM T-Dependent Antibody Response - PubMed (PMID:16286020)](https://pubmed.ncbi.nlm.nih.gov/16286020/)
- [The influence of Arhgef1 on pulmonary leukocyte function - PubMed (PMID:22941563)](https://pubmed.ncbi.nlm.nih.gov/22941563/)
- [Arhgef1 is required by T cells for the development of airway hyperreactivity and inflammation - PubMed (PMID:17463415)](https://pubmed.ncbi.nlm.nih.gov/17463415/)
- [JCI - Leukocyte RhoA exchange factor Arhgef1 mediates vascular inflammation and atherosclerosis (PMID:29130930)](https://www.jci.org/articles/view/92702)
- [ARHGEF1 Gene - GeneCards](https://www.genecards.org/card/ARHGEF1)
- [ARHGEF1 curation results - ClinGen](https://search.clinicalgenome.org/kb/genes/HGNC:681)
- [Gene: ARHGEF1 - Genomics England PanelApp](https://panelapp.genomicsengland.co.uk/panels/398/gene/ARHGEF1/)
- [The 2022 Update of IUIS Phenotypical Classification for Human Inborn Errors of Immunity - PubMed](https://pubmed.ncbi.nlm.nih.gov/35748970/)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 10 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 10 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 27 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 6 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0032763` (6 mentions) - the report calls it "MONDO"; MONDO calls it **immunodeficiency 62**
- `GO:0005089` (1 mention) - the report calls it "Rho guanyl-nucleotide exchange factor activity"; GO calls it **GO_0005089**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005089` (GO_0005089) (1 mention) - replaced by `GO:0005085`

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.