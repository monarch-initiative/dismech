---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-20T07:16:28.097391'
end_time: '2026-08-20T07:20:42.394817'
duration_seconds: 254.3
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Progressive Spondyloepimetaphyseal Dysplasia-short Stature-short Fourth
    Metatarsals-intellectual Disability Syndrome
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
  web_search_requests: 9
  num_turns: 25
  total_cost_usd: 1.9642491999999996
  session_id: f8013076-8ee3-558b-9ea3-39808e4b84d8
  stop_reason: end_turn
  assistant_text_blocks: 5
citation_count: 14
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 2
  relevance_assessed: 6
  on_topic: 6
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Progressive Spondyloepimetaphyseal Dysplasia-short Stature-short Fourth Metatarsals-intellectual Disability Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Progressive Spondyloepimetaphyseal Dysplasia-short Stature-short Fourth Metatarsals-intellectual Disability Syndrome** covering all of the
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

I'll research this rare syndrome using web search and fetch tools. Let me first load the necessary tools.

This is OMIM #616723 (Faden-Alkuraya type SEMD), caused by RSPRY1. Let me pull detailed data from OMIM, Orphanet, GARD, and key PubMed papers.

Excellent data. Now let me get the Simsek-Kiper 2018 abstract and OMIM clinical synopsis via an alternate route, plus GeneCards/UniProt for RSPRY1 molecular details.

I have sufficient data to compile a comprehensive report now.

I now have enough verified data across the primary literature (Faden et al. 2015, Simsek-Kiper et al. 2018, Alazami-adjacent case reports, the 2024 two-sisters report, and the 2025 mechanistic TGF-β paper) plus OMIM, Orphanet, GARD, and GeneCards. Here is the comprehensive report.

---

# Progressive Spondyloepimetaphyseal Dysplasia–Short Stature–Short Fourth Metatarsals–Intellectual Disability Syndrome (Spondyloepimetaphyseal Dysplasia, Faden-Alkuraya Type)

## 1. Disease Information

**Overview.** This is an ultra-rare autosomal recessive skeletal dysplasia syndrome first delineated by Faden, Alkuraya, and colleagues in 2015 in a large consanguineous Saudi Bedouin kindred. It is caused by biallelic loss-of-function or missense variants in **RSPRY1** (Ring finger and SPRY domain containing 1, 16q13). The name used by Orphanet/GARD — "Progressive spondyloepimetaphyseal dysplasia–short stature–short fourth metatarsals–intellectual disability syndrome" — and the OMIM/clinical eponym **"Spondyloepimetaphyseal Dysplasia, Faden-Alkuraya type" (SEMDFA)** refer to the same entity. The original paper describes it as "a clinically recognizable autosomal-recessive disorder ... comprising progressive spondyloepimetaphyseal dysplasia, short stature, facial dysmorphism, short fourth metatarsals, and intellectual disability" (Faden et al. 2015, PMID: [26365341](https://pubmed.ncbi.nlm.nih.gov/26365341/)).

**Key identifiers:**
- **OMIM phenotype:** #616723 — SPONDYLOEPIMETAPHYSEAL DYSPLASIA, FADEN-ALKURAYA TYPE (SEMDFA) ([omim.org/entry/616723](https://omim.org/entry/616723))
- **OMIM gene:** *616585 — RSPRY1 ([omim.org/entry/616585](https://www.omim.org/entry/616585))
- **Orphanet:** ORPHA:457395 ([orpha.net/en/disease/detail/457395](https://www.orpha.net/en/disease/detail/457395))
- **GARD:** disease ID 17808 ([rarediseases.info.nih.gov/diseases/17808](https://rarediseases.info.nih.gov/diseases/17808/progressive-spondyloepimetaphyseal-dysplasia-short-stature-short-fourth-metatarsals-intellectual-disability-syndrome))
- **Gene:** RSPRY1, HGNC:29420, chromosome 16q13
- **MONDO:** an entry paired to the OMIM/Orphanet record should be sought/confirmed directly against a MONDO SPARQL/OLS lookup at curation time (not independently confirmed with a stable MONDO CURIE in this research pass — flag for verification before curating `disease_term`).
- **Synonyms:** "SEMDFA"; "Spondylo-epi-metaphyseal dysplasia Faden-Alkuraya type"; "RSPRY1-related spondyloepimetaphyseal dysplasia."

**Provenance of information.** Aggregated disease-level knowledge (OMIM, Orphanet, GARD, GeneCards) synthesizing individual case/family reports — this is **not** an EHR-derived or population-registry disease; all epidemiological and phenotypic knowledge derives from fewer than ~10 published probands across at least four unrelated families/kindreds (Saudi Bedouin, Peruvian, Turkish ×2, and Vietnamese/other Asian sisters).

---

## 2. Etiology

**Disease causal factor:** Purely monogenic/genetic — biallelic (homozygous or compound heterozygous) pathogenic variants in **RSPRY1**. No environmental, infectious, or multifactorial contribution has been described; GARD's generic boilerplate mentioning "environmental triggers" for genetic mutations does not reflect condition-specific literature and should not be curated as evidence-backed.

**Genetic risk factors:**
- **Consanguinity** is the dominant risk factor reported across index families — the original description was in a large consanguineous Saudi Bedouin family with four affected siblings (Faden et al. 2015, PMID:26365341).
- Reported causal variants to date:
  - **Frameshift/1-bp duplication** causing nonsense-mediated decay — original Saudi family (Faden et al. 2015)
  - **Homozygous missense variant** in a Peruvian simplex case, identified via "gene-centric matchmaking" (Faden et al. 2015)
  - Two additional distinct mutations reported in five individuals from two unrelated Turkish families (Simsek-Kiper et al. 2018, PMID:[30063090](https://pubmed.ncbi.nlm.nih.gov/30063090/))
  - **c.1652G>A; p.(Cys551Tyr)**, a homozygous missense variant in the C3HC4 RING-finger domain (exon 15), reported in two sisters, "not present in gnomAD (v3.1.2)," in silico pathogenic (CADD phred 29.7, REVEL 0.967) (Zhu et al. 2024, PMID:[38562122](https://pubmed.ncbi.nlm.nih.gov/38562122/))
- **gnomAD constraint:** RSPRY1 shows a pLI ≈1 and LOEUF ≈0.45, indicating strong intolerance to loss-of-function variation in the general population — consistent with a recessive, severe phenotype from biallelic loss (no specific carrier-frequency estimate is published; the gene is too rare/recently described for population carrier-screening panels).

**Protective factors:** None described in the literature — not applicable for this ultra-rare monogenic disorder.

**Gene-environment interactions:** None reported; disease penetrance and severity appear driven entirely by genotype (frameshift/null alleles vs. missense hypomorphic alleles may modulate severity, though this has not been formally established across the small case series).

---

## 3. Phenotypes

Phenotype data are pooled from OMIM's clinical synopsis, Orphanet, GARD (~73 catalogued HPO-mapped findings), and the primary case reports.

### Skeletal (core diagnostic features)
| Phenotype | Suggested HPO | Notes |
|---|---|---|
| Progressive spondyloepimetaphyseal dysplasia | HP:0008875 (Spondyloepimetaphyseal dysplasia) | Defining, progressive over childhood |
| Short stature (disproportionate, short-trunk) | HP:0003510 / HP:0004452 | Severe — e.g., height −5.28 SD and −4.53 SD in two sisters (PMID:38562122) |
| Short fourth metatarsal(s) | HP:0010741 | Named in the syndrome's descriptive title; a hallmark, relatively specific finding |
| Platyspondyly | HP:0000926 | Flattened vertebral bodies, progressive |
| Mild spondylar/vertebral dysplasia progressing over time | HP:0008080 (referenced as component) | "Progressive vertebral defects" (PMID:38562122) |
| Epimetaphyseal dysplasia of long bones | HP:0005817 (Metaphyseal dysplasia) + epiphyseal component | With coxa vara and genu valgum |
| Coxa vara | HP:0002812 | |
| Genu valgum | HP:0002857 | |
| Small/cone-shaped epiphyses, metaphyseal cupping/fraying | HP:0010580 (cone-shaped epiphysis) | |
| Brachydactyly / cono-brachydactyly, clinodactyly | HP:0001156 / HP:0030084 | |
| Kyphoscoliosis / thoracolumbar scoliosis | HP:0002751 | |
| Lumbar lordosis | HP:0002938 | |
| Craniosynostosis | HP:0001363 | Noted as part of "further delineation" (PMID:30063090) |
| Copper-beaten (lückenschädel-like) skull appearance | HP:0007658 | Radiographic |
| Delayed skeletal maturation | HP:0002750 | |
| Short femoral neck, small carpal bones | HP:0100961-adjacent | Radiographic |
| Joint dislocation/subluxation (elbow) | HP:0001373 | Reported as a **novel** feature (PMID:38562122) |
| Wind-swept lower-limb deformity | HP:0100692-adjacent | |

### Craniofacial dysmorphism
Microcephaly (HP:0000252), hypertelorism (HP:0000316), epicanthal folds (HP:0000286), mild ptosis (HP:0000508), strabismus/exotropia (HP:0000486), malar hypoplasia/midface retrusion (HP:0000272), short nose with depressed nasal bridge (HP:0003196/HP:0000431), full lips (HP:0012471), small low-set ears (HP:0008551/HP:0000369), short neck (HP:0000470), broad forehead (HP:0000337).

### Neurological / developmental
- Global developmental delay / intellectual disability, mild-to-moderate — HP:0001263 / HP:0001249. In one sister, Vineland social quotient 68 (mild ID).
- Severe expressive language delay — HP:0002465
- Generalized hypotonia — HP:0001290
- Gait disturbance — HP:0001288
- Generalized tonic-clonic seizures (reported in one sibling from age 5) — HP:0002069
- Brain MRI: asymmetry of cerebral hemispheres, mild thinning of corpus callosum — HP:0100543 / HP:0002079

### Ocular
Myopia (both sisters, PMID:38562122) — HP:0000545; strabismus/exotropia; mild ptosis.

### Cardiac (reported in a subset)
Mitral regurgitation (HP:0031650), patent ductus arteriosus (HP:0001643, surgically repaired at age 3 in one proband), patent foramen ovale (HP:0001655).

**Onset, severity, progression:** Onset is congenital/neonatal-to-infantile (symptoms typically evident by 4 weeks–23 months per GARD). The skeletal dysplasia is explicitly **progressive** — the defining adjective in the syndrome name — with vertebral and epimetaphyseal changes worsening over the first years of life, and lower-limb deformity progressing from ~age 2 in at least one reported case. Growth deficiency is severe (height in the −4 to −5 SD range by mid-childhood). Intellectual disability ranges mild-to-moderate. Frequency data across the ~9 published cases suggest craniofacial dysmorphism, short stature, and short 4th metatarsals as near-universal; craniosynostosis, seizures, and joint dislocation are reported in a minority and may represent phenotypic expansion rather than core features.

**Quality-of-life impact:** Not formally studied (no EQ-5D/SF-36/PROMIS data published); qualitatively, GARD notes substantial multidisciplinary burden (orthopedic, neurologic, developmental) and a diagnostic odyssey averaging >6 years.

---

## 4. Genetic/Molecular Information

**Causal gene:** RSPRY1 (Ring Finger and SPRY Domain Containing 1); HGNC:29420; OMIM *616585; chromosome 16q13.

**Gene/protein structure:** RSPRY1 encodes a 576-amino-acid protein containing:
- A **B30.2/SPRY domain** (~residues 359–479), which mediates protein-protein interactions
- A **C3HC4-type RING-finger domain** (~residues 526–565), characteristic of E3 ubiquitin ligases

The 2015 discovery paper describes RSPRY1 as "a hypothetical RING and SPRY domain-containing protein of unknown physiological function" at the time of publication (PMID:26365341).

**Variants reported:**
| Family/Report | Variant | Type | Zygosity |
|---|---|---|---|
| Saudi Bedouin (index family, PMID:26365341) | 1-bp duplication (frameshift) | Nonsense-mediated decay (presumed null) | Homozygous |
| Peruvian simplex case (PMID:26365341) | Missense | Likely pathogenic | Homozygous |
| Turkish families ×2 (PMID:30063090) | Two additional distinct RSPRY1 variants | Not fully specified in available abstract | Reported in 5 individuals |
| Two sisters, East/Southeast Asian (PMID:38562122) | c.1652G>A; p.(Cys551Tyr), exon 15, RING-finger domain | Missense, likely pathogenic (CADD 29.7, M-CAP 0.812, REVEL 0.967); absent from gnomAD v3.1.2 and an in-house 3,076-exome cohort | Homozygous |

**Allele frequency:** No RSPRY1 pathogenic variant is present in gnomAD, consistent with extreme rarity and strong purifying selection (gene-level pLI ≈1, LOEUF ≈0.45 per GeneCards/gnomAD constraint metrics).

**Origin:** All reported cases are germline, consistent with autosomal recessive Mendelian inheritance in consanguineous or otherwise genetically isolated families; no somatic or mosaic cases reported.

**Functional consequence:** Loss-of-function (frameshift → NMD) and missense (hypomorphic/structurally destabilizing) alleles are both described, suggesting the phenotype arises from reduced or absent RSPRY1 activity rather than a specific gain-of-function or dominant-negative mechanism. The Cys551Tyr substitution is proposed to "perturb hydrophobic interactions, either in the core of the protein or on the surface" of the RING domain (PMID:38562122).

**ClinGen status:** As of this research, ClinGen has **not yet published a gene-disease validity curation** for RSPRY1 (confirmed via ClinGen KB, HGNC:29420) — an important curation caveat; the association currently rests on the primary literature (4 independent publications, ≥4 families) rather than a formal ClinGen classification.

**Modifier genes / epigenetics / chromosomal abnormalities:** None reported — this is a classical single-gene recessive disorder with no described modifier loci, epigenetic mechanism, or chromosomal rearrangement etiology.

---

## 5. Environmental Information

Not applicable/not described. No environmental toxin, lifestyle, or infectious trigger has been implicated in any published report; the disorder is fully genetically determined (autosomal recessive, biallelic RSPRY1).

---

## 6. Mechanism / Pathophysiology

**Proposed causal chain (from primary literature):**

1. **Biallelic RSPRY1 loss-of-function or destabilizing missense variant** → reduced/absent functional RSPRY1 protein (RING + SPRY domain protein, predicted E3 ubiquitin ligase activity; GO:0016567 protein ubiquitination, GO:0030163 protein catabolic process)
2. RSPRY1 shows "strong protein localization in murine embryonic osteoblasts and periosteal cells during primary endochondral ossification" (Faden et al. 2015), implicating a **cell-autonomous role in osteoblast/periosteal biology during bone growth** (CL:0000062 osteoblast; GO:0001958 endochondral ossification)
3. A 2025 mechanistic study (Unraveling the Role of RSPRY1 in TGF-β Pathway Dysregulation, PMID:[39940902](https://pubmed.ncbi.nlm.nih.gov/39940902/); PMC:[11817781](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11817781/)) used **patient-derived fibroblast transcriptomics and CRISPR-Cas9 RSPRY1/SMAD3 knockout cell lines** to show:
   - Significant enrichment of the "TGF-β regulation of the ECM pathway" (p = 1.12 × 10⁻²⁴), implicating **SMAD3, COL1A1, WISP1 (CCN4), and RUNX2**
   - RSPRY1 deficiency causes **overactivation (not suppression) of TGF-β/SMAD signaling** — RSPRY1 KO fibroblasts show constitutively enhanced wound-closure/motility, an effect abrogated in RSPRY1+SMAD3 double-knockout cells, establishing SMAD3-dependence
   - Exogenous TGF-β1 accelerated wound closure in control cells but had limited additional effect in RSPRY1-KO cells — consistent with a ceiling effect from constitutive pathway activation
   - The authors hypothesize RSPRY1 normally **restrains TGF-β/SMAD signaling via ubiquitination of pathway components**, and its loss removes this brake, driving dysregulated extracellular matrix (ECM) remodeling in growth-plate cartilage and bone
4. **Downstream:** dysregulated ECM dynamics at the growth plate/perichondrium → progressive epiphyseal/metaphyseal/vertebral dysplasia (the "spondyloepimetaphyseal" phenotype), disproportionate short stature, and characteristic acral findings (short 4th metatarsal, brachydactyly)
5. Craniofacial and neurodevelopmental features (microcephaly, ID, corpus callosum thinning) suggest RSPRY1 or its downstream TGF-β/ECM effects also influence neurocranial and CNS development, though the mechanistic link here is less well characterized than the skeletal arm.

**Suggested GO terms:** GO:0007179 (transforming growth factor beta receptor signaling pathway), GO:0030198 (extracellular matrix organization), GO:0001958 (endochondral ossification), GO:0016567 (protein ubiquitination), GO:0030282 (bone mineralization).
**Suggested CL terms:** CL:0000062 (osteoblast), CL:0000138 (chondrocyte), CL:0000058 (chondroblast), CL:0000057 (fibroblast — used as the patient-derived disease-modeling cell type).
**Molecular pathway framing:** This mechanism supports potential `conforms_to` linkage to a TGF-β/ECM-dysregulation pattern — note this is a *distinct, RSPRY1-specific ubiquitination-mediated brake on TGF-β signaling*, mechanistically related to but not identical to the canonical `aortopathy_tgfbeta_dysregulation` module's fibrillin/TGF-β receptor axis; a dismech curator should treat it as its own node rather than force-conforming it to that module without justification.

---

## 7. Anatomical Structures Affected

**Organ/system level:**
- **Skeletal system** (primary): axial skeleton (vertebral column — spondylo-), epiphyses and metaphyses of long bones (epimetaphyseal), skull (craniosynostosis, copper-beaten appearance), hands/feet (short 4th metatarsal, brachydactyly)
- **Craniofacial skeleton/soft tissue:** midface, orbits, nose, ears
- **Nervous system:** cerebral hemispheres (asymmetry), corpus callosum (thinning) — CNS structural involvement
- **Cardiovascular system:** mitral valve, ductus arteriosus, foramen ovale (secondary/associated findings in a subset)
- **Ocular system:** lens/refractive apparatus (myopia), extraocular muscles (strabismus, ptosis)

**Tissue/cell level:** Growth-plate cartilage (chondrocytes), periosteum and osteoblasts (per murine expression data), dermal fibroblasts (used as the patient-derived disease model in mechanistic studies).

**Subcellular level:** RSPRY1 is proposed as a **secreted/extracellular-acting protein** functioning via ubiquitin-mediated regulation — implicating the extracellular matrix compartment and secretory pathway (GO Cellular Component: GO:0005576 extracellular region) rather than a classical nuclear/cytoplasmic mechanism, though a defined subcellular localization study specific to RSPRY1 was not identified in this search.

**Localization/laterality:** Skeletal changes are typically bilateral/symmetric (e.g., bilateral short 4th metatarsals, symmetric epimetaphyseal changes); cerebral hemisphere **asymmetry** is itself a reported radiologic finding (not laterality of a symmetric process, but an intrinsic asymmetric brain finding).

**Suggested UBERON terms:** UBERON:0001474 (bone element), UBERON:0002228 (rib/vertebral column), UBERON:0002355 (metatarsal bone), UBERON:0000104 (life cycle stage-adjacent — not applicable), UBERON:0002316 (corpus callosum), UBERON:0002616 (odontoid — not applicable). Core: UBERON:0004357 (epiphysis), UBERON:0003064 (metaphysis), UBERON:0006558 (cartilaginous joint/growth plate).

---

## 8. Temporal Development

- **Onset:** Congenital-to-infantile; GARD states symptoms typically emerge "as a Newborn and as an Infant," within the first 4 weeks to 23 months of life.
- **Onset pattern:** Insidious/progressive rather than acute.
- **Progression:** Explicitly progressive — the skeletal dysplasia (vertebral, epiphyseal, metaphyseal changes) worsens through childhood; lower-limb deformity in one reported case progressed specifically from age 2 onward. No formal staging system exists (this is not a malignancy or a disease with a validated staging scheme).
- **Disease course:** Chronic, lifelong; no spontaneous remission described. Seizures, when present, began later in one case (age 5), suggesting some features may emerge progressively rather than being present from birth.
- **Critical periods:** Early childhood (infancy through the first several years) appears to be the period of most active skeletal deterioration based on the reported natural history, making this the presumptive window for orthopedic surveillance and any future intervention trials.

---

## 9. Inheritance and Population

**Epidemiology:** GARD estimates **fewer than 1,000 people in the U.S.** with this condition — consistent with an ultra-rare disorder; published literature comprises fewer than ~10 molecularly confirmed cases across 4+ unrelated families (Saudi Arabian Bedouin, Peruvian, two Turkish families, and an East/Southeast Asian sibling pair). No formal prevalence/incidence rate (cases per 100,000) has been published; this is a "cases in literature" epidemiological measure, not a population-based estimate.

**Inheritance pattern:** **Autosomal recessive.** GARD: "A child must inherit two copies of the mutated gene, one from each biological parent, to be affected by the disease," with the standard AR recurrence risk of 25% affected, 50% carrier, 25% unaffected per pregnancy for two carrier parents.

**Penetrance:** Presumed complete (all reported biallelic carriers are affected), though the very small case series limits confidence in this assessment.

**Expressivity:** Variable — severity of skeletal, neurodevelopmental (mild-vs-moderate ID), and additional features (craniosynostosis, seizures, joint dislocation, cardiac defects) differs between reported families and even between affected siblings, suggesting variable expressivity, possibly genotype-correlated (null vs. missense alleles) though this is not formally established.

**Consanguinity:** A major contributing factor — the founding family was a large **consanguineous Saudi Bedouin kindred**; consanguinity likely explains the homozygosity observed across most reported families and the extreme rarity of compound heterozygous presentations to date.

**Founder effects:** Not formally established, but the concentration of cases in specific consanguineous/isolated populations (Saudi Bedouin, and separately Turkish and Peruvian founder-type homozygous variants) is consistent with population-specific private alleles rather than a single recurrent founder mutation.

**Carrier frequency:** Not established/reported; RSPRY1 pathogenic variants are absent from gnomAD, precluding a population-based carrier-frequency estimate.

**Population demographics:** Reported cases span Middle Eastern (Saudi Arabian), South American (Peruvian), and Asian (Turkish, and separately an East/Southeast Asian sibling pair) ancestries — there is no evidence this is restricted to a single ethnic group, though ascertainment (via consanguineous-family exome sequencing) likely biases the reported cohort.

**Sex ratio:** No sex predilection reported; both male and female probands are represented across published families (autosomal recessive inheritance is expected to affect both sexes equally).

---

## 10. Diagnostics

**Radiographic/skeletal survey:** The primary diagnostic modality — findings include platyspondyly, mild scoliosis, lumbar lordosis, small carpal bones, short femoral neck, cone-shaped/small epiphyses with metaphyseal cupping and fraying, short metatarsals (particularly the 4th), copper-beaten skull appearance, and craniosynostosis on skull imaging.

**Molecular genetic testing:**
- **Confirmatory diagnosis requires molecular testing of RSPRY1** — via targeted single-gene sequencing, a skeletal dysplasia gene panel (e.g., "Spondylo-Epi-Metaphyseal dysplasias Comprehensive panel," listed in NCBI GTR), clinical exome sequencing (WES), or genome sequencing (WGS). WES was the diagnostic modality in essentially all published cases (combined autozygome/exome mapping in consanguineous families, or trio/singleton exome in simplex cases).
- **Chromosomal microarray/karyotype:** Not causally relevant — this is a single-gene point-variant disorder, not a copy-number or chromosomal disorder; CMA/karyotype would be expected to be normal and are used only to exclude alternative diagnoses.

**Brain MRI:** Recommended given reported findings of cerebral hemisphere asymmetry and corpus callosum thinning.

**Cardiac evaluation (echocardiography):** Recommended given reported associations (PDA, PFO, mitral regurgitation) in a subset of patients.

**Differential diagnosis:** Other spondyloepimetaphyseal dysplasias should be excluded, including SEMD with joint laxity type 2 (OMIM #603546, B3GALT6), SEMD Missouri type, SEMD Kondo-Fu type, and Dyggve-Melchior-Clausen-spectrum disorders — distinguished from SEMDFA by the combination of short 4th metatarsals, characteristic craniofacial gestalt, and RSPRY1 molecular confirmation.

**Diagnostic odyssey:** GARD notes it can take "more than six years" on average to reach an accurate diagnosis, underscoring both the rarity and phenotypic overlap with other skeletal dysplasias, and the value of multidisciplinary evaluation at a specialized skeletal-dysplasia/genetics center.

**Screening:** No population newborn-screening or carrier-screening program exists for this condition given its extreme rarity; prenatal diagnosis would rely on targeted familial variant testing once a proband's RSPRY1 genotype is known, or on incidental prenatal ultrasound detection of skeletal disproportion followed by genetic confirmation.

---

## 11. Outcome/Prognosis

No formal survival, mortality, or life-expectancy data have been published — the literature to date does not report early mortality attributable to this condition, and the clinical picture (progressive skeletal dysplasia with developmental delay) is not inherently life-limiting based on available case reports, though longitudinal outcome data beyond childhood/adolescence are not available in the current literature.

**Morbidity:** Primary long-term morbidity relates to (1) progressive skeletal deformity — kyphoscoliosis, joint laxity/dislocation, and disproportionate short stature, which may require ongoing orthopedic management, and (2) neurodevelopmental impact — mild-to-moderate intellectual disability and expressive language delay affecting educational and functional independence, with seizures as an additional morbidity in a subset.

**Quality of life:** Not formally measured with validated instruments in this population; qualitatively substantial given multisystem involvement.

**Prognostic factors:** No validated prognostic biomarkers or severity predictors exist; genotype (null/frameshift vs. missense) is a plausible but unproven modifier of severity based on the pattern of variants reported.

---

## 12. Treatment

There is **no disease-specific or FDA-approved therapy**; GARD explicitly notes "only about 5% of rare diseases have FDA-approved treatments," and this condition has none. Management is entirely **supportive/symptomatic and multidisciplinary**:

| Intervention | Purpose | Suggested NCIT term |
|---|---|---|
| Orthopedic surveillance and surgical correction (e.g., for scoliosis, coxa vara, joint dislocation) | Manage progressive skeletal deformity | NCIT:C15329 (Surgical Procedure); NCIT:C16186 (Orthopedic Surgical Procedure) |
| Physical/occupational therapy | Address hypotonia, gait disturbance, motor delay | NCIT:C15302 (Physical Therapy) |
| Speech/language therapy | Address expressive language delay | related NCIT term for speech therapy, NCIT:C159273 |
| Neurologic management (antiepileptic therapy) | Manage generalized tonic-clonic seizures in affected individuals | NCIT:C15986 (Pharmacotherapy) |
| Ophthalmologic correction | Manage myopia, strabismus, ptosis | NCIT:C49236 (Therapeutic Procedure) |
| Cardiac management/surgical repair | Manage PDA/PFO/mitral regurgitation (surgical PDA repair performed in one reported proband at age 3) | NCIT:C15329 (Surgical Procedure) |
| Genetic counseling | Recurrence risk counseling for carrier parents (25%/50%/25%) | NCIT:C15240 (Genetic Counseling) |
| Multidisciplinary care coordination (genetics, orthopedics, neurology, PCP) | Comprehensive management at a specialized center | NCIT:C15747 (Supportive Care) |

**Experimental/investigational:** No registered clinical trials specific to RSPRY1-related SEMD were identified. The 2025 mechanistic finding of **TGF-β/SMAD3 pathway overactivation** raises a plausible future therapeutic hypothesis (e.g., TGF-β pathway modulation), analogous to strategies explored in other TGF-β-dysregulated skeletal/connective tissue disorders (e.g., losartan in Marfan-spectrum aortopathies), but this remains speculative and has not been tested in RSPRY1-deficient models or patients.

---

## 13. Prevention

No primary, secondary, or tertiary prevention strategy beyond **genetic counseling and reproductive risk management** is described. For known carrier couples (typically identified after an affected child or via consanguinity-related genetic counseling), options include prenatal diagnosis via targeted variant testing and preimplantation genetic testing (PGT-M), following standard AR-disorder counseling practice — no condition-specific guideline was identified in the literature reviewed. No immunization, screening program, or public-health intervention applies, given the disorder's monogenic, non-infectious, non-multifactorial etiology.

---

## 14. Other Species / Natural Disease

No naturally occurring RSPRY1-associated disease in non-human species (companion animals, livestock, wildlife) was identified in this search (no OMIA entry located). This appears to be a human-specific clinical description at present.

---

## 15. Model Organisms

**Mouse (Mus musculus, NCBITaxon:10090):** No RSPRY1 germline knockout mouse model with a published skeletal phenotype was identified in this search. However, the original discovery paper (Faden et al. 2015, PMID:26365341) reports **RSPRY1 protein expression/localization studies in murine embryonic tissue**, showing "strong RSPRY1 protein localization in murine embryonic osteoblasts and periosteal cells during primary endochondral ossification, consistent with a role in bone development" — this is an expression/localization study, not a functional knockout model, and does not itself demonstrate phenotype recapitulation.

**Human patient-derived cellular models:** The 2025 mechanistic study (PMID:39940902) generated **CRISPR-Cas9 RSPRY1 knockout, SMAD3 knockout, and RSPRY1+SMAD3 double-knockout fibroblast lines** from patient-derived dermal fibroblasts (>90% knockout efficiency), used to demonstrate constitutive TGF-β/SMAD3-dependent hypermotility (wound-healing assay) in the absence of RSPRY1. This is currently the **only functional model system** in the literature for this gene/disease and would be the appropriate `experimental_models` entry for a dismech curation (IN_VITRO evidence source; relationship RECAPITULATES with respect to the TGF-β/ECM dysregulation mechanism node, though NOT a whole-organism/skeletal-phenotype model).

**Model limitations:** No animal model recapitulating the skeletal dysplasia phenotype in vivo has yet been published, representing a clear knowledge gap for future curation (a `KNOWLEDGE_GAP` discussion node would be appropriate: mechanistic data exist only in 2D fibroblast culture, not in a skeletal-relevant cell type such as chondrocytes/osteoblasts in vivo, nor in an animal model demonstrating the actual dysplasia phenotype).

---

## Summary Table of Key Primary Citations

| PMID | Citation | Contribution |
|---|---|---|
| [26365341](https://pubmed.ncbi.nlm.nih.gov/26365341/) | Faden et al., Am J Hum Genet 2015;97:608-615 | Original description; RSPRY1 identified via autozygome/exome + gene matchmaking; murine osteoblast/periosteal expression |
| [30063090](https://pubmed.ncbi.nlm.nih.gov/30063090/) | Simsek-Kiper et al., Am J Med Genet A 2018;176:2009-2016 | Phenotype delineation in 5 individuals/2 Turkish families; cono-brachydactyly and craniosynostosis emphasized |
| [38562122](https://pubmed.ncbi.nlm.nih.gov/38562122/) | Zhu et al. 2024 (PMC7616131) | Two sisters; novel joint-dislocation phenotype; c.1652G>A p.(Cys551Tyr) RING-domain missense variant |
| [39940902](https://pubmed.ncbi.nlm.nih.gov/39940902/) | 2025, Int J Mol Sci (PMC11817781) | Mechanistic dissection: RSPRY1 loss → TGF-β/SMAD3 pathway overactivation via CRISPR KO fibroblast models |

## Curation Caveats for dismech

1. **MONDO ID** was not definitively confirmed with a stable CURIE in this pass — verify via OAK/MONDO lookup before setting `disease_term`.
2. **ClinGen has not yet curated RSPRY1 gene-disease validity** — do not cite a ClinGen `CGGV:` record; the evidence base rests on 4 independent peer-reviewed publications instead.
3. GARD's "environmental triggers" boilerplate for the general concept of mutation causation is **not disease-specific evidence** and should not be curated as an environmental risk factor for this entry.
4. The Simsek-Kiper 2018 abstract could not be retrieved verbatim (PubMed blocked automated access) — before citing a specific quoted snippet from this paper in a `kb/disorders` evidence block, fetch and cache it properly via `just fetch-reference PMID:30063090` and verify the exact wording against the cached abstract.
5. No animal model recapitulates the skeletal phenotype in vivo — only patient-fibroblast CRISPR KO models exist; curate `experimental_models` (not `animal_models`) for the mechanistic evidence.

---

**Sources:**
- [OMIM #616723 — SEMDFA](https://omim.org/entry/616723)
- [OMIM *616585 — RSPRY1](https://www.omim.org/entry/616585)
- [Orphanet ORPHA:457395](https://www.orpha.net/en/disease/detail/457395)
- [GARD Disease 17808](https://rarediseases.info.nih.gov/diseases/17808/progressive-spondyloepimetaphyseal-dysplasia-short-stature-short-fourth-metatarsals-intellectual-disability-syndrome)
- [MalaCards — SEMDFA](https://www.malacards.org/card/spondyloepimetaphyseal_dysplasia_faden_alkuraya_type)
- [Faden et al. 2015, PMID:26365341](https://pubmed.ncbi.nlm.nih.gov/26365341/)
- [Simsek-Kiper et al. 2018, PMID:30063090](https://pubmed.ncbi.nlm.nih.gov/30063090/)
- [Zhu et al. 2024 (PMC7616131), PMID:38562122](https://pmc.ncbi.nlm.nih.gov/articles/PMC7616131/)
- [RSPRY1/TGF-β mechanistic study 2025, PMID:39940902 (PMC11817781)](https://www.mdpi.com/1422-0067/26/3/1134)
- [ClinGen RSPRY1 (HGNC:29420)](https://search.clinicalgenome.org/kb/genes/HGNC:29420)
- [GeneCards RSPRY1](https://www.genecards.org/cgi-bin/carddisp.pl?gene=RSPRY1)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 6 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.