---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-01T20:29:06.585344'
end_time: '2026-07-01T20:34:26.651341'
duration_seconds: 320.07
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Complex Hereditary Spastic Paraplegia
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
  web_search_requests: 19
  num_turns: 21
  total_cost_usd: 2.1402728
  session_id: 4a9a1b97-982c-5eb7-aa46-b5df71ea4244
  stop_reason: end_turn
citation_count: 67
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Complex Hereditary Spastic Paraplegia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Complex Hereditary Spastic Paraplegia** covering all of the
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

# Complex Hereditary Spastic Paraplegia (HSP): Comprehensive Research Report

## 1. Disease Information

**Overview.** Hereditary spastic paraplegia (HSP) is not a single disease but a large, clinically and genetically heterogeneous group of inherited neurodegenerative disorders whose unifying pathological feature is retrograde ("dying-back"), length-dependent axonal degeneration of the corticospinal tracts (and often the dorsal columns), producing progressive lower-limb spasticity and weakness ([MedLink Neurology](https://www.medlink.com/articles/hereditary-spastic-paraplegia); [PMC6827077](https://pmc.ncbi.nlm.nih.gov/articles/PMC6827077/)). HSPs are clinically split into:
- **Pure (uncomplicated) HSP** — progressive spastic paraplegia with hyperreflexia, extensor plantar responses (Babinski sign), and urinary urgency/bladder dysfunction as essentially the only findings ([GeneReviews NBK1509](https://www.ncbi.nlm.nih.gov/books/NBK1509/)).
- **Complex (complicated) HSP** — spastic paraplegia plus additional neurological features (ataxia, peripheral neuropathy, epilepsy, intellectual disability/cognitive decline, extrapyramidal signs/parkinsonism, optic atrophy, retinopathy, deafness) and/or non-neurological systemic features (dysmorphism, skeletal deformity, skin changes) ([PMC4939695](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4939695/); [PMC8749458](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8749458/)).

More than 88 spastic paraplegia (SPG) gene loci have been described, with 40+ confirmed causal genes, spanning autosomal dominant (AD), autosomal recessive (AR), X-linked, and (rarely) mitochondrial inheritance ([PMC8662366](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8662366/); [Pharos disease page](https://pharos.nih.gov/diseases/complex%20hereditary%20spastic%20paraplegia)). Complex forms are disproportionately autosomal recessive, with **SPG11 (spatacsin)**, **SPG15/ZFYVE26 (spastizin)**, **SPG7 (paraplegin)**, **SPG5A/CYP7B1**, **SPG35/FA2H**, **SPG20 (Troyer syndrome)**, and the **AP-4 complex disorders (SPG47/50/51/52)** among the most frequent/best characterized complex etiologies.

**Key identifiers.**
- Pharos lists "complex hereditary spastic paraplegia" as a distinct disease-concept entry ([Pharos](https://pharos.nih.gov/diseases/complex%20hereditary%20spastic%20paraplegia)).
- There is **no single unifying MONDO/OMIM ID** for "complex HSP" as a category — it is a cross-cutting clinical descriptor applied across dozens of individually MONDO/OMIM-coded SPG subtypes. Representative examples: pure-or-complex AD spastic paraplegia group **MONDO:0008438**; AR complex spastic paraplegia (SPG23) **MONDO:0010046**; pure-or-complex AR spastic paraplegia (SPG48) **MONDO:0013342** ([search aggregation](https://www.wikidata.org/wiki/Q4664694)).
- Individual OMIM entries exist per subtype, e.g., SPG3A **OMIM #182600**, SPG5A **OMIM #270800**, SPG7 **OMIM #607259**, SPG12 **OMIM #604805** ([OMIM](https://omim.org/entry/182600)).
- Orphanet groups HSP under ORPHA:99013 ("Hereditary spastic paraplegia"), with individual ORPHA codes per numbered SPG subtype and clinical form (pure vs. complicated).
- ICD-10: **G11.4** (hereditary spastic paraplegia); ICD-11: **8A02.1**.
- MeSH: **D015419** (Spastic Paraplegia, Hereditary).

**Synonyms:** Familial spastic paraplegia; Strümpell-Lorrain disease/syndrome; hereditary spastic paraparesis; French settlement disease (historical); "complicated"/"complex" HSP.

**Evidence base:** Predominantly aggregated disease-level literature (case series, natural-history cohorts, genetic-diagnostic cohorts) rather than large-scale EHR studies, though a few population-based epidemiologic studies exist (Norway, England/Northern Ireland; see Section 9) ([PMC12210554](https://pmc.ncbi.nlm.nih.gov/articles/PMC12210554/)).

---

## 2. Etiology

**Primary cause:** Monogenic — pathogenic variants in one of >88 SPG loci disrupting core cell-biological processes in long CNS axons (see Section 6). Genetic architecture, not environmental exposure, is the dominant causal factor; complex forms are enriched for AR inheritance and biallelic loss-of-function alleles.

**Genetic risk factors:**
- Causal, highly penetrant variants in **SPAST (SPG4)**, **ATL1 (SPG3A)**, **REEP1 (SPG31)** account for pure HSP; **SPAST/ATL1/REEP1 together account for well over 50% of all HSP** ([JCI PMC2846052](https://pmc.ncbi.nlm.nih.gov/articles/PMC2846052/)).
- Complex/recessive HSP causal genes: **SPG11 (spatacsin)** — most prevalent AR complex HSP gene (~8% of registered AR HSP cases) ([Frontiers/PMC search synthesis](https://pmc.ncbi.nlm.nih.gov/articles/PMC8004882/)); **SPG15/ZFYVE26**; **SPG7 (paraplegin)**; **CYP7B1 (SPG5A)**; **FA2H (SPG35)**; **SPG20 (spartin, Troyer syndrome)**; **AP4B1/AP4M1/AP4E1/AP4S1 (SPG47/50/51/52)**.
- Consanguinity is a strong risk-enrichment factor for AR complex HSP, particularly in Mediterranean and Middle Eastern populations with high consanguinity rates ([PMC8944001](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8944001/)).
- Modifier genes/digenic inheritance: recent work reports **digenic SPG7/AFG3L2** interactions modulating motor neuron and cerebellar phenotypes (medRxiv preprint, 2025) ([medRxiv](https://www.medrxiv.org/content/10.1101/2025.07.05.24312261.full.pdf)).

**Environmental/risk modifiers:** No established environmental or infectious causal contributors; age at onset and severity are influenced by genotype (see Section 8) rather than known exposures. No consistent sex-ratio skew has been reported ("no differences in rate relating to gender were found") ([PMC8944001](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8944001/)).

**Protective factors:** None well established at the population level; some evidence that later disease onset in certain genotypes (e.g., SPG3A vs. SPG4) correlates with slower progression, which may reflect allelic/genetic background effects rather than a true protective factor ([Springer natural history](https://link.springer.com/article/10.1007/s00415-025-13606-y)).

**Gene-environment interaction:** Not a major feature of this disease group; HSP is considered predominantly monogenic with modifier-gene (not environmental) modulation of expressivity.

---

## 3. Phenotypes

### Core "pure" phenotype (present in virtually all HSP, complex or pure)
| Phenotype | HPO term | Notes |
|---|---|---|
| Lower limb spasticity | HP:0002061 (Spastic paraplegia) / HP:0007256 | Core feature; progressive |
| Hyperreflexia | HP:0001347 | 93.9% in SPG4 cohorts |
| Babinski sign (extensor plantar response) | HP:0003487 | 71.9% in SPG4 |
| Lower limb muscle weakness | HP:0007340 | 54.2% (proximal) in SPG4 |
| Urinary bladder sphincter dysfunction / urgency | HP:0002839 / HP:0000012 | ~28.7–50% |
| Pes cavus | HP:0001761 | Frequent secondary orthopedic finding |
| Ankle clonus | HP:0013359 | Common exam finding |

Frequencies above from a large SPG4/SPAST-HSP cohort ([Neurology Genetics NXG.0000000000000664](https://www.neurology.org/doi/10.1212/NXG.0000000000000664)).

### Complex-form additional phenotypes (by representative subtype)
| Subtype/Gene | Additional phenotypes | HPO terms |
|---|---|---|
| SPG11 (spatacsin) / SPG15 (spastizin) | Thin corpus callosum, cognitive impairment/intellectual disability, cerebellar ataxia, cataracts, pigmentary retinopathy, early-onset parkinsonism, peripheral neuropathy | HP:0033725 (thin corpus callosum), HP:0001249 (ID), HP:0001251 (ataxia), HP:0000518 (cataract), HP:0000580 (pigmentary retinopathy), HP:0002548 (parkinsonism) |
| SPG7 (paraplegin) | Cerebellar ataxia, optic atrophy, progressive external ophthalmoplegia, nystagmus/dysmetric saccades, peripheral neuropathy | HP:0001251, HP:0000648 (optic atrophy), HP:0000544, HP:0000639 |
| SPG5A (CYP7B1) | Afferent ataxia (dorsal-column sensory loss), sometimes optic atrophy/white-matter changes | HP:0001251, HP:0000648 |
| SPG35 (FA2H) | Intellectual disability, seizures, leukodystrophy (white-matter abnormalities), extrapyramidal signs, sometimes brain iron accumulation | HP:0001249, HP:0001250 (seizure), HP:0002171 (leukoencephalopathy) |
| SPG20 (spartin, Troyer syndrome) | Distal amyotrophy (small hand-muscle wasting), dysarthria, short stature, mild intellectual disability, skeletal deformity | HP:0003693 (distal amyotrophy), HP:0001260 (dysarthria), HP:0004322 (short stature) |
| AP-4-HSP (SPG47/50/51/52) | Severe global developmental delay, microcephaly, seizures, brain malformation, early hypotonia progressing to hypertonia/spasticity, loss of ambulation, stereotypic laughter | HP:0001263 (developmental delay), HP:0000252 (microcephaly), HP:0001250, HP:0001252 (hypotonia)→HP:0001276 (hypertonia) |

**Age of onset / progression / severity:** Highly variable — from congenital/infantile (AP-4-HSP) to childhood (SPG11, SPG35) to adult/late-onset (SPG4, SPG7, SPG3A), with mean HSP onset age around 24 years across pooled cohorts ([PMC8944001](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8944001/)). Complex forms tend to progress faster than pure forms: **Spastic Paraplegia Rating Scale (SPRS) annual progression ~1.3 points/year in complicated HSP vs. 0.6 points/year in pure HSP** ([Austrian natural history cohort, Springer 2025](https://link.springer.com/article/10.1007/s00415-025-13606-y)). Disease severity/progression is genotype-dependent: SPG11 carries the highest severity burden; SPG3A tends to progress more slowly than SPG4 ([same source](https://pmc.ncbi.nlm.nih.gov/articles/PMC12835074/)).

**Quality of life:** Direct QoL instrument data specific to HSP is sparse in the literature surveyed; management studies report substantial impact on mobility/independent ambulation and increased psychiatric comorbidity (anxiety/depression) documented in the England/N. Ireland epidemiologic cohort ([PMC12210554](https://pmc.ncbi.nlm.nih.gov/articles/PMC12210554/)).

---

## 4. Genetic/Molecular Information

**Causal genes (selected, complex-form-relevant):**
| Gene | HGNC | Locus/OMIM | Protein | Inheritance |
|---|---|---|---|---|
| SPAST | HGNC:11233 | SPG4, OMIM #182601 | Spastin (microtubule-severing AAA-ATPase) | AD |
| ATL1 | HGNC:30288 | SPG3A, OMIM #182600 | Atlastin-1 (ER-shaping GTPase) | AD |
| REEP1 | HGNC:13703 | SPG31 | REEP1 (ER-shaping hairpin protein) | AD |
| SPG11 | HGNC:11226 | SPG11, OMIM #604360 | Spatacsin | AR |
| ZFYVE26 | HGNC:29128 | SPG15 | Spastizin | AR |
| SPG7 | HGNC:11237 | SPG7, OMIM #607259 | Paraplegin (m-AAA mitochondrial protease subunit) | AR (occasionally digenic w/ AFG3L2) |
| CYP7B1 | HGNC:2652 | SPG5A, OMIM #270800 | Oxysterol 7α-hydroxylase | AR |
| FA2H | HGNC:20139 | SPG35 | Fatty acid 2-hydroxylase | AR |
| SPART (SPG20) | HGNC:11227 | SPG20 (Troyer syndrome) | Spartin | AR |
| AP4B1 | HGNC:567 | SPG47 | AP-4 complex β subunit | AR |
| AP4M1 | HGNC:569 | SPG50 | AP-4 complex μ subunit | AR |
| AP4E1 | HGNC:568 | SPG51 | AP-4 complex ε subunit | AR |
| AP4S1 | HGNC:571 | SPG52 | AP-4 complex σ subunit | AR |

**Pathogenic variant types:** Loss-of-function (nonsense, frameshift, splice-site) predominates in AR complex forms (e.g., SPG11, SPG20, AP-4 genes are essentially null alleles: "the pathogenesis of Troyer syndrome results from a loss-of-function mechanism" rather than a toxic truncated protein) ([Wikipedia SPG20 synthesis](https://en.wikipedia.org/wiki/SPG20)). Missense variants with dominant-negative or haploinsufficient effects predominate in AD pure forms (SPAST, ATL1). Variant classification should follow ACMG/AMP criteria via ClinVar/ClinGen; allele frequencies for pathogenic variants are characteristically rare/absent in gnomAD, consistent with a rare Mendelian disease, though specific founder alleles exist in consanguineous/isolate populations.

**Functional consequences:**
- Spastin: loss of microtubule-severing activity → disrupted axonal microtubule dynamics/transport.
- Atlastin-1/REEP1: loss of ER tubule-fusion/shaping activity, disrupting the tubular ER network's coordination with microtubules in long axons ([PMC2846052](https://pmc.ncbi.nlm.nih.gov/articles/PMC2846052/)).
- Spatacsin/spastizin (SPG11/SPG15): loss of AP-5-adaptor accessory function → defective lysosomal reformation/tubulation and autophagosome-lysosome fusion, causing autophagosome/enlarged-lysosome accumulation ([PMC4078876](https://pmc.ncbi.nlm.nih.gov/articles/PMC4078876/)).
- Paraplegin (SPG7): loss of m-AAA mitochondrial protease function → mitochondrial proteostasis failure, permeability-transition-pore dysregulation, ATPase deficiency ([Lancet eBioMedicine](https://www.thelancet.com/journals/ebiom/article/PIIS2352-3964(20)30426-6/fulltext)).
- CYP7B1: loss of oxysterol 7α-hydroxylase activity → toxic accumulation of 25- and 27-hydroxycholesterol, which are neurotoxic and blood-brain-barrier permeable ([ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0022510X20305475); [PubMed 18252231](https://pubmed.ncbi.nlm.nih.gov/18252231/)).
- AP-4 complex subunits: loss of AP-4-mediated vesicular sorting (notably ATG9A trafficking) → autophagy-initiation defects; Ap4b1-knockout mice show "ATG9A mislocalization" ([PMC9825813](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9825813/)).

**Modifier genes:** AFG3L2 as a digenic modifier/co-causal partner with SPG7 in some motor neuron/cerebellar presentations ([medRxiv 2025](https://www.medrxiv.org/content/10.1101/2025.07.05.24312261.full.pdf)).

**Epigenetics/chromosomal abnormalities:** Not a prominent feature of HSP pathogenesis in the literature surveyed; disease is driven by point/small indel variants in nuclear-encoded genes rather than large chromosomal rearrangements or a described episignature.

---

## 5. Environmental Information

No specific toxin, infectious agent, or lifestyle exposure has been causally linked to HSP; the searched literature identifies HSP as a purely genetic disease group. Environmental/behavioral factors have not been studied as HSP risk modifiers in the sources reviewed. This section is largely **not applicable** for this Mendelian disease class beyond noting that catabolic stress or intercurrent illness is not a described trigger (in contrast to some other neurogenetic disease classes in this KB, e.g., metabolic intoxication disorders).

---

## 6. Mechanism / Pathophysiology

**Core convergent pathophysiology:** Regardless of causal gene, HSP mechanistically converges on **length-dependent ("dying-back") retrograde axonal degeneration of the corticospinal tract** (and often dorsal columns), because these are the longest axons in the human CNS (up to ~1 m) and are maximally dependent on efficient long-range organelle/cargo transport and membrane maintenance ([PMC6827077](https://pmc.ncbi.nlm.nih.gov/articles/PMC6827077/)). "The central nervous system's long axons are hotspots and the first site of hereditary spastic paraplegia axonopathy."

**Major convergent molecular pathway clusters** (from [PMC8004882](https://pmc.ncbi.nlm.nih.gov/articles/PMC8004882/) and [PMC6031053](https://pmc.ncbi.nlm.nih.gov/articles/PMC6031053/)):

1. **ER shaping / membrane trafficking (SPAST, ATL1, REEP1 axis).** Atlastin-1 (a GTPase) mediates homotypic fusion of ER tubules to form three-way junctions of the tubular ER network; it physically interacts with spastin (microtubule-severing AAA-ATPase) and REEP1 (a hairpin ER-shaping protein), and this tripartite complex "coordinate[s] microtubule interactions with the tubular ER network" specifically within long corticospinal axons ([JCI, PubMed 20200447](https://pubmed.ncbi.nlm.nih.gov/20200447/)). Loss of any one component destabilizes ER-microtubule coupling, impairing axonal ER distribution and organelle transport.
2. **Lysosomal/autophagosome maturation (SPG11/SPG15 axis).** Spatacsin (SPG11) and spastizin (SPG15) form a complex, cooperating with the AP-5 adaptor complex in late-endosome/lysosome membrane sorting; loss of function causes defective autophagosome-to-lysosome fusion, lysosome depletion, and enlarged/dysfunctional lysosomes, driving neurodegeneration with the distinctive thin-corpus-callosum, cognitive, and retinal phenotype ([PMC4078876](https://pmc.ncbi.nlm.nih.gov/articles/PMC4078876/); [PMC4540459](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4540459/)). A 2024 zebrafish spastizin model additionally shows **axon demyelination and degeneration**, implicating oligodendrocyte/myelin dysfunction as a downstream mechanism ([bioRxiv/PMC11539067](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11539067/)).
3. **Mitochondrial quality control (SPG7 axis).** Paraplegin, part of the mitochondrial inner-membrane m-AAA protease, is required for mitochondrial protein quality control and ribosome assembly; its loss causes ATPase deficiency, impaired permeability-transition-pore "flickering," and secondary anterograde/retrograde axonal transport failure, producing progressive distal axonopathy of spinal and peripheral nerves that faithfully recapitulates the human SPG7 phenotype in Spg7-knockout mice ([Lancet eBioMedicine](https://www.thelancet.com/journals/ebiom/article/PIIS2352-3964(20)30426-6/fulltext)).
4. **Cholesterol/oxysterol metabolism (CYP7B1/SPG5A axis).** Loss of oxysterol 7α-hydroxylase blocks the alternative bile-acid synthesis pathway, causing toxic accumulation of 25- and 27-hydroxycholesterol, which cross the blood-brain barrier and are directly neurotoxic to corticospinal and dorsal-column axons ([ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0022510X20305475)).
5. **Complex sphingolipid/myelin lipid metabolism (FA2H/SPG35 axis).** Loss of fatty acid 2-hydroxylase impairs synthesis of 2-hydroxylated sphingolipids required for normal myelin composition, producing a leukodystrophy-like phenotype with white-matter abnormalities, sometimes overlapping neurodegeneration with brain iron accumulation (the entity is also called **fatty acid hydroxylase-associated neurodegeneration, FAHN**) ([PMC6238570](https://ncbi.nlm.nih.gov/pmc/articles/PMC6238570); [PubMed 38353247](https://pubmed.ncbi.nlm.nih.gov/38353247/)).
6. **AP-4 vesicular sorting (SPG47/50/51/52 axis).** Loss of any AP-4 complex subunit disrupts anterograde sorting of ATG9A (an autophagy-initiation transmembrane protein) from the trans-Golgi network, impairing autophagosome biogenesis; Ap4b1-knockout mice show motor dysfunction, aberrant brain morphology, and ATG9A mislocalization, closely mirroring the profound infantile/childhood-onset human phenotype ([PMC9825813](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9825813/)).
7. **Non-cell-autonomous glial mechanism.** Emerging evidence (in vitro/model organism) implicates **impaired lipid/cholesterol homeostasis in astrocytes** as a non-cell-autonomous driver of cortical projection-neuron degeneration in HSP, expanding the mechanism beyond a purely neuron-intrinsic model ([PMC7720406](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7720406/)).
8. **Lipid metabolism broadly.** A dedicated review ("Lipids in the Physiopathology of Hereditary Spastic Paraplegias") frames disrupted lipid/membrane metabolism (cholesterol, sphingolipids, phospholipids) as a unifying downstream theme across many complex-HSP genes ([PMC7059351](https://pmc.ncbi.nlm.nih.gov/articles/PMC7059351/)).

**Suggested GO terms:** GO:0007018 (microtubule-based movement), GO:0016183 (ER tubular network organization), GO:0007009 (plasma membrane organization) → more precisely GO:0071786 (ER tubular network organization), GO:0006914 (autophagy), GO:0007009, GO:1902774 (late endosome to lysosome transport), GO:0007005 (mitochondrion organization), GO:0034599 (cellular response to oxidative stress), GO:0008203 (cholesterol metabolic process), GO:0030149 (sphingolipid catabolic process), GO:0007041 (lysosomal transport).

**Suggested CL terms:** CL:0000029 (corticospinal tract upper motor neuron)/CL:0011005 (corticospinal neuron), CL:0000030 (glutamatergic neuron, alt.), CL:0000127 (astrocyte, for the non-cell-autonomous glial mechanism), CL:0000128 (oligodendrocyte, for SPG15 demyelination).

**Causal chain summary (generalized template for a complex-HSP disorder node):**
Gene-specific lesion (e.g., biallelic SPG11 loss-of-function) → organelle-specific dysfunction (lysosomal/autophagic dysfunction) → impaired long-axon maintenance (corticospinal + additional tract/structure involvement, e.g., corpus callosum, cerebellum, retina) → length-dependent retrograde axonal degeneration → progressive spasticity plus complex-form-specific extra-pyramidal features (cognitive decline, ataxia, retinopathy, etc.).

---

## 7. Anatomical Structures Affected

**Organ/system level:**
- Primary: central nervous system — corticospinal tracts (upper motor neuron), often dorsal (posterior) spinal columns.
- Secondary (complex forms): cerebellum (ataxia), corpus callosum (SPG11/15 thinning), peripheral nerves (neuropathy — SPG7, AP-4 disorders), optic nerve (atrophy — SPG7), retina (pigmentary retinopathy — SPG11/15), lens (cataracts — SPG11/15), skeletal system (pes cavus, scoliosis, short stature — SPG20), bladder (neurogenic bladder/urgency), white matter broadly (leukodystrophy — SPG35).

**Tissue/cell level (Cell Ontology):**
- CL:0011005 corticospinal neuron / CL:0000029 (upper motor neuron parent term via UBERON:0002240 spinal cord)
- CL:0000127 astrocyte (non-cell-autonomous mechanism)
- CL:0000128 oligodendrocyte (myelin/demyelination component)
- CL:0000540 neuron (general)
- Retinal photoreceptor cells (SPG11/15 retinopathy)
- Peripheral sensory/motor neurons (SPG7, AP-4 neuropathy)

**Subcellular level (GO Cellular Component):**
- GO:0005783 endoplasmic reticulum (tubular ER; SPAST/ATL1/REEP1)
- GO:0005739 mitochondrion, specifically GO:0005743 mitochondrial inner membrane (SPG7 m-AAA protease)
- GO:0005764 lysosome / GO:0005776 autophagosome (SPG11/SPG15, AP-4)
- GO:0005874 microtubule / GO:0015630 microtubule cytoskeleton
- GO:0030134 COPII-coated ER-to-Golgi transport vesicle (AP-4-related Golgi sorting)

**Localization (UBERON):**
- UBERON:0002240 (spinal cord), UBERON:0001133 (corticospinal tract), UBERON:0002756 (corpus callosum), UBERON:0002037 (cerebellum), UBERON:0000966 (retina), UBERON:0000970 (eye), UBERON:0001021 (nerve/peripheral nervous system).
- Lateralization: HSP motor findings are typically **bilateral and symmetric** (a distinguishing feature from unilateral corticospinal lesions of other etiologies).

---

## 8. Temporal Development

**Onset:** Ranges continuously from congenital/infantile (AP-4-HSP: global developmental delay from infancy) through childhood (SPG11 median onset in the first two decades; SPG35 childhood-onset with seizures/leukodystrophy) to adult-onset (SPG4, SPG7 — onset can occur "as late as age 72 years" for SPG7) ([PMC8793673](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8793673/)). Mean HSP onset across pooled cohorts ≈ 24 years ([PMC8944001](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8944001/)). SPG5A median onset ~13 years (range 1–63) ([Elsevier](https://www.elsevier.es/en-revista-neurologia-english-edition--495-articulo-hereditary-spastic-paraparesis-due-spg5-cyp7b1-S2173580823000603)).

**Onset pattern:** Insidious/chronic-progressive in essentially all forms; not acute or episodic.

**Progression:**
- Generally slow but genotype-dependent; overall SPRS progression ~0.9 points/year pooled, but **1.3 points/year in complicated HSP vs. 0.6 points/year in pure HSP** ([Springer 2025](https://link.springer.com/article/10.1007/s00415-025-13606-y)).
- SPG11 carries higher severity and a more rapid course, with "limited lifespan of 3 to 4 decades after disease-onset" reported in some cohorts and rapid deterioration described in Dutch SPG11 cohorts ([PMC3798836](https://pmc.ncbi.nlm.nih.gov/articles/PMC3798836/)).
- Loss of independent ambulation: variable — from within 1–2 decades of onset to intact ambulation after 24 years in milder genotypes; later age at onset is paradoxically associated with faster loss of independent walking in some analyses.
- SPG3A tends to progress more slowly than SPG4.
- AP-4-HSP: children who achieve independent walking typically lose this ability months to a few years later as hypotonia converts to hypertonia/spasticity ([Boston Children's Hospital](https://www.childrenshospital.org/conditions-treatments/ap-4-associated-hereditary-spastic-paraplegia)).

**Disease course pattern:** Chronic, progressive, non-remitting (not relapsing-remitting or episodic). No spontaneous-remission pattern is described.

**Critical periods:** For the AP-4 disorders and other infantile-onset complex forms, early diagnosis is critical because gene-therapy intervention windows are being defined pre-symptomatically or in very early disease (see Section 12) — the SPG50 trial specifically dosed a pre-symptomatic 5-month-old alongside symptomatic children to test whether earlier intervention alters outcome ([CGTlive](https://www.cgtlive.com/view/spg50-gene-therapy-warrants-further-study)).

---

## 9. Inheritance and Population

**Epidemiology:**
- Pooled global HSP prevalence estimates: **2–7.4/100,000** across most populations, with a range of 0.1–9.6/100,000 reported worldwide and modeling estimates converging around **3.6/100,000** overall ([PMC8944001](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8944001/)).
- Genotype-specific global prevalence estimates: **SPG4 ≈ 0.90/100,000; SPG7 ≈ 0.22/100,000; SPG11 ≈ 0.34/100,000; SPG15 ≈ 0.13/100,000** ([BMC Neurology, Springer](https://link.springer.com/article/10.1186/s12883-022-02595-4)).
- Norway (population >2.5M): prevalence 7.4/100,000 (2009 study) — among the highest reported.
- Spain: ~2.24/100,000 (lower).
- Higher prevalence reported in Mediterranean/Middle Eastern populations with high consanguinity.
- Incidence in England/Northern Ireland rose from 0.12/100,000 person-years (2000) to 0.29/100,000 person-years (2021) ([PMC12210554](https://pmc.ncbi.nlm.nih.gov/articles/PMC12210554/)) — likely reflecting improved genetic diagnosis rather than true incidence increase.

**Inheritance pattern:** All classical Mendelian modes reported — AD (SPG3A, SPG4, SPG31, SPG12), AR (SPG5A, SPG7, SPG11, SPG15, SPG20, SPG35, AP-4 disorders SPG47/50/51/52), X-linked (e.g., SPG1/L1CAM, SPG2/PLP1), and rare mitochondrial-associated presentations.

**Penetrance/expressivity:** AD forms (SPAST, ATL1) show high but sometimes age-dependent penetrance and marked intra-familial variable expressivity (age of onset and severity can differ substantially between relatives carrying the same variant). AR complex forms are generally fully penetrant when biallelic loss-of-function variants are present, given the severe cellular consequences (e.g., near-complete loss of AP-4 complex function).

**Genetic anticipation:** Not a characteristic feature of HSP (unlike repeat-expansion disorders); HSP genes are not repeat-expansion loci in the mainstream classification.

**Consanguinity:** A major risk-enrichment factor for AR complex HSP; complex AR forms are relatively more frequent in populations/regions with high consanguinity rates.

**Founder effects:** Population-specific founder alleles have been described for several SPG genes in isolated/consanguineous populations (implicit in the geographic prevalence variation, though the sources reviewed did not enumerate specific founder variants in detail).

**Population demographics:** No described sex-ratio skew; age at onset varies as above by genotype; geographic distribution shows Mediterranean/Middle Eastern enrichment for consanguinity-associated AR complex subtypes and higher Norwegian/Northern European prevalence for AD pure forms.

---

## 10. Diagnostics

**Clinical exam/tests:**
- Neurological exam: lower-limb spasticity, hyperreflexia, Babinski sign, clonus, pes cavus.
- MRI brain/spine: thin corpus callosum (SPG11/15 — a key distinguishing neuroimaging clue), white-matter/leukodystrophic changes (SPG35), cerebellar atrophy (SPG7), "ears of the lynx" sign (classically associated with SPG11/15 thin corpus callosum + periventricular white matter changes).
- Ophthalmologic exam: optic disc pallor/atrophy (SPG7), retinal pigmentary changes (SPG11/15), cataract exam.
- Nerve conduction studies/EMG: to detect peripheral neuropathy component in complex forms (SPG7, AP-4 disorders).
- Urodynamic studies for neurogenic bladder assessment.
- Biochemical: elevated serum/CSF 25- and 27-hydroxycholesterol as a diagnostic/monitoring biomarker specific to SPG5A/CYP7B1 ([ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0022510X20305475)).

**Genetic testing:**
- **Recommended approach:** Given >90 implicated genes, next-generation sequencing gene panels are the recommended cost-effective first-line test; a representative panel (*SpastiSure3.0*) covers 118 HSP-associated genes.
- **Diagnostic yield:** Overall genetic diagnosis achieved in ~29–31% of clinically suspected pediatric HSP cohorts using panel testing; yield rises with age-stratified analysis (up to 37% in ages 0–5 when panel is followed by exome) ([Human Genomics, Springer](https://link.springer.com/article/10.1186/s40246-026-00935-w)). Diagnostic rate is markedly inheritance-pattern-dependent: **56.7% in AD HSP, 55.5% in AR HSP, but only 21.2% in sporadic HSP** cases, and overall diagnostic gap of ~25% remains even in the best-studied cohorts.
- **Whole exome sequencing (WES):** Recommended when panel testing is negative, particularly for complicated/complex phenotypes; "exome sequencing is a useful diagnostic tool for complicated forms of hereditary spastic paraplegia" ([PubMed 23438842](https://pubmed.ncbi.nlm.nih.gov/23438842/)); WES clearly benefits children with suspected HSP when panels are non-diagnostic ([PMC13040777](https://pmc.ncbi.nlm.nih.gov/articles/PMC13040777/)).
- Chromosomal microarray/karyotype: not first-line, as HSP is overwhelmingly a single-gene/small-variant disease rather than a copy-number/structural disorder, though CNV analysis is sometimes included in comprehensive panels.

**Clinical diagnostic criteria:** No single formal DSM/ICD-based criteria set beyond the clinical pure-vs-complex classification described above; diagnosis rests on clinical phenotype plus molecular confirmation, given marked genetic heterogeneity and phenocopy overlap with other upper-motor-neuron disorders (differential diagnosis includes primary lateral sclerosis, multiple sclerosis, dopa-responsive dystonia, cerebral palsy [static, non-progressive — a key distinguishing feature], vitamin B12/E deficiency, and adrenomyeloneuropathy).

**Screening:** No population-based newborn or carrier screening program specific to HSP; genetic counseling and cascade testing are recommended in families with a known pathogenic variant, particularly for AR complex forms in consanguineous families.

---

## 11. Outcome/Prognosis

**Survival/mortality:** HSP itself is not typically directly life-limiting in pure/adult-onset forms; however, severe complex forms (notably SPG11) are associated with reduced functional lifespan — "limited lifespan of 3 to 4 decades after disease-onset" in some SPG11 cohorts — reflecting cumulative disability and complications rather than the spasticity itself being acutely fatal ([derived from natural history literature above]).

**Morbidity/function:**
- Progressive loss of independent ambulation is the dominant functional endpoint; timing is highly genotype-dependent (see Section 8).
- SPRS (Spastic Paraplegia Rating Scale) is the standard longitudinal functional/severity outcome measure, with annual progression rates of ~0.6 (pure) to ~1.3 (complicated) points/year.
- Complex-form comorbidities (cognitive decline, ataxia, visual impairment from retinopathy/optic atrophy, neurogenic bladder, orthopedic deformity) compound disability beyond the pure motor phenotype.
- Increased burden of common mental health outcomes (anxiety, depression) documented in a large England/Northern Ireland epidemiologic cohort of HSP patients ([PMC12210554](https://pmc.ncbi.nlm.nih.gov/articles/PMC12210554/)).

**Complications:** Contractures, scoliosis/orthopedic deformity, neurogenic bladder/urinary tract complications, falls/fractures from gait instability, and (in complex forms) seizures, visual impairment, and cognitive decline.

**Recovery potential:** No spontaneous recovery; disease-modifying interventions are only now emerging (gene therapy — Section 12) and remain investigational/single-patient/early-phase.

**Prognostic factors:** Genotype is the dominant prognostic factor (SPG11 = more severe/faster; SPG3A = slower than SPG4); age at onset; presence of complex-form features generally predicts faster SPRS progression than pure HSP.

---

## 12. Treatment

**Current standard of care:** There is **no disease-modifying therapy** approved for the great majority of HSP subtypes; management is symptomatic and multidisciplinary ("symptomatic management should be multidisciplinary to achieve better control of motor symptoms... and prevent skeletal deformities") ([Merck Manual](https://www.merckmanuals.com/professional/neurologic-disorders/spinal-cord-disorders/hereditary-spastic-paraplegia); [PMC10858081](https://pmc.ncbi.nlm.nih.gov/articles/PMC10858081/)).

**Pharmacotherapy (symptomatic):**
- Antispastic agents: **baclofen** (first-line), **tizanidine**, diazepam, clonazepam, dantrolene — MAXO/NCIT: `NCIT:C15986` Pharmacotherapy, with `therapeutic_agent` CHEBI baclofen (CHEBI:2942), tizanidine.
- **Botulinum toxin type A/B** (BTX-A/BTX-B) — intramuscular injection for focal spasticity; reduces spasticity and fatigue without affecting depression/excessive daytime sleepiness; combined BTX + intensive physiotherapy shows added benefit ([PMC7046620](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7046620/); recent comprehensive 2025 review, [PMC12567745](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12567745/)). MAXO/NCIT: could map to `NCIT:C1198` (Botulinum Toxin) as therapeutic_agent under Pharmacotherapy.
- **Oxybutynin** for urinary urgency/neurogenic bladder.
- Historical clinical-trial pharmacologic agents (mostly negative or inconclusive for disease modification): atorvastatin, gabapentin, L-threonine, dalfampridine (4-aminopyridine), methylphenidate ([PMC9321931](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9321931/)).
- **SPG5A/CYP7B1-specific:** atorvastatin + chenodeoxycholic acid (± resveratrol) trialed to normalize elevated 25-/27-hydroxycholesterol and restore bile-acid profile; a randomized controlled trial (Schöls et al., *Brain* 2017, PMID 29126212) found atorvastatin reduced serum 27-OHC/25-OHC (though CSF 27-OHC reduction was not significant) ([PubMed 29126212](https://pubmed.ncbi.nlm.nih.gov/29126212/)).

**Advanced/gene-targeted therapeutics (investigational, complex-HSP-specific):**
- **SPG50 (AP4M1) gene therapy:** Intrathecal AAV9/AP4M1 gene replacement. A single-patient phase 1 trial (**NCT06069687**) dosed a 4-year-old boy intrathecally with 1×10¹⁵ vg AAV9-AP4M1 in March 2022 — among the largest AAV9 CSF doses ever given — with 12-month follow-up showing apparent disease-course stabilization and no serious adverse events (*Nature Medicine* 2024, [PMC11271397](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11271397/)). Elpida Therapeutics' "Melpida" program (**NCT05518188**, Phase I/II) has since dosed additional participants (ages 3–5 years at 1×10�1⁵ vg; a pre-symptomatic 5-month-old at 4×10¹⁴ vg), with FDA clearance to proceed to a **Phase III** trial (8 children, initiated August 2024) ([Clinical Trials Arena](https://www.clinicaltrialsarena.com/news/elpida-gene-therapy-phaseiii-trial-spg50/); [CGTlive](https://www.cgtlive.com/view/spg50-gene-therapy-warrants-further-study)). Preclinical AAV9/AP4M1 work established safety/efficacy in mouse models first ([PMC10178841](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10178841/)).
- **SPG47 (AP4B1) gene therapy:** Preclinical AAV9-hAP4B1 delivered into the cisterna magna in a mouse model, with "restoration of various hallmarks of disease" ([PMC11554807](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11554807/)); patient-advocacy-driven programs coordinated via Cure AP-4/Cure SPG47 foundations.
- **SPG5 (CYP7B1) gene therapy:** AAV8-based gene-replacement therapy in preclinical development ([PMC12309954](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12309954/)); an mRNA-based therapeutic strategy for SPG5 has also been proposed (*Molecular Therapy Methods & Clinical Development*, [Cell.com](https://www.cell.com/molecular-therapy-family/methods/fulltext/S2329-0501(19)30119-6)).
- Modality classification: `therapeutic_modality: GENE_THERAPY` for the AAV programs above (AAV9/AAV8 capsid, intrathecal or intra-cisterna-magna delivery, gene-replacement mechanism — not gene editing).

**Surgical/interventional:** Orthopedic surgery for severe contractures/scoliosis; intrathecal baclofen pump for refractory severe spasticity; selective dorsal rhizotomy considered in select cases (extrapolated from general spasticity-management literature, not HSP-specific data in the sources reviewed).

**Supportive/rehabilitative:**
- Physical therapy/exercise: maintains mobility, muscle strength, range of motion, reduces fatigue and spasms (`MAXO:0000011` physical therapy) — non-pharmacological systematic review (2023) supports benefit ([PMC10858081](https://pmc.ncbi.nlm.nih.gov/articles/PMC10858081/); [Springer](https://link.springer.com/article/10.1007/s10072-023-07200-1)).
- Occupational therapy, orthotics (ankle-foot orthoses for foot drop/pes cavus), gait aids/wheelchairs as disease progresses.
- Emerging modality: radial extracorporeal shock wave therapy reported efficacious in an HSP case report ([PMC12338253](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12338253/)).

**Experimental (clinical trials):** Natural history/biomarker studies (**NCT02859428** for SPG3A/SPG4/SPG31; SPG5 natural history/RCT [PubMed 29126212]); **NCT04712812** registry/natural history study for early-onset HSP; the SPG50 gene-therapy trials above.

**Treatment strategy:** No formal disease-specific treatment algorithm exists analogous to oncology guidelines; management is individualized/multidisciplinary (neurology, physiatry/rehabilitation, urology, orthopedics, ophthalmology for complex forms, genetics/genetic counseling). Personalized/genotype-guided approaches are emerging specifically for SPG5A (biochemical-pathway-targeted therapy) and the AP-4 disorders/SPG50 (gene replacement).

---

## 13. Prevention

**Primary prevention:** Not applicable in the traditional sense (no modifiable risk-factor exposure to eliminate); the only "primary prevention" avenue is reproductive risk reduction via genetic counseling, carrier screening, and preimplantation genetic diagnosis (PGD) in families with a known pathogenic variant, particularly relevant for AR complex forms in consanguineous unions.

**Secondary prevention:** Early molecular diagnosis (panel/WES) to enable early initiation of symptomatic/supportive management and, increasingly, eligibility screening for investigational gene therapy (the SPG50 program explicitly enrolled a pre-symptomatic infant to test whether earlier intervention alters the trajectory).

**Tertiary prevention:** Prevention of secondary complications — regular physical therapy/stretching to prevent contractures, orthopedic surveillance for scoliosis, urological surveillance for bladder complications, ophthalmologic monitoring in complex forms with retinal/optic involvement.

**Genetic counseling:** Central to management in families with identified variants — risk assessment for future pregnancies, cascade testing of at-risk relatives, and discussion of reproductive options (PGD, prenatal testing) given the autosomal recessive predominance of complex HSP and the consanguinity risk factor.

**Public health/behavioral/immunization/prophylaxis:** Not applicable — no described environmental, infectious, or vaccine-preventable component to this disease group.

---

## 14. Other Species / Natural Disease

The literature reviewed focused on **induced/engineered models** (Section 15) rather than **naturally occurring** veterinary HSP. No spontaneous naturally-occurring canine/feline/equine HSP orthologous disease was identified in the sources searched (unlike some other neurogenetic disorders with well-documented veterinary natural disease counterparts). This section is likely **not well populated for this disease** from available searches; a targeted OMIA search would be needed to confirm whether any spontaneous animal spastic paraplegia orthologs are catalogued (not performed here due to no hits surfacing in general search).

**Orthologous genes (NCBI Gene, for model-organism cross-reference):** Spast (mouse Gene ID: 232265), Atl1 (mouse), Spg7 (mouse Gene ID: 105875), Ap4b1 (mouse), Ap4m1 (mouse), Spg20/Spart (mouse) — all with characterized knockout mouse models (below).

---

## 15. Model Organisms

**Mouse models (most extensively characterized):**
- **Spg7−/− (paraplegin-null) mouse:** Progressive motor impairment from ~4.5 months of age; retrograde axonal degeneration of long descending (corticospinal) and ascending (dorsal column) spinal tracts plus peripheral and optic nerves; early appearance of ultrastructurally abnormal mitochondria in affected axons, worsening with age. Explicitly stated to **"successfully recapitulate the key phenotypic and pathological features observed in SPG7 patients"** ([PMC5628248](https://pmc.ncbi.nlm.nih.gov/articles/PMC5628248/) synthesis; [PMC7469654](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7469654/)).
- **Ap4b1-knockout mouse (SPG47 model):** Motor dysfunction, aberrant brain morphology, and ATG9A mislocalization, providing mechanistic and preclinical-therapeutic validation for the AAV9-hAP4B1 gene-therapy program ([PMC9825813](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9825813/)).
- **Spg20−/− mouse (Troyer syndrome model):** Reveals multimodal spartin functions in lipid-droplet maintenance, cytokinesis, and BMP signaling — expanding the mechanistic understanding of spartin beyond a single pathway ([PMC3406757](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3406757/)).
- SPG50 preclinical AAV9/AP4M1 efficacy studies were conducted in a corresponding **Ap4m1** mouse model prior to human dosing ([PMC10178841](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10178841/)).

**Zebrafish models:**
- **Spastizin (SPG15/ZFYVE26) zebrafish model:** Shows axon demyelination and degeneration, extending the disease-relevant phenotype into a myelin-dysfunction axis not previously emphasized in mammalian models — a 2024 bioRxiv/PMC study ([PMC11539067](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11539067/)).

**Cellular/iPSC and patient-derived models:**
- Patient-derived fibroblasts (SPG11, SPG15) show autophagosome accumulation and enlarged lysosomes, directly demonstrating defective autophagosome-lysosome fusion in a human cellular context ([PMC4078876](https://pmc.ncbi.nlm.nih.gov/articles/PMC4078876/)).
- iPSC-derived neuronal models comparing **SPG7 vs. SPAST patient-derived stem cells** show that mitochondrial functional deficits are specific to SPG7, not SPAST, patient cells — an important cross-genotype mechanistic distinction (title: "Mitochondrial Function in Hereditary Spastic Paraplegia: Deficits in SPG7 but Not SPAST Patient-Derived Stem Cells") ([PMC7469654](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7469654/)).
- Patient-derived fibroblasts were also used directly for translational validation of AAV2/AP4M1 gene-therapy vectors prior to the human SPG50 trial (phenotypic rescue demonstrated in vitro).

**Model limitations:** Mouse Spg7 and Ap4b1 knockouts recapitulate core motor/axonal-degeneration phenotypes reasonably well, but full complex-HSP multisystem features (e.g., human-specific cognitive/retinal phenotypes in SPG11/15) are less completely captured in rodent models — this is consistent with the general caveat that mouse CNS models often under-represent human-specific cortical/cognitive phenotypes. Zebrafish models add a demyelination phenotype not otherwise emphasized in mouse data, suggesting species-dependent phenotypic emphasis.

**Applications:** These models have been directly used for (a) mechanistic dissection of the axonal-transport/ER/mitochondrial/lysosomal/autophagy pathways described in Section 6, and (b) as the essential preclinical efficacy/safety platform for the AAV gene-therapy programs now in human trials for SPG47 and SPG50.

---

## Summary Table: Suggested Ontology Terms for KB Curation

| Category | Suggested terms |
|---|---|
| MONDO (subtype-level; no single "complex HSP" term) | MONDO:0008438 (AD group), MONDO:0010046 (SPG23), MONDO:0013342 (SPG48) — plus individual per-subtype MONDO IDs |
| HP (phenotypes) | HP:0002061 (spastic paraplegia), HP:0001347 (hyperreflexia), HP:0003487 (Babinski sign), HP:0002839 (bladder dysfunction), HP:0001761 (pes cavus), HP:0033725 (thin corpus callosum), HP:0001249 (intellectual disability), HP:0001251 (ataxia), HP:0000648 (optic atrophy), HP:0000580 (pigmentary retinopathy), HP:0000518 (cataract), HP:0002548 (parkinsonism), HP:0003693 (distal amyotrophy), HP:0004322 (short stature), HP:0001250 (seizure), HP:0002171 (leukoencephalopathy) |
| GO (biological process) | GO:0071786 (ER tubular network organization), GO:0006914 (autophagy), GO:1902774 (late endosome to lysosome transport), GO:0007005 (mitochondrion organization), GO:0008203 (cholesterol metabolic process), GO:0030149 (sphingolipid catabolic process), GO:0007018 (microtubule-based movement) |
| CL (cell types) | CL:0011005 (corticospinal neuron), CL:0000127 (astrocyte), CL:0000128 (oligodendrocyte) |
| GENO/HGNC (genes) | SPAST hgnc:11233, ATL1 hgnc:30288, REEP1 hgnc:13703, SPG11 hgnc:11226, ZFYVE26 hgnc:29128, SPG7 hgnc:11237, CYP7B1 hgnc:2652, FA2H hgnc:20139, SPART hgnc:11227, AP4B1 hgnc:567, AP4M1 hgnc:569, AP4E1 hgnc:568, AP4S1 hgnc:571 |
| MAXO/NCIT (treatment) | MAXO:0000011 (physical therapy), NCIT:C15986 (Pharmacotherapy) + therapeutic_agent (baclofen, tizanidine, botulinum toxin, atorvastatin, chenodeoxycholic acid) |
| Therapeutic modality | GENE_THERAPY (AAV9/AAV8 replacement — SPG47, SPG50, SPG5) |

---

## Sources

- [Genetic and phenotypic characterization of complex hereditary spastic paraplegia (PMC4939695)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4939695/)
- [Insights into Clinical, Genetic, and Pathological Aspects of HSP: A Comprehensive Overview (PMC8662366)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8662366/)
- [A complex form of HSP harboring p.W1515* in SPG11 (PMC8749458)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8749458/)
- [Hereditary Spastic Paraplegia: An Update (PMC8835766)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8835766/)
- [AP-4-Associated HSP – GeneReviews (NBK535153)](https://www.ncbi.nlm.nih.gov/books/NBK535153/)
- [Uncomplicated (Pure) HSP Overview – GeneReviews (NBK1509)](https://www.ncbi.nlm.nih.gov/books/NBK1509/)
- [Spastic Paraplegia 11 – GeneReviews (NBK1210)](https://www.ncbi.nlm.nih.gov/books/NBK1210/)
- [Hereditary Spastic Paraplegia: From Genes, Cells and Networks to Novel Pathways for Drug Discovery (PMC8004882)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8004882/)
- [Ascending Axonal Degeneration of the Corticospinal Tract in Pure HSP: DTI Study (PMC6827077)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6827077/)
- [Impaired lipid metabolism in astrocytes underlies degeneration of cortical projection neurons in HSP (PMC7720406)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7720406/)
- [Axon demyelination and degeneration in a zebrafish spastizin model of HSP (PMC11539067)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11539067/)
- [Lysosomal abnormalities in HSP types SPG15 and SPG11 (PMC4078876)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4078876/)
- [In Vivo Evidence for Lysosome Depletion and Impaired Autophagic Clearance in SPG11 (PMC4540459)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4540459/)
- [Janus-faced spatacsin (SPG11), Brain 2020](https://academic.oup.com/brain/article/143/8/2369/5827584)
- [Impaired mitochondrial dynamics underlie axonal defects in HSP (PMC6031053)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6031053/)
- [REEP1, spastin, atlastin-1 coordinate microtubule interactions with tubular ER network – PMID 20200447](https://pubmed.ncbi.nlm.nih.gov/20200447/) / [PMC2846052](https://pmc.ncbi.nlm.nih.gov/articles/PMC2846052/)
- [Global epidemiology of hereditary ataxia and spastic paraplegia – PMID 24603320](https://pubmed.ncbi.nlm.nih.gov/24603320/)
- [An integrated modelling methodology for estimating global incidence/prevalence of SPG4/7/11/15 (PMC8944001)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8944001/)
- [Epidemiology of HSP and mental health outcomes in England/N. Ireland (PMC12210554)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12210554/)
- [Natural history in HSP: Austrian cohort, J Neurol 2025 (PMC12835074)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12835074/)
- [Rapidly deteriorating course in Dutch SPG11 patients (PMC3798836)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3798836/)
- [HSP type 5: natural history, biomarkers, RCT – PMID 29126212](https://pubmed.ncbi.nlm.nih.gov/29126212/)
- [Cure AP-4 / Cure SPG47 Foundation](https://cureap4.org/)
- [Pre-clinical AP4B1 gene replacement therapy for SPG47 (PMC11554807)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11554807/)
- [Intrathecal AAV9/AP4M1 gene therapy for SPG50, preclinical (PMC10178841)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10178841/)
- [AAV gene therapy for HSP type 50: phase 1 single-patient trial, Nature Medicine (PMC11271397)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11271397/)
- [Elpida Therapeutics Phase III SPG50 trial announcement](https://www.clinicaltrialsarena.com/news/elpida-gene-therapy-phaseiii-trial-spg50/)
- [SPG50 Gene Therapy Warrants Further Study (CGTlive)](https://www.cgtlive.com/view/spg50-gene-therapy-warrants-further-study)
- [The Neuro-Ophthalmologic Manifestations of SPG7-Associated Disease (PMC12565430)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12565430/)
- [Impaired flickering of the permeability transition pore causes SPG7 spastic paraplegia (eBioMedicine)](https://www.thelancet.com/journals/ebiom/article/PIIS2352-3964(20)30426-6/fulltext)
- [Mitochondrial Function in HSP: Deficits in SPG7 but Not SPAST Patient-Derived Stem Cells (PMC7469654)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7469654/)
- [Ap4b1-knockout mouse model of SPG47 (PMC9825813)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9825813/)
- [Elevated hydroxycholesterols in Norwegian SPG5 patients](https://www.sciencedirect.com/science/article/pii/S0022510X20305475)
- [Sequence alterations within CYP7B1 – PMID 18252231](https://pubmed.ncbi.nlm.nih.gov/18252231/)
- [AAV8-based gene replacement therapy for HSP type 5 (PMC12309954)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12309954/)
- [mRNA as a Novel Treatment Strategy for HSP Type 5 (Cell.com)](https://www.cell.com/molecular-therapy-family/methods/fulltext/S2329-0501(19)30119-6)
- [Mutation of FA2H underlies SPG35 – PMID 20104589](https://pubmed.ncbi.nlm.nih.gov/20104589/)
- [HSP type 35 with novel FA2H mutation, literature review (PMC6238570)](https://ncbi.nlm.nih.gov/pmc/articles/PMC6238570)
- [SPG20/Spartin – Wikipedia synthesis](https://en.wikipedia.org/wiki/SPG20)
- [Spg20−/− mice reveal multimodal functions for spartin (PMC3406757)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3406757/)
- [Clinical-Genetic Features Influencing Disability in SPG4 (Neurology Genetics)](https://www.neurology.org/doi/10.1212/NXG.0000000000000664)
- [Children with suspected HSP benefit from whole exome analysis (Human Genomics, Springer)](https://link.springer.com/article/10.1186/s40246-026-00935-w)
- [Exome sequencing diagnostic tool for complicated HSP – PMID 23438842](https://pubmed.ncbi.nlm.nih.gov/23438842/)
- [Non-pharmacological treatment of HSP: systematic review (PMC10858081)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10858081/)
- [Botulinum Toxin Treatment in HSP — Comprehensive Review (PMC12567745)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12567745/)
- [Efficacy of combined botulinum toxin + intensive physiotherapy in HSP (PMC7046620)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7046620/)
- [The Puzzle of HSP: From Epidemiology to Treatment (PMC9321931)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9321931/)
- [Lipids in the Physiopathology of HSPs (PMC7059351)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7059351/)
- [Pharos: complex hereditary spastic paraplegia disease page](https://pharos.nih.gov/diseases/complex%20hereditary%20spastic%20paraplegia)
- [OMIM #182600 SPG3A](https://omim.org/entry/182600), [OMIM #270800 SPG5A](https://omim.org/entry/270800), [OMIM #604805 SPG12](https://omim.org/entry/604805)