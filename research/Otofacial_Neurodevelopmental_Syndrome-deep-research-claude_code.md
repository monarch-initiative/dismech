---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-31T17:16:52.292756'
end_time: '2026-07-31T17:21:34.726687'
duration_seconds: 282.43
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Otofacial Neurodevelopmental Syndrome
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
  - claude-sonnet-5
  web_search_requests: 6
  num_turns: 15
  total_cost_usd: 1.4835142000000001
  session_id: 9ef3a974-13cd-571e-b0e0-cf342d0ea0cf
  stop_reason: end_turn
citation_count: 14
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Otofacial Neurodevelopmental Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Otofacial Neurodevelopmental Syndrome** covering all of the
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

# Otofacial Neurodevelopmental Syndrome (OFNS) — Comprehensive Research Report

## 1. Disease Information

**Overview.** Otofacial neurodevelopmental syndrome (OFNS) is a recently delineated (2024), rare, **autosomal recessive** neurodevelopmental disorder caused by bi-allelic loss-of-function variants in **ZSCAN10**. It is characterized by the triad of (1) global developmental delay/intellectual disability, (2) variable facial asymmetry with hypotonic/dysmorphic facies, and (3) outer and inner ear malformations causing sensorineural hearing impairment. The condition was first described in a 2024 *Brain* paper by Laugwitz et al., "ZSCAN10 deficiency causes a neurodevelopmental disorder with characteristic oto-facial malformations" (PMID: [38386308](https://pmc.ncbi.nlm.nih.gov/articles/PMC11224597/)), based on 7 affected individuals from 5 unrelated families.

**Key identifiers:**
| Resource | ID |
|---|---|
| OMIM (phenotype) | [#620910](https://omim.org/entry/620910) — OTOFACIAL NEURODEVELOPMENTAL SYNDROME; OFNS |
| OMIM (gene) | [*618365](https://omim.org/entry/618365) — ZINC FINGER- AND SCAN DOMAIN-CONTAINING PROTEIN 10; ZSCAN10 |
| MONDO | [MONDO:0975705](https://monarchinitiative.org/MONDO:0975705) |
| MedGen | [UID 1857968](https://www.ncbi.nlm.nih.gov/medgen/1857968) / UMLS C5935642 |
| HGNC gene symbol | ZSCAN10 (formerly ZNF206) |
| NCBI Gene ID (human) | 84891 |
| Ensembl gene | ENSG00000130182 (chr16:3,088,890–3,099,295, GRCh38) |
| Orphanet / ICD-10/11 | Not yet assigned as of this writing — the disorder is too recently described (2024) to have an Orphanet or ICD entry; not found in Orphanet or WHO ICD searches during this research |

**Synonyms:** OFNS; ZSCAN10 deficiency; ZSCAN10-related neurodevelopmental disorder.

**Evidence basis:** All currently available clinical information derives from a single aggregated case-series publication (7 patients, 5 families) plus corroborating mouse and cell-line (mESC) functional data — this is an **aggregated disease-level literature resource**, not an EHR-derived cohort. There is no disease registry, natural-history study, or additional independent case series published yet (as of the July 2026 literature search performed for this report).

---

## 2. Etiology

**Disease causal factor:** OFNS is a monogenic disease caused by **bi-allelic (homozygous or compound heterozygous) protein-truncating (loss-of-function) variants in ZSCAN10** (chromosome 16p13.3). No environmental, infectious, or multifactorial causal contribution has been reported — it is a purely Mendelian, single-gene neurodevelopmental disorder.

**Genetic risk factors:**
- All 5 families' variants are protein-truncating variants (PTVs) clustered in the terminal coding exon (exon 6), which encodes 66% of the protein (518/780 amino acids) including 13–14 of the 14 C2H2 zinc-finger DNA-binding motifs.
- Variants identified (PMID:38386308):
  - **c.1456C>T, p.Gln486*** — homozygous in families F2, F4, F5 (5 individuals); population allele frequency ~7×10⁻⁴ in gnomAD South Asian subpopulation (17 heterozygotes; **no homozygous PTVs observed in gnomAD v2.1.1**), consistent with a possible South Asian founder allele.
  - **c.1112del, p.Pro371Argfs*49** — homozygous in family F1.
  - **c.1250C>A, p.Ser417*** and **c.2050del, p.His684Thrfs*153** — compound heterozygous in family F3.
- **Founder effect:** Families F2 and F5 shared runs of homozygosity (2.5–8.1 Mb) around the c.1456C>T allele, suggesting a shared ancestral haplotype in individuals of South/West Asian origin (Turkish, Iranian, Indian, Pakistani).
- **Consanguinity:** Consistent with autosomal recessive inheritance and the predominantly consanguineous/endogamous populations sampled (Turkey, Iran, India, Pakistan).
- Because all reported variants escape nonsense-mediated decay (they lie downstream of the last exon-junction complex), the mechanism is **truncated-protein production with loss/mislocalization of function**, not simple haploinsufficiency via mRNA degradation.

**Protective factors:** None reported; no protective variants or modifier alleles have been described for ZSCAN10-related disease.

**Gene-environment interactions:** None reported; no environmental modifiers of expressivity have been studied given the extreme rarity and recency of the disorder's description.

---

## 3. Phenotypes

All phenotype data below is drawn from the 7-patient cohort in Laugwitz et al. 2024 (PMID:38386308).

| Phenotype (clinical) | Frequency | Suggested HPO term | Notes |
|---|---|---|---|
| Global developmental delay | 7/7 | HP:0001263 (Global developmental delay) | Present in all patients; core feature |
| Intellectual disability | 7/7 | HP:0001249 (Intellectual disability) | Ranges mild to severe/profound |
| Delayed/absent speech | 5/7 delayed; 2/7 no expressive language | HP:0000750 (Delayed speech and language development) | Variable severity |
| Motor delay | 7/7 | HP:0001270 (Motor delay) | Variable severity |
| Facial asymmetry | 5/7 | HP:0000324 (Facial asymmetry) | Core distinguishing feature; validated computationally via GestaltMatcher (82% classification accuracy for asymmetry) |
| Hypotonic facies | Variable | HP:0000308 (Microretrognathia)-adjacent / HP:0000426 (Limited facial movement) | Unilaterally reduced facial movement described |
| Outer ear malformation | 7/7 | HP:0031703 (Abnormal external ear morphology) | Bilateral (5/7) or unilateral (2/7); low-set, posteriorly rotated, microtia, absent superior crus of antihelix |
| Microtia | Subset | HP:0008551 (Microtia) | |
| Low-set ears | Subset | HP:0000369 (Low-set ears) | |
| Posteriorly rotated ears | Subset | HP:0000358 (Posteriorly rotated ears) | |
| Inner ear/semicircular canal dysplasia | 2/2 tested (MRI) | HP:0011387 (Abnormal semicircular canal morphology) | Bilateral in both imaged patients |
| Sensorineural hearing loss | 4/5 tested | HP:0000407 (Sensorineural hearing impairment) | Unilateral deafness to profound bilateral loss |
| Behavioral abnormalities | 3/7 | — | Autistic features (2), aggression (2), stereotypic movements (1), hyperphagia (1) |
| Autistic behavior | 2/7 | HP:0000729 (Autistic behavior) | |
| Aggressive behavior | 2/7 | HP:0000718 (Aggressive behavior) | |
| Stereotypy | 1/7 | HP:0000733 (Stereotypy) | |
| Hyperphagia | 1/7 | HP:0002591 (Polyphagia) | |
| Visual impairment | 3/7 | HP:0000505 (Visual impairment) | |
| Micropenis | 2/4 males | HP:0000054 (Micropenis) | |
| Maldescended testis | Subset of the above | HP:0000028 (Cryptorchidism) | |
| Cardiac defect (mild LV enlargement) | 1/7 | HP:0001627 (Abnormal heart morphology) | |
| Cleft palate | 1/7 | HP:0000175 (Cleft palate) | |
| Down-slanting palpebral fissures | Variable | HP:0000494 (Downslanted palpebral fissures) | |
| Prominent epicanthic folds | Variable | HP:0000286 (Epicanthus) | |

**Onset:** Congenital/present from birth (ear malformations, facial asymmetry evident perinatally); developmental delay recognized in infancy/early childhood.
**Severity/progression:** Non-progressive, static congenital malformation plus a stable-to-slowly-clarifying developmental delay course (typical of a structural/transcription-factor neurodevelopmental disorder rather than a degenerative one); severity is variable across the cognitive spectrum (mild to profound).
**Quality of life impact:** Not formally measured (no EQ-5D/SF-36/PROMIS data reported); qualitatively, hearing loss and developmental delay are expected to impact communication, education, and adaptive functioning; behavioral features (aggression, autistic traits) may affect social functioning. No disease-specific QOL instrument exists yet given the 2024 initial description.

---

## 4. Genetic/Molecular Information

**Causal gene:** ZSCAN10 (Zinc Finger and SCAN Domain Containing 10; alias ZNF206), HGNC-approved symbol ZSCAN10, NCBI Gene ID 84891, located at 16p13.3 (OMIM *618365).

**Variant classification/type:** All four distinct variants identified to date are **protein-truncating variants (PTVs)** — one frameshift deletion pair and two nonsense (stop-gain) variants — clustered in the final coding exon (exon 6). Per ACMG/AMP framework these would be classified pathogenic/likely pathogenic on the basis of: PVS1-adjacent truncating location within a critical functional domain (loss of 13–14 zinc fingers), absence of homozygotes in population databases, full co-segregation with phenotype in available family members, and functional validation (mislocalization + loss of DNA binding).

**Population allele frequency:** The recurrent c.1456C>T (p.Gln486*) allele occurs at ~7×10⁻⁴ in the gnomAD South Asian subpopulation (17 heterozygous carriers, v2.1.1), with **zero homozygous PTV carriers** reported in gnomAD generally — consistent with a rare recessive disease allele under purifying selection against the homozygous state, and with a South/West Asian founder effect.

**Somatic vs. germline:** All variants reported are germline, inherited in autosomal recessive fashion; no somatic mosaicism reported.

**Functional consequences (loss of function):**
- Wild-type ZSCAN10 protein localizes to the nucleus; the truncated mutant protein (e.g., ZSCAN10^485 from c.1456C>T) is instead mainly cytoplasmic — i.e., the truncation disrupts nuclear import/localization.
- ChIP-qPCR shows the mutant protein loses DNA-binding capacity at the POU5F1 (OCT4) promoter, a direct ZSCAN10 target, versus strong wild-type binding.
- RNA-seq in Zscan10⁻/⁻ mouse embryonic stem cells (mESCs) shows 1,310 differentially expressed genes (710 down, 600 up; FDR<0.05), including dysregulation of pluripotency/developmental genes *Pou5f1*, *Sall4*, *Mtf2*, *Hoxb13*, *Meis2*. KEGG pathway analysis flagged "ATP-dependent chromatin remodeling" as the top affected pathway among downregulated genes.
- Direct quote (PMID:38386308): *"Loss of ZSCAN10 function is the likely consequence and pathomechanism of the identified disease alleles"* and *"Loss of ZSCAN10 dysregulates several genes associated with pluripotency and differentiation of ESCs."*

**Modifier genes:** None identified/reported.

**Epigenetic information:** No disease-specific DNA methylation, histone modification, or chromatin-mark studies have been reported in patients; the mechanistic link is via ZSCAN10's role as a transcriptional/chromatin-remodeling regulator rather than via an epigenetic mark on the ZSCAN10 locus itself.

**Chromosomal abnormalities:** None reported — OFNS is caused by small intragenic PTVs, not by copy-number/structural chromosomal rearrangements. (Note: a phenotypically distinct entity, "Chromosome 16p13.3 duplication syndrome," exists in the same cytogenetic region but is a separate, contiguous-gene-duplication condition, not OFNS — flagged here to avoid Named Entity Confusion.)

---

## 5. Environmental Information

No environmental, lifestyle, or infectious contributing factors have been identified or are biologically plausible for this monogenic transcription-factor disorder. Not applicable.

---

## 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream):**
1. **Molecular trigger:** Bi-allelic PTVs in ZSCAN10 exon 6 → truncated protein lacking most C2H2 zinc-finger DNA-binding motifs.
2. **Subcellular consequence:** Loss of nuclear localization (mutant protein mislocalizes to cytoplasm) → loss of transcription-factor access to target gene promoters.
3. **Molecular/transcriptional consequence:** Loss of ZSCAN10 binding at target promoters, including POU5F1 (OCT4) → dysregulation of pluripotency/developmental transcriptional network (Pou5f1, Sall4, Mtf2, Hoxb13, Meis2) and of ATP-dependent chromatin-remodeling pathway genes.
4. **Cellular/developmental consequence:** Disrupted transcriptional regulation during embryonic stem cell maintenance/early differentiation programs affecting cranial neural crest- and otic placode-derived structures.
5. **Tissue/organ consequence:** Aberrant morphogenesis of first/second pharyngeal-arch-derived facial structures (facial asymmetry) and otic-vesicle-derived structures (outer ear, semicircular canals, cochlea) → structural malformation and secondary sensorineural hearing loss; disrupted CNS developmental gene networks → global developmental delay/intellectual disability.
6. **Organism-level manifestation:** The OFNS clinical triad (developmental delay + facial asymmetry + oto-facial malformation/hearing loss), plus variably penetrant additional features (micropenis, cardiac defect, cleft palate, behavioral abnormalities).

**Molecular pathway:** ZSCAN10 acts as a **C2H2 zinc-finger/SCAN-domain transcription factor** operating within (and adjacent to) the core pluripotency transcriptional network alongside OCT4 (POU5F1), SOX2, and NANOG in embryonic stem cells, with genome-wide ChIP evidence of >3,000 binding sites, 183 of which overlap the OCT4/SOX2/NANOG trio — consistent with both direct and indirect roles in orchestrating developmental gene-regulatory programs. Suggested GO terms: **GO:0003700** (DNA-binding transcription factor activity), **GO:0000981** (RNA polymerase II-specific DNA-binding transcription factor activity), **GO:0019827/GO:1902459** (stem cell population maintenance / positive regulation thereof), **GO:0006338** (chromatin remodeling; specifically ATP-dependent chromatin remodeling per the KEGG-flagged pathway).

**Cellular processes:** Disrupted stem-cell transcriptional maintenance and differentiation-associated chromatin remodeling during embryogenesis (not apoptosis, autophagy, or classic inflammatory mechanisms). Suggested CL term: **CL:0002322** (embryonic stem cell) as the primary cellular substrate studied.

**Protein dysfunction:** Loss-of-function via truncation — loss of most zinc-finger DNA-binding domains plus **aberrant subcellular localization** (nuclear-to-cytoplasmic mislocalization of the truncated protein), rather than a gain-of-function or dominant-negative mechanism. Note a contextual duality: separate oncology literature (PMID:31933877) reports ZSCAN10 *overexpression* promoting glioma proliferation via OCT4 upregulation and Wnt/β-catenin activation — the inverse (gain-of-function/oncogenic) context, underscoring that ZSCAN10's normal role is dosage-sensitive and context-dependent. This is mechanistically distinct from OFNS and should not be conflated with the germline loss-of-function disease mechanism.

**Immune system involvement:** None reported/implicated.

**Tissue damage mechanisms:** Not applicable — this is a developmental morphogenesis defect (malformation) rather than a degenerative or injury-based tissue-damage mechanism.

**Molecular profiling performed to date:**
- **Transcriptomics:** RNA-seq of Zscan10⁻/⁻ vs wild-type mESCs (1,310 DEGs) — PMID:38386308.
- **Genomic structural features:** 3D geometric morphometric analysis of mouse embryonic craniofacial and inner-ear structures at E14.5 (26 surface landmarks + 22 inner-ear landmarks; Procrustes superimposition and fluctuating-asymmetry analysis).
- **ChIP-qPCR:** confirming direct ZSCAN10–Pou5f1 promoter binding, lost in the truncated mutant.
- No proteomics, metabolomics, lipidomics, single-cell, or spatial transcriptomic data have yet been published for this disorder.

---

## 7. Anatomical Structures Affected

**Organ level:**
- Primary: **Face** (asymmetry, dysmorphic features), **outer ear** (microtia, low-set/posteriorly rotated position, absent superior crus), **inner ear** (semicircular canal dysplasia, cochlear shortening in the mouse model), **brain/CNS** (developmental delay/intellectual disability — no structural cerebral anomalies noted on MRI beyond the otic findings).
- Secondary: **Cardiovascular** (mild left ventricular enlargement, 1/7), **palate** (cleft palate, 1/7), **genitourinary** (micropenis, cryptorchidism), **eyes** (visual impairment in 3/7, mechanism unspecified).
- Body systems involved: nervous system, craniofacial/musculoskeletal (ear/face), auditory/vestibular system, cardiovascular system, genitourinary system.

Suggested UBERON terms: **UBERON:0000980** (face), **UBERON:0001756** (external ear / outer ear), **UBERON:0001846** (inner ear... note: verify exact ID via OAK — likely **UBERON:0001846** for inner ear or **UBERON:0002105** depending on version), **UBERON:0001850** (semicircular canal), **UBERON:0001844** (cochlea), **UBERON:0001987** (palate).

**Tissue and cell level:** Craniofacial/pharyngeal-arch-derived neural-crest mesenchyme and otic-vesicle/otic-placode-derived epithelium are the developmental substrates implicated (inferred from the malformation pattern and mouse embryo findings), alongside the broadly studied **embryonic stem cell** (CL:0002322) as the in vitro model system for molecular mechanism.

**Subcellular level:** **Nucleus** (site of normal ZSCAN10 transcription-factor activity; GO Cellular Component **GO:0005634**) versus **cytoplasm** (site of aberrant mutant-protein mislocalization; **GO:0005737**).

**Localization/laterality:** Facial asymmetry and ear malformations are frequently **bilateral but asymmetric in severity**, sometimes strictly unilateral (2/7 unilateral outer-ear malformation; hearing loss ranging from unilateral to bilateral) — a distinctive "fluctuating asymmetry" pattern rather than fixed bilateral symmetry, also reproduced and quantified in the Zscan10⁻/⁻ mouse model.

---

## 8. Temporal Development

**Onset:** Congenital — facial asymmetry and ear malformations are present from birth; developmental delay is recognized in infancy/early childhood. No adult-onset or late-onset presentation reported.
**Onset pattern:** Insidious/congenital structural and developmental (not acute).
**Progression:** The malformative features (ear/face) are static/non-progressive congenital anomalies; the neurodevelopmental phenotype (developmental delay, cognitive impairment) is a stable, non-degenerative deficit typical of a transcriptional-regulator neurodevelopmental disorder — no reported evidence of regression or progressive decline.
**Disease course pattern:** Stable, chronic, lifelong (congenital malformation + static neurodevelopmental impairment); not episodic or relapsing-remitting.
**Disease stages:** Not formally staged — disease is not classified by stage/grade systems (unlike cancers).
**Remission patterns:** Not applicable (congenital structural/developmental disorder, not a remitting condition).
**Critical periods:** Embryonic craniofacial and otic morphogenesis (first-second pharyngeal arch and otic vesicle development, roughly corresponding to human 4th–8th gestational weeks by analogy to the mouse E14.5 model timepoint) represents the developmental window of vulnerability, based on the mouse embryo phenotyping timepoint.

---

## 9. Inheritance and Population

**Epidemiology:** Extremely rare — only 7 affected individuals from 5 families reported worldwide as of the founding 2024 publication; no formal prevalence or incidence estimate exists (likely well below 1/1,000,000; the disorder would fall in an ultra-rare/"cases in literature" prevalence class per Orphanet-style banding, with `prevalence_class: NOT_YET_DOCUMENTED` or `CASES_IN_LITERATURE` being the most defensible dismech curation choice).

**Inheritance pattern:** Autosomal recessive (AR) — confirmed by bi-allelic (homozygous or compound heterozygous) variant findings and full co-segregation with phenotype in family members tested.

**Penetrance:** Appears complete for the core phenotype (developmental delay + ear malformation) among the 7 reported bi-allelic carriers, though expressivity is markedly variable (see below); formal penetrance estimates are not available given the small cohort.

**Expressivity:** Highly variable — cognitive impairment ranges mild to profound; facial asymmetry present in 5/7; hearing loss severity ranges unilateral-mild to bilateral-profound; additional features (cardiac defect, cleft palate, micropenis, behavioral abnormalities) are present in only a subset, indicating variable expressivity even among carriers of the identical recurrent allele (c.1456C>T).

**Genetic anticipation:** Not applicable/not reported (not a repeat-expansion disorder).

**Germline mosaicism:** Not reported.

**Founder effects:** Strong evidence for a **South/West Asian founder allele** at c.1456C>T (p.Gln486*), shared among Turkish, Iranian, Indian, and Pakistani families, supported by shared runs of homozygosity (2.5–8.1 Mb) in families F2 and F5 and elevated allele frequency specifically in the gnomAD South Asian subpopulation.

**Consanguinity role:** Likely significant, consistent with the populations sampled and the autosomal recessive homozygous presentations in most families.

**Carrier frequency:** Estimated from gnomAD: ~7×10⁻⁴ heterozygote frequency for c.1456C>T specifically in the South Asian gnomAD subpopulation (i.e., roughly 1 in ~1,400 in that specific reference subpopulation); overall population carrier frequency across all ZSCAN10 PTV alleles is not separately reported.

**Population demographics:** All reported families are of Turkish (1), Iranian (4), Indian (1), and Pakistani (1) origin — a South/West/Central Asian geographic clustering, likely reflecting both the founder allele and ascertainment bias (genetic referral centers with expertise in consanguineous-population Mendelian disease gene discovery) rather than necessarily reflecting the disorder's true global geographic distribution.
**Sex ratio:** 3 females : 4 males reported — roughly equal, consistent with autosomal (non-X-linked) inheritance.
**Age distribution:** Patients examined ranged from 1 year 8 months to 15 years at time of report — a pediatric/adolescent cohort; no adult patients yet described (disease is presumably lifelong but long-term adult natural history is unknown).

---

## 10. Diagnostics

**Laboratory tests / biomarkers:** No specific diagnostic biochemical or serum biomarker exists; diagnosis is genetic/imaging-based, not biochemical.

**Imaging studies:**
- **MRI of the temporal bone/inner ear:** demonstrated bilateral semicircular canal dysplasia in both patients with available imaging (2/2), plus subtle osseous asymmetry of the skull and midface; no other cerebral structural anomalies identified.
- **3D facial/craniofacial imaging:** used in the mouse model (geometric morphometrics) and, in patients, computational facial-analysis tools (GestaltMatcher) were applied to frontal facial photographs to validate the facial-asymmetry phenotype, achieving 82% (41/50) correct classification for asymmetry detection, with all 6 affected individuals' frontal images correctly classified.

**Functional tests / electrophysiology:**
- **Audiology (audiometry):** sensorineural hearing loss documented in 4/5 tested individuals, ranging from unilateral deafness to profound bilateral loss. No vestibular symptoms (vertigo/imbalance) reported despite structural inner-ear pathology.

**Biopsy/pathology:** Not applicable/not performed — this is a structural developmental disorder, not evaluated by tissue biopsy.

**Genetic testing:**
- **Recommended approach:** Given the phenotype's rarity and gene-discovery status (2024), diagnosis currently relies on **exome or genome sequencing** (the modality by which all 7 reported cases were identified) rather than a targeted panel, as ZSCAN10 is unlikely to yet be included on most commercial hearing-loss or intellectual-disability gene panels.
- **WES/WGS utility:** High — this is precisely how the causal gene was discovered (trio/family exome sequencing with homozygosity mapping in consanguineous families).
- **Single-gene testing:** Feasible for confirmed familial variants once identified in a proband (e.g., targeted Sanger confirmation of the recurrent c.1456C>T allele in South Asian families).
- **Chromosomal microarray/karyotype/FISH:** Not the diagnostic modality of choice (disease is due to small intragenic PTVs, not copy-number/structural chromosomal changes), though may be used to exclude a differential such as 16p13.3 duplication/deletion syndrome.
- **Mitochondrial DNA / repeat-expansion testing:** Not applicable.

**Omics-based diagnostics:** Not yet in routine/research diagnostic use for this disorder; RNA-seq and ChIP-qPCR were used as **research validation** tools (mESC model), not as clinical diagnostic assays.

**Clinical criteria:** No formal consensus diagnostic criteria (DSM/ICD/society guidelines) yet exist, given the 2024 initial description; diagnosis currently rests on the combination of (a) bi-allelic ZSCAN10 PTV and (b) the characteristic phenotypic triad (developmental delay + facial asymmetry + oto-facial malformation/hearing loss).

**Differential diagnosis:** Should include other syndromic causes of combined craniofacial-asymmetry + ear-malformation + developmental delay, e.g., oculo-auriculo-vertebral spectrum (Goldenhar/hemifacial microsomia), CHARGE syndrome, branchio-oto-renal spectrum disorders, and other zinc-finger transcription-factor neurodevelopmental disorders — though a detailed differential-diagnosis discussion was not part of the identified literature and would benefit from independent verification.

**Screening:** No newborn or population screening program exists (disease too rare/recently described); no cascade or carrier screening program established, though targeted carrier testing for the recurrent c.1456C>T allele could be considered in high-risk South/West Asian consanguineous families given the founder-effect data.

---

## 11. Outcome/Prognosis

**Survival/mortality:** No mortality data reported among the 7 described patients; no evidence the condition is life-limiting based on available data, though the cohort is small and long-term follow-up is not yet published.

**Morbidity/function:** Long-term functional outcomes are not systematically reported; morbidity is driven by the combination of intellectual disability (mild-to-profound), hearing impairment (unilateral to profound bilateral sensorineural loss), and — in a subset — cardiac, palatal, or genitourinary anomalies requiring their own management.

**Quality of life measures:** None formally reported/available.

**Complications:** Feeding/speech difficulties secondary to cleft palate (1/7); potential cardiac monitoring needs for the individual with LV enlargement; genitourinary complications (undescended testis) requiring surgical correction; behavioral complications (aggression, autistic features) impacting social/adaptive function.

**Recovery potential:** Not a degenerative disease — the structural anomalies are fixed/congenital and the neurodevelopmental impairment is expected to be a static (not progressive) encephalopathy-type course, so "recovery" in the sense of reversal is not expected, but developmental gains with early intervention are plausible by analogy to other neurodevelopmental disorders (not disease-specifically demonstrated yet).

**Prognostic factors:** Not yet established given the small cohort; qualitatively, the marked variable expressivity (mild-to-profound cognitive range) suggests that individual outcome cannot currently be predicted from genotype alone (multiple individuals shared the identical c.1456C>T allele yet had differing symptom severity).

**Prognostic biomarkers:** None identified.

---

## 12. Treatment

No disease-specific/targeted therapy exists for OFNS (a very recently described monogenic disorder); management is **supportive and multidisciplinary**, addressing each component of the phenotype by extrapolation from standard care for its constituent features. No treatment outcome data (response rates, disease-specific trial results) exist for OFNS itself.

**Pharmacotherapy:** No specific pharmacological treatment targets ZSCAN10 or its pathway; symptomatic pharmacotherapy (e.g., for behavioral features such as aggression) would follow standard neurodevelopmental-disorder practice, not disease-specific evidence.
Suggested NCIT term: **NCIT:C15986** (Pharmacotherapy), used only for symptomatic/behavioral management, not disease-modifying treatment.

**Advanced therapeutics:** No gene therapy, cell therapy, RNA-based therapy, targeted therapy, or immunotherapy has been developed or trialed for OFNS. Given the loss-of-function truncating mechanism, gene-replacement/augmentation strategies are theoretically conceivable but entirely unstudied/speculative — should not be curated as an actual treatment.

**Surgical/interventional:**
- **Cleft palate repair** — standard surgical correction for the 1/7 patient with cleft palate. NCIT: **NCIT:C15329** (Surgical Procedure).
- **Orchidopexy** for cryptorchidism/maldescended testis. NCIT: **NCIT:C15329** (Surgical Procedure) or more specific urologic term if available.
- **Cochlear implantation** may be indicated for patients with profound bilateral sensorineural hearing loss (standard-of-care extrapolation, not disease-specifically reported).
- **Reconstructive otoplasty** may be considered for microtia/outer-ear malformation as in other syndromic microtia conditions (extrapolated, not disease-specifically reported).

**Supportive/rehabilitative care:**
- **Hearing aids** for less-than-profound sensorineural hearing loss (no dedicated NCIT term exists for "hearing aid usage" per the dismech NCIT remapping notes).
- **Speech-language therapy** — NCIT:C159273 (Speech Therapy) — for delayed/absent speech.
- **Physical/occupational therapy** — NCIT:C15302 (Physical Therapy) / NCIT:C121351 (Occupational Therapy) — for motor delay.
- **Developmental/early intervention programs** and special-education support for global developmental delay/intellectual disability.
- **Behavioral therapy** for autistic features, aggression, and stereotypy.
- **Genetic counseling** — NCIT:C15240 (Genetic Counseling) — for recurrence-risk counseling in autosomal recessive inheritance, particularly relevant given the consanguinity/founder-allele context.
- **Cardiology follow-up** for the subset with cardiac defects.

**Experimental treatments:** None identified in ClinicalTrials.gov or the literature search for ZSCAN10/OFNS specifically as of this report.

**Treatment strategy:** No published treatment algorithm exists; management is individualized and multidisciplinary (genetics, otolaryngology/audiology, cardiology, urology, developmental pediatrics, speech/OT/PT), following general principles for syndromic neurodevelopmental disorders rather than an OFNS-specific protocol.

---

## 13. Prevention

**Primary prevention:** Not applicable in the classic sense (this is a Mendelian genetic disease, not preventable by risk-factor modification); the only "primary prevention" lever is **reproductive/genetic counseling** in at-risk (consanguineous, or carriers of the South Asian founder allele) families, including discussion of preimplantation genetic diagnosis (PGD) or prenatal testing once a familial variant is known.

**Secondary prevention:** Early diagnosis via genetic testing in families with a known proband, followed by early audiological/developmental screening and intervention to mitigate downstream functional impact of hearing loss and developmental delay.

**Tertiary prevention:** Multidisciplinary management (above) to prevent/minimize complications (e.g., surgical correction of cleft palate to prevent feeding/speech complications; hearing amplification/cochlear implantation to mitigate the impact of hearing loss on language development).

**Immunization:** Not applicable — no infectious component.

**Screening/genetic counseling:** Carrier screening for the recurrent c.1456C>T allele could be considered in high-risk South/West Asian consanguineous populations given the demonstrated founder effect, though no formal population carrier-screening program has been established. Prenatal testing/PGD is feasible once a familial pathogenic variant is identified.

**Public health/environmental interventions:** Not applicable (no environmental risk factor identified).

**Prophylaxis:** Not applicable.

---

## 14. Other Species / Natural Disease

No naturally occurring ZSCAN10-deficient disease has been reported in companion animals or wildlife (no OMIA entry identified in this search). ZSCAN10 orthologs exist across mammals (e.g., mouse *Zscan10*, NCBI Gene; rat *Zscan10*, RGD:1310745; dog *ZSCAN10*, NCBI Gene 490045), but disease association has only been established via engineered knockout models (see Model Organisms below), not spontaneous natural disease in non-human species.

---

## 15. Model Organisms

**Primary model: Mouse (*Mus musculus*), Zscan10 knockout** — the core functional-validation model in the founding paper (PMID:38386308).
- **Model type:** Genetically engineered knockout-first allele, *Zscan10^tm2a(EUCOMM)Wtsi*, generated via a LacZ-cassette insertion upstream of exon 6 (International Mouse Phenotyping Consortium / EUCOMM resource lineage). This model reportedly showed **higher embryonic lethality than previously published Zscan10 knockout models**.
- **Phenotype recapitulation (E14.5 embryos):**
  - Significant fluctuating facial asymmetry compared to wild-type littermates (quantified via 3D geometric morphometrics, 26 surface landmarks, Procrustes superimposition).
  - Smaller eye size and ear opening on 3D imaging.
  - **Misalignment of the semicircular canals** and **shortening of the cochlea** (22-landmark inner-ear 3D morphometric analysis) — directly recapitulating the human inner-ear dysplasia phenotype.
  - Skull-shape differences on principal component analysis of symmetric shape variation.
- **Model limitations:** The knockout model is embryonic-lethal at higher rates than prior alleles, limiting study to embryonic timepoints (E14.5) rather than postnatal/adult phenotyping (e.g., postnatal hearing function, adult behavior, or long-term developmental outcomes cannot be directly assessed in a highly embryonic-lethal line). No mouse behavioral/cognitive phenotyping (correlating to the human developmental delay/intellectual disability phenotype) was reported in the available search results.
- **Research applications:** Craniofacial and inner-ear developmental morphogenesis; validating the causal role of Zscan10 loss in the oto-facial malformation phenotype independent of possible confounding in human genetic background.
- **Resource:** IMPC/EUCOMM allele resources (MGI database).

**Secondary model: Mouse embryonic stem cells (mESCs), Zscan10⁻/⁻** — an *in vitro* cellular model used for transcriptomic and mechanistic (ChIP-qPCR, subcellular localization) studies described in Section 6/4 above (PMID:38386308). This model recapitulates the molecular-level pathomechanism (transcriptional dysregulation of pluripotency/developmental genes, loss of POU5F1 promoter binding) but does not model the whole-organism phenotype.

**Related, disease-adjacent (not disease-causing) model literature on Zscan10 biology** (informative for mechanism, not for OFNS phenotype recapitulation per se):
- Cai et al., "Pleiotropic Functions for Transcription Factor Zscan10" (PLoS ONE; PMID available via [PMC4128777](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4128777/)) — establishes Zscan10's genome-wide binding-site profile and role alongside Oct4/Sox2/Nanog in ESC gene regulation.
- Nagelreiter et al., "Zscan10 is dispensable for maintenance of pluripotency in mouse embryonic stem cells" (PMID: [26592664](https://pubmed.ncbi.nlm.nih.gov/26592664/)) — an important **nuance/caveat**: this earlier study found Zscan10 was *not required* for baseline ESC self-renewal/pluripotency maintenance under standard culture conditions, which contextualizes the newer OFNS paper's findings as revealing a developmental (in vivo, organismal) rather than a strict cell-autonomous pluripotency-maintenance requirement — a good candidate for a `HUMAN_MODEL_MISMATCH`/nuance discussion node if curated into dismech, since apparent mESC dispensability contrasts with clear organismal necessity for normal craniofacial/otic development.
- Ma et al., "ZSCAN10 promotes cell proliferation, upregulates OCT4 expression, and activates Wnt/β-catenin signaling in glioma" (PMID: [31933877](https://pmc.ncbi.nlm.nih.gov/articles/PMC6945151/)) — describes an oncogenic, gain-of-function-type role for ZSCAN10 in glioma, mechanistically distinct from (and not to be conflated with) the germline loss-of-function OFNS mechanism; useful context for the gene's normal dosage-sensitive biology but not itself an OFNS model.

**Other species (non-model, orthology only):** No functional disease modeling reported in zebrafish, *Drosophila*, *C. elegans*, or yeast for ZSCAN10/OFNS in the available search results.

---

## Summary Evidence Table (Primary Citations)

| Claim | PMID/Source | Evidence type |
|---|---|---|
| OFNS gene discovery, clinical cohort (n=7/5 families), variant spectrum, GestaltMatcher facial analysis | PMID:38386308 (Laugwitz et al. 2024, *Brain* 147:2471–2482) | HUMAN_CLINICAL |
| Zscan10⁻/⁻ mouse embryo craniofacial/inner-ear morphometrics | PMID:38386308 | MODEL_ORGANISM |
| Zscan10⁻/⁻ mESC RNA-seq, ChIP-qPCR subcellular localization/DNA-binding studies | PMID:38386308 | IN_VITRO |
| ZSCAN10 genome-wide binding sites, role with Oct4/Sox2/Nanog | PMC4128777 (Cai et al., PLoS ONE) | IN_VITRO |
| Zscan10 dispensability for baseline ESC pluripotency maintenance | PMID:26592664 | IN_VITRO |
| ZSCAN10 oncogenic role in glioma (gain-of-function context) | PMID:31933877 | IN_VITRO / MODEL_ORGANISM (mixed — verify per-claim before citing) |

**Curatorial caveats for dismech entry construction:**
1. All PMIDs above must be independently fetched (`just fetch-reference PMID:XXXX`) and snippets validated against cached abstracts before use — this report's quotes were extracted via web fetch of the PMC full text, not yet run through the dismech reference-validation pipeline.
2. Orphanet and ICD identifiers could not be confirmed as existing yet for this very recently named condition (2024) — do not fabricate an Orphanet/ICD code; leave absent or explicitly note "not yet assigned" pending independent verification at curation time.
3. HPO term IDs suggested above (especially for semicircular canal dysplasia, downslanted palpebral fissures, epicanthus) should be verified with OAK (`uv run runoak -i sqlite:obo:hp info <ID> -O obo`) before committing to the KB, per standard dismech term-validation practice.
4. Given the extreme rarity/recency (single founding publication), this entry is a strong candidate for conservative curation with heavy reliance on `notes:` for claims lacking a directly quotable snippet, and appropriate use of `MECHANISTIC_HYPOTHESIS`/`HUMAN_MODEL_MISMATCH` framing for extrapolated (not disease-specifically demonstrated) treatment and prognosis content.

Sources:
- [Otofacial neurodevelopmental syndrome (Concept Id: C5935642) - MedGen - NCBI](https://www.ncbi.nlm.nih.gov/medgen/1857968)
- [Otofacial Neurodevelopmental Syndrome - MalaCards](https://www.malacards.org/card/otofacial_neurodevelopmental_syndrome)
- [Entry - #620910 - OTOFACIAL NEURODEVELOPMENTAL SYNDROME; OFNS - OMIM](https://omim.org/entry/620910)
- [Clinical Synopsis - #620910 - OMIM](https://www.omim.org/clinicalSynopsis/620910)
- [otofacial neurodevelopmental syndrome - Monarch Initiative](https://monarchinitiative.org/MONDO:0975705)
- [ZSCAN10 deficiency causes a neurodevelopmental disorder with characteristic oto-facial malformations - Brain (Oxford Academic)](https://academic.oup.com/brain/article/147/7/2471/7612544)
- [ZSCAN10 deficiency causes a neurodevelopmental disorder with characteristic oto-facial malformations - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11224597/)
- [Entry - *618365 - ZINC FINGER- AND SCAN DOMAIN-CONTAINING PROTEIN 10; ZSCAN10 - OMIM](https://omim.org/entry/618365)
- [ZSCAN10 Gene - GeneCards](https://www.genecards.org/cgi-bin/carddisp.pl?gene=ZSCAN10)
- [Pleiotropic Functions for Transcription Factor Zscan10 - PLOS ONE / PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4128777/)
- [Zscan10 is dispensable for maintenance of pluripotency in mouse embryonic stem cells - PubMed](https://pubmed.ncbi.nlm.nih.gov/26592664/)
- [ZSCAN10 promotes cell proliferation, upregulates OCT4 expression, and activates Wnt/β-catenin signaling in glioma - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6945151/)
- [ZSCAN10 zinc finger and SCAN domain containing 10 [Homo sapiens] - Gene - NCBI](https://www.ncbi.nlm.nih.gov/gene?Db=gene&Cmd=DetailsSearch&Term=84891)
- [Gene: ZSCAN10 (ENSG00000130182) - Ensembl](http://asia.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130182;r=16:3088890-3099295)