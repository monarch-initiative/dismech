---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-23T15:00:36.883243'
end_time: '2026-09-23T15:04:39.165493'
duration_seconds: 242.28
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: GPD1 Deficiency
  mondo_id: MONDO:0013771
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
  web_search_requests: 17
  num_turns: 24
  total_cost_usd: 1.4472926
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
citation_count: 14
reference_validation:
  total_references: 18
  verified: 11
  not_found: 0
  unverifiable: 7
  confabulation_rate: 0.0
  quotes_checked: 0
  quotes_valid: 0
  quotes_not_checkable: 4
  relevance_assessed: 11
  on_topic: 7
  validator_version: 0.2.1
term_validation:
  total_terms: 36
  verified: 31
  not_found: 0
  obsolete: 1
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 15
  labels_matching: 10
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: GENO:0000148
    reported_labels:
    - biallelic homozygous
    ontology_label: autosomal recessive inheritance
  - term_id: UBERON:0000178
    reported_labels:
    - blood, for triglyceride measurement
    ontology_label: blood
  - term_id: NCIT:C15709
    reported_labels:
    - Liver Biopsy
    ontology_label: Genetic Testing
  - term_id: NCIT:C61961
    reported_labels:
    - Fenofibrate
    ontology_label: Tacrine
  labels_variant: 1
  obsolete_terms:
  - term_id: GO:0004367
    ontology_label: GO_0004367
    replaced_by: GO:0047952
  unresolvable_prefixes:
  - OMIM
  - ORPHA
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** GPD1 Deficiency
- **MONDO ID:** MONDO:0013771 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **GPD1 Deficiency** covering all of the
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

# GPD1 Deficiency (Transient Infantile Hypertriglyceridemia, HTGTI) — Comprehensive Research Report

## Identifier note (flagged discrepancy)

The template lists **OMIM:611090** as a candidate identifier for GPD1 Deficiency. That MIM number does **not** correspond to this disease — OMIM #611090 is *Intellectual Developmental Disorder, Autosomal Recessive 12 (MRT12)*, an unrelated condition ([OMIM #611090](https://omim.org/entry/611090)). The correct OMIM identifiers are:
- **Phenotype MIM: 614480** — *Hypertriglyceridemia, Transient Infantile* ([OMIM #614480](https://omim.org/entry/614480))
- **Gene MIM: 138420** — *Glycerol-3-Phosphate Dehydrogenase 1; GPD1* ([OMIM *138420](https://omim.org/entry/138420))
- **Gene:** GPD1, HGNC:4455, cytogenetic location **12q13.12** (GRCh38: chr12:50,104,008–50,111,313), 8 exons ([GeneCards](https://www.genecards.org/cgi-bin/carddisp.pl?gene=GPD1); [GTR](https://www.ncbi.nlm.nih.gov/gtr/genes/2819/)). Note one AI-summarized source mis-stated the locus as "2q12-q13" — this is an error; 12q13.12 is the correct, multiply-confirmed location.
- **Orphanet:** ORPHA:300293, listed as germline GPD1 mutation causing "transient infantile hypertriglyceridemia and hepatic steatosis in infants."
- **MONDO:0013771** as given in the template is plausible as the disease-node identifier used by Monarch/MONDO for this entry but was not independently re-verified against a live MONDO browse in this session — treat as a lead pending confirmation via `just validate-terms`/OAK lookup before binding.
- **No dedicated GeneReviews chapter was found** for GPD1 deficiency/HTGTI in this search.

---

## 1. Disease Information

**Overview.** GPD1 deficiency, clinically designated **Transient Infantile Hypertriglyceridemia (HTGTI)**, is a rare autosomal recessive inborn error of triglyceride/glycerolipid metabolism caused by biallelic loss-of-function variants in *GPD1*, encoding cytosolic NAD⁺-dependent glycerol-3-phosphate dehydrogenase 1. It presents in infancy with hepatomegaly, marked hypertriglyceridemia, elevated transaminases, hepatic steatosis, and — in a substantial minority — hepatic fibrosis progressing occasionally to cirrhosis (Basel-Vanagaite et al., 2012, PMID not directly retrieved but paper is *Am J Hum Genet* 2012;90:49–60, [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0002929711005295)). Despite the name "transient," a growing literature (see §11) shows the biochemical/hepatic phenotype is often only *partially* transient, and the disease has been characterized as "a rare, overlooked cause of liver disease" in a 2025 review ([Journal of Human Genetics 2025](https://www.nature.com/articles/s10038-025-01339-9); [PMC12137118](https://pmc.ncbi.nlm.nih.gov/articles/PMC12137118/)) and, in an August 2026 commentary, questioned as "A Transient Disease or a Great Masquerader?" (Das et al. 2026, *Am J Med Genet A*, PMID:42063230, [Wiley](https://onlinelibrary.wiley.com/doi/10.1002/ajmg.a.70188)).

**Synonyms:** Transient infantile hypertriglyceridemia; HTGTI; GPD1 deficiency; glycerol-3-phosphate dehydrogenase 1 deficiency; glycerophosphate dehydrogenase 1 deficiency.

**Source of information base:** The evidence base is almost entirely **aggregated case-report/case-series literature** (individual pediatric/genetics case reports, plus several pooled literature reviews of 17–45 cumulative cases as of 2020–2025), not large disease-level registries or EHR cohorts. There is no dedicated patient registry or GeneReviews chapter identified.

---

## 2. Etiology

**Disease causal factor:** Monogenic — biallelic (homozygous or compound heterozygous) pathogenic variants in *GPD1* (12q13.12) are necessary and sufficient. No environmental, infectious, or polygenic contribution has been proposed; this is a purely Mendelian enzymopathy.

**Genetic risk factors:**
- Homozygosity for *GPD1* loss-of-function alleles (splice-site, nonsense, missense, frameshift).
- **Consanguinity** is a strong contributing factor at the population level: reported in ~28–40% of published cases (10/36, 27.7%, per the 2024 North-India series reviewing global literature, [PMC11743310](https://pmc.ncbi.nlm.nih.gov/articles/PMC11743310/); ~40% per another pooled review, [PMC12137118](https://pmc.ncbi.nlm.nih.gov/articles/PMC12137118/)). The founding description was in **four highly consanguineous Israeli Arab families** sharing the splice variant c.361-1G>C (Basel-Vanagaite et al. 2012).
- Founder effect: the c.361-1G>C splice-acceptor variant in intron 3 recurs across the original Israeli Arab kindred as a shared haplotype-associated allele.
- 86.1% of reported genotypes are homozygous, 13.9% compound heterozygous ([PMC11743310](https://pmc.ncbi.nlm.nih.gov/articles/PMC11743310/)).

**Environmental risk factors:** None specifically established; disease is congenital/metabolic rather than exposure-driven. Dietary fat intake modulates *severity* (see Treatment) but is not causal.

**Protective factors:** None reported in the literature; no protective alleles or modifier alleles have been characterized. The residual/partial enzymatic activity retained by some missense alleles (vs. null/truncating alleles) appears associated with milder or more clearly "transient" courses, though this genotype-severity correlation is not rigorously established across the small case series.

**Gene-environment interaction:** Dietary fat load (especially long-chain triglycerides and simple sugars, which increase hepatic glycerol-3-phosphate flux into triglyceride synthesis) appears to exacerbate hypertriglyceridemia and hepatic fat accumulation in affected children, which underlies the low-fat/MCT dietary management strategy (see §12). This is inferred from treatment-response literature rather than formally demonstrated G×E study designs.

**Suggested ontology terms:** MONDO (disease, pending verification above); GENO:0000148 (biallelic homozygous) / GENO:0000135 (compound heterozygous); HGNC:4455 (GPD1).

---

## 3. Phenotypes

The phenotype set below draws on the two largest pooled reviews (36 cumulative global cases through Dec 2023, [PMC11743310](https://pmc.ncbi.nlm.nih.gov/articles/PMC11743310/); 45 cases across 18 studies as of 2025, [PMC12137118](https://pmc.ncbi.nlm.nih.gov/articles/PMC12137118/)) plus individual case reports for rarer manifestations.

| Phenotype | Frequency (pooled literature) | HPO term (suggested) | Notes |
|---|---|---|---|
| Hypertriglyceridemia | 97.2% (35/36); also reported ~95–98% in other pooled series | HP:0002155 Hypertriglyceridemia | Moderate–severe; often several-fold to markedly elevated; peaks typically within first 6 months of life |
| Hepatomegaly | 94.4% (34/36); 100% in a smaller 18-patient series | HP:0002240 Hepatomegaly | Often the presenting clinical sign |
| Hepatic steatosis / fatty liver (imaging or biopsy) | 100% (26/26 with imaging; 18/18 biopsied) | HP:0001397 Hepatic steatosis | Universal finding on imaging/biopsy in reported cases |
| Elevated transaminases | ~95–100% depending on series | HP:0002910 Elevated hepatic transaminase | Typically mild–moderate (1.5–3× ULN) elevation |
| Hepatic fibrosis (biopsy) | 94.4% (17/18 biopsied) | HP:0001395 Hepatic fibrosis | High rate among biopsied cases — biopsy is not universal, so ascertainment bias toward more severe cases is likely |
| Cirrhosis | 22.2% (4/18 biopsied) | HP:0001394 Cirrhosis | Occurs in a meaningful minority; includes adolescent-onset case (Matarazzo et al. 2020) |
| Splenomegaly | 22.2% (8/36) | HP:0001744 Splenomegaly | |
| Growth failure / short stature | 22.2–23% (8/36) | HP:0004322 Short stature / HP:0001508 Failure to thrive | |
| Hypoglycemia (fasting) | ~11% | HP:0001943 Hypoglycemia | Rare but reported, including with insulin resistance (Karger 2022/PMC9801319) |
| Insulin resistance / obesity | Reported in a subset (case reports) | HP:0040270 Obesity / HP:0000855 Insulin resistance (proxy term) | E.g., Chinese boy with obesity, insulin resistance, fatty liver, short stature (PMID:28944580) |
| Elevated total bile acids / intrahepatic cholestasis | Case-reported | HP:0030957 Elevated circulating bile acid concentration | |
| Organic aciduria | Case-reported | (variable, non-specific organic aciduria) | |
| Hepatic adenoma | Single case report (first reported) | HP:0006725 Hepatic adenoma (proxy) | First reported case of hepatic adenoma arising in HTGTI (PMID:35365473, [PMC8977762](https://pmc.ncbi.nlm.nih.gov/articles/PMC8977762/)) |
| Kidney disease (renal) | Rare, case-reported | (non-specific) | Listed among "rare phenotypes" in pooled review |
| Vomiting | Case-reported | HP:0002013 Vomiting | |

**Onset:** Median age at diagnosis 6 months (range 1–164 months) in the largest pooled series ([PMC11743310](https://pmc.ncbi.nlm.nih.gov/articles/PMC11743310/)); most present within the first year of life, though later childhood/adolescent presentations (including a first diagnosis at age 16 with established cirrhosis) are recorded.

**Severity/progression:** Variable — spans an apparently "benign," self-limited biochemical course in some infants to progressive fibrosis/cirrhosis in others; genotype-phenotype correlation is not well established.

**Quality of life impact:** Not formally studied with validated instruments (no EQ-5D/SF-36/PROMIS data identified). Reported outcomes emphasize preserved growth and neurodevelopment in most followed patients; QoL burden is inferred to derive chiefly from chronic hepatic monitoring, dietary restriction, and (in severe cases) cirrhosis-related morbidity.

---

## 4. Genetic/Molecular Information

**Causal gene:** *GPD1* (HGNC:4455), OMIM *138420, chr12q13.12.

**Variant spectrum:** As of the most recent pooled reviews (2024–2025), **~24 distinct disease-causing GPD1 variants** have been reported worldwide ([PMC12137118](https://pmc.ncbi.nlm.nih.gov/articles/PMC12137118/)). Representative variants, all recessive/biallelic and largely private/founder alleles:

| Variant (cDNA/protein) | Type | Source |
|---|---|---|
| c.361-1G>C (p.Ile119fsX94) | Splice-acceptor, intron 3 → frameshift/truncation at residue 213, disrupting NAD-binding/substrate-recognition domain | Basel-Vanagaite et al. 2012 (founder allele, 4 consanguineous Israeli Arab families) |
| c.628G>C (p.G210R) | Missense | Chinese case report |
| c.454C>T (p.Q152*) | Nonsense | Case report |
| c.895G>A (p.G299R) | Missense | Matarazzo et al. 2020 (JIMD Reports), homozygous, associated with adolescent cirrhosis |
| c.805C>T (p.R269W) | Missense | Karger 2022 case, associated with hypoglycemia/insulin resistance |
| c.917T>C, c.905C>G | Missense (novel) | Reported in 2024 North India series ([PMC11743310](https://pmc.ncbi.nlm.nih.gov/articles/PMC11743310/)) |

Classification per ACMG/AMP is not systematically reported across the literature but the recurring splice/nonsense/frameshift alleles are consistent with **loss-of-function (biallelic null)** as the principal molecular mechanism; missense alleles presumably retain partial activity, though functional enzymatic assays confirming residual activity for each specific variant were not identified in this search.

**Allele frequency in population databases:** No systematic gnomAD/ExAC carrier-frequency figure for *GPD1* pathogenic variants was retrievable in this session; this should be checked directly against gnomAD v4 per-variant pages before citing a specific number in the KB entry (each of the variants above should be individually queried).

**Somatic vs. germline:** Exclusively germline/constitutional in this disease (not a somatic/cancer-associated gene in this context — do not conflate with the distinct paralog *GPD1L*, associated with Brugada syndrome/cardiac Na⁺ channel dysfunction via a different mechanism, PMC3150966).

**Functional consequence:** Loss of GPD1 catalytic (cytosolic glycerol-3-phosphate dehydrogenase) activity — i.e., **loss of function**, not gain-of-function or dominant-negative in the reported alleles.

**Modifier genes:** None established. Genotype-severity correlation (e.g., null vs. missense allele → cirrhosis risk) is suggested informally by case pattern but not statistically demonstrated.

**Epigenetic information:** None specifically reported for human GPD1 deficiency.

**Chromosomal abnormalities:** Not applicable — this is a single-gene sequence-variant disease, not a CNV/structural disorder.

---

## 5. Environmental Information

- **Environmental factors:** None causally implicated; this is a purely monogenic disease.
- **Lifestyle factors:** Dietary fat composition and quantity modulate the severity of the biochemical phenotype (hypertriglyceridemia, hepatic fat accumulation) — see Treatment. High dietary fat, particularly long-chain triglycerides, appears to worsen hypertriglyceridemia; medium-chain triglyceride (MCT)-enriched, low-long-chain-fat diets are used therapeutically.
- **Infectious agents:** None implicated.

---

## 6. Mechanism / Pathophysiology

**Causal chain (numbered):**

1. **Biallelic loss-of-function variant in *GPD1*** (e.g., c.361-1G>C splice defect, or missense/nonsense alleles) → **leads to** absent or markedly reduced cytosolic NAD⁺-dependent glycerol-3-phosphate dehydrogenase 1 enzymatic activity.
2. Loss of GPD1 activity **abolishes/reduces** the reversible cytosolic interconversion of **dihydroxyacetone phosphate (DHAP) ⇌ glycerol-3-phosphate (G3P)**, which normally couples glycolysis/gluconeogenesis to glycerolipid synthesis and regenerates cytosolic NAD⁺ from NADH.
3. The proposed primary mechanistic hypothesis (Basel-Vanagaite et al. 2012) is that GPD1 loss **limits the conversion of G3P back to DHAP**, which **results in** an increased pool of G3P available as substrate for glycerolipid/triglyceride backbone synthesis (via glycerol-3-phosphate acyltransferase and downstream acylation steps) — i.e., a substrate-accumulation mechanism driving excess hepatic triglyceride synthesis. (Note: this direction of flux — i.e., which arm of the readily reversible reaction is rate-limiting in vivo — is inferred rather than directly demonstrated biochemically in patient tissue, and should be flagged in curation as a hypothesis rather than a confirmed mechanism.)
4. An alternative/complementary hypothesis in the 2025 review ([PMC12137118](https://pmc.ncbi.nlm.nih.gov/articles/PMC12137118/)) proposes that fatty liver in GPD1 deficiency **"may result from excessive acylation of dihydroxyacetone phosphate (DHAP)"** via the alternative (acyl-DHAP) pathway of glycerolipid synthesis, which becomes favored when the GPD1-dependent G3P-generating route is blocked — this branch point is explicitly noted as mechanistically unclear ("detailed mechanisms remain unclear").
5. Excess hepatic triglyceride synthesis and/or impaired triglyceride clearance from hepatocytes **leads to** intrahepatocellular lipid droplet accumulation → **hepatic steatosis** (macro/microvesicular, confirmed histologically in nearly all biopsied cases).
6. Excess hepatic triglyceride is also secreted into the circulation as VLDL, **contributing to** systemic **hypertriglyceridemia**, which peaks in the first months of life and in many patients gradually declines with age (the basis for the "transient" designation), though this decline is incomplete/variable across patients.
7. Chronic hepatocellular lipid accumulation and associated lipotoxic/inflammatory stress **leads to** hepatocyte injury (reflected in elevated transaminases) and, over time, a **fibrogenic response** — progressive deposition of extracellular matrix — in a majority of biopsied patients (94.4%), and in a minority (22.2%) **progresses to cirrhosis** and, in single cases, to hepatic adenoma formation (a first-reported association, PMID:35365473) — mechanistically analogous to metabolic-dysfunction-associated steatotic liver disease (MASLD/NAFLD) progression, but of monogenic origin.
8. **Branch — carbohydrate/energy metabolism:** because DHAP↔G3P interconversion is also part of the cytosolic arm of the glycerol-3-phosphate shuttle that regenerates cytosolic NAD⁺ (paired with mitochondrial GPD2, which is FAD-linked and feeds electrons into the respiratory chain via coenzyme Q), GPD1 loss also **impairs gluconeogenesis from glycerol**. In mouse Gpd1-knockout models this **leads to** a compensatory shift toward **increased gluconeogenesis from glycogenic amino acids (notably alanine)**, evidenced by higher blood alanine and enhanced hepatic alanine-driven gluconeogenesis during fasting, and — counterintuitively — *higher* blood glucose after 1–4 hours of fasting than wild-type mice (Tanner et al., PMID:27733253). This branch is proposed as the mechanistic basis for the rare hypoglycemia/insulin-resistance phenotypes reported in some human patients, though the direct human-mechanistic link is inferred from the mouse fasting data rather than demonstrated in patient-derived tissue.
9. In some patients, chronic disturbance of hepatic lipid/glucose handling **is associated with** downstream insulin resistance and obesity (case-reported subset), though causal directionality (GPD1 loss → primary insulin resistance, vs. secondary to hepatic steatosis) is not established.

**Molecular pathways:** Glycerolipid/triglyceride biosynthesis pathway (KEGG map00561); glycerophospholipid metabolism; the glycerol-3-phosphate shuttle (bridges glycolysis and oxidative phosphorylation); gluconeogenesis (glycerol input arm).

**Cellular processes:** Lipid droplet biogenesis/accumulation in hepatocytes (steatosis); hepatic stellate cell activation and extracellular matrix deposition (fibrogenesis, likely via the same final-common-pathway mechanisms modeled generically in dismech's `fibrotic_response` module); possible lipotoxic hepatocellular stress.

**Protein dysfunction:** Loss-of-function via (a) splice disruption/premature truncation removing catalytic/substrate-recognition residues (c.361-1G>C), or (b) missense substitutions presumably destabilizing the NAD-binding or catalytic domain (e.g., p.G210R, p.G299R, p.R269W) — specific structural/functional characterization of these missense alleles (e.g., via AlphaFold modeling or recombinant enzyme assay) was not identified in this search and would need dedicated retrieval.

**Metabolic changes:** Elevated hepatic and circulating triglycerides; altered cytosolic NADH/NAD⁺ ratio; compensatory amino-acid-driven gluconeogenesis (mouse data); possible organic aciduria (case-reported, mechanism unclear).

**Suggested GO terms:** GO:0006650 (glycerophospholipid metabolic process); GO:0019432 (triglyceride biosynthetic process); GO:0006094 (gluconeogenesis); GO:0004367 (glycerol-3-phosphate dehydrogenase [NAD+] activity, molecular function for GPD1 itself); GO:0055088 (lipid homeostasis).

**Suggested CL terms:** CL:0000182 (hepatocyte) — primary affected cell type; CL:0000632 (hepatic stellate cell) — fibrogenic effector, inferred by analogy rather than directly demonstrated in GPD1-deficiency-specific studies.

**Advanced/omics technologies:** No transcriptomic, proteomic, metabolomic, single-cell, or spatial data specific to human GPD1-deficient liver tissue were identified in this search; the mouse Gpd1-knockout fasting/metabolomics study (PMID:27733253) is the principal molecular-profiling-adjacent dataset available.

---

## 7. Anatomical Structures Affected

- **Primary organ:** Liver (hepatomegaly, steatosis, fibrosis, cirrhosis, and rarely adenoma).
- **Secondary/systemic involvement:** Adipose tissue/systemic lipid metabolism (hypertriglyceridemia); spleen (splenomegaly, presumably secondary to portal hypertension/hepatic disease in advanced cases, or reactive); growth (short stature/failure to thrive); endocrine/metabolic axis (insulin resistance, hypoglycemia in a subset); kidney (rare reported involvement).
- **Body systems:** Digestive system (primary); metabolism/homeostasis; growth; cardiovascular (long-term theoretical risk from hypertriglyceridemia, see Prognosis); immune system (listed among HPO-mapped systems in one search result, though the specific immune phenotype was not itemized in retrieved sources).
- **Tissue/cell level:** Hepatocytes (steatosis, primary site of GPD1 dysfunction consequences); hepatic stellate cells (fibrogenesis, inferred).
- **Subcellular level:** Cytosol (site of GPD1 catalytic activity; contrast with mitochondrial GPD2, part of the same glycerol-3-phosphate shuttle but genetically and clinically distinct).
- **UBERON suggestions:** UBERON:0002107 (liver); UBERON:0002106 (spleen); UBERON:0000178 (blood, for triglyceride measurement).
- **Laterality:** Not applicable (diffuse hepatic process).

---

## 8. Temporal Development

- **Onset:** Typically infantile — most patients present within the first year of life; median age at diagnosis 6 months (range 1–164 months) in the largest pooled series. A minority present later in childhood or adolescence (e.g., first diagnosed at 16 years with established cirrhosis, Matarazzo et al. 2020).
- **Onset pattern:** Generally insidious/subacute, detected via incidental hepatomegaly or lipid-panel abnormality rather than acute presentation, though pancreatitis risk (from severe hypertriglyceridemia) could theoretically present acutely (none reported in the pooled cohort — see Prognosis).
- **Progression:** Variable. Triglycerides "typically peak within the first 6 months of life, tending to decrease with age" ([PMC12137118](https://pmc.ncbi.nlm.nih.gov/articles/PMC12137118/)), consistent with partial biochemical remission. However, on longer follow-up (11–376 months) in the 2024 pooled series, only a minority of patients showed full resolution: hepatomegaly resolved in 35.2% (6/17), triglycerides normalized in 29.1% (7/24), and transaminases normalized in 31.5% (6/19) — meaning the *majority* of followed patients had persistent abnormalities, challenging the "transient" label (hence the 2026 "Great Masquerader" commentary).
- **Disease course pattern:** Can be stable/improving (classic "transient" course) or slowly progressive toward fibrosis/cirrhosis in a subset (~22% progressing to cirrhosis among biopsied cases).
- **Critical periods:** Infancy appears to be the period of peak triglyceride elevation and diagnostic ascertainment; the mechanistic basis for age-related improvement (e.g., changing dietary composition, maturation of alternative lipid-handling pathways) is not established.

---

## 9. Inheritance and Population

- **Inheritance pattern:** Autosomal recessive (biallelic).
- **Penetrance:** Not formally quantified; presumed high/complete given ascertainment via symptomatic presentation, though this is subject to ascertainment bias (asymptomatic homozygotes would not enter the literature).
- **Expressivity:** Markedly **variable** — ranges from apparently self-limited infantile hypertriglyceridemia to progressive cirrhosis, hepatic adenoma, hypoglycemia/insulin resistance, and short stature. This variability is a major theme of recent reviews.
- **Genetic anticipation:** Not reported/applicable (not a repeat-expansion disorder).
- **Germline mosaicism:** Not specifically reported.
- **Founder effects:** Yes — the original 2012 description involved a shared splice variant (c.361-1G>C) across four consanguineous Israeli Arab families, consistent with a regional founder allele. Subsequent case reports come predominantly from China, India, Turkey, Italy, and other diverse populations with largely private (non-recurring) variants, suggesting genetic heterogeneity outside the founder cluster.
- **Consanguinity role:** Substantial — present in ~28–40% of reported cases across pooled series, well above general-population background rates, consistent with a rare autosomal recessive disease.
- **Carrier frequency:** Not established from a population reference database in this search; should be queried directly in gnomAD v4 per-variant.

**Epidemiology:**
- **Prevalence/incidence:** No formal population-based prevalence or incidence estimate exists; the disease is characterized purely by **cumulative reported case counts** — 10 (2012) → 17 (2016) → 31 (2022) → 36 (Dec 2023) → 45 (2025) cases worldwide across the literature, reflecting a very rare, likely underdiagnosed condition (multiple reviews explicitly describe it as "rare, overlooked" and "underdiagnosed").
- **Sex ratio:** ~1.6 male : 1 female among 31 reviewed genetically-confirmed cases (Wang et al. 2022 review, cited in [PMC11743310](https://pmc.ncbi.nlm.nih.gov/articles/PMC11743310/)) — a mild male excess, though the biological basis (vs. ascertainment) is unclear for an autosomal recessive disease.
- **Geographic/ethnic distribution:** Case reports span Israeli Arab (founder cohort), Chinese, Indian (North India series, 5 new cases 2024), Turkish, Italian, and other populations — suggesting the disease is pan-ethnic but detected wherever genomic/exome sequencing is applied to unexplained pediatric fatty liver/hypertriglyceridemia, with likely substantial underascertainment in resource-limited settings (see the 2026 companion paper on "targeted molecular testing in limited-resource settings," Malik et al., [Wiley](https://onlinelibrary.wiley.com/doi/10.1002/ajmg.a.70192)).

---

## 10. Diagnostics

**Clinical/laboratory tests:**
- Fasting lipid panel: marked hypertriglyceridemia (core finding).
- Liver function tests: elevated ALT/AST (typically 1.5–3× ULN).
- Total bile acids (elevated in a subset).
- Fasting glucose (hypoglycemia in a minority).
- Organic acid analysis (organic aciduria reported in some cases, though non-specific).

**Imaging:** Abdominal ultrasound (hepatomegaly, increased echogenicity consistent with steatosis — reported in 100% of imaged cases); transient elastography/FibroScan for non-invasive fibrosis assessment.

**Biopsy/histopathology:** Liver biopsy showing macro/microvesicular steatosis (100% of biopsied cases), fibrosis (94.4%), and cirrhosis (22.2% of biopsied cases) in the pooled series.

**Genetic testing:**
- **Whole-exome sequencing (WES)** is the diagnostic approach used in essentially all recent case identifications, given the absence of a distinctive enough clinical phenotype to prompt single-gene testing a priori, and the rarity/novelty of variants (most are novel, private alleles rather than recurrent hotspots outside the founder cluster).
- Single-gene *GPD1* Sanger sequencing is used for targeted confirmation/segregation analysis once a proband variant is identified, and for carrier testing in consanguineous families or known founder populations.
- A 2026 companion paper specifically addresses genetic-diagnosis nuances and targeted molecular testing strategies for GPD1 deficiency in limited-resource settings (Malik et al., [Wiley](https://onlinelibrary.wiley.com/doi/10.1002/ajmg.a.70192)), suggesting targeted panel/single-gene approaches may be preferable where WES access is limited.

**Differential diagnosis** (per [PMC12137118](https://pmc.ncbi.nlm.nih.gov/articles/PMC12137118/)): infectious hepatitis, Wilson disease, autoimmune hepatitis, alpha-1 antitrypsin deficiency, celiac disease, hemochromatosis, and other causes of unexplained pediatric elevated liver enzymes/hypertriglyceridemia/hepatosteatosis (e.g., other monogenic hypertriglyceridemia syndromes such as familial chylomicronemia syndrome, lipoprotein lipase deficiency, glycogen storage disease).

**Screening:** No newborn screening or population carrier-screening program identified for GPD1 deficiency; diagnosis is currently reactive (triggered by unexplained infantile hepatomegaly/hypertriglyceridemia/fatty liver) rather than proactive.

**Suggested LOINC/ontology terms:** Standard triglyceride, ALT, AST panel LOINC codes (not individually itemized here); NCIT:C15709 (Liver Biopsy) or similar procedure term for the diagnostic biopsy.

---

## 11. Outcome/Prognosis

**Survival/mortality:** No deaths attributable to GPD1 deficiency were identified in the literature reviewed; the disease is not associated with reported mortality in the pooled case series.

**Complication risk (theoretical vs. observed):** Reviews note that hypertriglyceridemia in general "contribute[s] independently to the risk of coronary artery disease and [is] additionally associated with heightened susceptibility to acute pancreatitis" ([PMC12137118](https://pmc.ncbi.nlm.nih.gov/articles/PMC12137118/)) — but critically, in the largest pooled follow-up (11–376 months), **"no pancreatitis, cardiac events, or liver decompensation was reported"** across all 36 reviewed cases ([PMC11743310](https://pmc.ncbi.nlm.nih.gov/articles/PMC11743310/)). This is an important curation point: the theoretical cardiovascular/pancreatitis risk of hypertriglyceridemia has **not** been empirically observed in this specific disease's reported natural history to date, though follow-up duration and cohort size remain limited.

**Disease course / "transient" vs. persistent:** As detailed in §8, only a minority of followed patients show full normalization (hepatomegaly resolution 35.2%, TG normalization 29.1%, transaminase normalization 31.5%), meaning most retain some abnormality at last follow-up, even though severity/degree often improves. Liver fibrosis, once established, does not clearly reverse in the available follow-up data. A subset progresses to cirrhosis (22.2% of biopsied cases) and, in one case, hepatic adenoma. The 2026 commentary explicitly frames this tension as reconsidering the disease as potentially a "great masquerader" rather than uniformly self-limited.

**Prognostic factors:** Not rigorously established; biopsy-proven fibrosis at diagnosis and null/truncating (vs. missense) genotype are plausible but unconfirmed candidate risk factors for a more severe/persistent course.

**Functional/developmental outcome:** Growth and neurodevelopment are reported as normal in most followed patients (e.g., siblings followed to ages 12.5 and 4.5 years with normal growth/development despite persistent hepatomegaly/lab abnormalities, [PMC12137118](https://pmc.ncbi.nlm.nih.gov/articles/PMC12137118/)), with growth failure/short stature as an exception in a minority (~22%).

---

## 12. Treatment

**Dietary/supportive (first-line):**
- **Low-fat diet with medium-chain triglyceride (MCT) enrichment** is the standard first-line management approach — one series recommends MCT comprising up to ~70% of fat intake ([PMC11743310](https://pmc.ncbi.nlm.nih.gov/articles/PMC11743310/)), based on the rationale that MCTs bypass the long-chain-fatty-acid/triglyceride-resynthesis pathway that is pathologically overactive in this disease.
- **Omega-3 fatty acid supplementation** has also been used as part of standard dietary management ([PMC12137118](https://pmc.ncbi.nlm.nih.gov/articles/PMC12137118/)).
- In many patients, **"no specific treatment is required"** and triglycerides/enzymes are managed with observation alone as they tend to improve with age (though see §11 on incomplete normalization).

**Pharmacotherapy:**
- **Fenofibrate** (a PPAR-α agonist, fibrate class) has been used successfully for severe, persistent hypertriglyceridemia refractory to diet, notably in a boy with cirrhosis and GPD1 deficiency: homozygous **c.895G>A (p.G299R)**, followed since age 1 for hepatomegaly/elevated LFTs/hypertriglyceridemia, biopsy-proven cirrhosis with micro/macrovesicular steatosis; fenofibrate started at age 15, with **successful triglyceride reduction over 1-year follow-up** (Matarazzo et al. 2020, *JIMD Reports*, PMID:32685347, [PMC7358666](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7358666/)). NCIT term candidate: NCIT:C61961 (Fenofibrate) as `therapeutic_agent` under a `NCIT:C15986` Pharmacotherapy `treatment_term`.
- **Allopurinol** has been used adjunctively for management of hyperuricemia in at least one reported case ([PMC11743310](https://pmc.ncbi.nlm.nih.gov/articles/PMC11743310/)).
- **Lipoprotein apheresis** is not routine but has been considered/mentioned for severe hyperlipidemia management in the broader monogenic-hypertriglyceridemia literature context (PMID:29940878 cited by [PMC12137118](https://pmc.ncbi.nlm.nih.gov/articles/PMC12137118/)), though a GPD1-deficiency-specific apheresis case was not directly retrieved in this search and should be verified before citing.

**Advanced therapeutics:** No gene therapy, cell therapy, RNA-based therapy (ASO/siRNA), or targeted molecular therapy has been developed or trialed for GPD1 deficiency — it remains managed purely with diet ± fibrate therapy. No relevant NCT-registered clinical trials were identified in this search.

**Surgical/interventional:** None specific to GPD1 deficiency identified; presumably standard cirrhosis-complication management (e.g., surveillance for hepatic adenoma/malignant transformation) would apply in advanced cases, but this is inferential rather than literature-documented.

**Monitoring:** Serial liver enzymes, triglycerides, abdominal ultrasound/elastography, and periodic biopsy consideration in persistent/progressive cases are implied by the follow-up structure of reported case series, though no formal consensus monitoring protocol/guideline was identified.

**Suggested NCIT terms:** NCIT:C15447 (Dietary Intervention) for the low-fat/MCT diet; NCIT:C15986 (Pharmacotherapy) with `therapeutic_agent` = fenofibrate (fibrate class; CHEBI or NCIT term to be confirmed via OAK lookup before binding).

---

## 13. Prevention

- **Primary prevention:** Not applicable in the traditional sense (monogenic recessive disease) beyond **genetic counseling** for carrier parents/consanguineous families, particularly in populations with known founder alleles (e.g., Israeli Arab c.361-1G>C).
- **Secondary prevention/early detection:** No population screening program (newborn or carrier) exists; early detection currently depends on clinical suspicion when a child presents with unexplained hepatomegaly/hypertriglyceridemia/fatty liver, triggering WES.
- **Carrier/prenatal testing:** Would be feasible via targeted variant testing once a familial pathogenic variant is known (standard for autosomal recessive Mendelian disease), but no specific prenatal diagnosis program was identified in the literature reviewed.
- **Behavioral/dietary prevention of complications:** Ongoing low-fat/MCT dietary management functions as tertiary prevention — limiting hepatic lipid accumulation/fibrosis progression rather than preventing disease onset.
- **Public health:** Not a public-health-scale condition given its rarity; management is individualized/genetic-counseling-based rather than population-level.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** No naturally occurring GPD1-deficiency disease model was identified in companion animals (dogs, cats) or wildlife in this search (no OMIA entry surfaced). This should be double-checked directly against OMIA before asserting absence in the KB.
- **Orthologous gene:** Mouse *Gpd1* (MGI:95679), located syntenically; the mouse ortholog has been characterized functionally (see Model Organisms below).
- **Comparative biology:** The dual cytosolic (GPD1)/mitochondrial (GPD2) glycerol-3-phosphate shuttle system is evolutionarily conserved from yeast to humans — the crystal structure of yeast (*Saccharomyces cerevisiae*) Gpd1 has been solved (PMC3515364), providing structural insight into the conserved catalytic fold, though yeast Gpd1 serves an osmotic-stress-response role distinct from the mammalian lipogenic/metabolic role.
- **Zoonotic potential:** Not applicable (non-infectious monogenic disease).

---

## 15. Model Organisms

**Mouse (*Mus musculus*, MGI:95679, orthologous gene *Gpd1*):**
- A **spontaneous loss-of-function mutant mouse line** exists: homozygous mice are described as **"viable and phenotypically normal"** at baseline but show **complete loss of GPD1 enzymatic activity in adult tissues** ([MGI:95679](https://www.informatics.jax.org/marker/MGI:95679); IMPC data).
- **Fasting/metabolic phenotyping** (Tanner et al., PMID:27733253, "Glycerol-3-phosphate dehydrogenase 1 deficiency induces compensatory amino acid metabolism during fasting in mice"): Gpd1-knockout mice show:
  - Inhibited gluconeogenesis specifically from glycerol (expected, given the enzyme's role).
  - **Higher** blood glucose after 1–4 hours of fasting compared to wild-type — a counterintuitive compensatory finding.
  - Significantly **higher blood alanine** and increased hepatic utilization of alanine for gluconeogenesis.
  - Interpretation: chronic GPD1 deficiency induces an adaptive shift toward glycogenic-amino-acid-driven gluconeogenesis, compensating for the lost glycerol-to-glucose route.
- **Fidelity/limitations as a model for the human liver disease:** Notably, the mouse model as characterized in the retrieved literature is centered on **fasting glucose/amino acid metabolism**, not on the hallmark human phenotype (hepatomegaly, hepatic steatosis, fibrosis, hypertriglyceridemia). This is an important **model-to-mechanism gap**: no clear evidence was retrieved in this search that the Gpd1-knockout mouse recapitulates hepatic steatosis/fibrosis/hypertriglyceridemia the way human patients do (the baseline phenotype is described as "phenotypically normal"). This divergence should be flagged explicitly in any `animal_models[].modeled_mechanisms` entry — likely `PARTIAL_RECAPITULATES` or `FAILS_TO_RECAPITULATE` for the hepatic/lipid phenotype specifically, pending a literature check for a fat-loading/high-fat-diet-challenged version of this model, which was not identified in this search but may exist and should be checked before finalizing model-fidelity calls.
- **Alcohol-related fatty liver context:** A separate mouse study examines "the role of glycerol-3-phosphate dehydrogenase 1 in the progression of fatty liver after acute ethanol administration in mice" (ScienceDirect, PMID not retrieved directly) — relevant to GPD1's general role in hepatic lipid handling but in an ethanol-injury context rather than a direct constitutive-deficiency human-disease model; should be checked for direct relevance/fidelity before citing as a disease model.

**Yeast (*Saccharomyces cerevisiae*):** Gpd1 structural biology (PDB structure solved at 2.45 Å, PMC3515364) provides conserved catalytic-domain insight but yeast Gpd1's physiological role (osmoadaptation via glycerol production) is not a disease model for the human hepatic phenotype — useful for structural/functional annotation only, not phenotype recapitulation.

**Other species (zebrafish, Drosophila, C. elegans, iPSC/organoid models):** None identified in this search; this is a gap worth a dedicated follow-up search before concluding no such model exists.

---

## Summary of Key PMIDs / Identifiers for Curation

| Reference | Content |
|---|---|
| Basel-Vanagaite et al. 2012, *Am J Hum Genet* 90:49–60 | Original description, c.361-1G>C, 10 patients/4 families, molecular mechanism hypothesis |
| PMID:27368975 | "Expanding the molecular diversity and phenotypic spectrum of GPD1 deficiency" — could not confirm full-text details in this session (CAPTCHA-blocked); re-fetch before citing specifics |
| PMID:32685347 / PMC7358666 | Matarazzo et al. 2020, fenofibrate therapy, c.895G>A/p.G299R, cirrhosis case |
| PMID:35365473 / PMC8977762 | First reported hepatic adenoma in HTGTI |
| PMID:36588760 / PMC9801319 | Hypoglycemia + insulin resistance, c.805C>T/p.R269W |
| PMID:28944580 | Obesity, insulin resistance, fatty liver, short stature, Chinese cohort |
| PMID:33120465 | Two cases + literature review (Chinese) |
| PMC11743310 (2024) | 5 North India cases + review of 36 global cases — primary source for frequency statistics used above |
| PMC12137118 / [Nature s10038-025-01339-9] (2025) | "GPD1 deficiency—a rare, overlooked cause of liver disease" — 45 cases/18 studies review |
| PMID:42063230 (2026) | Das et al., "Transient Disease or a Great Masquerader?" commentary |
| PMID:27733253 | Mouse Gpd1-KO fasting/amino-acid compensation study |
| OMIM *138420 / #614480 | Gene / phenotype entries |
| ORPHA:300293 | Orphanet entry |

## Notable gaps to close before KB entry finalization
1. **PMID for the original 2012 paper** and for PMID:27368975 could not be directly confirmed via full-text fetch in this session (access blocked); re-verify via PubMed/`just fetch-reference`.
2. **MONDO:0013771** binding should be confirmed via OAK/`just validate-terms` rather than taken from the template at face value.
3. **gnomAD allele/carrier frequencies** for the specific pathogenic variants (c.361-1G>C, p.G299R, p.R269W, etc.) need direct per-variant lookup.
4. **Mouse model hepatic/lipid phenotype fidelity** (vs. the baseline "phenotypically normal" finding) needs a dedicated search for any high-fat-diet-challenged or liver-specific-phenotyping Gpd1-KO study before writing an `animal_models` entry.
5. Confirm whether a fenofibrate/fibrate CHEBI or NCIT identifier and a `GPD1` HGNC lowercase CURIE (`hgnc:4455`) resolve correctly in the local caches before binding.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 7 |
| Quoted claims checked | 0 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 0 |
| Quoted claims with nothing to check against | 4 |
| References weighed for topical relevance | 11 |
| On topic | 7 |
| Off topic | 0 |

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `PMID:42063230`: "A Transient Disease or a Great Masquerader?"
  - Reference resolved but exposes no abstract or full text to search
- `DOI:10.1002/ajmg.a.70188`: "A Transient Disease or a Great Masquerader?"
  - Reference resolved but exposes no abstract or full text to search
- `PMC:PMC12137118`: "typically peak within the first 6 months of life, tending to decrease with age"
  - The PMC ID service was unreachable, so the quote was not checked
- `PMC:PMC12137118`: "contribute[s] independently to the risk of coronary artery disease and [is] additionally associated with heightened susceptibility to acute pancreatitis"
  - The PMC ID service was unreachable, so the quote was not checked

11 of 18 references resolved; the rest could not be looked up either way.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 36 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 4 |
| Terms whose name was checked | 15 |
| Terms named correctly | 10 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `GENO:0000148` (1 mention) - the report calls it "biallelic homozygous"; GENO calls it **autosomal recessive inheritance**
- `UBERON:0000178` (1 mention) - the report calls it "blood, for triglyceride measurement"; UBERON calls it **blood**
- `NCIT:C15709` (1 mention) - the report calls it "Liver Biopsy"; NCIT calls it **Genetic Testing**
- `NCIT:C61961` (1 mention) - the report calls it "Fenofibrate"; NCIT calls it **Tacrine**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0004367` (GO_0004367) (1 mention) - replaced by `GO:0047952`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GENO:0000135` (1 mention) - the report calls it "compound heterozygous"; GENO calls it **heterozygous**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MGI:95679` - called "Gpd1", "Orthologous gene:** Mouse *Gpd1"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `ORPHA`, `MGI`.