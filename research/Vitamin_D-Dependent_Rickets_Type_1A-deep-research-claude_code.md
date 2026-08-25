---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-19T18:02:23.435468'
end_time: '2026-08-19T18:08:36.074004'
duration_seconds: 372.64
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Vitamin D-Dependent Rickets Type 1A
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
  web_search_requests: 16
  num_turns: 27
  total_cost_usd: 2.1090923000000004
  session_id: 75ec52a1-0e70-502f-850e-ec2680b017b0
  stop_reason: end_turn
  assistant_text_blocks: 3
citation_count: 32
reference_validation:
  total_references: 21
  verified: 21
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 0
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMC:PMC11439522
  relevance_assessed: 21
  on_topic: 14
  needs_review: true
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Vitamin D-Dependent Rickets Type 1A
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Vitamin D-Dependent Rickets Type 1A** covering all of the
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

I'll research Vitamin D-Dependent Rickets Type 1A (CYP27B1 deficiency) now, gathering data from OMIM, GeneReviews, PubMed, and other authoritative sources.

I now have sufficient depth to compile the comprehensive report.

I now have comprehensive research material. Here is the complete report.

# Vitamin D-Dependent Rickets Type 1A (VDDR1A) — Comprehensive Research Report

## 1. Disease Information

**Overview.** Vitamin D-dependent rickets type 1A (VDDR1A), also called pseudovitamin D deficiency rickets (PDDR) or vitamin D hydroxylation-deficient rickets type 1A, is a rare autosomal recessive inborn error of vitamin D metabolism caused by biallelic loss-of-function variants in **CYP27B1**, the gene encoding renal 25-hydroxyvitamin D-1α-hydroxylase. The enzyme defect abolishes or severely impairs the final activating hydroxylation step that converts 25-hydroxyvitamin D (25(OH)D, calcidiol) to 1,25-dihydroxyvitamin D (1,25(OH)₂D, calcitriol), the biologically active vitamin D hormone. The resulting selective calcitriol deficiency causes intestinal calcium malabsorption, hypocalcemia, secondary hyperparathyroidism, and impaired bone mineralization (rickets in children; osteomalacia if it persisted to adulthood), despite normal-to-elevated levels of the inactive precursor 25(OH)D ([OMIM #264700](https://omim.org/entry/264700); [PMC4489500](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4489500/)).

**Key identifiers:**
- **OMIM:** #264700 (VDDR1A phenotype); *CYP27B1* gene OMIM 609506
- **Orphanet:** ORPHA289157 (Hypocalcemic vitamin D-dependent rickets)
- **ICD-10-CM:** E83.32 (Hereditary vitamin D-dependent rickets, type 1 and type 2); Orphanet also cross-maps to E55.0 (Rickets, active)
- **GARD (NIH Genetic and Rare Diseases Information Center):** "Vitamin D-dependent rickets, type 1"
- **Gene:** CYP27B1, chromosome 12q14.1 (some sources cite 12q13.3/12q14)
- **MeSH/synonym set:** Pseudo-vitamin D deficiency rickets; PDDR; Type I vitamin D-dependent rickets; 1α-hydroxylase deficiency; hereditary pseudo-vitamin D deficiency rickets

**Synonyms/alternative names:** Pseudovitamin D-deficiency rickets (PDDR), vitamin D-dependent rickets type I, 25-hydroxyvitamin D-1α-hydroxylase deficiency, hereditary vitamin D dependency, hypocalcemic vitamin D-dependent rickets.

**Data source character:** Understanding of VDDR1A derives almost entirely from aggregated case reports and small case series/cohorts (individual-patient literature), plus a founder-population registry (Saguenay–Lac-Saint-Jean, Quebec) and structured aggregations such as OMIM, Orphanet, and MalaCards; no large-scale EHR/claims-based epidemiologic studies exist given its rarity ([PMC9671943](https://pmc.ncbi.nlm.nih.gov/articles/PMC9671943/); [PMC9120640](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9120640/)).

Sources: [OMIM #264700](https://omim.org/entry/264700) | [PMC4489500](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4489500/) | [ICD10Data E83.32](https://www.icd10data.com/ICD10CM/Codes/E00-E89/E70-E88/E83-/E83.32) | [MalaCards VDDR1A](https://www.malacards.org/card/vitamin_d_hydroxylation_deficient_rickets_type_1a)

---

## 2. Etiology

**Disease causal factors — genetic.** VDDR1A is caused exclusively by biallelic (homozygous or compound heterozygous) pathogenic loss-of-function variants in *CYP27B1*. As of recent surveys, **~78–100 distinct pathogenic CYP27B1 variants** have been reported across >100–219 published patients from diverse ethnic groups, spanning all 9 exons; missense and nonsense substitutions predominate, alongside splice-site variants, small insertions, deletions, and duplications ([PMC6398191](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6398191/); PLOS ONE, [PMC4489500](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4489500/)). A 2022 series of 12 Chinese children found 9 CYP27B1 variants (4 known, 5 novel: c.937G>C p.Glu313Gln, c.232delG p.Ala78Profs*81, c.565G>T p.Glu189*, c.1192G>A p.Gly398Ser, c.402G>A p.Trp134*), with single-nucleotide substitutions (66.7%), small deletions (22.2%), and small insertions (11.1%) ([Front Pediatr 2022, PMID:36405822, PMC9671943](https://pmc.ncbi.nlm.nih.gov/articles/PMC9671943/)).

**Founder/recurrent variants:**
- **c.1319_1325dupCCCACCC (p.Phe443Profs*24):** a regional hotspot in southern China, found in 66.7% of a 12-patient Guangzhou cohort (45.8% of alleles) ([PMC9671943](https://pmc.ncbi.nlm.nih.gov/articles/PMC9671943/)).
- **c.262delG (p.Val88Trpfs*71):** the founder variant of the Saguenay–Lac-Saint-Jean (SLSJ) region of Quebec, Canada, where every molecularly confirmed VDDR1A case traces to this single allele.
- Intron-1 mutations shared by patients from a common city of origin have also suggested independent founder effects in other populations ([various case reports, search synthesis]).
- **p.(Ala129Thr):** a recurrent partial loss-of-function ("hypomorphic") variant retaining ~50% residual enzymatic activity, associated with a distinctly milder phenotype (see Section 4/Genotype-phenotype below) ([JCEM 2023, PMID:36321535](https://academic.oup.com/jcem/article/108/4/812/6793767)).

**Risk factors — genetic:** Biallelic CYP27B1 pathogenic variants are both necessary and sufficient (fully penetrant with autosomal recessive inheritance); consanguinity substantially raises risk in outbred populations via increased homozygosity; population founder effects (e.g., French-Canadian SLSJ) create geographically concentrated carrier clusters.

**Risk factors — environmental:** No environmental exposure causes VDDR1A itself (it is a purely monogenic disorder), but vitamin D nutritional status (dietary calciferol intake, sun exposure) modulates the severity and timing of clinical presentation, since substrate (25(OH)D) availability affects how much residual/hypomorphic enzyme activity can generate 1,25(OH)₂D in partial-deficiency genotypes.

**Protective factors:** Hypomorphic ("leaky") CYP27B1 alleles such as p.(Ala129Thr) are protective relative to null alleles, producing later onset and milder biochemical/skeletal disease. No population-level protective environmental factor is documented; adequate vitamin D nutritional status can partially compensate for hypomorphic (but not null) alleles by providing more substrate for residual enzyme activity.

**Gene-environment interactions:** The clearest interaction is that ambient/dietary vitamin D sufficiency provides substrate (25(OH)D) that residual-activity hypomorphic CYP27B1 enzyme can still partially hydroxylate — meaning a child with a partial loss-of-function genotype and good vitamin D status may present later/milder than one who is also nutritionally vitamin D deficient. There is no independent environmental trigger analogous to infection or toxin exposure.

Sources: [PMC6398191](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6398191/) | [PMC9671943](https://pmc.ncbi.nlm.nih.gov/articles/PMC9671943/) | [JCEM PMID:36321535](https://academic.oup.com/jcem/article/108/4/812/6793767)

---

## 3. Phenotypes

**Onset and general pattern:** Affected infants are **normal at birth** (maternal-fetal calcium transfer via placenta is largely 1,25(OH)₂D-independent) and become symptomatic typically between **6 months and 2 years of age** (mean onset ~1.1 ± 0.4 years in one cohort; overall reported range up to ~3 years, occasionally later with hypomorphic alleles) ([PMC9671943](https://pmc.ncbi.nlm.nih.gov/articles/PMC9671943/); Frontiers review [PMC7860650](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7860650/)).

**Symptoms/signs (categorized):**

| Phenotype | HPO suggestion | Frequency (from cohort data) |
|---|---|---|
| Delayed walking / motor delay | HP:0031936 (Delayed ability to walk) | 83.3% (10/12) |
| Short stature / growth retardation | HP:0004322 | 75.0% (9/12); 75% had severe HtSDS < −2 |
| Muscle weakness / hypotonia | HP:0001324 / HP:0001252 | 50.0% (6/12) |
| Recurrent long-bone fractures | HP:0002757 | 33.3% (4/12) |
| Hypocalcemic seizures/tetany | HP:0002014-adjacent; HP:0002378 (tetany) / HP:0032792 | Reported in classic descriptions; absent in one cohort (0/12), present in others (irritability, tetany, seizures common in early series) |
| Bracelet (wrist) deformity | HP:0002645-adjacent (widened wrist) | 91.7% |
| Rib eversion / rachitic rosary | HP:0000921 (rachitic rosary) | 83.3% / 50.0% |
| Leg bowing/deformity (genu varum/valgum) | HP:0002970 / HP:0002816 | 75.0% |
| Pectus carinatum | HP:0000768 | 50.0% |
| Scoliosis | HP:0002650 | 25.0% |
| Frontal bossing | HP:0011330 | Classically described |
| Dental enamel hypoplasia | HP:0006297 | High proportion of adults affected, especially incisors, canines, first molars |
| Widened cranial sutures / posterior flattening of skull | HP:0004422-adjacent | Described |
| Failure to thrive | HP:0001508 | Common presenting feature; mean diagnosis age 13.8 ± 5 months in newborn-screening cohort |

**Laboratory abnormalities (biochemical phenotype)** — the core diagnostic signature:
- **Hypocalcemia** (mean 1.57 ± 0.19 mmol/L vs. reference 2.24–2.74 mmol/L)
- **Hypophosphatemia** (mean 0.87 ± 0.23 mmol/L vs. reference 1.29–1.94 mmol/L) — secondary to PTH-driven renal phosphate wasting
- **Markedly elevated alkaline phosphatase (ALP)** (mean 1629 ± 673 U/L vs. reference 118–390 U/L)
- **Elevated PTH / secondary hyperparathyroidism** (mean 57.8 ± 32.7 pmol/L vs. reference 1.2–7.1 pmol/L)
- **Normal to elevated 25(OH)D** (mean 77.1 ± 18.4 nmol/L; distinguishes VDDR1A from nutritional deficiency and VDDR1B/CYP2R1 deficiency)
- **Low or inappropriately normal 1,25(OH)₂D** — the diagnostic hallmark, given the accompanying secondary hyperparathyroidism and hypocalcemia that should otherwise drive 1,25(OH)₂D up
(Data: [PMC9671943](https://pmc.ncbi.nlm.nih.gov/articles/PMC9671943/))

**Radiographic phenotype:** widened metaphyses, metaphyseal cupping/fraying, generalized decreased bone density, "fuzzy" metaphyseal margins on wrist/knee radiographs — classic rachitic changes; a Rickets Severity Score (RSS) of ~9.0 ± 1.0 at diagnosis in one cohort.

**Severity/progression:** Symptom severity is variable and correlates with residual enzyme activity and age at diagnosis/treatment onset (earlier diagnosis correlates with better height outcome; r = −0.62, p<0.05 between HtSDS and age at diagnosis). Untreated disease is progressive; treated disease shows biochemical normalization within ~3 months but height catch-up is less reliable, especially with poor treatment adherence.

**Quality of life impact:** Untreated/undertreated VDDR1A produces severe skeletal deformity, short stature, impaired mobility (documented case: inability to ambulate independently after 6-year treatment lapse, requiring surgical correction of scoliosis), and dental morbidity. With early, consistent calcitriol therapy, biochemical and most radiographic parameters normalize and QoL approaches normal, though sustained height catch-up occurs in only a minority (27.3% in one long-term cohort) — underscoring the QoL cost of treatment non-adherence, frequently linked to economic/social barriers (58.3% poor long-term compliance in one cohort).

Sources: [PMC9671943 (12-child cohort)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9671943/) | [PMC7860650](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7860650/) | [Craniofacial/dental study](https://link.springer.com/article/10.1007/s00784-017-2149-4) | [GARD](https://rarediseases.info.nih.gov/diseases/17319/vitamin-d-dependent-rickets-type-1)

---

## 4. Genetic/Molecular Information

**Causal gene:** **CYP27B1** (HGNC:2606; OMIM 609506), chromosome 12q14.1, encoding **25-hydroxyvitamin D-1α-hydroxylase (1α-OHase)**, a mitochondrial cytochrome P450 enzyme expressed predominantly in the renal proximal tubule (with documented extrarenal expression, see Section 6).

**Variant landscape:** ~78–100+ distinct pathogenic variants reported (missense, nonsense, frameshift indels, splice-site changes) spanning all coding exons ([PMC6398191](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6398191/); [PLOS ONE PMC4489500](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4489500/)). In one 19-family cohort: 17 variants (11 missense, 3 frameshift, 2 truncating, 1 splice-acceptor site), homozygosity in 58% (11/19) ([JCEM PMID:36321535](https://academic.oup.com/jcem/article/108/4/812/6793767)).

**Variant classification/pathogenicity:** Per ACMG/AMP framework as used in ClinVar — most reported CYP27B1 variants are classified pathogenic/likely pathogenic based on: (1) biochemical loss-of-function assays; (2) segregation with autosomal recessive disease; (3) absence/near-absence in population databases (gnomAD); (4) protein-truncating or highly conserved missense location.

**Functional consequence categories:**
- **Complete loss-of-function (null) alleles** — nonsense, frameshift, splice-disrupting variants that eliminate enzyme activity entirely — associated with classic early-onset, severe phenotype.
- **Partial loss-of-function (hypomorphic) alleles** — e.g., **p.(Ala129Thr)**, retaining ~50% residual catalytic activity — associated with later-onset, milder disease (median age at diagnosis 5.0 vs. 1.2 years; serum calcium 2.26 vs. 1.85 mmol/L; PTH 4.7 vs. 7.5× ULN; ALP 759 vs. 2082 IU/L compared to other genotypes) ([JCEM 2023, PMID:36321535](https://academic.oup.com/jcem/article/108/4/812/6793767)).
- **Enzyme-adrenodoxin interaction-disrupting variants** — e.g., **R459L**, which prevents CYP27B1 from forming its normal electrostatic/sulfide-bridge interaction with adrenodoxin (the mitochondrial electron-donor redox partner), dramatically reducing catalytic turnover; **H441Y**, which disrupts a hydrogen bond with adrenodoxin but only minimally reduces activity — illustrating a structure-function spectrum where different adrenodoxin-interface residues confer different severities ([JCEM PMID unspecified in search, "Adrenodoxin interactions" paper](https://academic.oup.com/jcem/article/101/9/3409/2806729); [Biochemistry, Arg458 mouse study](https://pubs.acs.org/doi/abs/10.1021/bi060072o)).
- **c.590G>A (p.G197D)**: shown to cause aberrant RNA splicing rather than a simple missense effect ([Front Genet, PMC7729158](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7729158/)).

**Modifier genes:** No established modifier loci distinct from CYP27B1 allelic series itself; phenotype variability is chiefly explained by allelic (residual activity) effects rather than trans-acting modifiers, though vitamin D nutritional status functions as a phenotype modifier for hypomorphic genotypes.

**Population/allele frequency:** Individual pathogenic CYP27B1 variants are each very rare in general population databases (gnomAD), consistent with an overall rare autosomal recessive disease (worldwide literature reports ~219 patients cumulatively). The exception is regional founder populations: SLSJ Quebec carrier frequency for c.262delG estimated at **1 in 26–29**, giving a birth prevalence of ~1 in 2,358–2,916 in that region — orders of magnitude above the general-population rate.

**Somatic vs. germline:** VDDR1A is exclusively a germline/constitutional disease; CYP27B1 has been separately studied (and largely excluded) as a candidate tumor-suppressor gene in primary and secondary/tertiary hyperparathyroidism, a distinct somatic-oncology question unrelated to VDDR1A pathogenesis ([PMC2689078](https://pmc.ncbi.nlm.nih.gov/articles/PMC2689078/)).

**Epigenetics/chromosomal abnormalities:** No epigenetic mechanism or chromosomal-scale abnormality (aneuploidy, large CNV, translocation) has been implicated in VDDR1A; it is a classic single-gene, sequence-level Mendelian disorder.

Sources: [OMIM 609506](https://omim.org/entry/609506) | [PMC6398191](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6398191/) | [JCEM PMID:36321535](https://academic.oup.com/jcem/article/108/4/812/6793767) | [JCEM adrenodoxin paper](https://academic.oup.com/jcem/article/101/9/3409/2806729) | [PMC7729158](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7729158/) | [PMC2689078](https://pmc.ncbi.nlm.nih.gov/articles/PMC2689078/)

---

## 5. Environmental Information

VDDR1A is a monogenic disorder with no infectious or toxin etiology. The principal environmental modulator is **vitamin D nutritional status** (dietary intake and sun-exposure-derived cutaneous synthesis), which determines substrate (25(OH)D) supply and thereby modulates severity/timing in patients with hypomorphic (partial-activity) CYP27B1 alleles, though it cannot compensate for null alleles. No occupational, toxin, radiation, or lifestyle risk factor beyond general vitamin D status has been documented in the literature reviewed. No infectious trigger is implicated in disease onset (as distinct from the separate observation that CYP27B1 extrarenal/immune-cell expression participates in granulomatous-disease vitamin D dysregulation, e.g., tuberculosis-associated hypercalcemia — a different clinical phenomenon from VDDR1A itself; see Section 6).

Sources: [PMC7860650](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7860650/) | [Regulation of extrarenal CYP27B1, PMID:24388948](https://pubmed.ncbi.nlm.nih.gov/24388948/)

---

## 6. Mechanism / Pathophysiology

**Causal chain (initial trigger → clinical manifestation):**

1. **Molecular lesion:** Biallelic pathogenic CYP27B1 variants → loss or severe reduction of 25-hydroxyvitamin D-1α-hydroxylase catalytic activity in renal proximal tubule mitochondria (GO molecular function: vitamin D 25-hydroxylase-derivative activity / 1,25-dihydroxyvitamin D synthesis; suggested **GO:0036378** calcitriol biosynthetic process, **GO:0070576** vitamin D 24-hydroxylase-adjacent metabolic pathway context).
2. **Enzymatic mechanism:** CYP27B1 is a mitochondrial cytochrome P450 (Type I, class I) enzyme requiring electron transfer from **NADPH → ferredoxin reductase → adrenodoxin (ferredoxin) → CYP27B1 heme iron** to catalyze C1α-hydroxylation of 25(OH)D₃. Mutations at the CYP27B1-adrenodoxin protein-protein interface (e.g., R459L disrupting the docking interaction, H441Y disrupting a hydrogen bond) impair electron transfer and catalytic turnover, providing a structural basis for the enzymatic loss of function ([Biochemistry, Arg458 study, PMID referenced above]; [JCEM adrenodoxin interaction paper](https://academic.oup.com/jcem/article/101/9/3409/2806729)).
3. **Biochemical consequence:** Failure to convert 25(OH)D to 1,25(OH)₂D (calcitriol) → selective calcitriol deficiency despite normal/elevated precursor 25(OH)D.
4. **Cellular/tissue consequence:** Calcitriol normally binds the vitamin D receptor (VDR, a nuclear hormone receptor/transcription factor) in intestinal enterocytes to upregulate calcium transport proteins (e.g., TRPV6, calbindin-D9k) — calcitriol deficiency causes **intestinal calcium malabsorption**.
5. **Systemic consequence:** Reduced intestinal calcium absorption → **hypocalcemia** → compensatory **secondary hyperparathyroidism** (elevated PTH) → PTH-driven increased renal phosphate clearance → **hypophosphatemia**; combined hypocalcemia/hypophosphatemia → **impaired hydroxyapatite deposition at the growth-plate mineralization front** → **rickets** (in growing bone) with elevated alkaline phosphatase reflecting osteoblast compensatory activity.
6. **End-organ/clinical manifestation:** Growth-plate widening/cupping, skeletal deformity, growth retardation, hypotonia, dental enamel hypoplasia, and (in severe/untreated cases) hypocalcemic tetany/seizures.

This maps closely onto the dismech `defective_skeletal_mineralization` module's **calciopenic arm** — a calcium-deficient (as opposed to phosphopenic or mineralization-inhibitor) route converging on impaired hydroxyapatite deposition at the mineralization front.

**Molecular pathway/GO term suggestions:**
- GO:0036378 — calcitriol biosynthetic process
- GO:0042359 — vitamin D metabolic process
- GO:0070257 — positive regulation of mucus secretion (not relevant) — *omit*
- GO:0006816 — calcium ion transport (downstream, intestinal)
- GO:0004497 — monooxygenase activity (CYP27B1 catalytic activity class)
- GO:0005506 — iron ion binding (heme cofactor)
- GO:0006874 — cellular calcium ion homeostasis (downstream systemic effect)

**Cellular processes involved:** Renal proximal tubular epithelial cell mitochondrial hydroxylation; intestinal enterocyte calcium transport; parathyroid chief cell PTH secretion (compensatory hyperplasia); osteoblast/osteoclast-mediated growth-plate chondro-osseous mineralization (impaired).

**Protein dysfunction:** Loss-of-function via (a) truncation/frameshift eliminating catalytic domain, (b) missense substitutions destabilizing heme-binding or substrate-binding pockets, (c) missense substitutions at the adrenodoxin-docking interface impairing electron transfer, (d) splice-site variants causing aberrant transcript/nonfunctional protein (e.g., c.590G>A/p.G197D causing an RNA splicing error) ([PMC7729158](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7729158/)).

**Biochemical abnormalities:** Enzyme deficiency (1α-hydroxylase); downstream hormonal cascade abnormalities (low calcitriol, compensatory high PTH); secondary electrolyte derangements (hypocalcemia, hypophosphatemia).

**Immune system involvement (extrarenal CYP27B1 biology, contextual):** CYP27B1 is also expressed extrarenally in macrophages, dendritic cells, T and B lymphocytes, and keratinocytes, where it participates in intracrine/paracrine vitamin D signaling relevant to innate/adaptive immune regulation (notably in granulomatous diseases such as tuberculosis, where IFN-γ stimulates and type I interferons inhibit macrophage CYP27B1 activity). This extrarenal pathway is a distinct physiological role from the renal-endocrine axis defective in VDDR1A and is not itself part of VDDR1A pathogenesis, but is mechanistically noteworthy and occasionally causes diagnostic confusion (e.g., a VDDR1A case "mimicking pseudohypoparathyroidism in the presence of active tuberculosis," [PMC11439522](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11439522/)) ([PMID:24388948](https://pubmed.ncbi.nlm.nih.gov/24388948/); [PMID:24314866](https://pubmed.ncbi.nlm.nih.gov/24314866/)).

**Tissue damage mechanism:** Chondro-osseous — defective mineralization of osteoid/growth-plate cartilage matrix (not classic oxidative/ischemic/fibrotic injury) due to insufficient available calcium-phosphate product at the mineralization front.

**Parathyroid biology:** Chronic secondary hyperparathyroidism can, in severe/prolonged untreated or undertreated cases, raise concern for autonomous (tertiary) parathyroid hyperplasia; however, CYP27B1 itself does not appear to function as a classical tumor-suppressor gene in parathyroid adenoma pathogenesis, based on molecular analyses in primary and refractory secondary/tertiary hyperparathyroidism cohorts ([PMC2689078](https://pmc.ncbi.nlm.nih.gov/articles/PMC2689078/)).

**Advanced/omics data:** No large-scale transcriptomic, proteomic, metabolomic, or single-cell/spatial datasets specific to VDDR1A patient tissue were identified in this search; mechanistic insight instead derives from biochemical enzymology (recombinant CYP27B1 kinetics, adrenodoxin-binding assays) and knockout animal models (below).

Sources: [JCEM adrenodoxin paper](https://academic.oup.com/jcem/article/101/9/3409/2806729) | [PMC7729158](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7729158/) | [PMC2689078](https://pmc.ncbi.nlm.nih.gov/articles/PMC2689078/) | [PMID:24388948](https://pubmed.ncbi.nlm.nih.gov/24388948/) | [PMC11439522](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11439522/)

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Skeletal system (growth plates, long bones, ribs, skull) — UBERON:0001434 (skeletal system); Kidney (site of primary enzymatic defect) — UBERON:0002113
- **Secondary:** Parathyroid glands (compensatory hyperplasia) — UBERON:0001132; Intestine (site of impaired calcium absorption, functional target) — UBERON:0000160; Teeth (enamel hypoplasia) — UBERON:0001091; Skull/cranial sutures (widened sutures, frontal bossing) — UBERON:0003129
- **Body systems involved:** Skeletal/musculoskeletal, endocrine (parathyroid-vitamin D axis), gastrointestinal (calcium absorption), and secondarily neuromuscular (hypotonia, tetany/seizures from hypocalcemia)

**Tissue/cell level:**
- Growth plate cartilage / hypertrophic chondrocytes — affected by impaired mineralization (CL:0000058 chondrocyte)
- Osteoblasts (CL:0000062) — compensatory activity reflected in elevated ALP; osteoid accumulation
- Renal proximal tubule epithelial cells (CL:1001016 or CL:0002306 — kidney proximal tubule cell) — site of CYP27B1 enzymatic activity
- Intestinal enterocytes (CL:0000584) — functional target of calcitriol-VDR signaling for calcium transport
- Parathyroid chief cells (CL:0000426) — secondary hyperplasia/hypersecretion of PTH
- Extrarenal: macrophages (CL:0000235), dendritic cells (CL:0000451), T lymphocytes (CL:0000084), B lymphocytes (CL:0000236), keratinocytes (CL:0000312) — sites of extrarenal CYP27B1 expression (not primary to VDDR1A pathology but part of the gene's broader biology)

**Subcellular level:**
- Mitochondria (GO:0005739 mitochondrion) — CYP27B1 is a mitochondrial inner-membrane-associated cytochrome P450 enzyme
- Mitochondrial matrix (site of adrenodoxin/adrenodoxin reductase electron transport chain interaction)

**Localization:** Bilateral/symmetric skeletal involvement (long bones, ribs, wrists, skull); no lateralization reported. Renal involvement is functional (enzymatic), not structural/anatomic (kidneys are not malformed).

Sources: synthesized from clinical descriptions across [PMC9671943](https://pmc.ncbi.nlm.nih.gov/articles/PMC9671943/), [PMC7860650](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7860650/), [craniofacial/dental study](https://link.springer.com/article/10.1007/s00784-017-2149-4)

---

## 8. Temporal Development

**Onset:** Congenitally normal at birth; clinical onset typically **6 months to ~2 years** of age (cohort mean onset 1.1 ± 0.4 years; range up to ~3 years reported); onset pattern is generally **insidious/subacute** (progressive failure to thrive, delayed motor milestones, evolving skeletal deformity) rather than acute, though acute hypocalcemic tetany/seizures can be a presenting event in severe null-allele cases. Milder (hypomorphic-allele) presentations can be delayed to ~5 years or discovered incidentally on family cascade screening.

**Progression:** Without treatment, disease is chronically progressive — worsening skeletal deformity, growth failure, and (rarely) life-threatening hypocalcemia. With calcitriol/alfacalcidol treatment, biochemical parameters (calcium, phosphate, ALP, PTH) normalize within approximately **3 months**; radiographic (rachitic) improvement follows over months to a few years; height catch-up is the slowest-responding and least reliably achieved parameter, and is critically dependent on early treatment initiation and sustained adherence.

**Disease course pattern:** Chronic and lifelong if untreated adherence lapses — the disease is **not self-limited**; discontinuation of therapy (even after years of good control) leads to biologic relapse, as illustrated by a documented case of a child who stopped treatment, was lost to follow-up for 6 years, and returned with severe skeletal deformity, elevated ALP (2662 U/L) and PTH (91.8 pmol/L), and requiring surgical intervention for scoliosis.

**Critical period for intervention:** Diagnosis/treatment initiation timing is inversely correlated with final height outcome (r = −0.62, p<0.05 for HtSDS vs. age at diagnosis) — earlier treatment (including pre-symptomatic initiation via newborn screening in the SLSJ founder population) yields substantially better growth and skeletal outcomes, establishing early infancy/toddlerhood as the critical therapeutic window.

Sources: [PMC9671943](https://pmc.ncbi.nlm.nih.gov/articles/PMC9671943/) | [PMC9120640](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9120640/)

---

## 9. Inheritance and Population

**Inheritance pattern:** **Autosomal recessive**. Both parents are typically obligate heterozygous carriers (asymptomatic); affected individuals carry two pathogenic CYP27B1 alleles (homozygous or compound heterozygous).

**Penetrance:** Complete/full penetrance for biallelic null genotypes; genotype-dependent expressivity for hypomorphic alleles (see below) means "penetrance" in a strict biochemical sense is universal, but clinical severity/age-of-onset varies continuously with residual enzyme activity.

**Expressivity:** **Variable**, correlating with allele-specific residual enzymatic activity — compare classic early/severe null-allele presentation vs. milder, later-onset p.(Ala129Thr) hypomorphic phenotype (older age at diagnosis, higher calcium, lower PTH/ALP, absence of hypotonia/seizures).

**Genetic anticipation:** Not reported/applicable (no repeat-expansion mechanism).

**Germline mosaicism:** Not specifically documented in the reviewed literature for CYP27B1, though theoretically possible for any recessive Mendelian disorder; recurrence-risk counseling follows standard autosomal recessive principles (25% recurrence risk per pregnancy for carrier × carrier couples).

**Founder effects:** Well-documented — the **Saguenay–Lac-Saint-Jean (SLSJ) region of Quebec, Canada** exhibits a strong founder effect for the **c.262delG (p.Val88Trpfs*71)** variant, with a **carrier frequency of 1 in 26–29** and a **birth prevalence of ~1 in 2,358–2,916** (i.e., roughly one affected child born annually in the region) — dramatically higher than the general worldwide rate. Independent founder/common-ancestor patterns (e.g., shared intron-1 mutations among patients from a single city) have also been suggested in other populations, and a regional Chinese hotspot allele (c.1319_1325dupCCCACCC) has been reported in southern China.

**Consanguinity:** A significant contributor in outbred, non-founder populations — the high proportion of homozygous (as opposed to compound heterozygous) genotypes in several case series (41.7–58%) is consistent with parental consanguinity in many reported families, particularly from regions/cultures with higher consanguinity rates.

**Carrier frequency:** ~1 in 26–29 in the SLSJ founder population (markedly elevated); general-population carrier frequency is not well established given overall rarity but is presumably very low (<<1%) outside founder clusters.

**Epidemiology (prevalence/incidence):**
- Overall exceedingly rare worldwide: **~219 patients** reported in the cumulative literature (per one synthesis).
- **Denmark:** prevalence among children <15 years estimated at **1/250,000**.
- **SLSJ, Quebec:** prevalence at birth estimated at **1 in 2,358** (regional founder-effect outlier).
- No formal Global Burden of Disease (GBD) or large national-registry incidence estimate exists given the disease's rarity; most epidemiologic knowledge is derived from case-series aggregation and the SLSJ founder registry.

**Population demographics:** No strong sex predilection is reported (autosomal recessive; one cohort reported exactly 1:1 male:female ratio, 6/6). Ethnic/geographic clustering reflects founder populations (French-Canadian SLSJ; regional hotspots in southern China) and consanguineous communities (e.g., Middle Eastern, Central/South Asian populations, based on the geographic spread of case reports including Uzbekistan, Vietnam, and others cited in the literature search).

Sources: [OMIM #264700](https://omim.org/entry/264700) | [Orphanet ORPHA289157](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Expert=289157&lng=EN) | [PMC9120640](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9120640/) | [PMC9671943](https://pmc.ncbi.nlm.nih.gov/articles/PMC9671943/) | [Cruz Marino 2023, AJMG-A](https://onlinelibrary.wiley.com/doi/10.1002/ajmg.a.63147)

---

## 10. Diagnostics

**Core biochemical panel (LOINC-codeable):**
- Serum calcium (low) — LOINC 17861-6
- Serum phosphate (low)
- Serum alkaline phosphatase (markedly elevated)
- Serum intact PTH (markedly elevated)
- 25-hydroxyvitamin D (normal or elevated — key discriminator from nutritional deficiency and VDDR1B)
- **1,25-dihydroxyvitamin D (calcitriol)** — low or inappropriately normal given the concurrent hypocalcemia/hyperparathyroidism that should otherwise drive it up; this is the single most discriminating biochemical test
- Urinary calcium/creatinine ratio (for monitoring hypercalciuria risk during treatment)

**Imaging:**
- Wrist and knee radiographs — widened epiphyses/metaphyses, metaphyseal cupping and fraying, generalized decreased bone density; graded via a Rickets Severity Score (RSS)
- Renal ultrasound — baseline and monitoring for nephrocalcinosis (a treatment-related risk), performed at diagnosis and every 1–2 years thereafter (more frequently if hypercalciuria develops)
- Skull imaging may show widened sutures, posterior flattening

**Genetic testing:**
- **Single-gene CYP27B1 sequencing** (Sanger or targeted NGS) is the definitive diagnostic test given the disorder's clean genotype-phenotype relationship; a **skeletal dysplasia/rickets gene panel** (including CYP27B1, CYP2R1, VDR, PHEX, DMP1, FGF23, ENPP1, SLC34A3, etc.) is commonly used clinically to differentiate the vitamin D-dependent and hypophosphatemic rickets spectrum. Whole-exome sequencing is increasingly used, especially in atypical or apparently sporadic presentations.
- Biochemical phenotype (low/inappropriately-normal 1,25(OH)₂D with normal/high 25(OH)D) strongly predicts CYP27B1 involvement prior to sequencing.

**Newborn screening:** A **prospective newborn genetic screening program** has been implemented in the SLSJ founder population (targeting the c.262delG founder allele), demonstrated to be safe, feasible, and efficient; pre-symptomatic identification allows calcitriol initiation before clinical manifestations develop, improving growth/skeletal outcomes ([PMC9120640](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9120640/)).

**Differential diagnosis:**
| Condition | Distinguishing feature vs. VDDR1A |
|---|---|
| **Nutritional vitamin D deficiency rickets** | Low 25(OH)D (vs. normal/high in VDDR1A); responds to standard vitamin D supplementation |
| **VDDR1B (CYP2R1 deficiency, 25-hydroxylase)** | Deficient 25(OH)D (upstream hydroxylation defect); may show gene-dosage/heterozygous partial phenotypes improving with age; can respond to calcifediol bypassing the block |
| **VDDR2A (VDR mutations, hereditary vitamin D-resistant rickets)** | Markedly *elevated* 1,25(OH)₂D (end-organ resistance, not deficiency); alopecia in ~50% of cases (absent in VDDR1A); requires massive calcitriol doses or IV calcium; may show dramatic post-pubertal improvement in calcium absorption |
| **X-linked hypophosphatemic rickets (PHEX)/other FGF23-mediated hypophosphatemic rickets** | Normal PTH and normal/low-normal calcium (vs. VDDR1A's elevated PTH and low calcium); phosphopenic rather than calciopenic mechanism |
| **Hypoparathyroidism/pseudohypoparathyroidism** | Low or inappropriately normal PTH (hypoPTH) or PTH resistance with characteristic Albright hereditary osteodystrophy features (pseudoHP) — VDDR1A shows appropriately *elevated* PTH; misdiagnosis as normocalcemic primary hyperparathyroidism or pseudohypoparathyroidism has been reported due to overlapping biochemistry in atypical presentations |

**Diagnostic pitfalls documented in the literature:** VDDR1A has been misdiagnosed as nutritional rickets, hypophosphatemic rickets, pseudohypoparathyroidism (including in the setting of concurrent active tuberculosis, where extrarenal CYP27B1 activity in granulomas confounds vitamin D metabolite interpretation), and normocalcemic primary hyperparathyroidism — underscoring the value of genetic confirmation.

Sources: [PMC11439522](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11439522/) | [JCEM Case Reports, PMID misdiagnosis paper](https://academic.oup.com/jcemcr/article/1/4/luad084/7224021) | [PMC9120640](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9120640/) | [Frontiers diagnosis/management review](https://www.frontiersin.org/journals/pediatrics/articles/10.3389/fped.2020.00315/full)

---

## 11. Outcome/Prognosis

**Survival/mortality:** With timely diagnosis and appropriate calcitriol replacement, VDDR1A is **not a life-shortening condition**; mortality risk is essentially confined to acute, severe, untreated hypocalcemia (tetany/seizures/cardiac effects) in infancy, which is preventable with treatment. No formal survival/life-expectancy statistics were identified, consistent with the expectation of near-normal life expectancy on treatment.

**Morbidity/functional outcomes:**
- **Biochemical normalization** is generally achieved within ~3 months of appropriate calcitriol/calcium therapy.
- **Radiographic (rachitic) improvement** follows, with RSS improving significantly with good adherence (e.g., from 8.6 ± 1.0 to 3.7 ± 3.4 in one cohort, p<0.05).
- **Growth/height outcome is the most treatment-resistant domain:** initial catch-up growth occurs in ~91% of patients in the first few years, but *sustained* catch-up to normal height was maintained in only ~27% at last follow-up in one long-term cohort; persistent short stature (HtSDS < −2) affected 63.6% at last visit. Biochemical normalization does **not** guarantee height recovery.
- **Renal outcomes:** No nephrocalcinosis was observed in a 12-patient cohort with appropriate calcitriol dosing over a mean 6.2-year follow-up (one patient had enhanced kidney echogenicity only), suggesting that with careful monitoring the treatment-related hypercalciuria/nephrocalcinosis risk (a concern for all calcitriol-treated rachitic disorders) can be managed effectively.

**Complications:** Severe/relapsed disease (from treatment discontinuation) can require **orthopedic surgical intervention** (e.g., for severe scoliosis); dental enamel hypoplasia is a persistent complication even with adequate systemic treatment; secondary/occasionally severe hyperparathyroidism can develop with chronic undertreatment, raising a theoretical (though apparently uncommon) concern for progression toward parathyroid autonomy.

**Prognostic factors:** The dominant modifiable prognostic factor is **age at diagnosis/treatment initiation** (earlier = better height outcome) and **long-term treatment adherence** (the primary determinant of sustained skeletal/growth benefit — cited reasons for poor adherence include economic constraints, social problems, inadequate medical education, and adolescent psychosocial issues). Genotype (null vs. hypomorphic allele, e.g., p.(Ala129Thr)) is a non-modifiable prognostic factor correlating with baseline severity and, indirectly, with the degree of catch-up needed.

Sources: [PMC9671943](https://pmc.ncbi.nlm.nih.gov/articles/PMC9671943/) | [JCEM PMID:36321535](https://academic.oup.com/jcem/article/108/4/812/6793767)

---

## 12. Treatment

**Pharmacotherapy — mainstay of treatment:**
- **Calcitriol (1,25-dihydroxyvitamin D₃)** is the **first-line, definitive replacement therapy**, since it bypasses the defective 1α-hydroxylation step entirely.
  - **Initial/loading dose:** commonly 1–2 μg/day (some protocols 1–1.5 μg twice daily); pediatric cohort dosing reported as low as 0.25–0.5 μg/day depending on severity and body size, titrated to response.
  - **Maintenance dose:** typically **0.25–1 μg/day** (ranges cited 0.3–2 μg/day), given in divided (twice-daily) doses owing to calcitriol's short biological half-life.
  - **Calcium supplementation** is co-administered, especially during the initial "hungry bone" remineralization phase (guidance cited: ~50 mg/kg/day elemental calcium in children; cohort doses of 500–1000 mg/day).
- **Alternative agents:** **1α-hydroxyvitamin D (alfacalcidol/1α-OH-D₃)** — a prodrug requiring only hepatic 25-hydroxylation (which is intact in VDDR1A) to become active — offers a longer half-life allowing once-daily dosing and is widely used, particularly in European cohorts (e.g., the 19-family JCEM genotype-phenotype cohort was treated with alfacalcidol). **Eldecalcitol** has shown superior osteogenic promotion versus alfacalcidol in the Cyp27b1-knockout mouse model (preclinical, not yet standard human therapy).
- **Therapeutic agent ontology:** calcitriol (CHEBI:17823), alfacalcidol (CHEBI equivalent), calcium carbonate/citrate (elemental calcium supplementation).
- **NCIT treatment term suggestions:** NCIT:C15986 (Pharmacotherapy) as the generic action, with `therapeutic_agent` bound to calcitriol/alfacalcidol.

**Treatment goals:** Achieve normocalcemia, maintain PTH within normal limits, avoid hypercalciuria/nephrocalcinosis, and normalize radiographic/growth parameters.

**Monitoring protocol:** Serum calcium, phosphorus, PTH, alkaline phosphatase, creatinine, and vitamin D metabolites every 3–6 months; 24-hour urinary calcium or spot calcium:creatinine ratio; renal ultrasound every 1–2 years (more frequently if hypercalciuria present); annual wrist/knee radiographs during active growth.

**Duration:** **Lifelong** — "treatment must be continued indefinitely"; discontinuation reliably leads to biochemical and skeletal relapse (documented case of a 6-year treatment lapse producing severe deformity requiring surgery).

**Surgical/interventional care:** Orthopedic surgical correction may be required for severe, established skeletal deformities (e.g., scoliosis) in patients with delayed diagnosis or prolonged non-adherence.

**Supportive/rehabilitative care:** Nutritional counseling to support adequate dietary calcium/vitamin D intake; physical therapy may be used adjunctively for motor delay/deformity-related functional limitation (NCIT:C15302, Physical Therapy), though this is not emphasized as a primary modality in the literature reviewed.

**Genetic counseling:** Recommended for families given autosomal recessive inheritance and (in founder populations) availability of targeted carrier/newborn screening; NCIT:C15240 (Genetic Counseling).

**Experimental/investigational therapies:** No gene therapy, RNA-based therapy, or novel targeted biologic specific to VDDR1A was identified in this search — enzyme-replacement is achieved pragmatically via direct hormone (calcitriol) replacement rather than protein or gene-based correction, which is feasible precisely because the deficient product (calcitriol) itself is an inexpensive, orally bioavailable small molecule.

**Treatment response/outcomes:** Excellent biochemical and radiographic response rates with adherent therapy; the principal "failure mode" is non-adherence rather than pharmacologic non-response — reinforcing that VDDR1A is, mechanistically, a highly treatable condition once diagnosed.

Sources: [PMC9671943](https://pmc.ncbi.nlm.nih.gov/articles/PMC9671943/) | [Frontiers diagnosis/management review](https://www.frontiersin.org/journals/pediatrics/articles/10.3389/fped.2020.00315/full) | [JCEM PMID:36321535](https://academic.oup.com/jcem/article/108/4/812/6793767) | [Calcitriol treatment, ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/002604959090264D) | [Eldecalcitol vs alfacalcidol mouse study, PMC6169848](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6169848/)

---

## 13. Prevention

**Primary prevention:** Not applicable in the classic sense (this is a genetic, not an acquired/exposure-based disease), but **pre-symptomatic treatment initiation via newborn/carrier screening** in founder populations effectively prevents the clinical manifestations of the disease from ever developing — the SLSJ program demonstrates that daily calcitriol initiated before symptom onset can prevent the phenotype entirely.

**Secondary prevention/screening:**
- **Targeted newborn genetic screening** for the founder c.262delG variant in the SLSJ Quebec population — shown safe, feasible, and effective at enabling pre-symptomatic treatment.
- **Carrier screening / cascade family testing** is recommended in founder populations and in families with an index case, given the high carrier frequency locally (1/26–29 in SLSJ) and the straightforward single-gene test.
- General population newborn screening for VDDR1A is not standard practice outside founder/high-prevalence populations, given the disease's overall rarity.

**Tertiary prevention:** Once diagnosed, ongoing monitoring (per Section 12) prevents complications (nephrocalcinosis, severe deformity, growth failure) and enables early detection/correction of relapse from non-adherence.

**Genetic counseling:** Central to prevention strategy in affected families and in founder communities — informing reproductive risk (25% recurrence for carrier couples) and enabling prenatal or preimplantation genetic testing where desired.

**Public health interventions:** No population-wide public health intervention (e.g., water fortification, mass supplementation) is applicable, since VDDR1A is refractory to standard vitamin D supplementation (the defect is downstream of 25(OH)D availability) — this is an important practical distinction from nutritional rickets prevention programs.

**Prophylaxis:** N/A beyond the therapeutic calcitriol regimen itself, which functions simultaneously as treatment and (when started pre-symptomatically) as prevention of phenotypic expression.

Sources: [PMC9120640](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9120640/)

---

## 14. Other Species / Natural Disease

**Naturally occurring VDDR1A in companion animals — a well-characterized comparative model:**
- **Dogs (Canis lupus familiaris, NCBI Taxon:9615):** Naturally occurring CYP27B1-mutation vitamin D-dependent rickets type IA has been documented in **pugs** and **Saint Bernards**, catalogued in **OMIA:000837-9615** ([OMIA](https://omia.org/OMIA000837/9615/)). A 2023 study identified a **stop-gain mutation (chr10:2182971G>T)** in CYP27B1 in affected pugs, causing premature truncation at codon 87 (loss of ~83% of the protein), producing a clinical phenotype "indistinguishable" from nutritional vitamin D deficiency and **life-threatening if untreated** in young pugs ([J Vet Intern Med 2023, PMID:37293695](https://pubmed.ncbi.nlm.nih.gov/37293695/); [PMC10365047](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10365047/)).
- **Breed relevance (VBO):** Pug and Saint Bernard breeds are specifically documented; this represents genuine veterinary clinical importance (a naturally arising, breed-associated inherited disease) rather than only a laboratory-induced model.

**Comparative biology:** The canine phenotype recapitulates the core human biochemical and skeletal signature (hypocalcemia, secondary hyperparathyroidism, rachitic bone disease), supporting deep evolutionary conservation of the CYP27B1-vitamin D endocrine axis across mammals. No zoonotic or transmission relevance applies — this is a purely genetic, non-communicable disease in both species.

**No non-mammalian natural disease models identified** in this search (the vitamin D endocrine/calcitriol-VDR axis is a vertebrate, largely mammalian/avian physiological system, but naturally occurring CYP27B1-deficiency disease was not found reported outside canines in the literature surveyed).

Sources: [OMIA:000837-9615](https://omia.org/OMIA000837/9615/) | [J Vet Intern Med, PMID:37293695](https://pubmed.ncbi.nlm.nih.gov/37293695/) | [PMC10365047](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10365047/)

---

## 15. Model Organisms

**Mouse (Mus musculus) — Cyp27b1 knockout:**
- **Model type:** Targeted gene-knockout (constitutive), the principal genetic animal model of VDDR1A/pseudo-vitamin-D-deficiency rickets.
- **Phenotype recapitulation:** Cyp27b1-knockout mice develop **hypocalcemia, hypophosphatemia, secondary hyperparathyroidism, and short, deformed bones with dysmorphic growth plates** — closely mirroring the human biochemical and skeletal phenotype. After weaning, mice show marked hypocalcemia and high PTH with decreased growth, osteodystrophy (bone hypocalcification), and growth-plate cartilage hypertrophy.
- **Rescue experiments:** Treatment with exogenous **1,25-dihydroxyvitamin D₃ (calcitriol)** rescues the pseudo-vitamin-D-deficiency-rickets phenotype in Cyp27b1-deficient mice — confirmed via biochemical, histomorphometric, and biomechanical analyses (PMID:12674324) — directly validating calcitriol replacement as mechanistically corrective, mirroring the human standard-of-care.
- **Comparative model characteristics:** The mineral/skeletal phenotype of Cyp27b1-KO mice is **more severe** than that of Vdr-KO mice (VDDR2A model) and, notably, **cannot be fully rescued by a "rescue diet" high in calcium, phosphate, and lactose** — a diet strategy that *does* substantially normalize the Vdr-KO phenotype — highlighting a biologically meaningful difference between the ligand-deficiency (VDDR1A) and receptor-resistance (VDDR2A) mechanisms even though both converge on impaired VDR signaling output ([Bone Research 2024](https://www.nature.com/articles/s41413-024-00343-7)).
- **Model limitations:** As with all knockout models, developmental compensation and species-specific differences in mineral handling/diet (rodent vs. human) limit direct translational fidelity, particularly regarding the precise growth/height catch-up dynamics seen in human patients on treatment.
- **Applications:** Studying calcitriol-VDR axis physiology, comparing therapeutic vitamin D analogs (e.g., eldecalcitol vs. alfacalcidol — eldecalcitol showed superior osteogenic promotion in Cyp27b1-KO mice, [PMC6169848](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6169848/)), and dissecting genetic vs. dietary rescue strategies.

**Rat (Rattus norvegicus):** Novel genetically modified rat models (including Vdr-KO rats) have been generated to further probe molecular mechanisms of vitamin D action; Vdr-KO rats notably show alopecia (as in human VDDR2A) — a feature that, by contrast, is **absent** in CYP27B1-deficient animals (and in human VDDR1A), reinforcing alopecia as a VDR-signaling/receptor-pathway-specific (not ligand-deficiency) feature ([Sci Rep, PMC7105495](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7105495/)).

**Naturally occurring large-animal model:** The pug/Saint Bernard dog model (Section 14) functions additionally as a valuable **spontaneous (non-engineered)** genetic model, complementing the engineered mouse knockout, particularly for large-animal/companion-animal translational and veterinary-clinical study.

**Cellular/in vitro models:** Recombinant CYP27B1 expression systems (e.g., in bacterial or mammalian expression systems) have been used extensively for structure-function mutagenesis studies (e.g., Arg458/Arg459 adrenodoxin-interaction mutants) to dissect enzyme kinetics and electron-transfer partner interactions at the molecular level, though these are biochemical rather than whole-cell disease models.

**Model databases:** MGI (Mouse Genome Informatics) for Cyp27b1 mouse alleles; OMIA for the canine model; no zebrafish, Drosophila, C. elegans, or yeast VDDR1A-specific model was identified (unsurprising, given the mammalian-specific renal-endocrine vitamin D axis).

Sources: [Bone Research 2024, Nature](https://www.nature.com/articles/s41413-024-00343-7) | [PMID:12674324 (rescue study)](https://pubmed.ncbi.nlm.nih.gov/12674324/) | [PMC6169848 (eldecalcitol study)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6169848/) | [PMC7105495 (rat models)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7105495/) | [OMIA:000837-9615](https://omia.org/OMIA000837/9615/)

---

## Summary Ontology Term Suggestions

| Category | Suggested terms |
|---|---|
| **MONDO/Disease** | ORPHA:289157; consider MONDO term for VDDR1A specifically (verify exact MONDO CURIE via OAK before curating) |
| **HGNC gene** | hgnc:2606 (CYP27B1) |
| **HP phenotypes** | HP:0002748 (Rickets, if using generic term) or defer to `defective_skeletal_mineralization` module conformance; HP:0002014-adjacent hypocalcemia terms; HP:0004322 (Short stature); HP:0001324 (Muscle weakness); HP:0001252 (Hypotonia); HP:0002757 (Recurrent fractures); HP:0000921 (Rachitic rosary); HP:0011330 (Frontal bossing); HP:0006297 (Dental enamel hypoplasia); HP:0002650 (Scoliosis); HP:0000768 (Pectus carinatum) |
| **GO biological process** | GO:0036378 (calcitriol biosynthetic process); GO:0042359 (vitamin D metabolic process); GO:0006874 (cellular calcium ion homeostasis) |
| **GO cellular component** | GO:0005739 (mitochondrion) |
| **CL cell types** | CL:0002306 (kidney proximal tubule cell — verify exact ID); CL:0000584 (enterocyte); CL:0000426 (parathyroid chief cell); CL:0000058 (chondrocyte); CL:0000062 (osteoblast) |
| **UBERON** | UBERON:0002113 (kidney); UBERON:0001434 (skeletal system); UBERON:0001132 (parathyroid gland); UBERON:0000160 (intestine) |
| **CHEBI** | Calcitriol; alfacalcidol; calcium (verify exact CHEBI CURIEs via OAK) |
| **NCIT treatment** | NCIT:C15986 (Pharmacotherapy) + therapeutic_agent (calcitriol) |
| **NCBITaxon (models)** | NCBITaxon:10090 (Mus musculus); NCBITaxon:9615 (Canis lupus familiaris) |

*(Per dismech convention, all suggested ontology terms should be independently verified via OAK — `runoak -i sqlite:obo:<ontology> info <CURIE> -O obo` — before use in curation, to guard against label mismatch or hallucination.)*

---

## Master Source List

- [OMIM #264700 — VDDR1A](https://omim.org/entry/264700)
- [OMIM 609506 — CYP27B1](https://omim.org/entry/609506)
- [OMIM #277440 — VDDR2A](https://www.omim.org/entry/277440)
- [Orphanet ORPHA289157](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Expert=289157&lng=EN)
- [GARD — Vitamin D-dependent rickets, type 1](https://rarediseases.info.nih.gov/diseases/17319/vitamin-d-dependent-rickets-type-1)
- [ICD-10-CM E83.32](https://www.icd10data.com/ICD10CM/Codes/E00-E89/E70-E88/E83-/E83.32)
- Sørensen KV et al. — [PLOS ONE / PMC4489500, Novel CYP27B1 Gene Mutations](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4489500/)
- Peng et al., Front Pediatr 2022, PMID:36405822 — [12-child Chinese cohort, PMC9671943](https://pmc.ncbi.nlm.nih.gov/articles/PMC9671943/)
- Molin/Kaufmann et al. — [Genetic and clinical characteristics of VDDR1A patients, PMC6398191](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6398191/)
- [Benefits of Newborn Screening for VDDR1A in a Founder Population, PMC9120640](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9120640/)
- Fauquier/Colin et al., JCEM 2023, PMID:36321535 — [CYP27B1 p.(Ala129Thr) Genotype-Phenotype, JCEM](https://academic.oup.com/jcem/article/108/4/812/6793767)
- Kim CJ et al., JCEM — [CYP27B1 Adrenodoxin Interaction Mutations](https://academic.oup.com/jcem/article/101/9/3409/2806729)
- [Molecular Analysis: c.590G>A p.G197D Splicing Error, PMC7729158](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7729158/)
- [CYP27B1 as candidate tumor suppressor in hyperparathyroidism, PMC2689078](https://pmc.ncbi.nlm.nih.gov/articles/PMC2689078/)
- [Regulation of extrarenal CYP27B1-hydroxylase, PMID:24388948](https://pubmed.ncbi.nlm.nih.gov/24388948/)
- [Murine CD8+ T cells express vitamin D 1α-hydroxylase, PMID:24314866](https://pubmed.ncbi.nlm.nih.gov/24314866/)
- [VDDR1A Mimicking Pseudohypoparathyroidism with Active TB, PMC11439522](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11439522/)
- [Craniofacial and dental characteristics of VDDR1A, Clin Oral Investig](https://link.springer.com/article/10.1007/s00784-017-2149-4)
- [Diagnosis and Management of Vitamin D Dependent Rickets, Front Pediatr](https://www.frontiersin.org/journals/pediatrics/articles/10.3389/fped.2020.00315/full)
- [Coactivator-independent VDR signaling causes severe rickets in mice, Bone Research 2024](https://www.nature.com/articles/s41413-024-00343-7)
- [Rescue of pseudo-VDDR phenotype in Cyp27b1-KO mice, PMID:12674324](https://pubmed.ncbi.nlm.nih.gov/12674324/)
- [Eldecalcitol vs alfacalcidol in Cyp27b1-KO mice, PMC6169848](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6169848/)
- [Generation of genetically modified rats for vitamin D action, PMC7105495](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7105495/)
- [Mutations in CYP27B1 cause VDDR in pugs, J Vet Intern Med, PMID:37293695 / PMC10365047](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10365047/)
- [OMIA:000837-9615 — Vitamin D-deficiency rickets, type IA in dog](https://omia.org/OMIA000837/9615/)
- [Cruz Marino et al. 2023, AJMG-A — SLSJ founder population autosomal recessive diseases](https://onlinelibrary.wiley.com/doi/10.1002/ajmg.a.63147)
- [MalaCards — VDDR1A](https://www.malacards.org/card/vitamin_d_hydroxylation_deficient_rickets_type_1a)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 21 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 21 |
| On topic | 14 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMC:PMC11439522` *(abstract only)*: "mimicking pseudohypoparathyroidism in the presence of active tuberculosis,"
  - closest text in source: "This report describes a case of vitamin D-dependent rickets type 1A, mimicking pseudohypoparathyroidism owing to presence of concurrent illness like extrapulmonary tuberculosis."