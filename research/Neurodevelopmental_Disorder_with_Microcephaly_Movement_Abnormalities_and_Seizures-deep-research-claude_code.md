---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-18T15:06:20.051955'
end_time: '2026-08-18T15:11:28.286073'
duration_seconds: 308.23
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Neurodevelopmental Disorder with Microcephaly, Movement Abnormalities,
    and Seizures
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
  web_search_requests: 10
  num_turns: 16
  total_cost_usd: 1.8154706000000003
  session_id: 412a89b8-c3df-54e4-9b0f-2a4177b05f0a
  stop_reason: end_turn
  assistant_text_blocks: 3
citation_count: 12
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 0
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:41308990
  relevance_assessed: 6
  on_topic: 5
  needs_review: true
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neurodevelopmental Disorder with Microcephaly, Movement Abnormalities, and Seizures
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Neurodevelopmental Disorder with Microcephaly, Movement Abnormalities, and Seizures** covering all of the
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

I'll research this specific disorder using web search and authoritative databases to build the report.

Excellent, this is very rich data. Let me follow up on the redirect and gather additional details on genetics, epidemiology, and related resources.

I now have sufficient primary-literature detail to compile the comprehensive report.

# Neurodevelopmental Disorder with Microcephaly, Movement Abnormalities, and Seizures (NEDMIMS) — Comprehensive Research Report

---

## 1. Disease Information

**Overview.** Neurodevelopmental disorder with microcephaly, movement abnormalities, and seizures (NEDMIMS) is a rare, severe, autosomal recessive Mendelian neurodevelopmental disorder first delineated in 2022. It is caused by biallelic (homozygous or compound-heterozygous) loss-of-function variants in **CHKA** (choline kinase alpha), the gene encoding the rate-limiting first enzyme of the CDP-choline (Kennedy) pathway for phosphatidylcholine biosynthesis. The disorder is defined by severe global developmental delay/intellectual disability apparent from infancy, progressive (often profound) microcephaly, early-onset — frequently treatment-refractory — epilepsy, and a spectrum of movement abnormalities (hypertonia, hypotonia, hyperreflexia, dystonia/dyskinesia, choreoathetosis) ([Klöckner et al. 2022, *Brain*, PMID:35202461](https://academic.oup.com/brain/article/145/6/1916/6535865); [PMC9630884](https://pmc.ncbi.nlm.nih.gov/articles/PMC9630884/)).

**Key identifiers:**
| Resource | Identifier |
|---|---|
| OMIM (phenotype) | **#620023** — NEURODEVELOPMENTAL DISORDER WITH MICROCEPHALY, MOVEMENT ABNORMALITIES, AND SEIZURES; NEDMIMS |
| OMIM (gene) | **\*118491** — CHOLINE KINASE, ALPHA; CHKA |
| Gene locus | 11q13.2 |
| HGNC | CHKA (HGNC:1937) |
| UniProt | P35790 |
| EC number | 2.7.1.32 (choline kinase); CHKA also has EC 2.7.1.82 (ethanolamine kinase) activity |
| MedGen | Concept ID **C5774208** |
| Inheritance | Autosomal recessive |
| ICD-10/ICD-11 | No disease-specific code; falls under general categories such as ICD-10-CM F88/F89 (disorders of psychological development) and Q02 (microcephaly) pending disorder-specific coding |

**Synonyms/alternative names:** NEDMIMS; CHKA-related neurodevelopmental disorder; CHKA deficiency; "neurodevelopmental disorder with epilepsy and microcephaly" (the descriptive title used in the founding publication before the OMIM-assigned acronym).

**Basis of evidence.** All currently published clinical knowledge is derived from **aggregated individual-patient case series** (n=6 across 5 families in the founding report, expanded functional/mechanistic work in follow-up studies), not registry- or EHR-level aggregated epidemiology. There is no disease registry, and prevalence/incidence estimates are not available (see Section 9).

---

## 2. Etiology

**Disease causal factors.** NEDMIMS is a monogenic, purely genetic disorder — no environmental, infectious, or acquired etiology has been implicated. Disease is caused by **biallelic loss-of-function variants in CHKA** that reduce choline kinase alpha enzymatic activity below a threshold compatible with normal phospholipid membrane biogenesis, particularly in the developing CNS (PMID:35202461).

**Genetic risk factors:**
- **Causal variants**: missense, frameshift, and start-loss variants in CHKA (detailed in Section 4). All six founding-cohort variants were assessed as pathogenic per ACMG/AMP criteria.
- **Consanguinity** is a strong risk factor: 4 of 5 founding families were consanguineous (Iranian, Indian, Egyptian, Bangladeshi backgrounds), consistent with autosomal recessive inheritance and regional consanguinity rates; one family (German) was non-consanguineous with compound-heterozygous variants (PMC9630884).
- **Modifier genes**: none established to date; sample size (n=6) is too small for modifier-gene discovery.

**Protective factors:** None reported in the literature — no protective variants, alleles, or environmental exposures have been described for CHKA-related disease. This is unsurprising for a newly delineated ultra-rare recessive disorder with a small case series.

**Gene-environment interactions:** Not studied; no data available. Given the pathway's link to choline (an essential dietary nutrient obtained partly from diet and partly synthesized via PEMT), a theoretical interaction between dietary choline intake and disease severity has not been formally investigated but is biologically plausible given the mechanism (Section 6).

---

## 3. Phenotypes

Phenotype data are drawn from the 6-individual/5-family founding cohort (PMID:35202461); frequencies below are calculated over this cohort and should be treated as provisional given the very small sample size.

| Phenotype | Type | Frequency | Onset | HPO term (suggested) |
|---|---|---|---|---|
| Severe global developmental delay / intellectual disability | Clinical/behavioral | 6/6 (100%) | Infancy | HP:0001263 (Global developmental delay) / HP:0001249 (Intellectual disability) |
| Progressive microcephaly | Physical sign | 6/6 (100%); severity range −3.3 to −7 SD | Infancy, progressive | HP:0000252 (Microcephaly) / HP:0005484 (Postnatal progressive microcephaly) |
| Epilepsy / early-onset seizures | Symptom | 6/6 (100%); often refractory | Infancy (as early as neonatal in some; onset up to ~3 y in Individual 2) | HP:0001250 (Seizure) |
| Epileptic spasms / West syndrome | Symptom subtype | present in ≥1 individual (Individual 4) | Infancy | HP:0011097 (Epileptic spasm) / HP:0012469 (Infantile spasms) |
| Absent speech / no language development | Behavioral | 6/6 or near-universal | From infancy | HP:0001344 (Absent speech) |
| Failure to achieve independent walking | Motor | 5/6 (one individual achieved assisted walking at age 3) | Persistent | HP:0002540 (Inability to walk) |
| Hypertonia | Movement abnormality | present in multiple individuals | Variable | HP:0001276 (Hypertonia) |
| Hypotonia | Movement abnormality | present in multiple individuals | Variable/overlapping with hypertonia in different individuals | HP:0001252 (Hypotonia) |
| Hyperreflexia | Sign | 5/6 (83%) | — | HP:0001347 (Hyperreflexia) |
| Dystonia / dyskinesia / choreoathetosis | Movement abnormality | present (Individuals 4, 5) | — | HP:0001332 (Dystonia); HP:0002273 (Dyskinesia); HP:0002270 (Chorea) |
| Cerebral palsy-like picture | Motor | present (Individual 1.1) | — | HP:0100021 (Cerebral palsy) |
| Nystagmus | Ocular sign | 3/6 (50%) | — | HP:0000639 (Nystagmus) |
| Retinal dysfunction / retinal pigment epithelium changes / cortical visual loss | Ophthalmologic | present (Individual 3) | — | HP:0000546 (Retinal degeneration); HP:0000556 (Retinal dystrophy); HP:0100704 (Cerebral visual impairment) |
| Developmental regression | Symptom | present (Individual 3) | — | HP:0002376 (Developmental regression) |
| Autistic features | Behavioral | present (Individual 3) | — | HP:0000717 (Autism) |
| Behavioral problems (aggression, self-injury, sleep disturbance) | Behavioral | present in a subset | — | HP:0000718 (Aggressive behavior); HP:0002171 (Gliosis — n/a); HP:0002360 (Sleep disturbance) |
| Hypomyelination / thin corpus callosum / white matter signal change on MRI | Neuroimaging | present in a subset | — | HP:0003429 (Hypomyelination); HP:0002079 (Hypoplasia of the corpus callosum) |

**Severity/progression.** The disorder is uniformly severe with global, non-remitting impairment; microcephaly is progressive (postnatal, worsening with age) rather than static/congenital-only. Motor and cognitive outcomes are profoundly impaired in essentially all reported individuals, with one partial exception (Individual 1.2 achieving assisted walking by age 3). Phenotypic severity correlates inversely with residual CHKA enzymatic activity measured in the yeast complementation assay (Section 4) — individuals with ~15–20% residual activity (homozygous missense) had severe phenotypes, and net-activity estimates were used post hoc to explain compound-heterozygous genotype severity.

**Quality of life impact.** Not formally measured with validated instruments (EQ-5D, SF-36) in the literature; qualitatively, the disorder is described as causing profound, lifelong dependency — absent speech, absent independent ambulation in nearly all cases, and behavioral/sleep disturbance burden on caregivers.

---

## 4. Genetic/Molecular Information

**Causal gene.** CHKA (choline kinase alpha), OMIM \*118491, HGNC:1937, chromosome 11q13.2, UniProt P35790.

**Reported pathogenic variants (founding cohort, PMID:35202461):**

| Individual(s) | cDNA change | Protein change | Variant type | Zygosity | Ethnic background/consanguinity | gnomAD |
|---|---|---|---|---|---|---|
| 1.1, 1.2, 2 | c.421C>T | p.(Arg141Trp) | Missense | Homozygous | Iranian (1.1/1.2), Indian (2) — consanguineous | Heterozygous carrier ×1 in gnomAD |
| 3 | c.580C>T | p.(Pro194Ser) | Missense | Homozygous | Egyptian — consanguineous | Heterozygous carrier ×1 in gnomAD |
| 4 | c.14dup / c.1021T>C | p.(Cys6Leufs\*19) / p.(Phe341Leu) | Frameshift + missense | Compound heterozygous | German — non-consanguineous | Absent in gnomAD |
| 5 | c.2T>C | p.(Met1?) | Start-loss | Homozygous | Bangladeshi — consanguineous | Absent in gnomAD |

**Variant classification:** All variants classified as **pathogenic** per ACMG/AMP guidelines; missense variants affect highly conserved residues, with multiple *in silico* predictors (and functional assays) supporting pathogenicity.

**Functional consequences (yeast complementation assay in choline-kinase-deficient *cki1Δ S. cerevisiae*):**
- Wild-type CHKA: 100% activity (reference)
- p.(Arg141Trp): ~20–25% residual activity
- p.(Pro194Ser): ~15–17% residual activity
- p.(Phe341Leu): ~50% residual activity
- p.(Cys6Leufs\*19): predicted null allele via nonsense-mediated decay
- p.(Met1?): start-loss predicted to remove ~26% of the N-terminal protein if reinitiated at the next in-frame methionine (residue 123)

All variants are consistent with a **loss-of-function** mechanism (PMC9630884).

**Structural basis (protein modeling):**
- p.(Arg141Trp) lies near the ADP-binding site; Arg141 normally forms stabilizing hydrogen bonds with Pro130 and Thr133, lost upon substitution.
- p.(Pro194Ser) also lies near the ADP-binding site and introduces steric clashes from altered side-chain geometry.
- p.(Phe341Leu) lies in the hydrophobic cluster forming the choline-binding pocket; substitution reduces hydrophobic interactions needed for substrate binding.

**Modifier genes:** None identified.

**Epigenetic information:** No CHKA-specific DNA methylation/histone modification data are reported in the disease literature.

**Chromosomal abnormalities:** None reported; disease is caused by point/small indel variants, not large structural rearrangements.

**Allelic/pathway-related disorders (Kennedy pathway paralogs):** CHKA shares its enzymatic step with its paralog **CHKB** (choline kinase beta), whose biallelic loss-of-function variants cause a **distinct** disorder — megaconial-type congenital muscular dystrophy (MDCMC, OMIM #602541) — with progressive muscular weakness and cardiomyopathy rather than the CNS-predominant NEDMIMS phenotype, illustrating tissue-specific non-redundancy despite shared catalytic function (PMID:35202461). Other Kennedy-pathway genes associated with recessive disease include **PCYT1A** (bone abnormalities with cone-rod dystrophy), **PCYT2** and **SELENOI** (hereditary spastic paraplegia).

---

## 5. Environmental Information

- **Environmental factors:** None identified as causal or modifying; NEDMIMS is a purely monogenic disorder.
- **Lifestyle factors:** Dietary choline intake has not been formally studied as a modifier of phenotype severity, though it is biologically plausible given the pathway's substrate dependence (see Section 12, choline supplementation discussion).
- **Infectious agents:** Not applicable — no infectious trigger or contributor identified.

---

## 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream):**

1. **Molecular trigger:** Biallelic CHKA loss-of-function variant → reduced/absent choline kinase alpha catalytic activity.
2. **Biochemical consequence:** CHKA "catalyses the first step of phospholipid synthesis in the Kennedy pathway," phosphorylating choline (and, less efficiently, ethanolamine) using ATP to generate phosphocholine (and phosphoethanolamine) + ADP (PMID:35202461). Loss of activity → markedly reduced phosphocholine (17–28% of control levels in patient fibroblasts) and downstream **phosphatidylcholine (PC) reduced ~75%** compared to controls; glycerophosphocholine (GPC) also reduced to ~30% of control (Tavasoli et al., PMID:41308990; PMC12800699).
3. **Compensatory cellular response:** Diminished PC synthesis triggers **enhanced nuclear-envelope translocation and activation of CCTα** (CTP:phosphocholine cytidylyltransferase alpha, the pathway's rate-limiting downstream enzyme), described as "a compensatory activation of CCTα at the inner nuclear membrane, likely as an adaptive response to restore PC synthesis" (PMID:41308990).
4. **Organelle/cellular consequence:** Altered mitochondrial morphology (fragmented mitochondria, reduced aspect ratio/form factor) and mitochondrial dysfunction — increased basal respiration when normalized to DNA content but reduced when normalized to mitochondrial mass, indicating a genuine bioenergetic defect rather than simple mitochondrial proliferation.
5. **Oxidative damage cascade:** Mitochondrial dysfunction → elevated mitochondrial superoxide (detected by MitoSOX staining) and reactive oxygen species (ROS) → increased **lipid peroxidation** (confirmed by C11-BODIPY fluorescence shift) in CHKA-variant patient fibroblasts. This links a primary lipid-synthesis defect to secondary oxidative cellular injury — a mechanistically novel finding for this pathway (PMID:41308990).
6. **Tissue/clinical consequence:** In the CNS, impaired membrane phospholipid biogenesis during critical periods of neurodevelopment (myelination, synaptogenesis, neuronal membrane growth) is proposed to underlie microcephaly, epileptogenesis, and the movement/motor phenotype. Notably, in muscle biopsy from one compound-heterozygous individual, mitochondria showed altered morphology (dense, enlarged, broadened cristae) on electron microscopy, but overt mitochondrial *functional* impairment was not detected by histochemistry in that tissue, suggesting some tissue-specificity in downstream consequences.

**Tissue selectivity puzzle:** Despite CHKA and CHKB sharing "similar molecular structure and catalys[ing] the same reaction in PC/PE biosynthesis, the phenotypic differences might be explained by different expression patterns throughout different tissues in the body" — CHKB loss predominantly affects skeletal/cardiac muscle (megaconial muscular dystrophy) whereas CHKA loss predominantly affects the developing CNS, implying CHKA is the physiologically dominant/non-redundant choline kinase isoform in brain (PMID:35202461).

**Suggested ontology terms:**
- **GO (molecular function):** GO:0004103 (choline kinase activity); GO:0004305 (ethanolamine kinase activity)
- **GO (biological process):** GO:0006656 (phosphatidylcholine biosynthetic process); GO:0006580 (ethanolamine metabolic process); GO:0034599 (cellular response to oxidative stress); GO:0007005 (mitochondrion organization)
- **GO (cellular component):** GO:0005739 (mitochondrion); GO:0005730 (nucleolus/nuclear envelope — for CCTα translocation); GO:0016020 (membrane)
- **CHEBI:** CHEBI:15354 (choline); CHEBI:18132 (phosphocholine); CHEBI:49183 (1,2-diacyl-sn-glycero-3-phosphocholine, i.e., phosphatidylcholine); CHEBI:456216 (ADP); CHEBI:26689 (reactive oxygen species — informal)
- **CL (cell type):** CL:0000540 (neuron); CL:0002319 (neural cell); CL:0000031 (neuroblast, for developmental relevance); dermal fibroblast (CL:0002620) for the patient-derived model system

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Central nervous system (brain) — cerebral cortex (microcephaly, developmental delay/ID), and diffusely affected white matter (hypomyelination in a subset).
- **Secondary:** Peripheral/central motor system (movement abnormalities, hyper/hypotonia); visual system (retina/cortical visual pathways in Individual 3); skeletal muscle (mitochondrial ultrastructural changes noted on biopsy in one individual, though without overt myopathy).
- **Body systems involved:** Nervous system (primary); ophthalmologic system (secondary, in a subset); musculoskeletal system (secondary, tone/motor).

**Tissue and cell level:**
- Neurons (developing cortical/subcortical neurons) — presumed primary target given the neurodevelopmental phenotype.
- Oligodendrocytes/myelinating glia — implicated by hypomyelination findings on MRI in a subset.
- Retinal pigment epithelium and photoreceptors — implicated in Individual 3's retinal dysfunction.
- Dermal fibroblasts — used as the tractable patient-derived cellular model in mechanistic studies (not a primary disease tissue but the experimental surrogate).
- Skeletal muscle fibers/mitochondria — altered ultrastructure noted on EM in one individual.

**Subcellular level:**
- Mitochondria (fragmented morphology, altered cristae, elevated ROS) — GO:0005739
- Nuclear envelope / inner nuclear membrane (site of compensatory CCTα translocation) — GO:0005637 (nuclear inner membrane)
- Plasma membrane and other cellular membranes (substrate for PC incorporation) — GO:0016020

**Localization:**
- Diffuse/bilateral CNS involvement (microcephaly is global, not focal); no reported lateralization or asymmetry.
- Suggested UBERON terms: UBERON:0000955 (brain); UBERON:0001851 (cortex); UBERON:0002037 (cerebellum, if ataxia/movement features implicate it); UBERON:0000966 (retina); UBERON:0001134 (skeletal muscle tissue).

---

## 8. Temporal Development

**Onset:** Congenital/infantile — developmental delay and progressive microcephaly are apparent from infancy in all reported individuals; seizure onset ranges from the neonatal/early infantile period up to approximately age 3 years in at least one individual (Individual 2). Onset pattern is insidious/progressive rather than acute.

**Progression:**
- Microcephaly is explicitly **progressive** (postnatal head-circumference deceleration), not merely congenital, ranging from −3.3 SD to −7 SD across the cohort.
- Developmental trajectory is one of severe, essentially static-to-progressive impairment; one individual (Individual 3) showed frank **developmental regression** with emergence of autistic features and retinal dysfunction, suggesting the disorder can have a neurodegenerative component in some patients rather than purely static encephalopathy.
- Epilepsy is often refractory/treatment-resistant and persists chronically.
- No formal staging system exists (too few patients, too recently described).

**Patterns:**
- No spontaneous remission reported.
- No "critical period" intervention data exist yet; the mechanistic link to membrane phospholipid synthesis during neurodevelopment suggests early gestational/infantile periods are biologically critical, but this is inferential, not directly demonstrated in humans.
- Disease course to date has been described only in pediatric/young patients (oldest reported individual ~11.5 years); long-term (adult) natural history is unknown.

---

## 9. Inheritance and Population

**Epidemiology:** NEDMIMS is an **ultra-rare** disorder. No formal prevalence or incidence estimates exist — only 6 individuals from 5 families have been reported in the peer-reviewed literature to date (as of the most recent 2025/2026 mechanistic follow-up study). Given the extreme rarity, it likely falls in an Orphanet "not yet documented" prevalence class, though no dedicated ORPHA number was identified in currently available Orphanet resources.

**Inheritance pattern:** Autosomal recessive (OMIM #620023).

**Penetrance:** Appears to be complete/high in reported biallelic carriers (all reported affected homozygotes/compound heterozygotes are symptomatic), but the sample size (n=6) is far too small for a rigorous penetrance estimate.

**Expressivity:** Variable — phenotypic severity differs somewhat across individuals and correlates with residual enzymatic activity (e.g., ~15–20% activity in homozygous missense cases vs. ~25% net activity in the compound-heterozygous case), and specific features (retinal involvement, developmental regression, degree of motor achievement) vary between individuals even with the same genotype (e.g., discordance between Individuals 1.1 and 1.2, who share the identical homozygous variant but differ somewhat in motor outcome).

**Genetic anticipation:** Not applicable/not reported (not a repeat-expansion disorder).

**Germline mosaicism:** Not specifically reported.

**Founder effects:** Not established; the recurrent p.(Arg141Trp) variant was found in unrelated Iranian and Indian consanguineous families, which could reflect either a low-level founder effect, a mutational hotspot, or simply a commonly ascertained pathogenic missense change — not formally distinguished in the literature.

**Consanguinity role:** Substantial — 4 of 5 founding families were consanguineous, consistent with autosomal recessive inheritance in an ultra-rare gene.

**Carrier frequency:** Both recurrent missense alleles [p.(Arg141Trp), p.(Pro194Ser)] were each observed as a single heterozygous carrier in gnomAD population data, consistent with extreme rarity in the general population; the frameshift and start-loss alleles were absent from gnomAD entirely.

**Population demographics:** Reported affected individuals originate from Iranian, Indian, Egyptian, Bangladeshi, and German backgrounds — indicating the disorder is not confined to a single ethnic group, though the consanguinity-enriched ascertainment (4/5 families) likely reflects referral/diagnostic bias toward populations with higher consanguinity rates rather than true geographic clustering. No sex predilection has been noted (small sample includes both sexes, exact ratio not detailed in available sources). Age distribution of reported/diagnosed individuals spans early childhood to early adolescence (~2 to ~11.5 years at report).

---

## 10. Diagnostics

**Clinical tests:**
- **Brain MRI:** Findings in a subset include hypomyelination, thin corpus callosum, and nonspecific white matter T2/FLAIR signal change; some individuals had normal or only subtly abnormal imaging, so imaging is supportive but not diagnostic.
- **EEG:** Documents seizure semiology consistent with epileptic spasms, focal, generalized, and myoclonic seizure types; hypsarrhythmia would be expected in the individual with West syndrome (Individual 4).
- **Ophthalmologic exam:** Retinal pigment epithelium changes and cortical visual impairment identified in Individual 3 via fundoscopy/electroretinography (implied but not explicitly detailed as ERG in available excerpts).
- **Muscle biopsy with electron microscopy:** Performed in one individual (4), showing altered mitochondrial ultrastructure (dense matrix, broadened cristae) without overt functional impairment — a research/diagnostic-adjunct finding rather than a routine diagnostic test.
- **Biomarkers:** No validated clinical biomarker yet exists; research-grade lipidomic findings (reduced phosphocholine, phosphatidylcholine, and glycerophosphocholine in patient fibroblasts) are investigational and not yet translated into a clinical diagnostic assay.

**Genetic testing:**
- **Diagnosis is made by molecular genetic testing** — given the disorder's genetic and phenotypic heterogeneity overlap with dozens of other autosomal recessive microcephaly/epilepsy syndromes (see Section 1's list of phenotypically similar OMIM entries: NEDMAS/SARS1, NEDHYMS/ADARB1, NDMSCA/VARS1, MCSZ/PNKP, etc.), **exome or genome sequencing** (as part of a developmental delay/epilepsy/microcephaly gene panel or trio-WES/WGS) is the practical diagnostic approach, as CHKA is not yet a standard single-gene test target given its recent (2022) disease association.
- **Gene panels:** CHKA should be considered for inclusion in comprehensive "microcephaly + epilepsy + developmental delay" NGS panels; not yet universally included given its recent discovery.
- **Single-gene testing:** Reasonable only for confirmation after familial variant identification (e.g., prenatal/carrier testing in a family with a known proband).
- **Chromosomal microarray/karyotype/FISH:** Not informative for this single-gene point-variant disorder but often performed as part of standard first-tier developmental-delay workup to exclude copy-number etiologies before/alongside sequencing.
- **Functional/research confirmation:** Yeast complementation enzymatic activity assay was used in the discovery cohort to confirm variant pathogenicity; not a clinical diagnostic test but informative for variant classification in research/reference laboratories.

**Omics-based diagnostics:** Not yet part of routine clinical diagnosis; lipidomic/metabolomic profiling (phosphocholine, PC, GPC levels) is investigational, described in PMID:41308990, and could plausibly develop into a future biochemical screening adjunct.

**Clinical criteria:** No formal consensus diagnostic criteria (DSM/ICD-specific) exist yet, given the disorder's recent delineation; diagnosis rests on the combination of (a) severe global DD/ID from infancy, (b) progressive microcephaly, (c) early-onset epilepsy, (d) movement abnormalities, and (e) confirmatory biallelic CHKA variants.

**Differential diagnosis:** The extensive list of similarly named OMIM "neurodevelopmental disorder with microcephaly + seizures/movement" entries constitutes the core differential, including:
- NEDMAS (SARS1, OMIM #617709) — microcephaly, ataxia, seizures
- NEDHYMS (ADARB1, OMIM #618862) — hypotonia, microcephaly, seizures
- NDMSCA (VARS1) — microcephaly, seizures, cortical atrophy
- MCSZ (PNKP) — microcephaly, seizures, developmental delay
- NEDMILG (OMIM #619091) — microcephaly, impaired language, gait abnormalities
- NEDMCMS (OMIM #618730) — microcephaly, cortical malformations, spasticity
- NDMSBA (OMIM #617527) — progressive microcephaly, spasticity, brain anomalies
- NEDSMBA (OMIM #620024) — seizures, microcephaly, brain abnormalities
- NMIHBA (OMIM #617481) — microcephaly, hypotonia, variable brain anomalies
- CHKB-related megaconial muscular dystrophy (distinguishable by predominant myopathy/cardiomyopathy rather than CNS-predominant phenotype)

**Screening:** No newborn screening, carrier screening panel, or population-level screening program currently exists for CHKA given its extreme rarity and recent discovery; carrier screening could be offered on a family-specific basis once a proband's variants are known.

---

## 11. Outcome/Prognosis

**Survival and mortality:** No mortality data reported in the literature to date; all reported individuals were alive at time of publication (ages ~2 to ~11.5 years). Long-term/adult survival and life expectancy are unknown due to the very recent disease description and young age of the reported cohort.

**Morbidity and function:** Uniformly severe — profound global developmental impairment, absent expressive language in essentially all individuals, and failure to achieve independent ambulation in the large majority (5/6), with one exception achieving assisted (not independent) walking by age 3. No quality-of-life instrument data (EQ-5D, SF-36, PROMIS) have been published.

**Disease course:** Chronic, non-remitting; epilepsy is frequently treatment-refractory. One individual (3) exhibited a regressive course with loss of skills, emergence of autistic features, and progressive retinal/visual dysfunction, suggesting the disease can manifest with a degenerative component in a subset of patients rather than purely static encephalopathy for all.

**Complications:** Refractory epilepsy; behavioral complications (aggression, self-injurious behavior, sleep disturbance) reported in a subset; visual impairment/cortical visual loss in at least one individual.

**Prognostic factors:** Residual CHKA enzymatic activity (as measured in the yeast functional assay) appears to correlate with phenotypic severity — lower residual activity (~15–20%) associates with the most severe presentations, while somewhat higher net activity (compound heterozygote, ~25%) was associated with a comparably severe but not clearly milder phenotype in the one such case reported, so this genotype-phenotype correlation remains tentative given the small sample.

**Prognostic biomarkers:** None validated clinically; research-grade biochemical markers (reduced PC, phosphocholine, GPC; elevated ROS/lipid peroxidation) are candidates for future prognostic or therapeutic-monitoring biomarkers but are not yet clinically deployed.

---

## 12. Treatment

**Current status: no disease-specific approved therapy exists.** The founding clinical report (PMID:35202461) does not describe specific treatments or management strategies beyond diagnostic identification; management is presumed to be supportive/symptomatic, following standard practice for severe developmental and epileptic encephalopathies (anti-seizure medications selected per seizure semiology, physical/occupational/speech therapy, nutritional and orthopedic supportive care), though no CHKA-specific published treatment protocol exists.

**Suggested general NCIT supportive-care terms (extrapolated from standard DEE management, not disease-specific literature):**
- NCIT:C15986 (Pharmacotherapy) — for anti-seizure medications
- NCIT:C15747 (Supportive Care)
- NCIT:C15302 (Physical Therapy)
- NCIT:C121351-type Occupational Therapy / NCIT:C159273 (Speech Therapy)
- NCIT:C15240 (Genetic Counseling) — relevant given autosomal recessive inheritance and consanguinity risk in affected families

**Emerging/investigational mechanistic leads (preclinical, not yet clinical therapy):**
- **Mitochondrial uncoupling (FCCP):** In patient-derived fibroblasts, treatment with the mitochondrial uncoupler FCCP "significantly reduced ROS levels and lipid peroxidation to a level similar to fibroblasts from controls" (PMID:41308990), suggesting mitochondrial-targeted antioxidant/uncoupling strategies as a **potential future therapeutic avenue** to mitigate downstream oxidative damage — though the authors note uncertainty as to whether this would restore phospholipid synthesis itself, and this remains a cell-culture finding with no in vivo or clinical translation yet.
- **Choline/CDP-choline (citicoline) supplementation:** Not directly tested in CHKA-deficient patients or models in the available literature, but is biologically plausible as a substrate-augmentation strategy given the pathway mechanism; citicoline is already used clinically (Europe/Asia) for unrelated indications (cognitive impairment post-stroke, traumatic brain injury), establishing safety precedent, but no CHKA-specific trial has been conducted. This should be considered a **hypothesis-generating**, not evidence-based, treatment avenue.

**Experimental treatments in clinical trials:** None identified — no registered ClinicalTrials.gov or WHO ICTRP trial specifically targets CHKA-related NEDMIMS as of current literature.

**Treatment outcomes/side effects:** Not applicable — no disease-specific therapy has been trialed.

**Treatment strategy/algorithms:** None established; management remains individualized and symptom-directed, following general pediatric neurology practice for developmental and epileptic encephalopathies of genetic etiology.

---

## 13. Prevention

**Primary prevention:** Given autosomal recessive inheritance and the substantial role of consanguinity in the founding cohort, **genetic counseling** for consanguineous couples or those with a family history of a similarly affected child is the principal available primary-prevention strategy. Carrier screening (once a family's specific pathogenic variants are known) can inform reproductive decision-making.

**Secondary prevention (screening/early detection):** No population or targeted newborn screening program exists; early detection currently relies on clinical suspicion (infantile developmental delay + progressive microcephaly + seizures) triggering diagnostic genetic testing (exome/genome sequencing).

**Genetic screening:** Prenatal diagnosis (chorionic villus sampling/amniocentesis with targeted variant testing) and preimplantation genetic testing (PGT-M) are technically feasible once familial pathogenic variants are identified, following standard practice for known autosomal recessive Mendelian disorders, though no CHKA-specific prenatal-testing case has been published.

**Risk stratification:** Formal risk-prediction models do not exist; risk is determined by empiric recurrence risk (25% per pregnancy for two known carrier parents, consistent with autosomal recessive inheritance).

**Behavioral interventions:** None specific to primary prevention of this genetic disorder.

**Counseling:** Genetic counseling is the central actionable preventive intervention, particularly relevant given the disorder's enrichment in consanguineous unions; counseling should address recurrence risk, the option of carrier testing for at-risk relatives, and reproductive options (prenatal diagnosis, PGT-M, or informed family planning).

**Public health/environmental interventions:** Not applicable — no environmental or infectious component to prevent.

**Prophylaxis:** No pharmacologic prophylaxis is established; any future role for dietary choline supplementation as a preventive/mitigating strategy remains entirely speculative and unstudied in this disorder.

---

## 14. Other Species / Natural Disease

**Naturally occurring disease in other species:** No naturally occurring CHKA-deficiency disease has been reported in companion animals or wildlife (e.g., no OMIA entry identified in the literature reviewed). This is consistent with the disorder's very recent human discovery (2022) and its ultra-rare status.

**Comparative biology:** The Kennedy pathway and choline kinase enzymology are highly conserved across mammals, which is what makes the mouse knockout data (below) directly informative for human disease mechanism, but no spontaneous veterinary disease model has been documented.

**Transmission:** Not applicable — purely genetic, non-communicable disorder; no zoonotic potential.

---

## 15. Model Organisms

**Mouse models (the only animal model system reported to date):**
- ***Chka⁻/⁻* (homozygous knockout) mice:** **Embryonically lethal**, indicating that complete loss of Chka is incompatible with mammalian development — underscoring that all human disease-causing CHKA variants must be hypomorphic (partial loss-of-function) rather than complete null, consistent with the residual 15–50% enzymatic activity measured for all tested human missense/compound-heterozygous alleles (PMID:35202461).
- ***Chka⁺/⁻* (heterozygous) mice:** Viable, showing ~30% reduction in choline kinase activity; identified through a large-scale mouse phenotyping screen as one of **198 mouse lines with neuroanatomical phenotypes**, supporting CNS relevance of partial Chka dosage reduction even in the heterozygous state in mice (a genetic dosage-sensitivity finding relevant to interpreting human hypomorphic variants).
- ***Chkb⁻/⁻* (paralog knockout) mice:** Show progressive muscular weakness, phenotypically paralleling the human CHKB-related megaconial muscular dystrophy phenotype — useful as a **comparator model** illustrating tissue-specific consequences of Kennedy-pathway enzyme loss (muscle-predominant for Chkb vs. presumed CNS-predominant for Chka).

**Yeast model (functional variant characterization, not a disease model per se):** *Saccharomyces cerevisiae cki1Δ* (choline-kinase-deficient) strain complemented with human wild-type or variant CHKA constructs — used as the primary functional assay confirming loss-of-function for all tested missense/start-loss human alleles (PMID:35202461). This is a **heterologous complementation assay**, valuable for variant functional classification but does not recapitulate organismal/CNS phenotypes.

**Cellular models (patient-derived and engineered):**
- **Patient-derived dermal fibroblasts** carrying homozygous p.(Pro194Ser) or p.(Arg141Trp) variants — the primary human cellular model used to demonstrate reduced phosphocholine/PC/GPC, mitochondrial dysfunction, elevated ROS, and lipid peroxidation (PMID:41308990).
- **U2OS (osteosarcoma) and SH-SY5Y (neuroblastoma) cell lines** treated with the pharmacological CHKA inhibitor **EB-3D** — used as an orthogonal, genotype-independent pharmacological model to corroborate the mechanistic findings from patient fibroblasts (PMID:41308990). SH-SY5Y is notable as a neuronally-relevant cell line, partially addressing the CNS-specificity question, though it remains a 2D cancer-derived cell line rather than a primary neuron or iPSC-neuron model.

**Model limitations / gaps:**
- **No zebrafish, *Drosophila*, or *C. elegans* CHKA model has been reported** in the literature reviewed, despite these being common rapid in vivo systems for neurodevelopmental gene characterization.
- **No iPSC-derived neuronal or brain organoid model** has yet been published for CHKA, which would be a natural and high-value next step given the disorder's core CNS phenotype (microcephaly, epilepsy) — patient fibroblast and cancer cell-line data, while mechanistically informative, cannot directly model neurodevelopmental/cortical phenotypes such as microcephaly.
- **No conditional or CNS-specific *Chka* knockout mouse** has been reported; the existing *Chka⁻/⁻* full-body knockout is embryonic lethal and therefore uninformative about postnatal/CNS-specific phenotypes, and no brain-restricted conditional knockout (e.g., Nestin-Cre or Emx1-Cre driven) modeling the partial/hypomorphic human genotype has yet been generated — this represents the most significant model-organism gap for mechanistic and preclinical therapeutic studies (e.g., testing FCCP or choline supplementation in vivo).

**Suggested model-organism resources for follow-up:** MGI (Chka: MGI:107760) for existing mouse allele/phenotype data; IMPC/KOMP for potential future conditional allele generation; no relevant ZFIN, FlyBase, or WormBase CHKA-disease entries identified.

---

## Summary of Key Citations

| Citation | Content |
|---|---|
| Klöckner et al., *Brain* 2022, **PMID:35202461**, DOI:10.1093/brain/awac074 | Founding clinical/genetic description of NEDMIMS; 6 individuals/5 families; variant identification; yeast functional assays; mouse knockout data; muscle biopsy findings |
| Tavasoli et al. (attributed), *J Biol Chem* 2025/2026, **PMID:41308990**, DOI:10.1016/j.jbc.2025.110983 | Mechanistic follow-up: patient fibroblast lipidomics, mitochondrial dysfunction, oxidative stress/lipid peroxidation, CCTα compensatory translocation, FCCP rescue experiment |
| OMIM #620023 | Clinical synopsis, gene mapping, inheritance |
| OMIM \*118491 | CHKA gene entry |
| MedGen C5774208 | Concept identifier, disease naming |
| MGI:107760 | *Chka* mouse gene/allele data |

**Notable evidence gaps flagged for future research and for knowledge-base curation:** absence of prevalence data, absence of a dedicated Orphanet entry, absence of an in vivo CNS-relevant animal model (zebrafish/organoid/conditional mouse), absence of any published treatment trial, and reliance on a very small (n=6) case series for all clinical/natural-history claims — all evidence in this report should be flagged as derived from a small, non-registry case series rather than population-level or randomized clinical-trial data.

Sources:
- [Entry - #620023 - NEURODEVELOPMENTAL DISORDER WITH MICROCEPHALY, MOVEMENT ABNORMALITIES, AND SEIZURES; NEDMIMS - OMIM](https://omim.org/entry/620023)
- [Entry - *118491 - CHOLINE KINASE, ALPHA; CHKA - OMIM](https://www.omim.org/entry/118491)
- [Bi-allelic variants in CHKA cause a neurodevelopmental disorder with epilepsy and microcephaly - PMC (PMID:35202461)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9630884/)
- [Bi-allelic variants in CHKA cause a neurodevelopmental disorder with epilepsy and microcephaly | Brain | Oxford Academic](https://academic.oup.com/brain/article/145/6/1916/6535865)
- [Neurodevelopmental disease-causing variants in choline kinase CHKA gene couple phosphatidylcholine synthesis to oxidative stress damage and disease etiology - PMC (PMID:41308990)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12800699/)
- [Neurodevelopmental disease-causing variants in choline kinase CHKA gene ... - ScienceDirect / J Biol Chem](https://www.sciencedirect.com/science/article/pii/S0021925825028352)
- [Neurodevelopmental disorder with microcephaly, movement abnormalities, and seizures (Concept Id: C5774208) - MedGen - NCBI](https://www.ncbi.nlm.nih.gov/medgen/1823981)
- [CHKA gene Choline Kinase Alpha - GeneCards](https://www.genecards.org/card/CHKA)
- [Chka MGI Mouse Gene Detail - MGI:107760](https://www.informatics.jax.org/marker/MGI:107760)
- [CHKA - Choline kinase alpha - UniProt P35790](https://www.uniprot.org/uniprotkb/P35790/entry)
- [Information on EC 2.7.1.32 - choline kinase - BRENDA Enzyme Database](https://www.brenda-enzymes.org/enzyme.php?ecno=2.7.1.32)
- [Neurodevelopmental Disease-causing Variants in Choline Kinase CHKA Gene ... - ResearchGate](https://www.researchgate.net/publication/397984406_Neurodevelopmental_Disease-causing_Variants_in_Choline_Kinase_CHKA_Gene_Couple_Phosphatidylcholine_Synthesis_to_Oxidative_Stress_Damage_and_Disease_Etiology)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 6 |
| On topic | 5 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:41308990` *(abstract only)*: "a compensatory activation of CCTα at the inner nuclear membrane, likely as an adaptive response to restore PC synthesis"
  - closest text in source: "Biallelic variants in CHKA, which encodes the first enzyme in the CDP-choline pathway for the synthesis of phosphatidylcholine, cause an inherited disorder characterized by epilepsy, microcephaly, and intellectual disability"
- `PMID:41308990` *(abstract only)*: "significantly reduced ROS levels and lipid peroxidation to a level similar to fibroblasts from controls"
  - closest text in source: "Treatment with FCCP, a mitochondrial uncoupler, reduced ROS levels and attenuated lipid peroxidation in CHKA patient fibroblasts, suggesting a potential approach to therapeutic intervention."