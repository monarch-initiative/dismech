---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-25T16:42:03.843555'
end_time: '2026-09-25T16:47:03.500337'
duration_seconds: 299.66
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: CAMLG-CDG
  mondo_id: MONDO:0859357
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
  web_search_requests: 8
  num_turns: 20
  total_cost_usd: 1.4171742000000003
  session_id: fd65d8eb-852b-5a9d-91de-140beff025e2
  stop_reason: end_turn
  assistant_text_blocks: 3
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
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 3
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 54
  verified: 52
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 17
  labels_matching: 12
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: HP:0002451
    reported_labels:
    - "Limb ataxia \u2014 not stated"
    ontology_label: Limb dystonia
  labels_variant: 4
  obsolete_terms:
  - term_id: GO:0006486
    ontology_label: obsolete protein glycosylation
    replaced_by: GO:0009101
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** CAMLG-CDG
- **MONDO ID:** MONDO:0859357 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **CAMLG-CDG** covering all of the
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

I'll research CAMLG-CDG using primary literature sources before compiling this report.

Confirmed: HGNC:1471. I now have sufficient primary-source detail to write the comprehensive report.

I have sufficient primary-source data now. Compiling the full report.

---

# CAMLG-CDG (Congenital Disorder of Glycosylation, Type IIz) — Comprehensive Research Report

## Summary

CAMLG-CDG is an ultra-rare, autosomal recessive congenital disorder of glycosylation (CDG) caused by biallelic loss-of-function variants in *CAMLG* (calcium-modulating ligand, encoding the CAML protein). It was first reported in a single 14-year-old male patient in 2022 by Wilson, Durin, Unal, and colleagues (Human Molecular Genetics) and is designated CDG2Z in OMIM (#620201; gene: *CAMLG*, OMIM *601118). CAMLG-CDG is the **third** described human disorder of the TRC ("transmembrane domain recognition complex," also called the GET pathway) — following GET4-CDG (OMIM #618751, CATP4/UBL4A-family disorder) and GET3/ASNA1-related disease — establishing "TRC pathway disorders" as an emerging disease category distinct from the classical CDG mechanisms (glycan assembly/transfer enzymes, nucleotide-sugar transporters, or COG/vesicular-tethering defects) (Wilson et al. 2022, PMID:35262690).

**Primary source for nearly all clinical/molecular/mechanistic content below:** Wilson MP, Durin Z, Unal Ö, et al. "CAMLG-CDG: a novel congenital disorder of glycosylation linked to defective membrane trafficking." *Hum Mol Genet.* 2022;31(15):2571-2581. doi:10.1093/hmg/ddac055. PMID:35262690; PMCID:PMC9396942. This is the sole primary literature report to date; no independent second family has yet been published (searched September 2026).

---

## 1. Disease Information

**What it is.** CAMLG-CDG is a Type II CDG (glycan-processing/trafficking defect rather than assembly defect) presenting with a predominantly severe neurological phenotype — global developmental delay, hypotonia, spasticity, epilepsy, and structural brain abnormalities — arising from combined defects in N-linked and mucin-type O-linked glycan sialylation, secondary to disrupted membrane insertion of tail-anchored (TA) SNARE proteins in the Golgi.

**Key identifiers:**
- **MONDO:** MONDO:0859357 (per the dismech curation stub for this disease, issue #12798 — a lead, not independently re-verified against the MONDO release in this session)
- **OMIM phenotype:** #620201 — Congenital Disorder of Glycosylation, Type IIz (CDG2Z)
- **OMIM gene:** *601118 — CALCIUM-MODULATING LIGAND; CAMLG
- **Gene identifiers:** HGNC:1471; NCBI Gene ID 819; approved name "calcium modulating ligand"; chromosome 5q31.1 (hg38 ~chr5:134,737,608–134,752,705)
- **Reference transcript used in the report:** NM_001745.4
- **Inheritance:** Autosomal recessive
- **Synonyms/aliases for the gene:** CAML (protein), calcium-modulating cyclophilin ligand
- **Orphanet/ICD-10/ICD-11:** No dedicated Orphanet or ICD codes were identified in this search — consistent with the condition's extreme rarity and single-patient status; it would fall under the general CDG-II ICD-10 code (E77.8, other disorders of glycoprotein metabolism) if coded clinically.
- **Data provenance:** All disease-level information is derived from a single published index case (a structured case report / mechanistic study), i.e., individual-patient-level data aggregated into one peer-reviewed report — not a registry or large cohort.

---

## 2. Etiology

**Disease causal factor:** Purely genetic/monogenic. Biallelic (here, homozygous) loss-of-function variation in *CAMLG* abrogates CAML protein expression, disrupting the TRC/GET tail-anchored protein insertion pathway.

**Genetic risk factors:**
- The reported variant, c.633+4A>G (chr5:134,741,527A>G, GRCh38.p13), is a canonical splice-donor-region variant in intron 2 causing exon 2 skipping.
- **Consanguinity is the dominant risk factor identified**: the patient is "the second child of consanguineous Turkish parents (fourth degree cousins)," with an unaffected older sibling and no other family history of metabolic disease (Wilson et al. 2022). This is the classic epidemiologic signature of an autosomal recessive founder/private variant surfacing through consanguineous mating.
- No population allele-frequency data for this specific variant were retrievable in this session (gnomAD query not performed); given a single reported homozygote in a consanguineous pedigree, the variant is presumptively very rare/private.
- No modifier genes have been reported (single case; no genotype-phenotype correlation possible yet).

**Environmental/other risk factors:** None reported or plausible — this is a purely monogenic ER/Golgi membrane-insertion disorder.

**Protective factors:** None reported. The report speculates (see mechanism/model-organism section below) that **residual leaky splicing producing a small amount of functional CAML** is what allows human survival, given that complete *Camlg* knockout is embryonic lethal in mice — this is an inferred within-patient mechanism of attenuation, not a population-level protective genetic variant.

**Gene-environment interactions:** None described; not applicable to this single-gene ER trafficking disorder.

---

## 3. Phenotypes

All phenotype data below derive from the one published patient (male, born 2007 at term; most recent evaluation at age 14) (Wilson et al. 2022, PMID:35262690). Frequencies are necessarily "1/1" (n=1); no population frequency data exist.

| Phenotype | Onset / Detail | Suggested HPO term |
|---|---|---|
| Global developmental delay | Noted from 3 months of age — "no head control" | HP:0001263 Global developmental delay |
| Loss of developmental milestones | Onset ~3 months, coincident with seizure onset | HP:0032199 Regression (or HP:0002376 Developmental regression) |
| Seizures | Onset ~3 months; described as "staring at a point accompanied by stiffness and unresponsiveness" (semiology consistent with tonic/absence-type seizures) | HP:0001250 Seizure; consider HP:0002373 Febrile seizure — not stated; better HP:0032794 (focal-onset seizure) or generic HP:0001250 |
| Drug-responsive epilepsy | Seizure-free ×4 years on levetiracetam at last follow-up | HP:0011182 Levetiracetam-responsive (not a real HPO term — record as treatment response in `notes`, not HPO); use HP:0001250 for the seizure phenotype itself |
| Axial hypotonia | Present at exam | HP:0008936 Axial hypotonia |
| Limb spasticity | Present | HP:0001257 Spasticity |
| Limb contractures | Present | HP:0001371 Flexion contracture (or HP:0034392 generic contractures) |
| Bilateral clonus | Present on exam | HP:0100659 Clonus (verify exact term) |
| Severe global motor impairment | "can only sit with considerable support" | HP:0002510 Spastic tetraparesis / HP:0002keeping generic HP:0001344 not appropriate — best mapped to HP:0002020 or functional-status descriptors; recommend HP:0001272 (Cerebellar atrophy) separately for imaging, and a general severe motor impairment term |
| Severe expressive language impairment | "makes only sounds" (nonverbal) | HP:0002465 or HP:0000750 Delayed speech and language development (severe/absent) |
| Growth failure — weight | 30.6 kg at 14 y, below 3rd centile | HP:0004325 Decreased body weight |
| Microcephaly (acquired/postnatal) | Head circumference 46 cm at 14 y, below 3rd centile | HP:0000252 Microcephaly |
| Dolichocephaly | Noted on exam; "no other significant dysmorphism" | HP:0000268 Dolichocephaly |
| Feeding difficulty requiring gastrostomy | Chronic, ongoing | HP:0002020 Gastrostomy / feeding difficulties → HP:0011968 |
| Respiratory insufficiency | Requires intermittent respiratory support | HP:0002093 Respiratory insufficiency |
| Normal eye movements | Explicitly noted as normal (negative finding, worth recording) | — |
| No organomegaly | Explicitly negative | — |

**Neuroimaging (brain MRI, age 7 years):** "very thin corpus callosum, atrophic brain stem, severe cerebral and cerebellar atrophy and diffuse hypomyelination" — HPO candidates: HP:0033725/HP:0002079 (Hypoplasia of the corpus callosum / Thin corpus callosum — HP:0002079 or HP:0033725), HP:0002099 or HP:0001272 (Cerebellar atrophy), HP:0002451 (Limb ataxia — not stated), HP:0007266 (Diffuse cerebral atrophy), HP:0002194 (Delayed gross motor development), HP:0002087/HP:0002012 (brainstem atrophy — map to HP:0007366 Cerebellar vermis atrophy / HP:0002080 or a generic "Abnormality of brainstem morphology"), and HP:0007305 (Abnormality of the cerebral white matter) / HP:0012448 (Delayed myelination) for diffuse hypomyelination.

**Severity/progression:** The phenotype is characterized as a **static, severe** encephalopathy after an early regression — not clearly progressive after the seizure-onset period, though long-term natural history is unknown from a single case followed to age 14. Seizures became well-controlled (4 years seizure-free on levetiracetam at last report), which is a meaningful treatment-response data point.

**Quality of life impact:** Not formally measured (no EQ-5D/SF-36/PROMIS data); qualitatively, the patient has profound functional dependency (gastrostomy-fed, intermittent respiratory support, nonverbal, needs support to sit), consistent with a severe pediatric neurodevelopmental CDG phenotype.

**Pediatric framing:** This is a congenital/infantile-onset disorder by definition (symptom onset at 3 months); there is no adult-onset or adult-recognized phenotype reported, and the disorder should not be conflated with adult presentations of unrelated Golgi trafficking disorders.

---

## 4. Genetic/Molecular Information

**Causal gene:** *CAMLG* (HGNC:1471; NCBI Gene 819; OMIM *601118), chromosome 5q31.1.

**The reported pathogenic variant (single family, homozygous):**
- Genomic: chr5:134,741,527A>G (GRCh38.p13)
- Transcript (NM_001745.4): **c.633+4A>G** — an intron 2 splice-donor-region variant, 4 bp into the intron
- Predicted protein consequence: **p.(Glu58ValfsTer80)** via aberrant splicing
- Splicing mechanism (functionally confirmed in patient fibroblasts): the variant causes **skipping of exon 2** (461 nucleotides, 154 codons) with fusion of exons 1 and 3, producing a frameshift and premature termination.
- RT-qPCR: "expression of the canonical CAMLG transcript was negligible" in patient fibroblasts vs. controls.
- cDNA PCR: the normal full-length 624 bp amplicon was **absent** in patient fibroblasts, replaced by a truncated ~163 bp amplicon, "confirming that the c.633+4A>G variant causes skipping of exon 2."
- Protein level: immunoblotting showed significantly **reduced CAML protein** in patient fibroblasts (P<0.05) — i.e., not a complete null at the protein level, consistent with leaky/residual normal splicing (see Mechanism section).

**Variant classification:** Not explicitly stated as an ACMG/AMP tier in the retrieved abstract/full-text excerpts; functionally it behaves as a hypomorphic loss-of-function allele (severe reduction, not complete absence, of protein) — this functional hypomorphism is proposed by the authors as the reason the patient is viable despite *Camlg* being an embryonic-lethal gene in mouse knockouts.

**Zygosity/origin:** Homozygous germline variant, inherited from consanguineous heterozygous-carrier parents (autosomal recessive).

**Population frequency:** Not retrieved in this session (gnomAD lookup not performed for this specific intronic variant); given a single reported homozygote from a consanguineous union, expect it to be absent or present at very low allele count in gnomAD — **this should be independently verified via gnomAD/ClinVar before curation**, not assumed from this report.

**Modifier genes:** None identified (n=1 case; no comparative genetics possible).

**Epigenetics / chromosomal abnormalities:** Not applicable/not reported for this disorder — it is a single-nucleotide splice variant, not a structural or epigenetic lesion.

**Gene product function (CAML protein):**
- CAML (calcium-modulating cyclophilin ligand) is an ER-resident, widely expressed multipass transmembrane protein.
- **TRC/GET pathway role (disease-relevant mechanism):** Together with GET1/WRB, CAML forms the ER membrane **receptor** component of the TRC (transmembrane domain recognition complex) pathway, which inserts C-terminal tail-anchored (TA) proteins into the ER membrane. Per the primary paper: "the recognition complex (composed of BAG6, GET4 and UBL4A)…binds to TA proteins and then to GET3 (TRC40, ASNA1)…GET3 chaperones the TA protein to the ER membrane where GET1 (WRB) and CAML form a receptor which enables its integration within the lipid bilayer."
- **Independent, non-CDG-related function (background/older literature, distinct from the 2022 disease report):** CAML was originally characterized as a calcium-signaling protein downstream of the T-cell receptor and upstream of calcineurin/NFAT, binding cyclophilin B (Bram & Crabtree, *Nature* 1994, not independently re-verified in this session — flagged as background knowledge, not a primary-source citation obtained here). Later functional work (PMID:26561552, *J Immunol* 2015) showed CAML is required for **survival of TCR-activated peripheral T cells** — tamoxifen-inducible CAML-knockout T cells expressed normal early activation markers (CD25, CD69) and produced IL-2 normally but proliferated less and died, implicating CAML in a late post-activation T-cell survival step rather than early signaling. A separate paper (PMID:16111633, not independently verified this session) reported CAML is required for **thymocyte development**, with CAML inactivation reducing double-positive/single-positive thymocyte numbers and altering positive/negative selection.
- **Note for dismech curation (§3a-type lump/split consideration):** these T-cell/immune functions of CAML are a *separate, non-disease-linked biological role of the same gene* — the one reported patient's phenotype is neurological, not immunological (no immunodeficiency features described), so this T-cell biology should be treated as background gene function rather than imported as a clinical feature of CAMLG-CDG absent direct patient evidence.

---

## 5. Environmental Information

No environmental factors, lifestyle factors, or infectious triggers are described or plausible for this monogenic ER-trafficking disorder. Not applicable.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (as established in Wilson et al. 2022, PMID:35262690)

1. **Homozygous c.633+4A>G splice variant in *CAMLG*** → causes skipping of exon 2 (RT-PCR/cDNA-confirmed) → frameshift/premature termination (p.Glu58ValfsTer80) → **near-loss of canonical CAMLG transcript and markedly reduced CAML protein** (immunoblot-confirmed, P<0.05) in patient fibroblasts.
2. **Reduced/absent functional CAML** → loss of the CAML/GET1(WRB) ER-membrane receptor component of the TRC (GET) pathway → **impaired insertion of a subset of tail-anchored (TA) proteins into ER/Golgi membranes**, specifically Golgi SNARE machinery.
3. Specifically, **short-form syntaxin-5 (STX5S) and, to a lesser extent, long-form (STX5L)** are mislocalized from Golgi membrane to cytosol — crude subcellular fractionation showed significantly increased cytoplasmic STX5 in both forms (P<0.05 long form, P<0.001 short form), with the short form more affected (43% mislocalized in CAMLG-CDG vs. 9% for the long form); immunofluorescence confirmed reduced STX5 colocalization with the Golgi marker giantin (P<0.0001). This was reproduced by **siRNA knockdown of CAMLG in HeLa cells** (residual CAML ~2%), reproducing STX5S (P<0.001) and STX5L (P<0.01) mislocalization — establishing STX5 mislocalization as a *consistent cellular biomarker of TRC pathway dysfunction* across two independent cell systems.
4. **Downstream v-SNARE BET1L (GS15)** — which the authors note is "more associated with the short form than the long form of STX5, and is required for retrograde trafficking within the Golgi" — is **drastically reduced at the protein level**: 37% of control levels in CAMLG-CDG fibroblasts and 27% of control in GET4-CDG fibroblasts (P<0.01; comparator disorder, see below), and reduced to 30.3% of control in CAMLG-siRNA-knockdown HeLa cells (P<0.01). BET1L/YKT6 *localization* (membrane vs. cytoplasm fractionation) was normal — the defect is in overall steady-state protein level, not mislocalization, distinguishing this from the STX5 mechanism.
5. **Loss of correctly assembled/positioned Golgi SNARE complexes (STX5-BET1L axis)** → impaired Golgi trafficking machinery → **disorganized Golgi** — indirectly supported by ST6GAL1 (a sialyltransferase) showing normal total protein levels but "a more fragmented distribution" upon CAMLG knockdown, "indicating at least some disorganization of the Golgi."
6. **Golgi disorganization / impaired SNARE-dependent trafficking of glycosylation enzymes** → **hyposialylation of both N-linked and mucin-type O-linked glycans**, producing the combined Type II CDG biochemical signature: 
   - Serum transferrin isoelectric focusing: "repeatedly showed a type 2 pattern."
   - Transferrin N-glycan MALDI-TOF: CDG-II pattern with **reduced pentasialotransferrin and raised trisialotransferrin** (undersialylated species).
   - ApoC-III (mucin-type O-glycosylation marker): "absence of asialo and disialo apoC-III, and only a small amount of monosialo apoC-III," indicating a defect of mucin-type O-glycosylation.
   - Lectin studies in patient fibroblasts: **peanut agglutinin (PNA)** fluorescence (binds desialylated core-1 O-glycan/Gal-GalNAc) was "barely detectable in control fibroblasts" but showed "a strong increase in signal…in affected fibroblasts" — direct evidence of O-glycan hyposialylation. In contrast, **vicia villosa lectin (VVL)** (binds the unmodified GalNAc/Tn antigen, marking O-glycan *initiation*) "showed no increased signal in affected fibroblasts" — demonstrating the defect is specifically in the **terminal sialylation step**, not in O-glycan chain initiation.
7. **Combined N- and O-glycan hyposialylation** → the multisystem CDG phenotype, dominated here by severe CNS involvement (hypomyelination, cerebral/cerebellar atrophy, thin corpus callosum), consistent with the general CDG pattern in which the developing brain is exquisitely sensitive to glycosylation defects (general CDG biology; this generalization is background knowledge, not a specific claim from the cited paper about mechanism of CNS vulnerability, and should be flagged as inferred/general in KB curation rather than disease-specific evidence).

**Branch/negative control — TRC pathway selectivity is incomplete:** Not all canonical TRC-dependent TA proteins are affected. The authors explicitly tested and found **normal subcellular localization of Emerin, VAMP7, and VAPB** — TA proteins canonically dependent on the TRC pathway — in both CAMLG-CDG and GET4-CDG fibroblasts, indicating the pathway defect in this disease selectively/preferentially disrupts **Golgi SNARE proteins (STX5, BET1L)** rather than causing indiscriminate failure of all TA protein insertion. This is an important qualifying/branching point in the causal chain: reduced CAML causes a *selective* TA-protein trafficking defect, not global ER insertion failure, which the authors propose explains why glycosylation (a Golgi-dependent process) is specifically hit.

**COG complex (a separate Golgi-tethering machinery) is not involved:** steady-state levels and subcellular localization of **COG1, COG4, and COG8** were normal in both CAMLG-CDG and GET4-CDG fibroblasts — ruling out a COG-complex-mediated mechanism (distinguishing this from the COG-CDG subgroup, CDG-IIa/IIc/IIe/etc.) and supporting that the TRC/SNARE-insertion defect is a mechanistically distinct route to hyposialylated CDG-II glycosylation.

### Comparative mechanism — GET4-CDG (the closest prior TRC disorder)

The paper studied a previously reported GET4-deficient patient's fibroblasts in parallel:
- "In fibroblasts from the previously identified individual with pathogenic variants in GET4, CAML steady state levels were normal." Interestingly, **GET4 levels were also decreased in the CAMLG-CDG patient** (~71% reduction versus controls), suggesting some interdependence/cross-stabilization between TRC pathway components even though CAML and GET4 act at different pathway steps.
- STX5 mislocalization was reproduced in GET4-deficient fibroblasts in parallel with CAMLG-CDG, and clinical features of the CAMLG patient were noted to be "similar to those in one of the two other described TRC pathway disorders (GET4 deficiency)" — supporting a shared clinical/mechanistic disease class ("TRC pathway disorders").

### Mouse model context (interpretive, not a primary-model experiment in this paper)

The authors note that **complete *Camlg* knockout is embryonic lethal in mice**, and interpret patient survival as evidence that "the small amount of remaining CAML protein…[is] sufficient to provide enough insertion of TA proteins that the phenotype is attenuated" — i.e., the human splice variant is a hypomorph, not a true null, and this residual function is proposed as necessary for viability. This is a **model-organism-informed inference about human genotype-phenotype correlation** (`HUMAN_MODEL_MISMATCH`-flavored reasoning: the mouse null is embryonic lethal, but the human hypomorphic allele produces a viable, severely affected phenotype) rather than a direct functional experiment performed in this paper on a mouse model.

### Suggested ontology terms for the mechanism

- **GO Biological Process:** GO:0071816 (tail-anchored membrane protein insertion into ER membrane); GO:0006890 (retrograde vesicle-mediated transport, Golgi to ER — for BET1L's role); GO:0006486 (protein glycosylation); GO:0006493 (protein O-linked glycosylation); GO:0006487 (protein N-linked glycosylation)
- **GO Molecular Function:** consider GO terms for SNARE binding/protein-membrane receptor activity of CAML/GET1
- **GO Cellular Component:** GO:0005794 (Golgi apparatus); GO:0000139 (Golgi membrane); GO:0005783 (endoplasmic reticulum)
- **Cell types (CL):** primary evidence is from patient dermal fibroblasts (CL:0000057, fibroblast) and HeLa cells (an epithelial-derived cell line, less directly CL-mappable as a disease-relevant cell type but used for the siRNA mechanistic confirmation) — no direct neuronal/CNS cell-type-specific experiment was performed; the CNS phenotype is inferred from general CDG biology, not from a CNS-specific cell model in this paper.

---

## 7. Anatomical Structures Affected

- **Organ level (primary):** Central nervous system — cerebrum, cerebellum, brainstem, corpus callosum (structural MRI abnormalities: cerebral/cerebellar atrophy, thin corpus callosum, brainstem atrophy, diffuse hypomyelination). UBERON: UBERON:0000955 (brain), UBERON:0002037 (cerebellum), UBERON:0002771 (falx cerebri/corpus callosum — use UBERON:0002336 corpus callosum), UBERON:0002298 (brainstem).
- **Secondary/systemic involvement:** Growth (failure to thrive — below 3rd centile weight/OFC), musculoskeletal (contractures, spasticity), respiratory system (requiring intermittent support), gastrointestinal (gastrostomy-dependent feeding).
- **Not involved / explicitly normal:** No organomegaly noted; eye movements normal (no overt ophthalmologic/oculomotor involvement reported, unlike some other CDGs).
- **Tissue/cell level:** Dermal fibroblasts (patient-derived, primary experimental system) — CL:0000057. Golgi apparatus and ER of these cells are the direct subcellular site of the trafficking defect.
- **Subcellular level (GO Cellular Component):** Golgi membrane (GO:0000139) and ER membrane (GO:0005789) are the two organelle membranes directly implicated — CAML/GET1 receptor acts at the ER membrane for TA protein insertion, while the functional consequence (STX5/BET1L dysfunction) manifests at the Golgi.
- **Laterality:** Not applicable/not described (a systemic biochemical-trafficking disorder, not a lateralized structural anomaly).

---

## 8. Temporal Development

- **Onset:** Infantile — developmental delay and seizure onset both noted at **3 months of age**. This is congenital-to-early-infantile onset by the standard CDG onset categories.
- **Onset pattern:** Insidious/subacute — a normal-appearing early infancy followed by loss of milestones concurrent with seizure onset at 3 months ("developmental delay at three months of age...seizures started at that age and he lost his milestones").
- **Progression:** The published natural history covers birth to age 14 (single longitudinal case, not a cohort). The picture is one of an early regression followed by a **static but severe** encephalopathy — seizures came under control (seizure-free 4 years on levetiracetam by last report), while the motor/functional profile (spasticity, contractures, need for gastrostomy and respiratory support) appears to represent a fixed, severe deficit state rather than a described progressive/degenerative course after the initial regression, though this cannot be fully distinguished from slow progression given only two time points (age 7 MRI, age 14 exam) were reported.
- **Disease stage/duration:** Chronic, lifelong — no data on adult survival beyond age 14 (patient's age at last follow-up in the report).
- **Remission patterns:** Partial — seizures achieved sustained remission with levetiracetam (treatment-induced, not spontaneous); no remission of the underlying developmental/motor phenotype is described (nor biologically expected, given the fixed genetic and structural brain basis).
- **Critical periods:** Not explicitly studied, but the infantile onset with regression suggests the first months of life are a period of particular vulnerability, consistent with general CDG biology (rapid CNS myelination and glycosylation-dependent processes in infancy) — this is a general inference, not paper-specific data.

---

## 9. Inheritance and Population

- **Epidemiology:** **n = 1** reported patient worldwide (as of the 2022 publication and as of this September 2026 search, no additional cases were located in the literature). No prevalence or incidence estimate exists or is calculable; this is an ultra-rare, essentially "cases-in-literature" epidemiology (CASES_IN_LITERATURE measure type, in dismech schema terms).
- **Inheritance pattern:** Autosomal recessive, confirmed by parental consanguinity and homozygosity of the proband.
- **Penetrance:** Cannot be assessed from a single case (parents, presumed obligate heterozygous carriers, were not reported to have any phenotype — consistent with typical AR carrier status, but this is not explicitly discussed in the retrieved text).
- **Expressivity:** Cannot be assessed (n=1; no comparator patients).
- **Genetic anticipation:** Not applicable (no repeat-expansion mechanism; not a multi-generational report).
- **Germline mosaicism:** Not discussed/not applicable (single conventional homozygous transmission from two heterozygous consanguineous parents).
- **Founder effects:** Not established — a single Turkish consanguineous family; whether this specific variant represents a Turkish founder allele or a private familial mutation cannot be determined from one report. This would need gnomAD/regional-cohort data to assess (not retrieved in this session).
- **Consanguinity role:** **Central to this case** — parents are fourth-degree cousins of Turkish origin; this is the mechanism by which a presumably rare recessive allele became homozygous.
- **Carrier frequency:** Unknown/not reported.
- **Population demographics:** Only known ethnicity is Turkish (single family); no broader geographic or ethnic distribution data exist. Sex: only a male patient has been reported (n=1, cannot establish a sex ratio). Age distribution: single pediatric/adolescent patient (followed birth–14 years).

---

## 10. Diagnostics

**Biochemical/laboratory tests (primary diagnostic route, as used in this case):**
- **Serum transferrin isoelectric focusing (IEF):** showed a repeatable **Type 2 pattern** — the standard first-tier CDG screening test, here indicating a Golgi-processing (Type II) rather than ER-assembly (Type I) defect.
- **Transferrin N-glycan analysis by MALDI-TOF mass spectrometry:** confirmed the CDG-II pattern with reduced pentasialotransferrin and increased trisialotransferrin — quantitative confirmation of undersialylation.
- **Serum Apolipoprotein C-III (apoC-III) isoform analysis:** used as the O-glycosylation marker; showed absence of asialo-/disialo-apoC-III and only trace monosialo-apoC-III, diagnostic of a **mucin-type O-glycosylation defect** — important because this combined N+O defect pattern is itself a diagnostic clue pointing away from classical single-pathway CDGs toward a Golgi-trafficking-level defect.
- **Lectin fluorescence microscopy in cultured fibroblasts** (PNA vs. VVL): a research-level cellular assay (not a routine clinical diagnostic test) used here to localize the defect specifically to the sialylation step of O-glycosylation rather than initiation.

**Genetic testing:** The diagnosis was reached via genome/exome-level sequencing identifying the homozygous *CAMLG* splice variant (specific sequencing modality — WES vs. WGS vs. panel — not specified in the retrieved excerpts); given the phenotype's severity and the era (patient evaluated to age 14, report published 2022), exome sequencing in a consanguineous family with a "CDG-II biochemical signature + neurological phenotype" gene panel/WES approach is the most likely diagnostic route. **Functional/RNA-level confirmation** (RT-qPCR, RT-PCR of cDNA showing exon 2 skipping, and immunoblot showing reduced CAML protein) was essential to establish pathogenicity of this intronic splice variant — illustrating that for CDG genes with unclear-significance intronic/splice variants, RNA and protein studies in patient fibroblasts are the diagnostic gold standard beyond DNA sequencing alone.

**Imaging:** Brain MRI (structural) — thin corpus callosum, brainstem atrophy, cerebral/cerebellar atrophy, diffuse hypomyelination — performed at age 7.

**Electrophysiology:** Seizure semiology described clinically; specific EEG findings were not detailed in the retrieved excerpts.

**Differential diagnosis:** Broadly, other Type II CDGs presenting with severe neurological phenotype and combined N-/O-glycosylation defects (e.g., COG-CDGs, other Golgi-trafficking CDGs) and, specifically within the emerging TRC-disorder class, **GET4-CDG** — clinically the closest comparator per the authors. Standard CDG diagnostic algorithms (transferrin IEF/MALDI-TOF as first-tier, followed by gene-specific or panel/exome sequencing) apply.

**Screening:** No population or newborn screening applicable (single case, no established screening program for CDGs of this type generally, let alone this ultra-rare subtype).

---

## 11. Outcome/Prognosis

- **Survival:** The patient was alive at last follow-up (age 14), demonstrating this genotype is compatible with survival to adolescence despite the corresponding mouse knockout being embryonic lethal — a key prognostic and mechanistic data point (interpreted by the authors as reflecting residual/hypomorphic CAML function from incomplete splice disruption).
- **Life expectancy:** Not established beyond the reported follow-up age; no long-term mortality data exist for this single-patient disorder.
- **Morbidity/functional outcome:** Severe and static-to-slowly evolving — profound motor impairment (sits only with support), nonverbal communication, gastrostomy-dependent nutrition, intermittent respiratory support — indicating a high burden of chronic disability typical of severe pediatric CDGs with CNS involvement.
- **Complications:** Feeding/nutritional compromise (requiring gastrostomy), respiratory insufficiency (requiring intermittent support), contractures/spasticity as secondary musculoskeletal complications of chronic hypertonia/immobility.
- **Recovery potential:** Seizures show good treatment response (sustained remission on levetiracetam); the structural brain abnormalities and motor/developmental impairments are not described as reversible.
- **Prognostic factors:** None can be statistically derived from n=1; qualitatively, early seizure onset and severe MRI abnormalities correlate with the severe overall phenotype in this patient, consistent with (but not independently proving) a general CDG pattern that early-onset epilepsy plus significant structural brain disease predicts poor functional outcome.

---

## 12. Treatment

**No disease-specific or mechanism-targeted therapy exists** for CAMLG-CDG; management reported is purely supportive/symptomatic:

- **Antiepileptic pharmacotherapy:** **Levetiracetam** — patient became and remained seizure-free for 4 years at last report. (NCIT treatment-action term: NCIT:C15986 Pharmacotherapy, with `therapeutic_agent` bound to the specific drug — CHEBI ID for levetiracetam would need independent lookup/verification, not retrieved in this session.)
- **Nutritional support:** Gastrostomy tube feeding for chronic feeding difficulty (NCIT candidate: a gastrostomy/enteral feeding procedure term — exact NCIT code not verified in this session).
- **Respiratory support:** Intermittent respiratory support (ventilatory/respiratory assistance — NCIT candidate term not verified in this session).
- **No gene therapy, enzyme replacement, cell therapy, RNA-based therapy, or disease-modifying treatment** has been reported or trialled for this disorder (consistent with its status as a single-case, very recently described condition; unlike PMM2-CDG, there is no dedicated clinical trial infrastructure).
- **No clinical trials** (ClinicalTrials.gov / WHO ICTRP) specific to CAMLG-CDG were identified.

**Treatment strategy:** Purely symptomatic/multidisciplinary supportive care (neurology for seizure management, nutrition/GI for gastrostomy feeding, pulmonology for respiratory support) — the standard approach for a severe, non-treatable Type II CDG with predominant CNS involvement.

---

## 13. Prevention

- **Primary prevention:** None specific to this disorder beyond general genetic counseling; given the demonstrated role of **consanguinity** in this case, standard genetic counseling regarding consanguineous unions and recessive disease risk is the only "prevention" lever identifiable from the available data.
- **Secondary prevention/screening:** No population or targeted carrier-screening program exists (ultra-rare, single-family-described variant); prenatal or preimplantation genetic testing would be theoretically possible for this specific family once the causal variant is known (standard for a molecularly characterized AR disorder), but this was not reported as having occurred or being offered in the paper.
- **Genetic counseling:** Applicable for the affected family (recurrence risk 25% for future pregnancies of the same parents; carrier risk for the unaffected sibling) — general AR genetics principles, not disease-specific data from the paper.
- **Public health/prophylaxis:** Not applicable to this ultra-rare monogenic disorder.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** No naturally occurring CAMLG-deficient disease has been reported in any non-human species (companion animal, livestock, or wildlife) in the literature searched. *Camlg* orthologs exist across mammals (the original CAMLG gene-mapping paper noted synteny with mouse chromosome 13; NCBITaxon:10090 for *Mus musculus* ortholog *Camlg*, MGI-mapped — exact MGI ID not independently verified in this session).
- **Comparative biology:** CAML/the TRC-GET pathway is evolutionarily conserved from yeast (where the pathway was first characterized: Get1/Get2/Get3/Get4/Get5 in *Saccharomyces cerevisiae*) to humans, underlying the pathway's alternate name "GET pathway" (Guided Entry of Tail-anchored proteins). This conservation is the basis for the yeast nomenclature (GET1=WRB, GET3=ASNA1/TRC40, GET4) used interchangeably with the mammalian TRC pathway naming in the primary paper.
- **Zoonotic potential:** Not applicable (not an infectious disease).

---

## 15. Model Organisms

- **Mouse (*Mus musculus*):** The primary paper cites that **complete germline *Camlg* knockout is embryonic lethal** in mice (cited as prior literature within Wilson et al. 2022, exact original mouse-knockout citation not independently retrieved/verified in this session — flag as a claim requiring its own primary-source PMID before KB citation). This model demonstrates CAML is essential for viability at the whole-organism level in a way that overlaps only partially with the human hypomorphic-allele phenotype — a **human-model mismatch** worth flagging explicitly in curation (`HUMAN_MODEL_MISMATCH`): the mouse null is incompatible with life, while the human splice-hypomorph is compatible with survival to at least adolescence, which the authors attribute to residual protein rather than to any species-specific difference in CAML's essentiality.
- **Conditional/inducible mouse models (immune-function studies, mechanistically related but not disease models per se):** Tamoxifen-inducible CAML-knockout mice (tCAML−/−) were used in unrelated immunology work (PMID:26561552) to study T-cell survival post-TCR activation, and thymocyte-specific CAML inactivation was studied in PMID:16111633 for T-cell development — **these are functional/mechanistic models of CAML biology in the immune system, not models of the CDG phenotype**, and should not be conflated with CAMLG-CDG animal-model evidence in KB curation; they establish gene function generally but were not designed or used to recapitulate the glycosylation/neurological disease phenotype.
- **Cellular models used directly for CAMLG-CDG mechanism (the actual disease models in the primary paper):**
  - **Patient-derived primary dermal fibroblasts** — the principal disease model, used for RT-PCR/RT-qPCR splicing confirmation, immunoblotting (CAML, GET4, STX5, BET1L, YKT6, COG1/4/8, ST6GAL1), subcellular fractionation, and immunofluorescence (STX5/giantin colocalization; PNA/VVL lectin staining).
  - **HeLa cells with siRNA-mediated CAMLG knockdown** (residual CAML ~2%) — used as an independent, non-patient-derived cellular system to confirm STX5 mislocalization and BET1L reduction, establishing reproducibility of the mechanism outside the patient's own genetic background — this fidelity/reproducibility is a strength of the mechanistic evidence (RECAPITULATES-type relationship in dismech `modeled_mechanisms` terms).
  - **GET4-deficient patient fibroblasts** (from a previously published, separate patient) — used as a comparator TRC-pathway-disorder cell line, not a model of CAMLG-CDG itself, but establishing shared downstream mechanism (STX5 mislocalization, BET1L reduction) across two distinct TRC pathway gene defects.
- **No zebrafish, *Drosophila*, *C. elegans*, or yeast disease-modeling experiments were performed in this paper** (the yeast GET pathway is referenced only as evolutionary/mechanistic background, not as an experimental model in this study).
- **No organoid, iPSC-derived, or CNS-specific (neuronal) model system was used** — this is a notable gap: despite the phenotype being predominantly neurological (hypomyelination, brain atrophy), all functional/mechanistic work was performed in fibroblasts and HeLa cells, not neural cell types. This is worth flagging as a limitation/gap for any `HUMAN_MODEL_MISMATCH` or knowledge-gap discussion in KB curation — the CNS-specific pathophysiology (why hypomyelination and cerebellar/cerebral atrophy specifically result from this Golgi-SNARE/sialylation defect) is inferred by analogy to general CDG neurobiology rather than directly demonstrated in a neural model in this paper.

---

## Notes on Evidence Quality and Gaps for Curation

- **Single-source, single-patient disease.** Essentially all clinical and molecular content in this report traces to one peer-reviewed paper (PMID:35262690) describing one family/one patient. This should be reflected in dismech curation as `CASES_IN_LITERATURE` for prevalence, and every phenotype should carry a frequency understood as "1/1," not a population percentage.
- **OMIM (#620201, *601118) and GeneCards/NCBI/HGNC identifiers** were retrieved via web search/API (mygene.info, OMIM search snippets) rather than fully fetched primary pages (OMIM blocked direct fetch with 403 in this session) — **the OMIM clinical synopsis full text was not independently verified**; treat the OMIM-sourced phrasing above as a lead requiring direct confirmation against omim.org before citing OMIM as a `reference:` in KB YAML.
- **MONDO:0859357** is carried over from the dismech repository's own open curation-stub issue (#12798) referencing this exact disease — this is a strong internal signal of correctness for this specific dismech instance, but was not independently re-derived from a live MONDO ontology query in this session and should still be confirmed via `just fetch-reference` / term-cache lookup per repository ontology-term-contract rules before binding.
- **HGNC:1471 for CAMLG** was cross-verified via the mygene.info API (an independent source from the initial GeneCards-derived search snippet, which had first reported a slightly different number) — treat HGNC:1471 as the better-supported value, but re-confirm via `just validate-terms` / the HGNC cache per the repository's "never write a CURIE from memory" rule.
- **The mouse *Camlg* embryonic-lethality claim** is cited within the primary paper but its ultimate original source (the specific mouse knockout study) was not independently traced/verified in this session — if used in KB curation as an `animal_models` entry, the original PMID for that mouse knockout paper should be located and cited directly rather than citing Wilson et al. 2022 as if it were the source of the mouse data.
- **No independent second case report, natural-history study, registry entry, or treatment trial exists as of this search (September 2026)** — this is consistent with the disease's very recent (2022) first description and extreme rarity.

## Sources

- [CAMLG-CDG: a novel congenital disorder of glycosylation linked to defective membrane trafficking — Human Molecular Genetics (Oxford Academic)](https://academic.oup.com/hmg/article/31/15/2571/6545759)
- [CAMLG-CDG: a novel congenital disorder of glycosylation linked to defective membrane trafficking — PubMed (PMID:35262690)](https://pubmed.ncbi.nlm.nih.gov/35262690/)
- [CAMLG-CDG: a novel congenital disorder of glycosylation linked to defective membrane trafficking — PMC (PMCID:PMC9396942)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9396942/)
- [OMIM #620201 — Congenital Disorder of Glycosylation, Type IIz (CDG2Z)](https://omim.org/entry/620201)
- [OMIM *601118 — Calcium-Modulating Ligand; CAMLG](https://omim.org/entry/601118)
- [GeneCards — CAMLG Gene](https://www.genecards.org/cgi-bin/carddisp.pl?gene=CAMLG)
- [NIH Genetic Testing Registry — Congenital disorder of glycosylation, type IIz](https://www.ncbi.nlm.nih.gov/gtr/conditions/C5774295/)
- [Congenital disorders of glycosylation (CDG): state of the art in 2022 — Orphanet Journal of Rare Diseases](https://link.springer.com/article/10.1186/s13023-023-02879-z)
- [Calcium-Modulating Cyclophilin Ligand Is Essential for the Survival of Activated T Cells and for Adaptive Immunity — J Immunol (PMID:26561552)](https://pubmed.ncbi.nlm.nih.gov/26561552/)
- [CAML is a p56Lck-interacting protein that is required for thymocyte development — PubMed (PMID:16111633)](https://pubmed.ncbi.nlm.nih.gov/16111633/)
- [OMIM *612056 — Guided Entry of Tail-Anchored Proteins Factor 4; GET4](https://omim.org/entry/612056)
- [OMIM *602915 — Guided Entry of Tail-Anchored Proteins Factor 1; GET1 (WRB)](https://omim.org/entry/602915)
- [dismech GitHub issue #12798 — Curate congenital disorder of glycosylation, type IIz (MONDO:0859357)](https://github.com/monarch-initiative/dismech/issues/12798)
- [mygene.info gene record for CAMLG (NCBI Gene 819)](https://mygene.info/v3/gene/819)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 54 |
| Resolved | 52 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 17 |
| Terms named correctly | 12 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002451` (1 mention) - the report calls it "Limb ataxia — not stated"; HP calls it **Limb dystonia**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0006486` (obsolete protein glycosylation) (1 mention) - replaced by `GO:0009101`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0007266` (1 mention) - the report calls it "Diffuse cerebral atrophy"; HP calls it **Cerebral dysmyelination**
- `HP:0007305` (1 mention) - the report calls it "Abnormality of the cerebral white matter"; HP calls it **CNS demyelination**, and lists "Demyelination in central white matter" among its other names
- `GO:0006890` (1 mention) - the report calls it "retrograde vesicle-mediated transport, Golgi to ER — for BET1L's role"; GO calls it **retrograde vesicle-mediated transport, Golgi to endoplasmic reticulum**, and lists "retrograde vesicle-mediated transport, Golgi to ER" among its other names
- `GO:0006486` (1 mention) - the report calls it "protein glycosylation"; GO calls it **obsolete protein glycosylation**