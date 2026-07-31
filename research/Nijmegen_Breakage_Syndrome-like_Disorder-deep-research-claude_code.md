---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-31T05:17:45.165435'
end_time: '2026-07-31T05:24:00.494440'
duration_seconds: 375.33
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Nijmegen Breakage Syndrome-like Disorder
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
  web_search_requests: 18
  num_turns: 32
  total_cost_usd: 2.2540102999999996
  session_id: 52469bf0-4a8c-56f7-9b13-329543e26fe9
  stop_reason: end_turn
citation_count: 32
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Nijmegen Breakage Syndrome-like Disorder
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Nijmegen Breakage Syndrome-like Disorder** covering all of the
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

Now compiling the full research report.

# Nijmegen Breakage Syndrome-Like Disorder (RAD50 Deficiency): Comprehensive Research Report

## 1. Disease Information

**Overview.** Nijmegen breakage syndrome-like disorder (NBSLD) is an ultra-rare autosomal recessive chromosomal-instability syndrome caused by biallelic pathogenic variants in **RAD50**, which encodes the structural ATPase core of the MRE11–RAD50–NBS1 (MRN) DNA double-strand-break (DSB) sensing/repair complex. It is the clinical and molecular "sibling" of classic Nijmegen breakage syndrome (NBS, caused by *NBN* mutations) and ataxia-telangiectasia-like disorder (ATLD, caused by *MRE11A* mutations) — together the three MRN-complex genetic diseases. NBSLD is defined by severe pre- and postnatal growth failure, congenital/progressive microcephaly, mild-to-borderline intellectual disability, radioresistant DNA synthesis, and spontaneous chromosomal instability, **but characteristically lacks the severe combined immunodeficiency and high cancer predisposition that define classic NBS** (OMIM: "Nijmegen breakage syndrome-like disorder; NBSLD" [OMIM:613078](https://www.omim.org/entry/613078)). It is exceptionally rare: fewer than ten molecularly confirmed patients/families have been reported worldwide as of 2026 (Weemaes 1981 [clinical description predating molecular diagnosis]; Waltes et al. 2009 [PMID:19409520]; Chansel-Da Cruz et al. 2020; Ragamin et al. 2020 [PMID:32449290]; Takagi/Kanegane et al. 2023; a 2026 Chinese case; a 2026 Frontiers in Endocrinology growth-hormone case report).

**Key identifiers:**
- **OMIM:** [#613078](https://www.omim.org/entry/613078) (disorder); [*604040](https://omim.org/entry/604040) (RAD50 gene)
- **Orphanet:** [ORPHA240760](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Lng=GB&Expert=240760) (contrasted with classic NBS, [ORPHA647](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Lng=GB&Expert=647))
- **MONDO:** [MONDO:0013118](https://monarchinitiative.org/MONDO:0013118)
- **MedGen/UMLS concept:** C2751318 ([NCBI MedGen](https://www.ncbi.nlm.nih.gov/medgen/442700))
- **Gene:** RAD50, HGNC:9816, NCBI Gene ID 10111, chromosome **5q31.1**
- **ICD-10/11:** No dedicated code exists; typically coded under Q87.8 (other specified congenital malformation syndromes) or grouped with chromosome-instability syndromes
- **MeSH:** Indexed under the broader "DNA Repair-Deficiency Disorders" / "Chromosome Breakage Syndromes" headings; no dedicated MeSH descriptor

**Synonyms:** NBS-like disorder; NBSLD; RAD50 deficiency; NBS2 (informal); "Nijmegen breakage syndrome 2" (non-standard, avoid confusion with NBS itself).

**Evidence basis:** All current knowledge derives from **individual, molecularly confirmed case reports** (n≈6–9 patients across ~6 publications) rather than aggregated registries or large cohort studies — a critical distinction from classic NBS, for which the Slavic-population founder mutation has generated a >130-patient international registry (Frontiers in Immunology, 2020, PMC7819964). Prevalence estimates for NBSLD are therefore extrapolated as "<1 in 1,000,000" by OMIM/Orphanet rather than measured directly.

---

## 2. Etiology

**Disease causal factor:** NBSLD is purely monogenic/Mendelian — biallelic (homozygous or compound heterozygous) loss-of-function or hypomorphic variants in **RAD50** are necessary and sufficient to cause disease. There is no known environmental, infectious, or multifactorial contribution to primary disease causation.

**Genetic risk factors:**
- **Causal variants (biallelic, required):** Reported alleles include:
  - A maternally inherited **nonsense mutation** + paternally inherited **stop-codon readthrough mutation** causing a 66-amino-acid C-terminal protein extension (Waltes et al. 2009, [PMID:19409520](https://www.sciencedirect.com/science/article/pii/S0002929709001529))
  - Homozygous **c.2524G>A** (splice donor disruption at the final base of exon 15), producing a major transcript with exon 15 skipping → frameshift (p.Met800Phefs*7) and a minor transcript with a missense change (p.Val842Ile) (Ragamin et al. 2020, [PMC7318339](https://pmc.ncbi.nlm.nih.gov/articles/PMC7318339/))
  - **RAD50 E1035Δ** — an in-frame single-amino-acid deletion in the coiled-coil domain, acting as a "separation-of-function" allele (Chansel-Da Cruz et al. 2020, [PMC7788285](https://pmc.ncbi.nlm.nih.gov/articles/PMC7788285))
  - Compound heterozygous **c.3806_3807del (p.His1269Argfs\*2)** + **c.2531G>A (p.Ser844Asn)**, both classified VUS, in a 2026 Chinese case (ScienceDirect, S037811192600051X)
  - Two distinct compound-heterozygous variants in a patient with bone-marrow failure/immunodeficiency features (Takagi/Kanegane 2023, *J Clin Immunol*, DOI:10.1007/s10875-023-01591-8)
- **Zygosity:** Both homozygous (typically in consanguineous families) and compound heterozygous configurations reported.
- **Modifier/susceptibility (distinct condition, not NBSLD):** Monoallelic (heterozygous) RAD50 variants are instead studied as **cancer-susceptibility alleles** — e.g., RAD50 c.687delT is a low-penetrance breast-cancer risk allele in the Finnish population (PMC3006189), and RAD50 zinc-hook-domain LoF variants confer familial esophageal squamous cell carcinoma risk (PMC8472384). A 2024 systematic review/meta-analysis found **no significantly increased breast cancer risk** for most RAD50 heterozygous pathogenic variants overall (OR 0.93, 95% CI 0.74–1.16), with c.687del as a specific exception (onlinelibrary.wiley.com/doi/full/10.1002/ijc.35066).
- **Founder effects:** None established for RAD50-NBSLD (contrast with the well-characterized NBN c.657_661del5 Slavic founder mutation for classic NBS, carrier frequency 0.5–1%, PMC5148078/PMC7819964). Each NBSLD family reported to date carries private/novel variants.

**Environmental risk factors:** None identified as causal. Ionizing radiation is not a cause but is a major **secondary hazard** given cellular radiosensitivity (see Diagnostics/Prevention).

**Protective factors:** None specifically described for NBSLD. By analogy to RAD50 heterozygosity literature, monoallelic carriers are generally asymptomatic carriers, not protected individuals.

**Gene-environment interactions:** The defining cellular gene-environment interaction is **radiosensitivity** — RAD50-deficient cells fail to arrest DNA synthesis after ionizing radiation exposure ("radioresistant DNA synthesis," RDS) due to defective ATM-dependent checkpoint signaling, making diagnostic/therapeutic radiation exposure disproportionately genotoxic in these patients (multiple sources below).

---

## 3. Phenotypes

Phenotypes are drawn from the ~6 reported cases; frequencies below are counts observed across the small case series (not population-level percentages) and should be read as qualitative/case-count "frequency," per Orphanet and OMIM clinical synopsis language.

| Phenotype | Type | Onset | Frequency in reported cases | Suggested HPO term |
|---|---|---|---|---|
| Severe prenatal growth retardation / IUGR | Physical/laboratory | Prenatal | ~75% (3/4 in one series) | HP:0001511 (Intrauterine growth retardation) |
| Persistent postnatal growth restriction / short stature | Physical | Congenital–lifelong | ~100% | HP:0008897 (Postnatal growth retardation); HP:0004322 (Short stature) |
| Congenital microcephaly, often progressive | Physical | Congenital, progressive | 100% | HP:0000252 (Microcephaly); HP:0000253 (Progressive microcephaly) |
| Mild-to-borderline intellectual disability / learning difficulty | Cognitive | Childhood | Variable (borderline IQ ~85 in one patient; "no decline" reported) | HP:0006889 (Mild global developmental delay) / HP:0001256 (Intellectual disability, mild) |
| Craniofacial dysmorphism: sloping forehead, prominent eyes, broad nasal ridge, hypoplastic nasal septum, epicanthal folds, micrognathia, low-set rotated ears | Physical | Congenital | Common across cases | HP:0000340 (Sloping forehead); HP:0000520 (Proptosis); HP:0000431 (Wide nasal bridge); HP:0000286 (Epicanthus); HP:0000347 (Micrognathia); HP:0000369 (Low-set ears) |
| Spontaneous chromosomal instability (lymphocyte breakage/rearrangement) | Laboratory | — | Present in some patients, normal karyotype in others (variant-dependent) | HP:0040012 (Chromosomal instability) |
| Cellular hypersensitivity to ionizing radiation / radioresistant DNA synthesis | Laboratory | — | 100% (defining feature) | HP:0032993 (Abnormal cellular DNA damage response, closest term) — no dedicated RDS HPO term exists |
| Sensorineural hearing loss (90 dB, bilateral) | Physical/laboratory | Diagnosed age 2 in one patient | 1 reported case | HP:0000407 (Sensorineural hearing loss) |
| Speech and motor delay | Developmental | Infancy | Reported in multiple cases | HP:0000750 (Delayed speech and language development); HP:0001270 (Motor delay) |
| Chiari malformation (cerebellar tonsillar herniation) | Physical/imaging | — | 1 reported case | HP:0007099 (Chiari type I malformation) |
| Wolff-Parkinson-White pattern (without arrhythmia) | Cardiac | — | 1 reported case | HP:0011712 (Ventricular pre-excitation) |
| Bilateral clinodactyly / brachydactyly with sandal gap | Skeletal | Congenital | Multiple cases | HP:0030084 (Clinodactyly); HP:0001156 (Brachydactyly) |
| Multiple café-au-lait macules | Skin | — | Multiple cases | HP:0000957 (Café-au-lait spot) |
| Mild spasticity; slight, nonprogressive ataxia | Neurological | — | Reported (Orphanet) | HP:0001257 (Spasticity); HP:0001251 (Ataxia — nonprogressive, distinguishing from ATLD) |
| Hyperopia | Ocular | — | Reported (Orphanet) | HP:0000540 (Hyperopia) |
| Widely spaced nipples | Physical | Congenital | Reported (Orphanet) | HP:0006610 (Wide intermamillary distance) |
| Normal sexual development / no hormonal deficiency | — | — | Consistent across all cases | Absence of HP:0000811 (Hypogonadism) |
| **Absent** severe/recurrent infections, immunodeficiency, myelodysplasia, or early neurodegeneration | — | — | Defining negative finding distinguishing NBSLD from NBS/ATLD | — |
| Bone marrow failure (thrombocytopenia, anemia, neutropenia, aplastic anemia) + B-lymphocyte deficiency | Laboratory/hematologic | Variable, one case age 7 | Reported in a phenotypic-spectrum-expanding subset (Chansel-Da Cruz 2020; Takagi 2023) — **contradicts the "no immunodeficiency" rule** for certain hypomorphic/separation-of-function alleles | HP:0005528 (Bone marrow hypocellularity); HP:0004313 (Decreased circulating antibody level); HP:0002846 (Abnormal B cell count) |
| Early-onset cataract (age 10) | Ocular | Childhood | 1 case (Chansel-Da Cruz) | HP:0000518 (Cataract) |
| Bilateral cryptorchidism, distinctive craniofacial features (Chinese case) | Physical | Congenital | 1 case | HP:0000028 (Cryptorchidism) |

**Quality-of-life impact:** No formal QoL instrument (EQ-5D/SF-36) data exist for this ultra-rare disease. Reported functional impact centers on growth failure requiring endocrine evaluation, hearing loss requiring amplification, and developmental/learning support; notably, unlike classic NBS, **no reported neurodegeneration or decline** in intellectual/motor function over time in the two best-characterized patients ("no decline of intellectual or motor functions has been observed").

---

## 4. Genetic/Molecular Information

**Causal gene:** RAD50 (RAD50 double-strand break repair protein), OMIM [*604040](https://omim.org/entry/604040), HGNC:9816, chr 5q31.1, NCBI Gene 10111.

**Gene/protein function:** RAD50 is a structural-maintenance-of-chromosomes (SMC)-family ATPase that, together with MRE11 and NBS1, forms the MRN complex — among the earliest sensors of DNA double-strand breaks. RAD50 uses its ABC-type ATPase domain, a Zn-hook dimerization motif, and long antiparallel coiled-coils to bridge broken DNA ends, gate MRE11 nuclease access for 5′→3′ end resection, tether sister chromatids, and license ATM kinase activation for checkpoint signaling (PMC4494100; GeneCards RAD50).

**Pathogenic variant classes reported in NBSLD:**
- **Nonsense/truncating:** classic LoF, near-complete loss of protein
- **Stop-codon readthrough (extension) mutations:** abnormal C-terminal extension impairing folding/stability
- **Splice-site disruption:** e.g., c.2524G>A causing exon-15 skipping/frameshift, with a minor missense-producing transcript as a partial "leaky" allele
- **In-frame single-residue deletion (separation-of-function):** RAD50 E1035Δ in the coiled-coil domain — selectively impairs DNA end resection/HR/replication-fork function while **sparing** ATM-dependent checkpoint signaling, illustrating that NBSLD's clinical spectrum can fractionate along distinct MRN sub-functions (PMC7788285)
- **Compound heterozygous frameshift + missense (VUS):** e.g., c.3806_3807del + c.2531G>A in the 2026 Chinese case, with the frameshift allele shown by Western blot to destabilize RAD50 protein

**Variant classification:** Most reported variants are classified pathogenic/likely pathogenic per ACMG/AMP given segregation, protein-loss functional data, and de novo absence in gnomAD; two recent Chinese-case variants remain formally VUS pending further functional confirmation.

**Allele frequency:** RAD50 loss-of-function alleles are individually ultra-rare in population databases — e.g., the Ragamin et al. splice variant had a minor allele frequency of only 1.072×10⁻⁴ in gnomAD, observed only in heterozygous state (consistent with a rare, non-founder recessive allele).

**Somatic vs. germline:** All NBSLD-causing variants are **constitutional/germline**. (Somatic RAD50 alterations are separately studied in sporadic cancers via COSMIC/TCGA but are not part of this Mendelian disease.)

**Functional consequences at the protein/cellular level:**
- Near-undetectable RAD50 protein by Western blot in patient fibroblasts, with secondary reduction of MRE11 and NBS1 protein levels (complex destabilization) — "RAD50 protein was almost undetectable in the F583 fibroblasts," with a "more pronounced reduction than previously reported" in the first patient (PMC7318339)
- Failure of DNA-damage-induced MRN nuclear focus formation
- Impaired ATM autophosphorylation and downstream substrate phosphorylation (CHK2 pSer19, KAP1/TRIM28 pSer824) after irradiation — "barely detectable at 6 Gy"
- Radioresistant DNA synthesis (failure of the intra-S-phase checkpoint) mimicking ataxia-telangiectasia cells
- Chromosomal instability in metaphase spreads (variable — one patient had a normal karyotype despite RDS, showing phenotypic/cytogenetic dissociation across alleles)

**Modifier genes:** None specifically established for NBSLD; by extension from MRN biology, TP53/ATM pathway status could theoretically modulate cellular phenotype but this is not documented in patients.

**Epigenetic information:** No disease-specific DNA methylation/chromatin studies have been published for RAD50-NBSLD specifically (contrast with broader MRN-complex chromatin-remodeling literature, PMID:17713585).

**Chromosomal abnormalities:** NBSLD is not a copy-number/structural chromosomal disorder — it is a sequence-level Mendelian gene defect that secondarily produces acquired chromosomal instability (translocations, breaks) as a cellular biomarker, not a germline CNV.

---

## 5. Environmental Information

- **Environmental factors:** Not causal, but critically relevant to **iatrogenic risk**: diagnostic/therapeutic ionizing radiation (X-ray, CT) poses disproportionate genotoxic/carcinogenic risk in RAD50-deficient patients due to radiosensitivity and impaired DSB repair; MRI and ultrasound are preferred alternatives (per management recommendations extrapolated from NBS and stated explicitly by Ragamin et al. 2020).
- **Lifestyle factors:** No specific lifestyle risk-modifying data published (disease is congenital/genetic, onset neonatal).
- **Infectious agents:** Not implicated in causation. Because immunodeficiency is largely (though not universally) absent in NBSLD — unlike classic NBS — recurrent infection susceptibility is not a defining environmental interaction, except in the minority of reported patients with bone-marrow failure/immunologic involvement (Takagi 2023; Chansel-Da Cruz 2020), where infection risk parallels that of primary immunodeficiency generally.

---

## 6. Mechanism / Pathophysiology

**Causal chain (trigger → clinical manifestation):**

1. **Molecular trigger:** Biallelic RAD50 variants → loss/destabilization of RAD50 protein → destabilization of the entire MRN (MRE11-RAD50-NBS1) complex (secondary reduction of MRE11 and NBS1 protein even though those genes are wild-type).
2. **Cellular DSB-sensing failure:** Loss of MRN focus formation at DNA double-strand breaks → failure to recruit and activate ATM kinase → loss of ATM-dependent phosphorylation cascade (CHK2, KAP1/TRIM28, and other substrates) → failure of the intra-S-phase checkpoint, manifesting as **radioresistant DNA synthesis**.
3. **Genome instability:** Impaired DSB end-resection (MRE11 nuclease access gated by RAD50 ATPase cycling) → defective homologous recombination repair → spontaneous and radiation-induced chromosomal instability (breaks, rearrangements) in some alleles; separation-of-function alleles (e.g., E1035Δ) show this resection/HR defect can be **dissociated** from the ATM-signaling defect, since ATM signaling and G2/M checkpoint remained intact in that patient despite defective resection.
4. **Developmental consequence:** Chronic replication stress and genome instability during embryonic/fetal neurodevelopment and somatic growth are hypothesized (by analogy to NBS/ATLD/microcephaly-primary genes) to drive **severe growth failure and progressive microcephaly**, likely reflecting impaired proliferation and increased apoptosis of neural progenitor and other rapidly dividing cell pools — the same final-common mechanism invoked broadly for "microcephaly-DNA repair" disorders.
5. **Divergence from NBS/ATLD:** Because RAD50 hypomorphic alleles in reported patients retain partial complex function (unlike complete NBS1 or MRE11 loss), the downstream **immune and oncogenic consequences are attenuated** in most patients — plausibly because sufficient residual MRN activity supports V(D)J recombination/class-switch recombination and tumor-suppressive checkpoint function, while growth/neurodevelopmental pathways (more sensitive to replication stress) are still impaired. This is a **hypothesis**, not established by direct mechanistic study, and the emerging bone-marrow-failure phenotype in some patients (Takagi 2023, Chansel-Da Cruz 2020) shows this attenuation is allele-dependent and incomplete.

**Molecular pathways:** DNA damage response (DDR) / ATM-CHK2 checkpoint signaling pathway (KEGG hsa03450 Non-homologous end-joining; hsa03440 Homologous recombination; Reactome "DNA Double-Strand Break Repair").

**Cellular processes (GO terms):**
- GO:0006302 double-strand break repair
- GO:0000724 double-strand break repair via homologous recombination
- GO:0007049 cell cycle / GO:0000077 DNA damage checkpoint signaling
- GO:0006281 DNA repair
- GO:0004725 (not applicable here; relevant to other modules) — instead: GO:0005524 ATP binding (RAD50 ATPase activity)

**Protein dysfunction:** Predominantly **loss of function** via destabilization/truncation; one well-characterized allele (E1035Δ) demonstrates a **separation-of-function** mechanism — selective loss of DNA-end-resection/replication-fork functions with preserved ATM-signaling function, attributed to disruption of coiled-coil heptad-repeat conformational dynamics (PMC7788285).

**Metabolic changes:** Not specifically documented for NBSLD.

**Immune system involvement:** Variable and allele-dependent — absent in "classic" NBSLD (Waltes 2009, Ragamin 2020), but documented in an emerging subset with bone marrow failure, B-lymphocyte deficiency, and impaired T-lymphopoiesis (Chansel-Da Cruz 2020: "virtual absence of B lymphocytes; impaired T lymphopoiesis"; Takagi 2023 patient with immunodeficiency).

**Tissue damage mechanisms:** Genome instability/replication stress in high-turnover progenitor pools (neural, hematopoietic, germline) rather than classical oxidative/ischemic/fibrotic injury.

**Biochemical abnormalities:** Defective RAD50 ATPase/Zn-hook function; failure of ATM autophosphorylation (Ser1981) and substrate phosphorylation after ionizing radiation.

**Suggested cell types (CL terms) and biological processes (GO terms) for pathophysiology nodes:**
- CL:0000034 stem cell / CL:0000037 hematopoietic stem cell (bone-marrow-failure subset)
- CL:0000542 lymphocyte / CL:0000236 B cell / CL:0000084 T cell (immunodeficiency subset)
- CL:0011020 neural progenitor cell (microcephaly mechanism, by analogy)
- GO:0000724 double-strand break repair via homologous recombination
- GO:0031573 intra-S DNA damage checkpoint signaling
- GO:0006974 DNA damage response

**Molecular profiling / advanced technologies:** No transcriptomic, proteomic, metabolomic, single-cell, or spatial-omics datasets specific to human NBSLD patient tissue have been published (GEO/ArrayExpress search did not return disease-specific datasets); available molecular data are limited to targeted Western blot, immunofluorescence (MRN foci), and functional cellular assays (RDS, chromosome breakage, ATM-substrate phosphoblotting) in patient-derived fibroblasts/lymphoblasts.

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Craniofacial skeleton/brain (microcephaly, dysmorphic facies), skeletal system (growth plates — short stature, brachydactyly/clinodactyly), skin (café-au-lait macules)
- **Secondary:** Inner ear (sensorineural hearing loss), cardiac conduction system (WPW pattern in one case), cerebellum/craniocervical junction (Chiari malformation), ocular (hyperopia, cataract in one allele), hematopoietic system and immune organs (bone marrow, lymphoid tissue — in the emerging severe subset), testes (cryptorchidism in one case)
- **Body systems:** Musculoskeletal, nervous, integumentary, and — in a subset — hematologic/immune systems

**Tissue and cell level:**
- Neural progenitor cells and developing cerebral cortex (microcephaly)
- Growth-plate chondrocytes/osteoblasts (short stature, skeletal dysmorphism)
- Cochlear hair cells / auditory neuroepithelium (sensorineural hearing loss)
- Hematopoietic stem/progenitor cells, B and T lymphocytes (bone marrow failure subset)
- Fibroblasts (the primary experimental cell type used for all functional/cellular studies — radiosensitivity, MRN foci, RDS assays)

**Subcellular level (GO Cellular Component):**
- GO:0005634 nucleus (site of MRN complex action)
- GO:0000784 nuclear chromosome, telomeric region (MRN telomere maintenance role)
- GO:0035861 site of double-strand break

**Localization (UBERON):**
- UBERON:0000955 brain; UBERON:0001851 cortex
- UBERON:0001690 ear / UBERON:0001846 cochlea
- UBERON:0002371 bone marrow
- UBERON:0002370 thymus (T-lymphopoiesis)
- UBERON:0000178 blood
- Bilateral/symmetric involvement typical (microcephaly, growth failure); no lateralization reported.

---

## 8. Temporal Development

**Onset:** Congenital/prenatal onset — severe intrauterine growth restriction and microcephaly are present from birth; postnatal growth restriction and microcephaly (often progressive) continue through childhood. This places NBSLD onset squarely in the **neonatal/congenital** category (OMIM lists "age of onset in the neonatal period").

**Progression:**
- **Growth/head circumference:** Progressive postnatal microcephaly documented in longitudinal case follow-up (e.g., patient followed to age 15 showed head circumference declining further below population norms).
- **Neurocognitive:** Notably **stable, non-progressive** course in the best-documented patients — "no decline of intellectual or motor functions has been observed," and ataxia (when present) is described as "slight and nonprogressive," a key distinguishing feature from the **progressive** cerebellar degeneration of ATLD.
- **Hematologic/immune (severe subset):** Progressive bone marrow failure has been documented in at least one patient, evolving over time (age 7 onward) to aplastic anemia — a distinct and more severe disease trajectory.
- **Disease course pattern:** Predominantly **stable/static** dysmorphic-growth phenotype punctuated by an occasional **progressive** hematologic/immunologic trajectory in a minority of alleles.
- **Duration:** Chronic, lifelong condition; the oldest reported patient was followed to at least 23 years of age (Waltes et al. 2009) without malignancy.

**Patterns:**
- No spontaneous remission described (structural/growth features are static; hematologic decline in the severe subset does not remit spontaneously).
- **Critical periods:** Prenatal and early postnatal periods are the critical windows for growth/head-circumference deficits, given congenital onset; genetic evaluation prior to any elective growth-hormone therapy is now explicitly recommended as a "critical intervention window" issue, since GH was started empirically (without genetic workup) in the 2026 Chinese case before RAD50 deficiency was recognized.

---

## 9. Inheritance and Population

**Epidemiology:** Prevalence <1 per 1,000,000 (OMIM/Orphanet estimate); incidence not separately calculable given fewer than 10 total published patients. This contrasts sharply with classic NBS, whose Slavic founder mutation gives regional prevalence up to >20 per 1,000,000 in parts of Belarus/Ukraine (PMC7819964).

**Inheritance pattern:** Autosomal recessive (AR); all reported cases are homozygous or compound heterozygous for biallelic RAD50 variants.

**Penetrance:** Presumed complete for the core growth/microcephaly phenotype in biallelic carriers (all reported patients manifest disease); however, phenotypic severity varies considerably by allele (from mild "classic" NBSLD to severe bone-marrow-failure phenotypes), suggesting **variable expressivity** driven largely by hypomorphic vs. separation-of-function vs. near-null allele combinations rather than incomplete penetrance per se.

**Genetic anticipation:** Not described/applicable (not a repeat-expansion disorder).

**Germline mosaicism:** Not specifically reported for RAD50-NBSLD.

**Founder effects:** None established (contrast NBN c.657del5 Slavic founder mutation, carrier frequency 0.5–1%, PMC5148078). Each RAD50-NBSLD family reported carries private variants; the disorder has been documented in Turkish (consanguineous), European, and Chinese families, arguing against a single founder population.

**Consanguinity:** A major risk factor in reported cases — e.g., the second reported patient (Ragamin et al. 2020) was homozygous for a novel variant, born to consanguineous Turkish parents.

**Carrier frequency:** Not established at a population level (each variant is individually ultra-rare; gnomAD MAF ~1.07×10⁻⁴ heterozygous-only for one reported allele).

**Population demographics:** Reported patients span European (Dutch/German, original 2009 report), Turkish, and Chinese ancestries — no clear ethnic clustering, unlike NBS's strong Slavic association.

**Geographic distribution:** No endemic region identified; cases are geographically scattered case reports (Netherlands/Germany, Turkey, China, Japan [Takagi/Kanegane group]).

**Sex ratio:** Both male and female patients reported (e.g., 23-year-old female in Waltes 2009; 15-year-old female in Ragamin 2020; male patients in the Chinese/GH case reports) — no established sex predilection given small numbers.

**Age distribution:** Diagnoses reported from infancy through the mid-20s in the oldest documented patient; disease is lifelong from a congenital onset.

---

## 10. Diagnostics

**Clinical laboratory tests:**
- **Radioresistant DNA synthesis (RDS) assay** — the key functional diagnostic test, measuring failure of DNA synthesis suppression after ionizing radiation exposure in patient fibroblasts/lymphocytes; abnormal (elevated) RDS is shared with ataxia-telangiectasia, NBS, and ATLD, so it is not RAD50-specific by itself.
- **Chromosomal breakage/instability analysis** (metaphase cytogenetics) — variably abnormal.
- **Clonogenic radiosensitivity assay** (colony survival after ionizing radiation) — demonstrates hypersensitivity.
- **Western blot for RAD50/MRE11/NBS1 protein levels** in patient-derived fibroblasts — shows absent/reduced RAD50 with secondary reduction of complex partners; this is the most disease-specific functional readout.
- **Immunofluorescence for MRN nuclear foci** after DNA damage — shows failure of focus formation.
- **ATM-pathway phosphoprotein assays** — absent/reduced phospho-CHK2 (Ser19), phospho-KAP1/TRIM28 (Ser824) post-irradiation.

**Biomarkers:** No circulating serum/plasma biomarker exists; diagnosis relies on cellular functional assays plus molecular genetics. (For context, classic NBS diagnostic workup also includes serum immunoglobulin levels and lymphocyte subsets — largely normal in NBSLD, distinguishing it.)

**Imaging:** Brain MRI recommended over CT (radiosensitivity) — has shown Chiari malformation in at least one patient; skeletal survey for growth/skeletal dysmorphism; **ionizing-radiation imaging (X-ray, CT) should be minimized** given cellular radiosensitivity.

**Functional/electrophysiology tests:** Audiometry (identified 90 dB bilateral sensorineural hearing loss in one patient); ECG (identified WPW pattern in one patient, without arrhythmia).

**Biopsy/histopathology:** Not a standard diagnostic requirement; disease diagnosis relies on fibroblast functional assays rather than tissue biopsy/histopathology.

**Genetic testing:**
- **Recommended approach:** Given phenotypic overlap with NBS/ATLD/other microcephaly-DNA-repair disorders, a **multi-gene panel** covering RAD50, NBN, MRE11A, ATM, and related chromosomal-instability genes is the recommended first-line approach, escalating to **whole-exome sequencing (WES)** — which is how essentially all reported NBSLD cases have actually been solved (trio-based WES in the recent Chinese case; WES in the Takagi 2023 case).
- **Single-gene RAD50 sequence analysis** (all coding exons) is commercially available (NCBI GTR test ID 578298, [ncbi.nlm.nih.gov/gtr/tests/578298](https://www.ncbi.nlm.nih.gov/gtr/tests/578298/)).
- **Chromosomal microarray/karyotype/FISH:** Not primary diagnostic tools (NBSLD is a sequence-level, not copy-number, disorder), though karyotype may show acquired instability.
- **Whole genome sequencing (WGS):** Not specifically reported as used but would capture splice-region variants like c.2524G>A that WES might miss without careful splice analysis.
- **Functional RNA studies (RT-PCR):** Essential for confirming splice-site variant pathogenicity (as done for c.2524G>A, revealing exon-15-skipping and missense transcripts).

**Clinical diagnostic criteria:** No formal consensus diagnostic criteria society guideline exists (disease is too rare); working diagnosis is based on the combination of (1) severe pre/postnatal growth failure + microcephaly, (2) laboratory evidence of radiosensitivity/RDS, and (3) biallelic RAD50 variants, **with exclusion of the immunodeficiency/cancer features that would instead suggest classic NBS or a more severe RAD50-null/bone-marrow-failure phenotype.**

**Differential diagnosis:**
- Classic Nijmegen breakage syndrome (NBN mutations) — distinguished by severe combined immunodeficiency and high lymphoid malignancy risk
- Ataxia-telangiectasia-like disorder (MRE11A mutations) — distinguished by progressive cerebellar ataxia/neurodegeneration, typically without microcephaly
- Ataxia-telangiectasia (ATM mutations)
- Other primary microcephaly syndromes (MCPH genes)
- Seckel syndrome and other growth-failure/microcephaly syndromes
- Fanconi anemia and other bone-marrow-failure syndromes (relevant differential for the severe subset with cytopenias)

**Screening:** No newborn screening program exists (disease too rare, no biochemical marker). Prenatal diagnosis/carrier screening is feasible via targeted molecular testing once a familial variant is known (as for any AR Mendelian disease), particularly relevant given documented consanguinity in some families.

---

## 11. Outcome / Prognosis

**Survival/mortality:** No formal survival statistics exist given the tiny cohort. The oldest well-documented patient survived to at least 23 years without malignancy (Waltes et al. 2009); a second patient was followed to 15 years without malignancy (Ragamin et al. 2020). This suggests a **substantially better long-term prognosis than classic NBS**, where malignancy (chiefly B-cell lymphoma) is the dominant cause of premature mortality, with lymphoid cancer developing in a large proportion of NBS patients by young adulthood.

**Morbidity/function:** Growth failure (short stature), microcephaly, and mild learning difficulties are the chronic morbidities; hearing loss and skeletal anomalies add functional burden in some patients. Critically, **no progressive neurological decline** has been documented in the core NBSLD phenotype (contrasting with ATLD's progressive ataxia and NBS's neurodevelopmental concerns).

**Disease course/complications:**
- Core NBSLD: stable, non-progressive intellectual/motor course; growth and craniofacial features are static congenital findings.
- Severe subset: progressive bone marrow failure (aplastic anemia), recurrent infection risk from B/T lymphopenia, early cataract — a materially worse prognosis paralleling inherited bone-marrow-failure syndromes.
- Unknown/theoretical malignancy risk: because RAD50 is a DNA-repair/tumor-suppressor-pathway gene and its paralogs (NBN, MRE11A) confer cancer predisposition, **authors explicitly recommend managing NBSLD patients with NBS-level cancer surveillance vigilance despite the absence of confirmed malignancy in the literature to date** — an important prognosis caveat: absence of evidence for cancer risk (small n, sometimes short follow-up) is not evidence of absence.

**Prognostic factors:** Allele type appears to be the dominant driver of prognosis — near-null/complex-destabilizing alleles associate with the "classic" milder NBSLD phenotype in some patients, whereas certain alleles (e.g., RAD50 E1035Δ separation-of-function, or the compound heterozygous genotype in the Takagi 2023 patient) associate with a bone-marrow-failure/immunodeficiency trajectory — suggesting genotype-phenotype correlation exists but is not yet fully mapped across the small number of known alleles.

**Prognostic biomarkers:** None validated; residual RAD50/MRE11/NBS1 protein level and degree of ATM-signaling preservation are plausible (but unvalidated) prognostic correlates based on the mechanistic literature.

---

## 12. Treatment

There is **no disease-specific or curative therapy** for RAD50-NBSLD; management is supportive and extrapolated largely from classic NBS protocols, adjusted for the (usually) milder immune phenotype.

**Pharmacotherapy:**
- No approved pharmacotherapy targets the RAD50/MRN defect itself.
- **Recombinant human growth hormone (rhGH)** has been used off-label for short stature — a 2026 case report (Frontiers in Endocrinology) documented **5 years 9 months of rhGH** (0.15–0.2 IU/kg/day, IGF-1-titrated) in a RAD50-NBSLD patient, improving height from −3.35 SD to −1.28 SD (average 7.3 cm/year growth velocity) with **no adverse reactions observed** and no tumor evidence at 5-year post-discontinuation follow-up. However, the authors explicitly flag this as an **"unplanned"** treatment response (GH was started before genetic diagnosis) and caution that **genetic evaluation should precede GH therapy** in syndromic short stature given the theoretical malignancy risk associated with impaired DNA-repair capacity — a risk-benefit issue specific to DNA-repair-deficiency syndromes (GH/IGF-1 signaling is mitogenic).
- **IVIG replacement and prophylactic antibiotics** — used empirically in the immunodeficient/bone-marrow-failure subset, extrapolated from NBS management (not specifically trialed in NBSLD but standard for the phenotypic overlap group).

**Advanced therapeutics:**
- **Hematopoietic stem cell transplantation (HSCT)** — not reported specifically for RAD50-NBSLD in the literature reviewed, but would be the standard consideration for the bone-marrow-failure subset (by analogy to other inherited BMF syndromes and to NBS management for severe immunodeficiency), with the caveat that conditioning-regimen radiosensitivity would require **radiation- and alkylator-reduced conditioning protocols**, again by analogy to ATM/MRN-pathway-deficient HSCT literature.
- Gene therapy, cell therapy (beyond HSCT), RNA-based therapies, and targeted molecular therapies have **not been reported** for this disorder.

**Surgical/interventional:** No disease-specific surgical intervention; management of individual complications (e.g., cataract extraction, Chiari decompression if symptomatic) would follow standard surgical practice, with radiologic planning shifted toward non-ionizing modalities where feasible.

**Supportive/rehabilitative care:**
- Speech/motor developmental therapy (physical therapy, occupational therapy, speech therapy) for developmental delay
- Hearing aids/audiologic support for sensorineural hearing loss
- Nutritional support for growth failure
- Multidisciplinary genetics, endocrinology, hematology/immunology, and neurology follow-up

**Experimental treatments:** No registered clinical trials specific to RAD50-NBSLD were identified in this search (ClinicalTrials.gov has no RAD50-NBSLD-specific studies; broader NBS-related trials focus on classic NBN-mutated NBS, e.g., cancer surveillance and antioxidant studies).

**Treatment outcomes/adverse events:** The only quantified treatment-outcome data available are from the rhGH case (above) — no other systematic treatment-response data exist.

**Treatment strategy / algorithm (extrapolated from NBS + expert case-report recommendations):**
1. Confirm molecular diagnosis (WES/panel) **before** initiating any growth-promoting or immunomodulatory therapy.
2. Avoid ionizing-radiation-based imaging; prefer MRI/ultrasound.
3. Baseline and periodic assessment of growth, immune function (immunoglobulins, lymphocyte subsets), cognitive development, and hematologic parameters (given emerging BMF phenotype).
4. Consider rhGH for growth failure only after genetic counseling on theoretical cancer-risk trade-offs.
5. Empiric cancer surveillance (physical exam, blood counts, imaging as tolerated) analogous to NBS protocols, pending disease-specific evidence.
6. Avoid live vaccines if any immunodeficiency is confirmed (extrapolated from NBS guidance).

**Suggested MAXO terms:**
- MAXO:0000647 chemotherapy — not applicable (no current chemo indication)
- MAXO:0010039 organ/hematopoietic transplantation — for HSCT in BMF subset
- MAXO:0000011 physical therapy; MAXO:0000930 speech therapy; MAXO:0001351 occupational therapy — for developmental support
- MAXO:0000950 supportive care
- Pharmacotherapy: NCIT:C15986 (generic) with `therapeutic_agent` bound to CHEBI/NCIT term for somatropin (recombinant human growth hormone)

---

## 13. Prevention

**Primary prevention:** Not applicable in the traditional sense (Mendelian genetic disease); the only "primary prevention" lever is **genetic/reproductive counseling** for known carrier couples (especially consanguineous families) to inform reproductive decision-making, and **preimplantation genetic diagnosis (PGD)** or prenatal testing once a familial pathogenic variant is identified.

**Secondary prevention (early detection):** Early molecular diagnosis via WES/panel testing in any infant presenting with severe pre/postnatal growth restriction plus congenital microcephaly (particularly without the severe immunodeficiency/infection pattern that would suggest classic NBS) allows earlier initiation of radiation-avoidance precautions and surveillance.

**Tertiary prevention:** Avoidance of ionizing radiation exposure (diagnostic and therapeutic) is the single most actionable, disease-specific preventive measure, given documented cellular radiosensitivity — this is analogous to, but with less certain magnitude of risk than, the well-established radiation-avoidance guidance for classic NBS and ataxia-telangiectasia.

**Immunization:** No NBSLD-specific vaccine guidance published; for the subset with confirmed immunodeficiency, standard primary-immunodeficiency vaccine precautions (avoidance of live vaccines pending immune assessment) would apply by extrapolation from NBS/PID management, not from disease-specific trial data.

**Screening/genetic counseling:** Carrier screening and cascade testing in relatives of an index case; genetic counseling emphasizing autosomal recessive inheritance (25% recurrence risk per pregnancy for carrier couples) and — as newly flagged by the 2026 GH case report — **counseling before elective growth-promoting therapy** given the theoretical mitogenic/malignancy-risk interaction with underlying DNA-repair deficiency.

**Behavioral interventions / public health / prophylaxis:** Not applicable beyond the radiation-avoidance and infection-precaution measures already described; this is not a disease with population-level environmental or infectious prevention levers.

---

## 14. Other Species / Natural Disease

**Taxonomy:** RAD50 is deeply evolutionarily conserved from yeast to human (NCBITaxon:9606 Homo sapiens for the human disease; orthologs exist across essentially all eukaryotes given the ancient, essential nature of DSB repair).

**Naturally occurring disease in other species:** No naturally occurring veterinary RAD50-deficiency syndrome analogous to human NBSLD has been reported in companion animals or wildlife (OMIA search did not surface a RAD50-associated natural veterinary disease); this contrasts with many other Mendelian disease genes that do have recognized veterinary/naturally-occurring counterparts.

**Comparative biology / orthologous genes:**
- Mouse: *Rad50* (MGI:109292)
- Yeast: RAD50 (the original gene discovery organism — S. cerevisiae radiation-sensitive mutant screens)
- Medaka fish: rad50 (used for an engineered disease model, see below)
- Drosophila: Mre11-Rad50-Nbs ortholog complex (implicated in telomere capping during embryogenesis, PMID:19520832)

**Transmission:** Not applicable (non-infectious, non-zoonotic genetic disease).

---

## 15. Model Organisms

**Genetic models:**
- **Mouse complete Rad50 knockout:** **Embryonic lethal** — a null Rad50 mutation, which presumably fully abrogates the structural role of the Mre11 complex, results in early embryonic death, underscoring RAD50's essential role in genome maintenance and precluding a viable full-knockout model of human disease.
- **Rad50^S/S hypomorphic mice** (the disease-relevant model): a separation-of-function allele preserving MRN complex integrity but reducing function. Phenotype: partial embryonic lethality; shortened lifespan; progressive loss of germline and hematopoietic cells; death from **hematopoietic failure by ~3 months of age**; growth defects; **cancer predisposition**; cultured cells show increased spontaneous apoptosis and chromosomal instability; telomere-maintenance defects due to loss of MRN integrity (PMID:12208847, genesdev.cshlp.org/content/16/17/2237). This model recapitulates the **cancer-predisposition and bone-marrow-failure** arm of the human phenotypic spectrum (i.e., the severe subset) better than the "classic" milder human NBSLD presentation, illustrating that mouse hypomorphic models may better model the severe end of the human allelic spectrum.
- **Medaka fish CRISPR/Cas9 rad50 2-bp-deletion model** (PLOS ONE 2023, PMC10129005): heterozygous rad50Δ2/+ medaka developed tumors in 8/10 fish and had reduced median survival (54.2 ± 2.6 weeks vs. 65.7 ± 1.1 weeks in controls); homozygous rad50Δ2/Δ2 fish were semi-lethal and reproduced most major **ataxia-telangiectasia** phenotypic features including ataxia — providing a tractable, transparent vertebrate model for both the cancer-predisposition and neurological aspects of MRN-complex disease, though notably modeling an AT-like rather than a growth-failure/microcephaly phenotype.

**Model characteristics — recapitulation vs. limitations:**
- Both the mouse Rad50S/S and medaka rad50 models capture the **cancer predisposition and hematopoietic/genome-instability** dimensions of RAD50 dysfunction robustly.
- Neither model fully recapitulates the **core "classic" human NBSLD phenotype** (severe growth restriction, progressive but non-degenerative microcephaly, absence of cancer/immunodeficiency) — a **human-model mismatch**: the animal models instead better represent the more severe bone-marrow-failure/malignancy-prone end of the human allelic spectrum, or an AT-like neurological phenotype, rather than the mild "classic" NBSLD growth/craniofacial phenotype first described by Waltes et al. This gap is consistent with the broader observation that complete or near-complete RAD50 loss is poorly tolerated in mammals (embryonic lethal), so viable human patients necessarily carry partial-function hypomorphic alleles whose precise residual activity is difficult to reproduce precisely in animal knock-in models.
- **Applications:** These models remain valuable for studying MRN-complex-dependent tumor suppression, hematopoietic stem cell maintenance, ATM-pathway biology, and telomere maintenance mechanisms relevant to the RAD50-disease spectrum broadly.

**Cellular/in vitro models:** Patient-derived primary fibroblasts (the dominant experimental system in every published human case report) are used for radiosensitivity, RDS, chromosome-breakage, MRN-focus, and ATM-substrate-phosphorylation assays; no iPSC-derived model of RAD50-NBSLD has been reported.

**Resources:** MGI (mouse, Rad50 MGI:109292); no dedicated RAD50-NBSLD registry exists in ZFIN/FlyBase/WormBase; IMPC/KOMP conditional-knockout resources for Rad50 exist for research use given the lethality of full constitutive knockout.

---

## Summary Table of Key Ontology Term Suggestions

| Category | Terms |
|---|---|
| Disease | MONDO:0013118; OMIM:613078; ORPHA:240760 |
| Gene | HGNC:9816 (RAD50); OMIM:604040 |
| Key phenotypes | HP:0000252 (Microcephaly), HP:0001511 (IUGR), HP:0008897 (Postnatal growth retardation), HP:0040012 (Chromosomal instability), HP:0000407 (SNHL), HP:0001156 (Brachydactyly), HP:0030084 (Clinodactyly), HP:0000957 (Café-au-lait spot), HP:0001251 (Ataxia, nonprogressive), HP:0007099 (Chiari malformation), HP:0005528 (Bone marrow hypocellularity — severe subset) |
| Cell types | CL:0000057 fibroblast (primary experimental cell); CL:0000037 hematopoietic stem cell; CL:0000236 B cell; CL:0000084 T cell |
| Biological processes | GO:0000724 (DSB repair via HR), GO:0006974 (DNA damage response), GO:0031573 (intra-S DNA damage checkpoint) |
| Treatment | MAXO:0010039 (transplantation, BMF subset); NCIT:C15986 (Pharmacotherapy) + therapeutic_agent for somatropin/rhGH |

---

## Sources

- [Nijmegen Breakage Syndrome-Like Disorder - MalaCards](https://www.malacards.org/card/nijmegen_breakage_syndrome_like_disorder)
- [OMIM #613078 - NIJMEGEN BREAKAGE SYNDROME-LIKE DISORDER; NBSLD](https://www.omim.org/entry/613078)
- [OMIM Clinical Synopsis #613078](https://omim.org/clinicalSynopsis/613078)
- [OMIM *604040 - RAD50 DOUBLE-STRAND BREAK REPAIR PROTEIN; RAD50](https://omim.org/entry/604040)
- [Orphanet: Nijmegen breakage syndrome-like disorder (ORPHA240760)](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Lng=GB&Expert=240760)
- [Orphanet: Nijmegen breakage syndrome (ORPHA647)](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Lng=GB&Expert=647)
- [Monarch Initiative: MONDO:0013118](https://monarchinitiative.org/MONDO:0013118)
- [NCBI MedGen C2751318](https://www.ncbi.nlm.nih.gov/medgen/442700)
- [NCBI GTR RAD50 sequence test](https://www.ncbi.nlm.nih.gov/gtr/tests/578298/)
- [Waltes et al. 2009, "Human RAD50 Deficiency in a Nijmegen Breakage Syndrome-like Disorder" (Am J Hum Genet), PMID:19409520](https://www.sciencedirect.com/science/article/pii/S0002929709001529)
- [Ragamin et al. 2020, "Human RAD50 deficiency: Confirmation of a distinctive phenotype" (Am J Med Genet A), PMC7318339](https://pmc.ncbi.nlm.nih.gov/articles/PMC7318339/)
- [Chansel-Da Cruz et al. 2020, RAD50 E1035Δ separation-of-function mutation, PMC7788285](https://pmc.ncbi.nlm.nih.gov/articles/PMC7788285)
- [Takagi/Kanegane et al. 2023, "Bone Marrow Failure and Immunodeficiency Associated with Human RAD50 Variants" (J Clin Immunol)](https://link.springer.com/article/10.1007/s10875-023-01591-8)
- [EurekAlert press release on Takagi/Kanegane RAD50 variant discovery](https://www.eurekalert.org/news-releases/1008134)
- [2026 ScienceDirect: "Expanding the mutational spectrum of RAD50: a case report... in a Chinese child"](https://www.sciencedirect.com/science/article/abs/pii/S037811192600051X)
- [2026 Frontiers in Endocrinology: "Novel RAD50 variants lead to NBS-like disorder and unplanned rhGH treatment response"](https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2026.1755251/full)
- [Redeker et al. 2025, "RAD50 missense variants differentially affect the DNA damage response and mitotic progression" (FEBS Letters), PMC12720227](https://pmc.ncbi.nlm.nih.gov/articles/PMC12720227/)
- [PeerJ 2020, "In silico analysis on the functional and structural impact of Rad50 mutations"](https://peerj.com/articles/9197/)
- [GeneCards: RAD50 Gene](https://www.genecards.org/cgi-bin/carddisp.pl?gene=RAD50)
- [RAD50, an SMC family member with multiple roles in DNA break repair (PMC4494100)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4494100/)
- [MRE11-RAD50-NBS1 keystone complex review, PMID:17713585](https://pubmed.ncbi.nlm.nih.gov/17713585/)
- [Ataxia-telangiectasia-like disorder MRE11A family, PMC6283458](https://ncbi.nlm.nih.gov/pmc/articles/PMC6283458)
- [Two unrelated patients with MRE11A mutations and NBS-like severe microcephaly, PubMed 21227757](https://pubmed.ncbi.nlm.nih.gov/21227757/)
- [OMIM #251260 - Nijmegen Breakage Syndrome](https://www.omim.org/entry/251260)
- [The Slavic NBN Founder Mutation: A Role for Reproductive Fitness?, PMC5148078](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5148078/)
- [Geographical Distribution, Incidence, Malignancies and Outcome of 136 Eastern Slavic NBS Patients, PMC7819964](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7819964/)
- [RAD50 and NBS1 are breast cancer susceptibility genes, PMC3006189](https://pmc.ncbi.nlm.nih.gov/articles/PMC3006189/)
- [Germline pathogenic variants in MRN genes and cancer predisposition, meta-analysis 2024, IJC](https://onlinelibrary.wiley.com/doi/full/10.1002/ijc.35066)
- [RAD50 zinc hook LoF variants and familial esophageal squamous cell carcinoma, PMC8472384](https://ncbi.nlm.nih.gov/pmc/articles/PMC8472384)
- [Cancer predisposition and hematopoietic failure in Rad50(S/S) mice, PMID:12208847](https://genesdev.cshlp.org/content/16/17/2237.long)
- [A rad50 germline mutation induces tumorigenesis and ataxia-telangiectasia phenotype in medaka, PMC10129005](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10129005/)
- [MGI Rad50 mouse gene detail (MGI:109292)](https://www.informatics.jax.org/marker/MGI:109292)