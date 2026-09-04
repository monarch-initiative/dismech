---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-02T13:18:40.022900'
end_time: '2026-09-02T13:24:08.703099'
duration_seconds: 328.68
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Developmental And Epileptic Encephalopathy 38
  mondo_id: ''
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
  web_search_requests: 9
  num_turns: 30
  total_cost_usd: 1.3513608
  session_id: a7ad17b6-3a08-5da2-b864-d177f77ddc2f
  stop_reason: end_turn
  assistant_text_blocks: 3
citation_count: 3
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 1
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:34017911
  relevance_assessed: 9
  on_topic: 9
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 50
  verified: 50
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
- **Disease Name:** Developmental And Epileptic Encephalopathy 38
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Developmental And Epileptic Encephalopathy 38** covering all of the
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

I'll research this now using web search and fetch tools.

I have enough primary-literature detail now to compile the full report.

I now have comprehensive primary-literature data. Let me compile the full research report.

# Developmental and Epileptic Encephalopathy 38 (DEE38 / EIEE38): Comprehensive Research Report

## 1. Disease Information

**Overview.** Developmental and Epileptic Encephalopathy 38 (DEE38; formerly designated Early Infantile Epileptic Encephalopathy 38, EIEE38) is an autosomal recessive neurologic/neurodegenerative disorder caused by biallelic loss-of-function variants in **ARV1** (ARV1 Fatty Acid Homeostasis Modulator), an endoplasmic reticulum transmembrane protein. It presents in early infancy with severe global developmental impairment followed by onset of refractory, multifocal/migrating seizures, and follows a progressive, usually fatal, neurodegenerative course [OMIM #617020; PMID:27270415].

**Key identifiers:**
- **OMIM:** #617020 (DEE38), gene locus *ARV1* OMIM 611647, chromosome 1q42
- **Gene:** ARV1 (HGNC — "ARV1 fatty acid homeostasis modulator"; historically annotated "acyl-CoA cholesterol acyltransferase [ACAT]-related enzyme 2, required for viability 1")
- **Inheritance:** Autosomal recessive
- **Synonyms:** Early Infantile Epileptic Encephalopathy 38 (EIEE38); ARV1-related developmental and epileptic encephalopathy; ARV1 deficiency
- Note: MONDO and dedicated GeneReviews/Orphanet entries were not directly retrievable in this search session (site access blocked); the OMIM entry #617020 is the authoritative primary identifier and should be used to cross-reference MONDO on curation.

**Evidence basis:** Nearly all published knowledge on DEE38 derives from individual case reports and small case series (single families or trios of patients) rather than large aggregated registries — as of the most recent literature identified (2024–2025), only on the order of ~20–30 molecularly confirmed cases have been reported worldwide, virtually all from consanguineous or compound-heterozygous pedigrees [PMC12080507].

Sources:
- [OMIM #617020 — DEE38](https://omim.org/entry/617020)
- [Palmer et al. 2016, Hum Mol Genet, PMID:27270415](https://pmc.ncbi.nlm.nih.gov/articles/PMC5181598/)
- [PMC12080507 — "When Genes Misfire" review](https://pmc.ncbi.nlm.nih.gov/articles/PMC12080507/)

---

## 2. Etiology

### Disease causal factors
DEE38 is caused exclusively by **biallelic (homozygous or compound heterozygous) pathogenic variants in ARV1**. No environmental, infectious, or purely mechanistic (non-genetic) cause has been described; this is a monogenic Mendelian disorder.

### Genetic risk factors
- **Causal variants reported to date** span multiple mutation classes:
  - Missense: p.Cys61Tyr (recurrent, seen in 2 of 3 cases in one Egyptian series) [PMC12103100]; p.Gly189Arg (homozygous, 3 related children) [Neurogenetics 2020]
  - Nonsense: p.Trp163* [PMID:34017911]; p.Gln62Ter [Springer J Rare Dis 2025]
  - Frameshift: p.Phe144Argfs*5 (novel) [PMC12103100]
  - Splice-site: c.294+1G>A (exon 2 skipping, ~45% mRNA reduction, ~20% protein reduction) and c.674-2A>T (exon 5 skipping, ~40-50% protein reduction) [PMID:32165008]; c.363_364del (p.Ser122Glnfs*7) [PMID:34017911]
  - In-frame deletion: c.554_556delTAT (p.Leu185del), in the fourth predicted transmembrane domain — associated with a dilated cardiomyopathy phenotype [PMID:35227294]
- **Founder/recurrent alleles:** p.Cys61Tyr and the exon-2/exon-5 splice variants recur across unrelated consanguineous families, consistent with regional founder effects (reported in Middle Eastern/North African and South Asian cohorts) [PMC12103100; PMID:32165008].
- **Modifier genes:** None established; phenotypic variability (e.g., presence/absence of cardiomyopathy, retinal dystrophy, or skeletal dysplasia) is not yet linked to specific modifier loci — likely reflects allelic severity (null vs hypomorphic) and possibly genetic background.

### Environmental risk factors
None identified — parental **consanguinity** is the dominant epidemiological risk factor (nearly all reported families), consistent with autosomal recessive inheritance and variant enrichment in consanguineous populations, not a true environmental exposure.

### Protective factors
No genetic or environmental protective factors have been reported. No protective alleles are documented in population databases for ARV1 loss-of-function variants (specific gnomAD constraint metrics for ARV1, e.g., pLI/LOEUF, were not retrievable in this search but should be checked directly on the gnomAD browser during curation).

### Gene-environment interactions
Not described; disease penetrance and expressivity appear driven by variant type/residual protein function rather than documented environmental modulation. Fever has been reported as a *trigger for seizure exacerbation* in affected patients (not a causal environmental factor) [PMID:34017911].

---

## 3. Phenotypes

DEE38 phenotypes are best organized along the disease's stereotyped **pre-seizure prodrome → seizure-onset → progressive regression** timeline.

### Pre-seizure (neonatal–early infantile) phenotypes
- **Global developmental delay / failure to achieve milestones** — onset in first weeks to months of life, universal, severe [OMIM #617020; PMID:27270415]
- **Central hypotonia with poor head control** — onset weeks 4–8, universal
- **Visual inattention with roving eye movements / nystagmus** — universal in the prodromal phase; some patients diagnosed with **Leber congenital amaurosis / retinal dystrophy** on electrophysiology [PMID:27270415]
- **Cortical visual impairment** progressing over time [PMID:32165008]

### Seizure phenotypes
- **Age of onset:** typically 4–7 months (range 3 months–8 months across reports) [OMIM #617020; PMID:34017911]
- **Seizure types:** multifocal/migrating focal (nonmotor) seizures meeting criteria for **epilepsy of infancy with migrating focal seizures (EIMFS)**; generalized tonic-clonic; myoclonic; status epilepticus (both focal and myoclonic status) is common and often fever-triggered [PMID:34017911; Neurology Genetics 2021]
- **Severity/course:** intractable/refractory to multiple antiseizure medications (up to 7 agents trialed in individual cases) [PMC12103100]; **progressive** with EEG evolution from normal → focal epileptiform discharges → multifocal → modified hypsarrhythmia [PMID:27270415]
- **Frequency:** seizures occur in essentially 100% of reported cases (defining feature); status epilepticus reported in a majority of the most severely affected patients

### Neurological/motor phenotypes
- **Dystonia, extensor posturing, dyskinetic movements** [PMID:27270415; PMID:34017911]
- **Ataxia**, progressive cerebellar signs
- **Spasticity** (peripheral) combined with central hypotonia
- **Loss of previously attained (already minimal) volitional movement** — progressive regression
- **Inability to walk or speak** in the majority of long-surviving patients [OMIM #617020]

### Other organ-system phenotypes
- **Dilated cardiomyopathy** — an increasingly recognized part of the ARV1 phenotype spectrum, reported in at least 4 patients across 2+ families, with LVEF as low as 20% [PMID:35227294]
- **Hearing loss** [WebSearch synthesis, PMC12080507]
- **Skeletal dysplasia / scoliosis** — "marked rotatory scoliosis" reported [PMID:32165008]
- **Dysmorphic features** — macrocephaly, low-set ears, midfacial hypoplasia/coarse facial features in some families [PMC12103100; PMID:32165008]
- **Feeding difficulties / poor oromotor control** requiring gastrostomy tube feeding; gastroesophageal reflux [PMID:27270415]
- **Elevated alpha-fetoprotein (AFP)** reported as a laboratory abnormality in some patients [PMC12080507] — of note, elevated AFP is a recognized feature of several other neurodegenerative/DNA-repair disorders and its mechanistic link to ARV1 deficiency is not established; flag for verification against primary source before curating.
- **Acute liver failure** — reported as a fatal complication in at least one case (in the setting of sepsis/hepatic encephalopathy) [PMC12103100], though causal relationship to ARV1 deficiency itself (vs. antiepileptic drug hepatotoxicity or intercurrent infection) is not established.

### Quality of life impact
Formal QOL instrument data (EQ-5D, SF-36) are not available for this ultra-rare disorder. Qualitatively, the disease produces profound, lifelong disability: no ambulation, no or minimal expressive language (one 21-year-old survivor had "a vocabulary restricted to about five words" [PMID:35227294]), dependence for all activities of daily living, and a very high risk of premature death from seizure-related complications (aspiration pneumonia, status epilepticus) [PMID:27270415; PMID:34017911].

### Suggested HPO terms
- HP:0001250 Seizure
- HP:0032792 (or HP:0011097) Epileptic encephalopathy
- HP:0002187 Intellectual disability, profound
- HP:0001263 Global developmental delay
- HP:0001252 Hypotonia
- HP:0001257 Spasticity
- HP:0002072 Chorea/dyskinetic movement (or HP:0002273 Ataxia)
- HP:0000639 Nystagmus
- HP:0000556 Retinal dystrophy
- HP:0007750 Recurrent status epilepticus (or HP:0002133 Status epilepticus)
- HP:0011451 Epileptic spasm / HP:0011097 Epileptic encephalopathy pattern (hypsarrhythmia: HP:0010544)
- HP:0001635 Dilated cardiomyopathy
- HP:0000407 Sensorineural hearing loss
- HP:0002650 Scoliosis
- HP:0000276 Long face / midface hypoplasia
- HP:0000508 Ptosis or HP:0000486 Strabismus (per detailed case review as needed)
- HP:0002910 Elevated alpha-fetoprotein (flag as needs-verification)

---

## 4. Genetic/Molecular Information

**Causal gene:** ARV1 (chr1q42; OMIM 611647). Encodes a **271-amino-acid endoplasmic reticulum transmembrane protein** with a cytosolic N-terminal zinc-binding motif and multiple transmembrane domains [PMID:27270415].

**Variant classification/spectrum** (ACMG pathogenic/likely pathogenic in all reported cases; disease is fully recessive):
| Variant (protein) | Type | Zygosity | Source |
|---|---|---|---|
| p.Trp163* | Nonsense | Compound het (with p.Ser122Glnfs*7) | PMID:34017911 |
| p.Ser122Glnfs*7 | Frameshift | Compound het | PMID:34017911 |
| c.294+1G>A | Splice donor (exon 2 skip) | Homozygous | PMID:32165008; PMID:27270415 |
| c.674-2A>T | Splice acceptor (exon 5 skip) | Homozygous | PMID:32165008 |
| p.Cys61Tyr | Missense | Homozygous (recurrent) | PMC12103100 |
| p.Phe144Argfs*5 | Frameshift (novel) | Homozygous | PMC12103100 |
| p.Gly189Arg | Missense | Homozygous | Neurogenetics 2020 |
| p.Gln62Ter | Nonsense | — | J Rare Dis 2025 |
| p.Leu185del (c.554_556delTAT) | In-frame deletion | Homozygous | PMID:35227294 |
| p.(Lys59_Asn98del) | In-frame deletion | — (fails temperature-sensitive rescue in yeast) | PMID:27270415 |

**Allele frequency:** Population frequency data specific to these variants (gnomAD) were not directly retrieved in this session; given the ultra-rare, founder-enriched, consanguinity-associated pattern, allele frequencies for individual pathogenic variants are expected to be at or near absent in gnomAD outside specific founder populations — verify per-variant in ClinVar/gnomAD during curation.

**Somatic vs. germline:** All reported variants are germline.

**Functional consequences (loss of function):** All characterized alleles behave as **loss-of-function** — nonsense/frameshift variants trigger nonsense-mediated decay of ARV1 mRNA [PMID:34017911]; splice variants reduce mRNA/protein by 20–50% [PMID:32165008]; the p.(Lys59_Asn98del) missense/deletion variant "completely failed to rescue at restrictive temperature" in a yeast complementation assay and showed no detectable protein in mammalian cells [PMID:27270415]. No gain-of-function or dominant-negative alleles have been reported.

**Molecular mechanism — GPI-anchor biosynthesis (a major recent advance):**
- ARV1 was originally characterized in *S. cerevisiae* as a sterol-trafficking protein required for viability in ACAT-deficient yeast, mediating ER-to-plasma-membrane sterol transport and also implicated in sphingolipid/ceramide metabolism [JBC classic yeast studies, Tinkelenberg & Sturley].
- A landmark 2020 human study demonstrated that patient fibroblasts and neutrophils show markedly reduced cell-surface **GPI-anchored proteins** (CD16 ~5% residual, CD59/CD87 <20% residual, reduced FLAER binding), directly implicating ARV1 in the **glycosylphosphatidylinositol (GPI) anchor biosynthesis pathway** and placing DEE38 among the **Inherited GPI Deficiency Disorders (IGDs)**, a group that also includes PIGA-, PIGN-, PIGT-, and related disorders [PMID:32165008].
- The 2021 genotype-phenotype refinement study (7 patients) confirmed reduced surface GPI-anchored proteins and — notably — showed that **lentiviral ARV1 gene transfer rescued the cellular GPI-anchoring defect** in patient cells, a proof-of-concept for gene-therapy correction [PMID:34296759].
- A 2025 mechanistic study resolved the molecular role definitively: **ARV1 is a bona fide component of the GPI N-acetylglucosaminyltransferase (GPI-GnT) complex**, the enzyme that catalyzes the first committed step of GPI biosynthesis. ARV1 associates specifically with the PIGQ subunit, and "ARV1-containing GPI-GnT used PI [phosphatidylinositol] more efficiently than ARV1-less GPI-GnT in an in vitro enzyme assay" — i.e., ARV1 facilitates recruitment of the PI substrate to the enzyme complex [PMID:40378954].
- Direct quote (2020 study): *"Loss of GPI-anchored proteins on our patients' cells confirms that the yeast Arv1 function of GPI-anchor synthesis is conserved in humans."* [PMID:32165008]

**Epigenetic information:** Not reported for ARV1/DEE38.

**Chromosomal abnormalities:** Disease is caused by point/indel variants within ARV1; no recurrent CNV or chromosomal rearrangement mechanism has been described.

**Suggested ontology terms:**
- HGNC: ARV1 gene
- GO:0006506 GPI anchor biosynthetic process
- GO:0016233 telomere capping (not relevant — exclude)
- GO:0034247 phosphatidylinositol N-acetylglucosaminyltransferase complex (GPI-GnT)
- GO:0032934 sterol binding / GO:0032366 intracellular sterol transport
- GO:0006672 ceramide metabolic process
- CHEBI:18085 glycosylphosphatidylinositol
- UniProt: ARV1_HUMAN (Q96BZ4)

---

## 5. Environmental Information

- **Environmental/toxin factors:** None established as causal.
- **Lifestyle factors:** Not applicable (early infantile monogenic disorder); note the **ketogenic diet** functions as a *treatment* modulator of seizure frequency in some patients (see Treatment, §12), not a risk/protective environmental exposure.
- **Infectious agents:** Not causal to the underlying disease, but **intercurrent infections (pneumonia, aspiration, sepsis) are the proximate cause of death** in the majority of reported fatal cases — e.g., death from "bronchopneumonia during status epilepticus" and "pneumonia" in two sisters [PMID:34017911], and death from "acute liver failure complicated by pneumonia, sepsis, and hepatic encephalopathy" in another case [PMC12103100]. **Fever is a well-documented trigger for seizure exacerbation and status epilepticus** in ARV1-deficient patients [PMID:34017911].

---

## 6. Mechanism / Pathophysiology

### Causal chain (numbered, from mutation to clinical manifestation)

1. Biallelic loss-of-function variants in **ARV1** → **loss/reduction of ARV1 protein** in the endoplasmic reticulum (demonstrated: NMD of nonsense/frameshift transcripts; 20–50% protein reduction from splice variants; failed rescue of missense/deletion alleles in yeast complementation assays) [PMID:34017911; PMID:32165008; PMID:27270415].
2. Loss of ARV1 **disrupts its role as a facilitating component of the GPI-GnT (GPI N-acetylglucosaminyltransferase) enzyme complex** (ARV1 binds PIGQ and promotes efficient recruitment of phosphatidylinositol substrate) → **impaired initiation of GPI-anchor biosynthesis** [PMID:40378954]. *(This is the most recently established, best-supported step in the chain — inferred from biochemical/enzymatic reconstitution data.)*
3. Impaired GPI biosynthesis → **reduced maturation and cell-surface expression of GPI-anchored proteins** (demonstrated directly in patient neutrophils/fibroblasts: CD16, CD59, CD87/uPAR, CD73, CD109 all reduced; FLAER binding reduced) [PMID:32165008; PMID:40378954].
4. In parallel (or contributing independently, degree of contribution not fully resolved), **ARV1's ancestral, evolutionarily conserved role in sterol/lipid trafficking is disrupted**: loss of ARV1 causes abnormal intracellular sterol distribution (ER sterol accumulation, reduced plasma-membrane sterol) and disturbed sphingolipid/ceramide metabolism, based on conserved yeast biology and demonstrated conservation of function by human ARV1 in yeast complementation assays [classic yeast literature; PMID:27270415].
5. Combined GPI-anchoring deficiency and lipid/sterol dyshomeostasis → **endoplasmic reticulum stress and activation of the unfolded protein response**, proposed as the proximate driver of cellular dysfunction: *"ER stress induced by accumulation of immature GPI-anchored proteins or aberrant lipid metabolism may be responsible for the diseases associated with ARV1 deficiency"* [PMID:34017911] *(explicitly flagged by the authors as inferred/hypothesized, not directly demonstrated in neurons)*.
6. ER stress/UPR activation and loss of GPI-anchored signaling/adhesion proteins on neuronal membranes → **disruption of neuronal membrane integrity, synaptic signaling, and excitatory-inhibitory balance** in the developing brain (this step draws an explicit mechanistic analogy to the well-characterized Inherited GPI Deficiency Disorders such as PIGA/PIGN/PIGT-CDG, which share "remarkably similar clinical and neuroimaging features," including EIMFS-type seizures, hypotonia, and cerebellar atrophy) [PMID:34017911].
7. This neuronal/synaptic disruption → **early-infantile-onset, multifocal/migrating, treatment-refractory seizures**, progressive **loss of developmental milestones**, and **progressive cerebral/cerebellar atrophy** on serial neuroimaging [PMID:27270415; PMID:34017911].
8. Independently, GPI-anchor/lipid dyshomeostasis in **non-neural tissues** produces the extra-neurological features of the phenotype: retinal GPI-anchored/lipid-dependent photoreceptor processes → **retinal dystrophy/cortical-retinal visual impairment**; cardiomyocyte membrane/lipid handling → **dilated cardiomyopathy** [PMID:35227294]; skeletal/connective tissue involvement → **scoliosis/skeletal dysplasia** [PMID:32165008]. The mechanistic link from ARV1 loss to each of these peripheral phenotypes is largely inferred by analogy to the neurological mechanism rather than tissue-specific experimentally demonstrated.
9. Repeated/prolonged seizures (status epilepticus) plus severe hypotonia/poor oromotor control → **aspiration risk and recurrent respiratory infection**, the proximate cause of death in most reported fatal cases (bronchopneumonia, sepsis) [PMID:27270415; PMID:34017911].

**Branch point:** Whether the dominant pathogenic driver is (a) GPI-anchor deficiency, (b) sterol/sphingolipid dyshomeostasis, or (c) both acting in parallel/synergistically remains an open mechanistic question in the field; the 2025 GPI-GnT structural/enzymatic data [PMID:40378954] provide the strongest direct causal evidence to date for the GPI-anchoring branch specifically.

### Molecular pathways
- GPI-anchor biosynthesis pathway (Reactome: "Synthesis of glycosylphosphatidylinositol (GPI)"; KEGG map00563 Glycosylphosphatidylinositol(GPI)-anchor biosynthesis)
- Sterol/lipid trafficking and homeostasis (ER-to-plasma-membrane sterol transport)
- Sphingolipid/ceramide metabolism
- Unfolded protein response / ER stress signaling (proposed downstream effector pathway)

### Cellular processes
- ER stress response, unfolded protein response
- Impaired post-translational lipid modification (GPI anchoring) of surface proteins
- Neuronal membrane/synaptic dysfunction (inferred)
- Purkinje cell loss (demonstrated on postmortem neuropathology: "severe and diffuse loss of Purkinje cells" [PMID:34017911])

### Protein dysfunction
Loss of function of ARV1 protein via nonsense-mediated decay, reduced transcript/protein abundance from splice defects, or failure of missense/in-frame-deletion variants to support ARV1's normal biochemical activity (yeast rescue assays) [PMID:27270415; PMID:32165008].

### Tissue damage mechanisms
Progressive cerebral and cerebellar atrophy with hypomyelination on serial MRI; cerebellar vermis atrophy; thin corpus callosum in infancy progressing to more diffuse atrophic change; muscle biopsy in one patient showed increased Type 1:Type 2 fiber ratio with lipid droplets adjacent to clumped mitochondria (suggesting a secondary muscle lipid-handling abnormality) [PMID:27270415].

### Molecular profiling
- Flow cytometry (neutrophils, fibroblasts): reduced CD16, CD59, CD66b, CD87/uPAR, CD73, CD109, FLAER binding [PMID:32165008; PMID:40378954]
- In vitro enzyme reconstitution assay: ARV1-containing vs. ARV1-less GPI-GnT complex activity comparison [PMID:40378954]
- No transcriptomic/proteomic/metabolomic datasets on human brain tissue were identified in this search.

### Advanced technologies
- **Mouse model (Palmer et al. 2016):** Neuronal-specific *Arv1* knockout mice recapitulate the human phenotype: circling behavior, hyperactivity, spontaneous generalized tonic-clonic seizures beginning after 12 weeks of age, reduced body weight (21% decrease in males, 15% in females) and white adipose tissue, and a striking **sex-dimorphic survival defect** (males: 80% survival to 20 weeks vs. females: 33% survival to 20 weeks, p=0.0053), plus fiber-type shifts in skeletal/diaphragm muscle [PMID:27270415]. Direct quote: *"Mice with a neuronal deletion of Arv1 recapitulated the human phenotype, exhibiting seizures and a severe survival defect in adulthood."*
- **Yeast complementation assays** used to functionally test human ARV1 missense/deletion variants [PMID:27270415].
- **AlphaFold3 structural modeling** used to predict the ring-shaped architecture of the ARV1-containing GPI-GnT complex [PMID:40378954].
- **Lentiviral gene-transfer rescue** in patient fibroblasts restoring GPI-anchored protein surface expression — a functional/therapeutic proof-of-concept experiment [PMID:34296759].

### Suggested GO / CL terms
- GO:0006506 GPI anchor biosynthetic process; GO:0034247 GPI-GnT complex; GO:0032366 intracellular sterol transport; GO:0006672 ceramide metabolic process; GO:0034976 response to endoplasmic reticulum stress; GO:0030968 endoplasmic reticulum unfolded protein response
- CL:0000540 neuron; CL:0000121 Purkinje cell; CL:0000775 neutrophil (for the GPI-anchor flow-cytometry assay system); CL:0000058 cardiac muscle myoblast / CL:0000746 cardiac muscle cell (cardiomyopathy)

---

## 7. Anatomical Structures Affected

**Organ level (primary):** Central nervous system — cerebrum, cerebellum (vermis atrophy prominent), corpus callosum (thinning), white matter (hypomyelination).
**Organ level (secondary/systemic):** Heart (dilated cardiomyopathy), eye/retina (retinal dystrophy, cortical visual impairment), ear (sensorineural hearing loss), skeletal system (scoliosis, skeletal dysplasia), gastrointestinal tract (reflux, feeding dysfunction — largely secondary to central hypotonia), respiratory system (recurrent aspiration pneumonia — secondary complication), liver (acute liver failure reported in one fatal case; causal link uncertain).

**Body systems involved:** Nervous system (primary); cardiovascular; ophthalmologic; auditory; musculoskeletal; digestive (secondary); respiratory (secondary complication).

**Tissue and cell level:**
- Neurons (cortical and cerebellar), with documented **Purkinje cell loss** on neuropathology [PMID:34017911]
- Skeletal muscle fibers (Type 1/Type 2 fiber ratio changes, lipid droplet accumulation) [PMID:27270415]
- Neutrophils and dermal fibroblasts (used as accessible surrogate tissues for GPI-anchor biochemical testing) [PMID:32165008; PMID:40378954]
- Cardiomyocytes (dilated cardiomyopathy)
- Retinal photoreceptors (retinal dystrophy)

**Subcellular level:** Endoplasmic reticulum (site of ARV1 localization and primary organelle dysfunction — ER stress, GPI-GnT complex assembly, sterol/ceramide accumulation); plasma membrane (site of reduced GPI-anchored protein display).

**Localization:** Bilateral, diffuse/symmetric cerebral and cerebellar involvement (no lateralization reported); seizures themselves are described as multifocal and "migrating," shifting between hemispheres rather than fixed laterality [PMID:34017911].

**Suggested UBERON/GO-CC terms:**
- UBERON:0000955 brain; UBERON:0002037 cerebellum; UBERON:0002298 brainstem; UBERON:0002037 cerebellar vermis; UBERON:0001133 corpus callosum white matter; UBERON:0000948 heart; UBERON:0000966 retina
- GO:0005783 endoplasmic reticulum; GO:0005886 plasma membrane

---

## 8. Temporal Development

**Onset:**
- Congenital/early neonatal prodrome (hypotonia, visual inattention) apparent within the first 4–8 weeks of life in most cases.
- Seizure onset: typically **4–7 months** of age (as low as 3 months, as late as 8 months reported) [OMIM #617020; PMID:34017911].
- Onset pattern: insidious neurodevelopmental impairment preceding an initially subacute/abrupt seizure onset (often first presenting as status epilepticus) [PMID:27270415].

**Progression:**
- **Disease stages:** (1) pre-seizure developmental impairment; (2) seizure onset with initial focal/multifocal epileptiform activity; (3) evolution to migrating focal seizures / modified hypsarrhythmia / myoclonic status; (4) progressive neurodegeneration with regression of any acquired skills, worsening spasticity/dystonia, progressive cerebral-cerebellar atrophy.
- **Progression rate:** Generally rapid and relentless in the most severe (null-allele) cases (death by 12 months in one reported case [PMID:27270415]); somewhat slower in others, with survival into the second and third decades reported in a minority (one patient alive at 21 years with severe residual disability and later-onset cardiomyopathy [PMID:35227294]; two sisters surviving to 4 and 9 years before death [PMID:34017911]).
- **Course pattern:** Progressive/neurodegenerative, punctuated by episodic seizure exacerbations (often fever-triggered) and intercurrent status epilepticus.
- **Duration:** Chronic and lifelong in survivors; disease is not self-limited.

**Patterns:**
- **Remission:** No spontaneous remission reported; the ketogenic diet produced **temporary partial seizure reduction** in two sisters (from daily seizures to "monthly clusters triggered by fever" for about 10 months), with subsequent deterioration/loss of effect by age 3 [PMID:34017911] — this is a treatment-induced partial response, not true remission.
- **Critical periods:** The first year of life (particularly months 3–8) represents the critical window in which the seizure disorder emerges and status epilepticus risk is highest; this is also plausibly the highest-yield window for early diagnosis and intervention (e.g., trial of ARV1-directed or GPI-pathway-directed therapy), though no such intervention window has been formally established in the literature.

---

## 9. Inheritance and Population

**Epidemiology:** DEE38 is an ultra-rare disorder. A 2025 review states that **only ~28 molecularly confirmed cases have been reported globally** [PMC12080507]; no formal population-based prevalence or incidence estimate exists in Orphanet/GBD-type sources (not retrievable in this session — flag for direct Orphanet/OMIM confirmation during curation, as a dedicated ORPHA code was not confirmed).

**Inheritance pattern:** Autosomal recessive (all reported cases; homozygous or compound heterozygous biallelic variants).

**Penetrance:** Appears complete/high for the core seizure/developmental phenotype among biallelic carriers reported to date (no asymptomatic biallelic carriers described), though ascertainment bias toward severe symptomatic cases in a rare, only recently molecularly characterized disorder must be considered.

**Expressivity:** Variable — phenotypic severity ranges from death in infancy (severe null alleles) to survival into adulthood with milder (but still profound) impairment; extra-neurological features (cardiomyopathy, retinal dystrophy, hearing loss, skeletal dysplasia) are variably present across families, suggesting variable expressivity possibly correlated with residual ARV1 activity (missense/splice/hypomorphic vs. complete null alleles).

**Genetic anticipation:** Not applicable/not reported (not a repeat-expansion disorder).

**Germline mosaicism:** Not specifically reported for ARV1.

**Founder effects:** Strongly suggested — recurrent alleles (e.g., p.Cys61Tyr, exon 2/exon 5 splice variants) reported repeatedly in consanguineous families from overlapping geographic/ethnic backgrounds (Middle Eastern, Iranian, Egyptian, South Asian cohorts in the literature reviewed) [PMC12103100; PMID:32165008; ScienceDirect Iranian family report].

**Consanguinity:** A dominant feature of nearly every reported pedigree; parental consanguinity is explicitly noted in the majority of case reports (Iranian family, Egyptian series, others) — reflecting the autosomal recessive, rare-allele nature of the disease.

**Carrier frequency:** Not established in population screening databases for this search session; likely to be population-specific and elevated in consanguineous founder populations, but should be verified against gnomAD during curation.

**Population demographics:**
- **Affected populations:** Case reports to date cluster in the Middle East/North Africa (Iran, Egypt, Qatar), and additional cases from Italy, France, Denmark, Canada, the US, and Australia (per multi-institutional collaborative series) [PMID:34296759] — consistent with a globally distributed but ascertainment-limited ultra-rare disorder, over-represented in consanguineous populations.
- **Geographic distribution of specific variants:** Recurrent alleles cluster regionally (see Founder effects above), though comprehensive geographic mapping data are not available.
- **Sex ratio:** No clear human sex-bias reported in the clinical literature (both sexes affected; e.g., two affected sisters in one family). Notably, the **mouse model shows a striking sex-dimorphic survival defect** (females far worse-affected than males) that has not yet been correlated with any human sex-difference signal [PMID:27270415].
- **Age distribution:** All reported patients are infantile-onset; documented survivors range from death at 12 months to survival to 21 years of age.

---

## 10. Diagnostics

**Laboratory tests:** Elevated alpha-fetoprotein reported in some cases (verify primary source); no specific ARV1 biomarker in routine clinical chemistry.

**Biomarkers (research-grade):**
- Flow cytometric assessment of **GPI-anchored surface proteins on neutrophils and fibroblasts** (CD16, CD59, CD66b, CD87/uPAR, CD73, CD109) and **FLAER binding** — used as functional biomarkers of GPI-anchor synthesis deficiency, analogous to the diagnostic workup used for PNH and other inherited GPI deficiencies [PMID:32165008; PMID:40378954].

**Imaging studies (MRI, the primary imaging modality used):**
- Thin corpus callosum (early infancy)
- Progressive cerebral atrophy (often with regional/temporal predominance)
- Cerebellar atrophy, particularly of the **vermis**
- Hypomyelination
- Small hippocampus reported in one case [PMID:34017911]
These neuroimaging features are explicitly noted to overlap substantially with the inherited GPI-deficiency disorder group (PIGA/PIGN/PIGT-CDG).

**Electrophysiology:**
- **EEG** is central to diagnosis and monitoring: serial EEG shows an evolution from normal background → focal epileptiform discharges → multifocal spikes/waves → modified hypsarrhythmia or subcontinuous high-amplitude multifocal spike-wave activity with myoclonic status patterns [PMID:27270415; PMID:34017911].
- No specific EMG/nerve conduction or ECG diagnostic criteria are described beyond routine cardiac workup prompted by clinical suspicion of cardiomyopathy.

**Biopsy/pathology findings:**
- Quadriceps **muscle biopsy**: increased Type 1:Type 2 fiber ratio, smaller Type 2 fibers, lipid droplets adjacent to clumped mitochondria on electron microscopy [PMID:27270415].
- **Postmortem neuropathology:** diffuse cerebellar atrophy with severe and diffuse Purkinje cell loss [PMID:34017911].

**Genetic testing:**
- **Whole-exome sequencing (WES)** is the diagnostic modality used in essentially all reported cases and is described in the literature as the practical gold-standard approach for this ultra-rare disorder, covering "85% of disease-causing mutations" typically found in coding regions [PMC12080507].
- No ARV1-specific single-gene panel or targeted gene panel is described as standard; ARV1 should be included in **DEE/epileptic encephalopathy gene panels** and specifically considered in the differential of **epilepsy of infancy with migrating focal seizures (EIMFS)** and in the **inherited GPI deficiency disorder** gene panel alongside PIGA, PIGN, PIGT, PIGO, PGAP1, PGAP2, PGAP3, etc. [Neurology Genetics 2021].
- Chromosomal microarray, karyotyping, FISH, mitochondrial DNA testing, and repeat-expansion testing are not specifically indicated for ARV1-DEE38 (no chromosomal-scale or repeat-expansion mechanism identified) but may be part of a standard first-tier DEE diagnostic workup before/alongside WES.

**Omics-based diagnostics:** Not part of routine clinical diagnosis; flow cytometric GPI-anchor protein assays function as a confirmatory functional test analogous to a "diagnostic omics" biomarker in research/reference laboratory settings.

**Clinical criteria:** No formal consensus diagnostic criteria (DSM/ICD-specific) exist for DEE38 specifically; diagnosis rests on the combination of (1) clinical phenotype (early infantile refractory multifocal seizures + severe global developmental impairment ± the extra-neurologic features above) and (2) molecular confirmation of biallelic ARV1 variants.

**Differential diagnosis:** Other inherited GPI deficiency disorders (PIGA-CDG/EIEE2, PIGN, PIGT, PIGO, PIGQ-related disorders); other EIMFS-causing genes (KCNT1, SCN2A, SCN8A, PLCB1, SLC25A22, QARS1, TBC1D24); other early infantile DEEs more broadly (STXBP1, CDKL5, KCNQ2).

**Screening:** No population-based or newborn screening program exists for ARV1/DEE38 given its ultra-rarity; carrier screening/cascade testing in consanguineous families with a known proband variant is the relevant practical screening application.

---

## 11. Outcome/Prognosis

**Survival/mortality:** Prognosis is generally poor. Reported outcomes range from death at **12 months** (most severe reported case, from intractable seizures and aspiration pneumonia [PMID:27270415]) to death at **4 years 2 months** and **9 years** (two sisters, both from bronchopneumonia during status epilepticus/intercurrent infection [PMID:34017911]) to survival to **21 years** with profound residual disability and later-onset dilated cardiomyopathy [PMID:35227294]. No formal actuarial 5-year/10-year survival statistics exist given the small number of reported cases; the disorder should be regarded as carrying a substantial risk of premature death, predominantly from **aspiration pneumonia/respiratory infection in the context of refractory status epilepticus**.

**Morbidity/function:** Uniformly severe and largely irreversible — profound intellectual disability, absence of ambulation, absent or minimal expressive language, dependence for all activities of daily living in essentially all reported survivors.

**Complications:** Recurrent aspiration pneumonia, sepsis, status epilepticus (both convulsive and myoclonic), acute liver failure (reported once, causal link uncertain), progressive scoliosis, dilated cardiomyopathy (which itself carries independent mortality risk from heart failure).

**Recovery potential:** Essentially none reported with current standard-of-care antiseizure medications; partial, temporary benefit reported only from the **ketogenic diet** in one family (see below), with eventual loss of effect.

**Prognostic factors:** Variant severity (complete-null vs. hypomorphic alleles) appears to correlate loosely with survival — patients with the most complete loss-of-function alleles and earliest, most severe seizure onset have the shortest survival, while patients with partial-function (splice/hypomorphic) alleles have survived longer with somewhat milder (though still severe) phenotypes. No validated prognostic biomarker exists.

---

## 12. Treatment

**Pharmacotherapy:** No disease-modifying or ARV1-specific pharmacotherapy exists. Symptomatic antiseizure drug (ASD) therapy is uniformly attempted but the disorder is characteristically **pharmacoresistant**. Agents trialed across reported cases (individually or in combination), largely with limited or no lasting benefit: valproate, phenobarbital, phenytoin, ethosuximide, levetiracetam, carbamazepine, vigabatrin, topiramate, lacosamide, diazepam/benzodiazepines, and hydrocortisone (ACTH-type approach) [PMID:34017911; PMC12103100].
- Suggested NCIT term: `NCIT:C15986` Pharmacotherapy (generic), with `therapeutic_agent` bindings to individual ASDs (e.g., CHEBI terms for levetiracetam, valproate, phenobarbital, vigabatrin, topiramate, lacosamide, phenytoin).

**Pharmacogenomics:** No ARV1-specific pharmacogenomic guidance has been established.

**Advanced therapeutics (experimental/preclinical):**
- **Gene therapy proof-of-concept:** Lentiviral transduction of wild-type ARV1 cDNA into patient-derived fibroblasts successfully **rescued the GPI-anchored protein cell-surface deficiency**, demonstrating cellular reversibility of the core molecular defect and establishing a rationale for future ARV1 gene-replacement therapy [PMID:34296759]. This remains preclinical (cell-based) only — no in vivo or clinical gene-therapy trial has been reported.
- Suggested NCIT term for this modality when curating: `NCIT:C15238` Gene Therapy; `therapeutic_modality: GENE_THERAPY`.

**Dietary/metabolic intervention:**
- **Ketogenic diet** produced a documented, though temporary, reduction in seizure frequency in two sisters — from multiple seizures/day to monthly fever-triggered clusters for ~10 months in one patient, with a milder transient benefit in her sister — before eventual loss of efficacy and disease progression [PMID:34017911].
- Suggested NCIT term: `NCIT:C15447` Dietary Intervention.

**Surgical/interventional:** Not applicable/not reported (no epilepsy surgery candidacy given the diffuse, multifocal seizure pattern); **gastrostomy tube placement** is used supportively for feeding difficulties/aspiration risk (`NCIT:C15747` Supportive Care or a specific enteral feeding procedure term).

**Supportive/rehabilitative care:** Multidisciplinary supportive management is emphasized throughout the literature as the mainstay of care — including nutritional support (gastrostomy), respiratory/aspiration precaution management, physical/occupational/speech therapy for symptomatic management of hypotonia/spasticity, and genetic counseling for families [PMC12080507].
- Suggested NCIT terms: `NCIT:C15302` Physical Therapy; `NCIT:C15240` Genetic Counseling.

**Experimental/clinical trials:** No ARV1-specific registered clinical trials (ClinicalTrials.gov) were identified in this search.

**Treatment outcomes:** As above — despite pharmacologic and dietary intervention, "neurodevelopmental outcomes often remain poor" even when partial seizure control is achieved [PMC12080507, citing case-series literature].

**Treatment strategy/algorithm:** No formal published treatment algorithm exists; management follows general refractory-DEE/EIMFS principles (sequential/combination ASD trials, early consideration of ketogenic diet, avoidance/aggressive management of febrile triggers, proactive aspiration/respiratory precautions) rather than an ARV1-specific protocol.

**Personalized medicine:** The demonstrated in vitro rescue of GPI-anchoring defects by ARV1 gene replacement [PMID:34296759] represents the most concrete precision-medicine lead in the current literature, though it has not progressed beyond patient-cell experiments.

---

## 13. Prevention

- **Primary prevention:** No vaccination or population-level primary prevention exists (monogenic recessive disorder). The only actionable primary-prevention lever identified in the literature is **genetic counseling regarding consanguinity and recurrence risk** in families with a known or suspected ARV1 pathogenic variant.
- **Secondary prevention:** **Carrier screening and prenatal/preimplantation genetic testing** are the relevant options once a familial ARV1 variant is identified, particularly given the strong consanguinity association in reported pedigrees; no population-based newborn screening program exists for this ultra-rare condition.
- **Tertiary prevention:** Aggressive **management of febrile illness and infection** (given documented fever-triggered status epilepticus and infection as the leading cause of death), proactive **aspiration precautions**, and early recognition/monitoring for the extra-neurologic complications of the phenotype (baseline and serial echocardiography for cardiomyopathy surveillance, ophthalmologic and audiologic screening, scoliosis monitoring) are the most concrete tertiary-prevention measures supported by the case literature.
- **Immunization:** No disease-specific vaccine strategy; standard childhood immunization plus attention to respiratory pathogen prevention (e.g., RSV prophylaxis, influenza/pneumococcal vaccination where age-appropriate) is a reasonable extrapolation given the infection-driven mortality pattern, though not explicitly studied in ARV1-DEE38.
- **Genetic counseling:** Central to family management — explicit recommendation in the literature that "ARV1 should be considered in the genetic screening of individuals with EIMFS" [Neurology Genetics 2021], with downstream implications for reproductive counseling in affected families.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** No naturally occurring ARV1-deficient disease has been reported in companion animals or wildlife (NCBITaxon — not applicable beyond the engineered mouse model below).
- **Orthologous gene:** ARV1 is highly conserved from yeast (*Saccharomyces cerevisiae* ARV1, "ARE2-required for viability 1") through mouse (*Arv1*) to human, with human ARV1 fully complementing yeast *arv1Δ* phenotypes in classic complementation assays [PMID:27270415 and cited yeast literature].
- **Comparative biology:** The yeast-to-human functional conservation of both the sterol-trafficking role and, by extension, contribution to GPI-anchor biosynthesis machinery underlies much of the current mechanistic model; this conservation was directly exploited experimentally (patient variant rescue assays performed in yeast).
- **Zoonotic potential / transmission:** Not applicable — ARV1-DEE38 is a purely genetic (non-infectious, non-transmissible) disorder.

---

## 15. Model Organisms

**Mouse (primary in vivo model):**
- **Neuronal-specific Arv1 knockout mouse** (Palmer et al., 2016) is the principal validated in vivo model. It recapitulates the core human phenotype: spontaneous **generalized tonic-clonic seizures** beginning after 12 weeks of age, **circling behavior and hyperactivity**, reduced body weight and white adipose tissue mass, skeletal-muscle fiber-type shifts, and a pronounced **sex-dimorphic survival defect** (33% female survival vs. 80% male survival to 20 weeks, p=0.0053) [PMID:27270415].
- **Applications:** Used to establish causality between neuronal ARV1 loss and the seizure/survival phenotype, and as the platform demonstrating that human ARV1 patient variants fail functional rescue.
- **Limitations:** The pronounced sex-dimorphism in the mouse model has no established human correlate; the mouse model does not obviously recapitulate the human extra-neurological features (cardiomyopathy, retinal dystrophy, hearing loss) reported in some human patients — these organ systems do not appear to have been systematically examined in the knockout mouse in the retrieved literature.

**Yeast (*Saccharomyces cerevisiae*):**
- The original and still mechanistically foundational model system for ARV1 function — used to define its role in sterol trafficking, sphingolipid/ceramide metabolism, and (via genetic and biochemical experiments) contribution to GPI-anchor biosynthesis. Human patient ARV1 variants have been functionally tested via yeast complementation/temperature-sensitive rescue assays [PMID:27270415].

**Human cell-based models:**
- Patient-derived **dermal fibroblasts** and **neutrophils** are used as the primary "model system" for confirmatory functional/biochemical testing (GPI-anchored protein flow cytometry) and for the lentiviral gene-rescue proof-of-concept experiment [PMID:32165008; PMID:34296759; PMID:40378954].
- **HEK293 ARV1-knockout cells** and **in vitro-reconstituted GPI-GnT enzyme assays** were used in the most recent (2025) mechanistic study to directly demonstrate ARV1's biochemical role within the GPI-GnT complex [PMID:40378954].

**Resources:** No dedicated ARV1/DEE38 entries were confirmed in MGI, IMPC, or veterinary (OMIA) databases within this search session; the Palmer et al. 2016 conditional neuronal knockout appears to be a custom, non-commercially-catalogued line rather than a broadly distributed IMPC/KOMP allele — verify directly in MGI during curation if a stable allele ID is needed.

---

## Summary Table: Key Primary Citations

| Citation | Contribution |
|---|---|
| PMID:27270415 (Palmer et al. 2016, *Hum Mol Genet*) | First description linking ARV1 to human DEE; neuronal knockout mouse model |
| PMID:32165008 (2020) | First direct biochemical evidence of GPI-anchor synthesis deficiency in patient cells; two splice-variant families |
| PMID:34017911 (2021, *Neurology Genetics*) | Expands phenotype to EIMFS/migrating focal seizures + myoclonic status; proposes ER-stress/GPI-deficiency-disorder framework; ketogenic diet response data |
| PMID:34296759 (2021) | Genotype-phenotype refinement across 7 patients; lentiviral gene-therapy rescue proof-of-concept |
| PMID:35227294 (2022) | Establishes dilated cardiomyopathy as part of the ARV1 phenotype spectrum |
| Neurogenetics 2020 (10.1007/s10048-020-00615-4) | p.Gly189Arg family; further mechanistic GPI-synthesis discussion |
| PMC12103100 / Cureus (2025) | Three additional pediatric cases (Egypt); novel p.Phe144Argfs*5 variant; fatal liver-failure outcome |
| Springer J Rare Dis (2025), 10.1007/s44162-025-00066-1 | Novel p.Gln62Ter variant |
| ScienceDirect (2021), S2214540021001043 | Iranian consanguineous family, novel homozygous variant |
| PMID:40378954 (2025) | Defines ARV1 as a structural/functional component of the GPI-GnT enzyme complex (mechanistic capstone paper) |
| OMIM #617020 | Authoritative clinical synopsis and gene-disease relationship record |

**Notes on gaps for curation:** A dedicated MONDO ID, Orphanet ORPHA code, and gnomAD constraint metrics (pLI/LOEUF) for ARV1 could not be directly confirmed via the sources accessible in this session (OMIM and Orphanet pages returned access-blocked/403 responses); these should be resolved directly against MONDO/Orphanet/gnomAD during formal knowledge-base curation rather than inferred from this report. The mechanistic step linking GPI-anchor/ER-stress dysfunction specifically to neuronal excitability (step 6 in the causal chain above) is explicitly flagged by the primary authors themselves as inferential/hypothesized rather than directly demonstrated in human or mouse neurons.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 9 |
| On topic | 9 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:34017911` *(abstract only)*: "severe and diffuse loss of Purkinje cells"
  - closest text in source: "CONCLUSIONS: This report confirms that biallelic ARV1 mutations cause a severe form of DEE and adds epilepsy with migrating focal seizures and myoclonic status to the spectrum of epilepsy phenotypes"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 50 |
| Resolved | 50 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.