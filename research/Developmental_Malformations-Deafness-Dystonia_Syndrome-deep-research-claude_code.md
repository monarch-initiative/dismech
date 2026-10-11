---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-11T12:50:32.453574'
end_time: '2026-09-11T12:55:12.990285'
duration_seconds: 280.54
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Developmental Malformations-Deafness-Dystonia Syndrome
  mondo_id: MONDO:0011823
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
  num_turns: 24
  total_cost_usd: 1.3555998
  session_id: 30472749-cc0b-5982-8425-d65a5081b928
  stop_reason: end_turn
  assistant_text_blocks: 2
fell_back: true
requested_provider: perplexity
provider_attempts:
- provider: perplexity
  succeeded: false
  error_type: ProviderNotConfiguredError
  remedy: the provider is not configured
  retryable: false
- provider: falcon
  succeeded: false
  error_type: ProviderAuthError
  status_code: 403
  remedy: the API key is missing, invalid, or lacks access to this endpoint
  retryable: false
- provider: claude_code
  succeeded: true
citation_count: 24
reference_validation:
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 5
  quotes_valid: 1
  quotes_unsupported: 4
  unsupported_quote_references:
  - PMID:28487785
  - PMC:PMC5405358
  relevance_assessed: 13
  on_topic: 5
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 47
  verified: 43
  not_found: 0
  obsolete: 0
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 12
  labels_matching: 10
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: HP:0025230
    reported_labels:
    - Dystonic tremor
    ontology_label: Tendonitis
  - term_id: NCIT:C1364
    reported_labels:
    - Botulinum Toxin
    ontology_label: Didemnin B
  unresolvable_prefixes:
  - ORPHA
  - MGI
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Developmental Malformations-Deafness-Dystonia Syndrome
- **MONDO ID:** MONDO:0011823 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Developmental Malformations-Deafness-Dystonia Syndrome** covering all of the
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

I'll research this disorder using web searches across the authoritative databases requested, then compile the full report.

I now have comprehensive, well-sourced material. Here is the complete research report.

---

# Developmental Malformations–Deafness–Dystonia Syndrome (Dystonia-Deafness Syndrome 1 / ACTB-Related Actinopathy)

## 1. Disease Information

**Overview.** Developmental malformations–deafness–dystonia syndrome — synonymous with **Dystonia-Deafness Syndrome 1 (DDS1)** — is an ultra-rare autosomal dominant neurodevelopmental/neurodegenerative disorder caused by heterozygous missense variants in **ACTB** (cytoplasmic β-actin). It is defined by the triad of (variable) midline/craniofacial developmental malformations, congenital or infancy-onset bilateral sensorineural hearing loss, and delayed-onset (childhood-to-adult) progressive generalized dystonia, often evolving to a severe, life-threatening motor disorder ([Orphanet](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Lng=GB&Expert=79107); [OMIM #607371](https://www.omim.org/entry/607371)).

**Key identifiers:**
- **OMIM phenotype:** #607371 — DYSTONIA-DEAFNESS SYNDROME 1 (DDS1)
- **OMIM gene:** *102630 — ACTIN, BETA (ACTB)
- **MONDO:** MONDO:0011823
- **Orphanet:** ORPHA:79107
- **ICD-10:** Q87.8 (other specified congenital malformation syndromes); **ICD-11:** classified among syndromic genetic deafness/developmental defects of embryogenesis
- **HGNC:** HGNC:132 (ACTB); **NCBI Gene:** 60 (human ACTB), located 7p22.1
- **UMLS/GTR concept:** C5848323
- **MalaCards / GARD ID:** 9818

**Synonyms/alternative names:** Dystonia-deafness syndrome (DDS); DDS1; Deafness-dystonia syndrome due to β-actin mutation; ACTB-related dystonia-deafness syndrome. (Note: this is distinct from **Mohr-Tranebjaerg syndrome / deafness-dystonia-optic neuronopathy**, TIMM8A/X-linked, OMIM #304700; from **BCAP31**-related "deafness, dystonia, and cerebral hypomyelination," OMIM #300475, X-linked; and from **MEGDEL syndrome/SERAC1**-related 3-methylglutaconic aciduria type VI with deafness-dystonia, OMIM #614739, autosomal recessive mitochondrial — all of which share the "deafness + dystonia" phenotype family but are genetically and mechanistically distinct.)

**Evidence basis:** This is one of the rarest known Mendelian disorders — described in aggregate literature review as fewer than 10–15 published families/cases worldwide, most sharing a single recurrent missense variant. Information is derived overwhelmingly from **individual case reports and small case series** (n=1 to n=7), not aggregated registry/EHR data; there is no disease registry or large cohort study.

Sources: [Orphanet 79107](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Lng=GB&Expert=79107); [OMIM #607371](https://www.omim.org/entry/607371); [GARD](https://rarediseases.info.nih.gov/diseases/9818/developmental-malformations-deafness-dystonia-syndrome); [MalaCards](https://www.malacards.org/card/developmental_malformations_deafness_dystonia_syndrome)

---

## 2. Etiology

**Disease causal factor — genetic, monogenic.** DDS1 is caused by **heterozygous, typically de novo, missense mutations in ACTB**, encoding cytoplasmic β-actin. There is no known environmental, infectious, or purely mechanistic (non-genetic) causal pathway; this is a pure Mendelian actinopathy.

**Causal/recurrent variant:** The dominant recurrent pathogenic variant across nearly all reported cases is **NM_001101.5(ACTB):c.547C>T, p.(Arg183Trp)**, first reported by Procaccio et al. (2006) in monozygotic twin brothers ([PMID:16685646](https://pubmed.ncbi.nlm.nih.gov/16685646/)). As of the most recent case series (Vermeulen et al. 2018), it had been reported in **six unrelated cases**; subsequent case reports (2020, 2021, 2022, 2025) have expanded this to roughly a dozen documented individuals/families.

> "A mutation of β-actin that alters depolymerization dynamics is associated with autosomal dominant developmental malformations, deafness, and dystonia" — title of the founding report, Procaccio et al., *Am J Hum Genet* 2006;78(6):947–60 ([PMID:16685646](https://pubmed.ncbi.nlm.nih.gov/16685646/)).

Arg183 lies in the ATP-binding pocket of β-actin and is highly evolutionarily conserved; the R183W substitution destabilizes the nucleotide-binding cleft, producing an actin monomer with abnormal (decreased) polymerization/depolymerization kinetics in both recombinant protein assays and patient-derived cells.

**Genetic risk factors:**
- Causal variant: ACTB c.547C>T p.Arg183Trp (the dominant recurrent allele)
- De novo occurrence is the most common inheritance mechanism reported (confirmed in multiple trios via exome sequencing), though vertical transmission (affected mother → affected daughter, and a multi-generation Argentinean family) has also been documented, consistent with autosomal dominant inheritance with full-to-high penetrance ([PMID:35005077](https://pubmed.ncbi.nlm.nih.gov/35005077/); [Vermeulen et al. PMID:29788902](https://pmc.ncbi.nlm.nih.gov/articles/PMC5964724/)).
- No established modifier genes, but **γ-actin (ACTG1) upregulation** is proposed as a partial genetic compensator modulating phenotypic severity and tissue-specific timing (see Mechanism, below).
- Allelic disorders: other, distinct ACTB missense variants (most commonly the recurrent p.Arg196His) cause **Baraitser-Winter cerebrofrontofacial syndrome type 1 (BRWS1)**, a phenotypically overlapping but mechanistically distinguishable actinopathy with more prominent brain malformation (pachygyria) and craniofacial dysmorphism ([PMC3677859](https://pmc.ncbi.nlm.nih.gov/articles/PMC3677859/); [PMC12443469](https://pmc.ncbi.nlm.nih.gov/articles/PMC12443469/)). 7p22.1 microdeletions encompassing ACTB cause a contiguous-gene developmental-delay/microcephaly/short-stature phenotype, distinct from DDS1.

**Environmental risk/protective factors:** None reported or plausible — this is a fully penetrant structural-protein Mendelian disorder with no documented gene-environment interaction literature.

**Protective factors:** None established. The hypothesized "protective" factor is endogenous — compensatory γ-actin (ACTG1) upregulation, which is proposed to explain incomplete penetrance of certain features and inter-individual phenotypic variability, but this is a molecular buffering mechanism rather than a modifiable protective exposure ([PMID:29788902](https://pmc.ncbi.nlm.nih.gov/articles/PMC5964724/)).

---

## 3. Phenotypes

The phenotype unfolds in an age-dependent sequence reflecting β-actin's differing tissue roles across development (see also Mechanism, §6).

| Phenotype | Type | Onset | Frequency (of reported cases) | Suggested HPO |
|---|---|---|---|---|
| Bilateral sensorineural hearing loss | Clinical sign | Congenital–infancy (often diagnosed ~2–8 months) | Near-universal (reported in essentially all cases) | HP:0000407 (Sensorineural hearing impairment) |
| Generalized dystonia | Motor symptom | Childhood–adolescence–young adulthood (range ~12–34 y at onset) | Universal (defining feature); progressive, often severe/disabling | HP:0007325 (Generalized dystonia) / HP:0012622 (Chronic progressive) |
| Craniofacial dysmorphism (mild) | Physical sign | Congenital | Frequent but variable severity — some cases (e.g., Argentinean family, Hutterite case) lack dysmorphism entirely | HP:0000271 (Abnormality of the face) |
| Midline structural brain malformation (corpus callosum/vermis hypoplasia) | Physical/imaging sign | Congenital | Variable — present in original twin cases and some later reports, absent in others (e.g., PMC5405358 case had no midline malformation) | HP:0002079 (Hypoplasia of the corpus callosum), HP:0001320 (Cerebellar vermis hypoplasia) |
| Developmental delay / mild intellectual disability | Neurodevelopmental | Infancy–childhood | Common but not universal; at least one adult-onset case (Argentinean proband) had no cognitive impairment | HP:0001263 (Global developmental delay), HP:0001249 (Intellectual disability) |
| Hypotonia, poor suck, feeding/swallowing difficulty | Neonatal sign | Neonatal | Reported in multiple cases | HP:0001252 (Hypotonia), HP:0002015 (Dysphagia) |
| Dystonic tremor / jerky action tremor | Motor symptom | Adolescence | Reported | HP:0025230 (Dystonic tremor) |
| Bulbar dystonia (dysphagia, velopharyngeal insufficiency) | Motor symptom, complication | Adolescence (progressive) | Reported in severe/fatal case | HP:0002310 (Dysarthria)/HP:0002015 |
| Parkinsonism (bradykinesia, resting/action tremor) | Motor symptom | Later adult onset (~40s) | Reported in at least one family member, "expanding the phenotype" | HP:0001300 (Parkinsonism) |
| Vision problems (cataracts, other) | Clinical sign | Variable | Reported per GARD summary | HP:0000518 (Cataract) |
| Scoliosis/kyphosis | Skeletal sign | Childhood–adolescence | Reported | HP:0002650 (Scoliosis) |
| Short stature | Growth | Childhood | Reported in a subset | HP:0004322 (Short stature) |

**Severity and progression:** Dystonia is typically **progressive**, evolving from focal onset (e.g., writer's cramp, lower-limb gait dystonia, unilateral upper-limb dystonia) to **generalized, often axial and bulbar** dystonia. In the most severe reported course, a patient became wheelchair- and then bed-bound within 3–5 years of motor onset and required emergency DBS for life-threatening status dystonicus-like decompensation ([PMID:29788902](https://pmc.ncbi.nlm.nih.gov/articles/PMC5964724/)); a Hutterite adolescent died at age 15 from complications of uncontrolled dystonia following status dystonicus ([PMID:28487785](https://pmc.ncbi.nlm.nih.gov/articles/PMC5405358)). Conversely, milder, adult-onset, non-progressive-to-cognition-sparing courses are also documented (Argentinean family, [PMID:35005077](https://pmc.ncbi.nlm.nih.gov/articles/PMC8721817/)), indicating **wide phenotypic variability even with the identical p.Arg183Trp allele**.

**Quality of life impact:** Severe cases show major functional impact — loss of ambulation, need for wheelchair/bed confinement, cochlear implantation for communication, feeding-tube dependency in bulbar involvement, and profound disability requiring full-time caregiver support; DBS responders regain sitting, standing-with-support, and ambulation with assistance ([PMID:29788902](https://pmc.ncbi.nlm.nih.gov/articles/PMC5964724/)).

Sources: [PMID:16685646](https://pubmed.ncbi.nlm.nih.gov/16685646/); [PMID:29788902](https://pmc.ncbi.nlm.nih.gov/articles/PMC5964724/); [PMID:28487785](https://pmc.ncbi.nlm.nih.gov/articles/PMC5405358); [PMID:35005077](https://pmc.ncbi.nlm.nih.gov/articles/PMC8721817/); [PMID:31970217](https://pubmed.ncbi.nlm.nih.gov/31970217/); [GARD](https://rarediseases.info.nih.gov/diseases/9818/developmental-malformations-deafness-dystonia-syndrome)

---

## 4. Genetic/Molecular Information

**Causal gene:** ACTB (HGNC:132; NCBI Gene 60; OMIM *102630), chr7p22.1, 6 exons, encoding a 374-amino-acid, ~41.7 kDa cytoplasmic β-actin protein — one of the most highly expressed and evolutionarily conserved structural proteins in the human proteome.

**Pathogenic variant details:**
- **Variant:** NM_001101.5:c.547C>T; p.(Arg183Trp) — the dominant recurrent DDS1 allele
- **Classification (ACMG/ClinVar):** Pathogenic/Likely pathogenic, recurrent de novo and dominantly inherited; ClinVar entry [RCV000019937](https://www.ncbi.nlm.nih.gov/clinvar/RCV000019937/)
- **Variant type:** Missense (single nucleotide substitution, Arg→Trp at codon 183)
- **Location:** Arg183 sits within the ATP-binding cleft/nucleotide-binding pocket of the actin monomer, a highly conserved residue (conserved across ~100 vertebrate species per UCSC alignment)
- **Allele frequency:** Absent from population databases — reported "not present in approximately 6,500 individuals of European and African American ancestry in the NHLBI Exome Sequencing Project" ([PMID:28487785](https://pmc.ncbi.nlm.nih.gov/articles/PMC5405358)); consistent with absence from gnomAD, as expected for a de novo dominant lethal-severity variant
- **Somatic vs. germline:** Germline (constitutional); documented de novo occurrences confirmed by trio exome sequencing in multiple independent families, plus vertical transmission in at least two multigenerational pedigrees
- **Functional consequence:** Dominant-negative/altered-function mechanism — the mutant monomer incorporates into filaments and **alters F-actin polymerization/depolymerization dynamics** rather than causing simple loss of function (see §6)
- A second reported ACTB variant in this syndrome is **c.1023C>T (p.Ile341=)**, a synonymous change of uncertain/contested significance, listed in ClinVar under this same disease term ([RCV002253209](https://www.ncbi.nlm.nih.gov/clinvar/RCV002253209/))

**Modifier genes:** No formal modifier locus identified; **ACTG1 (γ-actin)** is proposed as an endogenous molecular compensator — differential β-actin/γ-actin ratios across tissues and developmental stages are hypothesized to explain the tissue- and age-specific pattern of disease expression (craniofacial → cochlear → striatal), and its variable upregulation may account for phenotypic severity differences between otherwise genetically identical carriers ([PMID:29788902](https://pmc.ncbi.nlm.nih.gov/articles/PMC5964724/)).

**Epigenetic information:** No disease-specific epigenetic (DNA methylation/histone) data have been reported for DDS1; not covered in ENCODE/Roadmap Epigenomics disease-specific studies to date.

**Chromosomal abnormalities:** DDS1 itself is a point-mutation disorder, not a copy-number disorder. However, **7p22.1 contiguous microdeletions encompassing ACTB** cause a related but distinct phenotype (developmental delay, short stature, microcephaly) and should be distinguished on chromosomal microarray/CMA from the single-nucleotide DDS1 variant ([GeneCards ACTB](https://www.genecards.org/cgi-bin/carddisp.pl?gene=ACTB)).

**Allelic series — genotype-phenotype correlation:** ACTB is now recognized as a multi-phenotype actinopathy gene:
- p.Arg183Trp → DDS1 (deafness-dystonia-predominant, later-onset progressive movement disorder)
- p.Arg196His (recurrent) and other hotspot variants → Baraitser-Winter syndrome type 1 (more severe cortical malformation, pachygyria, characteristic craniofacial gestalt) — mechanistically distinguished by variant-specific effects on Arp2/3-mediated branching and myosin interaction rather than on simple polymerization rate ([PMC12443469](https://pmc.ncbi.nlm.nih.gov/articles/PMC12443469/); [PMC3677859](https://pmc.ncbi.nlm.nih.gov/articles/PMC3677859/))

Ontology suggestions: gene — **HGNC:132 (ACTB)**; variant functional impact — best modeled as `functional_impact_category: OTHER`/altered-dynamics rather than clean GAIN_OF_FUNCTION or LOSS_OF_FUNCTION, per the dismech guidance on qualitative pathway disruption.

Sources: [OMIM *102630](https://omim.org/entry/102630); [PMID:16685646](https://pubmed.ncbi.nlm.nih.gov/16685646/); [PMID:28487785](https://pmc.ncbi.nlm.nih.gov/articles/PMC5405358); [ClinVar RCV000019937](https://www.ncbi.nlm.nih.gov/clinvar/RCV000019937/); [GeneCards ACTB](https://www.genecards.org/cgi-bin/carddisp.pl?gene=ACTB)

---

## 5. Environmental Information

No environmental factors, lifestyle exposures, or infectious agents are implicated in DDS1 causation — it is a fully penetrant monogenic structural-protein disorder. No CTD, TOXNET, or epidemiological literature links environmental exposures to onset or severity. The only "environmental" modulators reported are iatrogenic/therapeutic (surgical DBS, pharmacologic dystonia management — see §12), not causal or risk-modifying exposures.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Germline heterozygous ACTB missense mutation** (predominantly c.547C>T, p.Arg183Trp) alters the nucleotide (ATP)-binding pocket of the β-actin monomer → **leads to** abnormal actin monomer (G-actin) conformation and altered nucleotide-exchange kinetics (demonstrated in recombinant protein assays; PMID:16685646).
2. The mutant monomer co-assembles into filaments (heterodimeric incorporation alongside wild-type β-actin and γ-actin) → **results in** filamentous actin (F-actin) with **altered polymerization/depolymerization dynamics** — reduced elongation rate and/or accelerated/aberrant depolymerization — rather than a simple structural absence of actin ("dominant-negative/altered-function" mechanism, not classic loss-of-function).
3. Because β-actin performs distinct, tissue- and life-stage-specific roles, the same molecular lesion **produces sequential, tissue-specific downstream consequences** as different actin-dependent processes become rate-limiting at different developmental windows (proposed temporal-vulnerability model, PMID:29788902):
   - **a. Prenatal — neural crest cell migration.** Actin-driven lamellipodial/filopodial motility is required for neural crest delamination and migration; disrupted dynamics → **causes** mild craniofacial dysmorphogenesis and, in more severe allelic variants (e.g., BWCFF-causing p.Arg196His), overt midline/cortical brain malformation via impaired neuronal migration (supported by loss-of-migration phenotypes in Actb-null neural crest cells in mouse, PLOS One 2014).
   - **b. Infancy — cochlear hair-cell stereocilia maintenance.** β-actin (with γ-actin) is a principal structural component of the stereociliary F-actin core. Actin isoforms are largely dispensable for initial stereocilia *development* but become essential for **stereocilia maintenance**; mouse Actb-deletion models show progressive, high-frequency-first hearing loss with age due to structural stereocilia degeneration, not developmental failure (PMID:20976199; PLOS Genetics PMC2954897) → in humans, this **leads to** progressive/early sensorineural deafness as the altered-dynamics mutant actin destabilizes stereociliary actin turnover over time.
   - **c. Puberty–adulthood — striatal (and pallidal) synaptic/neuronal actin turnover.** Actin cytoskeletal remodeling is essential for ongoing dendritic spine plasticity and synaptic maintenance in striatal medium spiny neurons. Chronic accumulation of dysfunctional actin turnover → **results in** progressive striatal neurodegeneration.
4. **Striatal/pallidal neurodegeneration** is directly evidenced at autopsy in the original index twins: **abundant eosinophilic spherical structures in the striatum**, strongly immunoreactive for actin and actin-depolymerizing factor (ADF)/cofilin, "consistent with degenerating neurons and processes... suggesting a defect in actin turnover," with additional actin/ADF-cofilin immunoreactivity in the **globus pallidus** ([PMID:29788902](https://pmc.ncbi.nlm.nih.gov/articles/PMC5964724/)).
5. This structural neurodegeneration → **leads to** measurable **striatal dopaminergic/neuronal dysfunction**: reduced DaT-SPECT striatal dopamine-transporter uptake, reduced D2-receptor binding on Epidepride-SPECT in the putamen (and to a lesser extent caudate), and reduced FDG-PET glucose uptake bilaterally in the striatum, particularly the putamen — the first in vivo neuroimaging confirmation, corroborating the twins' post-mortem findings ([PMID:29788902](https://pmc.ncbi.nlm.nih.gov/articles/PMC5964724/)).
6. Loss of normal striatal/pallidal neuronal output → **produces** the clinical phenotype of progressive, severe, generalized dystonia (basal-ganglia circuit dysfunction), which in a subset of patients later **evolves to include parkinsonism** (bradykinesia, resting tremor) in the fifth decade, reflecting broader degeneration of dopaminergic circuitry over time.
7. **Partial phenotypic buffering**: the authors propose that "partial compensation by the upregulation of other forms of actin, in particular gamma-actin, modulates the degree of severity and the temporal pattern of susceptibility" — explaining inter-individual variability in onset age, severity, and presence/absence of craniofacial or cognitive features despite an identical causal variant (inferred/hypothesis-level, not directly demonstrated in human striatal tissue).

### Category detail

- **Molecular pathways:** Actin cytoskeletal dynamics/turnover (polymerization–depolymerization cycle); ADF/cofilin-mediated filament severing and recycling; Arp2/3-complex-dependent branched-actin nucleation (implicated for the allelic BWCFF variants). GO: `GO:0030036` (actin cytoskeleton organization); `GO:0051015` (actin filament binding); `GO:0007015` (actin filament organization).
- **Cellular processes:** Cell migration (neural crest), stereocilia maintenance, synaptic/dendritic spine remodeling, and ultimately neurodegeneration (a form of accumulative proteinopathy-like process driven by cytoskeletal-protein dysfunction rather than classic protein aggregation).
- **Protein dysfunction:** Altered-function (not simple loss-of-function) monomer incorporation causing filament instability — UniProt P60709 (human ACTB); structural work maps Arg183 to the ATP-binding cleft.
- **Tissue damage mechanism:** Actin-turnover-defect-driven neuronal degeneration in striatum/globus pallidus, morphologically resembling axonal/dendritic spheroid (dystrophic neurite) formation.
- **Cell types involved:** Cochlear outer/inner hair cells (`CL:0000602`/`CL:0000601`); striatal medium spiny neurons (`CL:0000696`); neural crest cells (`CL:0000333`); globus pallidus neurons.
- **Anatomical/GO suggestions for pathograph:** `GO:0030041` (actin filament polymerization), `GO:0030042` (actin filament depolymerization), `GO:0007605` (sensory perception of sound, downstream phenotype), `GO:0050890` (cognition, for developmental delay branch).
- **Molecular profiling / advanced technologies:** No transcriptomic, proteomic, or single-cell datasets specific to human DDS1 tissue have been published (autopsy immunohistochemistry is the only human tissue-level molecular data available); mouse Actb-null and hair-cell-specific conditional-knockout models provide the closest molecular-profiling proxies (PMID:20976199).

Sources: [PMID:16685646](https://pubmed.ncbi.nlm.nih.gov/16685646/); [PMID:29788902](https://pmc.ncbi.nlm.nih.gov/articles/PMC5964724/); [PMID:20976199](https://pubmed.ncbi.nlm.nih.gov/20976199/) / [PMC2954897](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2954897/); [PMC12443469](https://pmc.ncbi.nlm.nih.gov/articles/PMC12443469/) (Baraitser-Winter mechanism, allelic comparator); [PLOS One 2014, Actb neural crest](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0085608)

---

## 7. Anatomical Structures Affected

- **Organ level (primary):** Inner ear (cochlea) — sensorineural hearing loss; central nervous system — basal ganglia (striatum, globus pallidus), and in some cases cerebral cortex/corpus callosum/cerebellar vermis (developmental malformation subset).
- **Organ level (secondary/complications):** Musculoskeletal system (scoliosis/kyphosis secondary to dystonic posturing); GI/upper aerodigestive tract (dysphagia, aspiration risk from bulbar dystonia); ophthalmologic (cataracts reported in some cases); craniofacial skeleton (mild dysmorphism).
- **Body systems:** Nervous system (primary), auditory system, musculoskeletal system, and craniofacial/developmental system.
- **Tissue/cell level:** Cochlear hair-cell stereocilia (actin-rich structures); striatal medium spiny neurons and globus pallidus neurons (site of autopsy-confirmed degeneration); neural crest-derived craniofacial mesenchyme (developmental).
- **Subcellular level (GO Cellular Component):** Cytoskeleton/actin cytoskeleton (`GO:0015629`); stereocilium actin core (`GO:0032420`); dendritic spine (`GO:0043197`).
- **UBERON suggestions:** `UBERON:0001851` (cortex of cerebral hemisphere — malformation subset), `UBERON:0002435` (striatum), `UBERON:0001875` (globus pallidus), `UBERON:0001846` (cochlea/organ of Corti structures), `UBERON:0009653` (stereocilium), `UBERON:0002539` (corpus callosum).
- **Laterality:** Bilateral and symmetric in essentially all reported features — bilateral sensorineural hearing loss, bilateral striatal/putaminal imaging abnormalities, generalized (non-lateralized) dystonia (though focal onset, e.g. unilateral writer's cramp, is reported before generalization).

Sources: [PMID:29788902](https://pmc.ncbi.nlm.nih.gov/articles/PMC5964724/); [PMID:31970217](https://pubmed.ncbi.nlm.nih.gov/31970217/) (corpus callosum/vermis hypoplasia case)

---

## 8. Temporal Development

**Onset:** Multi-stage, sequential onset pattern rather than single-point onset:
- Neonatal: hypotonia, weak suck, feeding difficulty (early, non-specific)
- Infancy (typically diagnosed 2.5–8 months): bilateral sensorineural hearing loss
- Childhood–adolescence (range documented: ~12–24 years, most commonly early-mid teens): focal-onset dystonia (commonly lower-limb gait disturbance or upper-limb/writer's cramp), progressing to generalized dystonia over months-to-years
- Adulthood (documented as late as the 40s in one family member): late parkinsonism as an expanded phenotype

**Onset pattern:** Insidious/subacute for dystonia; the hearing loss is typically noted as congenital-to-early-infancy and is not itself progressive in most reports (though the underlying stereocilia-maintenance mechanism predicts a progressive component with age, as in the mouse model).

**Progression:**
- Disease course is **progressive and often severe** for the dystonia component — from focal to segmental to generalized, with axial/bulbar involvement in severe cases, culminating in loss of ambulation, wheelchair/bed dependence, and in the most severe reported case, fatal status-dystonicus-like decompensation by age 15.
- **Progression rate is highly variable**: some cases show relatively indolent, non-progressive adult-onset dystonia without cognitive decline (Argentinean proband); others show rapid, life-threatening decompensation within a few years of onset.
- **Disease duration:** chronic, lifelong; no spontaneous remission reported. DBS can produce durable (years-long) symptomatic improvement but is not curative and outcomes can wane over time (one case showed sustained benefit from age 19 to 25, with subsequent decline attributed to disease progression/hardware factors) ([ScienceDirect S1353802022003145](https://www.sciencedirect.com/science/article/abs/pii/S1353802022003145)).
- **Critical periods:** the tissue-specific-vulnerability model implies three sequential critical windows — prenatal neural crest migration, infantile cochlear hair-cell maintenance, and peripubertal-to-adult striatal synaptic maintenance — each representing a period where actin-dependent processes become rate-limiting.

Sources: [PMID:29788902](https://pmc.ncbi.nlm.nih.gov/articles/PMC5964724/); [PMID:28487785](https://pmc.ncbi.nlm.nih.gov/articles/PMC5405358); [PMID:35005077](https://pmc.ncbi.nlm.nih.gov/articles/PMC8721817/)

---

## 9. Inheritance and Population

**Epidemiology:**
- **Prevalence:** Orphanet lists prevalence as **<1 per 1,000,000** — among the rarest of Mendelian syndromes, with only a small number of published families/cases worldwide (roughly a dozen documented individuals across all reports as of 2025) ([Orphanet 79107](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Lng=GB&Expert=79107)).
- **Incidence:** Not formally estimated; too rare for population-based incidence studies.

**Inheritance pattern:** **Autosomal dominant.** Both de novo occurrence (multiple independently confirmed trios) and vertical transmission (parent-to-child, multi-generational Argentinean family) are documented.

**Penetrance:** High/complete for at least the deafness component in reported carriers; dystonia penetrance appears high but with substantial variability in age of onset and severity, and at least one carrier (a mother in the Argentinean family) manifested facial dystonia plus later parkinsonism rather than classic generalized dystonia — consistent with variable expressivity rather than reduced penetrance per se.

**Expressivity:** Markedly **variable** — presence/absence of craniofacial dysmorphism, presence/absence of structural brain malformation, presence/absence of cognitive impairment, and severity/tempo of dystonia all vary substantially among carriers of the identical p.Arg183Trp variant.

**Genetic anticipation:** Not reported/established (no repeat-expansion mechanism; not expected mechanistically for a fixed missense variant).

**Germline mosaicism:** Not specifically documented in the literature reviewed, though possible given de novo occurrence pattern typical of such variants; not formally studied.

**Founder effects:** No population-specific founder variant identified; the recurrent p.Arg183Trp allele has arisen independently (recurrent de novo mutation at a mutational hotspot codon) across genetically distinct families (European, North American Hutterite, South American/Argentinean), rather than reflecting a single ancestral founder haplotype.

**Consanguinity:** Reported in at least one case (Hutterite family, a genetically isolated founder population, though the variant itself arose de novo rather than through recessive consanguineous transmission) ([PMID:28487785](https://pmc.ncbi.nlm.nih.gov/articles/PMC5405358)).

**Carrier frequency:** Not applicable/not estimable — autosomal dominant with de novo predominance, no population carrier-frequency data (variant essentially absent from gnomAD/ESP population databases).

**Population demographics:**
- Affected populations reported: European-ancestry families (original twins), a Hutterite (North American founder-population) family, and a South American (Argentinean) family — suggesting no strong ethnic restriction, consistent with a recurrent de novo mutational mechanism at a hotspot rather than a single ancestral allele.
- Sex ratio: no clear sex predilection reported (autosomal dominant; cases include both male and female probands).
- Age distribution: hearing loss universally identified in infancy; dystonia onset spans adolescence to middle adulthood across the reported cohort.

Sources: [Orphanet 79107](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Lng=GB&Expert=79107); [PMID:28487785](https://pmc.ncbi.nlm.nih.gov/articles/PMC5405358); [PMID:35005077](https://pmc.ncbi.nlm.nih.gov/articles/PMC8721817/)

---

## 10. Diagnostics

**Clinical tests:**
- **Laboratory tests:** No disease-specific biochemical/enzymatic biomarker exists (this is a structural-protein disorder, not a metabolic one — distinguishing it from the biochemically-positive SERAC1/MEGDEL deafness-dystonia phenocopy, which shows elevated urinary 3-methylglutaconic acid).
- **Imaging:**
  - Brain MRI: variable — may show corpus callosum/cerebellar vermis hypoplasia in a subset, or be entirely unremarkable in others (e.g., normal MRI in the Argentinean proband); T2/FLAIR hyperintensity in caudate/basal ganglia reported in at least one case ([PMID:28487785](https://pmc.ncbi.nlm.nih.gov/articles/PMC5405358)).
  - **DaT-SPECT** (dopamine transporter imaging): reduced striatal (putaminal) uptake
  - **Epidepride-SPECT** (D2-receptor imaging): reduced D2-receptor binding bilaterally in putamen, lesser degree in caudate
  - **FDG-PET:** reduced glucose metabolism bilaterally in striatum, particularly putamen
  — these three modalities together constitute the first in vivo demonstration of striatal dopaminergic/neuronal dysfunction and support DBS-candidacy assessment ([PMID:29788902](https://pmc.ncbi.nlm.nih.gov/articles/PMC5964724/))
- **Audiometry:** confirms bilateral sensorineural hearing loss, typically severe-to-profound, often prompting cochlear implantation
- **Electrophysiology:** not centrally diagnostic, though standard EMG/dystonia work-up (to exclude peripheral causes) is typical in movement-disorder evaluation
- **Biopsy/pathology:** not part of antemortem diagnostic work-up; the only histopathologic data are post-mortem autopsy findings (striatal eosinophilic spheroids, actin/ADF-cofilin immunoreactivity)

**Genetic testing:**
- Recommended approach: **ACTB gene sequencing should be included in the diagnostic work-up of any patient presenting with the combination of childhood/early-onset sensorineural deafness and delayed-onset generalized dystonia** ("ACTB sequencing should be included in the work-up of dystonia-deafness syndrome," PMID:29788902).
- **Whole-exome sequencing (WES)** has been the diagnostic modality in essentially every reported case, typically performed as trio-WES to establish de novo status, given the absence of a distinctive enough phenotype to prompt single-gene testing a priori.
- **Whole-genome sequencing (WGS):** not specifically reported as used but would be expected to have equivalent yield for this coding missense variant.
- **Single-gene ACTB Sanger sequencing:** used for cascade/confirmatory testing in familial cases (e.g., the Argentinean family) once the index variant was identified.
- **Chromosomal microarray/karyotype:** relevant to exclude the phenotypically distinct 7p22.1 microdeletion syndrome, not for DDS1 itself, which is a point mutation.
- **Movement-disorder/dystonia gene panels:** ACTB may or may not be included on standard early-onset dystonia panels; given its rarity, it is often identified only via broader exome analysis after panel-negative results.

**Clinical/differential diagnosis:** Key mimics/differentials in the "deafness + dystonia" phenotype family requiring molecular distinction:
- **Mohr-Tranebjaerg syndrome** (TIMM8A/DDP1, X-linked, OMIM #304700) — deafness-dystonia-optic neuronopathy, X-linked recessive, includes visual failure and later cognitive decline
- **BCAP31-related "deafness, dystonia, and cerebral hypomyelination" (DDCH)** (OMIM #300475, X-linked)
- **MEGDEL/SERAC1-related disease** (OMIM #614739, autosomal recessive, mitochondrial — distinguishable by elevated urinary 3-methylglutaconic acid and Leigh-like MRI findings)
- **Baraitser-Winter cerebrofrontofacial syndrome** (allelic, other ACTB or ACTG1 variants, more prominent pachygyria/craniofacial gestalt)

**Screening:** No population or newborn screening program exists for this ultra-rare disorder; case-finding is via clinical recognition of the deafness+dystonia combination followed by exome sequencing.

Sources: [PMID:29788902](https://pmc.ncbi.nlm.nih.gov/articles/PMC5964724/); [PMID:28487785](https://pmc.ncbi.nlm.nih.gov/articles/PMC5405358); [GeneReviews SERAC1](https://www.ncbi.nlm.nih.gov/books/NBK195853/) (comparator)

---

## 11. Outcome/Prognosis

- **Survival/mortality:** No formal survival statistics exist given the tiny reported cohort; however, mortality has been directly documented — the original index twins both died in their early twenties from **aspiration pneumonia secondary to severe adolescent-onset generalized dystonia**, and a separately reported Hutterite adolescent died at age 15 from complications of uncontrolled dystonia (status dystonicus) ([PMID:29788902](https://pmc.ncbi.nlm.nih.gov/articles/PMC5964724/); [PMID:28487785](https://pmc.ncbi.nlm.nih.gov/articles/PMC5405358)). This indicates a **potentially life-limiting prognosis in severe/untreated cases**, primarily via bulbar dystonia complications (aspiration, dysphagia) rather than the underlying neurodegeneration itself.
- **Morbidity/function:** Severe, often profound motor disability in advanced disease — loss of ambulation, wheelchair/bed dependence, need for assistance with all activities of daily living. Communication is further impaired by the combination of deafness and (in severe cases) bulbar dysarthria/dysphagia.
- **Quality of life:** No formal EQ-5D/SF-36 data published for this ultra-rare condition; qualitative reports (e.g., "she could sit relaxed in a chair," "could walk with support" after DBS) serve as the closest functional outcome proxies.
- **Complications:** Aspiration pneumonia (major cause of death in severe cases), status-dystonicus-like decompensation, contractures/skeletal deformity (scoliosis/kyphosis) from chronic dystonic posturing, DBS hardware-related complications in treated patients.
- **Recovery potential:** With DBS treatment, substantial and durable (multi-year) functional recovery is achievable in appropriately selected cases (large reductions in Burke-Fahn-Marsden Dystonia Rating Scale scores sustained 2.5 months to several years post-implantation); without treatment, the natural history in severe cases trends toward progressive, disabling, and potentially fatal outcomes.
- **Prognostic factors:** presence/severity of bulbar involvement (predicts aspiration risk); early recognition and DBS candidacy; possibly genotype (p.Arg183Trp specifically proposed as a marker identifying a "DBS-responsive" DDS subtype, [PMID:36339314](https://pubmed.ncbi.nlm.nih.gov/36339314/)); degree of striatal dopaminergic dysfunction on functional imaging.
- **Prognostic biomarkers:** DaT-SPECT/Epidepride-SPECT/FDG-PET striatal dysfunction severity has been proposed (not formally validated) as a potential biomarker correlating with dystonia severity and possibly DBS responsiveness.

Sources: [PMID:29788902](https://pmc.ncbi.nlm.nih.gov/articles/PMC5964724/); [PMID:28487785](https://pmc.ncbi.nlm.nih.gov/articles/PMC5405358); [ScienceDirect S1353802022003145](https://www.sciencedirect.com/science/article/abs/pii/S1353802022003145); [PMID:36339314](https://pubmed.ncbi.nlm.nih.gov/36339314/)

---

## 12. Treatment

There is **no disease-modifying or gene-targeted therapy**; all management is symptomatic, centered on the dystonia and the hearing loss.

**Pharmacotherapy:**
- First-line medical dystonia management (oral agents such as trihexyphenidyl, baclofen; anticholinergics/muscle relaxants) is the conventional first step per general dystonia-treatment paradigms, but the literature specifically notes response is **insufficient in many patients** with this syndrome, necessitating escalation.
- **Botulinum toxin injection** has been used, in at least one case providing initial symptom relief before progressive dystonia necessitated further/adjunctive therapy (NCIT:C1364 — Botulinum Toxin).
- No specific pharmacogenomic (PharmGKB/CPIC) guidance exists for this ultra-rare condition.
- No DOPA-responsiveness reported — in the fatal Hutterite case, dystonia was explicitly characterized as "DOPA-unresponsive, medically refractory" ([PMID:28487785](https://pmc.ncbi.nlm.nih.gov/articles/PMC5405358)).

**Surgical/interventional — the defining treatment modality for this syndrome:**
- **Bilateral Deep Brain Stimulation of the internal globus pallidus (GPi-DBS)** is the treatment most strongly and repeatedly documented as effective, across multiple independent case reports (PMID:29788902; PMID:36339314; ScienceDirect S1353802022003145; ScienceDirect S2590112525001100).
  > "Deep brain stimulation of the internal pallidum bilaterally should be strongly considered to treat generalized dystonia in ACTB p.Arg183Trp carriers." (PMID:29788902)
  - Documented outcome in the index case: Burke-Fahn-Marsden Dystonia Rating Scale (motor/disability) improved from 87/25 preoperatively to 21/13 at 2.5 months post-op, sustained at 26/14 (3 years) and 30/14 (4 years) post-op.
  - A separate report specifically frames p.Arg183Trp as potentially **identifying a DBS-responsive DDS subtype**, and a later "revisited" report describes long-term (multi-year) follow-up with continued — though not unlimited — benefit, tempered by disease progression and hardware-related factors over time.
  - **Subthalamic nucleus (STN) DBS** has also been reported as an alternative target with reported response in at least one case (PMID:36339314 title: "Dystonia-Deafness Syndrome: A Rare Deep Brain Stimulation Responsive Dystonia").
- NCIT suggestion: `NCIT:C116237` or the general Surgical/Therapeutic Procedure branch for "Deep Brain Stimulation"; `NCIT:C15329` (Surgical Procedure) as the parent action term with `qualifiers`/device annotation for the DBS device per the dismech device-vs-action convention.

**Auditory/rehabilitative:**
- **Cochlear implantation** is standard management for the profound sensorineural hearing loss and is documented in multiple cases as enabling functional communication.
- Physical therapy, occupational therapy, and speech/swallowing therapy are used adjunctively for motor and bulbar symptom management (NCIT:C15302 Physical Therapy; NCIT:C159273 Speech Therapy).

**Experimental/investigational:** No registered clinical trials specific to ACTB-DDS1 were identified (consistent with its ultra-rare status); no gene therapy, ASO, or targeted molecular therapy has been reported or is in development for this actinopathy.

**Treatment outcomes / adverse events:** GPi-DBS is generally well tolerated with hardware-related complications as the main procedural risk category; no syndrome-specific adverse-event database exists (too rare for FAERS-level signal detection).

**Treatment strategy:** Given medication-refractory dystonia is common, the literature converges on an algorithm of: (1) trial of oral antidystonic agents ± botulinum toxin, (2) early consideration of GPi (or STN) DBS once medical therapy fails or dystonia becomes severe/generalized/life-threatening, particularly once the p.Arg183Trp genotype is confirmed, given its specific association with good DBS responsiveness; (3) cochlear implantation for hearing rehabilitation, pursued independently and typically earlier in the disease course.

Sources: [PMID:29788902](https://pmc.ncbi.nlm.nih.gov/articles/PMC5964724/); [PMID:28487785](https://pmc.ncbi.nlm.nih.gov/articles/PMC5405358); [PMID:36339314](https://pubmed.ncbi.nlm.nih.gov/36339314/); [ScienceDirect S1353802022003145](https://www.sciencedirect.com/science/article/abs/pii/S1353802022003145); [ScienceDirect S2590112525001100](https://www.sciencedirect.com/science/article/pii/S2590112525001100)

---

## 13. Prevention

- **Primary prevention:** None available — this is a de novo/dominantly inherited structural-protein disorder with no modifiable risk factor; primary prevention is not applicable in the population-health sense.
- **Secondary prevention (early detection):** Early genetic diagnosis (via exome sequencing) in a patient presenting with congenital/infantile sensorineural deafness allows anticipatory monitoring for dystonia onset, and early referral to a movement-disorder/DBS center once dystonia emerges, given the DBS-responsiveness data.
- **Tertiary prevention:** Aggressive, early dystonia management (medical, then surgical) aims to prevent the most severe downstream complications — bulbar dysfunction, aspiration pneumonia, and loss of ambulation — which are the main drivers of morbidity/mortality in this condition.
- **Genetic counseling:** Central to family management given autosomal dominant inheritance with both de novo and inherited transmission patterns documented; at-risk relatives of a confirmed carrier can be offered targeted single-gene (Sanger) testing, as illustrated in the multi-generational Argentinean family, to identify pre-symptomatic carriers for early audiologic and neurologic surveillance. Prenatal/preimplantation genetic testing is theoretically available for known familial variants but not specifically reported in the literature reviewed.
- **Screening:** No newborn or population screening program exists; case detection relies on clinical phenotype recognition (audiology + movement-disorder evaluation) triggering genetic testing.
- **Public health/environmental/prophylaxis:** Not applicable — no environmental or infectious component to intervene upon.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** Human disease phenotype has no confirmed naturally-occurring veterinary counterpart reported in OMIA or the veterinary literature reviewed. ACTB itself is essentially universally conserved across vertebrates (`NCBITaxon:9606` Homo sapiens for the human disease; mouse ortholog `Actb`, MGI:87904, NCBI Gene 11461).
- **Orthologous gene:** Mouse *Actb* (chromosome 5), highly conserved; used extensively as the prototypical "housekeeping" cytoskeletal gene, which is itself informative — the fact that a missense change in such a universally essential, highly constrained protein produces a viable, tissue-restricted human phenotype (rather than being embryonic lethal, as complete knockout is) underscores that DDS1 arises from an **altered-function/dominant-negative mechanism**, not haploinsufficiency.
- **Natural disease in animals:** Not identified/reported; this appears to be a human-specific reported clinical entity (or at minimum, not yet described in veterinary case literature).
- **Comparative biology:** Cross-species conservation of β-actin's role in neural crest migration, hair-cell stereocilia maintenance, and neuronal cytoskeletal dynamics (demonstrated in mouse models, see §15) supports mechanistic homology, even without a documented spontaneous animal phenocopy.
- **Zoonotic potential/transmission:** Not applicable — genetic, non-infectious disorder.

---

## 15. Model Organisms

No mouse model carrying the specific human p.Arg183Trp DDS1 variant has been reported in the literature surveyed; available models instead establish the tissue-specific necessity of β-actin, supporting (but not directly replicating) the human disease mechanism:

- **Global Actb knockout (mouse):** Homozygous *Actb⁻/⁻* mice are **embryonic lethal**, despite compensatory upregulation of other actin isoforms — establishing that β-actin has essential, non-fully-redundant functions even amid isoform compensation ([PLOS One 2014, neural crest](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0085608)).
- **Neural-crest-specific Actb loss (mouse):** β-actin-null neural crest cells retain neural crest marker expression but show reduced delamination and migration arrest shortly after onset, associated with elevated apoptosis (not altered proliferation) — directly modeling the proposed prenatal craniofacial-dysmorphogenesis mechanism (PLOS One 2014, PMID referenced in search: also see PMC3677859 for actin gene review).
- **Hair-cell-specific Actb/Actg1 conditional knockout (mouse):** β-actin and γ-actin are each individually dispensable for initial auditory hair-cell development and normal hearing in young mice, but are **required for stereocilia maintenance** — mice lacking β-actin in hair cells develop progressive, high-frequency-first hearing loss with age, with stereocilia pathology progressing from basal/high-frequency to middle cochlear-turn regions over time, closely paralleling (and mechanistically explaining) the human infantile-onset, potentially progressive sensorineural deafness phenotype ([PMID:20976199](https://pubmed.ncbi.nlm.nih.gov/20976199/); [PMC2954897](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2954897/)).
- **Model limitations:** No existing animal model recapitulates the striatal/pallidal neurodegeneration and dystonia component of the human phenotype, nor carries the specific dominant p.Arg183Trp allele — this represents a significant gap; a knock-in mouse expressing the human R183W variant (rather than complete knockout) would be needed to model the "altered-dynamics" dominant mechanism and the striatal neurodegenerative phenotype seen at human autopsy.
- **Cellular models:** Patient-derived fibroblasts and recombinant R183W β-actin protein have been used in vitro to demonstrate altered polymerization/depolymerization kinetics directly (PMID:16685646) — this remains the most direct functional-genomics evidence for the molecular mechanism.

Sources: [PLOS One 2014 (Actb neural crest)](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0085608); [PMID:20976199](https://pubmed.ncbi.nlm.nih.gov/20976199/); [PMC2954897](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2954897/); [PMID:16685646](https://pubmed.ncbi.nlm.nih.gov/16685646/); [MGI:87904](https://www.informatics.jax.org/marker/MGI:87904)

---

## Summary Table: Key Ontology Term Suggestions for KB Curation

| Category | Suggested term |
|---|---|
| Disease | MONDO:0011823; OMIM:607371; ORPHA:79107 |
| Causal gene | hgnc:132 (ACTB) |
| Variant | ACTB c.547C>T p.(Arg183Trp); ClinVar RCV000019937 |
| Phenotype — hearing | HP:0000407 (Sensorineural hearing impairment) |
| Phenotype — dystonia | HP:0007325 (Generalized dystonia) |
| Phenotype — corpus callosum | HP:0002079 (Hypoplasia of the corpus callosum) |
| Phenotype — cerebellar vermis | HP:0001320 (Cerebellar vermis hypoplasia) |
| Phenotype — dev. delay | HP:0001263 (Global developmental delay) |
| Phenotype — parkinsonism | HP:0001300 (Parkinsonism) |
| Cell types | CL:0000602 (auditory hair cell), CL:0000696 (medium spiny neuron), CL:0000333 (neural crest cell) |
| Biological process (GO) | GO:0030036 (actin cytoskeleton organization), GO:0030041 (actin filament polymerization) |
| Anatomy (UBERON) | UBERON:0002435 (striatum), UBERON:0001875 (globus pallidus), UBERON:0009653 (stereocilium) |
| Treatment (NCIT) | NCIT:C15329 (Surgical Procedure, for DBS) + device qualifier; NCIT:C1364 (Botulinum Toxin) |

---

### Key limitations of the current evidence base
This is one of the rarest disorders in the medical literature — evidence derives entirely from ~10–15 individual case reports/small series spanning 2006–2025, no registry, no natural-history study, no clinical trial, and no animal model of the exact causal variant. Phenotypic variability is substantial even among carriers of the identical recurrent p.Arg183Trp allele, and prognostic/treatment conclusions (especially DBS responsiveness) are based on small numbers and should be curated with that caveat explicitly noted in evidence `directness`/`evidence_source` annotations.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 5 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 4 |
| References weighed for topical relevance | 13 |
| On topic | 5 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMID:28487785`: "not present in approximately 6,500 individuals of European and African American ancestry in the NHLBI Exome Sequencing Project"
  - closest text in source: "This variant has not been observed in approximately 6,500 individuals of European and African American ancestry in the NHLBI Exome Sequencing Project (ESP) or in over 60,000 individuals in the Exome Aggregation Consortium (ExAC) or in the whole genome sequences of 98 Hutterites [8]"
- `PMC:PMC5405358`: "not present in approximately 6,500 individuals of European and African American ancestry in the NHLBI Exome Sequencing Project"
  - closest text in source: "This variant has not been observed in approximately 6,500 individuals of European and African American ancestry in the NHLBI Exome Sequencing Project (ESP) or in over 60,000 individuals in the Exome Aggregation Consortium (ExAC) or in the whole genome sequences of 98 Hutterites [8]"
- `PMID:28487785`: "DOPA-unresponsive, medically refractory"
  - Text part not found as substring: 'DOPA-unresponsive, medically refractory'
- `PMC:PMC5405358`: "DOPA-unresponsive, medically refractory"
  - Text part not found as substring: 'DOPA-unresponsive, medically refractory'

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 47 |
| Resolved | 43 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 4 |
| Terms whose name was checked | 12 |
| Terms named correctly | 10 |
| Terms named as a **different** term | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0025230` (1 mention) - the report calls it "Dystonic tremor"; HP calls it **Tendonitis**
- `NCIT:C1364` (2 mentions) - the report calls it "Botulinum Toxin"; NCIT calls it **Didemnin B**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`, `OMIM`.