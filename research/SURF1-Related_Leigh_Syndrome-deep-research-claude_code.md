---
provider: claude_code
model: claude-opus-4-8[1m]
cached: false
start_time: '2026-07-10T17:26:45.348520'
end_time: '2026-07-10T17:32:01.148081'
duration_seconds: 315.8
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: SURF1-Related Leigh Syndrome
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
  - claude-opus-4-8[1m]
  num_turns: 18
  total_cost_usd: 2.505911
  session_id: 501cf562-a643-4974-afbc-89be7e13233f
  stop_reason: end_turn
citation_count: 9
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** SURF1-Related Leigh Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **SURF1-Related Leigh Syndrome** covering all of the
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

I now have well-sourced material across discovery, clinical natural history, mechanism, and models. Writing the complete report inline.

---

# Comprehensive Research Report: SURF1-Related Leigh Syndrome

**Prepared:** July 2026 · **Category:** Mendelian (autosomal recessive, nuclear-encoded mitochondrial disease)

> **Attribution note:** Primary-literature claims below are drawn from articles retrieved via PubMed; each is cited with its PMID and a DOI link. Ontology identifiers (MONDO, HP, GO, CL, UBERON, CHEBI, MAXO) were verified against the Ontology Lookup Service (OLS4). Where a specific datum could not be sourced to a citable primary paper, this is stated explicitly.

---

## 1. Disease Information

**Overview.** SURF1-related Leigh syndrome is a severe, early-onset, progressive neurodegenerative disorder — the nuclear-gene prototype of **cytochrome *c* oxidase (COX / mitochondrial respiratory chain complex IV)–deficient Leigh syndrome**. Leigh syndrome itself (subacute necrotizing encephalomyelopathy) is defined by **bilaterally symmetrical necrotic lesions in the basal ganglia, thalamus, brainstem, and/or cerebellum**, typically with lactic acidemia and psychomotor regression. Biallelic loss-of-function variants in *SURF1* — which encodes an assembly factor for complex IV — are **the single most frequent nuclear cause of COX-deficient Leigh syndrome**.

- According to PubMed, Zhu et al. (1998) established the gene: *"Analysis of a candidate gene (SURF1) of unknown function revealed several mutations, all of which predict a truncated protein… These data suggest a role for SURF1 in the biogenesis of the COX complex and define a new class of gene defects causing human neurodegenerative disease."* (PMID **9843204**, [DOI](https://doi.org/10.1038/3804)).
- Wedatilake et al. (2013) frame the entity: *"SURF1 deficiency, a monogenic mitochondrial disorder, is the most frequent cause of cytochrome c oxidase (COX) deficient Leigh syndrome (LS)."* (PMID **23829769**, [DOI](https://doi.org/10.1186/1750-1172-8-96)).

**Key identifiers.**
| Resource | Identifier |
|---|---|
| **MONDO** | **MONDO:0009723** (Leigh syndrome; broad). SURF1 form is captured in OMIM/Orphanet as the COX-deficient nuclear subtype. |
| **OMIM (phenotype)** | **256000** (LEIGH SYNDROME); the SURF1-specific phenotype is now curated as **220110** — *Mitochondrial complex IV deficiency, nuclear type 1 (MC4DN1)*. |
| **OMIM (gene)** | ***SURF1*, 185620** |
| **Orphanet** | **ORPHA:506** (Leigh syndrome); **ORPHA:255210** (mtDNA-associated LS, for contrast) |
| **ICD-10 / ICD-11** | ICD-10 **G31.82** (Leigh's disease); ICD-11 **8C72.0** / 5C53 metabolic grouping |
| **MeSH** | **D007888** (Leigh Disease); **D030401** (Cytochrome-c Oxidase Deficiency) |
| **DOID** | **DOID:3652** (Leigh disease) |
| **NCIT / SNOMED CT** | NCIT **C84814**; SNOMED **29570005** |
| **HGNC** | *SURF1* HGNC:**11474**; NCBI Gene **6834**; UniProt **Q15526** |

**Synonyms / alternative names.** SURF1 deficiency; COX-deficient Leigh syndrome, SURF1 type; Leigh syndrome due to COX deficiency (nuclear type 1); Mitochondrial complex IV deficiency nuclear type 1 (MC4DN1); Surfeit-1 assembly-factor deficiency. Historical umbrella term for Leigh syndrome: *subacute necrotizing encephalomyelopathy* (SNE).

**Data derivation.** Information is aggregated at the **disease level** from OMIM/Orphanet/GeneReviews plus published clinical cohorts and case series (e.g., the 44-patient multicentre natural history study, PMID 23829769), not from individual EHR records.

---

## 2. Etiology

**Primary cause (genetic).** Biallelic (homozygous or compound heterozygous) **loss-of-function variants in *SURF1*** (9q34.2). SURF1 is a mitochondrial inner-membrane protein required for the biogenesis/assembly of complex IV; its loss produces a profound, generalized COX deficiency. Nearly all reported pathogenic *SURF1* alleles are truncating (frameshift, nonsense, splice), predicting an absent or non-functional protein — *"All reported SURF1 mutations are loss of function, predicting a truncated protein (hSurf1) product… no protein in LS patient cells."* (Yao & Shoubridge 1999, PMID **10556303**, [DOI](https://doi.org/10.1093/hmg/8.13.2541)).

**Genetic risk factors.**
- *Causal locus:* *SURF1* (the disease is monogenic; the variant *is* the cause, not a susceptibility allele).
- *Founder/recurrent alleles:* the recurrent **c.312_321del10insAT** (exon 4) is the single most common allele — *"The most frequent mutation was 312_321del 311_312insAT which was found in 12 patients out of 40."* (Péquignot et al. 2001, PMID **11317352**, [DOI](https://doi.org/10.1002/humu.1112)). The **c.845_846delCT** deletion is another recurrent allele.
- *Consanguinity* increases homozygous-allele risk (relevant in populations with high consanguinity, e.g., North African/Tunisian series — Maalej et al. 2018, PMID **29481804**, [DOI](https://doi.org/10.1016/j.bbrc.2018.02.169)).

**Environmental / modifying triggers.** As with Leigh syndrome generally, **catabolic stressors** — intercurrent febrile illness, infection, vaccination, fasting, surgery/anesthesia — commonly precipitate acute decompensation, developmental regression, and stepwise clinical deterioration. These are *triggers of crises*, not causes of the disease. No lifestyle or occupational exposure causes SURF1 deficiency.

**Protective factors.** None established genetically. Aggressive avoidance/treatment of catabolic triggers is the practical "protective" strategy. No validated protective allele or dietary factor exists.

**Gene–environment interaction.** The mismatch between a fixed genetic bioenergetic ceiling (severely reduced COX capacity) and fluctuating metabolic demand explains the episodic, stress-provoked crises superimposed on chronic progression — a recurrent theme across mitochondrial Leigh syndromes.

---

## 3. Phenotypes

The most authoritative frequency data come from the 44-patient multicentre SURF1 natural-history cohort (Wedatilake et al. 2013, PMID **23829769**, [DOI](https://doi.org/10.1186/1750-1172-8-96)), which reports a **homogeneous** phenotype. Direct quote of the symptom spectrum and frequencies:

> *"The majority of patients (32/44, 73%) presented in infancy (median 9.5 months). Frequent symptoms were poor weight gain (95%, median age 10 months), hypotonia (93%, median age 14 months), poor feeding/vomiting (89%, median age 10 months), developmental delay (88%, median age 14 months), developmental regression (71%, median age 19 months), movement disorder (52%, median age 24 months), oculomotor involvement (52%, median age 29 months) and central respiratory failure (78%, median age 31 months). Hypertrichosis (41%), optic atrophy (23%), encephalopathy (20%), seizures (14%) and cardiomyopathy (2%) were observed less frequently."*

| Phenotype | Type | Frequency (SURF1 cohort) | Onset (median) | HPO suggestion |
|---|---|---|---|---|
| Poor weight gain / failure to thrive | Physical/constitutional | 95% | 10 mo | **HP:0001508** (Failure to thrive) |
| Hypotonia | Neurological sign | 93% | 14 mo | **HP:0001252** |
| Poor feeding / vomiting | Symptom | 89% | 10 mo | **HP:0011968** (Feeding difficulties); **HP:0002013** (Vomiting) |
| Developmental delay | Neurodevelopmental | 88% | 14 mo | **HP:0001263** (Global developmental delay) |
| Developmental regression | Neurodegenerative | 71% | 19 mo | **HP:0002376** (Developmental regression) |
| Central respiratory failure / apnea | Life-threatening sign | 78% | 31 mo | **HP:0002871** (Central apnea); **HP:0002093** (Respiratory insufficiency) |
| Movement disorder (dystonia, ataxia) | Neurological sign | 52% | 24 mo | **HP:0001332** (Dystonia); **HP:0001251** (Ataxia) |
| Oculomotor involvement (ophthalmoparesis, nystagmus, ptosis) | Clinical sign | 52% | 29 mo | **HP:0000597** (Ophthalmoparesis); **HP:0000639** (Nystagmus); **HP:0000508** (Ptosis) |
| Hypertrichosis | Physical manifestation (SURF1-suggestive) | 41% | — | **HP:0000998** (Hypertrichosis) |
| Optic atrophy | Ophthalmological sign | 23% | — | **HP:0000648** (Optic atrophy) |
| Encephalopathy | Neurological | 20% | — | **HP:0001298** (Encephalopathy) |
| Seizures | Neurological | 14% | — | **HP:0001250** (Seizures) |
| Cardiomyopathy | Cardiac | 2% (rare in SURF1) | — | **HP:0001638** (Cardiomyopathy) |
| Lactic acidosis (blood/CSF) | Laboratory abnormality | Common (near-universal) | — | **HP:0003128** (Lactic acidosis / elevated lactate); **HP:0003567** (Increased CSF lactate) |
| Bilateral symmetric basal ganglia/brainstem lesions (MRI) | Imaging sign | Defining | — | **HP:0002451** (Basal ganglia gliosis); **HP:0007366** (Atrophy/degeneration affecting the basal ganglia) |
| Sensorimotor peripheral neuropathy | Neurological | Subset | — | **HP:0009830** (Peripheral neuropathy) |

**Characteristics.** Onset is **infantile** in ~73% (median 9.5 months), with the remainder in early childhood; rare later-onset/attenuated cases exist but are uncommon. Severity is **severe**; course is **chronic-progressive punctuated by acute, stress-triggered regressions**. **Hypertrichosis is a comparatively SURF1-specific clue** that helps distinguish it clinically from other Leigh genotypes; notably, **cardiomyopathy is characteristically rare in SURF1** (2%), unlike SCO2/other COX-assembly defects.

**Quality-of-life impact.** Progressive loss of motor and bulbar function leads to non-ambulation, dysphagia (tube feeding), communication loss, respiratory dependency, and recurrent hospitalizations — profound impairment across all domains, with QoL dominated by respiratory/feeding failure and neurological disability. No SURF1-specific validated QoL instrument exists; generic pediatric/mitochondrial disease measures (PedsQL, Newcastle Mitochondrial Disease Scale) are used.

---

## 4. Genetic / Molecular Information

**Causal gene.** ***SURF1*** (Surfeit locus protein 1), 9q34.2; HGNC:11474; OMIM *185620; UniProt Q15526; 9 exons; ~30 kDa mature inner-membrane protein with two transmembrane domains flanking an intermembrane-space loop.

**Pathogenic variants.**
- **Variant classes:** predominantly **truncating** — frameshift insertions/deletions, nonsense, and splice-site variants distributed across exons and introns. Péquignot et al. catalogued the spectrum: *"Twelve of the mutations were insertion/deletion mutations… 10 were missense/nonsense… and eight were detected at splicing sites in introns 3 to 7… To date, 30 different mutations have been reported in 40 unrelated patients."* (PMID **11317352**, [DOI](https://doi.org/10.1002/humu.1112)). >100 pathogenic alleles are now in ClinVar/HGMD.
- **Recurrent alleles:** **c.312_321del10insAT** (exon 4; the most common) and **c.845_846delCT** (exon 8).
- **Splice variants:** e.g., the Tunisian series reported a homozygous splice-site **c.516-517delAG** and novel intronic variants predicted to disrupt splicing (Maalej et al. 2018, PMID **29481804**, [DOI](https://doi.org/10.1016/j.bbrc.2018.02.169)).
- **ACMG classification:** truncating variants in this loss-of-function gene are typically **Pathogenic/Likely pathogenic** (PVS1-supported); rare missense/intronic variants may be VUS pending functional or splicing evidence.
- **Allele frequency:** individually **rare/absent** in gnomAD (consistent with a recessive, early-lethal disorder); carrier frequency is low in the general population.
- **Origin:** **germline**, autosomal recessive. **Functional consequence: loss of function** — absent/truncated protein → failure to assemble/maintain complex IV.

**Genotype–phenotype.** SURF1 disease is strikingly homogeneous regardless of the specific truncating alleles, consistent with a shared complete loss-of-function mechanism (PMID 23829769). Rare hypomorphic/partial-function alleles have been associated with milder or atypical presentations (e.g., Charcot–Marie–Tooth-like neuropathy or later onset), but these are exceptions.

**Modifier genes.** Not formally established; residual mitochondrial biogenesis capacity and unidentified nuclear modifiers are hypothesized to explain intrafamilial variability, but no validated modifier locus exists.

**Epigenetics / chromosomal abnormalities.** No recurrent epigenetic mechanism or large chromosomal rearrangement is characteristic; the disorder is a small-variant single-gene condition. (Deletions of 9q34 encompassing *SURF1* are theoretically possible but not a described common mechanism.)

---

## 5. Environmental Information

- **Environmental/toxic factors:** none cause the disease. Mitochondrial toxins/inhibitors of the respiratory chain are conceptually relevant to bioenergetic stress but are not etiological.
- **Lifestyle factors:** not applicable to disease causation; **avoidance of catabolic stress** (fasting, dehydration) is a management consideration. Certain drugs that stress mitochondrial function (e.g., valproate, high-dose propofol infusions, aminoglycosides) are used with caution.
- **Infectious agents:** none cause SURF1 deficiency, but **intercurrent infections are the leading precipitants of acute neurological/metabolic decompensation and death.**

---

## 6. Mechanism / Pathophysiology

**Core biochemical defect.** SURF1 is a **complex IV (cytochrome *c* oxidase) assembly factor**. Complex IV is the terminal oxidase of the electron transport chain, transferring electrons from reduced cytochrome *c* to O₂ and contributing to the proton-motive force that drives ATP synthesis. Shoubridge (2001) summarizes: *"Cytochrome c oxidase (COX) is the terminal enzyme of the mitochondrial respiratory chain… composed of 13 structural subunits… a large number of accessory factors are necessary for the assembly and maintenance of the active holoenzyme complex… Mutations have… been identified in several COX assembly factors: SURF1 (Leigh Syndrome)…"* (PMID **11579424**, [DOI](https://doi.org/10.1002/ajmg.1378)).

**Causal chain (upstream → downstream).**
1. **Biallelic *SURF1* LOF** → loss of the SURF1 assembly factor (upstream trigger).
2. **Failure of complex IV assembly/maintenance** → accumulation of early COX assembly intermediates and reduced steady-state levels of both nuclear- and mtDNA-encoded COX subunits. *"Steady-state levels of both nuclear- and mitochondrial-encoded COX subunits were also markedly reduced in patient cells, consistent with a failure to assemble or maintain a normal amount of the enzyme complex"* (Yao & Shoubridge 1999, PMID **10556303**, [DOI](https://doi.org/10.1093/hmg/8.13.2541)).
3. **Severe, generalized COX (complex IV) deficiency** → impaired terminal electron transport and oxidative phosphorylation. In patient fibroblasts there is *"accumulation of abundant COX1 assembly intermediates, low content of COX monomer and preferential recruitment of COX into I-III₂-IVn supercomplexes"* (Kovářová et al. 2016, PMID **26804654**, [DOI](https://doi.org/10.1016/j.bbadis.2016.01.007)).
4. **Deficient ATP synthesis + compensatory anaerobic glycolysis** → **lactic acidosis** (blood and CSF), the biochemical hallmark.
5. **Energy failure in high-oxidative-demand neurons** → oxidative stress, secondary excitotoxicity, and **necrotizing, capillary-proliferating spongiform lesions** in symmetric deep-gray/brainstem structures.
6. **Bilateral symmetric neurodegeneration** of basal ganglia, brainstem, and cerebellum → the Leigh clinical/imaging phenotype (regression, dystonia, oculomotor/bulbar/respiratory failure).

**Molecular pathways / processes (GO).** Oxidative phosphorylation (**GO:0006119**); mitochondrial respiratory chain **complex IV assembly (GO:0033617)**; **cytochrome-c oxidase activity (GO:0004129)**; ATP synthesis coupled electron transport (**GO:0042775**); aerobic respiration (**GO:0009060**); response to oxidative stress (**GO:0006979**); neuron apoptotic process (**GO:0051402**).

**Cellular processes.** Bioenergetic failure, oxidative stress, and neuronal/glial cell death (necrosis > apoptosis) with reactive astrogliosis and microvascular proliferation; disrupted respiratory supercomplex organization.

**Protein dysfunction.** Loss of an integral inner-membrane assembly chaperone; both transmembrane domains are required for function — *"insertion of both transmembrane domains in the intact protein is necessary for function"* (PMID 10556303). Truncated products fail to accumulate and cannot rescue COX activity.

**Metabolic changes.** Shift to glycolysis; elevated lactate/pyruvate; elevated CSF lactate; secondary alterations in TCA-cycle flux. Chemical entities: lactate/lactic acid (**CHEBI:24996**), pyruvate (**CHEBI:15361**), heme *a* (a COX prosthetic group), molecular oxygen (**CHEBI:15379**), ATP (**CHEBI:30616**), ubiquinone/CoQ10 (**CHEBI:46245**).

**Immune involvement.** Not primary; secondary neuroinflammatory/gliotic responses accompany the lesions.

**Tissue-damage mechanism.** Chronic oxidative-phosphorylation insufficiency → oxidative stress and energy crisis → focal necrosis in metabolically vulnerable CNS regions (subcortical gray, brainstem).

**Cell types (CL) / affected populations.** Neurons (**CL:0000540**), including brainstem and basal-ganglia neurons; astrocytes (**CL:0000127**); the pathology is neuron- and vascular-endothelium–involving with astrogliosis.

**Molecular profiling.** Muscle/fibroblast biochemistry shows **isolated complex IV deficiency** with normal complexes I/II/III; BN-PAGE shows loss of assembled COX with accumulation of subassemblies; histochemistry shows COX-negative fibers with preserved SDH. Species-specific note (see §15): human COX assembly is far more SURF1-dependent than mouse — *"COX assembly is much more dependent on SURF1 in humans than in mice"* (PMID 26804654).

---

## 7. Anatomical Structures Affected

**Organ level.** Primary: **central nervous system** (nervous system, **UBERON:0001016**). Secondary/systemic: skeletal muscle (biochemical COX deficiency, variable weakness), and — infrequently — heart. Respiratory failure is central (brainstem) rather than pulmonary-parenchymal.

**Neuroanatomical sites (UBERON).**
- **Basal ganglia (UBERON:0002420)** — putamen (**UBERON:0001874**), caudate, globus pallidus — bilaterally symmetric lesions.
- **Brainstem (UBERON:0002298)** — midbrain (**UBERON:0001891**), periaqueductal gray, tegmentum, medulla (respiratory nuclei).
- **Thalamus (UBERON:0001897)**, **substantia nigra (UBERON:0002038)**, **cerebellum (UBERON:0002037)**.
- **Optic nerve (UBERON:0000941)** — optic atrophy.
- Peripheral nerve and **skeletal muscle (UBERON:0001134)** — subset.

**Tissue/cell level.** Neuronal loss with relative astroglial preservation, capillary proliferation, demyelination, and spongiform necrosis; affected cells are principally **neurons (CL:0000540)** and reactive **astrocytes (CL:0000127)**.

**Subcellular level (GO cellular component).** **Mitochondrion (GO:0005739)**; **mitochondrial inner membrane (GO:0005743)** — the locus of SURF1 and complex IV; mitochondrial respiratory chain complex IV (**GO:0005751**).

**Localization / lateralization.** Characteristically **bilateral and symmetric** — a defining imaging feature of Leigh syndrome.

---

## 8. Temporal Development

- **Onset:** predominantly **infantile** (median 9.5 months; 73% present in infancy per PMID 23829769); typically **subacute**, frequently unmasked by an intercurrent illness. Some early-childhood and rare later/attenuated presentations occur.
- **Progression / course:** **chronic-progressive with acute, stress-triggered relapses** (developmental regression episodes). Stages: early hypotonia/feeding failure/developmental delay → regression and movement disorder → brainstem involvement with oculomotor and **central respiratory failure** (median 31 months) → respiratory failure/death.
- **Duration / prognosis:** progressive and life-limiting; central respiratory failure is the principal cause of death (see §11). Spontaneous remission does not occur; transient plateaus between crises are typical.
- **Critical periods:** infancy/early childhood are the windows of both peak vulnerability (rapid neurodegeneration) and greatest therapeutic/supportive opportunity; aggressive management of catabolic triggers is most impactful during this window.

---

## 9. Inheritance and Population

**Inheritance.** **Autosomal recessive** — *"Leigh syndrome (LS) associated with cytochrome c oxidase (COX) deficiency is an autosomal recessive neurodegenerative disorder caused by mutations in SURF1"* (PMID **10556303**, [DOI](https://doi.org/10.1093/hmg/8.13.2541)). HPO inheritance term: **HP:0000007** (Autosomal recessive inheritance). Penetrance is essentially complete for biallelic LOF; expressivity is relatively consistent (homogeneous phenotype). No genetic anticipation (not a repeat-expansion disorder). Germline mosaicism is not a characteristic feature. **Consanguinity** raises risk of homozygosity (relevant in consanguineous populations). Carrier frequency is low; recurrence risk for parents of an affected child is 25%.

**Epidemiology.** Leigh syndrome overall has a birth prevalence on the order of **~1 in 36,000–40,000** (classic population estimates ~1:34,000–1:40,000). SURF1 deficiency is the **most common nuclear/COX-deficiency cause** of Leigh syndrome, but is individually rare (Orphanet classifies Leigh syndrome as <1–9/100,000). Precise SURF1-specific incidence figures are not robustly established; the largest assembled clinical series is the 44-patient UK/Australian cohort (PMID 23829769). *No reliable disease-specific incidence per 100,000 is available in the primary literature — reported figures are extrapolations from Leigh-syndrome-wide surveys.*

**Population demographics.** Pan-ethnic. Certain recurrent alleles cluster in specific populations (e.g., North African/Middle Eastern consanguineous families). **Sex ratio ~1:1** (autosomal). Age distribution: overwhelmingly infants/young children.

---

## 10. Diagnostics

**Biochemical / laboratory.**
- **Elevated lactate** in blood and (especially) **CSF**, with elevated lactate:pyruvate ratio; LOINC lactate e.g. **LOINC:2524-7** (Lactate, plasma).
- **Isolated complex IV (COX) deficiency** on respiratory-chain enzymology in muscle/fibroblasts, with normal complexes I–III.
- **Muscle histochemistry:** COX-negative, SDH-positive fibers; **BN-PAGE:** reduced assembled complex IV with accumulated subassemblies.
- Fibroblast Western blot: absent SURF1 protein and reduced COX subunits (PMID 10556303).

**Imaging.** **Brain MRI** is central: **bilaterally symmetric T2/FLAIR hyperintense lesions in basal ganglia (putamen), thalamus, and brainstem**, sometimes with restricted diffusion acutely; **MR spectroscopy** shows a **lactate doublet**. This pattern in an infant is highly suggestive of Leigh syndrome.

**Genetic testing (definitive).**
- **First-line:** molecular genetic testing — **whole-exome / whole-genome sequencing** or a **mitochondrial/Leigh-syndrome nuclear gene panel** including *SURF1*; **single-gene *SURF1* sequencing** is reasonable when the COX-deficient Leigh phenotype (± hypertrichosis) points strongly to SURF1. Confirm **biallelic** pathogenic variants (deletion/duplication analysis if only one variant found; MLPA for exon-level CNV).
- **mtDNA testing** is used to exclude maternally-inherited Leigh syndrome (e.g., *MT-ATP6* m.8993T>G/T>C, MILS) — important in the differential.
- Prenatal/preimplantation testing is feasible once familial variants are known.

**Diagnostic criteria / differential.** Consensus Leigh-syndrome criteria: (1) progressive neurological disease with motor/intellectual regression; (2) characteristic bilateral symmetric basal-ganglia/brainstem lesions; (3) raised lactate (blood/CSF); ideally with a mitochondrial biochemical/genetic defect. **Differential diagnosis:** maternally-inherited Leigh syndrome (*MT-ATP6*, *MT-TL1*), complex I–deficient LS (nuclear, e.g., NDUFS genes — cf. Loeffen et al. 1998, PMID **9837812**, [DOI](https://doi.org/10.1086/302154)), *LRPPRC*-related French-Canadian LS, PDH deficiency, biotin-thiamine-responsive basal ganglia disease, and other organic acidemias/mitochondrial encephalopathies. The **LRPPRC** form is clinically distinct with acidotic crises — *"The Leigh syndrome of SLSJ-COX differs from that of SURF1-related COX deficiency"* (Debray et al. 2011, PMID **21266382**, [DOI](https://doi.org/10.1136/jmg.2010.081976)).

**Screening.** No population newborn screening exists (lactate/COX are not NBS analytes). **Cascade carrier testing** and **prenatal diagnosis** are offered to families with known variants.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** SURF1 deficiency is **life-limiting**, generally with death in infancy or childhood; **central respiratory failure is the leading cause of death** (78% develop it, median 31 months — PMID 23829769). Survival is variable but historically most patients die within the first years of life; some survive into later childhood/adolescence with intensive support.
- **Comparative prognosis:** SURF1 LS is severe but has a **different survival profile** from LRPPRC (French-Canadian) LS, which shows earlier/higher crisis-driven mortality — *"SLSJ-COX is distinct by the occurrence of metabolic crises, leading to earlier and higher mortality (p=0.001)"* compared with an assembled SURF1 group (Debray et al. 2011, PMID **21266382**, [DOI](https://doi.org/10.1136/jmg.2010.081976)).
- **Morbidity/disability:** progressive motor disability (dystonia, non-ambulation), bulbar dysfunction/dysphagia, respiratory compromise, visual loss (optic atrophy), and cognitive regression → severe global disability.
- **Complications:** aspiration, recurrent respiratory infections, feeding failure/malnutrition, apnea, seizures (subset), metabolic decompensation during illness.
- **Prognostic factors:** earlier onset and early brainstem/respiratory involvement portend worse outcome; frequency and severity of stress-triggered crises drive trajectory.

---

## 12. Treatment

**There is no curative therapy; management is largely supportive.** Suggested MAXO terms are given per intervention.

**Supportive / rehabilitative (mainstay).**
- **Supportive care (MAXO:0000950)** — treatment of intercurrent illness, avoidance of fasting/catabolism, sick-day protocols.
- **Nutritional support / gastrostomy feeding — dietary intervention (MAXO:0000088)**, gastrostomy tube placement (surgical procedure, **MAXO:0000004**).
- **Respiratory support** — ventilatory/apnea management (assisted ventilation; supportive/critical care).
- **Physical / occupational / speech therapy — physical therapy (MAXO:0000011)**; **rehabilitation (NCIT:C15315)**.
- **Symptomatic management of dystonia** (e.g., trihexyphenidyl, baclofen, benzodiazepines), seizures (anticonvulsants — **avoiding valproate** where possible given mitochondrial toxicity), and sialorrhea.

**Pharmacotherapy / "mitochondrial cocktail" (unproven but commonly used; MAXO:0000058 vitamin/cofactor therapy).**
- **Coenzyme Q10 / ubiquinone** (CHEBI:46245), **riboflavin/vitamin B2** (CHEBI:17015), **thiamine** (CHEBI:18385), **L-carnitine** (CHEBI:16347), **biotin**, and antioxidants. Evidence base is weak; used empirically.
- **Sodium bicarbonate / dichloroacetate** for acute lactic acidosis (DCA use limited by peripheral neuropathy).
- **Avoid mitochondrial-toxic drugs** (valproate, prolonged propofol, aminoglycosides where feasible).

**Experimental / investigational.**
- **EPI-743 (vatiquinone/α-tocotrienol quinone)** — a redox-modulating antioxidant investigated in Leigh syndrome/inherited mitochondrial disease (early open-label studies suggested possible benefit in some patients; e.g., Martinelli et al. 2012, EPI-743 in Leigh syndrome, PMID **23010433**). Results across mitochondrial-disease trials have been mixed; not approved for SURF1 LS.
- Other agents explored across Leigh/mitochondrial disease broadly (not SURF1-specific): idebenone, cysteamine bitartrate (RP103), and general mitochondrial-disease pipeline candidates. **Gene- and cell-based therapies are not clinically available** for SURF1 deficiency.
- No effective **pharmacogenomic** or **targeted molecular** therapy is established.

**Genetic counseling** (see §13) is an essential component of care.

---

## 13. Prevention

- **Primary prevention:** not possible for an established biallelic-LOF genetic disease; **preventing crises** via avoidance of catabolic triggers, prompt treatment of infections, and structured sick-day/emergency protocols is the practical analog of prevention.
- **Secondary prevention (reproductive):** **genetic counseling — genetic counseling (MAXO:0000082/NCIT:C15516)**; **carrier/cascade testing** of relatives; **prenatal diagnosis** and **preimplantation genetic testing (PGT-M)** once familial *SURF1* variants are known, to prevent recurrence (25% risk per pregnancy).
- **Tertiary prevention:** anticipatory management of dysphagia/aspiration (gastrostomy), respiratory surveillance, immunizations to reduce infection-triggered crises, and multidisciplinary metabolic follow-up to forestall complications.
- **Immunization/public health:** routine vaccination is generally encouraged to reduce infection-precipitated decompensation, with attention to peri-vaccination metabolic support.

---

## 14. Other Species / Natural Disease

- **Taxonomy of models:** *Homo sapiens* (**NCBITaxon:9606**); *Mus musculus* (**NCBITaxon:10090**); and *Sus scrofa* — note OLS lists **MONDO:1012801** "Leigh syndrome, SURF1-related, pig," reflecting a porcine model resource.
- **Orthologous gene:** mouse *Surf1* (NCBI Gene 20930) is conserved; *SURF1* orthologs exist across metazoans (the Surfeit gene cluster is deeply conserved).
- **Natural disease in animals:** no well-characterized spontaneous companion-animal or wildlife SURF1 Leigh-syndrome analog is established; the disease is studied primarily through engineered models.
- **Comparative biology (important caveat):** the mouse **does not faithfully recapitulate the human severity** — *"SURF1 gene mutations cause a severe COX deficiency manifesting as the Leigh syndrome in humans, whereas in mice SURF1⁻/⁻ knockout leads only to a mild COX defect"* (Kovářová et al. 2016, PMID **26804654**, [DOI](https://doi.org/10.1016/j.bbadis.2016.01.007)). This is a documented **human–model mismatch** (species-specific dependence of COX assembly on SURF1).
- **Zoonotic potential:** none (non-transmissible genetic disorder).

---

## 15. Model Organisms

- **Mouse (*Surf1⁻/⁻* knockout):** the principal mammalian model. It shows **reduced COX activity but a paradoxically mild phenotype** and, in some reports, even **extended lifespan / altered stress resistance** — it does **not** reproduce the human necrotizing encephalopathy. Useful for studying COX assembly, supercomplex biology, and tissue-specific effects, but **limited as a phenotypic disease model**. Kovářová et al. used it to dissect *"tissue- and species-specific differences in cytochrome c oxidase assembly induced by SURF1 defects,"* concluding human COX assembly is **much more SURF1-dependent** than mouse (PMID **26804654**, [DOI](https://doi.org/10.1016/j.bbadis.2016.01.007)).
- **Patient-derived fibroblasts / cybrids:** the workhorse **in vitro** system — demonstrate absent SURF1 protein, reduced COX subunits, accumulated COX1 assembly intermediates, and preferential COX recruitment into supercomplexes; used for complementation/rescue assays (Yao & Shoubridge 1999, PMID **10556303**, [DOI](https://doi.org/10.1093/hmg/8.13.2541); Zhu et al. 1998 complementation mapping, PMID **9843204**, [DOI](https://doi.org/10.1038/3804)).
- **iPSC-derived neurons/organoids** (emerging): patient iPSC models are being used to capture the human-specific neuronal vulnerability that the mouse misses — the most promising route to a faithful disease model.
- **Invertebrate/yeast:** *Saccharomyces cerevisiae* **Shy1** (the SURF1 ortholog) and *Drosophila/C. elegans* orthologs have been used to define the conserved COX-assembly function biochemically.
- **Porcine model:** referenced via MONDO:1012801 (SURF1-related Leigh syndrome, pig), a large-animal resource with potentially better CNS fidelity than rodents.
- **Model resources:** MGI (mouse *Surf1*), IMPC/KOMP, Cellosaurus (patient fibroblast lines), Alliance of Genome Resources (orthology).

**Applications:** COX assembly-factor biology, respiratory supercomplex organization, tissue-specific bioenergetics, antioxidant/therapeutic screening. **Key limitation:** the rodent's mild phenotype means efficacy signals must be interpreted cautiously and confirmed in human-relevant (iPSC/large-animal) systems.

---

## Consolidated Ontology-Term Suggestions (for KB population)

- **Disease:** MONDO:0009723 (Leigh syndrome); OMIM 256000 / 220110 (MC4DN1); ORPHA:506; DOID:3652.
- **Gene/protein:** *SURF1* HGNC:11474; UniProt Q15526; GO:0004129 (cytochrome-c oxidase activity), GO:0033617 (complex IV assembly).
- **Phenotypes (HP):** 0001252 hypotonia; 0002376 developmental regression; 0001263 global developmental delay; 0001508 failure to thrive; 0011968 feeding difficulties; 0002013 vomiting; 0002871 central apnea; 0002093 respiratory insufficiency; 0001332 dystonia; 0001251 ataxia; 0000597 ophthalmoparesis; 0000639 nystagmus; 0000998 hypertrichosis; 0000648 optic atrophy; 0001250 seizures; 0003128 lactic acidosis; 0003567 increased CSF lactate; 0002451 basal ganglia gliosis; 0009830 peripheral neuropathy.
- **Cell types (CL):** 0000540 neuron; 0000127 astrocyte.
- **Anatomy (UBERON):** 0002420 basal ganglia; 0001874 putamen; 0002298 brainstem; 0001891 midbrain; 0001897 thalamus; 0002038 substantia nigra; 0002037 cerebellum; 0000941 optic nerve; 0001134 skeletal muscle.
- **Subcellular (GO CC):** 0005739 mitochondrion; 0005743 mitochondrial inner membrane; 0005751 complex IV.
- **Chemicals (CHEBI):** 24996 lactate; 15361 pyruvate; 46245 ubiquinone/CoQ10; 15379 O₂; 30616 ATP; 17015 riboflavin; 18385 thiamine; 16347 L-carnitine.
- **Treatments (MAXO):** 0000950 supportive care; 0000088 dietary intervention; 0000011 physical therapy; 0000004 surgical procedure; 0000058 vitamin/cofactor therapy; genetic counseling (MAXO/NCIT:C15516).
- **Inheritance (HP):** 0000007 autosomal recessive.

---

## Key References (PubMed; DOI links)

According to PubMed:
1. Zhu Z et al. *SURF1, encoding a factor involved in the biogenesis of cytochrome c oxidase, is mutated in Leigh syndrome.* Nat Genet 1998;20:337–43. PMID **9843204**, [DOI](https://doi.org/10.1038/3804). — *Gene discovery.*
2. Yao J, Shoubridge EA. *Expression and functional analysis of SURF1 in Leigh syndrome patients with cytochrome c oxidase deficiency.* Hum Mol Genet 1999;8:2541–9. PMID **10556303**, [DOI](https://doi.org/10.1093/hmg/8.13.2541). — *Protein function / LOF mechanism.*
3. Péquignot MO et al. *Mutations in the SURF1 gene associated with Leigh syndrome and cytochrome C oxidase deficiency.* Hum Mutat 2001;17:374–81. PMID **11317352**, [DOI](https://doi.org/10.1002/humu.1112). — *Mutation spectrum / recurrent allele.*
4. Shoubridge EA. *Cytochrome c oxidase deficiency.* Am J Med Genet 2001;106:46–52. PMID **11579424**, [DOI](https://doi.org/10.1002/ajmg.1378). — *COX biology and assembly factors.*
5. Wedatilake Y et al. *SURF1 deficiency: a multi-centre natural history study.* Orphanet J Rare Dis 2013;8:96. PMID **23829769**, [DOI](https://doi.org/10.1186/1750-1172-8-96). — *Flagship clinical/frequency/natural-history data.*
6. Debray FG et al. *LRPPRC mutations cause a phenotypically distinct form of Leigh syndrome with cytochrome c oxidase deficiency.* J Med Genet 2011;48:183–9. PMID **21266382**, [DOI](https://doi.org/10.1136/jmg.2010.081976). — *SURF1 vs LRPPRC contrast/prognosis.*
7. Kovářová N et al. *Tissue- and species-specific differences in cytochrome c oxidase assembly induced by SURF1 defects.* Biochim Biophys Acta 2016;1862:705–15. PMID **26804654**, [DOI](https://doi.org/10.1016/j.bbadis.2016.01.007). — *Mouse model / human–model mismatch.*
8. Maalej M et al. *Cytochrome C oxydase deficiency: SURF1 gene investigation in patients with Leigh syndrome.* Biochem Biophys Res Commun 2018;497:1043–8. PMID **29481804**, [DOI](https://doi.org/10.1016/j.bbrc.2018.02.169). — *Splice variants / consanguineous population.*
9. Loeffen J et al. *The first nuclear-encoded complex I mutation in a patient with Leigh syndrome.* Am J Hum Genet 1998;63:1598–608. PMID **9837812**, [DOI](https://doi.org/10.1086/302154). — *Differential (complex I LS).*

---

### Curation notes / caveats for KB entry
- **Onset/frequency numbers** in §3 are directly quotable from PMID 23829769 (exact abstract text preserved above) — suitable for evidence `snippet:` values with `evidence_source: HUMAN_CLINICAL`.
- The **mouse phenotype discrepancy** (§14–15) is a genuine **HUMAN_MODEL_MISMATCH** candidate (evidence exists in mouse but does not reproduce human disease severity), not a knowledge gap — flag accordingly with PMID 26804654.
- **Epidemiology:** no SURF1-specific per-100,000 incidence is reliably published; use Leigh-syndrome-wide estimates with a `notes:` caveat rather than asserting a precise SURF1 rate.
- **EPI-743** (§12) should be curated cautiously — cite as investigational; verify the precise Martinelli 2012 snippet against the fetched abstract before committing it as evidence, per the dismech DR/anti-hallucination SOP.
- Verify every PMID/snippet with `just fetch-reference` and `just validate-references` before entry, and confirm all ontology labels with `just validate-terms-file`.