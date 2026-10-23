---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5-5
cached: false
start_time: '2026-09-30T23:35:51.544344'
end_time: '2026-09-30T23:37:34.918037'
duration_seconds: 103.37
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Dermatitis Herpetiformis
  mondo_id: MONDO:0015614
  category: Autoimmune
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
  - claude-sonnet-5-5
  num_turns: 12
  total_cost_usd: 1.0315912000000003
  session_id: 81562984-f39d-5787-be67-7015e0b1b678
  stop_reason: end_turn
  permission_denials: 1
  denied_tools:
  - Bash
  assistant_text_blocks: 3
reference_validation:
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 6
  quotes_valid: 5
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:31244841
  relevance_assessed: 18
  on_topic: 8
  needs_review: true
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 2
  verified: 2
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Dermatitis Herpetiformis
- **MONDO ID:** MONDO:0015614 (if available)
- **Category:** Autoimmune

## Research Objectives

Please provide a comprehensive research report on **Dermatitis Herpetiformis** covering all of the
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

I'll load the search tools first, then verify the key citations before writing the report.

I'm checking PubMed to confirm the primary-literature PMIDs before I write the report.

# Dermatitis Herpetiformis (MONDO:0015614): Research Report for Knowledge Base Curation

**Evidence provenance.** I verified these PMIDs against PubMed E-utilities (title, year, journal) in this session. Quoted text comes from the abstracts I retrieved. Everything else is from general domain knowledge and is marked **[unverified]**. Check those claims and their PMIDs with `just fetch-reference` and `just count-verified-snippets` before using them as evidence. I did not look up ontology identifiers (HP, GO, CL, UBERON, NCIT, CHEBI, MONDO). Every term named below is a **lead only**, to be looked up with `runoak` or the term caches before binding. I did not confirm the MONDO ID from the template.

**Verified source list**

| PMID | Reference |
|---|---|
| 11901200 | Sárdy 2002, J Exp Med, "Epidermal transglutaminase (TGase 3) is the autoantigen of dermatitis herpetiformis." |
| 21517799 | Salmi 2011, Br J Dermatol, Finnish 40-year prevalence and incidence study |
| 37971253 | Swedish nationwide incidence study, Acta Derm Venereol 2023 |
| 33432477 | Reunala et al. 2021, Am J Clin Dermatol, update on diagnosis and management |
| 34441049 | Medicina 2021, update on diagnosis, disease monitoring and management |
| 31244841 | Antiga and Caproni 2019, Front Immunol, "Dermatitis Herpetiformis: Novel Perspectives" |
| 32039457 | Acta Derm Venereol 2020, "Current Concepts of Dermatitis Herpetiformis" |
| 24740905 | BMJ 2014, "Dermatitis herpetiformis" |
| 22560140, 21925009 | Management reviews (Immunol Allergy Clin North Am 2012; Dermatol Clin 2011) |
| 42256615 | Lancet Reg Health Am 2026, mortality, CVD and cancer in coeliac disease and DH |
| 37595955 | J Eur Acad Dermatol Venereol 2024, GI symptoms at diagnosis and on a long-term gluten-free diet |
| 32290504 | Nutrients 2020, oats in DH |
| 26267424 | Am J Clin Dermatol 2015, quality of life and GI symptoms in long-term treated DH |
| 37798283 | Nat Commun 2023, autoantibody binding to human TG3 |
| 39078587 | Am J Clin Dermatol 2024, dapsone use in dermatology |
| 31909480 | Int J Dermatol 2020, update on dapsone |
| 31106757 | Eur J Dermatol 2019, fibrillar-type DH |
| 26765204 | J Dtsch Dermatol Ges 2016, acantholytic variant |

---

## 1. Disease Information

Dermatitis herpetiformis (DH, Duhring-Brocq disease) is an intensely itchy, chronic, blistering skin disease. It is the cutaneous manifestation of gluten-sensitive enteropathy (coeliac disease). Diagnosis rests on granular IgA deposits in the papillary dermis.

> "DH diagnosis is confirmed by showing granular immunoglobulin A deposits in the papillary dermis" (PMID:33432477)

> "The DH autoantigen, transglutaminase 3, is deposited at the same site in tightly bound immune complexes" (PMID:33432477)

- **Identifiers:** MONDO:0015614 comes from the template and is unchecked. OMIM, Orphanet, ICD-10 (L13.0), ICD-11 and MeSH IDs were not retrieved. ICD-10 L13.0 is from memory **[unverified]**. Look the rest up with `just fetch-reference ORPHA:<n>` or the term caches.
- **Synonyms:** Duhring disease, Duhring-Brocq disease, "coeliac disease of the skin". The literature also calls it "gluten-sensitive dermatopathy" **[unverified]**.
- **Data level:** The resources cited are aggregated cohort, registry and review data, not EHR data from individual patients.
- **Differentials with similar names:** Pemphigus herpetiformis (PMID:40686696) is a different disease. The "acantholytic" (PMID:26765204) and "fibrillar-type" (PMID:31106757) variants are reported subtypes.

## 2. Etiology

- **Causal factors:** DH is a gluten-driven autoimmune disorder on the coeliac disease spectrum. Dietary gluten is the trigger. Susceptibility is HLA-DQ2/DQ8 restricted **[unverified, well established]**.
- **Genetic risk:** HLA-DQ2.5 (DQA1*05:01/DQB1*02:01) and DQ8 (DQA1*03/DQB1*03:02) are present in nearly all patients **[unverified]**. Non-HLA coeliac loci overlap with DH. I did not retrieve DH-specific GWAS data.
- **Environmental risk:** Gluten ingestion is the driver. Iodine exacerbation of DH is a long-standing clinical observation **[unverified]**.
- **Protective factors:** Strict gluten-free diet (GFD) induces remission and is the protective intervention. No protective genetic variants have been established.
- **Gene-environment interaction:** HLA-DQ2/DQ8 permits presentation of deamidated gluten peptides to T cells. Whether this leads to gut disease alone or to DH as well is poorly understood. Nothing in the retrieved material explains why only some coeliac patients develop skin disease (an **open question** worth a knowledge-gap entry).

## 3. Phenotypes

| Phenotype | Notes | HPO lead (verify) |
|---|---|---|
| Intense pruritus | Burning or itching often precedes lesions | Pruritus |
| Grouped papulovesicles on extensor surfaces | Elbows, knees, buttocks, scalp, sacrum; symmetric | Vesicular/bullous eruption |
| Excoriations and erosions | Vesicles are usually scratched off, so intact blisters are uncommon | Excoriation |
| Granular IgA deposits (laboratory/histologic) | Pathognomonic finding | Skin IgA deposition lead |
| Associated gluten-sensitive enteropathy | Often subclinical in DH | Villous atrophy |
| Gastrointestinal symptoms | Reported at diagnosis and persist in some patients on GFD (PMID:37595955) | Abdominal pain, diarrhea leads |

- **Onset:** Mean age at diagnosis was 60.9 years in Sweden (PMID:37971253). In Finland the mean age rose significantly during the study, in men from 35.3 to 51.1 years (PMID:21517799). Childhood onset occurs but is less common **[unverified]**.
- **Course:** Chronic and relapsing while gluten is eaten. Skin lesions remit on a GFD, often over months to years **[unverified]**.
- **Quality of life:** Quality of life and GI symptoms were studied in long-term treated patients (PMID:26267424). The extent of impairment is not quoted here because I did not read the abstract. Oats safety and quality-of-life effects are in PMID:32290504.

## 4. Genetic/Molecular Information

- **Monogenic cause:** None. DH is a complex, multifactorial condition.
- **HLA:** HLA-DQ2/DQ8 (HLA-DQA1/DQB1). HGNC IDs must be looked up; in this repository they use the lowercase `hgnc:` prefix.
- **Autoantigen gene:** TGM3 (epidermal transglutaminase, TG3), identified in PMID:11901200. Enzyme-substrate conformation and autoantibody binding are described in PMID:37798283. TGM2 (tissue transglutaminase) is the coeliac autoantigen.
- **Modifier, epigenetic, chromosomal features:** Not retrieved. Treat them as not available.

## 5. Environmental Information

- **Dietary gluten** (wheat, rye, barley) is the established trigger. Whether oats are safe is addressed in PMID:32290504. I did not read its conclusions, so check them before citing.
- **Iodine and drugs:** Iodide exacerbation **[unverified]**. Some NSAIDs are also implicated **[unverified]**.
- **Infectious agents:** None established.

## 6. Mechanism / Pathophysiology

**Causal chain** (steps marked *inferred* are not demonstrated in the retrieved sources):

1. HLA-DQ2/DQ8 genotype leads to presentation of gluten peptides to CD4+ T cells in the small intestine **[unverified]**.
2. Dietary gluten, deamidated by tissue transglutaminase (TG2), leads to gut T-cell activation and an IgA response to TG2 **[unverified]**.
3. Epitope spreading leads to IgA autoantibodies to epidermal transglutaminase (TG3). TG3 was identified as the DH autoantigen (PMID:11901200). Why the response spreads from TG2 to TG3 is *inferred*.
4. Circulating IgA-TG3 complexes or TG3 deposition at the papillary dermis leads to granular IgA-TG3 deposits (PMID:33432477).
5. The deposits lead to neutrophil recruitment and complement activation, causing dermal-epidermal separation **[unverified; the neutrophil step is *inferred* from the histology]**.
6. Subepidermal vesicle formation leads to intense itch and the clinical eruption.
7. Branch: a GFD removes the antigenic drive and leads to gradual clearance of skin deposits and lesions. Dapsone controls the neutrophil-mediated inflammation faster than diet does but does not treat the underlying cause (PMID:33432477).

- **Cells and GO/CL leads:** CD4+ T cells, B cells and plasma cells (IgA), neutrophils, enterocytes and keratinocytes. Terms to look up include "antibody-dependent" and "neutrophil chemotaxis" processes.
- **Protein dysfunction:** Autoantibodies bind TG3 in a defined enzyme-substrate intermediate conformation (PMID:37798283).
- **Molecular profiling, single-cell, spatial and functional-genomics data:** Not retrieved. I did not search GEO for DH datasets. Treat as a gap.

## 7. Anatomical Structures Affected

- **Skin:** Extensor surfaces and papillary dermis are the primary site. The lesions are symmetric and grouped.
- **Gut:** The small intestine often has subclinical coeliac-type enteropathy, and some patients have GI symptoms (PMID:37595955).
- **UBERON leads:** skin of elbow, knee and buttock; dermal papilla; small intestine.
- **Cellular/subcellular:** The dermal-epidermal junction is the target zone for the deposits.

## 8. Temporal Development

- **Onset:** Usually adult. Mean diagnosis age was 60.9 years in Sweden (PMID:37971253) and has risen over time in Finland (PMID:21517799).
- **Course:** Chronic, relapsing while gluten is eaten. Lifelong gluten sensitivity persists.
- **Remission:** Induced by the GFD. PMID:33432477 states "Dietary adherence offers an excellent long-term prognosis."

## 9. Inheritance and Population

- **Inheritance:** Multifactorial, with HLA-DQ2/DQ8 dependence. Bind `Multifactorial inheritance` (HP lead) or leave it absent if no suitable term is found.
- **Finland** (PMID:21517799): "The prevalence of DH was 75·3 per 100,000", "annual incidence of DH in the whole period was 3·5 per 100,000", male to female ratio "1·1:1".
- **Sweden, 2005–2018** (PMID:37971253): "The mean annual incidence of dermatitis herpetiformis was 0.93/100,000", female to male ratio "1:1", "mean age at diagnosis 60.9 years".
- **Geography and ethnicity:** Highest in Northern Europe. Rare in East Asian and African populations **[unverified]**.
- **Trend:** Incidence of DH has fallen in several countries while coeliac diagnoses have risen **[unverified]**. The Finnish and Swedish figures differ by several-fold, which is a methodological difference and possibly a real regional one.
- **Prevalence modelling:** Use `measure_type: POINT_PREVALENCE` for the Finnish figure and `ANNUAL_INCIDENCE` with an explicit `rate_denominator` for incidence.

## 10. Diagnostics

- **Direct immunofluorescence (DIF)** of perilesional skin is the gold standard. "Detecting granular IgA deposits at the dermal-epidermal junction by direct immunfluorescence represents the most specific diagnostic tool" (PMID:31244841).
- **Histology:** Neutrophilic microabscesses in dermal papillae with subepidermal blisters **[unverified]**.
- **Serology:** Anti-TG2, anti-TG3 and anti-endomysial IgA. Anti-TG3 may be more DH-specific **[unverified]**.
- **Small-bowel biopsy** is not always needed when DH is confirmed, but practice varies (see PMID:34441049).
- **Genetic testing:** HLA-DQ2/DQ8 typing can exclude coeliac disease and DH when both are negative (high negative predictive value) **[unverified]**.
- **Differential:** Linear IgA bullous dermatosis, bullous pemphigoid, scabies, eczema, pemphigus herpetiformis (PMID:40686696).

## 11. Outcome/Prognosis

- **Mortality and malignancy** (PMID:42256615, 2026 matched cohort): "566/6768 (8.36%) died, compared with 443/6770 (6.54%) matched comparators (aHR = 1.25; 1.10-1.42)" and "non-Hodgkin lymphoma (aHR = 2.58; 1.47-4.51)". I retrieved only the DH-specific sentences, so I can't confirm which group each figure belongs to. Re-read the abstract before curating, because it covers both coeliac disease and DH.
- **Lymphoma:** Risk is elevated in DH (see above). Earlier cohort data on this are not verified here.
- **Complications:** Associated autoimmune disease (thyroid disease, type 1 diabetes) **[unverified]**; osteoporosis and GFD-related nutritional issues.
- **Prognosis on diet:** "Dietary adherence offers an excellent long-term prognosis" (PMID:33432477).

## 12. Treatment

- **Gluten-free diet:** "the treatment of choice for all patients is a gluten-free diet" (PMID:33432477). Lesions clear slowly, over months to years. NCIT lead: Dietary Intervention (`NCIT:C15447` in this repository's table, re-check). `therapeutic_modality: BEHAVIORAL`.
- **Dapsone:** "most patients need additional dapsone" (PMID:33432477). It gives rapid control of itch and new lesions, typically within days **[unverified]**. Use the pharmacotherapy action term with `therapeutic_agent` bound to dapsone (look up in CHEBI). Reviews: PMID:39078587, PMID:31909480. `therapeutic_modality: SMALL_MOLECULE`.
- **Dapsone adverse effects:** Dose-related hemolysis, methemoglobinemia, agranulocytosis, neuropathy **[unverified]**. G6PD testing before starting is standard **[unverified]**. Pancreatitis and overdose are documented in case reports, which the literature search surfaced but I did not review.
- **Alternatives** when dapsone is not tolerated: sulfapyridine, sulfasalazine **[unverified]**. Topical steroids for symptoms.
- **Oats:** Safety and quality-of-life effects are addressed in PMID:32290504.
- **Reviews of management:** PMID:22560140, PMID:21925009, PMID:34441049.
- **Clinical trials:** Not searched. Run `just discover-datasets` and search ClinicalTrials.gov before adding any.

## 13. Prevention

- **Primary prevention:** None known.
- **Secondary prevention and tertiary prevention:** Lifelong strict GFD. It prevents skin flares and is believed to reduce lymphoma risk, but the protective effect on lymphoma needs confirmation **[unverified]**.
- **Monitoring:** Periodic dietary review and check-ups for associated autoimmune and malignancy risk (see PMID:34441049).
- **Counseling:** Family screening for coeliac disease in first-degree relatives **[unverified]**.

## 14. Other Species / Natural Disease

I did not search OMIA. The only possibly relevant naturally occurring analogue is gluten-sensitive enteropathy in Irish Setters **[unverified]**, and I know of no established DH equivalent. Treat species, breed and orthologous-gene fields as not available.

## 15. Model Organisms

I did not retrieve model-organism data. From memory, **[unverified]** there is no widely accepted faithful animal model of DH. Humanized HLA-DQ8 transgenic mice exist for gluten sensitivity, and some work on DH-like skin deposition in such mice has been reported. Flag this as a knowledge gap (`HUMAN_MODEL_MISMATCH` or `KNOWLEDGE_GAP` discussion) rather than inventing a model entry.

---

## Gaps and Next Steps for the Curator

1. **Unretrieved identifiers:** OMIM, Orphanet, ICD-11, MeSH, and the MONDO ID check.
2. **Unsourced claims:** Every item marked **[unverified]** needs a PMID with an exact snippet. Start with the HLA-DQ2/DQ8 frequency, the TG2-to-TG3 epitope spreading concept, and the neutrophil/complement steps.
3. **Quote check:** Quotes above came from abstract text returned by a summarizing fetch. Re-verify them against the `references_cache` copies before using them as snippets.
4. **Suggested next fetches:** `just fetch-reference PMID:11901200 PMID:33432477 PMID:21517799 PMID:37971253 PMID:31244841 PMID:42256615`.
5. **Search gaps:** GEO and other omics datasets, ClinicalTrials.gov, and OMIA were not searched.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 6 |
| Quoted claims found in source | 5 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 18 |
| On topic | 8 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMID:31244841`: "Detecting granular IgA deposits at the dermal-epidermal junction by direct immunfluorescence represents the most specific diagnostic tool"
  - closest text in source: "Detecting granular IgA deposits at the dermal-epidermal junction by direct immunofluorescence (DIF) from perilesional skin represents the most specific diagnostic tool"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 2 |
| Resolved | 2 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.