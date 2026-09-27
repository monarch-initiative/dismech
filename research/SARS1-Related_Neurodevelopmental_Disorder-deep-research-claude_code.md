---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-03T01:39:21.021642'
end_time: '2026-08-03T01:43:26.224927'
duration_seconds: 245.2
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: SARS1-Related Neurodevelopmental Disorder
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
  web_search_requests: 10
  num_turns: 21
  total_cost_usd: 1.4328601
  session_id: ccfe4e45-02a4-514e-bba5-3af1e8db647b
  stop_reason: end_turn
citation_count: 9
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** SARS1-Related Neurodevelopmental Disorder
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **SARS1-Related Neurodevelopmental Disorder** covering all of the
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

I have sufficient primary literature now (Musante 2017, Ravel 2021, Bögershausen 2022, the 2022 Turkish-family expansion paper, and the spastic-paraplegia/senescence paper). I'll compile the comprehensive report now.

# SARS1-Related Neurodevelopmental Disorder — Comprehensive Research Report

## 1. Disease Information

**Overview.** SARS1-related neurodevelopmental disorder — formally designated **Neurodevelopmental Disorder with Microcephaly, Ataxia, and Seizures (NEDMAS)** — is an ultra-rare, autosomal recessive Mendelian disorder caused by biallelic (and in one reported case, a dominant-negative de novo) pathogenic variants in *SARS1*, the gene encoding **cytoplasmic seryl-tRNA synthetase 1**. The core phenotype comprises global developmental delay/intellectual disability, postnatal microcephaly, early-onset seizures, ataxia, and muscle weakness, with an expanding phenotypic spectrum that now includes sensorineural deafness, cardiomyopathy, fever-triggered metabolic decompensation (in loss-of-function cases), and — in a distinct de novo dominant-negative case — complex spastic paraplegia without microcephaly ([Musante et al. 2017, PMID:28236339](https://www.ncbi.nlm.nih.gov/pubmed/28236339); [Ravel et al. 2021, PMID:34570399](https://pubmed.ncbi.nlm.nih.gov/34570399/); [Bögershausen et al. 2022, PMID unlisted](https://onlinelibrary.wiley.com/doi/full/10.1002/humu.24430); [Karaca-Mandic/Turkish cohort 2022, PMID:36004946](https://pubmed.ncbi.nlm.nih.gov/36004946/); [PMID:36041817](https://pmc.ncbi.nlm.nih.gov/articles/PMC9691831/)).

**Key identifiers:**
- **Gene:** *SARS1* (formerly *SARS*), HGNC:10537, located at chromosome 1p13.3
- **OMIM gene:** *607529 — Seryl-tRNA Synthetase 1; SARS1* ([OMIM:607529](https://omim.org/entry/607529))
- **OMIM phenotype:** **#617709 — Neurodevelopmental Disorder with Microcephaly, Ataxia, and Seizures (NEDMAS)** ([OMIM:617709](https://omim.org/entry/617709))
- **Suggested MONDO ID:** should correspond to the MONDO term cross-referenced to OMIM:617709 (mint via the standard OMIM→MONDO xref if not already in the local ontology cache; a specific MONDO CURIE could not be independently confirmed from public search results and should be verified with OAK against `sqlite:obo:mondo` before curation)
- **Inheritance:** Autosomal recessive (most reported families); one de novo dominant-negative case reported
- **Category:** Mendelian, aminoacyl-tRNA synthetase (ARS) disorder

**Synonyms/alternative names:** NEDMAS; SARS1 deficiency; seryl-tRNA synthetase 1 deficiency; SARS-related intellectual disability (older literature, pre-2017/pre-gene-renaming used "SARS" rather than "SARS1" since the gene was renamed from *SARS* to *SARS1* to distinguish from unrelated "SARS" coronavirus nomenclature).

**Important disambiguation:** *SARS1* encodes the **cytoplasmic** seryl-tRNA synthetase and must not be confused with ***SARS2***, which encodes the **mitochondrial** seryl-tRNA synthetase and causes a clinically distinct disorder (HUPRA syndrome — hyperuricemia, pulmonary hypertension, renal failure, alkalosis). Web search results returning SARS2/mitochondrial content were explicitly filtered out of this report; all findings below pertain to the cytoplasmic *SARS1* gene only.

**Evidence source note:** Information below is aggregated from published case series/case reports (peer-reviewed literature, disease-level aggregation) rather than large-cohort EHR data, consistent with an ultra-rare Mendelian disorder with fewer than ~15 reported individuals across all published families as of the most recent (2022) case series.

---

## 2. Etiology

**Disease causal factors:** Purely genetic/monogenic. Biallelic (homozygous or compound heterozygous) missense variants in *SARS1* are the predominant mechanism, causing partial loss of seryl-tRNA synthetase aminoacylation function. A single reported case involves a **de novo, dominant-negative, in-frame splice-altering deletion** producing a distinct, non-microcephalic spastic paraplegia phenotype via a toxic gain-of-function/dominant-negative mechanism rather than simple biallelic loss-of-function ([PMID:36041817](https://pmc.ncbi.nlm.nih.gov/articles/PMC9691831/)).

**Genetic risk factors:**
- Reported pathogenic variants (all missense unless noted):
  - **c.514G>A, p.(Asp172Asn)** — homozygous, consanguineous Iranian family, 4 affected siblings ([Musante et al. 2017, PMID:28236339](https://www.ncbi.nlm.nih.gov/pubmed/28236339))
  - **p.(Arg302Cys)** and **p.(Arg390Cys)** — compound heterozygous, second Iranian family ([Musante et al. 2017](https://www.ncbi.nlm.nih.gov/pubmed/28236339))
  - **c.638G>T, p.(Arg213Leu)** — homozygous, consanguineous Turkish family; associated with the deafness/cardiomyopathy/fever-decompensation phenotype ([Ravel et al. 2021, PMID:34570399](https://pubmed.ncbi.nlm.nih.gov/34570399/))
  - **c.1196C>T, p.(Thr399Met)** — novel missense variant identified in multiple unrelated Turkish NEDMAS families (biallelic) ([2022 clinical spectrum expansion, PMID:36004946](https://pubmed.ncbi.nlm.nih.gov/36004946/))
  - **chr1:109778053_109778055delGGT** (genomic deletion spanning the exon 7/intron 7 boundary) — de novo, heterozygous, splice-site-disrupting deletion causing in-frame insertion of 16 intronic bp / 5 aberrant amino acids near the enzyme active site; dominant-negative mechanism ([PMID:36041817](https://pmc.ncbi.nlm.nih.gov/articles/PMC9691831/))
  - Additional biallelic missense variants reported in a 2022 multi-gene series alongside WARS1 cases, in individuals presenting with an overlapping microcephaly/developmental-delay/brain-anomaly phenotype ([Bögershausen et al. 2022](https://onlinelibrary.wiley.com/doi/full/10.1002/humu.24430))
- **Consanguinity** is a recurring feature across nearly all reported pedigrees (Iranian and Turkish families), consistent with autosomal recessive transmission and suggesting the disorder is substantially under-ascertained outside consanguineous populations.
- No modifier genes or susceptibility loci have been reported to date; no GWAS/PheGenI signal exists given the extreme rarity and Mendelian nature of the condition.

**Environmental risk factors / gene-environment interaction:** The most clinically significant gene-environment interaction reported is **febrile illness as a precipitant of acute decompensation**. In the Ravel et al. (2021) family, affected children experienced severe metabolic/neurological decompensation during febrile episodes, in one case fatal, indicating that fever/infectious stress unmasks or exacerbates an underlying translational insufficiency — a pattern seen in several other aminoacyl-tRNA synthetase disorders where impaired global protein synthesis becomes rate-limiting under increased physiological demand. In the spastic-paraplegia case (PMID:36041817), seizures were "frequently precipitated by fever" as well, reinforcing fever as a cross-cutting trigger for this gene.

**Protective factors:** None reported in the literature; given the rarity of the disorder, no population-level protective variant or environmental protective factor data exists in gnomAD/GWAS resources specific to *SARS1*-NEDMAS.

---

## 3. Phenotypes

Phenotype burden is drawn from the aggregate of published cases (Musante 2017, n=5 across 2 families; Ravel 2021, n=2 siblings; the 2022 Turkish cohort, n=4 across 3 families; Bögershausen 2022, additional individuals; and the single spastic-paraplegia case). Because the total published cohort is small (~12-15 individuals), frequencies below are qualitative/descriptive rather than statistically robust percentages.

| Phenotype | Type | Suggested HPO term | Notes/Frequency |
|---|---|---|---|
| Global developmental delay | Symptom/sign | **HP:0001263** Global developmental delay | Reported in essentially all cases; core feature |
| Intellectual disability (moderate-severe; IQ 40-45 in original family) | Symptom | **HP:0001249** Intellectual disability | Core feature across all families |
| Postnatal microcephaly (−4 to −5 SD in original family) | Physical sign | **HP:0000252** Microcephaly | Present in most, but explicitly **absent** in the de novo dominant-negative spastic paraplegia case — a key phenotype-genotype distinguishing feature |
| Seizures | Symptom | **HP:0001250** Seizure | Early-onset in most; in the spastic-paraplegia case specifically "focal seizures... frequently precipitated by fever" |
| Ataxia | Sign | **HP:0001251** Ataxia | First apparent in childhood in the original family; present across nearly all reported cases |
| Muscle weakness | Sign | **HP:0001324** Muscle weakness | Reported in original and subsequent families |
| Speech impairment/delay | Symptom | **HP:0002167** Impaired speech or vocalization / **HP:0000750** Delayed speech and language development | Reported in original family and Turkish cohort |
| Aggressive behavior | Behavioral | **HP:0000718** Aggressive behavior | Reported in original Iranian family |
| Thin body habitus | Physical sign | **HP:0001519** Disproportionate tall stature / more precisely **HP:0004325** Decreased body weight or a thinness-specific term | Turkish cohort (2022) |
| Severe hypotonia | Sign | **HP:0008936** Severe muscular hypotonia | Turkish cohort (2022) |
| Cerebral and cerebellar atrophy (diffuse, bilateral) | Imaging finding | **HP:0002059** Cerebral atrophy / **HP:0001272** Cerebellar atrophy | Turkish cohort neuroimaging |
| Sensorineural/central deafness | Sign | **HP:0000407** Sensorineural hearing loss (or **HP:0008527** Congenital sensorineural hearing loss depending on documented mechanism) | Ravel et al. 2021 family |
| Cardiomyopathy | Sign | **HP:0001638** Cardiomyopathy | Ravel et al. 2021 family |
| Fever-triggered metabolic/neurological decompensation | Episodic/course feature | **HP:0034332** (or closest available "metabolic crisis" term) — consider free-text framing if no precise HPO term fits | Ravel et al. 2021 (fatal in one child); also seizure-precipitant pattern in PMID:36041817 |
| Spastic paraparesis (progressive in childhood, later stabilizing) | Sign | **HP:0001260** Spasticity / **HP:0007256** Progressive spasticity | De novo dominant-negative case only (PMID:36041817) |
| Non-progressive punctiform frontal subcortical white-matter hyperintensities on MRI | Imaging finding | **HP:0002499** or closest white-matter signal abnormality term | De novo case, distinguishes from classic biallelic phenotype |
| Increased visual evoked potential latency | Functional test finding | **HP:0000618**-adjacent or electrophysiology-specific term | De novo case |

**Onset:** Infantile to early childhood in virtually all reported cases (developmental delay and/or seizures typically noted in infancy/toddlerhood).

**Severity/progression:** Variable — ranges from moderate intellectual disability with stable ataxia (original Iranian family) to severe, fatal fever-triggered decompensation (Ravel et al. Turkish family) to a progressive-then-stabilizing spastic paraparesis (de novo case). This variability appears to correlate with variant type/mechanism (partial loss-of-function missense vs. dominant-negative splice variant vs. more severe loss-of-function variant with organ involvement).

**Quality of life impact:** Not formally studied with standardized instruments (EQ-5D/SF-36/PROMIS) in the literature; qualitatively, the combination of intellectual disability, seizures, ataxia, and (in some cases) cardiomyopathy/deafness confers substantial impact on daily functioning, communication, and mobility, with life-threatening risk during febrile illness in the loss-of-function subgroup.

---

## 4. Genetic/Molecular Information

**Causal gene:** *SARS1* (HGNC:10537; NCBI Gene ID 6301; OMIM *607529), chromosome 1p13.3, encoding cytoplasmic seryl-tRNA synthetase (protein SerRS/SYSC).

**Gene function:** SARS1 catalyzes the ATP-dependent aminoacylation of tRNA^Ser with L-serine — the first step of incorporating serine into nascent polypeptides during cytoplasmic translation. It also catalyzes the first step of selenocysteine (Sec) biosynthesis, since Sec-tRNA is initially charged with serine by SerRS before conversion to selenocysteine, giving SARS1 a secondary non-canonical role connecting it to selenoprotein synthesis. Notably, zebrafish studies (Fukui et al. 2009; Herzog et al. 2009) showed that Sars also has an aminoacylation-**independent** role in vascular development, indicating this synthetase family member has moonlighting functions beyond canonical translation.

**Protein structure:** SARS1 is a **Class II aminoacyl-tRNA synthetase (aaRS)** that functions as a homodimer in the cytoplasm (distinguishing it structurally/mechanistically from Class I aaRSs). Structural modeling of the de novo splice variant showed the aberrant 5-amino-acid in-frame insertion disrupts a critical β-strand near the catalytic core and displaces residues essential for ATP and serine substrate recognition, directly implicating the active site in pathogenesis for that variant ([PMID:36041817](https://pmc.ncbi.nlm.nih.gov/articles/PMC9691831/)).

**Pathogenic variant classes reported:**
- **Missense** (majority of biallelic cases): p.Asp172Asn, p.Arg302Cys, p.Arg390Cys, p.Arg213Leu, p.Thr399Met, plus additional biallelic missense variants in the Bögershausen 2022 series
- **Splice-region genomic deletion** (single de novo case): chr1:109778053_109778055delGGT, producing an in-frame 5-amino-acid insertion rather than a frameshift/null allele

**Variant classification (ACMG/AMP):** Not explicitly stated per-variant in the sources retrieved; given segregation in consanguineous families with clinical concordance and (for the de novo splice variant) direct functional/structural evidence, these variants would likely be classified pathogenic or likely pathogenic under ACMG/AMP criteria (PS2/PS3/PM1/PM2/PP1/PP3-type evidence), but formal ClinVar submission status should be independently verified.

**Allele frequency:** Not reported as present at appreciable frequency in population databases (gnomAD, 1000 Genomes) — consistent with an ultra-rare recessive disorder; specific gnomAD allele counts were not retrievable from the search results and should be checked directly in gnomAD/ClinVar during curation.

**Functional consequences:**
- Biallelic missense variants (loss-of-function, partial): reduce SARS1 aminoacylation activity, impairing global cytoplasmic protein synthesis capacity — most evident under physiological stress (fever).
- De novo splice deletion: **dominant-negative** mechanism — patient fibroblasts showed ~30% reduced aminoacylation activity, and yeast complementation studies demonstrated that co-expression of wild-type and mutant SARS1 produced significant growth defects, confirming a poisoning/dominant-negative effect of the mutant protein on the wild-type homodimer, rather than simple haploinsufficiency ([PMID:36041817](https://pmc.ncbi.nlm.nih.gov/articles/PMC9691831/)).

**Somatic vs. germline:** All reported variants are germline (constitutional); no somatic/cancer association has been reported for *SARS1*.

**Modifier genes:** None established.

**Epigenetic information:** No DNA methylation, histone modification, or chromatin-level disease mechanism has been reported for SARS1-NEDMAS in the retrieved literature.

**Chromosomal abnormalities:** None reported; disease mechanism is point-variant/small-indel based, not large structural rearrangement.

---

## 5. Environmental Information

- **Environmental factors:** No toxin, radiation, or occupational exposure has been implicated as a primary or contributing cause; this is a monogenic disorder.
- **Lifestyle factors:** Not applicable as a causal factor; however, febrile illness management (see below) is a critical environmental/clinical modifier of disease course.
- **Infectious agents:** No specific pathogen is causally implicated in disease onset. However, **febrile infectious illness (of any etiology) acts as a non-specific environmental trigger for acute decompensation and seizure exacerbation** in affected individuals — this is a gene-level vulnerability to physiological/metabolic stress rather than an infection-specific mechanism, analogous to fever-sensitivity patterns seen in other mitochondrial/translational disorders (e.g., RARS2-related pontocerebellar hypoplasia) and in certain channelopathies.

---

## 6. Mechanism / Pathophysiology

**Causal chain (loss-of-function/biallelic missense pathway):**
1. Biallelic missense variant in *SARS1* → partially impaired seryl-tRNA synthetase aminoacylation activity (charging of tRNA^Ser with serine)
2. Reduced/inefficient charging of tRNA^Ser → globally reduced or qualitatively impaired cytoplasmic protein synthesis, with likely selective vulnerability of high-translation-demand tissues (developing CNS, cardiac muscle, cochlea)
3. Chronic translational insufficiency during development → microcephaly, ataxia, intellectual disability, cardiomyopathy, sensorineural deafness (organ-specific manifestations depending on variant severity/tissue vulnerability)
4. Acute physiological stress (fever) → further reduction in translational capacity relative to increased metabolic demand → acute neurological/metabolic decompensation, in the most severe reported case leading to death

**Causal chain (de novo dominant-negative pathway — distinct disease mechanism):**
1. De novo in-frame splice-disrupting deletion → mutant SARS1 protein with an aberrant 5-residue insertion near the catalytic/ATP-serine-binding active site
2. Mutant monomer co-assembles with wild-type monomer in the obligate homodimer → dominant-negative poisoning of overall enzyme activity (~30% reduction in aminoacylation measured in patient fibroblasts; confirmed via yeast complementation growth-defect assay)
3. Reduced translational fidelity/capacity, **plus** an SARS1-specific non-canonical consequence: patient fibroblasts show a **cellular senescence phenotype** — reduced proliferation, abnormal morphology, increased senescence-associated beta-galactosidase staining, elevated phosphorylated histone H2AX (a DNA-damage-response marker), and markedly increased expression of senescence-associated secretory phenotype (SASP) genes (IL-6, p21, p16, p53)
4. This senescence-driving mechanism is described as **unique among known aminoacyl-tRNA synthetases** and represents a newly characterized pathway linking translational-machinery dysfunction to cellular aging/senescence programs, plausibly contributing to the progressive-then-stabilizing spastic paraparesis and CNS findings in this specific patient — distinct from the classic microcephaly-predominant biallelic phenotype ([PMID:36041817](https://pmc.ncbi.nlm.nih.gov/articles/PMC9691831/))

**Cellular processes involved:**
- Cytoplasmic mRNA translation (core aminoacylation step)
- Cellular senescence / SASP activation (de novo dominant-negative case)
- DNA damage response (elevated γH2AX)
- Possible selenoprotein synthesis impairment (via the Sec-tRNA charging role of SerRS), though this has not been directly demonstrated as pathogenic in NEDMAS

**Protein dysfunction:** Loss-of-function (reduced catalytic aminoacylation activity) is the primary mechanism for biallelic missense variants; the single de novo case is best characterized as **dominant-negative** (not simple gain-of-function toxicity, but interference with wild-type enzyme function in the obligate dimer).

**Cell types and biological processes (suggested ontology terms):**
- **GO:0006434** seryl-tRNA aminoacylation (molecular process directly disrupted)
- **GO:0006412** translation (downstream biological process impaired)
- **GO:0090398** cellular senescence (mechanism specific to the de novo dominant-negative case)
- **GO:0006974** DNA damage response (elevated γH2AX in senescent fibroblasts)
- **CL:0000057** fibroblast (primary patient-derived cell type used for functional studies)
- **CL:0000540** neuron (presumed primary affected cell type given CNS-predominant phenotype, though not directly assayed in these studies)
- **CL:0000187** myocyte / cardiac muscle cell (relevant to the cardiomyopathy phenotype in the Ravel et al. family)

**Tissue damage mechanisms:** Not characterized at the histopathological level in the retrieved literature (no biopsy/autopsy data reported); mechanism is inferred from functional/biochemical assays in patient fibroblasts and heterologous (yeast) complementation systems rather than direct tissue pathology.

**Molecular profiling:** No transcriptomic, proteomic, or metabolomic dataset specific to SARS1-NEDMAS patient tissue was identified in the retrieved sources beyond the targeted qPCR-level SASP gene expression analysis (IL-6, p21, p16, p53) described above.

---

## 7. Anatomical Structures Affected

- **Organ level (primary):** Central nervous system (brain — cerebrum and cerebellum), consistent with the microcephaly/ataxia/seizure triad
- **Organ level (secondary, variant-dependent):** Inner ear/cochlea (sensorineural deafness — Ravel et al. family); heart (cardiomyopathy — Ravel et al. family); skeletal muscle (weakness, spasticity)
- **Body systems involved:** Nervous system (primary), cardiovascular system (secondary, in loss-of-function severe phenotype), auditory system (secondary), musculoskeletal system (motor/spasticity findings)
- **Tissue/cell level:** Neurons and glial elements of cerebral cortex and cerebellum (inferred from atrophy on neuroimaging); cardiomyocytes; cochlear hair cells/auditory neurons (inferred, not directly biopsied); dermal fibroblasts (directly studied ex vivo in the functional characterization of the de novo variant)
- **Subcellular level:** Cytoplasm (site of SARS1 enzymatic activity — GO Cellular Component **GO:0005737** cytoplasm / more specifically **GO:0017101** aminoacyl-tRNA synthetase multienzyme complex); nucleus (site of γH2AX DNA damage marker accumulation in senescent cells, **GO:0005634**)
- **Localization (UBERON):** **UBERON:0000955** brain; **UBERON:0002037** cerebellum; **UBERON:0000956** cerebral cortex; **UBERON:0001690** ear / **UBERON:0001846** cochlea (deafness phenotype); **UBERON:0000948** heart (cardiomyopathy phenotype)
- **Lateralization:** Bilateral/symmetric involvement reported (bilateral cerebral and cerebellar atrophy in the Turkish cohort neuroimaging)

---

## 8. Temporal Development

- **Onset:** Infantile to early childhood for developmental delay and seizures; postnatal microcephaly (implying normal or near-normal head circumference at birth with subsequent deceleration, though this was not explicitly confirmed as congenital vs. postnatal across all cases in the retrieved sources — recommend verifying per-case in the primary papers before curating an `onset_category`)
- **Onset pattern:** Insidious/progressive for developmental delay; acute/episodic for fever-triggered decompensation and seizures
- **Progression:** Variable by genotype —
  - Biallelic missense (classic NEDMAS): chronic, relatively stable developmental impairment punctuated by acute febrile decompensation risk
  - De novo dominant-negative: spastic paraparesis **"worsened during childhood but later stabilized"** — a distinctive non-monotonic (progressive-then-plateauing) course
- **Disease course pattern:** Chronic with episodic acute crises (fever-triggered) in the severe loss-of-function subgroup; chronic-stable to chronic-progressive-then-stable in the dominant-negative case
- **Disease duration:** Lifelong/chronic; at least one reported case was fatal in childhood due to fever-triggered decompensation (Ravel et al. 2021)
- **Critical periods:** Febrile illness represents an identifiable window of acute vulnerability across multiple reported cases, suggesting a clinically actionable "critical period" for aggressive fever management/monitoring in affected individuals, though this has not been formalized into a published clinical protocol.

---

## 9. Inheritance and Population

- **Epidemiology:** No formal prevalence or incidence estimate exists; this is an ultra-rare disorder with fewer than ~15 individuals reported in the peer-reviewed literature across all publications identified (2017–2022+). No entry in large disease-registry/GBD-type databases was identified.
- **Inheritance pattern:** **Autosomal recessive** for the classic NEDMAS phenotype (all biallelic cases, occurring predominantly in consanguineous Iranian and Turkish families); **autosomal dominant, de novo** for the single reported spastic-paraplegia case with a dominant-negative mechanism.
- **Penetrance:** Presumed complete for the recessive form given consistent phenotype in all biallelic carriers reported to date, though the small sample size limits confidence.
- **Expressivity:** Clearly **variable** — phenotype ranges from moderate ID/ataxia (original Iranian family) to fatal fever-triggered decompensation with deafness/cardiomyopathy (Turkish family) to spastic paraplegia without microcephaly (de novo case) — indicating genotype-phenotype correlation by variant/mechanism rather than uniform expressivity.
- **Genetic anticipation:** Not reported/not applicable (no repeat-expansion mechanism).
- **Germline mosaicism:** Not specifically reported.
- **Founder effects:** Not established, though the recurrence of specific consanguineous-family variants (e.g., p.Thr399Met recurring across multiple unrelated Turkish families) raises the possibility of a Turkish population founder variant — this warrants further population-genetic study but was not explicitly confirmed as a founder effect in the retrieved sources.
- **Consanguinity role:** Prominent — most reported pedigrees (Iranian families in Musante et al. 2017; Turkish families in Ravel et al. 2021 and the 2022 cohort) are consanguineous, consistent with autosomal recessive transmission of rare alleles.
- **Carrier frequency:** Not established in population databases.
- **Affected populations:** Reported cases cluster in **Iranian** and **Turkish** consanguineous families; no data on other ethnic/geographic groups, likely reflecting ascertainment bias toward populations with higher consanguinity rates and active clinical genetics/exome-sequencing research programs rather than true population restriction.
- **Sex ratio:** Not reported as skewed; autosomal recessive/dominant inheritance would not a priori predict a sex bias, and no such bias was noted in the retrieved case descriptions.
- **Age distribution:** Reported cases span infancy through early adolescence (the de novo case patient is described as an "early adolescent male" at time of report).

---

## 10. Diagnostics

- **Genetic testing (primary diagnostic modality):** Diagnosis in all reported cases was established via **whole-exome sequencing (WES)**, either trio-based (de novo case, and Musante et al. 2017 original families) or proband/family-based (Turkish cohort, 2022). This reflects current clinical practice for undiagnosed neurodevelopmental disorders generally — WES/WGS with subsequent Sanger confirmation and segregation analysis in the family.
- **Single-gene testing:** Feasible via Sanger sequencing once a familial variant is known (e.g., for prenatal or carrier testing in a family with a previously identified proband).
- **Gene panels:** *SARS1* would reasonably be included in comprehensive intellectual-disability/microcephaly/epilepsy gene panels, though no specific commercial panel was identified in the retrieved sources; the NIH Genetic Testing Registry (GTR) lists *SARS1* as a testable gene ([GTR gene 6301](https://www.ncbi.nlm.nih.gov/gtr/genes/6301/)).
- **Chromosomal microarray/karyotype/FISH:** Not applicable as primary diagnostic tools (disease is caused by point variants/small indels, not large structural rearrangements), though these are typically part of the standard diagnostic workup to exclude other causes of ID/microcephaly before or alongside sequencing.
- **Imaging:** **Brain MRI** is diagnostically informative — bilateral cerebral and cerebellar atrophy was reported in the Turkish cohort; the de novo case showed subtle, non-progressive punctiform frontal subcortical white-matter hyperintensities, a distinguishing (milder) imaging pattern.
- **Electrophysiology:** Visual evoked potentials showed increased latency in the de novo case, suggesting a role for VEP/electrophysiological testing in characterizing CNS involvement; EEG would be standard given the seizure phenotype (not explicitly detailed in retrieved abstracts).
- **Functional/biochemical testing:** Not part of routine clinical diagnosis; aminoacylation activity assays and yeast complementation studies were **research-level functional validation** tools used to confirm variant pathogenicity in the de novo case, not standard-of-care diagnostics.
- **Differential diagnosis:** Other autosomal recessive/dominant aminoacyl-tRNA synthetase disorders (e.g., *WARS1*-related recessive microcephaly — a close mimic per Bögershausen et al. 2022 — as well as *RARS2*-related pontocerebellar hypoplasia type 6, *KARS1*-, *VARS1*-, *NARS1*-related neurodevelopmental disorders), other causes of primary microcephaly with intellectual disability and ataxia, and mitochondrial encephalopathies (given phenotypic overlap with fever-triggered decompensation) should be considered and excluded.
- **Screening:** No newborn screening or population carrier-screening program exists for this ultra-rare condition.

---

## 11. Outcome/Prognosis

- **Survival/mortality:** At least one reported case (Ravel et al. 2021 family) was **fatal** due to fever-triggered metabolic/neurological decompensation, establishing that the loss-of-function/severe end of the phenotypic spectrum carries meaningful mortality risk, particularly around febrile illness. No formal survival statistics (5-year/10-year) exist given the tiny reported cohort.
- **Morbidity/function:** Chronic, lifelong intellectual disability, ataxia, and (in some cases) spasticity impose significant functional impairment; no standardized disability or QOL outcome measures have been published for this condition.
- **Disease course:** As above — chronic-stable to chronic-progressive-then-stabilizing (de novo case), or chronic-with-acute-crisis-risk (loss-of-function biallelic cases).
- **Complications:** Fever-triggered acute decompensation (potentially fatal); cardiomyopathy (loss-of-function severe phenotype); progressive spasticity (de novo case, though noted to stabilize later in that individual).
- **Prognostic factors:** Variant type/mechanism appears to be the dominant prognostic factor identified to date — biallelic partial-loss-of-function missense variants with organ involvement (deafness, cardiomyopathy) carry the most severe/potentially fatal course; the de novo dominant-negative variant produced a phenotype without microcephaly and with a plateauing motor course. No molecular biomarker has been established as a prognostic tool.

---

## 12. Treatment

**No SARS1/NEDMAS-specific approved therapy exists.** Management reported in the literature is supportive/symptomatic:

- **Supportive care:** Management of seizures (standard antiepileptic approaches, implied but not itemized by specific agent in the retrieved abstracts), and — critically — **aggressive management of febrile illness** to prevent metabolic/neurological decompensation, given the clear fever-precipitant pattern documented across multiple families. This should be considered a de facto tertiary-prevention/critical-management principle for this disorder even though no formal clinical guideline was identified.
- **Rehabilitative therapies:** Physical therapy, occupational therapy, and speech therapy would be standard supportive interventions for the motor (ataxia, spasticity) and speech-delay phenotypes, consistent with general neurodevelopmental disorder management, though not specifically itemized in the retrieved case reports.
  - Suggested NCIT terms: **NCIT:C15302** (Physical Therapy), **NCIT:C159273** (Speech Therapy), **NCIT:C121351** (Occupational Therapy)
- **Cardiac management:** Cardiology follow-up/management would be indicated for the subset of patients with cardiomyopathy (Ravel et al. family) — **NCIT:C49236** (Therapeutic Procedure)/standard heart-failure management, not itemized specifically.
- **Audiology:** Hearing evaluation and intervention (hearing aids/cochlear implant as indicated) for the sensorineural deafness subgroup.
- **Genetic counseling:** Indicated given autosomal recessive inheritance in consanguineous families, for recurrence-risk counseling and potential prenatal/preimplantation testing in subsequent pregnancies. **NCIT:C15240** (Genetic Counseling).
- **Experimental/investigational therapy:** No SARS1-specific gene therapy, RNA-based therapy, or targeted molecular therapy has reached clinical trials; no ClinicalTrials.gov entries specific to SARS1-NEDMAS were identified in the retrieved search results. Broader aaRS-disorder research literature discusses conceptual therapeutic strategies applicable to this gene family in principle — amino acid supplementation, tRNA overexpression, modulation of integrated stress response, and genome editing — but these remain investigational/preclinical concepts rather than SARS1-specific interventions ([PMC11611227](https://pmc.ncbi.nlm.nih.gov/articles/PMC11611227/)).

---

## 13. Prevention

- **Primary prevention:** Not applicable in the traditional sense (monogenic disorder); the only actionable primary-prevention-adjacent measure is **genetic counseling and carrier/prenatal testing** in families with a known pathogenic variant, particularly relevant given the strong consanguinity pattern in reported pedigrees.
- **Secondary prevention:** Early diagnosis via WES in infants/children presenting with unexplained developmental delay, microcephaly, ataxia, and seizures enables anticipatory guidance (e.g., heightened vigilance and aggressive antipyretic/supportive management during febrile illness) that may mitigate the risk of severe/fatal decompensation identified in the Ravel et al. family.
- **Tertiary prevention:** Aggressive, proactive management of febrile illness (the clearest identified modifiable risk factor for acute decompensation) constitutes the most concrete tertiary-prevention strategy supported by the literature, though it has not been codified into a formal published clinical protocol or guideline.
- **Screening/genetic counseling:** Carrier screening is not population-based (given rarity) but should be offered to at-risk consanguineous families with a known proband; preimplantation genetic diagnosis (PGD) would be a reasonable option for families with an identified pathogenic variant, consistent with standard practice for autosomal recessive Mendelian disorders, though not explicitly documented as having been used in these specific families.

---

## 14. Other Species / Natural Disease

- **Taxonomy/model relevance:** **Zebrafish (*Danio rerio*, NCBITaxon:7955)** is the primary non-human model system referenced in the literature for *sars*/SARS1 biology. Fukui et al. (2009) and Herzog et al. (2009) identified zebrafish *sars* mutants with **abnormal vascular development**, and notably found this vascular role to be **independent of the canonical aminoacylation function** — an important non-canonical (moonlighting) function of this synthetase that is distinct from, but potentially mechanistically relevant to, its neurodevelopmental disease role in humans.
- **Orthologous gene:** Mouse ortholog *Sars1* (NCBI Gene ID 20226, *Mus musculus*); no *Sars1* knockout mouse model with a reported neurodevelopmental phenotype was identified in the retrieved search results — this appears to be a gap in the current model-organism literature for this specific gene (in contrast to related aaRS genes like *Kars1*, *Vars1*, and *Wars1*, for which zebrafish knockouts recapitulating brain/eye phenotypes have been more thoroughly characterized).
- **Natural disease in companion/veterinary species:** No OMIA entry or veterinary case series for naturally occurring SARS1-related disease in animals was identified.
- **Comparative biology:** The broader aaRS gene family shows a consistent pattern across paralogs (KARS1, VARS1, WARS1, NARS1, SARS1) of zebrafish knockouts preferentially affecting **brain and eye development**, mechanistically consistent with the microcephaly/CNS phenotype seen in human patients and supporting cross-paralog conservation of a dosage-sensitive requirement for aaRS activity during neurodevelopment.
- **Zoonotic potential/transmission:** Not applicable (non-infectious, monogenic disorder).

---

## 15. Model Organisms

- **Zebrafish (*Danio rerio*):** The most relevant existing model, though the published *sars* zebrafish mutants (Fukui 2009, Herzog 2009) were characterized for a **vascular development phenotype**, not the human neurodevelopmental (microcephaly/ataxia/seizure) phenotype — representing a translational gap. A zebrafish knock-in model of a specific human NEDMAS-causing missense variant (analogous to the KARS1 zebrafish knockout work cited for other aaRS disorders) does not appear to have been published yet for SARS1, and would be a natural follow-on model to more directly recapitulate and mechanistically dissect the human CNS phenotype.
- **Yeast complementation system:** Used as a **functional/heterologous validation model** (not a disease model per se) to demonstrate the dominant-negative growth-defect effect of the de novo splice variant when co-expressed with wild-type SARS1 — this represents an important functional-genomics tool for variant classification in this gene going forward ([PMID:36041817](https://pmc.ncbi.nlm.nih.gov/articles/PMC9691831/)).
- **Patient-derived fibroblasts:** The primary "model system" used across the functional characterization literature — patient dermal fibroblasts were used to measure aminoacylation activity (~30% reduction in the de novo case) and to characterize the cellular senescence phenotype (β-galactosidase staining, γH2AX, SASP gene expression). No iPSC-derived neuronal model specific to SARS1-NEDMAS was identified in the retrieved sources — this represents a clear opportunity for future model development given the CNS-predominant human phenotype.
- **Model limitations:** Current models (zebrafish vascular mutants, yeast complementation, patient fibroblasts) each capture only a partial aspect of the human disease — none directly recapitulates the CNS-specific microcephaly/ataxia/seizure phenotype in vivo, representing a significant translational gap for mechanistic and preclinical therapeutic studies in this gene.

---

## Summary of Key Ontology Term Suggestions for Curation

| Category | Suggested terms |
|---|---|
| Gene | *SARS1*, hgnc:10537 |
| Disease | OMIM:617709 (NEDMAS); MONDO ID to be confirmed via OAK lookup |
| Phenotypes (HP) | HP:0001263 (Global developmental delay), HP:0001249 (Intellectual disability), HP:0000252 (Microcephaly), HP:0001250 (Seizure), HP:0001251 (Ataxia), HP:0001324 (Muscle weakness), HP:0008936 (Severe muscular hypotonia), HP:0002059 (Cerebral atrophy), HP:0001272 (Cerebellar atrophy), HP:0000407 (Sensorineural hearing loss), HP:0001638 (Cardiomyopathy), HP:0001260 (Spasticity) |
| Biological processes (GO) | GO:0006434 (seryl-tRNA aminoacylation), GO:0006412 (translation), GO:0090398 (cellular senescence), GO:0006974 (DNA damage response) |
| Cell types (CL) | CL:0000057 (fibroblast), CL:0000540 (neuron), CL:0000187 (muscle cell) |
| Anatomy (UBERON) | UBERON:0000955 (brain), UBERON:0002037 (cerebellum), UBERON:0001846 (cochlea), UBERON:0000948 (heart) |
| Treatment (NCIT) | NCIT:C15302 (Physical Therapy), NCIT:C159273 (Speech Therapy), NCIT:C15240 (Genetic Counseling) |

---

## Key Citations

1. Musante L, et al. "Mutations of the aminoacyl-tRNA-synthetases SARS and WARS2 are implicated in the etiology of autosomal recessive intellectual disability." *Hum Mutat.* 2017. [PMID:28236339](https://www.ncbi.nlm.nih.gov/pubmed/28236339)
2. Ravel JM, et al. "A bi-allelic loss-of-function SARS1 variant in children with neurodevelopmental delay, deafness, cardiomyopathy, and decompensation during fever." *Hum Mutat.* 2021 Dec;42(12):1576-1583. [PMID:34570399](https://pubmed.ncbi.nlm.nih.gov/34570399/)
3. [Authors unlisted in retrieved abstract]. "Loss of seryl-tRNA synthetase (SARS1) causes complex spastic paraplegia and cellular senescence." 2022. [PMID:36041817](https://pmc.ncbi.nlm.nih.gov/articles/PMC9691831/)
4. Bögershausen N, Krawczyk HE, Jamra RA, et al. "WARS1 and SARS1: Two tRNA synthetases implicated in autosomal recessive microcephaly." *Hum Mutat.* 2022 Oct;43(10):1454-1471. [Wiley DOI](https://onlinelibrary.wiley.com/doi/full/10.1002/humu.24430)
5. [Turkish cohort authors unlisted in retrieved abstract]. "Neurodevelopmental disorder with microcephaly, ataxia, and seizures syndrome: expansion of the clinical spectrum." *Clin Dysmorphol.* 2022 Oct;31(4):167-173. [PMID:36004946](https://pubmed.ncbi.nlm.nih.gov/36004946/)
6. OMIM #617709 — Neurodevelopmental Disorder with Microcephaly, Ataxia, and Seizures (NEDMAS). [omim.org/entry/617709](https://omim.org/entry/617709)
7. OMIM *607529 — Seryl-tRNA Synthetase 1; SARS1. [omim.org/entry/607529](https://omim.org/entry/607529)
8. Review: "Aminoacyl-tRNA synthetase defects in neurological diseases." [PMC11611227](https://pmc.ncbi.nlm.nih.gov/articles/PMC11611227/)

**Note on gaps requiring direct primary-source verification before KB curation:** Several full-text primary sources (Ravel et al. 2021, Bögershausen et al. 2022) were paywalled and only accessible via abstract/secondary summary; exact quoted snippets for evidence items should be re-verified against the cached PubMed abstracts via `just fetch-reference` before use, per this repository's evidence-integrity SOP. The MONDO ID and specific author lists for two papers (PMID:36041817 and PMID:36004946 full author bylines) should also be confirmed directly against PubMed/MONDO before finalizing the KB entry.