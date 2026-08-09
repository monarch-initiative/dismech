---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-02T09:54:32.562533'
end_time: '2026-08-02T09:58:58.496883'
duration_seconds: 265.93
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Adenomyosis
  mondo_id: MONDO:0010888
  category: Complex
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
  web_search_requests: 21
  num_turns: 28
  total_cost_usd: 1.8018759999999998
  session_id: b2cd8e7a-75ab-5cad-941f-eba7858220b3
  stop_reason: end_turn
citation_count: 24
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Adenomyosis
- **MONDO ID:** MONDO:0010888 (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Adenomyosis** covering all of the
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

# Adenomyosis — Comprehensive Disease Research Report

## 1. Disease Information

**Overview:** Adenomyosis is a benign but often symptomatic gynecologic disorder defined by the ectopic presence of endometrial glands and stroma within the myometrium (the uterine smooth-muscle wall), accompanied by reactive myometrial smooth-muscle hyperplasia and hypertrophy surrounding the ectopic tissue. It was historically termed "endometriosis interna" to contrast with pelvic ("external") endometriosis, though the two are now understood as related but distinct disease entities sharing overlapping pathophysiology. Adenomyosis classically presents with heavy menstrual bleeding (HMB), dysmenorrhea, chronic pelvic pain, and subfertility, and is increasingly recognized as a distinct clinical entity that can occur with or without co-existing pelvic endometriosis or uterine leiomyomas (fibroids).

**Key identifiers:**
- **MONDO:** MONDO:0010888
- **OMIM:** 600458 (Adenomyosis)
- **ICD-11:** GA11 (Adenomyosis)
- **ICD-10:** N80.0
- **Synonyms:** Endometriosis interna; uterine adenomyosis; adenomyosis of the uterus/uterine corpus; adenomyoma (localized form)

**Nature of evidence base:** The literature is predominantly aggregated disease-level evidence — cross-sectional and retrospective cohort studies, systematic reviews/meta-analyses, hysterectomy-specimen histopathology series, imaging (MRI/TVUS) cohorts, and a growing body of single-cell/spatial transcriptomic and Mendelian-randomization studies using population biobank summary statistics (FinnGen, GTEx). Individual-patient EHR-level data exist (e.g., U.S. claims-based incidence/prevalence studies) but most mechanistic evidence derives from surgical-specimen molecular studies and small mouse models rather than large prospective clinical trials.

Sources: [OMIM 600458](https://www.omim.org/entry/600458); [StatPearls – Adenomyosis](https://www.ncbi.nlm.nih.gov/books/NBK539868/); [AAFP – Adenomyosis: Diagnosis and Management](https://www.aafp.org/pubs/afp/issues/2022/0100/p33.html)

---

## 2. Etiology

**Disease causal factors:** Adenomyosis has no single monogenic cause; it is a complex, multifactorial, estrogen-dependent disease. Three canonical (non-mutually-exclusive) pathogenic theories exist:
1. **Invagination/Tissue Injury and Repair (TIAR) theory** — mechanical disruption of the endometrial-myometrial interface (EMI) from uterine hyperperistalsis, parturition, or iatrogenic trauma triggers local micro-injury, downward endometrial basalis invagination into the myometrium, and local estradiol biosynthesis that perpetuates the lesion (Leyendecker et al., PMID: [25961248](https://pubmed.ncbi.nlm.nih.gov/25961248/)).
2. **Metaplasia of embryonic Müllerian remnants theory** — de novo lesions arise from misplaced Müllerian-derived tissue.
3. **Stem/progenitor cell origin theory** — aberrant migration and differentiation of endometrial or bone-marrow-derived multipotent progenitor cells into the myometrium.

A unifying "endometrial-myometrial interface disruption (EMID)" framework integrates these: tissue injury/repair, stem-cell recruitment, and epithelial-mesenchymal transition (EMT) converge to disrupt the archimetra and establish the adenomyotic microenvironment (PMC13070875; PMID: [41968335](https://pubmed.ncbi.nlm.nih.gov/41968335/)).

**Genetic risk factors:**
- No Mendelian causal gene is established; adenomyosis is polygenic/multifactorial.
- Somatic **KRAS** mutations are recurrent in adenomyotic glandular epithelium — found in 26/70 (37.1%) of cases in a next-generation-sequencing study of 192 multiregional samples, restricted to the epithelial (not stromal) compartment, and enriched in cases with co-existing endometriosis, low progesterone receptor (PR) expression, or prior progestin treatment (*Nat Commun*, "Uterine adenomyosis is an oligoclonal disorder associated with KRAS mutations"). Mutant KRAS hyperactivates downstream MAPK signaling and induces PGR gene hypermethylation, silencing PR-A/PR-B expression and driving progesterone resistance.
- **ARID1A** somatic mutations activate PI3K signaling, promoting EMT, migration, and invasion.
- A 2025 summary-data-based Mendelian randomization study using FinnGen GWAS (4,267 cases / 107,564 controls) plus GTEx v8 whole-blood and uterine cis-eQTLs identified 39 candidate causal genes (24 protein-coding), with **ARHGEF35, AMT, RCVRN, GMPPB,** and **INTS1** as top candidates; differential expression validation nominated DNA2, INTS1, EFCAB2, HLA-DQA2, and RPS26 (combined ROC AUC 0.8) (*Medicine (Baltimore)*, PMID: [40527793](https://pubmed.ncbi.nlm.nih.gov/40527793/)).
- **HOXA10** endometrial expression is decreased in adenomyosis, impairing endometrial receptivity (PMID: [21353411]; PMC3053130).
- No large adenomyosis-specific GWAS with genome-wide-significant loci has yet been published at the scale seen for endometriosis (42+ loci) or uterine fibroids; adenomyosis GWAS remain comparatively underpowered (FinnGen-scale only).

**Environmental/mechanistic risk factors** (all associated with estrogen excess or uterine mechanical trauma):
- Early menarche, short menstrual cycles, elevated BMI, multiparity (adjusted OR 1.8 for one birth, 3.1 for ≥2 births vs. nulliparous), oral contraceptive use, tamoxifen therapy (adenomyosis reported in up to 60% of long-term tamoxifen users, supporting estrogen dependence).
- Prior uterine surgery — dilation and curettage, cesarean delivery, myomectomy — associated with EMI disruption, though evidence is inconsistent across studies.
- Higher CA-125 levels, shorter menstrual cycle length, and earlier menarche were confirmed in a 2024 risk-factor cohort of MRI-diagnosed adenomyosis (PMC11981308).

**Protective factors:** Cigarette smoking is paradoxically associated with *decreased* adenomyosis risk in a dose-dependent manner (anti-estrogenic mechanism proposed, similar to endometriosis literature), though this is not a recommended intervention given smoking's broader harms.

**Gene-environment interaction:** The dominant model is that mechanical/hormonal environmental insults (parturition, surgery, hyperperistalsis) act on a genetically/epigenetically susceptible endometrial-myometrial interface (e.g., KRAS-mutant clones, altered METTL3/m6A epigenetic regulation) to trigger local estrogen biosynthesis (via aromatase upregulation and 17β-HSD2 downregulation) that sustains lesion growth — i.e., environmental injury unmasks and amplifies an underlying estrogen-dependent, epigenetically primed tissue.

Ontology suggestions: `HP:0000009` (functional abnormality of the female internal genitalia — broad); risk-factor genes `HGNC:6407` (KRAS), `HGNC:713` (ARID1A), `HGNC:5085` (HOXA10).

---

## 3. Phenotypes

| Phenotype | Type | Frequency | HPO suggestion |
|---|---|---|---|
| Heavy menstrual bleeding / menorrhagia | Symptom | ~60% of symptomatic cases; pooled 42% in AUB cohorts | HP:0008946 (Menorrhagia) / HP:0000132 (Menorrhagia — check exact label) |
| Dysmenorrhea (secondary, often progressive/worsening) | Symptom | 25–41% (pooled) | HP:0100608 (Dysmenorrhea) |
| Chronic pelvic pain | Symptom | Pooled 49% in symptomatic cohorts | HP:0012648 (Chronic pain) or pelvic-pain-specific term |
| Dyspareunia | Symptom | Pooled 46% | HP:0032389 (Dyspareunia, if present in HPO) |
| Infertility / subfertility | Clinical finding | 31% prevalence among infertility populations | HP:0000789 (Infertility) |
| Enlarged, globular uterus | Physical/imaging sign | Common on exam and imaging | HP:0000138 (Uterine neoplasm — not exact; better: descriptive) / consider "Uterine enlargement" |
| Elevated serum CA-125 | Laboratory abnormality | Variable, poorly sensitive/specific | Non-HPO lab marker |
| Chronic/recurrent pelvic pain with central sensitization | Symptom/mechanistic | Emerging area of study (2026 trial NCT07455721) | — |
| Abnormal uterine bleeding (irregular menses) | Symptom | Common, FIGO AUB structural category "A" (Adenomyosis) | HP:0000140 (Abnormal uterine bleeding, if present) |

**Onset:** Adenomyosis is a disease of reproductive-age and (increasingly, on imaging) even nulliparous younger women, classically diagnosed in the 4th–5th decade of life (peri- or late-reproductive years) at hysterectomy, but improved imaging has shifted diagnosis earlier, including in women in their 20s–30s presenting with dysmenorrhea/infertility. Symptoms typically resolve with menopause given estrogen dependence.

**Progression:** Generally a chronic, slowly progressive condition; dysmenorrhea and HMB often worsen over years, with severity, extent (focal vs. diffuse), and junctional-zone thickening correlating with symptom burden. Central sensitization to pelvic pain may develop with disease chronicity.

**Quality of life:** Multiple SF-36-based studies show significantly lower scores across all quality-of-life domains in women with adenomyosis compared to unaffected women, with the psychological impact and negative effect on work productivity exceeding that reported for pelvic endometriosis in some comparative studies (Alcalde et al., *J Womens Health* 2021). Pain interference and low self-efficacy are correlated with worse HRQoL.

---

## 4. Genetic/Molecular Information

- **Causal genes:** None Mendelian; disease is driven by somatic mosaicism/oligoclonality plus polygenic susceptibility.
- **Somatic pathogenic variants:**
  - **KRAS** (HGNC:6407) hotspot mutations in glandular epithelium — 37.1% of cases in NGS cohorts; gain-of-function, MAPK-pathway-activating; drives PGR hypermethylation → progesterone resistance and enhanced invasive capacity. Adenomyosis is described as an "oligoclonal disorder" with multiple independent KRAS-mutant clones across lesion regions.
  - **ARID1A** (HGNC:11110) mutations activate PI3K signaling.
  - Somatic mutation burden and clonality overlap substantially with deep infiltrating endometriosis, supporting a shared "endometriotic epithelium" mutational signature.
- **Germline candidate genes (MR-nominated):** ARHGEF35, AMT, RCVRN, GMPPB, INTS1, DNA2, EFCAB2, HLA-DQA2, RPS26 (PMID: 40527793) — associative/candidate-causal, not clinically validated; not yet ClinVar-classified for adenomyosis.
- **Allele frequency:** Not applicable in the germline-Mendelian sense; somatic KRAS variant allele fractions are lesion-specific and not captured in population databases (gnomAD/1000G not informative for this somatic-driven disease).
- **Epigenetics:**
  - Global and locus-specific DNA methylation changes at the *PGR* promoter (hypermethylation → PR silencing).
  - N6-methyladenosine (m6A) RNA methylation dysregulation: decreased **METTL3** reduces m6A levels, altering IGF1/DDT expression, disturbing estrogen–progesterone balance, and activating Wnt/EMT/angiogenesis programs.
  - Reduced histone deacetylase 3 (**HDAC3**) impairs resolution of NF-κB-driven inflammation.
- **Chromosomal abnormalities:** Not a recognized feature; adenomyosis is not classically associated with aneuploidy/CNV syndromes.
- **Transcriptomics:** Single-cell RNA-seq + spatial transcriptomics atlases (Protein & Cell 2024, PMC11214835; medRxiv 2025) have mapped cellular heterogeneity across the endometrial-myometrial junction, identifying unique epithelial/stromal/immune subpopulations, developmental trajectories, and altered cell-cell communication (notably involving macrophages and fibroblasts) specific to adenomyotic lesions versus eutopic endometrium and normal myometrium.

Ontology suggestions: HGNC:6407 (KRAS), HGNC:11110 (ARID1A), HGNC:5085 (HOXA10); GO:0007173 (EGF receptor signaling), GO:0004707 (MAP kinase activity).

---

## 5. Environmental Information

- **Environmental/toxicant factors:** Endocrine-disrupting chemicals (EDCs) — bisphenol A, dioxins/dioxin-like compounds, organochlorine pesticides, PCBs — are well studied in endometriosis (71% of reviewed studies show significant associations, PMID: 32903210) but only sparsely studied specifically in adenomyosis; the biological plausibility (estrogen-mimicry, aromatase upregulation) is shared given the common estrogen-dependent pathophysiology.
- **Lifestyle factors:** Elevated BMI is an established risk factor (adipose-tissue aromatization increases circulating/local estrogen). Smoking is inversely associated (protective, dose-dependent), an unusual and mechanistically debated finding.
- **Iatrogenic/mechanical exposures:** Cesarean section, dilation and curettage, myomectomy, and other intrauterine instrumentation are implicated as EMI-disrupting triggers under the TIAR model, though epidemiologic confirmation is inconsistent.
- **Infectious agents:** No established infectious etiology, though chronic endometritis co-occurs at increased frequency in adenomyosis/infertility cohorts (PMC11251133), raising a possible inflammatory-cofactor (not causal-pathogen) relationship.

---

## 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream):**

1. **Trigger:** Mechanical/hormonal injury at the endometrial-myometrial interface (uterine hyperperistalsis, parturition, instrumentation) or aberrant stem-cell/metaplastic seeding → local tissue injury.
2. **Tissue Injury and Repair (TIAR):** Injury activates local wound-healing programs that paradoxically include de novo estradiol biosynthesis (via **aromatase** upregulation and **17β-hydroxysteroid dehydrogenase type 2 (HSD17B2)** downregulation), producing sustained local hyperestrogenism (Leyendecker, PMID: 25961248).
3. **EMT and invasion:** Elevated local estrogen and COX-2/PGE2 signaling activate **ERK**, **RhoA/ROCK**, **TGF-β/Smad→β-catenin**, and **JAK2/STAT3** pathways, driving epithelial-mesenchymal transition (loss of E-cadherin, gain of α-SMA/vimentin) and endometrial-cell invasion into the myometrium.
4. **Progesterone resistance:** Somatic KRAS mutation and epigenetic PGR silencing (methylation, METTL3/m6A loss) blunt progesterone signaling, removing the physiological brake on proliferation and inflammation and driving *MIG-6* loss → ErbB2-ERK activation.
5. **Chronic inflammation:** TLR4/MyD88/NF-κB and cGAS-STING (mtDNA-sensing) activation drive cytokine dysregulation (↑IL-6, IL-1β, TNF-α, TGF-β1, CXCL8/IL-8, CXCL12; ↓IL-10, IL-22, IL-33). NLRP3 inflammasome activation (via GRIM19 downregulation) triggers macrophage pyroptosis and IL-1β release.
6. **Fibrosis/smooth-muscle metaplasia:** Fibroblast-to-myofibroblast transdifferentiation (FMT) and smooth-muscle metaplasia (SMM), mediated by GSK-3β/AKT and sphingosine-1-phosphate (S1P)/S1PR signaling, deposit excess extracellular matrix and generate the reactive myometrial hypertrophy characteristic of adenomyotic lesions.
7. **Angiogenesis:** Hypoxia (HIF-1α) and NF-κB drive VEGF/VEGFR-2 upregulation (amplified by an E2-Slug-VEGF axis), correlating with MMP-2/MMP-9 activity and lesion vascularity — vascularity is itself a prognostic factor for response to uterine artery embolization.
8. **Clinical manifestation:** The combination of ectopic endometrial tissue bleeding within a hypertrophic, poorly contractile, hypervascular myometrium produces heavy menstrual bleeding (impaired local hemostasis, increased endometrial surface area, dysregulated prostaglandins/eicosanoids) and dysmenorrhea/chronic pelvic pain (uterine hypercontractility from oxytocin/oxytocin-receptor upregulation, hyperperistalsis, and local inflammatory mediator release). Impaired decidualization (via HOXA10/FOXO1 downregulation, driven partly by low endometrial IL-10) and adverse endometrial receptivity, plus macrophage/NK-cell-mediated embryotoxic inflammation, underlie the associated subfertility and elevated miscarriage rate.

**Cell types involved:** endometrial epithelial cells, endometrial stromal cells, myometrial smooth muscle cells (CL:0000192), fibroblasts/myofibroblasts, macrophages (CL:0000235, including pyroptotic and polarized subtypes), endothelial cells (CL:0000115), and (proposed) bone-marrow-derived multipotent stem/progenitor cells.

**Molecular targets under therapeutic investigation:** COX-2 (celecoxib), NLRP3 inflammasome inhibitors, YAP1/Hippo modulators, JAK2/STAT3 inhibitors, GSK-3β inhibitors, sphingosine kinase (SphK) inhibitors, TrkB/TGF-β-Smad inhibitors, and epigallocatechin gallate (EGCG, multi-target).

Ontology suggestions:
- GO: GO:0001525 (angiogenesis), GO:0030198 (extracellular matrix organization), GO:0006954 (inflammatory response), GO:0001837 (epithelial to mesenchymal transition), GO:0038095 (Fc-epsilon/NF-κB — approximate; better GO:0043123 positive regulation of I-kappaB kinase/NF-kappaB signaling), GO:0016477 (cell migration)
- CL: CL:0000115 (endothelial cell), CL:0000235 (macrophage), CL:0002145 (ciliated columnar cell of endometrium — check exact), CL:0000499 (stromal cell)

Sources: [PMC11591984](https://pmc.ncbi.nlm.nih.gov/articles/PMC11591984/) (signaling pathways review); [PMC13070875](https://pmc.ncbi.nlm.nih.gov/articles/PMC13070875/) / PMID:41968335 (integrated pathogenesis review); [Nature Communications — KRAS oligoclonality](https://www.nature.com/articles/s41467-019-13708-y); [Human Reproduction Update — NGS insights](https://academic.oup.com/humupd/article/27/6/1086/6299969) PMID:34252159 (approx.); [PMC11214835](https://pmc.ncbi.nlm.nih.gov/articles/PMC11214835/) (single-cell/spatial atlas).

---

## 7. Anatomical Structures Affected

- **Organ level:** Primary organ — uterus (corpus), specifically the myometrium and the endometrial-myometrial junctional zone (JZ). Secondary/associated involvement: ovaries and pelvic peritoneum when co-existing endometriosis is present; rarely, deep adenomyoma can involve serosal/subserosal uterine layers.
- **Body systems:** Female reproductive system primarily; secondary systemic effects via chronic pain (nervous system sensitization) and chronic bleeding (hematologic — iron-deficiency anemia).
- **Tissue/cell level:** Ectopic endometrial glandular epithelium and stroma within myometrial smooth muscle; reactive smooth-muscle hyperplasia/hypertrophy surrounding lesions; increased vascular density.
- **Subcellular:** Altered mitochondrial DNA release triggering cGAS-STING (cytosolic DNA-sensing pathway); ER/Golgi involvement in secretory dysregulation of cytokines; nuclear epigenetic machinery (METTL3/m6A writer complex, HDAC3).
- **Localization:** UBERON:0000995 (uterus); more specifically UBERON:0001296 (myometrium) and the endometrial-myometrial junctional zone (no dedicated UBERON term for JZ; commonly described radiologically). Adenomyosis can be diffuse (throughout the myometrium) or focal/localized (adenomyoma), and can be classified by depth as internal/intrinsic (inner myometrium, junctional-zone-based) vs. external/extrinsic (outer myometrium, subserosal) per the Kishi MRI classification (subtypes I–IV).
- **Lateralization:** Not applicable (single midline organ); lesions may be anterior, posterior, or fundal, and diffuse or asymmetric within the uterine wall.

Ontology suggestions: UBERON:0000995 (uterus), UBERON:0001296 (myometrium), UBERON:0001295 (endometrium).

---

## 8. Temporal Development

- **Onset:** Classically diagnosed in the 4th–5th decade (peri-/late-reproductive years), historically at hysterectomy in multiparous women in their 40s; with modern imaging (TVUS, MRI), diagnosis increasingly occurs in younger, even nulliparous, symptomatic or infertile women in their 20s–30s.
- **Onset pattern:** Insidious/chronic — arises gradually from repeated microtrauma/inflammatory cycles rather than an acute event.
- **Progression:** Slowly progressive over years; junctional-zone thickening and lesion extent tend to increase with time and parity; estrogen-dependence means progression is expected to plateau/regress after menopause (endogenous estrogen decline) or with GnRH-agonist-induced hypoestrogenism.
- **Disease course pattern:** Chronic, generally stable-to-progressive during reproductive years; can be relapsing in terms of symptom flares tied to the menstrual cycle; recurrence after conservative (uterus-sparing) treatment is common, particularly in diffuse-type, younger, longer-duration-disease patients with thicker JZ and higher CA-125.
- **Remission:** Menopause (natural or medically induced via GnRH agonists) produces symptom remission through estrogen withdrawal; add-back therapy is needed for long-term GnRH-agonist use due to hypoestrogenic side effects (bone loss).
- **Critical periods:** Postpartum/post-instrumentation periods (cesarean section, D&C) are proposed windows of EMI vulnerability; the perimenopausal transition is a window where declining estrogen may naturally attenuate disease.

---

## 9. Inheritance and Population

**Epidemiology (from a 2025 systematic review/meta-analysis, PMID: 41257733):**
- General population point prevalence: ~1% (95% CI 0–2%) by strict criteria, but much higher (17–35%) when focal/diffuse imaging or histopathologic definitions are used across symptomatic/surgical cohorts.
- Prevalence by diagnostic method: histopathology 35.1% (95% CI 30.9–39.4%), MRI 35.0% (22.6–48.4%), ultrasound 30.7% (25.2–48.4%) — reflecting selected (mostly hysterectomy or symptomatic) populations rather than the general population.
- Infertility populations: 31% (95% CI 10–58%).
- Symptomatic subgroup prevalence: abnormal uterine bleeding 42%, pelvic pain 49%, dyspareunia 46%, dysmenorrhea 41%.
- Parity association: parous women 38% vs. nulliparous 28%.
- Co-occurrence with endometriosis: found in 42% of individuals with coexisting endometriosis.
- U.S. population-based claims study (2006–2015): annual incidence ~1.03% (28.9 per 10,000 woman-years); highest incidence in women 41–45 years (69.1/10,000 in 2008); Black women showed higher incidence (up to 44.6/10,000) than White women (up to 27.9/10,000), indicating racial disparity.

**Inheritance pattern:** Not a single-gene Mendelian disorder — complex/multifactorial (polygenic susceptibility + somatic mosaicism + environmental/mechanical triggers). No penetrance, expressivity, anticipation, mosaicism (germline), or founder-effect data apply in the classic monogenic sense; however, somatic mosaicism of KRAS-mutant epithelial clones is itself a defining molecular feature.

**Population demographics:**
- Affects individuals with a uterus during reproductive years, primarily 35–50; increasing detection in younger women due to improved imaging.
- Racial/ethnic disparity noted in U.S. incidence data (higher in Black women).
- Sex ratio: not applicable (uterus-specific disease in individuals assigned female at birth).
- No strong documented geographic/endemic clustering, though international incidence/prevalence estimates vary by diagnostic practice and access to hysterectomy pathology.

---

## 10. Diagnostics

**Imaging (first-line, non-invasive):**
- **Transvaginal ultrasound (TVUS)** and **MRI** are the two primary recommended modalities per SOGC Guideline No. 437 (2023) (PMID: 37244746).
- **MUSA (Morphological Uterus Sonographic Assessment) 2022 Delphi-revised criteria:** direct signs (echogenic subendometrial lines/buds, myometrial cysts, hyperechogenic islands, translesional vascularity on color Doppler, interrupted junctional zone — at least one required) and indirect signs (globular/enlarged uterus, asymmetric myometrial thickening, fan-shaped shadowing). Interrupted junctional zone and myometrial cysts show highest specificity (89.0%, 88.5%); hyperechoic islands show highest sensitivity (69.2%). No single sign is sufficiently accurate alone.
- **MRI:** Junctional zone (JZ) thickening >12 mm is the key diagnostic threshold; diagnostic accuracy up to 85%. MRI JZ thickness measurements are systematically larger than TVUS measurements of the same structure.
- **Classification systems:** Kishi 4-subtype MRI classification (I – intrinsic/inner myometrium; II – extrinsic/outer myometrium/subserosal; III – intramural/middle myometrium; IV – indeterminate); Gordts et al. proposed five descriptive parameters (affected area, wall location, diffuse vs. focal pattern, muscular vs. cystic lesion type, lesion volume/extent).

**Laboratory/biomarkers:**
- **CA-125:** can be markedly elevated (case reports up to 4,400 IU/mL in severe disease, normalizing post-surgery) and correlates with dysmenorrhea severity, but has poor sensitivity/specificity as a standalone diagnostic (elevated in endometriosis, pregnancy, and other benign/malignant conditions) — adjunctive use only. A >7-fold CA-125 decrease after GnRH-agonist treatment is associated with improved live-birth rates in IVF.
- No FDA-qualified specific biomarker exists; urinary biomarker panels are an active research area (PMC9025125).

**Genetic testing:** Not clinically indicated — adenomyosis is not diagnosed via germline genetic testing; somatic KRAS profiling remains a research tool.

**Histopathology (gold standard, post-hysterectomy):** Presence of endometrial glands/stroma within the myometrium, typically ≥2.5 mm from the endometrial-myometrial junction, with surrounding smooth-muscle hyperplasia.

**Differential diagnosis:** Uterine leiomyoma (fibroids), endometrial polyps, pelvic endometriosis, endometrial hyperplasia/carcinoma (especially given the CA-125 overlap and increased cancer risk noted below), primary dysmenorrhea, chronic pelvic inflammatory disease.

**Screening:** No population screening program exists (disease is not amenable to mass screening); case-finding relies on symptom-triggered imaging in reproductive-age individuals with HMB, dysmenorrhea, or infertility.

Ontology suggestions: NCIT terms for MRI (`NCIT:C16809` Magnetic Resonance Imaging) and transvaginal ultrasound (`NCIT:C113663` or closest match); LOINC for CA-125 assay.

---

## 11. Outcome/Prognosis

- **Not a mortality-associated disease** in itself (benign condition); no survival/mortality statistics apply directly, though associated cancer risk (below) has downstream mortality implications.
- **Fertility/reproductive outcomes:** Adenomyosis is associated with impaired IVF/ART outcomes — lower implantation rates (25.6% vs 28.6% controls), lower live-birth rates (26% vs 31.5%), and significantly higher miscarriage rates (29.1–35.4% vs 17.2–18.1% in controls) across multiple retrospective cohorts, with effects most pronounced in women ≥38 years. Mechanistically linked to impaired decidualization/receptivity and macrophage/NK-cell-mediated embryotoxicity.
- **Treatment response prognostic factors:** For uterine artery embolization (UAE), recurrence is more likely in younger patients, longer disease duration, more severe pretreatment symptoms, higher CA-125, diffuse-type disease, thicker JZ, and sparsely vascularized lesions; conversely, greater lesion vascularity is associated with better UAE response (PMC5091759).
- **Complications:** Iron-deficiency anemia from chronic HMB; chronic pelvic pain with risk of central sensitization; infertility/subfertility; in pregnancy, adenomyosis is associated with increased risk of preterm birth, preeclampsia, and other obstetric complications (per multiple cohort studies, not detailed above but consistently reported in the literature).
- **Malignancy risk:** Adenomyosis is associated with a 4–5-fold increased risk of subsequent endometrial cancer (aOR 5.13, 95% CI 1.36–19.40) and ovarian cancer (aOR 5.50, 95% CI 1.95–15.50) in population-based cohort studies; increased thyroid cancer risk has also been reported (PMC5844548). Co-existing endometriosis further raises colorectal cancer risk (aOR 13.04). Proposed shared mechanisms include chronic inflammation, hormonal dysregulation, and overlapping somatic mutational landscapes (KRAS, ARID1A) with endometrioid/clear-cell gynecologic cancers.
- **Quality of life prognosis:** Significant, sustained reduction across SF-36 domains; treatment (medical, interventional, or surgical) generally improves symptom-specific and global quality-of-life scores, though recurrence is common with conservative management.

---

## 12. Treatment

**Pharmacotherapy (first-line, per SOGC Guideline No. 437, 2023):**
- **Levonorgestrel-releasing intrauterine system (LNG-IUS, 20 μg/day)** — first-line for HMB and pain; reduces menstrual blood loss by 71–95%, efficacy comparable to endometrial ablation. NCIT: consider `NCIT:C15986` (Pharmacotherapy) with `therapeutic_agent` levonorgestrel (CHEBI applicable).
- **Combined oral contraceptives** — first-line for pain/HMB.
- **Dienogest** (progestin) — first-line.
- **NSAIDs** and **tranexamic acid** — symptomatic HMB/pain management (supportive care, NCIT:C15747).
- **GnRH agonists** — second-line (due to hypoestrogenic adverse effects — bone loss, vasomotor symptoms); add-back hormone therapy required if used >6 months.

**Interventional:**
- **Uterine artery embolization (UAE)** — minimally invasive, uterus-sparing; short-term (12-month) improvement rates of 70.9–74.0% for dysmenorrhea/menorrhagia, long-term (5–7 year) sustained improvement in a majority of patients (68.8–92.3% depending on cohort); outcomes correlate with lesion vascularity.

**Surgical:**
- Endometrial ablation, hysteroscopic/laparoscopic excision of adenomyoma (adenomyomectomy), high-intensity focused ultrasound (HIFU), and hysterectomy (definitive treatment, reserved for those who have completed childbearing or with refractory symptoms).

**Emerging/experimental targets (preclinical, not yet clinical standard):** COX-2 inhibitors (celecoxib), NLRP3 inflammasome inhibitors, JAK2/STAT3 inhibitors, YAP1/Hippo pathway modulators, GSK-3β inhibitors, sphingosine kinase inhibitors, TrkB inhibitors, EGCG (green tea catechin).

**Treatment strategy:** Management is individualized by symptom priority (HMB vs. pain vs. fertility), age, and desire for fertility preservation, following a stepwise algorithm from medical → interventional → surgical management (per SOGC Guideline No. 437 and AAFP 2022 review).

**Adverse events:** GnRH agonists → hypoestrogenic bone loss, vasomotor symptoms (mitigated by add-back therapy); UAE → post-embolization syndrome, rare ovarian-reserve impact; surgery → standard surgical/anesthetic risks, and hysterectomy is irreversible/fertility-ending.

Ontology suggestions: `NCIT:C15986` (Pharmacotherapy), `NCIT:C15329` (Surgical Procedure), `NCIT:C15313` is not applicable here but UAE could map to an interventional radiology procedure NCIT term; `therapeutic_agent` CHEBI terms for levonorgestrel, dienogest, tranexamic acid, leuprolide (GnRH agonist).

---

## 13. Prevention

- **Primary prevention:** No established primary prevention strategy exists given the multifactorial, not-fully-preventable etiology; minimizing unnecessary uterine instrumentation (D&C, non-medically-indicated cesarean) is a plausible but unproven risk-reduction measure under the TIAR mechanical-injury model.
- **Secondary prevention (early detection):** Prompt imaging (TVUS/MRI) in reproductive-age patients presenting with HMB, progressive dysmenorrhea, or unexplained infertility enables earlier diagnosis and fertility-preserving management before progression to diffuse disease.
- **Tertiary prevention:** Early initiation of LNG-IUS/hormonal therapy in diagnosed patients may reduce complication burden (anemia from chronic HMB, progression of pain/central sensitization) and preserve fertility options before disease progression necessitates surgery.
- **Behavioral/lifestyle interventions:** Weight management (given BMI-estrogen association) is a plausible, evidence-adjacent risk-modification strategy, though not a formally validated prevention protocol; lifestyle interventions for pelvic-pain symptom management (exercise, dietary modification) are under active scoping review (PMC12935590) but evidence remains preliminary.
- **Genetic counseling:** Not applicable — no Mendelian inheritance pattern to counsel on.
- **Screening programs:** None population-based; case-finding is symptom-triggered.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** Naturally occurring adenomyosis has been documented in **dogs** (*Canis lupus familiaris*, NCBITaxon:9615) and **cats** (*Felis catus*, NCBITaxon:9685), where it is typically an incidental finding associated with other uterine pathology (endometritis, pyometra, cystic endometrial hyperplasia, and occasionally co-occurring uterine leiomyoma), rather than a primary clinical disease entity.
- **Veterinary relevance:** Considered rare and usually asymptomatic/incidental in companion animals; case reports document adenomyosis with severe cervical inflammation in a dog (PMC1082876) and co-existing leiomyoma/adenomyosis/cystic endometrial hyperplasia (Karagiannis 2011, *Case Rep Vet Med*).
- **Comparative biology:** The fundamental mechanism (ectopic endometrial glandular/stromal tissue within myometrium with reactive smooth-muscle change) is conserved across mammals, but naturally-occurring veterinary disease has not been developed as a systematic comparative-pathology model given its rarity and incidental-finding status in animals.
- **Transmission:** Not applicable — non-infectious, non-zoonotic condition.
- **No dedicated OMIA (Online Mendelian Inheritance in Animals) entry** was identified for adenomyosis, consistent with its non-Mendelian, largely incidental veterinary occurrence.

---

## 15. Model Organisms

- **Mouse models (primary experimental system):**
  - **Mechanical-injury (EMI-puncture) model:** Repeated needle puncture disrupting the endometrial-myometrial interface generates persistent glandular epithelium/stroma structures within the myometrium resembling human adenomyosis; this 2022 model (*Sci Rep*, PMC9585053) is notable for producing durable, quantifiable lesions suitable for longitudinal and perinatal-outcome studies, improving on earlier, slower-developing models.
  - **Neonatal estrogen-receptor-β (ERβ) agonist exposure model:** Neonatal feeding of an ERβ agonist to ICR mice induces external adenomyosis-like lesions, supporting the estrogen-receptor-dependent mechanistic hypothesis (*Reprod Dev Med* 2021).
  - Other historical models include tamoxifen-induced and pituitary-isograft-induced hyperprolactinemia/hyperestrogenic mouse models (referenced in the broader animal-model literature but not detailed in current search results); the classically cited **Tsp2 (thrombospondin-2) knockout mouse** spontaneously develops adenomyosis-like lesions, supporting a role for ECM/anti-angiogenic regulation in disease genesis (cited across review literature, though not independently re-verified in this search pass — flag for confirmation before KB citation).
- **Model characteristics:** Mechanical-injury models best recapitulate the TIAR/EMI-disruption theory and are suited to studying lesion initiation, fibrosis, and perinatal/obstetric outcome consequences; hormonal-exposure models best recapitulate the estrogen-dependence and receptor-signaling arm. No single model captures the full human triad of somatic KRAS-driven epithelial clonality + progesterone resistance + chronic pelvic pain phenotype — a noted translational limitation.
- **Applications:** Used to study lesion initiation/EMI disruption, fibrosis and smooth-muscle metaplasia, angiogenesis, fertility/perinatal outcomes, and to test candidate therapeutics (e.g., COX-2, NLRP3, JAK/STAT inhibitors) preclinically.
- **In vitro/cell-based models:** Primary human endometrial epithelial/stromal cell cultures, endometriotic epithelial cell lines (used to study KRAS/PIK3CA-driven progesterone resistance, PMC11049223), and emerging patient-derived organoids.
- **Resources:** MGI (Mouse Genome Informatics) for strain/allele records; no dedicated adenomyosis-specific consortium repository identified (contrast with more established disease-model networks like IMPC for single-gene knockouts).

---

## Summary of Key Ontology Term Suggestions for KB Curation

| Category | Suggested terms |
|---|---|
| MONDO | MONDO:0010888 |
| Phenotypes (HP) | Dysmenorrhea, Menorrhagia/abnormal uterine bleeding, Chronic pelvic pain, Infertility, Dyspareunia |
| Genes (HGNC) | KRAS (hgnc:6407), ARID1A (hgnc:713 — verify), HOXA10 (hgnc:5100 — verify), METTL3 (hgnc — verify) |
| GO biological processes | epithelial to mesenchymal transition, angiogenesis, extracellular matrix organization, inflammatory response, response to estrogen |
| Cell types (CL) | endometrial stromal cell, endometrial epithelial cell, uterine smooth muscle cell, macrophage, endothelial cell |
| Anatomy (UBERON) | uterus (UBERON:0000995), myometrium (UBERON:0001296), endometrium (UBERON:0001295) |
| Treatments (NCIT) | Pharmacotherapy (NCIT:C15986), Surgical Procedure (NCIT:C15329), with therapeutic_agent CHEBI terms for levonorgestrel, dienogest, leuprolide, tranexamic acid |

*(Note: several HGNC/HPO IDs above are given from memory/search snippets and should be independently verified with OAK before committing to the dismech KB, per the project's anti-hallucination validation workflow — this report is a curation input, not pre-validated YAML.)*

---

### Sources

- [Research Advances in Adenomyosis-Related Signaling Pathways and Promising Targets (PMC11591984)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11591984/)
- [Pathogenesis of Adenomyosis: An Integrated Review of Cellular Origins, Molecular Mechanisms, and Intersecting Diseases (PMC13070875 / PMID:41968335)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13070875/)
- [A new concept of endometriosis and adenomyosis: tissue injury and repair (TIAR) — PMID:25961248](https://pubmed.ncbi.nlm.nih.gov/25961248/)
- [Uterine adenomyosis is an oligoclonal disorder associated with KRAS mutations — Nature Communications](https://www.nature.com/articles/s41467-019-13708-y)
- [Adenomyosis pathogenesis: insights from next-generation sequencing — Human Reproduction Update](https://academic.oup.com/humupd/article/27/6/1086/6299969)
- [Identification of novel causally related genes in adenomyosis: MR study — PMID:40527793](https://pmc.ncbi.nlm.nih.gov/articles/PMC12173309/)
- [Global prevalence of adenomyosis and endometriosis: systematic review and meta-analysis — PMID:41257733](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12629041/)
- [Adenomyosis incidence, prevalence and treatment: US population-based study 2006–2015 — AJOG](https://www.ajog.org/article/S0002-9378(20)30023-5/fulltext)
- [SOGC Guideline No. 437: Diagnosis and Management of Adenomyosis — PMID:37244746](https://pubmed.ncbi.nlm.nih.gov/37244746/)
- [Innovative Ultrasound Criteria for the Diagnosis of Adenomyosis (MUSA) — PMC10886873](https://pmc.ncbi.nlm.nih.gov/articles/PMC10886873/)
- [MRI and Adenomyosis: What Can Radiologists Evaluate? — PMC9140978](https://pmc.ncbi.nlm.nih.gov/articles/PMC9140978/)
- [Comprehensive transcriptional atlas of human adenomyosis — single-cell + spatial transcriptomics (PMC11214835)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11214835/)
- [Establishment of a novel mouse model of adenomyosis (EMI puncture) — Scientific Reports / PMC9585053](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9585053/)
- [Neonatal ERβ agonist adenomyosis-like mouse model — Reprod Dev Med](https://mednexus.org/doi/10.1097/RD9.0000000000000012)
- [Women with adenomyosis are at higher risks of endometrial and thyroid cancers — PMC5844548](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5844548/)
- [The Risks for Ovarian, Endometrial, Breast, Colorectal, and Other Cancers in Women With Newly Diagnosed Endometriosis or Adenomyosis](https://www.international-journal-of-gynecological-cancer.com/article/S1048-891X(24)03125-6/fulltext)
- [Impact of Adenomyosis on Women's Psychological Health and Work Productivity](https://journals.sagepub.com/doi/10.1089/jwh.2020.8789)
- [Outcomes in Adenomyosis Treated with Uterine Artery Embolization Are Associated with Lesion Vascularity — PMC5091759](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5091759/)
- [Risk factors for uterine adenomyosis diagnosed by MRI in women of reproductive age — PMC11981308](https://pmc.ncbi.nlm.nih.gov/articles/PMC11981308/)
- [OMIM Entry 600458 — Adenomyosis](https://www.omim.org/entry/600458)
- [StatPearls — Adenomyosis](https://www.ncbi.nlm.nih.gov/books/NBK539868/)
- [AAFP — Adenomyosis: Diagnosis and Management](https://www.aafp.org/pubs/afp/issues/2022/0100/p33.html)