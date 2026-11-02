---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-15T15:42:56.490021'
end_time: '2026-10-15T15:44:53.255149'
duration_seconds: 116.77
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: RNU5B-1 Related Neurodevelopmental Disorder With Seizures And Joint
    Laxity
  mondo_id: MONDO:1060179
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
  - claude-haiku-5-5
  - claude-sonnet-5-5
  web_search_requests: 3
  num_turns: 11
  total_cost_usd: 0.8071871999999998
  session_id: d98baee9-c229-5d8a-96f8-a4aee10f9c40
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 7
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 0
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMC:PMC12165836
  relevance_assessed: 6
  on_topic: 5
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 2
  verified: 2
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 1
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** RNU5B-1 Related Neurodevelopmental Disorder With Seizures And Joint Laxity
- **MONDO ID:** MONDO:1060179 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **RNU5B-1 Related Neurodevelopmental Disorder With Seizures And Joint Laxity** covering all of the
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

Try the PMC version of the Nava paper.

# RNU5B-1-Related Neurodevelopmental Disorder with Seizures and Joint Laxity (NEDSJL): Research Report

**Scope and reliability.** This is a very recent, rare, non-coding-gene disorder. I read two primary papers directly. I could not open the OMIM pages (HTTP 403), so OMIM details come only from search-result summaries and are marked "unverified". Most template sections (environment, protective factors, treatment, models and so on) have no disease-specific literature, and I say so. I did not run the prescribed ontology-term lookups. Every HPO, GO, CL, UBERON and NCIT ID below is a suggested name only, not a validated CURIE. Look each one up before binding it.

**Important discrepancy.** The disease name, from OMIM, includes "joint laxity". The two primary papers I could read do not clearly report joint hypermobility in RNU5B-1 carriers. In Nava et al., hypermobility appears only in the RNU4-2 cohort. Jackson et al. do not mention it in the text I could access. The OMIM clinical synopsis may draw on the supplementary tables or on unpublished data, and I could not check it. A curator should check the OMIM entry text and the supplements before asserting hypermobility or "seizures" as high-frequency features.

## 1. Disease Information

- **Overview.** NEDSJL is an autosomal dominant neurodevelopmental disorder. It is caused by de novo heterozygous variants in *RNU5B-1*, which encodes one of the paralogs of U5 small nuclear RNA, a core component of the major spliceosome. The variants cluster in the highly conserved loop I of U5 (about n.30–n.50). The main features are global developmental delay or intellectual disability, hypotonia, macrocephaly or other head-size abnormality, failure to thrive, and brain MRI abnormalities.
- **Identifiers.**
  - OMIM phenotype #621302 (NEDSJL) and OMIM gene *621090 (RNU5B-1). These come from search-result titles and are unverified in full. See [OMIM 621302](https://omim.org/entry/621302) and [OMIM 621090](https://omim.org/entry/621090).
  - MONDO:1060179 was supplied in the request. I did not independently confirm it.
  - Orphanet, ICD and MeSH: not found.
- **Synonyms.** Neurodevelopmental disorder with seizures and joint laxity; NEDSJL; RNU5B-1-related neurodevelopmental disorder.
- **Source of data.** The data are individual-level, from clinical sequencing cohorts. These are the UK 100,000 Genomes Project (100KGP), a French rare-disease cohort and international collaborators. There is no aggregate registry.

## 2. Etiology

- **Cause.** Heterozygous, mostly de novo, variants in *RNU5B-1* on 15q22 (n. positions on ENST00000363286.1). The constrained region is n.30–n.50.
- **Origin of the variants.** In Nava et al., phased loop I variants arose mostly on the maternal allele. Five of seven phaseable loop I variants were maternal: n.39C>G, n.42_43insA and three n.44A>G ([PMC12165858](https://pmc.ncbi.nlm.nih.gov/articles/PMC12165858/)). Jackson et al. likewise report that n.39_40insT "is highly likely to have arisen on the maternal allele" ([PMC12165836](https://pmc.ncbi.nlm.nih.gov/articles/PMC12165836)).
- **Risk and protective factors.** None identified. Searches turned up no data on environmental, protective or gene–environment factors. Jackson et al. found *RNU5B-1* by looking for R-loop-forming regions with de novo variants, which concerns where mutations arise, not an environmental risk factor.

## 3. Phenotypes

Clinical data are sparse, and the figures below mix two papers with overlapping individuals.

| Phenotype | Evidence | Suggested HPO (verify) |
|---|---|---|
| Global developmental delay / intellectual disability | Of nine RNU5B-1 patients with detailed data, six had severe delay, one moderate, and one normal cognition with attention difficulties (Nava). In Jackson, GDD had OR 22.1. | Global developmental delay (HP:0001263); Intellectual disability |
| Generalized hypotonia | Jackson: OR 37.3, P = 7.4×10⁻⁵ vs rare-disease probands | Generalized hypotonia |
| Macrocephaly | Jackson: OR 30.6. Nava: macrocephaly in two n.39C>G carriers. | Macrocephaly |
| Acquired microcephaly | Nava: three n.44A>G carriers | Acquired microcephaly |
| Failure to thrive | Jackson: OR 24.7 | Failure to thrive |
| Brain MRI abnormality | Nava: all 9 patients | Abnormal brain MRI |
| Seizures | Nava: "All nine patients showed brain MRI abnormalities, but only one had epilepsy." Jackson also describes seizures among the five individuals with detailed data. | Seizure |
| Pectus excavatum | Nava: 3 of 9, two also marfanoid | Pectus excavatum; Marfanoid habitus |
| Eye abnormalities | Jackson: OR 18.7. Nava: 3 patients. | Abnormality of the eye |
| Other malformations | Nava: pulmonary (2), sacrococcygeal (2), tooth agenesis or fusion (2), cardiac (2) | |
| Joint hypermobility | Named in the disease title via OMIM; not reported for RNU5 patients in Nava. Unverified. | Joint hypermobility |

- **Onset and course.** Developmental from infancy. Progression, quality of life and age-specific frequencies are not reported.
- **Possible allele-specific head-size effects.** Nava propose that variant-specific effects could explain opposing head-growth phenotypes (macrocephaly with n.39C>G, acquired microcephaly with n.44A>G). They state larger studies are needed to confirm this.
- **OMIM numbers I could not verify.** One search summary said OMIM lists epilepsy in 4, motor delay in 4, joint hypermobility in 4 and autism in 3. That conflicts with the one-in-nine epilepsy figure from Nava, possibly because the cohorts differ. Treat it as unverified.

## 4. Genetic/Molecular Information

- **Gene.** *RNU5B-1* (HGNC symbol RNU5B-1; look up the HGNC ID, which I did not retrieve). It is one of five U5 snRNA paralogs. *RNU5A-1* is a related candidate gene.
- **Variants** (n. numbering on ENST00000363286.1):
  - Recurrent loop I variants: n.39C>G, n.42_43insA, n.44A>G. Nava classify all three as likely pathogenic.
  - Single or rare variants: n.37G>C, n.39_40insT, and others outside loop I (n.24G>C, n.74T>C; paternal in Nava, unclear significance).
  - Variants of doubtful relevance: n.100C>G (the carrier had an alternative diagnosis), n.59G>C (also in three unaffected 100KGP participants), n.39C>T (three gnomADv4 individuals).
  - Jackson reports nine individuals with rare variants in the constrained region. Nava report 18 NDD probands with de novo RNU5B-1 variants, 17 of them in the critical region. Together with RNU5A-1, that makes 21 individuals.
  - Jackson's table lists n.39_40insT and n.37G>C and does not list n.39C>G, while Nava's lists n.39C>G; the two papers may use different numbering or overlapping patients. I did not reconcile them.
- **Mechanism class.** Non-coding RNA variants of a likely dominant-negative or altered-function type. This is inferred, not shown directly.
- **Variant frequency.** The constrained region is depleted of variants in gnomADv4.
- **Origin.** Germline, de novo.
- **Epigenetic and chromosomal features.** None reported.

## 5. Environmental Information

No environmental, lifestyle or infectious factors are reported.

## 6. Mechanism / Pathophysiology

**Causal chain** (steps 3 to 6 are inferred rather than demonstrated for RNU5B-1):

1. A de novo heterozygous variant arises, often on the maternal allele, in the loop I region of *RNU5B-1*. The region was identified through R-loop-forming-region analysis (Jackson).
2. The variant changes the sequence of U5 snRNA loop I. The sequence is invariantly conserved and binds and aligns exons during splicing.
3. In the spliceosome, altered loop I disrupts exon alignment. Nava note that "U5 loop I is crucial for 5′SS transfer."
4. This leads to variant-specific splicing changes, which Nava found in patient transcriptomes. n.39C>G mainly affected 5′ splice sites, n.44A>G mainly affected 3′ splice sites, and RNU5A-1 variants showed other patterns. The RNU5 variants lacked the shared signature seen with RNU4-2.
5. Mis-splicing of many transcripts is thought to impair brain development. The specific genes involved are unknown.
6. The outcome is the neurodevelopmental phenotype (delay, hypotonia, head-size change, MRI abnormalities, seizures in a minority).

- **Expression.** Jackson report high RNU5B-1 expression in developing brain and retina (ENCODE small RNA-seq). This is consistent with the neural phenotype.
- **Functional evidence level.** Jackson report no direct functional assays of RNU5B-1. Nava provide limited transcriptomic data from small patient numbers.
- **Suggested GO terms** (look up): spliceosomal complex; U5 snRNP; mRNA splicing via spliceosome; mRNA 5′-splice site recognition. Suggested CL: neurons and neural progenitors (inferred). Suggested subcellular location: nucleus, spliceosome.

## 7. Anatomical Structures Affected

Brain and nervous system (all nine patients had MRI abnormalities; corpus callosum hypoplasia was reported for one individual in Jackson's figure, but the gene cohort is not stated). Other involved sites are eye, chest wall (pectus excavatum), heart, lung, teeth and the sacrococcygeal region (small counts). Laterality is not reported.

## 8. Temporal Development

Onset is early, during development. Natural history, progression and critical windows have not been described.

## 9. Inheritance and Population

- Autosomal dominant, de novo. Parental origin is skewed to maternal in phaseable cases. Germline mosaicism and recurrence in siblings were not described.
- Penetrance and expressivity: apparently high penetrance among ascertained cases, with variable severity. Not formally estimated.
- Prevalence, incidence, sex ratio and geographic distribution: not available. Cases come from the UK, France and international collaborators, with a few dozen total.
- Recurrent variants (n.44A>G, n.42_43insA, n.39C>G) are mutational hotspots, not founder alleles.

## 10. Diagnostics

- **Genetic testing.** Exome sequencing generally does not cover snRNA genes, and some mapping filters flag them. Genome sequencing, or targeted analysis of snRNA genes, is needed. Jackson note that the n.42_43insA variant failed a stringent "altreadparent" filter in two cases, but manual IGV review showed no good-quality alternate reads in the parents. This indicates that pipeline filters can hide real de novo calls.
- **Imaging.** Brain MRI abnormalities are common; the specific findings are not described in the text I accessed.
- **Differential diagnosis.** RNU4-2 (ReNU) syndrome, RNU2-2 developmental and epileptic encephalopathy, and other spliceosomopathies. Nava found that RNU5 and RNU4-2 patients differ in splicing signature and clinical profile.
- No biomarkers or clinical criteria exist. No screening programme exists.

## 11. Outcome / Prognosis

Not reported. Most reported patients have severe developmental delay, but survival and long-term outcomes are unknown.

## 12. Treatment

No disease-specific therapy was found. Care is supportive: developmental therapies (NCIT rehabilitation, physical therapy, speech-language therapy), antiseizure medication for the minority with epilepsy, and nutritional support for failure to thrive. This is general practice, not drawn from RNU5B-1 literature. No clinical trials were identified. Antisense approaches to snRNA disorders are conceptual only.

## 13. Prevention

Genetic counselling is warranted. The recurrence risk appears low because the variants are de novo, but germline mosaicism cannot be excluded. No prevention strategies are known.

## 14. Other Species / Natural Disease

Not applicable. U5 snRNA is highly conserved, but no animal disease equivalents were found.

## 15. Model Organisms

No RNU5B-1 models were found. The U5 paralogs are redundant genes, which complicates modelling, and a patient-derived or edited cell line would be the likely route. This is my inference, not published work.

## Key Citations

- Nava C, et al. Dominant variants in major spliceosome U4 and U5 small nuclear RNA genes cause neurodevelopmental disorders through splicing disruption. *Nat Genet* 2025;57(6):1374–1388. PMID 40379786; DOI 10.1038/s41588-025-02184-4. [PMC12165858](https://pmc.ncbi.nlm.nih.gov/articles/PMC12165858/). Also available as a [medRxiv preprint](https://www.medrxiv.org/content/10.1101/2024.10.07.24314689.full.pdf).
- Jackson R, et al. Analysis of R-loop forming regions identifies RNU2-2 and RNU5B-1 as neurodevelopmental disorder genes. *Nat Genet* 2025;57(6):1362–1366. PMID 40442284; DOI 10.1038/s41588-025-02209-y. [PMC12165836](https://pmc.ncbi.nlm.nih.gov/articles/PMC12165836).
- OMIM [#621302](https://omim.org/entry/621302) and [*621090](https://omim.org/entry/621090) (not directly read).
- [GeneCards RNU5B-1](https://www.genecards.org/card/RNU5B-1) and [MalaCards NEDSJL](https://www.malacards.org/card/neurodevelopmental_disorder_with_seizures_and_joint_laxity) (secondary sources).

## Curation Recommendations

- Resolve the joint-laxity and seizure discrepancy against the OMIM entry text and supplementary tables before encoding frequencies.
- Do not state any splicing mechanism for RNU5B-1 as established. Nava's data come from small numbers of patients.
- Run `just fetch-reference PMID:40379786` and `PMID:40442284`, then quote exact snippets from the cached text. The quotes above were relayed by a summarizing tool, so verify them against the cache.
- Look up every ontology ID and the HGNC ID in the same step you write it.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 6 |
| On topic | 5 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMC:PMC12165836`: "is highly likely to have arisen on the maternal allele"
  - closest text in source: "Variants that pass base filter are then subject to the stringent filter, which include the following: altreadparent_filter (no more than one read supporting the alternate allele in either the mother or the father); abratio_filter (the AB ratio in the offspring is between 0.3 and 0.7); proximity_filter (DNV is not located within 20 bp of another DNV within the same trio); segmentalduplication_filter (no overlap with segmental duplications); simplerepeat_filter (no overlap with simple repeat regions; patch_filter (no overlap with patch regions); stringent_filter (**all base and stringent filters pass)"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 2 |
| Resolved | 2 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 0 |

Every term resolved, and every label the report gave matched.