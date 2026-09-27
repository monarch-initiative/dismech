---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-01T07:14:54.876887'
end_time: '2026-08-01T07:28:35.351791'
duration_seconds: 820.48
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: AFG2A-Related Encephalopathy
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
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-opus-5[1m]
  web_search_requests: 9
  num_turns: 69
  total_cost_usd: 5.411886250000002
  session_id: 6bfb8de0-ac6c-4bfb-b04a-d3887df9b7c3
  stop_reason: end_turn
citation_count: 24
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** AFG2A-Related Encephalopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **AFG2A-Related Encephalopathy** covering all of the
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

# AFG2A-Related Encephalopathy — Comprehensive Research Report

**Prepared:** 2026-08-01 · **Target for KB entry:** `kb/disorders/AFG2A-Related_Encephalopathy.yaml` · **MONDO:0014698**

**Scope note on evidence provenance:** Every PMID cited below was verified against a cached PubMed record in `references_cache/` or fetched live during this session. Quotes marked with `>` are verbatim from the cited abstract or open-access full text and are suitable as evidence `snippet:` values after running `just validate-references`. Ontology IDs are flagged **[verified]** (checked this session against HPO/OLS/HGNC/MGI APIs) or **[suggested — verify with OAK]**. Three published-literature discrepancies that would propagate into the KB if copied uncritically are flagged in §4.6.

---

## 1. Disease Information

### 1.1 Overview

AFG2A-related encephalopathy (AFG2A-RE) is an ultra-rare autosomal recessive neurodevelopmental disorder caused by biallelic variants in *AFG2A* (formerly *SPATA5*), encoding a AAA+ ATPase that is the human orthologue of yeast Drg1 and a core subunit of the **55LCC** complex responsible for late cytoplasmic maturation of the pre-60S ribosomal subunit and for replisome proteostasis.

The most recent and largest synthesis (Nou-Fontanet et al. 2026, n=51; **PMID:41933351**) defines it as follows:

> "AFG2A-RE is an ultra-rare, recessive disorder, sometimes presenting as a developmental and epileptic encephalopathy (DEE), characterised by the triad of epilepsy, congenital microcephaly, and deafness, and typically associated with intellectual disability, spasticity, and movement disorders."

The disorder was first delineated by Tanaka et al. 2015 (**PMID:26299366**):

> "Using whole-exome sequencing, we have identified in ten families 14 individuals with microcephaly, developmental delay, intellectual disability, hypotonia, spasticity, seizures, sensorineural hearing loss, cortical visual impairment, and rare autosomal-recessive predicted pathogenic variants in spermatogenesis-associated protein 5 (SPATA5)."

Independent confirmation followed within a year (Buchert et al. 2016, **PMID:27683084**):

> "We thus independently confirm that bi-allelic pathogenic variants in SPATA5 cause a syndromic form of intellectual disability, and we delineate its clinical presentation."

### 1.2 Identifiers

| Resource | Identifier | Status |
|---|---|---|
| MONDO | **MONDO:0014698** — *microcephaly-intellectual disability-sensorineural hearing loss-epilepsy-abnormal muscle tone syndrome* | **[verified]** via OLS4 |
| OMIM (phenotype) | **#616577** — NEURODEVELOPMENTAL DISORDER WITH HEARING LOSS, SEIZURES, AND BRAIN ABNORMALITIES (NEDHSB) | verified via MedGen/GTR + MONDO xref |
| OMIM (gene) | **\*613940** — AFG2 AAA ATPase HOMOLOG A; AFG2A | verified via HGNC |
| Orphanet | **ORPHA:457351** | verified via MONDO xref + GTR |
| UMLS / MedGen | **C4225276** / MedGen **895574** | verified |
| GARD | 0017804 | verified via MONDO xref |
| HGNC | **HGNC:18119** (`hgnc:18119` in repo casing) | **[verified]** via HGNC REST |
| Ensembl / NCBI Gene / UniProt | ENSG00000145375 / 166378 / **Q8NB90** | **[verified]** via HGNC REST |
| ClinGen gene-disease validity | AFG2A — **Definitive**, AR, Syndromic Disorders GCEP, evaluated **2024-07-23**, against MONDO:0800439 (includes MIM:616577) | verified via ClinGen search |
| Cytogenetic locus | **4q28.1** (GRCh38 chr4:122,923,070–123,319,433) | verified |
| ICD-10 / ICD-11 | **Not verified in this session** (Orphanet blocked automated retrieval). Orphanet typically maps such syndromes to ICD-10 Q87.8 — treat as unconfirmed. |
| MeSH | No dedicated descriptor; indexed via *Microcephaly*, *Intellectual Disability*, *Hearing Loss*, *Seizures*, *ATPases Associated with Diverse Cellular Activities* |

### 1.3 Synonyms and nomenclature

- **AFG2A-related encephalopathy (AFG2A-RE)** — current preferred clinical term (PMID:41933351, PMID:40712368)
- **SPATA5-related encephalopathy** — prior term (PMID:27246907)
- **NEDHSB** — Neurodevelopmental disorder with hearing loss, seizures, and brain abnormalities (OMIM #616577; MONDO exact synonym)
- **EHLMRS** — "Epilepsy, hearing loss, and mental retardation syndrome" (PMID:28293831, PMID:34360601). **MONDO flags this and the spelled-out form as *discouraged*/historic synonyms** — do not use as `preferred_term`.
- Gene aliases: *SPATA5*, *SPAF* (spermatogenesis-associated factor), *AFG2*

**Nomenclature caution for curation:** the gene symbol change *SPATA5* → **AFG2A** and the paralogue *SPATA5L1* → **AFG2B** (HGNC:28762, **[verified]**) means literature searches must cover both symbol eras. This is a mild named-entity-confusion (NEC) risk class: *AFG2A* and *AFG2B* cause phenotypically overlapping but distinct disorders (see §10.4).

### 1.4 Data provenance

All human knowledge on this disorder derives from **individual-patient case reports and small case series aggregated by systematic review**, plus targeted research cohorts of early-onset epileptic encephalopathy. There is **no EHR-derived, registry-derived, or population-scale dataset**. The largest single aggregation is the PRISMA systematic review of Nou-Fontanet et al. 2026 (51 individuals: 45 published + 6 new). An ERN ITHACA / SPATA Foundation natural-history collaboration led by Barbara Vona (Göttingen) has collected ~30 additional unpublished AFG2A cases; the call is currently closed to new submissions. Formal natural-history data do not yet exist — the 2026 review explicitly states: *"Prospective natural history studies across multiple reference centres are needed."*

---

## 2. Etiology

### 2.1 Primary causal factor

Monogenic: **biallelic (homozygous or compound heterozygous) pathogenic variants in *AFG2A*** (4q28.1). No environmental, infectious, or multifactorial contribution has been demonstrated or proposed. Heterozygous carriers (including obligate-carrier parents in every reported family) are unaffected.

### 2.2 Genetic risk factors

- **Causal variants:** >40 distinct *AFG2A* variants reported (PMID:41933351). Reference transcript **NM_145207.3** (older papers use NM_145207.2).
- **Consanguinity:** a recognized route to homozygosity — the largest single-family cluster (7 affected individuals) came from an extended consanguineous family (PMID:27683084). Most compound-heterozygous cases arose in non-consanguineous European families (PMID:29343804).
- **Uniparental disomy:** an unusual mechanism producing homozygosity without consanguinity was documented — homozygotization of a maternally inherited c.251G>A variant "due to **maternal isodisomy of chromosome 4**" (PMID:30552426). This has direct implications for recurrence-risk counselling.
- **Copy-number variants as one allele:** a 51 kb deletion spanning exons 12–13 (c.2080_2213del; p.(Gly694Phefs\*23)) *in trans* with a sequence variant (PMID:30552426) — i.e., CNV analysis is required for complete allele ascertainment.
- **Modifier genes:** none identified. Genotype–phenotype analysis in the largest cohort was negative: *"No significant associations between genotype and epilepsy phenotype were observed."* (PMID:41933351)

### 2.3 Environmental risk factors, protective factors, gene–environment interactions

**None identified, and none biologically expected** for a fully penetrant recessive Mendelian disorder. No protective alleles, dietary, or exposure modifiers have been described. Ketogenic diet (§12) is a *treatment*, not a protective/preventive factor.

The single evidence-supported "environmental" modifier of *disease expression* (not risk) is metabolic state: ketogenic-diet-mimicking medium reversed mitochondrial abnormalities in patient fibroblasts (PMID:40712368).

---

## 3. Phenotypes

### 3.1 Core frequency table (largest cohort, n=51; PMID:41933351)

All percentages below are from the Nou-Fontanet 2026 systematic review; denominators vary by feature because data availability differs. Verbatim abstract source:

> "The most frequently described clinical features included intellectual disability (97.92%), hearing loss (93.62%), microcephaly (85.71%), visual impairment (79.49%), hypotonia (71.74%), spasticity (60.87%), and movement disorders (36.96%). Epilepsy was present in 74.71% of cases, with seizures of generalized onset being the most common (70.83%), and infantile epileptic spasms syndrome (IESS) was the predominant epilepsy syndrome at onset (66.67%). Epilepsy was often drug-resistant (82.35%). Brain MRI abnormalities were frequently observed (68.29%), including hypomyelination (39.02%), brain atrophy (34.15%), and a thin corpus callosum (29.27%)."

| Phenotype | % | HPO frequency band | Suggested HP term | Verification |
|---|---|---|---|---|
| Intellectual disability | 97.92 | Very frequent (80–99%) | HP:0001249 Intellectual disability | [suggested] |
| — severe-to-profound subset | 75 of those graded | | HP:0002187 Intellectual disability, profound / HP:0010864 severe | [suggested] |
| Absent speech (all with ID) | ~100 of ID cases | Very frequent | **HP:0001344 Absent speech** | **[verified]** |
| Hearing loss (sensorineural) | 93.62 | Very frequent | **HP:0000407 Sensorineural hearing impairment** | **[verified]** |
| Microcephaly | 85.71 | Very frequent | **HP:0000252 Microcephaly**; congenital form → **HP:0011451 Primary microcephaly** | **[verified]** |
| Motor impairment (any) | 97.83 | Very frequent | HP:0002500 / composite | [suggested] |
| Visual impairment | 79.49 | Frequent | HP:0000505 Visual impairment | [suggested] |
| — cortical/cerebral blindness | 9.68 | Occasional | **HP:0100704 Cerebral visual impairment** | **[verified]** |
| — strabismus | 9.68 | Occasional | HP:0000486 Strabismus | [suggested] |
| — refraction abnormality | 9.68 | Occasional | HP:0000539 Abnormality of refraction | [suggested] |
| Epilepsy | 74.71 (38/51) | Frequent | HP:0001250 Seizure | [suggested] |
| Hypotonia | 71.74 | Frequent | **HP:0001252 Hypotonia** | **[verified]** |
| Spasticity | 60.87 | Frequent | HP:0001257 Spasticity | [suggested] |
| Movement disorder (non-paroxysmal, any) | 36.96 | Frequent | HP:0100022 Abnormality of movement | [suggested] |
| — dystonia | 21.74 | Occasional | HP:0001332 Dystonia | [suggested] |
| — dyskinesia | 6.52 | Occasional | HP:0100660 Dyskinesia | [suggested] |
| — ataxia | 6.52 | Occasional | HP:0001251 Ataxia | [suggested] |
| — chorea | 4.35 | Very rare | HP:0002072 Chorea | [suggested] |
| — athetosis | 2.17 | Very rare | HP:0002305 Athetosis | [suggested] |
| Neurodevelopmental delay | 84.31 | Very frequent | HP:0001263 Global developmental delay | [suggested] |
| GI symptoms (any) | 78.95 | Frequent | HP:0011024 Abnormality of the gastrointestinal tract | [suggested] |
| — dysphagia | 30 | Frequent | HP:0002015 Dysphagia | [suggested] |
| — gastroesophageal reflux | 20 | Occasional | HP:0002020 Gastroesophageal reflux | [suggested] |
| — constipation | 16.67 | Occasional | HP:0002019 Constipation | [suggested] |
| Short stature | 13.33 | Occasional | HP:0004322 Short stature | [suggested] |
| Failure to thrive | 13.33 | Occasional | HP:0001508 Failure to thrive | [suggested] |
| Neonatal hypotonia (perinatal) | 12.5 | Occasional | HP:0001319 Neonatal hypotonia | [suggested] |
| Neonatal respiratory distress | 9.38 | Occasional | HP:0002643 Neonatal respiratory distress | [suggested] |
| Preterm birth (mod-to-late) | 6.25 | Occasional | HP:0001622 Premature birth | [suggested] |
| IUGR | 6.25 | Occasional | HP:0001511 Intrauterine growth retardation | [suggested] |
| Normal growth | 73.33 | — | — | |
| Normal perinatal course | 75 | — | — | |

**Gross motor function (GMFCS, n=22):** level V 59.09%, IV 27.27%, III 9.09%, II 4.55% — i.e., **~86% are GMFCS IV–V (non-ambulatory, requiring full physical assistance)**. Suggested term: **HP:0002540 Inability to walk [verified]**.

### 3.2 Epilepsy phenotype (detailed data n=24; PMID:41933351)

- **Infantile epileptic spasms syndrome (IESS)** is the predominant presentation: 16/24 (66.67%), **mean age at onset 9.53 months (range 2.5–27 months)**. HP terms: **HP:0011097 Epileptic spasm [verified]**, HP:0012469 Infantile spasms **[verified]**.
- Independent series (PMID:40712368): *"In all but one case, the initial epilepsy presentation was infantile epileptic spasms syndrome (IESS), with a mean age at onset of 13.6 months."*
- Generalized-onset seizures 70.83%; focal 2 individuals; both types in 5.
- Semiologies: tonic 33.4%, tonic-clonic 25%, myoclonic 12.5%, atonic 4.17%, atypical absence 4.17%; focal clonic 12.5%, focal myoclonic 12.5%; gelastic and focal impaired-awareness in 1 each.
- **Seizures with complex ocular movements** in 3/24 (12.5%) — a distinctive feature first highlighted by Zanus et al. 2020 (**PMID:33063670**): *"The epileptic clinical features were characterized by infantile spasms associated with seizures with a complex ocular movement; a predominant involvement of the posterior cerebral area and cortical visual impairment were also noticed."*
- **EEG (n=20 detailed):** interictal epileptiform activity 95%; **multifocal epileptiform discharges 75%** (occipital/posterior predominance recurrently noted); **hypsarrhythmia 20%** (**HP:0002521 Hypsarrhythmia [verified]**); photoparoxysmal response 5%. Kurata et al. 2016 (**PMID:27246907**): *"Interictal electroencephalography showed multifocal spikes and bursts of asynchronous diffuse spike-wave complexes. Augmented amplitudes of visually evoked potentials were detected in two patients."*
- **Drug resistance:** the abstract states 82.35%; the results text reports 82.35% (14/17) were on **polytherapy**. Only **4/16** with follow-up were seizure-free. Treat the 82.35% figure as "polytherapy/drug-resistant" and cite the results text rather than over-claiming.

### 3.3 Neuroimaging phenotypes

MRI abnormal in **68.29%**; normal in 31.71%.

| Finding | % | Suggested HP term |
|---|---|---|
| Hypomyelination | 39.02 | **HP:0006808 Cerebral hypomyelination** or HP:0003429 CNS hypomyelination **[both verified]** |
| Global brain atrophy | 34.15 | HP:0002059 Cerebral atrophy [suggested] |
| Thin corpus callosum | 29.27 | **HP:0033725 Thin corpus callosum [verified]** |
| Leukoencephalopathy | 7.32 | HP:0002352 Leukoencephalopathy [suggested] |
| Cerebral white matter atrophy | 7.32 | HP:0012762 Cerebral white matter atrophy [suggested] |
| Small basal ganglia | 4.88 | HP:0006989 Abnormal basal ganglia morphology [suggested] |

Kurata et al. (**PMID:27246907**): *"Magnetic resonance imaging revealed hypomyelination, thin corpus callosum, and progressive cerebral atrophy."* — note the explicit **progressive** qualifier on atrophy (`clinical_course: PROGRESSIVE`).

### 3.4 Laboratory / biochemical phenotypes

Biochemistry is characteristically **near-normal**, which is diagnostically important because the clinical picture mimics mitochondrial disease.

- **Mild persistent lactate elevation** in 2/6 new cases (1.9–3.9 mmol/L), plasma only: *"Two individuals in our cohort exhibited a persistent mild elevation of lactate (1.9–3.9 mmol/l) without other abnormalities in mitochondrial biomarkers, including acid-base balance, creatine kinase, pyruvate, organic acids, amino acids, carnitines, oxidative stress markers, circulating cytokines, or mitochondrial growth factors. No elevated lactate was detected in urine or cerebrospinal fluid."* (PMID:41933351). HP term: **HP:0002151 Increased circulating lactate concentration [verified]** (note: the label is *not* "Increased serum lactate").
- **Elevated or high-normal blood copper** in 3/3 Japanese patients: *"Blood copper levels were also elevated or close to the upper normal levels in these children."* (PMID:27246907). This finding has **not been replicated** in any subsequent cohort — curate as a single-study observation, not a disease-level biomarker.
- Broad metabolic/mitochondrial screening "mostly unremarkable" (PMID:29343804).
- **Muscle respiratory chain:** combined complex I + IV deficiency in 1/3 tested (PMID:29343804); "low activity within the reference range" for complexes I, II/III, IV with elevated citrate synthase in another patient (PMID:34360601). Inconsistent — do not curate as a defining biochemical feature.

### 3.5 Dysmorphology

A recurrent but non-universal facial gestalt was described by Kurata et al. (PMID:27246907): *"Common facies were a depressed nasal bridge/ridge, broad eyebrows, and retrognathia."* Braun et al. explicitly note this **"does not seem to be shared with other cases in the literature"** (PMID:34360601) — curate as low-frequency / single-cohort. Suggested terms: HP:0005280 Depressed nasal bridge, HP:0011229 Broad eyebrow, HP:0000278 Retrognathia [all suggested].

### 3.6 Other systems

- **Skeletal:** congenital hip luxation and coxa valga antetorta requiring multiple surgeries in one patient (PMID:34360601); scoliosis listed among HPO annotations in MedGen.
- **Cardiac:** rare — atrial septal defect (1), heart failure (1) across 51 (PMID:41933351).
- **Hepatosplenomegaly (mild):** 3.33% (PMID:41933351).
- **Muscle:** a *bona fide* myopathology exists but is subtle. Braun et al. (PMID:34360601): *"Histological staining of our patient's muscle biopsy hints towards mitochondrial pathology, while the identification of dysregulated proteins attested to the vulnerability of the cell beyond the mitochondria."* Enzyme histochemistry showed reduced SDH reaction with normal COX; routine H&E, Gomori, PAS, NADH and ATPase stains were normal.
- **Fertility/spermatogenesis:** despite the gene's original "spermatogenesis-associated" naming, **no human fertility phenotype has been reported** — all patients are severely affected children/young adults.

### 3.7 Attenuated end of the spectrum — isolated sensorineural hearing loss

Critical for penetrance/expressivity modelling. Szczałuba et al. 2017 (**PMID:28293831**):

> "Herein we describe a family in which two SPATA5 mutations with established pathogenicity (p.Thr330del and c.1714+1G>A) were found in the proband and her younger sister. The proband had a similar clinical picture to the previous descriptions of EHLMRS. In the sister, the only manifestation was an isolated sensorineural hearing loss. Our findings extend the phenotypic spectrum of SPATA5-associated diseases and indicate that SPATA5 defects may account for a fraction of isolated sensorineural hearing impairment cases."

Two additional individuals in the Buchert consanguineous family had ID + microcephaly **without epilepsy or developmental delay** (PMID:27683084; Table 1 rows 18–24 of PMID:41933351). Intrafamilial variability with an identical genotype demonstrates **variable expressivity with additional unidentified modifying factors**.

### 3.8 Quality-of-life impact

No disease-specific QoL instrument (EQ-5D, PROMIS, SF-36, CPCHILD) has been applied to any AFG2A-RE cohort — a genuine gap. Functional burden is nonetheless inferable and severe: ~86% GMFCS IV–V, absent speech in all with ID, near-universal deafness plus ~80% visual impairment (a **dual sensory impairment** that compounds communication access), drug-resistant epilepsy in the majority, and dysphagia in 30% requiring feeding support. This combination places the disorder at the highest-dependency end of the DEE spectrum. Curate QoL as a `KNOWLEDGE_GAP` discussion.

---

## 4. Genetic / Molecular Information

### 4.1 Gene

| Field | Value |
|---|---|
| Approved symbol | **AFG2A** (previous: *SPATA5*; aliases *SPAF*, *AFG2*) |
| Approved name | AAA ATPase AFG2A |
| HGNC | `hgnc:18119` |
| Locus | 4q28.1 |
| Transcript | **NM_145207.3** (canonical; earlier literature NM_145207.2) |
| Protein | **892 aa**, UniProt **Q8NB90**; two conserved AAA+ ATPase modules (D1, D2) plus an N-terminal domain; a putative mitochondrial matrix-targeting sequence that is **not functional in neurons** (see §6.2) |
| Mouse orthologue | *Afg2a*, **MGI:1927170** |
| Yeast orthologue | **Drg1** |
| Expression | Ubiquitous — testis, spleen, skin, intestine, brain, skeletal muscle (PMID:34360601, PMID:41933351) |

### 4.2 Variant spectrum

> "Over 40 variants in AFG2A have been described as causative of AFG2A-RE. The most frequent variants are c.2081G>A, c.989_991del, c.251G>A, and c.1714+1G>A, present in 42% of the individuals, and more than half of the variants are missense." (PMID:41933351)

**Recurrent alleles:**

| Variant (NM_145207.3) | Protein | Class | Notes |
|---|---|---|---|
| c.989_991del | p.(Thr330del) | in-frame single-codon deletion | Most widely recurrent allele; rs748291365; ClinVar **Pathogenic**; ExAC ~0.02–0.03% (highest European MAF among EE-associated recessive variants in PMID:30552426), incl. one homozygote in population data |
| c.251G>A | p.(Arg84Gln) | missense | Recurrent; seen homozygous incl. via chr4 maternal isodisomy |
| c.2081G>A | p.(Gly694Glu) | missense | See §4.6 discrepancy flag |
| c.1714+1G>A | canonical +1 splice donor | splice | Recurrent, incl. homozygous |
| c.1822_1824del | p.(Asp608del) | in-frame deletion | Homozygous in the extended consanguineous family (PMID:27683084) |
| c.2130_2133del | p.(Glu711Profs\*21) | frameshift | Recurrent (Japan, Spain) |
| c.556C>T | p.(Arg186\*) | nonsense | Recurrent |

**Variant classes represented:** missense (>50%), nonsense, frameshift, canonical splice-site, in-frame codon deletions, start-loss (c.1A>C, p.Met1?), and a **multi-exon deletion CNV** (51 kb, exons 12–13).

**Functional consequence:** **loss of function / hypomorphic**. No gain-of-function or dominant-negative mechanism has been proposed. Two arguments strongly support residual-activity (hypomorphic) rather than complete-null biology in humans:
1. **No patient carries two unambiguous complete-null alleles** — biallelic combinations always include at least one missense or in-frame allele, and true null/null combinations are absent from the published cohort.
2. **Homozygous *Afg2a* knockout mice die before organogenesis** (§15) — complete loss is not compatible with mammalian development.

This is a load-bearing mechanistic inference for the KB: model the trigger node as *hypomorphic reduction of AFG2A ATPase activity*, not as complete ablation.

**Somatic vs germline:** exclusively germline. One notable exception in transmission mechanism — a *de novo* variant on the paternal allele combined with a maternally inherited variant (patient 73068, PMID:30552426), demonstrating that recessive disease can arise with a *de novo* second hit and therefore **cannot be excluded on the basis of negative parental carrier testing alone**.

**Population/constraint data:** gnomAD constraint metrics (pLI/LOEUF) could not be programmatically retrieved in this session — **do not populate these fields without direct gnomAD verification**. ClinGen has performed **zero dosage-sensitivity curations** for *AFG2A*, and heterozygous exon-deletion carriers are healthy, so haploinsufficiency is not a disease mechanism. ClinVar (queried 2026-08-01 via E-utilities): **970 total records** for `AFG2A[gene]`, of which **104** carry a pathogenic clinical-significance property.

### 4.3 Modifier genes

None identified. The intrafamilial variability in the Szczałuba family (severe encephalopathy vs isolated SNHL with the identical biallelic genotype, PMID:28293831) and in the Buchert consanguineous family (epilepsy present in some homozygous relatives, absent in others) is unexplained and constitutes a well-defined open question. Plausible but untested candidates: variation in the other 55LCC subunits (*AFG2B*, *AIRIM/C1orf109*, *CINP*) or in general ribosome-biogenesis capacity.

### 4.4 Epigenetics

No DNA-methylation episignature, histone-modification, or chromatin study of AFG2A-RE exists. Given that episignatures have been established for many DEEs, this is a tractable gap.

### 4.5 Chromosomal abnormalities

No recurrent cytogenetic syndrome. The relevant structural finding is **intragenic CNV as a disease allele** (51 kb exon 12–13 deletion, PMID:30552426) — mandating CMA or exome/genome CNV calling alongside sequencing. **Maternal uniparental isodisomy of chromosome 4** is a documented route to homozygosity.

### 4.6 ⚠ Three published-data discrepancies to avoid propagating

These were identified by cross-checking Table 1 of PMID:41933351 against the primary sources. **Do not transcribe the review table verbatim into the KB.**

1. **Genotype inversion for the Buchert 2016 families.** Table 1 of PMID:41933351 assigns homozygous **c.2081G>A p.(Gly694Glu)** to the extended consanguineous family (patients 18–24, no epilepsy) and homozygous **c.1822_1824del p.(Asp608del)** to patient B1 (with epilepsy). The Buchert abstract states the opposite: *"Linkage analysis followed by exome sequencing revealed a homozygous variant in SPATA5 (c.1822_1824del; p.Asp608del), which segregates with the phenotype in the family. In an unrelated family, we identified compound heterozygous variants in SPATA5 (c.[2081G > A];[989_991delCAA]; p.[Gly694Glu];[.Thr330del]) in a further individual with global developmental delay, infantile spasms, profound dystonia, and sensorineural hearing loss."* **Consequence:** the review's discussion claim that *"the c.2081G>A variant was associated with absence of epilepsy"* is, per the primary source, attributable to **p.(Asp608del)**, not p.(Gly694Glu) — and p.(Gly694Glu) was in fact found in an individual **with** infantile spasms. Any genotype–phenotype statement here must cite Buchert directly.
2. **Splice variant given a protein-deletion annotation.** Table 1 repeatedly renders `c.1714+1G>A; p.Thr339del`. A canonical +1 donor variant should be annotated `p.?`; Tanaka 2015 correctly lists `c.1714+1G>A; p.?`. Use `p.?`.
3. **Internally inconsistent row.** Patient 50 is listed as `c.554G>A; p.Lys648Glu` — c.554G>A corresponds to p.(Gly185Glu) elsewhere in the same table; p.Lys648Glu corresponds to c.1942A>G. Treat this row's genotype as unreliable.

---

## 5. Environmental Information

**Not applicable.** No environmental, toxic, occupational, radiation, lifestyle, dietary, or infectious factor has been implicated in causation or triggering. No infectious agent is involved (NCBI Taxonomy: N/A). Seizure-provoking factors beyond those generic to DEE have not been characterized (notably, fever-sensitivity has not been reported — unlike some channelopathy DEEs).

---

## 6. Mechanism / Pathophysiology

The mechanistic understanding has undergone a **substantial revision between 2015 and 2025**: from a presumed mitochondrial disorder to a **ribosome-biogenesis disorder (ribosomopathy) with secondary mitochondrial and proteostatic consequences**. Curating the causal chain correctly requires respecting this revision.

### 6.1 Primary mechanism — defective cytoplasmic pre-60S ribosome maturation

AFG2A is the human orthologue of yeast **Drg1**, the AAA+ ATPase that strips the placeholder assembly factor Rlp24 from newly exported pre-60S particles (Prattes et al. 2019, **PMID:31703473**):

> "Rix7, Rea1, and Drg1, which are well conserved across eukaryotes, are involved in different maturation steps of pre-60S ribosomal particles. These AAA-ATPases provide energy for the efficient removal of specific assembly factors from pre-60S particles after they have fulfilled their function in the maturation cascade."

The human step was defined by a genome-wide screen (Ni et al. 2022, Cell Rep, **PMID:35354024**):

> "These efforts identify two functionally uncharacterized genes, C1orf109 and SPATA5. We provide evidence that these factors, together with CINP and SPATA5L1, control a late step of human pre-60S maturation in the cytoplasm. **Loss of either C1orf109 or SPATA5 impairs global protein synthesis.** These results link ribosome assembly with neurodevelopmental disorders associated with recessive SPATA5 mutations."

Structural resolution followed (Dai et al. 2025, Nat Commun, **PMID:40268917**):

> "Here we reveal that SPATA5 forms a 4:2:2:2 complex with SPATA5L1, C1orf109, and CINP. This complex features an N-terminal ring made of C1orf109, CINP and NTDs of SPATA5/SPATA5L1, and two hexameric AAA+ ATPase rings. Intriguingly, a conserved cysteine C672 in the P-loop of SPATA5 is sulfinylated, generating an inactive conformation incompatible with ATP binding… Different from yeast, the recognition of the pre-60S particle is mediated by human-specific factor CINP, through two distinct sets of interactions: one with GTPBP4 and the other with ES27A."

Two points of curation value: (i) **human-specific architecture** — CINP-mediated pre-60S recognition has no yeast counterpart, limiting how far yeast Drg1 data can be extrapolated; (ii) the **redox-sensitive P-loop cysteine C672** provides a candidate regulatory/therapeutic node.

### 6.2 The 55LCC complex also governs replisome proteostasis and genome stability

Krishnamoorthy et al. 2024, Cell (**PMID:38554706**):

> "Here, we identify replisome factor interactions with a protein complex composed of AAA+ ATPases SPATA5-SPATA5L1 together with heterodimeric partners C1orf109-CINP (55LCC)… **Deficiency in the 55LCC complex elicited ubiquitin-independent proteotoxicity, replication stress, and severe chromosome instability.** 55LCC showed ATPase activity that was specifically enhanced by replication fork DNA and was coupled to cysteine protease-dependent cleavage of replisome substrates in response to replication fork damage. These findings define 55LCC-mediated proteostasis as critical for replication fork progression and genome stability and provide a rationale for pathogenic variants seen in associated human neurodevelopmental disorders."

Note the mechanism is explicitly **ubiquitin-independent** — distinguishing 55LCC from the VCP/p97 pathway. Replication stress in rapidly dividing neural progenitors is a plausible route to congenital microcephaly, complementary to the translation-capacity route.

### 6.3 Why a housekeeping defect produces a brain-and-ear-specific phenotype

The most consequential mechanistic advance of 2025 comes from Ni, Wei, Vona, Buszczak et al., Nat Cell Biol (**PMID:40760247**), studying the sister 55LCC subunit *AIRIM*/*C1orf109*:

> "Many neurodevelopmental defects are linked to genes involved in housekeeping functions, such as those encoding ribosome biogenesis factors. How reductions in ribosome biogenesis can result in tissue- and developmental-specific defects remains unclear. Here we describe variants in the ribosome biogenesis factor AIRIM/C1orf109 that are primarily associated with neurodevelopmental disorders. Using human cerebral organoids in combination with proteomic, single-cell RNA sequencing and single-organoid translation analyses, we identify a previously unappreciated drop in protein production during early brain development. **We find that ribosome levels decrease during neuroepithelial differentiation, making differentiating cells particularly vulnerable to perturbations in ribosome biogenesis during this time.** Reduced ribosome availability more profoundly impacts the translation of specific transcripts, disrupting both survival and cell fate commitment of transitioning neuroepithelia. **Enhancing mTOR activity suppresses the growth and developmental defects associated with AIRIM/C1orf109 variants.**"

This supplies the long-missing **tissue-specificity explanation**: a physiological trough in ribosome abundance during neuroepithelial differentiation creates a developmental window in which any further reduction in 60S output crosses a threshold. Selectively impaired transcripts included ribosomal proteins, the neurogenesis factor **FABP7**, and mitochondrial components bearing **5′ TOP-like motifs** — which also supplies a *translational* explanation for the observed mitochondrial phenotype. **mTOR pathway enhancement (TSC1 haploinsufficiency, PI3Kα activation) rescued organoid growth and cell-death phenotypes** — the first rational therapeutic target for this disease family.

> **Curation flag:** PMID:41933351 states *"no neurological disorders have been linked to the other components of the complex, C1orf109 and CINP, to date."* This was superseded ~5 months before that review's publication by PMID:40760247, which reports biallelic *AIRIM/C1orf109* variants in eleven unrelated families with global developmental delay, microcephaly, seizures and hearing loss — a phenotype closely overlapping AFG2A-RE. Curate the 55LCC complex as harbouring **at least three** neurodevelopmental disease genes (*AFG2A*, *AFG2B*, *AIRIM/C1orf109*).

### 6.4 Mitochondrial dysfunction — real, but likely downstream

Puusepp et al. 2018 (**PMID:29343804**) performed the foundational cell-biology work in rat cortical neurons and made a finding that **reframes the mitochondrial hypothesis**:

> "SPATA5 protein has a putative mitochondrial matrix-targeting sequence and has been shown to localize in mitochondria in mouse testis. However, subcellular localization data of SPATA5 in neurons and other cell types has not been reported. **To our surprise the localization of overexpressed SPATA5 in cultured primary cortical neurons was dominantly cytosolic and clearly not co-localizing with the mitochondrial marker.**"

Yet knockdown produced clear mitochondrial consequences:

> "there was a significant, 20% decrease in mitochondrial length in SPATA5 shRNA-treated neurons"
> "SPATA5 shRNA tends to decrease the fusion rate and increase the fission rate leading to significant decrease in fusion–fission ratio"
> "experiments performed at axonal endings… showed a statistically significant 12% decrease in signal in the SPATA5 shRNA group, suggesting a decrease in ATP levels… Overexpression of human shRNA-insensitive SPATA5 restored the ATP/ADP ratio in the SPATA5 shRNA-treated group demonstrating the specificity of shRNA."

Plus impaired neuronal maturation (short axons — PMID:34360601 summarizes: *"an imbalance in mitochondrial fusion–fission rates, impaired energy production and short axons"*).

Independently corroborated in patient-derived material (Raggio et al. 2023, **PMID:36849973**):

> "Oxygen consumption rates in platelets and PBMCs were impaired in the patient when compared to a healthy control. Also, a decrease in mitochondrial mass was observed in the patient monocytes with respect to the control. This suggests a true pathogenic effect of the mutations in mitochondrial function, especially in energy production and possibly biogenesis, leading to the observed phenotype."

And in patient fibroblasts (Nou-Fontanet et al. 2025, **PMID:40712368**):

> "In vitro studies demonstrated that AFG2A-deficient fibroblasts exhibited altered mitochondrial morphology and dynamics, as well as reduced ATP production and ROS levels. These abnormalities were significantly reversed when the fibroblasts were cultured in KD-MM."

**Recommended causal ordering for the pathograph:** hypomorphic AFG2A → impaired 55LCC ATPase activity → (a) defective pre-60S cytoplasmic maturation → reduced ribosome availability → selective translational insufficiency (including 5′-TOP-motif mitochondrial transcripts) → **secondary** mitochondrial fusion/fission imbalance, shortened mitochondria, reduced ATP; and (b) impaired replisome proteostasis → replication stress and chromosomal instability. Both converge on neuroepithelial/neural progenitor attrition and impaired neuronal maturation → microcephaly, hypomyelination, cortical atrophy, cortical hyperexcitability (IESS), sensorineural hearing loss, cerebral visual impairment.

The mitochondrial arm should be curated as a **downstream consequence with a documented `HUMAN_MODEL_MISMATCH`/hypothesis tension**: the protein is cytosolic in neurons, mitochondrial biomarkers are normal in patients, respiratory-chain findings are inconsistent, yet multiple independent patient-cell assays show real bioenergetic deficits. This is exactly the shape of a `mechanistic_hypotheses` entry with `status: EMERGING` for the "mitochondrial dysfunction as secondary to translational insufficiency" model.

### 6.5 Tissue/muscle proteomics

Braun et al. 2021 (**PMID:34360601**): *"Proteomic profiling of a quadriceps biopsy showed the dysregulation of 82 proteins, out of which 15 were localized in the mitochondrion, while 19 were associated with diseases presenting with phenotypical overlap to EHLMRS."* (31 up-, 51 down-regulated; ProteomeXchange **PXD026182**; upregulated disease-associated proteins included PURA1 and LAMA2.)

### 6.6 Immune involvement, metabolic pathways, fibrosis

No autoimmune or inflammatory mechanism. MedGen lists thrombocytopenia and immunodeficiency among annotated HPO features, but neither is supported by the 51-patient review and both should be treated as unreplicated single-report annotations. Intermediary metabolism is intact (normal organic acids, amino acids, carnitines, acid-base). No fibrosis, ischemia, or necrosis mechanism.

### 6.7 Suggested ontology terms for mechanism nodes

**GO biological process / molecular function [all suggested — verify with OAK]:**
- GO:0042273 ribosomal large subunit biogenesis
- GO:0000027 ribosomal large subunit assembly
- GO:0006412 translation
- GO:0016887 ATP hydrolysis activity; GO:0005524 ATP binding
- GO:0000226 / GO:0007005 mitochondrion organization
- GO:0008053 mitochondrial fusion; GO:0000266 mitochondrial fission
- GO:0006119 oxidative phosphorylation
- GO:0006260 DNA replication; GO:0031297 replication fork processing
- GO:0030163 protein catabolic process (ubiquitin-independent)
- GO:0021987 cerebral cortex development; GO:0022008 neurogenesis
- GO:0031175 neuron projection development (axon growth)
- GO:0031929 TOR signaling (rescue axis)

**GO cellular component:** GO:0005829 cytosol (primary neuronal localization, PMID:29343804); GO:0030687 preribosome, large subunit precursor; GO:0022625 cytosolic large ribosomal subunit; GO:0005739 mitochondrion (secondary/context).

**CL cell types [suggested]:** CL:0000540 neuron; CL:0000047 neuronal stem cell / neuroepithelial cell; CL:0000128 oligodendrocyte (hypomyelination); CL:0000855 auditory hair cell (paralogue *AFG2B* is expressed in "neurosensory hair cells and inner ear supporting cells", PMID:34626583 — direct AFG2A inner-ear expression data are lacking); CL:0008002 skeletal muscle fiber.

**UBERON [suggested]:** UBERON:0000955 brain; UBERON:0000956 cerebral cortex; UBERON:0002336 corpus callosum; UBERON:0002316 white matter; UBERON:0001844 cochlea; UBERON:0000970 eye; UBERON:0002240 spinal cord (corticospinal involvement / spasticity); UBERON:0001630 muscle organ; UBERON:0000473 testis (expression only).

**CHEBI [suggested]:** ATP, ADP, lactate, copper cation, ketone bodies (3-hydroxybutyrate).

---

## 7. Anatomical Structures Affected

**Primary organ:** brain (UBERON:0000955), bilaterally and diffusely.
- **Cerebral cortex** — global/cortico-subcortical atrophy (34%), often progressive; posterior/occipital predominance recurrently noted electrographically and clinically (cortical visual impairment, occipital-dominant spikes).
- **Cerebral white matter / myelin** — hypomyelination (39%), leukoencephalopathy (7%), white matter atrophy (7%); periventricular posterior predominance in at least one detailed case.
- **Corpus callosum** — thin in 29%.
- **Basal ganglia** — small in 5%; dystonia in 22% implicates extrapyramidal circuitry functionally even when imaging is normal.
- **Corticospinal tracts** — spasticity 61%, hyperreflexia.

**Sensory organs:**
- **Cochlea / auditory pathway** (UBERON:0001844) — sensorineural hearing loss in 94%, frequently detected on neonatal brainstem audiometry (i.e., **congenital**).
- **Visual system** — impairment in 79%, predominantly **cerebral/cortical** (post-geniculate) rather than ocular; strabismus and refractive error also present. Augmented visual evoked potential amplitudes (PMID:27246907) point to cortical hyperexcitability rather than retinal/optic-nerve failure. Note the 2026 review speculates about optic-nerve energy vulnerability by analogy with mitochondrial disease, but the primary data support a cerebral localization.

**Secondary/systemic:**
- **GI tract** — dysphagia (bulbar), GER, constipation (79% any GI symptom).
- **Skeletal muscle** (UBERON:0005090) — subtle myopathology (reduced SDH histochemistry, dysregulated proteome).
- **Musculoskeletal** — hip dysplasia/luxation, coxa valga, scoliosis (secondary to tone abnormality and non-ambulation).
- **Growth** — microcephaly is the cardinal growth abnormality; somatic growth is normal in 73%.
- **Heart** — rarely involved.

**Subcellular:** cytosol (site of AFG2A action and of pre-60S maturation), pre-ribosome/large subunit precursor, replication fork/replisome, mitochondrion (secondary).

**Lateralization:** bilateral and symmetric throughout.

---

## 8. Temporal Development

**Onset:** congenital to early infancy.
- **Congenital:** microcephaly (often present at birth — "congenital microcephaly" is part of the defining triad); sensorineural hearing loss detectable on newborn/neonatal brainstem audiometry.
- **Perinatal:** 75% uncomplicated; neonatal hypotonia 12.5%, respiratory distress 9.4%.
- **Epilepsy onset:** IESS at a **mean 9.53 months (range 2.5–27 months)** in the review cohort; mean 13.6 months in the KD series. Kurata: *"Epileptic spasms or tonic seizures emerged at 6-12 months of age."* Rarely later — one case is described as "developmental encephalopathy with **late-onset** epilepsy" (PMID:30552426).

**Onset pattern:** insidious/developmental — global developmental delay is apparent from early infancy, punctuated by an acute-subacute epilepsy onset in the first-to-second year.

**Course:** predominantly **static-with-progressive-elements**, not classically neurodegenerative.
- Developmental trajectory: severe global impairment reaching a plateau at a very low functional ceiling (absent speech, GMFCS IV–V).
- **Progressive elements documented:** *"progressive cerebral atrophy"* on serial MRI (PMID:27246907); the 2018 series characterizes the association as with *"a neurodegenerative disease"* (PMID:29343804). Formal developmental regression (HP:0002376 **[verified]**) is **not** a reported feature — distinguish "progressive atrophy on imaging" from "clinical regression."
- Epilepsy course: chronic, drug-resistant in the majority, requiring polytherapy.
- Duration: lifelong; oldest reported living individuals are 39 and 41 years (both from the attenuated, epilepsy-free consanguineous family) — i.e., **long survival is possible at the mild end**.

**Remission:** seizure freedom is achievable in a minority (4/16 with follow-up), always treatment-induced, never spontaneous. No spontaneous remission of any core feature.

**Critical intervention windows:**
1. **Neuroepithelial differentiation (embryonic)** — the mechanistic window of maximal vulnerability (PMID:40760247); largely inaccessible therapeutically but defines why postnatal intervention cannot reverse microcephaly.
2. **Early childhood, for ketogenic diet** — *"Greater seizure control was achieved when the ketogenic diet was initiated during early childhood."* (PMID:40712368)
3. **First months of life, for hearing habilitation** — congenital deafness, detectable neonatally; one patient received a hearing device before 2 months of age (PMID:34360601).

---

## 9. Inheritance and Population

### 9.1 Epidemiology

- **No formal prevalence or incidence estimate exists.** Orphanet ORPHA:457351 epidemiology could not be retrieved automatically; the disorder is consistently described as **"ultra-rare"** (PMID:41933351).
- **Cumulative published cases: 51** (PMID:41933351, July 2025 literature cut-off), plus ~30 additional unpublished cases collected by the ERN ITHACA / SPATA Foundation natural-history initiative → a real-world total on the order of **~80 known individuals worldwide**.
- **Enriched-cohort frequency:** the most quotable quantitative figure is the fraction among early-onset epileptic encephalopathies (Papuc et al. 2019, **PMID:30552426**):
  > "Notably, we found the recessive gene SPATA5 causative in as much as 3% of our cohort, indicating that it may have been underdiagnosed in previous studies."
  Confirmed on replication: *"our overall finding of 3 out of 102 combined research and diagnostic patients carrying causative biallelic variants indicates that SPATA5 is a frequent cause of developmental epileptic disorders accounting for 3% of cases."*
- **Yield in mitochondrial-suspicion cohorts is much lower:** *"The diagnostic yield was 0.6% and 0.8% in those two cohorts"* (Estonian n=21 of 181; German n=353) (PMID:29343804).
- **Underdiagnosis:** *"This disorder is likely underdiagnosed, despite exhibiting clinical features that constitute a hallmark of AFG2A-RE (microcephaly, deafness, and DEE)."* (PMID:41933351)

For the KB `prevalence` block, the defensible structured records are: `measure_type: UNKNOWN` / `prevalence_class: ULTRA_RARE` for population occurrence, plus a separate qualitative note recording the 3%-of-early-onset-EE/DEE figure (which is a **case-mix fraction, not a population prevalence** — do not convert it to `rate_per_100000`).

### 9.2 Inheritance genetics

- **Pattern:** autosomal recessive (HP:0000007). ClinGen: **Definitive**, AR.
- **Penetrance:** complete for the biochemical/genetic defect but with **markedly variable expressivity** — the same biallelic genotype produced full EHLMRS in one sister and isolated SNHL in the other (PMID:28293831). Practically: penetrance for *some* phenotype appears complete; penetrance for epilepsy is ~75%, for microcephaly ~86%.
- **Expressivity:** variable, including intrafamilial. Sensorineural hearing loss is the most consistently penetrant single feature (94%) and the sole feature at the mildest end.
- **Genetic anticipation:** not applicable (no repeat expansion).
- **Germline mosaicism:** not reported. However, a **paternal *de novo*** second allele has been documented (PMID:30552426) — recurrence counselling must account for both standard 25% AR recurrence and the possibility of *de novo* contribution.
- **Founder effects:** none established. The recurrent c.989_991del is present at low frequency across European population databases (rs748291365, highest European MAF 0.03%) and recurs in Japanese, European, and Uruguayan patients — consistent with either an old shared haplotype or recurrent mutation at a repetitive `CAA` tract; **haplotype analysis has not been published.**
- **Consanguinity:** contributes; the largest family cluster was consanguineous, but most reported cases are non-consanguineous compound heterozygotes.
- **Carrier frequency:** no published estimate. From ExAC/gnomAD, c.989_991del alone is ~0.02–0.03% allele frequency; aggregate carrier frequency across all pathogenic alleles has not been computed.

### 9.3 Demographics

- **Sex ratio:** 29 M / 22 F among 51 (56.7% male) — consistent with 1:1 and no sex effect (PMID:41933351).
- **Geography:** cases reported from the USA, Netherlands, Japan, Germany, Estonia, Poland, Italy, Switzerland, Bulgaria, Spain, Uruguay, and Canada — global distribution, no endemic cluster, likely reflecting exome-sequencing access rather than true prevalence.
- **Ancestry:** predominantly European in published series, almost certainly an ascertainment artefact.
- **Age distribution of reported individuals:** mean 8.35 years, **range 9 months – 41 years**.

---

## 10. Diagnostics

### 10.1 Genetic testing — the definitive diagnostic modality

- **First-line: whole-exome or whole-genome sequencing (trio preferred).** Every published diagnosis was made by WES or WGS. Nou-Fontanet: *"Genetic diagnosis was performed via clinical whole-exome sequencing, and variants were confirmed by Sanger sequencing."*
- **CNV detection is mandatory alongside sequencing** — a 51 kb intragenic deletion formed one allele in a published patient; the combined CMA+WES design is precisely what allowed Papuc et al. to detect it. WGS or exome-based CNV calling can substitute for standalone CMA.
- **Gene-panel testing:** *AFG2A* is included on epileptic-encephalopathy/DEE panels and on syndromic-hearing-loss panels; GTR lists **54 tests** for this condition. Panels lacking CNV analysis will miss deletion alleles.
- **Sanger confirmation and parental segregation** required (recall the *de novo* paternal allele case).
- **SNP-array/UPD assessment** is warranted when apparent homozygosity occurs in a non-consanguineous family (maternal chr4 isodisomy precedent).
- **Not indicated:** karyotype, FISH, mtDNA sequencing (though mtDNA testing is frequently performed *before* diagnosis because of the mitochondrial-disease mimicry), repeat-expansion testing.

### 10.2 Clinical and laboratory workup

| Test | Expected finding | Role |
|---|---|---|
| Head circumference (serial) | ≤ −2 SD in 86% | Cardinal sign |
| **Newborn/brainstem audiometry (ABR/BAEP)** | Bilateral SNHL, congenital | Near-universal; often the earliest objective abnormality |
| **EEG** | Interictal epileptiform activity 95%; multifocal discharges 75%, occipital predominance; hypsarrhythmia 20% | Essential for IESS diagnosis |
| **Brain MRI** | Abnormal in 68% — hypomyelination, atrophy, thin CC; **normal in 32%** | Supportive; a normal MRI does not exclude |
| **Visual evoked potentials** | Augmented amplitudes reported | Supports cortical rather than ocular visual impairment |
| Ophthalmology assessment | CVI, strabismus, refractive error | Habilitation planning |
| Plasma lactate | Normal or mildly elevated (1.9–3.9 mmol/L) | Non-specific; usually normal |
| Broad metabolic screen (organic/amino acids, carnitines, pyruvate, CK, acid–base, CSF and urine lactate) | **Normal** | Its *normality* alongside a mitochondrial-like phenotype is a diagnostic clue |
| Muscle biopsy | Usually normal light microscopy; reduced SDH histochemistry with normal COX; inconsistent respiratory-chain results | **Not recommended** as a diagnostic step now that the gene is known |
| Blood copper | Elevated/high-normal in one small series | Unreplicated; not a validated biomarker |

**LOINC candidates:** lactate (plasma) LOINC:2524-7 / LOINC:32693-4; copper (serum/plasma) LOINC:5631-7 **[all suggested — verify]**.

### 10.3 Omics-based diagnostics

No validated omics diagnostic exists. Research-grade assays with demonstrated patient-level signal, potentially deployable as functional-evidence adjuncts for VUS resolution:
- **Cellular bioenergetics on blood cells** — oxygen consumption in platelets/PBMCs and monocyte mitochondrial mass (PMID:36849973); explicitly framed by that group as minimizing "the need for invasive procedures such as muscle biopsy."
- **Fibroblast mitochondrial morphology/dynamics and ATP** (PMID:40712368).
- **Muscle proteomics** (PMID:34360601).
- **Fibroblast transcriptomics** distinguished affected from controls by principal components for the paralogous *AFG2B* disorder (PMID:34626583) — a plausible transferable approach.
- **Global protein-synthesis / ribosome-profiling assays** would be the mechanistically ideal functional readout given PMID:35354024 and PMID:40760247, but have not been applied diagnostically.

### 10.4 Differential diagnosis

| Differential | Distinguishing features |
|---|---|
| **Primary mitochondrial disease** (the single most important mimic) | *"The cardinal clinical features of AFG2A-RE may mimic those of a mitochondrial disease"* (PMID:41933351). AFG2A-RE has **normal metabolic screening**, no lactate elevation in CSF/urine, no stroke-like episodes, and a normal or mildly abnormal muscle biopsy. Historically most patients were first enrolled in mitochondrial-disease cohorts. |
| **AFG2B (*SPATA5L1*)-related disorders** | The closest genetic phenocopy. Two OMIM entities: **DFNB119 (#619615)**, nonsyndromic AR deafness; and **NEDHLS (#619616)**, neurodevelopmental disorder with hearing loss and spasticity. PMID:34626583: *"We report 28 bi-allelic variants in SPATA5L1 associated with sensorineural hearing loss in 47 individuals from 28 (26 unrelated) families. In addition, 25/47 affected individuals (53%) presented with microcephaly, developmental delay/intellectual disability, cerebral palsy, and/or epilepsy."* Distinguished only by gene; a shared 55LCC mechanism explains the overlap. |
| **AIRIM/C1orf109-related NDD** | Newly described (PMID:40760247) — global developmental delay, microcephaly, seizures, hearing loss in 11 families; same complex. |
| Other IESS/West syndrome genetic causes (*CDKL5*, *ARX*, *STXBP1*, *SCN2A*, *TSC1/2*, *ST3GAL3*) | Deafness plus congenital microcephaly is unusual in these; the AFG2A triad is discriminating. |
| Congenital CMV | Also causes microcephaly + SNHL + seizures + periventricular white-matter change; excluded by newborn/dried-blood-spot CMV PCR and characteristic calcifications. |
| Peroxisomal disorders, congenital disorders of glycosylation | Excluded by VLCFA and transferrin isoform testing. |
| Perinatal hypoxic-ischaemic injury / "cerebral palsy" | Frequently the initial working label given spastic-dystonic motor findings; 75% had uncomplicated perinatal courses. AFG2B disorders were explicitly presented as a genetic cause of "spastic-dystonic cerebral palsy." |

**Practical diagnostic heuristic:** *congenital microcephaly + congenital sensorineural deafness + infantile epileptic spasms + normal metabolic screen* should prompt AFG2A/AFG2B testing directly.

### 10.5 Screening

- No newborn screening. AFG2A-RE is **not** on the RUSP or comparable panels. However, **newborn hearing screening reliably flags these infants** — universal hearing screening is, incidentally, the earliest existing detection touchpoint, and AFG2A/AFG2B should be represented on genetic-deafness follow-up panels (per PMID:28293831, *AFG2A* "may account for a fraction of isolated sensorineural hearing impairment cases").
- **Carrier screening:** not on ACMG-recommended expanded carrier panels; would be reasonable in families with a known proband. The Dor Yeshorim programme participated in the *AFG2B* study, indicating community-based carrier-screening interest in this gene family.
- **Cascade testing** of at-risk relatives and reproductive partners of carriers is appropriate.

---

## 11. Outcome / Prognosis

### 11.1 Survival and mortality

- **48/51 alive at reporting**; three deaths at ages **3, 4.9, and 13.4 years**. Cause was respiratory failure in one; unstated in two (PMID:41933351). *(Note: the review reports this as 4.89%; 3/51 = 5.88% — cite the counts rather than the percentage.)*
- Puusepp's series independently records two sibling deaths at 3 years and 4 years 11 months (PMID:29343804).
- **Long survival is possible:** two brothers from the attenuated consanguineous family were alive at ages **39 and 41** (PMID:27683084 / Table 1 of PMID:41933351).
- No survival curve, median life expectancy, or standardized mortality ratio has been published. Deaths appear driven by respiratory complications in the context of profound motor impairment and dysphagia — the standard mortality profile for severe non-ambulatory DEE.

### 11.2 Morbidity and function

Uniformly high burden: absent speech in essentially all with ID; ~86% GMFCS IV–V; dual sensory impairment (deafness ~94% + visual impairment ~79%); drug-resistant epilepsy in the majority; dysphagia 30%. No formal disability instrument (ICF-based, CPCHILD, PedsQL) has been applied. Recovery potential is **nil for the neurodevelopmental core** — no treatment reverses microcephaly, deafness, or intellectual disability; the achievable gains are seizure control and functional/behavioural improvement.

### 11.3 Prognostic factors

Evidence is thin, but the following emerge:
- **Presence of epilepsy** (particularly IESS) marks the severe end; the epilepsy-free individuals in the Buchert family were the longest-lived.
- **Genotype:** no significant genotype–epilepsy association was found (PMID:41933351). The apparent "epilepsy-free" association with one homozygous in-frame deletion is confounded by all carriers belonging to a single family — and the allele's identity is disputed (§4.6).
- **Age at ketogenic-diet initiation** predicts seizure response: earlier is better (PMID:40712368).
- No prognostic biomarker exists.

---

## 12. Treatment

**There is no disease-modifying therapy.** Management is symptomatic, supportive, and multidisciplinary.

### 12.1 Antiseizure medications

Agents actually used in reported patients: **phenobarbital, valproate, levetiracetam, lacosamide, lamotrigine, zonisamide, ACTH/corticosteroids, vigabatrin**. Response is poor: only 4/16 with follow-up achieved seizure freedom, all on polytherapy — lacosamide + levetiracetam; valproate + levetiracetam + ACTH; lamotrigine + valproate; and one on ketogenic-diet monotherapy.

A clinically important negative finding: *"individuals with IESS do not achieve seizure control with usual first-line treatment (neither corticosteroids nor vigabatrin)."* (PMID:41933351) — i.e., **the standard IESS first-line algorithm underperforms in this genetic aetiology**, which is itself an actionable, curatable claim.

NCIT: `NCIT:C15986` Pharmacotherapy, with `therapeutic_agent` per drug (CHEBI/NCIT IDs **not verified this session — resolve with OAK before curation**).

### 12.2 Ketogenic diet — the most promising current intervention

Nou-Fontanet et al. 2025 (**PMID:40712368**):

> "Four patients received KD treatment for DRE, with seizure reduction rates of 0 %, 30 %, 70 % and 100 %, respectively. Improvement in social interaction improvement was observed in one patient, while improvements in attentional and motor function were noted in two. In vitro studies demonstrated that AFG2A-deficient fibroblasts exhibited altered mitochondrial morphology and dynamics, as well as reduced ATP production and ROS levels. These abnormalities were significantly reversed when the fibroblasts were cultured in KD-MM. In conclusion, this small series of patients with AFG2A-RE showed beneficial effects from KD treatment. Greater seizure control was achieved when the ketogenic diet was initiated during early childhood. These findings are preliminary and validation in multicenter prospective study is required."

The pairing of a clinical response with a matched *ex vivo* mechanistic readout (mitochondrial dynamics rescue in patient fibroblasts in KD-mimicking medium) is unusual for an ultra-rare disorder and makes KD the strongest mechanism-linked treatment claim available. An accompanying editorial (Catsman-Berrevoets, **PMID:40846618**, *"Deepening the understanding of mechanisms of antiepileptic effects of the ketogenic diet in children with AFG2A-related encephalopathy"*) marks its reception in the field. **Evidence grade: n=4–5, uncontrolled, retrospective — curate as PARTIAL/emerging, not established.**

NCIT: **`NCIT:C173168` Ketogenic Diet [verified]**, or `NCIT:C15447` Dietary Intervention; `therapeutic_modality: BEHAVIORAL`.

### 12.3 Sensory habilitation

- **Hearing amplification / cochlear implantation** — congenital profound SNHL; early fitting documented (hearing device before 2 months of age, PMID:34360601). Systematic outcome data for cochlear implantation in AFG2A-RE are absent, and profound cognitive impairment plus cerebral visual impairment complicate candidacy assessment. NCIT: **`NCIT:C157820` Cochlear Implant [verified]**; `therapeutic_modality: DEVICE`.
- **Vision** — CVI-adapted intervention, refractive correction, strabismus management.

### 12.4 Supportive, rehabilitative, and surgical

- Physiotherapy, occupational therapy, tone management for spasticity/dystonia, postural and seating management (GMFCS IV–V). NCIT: `NCIT:C15302` Physical Therapy, `NCIT:C121351` Occupational Therapy, `NCIT:C159273` speech/communication therapy (AAC given absent speech).
- Nutrition and feeding: dysphagia management, gastrostomy where indicated, GER treatment.
- Orthopaedic surgery for hip dysplasia/luxation and scoliosis (documented: multiple hip surgeries, PMID:34360601). NCIT: `NCIT:C16186` Orthopedic Surgical Procedure.
- Respiratory surveillance — the documented cause of death in one patient.
- Genetic counselling (`NCIT:C15240`).
- Palliative/supportive care (`NCIT:C15747`).

### 12.5 Experimental and future directions

- **ClinicalTrials.gov: no interventional trial registered for AFG2A/SPATA5 as of this search.** A multicentre prospective KD study is called for by PMID:40712368 but not yet registered.
- **mTOR pathway enhancement** is the first rationally derived target: in *AIRIM*/C1orf109-variant cerebral organoids, *"Enhancing mTOR activity suppresses the growth and developmental defects"* (PMID:40760247). Whether this transfers to AFG2A hypomorphs is untested, and the therapeutic window would be prenatal/neonatal for the structural phenotype — but it may be relevant to postnatal translation capacity. **Curate as a hypothesis with `evidence_source: IN_VITRO`, not as a treatment.**
- **The sulfinylated P-loop cysteine C672** (PMID:40268917) identifies a redox-regulated switch that the authors note "might be harnessed for therapeutic purposes."
- **Natural-history study** (ERN ITHACA / SPATA Foundation, Vona, Göttingen) — prerequisite infrastructure for any future trial.
- No gene therapy, ASO, enzyme-replacement, or cell-therapy programme exists. Note that ASO and gene-replacement strategies are conceptually poorly matched here: the phenotype is largely established prenatally, and the deficiency is of a ubiquitously required housekeeping ATPase.

### 12.6 Pharmacogenomics

None specific. Standard ASM pharmacogenomic considerations apply (e.g., HLA-B\*15:02 with aromatic ASMs, POLG-status before valproate — the latter especially relevant given the frequent initial mitochondrial-disease working diagnosis).

---

## 13. Prevention

- **Primary prevention:** not possible for an autosomal recessive Mendelian disorder. The only routes to occurrence-prevention are reproductive: **genetic counselling** with a 25% recurrence risk per pregnancy for carrier couples; **prenatal diagnosis** (CVS/amniocentesis) and **preimplantation genetic testing for monogenic disease (PGT-M)** once the familial variants are known; **carrier/cascade screening** of relatives and reproductive partners. Community-based carrier-screening programmes (e.g., Dor Yeshorim, which participated in the *AFG2B* study) provide a precedent model.
- **Secondary prevention (early detection):** universal newborn hearing screening is the existing system that reliably catches these infants earliest; inclusion of *AFG2A*/*AFG2B* on genetic-deafness follow-up panels would shorten the diagnostic odyssey. No newborn biochemical screen is applicable (metabolic screening is normal by design).
- **Tertiary prevention (complication prevention)** — this is where the actionable content lies:
  - Early hearing habilitation to preserve whatever auditory/communication access is achievable.
  - **Early ketogenic diet initiation** in drug-resistant epilepsy (the one evidence-linked timing recommendation).
  - Aspiration prevention through dysphagia assessment and feeding management; respiratory surveillance (documented mortality route).
  - Hip surveillance and scoliosis monitoring in the non-ambulatory (GMFCS IV–V) majority.
  - Avoidance of an unnecessary invasive diagnostic cascade (muscle biopsy) once the genetic diagnosis is available.
- **Immunization:** no disease-specific vaccine strategy; routine immunization plus respiratory-pathogen vaccination (influenza, RSV, pneumococcus) is standard of care for children with severe neurodisability and dysphagia.
- **Public/environmental health interventions:** not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** *Homo sapiens* **NCBITaxon:9606** is the only species with naturally occurring disease. Laboratory species used: *Mus musculus* (NCBITaxon:10090), *Rattus norvegicus* (NCBITaxon:10116), *Saccharomyces cerevisiae* (NCBITaxon:4932).
- **Orthologues:** mouse *Afg2a* **MGI:1927170** (NCBI Gene ortholog of human 166378); yeast **Drg1** — the functional orthologue whose pre-60S role framed the human mechanism (PMID:31703473, PMID:40268917).
- **Breed (VBO):** not applicable.
- **Natural disease in other species:** **none identified.** No OMIA entry for *SPATA5*/*AFG2A* in dog, cattle, horse, or other domestic species was found. No veterinary relevance.
- **Comparative biology / evolutionary conservation:** the AAA+ ATPase and its pre-60S maturation role are conserved from yeast to human — *"Rix7, Rea1, and Drg1, which are well conserved across eukaryotes, are involved in different maturation steps of pre-60S ribosomal particles"* (PMID:31703473). **But the conservation is partial and the difference matters:** the human complex is a 4:2:2:2 hetero-assembly (AFG2A:AFG2B:AIRIM/C1orf109:CINP) and *"Different from yeast, the recognition of the pre-60S particle is mediated by human-specific factor CINP"* (PMID:40268917). Yeast Drg1 data therefore inform the enzymology but not the substrate-recognition step or the disease-relevant complex composition. Curate this as an explicit conservation caveat.
- **Zoonotic potential / cross-species transmission:** not applicable.

---

## 15. Model Organisms

### 15.1 Mouse — *Afg2a* (MGI:1927170)

- **Alleles available:** MGI records **27 mutations** across classes — 3 targeted, 21 gene-trapped, 2 radiation-induced, 1 endonuclease-mediated; **38 strains/lines available through IMSR**.
- **IMPC knockout phenotype (allele `Afg2a^tm1b(KOMP)Wtsi`, homozygous, BCM phenotyping centre):**
  - **"Embryonic lethality prior to organogenesis"** (p = 0.0)
  - **"Preweaning lethality, complete penetrance"** (p = 0.0)
- **Interpretation — a first-class `HUMAN_MODEL_MISMATCH`:** the mouse constitutive null is embryonic lethal before organogenesis and therefore **cannot model the human disease at all**. Human AFG2A-RE necessarily results from **hypomorphic** biallelic combinations retaining partial ATPase function. Any faithful mouse model would need to be a **knock-in of a patient hypomorphic allele** (e.g., p.Thr330del, p.Arg84Gln) or a conditional/neural-specific hypomorph. **No such model has been published.** This is the single largest resource gap in the field and should be curated as a `HUMAN_MODEL_MISMATCH` discussion with proposed experiments.

### 15.2 Rat primary neuron model (the workhorse to date)

Puusepp et al. 2018 (**PMID:29343804**) — shRNA knockdown in primary neonatal Wistar rat cortical neurons, with rescue by shRNA-insensitive human *SPATA5*.
- **Recapitulates:** 20% reduction in mitochondrial length; significantly decreased fusion:fission ratio; 12% reduction in axonal ATP/ADP ratio (rescued by wild-type human SPATA5 — establishing specificity); impaired neuronal maturation with short axons.
- **Does not capture:** microcephaly, hearing loss, epilepsy, or any organismal phenotype. Acute knockdown also models complete loss rather than hypomorphic function.
- **Evidence source:** `MODEL_ORGANISM` (rat primary culture; arguably `IN_VITRO` for the cultured-neuron assays — split evidence items so each carries a single source type).

### 15.3 Human cell and organoid models

- **Patient fibroblasts** (n=3) — altered mitochondrial morphology and dynamics, reduced ATP production and ROS, all reversed in ketogenic-diet-mimicking medium (PMID:40712368). `IN_VITRO`. The best available pharmacodynamic model.
- **Patient PBMCs, platelets, monocytes** — impaired oxygen consumption, reduced mitochondrial mass (PMID:36849973). `IN_VITRO` / `HUMAN_CLINICAL` hybrid; split accordingly.
- **Patient muscle biopsy proteomics** — 82 dysregulated proteins, ProteomeXchange **PXD026182** (PMID:34360601). `HUMAN_CLINICAL`.
- **Genome-wide CRISPR loss-of-function screen with heterochronic ribosome labelling** in human cells — the discovery platform that assigned SPATA5 to pre-60S maturation (PMID:35354024). `IN_VITRO`.
- **Human cerebral organoids** — the most disease-relevant system available, established for the paralogous 55LCC subunit *AIRIM*/C1orf109 with proteomics, scRNA-seq, single-organoid translation analysis, ribosome profiling, and a genetic mTOR rescue (PMID:40760247). **Directly transferable to AFG2A and the obvious next model to build.** `IN_VITRO`.
- **Cryo-EM / integrative structural biology** of the purified 55LCC and pre-60S-bound complex (PMID:40268917, PMID:38554706). `IN_VITRO` / structural.
- **In silico:** molecular modelling of variant effects on protein stability was used as supporting evidence in PMID:27683084, PMID:30552426, PMID:34626583, PMID:36849973 → `COMPUTATIONAL`.

### 15.4 Yeast

*S. cerevisiae* Drg1 is the established genetic and biochemical model for the ATPase step, with well-characterized specific AAA inhibitors available (diazaborine; PMID:31703473). Useful for enzymology and inhibitor/chaperone-modulator screens; **not** a disease model, and limited by the human-specific CINP-mediated substrate recognition (§14).

### 15.5 Model databases

MGI (MGI:1927170), IMPC (`Afg2a`), IMSR (38 lines), KOMP/EuMMCR (tm1b allele), Alliance of Genome Resources, SGD (Drg1), ProteomeXchange (PXD026182), Cellosaurus (no dedicated AFG2A patient line deposited).

---

## Curation summary — recommended KB structure

**Pathophysiology chain (proposed nodes, upstream → downstream):**

1. **AFG2A Hypomorphic Loss of Function** — `MOLECULAR` — biallelic hypomorphic variants reduce AAA+ ATPase activity (evidence: PMID:26299366, PMID:27683084, PMID:29343804; hypomorphic inference supported by mouse null lethality, IMPC).
2. **55LCC Complex Dysfunction** — `MOLECULAR` — the 4:2:2:2 AFG2A/AFG2B/AIRIM/CINP assembly loses ATPase output (PMID:40268917, PMID:38554706).
3. **Impaired Cytoplasmic Pre-60S Ribosome Maturation** — `MOLECULAR` — late-step block in 60S subunit maturation (PMID:35354024, PMID:40268917, PMID:31703473).
4. **Reduced Global Protein Synthesis Capacity** — `CELLULAR` — with selective impact on 5′-TOP-like and neurogenesis transcripts (PMID:35354024, PMID:40760247).
5. **Neuroepithelial Vulnerability During Differentiation** — `CELLULAR` — physiological ribosome trough creates a developmental window of susceptibility (PMID:40760247).
6. *(Parallel branch)* **Replisome Proteostasis Failure → Replication Stress and Chromosomal Instability** — `CELLULAR` — ubiquitin-independent (PMID:38554706).
7. *(Downstream/secondary)* **Mitochondrial Fusion–Fission Imbalance and Bioenergetic Deficit** — `CELLULAR` — shortened mitochondria, reduced fusion:fission ratio, reduced axonal ATP (PMID:29343804, PMID:36849973, PMID:40712368). Attach a `mechanistic_hypotheses` entry (`status: EMERGING`) recording that AFG2A is cytosolic in neurons and that this arm is probably secondary to translational insufficiency rather than a primary mitochondrial-targeting defect.
8. **Impaired Neuronal Maturation and Cortical Development** — `TISSUE` — short axons, hypomyelination, reduced brain growth.
9. **Congenital Microcephaly / Cortical Hyperexcitability / Cochlear and Cortical Sensory Failure** — `ORGANISM`.

**Suggested module conformance to evaluate:** `epilepsy_excitation_inhibition_imbalance#Excitation-Inhibition Imbalance` (for the IESS/DEE arm) and `sensorineural_hair_cell_loss#Hair Cell Mechanotransduction Failure and Death` (for the SNHL arm — noting that direct AFG2A cochlear cell-type data are absent and the supporting expression evidence is from the *AFG2B* paralogue, so conformance should be declared cautiously or deferred).

**Treatment `target_mechanisms` pattern:** ketogenic diet → `INHIBITS`/modulates the *Mitochondrial Fusion–Fission Imbalance and Bioenergetic Deficit* node (PMID:40712368 provides the matched clinical + fibroblast-rescue evidence).

**Discussions to open:** (i) `HUMAN_MODEL_MISMATCH` — mouse null is embryonic lethal, no hypomorphic knock-in exists; (ii) `HUMAN_MODEL_MISMATCH` — neuronal cytosolic localization vs the annotated mitochondrial targeting sequence; (iii) `KNOWLEDGE_GAP` — no QoL instrument, no natural history, no prevalence, no episignature, no gnomAD-derived carrier frequency; (iv) `KNOWLEDGE_GAP` — unexplained intrafamilial variability (isolated SNHL vs full encephalopathy on identical genotypes).

**Before committing:** run `just fetch-reference` for the four PMIDs not yet in `references_cache/` (**40760247**, and confirm **41933351**, **40712368**, **40846618** are complete), then `just validate`, `just validate-references`, and `just validate-terms` — every HP/GO/CL/UBERON/NCIT/CHEBI ID marked **[suggested]** above must clear term validation before it enters the YAML.

---

## Sources

- [AFG2A-related encephalopathy, expanding the neurodevelopmental and epileptic spectrum — Orphanet J Rare Dis 2026 (PMID:41933351)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13049760/)
- [AFG2A-related encephalopathy: Effectiveness of ketogenic diet — Eur J Paediatr Neurol 2025 (PMID:40712368)](https://www.ejpn-journal.com/article/S1090-3798(25)00116-3/abstract)
- [Mutations in SPATA5 Are Associated with Microcephaly, Intellectual Disability, Seizures, and Hearing Loss — AJHG 2015 (PMID:26299366)](https://pubmed.ncbi.nlm.nih.gov/26299366/)
- [SPATA5 mutations cause a distinct autosomal recessive phenotype — Orphanet J Rare Dis 2016 (PMID:27683084)](https://link.springer.com/article/10.1186/s13023-016-0509-9)
- [Isolated Hearing Impairment Caused by SPATA5 Mutations — Adv Exp Med Biol 2017 (PMID:28293831)](https://pubmed.ncbi.nlm.nih.gov/28293831/)
- [Muscular and Molecular Pathology Associated with SPATA5 Deficiency in a Child with EHLMRS — IJMS 2021 (PMID:34360601)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8345956/)
- [Computational and mitochondrial functional studies of novel compound heterozygous variants in SPATA5 — Hum Genomics 2023 (PMID:36849973)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9972848/)
- [Bi-allelic variants in SPATA5L1 lead to intellectual disability, spastic-dystonic cerebral palsy, epilepsy, and hearing loss — AJHG 2021 (PMID:34626583)](https://pubmed.ncbi.nlm.nih.gov/34626583/)
- [A programmed decline in ribosome levels governs human early neurodevelopment — Nat Cell Biol 2025 (PMID:40760247)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12339376/)
- [OMIM #616577 — NEDHSB](https://omim.org/entry/616577)
- [OMIM \*613940 — AFG2A](https://omim.org/entry/613940)
- [OMIM \*619578 — AFG2B](https://omim.org/entry/619578); [#619615 DFNB119](https://omim.org/entry/619615); [#619616 NEDHLS](https://www.omim.org/entry/619616)
- [NIH GTR — Microcephaly-intellectual disability-sensorineural hearing loss-epilepsy-abnormal muscle tone syndrome (C4225276)](https://www.ncbi.nlm.nih.gov/gtr/conditions/C4225276/)
- [ClinGen — AFG2A gene curation (HGNC:18119)](https://search.clinicalgenome.org/kb/genes/HGNC:18119)
- [MGI — Afg2a (MGI:1927170)](https://www.informatics.jax.org/marker/MGI:1927170)
- [IMPC — Afg2a knockout phenotypes](https://www.mousephenotype.org/data/genes/MGI:1927170)
- [Orphanet — AFG2A gene page](https://www.orpha.net/en/disease/gene/AFG2A)
- [ERN ITHACA — Deep phenotyping and natural history of AFG2A (SPATA5) and AFG2B (SPATA5L1) disorders](https://ern-ithaca.eu/for-clinicians/calls-for-collaboration/deep-phenotyping-and-natural-history-of-afg2a-spata5-and-afg2b-spata5l1-disorders/)
- [ClinVar RCV000578291 — SPATA5 c.983_985CAA[2] (p.Thr330del)](https://www.ncbi.nlm.nih.gov/clinvar/RCV000578291.4/)
- [A further case of AFG2B-related neurodevelopmental disorder — Mol Genet Genomic Med 2024](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10767672/)
- [Neurodevelopmental Disorder with Psychomotor Delay, Hearing Loss, and Spasticity Caused by Compound Heterozygous SPATA5L1 Variants](https://pmc.ncbi.nlm.nih.gov/articles/PMC12693038/)
- [GeneCards — AFG2A](https://www.genecards.org/cgi-bin/carddisp.pl?gene=AFG2A)