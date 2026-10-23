---
provider: claude_code
model: claude-opus-5-5
cached: false
start_time: '2026-10-01T10:06:37.671224'
end_time: '2026-10-01T10:10:03.381446'
duration_seconds: 205.71
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Intellectual Disability, Autosomal Dominant 48
  mondo_id: MONDO:0030913
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
  - claude-opus-5-5
  num_turns: 9
  total_cost_usd: 1.7527198
  session_id: 78f7102b-f77b-406e-9556-a9e84f1cb399
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  assistant_text_blocks: 2
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderNotConfiguredError
  remedy: the provider is not configured
  retryable: false
- provider: claude_code
  succeeded: true
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 9
  on_topic: 7
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 66
  verified: 66
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 15
  labels_matching: 9
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: MONDO:0030913
    reported_labels:
    - MONDO
    ontology_label: intellectual disability, autosomal dominant 48
  - term_id: HP:0001263
    reported_labels:
    - Infancy
    ontology_label: Global developmental delay
  - term_id: GO:0030027
    reported_labels:
    - Subcellular location:** actin cytoskeleton / lamellipodium
    ontology_label: lamellipodium
  labels_variant: 3
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Intellectual Disability, Autosomal Dominant 48
- **MONDO ID:** MONDO:0030913 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Intellectual Disability, Autosomal Dominant 48** covering all of the
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

Permissions block grep; I'll use Read.

# Research Report: Intellectual Developmental Disorder, Autosomal Dominant 48 (MRD48; RAC1-related neurodevelopmental disorder)

**Target:** Intellectual Disability, Autosomal Dominant 48. MONDO:0030913 as given in the template; OMIM #617751.
**Report date:** 2026-10-01

## How this report was built

I read the nine primary references already cached in this worktree's `references_cache/` (PMIDs 28886345, 30042656, 34725860, 35139179, 37059841, 37328543, 39307291, 39838818, 42120539). Five have full text and four have abstracts only. Every quoted snippet below was copied from those cached files.

- **Live web and database searches were not run.** I did not query OMIM, Orphanet, ClinVar, gnomAD or MGI, so no figures from those sources appear here.
- **Unchecked CURIEs.** The ontology identifiers marked **[verify]** were recalled from memory and not looked up. Under the repo's term contract (CLAUDE.md), each must be checked with `runoak` or the term caches before it is bound.

---

## 1. Disease information

**Overview.** MRD48 is a rare, highly variable neurodevelopmental disorder (NDD). It is caused by heterozygous, almost always de novo, missense variants in **RAC1**, a Rho-family small GTPase. The core features are:
- developmental delay or intellectual disability (DD/ID) with speech delay;
- structural brain anomalies;
- hypotonia, feeding difficulties and behavioural problems;
- a recognisable but subtle facial gestalt.

Its most striking feature is that head size depends on the variant. Occipitofrontal circumference ranges from about −5 SD to +4.5 SD, and this follows whether the variant is dominant-negative or activating.

- *"De novo missense variants in RAC1 are associated with a rare neurodevelopmental disorder (MRD48) characterized by DD/ID and brain abnormalities coupled with a wide range of additional features."* (PMID:37059841, Priolo et al., Eur J Hum Genet 2023)
- *"Collectively, we observed an extraordinary spread of ∼10 SD of head circumferences orchestrated by distinct mutations in the same gene."* (PMID:28886345, Reijnders et al., Am J Hum Genet 2017; the founding report)

**Identifiers**

| Resource | ID | Note |
|---|---|---|
| OMIM (phenotype) | **617751** | Quoted in PMID:37059841 and PMID:35139179 |
| OMIM (gene) | RAC1 **602048** | PMID:37059841 |
| MONDO | MONDO:0030913 | From the template; check its label and status in `cache/mondo/terms.csv` (that file has uncommitted changes in this worktree) |
| HGNC | RAC1 = hgnc:9801 **[verify]** | Use the lowercase `hgnc:` prefix |
| Orphanet / ICD-10 / ICD-11 / MeSH | Not verified | No disease-specific Orphanet code was confirmed. Expect a generic ID code (for example ICD-10 F7x / Q-codes) rather than a specific one |

**Synonyms:** Intellectual developmental disorder, autosomal dominant 48; MRD48; RAC1-related neurodevelopmental disorder (RAC1-NDD, PMID:35139179); RAC1-related intellectual developmental disorder (PMID:39838818).

**Basis of knowledge.** Everything comes from individual-patient case series: about 7 patients in 2017, 8 in 2022, 2 in 2023, and further single cases from 2023 to 2025. The 2026 switch II paper reports 15 new individuals but gives clinical detail for only 6. No registry or EHR-level data exist.

**Lump/split note for curation.** The 2026 paper says *"variants affecting N- and C-terminal parts of RAC1 switch II cause phenotypically and mechanistically distinct disorders"* (PMID:42120539). Recommendation: keep one Disease entry anchored to OMIM 617751 / MONDO, and model functional-class strata as `has_subtypes`:
- dominant-negative / microcephalic;
- activating switch II N-terminal (Q61–R68) / normocephalic;
- macrocephalic (V51).

There are no separate MONDO terms for these strata.

---

## 2. Etiology

- **Cause:** a monoallelic germline missense variant in RAC1 (7p22.1), almost always de novo.
- **Variant spectrum:** missense only. *"RAC1 is highly conserved across species and is under strict mutational constraint"* (PMID:28886345).
- **Variant classes:** loss-of-function (truncating) variants and deletions have not been reported as a cause. Complete Rac1 loss is embryonic lethal in mice, so the disease appears to require dominant-negative or activating missense alleles rather than haploinsufficiency. That last point is an inference, not a demonstrated result.
- **Risk factors:** none are known apart from the de novo event (advanced parental age is not documented). No environmental, protective or gene–environment factors have been reported.
- **Double diagnosis.** One patient's sensorineural deafness was explained by a separate pathogenic GRHL2 nonsense variant (DFNA28) inherited from the father (PMID:37059841). This matters when attributing hearing loss to RAC1.

---

## 3. Phenotypes

Frequencies come from the 10-patient review in PMID:37059841. The denominator is the number of patients assessed for each feature:

> *"all subjects shared ID with speech delay (10/10 and 7/7, respectively), a wide array of brain abnormalities (8/8) … behavioral abnormalities (5/6), hypotonia and neonatal/childhood feeding difficulties (5/7 and 5/8, respectively). CHDs were also common (4/8), while epilepsy was reported in 3/8 subjects. We also observed recurrent ectodermal anomalies, mainly represented by eczematous rashes, with or without ichthyosiform manifestations (4/10), and various skeletal anomalies (3/10), such as small hands and feet (3/10)."*

| Phenotype | Frequency | Onset / course | Suggested HPO **[verify all]** | Source |
|---|---|---|---|---|
| Intellectual disability (mild to severe; 5/10 mild–moderate) | 10/10 | Infancy/childhood; static. Regression was reported once (worsening from age 12) | HP:0001249 Intellectual disability | 37059841 |
| Global developmental delay | Near-universal | Infancy | HP:0001263 | 28886345, 35139179 |
| Speech delay | 7/7 | Childhood | HP:0000750 Delayed speech and language development | 37059841 |
| Brain anomalies (polymicrogyria/pachygyria, corpus callosum hypoplasia, cerebellar vermis hypoplasia/dysgenesis, enlarged ventricles, mega cisterna magna, thin brainstem, white matter lesions) | 8/8 | Congenital | HP:0002126 Polymicrogyria; HP:0001338 Partial agenesis of the corpus callosum or HP:0002079 Hypoplasia of the corpus callosum; HP:0001320 Cerebellar vermis hypoplasia | 37059841 table; 35139179 |
| Microcephaly (−2.5 to −5 SD) | DN variants (C18Y, N39S, P73L, C157Y; switch II C-terminal P69–Q74; E31G acquired) | Congenital or acquired | HP:0000252 Microcephaly | 28886345, 42120539, 39307291 |
| Macrocephaly (+4.16 / +4.5 SD) | V51M/V51L | Congenital | HP:0000256 Macrocephaly | 28886345 |
| Normocephaly | Activating switch II Q61–R68 variants | – | – | 35139179, 42120539 |
| Behavioural anomalies (ASD, impulsivity, compulsivity, anxiety, stereotypies) | 5/6 | Childhood/adolescence | HP:0000729 Autistic behavior; HP:0000708 Behavioral abnormality; HP:0000733 Motor stereotypy | 37059841 |
| Hypotonia | 5/7 | Neonatal/infantile | HP:0001252 Hypotonia | 37059841 |
| Feeding difficulties | 5/8 | Neonatal/childhood | HP:0011968 Feeding difficulties | 37059841 |
| Congenital heart defects (septal defects, BAV, pulmonary valve stenosis, PDA, PFO, outflow tract) | 4/8 (5/10 in the discussion) | Congenital | HP:0001627 Abnormal heart morphology; HP:0001631 Atrial septal defect; HP:0001629 Ventricular septal defect; HP:0001647 Bicuspid aortic valve | 37059841, 35139179 |
| Seizures | 3/8 | Childhood | HP:0001250 Seizure | 37059841 |
| Ectodermal anomalies: eczema, ichthyosiform skin | 4/10 | Childhood | HP:0000964 Eczema; HP:0008064 Ichthyosis | 37059841, 34725860 |
| Small hands/feet, skeletal anomalies | 3/10 | Congenital | HP:0200055 Small hand; HP:0001773 Short foot | 37059841 |
| Sensorineural deafness | 2/10 (one has an alternative GRHL2 explanation) | Congenital/childhood | HP:0000407 Sensorineural hearing impairment | 37059841 |
| Hydronephrosis | 2/10 | Congenital | HP:0000126 Hydronephrosis | 37059841 |
| Ocular findings (myopia, chorioretinal atrophy, congenital cataract, visual impairment) | Isolated | – | HP:0000545 Myopia; HP:0000519 Congenital cataract | 37059841 table |
| Facial gestalt (see below) | 6–9/9 per feature | Softens with age | Individual facial HPO terms | 37059841 |

**Facial gestalt.** From systematic review of photographs: *"high anterior hairline (9/9), arched eyebrows (8/9) with tendency to lateral sparse (7/9) … mild widely spaced eyes (8/9), wave-shaped palpebral fissures (7/9), overhanging columella (6/9) … short philtrum (7/9), deep nasolabial folds (8/9), thin upper lip (7/9), abnormally spaced teeth … (6/6) … and a long pointed chin (7/9)."* The same paper notes that *"widely spaced eyes, bulbous nasal tip and prominent nasolabial folds tend to smoothen in adolescents and young adults"* (PMID:37059841).

Some HPO terms to check for these features: HP:0000294 Low anterior hairline (do not use; the feature here is a *high* hairline), HP:0002668 Arched eyebrow, HP:0000316 Hypertelorism, HP:0000322 Short philtrum, HP:0000219 Thin upper lip vermilion, HP:0000687 Widely spaced teeth. **[verify all]**

**Severe or atypical presentations.**
- **p.Tyr40His** (Seyama 2023, PMID:37328543): a VACTERL-like presentation with fatal tracheal aplasia. *"the patient died of respiratory failure caused by tracheal aplasia type III."* Other features were TAPVR, oesophageal atresia, scoliosis and polydactyly.
- **Mild cases:** Upadia et al. 2025 (PMID:39838818) widen the mild end of the spectrum: *"We present one case with typical phenotype and two cases with a mild phenotype."*

**Quality of life.** No studies using standard instruments (EQ-5D, PedsQL) were found. The burden is inferred from ID, behavioural disorder and congenital heart disease.

---

## 4. Genetic and molecular information

- **Gene:** RAC1 (Rac family small GTPase 1), 7p22.1, OMIM 602048, hgnc:9801 **[verify]**. Reference transcripts are NM_006908 (RAC1) and NM_018890 (RAC1B, which carries an extra exon 4) (PMID:28886345).
- **Inheritance:** autosomal dominant (HP:0000006 **[verify]**). All reported cases are de novo (HP:0025352 *de novo* **[verify]**).

**Reported pathogenic variants and functional class**

| Variant (NP_008839) | Region | Head size | Functional effect | Evidence |
|---|---|---|---|---|
| p.Cys18Tyr (c.53G>A) | P-loop/G1 vicinity | Microcephaly | **Dominant-negative**; blocks GTP-mediated activation and LTP | 28886345; 30042656 |
| p.Glu31Gly (c.92A>G) | Switch I | Acquired microcephaly | DN toward PAK1 | 39307291 |
| p.Asn39Ser (c.116A>G) | Switch I | Microcephaly | **Dominant-negative** | 28886345 |
| p.Tyr40His (c.118T>C) | PAK1-binding site, adjacent to switch I | Lethal, VACTERL-like | Inactivates PAK1 signalling | 37328543 |
| p.Val51Met / p.Val51Leu (c.151G>A/C) | β2–β3 | **Macrocephaly** | Context-dependent / unclear | 28886345 |
| p.Gln61–p.Arg68 (incl. p.Tyr64Asp c.190T>G, p.Glu62Lys c.184G>A) | Switch II N-terminal | Normocephaly | **Activating / gain of function** | 28886345, 35139179, 37059841, 42120539 |
| p.Pro69–p.Gln74 (incl. p.Pro73Leu c.218C>T) | Switch II C-terminal | Microcephaly | **Dominant-negative** | 28886345, 42120539 |
| p.Cys157Tyr (c.470G>A) | G5 box | Microcephaly | Weak DN / context-dependent | 28886345 |
| p.Ala159Thr (c.475G>A) | G5 nucleotide-binding pocket | Normocephaly | **Constitutively active** (like the oncogenic A159V) | 37059841 |

- **Classification and ClinVar.** The two Priolo variants are ACMG Pathogenic (ClinVar SCV002605544 and SCV002605545). They are absent from gnomAD v2.1.1 (PMID:37059841).
- **ClinGen.** I did not check whether a gene–disease validity curation exists. Run `just list-gene-validity` / `clingen-list` before filling `gene_disease_validity`, and do not assign a tier yourself.
- **Mechanistic summary:** *"Structural and functional studies have documented either a dominant negative or constitutively active behavior for a subset of mutations"* (PMID:37059841). In the 2026 switch II study: *"N-terminal variants are activating, while C-terminal variants are dominant-negative"* (PMID:42120539).
- **Hotspots shared with paralogs:** *"recurring variants at specific residues (E62 and Y64 in G3/Switch II) were reported in all proteins"* (RAC1–3, CDC42; PMID:37059841).
- **Not reported:** modifier genes, epigenetic signatures (no published episignature) and chromosomal abnormalities (CNVs) as a cause.

**Suggested `functional_impact_category` values:**
- `DOMINANT_NEGATIVE` for the C18Y, N39S, E31G and C-terminal switch II variants;
- `GAIN_OF_FUNCTION` (or `HYPERMORPHIC`) for Y64D, E62K, A159T and the other Q61–R68 variants.

---

## 5. Environmental information

Not applicable. No environmental, lifestyle or infectious contributors have been reported.

---

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. A **de novo heterozygous missense variant in RAC1** alters the GTP/GDP switch. It does so either by disrupting nucleotide binding or effector binding (C18, N39, Y40, E31, P69–Q74, C157), or by locking RAC1 in the GTP-bound state (Q61–R68, A159).
2. **Branch A (dominant-negative alleles):** the mutant protein fails to activate effectors such as PAK1. For C18Y it occludes the GTP pocket (*"this mutation will strongly inhibit Rac1 activation by occluding Rac1's GTP binding pocket"*, PMID:30042656). This **leads to reduced RAC1 signalling**: less actin polymerisation and lamellipodia formation.
   - 2a → **reduced neural progenitor proliferation** → **microcephaly** and cerebellar anomalies. This was demonstrated in zebrafish overexpression (PMID:28886345). Its relevance to human cortex is inferred.
   - 2b → impaired axon elongation and dendritic arborisation (E31G, in utero electroporation in mouse, PMID:39307291) → abnormal connectivity.
   - 2c → in hippocampal neurons, **loss of synaptic AMPA receptor function and failed LTP induction** (*"results in a selective reduction in synaptic AMPA receptor function… prevents the induction of long-term potentiation (LTP)"*, PMID:30042656) → this is argued to contribute to ID (the link to ID is inferred).
3. **Branch B (activating alleles):** a higher fraction of GTP-bound RAC1 → **over-activation of PAK1/2/3 and of the WAVE regulatory complex (WRC)/Arp2/3** (PMID:35139179) → excess actin branching:
   - shorter axons with more filopodia, axon fasciculation defects, and dendrite over-branching with loss of self-avoidance (Drosophila Y64D);
   - these defects are **rescued by Cyfip knockdown** (*"RNAi knock down of the WAVE regulatory complex component Cyfip significantly rescues these morphological defects"*).
   - → abnormal neuronal morphology and cortical malformation (polymicrogyria) → ID, seizures, and normocephaly or mild macrocephaly.
4. **Extra-neural branch (inferred from mouse models):** RAC1 dysfunction in **neural crest cells and the second heart field** → outflow tract and septal defects and craniofacial dysmorphism. *"the perturbed development of neural crest cell (NCC)-derived tissues documented in NCC-targeted Rac1 conditional KO mice may explain both craniofacial and cardiac features"* (PMID:37059841). This step is inferred and has not been shown with patient alleles.
5. **Macrocephaly (V51):** the mechanism is unresolved, described as "context dependent" (PMID:28886345). Mention of mTOR involvement in RAC1 biology is background only and has not been shown for these alleles.

### Pathways and processes, with ontology suggestions **[verify all]**

- **Molecular function:** GTPase activity (GO:0003924); GTP binding (GO:0005525).
- **Biological processes:**
  - small GTPase-mediated signal transduction (GO:0007264);
  - actin cytoskeleton organization (GO:0030036);
  - lamellipodium assembly (GO:0030032);
  - Arp2/3 complex-mediated actin nucleation (GO:0034314);
  - axonogenesis (GO:0007409);
  - dendrite morphogenesis (GO:0048813);
  - neural precursor cell proliferation (GO:0061351);
  - long-term synaptic potentiation (GO:0060291);
  - neural crest cell migration (GO:0001755).
- **Effectors:** PAK1 (hgnc:8590 **[verify]**), WAVE2/WASF2, CYFIP1/2, Arp2/3.
- **Cell types:** neural progenitor cell (CL:0011020), neuron (CL:0000540), hippocampal pyramidal neuron, cerebellar neurons, cranial or cardiac neural crest cell (CL:0000333 neural crest cell). **[verify]**
- **Subcellular location:** actin cytoskeleton / lamellipodium (GO:0030027), plasma membrane, postsynaptic density (GO:0014069), dendritic spine (GO:0043197). **[verify]**
- **Omics:** no transcriptomic, proteomic, metabolomic, single-cell or CRISPR-screen data for MRD48 were found.
- **Biological scale tags for the pathograph:**
  - RAC1 GTPase switch defect: MOLECULAR;
  - PAK/WRC over-activation or under-activation: CELLULAR;
  - progenitor proliferation and neuronal morphology: CELLULAR;
  - cortical malformation and microcephaly: TISSUE.

---

## 7. Anatomical structures affected

- **Primary:** brain, including cerebral cortex (polymicrogyria/pachygyria), corpus callosum, cerebellar vermis, brainstem/pons and lateral ventricles. UBERON candidates **[verify]**: UBERON:0000955 brain, UBERON:0000956 cerebral cortex, UBERON:0002336 corpus callosum, UBERON:0004720 cerebellar vermis.
- **Secondary:** heart (septa, valves, outflow tract; UBERON:0000948), craniofacial skeleton, skin, kidney (hydronephrosis), inner ear and eye. Rare cases involve the trachea and oesophagus (p.Y40H).
- **Laterality:** malformations are generally bilateral or midline. One case had left fronto-insular pachygyria.

---

## 8. Temporal development

- **Onset:** congenital, with brain and heart malformations present at birth. DD becomes apparent in infancy. Microcephaly can be congenital or acquired (E31G, PMID:39307291).
- **Course:** a static neurodevelopmental disorder. No degenerative course is documented. Behavioural and psychiatric problems may emerge in adolescence; one patient's competences worsened from age 12 (PMID:37059841). The facial gestalt changes with age.
- **Mortality:** one neonatal death, from tracheal aplasia (p.Y40H).
- **Critical period:** prenatal neurogenesis and neural crest development (inferred).

---

## 9. Inheritance and population

- **Inheritance pattern:** autosomal dominant, essentially always de novo.
- **Penetrance:** apparently complete for reported alleles, though the evidence is limited. No familial transmission has been reported.
- **Expressivity:** highly variable, with a strong allele-to-phenotype correlation for head size.
- **Not reported:** anticipation, founder effects, a role for consanguinity, and parental germline mosaicism. For counselling, a low recurrence risk (about 1%, the generic figure for de novo disorders) applies.
- **Prevalence:** unknown. Roughly 30 individuals have been described in the literature (7 + 8 + 2 + ~3 single cases + 15 in 2026, allowing for overlap).
  - Suggested KB record: `measure_type: CASES_IN_LITERATURE` with `prevalence_class: ULTRA_RARE` or `NOT_YET_DOCUMENTED`.
  - Source the count from the specific papers; do not invent a rate.
- **Sex ratio and ancestry:** both sexes are affected; no ancestry bias has been noted.

---

## 10. Diagnostics

- **Method:** diagnosis is molecular, by **trio exome or genome sequencing**. Most cases came through DDD trio WES or clinical WES after a normal chromosomal microarray (CMA) (PMID:28886345, 37059841). RAC1 is on most ID/NDD panels.
- **Variant interpretation:**
  - de novo status plus a constrained missense position support pathogenicity;
  - functional assays used in research are RAC1-GTP pulldown (PAK-CRIB), fibroblast spreading/roundness index, and phospho-PAK and WAVE2 staining (PMID:35139179, 37059841).
- **Imaging:** brain MRI (polymicrogyria, corpus callosum and cerebellar anomalies), echocardiography and renal ultrasound.
- **Other workup:** EEG if seizures occur; audiology; ophthalmology.
- **Biomarkers:** none (no metabolic or laboratory markers).
- **Differential diagnosis:**
  - RAC3-related NEDBAF (OMIM 618577): more severe ID, more frequent corpus callosum and brainstem/cerebellar dysplasia, upslanted fissures and upturned nares (PMID:37059841);
  - CDC42-related Takenouchi–Kosaki syndrome;
  - TRIO-related NDD;
  - HACE1 disorder;
  - RASopathies (Noonan, CFC, Costello);
  - other polymicrogyria or microcephaly genes;
  - VACTERL for the Y40H-type presentation.
- **Screening:** there is no newborn or carrier screening. Prenatal ultrasound may detect anomalies (as in the Y40H case).

---

## 11. Outcome and prognosis

- **Natural history:** no formal studies. Most individuals survive into adolescence or adulthood; patients aged 14 and 27 are described in PMID:37059841.
- **Mortality:** the main reported fatality was neonatal, from tracheal aplasia (PMID:37328543).
- **Morbidity:** driven by ID (mild to severe), behavioural disorder or ASD, epilepsy, and congenital heart disease.
- **Prognostic factors (tentative):**
  - dominant-negative / microcephalic variants and severe brain malformations tend to go with more severe ID;
  - RAC1 overall is milder than RAC3: *"subjects with pathogenic RAC1 variants show a milder developmental involvement (5/10 with mild to moderate DD/ID) compared to individuals with RAC3 mutations"* (PMID:37059841).
- **Not available:** survival rates, life-expectancy data, and QoL instrument studies.

---

## 12. Treatment

There is no disease-specific or approved therapy, and no clinical trials. Supportive, multidisciplinary management:

| Intervention | NCIT suggestion **[verify]** | `therapeutic_modality` |
|---|---|---|
| Early intervention / special education; speech therapy | Speech language therapy NCIT:C159273 | BEHAVIORAL |
| Physical / occupational therapy for hypotonia | NCIT:C15302 Physical Therapy; NCIT:C121351 Occupational Therapy | BEHAVIORAL |
| Antiseizure medication | NCIT:C15986 Pharmacotherapy (+ agent if one is named) | SMALL_MOLECULE |
| Cardiac surgery for CHD | NCIT:C15329 Surgical Procedure | SURGERY |
| Feeding support / nutrition | NCIT:C15433 Nutritional Support (review per case; do not tag mechanically) | – |
| Behavioural / psychiatric management | Behavioral counseling NCIT:C181743 | BEHAVIORAL |
| Hearing aids (if deaf) | Device; use a qualifier pattern per CLAUDE.md | DEVICE |
| Genetic counselling | NCIT:C15240 | – |

**Experimental and preclinical leads only:**
- For activating alleles, the **WAVE regulatory complex/Arp2/3 pathway** has been proposed as a target: *"reveal the WAVE regulatory complex/Arp2/3 pathway as a possible therapeutic target for activating RAC1 variants"* (PMID:35139179). This rests on Drosophila Cyfip knockdown only.
- RAC1 inhibitors (e.g., NSC23766, EHT1864) are research tools and have not been tested in patients.
- Because the functional classes are opposite, any targeted therapy would need to be **allele-class-specific**.

---

## 13. Prevention

- **Primary prevention:** none, because the disease arises de novo.
- **Reproductive options:** genetic counselling, with low recurrence risk but parental mosaicism to be considered. Prenatal or preimplantation testing can be offered once a familial variant is known.
- **Tertiary prevention:**
  - echocardiography and renal ultrasound at diagnosis;
  - hearing and vision screening;
  - developmental and behavioural surveillance;
  - seizure monitoring.

---

## 14. Other species and natural disease

- **Animals:** no naturally occurring RAC1 disease is known (OMIA not checked).
- **Conservation:** RAC1 is highly conserved. Orthologs: mouse *Rac1*, zebrafish *rac1a/rac1b*, Drosophila *Rac1*. The disease is not zoonotic.

---

## 15. Model organisms

| Model | Type | Findings | Fidelity / limits | PMID |
|---|---|---|---|---|
| Zebrafish embryo, overexpression of human C18Y and N39S | Transient overexpression | Microcephaly, reduced neuronal proliferation, cerebellar abnormalities | PARTIALLY_RECAPITULATES microcephaly. Overexpression is supraphysiological, and zebrafish lack cortical organisation | 28886345 |
| Drosophila *Rac1-Y64D* (UAS/Gal4: elav, ppk) | Transgenic | Short axons, more filopodia, fasciculation defects, dendrite over-branching; Cyfip RNAi rescue | Shows the GoF cellular mechanism; invertebrate, with no cortex or head-size readout | 35139179 |
| Drosophila switch II N- vs C-terminal variants | Transgenic | N-terminal: more dendritic complexity and locomotor hyperactivity; C-terminal: less complexity | Behavioural readout only in flies | 42120539 |
| Mouse in utero electroporation of RAC1-E31G | Acute cortical expression | Impaired axon elongation and dendritic arborisation | Overexpression, not knock-in | 39307291 |
| Rat/mouse hippocampal neurons (slice) with C18Y | Ex vivo / in vitro | Loss of AMPA receptor currents; LTP blocked | IN_VITRO; links to the learning mechanism | 30042656 |
| Mouse *Rac1* KO and conditional KOs (forebrain, neural crest, second heart field) | Knockout | Germline KO is embryonic lethal; forebrain cKO causes microcephaly, migration and dendrite defects; neural crest and SHF cKO cause craniofacial and outflow tract/right ventricular defects | Null alleles, not the patient DN/GoF missense alleles | Reviewed in 28886345, 37059841 (Supplementary Table S5) |
| COS-1/COS7, HEK293T, NIH3T3 cells | Cell lines | GTP-loading, PAK binding, cell spreading/roundness | IN_VITRO | 37059841, 35139179, 37328543 |

**Gap:** no patient-allele knock-in mouse or iPSC/organoid model was identified. A `HUMAN_MODEL_MISMATCH` discussion would fit here: the microcephaly and neuron-morphology mechanisms rest on zebrafish and Drosophila overexpression rather than human cortical tissue.

---

## Key references (all cached locally)

| PMID | Citation | Evidence type |
|---|---|---|
| 28886345 | Reijnders MRF et al. *RAC1 Missense Mutations in Developmental Disorders with Diverse Phenotypes.* Am J Hum Genet 2017. doi:10.1016/j.ajhg.2017.08.007 | Founding report; human clinical + MODEL_ORGANISM (zebrafish) + IN_VITRO |
| 30042656 | Tian C et al. *An Intellectual Disability-Related Missense Mutation in Rac1 Prevents LTP Induction.* Front Mol Neurosci 2018 | IN_VITRO / ex vivo |
| 34725860 | Haugh IM et al. *Ichthyosiform changes in a patient with RAC1 mutation.* Pediatr Dermatol 2021 | Case report |
| 35139179 | Banka S et al. *Activating RAC1 variants in the switch II region cause a developmental syndrome and alter neuronal morphology.* Brain 2022 | Human clinical + Drosophila + IN_VITRO |
| 37059841 | Priolo M et al. *Clinical profiling of MRD48 and functional characterization of two novel pathogenic RAC1 variants.* Eur J Hum Genet 2023 | Clinical review with frequencies + IN_VITRO |
| 37328543 | Seyama R et al. *A missense variant at the RAC1-PAK1 binding site of RAC1 inactivates downstream signaling in VACTERL association.* Sci Rep 2023 | Case report + IN_VITRO |
| 39307291 | Nishikawa M et al. *Pathophysiological significance of the p.E31G variant in RAC1…* Biochim Biophys Acta Mol Basis Dis 2025 | Case report + mouse in utero electroporation |
| 39838818 | Upadia J et al. *Diverse Clinical Presentation of RAC1-Related Intellectual Developmental Disorder.* Am J Med Genet A 2025 | Case series (abstract only) |
| 42120539 | Althebaiti HO et al. *Distinct sub-clusters of developmental disorder-associated variants in the switch II region of RAC1.* Eur J Hum Genet 2026 | Human clinical + Drosophila + IN_VITRO (abstract only) |

## Curation cautions

1. **Evidence classification for mixed papers.** Reijnders, Banka and Althebaiti each report patients, cell assays and animal models. Split their evidence items by `evidence_source`.
2. **Frequency denominators.** Use the per-feature denominators from PMID:37059841 (for example 5/7 for hypotonia), not a blanket n=10.
3. **Deafness attribution.** Do not attribute sensorineural deafness solely to RAC1. One of the two cases is explained by GRHL2.
4. **Abstract-only references.** PMID:39838818, 39307291, 34725860 and 42120539 are abstract-only in the cache, so snippets must come from those abstracts.
5. **Unchecked CURIEs.** Every CURIE marked [verify] must be looked up. This includes MONDO:0030913's label, the HGNC ID for RAC1, all HP/GO/CL/UBERON IDs, and the NCIT treatment terms.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 9 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 66 |
| Resolved | 66 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 15 |
| Terms named correctly | 9 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0030913` (3 mentions) - the report calls it "MONDO"; MONDO calls it **intellectual disability, autosomal dominant 48**
- `HP:0001263` (1 mention) - the report calls it "Infancy"; HP calls it **Global developmental delay**
- `GO:0030027` (1 mention) - the report calls it "Subcellular location:** actin cytoskeleton / lamellipodium"; GO calls it **lamellipodium**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0003924` (1 mention) - the report calls it "Molecular function:** GTPase activity"; GO calls it **GTPase activity**, and lists "tubulin GTPase activity" among its other names
- `CL:0011020` (1 mention) - the report calls it "Cell types:** neural progenitor cell"; CL calls it **neural progenitor cell**
- `NCIT:C15240` (1 mention) - the report calls it "Genetic counselling"; NCIT calls it **Genetic Counseling**