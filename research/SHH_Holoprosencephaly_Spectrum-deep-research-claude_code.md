---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-31T02:11:22.693387'
end_time: '2026-07-31T02:17:26.783459'
duration_seconds: 364.09
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: SHH Holoprosencephaly Spectrum
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
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 12
  num_turns: 17
  total_cost_usd: 1.7387436
  session_id: ace7b000-f678-576e-923d-e16b62f69e26
  stop_reason: end_turn
citation_count: 34
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** SHH Holoprosencephaly Spectrum
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **SHH Holoprosencephaly Spectrum** covering all of the
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

# SHH Holoprosencephaly Spectrum — Comprehensive Research Report

## 1. Disease Information

**Overview.** Holoprosencephaly (HPE) is the most common structural malformation of the developing human forebrain (prosencephalon), arising from failure of the prosencephalon to divide into distinct cerebral hemispheres and underlying deep-brain (diencephalic) structures during the third to fourth week of gestation. It exists as a continuous phenotypic spectrum — from the most severe form (alobar HPE with a single fused monoventricle and cyclopia) through semilobar and lobar forms to "microform" HPE, in which craniofacial midline anomalies (e.g., a single central maxillary incisor, hypotelorism) occur with an essentially normal-appearing brain on imaging ([GeneReviews Holoprosencephaly Overview](https://www.ncbi.nlm.nih.gov/books/NBK1530/); [Holoprosencephaly: Review of Embryology, Clinical Phenotypes, Etiology and Management, PMC10137117](https://pmc.ncbi.nlm.nih.gov/articles/PMC10137117/)). "SHH Holoprosencephaly Spectrum" designates the subset of the HPE spectrum attributable to heterozygous pathogenic variation in the *SHH* (Sonic Hedgehog) gene at 7q36.3 — the single most common identified monogenic cause of nonsyndromic HPE — and, more broadly, the mechanistic spectrum of disease produced by disruption anywhere along the SHH signal-transduction pathway (ligand, receptors, intracellular transducers, and transcriptional effectors).

**Key identifiers:**
- **OMIM:** Holoprosencephaly 1 (HPE1, chromosomal/locus designation) #236100; **Holoprosencephaly 3 (HPE3, the SHH-specific disorder)** #142945; *SHH* gene entry *600725 ([OMIM 236100](https://www.omim.org/entry/236100); [OMIM 142945](https://omim.org/entry/142945))
- **MONDO:** MONDO:0016296 (holoprosencephaly, general); MONDO:0012322 (holoprosencephaly 5/ZIC2, illustrating the per-gene MONDO subtyping pattern) ([Monarch Initiative](https://monarchinitiative.org/MONDO:0012322))
- **Orphanet:** ORPHA:2162 (Holoprosencephaly) ([Orphanet](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Lng=GB&Expert=2162))
- **ICD-10:** Q04.2 (Holoprosencephaly); **ICD-11:** LA02.0
- **MeSH:** D019204 (Holoprosencephaly)
- **HGNC gene:** SHH, HGNC:10848, chromosome 7q36.3

**Synonyms:** Arhinencephaly (older, imprecise term); HPE; "cyclopia" (for the most severe alobar phenotype); Holoprosencephaly-3 (HPE3, SHH-specific OMIM designation); Autosomal Dominant Holoprosencephaly (ADHPE, when referring to the SHH/ZIC2/SIX3/TGIF1 nonsyndromic group).

**Data provenance.** Most of the mechanistic and epidemiologic knowledge base for SHH-HPE is aggregated disease-level data: large multicenter case series and mutation-spectrum studies (Cohen, Roessler/Muenke, Solomon et al.), population birth-defects surveillance registries, and animal-model experimental data, rather than large-scale individual-patient EHR cohorts. GeneReviews and Orphanet function as the principal curated aggregating clinical-genetics resources; ClinVar/ClinGen aggregate individual-variant-level clinical data.

---

## 2. Etiology

**Disease-causal framework.** HPE is fundamentally a disorder of **Sonic Hedgehog (SHH) signaling failure** in the rostral neural plate/prosencephalon, producing inadequate ventral midline induction and incomplete telencephalic cleavage. "Disruption of sonic hedgehog (SHH) signaling is the main pathophysiologic mechanism underlying HPE. SHH is a secreted protein that has a key role in the maintenance of the notochord and the patterning and induction of the ventral forebrain" ([Holoprosencephaly Overview, GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK1530/)). Causation is **multifactorial and heterogeneous**, spanning chromosomal, monogenic, environmental/teratogenic, and — very often — combined ("multiple-hit") mechanisms in a single individual.

### Genetic risk factors

- **Chromosomal abnormalities** account for roughly **25–50%** of all HPE cases. **Trisomy 13 (Patau syndrome)** is the single most common chromosomal cause, comprising ~40–75% of chromosomally abnormal HPE depending on the series; trisomy 18 and triploidy are also recurrent ([PMC10137117](https://pmc.ncbi.nlm.nih.gov/articles/PMC10137117/)).
- **Copy-number variants (CNVs)** are found in ~10–14% of HPE cases, frequently overlapping known HPE-gene loci (e.g., 18p11.3/*TGIF1*, 2p21/*SIX3*, 13q32/*ZIC2*).
- **Monogenic (single-gene) causes** account for ~18–25% of cases. At least 17 non-syndromic HPE genes are recognized, virtually all functioning within or regulating the SHH pathway:
  - **SHH** (7q36.3) — the most common single-gene cause, **5.4–5.9%** of non-syndromic HPE ([PMC10137117](https://pmc.ncbi.nlm.nih.gov/articles/PMC10137117/)); in specific ascertainment strata, SHH mutations were found in "3.7% of sporadic cases, 18% of familial cases, and 37% of families with autosomal dominant transmission" ([Mutational Spectrum of the Sonic Hedgehog Gene, *Hum Mol Genet* 1999](https://academic.oup.com/hmg/article/8/13/2479/651151)).
  - **ZIC2** (13q32) — 4.8–5.2%, predominantly de novo (70–80%), distinctive facial gestalt.
  - **SIX3** (2p21), a direct transcriptional regulator of *SHH* expression — ~3%, associated with more severe HPE subtypes.
  - **GLI2** (2q14.2) — ~3.2%, often associated with microforms and pituitary anomalies.
  - **TGIF1** (18p11.3) — <1%.
  - Additional/rarer genes acting within the pathway: **PTCH1** (the SHH receptor), **CDON**, **GAS1**, **DISP1**, **FGF8**, **FGFR1**, **DLL1**, **NODAL**, **FOXH1** ([PMC10137117](https://pmc.ncbi.nlm.nih.gov/articles/PMC10137117/); [Monarch Initiative](https://monarchinitiative.org/MONDO:0012322)).
  - Rare non-dominant modes: autosomal recessive HPE (**STIL**), and X-linked HPE (**STAG2**, **SMC1A** — all reported probands female, suggesting male lethality).
- **Modifier / second-site (oligogenic) loci:** **GAS1** functions as a genetic modifier of SHH-pathway HPE — "loss of a single *Shh* allele in a *Gas1*−/− background significantly exacerbated the midline craniofacial phenotype, providing genetic evidence that Shh and Gas1 interact," and hypomorphic *GAS1* alleles are proposed to contribute to phenotypic variability in patients carrying primary mutations in other HPE genes, consistent with a "multiple-hit hypothesis" ([Gas1 is a modifier for holoprosencephaly, *J Clin Invest* 2007, PMID:17525797](https://pubmed.ncbi.nlm.nih.gov/17525797/)). GAS1 maps to 9q21.3–q22.

### Environmental / non-genetic risk factors

- **Maternal pre-gestational (insulin-requiring) diabetes mellitus** is the best-established environmental risk factor, conferring **>10-fold increased risk**; HPE occurs in ~1–2% of infants of diabetic mothers. Proposed mechanisms include hyperglycemia-driven oxidative free-radical injury, apoptosis, and impaired cranial neural crest cell migration ([PMC10137117](https://pmc.ncbi.nlm.nih.gov/articles/PMC10137117/)).
- **Maternal alcohol consumption** during pregnancy is dose-associated with increased HPE risk; ethanol is proposed to directly inhibit hedgehog protein cholesterol modification and SHH autoprocessing/signaling. Gene–environment interaction is well documented in the mouse: "the teratogenic effects of prenatal ethanol exposure are exacerbated by Sonic Hedgehog or Gli2 haploinsufficiency" (PMC3929747).
- **Retinoic acid** exposure, **mycotoxins** (ochratoxins), and pharmacologic/dietary **cholesterol-synthesis inhibitors** are implicated teratogens; heavy metals and ionizing radiation have been proposed but are not definitively established.
- **Maternal folic acid** intake has been reported as potentially protective (one study reporting a 73% risk reduction with periconceptional use), though evidence is mixed across studies.

### Gene–environment interaction

The clearest documented gene–environment interaction is between **SHH-pathway haploinsufficiency and ethanol exposure**: mice heterozygous for null alleles of *Shh* or *Gli2* show markedly exacerbated HPE-spectrum phenotypes upon prenatal ethanol exposure compared with either insult alone, directly modeling the "multiple-hit" (genetic susceptibility + teratogen) hypothesis proposed for human HPE, including the *Cdon*-mutant/ethanol interaction rescued by reduced *Ptch1* dosage (PMC3823703). This supports a threshold/dosage model in which partial SHH pathway function from a single mutant allele is pushed below the pathogenic threshold by an independent environmental insult on the wild-type allele's output.

**Suggested GO/pathway terms:** GO:0007224 (smoothened signaling pathway), GO:0007228 (positive regulation of hh target transcription factor activity), GO:0021537 (telencephalon development), GO:0021782 (glial cell development — ventral forebrain patterning downstream processes).

---

## 3. Phenotypes

Phenotype severity in SHH-HPE forms a continuum correlating loosely (not strictly) with genotype, with extreme intrafamilial variability — "ranging from alobar HPE with cyclopia to clinically normal" even within a single kindred carrying an identical *SHH* variant ([GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK1530/)).

### Structural brain (clinical signs, neuroimaging)
| Phenotype | HPO term (suggested) | Notes |
|---|---|---|
| Alobar holoprosencephaly | HP:0007169 | Single monoventricle, fused thalami, most severe |
| Semilobar holoprosencephaly | HP:0007193 | Partial hemispheric separation |
| Lobar holoprosencephaly | HP:0007194 | Minimal frontal fusion |
| Middle interhemispheric variant (MIHV/syntelencephaly) | HP:0030041 (or free text) | Posterior frontal/parietal fusion |
| Absent septum pellucidum | HP:0001331 | Common in lobar HPE |
| Agenesis of corpus callosum (partial) | HP:0001274 | Variable by subtype |
| Hydrocephalus | HP:0000238 | 16–40% of cohorts |
| Microcephaly | HP:0000252 | Present in nearly all without hydrocephalus |

### Craniofacial (symptoms/signs) — severity-graded
- **Cyclopia** (HP:0000531) / **synophthalmia** (HP:0000577): single/fused midline eye, alobar HPE.
- **Ethmocephaly** (extreme hypotelorism with absent nose and proboscis) and **cebocephaly** (single-nostril flattened nose) — severe/intermediate forms.
- **Hypotelorism** (HP:0000601), **midline cleft lip/palate** (HP:0000175/HP:0000176), **premaxillary agenesis**.
- **Microform features** (mild end of spectrum, may occur with normal-appearing brain): **single central maxillary incisor / solitary median maxillary central incisor (SMMCI)** (HP:0006315) — a distinctive marker of autosomal dominant (often SHH-related) HPE, estimated general-population incidence ~1:50,000; **hypotelorism**, **anosmia/hyposmia** (HP:0004408, from absent olfactory tracts/bulbs), **depressed nasal ridge**. A specific missense variant, SHH p.Ile111Phe, has been reported as potentially SMMCI-specific ([SMMCI syndrome, PMC1464380](https://pmc.ncbi.nlm.nih.gov/articles/PMC1464380/)).

### Neurodevelopmental / behavioral
- Developmental delay/intellectual disability (HP:0001263) — present in virtually all individuals with structural HPE; severity correlates with brain malformation grade.
- Spasticity (HP:0001257), axial hypotonia (HP:0008936), dystonia/choreoathetosis (correlating with basal ganglia non-separation).
- Seizures (HP:0001250) — present in ~50% of HPE patients, without strict correlation to HPE severity; often anticonvulsant-responsive but can be refractory when cortical dysplasia coexists.
- In higher-functioning (typically microform/lobar) individuals: executive dysfunction, ADHD, learning disabilities, anxiety, depression.

### Laboratory / endocrine abnormalities
- **Central diabetes insipidus** (HP:0000873) — the single most common endocrinopathy, occurring in ~70% of patients with classic (structural) HPE, correlating with severity of hypothalamic non-separation.
- Hypothyroidism (HP:0000821) ~11%, hypoadrenocorticism/ACTH deficiency (HP:0000829) ~7%, growth hormone deficiency (HP:0000824) ~5% ([Endocrine disorders associated with holoprosencephaly, PMID:16355806](https://pubmed.ncbi.nlm.nih.gov/16355806/)).

### Onset, severity, progression, frequency
- **Onset:** congenital/prenatal by definition (embryonic weeks 3–4); microform features may not be recognized clinically until later childhood or in an "unaffected" relative investigated after a severely affected proband is identified.
- **Severity/course:** structural brain phenotype itself is static (a developmental field defect, not degenerative), but the clinical picture "progresses" developmentally — feeding difficulties, seizures, and movement disorders often emerge/are recognized over the first years of life. Endocrine, orthopedic (contractures, scoliosis, hip dislocation), and gastrointestinal complications accrue over time and require longitudinal management.
- **Quality of life:** severely impacted in alobar/semilobar HPE (profound motor and cognitive impairment, ~60% of adolescent/adult survivors nonambulatory/nonverbal); comparatively preserved in microform/lobar/MIHV HPE, where individuals may be independently ambulatory, verbal, and in some cases of documented normal intelligence despite carrying an SHH pathogenic variant.

---

## 4. Genetic / Molecular Information

**Primary causal gene:** ***SHH*** (HGNC:10848, chromosome 7q36.3, OMIM *600725), encoding the secreted morphogen Sonic Hedgehog. Heterozygous pathogenic variants cause **Holoprosencephaly-3 (HPE3, OMIM #142945)**.

**Variant spectrum and classification:**
- Reported variant classes span "amino-acid substitutions, insertion/deletion mutations, frame-shift mutations, poly-alanine tract expansions, and gene deletions" throughout the gene ([Clinical Utility Gene Card, PMC3039493](https://ncbi.nlm.nih.gov/pmc/articles/PMC3039493)).
- The dominant molecular mechanism is **loss of function / haploinsufficiency**: "numerous different heterozygous mutations have been identified in HPE patients and include missense, nonsense, deletion, and frameshift mutations... predicted to cause loss-of-function through either key structural alterations of the ligand or its altered synthesis" (Mutational spectrum studies, [ResearchGate summary](https://www.researchgate.net/publication/26672080)).
- Genotype–phenotype correlation is imperfect but present in aggregate: truncating variants are more likely to produce frank structural HPE than non-truncating (missense) variants, though a substantial fraction of missense variants also cause severe disease and truncating variants can occur in essentially unaffected carriers — reflecting the pathway's extreme sensitivity to dosage and its dependence on genetic/environmental modifiers.
- ACMG/AMP classification: SHH variants curated in ClinVar and by ClinGen are predominantly classified pathogenic/likely pathogenic when truncating and located in functionally critical (N-terminal signaling) domains; missense VUS classification is common given incomplete penetrance and variable expressivity, complicating variant interpretation. ClinGen's Gene Dosage curation supports **haploinsufficiency (dosage sensitivity)** for *SHH* ([ClinGen SHH Dosage](https://search.clinicalgenome.org/kb/gene-dosage/HGNC:10848)).
- **De novo rate:** approximately 10–30% of SHH pathogenic variants arise de novo; the remainder are inherited from a heterozygous, often clinically unaffected or minimally affected (reduced penetrance), parent.
- **Population frequency:** SHH loss-of-function variants are constrained in population databases (gnomAD) consistent with dominant haploinsufficiency, though exact pLI/constraint metrics were not independently retrieved in this pass — curators should verify current gnomAD constraint scores directly.

**Related monogenic/HPE-pathway genes** (for the broader "SHH pathway" spectrum): *PTCH1* (SHH receptor, negative regulator of SMO), *SMO* (downstream transducer — also implicated in SMMCI via an SMO variant), *GLI2*/*GLI1*/*GLI3* (downstream zinc-finger transcription effectors — GLI2 acts as activator or repressor depending on pathway state), *CDON* and *GAS1* (co-receptors/modifiers), *DISP1* (dispatched homolog 1, required for SHH ligand release), *FGF8*/*FGFR1*, *ZIC2*, *SIX3*, *TGIF1*, *NODAL*, *FOXH1*.

**Somatic vs germline:** HPE-causing SHH variants are germline; SHH pathway *somatic* mutations (PTCH1, SMO, GLI activating variants) are separately implicated in medulloblastoma and basal cell carcinoma — a mechanistically related but clinically distinct disease process (oncogenic SHH-pathway activation vs. developmental SHH-pathway loss-of-function).

**Epigenetics:** Not well characterized specifically for SHH-HPE; the SHH pathway more broadly is subject to epigenetic regulation of its target-gene program (Gli-binding sites, cis-regulatory element methylation) but no HPE-specific epigenetic biomarker is established.

**Chromosomal abnormalities:** As above — trisomy 13, trisomy 18, triploidy; CNVs overlapping 7q36 (deletions encompassing *SHH* or its long-range cis-regulatory elements, e.g., the ZRS-like forebrain enhancers) can also produce HPE3-equivalent phenotypes and are detectable by chromosomal microarray (CMA), which identifies pathogenic CNVs in ~10% of HPE cases.

**Suggested ontology terms:** HGNC:10848 (SHH); GO:0005113 (patched binding); GO:0030177 (positive regulation of Wnt signaling pathway, cross-talk); UniProt P08151 (mouse Shh)/Q15465 (human SHH protein).

---

## 5. Environmental Information

(Overlaps with §2 but detailed here per template.)

- **Toxins/teratogens:** Cyclopamine and related *Veratrum californicum* steroidal jerveratrum alkaloids are the classic experimental HPE teratogens (see §14/§15) and act as direct pharmacologic SMO antagonists — a mechanistic proof-of-concept for pathway-level causation in humans.
- **Maternal metabolic factors:** Pregestational diabetes (strongest established environmental risk factor, >10-fold risk elevation), maternal obesity has been suggested in some epidemiologic series.
- **Lifestyle factors:** Maternal alcohol use (dose-related), tobacco use has been investigated with less consistent association; retinoic acid/vitamin A excess.
- **Infectious agents:** No well-established infectious cause of HPE; unlike some other CNS malformations (e.g., congenital Zika microcephaly), HPE is not primarily an infectious-teratogen disease, though isolated case reports of maternal infection coinciding with HPE exist without established causality.
- **Nutritional:** Low periconceptional folate has been proposed as a risk factor and supplementation as potentially protective, though data are less robust than for neural tube defects.

---

## 6. Mechanism / Pathophysiology

**Causal chain (trigger → clinical manifestation):**

1. **Molecular trigger:** Heterozygous loss-of-function variant in *SHH* (or another pathway gene) reduces the dose/gradient of functional SHH ligand available to the ventral prosencephalic midline and prechordal plate/notochord signaling centers during gastrulation and early neurulation (approximately days 18–28 of human gestation).
2. **Cellular/tissue-level consequence:** Insufficient SHH-PTCH1-SMO-GLI signal transduction in the ventral neural tube and rostral neural plate fails to specify ventral forebrain identity and fails to antagonize dorsalizing BMP/WNT signals adequately — "development of the forebrain critically depends on the Sonic Hedgehog (Shh) signaling pathway... regulating processes such as ventral forebrain neuronal differentiation" ([Frontiers in Molecular Biosciences, 2021](https://www.frontiersin.org/journals/molecular-biosciences/articles/10.3389/fmolb.2021.711710/full)).
3. **Morphogenetic consequence:** Failure of the prosencephalon to cleave sagittally into paired cerebral hemispheres and to separate horizontally into telencephalon/diencephalon, and failure of the underlying paired basal ganglia, thalami, and hypothalamus to individuate — producing the alobar/semilobar/lobar continuum of structural brain malformation.
4. **Coupled craniofacial consequence:** Because cranial neural crest cell migration and facial primordia patterning are co-regulated by the same rostral midline SHH signaling center, forebrain and facial anomalies are mechanistically coupled ("the face predicts the brain") — hence the correlation (though imperfect) between craniofacial severity and CNS malformation severity.
5. **Downstream systemic consequences:** Hypothalamic-pituitary axis maldevelopment (from disrupted ventral diencephalic/infundibular patterning) → central diabetes insipidus and anterior pituitary hormone deficiencies; abnormal olfactory bulb/tract formation → anosmia; cortical/white-matter maldevelopment and basal ganglia non-separation → developmental delay, spasticity, dystonia, seizures.

**Molecular pathway detail (canonical Hedgehog signal transduction):**
- In the absence of SHH ligand, **PTCH1** (the receptor) tonically inhibits **SMO** (Smoothened, a GPCR-family transducer).
- SHH ligand binding to PTCH1 relieves this inhibition, permitting SMO to translocate/accumulate in the primary cilium.
- Active SMO antagonizes **PKA**-mediated phosphorylation/proteolytic processing of the **GLI2/GLI3** transcription factors, shifting them from truncated transcriptional repressor forms (GLIR) to full-length activator forms (GLIA), and inducing **GLI1** as a downstream amplifying activator ([Role of Sonic Hedgehog in HPE and SRPS, PMC8468456](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8468456/)).
- This canonical pathway is strictly **primary-cilium-dependent** in vertebrates; non-canonical, cilium-independent SHH signaling also exists.
- **Modifiers/co-receptors CDON and GAS1** enhance ligand-receptor engagement and pathway sensitivity, explaining their role as dose-dependent genetic modifiers of HPE penetrance.

**Threshold/dosage model & variable expressivity:** HPE is understood as a classic dosage-sensitive developmental threshold disorder — total pathway output (from SHH ligand concentration, receptor/co-receptor availability, and downstream transducer dose) must exceed a minimum level for normal ventral forebrain patterning; any combination of genetic (primary mutation + modifier alleles, potentially oligogenic "multiple-hit" combinations) and environmental (ethanol, cholesterol-synthesis disruption) insults that additively reduces net pathway output below this threshold produces disease, with severity scaling to the degree of shortfall. This directly explains the extreme intrafamilial phenotypic variability characteristic of SHH-HPE — "temporal disruption of a single molecular pathway can produce variable expressivity" and "temporal perturbations in sonic hedgehog signaling elicit the [full] spectrum of holoprosencephaly phenotypes" ([JCI, PMID referenced via search](https://www.jci.org/articles/view/19596)).

**Cell types involved (CL terms suggested):** notochord cells, prechordal plate mesendoderm, ventral neural tube floor-plate cells (CL:0000030 glioblast/floor plate neuroepithelium), cranial neural crest cells (CL:0000333), telencephalic ventricular zone progenitors, radial glia.

**GO biological process terms:** GO:0007224 (smoothened signaling pathway), GO:0021998 (neural plate mediolateral regionalization), GO:0021801 (cerebral cortex radial glia guided migration — downstream), GO:0021537 (telencephalon development), GO:0060021 (roof plate formation — dorsal midline, indirectly perturbed by ectopic ventral signaling).

**Omics/advanced technologies:** Single-cell and spatial transcriptomic characterization of SHH-gradient-dependent ventral forebrain progenitor domains has been performed extensively in mouse and, more recently, in human forebrain organoid models, though HPE-specific patient-derived organoid/iPSC transcriptomic datasets are still relatively sparse in the literature compared with the extensive classical mouse genetic literature.

---

## 7. Anatomical Structures Affected

**Organ level (primary):** Brain — specifically prosencephalon-derived structures: cerebral hemispheres/telencephalon, diencephalon (thalamus, hypothalamus), pituitary gland (hypophysis), olfactory bulbs/tracts. **UBERON terms:** UBERON:0001890 (forebrain), UBERON:0002435 (striatum/basal ganglia), UBERON:0001898 (hypothalamus), UBERON:0000007 (pituitary gland), UBERON:0002264 (olfactory bulb).

**Organ level (secondary/associated):** craniofacial skeleton and soft tissue (midface, nose, maxilla, orbits) — UBERON:0000209 (midface), UBERON:0002397 (nose), UBERON:0000966 (retina/eye structures in cyclopia/synophthalmia); gastrointestinal tract (motility dysfunction, reflux); musculoskeletal system (contractures, scoliosis, hip dysplasia secondary to spasticity).

**Body systems involved:** nervous system (primary), endocrine system (hypothalamic-pituitary axis), craniofacial/skeletal system, gastrointestinal system (secondary, functional), sensory systems (olfactory, visual).

**Tissue/cell level:** neuroepithelium of the ventral neural tube and prosencephalic vesicle; cranial neural crest-derived mesenchyme of the face; notochord and prechordal plate (signaling source tissues, transiently present embryonic structures).

**Subcellular level (GO Cellular Component):** primary cilium (GO:0005929) — obligate site of canonical vertebrate Hedgehog pathway transduction; plasma membrane (PTCH1/SMO localization); nucleus (GLI transcription factor activity).

**Localization/laterality:** HPE is fundamentally a **midline** developmental field defect; laterality is not typically a feature (bilateral/symmetric midline non-separation), though craniofacial anomalies can show asymmetric severity.

---

## 8. Temporal Development

- **Onset:** Congenital/embryonic — the primary morphogenetic lesion occurs during the third–fourth week of gestation (Carnegie stages 8–13), i.e., before most pregnancies are clinically recognized. Clinical recognition, however, ranges from first-trimester prenatal ultrasound (severe forms) to incidental discovery in adulthood (microform HPE in an unaffected-appearing relative of a proband).
- **Onset pattern:** The structural malformation itself is a single embryonic developmental event (not acute/subacute in the postnatal sense); it is congenital and, at the anatomic level, non-progressive.
- **Disease stages/progression:** Anatomically static once formed, but the *clinical* course is one of evolving multisystem complications over infancy and childhood: emergence of seizures, feeding/aspiration issues, movement disorders, and endocrinopathies (diabetes insipidus, hypopituitarism) typically become apparent and require intervention over the first months to years of life. In milder (lobar/MIHV/microform) cases, diagnosis is sometimes delayed until developmental delay, seizures, or a movement disorder prompts neuroimaging later in childhood.
- **Course pattern:** Chronic, lifelong, non-remitting (a static structural malformation with a dynamic, generally stable-to-slowly-evolving functional/complications profile); not relapsing-remitting.
- **Critical developmental window:** The teratogenic/mutational critical period is narrow — gestational days ~18–28 in humans (directly paralleling the day-13–14 post-conception critical window identified for cyclopamine-induced HPE in sheep).

---

## 9. Inheritance and Population

**Epidemiology:**
- **Conceptus prevalence:** ~1:250 (i.e., extremely common among all conceptuses).
- **Live-birth prevalence:** ~1:8,000–1:16,000, reflecting massive fetal loss (spontaneous abortion) of severely affected conceptuses between conception and term ([PMC10137117](https://pmc.ncbi.nlm.nih.gov/articles/PMC10137117/)).
- Regional Orphanet-cited birth prevalence figures: 1–5/10,000 in Europe and Latin America; 6–9/10,000 in Taiwan; >1/1,000 reported in Japan ([Orphanet](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Lng=GB&Expert=2162)).

**Inheritance pattern (for nonsyndromic/SHH-pathway HPE):** **Autosomal dominant** with markedly **incomplete penetrance** and **extremely variable expressivity** — the hallmark genetic feature of this disorder. "Only about one-third of SHH pathogenic-variant carriers develop overt HPE," with the remainder showing microforms or apparently normal phenotype ([PMC10137117](https://pmc.ncbi.nlm.nih.gov/articles/PMC10137117/)). Rare autosomal recessive (*STIL*) and X-linked (*STAG2*, *SMC1A*) forms exist for specific genes outside the core SHH/ZIC2/SIX3/TGIF1 group.

**Penetrance:** Incomplete; empiric sibling recurrence data (from GeneReviews) for a parent known to carry a pathogenic variant: approximately 20% risk of overt HPE, 15% risk of microform-only phenotype, and 15% chance of apparently normal phenotype in offspring who inherit the variant — figures that must be communicated carefully in genetic counseling given their inherent imprecision.

**Expressivity:** Highly variable, both between and within families; documented range from cyclopia/alobar HPE to an entirely normal-appearing, sometimes "intellectually gifted," carrier relative.

**Genetic anticipation:** Not a recognized feature of SHH-HPE (not a repeat-expansion disorder).

**Germline mosaicism:** Documented in some HPE families, an important consideration when counseling apparently non-mosaic, phenotypically normal parents of a de novo-appearing proband — recurrence risk is not zero even when parental testing is negative.

**Founder effects / consanguinity:** No major SHH-specific founder mutation is broadly established in the literature reviewed here; consanguinity is more relevant to the rare autosomal recessive causes of syndromic HPE (e.g., Smith-Lemli-Opitz syndrome, *DHCR7*) than to dominant SHH-pathway HPE.

**Carrier frequency:** Not meaningfully defined for a dominant, highly penetrant-when-severe disorder in the way it is for recessive conditions; population allele frequency of SHH loss-of-function variants is expected to be very low given strong purifying selection (dosage sensitivity/haploinsufficiency).

**Population demographics:** No strong, consistently replicated ethnic/geographic predilection for SHH-specific HPE beyond the population-level birth-prevalence variation noted above (with Japan and Taiwan reporting higher observed birth prevalence than Europe/Latin America — the reasons for this variation, whether ascertainment, environmental, or genetic-background related, are not firmly established in the sources reviewed).
**Sex ratio:** No strong sex bias is established for autosomal dominant SHH-pathway HPE (in contrast to the rare X-linked forms, where affected probands are exclusively female, consistent with presumed male lethality).

---

## 10. Diagnostics

**Clinical/imaging tests:**
- **Prenatal ultrasound:** can detect severe (alobar, semilobar) HPE from the first trimester, showing absent interhemispheric fissure, fused/distorted choroid plexuses, fused thalami, and midline facial anomalies; the **"snake under the skull" Doppler sign** (anterior displacement of the anterior cerebral artery beneath the frontal bone) supports a diagnosis of mild lobar HPE. Milder forms are frequently missed prenatally.
- **Fetal MRI:** second-line confirmatory study for suspected cases.
- **Postnatal MRI** is the imaging modality of choice for definitive subtype classification and detection of associated anomalies; interpretation by a reviewer experienced with HPE subtyping is important to avoid misclassifying related-but-distinct entities (isolated callosal dysgenesis, arrhinencephaly, isolated pituitary dysgenesis) as HPE.

**Genetic testing (recommended sequential approach, per GeneReviews):**
1. **Chromosome analysis** — karyotype (if trisomy 13/18/triploidy is suspected clinically) and/or **chromosomal microarray (CMA)** (detects pathogenic CNVs in ~10% of cases).
2. **Multigene HPE panel** at minimum including *SHH*, *ZIC2*, *SIX3* (± *TGIF1*, *GLI2*, *PTCH1*, *CDON*, *FGF8*, *FGFR1*, *DISP1*, others).
3. **Exome sequencing** (± exome-based CNV/array analysis for multiexon deletions/duplications) if panel testing is non-diagnostic — a recent exome study cited a **22% diagnostic yield** in previously unresolved cases.
4. Targeted single-gene sequencing when a specific syndromic diagnosis (e.g., Smith-Lemli-Opitz) is clinically suspected.

**Biochemical/laboratory testing:** For suspected Smith-Lemli-Opitz syndrome (a key syndromic HPE differential), elevated 7-dehydrocholesterol / reduced cholesterol on sterol analysis supports the diagnosis pending *DHCR7* sequencing.

**Differential diagnosis:**
- Chromosomal HPE (trisomy 13 — the single most common overall cause of the HPE phenotype).
- Syndromic monogenic HPE: **Smith-Lemli-Opitz syndrome** (*DHCR7*, cholesterol-synthesis defect), **Kallmann syndrome type 2 / FGFR1-related** disorders (including Hartsfield syndrome: HPE + ectrodactyly + cleft lip/palate), **Steinfeld syndrome** (*CDON*), **Stromme syndrome** (*CENPF*, ciliopathy), **CNOT1-related (Vissers-Bodmer) syndrome**.
- Other non-HPE midline brain malformations that can be misdiagnosed as HPE (isolated septo-optic dysplasia, isolated agenesis of the corpus callosum, isolated arrhinencephaly) — correct subtyping is important since recurrence-risk counseling differs substantially.

**Screening:** No population-based newborn screening exists for HPE (it is a structural malformation, not a metabolic disorder detectable on standard newborn screening panels). Once a familial pathogenic variant is identified, **prenatal diagnosis** (chorionic villus sampling/amniocentesis for targeted variant testing) and **preimplantation genetic testing (PGT)** are available and have been reported in the literature, including an early NEJM report of preimplantation diagnosis for a familial SHH mutation ([NEJM 2003](https://www.nejm.org/doi/full/10.1056/NEJMoa022652)).

---

## 11. Outcome / Prognosis

**Survival/mortality (aggregate HPE-spectrum data):**
- **24-hour mortality:** ~33% across all HPE subtypes combined.
- **1-month mortality:** ~58%.
- **1-year survival:** ~29% overall (heavily weighted by the most severe alobar cases; survival is substantially better in lobar/MIHV/microform disease).
- Non-syndromic, euploid (normal-karyotype) HPE has meaningfully better survival than syndromic or chromosomally abnormal HPE.
- A described cohort of surviving adolescents/adults was ~50% semilobar variant, reflecting improved long-term survival in less severe subtypes with modern diagnostic and supportive care ([PMC10137117](https://pmc.ncbi.nlm.nih.gov/articles/PMC10137117/)).

**Morbidity/function:**
- Developmental delay is present in virtually all individuals with structural (imaging-positive) HPE, though severity spans from profound (alobar) to comparatively mild (lobar/MIHV).
- Approximately **60% of adolescent/adult alobar/semilobar survivors** are non-ambulatory and non-verbal with severe global impairment.
- Milder (lobar, MIHV) forms permit independent or assisted ambulation and, in some cases, functional speech; individuals are more often diagnosed later, upon emergence of developmental delay, seizures, or a movement disorder rather than at birth.

**Complications:** hydrocephalus (16–40%), refractory or well-controlled seizures (~50% of cases), central diabetes insipidus (~70% of classic/structural HPE), anterior hypopituitarism (5–10%), feeding dysfunction/aspiration risk (majority of alobar/semilobar patients require gastrostomy), gastroesophageal reflux, spasticity/dystonia-related orthopedic complications (contractures, hip dislocation, scoliosis).

**Prognostic factors:** HPE subtype/severity grade (alobar > semilobar > lobar/MIHV > microform) is the dominant prognostic determinant; euploidy vs. chromosomal/syndromic etiology; presence/absence of hydrocephalus; degree of hypothalamic non-separation (correlates with diabetes insipidus severity).

---

## 12. Treatment

There is **no disease-modifying or curative therapy** for SHH-HPE; management is exclusively **supportive, multidisciplinary, and complication-directed**.

**Pharmacotherapy (symptomatic/supportive):**
- **Desmopressin acetate** (synthetic vasopressin analog) for central diabetes insipidus — "the treatment of choice," typically dosed 10–40 µg/day in 2–3 divided doses in symptomatic patients (MAXO: pharmacotherapy, `NCIT:C15986`; specific agent CHEBI desmopressin).
- Hormone replacement for other pituitary axis deficiencies (levothyroxine for central hypothyroidism, hydrocortisone for ACTH deficiency, growth hormone for GH deficiency).
- Anticonvulsant pharmacotherapy for seizures (agent selection individualized; no HPE-specific anticonvulsant regimen is established).
- Antispasmodic/antispastic agents (oral baclofen/tizanidine-class agents) and **intramuscular botulinum toxin** injections for spasticity/dystonia management.
- Pharmacologic acid-suppression/prokinetic therapy for gastroesophageal reflux.

**Surgical/interventional:**
- **Ventriculoperitoneal shunt placement** for hydrocephalus (MAXO:0000004 surgical procedure).
- **Gastrostomy tube placement** — used in the majority of alobar/semilobar HPE patients to secure safe nutrition, reduce aspiration risk, and reduce hospitalization burden; **Nissen fundoplication** or transpyloric feeding for severe reflux.
- Craniofacial/plastic surgical repair of cleft lip/palate and other craniofacial anomalies.
- Orthopedic surgery for refractory contractures, hip dislocation, or scoliosis.

**Rehabilitative/supportive care:**
- Physical and occupational therapy (MAXO:0000011 physical therapy) to prevent/manage contractures and movement-disorder complications.
- Speech-language therapy for feeding/swallowing dysfunction and communication support in higher-functioning individuals.
- Detailed ophthalmologic and audiologic (hearing) evaluation and management.
- Neuropsychological assessment and psychological/psychiatric intervention (ADHD, learning disability, anxiety, depression) in higher-functioning microform/lobar-spectrum individuals.
- Genetic counseling (MAXO:0000079) is a core recommended component of care for the family, given the recurrence-risk complexity described in §9.

**Experimental/advanced therapeutics:** No SHH-HPE-specific gene therapy, cell therapy, or targeted molecular therapeutic is in active clinical development based on the sources reviewed; targeted searches of recent literature and ClinicalTrials.gov did not surface disease-modifying trials for HPE as of this writing — interventional trials registered under "holoprosencephaly" are predominantly natural-history/registry studies or trials of standard supportive interventions (e.g., anticonvulsants, feeding interventions) rather than SHH-pathway-targeted molecular therapies. This is consistent with the fundamental biological barrier that the causal lesion (failed embryonic midline patterning) occurs before pregnancy is typically recognized, making a postnatal molecular "fix" of the structural malformation implausible with current technology; therapeutic research in this space (to the extent any exists) would more plausibly target the SHH pathway pharmacologically in genetically at-risk pregnancies pre-conception or very early gestation, which is not an established or ethically straightforward intervention.

**Treatment strategy:** Management follows a **complication-driven, multidisciplinary team model** (genetics, neurology, neurosurgery, endocrinology, gastroenterology, ophthalmology, otolaryngology, plastic/craniofacial surgery, orthopedics, physiatry, psychology/psychiatry) rather than a fixed staged algorithm, individualized to HPE subtype and complication profile.

---

## 13. Prevention

**Primary prevention:**
- **Genetic counseling and family variant testing** once a proband's causal SHH (or other HPE-gene) variant is identified — testing of apparently unaffected parents is essential given reduced penetrance, since "the family history of some individuals diagnosed with HPE may appear to be negative because of reduced penetrance and failure to recognize the disorder in family members" ([GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK1530/)).
- **Prenatal diagnosis** (CVS/amniocentesis with targeted familial variant testing) once the familial pathogenic variant is known.
- **Preimplantation genetic testing (PGT)** for known familial SHH variants has been clinically implemented ([NEJM 2003](https://www.nejm.org/doi/full/10.1056/NEJMoa022652)).
- **Glycemic control in pregestational diabetic pregnancies** — given the strong, modifiable association between poor glycemic control and HPE risk, optimized preconception and early-pregnancy glucose control is a plausible primary-prevention lever, though this is inferential from the epidemiologic association rather than an intervention specifically validated to reduce HPE incidence in the sources reviewed.
- **Avoidance of alcohol use in pregnancy**, standard general teratogen-avoidance counseling (retinoic acid/vitamin A excess, known teratogenic medications).
- **Periconceptional folic acid supplementation** — plausibly protective per limited epidemiologic data, though evidence strength is lower than for neural tube defects; reasonable to recommend as standard preconception care regardless.

**Secondary prevention (early detection):**
- Routine anatomy-survey obstetric ultrasound (typically 18–22 weeks) is the principal population-level detection mechanism for structural (non-microform) HPE; earlier first-trimester detection is possible for severe forms.
- Focused clinical craniofacial examination of "unaffected" parents/siblings of an HPE proband to detect subtle microform features (single central incisor, hypotelorism, hyposmia) that would otherwise be overlooked.

**Genetic counseling — critical practice point:** Counseling language should be carefully chosen; the literature explicitly recommends **avoiding stigmatizing terms such as "not viable," "incompatible with life," or "vegetative,"** given the genuine phenotypic range (including surviving, communicative individuals with milder HPE subtypes) and should provide balanced, evidence-based prognostic information with referral to a genetic counselor or clinical geneticist.

**Tertiary prevention:** Standard complication-prevention measures embedded in the management plan above (aspiration-precaution feeding strategies/gastrostomy to prevent recurrent aspiration pneumonia, shunt surveillance to prevent hydrocephalus-related injury, endocrine surveillance to prevent undiagnosed adrenal crisis or severe hypothyroidism, orthopedic surveillance to prevent hip dislocation/severe scoliosis).

---

## 14. Other Species / Natural Disease

**Taxonomy of naturally/experimentally affected species:** Sheep (*Ovis aries*, NCBITaxon:9940), goats, and cattle (*Bos taurus*, NCBITaxon:9913) are documented to develop cyclopia/HPE-spectrum craniofacial-CNS malformations.

**Natural/environmentally induced disease:**
- The classic natural-disease model is **epidemic cyclopia/HPE among lambs on western U.S. sheep ranches**, traced to maternal grazing on ***Veratrum californicum*** during a narrow gestational window (days 13–14 post-conception in sheep) — "Veratrum californicum fed to ewes on the 13th and 14th days after conception is capable of producing the anomaly" ([54 Veratrum-Induced Placental Dysplasia in Sheep, USDA ARS](https://www.ars.usda.gov/ARSUserFiles/oc/np/PoisonousPlants/Fall2012/sheep.pdf)).
- The causative teratogens are steroidal jerveratrum alkaloids, principally **cyclopamine**, which directly inhibits Hedgehog pathway signal transduction (a direct SMO antagonist) — the historical discovery that established the mechanistic link between Hedgehog pathway inhibition and holoprosencephaly.
- Sporadic **veterinary case reports** document naturally occurring holoprosencephaly/synophthalmia in domestic cattle — e.g., a Holstein-cross calf with "synophthalmia, holoprosencephaly, absence of optic chiasma, hypoplastic maxilla, curved mandibles, arrhinia and dental pad agenesis" ([Synophthalmia in a Holstein cross calf, PMC4300002](https://pmc.ncbi.nlm.nih.gov/articles/PMC4300002/)).
- Comparative musculoskeletal analysis of cebocephalic and cyclopic lamb heads has been used to illuminate normal-vs-abnormal craniofacial developmental biology relevant to human pathology ([*Sci Rep* 2018](https://www.nature.com/articles/s41598-018-37735-9)).

**Orthologous gene/comparative biology:** *Shh* is highly conserved across vertebrates (mouse, chick, zebrafish, sheep, human), and the ventral-forebrain-patterning function of the pathway is deeply evolutionarily conserved, underpinning the strong translational validity of animal Hedgehog-pathway models for human HPE (see §15).

**Zoonotic potential:** None — HPE is a non-transmissible developmental malformation, not an infectious disease; there is no zoonotic dimension.

---

## 15. Model Organisms

**Mouse (*Mus musculus*, NCBITaxon:10090) — the primary genetic model:**
- **Complete Shh-null (*Shh*−/−) mice** display severe, essentially "worst-case" HPE-spectrum phenotypes, including cyclopia and single median telencephalic vesicle, phenocopying the most severe human alobar HPE/cyclopia end of the spectrum.
- **Heterozygous *Shh*+/− mice** are, notably, largely phenotypically normal at baseline — directly modeling the incomplete penetrance seen in human heterozygous carriers — but develop overt HPE-spectrum phenotypes when combined with a **second genetic hit** (e.g., *Gas1*−/− background) or an **environmental insult** (prenatal ethanol exposure), providing direct experimental proof of the multi-hit/threshold model of human HPE pathogenesis: "single allele mutations in the Hh pathway genes Sonic Hedgehog (SHH) and GLI2 cause holoprosencephaly with extremely variable phenotypic penetrance in humans," recapitulated by combinatorial mouse genetics.
- ***Disp1*-null and *Smo*-null mouse embryos** exhibit a single telencephalic vesicle and cyclopia, confirming that loss of ligand *release* (Disp1) or ligand *transduction* (Smo) each independently phenocopies loss of the ligand itself.
- ***Gli2*-null and *Gli2*+/− mice**, alone and combined with ethanol exposure, model the GLI2-associated human HPE phenotype and the gene–environment interaction described in §2/§6 (PMC3929747).
- ***Cdon*-mutant mice*** combined with prenatal ethanol exposure produce HPE that can be rescued by reduced *Ptch1* gene dosage — a genetic-rescue experiment directly demonstrating pathway-level dosage compensation as a therapeutic-relevant principle (PMC3823703).
- Ectopic/gain-of-function Shh signaling experiments (elevated ventral signaling encroaching dorsally) impair telencephalic dorsal midline development via Fgf8 upregulation, illustrating that both loss and ectopic gain of pathway activity disrupt normal midline patterning — relevant to understanding the full mechanistic landscape even though loss-of-function is the dominant human-disease-causing direction (PMID:17468181).

**Sheep (*Ovis aries*) — natural/pharmacologically-induced teratogenic model:** described in §14; historically the model system that led to discovery of the Hedgehog pathway's role in mammalian ventral forebrain/facial patterning via cyclopamine.

**Zebrafish (*Danio rerio*, NCBITaxon:7955):** Zebrafish hedgehog-pathway mutants (e.g., loss of *grk3*) produce "stereotypical shh-deficient developmental phenotypes, such as cyclopia," useful for high-throughput developmental and small-molecule screening given rapid ex utero development and optical transparency. (Zebrafish *ptch1*-mutant models are more extensively used for SHH-pathway-driven medulloblastoma — a related but oncogenic, gain-of-function application of the same pathway — rather than developmental HPE modeling specifically.)

**Model characteristics — recapitulation and limitations:**
- Mouse *Shh*/pathway-gene models recapitulate the core structural (cyclopia, single ventricle) and, in combinatorial/hypomorphic allelic series, the graded severity spectrum and incomplete penetrance of human HPE with high fidelity, making mouse genetics the dominant and most translationally informative model system for this disease.
- A key limitation: full *Shh*-null mice model only the most extreme end of the human spectrum; capturing the clinically most common and counseling-relevant **microform/reduced-penetrance** end of the spectrum has required more sophisticated combinatorial (second-hit) or environmentally-sensitized allelic models rather than simple heterozygous mutants alone, since simple *Shh*+/− mice are typically phenotypically unremarkable.
- Human forebrain organoid/iPSC-based models represent an emerging but, per the literature surveyed here, still comparatively less-developed complementary system for directly studying patient-derived SHH variant effects on human ventral telencephalic patterning in vitro.

**Resources:** MGI (Mouse Genome Informatics) for *Shh*, *Gli2*, *Ptch1*, *Cdon*, *Gas1*, *Disp1*, *Smo* allele/phenotype records; ZFIN for zebrafish hedgehog-pathway alleles; IMPC/KOMP for systematic knockout phenotyping resources.

---

## Summary of Key Ontology Term Suggestions

| Category | Term | ID |
|---|---|---|
| Disease | Holoprosencephaly | MONDO:0016296 |
| Disease (SHH-specific) | Holoprosencephaly 3 | OMIM:142945 |
| Gene | SHH | HGNC:10848 |
| Gene | GLI2 | HGNC:4318 |
| Gene | PTCH1 | HGNC:9585 |
| Gene | ZIC2 | HGNC:12873 |
| Gene | SIX3 | HGNC:10891 |
| Gene | TGIF1 | HGNC:11776 |
| Gene | GAS1 | HGNC:4166 |
| Gene | CDON | HGNC:24187 |
| Phenotype | Alobar holoprosencephaly | HP:0007169 |
| Phenotype | Cyclopia | HP:0000531 |
| Phenotype | Hypotelorism | HP:0000601 |
| Phenotype | Solitary median maxillary central incisor | HP:0006315 |
| Phenotype | Central diabetes insipidus | HP:0000873 |
| Phenotype | Seizures | HP:0001250 |
| Phenotype | Anosmia | HP:0000458 / HP:0004408 |
| Biological process | Smoothened signaling pathway | GO:0007224 |
| Biological process | Telencephalon development | GO:0021537 |
| Cellular component | Non-motile primary cilium | GO:0031513 |
| Anatomy | Forebrain | UBERON:0001890 |
| Anatomy | Pituitary gland | UBERON:0000007 |
| Treatment | Pharmacotherapy | NCIT:C15986 |
| Treatment | Physical therapy | MAXO:0000011 |
| Treatment | Genetic counseling | MAXO:0000079 |
| Treatment | Surgical procedure | MAXO:0000004 |

---

Sources:
- [Holoprosencephaly Overview - GeneReviews - NCBI - NIH](https://www.ncbi.nlm.nih.gov/books/NBK1530/)
- [Holoprosencephaly: Review of Embryology, Clinical Phenotypes, Etiology and Management, PMC10137117](https://pmc.ncbi.nlm.nih.gov/articles/PMC10137117/)
- [The unfolding clinical spectrum of holoprosencephaly due to mutations in SHH, ZIC2, SIX3 and TGIF genes, EJHG](https://www.nature.com/articles/ejhg201070)
- [Mutations in the human Sonic Hedgehog gene cause holoprosencephaly, Nature Genetics](https://www.nature.com/articles/ng1196-357)
- [Sonic hedgehog (SHH) mutation in patients within the spectrum of holoprosencephaly, ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0387760409000825)
- [Preimplantation Diagnosis for Sonic Hedgehog Mutation Causing Familial Holoprosencephaly, NEJM](https://www.nejm.org/doi/full/10.1056/NEJMoa022652)
- [Mutational Spectrum of the Sonic Hedgehog Gene in Holoprosencephaly, Human Molecular Genetics](https://academic.oup.com/hmg/article/8/13/2479/651151)
- [Clinical utility gene card for: Holoprosencephaly, PMC3039493](https://ncbi.nlm.nih.gov/pmc/articles/PMC3039493)
- [OMIM #236100 Holoprosencephaly 1](https://omim.org/entry/236100)
- [OMIM #142945 Holoprosencephaly 3](https://omim.org/entry/142945)
- [OMIM #610828 Holoprosencephaly 7](https://omim.org/entry/610828)
- [Orphanet: Holoprosencephaly](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Lng=GB&Expert=2162)
- [Holoprosencephaly, Orphanet Journal of Rare Diseases](https://link.springer.com/article/10.1186/1750-1172-2-8)
- [Epidemiological characteristics of holoprosencephaly in China, 2007-2014, PMC6553724](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6553724/)
- [Aberrant forebrain signaling during early development underlies HPE and coloboma, ScienceDirect](https://www.sciencedirect.com/science/article/pii/S092544391000205X)
- [The Role of Sonic Hedgehog in Human Holoprosencephaly and Short-Rib Polydactyly Syndromes, PMC8468456](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8468456/)
- [Rescue of Holoprosencephaly in Fetal Alcohol-Exposed Cdon Mutant Mice, PMC3823703](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3823703/)
- [The Teratogenic Effects of Prenatal Ethanol Exposure Are Exacerbated by Sonic Hedgehog or Gli2 Haploinsufficiency, PMC3929747](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3929747/)
- [Frontiers: The Role of Sonic Hedgehog Pathway in CNS Development and Neurodegenerative Diseases](https://www.frontiersin.org/journals/molecular-biosciences/articles/10.3389/fmolb.2021.711710/full)
- [JCI: Pathogenesis of holoprosencephaly](https://www.jci.org/articles/view/38937)
- [Gas1 is a modifier for holoprosencephaly and genetically interacts with sonic hedgehog, PMID:17525797](https://pubmed.ncbi.nlm.nih.gov/17525797/)
- [OMIM *139185 GAS1](https://omim.org/entry/139185)
- [Endocrine disorders associated with holoprosencephaly, PMID:16355806](https://pubmed.ncbi.nlm.nih.gov/16355806/)
- [Solitary median maxillary central incisor (SMMCI) syndrome, PMC1464380](https://pmc.ncbi.nlm.nih.gov/articles/PMC1464380/)
- [OMIM #147250 Solitary Median Maxillary Central Incisor](https://www.omim.org/entry/147250)
- [SHH curation results for Dosage Sensitivity, ClinGen](https://search.clinicalgenome.org/kb/gene-dosage/HGNC:10848)
- [holoprosencephaly 5 MONDO:0012322, Monarch Initiative](https://monarchinitiative.org/MONDO:0012322)
- [54 Veratrum-Induced Placental Dysplasia in Sheep, USDA ARS](https://www.ars.usda.gov/ARSUserFiles/oc/np/PoisonousPlants/Fall2012/sheep.pdf)
- [Synophthalmia in a Holstein cross calf, PMC4300002](https://pmc.ncbi.nlm.nih.gov/articles/PMC4300002/)
- [Musculoskeletal study of cebocephalic and cyclopic lamb heads, Scientific Reports](https://www.nature.com/articles/s41598-018-37735-9)
- [Holoprosencephaly - Child Neurology Foundation](https://www.childneurologyfoundation.org/disorder/holoprosencephaly/)