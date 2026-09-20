---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-10T00:48:12.125296'
end_time: '2026-08-10T00:54:56.844922'
duration_seconds: 404.72
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Tetralogy of Fallot
  mondo_id: ''
  category: Complex
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
  web_search_requests: 22
  num_turns: 25
  total_cost_usd: 2.2652032
  session_id: ccd9973f-d61b-50a6-8cfe-0a77b122d0f2
  stop_reason: end_turn
citation_count: 71
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Tetralogy of Fallot
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Tetralogy of Fallot** covering all of the
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

# Tetralogy of Fallot (TOF): Comprehensive Disease Characteristics Research Report

## 1. Disease Information

**Overview.** Tetralogy of Fallot (TOF) is the most common cyanotic congenital heart defect (CHD) and a member of the conotruncal (outflow-tract) family of malformations. It is defined by four anatomically related lesions arising from a single embryologic error — anterocephalad (superior and leftward) deviation/malalignment of the infundibular (outlet) septum relative to the muscular ventricular septum: (1) a large, non-restrictive ventricular septal defect (VSD, typically perimembranous, malalignment-type), (2) obstruction of the right ventricular outflow tract (RVOT)/pulmonary stenosis, (3) an aorta that overrides the VSD, and (4) secondary right ventricular hypertrophy (RVH) ([StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK513288/); [Medscape](https://emedicine.medscape.com/article/2063480-overview)).

**Key identifiers:**
- **OMIM:** #187500 (Tetralogy of Fallot) ([OMIM:187500](https://omim.org/entry/187500))
- **Orphanet:** ORPHA:3303 (with a related entry ORPHA:99068 for complete AV septal defect–TOF) ([Orphanet](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Lng=GB&Expert=3303))
- **MONDO:** MONDO:0008542
- **ICD-10-CM:** Q21.3 ([ICD10Data](https://www.icd10data.com/ICD10CM/Codes/Q00-QA0/Q20-Q28/Q21-/Q21.3)); **ICD-9-CM:** 745.2
- **SNOMED CT:** 86299006
- **MeSH:** D013771

**Synonyms:** Fallot tetralogy; TOF; TET; tetralogy of Fallot with pulmonic stenosis. Historically described by Niels Stensen (1672) and later systematically characterized by Étienne-Louis Arthur Fallot (1888).

**Anatomic variants (per the International Society for Nomenclature of Paediatric and Congenital Heart Disease):** TOF with pulmonary stenosis (classic form), TOF with pulmonary atresia (± major aortopulmonary collateral arteries, MAPCAs), TOF with absent pulmonary valve syndrome (APVS), and TOF with complete atrioventricular canal/septal defect ([Medscape](https://emedicine.medscape.com/article/899249-overview); [ISUOG](https://www.isuog.org/education/visuog/obstetrics/heart/abnormal-outflow-tracts/fallot-and-variants/absent-pulmonary-valve-syndrome.html)).

**Evidence basis:** Information below is aggregated across large clinical cohorts, national/regional birth-defect registries, surgical case series, and increasingly whole-exome/whole-genome sequencing cohorts (human clinical, aggregated at the disease level) supplemented by animal-model (mouse, zebrafish) mechanistic studies.

---

## 2. Etiology

### Disease Causal Factors
TOF is a **multifactorial** disease arising from disruption of second heart field (SHF)–derived outflow tract myocardium and cardiac neural crest cell (CNCC) migration during weeks 3–8 of embryogenesis. Roughly 20–25% of cases occur as part of a recognized genetic syndrome or chromosomal abnormality; the remaining ~75–80% are "non-syndromic," with a minority of these attributable to identifiable monogenic causes and the majority presumed multifactorial/polygenic with contributing environmental exposures ([StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK513288/); [PMC9582763](https://pmc.ncbi.nlm.nih.gov/articles/PMC9582763/)).

### Genetic Risk Factors

**Chromosomal/syndromic causes (~20–25% of cases):**
- **22q11.2 deletion syndrome (DiGeorge/velocardiofacial syndrome)** — the single most common identifiable genetic cause, found in **~15%** of all TOF cases (7.4–15% across cohorts) ([PMID:19948535](https://pubmed.ncbi.nlm.nih.gov/19948535/); [Circ Cardiovasc Genet](https://www.ahajournals.org/doi/10.1161/circgenetics.114.000819)). *TBX1* is the principal dosage-sensitive gene within the deleted region. 22q11.2DS-associated TOF shows a distinctive phenotype: proximal pulmonary artery obstruction, hypoplastic central pulmonary arteries, right aortic arch (24%), and interrupted aortic arch (22–48%) ([PMID:19948535](https://pubmed.ncbi.nlm.nih.gov/19948535/)).
- **Trisomy 21 (Down syndrome)** — accounts for **~7%** of TOF cases; ~5–10% of individuals with Down syndrome have TOF, and CHD overall occurs in ~40% of Down syndrome patients.
- **Trisomy 13, Trisomy 18** — less common associations.
- **Alagille syndrome** (*JAG1*, less commonly *NOTCH2*) — Notch-pathway hepato-cardio-vertebral disorder; **1–2%** of TOF patients carry pathogenic *JAG1* variants ([PMID:19948535](https://pubmed.ncbi.nlm.nih.gov/19948535/); [PMID:23956173](https://pubmed.ncbi.nlm.nih.gov/23956173/)).
- **CHARGE syndrome** (*CHD7*) — TOF is relatively frequent among CHARGE-associated conotruncal defects.
- **VACTERL association** — TOF among the cardiac component of this non-random constellation.

**Monogenic/non-syndromic causal and susceptibility genes** (whole-exome/genome sequencing cohorts):
- ***NOTCH1*** and ***FLT4* (VEGFR3)** are the two most frequently implicated genes in large non-syndromic cohorts. In the largest published cohort (n=829), deleterious variants in *NOTCH1* were found in **~4.5%** and *FLT4* in **~2.4%** of patients, "together explaining ~7% of non-syndromic TOF cases" ([PMID:30582441](https://pubmed.ncbi.nlm.nih.gov/30582441/); [PMC12940485](https://pmc.ncbi.nlm.nih.gov/articles/PMC12940485/)). *NOTCH1* variants are predominantly missense; *FLT4* variants are predominantly loss-of-function. Expanding to nine candidate genes captures **~15–16%** of non-syndromic cases.
- ***NKX2-5*** (OMIM *600584) — present in **≥4%** of TOF patients ([PMID:19948535](https://pubmed.ncbi.nlm.nih.gov/19948535/)); mutations identified in TOF patients often map outside the homeodomain and are incompletely penetrant, unlike classical homeodomain-disrupting *NKX2-5* mutations causing isolated ASD/AV block ([Circulation, hc4601.098427](https://www.ahajournals.org/doi/10.1161/hc4601.098427)).
- ***GATA4***, ***GATA6***, ***TBX5***, ***TBX1***, ***ZFPM2 (FOG2)***, ***FOXC2***.
- Signaling-pathway genes: ***JAG1***, ***KDR***, ***NFATC1***, ***PTPN11***, ***PDGFRA***, ***SMAD2/SMAD4***.
- Emerging/splicing-associated candidates: ***PUF60***, ***DVL3***, ***FLNA*** (X-linked), ***MEIS2***, ***SOX11***, ***FLRT2***, ***FKBP10***, ***MST1R***, ***GNE***.
- Ciliary genes: ***DNAH11***, ***DYNC2H1***, ***C2CD3***, ***OFD1*** (PMC12940485).
- ***NEDD4*** — a 2025 mouse-and-human study identified a human *NEDD4* variant associated with TOF; NEDD4 controls DKK1 levels in neural crest cells to modulate Wnt signaling in the SHF (bioRxiv/PMC12913648, model-organism + human variant evidence).

**Common/susceptibility variants (GWAS):**
- Loci at **12q24** and **13q32** reached genome-wide significance in a European TOF GWAS.
- Additional suggestive loci at 10p11, 10p14, 15q13, 16q12.
- A common *PTPN11* variant contributes to TOF risk in Europeans.
- In Chinese cohorts, **rs2228638 in *NRP1* (10p11)** significantly increased TOF risk (OR=1.52, 95% CI 1.13–2.04, P=0.006) ([PMID:24594544](https://pubmed.ncbi.nlm.nih.gov/24594544/)).
- Among 22q11.2 deletion carriers, a modifier GWAS identified **rs12519770 in *GPR98* (ADGRV1) at 5q14.3** (P=2.98×10⁻⁸) as associated with TOF risk specifically within the deletion population ([PMID:29025761](https://pubmed.ncbi.nlm.nih.gov/29025761/)).

**Recurrence risk (empirical/genetic-counseling estimates, PMC12940485):**
- Sporadic non-syndromic TOF, no identified genetic cause: **~2–5%** sibling recurrence risk (consistent with the classically cited 1–5% figure).
- Autosomal dominant monogenic cause identified (*NOTCH1*, *FLT4*, *NKX2-5*, *GATA6*): up to **50%** theoretical recurrence, tempered by incomplete/variable penetrance.
- Chromosomal syndromes (22q11.2 deletion, trisomy 21): typically **<1%** recurrence unless a parent carries a balanced structural rearrangement or is a mosaic/germline carrier.

### Environmental Risk Factors
- **Maternal pregestational diabetes mellitus** — meta-analyses show an increased odds ratio of approximately **3–5** for TOF in offspring; hyperglycemia is teratogenic during first-trimester cardiogenesis and alters embryonic retinoic acid catabolism ([PMC10449132](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10449132/)).
- **Retinoic acid/isotretinoin exposure** — a potent teratogen linked to conotruncal anomalies via interference with cardiac neural crest cell migration.
- **Maternal phenylketonuria (PKU)** with poor metabolic control.
- **Congenital rubella infection.**
- **Advanced maternal age** (>40 years) has been reported as a risk factor.
- **Fetal alcohol exposure and maternal warfarin use** — associated teratogens, though effect sizes for TOF specifically are less robustly quantified than for diabetes/retinoic acid.
- **Family history** of CHD, or parental history of TOF/22q11.2DS.

### Protective Factors
- **Periconceptional folic acid / multivitamin supplementation** is the best-documented protective/preventive factor:
  - A Hungarian cohort study (1980–1996) found high-dose folic acid users (mean 5.6 mg/day) had significantly reduced TOF risk, **OR 0.53** ([search synthesis, cites Czeizel-type Hungarian intervention data]).
  - A Netherlands registry-based case-control study found periconceptional folic acid use associated with an overall reduction in CHD risk ([PMID:19952004](https://pubmed.ncbi.nlm.nih.gov/19952004/)).
  - Broader meta-analytic estimates: periconceptional folic acid use associated with ~20% reduction in prevalence of any CHD, and up to 59% reduction in critical CHD in some cohort analyses; protection is greater when supplementation begins **before conception**.
- No specific genetic protective variants for TOF have been robustly established in the literature reviewed (in contrast to well-characterized protective alleles in other polygenic diseases); this is a **knowledge gap**.

### Gene-Environment Interactions
The 2025/2026 genetics-epigenetics review frames TOF as arising from "convergence of multiple disrupted developmental pathways — Notch, VEGF, and SHF–neural crest signaling — rather than single-gene defects" ([PMC12940485](https://pmc.ncbi.nlm.nih.gov/articles/PMC12940485/)). Maternal hyperglycemia has been mechanistically linked to altered embryonic retinoic acid catabolism, suggesting a shared final pathway between the diabetes and retinoic-acid teratogenic routes ([PMC10449132](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10449132/)). Postnatally, mitochondrial dysfunction and chronic hypoxia interact with genetic background — *FOXO1* is proposed to "act as a metabolic stress sensor" mediating postnatal right-ventricular cardiomyocyte vulnerability in unrepaired/palliated TOF (PMC12940485).

---

## 3. Phenotypes

### Cardinal anatomic/clinical features
| Phenotype | HPO term (suggested) | Frequency | Notes |
|---|---|---|---|
| Ventricular septal defect (malalignment-type) | HP:0001629 | Obligate (100%) | Perimembranous, non-restrictive; may extend to muscular septum |
| Overriding aorta | HP:0002623 | Obligate (100%) | Aortic valve annulus straddles the VSD |
| Right ventricular outflow tract obstruction / pulmonic stenosis | HP:0001642 (Pulmonic stenosis); HP:0004415 (infundibular pulmonic stenosis) | Obligate (100%), severity variable | Infundibular, valvar, supravalvar, or branch PA stenosis, singly or combined |
| Right ventricular hypertrophy | HP:0001714 | Obligate (secondary) | Compensatory, develops post-natally |
| Cyanosis | HP:0000961 | Variable — from birth to adulthood depending on RVOT obstruction severity | "Pink" (acyanotic) TOF possible with mild obstruction |
| Hypercyanotic ("Tet") spells | (no precise single HPO term; consider HP:0000961 + episodic qualifier) | Common in infancy, especially 2–4 months | See mechanism below |
| Clubbing (digital) | HP:0100759 | Common with chronic cyanosis | Late finding |
| Systolic ejection murmur (RVOT) | HP:0031264 (Heart murmur) | Nearly universal | Harsh, left upper sternal border |
| Squatting behavior (older children) | — | Historic, less seen with early surgical repair | Increases SVR, reduces right-to-left shunt |
| Failure to thrive | HP:0001508 | Variable | Seen in significant cyanosis/heart failure |
| Boot-shaped heart ("coeur en sabot") on chest radiograph | HP:0004943 (if applicable) | Classic imaging finding | Due to RVH and diminished main PA segment |

### Associated coronary and vascular anomalies
- **Coronary artery anomalies**: ~5–6% of TOF patients, most commonly the **left anterior descending (LAD) arising from the right coronary artery (RCA)** and crossing the RVOT — surgically important because a transannular ventriculotomy can jeopardize this vessel ([PMC7599042](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7599042/); International Journal of Cardiology meta-analysis). Combined risk of anomalous coronary artery or large conal branch crossing the RVOT: ~10.3%.
- **Right-sided aortic arch**: ~25% of all TOF, much higher (up to 24–48%) in 22q11.2DS-associated cases.
- **MAPCAs (major aortopulmonary collateral arteries)**: prominent in TOF with pulmonary atresia, providing alternate pulmonary blood supply when central pulmonary arteries are hypoplastic/atretic.
- **Patent foramen ovale/ASD** ("pentalogy of Fallot" when present).

### Phenotype characteristics
- **Age of onset:** Congenital (present from birth); cardiac malformation completes during weeks 3–8 of gestation. Clinical cyanosis may be present at birth (severe RVOT obstruction) or emerge over the first weeks to months of life as infundibular obstruction (dynamic, muscular) progresses.
- **Severity:** Highly variable, forming a spectrum from "pink TOF" (mild RVOT obstruction, net left-to-right shunt) to TOF with pulmonary atresia (ductal- or MAPCA-dependent pulmonary blood flow, most severe).
- **Progression:** The infundibular (muscular) component of RVOT obstruction is dynamic and can worsen over the first months of life due to progressive infundibular hypertrophy, precipitating hypercyanotic spells.
- **Frequency of hypercyanotic spells:** Peak incidence around 2–4 months of age; can occur in unrepaired or palliated patients.

### Hypercyanotic ("Tet") spell mechanism
Spells result from an **acute imbalance between pulmonary and systemic vascular resistance**, causing decreased pulmonary blood flow and increased right-to-left shunting; infundibular spasm can contribute but "is not required for these spells to occur" ([PMID:1428277](https://pubmed.ncbi.nlm.nih.gov/1428277/); [Starship guidelines](https://www.starship.org.nz/guidelines/tetralogy-of-fallot/)). A self-perpetuating cycle involves hypoxemia, metabolic acidosis, hyperpnea, increased systemic venous return, and catecholamine-driven pulmonary vasoconstriction. Common triggers: crying/distress, defecation/straining, feeding, waking from sleep (low SVR), fever, dehydration, tachycardia/tachypnea from any cause, and some medications (e.g., ACE inhibitors). Treatment: knee-chest positioning, supplemental oxygen, volume expansion (non-pharmacologic first-line); beta-blockade to reduce infundibular spasm and alpha-1 agonists to raise SVR for refractory spells.

### Long-term/late phenotypes (post-repair)
- **Chronic pulmonary regurgitation** — the dominant late residual lesion after transannular-patch repair, driving progressive RV dilation/dysfunction.
- **Arrhythmias** — ~43% of patients develop supraventricular or ventricular arrhythmias during long-term follow-up; QRS prolongation is a marker of RV dilation and arrhythmic risk.
- **Sudden cardiac death** — incidence ~1.8% at 8-year follow-up in some cohorts; overall ~10% of late deaths in repaired-TOF populations are attributed to sudden death, probably arrhythmic.
- **Heart failure** — ~40% of late deaths in repaired-TOF (rTOF) populations attributed to heart failure.

### Neurodevelopmental/cognitive phenotypes
Adolescents/adults with repaired TOF show **neurocognitive deficits** in executive function, visuospatial skills, memory, attention, academic achievement, social cognition, and problem-solving, alongside increased prevalence of anxiety disorders, disruptive behavior, and ADHD, despite normal IQ ([PMC8870281](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8870281/)).

### Quality of life impact
Health-related quality of life in adults with repaired TOF is generally satisfactory but with **residual psychosocial and cognitive problems**. Better NYHA class, >3 hours/week physical activity, and preserved RV function are positively associated with QoL ([PMC6443137](https://pmc.ncbi.nlm.nih.gov/articles/PMC6443137/)). Exercise capacity is measurably reduced at a group level (mean ~74.8% predicted workload in a cohort of 314 adults), though most patients remain NYHA class I.

---

## 4. Genetic/Molecular Information

### Causal genes (summary table)
| Gene | HGNC | OMIM | Role | % of TOF (approx.) | Variant type |
|---|---|---|---|---|---|
| *NOTCH1* | HGNC:7881 | *190198 | Notch signaling receptor | ~4.5% (non-syndromic) | Predominantly missense; some LOF/in-frame indel |
| *FLT4* (VEGFR3) | HGNC:3767 | *136352 | VEGF-C receptor, lymphatic/vascular signaling | ~2.4% | Predominantly loss-of-function; splice-site variants also reported |
| *NKX2-5* | HGNC:2488 | *600584 | Cardiac homeobox transcription factor | ≥4% | Non-homeodomain missense in TOF (contrast with classic homeodomain mutations in ASD/AV block) |
| *JAG1* | HGNC:6188 | *601920 | Notch ligand (Alagille syndrome gene) | 1–2% | Various — haploinsufficiency |
| *GATA4* | HGNC:4173 | *600576 | Zinc-finger cardiac transcription factor | Minority | Haploinsufficiency |
| *TBX1* | HGNC:11592 | *602054 | T-box transcription factor, 22q11.2 critical gene | Contained within 22q11.2 deletion (~15% of TOF) | Deletion/haploinsufficiency (rarely point mutation) |
| *TBX5* | HGNC:11602 | *601620 | T-box transcription factor (Holt-Oram) | Minority | — |
| *ZFPM2 (FOG2)* | HGNC:19091 | *603693 | GATA cofactor | Minority | — |
| *PTPN11* | HGNC:9644 | *176876 | RAS/MAPK pathway phosphatase (Noonan syndrome) | Minority; also a common-variant GWAS hit | — |

**Variant classification / population frequency:** Pathogenicity is assessed per ACMG/AMP guidelines via ClinVar/ClinGen; allele frequency filtering against **gnomAD** is standard practice in TOF exome studies to prioritize ultra-rare/de novo damaging variants. De novo damaging variants in TOF probands are enriched in genes whose expression is spatially restricted to the myogenic progenitors of the outflow tract, based on integration with single-cell/spatial transcriptomic atlases of early human heart development ([PMID:34905512](https://pubmed.ncbi.nlm.nih.gov/34905512/)).

**Somatic vs. germline:** TOF-causing variants are essentially all **germline** (developmental disorder); no somatic mosaicism literature of note was identified in this search.

**Functional consequences:** Mixed — loss-of-function (*FLT4*, most *JAG1*, *GATA4* haploinsufficiency), missense/gain- or loss-of-function depending on domain (*NOTCH1*), and dosage-sensitivity (*TBX1* within 22q11.2 deletion; *NKX2-5*).

### Diagnostic yield of sequencing
- Whole-exome sequencing (WES) of clinical cohorts with **non-isolated** TOF (TOF+ extracardiac features) yields a definitive/probable molecular diagnosis in **23.6%** of patients (31/131 individuals) ([EJHG 2025, PMC/non-isolated TOF exome study](https://www.nature.com/articles/s41431-025-01916-8)).
- In non-syndromic cohorts, the combined *NOTCH1*+*FLT4* yield is ~7%, rising to ~15–16% across nine candidate genes.

### Epigenetic information
From DNA methylation and microRNA studies of TOF myocardium/right ventricular outflow tract tissue ([PMC12940485](https://pmc.ncbi.nlm.nih.gov/articles/PMC12940485/); also see DNA methylation study [PMC3819647](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3819647/)):
- **Hypermethylation** of *NKX2-5*, *HAND1*, and *GATA4* promoter regions is reported to "repress their expression, leading to impaired cardiomyocyte differentiation."
- **Hypomethylation** of *VEGFA* and *FLT4* suggests "compensatory activation of vascular remodeling pathways."
- **MicroRNA dysregulation:** downregulation of **miR-1** and **miR-133** disrupts *HAND2* and *GJA1* (connexin-43) expression; dysregulated **miR-424** and **miR-222** "modulate endothelial and smooth muscle cell differentiation within the outflow tract."
- **Histone modification:** *TBX1* haploinsufficiency has been linked to promotion of histone deacetylation at the *MEF2C* enhancer, reducing H3 acetylation and silencing *MEF2C* — a proposed mechanism connecting the 22q11.2 deletion to downstream cardiac transcriptional dysregulation.

### Chromosomal abnormalities
- **22q11.2 microdeletion** (typically 1.5–3 Mb, encompassing *TBX1*, *DGCR8*, *CRKL*, *MAPK1*, and dozens of other genes) — detected by FISH, chromosomal microarray, or MLPA; the most common structural genetic finding in TOF (~15%).
- **Trisomy 21, 18, 13.**
- Genome-wide microarray/chromosomal microarray analysis (CMA) is recommended as the **first-line clinical genetic test** for TOF across the lifespan, given it captures the 22q11.2 microdeletion and other pathogenic CNVs.

---

## 5. Environmental Information

### Environmental (teratogenic) factors
- **Maternal hyperglycemia/pregestational diabetes** — most robustly evidenced teratogenic exposure (OR ~3–5); mechanistically linked to altered embryonic retinoic acid catabolism under a diabetic milieu ([PMC10449132](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10449132/), model-organism/embryo evidence).
- **Retinoic acid derivatives (isotretinoin)** — interferes with cardiac neural crest cell migration essential for outflow tract septation.
- **Maternal phenylketonuria** with poor dietary control during pregnancy.
- **Warfarin exposure** in utero.
- **Fetal alcohol exposure.**

### Lifestyle factors
No CHD-specific lifestyle risk factor beyond the above (e.g., maternal smoking data for TOF specifically were not surfaced with strong effect sizes in this search; general CHD literature implicates maternal smoking and obesity for CHD broadly but TOF-specific quantification is a **gap**).

### Infectious agents
- **Congenital rubella infection** — classically associated with a spectrum of CHD, including TOF, as part of congenital rubella syndrome, though PDA and pulmonary artery stenosis are more classically rubella-associated; TOF association is reported but less specific than for other lesions.

---

## 6. Mechanism / Pathophysiology

### Embryologic/causal chain
1. **Trigger:** Genetic lesion (e.g., *NOTCH1*, *FLT4*, *NKX2-5*, *TBX1* haploinsufficiency in 22q11.2DS) or environmental teratogenic insult (maternal hyperglycemia, retinoic acid) disrupts **second heart field (SHF)** progenitor addition and/or **cardiac neural crest cell (CNCC)** migration into the developing outflow tract during weeks 3–8 of gestation.
2. **Cellular process:** TBX1 is required for efficient incorporation of SHF cardiac progenitors into the heart; "loss of TBX1 impairs extracellular matrix (ECM)-integrin-focal adhesion (FA) signaling," non-cell-autonomously impairing progenitor cell migration ([Circ Res, PMID for Tbx1/SHF mechanism]). Neural-crest-derived **NEDD4** controls **DKK1** protein levels, modulating **Wnt signaling** in the SHF to balance progenitor maintenance vs. myocardial differentiation (mouse model + human variant evidence, bioRxiv/PMC12913648). **GATA4** drives Hedgehog (Hh) signaling required for SHF migration and outflow tract development; decreased *Gata4* expression in mice produces double-outlet right ventricle and hypoplastic ventricular myocardium.
3. **Anatomic result — infundibular septal malalignment:** Anterocephalad (superior/leftward) deviation of the infundibular (outlet) septum relative to the muscular ventricular septum prevents normal ventricular septal closure, producing the four cardinal TOF features as a single unified defect ([StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK513288/); [ScienceDirect CHD review](https://www.sciencedirect.com/org/science/article/pii/S1747079X2500005X)):
   - The malaligned septum leaves a large **VSD**.
   - The aortic root, no longer aligned over the LV outflow, **overrides** the VSD.
   - **Hypoplasia of the subpulmonary infundibulum** narrows the RVOT, producing obstruction at infundibular, valvar, and/or supravalvar/branch-PA levels.
   - The RV, ejecting against elevated afterload (systemic-level pressure via the VSD and RVOT obstruction), undergoes secondary **hypertrophy**.
4. **Physiologic consequence:** The degree of RVOT obstruction determines shunt direction and clinical severity — mild obstruction yields "pink" TOF with left-to-right (or balanced) shunting; severe/complete obstruction (pulmonary atresia) makes pulmonary blood flow duct- or MAPCA-dependent with obligate right-to-left shunting and cyanosis.
5. **Postnatal remodeling:** Chronic cyanosis and RV pressure/volume overload drive compensatory polycythemia, RVH, and later — post-repair — chronic pulmonary regurgitation-driven RV dilation, fibrosis, and arrhythmogenic substrate formation. Postnatal RV cardiomyocytes under chronic hypoxic/metabolic stress show mitochondrial dysfunction, with **FOXO1** proposed as a metabolic-stress sensor mediating cardiomyocyte vulnerability (PMC12940485).

### Molecular pathways
- **Notch signaling** (*NOTCH1*, *JAG1*) — outflow tract septation and cardiac neural crest/endocardial cushion signaling.
- **VEGF/VEGFR signaling** (*FLT4/VEGFR3*, *VEGFA*) — vascular and outflow tract endothelial-to-mesenchymal transition.
- **RAS-MAPK pathway** (*PTPN11*) — overlapping with RASopathy (Noonan syndrome) cardiac phenotypes.
- **Wnt signaling** (via NEDD4-DKK1 axis) — SHF progenitor balance.
- **Hedgehog signaling** (via GATA4) — SHF migration.
- Suggested **GO terms**: GO:0003151 (outflow tract morphogenesis), GO:0003148 (outflow tract septum morphogenesis), GO:0003208 (cardiac ventricle morphogenesis), GO:0061308 (cardiac neural crest cell development involved in outflow tract morphogenesis), GO:0055010 (ventricular cardiac muscle tissue morphogenesis) — verify canonical labels via OAK before curation.

### Cellular processes/cell types involved
- **Second heart field (SHF) cardiac progenitor cells** — anterior/posterior SHF contributes to right ventricle and outflow tract myocardium.
- **Cardiac neural crest cells (CNCC)** — migrate into the outflow tract cushions to pattern the aorticopulmonary septum.
- **Endocardial cushion mesenchyme** (endothelial-to-mesenchymal transition).
- **Cardiomyocytes** of the RV and outflow tract myocardium (hypertrophy, later fibrosis).
- Suggested **CL terms**: CL:0002079 (cardiac neural crest cell), CL:0000746 (cardiac muscle cell), CL:0002350 (endocardial cell) — verify via OAK.

### Molecular profiling (recent single-cell/transcriptomic findings)
- Integration of **single-cell and spatial transcriptomics** of early human heart development (6.5–7.0 post-conceptional weeks) with TOF exome data shows that genes carrying damaging de novo mutations in TOF probands are significantly enriched in **myogenic progenitors of the cardiac outflow tract** and show "significant spatial expression in outflow tract or great vessels, consistent with the anatomic defect in TOF" ([PMID:34905512](https://pubmed.ncbi.nlm.nih.gov/34905512/), JCI Insight, human clinical + computational).
- A **single-cell RNA-seq study of fetal TOF hearts** identified 15 cell-type clusters with differential expression in atrial/ventricular cardiomyocytes enriched for damaging mutations ([PMID:39097963](https://pubmed.ncbi.nlm.nih.gov/39097963/)).
- A 2026 integrative bulk + single-nucleus transcriptomic study of non-syndromic TOF RVOT tissue found **proteostasis- and metabolism-related alterations** (Functional & Integrative Genomics, 2026).
- A maternal-fetal **microRNA axis** has been proposed as a mechanistic and potential biomarker link in TOF (Frontiers in Cardiovascular Medicine, 2026).

---

## 7. Anatomical Structures Affected

### Organ level
- **Primary organ:** Heart — specifically the right ventricular outflow tract/infundibulum, pulmonary valve/main and branch pulmonary arteries, interventricular septum, and aortic root.
- **Secondary/complication-related involvement:** Lungs (pulmonary blood flow abnormalities, MAPCAs), liver/spleen (chronic cyanosis, polycythemia sequelae historically), CNS (neurodevelopmental effects, and historically brain abscess/paradoxical embolism risk in unrepaired cyanotic patients), skeletal system in syndromic forms (e.g., VACTERL vertebral anomalies).
- **Body system:** Primarily cardiovascular; secondarily can be part of multisystem syndromes (craniofacial/thymic/parathyroid in 22q11.2DS; hepatic/vertebral/ocular in Alagille syndrome).

### Tissue and cell level
- Myocardium of the RV outflow tract/infundibulum (hypertrophied, later fibrotic post-repair).
- Endocardial cushion-derived valve tissue (pulmonary valve — dysplastic or absent in APVS).
- Vascular smooth muscle and endothelium of the pulmonary arteries (hypoplasia, or dilation in APVS).
- Suggested Cell Ontology terms as above (cardiac muscle cell, cardiac neural crest cell, endocardial cell).

### Subcellular level
- Mitochondrial dysfunction implicated in chronically hypoxic/stressed RV cardiomyocytes (GO Cellular Component: GO:0005739 mitochondrion).
- Sarcomeric/cytoskeletal remodeling in hypertrophied RV myocytes.

### Localization
- **Bilateral/central structure** (the heart itself is midline, but lesion components are RV/RVOT-lateralized — i.e., right-sided obstruction with left-to-right positioned aortic override).
- Suggested UBERON terms: UBERON:0002080 (right cardiac ventricle), UBERON:0002094 (outflow tract, verify exact ID), interventricular septum, pulmonary trunk/pulmonary valve, aortic root — verify canonical IDs via OAK before curation.

---

## 8. Temporal Development

### Onset
- **Congenital** — the anatomic malformation is established during weeks 3–8 of embryogenesis (cardiogenesis).
- Clinical onset of cyanosis: variable — present at birth in severe RVOT obstruction/pulmonary atresia (ductal-dependent), or emerging over the first days to months of life as the dynamic infundibular component of obstruction progresses. "Pink" TOF (minimal cyanosis) is possible with milder obstruction.
- Onset pattern: typically **acute-to-subacute** recognition in the neonatal period via cyanosis, murmur, or prenatal diagnosis; occasionally **insidious** presentation in older infants/children with milder forms ("pink Fallot").

### Progression
- **Natural history (unrepaired):** Without surgical intervention, historical data (pre-surgical era) showed high mortality — approximately 25% mortality by 1 year, 40% by age 3, 70% by age 10, and only ~5% survival to age 40 in unrepaired disease (classical natural-history literature; note this reflects an older evidence base predating modern surgical care).
- **Post-repair progression:** Early survival is now excellent (see Section 11), but a well-characterized **late progression pattern** exists: residual/progressive pulmonary regurgitation → RV dilation → RV dysfunction → arrhythmia risk → (in a minority) heart failure or sudden death, typically emerging in the second to fourth decades of life. "About 75% of infants who undergo repair during infancy will survive to reach their second to third decade of life without major consequences; however, after the first two decades of life, symptoms start to appear due to pulmonary valve regurgitation, and by the fourth decade of life, most survivors are symptomatic."
- **Disease course pattern:** Largely **stable-to-slowly-progressive** after successful repair, punctuated by discrete reintervention events (pulmonary valve replacement) rather than continuous decline; a minority experience arrhythmic events.

### Patterns
- **Remission:** Surgical repair is curative for the anatomic shunt physiology but not for the RVOT/pulmonary valve — this is a "residual lesion" disease model rather than a remitting-relapsing one.
- **Critical periods:** (1) Weeks 3–8 gestation — the teratogenic/genetic vulnerability window for the primary malformation; (2) Infancy (particularly 2–4 months) — peak vulnerability window for hypercyanotic spells due to dynamic infundibular hypertrophy; (3) Timing of surgical intervention (see Section 12) is itself a "critical period" concept, balancing risks of early repair against benefits of allowing pulmonary annulus growth via staged palliation.

---

## 9. Inheritance and Population

### Epidemiology
- **Prevalence/incidence:** TOF occurs in approximately **30–60 per 100,000 births** (~3 per 10,000 live births); it represents **5–7%** (some sources cite 5–10%) of all congenital heart defects, and is the **most common cyanotic CHD**. Congenital heart defects overall affect ~1% of newborns worldwide. One source cites incidence of ~0.326 per 1,000 live births.
- **Geographic variation:** Prevalence appears **considerably higher in Sub-Saharan Africa** relative to global estimates and reports from developed countries (systematic review/meta-analysis, PLOS ONE), likely reflecting a combination of true prevalence differences, case-ascertainment/survival differences, and healthcare-access factors relevant to CHD registries.

### Inheritance pattern
Orphanet classifies TOF inheritance as **"Autosomal dominant"** and **"Multigenic/multifactorial"** (i.e., most cases are multifactorial/sporadic, but a genetic subset — when a single dominant pathogenic variant is identified, e.g., *NOTCH1*, *NKX2-5* — follows autosomal dominant inheritance with variable/incomplete penetrance).

- **Penetrance:** Incomplete for most identified monogenic causes (e.g., *NKX2-5* variants in TOF are "not fully penetrant" [Circulation, hc4601.098427]; *FLT4* splice-site variants show "incomplete penetrance" [EJHG 2025 study]).
- **Expressivity:** Variable — the same genetic lesion (e.g., 22q11.2 deletion) can produce a spectrum of conotruncal defects (TOF, interrupted aortic arch, truncus arteriosus, isolated VSD) even within families.
- **Genetic anticipation:** Not a recognized feature of TOF (not a repeat-expansion disorder).
- **Germline mosaicism:** Not specifically well-characterized for TOF in this search — plausible for recurrence in families without an affected parent but not quantified in the literature surveyed (**gap**).
- **Founder effects:** Not prominently reported for TOF (contrast with some other Mendelian conditions); population-specific common variants (e.g., *NRP1* rs2228638 in Chinese cohorts) suggest population-differentiated susceptibility-allele frequencies rather than classical founder mutations.
- **Consanguinity:** Autosomal recessive inheritance is documented in the **Keeshond dog model** (see Section 14) but is not the predominant human inheritance pattern; consanguinity's role in human non-syndromic TOF is not strongly quantified in this search.
- **Sibling recurrence risk:** ~1–5% for sporadic non-syndromic TOF (see Section 2).

### Population demographics
- **Sex ratio:** Not sharply skewed in the general literature reviewed (in contrast to some other CHDs); specific TOF male:female ratio data were not strongly surfaced in this search (**gap** — commonly cited informally as roughly equal or slight male predominance; should be verified against a registry source before curation).
- **Age distribution:** Diagnosed at any age given prenatal detection, neonatal screening, and, in low-resource settings, later childhood/adult presentation of unrepaired or palliated disease ("longstanding unrepaired TOF" is a recognized adult clinical entity, [PMC9508357](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9508357/)).
- **Syndromic subpopulations:** 22q11.2DS (~15% of TOF), trisomy 21 (~7% of TOF), Alagille syndrome (1–2%).

---

## 10. Diagnostics

### Clinical tests
- **Physical examination:** Cyanosis (variable), harsh systolic ejection murmur at the left upper sternal border (RVOT obstruction), single S2 (absent/soft pulmonic component), clubbing in chronic cyanosis.
- **Pulse oximetry screening** (universal newborn CCHD screening): a cutoff of **<90%** SpO2 (or the standard <95% + differential limb algorithm used broadly) shows in one analysis **90% sensitivity, 99.94% specificity, 75% PPV, 99.98% NPV** for detecting critical CHD; optimal screening window is **8–24 hours** of life. TOF is one of the seven CDC-defined "critical congenital heart disease" (CCHD) lesions targeted by this screening (alongside hypoplastic left heart syndrome, pulmonary atresia with intact septum, TAPVR, transposition of the great arteries, tricuspid atresia, truncus arteriosus).
- **Chest radiograph:** classic "boot-shaped heart" (coeur en sabot) from RVH and diminished main PA segment; decreased pulmonary vascular markings.
- **Electrocardiography:** right axis deviation, RVH pattern.
- **Echocardiography (transthoracic):** primary, first-line diagnostic modality — delineates VSD, aortic override, RVOT obstruction level/severity, pulmonary annulus/branch PA size (z-scores), and screens for associated coronary anomalies.
- **Cardiac CT angiography / cardiac catheterization / angiography:** used pre-operatively, especially to define coronary artery anatomy (LAD-from-RCA), MAPCAs, and branch PA anatomy in complex/pulmonary-atresia variants.
- **Cardiac MRI:** central to **adult/post-repair surveillance** — quantifies RV volumes, pulmonary regurgitant fraction, and guides timing of pulmonary valve replacement.

### Prenatal/fetal diagnosis
- **Fetal echocardiography** is the standard prenatal screening/diagnostic method in high-income countries; more than 50% of critical CHD cases are now prenatally detected in such settings.

### Genetic testing
- **Chromosomal microarray (CMA)** is recommended as the **first-line clinical genetic test** for TOF across the lifespan (captures 22q11.2 microdeletion and other pathogenic CNVs).
- **FISH** for targeted 22q11.2 deletion confirmation.
- **Karyotyping** for suspected aneuploidy (trisomy 21/18/13).
- **Gene panels / whole-exome sequencing (WES)** recommended for isolated (non-syndromic) TOF or when CMA is non-diagnostic, particularly for **non-isolated TOF (TOF+ extracardiac anomalies)**, where WES yields a definitive/probable diagnosis in ~23.6% of cases.
- **Whole-genome sequencing (WGS)** increasingly used in research cohorts (e.g., ultra-rare variant burden analysis across 231 genome sequences).

### Clinical/diagnostic criteria
No formal DSM/ICD-style diagnostic-criteria checklist exists beyond echocardiographic/anatomic confirmation of the four cardinal features (or their pulmonary-atresia/APVS variant equivalents). Differential diagnosis includes other conotruncal defects (double-outlet right ventricle, truncus arteriosus, transposition of the great arteries with VSD and pulmonary stenosis, isolated pulmonary atresia with VSD) which share overlapping embryology and can present similarly on initial imaging.

### Screening
- **Newborn pulse oximetry screening** — universal in most high-income health systems, part of standard CCHD screening panels.
- **Prenatal ultrasound anomaly scanning** — routine anatomy scan (typically ~18–22 weeks) with cardiac views; fetal echocardiography for higher-risk pregnancies or suspicious anatomy-scan findings.
- **Cascade/family genetic screening** when a pathogenic monogenic variant or 22q11.2 deletion is identified in a proband, given autosomal dominant inheritance patterns for identified single-gene causes.

---

## 11. Outcome/Prognosis

### Survival
- **Modern surgical era, long-term survival after complete repair:**
  - **97.7% at 10 years and 94.5% at 30 years** in one large series; another source reports **~95% at 10 years and 90% at 15 years**.
  - A landmark long-term follow-up (**36-year, 490 survivors of the first postoperative year**) found **32-year actuarial survival of 86%**, versus an expected 96% in an age/sex-matched general population ([PMID:9350942](https://pubmed.ncbi.nlm.nih.gov/9350942/)).
  - **Very long-term (50-year) follow-up:** survival at 50 years post-repair is **71%** overall (**84%** among in-hospital survivors), but **event-free survival is only 9%** — reintervention occurs in ~40%, supraventricular arrhythmia in ~18%, and ventricular tachycardia in ~7% ([PMID:39870118](https://pubmed.ncbi.nlm.nih.gov/39870118/)).
  - **Independent predictors of long-term survival:** older age at operation, and a higher postoperative RV:LV systolic pressure ratio (worse outcome) ([NEJM 1993, PMID via NEJM199308263290901](https://www.nejm.org/doi/full/10.1056/NEJM199308263290901)). Genetic abnormalities (e.g., 22q11.2DS) are associated with increased mortality risk in both early and late postsurgical phases.
- **Unrepaired natural history** (historical, pre-surgical-era data): substantial early mortality, with only a small minority surviving to adulthood without intervention.

### Morbidity and function
- **~43%** of repaired-TOF patients develop supraventricular or ventricular arrhythmias on long-term follow-up.
- **Sudden cardiac death**: incidence ~1.8% at 8-year follow-up in one cohort; ~10% of late deaths in rTOF populations attributed to sudden (likely arrhythmic) death; ~40% of late deaths attributed to heart failure.
- **Exercise capacity** is reduced at a group level (mean ~74.8% of predicted workload in one 314-patient adult cohort), though most patients remain functionally NYHA class I.
- **Neurodevelopmental morbidity:** deficits in executive function, visuospatial skills, memory, attention, academic achievement, and social cognition; increased anxiety, disruptive behavior disorders, and ADHD prevalence, persisting into adulthood and affecting employment/social adjustment ([PMC8870281](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8870281/); [PMC11082288](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11082288/)).
- **Quality of life:** generally satisfactory in repaired-TOF adults, with better QoL linked to NYHA class I status, greater physical activity, and preserved RV function; weight extremes (underweight or obesity) negatively affect QoL in children with TOF variants ([PMC11787155](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11787155/)).

### Complications
- Chronic pulmonary regurgitation → RV dilation/dysfunction (the dominant late complication driving reintervention).
- Residual/recurrent RVOT obstruction (valvar, subvalvar, or branch PA).
- Residual VSD.
- Aortic root dilation (late, in some cohorts).
- Endocarditis risk (as with any residual structural heart disease/prosthetic material).
- Reintervention burden: transannular-patch repair cohorts show increased procedural burden at 25 years compared to valve-sparing repair strategies.

### Prognostic factors and biomarkers
- Age at operation, postoperative RV:LV pressure ratio, presence of a genetic syndrome (particularly 22q11.2DS), QRS duration/prolongation (arrhythmia risk marker), degree of pulmonary regurgitation and RV dilation on cardiac MRI (guides timing of pulmonary valve replacement), and type of repair (transannular patch vs. valve-sparing) are the principal prognostic determinants identified in this literature.

---

## 12. Treatment

### Surgical/interventional (definitive management)
- **Complete surgical repair** — the mainstay of treatment: closure of the VSD with a patch, and relief of RVOT obstruction (resection of infundibular muscle, ± transannular patch across the pulmonary annulus, ± valve-sparing/pulmonary-valve-preserving techniques when annulus size permits). Suggested NCIT term: NCIT:C15329 (Surgical Procedure) — verify specific TOF-repair NCIT/procedure code if a more precise term exists.
- **Staged palliation** (for symptomatic/ductal-dependent or high-risk neonates/young infants):
  - **Modified Blalock-Taussig-Thomas (BTT) shunt** — surgical systemic-to-pulmonary shunt, historically the standard initial palliative procedure, allows pulmonary annulus/branch PA growth before complete repair, reducing need for transannular incision.
  - **RVOT stenting** and **arterial ductal stenting** — transcatheter alternatives to surgical shunting for initial palliation; comparative studies show RVOT-stented infants were palliated at a younger age (mean 1.62 ± 0.34 months) versus modified BT shunt (2.80 ± 0.52 months).
  - Indications for palliation over primary repair: low birth weight, small pulmonary arteries, complex/high-risk anatomy.
- **Balloon pulmonary valvuloplasty** — used in select cases as a bridging/palliative catheter intervention.
- **Pulmonary valve replacement (PVR)** — the principal late reintervention for symptomatic or hemodynamically significant chronic pulmonary regurgitation after repair; may be surgical or transcatheter (percutaneous pulmonary valve implantation). PVR improves symptoms and can reduce ventricular tachycardia incidence (one study: 22% → 9% at mean 4.7-year follow-up post-PVR) but **does not reliably reverse other deleterious effects**, and current guidelines do **not** consider ventricular arrhythmia risk alone a sufficient indication for PVR given lack of robust evidence that PVR reduces subsequent ventricular arrhythmia risk.

### Pharmacotherapy
- **Beta-blockers** (e.g., propranolol) — reduce infundibular spasm/hypercyanotic spell frequency, used both acutely for spells and as chronic prophylaxis in some unrepaired/palliated infants.
- **Alpha-1 agonists** (e.g., phenylephrine) — increase systemic vascular resistance to acutely terminate hypercyanotic spells.
- **Prostaglandin E1 (alprostadil)** — maintains ductal patency in ductal-dependent pulmonary blood flow (severe RVOT obstruction/pulmonary atresia) pending intervention.
- **Diuretics/afterload-reducing agents** — supportive management of heart failure symptoms in decompensated repaired-TOF patients.
- **Antiarrhythmic medications** — for management of supraventricular/ventricular arrhythmias in the long-term follow-up population.
- **Disopyramide** — reported in case literature (e.g., a 72-year-old awaiting primary TOF repair) for tet-spell management as an alternative agent.

### Supportive/rehabilitative
- Non-pharmacologic hypercyanotic spell management: knee-chest positioning, supplemental oxygen, IV volume expansion.
- Genetic counseling — particularly relevant given autosomal dominant inheritance patterns of identified monogenic causes and the ~15% 22q11.2DS association (NCIT:C15240, Genetic Counseling).
- Multidisciplinary neurodevelopmental follow-up/early intervention for at-risk repaired-TOF children (given the well-documented cognitive/behavioral morbidity profile).
- Cardiac rehabilitation/structured exercise programs to address measurable exercise-capacity deficits in adults.

### Device/electrophysiologic therapies
- Implantable cardioverter-defibrillator (ICD) placement — for selected high-risk patients based on arrhythmia risk stratification (QRS duration, RV dilation/dysfunction, inducible VT, prior sustained VT/aborted SCD).
- Catheter ablation of atrial or ventricular arrhythmia substrate in symptomatic late-postoperative patients.

### Experimental/emerging
- Ongoing clinical trials comparing **early versus later re-valving (PVR)** strategy in TOF with free pulmonary regurgitation (e.g., trial protocol referenced at [NCT04084132](https://cdn.clinicaltrials.gov/large-docs/32/NCT04084132/Prot_SAP_000.pdf)).
- Research-stage work on microRNA-based biomarkers (maternal-fetal microRNA axis) for risk stratification, and integrative multi-omics (bulk + single-nucleus transcriptomics of RVOT tissue) toward mechanistic/biomarker discovery — not yet clinical-grade diagnostics or therapeutics.

### Treatment algorithm summary
Neonatal/infant presentation → assess ductal dependency and anatomic risk factors → **primary complete repair** (if anatomy/size favorable) **or staged palliation** (BT shunt / RVOT or ductal stent) **followed by complete repair** later in infancy → long-term surveillance (echocardiography, cardiac MRI) for pulmonary regurgitation/RV dilation → **pulmonary valve replacement** when criteria met → arrhythmia risk stratification and, where indicated, ICD/ablation → lifelong adult congenital heart disease (ACHD) specialty follow-up.

---

## 13. Prevention

### Primary prevention
- **Periconceptional folic acid/multivitamin supplementation**, ideally initiated **before conception**, is the best-evidenced modifiable primary-prevention strategy, with reported risk reductions specifically for TOF (OR ~0.53 in a Hungarian cohort) and for CHD broadly (~20–59% reduction depending on cohort/definition) (see Section 2).
- **Optimization of maternal glycemic control** prior to and during early pregnancy in women with pregestational diabetes — directly targets the most robustly quantified modifiable teratogenic risk factor (OR ~3–5 reduction target).
- **Avoidance of retinoic acid/isotretinoin exposure** during the periconceptional period and pregnancy.
- **Rubella immunization** prior to pregnancy (standard public health measure, reduces congenital rubella syndrome-associated CHD broadly).
- **Genetic counseling and family planning guidance** for known carriers of monogenic TOF-associated variants or 22q11.2 deletion, given autosomal dominant transmission with variable penetrance.

### Secondary prevention (early detection)
- **Newborn pulse oximetry screening** — a low-cost, high-specificity universal screening tool for critical CHD including TOF, recommended for all newborns at 8–24 hours of life.
- **Fetal anomaly ultrasound screening** with referral to fetal echocardiography when cardiac views are abnormal or risk factors are present (family history, pregestational diabetes, teratogen exposure).
- **Prenatal genetic screening** (e.g., non-invasive prenatal testing, or targeted testing when a fetal cardiac anomaly suggestive of a conotruncal defect is found) to identify 22q11.2 deletion or trisomy, informing prenatal counseling and delivery planning.

### Tertiary prevention (preventing complications in affected individuals)
- Structured lifelong ACHD (adult congenital heart disease) follow-up protocols, including serial cardiac MRI for pulmonary regurgitant fraction/RV volumetric surveillance, to enable timely pulmonary valve replacement before irreversible RV dysfunction develops.
- Arrhythmia risk-stratification programs (QRS duration monitoring, Holter surveillance) to guide prophylactic ICD placement in appropriately selected patients.
- Infective endocarditis prophylaxis per standard congenital heart disease guidelines for at-risk repaired patients (prosthetic material, residual shunts).
- Structured neurodevelopmental screening and early intervention referral for repaired-TOF children, given the well-documented cognitive/behavioral risk profile.

### Public health / population-level
- Population folic acid fortification programs (mandatory grain fortification in many countries) are credited with reduction in neural tube defects and have shown associated reductions in some CHD categories, including conotruncal defects broadly.
- CCHD newborn screening mandates (adopted in most U.S. states and many other countries) function as a population-level secondary-prevention/early-detection public health intervention specifically because TOF is one of the seven core CDC-targeted lesions.

---

## 14. Other Species / Natural Disease

### Taxonomy and naturally occurring disease
- **Dogs (*Canis lupus familiaris*, NCBITaxon:9615)** — TOF is a recognized, naturally occurring congenital heart defect. **OMIA:000994-9615** documents Tetralogy of Fallot in dogs ([OMIA](https://omia.org/OMIA000994/9615/)).
  - **Breed predisposition:** **Keeshond**, English Bulldog, Wire-haired Fox Terrier, and West Highland White Terrier are reportedly overrepresented.
  - **Keeshond colony model:** Extensive pathologic and genetic studies have been conducted in a dedicated Keeshond research colony with hereditary conotruncal defects. The mode of inheritance in this colony is believed to be **autosomal recessive with variable expression**, and the defect is described as **oligogenic** — "The keeshond defect in cardiac conotruncal development is oligogenic" ([PMID:15711798](https://pubmed.ncbi.nlm.nih.gov/15711798/)). This colony represents one of the best-characterized **naturally occurring, heritable large-animal models** of human conotruncal CHD and has informed understanding of oligogenic inheritance mechanisms relevant to human non-syndromic TOF.
- **Cats** — TOF also occurs, though less commonly documented/characterized than in dogs. A retrospective veterinary case series covering dogs and cats with TOF (31 cases, 2003–2014) characterized epidemiological, clinical, echocardiographic features and survival times ([AVMA journal](https://avmajournals.avma.org/view/journals/javma/249/8/javma.249.8.909.xml)). In one large series of 967 consecutive veterinary CHD cases, TOF prevalence was reported at ~1%.

### Veterinary relevance
TOF in dogs and cats presents similarly to the human disease (cyanosis, exercise intolerance, murmur) and carries a guarded prognosis without surgical correction; veterinary management is largely supportive (given more limited surgical infrastructure for complex pediatric-style cardiac surgery in companion animals) compared to the near-universal surgical correction paradigm in human medicine.

### Comparative biology
The heritable, oligogenic Keeshond model provides a comparative genetics resource for understanding gene-gene interaction effects on conotruncal septation — directly complementing the human genetic architecture picture (where combinations of NOTCH1/FLT4/NKX2-5/TBX1 and modifier loci, rather than single fully penetrant mutations, appear to determine phenotype in most non-syndromic cases).

### Transmission
Not applicable — TOF is a non-infectious congenital developmental malformation, not a transmissible disease, in either humans or other species.

---

## 15. Model Organisms

### Mouse models (genetic, most extensively used)
- ***Tbx1* mutant/knockout mice** — recapitulate cardiovascular and glandular defects seen in human DiGeorge/22q11.2 deletion syndrome, including outflow tract lesions such as persistent truncus arteriosus and TOF-like phenotypes; establishes *Tbx1* haploinsufficiency as sufficient to cause conotruncal malformation, directly modeling the human 22q11.2DS-TOF association ([Circ Res, Tbx1/SHF study](https://www.ahajournals.org/doi/10.1161/circresaha.115.305020)).
- ***Hey2* mutant mice** — develop "tetralogy of Fallot and other congenital heart defects" ([PMID:12372254](https://pubmed.ncbi.nlm.nih.gov/12372254/)), implicating the Notch-effector *Hey2* gene in outflow-tract septation, mechanistically connected to the Notch pathway genes (*NOTCH1*, *JAG1*) causally implicated in human TOF.
- ***Jag1*-deficient mice** — show outflow tract abnormalities associated with abnormal ventricular activation and desynchronized contraction (2025 bioRxiv preprint), directly modeling the Notch-ligand mechanism underlying JAG1/Alagille-associated TOF.
- ***Nedd4* conditional knockout (Wnt1-Cre;Nedd4^fl/fl)*** — neural-crest-specific deletion produces outflow tract defects from failed SHF cell addition, and a human *NEDD4* variant found in a TOF patient shows impaired function in this model system, linking mouse mechanistic data directly to a human genetic finding.
- ***Gata4*-hypomorphic/reduced-expression mice** — produce double-outlet right ventricle and hypoplastic ventricular myocardium, modeling the *GATA4* haploinsufficiency mechanism implicated in a subset of human TOF/conotruncal defects.
- General mouse conotruncal/SHF/neural-crest lineage-tracing models (Wnt1-Cre, Mef2c-AHF-Cre) are widely used tools for dissecting the SHF and CNCC contributions to outflow tract septation relevant to TOF pathogenesis (Springer chapter, "Molecular Pathways and Animal Models of Tetralogy of Fallot and Double Outlet Right Ventricle").

### Phenotype recapitulation and limitations
- Mouse models robustly recapitulate the **anatomic** outflow-tract/conotruncal septation defects (VSD, overriding great vessel, RVOT obstruction analogs) and the **genetic dosage-sensitivity** principle (haploinsufficiency phenotypes for *Tbx1*, *Gata4*, *Nedd4*, *Jag1*).
- Limitations: full recapitulation of the exact four-component human TOF phenotype (including the specific degree/pattern of RVOT obstruction and later postnatal RV remodeling/arrhythmia biology) is variable across models; many single-gene mouse knockouts instead produce a broader spectrum of conotruncal defects (persistent truncus arteriosus, double-outlet right ventricle) rather than a TOF-specific phenotype, consistent with the human observation that TOF arises from combinatorial/oligogenic rather than single-gene mechanisms in most non-syndromic cases. This represents a **human-model mismatch consideration**: single-gene mouse models best capture mechanism/pathway biology rather than the precise clinical anatomic subtype, and postnatal chronic pulmonary-regurgitation/arrhythmia biology (a major driver of human long-term morbidity) is not well modeled by embryonic-lethal or perinatal-lethal knockout lines.

### Research applications
- Dissecting SHF progenitor addition and CNCC migration mechanisms (developmental biology).
- Testing gene-dosage/haploinsufficiency thresholds relevant to human 22q11.2 deletion-sized regions.
- Functional validation of candidate human variants (e.g., NEDD4) identified by exome sequencing, bridging human genetics and mechanistic causality.
- Postnatal RV remodeling/hypoxia and metabolic-stress models (relevant to *FOXO1*-related postnatal cardiomyocyte vulnerability hypotheses) are an emerging application area.

### Resources
Mouse Genome Informatics (MGI) and standard conditional/lineage-tracing Cre driver lines (Wnt1-Cre for neural crest, Mef2c-AHF-Cre for anterior SHF) are the primary community resources underlying this body of work; the large-animal **Keeshond dog colony** (Section 14) is a complementary heritable natural-disease model resource for oligogenic conotruncal defect genetics.

---

## Summary of Suggested Ontology Terms for KB Curation

*(All suggestions should be verified against canonical labels via OAK/appropriate adapters before curation, per standard practice — several IDs above are given with moderate rather than high confidence.)*

- **MONDO:** MONDO:0008542 (Tetralogy of Fallot)
- **OMIM:** #187500
- **Orphanet:** ORPHA:3303
- **HPO (phenotypes):** HP:0001629 (VSD), HP:0002623 (overriding aorta), HP:0001642 (pulmonic stenosis), HP:0004415 (infundibular pulmonic stenosis), HP:0001714 (RVH), HP:0000961 (cyanosis), HP:0100759 (clubbing), HP:0031264 (heart murmur), HP:0001508 (failure to thrive)
- **GO (biological process):** GO:0003151 (outflow tract morphogenesis), GO:0003148 (outflow tract septum morphogenesis), GO:0003208 (cardiac ventricle morphogenesis)
- **CL (cell types):** CL:0002079 (cardiac neural crest cell), CL:0000746 (cardiac muscle cell)
- **CHEBI:** CHEBI:26536 (retinoic acid), CHEBI:27470 (folic acid)
- **NCIT (treatments):** NCIT:C15329 (Surgical Procedure), NCIT:C15240 (Genetic Counseling)
- **Causal/susceptibility genes (HGNC):** *NOTCH1* (HGNC:7881), *FLT4* (HGNC:3767), *NKX2-5* (HGNC:2488), *JAG1* (HGNC:6188), *GATA4* (HGNC:4173), *TBX1* (HGNC:11592), *TBX5* (HGNC:11602), *ZFPM2* (HGNC:19091), *PTPN11* (HGNC:9644)

---

## Key Evidence Gaps Identified
1. Precise TOF-specific male:female sex ratio not robustly quantified in this search.
2. Germline mosaicism rates for TOF recurrence not well characterized.
3. Genetic protective variants/alleles specific to TOF are essentially undocumented (in contrast to well-established protective environmental factor — folic acid).
4. Maternal smoking/obesity effect sizes specific to TOF (as opposed to CHD broadly) were not strongly surfaced.
5. Mouse models capture pathway mechanism well but rarely recapitulate the precise TOF anatomic subtype or postnatal chronic pulmonary-regurgitation/arrhythmia biology — a human-model-mismatch consideration for any curated model-organism evidence.

---

## Sources

- [Comprehensive genotype-phenotype analysis in 230 patients with tetralogy of Fallot - PubMed (PMID:19948535)](https://pubmed.ncbi.nlm.nih.gov/19948535/)
- [JAG1 mutation in a patient with deletion 22q11.2 syndrome and tetralogy of Fallot - PubMed (PMID:23956173)](https://pubmed.ncbi.nlm.nih.gov/23956173/)
- [OMIM #187500 - Tetralogy of Fallot](https://omim.org/entry/187500)
- [OMIM *600584 - NKX2-5](https://omim.org/entry/600584)
- [NKX2.5 Mutations in Patients With Tetralogy of Fallot - Circulation](https://www.ahajournals.org/doi/10.1161/hc4601.098427)
- [Genetic insights into the Tetralogy of Fallot - GSC Online Press](https://gsconlinepress.com/journals/gscarr/sites/default/files/GSCARR-2023-0233.pdf)
- [Tetralogy of Fallot: Anatomy, Physiology, and Outcomes - ScienceDirect](https://www.sciencedirect.com/org/science/article/pii/S1747079X2500005X)
- [Tetralogy of Fallot - StatPearls - NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/NBK513288/)
- [Tetralogy of Fallot With Pulmonary Stenosis - Medscape](https://emedicine.medscape.com/article/2063480-overview)
- [Tetralogy of Fallot: Genetic, Epigenetic and Clinical Insights into a Multifactorial Congenital Heart Disease - PMC12940485](https://pmc.ncbi.nlm.nih.gov/articles/PMC12940485/)
- [Genetic insights into non-syndromic Tetralogy of Fallot - Frontiers/PMC9582763](https://pmc.ncbi.nlm.nih.gov/articles/PMC9582763/)
- [Pooled prevalence and subgroup variations of TOF in Sub-Saharan Africa - PLOS One](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0311686)
- [Long-Term Outcome in Patients Undergoing Surgical Repair of Tetralogy of Fallot - NEJM 1993](https://www.nejm.org/doi/full/10.1056/NEJM199308263290901)
- [Long-term survival in patients with repair of tetralogy of Fallot: 36-year follow-up - PubMed (PMID:9350942)](https://pubmed.ncbi.nlm.nih.gov/9350942/)
- [Long term outcome after surgical tetralogy of Fallot repair at young age: up to 50 years - PubMed (PMID:39870118)](https://pubmed.ncbi.nlm.nih.gov/39870118/)
- [Hyperglycemia alters retinoic acid catabolism in embryos exposed to a maternal diabetic milieu - PMC10449132](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10449132/)
- [Tetralogy of Fallot — Grokipedia](https://grokipedia.com/page/Tetralogy_of_Fallot)
- [Neural crest cell-derived DKK1 and NEDD4 modulate Wnt signalling in the second heart field - PMC12913648](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12913648/)
- [Tbx1 Coordinates Addition of Posterior Second Heart Field Progenitor Cells - Circulation Research](https://www.ahajournals.org/doi/10.1161/circresaha.115.305020)
- [Arrhythmia risk stratification late after Tetralogy of Fallot repair with pulmonary regurgitation - PMC11657245](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11657245/)
- [Impact of Pulmonary Valve Replacement on Arrhythmia Propensity Late After Repair of Tetralogy of Fallot - Circulation](https://www.ahajournals.org/doi/10.1161/01.CIR.103.20.2489)
- [Developmental outflow tract abnormalities of Jag1-deficient mice - bioRxiv 2025](https://www.biorxiv.org/content/10.1101/2025.08.08.669322.full.pdf)
- [Tetralogy of fallot and other congenital heart defects in Hey2 mutant mice - PubMed (PMID:12372254)](https://pubmed.ncbi.nlm.nih.gov/12372254/)
- [2-Year Outcomes After Complete or Staged Procedure for Tetralogy of Fallot in Neonates - JACC](https://www.jacc.org/doi/10.1016/j.jacc.2019.05.057)
- [Young infants with symptomatic tetralogy of Fallot: Shunt or primary repair? - PMC11247207](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11247207/)
- [Comparative Study RVOT stenting vs modified BT shunt - PMC11951935](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11951935/)
- [Pulse Oximetry Screening for Critical Congenital Heart Defects - PMC12674206](https://pmc.ncbi.nlm.nih.gov/articles/PMC12674206/)
- [Diagnostic Accuracy of Physical Examination and Pulse Oximetry for CCHD Screening - PMC10814555](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10814555/)
- [22q11.2 Deletion Status and Disease Burden in Children and Adolescents With Tetralogy of Fallot - Circ Cardiovasc Genet](https://www.ahajournals.org/doi/10.1161/circgenetics.114.000819)
- [Cardiovascular Malformations in CHARGE Syndrome with DiGeorge Phenotype - PMC5121448](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5121448/)
- [Tetralogy of Fallot – Management of hypercyanotic spell - Starship](https://www.starship.org.nz/guidelines/tetralogy-of-fallot/)
- [Mechanism of cyanotic spells in tetralogy of Fallot - PubMed (PMID:1428277)](https://pubmed.ncbi.nlm.nih.gov/1428277/)
- [Treating Tet Spells With Disopyramide in a 72-Year-Old - PMC10774763](https://pmc.ncbi.nlm.nih.gov/articles/PMC10774763/)
- [Whole Exome Sequencing Reveals the Major Genetic Contributors to Nonsyndromic Tetralogy of Fallot - Circ Res (PMID:30582441)](https://pubmed.ncbi.nlm.nih.gov/30582441/)
- [RNA-sequencing unveils FLT4 splice site variants in variable congenital heart disease - EJHG 2025](https://www.nature.com/articles/s41431-025-01788-y)
- [Non-isolated tetralogy of fallot (TOF+): exome sequencing efficacy - EJHG 2025](https://www.nature.com/articles/s41431-025-01916-8)
- [Another Notch in the Genetic Puzzle of tetralogy of Fallot - PMC6383779](https://pmc.ncbi.nlm.nih.gov/articles/PMC6383779/)
- [Tetralogy of Fallot With Absent Pulmonary Valve - Medscape](https://emedicine.medscape.com/article/899249-overview)
- [Absent pulmonary valve syndrome - ISUOG](https://www.isuog.org/education/visuog/obstetrics/heart/abnormal-outflow-tracts/fallot-and-variants/absent-pulmonary-valve-syndrome.html)
- [Folate Deficiency and Folic Acid Supplementation: Prevention of NTDs and CHDs - PMC3847759](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3847759/)
- [Protective effect of periconceptional folic acid supplements on CHD risk - PubMed (PMID:19952004)](https://pubmed.ncbi.nlm.nih.gov/19952004/)
- [Exercise capacity, quality of life, and resilience after repair of tetralogy of Fallot - Cardiology in the Young](https://www.cambridge.org/core/journals/cardiology-in-the-young/article/abs/exercise-capacity-quality-of-life-and-resilience-after-repair-of-tetralogy-of-fallot-a-crosssectional-study-of-patients-operated-between-1964-and-2009/2DC7E018441C55F39B868DB9313AE367)
- [Neurodevelopmental Outcomes in Tetralogy of Fallot: A Systematic Review - PMC8870281](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8870281/)
- [Factors associated with health-related quality of life among adults with tetralogy of Fallot - PMC6443137](https://pmc.ncbi.nlm.nih.gov/articles/PMC6443137/)
- [Neurodevelopment in patients with repaired tetralogy of Fallot - PMC11082288](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11082288/)
- [Impact of Underweight, Overweight, and Obesity on HRQoL in Children with TOF - PMC11787155](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11787155/)
- [OMIA:000994-9615: Tetralogy of Fallot in Canis lupus familiaris (dog)](https://omia.org/OMIA000994/9615/)
- [Uncommon Congenital Defects of the Cardiovascular System in Animals - Merck Veterinary Manual](https://www.merckvetmanual.com/circulatory-system/congenital-and-inherited-anomalies-of-the-cardiovascular-system/tetralogy-of-fallot-in-animals)
- [Epidemiological, clinical, and echocardiographic features of dogs and cats with TOF - JAVMA](https://avmajournals.avma.org/view/journals/javma/249/8/javma.249.8.909.xml)
- [The keeshond defect in cardiac conotruncal development is oligogenic - PubMed (PMID:15711798)](https://pubmed.ncbi.nlm.nih.gov/15711798/)
- [Orphanet: Tetralogy of Fallot](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Lng=GB&Expert=3303)
- [2026 ICD-10-CM Diagnosis Code Q21.3: Tetralogy of Fallot](https://www.icd10data.com/ICD10CM/Codes/Q00-QA0/Q20-Q28/Q21-/Q21.3)
- [Detection of Coronary Artery and Aortic Arch Anomalies in TOF Using CT Angiography - PMC9570993](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9570993/)
- [Coronary anomalies in tetralogy of Fallot – A meta-analysis - International Journal of Cardiology](https://www.internationaljournalofcardiology.com/article/S0167-5273(19)35852-8/pdf)
- [Coronary Artery Anomalies in Tetralogy of Fallot Patients Undergoing CT Angiography - PMC7599042](https://pmc.ncbi.nlm.nih.gov/articles/PMC7599042/)
- [Angiographic Anatomy of MAPCAs and Association With Early Surgical Outcomes in TOF - JAHA](https://www.ahajournals.org/doi/10.1161/JAHA.120.017981)
- [Sequencing of a Chinese tetralogy of Fallot cohort reveals clustering mutations in myogenic heart progenitors - JCI Insight (PMID:34905512)](https://insight.jci.org/articles/view/152198)
- [Single-Cell RNA-Seq Analysis of Hearts in Patients with Fetal Tetralogy of Fallot - Karger (PMID:39097963)](https://karger.com/crd/article/150/2/221/911068/Single-Cell-RNA-Seq-Analysis-of-Hearts-in-Patients)
- [Integrative analysis of bulk and single-nucleus transcriptomes in RVOT of non-syndromic TOF - Functional & Integrative Genomics 2026](https://link.springer.com/article/10.1007/s10142-026-01898-w)
- [Maternal–fetal microRNA axis in congenital heart disease: implications for tetralogy of Fallot - Frontiers 2026](https://www.frontiersin.org/journals/cardiovascular-medicine/articles/10.3389/fcvm.2026.1821322/full)
- [Genome-wide association study identifies loci on 12q24 and 13q32 associated with Tetralogy of Fallot](https://www.academia.edu/89468920/Genome_wide_association_study_identifies_loci_on_12q24_and_13q32_associated_with_Tetralogy_of_Fallot)
- [Genetic Variants at 10p11 Confer Risk of Tetralogy of Fallot in Chinese of Nanjing - PMC3940663 (PMID:24594544)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3940663/)
- [Genome-Wide Association Study to Find Modifiers for TOF in 22q11.2DS Identifies Variants in GPR98 - Circ Cardiovasc Genet (PMID:29025761)](https://www.ahajournals.org/doi/full/10.1161/CIRCGENETICS.116.001690)
- [DNA methylation status of NKX2-5, GATA4 and HAND1 in patients with tetralogy of fallot - PMC3819647](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3819647/)
- [Longstanding unrepaired tetralogy of Fallot - PMC9508357](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9508357/)