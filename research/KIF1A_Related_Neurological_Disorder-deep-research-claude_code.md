---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5-5
cached: false
start_time: '2026-10-01T10:31:48.664169'
end_time: '2026-10-01T10:35:25.450484'
duration_seconds: 216.79
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: KIF1A-Related Neurological Disorder
  mondo_id: MONDO:0700055
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
  - claude-opus-5-5
  web_search_requests: 10
  num_turns: 19
  total_cost_usd: 2.1901074000000005
  session_id: 9c60f84b-07a9-4f45-a461-e780ec246178
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
citation_count: 15
reference_validation:
  total_references: 17
  verified: 17
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 3
  quotes_valid: 3
  relevance_assessed: 17
  on_topic: 13
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 77
  verified: 76
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 8
  labels_matching: 5
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0700055
    reported_labels:
    - MONDO
    - SAIL concept library
    ontology_label: KIF1A related neurological disorder
  - term_id: NCIT:C15986
    reported_labels:
    - Baclofen, tizanidine; botulinum toxin injection
    ontology_label: Pharmacotherapy
  labels_variant: 1
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** KIF1A-Related Neurological Disorder
- **MONDO ID:** MONDO:0700055 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **KIF1A-Related Neurological Disorder** covering all of the
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

Found the core identifiers, mechanism papers, and treatment reports. Next I'm pulling phenotype frequencies from the full texts already cached locally, then I'll write the report.

# KIF1A-Related Neurological Disorder (KAND; MONDO:0700055): research report

**Prepared:** 2026-10-01. **Scope:** a source dossier for curating `kb/disorders/KIF1A_Related_Neurological_Disorder.yaml`.

**How to read this report**
- **Cached quotes.** Quotes marked ✅ come word-for-word from `references_cache/PMID_*.md` files already in this worktree, so they can be used directly as `snippet:` values.
- **Uncached sources.** Other PMIDs or sources are leads. Fetch them with `just fetch-reference` and confirm the wording before quoting.
- **Ontology IDs.** All ontology CURIEs below are candidates I recalled from memory. CLAUDE.md requires every one to be looked up with `runoak` or the term cache before it is written into the entry.

---

## 1. Disease information

**Overview.** KAND is a spectrum of rare neurodevelopmental and neurodegenerative conditions. They are caused by pathogenic variants in *KIF1A*, which encodes a neuron-specific kinesin-3 motor that carries synaptic vesicle precursors (SVPs) and dense-core vesicles forward along axons.
- ✅ PMID:33880452 (Boyle et al. 2021, HGG Adv): "KIF1A-associated neurological disorder (KAND) encompasses a group of rare neurodegenerative conditions caused by variants in KIF1A,a gene that encodes an anterograde neuronal microtubule (MT) motor protein."
- The GeneReviews chapter "KIF1A-Related Neurodevelopmental Disorder" (NBK621569; Chung lab authorship) describes it as "both a developmental and degenerative condition with a broad phenotypic spectrum commonly including developmental delay, communication difficulties, optic nerve atrophy, seizures, progressive spastic paraplegia, peripheral and autonomic neuropathy, poor weight gain, and neurobehavioral issues including autism spectrum disorder" ([NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/NBK621569/)).
  - I could not fetch the page (it is behind a reCAPTCHA). The quote comes from search-result text.
  - Run `just check-genereviews` and fetch the chapter's PMID before citing it. Per review item 15, GeneReviews is the required phenotype baseline for a Mendelian entry.

**Identifiers**

| System | ID | Notes |
|---|---|---|
| MONDO | MONDO:0700055 | "KIF1A-related neurological disorder" ([SAIL concept library](https://conceptlibrary.saildatabank.com/api/v1/ontology/node/MONDO:0700055/)) |
| OMIM gene | 601255 | KIF1A, 2q37.3 |
| OMIM phenotype: NESCAV syndrome (AD) | 614255 | Formerly "mental retardation, AD 9" (MRD9) |
| OMIM phenotype: SPG30A (AD) | 610357 | |
| OMIM phenotype: SPG30B (AR) | 620607 | Recessive SPG30 now has its own entry ([OMIM mirror](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/620607)) |
| OMIM phenotype: HSN2C (AR) | 614213 | Hereditary sensory neuropathy IIC |
| Orphanet | ORPHA:178469 (?) | Reported by one search snippet only. **Unverified; confirm before use.** |
| HGNC | hgnc:888 (KIF1A) | Verify against `cache/hgnc/terms.csv` |
| MeSH | none disease-specific | Use "Kinesins/genetics" or "Spastic Paraplegia, Hereditary" |

**Synonyms:** KIF1A-associated neurological disorder; KIF1A-associated neuronal disorder; KIF1A-related neurodevelopmental disorder (KIF1A-NDD, the GeneReviews name); NESCAV syndrome (neurodegeneration and spasticity with or without cerebellar atrophy or cortical visual impairment); MRD9; SPG30.

**Source of data:** all disease-level knowledge comes from aggregated cohorts and case series, not EHR data. The main sources are:
- the KIF1A.ORG–Columbia natural-history cohort (n = 117);
- the Dutch HSP exome cohort (n = 347);
- Italian multicentre series;
- the KOALA prospective study.

**Lump/split note for curation.** MONDO:0700055 is the umbrella term. NESCAV, SPG30A, SPG30B and HSN2C are natural `has_subtypes` rows, with MONDO-bound terms if they exist. The case for lumping: severity runs on a continuous spectrum across the subtypes (PMID:32737135, PMID:34487232, PMID:33880452).

## 2. Etiology

**Cause.** The disorder is monogenic and caused by *KIF1A* variants.
- Most cases are heterozygous de novo missense variants in the motor domain.
- Rarer forms:
  - biallelic variants (recessive SPG30B and HSN2C);
  - inherited dominant variants (SPG30A);
  - heterozygous loss-of-function variants outside the motor domain (dominant HSP).
- ✅ PMID:25265257 (Lee et al. 2015): "Here, we report 11 heterozygous de novo missense mutations (p.S58L, p.T99M, p.G102D, p.V144F, p.R167C, p.A202P, p.S215R, p.R216P, p.L249Q, p.E253K, and p.R316W) in KIF1A in 14 individuals, including two monozygotic twins." and "All these de novo mutations are located in the motor domain (MD) of KIF1A."
- ✅ PMID:21487076 (Erlich 2011, the first recessive HSP family): "Our analysis implicated the causative mutation in the motor domain of KIF1A, a gene that has not yet associated with HSP, which functions in anterograde axonal transportation."
- ✅ PMID:21820098 (Rivière 2011, HSAN2): "Sequencing of KIF1A in this family revealed a truncating mutation segregating with the disease phenotyp…" Read the full sentence in the cache before quoting it.

**Risk factors:**
- The main risk factor is a de novo germline mutation.
- Parental germline or somatic mosaicism explains rare recurrence. One mosaic proband appears in Boyle 2021.
- Consanguinity matters for the recessive SPG30B and HSN2C forms (Palestinian and Afghan families: PMID:21487076, PMID:21820098).

**Environmental, protective, and gene–environment factors:** none are documented, and the disease is not known to be modifiable by exposure. Fever and intercurrent illness are anecdotally reported to lower the seizure threshold, but I found no primary citation for this. Do not curate an `environmental:` entry without one.

**Genetic modifiers:** none have been established in humans. In *C. elegans*, an intragenic suppressor restores the motility of mutant KIF1A (PMID:35917346; see section 15).

## 3. Phenotypes

The main frequency source is Boyle 2021 Table 1 (✅ cached full text, n = 100), supplemented by Bernardi 2026 (✅ PMID:42500835, n = 51) and Abdelhakim 2024 (✅ PMID:39009236, n = 24).

| Phenotype | Frequency (source) | Candidate HPO (verify) | Notes |
|---|---|---|---|
| Developmental delay / intellectual disability | 92% (92/100) [Boyle]; global developmental delay 96.1% [Bernardi] | HP:0001263 Global developmental delay; HP:0001249 Intellectual disability | Onset in infancy. Cognitive regression is largely absent. |
| Hypotonia (neonatal/infantile) | 84% [Boyle]; 62.7% [Bernardi] | HP:0001252 Hypotonia | Early sign, typically followed later by spasticity |
| Hypertonia/spasticity, progressive, lower-limb predominant | 81% [Boyle]; 72.5% progressive [Bernardi] | HP:0001257 Spasticity; HP:0002061 Lower limb spasticity | Correlates with age (OR 1.56) |
| Lower-extremity weakness | 88.2% [Bernardi] | HP:0007340 Lower limb muscle weakness | |
| Loss of independent ambulation | 62.7% achieve walking; 31.4% retain it [Bernardi] | HP:0002540 Inability to walk | "By the time they reached their 20s, many individuals were largely wheelchair dependent" ✅ Boyle |
| Optic nerve atrophy/hypoplasia | 50% [Boyle]; 95% on exam/OCT [Abdelhakim] | HP:0000648 Optic atrophy | Progressive; prevalence underestimated without OCT |
| Cortical visual impairment | 20% [Boyle] | HP:0100704 Cortical visual impairment | |
| Strabismus | 26% [Boyle]; ~40% [Abdelhakim] | HP:0000486 Strabismus | |
| Seizures (overall) | 42% [Boyle] | HP:0001250 Seizure | Absence most common: 29% of the cohort, 69% of those with seizures |
| Absence / generalized tonic-clonic / atonic / infantile spasms | 29% / 17% / 9% / 4% | HP:0002121; HP:0002069; HP:0010819; HP:0012469 | |
| Abnormal brain MRI | 58% (54/93) | HP:0012443 Abnormality of brain morphology | |
| Cerebellar atrophy | 35% [Boyle]; 65% [literature] | HP:0001272 Cerebellar atrophy | Progressive; vermis-predominant at autopsy |
| Corpus callosum hypoplasia/atrophy | 11% | HP:0002079 Hypoplasia of the corpus callosum | |
| Cerebral atrophy | 6% | HP:0002059 Cerebral atrophy | |
| Microcephaly | 18% | HP:0000252 Microcephaly | Associated with earlier onset |
| Peripheral neuropathy (axonal, sensorimotor) | 27% [Boyle]; 38% [literature] | HP:0009830 Peripheral neuropathy; HP:0003477 Peripheral axonal neuropathy | Prominent in HSN2C, with acral ulceration and mutilation |
| Ataxia / cerebellar signs | 19.6% ataxia; 37.2% cerebellar signs [Bernardi] | HP:0001251 Ataxia | Congenital ataxia group (PMID:32737135) |
| Motor stereotypies; tremor; dystonia | 43.1%; 15.6%; 3.9% [Bernardi] | HP:0000733 Stereotypy; HP:0002345 Action tremor; HP:0001332 Dystonia | |
| Autism / ADHD / anxiety / OCD | 20% / 24% / 19% / 5% (n = 80) | HP:0000729; HP:0007018; HP:0000739; HP:0000722 | |
| Rett-like features | Hand stereotypies 21%, bruxism 35%, high pain tolerance 65% | HP:0012171 Stereotypical hand wringing; HP:0003763 Bruxism | Some patients were clinically diagnosed with Rett syndrome |
| Dysautonomia-like features | Temperature dysregulation 46%, sialorrhea 26%, dysphagia 29% | HP:0004370 Abnormality of temperature regulation; HP:0002307 Drooling; HP:0002015 Dysphagia | |
| GERD / constipation / diarrhea | 40% / 39% / 17% | HP:0002020; HP:0002019; HP:0002014 | 10% need enteral feeding |
| Short stature; growth hormone deficiency | 13%; 3% | HP:0004322; HP:0000824 | |
| Scoliosis | 14% | HP:0002650 Scoliosis | |
| Small penis/scrotum | 17% of males (9/53) | HP:0008736 Hypoplasia of penis | Newly described |

**Key ✅ quotes**
- PMID:42500835: "A history of global developmental delay was present in 96.1% and neonatal or infantile hypotonia in 62.7%. Progressive spasticity occurred in 72.5%, predominantly affecting the lower extremities and correlated with age"
- PMID:42500835: "Independent walking was achieved by 62.7% at a median age of 24 months, but only 31.4% retained independent ambulation at last evaluation."
- PMID:39009236: "Ninety-five percent of participants examined had some degree of optic nerve atrophy detected by clinical examination and/or optical coherence tomography (OCT). Almost 40% had strabismus."
- PMID:25265257: "Individuals with de novo mutations in KIF1A display a phenotype characterized by cognitive impairment and variable presence of cerebellar atrophy, spastic paraparesis, optic nerve atrophy, peripheral neuropathy, and epilepsy."
- PMID:31488895 (pure HSP): "In these patients, spastic paraplegia was slowly progressive and mostly pure, but with a highly variable disease onset (0-57 years)."

**Quality of life.**
- Mean VABS-3 Adaptive Behavior Composite is 60.6, a low level of adaptive functioning (Boyle).
- Loss of ambulation and progressive visual loss limit activities of daily living.
- No EQ-5D or SF-36 data were found.

## 4. Genetic and molecular information

**Gene and protein**
- Gene: *KIF1A* (hgnc:888; NCBI Gene 547; 2q37.3). Reference transcript in the main cohort study: NM_001244008.2.
- Protein: kinesin-3 family. Domains, from N- to C-terminus:
  - motor domain (about aa 1–361), containing the P-loop, switch I, switch II and K-loop;
  - neck linker;
  - CC1, the autoinhibitory coiled coil;
  - FHA domain;
  - CC2 and CC3;
  - the C-terminal PH domain, which binds cargo lipids.

**Variant spectrum**
- More than 110 variants are reported. Most are missense variants in the motor domain.
- Recurrent variants include p.Thr99Met, p.Glu253Lys, p.Arg254Trp/Gln, p.Arg307Gln, p.Arg316Trp, p.Ala255Val, p.Pro305Leu and p.Arg350Gly.
- ✅ PMID:33880452: "More than 30% of individuals with KAND have private variants".
- ✅ PMID:33880452: "the majority of KIF1A variants (64/115) were de novo".

**Variant types**
- Missense: predominant in all forms.
- Truncating or loss-of-function: in HSN2C and in dominant HSP. ✅ PMID:31488895: "unlike these allelic disorders, dominant spastic paraplegia was also caused by loss-of-function variants outside this domain in six families."
- Copy-number variants: one CNV encompassing KIF1A (PMID:34487232).

**Classification and population frequency.**
- Pathogenic variants are absent from gnomAD.
- The gene is highly constrained, so missense variants in the motor domain receive ACMG PM1 and PM2 support.
- Check ClinGen gene-disease validity with `just list-gene-validity`. Recording a validity tier requires the `CGGV:` record, and none is cached yet.

**Functional consequences: three molecular classes plus hyperactivation**
- ✅ PMID:33880452: "we describe three classes of protein dysfunction: reduced MT binding, reduced velocity and processivity, and increased non-motile rigor MT binding. The rigor phenotype is consistently associated with the most severe clinical phenotype, while reduced MT binding is associated with milder clinical phenotypes."
- ✅ PMID:35917346: "In our C. elegans models, both heterozygotes and homozygotes exhibited reduced axonal transport." and "We find that mutant KIF1A significantly impaired the motility of heterodimeric motors." These are **dominant-negative** effects.
- Budaitis et al. 2021, *eLife* (PMC7844421; PMID not yet confirmed): KAND motor-domain mutants relieve autoinhibition but "display decreased velocities, run lengths, and landing rates", reduce force generation, and behave in a dominant-negative way ([PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7844421/)).
- Chiba et al. 2019, *PNAS* (PMC6744892): some SPG30 variants (e.g. V8M, R350G, A255V) **hyperactivate** motility, with SVP accumulation at axon tips. "Hyperactivation of kinesin motor activity, rather than its loss of function, is a cause of motor neuron disease" ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6744892)).
- Haploinsufficiency is a mechanism in a subset of dominant HSP. ✅ PMID:31488895: "The identification of KIF1A loss-of-function variants suggests haploinsufficiency as a possible mechanism in autosomal dominant spastic…" (the sentence is truncated in this excerpt).

**Recommended `functional_impact_category` values:**
- `DOMINANT_NEGATIVE` for de novo motor-domain missense variants;
- `LOSS_OF_FUNCTION` for truncating variants (HSN2C, dominant HSP);
- `HYPERMORPHIC` for a subset of SPG30 variants (Chiba 2019).

**Genotype–severity correlation**
- ✅ PMID:33880452: "We found increased severity is strongly associated with variants occurring in protein regions involved with ATP and MT binding: the P loop, switch I, and switch II."
- ✅ PMID:42500835: "The p.Glu253Lys variant was associated with the most severe phenotype."
- Conflicting evidence: ✅ PMID:34487232 found that "location of mutation did not correlate with neurological and imaging presentations."

**Epigenetic and chromosomal findings.** No epigenetic signature has been reported. The only structural variant is a rare CNV at 2q37.3; 2q37 deletion syndrome includes *KIF1A* but is a separate entity.

## 5. Environmental information

No environmental, lifestyle, or infectious causes are known. This section is not applicable.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Germline *KIF1A* variant.** Usually a heterozygous de novo missense change in the motor domain; rarer forms are biallelic or truncating.
2. The variant alters ATP hydrolysis or microtubule binding in the motor domain (P-loop, switch I/II, K-loop/L12). This **leads to** one of four motor defects:
   - (a) reduced microtubule binding;
   - (b) reduced velocity and processivity, with reduced force;
   - (c) non-motile rigor binding;
   - (d) branch: loss of CC1 autoinhibition, causing hyperactive motility (some SPG30 alleles).
   - Sources: PMID:33880452, Budaitis 2021, Chiba 2019. The steps are demonstrated in vitro and in *C. elegans*.
3. The mutant subunit forms heterodimers with wild-type KIF1A. This **results in** dominant-negative suppression of total motor output. The step is demonstrated in vitro and in worms (PMID:35917346). In the truncating-allele branch, haploinsufficiency is **inferred** (PMID:31488895).
4. Anterograde axonal transport of SVPs (synaptophysin, synaptotagmin, RAB3) and dense-core vesicles (BDNF/TrkA) is impaired or, for hypermorphs, mislocalized. This **leads to** reduced cargo delivery to presynaptic sites, or cargo piling up at axon tips. Demonstrated in rodent neurons and worms (Guedes-Dias 2019, PMC6342647; Yonekawa 1998).
5. Synaptogenesis and synaptic vesicle release are impaired. This **results in** neurodevelopmental dysfunction (developmental delay/ID, autism, seizures, hypotonia). The link to seizures is **inferred**.
6. Neurons with the longest axons are the most vulnerable to chronic transport insufficiency, which **leads to** length-dependent axonal degeneration:
   - corticospinal tract → progressive spastic paraplegia;
   - optic nerve (retinal ganglion cells) → optic atrophy;
   - peripheral sensory and autonomic neurons → neuropathy and dysautonomia features;
   - cerebellar Purkinje and granule cells and olivary neurons → cerebellar atrophy and ataxia.
   - Supporting evidence: the Kif1a-knockout mouse shows neuronal death (Yonekawa 1998, PMID:9548721). The Kif1a^Lgdg mouse shows cerebellar axonal torpedoes. Autopsy findings are described next.
7. Neuropathology: two p.Thr99Met autopsies. ✅ PMID:33880452: "Microscopic examination revealed severe cerebellar atrophy most prominent in the superior cerebellar vermis, including a thin molecular layer, a depletion of Purkinje and internal granule cells, Bergmann gliosis, and white matter pallor. Rare axonal spheroids were observed."
8. These changes produce the clinical course: early developmental phenotype, then progressive motor, visual and cerebellar decline. ✅ PMID:33880452: "Spasticity was progressive … we largely did not see cognitive regression."

Two additional nodes:
- **Mitochondrial node (Vecchia 2022).** Muscle biopsy shows "oxidative metabolism alteratio[ns]" (✅ PMID:34487232; the snippet is truncated). This is probably secondary; the mechanism is uncertain.
- **TrkA/BDNF dense-core vesicle node.** Loss of KIF1A-dependent TrkA transport causes sensory neuron loss in mice (Tanaka et al. 2016, *Cell Rep*; PMID to confirm). This supports the HSN2C branch.

### Suggested ontology bindings (verify all)

| Category | Candidate terms |
|---|---|
| GO biological process | GO:0008089 anterograde axonal transport; GO:0048490 anterograde synaptic vesicle transport; GO:0047496 vesicle transport along microtubule; GO:0007416 synapse assembly; GO:0016079 synaptic vesicle exocytosis |
| GO molecular function | GO:0003777 microtubule motor activity; GO:0008017 microtubule binding; GO:0016887 ATP hydrolysis activity |
| GO cellular component | GO:0030424 axon; GO:0008021 synaptic vesicle; GO:0031045 dense core granule |
| Cell Ontology | CL:0000540 neuron; CL:0011113 spinal cord motor neuron / corticospinal (upper motor) neuron (check which label CL provides); CL:0000121 Purkinje cell; CL:0000740 retinal ganglion cell; CL:0000101 sensory neuron; CL:0001031 cerebellar granule cell |

**Molecular profiling.** No patient transcriptomic, proteomic or metabolomic datasets were found. iPSC-derived motor-neuron models are reported in KIF1A.ORG-funded projects but are largely unpublished. Run `just discover-datasets` before curating `datasets:`.

## 7. Anatomical structures affected

- **Primary site:** the nervous system, central and peripheral. Candidate UBERON terms (verify):
  - corticospinal tract (UBERON:0002707);
  - cerebellum, especially the vermis (UBERON:0002037 / UBERON:0004720);
  - optic nerve (UBERON:0000941);
  - inferior olivary complex (UBERON:0002127);
  - dentate nucleus (UBERON:0002132);
  - corpus callosum (UBERON:0002336);
  - peripheral nerve (UBERON:0001021).
- **Secondary involvement:**
  - gastrointestinal (GERD, dysmotility);
  - musculoskeletal (contractures, scoliosis, tendon-lengthening surgery in 15%);
  - endocrine (growth hormone deficiency);
  - genitourinary (rare).
- **Subcellular level:** axon; synaptic vesicle; presynaptic active zone; microtubules.
- **Laterality:** bilateral and symmetric (spasticity, optic atrophy).

## 8. Temporal development

- **Onset:** birth to 9 years in the severe cohort (median 6 months, mean 11 months; ✅ Boyle). Pure HSP can start anywhere from 0 to 57 years (✅ PMID:31488895).
- **Pattern:** a congenital or infantile developmental phenotype followed by slow neurodegeneration.
- **Progression:**
  - spasticity worsens with age;
  - ambulation is lost (62.7% → 31.4%);
  - optic atrophy progresses, and adults have worse acuity than children (20/119 vs 20/43; ✅ PMID:39009236);
  - cerebellar atrophy is progressive on serial MRI.
- **Course:** chronic and lifelong. Remission does not occur.
- **Critical period:** early childhood, before axonal loss. This is the presumed window for allele-specific or ASO therapy (inferred).
- **Suggested `progression:` phases:** infantile hypotonia and developmental delay → childhood spasticity and seizures → adolescent/adult loss of ambulation and vision.

## 9. Inheritance and population

- **Prevalence:** unknown. Hundreds to more than 1,000 diagnosed individuals are known worldwide through KIF1A.ORG.
  - Recommended record: `prevalence_class: NOT_YET_DOCUMENTED` or `RARE` with `measure_type: UNKNOWN`.
  - In the Dutch exome cohort, KIF1A explained 6–7% of mostly pure HSP. ✅ PMID:31488895: "KIF1A variants are a frequent cause of autosomal dominant spastic paraplegia in our cohort (6-7%)." This figure is a candidate for `case_fractions`, not population prevalence.
- **Inheritance:**
  - autosomal dominant: mostly de novo (64/115 confirmed); SPG30A can be inherited;
  - autosomal recessive: SPG30B, HSN2C.
- **Penetrance:** high for de novo motor-domain variants; reduced or variable penetrance in inherited dominant HSP families.
- **Expressivity:** highly variable, even for the same variant.
- **Other inheritance features:**
  - no anticipation;
  - germline mosaicism is possible;
  - founder alleles appear in consanguineous recessive families (Palestinian, Afghan).
- **Sex ratio:** about 1:1 (47 F / 53 M in Boyle).
- **Ancestry:** reported worldwide, with no enrichment.

## 10. Diagnostics

- **Genetic testing (definitive):**
  - exome or genome sequencing, or a multigene panel (HSP, epilepsy, NDD, ataxia, or neuropathy panels);
  - CNV analysis for rare deletions;
  - parental testing to establish de novo status.
  - GeneReviews: diagnosis rests on "a heterozygous pathogenic variant or, less commonly, biallelic pathogenic variants in KIF1A identified by molecular genetic testing."
- **Imaging:** MRI for cerebellar (vermian) atrophy, thin corpus callosum, and optic nerve thinning.
- **Ophthalmology:** OCT of the RNFL/GCL and visual evoked potentials (VEP). ✅ PMID:39009236: "VEPs showed findings consistent with optic neuropathy and visual dysfunction even in the absence of obvious structural changes on OCT."
- **Electrophysiology:**
  - EEG (absence seizures, generalized epileptiform activity);
  - nerve conduction/EMG (axonal sensorimotor neuropathy).
- **Muscle biopsy:** non-specific oxidative changes (PMID:34487232).
- **Laboratory biomarkers:** none validated. Neurofilament light chain has been proposed and is under study in KOALA (unpublished).
- **Clinical criteria:** none are standardized.
- **Differential diagnosis:**
  - other complicated HSPs (SPG11, SPG4/SPAST, SPG7);
  - Rett syndrome (MECP2, CDKL5, FOXG1);
  - PEHO syndrome;
  - congenital ataxias;
  - other HSAN genes (WNK1/HSN2, RETREG1/FAM134B);
  - cerebral palsy, the most common misdiagnosis;
  - other kinesinopathies (KIF5A, KIF1B, KIF1C).
- **Screening:** no newborn screening exists. Prenatal or preimplantation testing is available for known familial variants.

## 11. Outcome and prognosis

- **Survival:** KAND is described as "neurodegenerative and often lethal" (✅ PMID:39122967). Life-expectancy data are lacking; the oldest reported cohort members were in their 30s to 60s (dominant HSP).
- **Morbidity:**
  - wheelchair dependence by the 20s in severe forms;
  - progressive visual loss;
  - refractory epilepsy in some patients;
  - aspiration and feeding problems (10% need enteral nutrition).
- **Prognostic factors:**
  - variant location (P-loop/switch I/II = worse);
  - molecular class (rigor = worst);
  - earlier onset (associated with microcephaly);
  - p.Glu253Lys (most severe).
- **Recovery:** none. Cognition is generally stable and does not regress.

## 12. Treatment

No disease-modifying therapy is approved. Management is symptomatic and delivered by a multidisciplinary team.

| Intervention | Details | Candidate NCIT term (verify) | Modality |
|---|---|---|---|
| Antiseizure medication | Selected by seizure type; absence seizures are common | NCIT:C15986 Pharmacotherapy + `therapeutic_agent` | SMALL_MOLECULE |
| Spasticity drugs | Baclofen, tizanidine; botulinum toxin injection | NCIT:C15986 | SMALL_MOLECULE / biologic |
| Orthopedic surgery | Tendon lengthening (15%), scoliosis surgery | NCIT:C16186 Orthopedic Surgical Procedure | SURGERY |
| Physical, occupational, speech therapy | | NCIT:C15302 / NCIT:C121351 / NCIT:C159273 | BEHAVIORAL |
| Gastrostomy and nutritional support | GERD management | NCIT:C15433 Nutritional Support (not BEHAVIORAL; see CLAUDE.md) | — |
| Vision support, strabismus management | | NCIT:C15747 Supportive Care | — |
| Genetic counseling | | NCIT:C15240 Genetic Counseling | — |
| **Allele-specific ASO (n-of-1; experimental)** | p.Pro305Leu; intrathecal gapmer from n-Lorem | NCIT:C15986 + `oligonucleotide_details` (`RNASE_H_KNOCKDOWN`, target hgnc:888) | ANTISENSE_OLIGONUCLEOTIDE |

**ASO case (✅ PMID:39122967, Ziegler et al. 2024, *Nat Med*):**
- "treated with intrathecal injections of an allele-specific antisense oligonucleotide specifically designed to degrade the mRNA from the pathogenic allele."
- "the antisense oligonucleotide was safe and well tolerated over the 9-month treatment. Most outcome measures, including severity of the spells of behavioral arrest, number of falls and quality of life, improved."
- Adverse event: an epidural CSF collection after the first lumbar puncture, which resolved spontaneously.
- The design rationale is that silencing the dominant-negative allele preserves wild-type function. This depends on the patient tolerating 50% dosage, which haploinsufficient HSP families suggest may itself cause mild disease. That tension is worth recording in a `KNOWLEDGE_GAP` discussion.

**Other experimental programs:**
- further n-Lorem ASOs for other private variants;
- AAV gene-replacement preclinical work;
- the KOALA natural-history and endpoint study, which is pre-trial and currently moving from Columbia to Boston Children's ([KIF1A.ORG](https://www.kif1a.org/the-koala-study/)).

I found no registered interventional NCT trial. Search ClinicalTrials.gov directly before claiming that none exists.

## 13. Prevention

- **Primary prevention:** not possible for de novo cases.
- **Reproductive options:** genetic counseling; prenatal or preimplantation diagnosis for familial or recessive variants. Recurrence risk after a de novo case is low but above zero because of parental mosaicism.
- **Tertiary prevention:**
  - seizure control;
  - contracture and scoliosis surveillance;
  - regular ophthalmology (OCT/VEP);
  - aspiration prevention.

## 14. Other species and natural disease

- I found no naturally occurring KIF1A disease in OMIA. This should be confirmed in OMIA.
- KIF1A is highly conserved. The *C. elegans* ortholog is *unc-104* (the founding kinesin-3), and the *Drosophila* ortholog is *unc-104/imac*.

## 15. Model organisms

| Model | Phenotype and fidelity | Source |
|---|---|---|
| *Kif1a*−/− mouse | Neonatal lethal; SVP transport loss; sensory/motor deficits; neuronal death. Models complete loss of function only, which no human patient has. | PMID:9548721 (Yonekawa 1998, *J Cell Biol*) |
| *Kif1a*^Lgdg (C3H "legs at odd angles"-type) mouse | Progressive spasticity, hind-limb paralysis, cerebellar axonal torpedoes. Partially recapitulates human disease. | [search summary](https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2025.1704209/full); primary PMID needed |
| *Kif1a*+/− mouse | Sensory neuron/TrkA defects (Tanaka 2016) | PMID to confirm |
| *C. elegans* CRISPR KAND knock-ins (*unc-104* carrying human variants) | Reduced axonal transport in heterozygotes and homozygotes; a suppressor screen identified a rescue mutation. ✅ PMID:35917346 | MODEL_ORGANISM |
| *C. elegans* SPG-allele knock-ins | Hyperactive SVP transport (Chiba 2019) | MODEL_ORGANISM |
| Rat/mouse hippocampal neurons, in vitro TIRF motility | Reduced velocity, processivity and force; rigor binding | PMID:33880452; Budaitis 2021; IN_VITRO |
| Patient iPSC-derived neurons | In development (KIF1A.ORG-funded); unpublished | — |

**Limitations to record as `HUMAN_MODEL_MISMATCH`:**
- the knockout mouse is lethal while human disease is heterozygous and dominant-negative;
- no mouse knock-in of a common human allele (e.g. T99M, E253K) has been fully characterized in a peer-reviewed publication;
- the worm studies lack the optic nerve, cerebellum and corticospinal biology.

---

### Remaining work before using this in the YAML

1. Fetch these sources so their quotes can be verified against cached text: GeneReviews NBK621569 (and run `just check-genereviews`), Chiba 2019, Budaitis 2021, Guedes-Dias 2019, and Yonekawa 1998 (PMID:9548721).
2. Re-quote the truncated ✅ snippets from their complete sentences in the cache: PMID:21820098, PMID:31488895, and PMID:34487232.
3. Look up every HP/GO/CL/UBERON/NCIT/ORPHA CURIE above with `runoak` or the term cache. I wrote them from memory.
4. Check ClinGen for KIF1A–NESCAV/SPG30 `CGGV:` assertions before recording any gene-disease validity tier.

**Sources:**
- [GeneReviews NBK621569](https://www.ncbi.nlm.nih.gov/books/NBK621569/)
- [KAND overview (PMC9962247)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9962247/)
- [Chiba et al. 2019, PNAS (PMC6744892)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6744892)
- [Budaitis et al. 2021, eLife (PMC7844421)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7844421/)
- [Guedes-Dias et al. 2019 (PMC6342647)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6342647)
- [Yonekawa et al. 1998, J Cell Biol](https://rupress.org/jcb/article/141/2/431/950/Defect-in-Synaptic-Vesicle-Precursor-Transport-and)
- [OMIM SPG30B 620607 (mirror)](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/620607)
- [OMIM HSN2C 614213 (mirror)](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/commit/a3492137cada35c1427e5783c176e4344e6cbb56/www.ncbi.nlm.nih.gov/omim/614213)
- [MONDO:0700055 (SAIL concept library)](https://conceptlibrary.saildatabank.com/api/v1/ontology/node/MONDO:0700055/)
- [MalaCards](https://www.malacards.org/card/kif1a_associated_neurological_disorder)
- [Frontiers in Medicine 2025](https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2025.1704209/full)
- [KOALA study (KIF1A.ORG)](https://www.kif1a.org/the-koala-study/)
- [n-Lorem press release](https://www.nlorem.org/positive-clinical-observations-from-n-lorem-treated-kif1a-nano-rare-patient-published-in-nature-medicine/)
- [Ziegler et al. 2024, Nat Med (PubMed 39122967)](https://pubmed.ncbi.nlm.nih.gov/39122967/)
- [Genomics England PanelApp: KIF1A](https://panelapp.genomicsengland.co.uk/panels/568/gene/KIF1A)
- Local `references_cache/` files: PMID 21487076, 21820098, 25265257, 31488895, 32737135, 33880452, 34487232, 35917346, 39009236, 39122967, 42500835.

Two connector notes:
- The claude.ai Google Drive connector needs authorization in claude.ai's connector settings before it can be used.
- The GeneReviews page could not be fetched here because of a reCAPTCHA.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 3 |
| Quoted claims found in source | 3 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 17 |
| On topic | 13 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 77 |
| Resolved | 76 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 8 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0700055` (7 mentions) - the report calls it "MONDO", "SAIL concept library"; MONDO calls it **KIF1A related neurological disorder**
- `NCIT:C15986` (3 mentions) - the report calls it "Baclofen, tizanidine; botulinum toxin injection"; NCIT calls it **Pharmacotherapy**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0000941` (1 mention) - the report calls it "optic nerve"; UBERON calls it **cranial nerve II**, and lists "optic nerve" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0700055` - called "MONDO", "SAIL concept library"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.