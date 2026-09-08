---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-26T12:56:18.543852'
end_time: '2026-08-26T13:00:28.367751'
duration_seconds: 249.82
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Autosomal Recessive Nonsyndromic Hearing Loss 104
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
  web_search_requests: 12
  num_turns: 19
  total_cost_usd: 1.2291798000000003
  session_id: 00937d02-a143-56ac-a731-3747f9ee4c64
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 10
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Recessive Nonsyndromic Hearing Loss 104
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Recessive Nonsyndromic Hearing Loss 104** covering all of the
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

# Autosomal Recessive Nonsyndromic Hearing Loss 104 (DFNB104) — Comprehensive Research Report

## 1. Disease Information

**Overview:** Autosomal Recessive Nonsyndromic Hearing Loss 104 (DFNB104), also designated Deafness, Autosomal Recessive 104, is a form of prelingual, congenital, profound sensorineural hearing loss caused by biallelic (homozygous or compound heterozygous) loss-of-function variants in **RIPOR2** (formerly known as **FAM65B**), located on chromosome 6p22.3. The disorder was first mapped and the causal gene identified in 2014 by Diaz-Horta and colleagues in a large consanguineous Turkish kindred ([Diaz-Horta et al. 2014, PNAS, PMID 24958875](https://pmc.ncbi.nlm.nih.gov/articles/PMC4103326)). RIPOR2 encodes a plasma-membrane-associated actin-cytoskeletal regulatory protein that localizes to the base of the stereocilia in cochlear (and vestibular) hair cells and is required for normal stereocilia bundle structure and maintenance.

**Key Identifiers:**
- **OMIM:** #616515 (DFNB104); gene entry *611410 (RIPOR2) ([OMIM 616515](https://omim.org/entry/616515); [OMIM 611410](https://omim.org/entry/611410))
- **MONDO:** MONDO:0014675
- **MedGen (NCBI):** C4225298 — "Autosomal recessive nonsyndromic hearing loss 104" ([MedGen](https://www.ncbi.nlm.nih.gov/medgen/C4225298))
- **HGNC:** HGNC:13872 (RIPOR2; formerly FAM65B)
- **Gene locus:** 6p22.3
- **Orphanet:** Grouped under the generic "Autosomal recessive non-syndromic sensorineural deafness type DFNB" umbrella entries; a DFNB104-specific ORPHA code was not independently confirmed in primary Orphanet sources during this research and should be verified directly against Orphadata before citation.
- **ICD-10:** H90.3 (Sensorineural hearing loss, bilateral) — generic code; no disease-specific ICD-10/11 code exists for DFNB104.

**Synonyms/Alternative Names:**
- DFNB104
- Deafness, Autosomal Recessive 104
- FAM65B-related deafness
- RIPOR2-related nonsyndromic hearing loss (recessive form; distinct from the dominant RIPOR2-related DFNA21)

**Data source note:** All published information derives from aggregated disease-level resources — pedigree/cosegregation studies in a small number of consanguineous families (Turkish, Tunisian) — plus complementary murine and zebrafish model data, rather than large EHR-derived cohorts. This is consistent with an ultra-rare monogenic recessive deafness gene.

**Important nomenclature distinction:** RIPOR2 causes **two clinically and genetically distinct hearing-loss entities**:
- **DFNB104** — biallelic (recessive) loss-of-function variants → congenital, profound, non-progressive hearing loss (this report's focus).
- **DFNA21** — heterozygous, dominant-negative in-frame deletion (c.1696_1707del) → adult-onset, progressive hearing loss, described as a frequent Dutch founder variant ([Oonk et al. 2020, PMID 32631815](https://pubmed.ncbi.nlm.nih.gov/32631815/)).

---

## 2. Etiology

**Disease Causal Factors:** DFNB104 is purely genetic/monogenic — caused by biallelic loss-of-function (null or severely hypomorphic) variants in RIPOR2. No environmental, infectious, or multifactorial contribution has been reported.

**Genetic Risk Factors:**
- **Causal variants identified to date (small number of families):**
  - c.102-1G>A (splice acceptor, intron 2) — homozygous in the original consanguineous Turkish family, causing in-frame skipping of exon 3 and deletion of residues 34–86 (p.R34_D86delinsS) within the core PX membrane-localization domain ([Diaz-Horta et al. 2014, PMID 24958875](https://pmc.ncbi.nlm.nih.gov/articles/PMC4103326)).
  - c.189-1G>A (splice acceptor variant) — reported in ClinVar as pathogenic for DFNB104 ([ClinVar RCV000190353](https://www.ncbi.nlm.nih.gov/clinvar/RCV000190353/)).
  - c.1561C>T (p.Arg521*) — homozygous nonsense variant identified in three Tunisian siblings with congenital profound hearing loss **and** vestibular areflexia, the third reported RIPOR2 pathogenic allele and the first with a documented vestibular phenotype ([Morel et al. 2023, Clinical Genetics, DOI 10.1111/cge.14436](https://onlinelibrary.wiley.com/doi/10.1111/cge.14436)).
- Consanguinity is a strong risk factor for exposing biallelic RIPOR2 variants, consistent with the Turkish and Tunisian consanguineous pedigrees in which the condition has been reported.
- The mutation was absent from dbSNP, the Exome Variant Server, and 330 Turkish population controls in the original report, consistent with a rare, family-restricted (non-founder) allele in that population — in contrast to the common Dutch dominant founder deletion causing DFNA21.

**Environmental Risk Factors:** None identified; this is a purely Mendelian condition with no reported environmental modifiers of penetrance.

**Protective Factors:** None reported specific to RIPOR2/DFNB104. Speculative genetic compensation by paralogs RIPOR1 and RIPOR3 (~70% sequence similarity) has been proposed as a possible explanation for milder or absent vestibular phenotypes in some model systems, but this has not been demonstrated as a true protective mechanism in humans ([Morel et al. 2023](https://onlinelibrary.wiley.com/doi/10.1111/cge.14436)).

**Gene-Environment Interactions:** None documented; no CTD or GxE database entries were identified linking RIPOR2 to environmental modifiers.

---

## 3. Phenotypes

### Auditory phenotype (core feature)
- **Type:** Clinical sign / sensory (audiometric) abnormality.
- **Onset:** Congenital / prelingual — hearing loss is present from birth.
- **Severity:** Profound, and in the founding Turkish family, **symmetric** across affected individuals.
- **Progression:** Notably **non-progressive** — "available audiograms did not suggest progression of the hearing loss" in the original family, distinguishing DFNB104 from many other DFNB forms and from the dominant DFNA21 (which is progressive).
- **Frequency:** All 6 affected individuals in the index Turkish kindred; all 3 affected siblings in the Tunisian kindred — i.e., fully penetrant in reported biallelic carriers.
- Suggested HPO terms:
  - **HP:0001739** Sensorineural hearing impairment
  - **HP:0008625** Bilateral sensorineural hearing impairment
  - **HP:0000456** Prelingual sensorineural hearing impairment (or the more general HP:0008527 congenital sensorineural hearing impairment)
  - **HP:0001737** Profound sensorineural hearing impairment (if distinguishing profound severity)

### Audiological test findings
- Absent otoacoustic emissions (OAEs) — HP:0025400 or descriptor "absent OAEs" (no dedicated HPO term; document as laboratory abnormality).
- Absent/abnormal acoustic reflexes.
- Absent/abnormal auditory brainstem responses (ABR).

### Vestibular phenotype (variant-dependent, not uniform)
- The original Turkish family: **normal vestibular function** — negative Romberg test, normal tandem gait, no balance complaints ("None had balance problems").
- The Tunisian family (p.Arg521* nonsense variant): **vestibular areflexia**, delayed independent walking (21–24 months), abnormal cervical VEMPs, and abnormal video head-impulse testing showing negative gains and covert saccades on posterior and lateral semicircular canals ([Morel et al. 2023](https://onlinelibrary.wiley.com/doi/10.1111/cge.14436)).
- This indicates **variable expressivity/phenotypic heterogeneity** across RIPOR2 alleles — possibly allele-specific (nonsense/truncating vs. splice-site) or genetic-background-dependent.
- Suggested HPO terms:
  - **HP:0000763** or **HP:0002321** Vertigo / Vestibular dysfunction
  - **HP:0002321** Vestibular areflexia (if a specific term is used) — verify exact HPO ID at curation time
  - **HP:0001270** Motor delay (for delayed walking, if attributable)

### Quality of life impact
No dedicated EQ-5D/SF-36/disease-specific QOL studies were identified for DFNB104 specifically. As with other forms of congenital profound sensorineural deafness, the expected impact includes impaired spoken-language acquisition without early intervention (hearing aids/cochlear implantation), and — in the vestibular-areflexia subset — additional impact on gross motor development and balance-dependent activities (data extrapolated from general profound-deafness and vestibular-areflexia literature; no RIPOR2-specific QOL instrument data located).

---

## 4. Genetic/Molecular Information

**Causal Gene:** RIPOR2 (RHO Family Interacting Cell Polarization Regulator 2), formerly FAM65B.
- **HGNC:** HGNC:13872
- **OMIM gene:** *611410
- **Locus:** 6p22.3
- **Ensembl:** ENSG00000111913

**Pathogenic Variants (recessive, DFNB104):**
| Variant | Effect | Family/Population | Source |
|---|---|---|---|
| c.102-1G>A | Splice acceptor → exon 3 skipping, in-frame deletion of aa 34-86 (p.R34_D86delinsS), disrupting the PX membrane-localization domain | Consanguineous Turkish family (6 affected) | PMID 24958875 |
| c.189-1G>A | Splice acceptor variant, pathogenic | ClinVar-reported | ClinVar RCV000190353 |
| c.1561C>T (p.Arg521*) | Nonsense/premature stop, exon 14 | Consanguineous Tunisian family (3 affected siblings) | Morel et al. 2023, Clin Genet |

- **Variant classification (ACMG/AMP):** All reported variants classified pathogenic per cosegregation with disease, absence from population databases/controls, and functional evidence of protein mislocalization (for the splice variant).
- **Variant type/class:** Splice-site (2 variants) and nonsense (1 variant) — all predicted/demonstrated loss-of-function, consistent with a haploinsufficiency-independent, biallelic-null recessive mechanism (contrasting with the dominant-negative in-frame deletion causing DFNA21).
- **Allele frequency:** The recessive DFNB104 alleles are private/family-restricted and were absent from gnomAD/ExAC/dbSNP-scale population databases at the time of reporting — consistent with ultra-rare recessive alleles rather than founder variants (unlike the DFNA21 c.1696_1707del founder deletion, common in the Dutch population).
- **Somatic vs. germline:** Germline only; no somatic RIPOR2 hearing-loss association reported.
- **Functional consequence:** Loss of function — the mutant protein (from the splice variant) accumulates in cytoplasmic inclusion bodies and fails to reach the plasma membrane, in contrast to wild-type RIPOR2/FAM65B, which targets the stereocilia plasma membrane ([PMID 24958875](https://pmc.ncbi.nlm.nih.gov/articles/PMC4103326)).
- **ClinGen Gene-Disease Validity:** RIPOR2 has an **Expert Panel "Definitive"/"Strong"-tier classification** for autosomal recessive nonsyndromic deafness 104 (reported as ClinGen "Expert Review Green" via PanelApp aggregation).
- **Modifier genes:** RIPOR1 and RIPOR3 (paralogs, ~70% sequence similarity to RIPOR2) have been proposed as potential functional compensators explaining phenotypic variability (e.g., absence of vestibular phenotype in some carriers/models), though this is hypothesis-generating rather than directly demonstrated in humans.
- **Epigenetic information:** None reported specific to RIPOR2/DFNB104.
- **Chromosomal abnormalities:** None reported; DFNB104 is caused by sequence-level variants, not large structural/chromosomal rearrangements.

**Protein structure/function:**
- RIPOR2/FAM65B contains a PX(-like)-BAR module region implicated in membrane targeting and curvature sensing (though a later PNAS letter disputed strict PX-BAR domain classification — [PMID for "Little evidence that FAM65B belongs to the family of PX and BAR domain-containing proteins," PNAS 2014](https://pnas.org/content/111/39/E4064) — a caveat worth noting for structural claims).
- RIPOR2 is an atypical inhibitor of the small GTPase **RhoA**, implicated (in non-auditory contexts) in myoblast fusion and leukocyte polarization/migration.
- In hair cells, RIPOR2 forms **circumferential ring-like oligomeric structures** (~229 ± 7 nm diameter) at the basal taper of stereocilia, distinct from taperin's intra-stereociliary core localization; **RhoC** (not RhoA) co-localizes with and regulates RIPOR2 oligomerization in this compartment ([Krey et al. 2016, eLife, PMID for "Murine Fam65b forms ring-like structures..."](https://elifesciences.org/articles/14222)).
- RIPOR2 interacts with **MYH9** (a known deafness gene, DFNA17); loss of Ripor2 in mice is associated with reduced MYH9 protein abundance (despite increased transcript) and aberrant kinocilium localization during hair-bundle morphogenesis ([Xiong et al. 2018, J Mol Med, PMID 30280293](https://pmc.ncbi.nlm.nih.gov/articles/PMC6238639)).

**Suggested ontology terms:**
- **Gene:** hgnc:13872 (RIPOR2)
- **GO Molecular Function:** GO:0005096 (GTPase activator activity) — for RhoA/RhoC-modulating activity; verify precise GO term at curation
- **GO Cellular Component:** GO:0032420 (stereocilium), GO:0060091 (kinocilium)
- **GO Biological Process:** GO:0032420-related stereocilium organization; GO:0060088 auditory receptor cell stereocilium organization

---

## 5. Environmental Information

No environmental factors, lifestyle factors, or infectious agents have been implicated in DFNB104 causation — it is a fully penetrant monogenic recessive disorder. No CTD, TOXNET, or epidemiological database entries link RIPOR2/DFNB104 to environmental exposures.

---

## 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream):**

1. **Molecular trigger:** Biallelic loss-of-function RIPOR2 variants (splice-site or nonsense) → absent or non-functional RIPOR2 protein, or protein that fails to reach its normal subcellular destination (mutant protein retained in cytoplasmic inclusion bodies rather than trafficking to the plasma membrane) — PMID 24958875.
2. **Subcellular/structural consequence:** Loss of the RIPOR2 circumferential ring structure at the base of stereocilia (normally regulated by RhoC-dependent oligomerization) — PMID for Krey et al. 2016 eLife.
3. **Cytoskeletal/interactome consequence:** Disrupted interaction with MYH9 (myosin heavy chain 9), reduced MYH9 protein levels in the cochlea, and mislocalization of the kinocilium during hair-bundle morphogenesis — PMID 30280293.
4. **Cellular/organelle consequence:** Abnormal stereociliary bundle structure and orientation; in mouse models, this manifests as disorganized, misoriented hair bundles from early development (structural/developmental defect) rather than a purely late, degenerative process — PMID 30280293; complementary evidence from the paralogous EPS8L2/DFNB106 pathway shows a distinct maintenance-phase mechanism (see note below).
5. **Functional consequence:** Impaired mechanotransduction — reduced mechanotransduction currents in RIPOR2-deficient hair cells, with re-expression rescue demonstrated experimentally (eLife 2016), directly linking RIPOR2 loss to sensory transduction failure rather than only structural malformation.
6. **Clinical manifestation:** Congenital, profound, non-progressive sensorineural hearing loss (± vestibular areflexia in some allelic variants).

**Note on module conformance (dismech context):** This causal chain — stereociliary actin-cytoskeleton disruption → hair-bundle structural/mechanotransduction failure → profound congenital deafness — is mechanistically analogous to, but molecularly distinct from, the EPS8/EPS8L2 (DFNB102/DFNB106) pathway, which involves stereocilia **elongation and maintenance** via direct actin-bundling rather than RhoA/RhoC-regulated membrane-ring formation. If a "stereocilia structure/maintenance" mechanism module exists in dismech, DFNB104 nodes should specify the RIPOR2/RhoC/MYH9 axis distinctly from the EPS8/EPS8L2/actin-elongation axis.

**Cellular processes involved:**
- Actin cytoskeleton organization/regulation (via Rho-family GTPase signaling)
- Stereocilia bundle morphogenesis and maintenance
- Mechanotransduction (sensory transduction in hair cells)
- Possibly cell polarity establishment (kinocilium positioning)

**Protein dysfunction:** Loss of function via (a) failed membrane trafficking/localization (splice variant) or (b) truncation/nonsense-mediated decay (nonsense variant) — net effect is absence of functional RIPOR2 at the stereociliary base.

**Biochemical abnormalities:** Reduced MYH9 protein abundance despite normal/increased Myh9 transcript levels in Ripor2-null mouse cochlea — a post-transcriptional/protein-stability defect downstream of RIPOR2 loss.

**Molecular profiling:** No transcriptomic, proteomic, metabolomic, or single-cell/spatial datasets specific to human DFNB104 tissue were identified (expected, given the rarity of the condition and inaccessibility of human inner-ear tissue); mechanistic molecular data derive from mouse and zebrafish models.

**Suggested GO terms:**
- GO:0060088 — auditory receptor cell stereocilium organization
- GO:0035090 — maintenance of apical/basal cell polarity (if applicable to kinocilium positioning)
- GO:0007266 — Rho protein signal transduction

**Suggested CL terms:**
- CL:0000601 — inner hair cell
- CL:0000602 — outer hair cell
- CL:0000855 — sensory hair cell (general, if subtype not specified)

---

## 7. Anatomical Structures Affected

**Organ level:**
- Primary organ: **inner ear (cochlea)** — auditory portion.
- Secondary/variant-dependent involvement: **vestibular labyrinth** (semicircular canals, otolith organs) — affected in the Tunisian p.Arg521* family but not the original Turkish splice-variant family, indicating allele-dependent penetrance of the vestibular phenotype.
- Body system: sensory/auditory-vestibular system (cranial nerve VIII pathway secondarily, via sensory input loss, not primary neuronal pathology).

**Tissue and cell level:**
- Sensory epithelium of the organ of Corti (cochlea) — inner and outer hair cells (CL:0000601, CL:0000602).
- Vestibular sensory epithelium (cristae ampullares, maculae) in variant-affected individuals.

**Subcellular level:**
- **Stereocilia** — specifically the basal taper/base region where RIPOR2 forms its ring-like oligomeric structure (distinct from the stereocilia tips, where EPS8/EPS8L2 act).
- Plasma membrane (site of normal RIPOR2 localization; site of failed trafficking for the mutant splice-variant protein).
- Cytoplasmic inclusion bodies (site of pathological mutant-protein accumulation).
- Kinocilium (secondarily mislocalized in Ripor2-deficient mice).

**Localization:**
- Bilateral, symmetric involvement of both ears (consistent across all reported human cases).
- No lateralization/asymmetry reported.

**Suggested UBERON terms:**
- UBERON:0001846 — cochlea
- UBERON:0002106 — spiral organ (organ of Corti)
- UBERON:0002418 — stereocilium bundle / UBERON:0009866 stereocilium (verify precise term)
- UBERON:0001838 — vestibular apparatus (for the variant-associated phenotype)

**Suggested GO Cellular Component terms:**
- GO:0032420 — stereocilium
- GO:0005886 — plasma membrane

---

## 8. Temporal Development

**Onset:** Congenital/prelingual — hearing loss is present from birth or the earliest testable age (universal newborn hearing screening range), consistent with a developmental/structural stereociliary defect rather than a late degenerative process.

**Onset pattern:** Not acute or insidious in the usual sense — it is a static congenital deficit.

**Progression:**
- **Auditory phenotype:** Non-progressive in the original (splice-variant) family — audiograms performed at multiple ages did not show worsening. This is a notable point of contrast with the RIPOR2-associated **dominant** DFNA21, which is explicitly progressive with average onset age 30.6 years (range 0–70 years) in the Dutch founder-variant cohort (PMID 32631815).
- **Vestibular phenotype (where present):** Static congenital areflexia with developmental consequence (delayed independent walking at 21–24 months in the Tunisian siblings) rather than progressive vestibular decline.

**Disease course pattern:** Stable, chronic, lifelong sensorineural hearing loss.

**Disease stages:** Not formally staged (unlike some progressive conditions); severity is described simply as profound at diagnosis and remains profound.

**Remission patterns:** None — this is a structural/developmental sensory deficit with no spontaneous remission; management is via habilitation (hearing aids, cochlear implantation), not disease-modifying treatment.

**Critical periods:** As with all forms of prelingual profound deafness, early identification (newborn hearing screening) and early intervention (hearing aids/cochlear implant, before ~2–3 years of age) represent the critical window for optimizing spoken-language outcomes — a general principle for congenital SNHL, not RIPOR2-specific data.

---

## 9. Inheritance and Population

**Epidemiology:**
- No population-level prevalence or incidence estimates exist for DFNB104 specifically; it is described only via individual case families (an ultra-rare, "cases in literature" level of epidemiological documentation — likely fewer than 10 families reported worldwide as of 2023–2024: 1 Turkish family with 6 affected, 1 Tunisian family with 3 affected, plus scattered additional ClinVar-reported variants of uncertain full clinical documentation).
- Suggested `prevalence_class`: NOT_YET_DOCUMENTED or CASES_IN_LITERATURE (per dismech's PrevalenceMeasureEnum), given the case-family-level evidence base.

**Inheritance pattern:** Autosomal recessive (biallelic variants required; heterozygous carriers are unaffected for DFNB104, in contrast to the dominant DFNA21 allele in the same gene).

**Penetrance:** Complete in all reported biallelic carriers (100% penetrance for the auditory phenotype across both reported families).

**Expressivity:** Variable — specifically regarding the **vestibular** component (present in the Tunisian p.Arg521* family, absent in the Turkish c.102-1G>A family), suggesting possible allele-specific or genetic-background-dependent expressivity. The auditory phenotype (profound, congenital, non-progressive) appears consistent across families.

**Genetic anticipation:** Not applicable/not reported (not a repeat-expansion disorder).

**Germline mosaicism:** Not reported in the literature reviewed.

**Founder effects:** Not established for the recessive DFNB104 alleles (each reported variant appears private to its family) — this contrasts with the well-characterized Dutch founder deletion causing the dominant DFNA21.

**Consanguinity role:** Central — both reported families (Turkish, Tunisian) are consanguineous, which is the mechanism by which rare private recessive alleles became biallelic and phenotypically manifest.

**Carrier frequency:** Not established in population databases (gnomAD) given the rarity/private nature of reported alleles.

**Population demographics:**
- Reported affected families: Turkish (original discovery family) and Tunisian (second reported vestibular-affected family) — both from populations with documented elevated rates of consanguineous marriage, consistent with ascertainment bias toward populations where recessive conditions are more readily unmasked and studied.
- No broader geographic/ethnic prevalence data available.
- Sex ratio: Autosomal recessive — expected 1:1 male:female; no skew reported (consistent with the 6 and 3 affected individuals reported, though gender breakdown was not the emphasized detail in these papers).

---

## 10. Diagnostics

**Clinical/audiological tests:**
- **Auditory brainstem response (ABR):** absent, consistent with profound SNHL.
- **Otoacoustic emissions (OAE):** absent/negative.
- **Acoustic reflex testing:** absent.
- **Pure-tone audiometry:** profound bilateral symmetric SNHL.
- **Vestibular testing (where indicated):** cervical VEMPs (abnormal in Tunisian family), video head-impulse test (vHIT) — negative gains, covert saccades on posterior/lateral canals in the vestibular-areflexia subgroup.

**Genetic testing:**
- **Recommended approach:** Given DFNB104's genetic and phenotypic overlap with dozens of other DFNB loci (e.g., GJB2, MYO15A, OTOF, and the mechanistically related EPS8/EPS8L2/DFNB102/106), a multi-gene **nonsyndromic hearing loss panel** or exome sequencing (especially in consanguineous families, where autozygosity mapping/homozygosity-region analysis is powerful — as used in both the original Turkish and Tunisian discovery studies) is the standard diagnostic approach rather than single-gene RIPOR2 testing.
- **Whole exome sequencing (WES):** Was the discovery method in both published families (combined with linkage/homozygosity mapping).
- **Gene panels:** RIPOR2 is included in clinical "monogenic hearing loss" gene panels (e.g., Genomics England PanelApp lists RIPOR2 under its Monogenic hearing loss panel).
- **Chromosomal microarray/karyotyping/FISH:** Not applicable — DFNB104 arises from sequence-level (not structural chromosomal) variants.
- **Mitochondrial DNA testing:** Not applicable (nuclear gene).

**Clinical criteria:** No RIPOR2/DFNB104-specific diagnostic criteria exist beyond standard nonsyndromic hearing loss workup; diagnosis is genetically confirmed (biallelic pathogenic RIPOR2 variants in a proband with congenital nonsyndromic profound SNHL, especially with consanguinity or homozygosity by descent).

**Differential diagnosis:**
- Other DFNB loci causing congenital profound nonsyndromic SNHL (GJB2/DFNB1, MYO15A/DFNB3, OTOF/DFNB9, TMC1/DFNB7/11, and many others).
- Usher syndrome (if vestibular areflexia is present in an affected individual — must be distinguished from RP-associated Usher syndrome by absence of retinal/ophthalmologic findings, since the Tunisian RIPOR2 phenotype mimics a Usher-like cochleovestibular presentation without retinitis pigmentosa).
- The mechanistically related but molecularly distinct EPS8-family disorders (DFNB102/EPS8, DFNB106/EPS8L2) — clinically distinguishable by their typically progressive (rather than congenital-stable) course.

**Screening:** Universal newborn hearing screening (standard of care generally, not RIPOR2-specific) would detect the congenital profound hearing loss; cascade genetic testing/carrier screening is relevant in consanguineous families with a known proband variant.

---

## 11. Outcome/Prognosis

**Survival/mortality:** No excess mortality — DFNB104 is an isolated (nonsyndromic) sensory disorder with no reported systemic or life-limiting comorbidity.

**Morbidity/function:**
- Primary morbidity is profound congenital deafness, with attendant impact on spoken-language development if unaddressed by early habilitation.
- In the vestibular-areflexia subset (Tunisian family), additional morbidity includes delayed gross motor/balance milestones (delayed independent walking) and likely lifelong absence of the vestibulo-ocular reflex, which may affect balance in low-visual/proprioceptive-input conditions (e.g., darkness, uneven surfaces) — extrapolated from general vestibular-areflexia literature, not RIPOR2-specific outcome studies.

**Disease course:** Stable — the hearing loss does not progress further once established (a favorable prognostic feature relative to progressive DFNB/DFNA forms), meaning habilitative interventions (hearing aids, cochlear implants) are not expected to need escalation due to further hearing decline.

**Complications:** None specific reported beyond the sensory/developmental consequences above; cochlear implantation is expected to be effective given the absence of documented cochlear structural malformation beyond the stereociliary/hair-cell level (though implant-specific outcome data for RIPOR2/DFNB104 patients specifically were not identified in this search).

**Prognostic factors:** Early cochlear implantation/hearing amplification is the major modifiable prognostic factor for language outcomes, per general principles of congenital profound SNHL management (not RIPOR2-specific trial data).

---

## 12. Treatment

**No RIPOR2/DFNB104-specific gene therapy, pharmacotherapy, or targeted molecular treatment currently exists or is in registered clinical trials** (no ClinicalTrials.gov entries or AAV inner-ear gene-therapy programs targeting RIPOR2 were identified in this search, in contrast to genes like OTOF, which has advanced AAV gene-therapy programs).

**Standard of care (supportive/rehabilitative, non-gene-specific):**
- **Hearing amplification:** Hearing aids for residual hearing (typically limited benefit given profound loss).
  - NCIT term: NCIT:C15302 (Physical Therapy) is not correct; more appropriate would be a hearing-device/audiologic-rehabilitation NCIT term if available, or leave `treatment_term` free-text if no exact NCIT match exists (device-based interventions currently lack a precise NCIT clinical-action term per dismech's own documented gap for "DEVICE" modality).
- **Cochlear implantation:** The mainstay definitive intervention for congenital profound bilateral SNHL.
  - NCIT: no exact single term found in this search; consider NCIT:C15329 (Surgical Procedure) as the treatment_term with device/implant specified in description, or search NCIT specifically for "Cochlear Implantation" at curation time.
- **Vestibular rehabilitation** (for the vestibular-areflexia subgroup): standard balance/vestibular physical therapy.
  - NCIT:C15302 (Physical Therapy) applicable here.
- **Genetic counseling:** Recommended for consanguineous families with an identified proband, given the autosomal recessive inheritance and elevated recurrence risk (25% per pregnancy for carrier parents).
  - NCIT:C15240 (Genetic Counseling).

**Experimental/preclinical therapeutic direction (mechanistic rationale, not yet RIPOR2-specific):**
- Mouse model rescue experiments have shown that **re-expression of Fam65b/Ripor2 in deficient hair cells can rescue mechanotransduction defects** ([Krey et al. 2016, eLife](https://elifesciences.org/articles/14222)), providing proof-of-concept rationale for a future AAV-mediated gene-replacement approach analogous to those in advanced development for OTOF, TMC1, and other DFNB genes — but no RIPOR2-specific vector or preclinical inner-ear gene-therapy publication was identified as of this search.

**Treatment outcomes:** No RIPOR2-specific treatment-response, adverse-event, or comparative-effectiveness data located.

---

## 13. Prevention

- **Primary prevention:** Not applicable in the traditional sense (monogenic disorder); the only "prevention" avenue is reproductive genetic counseling and reduction of consanguineous-union recurrence risk awareness in affected families.
- **Secondary prevention/early detection:** Universal newborn hearing screening (general standard of care, not RIPOR2-specific) enables early diagnosis and prompt habilitative intervention.
- **Genetic screening:** Carrier screening and prenatal/preimplantation genetic diagnosis (PGD) are options for known-carrier consanguineous families once a familial RIPOR2 variant is identified, per standard ACMG-style recessive-disorder counseling principles.
- **Tertiary prevention:** Early cochlear implantation/amplification to prevent language-developmental complications of unaddressed profound deafness; vestibular rehabilitation to mitigate balance-related complications in the vestibular-areflexia subgroup.
- **Public health/behavioral/immunization/prophylaxis:** Not applicable — no infectious, immunizable, or behavioral risk-modification component to this monogenic disorder.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** No naturally occurring RIPOR2-associated hearing loss has been reported in companion animals or wildlife (no OMIA entry identified in this search) — all non-human data derive from **engineered/induced models** (see Section 15), not spontaneous natural disease.
- **Comparative biology:** The RIPOR2 gene and its role in stereociliary actin regulation appear evolutionarily conserved (functional orthologs studied in mouse and zebrafish), and the RhoC-RIPOR2-MYH9 interaction network appears conserved across these model systems, though the notable **species discrepancy in vestibular phenotype** (human vestibular areflexia in some RIPOR2-null patients vs. normal vestibular function in Ripor2-knockout mice and zebrafish) is a documented cross-species divergence meriting explicit note ([Morel et al. 2023](https://onlinelibrary.wiley.com/doi/10.1111/cge.14436)) — a candidate `HUMAN_MODEL_MISMATCH` discussion for dismech curation.
- **Zoonotic/transmission relevance:** Not applicable (non-infectious monogenic disorder).

---

## 15. Model Organisms

**Mouse models:**
- **Ripor2 (Fam65b) knockout mice:** Complete deafness; hair bundle morphological defects (disorganized/misoriented stereocilia bundles), reduced mechanotransduction currents, aberrant kinocilium localization, and reduced MYH9 protein abundance in the cochlea ([Xiong et al. 2018, J Mol Med, PMID 30280293](https://pmc.ncbi.nlm.nih.gov/articles/PMC6238639); [Krey et al. 2016, eLife](https://elifesciences.org/articles/14222)).
- **Phenotype recapitulation:** High fidelity for the **auditory** phenotype (deafness, hair-bundle/stereocilia structural defects, mechanotransduction failure) — closely mirrors human DFNB104.
- **Model limitation:** **Vestibular phenotype is NOT recapitulated** — Ripor2-knockout mice show normal balance/vestibular function (no circling behavior), unlike the vestibular areflexia documented in at least one human family. This is an explicit, well-documented **human-model mismatch** meriting `HUMAN_MODEL_MISMATCH` classification (per dismech schema conventions) rather than a generic `KNOWLEDGE_GAP`, since the evidence (mouse vestibular testing) exists but its translational validity to the human vestibular phenotype is the open question. Proposed explanations in the primary literature include incomplete/insensitive vestibular testing in mice and genetic compensation by paralogs RIPOR1/RIPOR3.
- **Rescue experiments:** Re-expression of wild-type Fam65b/Ripor2 in deficient hair cells rescues mechanotransduction current defects, demonstrating causality and supporting the eventual therapeutic feasibility of gene replacement (eLife 2016).

**Zebrafish models:**
- **fam65b knockdown (morpholino) zebrafish:** Significant reduction in saccular hair cell numbers and neuromasts, and hearing loss, reported in the original discovery paper ([Diaz-Horta et al. 2014, PMID 24958875](https://pmc.ncbi.nlm.nih.gov/articles/PMC4103326)).
- **fam65b nonsense-mutant zebrafish** (from the Tunisian-family follow-up study): No circling behavior or balance abnormality at 5 days post-fertilization, again showing the auditory-but-not-vestibular phenotype discrepancy relative to at least one human RIPOR2 family ([Morel et al. 2023](https://onlinelibrary.wiley.com/doi/10.1111/cge.14436)).

**Applications:** These models have been used to establish causality (loss-of-function → hearing loss), define the subcellular localization and oligomeric ring structure of RIPOR2 at the stereociliary base, dissect the RhoC-dependent regulatory mechanism, identify the MYH9 interaction, and demonstrate rescue of mechanotransduction by gene re-expression — the last providing direct preclinical proof-of-concept for a future gene-therapy approach.

**Resources:** MGI (Mouse Genome Informatics) for Ripor2 knockout allele records; ZFIN for zebrafish fam65b/ripor2 mutant/morphant lines (specific allele/stock IDs not retrieved in this search — recommend direct MGI/ZFIN query at curation time for exact resource identifiers).

---

## Summary of Key Evidence Citations

| Citation | Key Contribution |
|---|---|
| Diaz-Horta O, et al. PNAS 2014. PMID: [24958875](https://pmc.ncbi.nlm.nih.gov/articles/PMC4103326) | Discovery of FAM65B/RIPOR2 as DFNB104 gene; c.102-1G>A splice variant; Turkish family clinical/audiometric characterization; zebrafish knockdown model |
| Xiong W, et al. J Mol Med 2018. PMID: [30280293](https://pmc.ncbi.nlm.nih.gov/articles/PMC6238639) | Ripor2 mouse knockout: hair-bundle structure/orientation defects; MYH9 interaction |
| Krey JF, et al. eLife 2016. [DOI 10.7554/eLife.14222](https://elifesciences.org/articles/14222) | RIPOR2 ring-like stereociliary base structure; RhoC-dependent oligomerization; mechanotransduction rescue |
| Oonk AMM, et al. 2020. PMID: [32631815](https://pubmed.ncbi.nlm.nih.gov/32631815/) | Dominant RIPOR2 founder deletion causing DFNA21 (adult-onset, progressive) — important nosological contrast to DFNB104 |
| Morel N, et al. Clin Genet 2023. [DOI 10.1111/cge.14436](https://onlinelibrary.wiley.com/doi/10.1111/cge.14436) | Third RIPOR2 variant (p.Arg521*); Tunisian family with vestibular areflexia; explicit human-vs-animal-model vestibular-phenotype discrepancy discussion |
| OMIM #616515 | Clinical synopsis and molecular genetics summary for DFNB104 |
| OMIM *611410 | RIPOR2 gene entry |

**Notable curation caveats for dismech entry construction:**
1. The Orphanet-specific identifier for DFNB104 could not be independently confirmed in this research pass and should be verified directly against Orphadata/ORPHA before citation (avoid citing an unverified ORPHA code).
2. The PX-BAR domain structural classification for RIPOR2/FAM65B has been directly disputed in the literature (PNAS 2014 technical comment) — cite this nuance if describing protein domain structure in detail.
3. The vestibular phenotype is not uniform across reported DFNB104 families — this is a genuine expressivity finding, not an error, and should be modeled as such (e.g., via subtype-level or evidence-item-level distinction between the Turkish and Tunisian families) rather than collapsed into a single uniform phenotype claim.
4. No RIPOR2-specific prevalence, treatment-trial, or QOL data exist beyond the two published case families — this is an ultra-rare, "cases-in-literature" level disorder, and prevalence/epidemiology fields should be populated conservatively (e.g., `CASES_IN_LITERATURE` / `NOT_YET_DOCUMENTED`).