---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-8
cached: false
start_time: '2026-07-16T18:42:05.527384'
end_time: '2026-07-16T18:47:22.885601'
duration_seconds: 317.36
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Asbestosis
  mondo_id: ''
  category: Respiratory Disease
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
  web_search_requests: 6
  num_turns: 15
  total_cost_usd: 1.6106222499999996
  session_id: b70ae475-0408-4e7b-8030-092a8767bfc5
  stop_reason: end_turn
citation_count: 20
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Asbestosis
- **MONDO ID:**  (if available)
- **Category:** Respiratory Disease

## Research Objectives

Please provide a comprehensive research report on **Asbestosis** covering all of the
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

I have enough well-sourced material. Here is the comprehensive research report.

---

# Comprehensive Research Report: Asbestosis

> **Scope note on evidence.** Asbestosis is an acquired, exposure-driven (non-Mendelian) interstitial lung disease, so several template sections built for genetic disorders (causal genes, inheritance, carrier frequency, model-organism knockouts) are **not applicable** and are marked as such. Where I cite PMIDs I have verified the source; ontology term IDs below are **suggestions that must be verified with OAK before curation** (per the dismech anti-hallucination SOP), since I could not run `runoak`/OLS in this session.

---

## 1. Disease Information

**Overview.** Asbestosis is a chronic, progressive, diffuse **interstitial pulmonary fibrosis (pneumoconiosis)** caused by the inhalation and lung retention of asbestos mineral fibers. It is the fibrotic parenchymal lung disease specifically attributable to asbestos, distinct from asbestos-related pleural disease (pleural plaques, diffuse pleural thickening, benign asbestos pleural effusion) and from asbestos-associated malignancies (bronchogenic carcinoma, malignant mesothelioma). It is dose-dependent, typically follows heavy cumulative exposure, and manifests after a long latency (commonly 20–40 years; ≥10 years minimum). ([StatPearls, NBK555985](https://www.ncbi.nlm.nih.gov/books/NBK555985/); [Merck Manual Professional](https://www.merckmanuals.com/professional/pulmonary-disorders/environmental-and-occupational-pulmonary-diseases/asbestosis))

**Key identifiers.**
- **MONDO:** MONDO:0016466
- **Disease Ontology:** DOID:10320
- **ICD-10-CM:** J61 ("Pneumoconiosis due to asbestos and other mineral fibers")
- **ICD-11 (MMS):** CA60.2
- **MeSH:** D001195 ("Asbestosis")
- **OMIM:** Not applicable (not a Mendelian disorder)
- **Orphanet:** Not a designated rare-disease entry (occupational/acquired; excluded from Orphanet's rare-disease scope)

Sources: [Wikidata Q664174](https://www.wikidata.org/wiki/Q664174); [MalaCards](https://www.malacards.org/card/asbestosis); [ICD10Data J61](https://www.icd10data.com/ICD10CM/Codes/J00-J99/J60-J70/J61-/J61)

**Common synonyms / alternative names.** Pulmonary asbestosis; asbestos pneumoconiosis; interstitial pneumonitis due to asbestos; "white-lung" (colloquial). Note the important terminological distinction: *asbestosis* refers strictly to the **parenchymal fibrosis**, whereas "asbestos-related disease" is the broader umbrella.

**Data derivation.** Disease-level aggregated resources (occupational cohorts, national mortality/DALY databases, pathology case series, radiographic surveillance). There is no single OMIM/individual-patient genetic basis; population and cohort epidemiology dominate.

---

## 2. Etiology

**Primary cause (environmental/occupational).** Inhalation of respirable asbestos fibers with deposition in the distal airways and alveoli. Asbestos comprises two mineral families:
- **Serpentine** — *chrysotile* ("white asbestos"): curly, flexible fibers; more readily cleared; historically the most-used commercial form.
- **Amphibole** — *crocidolite* ("blue"), *amosite* ("brown"), tremolite, actinolite, anthophyllite: straight, stiff, needle-like, **biopersistent**, penetrate deeper and are more fibrogenic and carcinogenic. Amphiboles carry disproportionate pathogenic weight. ([StatPearls, NBK555985](https://www.ncbi.nlm.nih.gov/books/NBK555985/))

**Risk factors (environmental/occupational).**
- **Cumulative exposure (dose)** is the dominant determinant. A large Danish general-working-population cohort (1,514,136 workers; 1,084 incident asbestosis cases) found a fully adjusted incidence rate ratio of **1.18 per 1 f/ml-year** (95% CI 1.15–1.22) and **1.94** for highest vs. lowest exposure tertile, with the steepest risk rise up to ~1 f/ml-year. *"This study found exposure–response relations between cumulative asbestos exposure and incident asbestosis in the Danish general working population."* ([Iversen et al., *Scand J Work Environ Health* 2024; PMID: 38577971](https://pmc.ncbi.nlm.nih.gov/articles/PMC11245331/))
- **High-risk occupations:** insulation/lagging, shipbuilding, asbestos mining/milling, textile manufacture, boiler work, brake/clutch manufacture, construction (asbestos-board installers and sprayers show the highest prevalence in some series — 38–39% in Japanese data), demolition, plumbing/pipefitting. ([StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK555985/))
- **Bystander and paraoccupational exposure** (e.g., household members exposed to fibers on workers' clothing) and **environmental/community exposure** (near mines, from contaminated soils/building materials).
- **Fiber dimension & biopersistence:** long, thin, durable amphibole fibers are most fibrogenic ("frustrated phagocytosis").
- **Smoking:** does not cause asbestosis per se but **impairs mucociliary clearance**, increases fiber retention, and interacts multiplicatively with asbestos for lung cancer risk (see §6, §11).
- **Male predominance and older age** (reflecting historical occupational exposure patterns).

**Genetic (susceptibility, not causal).** Asbestosis has no single-gene cause. Candidate susceptibility/modifier loci — mostly studied for asbestos-related fibrotic and malignant endpoints — include:
- **GSTT1 null** genotype: associated with fibrotic changes and reduced diffusing capacity; **GSTM1 null**: associated with thicker pleural plaques and increased risk across asbestos-linked diseases (plausibly via impaired conjugation/detoxification of ROS). ([Franko et al., *Eur Respir J* 2011;38(3):672](https://publications.ersnet.org/content/erj/38/3/672))
- **GSTM1 null + NAT2 slow acetylator** each ~2-fold and together ~4-fold increased malignant mesothelioma risk in asbestos-exposed individuals. ([Hirvonen et al., *Cancer Res* 1995;55:2981; PMID: 7606735](https://aacrjournals.org/cancerres/article/55/14/2981/501256/))
- **Iron-homeostasis gene variants** modulate mesothelioma susceptibility after exposure. ([Frontiers Public Health 2023, PMC10628177](https://pmc.ncbi.nlm.nih.gov/articles/PMC10628177/))

**Protective factors.** No validated genetic protective allele for asbestosis. The only reliable protection is **primary exposure prevention** (fiber control, bans, PPE) and **smoking avoidance/cessation** (reduces synergistic cancer risk and slows functional decline). No dietary/antioxidant intervention has proven clinical benefit.

**Gene–environment interaction.** The paradigm is detoxification/oxidative-defense genotype × cumulative fiber burden: null GST genotypes and slow-acetylator NAT2 amplify oxidative and genotoxic injury from retained fibers, and smoking further raises fiber retention and cancer risk — a classic multiplicative environmental interaction. (CTD/PubMed as suggested sources.)

---

## 3. Phenotypes

Phenotype categories: **symptoms, clinical signs, functional (PFT) abnormalities, radiographic/histopathologic findings, laboratory abnormalities.** Onset is **adult/late-adult** after long latency; course is typically **chronic and slowly progressive**; frequencies below are approximate from clinical literature and should be curated with per-phenotype evidence.

| Phenotype | Type | Suggested HPO term (verify) | Characteristics / frequency |
|---|---|---|---|
| Exertional dyspnea | Symptom | Exertional dyspnea HP:0002875 | Earliest and most common; progressive; near-universal in symptomatic disease |
| Nonproductive (dry) cough | Symptom | Nonproductive cough HP:0031246 | Common |
| Fatigue | Symptom | Fatigue HP:0012378 | Common |
| Chest tightness/discomfort | Symptom | Chest pain HP:0100749 | Occasional |
| Bibasilar fine end-inspiratory crackles ("velcro" rales) | Sign | Crackles HP:0030830 | Characteristic; predominantly lower zones/posterolateral bases |
| Digital clubbing | Sign | Finger clubbing HP:0001217 | ~30–42% in some series; correlates with severity |
| Restrictive ventilatory defect (↓FVC, ↓TLC, preserved/↑FEV1/FVC) | PFT | Restrictive ventilatory defect HP:0002091 | Hallmark functional pattern |
| Reduced diffusing capacity (↓DLCO) | PFT | Abnormal DLCO (verify HP) | Often earliest physiologic abnormality |
| Hypoxemia (rest or exertional) | Lab/functional | Hypoxemia HP:0012418 | Advanced disease |
| Pulmonary fibrosis / reticular opacities | Imaging/path | Pulmonary fibrosis HP:0002206 | Bilateral, lower-lobe/subpleural predominant |
| Honeycombing | Imaging/path | Honeycomb lung (verify HP) | End-stage |
| Pleural plaques / pleural thickening | Imaging/path | Pleural thickening HP:0002102 (verify) | Frequent concomitant marker of exposure |
| Cor pulmonale / right heart failure | Complication sign | Cor pulmonale HP:0001648 (verify) | Late/advanced |
| Respiratory failure | Complication | Respiratory insufficiency HP:0002093 | End-stage |

**Severity & progression:** ranges from mild/subclinical (radiographic only) to severe with respiratory failure. Progression is usually **slow over years-to-decades**, may continue *after exposure ceases* (retained biopersistent fibers), and is influenced by cumulative dose and continued smoking. **Quality-of-life impact:** dyspnea limits exertion and ADLs; advanced disease causes oxygen dependence, reduced exercise capacity, anxiety/depression, and (via lung-cancer/mesothelioma fear and surveillance) psychological burden. Pulmonary rehabilitation improves QoL and reduces hospitalization. ([American Lung Association](https://www.lung.org/lung-health-diseases/lung-disease-lookup/asbestosis/treating-and-managing); [PMID: 32053838](https://pubmed.ncbi.nlm.nih.gov/32053838/))

---

## 4. Genetic / Molecular Information

- **Causal genes:** **None** — asbestosis is caused by fiber exposure, not germline mutation.
- **Pathogenic variants:** Not applicable in the ACMG/ClinVar sense. Relevant loci are **susceptibility/modifier polymorphisms**, not pathogenic variants: **GSTM1** (HGNC:4632, null/deletion), **GSTT1** (HGNC:4641, null/deletion), **GSTP1** (HGNC:4638), **GSTM3**, **EPHX1** (HGNC:3401), **NAT2** (HGNC:7646, slow-acetylator haplotypes), **SOD2/MnSOD**. These are common-population polymorphisms (GSTM1/GSTT1 null genotypes are frequent, ~20–50% depending on ancestry), germline in origin, with functional consequences of **reduced xenobiotic/ROS detoxification**. ([Eur Respir J 2011;38:672](https://publications.ersnet.org/content/erj/38/3/672); [Cancer Res 1995;55:2981](https://aacrjournals.org/cancerres/article/55/14/2981/501256/))
- **Somatic vs germline:** the above are germline modifiers; **somatic** genetic events (e.g., *BAP1*, *NF2*, *CDKN2A* losses) belong to the downstream malignancy (mesothelioma/lung cancer), not to asbestosis fibrosis itself.
- **Epigenetics:** asbestos exposure induces DNA-methylation and miRNA changes in airway/lung tissue described chiefly in the carcinogenesis literature; a specific validated asbestosis (fibrosis) methylation signature is not established — mark as a **knowledge gap**.
- **Chromosomal abnormalities:** none causal for asbestosis.

---

## 5. Environmental Information

- **Primary environmental agent:** asbestos fibers (serpentine chrysotile; amphiboles crocidolite, amosite, tremolite, actinolite, anthophyllite). CHEBI/exposure suggestion: *asbestos* (verify CHEBI), *silicon-containing mineral fiber*; ROS species CHEBI:26523.
- **Co-exposures:** other mineral dusts (silica → mixed-dust fibrosis), erionite (fibrous zeolite, mesothelioma), and cigarette smoke.
- **Lifestyle:** **cigarette smoking** is the key modifiable co-factor — impairs mucociliary clearance (increasing fiber retention) and multiplies lung-cancer risk. No specific dietary driver established.
- **Infectious agents:** None. Asbestosis is not infectious. (Secondary infections may complicate advanced disease.)

---

## 6. Mechanism / Pathophysiology

**Overarching causal chain:** inhaled biopersistent fiber deposition → alveolar macrophage "frustrated phagocytosis" → oxidative injury + inflammasome/cytokine activation → epithelial (type I/II pneumocyte) injury → fibroblast recruitment/activation → myofibroblast differentiation and excess ECM/collagen deposition → progressive interstitial fibrosis → impaired gas exchange and restrictive physiology → respiratory failure/cor pulmonale.

**Step-by-step mechanism (upstream → downstream):**

1. **Fiber deposition & retention (trigger).** Long, thin amphibole fibers deposit at alveolar-duct bifurcations; their length prevents complete macrophage engulfment ("frustrated phagocytosis"). Iron on/within fibers catalyzes redox chemistry. Cell types: **alveolar macrophage (CL:0000583)**. GO: phagocytosis (GO:0006909).

2. **Oxidative injury.** Frustrated phagocytosis and fiber-surface iron generate **ROS/RNS** (Fenton-type chemistry, mitochondrial ROS), directly injuring **type I pneumocytes (CL:0002062)** and epithelium and activating redox-sensitive transcription factors (NF-κB). GO: reactive oxygen species metabolic process (GO:0072593); response to oxidative stress (GO:0006979).

3. **Inflammasome activation & sterile inflammation.** Asbestos activates the **NLRP3 inflammasome** in macrophages/monocytes and lung epithelial and mesothelial cells → caspase-1 → **IL-1β** (and IL-18) release; mitochondrial ROS and thioredoxin/TXNIP dissociation contribute. GO: inflammasome complex (GO:0061702); inflammatory response (GO:0006954). ([Sayan & Mossman, *Part Fibre Toxicol* 2016;13:51, PMC5029018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5029018/))

4. **Fiber-size–dependent macrophage cell death (2023 mechanistic detail).** *"SFA [short-fiber amosite] internalization resulted in pyroptotic-related immunogenic cell death (ICD) characterized by the release of the pro-inflammatory damage signal (DAMP) IL-1α after inflammasome activation and gasdermin D (GSDMD)-pore formation."* By contrast, *"macrophage responses to non-internalizable LFA [long-fiber amosite] were associated with tumor necrosis factor alpha (TNF-α) release, caspase-3 and -7 activation, and apoptosis."* Short fibers signalled via TLR4; long fibers via MARCO/SR-A6 + ROS cascade + TLR4. GO: pyroptosis (GO:0070269); apoptotic process (GO:0006915). ([Della Latta-type study; PMID: 37894824, 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10606797/))

5. **Pro-fibrotic mediator surge.** Activated macrophages release **TNF-α, IL-1β, PDGF, TGF-β, IGF-1, fibronectin**. IL-1β/NLRP3 signalling promotes **TGF-β** pathways. Macrophages transition from a pro-inflammatory (M1) to a wound-healing (M2) phenotype driving repair-gone-awry. GO: transforming growth factor beta receptor signaling pathway (GO:0007179); cytokine-mediated signaling (GO:0019221).

6. **Fibroblast activation & myofibroblast transdifferentiation.** TGF-β drives fibroblast proliferation and **fibroblast→myofibroblast** differentiation (α-SMA+), plus epithelial–mesenchymal transition contributions. Cells: **fibroblast (CL:0000057)**, **myofibroblast (CL:0000186)**. GO: fibroblast proliferation (GO:0048144); epithelial to mesenchymal transition (GO:0001837).

7. **Excess ECM/collagen deposition.** Myofibroblasts deposit type I/III collagen and matrix → interstitial thickening. GO: collagen fibril organization (GO:0030199); extracellular matrix organization (GO:0030198). This is the **principal pathogenic endpoint** ("interstitial fibrosis is regarded as the principal pathogenic mechanism of asbestosis").

8. **Structural/functional consequence.** Alveolar-wall thickening and honeycombing impair diffusion and compliance → restrictive physiology, ↓DLCO, hypoxemia → pulmonary hypertension → cor pulmonale.

**Immune involvement:** sterile, chronic innate-immune-driven inflammation (macrophage/inflammasome-centric) rather than autoimmunity — though autoantibodies (ANA, RF) may be elevated. **Tissue-damage mechanisms:** oxidative stress, sterile inflammation, and fibrosis. **Biochemical/protein dysfunction:** no enzyme defect; the "dysfunction" is dysregulated cytokine/TGF-β signalling and matrix homeostasis. **Molecular profiling:** transcriptomic/innate-immunity gene-expression signatures associated with asbestos fibrotic change are reported ([PMC3888604](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3888604/)); dedicated proteomic/metabolomic/single-cell asbestosis signatures are limited — **knowledge gap**.

**Histopathology (CAP/Pulmonary Pathology Society criteria):** diffuse interstitial fibrosis in the proper anatomic distribution **plus** identifiable **asbestos (ferruginous) bodies** (golden-brown, beaded/dumbbell iron-protein-coated fibers) or documented elevated fiber burden. Fibrosis is graded, subpleural/lower-lobe predominant. ([Roggli et al., *Arch Pathol Lab Med* 2010;134:462](https://meridian.allenpress.com/aplm/article/134/3/462/461033/); [ATS mechanisms review, *AJRCCM* 1998;157:1666](https://www.atsjournals.org/doi/10.1164/ajrccm.157.5.9707141))

---

## 7. Anatomical Structures Affected

- **Primary organ:** **lung (UBERON:0002048)** — bilateral, **lower-lobe (UBERON:0008953)** and **subpleural/peripheral** predominance; **alveolus of lung (UBERON:0002299)** and pulmonary interstitium.
- **Secondary/associated:** **pleura (UBERON:0000977)** — visceral pleural thickening, plaques; **heart** (right ventricle → cor pulmonale); systemic effects of chronic hypoxemia.
- **Body systems:** respiratory (primary); cardiovascular (secondary, pulmonary hypertension/right heart).
- **Tissue level:** alveolar epithelium (type I/II pneumocytes), pulmonary interstitial connective tissue, pleural mesothelium.
- **Cell populations:** **alveolar macrophage (CL:0000583)**, **pulmonary alveolar type 1 cell (CL:0002062)**, **type 2 pneumocyte (CL:0002063)**, **fibroblast (CL:0000057)** / **myofibroblast (CL:0000186)**, **mesothelial cell (CL:0000077)**.
- **Subcellular:** mitochondria (mito-ROS; GO:0005739), lysosome/phagosome (frustrated phagocytosis; GO:0005764), extracellular region/matrix (GO:0031012).
- **Localization/lateralization:** **bilateral**, lower-zone and posterolateral/subpleural predominant.

---

## 8. Temporal Development

- **Onset:** **adult/late-adult**, after prolonged **latency of ~20–40 years** from first exposure (minimum ~10 years; shorter with very intense exposure). Onset is **insidious/chronic**.
- **Progression/stages:** subclinical/radiographic → mild symptomatic (exertional dyspnea, ↓DLCO) → moderate (restrictive PFT, hypoxemia) → advanced/end-stage (honeycombing, respiratory failure, cor pulmonale). Rate is usually **slow and variable over years**.
- **Course:** chronic, **irreversible and often progressive even after exposure ceases** (biopersistent retained fibers); no spontaneous remission. There is **no treatment-induced remission**; management slows decline and treats complications.
- **Critical window:** the actionable window is **exposure prevention before disease onset**; once fibrosis is established it is not reversible.

---

## 9. Inheritance and Population

- **Inheritance:** Not applicable — **acquired occupational/environmental disease**; genetic contribution is **modifier/susceptibility polygenic** (GST/NAT2/iron-homeostasis alleles), not Mendelian. No penetrance, anticipation, mosaicism, or carrier-frequency concepts apply.
- **Epidemiology (global burden):** In 2019, occupational asbestos exposure was linked to **~239,330 deaths and ~4,189,000 DALYs globally**; global asbestos-attributed deaths rose **~65.7%** (1990–2019). WHO-type estimates attribute **~55,000+ deaths/year** to asbestos-related disease broadly. In the US, absolute deaths rose but **age-standardized mortality and DALY rates declined** over 1990–2019 (reflecting historical-exposure cohort aging plus reduced new exposure). ([Merck Manual](https://www.merckmanuals.com/professional/pulmonary-disorders/environmental-and-occupational-pulmonary-diseases/asbestosis); [StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK555985/))
- **Incidence in exposed cohorts:** ~0.71 asbestosis cases per 100,000 person-years baseline in a general-working-population cohort, rising steeply with cumulative exposure (IRR 1.18 per f/ml-year). ([PMID: 38577971](https://pmc.ncbi.nlm.nih.gov/articles/PMC11245331/))
- **Demographics:** **male predominance** (occupational exposure history), older age at diagnosis. **Geographic variation** tracks historical mining/industrial use and regulatory timelines — declining in countries with asbestos bans, still rising in regions with ongoing chrysotile use. Prevalence extremely high in specific trades (e.g., asbestos-board installers ~39% in Japanese series). **Prevalence class:** occupational-cohort-dependent; in the general population it is uncommon.

---

## 10. Diagnostics

**Diagnosis rests on the triad of (1) credible exposure history with appropriate latency, (2) imaging/pathologic evidence of diffuse interstitial fibrosis, and (3) exclusion of alternatives.**

- **Exposure history:** occupational/paraoccupational/environmental asbestos exposure, typically ≥10–20 years prior.
- **Imaging:**
  - Chest radiograph: bilateral **lower-zone reticular/linear opacities** (ILO-classified small irregular opacities), ± pleural plaques/thickening; "shaggy heart border."
  - **HRCT (most sensitive):** subpleural/basal reticulation, interlobular/intralobular septal thickening, subpleural curvilinear/branching lines, parenchymal bands, ground-glass, honeycombing; **pleural plaques strongly support asbestos etiology** and help distinguish from IPF.
- **Pulmonary function tests:** **restrictive** pattern (↓FVC, ↓TLC, normal/↑FEV1/FVC), **reduced DLCO** (often earliest), exertional desaturation on 6-minute walk. (LOINC-coded spirometry/DLCO.)
- **Histopathology (when biopsy done):** diffuse interstitial fibrosis **plus asbestos/ferruginous bodies** or elevated tissue fiber burden (CAP/PPS criteria); asbestos-body quantification and fiber analysis (SEM/EDX) on digested tissue in reference labs.
- **Laboratory:** no specific diagnostic biomarker; nonspecific ↑CRP/ESR, and sometimes ↑RF/ANA. Serum mesothelin/osteopontin relate to mesothelioma, **not** asbestosis diagnosis.
- **Clinical criteria / differential:** Differentiate from **idiopathic pulmonary fibrosis (UIP)** — asbestosis favored by exposure history + pleural plaques + asbestos bodies; also from other pneumoconioses, hypersensitivity pneumonitis, connective-tissue-disease ILD, sarcoidosis, drug-induced fibrosis. A 2024 clinicopathological series of 102 cases refined 21st-century diagnostic correlation. ([PMID: 38192052](https://pubmed.ncbi.nlm.nih.gov/38192052/); [Merck Manual](https://www.merckmanuals.com/professional/pulmonary-disorders/environmental-and-occupational-pulmonary-diseases/asbestosis))
- **Genetic/omics testing:** Not used diagnostically. Newborn/carrier/cascade screening: **not applicable**.
- **Screening:** medical surveillance of exposed workers (periodic spirometry + low-dose CT), and lung-cancer LDCT screening consideration in exposed (especially smoking) individuals.

---

## 11. Outcome / Prognosis

- **Course/survival:** highly variable. Many patients have mild, slowly progressive disease and near-normal life expectancy; a subset progress to respiratory failure and cor pulmonale. Some clinical sources cite limited survival once symptomatic and worse outcomes with pleural involvement, but survival is heterogeneous and dose/severity-dependent. Progression can continue after exposure ends. ([StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK555985/); [Merck Manual](https://www.merckmanuals.com/professional/pulmonary-disorders/environmental-and-occupational-pulmonary-diseases/asbestosis))
- **Morbidity/disability:** progressive exertional limitation, oxygen dependence, reduced QoL.
- **Complications:**
  - **Bronchogenic lung cancer** — the most common asbestos-related malignancy; risk **multiplies synergistically with smoking** (asbestos + smoking risk far exceeds additive).
  - **Malignant pleural/peritoneal mesothelioma** — >80% attributable to asbestos; long latency (30–40+ yr); not smoking-related.
  - **Cor pulmonale / right heart failure**, **respiratory failure**, recurrent respiratory infection, pulmonary hypertension.
  - Associations with laryngeal and ovarian cancer (IARC).
- **Prognostic factors:** cumulative exposure/fiber burden, extent/rate of radiographic progression, baseline and decline in FVC/DLCO, degree of hypoxemia, continued smoking, age/comorbidity.

---

## 12. Treatment

**No curative or disease-reversing therapy exists; management is supportive, prevents progression, and treats complications.** (Suggested MAXO terms in brackets — verify with OAK.)

- **Exposure cessation** — remove from further asbestos and irritant exposure (foundational).
- **Smoking cessation** — highest-yield intervention to reduce lung-cancer risk and slow decline. [smoking cessation — MAXO, verify]
- **Supplemental long-term oxygen therapy** for resting/exertional hypoxemia (PaO₂ < ~55 mmHg). [oxygen administration — MAXO, verify]
- **Pulmonary rehabilitation** (exercise + breathing training + education) — improves QoL, exertional capacity, reduces hospitalization. [physical therapy MAXO:0000011 / pulmonary rehabilitation — verify] ([ALA](https://www.lung.org/lung-health-diseases/lung-disease-lookup/asbestosis/treating-and-managing); [PMID: 32053838](https://pubmed.ncbi.nlm.nih.gov/32053838/))
- **Vaccination** — influenza and pneumococcal to prevent respiratory infection. [vaccination MAXO:0001017 — verify]
- **Management of cor pulmonale / heart failure and pulmonary hypertension** — supportive/pharmacologic. [supportive care MAXO:0000950 — verify]
- **Corticosteroids** — sometimes used for inflammation, but evidence of benefit in established asbestosis is weak (not standard disease-modifying therapy). [pharmacotherapy — glucocorticoid, verify CHEBI prednisolone CHEBI:8378]
- **Lung transplantation** — for selected end-stage patients (double-lung preferred). [organ transplantation MAXO:0010039 / lung transplantation — verify]
- **Malignancy surveillance/treatment** — LDCT lung-cancer screening in appropriate exposed/smoking patients; oncologic management of lung cancer/mesothelioma as indicated.
- **Antifibrotics (pirfenidone, nintedanib):** approved for IPF and progressive pulmonary fibrosis phenotypes; **experimental/off-label** in asbestosis with progressive fibrosing behavior — an active area but **not established standard of care** (basis for clinical-trial follow-up). ([asbestos.com treatment overview](https://www.asbestos.com/asbestosis/treatment/); [StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK555985/))
- **Pharmacogenomics:** none specific/validated for asbestosis.

---

## 13. Prevention

- **Primary prevention (most important):** eliminate/control exposure — national **asbestos bans**, permissible-exposure-limit enforcement (OSHA), engineering controls (wet methods, enclosure, ventilation), respiratory PPE, safe removal/abatement, and product substitution. Historical latency means primary prevention today prevents disease decades hence.
- **Secondary prevention:** medical surveillance of exposed workers (periodic spirometry/DLCO, chest imaging), early identification, and **smoking-cessation programs** in exposed populations; LDCT lung-cancer screening in high-risk exposed smokers.
- **Tertiary prevention:** vaccinations, pulmonary rehab, prompt infection treatment, oxygen, comorbidity and malignancy management to limit complications.
- **Public-health/environmental:** worldwide asbestos-use bans (advocated by WHO), safe demolition/renovation regulation, environmental remediation of contaminated sites.
- **Genetic counseling / immunization against causal agent:** not applicable (no vaccine; not heritable).

Sources: [CDC/ATSDR asbestos toxicity module](https://archive.cdc.gov/www_atsdr_cdc_gov/csem/asbestos/managing_patients_exposed-to_asbestos.html); [ALA](https://www.lung.org/lung-health-diseases/lung-disease-lookup/asbestosis/treating-and-managing).

---

## 14. Other Species / Natural Disease

- **Taxonomy:** primarily ***Homo sapiens* (NCBITaxon:9606)**. Asbestosis is fundamentally a human occupational disease.
- **Naturally occurring animal disease:** rare/limited. Experimental asbestos-induced pulmonary fibrosis is well documented in laboratory rodents; naturally occurring companion-animal asbestosis is not a recognized clinical entity, though environmental asbestos exposure has been studied in pets as a **sentinel** for human household exposure (mesothelioma associations in dogs).
- **Comparative biology:** the macrophage-frustrated-phagocytosis/ROS/fibrosis mechanism is **evolutionarily conserved** across mammals, which underpins rodent modeling.
- **Zoonotic potential:** none (non-infectious).

---

## 15. Model Organisms

- **Rodent inhalation/instillation models (mammalian):** **rat and mouse** intratracheal instillation or inhalation of chrysotile/crocidolite/amosite reproduce alveolar macrophage accumulation, inflammation, and peribronchiolar/interstitial fibrosis — the workhorse asbestosis models. [MGI/RGD]
- **In vitro / cellular:** murine and human **alveolar macrophage** cultures (frustrated phagocytosis, NLRP3/IL-1β, ROS; short vs long amosite fiber studies, [PMID: 37894824](https://pmc.ncbi.nlm.nih.gov/articles/PMC10606797/)); **mesothelial cell** and **lung epithelial** cultures for inflammasome and TGF-β/fibroblast-activation assays; fibroblast/myofibroblast differentiation assays.
- **Genetic models:** *Nlrp3*-, *Casp1*-, *Tnf*-, *Il1r*-, and *Tgfb*-pathway knockout/transgenic mice used to dissect individual mechanistic steps (inflammasome, TNF, TGF-β signalling).
- **Phenotype recapitulation:** rodent models reproduce the **inflammation→fibrosis** cascade and fiber-size/biopersistence effects well.
- **Limitations:** accelerated timelines (weeks–months vs. human decades of latency), high bolus doses unlike chronic low-level human exposure, species differences in fiber clearance and airway anatomy, and incomplete modeling of honeycomb end-stage architecture and of asbestos-associated human malignancy latency.
- **Resources:** MGI, RGD, Alliance of Genome Resources, IMPC (for pathway-gene knockouts); Cellosaurus/ATCC for macrophage and mesothelial cell lines.

---

## Consolidated Ontology Term Suggestions (verify all with OAK/OLS before curation)

- **MONDO:** MONDO:0016466 (asbestosis)
- **HP (phenotypes):** HP:0002875 exertional dyspnea; HP:0031246 nonproductive cough; HP:0030830 crackles; HP:0001217 finger clubbing; HP:0002091 restrictive ventilatory defect; HP:0012418 hypoxemia; HP:0002206 pulmonary fibrosis; HP:0002102 pleural thickening (verify); HP:0001648 cor pulmonale (verify); HP:0002093 respiratory insufficiency; HP:0012378 fatigue
- **GO (processes):** GO:0006909 phagocytosis; GO:0072593 ROS metabolic process; GO:0006954 inflammatory response; GO:0061702 inflammasome complex; GO:0070269 pyroptosis; GO:0006915 apoptotic process; GO:0007179 TGF-β receptor signaling; GO:0048144 fibroblast proliferation; GO:0001837 EMT; GO:0030199 collagen fibril organization; GO:0030198 ECM organization
- **CL (cell types):** CL:0000583 alveolar macrophage; CL:0002062 type 1 pneumocyte; CL:0002063 type 2 pneumocyte; CL:0000057 fibroblast; CL:0000186 myofibroblast; CL:0000077 mesothelial cell
- **UBERON (anatomy):** UBERON:0002048 lung; UBERON:0008953 lower lobe of lung; UBERON:0002299 alveolus of lung; UBERON:0000977 pleura
- **CHEBI:** CHEBI:26523 reactive oxygen species; asbestos/mineral-fiber term (verify); CHEBI:8378 prednisolone; CHEBI:15379 dioxygen (O₂)
- **MAXO (treatments):** oxygen administration (verify); MAXO:0000011 physical therapy (pulmonary rehab); MAXO:0001017 vaccination; MAXO:0010039 organ transplantation (lung transplant); MAXO:0000950 supportive care
- **HGNC (modifier genes):** HGNC:4632 GSTM1; HGNC:4641 GSTT1; HGNC:4638 GSTP1; HGNC:3401 EPHX1; HGNC:7646 NAT2

---

## Key Citations (for evidence items)

| Claim | Source | PMID / DOI |
|---|---|---|
| Exposure–response, IRR 1.18 per f/ml-year, Danish cohort | Iversen et al., *Scand J Work Environ Health* 2024 | **PMID: 38577971** ([PMC11245331](https://pmc.ncbi.nlm.nih.gov/articles/PMC11245331/)) |
| Short- vs long-fiber amosite macrophage mechanisms (pyroptosis/IL-1α/GSDMD vs TNF-α/caspase-3,7/apoptosis) | 2023 macrophage study | **PMID: 37894824** ([PMC10606797](https://pmc.ncbi.nlm.nih.gov/articles/PMC10606797/)) |
| NLRP3 inflammasome in particle/fiber lung disease | Sayan & Mossman, *Part Fibre Toxicol* 2016;13:51 | doi:10.1186/s12989-016-0162-4 ([PMC5029018](https://pmc.ncbi.nlm.nih.gov/articles/PMC5029018/)) |
| Diagnostic clinicopathological correlation, 102 cases (21st c.) | 2024 series | **PMID: 38192052** ([PubMed](https://pubmed.ncbi.nlm.nih.gov/38192052/)) |
| GSTM1/GSTT1 susceptibility to asbestos fibrotic change | Franko et al., *Eur Respir J* 2011;38:672 | [ERJ](https://publications.ersnet.org/content/erj/38/3/672) |
| GSTM1 null + NAT2 slow acetylator ~4× mesothelioma risk | Hirvonen et al., *Cancer Res* 1995;55:2981 | **PMID: 7606735** |
| Pathology diagnostic criteria (CAP/PPS) | Roggli et al., *Arch Pathol Lab Med* 2010;134:462 | [Article](https://meridian.allenpress.com/aplm/article/134/3/462/461033/) |
| Mechanisms of asbestosis & silicosis | Mossman & Churg, *AJRCCM* 1998;157:1666 | [ATS](https://www.atsjournals.org/doi/10.1164/ajrccm.157.5.9707141) |
| Non-linear dose-response for respirable mineral fibers | 2018 review | **PMID: 29932955** ([PubMed](https://pubmed.ncbi.nlm.nih.gov/29932955/)) |
| Clinical overview, latency, PFT, treatment, prognosis | StatPearls / Merck Manual | [NBK555985](https://www.ncbi.nlm.nih.gov/books/NBK555985/); [Merck](https://www.merckmanuals.com/professional/pulmonary-disorders/environmental-and-occupational-pulmonary-diseases/asbestosis) |

**Evidence-source classification reminder for curation:** the fiber/macrophage mechanism papers (PMID 37894824; PFT 2016 review) are **IN_VITRO**; the Danish cohort (PMID 38577971) and clinicopathological series (PMID 38192052) are **HUMAN_CLINICAL**; rodent inhalation studies are **MODEL_ORGANISM**. Per the dismech DR/anti-hallucination SOP, **each PMID must be re-fetched with `just fetch-reference` and each snippet verified as an exact substring, and every ontology ID validated with OAK, before committing to a KB entry.**

**Explicitly not available / not applicable for asbestosis:** OMIM entry, Mendelian causal gene, inheritance pattern, penetrance/anticipation/carrier frequency, newborn/carrier screening, gene therapy, and a validated diagnostic molecular biomarker — all reflect that this is an acquired occupational fibrotic disease rather than a genetic disorder.