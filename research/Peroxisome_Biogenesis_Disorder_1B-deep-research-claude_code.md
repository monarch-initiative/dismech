---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-31T00:42:03.983546'
end_time: '2026-07-31T00:47:06.748609'
duration_seconds: 302.77
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Peroxisome Biogenesis Disorder 1B
  mondo_id: MONDO:0011101,PEX1-related,OMIM:601539,non-classic-Zellweger-spectrum/NALD/IRD
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
  total_cost_usd: 1.7740710000000002
  session_id: d6f6fe29-6d81-5583-8980-e24cd536256a
  stop_reason: end_turn
citation_count: 41
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Peroxisome Biogenesis Disorder 1B
- **MONDO ID:** MONDO:0011101,PEX1-related,OMIM:601539,non-classic-Zellweger-spectrum/NALD/IRD (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Peroxisome Biogenesis Disorder 1B** covering all of the
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

# Peroxisome Biogenesis Disorder 1B (PEX1-Related; Non-Classic Zellweger Spectrum Disorder — NALD/IRD Phenotype): Comprehensive Research Report

## 1. Disease Information

**Overview.** Peroxisome Biogenesis Disorder 1B (PBD1B) is the intermediate/mild end of the **Zellweger spectrum disorder (ZSD)** continuum caused by biallelic pathogenic variants in *PEX1*. Historically, PBD1B corresponded to the overlapping clinical entities **neonatal adrenoleukodystrophy (NALD)** and **infantile Refsum disease (IRD)** — the milder phenotypes of ZSD, as distinguished from classic/severe **Zellweger syndrome (PBD1A, OMIM 214100)**, which is caused by the most severe, null *PEX1* genotypes. Current clinical nosology (GeneReviews) treats ZSD as a single phenotypic continuum rather than three discrete diseases, because *PEX1* (and *PEX6*) genotypes span the full severity range: "the term 'ZSD' is now used to refer to all individuals with a defect in one of the ZSD-PEX genes regardless of phenotype" (GeneReviews, NBK1448).

**Key identifiers:**
- OMIM: **#601539** (PBD1B), gene locus *PEX1* **\*602136**; related severe allelic disorder Zellweger syndrome PBD1A **#214100**
- MONDO: **MONDO:0011101**
- Orphanet: **ORPHA912** (Zellweger spectrum disorder, umbrella term for the spectrum including this entity)
- ICD-10-CM: **E71.510** (Zellweger syndrome) / **Q87.8** (other specified congenital malformation syndromes) is used generically for ZSD-spectrum entries
- MeSH: Zellweger Syndrome (D019084)
- Gene: *PEX1* (HGNC:8850), chromosome 7q21.2
- Complementation group: CG1 (equivalent to complementation group E, CGE)

**Synonyms:** Peroxisome biogenesis disorder, complementation group 1 (CG1); Zellweger spectrum disorder (intermediate/mild forms); neonatal adrenoleukodystrophy (NALD); infantile Refsum disease (IRD); PEX1-related ZSD.

**Evidence base:** Information is drawn from aggregated disease-level clinical/genetic resources (OMIM, GeneReviews, Orphanet), longitudinal natural history cohort studies (e.g., NCT01668186), case reports/series, and mechanistic studies in cell and animal models — a mix of human-clinical, cohort-registry, and model-organism sources.

---

## 2. Etiology

**Disease causal factor:** Biallelic (homozygous or compound heterozygous) loss-of-function or hypomorphic pathogenic variants in ***PEX1*** (7q21.2), encoding a peroxisomal AAA+ ATPase. *PEX1* variants account for **~60–70% of all ZSD cases** — the single most common genetic cause (GeneReviews; PMID 20301621).

**Genetic risk factors / genotype determinants of severity:**
- **p.Ile700Tyrfs\*42** (a common frameshift/premature-truncation allele) — associated with **severe** disease when in trans with another null allele.
- **p.Gly843Asp (G843D, "Gly844Asp" in some mouse-model nomenclature offset by one residue)** — the most common **hypomorphic missense allele**, present in **~30% of ZSD patients**, producing a misfolded but partially functional PEX1 protein; homozygosity is associated with **milder, degenerative-type phenotypes without major congenital malformations**, with some patients surviving into adulthood (PMID 24503136; PMC4901203).
- Together, p.Ile700Tyrfs\*42 and p.Gly843Asp account for **~80% of *PEX1* pathogenic alleles** (GeneReviews NBK1448).
- Genotype-phenotype correlation: "PEX1 mutations in complementation group 1 ... correlate with severity of disease" — complete loss-of-function (large deletions, nonsense, frameshift) genotypes → severe (PBD1A/Zellweger); missense/hypomorphic combinations (including G843D) → intermediate-to-mild (PBD1B/NALD-IRD) (Nature Pediatric Research, PMID reference "pr2002118").
- At least **114 distinct *PEX1* mutations** have been reported (MedlinePlus/GeneReviews).

**Protective factors:** No genetic or environmental protective factors are established; disease severity is governed almost entirely by residual PEX1 functional capacity conferred by the specific allele combination (allelic "dosage" of function). No modifier genes are formally established, though allelic background effects have been documented for *PEX6* (p.Arg860Trp acts dominantly depending on allelic background), raising the possibility that similar background-dependent modifier effects could exist for *PEX1*, though this is not yet demonstrated.

**Environmental/other factors:** ZSD/PBD1B is a purely monogenic Mendelian disorder; no environmental, infectious, or lifestyle causal or risk factors are established. No gene-environment interaction data exist for *PEX1*.

**Suggested ontology terms:** Gene — `hgnc:8850` (PEX1); Inheritance — `HP:0000007` (Autosomal recessive inheritance).

---

## 3. Phenotypes

PBD1B (NALD/IRD-range ZSD) phenotypes are milder and more slowly progressive than classic Zellweger syndrome, but multisystemic. Suggested HPO terms and characteristics below (compiled from GeneReviews NBK1448, OMIM 601539, NORD, StatPearls NBK560676):

| Phenotype | HPO term | Onset | Severity/course | Frequency notes |
|---|---|---|---|---|
| Hypotonia | HP:0001252 | Neonatal/infantile | Variable; less severe than classic Zellweger | Most affected children (near-universal) |
| Developmental delay / intellectual disability | HP:0001263 / HP:0001249 | Infantile | Progressive in some; static in others; unlike Zellweger syndrome, some patients achieve head control, sit unsupported, or walk independently | Common but variable |
| Sensorineural hearing loss | HP:0000407 | Infantile–childhood, progressive | Progressive | Frequent; often severe |
| Retinal dystrophy / pigmentary retinopathy | HP:0000556 / HP:0000510 | Infantile–childhood | Progressive | Frequent |
| Cataracts | HP:0000518 | Infantile | Variable | Reported |
| Hepatomegaly / hepatic dysfunction (elevated LFTs, coagulopathy) | HP:0002240 / HP:0001392 | Infantile | Progressive to fibrosis in some | Common |
| Adrenal insufficiency | HP:0000846 | Any age, often subclinical | Progressive; requires surveillance | Occurs in a subset; often subclinical, detected on ACTH stimulation |
| Ataxia / peripheral neuropathy | HP:0001251 / HP:0009830 | Childhood | Progressive | Reported in milder/older survivors |
| Leukodystrophy / white matter disease on MRI | HP:0002352 | Variable, can present later | Can be progressive, mimicking X-ALD | Present in NALD-range phenotype |
| Renal cysts | HP:0000107 | Congenital-infantile | Static | Less common in milder forms than in classic Zellweger |
| Chondrodysplasia punctata (bone stippling, patella) | HP:0002832 / HP:0100255 | Congenital | Static | More typical of severe Zellweger; occasionally seen in milder PBD1B |
| Failure to thrive / feeding difficulty | HP:0001508 / HP:0011968 | Infantile | — | Common |
| Seizures | HP:0001250 | Variable | — | Less frequent/less severe than classic Zellweger |
| Amelogenesis imperfecta (dental enamel defects) | HP:0000705 | Childhood | — | Recognized secondary finding requiring dental surveillance |
| Nephrolithiasis (kidney stones) | HP:0000787 | Childhood-onset | — | Recognized complication, monitored via urine oxalate/creatinine ratio |
| Osteopenia/osteoporosis | HP:0000939 | Childhood | Progressive | Bone health surveillance recommended (vitamin D, bisphosphonate consideration) |

**Quality of life impact:** Combined sensory loss (vision + hearing), motor impairment, and cognitive delay substantially affect adaptive functioning; disease-specific QOL instruments are not well established, but functional impact is described qualitatively across natural-history cohort studies (e.g., NCT01668186, and the ophthalmic natural-history cohort study, medRxiv 2022.11.06.22279732).

**Distinguishing feature from classic Zellweger syndrome (PBD1A):** Unlike Zellweger syndrome, PBD1B patients typically **lack major congenital structural malformations** and show **a degree of psychomotor development** — some achieve head control, independent sitting, or walking — with disease dominated instead by **progressive sensorineural/degenerative** features (vision, hearing, neurologic).

---

## 4. Genetic/Molecular Information

**Causal gene:** *PEX1* (Peroxisome Biogenesis Factor 1), OMIM \*602136, HGNC:8850, chromosome 7q21.2. Encodes a 1,283 amino acid, ~143–147 kDa protein, a AAA+ (ATPases Associated with diverse cellular Activities) family ATPase.

**Variant classes causing PBD1B specifically:**
- Compound heterozygosity for one severe (null) and one hypomorphic allele, OR
- Homozygosity/compound heterozygosity for hypomorphic missense alleles (classically **p.Gly843Asp**), OR
- Combinations of hypomorphic alleles that retain partial PEX1 function.
- Contrast: **PBD1A (classic Zellweger, severe)** results from biallelic null/loss-of-function genotypes (large deletions, nonsense, frameshift such as p.Ile700Tyrfs\*42 in trans with another null allele).

**Variant classification (ACMG/ClinVar):** Missense (e.g., p.Gly843Asp — pathogenic/hypomorphic), frameshift (e.g., p.Ile700Tyrfs\*42 — pathogenic/null), nonsense, splice-site, and small indels are all reported; large deletions/duplications also occur (example ClinVar record: NM_000466.3(PEX1):c.2097dup (p.Ile700fs) associated with "Peroxisome biogenesis disorder 1B").

**Population/allele frequency:**
- The G843D hypomorphic allele is **relatively common throughout Europe**, less common in US cohorts; in **Japan, p.Arg633Ter predominates** instead, and the classic European alleles are largely absent (PMC12166394).
- Molecular testing panels detect **~98% of *PEX1* variants** in affected individuals (GeneReviews).

**Origin:** Exclusively germline (autosomal recessive Mendelian); no somatic PBD1B has been reported (this is a developmental/congenital metabolic disease, not neoplastic).

**Functional consequences:** Loss-of-function or partial loss-of-function of PEX1 ATPase activity → failure of the PEX1/PEX6 AAA-ATPase heterohexameric motor (the "Receptor Export Module," REM) to extract/recycle the PTS1-receptor PEX5 from the peroxisomal membrane after matrix-protein import, blocking further rounds of import and producing peroxisome-import-deficient "ghost peroxisomes" that carry the membrane but lack matrix enzymes (PMC6862443; PMC5762779; Nat Commun s41467-017-02474-4). The G843D variant specifically produces a **PEX1 protein with partial retained ATPase/import-supporting activity but reduced stability**, and is rapidly degraded by the proteasome — a defect amenable to pharmacologic chaperone rescue (biorxiv 2024.12.10.627778; PMC preprint).

**Modifier genes:** None formally validated for *PEX1* itself, though the analogous *PEX6* p.Arg860Trp allele shows allelic-background-dependent dominant behavior, illustrating that modifier/background effects are plausible in this gene family.

**Epigenetic information:** Not established/reported for PBD1B specifically; no disease-associated DNA methylation or histone modification signature has been characterized in the literature reviewed.

**Chromosomal abnormalities:** PBD1B is caused by intragenic *PEX1* variants (point mutations, small indels) rather than large chromosomal rearrangements; large deletions/duplications of *PEX1* are detected by deletion/duplication analysis as part of standard multigene panel testing but are not the predominant mutation type.

**Suggested ontology terms:** Gene — `hgnc:8850` (PEX1); Protein function — GO:0016887 (ATP hydrolysis activity), GO:0016558 (protein import into peroxisome matrix); Molecular function — GO:0004396 (unfoldase-related AAA-ATPase activity, mechanistically analogous term).

---

## 5. Environmental Information

PBD1B is a monogenic disorder; there are **no known environmental, toxic, occupational, or infectious causal or contributory factors**. No lifestyle risk-modifying factors (diet, smoking, exercise) are documented in the literature. This section is largely **not applicable** for this disease beyond standard supportive nutritional management (below), which addresses disease consequences (fat-soluble vitamin malabsorption) rather than etiology.

---

## 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream):**

1. **Molecular/upstream lesion:** Biallelic hypomorphic/partial-loss-of-function *PEX1* variants (e.g., G843D) → misfolded, unstable, but partially active PEX1 protein.
2. **Complex assembly failure:** PEX1 heterohexamerizes with PEX6 to form the AAA-ATPase "Receptor Export Module" (REM) that recycles PEX5 (the peroxisomal targeting signal-1, PTS1, receptor) from the peroxisomal membrane back to the cytosol after each round of matrix-protein import (PMC6862443, Nat Commun 2023 s41467-023-41640-9 — cryo-EM structure of the substrate-bound complex).
3. **Impaired matrix protein import:** With reduced PEX1/PEX6 REM activity, PEX5 is not efficiently extracted/recycled → progressive failure to import newly synthesized PTS1/PTS2-tagged matrix enzymes → formation of peroxisomal "ghost" membrane remnants that lack the full complement of >50 resident matrix enzymes.
4. **Biochemical consequences (multiple enzyme deficiencies in a single organelle):**
   - Failure of **β-oxidation of very-long-chain fatty acids (VLCFA, ≥C22)** → accumulation of C26:0, C26:1 in plasma.
   - Failure of α-oxidation → accumulation of **phytanic and pristanic acid**.
   - Failure of bile-acid side-chain oxidation → accumulation of **C27 bile-acid intermediates (DHCA, THCA)**.
   - Elevated **pipecolic acid**.
   - **Deficient synthesis** of plasmalogens (ether phospholipids) and **docosahexaenoic acid (DHA)**, both of which require peroxisomal enzymatic steps.
5. **Cellular consequences:** ER stress response and activation of pexophagy (autophagic clearance of dysfunctional peroxisomes) have been demonstrated transcriptomically in the zebrafish *pex1*-null model (PMC12626956); lipid dysregulation (VLCFA accumulation, DHA/plasmalogen deficiency) drives membrane and myelin lipid abnormalities.
6. **Tissue-level consequences:**
   - **CNS:** impaired myelination/leukodystrophy, neuronal dysfunction, sensorineural hearing loss (documented mechanistically via cochlear hair-cell-specific *Pex1* conditional knockout mouse — loss of Pex1 in inner ear hair cells causes cochlear synaptopathy and hearing loss, doi:10.3390/cells11243982).
   - **Retina:** photoreceptor/RPE lipid dysregulation and structural disruption (Pex1-G844D mouse RPE structural/lipid studies, biorxiv 2024.09.05.611330); disrupted outer nuclear/retinal layer architecture in zebrafish adults.
   - **Liver:** progressive hepatocellular injury/fibrosis (longitudinal Pex1-G844D mouse liver-disease-progression study, biorxiv 2025.05.08.652960).
   - **Adrenal cortex:** insufficiency from lipid-laden cortical dysfunction (mechanistically analogous to X-ALD adrenal involvement).
   - **Bone:** stippled epiphyses (chondrodysplasia punctata) in more affected individuals, reflecting disrupted plasmalogen-dependent cartilage/bone matrix processes.
7. **Clinical manifestation:** The cumulative multisystem, progressive, sensorineural/hepatic/neurologic phenotype characteristic of PBD1B (milder end of ZSD).

**Cell types involved:** hepatocyte (CL:0000182), cochlear hair cell (CL:0000855 or more specific inner/outer hair cell terms), retinal photoreceptor cell (CL:0000210) and retinal pigment epithelial cell (CL:0002586), adrenal cortex cell (CL:1000454), neuron (CL:0000540), oligodendrocyte (CL:0000128, for myelination defects), chondrocyte (CL:0000138, for stippled epiphyses).

**Suggested GO Biological Process terms:** GO:0016558 (protein import into peroxisome matrix), GO:0006635 (fatty acid beta-oxidation), GO:0001561 (fatty acid alpha-oxidation), GO:0097009 (energy homeostasis, less specific), GO:0008610 (lipid biosynthetic process), GO:0006687 (glycosphingolipid metabolic process — plasmalogen-adjacent), GO:0034389 (lipid droplet organization — peroxisome/pexophagy adjacent), GO:0044804 (autophagy of peroxisome/pexophagy).

**Omics/advanced technologies:** Transcriptomic profiling of *pex1*−/− zebrafish larvae shows upregulated ER-stress response genes and pexophagy pathway genes, and dysregulation of neurophysiological/visual-perception gene sets (PMC12626956; Frontiers 10.3389/fnmol.2025.1634536). Lipidomic studies in the zebrafish model reveal organ-specific accumulation of distinct fatty-acid species (bioRxiv 2021.01.03.425169). iPSC-derived models of ZSD show impaired peroxisome assembly and cell-type-specific lipid abnormalities (PMC4553005).

---

## 7. Anatomical Structures Affected

**Organ level (primary):** Brain/CNS, liver, adrenal glands, eye (retina, lens), inner ear (cochlea), kidney, skeletal system, peripheral nerves.
**Secondary/complications:** Cardiovascular (less prominent than in classic Zellweger, where congenital heart disease is common), dental (enamel), skeletal (osteopenia).
**Body systems:** Nervous, hepatobiliary, endocrine (adrenal), sensory (visual, auditory), skeletal, renal, digestive/nutritional (fat malabsorption).

**Tissue/cell level:**
- Neurons and oligodendrocytes (CNS white matter/myelination) — UBERON:0002240/UBERON:0001869
- Hepatocytes — UBERON:0001114/CL:0000182
- Cochlear hair cells — UBERON:0001846 (cochlea), CL:0000855 (auditory hair cell)
- Retinal photoreceptors, RPE — UBERON:0000966 (retina)
- Adrenal cortical cells — UBERON:0002134 (adrenal cortex)
- Chondrocytes at growth plate — UBERON:0002102 (epiphysis)

**Subcellular level:** The organelle itself — **peroxisome (GO:0005777, cellular component)** — is the primary site of dysfunction; downstream involvement of endoplasmic reticulum (ER stress, GO:0005783) and autophagosome/lysosome (pexophagy, GO:0005776) as clearance mechanisms for defective peroxisomes.

**Localization/laterality:** Disease is systemic/bilateral by nature (metabolic, not focal); hearing loss and retinopathy are bilateral and progressive; no meaningful lateralization pattern.

**Suggested UBERON terms:** UBERON:0002107 (liver), UBERON:0002369 (adrenal gland), UBERON:0000966 (retina), UBERON:0001846 (cochlea), UBERON:0001016 (nervous system), UBERON:0001474 (bone element).

---

## 8. Temporal Development

**Onset:** Typically **infantile** (many present as newborns/infants), though the intermediate/mild PBD1B phenotype can also present later in infancy or childhood; some very mild cases are recognized only in later childhood or, rarely, adulthood.
**Onset pattern:** Insidious-to-subacute for most features; not typically acute.

**Progression:**
- Disease course in PBD1B is **variably progressive**: sensorineural hearing loss and retinal dystrophy typically worsen over time; liver disease can progress to fibrosis; neurologic function may be relatively stable or slowly decline, in contrast to the rapidly fatal course of classic Zellweger syndrome.
- Leukodystrophy (progressive white-matter degeneration) can develop in a subset, causing loss of previously acquired developmental skills — a NALD-like course reminiscent of, and clinically overlapping with, X-linked adrenoleukodystrophy.
- **77% probability of reaching school age** has been cited for children who survive infancy with a non-progressive/milder course (GeneReviews NBK1448).

**Disease duration:** Chronic, lifelong (in contrast to the typically fatal first-year course of severe Zellweger syndrome/PBD1A).

**Patterns:** No spontaneous remission is described; disease is managed symptomatically rather than cured. No clearly defined "critical periods" beyond the general principle that earlier diagnosis enables earlier initiation of supportive/monitoring interventions (hearing aids, vision correction, cholic acid therapy, DHA supplementation) which may modify quality of life and possibly slow certain complications, though disease-modifying (curative) treatment does not yet exist.

---

## 9. Inheritance and Population

**Epidemiology (for the *PEX1*-driven ZSD spectrum overall, PBD1A+1B combined, from recent population-genetics modeling, PMC12166394):**
- **US birth incidence:**
  - Core model (known pathogenic variants only): ~15 births/year (13.8–16.1), i.e., **3.8–4.4 per million births (~1 in 245,000)**.
  - Expanded model (including predicted pathogenic variants): ~32 births/year (29.7–34.7), i.e., **8.1–9.5 per million births (~1 in 114,000)**.
- **US population prevalence** (patients <31 years old): ~200 (core model, mostly intermediate phenotype) to potentially ~900 (expanded model including undiagnosed mild cases).
- **Historical/older estimates** of ZSD overall incidence: **1 in 133,000 births** (US, confirmed via New York newborn screening data) vs. older literature estimate of **1 in 50,000** (now considered an overestimate) (GeneReviews NBK1448).
- **Japan:** markedly lower incidence, **~1 in 500,000 births**, attributable to the near-absence of the common European *PEX1* alleles (G843D, Ile700fs) in the Japanese population, where p.Arg633Ter predominates instead.
- A substantial proportion of intermediate/mild (PBD1B-range) patients are believed to be **underdiagnosed/unrecognized** by current biochemical screening practices, since VLCFA and plasmalogen levels can be normal or only mildly abnormal in milder cases.

**Inheritance pattern:** **Autosomal recessive.** Sibling recurrence risk 25% affected / 50% carrier / 25% unaffected; parents are obligate asymptomatic carriers.

**Penetrance:** Full penetrance is generally assumed for biallelic pathogenic genotypes, though **expressivity is highly variable** (severity ranges from neonatal death to adult survival) depending on the specific allele combination — this reflects variable expressivity more than incomplete penetrance.

**Genetic anticipation:** Not applicable (not a repeat-expansion disorder).

**Germline mosaicism:** Not specifically documented for *PEX1* in the reviewed literature, though it remains a theoretical possibility as in other autosomal recessive disorders and is relevant to recurrence-risk counseling when only one parent is confirmed as a carrier.

**Founder effects / geographic variant distribution:**
- p.Gly843Asp: common throughout **Europe** and in US cohorts of European ancestry.
- p.Arg633Ter: the predominant *PEX1* allele in **Japan**.
- These population-specific allele distributions materially affect regional incidence and the milder-vs-severe phenotype mix by geography.

**Consanguinity:** As an autosomal recessive disorder, consanguinity increases risk, though *PEX1*-ZSD is also frequently compound heterozygous (not homozygous) in outbred populations given the relatively high carrier frequency of common hypomorphic alleles like G843D.

**Carrier frequency:** Derivable from the birth-incidence modeling above (implicit in the population-genetics estimates); direct carrier frequency figures were not isolated from the excerpted sources but are being formally estimated in ongoing population-genetics modeling efforts (PMC12166394).

**Sex ratio:** No sex predilection is reported; autosomal recessive inheritance affects males and females equally.

---

## 10. Diagnostics

**Biochemical screening (first-line):**
| Test | Finding in PBD1B | Caveat |
|---|---|---|
| Plasma VLCFA (C26:0, C26:1, C24:0/C22:0 and C26:0/C22:0 ratios) | Elevated | May be **normal** in milder cases — insufficient alone to exclude diagnosis |
| Erythrocyte plasmalogens (C16-DMA, C18-DMA) | Reduced | Moderate-to-mild ZSD may show normal values |
| Plasma/urine pipecolic acid | Elevated | More reliable in older children than neonates |
| Plasma bile acid intermediates (DHCA, THCA) | Elevated | Plasma more sensitive than urine |
| C26:0-lysophosphatidylcholine (dried blood spot) | Elevated | Emerging newborn-screening-compatible biomarker (adapted from X-ALD NBS assays; can flag "other peroxisomal disorders" alongside X-ALD in pilot NBS cohorts) |

Because "some individuals with ZSD do not have abnormalities of these screening assays," a normal biochemical panel does **not** exclude PBD1B — molecular testing is required for definitive diagnosis (GeneReviews).

**Molecular genetic testing:**
- **Multigene panel** covering all 13–14 known ZSD-PEX genes (sequence + deletion/duplication analysis) is the preferred first-tier test when the phenotype suggests ZSD; detects ~98% of *PEX1* variants.
- **Exome/genome sequencing** preferred when the presentation is non-classic/doesn't strongly suggest ZSD.
- Single-gene *PEX1* sequencing alone is "rarely useful and typically NOT recommended" given genetic heterogeneity, unless a familial variant is already known.
- Diagnosis is confirmed by identification of **biallelic pathogenic/likely pathogenic *PEX1* variants**.

**Imaging:** Brain MRI (for white matter changes/leukodystrophy — recommended annual surveillance); abdominal ultrasound/liver elastography (fibroscan) for hepatic fibrosis surveillance.

**Functional/other tests:** Audiology (annual), ophthalmologic exam (annual, including ERG for retinal dystrophy), adrenal function testing (ACTH stimulation/cortisol by age 1 year and annually), urine oxalate-to-creatinine ratio (nephrolithiasis risk), coagulation studies and liver function tests, dental exam every 6 months (amelogenesis imperfecta).

**Histopathology/biopsy:** Not typically required for diagnosis in the genomic-testing era; historically, liver biopsy showed absence/reduction of peroxisomes and cholestatic changes; skin fibroblast culture allows complementation-group and peroxisome-import functional studies (used historically and still useful for VUS functional confirmation, e.g., PMC6968987 "Mild Zellweger syndrome due to functionally confirmed novel PEX1 variants").

**Prenatal/carrier/preimplantation testing:** Once the familial pathogenic variants are known, DNA-based prenatal or preimplantation genetic testing is available; biochemical prenatal testing (VLCFA/plasmalogens in chorionic villus/amniocyte samples) can supplement equivocal molecular results. **Carrier testing must be molecular** — "biochemical testing is not accurate for carrier testing, as the biochemical markers in carriers are normal."

**Differential diagnosis:** X-linked adrenoleukodystrophy (elevated VLCFA but distinct biochemical profile — isolated β-oxidation defect, not multi-enzyme), D-bifunctional protein (HSD17B4) deficiency, acyl-CoA oxidase 1 (ACOX1) deficiency (both single peroxisomal enzyme deficiencies that can mimic ZSD biochemically and clinically — the "pseudo-ZSD" single-enzyme disorders), congenital myotonic dystrophy, X-linked myotubular myopathy, spinal muscular atrophy, mitochondrial disease, Usher syndrome, other hereditary leukodystrophies.

**Screening programs:** No universal newborn screening for ZSD/PBD1B currently exists in most jurisdictions, but pilot programs adapting the C26:0-lysoPC LC-MS/MS assay used for X-ALD NBS have identified incidental "other peroxisomal disorders" cases, suggesting a path toward future ZSD-inclusive NBS.

**Suggested LOINC/ontology anchors:** VLCFA panel, erythrocyte plasmalogens, pipecolic acid, bile acid intermediates (specific LOINC codes not enumerated in sources reviewed — recommend confirming via LOINC search at curation time).

---

## 11. Outcome/Prognosis

**Survival:** Prognosis in PBD1B is markedly better than in classic/severe Zellweger syndrome (PBD1A), where death typically occurs within the first year of life. PBD1B patients (NALD/IRD-range) can survive into childhood, adolescence, and — particularly with the milder G843D-homozygous genotype — into **early adulthood**.

**School-age survival:** For children surviving infancy with a non-progressive/milder course, GeneReviews cites a **77% probability of reaching school age**.

**Morbidity/functional outcomes:** Progressive sensorineural hearing loss and retinal dystrophy commonly lead to combined visual and auditory impairment over time; motor and cognitive function are variably affected — unlike classic Zellweger syndrome, some individuals achieve independent ambulation and normal-range cognition. Leukodystrophy, when it develops, can cause loss of previously acquired skills (regression), analogous to childhood cerebral X-ALD.

**Complications:** Hepatic fibrosis/dysfunction, adrenal insufficiency (can be life-threatening if unrecognized during acute illness — "adrenal crisis" risk), nephrolithiasis, osteopenia/fracture risk, dental complications (amelogenesis imperfecta), feeding difficulties/failure to thrive.

**Prognostic factors:** Genotype is the dominant prognostic determinant — null/null genotypes → severe/lethal; hypomorphic combinations (e.g., G843D homozygosity) → milder, longer-surviving phenotype. Early recognition and proactive multisystem surveillance/supportive care (per management guidelines, e.g., PMID 26750748 Braverman et al. 2016 consensus guideline) likely improve functional outcomes, though disease-modifying therapy remains limited.

---

## 12. Treatment

There is currently **no curative or disease-reversing therapy**; management is multidisciplinary and supportive/preventive, targeting downstream consequences of peroxisomal dysfunction.

**Pharmacotherapy:**
- **Cholic acid (Cholbam®)** — FDA-approved (2015) as **adjunctive treatment for peroxisomal disorders including Zellweger spectrum disorders** in patients with manifestations of liver disease, steatorrhea, or fat-soluble vitamin malabsorption complications. Dosing: 10–15 mg/kg orally once daily or in two divided doses (pediatric and adult). Approval was based on a long-term single-arm trial + extension + case reports in 34 patients with peroxisomal disorders (including ZSD), showing improvement/normalization of liver-function labs, weight gain, developmental improvement, and prolonged survival in cholic-acid-responsive patients (PMC5065608; FDA NDA 205750; Travere Therapeutics press release).
  - Suggested MAXO term: MAXO:0000647-adjacent pharmacotherapy category; treatment_term = NCIT:C15986 (Pharmacotherapy); therapeutic_agent = CHEBI cholic acid (CHEBI:16359).
- **Fat-soluble vitamin supplementation** (A, D, E, K) for malabsorption; vitamin K especially for coagulopathy.
- **DHA (docosahexaenoic acid) supplementation** — studied in a randomized, double-blind, placebo-controlled trial at Johns Hopkins (100 mg/kg/day; 50 enrolled, 34 completed 1-year follow-up) targeting visual function and growth; results were **inconsistent** — earlier open-label case reports suggested improved tone and visual function, but the controlled trial did not yield a clear, consistent benefit (PMC3013498; PMID 8729110; Neurology 1993 43(7):1389).
- **Anti-seizure medications** — standard agents for the subset with seizures.
- **Bisphosphonates** — considered for osteopenia/bone fragility.

**Advanced/experimental therapeutics:**
- **AAV-mediated PEX1 gene augmentation** — proof-of-concept subretinal gene therapy (AAV8.CMV.HsPEX1.HA) tested in the Pex1-G844D mouse model of mild ZSD; improved peroxisomal function and electroretinogram (ERG) response (1.6–2.5-fold improvement in treated eyes; ~2-fold ffERG amplitude at 32 weeks vs. control) — first proof-of-concept gene augmentation therapy for a peroxisome biogenesis disorder, targeting the retina specifically (PMC8516995; Molecular Therapy Methods & Clinical Development, S2329-0501(21)00137-6). Not yet in human clinical trials.
- **Pharmacologic chaperones** — skin fibroblasts from G843D-genotype patients respond to chaperone-like small molecules that stabilize the mutant PEX1 protein and normalize peroxisomal β-oxidation in vitro, a promising precision approach specifically for the hypomorphic-allele (PBD1B-range) genotype (preclinical, biorxiv 2024.12.10.627778 and related literature).
- **Allogeneic hematopoietic stem cell transplantation (HSCT)** — reported in a single pediatric case report (PEX1-related ZSD, IRD phenotype) with significant clinical, biochemical (VLCFA normalization), and brain MRI improvement, and no abnormal findings at 2-year follow-up (PMC8424192, Frontiers in Pediatrics 2021). This is an isolated case, not a standard-of-care recommendation, and requires cautious interpretation pending larger series.

**Surgical/interventional:** Gastrostomy tube placement for persistent feeding difficulty; cataract extraction; lithotripsy or surgical management of kidney stones.

**Supportive/rehabilitative:** Hearing aids (or cochlear implantation in appropriate candidates) for hearing loss; vision correction; physical/occupational/speech therapy for developmental support; nutritional management.

**Treatment strategy:** A structured **annual surveillance protocol** underlies management — audiology, ophthalmology, liver panel + coagulation + ultrasound/fibroscan, brain MRI, adrenal function (ACTH/cortisol from age 1 year), urine oxalate/creatinine, and 6-monthly dental exams — enabling early detection and management of emerging complications (Braverman et al. 2016 consensus management guideline, PMID 26750748; GeneReviews NBK1448).

**Suggested MAXO terms:** MAXO:0000950 (supportive care), MAXO:0009030 (hearing aid usage), MAXO:0001001 (gene therapy — experimental), MAXO:0000747 (hematopoietic stem cell transplantation — case-report only), MAXO:0000088 (dietary intervention, DHA/vitamin supplementation).

---

## 13. Prevention

**Primary prevention:** Not applicable in the classic sense (no modifiable etiologic risk factor to intervene on); the sole primary-prevention lever is **reproductive/genetic — carrier screening and reproductive planning** in families with a known *PEX1* pathogenic variant.

**Secondary prevention (early detection):** Molecular carrier screening in at-risk relatives; prenatal diagnosis (DNA-based, once familial variants are known) and preimplantation genetic testing for at-risk couples; potential future expanded newborn screening leveraging C26:0-lysoPC or related biomarkers (currently piloted primarily for X-ALD but incidentally detects some "other peroxisomal disorders").

**Tertiary prevention:** The entire annual multisystem surveillance protocol described above (Section 12) functions as tertiary prevention — early detection of adrenal insufficiency, hepatic fibrosis, hearing/vision decline, bone fragility, and nephrolithiasis to enable early intervention and reduce morbidity.

**Genetic counseling:** Central to family management — includes carrier-status clarification via molecular testing (biochemical carrier testing is unreliable), discussion of the 25%/50%/25% recurrence risk pattern for future pregnancies, and availability of prenatal/preimplantation genetic testing once the familial variants are identified.

**Immunization/public health/prophylaxis:** Not applicable — this is a purely monogenic metabolic disorder with no infectious, vaccine-preventable, or public-health-intervention dimension.

---

## 14. Other Species / Natural Disease

**Taxonomy of studied model species:** Mouse (*Mus musculus*, NCBITaxon:10090), zebrafish (*Danio rerio*, NCBITaxon:7955).

**Orthologous gene:** Mouse *Pex1* (MGI:1339959); note the mouse numbering convention places the orthologous hypomorphic allele at **Gly844Asp** (one residue offset from human G843D) due to a minor sequence-length difference between species.

**Natural disease in other species:** No naturally occurring (spontaneous) veterinary PEX1-deficiency disease has been identified in the literature reviewed (no OMIA entry surfaced in this search) — all animal data derive from **engineered/induced genetic models**, not spontaneously occurring veterinary disease. This section is therefore largely not applicable; PBD1B does not have documented natural companion-animal or wildlife counterparts analogous to, e.g., naturally occurring lysosomal storage diseases in dogs/cats.

**Comparative biology:** Peroxisome biogenesis and the PEX1/PEX6 AAA-ATPase mechanism are evolutionarily conserved from yeast to humans (the REM/receptor-recycling mechanism was first characterized in yeast peroxisome biology), underlying the utility of zebrafish and mouse models as translationally relevant systems.

**Zoonotic potential/transmission:** Not applicable — this is a non-infectious, monogenic disorder.

---

## 15. Model Organisms

**Mouse models:**
- ***Pex1* global/null knockout mouse** — global deletion is **neonatal lethal**, precluding postnatal phenotypic study; this severe lethality models the human null/null (classic Zellweger, PBD1A) genotype and has driven development of conditional and hypomorphic alternatives.
- ***Pex1*-G844D hypomorphic knock-in mouse** — the primary translational model for **mild human ZSD (i.e., the PBD1B-range phenotype)**, recapitulating the human hypomorphic G843D genotype; viable postnatally (PMID 24503136; PMC4901203, "The Pex1-G844D mouse: A model for mild human Zellweger spectrum disorder"). Used extensively for:
  - Retinal/RPE structural and lipid characterization (biorxiv 2024.09.05.611330)
  - Liver disease progression natural history (biorxiv 2025.05.08.652960)
  - AAV-PEX1 gene augmentation proof-of-concept therapy (PMC8516995)
- **Conditional (floxed) *Pex1* mouse crossed with cell-type-specific Cre lines** (e.g., Gfi1-Cre, VGlut3-Cre for inner-ear hair cells) — used to dissect tissue-specific consequences (e.g., cochlear synaptopathy and hearing loss) while circumventing the neonatal lethality of the global knockout (doi:10.3390/cells11243982).

**Zebrafish model:**
- ***pex1*−/− loss-of-function zebrafish** — a recently reported (2025) model that is **viable** (unlike the mouse global knockout) and **recapitulates hallmark ZSD features**: ghost peroxisome formation, VLCFA/phytanic/pristanic acid accumulation, DHA/plasmalogen deficiency, ER-stress and pexophagy transcriptomic signatures, abnormal larval locomotor behavior, and disrupted adult retinal architecture (PMC12626956; Frontiers 10.3389/fnmol.2025.1634536). Its viability beyond early development is a key advantage over the mouse null model, enabling study of later-onset/progressive disease stages and serving as a **preclinical drug-screening platform**.
- A separate zebrafish Zellweger model study demonstrated **organ-specific accumulation of distinct fatty-acid species** and widespread gene-expression changes (bioRxiv 2021.01.03.425169).

**Cellular/iPSC models:**
- **Patient-derived induced pluripotent stem cells (iPSCs)** differentiated into relevant lineages show **impaired peroxisome assembly and cell-type-specific lipid abnormalities**, providing a human-cell-based platform complementary to animal models (PMC4553005).
- **Patient skin fibroblasts** (including from G843D-genotype patients) are used for complementation-group assignment, functional variant confirmation, and pharmacologic chaperone-response studies.

**Model recapitulation/limitations:** The Pex1-G844D mouse and zebrafish pex1-null models each capture different facets of the human mild-ZSD (PBD1B) phenotype — the mouse being the more established model for liver/retina longitudinal study and gene-therapy proof-of-concept, and zebrafish offering higher-throughput, viable, whole-organism assessment including behavior. Neither model fully recapitulates the human combination of progressive sensorineural (hearing + vision) decline together with hepatic and adrenal involvement in one system; cross-model and iPSC-based validation is used to build a fuller mechanistic picture.

**Research applications:** These models collectively support (1) natural-history/longitudinal organ-specific disease-progression studies, (2) mechanistic dissection of tissue-specific peroxisomal dysfunction (retina, liver, cochlea), and (3) preclinical testing of therapeutic candidates (AAV-PEX1 gene augmentation, pharmacologic chaperones, and potential future small-molecule or antisense approaches).

---

## Summary Table: Key Ontology Term Suggestions for Curation

| Domain | Suggested term(s) |
|---|---|
| Disease | MONDO:0011101 (PBD1B); OMIM:601539; ORPHA:912 (umbrella ZSD) |
| Gene | hgnc:8850 (PEX1) |
| Inheritance | HP:0000007 (Autosomal recessive) |
| Key phenotypes | HP:0001252 (Hypotonia), HP:0000407 (Sensorineural hearing loss), HP:0000510 (Retinal dystrophy), HP:0002240 (Hepatomegaly), HP:0000846 (Adrenal insufficiency), HP:0002352 (Leukodystrophy/CNS white matter abnormality), HP:0100255 (Chondrodysplasia punctata), HP:0000787 (Nephrolithiasis), HP:0000705 (Amelogenesis imperfecta), HP:0000939 (Osteoporosis/osteopenia) |
| Biological process | GO:0016558 (protein import into peroxisome matrix), GO:0006635 (fatty acid beta-oxidation), GO:0001561 (fatty acid alpha-oxidation), GO:0044804 (pexophagy) |
| Cellular component | GO:0005777 (peroxisome) |
| Cell types | CL:0000182 (hepatocyte), CL:0000855 (auditory hair cell), CL:0000210 (photoreceptor cell), CL:1000454 (adrenal cortex cell) |
| Anatomical | UBERON:0002107 (liver), UBERON:0002369 (adrenal gland), UBERON:0000966 (retina), UBERON:0001846 (cochlea) |
| Treatments | MAXO:0000950 (supportive care), NCIT:C15986 (Pharmacotherapy) + CHEBI:16359 (cholic acid), MAXO:0009030 (hearing aid usage), MAXO:0001001 (gene therapy, experimental) |

---

## Notes on Evidence Gaps

- No formally curated **modifier gene** for *PEX1* severity has been established (unlike the documented *PEX6* p.Arg860Trp allelic-background effect).
- **Carrier frequency** figures specific to *PEX1* were not directly located in the sources reviewed (birth-incidence modeling exists, PMC12166394, but explicit carrier-frequency percentages should be pulled directly from that paper's full text/supplement during curation).
- **DHA supplementation efficacy** is genuinely mixed in the literature (positive open-label reports vs. an inconclusive/negative-leaning randomized trial) — evidence should be curated as `PARTIAL` or with explicit conflicting evidence items rather than uniform `SUPPORT`.
- No naturally occurring veterinary/animal disease analog was identified — Section 14 findings should be marked "not applicable" unless a `dismech` curator's own OMIA search later surfaces a hit.
- The **AAV-PEX1 gene therapy** and **pharmacologic chaperone** approaches are preclinical (mouse-model, in vitro fibroblast) only — no human clinical trial data currently exists; the single **HSCT case report** is likewise a single-patient result and should be evidence-flagged accordingly (`evidence_source: HUMAN_CLINICAL`, but note the very low N and case-report study design in the `explanation` field).

---

### Sources

- [PEROXISOME BIOGENESIS DISORDER 1B; PBD1B - OMIM #601539](https://omim.org/entry/601539)
- [PEROXISOME BIOGENESIS FACTOR 1; PEX1 - OMIM *602136](https://omim.org/entry/602136)
- [NM_000466.3(PEX1):c.2097dup (p.Ile700fs) AND Peroxisome biogenesis disorder 1B - ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/RCV000853332/)
- [Zellweger Spectrum Disorder - GeneReviews® - NCBI Bookshelf (NBK1448)](https://www.ncbi.nlm.nih.gov/books/NBK1448/)
- [PEX1 gene - MedlinePlus Genetics](https://medlineplus.gov/download/genetics/gene/pex1.pdf)
- [Pex1 loss-of-function in zebrafish is viable and recapitulates hallmarks of Zellweger spectrum disorders - PMC12626956](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12626956/)
- [A novel PEX1 mutation in a Moroccan family with Zellweger spectrum disorders - Human Genome Variation](https://www.nature.com/articles/hgv20179)
- [Longitudinal study of liver disease progression in the PEX1-Gly844Asp mouse model of mild Zellweger Spectrum Disorder - bioRxiv](https://www.biorxiv.org/content/10.1101/2025.05.08.652960.full.pdf)
- [Estimation of PEX1-mediated Zellweger spectrum disorder births and population prevalence by population genetics modeling - PMC12166394](https://pmc.ncbi.nlm.nih.gov/articles/PMC12166394/)
- [The Pex1-G844D mouse: a model for mild human Zellweger spectrum disorder - PubMed 24503136](https://pubmed.ncbi.nlm.nih.gov/24503136/)
- [The Pex1-G844D Mouse: A Model for Mild Human Zellweger Spectrum Disorder - PMC4901203](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4901203/)
- [PEX1 Mutations in Complementation Group 1 of Zellweger Spectrum Patients Correlate with Severity of Disease - Pediatric Research](https://www.nature.com/articles/pr2002118)
- [AAV-mediated PEX1 gene augmentation improves visual function in the PEX1-Gly844Asp mouse model - PMC8516995](https://pmc.ncbi.nlm.nih.gov/articles/PMC8516995/)
- [Disorders of peroxisome assembly and function - MedLink Neurology](https://www.medlink.com/articles/disorders-of-peroxisome-assembly-and-function)
- [Longitudinal Natural History Study of Patients With Peroxisome Biogenesis Disorders (PBD) - ClinicalTrials.gov NCT01668186](https://clinicaltrials.gov/study/NCT01668186)
- [Peroxisome Biogenesis Disorders in the Zellweger Spectrum: Ophthalmic Findings from a New Natural History Study Cohort - medRxiv](https://www.medrxiv.org/content/10.1101/2022.11.06.22279732.full.pdf)
- [Zellweger Spectrum Disorders - NORD](https://rarediseases.org/rare-diseases/zellweger-spectrum-disorders/)
- [A Mechanistic Perspective on PEX1 and PEX6, Two AAA+ Proteins of the Peroxisomal Protein Import Machinery - PMC6862443](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6862443/)
- [The peroxisomal AAA-ATPase Pex1/Pex6 unfolds substrates by processive threading - Nature Communications](https://www.nature.com/articles/s41467-017-02474-4)
- [The peroxisomal AAA-ATPase Pex1/Pex6 unfolds substrates by processive threading - PMC5762779](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5762779/)
- [PEX1^G843D^ remains functional in peroxisome biogenesis but is rapidly degraded by the proteasome - bioRxiv](https://www.biorxiv.org/content/10.1101/2024.12.10.627778.full.pdf)
- [Structure of the peroxisomal Pex1/Pex6 ATPase complex bound to a substrate - Nature Communications](https://www.nature.com/articles/s41467-023-41640-9)
- [Cholic acid therapy in Zellweger spectrum disorders - PMC5065608](https://pmc.ncbi.nlm.nih.gov/articles/PMC5065608/)
- [U.S. FDA Approves Cholbam for the Treatment of Rare Bile Acid Synthesis Disorders - Travere Therapeutics](https://ir.travere.com/news-releases/news-release-details/us-food-and-drug-administration-approves-cholbam-treatment-rare/)
- [205750Orig1s000 - FDA ODMemo](https://www.accessdata.fda.gov/drugsatfda_docs/nda/2015/205750Orig1s000ODMemo.pdf)
- [CHOLBAM (cholic acid) capsules label - FDA](https://www.accessdata.fda.gov/drugsatfda_docs/label/2015/205750lbl.pdf)
- [Allogeneic Hematopoietic Stem Cell Transplantation for PEX1-Related Zellweger Spectrum Disorder: A Case Report and Literature Review - PMC8424192](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8424192/)
- [Docosahexaenoic acid therapy in peroxisomal diseases: Results of a double-blind, randomized trial - PMC3013498](https://ncbi.nlm.nih.gov/pmc/articles/PMC3013498)
- [Docosahexaenoic acid therapy in docosahexaenoic acid-deficient patients with disorders of peroxisomal biogenesis - PubMed 8729110](https://pubmed.ncbi.nlm.nih.gov/8729110/)
- [Docosahexaenoic acid – A new therapeutic approach to peroxisomal-disorder patients - Neurology](https://www.neurology.org/doi/10.1212/wnl.43.7.1389)
- [Structure of the N-terminal Domain of PEX1 AAA-ATPase - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0021925820677973)
- [Zellweger Syndrome - an overview - ScienceDirect Topics](https://www.sciencedirect.com/topics/nursing-and-health-professions/zellweger-syndrome)
- [Zellweger Spectrum Disorder - StatPearls - NBK560676](https://www.ncbi.nlm.nih.gov/books/NBK560676/)
- [Zellweger syndrome; identification of mutations in PEX19 and PEX26 gene in Saudi families - PMC11705544](https://pmc.ncbi.nlm.nih.gov/articles/PMC11705544/)
- [Loss of Pex1 in Inner Ear Hair Cells Contributes to Cochlear Synaptopathy and Hearing Loss - Cells (doi:10.3390/cells11243982)](https://doi.org/10.3390/cells11243982)
- [Orphanet: Zellweger syndrome (ORPHA912)](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=en&Expert=912)
- [2024 ICD-10-CM Diagnosis Code E71.510: Zellweger syndrome](https://www.icd10data.com/ICD10CM/Codes/E00-E89/E70-E88/E71-/E71.510)
- [Induced pluripotent stem cell models of Zellweger spectrum disorder show impaired peroxisome assembly and cell type-specific lipid abnormalities - PMC4553005](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4553005/)
- [A pilot study of newborn screening for X-linked adrenoleukodystrophy... - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0009898123004552)
- [Mild Zellweger syndrome due to functionally confirmed novel PEX1 variants - PMC6968987](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6968987/)
- [Mild form of Zellweger Spectrum Disorders (ZSD) due to variants in PEX1: Detailed clinical investigation in a 9-year-old female - PMC7306489](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7306489/)