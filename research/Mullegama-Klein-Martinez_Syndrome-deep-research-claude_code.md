---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-30T23:54:46.753131'
end_time: '2026-07-31T00:00:19.224918'
duration_seconds: 332.47
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Mullegama-Klein-Martinez Syndrome
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
  web_search_requests: 9
  num_turns: 23
  total_cost_usd: 1.7032407000000003
  session_id: a420e0e7-4ef5-5506-a389-453777267be1
  stop_reason: end_turn
citation_count: 12
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Mullegama-Klein-Martinez Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Mullegama-Klein-Martinez Syndrome** covering all of the
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

I now have comprehensive material from OMIM, PubMed/PMC primary literature, MalaCards, GTR, ClinVar, and disease ontology resources. Compiling the full research report now.

# Mullegama–Klein–Martinez Syndrome (MKMS): Comprehensive Research Report

---

## 1. Disease Information

**Overview:** Mullegama–Klein–Martinez syndrome (MKMS) is a rare X-linked cohesinopathy caused by pathogenic (typically de novo) variants in **STAG2** (Stromal Antigen 2), a core subunit of the cohesin complex. It presents as a syndromic neurodevelopmental disorder characterized by global developmental delay/intellectual disability, microcephaly, characteristic craniofacial dysmorphism, ear anomalies with hearing loss, short stature, digit/limb anomalies, brain malformations, and — in a subset — congenital heart defects. The condition is also catalogued as **NEURODEVELOPMENTAL DISORDER, X-LINKED, WITH CRANIOFACIAL ABNORMALITIES** (OMIM synonym). It was clinically delineated across several case series between 2015 and 2019 and named after the lead authors of the defining reports (Mullegama, Klein, Martinez).

**Key identifiers:**
- **OMIM:** #301022 (MULLEGAMA-KLEIN-MARTINEZ SYNDROME; MKMS) — [OMIM 301022](https://www.omim.org/entry/301022)
- **Gene locus:** STAG2, Xq25 (HGNC:11355; also called SA2, SA-2, SCC3B)
- **MedGen:** UID / CUI **C5193008**
- **MONDO:** MONDO:0026722
- **Disease Ontology:** DOID:0111845
- **Orphanet:** No dedicated ORPHA number was identified as of this search; an open community tracker issue (OD4RD/Main-Help-Desk #492) explicitly requests creation of a new ORPHAcode for this condition, indicating Orphanet coverage is still pending/incomplete.
- **ICD-10/ICD-11:** No syndrome-specific code identified; would fall under general codes for congenital malformation syndromes with intellectual disability (e.g., ICD-10 Q87.8).
- **Gene symbol synonyms in databases:** HPE13, MKMS, NEDXCF (Neurodevelopmental disorder, X-linked, with craniofacial abnormalities)

**Synonyms:** "STAG2-related disorder," "STAG2 cohesinopathy," "X-linked cohesinopathy due to STAG2 deficiency," "NEDXCF."

**Evidence base:** Information is derived almost entirely from **aggregated case-report/case-series literature** (individual published patients, not large registries or EHR cohorts). As of the most recent (2025) case report, approximately 19–20 patients have been reported in the literature in total, making this an ultra-rare, case-report-level evidence base rather than a population-level epidemiological resource.

Sources: [OMIM #301022](https://www.omim.org/entry/301022); [OMIM Clinical Synopsis](https://omim.org/clinicalSynopsis/301022); [NCBI GTR C5193008](https://www.ncbi.nlm.nih.gov/gtr/conditions/C5193008/); [MalaCards](https://www.malacards.org/card/mullegama_klein_martinez_syndrome)

---

## 2. Etiology

**Primary cause — genetic, X-linked, dosage-sensitive:**
MKMS is caused by heterozygous (in females) or hemizygous (in males) deleterious variants in **STAG2**, located at Xq25. STAG2 encodes a cohesin-complex subunit. Mullegama et al. (2017, PMID:[28296084](https://pubmed.ncbi.nlm.nih.gov/28296084/)) established the dosage-sensitivity model: *"we suggest that STAG2 is a dosage-sensitive gene and that heterozygous loss-of-function variants lead to a cohesinopathy."* The gene is under strong evolutionary constraint against loss-of-function (pLI ≈ 1, o/e ≈ 0.02), consistent with dosage sensitivity.

Notably, **both loss-of-function (deletion, duplication, and dosage-altering variants) can cause overlapping neurodevelopmental phenotypes**:
- **Loss-of-function (point mutations, truncating variants, deletions):** the classic MKMS/de novo STAG2 cohesinopathy (Mullegama et al. 2017).
- **Increased dosage (Xq25 microduplication encompassing only STAG2):** Leroy et al. 2016 (PMID:[25677961](https://pubmed.ncbi.nlm.nih.gov/25677961/)) reported six patients from two families with Xq25 duplications refined to a 173-kb single-gene (STAG2) critical region, with "delayed milestones, speech disturbance, intellectual disability, abnormal behaviours and a characteristic facial dysmorphism," concluding that "increased STAG2 gene copy number and dysregulation of its downstream target genes may be responsible for the specific clinical findings of this syndrome" — establishing this as "a novel cohesinopathy." This is a related but molecularly distinct entity (gain of dosage vs. loss of function) and both ends of the dosage spectrum perturb cohesin stoichiometry.

**Risk factors:**
- **Genetic:** Nearly all reported cases are **de novo**; no known population-level susceptibility loci or modifier genes have been established. Variant type and position appear to modulate phenotype (see Genetic section).
- **Environmental:** None established — this is a monogenic disorder with no known environmental, infectious, or lifestyle contributors.
- **Sex as a risk-modifying factor:** Because STAG2 is X-linked and dosage-sensitive, sex profoundly affects viability and phenotype (see Population section) — females (two X alleles, subject to X-inactivation) tolerate more severe/truncating variants and survive; males (single X allele/hemizygous) are proposed to be largely non-viable with severe loss-of-function alleles, explaining an ascertainment bias toward affected females and toward missense variants in affected males.

**Protective factors:** None specifically documented. Favorable/skewed X-chromosome inactivation (XCI) toward the wild-type allele in a carrier female could theoretically attenuate phenotype, though the literature (Mullegama et al. 2017; Aoi et al. 2020) instead documents the opposite — **skewed XCI favoring the mutant allele** in most reported affected females (see Mechanism section).

**Gene–environment interactions:** None reported; this is considered a purely monogenic/chromosomal-dosage disorder.

Sources: [Mullegama et al. 2017, AJMG-A, PMID:28296084](https://pubmed.ncbi.nlm.nih.gov/28296084/); [Leroy et al. 2016, Clin Genet, PMID:25677961](https://pubmed.ncbi.nlm.nih.gov/25677961/); [PMC8476567](https://pmc.ncbi.nlm.nih.gov/articles/PMC8476567/)

---

## 3. Phenotypes

Phenotype data are compiled principally from the "Expanding the known phenotype of Mullegama–Klein–Martinez syndrome in male patients" case series (PMC8476567, patient 19 of the aggregated literature cohort of 19 published cases at that time) and the 2025 conotruncal-defect case report (MDPI Genes, PMC12652599).

### Neurodevelopmental
- **Neurodevelopmental disorder / global developmental delay** — reported in essentially all patients (19/19 in the aggregated series). HPO: **HP:0012758** (Neurodevelopmental delay) / **HP:0001263** (Global developmental delay)
- **Intellectual disability** — 14/19. HPO: **HP:0001249** (Intellectual disability)
- **Speech/language delay, poor speech, pronunciation difficulties.** HPO: **HP:0000750** (Delayed speech and language development)
- **Hypotonia** — 6/19, including truncal hypotonia with fluctuating hypertonus in some. HPO: **HP:0001252** (Hypotonia)
- **Seizures** — 3/19; one case had a generalized tonic-clonic seizure at age 7 requiring lamotrigine. HPO: **HP:0001250** (Seizure)
- **ADHD/behavioral abnormalities** reported in a subset (per GTR/MalaCards compilations). HPO: **HP:0007018** (Attention deficit hyperactivity disorder)
- **EEG abnormality** (continuous beta activity, though not epileptiform in one reported case). HPO: **HP:0002353** (EEG abnormality)

### Growth
- **Short stature** — 10/19. HPO: **HP:0004322**
- **Failure to thrive** — 4/19. HPO: **HP:0001508**
- **Intrauterine growth restriction (IUGR)** — 2/19; also documented in the 2025 conotruncal case (birth weight 2190 g at 37+2 weeks). HPO: **HP:0001511**

### Craniofacial
- **Microcephaly** — 11/15 affected females in the male-phenotype-expansion series. HPO: **HP:0000252**
- Dysmorphic facial gestalt: narrow bifrontal diameter/narrow forehead, dolichocephaly or brachycephaly, prominent metopic suture, broad/bulbous nasal bridge, up-slanting or antimongoloid palpebral fissures, thick lips, coarse facies, triangular face, high anterior hairline, mild frontal bossing, prominent cheeks. HPO terms include **HP:0000252** microcephaly, **HP:0000341** narrow forehead, **HP:0000426** prominent nasal bridge, **HP:0000582** up-slanted palpebral fissures, **HP:0000463** anteverted nares (reported exclusively in females), **HP:0000343** long philtrum (females only)
- **Micrognathia**, **high-arched palate**. HPO: **HP:0000347**, **HP:0000218**
- **Fifth finger clinodactyly** reported in male patients. HPO: **HP:0004209**

### Ear/hearing
- **Microtia**, dysmorphic/posteriorly rotated ears, **sensorineural hearing loss**, atresia of external auditory canal. HPO: **HP:0008551** (microtia), **HP:0000407** (sensorineural hearing loss), **HP:0000356** (abnormal ear morphology)

### Brain/neuroimaging
- **Pathological brain MRI** — 15/18. Findings include **polymicrogyria** (perisylvian, novel finding in the 2021 case), **corpus callosum hypoplasia** (including hypoplastic presplenial portion), cortical thickening, dilated lateral ventricles, and **ectopic posterior pituitary with thin infundibulum** (shared between two patients with the same Tyr159 residue affected — see variant-phenotype correlation below). HPO: **HP:0002126** (polymicrogyria), **HP:0002079** (corpus callosum hypoplasia/agenesis), **HP:0002360** (abnormal circadian — not applicable), better: **HP:0011368** (ectopic posterior pituitary)

### Skeletal/limb
- Broad hands/feet with soft dorsum and deeply inserted nails, hyperextensible joints, severe **pes planus** (flat feet) — including one case with bilateral pes planus (left-sided severe, right equinovarus), digit/polydactyly anomalies (foot polydactyly reported in a male patient), rib fusion and vertebral abnormalities (females only), single palmar crease (females only). HPO: **HP:0001769** (pes planus), **HP:0001156** (broad finger), **HP:0001830** (broad foot), **HP:0100259** (foot polydactyly), **HP:0000159** (broad fingers/toes with soft tissue)

### Cardiac
- **Congenital heart defects** — 7/19 in the base cohort; range from mild/isolated septal defects (ASD, VSD, PDA — most commonly reported) to, in the novel 2025 case, a **severe complex conotruncal malformation**: pulmonary atresia, double-outlet right ventricle (DORV), large subaortic VSD, ostium secundum ASD, and moderate PDA. HPO: **HP:0001629** (ventricular septal defect), **HP:0001631** (atrial septal defect), **HP:0001636** (tetralogy-spectrum/conotruncal — closest term **HP:0001719**, double outlet right ventricle), **HP:0001719**, **HP:0006530** (pulmonary atresia)
- Persistent/patent foramen ovale reported as a minimal, self-resolving finding in two patients sharing the p.Tyr159 residue variant.

### Ophthalmologic
- **Strabismus** (females only). HPO: **HP:0000486**
- Atrophic retinal/uveal scar (one case).

### Other reported (female-exclusive per the 2021 aggregation)
Long eyelashes, hirsutism, cutis marmorata, hypoplastic nails, congenital diaphragmatic hernia, pulmonary hypoplasia, GERD, abnormal echocardiogram findings.

### Novel/rare features from most recent reports
- **Supernumerary nipple**, asymmetric/disproportionate growth (mosaic case, Frontiers 2022, PMC9710855) — asymmetry attributed to postzygotic mosaicism with tissue-variable variant allele fraction (29.65% blood, 35.64% urine, 40–42% buccal).
- **Semilobar holoprosencephaly** in a severely affected mosaic individual.

**Severity/progression:** Phenotype severity is highly variable ("highly variable phenotypes" — PMC8476567) and appears influenced by variant type/position, sex, and (in rare cases) somatic mosaicism level across tissues. Developmental delay and craniofacial features are present from infancy/early childhood (congenital onset); brain and cardiac malformations are present prenatally/at birth; seizures can emerge later in childhood (e.g., age 7 in one case). No systematic natural-history/QOL instrument data (EQ-5D, SF-36) were identified — QOL impact is inferred qualitatively from developmental/motor limitations (e.g., one 10-year-old patient "cannot walk unaided").

Sources: [PMC8476567 (Expanding known phenotype in males)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8476567/); [MDPI Genes 2025, PMC12652599](https://www.mdpi.com/2073-4425/16/11/1364); [Frontiers 2022 mosaicism paper, PMC9710855](https://pmc.ncbi.nlm.nih.gov/articles/PMC9710855/); [NCBI GTR](https://www.ncbi.nlm.nih.gov/gtr/conditions/C5193008/)

---

## 4. Genetic/Molecular Information

**Causal gene:** **STAG2** (HGNC:11355; Gene ID: 10735; located Xq25). Transcripts referenced in the literature: NM_001042749.2, NM_001042750.2, and NM_006603 (canonical). OMIM gene entry: *STAG2, 300826.

**Variant spectrum reported in MKMS (aggregated ~19–20 published cases):**
- **Truncating variants** (nonsense, frameshift): predominant in **females** — 13/15 female cases in the 2021 aggregation carried truncating variants (e.g., c.205C>T; p.(Arg69*) — the original 2017 index case; c.2972_2975dup, p.His992Glnfs*11 — 2025 conotruncal case, which truncates the final 237 amino acids and removes ~20% of the C-terminal domain).
- **Missense variants**: the **only variant class reported in males** (3–4 total male patients as of 2021), clustering within functional domains — the STAG domain and the C-terminal Stromalin Conservative Domain (SCD)/SA_C domain (e.g., p.Tyr159His and p.Tyr159Cys at the identical residue in two unrelated patients with a shared distinctive phenotype including ectopic posterior pituitary; K1009N in a 4-year-old boy, Mullegama et al. 2019).
- **Splice-site variants**: 1 reported female case; also seen in the mosaic cohort (predicted-but-unconfirmed aberrant splicing by RNA-seq).
- **Copy-number/dosage variants**: Xq25 microduplications spanning only STAG2 (Leroy et al. 2016) causing a phenotypically overlapping but molecularly distinct gain-of-dosage cohesinopathy.
- **Mosaic/postzygotic variants**: first reported in 2022 (PMC9710855), variant allele fractions 29–42% across tissues, associated with asymmetric phenotype expression.

**Variant classification (ACMG/AMP):** Reported MKMS variants in ClinVar are generally classified Pathogenic/Likely Pathogenic; examples curated: NM_001042750.2:c.1811G>A (p.Arg604Gln) [RCV000761368]; c.1894T>A (p.Cys632Ser) [RCV001823050]; c.1279G>A (p.Ala427Thr) [RCV003444413]; c.445A>G (p.Thr149Ala) [RCV004789936]. VUS and likely-benign STAG2 variants are also catalogued separately in ClinVar Miner for unrelated (non-MKMS) phenotype contexts, underscoring the need for careful variant-disease correlation.

**Allele frequency:** Novel MKMS-causing variants (e.g., p.Tyr159His, c.2972_2975dup) are consistently **absent from gnomAD and ClinVar** prior to publication, consistent with strong purifying selection against germline STAG2 loss-of-function (gnomAD pLI ≈ 1, o/e ≈ 0.02 — among the most LOF-intolerant genes in the genome).

**Somatic vs. germline:** MKMS variants are germline (constitutional), typically de novo, with one documented instance each of confirmed low-level parental (maternal/sibling) carrier status without phenotype (2021 case — asymptomatic heterozygous mother and sister) and postzygotic somatic mosaicism in the proband (2022 case). **Important distinction:** STAG2 is *also* one of the most frequently somatically mutated cohesin genes in human cancer (bladder cancer, Ewing sarcoma, myeloid malignancies) — this is a mechanistically related but clinically and pathophysiologically distinct entity from germline MKMS and should not be conflated in curation.

**Functional consequence:** Predominantly **loss of function** (haploinsufficiency in females via truncation/nonsense-mediated decay or protein truncation removing the RAD21-interaction SA_C domain; complete/near-complete loss in hemizygous males restricted to milder missense alleles compatible with survival) — plus a distinct **gain-of-dosage** mechanism for Xq25 duplication cases. No dominant-negative mechanism has been proposed; STAG2 is not itself an enzyme (it is an HEAT-repeat scaffolding/adaptor subunit), so no catalytic gain-of-function is expected.

**Modifier genes:** None formally established; compensatory **upregulation of the paralogous cohesin subunits STAG1 and ectopic STAG3** has been documented as a cellular response to STAG2 loss (forming "chimeric cohesin complexes"), which may modulate phenotype severity but is not a classical inherited modifier.

**Epigenetic information:** **X-chromosome inactivation (XCI) skewing** is the central "epigenetic" determinant of phenotype in affected females. Molecular analyses of patient fibroblasts show **highly skewed XCI favoring the mutant allele**, resulting in loss of STAG2 expression in most tested cells — i.e., the "wrong" X is preferentially silenced, exposing the mutant allele's effects despite heterozygosity. This is the key epigenetic/mechanistic explanation for why females survive severe truncating variants (mosaic expression across cell populations) while a fully hemizygous truncating male would not.

**Chromosomal abnormalities:** Xq25 microduplications (see Etiology) are the chromosomal-scale correlate of this locus; no aneuploidy or translocation syndromes are otherwise associated.

**Suggested ontology terms:** Gene — **hgnc:11355** (STAG2); related GO molecular function — **GO:0032116** (SMC loading complex) is not quite right; more precisely **GO:0008278** (cohesin complex, cellular component) and **GO:0007062** (sister chromatid cohesion, biological process); protein family — Pfam STAG domain, InterPro stromalin conservative domain (SCD).

Sources: [Mullegama et al. 2017, PMID:28296084](https://pubmed.ncbi.nlm.nih.gov/28296084/); [PMC8476567](https://pmc.ncbi.nlm.nih.gov/articles/PMC8476567/); [MDPI Genes 2025](https://www.mdpi.com/2073-4425/16/11/1364); [Frontiers 2022, PMC9710855](https://pmc.ncbi.nlm.nih.gov/articles/PMC9710855/); ClinVar records cited above; [ClinGen dosage curation, STAG2/HGNC:11355](https://search.clinicalgenome.org/kb/gene-dosage/HGNC:11355)

---

## 5. Environmental Information

No environmental, lifestyle, or infectious contributory factors have been identified or proposed in the literature — MKMS is a purely monogenic disorder. Not applicable for toxin/occupational-exposure, dietary, or pathogen-mediated etiology.

---

## 6. Mechanism / Pathophysiology

**Causal chain (molecular → cellular → tissue → clinical):**

1. **Molecular trigger:** De novo (or rarely postzygotic mosaic) pathogenic variant in STAG2 → truncated/absent protein (loss-of-function alleles) or, in the duplication variant, excess STAG2 gene dosage.
2. **Cohesin complex disruption:** STAG2 is a core, non-catalytic accessory subunit of the cohesin complex (core ring: SMC1A, SMC3, RAD21, plus one of STAG1/STAG2/STAG3). C-terminal truncations remove the **SA_C domain** required for physical interaction with **RAD21**, destabilizing the STAG2–RAD21 interface and, by extension, cohesin ring loading/stability (demonstrated by SWISS-MODEL structural modeling in the 2025 case report). Molecular Function/GO: **GO:0008278** cohesin complex; **GO:0003682** chromatin binding.
3. **Impaired sister chromatid cohesion and 3D genome organization:** Loss of functional cohesin at this subunit disrupts sister chromatid cohesion during mitosis/meiosis (directly demonstrated by delayed sister chromatid cohesion on cytogenetic analysis in the original 2017 index case) and, more broadly, disrupts cohesin's role in **chromatin loop extrusion and topologically associating domain (TAD) boundary formation**, thereby dysregulating enhancer–promoter looping. Biological process: **GO:0007062** sister chromatid cohesion; **GO:0034508** centromeric sister chromatid cohesion; **GO:0006325** chromatin organization.
4. **Transcriptional dysregulation of developmental gene programs:** Disrupted chromatin looping specifically dysregulates **cardiac developmental transcription factors** — TBX1, NKX2-5, HAND2 — as proposed in the 2025 conotruncal-defect case report, providing a direct mechanistic link between cohesin dysfunction and the cardiac phenotype via impaired **cardiac neural crest cell migration** and secondary heart field morphogenesis.
5. **Cellular/tissue consequence:** Global transcriptional/developmental dysregulation across multiple lineages produces the pleiotropic MKMS phenotype: impaired neurogenesis/cortical development (microcephaly, polymicrogyria, corpus callosum hypoplasia), impaired craniofacial and otic development (dysmorphism, microtia/hearing loss), impaired cardiac outflow tract septation (conotruncal defects), and impaired skeletal/limb patterning (digit anomalies, broad hands/feet).
6. **Modulation by X-inactivation (in females) and dosage (mosaicism, duplication):** As above, skewed XCI toward the mutant allele determines the effective cellular dose of functional STAG2 and hence severity; postzygotic mosaicism produces tissue-restricted/asymmetric phenotypes; compensatory paralog upregulation (STAG1, ectopic STAG3) may partially buffer cohesin function in some cells, contributing to phenotypic variability and cell-to-cell heterogeneity.
7. **Sex-differential lethality:** Complete hemizygous loss of STAG2 in males is proposed to be incompatible with survival beyond early embryogenesis (paralleling mouse Stag2-null lethality — see Model Organisms), explaining why surviving affected males carry only partial-function missense alleles positioned within structured functional domains, while surviving affected females can tolerate full truncating null alleles because of the buffering second X allele (even though skewed XCI often defeats this buffering at the cellular level in specific tissues).

**Protein dysfunction type:** Predominantly **loss of function** via truncation/domain disruption (SA_C/RAD21-interaction domain); the Xq25 duplication mechanism instead represents **dosage gain**. No evidence for a dominant-negative or aggregation-based mechanism; STAG2 is an HEAT-repeat-containing non-enzymatic scaffold protein (UniProt Q8N3U4), so classical "misfolding/enzyme deficiency" framing does not apply — this is a genome-architecture/regulatory disorder rather than a classical metabolic one.

**Immune system involvement:** Not implicated; no autoimmune or immunodeficiency phenotype described.

**Tissue damage mechanisms:** Not a degenerative/tissue-injury disorder in the classical sense (no oxidative stress, ischemia, or fibrosis mechanism); pathology is developmental/morphogenetic (structural malformation from disrupted transcriptional programs during embryogenesis), not post-natal tissue destruction.

**Molecular profiling:** No large-scale transcriptomic, proteomic, or single-cell datasets specific to MKMS patient tissue were identified in this search (this is consistent with the ultra-rare, case-report-level evidence base). Related mechanistic insight comes from **model systems** (mouse Stag2-null embryos, zebrafish stag1/stag2 morphants — see Model Organisms) rather than human multi-omics.

**Suggested ontology terms:**
- **GO (biological process):** GO:0007062 (sister chromatid cohesion), GO:0006325 (chromatin organization), GO:0006338 (chromatin remodeling), GO:0007507 (heart development), GO:0021987 (cerebral cortex development)
- **GO (cellular component):** GO:0008278 (cohesin complex), GO:0000785 (chromatin)
- **CL (cell types):** CL:0000047 (neural stem cell) / CL:0002608 (cortical neuron precursor) for neurodevelopmental phenotypes; CL:0008034 (cardiac neural crest cell) for the cardiac/conotruncal mechanism
- **UBERON:** UBERON:0000955 (brain), UBERON:0000948 (heart), UBERON:0001690 (ear), UBERON:0002616 (skeletal system)

Sources: [Mullegama et al. 2017, PMID:28296084](https://pubmed.ncbi.nlm.nih.gov/28296084/); [MDPI Genes 2025, PMC12652599](https://www.mdpi.com/2073-4425/16/11/1364); [PMC8476567](https://pmc.ncbi.nlm.nih.gov/articles/PMC8476567/); [PMC9710855](https://pmc.ncbi.nlm.nih.gov/articles/PMC9710855/); [PMC12765388 — STAG2-truncating variants mosaic inactivation/compensatory remodeling](https://pmc.ncbi.nlm.nih.gov/articles/PMC12765388/)

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Brain/CNS (microcephaly, polymicrogyria, corpus callosum hypoplasia, ectopic posterior pituitary), craniofacial skeleton, ear (microtia, hearing apparatus), heart (septal defects to complex conotruncal malformations), skeletal system/limbs (hands, feet, digits)
- **Secondary/complication-associated:** Eyes (strabismus, retinal/uveal scarring), gastrointestinal (GERD, diaphragmatic hernia in some female cases), respiratory (pulmonary hypoplasia secondary to diaphragmatic hernia), endocrine (pituitary stalk/ectopic posterior pituitary abnormalities)
- **Body systems involved:** Nervous system, cardiovascular system, musculoskeletal system, special senses (auditory, visual), endocrine system

**Tissue/cell level:** Neuroepithelium/cortical progenitors (polymicrogyria implies a migration/lamination defect), cardiac neural crest cells and secondary heart field mesoderm (conotruncal septation), otic placode-derived structures (microtia/hearing loss), chondro-osseous tissue (digit/limb skeletal anomalies).

**Subcellular level:** Nucleus/chromatin (cohesin complex operates at centromeres and along chromosome arms during interphase for loop extrusion — GO:0000785 chromatin, GO:0000775 chromosome centromeric region).

**Localization/lateralization:** Predominantly bilateral/symmetric malformations (craniofacial, cardiac), but the 2022 mosaic case demonstrated **markedly asymmetric/unilateral findings** (right-sided supernumerary nipple, unilateral ear dysplasia and hearing impairment, asymmetric growth) attributable to postzygotic mosaic distribution rather than a bilateral developmental field defect.

Suggested UBERON terms: UBERON:0000955 (brain), UBERON:0002021 (cerebral cortex), UBERON:0002336 (corpus callosum), UBERON:0000948 (heart), UBERON:0002078 (right ventricle) / UBERON:0002080 (heart outflow tract) for DORV/pulmonary atresia, UBERON:0001690 (external ear), UBERON:0001846 (pituitary gland)/ UBERON:0002116 (posterior pituitary).

---

## 8. Temporal Development

**Onset:** Congenital/prenatal for structural anomalies (cardiac malformations detected at birth or in utero via IUGR; craniofacial dysmorphism present from birth); developmental delay recognized in **infancy** (failure to meet motor/speech milestones); some features (e.g., seizures) can have later childhood onset (documented onset at age 7 in one case).

**Onset pattern:** Insidious/developmental rather than acute — this is a static structural/neurodevelopmental malformation syndrome, not an episodic or acutely progressive disease.

**Progression:** Predominantly **non-progressive/stable structural** phenotype (congenital malformations do not worsen per se), but the **functional/developmental trajectory** (motor, speech, cognitive) shows ongoing delay through childhood; one 10-year-old proband "cannot walk unaided," indicating persistent rather than resolving motor impairment. No formal staging system exists (this is not a staged disease like cancer). Seizures, once they emerge, may require ongoing anticonvulsant management (chronic, not self-limited).

**Disease course pattern:** Largely **stable congenital malformation plus chronic developmental disability**; a subset of findings are described as resolving (e.g., patent foramen ovale that was "minimal" and spontaneously closed by 1-year follow-up in two patients).

**Critical periods:** The embryonic/fetal period is the critical window for the structural anomalies (cardiac septation defects arise from disrupted neural crest/secondary heart field function during cardiogenesis; cortical malformations arise during neuronal migration). Early childhood is the critical window for surveillance and intervention for developmental delay, hearing loss (early identification is critical for speech/language outcomes), and seizure monitoring.

**Remission patterns:** Not a remitting-relapsing disease; the closest analog is spontaneous resolution of the minimal PFO noted above, which is a known feature of many congenital PFOs generally rather than a syndrome-specific remission.

---

## 9. Inheritance and Population

**Epidemiology:** MKMS is **ultra-rare** — approximately 19–20 patients reported in the peer-reviewed literature as of the most recent (2025) case report. No formal prevalence or incidence rate (per 100,000) has been established or published; there is no disease registry, and Orphanet coverage appears to be pending (per the open Orphanet-code request tracked at OD4RD/Main-Help-Desk #492). This places MKMS in the "ultra-rare, case-report-only" epidemiological tier (analogous to `PrevalenceClassEnum.NOT_YET_DOCUMENTED` in dismech schema terms).

**Inheritance pattern:** **X-linked**, most commonly described as **X-linked, typically de novo** (databases variably label it "X-linked recessive" or "X-linked dominant" depending on source — MalaCards/GTR describe it as X-linked recessive while acknowledging females are more severely, not less, affected, which is somewhat atypical for classic X-linked recessive inheritance and instead reflects dosage-sensitivity/XCI-driven pathophysiology rather than a simple recessive/dominant dichotomy). Virtually all reported cases are **de novo**, with rare exceptions of asymptomatic carrier relatives (heterozygous mother/sister documented in one 2021 case).

**Penetrance/expressivity:** Full penetrance is implied for the truncating variants reported in females (all are symptomatic), but **expressivity is markedly variable** — phenotype severity and specific feature combinations differ substantially between patients, correlating with variant type/position, sex, and (in mosaic cases) variant allele fraction/tissue distribution.

**Genetic anticipation:** Not applicable (not a repeat-expansion disorder).

**Germline mosaicism:** Not directly documented for parental transmission in MKMS specifically, but the general precedent for de novo disorders (recurrence risk can rise from <1% to as high as 50% if germline mosaicism is present in a parent) applies, and parental testing is recommended for accurate recurrence-risk counseling. **Somatic (postzygotic) mosaicism in the proband** has been directly documented (2022 case, variant allele fraction 29–42% across tissues).

**Founder effects / consanguinity:** None reported; consistent with a de novo mutational mechanism rather than a founder-population or consanguinity-driven recessive disorder.

**Carrier frequency:** Not established (too rare / not systematically screened; no population carrier-frequency data in gnomAD given the extreme rarity and severity of causal variants).

**Sex ratio and viability model:** Reported cases skew heavily female (≈15 female : 3–4 male in the 2021 aggregated series). The prevailing model: **"females, who carry 2 copies of the STAG2 gene, are able to survive with deleterious de novo variants but show severe phenotypes, while males, who have only 1 copy of the gene, are unable to survive with similar [severe/truncating] variants due to early embryonic lethality"** — surviving males are restricted to missense variants within structured functional domains (STAG domain/SCD), producing a generally milder or differently patterned phenotype. This mirrors mouse Stag2-knockout embryonic lethality data (see Model Organisms).

**Population demographics:** No specific ethnic/geographic enrichment identified; reported patients span multiple countries/ancestries (including at least one Hispanic patient in the 2025 report), consistent with a pan-ethnic de novo disorder rather than a population-specific one.

**Age distribution:** All reported patients are pediatric at time of ascertainment (from neonatal/infant presentation through at least age 10 in follow-up); no adult natural-history data identified.

Sources: [PMC8476567](https://pmc.ncbi.nlm.nih.gov/articles/PMC8476567/); [MalaCards](https://www.malacards.org/card/mullegama_klein_martinez_syndrome); [NCBI GTR](https://www.ncbi.nlm.nih.gov/gtr/conditions/C5193008/); [OD4RD Orphanet-code tracker issue #492](https://github.com/OD4RD/Main-Help-Desk/issues/492)

---

## 10. Diagnostics

**Genetic testing (primary diagnostic modality):**
- **Molecular confirmation of a pathogenic STAG2 variant** is the diagnostic gold standard, typically achieved via:
  - **Whole exome sequencing (WES)** — the modality used to identify the causal variant in essentially all published cases (trio WES enabling de novo variant confirmation).
  - **Single-gene STAG2 sequencing** — feasible once suspected clinically, though most cases were identified via unbiased exome/genome approaches given the nonspecific/overlapping phenotype.
  - **Chromosomal microarray (CMA)** — the diagnostic method for the Xq25-duplication cohesinopathy variant (array CGH identified the 173-kb critical duplicated region in Leroy et al. 2016).
  - Per NCBI GTR, **90 clinical tests** are listed as available for STAG2, reflecting availability through commercial/clinical gene panels (X-linked intellectual disability panels, cohesinopathy panels) as well as standalone sequencing.
  - **Tissue-specific testing for mosaicism**: the 2022 mosaicism report recommends testing **multiple tissues** (blood, urine, buccal) when mosaicism is suspected (asymmetric phenotype, lower-than-expected variant allele fraction in a single tissue), since variant allele fraction varied substantially by tissue (29.65% blood vs. 40–42% buccal in the reported case).

**Imaging:**
- **Brain MRI**: recommended given the high yield of pathological findings (15/18 in the aggregated cohort) — polymicrogyria, corpus callosum hypoplasia/hypoplastic presplenial portion, cortical thickening, ventriculomegaly, ectopic posterior pituitary with thin infundibulum.
- **Echocardiography**: essential given the cardiac defect prevalence (7/19, ranging from isolated septal defects to complex conotruncal malformation) — should be performed at diagnosis regardless of presenting phenotype, given the 2025 case demonstrating that severe cardiac disease can occur even when other features (brain MRI, early neurodevelopment) are relatively preserved.

**Other clinical tests:**
- **Cytogenetic assay for sister chromatid cohesion defects** — used investigationally in the original 2017 index-case report to functionally validate pathogenicity (delayed sister chromatid cohesion demonstrated on cytogenetic analysis).
- **EEG** for seizure/epileptiform activity surveillance.
- Standard audiology evaluation given high rate of hearing loss/ear anomalies.

**Differential diagnosis:** Other cohesinopathies (Cornelia de Lange syndrome — NIPBL, SMC1A, SMC3, HDAC8, RAD21; STAG1-related disorder), other X-linked intellectual disability syndromes, and other syndromic causes of microcephaly with congenital heart disease and craniofacial dysmorphism (e.g., 22q11.2 deletion syndrome for conotruncal defects specifically) should be considered and excluded, particularly before WES/WGS results are available.

**Screening:** No population-based newborn screening or carrier-screening program exists for this ultra-rare de novo disorder; family-specific carrier testing (of the mother and potentially siblings) is warranted after a proband diagnosis to assess for parental mosaicism and recurrence risk.

**Suggested LOINC/MAXO/ontology anchors:** MAXO:0000009 (medical imaging procedure) or more specifically brain MRI/echocardiography clinical procedure terms via NCIT; genetic testing terms via NCIT (Whole Exome Sequencing, Chromosomal Microarray Analysis).

Sources: [PMC8476567](https://pmc.ncbi.nlm.nih.gov/articles/PMC8476567/); [Mullegama et al. 2017, PMID:28296084](https://pubmed.ncbi.nlm.nih.gov/28296084/); [Leroy et al. 2016, PMID:25677961](https://pubmed.ncbi.nlm.nih.gov/25677961/); [PMC9710855](https://pmc.ncbi.nlm.nih.gov/articles/PMC9710855/); [NCBI GTR](https://www.ncbi.nlm.nih.gov/gtr/conditions/C5193008/)

---

## 11. Outcome/Prognosis

**Survival/mortality:** No formal survival statistics (5-year, 10-year) exist given the extreme rarity of the condition; reported patients have survived to at least early-to-mid childhood (oldest follow-up identified: age 10). The proposed **embryonic lethality of severe hemizygous STAG2 loss-of-function in males** (paralleling mouse data) implies that a subset of the most severe genotype-sex combinations may not be compatible with live birth at all — this is a survivorship-bias caveat relevant to interpreting the published cohort (only survivors are ascertained).

**Morbidity/function:** Chronic neurodevelopmental disability is the dominant long-term morbidity — intellectual disability (14/19), motor impairment (one 10-year-old unable to walk unaided), speech/language impairment, and hearing loss (with implications for speech development if unaddressed). Congenital heart defects, when severe (as in the 2025 conotruncal case), require neonatal surgical intervention and carry attendant surgical/perioperative morbidity risk. No formal QOL instrument (EQ-5D/SF-36/PROMIS) data are published for this condition.

**Complications:** Seizures (requiring anticonvulsant therapy in at least one reported case), recurrent GERD and pulmonary hypoplasia in association with congenital diaphragmatic hernia (in some female patients), ophthalmologic complications (strabismus, retinal/uveal scarring).

**Prognostic factors:** Variant type (truncating vs. missense) and position (functional-domain missense variants in males vs. domain-agnostic truncating variants in females) correlate with phenotype pattern/severity; degree and tissue distribution of mosaicism (in mosaic cases) correlates with asymmetry and severity; X-inactivation skewing in females is a proposed (though not exhaustively studied) severity modifier.

**Recovery potential:** Developmental gains are possible with early intervention (physical/occupational/speech therapy), consistent with general principles for neurodevelopmental disability, though no MKMS-specific outcome studies of intervention efficacy were identified.

---

## 12. Treatment

There is **no disease-specific or curative therapy** for MKMS — management is entirely **symptomatic/supportive and multidisciplinary**, following general practice for syndromic neurodevelopmental/congenital-malformation disorders. No pharmacogenomic, gene-therapy, or targeted-molecular therapy specific to STAG2 dosage correction has been reported in the human clinical literature (STAG2 is not a druggable enzyme, so classical small-molecule "restore function" strategies do not apply; investigational cohesin-related therapeutics in the literature relate to STAG2's role as a synthetic-lethal target in **cancer**, not to correcting germline dosage in MKMS).

**Documented management from case reports:**
- **Antiepileptic pharmacotherapy**: **Lamotrigine** was initiated in one patient following a generalized tonic-clonic seizure at age 7 (Pharmacotherapy; MAXO term: generic anticonvulsant use — no MAXO-specific "lamotrigine" term, would use `treatment_term` NCIT:C15986 Pharmacotherapy with `therapeutic_agent` CHEBI:6367 lamotrigine).
- **Cardiac surgical intervention**: The 2025 conotruncal-defect case required neonatal cardiac surgical management for pulmonary atresia/DORV/VSD/ASD/PDA (MAXO:0000004 surgical procedure; more specific NCIT:C15329 Surgical Procedure / cardiac surgery subtype).
- **Supportive/rehabilitative care**: Physical therapy, occupational therapy, and speech-language therapy are the standard of care implied by the motor and speech delay phenotype (MAXO:0000011 physical therapy; MAXO:0001351 occupational therapy; MAXO:0000930 speech therapy), though not explicitly detailed as an intervention protocol in the sourced case reports.
- **Audiological management**: hearing aids or other amplification/intervention would be indicated given the high rate of sensorineural hearing loss (MAXO:0009030 hearing aid usage), though not explicitly documented in a specific case.
- **Genetic counseling**: emphasized in the mosaicism literature as essential for accurate recurrence-risk assessment once mosaic or germline status is clarified (MAXO:0000079 genetic counseling).

**Treatment algorithm:** No published disease-specific clinical pathway exists; management follows a **multidisciplinary, phenotype-driven** approach (cardiology, neurology, genetics, audiology, developmental pediatrics, physical/occupational/speech therapy) analogous to other syndromic X-linked intellectual disability disorders.

**Clinical trials:** No MKMS-specific or STAG2-germline-targeted clinical trials were identified in this search (ClinicalTrials.gov not directly queried in this session, but no trial was surfaced through literature/database search).

Sources: [MDPI Genes 2025, PMC12652599](https://www.mdpi.com/2073-4425/16/11/1364); [PMC8476567](https://pmc.ncbi.nlm.nih.gov/articles/PMC8476567/)

---

## 13. Prevention

No primary, secondary, or tertiary prevention strategy exists for this de novo genetic disorder beyond standard reproductive genetic counseling:

- **Primary prevention:** Not applicable (de novo mutation, not preventable by risk-factor modification).
- **Secondary prevention (prenatal/preimplantation):** Once a familial pathogenic STAG2 variant is identified (e.g., in a case of parental germline mosaicism), **prenatal diagnosis** (chorionic villus sampling/amniocentesis for the known familial variant) or **preimplantation genetic testing (PGT-M)** would be technically available options for future pregnancies, following general principles for de novo dominant/X-linked disorders with a known causal variant — not specifically documented as performed in the MKMS literature reviewed here.
- **Genetic counseling:** Explicitly recommended in the literature (2022 mosaicism paper) as the key "preventive" (recurrence-risk-informing) intervention — testing parents for mosaicism given that germline mosaicism can raise recurrence risk substantially above the general de novo background rate.
- **Screening:** No population or newborn screening program exists (ultra-rare, no biochemical newborn-screening analyte).
- **Tertiary prevention:** Early identification of hearing loss and prompt audiological intervention to prevent secondary speech/language delay; early cardiac diagnosis (echocardiography) to enable timely surgical correction and prevent hemodynamic complications; seizure surveillance/EEG to enable prompt anticonvulsant treatment.

---

## 14. Other Species / Natural Disease

No naturally occurring veterinary or wildlife disease analog of MKMS has been reported (this is not a condition documented in OMIA or veterinary literature as a spontaneous animal disease). STAG2 is a highly conserved gene across vertebrates (ortholog present in mouse *Stag2*, zebrafish *stag2*), but no spontaneous companion-animal or livestock phenotype attributable to STAG2 variants was identified in this search. No zoonotic or cross-species transmission relevance (this is a non-infectious monogenic disorder).

---

## 15. Model Organisms

**Mouse (*Mus musculus*, NCBITaxon:10090):**
- **Constitutive Stag2-null mice**: homozygous-null embryos are **embryonic lethal at mid-gestation**, exhibiting global developmental delay and **defective heart morphogenesis**, "most prominently in structures derived from secondary heart field progenitors" — directly recapitulating and mechanistically explaining the human conotruncal/outflow-tract cardiac phenotype (relevant papers: "STAG2 cohesin is essential for heart morphogenesis," bioRxiv/PMID pending formal citation retrieval; "Essential Roles of Cohesin STAG2 in Mouse Embryonic Development and Adult Tissue Homeostasis," ScienceDirect/Cell Reports).
- **Adult conditional loss of Stag2** is tolerated (viable), indicating an embryonic-specific essential requirement — consistent with the disease model that surviving human patients (all carrying partial-function or mosaic/heterozygous-buffered alleles) retain sufficient STAG2 function to avoid the lethal embryonic phenotype seen with complete null alleles.
- This mouse model directly supports the **proposed mechanism of male embryonic lethality** with severe (truncating/null) human alleles, and models the **cardiac neural crest/secondary heart field mechanism** implicated in the human conotruncal phenotype.

**Zebrafish (*Danio rerio*, NCBITaxon:7955):**
- **stag1/stag2 double morphant/mutant studies** show that the two paralogous cohesin STAG subunits **differentially influence hematopoietic mesoderm development**, providing a model for studying tissue-specific requirements of STAG2 versus its paralog STAG1 during early vertebrate development (relevant to understanding compensatory paralog dynamics also seen in human patient fibroblasts).

**Model characteristics — recapitulation and limitations:**
- The mouse model **recapitulates** the cardiac/outflow-tract malformation mechanism and demonstrates the embryonic-lethality/dosage-sensitivity principle underlying the human sex-differential viability model.
- **Limitation**: Mouse and zebrafish models to date have focused on **embryonic lethality and cardiac/hematopoietic development**; they do not yet directly model the **postnatal neurodevelopmental phenotype** (intellectual disability, speech delay, seizures) that dominates the human clinical picture, since complete loss is embryonic lethal and viable hypomorphic/conditional models recapitulating the surviving human phenotype spectrum (missense, mosaic, or dosage-duplication alleles) are less developed in the literature surveyed here.
- No iPSC-derived organoid or patient-derived cellular model specific to MKMS neurodevelopmental phenotypes was identified in this search (an area for potential future model development, e.g., via the MorPhiC-style null-allele iPSC phenotyping approach referenced in the dismech project's own conventions, given STAG2 is exactly the kind of dosage-sensitive gene such platforms are designed to characterize).

Sources: search results citing "STAG2 cohesin is essential for heart morphogenesis" (bioRxiv), "Essential Roles of Cohesin STAG2 in Mouse Embryonic Development and Adult Tissue Homeostasis" (ScienceDirect/Cell Reports), and "Cohesin Components Stag1 and Stag2 Differentially Influence Haematopoietic Mesoderm Development in Zebrafish Embryos" (Frontiers in Cell and Developmental Biology, 2020)

---

## Summary Table: Suggested Ontology Term Bindings

| Category | Term | ID |
|---|---|---|
| Disease | Mullegama-Klein-Martinez syndrome | OMIM:301022 / MONDO:0026722 / DOID:0111845 |
| Gene | STAG2 | hgnc:11355 |
| Phenotype | Global developmental delay | HP:0001263 |
| Phenotype | Intellectual disability | HP:0001249 |
| Phenotype | Microcephaly | HP:0000252 |
| Phenotype | Microtia | HP:0008551 |
| Phenotype | Sensorineural hearing loss | HP:0000407 |
| Phenotype | Polymicrogyria | HP:0002126 |
| Phenotype | Corpus callosum hypoplasia | HP:0002079 |
| Phenotype | Ventricular septal defect | HP:0001629 |
| Phenotype | Double outlet right ventricle | HP:0001719 |
| Phenotype | Pulmonary atresia | HP:0006530 |
| Phenotype | Short stature | HP:0004322 |
| Phenotype | Seizure | HP:0001250 |
| Phenotype | Pes planus | HP:0001769 |
| Phenotype | Fifth finger clinodactyly | HP:0004209 |
| GO (BP) | Sister chromatid cohesion | GO:0007062 |
| GO (BP) | Heart development | GO:0007507 |
| GO (CC) | Cohesin complex | GO:0008278 |
| CL | Cardiac neural crest cell | CL:0008034 |
| UBERON | Corpus callosum | UBERON:0002336 |
| UBERON | Heart outflow tract | UBERON:0002080 |
| MAXO | Genetic counseling | MAXO:0000079 |
| MAXO | Surgical procedure | MAXO:0000004 |

---

## Key Caveats for Curation

1. **Evidence tier**: All clinical information derives from **case reports/case series** (n ≈ 19–20 published patients total) — not registries, cohorts, or large aggregated databases. Frequency fractions (e.g., "14/19 intellectual disability") should be flagged as small-denominator case-series proportions, not population prevalence.
2. **Orphanet gap**: No confirmed ORPHA identifier exists yet (community request pending) — do not fabricate one.
3. **Two related but distinct molecular mechanisms** exist under the STAG2-cohesinopathy umbrella: **loss-of-function/haploinsufficiency** (classical MKMS) versus **increased dosage** (Xq25 microduplication, Leroy et al. 2016) — these should likely be modeled as distinct pathophysiology nodes/subtypes rather than conflated.
4. **Sex-differential viability model** (male embryonic lethality with severe alleles) is inferential/proposed, supported by mouse Stag2-null lethality data and the observed variant-spectrum skew (missense-only in surviving males), but is not itself directly proven in humans — appropriate for a `mechanistic_hypotheses` framing rather than an established-fact framing.
5. **Somatic STAG2 mutation in cancer** (bladder cancer, Ewing sarcoma, AML/MDS) is a mechanistically related but clinically distinct phenomenon from germline MKMS and should be kept separate in any knowledge-base entry.

---

### Sources (consolidated)
- [OMIM #301022 — MULLEGAMA-KLEIN-MARTINEZ SYNDROME](https://www.omim.org/entry/301022)
- [OMIM Clinical Synopsis #301022](https://omim.org/clinicalSynopsis/301022)
- [PMC8476567 — Expanding the known phenotype of Mullegama–Klein–Martinez syndrome in male patients](https://pmc.ncbi.nlm.nih.gov/articles/PMC8476567/)
- [MDPI Genes 2025 — A Novel STAG2 Frameshift Variant in MKMS with Complex Conotruncal Heart Defect (PMC12652599)](https://www.mdpi.com/2073-4425/16/11/1364)
- [Mullegama et al. 2017, AJMG-A, PMID:28296084 — De novo loss-of-function variants in STAG2](https://pubmed.ncbi.nlm.nih.gov/28296084/)
- [Leroy et al. 2016, Clinical Genetics, PMID:25677961 — Xq25 duplication and STAG2](https://pubmed.ncbi.nlm.nih.gov/25677961/)
- [Frontiers 2022, PMC9710855 — Somatic mosaicism in STAG2-associated cohesinopathies](https://pmc.ncbi.nlm.nih.gov/articles/PMC9710855/)
- [NCBI GTR — Mullegama-Klein-Martinez syndrome (C5193008)](https://www.ncbi.nlm.nih.gov/gtr/conditions/C5193008/)
- [MalaCards — Mullegama-Klein-Martinez Syndrome](https://www.malacards.org/card/mullegama_klein_martinez_syndrome)
- [OD4RD/Main-Help-Desk Issue #492 — New ORPHAcode request for MKMS](https://github.com/OD4RD/Main-Help-Desk/issues/492)
- [ClinGen Dosage Sensitivity Curation, STAG2/HGNC:11355](https://search.clinicalgenome.org/kb/gene-dosage/HGNC:11355)
- [PMC12765388 — STAG2-truncating variants reveal mosaic inactivation and compensatory cohesin remodeling](https://pmc.ncbi.nlm.nih.gov/articles/PMC12765388/)
- Model organism references: bioRxiv "STAG2 cohesin is essential for heart morphogenesis"; ScienceDirect "Essential Roles of Cohesin STAG2 in Mouse Embryonic Development and Adult Tissue Homeostasis"; Frontiers 2020 "Cohesin Components Stag1 and Stag2 Differentially Influence Haematopoietic Mesoderm Development in Zebrafish Embryos"