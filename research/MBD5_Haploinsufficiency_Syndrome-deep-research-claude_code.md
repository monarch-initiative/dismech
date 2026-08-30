---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-27T23:16:28.768932'
end_time: '2026-08-27T23:21:25.387434'
duration_seconds: 296.62
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: MBD5 Haploinsufficiency Syndrome
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
  web_search_requests: 15
  num_turns: 32
  total_cost_usd: 1.3735510000000002
  session_id: 2df13fb4-9115-50fa-aa7c-75f1d91c874a
  stop_reason: end_turn
  assistant_text_blocks: 3
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 0
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMC:PMC8163803
  relevance_assessed: 16
  on_topic: 12
  needs_review: true
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** MBD5 Haploinsufficiency Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **MBD5 Haploinsufficiency Syndrome** covering all of the
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

I'll research MBD5 Haploinsufficiency Syndrome (also known as 2q23.1 microdeletion syndrome) using web search and fetch tools, then compile a comprehensive report.

I have sufficient comprehensive information now. Let me compile the complete research report.

# MBD5 Haploinsufficiency Syndrome (MBD5-Associated Neurodevelopmental Disorder / 2q23.1 Microdeletion Syndrome): Comprehensive Research Report

---

## 1. Disease Information

**Overview.** MBD5 haploinsufficiency — increasingly referred to under the umbrella term **MBD5-Associated Neurodevelopmental Disorder (MAND)** — is a genetic neurodevelopmental syndrome caused by reduced dosage of the *MBD5* gene at chromosome 2q23.1. It was originally described as "2q23.1 microdeletion syndrome" following identification of overlapping deletions in affected individuals; systematic mapping of the smallest region of overlap (SRO) across cases subsequently showed that *MBD5* itself, not neighboring genes, is the critical locus, and that point mutations/intragenic deletions of *MBD5* alone reproduce the full syndrome (Talkowski et al., PMID 21981781; GeneReviews, NBK390803). The condition is characterized by developmental delay, intellectual disability (usually moderate–severe), severe expressive speech impairment, epilepsy, sleep disturbance, and behavioral/autistic features, often with mild dysmorphism, microcephaly, and skeletal anomalies.

**Key identifiers:**
- **OMIM (gene):** *MBD5*, MIM 611472 ("METHYL-CpG-BINDING DOMAIN PROTEIN 5")
- **Orphanet:** ORPHA228402 (2q23.1 microdeletion syndrome / MBD5 haploinsufficiency)
- **HGNC:** HGNC:20444 (approved symbol *MBD5*; former aliases *KIAA1461*, *FLJ11113*)
- **NCBI Gene:** Entrez Gene ID 55777
- **Ensembl:** ENSG00000204406 (chr2:148,021,011–148,516,971, cytoband 2q23.1)
- **GeneReviews:** NBK390803 (Mullegama, Mendoza-Londono, Elsea; initial 2016, updated 2026)
- **MalaCards / MONDO:** cross-referenced as "MBD5 haploinsufficiency" / 2q23.1 deletion syndrome

**Common synonyms:** 2q23.1 microdeletion syndrome; 2q23.1 deletion syndrome; MBD5-associated neurodevelopmental disorder (MAND); intellectual developmental disorder, autosomal dominant 1 (MRD1/IDDAD1 in some nosologies).

**Source of information:** Predominantly aggregated, disease-level clinical genetics literature (case series, GeneReviews systematic reviews, cohort studies of 5–78+ patients pooled across publications) rather than large-scale EHR data, reflecting its status as an ultra-rare Mendelian disorder.

---

## 2. Etiology

**Primary cause — genetic haploinsufficiency.** Three molecular mechanisms converge on reduced *MBD5* dosage:
1. **Heterozygous deletion of 2q23.1** encompassing all or part of *MBD5* (~80% of diagnosed cases) — ranging from small 38 kb intragenic deletions up to >19 Mb multigene deletions (Talkowski et al. 2011, PMID 21981781, cohort of 65 subjects).
2. **Intragenic deletions/duplications** of one or more *MBD5* exons, including noncoding exons 1–5 (~15% of cases).
3. **Heterozygous pathogenic/likely pathogenic sequence variants** (nonsense, frameshift, canonical splice-site, and some missense) in *MBD5* (~5% of cases) (Mullegama et al. 2016, PMID 27514998 / PMC4989212; Talkowski et al. 2011).

MBD5 is explicitly established as a **dosage-sensitive gene**: MBD5 mRNA in lymphocytes from deletion carriers is reduced to ~0.22–0.59-fold of normal (22.5–55.4% expression, P<0.0001), while individuals with 2q23.1 microduplications show elevated MBD5 mRNA (1.5–1.83-fold, P<0.0001) and a phenotypically overlapping but generally milder syndrome — both over- and under-expression produce convergent neurodevelopmental phenotypes (PMC4989212).

**ClinGen Dosage Sensitivity curation (CCID:007440, last evaluated 08/29/2025):**
- **Haploinsufficiency score: 3 — Sufficient Evidence for Haploinsufficiency.** Rationale cites at least six independent reports of de novo nonsense/frameshift variants plus segregation data.
- **Triplosensitivity score: 0 — No Evidence for Triplosensitivity** at the single-gene level (regional 2q23.1 duplications spanning multiple genes exist, but no isolated whole-gene *MBD5* duplication case has been reported to establish gene-specific triplosensitivity).

**Genetic risk factors.** No population susceptibility loci are described (this is a fully penetrant monogenic disorder, not polygenic). *MBD5* shows strong evolutionary constraint against loss-of-function variation in gnomAD (high pLI / low LOEUF, consistent with the broader observation that monogenic neurodevelopmental disorder genes cluster among genes with o/e LoF confidence-interval upper bound <0.35, equivalent to pLI>0.9), consistent with dosage sensitivity.

**Environmental/infectious risk factors:** None identified as causal. However, **fever, viral illness, and hot weather are reported seizure triggers/exacerbating factors** in MAND patients with epilepsy (Smith-Hicks et al. 2021, PMID 33912662), representing a gene-environment interaction relevant to symptom exacerbation rather than causation.

**Protective factors:** None specifically described in the literature; this reflects the rarity and recency of syndrome delineation rather than an established absence.

---

## 3. Phenotypes

Phenotype frequency data are drawn primarily from GeneReviews (NBK390803) and the Mullegama/Elsea 2016 review (PMC4989212), synthesizing Talkowski et al. (2011) and subsequent cohorts.

### Neurodevelopmental / Cognitive
| Phenotype | Frequency | Notes | Suggested HPO |
|---|---|---|---|
| Developmental delay | 100% | Global | HP:0001263 |
| Intellectual disability | ~100% | Usually moderate–severe | HP:0001249 |
| Severe speech impairment | >80% | Many nonverbal or limited to single words/short phrases | HP:0002167 (Severe speech delay) / HP:0002376 |
| Motor delay, ataxic/poorly coordinated gait | >70% | Independent walking often delayed to 2–3 yrs | HP:0002194, HP:0002066 |
| Hypotonia | ~80% | Contributes to feeding difficulty | HP:0001252 |

### Neurological
| Phenotype | Frequency | Onset/course | HPO |
|---|---|---|---|
| Seizures/epilepsy | >80–90% | Median onset 2.9 yrs (range 3 days–13 yrs); generalized tonic-clonic most common; focal, atypical absence, tonic, drop attacks, myoclonic also seen; 7/23 had convulsive and 3/23 nonconvulsive status epilepticus in one cohort (Smith-Hicks 2021, PMID 33912662) | HP:0001250 |
| Microcephaly | ~80% | Postnatal/progressive in many | HP:0000252 |

### Sleep
| Phenotype | Frequency | Character | HPO |
|---|---|---|---|
| Sleep disturbance | ~90% | Frequent night waking, short sleep duration, early-morning waking, apparent night terrors, snoring, daytime sleepiness | HP:0002360 |

Mechanistically linked to disrupted circadian gene expression (see Mechanism, below) — molecularly overlapping with Smith-Magenis syndrome and fragile X syndrome sleep pathophysiology (Mullegama et al. 2014, PMID 25271084).

### Behavioral / Psychiatric
| Phenotype | Frequency | HPO |
|---|---|---|
| Autistic-like behaviors (gaze avoidance, stereotypies) | ~80% | HP:0000729 |
| Self-injurious behavior and/or aggression | >60% | HP:0100716 / HP:0000718 |
| Hyperactivity, short attention span | Frequent (>60%) | HP:0000752 |

### Gastrointestinal
- Feeding difficulties (>90%, related to hypotonia) — HP:0011968
- Constipation (>80%) — HP:0002019
- Hyperphagia (>50%) — HP:0002591

### Skeletal / Craniofacial
- Dysmorphic features (~80%) — mild, non-specific
- Small hands/feet (~75%) — HP:0001167/HP:0001773
- Fifth-finger clinodactyly (~70%) — HP:0004209
- Brachydactyly (~41%) — HP:0001156
- Sandal gap deformity (~33%)
- Short stature / postnatal growth retardation (frequent)

### Cardiovascular
- Congenital heart defects ~10–11% (ASD, VSD, pulmonic stenosis reported)

### Quality of life
No disease-specific QOL instrument has been validated; caregiver-reported burden centers on nonverbal communication, seizure management, disrupted sleep (affecting the whole family), and self-injurious/aggressive behavior requiring behavioral or psychiatric support.

---

## 4. Genetic/Molecular Information

**Causal gene:** *MBD5* (HGNC:20444; OMIM *611472; chr2q23.1; Entrez 55777).

**Protein/gene structure:** *MBD5* has two principal isoforms. Isoform 1 (1,448 aa, encoded across exons 6–15) contains both a **methyl-CpG-binding domain (MBD)** (~70 residues) and a **PWWP domain** (Pro-Trp-Trp-Pro motif, ~100–150 aa, associated with cell division/growth/differentiation proteins). Isoform 2 (851 aa, exons 6–9 with retained intron 9) lacks the PWWP domain. Isoform 1 is broadly expressed but enriched in brain and testis; isoform 2 is broadly expressed but enriched in brain and ovary (PMC4989212).

**Variant spectrum (Mullegama 2016; Talkowski 2011; Hodge et al. 2014, PMID 24173355/PMC3831065):**
- Large deletions: 38 kb to >19 Mb (2q23.1 deletion syndrome)
- Intragenic deletions/duplications: e.g., 19–68 kb deletions; a 34 kb duplication spanning exons 5–10
- Nonsense: c.440C>G, p.(Ser147*) (de novo)
- Frameshift: c.340_347del, p.(Lys114Glyfs*35)
- Missense variants in protein-coding exons (multiple, including inherited variants identified in ASD cohorts — 6 of 747 ASD subjects vs. 2,043 controls; 32 MBD5 changes across a 287-patient ASD cohort)
- Duplications (whole 2q23.1 region, ~40 documented cases, 68 kb–53.7 Mb), producing a milder but overlapping phenotype

**Variant classification:** ACMG/AMP-classified pathogenic/likely pathogenic variants are predominantly protein-truncating (nonsense, frameshift, canonical splice-site) or gene-disrupting CNVs; missense VUS are more common in ASD-ascertained cohorts and require careful curation (ClinVar, ClinGen).

**Allele frequency:** Essentially absent from gnomAD/population databases for pathogenic truncating alleles, consistent with strong LoF constraint and full penetrance of a severe pediatric-onset phenotype.

**Origin:** Predominantly **de novo** (both deletions and point variants). Rare parent-to-child transmission has been documented for intragenic deletions and sequence variants (not for whole-MBD5-encompassing large deletions, which have not been reported to transmit). **Germline mosaicism** has been documented in at least one family (Bagchi et al., *Molecular Case Studies*, PMC/CSHL, "Germline mosaicism in a family with MBD5 haploinsufficiency"), supporting counseling for a nonzero sibling recurrence risk even when parental blood testing is negative.

**Functional consequence:** Loss of function via haploinsufficiency (reduced transcriptional activator dosage). No dominant-negative or gain-of-function mechanism is described; the disease model is straightforward dosage insufficiency of a chromatin-associated transcriptional regulator, with dosage in the *opposite* direction (duplication) also pathogenic — a "two-hit dosage" model unusual for classic haploinsufficiency syndromes.

**Modifier genes:** Three genes adjacent to *MBD5* in the 2q23.1 region — *ORC4*, *KIF5C*, and *EPC2* — are proposed to contribute to phenotypic variability (e.g., microcephaly severity, additional neurobehavioral features) in individuals with larger deletions spanning multiple genes, though core MAND features map to *MBD5* alone (PMC4989212).

**Epigenetic information:** MBD5 itself is a chromatin-associated, methyl-CpG-domain-containing protein and functions in **epigenetic regulation** rather than being regulated epigenetically as a downstream target; it interacts with the **PR-DUB (Polycomb repressive deubiquitinase) complex** to remove monoubiquitin from histone H2A-K119 (H2AK119ub1), a repressive chromatin mark (Guo et al. 2024, *Nucleic Acids Research*, PMID 38366571/PMC11077058 — zebrafish model). Its target loci show enrichment for both RNA m5C modification and H2A-K119ub1 signal, positioning MBD5 as a novel **RNA m5C reader** linking RNA modification to chromatin state.

**Chromosomal abnormalities:** Contiguous gene deletions/duplications of 2q23.1 are themselves the chromosomal abnormality class most associated with this disorder (see Etiology); also reported: "apparently balanced complex chromosome rearrangements" of 2q23.1 disrupting MBD5 (GeneReviews).

---

## 5. Environmental Information

No causal environmental, infectious, or toxin exposure is implicated in disease etiology — this is a monogenic disorder. The only established environmental interaction is **symptom modulation**: fever, intercurrent viral illness, and hot ambient temperature are reported precipitants of seizures (including status epilepticus) in individuals with MAND-associated epilepsy (PMID 33912662). No lifestyle/behavioral risk-factor literature exists specific to this ultra-rare disorder. No infectious agent is causally or triggeringly implicated beyond the generic "febrile illness lowers seizure threshold" mechanism common to many pediatric epilepsies.

---

## 6. Mechanism / Pathophysiology

**Causal chain overview:**
1. **Initiating event:** Heterozygous deletion, intragenic CNV, or truncating/missense variant reduces functional MBD5 protein to ~50% (or, for duplications, increases it ~1.5–1.8×).
2. **Molecular consequence:** MBD5, unlike its paralog MeCP2, localizes to **non-heterochromatic, transcriptionally active nuclear regions** and functions as a **transcriptional activator** rather than a classical methyl-DNA-mediated repressor (Camarena et al. 2014, PMID 25001217/PMC4154127). It interacts with histone acetyltransferase **KAT2A** (linked to memory formation and glucose metabolism) and, per the 2024 zebrafish work, with the **PR-DUB complex**, promoting H2A-K119 deubiquitylation at loci enriched for RNA m5C modification (PMC11077058) — an unanticipated RNA-modification/chromatin-crosstalk mechanism, since zebrafish Mbd5 was found *not* to bind methylated DNA directly but instead to bind m5C-modified mRNA.
3. **Transcriptional dysregulation:** Haploinsufficiency dysregulates a network of other **autism/neurodevelopmental disease genes**, including *UBE3A* (Angelman syndrome), *RAI1* (Smith-Magenis syndrome), *TCF4* (Pitt-Hopkins syndrome), *MEF2C*, and *FMR1* (GeneReviews NBK390803; Mullegama 2014 PMID 25271084). iPSC-derived neural progenitor cell (NPC) transcriptome studies from three MAND patients found **468 differentially expressed genes (q<0.05)**, including 20 SFARI autism genes (upregulated: *FOXG1*, *GABRA3*, *SLC30A3*; downregulated: *MBD5*, *SLC1A1*, *GPR37*, *OXTR*), with enrichment for TGFβ signaling, Hippo signaling, DNA replication/cell cycle, spliceosome, and MAPK signaling pathways, and striking overlap with autism gene sets in "forebrain and telencephalon regionalization, neuron fate commitment" (PMC8163803).
4. **Circadian pathway disruption:** Patient lymphoblastoid lines show altered circadian gene expression (*NR1D2*, *PER1*, *PER2*, *PER3*), and circadian/mTOR pathway alterations overlap between MBD5 and RAI1 knockdown models and FMR1-related data — mechanistically linking MBD5 haploinsufficiency to the syndrome's prominent sleep phenotype and drawing a direct molecular parallel to Smith-Magenis syndrome (RAI1) and fragile X syndrome (FMR1) (PMID 25271084).
5. **Neuronal/circuit consequence:** Cortical neurons cultured from *Mbd5*+/GT mouse embryos show significantly reduced neurite length and branching within the first 2 days in culture (PMC4154129), consistent with impaired activity-dependent neuronal maturation.
6. **Mouse-brain regional transcriptomics:** In the *Mbd5*+/GT hypomorph, cortex shows the most widespread transcriptional changes of three brain regions examined, and gene co-expression network analysis reveals clusters enriched for **ciliary function** terms associated with reduced Mbd5 (Vegas et al. 2020, *Molecular Autism*, PMID 32503625/PMC7275313) — a novel and still poorly understood link, especially compared to CRISPR-edited human iPSC-neuron models, underscoring context-dependence of the transcriptional signature.
7. **Clinical manifestation:** The cumulative effect of dysregulated chromatin/transcriptional networks (autism genes), circadian genes, and neurite outgrowth deficits during brain development produces the clinical triad of intellectual disability/developmental delay, epilepsy, and autistic/behavioral features, plus the syndrome's characteristic sleep disturbance.

**Cell types/processes implicated:** cortical excitatory neurons (neurite outgrowth/branching deficits); suprachiasmatic/peripheral circadian oscillator cells (via PER1/2/3, NR1D2); neural progenitor cells (differentiation/fate commitment pathways).

**Suggested GO terms:** GO:0006357 (regulation of transcription by RNA polymerase II); GO:0006325 (chromatin organization); GO:0035522 (monoubiquitinated histone H2A deubiquitination); GO:0007623 (circadian rhythm); GO:0031175 (neuron projection development).

**Suggested CL terms:** CL:0000679 (glutamatergic neuron) / CL:0000540 (neuron); CL:0002608 (embryonic stem cell / iPSC-derived NPC context — CL:0011020 neural progenitor cell).

**Molecular profiling data available:** transcriptomics (mouse brain RNA-seq across 3 regions; human iPSC-NPC RNA-seq, 468 DEGs); no proteomics, metabolomics, or lipidomics datasets specific to MBD5 identified in the literature searched. Single-cell/spatial transcriptomic and multi-omic integration studies for MAND were not found — a notable gap.

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Central nervous system (cerebral cortex, and by extension cognitive/behavioral circuitry); the disorder is fundamentally a neurodevelopmental/encephalopathic condition.
- **Secondary:** Skeletal system (hands, feet, digits — clinodactyly, brachydactyly); cardiovascular system (~10% septal defects, pulmonic stenosis); gastrointestinal system (constipation, feeding dysfunction secondary to hypotonia); craniofacial structures (mild dysmorphism, microcephaly).
- **Body systems involved:** Nervous, musculoskeletal, digestive, cardiovascular, and (via sleep/circadian dysregulation) the endocrine/circadian system.

**Tissue/cell level:** Cerebral cortical neurons (reduced neurite length/branching in model systems); neural progenitor cells (dysregulated fate/regionalization programs).

**Subcellular level:** Nucleus — specifically **non-heterochromatic, transcriptionally active chromatin regions** (GO:0000785 chromatin; the MBD5 protein is notably excluded from classical heterochromatin, distinguishing it from MeCP2). Involvement of the PR-DUB histone-deubiquitination complex implicates chromatin/nucleosome subcompartments (H2A-K119ub1 sites).

**Localization/UBERON suggestions:** UBERON:0000955 (brain); UBERON:0001851 (cortex); UBERON:0002037 (cerebellum, less prominently implicated); UBERON:0002542 (chromatophore/skeletal structures for digit anomalies, e.g., UBERON:0002389 hand); UBERON:0000948 (heart) for the cardiac subset.

**Lateralization:** Not applicable — a symmetric, bilateral neurodevelopmental syndrome.

---

## 8. Temporal Development

**Onset:** Congenital/early-infantile in terms of underlying genetic lesion, but clinical recognition typically follows in **infancy through early childhood** as developmental delay becomes apparent; hypotonia and feeding difficulty may be evident from infancy (>90%). Seizure onset has a **median of 2.9 years** (range 3 days–13 years) (PMID 33912662); GeneReviews notes seizure onset "typically around age two."

**Onset pattern:** Insidious/progressive developmental delay rather than acute onset; epilepsy onset can be abrupt (including presentation with status epilepticus in some patients).

**Progression:** The neurodevelopmental phenotype is generally **static-to-slowly evolving** rather than degenerative — this is a developmental encephalopathy, not a neurodegenerative disorder. Seizures may show a relapsing/fluctuating course with fever/illness-provoked exacerbations. Behavioral features (self-injury, aggression) and sleep disturbance often persist chronically through childhood and adulthood; disease duration is **lifelong**.

**Disease course pattern:** Chronic, non-remitting core neurodevelopmental impairment; episodic component from seizure recurrence; some reports of germline-mosaic parents being "apparently asymptomatic" while transmitting to affected offspring, suggesting a spectrum of expressivity rather than true adult-onset remission.

**Critical periods:** Early childhood (0–5 years) is the key intervention window per GeneReviews management guidance (early intervention services, developmental preschool, early augmentative/alternative communication), reflecting the general neurodevelopmental-disorder principle that early therapeutic engagement optimizes outcomes even though no disease-modifying therapy exists.

---

## 9. Inheritance and Population

**Epidemiology:** True population prevalence and incidence are **unknown**; the disorder is likely underdiagnosed. Orphanet classifies point prevalence as **<1/1,000,000 worldwide**. One notable yield estimate: approximately **1% of 4,808 individuals ascertained for autism spectrum disorder** carried MBD5 haploinsufficiency (GeneReviews), suggesting enrichment within syndromic-ASD/ID cohorts far above general-population prevalence. The condition has been identified across diverse populations worldwide, with no reported geographic or ethnic clustering or founder effect.

**Inheritance pattern:** **Autosomal dominant**, overwhelmingly via **de novo** mutation/deletion. Rare parent-to-child transmission occurs for intragenic deletions and point variants (not for large 2q23.1-spanning deletions, which have not been observed to transmit, presumably due to more severe reproductive-fitness effects or ascertainment).

**Penetrance:** Predicted **complete**, though "an apparently asymptomatic mother" has transmitted a pathogenic variant to an affected child, which the GeneReviews authors interpret as more consistent with **variable expressivity** than incomplete penetrance.

**Expressivity:** **Variable** — genotype-phenotype correlation is generally poor between deletion vs. sequence-variant mechanisms, though larger multigene deletions may correlate with more severe/additional features (contribution from *ORC4*, *KIF5C*, *EPC2*). One reported patient with a de novo nonsense mutation (p.Ser147*) showed a notably more severe phenotype (nonambulatory, nonverbal at age 10) than typical deletion carriers, illustrating variant-specific severity variation (PMC3831065).

**Genetic anticipation:** Not described/applicable (not a repeat-expansion disorder).

**Germline mosaicism:** Documented in at least one family (Bagchi et al., *Molecular Case Studies*), with direct implications for recurrence-risk counseling of ostensibly "de novo" cases.

**Founder effects / consanguinity:** None reported; consistent with autosomal dominant de novo mechanism rather than recessive/founder biology.

**Carrier frequency:** Not applicable in the classic sense (dominant, not carrier-based); population allele frequency of pathogenic LoF variants is essentially zero in gnomAD, consistent with strong purifying selection against a severe pediatric neurodevelopmental phenotype.

**Demographics:** No sex-ratio skew reported (autosomal, dominant); age distribution reflects lifelong persistence with diagnosis typically in early-to-mid childhood following developmental/epilepsy workup.

---

## 10. Diagnostics

**First-tier test:** **Chromosomal microarray analysis (CMA)** — recommended as the initial test because ~80% of cases arise from deletions detectable by CMA but not by single-gene sequencing.

**Second-tier / complementary testing:**
- Multigene neurodevelopmental-disorder panel including *MBD5*
- Exome or genome sequencing (captures point variants missed by CMA)
- Single-gene sequence analysis plus gene-targeted deletion/duplication analysis (must include noncoding exon 1, which harbors some pathogenic deletions)

**Laboratory/biomarker tests:** No specific biochemical or enzymatic biomarker exists; MBD5 mRNA quantification (qRT-PCR in lymphocytes/lymphoblastoid lines) has been used as a research tool to confirm dosage effect (e.g., 22.5–55.4% of normal expression in deletion carriers) but is not a standard clinical diagnostic.

**Imaging:** No pathognomonic neuroimaging finding; brain MRI is typically part of the standard neurodevelopmental-disorder/epilepsy workup but is nonspecific in MAND (used to exclude alternative structural causes).

**Electrophysiology:** EEG is central to characterizing the seizure phenotype (documenting generalized tonic-clonic, focal, atypical absence, tonic, myoclonic patterns, and episodes of convulsive/nonconvulsive status epilepticus).

**Histopathology/biopsy:** Not applicable — no tissue-diagnostic biopsy finding is described.

**Genetic testing detail:**
- CMA is preferred over karyotype for initial detection given resolution needed for intragenic/smaller deletions.
- FISH is generally insufficiently sensitive for the smaller intragenic events but could confirm larger cytogenetically visible deletions.
- Mitochondrial DNA testing and repeat-expansion testing are **not relevant** to this disorder's mechanism.

**Omics-based diagnostics:** Not part of routine clinical diagnosis; iPSC/NPC transcriptomics and mouse transcriptomics are research tools only at this time.

**Clinical diagnostic criteria:** No formal consensus clinical diagnostic criteria (e.g., DSM/ICD-style) exist; diagnosis is **genetically confirmed** (molecular finding required) rather than clinically defined, given the nonspecific overlapping phenotype.

**Differential diagnosis:** Broad — essentially all causes of syndromic intellectual disability/developmental delay without pathognomonic features, including the autosomal dominant, autosomal recessive, and X-linked nonsyndromic ID phenotypic series in OMIM. Specific syndromes with mechanistic/phenotypic overlap warranting consideration: **Smith-Magenis syndrome** (RAI1, shares sleep/circadian and behavioral phenotype), **Pitt-Hopkins syndrome** (TCF4), **Angelman syndrome** (UBE3A), **fragile X syndrome** (FMR1), and **Rett syndrome-spectrum disorders** (MECP2, same MBD protein family).

**Screening:** No population newborn-screening or carrier-screening program exists (ultra-rare, predominantly de novo disorder); genetic counseling and prenatal/preimplantation testing become relevant only after a pathogenic variant is identified in an affected family member (relevant chiefly in the rare inherited/mosaic-parent scenario).

---

## 11. Outcome/Prognosis

**Survival/mortality:** No mortality data specific to MAND were identified in the literature searched; the disorder is not classically associated with reduced life expectancy from the underlying genetic lesion itself, though uncontrolled epilepsy (including reported episodes of convulsive/nonconvulsive status epilepticus in ~30–40% of one seizure cohort) represents a recognized risk for morbidity/mortality common to severe childhood epilepsies generally.

**Morbidity/function:** Substantial lifelong functional impairment is typical — most affected individuals have limited-to-absent expressive speech, require ongoing multidisciplinary support (speech/OT/PT), and a majority exhibit clinically significant behavioral challenges (self-injury/aggression >60%) requiring behavioral or psychiatric intervention.

**Quality of life:** No validated disease-specific QOL metric; qualitatively, sleep disturbance (~90%) is described as a major contributor to impaired daytime functioning/excessive daytime sleepiness for both patients and caregivers.

**Complications:** Epilepsy/status epilepticus; feeding difficulties sometimes requiring gastrostomy; scoliosis/hip dysplasia (musculoskeletal surveillance recommended); chronic constipation (>80%).

**Recovery potential:** No spontaneous "recovery" — this is a static/chronic developmental disorder; early multidisciplinary intervention is associated with better functional/communication outcomes (standard neurodevelopmental-disorder principle applied by GeneReviews management guidance), though no controlled outcome trial specific to MAND exists.

**Prognostic factors:** Variant type/deletion size appears to influence severity (larger multigene deletions and certain truncating variants like p.Ser147* correlate with more severe presentations), but no formal validated prognostic biomarker or scoring system exists.

---

## 12. Treatment

There is **no disease-modifying or curative therapy**; management is symptomatic and multidisciplinary, per GeneReviews consensus recommendations.

**Pharmacotherapy:**
- **Anti-seizure medications:** Valproate, clonazepam, zonisamide, and clobazam are reported as effective in case series (NCIT:C15986 Pharmacotherapy for the general category).
- **Sleep disturbance:** Melatonin, clonidine, and trazodone, combined with sleep-hygiene behavioral measures.
- No MBD5-specific pharmacogenomic guidance has been established.

**Advanced therapeutics:** No gene therapy, cell therapy, RNA-based therapy (ASO/siRNA/mRNA), targeted small-molecule therapy, or immunotherapy is in development or clinical use specific to MBD5 haploinsufficiency; this is a candidate area for future gene-dosage-correction research (e.g., ASO-based upregulation strategies analogous to those explored for other haploinsufficiency ID syndromes) but nothing is documented in the current literature.

**Surgical/interventional:** Orthopedic surgical management for hip dysplasia/scoliosis as clinically indicated (NCIT:C16186 Orthopedic Surgical Procedure); gastrostomy tube placement for persistent feeding difficulty (NCIT relevant to nutritional support procedures).

**Supportive/rehabilitative:**
- Speech-language therapy with early introduction of augmentative/alternative communication (sign language, AAC devices) — NCIT:C159273 (Speech Therapy)
- Occupational and physical therapy — NCIT:C15302 (Physical Therapy)
- Feeding therapy — relevant to NCIT:C15447 (Dietary Intervention) / nutritional support
- Applied behavior analysis (ABA) and psychiatric consultation for aggressive/self-injurious behavior — NCIT:C181743 (Behavioral Counseling) category
- Early intervention services (0–3 years) and developmental preschool (3–5 years); annual IEP review in least-restrictive educational placement

**Experimental treatments:** No registered clinical trials specific to MBD5 haploinsufficiency were identified in this search (searches did not surface an active ClinicalTrials.gov/ICTRP entry).

**Treatment strategy / algorithm:** Management follows a **surveillance-and-symptom-management algorithm**: developmental assessment at each visit; seizure, feeding, constipation, and sleep assessment; annual scoliosis screening; family psychosocial support assessment; multidisciplinary team including clinical genetics, neurology, developmental pediatrics, behavioral health, nutrition, and speech/OT/PT.

**Suggested therapeutic_modality mapping:** anti-seizure medications and sleep agents → `SMALL_MOLECULE`; speech/OT/PT/ABA → `BEHAVIORAL`; orthopedic surgery/gastrostomy → `SURGERY`.

---

## 13. Prevention

No primary prevention exists for this de novo genetic disorder (no modifiable environmental or lifestyle risk factor is causal). Relevant preventive/counseling measures are exclusively in the genetic-counseling and reproductive-planning domain:

- **Genetic counseling:** Recommended for families of an affected individual to discuss recurrence risk — near-baseline-population risk for truly de novo events, but **elevated above baseline due to possible parental germline mosaicism** (documented in at least one family), and 50% risk if a parent is a confirmed carrier (applicable to intragenic deletions/point variants, which can transmit, unlike large MBD5-spanning deletions).
- **Prenatal/preimplantation genetic testing:** Available once a familial pathogenic variant is identified.
- **Secondary prevention (of complications):** Early identification and treatment of seizures, proactive sleep-hygiene and pharmacologic sleep management, and early behavioral intervention to reduce self-injury/aggression severity.
- **Tertiary prevention:** Structured multidisciplinary surveillance (scoliosis screening, feeding/nutrition monitoring, seizure control optimization) to minimize secondary complications of the core disorder.
- No vaccine, screening program, or public-health intervention is applicable given the ultra-rare, non-communicable, non-environmentally-triggered nature of the disorder.

---

## 14. Other Species / Natural Disease

No naturally occurring veterinary or companion-animal disease caused by *MBD5* ortholog disruption has been reported (no OMIA entry identified in this search). The gene is evolutionarily conserved (murine *Mbd5*, zebrafish *mbd5*), enabling engineered models (see below), but no spontaneous animal disease analog is documented. No zoonotic or cross-species transmission relevance applies, as this is a purely genetic, non-infectious disorder.

**Orthologs used in model systems:**
- Mouse: *Mbd5* (chromosome 2, syntenic region)
- Zebrafish: *mbd5*

---

## 15. Model Organisms

### Mouse models
- ***Mbd5* gene-trap mouse (*Mbd5*GT)** — Camarena et al. 2014, PMID 25001217 (PMC4154127). Gene-trap cassette inserted into intron 2; **homozygotes (*Mbd5*GT/GT) die perinatally**, so the model is studied as heterozygous hypomorph.
- ***Mbd5*+/GT heterozygous hypomorph** — the principal viable model, characterized in Camarena et al. and Sanders et al. 2014 (PMID 25001218, PMC4154129). Recapitulates **most hallmark human phenotypes**:
  - Reduced body size/weight (P=0.026)
  - Abnormal nasal bone development / craniofacial abnormality (~60% of mutants, snout deviation)
  - Impaired motor coordination: reduced grip strength (P=0.036), impaired wire-hanging (P=0.01), increased dowel-balance falls (P=0.019), deficient rotarod performance (P<0.05 across trials)
  - Abnormal social behavior: excessive self-grooming (3× WT during undisturbed periods), increased/atypical interaction with stranger mice including mounting/fighting (P<0.05)
  - Impaired fear conditioning (contextual P=0.009; cued P=0.017), indicating learning/memory deficits
  - Cortical neuron cultures (E16 embryos): significantly reduced neurite length (significant by 6h, persisting through first 2 days in culture) and reduced branch points
  - In vitro luciferase assays confirm MBD5 functions as a **transcriptional activator** (GAL4-fusion constructs), localizing to euchromatic/active nuclear regions rather than heterochromatin — mechanistically distinguishing it from MeCP2.
- **Brain-region transcriptomics in *Mbd5*+/GT** (Vegas et al. 2020, PMID 32503625/PMC7275313): cortex shows the most widespread transcriptional changes of three regions studied; co-expression network analysis reveals ciliary-function-enriched gene clusters associated with reduced Mbd5, a novel and mechanistically unresolved observation. Comparison with CRISPR-edited human iPSC-derived neurons reinforces **context-dependence** of the transcriptional signature (i.e., limited direct concordance between mouse brain and human neuronal culture DEGs), a noted **model limitation**.

### Zebrafish model
- **CRISPR *mbd5* mutant zebrafish** (Guo et al. 2024, *Nucleic Acids Research*, PMID 38366571/PMC11077058): reveals that Mbd5 binds RNA m5C marks (not methylated DNA, contrary to prior assumption based on domain homology) and interacts with the PR-DUB complex to remove H2A-K119 monoubiquitination. Phenotypes include defects in **embryonic development, erythrocyte differentiation, iron metabolism, and behavior** — expanding the phenotypic reach of Mbd5 loss beyond the classic neurodevelopmental axis and suggesting hematologic/metabolic phenotypes that have not yet been systematically screened for in human patients.

### Human cellular models
- **Patient-derived iPSCs → neural progenitor cells (NPCs)** (transcriptome study, PMC8163803): fibroblasts from 3 MAND patients with 2q23.1 deletions reprogrammed via episomal iPSC induction, differentiated to PAX6+ NPCs (STEMdiff Neural Induction Medium); qRT-PCR confirmed ~50% reduction of *MBD5* mRNA; RNA-seq identified 468 DEGs with autism-gene and neurodevelopmental pathway enrichment (see Mechanism section).
- **CRISPR-edited human iPSC-derived neurons** (Vegas et al. 2020) used as a cross-species comparator to the mouse brain transcriptomic dataset.

### Model limitations
- *Mbd5* null (GT/GT) embryonic/perinatal lethality precludes studying complete loss of function in vivo in mammals; all mouse data reflect **partial (hypomorphic heterozygous) loss**, mirroring human haploinsufficiency reasonably well but limiting mechanistic dissection of full LOF.
- Mouse-vs-human iPSC-neuron transcriptomic discordance indicates **species/context-dependent transcriptional response**, a translational caveat for interpreting mouse mechanistic data as directly predictive of human neuronal biology (a candidate `HUMAN_MODEL_MISMATCH` consideration for dismech curation).
- No electrophysiology data exist in the primary Mbd5+/GT neurite-outgrowth study; functional synaptic/circuit consequences of reduced Mbd5 remain uncharacterized in vivo.
- Zebrafish model's RNA m5C/PR-DUB mechanism has not yet been confirmed in mammalian (mouse or human) systems — an open translational question given the surprising divergence from the DNA-methylation-binding paradigm long assumed for this MBD-family protein.

---

## Summary of Key Citations (PMID/PMC)

| Citation | Topic |
|---|---|
| PMID 21981781 (Talkowski et al. 2011) | SRO mapping establishing MBD5 as sole causal locus |
| NBK390803 (GeneReviews, Mullegama/Mendoza-Londono/Elsea) | Comprehensive clinical synopsis, testing, management |
| PMID 27514998 / PMC4989212 (Mullegama & Elsea 2016) | MAND clinical/molecular review, deletion/duplication dosage data |
| PMID 33912662 (Smith-Hicks et al. 2021) | Seizure phenotype spectrum, 23-patient cohort |
| PMID 25271084 (Mullegama et al. 2014) | Circadian gene dysregulation, sleep mechanism |
| PMID 25001217 / PMC4154127 (Camarena et al. 2014) | Mbd5 gene-trap mouse generation |
| PMID 25001218 / PMC4154129 (Sanders et al. 2014) | Mbd5+/GT neurobehavioral/neuronal phenotyping |
| PMID 32503625 / PMC7275313 (Vegas et al. 2020) | Mouse brain / iPSC-neuron transcriptomics |
| PMC8163803 | iPSC-NPC transcriptome, autism gene dysregulation |
| PMID 38366571 / PMC11077058 (Guo et al. 2024) | Zebrafish Mbd5, RNA m5C, PR-DUB mechanism |
| PMC3831065 (Hodge et al.) | Extended MBD5 mutation spectrum, 78-patient cohort |
| ClinGen CCID:007440 | Dosage sensitivity curation (HI=3, TS=0) |
| Orphanet ORPHA228402 | Prevalence classification |

**Notable gaps for curation:** no validated disease-specific QOL instrument; no proteomics/metabolomics/single-cell/spatial transcriptomic datasets; no registered clinical trials; no veterinary/natural-disease analog; mouse-vs-human transcriptomic model discordance flagged as an open translational question.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 16 |
| On topic | 12 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMC:PMC8163803` *(abstract only)*: "forebrain and telencephalon regionalization, neuron fate commitment"
  - Text part not found as substring: 'forebrain and telencephalon regionalization, neuron fate commitment' (note: only abstract available for PMID:34050248, full text may contain this excerpt)