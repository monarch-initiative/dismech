---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-15T08:51:22.357460'
end_time: '2026-08-15T09:09:16.729722'
duration_seconds: 1074.37
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Chuvash Polycythemia
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
  - claude-opus-5[1m]
  web_search_requests: 2
  num_turns: 59
  total_cost_usd: 8.122979
  session_id: 38281f5b-24f5-4b11-8e6d-35bfec9a0e96
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  - Write
  assistant_text_blocks: 1
citation_count: 8
reference_validation:
  total_references: 52
  verified: 52
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 15
  quotes_valid: 15
  quotes_not_checkable: 1
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Chuvash Polycythemia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Chuvash Polycythemia** covering all of the
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

# Chuvash Polycythemia — Comprehensive Research Report

*Prepared 2026-08-15 for a dismech knowledge-base entry. Every mechanistic and clinical claim below is tied to a PMID; direct abstract quotes are marked with quotation marks so they can be lifted straight into `evidence.snippet` fields. Where I could not verify something, I say so instead of filling the gap.*

---

## 0. The one-paragraph version

Your cells have a little oxygen thermostat. A protein called VHL is the part that says "okay, we have plenty of air, stand down" — it grabs the hypoxia-response transcription factors (HIF-1α, HIF-2α), tags them for the shredder, and the body's emergency oxygen program shuts off. In Chuvash polycythemia, both copies of *VHL* carry one specific typo (R200W), the grip on HIF is a bit slippery, and the thermostat never fully stands down. So the body sits in a permanent, low-grade impression that it's on a mountaintop: erythropoietin runs high, red cells pile up, the pulmonary arteries stay tense, ventilation runs fast. It is the first recognized *congenital disorder of oxygen sensing*. Crucially — and this is the weird, beautiful part — it is a *VHL* disease that **doesn't** cause the tumors *VHL* disease is famous for. What it does cause is clots, and those clots are what kills people.

---

## 1. Disease Information

**Concise overview.** Chuvash polycythemia (CP), increasingly called **Chuvash erythrocytosis (CE)**, is an autosomal recessive congenital secondary erythrocytosis caused by homozygosity for the *VHL* c.598C>T (p.Arg200Trp) allele. It was mapped to 3p25 and the gene identified in 2002 (PMID:12415268; PMID:11987242). It presents with lifelong elevated hemoglobin/hematocrit, inappropriately high or high-normal serum erythropoietin, **normal** hemoglobin–oxygen affinity, and a striking burden of thrombotic and cerebrovascular events — but no increase in the hemangioblastomas, renal cell carcinomas, or pheochromocytomas that define classical VHL syndrome.

Orphanet's definition (ORPHA:238557, retrieved 2026-08-15 via the Orphanet API):

> "Chuvash erythrocytosis is a rare, genetic, congenital secondary polycythemia disorder characterized by increased hemoglobin, hematocrit and erythropoietin serum levels and normal oxygen affinity, which usually manifests with headache, dizziness, dyspnea and/or plethora. Patients present an increased risk of hemorrhage, thrombosis and early death."

**Key identifiers** (all verified live against Monarch, ClinVar, and the Orphanet product1 XML on 2026-08-15):

| Resource | Identifier | Notes |
|---|---|---|
| **MONDO** | `MONDO:0009892` | label "Chuvash polycythemia"; Orphanet asserts an **Exact** mapping to ORPHA:238557 |
| OMIM | `263400` | ERYTHROCYTOSIS, FAMILIAL, 2 (ECYT2) |
| Orphanet | `ORPHA:238557` | preferred term "Chuvash erythrocytosis"; parent = Rare hematologic disease (ORPHA:97992) |
| DOID | `DOID:0060474` | "familial erythrocytosis 2" — this is the term MGI uses for the mouse model |
| ICD-10 | `D75.1` | Orphanet-attributed; relation **NTBT** (the ORPHA concept is *narrower* than D75.1, secondary polycythaemia) |
| ICD-11 | `3A80.0` | Orphanet-attributed index term, also **NTBT** |
| MeSH | `C563918` | supplementary concept record |
| UMLS | `C1837915` | |
| MedGen | `332974` | |
| GARD | `0017176` | |

**Synonyms / alternative names** (Orphanet + MONDO): Chuvash erythrocytosis; VHL-related polycythemia; VHL-related erythrocytosis; Von Hippel-Lindau-related erythrocytosis; Von Hippel-Lindau-dependent polycythemia; erythrocytosis, familial, 2; ECYT2; familial polycythemia caused by mutation in VHL. Older literature uses "Chuvash-type congenital polycythemia."

**Provenance of the evidence base.** This is a disease-level literature knowledge base built almost entirely from **deeply phenotyped cohort studies of individual patients**, not EHR aggregates. The backbone is a single long-running matched-cohort in Chuvashia (Cheboksary) run by Gordeuk, Prchal, Sergueeva, Miasnikova and colleagues from the late 1990s to the 2020s — the same ~30–155 homozygotes and matched wild-type controls reappear across two decades of papers, with a prospective arm registered as **NCT00495638** (PMID:21993671). Add to that the Ischia (Italy) cluster (PMID:16210343), the Oxford physiology group's studies of UK/Irish patients (PMID:16768548; PMID:20616028), and scattered case series from Belfast, Ulm, Chandigarh, and elsewhere. That means: rich mechanistic depth, but small N, one dominant investigator network, and geographic concentration. Curate frequencies with that in mind.

---

## 2. Etiology

### 2.1 Primary cause

A single germline point mutation, in **biallelic** dose. *VHL* NM_000551.4:c.598C>T, p.(Arg200Trp), rs28940298, GRCh38 chr3:10,149,921 C>T (GRCh37 chr3:10,191,605); ClinVar canonical SPDI `NC_000003.12:10149920:C:T`.

Ang et al. 2002 (PMID:12415268) established both the genetic and the mechanistic link:

> "Chuvash polycythemia is an autosomal recessive disorder that is endemic to the mid-Volga River region. We previously mapped the locus associated with Chuvash polycythemia to chromosome 3p25. The gene associated with von Hippel-Lindau syndrome, VHL, maps to this region, and homozygosity with respect to a C-->T missense mutation in VHL, causing an arginine-to-tryptophan change at amino-acid residue 200 (Arg200Trp), was identified in all individuals affected with Chuvash polycythemia."

and

> "Our data indicate that the Arg200Trp substitution impairs the interaction of VHL with HIF1alpha, reducing the rate of degradation of HIF1alpha and resulting in increased expression of downstream target genes including EPO (encoding erythropoietin), SLC2A1 (also known as GLUT1...), TF (encoding transferrin), TFRC (encoding transferrin receptor (p90, CD71)) and VEGF (encoding vascular endothelial growth factor)."

R200W is a **hypomorph**, not a null. That distinction is the whole story of why this disease is not cancer — see §6.

### 2.2 Genetic risk factors

- **Causal genotype:** R200W/R200W. This is the "Chuvash" form proper.
- **Allelic heterogeneity within the same disease concept.** Congenital erythrocytosis also arises from *VHL* compound heterozygosity (R200W plus a second *VHL* allele — e.g. c.562C>G/p.Leu188Val or c.574C>T) and from other homozygous *VHL* alleles such as the Croatian **H191D** (c.571C>G) (PMID:12844285). Pastore et al. concluded: *"up to half of the consecutive patients with apparent congenital polycythemia and increased serum Epo we have examined have mutations of both VHL alleles."* Whether these compound genotypes belong inside `Chuvash_Polycythemia` or as siblings is a lump/split call the curator has to make — Tomasic et al. (PMID:23403324) argue explicitly that **H191D homozygotes are phenotypically distinct** (higher EPO for age; erythroid progenitors *not* EPO-hypersensitive).
- **Cryptic-exon and splicing alleles.** Lenglet et al. 2018 (PMID:29891534) found a new *VHL* cryptic exon **E1′** deep in intron 1, with mutations in E1′ in 7 erythrocytosis families, plus pathogenic *synonymous* exon-2 variants acting via E2 skipping. Practical consequence: a standard coding-exon panel can miss a *VHL*-erythrocytosis diagnosis.
- **Modifier loci with real data.** Shah et al. 2023 (PMID:37435906) found that in *VHL*^R200W homozygotes, the A allele of the *EPO* promoter SNP **rs1617640** "associated with elevated erythropoietin and increased thrombosis risk," whereas the A allele of the *TF* intronic SNP **rs3811647** "associated with higher transferrin and protection from thrombosis in patients." These are the best-documented genetic modifiers in the disease.
- **Digenic coincidence, not modification.** A reported case of coinherited Chuvash polycythemia and G6PD Kerala-Kalyan producing a blended "hemolytic erythrocytosis" phenotype (PMID:33033909) — worth a note, not a mechanism.

### 2.3 Environmental risk / exacerbating factors

There is **no environmental cause**; this is Mendelian. But several exposures modulate the phenotype, and one of them is iatrogenic:

- **Iron deficiency, usually caused by therapeutic phlebotomy.** Low ferritin independently predicted higher tricuspid regurgitation velocity (a pulmonary-pressure surrogate) in 120 homozygotes (PMID:21993671, "low ferritin independently predicted higher tricuspid regurgitation velocity (standardized beta=0.29; P=0.009)"). Iron deficiency also reshapes the transcriptional response — potentiating HIF-1α while suppressing HIF-2α targets (PMID:23993337). So the standard polycythemia reflex (bleed them) may worsen two of the disease's main problems.
- **Hypoxic exposure (altitude, exercise).** The hypoxic EPO response is intact and set on top of an already-elevated baseline (PMID:14726398), and hypoxic ventilatory and pulmonary vasoconstrictive responses are *greatly exaggerated* (PMID:16768548). Altitude and exertion are physiologically meaningful stressors here.
- **Pregnancy** is a documented management challenge (PMID:18161409, a case managed with repeated venesection plus heparin) — thrombotic risk plus a physiologically expanded plasma volume.
- Smoking, obesity, and conventional cardiovascular risk factors are not disease-specific but sit directly on top of a thrombotic diathesis; guideline advice is to optimize them (PMID:34021251).

### 2.4 Protective factors

- **Heterozygote advantage — probably protection from anemia.** Miasnikova et al. 2011 (PMID:21606165): "Mild anemia was present in 15% of VHL(R200W) heterozygotes and 34% of controls without a mutated VHL allele. By multivariate logistic regression, the odds of anemia were reduced an estimated 5.6-fold in the VHL(R200W) heterozygotes compared to controls (95% confidence interval 1.4-22.7; P=0.017)." Perrotta et al. independently found that "nonaffected heterozygotes had increased HIF-1alpha activity, which might confer a biochemical advantage for mutation maintenance" (PMID:16210343). This is the leading explanation for why an ancient, mildly deleterious allele persists at ~6–7% in two separate populations.
- **High transferrin appears protective against thrombosis** — and this genuinely surprised the investigators (PMID:37435906): "Unexpectedly, transferrin elevation associated with reduced rather than increased thrombosis risk."
- **Relative protection from cancer.** No excess malignancy has been demonstrated (PMID:16673284). Transcriptomics offers a candidate reason: down-regulation of cell proliferation and stress-induced apoptosis modules (PMID:23993337). Also lower glucose/HbA1c (PMID:23015148) and lower systemic blood pressures (PMID:14726398) — cardiometabolically favorable traits sitting inside an otherwise dangerous phenotype. Classic antagonistic pleiotropy.

### 2.5 Gene–environment interaction

The cleanest documented GxE in this disease is **genotype × iron status**. Zhang et al. (PMID:23993337) compared PBMC expression in homozygotes with normal iron vs. homozygotes made iron-deficient by phlebotomy: "iron deficiency enhanced the induction effect of VHL(R200W) for 50 genes including hemoglobin synthesis loci but suppressed the effect for 107 genes enriched for HIF-2 targets. This pattern is consistent with potentiation of HIF-1α protein stability by iron deficiency but a trend for down-regulation of HIF-2α translation by iron deficiency overriding an increase in HIF-2α protein stability." Iron isn't just a nutrient here — it's a dial on which arm of the HIF response dominates.

Second: **genotype × hypoxic challenge** (§2.3), where the hypoxic response is preserved in shape but shifted in setpoint.

---

## 3. Phenotypes

### 3.1 HPO annotations already curated for OMIM:263400

Retrieved live from the HPO/Monarch annotation API on 2026-08-15. These are the terms the ontology itself already asserts, with their source and n/N frequencies — safest starting point for the `phenotypes` block.

| HP ID | Label | Frequency (as annotated) | Source |
|---|---|---|---|
| HP:0001900 | Increased circulating hemoglobin concentration | 9/9 | PMID:12844285, PMID:23403324 |
| HP:0001899 | Increased hematocrit | 7/7 | PMID:12844285 |
| HP:0001898 | Increased red blood cell mass | — | OMIM:263400 |
| HP:0033644 | Elevated circulating erythropoietin concentration | 7/9 | PMID:12844285, PMID:23403324 |
| HP:0002641 | Peripheral thrombosis | — | OMIM:263400 |
| HP:0001297 | Stroke | — | OMIM:263400 |
| HP:0001342 | Cerebral hemorrhage | — | OMIM:263400 |
| HP:0002092 | Pulmonary arterial hypertension | 1/1 | PMID:23403324 |
| HP:0002619 | Varicose veins | — | OMIM:263400 |
| HP:0002615 | Hypotension | — | OMIM:263400 |
| HP:0001028 | Hemangioma | — | OMIM:263400 (vertebral hemangiomas) |
| HP:0002315 | Headache | 1/1 | PMID:23403324 |
| HP:0012378 | Fatigue | — | OMIM:263400 |
| HP:0001050 | Plethora | — | OMIM:263400 |
| HP:0001508 | Failure to thrive | 1/1 | PMID:23403324 |
| HP:0011463 | Childhood onset | 7/8 | PMID:12844285, PMID:23403324 |
| HP:0003593 | Infantile onset | 1/1 | PMID:23403324 |
| HP:0003621 | Juvenile onset | 1/7 | PMID:12844285 |
| HP:0000007 | Autosomal recessive inheritance | — | PMID:12844285 |

⚠️ **Frequency caution.** Several of these n/N values (1/1, 7/9) come from tiny case series, one of which (PMID:23403324) is about the **Croatian H191D** genotype, not R200W. Under the dismech frequency-evidence SOP, most of these do **not** support a `FrequencyEnum` band. I would omit `frequency:` for nearly all of them and use the cohort-derived numbers below where a real denominator exists.

### 3.2 Additional phenotypes with cohort-level evidence

These are not in the current HPO annotation set but are supported by the matched-cohort literature. HP IDs below were verified against the dismech validated term cache.

| Feature | HP term | Evidence |
|---|---|---|
| Polycythemia / erythrocytosis (the umbrella finding) | HP:0001901 Polycythemia | PMID:9058724 → correction: PMID:9058738; PMID:12415268 |
| Vertebral hemangioma | HP:0001028 Hemangioma (+ UBERON:0001130 vertebral column) | PMID:14726398 |
| Low-to-normal / reduced systemic blood pressure | HP:0002632 Low-to-normal blood pressure | PMID:14726398; PMID:16769575 ("systolic systemic blood pressures were lower (p=0.001)") |
| Arterial thrombosis | HP:0004420 | PMID:16673284; PMID:37435906 |
| Venous thrombosis / DVT | HP:0004936 / HP:0002625 | PMID:16673284 |
| Thromboembolism, incl. pulmonary embolism | HP:0001907 / HP:0002204 | PMID:39113647 (review of cohort data) |
| Myocardial infarction | HP:0001658 | PMID:39113647 |
| Exercise intolerance | HP:0003546 | PMID:20616028 ("reduced maximum exercise capacities") |
| Exertional dyspnea | HP:0002875 | PMID:16768548 (elevated basal ventilation) |
| Vertigo / dizziness | HP:0002321 | Orphanet definition; PMID:25573974 (36.7% at baseline) |
| Splenomegaly / hepatomegaly (organ enlargement) | HP:0001744 / HP:0002240 | PMID:20140661 — "the volumes of liver, spleen, and kidneys relative to body mass were larger in 30 individuals with Chuvash polycythemia than in 30 matched Chuvash controls" |
| Decreased circulating ferritin (usually iatrogenic) | HP:0012343 | PMID:21993671; PMID:37435906 |
| Hypoglycemia-adjacent: lower glucose and HbA1c | HP:0001943 Hypoglycemia (use cautiously — the finding is *lower*, not frankly hypoglycemic) | PMID:23015148 |
| Major bleeding episodes | (no clean HP term; consider HP:0001892 Abnormal bleeding) | PMID:16673284 |

### 3.3 Laboratory phenotype (the diagnostic signature)

- **Hemoglobin markedly elevated from early life.** Sergeyeva et al. 1997 (PMID:9058738), studying six Chuvash patients under 20 years old: *"Hemoglobins were markedly elevated in the index subjects (mean +/- standard deviation [SD] of 22.6 +/- 1.4 g/dL), while platelet and white blood cell counts were normal."* That last clause is the key discriminator from polycythemia vera — **no leukocytosis, no thrombocytosis**. Cohort analyses actually report *lower* WBC and platelet counts than controls (PMID:16673284).
- **Erythropoietin inappropriately high, but hypoxic regulation intact.** Gordeuk et al. 2004 (PMID:14726398): *"Although hemoglobin-adjusted serum erythropoietin concentrations were approximately 10-fold higher in VHL 598C>T homozygotes than in controls, erythropoietin response to hypoxia was identical."* Note EPO can also be within the normal range — 4 of 9 in Percy's series had normal EPO (PMID:12702509), and in the Indian screening series EPO was low in 19% and normal in 69% of erythrocytosis cases (PMID:37362405). **A normal EPO does not exclude the diagnosis.**
- **Normal p50 / normal hemoglobin–oxygen affinity, normal 2,3-BPG.** This was established before the gene was known (PMID:9058738).
- Elevated serum **VEGF**, **endothelin-1**, **PAI-1** (PMID:14726398; PMID:16769575; PMID:16673284).
- Suppressed **hepcidin**: 8.1 (6.3–10.5) ng/mL in homozygotes vs 26.9 (18.6–38.0) ng/mL in controls after adjustment for EPO and ferritin, P<.001 (PMID:21876117).
- Elevated **transferrin**, reduced **ferritin** (PMID:37435906).
- Elevated **homocysteine, glutathione, γ-glutamyltransferase, cysteinylglycine**; reduced cysteine (PMID:18223282).
- Broadly elevated Th1 **and** Th2 cytokines with preserved ratio; lower CD4 counts and CD4/CD8 ratio (PMID:19062180).
- Lower random glucose and HbA1c; higher serum glycerol and citrate on metabolomics (PMID:23015148).

### 3.4 Onset, severity, course

- **Onset is congenital/lifelong** — elevated hematocrit is often documented from birth or infancy (PMID:39113647 case: "Her elevated hematocrit had been known since birth"). HPO annotates childhood onset 7/8.
- **Severity is variable**, even within the same genotype. The belzutifan case report notes: "in two patients with the same VHL R200W/L188V genotype as our patient, Hb levels ranged from 16.3 g/dL to 21.0 g/dL. This variability highlights the..." (PMID:39113647).
- **Course: chronic, lifelong, non-remitting**, punctuated by discrete vascular events. Not episodic in the seizure/attack sense — the hematologic phenotype is stable-to-slowly-worsening while the clinical risk is event-driven.

### 3.5 Quality-of-life impact

There are no published EQ-5D/SF-36/PROMIS data specific to CP that I could find — flag this as a genuine gap. What exists is symptom-burden reporting: in the pediatric/adolescent longitudinal letter (PMID:25573974, read via the PMC rendering), baseline symptoms in affected subjects were headache ~73%, leg pain ~50%, vertigo/dizziness ~37%, versus much lower rates in controls, and at follow-up "over half of the subjects continue to suffer from previously reported Chuvash polycythemia symptoms: chronic headache, fatigue, and/or lower extremity pain." Because these numbers were extracted from a rendered page rather than a cached abstract, **verify against the source PDF before using them as evidence snippets.**

The Formenti exercise study (PMID:20616028) gives an objective functional correlate: reduced maximum exercise capacity with early muscle acidosis. That's the physiological substrate of "I get tired fast."

---

## 4. Genetic / Molecular Information

### 4.1 Causal gene

**VHL** — von Hippel-Lindau tumor suppressor. HGNC: `hgnc:12687` (verified). Chromosome 3p25.3. UniProt P40337 (pVHL30 / pVHL19 isoforms). OMIM gene entry 608537.

### 4.2 The pathogenic variant

| Field | Value |
|---|---|
| HGVS (coding) | NM_000551.4:c.598C>T |
| HGVS (protein) | p.Arg200Trp (R200W) |
| dbSNP | rs28940298 |
| GRCh38 | chr3:10,149,921 C>T |
| GRCh37 | chr3:10,191,605 C>T |
| Variant type | single-nucleotide, **missense** |
| Origin | **germline** (never somatic in this disease) |
| Zygosity required | **homozygous** (or compound het with a second *VHL* allele) |
| Functional consequence | **partial loss of function / hypomorph** — reduced HIF-α binding and degradation, *not* abolished |

**ClinVar (VCV 2232, retrieved 2026-08-15):** germline classification is **"Conflicting classifications of pathogenicity"**, review status "criteria provided, conflicting classifications", last evaluated 2026-02-03. The conflict is *interpretive, not evidentiary*: the same allele is submitted against multiple conditions — Chuvash polycythemia (MONDO:0009892 / OMIM:263400), von Hippel-Lindau syndrome (OMIM:193300), and "Inherited phaeochromocytoma and paraganglioma excluding NF1." It is unambiguously pathogenic *for Chuvash polycythemia in the homozygous state*; it is **not** established as a heterozygous VHL-tumor-syndrome allele. Do not curate the ClinVar aggregate as "conflicting = uncertain" without that qualifier.

**Population frequency (gnomAD v4, queried live 2026-08-15):**

| Dataset | AC | AN | AF | Homozygotes |
|---|---|---|---|---|
| Exomes, global | 351 | 1,461,844 | **2.40 × 10⁻⁴** | 1 |
| — South Asian | 53 | 86,248 | 6.15 × 10⁻⁴ | **1** |
| — Non-Finnish European | 287 | 1,111,994 | 2.58 × 10⁻⁴ | 0 |
| — Finnish | 2 | 53,408 | 3.74 × 10⁻⁵ | 0 |
| — African/African-American | 1 | 33,480 | 2.99 × 10⁻⁵ | 0 |
| Genomes, global | 13 | 152,176 | 8.54 × 10⁻⁵ | 0 |

Note the mismatch between gnomAD's global ~0.024% and the **0.057 (Chuvashia) / 0.070 (Ischia)** allele frequencies in the endemic clusters (PMID:16210343) — a ~250-fold enrichment. gnomAD simply doesn't sample Chuvashia or Ischia. The single South Asian homozygote in gnomAD is consistent with the well-documented Bangladeshi/Pakistani/north Indian burden (PMID:12702509; PMID:37362405).

### 4.3 Other *VHL* alleles causing erythrocytosis

- **H191D** (c.571C>G), homozygous, Croatian founder (~6 generations back) — phenotypically distinct from R200W (PMID:12844285; PMID:23403324).
- **L188V** (c.562C>G) and c.574C>T, seen as the second allele in compound heterozygotes with R200W (PMID:12844285; PMID:39113647).
- **S179P** homozygous, reported in a Hungarian patient via WES and classified likely pathogenic by ACMG (PMID:40130200).
- **G311T** in exon 1, heterozygous, novel (PMID:15642664).
- **Cryptic exon E1′ variants** and **synonymous exon-2 splice-altering variants** (PMID:29891534) — genotype–phenotype correlation there tracked with the degree of splicing disruption: "In all the studied cases, the mutations differentially affected splicing, correlating with phenotype severity."

### 4.4 Modifier genes

Established: *EPO* promoter rs1617640 (risk) and *TF* rs3811647 (protective), both PMID:37435906. HGNC: *TF* = `hgnc:11740` (verified). Downstream candidates without direct CP modifier evidence but mechanistically implicated: *EPAS1*/HIF2A (`hgnc:3374`), *HIF1A*, *IRP1/ACO1*, *SOCS1*, *JAK2* (`hgnc:6192`).

### 4.5 Epigenetics and chromosomal abnormalities

**Not applicable / no data.** I found no methylation, histone-modification, or chromatin studies specific to Chuvash polycythemia, and no chromosomal abnormalities — this is a point mutation in a structurally normal genome. Somatic second-hit *VHL* loss (the mechanism of VHL-syndrome tumors) is specifically **not** part of CP pathogenesis, which is the point of §6.4.

---

## 5. Environmental Information

- **Environmental factors:** none causal. See §2.3 for modifiers (iron status, altitude/hypoxia, pregnancy).
- **Lifestyle factors:** no CP-specific data. General cardiovascular risk optimization is advised on first principles (PMID:34021251), and smoking is a particularly poor idea in someone whose baseline problem is a false hypoxia signal plus a thrombotic diathesis — but I can find no study testing this.
- **Infectious agents:** not applicable.
- Possible ECTO-style exposure terms if the entry needs them: exposure to high altitude / hypobaric hypoxia (modifier, `EXACERBATES`), and — unusually — a *therapeutic* exposure, repeated phlebotomy-induced iron depletion, which the evidence suggests is `EXACERBATES` for pulmonary pressure and possibly thrombosis rather than protective. That last one is worth modeling explicitly; it's the most clinically consequential "environmental" input in the disease and it comes from a doctor.

---

## 6. Mechanism / Pathophysiology

This is the section where the disease earns its reputation. The causal chain, upstream → downstream:

### 6.1 The canonical chain

**Node 1 (MOLECULAR) — Impaired pVHL–HIF-α binding.**
pVHL is the substrate-recognition subunit of a Cullin-2 RING E3 ubiquitin ligase (the VCB-CR complex: VHL–Elongin B–Elongin C–Cul2–Rbx1). Under normoxia, prolyl hydroxylases (EGLN1/PHD2 et al.) hydroxylate conserved prolines in HIF-1α/HIF-2α; pVHL binds the hydroxyproline and marks HIF-α for polyubiquitination and proteasomal destruction. R200W sits in the elongin-binding/β-domain region and **weakens, but does not abolish**, that interaction (PMID:12415268).
GO: `GO:0016567` protein ubiquitination; `GO:0043161` proteasome-mediated ubiquitin-dependent protein catabolic process; `GO:0004842` ubiquitin-protein transferase activity; `GO:0061630` ubiquitin protein ligase activity. Modifier: `LOSS_OF_FUNCTION` (qualitative — the E3 recognition step escapes normal oxygen-dependent control), or `DECREASED` if you prefer the quantitative reading.

**Node 2 (MOLECULAR/CELLULAR) — Normoxic HIF-α stabilization ("pseudohypoxia").**
HIF-1α and HIF-2α accumulate and dimerize with HIF-1β/ARNT at normal pO₂. The cell believes it is short of oxygen while sitting in ordinary room air.
GO: `GO:0001666` response to hypoxia; `GO:0071456` cellular response to hypoxia; `GO:0097411` hypoxia-inducible factor-1alpha signaling pathway; `GO:0070482` response to oxygen levels. Modifier: `GAIN_OF_FUNCTION` — this is genuinely qualitative (the pathway is no longer under its normal oxygen-dependent regulatory constraint), which is exactly the case where the dismech guidance says GOF beats INCREASED.

**Node 3 (MOLECULAR) — HIF target gene program activation.**
"increased expression of downstream target genes including EPO..., SLC2A1..., TF..., TFRC... and VEGF" (PMID:12415268). Add ET-1/*EDN1* (PMID:16769575), *CXCL12* (PMID:33512384), and PDK/PFK/PKM glycolytic enzymes (PMID:20616028).

**Node 4 (TISSUE/ORGANISM) — Erythropoietin excess → erythroid expansion.**
Renal (and hepatic) EPO output rises; erythroid progenitors expand. Two additional wrinkles:
 - **EPO hypersensitivity of erythroid progenitors** is reported for R200W but explicitly *not* for H191D (PMID:23403324) — an important asymmetry.
 - **Splenic erythropoiesis** contributes substantially, at least in mouse: "we observed a striking phenotype in Vhl(R/R) spleens, with greater numbers of erythroid progenitors and megakaryocytes and increased erythroid differentiation of Vhl(R/R) splenic cells in vitro" (PMID:17992257).
GO: `GO:0030218` erythrocyte differentiation; `GO:0030097` hemopoiesis. CL: `CL:0000038` erythroid progenitor cell; `CL:0000765` erythroblast; `CL:0000232` erythrocyte; `CL:0000037` hematopoietic stem cell; EPO source: `CL:1000692` kidney interstitial fibroblast. UBERON: `UBERON:0002371` bone marrow; `UBERON:0002106` spleen; `UBERON:0002113` kidney.

**Node 5a (ORGANISM) — Erythrocytosis and hyperviscosity.** Headache, fatigue, plethora, dizziness.

**Node 5b (TISSUE) — Pulmonary vascular tone and remodeling → pulmonary hypertension.**
Human: elevated basal pulmonary vascular tone and greatly increased hypoxic pulmonary vasoconstriction (PMID:16768548); 36% with sPAP ≥35 mmHg (PMID:16769575); elevated tricuspid regurgitation velocity independent of blood-volume surrogates (PMID:21993671). Mouse: PH develops **independently of polycythemia**, with vascular remodeling, hemorrhage, edema, macrophage infiltration, and later fibrosis, all HIF-2α-dependent (PMID:20197624).
GO: `GO:0042310` vasoconstriction; `GO:0045907` positive regulation of vasoconstriction; `GO:0001525` angiogenesis. CL: `CL:0002591` smooth muscle cell of the pulmonary artery; `CL:1001568` pulmonary artery endothelial cell. UBERON: `UBERON:0002012` pulmonary artery; `UBERON:0002048` lung.
**This node is a strong `conforms_to` candidate for `pulmonary_vascular_remodeling#Obstructive Pulmonary Vascular Remodeling`.**

**Node 5c (ORGANISM) — Prothrombotic state → arterial and venous thrombosis, stroke.**
The terminal, lethal branch. Elevated PAI-1, altered thrombospondin-1 (PMID:28104701), elevated VEGF and ET-1, and endothelial activation. Critically, **hematocrit is not the driver** (see §6.3).
GO: `GO:0007596` blood coagulation; `GO:0030194` positive regulation of blood coagulation; `GO:0070527` platelet aggregation. Candidate `conforms_to`: `thrombogenesis#Coagulation Cascade Activation and Thrombin-Driven Fibrin Formation`.

**Node 5d (ORGANISM) — Iron/hepcidin axis.** Hepcidin suppression (PMID:21876117) independent of EPO and RBC count, plus transferrin/TfR induction, gives a HIF-driven iron-mobilization program layered on top of phlebotomy-induced depletion.

**Node 5e (ORGANISM) — Metabolic reprogramming.** Increased glycolysis and lactate, reduced hepatic gluconeogenesis, lower glucose and HbA1c (PMID:23015148); in exercising humans "early and marked phosphocreatine depletion and acidosis in skeletal muscle, greater accumulation of lactate in blood, and reduced maximum exercise capacities" with elevated muscle *PDK*, *PFK*, *PKM* transcripts (PMID:20616028). Mouse hearts show 1.8-fold higher glycolytic flux and 1.5-fold higher lactate efflux (PMID:27422990).
GO: `GO:0006096` glycolytic process; `GO:0006094` gluconeogenesis.

**Node 5f (TISSUE) — Increased solid organ size.** Liver, spleen, kidney volumes larger than matched controls; proposed to run through HIF-2α ↑ / p21^Cip1 ↓ → hepatocyte proliferation (PMID:20140661).

### 6.2 The HIF-1α vs HIF-2α question — resolve this correctly

The 2002 discovery paper framed everything around **HIF-1α** (PMID:12415268), and much early literature followed. The mouse genetics say otherwise: "heterozygosity for Hif2a, but not Hif1a, genetically suppressed both the polycythemia and pulmonary hypertension in the VhlR/R mice" (PMID:20197624), and HIF-2α drives the splenic erythropoiesis phenotype (PMID:17992257). Human patients have **both** isoforms elevated (PMID:21876117 states "elevated hypoxia-inducible factor 1α (HIF-1α) and HIF-2α levels"). Curate this as: both accumulate; **HIF-2α is the dominant effector** for the erythroid and pulmonary-vascular phenotypes; HIF-1α contributes to the metabolic arm. The therapeutic data (§12) independently confirm the HIF-2α dominance.

### 6.3 The hematocrit heresy — the single most important clinical mechanism claim

Everyone's intuition is "high hematocrit → viscous blood → clots." In Chuvash erythrocytosis that intuition is **wrong**, and this is now well supported:

- Gordeuk et al. 2020 letter title says it flat out: *"Thrombotic risk in congenital erythrocytosis due to up-regulated hypoxia sensing is not associated with elevated hematocrit"* (PMID:31289208).
- The companion review (PMID:30872370) states: "We review studies indicating that the occurrence of thrombosis in Chuvash erythrocytosis is independent of hematocrit, that the thrombotic risk is paradoxically increased by phlebotomy in Chuvash erythrocytosis..."
- Prospectively, over 11 years in 155 patients vs 154 controls: "risk of thrombosis increased 8.9-fold in patients versus controls. **Erythropoietin elevation, but not hematocrit or ferritin, correlated with thrombosis risk**" (PMID:37435906).

So the causal edge is **HIF/EPO signaling → prothrombotic state**, with erythrocytosis as a *parallel* consequence rather than the intermediate. Model it that way. This has direct treatment implications (§12).

### 6.4 Why no tumors? (the mechanism-of-absence)

Three converging explanations, all worth curating as an explicit "absent phenotype with a mechanism":

1. **Dose.** R200W is a hypomorph retaining substantial pVHL function; classical VHL tumors need biallelic inactivation with much deeper loss (PMID:12415268; the Blood 2014 abstract by Lenglet-adjacent workers describes "a gradual dysregulation of the hypoxia pathway in oncogenesis" with severity correlating to the gradient of pVHL dysfunction).
2. **HIF is not sufficient.** Gordeuk 2004 (PMID:14726398): "Spinocerebellar hemangioblastomas, renal carcinomas, and pheochromocytomas typical of classical VHL syndrome were not found, suggesting that overexpression of HIF-1alpha and VEGF is not sufficient for tumorigenesis."
3. **A HIF-independent pVHL function is preserved.** Li et al. 2022 (PMID:35760869) found pVHL stabilizes hydroxylated TFAM to sustain mitochondrial biogenesis, and: "Tumorigenic VHL variants leading to different clinical manifestations fail to bind hydroxylated TFAM. In contrast, cells harbouring the Chuvash polycythaemia VHLR200W mutation, involved in hypoxia-sensing disorders without tumour development, are capable of binding hydroxylated TFAM." That is a beautifully clean molecular dissociation between the erythrocytosis arm and the oncogenic arm.

### 6.5 A contested alternative mechanism — curate as a competing hypothesis, not settled fact

Russell et al. 2011 (PMID:21685897) proposed that pVHL heterodimerizes with SOCS1 to form an E3 ligase degrading **phospho-JAK2**, and that CP mutants fail to do so — explaining EPO hypersensitivity through JAK2 rather than (only) HIF: "Systemic administration of a highly selective JAK2 inhibitor, TG101209, reversed the disease phenotype in Vhl(R200W/R200W) knock-in mice."

But Tomasic et al. 2013 (PMID:23403324) push back with human data: H191D homozygotes' "native erythroid progenitors, unlike Chuvash R200W, are not hypersensitive to erythropoietin. **This observation contrasts with a report suggesting that polycythemia in VHL R200W and H191D homozygotes is due to the loss of JAK2 regulation from VHL R200W and H191D binding to SOCS1.**"

Recommended curation: `mechanistic_hypotheses` with `canonical_hif_stabilization` (CANONICAL) and `vhl_socs1_jak2_dysregulation` (ALTERNATIVE), with the contradicting human progenitor data attached. The single successful ruxolitinib case (§12) is *consistent* with the JAK2 hypothesis but doesn't settle it — JAK2 inhibition would blunt EPO signaling regardless of why EPO signaling is high.

### 6.6 Molecular profiling data

- **Transcriptomics (human PBMCs):** 812 up, 2120 down at FDR 0.05 in 8 homozygotes vs 17 wild-type; three modules — "induction of innate immune responses, alteration of carbohydrate and lipid metabolism, and down-regulation of cell proliferation, stress-induced apoptosis and T-cell activation" (PMID:23993337). Search GEO for the accompanying accession before curating a `datasets:` record — I did not verify one, and per the dismech dataset SOP an unverified accession must not be written.
- **Metabolomics (serum):** higher glycerol and citrate in homozygotes (PMID:23015148).
- **Proteomics:** no dedicated CP proteomics study found. Gap.
- **Single-cell / spatial:** none found. Gap.
- **Structural biology:** the VCB complex structures (PDB 1LM8, 1LQB) define the HIF-hydroxyproline binding pocket; note I did not re-verify these PDB IDs in this session, so confirm before curating.

---

## 7. Anatomical Structures Affected

**Primary (where the lesion does its first work):**
- Kidney — `UBERON:0002113` — dysregulated EPO production; cell type `CL:1000692` kidney interstitial fibroblast.
- Bone marrow — `UBERON:0002371` — erythroid hyperplasia.
- Spleen — `UBERON:0002106` — extramedullary/splenic erythropoiesis (strongly shown in mouse, PMID:17992257) and increased volume in humans (PMID:20140661).
- Blood — `UBERON:0000178`, `UBERON:0001969` blood plasma, `UBERON:0001977` blood serum.

**Secondary / complication sites:**
- Pulmonary vasculature — `UBERON:0002012` pulmonary artery, `UBERON:0002048` lung. Cells: `CL:0002591`, `CL:1001568`. Mouse lungs additionally show fibrosis and macrophage infiltration (`CL:0000235`) (PMID:20197624).
- Cerebral arteries and brain — `UBERON:0004449` cerebral artery, `UBERON:0000955` brain — stroke and cerebral hemorrhage.
- Systemic veins — `UBERON:0001638` vein, `UBERON:0035552` deep vein — varicose veins and DVT.
- Vertebral column — `UBERON:0001130` — vertebral hemangiomas (PMID:14726398).
- Liver — `UBERON:0002107` — increased volume; altered gluconeogenesis (`CL:0000182` hepatocyte).
- Skeletal muscle — early acidosis and PCr depletion on exercise (PMID:20616028).
- Heart — altered substrate/high-energy phosphate metabolism, RV hypertrophy in mouse (PMID:27422990).

**Subcellular (GO CC):** cytosol (HIF-α accumulation), nucleus (HIF-α/ARNT transcriptional complex), proteasome complex `GO:0000502`, Cul2-RING ubiquitin ligase complex, and — per PMID:35760869 — mitochondrion (TFAM stabilization; preserved in R200W).

**Lateralization:** not applicable. Systemic and bilateral; vascular events are focal and stochastic.

---

## 8. Temporal Development

- **Onset:** congenital. Erythrocytosis is present from birth or infancy; formal diagnosis often in childhood or adolescence, sometimes not until adulthood when an incidental CBC or a first thrombosis prompts workup. HPO: childhood onset 7/8, infantile onset 1/1, juvenile onset 1/7.
- **Onset pattern:** insidious and chronic — there is no acute onset event.
- **Progression:** slow/stable hematologically; **event-driven** clinically. Vascular events accumulate with age. Pulmonary artery pressure appears to be a progressive, modifiable-by-iron-status variable (PMID:21993671).
- **Course:** lifelong, no spontaneous remission. Not relapsing-remitting.
- **Complications begin early.** In 30 children and adolescents followed a median of 8 years, 9 (31%) developed complications versus zero of 16 controls, including a thromboembolic death at age 17 (PMID:25573974 — numbers read from the PMC rendering; **verify against source before curating as snippets**). This matters: the window for intervention opens in childhood, not middle age.
- **Critical periods:** puberty onward (symptom escalation and start of phlebotomy in many patients), pregnancy (PMID:18161409), and any period of iron depletion.

---

## 9. Inheritance and Population

### 9.1 Epidemiology

- **Orphanet's own position (retrieved 2026-08-15 from `en_product9_prev.xml`): worldwide point prevalence class = "Unknown", validation status "Not yet validated."** No numeric estimate. Curate `prevalence_class: UNKNOWN` for worldwide rather than inventing a number.
- **Endemic-cluster allele frequencies** are the solid numbers (PMID:16210343): Ischia **0.070**, Chuvashia **0.057**. Under Hardy-Weinberg those imply homozygote frequencies of ~0.49% and ~0.32% respectively (~490 and ~320 per 100,000) — but treat this as *derived arithmetic*, not a published prevalence, and label it as such if you record it.
- Sergeyeva 1997 (PMID:9058738) qualitatively: "Hundreds of individuals appear to be affected in an autosomal recessive pattern... This condition is the only endemic form of familial and congenital polycythemia described."
- **Incidence:** no published incidence figure found.
- **Share of congenital erythrocytosis caseload:** up to half of consecutive congenital-polycythemia-with-high-EPO patients had biallelic *VHL* mutations in one series (PMID:12844285). In north India a prior report put Chuvash polycythemia at **61%** of inherited erythrocytosis; a 2023 PGIMER prospective screen found a lower **8%** (3/38) among JAK2-negative unexplained erythrocytosis patients and 0/61 among high-Hb blood donors (PMID:37362405). Big spread — ascertainment-dependent.

### 9.2 Genetics of inheritance

- **Pattern:** autosomal recessive (HP:0000007). Heterozygotes are clinically unaffected but not biologically silent (§2.4).
- **Penetrance:** appears essentially complete for the *hematologic* phenotype in homozygotes; **incomplete and variable for complications** — 31% of children/adolescents had complications over 8 years (PMID:25573974), 36% of adults had mild PH (PMID:16769575).
- **Expressivity:** variable, even within genotype (PMID:39113647).
- **Anticipation:** not applicable (no repeat expansion).
- **Germline mosaicism:** not reported.
- **Founder effect:** yes, and a striking one. Gordeuk 2004 (PMID:14726398): "Although endemic to the Chuvash population of Russia, this mutation occurs worldwide and originates from a single ancient event." Perrotta 2006 confirmed the Ischian cluster shares the Chuvash haplotype: "The haplotype of all patients matched that identified in the Chuvash cluster, thereby supporting the single-founder hypothesis." **But not exclusively single-origin** — Cario et al. (PMID:15642664) found "One patient of Turkish origin with homozygous Chuvash-type mutation had a haplotype not previously found in individuals with Chuvash-type mutation," concluding "this mutation was not spread only from a single founder but developed independently in other individuals." Curate both.
- **Consanguinity:** not specifically studied; expected to matter for a recessive disease outside endemic regions.
- **Carrier frequency:** ~11% in Chuvashia and ~14% on Ischia by HW from the allele frequencies above; ~0.05% globally by gnomAD exomes. Verify the derivation is labeled as such.

### 9.3 Population demographics

- **Ethnic/geographic clusters:** Chuvash Republic, mid-Volga, Russian Federation (PMID:9058738; PMID:11987242); island of **Ischia**, Bay of Naples, Italy (PMID:16210343 — 14 affected subjects in 5 families, 12 on Ischia); **Bangladeshi and Pakistani** ancestry (8 homozygotes among 78 erythrocytosis patients screened in Northern Ireland, PMID:12702509); **north Indian** (PMID:37362405); scattered cases of Danish, American, English, Turkish, German ancestry (PMID:12844285; PMID:15642664); a recent Turkish report (PMID:41930727).
- **Sex ratio:** no sex bias reported; autosomal recessive. gnomAD carrier counts are near-balanced across XX/XY.
- **Age distribution:** all ages; the disease is congenital, and the mortality burden falls disproportionately on adults through cerebrovascular and thrombotic events, but pediatric deaths occur (PMID:25573974).

---

## 10. Diagnostics

### 10.1 The workup, in order

1. **Confirm true erythrocytosis** (persistently elevated Hb/Hct; red cell mass measurement is largely unavailable now — PMID:30872370).
2. **Exclude polycythemia vera:** *JAK2* V617F (and exon 12) negative; and note the discriminating CBC pattern — in CP, "platelet and white blood cell counts were normal" (PMID:9058738), indeed often *lower* than controls (PMID:16673284), versus the trilineage expansion of PV.
3. **Exclude acquired secondary causes:** cardiopulmonary disease, high-altitude residence, sleep apnea, renal artery stenosis, EPO-secreting tumor, testosterone/ESA use (PMID:34021251).
4. **Serum erythropoietin** — high or inappropriately normal for the hematocrit. Low EPO points to *EPOR* instead. **Do not use a normal EPO to exclude CP** (PMID:12702509; PMID:37362405).
5. **p50 / oxygen dissociation curve** — normal in CP; abnormal in high-affinity hemoglobinopathies and *BPGM* deficiency (PMID:9058738).
6. **Genetic confirmation.**

### 10.2 Genetic testing

- **Targeted single-variant testing** is efficient where the allele is common. Duggal et al. validated **PCR-RFLP for VHL c.598C>T** as a cheap first-line screen: "the relatively simpler PCR-RFLP for VHL:c.598C > T mutation may be considered for the initial genetic screening of unexplained, suspected congenital erythrocytosis in regions where Chuvash polycythemia comprises a large proportion of inherited erythrocytosis, after polycythemia vera and common acquired secondary causes are excluded" (PMID:37362405).
- **Congenital erythrocytosis gene panel** — should include *VHL*, *EPAS1*/HIF2A, *EGLN1*/PHD2, *EPOR*, *HBB*, *HBA1/2*, *BPGM* (PMID:34021251).
- **WES/WGS** for unexplained cases — has yielded rare *VHL* genotypes (e.g. S179P homozygous, PMID:40130200), with the authors recommending "the utilization of high-throughput genomic testing in cases with unexplained polyglobulia."
- ⚠️ **Coverage caveat:** a coding-exon-only assay can miss the intron-1 **cryptic exon E1′** variants and the splice-altering synonymous exon-2 variants (PMID:29891534). If clinical suspicion is high and coding *VHL* is clean, that's the next place to look.
- CMA, karyotype, FISH, mtDNA testing, and repeat-expansion testing: **not applicable.**

### 10.3 Other testing

- **Echocardiography** for pulmonary hypertension screening — tricuspid regurgitation velocity, with the caveat that TRV is influenced by blood volume and iron status; the CP cohort study adjusted for LV diastolic and LA diameters and the elevation persisted (PMID:21993671).
- **Iron studies** (ferritin, transferrin, TIBC) — both to monitor phlebotomy-induced deficiency and because transferrin is prognostically informative (PMID:37435906).
- **VHL tumor surveillance:** classical VHL surveillance (abdominal/CNS/spine MRI, audiometry, ophthalmologic exam, metanephrines) has been performed in reported cases and was "unrevealing" (PMID:39113647). Since no excess tumor risk is demonstrated (PMID:16673284), routine lifelong VHL-syndrome surveillance is **not** standard for R200W homozygotes — but is reasonable in compound heterozygotes carrying a second allele of uncertain tumor risk. This is a real clinical judgment call worth recording in the entry.
- **Biopsy/histopathology:** no diagnostic biopsy role. Mouse lung histology shows vascular remodeling, hemorrhage, edema, macrophage infiltration, and fibrosis (PMID:20197624).

### 10.4 Differential diagnosis

| Condition | Distinguishing features |
|---|---|
| Polycythemia vera | *JAK2* mutation; **low** EPO; trilineage expansion (leukocytosis, thrombocytosis); splenomegaly; acquired, adult-onset |
| *EPOR* truncation erythrocytosis | **Low/subnormal** EPO; autosomal dominant |
| *EGLN1*/PHD2 erythrocytosis | Normal-to-high EPO; AD; no PH signature |
| *EPAS1*/HIF2A gain-of-function | AD; associated with paraganglioma/somatostatinoma in the mosaic Pacak-Zhuang form; belzutifan-responsive (PMID:34818480; PMID:40879399) |
| High-oxygen-affinity hemoglobin | **Left-shifted p50** |
| *BPGM* (2,3-BPG) deficiency | Abnormal p50; reduced 2,3-BPG |
| Croatian *VHL* H191D homozygous erythrocytosis | Higher EPO for age; erythroid progenitors **not** EPO-hypersensitive (PMID:23403324) |
| Secondary erythrocytosis (hypoxic, tumoral, drug-induced) | Acquired; identifiable cause |
| Classical VHL syndrome | Heterozygous *VHL*, autosomal dominant, tumor-predominant; erythrocytosis uncommon |

### 10.5 Screening

- **Cascade family testing** after a proband — straightforward for a known single variant; identifies affected sibs (recessive: 25% risk) and carriers.
- **Population/newborn screening:** not established anywhere. A regional screening program in Chuvashia or Ischia is plausible on paper (high allele frequency, cheap PCR-RFLP assay, complications starting in childhood) but I found no published program — flag as a gap and a potential `KNOWLEDGE_GAP` discussion.
- **Blood-donor screening was tested and was negative**: 0/61 volunteer donors deferred for unexplained high hemoglobin carried the mutation (PMID:37362405). Useful negative result.

---

## 11. Outcome / Prognosis

**The honest state of the evidence:** there is no dedicated survival study with a published median. What exists is repeated, consistent cohort language about **premature mortality**, plus one strong prospective hazard estimate.

- Gordeuk 2004 (PMID:14726398): VHL 598C>T homozygosity was associated with "...**premature mortality related to cerebral vascular events and peripheral thrombosis**."
- Gordeuk & Prchal 2006 (PMID:16673284): "These studies have also shown associations with arterial and venous thrombosis, major bleeding episodes, cerebral vascular events, and premature mortality."
- Orphanet: "Patients present an increased risk of hemorrhage, thrombosis and early death."
- **Best quantitative outcome figure:** over ~11 years of prospective follow-up of 155 patients vs 154 matched controls, "risk of thrombosis increased **8.9-fold** in patients versus controls" (PMID:37435906).
- Pediatric: 31% complication rate over a median 8 years in 30 children/adolescents including a death at 17 (PMID:25573974, verify).

**Prognostic factors:**
- **Elevated erythropoietin** predicts thrombosis; **hematocrit and ferritin do not** (PMID:37435906). This is the headline prognostic finding of the last decade.
- **Elevated transferrin** is protective (PMID:37435906).
- *EPO* rs1617640 A allele → higher risk; *TF* rs3811647 A allele → lower risk (PMID:37435906).
- Low ferritin → higher estimated pulmonary artery pressure (PMID:21993671).
- **Phlebotomy** is associated with increased thrombotic risk (PMID:30872370) — a prognostic factor that is also a treatment, which is uncomfortable and important.

**Morbidity:** chronic headache, fatigue, lower-extremity pain in over half of long-followed patients; reduced exercise capacity; pulmonary hypertension in ~a third; varicose veins; stroke sequelae. **Malignancy risk is not increased** (PMID:16673284).

**Quality-of-life instruments:** none published. Gap.

---

## 12. Treatment

⚠️ **Frame the whole section with this:** there are **no randomized trials** in Chuvash polycythemia. Everything below is cohort inference, expert opinion, mouse data, or single cases. Gordeuk & Prchal (PMID:16673284) put it plainly: "Retrospective analyses among patients with Chuvash polycythemia have not shown benefit for therapy with phlebotomy or aspirin, but these and other modes of therapy should be studied prospectively."

### 12.1 Phlebotomy — the contested standard of care

`treatment_term`: NCIT:C28221 Phlebotomy (verified). `therapeutic_modality`: OTHER or PROCEDURE-adjacent — it's not cleanly any of the enum values; consider `OTHER` with a note.

- **What it does:** reduces hematocrit and relieves hyperviscosity symptoms (PMID:37435906: "Phlebotomies reduce hematocrit and hyperviscosity symptoms").
- **What it also does:** causes iron deficiency, which raises pulmonary artery pressure (PMID:21993671) and may further elevate HIF activity; and phlebotomy is associated with *increased* thrombotic risk (PMID:30872370).
- **Current expert position (PMID:34021251):** "In general, cytoreductive therapy should be avoided and phlebotomy is seldom warranted where frequency is determined by **symptom control rather than Hct threshold**."
- The Hungarian case-report authors make the same point from the clinic: the PV rule of thumb (keep Hct <0.45) "needs to be re-evaluated" in genetically determined secondary polyglobulias (PMID:40130200).

**Curation guidance:** model this as a treatment with `treatment_effect` that is genuinely mixed, and attach the harm evidence as its own items rather than burying it in prose. The `INHIBITS` edge from phlebotomy goes to the erythrocytosis node, *not* to the thrombosis node — and there is an additional `EXACERBATES`-flavored edge from phlebotomy-induced iron deficiency back onto the pulmonary-pressure node. That inverted-arrow structure is the clinically important thing this entry should capture.

### 12.2 Low-dose aspirin

`treatment_term`: NCIT:C15986 Pharmacotherapy; `therapeutic_agent`: CHEBI:15365 acetylsalicylic acid (verified); `therapeutic_modality`: SMALL_MOLECULE.
Widely advised, not demonstrated to help in CP specifically. "Although not supported by hard evidence, cardiovascular risk optimization and low-dose aspirin use are often advised" (PMID:34021251); retrospective analyses showed no benefit (PMID:16673284). The British Society for Haematology guideline on polycythaemia vera and secondary erythrocytosis (PMID:30426472) is the relevant published guidance document, though its coverage of Chuvash-specific management is limited.

### 12.3 Anticoagulation

`treatment_term`: NCIT:C63341 Anticoagulation Therapy or agent class NCIT:C263 Anticoagulant Agent (both verified). Used for treatment/secondary prevention of documented thrombosis, per general thrombosis practice. Heparin was used through a pregnancy alongside venesection (PMID:18161409). No CP-specific primary-prophylaxis evidence.

### 12.4 HIF-2α inhibition — the mechanism-matched therapy, and the most interesting development

`therapeutic_agent`: NCIT:C135627 Belzutifan (verified); `treatment_term`: NCIT:C15986 Pharmacotherapy; `therapeutic_modality`: SMALL_MOLECULE. `target_mechanisms`: `INHIBITS` the normoxic HIF-2α stabilization node.

- **Preclinical, and it's convincing.** Ghosh et al. 2021 (PMID:33512384) treated Vhl^R200W mice (and Irp1-KO mice, and the double mutant) with the second-generation allosteric HIF-2α inhibitor **MK-6482 (belzutifan)**: "MK-6482 treatment decreased EPO production and reversed polycythemia in all 3 mouse models. Drug treatment also decreased right ventricular pressure and mitigated pulmonary hypertension... to near normal wild-type levels and normalized the movement of the cardiac interventricular septum in VhlR200W mice." It also reduced Cxcl-12, the proposed driver of the pulmonary fibrosis.
- **Human evidence: one case, and read it carefully.** Siqueira do Amaral et al. 2024 (PMID:39113647) report a 30-year-old woman with congenital polycythemia, phlebotomy-refractory symptoms, Hb 19.0 g/dL, Hct 63.8%, EPO 138 mIU/mL. On belzutifan 120 mg daily: Hb 17.0 at 4 weeks, normalized to 13.0 at 8 weeks, then 9.4 g/dL at 16 weeks (grade 2 anemia) prompting dose reduction to 80 mg with normalized Hb and EPO. **Important caveat for curation: this patient was a *compound heterozygote* (R200W + c.562C>G), not a Chuvash R200W homozygote.** Do not curate this as "belzutifan treats Chuvash polycythemia" without that qualifier. Note also the anemia — HIF-2α inhibition overshoots easily, and belzutifan carries a known hypoxia/anemia toxicity profile (PMID:40806229).
- Related supporting context: belzutifan works in the mechanistically adjacent *EPAS1*-driven conditions (Pacak-Zhuang syndrome, PMID:34818480; *EPAS1*-mutated congenital erythrocytosis, PMID:40879399).

**This is the most important open therapeutic question in the disease**, and a good `KNOWLEDGE_GAP` discussion: does HIF-2α inhibition reduce *thrombosis and mortality* in R200W homozygotes, or only normalize the hematocrit — which we now know is not the thing that kills people?

### 12.5 JAK2 inhibition

`therapeutic_agent`: CHEBI:66919 ruxolitinib / NCIT:C77888 Ruxolitinib (both verified).
Mouse: TG101209 "reversed the disease phenotype in Vhl(R200W/R200W) knock-in mice" (PMID:21685897). Human: a single NEJM correspondence, "Clinical Improvement with JAK2 Inhibition in Chuvash Polycythemia" (PMID:27518686) — one patient, letter format, no abstract. Curate as EMERGING/experimental with N=1.

### 12.6 Tempol / IRP1-mediated translational repression of HIF2α

Mouse only. Ghosh et al. 2018 (PMID:29480820): "Tempol decreased erythropoietin production, corrected splenomegaly, normalized hematocrit levels, and increased the lifespans of these mice," acting via Irp1 — the effect was abolished when Irp1 was genetically ablated. The authors suggest "dietary supplementation of Tempol" as a possible approach. **No human data.** `evidence_source: MODEL_ORGANISM`.

### 12.7 Not indicated / avoid

- **Cytoreduction (hydroxyurea, NCIT:C560 / CHEBI:44423)** — explicitly advised against in JAK2-unmutated erythrocytosis (PMID:34021251).
- **Aggressive Hct-target phlebotomy** — see §12.1.

### 12.8 Supportive and other

- Genetic counseling — NCIT:C15240 (verified).
- Supportive care / symptom management — NCIT:C15747 (verified).
- Cardiovascular risk optimization (PMID:34021251).
- Iron repletion is a genuinely open question: iron deficiency is harmful for pulmonary pressure (PMID:21993671), but iron repletion in someone with suppressed hepcidin and HIF-driven iron avidity has not been studied. Another good gap.

### 12.9 Pharmacogenomics

No CPIC/PharmGKB guideline exists for CP. The nearest thing is the *EPO* rs1617640 / *TF* rs3811647 risk stratification (PMID:37435906), which is prognostic rather than drug-metabolism pharmacogenomics.

### 12.10 Clinical trials

- **NCT00495638** — the observational cardiovascular/echocardiographic study underlying PMID:21993671. Cite with `clinicaltrials:NCT00495638` and fetch via `just fetch-reference NCT00495638` before curating; I did not verify its current status field here, so do **not** guess the `status:` or `phase:` enum values.
- I found **no interventional trial registered specifically for Chuvash polycythemia**. Belzutifan trials are in RCC/VHL-syndrome/PPGL populations, not CP.

---

## 13. Prevention

- **Primary prevention of the disease: not possible.** It's a germline recessive condition. The only true primary prevention is reproductive: carrier/cascade testing, genetic counseling (NCIT:C15240), and in endemic populations the option of prenatal or preimplantation genetic testing. No published program exists.
- **Secondary prevention (early detection):** cascade testing of relatives after a proband; targeted PCR-RFLP screening of unexplained JAK2-negative erythrocytosis in high-prevalence regions (PMID:37362405). Population newborn screening is not established anywhere — and given that complications begin in childhood (PMID:25573974), that's arguably a defensible target for a regional program.
- **Tertiary prevention (preventing complications in diagnosed patients)** is where the real action is, and where the evidence is thinnest:
  - Symptom-directed rather than threshold-directed phlebotomy (PMID:34021251).
  - Avoid unnecessary iron depletion (PMID:21993671).
  - Low-dose aspirin and cardiovascular risk-factor control — advised, unproven (PMID:34021251; PMID:16673284).
  - Echocardiographic pulmonary hypertension surveillance.
  - Thromboprophylaxis around surgery, immobility, and pregnancy (PMID:18161409) — extrapolated from general practice.
- **Immunization:** no disease-specific vaccine considerations.
- **Public health / environmental interventions:** not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** the disease as such is **human-only** — `NCBITaxon:9606`. No naturally occurring animal counterpart of Chuvash polycythemia has been described.
- **OMIA:** I did not find an OMIA entry for a *VHL*-associated polycythemia in any domestic species. Treat as absent unless a targeted OMIA search says otherwise.
- **Breed (VBO):** not applicable.
- **Orthologs:** mouse *Vhl* (chromosome 6, MGI); zebrafish *vhl*. Functional conservation of the human residue is demonstrated experimentally — van Rooijen et al. (PMID:19304954): "Injections with human VHLp30 and R200W mutant mRNA demonstrate functional conservation of VHL between mammals and zebrafish at the amino acid level, indicating that vhl mutants are a powerful new tool to study genotype-phenotype correlations in human disease."
- **Comparative biology:** the VHL–PHD–HIF oxygen-sensing axis is deeply conserved across metazoans, which is precisely why zebrafish and mouse models recapitulate the human phenotype so well. The interesting *divergence* is species scale: hypoxic pulmonary vasoconstriction and pulmonary vascular remodeling are much more prominent in the mouse lung phenotype (fibrosis appears with age, PMID:20197624) than the human data have so far demonstrated.
- **Zoonosis / cross-species transmission:** not applicable.

---

## 15. Model Organisms

### 15.1 Mouse — the flagship

**Vhl^R200W knock-in (Vhl^R/R).** MGI allele: **`MGI:3776030`, Vhl<tm1Mcs>** (synonym Vhl^R), targeted, allele attribute **Hypomorph**, germline transmission, created in the M. Celeste Simon lab. MGI annotates it to human disease "familial erythrocytosis 2 DOID:0060474" and to abnormal phenotype systems: cardiovascular, growth/size/body, hematopoietic, immune, liver/biliary, mortality/aging. (Verified live against MGI 2026-08-15.)

**Phenotype recapitulation — genuinely high fidelity:**
- Erythrocytosis: "Vhl(R/R) mice developed polycythemia highly similar to the human disease," with HIF-2α upregulation and striking splenic erythroid/megakaryocyte expansion (PMID:17992257). The authors conclude it "is a faithful recapitulation of this VHL-associated syndrome."
- Pulmonary hypertension + enhanced normoxic respiration: "These mice developed pulmonary hypertension independently of polycythemia and enhanced normoxic respiration similar to Chuvash patients, further validating VhlR/R mice as a model for Chuvash disease" (PMID:20197624). Lungs show vascular remodeling, hemorrhage, edema, macrophage infiltration, and — in older mice — **fibrosis**.
- Metabolic: lower fasting glucose and glucose excursions, reduced hepatic *Glut2*/*G6pc*, increased skeletal muscle *Glut1*/*Pdk1*/*Pdk4* (PMID:23015148) — matching the human metabolic phenotype.
- Cardiac: pulmonary hypertension, RV hypertrophy, increased LVEF, 1.8-fold higher glycolytic flux, 1.5-fold higher lactate efflux, PCr depletion under isoproterenol stress (PMID:27422990).

**Model limitations — curate these honestly:**
- Pulmonary **fibrosis** in aged Vhl^R/R mice is prominent; a corresponding human fibrotic phenotype has not been demonstrated. Candidate `HUMAN_MODEL_MISMATCH`.
- Human thrombosis — the disease's actual cause of death — is not well recapitulated in the published mouse work. That is a substantive gap, and arguably *the* gap: the model reproduces everything except the thing that kills patients.
- The mouse cardiac work found "no changes in cardiac gene expression were detected" despite clear metabolic changes, and the authors conclude "the effects of manipulating HIF on the heart are dose dependent" (PMID:27422990) — a caution against extrapolating from high-HIF models.
- Hif2a heterozygosity rescue "resulted in partial protection against vascular remodeling, hemorrhage, and edema, **but not inflammation**" (PMID:20197624) — a documented partial rescue, useful as a `PARTIALLY_RECAPITULATES` / mechanism-dissection link.

**Other mouse lines used in the CP literature:**
- **Irp1-knockout mice** — polycythemia, pulmonary hypertension, and cardiac fibrosis via translational derepression of Hif2α (PMID:33512384; PMID:23395173 in the wider literature). Used as a mechanistic complement and as a second model for HIF-2α-directed drug testing.
- **VhlR200W;Irp1-KO double mutant** (PMID:33512384).
- **Hif1a^+/−** mice for the organ-size mechanism (PMID:20140661).
- Numerous conditional *Vhl* floxed alleles (Vhl<tm1Jae> MGI:2136645, etc.) exist but model *VHL-syndrome* biology, not CP.

### 15.2 Zebrafish

*vhl* germline inactivating mutants (van Rooijen et al., PMID:19304954) — "the first congenital embryonic viable systemic vertebrate animal model for VHL, representing the most accurate model for VHL-associated polycythemia to date." Phenotype: systemic hypoxic response by 1 dpf, severe hyperventilation and cardiophysiologic response, polycythemia with increased *epo/epor*, expanded c-myb⁺ HSCs and circulating erythroid precursors. ZFIN alleles hu2117 and hu2081 (verify the exact allele IDs in ZFIN before curating).
**Limitation:** these are *null* alleles, not R200W knock-ins — so they model VHL loss broadly rather than the CP hypomorph specifically. The R200W-specific validation was done by mRNA injection rescue, not by a knock-in line.

### 15.3 In vitro / cellular

- **Vhl^R/R ES cells** showing HIF-2α-biased activity (PMID:17992257).
- Patient-derived **native erythroid progenitors** assayed for EPO hypersensitivity — the assay that discriminated R200W from H191D (PMID:23403324). This is a genuine human-tissue functional readout and belongs in `experimental_models`.
- Patient **PBMCs** for transcriptomics (PMID:23993337) and plasma for cytokine multiplex (PMID:19062180).
- Cell lines expressing tumorigenic vs CP *VHL* variants for the TFAM-binding assay (PMID:35760869) — the cleanest in vitro dissociation of the oncogenic from the erythrocytosis arm.
- Human **skeletal muscle biopsy** with ³¹P-MRS in vivo (PMID:20616028) — a rare integrated human "model."

### 15.4 Model databases

MGI (informatics.jax.org — `MGI:3776030` is the allele to start from), IMSR/JAX for strain availability, ZFIN for the *vhl* lines, Alliance of Genome Resources for orthology, and the Human Phenotype Ontology / Monarch for the human-side phenotype comparison.

---

## Curation notes for the dismech entry (read before writing YAML)

A few things this disease will trip you on:

1. **Model it as a hypoxia-sensing disorder, not a myeloproliferative one.** The erythrocytosis is a *branch*, not the trunk. The trunk is `Impaired pVHL-HIF-α Degradation` → `Normoxic HIF Stabilization`, from which erythroid, pulmonary-vascular, thrombotic, iron, and metabolic branches all hang in parallel.

2. **Do not draw an edge from erythrocytosis to thrombosis.** Three independent studies say the thrombotic risk is hematocrit-independent (PMID:30872370; PMID:31289208; PMID:37435906). Drawing that edge would encode the exact error the field spent a decade correcting.

3. **HIF-1α vs HIF-2α:** both elevated; HIF-2α dominant for erythroid + pulmonary phenotypes (mouse genetics, PMID:20197624). The 2002 discovery paper's HIF-1α framing is historically important but incomplete — cite it for the ubiquitination mechanism, not for isoform attribution.

4. **The tumor absence is a curatable finding, with a mechanism** (§6.4). Three lines of evidence, including a clean molecular dissociation (PMID:35760869). This is one of the more interesting negative phenotypes in the whole KB.

5. **Two competing mechanistic hypotheses** (HIF-canonical vs VHL-SOCS1-JAK2) with human data on both sides — use `mechanistic_hypotheses` + `hypothesis_groups` on the relevant `downstream` edges rather than picking a winner.

6. **Candidate `conforms_to` targets:** `pulmonary_vascular_remodeling#Obstructive Pulmonary Vascular Remodeling` (strong), `thrombogenesis#Coagulation Cascade Activation and Thrombin-Driven Fibrin Formation` (moderate — the prothrombotic mediators are documented but the platelet/fibrin chain is not directly evidenced in CP), and possibly `deregulated_cellular_energetics#Aerobic Glycolysis (Warburg Effect)` for the metabolic arm — though that module is framed oncologically, so check the fit before wiring it.

7. **Belzutifan evidence is one compound heterozygote, not a homozygote.** Say so in the treatment `notes:` and the evidence `explanation:`.

8. **Frequencies:** the HPO annotation n/N values are mostly too small (and partly drawn from the *H191D* genotype) to support a `FrequencyEnum` band. Omit `frequency:` rather than manufacture one. The defensible cohort numbers are ~36% for pulmonary hypertension (5/14, PMID:16769575) and ~31% for pediatric complications over 8 years (PMID:25573974, verify first).

9. **Prevalence:** Orphanet says Unknown, not-yet-validated. Record `prevalence_class: UNKNOWN` for worldwide, plus the two founder-population **allele frequencies** as separate records with `measure_type: CARRIER_FREQUENCY`-adjacent framing and the verbatim Perrotta quote. Do not silently convert an allele frequency into a prevalence and present it as sourced.

10. **PMID correction to watch for:** the 1997 Sergeyeva Chuvash paper is **PMID:9058738**, not 9058724 (which is an unrelated AML signaling paper in the same *Blood* issue). Adjacent PMIDs in the same issue are an easy and invisible mis-citation — I made exactly that mistake mid-research and caught it only by fetching the abstract.

---

## Reference list (all PMIDs verified by direct PubMed retrieval, 2026-08-15)

| PMID | Citation | Evidence type |
|---|---|---|
| 9058738 | Sergeyeva A, et al. Congenital polycythemia in Chuvashia. *Blood* 1997;89(6):2148-54 | HUMAN_CLINICAL |
| 11987242 | Ang SO, et al. Endemic polycythemia in Russia: mutation in the VHL gene. *Blood Cells Mol Dis* 2002;28(1):57-62 | HUMAN_CLINICAL |
| 12415268 | Ang SO, et al. Disruption of oxygen homeostasis underlies congenital Chuvash polycythemia. *Nat Genet* 2002;32(4):614-21 | HUMAN_CLINICAL / IN_VITRO |
| 12702509 | Percy MJ, et al. Chuvash-type congenital polycythemia in 4 families of Asian and Western European ancestry. *Blood* 2003;102(3):1097-9 | HUMAN_CLINICAL |
| 12844285 | Pastore Y, et al. Mutations of von Hippel-Lindau tumor-suppressor gene and congenital polycythemia. *Am J Hum Genet* 2003;73(2):412-9 | HUMAN_CLINICAL |
| 14726398 | Gordeuk VR, et al. Congenital disorder of oxygen sensing... *Blood* 2004;103(10):3924-32 | HUMAN_CLINICAL |
| 15642664 | Cario H, et al. Mutations in the VHL gene and VHL-haplotype analysis... *Haematologica* 2005;90(1):19-24 | HUMAN_CLINICAL |
| 16210343 | Perrotta S, et al. Von Hippel-Lindau-dependent polycythemia is endemic on the island of Ischia. *Blood* 2006;107(2):514-9 | HUMAN_CLINICAL |
| 16673284 | Gordeuk VR, Prchal JT. Vascular complications in Chuvash polycythemia. *Semin Thromb Hemost* 2006;32(3):289-94 | Review |
| 16768548 | Smith TG, et al. Mutation of von Hippel-Lindau tumour suppressor and human cardiopulmonary physiology. *PLoS Med* 2006;3(7):e290 | HUMAN_CLINICAL |
| 16769575 | Bushuev VI, et al. Endothelin-1, VEGF and systolic pulmonary artery pressure... *Haematologica* 2006;91(6):744-9 | HUMAN_CLINICAL |
| 17992257 | Hickey MM, et al. VHL mutation in mice recapitulates Chuvash polycythemia via HIF-2α... *J Clin Invest* 2007;117(12):3879-89 | MODEL_ORGANISM |
| 18161409 | Chuvash-type polycythemia in pregnancy... *J Reprod Med* 2007;52(11) | HUMAN_CLINICAL (case) |
| 18223282 | Sergueeva AI, et al. Elevated homocysteine, glutathione and cysteinylglycine... *Haematologica* 2008;93(2):279-82 | HUMAN_CLINICAL |
| 19062180 | Niu X, et al. Altered cytokine profiles in patients with Chuvash polycythemia. *Am J Hematol* 2009;84(2):74-8 | HUMAN_CLINICAL |
| 19304954 | van Rooijen E, et al. Zebrafish mutants in the von Hippel-Lindau tumor suppressor... *Blood* 2009;113(25):6449-60 | MODEL_ORGANISM |
| 20140661 | Yoon D, et al. Increased size of solid organs... *J Mol Med* 2010;88(5):523-30 | HUMAN_CLINICAL / MODEL_ORGANISM |
| 20197624 | Hickey MM, et al. The VHL Chuvash mutation promotes pulmonary hypertension and fibrosis in mice. *J Clin Invest* 2010;120(3):827-39 | MODEL_ORGANISM |
| 20616028 | Formenti F, et al. Regulation of human metabolism by hypoxia-inducible factor. *PNAS* 2010;107(28):12722-7 | HUMAN_CLINICAL |
| 21606165 | Miasnikova GY, et al. The heterozygote advantage of the Chuvash polycythemia VHLR200W mutation... *Haematologica* 2011;96(9):1371-4 | HUMAN_CLINICAL |
| 21685897 | Russell RC, et al. Loss of JAK2 regulation via a heterodimeric VHL-SOCS1 E3 ubiquitin ligase... *Nat Med* 2011;17(7):845-53 | IN_VITRO / MODEL_ORGANISM |
| 21876117 | Gordeuk VR, et al. Chuvash polycythemia VHLR200W mutation is associated with down-regulation of hepcidin. *Blood* 2011;118(19):5278-82 | HUMAN_CLINICAL |
| 21993671 | Sable CA, et al. Pulmonary artery pressure and iron deficiency... *Haematologica* 2012;97(2):193-200 | HUMAN_CLINICAL |
| 22252661 | Gordeuk VR. Chuvash polycythemia: diagnosis and management. *Clin Adv Hematol Oncol* 2011;9(12):929-30 | Review |
| 23015148 | McClain DA, et al. Decreased serum glucose and glycosylated hemoglobin levels... *J Mol Med* 2013;91(1):59-67 | HUMAN_CLINICAL / MODEL_ORGANISM |
| 23403324 | Tomasic NL, et al. The phenotype of polycythemia due to Croatian homozygous VHL (571C>G:H191D)... *Haematologica* 2013;98(4):560-7 | HUMAN_CLINICAL |
| 23993337 | Zhang X, et al. Iron deficiency modifies gene expression variation induced by augmented hypoxia sensing. *Blood Cells Mol Dis* 2014;52(1):35-45 | HUMAN_CLINICAL |
| 25573974 | Sergueeva AI, et al. Complications in children and adolescents with Chuvash polycythemia. *Blood* 2015;125(2):414-5 | HUMAN_CLINICAL (letter) |
| 27422990 | Slingo M, et al. The VHL Chuvash mutation in mice alters cardiac substrate and high-energy phosphate metabolism. *Am J Physiol Heart Circ Physiol* 2016;311(3):H759-67 | MODEL_ORGANISM |
| 27518686 | Zhou AW, et al. Clinical Improvement with JAK2 Inhibition in Chuvash Polycythemia. *N Engl J Med* 2016;375(5):494-6 | HUMAN_CLINICAL (letter, N=1) |
| 28104701 | Sergueeva A, et al. Prospective study of thrombosis and thrombospondin-1 expression in Chuvash polycythemia. *Haematologica* 2017;102(5):e166-9 | HUMAN_CLINICAL |
| 29480820 | Ghosh MC, et al. Translational repression of HIF2α expression in mice with Chuvash polycythemia reverses polycythemia. *J Clin Invest* 2018;128(4):1317-25 | MODEL_ORGANISM |
| 29891534 | Lenglet M, et al. Identification of a new VHL exon and complex splicing alterations... *Blood* 2018;132(5):469-83 | HUMAN_CLINICAL / IN_VITRO |
| 30426472 | McMullin MFF, et al. BSH Guideline: management of specific situations in polycythaemia vera and secondary erythrocytosis. *Br J Haematol* 2019;184(2):161-75 | Guideline |
| 30872370 | Gordeuk VR, Key NS, Prchal JT. Re-evaluation of hematocrit as a determinant of thrombotic risk in erythrocytosis. *Haematologica* 2019;104(4):653-8 | Review |
| 31289208 | Gordeuk VR, et al. Thrombotic risk in congenital erythrocytosis... is not associated with elevated hematocrit. *Haematologica* 2020;105(3):e87-90 | HUMAN_CLINICAL (letter) |
| 33033909 | Hemolytic erythrocytosis: coinherited Chuvash polycythemia and G6PD Kerala-Kalyan. *Ann Hematol* 2021 | HUMAN_CLINICAL (case) |
| 33512384 | Ghosh MC, et al. Therapeutic inhibition of HIF-2α reverses polycythemia and pulmonary hypertension in murine models. *Blood* 2021;137(18):2509-19 | MODEL_ORGANISM |
| 34021251 | Gangat N, et al. JAK2 unmutated erythrocytosis: current diagnostic approach and therapeutic views. *Leukemia* 2021;35(8):2166-81 | Review |
| 34818480 | Belzutifan, a Potent HIF2α Inhibitor, in the Pacak-Zhuang Syndrome. *N Engl J Med* 2021 | HUMAN_CLINICAL |
| 35205407 | Hudler P, Urbancic M. The Role of VHL in the Development of von Hippel-Lindau Disease and Erythrocytosis. *Genes* 2022;13(2):362 | Review |
| 35760869 | Li S, et al. Impaired oxygen-sensitive regulation of mitochondrial biogenesis within the von Hippel-Lindau syndrome. *Nat Metab* 2022;4(6):739-58 | IN_VITRO |
| 37362405 | Duggal N, et al. A Screening Approach for Inherited Erythrocytosis due to the VHL:c.598C>T Mutation. *Indian J Hematol Blood Transfus* 2023 | HUMAN_CLINICAL |
| 37435906 | Shah BN, et al. Increased transferrin protects from thrombosis in Chuvash erythrocytosis. *Am J Hematol* 2023;98(10):1532-9 | HUMAN_CLINICAL |
| 39113647 | Siqueira do Amaral P, et al. von Hippel-Lindau syndrome-related congenital polycythemia and response to belzutifan. *Haematologica* 2024;109(12):4145-7 | HUMAN_CLINICAL (case) |
| 40130200 | Nagy ZF, et al. Case Report: Importance of high-throughput genetic investigations... *Pathol Oncol Res* 2025;31:1612037 | HUMAN_CLINICAL (case) |
| 40806229 | Belzutifan-Associated Hypoxia: A Review... *Int J Mol Sci* 2025 | Review |
| 40879399 | Successful Use of Targeted HIF-2α Inhibition in EPAS1-Mutated Congenital Erythrocytosis. *Pediatr Blood Cancer* 2025 | HUMAN_CLINICAL (case) |
| 41930727 | Yurt ÖF, et al. A Rare Cause of Erythrocytosis: VHL Gene Mutation. *Turk J Haematol* 2026 (online ahead of print) | HUMAN_CLINICAL (case) |

**Non-literature sources consulted live on 2026-08-15:** HPO/Monarch annotation API (`ontology.jax.org`, `api.monarchinitiative.org`) for HP terms and MONDO identity; NCBI ClinVar E-utilities (VCV 2232) for variant classification and coordinates; gnomAD v4 GraphQL API for population frequencies; Orphanet `api.orphacode.org` and the Orphadata `en_product1.xml` / `en_product9_prev.xml` bulk files for ORPHA definition, synonyms, ICD-10/ICD-11 mappings, and prevalence class; MGI allele report for `MGI:3776030`; and the dismech repository's own validated term caches (`cache/hp`, `cache/go`, `cache/cl`, `cache/uberon`, `cache/chebi`, `cache/ncit`, `cache/hgnc`) for every ontology CURIE quoted above except the HPO-API-sourced terms noted in §3.1.

**Sources (web):**
- [ClinVar RCV000002320 — NM_000551.4(VHL):c.598C>T (p.Arg200Trp)](https://www.ncbi.nlm.nih.gov/clinvar/RCV000002320.11/)
- [OMIM #263400 — Erythrocytosis, Familial, 2 (ECYT2)](https://www.omim.org/entry/263400)
- [Ang et al. 2002, *Nature Genetics* — Disruption of oxygen homeostasis underlies congenital Chuvash polycythemia](https://pubmed.ncbi.nlm.nih.gov/12415268/)
- [Gordeuk et al. 2004, *Blood* — Congenital disorder of oxygen sensing](https://ashpublications.org/blood/article/103/10/3924/17668/Congenital-disorder-of-oxygen-sensing-association)
- [Siqueira do Amaral et al. 2024, *Haematologica* — VHL-related congenital polycythemia and response to belzutifan](https://pmc.ncbi.nlm.nih.gov/articles/PMC11609798/)
- [Sergueeva et al. 2015, *Blood* — Complications in children and adolescents with Chuvash polycythemia](https://pmc.ncbi.nlm.nih.gov/articles/PMC4287647/)
- [Zhou et al. 2016, *NEJM* — Clinical Improvement with JAK2 Inhibition in Chuvash Polycythemia](https://www.nejm.org/doi/full/10.1056/NEJMc1600337)
- [Miasnikova et al. 2011, *Haematologica* — The heterozygote advantage of the Chuvash polycythemia VHLR200W mutation](https://haematologica.org/article/view/6076)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 52 |
| Resolved | 52 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 15 |
| Quoted claims found in source | 15 |
| Quoted claims with nothing to check against | 1 |

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `PMID:39113647`: "in two patients with the same VHL R200W/L188V genotype as our patient, Hb levels ranged from 16.3 g/dL to 21.0 g/dL. This variability highlights the..."
  - Reference resolved but exposes no abstract or full text to search

All extracted references resolved successfully.