---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-8[1m]
cached: false
start_time: '2026-06-30T09:54:35.407185'
end_time: '2026-06-30T09:59:13.521009'
duration_seconds: 278.11
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Rosai-Dorfman Disease
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
  - claude-opus-4-8[1m]
  web_search_requests: 11
  num_turns: 11
  total_cost_usd: 2.2887644999999996
  session_id: 0c7ccbf5-7cb9-4afd-bf22-9c1112efa58b
  stop_reason: end_turn
citation_count: 14
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Rosai-Dorfman Disease
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Rosai-Dorfman Disease** covering all of the
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

I have enough authoritative material to write the report. Here it is.

---

# Comprehensive Research Report: Rosai-Dorfman Disease (Rosai-Dorfman-Destombes Disease)

*Prepared for dismech knowledge-base curation • 2026-06-30*

> **A note on evidence handling for the curator:** Every PMID and quotation below is drawn from web sources during research. Per the dismech SOP (§2a), treat these as *leads*. Before committing any snippet to a `kb/disorders/` entry, run `just fetch-reference PMID:XXXX` and verify each snippet is an exact substring of the cached abstract. Several quotes here are paraphrases assembled by the search tool and are flagged where that risk is highest.

---

## 1. Disease Information

**Overview.** Rosai-Dorfman disease (RDD), now preferentially called **Rosai-Dorfman-Destombes disease (RDD)** to credit Destombes' 1965 description, is a rare non-Langerhans-cell histiocytosis. The defining lesion is an accumulation of large, activated histiocytes (tissue macrophages) with a characteristic morphology — voluminous pale cytoplasm, a round nucleus with a prominent nucleolus, and **emperipolesis** (intact lymphocytes, plasma cells, or red cells trafficking *through* the histiocyte cytoplasm). Originally described in 1969 by Juan Rosai and Ronald Dorfman as **"sinus histiocytosis with massive lymphadenopathy" (SHML)**, it was long regarded as a benign reactive/inflammatory process, but the discovery of recurrent clonal MAPK-pathway mutations has reframed a substantial subset as a clonal histiocytic neoplasm.

Think of the RDD histiocyte as an overstuffed cellular vacuum cleaner that has swallowed its neighbors whole and refuses to digest them — that swallowing-but-not-killing (emperipolesis) is the morphologic signature.

**Key identifiers** (verify against the local MONDO/OAK adapter before use):
- **MONDO:** MONDO:0006412 (Rosai-Dorfman disease) — *verify with `runoak -i sqlite:obo:mondo info MONDO:0006412`*
- **MeSH:** D006666 — "Histiocytosis, Sinus"
- **ICD-10:** D76.3 (other histiocytosis syndromes)
- **ICD-11:** EK92 (or 4B21 region for histiocytic/dendritic cell neoplasms — verify)
- **ICD-O / WHO:** classified within histiocytic/dendritic neoplasms; placed in the **"R group"** of the 2016 revised histiocytosis classification
- **GARD:** 7588; **SNOMED CT:** 34287003 ("Sinus histiocytosis with massive lymphadenopathy")
- **OMIM:** No OMIM number for sporadic RDD; the **familial/syndromic** form maps to **OMIM 602782** (Histiocytosis-lymphadenopathy plus syndrome / *SLC29A3* spectrum)

**Synonyms / alternative names:** Sinus histiocytosis with massive lymphadenopathy (SHML); Rosai-Dorfman-Destombes disease (RDD); Destombes-Rosai-Dorfman disease; (familial form:) Faisalabad histiocytosis.

**Data provenance:** This entry is built from **aggregated disease-level resources** (consensus guidelines, case series, mutation surveys, ontologies) rather than individual EHR records. The largest data sources are the 2018 international consensus (Abla et al., PMID 29720485) and pooled molecular case series.

---

## 2. Etiology

RDD is **etiologically heterogeneous** — the consensus framework recognizes that it spans a reactive-to-neoplastic continuum, and different subtypes likely have different drivers.

**Primary causal factors:**
- **Clonal somatic MAPK/ERK-pathway activation** (a major, recently recognized driver). Activating mutations in *KRAS*, *NRAS*, *MAP2K1* (MEK1), *ARAF*, and occasionally *CSF1R*/*CBL* are found in roughly **one-third to one-half** of cases tested, indicating a clonal neoplastic process in those patients (Garces et al., PMID 28664935; molecular surveys below). *"Mutually exclusive recurrent KRAS and MAP2K1 mutations… were detected in one-third of cases of Rosai–Dorfman disease, suggesting this subgroup are clonal and involve activation of the MAPK/ERK pathway"* (paraphrase of PMID 28664935 — **verify exact wording**).
- **Reactive / immune-dysregulatory mechanism.** In mutation-negative cases, a polyclonal, cytokine-driven macrophage activation (an exaggerated immune response, possibly post-infectious) remains the leading model. Associations with autoimmune disease (~10% of cases) support an immune-dysregulation arm.
- **Germline genetic causes (familial RDD).** Biallelic germline *SLC29A3* mutations cause familial RDD / Faisalabad histiocytosis / the H-syndrome spectrum (PMID 20140240). Germline *FAS* (*TNFRSF6*) mutations link RDD to autoimmune lymphoproliferative syndrome (ALPS).
- **Proposed infectious triggers** (historically): Epstein-Barr virus (EBV), human herpesvirus 6 (HHV-6), parvovirus B19 — repeatedly investigated but **never confirmed as causal**; current evidence does not support an infectious etiology for most cases.

**Risk factors.**
- *Genetic:* germline *SLC29A3* (familial), germline *FAS* (ALPS-associated); somatic MAPK mutations are acquired drivers rather than inherited risk.
- *Demographic/environmental:* young age (classic nodal form peaks in the first two decades), African ancestry (classic nodal form more frequent), and a possible male predominance in nodal disease. No robust occupational, dietary, or toxic exposure has been established.

**Protective factors:** None established. No protective alleles or lifestyle factors are documented.

**Gene-environment interactions:** Not well characterized. The most plausible interaction is a clonal histiocyte bearing a MAPK mutation operating within an immune/cytokine milieu that determines disease extent and the autoimmune-associated subset; this remains hypothesis-level.

---

## 3. Phenotypes

RDD is protean. The hallmark presentation is **massive, painless, bilateral cervical lymphadenopathy**, but extranodal involvement occurs in ~43% of patients and can affect virtually any site.

| Phenotype | Type | Frequency / notes | Suggested HPO |
|---|---|---|---|
| Cervical lymphadenopathy (massive, bilateral, painless) | Clinical sign | Most common presentation of nodal RDD | HP:0000787 (Cervical lymphadenopathy) / HP:0002716 (Lymphadenopathy) |
| Generalized/peripheral lymphadenopathy (axillary, inguinal, mediastinal) | Clinical sign | Frequent | HP:0002716 (Lymphadenopathy) |
| Fever (often intermittent) | Symptom | Common, with nodal disease | HP:0001945 (Fever) |
| Cutaneous nodules/plaques/papules (yellow-red-brown) | Physical manifestation | ~10% of extranodal; "purely cutaneous RDD" is a distinct, more indolent subtype, more common in Asian females | HP:0011842 (skin nodule → use HP:0200035 Nodular skin lesion or HP:0001019) — verify |
| Orbital/ophthalmic mass, eyelid/lacrimal involvement, uveitis | Physical/clinical | ~11% of extranodal | HP:0000315 (Abnormality of the orbital region) / HP:0000554 (Uveitis) |
| Sinonasal mass, nasal obstruction, epistaxis | Clinical | ~11%; more common in Asian patients | HP:0011109 (Chronic sinusitis) / HP:0000421 (Epistaxis) / HP:0030781 (Nasal obstruction) |
| CNS mass (intracranial dural-based, mimics meningioma; spinal cord compression) | Clinical | <5% overall; 75% intracranial, 25% spinal | HP:0002423 / HP:0100295 (CNS lesion); HP:0002176 (Spinal cord compression) |
| Bone lesions (metaphyseal/diaphyseal lytic) | Physical | 5–10% | HP:0002659 (Increased susceptibility to fractures) / HP:0002757; use HP:0100242 (Osteolytic lesion) |
| Pulmonary / intrathoracic infiltration, interstitial lung disease | Clinical | ~2%; carries high (~45%) mortality | HP:0006530 (Abnormal pulmonary interstitial morphology) / HP:0002206 |
| Renal infiltration / mass | Clinical | ~4%; ~40% mortality | HP:0000077 (Abnormality of the kidney) |
| Hepatomegaly / splenomegaly | Clinical sign | Variable | HP:0002240 (Hepatomegaly) / HP:0001744 (Splenomegaly) |
| Salivary gland, breast, GI, soft tissue involvement | Physical | Less common (GI <1%) | site-specific HP terms |
| Polyclonal hypergammaglobulinemia | Laboratory | Common | HP:0003529 (Hypergammaglobulinemia) |
| Elevated ESR | Laboratory | Common | HP:0003565 (Elevated erythrocyte sedimentation rate) |
| Anemia (often normocytic, sometimes autoimmune hemolytic) | Laboratory | Frequent | HP:0001903 (Anemia) / HP:0001890 (Autoimmune hemolytic anemia) |
| Leukocytosis / neutrophilia | Laboratory | Variable | HP:0001974 (Leukocytosis) |
| Autoimmune cytopenias | Laboratory | In immune-associated subset | HP:0001973 (Autoimmune thrombocytopenia) |

**Phenotype characteristics:**
- **Onset:** Classic nodal RDD favors children/young adults (historical mean ~20.6 years), whereas extranodal and cutaneous forms and the treated/molecularly-profiled cohorts skew older (median ~50 years; cobimetinib cohort median 57). → onset spans **childhood to late adulthood**, broadly bimodal/variable.
- **Severity:** Highly **variable** — from asymptomatic, self-limited lymphadenopathy to life-threatening organ infiltration.
- **Progression:** Often **episodic/relapsing-remitting** with spontaneous remissions; a minority is progressive.
- **QoL impact:** Driven by site — disfiguring lymphadenopathy/cutaneous lesions, visual compromise (orbital), neurologic deficits (CNS/spinal), airway obstruction, or organ failure (renal/pulmonary). No RDD-specific validated QoL instrument exists.

---

## 4. Genetic / Molecular Information

**Somatic driver genes (the neoplastic arm).** RDD harbors recurrent activating mutations in the **MAPK/ERK (RAS-RAF-MEK-ERK) pathway**:

- **MAP2K1** (MEK1; HGNC:6840; OMIM 176872) — the **single most frequent** gene, ~14% of all RDD; in microdissected specimens the incidence is higher. Typical variants: p.Q56P, p.F53_Q58 in-frame deletions, p.P124 substitutions (kinase-activating).
- **KRAS** (HGNC:6407; OMIM 190070) — ~12.5%; e.g., p.G12D, p.G12V, p.A146T.
- **NRAS** (HGNC:7989) — e.g., p.G13D.
- **ARAF** (HGNC:646) — recurrent in a subset.
- **CSF1R**, **CBL** — less common.
- ***BRAF* p.V600E is characteristically ABSENT** in RDD (a key contrast with Erdheim-Chester disease and Langerhans cell histiocytosis), though rare BRAF-V600E "RDD-like" histiocytoses are reported as diagnostic pitfalls (PMC11871196).

*Frequency summary (paraphrased from molecular surveys, e.g., Cangelosi/MDPI review PMC9654168 and Garces PMID 28664935): "From 30% to 50% of patients with RDD harbor somatic mutations… frequently involving ARAF, NRAS, KRAS, MAP2K1, CSF1, and CBL genes, of which MAP2K1 and KRAS were most frequent (~14% and ~12.5%)."* **Verify exact numbers before citing.** A 2025 whole-exome study of Saudi patients (Frontiers Oncol, PMC12094912) revisited and expanded this landscape.

- **KRAS and MAP2K1 mutations are mutually exclusive**, consistent with single-pathway (MAPK) activation as the unifying mechanism (PMID 28664935).
- **Clonality:** Mutation-bearing cases are clonal; this underlies the 2016 WHO reframing of RDD as (in part) a neoplasm.

**Germline / inherited:**
- **SLC29A3** (HGNC:23096; OMIM 612373) — biallelic loss-of-function germline mutations cause **familial RDD / Faisalabad histiocytosis / H syndrome** (autosomal recessive; OMIM 602782). *"Mutations in SLC29A3, encoding an equilibrative nucleoside transporter ENT3, cause a familial histiocytosis syndrome (Faisalabad histiocytosis) and familial Rosai-Dorfman disease"* (PMID 20140240). Compound germline *SLC29A3* + somatic *MAP2K1* has been reported in pediatric recurrent RDD (PMID 32944792).
- **FAS / TNFRSF6** — germline mutations link RDD to **ALPS type Ia**; these patients show more aggressive ALPS, male predominance, and early onset.

**Variant classification / type:** drivers are activating **missense substitutions and small in-frame indels** (gain-of-function); germline *SLC29A3* variants are loss-of-function (missense/nonsense/frameshift). Somatic drivers are absent or rare in population databases (gnomAD); germline *SLC29A3* pathogenic alleles are rare with founder clustering in consanguineous populations.

**Functional consequence:** MAPK driver mutations cause **constitutive ERK signaling** (gain of function) → histiocyte proliferation/survival. *SLC29A3* mutations cause **loss of ENT3 nucleoside-transport function** in lysosomal/mitochondrial membranes, leading to nucleoside accumulation and aberrant macrophage activation.

**Epigenetics / chromosomal abnormalities:** No recurrent, established epigenetic signature or characteristic karyotypic aberration is described; RDD is genomically quiet apart from the single-pathway MAPK drivers.

**Suggested gene/term annotations:** *MAP2K1* (hgnc:6840), *KRAS* (hgnc:6407), *NRAS* (hgnc:7989), *ARAF* (hgnc:646), *SLC29A3* (hgnc:23096), *FAS* (hgnc:11920); GO:0070371 (ERK1 and ERK2 cascade); GO:0000165 (MAPK cascade).

---

## 5. Environmental Information

- **Environmental factors:** No confirmed toxic, radiation, or occupational exposure.
- **Lifestyle factors:** None established.
- **Infectious agents:** EBV, HHV-6, parvovirus B19, *Klebsiella*, *Brucella* have all been proposed as triggers historically; **none is confirmed causal**. Current consensus does not classify RDD as an infectious disease. (NCBITaxon references would be speculative and should not be added as causal.)

This section is largely **not applicable / negative** — worth recording explicitly so the KB doesn't imply an environmental etiology.

---

## 6. Mechanism / Pathophysiology

**Causal chain (neoplastic/clonal arm — best supported):**

1. **Somatic MAPK-activating lesion** (e.g., *MAP2K1* p.Q56P, *KRAS* p.G12D) arises in a histiocyte/macrophage progenitor → 
2. **Constitutive RAS-RAF-MEK-ERK signaling** (GO:0070371 ERK1/ERK2 cascade) drives histiocyte proliferation and survival → 
3. **Clonal expansion of large, activated S100+ histiocytes** in nodal sinuses and extranodal tissue → 
4. **Emperipolesis** — engulfment (without destruction) of lymphocytes/plasma cells/erythrocytes by these histiocytes (a non-specific but characteristic morphologic readout) → 
5. **Mass effect and tissue infiltration** → organ-specific manifestations (lymphadenopathy, CNS mass, renal/pulmonary infiltration) and an accompanying **plasma-cell-rich, polyclonal inflammatory infiltrate** (→ hypergammaglobulinemia, elevated ESR).

**Reactive/immune arm (mutation-negative cases):** dysregulated, cytokine-driven macrophage activation (a "phagocytic storm" of activated M2-like macrophages) with prominent plasmacytosis, possibly downstream of immune dysregulation or autoimmunity, producing the same histiocyte morphology without demonstrable clonal driver.

**Cellular identity of the RDD histiocyte.** The cell is a **late-activated, monocyte-derived macrophage / "RDD histiocyte"** with an immunophenotype intermediate between macrophage and dendritic cell:
- **Positive:** S100 (nuclear + cytoplasmic), CD68, CD163 (macrophage), fascin, CD14, **OCT2**, **cyclin D1** (the latter two increasingly used diagnostically and consistent with cell-cycle/ERK activation).
- **Negative:** **CD1a−, CD207/langerin−** (excludes Langerhans cell histiocytosis); ALK−.

Suggested **CL** terms: CL:0000235 (macrophage); CL:0000576 (monocyte); CL:0000842 (mononuclear cell). Suggested **GO**: GO:0070371 (ERK1/ERK2 cascade), GO:0000165 (MAPK cascade), GO:0006909 (phagocytosis), GO:0002281 (macrophage activation involved in immune response), GO:0008283 (cell population proliferation).

**Protein dysfunction:** MEK1 (MAP2K1) and KRAS gain-of-function → unregulated downstream kinase activity. ENT3 (SLC29A3) loss → impaired lysosomal nucleoside efflux.

**Immune involvement:** central — RDD is a disorder of the mononuclear phagocyte system with a heavy reactive plasma-cell/lymphocyte component; ~10% co-occur with autoimmune disease; IgG4+ plasma cells are increased in a subset (overlap with IgG4-related disease).

**Upstream vs downstream:** Upstream = MAPK driver mutation (or immune-dysregulatory trigger); midstream = clonal histiocyte proliferation + emperipolesis + plasmacytosis; downstream = mass effect, organ infiltration, systemic inflammatory phenotype.

**Molecular profiling:** Targeted/whole-exome sequencing is the main modality (above). No established transcriptomic/proteomic/metabolomic disease signature is in routine use; single-cell and spatial data are emerging but not yet definitive.

---

## 7. Anatomical Structures Affected

- **Primary:** lymph nodes (UBERON:0000029), especially cervical (UBERON:0000029 / cervical lymph node UBERON:0002429). Classic disease = lymphatic system (UBERON:0006558 lymphoid system / UBERON:0001744 lymphoid tissue).
- **Extranodal (any organ; most frequent):**
  - Skin (UBERON:0002097) and subcutaneous soft tissue
  - Orbit/eye and adnexa (UBERON:0001697 orbit; UBERON:0000970 eye)
  - Nasal cavity / paranasal sinuses (UBERON:0001707 nasal cavity)
  - Central nervous system — dura/meninges (UBERON:0002361 meninges), brain (UBERON:0000955), spinal cord (UBERON:0002240)
  - Bone (UBERON:0001474) — metaphysis/diaphysis of long bones
  - Kidney (UBERON:0002113); lung (UBERON:0002048); upper respiratory/airway
  - Salivary glands, breast (UBERON:0000310), GI tract, soft tissue
- **Body systems:** lymphatic/hematopoietic, integumentary, nervous, respiratory, urinary, skeletal, ocular.
- **Tissue/cell level:** expanded nodal **sinuses** lined/filled by histiocytes; connective/soft tissue at extranodal sites (more fibrotic, fewer histiocytes). Target cell = activated macrophage (CL:0000235).
- **Subcellular:** RAS/MEK signaling at the plasma membrane/cytosol; ENT3 localizes to lysosomal/mitochondrial membranes (GO:0005764 lysosome) in the familial form; nuclear S100/OCT2/cyclin D1 staining.
- **Lateralization:** classic cervical lymphadenopathy is **bilateral**; extranodal lesions are often focal/asymmetric.

---

## 8. Temporal Development

- **Onset:** classic nodal form — childhood/young adulthood (historical mean ~20.6 y); extranodal and molecularly-profiled cohorts — adult/older adult (median ~50–57 y). Onset pattern usually **subacute to chronic/insidious**; lymphadenopathy may enlarge over weeks–months.
- **Progression / course:** highly variable — **self-limited** in many nodal/cutaneous cases (spontaneous remission in ~20–50% of nodal/cutaneous disease per consensus) vs. **relapsing-remitting** over years vs. **progressive** organ-infiltrative disease in a minority. *"Outcomes are usually favorable, particularly for cases of nodal and cutaneous disease, which are often self-limited. Other patients experience an unpredictable clinical course, with alternating periods of remission and reactivation lasting years"* (paraphrase of Abla et al., PMID 29720485 — **verify**).
- **Staging:** no formal AJCC-style staging; prognosis correlates with the **number of nodal groups and extranodal systems** involved.
- **Remission:** both spontaneous and treatment-induced.
- **Critical intervention windows:** organ-threatening sites (CNS/spinal compression, airway, orbit with visual compromise) require timely debulking/therapy.

---

## 9. Inheritance and Population

**Epidemiology.**
- **Prevalence:** ~1 in 200,000 (consensus estimate, PMID 29720485).
- **Incidence:** ~**100 new cases per year in the US** (consensus estimate).
- **Age:** historically mean ~20.6 y for classic nodal disease; median ~50 y in mixed/extranodal contemporary series.
- **Sex:** slight **male predominance** in classic nodal disease (~1.4:1); some extranodal/cutaneous series show female predominance — overall roughly balanced and series-dependent.
- **Ethnicity/geography:** classic nodal form more frequent in individuals of **African descent**; cutaneous RDD more common in **Asian** patients (especially women); sinonasal disease more common in Asian patients.

**Genetic-etiology parameters:**
- **Inheritance:** sporadic RDD is **not inherited** (somatic/acquired). The **familial form** (*SLC29A3*) is **autosomal recessive** (OMIM 602782); FAS-associated RDD follows ALPS (autosomal dominant with variable penetrance).
- **Penetrance/expressivity:** *SLC29A3*-related disease shows **wide intrafamilial variability** — the *same* c.1088G>A allele can produce H syndrome in one relative and RDD in another (PMC8522101).
- **Consanguinity / founder effects:** familial *SLC29A3* disease clusters in consanguineous Middle Eastern/South Asian families (Faisalabad histiocytosis).
- **Anticipation / mosaicism:** not described.

**Demographics:** affects all populations; no single endemic region; sex and ethnic skews are subtype-dependent as above.

---

## 10. Diagnostics

**Diagnosis is histopathologic**, integrated with clinical and radiologic context (and exclusion of mimics).

- **Biopsy / histopathology (gold standard):** large histiocytes with abundant pale/"watery-clear" cytoplasm, vesicular nuclei with prominent nucleoli, and **emperipolesis**; admixed plasma cells and lymphocytes; sinus expansion in nodal disease; more fibrosis/fewer histiocytes extranodally. *"The presence of RDD histology is required, but not sufficient, for diagnosis"* (paraphrase, PMID 29720485 — **verify**).
- **Immunohistochemistry panel** (recommended: CD68, CD163, S100, OCT2, cyclin D1, CD1a, langerin, ALK):
  - **Positive:** S100 (nuclear+cytoplasmic), CD68, CD163, fascin, OCT2, cyclin D1.
  - **Negative:** CD1a, CD207/langerin (→ excludes LCH), ALK.
- **Molecular testing:** targeted NGS for MAPK-pathway mutations (*MAP2K1*, *KRAS*, *NRAS*, *ARAF*; confirm BRAF-V600E status) — increasingly standard because it identifies clonal disease and guides MEK-inhibitor therapy.
- **Laboratory:** elevated ESR, polyclonal hypergammaglobulinemia, anemia (sometimes autoimmune hemolytic), variable leukocytosis. None is specific.
- **Imaging:** CT/MRI to map nodal/extranodal extent; PET-CT for whole-body assessment and treatment response (FDG-avid lesions); MRI essential for CNS/spinal disease (dural-based, contrast-enhancing, meningioma-mimicking).
- **Genetic testing (familial):** germline *SLC29A3* sequencing when familial RDD / H-syndrome features are present; *FAS* testing if ALPS features.
- **Differential diagnosis (key mimics to exclude):** Langerhans cell histiocytosis (CD1a+/langerin+), Erdheim-Chester disease (BRAF-V600E+, "foamy" histiocytes, CD163+/S100±), lymphoma (esp. Hodgkin and ALCL), reactive sinus histiocytosis, IgG4-related disease, metastatic carcinoma/melanoma (S100+ — emperipolesis and CD68/CD163 help), tuberculosis/other granulomatous disease, juvenile xanthogranuloma.

**Screening:** No population screening. For *SLC29A3* families, cascade genetic testing/counseling is appropriate.

---

## 11. Outcome / Prognosis

- **Overall:** generally **favorable**, especially nodal and cutaneous disease (frequently self-limited). Course is unpredictable with remission-reactivation cycles.
- **Mortality:** historical disease-related mortality **~7%** (Foucar et al., 17/238) to **~12%** (Pulsoni et al., 10/80).
- **High-risk / poor-prognosis features:**
  - **Multifocal / multisystem disease** (prognosis worsens with number of nodal groups and extranodal systems involved)
  - **Renal involvement (~40% mortality)**
  - **Lower respiratory / pulmonary involvement (~45% mortality)**
  - **GI involvement (~20% mortality in one series)**
  - CNS disease (morbidity from mass effect/compression)
  - Immune dysregulation / associated autoimmune disease
- **Morbidity:** disfigurement, visual loss (orbital), neurologic deficits (CNS/spinal), airway compromise, organ dysfunction.
- **Prognostic/predictive biomarkers:** **KRAS/MEK (MAP2K1) mutation status predicts response to MEK inhibition** (see §12) — a genuinely actionable prognostic/predictive marker.

---

## 12. Treatment

There is no single standard; therapy is **site- and severity-driven**, codified in the 2018 consensus (PMID 29720485) and NCCN histiocytosis guidelines.

- **Observation** — for asymptomatic/uncomplicated nodal or cutaneous disease; **20–50% of nodal/cutaneous cases remit spontaneously**. → MAXO:0000950 (supportive care) / watchful waiting.
- **Surgery** — curative for unifocal disease; debulking for airway obstruction, spinal cord compression, orbital/organ compromise; excision is the most effective treatment for localized cutaneous RDD. → MAXO:0000004 (surgical procedure).
- **Corticosteroids** — first-line systemic agent for symptomatic disease (prednisone ~40–70 mg/day or 1 mg/kg/day with taper; dexamethasone 8–20 mg/day); variable, often non-durable. → NCIT:C15986 (Pharmacotherapy) + therapeutic_agent CHEBI prednisone/dexamethasone; NCIT corticosteroid class.
- **Chemotherapy** — for refractory/systemic disease: **cladribine** (2-CdA, 5 mg/m²×5 q28d) and **clofarabine** (notably effective in children/refractory disease); low-dose **methotrexate + 6-mercaptopurine**; vinca alkaloids (variable). → MAXO:0000647 (chemotherapy) + CHEBI cladribine/clofarabine/methotrexate.
- **Immunomodulatory** — **thalidomide/lenalidomide** (cutaneous and refractory nodal/bone disease); **rituximab** (autoimmune-associated RDD); **sirolimus** (mTOR inhibitor; resistant RDD with autoimmune cytopenias). 
- **Targeted therapy — MEK inhibition (the major recent advance):**
  - **Cobimetinib** received **FDA approval (Nov 2022)** for adults with histiocytic neoplasms, including RDD — the first agent approved across all forms of histiocytosis.
  - Retrospective cohort (Abeykoon et al., **JAMA Oncol 2022, PMID 36201194**, n=16): **overall response 63%** (5 CR + 5 PR); median PFS 21.4 months. **Outcomes were markedly better in KRAS/MEK-altered patients:** response **88% vs 38%** (P=.03), CR among responders **71% vs 0%** (P=.002), and at 1 year **100% vs 29% free from progression/death**. Grade ≥2 toxicity in 75%; 56% needed dose reduction/discontinuation. → MAXO/NCIT pharmacotherapy; therapeutic_agent **cobimetinib** (CHEBI:90851 — verify); `therapeutic_modality: SMALL_MOLECULE`.
  - Other reports: trametinib (incl. topical), and BRAF inhibitors are *not* indicated (RDD is BRAF-V600E−).
- **Radiotherapy** — modest, mainly for refractory soft-tissue/orbital disease with visual compromise or palliation (30–50 Gy). → MAXO:0000014 (radiation therapy).
- **Treatment strategy / personalized medicine:** test for MAPK mutations → MEK inhibitor (cobimetinib) for KRAS/MAP2K1-mutated or multisystem/refractory disease; reserve cytotoxics/immunomodulators for mutation-negative or MEK-refractory cases; observe indolent localized disease.

**Active trials:** Central China RDD Registry (NCT05284942); Lenalidomide + dexamethasone for RDD (NCT04924647); cobimetinib basket trial (NCT02649972). *Verify status before citing as `clinical_trials` entries.*

---

## 13. Prevention

- **Primary prevention:** **None** — sporadic RDD is not preventable (no modifiable cause). 
- **Secondary prevention:** no population screening; early biopsy of persistent massive lymphadenopathy/organ masses enables timely diagnosis.
- **Genetic counseling:** relevant only for **familial *SLC29A3* (autosomal recessive)** and **FAS/ALPS** kindreds — carrier testing, cascade screening, reproductive counseling; prenatal/preimplantation testing is theoretically possible for known familial variants. → MAXO:0000079 (genetic counseling).
- **Tertiary prevention:** treat organ-threatening disease early to prevent permanent deficits (vision, neurologic, renal, respiratory); monitor for relapse.
- **Immunization / public health / behavioral / environmental measures:** **not applicable** (no infectious or environmental cause established).

---

## 14. Other Species / Natural Disease

- **Taxonomy:** RDD is essentially a **human disease** (NCBITaxon:9606).
- **Veterinary / natural disease:** Rare RDD-like / emperipolesis-positive histiocytic proliferations have been described anecdotally in animals, but RDD is **not an established naturally-occurring veterinary entity**, and there is no OMIA entry analogous to sporadic human RDD. → Largely **not applicable**.
- **Comparative biology / orthologs:** human driver genes have clear orthologs (*Map2k1*, *Kras*, *Nras*, *Slc29a3* in mouse), enabling mechanistic modeling, but spontaneous cross-species RDD disease is not documented.
- **Zoonotic potential:** none (non-infectious).

This section is best recorded as **not applicable / no established natural animal disease**.

---

## 15. Model Organisms

There is **no widely-used, faithful animal model that recapitulates RDD** specifically — a genuine knowledge gap (candidate for a `KNOWLEDGE_GAP` discussion in the entry).

- **Mouse (*Mus musculus*, MGI):** conditional MAPK-activation alleles (e.g., *Kras^G12D*, *Map2k1*-activating, *Braf* models) in the myeloid/histiocyte lineage produce **histiocytic/macrophage proliferations** and model the broader histiocytosis MAPK paradigm, but none reproduces RDD's full clinicopathologic picture (emperipolesis, S100+ phenotype, sinus expansion). *Slc29a3*-knockout mice model the familial/lysosomal arm (macrophage lysosomal nucleoside accumulation, histiocytic infiltration) and are the most disease-relevant genetic model.
- **In vitro / cellular:** primary patient histiocytes and macrophage cultures bearing MAPK mutations are used to study ERK signaling and MEK-inhibitor response; iPSC/organoid RDD models are not established.
- **Applications:** MAPK-driver mouse models and patient-derived cells are most useful for **mechanism (ERK signaling)** and **MEK-inhibitor pharmacology**; *Slc29a3* mice for the lysosomal/familial mechanism.
- **Limitations:** emperipolesis and the characteristic S100+ RDD histiocyte morphology are **poorly recapitulated**; the reactive/immune arm has no good model. → Recommend tagging model evidence `evidence_source: MODEL_ORGANISM` and noting human-model mismatch.
- **Resources:** MGI/IMPC for *Slc29a3*, *Map2k1*, *Kras*, *Nras* alleles.

---

## Priority Evidence Citations (verify each with `just fetch-reference` before committing)

| PMID | Anchor claim | Evidence type |
|---|---|---|
| **29720485** | Abla et al., *Blood* 2018 — international **consensus**: classification, epidemiology, organ frequencies, diagnosis, treatment, prognosis | HUMAN_CLINICAL (consensus) |
| **26966089** | Emile et al., *Blood* 2016 — revised histiocytosis classification, RDD in "R group" (DOI 10.1182/blood-2016-01-690636) | OTHER (classification/consensus) |
| **28664935** | Garces et al., *Mod Pathol* 2017 — **mutually exclusive KRAS & MAP2K1** mutations in ~1/3 of RDD; clonal MAPK activation | HUMAN_CLINICAL / molecular |
| **36201194** | Abeykoon et al., *JAMA Oncol* 2022 — **cobimetinib** outcomes by KRAS/MEK status (ORR 63%; 88% vs 38%) | HUMAN_CLINICAL (cohort) |
| **20140240** | Morgan et al., *PLoS Genet* 2010 — germline **SLC29A3/ENT3** in familial RDD & Faisalabad histiocytosis | HUMAN_CLINICAL / genetics |
| **32944792** | Pediatric recurrent RDD: germline *SLC29A3* + somatic *MAP2K1* | HUMAN_CLINICAL |
| **32591351** | Bruce-Brand et al., 2020 — "Rosai-Dorfman disease: an overview" | review |
| **36358690** | "Rosai-Dorfman Disease between Proliferation and Neoplasia," *Cancers* 2022 (PMC9654168) — mutation-frequency synthesis | review |

**Suggested MONDO mapping:** MONDO:0006412. **Module-conformance candidates** for the dismech entry: `tumor_promoting_inflammation` (reactive/inflammatory arm) and `sustaining_proliferative_signaling` (the constitutive MAPK/ERK driver arm) — RDD is a clean example of a histiocytosis sitting on the inflammation↔clonal-neoplasia boundary, so a `mechanistic_hypotheses` block contrasting the **clonal-MAPK** vs **reactive-immune** models would capture the genuine scientific uncertainty.

---

**Sources:**
- [Consensus recommendations for the diagnosis and clinical management of Rosai-Dorfman-Destombes disease (Blood 2018, PMC6024636)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6024636/)
- [Mutually exclusive recurrent KRAS and MAP2K1 mutations in Rosai–Dorfman disease (Mod Pathol 2017, PMID 28664935)](https://pubmed.ncbi.nlm.nih.gov/28664935/)
- [Outcomes After Treatment With Cobimetinib in RDD by KRAS/MEK Status (JAMA Oncol 2022, PMC9539729)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9539729/)
- [Rosai–Dorfman Disease between Proliferation and Neoplasia (Cancers 2022, PMC9654168)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9654168/)
- [Revisiting the molecular landscape of RDD: WES of Saudi patients (Front Oncol 2025, PMC12094912)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12094912/)
- [Mutations in SLC29A3 cause familial histiocytosis / familial RDD (PLoS Genet 2010, PMID 20140240)](https://pubmed.ncbi.nlm.nih.gov/20140240/)
- [Pediatric recurrent RDD: germline SLC29A3 + somatic MAP2K1 (PMID 32944792)](https://pubmed.ncbi.nlm.nih.gov/32944792/)
- [How I Diagnose Rosai-Dorfman Disease (Am J Clin Pathol 2023)](https://academic.oup.com/ajcp/article/160/1/1/7160235)
- [Clinicopathological features, treatment approaches, and outcomes in RDD (PMC7012468)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7012468/)
- [FDA Approves Oral MEK Inhibitor Cobimetinib for Histiocytic Neoplasms (ASCO Post 2022)](https://ascopost.com/issues/december-10-2022/fda-approves-oral-mek-inhibitor-cobimetinib-for-histiocytic-neoplasms/)
- [Phenotypic intrafamilial variability with the same SLC29A3 mutation (PMC8522101)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8522101/)
- [Sinus histiocytosis with massive lymphadenopathy — GARD](https://rarediseases.info.nih.gov/diseases/7588/sinus-histiocytosis-with-massive-lymphadenopathy)
- [OMIM 602782 — Histiocytosis-lymphadenopathy plus syndrome](https://omim.org/entry/602782)
- [Rosai-Dorfman disease pathology — DermNet NZ](https://dermnetnz.org/topics/rosai-dorfman-disease-pathology)

*Curator reminder: the 2018 consensus quotes reproduced above came through the search tool as paraphrases of PMID 29720485. Before any of these become evidence `snippet:` values, fetch the real abstract (`just fetch-reference PMID:29720485`) and confirm exact substring matches, then run `just validate-references` and `just validate-terms-file`.*