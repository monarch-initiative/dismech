---
provider: claude_code
model: claude-fable-5, claude-haiku-4-5-20251001
cached: false
start_time: '2026-08-27T03:33:05.679397'
end_time: '2026-08-27T03:36:44.616579'
duration_seconds: 218.94
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Combined Oxidative Phosphorylation Defect Type 21
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
  web_search_requests: 3
  num_turns: 14
  total_cost_usd: 4.270769
  session_id: f70cae2e-abf8-4edd-a0f9-7745edae01ac
  stop_reason: end_turn
  permission_denials: 1
  denied_tools:
  - Bash
  assistant_text_blocks: 4
citation_count: 12
reference_validation:
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 9
  quotes_valid: 7
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:37454282
  relevance_assessed: 13
  on_topic: 12
  needs_review: true
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Combined Oxidative Phosphorylation Defect Type 21
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Combined Oxidative Phosphorylation Defect Type 21** covering all of the
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

I'll research Combined Oxidative Phosphorylation Defect Type 21 (COXPD21). I notice this repo already has cached references for this disease — I'll use those plus web searches to build the report.

The repo already contains a curated COXPD21 entry and cached primary references. I'll read those first, then supplement with web searches for identifiers and recent literature.

One final sweep for the most recent literature (2024–2026) before writing the report.

# Research Report: Combined Oxidative Phosphorylation Defect Type 21 (COXPD21)

**Prepared:** 2026-08-27 · **Category:** Mendelian (autosomal recessive mitochondrial disease) · **MONDO:** MONDO:0014398

---

## 1. Disease Information

**Overview.** Combined oxidative phosphorylation defect type 21 (COXPD21) is an ultra-rare autosomal recessive mitochondrial encephalomyopathy caused by biallelic pathogenic variants in **TARS2**, the nuclear gene encoding mitochondrial threonyl-tRNA synthetase. It presents in infancy with severe axial hypotonia combined with limb hypertonia, moderate-to-severe developmental delay (often with regression triggered by intercurrent illness), seizures, cerebellar signs, dystonia, and persistently elevated blood lactate. Brain MRI typically shows progressive cerebellar atrophy with vermian predominance and basal ganglia signal abnormalities. Roughly 30 patients have been reported worldwide.

The defining biochemical lesion is a **combined deficiency of respiratory chain complexes I, III, IV, and V with sparing of complex II** — the signature of impaired mitochondrial translation, since complex II is the only OXPHOS complex containing no mtDNA-encoded subunits (PMID:24827421):

> "Mutations in any component of the mitochondrial translation machinery can in principle cause inherited mitochondrial disorders affecting the MRC complexes containing mtDNA-encoded subunits (cI, cIII, cIV, cV), with the preservation of complex II, the only complex which has no mtDNA-encoded proteins." — Diodato et al., *Hum Mutat* 2014 (PMID:24827421)

**Key identifiers**

| Resource | Identifier |
|---|---|
| OMIM (disease) | [#615918](https://www.omim.org/entry/615918) |
| OMIM (gene) | [*612805 (TARS2)](https://omim.org/entry/612805) |
| Orphanet | [ORPHA:420733](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=420733) |
| MONDO | MONDO:0014398 |
| MedGen | [C4706316](https://www.ncbi.nlm.nih.gov/medgen/1638633) |
| ICD-10 | E88.8 (other specified metabolic disorders) |
| HGNC | hgnc:30740 (TARS2) |

**Synonyms:** COXPD21; combined oxidative phosphorylation deficiency 21; TARS2-related mitochondrial disease; TARS2 combined oxidative phosphorylation deficiency; mitochondrial threonyl-tRNA-synthetase (TARS2)-related disorder.

**Data provenance.** All information derives from aggregated disease-level resources (OMIM, Orphanet) and published case reports/cohorts — no EHR-derived or registry-scale individual-level data exist. The largest single source is the 2023 international cohort of Accogli et al. (18 new individuals, pooled analysis of 28; PMID:37454282, *Genetics in Medicine*). GeneReviews has **no chapter** for this entity.

---

## 2. Etiology

**Causal factor.** Exclusively genetic: biallelic (homozygous or compound heterozygous) germline variants in **TARS2** on chromosome 1q21.2. First identified in 2014 in two siblings:

> "compound heterozygous mutations in TARS2 in two siblings presenting with axial hypotonia and severe psychomotor delay associated with multiple MRC defects" — PMID:24827421

**Genetic risk factors.** Consanguinity (homozygous genotypes in consanguineous families); carrier parents. A **Chinese-specific founder allele**, c.470C>G p.(Thr157Arg), substantially shifts the prior in Chinese patients:

> "one previously reported variant (c.470 C > G, p.Thr157Arg) recurred in six Chinese individuals with COXPD21 but was not present in populations of other races" — Chen et al., *Orphanet J Rare Dis* 2024 (PMID:39394138)

**Environmental risk/modifying factors.** No environmental cause exists, but **intercurrent (usually febrile) illness is the recognized trigger of developmental regression** — the catabolic-stress pattern common to mitochondrial disease:

> "The regression of developmental milestones occurred within the first year of life for 3 individuals, typically triggered by intercurrent illnesses." — PMID:37454282

**Protective factors.** None described. **Gene–environment interaction:** limited to the illness-triggered decompensation above; no formal GxE data (CTD has no curated interactions for this disease).

---

## 3. Phenotypes

All frequencies below come from the pooled 28-patient analysis in PMID:37454282, the only source with denominators:

> "occurrence of regression (n = 10/28, 36%), seizure (n = 14/28, 50%), secondary microcephaly (8/23, 34%), axial hypotonia (24/27, 89%), limb hypertonia (18/27, 67%), cerebellar deficits (12/24, 50%), and extrapyramidal movements (13/23, 56%)"

| Phenotype | HPO term | Frequency | Notes |
|---|---|---|---|
| Axial hypotonia | HP:0008936 | 89% (24/27) | Congenital onset in nearly all; coexists with limb hypertonia — the "floppy trunk, stiff limbs" motor signature |
| Global developmental delay / intellectual disability | HP:0001263 / HP:0001249 | ~95% | "All but 1 individual had moderate (n = 7) or severe (n = 10) developmental delay/intellectual disability" (PMID:37454282); only 4/18 walked unsupported, 8 nonverbal |
| Increased circulating lactate | HP:0002151 | 85% (17/20) | "increased blood lactate is a consistent finding in all affected individuals for whom it was checked (17/20 85%)" (PMID:37454282); also demonstrable as brain lactate peaks on MRS |
| Limb hypertonia | HP:0002509 | 67% (18/27) | With brisk reflexes |
| Extrapyramidal movements / dystonia | HP:0001332 | 56% (13/23) | Consistent with basal ganglia involvement |
| Seizures | HP:0001250 | 50% (14/28) | Tonic-clonic, myoclonic, infantile spasms; controlled by ASMs in only ~half |
| Cerebellar signs (ataxia, tremor, titubation, dysmetria, oculomotor apraxia) | HP:0001251 | 50% (12/24) | |
| Developmental regression | HP:0002376 | 36% (10/28) | Typically illness-triggered; within the first year in 3 patients |
| Secondary microcephaly | HP:0005484 | 34% (8/23) | Postnatal, reflecting progressive brain volume loss |
| Cerebellar atrophy (MRI) | HP:0001272 | 75% (12/16) | Vermian predominance; **acquired** — one infant imaged early had a normal cerebellum, so follow-up MRI is needed |
| Basal ganglia MRI signal change | HP:0012751 | 50% globi pallidi; 31% caudate/putamen | Can progress with lactate peaks and dentate involvement → Leigh-like pattern |
| Reduced white matter volume + thin corpus callosum | HP:0002500 / HP:0033725 | 44% (7/16) | Plus enlarged subarachnoid spaces in 62.5% |
| Distal renal tubular acidosis | HP:0008341 | 24% (6/25) | Actionable and easily missed; one patient progressed to end-stage CKD by age 4.5 y (PMID:38482264) |
| Hypertrophic cardiomyopathy | HP:0001639 | 12% (3/25) | Biventricular; one with pulmonary hypertension |
| Sensorineural hearing impairment | HP:0000407 | uncertain | 3 earlier patients vs. 0/18 in the largest cohort; possibly under-ascertained (PMID:34508595, PMID:37454282) |
| Neonatal diabetes mellitus | HP:0008255 | genotype-restricted | Only in p.(Arg327Gln) homozygotes (PMID:39509107) |
| Hyperhidrosis | HP:0000975 | occasional | Added by PMID:34508595 |
| Refractory hypokalemia | HP:0002900 | rare | Single case, with tubulopathy (PMID:36150709) |
| Reduced fetal movement | HP:0001558 | rare | Proposed novel prenatal feature (PMID:36218002) |

**Onset:** neonatal/infantile. **Course:** progressive or stepwise-regressive. **Quality-of-life impact:** severe — most patients never achieve independent ambulation or speech; no formal QoL instrument data exist for this disorder.

---

## 4. Genetic/Molecular Information

**Causal gene.** TARS2 (hgnc:30740; OMIM *612805; chromosome 1q21.2), encoding the 718-residue mitochondrial threonyl-tRNA synthetase:

> "TARS2 (MIM 612805) encodes a 718-amino acid mitochondrial threonyl tRNA-synthetase, which contains an N-terminal N1 domain (Leu20–Ser124), an N2 domain (for editing) (Pro125–Asp301), an aminoacylation domain (for amino acid activation and tRNA charging) (His302–Gly605), and an anticodon binding domain (for tRNA binding) (Lys606–Phe718)" — PMID:39394138

**Variant spectrum.** Overwhelmingly **missense**, with strong recurrence: 17 of the 24 families reported by 2023 carried a recurrent variant (PMID:37454282). Recurrent alleles: p.(Thr157Arg) (Chinese founder), p.(Pro155Leu), p.(Ser258Leu), p.(Glu512Lys), p.(Phe323Cys), p.(Arg346Cys), and splice variants c.387+6T>C and c.695+3A>G. Missense variants cluster in three regions: the Rag GTPase-binding region (residues 301–381), the editing (N2) domain, and the anticodon-binding domain. Only one patient ever carried a stop-gain, and only in trans with a splice variant:

> "There is a predominance of missense variants and only 1 patient previously reported was harboring 1 stop-gain in combination with a splicing variant, suggesting that total loss of TARS2 is likely lethal in humans." — PMID:37454282

**Functional consequence:** partial loss of function (hypomorphic alleles). The p.(Pro282Leu) mutation was biochemically dissected in vitro:

> "the mutation induces a decrease in Thr activation, aminoacylation, and proofreading activities and a change in the protein structure and/or stability, which might cause reduced catalytic efficiency" — Wang et al., *J Biol Chem* 2016 (PMID:26811336)

**Genotype–phenotype correlation** is weak but not absent: p.(Pro155Leu) associates with severe disease; p.(Glu512Lys) and p.(Ser258Leu) with milder motor/cerebellar phenotypes; Rag-binding-region compound heterozygotes show basal ganglia and cerebellar *signal change without atrophy*; and p.(Arg327Gln) homozygosity uniquely produces syndromic neonatal diabetes (PMID:37454282; PMID:39509107).

**Origin:** germline in all cases; no somatic, epigenetic, or chromosomal contributions described. **Modifier genes:** none identified. **Allele frequencies:** all pathogenic alleles are absent or ultra-rare in gnomAD; founder-allele carrier data limited to the Chinese p.(Thr157Arg) observation.

---

## 5. Environmental Information

Not applicable as a cause. The only environmentally shaped element is **metabolic decompensation with intercurrent infection/fever**, driving developmental regression (PMID:37454282). No toxin, lifestyle, or infectious agent is implicated.

---

## 6. Mechanism / Pathophysiology

Two mechanistic arms are supported by the literature; they converge on the neurological phenotype.

### Arm 1 — Canonical: impaired mitochondrial aminoacylation → translation failure → combined OXPHOS deficiency (ESTABLISHED)

Causal chain: **biallelic hypomorphic TARS2 → ↓threonine-tRNA ligase activity (GO:0004829) and ↓editing of mischarged Ser-tRNA^Thr → ↓charged mt-tRNA^Thr (GO:0070127, tRNA aminoacylation for mitochondrial protein translation) → ↓mitochondrial translation (GO:0032543) of the 13 mtDNA-encoded subunits → combined deficiency of complexes I/III/IV/V with complex II spared (GO:0033108) → ↓oxidative phosphorylation (GO:0006119), ↓ATP, lactate accumulation → energy failure in cerebellum, basal ganglia, muscle, heart, kidney tubule, cochlea.**

Direct patient-level measurement of both key steps:

> "The amount of VARS2 and TARS2 proteins and valyl-tRNA and threonyl-tRNA levels were decreased in samples of afflicted patients according to the genetic defect." — PMID:24827421

Causality confirmed by rescue:

> "Expression of the corresponding wild-type transcripts in immortalized mutant fibroblasts rescued the biochemical impairment of mitochondrial respiration" — PMID:24827421

**Important caveat:** the respiratory chain defect is **tissue-restricted** — found in muscle but not reliably in fibroblasts or liver (Orphanet ORPHA:420733; PMID:37454282). Even in muscle, findings are inconsistent (one of two biopsied cohort patients showed only complex I deficiency).

### Arm 2 — Non-canonical: loss of threonine sensing / Rag GTPase binding → mTORC1 dysregulation (EMERGING)

TARS2 has a moonlighting role in amino acid sensing at the lysosome:

> "Upon threonine supplementation, TARS2 preferentially binds RagC^GTP and promotes the conversion of inactive Rag GTPases (RagA^GDP/RagC^GTP) into the active form (RagA^GTP/RagC^GDP). This is sufficient to recruit mTORC1 to lysosomes." — PMID:37454282

Four disease variants (F323C, R327Q, E342D, R346C) fall in the Rag-binding region (residues 301–381) and showed decreased Rag GTPase binding in co-IP experiments; zebrafish knockdown dysregulated mTORC1 targets (PGC1α down, PPARα up). The strongest human evidence for this arm is the neonatal diabetes association:

> "Current evidence suggests that the p.(Arg327Gln) variant disrupts TARS2's regulation of the mTORC1 pathway which is essential for β-cells." — Sanchis-Juan et al., 2025 (PMID:39509107)

Limitations keeping this arm provisional: the transfected variant constructs also had reduced basal expression (39–66% of wild type), confounding binding vs. abundance; mTORC1 activity was never measured in patient cells; and the in vivo readout is a morpholino knockdown, not an allele model. GO term: TORC1 signaling (GO:0038202), dysregulated.

**Cell types and processes:** neurons (CL:0000540) — especially cerebellar and basal ganglia neurons; oligodendrocytes/myelination (reduced mbpa in zebrafish); skeletal myocytes (CL:0000188); cardiomyocytes (CL:0000746); renal intercalated cells of the distal tubule (distal RTA); pancreatic beta cells (CL:0000169, allele-restricted). Subcellular compartment: mitochondrion (GO:0005739), mitochondrial matrix (GO:0005759); lysosomal surface for the mTORC1 arm (GO:0005765).

**Omics/profiling:** no disease-specific GEO/proteomics/metabolomics datasets, single-cell, or spatial data exist beyond the functional studies cited.

---

## 7. Anatomical Structures Affected

- **Primary — CNS:** cerebellum, especially vermis (UBERON:0002037, UBERON:0004720) — atrophy in 75%; basal ganglia (UBERON:0002420) — globus pallidus (UBERON:0001875), caudate (UBERON:0001873), putamen (UBERON:0001874); cerebral white matter (UBERON:0002316) and corpus callosum (UBERON:0002336); dentate nucleus (UBERON:0002130).
- **Secondary:** skeletal muscle (UBERON:0001134 — site of the biochemical defect and hypotonia); heart/myocardium (UBERON:0000948 — hypertrophic cardiomyopathy, 12%); kidney distal tubule (UBERON:0004135 — RTA, 24%; one CKD case); inner ear/cochlea (UBERON:0001844 — sensorineural hearing loss); pancreatic islets (UBERON:0000006 — allele-restricted diabetes).
- **Lateralization:** bilateral and symmetric (e.g., "the head of the caudate and partial lenticular nucleus were bilateral symmetrical T2-weighted imaging (T2WI) hyperintense," PMID:36218002).
- **Subcellular:** mitochondrion (GO:0005739); inner mitochondrial membrane respiratory complexes I, III, IV, V (GO:0005747, GO:0005750, GO:0005751, GO:0005753).

---

## 8. Temporal Development

- **Onset:** neonatal to infantile. OMIM describes a bimodal pattern: "onset within the first months of life of severe hypotonia, failure to thrive, epilepsy, and early death or… onset after 6 months of life with a milder course and longer survival" ([OMIM #615918](https://www.omim.org/entry/615918)). Reduced fetal movement suggests possible prenatal onset in some (PMID:36218002).
- **Progression:** progressive or stepwise, with regression episodes precipitated by febrile illness (36%). Cerebellar atrophy is acquired: "the cerebellum was initially normal in 1 infant who underwent brain MRI in the first months of life… cerebellar atrophy might develop later in TARS2-related disorders and be missed without follow-up MRI studies" (PMID:37454282). Basal ganglia lesions can progress to a Leigh-like pattern with lactate peaks.
- **Course:** chronic and lifelong; no remission described. **Critical periods:** infancy and intercurrent illnesses are the windows of decompensation; early diagnosis enables surveillance of treatable complications (RTA, cardiomyopathy, hearing).

---

## 9. Inheritance and Population

- **Prevalence:** <1/1,000,000 (Orphanet class); ~30 reported patients globally; no incidence estimate is possible.
- **Inheritance:** autosomal recessive (HP:0000007). "We identified 16 novel or ultra-rare TARS2 variants in either a homozygous (n = 7) or compound heterozygous state (n = 10)" (PMID:37454282).
- **Penetrance:** presumed complete for biallelic pathogenic genotypes; **expressivity** is variable (severe neonatal-lethal to milder later-onset; allele-dependent).
- **Anticipation, germline mosaicism:** not reported. **Consanguinity:** contributes homozygous cases.
- **Founder effect:** c.470C>G p.(Thr157Arg) is a confirmed Chinese-specific founder mutation (haplotype-supported; PMID:39394138). p.(Arg327Gln) recurred in four individuals with neonatal diabetes (PMID:39509107).
- **Demographics:** reported worldwide (Europe, China, US, Middle East); no sex bias evident in the small cohorts; carrier frequency unknown.

---

## 10. Diagnostics

- **Primary route: exome or genome sequencing** — in practice the only reliable one. The disorder lacks a pathognomonic biomarker, enzymology is tissue-restricted and inconsistent, and imaging overlaps with other mt-aaRS (ARS2) disorders. "Exome or genome sequencing was carried out in 15 families" (PMID:37454282). GTR lists clinical TARS2 testing ([GTR gene 80222](https://www.ncbi.nlm.nih.gov/gtr/genes/80222/)); trio WES is the typical approach (PMID:36218002). mtDNA testing is useful only to exclude phenocopies.
- **Laboratory:** blood lactate (elevated in 85%; LOINC 2524-7); consider urine analysis for tubulopathy, bicarbonate/potassium (one case with refractory hypokalemia, PMID:36150709).
- **Imaging:** brain MRI (abnormal in all imaged patients) — cerebellar atrophy with vermian predominance, faint pallidal T2 change, white matter loss with thin corpus callosum; MRS may show basal ganglia lactate peaks. Follow-up imaging is required because early MRI can be normal.
- **Muscle biopsy / respiratory chain enzymology:** historically diagnostic (combined I/III/IV/V deficiency, complex II spared) but no longer first-line; normal fibroblast or even muscle enzymology does not exclude the diagnosis.
- **Surveillance workup after diagnosis:** "A cardiological evaluation, urine analysis for tubulopathy and hearing screening is warranted in patients with biallelic TARS2 variants." (PMID:37454282)
- **Differential diagnosis:** other COXPD subtypes and mt-aaRS disorders (e.g., VARS2-related COXPD20 — described in the same 2014 paper), Leigh syndrome spectrum, pontocerebellar hypoplasias, primary dystonias. For infants with neonatal diabetes plus epilepsy/developmental delay, TARS2 p.(Arg327Gln) should now be on the panel (PMID:39509107).
- **Screening:** not on newborn screening panels; carrier/cascade testing appropriate in affected families; PGD/prenatal testing feasible once familial variants are known.

---

## 11. Outcome / Prognosis

- **Survival:** the severe neonatal form causes early death (OMIM); later-onset cases survive longer with severe disability. No survival-rate statistics exist given ~30 cases.
- **Function:** at last evaluation in the largest cohort, "only 4 individuals were able to walk without support and 8 were nonverbal" (PMID:37454282).
- **Complications:** progressive Leigh-like basal ganglia disease, epilepsy (drug-resistant in ~half), cardiomyopathy with pulmonary hypertension, chronic kidney disease — "We report on the first COXPD21 patient with generalized tubular dysfunction and early childhood progression to chronic kidney disease (CKD)" with ESKD at 4.5 years (PMID:38482264).
- **Prognostic factors:** allele identity is the best available predictor — p.(Pro155Leu) severe; p.(Glu512Lys)/p.(Ser258Leu) milder; Rag-region variants a distinct imaging/endocrine profile. Early onset (<6 months) predicts a worse course (OMIM). No validated prognostic biomarker.

---

## 12. Treatment

**No disease-modifying therapy exists.** Management is entirely supportive:

- **Antiseizure medication** (NCIT:C15986 Pharmacotherapy) — the only pharmacological intervention with reported outcomes: "Epilepsy… occurred in 8 individuals and was successfully controlled with anti-seizure medications in half of them" (PMID:37454282). No specific agent is established as preferable.
- **Electrolyte/alkali replacement** for renal tubular acidosis and hypokalemia (NCIT:C15368 Electrolyte Replacement / supportive care NCIT:C15747); renal replacement therapy was required in the CKD case (PMID:38482264).
- **Cardiac surveillance and management** of hypertrophic cardiomyopathy; **hearing aids/habilitation** where hearing loss is found; **physical/occupational/speech therapy** (NCIT:C15302, NCIT:C121351, NCIT:C159273); nutritional support for failure to thrive (NCIT:C15747).
- **Mitochondrial "cocktail" supplements** are commonly used empirically in COXPD disorders but have no reported efficacy evidence in COXPD21 specifically.
- **Experimental/future:** the mTORC1 finding raises a hypothesis-level therapeutic question — "these observations raise the question whether mTORC1 drug modulators could be therapeutic for individuals with TARS2-related disorder in the future" (PMID:37454282). No clinical trials (interventional or observational) are registered for COXPD21/TARS2 on ClinicalTrials.gov. **Genetic counseling** (NCIT:C15240) is indicated for all families.

**Pharmacogenomics:** none established. Standard mitochondrial-disease caution regarding valproate and other mitotoxic drugs is reasonable but not specifically evidenced in COXPD21.

---

## 13. Prevention

- **Primary:** none possible (genetic); **genetic counseling** with carrier testing of relatives, prenatal diagnosis, or preimplantation genetic testing once familial variants are known (ACMG-standard practice for AR conditions).
- **Secondary:** early molecular diagnosis via WES in infants with hypotonia + lactic acidosis; the Chinese founder allele simplifies targeted testing in that population (PMID:39394138).
- **Tertiary:** aggressive management of febrile illnesses (regression trigger); systematic cardiac, renal, and audiological surveillance to catch treatable complications early (PMID:37454282); RTA treatment to protect growth and kidney function.

---

## 14. Other Species / Natural Disease

No naturally occurring TARS2-deficiency disease is described in any non-human species (no OMIA entry). The gene is conserved across vertebrates (zebrafish *tars2* rescues experiments with human mRNA demonstrate functional conservation, PMID:37454282) and its bacterial/yeast orthologs (ThrRS; yeast mitochondrial MST1) have been used as surrogates. No zoonotic or veterinary relevance.

---

## 15. Model Organisms

- **Zebrafish morpholino knockdown (primary in vivo model; PMID:37454282).** Splice-blocking *tars2* MO produced "a significant reduction in head size… and heart edema"; a smaller cerebellum (olig2⁺ area); "decreased myelination and increased seizure activity, as indicated by reduced mbpa and elevated c-fos expressions"; extensive brain apoptosis; and mTORC1-target dysregulation (PGC1α↓, PPARα↑). Specificity was established by rescue with zebrafish or human wild-type mRNA — "This evidence confirms that the observed phenotypes resulted from tars2 downregulation and demonstrates functional conservation across species" — and the model was used as a variant-pathogenicity assay: none of 17 human variants rescued fully. **Fidelity: moderate/partial** — it recapitulates microcephaly, cerebellar hypoplasia, hypomyelination, and seizure-like activity, but as embryonic developmental hypoplasia rather than progressive postnatal atrophy, and morpholino knockdown cannot model the human hypomorphic missense state.
- **Yeast (S. cerevisiae) complementation** — used to validate pathogenicity of TARS2/VARS2 variants (PMID:24827421) and of P282L and splice variants ("the yeast ThrRS-deletion model is suitable to test pathology-associated point mutations," PMID:26811336).
- **Patient fibroblasts / HEK293T cells** — immortalized patient fibroblasts with wild-type rescue (PMID:24827421); transfection-based Rag GTPase co-IP studies (PMID:37454282).
- **No mouse knockout disease model** has been published; constitutive loss is likely embryonic-lethal, consistent with the absence of biallelic-truncating patients. **Not a MorPhiC anchor gene.** An iPSC-derived beta-cell model of p.(Arg327Gln) is the obvious next experimental system given the neonatal diabetes association (PMID:39509107) but has not yet been reported.

---

## Key Citations

1. Diodato D, et al. *VARS2 and TARS2 mutations in patients with mitochondrial encephalomyopathies.* Hum Mutat. 2014. **PMID:24827421** (first description)
2. Wang Y, et al. *A human disease-causing point mutation in mitochondrial threonyl-tRNA synthetase induces both structural and functional defects.* J Biol Chem. 2016. **PMID:26811336**
3. Li Y, et al. *Novel compound heterozygous TARS2 variants in a Chinese family… case report.* BMC Med Genet. 2020. **PMID:33153448** ([PMC7643390](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7643390/))
4. Zheng WQ, et al. *Elucidating the molecular mechanisms associated with TARS2-related mitochondrial disease.* Hum Mol Genet. 2022. **PMID:34508595**
5. He P, et al. *Novel TARS2 variant… and a systematic review.* Am J Med Genet A. 2023. **PMID:36218002**
6. Accogli A, et al. *Clinical, neuroradiological, and molecular characterization of mitochondrial threonyl-tRNA-synthetase (TARS2)-related disorder.* Genet Med. 2023. **PMID:37454282** (largest cohort; mTORC1 mechanism; zebrafish model)
7. Gao X, et al. *TARS2 variants cause COXPD-21: case report and literature review.* Neuropediatrics. 2024. **PMID:36150709**
8. *Expanding the phenotypic spectrum: chronic kidney disease in a patient with COXPD21.* 2023/2024. **PMID:38482264**
9. Chen et al. *TARS2 c.470C>G is a Chinese-specific founder mutation…* Orphanet J Rare Dis. 2024. **PMID:39394138** ([link](https://link.springer.com/article/10.1186/s13023-024-03365-w))
10. *A homozygous TARS2 variant is a novel cause of syndromic neonatal diabetes.* 2025. **PMID:39509107**

Sources: [OMIM #615918](https://www.omim.org/entry/615918) · [OMIM *612805](https://omim.org/entry/612805) · [Orphanet ORPHA:420733](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=420733) · [Orphanet TARS2 gene page](https://www.orpha.net/en/disease/gene/TARS2) · [MedGen C4706316](https://www.ncbi.nlm.nih.gov/medgen/1638633) · [NIH GTR TARS2](https://www.ncbi.nlm.nih.gov/gtr/genes/80222/) · [PubMed 36150709](https://pubmed.ncbi.nlm.nih.gov/36150709/) · [PubMed 33153448](https://pubmed.ncbi.nlm.nih.gov/33153448/) · [PubMed 36218002](https://pubmed.ncbi.nlm.nih.gov/36218002/) · [BMC Med Genet case report](https://bmcmedgenet.biomedcentral.com/articles/10.1186/s12881-020-01149-0) · [OJRD founder-mutation paper](https://link.springer.com/article/10.1186/s13023-024-03365-w)

**Gaps to flag for the knowledge base:** no prevalence numerator beyond case counts; no GeneReviews chapter; no registered clinical trials; no mouse model; no disease-specific omics datasets; hearing-loss frequency unresolvable from current denominators; and the mTORC1 arm remains an emerging (not established) mechanism pending direct mTORC1 activity measurement in patient cells.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 9 |
| Quoted claims found in source | 7 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 13 |
| On topic | 12 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMID:37454282`: "the cerebellum was initially normal in 1 infant who underwent brain MRI in the first months of life… cerebellar atrophy might develop later in TARS2-related disorders and be missed without follow-up MRI studies"
  - closest text in source: "Notably, the cerebellum was initially normal in 1 infant who underwent brain MRI in the first months of life"
- `PMID:37454282`: "Epilepsy… occurred in 8 individuals and was successfully controlled with anti-seizure medications in half of them"
  - closest text in source: "Epilepsy, including tonic-clonic seizures, myoclonic seizures, and infantile spasms, occurred in 8 individuals and was successfully controlled with anti-seizure medications in half of them"