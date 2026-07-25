---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-8
cached: false
start_time: '2026-07-19T04:38:19.235549'
end_time: '2026-07-19T04:45:04.802445'
duration_seconds: 405.57
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Genital Lichen Sclerosus
  mondo_id: ''
  category: ''
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
  - claude-opus-4-8
  web_search_requests: 11
  num_turns: 22
  total_cost_usd: 2.420597
  session_id: 52560dd4-3abf-4b56-806d-d11f46059052
  stop_reason: end_turn
citation_count: 21
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Genital Lichen Sclerosus
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Genital Lichen Sclerosus** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


## Output

I have comprehensive, well-sourced material across all major dimensions. Here is the full research report.

---

# Research Report: Genital Lichen Sclerosus

> **Scope note.** This report covers **genital lichen sclerosus (LS)** — the vulvar (female) and penile (male, historically "balanitis xerotica obliterans"/BXO) forms of the same disease — with reference to extragenital and pediatric disease where mechanistically relevant. It is compiled for a disease-knowledge-base entry. **Ontology identifiers (HP/GO/CL/UBERON/CHEBI/MAXO) suggested below are candidates that MUST be verified with OAK before curation** — per the dismech anti-hallucination policy I flag every term I did not independently confirm against the source ontology. Confirmed database IDs (MONDO, ICD, MeSH) are stated as such.

---

## 1. Disease Information

**Overview.** Lichen sclerosus is a chronic, relapsing, inflammatory, and sclerosing dermatosis with a strong predilection for the anogenital skin and mucosa. It is regarded as an **immune-mediated (autoimmune) disease** driven by a T-helper-1 (Th1)/IFN-γ, miR-155–dependent inflammatory program that produces the characteristic porcelain-white atrophic plaques, dermal sclerosis/hyalinization, architectural scarring, and — in genital disease — a significant risk of squamous cell carcinoma (SCC). Genital LS is far more common and more clinically consequential than extragenital LS, which comprises only ~15–20% of cases and occurs as an isolated (no genital involvement) entity in only ~6% ([Lichen sclerosus: The 2023 update, *Front Med* 2023, PMID:36873861](https://pmc.ncbi.nlm.nih.gov/articles/PMC9978401/); [StatPearls, NBK538246](https://www.ncbi.nlm.nih.gov/books/NBK538246/)).

**Key identifiers.**
- **MONDO:** `MONDO:0007899` — lichen sclerosus et atrophicus (general); `MONDO:0006491` — vulvar lichen sclerosus; `MONDO:0001725` — balanitis xerotica obliterans (penile LS) ([OLS/MONDO](https://www.ebi.ac.uk/ols4/ontologies/mondo)). *There is no single dedicated "genital lichen sclerosus" MONDO term; the general LS term plus the two site-specific terms together cover the genital forms. For a genital-specific KB entry, `MONDO:0007899` is the natural primary with cross-references to the vulvar/penile children.*
- **ICD-10-CM:** `L90.0` — Lichen sclerosus et atrophicus ([ICD10Data](https://www.icd10data.com/ICD10CM/Codes/L00-L99/L80-L99/L90-/L90.0)). Penile disease historically also coded under `N48.0` (leukoplakia of penis / BXO).
- **ICD-11:** `EB60.1` reported for lichen sclerosus of penis; lichen sclerosus of vulva falls under the genitourinary/skin chapters (verify exact stem — ICD-11 codes were not fully confirmable from the sources searched).
- **MeSH:** `D018459` — "Lichen Sclerosus et Atrophicus" (Balanitis Xerotica Obliterans is an entry synonym).
- **Orphanet:** LS is relatively common (not a classic rare disease); a dedicated ORPHA code was not confirmed in the searched sources — treat as **not clearly assigned**.
- **OMIM:** No Mendelian OMIM phenotype number — LS is multifactorial/polygenic, not a single-gene disorder. (The autoantibody target gene *ECM1* has OMIM 602201, but that is the *lipoid proteinosis* locus, not an LS Mendelian entry.)

**Synonyms / alternative names.** Lichen sclerosus et atrophicus (LSA); balanitis xerotica obliterans (BXO — penile); kraurosis vulvae and vulvar dystrophy (obsolete terms for vulvar disease); white spot disease; hypoplastic dystrophy.

**Data derivation.** Information here is aggregated from disease-level resources (reviews, pathology series, national pathology/cancer registries such as the Danish and Dutch cohorts) rather than individual EHR records, though several key epidemiologic estimates derive from population/registry-linked cohorts.

---

## 2. Etiology

LS is **multifactorial**: a genetically predisposed, autoimmune-prone host in whom local factors (chronic occlusion, urine exposure, microtrauma/Koebnerization, hormonal milieu, dysbiosis) trigger and perpetuate a self-sustaining Th1 inflammatory–sclerosing response.

**Primary causal factors (autoimmune / immune-mediated).** The consensus mechanism is a **Th1-specific, IFN-γ–driven, miR-155–dependent** immune reaction with CD4+ and CD8+ T-cell infiltration at the dermoepidermal junction, upregulated proinflammatory cytokines (IL-1α, IL-7, IL-15, TNF-α) and downregulated IL-10. Circulating **IgG autoantibodies to extracellular matrix protein 1 (ECM1)** are found in a majority of patients and autoantibodies to **hemidesmosomal (BP180/BP230)** antigens occur in a subset ([2023 update, PMID:36873861](https://pmc.ncbi.nlm.nih.gov/articles/PMC9978401/); [Oyama et al., *Lancet* 2003, PMID:12867112](https://pubmed.ncbi.nlm.nih.gov/12867112/)).

**Risk factors.**
- **Genetic:** family history of LS in 8.7–12% of women (first-degree female relatives); HLA class II associations (see §4, §9). *"A positive family history of LS in first-degree female relatives can be found in 12% of patients."*
- **Sex and hormonal status:** strong female predominance; disease peaks in the **hypoestrogenic** windows (prepuberty and peri/postmenopause), suggesting low-estrogen states are permissive.
- **Local mechanical/chemical:** chronic occlusion, friction, heat, moisture, and — in boys/men — **urinary occlusion/exposure** behind an intact foreskin; an **uncircumcised state is the strongest risk factor** for penile LS (98% of BXO patients uncircumcised in one series). Microtrauma triggers **Koebnerization** (new lesions at sites of injury).
- **Autoimmune comorbidity:** personal/family history of autoimmune disease (thyroid disease especially) is a well-established association (§4, §6).
- **Age:** bimodal, with prepubertal and peri/postmenopausal peaks.

**Protective factors.**
- **Circumcision** is protective and often curative in males — the single best-supported protective/interventional factor for penile disease ([StatPearls BXO, PMID:33620847](https://www.ncbi.nlm.nih.gov/books/NBK567770/)).
- **Regular topical corticosteroid use** is associated with reduced scarring progression and a *"statistically significant lesser likelihood to develop malignancies when [topical corticosteroids] were regularly used"* — i.e., treatment appears partially protective against SCC ([2023 update, PMID:36873861](https://pmc.ncbi.nlm.nih.gov/articles/PMC9978401/)).
- No well-validated *genetic* protective allele has been established, though HLA-DR17 shows *decreased* frequency in UK women with LS (possible protective association).

**Gene–environment interaction.** The prevailing model is that an HLA-restricted, autoimmune-predisposed epithelium responds to local Koebnerizing insults (occlusion, urine, trauma) with a Th1/IFN-γ response; oxidative stress and TGF-β/BMP-driven fibrosis then create a self-perpetuating sclerotic, carcinogenesis-prone microenvironment. Infectious triggers (Borrelia burgdorferi, HPV, HCV) have been repeatedly proposed and **subsequently dismissed** as consistent causes ([2023 update](https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2023.1106318/full)).

---

## 3. Phenotypes

**Symptoms (patient-reported).**
- **Pruritus** — the cardinal symptom; *">90% of patients present with severe pruritus"* (vulvar). Candidate HPO: **Pruritus (HP:0000989)**. Frequency: **Very frequent/obligate**.
- **Vulvar/perianal soreness, burning, pain**; **dyspareunia**; **dysuria**; **clitoral hyperesthesia**; **pain on defecation/constipation** (especially children with perianal involvement). Candidate HPO: Dysuria (**HP:0100518**, verify), Dyspareunia (verify ID), Constipation (**HP:0002019**).
- Anal discomfort/anal fissuring in perianal disease.

**Clinical signs / physical manifestations.**
- **Ivory/porcelain-white atrophic plaques and papules**; skin appears thinned, wrinkled ("cigarette-paper" / "crinkly"), sometimes hyperkeratotic. Candidate HPO: Hypopigmented skin patches (**HP:0001053**, verify), Cutaneous/skin atrophy (verify).
- **"Figure-of-eight" / hourglass / keyhole** peri-vulvar and perianal distribution.
- **Ecchymoses/purpura, fissures, erosions, hyperkeratosis** (dermal fragility → hemorrhage is a diagnostic clue).
- **Architectural scarring:** in vulvar disease, fusion/resorption of the **labia minora**, burying of the **clitoris** (clitoral phimosis/adhesions), introital narrowing. *"Scarring… is observed in 80% of adult female patients and 30% of girls."*
- **Male:** whitish sclerotic scarring of the distal **prepuce** and **glans** → **phimosis** (LS causes 80–90% of acquired phimosis); meatal/urethral involvement in ~17% → meatal stenosis and urethral stricture.

**Phenotype characteristics.**
- **Onset:** bimodal — prepubertal girls (mean ~7.6 y) and peri/postmenopausal women (mean ~52.6 y); men typically 30–50 y (with a smaller prepubertal boy peak).
- **Severity:** variable, from mild pruritus to severe scarring, functional impairment, and malignancy.
- **Progression:** chronic, **relapsing–remitting/progressive**; high relapse rate off treatment. Scarring is generally irreversible once established.
- **Frequency among affected (vulvar):** pruritus >90%; scarring ~80% adult women / ~30% girls; extragenital involvement 15–20%; oral involvement uncommon.

**Quality-of-life impact.** Substantial: chronic pruritus/pain, dyspareunia and sexual dysfunction, urinary symptoms, body-image and psychological burden. Sexual well-being and daily functioning are markedly affected; QoL is a primary treatment endpoint in vulvar-LS laser/steroid trials ([Treatment options scoping review, PMC7995233](https://pmc.ncbi.nlm.nih.gov/articles/PMC7995233/)).

---

## 4. Genetic / Molecular Information

**No single causal gene.** LS is polygenic/multifactorial; there is no Mendelian causal mutation. The relevant genetics are **HLA susceptibility alleles** and an **autoantibody target (ECM1)**.

**HLA associations (susceptibility loci).**
- **HLA-DQ7** enrichment: *"DQ7 was present in 39 of 78 (50%) of patients compared with 89 (25%) controls (P < 0.001)"*; 78% of patients carried DQ7, DQ8, or DQ9 vs 40% of controls ([Marren et al. 1995, PMID:7888355](https://pubmed.ncbi.nlm.nih.gov/7888355/)). In children with vulvar LS, HLA-DQ7 was present in **66% vs 31%** of controls.
- **HLA-DR** alleles: increased **HLA-DR12**; decreased **HLA-DR17** in UK women.
- **Han Chinese:** HLA-A*11, HLA-B*13, HLA-B*15, HLA-DRB1*12 linked to higher risk ([2023 update, PMID:36873861](https://pmc.ncbi.nlm.nih.gov/articles/PMC9978401/)).

**Autoantibody target — ECM1 (gene: `ECM1`, HGNC:3153, chromosome 1q21.2).** ~**67–80%** of LS patients have circulating IgG anti-ECM1 autoantibodies; sera most frequently recognize the distal second tandem-repeat domain and C-terminus. The antigen-specific ELISA was **93.7% specific**, and *"higher anti-ECM1 titers correlated with more longstanding and refractory disease and cases complicated by squamous cell carcinoma"* ([Oyama et al., *Lancet* 2003, PMID:12867112](https://pubmed.ncbi.nlm.nih.gov/12867112/); ELISA development, *JCI* 2004, [PMC419485](https://pmc.ncbi.nlm.nih.gov/articles/PMC419485/)). Note: these are **autoantibodies to the ECM1 protein**, *not* germline *ECM1* mutations (biallelic *ECM1* loss-of-function causes lipoid proteinosis, a distinct disorder).

**Other autoantibodies.** Anti-hemidesmosome (BP180/BP230) IgG in a subset; overlap with mucous membrane pemphigoid.

**Modifier / effector molecules and expression changes.**
- **miR-155** upregulated — enhances Th1 differentiation, lowers Foxp3 (impairs Treg suppression), downregulates FOXO3 and CDKN1B to promote fibroblast proliferation.
- Downregulation of tumor suppressors **p16INK4a (CDKN2A)** and **p27Kip1 (CDKN1B)** under oxidative stress.
- **TP53** somatic changes in SCC arising from LS: single-base substitutions at **C742T and G818C in p53** described in LS-associated SCC.
- **Galectin-7 (LGALS7)** induces collagen I/III synthesis in fibroblasts.

**Epigenetics.** miR-155 (and other microRNAs) and tissue-remodeling gene dysregulation are the main documented epigenetic/regulatory alterations; oxidative DNA damage (8-OHdG) is reported. No large-scale DNA-methylation datasets are established.

**Chromosomal abnormalities.** None characteristic (not a cytogenetic disorder). Somatic aneuploidy/TP53 mutation appears in the LS→dVIN→SCC progression, not in uncomplicated LS.

---

## 5. Environmental Information

- **Local physical/chemical factors:** chronic **occlusion**, friction, heat, moisture; **urine exposure** (a proposed driver in males and in incontinent patients). Microtrauma/**Koebner phenomenon** initiates lesions at sites of injury (scratching, surgery, radiotherapy fields).
- **Hormonal environment:** hypoestrogenism (prepubertal, postmenopausal) is permissive.
- **Lifestyle:** obesity/incontinence increase occlusion and urine contact; smoking is a general SCC co-risk. No strong dietary association is established.
- **Infectious agents:** *Borrelia burgdorferi*, HPV, and HCV have each been proposed and **not confirmed** as causal. LS-associated genital SCC is characteristically **HPV-independent** (differentiated-VIN pathway), distinguishing it from HPV-driven usual-VIN cancers.
- **Microbiome/dysbiosis (emerging):** vulvar/skin dysbiosis with **reduced *Lactobacillus*, *Finegoldia*, *Cutibacterium*, *Staphylococcus*, *Lawsonella*** and **increased *Porphyromonas*** and other anaerobes reported in vulvar LS; cutaneous dysbiosis also reported in girls ([Nature Sci Rep 2024](https://www.nature.com/articles/s41598-024-58983-y); [Microbiol Spectr 2024](https://journals.asm.org/doi/10.1128/spectrum.02674-24); [Genital LS & vulvar microbiome, PMC12471758](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12471758/)). Causality is unproven.

---

## 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream):**

1. **Trigger (upstream):** In an HLA-predisposed host, local Koebnerizing insults (occlusion, urine, microtrauma) plus autoimmune predisposition initiate epithelial/basement-membrane injury and antigen exposure (ECM1, BP180).
2. **Th1/IFN-γ immune activation:** *"LS is a type 1 T helper (Th1) mediated and miR-155 dependent immune-mediated disease."* CD4+ and CD8+ T cells infiltrate the dermoepidermal junction; IFN-γ, IL-1α, IL-7, IL-15, TNF-α rise while IL-10 falls. **miR-155** amplifies Th1 skewing and suppresses Treg (Foxp3) tolerance. Plasmacytoid dendritic cells and a type-I-IFN signature contribute.
3. **Autoantibody effector arm:** anti-ECM1 IgG may activate **MMP9 → TGF-β activation**; anti-BP180/BP230 target the hemidesmosome, weakening dermoepidermal adhesion (basal keratinocyte degeneration, subepidermal clefting).
4. **Oxidative stress:** lipid peroxidation in keratinocytes, oxidative DNA damage, and protein oxidation with **low antioxidant-enzyme levels**; this downregulates p16INK4a/p27Kip1 and creates a mutagenic, pro-autoimmune, pro-carcinogenic microenvironment.
5. **Fibrosis / sclerosis (downstream):** **TGF-β and BMP2** drive collagen synthesis; **galectin-7** induces collagen I/III; miR-155-driven fibroblast proliferation. Result: the pathognomonic **upper-dermal hyalinization/homogenized collagen** and clinical sclerosis/scarring.
6. **Tissue remodeling → clinical manifestation:** epidermal atrophy, dermoepidermal fragility (purpura, erosions), and progressive architectural scarring; in genital sites → labial fusion/clitoral burying (women) or phimosis/meatal stenosis/urethral stricture (men).
7. **Neoplastic terminal branch:** chronic inflammation + oxidative DNA damage + TP53 substitutions (C742T, G818C) → **differentiated VIN/PeIN → HPV-independent squamous cell carcinoma** (see §11).

**Molecular pathways:** Th1/IFN-γ signaling (JAK-STAT — rationale for JAK inhibitors); TGF-β/BMP–SMAD fibrotic signaling; MMP9-mediated ECM remodeling; oxidative-stress/ROS response; p16/p53 tumor-suppressor loss.

**Cellular processes:** chronic inflammation, autoimmunity, oxidative stress, fibroblast activation/ECM deposition, basal keratinocyte apoptosis/degeneration, impaired immune tolerance.

**Immune involvement:** organ-specific autoimmunity with Th1/CD8 cytotoxic effector cells, autoantibodies (ECM1, BP180/BP230), and strong clustering with other autoimmune diseases — **thyroid autoimmunity** most notably: associated in **18.9% of female vs 5.1% of male** LS patients, with odds ratios of **2.88 (autoimmune thyroiditis), 2.34 (hypothyroidism), 2.05 (hyperthyroidism)**; also vitiligo, alopecia areata, pernicious anemia, RA, SLE, Sjögren, and morphea (co-occurring in **5.7%**). *"Autoimmune diseases are associated with LS in more than a quarter of the patients."*

**Candidate ontology terms (verify with OAK):**
- **GO (biological process):** T-helper 1 type immune response (GO:0042088); interferon-gamma production (GO:0032609); extracellular matrix organization (GO:0030198); collagen fibril organization (GO:0030199); response to oxidative stress (GO:0006979); transforming growth factor beta receptor signaling pathway (GO:0007179); fibroblast proliferation (GO:0048144); chronic inflammatory response (GO:0002544).
- **CL (cell types):** T-helper 1 cell (CL:0000545); CD8-positive, alpha-beta T cell (CL:0000625); CD4-positive, alpha-beta T cell (CL:0000624); regulatory T cell (CL:0000815); keratinocyte (CL:0000312); fibroblast (CL:0000057); macrophage (CL:0000235); mast cell (CL:0000097); plasmacytoid dendritic cell (CL:0000784).
- **CHEBI (molecules/mediators):** interferon-gamma; TGF-beta; reactive oxygen species; collagen. (Confirm exact CHEBI/PR IDs.)

**Molecular profiling.** Transcriptomic studies show distinct tissue-remodeling gene and microRNA (miR-155) signatures; oxidative-stress biomarkers (lipid peroxidation products, 8-OHdG, low SOD/catalase) are documented. Proteomics/metabolomics/lipidomics and single-cell/spatial datasets are limited but expanding; no established clinical multi-omics classifier yet.

---

## 7. Anatomical Structures Affected

**Organ level (primary):** external genitalia and adjacent perineal/perianal skin and mucosa.
- **Female:** vulva — **clitoral hood/clitoris, labia minora, inner labia majora, interlabial sulci, perineum, perianal skin** (figure-of-eight). The vagina is characteristically **spared**. Candidate UBERON: vulva (UBERON:0000997), clitoris (UBERON:0000453), labia minora/majora (verify UBERON IDs), perineum (verify).
- **Male:** **prepuce (foreskin)** and **glans penis**, **frenulum**, **coronal sulcus**, **external urethral meatus/urethra** (~17%). Candidate UBERON: prepuce of penis (UBERON:0001332), glans penis (verify), male urethra (verify).

**Secondary organ involvement / complications:** **urethra** (stricture), **urinary tract** (obstruction, retention from meatal stenosis/phimosis); psychological/sexual-function sequelae; malignant transformation (vulvar/penile SCC).

**Extragenital sites (15–20%):** submammary area, neck, shoulders, upper back, inner thighs, wrists/flexural surfaces; **oral mucosa** (labial > buccal) uncommon.

**Tissue/cell level:** stratified squamous **epithelium/epidermis** (atrophy, basal keratinocyte degeneration) and **upper dermis** (collagen hyalinization); infiltrating **T lymphocytes (CD4+/CD8+)** and **CD68+ macrophages**; fibroblasts producing sclerotic ECM.

**Subcellular level:** oxidative damage to **nuclear DNA** and membrane lipids; extracellular matrix/basement-membrane remodeling. Candidate GO cellular component: extracellular matrix (GO:0031012), collagen-containing extracellular matrix (GO:0062023).

**Localization / lateralization:** typically **bilateral/symmetric** in genital distribution; extragenital lesions may be localized or generalized.

---

## 8. Temporal Development

- **Onset:** chronic, **insidious**. Age is **bimodal** — prepubertal children and peri/postmenopausal adults (women), 30–50 y (men). Diagnostic delay is common (reported ~12.5–18 months in pediatric series).
- **Progression / course:** **chronic, relapsing–remitting to progressive**; untreated disease progresses to irreversible scarring (labial fusion, clitoral burying, phimosis, urethral stricture). Stages: early interface/vacuolar dermatitis → established dermal sclerosis with band-like infiltrate → late atrophic/scarred, paucicellular disease.
- **Remission:** treatment-induced clinical remission is achievable with topical corticosteroids; **spontaneous remission is uncommon in adults**. Some **prepubertal girls improve at puberty**, but a substantial fraction have persistent disease. High relapse rate when therapy is stopped.
- **Duration:** typically **lifelong/chronic**, requiring long-term maintenance and surveillance.
- **Critical periods / windows of intervention:** early diagnosis and sustained topical-steroid control reduce scarring and appear to lower malignancy risk — the main modifiable window.

---

## 9. Inheritance and Population

**Epidemiology.**
- **Prevalence/incidence:** overall estimated incidence ~**0.1–0.3%** of both sexes; population prevalence commonly cited between **1:300 and 1:1000**. Vulvar LS prevalence estimates up to ~**1.5%** of adult women in some settings; pediatric LS ~**0.04–0.06%** (girls ~1:900). LS accounts for a large share of specialist vulvar-clinic visits. True incidence is under-ascertained; **biopsy-verified incidence is rising** (Danish national data 1997–2022) ([Baandrup et al., *Int J Cancer* 2024, DOI:10.1002/ijc.34927](https://onlinelibrary.wiley.com/doi/full/10.1002/ijc.34927)).
- **Sex ratio:** female predominance, F:M ≈ **3:1 to 10:1** in adults. **In children the ratio is more balanced/reversed** (~1:1.7 female:male reported in one synthesis; most pediatric series still show girl predominance) ([Kumar et al., *Pediatr Dermatol* 2022, DOI:10.1111/pde.14967](https://onlinelibrary.wiley.com/doi/full/10.1111/pde.14967)).
- **Age distribution:** bimodal (prepubertal; peri/postmenopausal). ~7–15% of all LS cases occur in children.

**Genetic/inheritance features.** Not Mendelian — **multifactorial/polygenic** with HLA class II susceptibility (DQ7/DQ8/DQ9, DR12; DRB1*12 in Han Chinese). **Familial clustering** in ~8.7–12% (first-degree female relatives). No penetrance/expressivity/anticipation figures apply (not single-gene); no founder mutation, consanguinity effect, or carrier-frequency concept.

**Population demographics / geography.** Reported worldwide across ethnicities; most large cohorts are European (Danish, Dutch, UK). Population-specific HLA associations differ (UK vs Han Chinese). No strong endemic geographic clustering.

---

## 10. Diagnostics

**Clinical diagnosis.** Often clinical, based on the characteristic porcelain-white atrophic anogenital plaques with the figure-of-eight distribution. **ISSVD** provides a practical diagnostic/management guide ([ISSVD 2024 guide](https://www.lichensclerosus.ch/custom/data/ckeditorfiles/Dokumente/LichenSclerosusGuide2024.pdf)).

**Biopsy / histopathology (diagnostic gold standard when atypical, refractory, or to exclude malignancy).** Hallmark features ([Pathology Outlines](https://www.pathologyoutlines.com/topic/vulvalichensclerosus.html); StatPearls):
- **Epidermal atrophy** with loss/effacement of rete ridges; **orthohyperkeratosis** and follicular plugging.
- **Interface/vacuolar (lichenoid) change** with basal keratinocyte degeneration.
- **Broad band of upper-dermal hyalinization/homogenized ("sclerotic") collagen.**
- **Band-like and perivascular lymphohistiocytic infiltrate** *beneath* the hyalinized zone (CD4+/CD8+ T cells, CD68+ macrophages).
- **Dermal edema and hemorrhage/ecchymosis** — a useful early clue.
- Late lesions become atrophic, sclerotic, and paucicellular.
- IHC: p53 mutant-pattern staining flags associated **differentiated VIN/PeIN** (premalignant); HPV/p16 usually negative in LS-associated dysplasia.

**Biomarkers.** Serum **anti-ECM1 IgG** (research/adjunct; ~67–80% sensitivity, ELISA ~93.7% specificity) and anti-BP180/BP230 in a subset; **thyroid autoantibodies/TFTs** recommended given the association. No routine imaging biomarker.

**Adjunctive tests.** Dermoscopy (whitish structureless areas, comedo-like openings); reflectance confocal microscopy in research settings; urethral imaging/uroflowmetry in men with meatal/urethral involvement.

**Differential diagnosis.** Vulvar/penile **lichen planus** (mucosal erosive disease, vaginal involvement, Wickham striae — helps distinguish); **morphea/localized scleroderma** (extragenital overlap); **vitiligo** (pigment loss without atrophy/sclerosis); **mucous membrane pemphigoid**; **psoriasis/eczema/lichen simplex chronicus**; **candidal/atrophic vaginitis**; sexual-abuse mimics in children (LS purpura/fissures can be mistaken and vice versa); **VIN/PeIN/SCC** (biopsy to exclude).

**Genetic testing:** not indicated (no causal gene). HLA typing is research-only.

**Screening.** No population screening; the key is **lifelong clinical surveillance of established genital LS for malignant transformation**, with biopsy of thickened, ulcerated, fixed, or non-responding areas.

---

## 11. Outcome / Prognosis

**Malignant transformation — the principal serious outcome.**
- **Vulvar SCC:** *"Vulvar SCC was observed in 3.5 to 7% of women with VLS, while up to 65% of vulvar carcinomas arise on a background of VLS."* Cohort incidence ~**8.1 per 1,000 person-years**; cumulative probability of progression rising from **1.2% at 2 years to 36.8% at 25 years** in one series ([2023 update, PMID:36873861](https://pmc.ncbi.nlm.nih.gov/articles/PMC9978401/)).
- **Bleeker et al. (2016), 976 women:** median age at LS diagnosis 59.8 y; **cumulative VSCC incidence 6.7%**; 10-year VSCC risk strongly modified by concurrent VIN (**18.8% with VIN vs 2.8% without**) and age (**5.9% if ≥70 y; 3% if 50–70 y; 1.8% if <50 y**) ([Bleeker et al., *Cancer Epidemiol Biomarkers Prev* 2016, PMID:27257093](https://pubmed.ncbi.nlm.nih.gov/27257093/)).
- **Danish nationwide biopsy-verified cohort (2024):** absolute risk of vulvar high-grade squamous precancer **0.6% at 10 y, 1.3% at 20 y, 2.4% at 30 y**; **8.5-fold** increased standardized incidence ratio vs the general female population ([Baandrup et al., *Int J Cancer* 2024, DOI:10.1002/ijc.34927](https://onlinelibrary.wiley.com/doi/full/10.1002/ijc.34927)). A companion nationwide study examined **non-vulvar cancer risk** in biopsy-verified vulvar LS ([Kaderly Rasmussen et al., *Int J Cancer* 2024, DOI:10.1002/ijc.35101](https://onlinelibrary.wiley.com/doi/full/10.1002/ijc.35101)).
- **Penile SCC:** estimated in **4–13.4%** of men with penile LS; *"Twelve percent of all penile SCC are entirely due to MGLS."* LS-associated genital SCC is predominantly **HPV-independent**.

**Morbidity / function.** Even without cancer: chronic pruritus/pain, dyspareunia and sexual dysfunction, urinary obstruction (phimosis, meatal stenosis, urethral stricture), irreversible architectural scarring, and significant QoL/psychological burden.

**Survival/mortality.** LS itself is **not directly life-limiting**; mortality is driven by the associated SCC. Overall prognosis for uncomplicated LS controlled with topical steroids is good.

**Prognostic factors.** Older age at diagnosis, concurrent VIN/PeIN/dVIN, hyperkeratotic/ulcerated or fixed lesions, high anti-ECM1 titers (correlate with refractory/longstanding disease and SCC), poor treatment adherence. **Regular topical-steroid use is associated with less scarring and lower malignancy risk** — arguing that sustained control is both symptom- and cancer-protective.

---

## 12. Treatment

**First-line — superpotent topical corticosteroids (gold standard).**
- **Clobetasol propionate 0.05% ointment** (or **mometasone furoate 0.1%**). Typical induction: **nightly ~1 month → alternate nights ~1 month → twice weekly** (British Association of Dermatologists 3-phase regimen); men often once daily for 1–3 months, then taper ([Medscape treatment](https://emedicine.medscape.com/article/1123316-treatment); [2023 update](https://pmc.ncbi.nlm.nih.gov/articles/PMC9978401/)).
- **Maintenance** (long-term): clobetasol 2–3×/week or step-down to a mid-potency steroid (e.g., triamcinolone 0.1%) — **proactive maintenance reduces relapse, scarring, and malignancy risk**; high relapse when stopped entirely.
- Candidate MAXO/NCIT: topical anti-inflammatory/corticosteroid pharmacotherapy (verify MAXO term; NCIT:C15986 Pharmacotherapy). CHEBI: clobetasol propionate, mometasone furoate (verify IDs).

**Second-line — topical calcineurin inhibitors.** **Tacrolimus 0.1% ointment** and **pimecrolimus 1% cream** — effective steroid-sparing adjuncts/maintenance ([2023 update](https://pmc.ncbi.nlm.nih.gov/articles/PMC9978401/); [male-LS maintenance study, PMID:23472631](https://pubmed.ncbi.nlm.nih.gov/23472631/)). CHEBI: tacrolimus, pimecrolimus (verify).

**Surgical / interventional.**
- **Circumcision** in penile LS — often **curative** (definitive treatment for phimotic/preputial disease); partial/incomplete circumcision risks recurrence ([StatPearls BXO, PMID:33620847](https://www.ncbi.nlm.nih.gov/books/NBK567770/)). Candidate MAXO: surgical procedure (MAXO:0000004; confirm a circumcision-specific term).
- **Urethral/meatal reconstruction** for LS-related stricture; **perineoplasty/vulvar surgery** for functional scarring or to excise dVIN/SCC (surgery is not used to treat inflammation, only its complications/malignancy).

**Emerging / experimental (limited long-term data).**
- **Fractional CO₂ laser** and other energy devices (multiple RCTs vs clobetasol; benefit uncertain/adjunctive).
- **Platelet-rich plasma (PRP)** injections; **polydeoxyribonucleotide** dermal infiltration (adjuvant).
- **Photodynamic therapy.**
- **Topical/oral JAK inhibitors** (e.g., **ruxolitinib**) — mechanistically rational given the IFN-γ/JAK-STAT axis; trials ongoing.
- Topical **testosterone/estrogen** are **outdated/not recommended** as primary therapy.

**Supportive care.** Emollients/barrier ointments, gentle genital skin care, avoidance of irritants/soaps, treatment of secondary infection/candidiasis, and psychosexual support. Patient education strongly improves adherence and outcomes.

**Pharmacogenomics:** none established for LS therapy.

**Treatment algorithm summary:** confirm diagnosis (± biopsy) → induction superpotent topical steroid → proactive maintenance steroid ± calcineurin inhibitor → circumcision for penile phimotic disease → surveillance for malignancy → surgery reserved for strictures/functional scarring/neoplasia.

---

## 13. Prevention

- **Primary prevention:** none proven for first onset (etiology multifactorial); avoiding chronic occlusion/urine exposure/microtrauma is reasonable but unproven. **Circumcision** effectively prevents/cures preputial penile disease and is the closest thing to primary prevention in males.
- **Secondary prevention (early detection/treatment):** prompt diagnosis and **early sustained topical-steroid therapy** prevent scarring and appear to **reduce malignant transformation** — the best-supported preventive strategy.
- **Tertiary prevention (preventing complications):** lifelong maintenance therapy + structured surveillance for SCC; biopsy of suspicious lesions; management of phimosis/stricture before obstruction.
- **Screening/counseling:** no population screening; counsel patients on adherence, self-examination, and malignancy warning signs; screen for/monitor **associated autoimmune disease (thyroid)**.
- **Immunization / public-health / prophylaxis:** not applicable (LS-associated SCC is largely HPV-independent, so HPV vaccination is not expected to prevent LS-associated genital cancer, though it prevents HPV-driven VIN/SCC).

---

## 14. Other Species / Natural Disease

- **Taxonomy:** primarily a **human (Homo sapiens, NCBI:txid9606)** disease.
- **Veterinary / natural disease:** LS is essentially a human condition; there is **no well-characterized naturally occurring animal homolog** analogous to human genital LS. (Sclerosing/fibrosing genital dermatoses exist across species but are not established LS orthologs.)
- **Comparative biology / models:** understanding is driven by human tissue studies; no robust spontaneous animal model recapitulates the full disease. Evolutionary conservation of the implicated pathways (Th1/IFN-γ, TGF-β, ECM1) is high, but disease-level conservation is not documented.
- **Transmission:** not transmissible; **not zoonotic**; not an infectious disease.

---

## 15. Model Organisms

- **Model status:** **no widely accepted, well-validated animal model** of genital LS exists — a recognized gap. Research relies chiefly on **human lesional tissue, patient sera, and cell-based systems** (keratinocyte/fibroblast cultures, immunohistochemistry, transcriptomic/microRNA profiling).
- **In vitro / cellular:** patient-derived fibroblasts and keratinocytes used to study oxidative stress, TGF-β/BMP/galectin-7–driven collagen synthesis, and miR-155 effects; ECM1 autoantibody assays in patient sera.
- **Genetic models:** *Ecm1* and immune-pathway (IFN-γ, miR-155, TGF-β) knockout/transgenic mice inform component mechanisms but do **not reproduce genital LS** as a syndrome; *ECM1*-null biology is more relevant to lipoid proteinosis than to LS.
- **Limitations:** absence of a faithful in vivo model limits preclinical therapeutic testing (e.g., for JAK inhibitors), which is a major reason evidence rests on human observational and interventional studies.
- **Resources:** MGI/IMPC for the individual pathway genes; no dedicated LS model repository.

---

## Key References (PMID / DOI)

1. **Lichen sclerosus: The 2023 update.** *Front Med* 2023. **PMID:36873861** — comprehensive pathogenesis/genetics/malignancy/treatment review (primary source for most quantitative claims). https://pmc.ncbi.nlm.nih.gov/articles/PMC9978401/
2. **Oyama M, et al.** Autoantibodies to extracellular matrix protein 1 in lichen sclerosus. *Lancet* 2003. **PMID:12867112.** https://pubmed.ncbi.nlm.nih.gov/12867112/
3. **Development of antigen-specific ELISA for circulating anti-ECM1 autoantibodies in LS.** *JCI* 2004. https://pmc.ncbi.nlm.nih.gov/articles/PMC419485/
4. **Marren P, et al.** The association between lichen sclerosus and antigens of the HLA system. *Br J Dermatol* 1995. **PMID:7888355.** https://pubmed.ncbi.nlm.nih.gov/7888355/
5. **Bleeker MCG, et al.** Lichen Sclerosus: Incidence and Risk of Vulvar Squamous Cell Carcinoma. *Cancer Epidemiol Biomarkers Prev* 2016. **PMID:27257093.** https://pubmed.ncbi.nlm.nih.gov/27257093/
6. **Baandrup L, et al.** Biopsy-verified vulvar lichen sclerosus: incidence trends 1997–2022 and increased risk of vulvar squamous precancer and SCC. *Int J Cancer* 2024. **DOI:10.1002/ijc.34927.** https://onlinelibrary.wiley.com/doi/full/10.1002/ijc.34927
7. **Kaderly Rasmussen E, et al.** Biopsy-verified vulvar lichen sclerosus and the risk of non-vulvar cancer: a nationwide cohort study. *Int J Cancer* 2024. **DOI:10.1002/ijc.35101.** https://onlinelibrary.wiley.com/doi/full/10.1002/ijc.35101
8. **Balanitis Xerotica Obliterans (Male Penile Lichen Sclerosus).** *StatPearls* (NBK567770). **PMID:33620847.** https://www.ncbi.nlm.nih.gov/books/NBK567770/
9. **Lichen Sclerosus.** *StatPearls* (NBK538246). https://www.ncbi.nlm.nih.gov/books/NBK538246/
10. **Kumar S, et al.** Comparison of lichen sclerosus in boys and girls: a systematic review. *Pediatr Dermatol* 2022. **DOI:10.1111/pde.14967.** https://onlinelibrary.wiley.com/doi/full/10.1111/pde.14967
11. **ISSVD Practical Guide to Diagnosis and Management of Lichen Sclerosus (2024).** https://www.lichensclerosus.ch/custom/data/ckeditorfiles/Dokumente/LichenSclerosusGuide2024.pdf
12. **Vulvar/skin/gut microbiome alterations in vulvar LS.** *Sci Rep* 2024. https://www.nature.com/articles/s41598-024-58983-y

---

## Curation notes for the dismech entry

- **Primary MONDO:** `MONDO:0007899` (lichen sclerosus et atrophicus), cross-referencing `MONDO:0006491` (vulvar) and `MONDO:0001725` (penile/BXO). This aligns with the recent KB commits describing a **Th1-CD8+ autoimmune mechanism** — the mechanism captured in §6 above.
- **Highest-value, verifiable evidence anchors:** anti-ECM1 (PMID:12867112), HLA-DQ7 (PMID:7888355), SCC risk (PMID:27257093; Baandrup 2024), and the 2023 update review (PMID:36873861). Fetch each with `just fetch-reference` and confirm every snippet is an exact abstract substring before committing.
- **Before entry, run `just validate-terms-file`** on all HP/GO/CL/UBERON/CHEBI/MAXO IDs above — I have flagged each unverified ID explicitly; several (dyspareunia HP, labia/glans/perineum UBERON, clobetasol/tacrolimus CHEBI, circumcision MAXO) should be looked up with OAK rather than trusted from this report.
- **Possible module conformance:** `fibrotic_response` (TGF-β/BMP-driven dermal sclerosis) and, for the SCC branch, `tumor_promoting_inflammation` / a chronic-inflammation-to-SCC pathway. Malignant transformation could be modeled as a comorbidity/trajectory edge (LS → dVIN/PeIN → HPV-independent SCC) rather than embedded wholesale.

**Sources:** [Front Med 2023 / PMC9978401](https://pmc.ncbi.nlm.nih.gov/articles/PMC9978401/) · [Frontiers 2023 update](https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2023.1106318/full) · [StatPearls NBK538246](https://www.ncbi.nlm.nih.gov/books/NBK538246/) · [StatPearls BXO NBK567770 / PMID:33620847](https://www.ncbi.nlm.nih.gov/books/NBK567770/) · [Oyama Lancet 2003 / PMID:12867112](https://pubmed.ncbi.nlm.nih.gov/12867112/) · [JCI ELISA / PMC419485](https://pmc.ncbi.nlm.nih.gov/articles/PMC419485/) · [Marren HLA / PMID:7888355](https://pubmed.ncbi.nlm.nih.gov/7888355/) · [Bleeker 2016 / PMID:27257093](https://pubmed.ncbi.nlm.nih.gov/27257093/) · [Baandrup 2024 / IJC](https://onlinelibrary.wiley.com/doi/full/10.1002/ijc.34927) · [Kaderly Rasmussen 2024 / IJC](https://onlinelibrary.wiley.com/doi/full/10.1002/ijc.35101) · [Kumar 2022 / Pediatr Dermatol](https://onlinelibrary.wiley.com/doi/full/10.1111/pde.14967) · [Treatment scoping review / PMC7995233](https://pmc.ncbi.nlm.nih.gov/articles/PMC7995233/) · [Medscape treatment](https://emedicine.medscape.com/article/1123316-treatment) · [Male-LS maintenance / PMID:23472631](https://pubmed.ncbi.nlm.nih.gov/23472631/) · [MONDO via OLS](https://www.ebi.ac.uk/ols4/ontologies/mondo) · [ICD-10 L90.0](https://www.icd10data.com/ICD10CM/Codes/L00-L99/L80-L99/L90-/L90.0) · [Sci Rep 2024 microbiome](https://www.nature.com/articles/s41598-024-58983-y) · [Microbiol Spectr 2024](https://journals.asm.org/doi/10.1128/spectrum.02674-24) · [ISSVD 2024 guide](https://www.lichensclerosus.ch/custom/data/ckeditorfiles/Dokumente/LichenSclerosusGuide2024.pdf) · [Pathology Outlines](https://www.pathologyoutlines.com/topic/vulvalichensclerosus.html)
