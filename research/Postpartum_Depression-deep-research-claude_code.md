---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-02T09:54:26.760267'
end_time: '2026-08-02T09:59:25.034149'
duration_seconds: 298.27
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Postpartum Depression
  mondo_id: MONDO:0005929
  category: Psychiatric
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
  num_turns: 24
  total_cost_usd: 1.9051541000000003
  session_id: b2cd8e7a-75ab-5cad-941f-eba7858220b3
  stop_reason: end_turn
citation_count: 58
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Postpartum Depression
- **MONDO ID:** MONDO:0005929 (if available)
- **Category:** Psychiatric

## Research Objectives

Please provide a comprehensive research report on **Postpartum Depression** covering all of the
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

# Postpartum Depression (PPD) — Comprehensive Research Report

## 1. Disease Information

**Overview:** Postpartum depression (PPD) is a non-psychotic, moderate-to-severe depressive episode that begins during pregnancy or within the weeks following childbirth. DSM-5 formally reclassified "postpartum depression" as major depressive disorder (MDD) **with peripartum onset**, defined as a major depressive episode with onset during pregnancy or within 4 weeks postpartum — a change made because roughly half of "postpartum" episodes actually begin antenatally. ICD-11 uses a broader 6-week postnatal onset window. Clinically and in most epidemiological literature, "postpartum depression" is used more loosely to include episodes beginning up to 12 months after delivery. PPD is distinguished from the much more common, self-limited "baby blues" (mild tearfulness/mood lability peaking days 3–5, resolving within ~2 weeks, occurring in up to 80% of mothers) and from postpartum psychosis (a psychiatric emergency with delusions/hallucinations, incidence ~0.1–0.2%, usually within the first 2 weeks postpartum).

**Key identifiers:**
- **MONDO:** MONDO:0005929
- **ICD-11 (MMS):** 6E20.0 (Foundation ID 169328648)
- **ICD-10 / ICD-10-CM:** F53 (Mental and behavioural disorders associated with the puerperium, not elsewhere classified); F53.0 (Postpartum depression, mild)
- **DSM-5:** Major Depressive Disorder, with Peripartum Onset specifier (296.xx)
- **MeSH:** D019052 (Depression, Postpartum)
- No dedicated **OMIM** phenotype number exists — PPD is modeled as a complex/multifactorial trait, not a Mendelian disorder, and is typically discussed under MDD-related OMIM entries (e.g., PHIH loci) rather than its own OMIM MIM number.
- **Orphanet** does not carry a distinct PPD entry (Orphanet does list postpartum *psychosis* as ORPHA:443173), consistent with PPD being a common complex psychiatric condition rather than a rare disease.

**Synonyms:** Postnatal depression; peripartum depression (DSM-5 term); puerperal depression; maternal postnatal depression. Note: "postpartum depression" is sometimes used loosely to include "perinatal depression" (antenatal + postnatal).

**Evidence basis:** Aggregated disease-level knowledge, drawn from large cohort studies (e.g., the French IGEDEPP cohort), meta-analyses across country-level EHR/registry data, and increasingly EHR-based case ascertainment algorithms validated within integrated health systems (e.g., PMC10018380 validated PPD identification in a large integrated US health system's EHR).

Sources: [Postnatal mental disorder: towards ICD-11 (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC1414676/), [Postpartum depression: a disorder in search of a definition (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4426488/), [Identification of Postpartum Depression in EHRs (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10018380/), [DSM V Postpartum Depression Criteria](https://sensiqnootropics.com/blogs/news/dsm-v-postpartum-depression), [Postpartum psychosis (Orphanet)](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=443173)

---

## 2. Etiology

**Causal framework:** PPD is a multifactorial, biopsychosocial disorder — no single causal gene or lesion; rather a convergence of genetic susceptibility, the abrupt peripartum neuroendocrine/neurosteroid transition, immune/inflammatory shifts, and major psychosocial stressors of the postpartum period, occurring against a background of prior depression/anxiety vulnerability.

**Genetic risk factors:**
- **Heritability:** Twin studies estimate PPD heritability at **38–54%**, generally higher than heritability estimates for non-perinatal depression in the same cohorts (Treloar et al.: 38% PPD vs 25% non-perinatal; Viktorin et al.: 44–54% PPD vs 32% non-perinatal), with roughly a third of the genetic architecture unique to the perinatal phenotype rather than shared with general MDD. ("Heritability of Perinatal Depression and Genetic Overlap With Nonperinatal Depression," *Am J Psychiatry*, PMID search via psychiatryonline.org)
- **GWAS:** The first large PPD GWAS meta-analysis (Guintivano et al. 2023, *Am J Psychiatry*, DOI 10.1176/appi.ajp.20230053) combined 18 European-ancestry cohorts (17,339 cases/53,426 controls) plus East Asian and African-ancestry cohorts (total 18,770 cases/58,461 controls). SNP-based heritability was **~14%** of variance attributable to common variants. The lead (non-genome-wide-significant) SNP mapped to **TXNRD2** (thioredoxin reductase 2, a mitochondrial redox/metabolism gene). Genetic correlations were significant with major depression, bipolar disorder, anxiety disorders, PTSD, insomnia, and **polycystic ovary syndrome**.
- A 2024 GWAS (Li et al., *Psychiatry and Clinical Neurosciences*) identified **8 additional risk loci**, and a separate 2023 medRxiv/PMC preprint reported a **novel susceptibility locus at 18q12.1**.
- Candidate gene categories implicated across studies: estrogen-signaling genes, oxytocin pathway genes (**OXTR**, **OXT**), and GABAergic neurotransmission genes — echoing the neurosteroid/GABA-A mechanistic hypothesis (Section 6).
- **HGNC candidates for annotation:** OXTR (HGNC:8529), TXNRD2 (HGNC:12437), TTC9B, HP1BP3 (epigenetic biomarker loci, see below).

**Environmental / psychosocial risk factors** (strong, consistently replicated):
- Personal history of depression or anxiety (single strongest predictor)
- Depression/anxiety during pregnancy (antenatal depression)
- Poor sleep quality/short sleep duration in pregnancy (≤6 hours)
- Low social support, poor partner relationship, intimate partner violence
- Unplanned/unwanted pregnancy
- Obstetric complications (preterm birth, cesarean delivery, negative birth experience), gestational diabetes
- Low socioeconomic status, chronic stress, adverse life events
- Excessive infant crying / difficult infant temperament, low maternal self-efficacy

**Protective factors:**
- Strong partner and social support
- Secure early mother-infant bonding (also buffers downstream child effects — see Section 11)
- Regular moderate-intensity aerobic exercise during/after pregnancy
- Adequate sleep
- Psychosocial/psychoeducational prenatal interventions (peer support, structured counseling)
- No specific *protective genetic variant* has been robustly identified to date (an evidence gap).

**Gene–environment interaction:** The dominant mechanistic GxE model is the **hormone-sensitivity hypothesis**: it is not absolute hormone levels but *differential sensitivity* to the hormonal (estrogen/progesterone/allopregnanolone) fluctuation that confers risk, and this sensitivity appears to have an epigenetic/genetic substrate (estrogen-responsive DNA methylation at HP1BP3/TTC9B; see Section 4). Stressful life events interact with genetic loading for depression risk (studied e.g. in NCT01648816, "Interaction Between Genetic Factors and Maternal Stressors During Pregnancy").

Sources: [First Large GWAS Meta-Analysis for PPD (AJP)](https://psychiatryonline.org/doi/10.1176/appi.ajp.20230794), [Meta-Analyses of GWAS for PPD (AJP full text)](https://psychiatryonline.org/doi/full/10.1176/appi.ajp.20230053), [MGH Women's Mental Health summary of GWAS](https://womensmentalhealth.org/posts/largest-ever-genetic-study-of-ppd-evidence-of-involvement-of-gabaergic-systems/), [Novel susceptibility locus 18q12.1 (medRxiv)](https://www.medrxiv.org/content/medrxiv/early/2023/04/25/2023.04.24.23289058.full.pdf), [Heritability of Perinatal Depression (AJP)](https://psychiatryonline.org/doi/10.1176/appi.ajp.2015.15010085), [Psychiatric Risk Factors for PPD: Systematic Review (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11851958/), [Risk factors community-based study](https://www.sciencedirect.com/science/article/pii/S0165032721001968)

---

## 3. Phenotypes

PPD phenotypes span **symptoms/behavioral changes** (core, per DSM-5 MDE criteria applied in the peripartum window) and **laboratory/biomarker abnormalities** (research-stage, not yet diagnostic).

### Core symptom/behavioral phenotypes (DSM-5 MDE criteria, ≥5 of 9, ≥2 weeks, most of the day nearly every day)
| Phenotype | Suggested HPO term | Notes |
|---|---|---|
| Depressed mood | HP:0000716 (Depressivity) | Core symptom |
| Anhedonia / loss of interest | HP:0031966 (Anhedonia) or HP:0000716 | |
| Appetite disturbance (increase or decrease) | HP:0004396 (Decreased body weight) / HP:0004324 (Weight gain) | |
| Sleep disturbance (insomnia/hypersomnia) | HP:0100785 (Insomnia) | Distinct from normal infant-care sleep disruption |
| Psychomotor agitation or retardation | HP:0025278 (Psychomotor agitation) | |
| Fatigue / loss of energy | HP:0012378 (Fatigue) | |
| Difficulty concentrating / indecisiveness | HP:0031936 (Decreased ability to concentrate) | |
| Feelings of worthlessness / excessive guilt | HP:0031332 (approx.; guilt not separately coded in HPO — free text) | PPD-specific: guilt over perceived maternal inadequacy |
| Suicidal ideation | HP:0031589 (Suicidal ideation) | |
| Anxiety (very frequent comorbid) | HP:0000739 (Anxiety) | Present in most PPD presentations |
| Irritability / hostility toward infant | HP:0000737 (Irritability) | Characteristic PPD-specific presentation |
| Intrusive/obsessive worry about infant harm | (behavioral, no direct HPO) | Distinguish from psychotic infanticidal ideation |
| Impaired mother-infant bonding | (behavioral phenotype, no direct HPO) | ~57% of PPD inpatients show impaired bonding at admission |

**Onset:** Peak onset 4–12 weeks postpartum by DSM-5/clinical convention, though ~50% of "postpartum" episodes have antenatal onset (hence DSM-5's "peripartum" reframing).
**Severity:** Ranges mild to severe, including psychotic features in a minority; assessed via HAM-D-17 or EPDS score bands.
**Progression/course:** Typically episodic; most cases remit within 3–6 months with treatment, but ~30–50% have a chronic or recurrent course if untreated, and prior PPD strongly predicts recurrence in subsequent pregnancies (30–50% recurrence risk).
**Frequency among affected individuals:** Global pooled prevalence of depressive symptoms ~19% (see Section 9); frequency of individual symptom domains within diagnosed PPD populations less systematically quantified in registries (an evidence gap best filled via cohort-specific data, e.g., IGEDEPP network-analysis paper).
**QoL impact:** Impaired maternal functioning, impaired bonding (57.1% impaired at admission, dropping to 18.2% by discharge with treatment), and downstream child cognitive/behavioral/attachment effects (see Section 11).

Sources: [Perinatal Depression - StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK519070/), [Major depressive episode and PPD network analysis (IGEDEPP, PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10377454/), [Maternal Attachment Networks and Bonding Disturbances (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10298680/)

---

## 4. Genetic / Molecular Information

- **No single causal gene** — PPD is polygenic/complex, unlike Mendelian OMIM disorders.
- **GWAS-implicated loci:** lead signal near **TXNRD2** (thioredoxin reductase 2; mitochondrial antioxidant/redox enzyme) in the 2023 AJP meta-analysis (no locus reached genome-wide significance in the European-only analysis); additional loci reported in the 2024 Li et al. study (8 loci) and an 18q12.1 locus (2023 preprint).
- **Variant classification:** Common variants of small individual effect (polygenic architecture), not ACMG-classified pathogenic/likely-pathogenic variants — PPD is not curated in ClinVar as a Mendelian phenotype.
- **Population frequency:** Not applicable in the Mendelian sense; SNP-based heritability (h²SNP) ≈ 14%.
- **Somatic vs. germline:** Germline (heritable common-variant) architecture; no somatic component described.
- **Functional consequence themes:** GWAS/candidate-gene results converge on (1) estrogen receptor signaling, (2) oxytocin signaling (OXTR/OXT), (3) GABAergic neurotransmission, (4) mitochondrial/metabolic genes (TXNRD2), consistent with the neurosteroid-withdrawal and immune mechanistic models below.

**Epigenetic information (a major PPD-specific research thread):**
- Prospective, prediction-oriented DNA methylation biomarker studies (Guintivano, Mehta, Kaminsky et al.) identified two blood-based methylation loci — **HP1BP3** and **TTC9B** — measured antenatally, that predicted subsequent PPD with **AUC = 0.87** in a discovery cohort of euthymic pregnant women, later independently replicated with variation tied to circulating hormone levels ("Replication of Epigenetic Postpartum Depression Biomarkers and Variation with Hormone Levels," *Neuropsychopharmacology*).
- Methylation at these loci is **estrogen-responsive**: PPD-risk-associated methylation change correlates significantly with estrogen-induced methylation change in hippocampal tissue (rodent), supporting an "estrogen-sensitivity" mechanistic model in which the brains of at-risk women show exaggerated epigenetic reprogramming in response to the massive third-trimester rise and postpartum collapse of estradiol.
- Bioinformatic annotation suggests HP1BP3 and TTC9B may be involved in **synaptic plasticity**; both have direct ties to estrogen signaling pathways.
- Genome-wide blood gene-expression profiling (2021, *Translational Psychiatry*) found PPD-associated transcriptomic changes pointing to an **altered immune landscape** (71 genes significant at 2 months postpartum, FDR 5%), and separately, transcript-level enrichment for **estrogen receptor signaling** genes in early antenatal blood, confirming increased estrogen-signaling sensitivity as a biomarker axis even though plasma estradiol itself is not elevated in PPD cases relative to controls.

**Chromosomal abnormalities:** None specifically implicated; not a chromosomal/CNV disorder.

**Suggested ontology terms for curation:** HGNC gene symbols OXTR (hgnc:8529), TXNRD2 (hgnc:12437); GO biological process terms for "estrogen receptor signaling pathway" (GO:0030520) and "regulation of GABA-A receptor activity"; CHEBI terms for allopregnanolone (CHEBI:2755) and estradiol (CHEBI:16469).

Sources: [Meta-Analyses of GWAS for PPD (AJP)](https://psychiatryonline.org/doi/full/10.1176/appi.ajp.20230053), [Early predictive biomarkers — estrogen receptor signaling (PubMed)](https://pubmed.ncbi.nlm.nih.gov/24495551/), [Seeing the Future: Epigenetic Biomarkers of PPD (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3857665/), [Antenatal prediction of PPD with blood DNA methylation biomarkers (Mol Psychiatry)](https://www.nature.com/articles/mp201362), [Replication of Epigenetic PPD Biomarkers (Neuropsychopharmacology)](https://www.nature.com/articles/npp2015333), [Genome-wide gene expression changes in PPD — altered immune landscape (Transl Psychiatry)](https://www.nature.com/articles/s41398-021-01270-5)

---

## 5. Environmental Information

- **Environmental/toxicant factors:** No specific toxin or pollutant is established as a primary PPD cause; the dominant "environmental" contributors are psychosocial/physiological rather than toxicological.
- **Lifestyle factors:** Poor/short sleep, sedentary behavior (exercise is protective — see Section 13), tobacco/alcohol use are associated with elevated risk in observational cohorts; low socioeconomic status and food/housing insecurity are consistently reported risk amplifiers.
- **Major life-event/stress exposures:** Intimate partner violence, chronic relationship conflict, unplanned pregnancy, traumatic or medically complicated birth experience, lack of social support network.
- **COVID-19 pandemic as an environmental stressor exemplar:** Pooled PPD prevalence rose to ~34% during the pandemic (roughly double pre-pandemic estimates), illustrating the sensitivity of PPD incidence to acute large-scale environmental/psychosocial stress.
- **Infectious agents:** Not a primary etiologic category for PPD; postpartum thyroiditis (autoimmune, not infectious) is a relevant differential/comorbid endocrine condition (Section 10) but is not itself infectious.

Sources: [Mapping global prevalence of depression among postpartum women (Transl Psychiatry)](https://www.nature.com/articles/s41398-021-01663-6), [Postpartum depression statistics 2024](https://www.singlecare.com/blog/postpartum-depression-statistics/)

---

## 6. Mechanism / Pathophysiology

PPD pathophysiology converges on three interacting, partially causal-chain mechanisms: **(A) neurosteroid/GABAergic withdrawal**, **(B) HPA-axis dysregulation and postpartum immune/inflammatory shift**, and **(C) altered emotion-circuit (limbic-prefrontal) function**, with genetic/epigenetic estrogen-sensitivity as an upstream modifier of (A).

### A. Neurosteroid (allopregnanolone) withdrawal — GABA-A mechanism (the best-established, drug-actionable pathway)
- **Causal chain:** Massive third-trimester rise in progesterone and its neuroactive metabolite **allopregnanolone (ALLO)**, a potent positive allosteric modulator of the GABA-A receptor → chronic ALLO exposure drives compensatory downregulation/altered subunit composition of GABA-A receptors (notably **δ-subunit-containing extrasynaptic receptors**) → parturition causes an abrupt, precipitous drop in ALLO ("neurosteroid withdrawal") → in women/mice whose GABA-A receptors fail to appropriately re-adapt (fail to upregulate δ-subunit-containing receptors as ALLO falls), there is a net loss of inhibitory tone → depressive-like and anxiety-like behavior, plus abnormal maternal behavior.
- **Model organism evidence:** GABA-A receptor **δ-subunit knockout mice** fail to appropriately regulate receptor dynamics across the ALLO rise-and-fall of pregnancy/postpartum and display depression-like and anxiety-like behavior specifically in the postpartum period, plus abnormal maternal behavior with increased pup mortality (cannibalism/neglect) — phenotypes reversible by exogenous ALLO administration (Maguire & Mody, *Neuron* 2008, foundational paper; PMC12076219 extends this to a hypothalamic MPA–PVN circuit modulating postpartum depressive-like behavior).
- **Therapeutic translation:** This mechanism directly motivated **brexanolone** (IV allopregnanolone analog; FDA-approved 2019 as Zulresso, first drug ever approved specifically for PPD; approval **withdrawn April 2025** at manufacturer's request due to the burdensome 60-hour inpatient IV infusion protocol and >$34,000 cost) and **zuranolone** (oral synthetic neurosteroid GABA-A positive allosteric modulator, FDA-approved August 2023 as Zurzuvae) — see Section 12.

### B. HPA axis dysregulation and postpartum inflammatory shift
- **Causal chain:** Placental CRH secretion during pregnancy escapes normal cortisol negative feedback → abrupt post-delivery loss of placental CRH plus normal HPA recalibration creates a period of HPA-axis instability → proinflammatory cytokines (which are normally suppressed in the anti-inflammatory pregnancy state to protect the fetal allograft) rebound sharply after delivery in response to the physical trauma of childbirth (a "pro-inflammatory shift") → elevated **IL-6** and **hs-CRP** postpartum are independent predictors of subsequent depression; PPD patients show decreased T-cell activation, increased proinflammatory cytokine secretion, kynurenine-pathway activation, and NLRP3 inflammasome activation.
- **Downstream neuroinflammatory link:** Kynurenine pathway activation shunts tryptophan away from serotonin synthesis toward neurotoxic kynurenine metabolites, linking peripheral inflammation to central monoaminergic and glutamatergic dysfunction.

### C. Emotion-circuit (limbic-prefrontal) dysfunction — neuroimaging correlates
- Structural/functional MRI meta-analyses consistently implicate the **medial prefrontal cortex** (default-mode-network hub), **anterior cingulate cortex**, **amygdala**, and **hippocampus**.
- Amygdala responses to negative emotional stimuli are typically **blunted** in PPD (contrasting with the hyperreactive amygdala more typical of non-perinatal MDD), suggesting a distinct PPD neurobiological signature.
- Functional connectivity between the posterior cingulate cortex and right amygdala is disrupted; dorsolateral prefrontal cortex resting activity (fALFF) correlates negatively with depression severity.
- Acupuncture intervention studies report partial normalization of amygdala subregion structure/function alongside symptom improvement, offered as indirect mechanistic/therapeutic-response evidence.

### D. Oxytocin and estrogen/progesterone withdrawal (hormone-sensitivity hypothesis)
- Estrogen surges ~100–1000-fold in the third trimester then collapses below pre-pregnancy levels within days of delivery ("estrogen withdrawal"); the **hormone-sensitivity hypothesis** (Bloch, Schmidt et al.) — supported by a landmark hormone-manipulation experimental paradigm — shows that experimentally induced supraphysiologic estradiol/progesterone followed by simulated "withdrawal" precipitates depressive symptoms selectively in women with a prior PPD history, even though absolute hormone trajectories do not differ from unaffected women; this is the direct human-experimental analog of the epigenetic estrogen-sensitivity biomarker findings in Section 4.
- Estrogen withdrawal alters **oxytocin signaling** in the paraventricular hypothalamus and dorsal raphe nucleus, increasing postpartum anxiety in rodent models — mechanistically linking the hormone-withdrawal and neuroendocrine-behavioral axes.
- Progesterone modulates oxytocin receptor sensitivity, providing a further node connecting the neurosteroid and oxytocin mechanisms.

### Suggested GO/CL/UBERON terms
- GO:0007165 (signal transduction) / GO:0030520 (estrogen receptor signaling pathway) / GO:0007214 (gamma-aminobutyric acid signaling pathway) / GO:0006954 (inflammatory response) / GO:0033197 (response to vitamin E — not relevant, omit) / GO:0034612 (response to tumor necrosis factor)
- CL:0000617 (GABAergic neuron), CL:0000704 (astrocyte, for neuroinflammatory glial component), CL:0000542 (lymphocyte, for peripheral immune component)
- UBERON:0001876 (amygdala), UBERON:0002771 (anterior cingulate cortex), UBERON:0002795 (mPFC region), UBERON:0002421 (hippocampal formation), UBERON:0035054 (hypothalamic paraventricular nucleus)

Sources: [Allopregnanolone in Postpartum Depression (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9088875/), [Allopregnanolone in PPD: Role in pathophysiology and treatment (PubMed)](https://pubmed.ncbi.nlm.nih.gov/32435663/), [A Mouse Model of Postpartum Depression (MGH)](https://womensmentalhealth.org/posts/a-mouse-model-of-postpartum-depression/), [Hypothalamic MPA-PVN Circuit in PPD Mouse Model (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12076219/), [Inflammatory pathophysiological mechanisms in PPD (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9669749/), [Elevated Hs-CRP and IL-6 after delivery (ScienceDirect)](https://www.sciencedirect.com/science/article/abs/pii/S016517811630275X), [Neuroimaging biomarkers structural/functional/metabolic review (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11354679/), [Consistent functional abnormalities in PPD](https://www.sciencedirect.com/science/article/abs/pii/S0166432823001857), [Estrogen withdrawal alters oxytocin signaling (bioRxiv)](https://www.biorxiv.org/content/10.1101/2020.06.16.154492.full.pdf), [Pathophysiological Mechanisms Implicated in PPD (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6370514/)

---

## 7. Anatomical Structures Affected

- **Organ level:** Primary organ = brain (CNS); no direct primary pathology in peripheral organs, though the postpartum uterus/placenta is the physiologic trigger organ (abrupt loss of placental steroidogenesis and CRH source at delivery). Endocrine system (HPA axis, ovarian/placental steroid axis, thyroid — postpartum thyroiditis is a relevant comorbid/differential endocrine condition) and immune system (postpartum pro-inflammatory shift) are secondarily involved. Body systems: nervous, endocrine, immune.
- **Tissue/cell level:** Cortical and limbic neuronal populations (GABAergic interneurons expressing δ-subunit GABA-A receptors; glutamatergic pyramidal neurons in mPFC/hippocampus); astrocytes and microglia (neuroinflammatory component); circulating peripheral blood mononuclear cells / T cells and monocytes (peripheral inflammatory/immune signature used in blood-based biomarker studies).
- **Subcellular level:** GABA-A receptor complex (plasma membrane, extrasynaptic and synaptic pools); mitochondria (TXNRD2 mitochondrial redox function implicated by GWAS); nuclear chromatin (DNA methylation changes at HP1BP3/TTC9B).
- **Localization (UBERON):** Amygdala (UBERON:0001876), medial prefrontal cortex, anterior cingulate cortex (UBERON:0002771), hippocampus (UBERON:0002421), hypothalamic paraventricular nucleus, dorsal raphe nucleus (UBERON:0002043).
- **Lateralization:** Not strongly lateralized; some studies report a left-dorsolateral-PFC correlation with symptom severity, but this is not a defining feature.

Sources: as in Section 6 (neuroimaging review references)

---

## 8. Temporal Development

- **Onset:** By DSM-5, within pregnancy or the first 4 weeks postpartum ("peripartum onset" specifier); by broader clinical/epidemiological convention up to 12 months postpartum. Onset pattern is typically subacute (days to weeks), distinguishing it from the acute (within days), self-limited "baby blues" and from postpartum psychosis (acute onset, typically within the first 2 weeks, often days).
- **Progression/course:** Most commonly episodic and treatable; the majority of women show significant improvement within 3–6 months of treatment initiation. Untreated or under-treated PPD can become chronic, blending into ongoing MDD beyond the first postpartum year.
- **Disease course pattern:** Not classically relapsing-remitting like an autoimmune disease, but recurrence risk in future pregnancies is substantial (historically cited at 30–50% for women with a prior PPD episode — a widely used clinical estimate, though exact modern PMID-sourced recurrence rate should be separately verified for KB citation).
- **Remission:** Both spontaneous (untreated, especially milder cases) and treatment-induced remission occur; treatment (SSRIs, psychotherapy, neurosteroid therapy) accelerates and increases likelihood of remission. Bonding-impairment data show striking within-admission improvement (57.1% → 18.2% impaired bonding from admission to discharge with treatment), illustrating a favorable short-term trajectory when treated.
- **Critical/vulnerability window:** The first days to weeks postpartum represent the critical neuroendocrine vulnerability window (precipitous ALLO/estrogen withdrawal); this window is also the target for pre-emptive screening and rapid-acting neurosteroid intervention (zuranolone shows separation from placebo by Day 3 of a 14-day course).

Sources: [SKYLARK trial results (MGH summary)](https://womensmentalhealth.org/posts/essential-reads-zuranolone-for-postpartum-depression-2/), [Postpartum blues (background)](https://en.wikipedia.org/wiki/Postpartum_blues)

---

## 9. Inheritance and Population

**Epidemiology:**
- **Global pooled prevalence:** A 2023 meta-analysis spanning 412 studies across 46 countries estimated a global pooled prevalence of **19.18%** (95% CI 18.02–20.34%), with national estimates ranging from ~3% to 44%. WHO cites a broad range of **10–20%** worldwide.
- **Regional variation:** ~15.5% in high-income countries vs. ~19.9% in developing regions (2021 estimates); highest reported regional rate Southern Africa (~39.96%); country-level extremes reported at Denmark ~6.48% (lowest) and Afghanistan ~61% (highest) in some analyses.
- **US trend:** Reported PPD prevalence rose from 9.4% (2010) to 19.0% (2021), partly reflecting improved screening/detection as well as true risk-factor shifts. By race/ethnicity in the same US data: ~21% White, ~19% Hispanic, ~22% Black, ~14% Asian/Pacific Islander women reporting PPD symptoms.
- **Pandemic effect:** Pooled PPD prevalence during COVID-19 rose to ~34%, roughly double pre-pandemic estimates, underscoring the psychosocial-stress sensitivity of the disorder.
- **Underdiagnosis:** Up to ~50% of PPD cases are estimated to go undiagnosed/untreated in various settings.

**Genetic architecture / inheritance pattern:** **Complex/multifactorial (polygenic)** — not Mendelian. No AD/AR/X-linked pattern; no established penetrance, expressivity, anticipation, mosaicism, founder-effect, or carrier-frequency concepts apply in the classical single-gene sense. SNP-based heritability ≈14% (common variants); twin-study broad-sense heritability 38–54% (see Section 2/4).

**Population demographics:**
- **Sex:** By definition affects only birthing individuals (female-specific/perinatal condition); "sex ratio" concept not applicable in the traditional sense, though partner (paternal) postpartum depression is a related, distinct phenomenon in the perinatal-mental-health literature (not covered here).
- **Age distribution:** Can occur at any reproductive age; younger maternal age and adolescent/teenage motherhood are reported as risk-elevating in some meta-analyses (see psychosocial-intervention-in-teenage-mothers meta-analysis).
- **Geographic distribution:** Highly variable by country/region as above; disparities strongly track socioeconomic and healthcare-access factors as well as cultural stigma affecting reporting/screening uptake.
- **Ethnic/racial disparities:** Documented disparities in US data (higher self-reported rates among Black and White women vs. Asian/Pacific Islander women), with a 2023 *AJP* paper specifically examining "Adversity and Resilience, Postpartum Depression, Suicide, and Racial/Ethnic Disparities."

Sources: [Postpartum depression statistics 2024 (SingleCare)](https://www.singlecare.com/blog/postpartum-depression-statistics/), [Mapping global prevalence of depression among postpartum women (Transl Psychiatry)](https://www.nature.com/articles/s41398-021-01663-6), [Exploring predictors and prevalence of PPD: Multinational study (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11092128/), [Adversity/Resilience/Racial Disparities (AJP)](https://psychiatryonline.org/doi/10.1176/appi.ajp.20230827)

---

## 10. Diagnostics

**Clinical criteria:** DSM-5 MDE criteria applied with the "peripartum onset" specifier (pregnancy through 4 weeks postpartum); ICD-11 6E20.0 uses a 6-week window. No dedicated PPD-specific diagnostic algorithm exists outside standard MDE criteria — diagnosis is fundamentally clinical.

**Screening instruments (not diagnostic, but central to case detection):**
- **Edinburgh Postnatal Depression Scale (EPDS):** 10-item, perinatal-period-specific self-report instrument that also captures 2 anxiety items; free, validated, translated into many languages, widely used as the primary perinatal screening tool globally.
- **PHQ-9:** Also validated for the perinatal population, self-administered, free.
- **Screening policy variation:** US-based organizations (e.g., Postpartum Support International/PSI) recommend **universal screening** using EPDS or PHQ-9 at multiple perinatal touchpoints. By contrast, UK NICE guidance recommends the 2 Whooley questions with EPDS as an adjunct, and does **not** endorse universal formal-scale screening — an internationally divergent policy area worth flagging (a genuine cross-jurisdictional guideline discrepancy rather than a single consensus).

**Laboratory/biomarker tests (research-stage, not yet standard-of-care diagnostics):**
- Antenatal DNA methylation panel at **HP1BP3/TTC9B** loci (AUC 0.87 in the discovery cohort) — a promising predictive (not diagnostic) blood biomarker, not yet in routine clinical use.
- Elevated **IL-6** and **hs-CRP** postpartum as candidate inflammatory biomarkers/predictors.
- Thyroid function testing (TSH, thyroid antibodies) is clinically indicated to rule out **postpartum thyroiditis**, an important differential/comorbid diagnosis that can mimic or exacerbate mood symptoms.

**Differential diagnosis:**
- **Baby blues** (postpartum blues): milder, self-limited, resolves within 2 weeks, does not significantly impair function — distinguished by duration/severity, not distinct pathophysiology.
- **Postpartum psychosis:** psychiatric emergency; delusions, hallucinations, agitation, insomnia, cognitive impairment, incidence ~0.1–0.2% of new mothers, often no prior psychiatric history, onset typically within first 2 weeks — requires urgent inpatient management, distinct from PPD though sometimes preceded by mood symptoms.
- **Postpartum thyroiditis:** autoimmune thyroid dysfunction in the postpartum period can produce depressive (hypothyroid phase) or anxious/hypomanic-like (hyperthyroid phase) symptoms and has been specifically implicated as a contributor to or mimic of postpartum psychosis in case literature — thyroid panel is a standard part of the diagnostic workup to exclude this mimicker.
- Substance-induced mood disorder, bipolar disorder with peripartum episode (important to screen for bipolarity before prescribing antidepressant monotherapy), and adjustment disorder.

**Genetic testing:** Not clinically indicated (no Mendelian gene panel exists); this is a research-only domain (GWAS/methylation biomarker development, not diagnostic gene panels, WES/WGS, CMA, karyotyping, or repeat-expansion testing).

Sources: [EPDS / screening recommendations (PSI)](https://postpartum.net/professionals/screening/), [Universal Screening for Maternal Mental Health Disorders](https://policycentermmh.org/universal-screening-for-maternal-mental-health-disorders-issue-brief/), [Postpartum Psychosis as Consequence of Thyroiditis vs Relapse (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10867710/), [Postpartum Mood Disorders and Thyroid Autoimmunity (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5415609/), [Thirty years with the EPDS (Br J Psychiatry)](https://www.cambridge.org/core/journals/the-british-journal-of-psychiatry/article/thirty-years-with-the-edinburgh-postnatal-depression-scale-voices-from-the-past-and-recommendations-for-the-future/B22C1AF432691C13E96E48988758D939)

---

## 11. Outcome / Prognosis

- **Mortality:** PPD is a major contributor to **maternal suicide**, one of the leading causes of pregnancy-associated death in the first postpartum year in several high-income-country surveillance systems (an important, separately-citable statistic for KB curation — the 2023 *AJP* paper on adversity/resilience/PPD/suicide/racial disparities is directly relevant here and should be pulled for exact figures during curation).
- **Recovery/treatment response:** Prognosis is generally favorable with treatment — most women achieve significant symptom improvement within weeks to months; zuranolone and brexanolone trials demonstrate rapid response (symptom separation from placebo by Day 3 of a 14-day oral course), and standard antidepressant/psychotherapy approaches show good response rates over 6–12 weeks.
- **Impact on mother-infant bonding (a key functional-outcome domain):** 57.1% of hospitalized PPD patients show impaired bonding at admission, improving to 18.2% impaired at discharge — indicating bonding impairment is common but substantially reversible with treatment.
- **Child developmental outcomes:** Untreated PPD is associated with insecure infant attachment, and downstream child behavioral/cognitive/emotional difficulties; a 2025 longitudinal study found mother-to-infant bonding **mediates 34.6%** of the effect of postpartum maternal depression on child difficulties, and secure early bonding **partially buffers** the long-term (school-age) effects of PPD on child outcomes — establishing bonding quality as both an outcome and an effect-modifier/mediator.
- **Recurrence:** Elevated risk of recurrence in subsequent pregnancies and of transition to chronic/recurrent MDD if untreated (see Section 8).
- **Prognostic factors:** Symptom severity at presentation, presence of prior depression/anxiety history, quality of social/partner support, timeliness of treatment initiation, and (per newer research) inflammatory/epigenetic biomarker profiles are candidate prognostic indicators, though none are yet clinically validated prognostic tools.

Sources: [Mother-infant bonding can buffer long-term effects of PPD on child outcomes](https://www.news-medical.net/news/20250514/Mother-infant-bonding-can-buffer-long-term-effects-of-postpartum-depression-on-child-outcomes.aspx), [Maternal Attachment Networks and Bonding Disturbances (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10298680/), [PPD and bonding: long-term effects on school-age children (ScienceDaily)](https://www.sciencedaily.com/releases/2025/05/250514111245.htm), [Adversity and Resilience, PPD, Suicide, and Racial/Ethnic Disparities (AJP)](https://psychiatryonline.org/doi/10.1176/appi.ajp.20230827)

---

## 12. Treatment

**Pharmacotherapy — Neurosteroid/GABA-A modulators (PPD-specific, mechanism-targeted; NCIT:C15986 Pharmacotherapy):**
- **Brexanolone (Zulresso):** IV allopregnanolone analog, FDA-approved 2019 as the first drug specifically approved for PPD; 60-hour continuous inpatient infusion; **FDA approval withdrawn April 14, 2025** at manufacturer request due to cost (>$34,000/patient) and complex administration logistics.
- **Zuranolone (Zurzuvae):** Oral synthetic neurosteroid, GABA-A receptor positive allosteric modulator engineered to overcome allopregnanolone's poor oral bioavailability/short half-life; FDA-approved August 2023, 14-day oral course, 50 mg daily. **SKYLARK Phase 3 trial (NCT04442503):** LS-mean HAM-D-17 change from baseline at Day 15 = −15.6 (zuranolone) vs −11.6 (placebo), difference −4.0 points (p=0.0007); improvement detectable as early as **Day 3** (mean HAM-D reduction 9.5 vs 6.1, p=0.0008), sustained through Day 45. Also improves insomnia symptoms specifically. Currently the only FDA-approved oral, at-home PPD-specific pharmacotherapy.

**Pharmacotherapy — Standard antidepressants:**
- **SSRIs** are first-line per ACOG (2023 Clinical Practice Guideline No. 5): **sertraline** or **escitalopram** preferred, especially in treatment-naive patients (favorable lactation safety profile is a key selection driver, though not itself a mechanistic point).
- Standard antidepressant classes (SNRIs, etc.) used as in general MDD when SSRIs are ineffective/not tolerated.

**Psychotherapy (first-line for mild-moderate PPD, per multiple guideline summaries):**
- **Cognitive Behavioral Therapy (CBT):** structured, time-limited, targets negative thought patterns/behaviors.
- **Interpersonal Psychotherapy (IPT):** targets role transition and interpersonal relationship strain specific to new motherhood; demonstrated efficacy including in low- and middle-income country settings.
- Psychoeducation and structured digital/web-based interventions (e.g., MomMoodBooster) also show efficacy.

**Supportive/behavioral care:**
- Peer support programs, structured social support interventions, sleep optimization.

**Experimental / emerging:**
- Additional neuroactive-steroid compounds and next-generation GABA-A modulators in clinical development (ongoing trials registered at ClinicalTrials.gov).
- Novel psychotherapeutic delivery models under trial (e.g., NCT06991166 "OBWELL").

**Treatment outcomes / adverse events:**
- Zuranolone: generally well tolerated; somnolence/sedation is the most common adverse effect (mechanistically expected from GABA-A potentiation); real-world pharmacovigilance analyses (FAERS-based) are ongoing to characterize post-marketing safety.
- Brexanolone: sedation, loss of consciousness risk (boxed warning), requiring continuous monitoring during the 60-hour infusion — a major driver of its subsequent market withdrawal.

**Suggested NCIT terms:** NCIT:C15986 (Pharmacotherapy) as `treatment_term`, with `therapeutic_agent` bound to CHEBI/NCIT terms for zuranolone and sertraline; `therapeutic_modality: SMALL_MOLECULE` for both; brexanolone/zuranolone could additionally be flagged as neurosteroid GABA-A PAMs distinct from classical antidepressants, aligning with the general `NCIT:C49236` (Therapeutic Procedure) / psychotherapy-specific NCIT codes (e.g., a Cognitive/Interpersonal Therapy NCIT term) for CBT/IPT.

Sources: [ACOG Clinical Practice Guideline No. 5](https://www.acog.org/clinical/clinical-guidance/clinical-practice-guideline/articles/2023/06/treatment-and-management-of-mental-health-conditions-during-pregnancy-and-postpartum), [Neurosteroids and PPD: Mechanism, Efficacy, Approval of Brexanolone and Zurzuvae (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10577692/), [Zuranolone and Brexanolone for Treatment of PPD (Obstet Gynecol)](https://journals.lww.com/greenjournal/fulltext/10.1097/aog.0000000000006093~zuranolone-and-brexanolone-for-the-treatment-of-postpartum), [SKYLARK study primary/secondary endpoints (Biogen press release)](https://investors.biogen.com/news-releases/news-release-details/sage-therapeutics-and-biogen-announce-phase-3-skylark-study), [Post-marketing safety of zuranolone (FAERS analysis, PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12394218/), [Current Developments: Zuranolone (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11535317/)

---

## 13. Prevention

- **Primary prevention:**
  - **Aerobic exercise:** Network meta-analysis of 26 RCTs (n=2,867) found moderate-intensity aerobic exercise (3–4×/week, 35–45 min) significantly reduced depressive symptoms vs. standard care (MD = −1.90, 95% CI −2.58 to −1.21); supervised and team-based exercise slightly outperformed unsupervised/individual exercise.
  - **Psychosocial/psychoeducational interventions:** Meta-analytic pooled effect size −0.5 (95% CI −0.95 to −0.06) for prevention of PPD at final assessment; interventions include peer support, structured counseling, educational programs, CBT-based prevention, motivational interviewing, and mindfulness-based programs. Specifically effective in high-risk subgroups (e.g., adolescent/teenage mothers per a dedicated systematic review/meta-analysis of RCTs).
  - **App-based/digital interventions:** Systematic review/meta-analysis supports modest preventive efficacy of app-based interventions.
- **Secondary prevention (screening for early detection):** Universal EPDS/PHQ-9 screening at perinatal touchpoints (endorsed by PSI/ACOG in the US), though international guideline divergence exists (NICE in the UK does not endorse universal formal-scale screening — see Section 10).
- **Targeted/risk-stratified prevention:** Women with personal/family history of depression, prior PPD, or other identified risk factors (Section 2) are candidates for targeted surveillance and pre-emptive psychosocial support; the antenatal DNA methylation biomarker panel (Section 4) is a research-stage tool aimed at enabling this kind of risk stratification.
- **Tertiary prevention:** Early treatment to prevent chronicity, recurrence in future pregnancies, and downstream child developmental harms (mediated substantially through bonding — Section 11); relapse-prevention planning for women with prior PPD episodes, given elevated recurrence risk in subsequent pregnancies.
- **Counseling:** Preconception/prenatal counseling on recurrence risk for women with a prior PPD history is standard clinical practice (parallel to genetic counseling in Mendelian disease, though here it addresses recurrence-risk counseling rather than inheritance-risk counseling).
- **Immunization:** Not applicable (non-infectious).

Sources: [Effectiveness of aerobic exercise (Meta-analysis/network meta-analysis, PLOS One)](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0287650), [Physical exercise interventions for perinatal depression (Frontiers)](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.1022402/full), [Effectiveness of Psychosocial Interventions Preventing PPD Among Teenage Mothers (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11519152/), [The preventive effect of psychological/psychosocial interventions on PPD (ScienceDirect)](https://www.sciencedirect.com/science/article/abs/pii/S0022395624006782), [App-based interventions for prevention of PPD (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10265566/)

---

## 14. Other Species / Natural Disease

- PPD as clinically defined is a **human-specific diagnostic construct** (tied to DSM-5/ICD-11 criteria); a directly analogous *naturally occurring* veterinary disease entity is not established in the literature surveyed. No OMIA (Online Mendelian Inheritance in Animals) entry or veterinary case-series literature on naturally occurring "postpartum depression" in companion animals or livestock was found in this search — this appears to be a genuine gap rather than an oversight, since postpartum affective states in animals are typically studied only as experimentally *induced* models (Section 15) rather than documented spontaneous veterinary disease.
- **Comparative/evolutionary biology:** The core neuroendocrine substrate (progesterone/allopregnanolone rise-and-fall around parturition, GABA-A receptor plasticity, oxytocin-mediated maternal behavior circuitry) is deeply conserved across mammals, which is precisely why rodent models are considered mechanistically informative despite the absence of a documented "natural" PPD phenotype in non-human species; abnormal maternal behavior with increased offspring mortality (neglect/cannibalism) in genetically or pharmacologically manipulated rodents is the closest cross-species analog to human PPD's impact on maternal-infant bonding.
- **Taxonomy:** Primary study species is *Mus musculus* (NCBITaxon:10090) and *Rattus norvegicus* (NCBITaxon:10116); no specific affected breed/strain beyond the genetically selected WKY/WMI depression-model rat line and various targeted knockout mouse lines (Section 15).

Sources: (absence of positive hits is itself informative) [Postpartum depression spans generations, animal study suggests (ScienceDaily)](https://www.sciencedaily.com/releases/2013/10/131008132914.htm)

---

## 15. Model Organisms

**Genetic (knockout) mouse models — the mechanistic gold standard:**
- **GABA-A receptor δ-subunit knockout mice** (Maguire & Mody, *Neuron* 2008; foundational model): fail to appropriately regulate GABA-A receptor subunit composition across the pregnancy-to-postpartum allopregnanolone rise-and-fall, and display depression-like and anxiety-like behavior specific to the postpartum period, plus abnormal maternal behavior and increased pup mortality (neglect/cannibalism) — phenotypes rescued by exogenous allopregnanolone administration. This model directly recapitulates the human neurosteroid-withdrawal hypothesis and provided the preclinical rationale for brexanolone/zuranolone development.
- Follow-on circuit-level work: a hypothalamic **medial preoptic area (MPA)–paraventricular nucleus (PVN)** circuit has been shown to modulate depressive-like behaviors in a mouse PPD model (2024/2025 PMC12076219), extending the mechanism from receptor-level to defined neural-circuit level.

**Induced (stress/hormone-manipulation) rodent models:**
- **Maternal separation model:** dams separated from litters (e.g., 3 hr/day, lactation days 2–12) → poor maternal care, transient offspring anxiety.
- **Chronic stress models:** chronic social stress or chronic restraint stress during pregnancy/postpartum → increased depressive-like and aggressive maternal behavior, altered maternal care toward pups; a transgenerational rat study (Tufts Cummings School) showed early-life chronic social stress effects propagate across generations of maternal behavior/physiology.
- **Corticosterone-treatment model:** postpartum CORT administration (e.g., 40 mg/kg daily) in Sprague-Dawley dams to model HPA-axis-driven depressive phenotypes; shown to impair maternal care and produce neurochemical alterations in dams plus long-lasting sociability impairment in offspring.
- **Genetic selectively-bred model:** the **Wistar Kyoto More Immobile (WMI)** rat strain, bidirectionally selectively bred from the parental WKY line for depression-like immobility behavior, used to study postpartum-specific hypothalamic gene expression and behavior.

**Phenotype recapitulation and limitations:**
- Rodent models robustly recapitulate core depression-like behavioral readouts (forced-swim/tail-suspension immobility, anhedonia proxies), impaired maternal care, and the neurosteroid/GABA-A mechanistic axis, and have directly enabled a first-in-class drug class (neurosteroid GABA-A PAMs).
- Limitations: rodent "depression-like behavior" readouts are behavioral proxies rather than validated homologs of human subjective mood/cognitive symptoms (rumination, guilt, suicidal ideation have no clean rodent correlate); psychosocial risk factors central to human PPD (relationship stress, cultural/socioeconomic stigma, sleep deprivation from infant care specifically) are harder to model with construct validity; and the translational gap between rodent HPA/immune findings and the specific human postpartum immune-shift literature (Section 6B) is not fully resolved.

**Resources:** MGI (Mouse Genome Informatics) for GABA-A δ-subunit knockout lines; standard rodent behavioral-neuroscience repositories for the WMI rat strain and induced-stress protocols.

Sources: [A Mouse Model of Postpartum Depression (MGH)](https://womensmentalhealth.org/posts/a-mouse-model-of-postpartum-depression/), [Hypothalamic MPA-PVN Circuit Modulates Depressive-Like Behaviors in PPD Mouse Model (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12076219/), [Modeling postpartum depression in rats: theoretic and methodological issues](https://www.zoores.ac.cn/en/article/doi/10.13918/j.issn.2095-8137.2016.4.229), [Hypothalamic Gene Expression and Postpartum Behavior in a Genetic Rat Model of Depression (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7649805/), [PPD in rats causes poor maternal care and neurochemical alterations, offspring sociability impairment (PubMed)](https://pubmed.ncbi.nlm.nih.gov/36041571/), [Postpartum depression spans generations, animal study suggests (ScienceDaily)](https://www.sciencedaily.com/releases/2013/10/131008132914.htm)

---

## Summary of Key Evidence Gaps for Curators

1. **No dedicated OMIM/Orphanet entry** — PPD must be curated as a complex/multifactorial MONDO:0005929 entry, not linked to a Mendelian OMIM phenotype MIM number.
2. **GWAS loci did not reach genome-wide significance** in the largest 2023 meta-analysis (lead TXNRD2 signal was suggestive, not GWS) — curate genetic evidence with appropriately hedged `supports: PARTIAL` classifications rather than definitive causal gene claims.
3. **Epigenetic biomarkers (HP1BP3/TTC9B)** are prediction-stage research tools, not validated clinical diagnostics — do not conflate with an established diagnostic test.
4. **Brexanolone's FDA approval was withdrawn in April 2025** — any treatment entry must reflect current regulatory status (zuranolone remains the sole current FDA-approved PPD-specific pharmacotherapy) rather than presenting brexanolone as an actively marketed product.
5. **International screening-guideline divergence** (US universal-EPDS-screening consensus vs. UK NICE's non-universal approach) is a genuine unresolved policy tension worth flagging as a `discussion`, not smoothing over as consensus.
6. **No documented naturally-occurring veterinary/OMIA analog** was found — Section 14 content should be marked as a knowledge gap rather than populated with fabricated cross-species claims.
7. Several statistics here (recurrence-risk percentage, exact maternal-suicide contribution figures) are cited as commonly-used clinical estimates from secondary sources; before final KB curation, each should be traced to and quote-verified against its specific primary PMID per the dismech evidence SOP.