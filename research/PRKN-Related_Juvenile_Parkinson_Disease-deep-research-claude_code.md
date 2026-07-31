---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-31T16:46:44.368396'
end_time: '2026-07-31T16:51:50.724886'
duration_seconds: 306.36
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: PRKN-Related Juvenile Parkinson Disease
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
  web_search_requests: 13
  num_turns: 16
  total_cost_usd: 1.5087796999999998
  session_id: 1ff1ab7e-d42a-5ad6-b222-89444922f8c7
  stop_reason: end_turn
citation_count: 42
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** PRKN-Related Juvenile Parkinson Disease
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **PRKN-Related Juvenile Parkinson Disease** covering all of the
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

# PRKN-Related Juvenile/Early-Onset Parkinson Disease — Comprehensive Research Report

## 1. Disease Information

**Overview.** PRKN-related Parkinson disease (historically "autosomal recessive juvenile parkinsonism," AR-JP, or PARK2) is a monogenic, autosomal recessive form of early-onset parkinsonism caused by biallelic loss-of-function variants in *PRKN* (formerly *PARK2*), which encodes the E3 ubiquitin ligase parkin. It is the most common known monogenic cause of early-onset Parkinson disease (EOPD) [GeneReviews, NBK1478](https://www.ncbi.nlm.nih.gov/books/NBK1478/). The clinical designation has shifted from "juvenile parkinsonism" (onset <21 years) to the broader **PARK-PRKN / PRKN-Type Early-Onset Parkinson Disease**, since the true age range at onset is 1–84 years with a median of 31 years [GeneReviews, NBK1478](https://www.ncbi.nlm.nih.gov/books/NBK1478/).

**Key identifiers:**
- **OMIM phenotype:** #600116 — Parkinson Disease 2, Autosomal Recessive Juvenile; PARK2 [OMIM #600116](https://omim.org/entry/600116)
- **OMIM gene:** *602544 — Parkin RBR E3 Ubiquitin Protein Ligase; PRKN [OMIM *602544](https://www.omim.org/entry/602544)
- **MONDO:** MONDO:0010820 — autosomal recessive juvenile Parkinson disease 2 [ClinGen curation](https://search.clinicalgenome.org/kb/conditions/MONDO:0010820)
- **Gene symbol:** PRKN (previously PARK2); located at chromosome 6q26, one of the largest human genes (~1.38 Mb)
- **ICD-11:** 8A00.0 (Parkinson disease), with genetic-etiology extension coding; **ICD-10:** G20
- **MeSH:** Parkinson Disease (D010300); Parkinsonian Disorders

**Synonyms:** Autosomal recessive juvenile parkinsonism (AR-JP); Parkinson disease 2; PARK2; Parkin-type early-onset Parkinson disease (PARK-PRKN, in the current Mendelian nomenclature used by GeneReviews/MDSGene).

**Data provenance:** Information is derived from aggregated disease-level resources (OMIM, GeneReviews, ClinGen, MDSGene, Orphanet-linked literature reviews and meta-analyses of published case series and cohort studies), not from a single-patient EHR source.

---

## 2. Etiology

**Disease causal factor:** PRKN-PD is caused exclusively by **biallelic (homozygous or compound heterozygous) pathogenic variants in *PRKN*** that abolish or severely reduce parkin E3 ubiquitin ligase activity. It is a purely genetic/mechanistic (loss-of-function) disease with no known infectious cause; environmental exposures are not established causal factors, though they are studied as modifiers in idiopathic PD generally.

**Genetic risk factors:**
- **Causal (biallelic) variants:** Deletions/duplications of whole exons account for roughly half of pathogenic alleles; among 159 disease-causing genotypes reviewed, 45.3% were structural variants (large deletions/duplications/indels/rearrangements), 30.2% were loss-of-function SNVs, and 20.8% were missense variants [Frontiers, Genetic Analysis of EOPD, Eastern China](https://www.frontiersin.org/journals/aging-neuroscience/articles/10.3389/fnagi.2022.849462/full). In some series, copy-number variants account for up to 60% of PRKN-PD cases.
- **Founder effects:** A common **exon 2 duplication** identified in European populations was absent from non-European populations in gnomAD structural-variant data, suggesting a founder effect [Frontiers, Heterozygous PRKN Variants CHRIS Cohort](https://www.frontiersin.org/journals/neurology/articles/10.3389/fneur.2021.706145/full).
- **Heterozygous carriage:** Population carrier frequency of PRKN pathogenic variants is estimated between 0.17% and 3.7% depending on population and ascertainment method. A large case-control genetic study found **heterozygous PRKN mutations are common in the population but do not confer significantly increased Parkinson disease risk on their own** [Brain, Heterozygous PRKN mutations](https://academic.oup.com/brain/article/145/6/2077/6595863); a modest susceptibility effect combined with additional genetic or environmental risk factors cannot be excluded [GeneReviews, NBK1478](https://www.ncbi.nlm.nih.gov/books/NBK1478/).
- **Modifier genes:** No robustly validated modifier loci for PRKN-PD severity/onset are established; genotype–phenotype correlation across the >200 reported PRKN pathogenic variants has not been firmly established, as symptoms vary substantially even among individuals with the same genotype [Frontiers, Genotype-Phenotype Correlations Monogenic PD](https://www.frontiersin.org/journals/neurology/articles/10.3389/fneur.2021.648588/full).

**Environmental risk/protective factors:** Not specifically established for PRKN-PD; the broader PD literature implicates pesticide exposure, rural living, and traumatic brain injury as risk factors and caffeine/smoking as inversely associated (epidemiologic, not causal-confirmed) — these associations have not been specifically tested in PRKN-genotyped cohorts and should not be assumed to transfer directly.

**Gene–environment interactions:** No PRKN-specific gene–environment interaction studies were identified in this search; mechanistically, since parkin loss impairs clearance of oxidatively damaged mitochondria, environmental oxidative/mitochondrial stressors (e.g., rotenone, MPTP-like toxins) are plausible severity modifiers based on cellular models, but this is inferential rather than directly demonstrated in PRKN-PD patients.

---

## 3. Phenotypes

**Cardinal motor signs** (symptoms/signs; HPO/OMIM/GeneReviews-sourced): bradykinesia, resting tremor, rigidity, and postural instability — the core parkinsonian tetrad [OMIM Clinical Synopsis #600116](https://www.omim.org/clinicalSynopsis/600116).

| Phenotype | Category | Frequency/notes | Suggested HPO term (verify via OAK before curation) |
|---|---|---|---|
| Bradykinesia | Motor sign | Cardinal feature | HP:0002067 Bradykinesia |
| Resting tremor | Motor sign | Cardinal, common presenting sign | HP:0002322 Resting tremor |
| Rigidity | Motor sign | Cardinal feature | HP:0002063 Rigidity |
| Postural instability | Motor sign | Cardinal, typically later stage | HP:0002172 Postural instability |
| Lower-limb dystonia | Motor sign | Presenting sign in ~66% of individuals; may be isolated for years before parkinsonism | HP:0001332 Dystonia |
| Hyperreflexia | Motor sign | Present in ~50% of affected individuals; distinguishes from idiopathic PD | HP:0001347 Hyperreflexia |
| Levodopa-induced dyskinesia | Treatment-related sign | Higher likelihood than in non-genetic parkinsonism; early and sustained | HP:0002346 (Dyskinesia — verify) |
| Diurnal fluctuation / sleep benefit | Motor sign | Symptoms improve after sleep, worsen through the day — a distinguishing clinical clue | (no precise HPO; describe in notes) |
| Autonomic dysfunction (constipation, urinary frequency, sexual dysfunction, orthostatic hypotension) | Autonomic/laboratory-adjacent sign | ~53% of individuals | HP:0002019 Constipation; HP:0000020 Urinary incontinence; HP:0001278 Orthostatic hypotension |
| Depression / anxiety | Behavioral | Frequent | HP:0000716 Depression; HP:0000739 Anxiety |
| Cognitive impairment / dementia | Behavioral/cognitive | Uncommon; dementia in <3%, no more frequent than general population | HP:0000726 (Dementia — rare in this disease) |
| Preserved olfaction | Sign (distinguishing, absence of typical feature) | "Well-preserved sense of smell" — contrasts with idiopathic PD hyposmia | HP:0004408 (Olfactory dysfunction — typically ABSENT here) |

Source for the frequency and clinical-distinguishing data: [GeneReviews, NBK1478](https://www.ncbi.nlm.nih.gov/books/NBK1478/); [MalaCards](https://www.malacards.org/card/parkinson_disease_2_autosomal_recessive_juvenile).

**Onset:** Median 31 years, range 1–84 years; onset is usually before age 40; juvenile onset (<20 years) is comparatively rare but gives the disease its historical name.

**Severity/progression:** Slowly progressive — disease duration >60 years has been reported, substantially slower progression than idiopathic PD. Freezing of gait, postural deformities, and motor fluctuations may emerge in later stages, but dementia typically does not develop.

**Quality of life impact:** Levodopa-induced dyskinesia and early motor fluctuations are the dominant drivers of disability given the very long disease duration; autonomic symptoms (constipation, urinary, orthostatic) and mood symptoms (depression/anxiety) contribute meaningfully to quality of life over decades of disease, though formal EQ-5D/SF-36 PRKN-specific QoL studies were not identified in this search.

---

## 4. Genetic/Molecular Information

**Causal gene:** PRKN (HGNC symbol PRKN, previously PARK2), OMIM *602544, chromosome 6q26. PRKN spans ~1.38 Mb of genomic DNA with 12 exons, making it one of the largest genes in the human genome and overlapping the common fragile site FRA6E — a feature thought to predispose to the high rate of exonic structural rearrangements [GeneReviews, NBK1478](https://www.ncbi.nlm.nih.gov/books/NBK1478/).

**Pathogenic variant spectrum:**
- Pathogenic variants have been described across all 12 exons.
- **Structural/copy-number variants (exon deletions/duplications)** are the single largest class (~45–60% depending on cohort) [Frontiers EOPD China](https://www.frontiersin.org/journals/aging-neuroscience/articles/10.3389/fnagi.2022.849462/full); complex structural variants including **exon inversions** can be invisible to standard exome sequencing and require targeted deletion/duplication or long-read sequencing methods to detect [Brain Communications, Levodopa-responsive dystonia from PRKN exon inversion](https://academic.oup.com/braincomms/article/3/3/fcab197/6364893).
- **Loss-of-function SNVs** (nonsense, frameshift, canonical splice-site): ~30%.
- **Missense variants:** ~21%, often clustering in the RING/IBR zinc-binding domains where they destabilize protein folding.
- Detection: sequence analysis alone detects ~39% of pathogenic alleles; gene-targeted deletion/duplication testing (MLPA, quantitative PCR, long-range PCR, targeted microarray, or long-read sequencing for complex rearrangements) is required to detect the remaining ~61% — single-gene sequencing-only testing is explicitly **not recommended** as a standalone approach [GeneReviews, NBK1478](https://www.ncbi.nlm.nih.gov/books/NBK1478/); [medRxiv, long-read sequencing PRKN structural variants](https://www.medrxiv.org/content/10.1101/2024.05.02.24306523.full.pdf).

**Frequency in PD cohorts:** PRKN biallelic pathogenic variants are found in 6–12% of PD with onset <50 years, 30% of onset <30 years, and up to 42.2% of onset ≤20 years [GeneReviews, NBK1478](https://www.ncbi.nlm.nih.gov/books/NBK1478/); Central European EOPD cohorts show 2.6–9.3% prevalence of biallelic PRKN variants [GeneReviews, NBK1478](https://www.ncbi.nlm.nih.gov/books/NBK1478/).

**Functional consequence:** The great majority of PRKN pathogenic variants act through **loss of function** of the E3 ubiquitin ligase — either by truncation/instability (nonsense, frameshift, most structural variants) or catalytic/structural inactivation (missense variants, especially in zinc-coordinating RING/IBR residues) [GeneReviews, NBK1478](https://www.ncbi.nlm.nih.gov/books/NBK1478/).

**Protein domain architecture:** Parkin has an N-terminal ubiquitin-like (Ubl) domain followed by four zinc-coordinating domains: **RING0** (also called the Unique Parkin Domain, UPD — interacts with PINK1), **RING1** (E2-binding), **IBR** (in-between-RING, two zinc-binding sites required for correct folding), and **RING2** (contains the catalytic cysteine, Cys431, required for E2-mediated ubiquitin transfer) [GeneCards PRKN](https://www.genecards.org/card/PRKN); [PMC3730226, Structure of human Parkin ligase domain](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3730226/).

**Modifier genes:** None robustly established specific to PRKN-PD.

**Somatic vs. germline:** Exclusively germline in PRKN-PD (biallelic constitutional variants); no somatic mosaicism mechanism described for this disease.

**Epigenetics / chromosomal abnormalities:** No disease-defining epigenetic mechanism or large chromosomal aneuploidy is implicated; the relevant "structural variation" here is at the level of intragenic exon-level deletions/duplications/inversions rather than whole-chromosome abnormalities.

---

## 5. Environmental Information

No PRKN-PD-specific environmental, lifestyle, or infectious causal factors were identified in the literature searched. As a monogenic, fully penetrant-in-biallelic-carriers disease (see Section 9 for nuance on penetrance), environmental factors are not considered primary drivers, though — as in idiopathic PD — mitochondrial/oxidative toxicant exposure is mechanistically plausible as a severity modifier given the pathway involved (see Section 6).

---

## 6. Mechanism / Pathophysiology

**Molecular function of parkin:** Parkin is a cytosolic RBR (RING-Between-RING) E3 ubiquitin ligase central to **mitochondrial quality control (mitophagy)** and general proteasome-dependent protein degradation [GeneCards PRKN](https://www.genecards.org/card/PRKN).

**Causal chain (PINK1–Parkin mitophagy pathway):**
1. **Trigger:** Mitochondrial damage causes loss of inner-membrane potential, preventing the normal proteolytic removal of PINK1, which then accumulates and stabilizes on the outer mitochondrial membrane (OMM).
2. **Activation:** PINK1 phosphorylates pre-existing ubiquitin on OMM proteins at Ser65 and recruits/phosphorylates parkin's Ubl domain, releasing autoinhibition and activating parkin's E3 ligase activity [J Cell Biol, PINK1 phosphorylates ubiquitin to activate Parkin](https://rupress.org/jcb/article/205/2/143/37633/PINK1-phosphorylates-ubiquitin-to-activate-Parkin).
3. **Amplification:** Activated parkin ubiquitinates additional OMM proteins (e.g., **VDAC1, MFN1/2, MIRO1**) via Lys-63-linked polyubiquitin chains, which PINK1 can again phosphorylate — a feedforward amplification loop that rapidly decorates damaged mitochondria with ubiquitin [PMC9851250, Feedforward activation of PRKN/parkin](https://pmc.ncbi.nlm.nih.gov/articles/PMC9851250/).
4. **Downstream execution:** Ubiquitinated OMM proteins recruit autophagy receptors and the LC3/autophagosome machinery, marking damaged mitochondria for selective autophagic clearance (mitophagy) [PMC9763867, Parkin-PHB2 interaction links inner membrane ubiquitination to mitophagy](https://pmc.ncbi.nlm.nih.gov/articles/PMC9763867/).
5. **Disease consequence:** Loss-of-function PRKN variants abolish or impair this quality-control step. Parkin-deficient cells cannot efficiently clear depolarized/damaged mitochondria; the accumulating burden of dysfunctional mitochondria drives **chronic oxidative stress, decreased proteasome-mediated mitochondrial protein turnover, and ultimately apoptotic loss of dopaminergic neurons in the substantia nigra pars compacta (SNpc)** — the anatomic hallmark shared with idiopathic PD [Cyagen, PRKN Gene Function](https://www.cyagen.com/cyagen-lab-notes/prkn-loss-function-parkinsons-neurobiology).

**Cellular processes:** mitophagy (GO:0000422), autophagy (GO:0006914), protein polyubiquitination (GO:0000209), ubiquitin-protein transferase/E3 ligase activity (GO:0061630 or GO:0004842), mitochondrion organization (GO:0007005), apoptotic cell death of vulnerable neurons/muscle (in model systems).

**Metabolic context — differentiation-state dependence:** A key mechanistic nuance from iPSC-neuron studies: when neuronal precursors are still glycolytic early in differentiation, mitophagy is unimpaired by PRKN deficiency; but as neurons mature and become dependent on oxidative phosphorylation, mitophagy becomes severely impaired in PRKN-mutant neurons [PMC7511396, Oxidative switch drives mitophagy defects in parkin mutant patient neurons](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7511396/). This helps explain selective vulnerability of long-lived, highly oxidative dopaminergic neurons.

**Oxidative stress:** iPSC-derived PARK2 (PRKN) neurons and postmortem brain tissue show mitochondrial dysfunction, increased oxidative stress, and **α-synuclein accumulation** despite the characteristic absence of classical Lewy body pathology at autopsy in most PRKN-PD cases [PMC3546866, Mitochondrial dysfunction with oxidative stress and α-synuclein accumulation in PARK2 iPSC neurons](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3546866/). Model-organism work (Drosophila) shows that antioxidant overexpression (glutathione S-transferase) rescues dopaminergic neurodegeneration in parkin mutants, supporting oxidative stress as a major downstream driver [PMC5818410].

**Pathology (human):** Loss of dopaminergic neurons in the substantia nigra similar to idiopathic PD, but classically **without Lewy bodies** — a key neuropathological distinction, although this is not absolute across all reported cases [MalaCards; OMIM #600116](https://omim.org/entry/600116).

**Suggested ontology terms:** GO:0000422 (mitophagy), GO:0006914 (autophagy), GO:0016567 (protein ubiquitination), GO:0004842/GO:0061630 (ubiquitin-protein ligase activity), GO:0007005 (mitochondrion organization); CL:0000700 (dopaminergic neuron); all should be verified against current OBO labels before curation (per dismech OAK-verification convention).

---

## 7. Anatomical Structures Affected

**Organ/system level:** Primary — central nervous system, specifically the basal ganglia dopaminergic circuit. **Substantia nigra pars compacta (SNpc)** dopaminergic neurons are the principal site of degeneration; the nigrostriatal projection to the **striatum (caudate + putamen)** is functionally denervated, producing the parkinsonian motor syndrome. Secondary/complication-level involvement includes the autonomic nervous system (gut, bladder, cardiovascular reflexes) accounting for the autonomic phenotype cluster.

**Tissue/cell level:** Dopaminergic neurons (CL:0000700) of the SNpc are the principal vulnerable population. Note that unlike idiopathic PD, locus coeruleus noradrenergic neurons and olfactory pathways are comparatively spared (consistent with preserved olfaction being a clinical distinguishing feature).

**Subcellular level:** **Mitochondria** (outer mitochondrial membrane specifically) are the central subcellular compartment implicated, via the PINK1-parkin mitophagy pathway; also the ubiquitin-proteasome system machinery broadly. Suggested GO Cellular Component terms: mitochondrial outer membrane (GO:0005741), mitochondrion (GO:0005739).

**Localization (UBERON):** substantia nigra (UBERON:0002038), basal ganglion (UBERON:0002420), brain (UBERON:0000955), striatum (UBERON:0002435) — terms should be verified via OAK/UBERON before use.

**Lateralization:** Typically bilateral, though — as in idiopathic PD — asymmetric onset (e.g., unilateral lower-limb dystonia or tremor) is common at presentation.

---

## 8. Temporal Development

**Onset:** Median age 31 years (range 1–84 years); onset is usually before age 40. Insidious/gradual onset is typical, consistent with a slowly evolving neurodegenerative process rather than acute or subacute presentation. Lower-limb dystonia may precede overt parkinsonism by years.

**Progression:** Slowly progressive over an unusually long disease course — disease duration exceeding 60 years has been documented, substantially longer than idiopathic PD [GeneReviews, NBK1478](https://www.ncbi.nlm.nih.gov/books/NBK1478/). Motor progression rate is markedly slower than idiopathic PD. Later stages can include freezing of gait, postural deformities, and motor fluctuations, but — notably — dementia does not typically supervene even after decades, distinguishing the long-term course from idiopathic PD with dementia.

**Course pattern:** Progressive but with a characteristic **diurnal fluctuation** (symptoms worse later in the day) and **sleep benefit** (improvement after sleep) — a distinctive fluctuating component layered on the progressive baseline.

**Treatment-response pattern:** Marked, sustained levodopa responsiveness is a defining clinical feature, but with a higher-than-typical propensity for levodopa-induced dyskinesia, which becomes a dominant driver of later-stage disability/motor complications.

**Critical periods:** No formally defined developmental "critical window," but early recognition of the young-onset dystonia-parkinsonism phenotype is clinically important for genetic diagnosis and levodopa-dose optimization to minimize dyskinesia risk over a multi-decade disease course.

---

## 9. Inheritance and Population

**Inheritance pattern:** Autosomal recessive [GeneReviews, NBK1478](https://www.ncbi.nlm.nih.gov/books/NBK1478/); heterozygotes (single pathogenic variant carriers) are not considered to have a strongly increased risk of disease on their own, though a modest susceptibility effect in combination with other genetic/environmental factors cannot be excluded [Brain, Heterozygous PRKN mutations](https://academic.oup.com/brain/article/145/6/2077/6595863).

**Recurrence risk:** If both parents are confirmed heterozygous carriers, each sibling has at conception a 25% chance of being affected (biallelic), 50% chance of being an asymptomatic heterozygous carrier, and 25% chance of inheriting neither variant [GeneReviews, NBK1478](https://www.ncbi.nlm.nih.gov/books/NBK1478/).

**Penetrance:** Notably **incomplete even among biallelic carriers** — in a population cohort, while biallelic PRKN carriers were more likely overall to carry a PD diagnosis, 91.7% of biallelic carriers identified through population screening were asymptomatic, reflecting substantial incomplete penetrance or an as-yet-unelapsed disease latency [PMC8382284, Frequency of Heterozygous PRKN Variants and Penetrance, CHRIS Cohort](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8382284/).

**Expressivity:** Highly variable — no robust genotype-phenotype correlation has been established across the many different pathogenic PRKN alleles; clinical severity and symptom constellation vary substantially even for ostensibly similar genotypes [Frontiers, Genotype-Phenotype Correlations Monogenic PD](https://www.frontiersin.org/journals/neurology/articles/10.3389/fneur.2021.648588/full).

**Genetic anticipation / germline mosaicism:** Not a described feature of PRKN-PD (unlike repeat-expansion disorders).

**Founder effects:** The European exon 2 duplication is a well-documented founder allele, absent in non-European gnomAD structural-variant data [Frontiers, CHRIS Cohort](https://www.frontiersin.org/journals/neurology/articles/10.3389/fneur.2021.706145/full).

**Carrier frequency / population prevalence:** Heterozygous PRKN pathogenic variant carrier frequency is estimated at 0.17%–3.7% depending on population and methodology. A modeling study estimated genetic prevalence of PRKN-PD itself (biallelic) at approximately **24 per 100,000** in non-Japanese East Asians and **22 per 100,000** in Non-Finnish Europeans, the two highest-prevalence groups modeled (this is a preprint/medRxiv estimate and should be treated as provisional pending peer review) [medRxiv, Estimated genetic prevalence of EOPD from PRKN mutations](https://www.medrxiv.org/content/10.1101/2024.01.22.24301610v1.full).

**Consanguinity:** As an autosomal recessive disease, consanguineous unions increase the probability of homozygosity for a given PRKN variant in populations/families where consanguinity is common; this is standard AR genetics reasoning rather than a PRKN-specific finding in the sources reviewed.

**Sex ratio / geographic distribution:** No strong sex-ratio skew is reported for PRKN-PD specifically in the sources reviewed (distinct from idiopathic PD's modest male excess). Geographic/ethnic variation in variant spectrum is well documented (e.g., European exon 2 duplication founder effect; differing structural-variant vs. point-mutation ratios reported in East Asian vs. European cohorts).

---

## 10. Diagnostics

**Clinical suspicion criteria** (no formal consensus criteria exist, but diagnosis should be suspected when):
- Parkinsonism onset before ~age 40 (especially <20–30)
- Prominent lower-limb dystonia, sometimes isolated for years
- Hyperreflexia
- Slow disease progression
- Preserved olfaction (unusual for parkinsonism generally)
- Marked, sustained levodopa response, but with early/prominent dyskinesia
- Absence of dementia even after long disease duration
[GeneReviews, NBK1478](https://www.ncbi.nlm.nih.gov/books/NBK1478/)

**Genetic testing (definitive diagnosis):**
- Diagnosis requires demonstration of **biallelic pathogenic PRKN variants**.
- Sequence analysis alone detects ~39% of pathogenic alleles; **gene-targeted deletion/duplication analysis is essential** (detects the remaining ~61%, given the high rate of exonic structural rearrangements) — techniques include quantitative PCR, long-range PCR, multiplex ligation-dependent probe amplification (MLPA), and gene-targeted microarray [GeneReviews, NBK1478](https://www.ncbi.nlm.nih.gov/books/NBK1478/).
- Complex structural variants such as exon inversions can be **invisible to standard exome sequencing** and require MLPA or long-read sequencing for detection [Brain Communications, PRKN exon inversion](https://academic.oup.com/braincomms/article/3/3/fcab197/6364893); [medRxiv, long-read sequencing of PRKN structural variants](https://www.medrxiv.org/content/10.1101/2024.05.02.24306523.full.pdf).
- Recommended testing strategy: multigene panel covering PRKN plus other EOPD genes (PINK1, PARK7/DJ-1, ATP13A2, DNAJC6, FBXO7, PLA2G6, SYNJ1, VPS13C), OR comprehensive genomic testing (exome/genome sequencing) combined with dedicated CNV analysis; single-gene sequencing-only testing is explicitly discouraged as insufficient.

**Imaging:** DAT-SPECT (¹²³I-ioflupane) demonstrates the expected nigrostriatal dopaminergic deficit consistent with any dopamine-deficient parkinsonism, confirming a neurodegenerative parkinsonism versus non-degenerative mimics, but **does not distinguish PRKN-PD from idiopathic PD or other genetic forms** [AJNR, Role of DAT-SPECT in Parkinsonian Syndromes](https://www.ajnr.org/content/36/2/229).

**Emerging biomarkers:** α-synuclein seed amplification assay (SAA) in CSF is a sensitive/specific marker for Lewy body disease; because PRKN-PD classically lacks Lewy body pathology, SAA status may theoretically differ from idiopathic PD, though PRKN-specific SAA data were not identified in this search and this should be treated as a hypothesis rather than an established diagnostic fact.

**Differential diagnosis:**
- **PARK-PINK1** (PINK1-related EOPD) — the second most common monogenic EOPD cause; clinically indistinguishable from PARK-PRKN, differentiated only by molecular testing [GeneReviews, NBK1478](https://www.ncbi.nlm.nih.gov/books/NBK1478/)
- **PARK7 (DJ-1)-related parkinsonism**
- Other recessive EOPD/parkinsonism-plus genes: ATP13A2 (Kufor-Rakeb syndrome), DNAJC6, FBXO7, PLA2G6, SYNJ1, VPS13C
- Dopa-responsive dystonia (GCH1, TH, SPR mutations) — important because of phenotypic overlap with the dystonia-predominant PRKN-PD presentation

**Screening:** No population-based newborn or general screening program exists for PRKN-PD given its adult/young-adult typical onset; targeted cascade testing of at-risk relatives (once a family's causal variants are known) and reproductive-partner carrier testing (particularly with known consanguinity) are the recommended screening applications. Prenatal diagnosis and preimplantation genetic testing are available once familial variants are identified [GeneReviews, NBK1478](https://www.ncbi.nlm.nih.gov/books/NBK1478/).

---

## 11. Outcome/Prognosis

**Survival/mortality:** PRKN-PD is not directly life-shortening in the way many pediatric-onset genetic diseases are; disease duration exceeding 60 years has been documented, indicating survival compatible with a normal or near-normal lifespan, with morbidity driven by progressive motor disability rather than early mortality.

**Morbidity/function:** Long-term disability accrues from: (1) progressive core parkinsonian motor impairment (bradykinesia, rigidity, gait freezing, postural instability in later stages), and (2) treatment-related motor complications, especially **levodopa-induced dyskinesia**, which tends to appear earlier and more prominently than in idiopathic PD and becomes a major determinant of quality of life over a multi-decade disease course.

**Preserved domains:** Cognitive function is relatively preserved — dementia is rare (<3%) and, per available data, roughly comparable to general-population rates, a strikingly different long-term trajectory than idiopathic PD, where PD-associated dementia is common in advanced disease.

**Complications:** Autonomic complications (constipation, urinary dysfunction, orthostatic hypotension) and psychiatric symptoms (depression, anxiety) are frequent contributors to morbidity; falls/postural instability become relevant in advanced stages.

**Prognostic factors:** No robust genotype-specific prognostic biomarkers have been established (see Section 9, expressivity); disease duration and the emergence of dyskinesia/motor fluctuations are the dominant clinically tracked prognostic markers, managed proactively by minimizing levodopa dose above the minimum effective threshold.

---

## 12. Treatment

**Pharmacotherapy (first-line and adjunctive):**
- **Levodopa** (with peripheral decarboxylase inhibitor) — first-line; produces a "marked and sustained response," the most distinctive treatment feature of this disease [GeneReviews, NBK1478](https://www.ncbi.nlm.nih.gov/books/NBK1478/). Suggested NCIT term: NCIT:C15986 (Pharmacotherapy) as treatment_term with therapeutic_agent bound to levodopa (verify CHEBI/NCIT ID via OAK).
- Dopamine receptor agonists
- Monoamine oxidase type B (MAO-B) inhibitors
- Catechol-O-methyltransferase (COMT) inhibitors
- Amantadine
- Adenosine A2A receptor antagonists
- Anticholinergics (useful especially for dystonia-predominant presentations)
[GeneReviews, NBK1478](https://www.ncbi.nlm.nih.gov/books/NBK1478/)

**Critical dosing caution:** Because of the elevated risk of levodopa-induced dyskinesia in this population, clinicians are specifically advised to avoid levodopa doses that exceed what is needed for satisfactory clinical response [GeneReviews, NBK1478](https://www.ncbi.nlm.nih.gov/books/NBK1478/).

**Agents to avoid:** Dopamine-blocking drugs — both typical/atypical antipsychotics and dopamine-blocking antiemetics/GI agents — can exacerbate parkinsonism and should be avoided when possible [GeneReviews, NBK1478](https://www.ncbi.nlm.nih.gov/books/NBK1478/).

**Surgical/device therapy:** Deep brain stimulation (DBS) of the subthalamic nucleus (STN) or globus pallidus internus (GPi) is appropriate for individuals with disabling motor fluctuations/dyskinesia refractory to medical optimization. STN DBS's antidyskinetic effect is largely mediated through allowing reduction of dopaminergic medication dose, whereas GPi stimulation has more direct antidyskinetic effects [PMC4010755, Surgical Treatment of Dyskinesia in PD](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4010755/). Modern DBS series report ≥50% symptom reduction and roughly 4 additional hours of "ON" time daily in PD generally (not PRKN-specific figures).

**Supportive/rehabilitative care:** Physical therapy, occupational therapy, speech/voice therapy (e.g., Lee Silverman Voice Treatment), and structured exercise (aerobic, strength training, Tai Chi) are recommended; management of constipation, sleep disturbance, and orthostatic hypotension is part of routine longitudinal care.

**Experimental/advanced therapeutics:**
- **AAV9-PRKN gene replacement therapy** — preclinical: AAV9 vectors (e.g., AAV9-PK041, developed at Takeda) restore parkin expression in dopaminergic neurons and protect nigral dopaminergic neurons in 6-OHDA-lesion and α-synuclein preformed-fibril mouse models of PD [Gene Therapy (Nature), In vitro/vivo rescue of dopaminergic neurons after Parkin gene therapy](https://www.nature.com/articles/s41434-026-00599-0); [PMC12263715, Investigational Gene Therapies for PD](https://pmc.ncbi.nlm.nih.gov/articles/PMC12263715/). No completed human clinical trial specific to PRKN-PD gene replacement was identified in this search (as of this report).
- **Splice-intervention (antisense oligonucleotide) therapy** targeting specific PRKN exon-deletion genotypes has been described preclinically as a strategy to restore an in-frame, functional transcript for particular structural variants [PMC7582384, Splice Intervention Therapy for AR Juvenile PD from Parkin mutations](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7582384/). Suggested therapeutic_modality: ANTISENSE_OLIGONUCLEOTIDE with aso_mechanism SPLICE_MODULATION_EXON_SKIPPING/INCLUSION depending on the specific variant targeted, once a specific clinical-stage candidate and molecular target (exon number) are identified from primary literature.

**Treatment outcomes:** Response rates to levodopa in PRKN-PD are characteristically excellent and durable relative to idiopathic PD; the principal adverse "cost" is the elevated rate of levodopa-induced dyskinesia (general PD literature: ~40% of patients affected by 4 years of levodopa use, 50–80% by 5–10 years) [PMC12583070, Levodopa-induced dyskinesia review](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12583070/); PRKN-PD patients are considered to have proportionally higher dyskinesia liability than average.

**Treatment strategy:** No PRKN-specific formal treatment algorithm/guideline distinct from general early-onset PD management was identified; the core personalized-medicine principle specific to this disease is genetic confirmation to (a) counsel patients on the expected long, dyskinesia-prone but cognitively spared disease course, (b) guide conservative levodopa titration, and (c) inform family genetic counseling.

---

## 13. Prevention

**Primary prevention:** Not applicable in the traditional sense (no modifiable environmental cause established); the relevant "primary prevention" lever is reproductive/genetic — carrier screening and reproductive counseling in families with a known proband, and prenatal/preimplantation genetic testing once familial PRKN variants are identified [GeneReviews, NBK1478](https://www.ncbi.nlm.nih.gov/books/NBK1478/).

**Secondary prevention:** Early genetic diagnosis in individuals presenting with young-onset dystonia-parkinsonism allows earlier, dose-conservative levodopa initiation aimed at minimizing later dyskinesia burden — the closest analog to "early detection and treatment" for this disease.

**Genetic counseling:** Central to family management — explaining the 25% recurrence risk for future siblings when both parents are confirmed carriers, offering heterozygote (carrier) testing to at-risk relatives once the familial variants are known, and discussing incomplete penetrance (most biallelic carriers identified outside a clinical ascertainment context are asymptomatic) so that genetic results are interpreted with appropriate caution [GeneReviews, NBK1478](https://www.ncbi.nlm.nih.gov/books/NBK1478/); [PMC8382284, CHRIS Cohort penetrance data](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8382284/).

**Screening:** No population-based newborn or adult screening program exists; targeted family (cascade) screening is the applicable model.

**Public health/immunization/behavioral prevention:** Not applicable — no infectious, vaccine-preventable, or established behavioral-risk component to this monogenic disease.

---

## 14. Other Species / Natural Disease

No naturally occurring PRKN-orthologous parkinsonism has been documented in companion animals or wildlife in the sources reviewed (this is a human genetic disease without a recognized veterinary natural-disease counterpart, unlike, e.g., some lysosomal storage disorders with dog/cat models). The disease-relevant biology is instead studied through engineered model organisms (Section 15). Human PRKN taxon: NCBITaxon:9606 (Homo sapiens).

---

## 15. Model Organisms

**Drosophila melanogaster (parkin null mutants):** The most phenotypically robust invertebrate model. Parkin-null flies show reduced lifespan, locomotor defects, male sterility, and dramatic mitochondrial pathology — swollen mitochondria with severely fragmented cristae — concentrated in energy-intensive tissues, especially adult flight muscle, which ultimately undergoes apoptotic degeneration; modest dopaminergic neurodegeneration is also observed [PNAS, Mitochondrial pathology and apoptotic muscle degeneration in Drosophila parkin mutants](https://www.pnas.org/doi/10.1073/pnas.0737556100); [ScienceDirect, Parkin Mutant Drosophila overview]. This model strongly supports the mitochondrial-quality-control mechanism and is widely used for genetic modifier screens (e.g., rescue by antioxidant gene overexpression) [PMC5818410; PMC9598960, Folic acid rescue of Parkin-null Drosophila phenotypes](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9598960/).

**Mouse (Mus musculus):**
- **Constitutive Prkn knockout mice** largely **fail to recapitulate** the dopaminergic neuronal loss and motor impairment seen in human PRKN-PD, despite showing mitochondrial dysfunction and broad proteomic changes — a long-standing puzzle in the field [Nature npj Parkinson's Disease, PARKIN is not required to sustain OXPHOS function in adult mammalian tissues](https://www.nature.com/articles/s41531-024-00707-0). One proposed explanation: germline (from-birth) Prkn deletion triggers developmental genetic compensation, whereas **adult-onset Prkn deletion via lentiviral delivery does produce progressive dopamine neuron loss** — implicating a compensation mechanism specific to constitutive knockouts [search synthesis, multiple sources].
- **Prkn R275W knock-in mice** (a disease-relevant missense allele rather than a null) represent a **more accurate model**, showing early dopamine neuron dysfunction, age-dependent substantia nigra dopamine neuron loss, and progressive motor impairment — considered a superior model of human juvenile parkinsonism relative to constitutive knockouts [PMID:39350737 / Brain 2024, Dopamine neuron dysfunction and loss in the Prkn R275W mouse model of Juvenile Parkinsonism](https://pubmed.ncbi.nlm.nih.gov/39350737/).
- Prkn-knockout mice additionally show autistic-like behaviors and aberrant synapse formation, suggesting broader circuit-level roles for parkin beyond dopaminergic neurodegeneration [PMC9249611, Prkn knockout mice autistic-like behaviors](https://pmc.ncbi.nlm.nih.gov/articles/PMC9249611/).
- A combined parkin-Pacrg knockout line and an isolated Pacrg knockout line have also been generated and characterized, given the overlapping genomic locus of PRKN and PACRG [Scientific Reports, parkin-Pacrg knockout mouse](https://www.nature.com/articles/s41598-018-25766-1).

**Zebrafish (Danio rerio):** Transient antisense (morpholino) knockdown of parkin does **not** produce morphological or behavioral abnormalities, and no dopaminergic neuron loss is observed — a negative/limited model. Conversely, **transgenic zebrafish overexpressing parkin are protected from proteotoxic-stress-induced cell death**, supporting a protective/quality-control role for parkin even though loss-of-function knockdown alone is insufficient to produce an overt phenotype in this system [PLOS ONE, Parkin Is Protective against Proteotoxic Stress in a Transgenic Zebrafish Model](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0011783).

**Human iPSC-derived neuronal models:** PARK2 (PRKN) patient-derived iPSC neurons and postmortem brain tissue show mitochondrial dysfunction, increased oxidative stress, and α-synuclein accumulation, providing a human cellular correlate of the pathway [PMC3546866](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3546866/). Mitophagy defects in these neurons are unmasked specifically as cells transition to oxidative-phosphorylation dependence during differentiation, offering a plausible explanation for selective adult-onset dopaminergic vulnerability despite germline gene loss from conception [PMC7511396](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7511396/). Skin fibroblasts from PRKN-PD patients also show mitochondrial and autophagic alterations, useful as an accessible non-neuronal patient cell model [PMC6594812, Mitochondrial and autophagic alterations in PD patient fibroblasts with Parkin mutations](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6594812/).

**Human-model translational gap (flag for curation as a HUMAN_MODEL_MISMATCH candidate):** The striking discrepancy between constitutive Prkn-knockout mice (minimal phenotype) and the clear human disease phenotype is a well-recognized, unresolved translational-fidelity gap in the field — the R275W knock-in and adult-conditional-deletion models represent partial resolutions but the mechanistic basis of developmental compensation remains "unknown" per the primary sources [Nature npj Parkinson's Disease 2024](https://www.nature.com/articles/s41531-024-00707-0).

---

## Summary of Key Ontology Term Candidates (verify all via OAK before curation)

| Domain | Suggested term | ID (verify) |
|---|---|---|
| Disease | autosomal recessive juvenile Parkinson disease 2 | MONDO:0010820 |
| Gene | PRKN | hgnc:8607 (verify) |
| Phenotype | Bradykinesia | HP:0002067 |
| Phenotype | Resting tremor | HP:0002322 |
| Phenotype | Rigidity | HP:0002063 |
| Phenotype | Dystonia | HP:0001332 |
| Phenotype | Hyperreflexia | HP:0001347 |
| Phenotype | Orthostatic hypotension | HP:0001278 |
| Phenotype | Constipation | HP:0002019 |
| Phenotype | Depression | HP:0000716 |
| GO Biological Process | mitophagy | GO:0000422 |
| GO Biological Process | protein polyubiquitination | GO:0000209 |
| GO Molecular Function | ubiquitin-protein transferase activity | GO:0004842 |
| Cell type | dopaminergic neuron | CL:0000700 |
| Anatomy | substantia nigra | UBERON:0002038 |
| Anatomy | basal ganglion | UBERON:0002420 |
| Chemical | levodopa | CHEBI:6437 |
| Chemical | dopamine | CHEBI:18243 |
| Treatment | Pharmacotherapy | NCIT:C15986 |
| Treatment | Gene Therapy | NCIT:C15238 |
| Treatment | Deep Brain Stimulation (Device) | verify NCIT term |

---

## Sources

- [Autosomal recessive juvenile Parkinson disease 2 — ClinGen/MONDO](https://search.clinicalgenome.org/kb/conditions/MONDO:0010820)
- [OMIM #600116 — PARKINSON DISEASE 2, AUTOSOMAL RECESSIVE JUVENILE; PARK2](https://omim.org/entry/600116)
- [OMIM Clinical Synopsis #600116](https://www.omim.org/clinicalSynopsis/600116)
- [OMIM *602544 — PARKIN RBR E3 UBIQUITIN PROTEIN LIGASE; PRKN](https://www.omim.org/entry/602544)
- [MalaCards — Parkinson Disease 2, Autosomal Recessive Juvenile](https://www.malacards.org/card/parkinson_disease_2_autosomal_recessive_juvenile)
- [GeneReviews — PRKN-Related Early-Onset Parkinson Disease (NBK1478)](https://www.ncbi.nlm.nih.gov/books/NBK1478/)
- [Frontiers — Frequency of Heterozygous Parkin (PRKN) Variants and Penetrance, CHRIS Cohort](https://www.frontiersin.org/journals/neurology/articles/10.3389/fneur.2021.706145/full) / [PMC8382284](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8382284/)
- [Frontiers — Genetic Analysis of Patients With Early-Onset Parkinson's Disease in Eastern China](https://www.frontiersin.org/journals/aging-neuroscience/articles/10.3389/fnagi.2022.849462/full)
- [medRxiv — Long-read sequencing unravels structural variants in PRKN](https://www.medrxiv.org/content/10.1101/2024.05.02.24306523.full.pdf)
- [medRxiv — Estimated genetic prevalence of early-onset PD from PRKN mutations](https://www.medrxiv.org/content/10.1101/2024.01.22.24301610v1.full)
- [Brain (Oxford Academic) — Heterozygous PRKN mutations are common but do not increase the risk of Parkinson's disease](https://academic.oup.com/brain/article/145/6/2077/6595863) / [PMC9423714](https://pmc.ncbi.nlm.nih.gov/articles/PMC9423714/)
- [Brain Communications — Levodopa-responsive dystonia caused by biallelic PRKN exon inversion invisible to exome sequencing](https://academic.oup.com/braincomms/article/3/3/fcab197/6364893) / [PMC8421701](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8421701/)
- [PMC7582384 — A Splice Intervention Therapy for AR Juvenile Parkinson's Disease from Parkin Mutations](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7582384/)
- [Frontiers — Case report: EOPD with spastic paraparesis/hyperreflexia from compound heterozygous PRKN exon 2/4 deletions](https://www.frontiersin.org/journals/neurology/articles/10.3389/fneur.2022.969232/full) / [PMC9714025](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9714025/)
- [Frontiers — Genotype-Phenotype Correlations in Monogenic Parkinson Disease](https://www.frontiersin.org/journals/neurology/articles/10.3389/fneur.2021.648588/full)
- [GeneCards — PRKN Gene](https://www.genecards.org/card/PRKN)
- [Cyagen — PRKN Gene Function & Its Critical Role in Parkinson's Pathogenesis](https://www.cyagen.com/cyagen-lab-notes/prkn-loss-function-parkinsons-neurobiology)
- [PMC9851250 — Feedforward activation of PRKN/parkin](https://pmc.ncbi.nlm.nih.gov/articles/PMC9851250/)
- [PMC3730226 — Structure of the human Parkin ligase domain in an autoinhibited state](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3730226/)
- [J Cell Biol — PINK1 phosphorylates ubiquitin to activate Parkin E3 ubiquitin ligase activity](https://rupress.org/jcb/article/205/2/143/37633/PINK1-phosphorylates-ubiquitin-to-activate-Parkin)
- [PMC9763867 — Parkin-PHB2 interaction links inner mitochondrial membrane ubiquitination to efficient mitophagy](https://pmc.ncbi.nlm.nih.gov/articles/PMC9763867/)
- [PMC3546866 — Mitochondrial dysfunction with oxidative stress and α-synuclein accumulation in PARK2 iPSC-derived neurons and postmortem brain tissue](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3546866/)
- [PMC7511396 — Oxidative switch drives mitophagy defects in dopaminergic parkin mutant patient neurons](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7511396/)
- [PMC6594812 — Mitochondrial and autophagic alterations in skin fibroblasts from PD patients with Parkin mutations](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6594812/)
- [PMC5818410 — Vulnerable Parkin Loss-of-Function Drosophila Dopaminergic Neurons](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5818410/)
- [PMC9598960 — Folic Acid Improves Parkin-Null Drosophila Phenotypes](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9598960/)
- [PNAS — Mitochondrial pathology and apoptotic muscle degeneration in Drosophila parkin mutants](https://www.pnas.org/doi/10.1073/pnas.0737556100)
- [Nature npj Parkinson's Disease — PARKIN is not required to sustain OXPHOS function in adult mammalian tissues](https://www.nature.com/articles/s41531-024-00707-0) / [PMC11058849](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11058849/)
- [Brain (PubMed) — Dopamine neuron dysfunction and loss in the Prkn R275W mouse model of juvenile parkinsonism](https://pubmed.ncbi.nlm.nih.gov/39350737/)
- [PMC9249611 — Prkn knockout mice show autistic-like behaviors and aberrant synapse formation](https://pmc.ncbi.nlm.nih.gov/articles/PMC9249611/)
- [Scientific Reports — Generation and characterisation of a parkin-Pacrg knockout mouse line](https://www.nature.com/articles/s41598-018-25766-1)
- [PLOS ONE — Parkin Is Protective against Proteotoxic Stress in a Transgenic Zebrafish Model](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0011783)
- [Nature Gene Therapy — In vitro and in vivo rescue of dopaminergic neurons in PD models after Parkin gene therapy](https://www.nature.com/articles/s41434-026-00599-0)
- [PMC12263715 — Investigational Gene Therapies for Parkinson's Disease](https://pmc.ncbi.nlm.nih.gov/articles/PMC12263715/)
- [PMC4010755 — Surgical Treatment of Dyskinesia in Parkinson's Disease](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4010755/)
- [PMC12583070 — Levodopa-induced dyskinesia in Parkinson's disease: an updated review of pharmacological treatments](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12583070/)
- [AJNR — The Role of Functional Dopamine-Transporter SPECT Imaging in Parkinsonian Syndromes](https://www.ajnr.org/content/36/2/229)

**Caveat on citation format:** The above are review/database/aggregator citations rather than exact primary-literature PMIDs for every claim; for dismech KB curation, each specific `evidence:` block should be traced back to its primary PubMed-indexed source (e.g., the original GeneReviews-cited studies, the specific cohort papers underlying the 6–12%/30%/42.2% frequency figures, and the primary Drosophila/mouse/zebrafish papers) and verified per the dismech reference-validation SOP (`just fetch-reference PMID:XXXX` + `just validate-references`) before being committed as PMID-anchored snippets.