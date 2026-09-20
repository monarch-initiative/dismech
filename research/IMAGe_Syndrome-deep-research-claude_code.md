---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-27T01:50:38.760492'
end_time: '2026-08-27T01:54:33.132612'
duration_seconds: 234.37
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: IMAGe Syndrome
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
  num_turns: 15
  total_cost_usd: 0.9721700000000001
  session_id: a1f65bb8-1b49-516c-9197-25fb2b9c84dd
  stop_reason: end_turn
  assistant_text_blocks: 3
citation_count: 21
reference_validation:
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 18
  on_topic: 16
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** IMAGe Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **IMAGe Syndrome** covering all of the
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

I'll research IMAGe Syndrome using web search to gather current, well-cited information for this comprehensive report.

I now have comprehensive, well-cited data. Let me compile the full research report.

I have sufficient primary-source data now to produce the comprehensive report.

---

# IMAGe Syndrome: Comprehensive Research Report

## 1. Disease Information

**Overview.** IMAGe syndrome is a rare, multisystem, imprinted genetic disorder whose name is an acronym for its four cardinal features: **I**ntrauterine growth restriction, **M**etaphyseal dysplasia, **A**drenal hypoplasia congenita, and **Ge**nital anomalies (in males). It typically presents in the neonatal period with severe, potentially life-threatening primary adrenal insufficiency superimposed on prenatal-onset growth failure and skeletal dysplasia. First delineated clinically by Vilain et al. in 1999 (PMID: not indexed in this search; described in *J Clin Endocrinol Metab*), the molecular cause — heterozygous, maternally inherited, gain-of-function missense variants in **CDKN1C** — was identified in 2012 (Nature Genetics; PMID: cited below).

**Key identifiers:**
- **OMIM:** #614732 — *Intrauterine Growth Retardation, Metaphyseal Dysplasia, Adrenal Hypoplasia Congenita, and Genital Anomalies; IMAGE* ([omim.org/entry/614732](https://omim.org/entry/614732))
- **OMIM (allelic recessive form, POLE1-related):** #618336
- **MONDO:** MONDO:0013873 ([monarchinitiative.org/MONDO:0013873](https://monarchinitiative.org/MONDO:0013873))
- **Orphanet:** ORPHA:85173
- **GeneReviews:** Schrier Vergano SA, Deardorff MA. *IMAGe Syndrome*. NCBI Bookshelf NBK190103, updated 5 August 2021 ([ncbi.nlm.nih.gov/books/NBK190103](https://www.ncbi.nlm.nih.gov/books/NBK190103/))
- **Causal gene:** CDKN1C (HGNC:1785; OMIM *600856), chromosome 11p15.4 (within the imprinted 11p15.5 domain)
- **GTR:** C1846009

**Synonyms:** IMAGe association; Intrauterine Growth Retardation, Metaphyseal Dysplasia, Adrenal Hypoplasia Congenita, and Genital Anomalies syndrome.

**Data source note:** Nearly all published knowledge is derived from aggregated case reports/case series (individual-patient-level data pooled across publications) rather than large cohort or EHR-based studies, reflecting the disorder's extreme rarity — as of the 2021 GeneReviews update, only **31 affected individuals from 19 families** had been documented worldwide (22 of 31 male, reflecting ascertainment bias from visible genital anomalies) [GeneReviews NBK190103].

---

## 2. Etiology

**Primary cause — genetic, imprinted, gain-of-function.** IMAGe syndrome is caused by heterozygous missense pathogenic variants clustered in an 8-amino-acid region of CDKN1C's **PCNA-binding domain** (approximately residues 271/274–279), and the phenotype manifests **only when the variant is maternally inherited**, owing to genomic imprinting of CDKN1C (paternal allele normally silenced; only the maternal allele is expressed). Paternal transmission produces an unaffected carrier — de facto autosomal dominant inheritance restricted to the maternal line.

> "IMAGe syndrome is caused by gain-of-function pathogenic missense variants in the CDKN1C region encoding the PCNA-binding domain (amino acids 271-279) of the maternal allele, which cause loss of PCNA binding and pathogenic CDKN1C gain of function." — GeneReviews (NBK190103)

Known recurrent pathogenic variants include p.Ile272Ser (c.815T>G), p.Asp274Asn (c.820G>A), p.Phe276Val (c.826T>G), p.Arg279Pro (c.836G>C), p.Arg279Leu (c.836G>T), and p.Arg279Ser (c.835C>A) (PMC3787065, PMC4389716, Nature Genetics ng.2275).

**A distinct, allelic, recessive cause — POLE1/POLE.** A minority of IMAGe-like cases (sometimes termed "IMAGe syndrome with immunodeficiency," IMAGe-I; OMIM #618336) result from **biallelic hypomorphic variants in POLE1/POLE** (DNA polymerase epsilon catalytic subunit, chromosome 12q24), often a shared intronic splice-altering variant (c.1686+32C>G) in trans with a loss-of-function allele, causing cellular Pol ε deficiency and delayed S-phase progression (Logan et al., *AJHG* 2018, cell.com/ajhg S0002-9297(18)30400-2; Pachlopnik Schmid et al., PMC4630961). This recessive form adds **variable immunodeficiency** (lymphocyte deficiency), and sometimes craniosynostosis and cleft palate, to the classic tetrad.

**Risk factors:**
- *Genetic*: A maternal CDKN1C PCNA-binding-domain variant is both necessary and sufficient; there is no known variable penetrance modifier reported for the dominant CDKN1C form (adrenal insufficiency described as "fully penetrant" in maternally-inherited cases). For the recessive POLE1 form, biallelic inheritance (often via a common founder-like intronic variant) is required.
- *Environmental/other*: No environmental, infectious, lifestyle, or exposure-related risk factors have been reported — this is a purely monogenic/imprinting disorder with no described gene-environment interaction literature.

**Protective factors:** None identified in the literature; not applicable to this class of highly penetrant, single-gene, imprinted disorder.

---

## 3. Phenotypes

All data below are drawn from the GeneReviews cohort synthesis (31 individuals/19 families) and the founding clinical/molecular literature.

### Growth
- **Intrauterine growth restriction**: present in essentially all neonates; birth weights **−2 to −4 SD**. HP:0001511 (Intrauterine growth retardation)
- **Postnatal short stature**: continues after birth, height **−2.7 to −6.5 SD**. HP:0004322 (Short stature)
- Frequency: universal (100% of documented cases)
- Onset: prenatal; persists lifelong
- Course: generally stable/non-progressive after infancy, though some individuals are considered for growth hormone therapy

### Skeletal ("Metaphyseal dysplasia")
- **Metaphyseal and epiphyseal dysplasia** of long bones. HP:0003006 (Metaphyseal dysplasia) / HP:0010602 (Abnormality of epiphysis morphology)
- **Delayed bone age** — the most common radiologic finding
- **Scoliosis** (HP:0002650) and **osteoporosis** (HP:0000939) in a subset
- Frequency: skeletal abnormality in essentially all affected individuals, but radiologic evidence often not apparent until roughly age 5 years — subtle/absent in early infancy (age-dependent expressivity)
- Severity: variable, generally mild-to-moderate

### Adrenal (Adrenal hypoplasia congenita — most severe feature)
- Presents as **life-threatening primary adrenal insufficiency/adrenal crisis** in the first week to month of life: vomiting, feeding difficulty, dehydration, severe hypoglycemia, shock. HP:0000834 (Adrenocortical insufficiency) / HP:0000835 (Adrenal hypoplasia)
- Laboratory: hyponatremia, hyperkalemia, hypotension, and markedly elevated ACTH (often >1000 pg/mL vs. normal 10–60 pg/mL), producing marked hyperpigmentation (HP:0000953)
- Frequency: essentially universal/fully penetrant in maternally-inherited disease
- Onset: neonatal
- QoL impact: high — untreated adrenal crisis is fatal; lifelong glucocorticoid/mineralocorticoid dependence with need for stress dosing

### Genital (males only)
- **Bilateral cryptorchidism** (HP:0000028), **micropenis** (HP:0000054), **hypospadias**, **hypogonadotropic hypogonadism** (HP:0000044)
- Frequency: nearly universal in affected males; **absent in affected females** (a defining sex-limited feature)
- QoL impact: requires urologic surgery and, at puberty, testosterone replacement

### Craniofacial/dysmorphic
- Frontal bossing (HP:0002007), depressed/broad nasal bridge (HP:0000431), small and/or low-set ears (HP:0008551/HP:0000369), relative macrocephaly
- Generally mild, non-disfiguring

### Other reported features
- **Hypercalciuria/hypercalcemia**, occasionally with **nephrocalcinosis** or soft-tissue/hepatosplenic calcifications — reported in **8 of 16** assessed individuals (~50%); possibly secondary to sodium chloride supplementation used to treat mineralocorticoid deficiency (PMC4293665; GeneReviews)
- **Hypotonia** — reported in 6 of 31 documented individuals
- **Cognitive outcome**: normal in ~94% (15/16 assessed) — reassuring for long-term neurodevelopment in the classic CDKN1C form
- One reported case of **rhabdomyosarcoma** co-occurring with molecularly confirmed IMAGe syndrome (CDKN1C p.Asp274Asn) — the first such report, of unclear causal significance given p57KIP2's role as a tumor-suppressor/cell-cycle regulator (PMID: 34098225)
- POLE1-related (recessive) cases add: variable **immunodeficiency**/lymphopenia, occasionally craniosynostosis (HP:0004437) and cleft palate (HP:0000175)

---

## 4. Genetic/Molecular Information

**Causal gene:** CDKN1C (Cyclin-Dependent Kinase Inhibitor 1C, p57^KIP2^), HGNC:1785, OMIM *600856, chromosome 11p15.4, within the imprinted **KCNQ1/CDKN1C domain (ICR2)** of the 11p15.5 region that also harbors IGF2/H19 (ICR1). CDKN1C is maternally expressed (paternal allele silenced).

**Variant class:** Missense, gain-of-function, restricted to the PCNA-binding domain (residues ~271/274–279).

**Molecular mechanism:**
- p57^KIP2^ is "a tight-binding, strong inhibitor of several G1 cyclin/Cdk complexes" — specifically cyclin E–CDK2, cyclin D2–CDK4, and cyclin A–CDK2 (PMC3580416), acting as a negative regulator of the G1-to-S cell-cycle transition.
- Normally, phosphorylation of Thr310 by cyclin E/CDK2 creates a docking site for the F-box protein **Skp2**, targeting p57 for **SCF^Skp2^-mediated ubiquitination and proteasomal degradation** — this is the physiological "off-switch" that permits cell-cycle progression.
- IMAGe-associated PCNA-binding-domain mutations **disrupt PCNA binding**, which paradoxically and dramatically **increases CDKN1C protein stability**, preventing normal degradation.
- The resulting stabilized p57^KIP2^ protein is a more potent, longer-lived cell-cycle inhibitor, producing a **gain-of-function** phenotype: excessive suppression of cell proliferation/entry into S phase, manifesting clinically as growth restriction (PMID: 24098681, PMC3787065, PLOS ONE 2013; PMID: 25861374, PMC4389716).
- Functional validation: targeted expression of IMAGe-associated CDKN1C mutants in *Drosophila* eye caused severe growth defects compared with wild-type, and mutant protein decreased cell growth significantly more than wild-type or Beckwith-Wiedemann (loss-of-function) CDKN1C variants (Nature Genetics, ng.2275; PMID: 22609246 is the original 2012 discovery paper by Arboleda et al.).

**Allelic disorders (same gene, different variant class/location) — critical for interpretation:**
| Disorder | CDKN1C variant class | Effect | Phenotype |
|---|---|---|---|
| IMAGe syndrome | Missense, PCNA-binding domain (271–279), maternal | Gain of function (increased stability) | Growth restriction, adrenal hypoplasia, skeletal dysplasia |
| Beckwith-Wiedemann syndrome | Nonsense/truncating/missense outside PCNA domain, maternal | Loss of function | Overgrowth, macroglossia, omphalocele, tumor predisposition |
| Silver-Russell-like phenotype | p.Arg279Leu/Ser (PCNA domain) | Gain of function, milder | Growth restriction + SRS-like facial features, **without** adrenal insufficiency |
| IMAGe syndrome with immunodeficiency (IMAGe-I, OMIM #618336) | Biallelic POLE1 (different gene, 12q24) | Loss of Pol ε function | IMAGe features + immunodeficiency |

**Modifier genes:** None specifically established; phenotypic variability (e.g., partial BWS/IMAGe overlap phenotypes, or IMAGe plus developmental delay/microcephaly) has been reported for specific variants but no discrete modifier locus is characterized (PMC8788247).

**Epigenetics:** The disease mechanism is intrinsically epigenetic — normal CDKN1C expression is governed by genomic imprinting at the KvDMR1/ICR2 differentially methylated region in 11p15.5; IMAGe syndrome is a paradigm case of an imprinting-dependent Mendelian disorder rather than a classical imprinting-defect (methylation-loss) disorder — the defect here is a coding-sequence gain-of-function variant on the already-expressed maternal allele, not loss of imprinting per se.

**Population/allele frequency:** Given extreme rarity (single-digit families per variant), IMAGe-causing CDKN1C variants are essentially absent from population databases (gnomAD) — de novo maternal-germline or newly arising variants, or transmitted through unaffected carrier fathers, account for observed pedigrees.

**Chromosomal abnormalities:** Not a copy-number/structural disorder; no aneuploidy or large CNV mechanism described (distinguishing it from other 11p15.5 imprinting disorders like BWS/Silver-Russell syndrome that can also arise via uniparental disomy or ICR methylation defects).

**Suggested ontology terms:** HGNC:1785 (CDKN1C); GO:0007050 (cell cycle arrest); GO:0000079 (regulation of cyclin-dependent protein serine/threonine kinase activity); GO:0006511 (ubiquitin-dependent protein catabolic process).

---

## 5. Environmental Information

No environmental toxin, radiation, occupational, dietary, or lifestyle risk factor is described in the literature as contributing to IMAGe syndrome causation — consistent with its status as a fully penetrant, imprinted monogenic disorder. No infectious trigger is implicated. The only "environmental" element with disease-relevance is iatrogenic: chronic **sodium chloride (salt) supplementation**, used therapeutically for mineralocorticoid deficiency, is proposed as a contributor to the hypercalciuria/hypercalcemia seen in roughly half of assessed patients (GeneReviews NBK190103) — a treatment-related rather than causal environmental factor.

---

## 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream):**

1. **Molecular trigger**: Maternally inherited missense variant in the CDKN1C PCNA-binding domain (e.g., p.Arg279Pro, p.Phe276Val, p.Asp274Asn).
2. **Loss of PCNA interaction** → mutant p57^KIP2^ escapes the normal Skp2-SCF ubiquitin-proteasome degradation pathway (loss of Thr310-phosphorylation-dependent turnover) → **markedly increased protein half-life/stability**.
3. **Gain-of-function cell-cycle inhibition**: stabilized p57^KIP2^ exerts excess, prolonged inhibition of cyclin E–CDK2, cyclin D2–CDK4, and cyclin A–CDK2 complexes → impaired G1-to-S phase transition → **reduced cell proliferation** across affected tissues.
4. **Tissue-level consequences**:
   - Reduced proliferation of growth-plate chondrocytes and osteoblast precursors → metaphyseal/epiphyseal dysplasia, delayed bone age, short stature (skeletal/tissue-scale).
   - Impaired proliferation of adrenocortical progenitor cells during fetal adrenal cortex development → adrenal hypoplasia congenita → primary adrenal insufficiency (organ-scale endocrine failure).
   - Impaired growth of somatic tissues generally → intrauterine and postnatal growth restriction (organism-scale).
   - Disrupted genital tubercle/gonadal development in males (androgen-sensitive tissues appear particularly vulnerable) → cryptorchidism, micropenis, hypogonadotropic hypogonadism; the mechanism for the striking male-limited genital phenotype is not fully elucidated but is thought to reflect tissue-specific sensitivity to excess CDK-inhibitor dosage during a critical androgen-dependent developmental window.
5. **Downstream/secondary**: chronic glucocorticoid/mineralocorticoid replacement and salt supplementation → possible hypercalciuria/nephrocalcinosis (iatrogenic-mechanistic overlay).

**Cellular processes involved:** cell-cycle arrest/G1 checkpoint control (GO:0000082, G1/S transition of mitotic cell cycle), protein ubiquitination and proteasomal degradation (GO:0006511), negative regulation of cell proliferation (GO:0008285).

**Protein dysfunction class:** Not misfolding/aggregation — this is a **regulatory gain-of-function via impaired degradation** (increased protein stability/half-life), a distinct mechanistic category from the more common loss-of-function disease paradigm.

**Biochemical abnormality:** Failure of Skp2-SCF-mediated ubiquitination of p57^KIP2^ due to loss of the PCNA-docking interaction required for the normal Thr310-phosphorylation/degradation cascade.

**Model-system evidence for mechanism:**
- ***Drosophila* eye model**: transgenic expression of IMAGe-mutant CDKN1C caused significantly greater eye growth defects than wild-type CDKN1C, directly supporting a gain-of-function (not simple loss-of-function or dominant-negative) mechanism (Nature Genetics, ng.2275).
- **Cell-based (in vitro) assays**: IMAGe-mutant p57^KIP2^ shows increased protein half-life, impaired PCNA binding, and impaired S-phase entry compared to wild-type and to BWS-associated (loss-of-function) CDKN1C variants (PMID: 24098681; PMID: 25861374).
- ***Cdkn1c* mouse models** (relevant mechanistic/comparator system, though modeling the *loss-of-function*/BWS side of the allelic spectrum): *Cdkn1c*-null mice show ~20% fetal overgrowth followed by late-gestation growth reversal, placental labyrinth thrombotic lesions and disordered trophoblast architecture, and high perinatal lethality (<10% survival to adulthood) (PMID: 21729874). No published *Cdkn1c* PCNA-domain "knock-in" mouse fully recapitulating IMAGe (gain-of-function, growth-restricted) phenotype was identified in this search — this appears to be a genuine **model-system gap** (an IMAGe-specific knock-in mouse has not yet been reported), distinguishing it from the reciprocal BWS knock-in mouse (p57 Cdk-binding-domain knock-in reported by PMID: 27015986).
- **POLE1 mechanistic arm**: patient-derived cells with the recessive splice variant show cellular Pol ε deficiency and delayed S-phase progression, and novel POLE mutations cause aberrant nuclear subcellular localization and increased protein degradation (PMID: 35534205) — a mechanistically distinct but convergent route to impaired DNA replication/growth.

Suggested GO terms: GO:0000082 (G1/S transition of mitotic cell cycle), GO:0045930 (negative regulation of mitotic cell cycle), GO:0031145 (anaphase-promoting complex-dependent catabolic process, related SCF/ubiquitin pathway), GO:0006974 (DNA damage response, for the POLE1 arm).

---

## 7. Anatomical Structures Affected

**Organ level:**
- Primary: adrenal cortex (adrenal hypoplasia), skeletal system (long bone metaphyses/epiphyses), external/internal male genitalia and gonads
- Secondary: kidney (nephrocalcinosis, secondary to hypercalciuria), spine (scoliosis), skull/face (frontal bossing, craniofacial dysmorphism)
- Body systems: endocrine (adrenal, gonadal), skeletal, genitourinary; occasionally immune system (POLE1 subtype)

**Tissue/cell level:**
- Adrenal cortex fetal zone/definitive zone progenitor cells (steroidogenic cells)
- Growth-plate chondrocytes and metaphyseal osteoblasts
- Testicular/genital tubercle mesenchyme
- Suggested UBERON terms: UBERON:0001235 (adrenal cortex), UBERON:0002513 (endochondral bone), UBERON:0000019 (camera-type eye — not relevant here, omit), UBERON:0000992 (gonad), UBERON:0000151 (long bone metaphysis — check UBERON:0003535 metaphysis)
- Suggested CL terms: CL:0002095 (adrenal cortex cell), CL:0000058 (chondrocyte)

**Subcellular level:**
- Nucleus (site of p57^KIP2^-cyclin/CDK complex activity and cell-cycle control); GO Cellular Component: GO:0005634 (nucleus), GO:0000307 (cyclin-dependent protein kinase holoenzyme complex)
- Ubiquitin-proteasome system components (cytoplasmic and nuclear)

**Localization:** Bilateral/symmetric adrenal hypoplasia; bilateral cryptorchidism; skeletal changes are typically symmetric/bilateral in the metaphyses of long bones.

---

## 8. Temporal Development

- **Onset:** Congenital/prenatal for growth restriction and skeletal dysplasia (detectable in utero via growth restriction); neonatal onset (first week to month of life) for adrenal crisis — often the presenting, life-threatening event.
- **Onset pattern:** Acute for adrenal crisis; chronic/static for growth and skeletal features.
- **Progression:** Skeletal radiologic findings are age-dependent — often subtle or absent in early infancy, becoming apparent by approximately **age 5 years**. Growth restriction is largely established prenatally/in infancy and remains stable (not classically progressive) thereafter, though final height varies (−2.7 to −6.5 SD).
- **Disease course:** Chronic, lifelong (adrenal insufficiency requires permanent glucocorticoid/mineralocorticoid replacement); not typically relapsing-remitting.
- **Longest follow-up reported:** oldest documented affected individual was 26 years old, with normal cognitive development (GeneReviews NBK190103).
- **Critical period:** The neonatal period is the critical window of vulnerability for undiagnosed/untreated adrenal crisis — early recognition and glucocorticoid/mineralocorticoid initiation is the single most important time-sensitive intervention.
- **Reproduction:** Two affected females have successfully reproduced; no affected males are known to have reproduced (consistent with hypogonadotropic hypogonadism/genital anomalies in males) (GeneReviews NBK190103).

---

## 9. Inheritance and Population

**Epidemiology:**
- **Prevalence:** Orphanet classifies IMAGe syndrome as affecting fewer than 1 in 1,000,000 individuals (ultra-rare). As of the 2021 GeneReviews update, only **31 affected individuals from 19 families** had been documented worldwide — true prevalence is unknown and likely undercounted owing to underrecognition/misdiagnosis (e.g., as congenital adrenal hyperplasia or isolated adrenal hypoplasia).
- **Incidence:** Not established; too rare for population-based incidence estimates.

**Inheritance pattern:** Autosomal dominant with a strict **imprinting/parent-of-origin effect** — pathogenic only when maternally transmitted (CDKN1C form). The POLE1-related form is **autosomal recessive** (biallelic).

**Penetrance:** Adrenal insufficiency appears **fully penetrant** in maternally-inherited CDKN1C pathogenic variant carriers.

**Expressivity:** Variable — e.g., skeletal findings are age-dependent and can be subtle; some CDKN1C PCNA-domain variants (p.Arg279Leu/Ser) produce a milder Silver-Russell-like phenotype without adrenal insufficiency, indicating variant-specific expressivity along a phenotypic spectrum (PMID: 28508599, "IMAGe and Related Undergrowth Syndromes: The Complex Spectrum of Gain-of-Function CDKN1C Mutations").

**Genetic anticipation:** Not reported/applicable (not a repeat-expansion disorder).

**Germline mosaicism:** Possible — GeneReviews notes that when the mother does not carry the variant in blood, sibling recurrence risk is <1%, reflecting the possibility of maternal germline mosaicism rather than zero risk.

**Founder effects:** The recessive POLE1 form is notable for multiple unrelated families sharing the same intronic splice variant (c.1686+32C>G) as part of a common haplotype — suggestive of a founder allele, though geographic/ethnic clustering was not detailed in the sources reviewed here.

**Consanguinity:** Relevant to the recessive POLE1 form (biallelic inheritance), though not specifically highlighted as a risk factor in the sources found; not applicable to the dominant/imprinted CDKN1C form.

**Carrier frequency:** Not established in population databases given extreme rarity.

**Population demographics:**
- **Sex ratio:** 22 of 31 documented cases male — attributed to ascertainment bias (genital anomalies in males are more clinically apparent and prompt diagnostic workup), not necessarily a true sex-linked susceptibility difference for adrenal/growth features (both sexes affected equally by the core adrenal/growth/skeletal features; genital anomalies affect only males).
- **Geographic distribution:** No endemic region reported; described in geographically diverse case reports/families (implying panethnic occurrence, though systematic geographic epidemiology has not been performed given rarity).
- **Age distribution:** Predominantly diagnosed in infancy/early childhood; oldest reported case 26 years.

---

## 10. Diagnostics

**No formal consensus clinical diagnostic criteria exist**; diagnosis rests on the combination of suggestive clinical/radiologic findings plus molecular confirmation.

**Laboratory tests:**
- Serum electrolytes (hyponatremia, hyperkalemia during adrenal crisis)
- Plasma ACTH (markedly elevated, often >1000 pg/mL; normal 10–60 pg/mL)
- Cortisol (low/inappropriately low for degree of stress)
- Renin/aldosterone (assessing mineralocorticoid axis)
- Serum and urine calcium (hypercalcemia/hypercalciuria surveillance)
- Suggested LOINC terms: cortisol serum panels, ACTH plasma panels (specific LOINC codes not resolved in this search — recommend direct LOINC lookup during curation)

**Imaging:**
- Skeletal radiographs: metaphyseal/epiphyseal dysplasia, bone-age assessment (delayed)
- Renal ultrasound: nephrocalcinosis surveillance
- Adrenal imaging (ultrasound/CT/MRI showing small/hypoplastic adrenal glands) — though imaging can be normal early, and the diagnosis is primarily biochemical/genetic

**Genetic testing (primary diagnostic modality):**
- **Single-gene sequence analysis of CDKN1C** — GeneReviews reports 11/11 families with a clinically diagnosed phenotype had a pathogenic variant identified this way; targeted testing of the PCNA-binding-domain "hot spot" region is efficient given the tight mutational clustering
- Multigene panels for growth restriction/adrenal hypoplasia differential (including CDKN1C, NR0B1, POLE1, SAMD9)
- Exome/genome sequencing when the phenotype is atypical or overlaps other growth/adrenal disorders
- Parent-of-origin (imprinting) testing/methylation studies may be relevant to confirm maternal transmission where pedigree information is ambiguous

**Clinical criteria/differential diagnosis:**

| Condition | Gene | Distinguishing features |
|---|---|---|
| **Congenital adrenal hyperplasia (CAH)** | CYP21A2, others | Hyperplastic (not hypoplastic) adrenals; female virilization; rarely IUGR |
| **X-linked adrenal hypoplasia congenita** | NR0B1 (DAX1) | X-linked; no growth restriction, metaphyseal dysplasia, or characteristic facial features |
| **MIRAGE syndrome** | SAMD9 | Myelodysplasia, recurrent/invasive infections, enteropathy; often fatal in first decade; metaphyseal dysplasia, macrocephaly, and hypercalciuria are NOT typical of MIRAGE (helps distinguish from IMAGe) |
| **Silver-Russell syndrome** | 11p15 (H19/IGF2 hypomethylation, mUPD7), or CDKN1C p.Arg279Leu/Ser | 5th-finger clinodactyly, limb asymmetry, café-au-lait macules; normal growth velocity; CDKN1C-related SRS-like cases lack adrenal insufficiency |
| **3-M syndrome** | CUL7, OBSL1, CCDC8 | Autosomal recessive; dolichocephaly, prominent heels, full eyebrows, downturned mouth |
| **IMAGe with immunodeficiency (IMAGe-I)** | POLE1 (biallelic) | Recessive; adds variable immunodeficiency, sometimes craniosynostosis/cleft palate |

**Screening:** No population newborn-screening program exists (too rare, and adrenal insufficiency is not part of standard newborn screening panels such as 17-OHP-based CAH screening). Cascade/prenatal testing is offered in known-affected families once the pathogenic variant is identified (see Genetic Counseling above).

---

## 11. Outcome/Prognosis

- **Survival/mortality:** With prompt recognition and glucocorticoid/mineralocorticoid replacement, adrenal crisis is treatable and long-term survival into adulthood is achieved (oldest reported case: 26 years). Untreated/unrecognized adrenal crisis in the neonatal period is **life-threatening** and represents the principal acute mortality risk.
- **Morbidity:** Lifelong dependence on steroid replacement with attendant risks (adrenal crisis during intercurrent illness if stress-dosing is inadequate); skeletal complications (scoliosis, osteoporosis); renal complications (nephrocalcinosis) in a subset; urogenital surgical needs in males.
- **Cognitive/functional outcome:** Generally favorable — normal cognitive development reported in ~94% of assessed individuals (15/16), a notably reassuring prognostic feature relative to many other congenital syndromes.
- **Reproductive outcome:** Two affected females have reproduced; no affected males have reproduced, consistent with male hypogonadism.
- **Neoplasia risk:** Not established as an elevated cancer-predisposition syndrome analogous to the tumor-suppressor loss-of-function paradigm in Beckwith-Wiedemann syndrome (where CDKN1C loss-of-function contributes to embryonal tumor risk, e.g., Wilms tumor). However, a single case report of co-occurring rhabdomyosarcoma (PMID: 34098225) raises an open question about possible tumor association that has not been systematically studied given the tiny total case count — this should be flagged as a knowledge gap rather than an established risk.
- **Prognostic factors:** Timeliness of adrenal insufficiency diagnosis/treatment is the dominant modifiable prognostic factor; specific missense variant may influence phenotypic severity/spectrum (e.g., p.Arg279Leu/Ser giving a milder, non-adrenal Silver-Russell-like presentation).

---

## 12. Treatment

**Pharmacotherapy (mainstay):**
- **Acute adrenal crisis:** IV isotonic saline, IV dextrose/glucose, and IV hydrocortisone (stress-dose glucocorticoid), with close monitoring of blood pressure, hydration status, and electrolytes; NCIT term: NCIT:C15986 (Pharmacotherapy), NCIT:C2924 (Corticosteroid, or specific NCIT:C328 Hydrocortisone)
- **Chronic maintenance:** Physiologic glucocorticoid replacement (hydrocortisone) plus mineralocorticoid replacement (fludrocortisone) when needed; oral sodium chloride supplementation for salt-wasting
- **Stress dosing protocols:** Increased glucocorticoid dose during illness, surgery, or trauma; MedicAlert bracelet strongly recommended for emergency recognition
- **Growth hormone therapy:** Considered in selected cases with evidence of growth hormone deficiency/insufficient growth response
- **Testosterone replacement:** For males with hypogonadotropic hypogonadism at expected puberty

**Surgical/interventional:**
- Urologic surgery for cryptorchidism and hypospadias (NCIT:C15329, Surgical Procedure)
- Orthopedic intervention for scoliosis or hip dysplasia as clinically indicated

**Supportive/rehabilitative:**
- Occupational, speech, and physical therapy for hypotonia and any developmental delay (NCIT:C15302, Physical Therapy)

**Experimental/targeted therapy:** No gene therapy, RNA-based therapy, or molecularly targeted therapy specific to CDKN1C stabilization has been reported for IMAGe syndrome in the literature surveyed — management remains supportive/replacement-based rather than mechanism-correcting. No disease-specific registered clinical trials (ClinicalTrials.gov) were identified, consistent with the disorder's ultra-rare status.

**Surveillance protocol (per GeneReviews):**
- Growth measurement at every visit
- Annual endocrine evaluation of adrenal function; monitoring for hypercalciuria/nephrocalcinosis
- Orthopedic evaluation as needed
- Neurodevelopmental assessment at each visit

**Treatment outcomes:** Well-managed replacement therapy allows normal growth trajectories to be partially supported and prevents crisis-related mortality; no systematic response-rate or adverse-event data exist beyond general glucocorticoid/mineralocorticoid replacement pharmacology (well characterized in adrenal insufficiency literature generally, not disease-specific).

---

## 13. Prevention

- **Primary prevention:** Not applicable in the classic sense (this is a highly penetrant monogenic disorder) — the closest analog is **reproductive/genetic counseling** for at-risk families to inform reproductive decisions.
- **Secondary prevention:** Early recognition and prompt glucocorticoid/mineralocorticoid initiation in a neonate with IUGR plus biochemical signs of adrenal insufficiency prevents crisis-related morbidity/mortality — this is the single most impactful "preventive" intervention described.
- **Genetic counseling:**
  | Scenario | Recurrence risk |
  |---|---|
  | Child of affected/carrier mother | 50% |
  | Child of affected/carrier father | 50% chance of inheriting variant, but expected unaffected (imprinting) |
  | Sibling, mother confirmed carrier | 50% |
  | Sibling, mother tested negative | <1% (germline mosaicism possibility) |
  - Prenatal testing and preimplantation genetic testing (PGT) are available once the familial pathogenic variant is known, offered as a personal reproductive decision (GeneReviews NBK190103).
- **Screening:** No population-level newborn screening exists; targeted cascade testing is the applicable "screening" modality in known families.
- **Prophylaxis:** Stress-dose glucocorticoid protocols function as prophylaxis against adrenal crisis during physiologic stress in already-diagnosed patients.

---

## 14. Other Species / Natural Disease

- No naturally occurring IMAGe syndrome has been reported in non-human species (companion animals, livestock, or wildlife); no OMIA (Online Mendelian Inheritance in Animals) entry was identified in this search.
- CDKN1C (p57^KIP2^) is evolutionarily conserved across mammals, and mouse Cdkn1c is the basis of the principal animal-model literature (see Section 15), but this reflects engineered laboratory models, not natural veterinary disease.
- No zoonotic or cross-species transmission relevance (monogenic, non-infectious disorder).

---

## 15. Model Organisms

**Mouse (*Mus musculus*):**
- ***Cdkn1c*-null mice**: Model the reciprocal, **loss-of-function/BWS side** of the allelic spectrum rather than IMAGe itself. Show ~20% fetal overgrowth followed by a late-gestation reversal, placental labyrinth thrombotic lesions, disordered trophoblast/sinusoidal giant-cell architecture, and high perinatal lethality (<10% survival to adulthood) (PMID: 21729874, *Dis Model Mech* 2011).
- **p57^Kip2^ Cdk-binding-domain knock-in mice**: Used to dissect CDK-dependent versus CDK-independent p57 functions relevant to BWS pathogenesis (PMID: 27015986).
- **Gap identified**: No CDKN1C PCNA-binding-domain (IMAGe-specific gain-of-function) knock-in mouse model was found in this search — an IMAGe-mimicking growth-restricted mouse model appears not yet reported in the literature surveyed, representing a HUMAN_MODEL_MISMATCH-relevant gap: existing *Cdkn1c* mouse literature informs the opposite (loss-of-function/overgrowth) end of the phenotypic spectrum, and its translational relevance to the IMAGe gain-of-function mechanism should be treated cautiously if cited as supporting evidence for IMAGe-specific pathophysiology.

**Drosophila melanogaster:**
- Transgenic eye-specific expression of IMAGe-mutant human CDKN1C (versus wild-type) produced significantly more severe eye growth defects, providing direct in vivo functional evidence for the gain-of-function mechanism outside a mammalian system (Nature Genetics, ng.2275, Arboleda et al. 2012).

**Cell-based/in vitro systems:**
- Patient-derived and transfected mammalian cell lines used to measure p57^KIP2^ protein half-life, PCNA-binding, ubiquitination, and S-phase entry — the principal direct evidence base for the stabilization/gain-of-function mechanism (PMID: 24098681; PMID: 25861374).
- POLE1-mutant patient fibroblasts: used to demonstrate delayed S-phase progression and aberrant nuclear localization/degradation of mutant Pol ε protein (PMID: 35534205).

**Model limitations:** The existing mouse literature captures BWS (loss-of-function) biology well but has not yet produced a validated IMAGe (gain-of-function) in vivo mammalian model; *Drosophila* and cell-based systems, while mechanistically informative, cannot recapitulate the tissue-specific human phenotypes (adrenal hypoplasia, male-specific genital anomalies) — this is an appropriate candidate for a `HUMAN_MODEL_MISMATCH`-style knowledge-gap annotation if curated into a mechanism-graph knowledge base, since the available fly/cell evidence supports the general gain-of-function/proliferation-inhibition mechanism but not the organ-specific developmental phenotypes.

---

## Summary Table: Suggested Ontology Term Bindings for Curation

| Concept | Suggested term |
|---|---|
| Disease | MONDO:0013873 (IMAGe syndrome); OMIM:614732 |
| Causal gene | hgnc:1785 (CDKN1C) |
| Recessive allelic form gene | POLE1/POLE (chr 12q24) |
| Intrauterine growth restriction | HP:0001511 |
| Short stature | HP:0004322 |
| Metaphyseal dysplasia | HP:0003006 |
| Adrenal hypoplasia | HP:0000835 |
| Adrenocortical insufficiency | HP:0000834 |
| Hyperpigmentation of the skin | HP:0000953 |
| Cryptorchidism | HP:0000028 |
| Micropenis | HP:0000054 |
| Hypogonadotropic hypogonadism | HP:0000044 |
| Frontal bossing | HP:0002007 |
| Scoliosis | HP:0002650 |
| Hypercalciuria | HP:0002150 |
| Nephrocalcinosis | HP:0000121 |
| Hypotonia | HP:0001252 |
| Cell-cycle/mechanism | GO:0000082 (G1/S transition), GO:0006511 (ubiquitin-dependent protein catabolic process) |
| Adrenal cortex | UBERON:0001235 |
| Adrenal cortex cell | CL:0002095 |
| Treatment: Pharmacotherapy | NCIT:C15986 |
| Treatment: Surgical procedure | NCIT:C15329 |
| Treatment: Physical therapy | NCIT:C15302 |

---

## Sources

- [GeneReviews: IMAGe Syndrome (NBK190103)](https://www.ncbi.nlm.nih.gov/books/NBK190103/) — Schrier Vergano SA, Deardorff MA, updated 2021
- [OMIM #614732](https://omim.org/entry/614732)
- [OMIM #618336 (POLE1/IMAGe-I)](https://www.omim.org/entry/618336)
- [MONDO:0013873](https://monarchinitiative.org/MONDO:0013873)
- [Increased Protein Stability of CDKN1C Causes a Gain-of-Function Phenotype in Patients with IMAGe Syndrome, PLOS ONE (PMID 24098681)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3787065/)
- [Mutations in the PCNA-binding domain of CDKN1C cause IMAGe syndrome, Nature Genetics](https://www.nature.com/articles/ng.2275)
- [Mutations in the PCNA-binding site of CDKN1C inhibit cell proliferation by impairing entry into S phase (PMID 25861374)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4389716/)
- [IMAGe and Related Undergrowth Syndromes: The Complex Spectrum of Gain-of-Function CDKN1C Mutations (PMID 28508599)](https://pubmed.ncbi.nlm.nih.gov/28508599/)
- [DNA Polymerase Epsilon Deficiency Causes IMAGe Syndrome with Variable Immunodeficiency, AJHG](https://www.cell.com/ajhg/fulltext/S0002-9297(18)30400-2)
- [Novel POLE mutations identified in patients with IMAGE-I syndrome (PMID 35534205)](https://pubmed.ncbi.nlm.nih.gov/35534205/)
- [A patient with polymerase E1 deficiency (POLE1) (PMC4630961)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4630961/)
- [A case of an infant suspected as IMAGE syndrome finally diagnosed with MIRAGE syndrome (PMID 29506479)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5836387/)
- [A Case report: Co-occurrence of IMAGe syndrome and Rhabdomyosarcoma (PMID 34098225)](https://pubmed.ncbi.nlm.nih.gov/34098225/)
- [Is Hyperpigmentation on the First Day of Life Always Associated with IMAGe Syndrome? (PMC4293665)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4293665/)
- [Fetal overgrowth in the Cdkn1c mouse model of Beckwith-Wiedemann syndrome (PMID 21729874)](https://pubmed.ncbi.nlm.nih.gov/21729874/)
- [p57(Kip2) knock-in mouse reveals CDK-independent contribution in the development of BWS (PMID 27015986)](https://pubmed.ncbi.nlm.nih.gov/27015986/)
- [An imprinted IMAGe: insights into growth regulation through genomic analysis of a rare disease (PMC3580416)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3580416/)
- [Functional Versatility of the CDK Inhibitor p57Kip2 (PMC7575724)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7575724/)
- [Deep exploration of a CDKN1C mutation causing a mixture of BWS and IMAGe syndromes (PMC8788247)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8788247/)
- [An Intronic Variant in CDKN1C Gene Causing IMAGe Syndrome in an Iranian Girl (PMC12604900)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12604900/)
- [MedlinePlus Genetics: IMAGe syndrome](https://medlineplus.gov/genetics/condition/image-syndrome/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 18 |
| On topic | 16 |
| Off topic | 0 |

All extracted references resolved successfully.