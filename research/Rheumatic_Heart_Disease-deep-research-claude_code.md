---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-10T00:48:15.158250'
end_time: '2026-08-10T00:53:54.646450'
duration_seconds: 339.49
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Rheumatic Heart Disease
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
  web_search_requests: 20
  num_turns: 22
  total_cost_usd: 1.8363423999999995
  session_id: ccd9973f-d61b-50a6-8cfe-0a77b122d0f2
  stop_reason: end_turn
citation_count: 69
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Rheumatic Heart Disease
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Rheumatic Heart Disease** covering all of the
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

# Rheumatic Heart Disease (RHD) — Comprehensive Research Report

*Prepared to populate a disease-knowledge-base entry (pathophysiology graph, phenotype/gene/treatment annotations). Ontology term suggestions are given as best-effort identifiers; because AI-suggested ontology IDs are known to be occasionally wrong, **curators should verify every ID/label pair against the authoritative ontology (OAK/OLS) before committing** — this report flags terms with lower confidence explicitly.*

---

## 1. Disease Information

**Overview.** Rheumatic heart disease (RHD) is the chronic, permanent cardiac valvular damage that results from one or more episodes of **acute rheumatic fever (ARF)**, itself a delayed, non-suppurative autoimmune sequela of mucosal (pharyngeal, and increasingly recognized skin) infection with **Group A *Streptococcus* (GAS, *Streptococcus pyogenes*)** in a genetically susceptible host. ARF is a multisystem inflammatory illness (joints, heart, CNS, skin, subcutaneous tissue); RHD is specifically the residual, usually left-sided, valvular fibrosis/scarring that persists after the acute inflammatory episode(s) resolve. A single severe ARF episode, and more often *recurrent* episodes, converts initially reversible valvulitis into fixed valve damage — chiefly mitral, then aortic, disease ([WHO fact sheet](https://www.who.int/news-room/fact-sheets/detail/rheumatic-heart-disease); [StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK538286/)).

**Key identifiers:**
- **ICD-10-CM:** I00–I02 (acute rheumatic fever, incl. I01.* "rheumatic fever with heart involvement"); **I05–I09** (chronic rheumatic heart diseases — I05 mitral valve diseases, I06 aortic valve diseases, I07 tricuspid valve diseases, I08 multiple valve diseases, I09 other/unspecified rheumatic heart disease, incl. I09.81 rheumatic heart failure, I09.9 unspecified) ([icd10data.com](https://www.icd10data.com/ICD10CM/Codes/I00-I99/I05-I09)).
- **MONDO / OMIM / Orphanet:** RHD and ARF have MONDO terms integrating DOID/OMIM/Orphanet mappings; exact CURIEs should be confirmed via `mondo.monarchinitiative.org` lookup before curation (not independently verified in this research pass — flag for OAK confirmation rather than assume a specific numeric ID).
- **MeSH:** "Rheumatic Heart Disease" (D012214); "Rheumatic Fever" (D012213).
- **Synonyms:** chronic rheumatic valvular heart disease; post-streptococcal valvulitis; rheumatic valve disease; (historical) rheumatic mitral stenosis/regurgitation, rheumatic aortic stenosis/regurgitation as organ-specific labels.

**Evidence base character:** RHD knowledge is drawn from a mix of aggregated disease-level resources (Global Burden of Disease modeling, national/regional registries such as Australia's RHD registers, WHO fact sheets) and individual-patient data (echocardiographic screening cohorts, hospital case series, and increasingly EHR-linked data in Australia/NZ). Genetic association data come from case-control and GWAS cohorts (South Asia, Aboriginal Australia, sub-Saharan Africa, Brazil, Uganda).

---

## 2. Etiology

**Primary causal chain:** GAS pharyngeal (± skin) infection → in a genetically susceptible host, an aberrant, cross-reactive humoral and cellular immune response → ARF (which may include carditis) → in a subset, and especially with recurrent episodes, permanent valvular fibrosis (RHD). This is fundamentally an **infection-triggered autoimmune** disease, not a direct infective process of the valve (GAS itself is not found in the damaged valve tissue).

### Risk factors

**Environmental/host risk factors** ([WHO](https://www.who.int/news-room/fact-sheets/detail/rheumatic-heart-disease); [Indigenous HPF](https://www.indigenoushpf.gov.au/measures/1-06-rheumatic-fever-rheumatic-heart-disease)):
- Poverty, household crowding, and reduced access to healthcare — the dominant social determinants, driving both the incidence of untreated GAS pharyngitis and delayed diagnosis/inadequate secondary prophylaxis.
- Age 5–14 years for first ARF episode (peak susceptibility window).
- Prior episode(s) of ARF (single strongest risk factor for recurrence/progression — each recurrence compounds valve damage).
- Crowded living conditions facilitating GAS transmission (households, boarding schools, remote communities).
- Possibly skin GAS infection (impetigo/scabies-associated) as an under-recognized trigger, particularly implicated in some high-burden tropical settings.

**Genetic risk factors** (see §4 for detail): HLA class II alleles (HLA-DR/DQ), a novel HLA class III susceptibility locus, and candidate non-HLA loci including the immunoglobulin heavy-chain locus (IGHV4-61 region) ([Nature Reviews Cardiology genetics review](https://www.nature.com/articles/s41569-019-0258-2); [Sci Rep 2020, PMC7265443](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7265443/)).

**Protective factors:** No robust genetic protective variant is well established; the principal modifiable protective interventions are behavioral/health-system (see §13) rather than intrinsic biological protection. Some HLA alleles show consistent negative (protective) association across cohorts in individual studies, but replication across ancestries is inconsistent ([Circulation 1999](https://www.ahajournals.org/doi/full/10.1161/01.cir.99.21.2784)).

**Gene–environment interaction:** The core G×E interaction is between host HLA class II genotype (governing which streptococcal/self peptide epitopes are presented to CD4+ T cells) and the degree/recurrence of GAS exposure (itself environmentally/socioeconomically determined) — repeated antigenic exposure in a susceptible HLA background is thought to drive epitope spreading and progressively severe autoimmune valvulitis.

---

## 3. Phenotypes

RHD/ARF phenotypes span **acute (ARF) manifestations** and **chronic valvular (RHD) manifestations**.

### Acute rheumatic fever manifestations (Jones criteria major/minor)

| Phenotype | Frequency | Notes | Suggested HPO |
|---|---|---|---|
| Carditis (endocarditis/valvulitis, ± myocarditis, ± pericarditis) | Most commonly reported major criterion; subclinical carditis detectable by echo even without murmur | Mitral valve most frequent/severe, then aortic | HP:0001635 (heart failure, if decompensated); HP:0001653 (mitral regurgitation); HP:0001659 (aortic regurgitation) |
| Migratory polyarthritis | Very common major criterion, classically large joints | Fleeting, asymmetric, exquisitely aspirin-responsive | HP:0001369 (arthritis) |
| Sydenham chorea | 10–30% of ARF cases; sole finding in ~20% ([MedLink/StatPearls search summary](https://www.ncbi.nlm.nih.gov/books/NBK594238/)) | Delayed onset 1–8 months post-GAS; 60–80% have concurrent cardiac involvement | HP:0002072 (chorea) |
| Erythema marginatum | <6% of cases | Serpiginous, migratory, trunk/limb-sparing face | HP:0025590 or search HPO "erythema marginatum" |
| Subcutaneous nodules | <10% of cases | Firm, painless, over extensor surfaces; almost always co-occurs with carditis | HP:0001482 (subcutaneous nodule) |
| Fever | Minor criterion | — | HP:0001945 |
| Arthralgia | Minor criterion (cannot double-count with major arthritis) | — | HP:0002829 |
| Elevated ESR/CRP | Minor criterion | Reflects systemic inflammation | HP:0011227 / HP:0011227-adjacent |
| Prolonged PR interval | Minor criterion | ECG finding | HP:0011703 |

**2015 revised Jones criteria** stratify by population risk (low-risk vs. moderate/high-risk, the latter ARF incidence >2/100,000 children/year), formally incorporate **Doppler echocardiography** for subclinical carditis detection, and treat **isolated chorea** or **indolent carditis** as presumptive ARF without requiring other criteria ([Gewitz et al., Circulation 2015, PMID 25908771](https://www.ahajournals.org/doi/10.1161/cir.0000000000000205); [AAP 2024 specificity analysis](https://publications.aap.org/pediatrics/article/153/3/e2023062624/196623/Specificity-of-the-Modified-Jones-Criteria)).

### Chronic RHD manifestations

- **Mitral regurgitation** (earliest, most common lesion; HP:0001653) and **mitral stenosis** (later, from progressive leaflet thickening/fusion; HP:0001718).
- **Aortic regurgitation** (HP:0001659) and **aortic stenosis** (HP:0001650), typically less frequent/severe than mitral disease and rarely isolated.
- **Tricuspid regurgitation**, usually functional/secondary to pulmonary hypertension from left heart disease.
- **Atrial fibrillation** (HP:0005110), often from left atrial enlargement in mitral stenosis — a major driver of thromboembolic stroke risk.
- **Congestive heart failure** (HP:0001635) — dyspnea, edema, orthopnea; often the presenting symptom since chronic RHD is frequently asymptomatic until decompensation.
- **Pulmonary hypertension** (HP:0002092), secondary to chronic left-sided valvular disease.
- **Infective endocarditis** risk elevated on damaged valves.
- **Stroke/systemic embolism** from atrial fibrillation or valve-associated thrombus.

**Age of onset:** ARF classically presents in school-age children (5–14 yrs); first presentation of RHD (often with a murmur or heart-failure symptoms) may not occur until years later, sometimes not until young adulthood, because chronic RHD is frequently **asymptomatic ("latent") until echocardiographic screening or heart failure onset** ([news-medical.net pathophysiology summary](https://www.news-medical.net/health/Rheumatic-heart-disease-pathophysiology.aspx)).

**Severity/progression pattern** (from a prospective severity-progression cohort, [JAHA 2017, Multi-State Model, PMID 28255075](https://www.ahajournals.org/doi/10.1161/jaha.116.003498)):
- Severe RHD at diagnosis: rapid progression, 50% require surgery within 2 years, 10% die within 6 years.
- Moderate RHD: mixed — roughly one-third each progress to severe, remain moderate, or regress to mild over 10 years.
- Mild RHD: most favorable — >60% remain mild at 10 years; ~10% become "inactive."

**Quality of life:** Chronic heart failure, activity limitation, recurrent hospitalization, anticoagulation burden (bleeding risk, INR monitoring), pregnancy risk, and the psychosocial burden of lifelong monthly intramuscular penicillin injections (frequently reported as painful, with poor long-term adherence) all substantially affect QoL, particularly in adolescents and young adults in endemic, resource-limited settings.

---

## 4. Genetic/Molecular Information

RHD/ARF is **not a monogenic Mendelian disease** — it is a complex, polygenic, infection-triggered autoimmune condition with strong immunogenetic (HLA) contribution.

**Causal/major-effect loci — HLA class II and III:**
- HLA-DR and HLA-DQ alleles (class II) show the most consistent associations across African, South Asian, and Latin American cohorts ([Nat Rev Cardiol genetics review](https://www.nature.com/articles/s41569-019-0258-2); [Uganda case-control, PMC3943278](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3943278/); [Brazil, PMID 2040052](https://pubmed.ncbi.nlm.nih.gov/2040052/)).
- A GWAS in South Asians (India/Fiji; 672 cases, 491 controls) replicated in a UK Biobank European follow-up (150 cases, 1,309 controls) identified a novel susceptibility signal in the **HLA class III region** (rs201026476; combined OR 1.81, 95% CI 1.51–2.18, P = 3.48×10⁻¹⁰) ([Sci Rep 2020, PMC7265443](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7265443/)).
- Earlier GWAS work implicated the **HLA-DQA1–HLA-DQB1** region and, notably, the **immunoglobulin heavy-chain locus (chromosome 14, including the IGHV4-61 gene segment)** — supporting a B-cell/antibody-response contribution to susceptibility, consistent with the molecular-mimicry model ([biorxiv/GWAS Aboriginal Australians](https://www.biorxiv.org/content/10.1101/188334.full.pdf)).

**Suggested HGNC genes for annotation:** `HLA-DRB1`, `HLA-DQA1`, `HLA-DQB1`, `IGHV4-61` (contributing locus). Curators should bind via HGNC where a stable symbol exists (HLA genes are commonly annotated at the allele/serotype level rather than single HGNC IDs; verify convention).

**Functional impact:** These are **susceptibility/modifier** alleles (not classic pathogenic variants) — appropriate `relationship_type` is `SUSCEPTIBILITY`, and inheritance is best modeled as **polygenic/complex** (HP:0010982-style, if adapting the dismech Inheritance slot) rather than monogenic Mendelian, given no single-gene causal variant explains most cases.

**Epigenetics:** No well-established disease-specific epigenetic signature has been robustly replicated; this remains an evidence gap.

**Chromosomal abnormalities:** None reported — RHD is not associated with aneuploidy or structural chromosomal rearrangement; it is a complex autoimmune trait.

**Molecular target of the autoimmune response (the "antigen" side):** cardiac myosin (α-myosin heavy chain), valve endothelial/interstitial proteins including **laminin, collagen IV, cardiac myosin, tropomyosin, keratin, and vimentin**, plus the **CAR (coxsackievirus-adenovirus receptor)** and **β1-adrenergic receptor (β1AR)** as proposed valve-endothelial/cardiomyocyte targets of cross-reactive antibody ([PMC4137453, "Rethinking Molecular Mimicry"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4137453/)). Suggested UniProt/HGNC anchors: `MYH6` (cardiac myosin heavy chain, alpha), `VIM` (vimentin), `LAMA2`/laminin family, `COL4A1` and related collagen IV genes, `ADRB1` (β1-adrenergic receptor).

---

## 5. Environmental Information

- **Infectious trigger:** *Streptococcus pyogenes* (Group A *Streptococcus*), primarily via pharyngeal infection; skin infection (impetigo) is an increasingly recognized alternative/contributing portal in some high-incidence tropical settings. NCBITaxon: `NCBITaxon:1314` (*Streptococcus pyogenes*).
- **Socioeconomic/environmental risk factors:** overcrowded housing, poverty, limited access to primary healthcare and diagnostic microbiology, and reduced access to secondary prophylaxis programs are the dominant modifiable environmental determinants — these explain most of the geographic and Indigenous-population disparity in disease burden (see §9) ([Far North Queensland temporospatial study, PLOS NTD](https://journals.plos.org/plosntds/article?id=10.1371%2Fjournal.pntd.0008990)).
- **Lifestyle factors:** No specific diet/exercise/substance-use risk modifiers are established beyond the crowding/transmission pathway above; adherence behavior to secondary prophylaxis is itself a major modifiable "environmental" determinant of RHD progression.
- ECTO/exposure-term candidates: exposure to overcrowded housing; exposure to *Streptococcus pyogenes* (a term for GAS mucosal/skin exposure).

---

## 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream):**

1. **GAS mucosal (pharyngeal ± skin) infection** in a genetically susceptible (HLA class II/III) host.
2. **Molecular mimicry / cross-reactive immune priming:** The GAS group A carbohydrate epitope (N-acetyl-glucosamine on a rhamnose backbone) and the α-helical coiled-coil **M protein** structurally mimic host cardiac and connective-tissue antigens — cardiac myosin, laminin, collagen IV, vimentin, tropomyosin, keratin — plus CAR and β1AR on valve endothelium/cardiomyocytes ([PMC4137453](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4137453/); [PMID 16455580](https://pubmed.ncbi.nlm.nih.gov/16455580/)).
3. **B-cell response:** cross-reactive antibody (initially IgM, later IgG) is produced against GAS carbohydrate/M-protein epitopes and binds valve endothelium, **up-regulating VCAM-1** and promoting inflammatory cell recruitment ([Frontiers 2025 pathogenesis review, PMC12018407](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12018407/)).
4. **CD4+ T-cell response:** CD4+ T lymphocytes, exhibiting a "degenerate" (cross-reactive/promiscuous) pattern of antigen recognition, infiltrate valve tissue and myocardium and are considered the prime effector cells of chronic valvular damage; Th1-skewed, IFN-γ-driven inflammation predominates.
5. **Acute valvulitis/carditis:** endothelial activation and immune-cell infiltration produce **Aschoff bodies** — granulomatous foci of central fibrinoid necrosis surrounded by lymphocytes, plasma cells, macrophages, and pathognomonic **Anitschkow cells** (activated macrophages with a distinctive "caterpillar"-like linear chromatin pattern) ([Wikipedia/Grokipedia histopathology summary](https://en.wikipedia.org/wiki/Anitschkow_cell); pathology reference [PEIR](https://peir.path.uab.edu/wiki/IPLab:Lab_9:ARF)).
6. **Chronic remodeling:** repeated/persistent inflammation drives **valve leaflet fibrosis, neovascularization (abnormal thick-walled vessels within normally avascular valve tissue), leaflet thickening, commissural fusion, and dystrophic calcification** — converting reversible acute valvulitis into fixed **stenosis and/or regurgitation**, predominantly mitral > aortic > tricuspid.
7. **Hemodynamic/organ-level consequences:** valve dysfunction → left atrial enlargement → atrial fibrillation and thrombus formation → stroke/systemic embolism; and/or → pulmonary venous congestion → pulmonary hypertension → right heart failure; and/or → ventricular volume/pressure overload → congestive heart failure.

**Cell types involved** (candidate CL terms — verify via OAK): CD4+ T lymphocyte (`CL:0000624`), Th1 cell (`CL:0000545`), B lymphocyte / plasma cell (`CL:0000236` / `CL:0000786`), macrophage (`CL:0000235`), activated/"Anitschkow" macrophage (no dedicated CL term — annotate as macrophage with a descriptive qualifier), valve endothelial cell (`CL:0000115` generic endothelial cell, or a valve-specific subtype if available), valve interstitial fibroblast (`CL:0000057` fibroblast).

**Biological processes** (candidate GO terms): antigen processing and presentation (`GO:0019882`), T-cell mediated cytotoxicity (`GO:0001913`), complement activation (`GO:0006956`), acute inflammatory response (`GO:0002526`), positive regulation of leukocyte cell-cell adhesion / VCAM-1-mediated adhesion (`GO:1903039`-family), fibrosis-related extracellular matrix remodeling processes (as used elsewhere in the KB's `fibrotic_response` module).

**Relationship to existing dismech mechanism modules:** RHD is a strong candidate to `conforms_to` the **`fibrotic_response`** module (chronic valvulitis → mesenchymal/valve interstitial cell activation → excessive ECM deposition → organ [valve] dysfunction), the **`cardiomyopathy_maladaptive_remodeling`** module if ventricular remodeling/heart failure nodes are curated, and **`cardiac_ion_channel_repolarization`** is *not* the right fit for the AF here (RHD-associated AF is structural/left-atrial-enlargement-driven, not a primary channelopathy) — model AF as a downstream structural consequence rather than conforming to that module. The granulomatous Aschoff-body lesion itself may be a candidate for an **"Xogenesis"**-style pathological-structure-formation node (a defined pathological granulomatous body, analogous to the `granuloma_formation` module's macrophage-fusion pattern, though Aschoff bodies are histologically and immunologically distinct from infectious/mycobacterial granulomas and a new/adapted anchor would be needed rather than direct conformance).

**Molecular profiling / omics:** RHD mechanistic omics data are comparatively sparse relative to other cardiovascular diseases; most mechanistic evidence derives from immunohistochemistry of excised valve/appendage tissue, serologic/antibody studies, and the Lewis-rat model transcriptome/histology (see §15) rather than large-scale human transcriptomic/proteomic atlases. This is a notable evidence gap relative to better-profiled cardiovascular conditions.

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** heart valves — **mitral valve** (most common and most severely affected; UBERON candidate: `UBERON:0002094` mitral valve or generic `UBERON:0002136`/verify), **aortic valve** (`UBERON:0002137`-family, verify), less commonly tricuspid valve, rarely pulmonary valve.
- **Secondary/associated in ARF (not RHD per se):** joints (synovium, `UBERON:0000980` synovial joint) in migratory polyarthritis; basal ganglia/caudate-putamen (`UBERON:0002420` basal ganglia region) in Sydenham chorea; skin/subcutaneous tissue in erythema marginatum and subcutaneous nodules; pharynx (`UBERON:0000165`) as the primary infection site.
- **Body systems:** cardiovascular (primary), musculoskeletal (ARF arthritis), nervous (ARF chorea), integumentary (ARF skin findings), and secondarily respiratory (pulmonary hypertension/congestion from left heart disease).

**Tissue/cell level:** valve leaflet fibrous layer, valve endothelium, myocardial interstitium (Aschoff bodies classically myocardial/subendocardial), pericardium (pericarditis in severe carditis). Cell populations: valve endothelial cells, valve interstitial fibroblasts, infiltrating CD4+ T cells, macrophages/Anitschkow cells, plasma cells.

**Subcellular:** no disease-defining subcellular organelle lesion (this is an extracellular-matrix/immune-infiltrate disease rather than an organellopathy); GO Cellular Component annotations would center on extracellular matrix (`GO:0031012`) and cell surface/plasma membrane VCAM-1 (`GO:0009986` cell surface) rather than intracellular compartments.

**Localization/laterality:** left-sided valves (mitral, then aortic) affected far more often and more severely than right-sided valves — a consistent, mechanistically notable asymmetry attributed to higher hemodynamic shear stress on the left side of the heart amplifying endothelial activation/antibody deposition.

---

## 8. Temporal Development

- **Onset:** ARF typically presents in **school-age children (5–14 years)**, 1–5 weeks after GAS pharyngitis (except Sydenham chorea, which can be delayed 1–8 months). Chronic RHD may not become clinically apparent (murmur, symptoms) until years to decades later; **latent RHD** (echocardiographically detectable, subclinical) is a recognized and common intermediate state, especially in endemic screening cohorts.
- **Progression pattern:** Variable and stage-dependent (see severity data in §3): mild disease is often stable/regressive; moderate disease shows a roughly even three-way split (progress/stable/regress) over a decade; severe disease at diagnosis progresses rapidly, with a high 2-year surgical intervention rate and appreciable 6-year mortality ([JAHA multi-state model, PMID 28255075](https://www.ahajournals.org/doi/10.1161/jaha.116.003498)).
- **Disease course:** classically **episodic-to-progressive** — each ARF recurrence adds incremental, cumulative valvular damage; disease is not typically "relapsing-remitting" in the neurological sense but rather step-wise worsening punctuated by inflammatory flares (ARF recurrences), against a background of gradually progressive valvular fibrosis/calcification even in inflammation-free intervals.
- **Remission:** acute inflammatory episodes (arthritis, fever, even carditis) can resolve completely, especially with anti-inflammatory treatment; however, once structural valve fibrosis/scarring has occurred it is **not reversible** — "regression" documented in mild latent RHD cohorts likely reflects resolution of reversible valvulitis/edema rather than true fibrotic reversal.
- **Critical intervention window:** primary prevention (antibiotic treatment of GAS pharyngitis within 9 days of symptom onset) reliably prevents the first ARF episode; secondary prophylaxis initiated promptly after a first ARF episode, and sustained for years, is the critical window for preventing the cumulative valvular damage that defines RHD.

---

## 9. Inheritance and Population

**Epidemiology (Global Burden of Disease 2021):**
- ~40.5 million people affected globally; ~306,000–373,000 deaths annually (~2% of all cardiovascular deaths) ([WHO](https://www.who.int/news-room/fact-sheets/detail/rheumatic-heart-disease); [GBD pediatric RHD 2021, PMC12293350](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12293350/)).
- ~3.85 million new RHD cases in 2021; global age-standardized **incidence rate rose** modestly from 55.84 to 66.76 per 100,000 (1990→2021), while age-standardized **death rate in children fell ~74%** and DALY rate fell from 117.22 to 41.56 per 100,000 over the same period — a "declining severity, persistent/rising incidence, widening inequality" pattern ([GBD pediatric analysis, PMC12293350](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12293350/)).
- Historical benchmark: 1990–2015 GBD estimated 319,400 RHD deaths globally in 2015 ([NEJM 2017, PMID 28834488](https://www.nejm.org/doi/full/10.1056/NEJMoa1603693)).
- Highest incidence in **children aged 0–14**, concentrated in low- and middle-income countries.

**Inheritance pattern:** **Multifactorial/polygenic**, infection-dependent — not a Mendelian single-gene disorder. HLA-associated susceptibility with modest individual-allele effect sizes (e.g., OR ~1.8 for the HLA class III GWAS hit), consistent with a complex trait requiring an environmental (GAS exposure) trigger. No described penetrance/expressivity framework analogous to monogenic disease; no genetic anticipation or germline mosaicism relevance; no described founder-effect variant, though population-specific HLA allele frequencies likely contribute to regional prevalence differences.

**Population demographics and geographic distribution:**
- **Highest global rates:** sub-Saharan Africa, followed by **Aboriginal and Torres Strait Islander Australians**, **Māori and Pacific Islanders**, and South Asia.
- **Australia (Indigenous disparity):** First Nations Australians are **≥60 times** more likely to experience ARF/RHD than non-Indigenous Australians; the Northern Territory has one of the highest documented RHD prevalence rates worldwide (~3,005 per 100,000 Indigenous residents). Indigenous communities account for **78% of all RHD cases and 92% of all ARF cases** in Australia (2022 data). Mortality rate ratio (Indigenous vs. non-Indigenous), 2013–2017: **15.9** ([Excess Deaths, PMC10756360](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10756360/); [Indigenous HPF](https://www.indigenoushpf.gov.au/measures/1-06-rheumatic-fever-rheumatic-heart-disease)). In Far North Queensland, RHD incidence rose from 4.7 to 49.4 per 100,000/year (1997→2017); 2017 prevalence was 12/1000 Indigenous vs. 2/1000 non-Indigenous ([PLOS NTD](https://journals.plos.org/plosntds/article?id=10.1371%2Fjournal.pntd.0008990)).
- **Māori/Pacific Islander (NZ):** cumulative ARF hospitalization risk by age 13 is approximately **1 in 150**.
- **Sex ratio:** GBD 2021 data indicate women represent just over half of global RHD cases; some regional/age-specific variation exists (e.g., possible sex differences in Sydenham chorea susceptibility) but no large, uniform sex skew is established for ARF susceptibility itself.
- **Consanguinity/carrier frequency:** not applicable in the classic Mendelian sense (complex trait); HLA allele-frequency variation across ancestries is the relevant population-genetic parameter rather than a carrier-frequency concept.

---

## 10. Diagnostics

**Clinical/serologic tests:**
- **Evidence of preceding GAS infection:** throat culture/rapid antigen test (acute infection); **anti-streptolysin O (ASOT)** — sensitivity ~80% (adult cutoff >240 Todd units, child >320); **anti-DNase B** — sensitivity ~90%, complementary to ASOT (paired/sequential titers recommended for optimal sensitivity) ([search summary of Frontiers 2021, "Holy Grail" review](https://www.frontiersin.org/journals/cardiovascular-medicine/articles/10.3389/fcvm.2021.674805/full)).
- **Inflammatory markers:** ESR and CRP — elevated as ARF minor criteria; positively correlate with ASOT; may help monitor transition from acute carditis toward chronic RHD.
- **Electrocardiography:** prolonged PR interval (minor Jones criterion); atrial fibrillation detection in chronic disease.
- **Echocardiography (the central chronic-disease diagnostic modality):** 2D + continuous-wave + color-Doppler echo per the **2012 World Heart Federation (WHF) criteria**, which classify findings into **"definite RHD"** (4 subcategories), **"borderline RHD"** (3 subcategories), and **"normal"**, with age-based modifications for those >20 years — designed to standardize detection of latent/subclinical disease for enrollment into secondary-prophylaxis programs ([Reményi et al., Nat Rev Cardiol 2012, PMID 22371105](https://www.nature.com/articles/nrcardio.2012.7); [WHF PDF](https://www.world-heart-federation.org/wp-content/uploads/2017/05/WHFechoCriteriaForDxRHDnrcardio.2012.7.pdf)). Simplified screening criteria have since been validated to predict progression of latent disease ([Circ Cardiovasc Imaging, search summary](https://www.ahajournals.org/doi/10.1161/CIRCIMAGING.118.007928)).
- **Histopathology (rarely obtained clinically; mainly surgical/autopsy specimens):** Aschoff bodies and Anitschkow cells in active carditis; chronic valve leaflet fibrosis, neovascularization, and dystrophic calcification in end-stage disease.

**Genetic testing:** RHD is **not currently subject to clinical genetic testing** — there is no validated single-gene, panel, or polygenic-risk-score test used in patient management; genetic association findings (HLA, IGH locus) remain research-stage.

**Clinical diagnostic criteria:** **Revised (2015) Jones criteria**, risk-stratified by population ARF incidence, incorporating echocardiography and presumptive-ARF categories for isolated chorea/indolent carditis/recurrence ([Gewitz et al. 2015, PMID 25908771](https://www.ahajournals.org/doi/10.1161/cir.0000000000000205)). Differential diagnosis of ARF includes reactive arthritis, septic arthritis, juvenile idiopathic arthritis, systemic lupus erythematosus, viral myocarditis/pericarditis, infective endocarditis, and (for chorea) other movement disorders (tic disorders, Huntington disease in adults, drug-induced chorea).

**Screening:** Active echocardiographic screening programs in endemic/high-risk populations (e.g., Australia, Pacific, sub-Saharan Africa) using WHF criteria to detect latent RHD before clinical presentation, enabling early enrollment in secondary prophylaxis — though the clinical/cost-effectiveness value of screening asymptomatic borderline disease remains an area of active debate ([Nat Rev Cardiol WHF criteria paper](https://www.nature.com/articles/nrcardio.2012.7); [Global Heart 2023 review of WHF criteria performance](https://globalheartjournal.com/articles/10.5334/gh.1327)).

---

## 11. Outcome/Prognosis

- **Mortality:** GBD 2021 attributes ~306,000–373,000 deaths/year to RHD globally; nearly 2% of all cardiovascular deaths. Pediatric age-standardized RHD death rate fell ~74% from 1990–2021, reflecting improved secondary prophylaxis and surgical access in many settings, but absolute burden remains high in under-resourced regions.
- **Survival by severity at diagnosis** ([JAHA 2017 multi-state model](https://www.ahajournals.org/doi/10.1161/jaha.116.003498)):
  - Severe RHD: 50% require surgery within 2 years; 10% die within 6 years.
  - Moderate RHD: ~1/3 progress to severe, ~1/3 stable, ~1/3 regress to mild over 10 years.
  - Mild RHD: >60% remain mild at 10 years; ~10% become inactive.
- **Disability burden:** RHD causes the **highest DALYs of any cardiovascular disease among 10–14-year-olds** globally — reflecting its unique concentration in children/young people relative to other, older-onset cardiovascular conditions.
- **Complications driving morbidity:** progressive heart failure, atrial fibrillation, cardioembolic stroke, infective endocarditis, pulmonary hypertension, and — in higher-resource settings — the risks/burdens of anticoagulation and prosthetic valve surgery (thromboembolism ~11% cumulative incidence over 25 years post-mechanical mitral valve replacement in one cohort; rising rates of intracranial hemorrhage, perivalvular leak, and infective endocarditis over time on mechanical valves — search summary of valve-surgery outcome literature).
- **Prognostic factors:** severity of carditis at first presentation is the single strongest prognostic determinant; timely secondary prophylaxis adherence, access to echocardiographic monitoring, and access to timely valve surgery in low-resource settings are the major modifiable prognostic levers.

---

## 12. Treatment

### Pharmacotherapy — acute rheumatic fever

- **Aspirin** (CHEBI:15365) — first-line anti-inflammatory for arthritis/mild carditis; 50–60 mg/kg/day, tapered over 1–2 weeks after symptom resolution.
- **NSAIDs** (e.g., naproxen, CHEBI:7476) — endorsed alternative to aspirin with comparable efficacy and fewer GI side effects in comparative pediatric trials.
- **Corticosteroids** (e.g., prednisone/prednisolone, CHEBI:8382) — reserved for moderate-to-severe carditis; a Cochrane systematic review found **no robust evidence that anti-inflammatory treatment (steroids or aspirin) prevents or reduces long-term cardiac valve damage**, despite symptomatic benefit ([Cilliers et al., Cochrane 2015](https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.CD003176.pub3/full)) — an important evidence caveat for curation (treat as symptomatic, not disease-modifying for valve outcome).

### Antibiotic therapy (both eradication and secondary prophylaxis)

- **Benzathine penicillin G (BPG)**, CHEBI (verify exact CURIE for the benzathine salt) — the cornerstone of both (a) eradication of the inciting GAS infection and (b) **secondary prophylaxis**: standard dosing is 1.2 million units (900 mg) deep IM every 3–4 weeks for a **minimum of 5 years**, often extended to age 21 or 10 years post-ARF episode (regimen duration guidance varies by carditis severity per AHA/WHO guidance) ([AAC 2023 phase 1 PK study, PMC10720493](https://pmc.ncbi.nlm.nih.gov/articles/PMC10720493/)).
- **Adherence challenge:** dosing frequency and injection pain drive suboptimal real-world adherence; a **subcutaneous high-dose BPG infusion** formulation is under phase 1 investigation to allow less-frequent dosing ([PMC10720493](https://pmc.ncbi.nlm.nih.gov/articles/PMC10720493/)).
- **Primary prevention:** oral penicillin V or single-dose IM BPG for confirmed/probable GAS pharyngitis, started within 9 days of symptom onset, reduces ARF attack rate by **~70%** ([meta-analysis, PMID 15927077](https://pmc.ncbi.nlm.nih.gov/articles/PMC1164408/)); macrolides/cephalosporins are penicillin-allergy alternatives.
- **Penicillin allergy in severe RHD** is a specific clinical challenge addressed by a dedicated AHA presidential advisory on desensitization/testing strategies ([JAHA 2022](https://www.ahajournals.org/doi/10.1161/JAHA.121.024517)).

### Anticoagulation (chronic RHD with AF or mechanical valve)

- **Warfarin** (CHEBI:10033), target INR 2–3, remains standard for RHD-associated atrial fibrillation — a landmark trial (INVICTUS) established warfarin's superiority over DOACs specifically in RHD-associated AF, a population historically excluded from DOAC trials ([NEJM editorial, PMID/DOI 10.1056/NEJMe2210187](https://www.nejm.org/doi/full/10.1056/NEJMe2210187)).
- **Pregnancy-specific management:** warfarin crosses the placenta and risks fetal warfarin syndrome (nasal hypoplasia, skeletal abnormalities) in the first trimester; low-molecular-weight heparin (LMWH, dose-adjusted to anti-Xa 0.5–1.0 U/mL) or unfractionated heparin is preferred peripartum, with heparin bridging around delivery and resumption of warfarin postpartum.

### Interventional/surgical

- **Percutaneous balloon mitral valvuloplasty (PBMV)** — preferred for suitable (non-calcified, non-regurgitant) rheumatic mitral stenosis; less invasive, shorter procedure, lower cost than surgery, with comparable mid-term outcomes in appropriately selected patients; ~20% develop new/worsened mitral regurgitation post-procedure.
- **Mitral valve repair** vs. **replacement** — repair shows greater hemodynamic improvement and short-term clinical efficacy where anatomically feasible; replacement (mechanical or bioprosthetic) is required for more advanced/calcified/regurgitant disease. Mechanical valve replacement carries long-term thromboembolism (~11% cumulative at 25 years in one cohort), intracranial hemorrhage, perivalvular leak, and endocarditis risk requiring lifelong anticoagulation.
- NCIT candidate treatment terms (verify exact IDs via OAK): `NCIT:C15986` Pharmacotherapy (generic anchor for aspirin/NSAID/steroid/penicillin/warfarin, paired with `therapeutic_agent`); `NCIT:C15329` Surgical Procedure (mitral/aortic valve repair or replacement); a balloon-valvuloplasty-specific NCIT term should be looked up directly (not confidently identified in this pass).

### Prevention of complications / supportive care
Standard heart-failure pharmacotherapy (diuretics, ACE inhibitors/ARBs, beta-blockers) is used symptomatically for RHD-related heart failure, following general heart-failure guidelines rather than RHD-specific evidence — these represent generic HF pharmacotherapy rather than RHD-mechanism-targeted treatment and should be annotated as `treatment_term: NCIT:C15986 Pharmacotherapy` with the appropriate agent, not `target_mechanisms` on the autoimmune valvulitis pathway itself.

### Experimental
No RHD-specific advanced therapeutics (gene therapy, cell therapy, targeted immunotherapy) are in clinical development at this time; the major "experimental" frontier is **primary prevention via GAS vaccine** (§13) rather than disease-modifying treatment of established RHD.

---

## 13. Prevention

**Primary prevention:** prompt antibiotic treatment (penicillin) of confirmed/probable GAS pharyngitis — ~70% reduction in ARF attack rate ([PMID 15927077](https://pmc.ncbi.nlm.nih.gov/articles/PMC1164408/); [AHA 2009 statement](https://www.ahajournals.org/doi/10.1161/circulationaha.109.191959)). Population-level "sore throat management" programs (school-based throat-swab/treat programs) are a core public-health strategy in endemic regions.

**Secondary prevention:** regular BPG secondary prophylaxis after a confirmed ARF episode, sustained for years (minimum 5, often to age 21+ or longer for those with carditis/RHD) — the single most impactful intervention for preventing RHD progression once ARF has occurred.

**Tertiary prevention:** infective-endocarditis prophylaxis considerations for high-risk dental/surgical procedures in patients with damaged valves (per current, more restrictive endocarditis-prophylaxis guidelines); anticoagulation to prevent thromboembolic stroke in RHD-associated AF; timely surgical referral to prevent irreversible heart-failure decompensation.

**Vaccination (the major prevention frontier):** **No licensed GAS vaccine currently exists.** Active development includes:
- **Carbohydrate-based (L-rhamnose/group A carbohydrate backbone)** candidates designed to raise protective IgG without inducing cross-reactive (cardiac-mimicking) antibody — directly addressing the historical safety concern that a poorly designed GAS vaccine could itself trigger molecular-mimicry-driven carditis ([F1000Research/PMC11829149](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11829149/); [PMID 39959434](https://pubmed.ncbi.nlm.nih.gov/39959434/)).
- **Peptide-based** candidates — phase 1 RCT ongoing/recently completed (est. completion March 2025) ([Trials journal, 2024](https://trialsjournal.biomedcentral.com/articles/10.1186/s13063-024-08634-4)).
- **IVI universal conjugate vaccine program** — proof-of-concept study launched 2024, running through 2027, aiming to select an optimal conjugation platform via animal immunogenicity/efficacy studies ([IVI](https://www.ivi.int/what-we-do/research-areas/group-a-strep/)).
- **WHO R&D Technology Roadmap / Preferred Product Characteristics** for GAS vaccines formally guides the development pipeline ([Clin Infect Dis 2019, PMID 30624673](https://academic.oup.com/cid/article/69/5/877/5280612)).
- A dedicated **cardiac-safety monitoring framework** (endorsed by SAVAC/ASAVI) has been developed specifically for early-phase GAS vaccine trials, given the historical precedent of vaccine-associated ARF risk, standardizing echocardiographic + clinical cardiac surveillance ([PMID 40450801](https://pubmed.ncbi.nlm.nih.gov/40450801/)).

**Public health/behavioral interventions:** overcrowding reduction, health-system strengthening for GAS pharyngitis diagnosis/treatment access, and community-based ARF/RHD control programs (notably in Aboriginal/Torres Strait Islander Australian communities) — a recent systematic review catalogued Australian RHD-elimination prevention programs and their implementation gaps ([Lowitja Journal 2024](https://www.lowitjajournal.org.au/article/S2949-8406(24)00031-7/fulltext)).

**Genetic counseling / risk stratification:** not applicable in the classic monogenic sense; population/community-level risk stratification (Indigenous status, remoteness, prior ARF history) drives targeted screening and prophylaxis-program enrollment rather than individual genetic counseling.

---

## 14. Other Species / Natural Disease

RHD is, for practical purposes, a **human-specific disease** — *S. pyogenes* is essentially a human-adapted pathogen, and there is no well-documented naturally occurring veterinary/wildlife analog of GAS-triggered post-infectious autoimmune carditis. No OMIA (animal Mendelian disease) entry or established veterinary RHD analog was identified in this search. This is a notable contrast to many other cardiovascular/autoimmune diseases in the dismech KB that have companion-animal natural-disease correlates — for RHD, the "other species" content is essentially limited to laboratory-induced models (§15) rather than spontaneous natural disease. No zoonotic transmission concern applies (GAS pharyngitis/ARF pathogenesis is human-host-restricted in practice, notwithstanding rare GAS colonization reports in other mammals).

---

## 15. Model Organisms

**Lewis rat — the primary, best-validated model** ([Animal Models review, PMC4220098 / PMID 25414841](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4220098/); [AJP epitope-mapping study](https://ajp.amjpathol.org/article/S0002-9440(10)64373-8/fulltext)):
- Female Lewis rats (8–12 weeks) immunized subcutaneously with recombinant GAS **M5 protein** (or M5 peptide) in complete Freund's adjuvant, with *Bordetella pertussis* as additional adjuvant and a day-7 booster, develop **autoimmune valvulitis** recapitulating human histopathology.
- Outcomes: **75% develop rheumatic-like myocarditis**, **62.5% develop chronic valvulitis** by 24 weeks post-immunization, with cross-reactive heart-tissue antibodies and T cells, and histological findings including acute damage progressing to fibrosis and vascular neogenesis — closely mirroring the human chronic valve lesion.
- **Cardiac myosin immunization** (rather than M protein) also induces valvulitis in Lewis rats, with the pathogenic epitopes mapped to the myosin **rod region**, supporting the molecular-mimicry model directly.
- An alternative **formalin-killed streptococci** induction protocol has also been reported to produce chronic rheumatic valvulitis (PMID referenced via search: "An animal model of chronic rheumatic valvulitis induced by formalin-killed streptococci").
- A **2025 Nature Reviews Cardiology** commentary describes a "transformative preclinical model" development, suggesting active ongoing refinement of RHD animal modeling as of this reporting period (title only identified; full mechanistic detail not retrieved in this pass — recommend direct follow-up read: [Nat Rev Cardiol 2025](https://www.nature.com/articles/s41569-025-01203-5)).

**Model limitations:** Rodent models require artificial immunization (adjuvant-driven) rather than natural GAS mucosal infection, so they model the **downstream autoimmune effector phase** well but do not fully recapitulate the natural infection-to-autoimmunity transition, repeated-exposure/recurrence biology, or the human HLA-restricted antigen-presentation context (rat MHC, not human HLA, governs susceptibility in these models) — a genuine human-model-fidelity gap worth flagging explicitly if curated (candidate for a `HUMAN_MODEL_MISMATCH` discussion given rat MHC vs. human HLA-restricted epitope presentation, and adjuvant-driven vs. natural-infection induction).

**Research applications:** Lewis rat valvulitis models are used to dissect molecular-mimicry epitope specificity (M-protein vs. myosin vs. other candidate antigens), test candidate GAS vaccine constructs for cardiac cross-reactivity/safety (a major use case given the vaccine-safety concerns noted in §13), and study T-cell/antibody effector mechanisms of valve damage.

**Other model systems:** No robust zebrafish, *Drosophila*, *C. elegans*, or iPSC-organoid RHD model was identified in this search — the field remains centered on the Lewis rat immunization paradigm, with in vitro human valve endothelial/interstitial cell cross-reactivity assays as a complementary (non-whole-organism) system for mechanism dissection.

---

## Summary Table — Suggested Ontology Term Anchors (verify all before curation)

| Domain | Suggested term | Confidence |
|---|---|---|
| Organism/pathogen | NCBITaxon:1314 (*Streptococcus pyogenes*) | High |
| Phenotype | HP:0001653 (mitral regurgitation), HP:0001718 (mitral stenosis), HP:0001659 (aortic regurgitation), HP:0001650 (aortic valve stenosis), HP:0002072 (chorea), HP:0001369 (arthritis), HP:0001482 (subcutaneous nodule), HP:0005110 (atrial fibrillation), HP:0001635 (heart failure) | Moderate–high; verify labels via OAK |
| Anatomy | UBERON heart valve / mitral valve / aortic valve terms, UBERON:0000165 (pharynx), UBERON:0000980 (synovial joint) | Moderate; verify exact CURIEs |
| Cell types | CL:0000624 (CD4+ T cell), CL:0000235 (macrophage), CL:0000786 (plasma cell), CL:0000057 (fibroblast) | Moderate |
| Genes | HLA-DRB1, HLA-DQA1, HLA-DQB1, IGHV4-61, MYH6, VIM, ADRB1 | Moderate; HLA CURIE convention needs confirmation |
| Chemicals/drugs | CHEBI:15365 (aspirin), CHEBI:7476 (naproxen), CHEBI:8382 (prednisone), CHEBI:10033 (warfarin) | High for common drugs; verify benzathine penicillin G CURIE |
| Treatment action | NCIT:C15986 (Pharmacotherapy), NCIT:C15329 (Surgical Procedure) | High for generic anchors; verify any procedure-specific NCIT code |
| ICD-10-CM | I00–I02 (acute rheumatic fever), I05–I09 (chronic RHD) | High |

---

## Sources

- [WHO — Rheumatic heart disease fact sheet](https://www.who.int/news-room/fact-sheets/detail/rheumatic-heart-disease)
- [World Heart Federation — Rheumatic Heart Disease](https://world-heart-federation.org/heart-health/rheumatic-heart-disease/)
- [StatPearls — Rheumatic Heart Disease](https://www.ncbi.nlm.nih.gov/books/NBK538286/)
- [StatPearls — Acute Rheumatic Fever](https://www.ncbi.nlm.nih.gov/books/NBK594238/)
- [Standardization of Epidemiological Surveillance of RHD, PMC9474940](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9474940/)
- [Molecular mimicry in the autoimmune pathogenesis of RHD — PubMed 16455580](https://pubmed.ncbi.nlm.nih.gov/16455580/)
- [Rethinking Molecular Mimicry in RHD — PMC4137453](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4137453/)
- [A mini review of the pathogenesis of ARF/RHD — PMC12018407](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12018407/)
- [Genome-wide analysis of genetic risk factors for RHD in Aboriginal Australians — bioRxiv](https://www.biorxiv.org/content/10.1101/188334.full.pdf)
- [Revision of the Jones Criteria — Circulation 2015, PMID 25908771](https://www.ahajournals.org/doi/10.1161/cir.0000000000000205)
- [Specificity of the Modified Jones Criteria — Pediatrics 2024](https://publications.aap.org/pediatrics/article/153/3/e2023062624/196623/Specificity-of-the-Modified-Jones-Criteria)
- [HLA Locus and RHD Susceptibility in South Asians and Europeans — PMC7265443](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7265443/)
- [Genetics of rheumatic fever and RHD — Nature Reviews Cardiology](https://www.nature.com/articles/s41569-019-0258-2)
- [RHD in Uganda: MHC class II HLA-DR alleles — PMC3943278](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3943278/)
- [HLA class II antigens with rheumatic fever/RHD in Brazil — PMID 2040052](https://pubmed.ncbi.nlm.nih.gov/2040052/)
- [Global Burden of Pediatric RHD 1990–2021 — PMC12293350](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12293350/)
- [Global, Regional, National Burden of RHD 1990–2015 — NEJM, PMID 28834488](https://www.nejm.org/doi/full/10.1056/NEJMoa1603693)
- [Temporal Trends RHD South Asia GBD — PMC11212786](https://pmc.ncbi.nlm.nih.gov/articles/PMC11212786/)
- [Changes in burden of RHD children/youth 1990–2021 — PMC12241001](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12241001/)
- [Subcutaneous BPG phase 1 PK study — PMC10720493](https://pmc.ncbi.nlm.nih.gov/articles/PMC10720493/)
- [Penicillin Reactions in Severe RHD — AHA Presidential Advisory, JAHA](https://www.ahajournals.org/doi/10.1161/JAHA.121.024517)
- [Repair vs. replacement rheumatic mitral valve disease — PMC12394501](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12394501/)
- [Surgical repair vs. PBMV propensity-matched — PMC7711429](https://pmc.ncbi.nlm.nih.gov/articles/PMC7711429/)
- [Clinical outcomes mitral repair/replacement meta-analysis — PMC7940942](https://pmc.ncbi.nlm.nih.gov/articles/PMC7940942/)
- [World Heart Federation echo criteria — Nat Rev Cardiol, PMID 22371105](https://www.nature.com/articles/nrcardio.2012.7)
- [Simplified echo screening criteria for latent RHD — Circ Cardiovasc Imaging](https://www.ahajournals.org/doi/10.1161/CIRCIMAGING.118.007928)
- [Echocardiographic Diagnosis of RHD: WHF criteria performance 2012–2023 — Global Heart](https://globalheartjournal.com/articles/10.5334/gh.1327)
- [GAS Vaccine — IVI research](https://www.ivi.int/what-we-do/research-areas/group-a-strep/)
- [L-Rhamnose GAS vaccine — PMID 39959434](https://pubmed.ncbi.nlm.nih.gov/39959434/)
- [Update on development of GAS vaccines — PMC10502077](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10502077/)
- [Phase 1 peptide-based GAS vaccine RCT — Trials 2024](https://trialsjournal.biomedcentral.com/articles/10.1186/s13063-024-08634-4)
- [WHO GAS Vaccine R&D Roadmap — Clin Infect Dis, PMID 30624673](https://academic.oup.com/cid/article/69/5/877/5280612)
- [Cardiac monitoring safety framework for GAS vaccine trials — PMID 40450801](https://pubmed.ncbi.nlm.nih.gov/40450801/)
- [Animal models to investigate pathogenesis of RHD — PMID 25414841 / PMC4220098](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4220098/)
- [Induction of myocarditis/valvulitis in Lewis rats by cardiac myosin epitopes — AJP](https://ajp.amjpathol.org/article/S0002-9440(10)64373-8/fulltext)
- [Requirements for a robust ARF/RHD animal model — PMC8131511](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8131511/)
- [A transformative preclinical model of RHD — Nat Rev Cardiol 2025](https://www.nature.com/articles/s41569-025-01203-5)
- [Sydenham chorea — StatPearls/MedLink summary](https://www.ncbi.nlm.nih.gov/books/NBK594238/)
- [CDC Clinical Guidance for Acute Rheumatic Fever](https://www.cdc.gov/group-a-strep/hcp/clinical-guidance/acute-rheumatic-fever.html)
- [Erythema marginatum — DermNet NZ](https://dermnetnz.org/topics/rheumatic-fever)
- [Aschoff cell — Wikipedia](https://en.wikipedia.org/wiki/Aschoff_cell)
- [Anitschkow cell — Wikipedia](https://en.wikipedia.org/wiki/Anitschkow_cell)
- [Aschoff bodies granulomatous lesions of histiocytic origin — PMID 3070554](https://pubmed.ncbi.nlm.nih.gov/3070554/)
- [Disparity in Mortality from RHD in Indigenous Australians — JAHA](https://www.ahajournals.org/doi/10.1161/JAHA.114.001282)
- [Ending RHD in Aboriginal/Torres Strait Islander communities — Lowitja Journal 2024](https://www.lowitjajournal.org.au/article/S2949-8406(24)00031-7/fulltext)
- [Temporospatial epidemiology RHD Far North Queensland — PLOS NTD](https://journals.plos.org/plosntds/article?id=10.1371%2Fjournal.pntd.0008990)
- [Contemporary Incidence and Prevalence RHD Australia Linked Data — JAHA](https://www.ahajournals.org/doi/10.1161/JAHA.120.016851)
- [AIHW Indigenous HPF — ARF and RHD measure](https://www.indigenoushpf.gov.au/measures/1-06-rheumatic-fever-rheumatic-heart-disease)
- [Excess Deaths Associated with RHD, Australia 2013–2017 — PMC10756360](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10756360/)
- [Anticoagulation for mechanical heart valves in pregnancy — PMC9803450](https://pmc.ncbi.nlm.nih.gov/articles/PMC9803450/)
- [Safety/efficacy LMWH pregnant women RHD/valve replacement — PMC9001812](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9001812/)
- [Anticoagulation in Atrial Fibrillation and RHD — NEJM editorial](https://www.nejm.org/doi/full/10.1056/NEJMe2210187)
- [ICD-10-CM codes I05–I09 — icd10data.com](https://www.icd10data.com/ICD10CM/Codes/I00-I99/I05-I09)
- [ICD-10-CM I01 rheumatic fever with heart involvement — icd10data.com](https://www.icd10data.com/ICD10CM/Codes/I00-I99/I00-I02/I01-)
- [RHD Severity, Progression and Outcomes: Multi-State Model — JAHA, PMID 28255075](https://www.ahajournals.org/doi/10.1161/jaha.116.003498)
- [Natural history of latent RHD 5-year follow-up — PMC4759741](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4759741/)
- [Long-term outcomes following RHD diagnosis in Australia — Eur Heart J Open](https://academic.oup.com/ehjopen/article/1/3/oeab035/6423987)
- [Anti-inflammatory treatment for carditis in ARF — Cochrane, Cilliers 2015](https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.CD003176.pub3/full)
- [Prescribing for people with ARF — PMC5407997](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5407997/)
- [Antibiotics for primary prevention of ARF — meta-analysis, PMID 15927077](https://pmc.ncbi.nlm.nih.gov/articles/PMC1164408/)
- [AHA Guidelines Prevention of Rheumatic Fever and Streptococcal Pharyngitis — Circulation](https://www.ahajournals.org/doi/10.1161/circulationaha.109.191959)
- [Mondo Disease Ontology](https://mondo.monarchinitiative.org/)
- [Serum ASO antibodies role in rheumatic disease evaluation](https://www.researchgate.net/publication/221823395_Serum_levels_of_anti-streptolysin_O_antibodies_Their_role_in_evaluating_rheumatic_diseases)
- [In Search of the Holy Grail: A Specific Diagnostic Test for Rheumatic Fever — PMC8160110](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8160110/)