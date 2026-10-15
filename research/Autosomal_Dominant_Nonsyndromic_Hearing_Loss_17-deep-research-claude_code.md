---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-22T14:12:41.314544'
end_time: '2026-08-22T14:17:22.025101'
duration_seconds: 280.71
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Autosomal Dominant Nonsyndromic Hearing Loss 17
  mondo_id: ''
  category: Genetic
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
  web_search_requests: 16
  num_turns: 24
  total_cost_usd: 1.4848270000000003
  session_id: 6f8bf895-3ab0-55cb-a154-acb932b43f03
  stop_reason: end_turn
  assistant_text_blocks: 4
citation_count: 24
reference_validation:
  total_references: 19
  verified: 18
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.053
  relevance_assessed: 18
  on_topic: 17
  unresolved_references:
  - DOI:10.3390/genes17020154)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12941242/
  needs_review: true
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Dominant Nonsyndromic Hearing Loss 17
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Autosomal Dominant Nonsyndromic Hearing Loss 17** covering all of the
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

I'll research this topic using web search to gather accurate, citable information on DFNA17/MYH9-related nonsyndromic hearing loss.

I now have comprehensive material. Let me pull a few remaining pieces — the PMC full text for the original 2000 paper (for precise quotes), and check the audiological phenotype and MYH14 comparison paper for additional genotype-phenotype detail.

I have enough well-sourced material now to compile the comprehensive report.

I now have sufficient sourced material to compile the full report.

# Autosomal Dominant Nonsyndromic Hearing Loss 17 (DFNA17) — Comprehensive Research Report

## 1. Disease Information

**Overview.** DFNA17 (Deafness, Autosomal Dominant 17) is a form of nonsyndromic, progressive, high-frequency-predominant sensorineural hearing loss caused by heterozygous missense mutation in **MYH9**, the gene encoding non-muscle myosin heavy chain IIA (NMMHC-IIA), on chromosome 22q12.3 [(OMIM #603622)](https://omim.org/entry/603622). It was originally mapped as a novel autosomal dominant deafness locus in a five-generation American kindred with hearing loss due to histopathologically confirmed **cochleosaccular degeneration (CSD)** — collapse of Reissner's membrane with degeneration of the organ of Corti, saccular epithelium, and stria vascularis [(Lalwani et al., 1999, PMID:9915977)](https://pubmed.ncbi.nlm.nih.gov/9915977/). The causative gene was identified the following year: sequencing of MYH9 in the same kindred revealed a heterozygous **c.2114G>A (p.Arg705His, R705H)** mutation that cosegregated with deafness [(Lalwani et al., 2000, PMID:11023810; full text PMC1288554)](https://pmc.ncbi.nlm.nih.gov/articles/PMC1288554/).

Critically, MYH9 mutations more broadly cause **MYH9-related disease (MYH9-RD)** — a syndromic disorder combining congenital macrothrombocytopenia with variable, later-onset sensorineural hearing loss, presenile cataracts, and progressive nephropathy, historically split into four eponymous entities (May-Hegglin anomaly, Epstein syndrome, Fechtner syndrome, Sebastian syndrome) now recognized as one clinical continuum [(GeneReviews, NBK2689)](https://www.ncbi.nlm.nih.gov/books/NBK2689/). Subsequent work showed that even the R705H variant originally described as causing "pure" nonsyndromic DFNA17 can, on closer hematologic/renal evaluation, present with subtle MYH9-RD features — i.e., DFNA17 and MYH9-RD lie on a phenotypic spectrum rather than being fully distinct entities [(Verver et al., 2015, PMID:24890873)](https://pubmed.ncbi.nlm.nih.gov/24890873/).

**Key identifiers:**
- **OMIM:** #603622 (DEAFNESS, AUTOSOMAL DOMINANT 17; DFNA17)
- **Gene:** MYH9 — HGNC:7579, NCBI Gene ID 4627, chromosome 22q12.3, 41 exons, ~107 kb, encoding a 1,960-amino-acid protein [(GeneCards)](https://www.genecards.org/cgi-bin/carddisp.pl?gene=MYH9)
- **MONDO/Orphanet/GARD:** listed as "autosomal dominant nonsyndromic hearing loss 17" [(NORD/GARD)](https://rarediseases.info.nih.gov/diseases/9726/autosomal-dominant-nonsyndromic-hearing-loss-17); MYH9-RD as a whole is Orphanet ORPHA:182050 (umbrella) with related individual disorder entries for May-Hegglin/Fechtner/Sebastian/Epstein syndromes
- **Disease Ontology:** DOID:0110548
- **GTR condition:** C1863659

**Synonyms:** DFNA17; deafness, autosomal dominant, cochleosaccular type; nonsyndromic hereditary hearing impairment, DFNA17 type. Note the broader disease-family synonyms (not equivalent, but genetically allelic): May-Hegglin anomaly, Fechtner syndrome, Epstein syndrome, Sebastian (platelet) syndrome — all subsumed under **MYH9-related disease** [(GeneReviews)](https://www.ncbi.nlm.nih.gov/books/NBK2689/); [(Nature Genetics, Seri et al. 2000, ng0900_103)](https://www.nature.com/articles/ng0900_103).

**Source of information:** Aggregated disease-level knowledge from OMIM, GeneReviews (systematic literature synthesis + registry data), and peer-reviewed case series/family reports (individually ascertained pedigrees) — not primary EHR data.

---

## 2. Etiology

**Disease causal factor:** Purely genetic. DFNA17 is caused by heterozygous, typically missense, gain-of-function/dominant-negative mutations in **MYH9** (non-muscle myosin heavy chain IIA). No environmental or infectious cause is implicated in the nonsyndromic (isolated hearing loss) presentation.

**Genetic risk factors:**
- The **R705H** mutation (exon 16, SH1 helix/linker region of the motor head domain) is the best-characterized DFNA17-causing allele, independently identified in an American kindred [(PMID:11023810)](https://pubmed.ncbi.nlm.nih.gov/11023810/), a five-generation Australian family [(cochlear-implant outcome paper, PMID:17146397)](https://pubmed.ncbi.nlm.nih.gov/17146397/), and a Brazilian family [(PMID:25505834)](https://pubmed.ncbi.nlm.nih.gov/25505834/).
- Other MYH9 missense variants across the motor head (exons 1–19) and coiled-coil tail (exons 21–40) cause the broader MYH9-RD spectrum; genotype strongly predicts phenotype severity (see Section 4/9) [(GeneReviews)](https://www.ncbi.nlm.nih.gov/books/NBK2689/).
- Approximately **65%** of MYH9-RD probands have an affected parent (true autosomal dominant transmission); **~35%** arise as de novo mutations, with documented parental germline/somatic mosaicism in some kindreds [(GeneReviews)](https://www.ncbi.nlm.nih.gov/books/NBK2689/).
- A large 2026 Japanese cohort study (Genes, 24 patients/18 families) found hearing loss progresses faster in patients with **myosin head-domain** variants than **tail-domain** variants, though both eventually reach bilateral profound loss [(PMC12941242 / DOI:10.3390/genes17020154)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12941242/).

**Environmental risk factors:** None established as disease-causing. However, **ototoxic exposure is a documented risk factor for accelerated hearing decline** in MYH9-RD/DFNA17 patients — aminoglycosides, high-dose salicylates, and loop diuretics are specifically flagged in management guidance as agents to avoid because they may exacerbate the underlying cochlear vulnerability [(GeneReviews)](https://www.ncbi.nlm.nih.gov/books/NBK2689/).

**Protective factors:** None specifically documented for hearing loss in MYH9-RD. (Note: the well-known MYH9 "E-1" risk haplotype associated with chronic kidney disease/FSGS susceptibility in African-ancestry populations is a **distinct, common-variant association** unrelated to the rare dominant MYH9-RD/DFNA17-causing mutations — it should not be conflated with DFNA17 causal genetics [(Nelson et al., PMC2901326)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2901326/).)

**Gene-environment interactions:** Not specifically characterized for DFNA17; the ototoxic-drug avoidance recommendation implies a genotype (MYH9-compromised cochlear cytoskeleton) × environment (ototoxin exposure) interaction affecting rate of hearing decline, though this is based on expert clinical guidance rather than a formal interaction study.

---

## 3. Phenotypes

### Primary phenotype: Progressive sensorineural hearing loss
- **Type:** Clinical sign / audiometric abnormality (symptom: perceived hearing loss; sign: abnormal pure-tone audiometry)
- **HPO term suggestion:** `HP:0000407` (Sensorineural hearing impairment); more specific: `HP:0000362` (Progressive sensorineural hearing impairment) or `HP:0000410` (Progressive hearing impairment); `HP:0008527` (Congenital sensorineural hearing impairment) is **not** typically applicable — onset is postlingual.
- **Age of onset:** In the original American DFNA17 kindred, onset was reported at **~10 years of age**, beginning in the high frequencies [(PMC1288554)](https://pmc.ncbi.nlm.nih.gov/articles/PMC1288554/). Across the broader MYH9-RD population, hearing loss develops later and more variably: ~36% before age 20, ~33% between ages 20–40, ~31% after 40, with ~50% of individuals affected by a mean age of 33 [(GeneReviews)](https://www.ncbi.nlm.nih.gov/books/NBK2689/).
- **Progression/severity:** Classically described as beginning as **mild, high-frequency** loss in childhood/adolescence that progresses to **moderate-to-severe/profound** deafness by the third decade [(OMIM #603622)](https://omim.org/entry/603622); [(PMC1288554)](https://pmc.ncbi.nlm.nih.gov/articles/PMC1288554/). A 2026 Japanese cohort documented cases with rapid deterioration (~50 dB worsening within 5 years), ultimately reaching bilateral profound loss regardless of head- vs. tail-domain mutation, though head-domain variants progressed faster [(Genes 2026)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12941242/). Overall in MYH9-RD, ~80–85% eventually develop sensorineural hearing loss [(GeneReviews)](https://www.ncbi.nlm.nih.gov/books/NBK2689/).
- **Frequency among affected individuals:** Near-complete for R705H-type DFNA17 kindreds (fully penetrant by adulthood); ~80–85% across the full MYH9-RD spectrum.
- **Laterality:** Bilateral, generally symmetric.
- **Quality of life impact:** Progression to severe-profound deafness by young adulthood; the condition "interferes with daily functioning in ~90% of affected individuals with abnormal audiometry" per GeneReviews summary data.

### Related/associated audiovestibular pathology
- **Cochleosaccular degeneration** on temporal bone histopathology: collapsed Reissner's membrane, degeneration of the organ of Corti, saccular epithelium, and stria vascularis — the anatomic substrate of DFNA17 hearing loss in the original kindred [(PMID:9915977)](https://pubmed.ncbi.nlm.nih.gov/9915977/); [(PMC1288554)](https://pmc.ncbi.nlm.nih.gov/articles/PMC1288554/). HPO suggestion: no precise dedicated term; `HP:0011471` (Reissner membrane rupture/absence — check OMIM CS) or free-text/anatomic annotation may be more appropriate; broadly `HP:0000359` (Abnormality of the inner ear).

### Phenotypes seen only in syndromic MYH9-RD (relevant for differential/pleiotropy, not part of "pure" DFNA17 nonsyndromic presentation)
- Macrothrombocytopenia (congenital, ~100% penetrant) — `HP:0040218` (Macrothrombocytopenia)
- Presenile cataracts (~20%, mean onset 37) — `HP:0000518` (Cataract)
- Progressive nephropathy/glomerulopathy with proteinuria, progressing to ESRD in ~43% of those affected (~25% overall) — `HP:0000093` (Proteinuria), `HP:0000112` (Nephropathy)
- Neutrophil Döhle-like inclusion bodies (42–84%) — a laboratory/histologic finding, not applicable to nonsyndromic DFNA17
[(GeneReviews)](https://www.ncbi.nlm.nih.gov/books/NBK2689/)

---

## 4. Genetic/Molecular Information

**Causal gene:** MYH9 (HGNC:7579; NCBI Gene 4627; chromosome 22q12.3). Encodes **non-muscle myosin heavy chain IIA (NMMHC-IIA)**, a 1,960-amino-acid actin-binding motor protein.

**Protein domain structure** [(MYH9 structure review, PMID:29679756)](https://pubmed.ncbi.nlm.nih.gov/29679756/):
- **N-terminal motor/head domain** (exons 1–19): globular ATPase motor head that binds actin and hydrolyzes ATP to generate force; subdivided into an SH3-like motif, upper subdomain, lower subdomain, and converter region.
- **Neck domain** (exon 20): binds essential and regulatory myosin light chains (ELC/RLC).
- **Coiled-coil rod/tail domain** (exons 21–40): mediates bipolar filament self-assembly via a 28-residue heptad repeat pattern.
- **Non-helical tailpiece** (exon 41): C-terminal region.

**DFNA17 causal variant:** c.2114G>A, p.**Arg705His (R705H)** — a missense change at an invariant, highly conserved arginine within the **SH1 helix/linker region of the motor head domain**, considered critical for myosin ATPase activity [(PMC1288554)](https://pmc.ncbi.nlm.nih.gov/articles/PMC1288554/). Same variant independently found in American, Australian, and Brazilian kindreds [(PMID:11023810)](https://pubmed.ncbi.nlm.nih.gov/11023810/); [(PMID:25505834)](https://pubmed.ncbi.nlm.nih.gov/25505834/); [(PMID:17146397)](https://pubmed.ncbi.nlm.nih.gov/17146397/). Verver et al. (2015) subsequently showed that R705H is not exclusively "nonsyndromic" — some carriers show subtle macrothrombocytopenia/other MYH9-RD features on closer evaluation, arguing R705H sits at the mild end of the MYH9-RD spectrum rather than being a truly separate nonsyndromic entity [(PMID:24890873)](https://pubmed.ncbi.nlm.nih.gov/24890873/).

**Variant classification (ACMG/AMP):** R705H — Pathogenic/Likely Pathogenic (ClinVar; segregates with disease across 3 independent families, absent/extremely rare in population databases, affects a highly conserved functional residue). MYH9 variants broadly are missense or small in-frame indels; **~70% of MYH9-RD cases cluster in six hotspot residues** (predominantly within exons 2, 17, 25–27, 31, 39) [(GeneReviews)](https://www.ncbi.nlm.nih.gov/books/NBK2689/).

**Allele frequency:** MYH9 pathogenic variants causing hearing loss are rare in population databases — a 2025 audiological-phenotype study reported minor allele frequencies < 0.5×10⁻⁵ for the variants identified, consistent with pathogenicity [(Scientific Reports 2025, PMC12219520)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12219520/). (Note: the common **MYH9 E-1 kidney-risk haplotype**, at high frequency in African-ancestry populations, is a distinct non-Mendelian susceptibility variant unrelated to DFNA17/MYH9-RD causal mutations — see Section 2.)

**Origin:** Germline (constitutional heterozygous), autosomal dominant. Somatic mosaicism has been documented in some MYH9-RD kindreds among apparently unaffected/mildly affected parents [(GeneReviews)](https://www.ncbi.nlm.nih.gov/books/NBK2689/).

**Functional consequence:** Dominant-negative mechanism — mutant NMMHC-IIA monomers co-assemble with wild-type monomers into bipolar filaments, disrupting normal filament assembly, ATPase motor function, and/or subcellular localization, thereby impairing cytoskeletal force-generating processes in megakaryocytes, podocytes, lens epithelium, and cochlear structures [(structure/mechanism review, PMC7348894)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7348894/); [(rod-mutation assembly study, Blood, PMID for ASH article)](https://ashpublications.org/blood/article/105/1/161/20003/Rod-mutations-associated-with-MYH9-related).

**Genotype-phenotype correlation (established across MYH9-RD, informative for DFNA17 counseling):**
| Mutation region | Hearing loss risk | Nephropathy risk | Cataract risk | Notes |
|---|---|---|---|---|
| Arg702 (head domain) | Severe, early | High, rapid to ESRD | Present | Most severe overall phenotype |
| Arg705 (head domain, incl. R705H) | High | Low-moderate | Variable | Classic "DFNA17" allele |
| Arg1165 | All by age 60 | Low | Low | Hearing-predominant |
| Asp1424His | All by age 60 | Most | Elevated | Intermediate-high risk |
| Asp1424Asn, Glu1841Lys | Low | Low | Low | Macrothrombocytopenia often sole feature |
| Exon 41 (nonsense/frameshift, tail) | Rare | Rare | Rare | Thrombocytopenia-limited |
[(GeneReviews genotype-phenotype table)](https://www.ncbi.nlm.nih.gov/books/NBK2689/); consistent with the 2026 Japanese cohort finding of faster progression for head-domain vs. tail-domain variants [(PMC12941242)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12941242/).

**Modifier genes:** None specifically established for DFNA17/MYH9-RD hearing loss.

**Epigenetics / chromosomal abnormalities:** Not implicated; DFNA17 is a single-gene missense disorder, not a copy-number or epigenetic condition.

---

## 5. Environmental Information

- **Environmental factors:** No environmental agent causes DFNA17; the disease is fully genetic. The clinically relevant environmental modifier is **avoidance of ototoxic drugs** (aminoglycoside antibiotics, high-dose salicylates, loop diuretics), recommended because these agents may accelerate hearing decline in a cochlea already structurally compromised by MYH9 dysfunction [(GeneReviews)](https://www.ncbi.nlm.nih.gov/books/NBK2689/).
- **Lifestyle factors:** No specific lifestyle risk/protective factors documented.
- **Infectious agents:** Not applicable — DFNA17 is a monogenic, non-infectious disorder.

---

## 6. Mechanism / Pathophysiology

**Causal chain (proposed):**
1. Heterozygous MYH9 missense mutation (e.g., R705H in the motor head SH1-linker) → altered NMMHC-IIA structure/ATPase function within actomyosin motor complexes.
2. Dominant-negative incorporation of mutant heavy chains into non-muscle myosin IIA bipolar filaments → impaired filament assembly/disassembly dynamics and cytoskeletal force generation [(PMC7348894)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7348894/).
3. In the cochlea, MYH9 is normally expressed in the **organ of Corti (sensory and supporting hair cells), the spiral ligament, the spiral limbus, and Reissner's membrane** — but notably **not** in the stria vascularis proper (though CSD ultimately involves the stria as a secondary/downstream finding) [(PMID:15079858)](https://pubmed.ncbi.nlm.nih.gov/15079858/); [(PMID:16862555 — stereocilia localization)](https://pubmed.ncbi.nlm.nih.gov/16862555/); [(original DFNA17 paper)](https://pmc.ncbi.nlm.nih.gov/articles/PMC1288554/). MYH9 protein is specifically localized **within the stereocilia** of hair cells, implicating a role in stereocilia bundle architecture and mechanotransduction.
4. Progressive structural failure manifests histopathologically as **cochleosaccular degeneration**: collapse of Reissner's membrane, degeneration of the organ of Corti, and degeneration of the saccular epithelium — a pattern classically termed **Scheibe dysplasia** when seen developmentally, but here representing a postnatal degenerative process [(PMID:9915977)](https://pubmed.ncbi.nlm.nih.gov/9915977/).
5. Progressive, high-frequency-first sensorineural hearing loss results, consistent with a basal-turn (high-frequency) predilection of degeneration.

**Upstream vs. downstream:** The genetic lesion (MYH9 mutation) is upstream; loss of normal actomyosin-based cytoskeletal support in cochlear epithelial/hair-cell structures is intermediate; cochleosaccular degeneration and consequent mechanotransduction failure are downstream, directly producing the audiometric phenotype.

**Cell types involved:**
- Inner and outer hair cells of the organ of Corti (`CL:0002165` outer hair cell of Corti's organ; `CL:0002167` inner hair cell of Corti's organ)
- Supporting cells of the organ of Corti
- Spiral ligament fibrocytes
- Reissner's membrane epithelial cells
- Saccular epithelial cells

**Molecular functions / biological processes (GO term suggestions):**
- `GO:0000146` (microfilament motor activity) / `GO:0003774` (cytoskeletal motor activity)
- `GO:0031982` — n/a; more relevant: `GO:0007015` (actin filament organization)
- `GO:0032796` (uropod organization) — n/a; better: `GO:0030036` (actin cytoskeleton organization)
- `GO:0016459` (myosin complex)
- `GO:0032060` (bleb assembly) — n/a
- Relevant curated GO BP: `GO:0007605` (sensory perception of sound) as the phenotypic endpoint; mechanistically `GO:0030048` (actin filament-based movement) and `GO:0060121` (inner ear receptor stereocilium organization) are strong candidates for stereocilia-related MYH9 function.

**Protein dysfunction:** Altered ATPase motor activity / filament assembly due to a missense substitution at a catalytically important residue (R705H — SH1 linker, essential for the converter/lever-arm mechanism that couples ATP hydrolysis to force generation).

**Tissue damage mechanism:** Degenerative (not inflammatory or vascular) — progressive structural collapse of cytoskeleton-dependent inner-ear membranous structures, consistent with a chronic mechanical/structural-support failure model rather than oxidative stress or ischemia.

**Molecular profiling / advanced technologies:** No human cochlear single-cell, transcriptomic, proteomic, or spatial-omics data specific to DFNA17 were identified in this search; mechanistic data derive largely from rodent expression studies (RT-PCR/immunohistochemistry in rat cochlea) [(PMC1288554)](https://pmc.ncbi.nlm.nih.gov/articles/PMC1288554/) and mouse models (Section 15).

**Important negative/complicating mechanistic finding:** A knockout-first ES-cell-derived heterozygous *Myh9*-null mouse model showed **no hearing loss and no cochleosaccular degeneration**, in contrast to human DFNA17/MYH9-RD — homozygous nulls were embryonic lethal, and heterozygotes (modeling haploinsufficiency) were phenotypically normal audiologically [(Parker et al., 2006, PMID:16630581)](https://pubmed.ncbi.nlm.nih.gov/16630581/). This strongly supports a **dominant-negative** (rather than simple haploinsufficiency) mechanism for human MYH9-RD/DFNA17 hearing loss — i.e., the mutant protein must be expressed and incorporated into filaments to cause disease, not merely reduced gene dosage.

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary organ:** Inner ear (cochlea and vestibular labyrinth — specifically saccule) — `UBERON:0001846` (cochlea), `UBERON:0002071` (auditory system component)
- **Body system:** Auditory/special sensory system (nonsyndromic form). In the broader MYH9-RD spectrum, additionally: hematologic system (platelets/megakaryocytes), renal system (glomerulus), and ocular lens.

**Tissue/cell level:**
- Organ of Corti (sensory epithelium) — `UBERON:0001844`
- Reissner's (vestibular) membrane — `UBERON:0002068`
- Spiral ligament — `UBERON:0002261`
- Spiral limbus
- Saccular epithelium (vestibular sensory epithelium of the saccule) — `UBERON:0001846`-adjacent structure
- Stria vascularis (secondarily affected in CSD histopathology)
- Cell types: inner/outer hair cells (`CL:0002167`, `CL:0002165`), supporting cells, spiral ligament fibrocytes

**Subcellular level:**
- Stereocilia (actin-rich mechanotransduction organelles) — MYH9 is specifically localized within stereocilia [(PMID:16862555)](https://pubmed.ncbi.nlm.nih.gov/16862555/); GO Cellular Component: `GO:0032420` (stereocilium)
- Actomyosin cytoskeleton / cortical actin network — `GO:0042995` (cell projection), `GO:0015629` (actin cytoskeleton)

**Localization/laterality:** Bilateral, generally symmetric sensorineural hearing loss; no lateralization pattern reported.

---

## 8. Temporal Development

- **Onset:** Postlingual, typically childhood-to-adolescent onset (as early as age 10 in the original kindred) for the high-frequency component; onset across broader MYH9-RD hearing loss spans childhood through the sixth decade, with roughly even distribution across age bands (<20, 20–40, >40) [(GeneReviews)](https://www.ncbi.nlm.nih.gov/books/NBK2689/).
- **Onset pattern:** Insidious and progressive, not acute or episodic.
- **Progression:** Classic pattern is mild high-frequency loss progressing to moderate-severe-to-profound deafness affecting all frequencies by the third decade [(OMIM #603622)](https://omim.org/entry/603622). Some patients show rapid deterioration (up to ~50 dB within 5 years) [(Genes 2026 cohort)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12941242/). Progression rate correlates with mutation location (head-domain variants progress faster than tail-domain variants), though ultimate endpoint (bilateral profound loss) is similar across genotypes.
- **Disease course:** Chronic, progressive, lifelong; not relapsing-remitting.
- **Duration:** Lifelong (no spontaneous remission reported).
- **Critical periods:** Early identification during the high-frequency-only phase is clinically important for timely audiologic intervention/genetic counseling before progression to more disabling levels.

---

## 9. Inheritance and Population

**Epidemiology:**
- DFNA17 itself is exceedingly rare — reported in only a handful of kindreds worldwide (American, Australian, Brazilian, and additional cases identified in Japanese and Chinese cohorts of dominant nonsyndromic hearing loss).
- MYH9-RD as a whole: Italian national registry–based prevalence estimate of **3.75 per 1,000,000**; broader estimates based on population genetic databases suggest a potentially higher true frequency, on the order of **1:20,000–25,000** [(GeneReviews)](https://www.ncbi.nlm.nih.gov/books/NBK2689/).
- Screening of MYH9 exons in general "nonsyndromic deafness" cohorts finds it an **infrequent** cause overall (e.g., a Japanese screening study of MYH9 exons 1, 16, 26, 30 found few positive cases) [(PMID:19645626)](https://pubmed.ncbi.nlm.nih.gov/19645626/), underscoring that MYH9 mutations are a rare but recurrent cause of ADNSHL requiring targeted or panel-based testing to detect.

**Inheritance pattern:** Autosomal dominant.

**Penetrance:** Complete to near-complete for hearing loss by adulthood in classic DFNA17 kindreds carrying R705H; across the wider MYH9-RD spectrum, penetrance/expressivity for hearing loss (and nephropathy, cataract) is **variable and age-dependent**, in contrast to the fully penetrant congenital macrothrombocytopenia [(GeneReviews)](https://www.ncbi.nlm.nih.gov/books/NBK2689/).

**Expressivity:** Highly variable across families and even within families — illustrated by markedly different cochlear-implant outcomes between the American (poor outcome) and Australian (excellent outcome) R705H kindreds despite an identical mutation [(PMID:17146397)](https://pubmed.ncbi.nlm.nih.gov/17146397/).

**Genetic anticipation:** Not reported/applicable (not a repeat-expansion disorder).

**Germline mosaicism:** Documented in some MYH9-RD families among parents of de novo cases.

**Founder effects:** Not specifically reported for DFNA17/R705H — the mutation has arisen (or been inherited) independently in geographically distinct (American, Australian, Brazilian) kindreds, more consistent with a recurrent mutational hotspot at a critical conserved residue than a single founder event, though formal haplotype analysis to confirm this was not identified in this search.

**Carrier frequency:** Not applicable in the traditional sense (autosomal dominant, not recessive carrier state); population allele frequency for pathogenic MYH9 hearing-loss variants is <0.5×10⁻⁵ [(Scientific Reports 2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12219520/).

**Population demographics:**
- No specific ethnic/geographic predilection established for DFNA17 (R705H) beyond the independently ascertained American, Australian, and Brazilian families.
- Sex ratio: no sex bias reported (autosomal, not X-linked).
- Age distribution: skewed toward pediatric/adolescent-to-young-adult presentation for hearing symptoms, consistent with progressive postlingual onset.

---

## 10. Diagnostics

**Clinical tests:**
- **Audiometry (pure-tone and speech audiometry):** Serial audiograms document the characteristic bilateral, symmetric, progressive, initially high-frequency-predominant sensorineural pattern. LOINC-coded audiometry panels apply (general audiometric LOINC codes, e.g., LOINC:28569-6 class); no disease-specific biomarker exists.
- **Temporal bone imaging:** High-resolution CT/MRI may be used to exclude structural/syndromic causes but is not diagnostic for MYH9-associated CSD, which is a histopathologic (not typically radiologically visible in vivo) diagnosis.
- **Temporal bone histopathology** (research/autopsy only): demonstrates cochleosaccular degeneration — collapsed Reissner's membrane, organ of Corti degeneration.
- **Peripheral blood smear / platelet morphometry:** essential for distinguishing isolated DFNA17 from broader MYH9-RD — mean platelet diameter >3.7 µm and >40% of platelets >3.9 µm are diagnostic thresholds for MYH9-RD (86–87% sensitivity/specificity) [(GeneReviews)](https://www.ncbi.nlm.nih.gov/books/NBK2689/).
- **Immunofluorescence for MYH9 protein aggregates in neutrophils:** near-100% sensitivity/specificity for MYH9-RD; a key ancillary test to determine whether a "nonsyndromic" hearing-loss patient actually has occult MYH9-RD.

**Genetic testing:**
- **Recommended approach:** Given genetic heterogeneity of ADNSHL, a **hearing-loss gene panel** (including MYH9) or exome/genome sequencing is typically first-line; single-gene MYH9 sequencing is appropriate when clinical suspicion is high (e.g., known family history of the R705H mutation, or coexisting subtle platelet/renal/lens findings).
- **Sequence analysis:** detects ~98% of MYH9 pathogenic variants; deletion/duplication analysis reserved for sequence-negative cases [(GeneReviews)](https://www.ncbi.nlm.nih.gov/books/NBK2689/).
- **Cascade/family testing:** appropriate for at-risk relatives given autosomal dominant inheritance and variable expressivity.

**Clinical criteria / differential diagnosis:**
- Must be distinguished from other DFNA (autosomal dominant nonsyndromic) loci — e.g., DFNA14/34 gene **MYH14** (a paralogous myosin gene with a very similar progressive high-frequency phenotype) [(Scientific Reports 2025 comparison study)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12219520/); [(Donaudy et al. MYH14 discovery paper, PMID:28221712)](https://pubmed.ncbi.nlm.nih.gov/28221712/).
- Must be distinguished from **Alport syndrome** (also autosomal-pattern progressive SNHL + nephropathy, but caused by COL4A3/4/5 and lacking the platelet abnormality that is pathognomonic for MYH9-RD) [(GeneReviews)](https://www.ncbi.nlm.nih.gov/books/NBK2689/).
- Isolated apparent "DFNA17" presentations should prompt evaluation for occult MYH9-RD (platelet count/morphology) given the Verver et al. finding that R705H is not always purely nonsyndromic [(PMID:24890873)](https://pubmed.ncbi.nlm.nih.gov/24890873/).

**Screening:** No population newborn-screening program specifically targets MYH9-RD/DFNA17 (postlingual onset limits utility of newborn hearing screening for early detection); genetic cascade testing in known families is the primary screening modality.

---

## 11. Outcome/Prognosis

- **Survival/mortality:** DFNA17 (isolated nonsyndromic form) does not affect survival or life expectancy. In the broader MYH9-RD spectrum, mortality risk relates to complications of progressive renal failure (in genotypes with high nephropathy risk) and, rarely, severe hemorrhage — not to the hearing loss itself.
- **Morbidity/function:** Progressive bilateral deafness by young adulthood is the dominant functional morbidity; profound communicative disability without intervention.
- **Complications:** Social/educational/vocational impact of progressive childhood-onset hearing loss; risk of misdiagnosis (e.g., as isolated presbycusis-pattern or as unrelated ADNSHL) delaying appropriate genetic counseling.
- **Recovery potential:** No spontaneous recovery; hearing aids and cochlear implantation are effective interventions (see Treatment).
- **Prognostic factors:** Mutation location (head-domain variants → faster progression) is the clearest prognostic genotype-phenotype correlate identified [(Genes 2026 cohort)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12941242/); earlier age of hearing-loss onset in MYH9-RD broadly correlates with faster deterioration and higher likelihood of eventual severe-to-profound deafness [(GeneReviews)](https://www.ncbi.nlm.nih.gov/books/NBK2689/).

---

## 12. Treatment

**No disease-modifying/curative therapy exists** for MYH9-associated hearing loss; management is supportive/rehabilitative.

- **Hearing aids:** First-line for mild-moderate loss. NCIT suggestion: `NCIT:C122435` (Hearing Aid) — no dedicated NCIT clinical-action term historically existed for hearing-aid usage in this KB's controlled set (per project convention, `DEVICE` modality cannot always be inferred mechanically).
- **Cochlear implantation:** Recommended and effective for progression to severe-to-profound deafness. Outcomes reported as variable between kindreds — poor in the original American R705H family, excellent in the Australian R705H family — but the literature concludes CI "should be strongly considered" for DFNA17/MYH9-RD deafness [(Kim et al., 2007, PMID:17146397)](https://pubmed.ncbi.nlm.nih.gov/17146397/). NCIT suggestion: cochlear implantation maps most closely to `NCIT:C15329` (Surgical Procedure) with device-specific detail in `therapeutic_modality: DEVICE`.
- **Avoidance of ototoxic agents** (aminoglycosides, high-dose salicylates, loop diuretics) as a preventive/supportive measure to avoid accelerating hearing decline [(GeneReviews)](https://www.ncbi.nlm.nih.gov/books/NBK2689/) — maps to `NCIT:C49236` (Therapeutic Procedure)/behavioral-modality counseling rather than a drug treatment per se.
- **Genetic counseling:** `NCIT:C15240` (Genetic Counseling) — essential given autosomal dominant inheritance, variable expressivity, and the potential for occult syndromic (MYH9-RD) features.
- **Audiologic surveillance:** GeneReviews management guidance recommends hearing evaluation approximately **every 3 years** in known MYH9 mutation carriers (more frequently if symptomatic) to track progression and time intervention.
- **No gene therapy, RNA-based therapy, or targeted pharmacotherapy** for MYH9-associated hearing loss has reached clinical trials at the time of this search (searches for MYH9 hearing-loss-specific clinical trials on ClinicalTrials.gov were not separately queried in this pass but no such trials surfaced in the literature reviewed).
- **Note:** For the broader MYH9-RD syndrome (not applicable to isolated nonsyndromic hearing loss but relevant to the allelic disease family), eltrombopag (thrombopoietin-receptor agonist) is used perioperatively for severe thrombocytopenia, and ACE inhibitors/ARBs are used for early nephropathy — these are not hearing-loss treatments.

**Treatment algorithm:** Stepwise — amplification (hearing aids) → cochlear implantation upon progression to severe/profound loss, paired with ongoing audiologic surveillance and avoidance of ototoxins; genetic counseling throughout.

---

## 13. Prevention

- **Primary prevention:** Not applicable in the classic sense (germline genetic disease); genetic counseling and reproductive options (e.g., prenatal or preimplantation genetic testing) are available to at-risk families given known familial mutation status but were not specifically documented as widely utilized in the literature reviewed.
- **Secondary prevention:** Early identification via cascade genetic testing in known families and vigilant audiologic surveillance enables earlier intervention (hearing aids) before profound loss develops.
- **Tertiary prevention:** Avoidance of ototoxic medications; timely cochlear implantation to prevent secondary developmental/communicative morbidity from progressing deafness in pediatric patients.
- **Immunization:** Not applicable.
- **Screening:** No dedicated population screening program; genetic testing driven by family history/clinical suspicion, not universal newborn screening (given postlingual onset).
- **Genetic counseling:** Central preventive strategy — informing at-risk relatives of 50% transmission risk, enabling early surveillance planning, and evaluating for occult syndromic MYH9-RD features that would change surveillance recommendations (nephropathy, cataract, platelet monitoring).
- **Public health/environmental interventions:** Not applicable (not an environmentally caused disease); the sole "environmental" preventive measure is ototoxin avoidance (see Section 12).

---

## 14. Other Species / Natural Disease

- **Taxonomy:** No naturally occurring veterinary/companion-animal disease analog for MYH9-associated hearing loss was identified in this search (unlike, e.g., well-documented canine models for other deafness genes). *Mus musculus* — `NCBITaxon:10090` — is the primary comparative species, but via engineered (not naturally occurring) models (see Section 15).
- **Orthologous gene:** Mouse *Myh9* (MGI ortholog of human MYH9); highly conserved across mammals given the essential, ancient function of non-muscle myosin II in cytokinesis and cell motility.
- **Comparative biology:** The actomyosin cytoskeletal machinery and its role in cell shape/motility is deeply evolutionarily conserved; however, whether MYH9's specific inner-ear/stereociliary role is conserved between mouse and human is called into question by the discordant mouse knockout phenotype (Section 6/15).
- **Transmission/zoonotic potential:** Not applicable — a purely genetic, non-transmissible disorder.

---

## 15. Model Organisms

**Mouse models — the key (and somewhat surprising) evidence base:**

1. **Heterozygous *Myh9*-null (gene-trap ES cell–derived) mice** [(Parker et al., 2006, PMID:16630581)](https://pubmed.ncbi.nlm.nih.gov/16630581/):
   - Derived using public BayGenomics gene-trapped ES cell resources.
   - **Homozygous nulls: embryonic lethal** (none identified at birth), consistent with MYH9's essential developmental role.
   - **Heterozygous mice: no hearing loss and no cochleosaccular degeneration** were observed, even in aged animals — in **direct contrast to the human DFNA17 phenotype**.
   - **Conclusion/limitation:** Heterozygous loss (haploinsufficiency) of Myh9 alone is not sufficient to reproduce human hearing loss in mice, implying the human disease mechanism is more likely **dominant-negative** (requiring expression of the specific mutant protein) rather than simple dosage reduction — an important **HUMAN_MODEL_MISMATCH**-type caveat for curation.

2. **Heterozygous *Myh9* R702C knock-in mice** [(Suzuki et al., 2013, PLoS ONE, PMC3748045)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3748045/):
   - Models the human R702 mutation hotspot (associated with the most severe human MYH9-RD phenotype).
   - Homozygous R702C: embryonic lethal (E10.5–11.5).
   - Heterozygous R702C: macrothrombocytopenia with leukocyte inclusion bodies (recapitulating Döhle-body-like inclusions), renal glomerulosclerosis with abnormal albumin/creatinine ratios, and **hearing disability** — this model, unlike the null, **does recapitulate multi-organ MYH9-RD features including hearing impairment**, supporting the dominant-negative mutant-protein mechanism over haploinsufficiency.
   - This is consistent with a broader review of "Mouse models of MYH9-related disease: mutations in nonmuscle myosin II-A" summarizing that missense knock-in models (not simple knockouts) are required to recapitulate the human phenotype [(PMC3251230)](https://ncbi.nlm.nih.gov/pmc/articles/PMC3251230).

3. **Rat cochlea expression studies** (non-genetic model, expression mapping only): RT-PCR and immunohistochemistry confirmed native Myh9 expression in the organ of Corti, spiral ligament, and Reissner's membrane, supporting biological plausibility of the human mutation's tissue-specific effects [(PMC1288554)](https://pmc.ncbi.nlm.nih.gov/articles/PMC1288554/); further work localized Myh9 specifically within cochlear **stereocilia** [(PMID:16862555)](https://pubmed.ncbi.nlm.nih.gov/16862555/) and characterized its developmental expression pattern in the inner ear [(PMID:15079858)](https://pubmed.ncbi.nlm.nih.gov/15079858/).

**Modeling implications for curation:** This is a clear case where **a simple gene-knockout mouse model FAILS to recapitulate the human phenotype (FAILS_TO_RECAPITULATE)**, while a **missense knock-in model matched to a specific human pathogenic hotspot (R702C) DOES recapitulate it (RECAPITULATES/PARTIALLY_RECAPITULATES)**. This is directly informative for modeling the mechanism as dominant-negative rather than loss-of-function/haploinsufficient, and should be reflected explicitly (e.g., via `modeled_mechanisms` links with contrasting `relationship` values) if curated into a mechanism graph.

---

## Summary Table of Suggested Ontology Terms

| Category | Suggested term(s) |
|---|---|
| Disease | MONDO (per GARD/NORD listing); OMIM #603622; DOID:0110548 |
| Causal gene | hgnc:7579 (MYH9) |
| Phenotype | HP:0000407 (Sensorineural hearing impairment); HP:0000410/HP:0000362 (Progressive hearing impairment) |
| Cell types | CL:0002165 (outer hair cell of Corti's organ); CL:0002167 (inner hair cell of Corti's organ) |
| Anatomy | UBERON:0001844 (organ of Corti); UBERON:0002068 (Reissner's membrane); UBERON:0002261 (spiral ligament) |
| Biological process | GO:0030036 (actin cytoskeleton organization); GO:0007605 (sensory perception of sound); GO:0060121 (inner ear receptor cell stereocilium organization) |
| Molecular function | GO:0000146/GO:0003774 (motor activity) |
| Cellular component | GO:0032420 (stereocilium); GO:0016459 (myosin complex) |
| Treatment | NCIT:C15329 (Surgical Procedure — cochlear implant); NCIT:C15240 (Genetic Counseling) |
| Model organism gene | Mouse *Myh9* ortholog (MGI) |

---

## Key Primary Literature (PMID-cited)

1. Lalwani AK et al. 1999. "A new locus for nonsyndromic hereditary hearing impairment, DFNA17, maps to chromosome 22 and represents a gene for cochleosaccular degeneration." PMID:[9915977](https://pubmed.ncbi.nlm.nih.gov/9915977/)
2. Lalwani AK et al. 2000. "Human nonsyndromic hereditary deafness DFNA17 is due to a mutation in nonmuscle myosin MYH9." PMID:[11023810](https://pubmed.ncbi.nlm.nih.gov/11023810/) (full text: [PMC1288554](https://pmc.ncbi.nlm.nih.gov/articles/PMC1288554/))
3. Seri M et al. 2000. "Mutations in MYH9 result in the May-Hegglin anomaly, and Fechtner and Sebastian syndromes." Nat Genet. [ng0900_103](https://www.nature.com/articles/ng0900_103)
4. Kim TB et al. 2007. "Cochlear implants for DFNA17 deafness." PMID:[17146397](https://pubmed.ncbi.nlm.nih.gov/17146397/)
5. Parker LL et al. 2006. "Absence of hearing loss in a mouse model for DFNA17 and MYH9-related disease." PMID:[16630581](https://pubmed.ncbi.nlm.nih.gov/16630581/)
6. Suzuki N et al. 2013. "Establishment of Mouse Model of MYH9 Disorders: Heterozygous R702C Mutation..." PMC:[3748045](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3748045/)
7. Verver EJJ et al. 2015. "R705H mutation of MYH9 is associated with MYH9-related disease and not only with non-syndromic deafness DFNA17." PMID:[24890873](https://pubmed.ncbi.nlm.nih.gov/24890873/)
8. de Heer AM et al. 2015 (Brazilian family). "c.G2114A MYH9 mutation (DFNA17) causes non-syndromic autosomal dominant hearing loss in a Brazilian family." PMID:[25505834](https://pubmed.ncbi.nlm.nih.gov/25505834/)
9. GeneReviews: Saposnik B, Aviner S, Verver EJJ, et al. "MYH9-Related Disease." [NBK2689](https://www.ncbi.nlm.nih.gov/books/NBK2689/) (updated periodically; primary comprehensive clinical synthesis)
10. OMIM #603622. "Deafness, Autosomal Dominant 17; DFNA17." [omim.org/entry/603622](https://omim.org/entry/603622)
11. 2026 Japanese cohort. "The Clinical Details of MYH9-Related Disease and DFNA17 in a Large Japanese Hearing Loss Cohort." Genes 17(2):154. [PMC12941242](https://pmc.ncbi.nlm.nih.gov/articles/PMC12941242/)
12. 2025 MYH9/MYH14 comparison. "The audiological phenotype of patients with a variant in MYH9 and MYH14 genes." Sci Rep. [PMC12219520](https://pmc.ncbi.nlm.nih.gov/articles/PMC12219520/)

---

**Note on evidence gaps:** No dedicated single-cell/spatial transcriptomic, proteomic, or CRISPR-screen data specific to DFNA17/MYH9 cochlear pathophysiology in humans were located in this search — mechanistic understanding rests primarily on rodent expression mapping and knock-in mouse models rather than direct human inner-ear molecular profiling (inner ear tissue being very difficult to obtain from living patients). This represents a genuine `KNOWLEDGE_GAP` for curation purposes, and the mouse knockout-vs-knock-in discordance (Section 15) should be flagged explicitly as a `HUMAN_MODEL_MISMATCH` if incorporated into a mechanism module.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 19 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| References weighed for topical relevance | 18 |
| On topic | 17 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `DOI:10.3390/genes17020154)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12941242/` (1 mention) - Identifier did not resolve to a record