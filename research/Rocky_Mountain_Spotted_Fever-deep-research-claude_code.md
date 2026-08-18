---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-02T14:17:31.442467'
end_time: '2026-08-02T14:22:09.406702'
duration_seconds: 277.96
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Rocky Mountain spotted fever
  mondo_id: ''
  category: Infectious Disease
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
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 20
  num_turns: 23
  total_cost_usd: 1.8624720999999997
  session_id: b20bd498-c3d4-5201-8d0b-983a970fa830
  stop_reason: end_turn
citation_count: 28
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Rocky Mountain spotted fever
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Rocky Mountain spotted fever** covering all of the
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

I now have comprehensive research coverage. Compiling the full report.

# Rocky Mountain Spotted Fever (RMSF): Comprehensive Disease Research Report

## 1. Disease Information

**Overview:** Rocky Mountain spotted fever (RMSF) is a rare, acquired, life-threatening tick-borne infectious disease caused by *Rickettsia rickettsii*, an obligate intracellular, Gram-negative bacterium of the spotted fever group (SFG) rickettsiae. It is characterized by an acute onset of fever, malaise, and severe headache, followed in most patients by a characteristic centripetally-spreading petechial rash. It is the most severe and most frequently fatal rickettsial illness in the United States [Orphanet: Rocky Mountain spotted fever](https://www.orpha.net/en/disease/detail/83311).

**Key Identifiers:**
- **Orphanet ID:** ORPHA:83311
- **MONDO ID:** MONDO:0019359
- **ICD-10-CM:** A77.0
- **ICD-11:** 1C31.0
- **UMLS CUI:** C0035793
- **MeSH:** D012373 (Rocky Mountain Spotted Fever)
- No dedicated OMIM entry exists (RMSF is an acquired infectious disease, not a classically Mendelian OMIM phenotype)

**Synonyms/alternative names:** Tick typhus (Americas); "spotted fever" (historical, non-specific); São Paulo fever / febre maculosa brasileira (Brazilian form, caused by the same organism); New World spotted fever. Note: "spotted fever" as a general term (Wikidata Q9274700) also covers other SFG rickettsioses (Mediterranean spotted fever/*R. conorii*, etc.) and should not be conflated with RMSF specifically.

**Data source type:** Information is derived from aggregated disease-level resources (CDC national surveillance case counts, MMWR clinical guidelines, Orphanet/GARD rare disease summaries) and primary/case-series literature (individual patient case reports and cohort studies), rather than large-scale structured EHR datasets — consistent with a notifiable infectious disease under public health surveillance.

Sources: [CDC – About RMSF](https://www.cdc.gov/rocky-mountain-spotted-fever/about/index.html), [GARD](https://rarediseases.info.nih.gov/diseases/7585/rocky-mountain-spotted-fever), [NORD](https://rarediseases.org/rare-diseases/rocky-mountain-spotted-fever/), [StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK430881/)

---

## 2. Etiology

**Disease causal factor:** RMSF is caused exclusively by infection with ***Rickettsia rickettsii*** (an obligate intracellular alphaproteobacterium, order Rickettsiales, family Rickettsiaceae), transmitted to humans via the bite of an infected hard tick. This is a purely infectious etiology — there is no known genetic disease-causing mutation; rather, host genetics modulates *severity* (see below), not occurrence.

**Risk factors — environmental/exposure:**
- Tick exposure through outdoor occupational or recreational activity in endemic regions (camping, hiking, gardening, dog ownership) [CDC Data & Statistics](https://www.cdc.gov/rocky-mountain-spotted-fever/data-research/facts-stats/index.html)
- Age >40 years is associated with highest reported incidence [CDC](https://www.cdc.gov/rocky-mountain-spotted-fever/data-research/facts-stats/index.html)
- Male sex and possibly alcohol abuse are associated with increased risk of severe/fatal outcomes
- Geographic residence in high-incidence states (North Carolina, Oklahoma, Arkansas, Tennessee, Missouri — >60% of U.S. cases) and in Arizona/northern Mexico border regions where *Rhipicephalus sanguineus* (brown dog tick)-associated epidemics produce unusually high incidence and case-fatality, particularly in children
- Delay in initiating doxycycline (beyond day 5 of illness) is the single strongest modifiable risk factor for severe or fatal outcome

**Genetic risk factor — G6PD deficiency:** Glucose-6-phosphate dehydrogenase (G6PD) deficiency, an X-linked enzymopathy affecting ~10% of Black males in the U.S., is a documented genetic risk factor for **fulminant** RMSF (death by day 5 of illness). Walker et al. (PMID: [6687526](https://pubmed.ncbi.nlm.nih.gov/6687526/)) reported that "all three patients were male individuals of African descent with glucose-6-phosphate dehydrogenase (G6PD) deficiency," presenting with extensive thrombosis, fibrin thrombi at infection sites, absent/preterminal rash, severe pulmonary lesions, and shock-related organ damage including hepatic necrosis, despite minimal mononuclear inflammatory response on microscopy — an atypical, hyperacute pathological picture distinct from the classic vasculitic course.

**Protective factors:** No specific host genetic protective variant has been established. Prompt tick removal (reducing attachment time below the transmission threshold) and antimicrobial chemoprophylaxis are not recommended as primary prevention (post-exposure prophylactic antibiotics are explicitly discouraged by CDC because they may only delay, not prevent, illness).

**Gene–environment interaction:** The G6PD–RMSF interaction is the clearest documented gene-environment interaction: the underlying enzymatic deficiency does not cause disease alone but interacts with rickettsial infection (likely via unknown secondary effects of oxidative/hemolytic stress) to produce an accelerated, fulminant, thrombotic phenotype rather than the more typical subacute vasculitic course.

Suggested ontology terms: NCBITaxon:783 (*Rickettsia rickettsii*, per NCBI Taxonomy — verify directly), CHEBI/HGNC: **G6PD** (hgnc:4057).

---

## 3. Phenotypes

RMSF phenotypes are best organized as: (a) classic triad/early symptoms, (b) rash evolution, (c) gastrointestinal, (d) laboratory abnormalities, (e) neurological, (f) multi-organ/severe complications.

### Classic triad
The classic triad of fever, headache, and rash is present in **<5% of patients in the first 3 days of illness**, rising to **60–70% by the second week** [CDC](https://www.cdc.gov/rocky-mountain-spotted-fever/hcp/signs-symptoms/index.html); [emedicine](https://emedicine.medscape.com/article/228042-clinical). This low early sensitivity is the central diagnostic challenge in RMSF — treatment must not await the full triad.

- **Fever** — HP:0001945 (Fever); nearly universal, acute onset
- **Severe headache** (typically frontal) — HP:0002315 (Headache); majority of patients
- **Malaise/fatigue** — HP:0033834 or HP:0012378 (Fatigue)
- **Myalgia** — HP:0003326 (Myalgia)

### Cutaneous
- **Rash** — HP:0000988 (Skin rash). Occurs in ~90% of cases eventually, but only in 1–4 days after symptom onset and in <50% during the first 3 days of illness. Classic evolution: begins on ankles/wrists as small, discrete, macular, blanching, rose-colored lesions; spreads centripetally to trunk and head over hours to days; becomes papular, then petechial/purpuric by day 2–3 of rash [CDC signs & symptoms](https://www.cdc.gov/rocky-mountain-spotted-fever/hcp/signs-symptoms/index.html).
- **Petechiae/purpura** — HP:0000965 (Petechiae) / HP:0000978 (Bruising); a late, severity-associated sign
- Histopathology (skin biopsy): lymphohistiocytic capillaritis and venulitis with perivascular/interstitial infiltrate and erythrocyte extravasation; leukocytoclastic vasculitis with neutrophilic infiltrate and nuclear dust seen in 73% of biopsies; fibrin thrombi and capillary-wall necrosis in a minority; immunohistochemical staining for *R. rickettsii* is positive in affected endothelium in nearly all confirmed cases but only ~70% sensitive overall (Kao et al., *J Cutan Pathol* 1997; [PMC workup ref](https://emedicine.medscape.com/article/228042-workup)).

### Gastrointestinal
Gastrointestinal symptoms (anorexia, nausea, vomiting, abdominal pain) occur in up to **80%** of patients; diarrhea in up to **45%** — commonly leading to misdiagnosis as gastroenteritis, especially in children [PMC8159303](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8159303/).
- HP:0002018 (Nausea), HP:0002013 (Vomiting), HP:0002014 (Diarrhea), HP:0002027 (Abdominal pain), HP:0002039 (Anorexia)

### Laboratory abnormalities
- **Thrombocytopenia** — HP:0001873; ~60% of patients; mechanistically attributed to intravascular platelet consumption from vasculitic endothelial injury
- **Hyponatremia** — HP:0002902; found in ~50–60% of cases, more common with CNS involvement, mechanistically linked to SIADH secondary to CNS vasculitis/inflammation
- **Elevated liver enzymes** — HP:0002910 (Elevated hepatic transaminase); >70% of patients with enzyme testing show at least one abnormality
- **Elevated CSF protein/pleocytosis** — CSF WBC >5/µL (pleocytosis) in 87.5% of meningoencephalitis cases; median CSF WBC 41 cells/µL; elevated protein (>50 mg/dL) in 87.5%; hypoglycorrhachia in 18.8% [PMC5781900](https://pmc.ncbi.nlm.nih.gov/articles/PMC5781900/)

### Neurological (severe disease)
- **Meningoencephalitis** — HP:0002480 or HP:0002383 (Encephalitis); altered mental status, focal neurologic deficits, increased tone, reflex abnormalities
- **Cerebral edema, cerebral infarction/stroke, cerebral vasospasm** — HP:0002119 (Cerebral vasculitis-related); "starry sky" appearance on neuroimaging (perivascular/deep white-matter microinfarcts), especially in children
- Autopsy in fatal RMSF encephalitis shows gliosis, demyelination, and necrosis in affected brain regions

### Multi-organ complications (severe/fatal disease)
Hepatic injury, renal failure, lobar pneumonia (non-cardiogenic pulmonary edema), meningoencephalitis, cardiac or respiratory failure, and disseminated intravascular coagulation (DIC) — typically emerging 8–15 days after onset in untreated/undertreated patients.

### Phenotype characteristics
- **Onset:** Acute, 3–12 days post-tick-attachment (average ~7 days)
- **Severity:** Highly variable — from self-limited febrile illness to fulminant multi-organ failure within 5 days (G6PD-deficient patients)
- **Progression:** Rapidly progressive if untreated; can be halted/reversed with early doxycycline
- **Quality of life impact:** Long-term sequelae in survivors of severe (especially pediatric encephalitic) disease include behavioral disturbances and learning disabilities as the most commonly reported long-term problems [MedLink Neurology](https://www.medlink.com/articles/cns-infection-with-rickettsia-species-and-related-organisms); limb amputation has been reported after severe peripheral vasculitis/gangrene in fulminant cases.

---

## 4. Genetic/Molecular Information

RMSF is **not a Mendelian/monogenic disease** — there is no causal human gene. The relevant "genetic/molecular information" for this KB entry is twofold: (a) the human host modifier gene (G6PD) affecting severity, and (b) the pathogen's molecular virulence determinants.

**Host modifier gene:**
- **G6PD** (glucose-6-phosphate dehydrogenase; HGNC:4057; X-linked) — deficiency is a documented severity modifier associated with fulminant, rapidly fatal RMSF (PMID: 6687526). This is not a "pathogenic variant causing RMSF" in the classic sense but a modifier/susceptibility relationship (`relationship_type: MODIFIER` or `SUSCEPTIBILITY` in dismech schema terms) — no specific G6PD allele/variant was singled out in the literature beyond "G6PD deficiency" broadly (common variants: G6PD A- in African-descent populations).

**Pathogen (*R. rickettsii*) virulence factors — molecular mechanism:**
- **rOmpA** (outer membrane protein A, gene *ompA*) — surface autotransporter protein conserved throughout the spotted fever group; implicated in adhesion to host cells. Notably, targeted knockout of *ompA* in *R. rickettsii* did **not** diminish virulence in a mammalian (guinea pig) model, indicating redundancy among adhesins (Noriea et al., *mBio* 2015; [PMC4453529](https://pmc.ncbi.nlm.nih.gov/articles/PMC4453529/)).
- **rOmpB** (outer membrane protein B, gene *sca5*) — conserved across both spotted-fever and typhus groups; implicated in both adhesion and invasion via interaction with the host receptor Ku70.
- **Sca1, Sca2, Sca4 ("gene D")** — additional surface-cell-antigen (sca) family autotransporter proteins; Sca1 is the only sca gene present in all sequenced *Rickettsia* genomes.
- **Host receptor Ku70** — a subunit of DNA-dependent protein kinase (DNA-PKcs), identified as a mammalian receptor mediating rickettsial (initially characterized for *R. conorii*, homologous mechanism proposed for *R. rickettsii*) internalization via OmpB–Ku70 interaction, requiring cholesterol-rich membrane microdomain ubiquitination (mediated by c-Cbl ubiquitin ligase) and engaging clathrin/caveolin-2-dependent endocytosis (Martinez et al., *Cell* 2005, PMID: [16360032](https://pubmed.ncbi.nlm.nih.gov/16360032/)).
- Additional endothelial receptors implicated with partial (~40% each) contribution when silenced individually: **α2β1 integrin, FGFR1, Epac1** — indicating multiple redundant invasion pathways.
- Post-invasion, *R. rickettsii* rapidly escapes the transient phagocytic vacuole (via phospholipase activity) to replicate freely in the host cytoplasm by binary fission, and spreads cell-to-cell by hijacking host actin polymerization machinery (actin-based motility), analogous to *Listeria*/*Shigella*.

**Functional consequence:** Loss-of-function of individual adhesins does not abrogate virulence (redundancy), but disruption of the invasion/intracytoplasmic-survival machinery broadly is essential to intracellular parasitism and endothelial tropism.

**Epigenetics / chromosomal abnormalities:** Not applicable — RMSF has no described epigenetic disease mechanism or chromosomal abnormality; it is an acute bacterial infection.

Suggested ontology terms: **hgnc:4057** (G6PD); GO:0044409 (entry into host), GO:0075512 (clathrin-dependent endocytosis of virus by host cell — analogous GO term set exists for bacteria under GO:0035821 modulation of process of another organism); CHEBI not directly applicable to pathogen proteins.

---

## 5. Environmental Information

**Environmental/vector factors:**
- **Primary tick vectors (United States):**
  - ***Dermacentor variabilis*** (American dog tick) — most frequently associated with transmission; found in eastern, central, and Pacific coastal U.S.
  - ***Dermacentor andersoni*** (Rocky Mountain wood tick) — western U.S. vector
  - ***Rhipicephalus sanguineus*** (brown dog tick) — increasingly important vector in Arizona and along the U.S.–Mexico border, associated with unusually high incidence and case-fatality (especially pediatric) in that region
- Free-roaming dog populations and peridomestic tick infestations are key amplifying factors in the brown-dog-tick-driven Arizona/Sonora epidemic
- Tick attachment duration is a critical transmission determinant: unfed nymphs/adults require >10 hours of attachment for transmission, whereas ticks that have already partially fed can transmit in as little as ~10 minutes (reflecting rickettsial "reactivation"/increased virulence after a blood meal) — earlier literature commonly cites a 4–6 hour minimum attachment threshold.
- **Seasonality:** Peak May–August (tick questing season), though cases occur year-round, especially in warmer southern latitudes.

**Lifestyle factors:** Occupational/recreational outdoor activity (agriculture, forestry, hiking, camping), dog ownership (dogs both serve as sentinel hosts and can carry ticks into the home/peridomestic environment).

**Infectious agent:** ***Rickettsia rickettsii*** — obligate intracellular, aerobic, Gram-negative coccobacillus; taxonomically placed in order Rickettsiales, family Rickettsiaceae, genus *Rickettsia*, spotted fever group. (NCBI Taxonomy ID for *R. rickettsii* should be independently confirmed at ncbi.nlm.nih.gov/taxonomy — not definitively retrieved in this search pass.)

Sources: [CDC clinical overview](https://restoredcdc.org/www.cdc.gov/rocky-mountain-spotted-fever/hcp/clinical-overview/index.html), [MMWR RR6502a1](https://www.cdc.gov/mmwr/volumes/65/rr/rr6502a1.htm)

---

## 6. Mechanism / Pathophysiology

**Causal chain overview:** Tick bite → dermal/subcutaneous rickettsial inoculation → hematogenous/lymphatic dissemination → **endothelial cell invasion** (via OmpA/OmpB-mediated adhesion, Ku70/integrin/FGFR1/Epac1-mediated receptor engagement, and cholesterol-microdomain-dependent, ubiquitin/clathrin/caveolin-2-facilitated endocytosis) → rapid escape from the phagosome into free cytoplasmic residence → intracellular replication and cell-to-cell spread via actin-based motility → **direct and immune-mediated endothelial injury** → **disseminated small-vessel vasculitis** → increased microvascular permeability, coagulation activation, and multi-organ dysfunction.

**Endothelial injury and vascular permeability (central pathophysiologic event):** "Fatal rickettsioses are fundamentally a vasculitis" — *R. rickettsii* directly infects microvascular endothelial cells throughout the body, and the dominant pathophysiological effect is markedly increased vascular permeability, producing vasogenic cerebral edema and non-cardiogenic pulmonary edema (Walker/Olano/UTMB review; [ScienceDirect overview](https://www.sciencedirect.com/topics/medicine-and-dentistry/rickettsia-rickettsii)). A key molecular mechanism: rickettsial infection induces **phosphorylation of VE-cadherin**, directly attenuating homophilic adherens-junction protein–protein interactions, causing endothelial paracellular barrier dysfunction and microvascular hyperpermeability (Woods & Olano, PMC3373609). Rickettsial infection also disrupts and reduces the tight-junction protein **zonula occludens-1 (ZO-1)**, associated with **inflammasome activation** (PMC11784141). Oxidative injury via generation of oxygen free radicals by infected endothelial cells further compounds membrane injury (PMID 9720025-class studies).

**Coagulopathy/thrombocytopenia:** Endothelial injury exposes subendothelial collagen/tissue factor, triggering platelet adhesion/activation and consumption (intravascular platelet destruction), together with mild activation of the coagulation cascade (increased fibrinogen, mildly prolonged aPTT) — producing the characteristic thrombocytopenia and, in severe/fulminant cases, disseminated intravascular coagulation with fibrin thrombi (PMID: [2105679](https://pubmed.ncbi.nlm.nih.gov/2105679/), canine model). Retinal vasculitic foci correlate temporally (24–48h post-fever onset) with areas of altered vascular permeability, providing a directly visualizable model of the systemic process.

**Immune response:** Clearance of rickettsiae is critically dependent on **cytotoxic CD8+ T lymphocytes and interferon-gamma (IFN-γ)** — in murine models, MHC class I-knockout mice were >50,000-fold more susceptible to lethal rickettsial infection than wild-type, indicating CTL activity is more critical than IFN-γ effects alone for recovery (Walker, Olano, Feng; PMID: [11179362](https://pubmed.ncbi.nlm.nih.gov/11179362/)). CD4+ T cells also contribute via macrophage activation (iNOS/NO-mediated bactericidal activity), and macrophages/infiltrating T-lymphocytes produce cytokines that both control infection and, paradoxically, worsen vascular permeability/injury as part of the host inflammatory response to endothelial infection (PMC3691998, "Host Defenses to *R. rickettsii* Infection Contribute to Increased Microvascular Permeability").

**Cellular processes and cell types involved:**
- **Endothelial cells** (primary target; CL:0000115 endothelial cell) — direct infection, junctional disruption, apoptosis-resistance subversion to prolong the intracellular replicative niche
- **Platelets** (CL:0000233) — consumption/aggregation at sites of endothelial injury
- **Macrophages/monocytes** (CL:0000235) and **CD8+/CD4+ T lymphocytes** (CL:0000625, CL:0000624) — immune clearance and inflammatory amplification
- **Perivascular dermal and CNS vasculature** — site of clinically visible vasculitis (skin) and of encephalitis-associated microinfarction (brain)

**Tissue damage mechanisms:** Vasculitis-driven ischemia/microinfarction, vasogenic edema, oxidative stress, and (in fulminant G6PD-deficient cases) thrombotic microangiopathy with fibrin thrombi and organ necrosis (notably hepatic necrosis) in the near-absence of the typical mononuclear inflammatory infiltrate — suggesting a distinct, more hyperacute/thrombotic pathological subtype in this genetically susceptible group.

**Suggested GO terms:**
- GO:0007566 / more precisely bacterial entry processes — GO:0044409 (entry into host), GO:0035821 (modulation of process of another organism)
- GO:0016477 (cell migration) / actin-based motility analogous to GO:0030044 (in intracellular pathogen movement literature, often annotated under host actin cytoskeleton reorganization, GO:0030036)
- GO:0034332 (adherens junction organization) — for VE-cadherin disruption
- GO:0002532 (production of molecular mediator involved in inflammatory response), GO:0050818 (regulation of coagulation)
- GO:0001525 (angiogenesis) not directly relevant; better: GO:0061028 (establishment of endothelial barrier), GO:0061028 disruption

**Suggested CL terms:** CL:0000115 (endothelial cell), CL:0000235 (macrophage), CL:0000624 (CD4-positive T cell), CL:0000625 (CD8-positive T cell), CL:0000233 (platelet)

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Skin/cutaneous microvasculature (rash), systemic small blood vessels (arterioles, capillaries, venules) throughout the body — RMSF is fundamentally a **systemic small-vessel vasculitis**, not confined to one organ.
- **Secondary/complication organs:** Brain (meningoencephalitis, cerebral edema, infarction — UBERON:0000955), lungs (non-cardiogenic pulmonary edema/ARDS — UBERON:0002048), liver (hepatocellular injury/necrosis — UBERON:0002107), kidneys (acute kidney injury — UBERON:0002113), heart (myocarditis/cardiac dysfunction — UBERON:0000948), gastrointestinal tract (UBERON:0001555, prominent early symptoms), retina (vasculitis visible on fundoscopy — UBERON:0000966), adrenal glands (case reports of adrenal hemorrhage/adrenalectomy)
- **Body systems involved:** Integumentary, cardiovascular, nervous, respiratory, digestive, renal, hematologic/coagulation

**Tissue/cell level:**
- Vascular endothelium (UBERON:0002316 blood vessel endothelium) is the principal cellular target — infection is fundamentally endotheliotropic
- Dermal capillaries/venules (histopathology: lymphohistiocytic capillaritis/venulitis)
- CNS white matter (perivascular microinfarcts, demyelination in fatal encephalitis)

**Subcellular level:**
- Host cytoplasm (site of rickettsial replication after phagosomal escape) — GO:0005737
- Cholesterol-enriched plasma membrane microdomains (site of Ku70-mediated invasion) — GO:0005886 / lipid raft GO:0045121
- Adherens junctions (VE-cadherin) — GO:0005912; tight junctions (ZO-1) — GO:0005923

**Localization:** Systemic/disseminated — not focal or lateralized; skin rash is bilateral, acral-onset with centripetal spread.

---

## 8. Temporal Development

- **Onset:** Acute; incubation period 3–12 days post-tick-attachment, average ~7 days (shorter incubation correlates with higher inoculum/exposure magnitude)
- **Onset pattern:** Abrupt febrile illness
- **Progression:** Classic disease course over the first 1–2 weeks: nonspecific febrile prodrome (days 1–3, often without rash) → rash onset (days 3–5) → petechial/purpuric evolution (days 5–7) → in untreated or delayed-treatment cases, multi-organ complications (days 8–15) → death (median around day 8–9 in fatal untreated cases; as early as day 5 in "fulminant" G6PD-deficient cases)
- **Disease course pattern:** Monophasic acute illness (not relapsing-remitting); resolves fully with prompt treatment; can progress to fulminant multisystem failure without treatment
- **Duration:** Self-limited with appropriate antibiotic therapy (clinical improvement typically within 24–72 hours of starting doxycycline); potentially fatal (days) without treatment
- **Remission:** Treatment-induced; no spontaneous remission mechanism reported once vasculitic phase is established — untreated case-fatality is 20–30%
- **Critical period for intervention:** Treatment initiated within the first 5 days of symptom onset is strongly associated with reduced morbidity/mortality — this is the single most important "critical window" in RMSF management

---

## 9. Inheritance and Population

RMSF is an acquired infectious disease with **no Mendelian inheritance pattern**. Population/epidemiological data:

**Epidemiology:**
- 2023 U.S. surveillance: **1,205 cases** of spotted fever rickettsioses (including RMSF) reported to CDC [CDC Data & Statistics](https://www.cdc.gov/rocky-mountain-spotted-fever/data-research/facts-stats/index.html)
- Geographic concentration: >60% of cases in North Carolina, Oklahoma, Arkansas, Tennessee, and Missouri
- Distinct high-incidence/high-case-fatality foci: Arizona and northern Mexico border regions (brown-dog-tick-transmitted, disproportionately affecting children)
- **Seasonality:** year-round with a strong May–August peak

**"Inheritance"-analog (host modifier):** G6PD deficiency is X-linked recessive (as a modifier, not disease-causing) — hemizygous males (and rarely homozygous females) are at higher risk for fulminant disease.

**Population demographics:**
- **Age:** Highest reported incidence in adults >40 years old, but case-fatality is disproportionately high in young children (especially in the Arizona/brown-dog-tick epidemic)
- **Sex:** Male sex is associated with increased risk of severe/fatal complications
- **Ethnicity/genetic background:** African-descent males with G6PD deficiency are at particular risk for fulminant, rapidly fatal disease
- **Mortality:** Case-fatality rate <0.5% with modern treatment nationally (varies significantly by region — much higher, historically 20-30%, in the pre-antibiotic/untreated era, and elevated in the Arizona tribal-community outbreaks)

Sources: [CDC facts & stats](https://www.cdc.gov/rocky-mountain-spotted-fever/data-research/facts-stats/index.html), [MMWR RR6502a1](https://www.cdc.gov/mmwr/volumes/65/rr/rr6502a1.htm), [PMC12928218 — pediatric mortality predictors, Sonora Mexico](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12928218/)

---

## 10. Diagnostics

**Clinical/laboratory tests:**
- **PCR** — detects *R. rickettsii* DNA from blood, plasma, or skin biopsy tissue; limited sensitivity early because the organism is endotheliotropic and does not circulate in large numbers in blood until disease is advanced; a **negative PCR does not rule out RMSF** and should never delay treatment [CDC diagnosis/testing](https://www.cdc.gov/rocky-mountain-spotted-fever/hcp/diagnosis-testing/index.html)
- **Serology (IFA)** — the standard serologic test is the **indirect immunofluorescence assay (IFA)** for IgG against *R. rickettsii* antigen; requires **paired acute and convalescent sera 2–10 weeks apart** demonstrating a **≥4-fold rise in titer**; antibody titers are frequently negative in the first week of illness (a major diagnostic limitation — serology confirms retrospectively, it does not guide acute treatment decisions)
- **Skin biopsy with immunohistochemistry (IHC)/direct immunofluorescence** — detects rickettsial antigen in endothelial cells of biopsied rash lesions; most sensitive in early disease before antibiotics are started, but available only at specialized reference laboratories (CDC); ~70% sensitivity even under optimal conditions
- **Laboratory abnormalities supportive of diagnosis** (non-specific but pattern-suggestive): thrombocytopenia, hyponatremia, elevated hepatic transaminases, elevated CSF protein/pleocytosis in CNS disease
- **Imaging:** Brain MRI in encephalitic cases may show the "starry sky" pattern of scattered perivascular/deep white-matter microinfarcts, meningeal enhancement, or cerebral edema

**Genetic testing:** Not applicable to the infection itself; G6PD enzyme activity testing (or genetic testing for G6PD variants) may be clinically relevant in patients (especially Black males) presenting with unusually fulminant/hyperacute RMSF, to explain severity and anticipate hemolysis risk, though this is not a diagnostic test for RMSF itself.

**Clinical criteria:** RMSF is a **clinical diagnosis requiring empiric treatment** — CDC/AAP explicitly recommend starting doxycycline based on clinical suspicion (fever + history of tick exposure in an endemic area/season ± rash) without waiting for laboratory confirmation, given the narrow therapeutic window. Case is classified as "probable" or "confirmed" retrospectively per CDC/CSTE surveillance case definitions (using the 4-fold IFA titer rise, PCR, IHC, or culture isolation as confirmatory criteria).

**Differential diagnosis:** Other spotted fever group rickettsioses, ehrlichiosis, anaplasmosis, meningococcemia, measles, enteroviral illness, viral exanthems, gastroenteritis (particularly in children, given the high frequency of GI symptoms), Kawasaki disease, drug reaction/Stevens-Johnson-type eruptions, leptospirosis, and dengue (in travel-relevant settings).

**Screening:** No population screening program exists; case-finding relies on clinical suspicion in tick-exposed patients during peak season in endemic regions.

Suggested NCIT terms: NCIT:C15473 (Polymerase Chain Reaction), NCIT:C15188 (Serology), skin biopsy → NCIT:C15230 (Biopsy Procedure)/immunohistochemistry NCIT:C16336.

---

## 11. Outcome/Prognosis

**Mortality:**
- **Untreated/inadequately treated:** case-fatality historically 20–30%
- **Treated (modern era):** case-fatality <1% overall; U.S. national surveillance estimates <0.5%, though this varies substantially by region, with much higher rates in specific high-burden pediatric/Indigenous-community outbreaks in Arizona/Sonora
- Risk factors for fatal outcome: advanced age, male sex, delayed diagnosis/treatment (particularly beyond day 5), G6PD deficiency (fulminant subtype), possibly alcohol use disorder

**Morbidity/complications:** Hepatic injury, renal failure, pneumonia/ARDS, meningoencephalitis, cardiac/respiratory failure, DIC, digit/limb gangrene requiring amputation in severe vasculitic/thrombotic cases, and — in survivors of severe pediatric encephalitis — long-term behavioral disturbances and learning disabilities as the most commonly reported sequelae.

**Recovery potential:** Excellent with treatment initiated early (within 5 days) — most patients recover fully without sequelae. Recovery potential drops sharply once multi-organ vasculitic complications (renal failure, ARDS, DIC, encephalitis) have developed.

**Prognostic factors:** Time to treatment initiation (dominant factor), presence/severity of neurologic involvement, G6PD status, age extremes, and degree of thrombocytopenia/coagulopathy at presentation.

---

## 12. Treatment

**Pharmacotherapy (first-line):**
- **Doxycycline** is the first-line treatment for **all patients regardless of age**, including children <8 years old and pregnant women — this is an explicit, evidence-based departure from the older tetracycline-class contraindication in young children. Multiple studies have shown that short courses (5–10 days) of doxycycline used for RMSF, even across up to five treatment courses before age 8, do **not** cause permanent tooth staining or enamel hypoplasia [CDC — doxycycline & tooth staining research](https://www.cdc.gov/anaplasmosis/hcp/doxycycline/index.html). Treatment should begin empirically based on clinical suspicion, ideally within the first 5 days of symptom onset, without waiting for laboratory confirmation.
  - NCIT term: NCIT:C820 (Doxycycline) under NCIT:C15986 (Pharmacotherapy)
- **Chloramphenicol** — the only alternative agent with historical use, reserved for patients with life-threatening doxycycline allergy or in mild disease in pregnant patients; **associated with increased mortality risk** compared to doxycycline and carries risks of aplastic anemia and gray baby syndrome; oral formulation is not available in the U.S.
  - Explicit safety point: "Use of antibiotics other than doxycycline increases the risk of patient death" [emedicine treatment](https://emedicine.medscape.com/article/228042-treatment)

**Pregnancy:** Doxycycline is recommended as first-line even in pregnancy given the severity of untreated RMSF; available data suggest low risk of substantial teratogenicity at RMSF treatment dosing/duration.

**Supportive care:** Fluid/electrolyte management (for hyponatremia), transfusion support for severe thrombocytopenia/coagulopathy, ICU-level supportive care (mechanical ventilation, vasopressors, renal replacement therapy) for fulminant multi-organ disease. NCIT:C15747 (Supportive Care).

**No vaccine currently exists** for RMSF; prevention is entirely non-pharmacologic (see Section 13).

**No targeted/gene/cell/immunotherapies** are applicable — RMSF treatment is standard antimicrobial pharmacotherapy plus supportive care; there are no RMSF-specific clinical trials of novel therapeutics identified in this search (research is ongoing into recombinant rickettsial antigen vaccines, still preclinical/veterinary stage — see canine whole-cell antigen vaccine studies).

---

## 13. Prevention

**Primary prevention (no vaccine available for humans):**
- **Repellents:** EPA-registered repellents containing DEET, picaridin, IR3535, oil of lemon eucalyptus (OLE), PMD, or 2-undecanone applied to skin
- **Acaricide/permethrin:** 0.5% permethrin applied to clothing/gear (not skin) — effective at killing/repelling ticks
- **Protective clothing:** long sleeves/pants, tucking pants into socks
- **Behavioral:** avoiding tall grass, leaf litter, brushy trails, especially May–August in endemic regions
- **Post-exposure:** full-body tick checks, checking pets/gear, showering promptly after outdoor exposure to remove unattached ticks (reducing the critical attachment-time window needed for transmission)

**Secondary prevention:** Prompt tick removal reduces transmission risk given the attachment-time dependence of transmission (though CDC does not recommend prophylactic antibiotics after a tick bite, as data do not support this practice preventing RMSF).

**Public health/vector control:** Environmental/peridomestic acaricide treatment and stray-dog population control have been used as public health interventions in the Arizona/Sonora brown-dog-tick epidemic (modeling studies on *Rhipicephalus sanguineus* control, [PMC8951036](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8951036/)).

**Veterinary/One Health prevention:** Tick control on dogs (topical/oral acaricides) reduces both canine disease and human exposure risk from peridomestic ticks, especially relevant to the brown dog tick transmission cycle.

**Vaccine status:** No licensed human vaccine; experimental whole-cell inactivated *R. rickettsii* vaccines have shown protective efficacy in the canine model (PMC12707144, PMC6346123) but are not available for human use.

---

## 14. Other Species / Natural Disease

**Taxonomy:** *R. rickettsii* naturally infects a broad range of vertebrate hosts and tick vectors across the Americas (North, Central, and South America — the same organism causing "febre maculosa brasileira" in Brazil).

**Natural disease in companion animals — dogs (primary veterinary relevance):**
Dogs are naturally, highly susceptible to *R. rickettsii* infection and serve as important **sentinel hosts** due to high tick exposure. Clinical signs in dogs closely parallel human disease: high fever (up to 105°F/40.6°C), anorexia, lymphadenopathy, polyarthropathy, cough/dyspnea, abdominal pain, vomiting, diarrhea, and facial/limb edema [Merck Veterinary Manual](https://www.merckvetmanual.com/dog-owners/disorders-affecting-multiple-body-systems-of-dogs/rocky-mountain-spotted-fever-tick-fever-in-dogs). A detailed natural-history study of experimentally tick-bite-infected dogs characterized clinical, hematological, molecular, and serological dynamics from exposure through convalescence and relapse (PMC4277292).

**Comparative biology:** The canine disease recapitulates the vasculitic/coagulopathic pathophysiology of human RMSF closely enough that experimental canine infection (via tick bite, the natural route) has been used as a translational model for vaccine development (whole-cell antigen vaccines protective in dogs, PMC6346123, PMC12707144) and for characterizing vascular permeability/coagulation pathophysiology (PMID: [2105679](https://pubmed.ncbi.nlm.nih.gov/2105679/), foundational canine coagulation study).

**Zoonotic/transmission considerations:** RMSF is a zoonosis maintained in nature by tick–small-mammal (and, regionally, tick–dog) cycles; it is **not communicable person-to-person** (with rare, unconfirmed exceptions for blood transfusion; no documented transplant transmission). Dogs act as both amplifying/sentinel hosts and as tick-carriers into human peridomestic environments, making canine surveillance and tick control a key "One Health" intervention point, especially in the brown-dog-tick-driven Arizona epidemic.

---

## 15. Model Organisms

**Mouse models:**
- **C3H/HeN mice** — described as providing "the best model to date for examining rickettsial disease with endothelial infection and injury." While much of the detailed published characterization uses the closely related *R. conorii* (Mediterranean spotted fever agent) in C3H/HeN mice — establishing disseminated endothelial infection by day 1, progressive rickettsemia, and death from vascular-injury-based meningoencephalitis and interstitial pneumonia by day 5–6 — this endothelial-target model system has also been used directly for *R. rickettsii* vaccine/pathogenesis studies. It recapitulates the core human pathophysiology: endotheliotropism, vasculitis-driven CNS and pulmonary injury.
- **MHC class I-knockout mice** (C57BL/6 background) — used to demonstrate the essential role of CD8+ cytotoxic T lymphocytes in rickettsial clearance (>50,000-fold increased susceptibility to lethal outcome vs. wild-type) — a genetic immunodeficiency model rather than a disease-replicating model per se, but critical for defining protective immune mechanisms (PMID: 11179362).
- **Guinea pig model** — used in virulence studies of *R. rickettsii* mutants (e.g., *ompA* knockout, which did not attenuate virulence), providing a classic rickettsiosis animal model with fever and scrotal/testicular necrosis as a virulence readout (Noriea et al., *mBio* 2015).

**Canine model (natural/experimental):** As above — the dog is both a natural disease host and a valuable experimental model (tick-bite-route infection) because it reproduces the vasculitic, coagulopathic, and clinical syndrome of human RMSF with high fidelity, and has been used for both pathophysiology studies (vascular permeability/coagulation, PMID 2105679) and vaccine efficacy testing.

**Model limitations:** Mouse models (especially with *R. conorii* rather than *R. rickettsii* itself) may not fully capture *R. rickettsii*-specific virulence factor biology (e.g., the *ompA* knockout virulence result may not generalize across species); the canine model, while pathophysiologically faithful, does not model human-specific risk factors such as G6PD deficiency-associated fulminant disease. No model has been reported that specifically recapitulates the G6PD-deficiency-associated fulminant/thrombotic human phenotype.

**Applications:** Endothelial infection/injury mechanisms, vascular permeability biology (VE-cadherin phosphorylation, ZO-1 disruption), immune clearance mechanisms (CD8+ T cell/IFN-γ dependence), and vaccine antigen efficacy testing (recombinant/whole-cell antigen protection studies in both mice and dogs).

---

## Ontology Term Summary Table

| Category | Suggested Term | ID |
|---|---|---|
| Disease | Rocky Mountain spotted fever | MONDO:0019359 |
| Disease (Orphanet) | Rocky Mountain spotted fever | ORPHA:83311 |
| Pathogen | *Rickettsia rickettsii* | NCBITaxon:783 (verify) |
| Gene (modifier) | G6PD | hgnc:4057 |
| Phenotype | Fever | HP:0001945 |
| Phenotype | Skin rash | HP:0000988 |
| Phenotype | Petechiae | HP:0000965 |
| Phenotype | Headache | HP:0002315 |
| Phenotype | Thrombocytopenia | HP:0001873 |
| Phenotype | Hyponatremia | HP:0002902 |
| Phenotype | Elevated hepatic transaminase | HP:0002910 |
| Phenotype | Encephalitis/Meningoencephalitis | HP:0002383 |
| Phenotype | Vomiting | HP:0002013 |
| Phenotype | Diarrhea | HP:0002014 |
| Cell type | Endothelial cell | CL:0000115 |
| Cell type | CD8-positive T cell | CL:0000625 |
| Cell type | Macrophage | CL:0000235 |
| Cell type | Platelet | CL:0000233 |
| Anatomy | Blood vessel endothelium | UBERON:0002316 |
| Anatomy | Brain | UBERON:0000955 |
| Anatomy | Liver | UBERON:0002107 |
| Treatment | Doxycycline | NCIT:C820 / CHEBI:50845 |
| Treatment | Chloramphenicol | NCIT:C532 / CHEBI:17698 |

*(Ontology mappings above are research suggestions and should be independently verified with OAK/runoak against the local sqlite adapters before use in a KB entry, per dismech curation SOP.)*

---

## Key Primary Sources Cited

- Walker DH et al. Fulminant Rocky Mountain spotted fever and G6PD deficiency. *Arch Pathol Lab Med* 1983;107(3):121-5. PMID: [6687526](https://pubmed.ncbi.nlm.nih.gov/6687526/)
- Martinez JJ et al. Ku70, a component of DNA-dependent protein kinase, is a mammalian receptor for *Rickettsia conorii*. *Cell* 2005. PMID: [16360032](https://pubmed.ncbi.nlm.nih.gov/16360032/)
- Feng HM, Whitworth T, Popov V, Walker DH. Critical role of cytotoxic T lymphocytes in immune clearance of rickettsial infection. *Infect Immun* 2001;69:1841-6. PMID: [11179362](https://pubmed.ncbi.nlm.nih.gov/11179362/)
- Noriea NF et al. Targeted knockout of the *Rickettsia rickettsii* OmpA surface antigen does not diminish virulence. *mBio* 2015. [PMC4453529](https://pmc.ncbi.nlm.nih.gov/articles/PMC4453529/)
- Woods ME, Olano JP. Host defenses to *Rickettsia rickettsii* infection contribute to increased microvascular permeability. [PMC3691998](https://pmc.ncbi.nlm.nih.gov/articles/PMC3691998/)
- Canine coagulation/vascular permeability study. PMID: [2105679](https://pubmed.ncbi.nlm.nih.gov/2105679/)
- CDC. Diagnosis and Management of Tickborne Rickettsial Diseases, MMWR RR6502a1: [link](https://www.cdc.gov/mmwr/volumes/65/rr/rr6502a1.htm)
- CDC. Signs & Symptoms, Diagnosis/Testing, Clinical Care, Facts & Stats pages: [cdc.gov/rocky-mountain-spotted-fever](https://www.cdc.gov/rocky-mountain-spotted-fever/)
- Orphanet: [ORPHA:83311](https://www.orpha.net/en/disease/detail/83311); GARD: [rarediseases.info.nih.gov](https://rarediseases.info.nih.gov/diseases/7585/rocky-mountain-spotted-fever)

**Note on gaps:** No dedicated OMIM phenotype entry exists (expected, as RMSF is acquired/infectious). Precise NCBI Taxonomy IDs for *Dermacentor variabilis*/*andersoni*/*Rhipicephalus sanguineus* and confirmed *R. rickettsii* NCBITaxon ID were not definitively retrieved in this pass and should be looked up directly at ncbi.nlm.nih.gov/taxonomy before KB entry. No published RMSF-specific GWAS or additional host susceptibility loci beyond G6PD were identified.