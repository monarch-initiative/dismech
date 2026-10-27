---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-19T08:41:24.067314'
end_time: '2026-08-19T08:45:45.832157'
duration_seconds: 261.76
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: DLG4-Related Synaptopathy
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
  web_search_requests: 13
  num_turns: 19
  total_cost_usd: 1.8382972999999998
  session_id: 39a0bbf2-8447-55f9-bf44-86bf2cfba3f2
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 26
reference_validation:
  total_references: 14
  verified: 13
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.071
  quotes_checked: 4
  quotes_valid: 3
  quotes_unsupported: 1
  unsupported_quote_references:
  - DOI:10.1073/pnas.1517045112
  relevance_assessed: 13
  on_topic: 8
  off_topic: 2
  off_topic_references:
  - DOI:10.1073/pnas.1517045112
  - PMC:PMC3546964
  unresolved_references:
  - DOI:10.1111/cge.14411](https://onlinelibrary.wiley.com/doi/full/10.1111/cge.14411
  needs_review: true
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** DLG4-Related Synaptopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **DLG4-Related Synaptopathy** covering all of the
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

# DLG4-Related Synaptopathy: Comprehensive Research Report

## 1. Disease Information

### Overview
DLG4-related synaptopathy is a rare, autosomal dominant neurodevelopmental disorder caused by de novo (or, rarely, inherited) pathogenic variants in *DLG4*, the gene encoding postsynaptic density protein 95 (PSD-95), a master scaffolding protein of the glutamatergic postsynaptic density. The disorder was first delineated as a distinct clinical entity by Rodríguez-Palmero et al. (2021), who characterized 53 individuals and coined the term "DLG4-related synaptopathy" ([Rodríguez-Palmero et al., 2021, *Genet Med*](https://www.nature.com/articles/s41436-020-01075-9); [PMID:33597769](https://pubmed.ncbi.nlm.nih.gov/33597769/)). The clinical picture is dominated by global developmental delay, intellectual disability (typically mild-to-moderate), autism spectrum disorder (ASD), attention-deficit/hyperactivity disorder (ADHD), and epilepsy in roughly half of patients, with a broader multisystem phenotype including hypotonia, movement disorders, sleep disturbance, ophthalmologic abnormalities, and marfanoid connective-tissue features in a subset.

### Key Identifiers
| Resource | Identifier |
|---|---|
| Gene (HGNC) | *DLG4*, HGNC:2903 |
| OMIM Gene | *602887 – DISCS LARGE MAGUK SCAFFOLD PROTEIN 4; DLG4 |
| OMIM Phenotype | **#618793 – INTELLECTUAL DEVELOPMENTAL DISORDER, AUTOSOMAL DOMINANT 62 (MRD62)** ([OMIM:618793](https://www.omim.org/entry/618793)) |
| MONDO | **MONDO:0032919** (label: "intellectual developmental disorder 62"; "DLG4-related synaptopathy" is an exact synonym, confirmed via OLS/MONDO) |
| GeneReviews | [DLG4-Related Synaptopathy — NBK592682](https://www.ncbi.nlm.nih.gov/books/NBK592682/) |
| Chromosomal locus | 17p13.1 |
| MedlinePlus Genetics | [dlg4-related-synaptopathy](https://medlineplus.gov/genetics/condition/dlg4-related-synaptopathy/) |

### Synonyms / Alternative Names
- SHINE syndrome (**S**leep disturbances, **H**ypotonia, **I**ntellectual disability, **N**eurologic disorder, **E**pilepsy) — the patient-advocacy-coined acronym used by the DLG4 SHINE Foundation
- DLG4 synaptopathy
- Intellectual developmental disorder, autosomal dominant 62 (MRD62/IDDA62)
- Historically, before the syndrome was delineated, some cases were reported as "intellectual disability with marfanoid features" (Moutton et al., 2018)

### Data Provenance
Information derives predominantly from **aggregated, multi-center case-series/cohort resources** rather than a single large EHR-based cohort, reflecting the disorder's rarity:
- Rodríguez-Palmero et al. 2021 (n=53, GeneMatcher-assembled international cohort)
- Moutton et al. 2018 (n=3, exome-sequencing trio discovery cohort; [PMID study](https://onlinelibrary.wiley.com/doi/abs/10.1111/cge.13243))
- Kassabian et al. 2024, *Epilepsia* — expanded epilepsy-focused cohort (n=35: 23 newly reported + 12 updated) ([Genotype-phenotype/DEE study](https://onlinelibrary.wiley.com/doi/abs/10.1111/epi.17876))
- Patient-registry/natural-history data curated by the **DLG4 SHINE Foundation** and **Simons Searchlight**, which together have identified ~100 individuals with pathogenic *DLG4* variants
- Individual case reports (deep intronic variant, Levy et al. 2024, *Clin Genet*; intellectual-regression case, 2023, *Hum Genome Var*)

---

## 2. Etiology

### Disease Causal Factors
DLG4-related synaptopathy is a **monogenic, genetically determined** disorder. There is no known infectious, toxic, or purely environmental cause. The near-exclusive mechanism is **haploinsufficiency of PSD-95** produced by heterozygous loss-of-function (or loss-of-function-equivalent) variants in *DLG4*.

### Genetic Risk Factors
- **Causal variant class:** predominantly **protein-truncating variants** (nonsense, frameshift, canonical splice-site) predicted to trigger nonsense-mediated decay or produce a non-functional truncated protein; missense variants are also reported (mechanism less certain, but generally interpreted as loss-of-function); rare **deep intronic** variants disrupting splicing have also been described (Levy et al., 2024, *Clin Genet*, [DOI:10.1111/cge.14411](https://onlinelibrary.wiley.com/doi/full/10.1111/cge.14411)).
- **Gene constraint:** *DLG4* is exceptionally intolerant of loss-of-function variation in the general population (**pLI = 1**; under gnomAD v4 conventions this corresponds to LOEUF well below the 0.6 constrained-gene threshold), consistent with haploinsufficiency as the pathogenic mechanism and explaining the complete absence of the variant class in population databases.
- **Inheritance:** essentially always **de novo**; rare instances of transmission from a mosaic or (very rarely) mildly affected heterozygous parent are described in GeneReviews.
- No modifier genes have yet been formally established, though interacting synaptic genes (*SYNGAP1*, other DLG-MAGUK family members) are biologically plausible candidates given shared pathway membership.

### Environmental Risk Factors
None established. This is a purely genetic (Mendelian) disorder; no epidemiological association with parental age, toxin exposure, or perinatal factors has been reported in the literature to date.

### Protective Factors
None identified in the literature — genetic or environmental. No protective variants or modifier alleles have been characterized.

### Gene-Environment Interactions
Not established/not applicable given the disorder's fully penetrant monogenic basis; no CTD/PheGenI gene-environment interaction data exist for *DLG4*.

---

## 3. Phenotypes

Frequencies below are drawn primarily from the Rodríguez-Palmero et al. 2021 cohort (n=53) and the Kassabian et al. 2024 expanded/epilepsy cohort (n=35), as reported in GeneReviews and the primary literature.

### Cognitive / Developmental (Symptoms)
| Phenotype | Frequency | Notes | Suggested HPO term |
|---|---|---|---|
| Intellectual disability | ~98–100% | Mild-to-moderate most common; severe/profound less common | HP:0001249 (Intellectual disability) |
| Global developmental delay | 84% | Mean age of independent walking 20.7 months; first words 32.2 months | HP:0001263 (Global developmental delay) |
| Developmental regression | ~40% | Motor and/or language regression; strongly associated with ESES/DEE-SWAS in the epilepsy subgroup | HP:0002376 (Developmental regression) |
| Autism spectrum disorder | 56% | More frequent in individuals with moderate-severe ID | HP:0000729 (Autistic behavior) |
| ADHD | 57% | More frequent with co-occurring ASD | HP:0007018 (Attention deficit hyperactivity disorder) |
| Anxiety | 53% | Often triggered by loud sounds or separation | HP:0000739 (Anxiety) |

### Neurologic Signs
| Phenotype | Frequency | Notes | HPO term |
|---|---|---|---|
| Epilepsy | 53% | Generalized and/or focal; mean onset ~6 years | HP:0001250 (Seizure) |
| Developmental and epileptic encephalopathy with spike-wave activation in sleep (DEE-SWAS/ESES) | >25% of the epilepsy-cohort subset | Confirmed as part of the phenotypic spectrum by Kassabian et al. 2024; associated with regression in essentially all affected individuals | HP:0011200 (Ictal EEG abnormality) / HP:0012469 (Infantile spasms — n/a; use ESES-specific term where available) |
| Hypotonia | 53% (up to ~60% in some series) | Central hypotonia | HP:0001252 (Hypotonia) |
| Movement disorder | 46% | Stereotypies and ataxia most common; also dystonia and tremor | HP:0100022 (Abnormality of movement); HP:0000733 (Stereotypy); HP:0001251 (Ataxia); HP:0001332 (Dystonia); HP:0001337 (Tremor) |
| Migraine / headache | reported in a subset | — | HP:0002076 (Migraine) |
| Brain MRI abnormalities | ~30% | Cerebral/cerebellar atrophy, thin corpus callosum, dysmorphic hippocampus | HP:0002119 (Ventriculomegaly), HP:0002079 (Hypoplasia of the corpus callosum), HP:0007360 (Aplasia/hypoplasia of the cerebellum) |

### Ophthalmologic Findings (Clinical Signs)
| Phenotype | Frequency | Notes | HPO term |
|---|---|---|---|
| Overall ophthalmologic involvement | ~50% | — | — |
| Strabismus | most common ocular finding | — | HP:0000486 (Strabismus) |
| Hyperopia | second most common | — | HP:0000540 (Hyperopia) |
| Nystagmus | — | — | HP:0000639 (Nystagmus) |
| Cortical visual impairment | less common | — | HP:0100704 (Cerebral visual impairment) |

### Musculoskeletal / Marfanoid Connective-Tissue Findings
| Phenotype | Frequency | Notes | HPO term |
|---|---|---|---|
| Joint laxity | 36.9% | — | HP:0001382 (Joint hypermobility) |
| Scoliosis | 20% | — | HP:0002650 (Scoliosis) |
| Marfanoid habitus | ~24% | Long face, slender build, long/thin fingers, pectus excavatum, high-arched palate | HP:0001519 (Disproportionate tall stature) / HP:0001166 (Arachnodactyly) / HP:0000276 (Long face) / HP:0000218 (High-palate) / HP:0000767 (Pectus excavatum) |

This marfanoid connective-tissue association was the original phenotype through which *DLG4* was first implicated in disease (Moutton et al. 2018, *Clin Genet*: "Truncating variants of the DLG4 gene are responsible for intellectual disability with marfanoid features," [PMID study](https://onlinelibrary.wiley.com/doi/abs/10.1111/cge.13243)) — patients showed "mild-to-moderate intellectual disability with similar marfanoid features, including a long face, high-arched palate, long and thin fingers, pectus excavatum, scoliosis and ophthalmological manifestations (nystagmus or strabismus)."

### Sleep and Gastrointestinal
| Phenotype | Frequency | Notes | HPO term |
|---|---|---|---|
| Sleep disturbance | 45% | Sleep-onset and/or sleep-maintenance difficulty | HP:0002360 (Sleep disturbance) |
| Vomiting | 29% | Often triggered by seizures, motion, or fatigue | HP:0002013 (Vomiting) |
| GERD / feeding difficulty | reported | — | HP:0002020 (Gastroesophageal reflux); HP:0011968 (Feeding difficulties) |

### Phenotype Characteristics
- **Onset:** Early childhood — congenital/infantile-onset global developmental delay is the rule; epilepsy onset averages ~6 years.
- **Severity:** Predominantly mild-to-moderate for ID, but a subset (particularly those with DEE-SWAS/ESES) show a more severe, regressive course.
- **Progression:** Static/developmental-delay pattern in most; a **regressive** subgroup (~40%) exists, closely tied to the presence of DEE-SWAS/ESES epilepsy.
- **Frequency data source:** Rodríguez-Palmero et al. 2021 (primary source of the percentages above) and Kassabian et al. 2024 (epilepsy/DEE-focused expansion).

### Quality of Life Impact
No disease-specific EQ-5D/SF-36/PROMIS data have been published; QoL burden is inferred qualitatively from the combination of intellectual disability, autism, epilepsy (often drug-resistant in the DEE-SWAS subset), sleep disturbance, and anxiety — all of which are recognized independently as major contributors to caregiver burden and reduced adaptive functioning in neurodevelopmental disorders generally. The DLG4 SHINE Foundation registry/natural-history effort is intended in part to generate such data prospectively ([DLG4 SHINE Natural History Studies](https://www.dlg4shine.org/natural-history-studies)).

---

## 4. Genetic/Molecular Information

### Causal Gene
- ***DLG4*** (Discs Large MAGUK Scaffold Protein 4 / PSD-95), HGNC:2903, OMIM *602887, located at **17p13.1**.
- Sole established causal gene for this disorder; OMIM phenotype #618793 (MRD62).

### Pathogenic Variants
- **Gene/protein:** DLG4/PSD-95; UniProt human PSD-95.
- **Variant classification:** Per ACMG/AMP, essentially all reported variants are classified pathogenic/likely pathogenic; ClinVar contains multiple submissions (e.g., NM_001321075.3(DLG4):c.1592-1G>A associated with "Intellectual developmental disorder 62," [ClinVar RCV001800207](https://www.ncbi.nlm.nih.gov/clinvar/RCV001800207/)).
- **Variant type/class:**
  - **Protein-truncating variants** (nonsense, frameshift, canonical ±1/±2 splice-site) — the large majority
  - **Missense variants** — reported, presumed loss-of-function but mechanism not experimentally proven in most cases
  - **Silent (synonymous) and deep-intronic variants** affecting splicing — rare but documented (Levy et al. 2024)
  - **No gene-targeted deletions/duplications (CNVs)** reported to date per GeneReviews
- **Allele frequency:** *DLG4* pathogenic/truncating variants are **absent from population databases** (gnomAD), consistent with the gene's extreme constraint (pLI = 1).
- **Somatic vs. germline:** Disease-causing variants are germline (de novo in the proband in the great majority of cases); parental somatic/germline mosaicism has been documented in rare families, informing recurrence-risk counseling.
- **Functional consequence:** **Haploinsufficiency** is the dominant proposed mechanism — loss of one functional *DLG4* allele is not compensated by other DLG-MAGUK paralogs, based on both human genetic and mouse-knockout data.

### Protein Domain Structure and Molecular Function
PSD-95 is an ~80 kDa **MAGUK (membrane-associated guanylate kinase) family** scaffolding protein with a modular domain architecture: **three PDZ domains (PDZ1, PDZ2, PDZ3)**, one **SH3 domain**, and one catalytically-dead **guanylate kinase (GK) domain** (the SH3-GK forms a conserved "supermodule").
- **PDZ1/PDZ2** cluster NMDA receptor GluN2 (NR2) subunits (via the C-terminal -ESDV/tSXV PDZ-binding motif), neuroligins, and inward-rectifier/voltage-gated K⁺ channels at the postsynaptic membrane.
- **PDZ3** binds distinct partners including neuroligins and CRIPT.
- PSD-95 anchors **AMPA receptors** indirectly through auxiliary transmembrane AMPAR regulatory proteins (**TARPs/stargazin**), which bind PDZ domains and stabilize AMPARs at the postsynaptic density.
- PSD-95-family MAGUKs are described as "essential for anchoring AMPA and NMDA receptor complexes at the postsynaptic density" ([PNAS 2015](https://www.pnas.org/doi/10.1073/pnas.1517045112)).
- PSD-95 interacts with, and helps organize, additional neurodevelopmental-disease-relevant partners including **SYNGAP1** and other postsynaptic scaffolding/signaling molecules.
- Acute inactivation of PSD-95 destabilizes AMPA receptors at hippocampal synapses, and PSD-95 is required for NMDA-receptor-dependent synaptic plasticity, directly linking loss of PSD-95 function to impaired excitatory synaptic signaling and plasticity.

**Suggested GO terms:** GO:0098794 (postsynapse); GO:0014069 (postsynaptic density); GO:0098839 (postsynaptic density membrane); GO:0035249 (synaptic transmission, glutamatergic); GO:0035255 (ionotropic glutamate receptor binding); GO:0007268 (chemical synaptic transmission); GO:0099054 (presynapse — for the paralogous Drosophila dlg data).

### Other DLG-MAGUK Family Members (Relevant Comparators)
Vertebrates have four DLG-MAGUK paralogs: **DLG1 (SAP97)**, **DLG2 (PSD-93/chapsyn-110... note: DLG2 = SAP102/NE-dlg per some nomenclature)**, **DLG3 (SAP102/NE-dlg or PSD-93 depending on source)**, and **DLG4 (PSD-95)**. Each has its own associated neurodevelopmental disorder (*DLG2*- and *DLG3*-related intellectual disability/schizophrenia-risk phenotypes have been separately described), and the human genetic and phenotypic data indicate that **these paralogs cannot functionally compensate for loss of PSD-95**, explaining why *DLG4* haploinsufficiency alone is sufficient to cause disease (see "Neurodevelopmental Disorders Associated with PSD-95 and Its Interaction Partners," [PMID:35457207](https://pubmed.ncbi.nlm.nih.gov/35457207/); [PMC9025546](https://pmc.ncbi.nlm.nih.gov/articles/PMC9025546/)).

### Modifier Genes
None formally established.

### Epigenetic Information / Chromosomal Abnormalities
No disease-specific epigenetic signature (DNA methylation episignature) has yet been published for DLG4-related synaptopathy (unlike some other NDD genes). No recurrent chromosomal abnormalities (aneuploidy, translocation) are implicated — this is a single-gene, sequence-variant disorder.

---

## 5. Environmental Information

- **Environmental/toxin factors:** None identified as causal or exacerbating.
- **Lifestyle factors:** Not applicable as a primary etiologic contributor; seizure and behavioral triggers (loud sounds, separation, motion, fatigue) are described as symptom modulators rather than disease causes.
- **Infectious agents:** None implicated.

---

## 6. Mechanism / Pathophysiology

### Causal Chain (Molecular → Cellular → Clinical)
1. **Molecular trigger:** Heterozygous loss-of-function (or splice-disrupting) variant in *DLG4* → reduced/absent functional PSD-95 protein (haploinsufficiency), most consistent with nonsense-mediated decay of the truncated transcript or production of a non-functional truncated protein lacking key PDZ/SH3/GK domains.
2. **Molecular consequence:** Reduced PSD-95 scaffolding capacity at the excitatory postsynaptic density → impaired clustering/stabilization/trafficking of **NMDA receptors** (via PDZ1/PDZ2-NR2 interaction) and **AMPA receptors** (via TARP/stargazin-PDZ interactions) at the synaptic membrane.
3. **Cellular consequence:** Altered excitatory synapse number, maturation, and dendritic spine morphology; disrupted excitatory/inhibitory synaptic balance in cortical and hippocampal circuits; impaired NMDA-receptor-dependent long-term potentiation/synaptic plasticity (demonstrated directly in *Dlg4*-null mouse studies).
4. **Circuit/systems consequence:** Disrupted glutamatergic synaptic transmission and plasticity in cortex, hippocampus, and cerebellum — a **synaptopathy** — producing the core neurodevelopmental phenotype (global developmental delay, intellectual disability). In a subset, cortical hyperexcitability manifests as epilepsy, including the severe DEE-SWAS/ESES phenotype associated with active regression.
5. **Clinical manifestation:** Global developmental delay, intellectual disability, ASD/ADHD, epilepsy (including DEE-SWAS), movement disorder, hypotonia, and — via a less well-characterized connective-tissue mechanism — marfanoid skeletal/ophthalmologic features.

### Cellular Processes and Cell Types Involved
- **Primary cell type:** Glutamatergic (excitatory) neurons — cortical pyramidal neurons and hippocampal principal neurons (suggested CL term: CL:0000679, glutamatergic neuron; CL:0000598, pyramidal neuron).
- **Subcellular compartment:** Postsynaptic density of the dendritic spine (suggested GO Cellular Component: GO:0014069 postsynaptic density; GO:0043197 dendritic spine).
- **Process:** Synaptogenesis, excitatory synaptic maturation, receptor trafficking/anchoring, and activity-dependent synaptic plasticity (LTP/LTD).

### Molecular/Systems Biology Evidence
- **Animal model data (mouse, Feyder et al. 2010):** *Dlg4⁻/⁻* (PSD-95 knockout) mice show increased repetitive behaviors, abnormal social/communicative behaviors, impaired motor coordination, and increased stress reactivity, together with subtle dysmorphology of amygdala dendritic spines and altered forebrain expression of synaptic genes — directly paralleling the human ASD/anxiety/motor phenotype ("Association of Mouse *Dlg4* (PSD-95) Gene Deletion and Human *DLG4* Gene Variation With Phenotypes Relevant to Autism Spectrum Disorders and Williams' Syndrome," [PMID:20952458](https://pubmed.ncbi.nlm.nih.gov/20952458/)).
- **Invertebrate model data (Drosophila):** The *dlg* (discs-large) tumor suppressor gene — the invertebrate DLG-MAGUK ortholog — is required for normal synapse structure at the glutamatergic neuromuscular junction and regulates postsynaptic glutamate receptor subunit composition and structural synaptic plasticity, establishing deep evolutionary conservation of the DLG-MAGUK synaptic scaffolding function across the animal kingdom ([PMC545058](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC545058/); [PMC4658212](https://pmc.ncbi.nlm.nih.gov/articles/PMC4658212/)).
- **In vitro/biochemical data:** Acute inactivation of PSD-95 destabilizes AMPA receptors at hippocampal synapses ([PMC3546964](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3546964/)); PDZ1/PDZ2 ligand-binding-deficient PSD-95 knock-in mice show impaired synaptic clustering of PSD proteins, altered signal transmission, and disrupted learning behavior — directly modeling domain-specific loss of function ([PMC3575367](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3575367/)).

### Genotype-Phenotype Correlation
No robust variant-position-specific genotype-phenotype correlation has been firmly established; the disorder is thought to be driven predominantly by simple **haploinsufficiency** regardless of the precise truncating-variant location, though a dedicated genotype-phenotype study is an active area of ongoing collaborative research (ERN-ITHACA "Genotype-phenotype characterization of DLG4-related synaptopathy" call for collaboration, and the Kassabian et al. 2024 DEE-focused cohort).

---

## 7. Anatomical Structures Affected

### Organ Level
- **Primary organ:** Brain (central nervous system) — cortex, hippocampus, cerebellum, corpus callosum (per neuroimaging findings in ~30% of patients).
- **Secondary/associated systems:**
  - Musculoskeletal system (joint laxity, scoliosis, marfanoid habitus)
  - Visual system/eye (strabismus, hyperopia, nystagmus, cortical visual impairment)
  - Gastrointestinal system (vomiting, GERD/feeding difficulty)
  - Sleep/circadian system

**Suggested UBERON terms:** UBERON:0000955 (brain); UBERON:0001950 (neocortex); UBERON:0002421 (hippocampal formation); UBERON:0002037 (cerebellum); UBERON:0002336 (corpus callosum); UBERON:0000970 (eye); UBERON:0001474 (bone element, for scoliosis/skeletal features).

### Tissue and Cell Level
- Glutamatergic excitatory neuronal populations in cerebral cortex and hippocampus (CL:0000679); cerebellar Purkinje/granule cell circuits secondarily implicated via cerebellar atrophy findings.

### Subcellular Level
- Postsynaptic density / dendritic spine of the excitatory glutamatergic synapse (GO:0014069 postsynaptic density; GO:0043197 dendritic spine; GO:0098794 postsynapse).

### Localization
- Diffuse/bilateral CNS involvement (no clear lateralization); neuroimaging abnormalities when present are typically bilateral/symmetric (cerebral/cerebellar atrophy, thin corpus callosum).

---

## 8. Temporal Development

### Onset
- **Age of onset:** Congenital/early-infantile onset of developmental delay is typical (recognizable within the first 1–2 years of life); mean age of independent walking 20.7 months and first words at 32.2 months indicate onset well within infancy/early childhood.
- **Epilepsy onset:** Mean age ~6 years, though it can occur earlier or later.
- **Onset pattern:** Predominantly **insidious/developmental** (delay from early infancy) rather than acute; a distinct **regressive** subpattern occurs in association with DEE-SWAS/ESES epilepsy.

### Progression
- **Course:** Generally a **static-to-slowly-evolving neurodevelopmental disorder** in the majority; however, ~40% experience frank **developmental regression** (motor and/or language), which is closely tied to the DEE-SWAS/ESES epileptic subtype — in the Kassabian et al. 2024 cohort, regression occurred in essentially all individuals with ESES/DEE-SWAS and in some without it.
- **Disease duration:** Chronic, lifelong; documented survival into adulthood (oldest reported patient in the Kassabian cohort was 61 years old; another report described a patient at age 47), suggesting normal or near-normal life expectancy, though the adult phenotype is likely underrecognized due to historically limited genetic testing in adults.

### Patterns
- **Remission:** No spontaneous remission of the underlying neurodevelopmental phenotype; seizures in the DEE-SWAS subgroup can show EEG/clinical improvement with targeted anti-epileptic treatment (e.g., corticosteroids or other ESES-directed regimens), consistent with general DEE-SWAS management principles.
- **Critical periods:** The DEE-SWAS/ESES window (typically preschool-to-school age) represents a critical period of vulnerability during which active regression occurs — early recognition and EEG monitoring (including overnight/24-hour EEG) during this window is emphasized in management recommendations.

---

## 9. Inheritance and Population

### Epidemiology
- **Prevalence:** Not formally established (no population-based prevalence study); the disorder is characterized as **rare**. As of recent counts, **~100 individuals** worldwide have been identified with a confirmed pathogenic *DLG4* variant through combined clinical literature and the DLG4 SHINE Foundation/Simons Searchlight registries, with 53 formally published in the founding cohort study and 35 in the more recent Kassabian et al. 2024 expanded/epilepsy-focused series.
- **Incidence:** Not established.

### Inheritance Pattern
- **Autosomal dominant**, virtually always due to a **de novo** pathogenic variant.
- **Penetrance:** Appears to be **complete** (or very high) in reported cases — no confirmed asymptomatic carriers of a clearly pathogenic truncating variant have been well documented, though ascertainment bias (family members generally tested only when clinically indicated) limits certainty.
- **Expressivity:** **Variable** — phenotypic severity ranges from mild ID without epilepsy to a severe DEE-SWAS/regressive phenotype, without a clear genotype-driving explanation established to date.
- **Genetic anticipation:** Not applicable/not reported (not a repeat-expansion disorder).
- **Germline mosaicism:** Documented as a rare cause of recurrence in siblings of an apparently de novo proband; GeneReviews notes sibling recurrence risk is "slightly above the general population risk" for this reason.
- **Founder effects:** None reported.
- **Consanguinity:** Not a relevant risk factor given the dominant, de novo mechanism.
- **Carrier frequency:** Not applicable in the traditional sense (dominant, not typically "carried" asymptomatically); population database absence of truncating variants (gnomAD, pLI=1) confirms these variants are not tolerated even in single copy in unaffected individuals.

### Population Demographics
- **Affected populations:** No ethnic/geographic predilection has been reported; cases have been identified across multiple continents/cohorts (European, North American, and other GeneMatcher-connected centers).
- **Sex ratio:** Approximately balanced — the Kassabian et al. 2024 cohort reported a male:female ratio of **19:16**, consistent with no strong sex bias, as expected for an autosomal (not X-linked) disorder.
- **Age distribution:** Wide range reported — from infancy through at least the 6th–7th decade of life (Kassabian cohort median age at inclusion 13 years, range 1.7–61 years).

---

## 10. Diagnostics

### Clinical Tests
- No pathognomonic laboratory biomarker, imaging finding, or biopsy result exists; **the phenotype alone is not sufficiently specific to establish the diagnosis** — GeneReviews explicitly states molecular testing is required.
- **Brain MRI:** Recommended as part of the diagnostic work-up in patients presenting with developmental delay/ID; abnormal in ~30% (cerebral/cerebellar atrophy, corpus callosum thinning, hippocampal dysmorphism), but findings are nonspecific.
- **EEG:** Important given the ~53% epilepsy prevalence and the specific DEE-SWAS/ESES subtype; overnight/24-hour EEG is recommended for individuals with significant cognitive delay, regression, or clinical suspicion of subclinical epileptiform activity.
- **Ophthalmologic exam:** Recommended given the ~50% prevalence of ocular findings (strabismus, hyperopia, nystagmus).

### Genetic Testing
- **Recommended approach:** A **multigene panel** for intellectual disability/epilepsy, or **comprehensive genomic testing** (exome or genome sequencing) — GeneReviews explicitly states that **single-gene *DLG4* testing is rarely useful and typically not recommended** as a first-tier test, given the lack of a specific enough clinical gestalt.
- **Sequence analysis:** Detects the full spectrum of reported variant types (missense, nonsense, small indels, canonical splice-site variants).
- **Gene-targeted deletion/duplication analysis (CNV testing):** No pathogenic CNVs identified to date, so this modality has low diagnostic yield but may still be included in standard panels/exome CNV-calling pipelines.
- **RNA testing (RT-PCR/RNA-seq):** Should be considered for variants of uncertain splicing consequence, including synonymous and deep-intronic variants (as demonstrated by the Levy et al. 2024 deep-intronic case).
- **Trio (parent-child) sequencing** is valuable both diagnostically (confirming de novo status supports pathogenicity) and for recurrence-risk counseling.

### Clinical Diagnostic Criteria
No formal consensus clinical diagnostic criteria (DSM/ICD-style) exist; diagnosis is **genotype-first** (molecular confirmation) combined with a compatible phenotype.

### Differential Diagnosis
Because features (ID, ASD, epilepsy, hypotonia) are non-specific, the differential includes other genetic **synaptopathies** and syndromic neurodevelopmental disorders, most notably:
- **SYNGAP1-related intellectual disability** (explicitly noted as an overlapping synaptopathy differential in GeneReviews, given the direct PSD-95–SynGAP1 interaction)
- Other DLG-MAGUK-family-related disorders (*DLG2*-, *DLG3*-related NDDs)
- Other causes of syndromic ID with marfanoid habitus (e.g., *FBN1*-related Marfan syndrome itself, Lujan-Fryns syndrome, and — per a 2024 case report — *PCDHGA5*-related NDD) must be distinguished from the connective-tissue-overlap presentation.

### Screening
No population-based or newborn screening program exists for this ultra-rare disorder; identification occurs via clinical genetic testing triggered by developmental delay/ID/epilepsy work-up.

---

## 11. Outcome/Prognosis

### Survival and Mortality
- No formal survival statistics (5-/10-year survival, standardized mortality ratio) have been published.
- Survival into adulthood is well documented (oldest reported case 61 years in the Kassabian 2024 cohort; another individual reported at age 47), suggesting the disorder is not associated with markedly shortened life expectancy in the majority of cases, though this is likely an underestimate of the true adult population given historical underdiagnosis.

### Morbidity and Functional Outcomes
- **Functional impact:** Lifelong intellectual disability (typically mild-to-moderate) with need for ongoing developmental/educational support; motor impairment (hypotonia, movement disorder) contributes to functional morbidity; a substantial subset experiences developmental regression.
- **Quality of life:** No validated disease-specific QoL instrument data published; burden is inferred from the combination of ID + ASD + epilepsy + sleep disturbance + anxiety, all independently associated with reduced QoL in neurodevelopmental disorders broadly.

### Disease Course / Complications
- **Complications:** Refractory or difficult-to-control epilepsy (notably DEE-SWAS/ESES) is the most clinically significant complication, directly associated with cognitive/language regression; scoliosis requiring orthopedic monitoring; ophthalmologic complications from untreated strabismus/refractive error; feeding/GI complications (GERD, vomiting).
- **Recovery potential:** With early intervention (developmental therapies, seizure control), stabilization of function is achievable; the regressive DEE-SWAS phenotype in particular may show partial recovery with EEG-directed antiepileptic/anti-inflammatory treatment (per general DEE-SWAS management principles extrapolated to this disorder, as GeneReviews and Kassabian et al. discuss).

### Prognostic Factors
- Presence of DEE-SWAS/ESES epilepsy appears to be the strongest identified prognostic factor for regression/worse cognitive trajectory.
- Severity of baseline ID correlates with likelihood of co-occurring ASD (moderate-severe ID more often associated with ASD).
- No molecular/biomarker-based prognostic classifier has yet been validated.

---

## 12. Treatment

There is **no disease-modifying or curative therapy**; management is entirely **supportive and symptom-directed**, per GeneReviews consensus recommendations.

### Pharmacotherapy
- **Anti-seizure medications (ASMs):** Standard epilepsy pharmacotherapy tailored to seizure type; for the DEE-SWAS/ESES subtype, ESES-directed regimens (e.g., corticosteroids/ACTH, or specific ASMs used for encephalopathy with spike-wave activation in sleep) may be considered, following general DEE-SWAS treatment principles rather than DLG4-specific trial data.
- **Migraine therapy:** Standard migraine treatment as clinically indicated.
- **Sleep pharmacotherapy:** Reserved for refractory sleep disturbance after behavioral measures.
- No pharmacogenomic (PharmGKB/CPIC) guidance specific to *DLG4* variants exists.
- Suggested NCIT term: **NCIT:C15986** (Pharmacotherapy), with `therapeutic_agent` specifying individual anti-seizure medications as used case-by-case.

### Advanced/Experimental Therapeutics
- No gene therapy, ASO, siRNA, or targeted molecular therapy has been reported or is in registered clinical trials specifically for DLG4-related synaptopathy as of current literature.
- No NCT-registered interventional trials specific to *DLG4* were identified via available search; research activity is centered on **natural history / registry studies** rather than therapeutic trials (see below).

### Non-Pharmacologic / Supportive Care
| Domain | Intervention | Suggested NCIT term |
|---|---|---|
| Developmental | Early intervention (birth–3 years), developmental preschool (3–5 years), individualized education plan (IEP) | NCIT:C49236 (Therapeutic Procedure) |
| Motor | Physical therapy, occupational therapy, adaptive devices | NCIT:C15302 (Physical Therapy) |
| Behavioral/ASD | Formal autism evaluation; Applied Behavior Analysis (ABA) therapy; ADHD/anxiety screening and management | NCIT:C15747 (Supportive Care) |
| Orthopedic | Monitoring/management of scoliosis; surgical referral if progressive | NCIT:C16186 (Orthopedic Surgical Procedure), as needed |
| Ophthalmologic | Annual ophthalmologic evaluation; correction of refractive error; low vision services | — |
| GI | Standard management of feeding difficulty, GERD, vomiting | — |
| Genetic | Genetic counseling for families | NCIT:C15240 (Genetic Counseling) |

### Treatment Strategy / Algorithms
Management follows a **multidisciplinary surveillance-and-support algorithm** as codified in GeneReviews:
- At every visit: assess for seizures, developmental progress, behavioral concerns (post-infancy), mobility/self-help skills, and sleep disturbance.
- Annually: ophthalmologic evaluation; consider 24-hour EEG based on clinical indicators (regression, cognitive plateau, suspected subclinical seizures).

### Experimental/Research Infrastructure
- The **DLG4 SHINE Foundation** (patient advocacy organization) coordinates natural history studies, a patient registry, and biospecimen collection in partnership with **Simons Searchlight** and other research groups, explicitly framed as the necessary first step toward future targeted-treatment development ("Finding Treatment of DLG4 Synaptopathy Starts with Registry," [dlg4shine.org](https://www.dlg4shine.org/what-is-registry)).

---

## 13. Prevention

Given the disorder's near-exclusively **de novo** genetic origin, classical primary/secondary/tertiary prevention paradigms (vaccination, lifestyle modification, screening programs) are **not applicable** in the traditional sense.

- **Primary prevention:** Not possible to prevent de novo germline mutation; population carrier screening is not relevant given the de novo mechanism.
- **Secondary prevention (reproductive counseling):**
  - **Genetic counseling** is central: recurrence risk for future pregnancies of parents of an affected (apparently de novo) proband is **low but not zero** (above general population risk) due to the possibility of parental germline mosaicism; recurrence risk rises to **50%** if a parent is confirmed to carry the variant (germline or somatic-germline mosaic, or, rarely, is mildly affected).
  - **Prenatal diagnosis and preimplantation genetic testing (PGT)** are available once the familial pathogenic variant is identified, allowing informed reproductive decision-making in subsequent pregnancies.
- **Tertiary prevention:** Aimed at reducing complications of the established disease — e.g., early EEG surveillance to catch DEE-SWAS/ESES before extensive regression occurs, annual ophthalmologic screening to prevent amblyopia from untreated strabismus/refractive error, and scoliosis monitoring to enable early orthopedic intervention.
- **Public health / behavioral / immunization strategies:** Not applicable — this is not an infectious, environmental, or lifestyle-driven condition.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** No naturally occurring veterinary/companion-animal disease attributable to spontaneous *Dlg4* mutation has been reported in OMIA or the veterinary literature; DLG4-related synaptopathy is a human-specific clinical entity as currently documented.
- **Orthologous gene:** *Dlg4* is conserved across vertebrates (mouse *Dlg4*, NCBI Gene) and has clear orthologs in zebrafish (*dlg4*, Gene ID referenced in GeneCards) and in Drosophila (*dlg*, "discs large," the founding member of the gene family, originally identified as a tumor suppressor).
- **Comparative biology:** The DLG-MAGUK gene family (*dlg1–dlg4* in vertebrates; single *dlg* in Drosophila) shows deep evolutionary conservation of function in organizing glutamatergic postsynaptic signaling complexes — from the Drosophila neuromuscular junction through to the mammalian cortical excitatory synapse — underscoring that PSD-95's core synaptic scaffolding role, and its vulnerability to haploinsufficiency-driven disease, is an ancient and conserved biological function.
- **Zoonotic potential:** Not applicable (not an infectious disease).

---

## 15. Model Organisms

### Mammalian Models
- **Mouse — *Dlg4⁻/⁻* (PSD-95 knockout) germline knockout:** The best-characterized model. Recapitulates behavioral features relevant to human ASD/anxiety phenotype: **increased repetitive behaviors, abnormal social and communication behaviors, impaired motor coordination, and increased stress reactivity**; molecular/anatomical correlates include subtle dysmorphology of amygdala dendritic spines and altered forebrain expression of synaptic genes ([PMID:20952458](https://pubmed.ncbi.nlm.nih.gov/20952458/); American Journal of Psychiatry, 2010).
- **Mouse — PDZ1/PDZ2 ligand-binding-deficient PSD-95 knock-in:** A domain-specific model showing impaired synaptic clustering of postsynaptic density proteins, altered synaptic signal transmission, and disrupted learning behavior in hippocampal neurons — directly informative for the mechanistic consequence of PDZ-domain-disrupting human variants ([PMC3575367](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3575367/)).
- **Model characteristics:** These murine models show reasonably good **face validity** for the core behavioral domains of the human disease (autism-relevant behaviors, motor coordination deficits) but, as a **complete knockout**, represent a more severe loss-of-function state than the heterozygous human condition; the PDZ-domain-specific knock-in more precisely models a partial/domain-restricted functional loss.
- **Model limitations:** Homozygous *Dlg4⁻/⁻* mice do not directly model the human **heterozygous haploinsufficiency** state (most human patients are heterozygous), so heterozygous *Dlg4⁺/⁻* mice would in principle be a more disease-relevant model; specific epilepsy/DEE-SWAS phenotypes and the marfanoid connective-tissue phenotype observed in humans have not been reported as recapitulated in existing mouse models.

### Invertebrate Models
- **Drosophila — *dlg* (discs-large) mutants:** The Drosophila glutamatergic neuromuscular junction (NMJ) model demonstrates that *dlg* is required for normal synapse structure, clusters postsynaptic glutamate receptor subunit composition, and mediates structural synaptic plasticity during postsynaptic target growth ([PMC545058](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC545058/); [PMC4658212](https://pmc.ncbi.nlm.nih.gov/articles/PMC4658212/)). This provides a genetically tractable system for dissecting fundamental DLG-MAGUK synaptic scaffolding function, though it models the ancestral single-paralog system rather than the vertebrate-specific compensatory context.

### Cellular / iPSC Models
- No published human iPSC-derived neuron model specific to *DLG4* patient variants was identified in the current literature search; this represents an identified research gap, and the DLG4 SHINE Foundation biospecimen-collection effort may support development of such models in the future.

### Resources
- Mouse Genome Informatics (MGI) — *Dlg4* allele records
- ZFIN — zebrafish *dlg4* records
- FlyBase — Drosophila *dlg* records
- International Mouse Phenotyping Consortium (IMPC) — potential source of additional *Dlg4* conditional/heterozygous allele phenotyping data (not specifically reviewed here)

---

## Summary of Key Evidence Gaps for Curation

1. **Genotype-phenotype correlation** remains unresolved — an active area of ongoing collaborative study (ERN-ITHACA call for collaboration; Kassabian et al. 2024).
2. **No approved or trial-stage disease-modifying therapy** exists; management is entirely supportive.
3. **Heterozygous (haploinsufficient) mouse models** more precisely matching the human genetic state, and human iPSC-neuron models, are not yet well represented in the published literature — an important caveat for any `HUMAN_MODEL_MISMATCH` discussion, since the best-characterized mouse data (Feyder et al. 2010) derive from a full knockout rather than a heterozygous model.
4. **Formal prevalence/incidence figures** and validated QoL instrument data are not yet available — current numbers (~100 individuals identified) reflect registry/cohort ascertainment rather than population-based epidemiology.
5. **DEE-SWAS/ESES epilepsy subtype** is the most clinically consequential and best-recently-characterized complication (Kassabian et al. 2024) and should be modeled as a distinct, evidence-rich pathophysiology/phenotype node given its strong association with developmental regression.

---

### Sources
- [DLG4-Related Synaptopathy — GeneReviews® (NCBI Bookshelf, NBK592682)](https://www.ncbi.nlm.nih.gov/books/NBK592682/)
- [DLG4-related synaptopathy: a new rare brain disorder — Genetics in Medicine (Rodríguez-Palmero et al., 2021)](https://www.nature.com/articles/s41436-020-01075-9) / [PubMed PMID:33597769](https://pubmed.ncbi.nlm.nih.gov/33597769/) / [ScienceDirect mirror](https://www.sciencedirect.com/science/article/pii/S1098360021014465)
- [Truncating variants of the DLG4 gene are responsible for intellectual disability with marfanoid features — Moutton et al., 2018, Clinical Genetics](https://onlinelibrary.wiley.com/doi/abs/10.1111/cge.13243)
- [Developmental epileptic encephalopathy in DLG4-related synaptopathy — Kassabian et al., 2024, Epilepsia](https://onlinelibrary.wiley.com/doi/abs/10.1111/epi.17876)
- [A deep intronic DLG4 variant resulting in DLG4-related synaptopathy — Levy et al., 2024, Clinical Genetics](https://onlinelibrary.wiley.com/doi/full/10.1111/cge.14411)
- [A novel DLG4 variant causes DLG4-related synaptopathy with intellectual regression — Human Genome Variation, 2023](https://www.nature.com/articles/s41439-023-00260-x) / [PMC10770362](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10770362/)
- [OMIM #618793 — Intellectual Developmental Disorder, Autosomal Dominant 62 (MRD62)](https://www.omim.org/entry/618793)
- [OMIM *602887 — DLG4](https://omim.org/entry/602887)
- [MedlinePlus Genetics — DLG4-related synaptopathy](https://medlineplus.gov/genetics/condition/dlg4-related-synaptopathy/)
- [Neurodevelopmental Disorders Associated with PSD-95 and Its Interaction Partners — PMC9025546](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9025546/) / [PubMed PMID:35457207](https://pubmed.ncbi.nlm.nih.gov/35457207/)
- [Association of Mouse Dlg4 (PSD-95) Gene Deletion and Human DLG4 Gene Variation With Phenotypes Relevant to ASD and Williams' Syndrome — Feyder et al., 2010, American Journal of Psychiatry / PubMed PMID:20952458](https://pubmed.ncbi.nlm.nih.gov/20952458/)
- [PSD-95 family MAGUKs are essential for anchoring AMPA and NMDA receptor complexes at the postsynaptic density — PNAS](https://www.pnas.org/doi/10.1073/pnas.1517045112)
- [Impaired synaptic clustering of postsynaptic density proteins... in PDZ1 and PDZ2 ligand binding-deficient PSD-95 knockin mice — PMC3575367](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3575367/)
- [Acute Inactivation of PSD-95 Destabilizes AMPA Receptors at Hippocampal Synapses — PMC3546964](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3546964/)
- [Discs-large (DLG) is clustered by presynaptic innervation and regulates postsynaptic glutamate receptor subunit composition in Drosophila — PMC545058](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC545058/)
- [The Drosophila tumor suppressor gene, dlg, is involved in structural plasticity at a glutamatergic synapse — PMC4658212](https://pmc.ncbi.nlm.nih.gov/articles/PMC4658212/)
- [DLG4 SHINE Foundation — Natural History Studies / Registry](https://www.dlg4shine.org/natural-history-studies)
- [Simons Searchlight — DLG4](https://www.simonssearchlight.org/research/what-we-study/dlg4/)
- [ERN-ITHACA — Genotype-phenotype characterization of DLG4-related synaptopathy (call for collaboration)](https://ern-ithaca.eu/for-clinicians/calls-for-collaboration/genotype-phenotype-characterization-of-dlg4-related-synaptopathy/)
- MONDO:0032919 (confirmed via EBI OLS4 MONDO ontology search; exact synonym "DLG4-related synaptopathy")

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| Quoted claims checked | 4 |
| Quoted claims found in source | 3 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 13 |
| On topic | 8 |
| Off topic | 2 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `DOI:10.1111/cge.14411](https://onlinelibrary.wiley.com/doi/full/10.1111/cge.14411` (1 mention) - Identifier did not resolve to a record

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `DOI:10.1073/pnas.1517045112` *(abstract only)*: "essential for anchoring AMPA and NMDA receptor complexes at the postsynaptic density"
  - closest text in source: "Significance The postsynaptic density (PSD) at the glutamatergic excitatory synapse is a macromolecular machine that underlies synaptic transmission and information storage"

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `DOI:10.1073/pnas.1517045112` (3 mentions) - PSD-95 family MAGUKs are essential for anchoring AMPA and NMDA receptor complexes at the postsynaptic density
  - shared terms: psd-95, postsynaptic
- `PMC:PMC3546964` (5 mentions) - Acute inactivation of PSD-95 destabilizes AMPA receptors at hippocampal synapses.
  - shared terms: psd-95, postsynaptic

Weighed against this report's own most characteristic terms: `disorder`, `dlg4`, `epilepsy`, `phenotype`, `developmental`, `variant`, `dee-swas`, `genetic`, `gene`, `synaptopathy`, `intellectual`, `psd-95`, `clinical`, `regression`, `eses`, `kassabian`, `identified`, `disability`, `postsynaptic`, `associated`.