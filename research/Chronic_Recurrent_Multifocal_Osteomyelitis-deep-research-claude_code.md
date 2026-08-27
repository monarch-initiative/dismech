---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-21T16:24:55.639971'
end_time: '2026-08-21T16:29:53.960451'
duration_seconds: 298.32
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Chronic Recurrent Multifocal Osteomyelitis
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
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 17
  num_turns: 24
  total_cost_usd: 1.9447541999999998
  session_id: 6f8bf895-3ab0-55cb-a154-acb932b43f03
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 41
reference_validation:
  total_references: 31
  verified: 31
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 31
  on_topic: 26
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Chronic Recurrent Multifocal Osteomyelitis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Chronic Recurrent Multifocal Osteomyelitis** covering all of the
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

I now have sufficient material to compile a comprehensive research report.

# Chronic Recurrent Multifocal Osteomyelitis (CRMO) / Chronic Nonbacterial Osteomyelitis (CNO): Comprehensive Research Report

## 1. Disease Information

**Overview.** Chronic recurrent multifocal osteomyelitis (CRMO) — increasingly referred to in the broader literature as **chronic nonbacterial osteomyelitis (CNO)**, of which CRMO represents the recurrent/multifocal end of the spectrum — is a rare, non-infectious **autoinflammatory bone disease** that causes sterile inflammatory bone lesions, predominantly in children and adolescents. It mimics infectious (bacterial) osteomyelitis clinically and radiographically but yields negative cultures and does not respond to antibiotics. CRMO is classified as an autoinflammatory disorder of the innate immune system rather than an autoimmune disease, since it lacks high-titer autoantibodies or clear autoreactive lymphocyte involvement ([PMC10483435](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10483435/)).

**Key identifiers:**
- **ICD-10-CM:** M86.3 (Chronic multifocal osteomyelitis), M86.30 ([AAPC](https://www.aapc.com/codes/icd-10-codes/M86.3))
- **Orphanet:** ORPHA:324964 (also historically ORPHA:169147 for the broader syndrome group)
- **Disease Ontology:** DOID:0060645
- **MONDO:** MONDO:0958177 (non-syndromic CRMO); syndromic monogenic forms carry separate MONDO/OMIM entries
- **OMIM (monogenic subtypes):**
  - CRMO2 (with periostitis and pustulosis) — OMIM #612852
  - CRMO3 — OMIM #259680 (autosomal dominant form)
  - Majeed syndrome (CRMO + congenital dyserythropoietic anemia) — OMIM #609628, caused by *LPIN2*
  - DIRA (deficiency of IL-1 receptor antagonist), a related monogenic autoinflammatory bone disease — caused by *IL1RN*

**Synonyms:** Chronic nonbacterial osteomyelitis (CNO), chronic nonbacterial osteitis, nonbacterial osteitis (NBO), sterile multifocal osteomyelitis; the adult-spectrum manifestation overlaps with **SAPHO syndrome** (Synovitis, Acne, Pustulosis, Hyperostosis, Osteitis), which is now widely regarded as part of the same disease continuum in adults ([Oxford Rheumatology Advances in Practice](https://academic.oup.com/rheumap/article/8/4/rkae114/7822209)).

**Evidence base:** Because CRMO is rare, most disease-level knowledge derives from aggregated resources — multicenter retrospective cohorts, international registries (e.g., Eurofever), and national prospective surveillance studies (e.g., the UK/Republic of Ireland British Paediatric Surveillance Unit [BPSU] study) — rather than single-patient EHR mining, supplemented by murine genetic models.

---

## 2. Etiology

### Disease Causal Factors
CRMO is understood as resulting from **dysregulated innate immune/monocyte signaling** causing an imbalance between pro- and anti-inflammatory cytokines, culminating in **NLRP3 inflammasome hyperactivation**, IL-1β-driven inflammation, and pathological osteoclastogenesis. Three converging mechanisms have been proposed: (1) imbalanced cytokine expression, (2) increased inflammasome activation, and (3) enhanced osteoclast differentiation ([PMC10483435](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10483435/); [PMC5705736](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5705736/)).

### Genetic Risk Factors

**Monogenic syndromic forms (Mendelian, high-penetrance):**
- **Majeed syndrome** — autosomal recessive, caused by loss-of-function mutations in **LPIN2** (encoding lipin-2, a phosphatidic acid phosphatase); presents with CRMO, congenital dyserythropoietic anemia, and often neutrophilic dermatosis. Only ~24 individuals from 10 families with genetically confirmed disease reported to date ([PMC8252456](https://pmc.ncbi.nlm.nih.gov/articles/PMC8252456/); OMIM #609628). Novel *LPIN2* mutations have been shown to link bone inflammation to inflammatory M2 macrophages and accelerated osteoclastogenesis (PMID:33314777).
- **DIRA (Deficiency of IL-1 Receptor Antagonist)** — autosomal recessive, caused by loss-of-function mutations in **IL1RN**, producing unopposed IL-1 signaling; presents with neonatal-onset pustulosis, marked inflammatory markers, sterile multifocal osteitis, and periostitis.
- **PAPA syndrome** — caused by mutations in *PSTPIP1*, driving pyrin inflammasome activation and elevated IL-1β; shares mechanistic overlap with CRMO.
- **CRMO3** (OMIM #259680) — autosomal dominant form, early childhood-onset bone pain/arthritis from sterile osteomyelitis.
- **CRMO2** (OMIM #612852) — CRMO with periostitis and pustulosis.

**Non-syndromic (sporadic) CRMO susceptibility genes:**
- **FBLIM1** (filamin-binding LIM protein 1) — recessive coding and regulatory mutations identified via whole-exome sequencing in a consanguineous family (South Asian ancestry); *Fblim1* is the most differentially expressed gene (>20-fold downregulated) in bone marrow macrophages of the murine *cmo* (chronic multifocal osteomyelitis) model, implicating impaired RANKL regulation and osteoclast differentiation (PMID:28301468; [PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0169687)).
- **P2RX7** — a 2023–2024 targeted/exome sequencing study (n=190 CNO patients vs. 1,873 controls) found rare, presumably damaging *P2RX7* variants in **5.8% of CNO patients vs. 1.9% of controls**, and rare lower-impact variants in **32.4% vs. 4.4%** of controls — the gene was "more than 10-fold more variable" among patients. P2X7 is an ATP-gated cation channel that mediates potassium efflux, a potent NLRP3 inflammasome trigger; CNO-associated variants alter inflammasome assembly and **reduce pyroptosis**, potentially prolonging monocyte survival and cytokine output. Patients with damaging *P2RX7* variants had more GI symptoms and lymphadenopathy but less spinal/joint/skin (psoriasis) involvement ([ScienceDirect 2024](https://www.sciencedirect.com/science/article/pii/S0896841124000179); [Liverpool repository](https://livrepository.liverpool.ac.uk/3179118/)).
- **FGR** (Src-family kinase) — expressed in mast cells/neutrophils, contributes to aseptic bone inflammation independently of NLRP3 (PMID:31138708).
- **IL-10 promoter haplotypes** (GCC/ACC/ATA) modulate transcriptional output; most sporadic CRMO patients show enrichment for the lower-expressing haplotype pattern relative to controls, consistent with the impaired-IL-10 mechanistic model.
- **HLA-B27** positivity has been noted as a susceptibility marker in some cohorts, particularly overlapping spondyloarthropathy phenotypes.

**Environmental/demographic risk factors:** Female sex predominance in classic pediatric CRMO (though a "severe" phenotype subgroup skews male — see Phenotypes below); White/Caucasian ancestry is over-represented in published cohorts, though this likely reflects ascertainment bias rather than true differential susceptibility; family history of autoinflammatory/autoimmune disease (psoriasis, IBD, spondyloarthritis) increases risk.

### Protective Factors
No well-established genetic or environmental protective factors are documented in the literature; this remains an evidence gap.

### Gene–Environment Interactions
Not well characterized for CRMO specifically; the leading hypothesis is that in genetically susceptible individuals (e.g., carrying *P2RX7* or IL-10 promoter risk variants), an as-yet-unidentified triggering stimulus (possibly microbial/microbiome-related, per murine data) precipitates monocyte/macrophage TLR4-MAPK signaling defects and downstream inflammasome activation.

---

## 3. Phenotypes

### Core symptoms and signs
- **Bone pain** — insidious onset, localized, often worse at night, with a waxing-and-waning course (suggest **HP:0002653** Bone pain / **HP:0006414**)
- **Local swelling, tenderness, warmth** over affected bone (suggest **HP:0025378** or general inflammatory swelling terms)
- **Arthritis/synovitis** adjacent to lesions
- **Bone overgrowth/hyperostosis**, particularly clavicular and mandibular (suggest **HP:0004422** Bone hyperostosis)
- **Vertebral compression fractures**, kyphosis, leg-length discrepancy in spinal disease
- Generally **afebrile or low-grade fever**, distinguishing from infectious osteomyelitis in most cases

### Laboratory abnormalities
- Normal-to-mildly-elevated ESR/CRP (a substantial subset show no systemic inflammatory marker elevation)
- Anemia of chronic disease (common)
- Elevated serum cytokines: IL-6, TNF-α (see Mechanism section for full cytokine panel)

### Phenotype characteristics
- **Age of onset:** Peak incidence **7–12 years**, though reported across all pediatric age groups and increasingly recognized in adults (where it overlaps with SAPHO syndrome). Median age of symptom onset in one UK cohort was **12 years**.
- **Severity/progression:** Variable — a **relapsing-remitting or progressive course** is now recognized as more typical than the historically assumed "self-limited" course. Diagnosis delay averages **~15 months (range 0–92 months)** due to low disease awareness (PMID:27576444).
- **Distinct phenotype clusters** (2022 medRxiv study, "Two phenotypes of CRMO"):
  - **Severe phenotype:** predominantly male, multifocal, rare clavicular involvement, prominent inflammatory syndrome
  - **Mild phenotype:** predominantly female, unifocal, common clavicular involvement, minimal systemic inflammation, rare extraosseous lesions
  - **Intermediate phenotype:** predominantly female, multifocal, common inflammatory syndrome, some with family history and extraosseous disease

### Skeletal distribution
- **Most commonly affected sites:** metaphyses/epiphyses of long bones (femur, tibia, humerus), pelvis, clavicle, vertebrae, mandible
- The **clavicle and mandible are distinctively involved in CRMO but rare in bacterial osteomyelitis** — involvement at these sites should raise diagnostic suspicion for CRMO specifically (Radsource; PathologyOutlines).
- Periosteal reaction reported in ~33% of symptomatic sites; radiographic pattern: **50% lytic, 53% sclerotic** lesions in one cohort of 36 patients (Bristol study, PMID:27576444).

### Associated (extra-osseous) manifestations / comorbidities
- **Inflammatory bowel disease (Crohn disease, ulcerative colitis):** ~10% of patients
- **Psoriasis / palmoplantar pustulosis:** ~8–21% (estimates vary by cohort)
- **Severe acne:** ~10%
- **Ankylosing spondylitis / spondyloarthropathy features:** up to ~25% in some series
- **Pulmonary involvement:** 3–8% (German cohort)

### Quality of life impact
Chronic pain and activity restriction (especially with spinal involvement, given vertebral fracture risk) substantially affect quality of life; amplified musculoskeletal pain syndromes can persist even when active inflammation resolves, per longitudinal UK cohort follow-up data.

**Suggested HPO terms:** HP:0002653 (Bone pain), HP:0100774 (Osteomyelitis), HP:0004422 (Hyperostosis), HP:0002758 (Osteoarthritis-adjacent joint involvement), HP:0001369 (Arthritis), HP:0100255 (Long bone bowing — for structural sequelae), HP:0002650 (Scoliosis/kyphosis — vertebral involvement), HP:0004616 (Vertebral wedging/compression), HP:0100785 (Recurrent fractures).

---

## 4. Genetic/Molecular Information

### Causal genes (monogenic forms)
| Gene | HGNC | Disorder | Inheritance | Mechanism |
|---|---|---|---|---|
| LPIN2 | phosphatidic acid phosphatase | Majeed syndrome | AR | Loss of lipin-2 function → dysregulated lipid metabolism, macrophage polarization toward inflammatory M2 phenotype, accelerated osteoclastogenesis |
| IL1RN | IL-1 receptor antagonist | DIRA | AR | Loss of IL-1Ra function → unopposed IL-1α/β signaling |
| PSTPIP1 | proline-serine-threonine phosphatase-interacting protein 1 | PAPA syndrome | AD | Pyrin inflammasome dysregulation, elevated IL-1β |
| FBLIM1 | filamin-binding LIM protein 1 | Non-syndromic CRMO (rare) | AR (reported family) | Impaired RANKL regulation, altered osteoclast differentiation |

### Variant classification and population data
Most reported pathogenic variants in *LPIN2* and *IL1RN* are classified pathogenic/likely pathogenic per ACMG/AMP criteria in ClinVar given clear loss-of-function consequences and segregation in consanguineous pedigrees. *P2RX7* CNO-associated variants are predominantly **rare, missense, presumed-damaging variants** rather than clear loss-of-function alleles; population frequency data (gnomAD-derived control cohorts) show these variants at low but non-zero frequency (~1.9–4.4% carrying rare variants in healthy controls vs. 5.8–32.4% in CNO cohorts), consistent with a **susceptibility/risk-modifier** rather than fully penetrant Mendelian model.

### Functional consequences
- *LPIN2* loss-of-function → gain of inflammatory signaling (M2 macrophage skewing, enhanced osteoclastogenesis)
- *IL1RN* loss-of-function → gain of IL-1 pathway activity (classic loss-of-inhibitor mechanism)
- *P2RX7* risk variants → **gain-of-function-like effect on inflammasome assembly** coupled with **reduced pyroptotic cell death**, prolonging pro-inflammatory monocyte/macrophage activity
- *FBLIM1* loss-of-function → dysregulated RANKL-driven osteoclast differentiation

### Modifier genes
IL-10 promoter haplotype (GCC/ACC/ATA) modulates baseline anti-inflammatory tone and may modify severity/expressivity in sporadic disease.

### Epigenetic information
CRMO monocytes show **reduced DNA methylation** at loci controlling NLRP3 inflammasome components (NLRP3, ASC/PYCARD) and IL-1β, and **reduced histone H3 serine-10 phosphorylation** at the IL-10 promoter — both consistent with an epigenetically reinforced pro-inflammatory monocyte state ([PMC10483435](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10483435/)).

### Chromosomal abnormalities
No recurrent aneuploidies, translocations, or copy-number syndromes are established causes of CRMO; it is not currently modeled as a chromosomal disorder.

**Suggested gene/ontology annotations:** HGNC gene symbols LPIN2, IL1RN, PSTPIP1, FBLIM1, P2RX7, FGR (all lowercase `hgnc:` CURIEs per local convention); GO:0061702 (canonical inflammasome complex), GO:0043123 (positive regulation of NF-kB signaling), GO:0045453 (bone resorption), GO:0030316 (osteoclast differentiation).

---

## 5. Environmental Information

**Environmental factors:** No specific toxin, chemical, or occupational exposure has been robustly linked to CRMO onset; the disease is pediatric-onset in the great majority of cases.

**Lifestyle factors:** Not established as causal; physical activity/trauma to affected long bones can precipitate symptomatic flares once disease is established (mechanical loading is a recognized aggravator, not an initiator).

**Infectious agents:** CRMO is explicitly **non-infectious** and cultures are sterile by definition. However, murine model data (Pstpip2-deficient mice) and some human hypotheses implicate the **microbiome** as a possible disease-modifying or triggering factor via innate immune signaling (TLR activation), rather than a specific causal pathogen — this remains an active but unresolved research area ("New discoveries in CRMO: IL-1β, the neutrophil, and the microbiome implicated in disease pathogenesis in Pstpip2-deficient mice," *Seminars in Immunopathology*).

---

## 6. Mechanism / Pathophysiology

### Causal chain overview
1. **Trigger** (unknown in sporadic disease; monogenic loss-of-function in syndromic forms) →
2. **Defective TLR4/MAPK/ERK1-2 signaling in monocytes** → failure to phosphorylate ERK1/2 → failure to activate Sp-1 transcription factor →
3. **Impaired expression of anti-inflammatory cytokines IL-10 and IL-19** (chromatin/epigenetically mediated) →
4. **Disinhibited NLRP3 inflammasome assembly** (elevated NLRP3, ASC, caspase-1) →
5. **Increased IL-1β and IL-18 secretion** →
6. **RANKL upregulation on osteoblasts/bone marrow macrophages, OPG downregulation** →
7. **Enhanced osteoclast differentiation and activation** →
8. **Bone resorption, sterile inflammatory bone lesions, and secondary reparative hyperostosis/sclerosis**

### Molecular pathways
- **TLR4 → MAPK/ERK → Sp-1 → IL-10/IL-19 transcription** (defective in CRMO monocytes; PMID:22940633)
- **NF-κB and MAPK signaling** downstream of IL-1β, TNF-α, IL-6, IL-8, IL-18 — all converge on osteoclastogenic and pro-inflammatory transcriptional programs (KEGG hsa04621 NOD-like receptor signaling; KEGG hsa04064 NF-kB signaling)
- **JAK-STAT3 signaling** downstream of IL-6, driving Th17 differentiation and IL-17 production
- **RANK/RANKL/OPG axis** — central convergence point for bone resorption

### Cytokine profile (imbalance model)
| Elevated (pro-inflammatory) | Reduced (anti-inflammatory) |
|---|---|
| IL-1β, TNF-α, IL-6, IL-8, IL-18, IL-17, IL-23, IL-20 | IL-10, IL-19, IL-9 |

Elevated serum IL-6 (>17 pg/mL) and eotaxin (>110 pg/mL) have been proposed as a minimal diagnostic biomarker panel with **93% sensitivity and 97% specificity** in preliminary ROC analyses, alongside candidate markers S100A8, collagen Iα, RANTES, and soluble IL-2 receptor ([JBMR 2024 review](https://academic.oup.com/jbmr/article/39/11/1523/7745421)); these require validation in larger independent cohorts.

### Cellular processes
- **Monocyte/macrophage dysfunction** is the central cellular lesion — attenuated TLR4/MAPK signaling, chromatin-level failure of IL-10/IL-19 induction
- **Osteoclast hyperactivation** — RANKL-driven differentiation from monocyte/macrophage precursors
- **Mast cell involvement** — a preclinical study ("Mast Cells Enhance Sterile Inflammation in Chronic Nonbacterial Osteomyelitis," PMC6737947) demonstrated mast cells amplify sterile bone inflammation in the murine model
- **Th17 cell differentiation** — chronic pro-inflammatory cytokine release (IL-6, IL-23) may drive IL-17-expressing effector T cells, further amplifying osteoclastogenesis (adaptive immune contribution to a primarily innate disease)
- **Reduced pyroptosis** in *P2RX7* variant carriers — paradoxically prolongs pro-inflammatory monocyte survival rather than clearing them via cell death

### Tissue damage mechanisms
Cycles of osteolysis (active inflammatory phase) followed by reparative sclerosis/hyperostosis (chronic phase) — this destruction-repair cycle underlies the mixed lytic/sclerotic radiographic appearance and progressive bone overgrowth seen at sites like the clavicle and mandible.

### Immune system involvement
Predominantly **innate immune dysregulation** (monocyte/macrophage/neutrophil axis, inflammasome), with secondary adaptive immune (Th17) amplification; not classically autoimmune (no dominant autoantibody or autoreactive T-cell clone identified).

### Molecular profiling data
- **Genomics:** Whole-exome sequencing has identified *FBLIM1* (familial) and *P2RX7* (cohort-level risk variant) associations
- **Transcriptomics:** Single-cell RNA-sequencing in the *Pstpip2⁻/⁻* mouse model identified co-expression of the lncRNA **Morrbid** with *Pstpip2* in mature myeloid cells (neutrophils, eosinophils, classical monocytes); Morrbid knockout **significantly inhibited CRMO initiation and progression** in this model by reducing inflammatory myeloid cell lifespan and cytokine output (2025, *Disease Models & Mechanisms*, PMID:40503910) — a promising mechanistic and therapeutic lead published very recently.
- **Proteomics/serum biomarker panels:** As above (IL-6, eotaxin, S100A8, RANTES).

### Advanced technologies
Single-cell RNA-seq has been applied in the murine *Pstpip2*-deficient model (Morrbid study) to define myeloid-lineage-specific contributions; equivalent human single-cell/spatial transcriptomic data in bone biopsy tissue remains an area for future research — not yet reported at scale for CRMO.

**Suggested GO terms:** GO:0032640 (TNF production), GO:0032611 (IL-1β production), GO:0032693 (negative regulation of IL-10 production — CRMO shows failure of this), GO:0045453 (bone resorption), GO:0030316 (osteoclast differentiation), GO:0002534 (cytokine production involved in inflammatory response), GO:0061702 (inflammasome complex).
**Suggested CL terms:** CL:0000576 (monocyte), CL:0000235 (macrophage), CL:0000775 (neutrophil), CL:0000097 (mast cell), CL:0000092 (osteoclast), CL:0001051 (CD4-positive, IL-17-secreting Th17 cell).

---

## 7. Anatomical Structures Affected

### Organ level
- **Primary:** Skeletal system — long bone metaphyses (femur, tibia, humerus), clavicle, mandible, pelvis, vertebrae
- **Secondary:** Joints (adjacent arthritis/synovitis), skin (psoriasis, palmoplantar pustulosis, acne), gastrointestinal tract (IBD), lungs (rare, 3-8%)
- **Body systems involved:** Musculoskeletal (primary), integumentary, gastrointestinal, and — in SAPHO overlap — the axial skeleton/sacroiliac joints

### Tissue and cell level
- **Bone tissue:** metaphyseal/epiphyseal trabecular and cortical bone; periosteum (periosteal reaction/new bone formation)
- **Cell populations:** monocytes, macrophages, osteoclasts, neutrophils, mast cells, and — in chronic lesions — lymphocytes, plasma cells, histiocytes

### Subcellular level
Implicated: inflammasome assembly at the cytoplasmic level (NLRP3/ASC/caspase-1 complex — GO Cellular Component: inflammasome complex), plasma membrane P2X7 channel activity.

### Localization
- **UBERON terms (suggested):** UBERON:0002481 (clavicle), UBERON:0002397 (mandible), UBERON:0001474 (bone element), UBERON:0002228 (vertebral column), UBERON:0004538 (long bone metaphysis is not a distinct UBERON term but metaphysis-adjacent structures apply)
- **Lateralization:** Typically **asymmetric/multifocal**, non-contiguous lesions distributed across multiple bones simultaneously — a hallmark distinguishing feature from unifocal bacterial osteomyelitis.

---

## 8. Temporal Development

### Onset
- **Typical age:** Peak 7–12 years; can present at any pediatric age and, less commonly, in adults (where overlap with SAPHO is emphasized)
- **Pattern:** Insidious, gradually worsening bone pain/swelling rather than acute high-fever presentation typical of bacterial osteomyelitis

### Progression
- **Disease course pattern:** Historically viewed as self-limited, but increasingly recognized as **chronic with a relapsing-remitting OR progressive course** — a key revision in current understanding (JBMR 2024 review; UK longitudinal cohort data)
- **Stages:** acute/active inflammatory (lytic) phase → reparative/chronic (sclerotic, hyperostotic) phase, often cycling at the same or different sites over time
- **Duration:** Chronic, potentially lifelong disease activity in a subset; median follow-up studies show many but not all patients eventually reach durable remission

### Patterns
- **Remission:** Can be spontaneous or treatment-induced (NSAID, bisphosphonate, or biologic-associated); >50% of NSAID responders experience a flare at a median of ~29 months despite initial response
- **Relapse:** A UK tertiary center cohort (17 patients, 1999–2015) demonstrated ongoing relapse risk into adolescence/young adulthood requiring long-term rheumatology follow-up
- **Critical periods:** Early diagnosis (median delay currently ~15 months) is emphasized as a window to prevent structural bone damage (vertebral fracture, growth disturbance) before it occurs.

---

## 9. Inheritance and Population

### Epidemiology
- **Incidence (most authoritative recent estimate):** **0.65 per 100,000 person-years** in children <16 in the UK/Republic of Ireland (2024 BPSU national prospective surveillance study, October 2020–November 2022; 288 patients reported, 165 confirmed + 20 probable cases analyzed) ([PMC11962910](https://pmc.ncbi.nlm.nih.gov/articles/PMC11962910/); [Rheumatology Oxford 2025](https://academic.oup.com/rheumatology/article/64/4/2162/7738107)).
- Other national estimates: **0.4 per 100,000 children in Germany**; **2.3 per 100,000 children** in one large catchment area of the northwestern United States; a pooled pediatric estimate of **~0.605 CNO cases per 100,000 person-years** has also been cited (JBMR 2024).
- Historic literature-review estimate: as low as **4 per million children**, though rising with increased clinical recognition — likely reflecting under-ascertainment rather than a true rising incidence.

### For genetic etiology
- **Inheritance pattern:** Sporadic/non-syndromic CRMO is generally considered **complex/multifactorial** (polygenic risk-variant model, e.g., *P2RX7*); the monogenic syndromic forms (Majeed, DIRA, PAPA) follow classic **autosomal recessive** (Majeed, DIRA) or **autosomal dominant** (PAPA, CRMO3) Mendelian inheritance.
- **Penetrance:** Complete/high for monogenic LPIN2/IL1RN loss-of-function alleles; incomplete/variable for P2RX7 and IL-10 haplotype risk variants (risk-modifier model, not deterministic).
- **Consanguinity:** A recognized risk factor for the recessive monogenic forms — the original *FBLIM1* and several *LPIN2* pedigrees were identified in consanguineous families.
- **Carrier frequency:** Not systematically established for *LPIN2*/*IL1RN* given extreme rarity (~24 genetically confirmed Majeed syndrome individuals worldwide reported to date).

### Population demographics
- **Sex ratio:** Overall female predominance in classic pediatric CRMO cohorts, though the "severe/multifocal" phenotype subgroup skews male (see Phenotypes section) — UK longitudinal cohort: 10 female : 7 male.
- **Ethnic/geographic distribution:** White/Caucasian populations most frequently reported in the literature, though this likely reflects study-site bias; global epidemiologic data remain limited. *FBLIM1*-associated CRMO was identified in a South Asian consanguineous family, indicating the disease is not confined to any single ancestry.
- **Age distribution:** Concentrated in the pediatric/adolescent range (peak 7–12 years), with adult-onset presentations increasingly reported (overlapping SAPHO nomenclature).

---

## 10. Diagnostics

### Clinical/laboratory tests
- **Blood tests:** ESR, CRP (often normal-to-mildly elevated — a distinguishing feature versus bacterial osteomyelitis), CBC (anemia of chronic disease)
- **Biomarkers (investigational):** Serum IL-6 + eotaxin panel (93% sensitivity/97% specificity in preliminary studies), S100A8, RANTES, soluble IL-2 receptor — not yet standard of care
- **Bone biopsy/histopathology:** Traditionally required to exclude infection/malignancy; early lesions show neutrophils, lymphocyte clusters, occasional eosinophils; chronic lesions show lymphocytes, plasma cells, histiocytes; established lesions show necrotic bone fragments, fibrosis, increased osteoblasts, and dilated vessels. Cultures are sterile.

### Imaging
- **Plain radiographs:** May be normal early; later show lytic and/or sclerotic lesions with periosteal reaction (Bristol cohort, n=36: 50% lytic, 53% sclerotic, 33% periosteal reaction)
- **Whole-body MRI (WB-MRI): the diagnostic "gold standard."** Detects bone marrow edema on fat-saturated T2/STIR sequences before structural change is visible, and — critically — reveals **clinically silent, radiographically occult multifocal lesions**, establishing the multifocal distribution pattern central to diagnosis and helping exclude alternative diagnoses ([Insights into Imaging 2022](https://link.springer.com/article/10.1186/s13244-022-01288-3); PMID:36114435).
- Bone biopsy may be **avoided** when WB-MRI shows the characteristic multifocal pattern at typical sites (clavicle, mandible, metaphyses) with no systemic infectious signs.

### Diagnostic criteria
Two named clinical criteria sets exist, neither prospectively validated at scale:
- **Jansson criteria** — found to be **more sensitive than Bristol criteria** (OR 3.94, P<0.001)
- **Bristol criteria** — use by an experienced clinician may obviate the need for biopsy in some patients
- **ACR/EULAR candidate classification criteria**, derived from ~450 international cases, are in development/pending final dissemination as of the 2024 JBMR review — representing an important near-term advance in standardized diagnosis.

### Genetic testing
Not routine for sporadic CRMO; recommended when syndromic features suggest Majeed syndrome (congenital dyserythropoietic anemia, neutrophilic dermatosis — test *LPIN2*), DIRA (neonatal pustulosis, extreme inflammatory markers — test *IL1RN*), or PAPA syndrome (pyoderma gangrenosum, cystic acne — test *PSTPIP1*).

### Differential diagnosis
Bacterial/fungal/mycobacterial osteomyelitis, malignancy (Ewing sarcoma, Langerhans cell histiocytosis, leukemia/lymphoma bone involvement), benign bone tumors (osteoid osteoma, bone cysts), other monogenic autoinflammatory disorders (PAPA, DIRA, Majeed syndrome), metabolic bone disease (hypophosphatasia), osteonecrosis, osteopetrosis, juvenile idiopathic arthritis.

---

## 11. Outcome/Prognosis

- **Mortality:** CRMO is not associated with excess mortality; it is a morbidity-driving, not life-threatening, condition.
- **Disease course:** The historically assumed "self-limiting" natural history is now understood to be an **oversimplification** — CRMO frequently follows a **relapsing-remitting or progressive course**, with a substantial proportion of patients experiencing relapses even after apparent remission.
- **Complications:** Vertebral compression fractures, kyphosis/scoliosis, leg-length discrepancy (from growth-plate involvement), progressive bone overgrowth/hyperostosis (clavicle, mandible), and — independent of active inflammation — amplified musculoskeletal pain syndromes that can persist and are treatment-refractory.
- **Prognostic factors:** Multifocal/severe phenotype (male predominant subgroup), spinal involvement, and delayed diagnosis (median 15 months) are associated with greater risk of structural damage.
- **Quality of life:** Chronic pain and activity restriction substantially affect daily functioning; long-term rheumatology follow-up into adulthood is recommended given persistent relapse risk documented in UK tertiary-center cohorts.

---

## 12. Treatment

### First-line
- **NSAIDs** (typically naproxen) — inhibit cyclooxygenase, reducing prostaglandin E–mediated osteoclast activation. Effective in **>60%** of patients over 12–18 months, but **>50% experience a flare** at a median of ~29 months. *(Suggested NCIT: NCIT:C15986 Pharmacotherapy; therapeutic_agent CHEBI-bound NSAID)*

### Second-line / escalation
- **Corticosteroids:** Short courses (e.g., prednisone-equivalent 2 mg/kg/day for 5–10 days, or bridging 0.1–0.2 mg/kg/day); mechanism via phospholipase A2 and NF-κB-regulated cytokine (IL-1, IL-6, TNF-α) inhibition; long-term use limited by adverse-effect burden.
- **Bisphosphonates (pamidronate, zoledronic acid):**
  - Pamidronate: 1 mg/kg/dose (max 60 mg) monthly, or 3 consecutive days every 3 months, for 9–12 months
  - Zoledronic acid: 0.0125–0.025 mg/kg/dose (max 4 mg) every 6–12 months
  - Mechanism: osteoclast apoptosis + reduction of pro-inflammatory cytokine expression
  - Particularly effective for **vertebral involvement**; mean MRI resolution of inflammation ~6 months (range 2–12 months)
  - The **only published RCT in this disease is pamidronate vs. placebo in adults**, underscoring the overall paucity of controlled trial evidence
  - *(NCIT:C15986 Pharmacotherapy; therapeutic_agent CHEBI-bound pamidronate/zoledronic acid)*
- **Conventional DMARDs** (methotrexate, sulfasalazine, leflunomide): increasingly used but with sparse supporting evidence

### Biologics / emerging therapies
- **TNF inhibitors** (adalimumab, infliximab, etanercept): **40–50% remission rates** in European registry data; beneficial for vertebral lesions refractory to pamidronate; **paradoxical psoriasis** is a recognized adverse effect, arguably more common than with other indications; **not currently licensed for CNO/CRMO**. A comparative international multicenter retrospective study (n=91: pamidronate=47, TNFi=22, both sequentially=22) found both therapies associated with clinical remission at 6 months and MRI lesion reduction at 12 months; pamidronate trended toward faster MRI resolution (not statistically significant), while **TNF inhibitors were associated with fewer flares** (PMID:35460903).
- **IL-1 blockade** (anakinra, canakinumab, rilonacept): beneficial for osteitis/arthritis with variable mucocutaneous response; canakinumab produced rapid response in a refractory CRMO-with-pyoderma-gangrenosum case, though efficacy for bone disease waned over time in some reports (PMID:36004431). Majeed syndrome and DIRA patients respond well to IL-1 blockade, supporting mechanistic centrality of this pathway; canakinumab has produced long-lasting remission in Majeed syndrome.
- **IL-17/IL-23 inhibition:** Secukinumab (anti-IL-17A) successfully used in SAPHO patients in some reports but **led to recurrence of osteomyelitis** despite psoriasis non-response in at least one case — efficacy is inconsistent. Ustekinumab (anti-IL-12/23) has shown case-report success for CNO, including resolution of back pain.
- **JAK inhibitors:** Deucravacitinib (TYK2 inhibitor) showed effectiveness in a 2024/2025 case report for CRMO with concomitant psoriasis ([PMC12138201](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12138201/)); tofacitinib shows promise in SAPHO with limited pediatric CNO data.
- **IL-6 blockade** (tocilizumab): mixed results despite IL-6 being a consistent serum biomarker.
- **RANKL inhibition (denosumab):** theoretical potential given RANK/RANKL centrality to mechanism, but no published CNO reports to date.
- **Investigational/preclinical targets:** P2X7 antagonism, NLRP3 inflammasome small-molecule inhibitors (e.g., MCC950), ASC inhibitors (e.g., MM01), IL-18-selective inhibitors, and — from the newest (2025) murine mechanistic work — **targeting the lncRNA Morrbid** to shorten inflammatory myeloid cell lifespan.

### Surgical/other
Surgery is generally reserved for structural complications (e.g., severe vertebral deformity) rather than as primary disease-modifying treatment.

### Treatment strategy / trial design gaps
No treatments are currently FDA/EMA-licensed specifically for CNO/CRMO. Expert consensus prioritizes **IL-1 and IL-17 blockade** as the leading candidate interventions for future controlled trials, with pamidronate as an active comparator. **ACR/EULAR classification criteria and OMERACT core outcome measures are anticipated** as near-term advances that should enable better-powered trials (JBMR 2024 review).

**Suggested NCIT terms:** NCIT:C15986 (Pharmacotherapy), NCIT:C15632 (Chemotherapy — n/a here), NCIT:C49236 (Therapeutic Procedure), NCIT:C15329 (Surgical Procedure — for structural complications), NCIT:C20401 (Monoclonal Antibody — for biologics), NCIT:C2986 (drug class terms per specific agent).

---

## 13. Prevention

- **Primary prevention:** None established — no known modifiable risk factor or vaccination strategy exists, since etiology in sporadic disease remains incompletely defined.
- **Secondary prevention (early detection):** The chief actionable lever is **reducing diagnostic delay** (currently median ~15 months) through greater clinical awareness and appropriate use of whole-body MRI, since earlier treatment initiation is presumed (though not RCT-proven) to reduce risk of structural damage (vertebral fracture, growth disturbance, permanent hyperostosis).
- **Genetic counseling:** Relevant for families with confirmed monogenic disease (Majeed syndrome, DIRA, PAPA) given autosomal recessive/dominant inheritance patterns and availability of single-gene testing; carrier screening/prenatal diagnosis can be discussed in consanguineous families with a confirmed proband mutation.
- **Tertiary prevention:** Activity modification (particularly avoiding high-impact loading with active spinal lesions) to reduce fracture risk; routine surveillance imaging and bloodwork during treatment to catch flares early.

---

## 14. Other Species / Natural Disease

No naturally occurring veterinary counterpart of CRMO in companion animals or wildlife is well documented in the literature surveyed (unlike many Mendelian diseases with OMIA veterinary entries); the disease's key animal correlates are **engineered/spontaneous mouse mutants** (below) rather than natural disease in other species.

---

## 15. Model Organisms

### Murine genetic models (the field's principal disease models)
- ***cmo* (chronic multifocal osteomyelitis) mice** — spontaneous homozygous missense mutation in **Pstpip2** (PMID:16122996); develop sterile osteomyelitis with severe systemic cytokine/chemokine dysregulation, extramedullary hematopoiesis, and inflammatory skin lesions.
- ***lupo* mice** — chemically induced (ENU) homozygous *Pstpip2* mutation with a very similar phenotype to *cmo* mice.
- **Mechanistic insight from these models:** Bone inflammation in *Pstpip2*-deficient mice is **IL-1β-mediated but NLRP3-inflammasome- and caspase-1-independent** — notably different from most other IL-1-mediated autoinflammatory diseases, and an important nuance for interpreting IL-1 pathway targeting ([PNAS](https://www.pnas.org/doi/10.1073/pnas.1318685111); [PMC3903222](https://pmc.ncbi.nlm.nih.gov/articles/PMC3903222/)).
- **Mast cell contribution:** Mast cells enhance sterile inflammation in this model (PMC6737947/biorxiv preprint), implicating a non-myeloid innate immune cell type beyond monocytes/macrophages.
- **Morrbid lncRNA (2025):** Single-cell RNA-seq in *Pstpip2⁻/⁻* mice identified co-expression of the myeloid-restricted long non-coding RNA **Morrbid** with *Pstpip2*; genetic disruption of Morrbid **significantly inhibited CRMO initiation and progression**, mitigating myeloid cell activation and excessive cytokine release — proposed as a novel therapeutic strategy of shortening inflammatory myeloid cell lifespan ([Disease Models & Mechanisms, PMID:40503910](https://pubmed.ncbi.nlm.nih.gov/40503910/); [PMC12309896](https://pmc.ncbi.nlm.nih.gov/articles/PMC12309896/)).
- ***FBLIM1***-related insight originated from **microarray analysis of the *cmo* mouse bone marrow macrophage transcriptome**, which nominated *Fblim1* before the human familial mutation was identified — a model-to-human translational discovery pathway.

### Phenotype recapitulation and limitations
The *Pstpip2*-mutant models recapitulate multifocal sterile osteomyelitis, systemic inflammatory cytokine dysregulation, and skin inflammation, closely mirroring human CRMO/Majeed-spectrum disease. However, they model the **syndromic/PSTPIP-pathway** disease axis specifically; they do not directly model the **P2RX7-variant or IL-10-haplotype-driven sporadic human CRMO** subtype, and — as with most mouse inflammatory models — species differences in innate immune receptor biology and inflammasome regulation limit direct translational certainty (a candidate `HUMAN_MODEL_MISMATCH` consideration for any KB entry: the NLRP3-independence of murine IL-1β-driven disease contrasts with the NLRP3-centric human mechanistic literature).

### Other model systems
- **Zebrafish:** No CRMO-specific zebrafish model was identified in the literature searched, but zebrafish are an established platform for skeletal disorder and innate-immune/notochord-infection modeling generally, and represent a plausible future avenue (real-time imaging of innate immune cells, ease of genetic manipulation) — not yet applied to CRMO specifically per available sources.
- **iPSC/organoid models:** No CRMO-specific iPSC-derived or organoid models were identified in the current literature — a research gap.

### Resources
MGI (Mouse Genome Informatics) for *Pstpip2* allele records (*cmo*, *lupo*); no dedicated CRMO patient-derived cell biobank was identified in this search.

---

## Summary of Key Evidence Gaps (for curation prioritization)

1. **No licensed treatment** exists for CNO/CRMO; only one RCT (pamidronate vs. placebo, adults) has been conducted.
2. **ACR/EULAR classification criteria** are in development but not yet finalized/published in final form.
3. Sporadic (non-syndromic) CRMO genetics remain **largely unresolved** — *P2RX7* explains only a minority of cases.
4. The **NLRP3-independence** of the leading murine model (*Pstpip2*-deficient mice) versus the NLRP3-centric human mechanistic literature is a notable model-translatability nuance.
5. Biomarker panels (IL-6/eotaxin) require **independent validation** before clinical adoption.
6. Long-term natural history / outcome data beyond adolescence remain sparse — most cohorts are pediatric-center-based with limited adult follow-up.

---

## Sources

- [A Case of Chronic Recurrent Multifocal Osteomyelitis (CRMO) - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11578638/)
- [Chronic Recurrent Multifocal Osteomyelitis: A Review of the Noninfectious Inflammatory Bone Disease and Lessons for More Timely Diagnosis - PubMed](https://pubmed.ncbi.nlm.nih.gov/35876774/)
- [Chronic recurrent multifocal osteomyelitis in pediatric patients: A Chinese single center observational study and literature review](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11630947/)
- [Chronic Recurrent Multifocal Osteomyelitis (CRMO): Presentation, Pathogenesis, and Treatment - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5705736/)
- [Chronic Recurrent Multifocal Osteomyelitis: A Comprehensive Literature Review - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10483435/)
- [Chronic recurrent multifocal osteomyelitis. A narrative and pictorial review - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9441751/)
- [Chronic recurrent multifocal osteomyelitis: diagnosis and treatment - PubMed](https://pubmed.ncbi.nlm.nih.gov/33278106/)
- [Chronic Recurrent Multifocal Osteomyelitis (CRMO) | American College of Rheumatology](https://rheumatology.org/patients/chronic-recurrent-multifocal-osteomyelitis-crmo)
- [improved understanding of pediatric chronic nonbacterial osteomyelitis pathophysiology informs current and future treatment | JBMR 2024](https://academic.oup.com/jbmr/article/39/11/1523/7745421)
- [TNF-inhibitors or bisphosphonates in chronic nonbacterial osteomyelitis? International retrospective multicenter study - PubMed](https://pubmed.ncbi.nlm.nih.gov/35460903/)
- [Ustekinumab as a novel treatment of chronic nonbacterial osteomyelitis: a case report](https://acr.amegroups.org/article/view/12077/html)
- [Treatment of Chronic Nonbacterial Osteomyelitis with Bisphosphonates | Indian Journal of Pediatrics](https://link.springer.com/article/10.1007/s12098-023-04688-5)
- [Inflammasome-independent IL-1β mediates autoinflammatory disease in Pstpip2-deficient mice | PNAS](https://www.pnas.org/doi/10.1073/pnas.1318685111)
- [A missense mutation in pstpip2 is associated with the murine autoinflammatory disorder chronic multifocal osteomyelitis - PubMed](https://pubmed.ncbi.nlm.nih.gov/16122996/)
- [Recessive coding and regulatory mutations in FBLIM1 underlie the pathogenesis of CRMO - PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0169687)
- [Disruption of Morrbid alleviates autoinflammatory osteomyelitis in Pstpip2-deficient mice - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12309896/)
- [Chronic nonbacterial osteomyelitis: the role of whole-body MRI - Insights into Imaging](https://link.springer.com/article/10.1186/s13244-022-01288-3)
- [Chronic nonbacterial osteomyelitis - clinical and magnetic resonance imaging features - PubMed](https://pubmed.ncbi.nlm.nih.gov/33033917/)
- [Current and future advances in practice: SAPHO syndrome and chronic non-bacterial osteitis (CNO) | Rheumatology Advances in Practice](https://academic.oup.com/rheumap/article/8/4/rkae114/7822209)
- [The role of cytokines in the pathogenesis of SAPHO syndrome - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11402674/)
- [Attenuated TLR4/MAPK signaling in monocytes from patients with CRMO results in impaired IL-10 expression - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1521661612001878)
- [Altered expression of IL-10 family cytokines in CRMO result in enhanced inflammasome activation - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4597083/)
- [OMIM #259680 CHRONIC RECURRENT MULTIFOCAL OSTEOMYELITIS 3; CRMO3](https://www.omim.org/entry/259680)
- [OMIM #612852 CHRONIC RECURRENT MULTIFOCAL OSTEOMYELITIS 2, WITH PERIOSTITIS AND PUSTULOSIS; CRMO2](https://omim.org/entry/612852)
- [OMIM #609628 MAJEED SYNDROME](https://www.omim.org/entry/609628)
- [Novel Majeed Syndrome–Causing LPIN2 Mutations Link Bone Inflammation to Inflammatory M2 Macrophages and Accelerated Osteoclastogenesis - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8252456/)
- [P2RX7 gene variants associate with altered inflammasome assembly and reduced pyroptosis in chronic nonbacterial osteomyelitis (CNO) - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0896841124000179)
- [Incidence of chronic recurrent multifocal osteomyelitis in children and adolescents in the UK and Republic of Ireland - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11962910/)
- [Incidence of chronic recurrent multifocal osteomyelitis in children and adolescents in the UK and Republic of Ireland | Rheumatology, Oxford Academic](https://academic.oup.com/rheumatology/article/64/4/2162/7738107)
- [BPSU study - Chronic recurrent multifocal osteomyelitis/chronic nonbacterial osteomyelitis (CRMO/CNO) | RCPCH](https://www.rcpch.ac.uk/work-we-do/bpsu/study-crmo)
- [Two phenotypes of Chronic Recurrent Multifocal Osteomyelitis with different patterns of bone involvement - medRxiv](https://www.medrxiv.org/content/10.1101/2022.05.10.22274859.full.pdf)
- [Chronic recurrent multifocal osteomyelitis (CRMO) – advancing the diagnosis - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5006369/)
- [Retrospective Review of 80 Patients with Chronic Recurrent Multifocal Osteomyelitis Evaluated by Pediatric Orthopaedic Surgeons - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2768276524005029)
- [Mast Cells Enhance Sterile Inflammation in Chronic Nonbacterial Osteomyelitis - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6737947/)
- [Case Report: Effectiveness of deucravacitinib in chronic recurrent multifocal osteomyelitis and concomitant psoriasis - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12138201/)
- [Canakinumab treatment in a young girl with refractory chronic recurrent multifocal osteomyelitis associated with pyoderma gangrenosum - PubMed](https://pubmed.ncbi.nlm.nih.gov/36004431/)
- [Choosing the right animal model for osteomyelitis research: Considerations and challenges - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10716383/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 31 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 31 |
| On topic | 26 |
| Off topic | 0 |

All extracted references resolved successfully.