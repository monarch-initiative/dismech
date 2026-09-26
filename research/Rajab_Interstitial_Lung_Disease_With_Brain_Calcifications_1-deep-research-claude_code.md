---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-06T00:36:47.705279'
end_time: '2026-09-06T00:43:42.162768'
duration_seconds: 414.46
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Rajab Interstitial Lung Disease With Brain Calcifications 1
  mondo_id: MONDO:0100215
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
  web_search_requests: 40
  num_turns: 48
  total_cost_usd: 2.3459139999999996
  session_id: 23e0b693-4c33-5868-888b-9a62047e1e75
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  - Read
  assistant_text_blocks: 3
citation_count: 23
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Rajab Interstitial Lung Disease With Brain Calcifications 1
- **MONDO ID:** MONDO:0100215 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Rajab Interstitial Lung Disease With Brain Calcifications 1** covering all of the
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

**Present this section as an ordered causal chain first, then the detail below.**
Open with a numbered sequence of mechanistic steps running from the initiating
lesion (mutation, exposure, infection) to the clinical manifestation, one step per
line, each naming what it causes next. State the causal verb explicitly ("leads
to", "results in") and say where a step is inferred rather than demonstrated.
Where the mechanism branches, show the branch. The categories below are a
checklist of what to cover within those steps, not the organizing structure —
a step may draw on several of them, and a category may contribute to several
steps.

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

I'll research this disease using web searches and primary literature sources.

WebFetch appears to be down via the proxy right now, so I'll rely on WebSearch (which is working) for comprehensive coverage, running many targeted queries in parallel.

I now have sufficient primary-literature coverage to compile the full report.

---

# Rajab Interstitial Lung Disease with Brain Calcifications 1 (RILDBC1) — Comprehensive Research Report

**MONDO:0100215 | OMIM #613658 | Orphanet ORPHA:178506 | Gene: *FARSB* (OMIM *609690, HGNC:17800, chr2q36.1)**

---

## 1. Disease Information

**Overview.** Rajab interstitial lung disease with brain calcifications 1 (RILDBC1) is a rare, autosomal recessive, multisystem disorder of highly variable severity — ranging from a relatively mild neurodevelopmental phenotype to a lethal infantile multi-organ disease. It is caused by biallelic (homozygous or compound heterozygous) loss-of-function variants in *FARSB*, which encodes the beta subunit of cytoplasmic phenylalanyl-tRNA synthetase (FARS1/PheRS). The disease is one of two genetically distinct forms of "Rajab interstitial lung disease with brain calcifications": RILDBC1 (*FARSB*, OMIM #613658) and RILDBC2 (*FARSA*, OMIM #619013), which together with related reports form the broader "FARS1-related disorder" spectrum (Schuch et al., 2021, *Clin Genet* 99:789–801, DOI:10.1111/cge.13943, [ResearchGate PDF](https://www.researchgate.net/publication/349463869_FARS1-related_disorders_caused_by_bi-allelic_mutations_in_cytosolic_phenylalanyl-tRNA_synthetase_genes_Look_beyond_the_lungs)).

Most affected individuals present in infancy or early childhood with intrauterine growth restriction (IUGR), poor growth/failure to thrive, and progressive, sometimes fatal, interstitial lung disease (ILD). Additional features include developmental delay, hypotonia, liver dysfunction, and — in a subset — skeletal, renal, and vascular (cerebral aneurysm) abnormalities. Neuroimaging in nearly all reported patients shows characteristic bilateral, symmetric intracranial calcifications (basal ganglia, subcortical white matter, cerebellum, cortex), often with preserved myelination and normal-to-mildly-impaired cognition despite motor delay (OMIM #613658; [MedGen C3150910](https://www.ncbi.nlm.nih.gov/medgen/462260)).

**Key identifiers:**

| Resource | ID |
|---|---|
| OMIM (phenotype) | #613658 — RILDBC1 |
| OMIM (gene) | *609690 — *FARSB* |
| Orphanet | ORPHA:178506 — "Interstitial lung disease-brain calcification syndrome" (historically also "Brain calcification, Rajab type") |
| MONDO | MONDO:0100215 |
| MedGen | C3150910 |
| HGNC | 17800 (*FARSB*) |
| NCBI Gene | 10056 (*FARSB*) |
| Related disorder | RILDBC2, OMIM #619013 (*FARSA*, 602918) |

**Synonyms/alternative names:** RILDBC1; Rajab syndrome; brain calcification, Rajab type; FARS1-related disorder (FARSB-related); phenylalanyl-tRNA synthetase-related disease of growth restriction, brain calcification, and interstitial lung disease; recessive aminoacyl-tRNA synthetase (ARS1)-related disease.

**Data provenance.** Nearly all current knowledge derives from **aggregated case series and family reports** in the medical literature (not large EHR cohorts): the original clinical/linkage description of two consanguineous Omani kindreds (Rajab et al., 2009, *Am J Med Genet A* 149A:129–137, PMID:[19161147](https://pubmed.ncbi.nlm.nih.gov/19161147/), [PMC2800951](https://pmc.ncbi.nlm.nih.gov/articles/PMC2800951/)), the gene-identification papers (Zadjali et al. 2018; Antonellis et al. 2018; Xu/Ling et al. 2018 — see §4), subsequent case reports/series (Karimzadeh et al. 2022; others), and a systematic literature-review/phenotype paper (Schuch et al. 2021; Hoytema van Konijnenburg et al. 2025, *J Inherit Metab Dis*, DOI:10.1002/jimd.70017). As of 2026, media coverage of a newly diagnosed U.S. toddler (Wrenley Lantaff, diagnosed October 2025) reiterates that only "about 10" cases have been formally reported worldwide ([Respiratory Therapy, 2026](https://respiratory-therapy.com/disorders-diseases/chronic-pulmonary-disorders/chronic-diseases/first-us-toddler-diagnosed-with-rare-lung-disease/); [14 News, July 2026](https://www.14news.com/2026/07/13/pike-county-toddler-is-first-us-child-diagnosed-with-rare-lung-disease/)) — this figure should be treated as an approximate, informally tracked count rather than a registry-verified prevalence estimate.

---

## 2. Etiology

**Disease causal factors — genetic/mechanistic, monogenic.** RILDBC1 is caused by biallelic (homozygous or compound heterozygous) pathogenic variants in *FARSB*, which reduce or abolish function of cytoplasmic phenylalanyl-tRNA synthetase (FARS1/PheRS), the enzyme that charges tRNA^Phe with phenylalanine during protein translation and additionally appears to have non-canonical/non-translational roles important to vascular and pulmonary tissue homeostasis (Xu et al., 2018, *AJHG* 103:100–114, PMID:[29979980](https://pubmed.ncbi.nlm.nih.gov/29979980/), [PMC6035289](https://pmc.ncbi.nlm.nih.gov/articles/PMC6035289/)). There is no known infectious, toxic, or purely environmental cause; RILDBC1 is a purely Mendelian (single-gene) disorder.

**Genetic risk factors:**
- **Causal biallelic variants in *FARSB*** (2q36.1) — see §4 for specific alleles.
- **Consanguinity** is a strong risk factor for homozygosity at this rare recessive locus: essentially all reported kindreds are from consanguineous unions (Omani, Iranian, and other Middle Eastern families are over-represented in the literature).
- **Founder variant**: c.853G>A (p.Glu285Lys) segregates as a founder allele in an extended Omani kindred (8 affected individuals; Zadjali et al., 2018, *Hum Mutat* 39:1355–1359, PMID:[30014610](https://pubmed.ncbi.nlm.nih.gov/30014610/)) — this variant is absent from gnomAD, ExAC, 1000 Genomes, and Iranome, consistent with a rare, population-restricted allele rather than a common polymorphism.
- **Modifier/severity factors**: Genotype (null/loss-of-function vs. hypomorphic missense; homozygous vs. compound heterozygous) appears to correlate with phenotypic severity across the FARS1-related-disorder spectrum, per the pooled genotype–phenotype analysis in Schuch et al. (2021) and Hoytema van Konijnenburg et al. (2025) — patients with near-complete loss of FARSB/FARS1 activity (e.g., the compound-heterozygous T256M + frameshift patient of Antonellis et al. 2018, with 97% reduction of FARSB protein) tend toward the most severe, early-lethal end of the spectrum.

**Environmental risk factors:** None have been identified as causal. Given the pulmonary phenotype, it is plausible (but not established in the literature reviewed here) that intercurrent respiratory infections or environmental lung insults could exacerbate the interstitial lung disease course, analogous to other genetic pediatric ILDs — this should be treated as an inference, not a documented finding for RILDBC1 specifically.

**Protective factors:** None reported. No protective genetic variants, modifier alleles, or environmental/lifestyle protective factors are described in the literature identified.

**Gene–environment interactions:** Not established for this monogenic disorder; no GxE studies were identified.

---

## 3. Phenotypes

RILDBC1 is multisystemic. Frequencies below are qualitative ("most," "some," "occasional") as reported by OMIM's clinical synopsis aggregation and the case series/reviews cited, since no large denominator cohort exists to generate precise percentages.

### Pulmonary
| Phenotype | Notes | Suggested HP term* |
|---|---|---|
| Interstitial lung disease | Core, near-universal feature; progressive, can be fatal | HP:0006530 (Interstitial pneumonitis) |
| Cholesterol pneumonitis (histologic pattern) | Intra-alveolar/interstitial cholesterol granulomas on lung biopsy — an early, characteristic histologic signature across FARS1-related disease (Schuch et al. 2021) | — (histopathologic finding; consider NCIT/SNOMED coding) |
| Recurrent respiratory infections/failure | Reported in severe cases | HP:0002205 / HP:0002205-adjacent terms |
| Pneumothorax (in a subset, per the *FARSB* c.848+1G>A cohort) | Xu et al. 2018 | HP:0002107 |

### Neurological / CNS
| Phenotype | Notes | Suggested HP term* |
|---|---|---|
| Intracranial (brain) calcifications | Bilateral, symmetric; basal ganglia, subcortical cerebrum, cerebellum, subcortical nuclei; nearly universal finding on neuroimaging | HP:0002514 (verify — "Basal ganglia calcification"-type term) or a general "Intracranial calcification" term |
| Periventricular cysts | Reported particularly in RILDBC2 (*FARSA*) but also in some RILDBC1 patients | — |
| Cerebral volume loss / atrophy | Reported | HP:0002087 (adjust) |
| Incomplete closure of the Sylvian fissures | Distinctive imaging feature | — |
| Preserved (normal) myelination | Distinguishes from many leukodystrophies/AGS | — |
| Developmental delay | Mild-to-moderate in Omani cohort; cognition often relatively preserved | HP:0001263 |
| Microcephaly | Reported in the original Omani kindreds | HP:0000252 |
| Hypotonia | Common | HP:0001252 |
| Motor developmental delay | Some patients | HP:0001270 |
| Cerebral/intracranial aneurysms | Reported in the Xu et al. 2018 cohort (vascular/connective-tissue component) | HP:0004944 |

### Hepatic
| Phenotype | Notes |
|---|---|
| Liver dysfunction / cirrhosis | Reported across the spectrum; more prominent in RILDBC2 (*FARSA*) but also seen in FARSB patients (Xu et al. 2018) |
| Hepatosplenomegaly | Reported, e.g., diagnosed before age 2 in RILDBC2-type presentations; hepatomegaly/abdominal distension was also the presenting sign in the 2025–2026 U.S. case (progressing to liver failure) |
| Cholestasis / coagulopathy | Reported in the broader FARS1-deficiency literature (more consistently documented for *FARSA*) |

### Skeletal / Renal / Other
| Phenotype | Notes |
|---|---|
| Osteopenia | Documented in the original Omani families |
| Skeletal abnormalities (scoliosis, pectus deformity) | Reported in the Xu et al. cohort — framed as connective-tissue involvement |
| Renal abnormalities | Reported but non-specific and inconsistent across families |
| Intestinal malrotation | Reported in at least one cohort |
| Facial dysmorphism | Variable, reported in the broader FARS1 literature |

**Phenotype characteristics:**
- **Onset**: Most patients present in infancy/early childhood; some features (IUGR) are prenatal.
- **Severity/progression**: Highly variable — from a milder, largely neurodevelopmental/skeletal phenotype without early lethality (original Omani kindreds, Rajab et al. 2009) to a rapidly progressive, fatal multisystem disease in infancy (Antonellis et al. 2018 patient died at 32 months; the 2025–2026 U.S. patient developed liver failure awaiting transplant).
- **Neurological course**: A notable feature emphasized by Rajab et al. (2009) is the **absence of progressive neurological deterioration** despite static brain calcifications — this distinguishes RILDBC from progressive leukoencephalopathies.
- **Quality-of-life impact**: Not formally studied with standardized instruments (no EQ-5D/SF-36/PedsQL data identified). Qualitatively, disease burden is driven by respiratory insufficiency, growth failure, and (when present) liver failure requiring transplantation; developmental/cognitive impact is comparatively mild in most reported patients.

*HP term IDs above are best-effort suggestions based on standard HPO nomenclature for these clinical concepts; **exact CURIEs should be verified against the HPO browser/OAK before curation**, per this KB's ontology-term contract — some (e.g., the specific basal-ganglia-calcification and cerebral-volume-loss terms) were not independently confirmed via a live HPO lookup in this research session.

---

## 4. Genetic / Molecular Information

**Gene:** *FARSB* — Phenylalanyl-tRNA synthetase subunit beta (aliases: FARSLB, FRSB, PheHB, PheRS-beta). HGNC:17800; NCBI Gene ID 10056; OMIM *609690; located at chromosome **2q36.1** (GRCh38: chr2:222,566,899–222,656,092). Encodes a 589-amino-acid, ~66 kDa protein.

**Function:** Cytoplasmic phenylalanyl-tRNA synthetase (FARS1/PheRS) is a heterotetramer (α2β2): two catalytic alpha subunits (*FARSA*, OMIM *602918) and two regulatory beta subunits (*FARSB*). In the presence of ATP, the enzyme charges tRNA^Phe with L-phenylalanine, an essential step in cytoplasmic mRNA translation. Beyond canonical aminoacylation, evidence supports **non-canonical (non-translational) functions** of FARS1 relevant to vascular and pulmonary development/homeostasis (Xu et al., 2018, PMID:29979980).

**Causal variants reported to date** (biallelic in all cases; autosomal recessive):

| Variant (cDNA/protein) | Zygosity | Patients | Publication |
|---|---|---|---|
| c.853G>A, p.Glu285Lys (homozygous founder allele) | Homozygous | 8 individuals, extended consanguineous Omani kindred | Zadjali et al. 2018, *Hum Mutat* 39:1355–1359, PMID:[30014610](https://pubmed.ncbi.nlm.nih.gov/30014610/) |
| c.767C>T, p.Thr256Met (editing-domain missense) + c.1486delCinsAA, p.His496LysfsTer14 (frameshift) | Compound heterozygous | 1 boy (died at 32 months) | Antonellis et al. 2018, *Hum Mutat* 39:834–840, PMID:[29573043](https://pubmed.ncbi.nlm.nih.gov/29573043/) |
| c.848+1G>A (5′ splice-junction variant, causing exon skipping/frameshift, loss-of-function) + six distinct missense variants (one shared between unrelated individuals) | Compound heterozygous / biallelic | 5 individuals, 4 families | Xu et al. 2018, *AJHG* 103:100–114, PMID:[29979980](https://pubmed.ncbi.nlm.nih.gov/29979980/) |
| c.1618+17G>A | — | Reported in ClinVar | [ClinVar RCV002494045](https://www.ncbi.nlm.nih.gov/clinvar/RCV002494045/) |

**Functional consequences:** Western blot in the Antonellis et al. (2018) patient's fibroblasts showed a **97% reduction in FARSB protein** and a **66% reduction in FARSA protein** relative to controls, indicating that loss of the beta (regulatory) subunit destabilizes the catalytic alpha subunit and severely impairs holoenzyme (FARS1) activity — consistent with a **loss-of-function** mechanism. The c.848+1G>A splice variant similarly produces decreased transcript/protein levels, again consistent with loss-of-function.

**Variant classification:** Reported variants are classified pathogenic/likely pathogenic under ACMG/AMP criteria based on segregation with disease, absence/extreme rarity in population databases (gnomAD, ExAC, 1000 Genomes, Iranome all show zero frequency for the E285K founder allele), and functional/protein-level evidence of loss-of-function.

**Allele frequency:** All reported pathogenic *FARSB* variants are private or population-restricted (e.g., the Omani founder E285K allele) and are essentially absent from gnomAD — consistent with the disease's extreme rarity.

**Somatic vs. germline:** Exclusively germline (constitutional), autosomal recessive.

**Modifier genes:** None specifically identified for *FARSB*-related disease; genotype (allele severity, e.g., null vs. hypomorphic) itself functions as the principal determinant of phenotypic severity across the FARS1-related-disorder spectrum (Schuch et al. 2021; Hoytema van Konijnenburg et al. 2025).

**Epigenetic information / chromosomal abnormalities:** None reported specific to RILDBC1; this is a classic monogenic sequence-variant disorder, not a copy-number or epigenetic condition.

**Related gene — *FARSA*:** Biallelic *FARSA* variants cause the phenotypically overlapping but genetically distinct RILDBC2 (OMIM #619013), and a growing, partially overlapping literature on "FARSA deficiency" describes neonatal cholestasis progressing to multisystem disease with liver cirrhosis (Aelvoet et al. 2025, *JIMD Reports*), systemic inflammatory syndrome (PMC9303323), and fatal systemic disease (PMC9344665) — useful comparator literature for curating the *FARSB* entry's "related disorders" context.

---

## 5. Environmental Information

No environmental, occupational, toxic, or lifestyle causal or contributory factors have been identified for RILDBC1 in the literature reviewed — it is a purely monogenic autosomal recessive disorder. No infectious agents are implicated (notably, the brain-calcification phenotype must be actively distinguished from **congenital TORCH infections**, which are a key differential diagnosis rather than a cause — see §10 differential diagnosis). No CTD/TOXNET/EPA entries or infectious-agent associations were found.

---

## 6. Mechanism / Pathophysiology

### Causal chain (numbered, from molecular lesion to clinical phenotype)

1. **Biallelic loss-of-function variants in *FARSB*** (missense in the editing/catalytic-interface domain, frameshift, or splice-donor variants) *lead to* markedly reduced steady-state FARSB protein (up to ~97% reduction demonstrated by Western blot in patient fibroblasts).
2. Reduced FARSB *leads to* destabilization/co-depletion of its obligate heterotetramer partner, the FARSA catalytic subunit (a ~66% reduction in FARSA protein was demonstrated in the same patient), because FARS1 (α2β2 PheRS) assembly requires stoichiometric beta subunit.
3. Loss of holoenzyme (FARS1) abundance/activity *results in* impaired charging of tRNA^Phe with phenylalanine — impairing canonical cytoplasmic mRNA translation capacity, particularly in tissues with high translational/proteostatic demand.
4. In parallel — and this is an **inferred, not fully demonstrated**, branch — evidence from Xu et al. (2018) supports a **non-canonical, non-translational function** of FARS1 that is specifically required for normal pulmonary and vascular tissue integrity; disruption of this non-translational role is proposed (rather than conclusively proven) to contribute independently to the lung and vascular phenotypes, distinguishing this disease's pathogenesis from a "simple" translation-insufficiency model common to other aminoacyl-tRNA synthetase disorders.
5. Combined translational impairment and disrupted non-canonical FARS1 function in the lung *lead to* alveolar/interstitial injury with a distinctive histologic response: **cholesterol pneumonitis** (intra-alveolar and interstitial cholesterol granulomas), which *results in* progressive interstitial lung disease, impaired gas exchange, and — in severe cases — respiratory failure and death.
6. In the developing brain, disrupted FARS1 function is hypothesized (mechanism not fully elucidated) to *cause* a static, non-progressive process of **basal ganglia/subcortical calcification**, accompanied in some patients by developmental delay, hypotonia, and microcephaly, but — notably — **without progressive neurodegeneration**, distinguishing it mechanistically/clinically from progressive interferonopathies such as Aicardi–Goutières syndrome.
7. In the liver, impaired FARS1 function *leads to* hepatocellular dysfunction, manifesting as hepatomegaly/hepatosplenomegaly, cholestasis, and — in severe cases — progression to cirrhosis and liver failure requiring transplantation (as in the 2025–2026 U.S. index case).
8. In blood vessels and connective tissue, disrupted FARS1 function (again, an area where non-canonical function is implicated) is associated in a subset of patients with **cerebral/intracranial aneurysm formation** and skeletal connective-tissue features (scoliosis, pectus deformity), suggesting a vascular/connective-tissue mechanistic branch parallel to the pulmonary and neurological ones.
9. Growth failure (IUGR, failure to thrive, short stature, osteopenia) is best understood as a systemic consequence of chronic translational insufficiency and multi-organ disease burden rather than a single localized lesion.

### Detail by mechanistic category

- **Molecular pathways**: Aminoacyl-tRNA synthetase (aaRS) charging step of cytoplasmic mRNA translation (not a classical signaling cascade like Wnt/MAPK/mTOR); secondary proteostatic stress. GO term suggestions: **GO:0004826** (phenylalanine-tRNA ligase activity), **GO:0006432** (phenylalanyl-tRNA aminoacylation), **GO:0006418** (tRNA aminoacylation for protein translation).
- **Cellular processes**: Impaired protein synthesis; possible proteotoxic/proteostatic stress in high-translation-demand tissues (lung epithelium, hepatocytes, neurons); no direct evidence reviewed here for classical apoptosis/autophagy dysregulation specific to this disease, though such mechanisms are plausible extrapolations from general aaRS-disease biology.
- **Protein dysfunction**: Loss-of-function via (a) destabilizing missense substitutions in conserved domains (e.g., T256M in the "editing domain," E285K), (b) frameshift/premature truncation (His496LysfsTer14), and (c) splice-site disruption (c.848+1G>A) — all converging on reduced FARSB protein abundance and secondary FARSA co-depletion, i.e., loss of holoenzyme rather than a dominant-negative or gain-of-function mechanism.
- **Metabolic changes**: Not specifically characterized (no dedicated metabolomics studies identified); the primary metabolic lesion is at the level of amino-acid-charging of tRNA rather than a classical small-molecule metabolic pathway.
- **Immune system involvement**: Not a primary feature of RILDBC1 per se, though the related *FARSA*-deficiency literature describes a "systemic inflammatory syndrome" phenotype (PMC9303323) — raising the possibility of an inflammatory/immune contribution to the FARS1-disease spectrum broadly, not conclusively established for *FARSB* specifically.
- **Tissue damage mechanisms**: Cholesterol pneumonitis/granulomatous lung injury (lung); calcific deposition (brain); fibrosis/cirrhosis (liver) — the lung and liver findings both reflect a chronic injury-and-remodeling pattern; the exact cellular trigger for cholesterol accumulation in alveolar macrophages/interstitium is not fully elucidated in the literature reviewed.
- **Biochemical abnormalities**: Reduced/absent phenylalanyl-tRNA synthetase (FARS1) enzymatic activity, demonstrable by reduced FARSA/FARSB protein on Western blot in patient-derived fibroblasts (direct evidence, IN_VITRO, Antonellis et al. 2018).
- **Epigenetic changes**: None reported.
- **Molecular profiling**: No transcriptomic, proteomic, metabolomic, or single-cell/spatial datasets specific to RILDBC1/*FARSB* patient tissue were identified in this search; this remains an open evidence gap.
- **Cell types involved** (suggested CL terms): 
  - Type II pneumocyte (CL:0002063) — alveolar epithelium, relevant to ILD.
  - Alveolar macrophage (CL:0000583) — likely relevant to cholesterol granuloma formation (inferred).
  - Hepatocyte (CL:0000182) — liver dysfunction/cirrhosis.
  - Neuron (CL:0000540) / astrocyte (CL:0000127) — relevant to CNS calcification context (by analogy to other brain-calcification disorders; not directly demonstrated for *FARSB*).

**Upstream vs. downstream**: The *FARSB* loss-of-function lesion and consequent FARS1 holoenzyme deficiency are clearly upstream/initiating; the pulmonary (cholesterol pneumonitis/ILD), hepatic (cirrhosis), neurological (calcification, developmental delay), skeletal (osteopenia), and vascular (aneurysm) manifestations are downstream, organ-specific consequences that appear to arise largely in parallel rather than in a strict linear cascade from one another — i.e., this is best modeled as one causal trigger with several parallel downstream organ-specific branches, rather than a single linear chain (the ordered list above reflects that branching explicitly at steps 4–8).

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary**: Lungs (interstitial lung disease, cholesterol pneumonitis), brain (calcifications), liver (dysfunction/cirrhosis).
- **Secondary**: Skeleton (osteopenia, scoliosis, pectus deformity), kidneys (nonspecific renal abnormalities), cerebral vasculature (aneurysms), gastrointestinal tract (intestinal malrotation in some), craniofacial structures (dysmorphism in some).
- **Body systems**: Respiratory, nervous, hepatobiliary, skeletal, renal, cardiovascular (cerebrovascular).

**Suggested UBERON terms:**
- UBERON:0002048 (lung)
- UBERON:0000955 (brain) / UBERON:0002420 (basal ganglion)
- UBERON:0002107 (liver)
- UBERON:0001474 (bone element) — for skeletal involvement
- UBERON:0002113 (kidney)
- UBERON:0002049 (vasculature) / cerebral artery structures — for aneurysms

**Tissue/cell level:** Alveolar epithelium and interstitium (pulmonary), hepatocytes, basal ganglia/subcortical neural tissue and its vasculature (site of calcification), osteoblast/osteoclast-mediated bone tissue (osteopenia). Specific single-cell profiling of affected tissue was not identified.

**Subcellular level:** No cellular-compartment-specific pathology (e.g., mitochondrial, ER) is specifically implicated beyond the cytoplasmic localization of FARS1 itself (GO Cellular Component: **GO:0017101**, aminoacyl-tRNA synthetase multienzyme complex, or **GO:0005737** cytoplasm) — this is distinct from the mitochondrial *FARS2*-related disease (see §10 differential diagnosis), a common point of confusion given the similarly named gene.

**Localization/lateralization:** Brain calcifications are characteristically **bilateral and symmetric** (a distinguishing feature from many acquired/vascular calcification patterns).

---

## 8. Temporal Development

- **Onset**: Prenatal (IUGR) through infancy/early childhood for most features; the pulmonary and hepatic manifestations are typically first recognized in infancy or toddlerhood (e.g., the 2025–2026 U.S. index case first showed feeding difficulty, vomiting, and poor weight gain, with abdominal distension noted in toddlerhood).
- **Onset pattern**: Generally insidious/subacute for growth failure and neurodevelopmental features; can be more acute for pulmonary decompensation or liver failure.
- **Progression**: **Highly variable across reported patients** — from a comparatively stable, non-progressive course dominated by static brain findings and mild developmental delay (original Omani kindreds) to rapid, fatal multisystem progression in infancy (death at 32 months in the Antonellis et al. patient; the current U.S. patient in liver failure awaiting transplant). A key emphasized feature (Rajab et al. 2009) is that neurological findings, despite radiographically striking calcifications, generally do **not** show progressive deterioration — differentiating the neurological course from progressive interferonopathies.
- **Disease course pattern**: Chronic; can be stable (neurological) while progressive in other organs (lung, liver) within the same patient.
- **Duration**: Lifelong for survivors; disease can be fatal in infancy/early childhood in severe cases.
- **Remission**: Not described — this is not a relapsing-remitting condition.
- **Critical periods**: Infancy/early childhood is the critical period both for diagnosis (symptom onset) and for the highest mortality risk (progressive ILD, liver failure).

---

## 9. Inheritance and Population

**Epidemiology:**
- **Prevalence**: Orphanet lists ORPHA:178506 ("Interstitial lung disease-brain calcification syndrome") prevalence as **<1/1,000,000**.
- Approximately **10 or fewer molecularly confirmed cases** have been reported in the literature/media as of 2026, spanning the original Omani kindred (8 individuals), the Antonellis et al. 2018 patient, the Xu et al. 2018 cohort (5 individuals/4 families), the Karimzadeh et al. 2022 Iranian siblings, and the 2025-diagnosed U.S. toddler — noting overlap/possible double-counting across these reports is plausible and a rigorous unique-patient census was not attempted here.
- No incidence estimates, sex-ratio data, or age-distribution statistics were identified — consistent with the disease's extreme rarity and absence of large-scale registries.

**Inheritance pattern**: **Autosomal recessive.**

**Penetrance**: Presumed complete for the reported biallelic loss-of-function genotypes, though this has not been formally studied given the small number of cases; phenotypic expressivity is markedly variable (see §8).

**Expressivity**: **Markedly variable** — from a relatively mild neurodevelopmental/skeletal phenotype to fatal infantile multisystem disease, apparently correlating in part with the severity of the underlying variant(s) (null/loss-of-function vs. partial hypomorph) per the pooled analysis in Schuch et al. (2021) and Hoytema van Konijnenburg et al. (2025).

**Genetic anticipation**: Not applicable/not reported (not a repeat-expansion disorder).

**Germline mosaicism**: Not specifically reported for *FARSB*.

**Founder effects**: A **founder allele, c.853G>A (p.Glu285Lys), segregates in an extended consanguineous Omani kindred** (Zadjali et al. 2018) — the clearest documented founder effect for this gene.

**Consanguinity**: A major contributing factor — the majority of reported families (Omani, Iranian) are consanguineous, consistent with autosomal recessive inheritance of a very rare allele.

**Carrier frequency**: Not established in population databases; the causal alleles are essentially absent from gnomAD, ExAC, 1000 Genomes, and Iranome.

**Population demographics**: Reported cases cluster in Middle Eastern populations (Oman, Iran) with documented consanguinity, plus at least one North American (U.S.) case (2025–2026, ancestry not specified in available reporting) and cases reported from other unspecified families in the Xu et al. 2018 cohort. No robust geographic-distribution or ethnic-prevalence data exist beyond these case reports.

---

## 10. Diagnostics

**Clinical tests:**
- **Chest imaging** (CT): identifies interstitial lung disease pattern.
- **Lung biopsy/histopathology**: characteristic finding is **cholesterol pneumonitis** — intra-alveolar and interstitial cholesterol granulomas — described as an early, distinguishing histologic feature across the FARS1-related-disorder spectrum (Schuch et al. 2021).
- **Brain imaging (CT/MRI)**: bilateral, symmetric calcifications of basal ganglia, subcortical white matter, cerebellum, and cortex; periventricular cysts (more typical of RILDBC2); preserved myelination; incomplete Sylvian fissure closure; cerebral volume loss.
- **Liver function tests / liver biopsy**: assess for cholestasis, coagulopathy, cirrhosis.
- **Skeletal survey**: for osteopenia, scoliosis, pectus deformity.
- **Functional/biochemical assay**: FARS1 (PheRS) enzymatic activity or FARSA/FARSB protein levels can be assessed in patient-derived fibroblasts by Western blot, as demonstrated in Antonellis et al. (2018) — a research-grade rather than routine clinical assay.

**Genetic testing:**
- **Recommended approach**: Given the extreme rarity and phenotypic overlap with other genetic ILD/brain-calcification syndromes, **whole-exome sequencing (WES)** is the diagnostic modality used in essentially all published cases (Zadjali et al. 2018; Antonellis et al. 2018; Xu et al. 2018), often following genome-wide linkage analysis in consanguineous families. **Whole-genome sequencing (WGS)** would be expected to have similar or greater utility, particularly for detecting the reported splice-region variants, but was not the primary method used historically for this gene.
- **Gene panels**: A *FARSB* single-gene test or a targeted panel for genetic pediatric interstitial lung disease (chILD) / aminoacyl-tRNA synthetase-related disease panels would be expected to include *FARSB* and *FARSA*; specific commercial panel names were not catalogued in this search.
- **Single-gene testing**: Feasible once a specific familial variant or strong phenotypic suspicion exists (e.g., in a consanguineous family from a population with a known founder allele).
- **Chromosomal microarray/karyotype/FISH**: Not informative — this is a sequence-variant (not copy-number or structural chromosomal) disorder.
- **Mitochondrial DNA testing**: Not relevant to *FARSB* (cytoplasmic enzyme) — **important differential-diagnostic caveat**: do not confuse with *FARS2* (mitochondrial phenylalanyl-tRNA synthetase), which causes a clinically distinct, unrelated mitochondrial disease ("FARS2 deficiency," covered by its own GeneReviews chapter, NCBI Bookshelf NBK538658) with combined oxidative phosphorylation deficiency and epilepsy — a naming-based confusion risk worth flagging explicitly during curation.

**Clinical criteria:** No formal consensus diagnostic criteria (e.g., DSM/ICD-style) exist for this ultra-rare disorder; diagnosis rests on the combination of characteristic multisystem phenotype (ILD + brain calcification + growth failure ± liver/skeletal/renal findings) plus molecular confirmation of biallelic *FARSB* variants.

**Differential diagnosis** (as explicitly discussed by Rajab et al. 2009 and general brain-calcification-syndrome literature):
- **Aicardi–Goutières syndrome (AGS)** — considered and explicitly distinguished by Rajab et al. (2009); AGS typically shows progressive neurological deterioration, elevated CSF interferon-alpha/CSF lymphocytosis, and leukodystrophy, which are not features of RILDBC1.
- **Coats plus syndrome** — also explicitly considered and excluded by Rajab et al. (2009) based on divergent clinical features.
- **Congenital TORCH infections** (CMV, toxoplasmosis, etc.) — can produce intracranial calcifications and hepatosplenomegaly; excluded by negative infectious serologies/PCR.
- ***FARSA*-related disease (RILDBC2)** — clinically overlapping (ILD, liver disease, brain calcifications/periventricular cysts) but genetically distinct; distinguished by molecular testing.
- ***FARS2* deficiency** (mitochondrial PheRS) — a different, unrelated disease despite the similar gene name; distinguished by molecular testing and by its distinct clinical/biochemical (mitochondrial) profile.
- Other genetic pediatric interstitial lung diseases (e.g., surfactant protein gene disorders — *SFTPC*, *ABCA3*) — distinguished by the combination of brain calcification and multisystem (hepatic/skeletal) involvement, which is atypical for isolated surfactant dysfunction disorders.
- Primary familial brain calcification (PFBC) — typically adult-onset and without the pulmonary/hepatic phenotype; distinguished on clinical grounds and by molecular testing (PFBC genes: *SLC20A2*, *PDGFB*, *PDGFRB*, *XPR1*, *MYORG*).

**Screening:** No population or newborn screening program exists for this ultra-rare condition; case-finding is clinical (presentation with ILD/growth failure/brain calcification) followed by genetic confirmation. Carrier screening could theoretically be offered in populations with a known founder allele (e.g., the Omani E285K allele) for at-risk consanguineous families, though this was not explicitly documented as an established practice in the sources reviewed.

---

## 11. Outcome / Prognosis

- **Survival/mortality**: Highly variable. Some reported patients (original Omani kindred) survived into childhood with relatively stable neurological status; others died in infancy/early childhood from progressive respiratory failure (e.g., death at 32 months, Antonellis et al. 2018). No formal survival curves, 5-/10-year survival rates, or standardized mortality statistics exist given the very small number of published cases.
- **Life expectancy**: Not quantifiable from available data; ranges from early childhood death (severe genotype/phenotype) to survival into later childhood/beyond with chronic multisystem morbidity (milder genotype/phenotype).
- **Morbidity/function**: Chronic respiratory insufficiency, growth failure/short stature, variable developmental/motor impairment (cognition often relatively spared), and — in severe cases — progressive liver disease culminating in liver failure requiring transplantation (illustrated by the 2025–2026 U.S. case).
- **Complications**: Progressive interstitial lung disease/respiratory failure; hepatic cirrhosis/liver failure; cerebral aneurysm (vascular complication risk in a subset of patients, per Xu et al. 2018); recurrent infections; skeletal deformity (scoliosis).
- **Recovery potential**: No curative treatment exists; clinical course is managed supportively. In the FARS1-disease spectrum broadly, amino-acid supplementation has shown benefit for some organ systems in some patients (see §12) but does not reliably prevent the most severe phenotypes.
- **Prognostic factors**: Genotype severity (null/loss-of-function vs. partial-function alleles) appears to be the principal prognostic determinant identified in the pooled literature (Schuch et al. 2021; Hoytema van Konijnenburg et al. 2025), though formal statistical genotype–phenotype correlation studies with adequate sample size do not exist given the rarity of the disease.
- **Prognostic biomarkers**: None validated; residual FARS1 enzymatic activity/protein level (measured in patient fibroblasts) is a research-level correlate of severity rather than a clinically validated prognostic biomarker.

---

## 12. Treatment

There is **no disease-specific approved therapy** for RILDBC1; management is supportive and organ-directed, informed by the broader FARS1-related-disorder / aminoacyl-tRNA synthetase (ARS1)-deficiency literature.

**Pharmacotherapy / experimental disease-modifying approach:**
- **Cognate amino acid supplementation** (i.e., supplementation with phenylalanine, the amino acid product of the deficient enzyme's charging reaction, by analogy with strategies used in other aaRS deficiencies) has been described across the pooled FARS1-related-disorder literature: Hoytema van Konijnenburg et al. (2025, *J Inherit Metab Dis*, DOI:10.1002/jimd.70017) report that amino-acid supplementation was attempted in a substantial number of patients (reported in the broader FARS1-deficiency literature as having been tried in roughly two dozen patients across the *FARSA*/*FARSB* spectrum) with **beneficial effects on growth, development, and liver/lung disease in the majority**, but with **poor response in the most severely affected patients**, and with difficulty distinguishing true treatment effect from natural disease history given the absence of controlled trials. This should be treated as a **general FARS1-related-disorder therapeutic strategy**, not a treatment specifically validated in a controlled trial for *FARSB*/RILDBC1 alone. Suggested NCIT term: NCIT:C15447 (Dietary Intervention) or NCIT:C15433 (Nutritional Support), used cautiously per this KB's guidance that supplement-type interventions frequently name a specific compound rather than a behavioral/dietary pattern.
- No small-molecule, enzyme-replacement, gene-therapy, or RNA-based therapy specific to *FARSB*/RILDBC1 was identified in the literature reviewed.

**Advanced therapeutics:** None reported — no gene therapy, cell therapy, or targeted molecular therapy specific to this disease has reached even early clinical description.

**Surgical/interventional:**
- **Liver transplantation** — required in the most severe hepatic phenotype (the 2025–2026 U.S. index case was reported awaiting liver transplant for progressive liver failure). Suggested NCIT term: NCIT:C15289 (Organ Transplantation).
- Management of cerebral aneurysms, where present, would follow standard neurovascular/neurosurgical practice (not specifically described for this disease in the literature reviewed).
- Orthopedic management (e.g., for scoliosis) as clinically indicated — NCIT:C16186 (Orthopedic Surgical Procedure).

**Supportive and rehabilitative care:**
- Nutritional support for growth failure/failure to thrive (NCIT:C15447 Dietary Intervention).
- Respiratory supportive care (supplemental oxygen, management of infections, and — in end-stage disease — consideration of lung transplantation, though no specific report of lung transplantation for RILDBC1 was identified in this search) — NCIT:C15747 (Supportive Care).
- Physical/occupational therapy for hypotonia and motor delay (NCIT:C15302 Physical Therapy).
- Immunomodulatory therapy for interstitial lung disease is used empirically in genetic pediatric ILDs generally (corticosteroids, hydroxychloroquine), but no report specifically documenting these agents' use or efficacy in RILDBC1/*FARSB*-confirmed patients was identified in this search — this should be flagged as an evidence gap rather than asserted as an established RILDBC1 treatment.

**Genetic counseling** — recommended for families given the autosomal recessive inheritance pattern and elevated recurrence risk (25% per pregnancy for carrier couples), particularly relevant in consanguineous families and populations carrying the Omani founder allele. NCIT:C15240 (Genetic Counseling).

**Treatment outcomes:** No systematic response-rate or adverse-event data exist. The overarching message from the most recent pooled review (Hoytema van Konijnenburg et al. 2025) is that current therapies (chiefly amino acid supplementation and organ-directed supportive/transplant care) have **not eliminated the most severe phenotypes**, and international collaboration/longitudinal natural-history data are explicitly called for to refine genotype–phenotype correlation and develop better treatments.

**Experimental treatments in clinical trials:** No disease-specific registered clinical trial (ClinicalTrials.gov) for *FARSB*/RILDBC1 was identified in this search.

---

## 13. Prevention

- **Primary prevention**: Not applicable in the traditional sense (no modifiable environmental cause); the only actionable primary-prevention lever is **genetic counseling and reproductive planning** in known carrier couples or high-risk (consanguineous, founder-allele) populations, including consideration of preimplantation genetic diagnosis or prenatal diagnosis where a familial variant is known.
- **Secondary prevention**: Early clinical recognition (growth failure + ILD + brain calcification triad) followed by prompt genetic testing could, in principle, expedite supportive management, though no formal early-detection/screening program exists.
- **Tertiary prevention**: Organ-directed supportive care (nutritional support, pulmonary care, monitoring for and managing hepatic and vascular complications) aims to reduce complication burden and prolong function, though it is not curative.
- **Immunization**: No disease-specific immunization strategy; standard-of-care vaccination (including against respiratory pathogens, e.g., RSV prophylaxis where age-appropriate, influenza, pneumococcal vaccination) would be a reasonable general supportive measure for a child with chronic ILD, though this is inferred general pediatric-ILD practice rather than a documented RILDBC1-specific recommendation.
- **Screening/genetic counseling**: Carrier screening is feasible in principle for populations with a known founder allele (e.g., Omani p.Glu285Lys) but was not documented as an established program in the sources reviewed. Cascade testing of at-risk relatives following an index diagnosis is the standard approach for ultra-rare autosomal recessive disorders.
- **Public health/environmental interventions**: Not applicable — no environmental risk factor to mitigate.
- **Prophylaxis**: None specific; amino acid supplementation (see §12) has been framed in the broader FARS1-disorder literature as potentially disease-modifying rather than strictly prophylactic, and is not curative.

---

## 14. Other Species / Natural Disease

No naturally occurring veterinary or wildlife disease attributable to *FARSB* loss-of-function was identified in this search (no OMIA entries or veterinary case reports were found). *FARSB* orthologs exist across mammals (mouse, and others) and more distantly across vertebrates, consistent with the gene's essential, highly conserved role in cytoplasmic translation, but no spontaneous animal disease model analogous to RILDBC1 has been reported in the literature reviewed. Given that complete loss of an essential translation-machinery gene would be expected to be embryonic lethal in most vertebrate models (see §15), it is plausible that no viable naturally occurring null animal phenotype exists — this is an inference, not a documented finding.

- **Taxonomy**: Human disease-relevant ortholog searches identified only the human *FARSB* gene page and general cross-species conservation notes (GeneCards); NCBI Taxon-level comparative data specific to disease modeling were not identified.
- **Zoonotic potential**: Not applicable (genetic, non-infectious disease).

---

## 15. Model Organisms

No dedicated, published animal or cellular disease model specifically engineered to recapitulate *FARSB*-related RILDBC1 was identified in this search (no zebrafish, mouse conditional-knockout, or patient-iPSC-derived organoid model of *FARSB* loss-of-function was found in the literature reviewed).

- **Patient-derived fibroblasts**: The principal "model system" used to date is **patient-derived dermal fibroblasts**, in which Western blot demonstrated the ~97%/66% reduction in FARSB/FARSA protein (Antonellis et al. 2018) — this is an *in vitro*, patient-cell-based functional confirmation rather than an engineered model organism, and is the strongest direct functional evidence available for the loss-of-function mechanism.
- **Related-gene models (context, not RILDBC1-specific)**: A **zebrafish morpholino knockdown model of *fars2*** (the distinct, mitochondrial paralog) has been used to study developmental angiogenesis requirements for mitochondrial phenylalanyl-tRNA synthetase (PMID:[34540921](https://pubmed.ncbi.nlm.nih.gov/34540921/), *Front Cardiovasc Med* 2021) — this is informative for the general biology of Phe-tRNA synthetases in vascular development (relevant context given the cerebral-aneurysm phenotype seen in some *FARSB* patients) but is **not** a direct model of the cytoplasmic *FARSB* gene or of RILDBC1, and should not be conflated with it during curation.
- **Essential-gene consideration**: Because *FARSB* encodes a core, ubiquitously required subunit of the cytoplasmic protein-synthesis machinery, a complete germline knockout would be expected on general principle to be embryonic lethal in mouse or other standard model systems (as is typical for aminoacyl-tRNA synthetase genes generally) — no MGI record of a *Farsb* knockout mouse phenotype was retrieved in this search, and this point should be verified directly against IMPC/MGI (`https://www.informatics.jax.org`, MGI:1346035) before being asserted as an established finding in a curated entry.
- **Research applications / resources**: Given the absence of an established animal model, functional studies of *FARSB* variants to date rely on (a) patient fibroblasts for protein-level/functional assays and (b) presumably (though not directly confirmed in this search) in vitro aminoacylation assays with recombinant/purified FARS1 complex — both are reasonable candidate approaches for future model-development work, representing a clear **research gap**: no organism-level model exists to study the tissue-specific (lung/brain/liver/vascular) pathophysiology of *FARSB* loss-of-function in vivo.

---

## Summary of Key Evidence Gaps (for curation awareness)

1. **No large cohort/registry** — all data derive from fewer than ~20 published patients across 4–5 kindreds/case series; percentage-based phenotype frequencies should not be over-stated.
2. **No animal or iPSC/organoid model** of *FARSB* loss-of-function has been published; mechanistic claims about non-canonical FARS1 function in lung/vascular tissue rest on human genetic/histologic correlation (Xu et al. 2018) rather than direct experimental perturbation in a model system.
3. **No controlled treatment trial**; amino acid supplementation evidence is retrospective/observational and pooled across the *FARSA*+*FARSB* spectrum, not RILDBC1-specific.
4. **HPO term IDs given above are best-effort suggestions** and should be verified against a live HPO/OAK lookup before being bound in a curated entry, consistent with this knowledge base's anti-hallucination term-validation policy.
5. This session's `WebFetch` tool was unavailable (proxy connection refused) for the full duration of research, so **OMIM, Orphanet, and PubMed full-text/abstract pages could not be directly fetched and parsed**; all information above was synthesized from WebSearch result snippets, which sometimes provide only excerpted or aggregated text rather than verbatim primary-source quotations. Direct fetches of OMIM #613658, OMIM *609690, Orphanet ORPHA:178506, and the primary PMIDs cited (19161147, 29573043, 29979980, 30014610) are recommended as a follow-up verification step before finalizing any curated entry, to obtain exact verbatim abstract quotations for evidence `snippet:` fields.

---

## Sources

- [Entry - #613658 - RAJAB INTERSTITIAL LUNG DISEASE WITH BRAIN CALCIFICATIONS 1; RILDBC1 - OMIM](https://omim.org/entry/613658)
- [Entry - #619013 - RAJAB INTERSTITIAL LUNG DISEASE WITH BRAIN CALCIFICATIONS 2; RILDBC2 - OMIM](https://www.omim.org/entry/619013)
- [Entry - *609690 - PHENYLALANINE-tRNA SYNTHETASE, BETA SUBUNIT; FARSB - OMIM](https://omim.org/entry/609690)
- [Orphanet: Interstitial lung disease-brain calcification syndrome (ORPHA:178506)](https://www.orpha.net/en/disease/detail/178506)
- [Rajab interstitial lung disease with brain calcifications 1 - NORD](https://rarediseases.org/mondo-disease/rajab-interstitial-lung-disease-with-brain-calcifications-1/)
- [MedGen C3150910](https://www.ncbi.nlm.nih.gov/medgen/462260) / [MedGen C5436603 (RILDBC2)](https://www.ncbi.nlm.nih.gov/medgen/1770895)
- [Recessive developmental delay, small stature, microcephaly and brain calcifications with locus on chromosome 2 — Rajab et al. 2009, PMID:19161147](https://pubmed.ncbi.nlm.nih.gov/19161147/) / [PMC2800951](https://pmc.ncbi.nlm.nih.gov/articles/PMC2800951/)
- [Homozygosity for FARSB mutation leads to Phe-tRNA synthetase-related disease of growth restriction, brain calcification, and interstitial lung disease — Zadjali et al. 2018, PMID:30014610](https://pubmed.ncbi.nlm.nih.gov/30014610/)
- [Compound heterozygosity for loss-of-function FARSB variants in a patient with classic features of recessive aminoacyl-tRNA synthetase-related disease — Antonellis et al. 2018, PMID:29573043](https://pubmed.ncbi.nlm.nih.gov/29573043/)
- [Bi-allelic Mutations in Phe-tRNA Synthetase Associated with a Multi-system Pulmonary Disease Support Non-translational Function — Xu et al. 2018, PMID:29979980, PMC6035289](https://pmc.ncbi.nlm.nih.gov/articles/PMC6035289/)
- [FARS1-related disorders caused by bi-allelic mutations in cytosolic phenylalanyl-tRNA synthetase genes: Look beyond the lungs! — Schuch et al. 2021, Clin Genet](https://www.researchgate.net/publication/349463869_FARS1-related_disorders_caused_by_bi-allelic_mutations_in_cytosolic_phenylalanyl-tRNA_synthetase_genes_Look_beyond_the_lungs)
- [Neurodegenerative disorder and diffuse brain calcifications due to FARSB mutation in two siblings — Karimzadeh et al. 2022, PMC9347330](https://pmc.ncbi.nlm.nih.gov/articles/PMC9347330/)
- [Setting the Stage for Treatment of Aminoacyl-tRNA Synthetase (ARS)1-Deficiencies — Hoytema van Konijnenburg et al. 2025, J Inherit Metab Dis](https://onlinelibrary.wiley.com/doi/10.1002/jimd.70017)
- [FARSB Gene - GeneCards](https://www.genecards.org/cgi-bin/carddisp.pl?gene=FARSB)
- [NM_005687.5(FARSB):c.1618+17G>A AND Rajab interstitial lung disease with brain calcifications 1 - ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/RCV002494045/)
- [Developmental Angiogenesis Requires the Mitochondrial Phenylalanyl-tRNA Synthetase (FARS2 zebrafish model, context only) — PMID:34540921](https://pubmed.ncbi.nlm.nih.gov/34540921/)
- [First US Toddler Diagnosed With Rare Lung Disease - Respiratory Therapy, 2026](https://respiratory-therapy.com/disorders-diseases/chronic-pulmonary-disorders/chronic-diseases/first-us-toddler-diagnosed-with-rare-lung-disease/)
- [Pike County toddler is first U.S. child diagnosed with rare lung disease - 14 News, July 2026](https://www.14news.com/2026/07/13/pike-county-toddler-is-first-us-child-diagnosed-with-rare-lung-disease/)
- [FARS2 Deficiency - GeneReviews - NCBI Bookshelf NBK538658](https://www.ncbi.nlm.nih.gov/books/NBK538658/) (differential-diagnosis context)