---
provider: claude_code
model: claude-fable-5, claude-haiku-4-5-20251001, claude-opus-5
cached: false
start_time: '2026-08-25T18:45:29.101497'
end_time: '2026-08-25T18:54:40.635934'
duration_seconds: 551.53
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Spastic Paraplegia 90A, Autosomal Dominant
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
  - claude-fable-5
  - claude-haiku-4-5-20251001
  - claude-opus-5
  web_search_requests: 18
  num_turns: 40
  total_cost_usd: 4.168262500000001
  session_id: 3f4f734d-821f-47c0-928c-79684f7d6cb1
  stop_reason: end_turn
  assistant_text_blocks: 6
citation_count: 37
reference_validation:
  total_references: 23
  verified: 23
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 18
  quotes_valid: 12
  quotes_unsupported: 6
  unsupported_quote_references:
  - PMID:36718090
  - PMC:PMC11271397
  relevance_assessed: 23
  on_topic: 7
  off_topic: 1
  off_topic_references:
  - DOI:10.1073/pnas.1516733112
  needs_review: true
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spastic Paraplegia 90A, Autosomal Dominant
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spastic Paraplegia 90A, Autosomal Dominant** covering all of the
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

I'll research Spastic Paraplegia 90A (SPG90A). This repo already has a draft KB entry and cached references for it, so I'll read those local resources first, then supplement with web searches.

I have the local KB draft and one cached reference. Let me read the remaining cached references and search for additional sources in parallel.

Now let me search for additional authoritative sources to fill the gaps.

Let me fetch the primary sources in detail.

Let me verify a few citation identifiers before writing up.

I have enough to write the report. Here it is.

---

# Research Report: Spastic Paraplegia 90A, Autosomal Dominant (SPG90A)

**Prepared:** 2026-08-25 · **MONDO:0957308** · **OMIM #620416** · Gene: **SPTSSA**

**Bottom line up front:** SPG90A is an ultra-rare, de novo–dominant, early-childhood-onset *complicated* hereditary spastic paraplegia caused by activating missense variants in *SPTSSA*, the small activating subunit of serine palmitoyltransferase. The entire published autosomal-dominant cohort is **three patients, all carrying the same recurrent p.Thr51Ile allele**. The mechanism is unusually well characterized for a disease this rare: the variant breaks ORMDL-mediated feedback inhibition of SPT, producing unrestrained de novo sphingolipid synthesis — a *gain* of pathway activity, not an enzyme deficiency. The single most actionable clinical fact is a **therapeutic contraindication**: L-serine supplementation, the standard-of-care rationale for the related HSAN1 disorders, is expected to worsen SPG90A.

---

## 1. Disease Information

### Overview

Spastic paraplegia 90A is a monogenic neurodevelopmental-and-neurodegenerative disorder in which progressive lower-limb spasticity from upper motor neuron dysfunction is superimposed on global developmental delay. It sits in the *complicated* (complex) tier of the hereditary spastic paraplegias — features extend well beyond the corticospinal tract, including intellectual disability, sensorineural hearing loss, epileptiform EEG changes, dysmorphic/cutaneous findings, and growth failure.

The disease was defined in 2023 by Srivastava and colleagues in *Brain*, working through the Undiagnosed Diseases Network:

> "Exome sequencing identified potential disease-causing variants in *SPTSSA* in three children presenting with a complex form of hereditary spastic paraplegia." — [PMID:36718090](https://pubmed.ncbi.nlm.nih.gov/36718090/)

**Important nosological point.** SPG90 splits into two OMIM concepts by zygosity, and only the dominant pole is SPG90A:

| Concept | OMIM | Zygosity | Variant(s) reported |
|---|---|---|---|
| **SPG90A** (this entry) | #620416 | Monoallelic / heterozygous | p.Thr51Ile (c.152C>T) |
| SPG90B | #620417 | Biallelic / homozygous | c.171_172del, p.Gln58AlafsTer10 |

Of the three children in the founding *Brain* paper, **Patients 1 and 2 are SPG90A** (both heterozygous de novo p.Thr51Ile) and **Patient 3 is SPG90B** (homozygous frameshift). The fourth published SPG90 patient ([PMID:40533086](https://pubmed.ncbi.nlm.nih.gov/40533086/), Duzenli et al., *Clin Genet* 2026) is heterozygous p.Thr51Ile and therefore **SPG90A**. Total published SPG90A cases: **three**.

### Key identifiers

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0957308 — *spastic paraplegia 90A, autosomal dominant* |
| OMIM (disease) | #620416 |
| OMIM (gene) | *613540 (*SPTSSA*) |
| MedGen | C5830574 (CUI 1841210) |
| HGNC | hgnc:20361 (*SPTSSA*) |
| Ensembl | ENSG00000165389 |
| UniProt | Q969W0 (SPTSSA_HUMAN) |
| Cytoband | 14q13.1 |
| MGI (mouse ortholog) | MGI:1913399 (*Sptssa*) |

**Not found / not applicable:** No dedicated Orphanet code exists for SPG90A. The nearest Orphanet concept is the group term **ORPHA:102013 "Complex hereditary spastic paraplegia"**, which is explicitly a category rather than a disease. ICD-10 **G11.4** (hereditary spastic paraplegia) and ICD-11 **8A41** apply only at the class level — neither codes SPG90A specifically, and I could not verify a SPG90A-specific code in either system. No MeSH descriptor exists below "Spastic Paraplegia, Hereditary" (D015419).

### Synonyms

- SPG90A
- Spastic paraplegia 90, autosomal dominant
- *SPTSSA*-related complex/complicated hereditary spastic paraplegia
- *SPTSSA*-related cHSP (the usage preferred in the mechanistic literature)

### Data provenance

All disease-level knowledge derives from **individual published case reports and their functional workups** — three patients across two papers. There is no registry, no EHR-derived cohort, no natural-history study, and no aggregated disease-level resource with independent content. Every aggregator entry (MalaCards, MedGen, GeneCards, HPO annotations) traces back to PMID:36718090. Curators should treat these aggregators as *redistributions of a single n=2 source*, not as independent corroboration.

---

## 2. Etiology

### Primary causal factor

A **heterozygous activating missense variant in *SPTSSA***, arising **de novo** in both index patients. There is no environmental, infectious, or multifactorial component. This is a fully penetrant Mendelian dominant disorder with a single reported allele.

### Mechanistic causal factor

The variant does not damage the catalytic machinery — *SPTSSA* has no catalytic centre. It disables the **regulatory brake**:

> "The variants in *SPTSSA* impaired the negative regulation of serine palmitoyltransferase by ORMDLs leading to excessive sphingolipid synthesis based on biochemical studies and *in vivo* studies in *Drosophila*." — [PMID:36718090](https://pubmed.ncbi.nlm.nih.gov/36718090/)

> "Similar to juvenile ALS variants, *SPTSSA* variants seem to interfere with ORMDL regulation of the SPT complex, thus resulting in unrestrained SPT activity." — Mohassel et al. 2024, [PMID:38788085](https://pubmed.ncbi.nlm.nih.gov/38788085/)

### Genetic risk factors

- **Causal variant:** *SPTSSA* c.152C>T, p.Thr51Ile (NM_138288.4), heterozygous, de novo.
- **Susceptibility loci / modifier genes:** None identified. No GWAS, no PheGenI signal, no polygenic contribution described. With n=3, no modifier analysis is possible.
- **Candidate modifier hypothesis (not established):** *ORMDL1/2/3* expression levels are a mechanistically plausible modifier class, since the disease *is* a failure of ORMDL restraint, and ORMDL3 dosage is itself a well-known asthma locus. **No data support this in SPG90A** — flagging it as a hypothesis worth a knowledge-gap discussion, not a curatable claim.

### Environmental risk factors

**None known.** No toxin, occupational exposure, infection, or lifestyle factor has been implicated. Age, sex, and family history are non-contributory: both index cases were de novo, and the two SPG90A patients from the *Brain* paper plus the Turkish patient are all female — a sex distribution with no statistical meaning at n=3.

### Protective factors

**None known** — with one important inversion. There is a documented **anti-protective dietary factor**: L-serine, which is *therapeutic* in the sibling disorder HSAN1, is expected to be harmful here (see §12).

### Gene–environment interactions

One substantiated interaction, and it is a therapeutic one rather than an etiologic one — **substrate availability modulates the biochemical lesion**:

> "Elevated serine exacerbates the overproduction of SLs associated with the *SPTLC1* juvenile ALS variants and the *SPTSSA* variants described here... Thus serine supplementation is not a rational therapeutic strategy and may even be detrimental for these patients." — [PMID:36718090](https://pmc.ncbi.nlm.nih.gov/articles/PMC10319774/)

L-serine is the amino-acid substrate SPT condenses with palmitoyl-CoA. Because the enzyme is de-restrained, increasing substrate supply increases flux through an already-runaway pathway. This is a genuine gene–diet interaction with direct management implications.

---

## 3. Phenotypes

### Source and frequency caveat

HPO annotations for OMIM:620416 derive **entirely from PMID:36718090** and are scored over **two patients** (denominators of "2/2", "1/2", "1/1" in the table below). Frequencies are therefore *illustrative of which features were present in the index pair*, not population estimates. The fourth patient (PMID:40533086) is not yet folded into HPO annotations.

### Curated HPO phenotype table

| HPO ID | Phenotype | Frequency (source cohort) | Notes |
|---|---|---|---|
| HP:0003593 | Infantile onset | 2/2 | Onset in infancy, before the spasticity is apparent |
| HP:0034353 | Appendicular spasticity | 2/2 | The defining motor sign |
| HP:0008936 | Axial hypotonia | 2/2 | Coexists with limb spasticity |
| HP:0031936 | Delayed ability to walk | 2/2 | |
| HP:0001249 | Intellectual disability | 2/2 | |
| HP:0004322 | Short stature | 2/2 | Under-appreciated non-neurological feature |
| HP:0001052 | Nevus flammeus (port-wine stain) | 2/2 | **Unexplained**; see below |
| HP:0002064 | Spastic gait | 1/1 | Only assessable in the ambulatory patient |
| HP:0000750 | Delayed speech and language development | 1/1 | |
| HP:0002650 | Scoliosis | 1/1 | |
| HP:0000407 | Sensorineural hearing impairment | 1/2 | Variable across the wider SPG90 cohort |
| HP:0001332 | Dystonia | 1/2 | Also present in the 4th patient |
| HP:0001344 | Absent speech | 1/2 | Severe end of the language spectrum |
| HP:0002144 | Tethered cord | 1/2 | Structural; a confounder for the spasticity |
| HP:0002360 | Sleep disturbance | 1/2 | |
| HP:0001508 | Failure to thrive | 1/2 | |
| HP:0002015 | Dysphagia | 1/2 | |
| HP:0002020 | Gastroesophageal reflux | 1/2 | |
| HP:0002307 | Drooling | 1/2 | |
| HP:0000256 | Macrocephaly | 1/2 | |
| HP:0001250 | Seizure | **0/2** | See EEG note — SPG90A patients had epileptiform EEG *without* clinical seizures |

**Additional phenotypes from the fourth patient** ([PMID:40533086](https://pubmed.ncbi.nlm.nih.gov/40533086/)), each n=1 and therefore provisional:

| HPO ID | Phenotype | Status |
|---|---|---|
| HP:0002540 | Inability to walk | Documented at age 10 |
| HP:0001263 | Global developmental delay | Documented |
| HP:0000011 | Neurogenic bladder | **Proposed, not established** |
| HP:0004918 (or HP:0008341) | Distal renal tubular acidosis | Proposed |
| HP:0000787 | Nephrolithiasis | Proposed |
| HP:0000010 | Recurrent urinary tract infections | Proposed |
| HP:0001959 | Polydipsia (primary) | **Proposed, not established** |

The authors are explicit that the genitourinary cluster is a hypothesis:

> "The neurogenic bladder and primary polydipsia found in our patient are novel findings, and we propose that genitourinary problems may be a component of the syndrome." — [PMID:40533086](https://pubmed.ncbi.nlm.nih.gov/40533086/)

### Three phenotype findings worth curator attention

**1. Nevus flammeus (port-wine stain) at 2/2 is a striking and unexplained association.** Both SPG90A index patients had a capillary malformation — present at birth in Patient 1, apparent in infancy in Patient 2. At 100% of the dominant cohort this is as frequent as the spasticity itself. No mechanism has been proposed linking sphingolipid overproduction to capillary malformation, and the classic port-wine-stain gene (*GNAQ*, somatic) is unrelated. This is either (a) a genuine and mechanistically unexplained component of SPG90A, or (b) a two-patient coincidence. It cannot be resolved at n=2, but it deserves recording — it is potentially the most useful *diagnostic handle* for recognizing the next case, and it is a real knowledge gap.

**2. The EEG/seizure dissociation matters for accurate curation.** All three founding patients had epileptiform EEG abnormalities, but only Patient 3 — the **SPG90B** (recessive) patient — had clinical seizures:

> Patient 1: "Electroencephalography at 2 years of age showed frequent sleep potentiated multifocal spikes which rarely synchronized but no evidence of clinical seizures."
> Patient 2: "Her EEG showed mild diffuse background slowing, multifocal polymorphic sharp waves, and sharp slow waves during sleep, but no seizures."
> Patient 3 (SPG90B): "Around 6 years of age, he developed rolandic seizures with temporoparietal spike-waves evident on EEG." — [PMID:36718090](https://pmc.ncbi.nlm.nih.gov/articles/PMC10319774/)

HPO correctly scores Seizure as **0/2** for OMIM:620416. Review-level sources that list "seizures" as a cHSP feature (e.g. Table 1 of PMID:38788085) are pooling SPG90A and SPG90B. **Abnormal EEG (HP:0002353) should be curated for SPG90A; clinical seizure should not**, or should be curated as absent.

**3. Nerve conduction and EMG were normal in all three patients** — "showed no evidence of polyneuropathy or motor neuron disease." This is the electrophysiological anchor for pure upper-motor-neuron localization and the key discriminator from the *SPTLC1*/*SPTLC2* juvenile ALS phenotype. It is a **negative finding with high diagnostic value** (see §10).

### Onset, severity, progression

- **Onset:** Infantile (HP:0003593), 2/2. Developmental concerns precede recognizable spasticity.
- **Severity:** Severe and **markedly variable even between two carriers of the identical allele**. Patient 1 achieved sitting at 11–12 months and a scissoring gait with a walker by age 3–4, with 4–6-word phrases at age 4. Patient 2 "never acquired the ability to sit independently," had no leg control by age 8, and was non-verbal, communicating "through facial/eye expressions." This is dramatic intrafamilial-equivalent variable expressivity on a single de novo allele.
- **Progression:** Progressive on both motor and cognitive axes. Patient 2's serial MRI showed "progressive cerebral volume loss and development of cerebellar atrophy." The review describes "Progressive cognitive decline and sensorineural hearing loss" as clinical features (PMID:38788085) — i.e. this is neurodegeneration layered on a neurodevelopmental baseline, not static encephalopathy.

### Quality of life

**No QoL instrument (EQ-5D, SF-36, PROMIS, SPRS) has been administered in any SPG90A patient.** Inferring from the documented function: non-ambulatory or walker-dependent mobility, absent-to-limited expressive language, dysphagia and reflux requiring feeding management, and hearing impairment together imply near-total dependence for activities of daily living. Patient 3's hearing loss "improved with hearing aids" and normal subsequent language development is the one documented instance of an intervention meaningfully changing a functional trajectory in this gene — though that patient is SPG90B.

---

## 4. Genetic / Molecular Information

### Causal gene

***SPTSSA*** — serine palmitoyltransferase small subunit A (hgnc:20361; OMIM *613540; 14q13.1; UniProt Q969W0; Ensembl ENSG00000165389). Also known as C14orf147, ssSPTa, SSSPTA.

The protein is tiny and purely regulatory:

> "The deduced 71-amino acid SSSPTA peptide contains 2 predicted transmembrane spans and shares 45% identity with SSSPTB, with most similarity in a central 28-amino acid domain that overlaps transmembrane span 2." — OMIM *613540

Function, from cryo-EM:

> "SPTssa participates in acyl-CoA coordination, thereby stimulating the SPT activity and regulating the substrate selectivity." — Li et al. 2021, [PMID:33558762](https://pubmed.ncbi.nlm.nih.gov/33558762/)

### Pathogenic variants

| Variant | cDNA | Protein | Zygosity | Origin | Disease | Consequence |
|---|---|---|---|---|---|---|
| Recurrent SPG90A allele | c.152C>T | p.Thr51Ile | Heterozygous | **de novo** (P1, P2) | SPG90A | Activating / loss-of-restraint |
| SPG90B allele | c.171_172del | p.Gln58AlafsTer10 | Homozygous | Inherited (non-consanguineous Ashkenazi parents) | **SPG90B** — out of scope | C-terminal 14 aa replaced by 10 out-of-frame residues |

**p.Thr51Ile is the only known SPG90A allele.** All three published SPG90A patients carry it:

> "Exome sequencing revealed a heterozygous pathogenic variant (p.Thr51Ile), which was detected in two of the reported patients, suggesting a recurrent variant in this syndrome." — [PMID:40533086](https://pubmed.ncbi.nlm.nih.gov/40533086/)

**Variant classification (ACMG/AMP):** Pathogenic. The supporting criteria are unusually strong for an ultra-rare allele — de novo occurrence in two independent probands with consistent phenotype (PS2, applied twice), well-established functional studies demonstrating the damaging mechanism (PS3, from HEK293, patient fibroblast, and *Drosophila* work), and absence from population databases (PM2).

**Variant type:** Missense, located in the transmembrane region of the small subunit. This structural placement is the shared feature of the unrestrained-SPT phenotypes:

> "those variants that affect the transmembrane domains of *SPTLC1* or *SPTSSA* or intermembrane domain of *SPTLC2* are more likely to cause jALS or cHSP" — [PMID:38788085](https://pubmed.ncbi.nlm.nih.gov/38788085/)

**Allele frequency:** p.Thr51Ile is absent from gnomAD (consistent with de novo occurrence and a severe pediatric dominant phenotype). For contrast, the SPG90B frameshift c.171_172del is present at 0.0000517 overall and **0.001191 in the Ashkenazi Jewish population**, with no homozygotes — a carrier frequency that suggests a modest Ashkenazi founder effect for the *recessive* pole (see §9). *Note: I could not directly retrieve the gnomAD gene-constraint page for* SPTSSA*; pLI, LOEUF, and missense-Z values should be looked up directly at gnomad.broadinstitute.org before being curated as facts.*

**Somatic vs germline:** Germline, de novo. No somatic or mosaic mechanism described.

**Functional consequence:** This requires care, because the mechanism does not map cleanly onto standard categories. The variant is **activating** — a gain of pathway function achieved through **loss of a regulatory interaction**. In dismech's schema terms this argues for `functional_impact_category: GAIN_OF_FUNCTION` on the variant (the allele confers unrestrained activity) with a `modifier: LOSS_OF_FUNCTION` on the *negative regulation of sphingolipid biosynthetic process* node. Both descriptions are true of different objects; conflating them into one slot loses the mechanism. Direct evidence for the de-restraint:

- SPT carrying T51I was "less responsive to inhibition by co-transfected ORMDL3."
- "ORMDL silencing had minimal effect on T51I-containing SPT activity" — i.e. the brake was already off.
- Patient fibroblasts showed reduced responsiveness to C8-ceramide feedback inhibition.
- Microsomal SPT activity in Patients 1 and 2 was "comparable to that from age and gender matched control fibroblasts" — **the enzyme is not hyperactive in isolation; it is unregulated in the cell.** This is an important subtlety: bulk enzyme assays are normal while cellular flux is elevated.

### Modifier genes, epigenetics, chromosomal abnormalities

**None reported for any of these categories.** No methylation, histone, or chromatin data exist for SPG90A. No CNV, aneuploidy, translocation, or inversion mechanism — this is a single-nucleotide dominant disorder. Chromosomal microarray has no role.

---

## 5. Environmental Information

**Environmental factors:** None. No entry in CTD, no toxicological or radiation association.

**Lifestyle factors:** One, and it is dietary and *harmful*: **L-serine supplementation should be avoided** (see §2, §12). This is the only lifestyle/nutritional variable with a mechanistic rationale in this disease, and its sign is negative.

**Infectious agents:** Not applicable.

---

## 6. Mechanism / Pathophysiology

### The causal chain

```
SPTSSA p.Thr51Ile (transmembrane face of the small subunit)
   ↓ DIRECT
Impaired ORMDL binding / failed ceramide-triggered feedback inhibition of SPT
   ↓ DIRECT
Unrestrained de novo sphingolipid synthesis (elevated serum + fibroblast SLs)
   ↓ INDIRECT, intermediates unknown in humans
   ├──→ Distal degeneration of long corticospinal axons ──→ loss of supraspinal
   │      inhibitory control of the stretch reflex ──→ lower-limb spasticity,
   │      spastic paraparesis, loss of ambulation
   └──→ Broader CNS developmental + degenerative involvement ──→ global
          developmental delay, intellectual disability, progressive cognitive
          decline, cerebral/cerebellar volume loss, SNHL, dystonia,
          epileptiform EEG
```

The founding authors' own attribution of the terminal step:

> "These findings support the pathogenicity of the *SPTSSA* variants and point to excessive sphingolipid synthesis due to impaired homeostatic regulation of serine palmitoyltransferase as responsible for defects in early brain development and function." — [PMID:36718090](https://pubmed.ncbi.nlm.nih.gov/36718090/)

### Molecular pathway

**De novo sphingolipid biosynthesis** (KEGG hsa00600 Sphingolipid metabolism; Reactome R-HSA-1660661 Sphingolipid de novo biosynthesis). SPT catalyzes the first, committed, rate-limiting step: condensation of L-serine with palmitoyl-CoA to form 3-ketodihydrosphingosine, via a PLP-dependent mechanism.

The holoenzyme architecture, from cryo-EM ([PMID:33558762](https://pubmed.ncbi.nlm.nih.gov/33558762/)):

> "SPTLC1 and SPTLC2 form a dimer of heterodimers as the catalytic core. SPTssa participates in acyl-CoA coordination, thereby stimulating the SPT activity and regulating the substrate selectivity. ORMDL3 is located in the center of the complex, serving to stabilize the SPT assembly."

The homeostatic sensing mechanism was solved two years later ([Xie et al., *Nat Commun* 2023, PMID:37308477](https://pubmed.ncbi.nlm.nih.gov/37308477/), DOI 10.1038/s41467-023-39274-y):

> "purified human SPT-ORMDL complexes are inhibited by the central sphingolipid metabolite ceramide... Structure-guided mutational analyses reveal the essential function of this ceramide binding site for the suppression of SPT activity... ceramide can induce and lock the N-terminus of ORMDL3 into an inhibitory conformation."

That paper also showed that "childhood amyotrophic lateral sclerosis (ALS) variants in the SPTLC1 subunit cause impaired ceramide sensing in the SPT-ORMDL3 mutants" — establishing broken ceramide-sensing as the shared molecular lesion class into which the *SPTSSA* variants fall. **This structural work is highly relevant to SPG90A and is not currently cited in the draft KB entry.**

**Normal homeostatic logic:**

> "Sphingolipids are both essential and cytotoxic and their synthesis must therefore be tightly regulated. Key to the homeostatic regulation are the ORMDL proteins that are bound to serine palmitoyltransferase and mediate feedback inhibition of enzymatic activity when sphingolipid levels become excessive." — [PMID:36718090](https://pubmed.ncbi.nlm.nih.gov/36718090/)

### Suggested GO terms

| GO ID | Label | Modifier |
|---|---|---|
| GO:0004758 | serine C-palmitoyltransferase activity | GAIN_OF_FUNCTION |
| GO:0090155 | negative regulation of sphingolipid biosynthetic process | LOSS_OF_FUNCTION |
| GO:0030148 | sphingolipid biosynthetic process | INCREASED |
| GO:0017059 | serine palmitoyltransferase complex | — (cellular component / complex) |
| GO:0005783 | endoplasmic reticulum | — (subcellular site of SPT) |
| GO:0046513 | ceramide biosynthetic process | INCREASED (inferred) |
| GO:0006672 | ceramide metabolic process | INCREASED (inferred) |

### Cellular processes

**Established:** Dysregulated lipid homeostasis at the ER membrane. **Inferred but not demonstrated in SPG90A:** membrane composition change in myelin and axolemma, axonal transport failure, and length-dependent dying-back degeneration. The rationale for expecting neurological rather than systemic consequences:

> "Sphingolipids are a diverse family of lipids with critical structural and signalling functions in the mammalian nervous system, where they are abundant in myelin membranes." — [PMID:36718090](https://pubmed.ncbi.nlm.nih.gov/36718090/)

The strongest mechanistic *analogy* for how excess/aberrant sphingoid bases damage neurons comes from the *Sptssb* Stellar mouse ([PMID:26438849](https://pubmed.ncbi.nlm.nih.gov/26438849/)):

> "resulting in surprising neurodegenerative effects including aberrant membrane structures, accumulation of ubiquitinated proteins on membranes, and axon degeneration... our studies also suggest that excessive C20 LCBs or C20 LCB-containing sphingolipids impair protein homeostasis and neural functions."

Note carefully: this is a *different gene* (*Sptssb*), a *different molecular lesion* (altered acyl-CoA substrate affinity, not lost ORMDL restraint), and a *different lipid species* (C20 long-chain bases). It supports the general principle that SPT small-subunit dysregulation is neurodegenerative; it does not establish the SPG90A mechanism.

### Protein dysfunction

No misfolding or aggregation of SPTSSA itself is described. The defect is a **lost protein–protein interaction interface** — the variant sits on the transmembrane face where the small subunit participates in the ORMDL-regulated assembly. Structures available: PDB **7YIU** (C6-ceramide-bound SPT–ORMDL3), **7YIY** (SPT–ORMDL3), **7YJ1** (ORMDL3-ΔN2), **7YJ2** (ORMDL3-N13A). These provide a direct structural framework for modeling p.Thr51Ile, which to my knowledge has not been published.

### Metabolic changes

Elevated de novo sphingolipid synthesis, measured in two compartments:

- **Serum:** "Serum levels of SLs were increased in all three patients."
- **Fibroblasts:** Patients 1 and 2 "showed substantially elevated synthesis compared to controls."

**Critically, 1-deoxysphingolipids are NOT the accumulating species.** The full text does not report deoxySL elevation, and the mechanistic distinction is central to the disease family: HSAN1 variants shift SPT's substrate preference from L-serine to L-alanine/glycine, generating toxic 1-deoxySLs; the unrestrained-SPT variants instead overproduce **canonical** sphingolipids. Per the 2024 review, *SPTLC1*-ALS variants show "unrestrained SPT activity and overproduction of canonical sphingolipid species instead of overproduction of 1-deoxysphingolipids." The same logic applies to *SPTSSA*. **A curated entry should not import deoxySL toxicity from HSAN1.**

*Gap:* No untargeted sphingolipidomic profile of an SPG90A patient distinguishing which specific ceramide/sphingomyelin/hexosylceramide species accumulate has been published with quantitative values.

### Immune system involvement

None described. (Worth noting that *ORMDL3* — the regulatory partner — is a major asthma susceptibility locus, but no immune or atopic phenotype has been reported in any SPG90 patient.)

### Tissue damage mechanisms

Axonal degeneration and progressive brain volume loss. Patient 2's magnetic resonance spectroscopy showed **"decreased NAA and increased lactate signals"** — decreased N-acetylaspartate indicating neuronal/axonal loss, and elevated lactate suggesting impaired oxidative metabolism. This is the only *in vivo* human evidence of a bioenergetic component and is a notable, uncurated finding.

### Molecular profiling status

| Modality | Status |
|---|---|
| Targeted lipidomics (LC-MS) | **Done** — serum + fibroblasts, all 3 founding patients |
| Enzymatic/microsomal SPT assays | **Done** |
| Transcriptomics | **Not done.** No GEO/ArrayExpress accession for SPG90A |
| Proteomics | Not done |
| Untargeted metabolomics / full sphingolipidomics | **Not done in SPG90A** (done for *SPTLC1*-ALS) |
| Single-cell / spatial transcriptomics | Not done |
| CRISPR/RNAi functional screens | Not done for this disease |

**There is no disease-specific omics dataset accession for SPG90A.** The founding study's data are targeted assays, not deposited datasets. A `datasets:` block cannot be honestly curated.

---

## 7. Anatomical Structures Affected

### Organ level

- **Primary:** Central nervous system. Specifically the **corticospinal tract** (UBERON:0002314 / UBERON:0001075 pyramidal tract), inferred from selective upper-motor-neuron signs with normal EMG/NCS.
- **Secondary CNS:** Cerebrum (progressive volume loss), **cerebellum** (UBERON:0002037 — atrophy on serial MRI in Patient 2), **corpus callosum** (UBERON:0002336 — thinning, in the SPG90B patient), lateral ventricles (UBERON:0002285 — ventriculomegaly), cerebral white matter (UBERON:0002316 — depressed volume).
- **Cochlea / auditory system** (UBERON:0001844): sensorineural hearing loss.
- **Genitourinary** (bladder UBERON:0001255; kidney UBERON:0002113): proposed only, from a single patient.
- **Skeletal:** scoliosis (vertebral column, UBERON:0000955... more precisely UBERON:0002240 spinal cord vs UBERON:0001130 vertebral column — use the latter for scoliosis).
- **Skin** (UBERON:0002097): nevus flammeus / capillary malformation.
- **Body systems:** Nervous (primary), auditory, musculoskeletal, gastrointestinal (dysphagia, GERD), integumentary, genitourinary (provisional).

**Explicitly spared:** Peripheral nerve and lower motor neurons. "All three patients showed no evidence of polyneuropathy or motor neuron disease" on NCS/EMG. This negative localization is diagnostically load-bearing.

### Tissue and cell level

| CL / UBERON | Term | Basis |
|---|---|---|
| CL:0008048 | upper motor neuron | Inferred from clinical localization |
| CL:0000679 | glutamatergic neuron (corticospinal projection neurons) | Inferred |
| CL:0000128 | oligodendrocyte | Inferred — sphingolipids are myelin components; **not demonstrated** |
| CL:0000855 | sensory hair cell | Inferred from SNHL; cochlear vs retrocochlear localization **never determined** |
| UBERON:0002240 | spinal cord | Site of corticospinal axon degeneration |

**Every cell-type assignment here is inferential.** No neuropathological examination of an SPG90A patient has been published. There is no autopsy, no biopsy, no iPSC-derived neuron model of *SPTSSA* p.Thr51Ile. Curators should mark these as inferred from clinical localization plus class-level HSP knowledge.

### Subcellular level

- **GO:0005783 endoplasmic reticulum** — SPT is an ER-resident membrane complex; this is where the lesion physically sits.
- **GO:0005789 endoplasmic reticulum membrane** — more precise.
- **GO:0017059 serine palmitoyltransferase complex** — the affected assembly.
- Inferred downstream: axonal plasma membrane, myelin sheath (GO:0043209).

### Localization and lateralization

**Bilateral and symmetric**, as expected for a genetic corticospinal tract disorder. Length-dependent distal predominance is the class-level HSP expectation and is *imported*, not demonstrated in SPG90A.

---

## 8. Temporal Development

**Onset:** Infantile (HP:0003593, 2/2). Perinatal history was unremarkable in both index patients; Patient 2 was "born at 39 weeks after uneventful pregnancy." The first manifestation is developmental — delayed motor and language milestones — with spasticity becoming apparent as the child fails to acquire or loses ambulation. The port-wine stain was present at birth (P1) or appeared in infancy (P2), making it potentially the **earliest observable sign**.

**Onset pattern:** Insidious and chronic. No acute or subacute presentation.

**Progression rate and stages:** Slow but unequivocally progressive, on two independent axes:

- *Motor:* P1 — sitting at 11–12 months → scissoring gait with walker by 3–4 years. P2 — never sat independently → no leg control by age 8. Patient 4 — unable to walk at age 10. For contrast, the SPG90B patient walked independently at 24 months and **lost ambulation by age 10**, documenting frank regression.
- *Cognitive/structural:* "Progressive cognitive decline" (PMID:38788085); serial MRI in P2 showed "progressive cerebral volume loss and development of cerebellar atrophy."

**Course pattern:** Progressive. Not episodic, relapsing-remitting, or fluctuating.

**Duration:** Chronic, lifelong. No published patient has died; the oldest SPG90A patient reported is 10 years old, so adult outcomes are entirely unknown.

**Remission:** None, spontaneous or treatment-induced.

**Critical periods:** Not established. Two considerations argue that an intervention window would be **early**: the disorder has a genuine neurodevelopmental component ("defects in early brain development and function"), implying that damage accrues before diagnosis; and the one intervention with a documented benefit — hearing aids from age 3 in the SPG90B patient, after which "normal language development" followed — was an early sensory intervention. This is a reasonable but unproven basis for arguing that any future SPT-directed therapy would need to start young.

---

## 9. Inheritance and Population

### Epidemiology

**Prevalence: not estimable.** Three published SPG90A patients worldwide. Use `measure_type: CASES_IN_LITERATURE`, `prevalence_class: ULTRA_RARE`, and do not assign a `rate_per_100000`.

> "To date, only three patients have been reported." — [PMID:40533086](https://pubmed.ncbi.nlm.nih.gov/40533086/), writing before adding their own (i.e., 4 total SPG90; 3 of them SPG90A).

For class-level context only — **do not attribute these figures to SPG90A** — the pooled global HSP prevalence from the standard systematic review ([Ruano et al., *Neuroepidemiology* 2014;42(3):174–83, PMID:24603320](https://pubmed.ncbi.nlm.nih.gov/24603320/), DOI 10.1159/000358801) is:

> "The prevalence of autosomal dominant (AD) HSP ranged from 0.5 to 5.5/10⁵ and that of AR-HSP from 0.0 to 5.3/10⁵, with pooled averages of 1.8/10⁵ (95% CI: 1.0–2.7/10⁵) and 1.8/10⁵ (95% CI: 1.0–2.6/10⁵), respectively."

SPG4 dominates AD-HSP, followed by SPG3A. SPG90A is a vanishingly small fraction of that total.

### Inheritance

**Autosomal dominant (HP:0000006)**, arising **de novo** in both index cases. There has been **no transmission from an affected parent to a child in any published pedigree** — every SPG90A case to date is sporadic.

**Penetrance:** Complete in reported cases (n=3), but this is uninformative — de novo ascertainment guarantees affected probands and tells you nothing about whether a milder carrier would come to attention.

**Expressivity: highly variable**, and this is a substantive finding rather than a hedge. Patients 1 and 2 carry the *identical de novo allele* on *different genetic backgrounds* and differ profoundly: walker-assisted ambulation with phrase speech versus never sitting and non-verbal. Whatever determines severity in SPG90A is not the allele. This is the single strongest argument that unidentified modifiers exist.

**Genetic anticipation:** Not applicable — no repeat expansion, no multigenerational pedigree.

**Germline mosaicism:** Not reported. Given two independent de novo events at the same nucleotide, recurrence risk counseling should nonetheless mention gonadal mosaicism as a small but non-zero possibility, per standard de novo-dominant practice.

**Founder effects:** None for SPG90A (p.Thr51Ile is absent from gnomAD and arose de novo twice — a recurrent mutational event, not a founder haplotype). A possible **Ashkenazi founder effect applies to the recessive SPG90B allele**: c.171_172del has an Ashkenazi allele frequency of **0.001191** (~1 in 420 carriers) versus 0.0000517 overall, with no homozygotes in gnomAD. **This is an SPG90B fact and must not be attributed to SPG90A.**

**Consanguinity:** No role in SPG90A. (The SPG90B patient's parents were explicitly non-consanguineous, with the homozygosity attributable to the founder allele frequency.)

**Carrier frequency:** Not applicable to a de novo dominant disorder.

### Population demographics

- **Ethnic/geographic:** No population enrichment. Reported patients come from the US Undiagnosed Diseases Network (P1, P2) and Türkiye (P4). The Ashkenazi association is exclusive to SPG90B.
- **Sex ratio:** All three SPG90A patients are female. **At n=3 this is statistically meaningless** and should not be curated as a sex bias. There is no mechanistic basis for one (autosomal gene, autosomal dominant).
- **Age distribution:** All reported patients are children (ages 5, 10, and 10 at report). No adult SPG90A patient has been described.

---

## 10. Diagnostics

### The diagnostic pathway in practice

Both index patients reached diagnosis through the **Undiagnosed Diseases Network via exome sequencing** — i.e., SPG90A is currently a diagnosis of genomic discovery, not of clinical suspicion. There is no clinician who diagnoses SPG90A from the bedside.

### Genetic testing

**Exome or genome sequencing is the appropriate first-tier test.** Rationale: the phenotype (global developmental delay + spasticity + hearing loss) is not specific enough to direct single-gene testing, and *SPTSSA* is a recently described gene that may be absent from older HSP panels. GeneReviews' general HSP guidance applies:

> "A multigene panel that includes some or all the genes listed in Tables 1 and 2 is most likely to identify the genetic cause of the condition while limiting identification of pathogenic variants." — [GeneReviews, Hereditary Spastic Paraplegia Overview, NBK1509](https://www.ncbi.nlm.nih.gov/books/NBK1509/)

**Practical caveat for curators and clinicians:** verify that any HSP panel offered actually includes *SPTSSA*. Given the 2023 gene-disease discovery date, panel inclusion is not guaranteed. Trio exome/genome is preferable because it establishes de novo status directly — which is both the strongest ACMG evidence (PS2) and the key to accurate recurrence counseling.

| Test | Utility in SPG90A |
|---|---|
| Trio WES / WGS | **First-line.** How all reported cases were diagnosed |
| HSP multigene panel | Useful *if it contains SPTSSA* — confirm before ordering |
| Single-gene *SPTSSA* sequencing | Reasonable only for targeted confirmation or family testing of the known p.Thr51Ile allele |
| Chromosomal microarray | **No role** — no CNV mechanism |
| Karyotype / FISH | **No role** |
| mtDNA testing | **No role** (though it may feature in the differential given the elevated MRS lactate) |
| Repeat expansion testing | **No role** |

### Biomarkers and laboratory tests

**Plasma/serum sphingolipid profiling is the disease-relevant biochemical assay** and is currently the only candidate biomarker: "Serum levels of SLs were increased in all three patients" (PMID:36718090). The 2024 review positions "untargeted sphingolipidomic studies of patient serum samples" as the key modality for distinguishing mechanisms across the SPT disease family — HSAN1 (1-deoxySL elevation) versus unrestrained-SPT disorders (canonical SL elevation).

**However, this is a research assay, not a validated clinical diagnostic.** No reference interval, sensitivity, specificity, or clinical LOINC code exists for SPG90A. It should be curated as an investigational biomarker with `validation_status` explicitly unvalidated — not as a diagnostic test.

**De novo sphingolipid synthesis assay in cultured patient fibroblasts** is the functional confirmatory test used in the founding study, and is a legitimate route to reclassifying a *SPTSSA* VUS. Note the pitfall documented in that paper: **microsomal SPT activity was normal in the SPG90A patients** — only the cellular flux and the *responsiveness to ORMDL/ceramide inhibition* were abnormal. An assay measuring bulk enzyme activity will return a false negative. The informative readout is feedback-inhibition responsiveness.

### Imaging

Brain MRI findings are non-specific but support a progressive process:
- Ventriculomegaly with depressed white matter volume (P1, age 1)
- Progressive cerebral volume loss and cerebellar atrophy on serial imaging (P2, age 4)
- MR spectroscopy: decreased NAA, increased lactate (P2)
- Thinning of the corpus callosum (P3 — SPG90B)

**Serial rather than single MRI is what carries information here**, since it was the change between studies that revealed progression.

Spinal MRI is warranted given tethered cord in 1/2 patients — a surgically actionable finding that independently causes spasticity and must be assessed rather than assumed to be part of the genetic syndrome.

### Electrophysiology

**EEG:** Abnormal in all founding patients (multifocal sleep-potentiated spikes, polymorphic sharp waves, background slowing). Should be obtained; expect epileptiform abnormality without necessarily clinical seizures in SPG90A.

**NCS/EMG:** Should be **normal**. "All three patients showed no evidence of polyneuropathy or motor neuron disease." This normal result is diagnostically informative — it excludes the *SPTLC1*/*SPTLC2* juvenile ALS and HSAN1 phenotypes, which is precisely the discrimination that matters within this gene family.

**Audiometry:** Required — SNHL is present in a substantial fraction and is the one deficit with a demonstrably effective intervention.

### Biopsy / pathology

No histopathology, immunohistochemistry, or autopsy data exist for any SPG90A patient. Nerve biopsy has no role (peripheral nerve is spared).

### Clinical criteria and differential diagnosis

**No standardized diagnostic criteria exist for SPG90A.** Diagnosis is molecular.

Differential diagnosis for a child with global developmental delay plus progressive lower-limb spasticity:

| Category | Entities | Distinguishing features |
|---|---|---|
| Within the SPT family | *SPTLC1*/*SPTLC2* juvenile ALS | Combined UMN **and LMN** signs; atrophy, weakness, fasciculations; abnormal EMG |
| Within the SPT family | HSAN1 (*SPTLC1*, *SPTLC2*) | Sensory-predominant neuropathy; 1-deoxySL elevation; adult onset; **serine is therapeutic** |
| Other complicated HSPs | SPG11, SPG15, SPG50 (*AP4M1*), SPG7 | Panel/exome resolves |
| Non-genetic mimic | **Cerebral palsy** | The most important practical mimic — a non-progressive presumption delays diagnosis. Progression on serial exam/MRI is the discriminator |
| Structural | **Tethered cord** | Present in 1/2 SPG90A patients; must be imaged and may be independently treatable |
| Treatable metabolic | Dopa-responsive dystonia, cobalamin C, biotinidase deficiency, homocystinuria | GeneReviews flags these as must-excludes because they are treatable |
| Other | Leukodystrophies, spinocerebellar ataxias, MS, HTLV-1/HIV myelopathy | Per GeneReviews HSP Overview |

### Screening

**No newborn screening, carrier screening, or population screening applies.** A de novo dominant disorder with no carrier state and a single ultra-rare allele is not screenable. Cascade testing of parents is appropriate solely to confirm de novo status for recurrence counseling — not to identify at-risk relatives.

---

## 11. Outcome / Prognosis

**This section is the most data-poor in the report, and the honest summary is that SPG90A prognosis is unknown.**

- **Survival, life expectancy, mortality rate, disease-specific mortality:** **No data.** No SPG90A patient death has been reported. The oldest reported patient is 10. Any survival figure would be fabrication. Note for contrast that the *Drosophila* model shows shortened lifespan and the *Sptssb* Stellar mouse shows premature death — **neither licenses a human life-expectancy claim.**
- **Morbidity:** Severe. Documented outcomes include non-ambulation by age 8–10, absent speech, intellectual disability, dysphagia, and hearing impairment — a combination implying full-time care dependence.
- **Disability outcomes:** No ICF-coded or standardized disability assessment has been performed.
- **Quality of life measures:** None administered. No EQ-5D, SF-36, PROMIS, or the HSP-specific Spastic Paraplegia Rating Scale (SPRS).
- **Complications:** Reported or expected — aspiration secondary to dysphagia, GERD, scoliosis (progressive, potentially surgical), contractures from chronic spasticity, failure to thrive, and (provisionally, from the fourth patient) nephrolithiasis, recurrent UTI, and neurogenic bladder with its attendant renal risk.
- **Recovery potential:** None for the neurological deficit. The one documented functional gain in the gene family is **auditory**: the SPG90B patient's hearing loss "improved with hearing aids," after which language developed normally — a strong argument for aggressive early audiological management.
- **Prognostic factors:** **Unknown, and notably not predicted by genotype** — the two patients sharing the identical p.Thr51Ile allele had radically different severity. Whatever predicts outcome here is not the variant.
- **Prognostic biomarkers:** None validated. Whether the magnitude of serum sphingolipid elevation tracks severity is an obvious and untested hypothesis — worth recording as a proposed experiment.

---

## 12. Treatment

### Current state

**No disease-modifying therapy exists.** Management is entirely symptomatic and supportive, following general complicated-HSP practice. **No clinical trial has ever enrolled an SPG90A patient**, and no NCT or ICTRP identifier exists for this disorder.

### The one disease-specific management directive

**Avoid L-serine supplementation.** This is the single most important treatment fact for SPG90A and it is a *contraindication*, which makes it easy to miss:

> "Elevated serine exacerbates the overproduction of SLs associated with the *SPTLC1* juvenile ALS variants and the *SPTSSA* variants described here... Thus serine supplementation is not a rational therapeutic strategy and may even be detrimental for these patients." — [PMID:36718090](https://pmc.ncbi.nlm.nih.gov/articles/PMC10319774/)

The 2024 review's Table 1 lists the cHSP (*SPTSSA*) treatment strategy as, verbatim, **"Avoid serine supplementation; SPT inhibition."**

Why this is a real clinical hazard rather than a theoretical one: L-serine supplementation *is* the established rationale for HSAN1, caused by variants in the *same enzyme complex*. A clinician who recognizes "serine palmitoyltransferase disorder" and reaches for the familiar intervention would be actively worsening the disease. Any KB entry for SPG90A should carry this as an explicit contraindication, not merely omit serine from the treatment list.

### Symptomatic pharmacotherapy

Extrapolated from general HSP management ([GeneReviews NBK1509](https://www.ncbi.nlm.nih.gov/books/NBK1509/)); **no trial evidence specific to SPG90A**:

> "Baclofen, botulinum toxin, dantrolene, tizanidine (used 1 at a time), especially early in disease course to decrease cramps."

with the caution that dantrolene should be avoided in ambulatory patients due to risk of irreversible weakness.

| Treatment | Agent | NCIT | Modality |
|---|---|---|---|
| Antispasticity pharmacotherapy | baclofen (CHEBI:2972) | NCIT:C15986 Pharmacotherapy | SMALL_MOLECULE |
| Antispasticity pharmacotherapy | tizanidine (CHEBI:63631) | NCIT:C15986 | SMALL_MOLECULE |
| Focal spasticity injection | botulinum toxin type A (NCIT:C1090) | NCIT:C15986 | OTHER/PROTEIN |
| Intrathecal baclofen (for refractory spasticity) | baclofen | NCIT:C15986 / device | DEVICE |
| Anticholinergic for neurogenic bladder | oxybutynin (CHEBI:7856), solifenacin | NCIT:C15986 | SMALL_MOLECULE |
| Anticonvulsant (SPG90B; consider if clinical seizures) | per seizure type | NCIT:C15986 | SMALL_MOLECULE |

### Supportive, rehabilitative, and surgical

| Intervention | NCIT | Rationale |
|---|---|---|
| Physical therapy | NCIT:C15302 | Addresses the **non-reflex** soft-tissue component of hypertonia, not just the reflex component ([PMID:25530960](https://pubmed.ncbi.nlm.nih.gov/25530960/)); preserves range of motion |
| Occupational therapy | NCIT:C121351 | Adaptive equipment, ADL support |
| Speech and language therapy | NCIT:C159273 | Delayed/absent speech; also dysphagia management |
| **Hearing aids / audiological management** | (device) | **The one intervention with documented functional benefit in this gene** — SPG90B patient's language normalized after aids at age 3 |
| Nutritional support / feeding management | NCIT:C15433 | Dysphagia, GERD, failure to thrive. **Note: this is nutritional supplementation, not a "dietary modification" — and it must not include serine** |
| Orthopedic surgery (scoliosis, contractures) | NCIT:C16186 | Progressive scoliosis |
| Neurosurgery for tethered cord | NCIT:C15329 | **Independently treatable contributor to spasticity** — must be evaluated |
| Genetic counseling | NCIT:C15240 | De novo recurrence risk; gonadal mosaicism |
| Supportive care (overall) | NCIT:C15747 | |

Botulinum toxin in HSP specifically has a recent dedicated review ([PMC12567745](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12567745/), 2025).

### Experimental and future therapeutics

**None in or near clinical trial for SPG90A.** The 2024 review outlines the rational targets:

- **SPT inhibition.** "Myriocin (also known as thermozymocidin or ISP-10)" is the canonical potent SPT inhibitor but faces "toxicity" barriers to clinical development. This is the mechanistically correct target — the pathway is overactive — but no tolerable clinical-stage SPT inhibitor exists.
- **Allele-specific knockdown / ASOs.** The review states "allele-specific knockdown is a feasible approach" and that "antisense oligonucleotides (ASOs), improves on the generalizability limitations." A single recurrent allele (p.Thr51Ile) in a dominant gain-of-function disorder is close to the ideal ASO/siRNA target profile — arguably SPG90A's most tractable future therapeutic avenue.
- **Open questions the authors flag:** the need to "establish the tolerated threshold for SPT inhibition" and determine "optimal timing of interventions." Both are unresolved, and the second is sharpened by SPG90A's neurodevelopmental component.

**Precedent from the HSP field:** AAV9 gene therapy for SPG50 (*AP4M1*) reached a single-patient phase 1 trial and "was well tolerated, showing preliminary evidence of disease stabilization" ([*Nat Med* 2024, PMC11271397](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11271397/)). Note that this is a *gene replacement* strategy for a loss-of-function disorder and is **not** transferable to SPG90A — a gain-of-function disease needs knockdown or inhibition, not replacement. ASO work targeting GM3 synthase in an SPG11 model is a closer conceptual analog.

### Pharmacogenomics

None. No PharmGKB or CPIC guidance applies.

### Treatment outcomes, response rates, adverse events

**No data for SPG90A.** Response rates and adverse-event profiles for baclofen, tizanidine, and botulinum toxin come from the general spasticity literature and should be cited as such, never as SPG90A-specific.

---

## 13. Prevention

**Primary prevention: not possible.** A de novo dominant mutation cannot be prevented by risk-factor modification, immunization, or environmental intervention.

**Secondary prevention (early detection):** No screening program applies. The realistic lever is **reducing diagnostic delay** — earlier trio exome in children with unexplained global developmental delay plus progressive spasticity, and resisting a default "cerebral palsy" label when the course is progressive.

**Tertiary prevention (complication prevention) is where the actionable content sits:**

| Target complication | Preventive action |
|---|---|
| Contractures, joint deformity | Early and sustained physiotherapy, stretching, orthotics |
| Progressive scoliosis | Serial spine monitoring; timely orthopedic referral |
| Aspiration pneumonia | Dysphagia assessment; feeding modification |
| Language deprivation from undetected SNHL | **Early audiology and hearing aids** — the one measure with demonstrated benefit in this gene |
| Renal damage from neurogenic bladder | Urological surveillance (provisional, based on the 4th patient) |
| Iatrogenic disease worsening | **Do not prescribe L-serine supplementation** |

**Genetic counseling:** Recurrence risk for the parents of a de novo proband is low but not zero (gonadal mosaicism). An affected individual would have a 50% transmission risk, though no SPG90A patient has reproduced. **Prenatal diagnosis and PGT are technically straightforward** once the familial p.Thr51Ile variant is known — a defined single-nucleotide target.

**Immunization, public health, environmental interventions, prophylaxis:** Not applicable.

---

## 14. Other Species / Natural Disease

**Naturally occurring SPG90A does not exist in any non-human species.** No OMIA entry, no veterinary case, no wildlife or companion-animal disease. Not zoonotic; no cross-species transmission concept applies.

### Orthologs and conservation

| Species | NCBI Taxon | Gene | Resource |
|---|---|---|---|
| *Homo sapiens* | NCBITaxon:9606 | *SPTSSA* | HGNC:20361 |
| *Mus musculus* | NCBITaxon:10090 | *Sptssa* | MGI:1913399 |
| *Drosophila melanogaster* | NCBITaxon:7227 | *sptssa* / small subunit ortholog | FlyBase |

**Breed (VBO):** Not applicable.

### Comparative biology

The SPT complex is deeply conserved — the ORM/ORMDL regulatory system was first characterized in yeast (Orm1/Orm2), and the human ORMDL proteins are its direct descendants. This conservation is what makes the *Drosophila* model informative for the *biochemistry* despite the fly's total lack of the relevant anatomy.

A conserved-mechanism observation worth recording: the paralogous small subunit **SPTSSB** produces neurodegeneration in mouse when dysregulated ([PMID:26438849](https://pubmed.ncbi.nlm.nih.gov/26438849/)):

> "Our work demonstrates that SPT small subunits play a major role in controlling SPT activity and substrate affinity, and in specifying sphingolipid LCB chain length *in vivo*."

That the *general principle* "SPT small-subunit dysregulation → neurodegeneration" holds across mouse and human, via two different genes and two different molecular routes, is the strongest cross-species support available for SPG90A's pathogenesis.

---

## 15. Model Organisms

### Models that exist

**1. *Drosophila melanogaster* — the only model of the actual SPG90A variant.**

- **Type:** Invertebrate, transgenic overexpression (single-chain SPT construct, "scSPT," carrying the human p.Thr51Ile change), with GAL4-driven neuronal or ubiquitous expression.
- **Publication:** PMID:36718090
- **Phenotypes:** Neuronal expression caused "severely compromised climbing activity and... very short lifespan"; ubiquitous expression caused lethality at various developmental stages.
- **The key rescue experiment — this is the elegant part of the study:** "ORMDL3 expression rescues the lifespan in flies expressing WT scSPT but not in flies expressing the p.Thr51Ile scSPT variant." Correspondingly, ORMDL3 co-expression "abolished the C18 SL levels" with wild-type SPT but "did not fully suppress the production of C18 SLs" with T51I. **This is a clean in-vivo demonstration that the variant's defect is specifically insensitivity to ORMDL restraint** — not merely elevated activity.
- **Readouts:** climbing/motor performance (DECREASED), lifespan (DECREASED), whole-animal C18 sphingolipid levels (INCREASED).
- **Fidelity: MODERATE for the biochemistry, absent for the anatomy.** *Drosophila* has no corticospinal tract, no myelin, and no oligodendrocytes. The model demonstrates the metabolic lesion and an organismal motor consequence; it cannot demonstrate length-dependent upper-motor-neuron degeneration. It is also an *overexpression* model, which is a further remove from the human heterozygous knock-in situation.

**2. *Sptssb* "Stellar" (Stl) mouse — a related-but-different mammalian model.**

- **Type:** Spontaneous chemically-arising mutation in the *paralogous* small subunit *Sptssb*.
- **Publication:** [PMID:26438849](https://pubmed.ncbi.nlm.nih.gov/26438849/), *PNAS* 2015.
- **Mechanism:** "increased the SPT affinity toward the C18 fatty acyl-CoA substrate by twofold and significantly elevated 20-carbon (C20) LCB production in the mutant mouse brain and eye."
- **Phenotypes:** "aberrant membrane structures, accumulation of ubiquitinated proteins on membranes, and axon degeneration"; ataxia and premature death.
- **Fidelity: LOW.** Wrong gene (*Sptssb*), wrong molecular mechanism (altered substrate affinity, **not** lost ORMDL restraint), wrong accumulating species (C20 LCBs, not canonical C18 SLs), wrong phenotype (ataxia, not spastic paraparesis). Curate as `PARTIALLY_RECAPITULATES` / `LOW` fidelity with explicit limitations. It supports a general principle, not the specific disease.

**3. *Sptssa* knockout mouse — exists, but is embryonic-lethal and therefore not a disease model.**

MGI records 7 alleles. The null phenotype ([MGI:1913399](https://www.informatics.jax.org/marker/MGI:1913399)): "decreased embryo size, failure of primitive streak formation, absent primitive node and head folds, failure to gastrulate, and complete embryonic lethality by E9.5."

**This is a mechanistically important negative.** Complete loss of *SPTSSA* is incompatible with gastrulation, which independently confirms that SPG90A **cannot** be a haploinsufficiency/loss-of-function disorder — the phenotype of losing this gene is embryonic death, not childhood spasticity. It corroborates the gain-of-function interpretation from an orthogonal direction.

### The critical model gap

> "No murine models with SPT-related ALS or HSP variants have been reported so far." — [PMID:38788085](https://pubmed.ncbi.nlm.nih.gov/38788085/) (2024)

**There is no mammalian model of any unrestrained-SPT disease variant** — not for SPG90A, not for *SPTLC1*-ALS. Combined with the absence of human neuropathology, this means the corticospinal localization of SPG90A rests entirely on **clinical inference** (selective UMN signs, normal EMG/NCS) plus class-level HSP knowledge. This should be curated as a `HUMAN_MODEL_MISMATCH` discussion, not glossed.

### Models that do not exist but should

| Proposed model | What it would resolve |
|---|---|
| **Knock-in mouse carrying *Sptssa* p.Thr51Ile** (heterozygous, matching human dosage) | Whether the lesion produces length-dependent corticospinal degeneration with LMN sparing; whether the developmental and auditory components reproduce; a substrate for preclinical SPT-inhibitor and ASO testing |
| **Patient-derived iPSC → cortical/spinal motor neurons** | The first *neuronal* measurement of sphingolipid excess in this disease — currently measured only in HEK293, fibroblasts, and fly |
| **Comparative sphingolipidomics across SPT-subunit alleles** | Whether *SPTSSA*-cHSP and *SPTLC1*-ALS accumulate different species, which is the leading hypothesis for the phenotypic divergence |

### Available model resources

MGI, IMSR (11 *Sptssa* strains/lines available), IMPC, Alliance of Genome Resources, FlyBase. **No SPG90A-specific patient cell line is deposited in Coriell or Cellosaurus** that I could identify; the patient fibroblasts used in PMID:36718090 appear to be lab-held.

---

## The central unresolved question

Worth stating on its own because it governs how much any SPG90A entry can claim. The *SPTSSA*, *SPTLC1*, and *SPTLC2* disease variants converge on **the same biochemical lesion** — impaired ORMDL regulation, unrestrained SPT — yet produce clinically distinct diseases: upper-motor-neuron-predominant complicated HSP with neurodevelopmental involvement versus combined UMN/LMN juvenile ALS. The founding authors are direct about not knowing why:

> "We do not yet understand why mutations in different subunits of SPT that similarly impact ORMDL regulation cause such distinct clinical presentations." — [PMID:36718090](https://pmc.ncbi.nlm.nih.gov/articles/PMC10319774/)

They offer the leading structural hypothesis:

> "All SPT isozymes contain SPTLC1 and are thus dysregulated in the ALS patients, but in the HSP patients only the isozymes containing SPTSSA are affected."

And the 2024 review adds a second, biochemical, hedged observation:

> "It is notable that unlike the *SPTLC1* and *SPTLC2*-related ALS variants, the cHSP-related *SPTSSA* variants do not increase, and likely decrease (via ORMDL inhibition) the activity of *SPTSSB*-containing SPT." — [PMID:38788085](https://pubmed.ncbi.nlm.nih.gov/38788085/)

> "Despite the biochemical similarities and differences between SPT-related juvenile ALS and cHSP, the mechanisms underlying the phenotypic differences remain poorly understood."

**Practical consequence:** no entry in this disease family should assert a specific downstream neurotoxic sphingolipid species as the effector. The identity of the toxic species in SPG90A is unknown.

---

## Findings that differ from, or are missing in, the existing draft KB entry

I read `kb/disorders/Spastic_Paraplegia_90A_Autosomal_Dominant.yaml` before researching. The draft is mechanistically sound and its evidence discipline is good. Five things surfaced that would change it:

**1. A factual error about the recurrent allele.** The draft's `description` says p.Thr51Ile "has now been reported in a third of the very small published cohort." The actual position: T51I is in **3 of 4 published SPG90 patients and 3 of 3 published SPG90A patients — it is the only known SPG90A allele, at 100%**. The "one third" reading appears to misparse "detected in two of the reported patients." The `genetic:` block's `notes` also says T51I was "found in two of the first three reported patients," but the third of those (homozygous p.Gln58AlafsTer10) is the **SPG90B** patient, so within the dominant entity the denominator is two, not three.

**2. Substantial phenotype under-coverage.** HPO annotations for OMIM:620416 (all from PMID:36718090) include several features present in **2/2** patients that the draft omits entirely: **nevus flammeus / port-wine stain (HP:0001052, 2/2)**, **short stature (HP:0004322, 2/2)**, **intellectual disability (HP:0001249, 2/2)**, **delayed ability to walk (HP:0031936, 2/2)**, and **appendicular spasticity (HP:0034353, 2/2)**. Also missing at 1/2 or 1/1: tethered cord, scoliosis, macrocephaly, dysphagia, GERD, drooling, failure to thrive, sleep disturbance, absent speech, delayed speech and language development. The port-wine stain at 2/2 is the most striking omission — it is as frequent as the spasticity and entirely unexplained.

**3. Missing clinical findings with diagnostic weight.** The draft does not record (a) **abnormal EEG in all patients without clinical seizures in the SPG90A pair** — the HPO annotation for Seizure is explicitly 0/2, so review sources listing "seizures" for cHSP are pooling in the SPG90B patient; (b) **normal NCS/EMG**, the negative finding that localizes the lesion and separates this from *SPTLC1*-ALS; (c) the MRI/MRS findings, including **decreased NAA and increased lactate**, the only in-vivo human evidence of a bioenergetic component.

**4. A missing treatment contraindication.** The draft's `treatments:` block lists supportive care, physiotherapy, and antispastic drugs but does not record that **L-serine supplementation should be avoided and may be harmful** — the one disease-specific management directive in the literature, and a real hazard precisely because serine *is* therapeutic in HSAN1, a disorder of the same enzyme complex.

**5. Two uncited highly relevant references.** [PMID:37308477](https://pubmed.ncbi.nlm.nih.gov/37308477/) (Xie et al., *Nat Commun* 2023) solves the ceramide-sensing mechanism that the disease breaks, with structures 7YIU/7YIY/7YJ1/7YJ2 and a demonstration that ALS variants impair ceramide sensing. The *Sptssa* **knockout mouse being embryonic-lethal by E9.5** (MGI:1913399) is a strong orthogonal argument that SPG90A cannot be haploinsufficiency — useful support for the entry's own gain-of-function framing.

I have not modified the file; you asked for research, so this is a report. Say the word and I'll apply these as edits, fetch the missing references through `just fetch-reference`, and run the validation loop.

---

## Sources

**Primary literature**
- Srivastava S, Shaked HM, Gable K, et al. *SPTSSA variants alter sphingolipid synthesis and cause a complex hereditary spastic paraplegia.* Brain. 2023;146(4):1420–1435. [PMID:36718090](https://pubmed.ncbi.nlm.nih.gov/36718090/) · DOI 10.1093/brain/awac460 · [PMC10319774](https://pmc.ncbi.nlm.nih.gov/articles/PMC10319774/) · [Oxford Academic](https://academic.oup.com/brain/article/146/4/1420/7010590)
- Duzenli T, Yusufova V, Cetin H, et al. *Identifying the Fourth Patient With Spastic Paraplegia 90, Extending the Phenotype Spectrum.* Clin Genet. 2026. [PMID:40533086](https://pubmed.ncbi.nlm.nih.gov/40533086/) · DOI 10.1111/cge.70009
- Mohassel P, Abdullah M, Eichler FS, Dunn TM. *Serine Palmitoyltransferase (SPT)-related Neurodegenerative and Neurodevelopmental Disorders.* J Neuromuscul Dis. 2024;11(4):735–747. [PMID:38788085](https://pubmed.ncbi.nlm.nih.gov/38788085/) · DOI 10.3233/JND-240014 · [PMC11307022](https://pmc.ncbi.nlm.nih.gov/articles/PMC11307022/) · [SAGE](https://journals.sagepub.com/doi/full/10.3233/JND-240014)
- Li S, Xie T, Liu P, Wang L, Gong X. *Structural insights into the assembly and substrate selectivity of human SPT–ORMDL3 complex.* Nat Struct Mol Biol. 2021;28(3):249–257. [PMID:33558762](https://pubmed.ncbi.nlm.nih.gov/33558762/) · DOI 10.1038/s41594-020-00553-7
- Xie T, Liu P, Wu X, et al. *Ceramide sensing by human SPT-ORMDL complex for establishing sphingolipid homeostasis.* Nat Commun. 2023. [PMID:37308477](https://pubmed.ncbi.nlm.nih.gov/37308477/) · DOI 10.1038/s41467-023-39274-y · [PMC10261145](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10261145/)
- Zhao L, Spassieva S, Gable K, et al. *Elevation of 20-carbon long chain bases due to a mutation in serine palmitoyltransferase small subunit b results in neurodegeneration.* PNAS. 2015. [PMID:26438849](https://pubmed.ncbi.nlm.nih.gov/26438849/) · DOI 10.1073/pnas.1516733112
- *SPTLC1 variants associated with ALS produce distinct sphingolipid signatures through impaired interaction with ORMDL proteins.* J Clin Invest. 2022;132(18):e161908. DOI 10.1172/JCI161908 · [PMC9479574](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9479574/) · [JCI](https://www.jci.org/articles/view/161908)
- Ruano L, Melo C, Silva MC, Coutinho P. *The Global Epidemiology of Hereditary Ataxia and Spastic Paraplegia: A Systematic Review of Prevalence Studies.* Neuroepidemiology. 2014;42(3):174–183. [PMID:24603320](https://pubmed.ncbi.nlm.nih.gov/24603320/) · DOI 10.1159/000358801 · [Karger](https://karger.com/ned/article/42/3/174/226445/The-Global-Epidemiology-of-Hereditary-Ataxia-and)
- *AAV gene therapy for hereditary spastic paraplegia type 50: a phase 1 trial in a single patient.* Nat Med. 2024. [PMC11271397](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11271397/) · [Nature Medicine](https://www.nature.com/articles/s41591-024-03078-4)
- *Botulinum Toxin Treatment in Hereditary Spastic Paraplegia — A Comprehensive Review and Update.* [PMC12567745](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12567745/)
- Cipriano L, Angelini C, Santorelli FM. *Hereditary spastic paraplegia: from decades of therapy to future innovations.* Ther Adv Neurol Disord. 2026. [SAGE](https://journals.sagepub.com/doi/10.1177/17562864251406589)

**Databases and reference resources**
- [OMIM #620416 — SPG90A](https://www.omim.org/entry/620416) · [OMIM #620417 — SPG90B](https://www.omim.org/entry/620417) · [OMIM *613540 — SPTSSA](https://omim.org/entry/613540)
- [MedGen C5830574 — Spastic paraplegia 90A](https://www.ncbi.nlm.nih.gov/medgen/?term=spastic+paraplegia+90A)
- [HPO annotations for OMIM:620416](https://ontology.jax.org/api/network/annotation/OMIM:620416)
- [MGI:1913399 — mouse *Sptssa*](https://www.informatics.jax.org/marker/MGI:1913399)
- [Human Protein Atlas — SPTSSA (ENSG00000165389)](https://www.proteinatlas.org/ENSG00000165389-SPTSSA/tissue)
- [GeneCards — SPTSSA](https://www.genecards.org/card/SPTSSA)
- [MalaCards — Spastic Paraplegia 90A, Autosomal Dominant](https://www.malacards.org/card/spastic_paraplegia_90a_autosomal_dominant)
- [GeneReviews — Hereditary Spastic Paraplegia Overview (NBK1509)](https://www.ncbi.nlm.nih.gov/books/NBK1509/)
- [Orphanet ORPHA:102013 — Complex hereditary spastic paraplegia](https://www.orpha.net/en/disease/detail/102013)
- RCSB PDB: [7YIU](https://www.rcsb.org/structure/7YIU) · [7YIY](https://www.rcsb.org/structure/7YIY) · [7YJ1](https://www.rcsb.org/structure/7YJ1) · [7YJ2](https://www.rcsb.org/structure/7YJ2)
- [Atlas of Genetics and Cytogenetics — SPTSSA](https://atlasgeneticsoncology.org/Genes/GC_SPTSSA.html)
- [Undiagnosed Diseases Network — SPTSSA](https://undiagnosed.hms.harvard.edu/genes/sptssa/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 23 |
| Resolved | 23 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 18 |
| Quoted claims found in source | 12 |
| Quoted claims **not** found in source | 6 |
| References weighed for topical relevance | 23 |
| On topic | 7 |
| Off topic | 1 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:36718090` *(abstract only)*: "Elevated serine exacerbates the overproduction of SLs associated with the *SPTLC1* juvenile ALS variants and the *SPTSSA* variants described here... Thus serine supplementation is not a rational therapeutic strategy and may even be detrimental for these patients."
  - closest text in source: "These findings support the pathogenicity of the SPTSSA variants and point to excessive sphingolipid synthesis due to impaired homeostatic regulation of serine palmitoyltransferase as responsible for defects in early brain development and function."
- `PMID:36718090` *(abstract only)*: "Around 6 years of age, he developed rolandic seizures with temporoparietal spike-waves evident on EEG."
  - Text part not found as substring: 'Around 6 years of age, he developed rolandic seizures with temporoparietal spike-waves evident on EEG.' (note: only abstract available for PMID:36718090, full text may contain this excerpt)
- `PMID:36718090` *(abstract only)*: "Serum levels of SLs were increased in all three patients"
  - closest text in source: "Exome sequencing identified potential disease-causing variants in SPTSSA in three children presenting with a complex form of hereditary spastic paraplegia"
- `PMID:36718090` *(abstract only)*: "Elevated serine exacerbates the overproduction of SLs associated with the *SPTLC1* juvenile ALS variants and the *SPTSSA* variants described here... Thus serine supplementation is not a rational therapeutic strategy and may even be detrimental for these patients."
  - closest text in source: "These findings support the pathogenicity of the SPTSSA variants and point to excessive sphingolipid synthesis due to impaired homeostatic regulation of serine palmitoyltransferase as responsible for defects in early brain development and function."
- `PMC:PMC11271397` *(abstract only)*: "was well tolerated, showing preliminary evidence of disease stabilization"
  - closest text in source: "Preliminary efficacy measures suggest a stabilization of the disease course"
- `PMID:36718090` *(abstract only)*: "We do not yet understand why mutations in different subunits of SPT that similarly impact ORMDL regulation cause such distinct clinical presentations."
  - closest text in source: "Key to the homeostatic regulation are the ORMDL proteins that are bound to serine palmitoyltransferase and mediate feedback inhibition of enzymatic activity when sphingolipid levels become excessive"

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `DOI:10.1073/pnas.1516733112` (1 mention) - Elevation of 20-carbon long chain bases due to a mutation in serine palmitoyltransferase small subunit b results in neurodegeneration
  - shared terms: sphingolipid, serine

Weighed against this report's own most characteristic terms: `spg90a`, `patient`, `disease`, `sptssa`, `spt`, `variant`, `gene`, `sphingolipid`, `clinical`, `novo`, `dominant`, `disorder`, `spasticity`, `spg90b`, `thr51ile`, `mechanism`, `allele`, `als`, `serine`, `sptlc1`.