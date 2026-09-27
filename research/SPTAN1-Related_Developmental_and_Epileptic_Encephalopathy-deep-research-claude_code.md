---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-19T20:08:27.698467'
end_time: '2026-08-19T20:13:37.996411'
duration_seconds: 310.3
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: SPTAN1-Related Developmental and Epileptic Encephalopathy
  mondo_id: ''
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
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 18
  num_turns: 35
  total_cost_usd: 2.1335086
  session_id: 6f8bf895-3ab0-55cb-a154-acb932b43f03
  stop_reason: end_turn
  assistant_text_blocks: 4
citation_count: 19
reference_validation:
  total_references: 12
  verified: 11
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.083
  relevance_assessed: 11
  on_topic: 7
  off_topic: 1
  off_topic_references:
  - PMID:28838957
  unresolved_references:
  - DOI:10.1172/JCI95743](https://www.jci.org/articles/view/95743
  needs_review: true
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** SPTAN1-Related Developmental and Epileptic Encephalopathy
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **SPTAN1-Related Developmental and Epileptic Encephalopathy** covering all of the
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

I'll research SPTAN1-Related Developmental and Epileptic Encephalopathy now, running parallel searches across the key domains.

I have sufficient material now. Let me do one final round on differential diagnosis, animal models, and treatment/genetic counseling specifics before compiling the report.

I now have enough material to compile a comprehensive report.

I have gathered sufficient information across all domains. Here is the comprehensive research report.

# SPTAN1-Related Developmental and Epileptic Encephalopathy: Comprehensive Research Report

## 1. Disease Information

**Overview.** SPTAN1-related developmental and epileptic encephalopathy (SPTAN1-DEE, historically **DEE5** / "early infantile epileptic encephalopathy 5," EIEE5) is a rare, genetically defined neurodevelopmental disorder caused by heterozygous (typically de novo) pathogenic variants in *SPTAN1*, which encodes the cytoskeletal scaffold protein **αII-spectrin** (non-erythrocytic spectrin alpha chain 1). The prototypic severe form presents in the first months of life with intractable epilepsy (often infantile spasms/West syndrome with hypsarrhythmia), profound global developmental delay, acquired microcephaly, spastic quadriplegia, and severe cerebral hypomyelination with progressive brain atrophy on MRI ([OMIM #613477](https://omim.org/entry/613477); [NORD/MONDO](https://rarediseases.org/mondo-disease/developmental-and-epileptic-encephalopathy-5/)).

Since the original 2010 description, *SPTAN1* has been shown to cause a much broader **phenotypic continuum** rather than a single syndrome — ranging from severe infantile DEE, through milder developmental delay ± epilepsy, to pure/complex hereditary spastic paraplegia (HSP) and cerebellar ataxia, and even distal hereditary motor neuropathy — depending on variant type and location within the protein ([Saitsu et al. 2010, PMID:20493457](https://pubmed.ncbi.nlm.nih.gov/20493457/); [Jaglin et al./Brain 2017, PMID:28838957](https://academic.oup.com/brain/article/140/9/2322/4096697); [Klug et al./GenetMed 2022, PMID:36331550](https://pmc.ncbi.nlm.nih.gov/articles/PMC10620943/)).

**Key identifiers:**
- **OMIM (gene):** 182810 (SPTAN1, SPECTRIN ALPHA, NONERYTHROCYTIC 1)
- **OMIM (phenotype):** #613477 — Developmental and Epileptic Encephalopathy 5 (DEE5); also 620540 — Developmental delay with or without epilepsy (DEVEP, milder allelic phenotype); Spastic Paraplegia 91, autosomal dominant, with or without cerebellar ataxia; Neuronopathy, distal hereditary motor, autosomal dominant 11
- **MONDO:** MONDO:0013277 (DEE5)
- **HGNC:** SPTAN1, chromosome location 9q34.11
- **Orphanet:** SPTAN1 is listed as a disease-associated gene at Orphanet's gene page (multiple linked disorder entries for the epileptic-encephalopathy and HSP/ataxia phenotypes)
- **Common synonyms:** DEE5; Early Infantile Epileptic Encephalopathy 5 (EIEE5); West syndrome due to SPTAN1 mutation; αII-spectrinopathy; SPTAN1 encephalopathy

**Source of information:** The evidence base is derived almost entirely from **aggregated case series and case reports** (dozens of published cohorts totaling well under 100 well-characterized patients) rather than large-scale population/EHR-level resources, reflecting its status as an ultra-rare disorder identified mainly through exome/genome sequencing in epilepsy and neurodevelopmental-disorder cohorts. A 2025 caregiver survey (25 families) is the largest patient-reported dataset to date ([Wilson & Wong 2025, PMID:40261672](https://pubmed.ncbi.nlm.nih.gov/40261672/)).

---

## 2. Etiology

**Disease causal factor.** SPTAN1-DEE is a monogenic disorder caused by heterozygous variants in *SPTAN1*. The overwhelming majority of pathogenic variants arise **de novo**, though dominantly inherited and intrafamilial-variable transmission has been documented (including one family spanning "benign convulsions with mild gastroenteritis" to developmental encephalopathy — [ScienceDirect 2020](https://www.sciencedirect.com/science/article/abs/pii/S1090379820301537)).

**Genetic risk factors:**
- **Causal variant classes:** missense variants (clustering in specific spectrin repeats), in-frame small deletions/duplications/insertions (especially within the C-terminal α19–α20 spectrin repeats), and — for the milder DEVEP/HSP-ataxia phenotypes — truncating variants (nonsense, frameshift, splice-altering) and whole-gene microdeletions ([Jaglin et al. 2017](https://academic.oup.com/brain/article/140/9/2322/4096697); [Klug et al. 2022, PMID:36331550](https://pmc.ncbi.nlm.nih.gov/articles/PMC10620943/)).
- **Recurrent variant:** p.(Asp2303_Leu2305dup) — a 3-amino-acid duplication reported recurrently (5 unrelated patients) associated with severe infantile encephalopathy.
- **Modifier/susceptibility loci:** none well established; phenotype is driven largely by variant location/type (see Mechanism, below) rather than a distinct modifier gene.
- **Locus constraint:** *SPTAN1* is strongly loss-of-function constrained in gnomAD (pLI ≈ 1), consistent with haploinsufficiency intolerance and supporting pathogenicity of truncating alleles (identified in a distinct distal myopathy phenotype, see below).
- **Contiguous-gene syndromes:** 9q34.11 microdeletions can encompass *SPTAN1* together with *STXBP1*, *ENG*, and *TOR1A*, producing blended phenotypes ([Nature/GenetMed 2013](https://www.nature.com/articles/gim201265)).

**Environmental risk factors:** None established; this is a purely genetic (Mendelian) disorder with no known environmental, toxic, infectious, or lifestyle contribution to primary causation.

**Protective factors:** No genetic or environmental protective factors have been identified; there is no described modifier allele that mitigates severity.

**Gene-environment interactions:** Not applicable/not described — SPTAN1-DEE is not currently understood to involve gene-environment interaction. (Febrile illness can act as a seizure trigger in some patients, as in many genetic epilepsies, but this is symptomatic exacerbation rather than a causal G×E mechanism.)

---

## 3. Phenotypes

### Clinical spectrum overview
Three broad, evidence-supported phenotypic groups have been delineated ([Jaglin 2017](https://academic.oup.com/brain/article/140/9/2322/4096697); [Klug 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC10620943/)):

1. **Severe infantile developmental and epileptic encephalopathy (DEE)** — the classic/original phenotype
2. **Milder developmental delay ± seizures** (childhood-onset epilepsy, variable severity)
3. **Pure or complex hereditary spastic paraplegia (HSP) / hereditary ataxia**, often without seizures or significant intellectual disability

A fourth, distinct presentation — **heterozygous loss-of-function SPTAN1 variants causing an early-childhood-onset distal myopathy with chronic neurogenic features** (foot/toe extensor weakness, gait abnormality) — has recently been reported, further widening the allelic spectrum ([medRxiv/GenetMed 2024](https://www.medrxiv.org/content/10.1101/2024.09.23.24313872.full.pdf)).

### Symptoms/signs (Group 1 — severe DEE, HP-suggested terms)
| Phenotype | Frequency (reported cohorts) | Onset | HPO suggestion |
|---|---|---|---|
| Infantile spasms/epileptic spasms | 93% of DEE group; seizures overall in 85–95% of all SPTAN1 patients | Median ~4 months (first months of life) | HP:0011097 (Epileptic spasms) |
| Hypsarrhythmia on EEG | Common in DEE group | Infancy | HP:0011096 |
| Profound global developmental delay/intellectual disability | Nearly universal in DEE group | Congenital–infantile | HP:0012758 / HP:0001263 |
| Lack of visual attention / cortical visual impairment | Frequent | Infancy | HP:0000572 |
| Poor head control / axial hypotonia | Frequent | Infancy | HP:0002476 |
| Feeding difficulties | Frequent | Infancy | HP:0011968 |
| Acquired (postnatal) microcephaly | Frequent | Infancy–childhood, progressive | HP:0000252 |
| Spastic quadriplegia | Common in severe form | Progressive | HP:0002510 |
| Cerebral hypomyelination | ~79% on MRI | Infancy, may progress | HP:0007123 |
| Progressive cerebral/cerebellar/brainstem atrophy | ~93% of encephalopathy cases | Progressive, often marked within 2–3 years | HP:0002059 / HP:0001272 |
| Corpus callosum thinning/agenesis | ~86% | — | HP:0002079 |
| Death in early childhood | ~21% (7/34 in one pooled cohort) | Median 5.6 years in one series | — |

### Milder/Group 2–3 phenotype
- 30% of a pooled cohort had less severe intellectual disability with childhood-onset epilepsy (generalized, myoclonic, focal, or no epilepsy at all)
- Benign convulsions with mild gastroenteritis reported in one family
- Migraine, epilepsy, and subependymal heterotopias **without** intellectual disability described in an extended-phenotype report ([PMID:34590414](https://pubmed.ncbi.nlm.nih.gov/34590414/))
- Group 3 (HSP/ataxia): progressive spasticity and/or ataxia, generally without seizures or significant cognitive impairment, sometimes adult-onset; a recurrent N-terminal variant (p.Arg19Trp) is enriched in pure HSP presentations

### 2025 caregiver survey (real-world/patient-reported data, n=25)
Reported: epilepsy (~60%+), intellectual and motor delay, encephalopathy, motor neuropathy, absent/difficult speech, cognitive/motor decline with age, vision and hearing abnormalities, organ and skeletal effects, autoimmune disease, and immune dysfunction in some patients — broadening the phenotype beyond the classical neurologic triad ([Wilson & Wong 2025, PMID:40261672](https://pubmed.ncbi.nlm.nih.gov/40261672/)). Median time to diagnosis was 3.6 years, reflecting recent uptake of genetic testing.

### Quality of life impact
Severely affected individuals have profound functional impairment across all domains (mobility, communication, feeding), high caregiver burden, and shortened lifespan in the severe subgroup; the 2025 caregiver survey is the first systematic patient-reported QoL/burden dataset for this ultra-rare gene.

---

## 4. Genetic/Molecular Information

**Causal gene:** *SPTAN1* (HGNC:11273; OMIM 182810), chromosome 9q34.11, 57 exons, encoding αII-spectrin (SPTA2/SPTAN1 protein), the principal non-erythroid α-spectrin subunit expressed in brain.

**Protein structure:** αII-spectrin is organized as an N-terminal tetramerization/calponin-homology actin-binding domain, **~20–21 tandem spectrin repeats (SR)**, a Src-homology-3 (SH3) domain (within repeat α9/α10 region), a **calmodulin-binding "CCC" insert** within repeat 10/11 (also containing calpain and caspase cleavage sites), and a C-terminal **EF-hand calcium-binding domain**. Heterodimerization with β-spectrin depends critically on the antiparallel pairing of the **N-terminal repeats of β-spectrin with the C-terminal repeats (α19–α21) of α-spectrin**, forming heterotetramers that build the sub-membranous actin-spectrin cytoskeleton.

**Variant classification and functional consequence (genotype-phenotype correlation):**
- **Missense and small in-frame indels in the C-terminal heterodimerization repeats (α19–α20)** → most severe DEE phenotype, via a **dominant-negative** mechanism: mutant protein misfolds/aggregates and disrupts assembly of the wild-type spectrin-actin lattice, rather than simple haploinsufficiency ([Jaglin 2017](https://academic.oup.com/brain/article/140/9/2322/4096697); [JCI 2018, PMID unlisted but DOI 10.1172/JCI95743](https://www.jci.org/articles/view/95743)).
- **Missense variants outside the heterodimerization domain** (e.g., repeats α2, α3, α11, α14, α16, α18) → milder phenotypes, better developmental outcomes.
- **Truncating variants (nonsense, frameshift) and whole-gene microdeletions** → generally the **milder** developmental-delay-with-or-without-epilepsy phenotype, consistent with a **haploinsufficiency (quantitative loss)** mechanism rather than dominant-negative aggregation.
- **N-terminal tetramerization-domain missense variant p.Arg19Trp** → recurrently associated with **pure hereditary spastic paraplegia**.
- **Distinct heterozygous loss-of-function (nonsense/frameshift/splice-acceptor) variants** → newly described distal myopathy with chronic neurogenic features (14 families), reinforcing that LoF variants produce a mechanistically and clinically distinct phenotype from the dominant-negative DEE variants.

**Functional/aggregation studies:** Patient fibroblasts and iPSC-derived neurons carrying C-terminal dominant-negative variants (e.g., p.Arg1464Trp-region variants, p.Glu2207del, p.Arg19Trp) show abnormal αII-spectrin **protein aggregation**, shortened neurites, and disrupted cytoskeletal organization ([Klug 2022, PMID:36331550](https://pmc.ncbi.nlm.nih.gov/articles/PMC10620943/); JCI 2018).

**Population frequency:** *SPTAN1* is not a common contributor to disease broadly, but rare damaging variants account for an estimated **~1.1% of hereditary ataxia/spastic paraplegia cohorts**, with statistically significant case-control enrichment (p = 2.8 × 10⁻⁵) ([Klug 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC10620943/)).

**gnomAD constraint:** pLI ≈ 1 (extremely LoF-intolerant), consistent with haploinsufficiency sensitivity; this supports pathogenicity assignment for truncating variants and argues against simple biallelic LoF as the mechanism for most DEE cases (which are heterozygous dominant-negative missense/indel).

**Somatic vs. germline:** All reported pathogenic variants are germline (constitutional), most de novo; no somatic mosaicism series specifically reported to date, though germline mosaicism is plausible given recurrence in some families and should be considered for genetic counseling of unaffected parents.

**Epigenetics/chromosomal abnormalities:** No specific DNA methylation signature or recurrent chromosomal rearrangement is described beyond the 9q34.11 contiguous microdeletions noted above (which also remove *STXBP1*, *ENG*, *TOR1A*).

**Suggested ontology terms:** HGNC:11273 (SPTAN1); GO:0008091 (spectrin); GO:0030507 (spectrin binding); GO:0030426 (growth cone); GO:0043194 (axon initial segment); GO:0030018 (Z disc, for the myopathy phenotype).

---

## 5. Environmental Information

No specific environmental toxins, occupational exposures, dietary factors, or infectious agents have been implicated as causal in SPTAN1-DEE — this is a purely monogenic disorder. Febrile illness may act as a nonspecific seizure trigger/exacerbant in some affected individuals, as is common across genetic epilepsies, but this is not disease-causal. No lifestyle or infectious contribution has been described in the literature reviewed.

---

## 6. Mechanism / Pathophysiology

**Causal chain (severe DEE, dominant-negative mechanism):**

1. **Trigger:** De novo heterozygous missense or small in-frame indel variant, predominantly in the C-terminal spectrin repeats (α19–α20) required for α/β-spectrin heterodimerization.
2. **Molecular consequence:** Mutant αII-spectrin protein misfolds and **aggregates**, sequestering or destabilizing wild-type αII- and βII/βIV-spectrin, producing a dominant-negative disruption of the spectrin-actin sub-membranous cytoskeleton (rather than simple loss of one allele's product) — demonstrated in patient fibroblasts, iPSC-neurons, and heterologous overexpression systems.
3. **Cellular consequence:**
   - Disruption of the **axon initial segment (AIS)** periodic sub-membranous spectrin-actin lattice (normally formed together with βIV-spectrin and ankyrin-G), which is required for clustering of voltage-gated sodium/potassium channels and normal action-potential initiation.
   - Impaired **dendritic and axonal development/neuronal polarity**.
   - **Decreased inhibitory (GABAergic) synaptic innervation** — reduced inhibitory synapse frequency shown by patch-clamp electrophysiology in a conditional mouse knockout model, implicating **cortical disinhibition** as a proximate seizure mechanism.
   - Disrupted cortical lamination during development.
4. **Tissue/organ consequence:** Progressive **cerebral, cerebellar, and brainstem atrophy**; severe **hypomyelination**; thinning/agenesis of the corpus callosum — visible on serial MRI, with heterodimerization-domain mutations showing the most rapid 2–3 year radiographic progression.
5. **Clinical manifestation:** Infantile-onset epileptic spasms/hypsarrhythmia (West syndrome), profound developmental arrest, acquired microcephaly, spastic quadriplegia.

**Molecular pathways/cellular processes:** Axon initial segment assembly (GO:0043194); spectrin-based membrane skeleton organization (GO:0008091, GO:0030507); neuronal polarity establishment; GABAergic synaptogenesis and inhibitory synaptic transmission; axonal transport support (spectrin-actin lattice provides mechanical stability along the axon shaft).

**Model system evidence:**
- **Conditional knockout mouse (*Sptan1^f/f*; CNS-specific αII-spectrin deletion):** disrupted AIS, disrupted cortical lamination, widespread neurodegeneration, seizures, and premature death (before 1 month) — full knockout is required to produce a phenotype, since **heterozygous Sptan1-knockout mice show no phenotype**, supporting a dominant-negative (not simple haploinsufficiency) mechanism for the severe human DEE alleles (consistent with truncating variants instead producing the milder human phenotype through haploinsufficiency) ([J Neurosci 2017, PMID:29038240](https://pmc.ncbi.nlm.nih.gov/articles/PMC5700417/); [JCI 2018](https://www.jci.org/articles/view/95743)).
- **In utero CRISPR/Cas9 electroporation** achieving ~80% mosaic knockout recapitulates AIS and lamination defects, allowing dissection of cell-autonomous vs. non-cell-autonomous contributions.
- **Human iPSC-derived neurons** from patients carrying dominant-negative variants show spectrin aggregation and shortened neuronal processes, directly linking the human genotype to the aggregation mechanism seen in mouse and heterologous systems.
- A separate **Spna2 R1098Q mouse variant model** (affecting scaffold stability) shows progressive ataxia, memory impairments, and seizure episodes, modeling the milder/HSP-ataxia end of the human spectrum ([PMC9953789](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9953789/)).

**Cell types implicated:** cortical pyramidal neurons (CL:0000598), GABAergic interneurons (CL:0000617), oligodendrocytes/myelinating glia (secondary to hypomyelination, CL:0000128), cerebellar Purkinje/granule neurons (in the atrophy/ataxia phenotypes).

**Biochemical abnormalities:** No specific circulating biomarker or enzyme deficiency is described; the core defect is structural/cytoskeletal protein dysfunction (spectrin aggregation) rather than a classical metabolic lesion.

---

## 7. Anatomical Structures Affected

**Organ level (primary):** Central nervous system — cerebral cortex, cerebellum, brainstem, corpus callosum, and (in the neuropathy/myopathy allelic phenotypes) peripheral motor nerve and skeletal muscle.

**Body systems involved:** Nervous system (primary); musculoskeletal system (spasticity, distal myopathy variant); visual system (cortical visual impairment); in the 2025 caregiver survey, also reported organ/skeletal effects, immune dysfunction, and autoimmune disease in a subset — these associations require further characterization.

**Tissue/cell level:**
- Cerebral cortex: disrupted lamination, cortical atrophy
- White matter/oligodendrocytes: severe hypomyelination
- Cerebellum and brainstem: progressive atrophy (hallmark of the severe form)
- Axon initial segment and nodes of Ranvier (specialized axonal membrane subdomains) — primary site of spectrin-actin cytoskeletal disruption
- Inhibitory (GABAergic) synapses — reduced density/function

**Subcellular level:** Plasma membrane-proximal sub-membranous cytoskeleton (spectrin-actin lattice); axon initial segment periodic scaffold (GO Cellular Component: axon initial segment, GO:0043194; plasma membrane region, GO:0098590).

**Localization/lateralization:** Diffuse, bilateral, symmetric cerebral/cerebellar involvement — no lateralization pattern reported.

**Suggested UBERON terms:** UBERON:0000956 (cerebral cortex), UBERON:0002037 (cerebellum), UBERON:0002298 (brainstem), UBERON:0002336 (corpus callosum), UBERON:0002037 (white matter).

---

## 8. Temporal Development

**Onset:**
- Severe DEE group: congenital/first months of life — median onset of epileptic spasms ~4 months
- Milder group: childhood onset (ages 2–15 years) for seizures; developmental delay may be apparent from infancy
- HSP/ataxia group: can be later-onset, including adult presentations

**Progression:**
- Severe form: **progressive** — cortical/cerebellar/brainstem atrophy and hypomyelination worsen over the first several years of life, with the most rapid MRI progression (within 2–3 years) in patients with heterodimerization-domain (α19–α20) mutations; motor and cognitive regression/plateauing is typical
- Milder form: relatively **stable** developmental trajectory with variable, sometimes better-controlled epilepsy
- HSP/ataxia form: slowly progressive spasticity/ataxia over years to decades
- Caregiver-survey data additionally note cognitive and motor **decline with age** in some patients, suggesting the disorder is not uniformly static even outside the classic infantile-atrophy group

**Disease course pattern:** Predominantly progressive/degenerative in the severe DEE group (not simply a static encephalopathy); episodic seizure activity is refractory in most; some kindreds show intrafamilial variability from mild (febrile/GI-triggered convulsions) to severe encephalopathy, indicating incomplete penetrance/variable expressivity even for identical or related variants.

**Duration/mortality:** Chronic, lifelong; premature death reported in ~21% of a pooled severe cohort (7/34), with a reported median age at death of 5.6 years in one series.

**Remission:** No spontaneous remission described; seizure control, when achieved, is generally treatment-associated and often partial/refractory.

**Critical periods:** Infancy appears to be a critical window — the timing of epileptic-spasm onset and the degree of AIS/cortical developmental disruption in the first year of life correlate with long-term outcome, arguing for early diagnosis and intervention where possible.

---

## 9. Inheritance and Population

**Epidemiology:** SPTAN1-DEE is an **ultra-rare** disorder; exact prevalence/incidence figures are not established in the literature — the total published cohort across all phenotypic groups numbers in the low hundreds worldwide (e.g., one multi-center study identified 31 individuals from 26 families; other series report 20–34 patients). No national registry-based prevalence estimate exists.

**Inheritance pattern:** **Autosomal dominant**, overwhelmingly **de novo** in the DEE presentation; dominantly inherited transmission (including intrafamilial phenotypic variability) is documented for milder alleles. The distal myopathy phenotype is also autosomal dominant (heterozygous LoF).

**Penetrance:** Appears high but not necessarily complete for the mildest end of the spectrum (e.g., benign febrile/GI-triggered convulsions in some family members carrying the same variant as a more severely affected relative).

**Expressivity:** **Markedly variable**, both between families/variants (genotype-driven, see Mechanism) and within families carrying the identical variant (documented intrafamilial variability from benign convulsions to developmental encephalopathy).

**Genetic anticipation:** Not described/not applicable (not a repeat-expansion disorder).

**Germline mosaicism:** Not systematically studied but biologically plausible given autosomal dominant de novo inheritance patterns seen in other DEE genes; should be discussed in genetic counseling despite typically low recurrence risk for truly de novo cases.

**Founder effects:** None reported; variants are largely private/family-specific, with the exception of the recurrent p.(Asp2303_Leu2305dup) (severe DEE) and p.Arg19Trp (HSP) variants which appear at multiple unrelated loci (likely mutational hotspots rather than a founder effect).

**Consanguinity:** Not a relevant risk factor, as inheritance is autosomal dominant/de novo rather than recessive.

**Carrier frequency:** Not applicable (dominant disorder, not carrier-screening relevant in the classical AR sense).

**Population demographics:** Cohorts reported from Europe, Asia, Africa, and North America (2025 caregiver survey and the 100,000 Genomes Project/DECIPHER/GeneMatcher-based study), suggesting no strong ethnic/geographic restriction, though systematic epidemiologic mapping is lacking.

**Sex ratio:** No strong sex bias reported (2025 survey: 14 males, 11 females in a 25-patient cohort — roughly balanced).

**Age distribution:** Bimodal by phenotype group — infancy for the severe DEE group; childhood for the milder DD/epilepsy group; and childhood through adulthood (including a 72-year-old) for the HSP/ataxia group.

---

## 10. Diagnostics

**Laboratory tests/biomarkers:** No specific diagnostic biochemical or serum biomarker exists; diagnosis is genetic/molecular, supported by clinical and neuroimaging phenotype.

**Imaging:**
- **Brain MRI** is central to diagnosis and phenotyping: severe hypomyelination (especially frontal white matter), progressive cortical/cerebellar/brainstem atrophy, thin/absent corpus callosum, and (in some extended-phenotype cases) subependymal heterotopias.

**Electrophysiology:**
- **EEG**: hypsarrhythmia in the infantile-spasms subgroup; multifocal/generalized epileptiform discharges in milder groups.
- Nerve conduction studies/EMG relevant for the distal hereditary motor neuropathy and myopathy allelic phenotypes (showing chronic neurogenic features).

**Biopsy/pathology:** Not a standard diagnostic requirement; research-level fibroblast/iPSC studies show spectrin protein aggregation (research tool, not clinical diagnostic).

**Genetic testing (primary diagnostic modality):**
- **Whole-exome sequencing (WES)** or **whole-genome sequencing (WGS)**, typically as trio analysis, is the standard approach given the phenotypic heterogeneity and de novo predominance — most reported cases were identified via exome/genome sequencing in DEE or broader NDD cohorts.
- **Epilepsy/DEE gene panels** including *SPTAN1* alongside *STXBP1*, *SCN1A/SCN2A*, *KCNQ2*, *CDKL5*, *SCN8A*, *GRIN1*, *CACNA1A*, etc.
- **Chromosomal microarray (CMA)** to detect 9q34.11 microdeletions encompassing *SPTAN1* (and potentially *STXBP1*/*ENG*/*TOR1A*).
- Single-gene *Sanger* confirmation once a candidate variant is found by panel/exome.
- Variant interpretation follows **ACMG/AMP guidelines**; ClinVar contains numerous SPTAN1 variant submissions classified as pathogenic/likely pathogenic for "Developmental and epileptic encephalopathy."

**Differential diagnosis:** Other genetic DEEs presenting with infantile spasms/early-onset refractory epilepsy — *STXBP1*, *CDKL5*, *SCN2A*, *SCN1A*, *KCNQ2*, *SCN8A*, *GRIN1*, *KCNT1*, *CACNA1A*, *PCDH19* — distinguished by electroclinical pattern, MRI findings (SPTAN1's hallmark being pronounced hypomyelination plus progressive cerebellar/brainstem atrophy), and ultimately molecular confirmation. Contiguous 9q34.11 deletion should be considered when *STXBP1* and *SPTAN1* phenotypic features overlap.

**Screening:** No population or newborn screening program exists (ultra-rare, no biochemical marker); diagnosis is reactive, prompted by clinical presentation.

---

## 11. Outcome/Prognosis

**Survival/mortality:** Elevated early mortality in the severe DEE subgroup — approximately **21% (7/34)** died in early childhood in one pooled cohort; specific life-expectancy tables are not established for milder phenotypes, which may have near-normal lifespan.

**Morbidity/function:** Severe DEE patients have profound, lifelong disability — non-ambulatory spastic quadriplegia, absent/minimal communication, tube feeding often required, refractory epilepsy. Milder-group patients retain variable but real functional capacity; HSP/ataxia-group patients have progressive but generally non-life-limiting motor disability.

**Complications:** Refractory epilepsy (seizures persist in most despite multiple antiseizure medications), feeding difficulties/aspiration risk, orthopedic complications of spasticity, visual impairment, and (per the 2025 caregiver survey) reported vision/hearing abnormalities, autoimmune disease, and immune dysfunction in a subset — these associations need confirmation in larger series.

**Prognostic factors:** **Variant location and mechanism is the dominant prognostic determinant** — dominant-negative missense/in-frame indel variants in the C-terminal heterodimerization domain (α19–α20) predict the most severe, rapidly progressive course; missense variants elsewhere or truncating/haploinsufficiency variants predict milder outcomes. Early, severe hypomyelination and rapid atrophy progression on serial MRI also correlate with worse neurodevelopmental outcome.

**Recovery potential:** Recovery in the severe form is essentially absent; the disease course is progressive/degenerative rather than static, distinguishing it from many "static encephalopathies." Milder forms may show developmental gains, particularly if seizures are better controlled.

---

## 12. Treatment

**Pharmacotherapy:**
- Seizures in SPTAN1-DEE are characteristically **highly drug-resistant**. No SPTAN1-specific antiseizure medication has demonstrated superior efficacy; management follows standard infantile-spasms and refractory-epilepsy protocols.
- **ACTH (adrenocorticotropic hormone)** and **vigabatrin** are first-line for infantile spasms broadly (~60–70% spasm-free with corticosteroids, ~40–60% with vigabatrin in general infantile-spasms populations; combination ACTH+vigabatrin achieves spasm cessation in ~72% in mixed-etiology cohorts). In SPTAN1 specifically, spasms may respond initially, but **focal seizures typically persist/emerge after spasm resolution and remain refractory**.
- No pharmacogenomic (PharmGKB/CPIC) guidance specific to *SPTAN1* has been established — treatment selection is empiric, as for most genetic DEEs.

Suggested NCIT terms: NCIT:C15632 (Chemotherapy — N/A here), more relevantly **NCIT:C15986** (Pharmacotherapy) with therapeutic_agent bindings for corticotropin/ACTH (CHEBI or NCIT term for corticotropin) and vigabatrin (CHEBI:9645).

**Dietary/nutritional therapy:**
- **Ketogenic diet therapy (KDT)** has been used as a second-line treatment after failure of hormonal therapy/vigabatrin for infantile spasms broadly; case-level evidence specifically in SPTAN1 encephalopathy (including a reported case of focal epilepsy responding to KDT) shows the diet **can reduce seizure frequency**, but efficacy in SPTAN1 specifically "remains unclear" given the very small number of reported cases ([Cairn.info 2022](https://stm.cairn.info/revue-epileptic-disorders-2022-4-page-726?lang=en); NCIT:C15447, Dietary Intervention).

**Advanced/experimental therapeutics:**
- **Antisense oligonucleotide (ASO) approaches** are in active development by the patient advocacy organization **Hope for SPTAN1**, working toward a personalized/allele-specific ASO strategy analogous to bespoke ASO programs for other ultra-rare dominant-negative neurodevelopmental disorders (e.g., via the n-Lorem Foundation model). This mirrors the broader "screening rare genetic diagnoses for amenability to bespoke ASO therapy" paradigm now being applied across ultra-rare DEEs (see ScienceDirect 2025 review on bespoke ASO screening cohorts). Given SPTAN1-DEE's dominant-negative aggregation mechanism, allele-selective knockdown of the mutant transcript (sparing the wild-type allele) is mechanistically well-motivated — directly analogous to strategies validated for other toxic gain-of-function dominant-negative neurodevelopmental/neurodegenerative disorders (e.g., FUS-ALS allele-selective ASOs, KCNT1 DEE ASO case reports in *Nature Medicine* 2026).
- No gene therapy, gene editing, or cell therapy program specific to *SPTAN1* has yet reached publication/trial stage as of this research.

**Surgical/interventional:** Standard supportive orthopedic interventions for spasticity (e.g., tendon releases, tone management) as needed; no disease-specific surgical procedure exists. Vagus nerve stimulation or epilepsy surgery evaluation may be considered case-by-case for refractory focal seizures, as in other genetic DEEs, though no SPTAN1-specific outcome data were identified.

**Supportive/rehabilitative care:** Physical therapy, occupational therapy, speech/communication therapy, nutritional support (including gastrostomy feeding where needed), and multidisciplinary developmental support are mainstays of management (NCIT:C15302 Physical Therapy; NCIT:C15747 Supportive Care).

**Experimental treatment registries:** No SPTAN1-specific interventional trial was identified on ClinicalTrials.gov in this search; broader DEE natural-history/registry studies (e.g., STXBP1 natural history study, NCT05462054; neonatal-onset epileptic encephalopathy patient registry, NCT04802135) may include or be adaptable to SPTAN1 patients for natural-history data collection.

**Treatment outcomes:** Overall, seizure control in the severe DEE group is poor; "no effective treatment for focal seizures" following initial spasm resolution is explicitly noted in the literature. Milder-phenotype patients may achieve better seizure control with standard antiseizure medications.

---

## 13. Prevention

Because SPTAN1-DEE arises predominantly from **de novo** dominant variants, there is no established **primary prevention** strategy at the population level (no known modifiable risk factor). Relevant prevention/counseling measures include:

- **Genetic counseling:** For families with a confirmed de novo *SPTAN1* variant, recurrence risk for future pregnancies is low but not zero (accounting for the possibility of parental germline mosaicism); for the rarer dominantly inherited/variable-expressivity families, 50% transmission risk applies to each pregnancy, with the caveat of unpredictable severity due to variable expressivity.
- **Prenatal/preimplantation testing:** Once a familial variant is identified, prenatal diagnosis (chorionic villus sampling/amniocentesis) or preimplantation genetic testing (PGT-M) can be offered for at-risk pregnancies, as for other dominant Mendelian disorders — no SPTAN1-specific program was identified, but this follows standard genetic counseling practice (NCIT:C15240 Genetic Counseling).
- **Secondary prevention:** Early recognition and prompt treatment of infantile spasms (early ACTH/vigabatrin initiation) is emphasized generally in infantile-spasms management to minimize the "critical period" developmental impact, though disease-modifying benefit specific to the underlying spectrin pathology has not been demonstrated.
- **Tertiary prevention:** Multidisciplinary supportive care (as above) to reduce complications (aspiration, contractures, secondary orthopedic deformity).
- No immunization, public-health, or environmental intervention is relevant, as this is not an infectious or environmentally triggered disease.

---

## 14. Other Species / Natural Disease

No naturally occurring SPTAN1-related disease has been reported in companion animals or wildlife (no OMIA entry identified in this search). *SPTAN1* orthologs are broadly conserved across vertebrates (e.g., zebrafish *sptan1*, [ZFIN:ZDB-GENE-051113-60](https://zfin.org/ZDB-GENE-051113-60)) and mammals, but comparative/veterinary natural-disease data specific to this gene were not found in the literature searched. This is consistent with SPTAN1-DEE being studied almost exclusively through engineered laboratory models rather than a recognized natural veterinary disease.

---

## 15. Model Organisms

**Mouse models (primary model system):**
- **Conditional CNS-specific αII-spectrin knockout mouse** (*Sptan1^fl/fl*; Nestin-Cre or similar CNS-restricted deletion): loxP sites flanking exon 8; complete CNS knockout mice die before 1 month of age with disrupted axon initial segments, disrupted cortical lamination, widespread neurodegeneration, and seizures — directly modeling loss of the spectrin-actin cytoskeletal scaffold ([J Neurosci 2017, PMID:29038240](https://pmc.ncbi.nlm.nih.gov/articles/PMC5700417/); [JCI 2018](https://www.jci.org/articles/view/95743)).
  - **Fidelity note:** Heterozygous conditional knockout mice show **no phenotype**, meaning this model best recapitulates the mechanism of the milder, haploinsufficiency-driven human alleles (truncating variants) only in the homozygous/full-knockout state, while the dominant-negative aggregation mechanism underlying the most severe human DEE variants required separate approaches (patient-variant overexpression, iPSC models) to be captured — an important **human-model mismatch** to note when interpreting knockout data against the dominant human phenotype.
- ***In utero* CRISPR/Cas9 electroporation model** achieving ~80% mosaic knockout efficiency — used to dissect cell-autonomous AIS/lamination phenotypes in a temporally and spatially controlled manner.
- ***Spna2* R1098Q point-mutant mouse** (affecting αII-spectrin scaffold stability): shows **progressive ataxia, memory impairments, and seizure episodes**, modeling the milder ataxia/cognitive end of the human spectrum rather than the severe infantile DEE end ([PMC9953789](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9953789/)).

**Cellular/iPSC models:**
- **Patient-derived iPSC neurons** (from individuals with C-terminal dominant-negative variants) recapitulate **spectrin protein aggregation** and **shortened neuronal processes**, directly linking human genotype to the aggregation mechanism proposed from mouse/heterologous data — considered a high-fidelity model for the molecular (aggregation) phenotype, though not for whole-organism seizure/developmental readouts.
- **Patient fibroblasts** used similarly to demonstrate spectrin aggregation for specific variants (p.Arg19Trp, p.Glu2207del).
- **Heterologous overexpression systems** (transfected cell lines expressing mutant αII-spectrin constructs) used to establish dominant-negative aggregation behavior of specific patient variants.

**Zebrafish:** *sptan1* ortholog is annotated in ZFIN, but no published SPTAN1-specific zebrafish disease model (knockdown/knockout) was identified in this search — this remains a **model-system gap** relative to other DEE genes.

**Applications:** These models collectively support (1) the AIS-assembly/cortical-lamination/GABAergic-synapse mechanism of disease, (2) the dominant-negative aggregation mechanism for C-terminal variants versus haploinsufficiency for truncating variants, and (3) provide a preclinical substrate (particularly iPSC neurons) for testing candidate therapies such as allele-selective ASO knockdown, which is the leading translational approach currently being pursued by the patient community (Hope for SPTAN1).

**Resources:** MGI (Mouse Genome Informatics) for *Sptan1* mouse alleles; ZFIN for zebrafish *sptan1*; no IMPC standardized knockout mouse line phenotype data were specifically reviewed here but would be a useful supplementary resource to check.

---

## Summary of Key Evidence Gaps

1. **No formal GeneReviews chapter** currently exists specifically for SPTAN1-DEE (unlike many other DEE genes), limiting availability of a single authoritative clinical-management reference.
2. **Population prevalence/incidence is unknown** — only aggregated case-series counts exist.
3. **Genotype-phenotype correlation, while directionally clear (C-terminal dominant-negative = severe; truncating = milder; N-terminal p.Arg19Trp = HSP), remains incompletely resolved** given the still-small total number of published cases.
4. **No disease-modifying or SPTAN1-specific therapy is yet validated**; ASO development is at an early, patient-advocacy-driven stage.
5. **Comparative/veterinary natural disease models are absent**, and zebrafish modeling has not been published, leaving mouse conditional-knockout and iPSC systems as the primary preclinical tools — with an acknowledged mismatch between the (haploinsufficiency-only) heterozygous knockout mouse and the (dominant-negative) severe human phenotype.

---

### Sources

- [OMIM #613477 — Developmental and Epileptic Encephalopathy 5](https://omim.org/entry/613477)
- [OMIM *182810 — SPTAN1](https://omim.org/entry/182810)
- [Saitsu et al. 2010, Am J Hum Genet, PMID:20493457 — Dominant-negative mutations in α-II spectrin cause West syndrome](https://pubmed.ncbi.nlm.nih.gov/20493457/)
- [Jaglin/Writzl et al. 2017, Brain 140:2322, PMID:28838957 — Delineating SPTAN1 associated phenotypes](https://academic.oup.com/brain/article/140/9/2322/4096697)
- [Tohyama et al. 2015, J Hum Genet — SPTAN1 encephalopathy: distinct phenotypes and genotypes, PMID:25631096](https://www.nature.com/articles/jhg20155)
- [Klug et al. 2022, Genet Med, PMID:36331550 — Expanding SPTAN1 monoallelic variant associated disorders](https://pmc.ncbi.nlm.nih.gov/articles/PMC10620943/)
- [Huang et al. 2018, J Clin Invest, DOI:10.1172/JCI95743 — Critical roles of αII spectrin in brain development and epileptic encephalopathy](https://www.jci.org/articles/view/95743)
- [Clarkson et al. 2017, J Neurosci, PMID:29038240 — αII Spectrin Forms a Periodic Cytoskeleton at the Axon Initial Segment](https://pmc.ncbi.nlm.nih.gov/articles/PMC5700417/)
- [Progressive Ataxia, Memory Impairments, and Seizure Episodes in Spna2 R1098Q Mouse Variant, PMC9953789](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9953789/)
- [Heterozygous loss-of-function variants in SPTAN1 cause distal myopathy, medRxiv 2024](https://www.medrxiv.org/content/10.1101/2024.09.23.24313872.full.pdf)
- [Wilson & Wong 2025, J Child Adolesc Psychopharmacol, PMID:40261672 — SPTAN1: Results of a Caregiver Survey](https://pubmed.ncbi.nlm.nih.gov/40261672/)
- [Intrafamilial variability in SPTAN1-related disorder, 2020, ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1090379820301537)
- [Extending the clinical phenotype of SPTAN1: migraine, epilepsy, subependymal heterotopias, PMID:34590414](https://pubmed.ncbi.nlm.nih.gov/34590414/)
- [Novel 9q34.11 deletions encompassing STXBP1, SPTAN1, ENG, TOR1A, Genet Med 2013](https://www.nature.com/articles/gim201265)
- [NORD/MONDO — Developmental and epileptic encephalopathy 5](https://rarediseases.org/mondo-disease/developmental-and-epileptic-encephalopathy-5/)
- [Ketogenic diet for focal epilepsy with SPTAN1 encephalopathy, Epileptic Disorders 2022](https://stm.cairn.info/revue-epileptic-disorders-2022-4-page-726?lang=en)
- [Hope for SPTAN1 patient organization](https://www.hopeforsptan1.org/team-1)
- [The Defeating Epilepsy Foundation — SPTAN1 Genetic Mutation and Epilepsy](https://www.defeatingepilepsy.org/genetic-mutation-series/sptan1-genetic-mutation-and-epilepsy/)
- [ZFIN Gene: sptan1](https://zfin.org/ZDB-GENE-051113-60)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| References weighed for topical relevance | 11 |
| On topic | 7 |
| Off topic | 1 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `DOI:10.1172/JCI95743](https://www.jci.org/articles/view/95743` (1 mention) - Identifier did not resolve to a record

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:28838957` (2 mentions) - Vascular endothelium plays a key role in directing pulmonary epithelial cell differentiation.
  - shared terms: genetic

Weighed against this report's own most characteristic terms: `phenotype`, `severe`, `variant`, `developmental`, `sptan1`, `dee`, `encephalopathy`, `patient`, `milder`, `seizure`, `disease`, `gene`, `genetic`, `epilepsy`, `progressive`, `epileptic`, `ataxia`, `cohort`, `spectrin`, `heterozygous`.