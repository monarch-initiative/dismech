---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-27T04:34:58.228233'
end_time: '2026-08-27T04:38:50.384310'
duration_seconds: 232.16
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: DONSON-Related Microcephalic Primordial Dwarfism
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
  web_search_requests: 23
  num_turns: 30
  total_cost_usd: 1.4415152
  session_id: a1f65bb8-1b49-516c-9197-25fb2b9c84dd
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 22
reference_validation:
  total_references: 15
  verified: 15
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 0
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMC:PMC6936249
  relevance_assessed: 15
  on_topic: 12
  needs_review: true
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** DONSON-Related Microcephalic Primordial Dwarfism
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **DONSON-Related Microcephalic Primordial Dwarfism** covering all of the
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

I have sufficient primary-literature detail now to compile the report.

I now have enough sourced material to compile the full report.

# DONSON-Related Microcephalic Primordial Dwarfism: Comprehensive Research Report

## 1. Disease Information

**Overview.** DONSON-related disorder is a rare, autosomal recessive (with rare de novo cases) microcephalic primordial dwarfism (MPD) caused by biallelic (or, uncommonly, de novo monoallelic) hypomorphic variants in *DONSON* (Downstream Neighbor Of SON), a gene encoding an essential replisome/replication-initiation factor. Because complete loss of DONSON is embryonic lethal, all disease-causing alleles identified to date are partial loss-of-function ("hypomorphic") — no patient carries a biallelic combination of two complete null (nonsense/frameshift) alleles (PMID:28191891). The disorder spans a clinical continuum rather than a single discrete syndrome, ranging from prenatally/perinatally lethal **microcephaly-micromelia syndrome (MIMIS)** at the severe end, through **Meier-Gorlin syndrome (MGS)**-like and **Seckel-syndrome**-like presentations, to the comparatively milder **microcephaly, short stature, and limb abnormalities (MISSLA)** phenotype, plus rare **femoral-facial syndrome (FFS)**-like presentations (PMID:31407851; PMC6528082).

**Key identifiers:**
- **Gene:** *DONSON*, HGNC:2993, chromosome 21q22.11, UniProt Q9NYP3, protein "DNA replication fork stabilization factor DONSON" (566 aa, ~62.7 kDa, 10 coding exons; transcript NM_017613)
- **OMIM gene:** *611428 (DOWNSTREAM NEIGHBOR OF SON; DONSON)
- **OMIM phenotypes:**
  - #617604 — Microcephaly, Short Stature, and Limb Abnormalities (MISSLA)
  - #251230 — Microcephaly-Micromelia Syndrome (MIMIS)
  - Additional overlapping entries for Meier-Gorlin syndrome and Seckel-like presentations attributed to *DONSON*
- **Orphanet:** ORPHA:572768 (Microcephaly-micromelia syndrome); ORPHA:572773 (Microcephaly-short stature-limb abnormalities syndrome); gene page "DONSON — DNA replication fork stabilization factor DONSON" (orpha.net)
- **MONDO:** parent grouping term MONDO:0017950 (microcephalic primordial dwarfism); disease-specific MONDO terms map to the MISSLA/MIMIS/MGS-DONSON entries
- **GARD/NIH:** "DONSON-related microcephaly-short stature-limb abnormalities spectrum" (rarediseases.info.nih.gov/diseases/22314)
- Data is derived from **aggregated case series and pedigrees** (exome/genome sequencing cohorts of families with microcephalic dwarfism), not large EHR-scale registries — the total published patient count across all DONSON-related phenotypes is on the order of 40–50 individuals as of the most recent literature.

**Synonyms:** DONSON deficiency; DONSON-related microcephalic primordial dwarfism; DONSON-related cell cycle-opathy; Meier-Gorlin syndrome 8 / DONSON-related MGS; Seckel-like syndrome (DONSON-related); Microcephaly-Micromelia Syndrome (MIMIS); Microcephaly, Short Stature and Limb Abnormalities (MISSLA); DONSON-related femoral-facial syndrome.

## 2. Etiology

**Causal factor:** Purely genetic/molecular — biallelic hypomorphic pathogenic variants in *DONSON* impairing (but not abolishing) its replisome function. A minority of reported cases are compound heterozygous with one de novo allele (PMC6936249).

**Genetic risk factors:**
- Missense, splice-site, small indel/frameshift, and non-coding (deep intronic, promoter/UTR) variants have all been reported. Critically, **no patient has two complete null alleles** — this genotype is presumed embryonic lethal, consistent with mouse knockout data (see §15) (PMID:28191891).
- A recurrent homozygous missense variant, **c.631C>T p.(Arg211Cys)**, has been independently identified in unrelated families with the Meier-Gorlin phenotype, suggesting either a mutational hotspot or a shared ancestral/founder allele in some populations (PMC6936249; recent Turkish-family case report, PMID:41612845).
- A recurrent **K489T** substitution and a **noncoding variant disrupting exon 4/5 splicing** have also been described as causing exon skipping and nonsense-mediated decay or post-transcriptional destabilization of DONSON protein (PMID:28191891; PMC5538549 — the noncoding "genome-and-transcriptome sequencing" MIMIS discovery).
- **Genotype–phenotype correlation:** variants affecting exon 4 have been associated with the milder MGS/FFS end of the spectrum, whereas frameshift variants and those in exons 5–10 correlate with more severe microcephaly and developmental impairment (PMC6936249).
- Variants are rare in population databases (reported at <0.5% frequency in ExAC in the original description; no specific carrier-frequency or founder-population data were identified in this search beyond the shared p.Arg211Cys recurrence).

**Environmental/other risk factors:** None established; this is a purely monogenic disorder with no known environmental, infectious, or lifestyle contributory factors.

**Protective factors:** None reported.

**Gene-environment interactions:** Not applicable/not reported.

## 3. Phenotypes

The DONSON phenotypic spectrum shares a common "core" triad — profound microcephaly, growth restriction, and skeletal anomalies — of variable severity:

| Phenotype | HPO term (suggested) | Notes |
|---|---|---|
| Severe microcephaly (often congenital/prenatal-onset) | HP:0000252 (Microcephaly) / HP:0011451 (Congenital microcephaly) | Reported mean head circumference −7.5 ± 2.4 SD in the original 29-patient cohort — disproportionately more severe than height deficit (PMID:28191891) |
| Intrauterine growth restriction / short stature | HP:0001511 (IUGR) / HP:0004322 (Short stature) | Height −3.2 ± 1.4 SD in the milder cohort; as severe as −6 SD head circumference vs −3 SD height in MISSLA (OMIM:617604) |
| Reduced cerebral cortical volume / simplified gyration | HP:0002506 (Simplified gyral pattern) / HP:0012340 (Abnormal cerebral cortex morphology) | Reduced gyral folding on imaging |
| Hypoplastic/absent corpus callosum (severe end) | HP:0002079 / HP:0006989 | Reported in MIMIS fetuses (PMC5538549) |
| Craniosynostosis | HP:0001363 | Seen in severe MIMIS cases |
| Triangular facies, micrognathia/microretrognathia, small dysplastic ears | HP:0000325 (Triangular face) / HP:0000347 (Micrognathia) / HP:0008551 (Microtia) | Classic MGS-like facial gestalt |
| Small anterior fontanel, high forehead | HP:0000267 / HP:0000348 | MISSLA-specific dysmorphism |
| Absent/hypoplastic patellae | HP:0003308 (Aplasia/Hypoplasia of the patella) | Core MGS feature |
| Radial ray defects: thumb hypo/aplasia, radial head dislocation, proximally implanted thumbs | HP:0009601 / HP:0009775 | Recurrent skeletal finding across the spectrum |
| Clinodactyly, syndactyly, brachydactyly | HP:0030084 / HP:0001159 / HP:0009824 | |
| Micromelia / limb malformation (severe end, MIMIS) | HP:0002983 | Prenatal-onset, can be lethal |
| Femoral hypoplasia (femoral-facial syndrome variant) | HP:0005630 | First gene association for FFS reported in Kim/Karaca 2019 (PMC6936249) |
| Mild intellectual disability / poor speech acquisition | HP:0001256 / HP:0000750 | Present in milder survivors (MISSLA) |
| Hypopigmented skin lesions | HP:0001010 | Reported as a novel, previously unreported finding in one MGS patient |
| Sparse scalp hair/eyebrows, long eyelashes, thick vermilion of lips | HP:0002286 / HP:0045075 / HP:0012471 | MISSLA facial features |

**Onset:** Prenatal (severe end — detectable IUGR and microcephaly on antenatal ultrasound) through neonatal presentation for milder forms.

**Severity/progression:** Static/non-progressive congenital malformation and growth pattern once established (not a degenerative disease), but growth deficiency and microcephaly are lifelong. Severity is graded along the described spectrum from perinatally lethal MIMIS to milder, non-lethal MISSLA/MGS-like presentations with survival into childhood/adulthood.

**Quality of life:** Limited direct QoL data; morbidity relates to short stature, skeletal deformity, and (in a subset) mild intellectual disability affecting educational/functional outcomes. No specific EQ-5D/SF-36 data identified.

## 4. Genetic / Molecular Information

- **Causal gene:** *DONSON* (HGNC:2993, OMIM *611428), chromosome 21q22.11.
- **Variant classes observed:** missense, nonsense, frameshift, canonical and non-canonical splice-site variants, and at least one deep intronic/regulatory noncoding variant causing aberrant splicing (identified via combined genome+transcriptome sequencing in a MIMIS family; PMC5538549).
- **ACMG classification:** Reported variants are generally classified pathogenic/likely pathogenic in ClinVar (e.g., NM_017613.4:c.1466A>C p.(Lys489Thr); c.82A>C p.(Ser28Arg)) in the context of biallelic inheritance.
- **Functional consequence:** All disease variants are **hypomorphic** (partial loss of function) rather than complete null — consistent with the embryonic lethality of complete DONSON loss. Mechanisms of hypomorphism include: exon skipping leading to partial nonsense-mediated decay, post-transcriptional protein destabilization (e.g., the K489T variant), subcellular mislocalization, and reduced ability to rescue replication defects in functional assays (e.g., R217C severely impairs function while M463T remains largely functional in complementation assays) (PMID:28191891; academic.oup.com/nar/51/18/9748).
- **Inheritance:** Autosomal recessive in the great majority of cases; rare compound heterozygous cases include one de novo allele (e.g., the femoral-facial syndrome patient with de novo c.683G>T p.(Trp228Leu)) (PMC6936249).
- **Modifier genes:** None specifically established.
- **Epigenetics:** No disease-specific epigenetic (DNA methylation/histone) data identified.
- **Chromosomal abnormalities:** Not a copy-number/structural disorder — point mutations and small indels/splice variants predominate; not associated with 21q22 microdeletion/duplication syndromes as a class (though 21q22.11 duplications encompassing *DONSON* have been studied for partial trisomy 21 phenotypes in an unrelated context; PMC5102301).

## 5. Environmental Information

Not applicable — this is a purely monogenic Mendelian disorder. No toxin, lifestyle, or infectious contributory factors have been identified in the literature reviewed.

## 6. Mechanism / Pathophysiology

**Core molecular function of DONSON.** DONSON is a replisome component essential for both (a) origin firing/replication initiation and (b) replication fork stability during elongation:

- **Replication initiation:** DONSON is required for **Cdc45 and GINS chromatin association** with the MCM2-7 helicase and is essential for assembly of the active CMG (Cdc45-MCM-GINS) replicative helicase at replication origins (PMID:37638758; academic.oup.com/nar/51/18/9748). Recent structural work shows DONSON acts as a **dimerization scaffold that synchronizes the delivery of two GINS complexes** to the pre-replication complex, even though GINS itself cannot dimerize (PMC10996697; "structural mechanism of dimeric DONSON in replicative helicase activation," PMC7616792/ScienceDirect S109727652300761X). DONSON interacts with the initiation master-regulator **TopBP1** in a CDK-dependent manner, and together with RecQL4 transiently docks the pre-replication complex before origin firing, without itself traveling with the elongating fork.
- **Fork stability:** During S-phase, DONSON protein levels peak in parallel with Cyclin A and it associates with MCM helicase subunits, the GINS complex, PCNA, Treslin, and RPA to prevent spontaneous replication fork stalling during unperturbed DNA synthesis (PMID:28191891).

**Consequence of DONSON hypomorphism:**
1. Patient-derived and DONSON-depleted cells show elevated spontaneous replication fork asymmetry and stalling.
2. Stalled forks undergo pathological **nucleolytic cleavage by the structure-specific endonucleases MUS81 and XPF**, generating severe replication-associated DNA damage.
3. The ATR-dependent intra-S and G2/M checkpoints are impaired — reduced phosphorylation of CHK1 and NBS1 — so cells fail to properly arrest and repair in response to this damage ("Loss of DONSON leads to severe replication-associated DNA damage arising from nucleolytic cleavage of stalled replication forks," PMID:28191891).
4. Separately, DONSON depletion causes **premature centriole disengagement** during interphase, generating supernumerary centrosomes that drive abnormal mitotic spindle formation and chromosome segregation errors — a distinct centrosome-cycle mechanism proposed to compound the replication-stress phenotype (bioRxiv 2020.05.10.086777; later peer-reviewed).

**Cell-type and tissue vulnerability — causal chain to microcephaly:** Neural progenitor cells are exquisitely sensitive to replication stress because of their extremely high proliferative demand during cortical neurogenesis. Conditional mouse knockout studies (necessary because germline *Donson* loss is embryonic lethal) show that:
- Cre-mediated *Donson* deletion in progenitors of both cortical glutamatergic (dorsal telencephalon/neocortex, hippocampus) and GABAergic (subpallial, Nkx2.1+ lineage) neurons causes extensive apoptosis in both the proliferative zones and postmitotic differentiation zones.
- Nkx2.1-Cre-mediated deletion ablated ~75% of Nkx2.1-derived cortical GABAergic interneurons, and progenitors generating cortical interneurons and oligodendrocyte precursors were also affected (PLOS Genetics, PMC8011756/PMID via journals.plos.org/plosgenetics/10.1371/journal.pgen.1009441).
- This establishes microcephaly in DONSON disease as a **progenitor-depletion mechanism**: replication-stress-induced apoptosis in rapidly dividing neuroepithelial and interneuron progenitor pools, rather than a primary neuronal degeneration process.

**Suggested GO terms:** GO:0006260 (DNA replication), GO:0031297 (replication fork processing), GO:0000076 (DNA replication checkpoint signaling), GO:0007099 (centriole replication), GO:0000086 (G2/M transition of mitotic cell cycle).
**Suggested CL terms:** CL:0000047 (neural stem cell) / CL:0002605 (neural progenitor cell), CL:0000617 (GABAergic neuron), CL:0000679 (glutamatergic neuron).

## 7. Anatomical Structures Affected

- **Organ/system level:** Central nervous system (brain — cerebral cortex, corpus callosum), skeletal system (limbs — radial ray, patella, digits; craniofacial skeleton — skull sutures, mandible, ears), growth/endocrine axis (generalized somatic growth failure). No primary cardiac, renal, or hepatic involvement is characteristic of the core phenotype (distinguishing it from some other MPDs).
- **Tissue/cell level:** Neuroepithelial progenitors and cortical interneuron progenitors (proliferation and differentiation zones); chondro-osseous tissue of the growth plate and appendicular skeleton.
- **Subcellular level:** DNA replication fork/replisome (nuclear, chromatin-associated), centrosome/centriole.
- **UBERON suggestions:** UBERON:0000955 (brain), UBERON:0000956 (cerebral cortex), UBERON:0002331 (corpus callosum), UBERON:0002102 (forelimb/radius), UBERON:0002337 (patella).
- **Laterality:** Generally bilateral/symmetric (microcephaly, growth restriction); limb involvement can be asymmetric in some case reports.

## 8. Temporal Development

- **Onset:** Prenatal in the severe end of the spectrum (detectable IUGR, microcephaly, and limb anomalies on antenatal ultrasound in MIMIS); congenital/neonatal in milder MISSLA/MGS-like presentations.
- **Course:** A static congenital malformation/growth syndrome rather than a progressive neurodegenerative disease — microcephaly and short stature are present from birth and persist, without a described post-natal regression phase.
- **Severity spectrum (disease "stages" in effect):** MIMIS (prenatal/perinatal lethal) → Seckel-like/severe microcephaly with developmental delay → MGS-like (short stature, ear/patella anomalies) → FFS-like → MISSLA (mildest, survivable into childhood with mild ID). Authors have proposed these represent "a continuum of the same clinical spectrum of cell cycle-opathies, rather than discrete clinical entities" (PMC6936249).
- **Critical period:** Embryonic/fetal neurogenesis and skeletal patterning windows, given the progenitor-depletion mechanism.

## 9. Inheritance and Population

- **Inheritance pattern:** Autosomal recessive (biallelic hypomorphic variants); rare de novo/compound heterozygous cases reported.
- **Penetrance/expressivity:** Full penetrance for biallelic hypomorphic genotypes but markedly variable expressivity (phenotype severity is genotype-dependent, per the exon 4 vs exons 5–10 correlation noted above).
- **Prevalence/incidence:** Ultra-rare; exact population prevalence is not established. Total published cases across all DONSON-associated phenotypes number in the tens (the founding 2017 series described 29 individuals with biallelic DONSON mutations across multiple families; subsequent series added further families through 2019–2026).
- **Consanguinity:** A notable proportion of reported families are consanguineous (homozygous variants identified via autozygosity mapping in several reports), consistent with a rare autosomal recessive disorder.
- **Founder effects:** The recurrent p.(Arg211Cys) allele has now been reported in multiple, apparently unrelated families (including a Turkish family, PMID:41612845), raising the possibility of a mutational hotspot or a shared founder haplotype — not conclusively established from available sources.
- **Sex ratio / geographic distribution:** No skewed sex ratio reported (consistent with autosomal inheritance); cases have been reported across diverse populations (European, Middle Eastern/Turkish, and others) without a described endemic geographic pattern.

## 10. Diagnostics

- **Primary diagnostic approach:** Clinical suspicion based on the combination of severe (disproportionate) microcephaly, IUGR/short stature, and characteristic skeletal (radial ray, patellar) and craniofacial features, confirmed by molecular genetic testing.
- **Genetic testing:**
  - **Exome/genome sequencing** is the primary diagnostic modality used in essentially all published cases; several diagnoses were made via research-based whole-exome or whole-genome sequencing, including one case solved only by **combined genome + transcriptome (RNA) sequencing** to detect a noncoding splice-disrupting variant not identifiable by exome alone (PMC5538549).
  - **Targeted gene panels** for microcephalic primordial dwarfism / Meier-Gorlin syndrome / Seckel syndrome typically now include *DONSON* alongside *ORC1, ORC4, ORC6, CDT1, CDC6, GMNN, CDC45, MCM5, PCNT, ATR, RNU4ATAC*, etc.
  - **Single-gene sequencing** of *DONSON* is reasonable when the clinical gestalt is highly suggestive (e.g., recurrent p.Arg211Cys hotspot).
  - Chromosomal microarray/karyotype are used to exclude alternative chromosomal causes of microcephalic dwarfism but are not diagnostic for DONSON disease itself.
- **Imaging:** Prenatal ultrasound (severe IUGR, microcephaly, limb shortening) and postnatal brain MRI (simplified gyral pattern, reduced cortical volume, hypoplastic/absent corpus callosum in severe cases) and skeletal radiographs (patellar aplasia/hypoplasia, radial ray anomalies).
- **Differential diagnosis:** Other microcephalic primordial dwarfisms — MOPD I (RNU4ATAC), MOPD II (PCNT), Seckel syndrome (ATR, CENPJ, CEP152, etc.), other Meier-Gorlin syndrome genes (ORC1/4/6, CDT1, CDC6, GMNN, CDC45, MCM5), 3-M syndrome, and Cornelia de Lange syndrome, need to be distinguished — genetically definitive but clinically overlapping.
- **Screening:** No population/newborn screening program exists (ultra-rare Mendelian disorder); prenatal diagnosis via targeted variant testing is possible in families with a known DONSON variant, and preimplantation genetic diagnosis is theoretically applicable for known-carrier couples.

## 11. Outcome / Prognosis

- **Survival:** Bimodal by phenotype severity — the MIMIS end of the spectrum is associated with **intrauterine fetal death or perinatal lethality** (severe growth restriction, microcephaly, and limb malformation incompatible with survival in the most severe reported fetuses). The MISSLA/MGS-like end of the spectrum is compatible with survival into childhood and beyond, albeit with lifelong short stature, microcephaly, and (in some) mild intellectual disability.
- **Morbidity:** Persistent short stature, microcephaly, and skeletal (particularly upper-limb/radial ray) anomalies; mild intellectual disability and speech delay in a subset of survivors.
- **No disease-specific FDA-approved therapy exists** — as with the great majority of ultra-rare Mendelian disorders (only ~5% of rare diseases overall have an FDA-approved treatment).
- **Prognostic factors:** Variant location/type appears to be the major driver of severity (exon 4 missense variants → milder MGS/FFS phenotype; frameshift and exon 5–10 variants → more severe microcephaly/developmental impairment) (PMC6936249).

## 12. Treatment

No disease-modifying or curative therapy exists for DONSON-related disease; management is entirely **supportive and multidisciplinary**, analogous to management approaches used across the microcephalic primordial dwarfism spectrum (e.g., MOPD II):

- **Growth management:** Auxological monitoring; growth hormone therapy is sometimes trialed empirically in primordial dwarfism syndromes generally, though no DONSON-specific efficacy data were identified in this search (suggested NCIT term: NCIT:C15986 Pharmacotherapy, generic, if used).
- **Neurodevelopmental support:** Early intervention, physical/occupational/speech therapy (NCIT:C15302 Physical Therapy; NCIT:C159273 Speech Therapy; NCIT:C121351 Occupational Therapy) for developmental delay and mild intellectual disability.
- **Orthopedic management:** Surgical correction of severe radial ray/thumb anomalies or patellar instability where functionally indicated (NCIT:C15329 Surgical Procedure; NCIT:C16186 Orthopedic Surgical Procedure).
- **Genetic counseling:** Essential for affected families given autosomal recessive inheritance and 25% recurrence risk per pregnancy for carrier couples; prenatal diagnosis/PGD offered where a familial variant is known (NCIT:C15240 Genetic Counseling).
- **Multidisciplinary surveillance:** As generalized for MPD/MOPD-spectrum disorders, follow-up should monitor for comorbidities described in related MPDs (e.g., MOPD II) such as cerebral vasculopathy, though DONSON-specific vasculopathy risk is not established in the literature reviewed — this should be treated as an extrapolation from the broader MPD category rather than a DONSON-specific finding.
- **Experimental/investigational therapy:** None identified in ClinicalTrials.gov or the literature reviewed; no gene therapy, small-molecule, or targeted approach is in development specifically for DONSON disease as of this search.

## 13. Prevention

- **Primary prevention:** Not applicable (Mendelian genetic disorder) beyond genetic counseling and reproductive options (carrier screening, prenatal diagnosis, PGD) in families with a known pathogenic variant.
- **Secondary prevention:** Early molecular diagnosis enables anticipatory multidisciplinary surveillance (growth, neurodevelopment, orthopedic) but does not prevent disease onset.
- **Public health measures:** None applicable — no environmental or infectious component.

## 14. Other Species / Natural Disease

No naturally occurring DONSON-related disease has been reported in non-human species in the literature surveyed here (no OMIA entries or veterinary case reports identified). *DONSON* orthologs exist across vertebrates (used experimentally in mouse and presumably zebrafish/other model systems — see below), but no spontaneous animal disease analog was found.

## 15. Model Organisms

- **Mouse (Mus musculus):**
  - **Constitutive/germline *Donson* knockout is embryonic lethal early in development** — directly supporting the inference that all human disease alleles must be hypomorphic, since a complete null is not compatible with life (ResearchGate table, "Donson loss of function is lethal in early embryonic mouse development," referencing PMID:28191891 supplementary data).
  - **Conditional (Cre-lox) knockout models** were therefore developed to study tissue-specific roles. *Donson* is widely expressed in proliferative and differentiation zones of the embryonic dorsal and ventral telencephalon, with expression declining postnatally.
    - Emx1-Cre-mediated deletion in the dorsal telencephalic (cortical excitatory/glutamatergic) lineage and Nkx2.1-Cre-mediated deletion in the ventral (GABAergic interneuron) lineage both caused extensive apoptosis in proliferating progenitors and postmitotic differentiating cells, with Nkx2.1-Cre deletion ablating ~75% of Nkx2.1-derived cortical GABAergic interneurons and also affecting oligodendrocyte precursor generation (PLOS Genetics 2021, PMC8011756).
  - This conditional-knockout model **recapitulates the human microcephaly phenotype at the cellular/progenitor level** (progenitor loss via apoptosis) though it does not model the skeletal/limb component of the human disease.
- **Patient-derived cell lines:** Primary fibroblasts and lymphoblastoid lines from affected individuals are the principal human cellular model, showing increased spontaneous replication fork stalling/asymmetry, impaired ATR checkpoint signaling (reduced CHK1/NBS1 phosphorylation), and elevated S-phase DNA damage — used extensively for functional variant characterization (complementation/rescue assays) (PMID:28191891; academic.oup.com/nar/51/18/9748).
- **In vitro/biochemical systems:** Cell-free Xenopus egg extract and reconstituted human replication systems have been used to define DONSON's biochemical role in CMG helicase assembly and its dimeric GINS-scaffolding function (single-molecule imaging studies, PMC10996697; PMC7616792).
- **Invertebrate models (Drosophila, zebrafish, C. elegans):** No DONSON-specific knockout/mutant phenotype data were identified in this search; general zebrafish microcephaly-modeling methodology exists for other MCPH genes but no DONSON-specific zebrafish study was found.
- **Model limitations:** The mouse conditional-knockout system captures the neural progenitor-depletion/microcephaly mechanism well but does not reproduce the skeletal (limb, patellar) phenotype seen in humans, and — because human disease alleles are hypomorphic rather than null — a true knockout may over-represent the severity of pathway disruption relative to the partial-function state present in patients.

---

## Sources

- [Mutations in DONSON disrupt replication fork stability and cause microcephalic dwarfism — Reynolds JJ et al., Nat Genet 2017;49(4):537–549, PMID:28191891 (PMC5450907)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5450907)
- [Biallelic and De Novo Variants in DONSON Reveal a Clinical Spectrum of Cell Cycle-opathies with Microcephaly, Dwarfism and Skeletal Abnormalities — Kim/Karaca et al., Am J Med Genet A 2019, PMID:31407851 (PMC6936249)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6936249)
- [Integrated genome and transcriptome sequencing identifies a noncoding mutation in the genome replication factor DONSON as the cause of microcephaly-micromelia syndrome (PMC5538549)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5538549)
- [Further Delineation of the Microcephaly-Micromelia Syndrome Associated with Loss-of-Function Variants in DONSON — Molecular Syndromology (PMC6528082)](https://ncbi.nlm.nih.gov/pmc/articles/PMC6528082)
- [Microcephalic primordial dwarfism with predominant Meier-Gorlin phenotype, ichthyosis, and multiple joint deformities — PMID:35298084](https://pubmed.ncbi.nlm.nih.gov/35298084/)
- [Meier-Gorlin syndrome due to a recurrent DONSON variant in a Turkish family — PMID:41612845](https://pubmed.ncbi.nlm.nih.gov/41612845/)
- [Linked-read genome sequencing identifies biallelic pathogenic variants in DONSON as a novel cause of Meier-Gorlin syndrome (PMC7042968)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7042968)
- [Microcephaly, short stature, and limb abnormality disorder due to novel autosomal biallelic DONSON mutations in two German siblings — Eur J Hum Genet (PMC6117362)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6117362)
- [DONSON facilitates Cdc45 and GINS chromatin association and is essential for DNA replication initiation — Nucleic Acids Research 2023, PMID:37638758](https://academic.oup.com/nar/article/51/18/9748/7252675)
- [Single-Molecule Imaging Reveals the Mechanism of Bidirectional Replication Initiation in Metazoa (PMC10996697)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10996697)
- [The structural mechanism of dimeric DONSON in replicative helicase activation](https://www.sciencedirect.com/science/article/pii/S109727652300761X)
- [DONSON, a gene responsible for microcephalic primordial dwarfism, ensures proper centriole duplication cycle by maintaining centriole engagement during interphase — bioRxiv](https://www.biorxiv.org/content/10.1101/2020.05.10.086777v1.full)
- [The microcephaly gene Donson is essential for progenitors of cortical glutamatergic and GABAergic neurons — PLOS Genetics 2021 (PMC8011756)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8011756)
- [OMIM #617604 — Microcephaly, Short Stature, and Limb Abnormalities (MISSLA)](https://omim.org/entry/617604)
- [OMIM *611428 — DOWNSTREAM NEIGHBOR OF SON; DONSON](https://omim.org/entry/611428)
- [OMIM #251230 — Microcephaly-Micromelia Syndrome](https://www.omim.org/entry/251230)
- [Orphanet: DONSON — DNA replication fork stabilization factor DONSON](https://www.orpha.net/en/disease/gene/DONSON)
- [Orphanet: Microcephaly-micromelia syndrome (ORPHA:572768)](https://www.orpha.net/en/disease/detail/572768)
- [GARD/NIH: DONSON-related microcephaly-short stature-limb abnormalities spectrum](https://rarediseases.info.nih.gov/diseases/22314/donson-related-microcephaly-short-stature-limb-abnormalities-spectrum)
- [The expanding genetic and clinical landscape associated with Meier-Gorlin syndrome — Eur J Hum Genet 2023](https://www.nature.com/articles/s41431-023-01359-z)
- [DONSON Gene — GeneCards](https://www.genecards.org/cgi-bin/carddisp.pl?gene=DONSON)
- [Primordial Dwarfism Information Sheet — University of Chicago Genetic Services Laboratory](https://dnatesting.uchicago.edu/sites/default/files/Primordial%20Dwarfism%20Information%20Sheet%206-13-19.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 15 |
| On topic | 12 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMC:PMC6936249` *(abstract only)*: "a continuum of the same clinical spectrum of cell cycle-opathies, rather than discrete clinical entities"
  - closest text in source: "Genes associated with these syndromes encode proteins that have crucial roles in DNA replication or in other critical steps of the cell cycle that link DNA replication to cell division"
