---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-27T23:16:24.461080'
end_time: '2026-08-27T23:22:12.995495'
duration_seconds: 348.53
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Immunodeficiency 65 (IRF9 Deficiency)
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
  web_search_requests: 24
  num_turns: 32
  total_cost_usd: 1.6273076
  session_id: 2df13fb4-9115-50fa-aa7c-75f1d91c874a
  stop_reason: end_turn
  assistant_text_blocks: 3
citation_count: 18
reference_validation:
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 8
  on_topic: 4
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Immunodeficiency 65 (IRF9 Deficiency)
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Immunodeficiency 65 (IRF9 Deficiency)** covering all of the
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

I'll research Immunodeficiency 65 (IRF9 Deficiency) using web search and fetch tools, then compile a comprehensive report.

I have sufficient sourced material now to compile a comprehensive report.

# Immunodeficiency 65 (IRF9 Deficiency): Comprehensive Research Report

## 1. Disease Information

**Overview.** Immunodeficiency 65 (IMD65), also called "IRF9 deficiency" or "primary immunodeficiency with predisposition to severe viral infection," is an autosomal recessive inborn error of immunity (IEI) caused by biallelic loss-of-function variants in *IRF9*. It disrupts the interferon-stimulated gene factor 3 (ISGF3) transcription-factor complex, crippling the cellular response to type I (IFN-α/β) and type III (IFN-λ) interferons and leaving affected children susceptible to severe, sometimes life-threatening, viral infections from early life (OMIM #618648) [omim.org/entry/618648].

**Key identifiers:**
- **OMIM disease:** #618648 (IMMUNODEFICIENCY 65, SUSCEPTIBILITY TO VIRAL INFECTIONS; IMD65)
- **OMIM gene:** *147574 (INTERFERON REGULATORY FACTOR 9; IRF9)
- **Gene location:** Chromosome 14q12 (9 exons; exons 2–9 protein-coding)
- **Inheritance:** Autosomal recessive
- **Related but distinct entries:** IMD51 (IRF7 deficiency, OMIM #613953) and IMD62 (STAT2 deficiency, OMIM #618459) — both also disrupt ISGF3-dependent signaling and share overlapping phenotypes.

**Synonyms:** IRF9 deficiency; ISGF3γ (p48) deficiency; primary immunodeficiency with predisposition to severe viral infection.

**Data provenance.** Clinical knowledge of IMD65 is derived almost entirely from **individual patient case reports** (at most two or three unrelated families/kindreds published to date), not from a large aggregated disease cohort — this is an ultra-rare monogenic IEI, and virtually every published clinical detail traces back to primary case reports from the Casanova/Zhang laboratories (Rockefeller/Imagine Institute) and UK/Newcastle groups studying inborn errors of type I IFN immunity.

Sources: [OMIM #618648](https://www.omim.org/entry/618648) · [OMIM *147574](https://omim.org/entry/147574) · [GeneCards IRF9](https://www.genecards.org/cgi-bin/carddisp.pl?gene=IRF9)

---

## 2. Etiology

**Disease-causal factor:** Purely genetic — biallelic (homozygous or compound heterozygous) loss-of-function variants in *IRF9* that abolish or severely impair ISGF3 complex assembly.

**Genetic risk factors:**
- Homozygous or compound heterozygous null/hypomorphic *IRF9* alleles.
- Consanguinity is a recognized risk factor: the second reported family (two affected siblings) arose in a consanguineous kindred (identified through gene-panel sequencing) [Duncan/Bucciol et al., *JACI* 2022].

**Reported causal variants:**
| Patient/family | Variant | Consequence | Zygosity |
|---|---|---|---|
| Index case (Hernandez et al. 2018, *JEM*) | c.991G>A (last nucleotide of exon 7), possible p.Asp331Asn | Predicted splice-site alteration ± missense | Homozygous |
| Two siblings (Duncan et al. 2022, *JACI*) | c.577+1G>T | Splice-donor loss → exon 5 skipping → premature stop codon | Homozygous (consanguineous family) |

ClinVar entries document both variants under "Immunodeficiency 65, susceptibility to viral infections" (RCV000855434 for c.577+1G>T; RCV000855435 for c.991G>A / p.Asp331Asn).

**Environmental/triggering factors are not causal but are disease-revealing:** because the defect is in an antiviral pathway, the phenotype is essentially unmasked only upon viral challenge — influenza A virus, respiratory syncytial virus (RSV), parainfluenza virus, adenovirus, varicella-zoster virus (VZV, including vaccine-strain), HSV-1, and SARS-CoV-2 have all precipitated severe disease episodes in reported patients.

**Protective factors:** No genetic protective variants are described (the gene is essentially haploinsufficiency-tolerant but complete biallelic loss is deleterious). Prophylactic immunoglobulin (containing neutralizing antibodies from IFN-competent donors) and, in the COVID-19 case, exogenous SARS-CoV-2 neutralizing monoclonal antibodies were protective by bypassing the defective interferon-dependent antiviral pathway entirely (see Treatment).

**Gene-environment interaction:** The defect is a pure loss-of-function in the host antiviral signaling axis; interaction is essentially "genotype defines penetrance of specific viral phenotypes" — e.g., live-attenuated viral vaccines (yellow fever 17D, VZV, MMR) act as the "environmental trigger" that a competent ISGF3 pathway would normally control, but in IRF9-deficient individuals cause vaccine-strain disseminated disease.

Sources: [Hernandez et al. 2018, JEM 215(10):2567–2585](https://rupress.org/jem/article/215/10/2567/120233/) · [ClinVar RCV000855434](https://www.ncbi.nlm.nih.gov/clinvar/RCV000855434/) · [ClinVar RCV000855435](https://www.ncbi.nlm.nih.gov/clinvar/RCV000855435/)

---

## 3. Phenotypes

Reported phenotypes span three domains — infectious, vaccine-associated, and inflammatory/immune-dysregulation.

### Infectious phenotypes
| Phenotype | Onset | Severity/course | Suggested HPO term |
|---|---|---|---|
| Life-threatening influenza pneumonitis | Early childhood (age 2 in index case) | Severe, ICU/mechanical ventilation | HP:0011947 (Respiratory tract infection), consider HP:0002090 (Pneumonia) |
| Critical COVID-19 pneumonia risk | Any age | High viral load, viremia (documented Ct 16.5 nasal load) | HP:0002090 |
| RSV, parainfluenza, adenovirus infections | Infancy | Recurrent, severe; "unrestricted viral replication" shown in vitro | HP:0011947 |
| Recurrent bronchiolitis | Infancy | Recurrent | HP:0011950 (Bronchiolitis) |
| Bronchiectasis (sequela) | Later childhood | Progressive/structural lung damage | HP:0002110 (Bronchiectasis) |
| Disseminated post-vaccination VZV | Post-vaccination | Severe, pneumonitis; reported fatal outcome in some vaccine-related episodes | HP:0011971 (poor response to vaccination) |
| Fatal enterohemorrhagic/viscerotropic disease after yellow fever vaccination | Post-vaccination | Fatal in at least one reported case | related to HP:0011971 |
| HSV-1 encephalitis susceptibility | Any age (class effect of ISGF3 deficiency) | Severe | HP:0002383 (Encephalitis) |
| Recurrent fevers of unknown cause | Childhood | Recurrent | HP:0001945 (Fever) |
| Sepsis/septic shock | Any age | Life-threatening | HP:0100806 (Shock) |
| Neurological sequelae (post-infectious) | Following severe infection episodes | Persistent | HP:0012759 (Neurodevelopmental abnormality) |

### Inflammatory/immune dysregulation phenotypes
Paradoxically, IRF9-deficient (and STAT2-deficient) patients show a propensity to **hyperinflammation and hemophagocytic lymphohistiocytosis (HLH)** despite failing to control viruses. Mechanistically, loss of ISGF3 does not eliminate all type I IFN receptor (IFNAR) signaling — it removes negative feedback (via reduced induction of USP18), causing **abnormally prolonged IFNAR signaling** that switches the transcriptional output toward a sustained, IFN-γ (GAF)-like inflammatory program, contributing to overt clinical inflammation [Duncan et al. 2022, *JACI*]. HPO term: HP:0005522/HP:0004315 (Hemophagocytic lymphohistiocytosis-related) — code HP:0005537 if modeling.

### Laboratory abnormalities
- Lymphopenia and/or hypogammaglobulinemia, particularly evident during acute infection (per OMIM clinical synopsis).
- Impaired cellular type I interferon response (defective ISGF3 formation on functional testing; intact GAF/STAT1-homodimer formation).

**Severity/progression:** Onset is neonatal-to-early-infancy; course is episodic (severe infections punctuated by relative wellness) but can leave permanent sequelae (bronchiectasis, neurological impairment after severe CNS/systemic infection episodes). Frequency data (percentage of patients with each feature) cannot be meaningfully computed given the extremely small published cohort (2–3 kindreds).

**Quality of life impact:** Not formally studied with QoL instruments (no EQ-5D/SF-36 data identified); qualitatively, recurrent ICU admissions, bronchiectasis, and neurological impairment described in the second family imply substantial chronic morbidity.

Sources: [Hernandez et al. 2018 JEM](https://rupress.org/jem/article/215/10/2567/120233/) · [Duncan et al. 2022 JACI (Aberrant inflammatory responses)](https://www.jacionline.org/article/S0091-6749(22)00185-3/fulltext) · [Vanderver et al./monoclonal antibody case, PMC8609338](https://pmc.ncbi.nlm.nih.gov/articles/PMC8609338/) · [OMIM #618648 Clinical Synopsis](https://www.omim.org/clinicalSynopsis/618648)

---

## 4. Genetic/Molecular Information

**Causal gene:** *IRF9* (HGNC:6398; NCBI Gene ID 10379; OMIM *147574), encoding Interferon Regulatory Factor 9 (also historically named ISGF3γ or p48).

**Reference transcript:** NM_006084.5 (used in ClinVar variant nomenclature).

**Pathogenic variants documented:**
1. **c.991G>A** — last nucleotide of exon 7; predicted to cause a splice-site alteration and possibly p.Asp331Asn substitution. Homozygous in the index patient (Hernandez et al. 2018).
2. **c.577+1G>T** — canonical splice-donor site variant causing skipping of exon 5 and a premature stop codon (frameshift/truncation). Homozygous in two siblings from a consanguineous family (Duncan et al. 2022).

**Variant classification:** Both variants are classified as pathogenic/likely pathogenic for "Immunodeficiency 65, susceptibility to viral infections" in ClinVar.

**Functional consequence:** Loss of function — in vitro functional expression studies show the mutant protein cannot support formation of a functional ISGF3 complex upon IFN stimulation, resulting in loss of ISRE-driven transcriptional activity and failure to induce type-I-IFN-responsive interferon-stimulated genes (ISGs), while GAF (STAT1 homodimer) signaling downstream of IFN-γ remains intact.

**Population frequency:** Specific gnomAD constraint metrics (pLI/LOEUF) for *IRF9* were not retrievable from the search tools used in this session; given that only 1–2 disease-causing families have ever been published, the pathogenic alleles themselves are expected to be essentially private/ultra-rare or absent from population databases. (Recommend direct gnomAD browser query for current o/e and LOEUF values if precise constraint metrics are required for curation.)

**Somatic vs. germline:** Germline only — this is a classic monogenic IEI, not a somatic/oncologic process.

**Modifier genes:** None specifically established; incomplete penetrance patterns are noted generally across inherited defects of type I/III IFN immunity (as discussed in reviews of IRF7/TLR3/IRF9/GATA2 severe-influenza genetics), implying as-yet-unidentified genetic or environmental modifiers.

**Epigenetics/chromosomal abnormalities:** No epigenetic mechanism or chromosomal-level abnormality has been reported for IMD65; it is a single-gene coding/splicing defect.

**Protein structure:** IRF9 is the DNA-binding subunit of ISGF3, containing:
- An N-terminal **DNA-binding domain (DBD)** that binds the interferon-stimulated response element (ISRE).
- A C-terminal **IRF-association domain (IAD)**, structurally resolved in complex with the STAT2 coiled-coil domain (CCD) at 2.9 Å resolution (Rengachari et al., *PNAS* 2018). IRF9 engages the tip of the STAT2-CCD via the convex β-sandwich surface of its IAD; mutating the primary interface (IF1) abolishes STAT2 binding, while IF2/IF3 mutations do not. IRF9 has ~500-fold higher binding affinity for STAT2 than STAT1, explaining its constitutive STAT2 association even before IFN stimulation, and a recently described "molecular switch" model shows pre-formed STAT2–IRF9 complexes converting to active ISGF3 upon STAT1 recruitment after IFN stimulation (Rengachari et al. 2018; Blaszczyk et al., *Nat Commun* 2019).

Ontology suggestions: **HGNC:6398** (IRF9); **GO:0003700** (DNA-binding transcription factor activity); **GO:0060333** (interferon-gamma-mediated signaling pathway, for GAF context); **GO:0060337** (type I interferon-mediated signaling pathway).

Sources: [ClinVar RCV000855434](https://www.ncbi.nlm.nih.gov/clinvar/RCV000855434/) · [ClinVar RCV000855435](https://www.ncbi.nlm.nih.gov/clinvar/RCV000855435/) · [Rengachari et al. 2018, PNAS — Structural basis of STAT2 recognition by IRF9](https://www.pnas.org/doi/10.1073/pnas.1718426115) · [Blaszczyk et al. 2019, Nat Commun — A molecular switch from STAT2-IRF9 to ISGF3](https://www.nature.com/articles/s41467-019-10970-y) · [NIH GTR — IRF9 gene](https://www.ncbi.nlm.nih.gov/gtr/genes/10379/)

---

## 5. Environmental Information

- **Non-genetic contributing factors:** None causal (this is a fully penetrant-for-genotype monogenic disease); environmental exposures act only as *triggers* that reveal the immunodeficiency.
- **Infectious triggers reported:** Influenza A virus, RSV, parainfluenza virus, adenovirus, SARS-CoV-2, HSV-1, and VZV (both wild-type and vaccine strain). No bacterial, fungal, or parasitic triggers are specifically documented as primary drivers, though septic shock (potentially with secondary bacterial superinfection) has been listed as a clinical feature in OMIM.
- **Iatrogenic/vaccine exposure:** Live-attenuated viral vaccines (yellow fever 17D, VZV vaccine, MMR) are a well-documented "environmental" precipitant of severe/fatal disease in this and related ISGF3-pathway deficiencies (also seen in STAT2 and IFNAR1 deficiency), underscoring why these vaccines are specifically contraindicated in this population.
- **Lifestyle factors:** None specifically implicated; this is a pediatric-onset primary immunodeficiency, not a lifestyle-modulated disease.

Sources: [Duncan et al. 2022, JACI](https://www.jacionline.org/article/S0091-6749(22)00185-3/fulltext) · [Hernandez et al. 2018, JEM](https://rupress.org/jem/article/215/10/2567/120233/)

---

## 6. Mechanism / Pathophysiology

**Core molecular pathway (causal chain):**

1. **Trigger:** Viral infection → viral RNA/DNA sensing by pattern-recognition receptors (TLR3, RIG-I/MDA5) → production of type I (IFN-α/β) and type III (IFN-λ) interferons by infected cells and plasmacytoid dendritic cells.
2. **Receptor engagement:** IFN-α/β bind IFNAR1/IFNAR2; IFN-λ binds IFNLR1/IL10RB.
3. **JAK-STAT activation:** Receptor engagement activates JAK1/TYK2, which phosphorylate STAT1 and STAT2.
4. **ISGF3 assembly (normal):** Phosphorylated STAT1–STAT2 heterodimer associates with **IRF9** to form the heterotrimeric **ISGF3 complex**. IRF9 provides the DNA-binding specificity, targeting ISGF3 to interferon-stimulated response elements (ISREs) in ISG promoters.
5. **ISG transcription (normal):** ISGF3 drives transcription of hundreds of interferon-stimulated genes establishing a cell-intrinsic antiviral state (restriction of viral replication, apoptosis of infected cells, amplification loops via IRF7).
6. **Defect in IRF9 deficiency:** Loss-of-function IRF9 variants prevent ISGF3 complex formation entirely. Patient cells can still form GAF (STAT1 homodimers, IFN-γ pathway) but **cannot activate ISGF3 trimers** in response to type I IFN — resulting in global failure of type I/III-IFN-driven ISG induction.
7. **Downstream consequence:** Unrestricted viral replication is observed in patient-derived cells for influenza A virus, parainfluenza virus, and RSV in vitro — a phenotype rescued by reintroducing wild-type IRF9 — demonstrating the ISGF3 pathway is essential (non-redundant) for controlling these respiratory viruses in human airway/epithelial contexts.
8. **Paradoxical hyperinflammation branch:** Even without a functional ISGF3, some IFNAR signaling persists (via GAF or residual signaling), but because ISGF3 normally also induces the negative-feedback regulator **USP18** (which dampens JAK-STAT signaling), IRF9 (and STAT2) deficiency results in **abnormally prolonged IFNAR signaling** that shifts toward a sustained, IFN-γ-like transcriptional output. This aberrant, unchecked inflammatory signaling is proposed as the mechanism underlying the hyperinflammation/HLH phenotype seen in some patients — i.e., failure of negative feedback, not excess ISGF3 activity, drives immune dysregulation.

**Cell types involved:** Airway/pulmonary epithelial cells (site of respiratory viral replication and IFN response failure — modeled using iPSC-derived pulmonary epithelial cells in comparable IRF7/TLR3 studies), plasmacytoid dendritic cells, fibroblasts (used as the standard patient-cell model for functional IFN-response testing), and lymphocytes (B and T cell abnormalities noted clinically).

**Suggested GO terms:**
- GO:0060337 – type I interferon-mediated signaling pathway (impaired)
- GO:0002606 – regulation of dendritic cell antigen processing/presentation (context: pDC IFN production)
- GO:0009615 – response to virus
- GO:0039528 – cytoplasmic pattern recognition receptor signaling pathway (upstream sensing)
- GO:0060333 – interferon-gamma-mediated signaling pathway (intact/compensatory GAF pathway)

**Suggested CL terms:**
- CL:0002563 – respiratory basal cell / CL:0002370 – respiratory epithelial cell (site of infection)
- CL:0000784 – plasmacytoid dendritic cell (IFN-α/β source)
- CL:0000542 – lymphocyte (lymphopenia)

**Molecular/biochemical abnormality:** Complete or near-complete loss of ISGF3 DNA-binding/transcriptional activity at ISREs; GAF/STAT1-homodimer activity is preserved, distinguishing IRF9 deficiency mechanistically from STAT1 deficiency (which would ablate both ISGF3 and GAF pathways).

**Omics/advanced technologies:** No transcriptomic (RNA-seq/GEO), proteomic, or single-cell datasets specific to IRF9-deficient patient tissue were identified in this search; functional characterization to date has relied on classical reporter assays (ISRE-luciferase), EMSA/DNA-binding assays, phospho-flow/immunoblot for STAT1/STAT2 phosphorylation, and viral-challenge assays in patient-derived fibroblasts and complementation (wild-type IRF9 rescue) experiments.

Sources: [Hernandez et al. 2018, JEM](https://rupress.org/jem/article/215/10/2567/120233/) · [Duncan et al. 2022, JACI](https://www.jacionline.org/article/S0091-6749(22)00185-3/fulltext) · [Kimura et al. 1996, original Irf9(-/-) mouse study, cited via ScienceDirect Topics IRF9 overview](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/irf9) · [Blaszczyk et al. 2019, Nat Commun](https://www.nature.com/articles/s41467-019-10970-y)

---

## 7. Anatomical Structures Affected

- **Primary organ:** Respiratory system (lungs) — the dominant clinical target, with pneumonia/pneumonitis as the recurring presenting feature across all reported patients (influenza pneumonitis, VZV pneumonitis, COVID-19).
- **Secondary/complication-level involvement:**
  - Airways: bronchiectasis (structural, likely post-infectious/inflammatory sequela) — UBERON:0002185 (bronchus), UBERON:0002048 (lung).
  - Nervous system: encephalitis susceptibility (HSV-1), neurological impairment as sequela of severe systemic infection — UBERON:0000955 (brain).
  - Hematologic/immune system: lymphopenia, hypogammaglobulinemia, HLH-associated macrophage activation — UBERON:0002371 (bone marrow), UBERON:0002106 (spleen), UBERON:0000029 (lymph node).
  - Systemic: septic shock, viscerotropic disease (multi-organ, seen after yellow fever vaccine) affecting liver and other viscera — UBERON:0002107 (liver).
- **Tissue/cell level:** Respiratory epithelium (site of unrestricted viral replication), plasmacytoid dendritic cells and lymphocytes (immune dysregulation), macrophages/histiocytes (HLH).
- **Subcellular level:** Nucleus (site of failed ISGF3-ISRE transcriptional activation); cytoplasm (site of JAK-STAT activation and STAT2-IRF9 complex assembly prior to nuclear translocation) — GO Cellular Component: GO:0005634 (nucleus), GO:0005737 (cytoplasm).
- **Localization pattern:** Bilateral pulmonary involvement typical of viral pneumonitis (not lateralized).

Source: [Hernandez et al. 2018, JEM](https://rupress.org/jem/article/215/10/2567/120233/) · [Duncan et al. 2022, JACI](https://www.jacionline.org/article/S0091-6749(22)00185-3/fulltext)

---

## 8. Temporal Development

- **Onset:** Congenital defect, but clinically silent until first significant viral exposure; the index patient's first severe presentation (influenza pneumonitis) was at **age 2 years**; the sibling family had **onset in the first year of life** (multiple severe viral infections including RSV and disseminated post-vaccination VZV).
- **Onset pattern:** Acute, episodic — each viral encounter can precipitate an acute severe illness against a baseline of apparent wellness.
- **Progression:** Not a steadily progressive degenerative disease; rather a **relapsing pattern of acute severe infectious episodes**, some of which leave permanent structural/functional damage (bronchiectasis, persistent neurological impairment reported in the sibling case after prolonged ICU stays).
- **Disease course pattern:** Episodic/relapsing, punctuated by intercurrent health; underlying immunologic defect is lifelong and static (the genetic lesion does not change), but clinical burden accumulates with each infectious/vaccine-associated event.
- **Duration:** Chronic, lifelong immunologic defect; clinical episodes are acute but recurrent across childhood (and demonstrated into at least age 8 in the COVID-19 case).
- **Remission:** No spontaneous "cure"; interepisode periods represent clinical quiescence, not resolution of the underlying defect. Treatment-induced resolution of acute episodes (e.g., monoclonal antibody therapy) has been documented (see Treatment).
- **Critical periods:** Early childhood is the period of highest risk, coinciding with the height of routine live-vaccine administration (MMR, VZV, and in endemic/travel contexts, yellow fever) and highest exposure to common respiratory viruses (RSV, influenza, parainfluenza) — making early genetic diagnosis critical to avoid live-vaccine—triggered catastrophic events.

Sources: [Hernandez et al. 2018, JEM](https://rupress.org/jem/article/215/10/2567/120233/) · [Duncan et al. 2022, JACI](https://www.jacionline.org/article/S0091-6749(22)00185-3/fulltext) · [PMC8609338 — COVID-19 case](https://pmc.ncbi.nlm.nih.gov/articles/PMC8609338/)

---

## 9. Inheritance and Population

- **Epidemiology:** Extremely rare — to date, the peer-reviewed literature reports **only two or three unrelated kindreds worldwide** (one sporadic case reported in 2018, and one consanguineous two-sibling family reported in 2022), so no formal prevalence/incidence estimate exists (essentially "ultra-rare," likely well below 1/1,000,000).
- **Inheritance pattern:** Autosomal recessive (AR); confirmed homozygosity/compound heterozygosity in all reported cases.
- **Penetrance:** Appears high/complete for the immunologic (ISGF3 loss-of-function) defect itself, but **clinical penetrance for any single infectious phenotype is incomplete and stochastic** — analogous to other monogenic causes of severe influenza pneumonitis (IRF7, TLR3, GATA2), where the disease only manifests upon specific viral exposure, and severity/expressivity varies between patients and even between infectious episodes in the same patient.
- **Expressivity:** Variable — the index patient's dominant phenotype was severe influenza pneumonitis; the sibling family's dominant phenotypes were RSV, disseminated vaccine-strain VZV, and features of hyperinflammation/HLH — illustrating that the same genotype can manifest with different predominant viral susceptibilities and different degrees of inflammatory dysregulation.
- **Genetic anticipation:** Not applicable (not a repeat-expansion disorder).
- **Germline mosaicism:** Not reported.
- **Founder effects:** None established; the two published pathogenic alleles (c.991G>A and c.577+1G>T) are private to their respective families.
- **Consanguinity:** A documented risk factor — the sibling family with c.577+1G>T arose in a consanguineous kindred.
- **Carrier frequency:** No population carrier-frequency data available given the extreme rarity and apparent absence of these specific alleles from large population databases (gnomAD frequency data specific to *IRF9* pathogenic variants were not retrievable in this search session).
- **Population demographics:** The COVID-19 case patient was of **Algerian ancestry** (French nationality); the original index patient's ancestry was not specified in available search results; specific geographic/ethnic clustering has not been established beyond these isolated reports.
- **Sex ratio / age distribution:** Insufficient case numbers (n=3–4 patients across all published reports) to derive meaningful sex ratio or age-distribution statistics.

Sources: [Hernandez et al. 2018, JEM](https://rupress.org/jem/article/215/10/2567/120233/) · [Duncan et al. 2022, JACI](https://www.jacionline.org/article/S0091-6749(22)00185-3/fulltext) · [PMC8609338](https://pmc.ncbi.nlm.nih.gov/articles/PMC8609338/)

---

## 10. Diagnostics

**Clinical/laboratory tests:**
- Standard immunologic workup: lymphocyte subset enumeration (lymphopenia reported), immunoglobulin levels (hypogammaglobulinemia reported during infection), vaccine antibody responses.
- **Functional interferon-response assays** (the gold-standard confirmatory test): patient-derived fibroblasts or PBMCs stimulated with IFN-α2b, assessed for:
  - **ISGF3 complex formation** — EMSA/DNA-binding assays showing loss of ISGF3 trimer formation while GAF (STAT1 homodimer) formation is preserved.
  - **ISG induction** — qPCR/expression panels for canonical ISGs (e.g., MX1, ISG15, IFIT1) showing blunted induction.
  - **Phospho-flow cytometry** for pSTAT1/pSTAT2 can help localize the block relative to receptor-proximal JAK-STAT signaling.
  - **Viral challenge/complementation assays** — direct demonstration that patient cells fail to control IAV/PIV/RSV replication, rescued by wild-type IRF9 re-expression (used definitively in the index case).
- **Biopsy/histopathology:** Not a primary diagnostic modality for this condition (no characteristic tissue histopathology reported beyond nonspecific inflammatory/HLH-type bone-marrow or lymph-node findings during acute hyperinflammatory episodes).

**Genetic testing:**
- **Recommended approach:** Given the phenotypic overlap with other IEIs of type I/III interferon immunity (IRF7, STAT1, STAT2, TYK2, IFNAR1/2, TLR3, IFIH1, GATA2), a **targeted primary immunodeficiency/severe viral susceptibility gene panel** or **whole-exome/whole-genome sequencing** is the standard diagnostic route, as used in both published cases (WES in the index case; panel sequencing in the consanguineous sibling family).
- **Single-gene testing:** Reasonable if a specific *IRF9* variant is suspected from family history or panel screening.
- **Chromosomal microarray/karyotyping/FISH:** Not indicated — this is a single-gene coding/splice-site disorder, not a copy-number or structural chromosomal disease.
- **Confirmatory functional testing** (as above) is recommended given the WES/panel finding, since splice-site predictions (e.g., c.991G>A) benefit from functional/RNA-level confirmation.

**Clinical criteria/differential diagnosis:** No formal diagnostic consensus criteria exist (too rare); the practical differential diagnosis for a child presenting with unexplained severe/recurrent viral pneumonitis and/or severe reaction to live vaccines includes: **STAT1 deficiency, STAT2 deficiency (IMD62), IRF7 deficiency (IMD51), TLR3 deficiency, IFNAR1/IFNAR2 deficiency, TYK2 deficiency, IFIH1 deficiency, GATA2 deficiency**, and severe combined immunodeficiency (SCID) more broadly, particularly when a live-vaccine-associated catastrophic illness is the presenting event (as SCID is the more common genetic cause of such presentations, and must be excluded).

**Screening:** No population newborn-screening program targets *IRF9* specifically; however, given the risk of catastrophic reactions to live-attenuated vaccines, **genetic/immunologic screening prior to live vaccination (MMR, VZV, yellow fever) is warranted in any infant with a family history of unexplained severe/fatal reactions to viral infection or vaccination**, and cascade testing of siblings in an index family is recommended (as performed in the reported sibling kindred).

Sources: [Hernandez et al. 2018, JEM](https://rupress.org/jem/article/215/10/2567/120233/) · [Duncan et al. 2022, JACI](https://www.jacionline.org/article/S0091-6749(22)00185-3/fulltext)

---

## 11. Outcome/Prognosis

- **Survival/mortality:** Not uniformly fatal, but the disease has a documented lethal potential — one reported association is a **fatal enterohemorrhagic/viscerotropic-type illness following yellow fever vaccination**, and the disseminated post-vaccination VZV pneumonitis episode in the sibling family was severe/life-threatening. The index patient and the COVID-19 case patient both survived their severe infectious episodes with appropriate intensive/targeted therapy.
- **Life expectancy:** No formal actuarial data exist given the extremely small number of published patients; prognosis appears strongly dependent on avoidance of live vaccines and prompt, aggressive management of viral infections (including early antiviral/monoclonal antibody intervention).
- **Morbidity/functional outcomes:** Bronchiectasis (chronic structural lung disease) and persistent neurological impairment have been documented as long-term sequelae following severe infectious episodes in the sibling family, indicating that even survivors can carry significant chronic morbidity.
- **Complications:** Pneumonia/pneumonitis, bronchiectasis, septic shock, HLH/hyperinflammation, encephalitis (HSV-1 risk), and vaccine-strain disseminated viral disease are all recognized complications.
- **Recovery potential:** With early diagnosis, live-vaccine avoidance, and prompt treatment of acute viral episodes (including newer targeted therapies such as neutralizing monoclonal antibodies), acute episodes can resolve without further sequelae — as demonstrated in the COVID-19 case, where the patient was **completely asymptomatic with an unremarkable follow-up at day 50** after monoclonal antibody treatment.
- **Prognostic factors:** Early genetic diagnosis (enabling live-vaccine avoidance and vigilant infection management) appears to be the single most actionable prognostic factor described in the literature; no specific molecular biomarker for prognosis (beyond the underlying genotype) has been established.

Sources: [PMC8609338 — Monoclonal antibody neutralization of SARS-CoV-2 in an IRF9-deficient child](https://pmc.ncbi.nlm.nih.gov/articles/PMC8609338/) · [Duncan et al. 2022, JACI](https://www.jacionline.org/article/S0091-6749(22)00185-3/fulltext)

---

## 12. Treatment

Because IRF9 deficiency disables an endogenous antiviral signaling pathway rather than a druggable enzyme, management is centered on **prevention (avoiding triggers), passive/targeted antiviral immunity, and supportive/immunomodulatory care**, rather than gene-specific pharmacotherapy.

**Pharmacotherapy / targeted antiviral therapy:**
- **Neutralizing monoclonal antibodies** — In the best-documented treatment success, an 8-year-old IRF9-deficient girl with SARS-CoV-2 infection and very high viral load was treated with a half-dose (600 mg total) of the **casirivimab + imdevimab** monoclonal antibody combination on day 2 of illness; her viremia cleared by day 4, and pneumonia was prevented entirely — demonstrating that direct viral neutralization can compensate for a complete defect in interferon-dependent intrinsic antiviral immunity. Suggested NCIT term: NCIT:C171760 (Monoclonal Antibody Therapy) / therapeutic modality = MONOCLONAL_ANTIBODY.
- **Interferon-lambda (peginterferon-λ)** is mechanistically attractive as a potential therapeutic in some interferon-pathway defects (given its epithelial-restricted receptor distribution and lower systemic toxicity than IFN-α), and has independent evidence as an early COVID-19 antiviral in the general population; however, **it would not be expected to bypass an ISGF3-complex defect like IRF9 deficiency**, since IFN-λ signals through the same downstream ISGF3 machinery — its utility in this specific IEI is therefore mechanistically limited/unproven, unlike its role in other, more receptor-proximal defects.

**Immunoglobulin/passive immunity:**
- **Immunoglobulin replacement therapy (IVIG/SCIG)** is a mainstay supportive strategy in PID management generally and has specifically been proposed as protective in ISGF3-pathway deficiencies, since pooled immunoglobulin from immunocompetent donors provides passive neutralizing antibody coverage against common pathogens, substituting for the patient's own impaired antiviral defense. NCIT term candidate: NCIT:C15986 (Pharmacotherapy) with therapeutic_agent = immune globulin.

**Preventive/avoidance strategy (most emphasized in the literature):**
- **Strict avoidance of live-attenuated viral vaccines** (yellow fever 17D, VZV vaccine, MMR) is the single most repeatedly emphasized management recommendation, given documented severe/fatal reactions in this and related ISGF3-pathway deficiencies (STAT2, IFNAR1/2).
- Use of **inactivated/killed vaccines** where possible for routine immunization.

**Supportive care:**
- Aggressive supportive management of acute severe viral pneumonitis episodes (mechanical ventilation, ICU-level care), as required in the index influenza case.
- Management of HLH/hyperinflammatory episodes would follow standard HLH-directed immunomodulatory protocols (e.g., corticosteroids, IL-1/IL-6 pathway-directed therapy where clinically indicated), though no IRF9-deficiency-specific HLH treatment trial data exist.

**Experimental/investigational:**
- No gene therapy, gene editing, or hematopoietic stem cell transplantation approach has been reported specifically for IRF9 deficiency in the literature surveyed (unlike some other severe IEIs where HSCT is curative, IRF9 deficiency's defect is not primarily hematopoietic-cell-intrinsic in a way that clearly predicts HSCT benefit, and no such case has been published).
- No disease-specific registered clinical trials (ClinicalTrials.gov) were identified for IRF9 deficiency specifically.

**Treatment outcomes:** The single best-documented outcome is the COVID-19 case, in which monoclonal antibody therapy prevented pneumonia and led to full recovery with no residual symptoms at 50-day follow-up — supporting monoclonal antibody-based passive immunotherapy as a rational, evidence-based intervention for this genotype during specific viral infections for which such antibodies are available.

**Personalized/genotype-guided approach:** Because the defect is precisely characterized at the molecular level (loss of ISGF3 formation, intact GAF), therapy can be rationally targeted to **bypass rather than restore** the defective pathway — i.e., preferring therapies that act independently of ISGF3 (direct viral neutralization via monoclonal antibodies, passive immunoglobulin) over therapies that would require an intact ISGF3 response to be effective (e.g., IFN-α/β or IFN-λ administration alone, which would be expected to have blunted efficacy).

Sources: [PMC8609338 — Monoclonal antibody-mediated neutralization of SARS-CoV-2 in an IRF9-deficient child](https://pmc.ncbi.nlm.nih.gov/articles/PMC8609338/) · [Duncan et al. 2022, JACI](https://www.jacionline.org/article/S0091-6749(22)00185-3/fulltext)

---

## 13. Prevention

- **Primary prevention:** Not possible at the population level (no environmental risk factor to modify); at the individual/family level, **genetic counseling and carrier testing** in families with a known pathogenic *IRF9* allele, plus **avoidance of live-attenuated vaccines** in confirmed or at-risk individuals, constitute the primary preventive strategy.
- **Secondary prevention (early detection):** Prompt genetic diagnosis following a first severe/atypical viral infection episode enables early institution of protective measures (vaccine avoidance, close infection monitoring, early antiviral/monoclonal antibody treatment access) before a second, potentially fatal, event occurs — as illustrated by the index-to-sibling diagnostic cascade in the second reported family.
- **Genetic counseling:** Essential in any family with a confirmed proband, given autosomal recessive inheritance (25% recurrence risk for future siblings) and demonstrated consanguinity risk; prenatal or preimplantation genetic testing could be considered in informed families given the demonstrated risk of fatal outcomes.
- **Screening for at-risk relatives:** Cascade genetic screening of siblings (as performed in the consanguineous family) allows pre-symptomatic identification and vaccine-avoidance counseling before a sentinel catastrophic event.
- **Immunization strategy:** Substituting **inactivated vaccines** for all live-vaccine equivalents in the routine immunization schedule where such alternatives exist, and case-by-case risk-benefit discussion (with likely deferral/avoidance) for vaccines with no inactivated alternative (e.g., yellow fever, where travel to endemic areas would need individualized risk mitigation such as avoidance or reliance on non-vaccine protective measures).
- **Prophylaxis:** Regular immunoglobulin replacement has been suggested as a prophylactic strategy providing passive antiviral antibody coverage in ISGF3-pathway-deficient patients.
- **Public health relevance:** As an ultra-rare monogenic condition, this disease has no population-level public-health intervention; its main public-health relevance is as a genetic explanatory model informing broader vaccine-safety monitoring for rare severe/fatal live-vaccine reactions in children, prompting genetic workup in such sentinel cases.

Sources: [Duncan et al. 2022, JACI](https://www.jacionline.org/article/S0091-6749(22)00185-3/fulltext) · [Hernandez et al. 2018, JEM](https://rupress.org/jem/article/215/10/2567/120233/)

---

## 14. Other Species / Natural Disease

- **Taxonomy:** No naturally occurring IRF9-deficiency disease has been reported in non-human species (companion animals or wildlife) in the sources surveyed.
- **Orthologous gene:** *Irf9* is highly conserved across mammals; the mouse ortholog (*Irf9*, historically *Isgf3g*, protein p48) is the basis of the principal animal model (see Section 15). NCBI Gene IDs: human *IRF9* = 10379; mouse *Irf9* ortholog exists in MGI (specific ID not retrieved in this session).
- **Comparative biology:** The IRF9-STAT1-STAT2 ISGF3 axis is deeply conserved across vertebrates, underlying its fundamental role in antiviral immunity; a recent (2024) preprint reports identification of avian IRF3 and IRF9 orthologs, reflecting ongoing interest in evolutionary conservation of this pathway across the IRF family, though this is basic comparative genomics rather than a disease model.
- **Zoonotic potential/cross-species susceptibility:** Not applicable — this is a human genetic immunodeficiency, not an infectious/zoonotic disease itself.

Sources: [Avian IRF3/IRF9 preprint, bioRxiv 2024](https://www.biorxiv.org/content/10.1101/2024.09.24.613690.full.pdf) · general IRF9 literature above

---

## 15. Model Organisms

**Primary model: *Irf9*-knockout (formerly *Isgf3g*/"p48"-null) mice** (Kimura et al., 1996 — the original characterization).

- **Model type:** Mammalian, germline gene-knockout (constitutive, whole-organism).
- **Key phenotype:** *Irf9*⁻/⁻ mice **fail to survive viral challenge**; in *Irf9*⁻/⁻-derived embryonic fibroblasts (EFs) and peritoneal macrophages, IFN-α– or IFN-γ–induced antiviral states are abolished or dramatically impaired against multiple virus classes tested (encephalomyocarditis virus [EMCV], vesicular stomatitis virus [VSV], herpes simplex virus [HSV]). ISGF3-like DNA-binding activity, present in IFN-γ–stimulated wild-type fibroblasts, is absent in *Irf9*⁻/⁻ fibroblasts, and IFN-α–induced ISG expression is severely blunted.
- **Fidelity to human disease:** This model **recapitulates the core human mechanistic defect** (loss of ISGF3-dependent antiviral gene induction and consequent uncontrolled viral replication) with high fidelity at the molecular/cellular level; however, the mouse constitutive-knockout phenotype (susceptibility across at least three virus classes, with lethality on challenge) is notably **more severe/broadly susceptible than the surviving human patients**, who — despite comparable ISGF3 loss — have survived to school age with targeted interventions, illustrating a translational gap likely explained by differences in pathogen exposure, redundant human host defenses (e.g., passive/adaptive immunity, medical intervention), and species-specific differences in interferon biology.
- **Limitations:** The constitutive knockout does not model the episodic/vaccine-triggered clinical pattern seen in humans, nor the paradoxical hyperinflammatory/HLH phenotype now recognized in human STAT2/IRF9 deficiency (which depends on subtler negative-feedback dysregulation, e.g., via USP18, that may not be fully captured in acute lethal-challenge knockout studies).
- **Research applications:** The *Irf9*-null mouse remains the standard tool for dissecting ISGF3-dependent versus ISGF3-independent (e.g., STAT2/IRF9-only, or GAF-mediated) antiviral and immunoregulatory pathways, and has also been used to study IRF9's role in preventing CD8+ T-cell exhaustion during chronic LCMV infection (an extrinsic, non-cell-autonomous immunoregulatory role for IRF9 beyond classical antiviral ISG induction) and in intestinal inflammation (noncanonical IRF9 effects reported independent of type I/III interferon signaling).
- **Cellular/in vitro models:** Human patient-derived primary fibroblasts and PBMCs (used in both published human case reports) remain the principal disease-relevant cellular models, with viral-challenge complementation (wild-type IRF9 re-expression rescuing antiviral control) serving as the functional proof of causality in humans, analogous in logic to the mouse knockout/rescue paradigm.
- **Resources:** MGI (Mouse Genome Informatics) for *Irf9* allele records; no zebrafish, Drosophila, or C. elegans orthologous disease models were identified in this search (IRF-family transcription factors of this type are vertebrate-specific innovations, limiting invertebrate modeling utility).

Sources: [ScienceDirect Topics — IRF9 overview, summarizing Kimura et al. 1996](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/irf9) · [IRF9 Prevents CD8+ T Cell Exhaustion, J Virol 2017 / PMC5660491](https://pmc.ncbi.nlm.nih.gov/articles/PMC5660491/) · [Noncanonical Effects of IRF9 in Intestinal Inflammation, PubMed 25918247](https://pubmed.ncbi.nlm.nih.gov/25918247/)

---

## Summary of Key Citations

1. Hernandez N, et al. "Life-threatening influenza pneumonitis in a child with inherited IRF9 deficiency." *J Exp Med.* 2018;215(10):2567–2585. PMID: 30143481. https://rupress.org/jem/article/215/10/2567/120233/
2. Duncan CJA, et al. "Aberrant inflammatory responses to type I interferon in STAT2 or IRF9 deficiency." *J Allergy Clin Immunol.* 2022. PMID: 35182547. https://www.jacionline.org/article/S0091-6749(22)00185-3/fulltext
3. "Monoclonal antibody-mediated neutralization of SARS-CoV-2 in an IRF9-deficient child." PMC8609338. https://pmc.ncbi.nlm.nih.gov/articles/PMC8609338/
4. OMIM #618648 — IMMUNODEFICIENCY 65, SUSCEPTIBILITY TO VIRAL INFECTIONS. https://www.omim.org/entry/618648
5. OMIM *147574 — INTERFERON REGULATORY FACTOR 9; IRF9. https://omim.org/entry/147574
6. Rengachari S, et al. "Structural basis of STAT2 recognition by IRF9 reveals molecular insights into ISGF3 function." *PNAS.* 2018. https://www.pnas.org/doi/10.1073/pnas.1718426115
7. Blaszczyk K, et al. "A molecular switch from STAT2-IRF9 to ISGF3 underlies interferon-induced gene transcription." *Nat Commun.* 2019. PMID: (PMC6606597). https://www.nature.com/articles/s41467-019-10970-y
8. "Human genetics of life-threatening influenza pneumonitis." *Hum Genet.* 2019. PMC7094886. https://pmc.ncbi.nlm.nih.gov/articles/PMC7094886
9. ClinVar RCV000855434 (c.577+1G>T) and RCV000855435 (c.991G>A/p.Asp331Asn), NCBI. https://www.ncbi.nlm.nih.gov/clinvar/
10. IRF9 gene records — GeneCards, NCBI GTR. https://www.genecards.org/cgi-bin/carddisp.pl?gene=IRF9 · https://www.ncbi.nlm.nih.gov/gtr/genes/10379/

**Note on data gaps:** This is one of the rarest inborn errors of immunity in the literature (only ~2 published kindreds, ~3–4 total patients as of this writing), so several requested data points — formal prevalence/incidence, gnomAD constraint metrics, QoL instrument scores, and any animal-model-independent transcriptomic/proteomic datasets — are simply not available in the primary literature and should be flagged as "not yet documented" (`NOT_YET_DOCUMENTED`) rather than estimated when this report is used to populate structured knowledge-base fields (e.g., `PrevalenceClassEnum`). One search result linking IRF9 to "alacrima, achalasia, and impaired intellectual development syndrome" (Triple-A syndrome) is flagged as almost certainly a gene-database cross-contamination artifact (that syndrome is caused by *AAAS*, not *IRF9*) and should **not** be incorporated into curation.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 8 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.