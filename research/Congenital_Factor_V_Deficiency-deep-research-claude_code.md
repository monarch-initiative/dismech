---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-12T04:05:21.147686'
end_time: '2026-10-12T04:06:22.612151'
duration_seconds: 61.46
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Congenital Factor V Deficiency
  mondo_id: MONDO:0009210
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
  num_turns: 5
  total_cost_usd: 0.7874280999999999
  session_id: c5bca049-79dd-565a-9d58-3e2354d3de80
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 13
reference_validation:
  total_references: 2
  verified: 2
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 2
  on_topic: 1
  validator_version: 0.3.0
term_validation:
  total_terms: 4
  verified: 3
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Congenital Factor V Deficiency
- **MONDO ID:** MONDO:0009210 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Congenital Factor V Deficiency** covering all of the
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

# Congenital Factor V Deficiency (MONDO:0009210): research report

**Verification status.** I ran three web searches. They returned review-level sources but no abstract text I could quote, and none of the PMIDs were confirmed. Claims are tagged **[sourced]** where a search result supports them. Claims tagged **[background]** come from my own knowledge and have not been checked. The `Term Validation` and `just preflight-dr` steps in CLAUDE.md still apply, and so does the rule that every CURIE and PMID is read from a source before it is written. The ontology IDs below are leads, not bindings. I did not look up any of them. Please do not bind them, or quote snippets, without a lookup and `just fetch-reference`.

## 1. Disease information
- Congenital factor V (FV) deficiency is a rare autosomal recessive bleeding disorder. It is caused by a deficiency of coagulation factor V (proaccelerin, labile factor). [sourced: [NHF/HFA overview](https://www.hemophilia.org/bleeding-disorders-a-z/types/other-factor-deficiencies/factor-v)]
- Synonyms: Owren's disease, parahemophilia, proaccelerin deficiency, labile factor deficiency. [sourced: same page]
- Identifiers:
  - MONDO:0009210, given in the template.
  - HGNC:3542 appears in a GenCC submission linking F5 to MONDO:0009210. [sourced: [GenCC](https://search.thegencc.org/submissions/GENCC_000102-HGNC_3542-MONDO_0009210-HP_0000007-GENCC_100001)]
  - The repo uses the lowercase form `hgnc:3542`.
  - OMIM 227400 [background, unverified].
  - Orphanet number: not found.
  - ICD-10 D68.2 (hereditary deficiency of other clotting factors) [background, unverified].
- Do not confuse it with FV Leiden (thrombophilia), combined FV/FVIII deficiency (LMAN1/MCFD2), or acquired FV inhibitors. Combined FV/FVIII deficiency is a separate disease. [background]
- The data are aggregated disease-level resources and case series, not EHR-derived.

## 2. Etiology
- Causal factor: biallelic loss-of-function variants in F5. [sourced: [Asselta & Peyvandi review, 2009](https://www.qxmd.com/r/19598066)] The review reports that 56 mutations had been published in severe or moderately severe FV deficiency. More than two thirds were null mutations, and the rest were mostly missense.
- Heterozygous carriers have about half-normal FV and are usually asymptomatic. [sourced]
- Risk factors:
  - Consanguinity raises the chance of homozygosity. [background]
  - No environmental risk factors are known.
- Protective factors:
  - Platelet-derived FV can partly preserve hemostasis even when plasma FV is near zero. [sourced: [Cornell VIVO record, "Platelets and platelet-derived factor Va confer hemostatic competence in complete factor V deficiency"](https://vivo.weill.cornell.edu/display/pubid25896652)]
  - Concurrent thrombophilic variants (e.g. FV Leiden in trans) can attenuate the bleeding phenotype. [background, unverified]
- Gene–environment interactions: none established.

## 3. Phenotypes
Suggested HPO terms are leads and must be looked up before binding.

| Phenotype | Notes | Suggested HPO |
|---|---|---|
| Mucosal bleeding (epistaxis, gum bleeding, menorrhagia) | Most common feature. [sourced: [2019 overview](https://www.thieme-connect.com/products/ejournals/pdf/10.1055/s-0039-1687906.pdf)] | Epistaxis; Menorrhagia; Gingival bleeding |
| Easy bruising / ecchymoses | Mild cases. [sourced] | Bruising susceptibility |
| Postoperative or post-traumatic hemorrhage | [sourced: [NHF/HFA overview](https://www.hemophilia.org/bleeding-disorders-a-z/types/other-factor-deficiencies/factor-v)] | Abnormal bleeding |
| Pulmonary and GI bleeding | Severe cases. [sourced: [NHF/HFA overview](https://www.hemophilia.org/bleeding-disorders-a-z/types/other-factor-deficiencies/factor-v)] | Gastrointestinal hemorrhage |
| Intracranial hemorrhage | Severe cases, including perinatal onset. A report links homozygous F5 splicing mutations to a high incidence of intracranial bleeding. [sourced: [Haematologica](https://haematologica.org/article/view/4255/14625)] | Intracranial hemorrhage |
| Hemarthrosis | Uncommon. [background] | Hemarthrosis |
| Prolonged PT and aPTT | Laboratory finding. [background, unverified] | Prolonged prothrombin time; Prolonged partial thromboplastin time |

- Onset runs from neonatal to adult. The mildest cases are diagnosed late.
- Severity correlates imperfectly with plasma FV activity, and platelet FV helps account for the mismatch.
- The course is lifelong. Bleeding is episodic.
- Frequency percentages and quality-of-life data: not retrieved.

## 4. Genetic and molecular information
- Gene: F5 (HGNC:3542), at 1q24.2 [background]. The protein is large, with A1-A2-B-A3-C1-C2 domains. [background]
- Variant spectrum: null (nonsense, frameshift, splice) and missense variants spread across the gene. [sourced: [2019 overview](https://www.thieme-connect.com/products/ejournals/pdf/10.1055/s-0039-1687906.pdf)]
  - Reported case series include an Indian cohort with three novel exon 13 deletions and an African American patient with two novel variants. [sourced via search summary; citations not verified]
- Mechanism: loss of function. [sourced]
- Modifier genes: not established in what I retrieved.
- Epigenetic and chromosomal abnormalities: none known.
- Allele frequencies (gnomAD) and ClinVar classifications: not retrieved.
- Gene-disease validity: GenCC lists an F5–MONDO:0009210 submission. [sourced: [GenCC](https://search.thegencc.org/submissions/GENCC_000102-HGNC_3542-MONDO_0009210-HP_0000007-GENCC_100001)] Run `just check-gene-validity` and copy the tier from ClinGen. Do not assign one.

## 5. Environmental information
None are known. There are no environmental, lifestyle, or infectious causes of the congenital form. Acquired FV deficiency (inhibitors, liver disease, DIC) is a separate entity.

## 6. Mechanism / pathophysiology
Causal chain:
1. Biallelic F5 loss-of-function variants lead to absent or reduced synthesis or secretion of FV. [sourced]
2. FV is made mainly in the liver (hepatocytes) and circulates as plasma FV. About 20% is stored in platelet α-granules. [sourced via search summary; hepatic synthesis is background]
3. Without FV there is no cofactor Va for factor Xa in the prothrombinase complex. Prothrombin conversion to thrombin on activated platelet surfaces is then impaired. [background]
4. Reduced thrombin generation leads to defective fibrin formation, and the PT and aPTT are prolonged. [background]
5. The result is mucosal and postoperative bleeding. The phenotype is variable because platelet FV/Va can partly compensate. [sourced: [Cornell VIVO record](https://vivo.weill.cornell.edu/display/pubid25896652)]
6. Branch: in the most severe genotypes, with absent plasma and platelet FV, intracranial hemorrhage occurs, including perinatally. [sourced: [Haematologica](https://haematologica.org/article/view/4255/14625)]

Suggested terms, to be verified by lookup:
- GO: blood coagulation, thrombin generation, prothrombinase complex.
- CL: hepatocyte, platelet, megakaryocyte.
- GO CC: platelet alpha granule.

There are no single-cell, proteomic, or other omics findings in what I retrieved.

## 7. Anatomical structures affected
- Systemic hemostasis, with the liver as the site of synthesis. Mucosae (nose, gut, uterus), brain, lung, and joints are the bleeding sites. [sourced / background]
- Subcellular: platelet alpha granule. Laterality: not applicable.

## 8. Temporal development
- Onset is congenital. The phenotype may present in the neonatal period, in childhood, or in adulthood.
- The course is lifelong, non-progressive, and episodic. Intracranial hemorrhage is the main early-life risk. [sourced]
- No remission patterns are described.

## 9. Inheritance and population
- Autosomal recessive.
- Prevalence: about 1 in 1,000,000 is the usual figure [background]. A 2025 knock-in mouse paper describes the disease as ultra-rare, "1–9 cases per million live births". [sourced: [PMC12129228](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12129228/)] Reconcile the two against Orphanet before choosing a `prevalence_class`. I found no Orphanet page.
- Carrier frequency: not retrieved.
- Consanguinity increases the disease frequency. [background]
- Founder effects: I did not retrieve any; the Indian cohort exon 13 deletions are a lead. Sex ratio is expected to be equal, as expected for autosomal inheritance. [background]

## 10. Diagnostics
- Prolonged PT and aPTT with a normal thrombin time. A mixing study corrects. [background]
- FV activity assay, which is diagnostic. FV antigen can distinguish type I (quantitative) from type II (qualitative) deficiency. [background]
- Heterozygotes have about 50% FV. [sourced]
- Genetic testing: F5 sequencing, which is large and requires Sanger sequencing, a panel, or exome sequencing. [background]
- Differential: combined FV/FVIII deficiency (LMAN1/MCFD2), acquired FV inhibitor, liver disease, vitamin K deficiency, DIC. [background]
- Screening: none population-wide. Cascade testing of relatives is relevant.
- GeneReviews chapter: not found in my search. Run `just check-genereviews`.

## 11. Outcome / prognosis
- Bleeding severity is variable. Most patients have mucosal bleeding that is managed with treatment. Severe cases can involve life-threatening intracranial, pulmonary, or GI hemorrhage. [sourced]
- Survival and life-expectancy data: not retrieved.
- Prognostic factors: FV activity level and genotype, with platelet FV as a modifier. [sourced / background]

## 12. Treatment
- There is no FV-specific concentrate. Fresh frozen plasma (FFP) is the mainstay. [sourced: [Rare Coagulation Disorders](https://rarecoagulationdisorders.org/disorder/factor-v-deficiency/medication-treatment/); [NHF/HFA overview](https://www.hemophilia.org/bleeding-disorders-a-z/types/other-factor-deficiencies/factor-v)]
- Dosing: one review sets a target of FV above 20% for procedures and acute bleeding, with daily FFP infusions of 15–20 mL/kg typically enough. [sourced via search summary; verify at the source]
- Platelet transfusion is added in severe or refractory bleeding. Platelet FV supports hemostasis after plasma infusion. [sourced: [Cornell VIVO record](https://vivo.weill.cornell.edu/display/pubid25896652)]
- Antifibrinolytics (aminocaproic acid or tranexamic acid) are used for mucosal bleeding. rFVIIa and prothrombin complex concentrate have been used in refractory cases. [sourced via search summary]
- Experimental: a 2025 Thieme article, "From Fresh Frozen Plasma to First-in-human: Bringing Coagulation Factor V Deficiency into Therapeutic Trials", covers development of FV therapeutics, but I did not read it. [sourced: [Thieme](https://www.thieme-connect.com/products/ejournals/html/10.1055/a-2735-1659)] I found no NCT identifiers.
- NCIT leads to look up and not bind from memory: Pharmacotherapy (NCIT:C15986), Supportive Care (NCIT:C15747), and a plasma or blood transfusion term.
- For the KB, use `therapeutic_modality: PROTEIN_REPLACEMENT` for FFP, only after a source check.

## 13. Prevention
- No primary prevention.
- Genetic counseling and cascade testing apply. Prenatal diagnosis is possible in families with a known variant. [background]
- Prophylactic FFP before surgery or procedures is used as secondary and tertiary prevention. Peripartum and neonatal management planning is needed in severe cases. [background]
- Avoid antiplatelet drugs. [background, unverified]

## 14. Other species
- I did not search OMIA. Naturally occurring FV deficiency has been described in animals. I have not verified it and would not cite it without a source.

## 15. Model organisms
- F5 knockout mice: about half die at E9–E10 with yolk-sac vascular and somite defects. The rest are born and die of massive hemorrhage within hours of birth. [sourced: [PMC4260973 table T3](https://pmc.ncbi.nlm.nih.gov/articles/PMC4260973/table/T3); [UMich listing](https://available-inventions.umich.edu/product/mouse-models-for-developmental-biology-research-f5-knock-out)] The primary paper is probably Cui et al. 1996. That attribution is a lead and not confirmed.
- A 2025 knock-in model is viable and was developed for an ultra-rare disease. [sourced: [PMC12129228](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12129228/)]
- A truncated mutant FV mouse affected hemostasis and embryonic development. [sourced: [UCM record](https://docta.ucm.es/entities/publication/deec17e8-06ec-4895-ac5f-ba1ca26fe954)]
- The null mouse is much more severe than most human cases, because human partial or platelet FV and residual variants soften the phenotype. This fits `HUMAN_MODEL_MISMATCH` or a `PARTIALLY_RECAPITULATES` link. [background]

## Sources
- [Asselta & Peyvandi review](https://www.qxmd.com/r/19598066) (identified from the QxMD record; PMID not verified)
- [2019 overview](https://www.thieme-connect.com/products/ejournals/pdf/10.1055/s-0039-1687906.pdf)
- [2024 review](https://www.thieme-connect.com/products/ejournals/html/10.1055/s-0044-1789021)
- [Haematologica, splicing mutations and intracranial bleeding](https://haematologica.org/article/view/4255/14625)
- [NHF/HFA overview](https://www.hemophilia.org/bleeding-disorders-a-z/types/other-factor-deficiencies/factor-v)
- [Rare Coagulation Disorders](https://rarecoagulationdisorders.org/disorder/factor-v-deficiency/medication-treatment/)
- [Cornell VIVO, platelet FV](https://vivo.weill.cornell.edu/display/pubid25896652)
- [GenCC](https://search.thegencc.org/submissions/GENCC_000102-HGNC_3542-MONDO_0009210-HP_0000007-GENCC_100001)
- [PMC12129228](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12129228/)
- [PMC4260973](https://pmc.ncbi.nlm.nih.gov/articles/PMC4260973/table/T3)
- [Thieme therapeutic trials article](https://www.thieme-connect.com/products/ejournals/html/10.1055/a-2735-1659)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 2 |
| Resolved | 2 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 2 |
| On topic | 1 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 4 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |

3 of 4 terms resolved to a current term; the rest could not be looked up either way.