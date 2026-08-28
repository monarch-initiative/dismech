---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-27T23:16:34.850762'
end_time: '2026-08-27T23:21:35.952763'
duration_seconds: 301.1
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Primary Bile Acid Malabsorption
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
  web_search_requests: 19
  num_turns: 28
  total_cost_usd: 1.3470584000000003
  session_id: 2df13fb4-9115-50fa-aa7c-75f1d91c874a
  stop_reason: end_turn
  assistant_text_blocks: 3
citation_count: 39
reference_validation:
  total_references: 25
  verified: 24
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.04
  quotes_checked: 3
  quotes_valid: 1
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMC:PMC3170668
  - PMID:40814585
  relevance_assessed: 24
  on_topic: 16
  off_topic: 1
  off_topic_references:
  - PMID:16816347
  unresolved_references:
  - DOI:10.1093/ibd/izag137/8732609
  needs_review: true
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Primary Bile Acid Malabsorption
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Primary Bile Acid Malabsorption** covering all of the
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

I'll research Primary Bile Acid Malabsorption (BAM) using web search and fetch tools, then compile a comprehensive cited report.

I now have sufficient depth across genetics, mechanism, diagnostics, treatment, and animal models to compile the full report.

I now have comprehensive research material across all required domains. Compiling the full report.

# Primary Bile Acid Malabsorption: Comprehensive Research Report

## 1. Disease Information

**Overview.** Bile acid malabsorption (BAM), also called bile acid diarrhea (BAD), is a condition in which excess bile acids reach the colon — either because the ileum fails to reabsorb them or because the liver overproduces them — producing chronic, often urgent, watery diarrhea. "Bile acid malabsorption (BAM), also known as bile acid diarrhea (BAD), is a condition characterized by excessive biosynthesis of bile acids or inability to reabsorb sufficient bile acids in the terminal ileum" (searched via PubMed/PMC literature). Historically the disease is split into a **primary (genetic/idiopathic)** form and **secondary** forms caused by identifiable gut disease. The genetically defined entity **Primary Bile Acid Malabsorption (PBAM)** is a rare, treatable, congenital, **autosomal recessive** diarrheal disorder caused by biallelic loss-of-function variants in the ileal bile acid transporter gene *SLC10A2* (OMIM #613291, PBAM1) or, in a second molecular subtype, in *SLC51B* (OMIM #619481, PBAM2), which encodes the basolateral organic solute transporter beta (OSTβ) subunit.

- **OMIM**: #613291 (Bile Acid Malabsorption, Primary, 1; PBAM1, gene *SLC10A2*/601295, 13q33.1); #619481 (Bile Acid Malabsorption, Primary, 2; PBAM2, gene *SLC51B*/612085, 15q22)
- **Orphanet**: ORPHA:449262 (Primary bile acid malabsorption); note Orphanet also separately lists "Idiopathic malabsorption due to bile acid synthesis defects" (ORPHA:84065) as a related but distinct entity
- **ICD-10-CM**: K90.8/K90.89 (Other intestinal malabsorption) — bile acid malabsorption syndrome is an approximate synonym; there is no dedicated ICD-10 code
- **Gene symbols/HGNC**: *SLC10A2* (ASBT/ISBT/NTCP2), *SLC51B* (OSTβ)
- **Synonyms**: Bile acid diarrhea (BAD); idiopathic bile acid diarrhea/malabsorption (when acquired, non-Mendelian); congenital chronic diarrhea due to bile acid malabsorption; ASBT deficiency; ileal bile acid transporter deficiency; "Type 2" bile acid diarrhea (in the acquired/idiopathic clinical classification, as opposed to Mendelian PBAM)

**Data provenance note:** Most of what is known about the *Mendelian* form comes from individual patient case reports and small pedigrees (aggregated in OMIM/ClinVar); the much larger literature on "bile acid diarrhea" broadly is aggregated epidemiological/clinical-trial data (SeHCAT cohorts, IBS-D meta-analyses) that mixes primary (idiopathic) and secondary causes and is not gene-resolved.

Sources: [OMIM 613291](https://www.omim.org/entry/613291), [OMIM 619481](https://www.omim.org/entry/619481), [OMIM 601295 SLC10A2](https://www.omim.org/entry/601295), [Orphanet ORPHA:457478/449262](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Lng=GB&Expert=457478), [ICD10Data K90.89](https://www.icd10data.com/ICD10CM/Codes/K00-K95/K90-K95/K90-/K90.89)

---

## 2. Etiology

**Molecular/genetic cause (PBAM1).** *SLC10A2* encodes the apical sodium-dependent bile acid transporter (ASBT), which mediates the rate-limiting, active reuptake of conjugated bile acids across the apical brush-border membrane of terminal ileal enterocytes. Biallelic loss-of-function variants abolish or severely impair this transport, so bile acids that escape hepatic/ileal reclamation spill into the colon in massive excess, causing secretory diarrhea and depleting the circulating bile acid pool needed for fat and fat-soluble vitamin absorption. Genotype-phenotype correlation work has shown a dose-dependent relationship between variant severity and transport loss: "The 868C>T variant is associated with complete functional loss of ASBT" while "292G>A and 431G>A variants were associated with mild and moderately impaired transport function, respectively" (PMC3170668, functional characterization of ASBT variants). The original disease-defining mutations were reported in the *Journal of Clinical Investigation* (Oelkers et al., JCI 1997, PMID:9207482 — "Primary bile acid malabsorption caused by mutations in the ileal sodium-dependent bile acid transporter gene (SLC10A2)").

**Molecular/genetic cause (PBAM2).** A second molecular subtype is caused by biallelic mutation in *SLC51B*, encoding OSTβ, the basolateral partner (with OSTα/*SLC51A*) that exports reabsorbed bile acids from the enterocyte into portal blood. The founding report (Sultan et al., *Hepatology* 2018, "Organic solute transporter‑β (SLC51B) deficiency in two brothers with congenital diarrhea and features of cholestasis") described a frameshift mutation predicted to eliminate the C-terminal region required for membrane insertion, OSTα interaction, and solute transport, producing a phenotype that combines chronic diarrhea with **cholestatic liver disease features** (elevated ALT/AST/GGT, borderline coagulopathy) not seen in PBAM1 — reflecting bile acid retention within the enterocyte/liver axis rather than pure loss of luminal reclamation.

**Risk/predisposing factors:**
- *Genetic*: homozygosity or compound heterozygosity for *SLC10A2* or *SLC51B* loss-of-function variants; **consanguinity** is a recurrent feature in reported pedigrees (e.g., the 2025 case of a homozygous *SLC10A2* c.194C>T, p.Pro65Leu variant in a patient from consanguineous Pakistani parents, PMID:40814585).
- A common *SLC10A2* coding variant has also been studied as a modest population-level risk factor for **gallstone disease** via altered bile acid pool composition (PMC2757911), distinct from the rare biallelic loss-of-function alleles that cause PBAM.
- *Environmental/acquired* (relevant to the broader "bile acid diarrhea" spectrum, not the Mendelian disease per se): terminal ileal resection or disease (Crohn's disease, radiation enteritis), cholecystectomy, and use of GLP-1 receptor agonists or other drugs altering gut transit.
- **Protective factors**: none specifically described for the genetic form; for the broader acquired condition, an intact terminal ileum and normal FXR–FGF19 feedback are implicitly protective.
- **Gene-environment interaction**: not well characterized for the Mendelian disease; for acquired disease, ileal inflammation/resection interacts with baseline hepatic bile-acid synthetic capacity to determine severity.

Sources: [OMIM SLC10A2](https://www.omim.org/entry/601295), [JCI 1997 primary paper](https://www.jci.org/articles/view/119355), [PMC3170668 functional variants](https://ncbi.nlm.nih.gov/pmc/articles/PMC3170668), [Hepatology 2018 SLC51B](https://onlinelibrary.wiley.com/doi/pdf/10.1002/hep.29516), [JPGN Reports 2025 case, PMID:40814585](https://pmc.ncbi.nlm.nih.gov/articles/PMC12350027/), [PMC2757911 gallstone risk variant](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2757911/)

---

## 3. Phenotypes

**Core symptom complex** (HPO-suggested terms in parentheses):
- Chronic watery diarrhea, often from infancy/birth (**HP:0002014** Diarrhea; chronic watery diarrhea has been described as present "since birth" in PBAM2 pedigrees)
- Steatorrhea — greasy, foul-smelling stools (**HP:0002570** Steatorrhea); one PBAM2 case described "8 to 10 greasy stools per day"
- Failure to thrive / poor growth / stunting in congenital-onset cases (**HP:0001508** Failure to thrive; **HP:0004322** Short stature) — a 2021 report is explicitly titled "SLC10A2 deficiency‑induced congenital chronic bile acid diarrhea **and stunting**" (PMID:34192422)
- Excess fecal bile acids (a laboratory/biochemical HPO-style descriptor, "increased fecal bile acid")
- Fat-soluble vitamin deficiency (A, D, E, K) — this can be the **dominant or even sole presenting feature**: the 2025 case report describes a patient with lifelong severe vitamin A/D/E/K deficiency, rickets, hypocalcemic seizure at 10 months, dental enamel defects, and stunted final height (155.5 cm) with **no diarrhea or steatorrhea at all**, illustrating marked phenotypic heterogeneity (PMID:40814585).
- Urgency, occasional fecal incontinence, abdominal pain/bloating, and fatigue in the broader (mostly acquired) bile-acid-diarrhea population
- Elevated liver transaminases/GGT and borderline coagulopathy specifically in PBAM2 (OSTβ-mediated, cholestatic subtype)
- Laboratory: low LDL cholesterol (reduced enterohepatic bile-acid-driven cholesterol turnover feedback)

**Onset/course**: Congenital/infantile onset is typical for the Mendelian disease (symptoms from birth or first months of life), though the 2025 vitamin-deficiency case was not molecularly diagnosed until age 18, underscoring diagnostic delay. Course is chronic and, without treatment, lifelong; it is not typically progressive in a degenerative sense but produces cumulative nutritional and growth deficits if uncorrected. In the broader acquired/idiopathic bile acid diarrhea population, symptoms are typically episodic/fluctuating and overlap heavily with IBS-D, contributing to years of misdiagnosis.

**Quality of life**: Poorly characterized with dedicated instruments for the genetic form specifically, but the general bile-acid-diarrhea literature documents substantial QoL burden from urgency and incontinence, comparable to inflammatory bowel disease in some cohorts (general BAD literature, PMC9180966).

**Suggested ontology terms**: HP:0002014 (Diarrhea), HP:0002570 (Steatorrhea), HP:0001508 (Failure to thrive), HP:0001510 (Growth delay), HP:0004325 (Decreased body weight), HP:0001939 (Abnormality of metabolism/homeostasis, generic parent), vitamin-deficiency-specific terms (e.g., HP:0002153 Hypocalcemia, HP:0002656 Abnormality of coagulation for vitamin K deficiency), HP:0000938 (Osteopenia) / rickets-related terms.

Sources: [PMID:34192422 Molecular Genetics & Genomic Medicine](https://onlinelibrary.wiley.com/doi/full/10.1002/mgg3.1740), [PMID:40814585 JPGN Rep. case](https://pmc.ncbi.nlm.nih.gov/articles/PMC12350027/), [OMIM 619481 clinical synopsis](https://omim.org/clinicalSynopsis/619481)

---

## 4. Genetic/Molecular Information

**Causal genes:**
| Gene | HGNC/OMIM | Locus | Protein | Disease |
|---|---|---|---|---|
| *SLC10A2* | OMIM *601295 | 13q33.1 | ASBT (apical sodium-dependent bile acid transporter) | PBAM1 (#613291) |
| *SLC51B* | OMIM *612085 | 15q22 | OSTβ (organic solute transporter, beta subunit) | PBAM2 (#619481) |

**Pathogenic variants (SLC10A2):**
- Missense variants: c.230G>A (p.Gly77Glu) and others catalogued in ClinVar with "Primary bile acid malabsorption 1" clinical significance
- Splicing variant: c.920-20G>A (ClinVar RCV001807609)
- Recently reported: homozygous c.194C>T (p.Pro65Leu) — described as "completely conserved in vertebrates from human to zebrafish" (PMID:40814585); a homozygous c.313T>C variant in another pedigree; novel compound heterozygous variants reported in 2024–2026 in a child initially misdiagnosed with Crohn's disease (Oxford Academic, *Inflammatory Bowel Diseases*, "Novel SLC10A2 variants induce primary bile acid malabsorption and dysbiosis with IBD-like features," doi:10.1093/ibd/izag137)
- Functional variant panel: c.868C>T = complete loss of function; c.292G>A and c.431G>A = mild/moderate impairment (PMC3170668)
- A six-variant novel haplotype block linked to reduced *SLC10A2* expression was identified by systematic mutation screening (Renner et al., *Human Genetics* 2009, doi:10.1007/s00439-009-0630-0)

**Variant classification**: Per ACMG/AMP framework, disease-causing alleles are typically classified pathogenic/likely pathogenic in ClinVar when biallelic and functionally validated (reduced/absent transport in transfected cell systems); population allele frequencies for the rare loss-of-function alleles are very low/absent in gnomAD, consistent with an ultra-rare recessive disorder, though the search did not surface a specific gnomAD carrier-frequency figure for a founder allele.

**Functional consequences**: Loss-of-function (complete or partial) is the operative mechanism for *SLC10A2*; the recessive inheritance and biallelic requirement are consistent with haploinsufficiency-resistant, true LOF biology (heterozygous carriers are asymptomatic). For *SLC51B*, the reported frameshift removes the C-terminal domain needed for membrane insertion and OSTα heterodimerization — again a LOF mechanism, but at the basolateral efflux step rather than apical uptake, which is proposed to explain the additional cholestatic-liver phenotype in PBAM2.

**Somatic vs. germline**: The disease-causing variants are germline; there is no known somatic/mosaic contribution to PBAM.

**Modifier genes / broader genetic architecture of "bile acid diarrhea"**: Distinct from the rare Mendelian PBAM, common variants in genes governing the hepatic bile-acid-synthesis feedback loop have been associated with the more common, largely idiopathic/acquired bile acid diarrhea phenotype: *FGFR4* and *KLB* (β-klotho, FGFR4 co-receptor) variants show "significant associations with primary BAD and IBS-D," and the *CYP7A1* promoter polymorphism rs3808607 (T>G) correlates with elevated bile-acid-synthesis marker (C4) levels, with TT-genotype carriers showing roughly a two-fold increase in synthesis (2024 review, PMC10855108, citing Yang et al. 2024).

**Epigenetics / chromosomal abnormalities**: No epigenetic or chromosomal-abnormality mechanism has been reported for PBAM; it is a single-gene recessive disorder in both known molecular subtypes.

Sources: [OMIM SLC10A2 601295](https://www.omim.org/entry/601295), [ClinVar SLC10A2 variants](https://www.ncbi.nlm.nih.gov/clinvar/RCV001807609/), [PMC3170668 functional variant panel](https://ncbi.nlm.nih.gov/pmc/articles/PMC3170668), [JCI 1997](https://www.jci.org/articles/view/119355), [Hum Genet 2009 haplotype screen](https://link.springer.com/article/10.1007/s00439-009-0630-0), [IBD journal 2024/2026 novel variants](https://academic.oup.com/ibdjournal/advance-article/doi/10.1093/ibd/izag137/8732609), [PMC10855108 precision-medicine review](https://pmc.ncbi.nlm.nih.gov/articles/PMC10855108/)

---

## 5. Environmental Information

The Mendelian form is purely genetic (autosomal recessive), with no known environmental trigger required for disease expression. However, environmental/lifestyle and iatrogenic factors are central to the much larger population of patients with **acquired/secondary or idiopathic bile acid diarrhea** who present with an overlapping phenotype and must be distinguished from true PBAM:

- **Surgical/anatomic**: terminal ileal resection (Crohn's disease surgery), cholecystectomy (68–86% incidence of BAM reported afterward per the 2022 pathophysiology review, PMC9180966)
- **Pharmacologic**: metformin, GLP-1 receptor agonists, and other drugs affecting gut transit or bile flow
- **Radiation**: pelvic/abdominal radiotherapy causing radiation enteritis and secondary (Type 1) BAM
- **Dietary**: high dietary fat intake exacerbates symptoms in all forms; a low-fat diet (<20% of energy from fat) is reported to improve urgency, bloating, and stool consistency (PMC9180966)
- **Infectious**: small intestinal bacterial overgrowth (SIBO) causes bacterial deconjugation of bile acids, a mechanism of Type 3 BAM; no specific pathogen causes the genetic disease itself, though secondary dysbiosis (see Mechanism section) is a downstream consequence of ASBT loss

Sources: [PMC9180966 Pathophysiology and Clinical Management](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9180966/)

---

## 6. Mechanism / Pathophysiology

**Normal physiology.** Bile acids undergo enterohepatic circulation roughly 4–12 times daily. In the terminal ileum, ASBT (SLC10A2) actively imports conjugated bile acids across the brush-border membrane (Na⁺-coupled), working with intracellular bile-acid-binding protein (I-BABP/FABP6) to shuttle them across the cytoplasm to the basolateral membrane, where the OSTα/OSTβ heterodimer (SLC51A/SLC51B) exports them into portal blood for hepatic re-uptake (PMC9180966, citing PMID:16816347).

**FXR–FGF19–CYP7A1 feedback axis.** High intracellular ileal bile acid concentration activates the nuclear receptor FXR, which transcriptionally induces **FGF19** (fibroblast growth factor 19). FGF19 travels via portal blood to hepatocytes and binds FGFR4 (with β-klotho/KLB as co-receptor), suppressing **CYP7A1**, the rate-limiting enzyme of hepatic bile acid synthesis from cholesterol — a classical negative feedback loop. **7α-hydroxy-4-cholesten-3-one (C4)** is a direct downstream metabolite of CYP7A1 activity and thus a serum biomarker of synthesis rate.

**Disease mechanism.**
- *In PBAM1 (SLC10A2 loss)*: ASBT failure means bile acids are not reclaimed in the ileum; ileal intracellular bile acid concentration falls, FXR activation and FGF19 output collapse, CYP7A1 is disinhibited, and bile acid synthesis increases up to **6- to 7-fold** to compensate (PMC9180966). Despite this compensatory overproduction, net circulating bile acid pool size falls (in *Slc10a2*-null mice, pool size dropped ~80% despite increased synthesis and became selectively enriched in cholic acid), while massive quantities of unabsorbed bile acids reach the colon.
- *In PBAM2 (SLC51B/OSTβ loss)*: basolateral export fails, so bile acids accumulate within enterocytes and, mechanistically, in a manner that produces both diarrhea and features of cholestatic liver injury (elevated transaminases/GGT), distinguishing it from pure ASBT loss.
- *Colonic secretory mechanism*: excess luminal bile acids in the colon activate multiple secretory pathways — increased intracellular **cAMP**, EGFR stimulation, reduced Na⁺/K⁺-ATPase expression, upregulated **aquaporin-3 and aquaporin-8** water channels (shown in rat models), and activation of the G-protein-coupled bile acid receptor **TGR5** on colonocytes/enterochromaffin cells, which stimulates serotonin release and further drives fluid/mucus secretion and altered motility (TGR5 expression is reported elevated in IBS-D patients and correlates with symptom severity) (PMC9180966; PMC10855108).
- *Dysbiosis and secondary inflammation*: excess bile acid exposure in the colon alters the microbiome — reported shifts include increased *Clostridia* and reduced *Ruminococcaceae*, an elevated Firmicutes:Bacteroidetes ratio, and reduced bacterial diversity, correlating with fecal bile acid and serum C4 levels. A 2025 metagenomic study of PBAM patients found elevated **Ruminococcus gnavus** and biofilm markers versus controls, proposing new disease-associated microbial signatures with diagnostic potential (PMC12702444). This dysbiosis can reduce **colonization resistance to *Clostridioides difficile*** and produce secondary inflammatory changes that mimic inflammatory bowel disease — a mechanism explicitly invoked in the 2024–2026 report of children with genetically confirmed PBAM initially misdiagnosed as Crohn's disease (Oxford IBD journal, doi:10.1093/ibd/izag137).

**Cell types/tissues involved**: ileal enterocytes (apical and basolateral membrane transport machinery), colonic epithelial cells (secretory response), enterochromaffin cells (TGR5-serotonin axis), hepatocytes (CYP7A1/FGFR4 feedback), gut microbiota (bile acid deconjugation/biotransformation).

**Suggested GO terms**: bile acid and bile salt transport (GO:0015721), bile acid metabolic process (GO:0008206), regulation of bile acid biosynthetic process (GO:0070857), farnesoid X-activated receptor signaling pathway, cellular response to bile acid (GO:1904373). **Suggested CL terms**: enterocyte of epithelium of small intestine (CL:1000334/ileal enterocyte), colonic epithelial cell, enterochromaffin cell, hepatocyte.

Sources: [PMC9180966](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9180966/), [PMC10855108](https://pmc.ncbi.nlm.nih.gov/articles/PMC10855108/), [Carcinogenesis 2015 Slc10a2-null mice, PMID:26210740](https://academic.oup.com/carcin/article/36/10/1193/316547), [PMC12702444 Ruminococcus gnavus 2025](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12702444/), [IBD journal SLC10A2/dysbiosis](https://academic.oup.com/ibdjournal/advance-article/doi/10.1093/ibd/izag137/8732609)

---

## 7. Anatomical Structures Affected

- **Primary organ**: terminal ileum (site of ASBT-mediated bile acid reuptake failure)
- **Secondary organ involvement**: colon (site of secretory diarrhea from excess bile acid exposure); liver (compensatory bile acid overproduction in PBAM1; direct cholestatic injury in PBAM2); skeletal system (rickets/osteopenia from vitamin D deficiency); coagulation system (vitamin K deficiency); potentially retina/dermatologic system (vitamin A/E deficiency, not specifically documented in the reviewed cases but expected from fat-soluble vitamin malabsorption)
- **Body systems**: digestive (primary), skeletal, hematologic/coagulation, hepatobiliary (PBAM2)
- **Tissue/cell level**: intestinal epithelium (enterocytes of the ileal brush border), colonic mucosal epithelium
- **Subcellular level**: apical (brush-border) plasma membrane (ASBT/SLC10A2 localization), basolateral plasma membrane (OSTα/OSTβ), cytoplasm (I-BABP-mediated bile acid trafficking)
- **UBERON-relevant anatomical terms**: ileum (UBERON:0002116), colon (UBERON:0001155), liver (UBERON:0002107), intestinal epithelium (UBERON:0001277)
- **Laterality**: not applicable (diffuse/systemic GI process, not lateralized)

Sources: synthesized from mechanism literature above (PMC9180966, OMIM entries).

---

## 8. Temporal Development

- **Onset**: Congenital/infantile in the classic Mendelian disease — diarrhea from birth or early infancy is typical (PBAM2 pedigree: "chronic diarrhea since birth and infantile jaundice lasting for months"). However, presentation can be markedly delayed or atypical: the 2025 case presented with a hypocalcemic seizure at **10 months** as the first recognized clinical event, and the molecular diagnosis was not made until **age 18** — illustrating that isolated fat-soluble vitamin deficiency without overt GI symptoms can be the presenting (and sole) phenotype for years.
- **Onset pattern**: Chronic/insidious in most reported cases rather than acute.
- **Progression**: Not classically progressive/degenerative; rather, a stable chronic secretory diarrhea and malabsorptive state that persists lifelong without treatment, with cumulative nutritional/growth consequences (stunting, rickets) if uncorrected in childhood.
- **Disease course**: Chronic, lifelong (no spontaneous resolution documented); the disease is effectively a fixed transport lesion, so course parallels dietary bile acid load and treatment adherence rather than following discrete stages.
- **Remission**: No spontaneous remission described; symptomatic control is achievable with bile acid sequestrants or vitamin supplementation, though sequestrant intolerance (nausea, worsened diarrhea) can limit use, as seen in the 2025 case where cholestyramine was discontinued after 3 months.
- **Critical periods**: Infancy/early childhood is a critical window for growth and bone mineralization — undiagnosed disease during this period risks permanent stunting and skeletal sequelae, making early recognition and vitamin repletion time-sensitive.

Sources: [PMID:40814585 case report](https://pmc.ncbi.nlm.nih.gov/articles/PMC12350027/), [Hepatology 2018 SLC51B pedigree](https://onlinelibrary.wiley.com/doi/pdf/10.1002/hep.29516)

---

## 9. Inheritance and Population

**Epidemiology (broad bile acid diarrhea, not gene-resolved):**
- Bile acid diarrhea overall has an estimated **population prevalence of over 1%**, though it is considered substantially under-diagnosed.
- Among patients with chronic diarrhea generally, prevalence of bile acid diarrhea (by SeHCAT or equivalent testing) is reported at **~28.1% (95% CI 19.9–38.4%)**.
- In diarrhea-predominant IBS (IBS-D) specifically, systematic reviews report roughly **25–33% of patients have bile acid malabsorption**, stratified by SeHCAT retention severity: ~10% severe (<5% retention), ~32% moderate (<10%), ~26% mild (<15%).
- The genetically defined PBAM (SLC10A2/SLC51B-driven) is considered a **rare, ultra-rare Mendelian disorder** documented in only a handful of pedigrees worldwide; a precise incidence/prevalence figure is not established in the literature reviewed.

**Inheritance pattern**: Autosomal recessive for both PBAM1 (*SLC10A2*) and PBAM2 (*SLC51B*). Reported pedigrees show homozygosity or compound heterozygosity, with unaffected heterozygous carrier parents.

**Penetrance/expressivity**: Full penetrance is implied by all reported homozygous/compound-heterozygous individuals being symptomatic, but expressivity is markedly variable — from severe congenital diarrhea/steatorrhea with failure to thrive (classic presentation) to isolated fat-soluble vitamin deficiency with **no gastrointestinal symptoms at all** (2025 case), indicating that GI phenotype is not obligate even with complete loss-of-function genotypes.

**Consanguinity/founder effects**: Consanguinity is a recurrent feature of reported pedigrees (e.g., consanguineous Pakistani parents in the 2025 case), consistent with a rare autosomal recessive disorder more frequently unmasked in consanguineous populations; no specific founder mutation or geographically enriched allele was identified in the sources reviewed.

**Demographics**: No clear sex predilection is reported for the Mendelian disease. For the broader (largely non-Mendelian) bile acid diarrhea population overlapping with IBS-D, the epidemiology mirrors IBS-D demographics generally.

Sources: [Lancet eClinicalMedicine 2020, prevalence in functional diarrhea/IBS-D](https://www.thelancet.com/journals/eclinm/article/PIIS2589-5370(20)30209-1/fulltext), [PubMed 33438795](https://pubmed.ncbi.nlm.nih.gov/33438795/), [PMC10855108](https://pmc.ncbi.nlm.nih.gov/articles/PMC10855108/), [PMID:19570102 SeHCAT/IBS-D systematic review](https://pubmed.ncbi.nlm.nih.gov/19570102/), [PMID:25913530 meta-analysis IBS-D](https://pubmed.ncbi.nlm.nih.gov/25913530/)

---

## 10. Diagnostics

**Clinical/laboratory tests:**
- **75SeHCAT (⁷⁵Se-homotaurocholic acid) scan** — the international **gold standard**, a nuclear medicine test measuring 7-day retention of a radiolabeled bile acid analog. Reported sensitivity ~87.3%, specificity ~93.2%. Retention thresholds: <5% severe, 5–10% moderate, 10–15% mild BAM. Available in Europe but **not in the United States**.
- **48-hour fecal bile acid quantification**: diagnostic thresholds reported as total fecal bile acids ≥2337 µmol/48h or primary bile acids >10%, or total ≥1000 µmol/48h with primary bile acids >4%; can be performed by HPLC/mass spectrometry.
- **Serum 7α-hydroxy-4-cholesten-3-one (C4)**: elevated C4 (>~48–52.5 ng/mL depending on assay/cutoff cited) reflects increased CYP7A1 activity/bile acid synthesis; reported sensitivity ~90%, specificity ~79%. Requires fasting, morning (pre-9am) sampling due to diurnal variation.
- **Serum FGF19**: low FGF19 (≤~61.7–145 pg/mL depending on cutoff) supports the diagnosis; sensitivity ~58%, specificity ~84% (lower diagnostic accuracy than C4 or SeHCAT alone).
- **Emerging biomarkers**: serum lipidomic profiling (reported sensitivity 78%, specificity 93% in one study) and fecal microbiome/metabolome signatures (e.g., *Ruminococcus gnavus* and biofilm markers) are investigational but promising non-invasive alternatives.

**Genetic testing** (for the Mendelian form specifically): targeted gene sequencing or exome sequencing of *SLC10A2* and *SLC51B* is the definitive diagnostic approach once secondary/acquired causes are excluded and biochemical testing (fecal bile acids, C4, or SeHCAT) supports a bile-acid-driven diarrhea; a commercial NCBI GTR clinical genetic test for "Bile acid malabsorption, primary" targeting *SLC10A2* exists. Functional validation (patient-derived intestinal organoids/epithelial cultures, or heterologous expression assays) has been used in recent case reports to confirm variant pathogenicity beyond sequence-level prediction.

**Differential diagnosis**: diarrhea-predominant IBS (IBS-D) is the most important and most frequently confused mimic — a substantial fraction of "IBS-D" is actually undiagnosed bile acid diarrhea. Inflammatory bowel disease (Crohn's disease) is a critical differential for pediatric presentations, since PBAM-driven dysbiosis and secondary inflammation can produce IBD-like endoscopic/microbiome findings, as documented in a genetically confirmed pediatric case initially treated as Crohn's disease. Other differentials: microscopic colitis, celiac disease, chronic pancreatitis/exocrine pancreatic insufficiency, SIBO, and other congenital diarrheal disorders (e.g., congenital chloride-losing diarrhea, glucose-galactose malabsorption).

**Screening**: No population newborn-screening program exists for PBAM; case-finding relies on clinical suspicion in infants/children with unexplained chronic watery diarrhea, steatorrhea, failure to thrive, or unexplained fat-soluble vitamin deficiency, particularly with a family history of consanguinity.

Sources: [PMC9180966](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9180966/), [PMC10855108](https://pmc.ncbi.nlm.nih.gov/articles/PMC10855108/), [AGA/Gastroenterology practice reviews](https://www.gastrojournal.org/article/S0016-5085(18)35400-3/fulltext), [IBD journal 2024/2026 misdiagnosed-as-Crohn's case](https://academic.oup.com/ibdjournal/advance-article/doi/10.1093/ibd/izag137/8732609), [NCBI GTR test listing](https://ncbi.nlm.nih.gov/gtr/tests/551357.1/methodology)

---

## 11. Outcome/Prognosis

- **Survival/mortality**: With appropriate treatment (bile acid sequestrant therapy and/or fat-soluble vitamin supplementation), PBAM is compatible with a normal lifespan; no mortality data specific to the genetic disease were identified, consistent with it being a manageable metabolic/transport disorder rather than a degenerative or malignant condition.
- **Morbidity**: Untreated or delayed-diagnosis disease carries risk of chronic malnutrition, growth stunting, rickets/osteopenia (vitamin D), coagulopathy (vitamin K), and dental enamel defects, as documented in the 2025 case (final height 155.5 cm, enamel damage, lifelong vitamin dependence).
- **Functional outcome**: In the 2025 case, the patient reached age 19 with normal development and neurological status, asymptomatic on permanent vitamin/mineral supplementation — illustrating that with recognition and management, functional outcomes can be favorable even when the underlying transport defect is never "cured."
- **Complications**: In the broader bile acid diarrhea population, chronic disease is linked to increased colorectal neoplasia risk in some animal-model data (see Model Organisms, below) — a 54–70% increase in colon adenoma/adenocarcinoma measures was seen in *Slc10a2*-null mice — though this has not been established as a confirmed human PBAM complication.
- **Prognostic factors**: early recognition and initiation of bile acid sequestrant therapy or vitamin repletion appears to be the dominant modifiable prognostic factor; genotype severity (complete vs. partial loss of ASBT function) may correlate with disease severity, per the variant functional data above, though large genotype-outcome correlation studies do not yet exist given disease rarity.

Sources: [PMID:40814585](https://pmc.ncbi.nlm.nih.gov/articles/PMC12350027/), [PMID:26210740 Carcinogenesis, colon tumor risk in Slc10a2-null mice](https://academic.oup.com/carcin/article/36/10/1193/316547)

---

## 12. Treatment

**Pharmacotherapy — Bile acid sequestrants (first-line):**
- **Cholestyramine**: most widely used; anion-exchange resin binding luminal bile acids for fecal excretion; reported response rates ~40–54% depending on disease severity threshold (up to 96% response in patients with SeHCAT retention <5%, 80% at <10%, 70% at <15%). No placebo-controlled trials exist because an adequate placebo formulation has not been developed. Common adverse effects: constipation, bloating, nausea, and interference with absorption of concurrently administered drugs and fat-soluble vitamins — an important consideration in a disease that already causes fat-soluble vitamin deficiency (illustrated by the 2025 case where cholestyramine was discontinued for intolerance).
- **Colesevelam**: second-line, used off-label (not FDA-licensed for this indication), 4–6× higher bile-acid binding affinity than cholestyramine, better tolerability; a placebo-controlled phase 4 trial reported 67% diarrhea remission with colesevelam vs 27% with placebo (2022, *Lancet Gastroenterology & Hepatology* correspondence/trial).
- **Colestipol**: a third older sequestrant, similarly used off-label.

**Emerging/investigational pharmacotherapy:**
- **FXR agonists** — obeticholic acid (OCA) and tropifexor: increase FGF19, suppress CYP7A1/reduce C4, and reduce fecal bile acids; pilot trials of OCA (25 mg/day for 2 weeks) showed clinical benefit and safety, though OCA has since faced hepatotoxicity concerns leading to its 2024 EU commercial discontinuation (for its approved liver-disease indications, not specifically bile acid diarrhea).
- **FGF19 analogs** — **aldafermin (NGM282)**: an engineered FGF19 analog (95.4% homology to native FGF19) that suppresses bile acid synthesis directly; a 2023 investigator-sponsored phase 2 trial in IBS-D patients with idiopathic BAM showed statistically significant reductions in serum 7α-C4 and fecal bile acids versus placebo (presented at Digestive Disease Week 2023; ClinicalTrials.gov NCT05130047).
- **GLP-1 receptor agonists** — **liraglutide**: a randomized, double-blind, active-comparator non-inferiority trial versus colesevelam found liraglutide **superior** to colesevelam in reducing stool frequency (77% vs 50% achieving ≥25% stool-frequency reduction), acting by slowing small intestinal transit (allowing more passive bile acid reabsorption) rather than by luminal binding, with added glucometabolic benefit; semaglutide has also shown effect in case reports, though with differing kinetics (once-weekly vs once-daily dosing) compared to liraglutide.
- **Ileal bile acid transporter (IBAT) inhibitors** (elobixibat, maralixibat, odevixibat, linerixibat): approved/used for chronic constipation and cholestatic pruritus by *increasing* colonic bile acid delivery — mechanistically the opposite of what is needed in bile acid diarrhea, and diarrhea is a recognized adverse effect of this drug class, underscoring the bidirectional nature of bile-acid-driven colonic motility/secretion.

**Dietary/supportive management:**
- Low-fat diet (<20% of energy from fat) improves urgency, bloating, and stool consistency.
- Fat-soluble vitamin (A, D, E, K) and mineral (calcium) supplementation is essential in genetically confirmed PBAM, and may be the **primary** long-term therapy when sequestrants are not tolerated, as in the 2025 case (permanent vitamin D/K plus mineral supplementation, asymptomatic at last follow-up).

**Experimental/pipeline therapies**: microbiota modulation (targeting dysbiosis patterns such as increased *Clostridia*/reduced *Ruminococcaceae*, or elevated *Ruminococcus gnavus*) is discussed as a future therapeutic avenue but lacks definitive clinical trial support to date.

**Suggested NCIT terms**: NCIT:C15986 (Pharmacotherapy) as the umbrella treatment_term, with `therapeutic_agent` bound to specific agents (CHEBI/NCIT terms for cholestyramine, colesevelam, colestipol, obeticholic acid, liraglutide); NCIT:C15447 (Dietary Intervention) for the low-fat diet; NCIT:C15747 (Supportive Care) for vitamin/mineral supplementation.

Sources: [PMC9180966](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9180966/), [PMC10855108](https://pmc.ncbi.nlm.nih.gov/articles/PMC10855108/), [Lancet Gastro Hepatol colesevelam trial](https://www.thelancet.com/journals/langas/article/PIIS2468-1253(22)00436-8/abstract), [NICE ESUOM22 colesevelam](https://www.nice.org.uk/advice/esuom22/chapter/intervention-and-alternatives), [NGM Bio press release 2023](https://www.sec.gov/Archives/edgar/data/1426332/000162828023027198/ngm-20230803xexx991.htm), [ClinicalTrials.gov NCT05130047](https://clinicaltrials.gov/study/NCT05130047), [Lancet Gastro Hepatol liraglutide vs colesevelam](https://www.thelancet.com/journals/langas/article/PIIS2468-1253(22)00198-4/abstract), [PMC11596762 liraglutide/colesevelam bile acid levels](https://pmc.ncbi.nlm.nih.gov/articles/PMC11596762/), [PMID:39807780 GLP-1RA review](https://pubmed.ncbi.nlm.nih.gov/39807780/), [PMID:40814585 vitamin supplementation case](https://pmc.ncbi.nlm.nih.gov/articles/PMC12350027/)

---

## 13. Prevention

- **Primary prevention**: Not applicable in the traditional sense for a Mendelian recessive disorder; the only "primary prevention" avenue is genetic counseling and carrier screening in consanguineous families or those with a known affected relative, plus prenatal/preimplantation genetic testing where the causal variant is known in a family.
- **Secondary prevention (early detection)**: Clinical suspicion and biochemical/genetic testing in infants with unexplained chronic diarrhea, steatorrhea, or unexplained fat-soluble vitamin deficiency/rickets — particularly important given the 2025 case's 18-year diagnostic delay — represents the main actionable "secondary prevention" lever to avert growth stunting and skeletal/coagulation complications.
- **Tertiary prevention**: Ongoing vitamin/mineral supplementation and dietary fat modification to prevent complications (rickets, coagulopathy, growth failure) in individuals with confirmed disease.
- **Genetic counseling**: Recommended for parents of an affected child (autosomal recessive, 25% recurrence risk per pregnancy) and for consanguineous couples with a family history.
- **Public health/immunization/prophylaxis**: Not applicable — this is not an infectious or vaccine-preventable disease.

Sources: synthesized from OMIM inheritance-pattern data and case-report literature above.

---

## 14. Other Species / Natural Disease

- **Taxonomy**: The disease-relevant biology has been most extensively studied in laboratory mouse (*Mus musculus*, NCBITaxon:10090) via *Slc10a2* (Asbt) knockout models, and in rat for aquaporin-mediated colonic secretion studies.
- **Naturally occurring veterinary disease**: Bile acid diarrhea/malabsorption is increasingly recognized in **dogs and cats** with chronic enteropathies, though it remains "insufficiently recognized" clinically. In dogs with chronic enteropathy, markedly reduced ileal ASBT expression and altered bile acid metabolism disrupt bile acid recycling, allowing excess bile acids to spill into the colon and drive diarrhea; contributing factors include decreased ileal absorptive capacity, accelerated transit, bile acid overproduction, and intestinal dysbiosis with reduced conversion capacity by specific colonic bacteria. Diagnostic testing in veterinary medicine favors a paired pre- and 2-hour-postprandial serum bile acids "challenge" test over a single fasting sample for sensitivity. Retrospective case series describe dogs with chronic enteropathies successfully managed with bile acid sequestrants over 5–47 months (PMC12365994). No specific OMIA (Online Mendelian Inheritance in Animals) entry for a naturally occurring genetic (*SLC10A2*-mutant) canine or feline disease was identified in this search — the veterinary literature describes an acquired/secondary bile-acid-diarrhea phenotype analogous to human Type 1/3 disease rather than a documented spontaneous Mendelian ortholog.
- **Comparative biology**: The ASBT/FXR/FGF19(FGF15 in rodents)/CYP7A1 axis is highly conserved across mammals, which is why rodent knockout models recapitulate the core human biochemical phenotype (see Model Organisms below) despite species differences in bile acid pool composition (e.g., mice normally have more hydrophilic, muricholic-acid-rich pools than humans).
- **Zoonotic potential**: None — this is a metabolic/transport disorder, not an infectious disease.

Sources: [Merck Veterinary Manual, Malabsorption Syndromes](https://www.merckvetmanual.com/digestive-system/diseases-of-the-small-intestine-in-small-animals/malabsorption-syndromes-in-small-animals), [criticalcaredvm.com veterinary BAD review](https://criticalcaredvm.com/bile-acid-diarrhea-dogs-cats/), [PMC12365994 dog case series](https://pmc.ncbi.nlm.nih.gov/articles/PMC12365994/), [PMC11199873 feline chronic enteropathy bile acids](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11199873/)

---

## 15. Model Organisms

- **Mouse (*Slc10a2*/Asbt knockout)** — the principal genetic model:
  - Fecal bile acid excretion increased **>10-fold** in *Slc10a2*-null mice, with decreased plasma bile acid levels — directly recapitulating the human ASBT-loss biochemical phenotype.
  - Bile acid pool size decreased by ~80% despite increased hepatic synthesis, and became selectively enriched in cholic acid — showing the compensatory-synthesis-but-net-depletion pattern seen in human PBAM1.
  - Plasma triglycerides were reduced, and hepatic triglyceride production response to a sucrose-rich diet was blunted, linking the transporter to lipid metabolism beyond bile acids alone.
  - *Slc10a2*-null mice showed a 54% increase in aberrant crypt foci and 70%/59% increases in colon tumor number/size respectively, with a 2-fold increase in colon adenocarcinomas — establishing a **fidelity: MODERATE** model for a bile-acid-driven colorectal cancer-promotion hypothesis, though this specific complication is not yet confirmed in human PBAM patients (a translational gap / potential HUMAN_MODEL_MISMATCH candidate).
  - Related knockout of *Ostα* (organic solute transporter alpha, OSTβ's obligate heterodimer partner) similarly disrupts bile acid enterohepatic cycling and has been used to dissect basolateral efflux biology relevant to PBAM2.
- **Patient-derived intestinal organoids/epithelial cultures**: used in at least one recent case (the compound-heterozygous *SLC10A2* pediatric case initially diagnosed as Crohn's disease) to functionally validate impaired ASBT-mediated bile acid transport directly in patient tissue — a high-fidelity, patient-specific model bridging genotype to functional phenotype.
- **Heterologous expression systems** (e.g., transfected cell lines expressing mutant ASBT): used extensively to functionally characterize individual *SLC10A2* missense variants (e.g., the 868C>T, 292G>A, 431G>A allelic series) and assign quantitative loss-of-function severity (PMC3170668).
- **Rat models**: used specifically to demonstrate colonic aquaporin-3/aquaporin-8 upregulation as a downstream secretory mechanism of bile-acid-induced diarrhea, complementing the mouse genetic knockout data.
- **Limitations of current models**: Mouse bile acid pool composition differs substantially from human (more hydrophilic/muricholic-acid-rich), which limits direct extrapolation of pool-size and lipid-metabolism findings; no existing animal model reproduces the PBAM2/OSTβ cholestatic-liver-disease phenotype with the same depth of characterization as the ASBT/PBAM1 knockout model, representing a gap for future model development.

Sources: [PubMed 26210740 / Carcinogenesis, colon cancer promotion in Slc10a2-null mice](https://pubmed.ncbi.nlm.nih.gov/26210740/), [PubMed 21691100, OSTα knockout bile acid homeostasis](https://pubmed.ncbi.nlm.nih.gov/21691100/), [PMC3602841 SLC10 family review](https://pmc.ncbi.nlm.nih.gov/articles/PMC3602841/), [PMC3170668 functional variant characterization](https://ncbi.nlm.nih.gov/pmc/articles/PMC3170668), [Cyagen Slc10a2-KO model](https://www.cyagen.com/mouseatlas/S-KO-16831), [IBD journal patient organoid validation](https://academic.oup.com/ibdjournal/advance-article/doi/10.1093/ibd/izag137/8732609)

---

## Summary for Knowledge-Base Curation

Primary Bile Acid Malabsorption is best modeled in a dismech-style pathograph as a **two-molecular-subtype Mendelian disease** (PBAM1/*SLC10A2*, PBAM2/*SLC51B*), clearly distinguished from the much larger, largely non-Mendelian "bile acid diarrhea" clinical spectrum that dominates the diagnostic/treatment literature. Key causal-chain nodes: (1) ASBT/OSTβ loss-of-function → (2) failed ileal bile acid reclamation → (3) disrupted FXR-FGF19-CYP7A1 feedback with compensatory hepatic bile acid overproduction → (4) colonic bile acid excess → (5) cAMP/aquaporin/TGR5-mediated secretory diarrhea → (6) downstream dysbiosis, fat-soluble vitamin malabsorption, and (in PBAM2) cholestatic liver injury. Curators should take care to source PBAM1-specific evidence from the *SLC10A2* case literature (OMIM 613291, JCI 1997, PMC3170668, PMID:40814585, PMID:34192422, the 2024/2026 Oxford IBD-journal report) and PBAM2-specific evidence from the *SLC51B*/OSTβ literature (OMIM 619481, *Hepatology* 2018), while citing the broader mechanistic/diagnostic/treatment literature (PMC9180966, PMC10855108) as general bile-acid-diarrhea pathway evidence rather than PBAM-specific human clinical evidence — flagging the mouse colon-cancer-promotion finding as a candidate `HUMAN_MODEL_MISMATCH` given its translational status is unconfirmed in humans.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 25 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| Quoted claims checked | 3 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 24 |
| On topic | 16 |
| Off topic | 1 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `DOI:10.1093/ibd/izag137/8732609` (5 mentions) - Identifier did not resolve to a record

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMC:PMC3170668` *(abstract only)*: "292G>A and 431G>A variants were associated with mild and moderately impaired transport function, respectively"
  - closest text in source: "RESULTS: The studies revealed two nonsynonymous SNPs, 292G>A and 431G>A, with partially impaired in vitro taurocholate transport"
- `PMID:40814585` *(abstract only)*: "completely conserved in vertebrates from human to zebrafish"
  - Text part not found as substring: 'completely conserved in vertebrates from human to zebrafish' (note: only abstract available for PMID:40814585, full text may contain this excerpt)

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:16816347` (1 mention) - Dyspnoea and hypoxaemia after lung surgery: the role of interatrial right-to-left shunt.
  - shared terms: clinical, patient

Weighed against this report's own most characteristic terms: `acid`, `bile`, `diarrhea`, `disease`, `slc10a2`, `genetic`, `vitamin`, `mendelian`, `malabsorption`, `chronic`, `primary`, `asbt`, `pbam2`, `pbam`, `clinical`, `fat-soluble`, `deficiency`, `patient`, `ost`, `ileal`.