---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-30T23:40:11.813025'
end_time: '2026-07-30T23:44:56.870803'
duration_seconds: 285.06
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Spinocerebellar Ataxia 43
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
  web_search_requests: 16
  num_turns: 23
  total_cost_usd: 1.7974728999999998
  session_id: 6191bdd5-f8af-53be-a517-35c785311542
  stop_reason: end_turn
citation_count: 18
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spinocerebellar Ataxia 43
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spinocerebellar Ataxia 43** covering all of the
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

# Spinocerebellar Ataxia 43 (SCA43) — Comprehensive Research Report

## 1. Disease Information

**Overview:** Spinocerebellar ataxia 43 (SCA43) is a rare, autosomal dominant, adult/late-onset, slowly progressive neurodegenerative disorder combining cerebellar ataxia with a peripheral (predominantly motor axonal) polyneuropathy. It was first described in 2016 by Depondt and colleagues in a large five-generation Belgian family, who identified a heterozygous missense mutation in the **MME** gene (encoding neprilysin/neutral endopeptidase) as the cause ([Depondt et al. 2016, *Neurology Genetics*, PMID: 27583304](https://pubmed.ncbi.nlm.nih.gov/27583304/); [PMC4991603](https://pmc.ncbi.nlm.nih.gov/articles/PMC4991603)). SCA43 is classified within the "ADCA type I" group of dominant ataxias — i.e., cerebellar ataxia plus additional neurological features (here, peripheral neuropathy) rather than pure cerebellar ataxia.

**Key identifiers:**
- **OMIM:** #617018 (SPINOCEREBELLAR ATAXIA 43; SCA43) — [omim.org/entry/617018](https://www.omim.org/entry/617018)
- **Gene locus (OMIM):** *MME, #120520 (MEMBRANE METALLOENDOPEPTIDASE), chromosome 3q25.2
- **MONDO:** MONDO:0014867 (per NCBI MedGen cross-reference)
- **MedGen:** C4310763
- **Orphanet:** ORPHA:497764 (Spinocerebellar ataxia type 43)
- **GARD (NIH rare disease):** disease ID 17917 — [rarediseases.info.nih.gov/diseases/17917](https://rarediseases.info.nih.gov/diseases/17917/spinocerebellar-ataxia-43)
- **Allelic disorder:** CMT2T — Charcot-Marie-Tooth disease, axonal, type 2T, OMIM #617017 (autosomal recessive, biallelic *MME* mutation, no cerebellar involvement)

**Synonyms:** SCA43; ADCA with neuropathy (MME-related); MME-related ataxia.

**Evidence source note:** The founding evidence base for SCA43 is a single deeply phenotyped extended pedigree (individual-patient/family-level clinical and genetic data), subsequently supplemented by a small number of independent case reports (aggregated, disease-level literature is sparse — this is a very recently described, ultra-rare entity).

---

## 2. Etiology

**Disease causal factor:** SCA43 is caused by heterozygous (dominant), gain-of-function/dominant-negative-acting missense (and at least one nonsense) variants in **MME** (membrane metalloendopeptidase; neprilysin, NEP), a zinc-dependent M13-family metalloprotease.

**Genetic risk factors:**
- The founding pathogenic variant is **NM_007289.4(MME):c.428G>A, p.(Cys143Tyr)** (also written C143Y), identified by linkage analysis + whole-exome sequencing in the Belgian kindred and cosegregating perfectly with disease across 24 of 28 genotyped family members (PMID: 27583304).
- A second, distinct pathogenic variant reported in ClinVar is **NM_007289.4(MME):c.1342C>T, p.(Arg448Ter)** — a nonsense/truncating variant classified pathogenic for SCA43 ([ClinVar RCV001196533](https://www.ncbi.nlm.nih.gov/clinvar/RCV001196533/)).
- No large case-control allele-frequency or GWAS susceptibility-locus data exist (this is a monogenic Mendelian disorder), but the C143Y variant was confirmed **absent from ExAC (60,706 unrelated individuals)** and from 96 additional unrelated dominant-ataxia probands screened by the discovery group — supporting pathogenicity via absence from population databases (PMID: 27583304).
- **In silico pathogenicity of C143Y:** SIFT = 0 (damaging), PolyPhen-2 = 1.000 (probably damaging), PROVEAN = −10.185 (deleterious) (PMID: 27583304).

**Environmental/lifestyle risk factors:** None established; SCA43 is a purely monogenic disorder with no reported environmental, infectious, or lifestyle modifiers of onset or severity in the literature to date.

**Protective factors:** None reported (genetic or environmental).

**Gene-environment interaction:** Not described; the extreme rarity of the disorder (essentially a handful of families/cases worldwide) has precluded any GxE study.

**Modifier genes:** None formally established, though intrafamilial variability in the founding pedigree (see §3/§8) suggests unidentified genetic or stochastic modifiers.

---

## 3. Phenotypes

### Core clinical picture (from the Belgian founder family, PMID: 27583304)
Of 7 living affected individuals (ages of onset 42–68 years), **6 of 7 had cerebellar ataxia** and **all but one had sensorimotor axonal polyneuropathy**; one individual presented with polyneuropathy alone, without cerebellar signs — indicating incomplete/variable penetrance of the cerebellar component even within one kindred.

**Cerebellar/neurological phenotypes:**
| Phenotype | HPO suggestion | Notes |
|---|---|---|
| Gait ataxia | HP:0002066 (Gait ataxia) | Core presenting feature; "ataxic gait with difficulties in turning" |
| Limb ataxia | HP:0002070 (Limb ataxia) | Mild upper and lower limb ataxia in proband |
| Dysarthria | HP:0001260 (Dysarthria) | Reported cerebellar sign |
| Nystagmus | HP:0000639 (Nystagmus) | Reported cerebellar sign |
| Hypometric saccades | HP:0000571 or HP:0007874 (Saccadic hypometria) | Oculomotor cerebellar sign |
| Tremor | HP:0001337 (Tremor) | Reported cerebellar/movement sign; also reported as a presenting feature preceding ataxia in a later case (postural tremor; Prashanth, *Cerebellum* 2026) |
| Cerebellar vermis atrophy (MRI) | HP:0006855 (Cerebellar vermis atrophy) | "Moderate atrophy of the cerebellar vermis" on brain MRI |

**Peripheral neuropathy phenotypes:**
| Phenotype | HPO suggestion | Notes |
|---|---|---|
| Distal muscle weakness/atrophy | HP:0003693 / HP:0007340 (Distal muscle weakness/atrophy) | "Mild distal lower limb atrophy" |
| Pes cavus | HP:0001761 (Pes cavus) | Present in proband |
| Areflexia/hyporeflexia (lower limb) | HP:0001284 (Areflexia); HP:0001596/HP:0001265 | "Absent Achilles tendon reflexes," "bilaterally weak knee tendon reflexes" |
| Axonal sensorimotor polyneuropathy | HP:0003477 (Axonal neuropathy) | EMG: "progressive, severe motor neuropathy in the lower limbs with significantly increased F-response latency but preserved sensory responses" in most patients; sural nerve biopsy in one patient showed axonal CMT2-type pathology |
| Lower limb pain | HP:0012531 (Pain) / HP:0009830-adjacent | Present in some patients |
| Distal sensory impairment | HP:0003390 (Impaired distal vibration sensation) or general HP:0003676 | A minority had distal sensory loss (later case reports emphasize vibration loss) |

**Skeletal/other:**
- **Pectus carinatum** — "not omnipresent" but noted as a **distinctive clinical feature** of the family (no precise HPO term routinely used for this SCA context but HP:0000768 Pectus carinatum applies).
- **Cognitive status:** In the founding family, **no cognitive complaints were reported**, though formal neuropsychological testing was not performed — an important negative given NEP's role in Aβ clearance (see §6). This contrasts with a later sporadic case (below).

**Extended/atypical phenotypes reported in subsequent literature (expanding the phenotypic spectrum):**
- A **parkinsonian-plus presentation** has been described as an SCA43 phenocopy pitfall — "SCA Variant Masquerading as a Parkinsonian-plus Syndrome" (Vijaywargiya et al., abstract, *Neurology* 2025, DOI 10.1212/WNL.0000000000211725), underscoring diagnostic overlap with parkinsonism.
- A sporadic case (Journal of the Neurological Sciences, 2023) described a **40-year-old man** with ataxia, dysarthria, fasciculations, **anterior horn cell involvement** (wasting/weakness of small hand muscles, brisk reflexes, lower-limb spasticity, upper-limb rigidity), and **mild cognitive dysfunction (recent memory)** — explicitly noted as a rare/atypical association not seen in the founder family.
- A 2026 case report (Prashanth, *The Cerebellum*, DOI 10.1007/s12311-026-02023-0) described a **63-year-old woman** with progressive **orobuccolingual dystonia** and **choreiform movements of the right hand** preceding gait ataxia by several years, plus postural tremor and distal lower-limb vibratory sensory loss — expanding SCA43 into the hyperkinetic-movement-disorder spectrum (dystonia/chorea), previously undocumented for this gene.

**Quality-of-life impact:** No disease-specific EQ-5D/SF-36 data exist for SCA43 specifically; given the slowly progressive gait ataxia and motor polyneuropathy with lower-limb amyotrophy, the expected functional impact (extrapolated from general ADCA-I literature) includes progressive gait/balance impairment, falls risk, need for mobility aids, and functional hand/foot impairment from motor neuropathy — but this has not been formally measured in SCA43 patients.

---

## 4. Genetic/Molecular Information

**Causal gene:** *MME* (HGNC:7154), encoding neprilysin (NEP; also called neutral endopeptidase, CD10, CALLA — common acute lymphoblastic leukemia antigen). Gene comprises 23 exons on chromosome 3q25.2.

**Pathogenic variants for SCA43:**
1. **c.428G>A, p.(Cys143Tyr)** — heterozygous missense; **variant type:** missense; **classification:** pathogenic (cosegregation, absence from ExAC, strong in silico predictions); **origin:** germline; **functional consequence:** disrupts a highly conserved disulfide bridge (Cys143–Cys411) within the N-terminal peptidase M13 domain — one of 10 conserved cysteines among related M13-family neutral endopeptidases (NEP, ECE, KELL, PEX). Proposed as **dominant-negative or gain-of-function-like** rather than simple haploinsufficiency (see mechanism, §6).
2. **c.1342C>T, p.(Arg448Ter)** — heterozygous nonsense/truncating variant, classified pathogenic in ClinVar for SCA43 ([RCV001196533](https://www.ncbi.nlm.nih.gov/clinvar/RCV001196533/)).

**Gene identifiers:** HGNC gene symbol MME; NCBI Gene ID 4311; UniProt P08473 (human neprilysin); Ensembl ENSG00000196549.

**Allele frequency:** The C143Y variant is absent from gnomAD/ExAC population databases (0 alleles among 60,706 individuals in the original ExAC analysis), consistent with a rare, highly penetrant dominant variant.

**Somatic vs. germline:** Germline in all reported cases (Mendelian dominant transmission across generations in the founder pedigree).

**Functional consequence / mechanism of protein dysfunction:** Loss of the Cys143–Cys411 disulfide bond is predicted to destabilize NEP's extracellular peptidase M13 catalytic domain. Critically, this is **not** modeled as simple loss-of-function/haploinsufficiency, because **biallelic (homozygous/compound heterozygous) loss-of-function MME mutations cause a recessive, purely peripheral neuropathy (CMT2T) without cerebellar involvement** — heterozygous carriers of null CMT2T alleles are unaffected. This apparent paradox led the discovery authors to propose that the dominant C143Y (and other dominant) variants act via a **distinct, possibly dominant-negative or altered-substrate-specificity mechanism** (e.g., competing with wild-type NEP for substrate binding without normal catalytic turnover) rather than through simple reduced enzyme dosage (PMID: 27583304).

**Modifier genes:** None established.

**Epigenetic information:** Not reported for SCA43.

**Chromosomal abnormalities:** None reported; SCA43 is caused by point mutations, not structural chromosomal rearrangements.

**Allelic disorders (important for differential/genetic counseling):**
- **CMT2T** (Charcot-Marie-Tooth disease, axonal, type 2T; OMIM #617017) — autosomal recessive, biallelic (homozygous or compound heterozygous) *MME* mutations causing slowly progressive sensorimotor axonal polyneuropathy **without cerebellar ataxia**. First described by Higuchi et al. 2016 (*Annals of Neurology*, DOI 10.1002/ana.24612). *MME* mutations are reported as **the most frequent cause of autosomal recessive axonal CMT in the Japanese population**. Both mono- and biallelic *MME* mutations can cause late-onset axonal peripheral neuropathy; biallelic mutations are associated with more rapid progression.

---

## 5. Environmental Information

No environmental toxin, occupational exposure, radiation, infectious agent, or lifestyle factor (smoking, diet, alcohol) has been implicated in SCA43 causation or modification — consistent with its purely monogenic, highly penetrant dominant inheritance. No infectious trigger is described.

---

## 6. Mechanism / Pathophysiology

**Protein/pathway biology (normal NEP function):** Neprilysin (NEP) is a type II integral membrane, **zinc-dependent metalloendopeptidase** of the **M13 peptidase family** (EC 3.4.24.11), with a short N-terminal cytoplasmic domain, a single transmembrane helix, and a large C-terminal extracellular catalytic portion composed of two major α-helical (peptidase M13) domains (PMID: 27583304). NEP cleaves peptide bonds on the amino side of hydrophobic residues and has broad substrate specificity, acting on numerous neuropeptides: **glucagon, enkephalins, cholecystokinin, neuropeptide Y, substance P, somatostatin, neurotensin, oxytocin, prodynorphin, and bradykinin**, as well as the **amyloid-beta (Aβ) peptides** (its best-characterized role, as one of the principal Aβ-degrading enzymes in brain).

**Expression pattern:**
- CNS: predominantly neuronal, concentrated in **axons and synaptic terminals**.
- PNS: predominantly in **Schwann cells**, though NEP protein is also transported along peripheral (sciatic) nerve axons.

**Proposed causal chain in SCA43:**
1. Dominant *MME* missense variant (e.g., p.C143Y) disrupts a conserved disulfide bond (Cys143–Cys411) in the extracellular M13 peptidase domain.
2. Because **biallelic loss-of-function** *MME* variants cause only peripheral neuropathy (CMT2T) with **no cerebellar phenotype**, simple haploinsufficiency of catalytic NEP activity cannot fully explain the dominant SCA43 phenotype — the mutant protein is hypothesized to exert a **dominant-negative or altered-function effect**, e.g., competing with wild-type NEP monomers/dimers for substrate binding while lacking normal catalytic turnover.
3. **Leading substrate hypothesis:** prodynorphin (precursor of the opioid neuropeptides α-neoendorphin, dynorphin A, and dynorphin B) is a known NEP substrate, and separately, mutations in the **prodynorphin gene (PDYN)** cause a different dominant ataxia, **SCA23**. The SCA43 discovery authors hypothesize that mutant NEP (p.C143Y) may have an altered, possibly toxic, effect specifically on dynorphin-peptide processing, "possibly competing with wild-type NEP for substrate affinity and catalytic activity, which eventually triggers cerebellar degeneration" (direct quote, PMID: 27583304).
4. This altered neuropeptide processing in **cerebellar Purkinje cell / cerebellar circuitry** (site of the observed vermis atrophy) is proposed to drive **cerebellar degeneration**, while a **parallel or independent toxic gain-of-function effect in axons and Schwann cells** of peripheral nerves drives the **axonal (Wallerian-type/CMT2-pattern) motor-predominant neuropathy**, confirmed histologically by sural nerve biopsy showing axonal CMT2 pathology.

**Amyloid-beta connection (largely excluded as a disease mechanism here):** Despite NEP's prominent role as an Aβ-degrading enzyme (relevant to Alzheimer disease pathobiology and a rationale for genetic studies of *MME* in AD risk), **no cognitive impairment/Alzheimer-like phenotype was observed** in the SCA43 founder family, nor in Japanese CMT2 patients with biallelic *MME* mutations — leading the authors to state that "NEP deficiency does not lead to the development of AD" in this context, arguing against Aβ accumulation as the primary SCA43 mechanism (though one later, atypical sporadic SCA43 case did show mild cognitive dysfunction — see §3).

**Cell types implicated (Cell Ontology suggestions):**
- Cerebellar Purkinje cells (CL:0000121) — presumptive site of cerebellar degeneration (vermis atrophy).
- Peripheral motor neurons / lower motor neuron axons (CL:0000100 neuron, or CL:0011103 sympathetic/motor neuron as relevant) — axonal degeneration.
- Schwann cells (CL:0002573 or CL:0000381) — principal peripheral site of normal NEP expression; implicated in the peripheral neuropathy arm.

**Biological process (GO) suggestions:**
- GO:0006508 proteolysis (general NEP catalytic activity)
- GO:0004222 metalloendopeptidase activity (molecular function)
- GO:0006509 membrane protein ectodomain proteolysis
- GO:0097242 amyloid-beta clearance
- GO:0007218 neuropeptide signaling pathway (substrate processing, e.g., dynorphin/opioid peptide catabolism — GO:0035812 negative regulation of renal sodium excretion is unrelated; more precisely GO:0090277 positive regulation of peptide hormone secretion is not ideal — best generic terms are GO:0006518 peptide metabolic process and GO:0007218 neuropeptide signaling pathway)
- GO:0007049/GO:0008219 not directly implicated; no clear apoptosis/cell-death GO evidence reported specifically for SCA43 mechanism (inferred, not shown).

**Molecular profiling / omics:** No transcriptomic, proteomic, metabolomic, or single-cell datasets specific to SCA43 patient tissue have been published; the field currently rests entirely on clinical-genetic characterization plus general NEP biochemistry extrapolated from other contexts (Alzheimer disease research, CMT2T).

**Tissue damage mechanism:** Best characterized as **length-dependent axonal degeneration** in peripheral nerve (consistent with CMT2-pattern EMG/biopsy findings) combined with **cerebellar (vermis) atrophy** on imaging, consistent with a **neurodegenerative** rather than inflammatory or vascular process.

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Central nervous system — cerebellum (vermis) — UBERON:0002037 (cerebellum); UBERON:0004720 (cerebellar vermis, if available) or more general UBERON term for cerebellar vermis.
- **Primary:** Peripheral nervous system — peripheral (particularly lower-limb) motor and sensory nerves — UBERON:0000010 (peripheral nervous system); UBERON:0001511 (sciatic nerve) or general UBERON:0002211 (peripheral nerve).
- **Secondary:** Skeletal system — anterior chest wall deformity (pectus carinatum) — UBERON:0001911 (sternum)/thoracic skeleton.
- **Body systems involved:** Nervous system (central + peripheral); musculoskeletal system (secondary, distal muscle atrophy, pes cavus, pectus carinatum).

**Tissue/cell level:**
- Cerebellar cortex — Purkinje cell layer implicated by degeneration/atrophy pattern (not directly biopsied in humans; inferred from imaging).
- Peripheral nerve axons (motor > sensory) and myelinating Schwann cells — directly demonstrated by sural nerve biopsy (axonal CMT2-type pathology) in the founder family.
- Skeletal muscle — secondary distal denervation atrophy (small hand/lower-limb muscles).

**Subcellular level:**
- NEP is a plasma-membrane ectoenzyme (type II integral membrane protein) with its catalytic domain facing the extracellular space — GO:0005886 (plasma membrane), GO:0009986 (cell surface), GO:0016021 (integral component of membrane).
- Within neurons, NEP localizes to axonal and synaptic-terminal membranes (GO:0043679 axon terminus / GO:0030424 axon; GO:0045202 synapse).

**Localization/lateralization:** Bilateral, symmetric involvement in both the cerebellar (vermis, midline structure) and peripheral neuropathy components (lower limbs > upper limbs, length-dependent, bilateral).

---

## 8. Temporal Development

**Onset:** Adult-onset, ranging from **age 42 to 68 years** in the founding pedigree (proband's initial symptoms at age 58; diagnosed at 69). This places SCA43 among the later-onset dominant ataxias. Onset pattern is **insidious/chronic**, not acute or subacute.

**Progression:** **Slowly progressive** — consistent across all literature descriptions ("slowly progressive neurologic disorder," OMIM #617018). No formal staging system exists specific to SCA43. Disease course is chronic and lifelong (neurodegenerative, non-remitting), with gradual accrual of both cerebellar and peripheral neuropathic deficits over years to decades.

**Patterns:**
- **Intrafamilial variability:** within the same founder pedigree, one affected individual had **isolated peripheral neuropathy without cerebellar ataxia**, demonstrating incomplete penetrance/expressivity of the ataxia component even among carriers of the identical C143Y variant.
- Some later-reported cases show **atypical or unusual sequences of symptom emergence** — e.g., a hyperkinetic movement disorder (dystonia, chorea, tremor) preceding classic gait ataxia by several years in one 2026 case report — indicating broader phenotypic and temporal heterogeneity than initially appreciated.
- No spontaneous remission has been described; this is a neurodegenerative, progressive disorder.
- No defined "critical period" or treatment window has been established, given the very limited natural-history data.

---

## 9. Inheritance and Population

**Epidemiology:** SCA43 is an **extremely rare, essentially "cases in literature"-level** disorder — to date, described in one large multigenerational Belgian family (7 living affected members across generations) plus a small number of subsequently reported sporadic/atypical cases (parkinsonian-plus phenocopy case; anterior-horn-cell/cognitive-change case; dystonia/chorea-predominant case). No formal prevalence or incidence estimate exists; it should be considered **prevalence_class: NOT_YET_DOCUMENTED / ULTRA_RARE** in dismech terms. For context, autosomal dominant cerebellar ataxias as a group have an estimated overall prevalence of roughly **1.6–2.7 per 100,000** in European cohorts (e.g., Cantabria, Spain: 1.6/100,000; general dominant ataxia estimates 2–7/100,000), but SCA43 itself represents a vanishingly small fraction of that total given its single-family origin.

**Inheritance pattern:** **Autosomal dominant** (HP:0000006). The allelic disorder CMT2T is **autosomal recessive** (HP:0000007) — an important genetic-counseling distinction, since *MME* is one of the rare genes producing genuinely different, non-overlapping phenotypes depending on zygosity (heterozygous dominant missense/nonsense → SCA43 with cerebellar+peripheral disease; biallelic loss-of-function → CMT2T, peripheral-only disease).

**Penetrance:** Appears **high but not complete/uniform for the cerebellar component** — the founder pedigree included a mutation carrier with neuropathy but no ataxia, suggesting age-dependent or incomplete penetrance for the cerebellar phenotype specifically, while the peripheral neuropathy component may be more consistently penetrant.

**Expressivity:** **Variable** — supported by (a) intrafamilial variation in phenotype composition (ataxia+neuropathy vs. neuropathy alone), (b) variable presence of pectus carinatum, and (c) the atypical/expanded phenotypes reported in later, presumably unrelated cases (parkinsonism, dystonia/chorea, anterior horn cell signs, mild cognitive change) — suggesting a broad and still-emerging phenotypic spectrum.

**Genetic anticipation:** Not reported/established (unlike polyglutamine-repeat SCAs, SCA43 is caused by conventional missense/nonsense point mutations, not a repeat expansion, so anticipation is not mechanistically expected and has not been described).

**Germline mosaicism:** Not reported.

**Founder effects:** The C143Y mutation was identified in a single large Belgian founder family; whether it represents a true population founder mutation for Belgium/Northern Europe versus a private familial mutation is not established from available data.

**Consanguinity:** Not relevant to the dominant SCA43 phenotype (relevant instead to the recessive allelic disorder CMT2T, where biallelic transmission would be favored by consanguinity).

**Carrier frequency:** Not established for SCA43 (autosomal dominant, so "carrier" framing is less applicable than for recessive CMT2T, whose carrier frequency also has not been formally reported, though *MME* recessive variants are noted to be a comparatively frequent cause of recessive axonal CMT in the Japanese population specifically).

**Population demographics:**
- Affected populations: Founder family of Belgian (European) ancestry; additional reported cases lack detailed ancestry information in the abstracts reviewed, though the Japanese CMT2T literature is extensive for the *allelic* recessive disorder.
- Geographic distribution: No endemic/regional clustering established beyond the single reported kindred.
- Sex ratio: No skew reported/expected (autosomal dominant, non-sex-linked).
- Age distribution: Adult (post-40s) onset in all reported cases to date; no pediatric cases described.

---

## 10. Diagnostics

**Clinical tests:**
- **Nerve conduction studies/EMG:** Demonstrates progressive, predominantly **motor axonal neuropathy** in the lower limbs, with significantly increased F-wave latency and typically preserved sensory nerve action potentials in most affected individuals (LOINC/electrophysiology testing category).
- **Nerve biopsy (sural nerve):** Shows axonal pathology consistent with CMT2-type polyneuropathy (performed in at least one patient in the founder family).
- **Brain MRI:** Shows **moderate cerebellar vermis atrophy** — a supportive but non-specific imaging finding (Radiopaedia/RadLex: cerebellar atrophy, vermian atrophy).
- No specific validated biomarker (blood/CSF) has been identified for SCA43.

**Genetic testing:**
- **Recommended approach:** Given the extreme rarity and the fact that only two pathogenic variants are so far described, *MME* sequencing is typically included as part of a **broader hereditary ataxia gene panel** or via **exome/genome sequencing** in patients with combined cerebellar ataxia + peripheral (especially motor axonal) neuropathy, once more common causes (SCA1/2/3/6, Friedreich ataxia, etc.) have been excluded.
- **Whole exome sequencing (WES)** was the discovery method used in the founder family (Agilent SureSelect All Exon v1 capture, Illumina HiSeq2000), combined with prior **genome-wide linkage analysis** (400 microsatellite markers, ~8.7 cM spacing) that localized the locus to a 31.3 Mb region on chromosome 3q23–q26.31 (LOD score Z = 2.47).
- **Single-gene *MME* Sanger sequencing** can confirm/screen a suspected pathogenic variant once identified by WES/panel.
- No specific chromosomal microarray, karyotype, FISH, mitochondrial DNA testing, or repeat-expansion testing is relevant, as SCA43 is not caused by a repeat expansion or structural/chromosomal abnormality.

**Clinical diagnostic criteria:** No formal consensus/society diagnostic criteria exist specifically for SCA43 (too recently described, too few cases); diagnosis rests on the combination of adult-onset progressive cerebellar ataxia + axonal (typically motor-predominant) peripheral neuropathy + a confirmed pathogenic heterozygous *MME* variant, after exclusion of more common dominant ataxias.

**Differential diagnosis:** Other ADCA type I disorders with combined ataxia+neuropathy phenotype (e.g., SCA1, SCA2, SCA3/Machado-Joseph disease, SCA4), Friedreich ataxia (though typically recessive/early-onset), CMT2 subtypes with incidental ataxia, and — per the reported phenocopy literature — atypical parkinsonian syndromes and adult-onset dystonia/chorea syndromes, given the expanding movement-disorder phenotypic overlap now reported for SCA43.

**Screening:** No population or newborn screening applicable (adult-onset, ultra-rare, family-specific mutation); cascade genetic testing/counseling of at-risk relatives in identified families is the relevant screening approach once a family-specific *MME* variant is known.

---

## 11. Outcome/Prognosis

No formal survival, life-expectancy, or standardized quality-of-life outcome data exist for SCA43 given the small number of reported cases. The disorder is described as **slowly progressive**, implying a chronic, non-remitting course over years to decades, with progressive gait/limb ataxia and progressive lower-limb motor neuropathy (weakness, atrophy, areflexia) as the dominant drivers of disability. **Complications** would be expected to parallel other ADCA/CMT2-overlap disorders: falls, mobility impairment, foot deformity progression (pes cavus), and — in the atypical cases — additional motor system involvement (anterior horn cell signs, rigidity) or hyperkinetic movement-disorder features that may further impact function. No disease-specific prognostic biomarkers have been identified.

---

## 12. Treatment

**No disease-modifying or curative therapy exists for SCA43.** Management is entirely **symptomatic and supportive**, following general practice for autosomal dominant cerebellar ataxias:

- **Pharmacotherapy (symptomatic):**
  - Tremor: beta-blockers, primidone (MAXO: pharmacotherapy; specific agents not SCA43-validated but general ADCA practice).
  - Dystonia (in cases with the expanded dystonic phenotype): botulinum toxin injections.
  - Parkinsonism (in phenocopy/overlap presentations): levodopa trial.
  - Mood/depression: antidepressants as needed.
  - Neuropathic pain (lower-limb pain component): standard neuropathic pain agents (not specifically studied in SCA43).
- **Rehabilitative/supportive care (MAXO:0000011 physical therapy; MAXO:0000950 supportive care):**
  - Physical therapy, occupational therapy, and speech therapy have been noted to produce gradual functional improvement in general ADCA management and would be the mainstay for SCA43 gait/balance and motor neuropathy symptoms.
  - Orthotic management (e.g., ankle-foot orthoses) for pes cavus/foot drop from motor neuropathy.
- **Genetic counseling (MAXO:0000079):** Recommended for affected families given autosomal dominant transmission with ~50% risk to offspring, and for distinguishing SCA43 (dominant) from the biallelic recessive CMT2T allelic disorder in relatives.
- **Experimental/targeted therapy:** None specific to SCA43 in clinical trials (searched ClinicalTrials.gov context — no SCA43-specific trials identified). Of note, **neprilysin itself is a drug target in an unrelated context** — the ARNI drug **sacubitril/valsartan (LCZ696)**, an FDA-approved neprilysin *inhibitor* combined with an angiotensin receptor blocker, is used in heart failure with reduced ejection fraction (PARADIGM-HF trial) to raise natriuretic peptide levels by blocking their NEP-mediated degradation. This is **mechanistically the opposite direction** relevant to SCA43 (SCA43 arises from NEP dysfunction/altered activity, not from a state where further pharmacologic NEP inhibition would be therapeutic) — worth noting only as a caution that *MME*/NEP is already a pharmacologically manipulated target in a different clinical context, and is not itself a suggested treatment avenue for SCA43.
- **Treatment algorithms/combination therapy:** No SCA43-specific clinical pathway exists; management follows general multidisciplinary ataxia/neuropathy care (neurology + physiatry + genetics).

---

## 13. Prevention

No primary prevention exists (monogenic dominant disorder). **Prenatal genetic counseling and cascade predictive testing** of at-risk relatives in a known SCA43 family is the only applicable preventive/risk-stratification measure once a family-specific pathogenic *MME* variant has been identified — standard ACMG/genetic-counseling practice for autosomal dominant adult-onset neurodegenerative disease, though no SCA43-specific prenatal or preimplantation genetic diagnosis (PGD) case has been reported in the literature reviewed. No vaccination, public health, or environmental intervention is applicable.

---

## 14. Other Species / Natural Disease

No naturally occurring SCA43 has been described in non-human species. *MME*/neprilysin is highly conserved across mammals (mouse ortholog *Mme*, MGI:97004), but no spontaneous or naturally occurring animal disease analogous to human SCA43 has been reported (searched OMIA and general veterinary literature — no hits). No zoonotic or cross-species transmission relevance (this is a non-infectious, monogenic disorder).

---

## 15. Model Organisms

**Mouse (*Mme* knockout, MGI:97004; e.g., allele *Mme^tm1Cge*, MGI:2137696):** Constitutive *Mme*-null mice have been characterized primarily in the context of **amyloid-beta metabolism and innate immune/inflammatory phenotypes**, not ataxia:
- **Increased brain and plasma amyloid-beta peptide levels**, in a gene-dose-dependent manner — neprilysin deficiency impairs both degradation of exogenously administered Aβ and suppression of endogenous Aβ.
- Regional brain Aβ levels in *Mme*-deficient mice follow the order hippocampus > cortex > thalamus/striatum > **cerebellum (lowest)** — notably, the region least affected by Aβ accumulation in this model (cerebellum) is the region most affected in human SCA43, arguing against a simple Aβ-accumulation mechanism for the cerebellar phenotype (consistent with the human genetic authors' own conclusion that "NEP deficiency does not lead to the development of AD" in SCA43 patients).
- **Non-neurological phenotypes:** enhanced allergic contact dermatitis responses; diffuse hepatic necrosis after LPS shock or combined TNF/IL-1β treatment — reflecting NEP's broader immunomodulatory/neuropeptide-degrading roles outside the nervous system.

**Critical model limitation:** No mouse model carrying the human-specific dominant missense variant (p.C143Y) or a comparable dominant-negative *Mme* allele has been reported. The discovery authors explicitly caution that **standard *Mme* loss-of-function/knockout mice would likely not recapitulate the human SCA43 phenotype**, precisely because the human disease appears to depend on a dominant, likely non-haploinsufficient mechanism (possibly dominant-negative competition for substrate, e.g., dynorphin processing) rather than simple reduced NEP dosage — a mechanism a simple knockout cannot model. This represents a clear, currently unaddressed need for an appropriately engineered knock-in mouse model (e.g., *Mme^C143Y/+*) to test the dominant-negative/altered-substrate-specificity hypothesis in vivo, and is a candidate `HUMAN_MODEL_MISMATCH` consideration if this disease is curated into dismech (existing *Mme*-null mouse phenotypes should not be assumed to validate or recapitulate the human SCA43 cerebellar/neuropathy phenotype).

**Other species:** No zebrafish, *Drosophila*, *C. elegans*, or iPSC/organoid models specific to the SCA43 dominant variant have been reported in the literature surveyed.

---

## Summary Table of Key Ontology Term Suggestions

| Category | Suggested term(s) |
|---|---|
| Disease | MONDO:0014867 (Spinocerebellar ataxia 43); OMIM:617018 |
| Causal gene | HGNC:7154 (MME); hgnc:7154 lowercase form per dismech convention |
| Allelic disorder | OMIM:617017 (CMT2T) |
| Phenotypes (HP) | HP:0002066 Gait ataxia; HP:0002070 Limb ataxia; HP:0001260 Dysarthria; HP:0000639 Nystagmus; HP:0001337 Tremor; HP:0006855 Cerebellar vermis atrophy; HP:0003693/HP:0007340 Distal muscle weakness/atrophy; HP:0001761 Pes cavus; HP:0001284 Areflexia; HP:0003477 Axonal neuropathy; HP:0000768 Pectus carinatum |
| Biological process (GO) | GO:0006508 proteolysis; GO:0004222 metalloendopeptidase activity; GO:0097242 amyloid-beta clearance; GO:0007218 neuropeptide signaling pathway |
| Cell types (CL) | CL:0000121 Purkinje cell; Schwann cell (CL:0002573/CL:0000381); peripheral motor neuron |
| Anatomy (UBERON) | UBERON:0002037 cerebellum; peripheral nerve (UBERON:0002211) |
| Treatment (MAXO) | MAXO:0000011 physical therapy; MAXO:0000950 supportive care; MAXO:0000079 genetic counseling; NCIT:C15986 Pharmacotherapy |

---

## Sources

- [Entry - #617018 - SPINOCEREBELLAR ATAXIA 43; SCA43 - OMIM](https://www.omim.org/entry/617018)
- [MME mutation in dominant spinocerebellar ataxia with neuropathy (SCA43) - PMC (full text)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4991603)
- [MME mutation in dominant spinocerebellar ataxia with neuropathy (SCA43) - PubMed, PMID: 27583304](https://pubmed.ncbi.nlm.nih.gov/27583304/)
- [MME mutation in dominant spinocerebellar ataxia with neuropathy (SCA43) - Neurology Genetics](https://www.neurology.org/doi/10.1212/NXG.0000000000000094)
- [Entry - *120520 - MEMBRANE METALLOENDOPEPTIDASE; MME - OMIM](https://omim.org/entry/120520)
- [Entry - #617017 - CHARCOT-MARIE-TOOTH DISEASE, AXONAL, TYPE 2T; CMT2T - OMIM](https://www.omim.org/entry/617017)
- [Mutations in MME cause an autosomal-recessive Charcot–Marie–Tooth disease type 2 - Higuchi et al., Annals of Neurology](https://onlinelibrary.wiley.com/doi/full/10.1002/ana.24612)
- [NM_007289.4(MME):c.1342C>T (p.Arg448Ter) AND Spinocerebellar ataxia 43 - ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/RCV001196533/)
- [Spinocerebellar ataxia 43 - GARD (NIH Genetic and Rare Diseases Information Center)](https://rarediseases.info.nih.gov/diseases/17917/spinocerebellar-ataxia-43)
- [spinocerebellar ataxia 43 - National Organization for Rare Disorders](https://rarediseases.org/mondo-disease/spinocerebellar-ataxia-43/)
- [Spinocerebellar ataxia 43 (Concept Id: C4310763) - MedGen - NCBI](https://www.ncbi.nlm.nih.gov/medgen/934730)
- [Orphanet: Spinocerebellar ataxia type 43](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Lng=GB&Expert=497764)
- [A case of sporadic spino cerebellar ataxia-43 presenting as ataxia, rigidity, anterior horn cell involvement and cognitive changes - Journal of the Neurological Sciences](https://www.jns-journal.com/article/S0022-510X(23)00650-0/fulltext)
- [Tremor and Craniofacial Dystonia Preceding Ataxia in SCA43: Expanding the Phenotypic Spectrum of MME-related Ataxia - The Cerebellum](https://link.springer.com/article/10.1007/s12311-026-02023-0)
- [Spinocerebellar Ataxia (SCA) Variant Masquerading as a Parkinsonian-plus Syndrome (P6-5.022) - Neurology](https://www.neurology.org/doi/10.1212/WNL.0000000000211725)
- [Mme MGI Mouse Gene Detail - MGI:97004](https://www.informatics.jax.org/marker/MGI:97004)
- [LCZ696 (sacubitril/valsartan), an angiotensin receptor neprilysin inhibitor (ARNI) - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4565085/)
- [Autosomal dominant cerebellar ataxias in Spain: molecular and clinical correlations, prevalence estimation and survival analysis - PubMed](https://pubmed.ncbi.nlm.nih.gov/15876341/)