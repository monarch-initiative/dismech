---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-10T14:06:57.679959'
end_time: '2026-08-10T14:11:14.156917'
duration_seconds: 256.48
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Ventricular Septal Defect
  mondo_id: ''
  category: Congenital
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
  web_search_requests: 12
  num_turns: 14
  total_cost_usd: 1.5746174000000002
  session_id: ccd9973f-d61b-50a6-8cfe-0a77b122d0f2
  stop_reason: end_turn
citation_count: 32
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Ventricular Septal Defect
- **MONDO ID:**  (if available)
- **Category:** Congenital

## Research Objectives

Please provide a comprehensive research report on **Ventricular Septal Defect** covering all of the
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

# Ventricular Septal Defect (VSD): Comprehensive Research Report

## 1. Disease Information

**Overview:** Ventricular septal defect (VSD) is a congenital cardiac malformation characterized by an abnormal opening in the interventricular septum, the muscular/membranous wall separating the left and right ventricles. It is the **most common congenital heart defect (CHD)** in live-born infants (excluding bicuspid aortic valve), accounting for roughly 20–30% of all congenital heart lesions. VSDs range from small, hemodynamically insignificant defects that close spontaneously to large defects causing heart failure and, if untreated, pulmonary vascular disease (Eisenmenger syndrome).

**Key identifiers:**
- **MONDO:** MONDO:0002070
- **OMIM:** 614429 (ventricular septal defect 1, VSD1; note OMIM also separately catalogs syndromic forms, e.g., under specific gene entries such as GATA4 600576, NKX2-5 600584, TBX5 601620)
- **Orphanet:** ORPHA:1480 (isolated ventricular septal defect)
- **ICD-10-CM:** Q21.0 (congenital VSD); I23.2 (acquired/post-MI VSD, a distinct acquired mechanical complication)
- **ICD-11 (MMS):** LA88.4
- **MeSH:** D006345 (Heart Septal Defects, Ventricular)
- **HPO:** HP:0001629 (Ventricular septal defect)

**Synonyms:** interventricular septal defect; VSD; "hole in the heart" (lay term); perimembranous/membranous VSD, muscular VSD, inlet (AV canal-type) VSD, outlet (conal/infundibular/doubly committed subarterial) VSD (classification by anatomic location, per STS/EACTS congenital nomenclature).

**Data source note:** Most quantitative claims below derive from aggregated disease-level resources — population birth-defect registries (EUROCAT, national/regional CHD registries), meta-analyses, and large clinical cohorts — rather than individual-patient EHR mining, though several cited studies (e.g., Murmansk registry, Chinese birth cohorts) are themselves registry/EHR-derived aggregates.

Sources: [ICD10Data Q21.0](https://www.icd10data.com/ICD10CM/Codes/Q00-QA0/Q20-Q28/Q21-/Q21.0), [Wikidata Q838139](https://www.wikidata.org/wiki/Q838139)

---

## 2. Etiology

### Disease Causal Factors
VSD arises from **failure of fusion/closure of one or more embryologic components of the interventricular septum** during weeks 4–8 of gestation (see Mechanism section). Etiology is heterogeneous: isolated/non-syndromic VSD is typically considered **multifactorial** (polygenic + environmental), while a substantial minority occur as part of monogenic syndromes or chromosomal disorders.

### Genetic Risk Factors
- **Chromosomal:** Trisomy 21 (Down syndrome) — VSD (often as part of complete atrioventricular septal defect) is present in ~40–45% of Down syndrome individuals with CHD. **22q11.2 deletion syndrome** (DiGeorge/velocardiofacial syndrome) — conotruncal VSDs (often malalignment-type, associated with tetralogy of Fallot, interrupted aortic arch, truncus arteriosus) occur in a meta-analysis pooled prevalence of **14% (95% CI 0.12–0.16)** of 22q11.2DS individuals, with VSD as part of the broader conotruncal spectrum reported in up to 64% of some cohorts when tetralogy of Fallot/pulmonary atresia-with-VSD phenotypes are included.
- **Single-gene / transcription-factor mutations:** *GATA4* (HGNC:4171, OMIM 600576) — heterozygous missense mutations (e.g., G296S) cause familial ASD/VSD with interrupted GATA4–TBX5 physical interaction (Garg et al., PMID:12845333). *NKX2-5* (HGNC:2488, OMIM 600584) — mutations/promoter variants found in VSD cohorts, also cause AV block and other CHD (PMID:22576768). *TBX5* (HGNC:11602, OMIM 601620) — causes Holt-Oram syndrome (heart-hand syndrome), with septal defects (ASD, VSD) among its cardiac manifestations, via TBX5–GATA4 protein interaction disruption. *CFC1* (Cryptic) — implicated in laterality-associated septal defects.
- **Syndromic associations:** Noonan syndrome (PTPN11, RAF1, and other RAS-MAPK pathway genes), Alagille syndrome (JAG1, NOTCH2), VACTERL association, CHARGE syndrome, Ellis-van Creveld syndrome, fetal alcohol syndrome (see environmental).
- **Susceptibility loci:** Genome-wide and candidate-gene studies also implicate polymorphisms in *NKX2-5*, *GATA4*, and *TBX5* as modifiers/susceptibility variants in non-syndromic CHD (PMID:30834692, PMC6503026 — Egyptian cohort).

### Protective Factors
- **Periconceptional folic acid supplementation** is the best-documented protective/environmental factor — associated with an estimated **~20% reduction in overall CHD risk** in a Dutch EUROCAT case-control study (PMID:19952004), and specifically for VSD an adjusted RR of **0.47** in a Chinese folic-acid-user cohort; Hungarian intervention data suggest periconceptional multivitamin/high-dose folic acid supplementation prevented ~40% of CHDs, with the association strongest for VSD and conotruncal defects.
- No well-established protective genetic variants specific to VSD have been robustly replicated (in contrast to protective alleles described for some other complex diseases).

### Environmental / Non-Genetic Risk Factors
- **Maternal pregestational diabetes mellitus** — strong teratogenic risk factor; one case-control estimate gives OR **8.72 (95% CI 3.16–24.07)** for VSD.
- **Maternal alcohol use** — moderate-to-heavy periconceptional alcohol consumption associated with isolated VSD; OR **4.83 (95% CI 1.88–12.41)** for alcohol abuse.
- **Maternal infections** — rubella (congenital rubella syndrome classically causes PDA but also VSD), influenza, febrile illness.
- **Maternal phenylketonuria** (uncontrolled, elevated phenylalanine) — teratogenic to cardiac septation.
- **Teratogenic medications/substances** — retinoic acid, certain anticonvulsants, metronidazole, ibuprofen (implicated in some case-control studies), cocaine, marijuana.
- **Maternal smoking.**
- **Advanced/extreme maternal age**, though the classic epidemiology literature notes VSD incidence is largely *unrelated* to maternal age, birth order, sex, or socioeconomic status in most studies (PMID:3840586).

### Gene-Environment Interactions
Folate-pathway gene polymorphisms (e.g., *MTHFR*, *FOLR1*, *FOLR2*) have been studied for interaction with periconceptional folate status and CHD/VSD risk (PMC10930486), though the *TYMS* gene specifically was not associated with septal defects in a Han Chinese cohort (PMC3285645). Maternal diabetic hyperglycemia interacting with genetic susceptibility (e.g., in the RAS-MAPK or NKX2-5 pathways) is a proposed but incompletely characterized gene-environment mechanism.

Sources: [PMID:12845333 GATA4](https://pubmed.ncbi.nlm.nih.gov/12845333/), [PMID:22576768 NKX2-5](https://pubmed.ncbi.nlm.nih.gov/22576768/), [PMC12573319 22q11.2 meta-analysis](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12573319/), [Johns Hopkins maternal lifestyle](https://pure.johnshopkins.edu/en/publications/maternal-lifestyle-factors-and-risk-for-ventricular-septal-defect/), [PMC6069126 Murmansk registry](https://pmc.ncbi.nlm.nih.gov/articles/PMC6069126/), [PMID:19952004 folic acid Netherlands](https://pubmed.ncbi.nlm.nih.gov/19952004/)

---

## 3. Phenotypes

### Symptoms / Clinical Signs (by defect size and shunt magnitude)

| Phenotype | HPO term | Onset | Frequency/notes |
|---|---|---|---|
| Holosystolic (pansystolic) murmur, harsh, left lower sternal border | HP:0030148 (Holosystolic murmur) / HP:0030148-adjacent HP:0031667 | Neonatal–infancy | Classic finding in small-moderate VSD; loudness inversely correlates with defect size in small VSDs ("much cry, little wool") |
| Tachypnea | HP:0002789 | Infancy (moderate–large VSD) | Frequent with significant left-to-right shunt |
| Failure to thrive / poor weight gain | HP:0001508 | Infancy | Common in moderate-large VSD due to increased metabolic demand and feeding difficulty |
| Diaphoresis with feeding | HP:0031929 (Hyperhidrosis) | Infancy | Sign of heart failure in infants |
| Congestive heart failure | HP:0001635 | Infancy (large VSD, as pulmonary vascular resistance falls, typically 4–8 weeks of age) | Frequent in unrepaired large VSD |
| Recurrent respiratory infections | HP:0002205 (Recurrent respiratory infections) | Infancy–childhood | Pulmonary overcirculation predisposes to pneumonia |
| Failure to thrive with tachypnea/diaphoresis with feeds | — | Infancy | Classic infant heart-failure triad |
| Cyanosis (late) | HP:0000961 | Late (years, if Eisenmenger physiology develops) | Only with reversal of shunt (right-to-left) |
| Clubbing (late, Eisenmenger) | HP:0100759 | Late | Sign of chronic hypoxemia |
| Exertional dyspnea | HP:0002875 | Childhood–adult | With larger or uncorrected defects |
| Growth retardation | HP:0001510 | Infancy–childhood | Correlates with shunt magnitude |
| Hepatomegaly | HP:0002240 | Infancy | Sign of right heart failure/systemic venous congestion |

### Laboratory / Imaging Abnormalities
- **Elevated BNP/NT-proBNP** — correlates with hemodynamically significant shunts and heart failure.
- **Echocardiographic findings** — defect location/size, direction and velocity of shunt flow (color Doppler), left atrial/ventricular enlargement (volume overload), estimated pulmonary artery pressure via tricuspid regurgitant jet.
- **ECG** — left ventricular hypertrophy (volume overload) in moderate-large VSD; biventricular hypertrophy if pulmonary hypertension develops.
- **Chest X-ray** — cardiomegaly, increased pulmonary vascular markings (pulmonary plethora) with significant shunts.

### Phenotype Characteristics
- **Age of onset:** Congenital (present at birth); clinical detection ranges from prenatal (fetal echo, from ~18–24 weeks) to incidental detection in asymptomatic adults for small residual/undiagnosed defects.
- **Severity:** Highly variable — trivial/small VSDs are often asymptomatic (Qp:Qs <1.5:1); moderate VSDs cause mild-moderate symptoms; large, unrestrictive VSDs (Qp:Qs >2:1) cause overt heart failure in infancy.
- **Progression:** Most small muscular VSDs are stable or regress (spontaneous closure); large VSDs are progressive toward heart failure and, if uncorrected, irreversible pulmonary vascular disease (Eisenmenger syndrome) typically by 1–2 years of age in the largest defects.
- **Frequency of specific findings among affected individuals:** Directly size-dependent; ~85–90% of small isolated VSDs are asymptomatic and close spontaneously; large VSDs are almost universally symptomatic if unrepaired.

### Quality of Life Impact
Small, hemodynamically insignificant or spontaneously closed VSDs carry essentially normal QoL and life expectancy. Unrepaired large VSDs or those progressing to Eisenmenger syndrome carry major QoL impact: exercise intolerance, cyanosis, recurrent hospitalization, pregnancy contraindication, and reduced life expectancy. Corrected VSDs (surgical/transcatheter) generally normalize long-term QoL, though a subset have residual arrhythmia, valve regurgitation, or exercise limitation.

Sources: [NCBI Bookshelf StatPearls VSD](https://www.ncbi.nlm.nih.gov/books/NBK470330/), [PMID:38857582 prevalence and spontaneous closure first year](https://pubmed.ncbi.nlm.nih.gov/38857582/)

---

## 4. Genetic / Molecular Information

### Causal Genes (non-syndromic and syndromic)
| Gene | HGNC | OMIM | Role |
|---|---|---|---|
| GATA4 | HGNC:4171 | 600576 | Cardiac transcription factor; missense mutations (e.g. p.Gly296Ser) cause familial ASD/VSD; disrupts GATA4-TBX5 interaction (PMID:12845333) |
| NKX2-5 | HGNC:2488 | 600584 | Homeobox transcription factor; promoter and coding variants found in VSD (PMID:22576768); also causes AV conduction defects |
| TBX5 | HGNC:11602 | 601620 | T-box transcription factor; causes Holt-Oram syndrome; interacts physically with GATA4 |
| CFC1 (Cryptic) | HGNC:1878 | 605194 | Laterality/Nodal signaling; implicated in septal defects with heterotaxy |
| JAG1 / NOTCH2 | HGNC:6188 / HGNC:7882 | 601920 / 600275 | Alagille syndrome (VSD/peripheral pulmonic stenosis common) |
| PTPN11 / RAF1 / others | — | Noonan syndrome genes | RAS-MAPK pathway; pulmonic stenosis, hypertrophic cardiomyopathy, and septal defects |

### Pathogenic Variants
- **Variant classification/type:** Predominantly missense mutations in cardiac transcription factor genes (per ACMG/AMP framework, classified pathogenic/likely pathogenic via functional and segregation data — e.g., ClinVar entries for GATA4/NKX2-5/TBX5).
- **Allele frequency:** Disease-causing variants in GATA4/NKX2-5/TBX5 are individually rare (private/familial) in gnomAD; common non-coding polymorphisms in these genes have been studied as susceptibility alleles in case-control association studies but effect sizes are generally modest.
- **Somatic vs germline:** VSD-causing variants are germline (developmental disease); no established somatic mosaicism mechanism specific to isolated VSD, though mosaicism has been documented in some familial CHD pedigrees.
- **Functional consequences:** Loss-of-function/haploinsufficiency is the predominant mechanism for GATA4, NKX2-5, and TBX5 (dose-sensitive transcription factors); dominant-negative effects also reported for some GATA4/TBX5 missense alleles that disrupt protein-protein interaction rather than DNA binding.

### Modifier Genes
*Sarcospan (SSPN)* — genetically interacts with *Nkx2-5* in mouse models to modulate penetrance/severity of muscular VSD (PMC5390293). Genetic background/modifier loci mapped to mouse chromosomes 6, 8, and 10 influence VSD susceptibility in *Nkx2-5+/-* mice (PMID:22534315).

### Chromosomal Abnormalities
- **Trisomy 21** (Down syndrome) — most common chromosomal association with VSD/AVSD.
- **22q11.2 deletion** — conotruncal VSD spectrum.
- **Trisomy 13, Trisomy 18** — VSD frequently part of the multi-organ malformation phenotype.
- **Turner syndrome (45,X)** — more classically left-sided lesions (bicuspid aortic valve, coarctation) but VSD reported.

### Epigenetic Information
Epigenetic mechanisms in cardiac septation are an active research area (e.g., histone modification at cardiac transcription factor loci during second heart field development), but disease-specific DNA methylation signatures for isolated VSD are not yet well established in humans; most epigenetic CHD literature focuses on broader conotruncal/hypoplastic left heart phenotypes.

Sources: [PMID:12845333](https://pubmed.ncbi.nlm.nih.gov/12845333/), [PMID:22576768](https://pubmed.ncbi.nlm.nih.gov/22576768/), [PMC5390293 Sspn-Nkx2-5](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5390293/), [PMID:22534315 complex trait Nkx2-5](https://pubmed.ncbi.nlm.nih.gov/22534315/)

---

## 5. Environmental Information

- **Environmental/teratogenic factors:** maternal diabetes (OR 8.72), maternal alcohol use (OR 4.83), phenylketonuria, retinoic acid exposure, certain medications (metronidazole, NSAIDs in some studies), organic solvent exposure (industrial/occupational, less robustly established).
- **Lifestyle factors:** maternal smoking, alcohol consumption, poor glycemic control in pregestational diabetes, obesity (emerging risk factor in some cohorts), inadequate periconceptional folate intake.
- **Infectious agents:** Congenital rubella syndrome (Rubella virus, NCBI Taxon 11041) is the classical infectious teratogen associated with structural CHD including VSD, though PDA and pulmonary artery stenosis are more characteristic; maternal influenza and other febrile illnesses during the critical period of cardiac septation (weeks 4–8) have also been associated with increased VSD risk in some epidemiologic studies.

Sources: [PMC6069126 Murmansk risk factors](https://pmc.ncbi.nlm.nih.gov/articles/PMC6069126/), [Johns Hopkins maternal lifestyle](https://pure.johnshopkins.edu/en/publications/maternal-lifestyle-factors-and-risk-for-ventricular-septal-defect/)

---

## 6. Mechanism / Pathophysiology

### Embryologic/Developmental Causal Chain
The interventricular septum forms through **coordinated fusion of at least three embryologic components** between roughly the 5th and 8th weeks of gestation:
1. **Muscular (trabecular) septum** — grows upward from the ventricular floor.
2. **Membranous septum** — derives from the fusion of endocardial cushion tissue with the conotruncal (outflow tract) ridges.
3. **Inlet septum** — formed by the endocardial cushions during atrioventricular canal septation.
4. **Outlet (infundibular/conal) septum** — formed by fusion/rotation of the conotruncal ridges as they spiral to separate the aorta and pulmonary trunk.

**Failure of fusion at any of these sites** produces a VSD classified by anatomic location: **perimembranous** (most common, ~80% of clinically significant VSDs, at the junction of muscular and membranous septum, often adjacent to the tricuspid/aortic valves), **muscular** (most common type overall, including small trabecular defects, high spontaneous closure rate), **inlet** (AV-canal type, often associated with AVSD/Down syndrome), and **outlet/doubly-committed subarterial** (conotruncal, associated with 22q11.2 deletion and often with aortic cusp prolapse/aortic regurgitation).

### Cellular Processes
Second heart field (SHF)-derived cardiomyocyte proliferation and migration are essential for septal myocardial growth; **impaired cardiomyocyte proliferation** (e.g., via reduced Cdk4/Cdk2 activity downstream of Gata4/Tbx5 haploinsufficiency) produces thin, incompletely fused septal myocardium (PMC3349729, academic.oup.com/hmg article). Endocardial cushion mesenchymal transformation (epithelial-to-mesenchymal transition, EMT) is required for inlet/membranous septation; disruption of this process (e.g., in Down syndrome-associated AVSD) contributes to septal defects.

### Molecular Pathways
- **Cardiac transcription factor network:** GATA4–NKX2-5–TBX5 form a cooperative transcriptional complex regulating downstream cardiac structural and cell-cycle genes; GATA4 and TBX5 directly activate *Cdk4*, and TBX5 alone activates *Cdk2*, linking this network to septal myocardial proliferation.
- **NOTCH signaling** — critical for endocardial cushion EMT and outflow tract septation (relevant to Alagille syndrome-associated VSD).
- **RAS-MAPK pathway** — implicated in Noonan-syndrome-associated septal and valvar defects.
- **Nodal/Cryptic (CFC1) signaling** — left-right patterning pathway relevant to laterality-associated conotruncal/septal defects.

Suggested GO terms: `GO:0003281` (ventricular septum development), `GO:0003148` (outflow tract septum morphogenesis), `GO:0003203` (endocardial cushion morphogenesis), `GO:0061036` (positive regulation of cardiac muscle cell proliferation).

### Protein Dysfunction
Loss-of-function/haploinsufficiency of dose-sensitive cardiac transcription factors (GATA4, NKX2-5, TBX5) is the principal molecular mechanism identified to date; these are DNA-binding transcriptional regulators whose reduced dosage or disrupted protein-protein interaction (rather than misfolding/aggregation, which is not a feature of this disease class) impairs target gene activation during septal myocardial development.

### Pathophysiologic Consequence — Hemodynamics (postnatal)
Once a VSD is present, the **causal chain from anatomic defect to clinical manifestation** is:
1. Structural defect in ventricular septum (persists from embryogenesis) →
2. Communication between high-pressure LV and lower-pressure RV →
3. **Left-to-right shunt** (shunt magnitude determined by defect size + relative pulmonary vs. systemic vascular resistance) →
4. Increased pulmonary blood flow (pulmonary overcirculation) and LA/LV volume overload →
5. (If large/unrestrictive and uncorrected) chronic pulmonary vascular remodeling → progressively rising pulmonary vascular resistance →
6. Shunt reversal (right-to-left) once pulmonary vascular resistance exceeds systemic resistance → **Eisenmenger syndrome** (cyanosis, clubbing, irreversible pulmonary hypertension, inoperability).

This same convergent cascade (endothelial dysfunction → PASMC proliferation/vasoconstriction → obstructive pulmonary vascular remodeling → increased PVR) is captured generically in the dismech `pulmonary_vascular_remodeling` module and is directly applicable as the downstream consequence node for large/uncorrected VSD.

### Tissue Damage / Downstream Organ Involvement
Chronic pulmonary overcirculation causes pulmonary vascular smooth muscle hypertrophy and eventual plexiform arteriopathy (irreversible pulmonary vascular disease). Chronic RV volume/pressure overload can progress to right ventricular hypertrophy and failure. Aortic cusp prolapse (particularly right coronary cusp) with resultant aortic regurgitation is a recognized complication of outlet/perimembranous VSDs due to loss of septal support beneath the aortic valve (Venturi effect).

### Molecular/Omics Profiling
Single-cell and spatial transcriptomic atlases of the developing human and mouse heart (e.g., Human Developmental Cell Atlas) have profiled second heart field and endocardial cushion populations relevant to septation, though disease-specific (VSD-patient-derived) single-cell data are limited; most mechanistic single-cell work is in animal/iPSC-cardiomyocyte models rather than direct human VSD tissue, given the fetal/embryonic timing of the causal lesion.

Sources: [UNSW Embryology VSD](https://embryology.med.unsw.edu.au/embryology/index.php/Cardiovascular_System_-_Ventricular_Septal_Defects), [StatPearls VSD](https://www.ncbi.nlm.nih.gov/books/NBK470330/), [Oxford HMG Gata4/Tbx5 disruption](https://academic.oup.com/hmg/article/23/19/5025/2900639), [PMC3349729 Gata4 functional deficits](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3349729/)

---

## 7. Anatomical Structures Affected

### Organ Level
- **Primary:** Heart, specifically the interventricular septum (UBERON:0002094, interventricular septum).
- **Secondary/complication-driven:** Lungs (pulmonary vasculature, in chronic overcirculation/pulmonary hypertension — UBERON:0002048), right ventricle (UBERON:0002080, secondary hypertrophy/failure), left atrium and left ventricle (UBERON:0002079/UBERON:0002084/UBERON:0002078/UBERON:0006631, volume overload/dilation), aortic valve (UBERON:0002137, cusp prolapse/regurgitation in outlet VSD), liver (UBERON:0002107, congestive hepatomegaly in heart failure).
- **Body systems:** Cardiovascular system primarily; respiratory system secondarily (pulmonary overcirculation, recurrent infections); hepatic/systemic venous congestion in decompensated heart failure.

### Tissue and Cell Level
- **Cardiac myocytes** (CL:0000746, cardiac muscle cell) — septal myocardial tissue, site of the primary developmental defect.
- **Endocardial cushion mesenchymal cells** (CL:0002350-adjacent, endocardial cell/cushion mesenchyme) — involved in inlet/membranous septum formation.
- **Second heart field progenitor cells** — contribute to outflow tract/conal septum.
- **Pulmonary vascular smooth muscle cells** (CL:0000359, pulmonary artery smooth muscle cell) — remodel in chronic pulmonary hypertension/Eisenmenger physiology.
- **Cardiac fibroblasts** — involved in septal connective tissue and, secondarily, in any reparative/scarring response post-surgical closure.

### Subcellular Level
GO Cellular Component relevance is largely at the level of **nucleus** (GO:0005634, site of GATA4/NKX2-5/TBX5 transcriptional activity) rather than a specific organelle-level pathology (this is a morphogenetic/structural disease, not a primary organelle disease).

### Localization
- Perimembranous (adjacent to aortic and tricuspid valves) — most common clinically significant location.
- Muscular (trabecular, apical, mid-muscular) — most common overall (many spontaneously close).
- Inlet (AV canal type).
- Outlet/infundibular/doubly committed subarterial (conal).
Defects can be single or multiple ("Swiss cheese septum," typically multiple muscular defects). No inherent lateralization (the septum is a midline structure), though anterior/posterior/superior/inferior location within the septum is clinically relevant for surgical planning.

Sources: [PMC6052685 anatomy of VSD](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6052685/)

---

## 8. Temporal Development

### Onset
- **Congenital** — the anatomic defect is present at birth (embryogenesis complete by 8 weeks gestation).
- **Detection timing:** Prenatal detection possible from ~18–24 weeks via fetal echocardiography (isolated VSDs detected in a large series between 19–24 weeks gestation, PMID/PMC references above); many small VSDs are detected postnatally on routine neonatal exam (murmur) or incidentally later in childhood/adulthood.
- **Symptom onset pattern:** Large VSDs become symptomatic as pulmonary vascular resistance falls after birth, typically **4–8 weeks of age**, coinciding with the physiologic drop in PVR that unmasks the full left-to-right shunt.

### Progression
- **Disease course:** Highly bimodal — (1) small/muscular VSDs frequently regress via spontaneous closure (see below), becoming asymptomatic/resolved; (2) moderate-large VSDs are progressive without intervention, evolving toward heart failure in infancy and, if uncorrected for years, irreversible pulmonary vascular disease (Eisenmenger syndrome, generally established by early childhood in the largest defects, though timeline is variable).
- **Progression rate:** Rapid in large unrestrictive defects (heart failure within weeks-months of birth); slow/absent in small restrictive defects.
- **Course pattern:** Largely stable once either spontaneously closed or surgically/percutaneously corrected; progressive if left uncorrected and hemodynamically significant.

### Patterns — Spontaneous Closure (Remission)
- **~85–90% of small isolated VSDs close spontaneously within the first year of life** (StatPearls; PMID:38857582 reports resultant 1-year prevalence of ~0.5% down from a newborn prevalence as high as 3.3% with sensitive echo screening).
- By **10 years of age, ~75% of small VSDs have closed spontaneously**, with muscular defects closing more often (83%) than perimembranous defects (68% vs. 29% in one comparative series).
- Closure predictors: smaller defect size, muscular (vs. perimembranous) morphology, younger age at diagnosis.
- Some muscular VSDs close spontaneously **in utero** (6.8% of prenatally diagnosed muscular VSDs in one series), with an additional 75% closing within the first postnatal year.

### Critical Periods
The embryologic window of **weeks 4–8 of gestation** is the critical period during which septal fusion occurs and during which teratogenic exposures (maternal diabetes, alcohol, retinoic acid, rubella) exert their effect. Postnatally, the **first 1–2 years of life** represent the critical window both for spontaneous closure to occur and, in large defects, for surgical intervention to prevent irreversible pulmonary vascular disease.

Sources: [PMID:38857582](https://pubmed.ncbi.nlm.nih.gov/38857582/), [PMID:31208700 spontaneous closure rates](https://pubmed.ncbi.nlm.nih.gov/31208700/), [PMID:12206559 factors influencing closure](https://pubmed.ncbi.nlm.nih.gov/12206559/), [PMC4072558 prenatal muscular VSD natural history](https://pmc.ncbi.nlm.nih.gov/articles/PMC4072558/)

---

## 9. Inheritance and Population

### Epidemiology
- **Incidence/prevalence at birth:** Classic teaching cites ~300–350 per 100,000 live births (~3–3.5 per 1000), representing ~30% of all newborn CHD. With sensitive echocardiographic screening protocols, newborn prevalence estimates rise substantially — one study found a **3.3% prevalence in unselected newborns**, reflecting detection of small, often clinically silent muscular VSDs that would previously go undetected and would mostly close spontaneously.
- **1-year prevalence:** ~0.5% (following spontaneous closure of ~9/10 of newborn-detected defects) (PMID:38857582).
- **Adult prevalence:** Estimated 0.3 per 1000 for simple/isolated VSD, making it (excluding bicuspid aortic valve) the most common CHD persisting into adulthood.
- VSD represents nearly 50% of all infants presenting with a congenital cardiovascular anomaly in some series (StatPearls).

### Inheritance Pattern
- **Isolated/non-syndromic VSD:** predominantly **multifactorial/polygenic** inheritance, though family recurrence risk is elevated above general population risk (empiric recurrence risk for a subsequent sibling of an isolated CHD proband is commonly cited around 2–4%, higher with an affected parent).
- **Syndromic monogenic forms:** **Autosomal dominant** for GATA4-, NKX2-5-, and TBX5-related familial CHD/Holt-Oram syndrome, with variable expressivity and incomplete penetrance.
- **Chromosomal forms:** Trisomy 21 (usually sporadic nondisjunction; ~1% familial via Robertsonian translocation), 22q11.2 deletion (mostly de novo, ~10% inherited autosomal dominant from an affected parent).
- **Penetrance/expressivity:** Incomplete penetrance and variable expressivity are well documented for GATA4/NKX2-5/TBX5 familial CHD pedigrees — some mutation carriers are unaffected or have only mild/subclinical defects, complicating genetic counseling.
- **Founder effects:** Not prominently described for isolated VSD-causing variants (contrast with some other monogenic cardiac diseases); GATA4/NKX2-5/TBX5 mutations are generally private/family-specific.

### Population Demographics
- **Sex ratio:** No strong sex predilection reported in the classic epidemiologic literature (PMID:3840586), though some sources note a slight male predominance for perimembranous VSD specifically; AVSD (inlet-type, Down syndrome-associated) has no strong sex skew either.
- **Racial/ethnic and geographic variation:** Incidence reported as broadly similar across races/regions in classic studies, though registry-based studies (e.g., Murmansk County, Russia, PMC6069126) identify region-specific risk-factor profiles; some studies suggest higher birth prevalence in Asian populations, potentially confounded by screening intensity.
- **Age distribution:** By definition present from birth; clinically ascertained age distribution skews toward infancy (symptomatic large defects) and incidental discovery in childhood/adulthood (small residual defects).

Sources: [wikidoc VSD epidemiology](https://www.wikidoc.org/index.php/Ventricular_septal_defect_epidemiology_and_demographics), [PMID:38857582](https://pubmed.ncbi.nlm.nih.gov/38857582/), [PMID:3840586](https://pubmed.ncbi.nlm.nih.gov/3840586/), [AHA Journals Circulation VSD review](https://www.ahajournals.org/doi/full/10.1161/circulationaha.106.618124)

---

## 10. Diagnostics

### Clinical Tests
- **Auscultation:** Harsh holosystolic murmur, loudest at the left lower sternal border; intensity/duration inversely related to defect size for small restrictive VSDs.
- **Echocardiography (transthoracic, 2D/color Doppler)** — the primary diagnostic modality: defines defect location/size, shunt direction/velocity (estimates RV/PA pressure via Doppler gradient), chamber size, and associated lesions (aortic cusp prolapse, other CHD).
- **ECG:** LVH pattern with significant shunt; combined ventricular hypertrophy if pulmonary hypertension present.
- **Chest radiograph:** Cardiomegaly and pulmonary vascular plethora with significant shunts; normal in small VSDs.
- **Cardiac catheterization:** Reserved for cases needing precise Qp:Qs ratio and pulmonary vascular resistance measurement (especially pre-operative assessment for borderline/large defects, or when non-invasive imaging is discordant/inconclusive), and for device closure procedures.
- **Cardiac MRI/CT:** Adjunctive for complex anatomy, RV/LV volumetrics, or when echo windows are poor (e.g., adult/post-surgical patients).
- **Biomarkers:** BNP/NT-proBNP as adjuncts to assess hemodynamic significance/heart-failure status (not diagnostic of VSD itself).

### Genetic Testing
- Not routinely indicated for isolated, non-syndromic VSD without other anomalies.
- **Chromosomal microarray (CMA)** and/or **FISH for 22q11.2 deletion** recommended when VSD is conotruncal-type (especially outlet/malalignment VSD) or accompanied by other 22q11.2DS features (immune, palatal, facial, endocrine).
- **Karyotype/trisomy 21 testing** when VSD occurs with AVSD-type morphology or other Down syndrome features.
- **Gene panels** for syndromic CHD (Noonan spectrum panel, CHD gene panels including GATA4/NKX2-5/TBX5) when familial recurrence, syndromic features, or multiple affected relatives are present.
- **Whole exome/genome sequencing** increasingly used in research and clinical settings for CHD with extracardiac anomalies or suspected monogenic etiology, though yield for truly isolated non-syndromic VSD remains modest.

### Prenatal / Screening
- Fetal echocardiography (routine anatomy scan can detect larger VSDs; dedicated fetal echo for higher-risk pregnancies) from ~18–24 weeks gestation.
- Standard screening includes 2D grayscale imaging plus color/Doppler flow mapping; 4D/STIC ultrasound increasingly used to improve detection.
- Postnatal pulse oximetry screening (universal newborn CCHD screening) is designed primarily to detect critical cyanotic CHD and will often miss small acyanotic VSDs, which are typically identified by murmur on physical exam.

### Clinical Criteria / Differential Diagnosis
Diagnosis is definitively established by echocardiography demonstrating the septal defect and shunt flow; differential diagnosis for the clinical murmur includes other left-to-right shunt lesions (ASD, PDA), semilunar valve stenosis (pulmonic/aortic stenosis murmurs), and innocent/functional murmurs of infancy.

Sources: [PMC3903045 prenatal ultrasound/Doppler](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3903045/), [PMID:31928261 fetal echo isolated VSD outcome](https://pubmed.ncbi.nlm.nih.gov/31928261/), [StatPearls VSD](https://www.ncbi.nlm.nih.gov/books/NBK470330/)

---

## 11. Outcome / Prognosis

### Survival and Mortality
- **Small, isolated VSDs (spontaneously closed or hemodynamically insignificant):** Excellent prognosis, essentially normal life expectancy.
- **Surgically or percutaneously repaired moderate-large VSDs (repaired before development of pulmonary vascular disease):** Excellent long-term survival, generally approaching that of the general population, though lifelong cardiology follow-up is recommended for residual lesions (shunt, arrhythmia, valve regurgitation).
- **Uncorrected large VSD progressing to Eisenmenger syndrome:** Significantly reduced life expectancy; ventricular failure, hemoptysis, arrhythmia/sudden cardiac death, and pregnancy-related complications are the principal causes of death. Pulmonary thromboembolism occurs in a reported **21–29%** of Eisenmenger patients as a complication. Eisenmenger physiology is generally considered an irreversible, inoperable state, marking a pivotal negative prognostic transition.
- **Pregnancy in Eisenmenger syndrome** carries very high maternal mortality (one case series reported **36% maternal mortality**), and is generally considered a contraindication to pregnancy.

### Morbidity and Function
- Post-repair morbidity: residual VSD/shunt, complete heart block (risk from surgical proximity to conduction tissue in perimembranous defects), tricuspid or aortic valve regurgitation (particularly outlet VSD with pre-existing cusp prolapse), arrhythmia (long-term surveillance concern), and rarely need for reintervention.
- Unrepaired, hemodynamically significant VSD: failure to thrive, recurrent respiratory infections, exercise intolerance, and if progressing to Eisenmenger physiology, cyanosis, clubbing, erythrocytosis, and multi-organ effects of chronic hypoxemia.

### Prognostic Factors
- Defect size/type (muscular defects have better spontaneous closure/prognosis than perimembranous).
- Timing of surgical correction relative to onset of pulmonary vascular disease (earlier correction before irreversible pulmonary vascular remodeling yields markedly better outcomes).
- Presence of associated syndromic/chromosomal diagnosis (e.g., Down syndrome/AVSD carries additional risk of accelerated pulmonary vascular disease at lower shunt volumes than isolated VSD).
- Development of aortic regurgitation (progressive, may require earlier surgical closure even for small defects to prevent valve damage).

Sources: [StatPearls Eisenmenger Syndrome](https://www.ncbi.nlm.nih.gov/books/NBK507800/), [PMC5112756 pregnancy outcomes Eisenmenger](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5112756/), [Medscape VSD pathophysiology](https://emedicine.medscape.com/article/892980-overview)

---

## 12. Treatment

### Pharmacotherapy (medical management, pre-/peri-operative)
- **Diuretics** (e.g., furosemide) — for heart-failure symptom management in infants with significant left-to-right shunt (NCIT:C15986 Pharmacotherapy).
- **ACE inhibitors** (e.g., captopril, enalapril) — afterload reduction to reduce shunt fraction and improve symptoms.
- **Digoxin** — historically used for heart failure symptom control in infants, though use has declined.
- **Nutritional support/high-calorie formula** — for failure to thrive due to increased metabolic demand (NCIT:C15433 Nutritional Support — a genuinely dietary/caloric-density intervention here, not a drug substitute).
- **Pulmonary vasodilator therapy** (e.g., bosentan, sildenafil, prostacyclin analogs) — for established Eisenmenger physiology/pulmonary arterial hypertension, targeting symptom palliation rather than cure (NCIT:C15986 Pharmacotherapy; therapeutic_agent bindable to CHEBI, e.g. CHEBI:59784 bosentan, CHEBI:9139 sildenafil).

### Surgical / Interventional
- **Surgical VSD closure (patch closure via cardiopulmonary bypass)** — the historic standard of care for moderate-large, hemodynamically significant defects; typically performed in infancy for large defects with heart failure/failure to thrive, or electively in early childhood for moderate defects (NCIT:C15329 Surgical Procedure).
- **Transcatheter (percutaneous) device closure** — an increasingly used alternative for selected muscular VSDs (technically difficult surgically) and for post-surgical residual defects; uses FDA-approved occluder devices delivered via catheter; considered particularly for complex/high-surgical-risk patients. Long-term outcomes for perimembranous device closure show durable results but historically carry a risk of complete heart block requiring careful patient selection.
- **Hybrid procedures** (perventricular device closure without cardiopulmonary bypass, via small thoracotomy with echo guidance) — emerging technique combining surgical access with device delivery, reducing bypass-related morbidity.
- **Pulmonary artery banding** — a palliative surgical procedure (historically, now less common) to reduce pulmonary overcirculation in infants deemed too high-risk for primary repair, as a bridge to later definitive closure.

### Supportive / Rehabilitative
- Routine pediatric cardiology follow-up echocardiography.
- Physical activity guidance based on hemodynamic status (no restriction for small/repaired defects with normal pulmonary pressures; activity restriction for significant residual pulmonary hypertension).
- Endocarditis prophylaxis per current AHA guidelines — generally recommended for unrepaired cyanotic CHD or during the first 6 months after prosthetic material repair, not for isolated small unrepaired VSD in current guidelines.

### Experimental
- Ongoing trials of newer transcatheter occluder device designs and refined perventricular hybrid techniques (searchable on ClinicalTrials.gov under "ventricular septal defect device closure").
- Investigational pulmonary vasodilator regimens for established Eisenmenger physiology (combination therapy trials).

### Treatment Strategy / Algorithm
General approach: (1) observe small, asymptomatic VSDs for spontaneous closure with serial echo; (2) medically manage symptomatic moderate-large VSDs with diuretics/afterload reduction while awaiting either spontaneous improvement or surgical timing; (3) proceed to surgical or transcatheter closure for large/unrestrictive defects causing heart failure, failure to thrive, or significant pulmonary overcirculation, generally before 6–12 months of age to prevent irreversible pulmonary vascular disease, or earlier if refractory heart failure; (4) closure also indicated for smaller defects complicated by progressive aortic regurgitation or recurrent endocarditis regardless of shunt magnitude; (5) for established Eisenmenger syndrome, closure is contraindicated (would acutely worsen RV afterload against fixed pulmonary vascular resistance) and management shifts to palliative pulmonary vasodilator therapy.

Sources: [Johns Hopkins transcatheter VSD](https://www.hopkinsmedicine.org/health/treatment-tests-and-therapies/ventricular-septal-defect-transcatheter-repair-for-children), [PMC5943568 long-term device closure outcomes](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5943568/), [AHA Circulation transcatheter device closure](https://www.ahajournals.org/doi/10.1161/01.cir.0000137116.12176.a6)

---

## 13. Prevention

### Primary Prevention
- **Periconceptional folic acid/multivitamin supplementation** is the single most evidence-supported primary prevention strategy, with the strongest documented effect specifically for VSD and conotruncal defects among CHD subtypes (RR ~0.47–0.72 across studies cited above; Hungarian intervention data suggesting up to ~40% CHD reduction with high-dose periconceptional folic acid).
- **Optimization of maternal pregestational diabetes glycemic control** prior to and during early pregnancy substantially reduces teratogenic CHD risk.
- **Avoidance of alcohol** during pregnancy (no established safe threshold; abstinence recommended).
- **Rubella vaccination** (MMR) prior to pregnancy to prevent congenital rubella syndrome-associated CHD.
- **Avoidance of known teratogenic medications** (e.g., isotretinoin/retinoic acid) during pregnancy planning and gestation.

### Secondary Prevention (Early Detection)
- Prenatal fetal echocardiography for pregnancies at elevated risk (family history of CHD, maternal diabetes, known teratogen exposure, abnormal first-trimester screening/nuchal translucency).
- Newborn physical examination (auscultation for murmur) as a low-cost universal secondary screening tool, supplemented by echocardiography when a murmur or other clinical sign is detected.
- Genetic counseling and prenatal genetic testing (CMA, 22q11.2 FISH, karyotype) when VSD is identified prenatally, given the substantial rate of associated chromosomal/syndromic diagnoses, particularly for conotruncal/outlet and inlet/AVSD-type defects.

### Tertiary Prevention
- Timely surgical/transcatheter closure of hemodynamically significant VSD before irreversible pulmonary vascular disease develops is the key tertiary-prevention intervention, preventing progression to Eisenmenger syndrome.
- Surveillance and early closure for progressive aortic regurgitation in outlet-type VSD to prevent long-term valve damage.

### Genetic Counseling
Recommended for families with a monogenic (GATA4/NKX2-5/TBX5/Holt-Oram) or chromosomal (22q11.2, trisomy 21) etiology, addressing recurrence risk (elevated above baseline population risk of ~1% for a couple with one affected child with isolated CHD, substantially higher — up to 50% — for autosomal dominant monogenic forms) and reproductive options (preimplantation genetic diagnosis, prenatal diagnosis).

Sources: [PMID:19952004](https://pubmed.ncbi.nlm.nih.gov/19952004/), [Obeid et al. folate/CHD review](https://cdt.amegroups.org/article/view/24182/html), [PMC10930486 folate gene polymorphisms](https://pmc.ncbi.nlm.nih.gov/articles/PMC10930486/)

---

## 14. Other Species / Natural Disease

- **Taxonomy of affected species:** VSD occurs naturally in several domestic species, most notably **dogs** (Canis lupus familiaris, NCBITaxon:9615) and **cats** (Felis catus, NCBITaxon:9685), as well as reported in cattle, pigs, and horses.
- **Breed predisposition (dogs):** English Bulldogs, West Highland White Terriers, and other breeds show elevated reported prevalence in veterinary cardiology literature (breed-specific data catalogued in OMIA and veterinary cardiology registries; specific VBO breed identifiers available via the Vertebrate Breed Ontology for these predisposed breeds).
- **Natural disease significance:** VSD is among the more commonly diagnosed congenital cardiac defects in small-animal veterinary cardiology, typically identified via auscultation (murmur) and echocardiography in young animals, analogous to human clinical pathways; small/muscular defects in animals similarly show potential for a benign course, while large defects can progress to heart failure or (rarely reported) pulmonary hypertension analogous to Eisenmenger physiology.
- **Comparative biology:** The embryologic septation process (fusion of muscular, membranous, inlet, and outlet septal components) is highly conserved across mammals, supporting the translational relevance of veterinary case series and of genetically engineered mouse models to human disease mechanism.
- **Orthologous genes:** Mouse *Gata4*, *Nkx2-5*, and *Tbx5* are direct orthologs of the human genes discussed above and drive essentially the same septation biology (see Model Organisms, below).
- **Zoonotic potential:** None — VSD is a non-infectious congenital structural anomaly, not a transmissible condition.

Sources: general veterinary cardiology literature (OMIA); no specific PMID retrieved in this search pass — recommend a dedicated OMIA/veterinary-cardiology literature search if breed-level citations are required for KB entry.

---

## 15. Model Organisms

### Genetic Mouse Models
- ***Gata4* heterozygous / conditional mutants:** *Gata4+/-;Tbx5+/-* compound heterozygous mouse embryos display decreased atrial/ventricular myocardial thickness by E11.5 (prior to septation) and, in more severe allelic combinations (e.g., *Gata4^MyoDel/wt;Tbx5+/-*), embryonic lethality with thin myocardium, reduced cardiomyocyte proliferation, and complete atrioventricular septal defects with a common AV valve — closely recapitulating features of human GATA4/TBX5-related septal defects (Oxford HMG 2014, academic.oup.com/hmg/article/23/19/5025).
- ***Nkx2-5* heterozygous knockout mice:** Develop muscular and membranous VSDs; genetic linkage mapping in this model identified modifier loci on mouse chromosomes 6, 8, and 10 that govern susceptibility/penetrance of membranous VSD, demonstrating a complex-trait (multi-locus) genetic architecture even for a single primary mutation (PMID:22534315).
- ***Nkx2-5+/-;Sspn* (Sarcospan) double mutants:** Show higher incidence of muscular VSD than *Nkx2-5+/-* alone, establishing Sspn as a genetic modifier of VSD penetrance in this model (PMC5390293).
- ***Gata4* missense knock-in models (e.g., G296S orthologous variant):** Recapitulate human CHD-causing GATA4 mutation phenotypes in vivo, showing functional deficits in cardiac development consistent with the human familial phenotype (PMC3349729).

### Model Characteristics
- **Phenotype recapitulation:** Mouse transcription-factor mutant models (Gata4, Nkx2-5, Tbx5) faithfully reproduce the core structural phenotype (septal defects, myocardial thinning) and provide direct mechanistic insight into the cell-cycle/proliferation defect (via Cdk4/Cdk2 downregulation) underlying failed septal fusion.
- **Model limitations:** Complete knockouts of these transcription factors are typically embryonic lethal at earlier developmental stages (reflecting broader essential roles in cardiogenesis beyond septation specifically), necessitating heterozygous or conditional/tissue-specific alleles to model the viable, human-relevant VSD phenotype; mouse models also do not fully capture the postnatal hemodynamic and pulmonary vascular disease progression (Eisenmenger physiology) that defines much of human VSD morbidity/mortality, since this is a consequence of the four-chambered postnatal circulation under sustained shunt physiology over years, poorly modeled in short-lived rodents.

### Applications
These murine models are primarily used to dissect the **causal molecular/cellular mechanism of septal non-fusion** (transcription factor dosage, cell-cycle regulation, genetic modifier discovery) rather than to model the later clinical/hemodynamic natural history, which is better characterized through human longitudinal cohorts and registries.

### Resources
- **MGI** (Mouse Genome Informatics) — for *Gata4*, *Nkx2-5*, *Tbx5* allele records and phenotype annotations.
- **IMPC** (International Mouse Phenotyping Consortium) — systematic phenotyping data for knockout alleles of these genes.

Sources: [academic.oup.com/hmg Gata4/Tbx5 disruption 2014](https://academic.oup.com/hmg/article/23/19/5025/2900639), [PMID:22534315 Nkx2-5 complex trait](https://pubmed.ncbi.nlm.nih.gov/22534315/), [PMC5390293 Nkx2-5/Sspn](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5390293/), [PMC3349729 Gata4 in vivo functional deficits](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3349729/)

---

## Summary of Suggested Ontology Term Bindings for KB Curation

| Category | Suggested term(s) |
|---|---|
| Disease | MONDO:0002070; HP:0001629 (VSD as phenotype); Orphanet ORPHA:1480; OMIM 614429 |
| Causal genes | GATA4 (hgnc:4171), NKX2-5 (hgnc:2488), TBX5 (hgnc:11602), CFC1 (hgnc:1878) |
| Phenotypes | HP:0030148 (holosystolic murmur-adjacent), HP:0001635 (congestive heart failure), HP:0001508 (failure to thrive), HP:0002789 (tachypnea), HP:0002205 (recurrent respiratory infections), HP:0000961 (cyanosis), HP:0100759 (clubbing), HP:0002875 (exertional dyspnea) |
| Anatomy | UBERON:0002094 (interventricular septum), UBERON:0002080 (right ventricle), UBERON:0002084 (left ventricle), UBERON:0002048 (lung), UBERON:0002137 (aortic valve) |
| Cell types | CL:0000746 (cardiac muscle cell), CL:0000359 (pulmonary artery smooth muscle cell) |
| Biological process (GO) | GO:0003281 (ventricular septum development), GO:0003148 (outflow tract septum morphogenesis), GO:0003203 (endocardial cushion morphogenesis) |
| Treatments (NCIT) | NCIT:C15329 (Surgical Procedure), NCIT:C15986 (Pharmacotherapy), NCIT:C15433 (Nutritional Support) |
| Chemicals (CHEBI) | CHEBI:59784 (bosentan), CHEBI:9139 (sildenafil) |
| Associated syndromic entities | MONDO term for 22q11.2 deletion syndrome; MONDO term for Down syndrome (trisomy 21); MONDO term for Holt-Oram syndrome |

**Note on data gaps:** This search pass did not retrieve species/breed-specific veterinary PMIDs (Section 14) or detailed single-cell/spatial transcriptomic human VSD-tissue studies (Section 6) — both would benefit from a dedicated follow-up search (OMIA for veterinary; GEO/Human Cell Atlas for omics) before finalizing a KB entry that requires citations in those specific areas.