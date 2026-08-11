---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-8[1m]
cached: true
start_time: '2026-07-01T09:17:28.167280'
end_time: '2026-07-01T09:17:28.178827'
duration_seconds: 0.01
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Chediak-Higashi Syndrome
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
  - claude-opus-4-8[1m]
  web_search_requests: 5
  num_turns: 29
  total_cost_usd: 3.20454
  session_id: 24b7c5f1-908f-4490-a1af-b604a780c706
  stop_reason: end_turn
citation_count: 16
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Chediak-Higashi Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Chediak-Higashi Syndrome** covering all of the
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

I now have enough verified material to write the full report. Here it is.

---

# Comprehensive Research Report: Chédiak-Higashi Syndrome (CHS)

**Prepared for dismech knowledge-base curation | Date: 2026-07-01**

> **Evidence provenance note (important for downstream curation):** Six of the PMIDs I quote below are already present as *verified abstract cache files* in `references_cache/` and their snippets are exact substrings of the cached text: **PMID:18544035, PMID:23521865, PMID:33329964, PMID:37788905, PMID:38774881, PMID:8673129**. These are safe to use as evidence items after the usual `just validate-references` pass. Other PMIDs I cite (e.g., 8896560, 8600540, 17293882, 40681653, 24618333) come from web/authoritative sources and **must be fetched with `just fetch-reference PMID:XXXX` and snippet-verified before being committed as evidence**. Several already-cached files in this branch (PMID:16862044, 8332901, 8380905, 8425221, 8751853, 23237827, 29127110) are actually about *other* diseases (X-linked agammaglobulinemia / BTK, NF2, PFOS hepatotoxicity, proteostasis) — **do not cite those for CHS**; they appear to be stale/placeholder cache entries.

---

## 1. Disease Information

**Overview.** Chédiak-Higashi syndrome (CHS) is a rare autosomal recessive multisystem disorder caused by biallelic loss-of-function variants in *LYST* (also called *CHS1*), which encodes the **lysosomal trafficking regulator**, a ~429-kDa cytoplasmic protein that governs the size, biogenesis, and fusion/fission dynamics of lysosomes and lysosome-related organelles (LROs). The pathognomonic cellular hallmark is **giant cytoplasmic granules** in leukocytes (and other granule-containing cells), visible on peripheral blood smear. The clinical tetrad-plus is: (1) **partial oculocutaneous albinism** (silvery hair, photophobia, nystagmus, reduced visual acuity); (2) **recurrent pyogenic infections** from neutrophil and NK/cytotoxic-lymphocyte dysfunction; (3) a **mild bleeding diathesis** from platelet dense-granule (δ storage pool) deficiency; and (4) **progressive neurologic degeneration** (peripheral neuropathy, ataxia, parkinsonism, cognitive decline) that dominates in long-term survivors. The life-threatening **"accelerated phase"** is a hemophagocytic-lymphohistiocytosis (HLH)-like lymphoproliferative infiltration, frequently EBV-triggered, and is the usual cause of early death.

The 2024 *Front Immunol* review states the core genetics succinctly (**verified cache quote, PMID:38774881**):
> "Mutations to the LYST gene result in Chédiak-Higashi syndrome, an autosomal recessive immunodeficiency characterized by defective granule exocytosis, cytotoxicity"

And the *J Med Genet* mutation-spectrum paper (**verified cache quote, PMID:37788905**):
> "Chediak-Higashi syndrome (CHS) is a rare autosomal recessive disorder characterised by partial oculocutaneous albinism, a bleeding diathesis, immunological dysfunction and neurological impairment. Bi-allelic loss-of-function variants in LYST cause CHS. LYST encodes the lysosomal trafficking regulator, a highly conserved 429 kDa cytoplasmic protein with an unknown function."

**Key identifiers.**
- **MONDO:** MONDO:0008963 (Chédiak-Higashi syndrome) — matches the `disease_term` in the existing draft.
- **OMIM:** #214500 (CHS, phenotype); *LYST* gene 606897.
- **Orphanet:** ORPHA:167 (classic Chédiak-Higashi syndrome); ORPHA:352723 (attenuated/atypical Chédiak-Higashi syndrome).
- **ICD-10:** E70.3 (albinism group); **ICD-11:** 4A00.1 (predominantly antibody/combined immunodeficiency with syndromic features) / commonly cross-referenced under immune dysregulation.
- **MeSH:** D002609 (Chediak-Higashi Syndrome).
- **Disease Ontology:** DOID:2935.
- **UMLS:** C0007965.

**Synonyms / alternative names.** Chédiak-Higashi syndrome; Chediak-Steinbrinck-Higashi syndrome; Béguez César disease (Béguez-César-Steinbrinck-Chédiak-Higashi); CHS; attenuated/atypical CHS (adult-onset milder form).

**Data derivation.** Information is drawn from **disease-level aggregated resources** (OMIM, GeneReviews, Orphanet, published natural-history cohorts — notably the NIH intramural CHS natural history study led by Introne/Gahl/Malicdan) rather than individual EHR records. The NIH cohort (NCT00005917) is the largest longitudinal source.

*Sources:* [OMIM #214500](https://www.omim.org/entry/214500); [GeneReviews NBK5188](https://www.ncbi.nlm.nih.gov/books/NBK5188/); [Orphanet ORPHA:167](https://www.orpha.net/en/disease/detail/167).

---

## 2. Etiology

**Primary cause (genetic).** CHS is **monogenic and autosomal recessive** — biallelic (homozygous or compound heterozygous) loss-of-function variants in *LYST* (chromosome **1q42.3**). There are no established non-genetic causes; environmental factors act only as *triggers* of downstream events (see below).

**Genetic risk factors.**
- Causal gene: **LYST / CHS1** (the only known disease gene). HGNC:1968.
- **Consanguinity** substantially increases risk, as expected for a rare AR disorder; many reported families are consanguineous (e.g., the atypical-CHS Pakistani kindred, **verified cache quote, PMID:23521865**): *"In a consanguineous Pakistani kindred with clinical phenotypes consistent with attenuated CHS, we performed SNP array-based homozygosity mapping and whole gene sequencing of LYST."*
- **Genotype as severity modifier (allelic/dose effect):** variant class is the dominant modifier of phenotype (see Section 4). Two null (nonsense/frameshift) alleles → severe classic CHS; at least one missense/in-frame allele with residual protein → milder atypical/attenuated CHS.

**Environmental risk / trigger factors.** No environmental factor *causes* CHS, but **viral infection (especially Epstein-Barr virus)** is the principal **trigger of the accelerated phase / HLH** (**verified cache quote, PMID:33329964**): the reported child *"was in advanced stage of HLH induced by an Epstein-Barr virus (EBV) infection."* Other infections and immune activation can likewise precipitate the accelerated phase.

**Protective factors.** No established genetic or environmental protective factors. The only "protective" modifier is **retention of partial LYST function** (hypomorphic missense/in-frame alleles), which shifts the phenotype toward the attenuated end. Early **allogeneic HSCT before accelerated phase** is protective against hematologic/immunologic death (Section 12).

**Gene-environment interaction.** The central GxE axis is **LYST-deficient cytotoxic-lymphocyte impairment × viral antigen load → uncontrolled macrophage activation (HLH/accelerated phase).** The defective granule-dependent killing by NK and CD8⁺ T cells cannot clear virally infected cells, driving the hyperinflammatory cascade — the same mechanism as familial HLH.

---

## 3. Phenotypes

For each, I give type, characteristics, and a suggested HP term (verify labels/IDs with OAK before curation).

| Phenotype | Type | Onset / course / frequency | Suggested HP term |
|---|---|---|---|
| **Partial oculocutaneous albinism / silvery-grey hair** | Physical sign | Congenital; stable; ~near-universal | Partial albinism HP:0007443; Silver-gray hair HP:0002216; Generalized hypopigmentation of hair HP:0011364 |
| **Photophobia** | Symptom | Early childhood; stable | Photophobia HP:0000613 |
| **Nystagmus** | Clinical sign | Early childhood | Nystagmus HP:0000639 |
| **Reduced visual acuity / foveal hypoplasia** | Sign | Childhood | Reduced visual acuity HP:0007663 |
| **Recurrent pyogenic (skin/respiratory) infections** | Clinical course | Infancy/childhood; recurrent; frequent | Recurrent bacterial infections HP:0002718 |
| **Neutropenia** | Lab abnormality | Childhood; variable | Neutropenia HP:0001875 |
| **Giant granules in leukocytes** (pathognomonic) | Lab/histopathology | Congenital; diagnostic | (no precise HP; use Abnormal granulation of granulocytes HP:0011925) |
| **Impaired NK / CTL cytotoxicity** | Lab abnormality | Congenital | Decreased NK-cell activity HP:0012178; Impaired lymphocyte cytotoxicity |
| **Mild bleeding diathesis / easy bruising** | Sign/symptom | Childhood; mild; frequent | Abnormal bleeding HP:0001892; Prolonged bleeding time HP:0003010; Abnormal platelet function |
| **Hepatosplenomegaly / lymphadenopathy** (accelerated phase) | Sign | Variable; episodic | Hepatosplenomegaly HP:0001433; Lymphadenopathy HP:0002716 |
| **Pancytopenia (accelerated phase/HLH)** | Lab | Episodic | Pancytopenia HP:0001876 |
| **Hemophagocytic lymphohistiocytosis** | Syndrome | Any age; life-threatening; ~85% of classic CHS eventually | Hemophagocytosis HP:0012156 |
| **Peripheral neuropathy** | Sign | Adolescent–adult; progressive | Peripheral neuropathy HP:0009830 |
| **Cerebellar ataxia** | Sign | Adult; progressive | Ataxia HP:0001251 |
| **Parkinsonism** | Sign | Adult; progressive | Parkinsonism HP:0001300 |
| **Cognitive decline / intellectual difficulty** | Behavioral/cognitive | Variable | Cognitive impairment HP:0100543 |

**Onset/severity/progression characteristics** (**verified cache quote, PMID:23521865**), describing the attenuated end and its neurodegeneration:
> "A small number of reports of rare, attenuated forms of CHS exist, with affected individuals exhibiting progressive neurodegenerative disease beginning in early adulthood with cognitive decline, parkinsonism, features of spinocerebellar degeneration, and peripheral neuropathy, as well as subtle pigmentary abnormalities and subclinical or absent immune dysfunction."

**Accelerated-phase phenotype cluster** (**verified cache quote, PMID:33329964**):
> "a high risk of developing hemophagocytic lymphohistiocytosis characterized by pancytopenia, high fever, and lymphohistiocytic infiltration of liver, spleen, and lymph nodes."

**Quality-of-life impact.** Severe in classic CHS (chronic infection burden, transfusion/immunoglobulin dependence, transplant morbidity, early mortality). In attenuated CHS, QoL is dominated by the **progressive, treatment-refractory neurodegeneration** (gait, cognition, autonomic function) that HSCT does not correct. No CHS-specific validated QoL instrument exists; generic tools (PROMIS, EQ-5D) would apply.

---

## 4. Genetic / Molecular Information

**Causal gene.** ***LYST*** (lysosomal trafficking regulator), aka **CHS1**; HGNC:1968; NCBI Gene 1130; chromosome **1q42.3**; OMIM 606897. Transcript NM_000081.4. Encodes a highly conserved ~429-kDa (3801-aa) cytoplasmic protein with a C-terminal **BEACH domain** and **WD40 repeats**, plumbing scaffolding/protein-interaction functions in membrane trafficking; its precise molecular function remains only partly defined ("80-year traffic jam," **PMID:38774881**).

- Human gene identification: **Nagle DL et al., *Nat Genet* 1996** (PMID:8896560, "Identification and mutation analysis of the complete gene for Chediak-Higashi syndrome") and **Barbosa MD et al., *Nature* 1996** (PMID:8600540, "Identification of the homologous beige and Chediak-Higashi syndrome genes") — both leveraging the murine *beige* homolog. *Fetch-verify before citing.*
- The murine ortholog (*Lyst*/beige) was cloned first (**verified cache quote, PMID:8673129**): *"The beige mutation is a murine autosomal recessive disorder, resulting in hypopigmentation, bleeding and immune cell dysfunction. The gene defective in beige is thought to be a homologue of the gene for the human disorder Chediak-Higashi syndrome."*

**Pathogenic variant spectrum & classification.** The definitive modern catalog is the NIH mutation-spectrum review (**verified cache quote, PMID:37788905**):
> "we compiled a total of 147 variants in LYST, including 61 frameshift variants (41%), 44 nonsense variants (30%), 23 missense variants (16%), 13 splice site variants or small genomic deletions for which the coding effect is unknown (9%), 5 in-frame variants (3%) and 1 start-loss variant (1%)."

- **Variant classes:** predominantly **truncating (frameshift + nonsense = ~71%)**, with missense, splice, and in-frame/small deletions completing the spectrum. Variants distribute across the large gene without a strong hotspot.
- **ACMG/AMP classification:** most reported variants are pathogenic/likely pathogenic; the paper explicitly re-classified novel and reported variants per ACMG/AMP guidelines.
- **Functional consequence:** **loss of function** (truncating alleles → absent/nonfunctional protein). No gain-of-function or dominant-negative mechanism is established; heterozygous carriers are unaffected.
- **Origin:** **germline**, biallelic. No somatic-mutation disease mechanism.
- **Allele frequency:** individual pathogenic variants are private/ultra-rare in gnomAD; carrier frequency is very low and population-nonspecific (consistent with <500 reported cases worldwide).

**Genotype-phenotype correlation (key clinical genetics point)** (**verified cache quote, PMID:37788905**):
> "a genotype-phenotype correlation emerged, whereby individuals harbouring at least one missense or in-frame variant generally resulted in milder disease, while those with two nonsense or frameshift variants generally had more severe disease."

**Modifier genes / epigenetics / chromosomal abnormalities.** No robustly established trans-acting modifier genes; the primary "modifier" is the *LYST* allele class itself (residual function). No CHS-specific epigenetic signature is established. CHS is a **single-gene disorder, not a copy-number/aneuploidy syndrome**, though large intragenic deletions/duplications in *LYST* occur (e.g., the feline model's large *LYST* duplication).

---

## 5. Environmental Information

- **Environmental factors:** None causal. Sun/UV exposure is relevant only insofar as albinism reduces photoprotection (increased actinic damage risk), and photophobia mandates light avoidance.
- **Lifestyle factors:** None causal. Infection-avoidance behaviors and prophylaxis modify infection burden.
- **Infectious agents (as triggers, not causes):** **Epstein-Barr virus** is the archetypal trigger of the accelerated phase/HLH (**PMID:33329964**). Other herpesviruses and bacterial/viral infections can precipitate accelerated phase or contribute to the chronic infection burden (recurrent *Staphylococcus aureus*, *Streptococcus*, and other pyogenic organisms; NCBI Taxonomy: EBV = NCBITaxon:10376; *S. aureus* = NCBITaxon:1280).

---

## 6. Mechanism / Pathophysiology

**Central lesion → causal chain.** LYST loss of function → **dysregulated biogenesis/fission of lysosomes and LROs → giant, dysfunctional granules** → cell-type-specific failures of granule-dependent processes → multisystem phenotype.

The LRO framework is well summarized (**verified cache quote, PMID:18544035**):
> "Lysosome-related organelles (LROs) are a heterogeneous group of vesicles that share various features with lysosomes, but are distinct in function, morphology, and composition. The biogenesis of LROs employs a common machinery, and genetic defects in this machinery can affect all LROs or only an individual LRO, resulting in a variety of clinical features."

**Cell-type-specific mechanisms (upstream → downstream):**

1. **Melanocytes → albinism.** Giant melanosomes fail to transfer melanin normally to keratinocytes/hair → partial oculocutaneous albinism, silvery hair (light-microscopy hair shafts show pathognomonic large, evenly distributed pigment clumps). *Cells:* melanocyte **CL:0000148**. *Location:* skin **UBERON:0002097**, hair follicle **UBERON:0002073**, eye **UBERON:0000970**.

2. **Neutrophils → infection.** Giant azurophilic granules impair **chemotaxis and regulated degranulation**; intramedullary destruction of granulocyte precursors causes **neutropenia** → recurrent pyogenic infection. *Cell:* neutrophil **CL:0000775**. *GO:* regulated exocytosis **GO:0045055**; neutrophil chemotaxis **GO:0030593**.

3. **NK cells & cytotoxic T lymphocytes → immune dysregulation/HLH.** Defective **cytotoxic granule (secretory lysosome) polarization and exocytosis** → failed perforin/granzyme delivery → impaired killing of infected/activated cells → uncontrolled macrophage activation → **HLH/accelerated phase**. *Cells:* NK cell **CL:0000623**, CD8⁺ cytotoxic T cell **CL:0000910**, macrophage **CL:0000235**. *GO:* natural killer cell mediated cytotoxicity **GO:0042267**; T cell mediated cytotoxicity **GO:0001913**.

4. **Platelets → bleeding.** **Dense-granule (δ) storage pool deficiency** → impaired secondary aggregation → mild bleeding diathesis. *Cell:* platelet **CL:0000233**. *GO:* platelet dense granule organization **GO:0060155**; platelet degranulation **GO:0002576**.

5. **Neurons/Purkinje cells → neurodegeneration.** Progressive **cerebellar Purkinje-cell loss, peripheral axonal degeneration**, with emerging evidence of **neuroinflammation** (microglial activation, complement, proinflammatory lipids). This arm is largely **independent of the hematologic disease and not corrected by HSCT**. *Cells:* Purkinje cell **CL:0000121**, peripheral neuron, microglial cell **CL:0000129**. *Location:* cerebellum **UBERON:0002037**, peripheral nervous system **UBERON:0000010**.

**Molecular pathway / cellular processes / subcellular compartments.** Core process is **lysosome/LRO organization** (GO:0007040 lysosome organization) and **vesicle-mediated transport / regulated secretion** (GO:0016192). *Subcellular compartments:* lysosome **GO:0005764**, melanosome **GO:0042470**, secretory/cytolytic granule, endosome. Protein dysfunction is **loss of a scaffolding/BEACH-domain regulator**, not enzyme deficiency — CHS is a **trafficking disorder**, distinct from classic lysosomal *storage* diseases (no accumulating substrate; the defect is organelle size/dynamics).

**Immune involvement.** Combined **innate + adaptive immunodeficiency** (neutrophil, NK, CTL) *plus* **immune dysregulation** (HLH-predisposition) — CHS sits in the **IUIS "immune dysregulation / familial HLH" category** (consistent with the draft's `iuis_category`).

**Metabolic/-omics.** No primary metabolic derangement. Recent mouse transcriptomics/lipidomics implicate **neuroinflammatory signaling and proinflammatory lipids** in the cerebellum (PMID:40681653, below). No established human proteomic/metabolomic diagnostic signature.

---

## 7. Anatomical Structures Affected

- **Organ/system level:** **Hematopoietic/immune system** (bone marrow **UBERON:0002371**, spleen **UBERON:0002106**, lymph nodes **UBERON:0000029**, liver **UBERON:0002107**); **integument** (skin **UBERON:0002097**, hair **UBERON:0001037**); **eye** (**UBERON:0000970**, retina/fovea); **nervous system** — central (cerebellum **UBERON:0002037**, brain **UBERON:0000955**) and peripheral (**UBERON:0000010**).
- **Tissue/cell level:** melanocytes, neutrophils, NK cells, cytotoxic T cells, platelets/megakaryocytes, macrophages/histiocytes, Purkinje neurons, peripheral axons/Schwann cells (see CL terms in Section 6).
- **Subcellular level:** **lysosome (GO:0005764), melanosome (GO:0042470), cytolytic/secretory granule, dense granule, endosomal compartment.**
- **Localization/lateralization:** systemic and **bilateral/symmetric** (albinism, neurodegeneration); hepatosplenomegaly/lymphadenopathy are central/generalized.

---

## 8. Temporal Development

- **Onset.** Classic CHS presents in **infancy/early childhood** (albinism from birth; infections and giant granules early). Attenuated/atypical CHS presents in **adolescence–adulthood**, often first with neurologic disease. Onset pattern for the accelerated phase is **subacute/acute** and can occur at any age.
- **Progression/stages.** (1) **Childhood classic disease** — albinism, infections, bleeding, giant granules; (2) **accelerated phase / HLH** — episodic, life-threatening, EBV-triggerable; (3) **neurodegenerative phase** — progressive in survivors and in attenuated CHS. The albinism is **stable/non-progressive**; the neurologic disease is **relentlessly progressive**.
- **Course pattern.** Chronic lifelong; punctuated by episodic accelerated-phase crises. Accelerated-phase HLH shows **remission in ~75% within 8 weeks** on HLH-directed therapy but **relapses are common and responses wane** (StatPearls/HLH-2004).
- **Critical intervention window.** **HSCT performed in the pre-accelerated / remission phase** is the key window for improving survival (Section 11–12).

---

## 9. Inheritance and Population

**Epidemiology.** Ultra-rare: **fewer than 500 cases reported worldwide**; Orphanet prevalence <1/1,000,000. Underdiagnosis is likely, especially of attenuated forms. No strong sex predilection (autosomal). ~**85–90% are the severe "classic" childhood form**; ~10–15% attenuated/atypical.

**Inheritance genetics.**
- **Pattern:** autosomal recessive (**HP:0000007**). Sibling recurrence risk 25%. From GeneReviews (as reflected in the draft's `inheritance` evidence): *"CHS is inherited in an autosomal recessive manner. If both parents are known to be heterozygous for a LYST pathogenic variant, each sib of an affected individual has at conception a 25% chance of being affected."*
- **Penetrance:** essentially complete for biallelic LOF; **expressivity is variable** and strongly allele-class-dependent (Section 4).
- **Anticipation:** none (not a repeat-expansion disorder).
- **Consanguinity/founder effects:** consanguinity is a major contributor; private variants predominate — no single global founder allele, though individual kindreds/populations carry recurrent variants.
- **Carrier frequency:** very low; population-nonspecific.

**Population demographics.** Reported across all ethnicities and geographies; no defined endemic region. Higher observed rates in consanguineous populations. Sex ratio ~1:1. Age distribution bimodal by form (early childhood classic vs. adult attenuated).

*Sources:* [Orphanet ORPHA:167](https://www.orpha.net/en/disease/detail/167); [GeneReviews NBK5188](https://www.ncbi.nlm.nih.gov/books/NBK5188/).

---

## 10. Diagnostics

**Clinical/laboratory tests.**
- **Peripheral blood smear / bone marrow:** **giant peroxidase-positive granules in neutrophils and other leukocytes** — the pathognomonic finding. Giant granules were the diagnostic anchor in the reported EBV-HLH case (**verified cache quote, PMID:33329964**): the child was *"diagnosed with Chediak-Higashi Syndrome based on silvery hair, pathognomonic hair microscopy and giant azurophilic granules in granulocytes."*
- **Light microscopy of hair shaft:** regularly distributed large melanin clumps (distinguishes CHS from Griscelli/Elejalde).
- **CBC:** neutropenia, and in accelerated phase pancytopenia; **NK-cell functional assay:** reduced cytotoxicity; **platelet function/dense-granule studies:** δ-storage-pool defect; **HLH workup** (ferritin, sIL-2R, triglycerides, fibrinogen, hemophagocytosis on marrow) when accelerated phase suspected.
- **Ophthalmologic exam:** iris transillumination, foveal hypoplasia, nystagmus.
- **LOINC:** neutrophil count 751-8; ferritin 2276-4 (HLH context).

**Genetic testing.**
- **Confirmatory:** biallelic pathogenic **LYST** variants by **single-gene sequencing**, or via **immunodeficiency/HLH gene panels, WES, or WGS**; MLPA/CMA to capture large *LYST* deletions/duplications. The NIH review emphasizes that improved variant classification enables **earlier diagnosis** (**verified cache quote, PMID:37788905**): *"The identification of novel pathogenic LYST variants and improvements in variant classification will provide earlier diagnoses and improved care to individuals with CHS."*
- **Carrier/prenatal/PGT:** possible once familial variants are known.

**Differential diagnosis.** Griscelli syndrome type 2 (RAB27A), Hermansky-Pudlak syndrome (HPS genes — same LRO-biogenesis family, PMID:18544035), Elejalde syndrome, familial HLH (PRF1, UNC13D, STX11, STXBP2), other primary immunodeficiencies with silvery hair. **Distinguishing feature:** giant leukocyte granules + evenly clumped hair melanin are unique to CHS.

**Omics-based diagnostics.** Not routine; research-stage transcriptomic/lipidomic signatures only.

**Screening.** Not part of standard newborn screening. Suspicion is clinical (silvery hair + infections/bleeding) → smear → LYST sequencing. Cascade carrier testing in families.

---

## 11. Outcome / Prognosis

- **Survival/mortality.** Without HSCT, classic CHS is usually **fatal in the first decade**, most often from the **accelerated phase/HLH** or overwhelming infection. The EBV-HLH case illustrates the grim accelerated-phase prognosis (**verified cache quote, PMID:33329964**): *"Treatment of accelerated-phase CHS is difficult with poor prognosis"* — the child *"did not survive."*
- **HSCT outcomes.** In the landmark international cohort of **35 children** (Eapen et al., *Bone Marrow Transplant* 2007, **PMID:17293882 — fetch-verify**), the **5-year overall survival was ~62%**, best with HLA-matched sibling donors and when transplanted **in remission/pre-accelerated phase**; outcomes were worst with active accelerated-phase disease at transplant.
- **The neurologic caveat.** HSCT corrects the immunologic/hematologic disease but **does not prevent or reverse the progressive neurodegeneration**, which becomes the dominant long-term morbidity in survivors and attenuated CHS (PMID:23521865). Recovery of neurologic function is not expected.
- **Prognostic factors.** Genotype (two null alleles → severe; ≥1 missense/in-frame → attenuated, PMID:37788905); presence/absence of accelerated phase; timing of HSCT; donor type. No validated molecular prognostic biomarker beyond genotype.

---

## 12. Treatment

**Curative / disease-modifying.**
- **Allogeneic hematopoietic stem cell transplantation (HSCT)** — the only treatment that corrects the immune/hematologic disease and prevents/treats the accelerated phase; ideally performed **early, in remission, before organ damage**. *(MAXO: hematopoietic stem cell transplantation — verify term, e.g. MAXO:0010039 organ/cell transplantation.)* Note this parallels HSCT experience in other inborn errors of immunity (the XLA transplant survey, PMID:37454339, is an analogous IEI-HSCT reference but is *not* about CHS — do not cite it as CHS evidence).

**Accelerated-phase / HLH therapy.**
- **HLH-2004 protocol:** **etoposide + dexamethasone + cyclosporine A**, bridging to HSCT once remission achieved. Remission in ~75% within 8 weeks; relapses common.
- *CHEBI:* etoposide **CHEBI:4911**; dexamethasone **CHEBI:41879**; ciclosporin **CHEBI:4031**. *(MAXO: chemotherapy MAXO:0000647.)*

**Supportive / preventive.**
- **Infection management:** prophylactic antibiotics, aggressive treatment of infections, immunoglobulin support as needed; vaccination *(MAXO:0001017)*.
- **Bleeding:** platelet support/desmopressin peri-procedure for the δ-storage-pool defect.
- **Ophthalmologic/dermatologic:** photoprotection, tinted lenses, refractive correction, sun protection.
- **Neurologic:** symptomatic/rehabilitative care (physical, occupational therapy; MAXO:0000011 physical therapy); no disease-modifying neuro-therapy exists.
- **Supportive care** MAXO:0000950; **genetic counseling** MAXO:0000079.

**Experimental / investigational.**
- **High-dose ascorbate and the tyrosine-kinase inhibitor context:** the "Towards the targeted management of Chediak-Higashi syndrome" review (*Orphanet J Rare Dis* 2014, ~PMID:24618333 — **fetch-verify**) discusses emerging targeted concepts. Preclinical work has explored agents that modulate LYST-dependent granule size.
- **Gene therapy / next-gen models:** the new complete-knockout mouse (PMID:40681653) is positioned as *"a robust platform for therapeutic development,"* including for the neurologic disease that HSCT cannot address.
- **Clinical study:** NIH natural history study **NCT00005917**.

---

## 13. Prevention

- **Primary prevention:** not possible (monogenic). **Genetic counseling** for at-risk consanguineous families; **carrier screening** and **prenatal / preimplantation genetic testing** once familial *LYST* variants are known.
- **Secondary prevention:** early diagnosis (smear + sequencing) and **pre-emptive HSCT before accelerated phase**; vigilant infection prophylaxis; EBV monitoring to catch accelerated-phase onset early.
- **Tertiary prevention:** HLH-directed therapy to prevent accelerated-phase mortality; photoprotection to prevent actinic skin damage; rehabilitation to mitigate neuro-disability.
- **Counseling:** cornerstone — recurrence risk 25%, reproductive options, and expectation-setting about persistent neurodegeneration post-HSCT.

---

## 14. Other Species / Natural Disease

CHS is a **classic comparative-genetics disorder** — naturally occurring *LYST*/beige-orthologue mutants exist across mammals and beyond, all showing hypopigmentation + giant granules + bleeding/immune defects, underscoring LYST's conserved trafficking role.

- **Beige mouse** (*Mus musculus*, NCBITaxon:10090) — the foundational model; *Lyst*/beige gene cloned first and used to find the human gene (**verified cache quote, PMID:8673129**): *"The beige mutation is a murine autosomal recessive disorder, resulting in hypopigmentation, bleeding and immune cell dysfunction."*
- **Other natural models:** Japanese Black **cattle** (*Bos taurus*), **Persian cats** (*Felis catus* — a large *LYST* duplication; feline model "resurrected" via assisted reproduction, *Sci Rep* 2019), **Aleutian mink**, blue/silver **foxes**, **rat**, **corn snake**, and a reported **killer whale**. *(OMIA has CHS entries across species; VBO for specific breeds.)*
- **Orthologous genes:** mouse *Lyst* (NCBI Gene 17864), and conserved BEACH-domain orthologs in *C. elegans* and yeast (per PMID:8673129).
- **Comparative pathology / conservation.** All models share partial oculocutaneous albinism, infection susceptibility, hemorrhagic tendency, and enlarged membrane-bound granules — but **natural animal models incompletely recapitulate the human neurodegeneration**, motivating engineered models (Section 15).
- **Zoonosis:** not applicable (genetic disorder).

---

## 15. Model Organisms

- **Natural mutants:** beige mouse, Persian cat, cattle, mink, etc. (Section 14) — good for **pigment, hematologic, and immune** phenotypes; **limited for neurologic** disease.
- **Engineered mouse (state of the art):** a **CRISPR-Cas9 complete-knockout Lyst mouse (ΔLYST-B6)** — **Greene et al., *Communications Biology* 2025 (PMID:40681653 — fetch-verify)** — is reported to recapitulate CHS *with an earlier-onset neurodegenerative phenotype*: partial oculocutaneous albinism, enlarged neutrophil granules/lysosomes, platelet dense-granule reduction with prolonged bleeding, and **progressive cerebellar Purkinje-cell loss + peripheral axonal degeneration with significant neurological impairment by ~6 months**, alongside **cerebellar neuroinflammation** (microglial/complement activation, proinflammatory lipids). Positioned as *"a robust platform for therapeutic development."* This is the best current model for the **neurologic** arm HSCT cannot treat.
- **Model types available:** knockout/null alleles (engineered), spontaneous hypomorph/null alleles (natural), plus **patient-derived cell lines** (fibroblasts, EBV-LCLs, iPSC potential) for cell-biological study of granule dynamics and cytotoxic-granule exocytosis.
- **Applications:** dissecting LYST's trafficking function, HLH/cytotoxicity mechanisms, and — with the new mouse — **neurodegeneration mechanisms and preclinical therapeutics** (gene therapy, small molecules).
- **Limitations:** natural models under-represent neurodegeneration; LYST's biochemical function remains incompletely defined ("80-year traffic jam," PMID:38774881).
- **Resources:** MGI (mouse *Lyst*/beige), OMIA (cross-species CHS), IMSR/JAX for beige strains.

---

## Consolidated Ontology-Term Suggestions (verify with OAK before curation)

- **MONDO:** MONDO:0008963 (disease).
- **HGNC/Gene:** *LYST* HGNC:1968; use lowercase `hgnc:1968` per repo convention.
- **GO (process):** lysosome organization GO:0007040; vesicle-mediated transport GO:0016192; regulated exocytosis GO:0045055; natural killer cell mediated cytotoxicity GO:0042267; platelet degranulation GO:0002576. **(GO CC):** lysosome GO:0005764; melanosome GO:0042470.
- **CL:** neutrophil CL:0000775; NK cell CL:0000623; cytotoxic T cell CL:0000910; melanocyte CL:0000148; platelet CL:0000233; macrophage CL:0000235; Purkinje cell CL:0000121; microglial cell CL:0000129.
- **UBERON:** skin UBERON:0002097; hair follicle UBERON:0002073; eye UBERON:0000970; bone marrow UBERON:0002371; spleen UBERON:0002106; liver UBERON:0002107; cerebellum UBERON:0002037; peripheral nervous system UBERON:0000010.
- **HP:** see Section 3 table (HP:0000007 AR inheritance; HP:0000613 photophobia; HP:0000639 nystagmus; HP:0002718 recurrent bacterial infections; HP:0001875 neutropenia; HP:0001892 abnormal bleeding; HP:0009830 peripheral neuropathy; HP:0001251 ataxia; HP:0001300 parkinsonism; HP:0012156 hemophagocytosis; HP:0011364/HP:0002216 pigment/silvery-hair).
- **CHEBI:** etoposide CHEBI:4911; dexamethasone CHEBI:41879; ciclosporin CHEBI:4031; ascorbate CHEBI:38290/29073.
- **MAXO:** HSCT (cell transplantation) MAXO:0010039; chemotherapy MAXO:0000647; genetic counseling MAXO:0000079; supportive care MAXO:0000950; vaccination MAXO:0001017; physical therapy MAXO:0000011.

---

## Curation-ready evidence anchors (already cache-verified in this branch)

| PMID | Use for | Status |
|---|---|---|
| **37788905** | Core definition, LYST LOF, 429 kDa, variant spectrum (147 variants), genotype-phenotype | ✅ cached/verified |
| **38774881** | LYST function, "defective granule exocytosis, cytotoxicity," AR immunodeficiency | ✅ cached/verified |
| **23521865** | Attenuated CHS, novel LYST in-frame deletion, adult neurodegeneration, consanguinity | ✅ cached/verified |
| **33329964** | Accelerated phase / EBV-triggered HLH, diagnostic giant granules + silvery hair, poor prognosis | ✅ cached/verified |
| **18544035** | LRO-biogenesis framework (positions CHS among LRO disorders) | ✅ cached/verified |
| **8673129** | Beige mouse = murine CHS homolog (model organism / gene discovery) | ✅ cached/verified |
| 8896560, 8600540 | Human LYST/CHS1 gene identification (1996) | ⚠️ fetch-verify |
| 17293882 | HSCT outcomes cohort (n=35, 5-yr OS ~62%) | ⚠️ fetch-verify |
| 40681653 | 2025 complete-KO mouse, earlier-onset neurodegeneration/neuroinflammation | ⚠️ fetch-verify |
| 24618333 | "Towards targeted management of CHS" (experimental therapeutics) | ⚠️ fetch-verify |

---

### Sources
- [OMIM #214500 — Chediak-Higashi Syndrome](https://www.omim.org/entry/214500)
- [GeneReviews: Chediak-Higashi Syndrome (NBK5188)](https://www.ncbi.nlm.nih.gov/books/NBK5188/)
- [Orphanet ORPHA:167 — Chédiak-Higashi syndrome](https://www.orpha.net/en/disease/detail/167) and [ORPHA:352723 — Attenuated CHS](https://www.orpha.net/en/disease/detail/352723)
- [StatPearls: Chediak-Higashi Syndrome (NBK507881)](https://www.ncbi.nlm.nih.gov/books/NBK507881/)
- [Morimoto et al. 2024, J Med Genet — LYST mutation spectrum (PMID:37788905)](https://pubmed.ncbi.nlm.nih.gov/37788905/)
- [Turner et al. 2024, Front Immunol — "LYST: an 80-year traffic jam" (PMID:38774881)](https://pubmed.ncbi.nlm.nih.gov/38774881/)
- [Weisfeld-Adams et al. 2013, Orphanet J Rare Dis — attenuated CHS (PMID:23521865)](https://pubmed.ncbi.nlm.nih.gov/23521865/)
- [Gopaal et al. 2020, Cureus — CHS with EBV-triggered HLH (PMID:33329964)](https://pubmed.ncbi.nlm.nih.gov/33329964/)
- [Huizing et al. 2008, Annu Rev Genomics Hum Genet — LRO biogenesis (PMID:18544035)](https://pubmed.ncbi.nlm.nih.gov/18544035/)
- [Perou et al. 1996, Nat Genet — murine beige gene (PMID:8673129)](https://pubmed.ncbi.nlm.nih.gov/8673129/)
- [Eapen et al. 2007 — HSCT for CHS (PMID:17293882)](https://pubmed.ncbi.nlm.nih.gov/17293882/)
- [Greene et al. 2025, Communications Biology — Lyst-KO mouse (PMID:40681653)](https://www.nature.com/articles/s42003-025-08482-1) and [PMC12274407](https://pmc.ncbi.nlm.nih.gov/articles/PMC12274407/)
- [Toro et al. 2014, Orphanet J Rare Dis — targeted management of CHS](https://link.springer.com/article/10.1186/s13023-014-0132-6)
- [NORD — Chediak-Higashi Syndrome](https://rarediseases.org/rare-diseases/chediak-higashi-syndrome/)

---

**One caretaker's note for the curator picking this up:** the existing `kb/disorders/Chediak-Higashi_Syndrome.yaml` draft is already solid on the LYST/AR/HLH backbone. The two richest veins still worth mining into structured pathophysiology nodes are (a) the **cell-type-resolved granule-dysfunction cascade** (melanocyte / neutrophil / NK-CTL / platelet / neuron — each a clean causal edge), and (b) the **HSCT-corrects-blood-but-not-brain** dissociation, which is the single most clinically important nuance and is well-supported by PMID:23521865 + the 2025 mouse paper. Before committing any of the ⚠️ web-sourced PMIDs, run `just fetch-reference` and eyeball the snippet against the cached abstract — a couple of those (17293882, 24618333, 40681653) I inferred numbers for from secondary sources, so they need a first-hand read.