---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-25T16:30:49.666897'
end_time: '2026-09-25T16:38:23.824639'
duration_seconds: 454.16
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Peroxisome Biogenesis Disorder 6B
  mondo_id: MONDO:0013937
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
  web_search_requests: 29
  num_turns: 57
  total_cost_usd: 2.5024171999999996
  session_id: fd65d8eb-852b-5a9d-91de-140beff025e2
  stop_reason: end_turn
  assistant_text_blocks: 5
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
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 12
  on_topic: 7
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 40
  verified: 39
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 25
  labels_matching: 19
  labels_variant: 6
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Peroxisome Biogenesis Disorder 6B
- **MONDO ID:** MONDO:0013937 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Peroxisome Biogenesis Disorder 6B** covering all of the
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

I'll research Peroxisome Biogenesis Disorder 6B (PEX26-related Zellweger spectrum disorder) across primary literature, OMIM, Orphanet, GeneReviews, and related databases.

The search snippets conflicted on which gene causes PBD-6B — I need to verify directly against OMIM and MONDO rather than trust contradictory summaries.

Confirmed: PBD-6B (MONDO:0013937, OMIM 614871) is caused by **PEX10**, not PEX26 — PBD6A (614870, severe/Zellweger) and PBD6B (614871, milder NALD/IRD) are the two PEX10-linked phenotypes, complementation group 7. Let me now research PEX10 thoroughly.

PubMed/NCBI are captcha-blocked for WebFetch. Let me try Europe PMC, which mirrors abstracts without the captcha wall.

# Research Report: Peroxisome Biogenesis Disorder 6B (PBD6B)

## Critical correction before starting

The template's target GeneCards/identifier assumption needs correcting up front. **PBD6B (OMIM #614871, MONDO:0013937, MedGen C3553948, Orphanet 44 — grouped under "Zellweger syndrome spectrum") is caused by biallelic pathogenic variants in *PEX10*** (OMIM *602859, HGNC:8851, NCBI Gene 5192, 1p36.32) — **not** *PEX26*. *PEX26* causes a different complementation group (CG8; PBD7A/OMIM 615872 and PBD7B/OMIM 614873). I confirmed this by cross-checking OMIM's own gene-phenotype table (via search snippets naming 614871 → PEX10, 602859) against MONDO's identifier mapping for MONDO:0013937, which independently returned OMIM 614871 and Orphanet 44 with PEX10 as the causal gene. First-pass web search results genuinely conflated the two genes (both are peroxins causing overlapping Zellweger-spectrum phenotypes), so I flag this explicitly rather than silently picking one. **Everything below concerns PEX10, complementation group 7 (US nomenclature) / group B (Japanese nomenclature).**

A note on evidence density: PEX10 accounts for a minority of Zellweger spectrum disorder (ZSD) cases (PEX1 ~60–65%, PEX6 ~14.5%, with PEX1/PEX6/PEX10/PEX12/PEX26 together >90% of cases) — I could not find a search result giving an exact PEX10-specific percentage, so I report the surrounding figures rather than fabricate one. Consequently, much of the phenotype/management literature is written for ZSD as a whole (dominated by PEX1 patients) rather than PEX10/PBD6B specifically. I mark ZSD-wide generalizations versus PEX10-specific case reports throughout — this distinction matters for a pediatric/genetics-trained reader deciding how much weight a given claim deserves.

---

## 1. Disease Information

**Overview.** PBD6B is the milder of two PEX10-linked phenotypes on the Zellweger spectrum: PBD6A (OMIM 614870) is the severe, classically lethal Zellweger syndrome; PBD6B (OMIM 614871) is the intermediate/mild end, corresponding clinically to neonatal adrenoleukodystrophy (NALD) or infantile Refsum disease (IRD)-type presentations, with an extreme mild outlier phenotype of isolated cerebellar ataxia now described.

**Identifiers:**
- OMIM phenotype: 614871 (PBD6B); sibling severe phenotype 614870 (PBD6A)
- OMIM gene: *602859 (PEX10)
- MONDO: MONDO:0013937
- MedGen: C3553948
- Orphanet: 44 (Zellweger syndrome spectrum — umbrella code; I did not find a PBD6B-specific Orphanet code distinct from this ZSD-spectrum entry)
- HGNC: 8851 (PEX10); NCBI Gene: 5192
- Locus: 1p36.32
- ICD-10-CM: E71.510 (Zellweger syndrome) is the billable code found; there is no PEX10/PBD6B-specific ICD-10 code — ZSD as a whole maps to E71.5-series codes (E71.541 "Zellweger-like syndrome" also exists but that is a distinct entity, not a synonym)

**Synonyms:** Peroxisome biogenesis disorder, complementation group 7, mild form; Zellweger spectrum disorder, PEX10-related, attenuated form; historically "complementation group B" (Japanese fibroblast-fusion nomenclature) vs. "complementation group 7" (US nomenclature) — both refer to the same PEX10 defect (confirmed via Okumoto et al. 1998, PMID:9700193, and Warren et al. 1998, PMID:9683594).

**Data derivation:** The clinical picture below is derived from aggregated disease-level resources (OMIM, case series, review articles) rather than a single large natural-history cohort specific to PEX10 — PBD6B is documented almost entirely through individual case reports and small family series (Blomqvist et al. 2017, PMID:28784167; Huang et al. 2025, PMID:40267090; Nava et al. 2022, PMID:35038753), supplemented by ZSD-wide reviews that are PEX1-dominated.

---

## 2. Etiology

**Disease causal factor:** Exclusively genetic — biallelic (homozygous or compound heterozygous) loss-of-function or hypomorphic pathogenic variants in *PEX10*. No environmental, infectious, or purely mechanistic (non-genetic) causal factor has been reported for this entry; I found nothing in the literature search suggesting otherwise.

**Genetic risk factors and genotype-phenotype correlation.** This is the most substantively documented part of PEX10 biology and is worth stating precisely because it is the mechanistic basis for the PBD6A/PBD6B split:

- Warren, Wolfe & Gould (2000, *Human Mutation*, PMID:10862081) established the founding genotype-phenotype correlation: **nonsense, frameshift, and splice-site mutations correlate with severe Zellweger syndrome (PBD6A)**, whereas **missense mutations retaining partial function** — the reported example is a mutation in the C-terminal zinc-binding RING domain (H290Q) — **associate with milder NALD-type disease (PBD6B)**. Notably, the same paper also found some nonsense/frameshift mutations truncating only the C-terminal 1/3–2/3 of the protein retained "nearly normal PEX10 activity" in a complementation assay, underscoring that truncation location, not variant class alone, predicts residual function.
- Subsequent PBD6B-specific missense variants reported: c.530T>G (p.Leu177Arg), homozygous, in an attenuated/late-onset case (Blomqvist et al. 2017, PMID:28784167); a novel splice-acceptor variant c.113-2A>G causing in-frame exon 2 skipping, compound heterozygous with c.890T>C (p.Leu297Pro), in a Han-Chinese family with three affected members classified as PBD6B (Huang et al. 2025, PMID:40267090).
- A structurally distinct **extreme-mild outlier phenotype — isolated, later-onset (age 3–8 years) cerebellar ataxia with cerebellar atrophy, without the classic multisystem ZSD picture** — has been described in at least 15 patients across 9 families with biallelic PEX10 variants (Nava et al. 2022, PMID:35038753). This is a genotype-phenotype extreme worth flagging separately from "classic" PBD6B/NALD-IRD, since it changes the differential diagnosis (unexplained pediatric/young-adult ataxia) rather than presenting as a recognizable ZSD gestalt.

**Modifier genes:** None specific to PEX10/PBD6B identified in this search. The general ZSD literature (Klouwer et al. 2015, PMID:26627182) notes only that "although a rough genotype-phenotype correlation exists for several PEX genes, such as PEX1 and PEX26, the severity and progression of the disease is difficult to predict for individual patients" — implying unidentified modifying factors even within an allele class.

**Environmental/lifestyle risk or protective factors, gene-environment interaction:** None identified. This is a purely Mendelian biochemical disorder; I found no CTD, epidemiological, or GWAS-type literature suggesting environmental modulation of PEX10-related disease risk or severity.

**Consanguinity/founder context:** Several PBD6B case reports come from consanguineous or genetically isolated families (Han-Chinese family, PMID:40267090; an Assyrian/Iraqi-origin patient, PMID:28784167), consistent with autosomal recessive inheritance generally, but I found no evidence of a defined *PEX10* founder allele or population-specific carrier frequency estimate — a Dagestan-family PEX26 report and a Saudi PEX19/PEX26 report turned up in search but concern different genes and should not be conflated with PEX10/PBD6B.

---

## 3. Phenotypes

Phenotype data below draws on two evidence tiers that should not be blended uncritically: (A) ZSD-wide severity-tiered descriptions from Klouwer et al. 2015 (PMID:26627182) and the Bose et al. 2022 severity meta-analysis (PMID:35741019, *Cells*, analyzing 307 patients from 107 studies plus 136 chart-reviewed patients), which are PEX1-dominated; and (B) PEX10/PBD6B-specific case reports, which are the more directly applicable source for this entry but numerically sparse.

**Severe end (PBD6A, for contrast — this entry is PBD6B but the spectrum framing matters clinically):**
- Onset: neonatal
- Hepatic dysfunction, profound hypotonia, prolonged jaundice, feeding difficulties, seizures, characteristic craniofacial dysmorphism, retinopathy/cataracts/glaucoma, sensorineural deafness
- Brain MRI: neocortical dysplasia (especially perisylvian polymicrogyria — a neuronal migration defect), generalized white matter volume reduction, delayed myelination
- Prognosis: "survival is usually not beyond the first year of life" (Klouwer et al. 2015)

**PBD6B — intermediate/childhood tier (NALD-like):**
- Onset: infancy/childhood, delayed developmental milestones as a presenting feature
- Ocular: retinitis pigmentosa, cataract, glaucoma, "often leading to early blindness" (Klouwer et al. 2015)
- Auditory: sensorineural deafness "almost always present"
- Hepatic: hepatomegaly and dysfunction, coagulopathy, elevated transaminases, history of hyperbilirubinemia
- Neurologic: some patients develop early-onset progressive leukodystrophy with loss of acquired skills
- Prognosis: "most patients die before adolescence" for this tier as a class, though individual course varies

**PBD6B — milder/adolescent-adult tier (IRD-like), the tier best documented specifically for PEX10:**
- Diagnosis can occur in late childhood or adulthood
- "Ocular abnormalities and a sensorineural hearing deficit are the most consistent symptoms" (Klouwer et al. 2015)
- Primary adrenal insufficiency, "probably underdiagnosed"
- Clinical course "usually slowly progressive, although the disease may remain stable for (many) years"
- **PEX10-specific worked case** (Blomqvist et al. 2017, PMID:28784167): an adolescent girl presenting first with sensorineural hearing impairment (age 5), followed in the teen years by sensorimotor polyneuropathy, cognitive delay, impaired gross/fine motor skills, tremor, and muscle weakness — a trajectory the authors explicitly frame as atypically mild for the gene, underscoring the need for peroxisomal screening even without classic Zellweger gestalt.
- **PEX10-specific outlier phenotype** (Nava et al. 2022, PMID:35038753): isolated cerebellar ataxia, onset age 3–8, cerebellar atrophy on MRI in most cases (ataxia was the presenting symptom in 11/14 literature patients), with polyneuropathy and cognitive impairment in roughly two-thirds. The authors recommend metabolic screening (phytanic acid, VLCFA *ratios* rather than absolute VLCFA levels, which can be misleadingly near-normal in this mild phenotype) for unexplained pediatric ataxia.
- **Han-Chinese family** (Huang et al. 2025, PMID:40267090): three affected relatives with "milder phenotypes," described as "neurological dysfunction, hypotonia, seizures, and various systemic abnormalities" — classified PBD6B.

**Severity meta-analysis findings (ZSD-wide, PMID:35741019):** seizures, hypotonia, reduced mobility, feeding difficulties, renal cysts, adrenal insufficiency, and hearing/vision loss significantly correlated with severity classification; plasma C26:0 fatty acid levels also differentiated severity tiers.

**Quality of life:** I found no disease-specific EQ-5D/SF-36/PROMIS data for PBD6B or PEX10-related disease. The Bose group has run a caregiver-reported cross-sectional symptom-prevalence survey for ZSD generally (referenced in search results but not fetched in detail here); a dedicated per-phenotype QoL dataset for the PEX10 subgroup specifically was not located.

**Suggested HPO terms (leads only — not verified via OAK/HPO lookup in this session; treat as candidates to check before curation):** HP:0001518 (Small for gestational age is not relevant — omit), HP:0001250 (Seizure), HP:0001252 (Hypotonia), HP:0000505 (Visual impairment), HP:0000510 (Retinitis pigmentosa jointly relevant), HP:0000407 (Sensorineural hearing impairment), HP:0001392 (Abnormality of the liver / hepatomegaly-adjacent), HP:0002240 (Hepatomegaly), HP:0000794 (Nephropathy is too broad — renal cortical cysts is HP:0000107), HP:0007281 (Adrenal hypoplasia is not accurate — primary adrenal insufficiency is HP:0000846), HP:0001510-adjacent developmental delay terms, HP:0002066 (Gait ataxia) and HP:0001272 (Cerebellar atrophy) for the ataxia-outlier phenotype, HP:0000965/HP:0007270-type peripheral neuropathy terms. **All of these must be re-verified against the current HPO build before use — I am not treating this list as curated.**

---

## 4. Genetic/Molecular Information

**Causal gene:** *PEX10* (OMIM *602859, HGNC:8851, NCBI Gene 5192), chr1:2,403,964–2,413,797 (1p36.32). Encodes a 326-amino-acid peroxisomal membrane protein (Okumoto et al. 1998, PMID:9700193 describes a 326-aa protein; note Matsumoto/other sources for the related PEX26 gene describe a different, 305-aa protein — these are not interchangeable, reinforcing the gene-identity correction above).

**Protein structure and function:** PEX10 is a RING-type (C3HC4 zinc finger) E3 ubiquitin ligase embedded in the peroxisomal membrane. It is one of three RING-domain peroxins (PEX2, PEX10, PEX12) that co-assemble into the **PEX2-PEX10-PEX12 retrotranslocation channel**, whose cryo-EM structure was solved by Feng et al. 2022 (*Nature*, PMID:35768507): "the three subunits...coassemble in the membrane into a channel with an open 10 Å pore," with the RING zinc-fingers positioned on the cytosolic side to catalyze ubiquitination of the PTS1 import receptor PEX5 as it is extracted (retrotranslocated) from the peroxisomal lumen back to the cytosol. Under normal recycling, monoubiquitination (via the E2 enzyme PEX4) allows PEX5 reuse for another import cycle; when recycling is impaired, PEX10 (with PEX12 stimulating its ligase activity) instead polyubiquitinates PEX5, targeting it for proteasomal degradation.

**Pathogenic variant classes reported (PEX10, various complementation-group-7 phenotypes across the PBD6A/6B spectrum):**
- Homozygous 2-bp deletion, frameshift (Okumoto et al. 1998, PMID:9700193) — severe
- Homozygous splice donor-site mutation causing exon skipping vs. compound heterozygous missense + nonsense (two CG7 patients of differing severity; Warren et al. 1998, PMID:9683594)
- Missense H290Q in the C-terminal zinc-binding domain — milder NALD phenotype (Warren et al. 2000, PMID:10862081)
- c.530T>G (p.Leu177Arg), homozygous — attenuated/late-onset phenotype (Blomqvist et al. 2017, PMID:28784167)
- c.113-2A>G (splice acceptor, exon 2 skipping) compound heterozygous with c.890T>C (p.Leu297Pro) — PBD6B, three affected relatives (Huang et al. 2025, PMID:40267090)
- c.790C>T (p.Arg264X), a premature termination variant reported in ClinVar/gnomAD-linked material I surfaced via search but did not independently verify against a primary source — flagging this one specifically as **unverified for this report** (allele frequency cited as 2.5×10⁻⁵ in 237,538 control chromosomes in the search snippet; I could not confirm the originating publication, so treat this figure as a lead only).

**Variant classification:** ACMG/AMP pathogenic and likely pathogenic classifications exist in ClinVar for numerous PEX10 variants (multiple RCV accessions surfaced in search, e.g., c.790C>T/p.Arg264X, c.1A>G/p.Met1Val, c.711C>T) — I did not systematically enumerate ClinVar's full PEX10 variant table in this session; a dedicated ClinVar query would be needed before curation.

**Somatic vs. germline:** Exclusively germline — no somatic/oncologic role identified for PEX10 in this search (consistent with its being a housekeeping peroxisomal-import gene rather than a tumor-suppressor/oncogene axis).

**Functional consequence:** Loss of function (null alleles: nonsense, frameshift, canonical splice-site) → severe phenotype (PBD6A); partial loss of function (missense variants retaining residual retrotranslocation-channel activity) → PBD6B and its ataxia-only extreme. Mechanistically this is **loss-of-function/hypomorphic**, not gain-of-function or dominant-negative — consistent with recessive inheritance and with the direct biochemical demonstration (Warren et al. 1998) that CG7/PEX10-deficient cells "contain many peroxisomes and import peroxisomal membrane proteins but do not import peroxisomal matrix proteins," i.e., a selective matrix-import defect rather than failure of peroxisome formation per se.

**Epigenetic information:** None identified specific to PEX10/PBD6B.

**Chromosomal abnormalities:** None identified as an alternative disease mechanism for PBD6B (contrast: I found an unrelated case report of 1p36.33-p36.32 microdeletion causing pancytopenia, which is a different entity and should not be conflated with PEX10 point-variant disease, since the deletion region only partially overlaps the gene locus and was not reported as PBD6B).

---

## 5. Environmental Information

I found no evidence of environmental factors (toxins, radiation, occupational exposure), lifestyle factors, or infectious agents contributing causally to PBD6B. This is consistent with its being a monogenic autosomal recessive enzymopathy/traffic disorder with no known gene-environment interaction literature. This section is genuinely N/A rather than under-researched — the biology (loss of a specific ubiquitin-ligase/retrotranslocation-channel protein) gives no plausible mechanism for environmental modulation, and no CTD/epidemiological hits surfaced.

---

## 6. Mechanism / Pathophysiology

**Causal chain (numbered, from initiating lesion to clinical manifestation).** I want to flag explicitly that steps 1–3 are directly evidenced for PEX10 specifically (Warren et al. 1998, PMID:9683594; Feng et al. 2022, PMID:35768507), while steps 4 onward are **inferred by extension from general ZSD/peroxisomal pathophysiology** — largely characterized in PEX1-dominant cohorts and in generic peroxisomal-biochemistry literature — rather than demonstrated in PEX10-specific mechanistic studies. I have not found PEX10-specific tissue pathology, transcriptomic, or lipidomic studies; the downstream biology should be read as "expected by shared final-common-pathway logic," not as directly measured in PBD6B patients.

1. Biallelic pathogenic *PEX10* variants → reduced or absent functional PEX10 protein (RING-domain E3 ubiquitin ligase) at the peroxisomal membrane. [Direct — Okumoto 1998, Warren 1998]
2. Loss of PEX10 disrupts assembly/function of the **PEX2-PEX10-PEX12 retrotranslocation channel**, the structure responsible for extracting the ubiquitinated PTS1 receptor PEX5 from the peroxisomal membrane back to the cytosol for reuse. [Direct, structural — Feng et al. 2022, PMID:35768507]
3. Failure of PEX5 recycling (and, via PEX5L as PEX7's obligate co-receptor, secondary failure of PTS2-mediated import) leads to **selective failure of peroxisomal matrix protein import while the peroxisomal membrane and membrane-protein trafficking remain comparatively intact** — CG7/PEX10-deficient fibroblasts retain morphologically identifiable peroxisomes ("peroxisomal ghosts") that import membrane but not matrix proteins. [Direct — Warren 1998]
4. → Deficient peroxisomal matrix enzyme activities: beta-oxidation of very-long-chain fatty acids (VLCFA), alpha-oxidation of phytanic acid (with downstream pristanic acid accumulation), peroxisomal steps of bile acid synthesis (side-chain oxidation of DHCA/THCA to cholic/chenodeoxycholic acid), and the first two enzymatic steps of ether-phospholipid (plasmalogen) biosynthesis, plus glyoxylate detoxification. [Inferred by extension from general peroxisomal biochemistry — this is the same final common pathway across ZSD complementation groups, not PEX10-specific data]
5. → Biochemical signature: accumulation of VLCFA, phytanic/pristanic acid, and bile acid intermediates (DHCA, THCA) in plasma/urine, with **deficiency** of plasmalogens (erythrocyte membrane) and mature bile acids. This is the biochemical basis of the diagnostic panel described in Section 10.
6. Branch A — CNS/myelin: VLCFA accumulation incorporates into oligodendrocyte and neuronal membranes, and (by analogy with the better-studied ABCD1/X-ALD pathway) promotes oxidative stress and mitochondrial dysfunction; combined with plasmalogen deficiency (plasmalogens are a major myelin lipid component), this destabilizes myelin → leukodystrophy, and in the severe end of the spectrum disrupts neuronal migration during corticogenesis → neocortical dysplasia/polymicrogyria. [Inferred by extension — the myelin/oxidative-stress mechanism is best evidenced in X-ALD (ABCD1) literature, not PEX10-specific studies; polymicrogyria is a PBD6A-tier (severe) finding and less expected in PBD6B]
7. Branch B — sensory epithelia: plasmalogen deficiency and VLCFA accumulation are proposed to impair photoreceptor/retinal pigment epithelium membrane integrity (→ retinitis pigmentosa/cataract/glaucoma) and cochlear hair-cell function (→ sensorineural hearing loss) — the two most consistently reported PBD6B features. [Inferred/generalized; specific PEX10 cochlear or retinal histopathology was not located in this search]
8. Branch C — liver: failure of peroxisomal bile-acid-intermediate oxidation causes both accumulation of hepatotoxic intermediates (DHCA/THCA) and deficiency of mature bile acids needed for fat/fat-soluble-vitamin absorption → cholestasis, coagulopathy (secondary to vitamin K malabsorption), transaminase elevation, and in more severe cases progressive fibrosis/cirrhosis. [Klouwer et al. 2015 clinical description; general peroxisomal bile-acid biology]
9. Branch D — adrenal cortex: VLCFA/lipid accumulation in adrenocortical cells produces the "striated adrenocortical cell" histopathology described in classic Zellweger syndrome, with reduced steroid biosynthesis → primary adrenal insufficiency, reported in 7/24 ZSD patients (4 asymptomatic) in Berendse et al. 2014 (*Orphanet J Rare Dis*, PMID for this I located via search snippet as within volume 9/article 133, DOI 10.1186/s13023-014-0133-5 — PMID not independently confirmed in this session). [ZSD-wide, not PEX10-isolated data]
10. Branch E — kidney: renal cortical cysts (reported in ~70% of ZSD cases per search-derived summary; mechanism not detailed in sources retrieved — likely developmental, related to disrupted peroxisomal lipid metabolism during nephrogenesis, but I did not find a mechanistic paper specific to this).
11. Branch F — peripheral nerve/cerebellum (the PEX10-specific mild-end signature): the ataxia/polyneuropathy phenotype described by Nava et al. 2022 and Blomqvist et al. 2017 implies a disproportionate vulnerability of cerebellar and peripheral-nerve tissue to partial (hypomorphic) PEX10 loss relative to liver/adrenal/kidney — this pattern is **descriptive, not yet mechanistically explained** in the literature I retrieved; I would flag this as an open mechanistic question rather than assert a specific molecular explanation.

**Cell types implicated:** hepatocyte (liver), oligodendrocyte and cortical/cerebellar neuron (CNS), retinal photoreceptor/RPE (eye), cochlear hair cell (ear), adrenocortical cell (adrenal), renal tubular/cortical epithelium (kidney), Schwann cell/peripheral neuron (the ENU-mouse literature specifically notes "decreased Schwann cell number, defects at the neuromuscular junction," which maps suggestively onto the human polyneuropathy phenotype in mild PEX10 disease).

**Suggested GO terms (leads, unverified in this session):** GO:0007031 (peroxisome organization), GO:0016558 (protein import into peroxisome matrix), GO:0043574 (peroxisomal transport), GO:0006635 (fatty acid beta-oxidation), GO:0006693 (prostaglandin metabolic process — not directly relevant, omit), GO:0008306 (associative learning — not relevant, omit), a plasmalogen-biosynthesis term (GO:0001516 prostaglandin biosynthetic process is wrong; the correct term is likely GO:0090207 or a related ether-lipid biosynthesis GO ID that I have not verified — **do not bind without OAK lookup**), GO:0031625 (ubiquitin protein ligase binding) for PEX10's E3 activity. **These require verification before curation use.**

**Suggested CL/UBERON terms (leads, unverified):** CL:0000182 (hepatocyte), CL:0000128 (oligodendrocyte), CL:0000540 (neuron), CL:0000646/CL:0002586-type retinal photoreceptor terms, CL:0000499 (stromal cell — too generic, avoid), UBERON:0002107 (liver), UBERON:0000955 (brain), UBERON:0002369 (adrenal gland), UBERON:0002113 (kidney), UBERON:0001846-type cochlea/inner-ear term. **Verify all before binding.**

---

## 7. Anatomical Structures Affected

**Organ level (primary):** liver, central nervous system (cerebral white matter; cerebellum specifically in the PEX10 mild-outlier phenotype; cortex in severe polymicrogyria), eye (retina, lens, optic structures), ear (cochlea — sensorineural hearing loss), kidney (renal cortex — cysts), adrenal gland (cortex — primary insufficiency).

**Secondary/complication-level:** peripheral nervous system (polyneuropathy, prominent in the PEX10 mild phenotype specifically), skeletal system (enamel hypoplasia reported as "present in nearly all patients" per Klouwer et al. 2015; classic chondrodysplasia punctata/epiphyseal stippling is a **PEX7/RCDP1-defining** feature, not a PBD6B-typical one — I want to be explicit that this is a different gene and a different, non-overlapping disorder, even though both are peroxisomal).

**Body systems involved:** hepatic, neurologic (central and peripheral), ophthalmologic, otologic/auditory, renal, endocrine (adrenal), skeletal (dental enamel), hematologic (coagulopathy, secondary to fat-soluble vitamin malabsorption).

**Subcellular level:** peroxisomal membrane (site of PEX10 function and the retrotranslocation channel), peroxisomal matrix (site of the resulting import failure), secondarily mitochondria (oxidative stress/dysfunction is implicated by extension from X-ALD biology, not directly demonstrated for PEX10).

**Lateralization:** Not applicable — this is a systemic/bilateral biochemical disorder, not a laterality-associated condition.

---

## 8. Temporal Development

**Onset:** Highly variable across the PEX10 allelic series — this is the central organizing fact for PBD6B specifically. Null/severe biallelic combinations → neonatal-onset PBD6A (Zellweger syndrome proper, outside this entry's scope but relevant as the severe pole of the same gene). Hypomorphic missense combinations → PBD6B, itself spanning infantile (NALD-like) through late-childhood/adolescent (IRD-like) onset, down to an extreme late-onset (age 3–8) isolated-ataxia presentation (Nava et al. 2022).

**Onset pattern:** Generally insidious/subacute rather than acute, even in the mildest presentations — e.g., the Blomqvist 2017 case first came to attention via hearing loss at age 5, with polyneuropathy/cognitive/motor decline only becoming apparent through the teenage years.

**Progression:** "Usually slowly progressive, although the disease may remain stable for (many) years" at the mild end (Klouwer et al. 2015); when progression does occur in the mild/adult tier, it is "mainly related to peripheral neuropathy and pyramidal signs, while cognition remains stable" per the same source — an important prognostic nuance for counseling.

**Disease course pattern:** Progressive rather than relapsing-remitting; no spontaneous-remission pattern is described anywhere in the literature I retrieved.

**Critical periods:** Implicit rather than explicitly stated in the sources retrieved — the severe/neonatal tier's neocortical migration defects (polymicrogyria) imply a prenatal critical window, while the mild/PBD6B tier's slow, adult-persisting course suggests no comparable fixed developmental window, consistent with a milder biochemical lesion causing chronic accumulation/deficiency rather than a developmental catastrophe. I am reasoning past directly cited evidence here rather than quoting a specific source.

---

## 9. Inheritance and Population

**Inheritance pattern:** Autosomal recessive. Both PBD6A and PBD6B are allelic (same gene, different variant severity) — this is a point worth surfacing rather than treating them as unrelated diseases, per the dismech convention of keeping related-severity allelic disorders explicit rather than silently lumped or split.

**Epidemiology (ZSD-wide, not PEX10-isolated):**
- Cumulative ZSD incidence commonly cited around 1:50,000 births (Bose et al. 2022, PMID:35741019, cites this figure for context)
- US regional newborn-screening-derived estimate: ~1:90,000 (New York, from 1.08 million screenings, per a search-derived summary I could not independently verify against a primary citation this session)
- Japan: markedly lower, ~1:500,000 — a striking geographic disparity I found stated in search results but without a primary citation I directly fetched; treat as a lead pending verification
- **No PEX10/PBD6B-specific incidence figure was found** — given the rarity of published PEX10 cases (a handful of families across the literature I retrieved: Chinese, Assyrian/Iraqi, and the Nava et al. 9-family European/mixed ataxia cohort), PBD6B is almost certainly substantially rarer than the ZSD aggregate figure, but I have no quantitative basis to state a number.

**Penetrance/expressivity:** Functionally complete penetrance is implied (no asymptomatic biallelic carriers reported), but **expressivity is highly variable** — this is the genotype-phenotype axis already covered in Section 2 (severity tracks variant class/residual function) rather than a separate stochastic-penetrance phenomenon.

**Genetic anticipation, germline mosaicism, founder effects:** None reported for PEX10/PBD6B in this search.

**Consanguinity:** Several reported families are consanguineous or from genetically isolated populations, consistent with autosomal recessive disease generally, but no specific consanguinity-attributable-fraction statistic for PEX10 was found.

**Carrier frequency:** Not established with a verified primary source in this session (the one gnomAD-adjacent figure I surfaced, c.790C>T at AF 2.5×10⁻⁵, is flagged above as unverified).

**Population demographics, geographic distribution, sex ratio:** No PEX10-specific sex-ratio or ancestry-enrichment data found. Reported case geography spans China, Iraq (Assyrian ancestry), and mixed European cohorts for the ataxia phenotype — this reads as broad geographic distribution rather than a defined high-prevalence population, though the sparse case count makes any such inference weak.

---

## 10. Diagnostics

**Biochemical testing (plasma/blood, general ZSD panel — Klouwer et al. 2015, quoted directly):** "VLCFAs, the peroxisomal bile acid intermediates di- and trihydroxycholestanoic acid (DHCA, THCA), the branched-chain fatty acids phytanic and pristanic acid, and pipecolic acid in plasma, plasmalogen levels in erythrocytes, and C26:0-lysoPC in dried blood spots."

**Important caveat specific to mild PEX10 disease:** Klouwer et al. explicitly warn that "relatively mild ZSD patients may have (near) normal biochemical tests in plasma and urine" — and Nava et al. 2022 make the same point specifically for PEX10-related ataxia, recommending **VLCFA ratios rather than absolute VLCFA levels** and phytanic acid measurement as more sensitive in this attenuated phenotype. This is a clinically important point: a normal standard VLCFA panel does not exclude PBD6B.

**Urine testing:** Bile acids and oxalic acid.

**Fibroblast-based testing:** When clinical suspicion is high but blood/urine biochemistry is normal, culturing fibroblasts (including at 40°C, a temperature-sensitivity complementation approach historically used to unmask hypomorphic PEX1/PEX6 alleles, per Klouwer et al. 2015) is recommended — I did not find explicit confirmation that the 40°C assay specifically unmasks PEX10 hypomorphs, so I present this as a general ZSD-diagnostic-algorithm step rather than a PEX10-validated technique.

**Molecular/genetic testing:** Given PEX10's established role, single-gene sequencing, ZSD/peroxisomal gene panels, or exome sequencing are all reasonable approaches; multiple case reports used exome + Sanger confirmation (Huang et al. 2025) or targeted PEX gene screening panels ("The PEX Gene Screen," referenced in search results as a diagnostic approach paper, exact PMID not fetched in this session).

**Imaging:** Brain MRI for leukodystrophy/polymicrogyria/cerebellar atrophy (the latter specifically relevant to the PEX10 ataxia phenotype per Nava et al. 2022); renal ultrasound for cortical cysts; ophthalmologic exam (retinitis pigmentosa, cataract, glaucoma); audiology (sensorineural hearing loss).

**Differential diagnosis:** Other ZSD complementation groups (clinically indistinguishable without biochemical/molecular testing); for the isolated-ataxia PEX10 phenotype specifically, the differential is the broader autosomal-recessive-ataxia gene list (Nava et al. 2022 explicitly frame PEX10 as a diagnosis to consider in "unexplained autosomal recessive ataxias"); RCDP1 (PEX7) for any skeletal/rhizomelic features, which — again — should not be expected in PEX10-related disease specifically.

**Screening:** No dedicated newborn screening program for PBD/ZSD generally exists in most jurisdictions I found evidence for (X-linked ALD newborn screening via C26:0-lysoPC, now on the US RUSP since 2016, is a related but distinct screening target — it detects ABCD1-related disease, not PEX-gene ZSD, though the same analyte can incidentally flag peroxisomal biogenesis disorders). A "Spanish Uniform Newborn Screening Panel" reference surfaced in search results as potentially including peroxisomal markers, but I did not verify its exact scope in this session.

---

## 11. Outcome/Prognosis

Prognosis tracks tightly with the genotype-driven severity tier already discussed:

- **Severe/PBD6A pole (context only):** death typically within the first year of life.
- **PBD6B intermediate tier:** "most patients die before adolescence" as a class statement (Klouwer et al. 2015), though this generalization is drawn from ZSD-wide (PEX1-dominant) data, and PEX10-specific mortality figures for this tier were not located.
- **PBD6B mild tier:** patients "can reach adulthood without progression or with long periods of stabilization," with progression (when it occurs) dominated by peripheral neuropathy and pyramidal signs while cognition remains comparatively preserved (Klouwer et al. 2015). This matches the PEX10-specific case reports directly — the Blomqvist 2017 patient and the Nava 2022 ataxia cohort both describe adolescent/adult survival with a slowly accruing neurologic burden rather than early mortality.
- **Complications:** progressive liver disease, leukodystrophy (both flagged by Klouwer et al. as the drivers of a worse prognosis when they occur even in the milder tiers), primary adrenal insufficiency (treatable if detected), coagulopathy, hearing/vision loss, low bone mineral density (a "Reply: Low bone mineral density is a common feature of Zellweger spectrum disorders" letter surfaced in search — PMID not fetched, flagged as a lead).
- **No PEX10/PBD6B-specific survival curve, life-expectancy figure, or prognostic-biomarker study** was located in this search beyond the general ZSD severity-correlate list from Bose et al. 2022 (seizures, abnormal EEG, renal cysts, cardiac abnormalities, plasma C26:0 level).

---

## 12. Treatment

No curative therapy exists for PBD6B or ZSD generally — Klouwer et al. 2015 state this directly: "Because no curative therapy for patients with a ZSD exists, intervention is supportive and based on symptoms." Management is therefore organ-system-directed:

- **Pharmacotherapy — bile acid replacement:** Cholic acid (Cholbam®) received FDA approval (announced March 2015 per search-derived regulatory summaries) as the first approved treatment for bile acid synthesis disorders due to single-enzyme defects **and** "for adjunctive treatment of peroxisomal disorders such as Zellweger spectrum disorders in patients who have liver disease, steatorrhea, or complications from fat-soluble vitamin malabsorption." Approval was based on a long-term single-arm trial plus case reports across 77 bile-acid-synthesis-disorder patients and 34 peroxisomal-disorder patients; cholic acid appeared to decrease hepatic injury and increase height/weight, with 42% of treated peroxisomal-disorder patients surviving beyond 3 years in the trial population (search-derived; I did not independently verify this survival figure against the primary FDA review document, though the URL for that document was surfaced). Suggested NCIT term (lead, unverified): a Pharmacotherapy action term (NCIT:C15986) with `therapeutic_agent` CHEBI cholic acid.
- **DHA supplementation — tried and found ineffective for its primary endpoint:** A double-blind, randomized, placebo-controlled trial (search-derived citation as Neurology 2010, PMID likely in the PMC3013498/Paker et al. lineage — I did not fetch the primary abstract directly in this session) of DHA 100 mg/kg/day in 50 enrolled ZSD patients found **no significant improvement in visual function or growth** over 1 year, despite earlier open-label/MRI-myelination signal from Martinez-group studies. This is an important negative-trial data point for a "Treatment" section — DHA should not be presented as an established effective therapy without this caveat.
- **Adrenal insufficiency:** systematic Synacthen-test screening recommended for all ZSD patients (Klouwer et al. 2015; Berendse et al. 2014); cortisone/hydrocortisone replacement only for confirmed true insufficiency, given growth-suppression/osteoporosis risk from unnecessary supplementation.
- **Coagulopathy:** vitamin K supplementation.
- **Sensory support:** hearing aids/audiological follow-up and glasses/ophthalmologic follow-up, both recommended yearly.
- **Hyperoxaluria/renal stones:** oral citrate plus adequate fluid intake.
- **Nutrition:** gastrostomy where needed for caloric intake; phytanic-acid-restricted diet only when phytanic acid is markedly elevated (not for moderate elevation, where adequate caloric intake takes priority).
- **Dental care:** routine follow-up for enamel hypoplasia, "present in nearly all patients."
- **Rehabilitative:** physical/occupational/speech therapy implied by the overall supportive-care framework, though not itemized with PEX10-specific detail in the sources retrieved.
- **Experimental/advanced therapeutics:** No gene therapy, ASO, cell therapy, or targeted molecular therapy specific to PEX10/PBD6B was located in this search. Given the mechanism (loss of a membrane-embedded E3 ligase required for a multi-subunit channel), a small-molecule chaperone or gene-replacement approach is theoretically conceivable, but I found no clinical-trial evidence supporting this — absence of evidence here should be read as an actual gap, not an oversight.
- **Personalized/genotype-guided treatment:** Not established. The genotype-phenotype correlation (Section 2) has prognostic value but does not yet inform a differentiated treatment algorithm.

---

## 13. Prevention

**Primary/secondary/tertiary prevention:** No primary prevention exists (not environmentally caused). Secondary prevention is via early biochemical/molecular diagnosis to initiate supportive management (adrenal screening, vitamin K, sensory aids) before complications manifest — this is really the only "prevention" lever available and is why the diagnostic-delay problem in mild PBD6B (near-normal standard biochemistry per Section 10) matters clinically. Tertiary prevention is the organ-system surveillance program (yearly audiology/ophthalmology, adrenal screening, dental follow-up) described in Section 12.

**Immunization:** Not applicable — no disease-specific immunization strategy identified.

**Genetic screening:**
- Carrier screening in relatives of an affected proband, once the familial variant(s) are known, is standard practice for an AR condition, though I found no PEX10-specific carrier-screening panel data.
- Prenatal diagnosis: historically via VLCFA/peroxisomal biochemical assay on amniocytes or chorionic villus sampling; now more directly via molecular testing once familial variants are identified. I did not find a PEX10-specific prenatal-diagnosis case series in this search, though the general ZSD prenatal-testing approach should apply.
- Preimplantation genetic testing is plausible once familial variants are characterized, though no PEX10-specific PGT case report was located.

**Genetic counseling:** Standard AR recurrence-risk counseling (25% recurrence per pregnancy for carrier parents) applies; given the wide expressivity range within PBD6B itself (from NALD-like childhood disease to adult-onset isolated ataxia), counseling should explicitly address that a known familial genotype constrains but does not precisely predict phenotype severity — this is directly supported by the genotype-phenotype literature in Section 2, not merely a generic AR-counseling point.

**Newborn/population screening:** No dedicated PBD/ZSD population screening program identified (see Section 10 caveat re: X-ALD screening being gene- and disease-distinct, even though it shares an analyte).

---

## 14. Other Species / Natural Disease

**Taxonomy of model use:** I found no report of naturally occurring PEX10-related peroxisome biogenesis disease in a non-human species (companion animal, livestock, or wildlife) in this search — this reads as a genuine absence in the literature I could access, not a confirmed negative, since I did not query OMIA directly.

**Orthology:** PEX10 has 1:1 orthology across human, mouse, rat, and zebrafish (per search-derived GeneCards/ortholog summary) — consistent with its being a conserved, essential peroxisomal-biogenesis gene rather than one with lineage-specific duplication/divergence.

**Comparative biology:** The PEX10 protein's core function (RING-domain E3 ligase within the PEX2-PEX10-PEX12 retrotranslocation channel) is deeply conserved from yeast to human — the original human PEX10 identification (Warren et al. 1998; Okumoto et al. 1998) relied on functional complementation of a yeast-homologous defect and of CHO cell mutants (complementation groups ZP139/ZP105), demonstrating that the peroxisomal-import machinery is evolutionarily ancient and functionally interchangeable across eukaryotes for basic biochemical assay purposes, even though disease-level phenotypes (obviously) only manifest in the organismal context of higher vertebrates with the relevant tissue systems (myelinated CNS, adrenal cortex, etc.).

**Zoonotic/transmission relevance:** Not applicable — this is a non-communicable monogenic disorder.

---

## 15. Model Organisms

**Mouse:** Homozygous *Pex10* knockout mice are **embryonic or perinatal lethal** (search-derived summary of MGI/IMPC-type data — I did not fetch the primary knockout-characterization paper directly in this session, so the specific publication and detailed phenotype description are not independently verified here). A separate ENU-induced *Pex10* mouse allele shows a less-than-fully-null phenotype: partial neonatal mortality from respiratory distress, loss of embryonic movement, and prenatal pathology including altered biochemistry, axonal integrity defects, decreased Schwann cell number, and neuromuscular junction defects (search-derived; primary citation not independently fetched). This hypomorphic-mouse/full-null-lethal contrast is directly analogous to the human null-vs-missense PBD6A/PBD6B split and would be worth citing as supportive cross-species evidence for the genotype-severity model **once the primary mouse paper is located and verified** — I am flagging this as a promising but currently unverified lead rather than asserting it as confirmed.

**Zebrafish:** Zebrafish are an established peroxisome-biogenesis-disorder model system generally (a 2025 review, "Modelling Peroxisomal Disorders in Zebrafish," PMC11764017, was located), and *pex10* has a defined zebrafish ortholog (per PubChem gene record), but **I did not find a published pex10-specific zebrafish knockout/phenotype paper** in this search — the zebrafish literature I retrieved concerns *pex1* loss-of-function specifically (a November 2025 paper showing *pex1⁻/⁻* zebrafish are viable and recapitulate ZSD hallmarks, including ER-stress/pexophagy upregulation and dysregulated neurophysiological/visual-perception transcriptomic signatures). This is a genuine gap in the PEX10-specific model-organism literature as far as I could determine, not an oversight on my part — if a PBD6B curation effort needs a zebrafish reference, *pex1* is the closest available surrogate model, not a PEX10-specific one, and that distinction should be preserved rather than blurred.

**Cell-based models:**
- Patient-derived fibroblasts, complementation group 7 (US)/B (Japan) — the primary historical and ongoing tool for functional variant characterization (used in essentially every gene-identification and genotype-phenotype paper cited above).
- CHO mutant cell lines ZP139 and ZP105, both defective in peroxisome biogenesis and used for the original functional-complementation cloning of human PEX10 (Warren et al. 1998).
- Yeast Pex10p — the original ortholog whose characterization guided human gene identification, useful for basic mechanistic/structural studies of the retrotranslocation channel but not a disease model per se.

**Applications:** These models have supported (a) gene identification and functional complementation assays establishing loss-of-function as the mechanism, (b) genotype-phenotype correlation work distinguishing null from hypomorphic alleles by residual complementation activity, and (c) — via the *Nature* 2022 cryo-EM structure (Feng et al., using reconstituted/heterologous systems rather than a patient-derived model per se) — direct structural insight into how PEX10 variants would be predicted to disrupt channel assembly, though I did not find a paper mapping specific PBD6B patient variants onto that structure.

**Model limitations:** Not explicitly discussed for PEX10 in the sources I retrieved. By extension from the general ZSD mouse-model literature (which I did not fetch directly for this report), a recurring limitation across peroxisomal-disorder models is imperfect recapitulation of the human CNS neuronal-migration phenotype and variable severity concordance with the causal human allele — I flag this as a reasoned expectation rather than a directly cited finding for PEX10 specifically.

---

## Summary of confidence levels and open gaps

- **High confidence, directly sourced:** gene identity (PEX10, not PEX26) and disease identifiers; PEX10 protein function and the PEX2-PEX10-PEX12 retrotranslocation-channel structure; the core genotype-phenotype rule (null → severe, hypomorphic missense → mild); the specific PBD6B case reports and their described phenotypes; the ZSD-wide diagnostic panel and its caveat about near-normal biochemistry in mild disease; cholic acid's FDA approval and the DHA trial's negative primary-endpoint result.
- **Moderate confidence, generalized from ZSD-wide (largely PEX1) literature rather than PEX10-specific data:** the full organ-by-organ pathophysiologic mechanism (steps 4–10 in Section 6), general prognosis/mortality figures by severity tier, adrenal insufficiency prevalence, management recommendations for individual organ systems.
- **Explicitly flagged as unverified leads requiring primary-source confirmation before any curation use:** the c.790C>T/p.Arg264X gnomAD allele-frequency figure; the New York and Japan ZSD incidence figures; the Berendse et al. 2014 PMID; the exact mouse *Pex10* knockout paper; all suggested HPO/GO/CL/UBERON/NCIT/CHEBI terms.
- **Genuine gaps, not oversights:** PEX10-specific zebrafish model; PEX10-isolated prevalence/incidence figure; PEX10-specific carrier frequency; quantitative PEX10-specific survival data; any environmental/gene-environment interaction literature (none exists, as expected for this mechanism).

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 12 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 40 |
| Resolved | 39 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 25 |
| Terms named correctly | 19 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 6 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001518` (1 mention) - the report calls it "Small for gestational age is not relevant — omit"; HP calls it **Small for gestational age**
- `HP:0000510` (1 mention) - the report calls it "Retinitis pigmentosa jointly relevant"; HP calls it **Rod-cone dystrophy**, and lists "Retinitis pigmentosa" among its other names
- `HP:0001392` (1 mention) - the report calls it "Abnormality of the liver / hepatomegaly-adjacent"; HP calls it **Abnormality of the liver**
- `GO:0006693` (1 mention) - the report calls it "prostaglandin metabolic process — not directly relevant, omit"; GO calls it **prostaglandin metabolic process**
- `GO:0008306` (1 mention) - the report calls it "associative learning — not relevant, omit"; GO calls it **associative learning**
- `CL:0000499` (1 mention) - the report calls it "stromal cell — too generic, avoid"; CL calls it **stromal cell**

39 of 40 terms resolved to a current term; the rest could not be looked up either way.