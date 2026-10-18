---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-15T20:02:11.183438'
end_time: '2026-10-15T20:03:15.723906'
duration_seconds: 64.54
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Long QT Syndrome 10
  mondo_id: MONDO:0012737
  category: Genetic
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
  - claude-haiku-5-5
  - claude-sonnet-5-5
  web_search_requests: 3
  num_turns: 5
  total_cost_usd: 0.7906832000000001
  session_id: 1411d6e0-a3a9-57ef-a642-a756ff0785bd
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 5
reference_validation:
  total_references: 3
  verified: 3
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 3
  on_topic: 3
  validator_version: 0.3.0
term_validation:
  total_terms: 13
  verified: 13
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 6
  labels_matching: 5
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Long QT Syndrome 10
- **MONDO ID:** MONDO:0012737 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Long QT Syndrome 10** covering all of the
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

I'll check the key claims against live sources before writing the report.

# Long QT Syndrome 10 (LQT10; SCN4B): Research Report

**Method and confidence.** I checked the core claims with web searches. They covered the discovery paper (Medeiros-Domingo 2007), the ClinGen-framework reappraisal (Adler 2020), and the mouse modifier data (Remme 2009). I did not retrieve full text of most papers. Items I did not verify are marked **[unverified]**. Please confirm any PMID marked that way, and run `just fetch-reference` on every PMID before it is used as evidence. Every CURIE below is a suggestion from memory and must be looked up before binding.

**Bottom line.** LQT10 is a disputed gene–disease entity. The only LQTS evidence is a single four-generation family with the SCN4B p.L179F variant. ClinGen-framework curation (Adler 2020) rated SCN4B as having limited or disputed evidence for congenital LQTS. A dismech entry should state this, and should not present LQT10 as an established Mendelian LQTS subtype.

---

## 1. Disease Information

- **Overview.** LQT10 is a proposed rare, autosomal dominant long QT syndrome attributed to heterozygous variants in *SCN4B*. That gene encodes the auxiliary β4 subunit of voltage-gated sodium channels. The original report described a "gain-of-function" increase in late sodium current (I_Na,L), which makes the phenotype LQT3-like.
- **Identifiers.**
  - MONDO:0012737 (from the template).
  - OMIM: LQT10 is phenotype MIM 611819 **[unverified]**. The gene entry is OMIM *608256 (confirmed in search results).
  - SCN4B is located at 11q23.3.
  - HGNC ID for SCN4B: look up the `hgnc:` CURIE. I believe it is hgnc:10592 but have not confirmed it.
  - Orphanet and ICD-10/11: not checked. Long QT syndrome in general is ICD-10 I45.81.
- **Synonyms.** LQT10, LQTS10, long QT syndrome 10, SCN4B-related long QT syndrome.
- **Data source.** The evidence is aggregated from a single published family. It does not come from EHR data.

## 2. Etiology

- **Causal factor.** A heterozygous missense variant in *SCN4B*, p.L179F (Leu179Phe), at a conserved residue.
  - Medeiros-Domingo et al. studied a 4-generation Mexican mestizo family with sudden death. Family members had no mutation in the nine LQTS genes known at the time.
  - The variant segregated with the phenotype with **incomplete penetrance**.
  - It was absent from 800 control alleles.
  - Source: Medeiros-Domingo et al., Circulation 2007;116:134-142, PMID:17592081 ([search summary](https://pmc.ncbi.nlm.nih.gov/articles/PMC3332546); PMC author manuscript PMC3332546).
- **Index case.** A girl found at 21 months with asymptomatic bradycardia, QTc 712 ms and intermittent 2:1 AV block (secondary summary of the paper; full text not read).
- **Genetic risk factors beyond L179F.** None are established for LQTS. SCN4B variants have also been reported in atrial fibrillation (ATFB17, Li et al. 2013, two Han Chinese families; see the OMIM summary). SIDS and other reports exist **[unverified]**.
- **Environmental risk factors.** None are specific to LQT10. Generic QT-prolonging drugs and electrolyte disturbances (hypokalemia, hypomagnesemia) are expected modifiers in any LQTS, but I found no LQT10-specific evidence.
- **Protective factors and gene–environment interactions.** None reported.
- **Modifier role.** Remme et al., Circ Res 2009 **[PMID unverified]**, found a marked reduction in *Scn4b* mRNA in the 129P2 mouse strain versus FVB/N. The 129P2 strain has more severe conduction slowing in a mouse model of an SCN5A mutation. The authors proposed SCN4B as a potential genetic modifier of conduction and sodium channel disease. This is correlational and does not show an LQTS mechanism.

## 3. Phenotypes

Only one family supports these, so no population frequencies exist. Treat all frequencies as unavailable.

| Phenotype | Suggested HPO | Notes |
|---|---|---|
| Prolonged QT interval | HP:0001657 | The proband's QTc was 712 ms. |
| Sinus bradycardia | HP:0001688 | Reported in the proband. |
| 2:1 atrioventricular block | look up (AV block is HP:0001678) | Intermittent, in the proband. |
| Sudden cardiac death | HP:0001645 | Family history. |
| Syncope | HP:0001279 | Typical of LQTS; I did not confirm it in this family. |

- **Onset.** The proband presented in infancy. Penetrance was incomplete.
- **Quality-of-life data.** None found.

## 4. Genetic and Molecular Information

- **Gene.** *SCN4B* (protein Navβ4, UniProt: look up). It is a single-pass transmembrane protein with an extracellular Ig-like domain and a short cytoplasmic tail.
- **Variant.** NP p.L179F, a missense change, heterozygous and germline. ACMG/AMP classification: given the ClinGen-framework dispute, it should not be treated as an established pathogenic variant. I did not look up its ClinVar status or gnomAD frequency.
- **Functional effect.** In HEK293 cells, L179F-β4 increased late sodium current about 8-fold compared with SCN5A alone, and about 3-fold compared with SCN5A plus wild-type β4 (search summary of the abstract, PMID:17592081). Suggested `functional_impact_category`: because the mechanism is an altered auxiliary subunit, not a mutated pore-forming channel, check whether this is best recorded as a `modifier` on a process or as a variant-level category. The paper reports an increased late current.
- **ClinGen-framework gene-disease validity.**
  - Adler et al., Circulation 2020, PMC7017940: Of 17 genes reappraised, only *KCNQ1*, *KCNH2* and *SCN5A* were definitive for typical LQTS. Nine genes, including *SCN4B*, had limited or disputed evidence. The reviewers said they lacked significant segregation of the suspected variant in multiple affected cases beyond chance.
  - I did not see the exact tier for SCN4B (Limited versus Disputed). Run `just fetch-reference` for the CGGV assertion and copy the tier, as the repository's rules require. Do not assign one.
- **Epigenetics and chromosomal abnormalities.** None reported.

## 5. Environmental Information

No environmental, lifestyle or infectious factors are specific to LQT10. Generic LQTS triggers (QT-prolonging drugs, hypokalemia) are expected to apply, but I found no source for them in this disease.

## 6. Mechanism / Pathophysiology

Ordered causal chain, as proposed in the original report:

1. A heterozygous *SCN4B* L179F substitution alters the Navβ4 subunit. This is demonstrated by sequencing and segregation.
2. The altered β4 subunit interacts with the Nav1.5 (SCN5A) channel in a way that increases late sodium current (I_Na,L). This is demonstrated in HEK293 heterologous expression only. It has not been shown in cardiomyocytes.
3. Persistent inward sodium current during the plateau phase prolongs the ventricular action potential. This is inferred from the LQT3 analogy.
4. Prolonged repolarization appears on the ECG as QT prolongation. This is demonstrated in the proband.
5. Prolonged repolarization predisposes to early afterdepolarizations and torsades de pointes, and so to syncope and sudden death. This is inferred. Sudden death is reported in the family.
6. Branch: bradycardia and 2:1 AV block were reported in the proband. Whether this is a repolarization effect or a separate conduction effect is not established.

- **Suggested GO terms** (look up before use): regulation of sodium ion transmembrane transport; cardiac muscle cell action potential; regulation of ventricular cardiac muscle cell membrane repolarization. **Cell type:** cardiac muscle cell, ventricular cardiac muscle cell (CL:0000746 and CL:0002129, to verify).
- **Cellular compartment:** plasma membrane, intercalated disc.
- **Molecular profiling, single-cell or CRISPR data:** none found.
- **Why the mechanism is uncertain.** The ClinGen-framework reviewers found the genetic evidence for causality insufficient. The functional result may show that L179F alters sodium current without proving that this causes LQTS in humans.

## 7. Anatomical Structures Affected

- **Primary organ:** heart (UBERON:0000948), specifically ventricular myocardium and the conduction system.
- **Body system:** cardiovascular.
- **Lateralization:** not applicable.
- **Subcellular site:** sarcolemma, where the Nav1.5–β4 complex sits.

## 8. Temporal Development

Infantile presentation in the single reported proband. Penetrance was incomplete, so some carriers were unaffected. There is no stage or progression data and no natural-history study.

## 9. Inheritance and Population

- **Inheritance:** autosomal dominant (HP:0000006) with incomplete penetrance (HP:0003829), per the single family.
- **Prevalence and incidence:** not estimable. There is one reported family. Record `prevalence_class: NOT_YET_DOCUMENTED` or `CASES_IN_LITERATURE`.
- **Founder effect, consanguinity, sex ratio, carrier frequency:** not reported.
- **Population:** the family was Mexican mestizo.

## 10. Diagnostics

- **ECG.** Prolonged QTc and bradycardia or AV block (the proband's QTc was 712 ms).
- **Genetic testing.** *SCN4B* is on some research and commercial LQTS panels. Under the Adler 2020 conclusions, variants in it should not be used for clinical decision-making without new genetic evidence. I did not retrieve GTR or guideline statements.
- **Differential diagnosis.** LQT1–3 (*KCNQ1*, *KCNH2*, *SCN5A*), the definitive genes, and acquired QT prolongation from drugs or electrolytes.
- **Biopsy, imaging, omics, and screening recommendations:** none specific.

## 11. Outcome / Prognosis

No outcome data exist beyond the sudden deaths in the family history. Survival, QoL and prognostic factors are not available.

## 12. Treatment

No LQT10-specific trials or evidence were found. By analogy to LQT3, a sodium channel blocker such as mexiletine and β-blockade are used, but this is **not demonstrated for LQT10**. Do not curate it as an LQT10 treatment without a source. Generic LQTS options are beta-blockers, left cardiac sympathetic denervation and ICD placement. Suggested NCIT terms, to be looked up: Pharmacotherapy (NCIT:C15986) and Surgical Procedure (NCIT:C15329). Note that NCIT:C15986 is the generic action and the specific drug goes in `therapeutic_agent`.

## 13. Prevention

Cascade genetic testing and counseling for relatives of the proband, and avoidance of QT-prolonging drugs, are standard LQTS practice. They are not supported by LQT10-specific data. Because SCN4B pathogenicity is disputed, counselling should say so.

## 14. Other Species / Natural Disease

No naturally occurring disease was found. I did not check OMIA.

## 15. Model Organisms

- **Mouse.** I found no *Scn4b* knockout or knock-in mouse that models LQT10. The one cardiac mouse result is the Remme 2009 strain comparison above, which is correlational.
- **Other work (not verified).** Grieco et al. (Neuron 2005) showed that the β4 cytoplasmic tail causes open-channel block, a mechanism for resurgent sodium current. I only confirmed the title. That paper is not a cardiac model. The resurgent-current mechanism is a possible link to late current, but this is speculative.
- **Cell models.** HEK293 co-expression of SCN5A with wild-type or L179F β4 is the only functional model identified. There is no iPSC-cardiomyocyte model that I found.

---

## Key recommendations for the dismech entry

1. Describe the gene–disease relationship as disputed or limited, citing Adler 2020, and copy the ClinGen tier from the source record. Do not assign one.
2. Keep the pathophysiology confined to what the 2007 paper shows (heterologous late current), and label the cardiomyocyte mechanism as inferred.
3. Add a `KNOWLEDGE_GAP` discussion: no second family, no cardiomyocyte or animal model, and no treatment data.
4. Use `evidence_source: IN_VITRO` for the HEK293 data and `HUMAN_CLINICAL` for the pedigree.

## Sources

- [Medeiros-Domingo et al., Circulation 2007 (PMID 17592081); PMC author manuscript](https://pmc.ncbi.nlm.nih.gov/articles/PMC3332546)
- [OMIM *608256, SCN4B](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/608256)
- [Adler et al., Circulation 2020, reappraisal of LQTS genes (PMC7017940)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7017940)
- [Healio summary of Adler 2020](https://www.healio.com/news/cardiology/20200203/many-genes-reportedly-tied-to-long-qt-syndrome-have-weak-evidence)
- [Channelpedia record for Remme 2009 (Scn4b as modifier)](https://channelpedia.epfl.ch/pubmeds/131651)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 3 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 3 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 6 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 1 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0000948` (1 mention) - the report calls it "Primary organ:** heart"; UBERON calls it **heart**, and lists "branchial heart" among its other names

Every term resolved, and every label the report gave matched.