---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-15T19:10:28.513728'
end_time: '2026-08-15T19:16:25.435996'
duration_seconds: 356.92
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Blue Cone Monochromacy
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
  web_search_requests: 21
  num_turns: 23
  total_cost_usd: 2.2581312
  session_id: 8ebdbdea-f16d-5e75-8ed9-a88b56851407
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 50
reference_validation:
  total_references: 20
  verified: 20
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Blue Cone Monochromacy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Blue Cone Monochromacy** covering all of the
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

I'll research Blue Cone Monochromacy now using web search and fetch tools, then compile the full report.

# Blue Cone Monochromacy: Comprehensive Research Report

## 1. Disease Information

### Overview
Blue cone monochromacy (BCM) is a rare, congenital, X-linked recessive retinal disorder characterized by absent or severely reduced function of the long-wavelength (L, "red") and middle-wavelength (M, "green") sensitive cone photoreceptors, with preserved function of short-wavelength (S, "blue") cones and rods. It is sometimes classified as an "incomplete" or "atypical" form of achromatopsia, or as X-linked congenital cone dysfunction. Patients typically present at birth or in early infancy with poor visual acuity, pendular nystagmus, photophobia, myopia, and severely impaired color discrimination limited largely to the blue range of the spectrum ([Wikipedia](https://en.wikipedia.org/wiki/Blue-cone_monochromacy); [Vision Research review](https://www.sciencedirect.com/science/article/pii/S0042698923000457)).

### Key Identifiers
- **OMIM:** #303700 (Blue Cone Monochromacy; BCM) — phenotype entry; causal genes OPN1LW (*300822), OPN1MW (*300821), and the locus control region (LCR; *300824) ([OMIM 303700](https://omim.org/entry/303700); [OMIM 300822](https://omim.org/entry/300822); [OMIM 300821](https://omim.org/entry/300821))
- **Orphanet (ORPHA):** ORPHA:16 — "Blue cone monochromatism," prevalence class 1–9/100,000, X-linked recessive, infancy onset ([Orphanet](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Lng=GB&Expert=16))
- **MONDO:** MONDO:0010563
- **ICD-10-CM:** H53.5x (Color vision deficiencies); frequently cross-coded/grouped with H53.51 (Achromatopsia) since ICD-10-CM has no dedicated BCM code
- **MeSH/GARD synonym entry:** "Cone monochromatism" (NIH GARD) ([GARD](https://rarediseases.info.nih.gov/diseases/917/cone-monochromatism))
- **GeneReviews-adjacent resource:** Achromatopsia GeneReviews chapter discusses BCM in differential diagnosis ([NCBI Bookshelf NBK1418](https://www.ncbi.nlm.nih.gov/books/NBK1418/))

### Synonyms and Alternative Names
- X-linked incomplete achromatopsia / atypical achromatopsia
- S-cone monochromacy (informal; technically S-cones and rods are the only functioning photoreceptors)
- X-linked cone dysfunction syndrome
- Pi-1 pigment deficiency / "blue monochromatism" (historical terms)

The condition was first clinically described by J. Huddart in 1777, and typical vs. "atypical" (incomplete) achromatopsia was distinguished by Sloan in 1942 based on inheritance pattern; the molecular genetic basis at the OPN1LW/OPN1MW locus was established by Nathans and colleagues in 1989 and 1993 ([Wikipedia](https://en.wikipedia.org/wiki/Blue-cone_monochromacy); [Nathans et al., Science 1989](https://www.science.org/doi/10.1126/science.2788922)).

### Data Source Type
Information is derived predominantly from **aggregated disease-level resources**: peer-reviewed case series and genotype-phenotype cohort studies (tertiary academic centers, e.g., University of Pennsylvania Center for Hereditary Retinal Degenerations), Orphanet/OMIM curated summaries, and molecular genetics literature — rather than large-scale EHR datasets, reflecting BCM's rarity (~1/100,000).

---

## 2. Etiology

### Disease Causal Factors
BCM is caused **exclusively by genetic mechanisms** — combined loss of function of both the OPN1LW and OPN1MW genes at Xq28. There are no known environmental, infectious, or acquired causes; it is a purely Mendelian, monogenic (locus-level) disorder. Three principal molecular mechanisms account for essentially all cases ([Gardner et al., Mol Vis 2009, PMID:19421413](https://pmc.ncbi.nlm.nih.gov/articles/PMC2676201/)):

1. **Locus control region (LCR) deletions (~40% of families):** Deletion of the LCR, located 3.1–3.7 kb upstream of the OPN1LW transcription start site, abolishes transcriptional activation of an otherwise structurally normal L/M opsin gene array. Because the LCR is the sole enhancer shared by the entire tandem gene array, its loss silences all downstream opsin genes ([Gardner et al. 2009](https://pmc.ncbi.nlm.nih.gov/articles/PMC2676201/); [OMIM 300824](https://omim.org/entry/300824)).
2. **Hybrid gene formation + inactivating point mutation (~55–60% of families):** Nonallelic homologous recombination (NAHR) between the highly homologous (>98% identical) OPN1LW and OPN1MW sequences reduces the array to a single gene (often an L/M hybrid), which then acquires an inactivating missense or nonsense mutation. The most common recurrent point mutations are **Cys203Arg (C203R)**, **Arg247Ter (R247X)**, and **Pro307Leu (P307L)**; C203R disrupts a disulfide bond required for opsin folding and is the single most frequent BCM-causing variant ([IOVS C203R study](https://iovs.arvojournals.org/article.aspx?articleid=2717851); [Gardner et al. 2009](https://pmc.ncbi.nlm.nih.gov/articles/PMC2676201/)).
3. **Exon deletions / rare interchange (mosaic) haplotypes (uncommon):** Deletion of individual exons (e.g., exon 2 or exon 3) within the single remaining opsin gene, or rare L/M "interchange" haplotypes generated by gene conversion at polymorphic exon-3 positions, can also abolish function ([Gardner et al. 2009](https://pmc.ncbi.nlm.nih.gov/articles/PMC2676201/); [Sci Rep, Ueno et al. 2018](https://www.nature.com/articles/s41598-018-29891-9)).

Large de novo structural deletions spanning the entire LCR–gene-cluster region (e.g., a documented 73,128-bp deletion) have also been reported as sporadic events ([BMC Med Genet 2018](https://bmcmedgenet.biomedcentral.com/articles/10.1186/s12881-018-0623-8)), and high-resolution microarray studies have revealed a broader landscape of complex Xq28 structural variants (deletions, duplications, and combined rearrangements) than previously appreciated ([PNAS 2022, PMC9271157](https://pmc.ncbi.nlm.nih.gov/articles/PMC9271157/)).

### Risk Factors
- **Genetic:** Male sex (hemizygosity for the single X chromosome) is the dominant risk factor; any pathogenic variant fully inactivating both OPN1LW and OPN1MW function confers disease. Family history of X-linked color vision deficiency/BCM in maternal male relatives is a strong indicator.
- **Founder/recurrent mutations:** The C203R hybrid-gene mutation and several recurrent LCR deletions behave as founder mutations recurring across unrelated families of diverse ancestry, reflecting the intrinsic recombination-prone architecture of the locus rather than a single ancestral haplotype in most populations; specific founder haplotypes (e.g., a complex 3-kb LCR deletion plus an inserted aberrant OPN1MW gene) have been documented in individual pedigrees ([PubMed 26153062](https://pubmed.ncbi.nlm.nih.gov/26153062/)).
- **Locus architecture as an intrinsic risk factor:** The tandem, near-identical (>98%) sequence homology between OPN1LW and OPN1MW predisposes the region to frequent unequal (nonallelic homologous) recombination and gene conversion, independently of any external exposure — this structural instability is itself the principal "risk factor" driving new mutational events in the population ([ScienceDirect OPN1MW overview](https://www.sciencedirect.com/topics/neuroscience/opn1mw)).
- **Environmental/lifestyle:** None identified; BCM is not associated with toxins, occupational exposures, maternal illness, or age-related risk.

### Protective Factors
No genetic or environmental protective factors are described in the literature; because BCM is a fully penetrant loss-of-function disorder in hemizygous males, there is no known modifier that prevents disease expression once both opsin genes are inactivated. In carrier females, retention of a normal X chromosome (and favorable X-inactivation ratios) is protective against full phenotypic expression (see Section 9).

### Gene-Environment Interactions
No gene-environment interactions have been established; BCM is a purely monogenic, cell-autonomous photopigment-deficiency disorder unaffected by diet, toxins, or infection.

---

## 3. Phenotypes

### Core Phenotype Set (with suggested HPO terms)

| Phenotype | Type | Onset/Course | Frequency | Suggested HPO term |
|---|---|---|---|---|
| Severely impaired color vision (blue-cone/tritan-only discrimination) | Symptom/clinical sign | Congenital, stationary | Universal (defining feature) | HP:0000551 (Impaired color vision) / HP:0007663 (Reduced visual acuity) related terms; consider HP:0000546 (Blindness) not applicable — use color-vision-specific term |
| Reduced visual acuity (20/60–20/200; 6/24–6/60) | Clinical sign | Congenital, may slowly worsen | Universal | HP:0000572 (Visual impairment) / HP:0000505 (Visual impairment) |
| Pendular nystagmus | Clinical sign | Infantile onset, may improve with age | Very frequent | HP:0000640 (Nystagmus) / HP:0001348 (Pendular nystagmus) |
| Photophobia / hemeralopia (day blindness) | Symptom | Congenital, may persist | Very frequent | HP:0000613 (Photophobia) |
| Myopia (often high/progressive) | Clinical sign | Childhood onset | Frequent–very frequent | HP:0000545 (Myopia) / HP:0011003 (High myopia) |
| Foveal ellipsoid zone (EZ) disruption on OCT | Imaging/laboratory finding | Present from early childhood | Frequent | (no direct HPO; map to macular imaging findings, e.g., HP:0007675 "Retinal atrophy" for advanced changes) |
| Progressive foveal/macular thinning and atrophy (later in life) | Clinical sign, progressive | Adolescent/adult onset, slowly progressive | Occasional–frequent (reported in older cohorts) | HP:0000608 (Macular atrophy) |
| Preserved tritan (blue-yellow) discrimination | Clinical sign | Congenital | Universal (distinguishing feature) | — |
| Absent 30-Hz photopic (L/M cone) ERG with normal/near-normal rod ERG | Laboratory abnormality | Congenital, stationary in most | Universal | HP:0000550 (Abnormal electroretinogram) |

### Phenotype Characteristics
- **Age of onset:** Congenital/early infancy — most children present by 3–6 months with nystagmus, photophobia, and poor fixation ([Wikipedia](https://en.wikipedia.org/wiki/Blue-cone_monochromacy); [Vision Research review](https://www.sciencedirect.com/science/article/pii/S0042698923000457)).
- **Severity:** Visual acuity ranges from roughly 20/60 to 20/200 (6/24–6/60), generally better than complete (rod) achromatopsia (typically 20/200 or worse) ([Mol Vis 2009](https://pmc.ncbi.nlm.nih.gov/articles/PMC2676201/)).
- **Progression:** BCM has traditionally been considered a **stationary** cone dysfunction syndrome, but longitudinal OCT and psychophysical studies show a **slow, progressive component** in a subset of patients, particularly with advancing age — progressive thinning of the foveal outer nuclear layer (ONL), shortening of cone outer segments, and eventual macular atrophy in older individuals ([Michaelides et al., PMID:15094734](https://pubmed.ncbi.nlm.nih.gov/15094734/); [Ophthalmology Science OCT study, PMC9521040](https://pmc.ncbi.nlm.nih.gov/articles/PMC9521040/)). Genotype strongly influences the rate of progression: patients with the **C203R missense mutation** show markedly slower, decades-longer preservation of foveal ONL thickness and delayed ellipsoid-zone (IS/OS) disruption compared with patients carrying **large deletion mutations**, who progress to outer retinal atrophy considerably faster ([IOVS, "C203R Missense Mutation or Large Deletion Mutations"](https://iovs.arvojournals.org/article.aspx?articleid=2717851)).
- **Frequency of individual signs:** Nystagmus and photophobia are near-universal at presentation; nystagmus amplitude frequently decreases (but rarely fully resolves) with age. Myopia, often significant, is very common and is a useful distinguishing feature from achromatopsia (in which hyperopia is more typical).

### Quality of Life Impact
Reduced visual acuity, glare sensitivity, and profound color-vision loss impair reading, mobility, driving eligibility, and educational/occupational tasks requiring color discrimination. Clinical-trial-readiness studies have specifically developed and validated **reading performance** and **color vision** outcome measures for BCM populations, reflecting the functional impact on literacy and daily tasks ([TVST Reading Performance study, PMC7726588](https://pmc.ncbi.nlm.nih.gov/articles/PMC7726588/); [TVST Color Vision Outcome Measures](https://tvst.arvojournals.org/article.aspx?articleid=2785310)). Photophobia and nystagmus further affect outdoor mobility and can carry psychosocial burden in childhood.

---

## 4. Genetic/Molecular Information

### Causal Genes
- **OPN1LW** (Opsin 1, Long-Wave-Sensitive; red/L-cone opsin) — OMIM *300822, Xq28
- **OPN1MW** (Opsin 1, Medium-Wave-Sensitive; green/M-cone opsin) — OMIM *300821, Xq28
- **Locus Control Region (LCR)** — OMIM *300824, a *cis*-regulatory element (not itself protein-coding) located 3.1–3.7 kb 5′ of the gene array, required in *trans*-independent fashion for expression of both downstream genes.

Both BCM causal genes must lose function (combined L+M opsin loss) for the phenotype to manifest; loss of only one gene produces ordinary red-green color blindness (protanopia/deuteranopia), not BCM.

### Gene Structure and Regulation
OPN1LW and OPN1MW are arranged head-to-tail in a tandem array on Xq28, sharing >98% sequence identity (including introns) and only ~19 differing amino acids between the encoded L and M opsins (~96% protein identity), while both are only ~40% homologous to the S-cone opsin gene OPN1SW ([Wikipedia](https://en.wikipedia.org/wiki/Blue-cone_monochromacy)). A single LCR located upstream of the array physically loops to interact with the proximal promoter of either the OPN1LW gene or one of the OPN1MW copies, enforcing **mutually exclusive, stochastic expression of a single opsin gene per cone photoreceptor**; the LCR's regulatory reach is limited to roughly the first two genes in the array, explaining why extra downstream OPN1MW copies are transcriptionally silent in normal individuals ([Vision Research review](https://www.sciencedirect.com/science/article/pii/S0042698923000457)).

### Pathogenic Variant Categories
- **Variant classification (ACMG/AMP):** Recurrent nonsense (R247X) and structurally disruptive missense variants (C203R — disrupts a conserved disulfide bond) are classified as pathogenic in ClinVar; large deletions of the LCR or gene array are similarly pathogenic ([ClinVar RCV000011249](https://www.ncbi.nlm.nih.gov/clinvar/RCV000011249/)).
- **Variant types:** Large structural deletions (LCR, whole gene, or gene-cluster deletions), missense (C203R, P307L), nonsense (R247X), exonic deletions, and rare exon-3 interchange/hybrid alleles.
- **Allele frequency:** BCM-causing variants are individually very rare/private or recurrent-but-low-frequency in population databases (gnomAD), consistent with an X-linked disorder under purifying selection in affected males; specific population allele frequencies for LCR deletions or C203R are not well captured in standard gnomAD summary statistics due to the structural complexity of the locus (segmental duplication/homology confounds short-read mapping).
- **Origin:** Predominantly germline; can be inherited from a carrier mother or arise as a **de novo** structural event (documented de novo 73-kb deletions) in sporadic cases with no family history ([BMC Med Genet 2018](https://bmcmedgenet.biomedcentral.com/articles/10.1186/s12881-018-0623-8)).
- **Functional consequence:** Loss of function — either complete transcriptional silencing (LCR/array deletion) or loss of functional opsin protein (misfolding/instability from missense variants such as C203R, or truncation from nonsense variants).

### Modifier Genes
No independent modifier genes are firmly established, but **genotype at the primary BCM locus itself acts as a phenotypic modifier of progression rate** (C203R vs. deletion genotypes, above). A single case report describes a **digenic-like interaction** between OPN1LW/OPN1MW variants and a concomitant GPR143 variant (the ocular albinism gene) producing BCM with superimposed foveal hypoplasia, illustrating how a second unrelated X-linked locus can modify the retinal phenotype in an individual patient ([PMC8395340](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8395340/)).

### Epigenetic Information
The defining regulatory mechanism of the normal locus (LCR-driven, X-inactivation-coupled, single-active-gene choice per cone) is itself an epigenetic/allelic-exclusion phenomenon. In carrier females, random X-chromosome inactivation (XCI) determines which X-linked opsin allele is expressed in each cone, and **skewed XCI** toward the mutant allele is the proposed mechanism underlying variable, sometimes symptomatic, carrier phenotypes (see Section 9) ([PubMed 22998501](https://pubmed.ncbi.nlm.nih.gov/22998501/)). No disease-specific DNA methylation or histone-modification signature has been characterized beyond this XCI mechanism.

### Chromosomal Abnormalities
BCM is caused by submicroscopic structural variants (kilobase-scale deletions/duplications/rearrangements) rather than classical whole-chromosome aneuploidy or large cytogenetically visible translocations. High-resolution microarray and long-read sequencing studies have revealed a broader-than-expected landscape of complex Xq28 rearrangements (combined deletions, duplications, and inversions) at this locus in BCM patients and carriers ([PNAS 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9271157/); [PubMed 26153062](https://pubmed.ncbi.nlm.nih.gov/26153062/)).

---

## 5. Environmental Information

BCM is a purely genetic disorder with **no established environmental, lifestyle, or infectious contributing factors**. No toxin, occupational exposure, dietary factor, or pathogen has been implicated in either causing BCM or modifying its severity. This section is not applicable beyond noting the absence of such associations in the literature reviewed.

---

## 6. Mechanism / Pathophysiology

### Causal Chain
1. **Molecular trigger:** LCR deletion, hybrid-gene formation with inactivating point mutation, or exonic deletion → loss of functional L- and M-opsin (photopigment) protein expression in cone photoreceptors that would normally express OPN1LW or OPN1MW.
2. **Cellular consequence:** L- and M-cones fail to synthesize functional visual pigment. Because opsin apoprotein (in complex with 11-cis-retinal) is required for normal outer segment disc morphogenesis and stability, "opsin-null" cones **fail to elaborate normal outer segments** and are structurally compromised from early development, even though the cell bodies may initially survive ([Vision Research review](https://www.sciencedirect.com/science/article/pii/S0042698923000457); [PubMed 20638402](https://pubmed.ncbi.nlm.nih.gov/20638402/) — "Deletion of the X-linked opsin gene array locus control region (LCR) results in disruption of the cone mosaic").
3. **Downstream degeneration:** Over time, opsin-deficient L/M cones undergo progressive dysfunction and, in a genotype-dependent manner, degeneration — with slower attrition in C203R (a partially foldable/mistrafficked missense protein may retain some residual structural support) versus faster attrition in complete-deletion genotypes (no protein product at all) ([IOVS C203R study](https://iovs.arvojournals.org/article.aspx?articleid=2717851)).
4. **Tissue-level outcome:** Progressive thinning of the foveal outer nuclear layer, ellipsoid zone (inner segment/outer segment junction) disruption on OCT, and eventual foveal/macular atrophy in a subset of older patients — while S-cones and rods, whose opsin genes (OPN1SW, RHO) are unaffected, remain structurally and functionally intact, preserving blue-cone and scotopic (rod) vision ([Ophthalmology Science OCT comparison, PMC9521040](https://pmc.ncbi.nlm.nih.gov/articles/PMC9521040/)).
5. **Clinical manifestation:** The combination of absent L/M-cone signal with intact S-cone and rod signal produces the clinical triad of severe red-green (and functionally near-total) color vision loss, reduced but non-zero visual acuity (mediated by residual S-cones/rods and the small central S-cone-free zone), nystagmus (from poor foveal fixation input in infancy), photophobia (relative rod/S-cone over-stimulation without normal L/M gain control), and myopia (a common secondary refractive association in congenital cone dysfunction syndromes).

### Upstream vs. Downstream Mechanisms
- **Upstream (initiating):** Genomic structural/point mutation events at the OPN1LW/OPN1MW/LCR locus (germline or de novo).
- **Midstream:** Failure of opsin transcription/translation/protein folding → absent or non-functional visual pigment.
- **Downstream:** Cone outer segment morphogenesis failure → progressive (genotype-dependent) foveal cone structural loss → clinical visual/color phenotype, with the latest downstream event being macular atrophy in a subset of aging patients.

### Cell Types and Biological Processes Involved
- **Cell types:** Long-wavelength-sensitive cone photoreceptor; medium-wavelength-sensitive cone photoreceptor (both spared: short-wavelength-sensitive cone photoreceptor and rod photoreceptor). Suggested **Cell Ontology (CL)** terms: CL:0000573 (retinal cone cell), with L/M-cone subtype distinctions less finely resolved in CL; CL:0000604 (retinal rod cell) for the spared population.
- **Biological processes (GO terms):** 
  - GO:0007601 (visual perception)
  - GO:0016038 (absorption of visible light) / GO:0009583 (detection of light stimulus)
  - GO:0007602 (phototransduction)
  - GO:0035845 (photoreceptor cell outer segment organization)
  - GO:0046549 (retinal cone cell development)
  - GO:0006355 (regulation of transcription, DNA-templated) — for LCR enhancer function
- **Molecular function:** GO:0008020 (G-protein coupled photoreceptor activity) — opsin as a light-activated GPCR.

### Protein Dysfunction
- **Loss of function** is the unifying mechanism: complete absence of opsin protein (deletion genotypes) or an unstable/misfolded, functionally null opsin (C203R disrupts a disulfide bond critical for correct tertiary folding of the seven-transmembrane opsin GPCR, leading to endoplasmic reticulum retention/degradation and failure to reach or function properly in the outer segment membrane) ([IOVS C203R study](https://iovs.arvojournals.org/article.aspx?articleid=2717851); [JCI Insight, "Structural and functional rescue of cones carrying...C203R"](https://insight.jci.org/articles/view/172834)). No gain-of-function or dominant-negative mechanism is implicated.

### Molecular Profiling / Advanced Technologies
Given BCM's rarity and the technical difficulty of live human cone-transcriptomic sampling, most molecular characterization has relied on: (a) targeted long-range PCR, Southern blotting, and microarray/optical genome mapping of the Xq28 locus to resolve structural variants ([PNAS 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9271157/); [PubMed 26153062](https://pubmed.ncbi.nlm.nih.gov/26153062/)); (b) high-resolution adaptive optics and OCT imaging as an in vivo structural proxy for cone survival ([Ophthalmology Science, PMC9521040](https://pmc.ncbi.nlm.nih.gov/articles/PMC9521040/)); and (c) mouse-model transcriptomic/histologic studies of engineered Opn1mw-null and C198R-knock-in retinas (the murine equivalent of human C203R) to dissect degeneration kinetics ([Communications Biology 2025](https://www.nature.com/articles/s42003-025-09045-0); [PMC12036465](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12036465/)). No large-scale human single-cell/spatial transcriptomic or CRISPR functional-genomics dataset specific to BCM was identified in this search.

---

## 7. Anatomical Structures Affected

### Organ Level
- **Primary organ:** Eye (retina), specifically the **posterior pole/macula/fovea**, where cone density is highest.
- **Secondary/complications:** Secondary refractive changes (myopia); no major involvement of other organ systems — BCM is an isolated, non-syndromic ocular disorder (except in rare digenic cases with concurrent albinism-related genes producing additional anterior-segment/foveal hypoplasia features).
- **Body system:** Visual system / sensory nervous system.

Suggested **UBERON** terms: UBERON:0000966 (retina), UBERON:0001782 (fovea centralis), UBERON:0001789 (macula lutea).

### Tissue and Cell Level
- **Tissue:** Neurosensory retina, specifically the outer retina (photoreceptor layer) and outer nuclear layer.
- **Cell populations:** L-cone photoreceptors and M-cone photoreceptors (primarily affected/lost); S-cone photoreceptors and rod photoreceptors (spared). Suggested **CL** term: CL:0000573 (retinal cone cell); more specific L/M vs. S subtypes are not yet finely distinguished in CL nomenclature but can be annotated via free-text qualifiers.

### Subcellular Level
- **Cellular compartments:** Cone outer segment (site of opsin protein localization and phototransduction) is structurally deficient/absent in affected cones; endoplasmic reticulum (site of opsin misfolding/retention for missense variants like C203R). Suggested **GO Cellular Component** terms: GO:0001750 (photoreceptor outer segment), GO:0005783 (endoplasmic reticulum).

### Localization
- **Site:** Central retina/fovea, where cone density is greatest and where visual acuity loss and OCT abnormalities are most pronounced and earliest to progress to atrophy.
- **Laterality:** Bilateral and symmetric, consistent with a systemic (whole-body, X-linked) genetic mechanism rather than a focal or asymmetric insult.

---

## 8. Temporal Development

### Onset
- **Age of onset:** Congenital — signs (nystagmus, poor fixation, photophobia) typically noted in the first months of life; formal diagnosis often made in early-to-mid childhood once color vision and acuity can be more precisely tested ([Vision Research review](https://www.sciencedirect.com/science/article/pii/S0042698923000457)).
- **Onset pattern:** Congenital/insidious — present from birth rather than an acute event.

### Progression
- **Disease course pattern:** Historically classified as a **stationary** congenital cone dysfunction syndrome, but longitudinal cohort and OCT studies demonstrate a **slow, genotype-dependent progressive component** in many patients, particularly evident by young-to-mid adulthood, with foveal ONL thinning, ellipsoid zone disruption, and in a minority of patients (~3% in one comparative OCT cohort) frank macular atrophy at later ages ([Michaelides et al. PMID:15094734](https://pubmed.ncbi.nlm.nih.gov/15094734/); [Ophthalmology Science, PMC9521040](https://pmc.ncbi.nlm.nih.gov/articles/PMC9521040/)).
- **Progression rate:** Variable by genotype — C203R-associated disease progresses markedly more slowly (foveal ONL preserved for decades longer) than large-deletion-associated disease, which shows earlier ellipsoid-zone loss ([IOVS C203R study](https://iovs.arvojournals.org/article.aspx?articleid=2717851)).
- **Disease duration:** Chronic, lifelong — there is no spontaneous resolution of the underlying cone dysfunction, though nystagmus amplitude often lessens with age.

### Patterns
- **Remission:** No spontaneous remission of the underlying color/acuity deficit; nystagmus may clinically improve/dampen with age even though the molecular lesion is unchanged.
- **Critical periods:** The developing visual system in infancy (fixation, nystagmus circuitry) is a period of particular clinical relevance, and any future gene-replacement therapy is hypothesized to have the greatest benefit if administered **before substantial cone structural loss has occurred** — mouse studies indicate a shrinking "therapeutic window" for AAV-mediated rescue with increasing age/degeneration ([PMC12036465, "Molecular Mechanisms Limiting the Therapeutic Window of AAV Gene Therapy in Mouse Models of BCM"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12036465/)).

---

## 9. Inheritance and Population

### Epidemiology
- **Prevalence:** Estimated at approximately **1 in 100,000** individuals overall, with Orphanet classifying prevalence as 1–9 per 100,000 ([Orphanet ORPHA:16](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Lng=GB&Expert=16)); some sources cite a male incidence range of roughly **1 in 40,000 to 1 in 100,000**.
- **Sex-specific incidence:** Because it is X-linked recessive, BCM is overwhelmingly a **disease of males**; fully symptomatic disease in females is exceptionally rare (estimated by some sources at roughly 1 in tens of billions of female births under strict biallelic assumptions, though skewed X-inactivation carrier phenotypes are more commonly reported than fully biallelic female cases).

### Inheritance Pattern and Genetic Parameters
- **Mode of inheritance:** X-linked recessive.
- **Penetrance:** Complete/high penetrance in hemizygous males carrying a fully inactivating genotype.
- **Expressivity:** Variable — genotype (C203R vs. deletion vs. exon-deletion) significantly influences severity and, especially, the rate of later-life progression to macular atrophy (Section 8).
- **Genetic anticipation:** Not reported for BCM; this is not a repeat-expansion disorder.
- **Germline mosaicism:** Not specifically well-documented in the literature reviewed, though possible in principle for any de novo X-linked structural variant.
- **Founder effects:** Recurrent structural (LCR deletion) and point-mutation (C203R) alleles behave as low-frequency founder/recurrent mutations across multiple unrelated pedigrees, attributable to the intrinsically recombinogenic locus architecture rather than a single shared ancestral haplotype in most reported cohorts; specific multi-family founder haplotypes (e.g., a 3-kb LCR deletion plus inserted aberrant OPN1MW gene) have also been documented ([PubMed 26153062](https://pubmed.ncbi.nlm.nih.gov/26153062/)).
- **Carrier frequency:** Not precisely established in large population databases due to locus mapping difficulty (segmental duplication); inferred to be low, consistent with disease rarity.
- **Consanguinity:** Not a major factor for an X-linked recessive disorder transmitted maternally (relevant mainly to autosomal recessive conditions), though it can theoretically increase risk of an affected homozygous female in rare pedigrees.

### Carrier (Female) Phenotype
Female carriers are typically unaffected or only mildly/subclinically affected due to random X-inactivation, but can show detectable abnormalities: **on average, about half of cones fated to express L or M opsin fail to make photopigment**, producing a disrupted cone mosaic with reduced density and abnormal spatial organization on adaptive optics imaging, and multifocal ERG evidence of patchy dysfunction ([PubMed 20638402](https://pubmed.ncbi.nlm.nih.gov/20638402/)). In rare cases of **skewed X-inactivation**, carrier females can manifest a clinically overt BCM-like phenotype despite heterozygosity ([PubMed 22998501, "Blue cone monochromatism in a female due to skewed X-inactivation"](https://pubmed.ncbi.nlm.nih.gov/22998501/)).

### Population Demographics
- **Affected populations:** No strong ethnic/geographic clustering has been robustly established in the literature surveyed; cases and distinct causal variants have been reported across European, Japanese, and other populations, consistent with the locus's intrinsic mutability across diverse genetic backgrounds ([Sci Rep, Japanese cohort](https://www.nature.com/articles/s41598-018-29891-9); [Human Genome Variation, Japanese families](https://www.nature.com/articles/hgv201611)).
- **Sex ratio:** Essentially all-male among clinically ascertained probands, consistent with X-linked recessive inheritance; carrier females are asymptomatic-to-mildly-affected.
- **Age distribution:** Presentation across all pediatric and adult age ranges (congenital onset with lifelong persistence); cohort studies specifically include pediatric-through-elderly patients to characterize the slow, genotype-dependent progression described above.

---

## 10. Diagnostics

### Clinical Tests
- **Electroretinogram (ERG):** The key diagnostic test. Standard rod-specific and maximal (mixed rod-cone) ERG responses are typically normal or near-normal, while the **30-Hz photopic flicker ERG (which is L/M-cone-driven) is undetectable or severely reduced**. Specialized S-cone-isolating stimuli elicit a characteristic blue-flash response (S-cone b-wave, amplitude ~5–10 µV, implicit time ~35–45 ms) that is essentially absent to red/green flashes of any intensity — this dissociation (present S-cone/rod signal, absent L/M-cone signal) is the diagnostic hallmark distinguishing BCM from complete (rod) achromatopsia, in which all cone signals are extinguished ([Springer ERG chapter](https://link.springer.com/chapter/10.1007/978-94-011-5408-6_46); [Wikipedia](https://en.wikipedia.org/wiki/Blue-cone_monochromacy)). S-cone contributions to oscillatory potentials have also been specifically characterized as an ancillary ERG signature ([PMC11236933](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11236933/)).
- **Color vision testing:** Farnsworth D-15 and Farnsworth-Munsell 100-Hue tests demonstrate severe generalized color confusion with relatively better-preserved tritan (blue-yellow) axis performance; the Berson test and other specialized instruments are also used.
- **Imaging (OCT):** Optical coherence tomography shows foveal ellipsoid zone (EZ) disruption and outer nuclear layer thinning from an early age (mean foveolar ONL ~60% of normal in patients aged 5–20 years), with slow further thinning and occasional macular atrophy with age ([Ophthalmology Science, PMC9521040](https://pmc.ncbi.nlm.nih.gov/articles/PMC9521040/)). Adaptive optics imaging can further resolve residual (structurally abnormal, shortened-outer-segment) cone mosaics.
- **Family history:** Reconstruction of an X-linked recessive pedigree (affected males, carrier females, no male-to-male transmission) supports the diagnosis.

### Genetic Testing
- **Recommended approach:** Targeted analysis of the OPN1LW/OPN1MW gene cluster and LCR, given the segmental-duplication/high-homology architecture that confounds standard short-read whole-exome sequencing. Specialized long-range PCR, Southern blotting, high-resolution microarray (chromosomal microarray/CMA equivalent for this locus), or long-read sequencing/optical genome mapping are typically required to accurately resolve deletions, hybrid genes, and copy-number changes at Xq28 ([PNAS 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9271157/); [PubMed 26153062](https://pubmed.ncbi.nlm.nih.gov/26153062/)). Orphanet lists a dedicated diagnostic test entry for OPN1LW/OPN1MW analysis ([Orphanet diagnostic test 317156](https://www.orpha.net/en/diagnostic-tests/diagnostic/317156)).
- **WES/WGS utility:** Standard WES pipelines frequently **miss or misclassify variants at this locus** due to near-identical paralog sequences, so a negative standard WES/WGS result does not exclude BCM; specialized bioinformatic pipelines or orthogonal structural-variant-focused testing are advised when BCM is clinically suspected.
- **Single-gene/targeted testing:** Direct amplicon sequencing or MLPA-style copy-number analysis of the OPN1LW/OPN1MW/LCR region is the most sensitive first-line molecular test.
- Chromosomal microarray, karyotyping, and FISH are generally not sensitive enough for these submicroscopic (kilobase-scale) rearrangements and are not first-line for BCM specifically.

### Clinical Diagnostic Criteria and Differential Diagnosis
There is no formal DSM/ICD structured diagnostic algorithm; diagnosis rests on the clinical triad (nystagmus/photophobia/myopia with poor acuity), ERG dissociation pattern, color-vision test results, and confirmatory molecular genetics. Key differential diagnoses:
- **Achromatopsia (rod monochromatism)**, autosomal recessive (CNGA3, CNGB3, GNAT2, PDE6C, PDE6H, ATF6), which affects all three cone types (not just L/M), typically produces worse visual acuity, more frequent foveal hypoplasia, and hyperopia rather than myopia — BCM patients have relatively better acuity, less-frequent foveal hypoplasia, and preserved tritan discrimination as distinguishing features ([PMC9521040](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9521040/); [GeneReviews Achromatopsia](https://www.ncbi.nlm.nih.gov/books/NBK1418/)).
- Other cone dystrophies/cone-rod dystrophies (progressive, often autosomal, with more marked rod involvement over time) should also be excluded via ERG and genetic testing.

### Screening
No population-based newborn or carrier screening program specifically targets BCM given its rarity; genetic counseling and cascade testing of at-risk maternal relatives in known BCM families is the practical screening approach once a proband's causal variant is identified.

---

## 11. Outcome/Prognosis

### Survival and Mortality
BCM is a purely ocular disorder with **no systemic organ involvement and no reduction in life expectancy or increased mortality**; it is not a life-limiting condition.

### Morbidity and Function
- **Visual morbidity:** Lifelong visual acuity impairment (20/60–20/200 range), profound color-vision deficit, photophobia, and nystagmus produce measurable functional impact on reading speed, mobility, and tasks requiring fine visual discrimination or color identification. Quality-of-life/functional outcome measures (reading performance, color-discrimination task batteries) have been specifically validated in BCM cohorts to quantify this burden and to serve as trial endpoints ([TVST Reading Performance, PMC7726588](https://pmc.ncbi.nlm.nih.gov/articles/PMC7726588/); [PLOS ONE Visual Function Outcome Measures, PMC4409040](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4409040/)).
- **Disability outcomes:** Most patients qualify as visually impaired/low vision by acuity criteria but retain functional (non-blind) vision; complete blindness is not typical.

### Disease Course
- **Complications:** The principal late complication is progressive foveal/macular atrophy in a subset of (typically older, and especially deletion-genotype) patients, which can further reduce visual acuity beyond the baseline congenital deficit.
- **Recovery potential:** No spontaneous recovery of L/M-cone function occurs with current standard care; the disorder is not reversible without investigational gene therapy (Section 12).

### Prediction / Prognostic Factors
- **Genotype is the principal prognostic factor identified in the literature:** the **C203R missense mutation** is associated with a substantially more indolent course (slower foveal ONL thinning and IS/OS disruption) than large **deletion** genotypes, which progress to structural retinal atrophy earlier and more rapidly ([IOVS C203R study](https://iovs.arvojournals.org/article.aspx?articleid=2717851)). This genotype-severity correlation is directly relevant to patient counseling and to gene-therapy trial patient selection/timing, since a shrinking therapeutic window with age/degeneration has been demonstrated in animal models ([PMC12036465](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12036465/)).

---

## 12. Treatment

### Current Standard of Care (Supportive/Symptomatic — No Disease-Modifying Therapy Approved)
There is **no curative or disease-modifying therapy currently approved** for BCM; management is entirely supportive:
- **Tinted lenses/filters:** Magenta- or brown-tinted lenses or contact lenses reduce photophobia and can enhance color contrast; magenta tints are specifically favored because they protect rods from over-stimulation while allowing maximal light transmission to stimulate the residual S-cones ([BCM Families Foundation clinical management](https://www.blueconemonochromacy.org/clinical-management/)). Suggested **NCIT** term: NCIT:C15747 (Supportive Care) as the general category; no specific NCIT code exists for "tinted lens therapy," though it can be mapped under low-vision rehabilitation/device categories.
- **Low vision aids:** Magnifiers, telescopic devices, and adaptive technology (tablet/e-reader adjustable lighting, color-identification apps/colorimeters, screen-reader software) support daily function, particularly reading and color-dependent tasks.
- **Refractive correction:** Standard correction of myopia with spectacles/contact lenses.
- **Periodic ophthalmologic monitoring:** Regular follow-up (including OCT) to track the genotype-dependent risk of late progressive macular atrophy.
- **NCIT terms applicable to current management:** NCIT:C15302 (Physical Therapy) — not typically relevant; more applicable are NCIT:C15747 (Supportive Care) and device/low-vision-aid categories; NCIT:C15240 (Genetic Counseling) for family counseling.

### Experimental / Investigational Gene Therapy
BCM is a leading candidate for **AAV-mediated gene supplementation therapy** because it is a monogenic, cell-autonomous, loss-of-function disorder amenable to opsin gene replacement in surviving cones:
- **Preclinical vector development — ADVM-062 (Adverum Biotechnologies):** An AAV.7m8-capsid vector (an AAV2 variant with enhanced foveal cone transduction after **intravitreal**, rather than subretinal, injection) expressing human L-opsin under a synthetic cone-specific promoter (MNTC cassette). GLP toxicology/biodistribution studies showed the vector was well tolerated up to 5×10¹¹ vg/eye with dose-dependent hL-opsin expression and functional opsin activity in non-human primate cones, supporting its potential as a single intravitreal injection therapy ([Molecular Therapy 2023, PMC10362383](https://pmc.ncbi.nlm.nih.gov/articles/PMC10362383/)).
- **Preclinical academic programs:** The Vision Center at Children's Hospital Los Angeles is developing a Phase 1 clinical trial protocol for the first gene therapy specifically for boys with BCM, supported by a $4.7 million grant from the California Institute for Regenerative Medicine (CIRM) ([Managed Healthcare Executive](https://www.managedhealthcareexecutive.com/view/gene-therapy-for-rare-eye-disease-to-advance-to-human-trial)); orphan drug designation has been granted to at least one BCM gene therapy candidate ([CGTlive, "Blue Cone Monochromacy Gene Therapy Gets Orphan Drug Designation"](https://www.cgtlive.com/view/blue-cone-monochromacy-gene-therapy-orphan-drug-designation)).
- **Mouse model proof-of-concept:** AAV-mediated L/M-opsin gene replacement rescues cone function and partially restores outer segment structure in Opn1lw/Opn1mw double-knockout and C198R (mouse equivalent of human C203R) knock-in models, and in an all-cone (Nrl-null) BCM model, using various capsids (AAV8-Y733F shown to outperform AAV5 in some comparisons) ([Sci Rep 2017, PMC5532293](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5532293/); [Molecular Therapy Advances 2025](https://www.cell.com/molecular-therapy-family/advances/fulltext/S3117-387X(25)00007-2); [JCI Insight, C203R structural/functional rescue](https://insight.jci.org/articles/view/172834)).
- **Key translational caveat — the therapeutic window:** Recent mouse studies specifically demonstrate that **AAV rescue efficacy declines with age/disease duration**, associated with mislocalized mitochondria, compromised connecting cilia, and reduced transgene expression in aged, degenerating cones — implying that human gene therapy trials will likely need to target patients relatively early in the disease course, before extensive cone structural loss, for maximal benefit ([Communications Biology 2025 / PMC12036465](https://pmc.ncbi.nlm.nih.gov/articles/PMC12036465/)).
- As of this review, **no completed or actively enrolling registered human clinical trial (ClinicalTrials.gov NCT identifier) for BCM gene therapy was identified** in available search results; development remains at the advanced preclinical/IND-enabling stage for the programs identified (ADVM-062 and the CHLA-CIRM program), with trial readiness work (validated outcome measures — see below) actively underway.
- Suggested **NCIT** term for the investigational modality: NCIT:C15238 (Gene Therapy).

### Trial Readiness / Outcome Measures Development
Because BCM has no natural endpoint analogous to a tumor response or a lab value, substantial dedicated methodological work has defined and validated functional outcome measures for future gene therapy trials, including: standardized **visual acuity and contrast sensitivity** protocols, a validated **reading performance** metric, and structured **color vision** discrimination tasks with quantified test-retest reliability ([PLOS ONE / PMC4409040](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4409040/); [TVST Reading Performance / PMC7726588](https://pmc.ncbi.nlm.nih.gov/articles/PMC7726588/); [TVST Color Vision Outcome Measures](https://tvst.arvojournals.org/article.aspx?articleid=2785310)), as well as detailed natural-history OCT/retinal-structure studies intended to define clinical endpoints and inform optimal patient/age selection for L-opsin gene therapy trials ([PMC11477341](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11477341/)).

### Treatment Strategy Notes
There is no combination-therapy or personalized-medicine algorithm beyond genotype-informed prognostic counseling (C203R vs. deletion genotype) and — prospectively — genotype/age-informed patient selection for gene therapy trials given the demonstrated shrinking therapeutic window.

---

## 13. Prevention

### Prevention Levels
- **Primary prevention:** Not applicable in the traditional sense (no modifiable environmental exposure to avoid); the only "primary prevention" pathway is **reproductive/genetic counseling** for known carrier families, including options such as preimplantation genetic diagnosis (PGD) or prenatal testing for at-risk pregnancies once a family's causal variant is characterized.
- **Secondary prevention:** Early recognition of the classic infantile triad (nystagmus, photophobia, poor fixation) with prompt ERG/genetic testing allows earlier diagnosis, appropriate low-vision intervention, and — in the future — earlier eligibility for gene therapy while cone structure is best preserved (directly relevant given the genotype/age-dependent progression and shrinking therapeutic window discussed above).
- **Tertiary prevention:** Regular ophthalmologic surveillance (including OCT) to detect and manage the onset of progressive macular atrophy, tinted-lens/low-vision interventions to minimize functional disability, and myopia correction to optimize best-corrected visual function.

### Immunization
Not applicable — BCM is not an infectious or immune-mediated disease.

### Screening and Early Detection
- No population-based newborn screening program exists for BCM specifically (unlike some metabolic disorders).
- **Genetic/carrier screening and cascade testing:** Once a proband's OPN1LW/OPN1MW/LCR variant is identified, cascade testing of at-risk maternal relatives (obligate and possible carrier females, at-risk male relatives) is the practical form of "screening" in this disorder, supporting informed reproductive decision-making.
- **Risk stratification:** Family pedigree analysis (X-linked recessive pattern) combined with confirmed molecular diagnosis in a proband allows precise risk stratification for relatives.

### Counseling
**Genetic counseling** is central to BCM management for family planning — explaining X-linked recessive transmission (obligate carrier status of daughters of affected males; 50% carrier risk for daughters, 50% affected risk for sons of carrier mothers), clarifying that carrier females are usually unaffected or mildly affected (with rare exceptions from skewed X-inactivation), and discussing reproductive options ([BCM Families Foundation transmission page](https://www.blueconemonochromacy.org/how-it-is-transmitted/); NCIT:C15240 Genetic Counseling).

### Public Health / Environmental Interventions
Not applicable — there are no environmental or public-health interventions relevant to this purely genetic disorder.

### Prophylaxis
No pharmacologic or procedural prophylaxis exists; management is entirely supportive/monitoring-based as described above (Section 12).

---

## 14. Other Species / Natural Disease

### Taxonomy
No naturally occurring companion-animal or wildlife disease directly homologous to human BCM (i.e., a spontaneous L/M-opsin-locus loss-of-function disorder) was identified in the available search results. Most non-human mammals (with the exception of catarrhine primates) are naturally dichromatic, possessing only a single long/middle-wavelength cone opsin gene plus an S-opsin gene — meaning the specific "duplicated-gene-array-with-shared-LCR" architecture that predisposes humans (and other catarrhine primates) to BCM is itself a primate-specific genomic feature, limiting natural cross-species disease models. Relevant taxonomic context: NCBITaxon:9606 (Homo sapiens); the L/M-opsin gene duplication is shared with Old World monkeys and apes (Catarrhini).

### Model Organism Orthologs
- **Mouse (Mus musculus):** *Opn1mw* (mouse M-opsin gene; ortholog of human OPN1MW/OPN1LW, since mice have a single M-opsin gene rather than the human tandem L/M array) and *Opn1sw* (S-opsin). NCBI Gene mouse *Opn1mw* is the key ortholog engineered in BCM models (see Section 15).
- No natural (spontaneously occurring) veterinary BCM-like disease was found in the literature surveyed; all animal "models" identified are engineered (see below), not naturally occurring disease.

### Comparative Biology
The evolutionary origin of the human OPN1LW/OPN1MW tandem duplication (from a single ancestral opsin gene via a relatively recent primate-lineage gene duplication event) explains both the disease-predisposing genomic instability (segmental duplication prone to NAHR) and the absence of a natural non-primate counterpart — most mammalian model species must be genetically engineered to recapitulate the human gene-loss phenotype.

### Transmission
Not applicable — BCM is a non-infectious, non-zoonotic, purely genetic disorder.

---

## 15. Model Organisms

### Model Types and Genetic Models
- **Mouse (Mus musculus) — the dominant model system:**
  - ***Opn1mw/Opn1sw* double-knockout (DKO) mice:** Complete genetic ablation of the murine M- and S-opsin genes, producing an "all-rod-driven-cone-loss" model analogous to complete L/M-opsin loss in humans ([Sci Rep 2017, PMC5532293](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5532293/)).
  - **Opn1mw^C198R^/Opn1sw^−/−^ knock-in ("C198R") mice:** A missense knock-in engineered to model the human C203R hybrid-gene missense mutation (the single most common human BCM genotype), allowing direct comparison of missense- versus deletion/null-genotype degeneration kinetics in a controlled genetic background ([PMC12036465](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12036465/); [Communications Biology 2025](https://www.nature.com/articles/s42003-025-09045-0)).
  - **All-cone retina models (e.g., *Opn1mw⁻/⁻/Opn1sw⁻/⁻/Nrl⁻/−* mice):** Combine opsin knockouts with *Nrl* loss (which converts the retina to an all-cone phenotype, eliminating rods) to increase the proportion of cone photoreceptors available for study and gene-therapy testing, since mice are naturally rod-dominant and have far fewer cones than the human macula ([Molecular Therapy Advances 2025](https://www.cell.com/molecular-therapy-family/advances/fulltext/S3117-387X(25)00007-2)).
  - **Induced/AAV-treated models:** The same knockout/knock-in lines are used as the substrate for AAV-mediated L/M-opsin gene replacement studies (Section 12).
- **Non-human primates (used for preclinical vector biodistribution/toxicology, not as genetic disease models):** Cynomolgus/rhesus macaques were used in GLP toxicology and biodistribution studies of the ADVM-062 intravitreal vector, leveraging the primate eye's similarity in size and foveal cone density to the human eye and the fact that primates share the tandem L/M-opsin gene architecture ([Molecular Therapy 2023, PMC10362383](https://pmc.ncbi.nlm.nih.gov/articles/PMC10362383/); [ASGCT 2022 poster](https://adverum.com/wp-content/uploads/2022/09/ASGCT-2022_ADVM-062_FINAL_05-09-22.pdf)).

### Model Characteristics — Phenotype Recapitulation and Limitations
- **Recapitulation:** Mouse knockout/knock-in models faithfully recapitulate the core molecular lesion (loss of functional M/L-opsin) and reproduce key downstream cellular findings seen in human BCM retina — absent/abnormal cone outer segments, progressive cone structural degeneration, and (in the C198R knock-in) a slower degeneration course than in full-null models, mirroring the human C203R-vs-deletion genotype-severity correlation ([PMC12036465](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12036465/)).
- **Limitations:** Mice lack a true fovea and have a rod-dominant, cone-sparse retina, substantially limiting direct translation of cone density/structural findings and necessitating all-cone (*Nrl*-null) or other cone-enriched engineering to increase experimental tractability; mice also possess only a single ancestral M/L-opsin gene (no tandem duplication/shared LCR), so the specific LCR-deletion and hybrid-gene-formation mutational mechanisms that predominate in human BCM cannot be modeled at the genomic-architecture level in mice — only the downstream consequence (opsin loss) is modeled via direct gene knockout/knock-in. Non-human primates better preserve foveal anatomy and gene-array architecture but are far more resource-intensive and are used primarily for vector safety/biodistribution rather than as a genetic disease model per se.

### Applications
Mouse models have been used to: (1) establish proof-of-concept that AAV-mediated opsin gene replacement can restore cone function and partially regenerate outer segment structure; (2) directly compare degeneration kinetics and gene-therapy rescue efficacy between missense (C198R) and null/deletion genotypes, informing human genotype-based prognosis; and (3) define the age-dependent "therapeutic window" for gene therapy — a critical translational finding indicating that earlier intervention (before advanced cone degeneration, mitochondrial mislocalization, and connecting-cilium compromise) yields substantially better rescue outcomes ([PMC12036465](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12036465/); [biorxiv preprint, C203R all-cone rescue](https://www.biorxiv.org/content/10.1101/2025.09.04.674359.full.pdf)).

### Resources
Mouse Genome Informatics (MGI) is the primary repository for the *Opn1mw*/*Opn1sw* knockout and knock-in alleles described above; no dedicated public repository entry for a BCM-specific "disease model" collection (e.g., in IMPC/KOMP) was specifically identified in this search, suggesting these lines are largely custom/investigator-generated rather than centrally banked as of this review.

---

## Summary of Suggested Ontology Term Mappings

| Category | Suggested Term(s) |
|---|---|
| Disease (MONDO) | MONDO:0010563 |
| Disease (OMIM) | #303700 |
| Disease (Orphanet) | ORPHA:16 |
| Causal genes (HGNC symbols) | OPN1LW (OMIM *300822); OPN1MW (OMIM *300821); regulatory element LCR (OMIM *300824) |
| Key phenotypes (HPO) | HP:0000640 (Nystagmus); HP:0000613 (Photophobia); HP:0000545 (Myopia); HP:0000572/HP:0000505 (Visual impairment); HP:0000550 (Abnormal electroretinogram); HP:0000608 (Macular atrophy); impaired color vision term |
| Cell types (CL) | CL:0000573 (retinal cone cell); CL:0000604 (retinal rod cell) |
| Anatomy (UBERON) | UBERON:0000966 (retina); UBERON:0001782 (fovea centralis); UBERON:0001789 (macula lutea) |
| Biological process (GO) | GO:0007601 (visual perception); GO:0007602 (phototransduction); GO:0035845 (photoreceptor outer segment organization) |
| Cellular component (GO) | GO:0001750 (photoreceptor outer segment); GO:0005783 (endoplasmic reticulum) |
| Treatment/intervention (NCIT) | NCIT:C15747 (Supportive Care); NCIT:C15238 (Gene Therapy, investigational); NCIT:C15240 (Genetic Counseling) |
| Model organism gene | Mouse *Opn1mw*, *Opn1sw* (NCBI Gene) |

---

## Sources

- [A 73,128 bp de novo deletion encompassing the OPN1LW/OPN1MW gene cluster in sporadic Blue Cone Monochromacy: a case report — BMC Medical Genetics](https://bmcmedgenet.biomedcentral.com/articles/10.1186/s12881-018-0623-8)
- [Genotype determination of the OPN1LW/OPN1MW genes: novel disease-causing mechanisms in Japanese patients with blue cone monochromacy — Scientific Reports](https://www.nature.com/articles/s41598-018-29891-9)
- [Novel OPN1LW/OPN1MW deletion mutations in 2 Japanese families with blue cone monochromacy — Human Genome Variation](https://www.nature.com/articles/hgv201611)
- [The landscape of submicroscopic structural variants at the OPN1LW/OPN1MW gene cluster on Xq28 underlying blue cone monochromacy — PNAS/PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9271157/)
- [Blue cone monochromacy: Causative mutations and associated phenotypes — Molecular Vision / PMC2676201 (PMID:19421413)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2676201/)
- [Blue cone monochromacy and gene therapy — Vision Research (ScienceDirect)](https://www.sciencedirect.com/science/article/pii/S0042698923000457)
- [Spectrum of color gene deletions and phenotype in patients with blue cone monochromacy — PubMed](https://pubmed.ncbi.nlm.nih.gov/10982039/)
- [Blue cone monochromatism: a phenotype and genotype assessment with evidence of progressive loss of cone function in older individuals — PubMed (PMID:15094734)](https://pubmed.ncbi.nlm.nih.gov/15094734/)
- [Blue Cone Monochromacy: Visual Function and Efficacy Outcome Measures for Clinical Trials — PLOS ONE/PMC4409040](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4409040/)
- [Reading Performance in Blue Cone Monochromacy: Defining an Outcome Measure for a Clinical Trial — TVST/PMC7726588](https://pmc.ncbi.nlm.nih.gov/articles/PMC7726588/)
- [Color Vision in Blue Cone Monochromacy: Outcome Measures for a Clinical Trial — TVST](https://tvst.arvojournals.org/article.aspx?articleid=2785310)
- [Blue-cone monochromacy and achromatopsia — CHRD, Perelman School of Medicine, University of Pennsylvania](https://www.med.upenn.edu/chrd/conedisorders.html)
- [Evaluation of Retinal Structure and Visual Function in Blue Cone Monochromacy to Develop Clinical Endpoints for L-opsin Gene Therapy — PMC11477341](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11477341/)
- [Preclinical evaluation of ADVM-062, a novel intravitreal gene therapy vector for the treatment of blue cone monochromacy — Molecular Therapy/PMC10362383](https://pmc.ncbi.nlm.nih.gov/articles/PMC10362383/)
- [Gene Therapy for Rare Eye Disease to Advance to Human Trial — Managed Healthcare Executive](https://www.managedhealthcareexecutive.com/view/gene-therapy-for-rare-eye-disease-to-advance-to-human-trial)
- [Blue Cone Monochromacy Gene Therapy Gets Orphan Drug Designation — CGTlive](https://www.cgtlive.com/view/blue-cone-monochromacy-gene-therapy-orphan-drug-designation)
- [Orphanet: Blue cone monochromatism (ORPHA:16)](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Lng=GB&Expert=16)
- [Orphanet: Diagnosis of Blue Cone Monochromacy (OPN1LW and OPN1MW gene)](https://www.orpha.net/en/diagnostic-tests/diagnostic/317156)
- [Cone monochromatism — NIH Genetic Testing Registry / GARD](https://rarediseases.info.nih.gov/diseases/917/cone-monochromatism)
- [Clinical Synopsis - #303700 - BLUE CONE MONOCHROMACY; BCM — OMIM](https://omim.org/clinicalSynopsis/303700)
- [Entry - #303700 - BLUE CONE MONOCHROMACY; BCM — OMIM](https://omim.org/entry/303700)
- [Entry - *300822 - OPSIN 1, LONG-WAVE-SENSITIVE; OPN1LW — OMIM](https://omim.org/entry/300822)
- [Entry - *300821 - OPSIN 1, MEDIUM-WAVE-SENSITIVE; OPN1MW — OMIM](https://omim.org/entry/300821)
- [Entry - *300824 - OPN1LW AND OPN1MW GENES, CONTROLLER OF — OMIM](https://omim.org/entry/300824)
- [Blue Cone Monochromatism with Foveal Hypoplasia Caused by the Concomitant Effect of Variants in OPN1LW/OPN1MW and GPR143 Genes — PMC8395340](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8395340/)
- [Blue Cone Monochromacy Caused by the C203R Missense Mutation or Large Deletion Mutations — IOVS](https://iovs.arvojournals.org/article.aspx?articleid=2717851)
- [Structural and functional rescue of cones carrying the most common cone opsin C203R missense mutation — JCI Insight](https://insight.jci.org/articles/view/172834)
- [Molecular and cellular impact of a C203R/C198R M-opsin mutation — PubMed](https://pubmed.ncbi.nlm.nih.gov/41941983/)
- [Molecular Mechanisms Limiting the Therapeutic Window of AAV Gene Therapy in Mouse Models of Blue Cone Monochromacy — PMC12036465](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12036465/)
- [Molecular mechanisms limiting the AAV gene therapy treatment window in mouse models of blue cone monochromacy — Communications Biology](https://www.nature.com/articles/s42003-025-09045-0)
- [Gene therapy rescues cone function in opn1mw−/−/opn1sw−/−/Nrl−/− mice, an all-cone model of blue cone monochromacy — Molecular Therapy Advances](https://www.cell.com/molecular-therapy-family/advances/fulltext/S3117-387X(25)00007-2)
- [Gene-based Therapy in a Mouse Model of Blue Cone Monochromacy — Scientific Reports/PMC5532293](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5532293/)
- [Gene Therapy Rescues Cone Function in an All-cone Retina Mouse Model for Blue Cone Monochromacy with the Most Common C203R Missense Mutation — bioRxiv](https://www.biorxiv.org/content/10.1101/2025.09.04.674359.full.pdf)
- [Comparing Retinal Structure in Patients with Achromatopsia and Blue Cone Monochromacy Using OCT — Ophthalmology Science/PMC9521040](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9521040/)
- [Blue-cone monochromacy — Wikipedia](https://en.wikipedia.org/wiki/Blue-cone_monochromacy)
- [What is Blue Cone Monochromacy? — BCM Families Foundation](https://www.blueconemonochromacy.org/blueconemonochromacy/)
- [Clinical Management of Blue Cone Monochromacy — BCM Families Foundation](https://www.blueconemonochromacy.org/clinical-management/)
- [How Blue Cone Monochromacy is transmitted? — BCM Families Foundation](https://www.blueconemonochromacy.org/how-it-is-transmitted/)
- [High-resolution microarray analysis unravels complex Xq28 aberrations in patients and carriers affected by X-linked blue cone monochromacy — PubMed](https://pubmed.ncbi.nlm.nih.gov/26153062/)
- [Molecular Genetics of Human Blue Cone Monochromacy — Science (Nathans et al.)](https://www.science.org/doi/10.1126/science.2788922)
- [Deletion of the X-linked opsin gene array locus control region (LCR) results in disruption of the cone mosaic — PubMed](https://pubmed.ncbi.nlm.nih.gov/20638402/)
- [Blue cone monochromatism in a female due to skewed X-inactivation — PubMed](https://pubmed.ncbi.nlm.nih.gov/22998501/)
- [Achromatopsia — GeneReviews®, NCBI Bookshelf NBK1418](https://www.ncbi.nlm.nih.gov/books/NBK1418/)
- [S-cone contribution to oscillatory potentials in patients with blue cone monochromacy — PMC11236933](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11236933/)
- [NM_020061.6(OPN1LW):c.739C>T (p.Arg247Ter) AND Cone monochromatism — ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/RCV000011249/)
- [OPN1MW — an overview — ScienceDirect Topics](https://www.sciencedirect.com/topics/neuroscience/opn1mw)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 20 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |

All extracted references resolved successfully.
