---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-11T01:16:09.857140'
end_time: '2026-08-11T01:21:02.907177'
duration_seconds: 293.05
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Toxic Shock Syndrome
  mondo_id: ''
  category: Infectious Disease
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
  web_search_requests: 20
  num_turns: 25
  total_cost_usd: 2.0369165
  session_id: 469bfc9c-cb97-50c5-9454-65fc53551d45
  stop_reason: end_turn
citation_count: 45
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Toxic Shock Syndrome
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Toxic Shock Syndrome** covering all of the
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

# Toxic Shock Syndrome (TSS): Comprehensive Research Report

## 1. Disease Information

### Overview
Toxic Shock Syndrome (TSS) is an acute, rapidly progressive, toxin-mediated multisystem illness caused by exotoxin-producing strains of *Staphylococcus aureus* (staphylococcal TSS) or *Streptococcus pyogenes* (Group A Streptococcus; streptococcal TSS, STSS), and rarely group C or G streptococci. The defining pathophysiologic feature is bacterial superantigen exotoxin production that triggers massive, non-specific polyclonal T-cell activation and a resulting cytokine storm, producing high fever, diffuse erythematous ("sunburn-like") rash with later desquamation, hypotension/shock, and multi-organ dysfunction (NCBI Bookshelf StatPearls, NBK459345; PMC10812596, "Toxic Shock Syndrome: A Literature Review," PMID:38247655).

> "Central to pathogenesis is TSST-1, which bypasses conventional antigen processing by cross-linking MHC class II molecules on antigen-presenting cells with T cell receptors, triggering massive polyclonal T cell activation and a resultant cytokine storm. The ensuing release of interleukins, tumour necrosis factor and other mediators leads to fever, hypotension and multi-organ dysfunction." (PMC10812596)

TSS is historically associated with high-absorbency tampon use in menstruating women (menstrual TSS, mTSS), but non-menstrual TSS (nmTSS) — arising from surgical-site infections, burns, nasal packing, postpartum/puerperal infection, skin/soft-tissue infection, influenza-associated superinfection, and retained foreign bodies (barrier contraceptives, dialysis catheters) — is now more common than menstrual disease in the U.S. (StatPearls NBK459345; CDC MMWR historical surveillance).

### Key Identifiers
- **ICD-10-CM:** A48.3 (Toxic shock syndrome)
- **ICD-11:** 1C45 (bacterial TSS); 1C45.0 (streptococcal TSS)
- **Orphanet:** ORPHA:36234 (Bacterial toxic shock syndrome); ORPHA:99918 (Streptococcal toxic-shock syndrome)
- **MeSH:** D017676 (Shock, Septic — parent category); specific MeSH descriptor "Shock, Toxic" (D014017)
- **MONDO / OMIM:** TSS is an acquired infectious-toxin syndrome, not a monogenic Mendelian disease, so it lacks a dedicated OMIM phenotype MIM number in the classical sense; MONDO cross-references the Orphanet/ICD entities above. (No specific MONDO ID was confirmed in available search results — flagged as a gap for curator lookup via the MONDO OLS browser.)

### Synonyms / Alternative Names
- Staphylococcal toxic shock syndrome; Streptococcal toxic shock syndrome (STSS); Streptococcal toxic shock-like syndrome (TSLS); Tampon disease (historical, non-preferred); Toxic shock-like syndrome.

### Evidence Basis
Information is derived predominantly from **aggregated disease-level resources**: CDC national notifiable-disease surveillance (active, passive, and enhanced surveillance systems since 1980), case-control epidemiologic studies, case series/cohorts from pediatric and adult ICUs, and structured case reports — rather than large-scale EHR data mining, reflecting TSS's rarity and its status as a nationally notifiable condition in the U.S.

---

## 2. Etiology

### Disease Causal Factors
TSS is fundamentally an **infectious/toxin-mediated** disease, not genetic — though host genetic factors modulate susceptibility (see below).

- **Staphylococcal TSS**: caused by toxigenic *S. aureus* strains producing **TSST-1** (toxic shock syndrome toxin-1), and less commonly staphylococcal enterotoxins B and C (SEB, SEC), which act as superantigens. Both MSSA and CA-MRSA strains have been implicated.
- **Streptococcal TSS (STSS)**: caused by *Streptococcus pyogenes* (Group A Streptococcus, GAS) producing streptococcal pyrogenic exotoxins (Spe A, SpeB, SpeC) acting as superantigens, often in the context of invasive soft-tissue infection/necrotizing fasciitis. Rarely, group C or G streptococci cause an analogous syndrome.

> "M-proteins, especially types 1 and 3, and the streptococcal pyrogenic exotoxin A (speA) play an important role in the pathogenesis of the infection... M protein is an important virulent determinant of GAS; strains lacking M protein are less virulent." (search synthesis, CDC EID 1995 review; PubMed 9331631)

The most common GAS *emm* genotypes associated with STSS/shock and multiorgan damage are **emm1, emm3, emm12, emm28, and emm89**, with the hypervirulent **M1_UK** lineage recently replacing M1_global in some regions (PMC10825083; PMC11705883, Argentina 2023 genomic surveillance). Mutations in the **CovRS two-component regulatory system** are implicated in the switch to an invasive/toxigenic phenotype.

### Risk Factors

**Genetic risk factors:**
- **HLA class II alleles** strongly determine the magnitude of the anti-TSST-1 antibody response: **HLA-DRB1\*03:01** and **HLA-DQB1\*02:01** are positively associated, while **HLA-DRB1\*01:01** and **HLA-DQB1\*05:01** are negatively associated with anti-TSST-1 antibody titers (PMC10507260). Women who fail to seroconvert after TSST-1 exposure may carry HLA class II genotypes associated with a genetically higher intrinsic risk of TSS.
- **Absence or low titer of neutralizing anti-TSST-1 antibody** is considered a core host-susceptibility factor — classic work by Bonventre/Parsonnet-era investigators found antibody levels in TSS cases were significantly lower than in matched controls without a TSS history (search synthesis; PMID:6491377; PMID:17340193).

**Environmental / behavioral risk factors:**
- Use of high-absorbency tampons (historically superabsorbent polyacrylate-containing tampons, withdrawn from market in 1980); **tampon oxygen content** appears more strongly associated with TSS risk than absorbency or chemical composition per se (ScienceDirect 089543569090105X).
- Nasal packing after nasal/sinus surgery — "Nasal packing was used in all patients with TSS and in 98% of all patients" in one post-nasal-surgery case series (PMID:3942641).
- Surgical wound infection, postpartum/puerperal infection, burns, retained foreign bodies (diaphragms, cervical caps, dialysis catheters), skin/soft-tissue infection or varicella superinfection, recent influenza infection, and immunocompromised states.
- 15–33% of TSS cases occur without an identifiable predisposing risk factor (StatPearls NBK459345).

### Protective Factors
- **Circulating neutralizing antibody to TSST-1 (or to the relevant streptococcal exotoxins)** is the principal known protective factor; most adults acquire protective anti-TSST-1 antibody through subclinical colonization/exposure over time.
- Removal of superabsorbent tampon formulations from the U.S. market (early 1980s) was followed by a marked decline in menstrual TSS incidence (from 6–12/100,000 in 1980 to ~1/100,000 by 1986) (CDC MMWR historical surveillance).
- Beta-lactamase-resistant antistaphylococcal antibiotic therapy after a first episode reduces recurrence risk.

### Gene-Environment Interactions
The clearest documented gene-environment interaction is between **HLA class II genotype and toxin exposure**: "Both toxin exposure and HLA alleles affect the human antibody response to TSST-1" (PMC10507260) — i.e., an individual's genetically determined capacity to mount a neutralizing humoral response, combined with the degree/duration of environmental toxin exposure (e.g., prolonged high-absorbency tampon use enabling *S. aureus* toxin elaboration in a low-oxygen vaginal microenvironment), jointly determines whether clinical TSS develops after colonization.

---

## 3. Phenotypes

TSS phenotypes span symptoms, physical signs, and laboratory abnormalities, with an abrupt onset and rapid (24–48 hour) progression.

### Symptoms / Early Prodrome
- Sudden-onset high fever, chills, headache, sore throat, vomiting, watery diarrhea, and severe myalgia, typically preceding hypotension and rash by 24–48 hours (search synthesis; HPO suggestion: **HP:0001945** Fever; **HP:0002018** Nausea and vomiting; **HP:0002014** Diarrhea; **HP:0003326** Myalgia).

### Clinical Signs / Physical Manifestations
- **Diffuse macular erythroderma** ("sunburn-like rash") — HP:0000988 Skin rash / a more specific erythroderma term.
- **Desquamation**, classically palms/soles, occurring 1–2 weeks after rash onset, with full-thickness peeling — HP:0025044 (Desquamation) if available in HPO, or closest matching term.
- **Strawberry tongue** and mucosal hyperemia (oropharyngeal, conjunctival, vaginal) — HP:0031013 (Strawberry tongue).
- **Hypotension / shock** — HP:0002615 (Hypotension) / HP:0001744-adjacent shock terminology.
- Peripheral edema, non-pitting edema of hands/feet.
- Altered mental status/disorientation without focal neurologic deficits — HP:0007018 (Attention deficit) is not ideal; better: HP:0000733 (Agitation) or generically HP:0002360 (Sleep disturbance) — most fitting is a general "confusion"/"altered consciousness" term (HP:0031466 Confusion or HP:0002015-related encephalopathy term).
- Soft-tissue necrosis / necrotizing fasciitis in STSS — HP:0032658 (Skin ulcer)-adjacent or necrosis-specific term.
- Conjunctival injection/hyperemia — HP:0000585 (Conjunctivitis) or HP:0000998-adjacent.

### Laboratory Abnormalities
- Elevated creatine phosphokinase (≥2× ULN) — reflecting myositis/muscle injury.
- Elevated BUN/creatinine (≥2× ULN) or sterile pyuria (≥5 WBC/hpf).
- Elevated bilirubin/transaminases (≥2× ULN) — hepatic involvement.
- **Thrombocytopenia** (platelets ≤100,000/mm³), often DIC-pattern coagulopathy with prolonged clotting times, low fibrinogen, elevated fibrin degradation products.
- Leukocytosis or leukopenia with bandemia/left shift.
- **Hypocalcemia** — described as "prominent throughout the disease" in StatPearls (NBK459345).
- Negative blood/CSF cultures for other pathogens (part of the case-definition exclusionary lab criteria); blood cultures *may* be positive for *S. aureus* in staphylococcal TSS (unlike STSS, where blood cultures are frequently positive for GAS).

### Phenotype Characteristics
- **Age of onset**: any age; menstrual TSS peaks in females aged 15–19 (incidence 1.52/100,000); pediatric STSS is well described; elderly patients with STSS have notably worse prognosis.
- **Severity**: variable, ranging from moderate illness to fulminant multi-organ failure and death within 24–96 hours, especially in STSS.
- **Progression**: acute and rapid — "signs of soft tissue infection... can lead to necrotizing fasciitis... kills 30–60% of patients in 72–96 hours" (search synthesis on STSS/necrotizing fasciitis).
- **Frequency of organ involvement**: by CDC case definition, ≥3 organ systems must be involved for a probable/confirmed staphylococcal TSS diagnosis (GI, muscular, mucous membrane, renal, hepatic, hematologic, CNS).

### Quality of Life Impact
Long-term survivor data (see Outcome/Prognosis, §11) document persistent sequelae — cognitive/memory complaints, new-onset allergies, Raynaud phenomenon, dermatitis, and organ-specific hospitalization risk — that can meaningfully affect post-illness quality of life, though most patients recover without major long-term handicap if treated early (toxicshock.com "After TSS"; PMC via ScienceDirect Long-term outcomes cohort study, J Infect 2024).

---

## 4. Genetic/Molecular Information

TSS is **not caused by a germline pathogenic variant** in a human disease gene — there is no "causal gene" in the Mendelian sense. The molecular basis instead resides in **bacterial virulence genes**:

- **Staphylococcal TSST-1**: encoded by the *tst* gene, carried on a mobile pathogenicity island (SaPI) in a subset of *S. aureus* strains; also relevant are *sea*/*sec* enterotoxin genes (staphylococcal enterotoxin B/C) as alternative superantigens.
- **Streptococcal exotoxins**: *speA*, *speB*, *speC* genes in *S. pyogenes*, with M-protein (*emm* gene) serotype and *covRS* regulatory mutations modulating invasiveness/toxin expression.

### Host Genetic Modifiers
- **HLA-DRB1/DQB1 class II haplotypes** (see §2) modulate the strength and quality of the anti-TSST-1 antibody response and thus host susceptibility — this is the best-characterized human genetic modifier locus for TSS. (HGNC: HLA-DRB1, HLA-DQB1)
- No pathogenic germline variant classification (ACMG/AMP), allele frequency in gnomAD, or somatic/germline distinction applies in the conventional sense, since TSS pathophysiology is toxin-driven rather than variant-driven.

### Epigenetic / Chromosomal Information
No disease-specific epigenetic signature or chromosomal abnormality has been established for TSS; this section is **not applicable** in the classical Mendelian-disease sense. (Bacterial mobile genetic elements — SaPIs carrying *tst* — are the closest analogous "genomic structural feature," but these are bacterial, not human, genomic elements.)

---

## 5. Environmental Information

### Environmental Factors
- Superabsorbent tampon materials (historically carboxymethylcellulose/polyacrylate rayon blends) that increase vaginal oxygen tension and *S. aureus* toxin elaboration.
- Nasal packing materials/tampons used post-surgically.
- Retained barrier contraceptive devices (diaphragms, cervical caps, contraceptive sponges).
- Surgical wound environments, burns, and postpartum uterine environment as niches for toxigenic organism proliferation.

### Lifestyle Factors
- Duration of tampon use per cycle and continuous (rather than intermittent) tampon wear.
- Not using tampons does not eliminate risk — cases have been documented in women colonized by TSST-1-producing *S. aureus* who never used tampons, including recurrent TSS despite abstaining from tampon use post-first episode (Lancet Infect Dis systematic review, PMID:31151811).

### Infectious Agents
- ***Staphylococcus aureus*** (toxigenic, TSST-1/SEB/SEC-producing strains, MSSA and MRSA) — NCBI Taxonomy: NCBITaxon:1280.
- ***Streptococcus pyogenes*** (Group A Streptococcus) — NCBITaxon:1314; rarely group C/G streptococci.
- Antecedent viral infection (e.g., influenza, varicella) creating a portal for secondary toxigenic bacterial superinfection is a recognized non-menstrual TSS risk context.

---

## 6. Mechanism / Pathophysiology

### Causal Chain (Upstream → Downstream)

1. **Colonization/infection** with a toxigenic strain (vaginal *S. aureus* colonization in mTSS; wound/soft-tissue GAS infection in STSS) in a host lacking protective neutralizing antibody.
2. **Superantigen exotoxin production** (TSST-1, SEB/SEC for staph; SpeA/B/C for strep) in a permissive microenvironment (e.g., elevated vaginal O₂ tension from tampon use; devitalized/necrotic tissue in soft-tissue infection).
3. **Non-conventional MHC-II/TCR cross-linking**: the superantigen binds directly to MHC class II molecules on antigen-presenting cells *outside* the conventional peptide-binding groove, and simultaneously to the **variable β (Vβ) chain of the T-cell receptor**, bypassing normal antigen-specific presentation.

   > "TSST-1... binds to the MHC class II outside the antigen presentation site and the variable beta (Vβ) chain of the T-cell receptor... leading to nonspecific, polyclonal lymphocyte activation of 5-30% of the total population of T cells." (search synthesis on superantigen mechanism; PMC6468478, "Staphylococcal Superantigens: Pyrogenic Toxins Induce Toxic Shock")

4. **Massive polyclonal T-cell activation and cytokine storm**: activated T cells and macrophages release **TNF-α, TNF-β, IL-1β, IL-2, IL-6, and IFN-γ**, plus chemokines such as macrophage chemoattractant protein-1 (MCP-1). Downstream signaling includes **MAPK cascades, NF-κB activation, and PI3K/Akt/mTOR pathway engagement**.
5. **Systemic inflammatory/vascular effects**: cytokine-mediated **capillary leak**, vasodilation, endothelial activation/dysfunction (demonstrated directly on human aortic endothelial cells, PMID:29229737), and disseminated microvascular injury.
6. **Clinical manifestation**: fever, diffuse erythroderma, profound hypotension/distributive shock, and multi-organ dysfunction (renal, hepatic, hematologic/coagulopathy, muscular, CNS), with desquamation as a late cutaneous sequela of the acute inflammatory insult.
7. In **STSS**, a parallel/overlapping mechanism involves **M-protein-mediated antiphagocytic virulence**, enabling invasive soft-tissue infection and **necrotizing fasciitis**, compounding shock with local tissue destruction and a markedly higher case-fatality rate than staphylococcal TSS.

### Cellular Processes
- T-lymphocyte hyperactivation and clonal (Vβ-restricted) expansion (e.g., TRBV12-3/12-4+ memory T cells specifically activated by SpeC and TSST-1; PMC9854414).
- Macrophage/monocyte activation and inflammatory cytokine secretion.
- Vaginal/epithelial cell activation — TSST-1 interacts with **CD40** on vaginal epithelial cells to stimulate chemokine production that facilitates local T-cell/macrophage activation (search synthesis; PMC6426597).
- Suppression of epithelial autophagy by TSST-1 (PMC4234639).
- Endothelial dysfunction and vascular leak.
- Neutrophil/complement-mediated tissue injury in soft-tissue necrosis (STSS).

### Suggested Ontology Terms
- **GO:0002347** (response to bacterial pathogen-associated pattern) / **GO:0035723** (interleukin-6-mediated signaling pathway) / **GO:0033209** (tumor necrosis factor-mediated signaling pathway) / **GO:0043123** (positive regulation of I-kappaB kinase/NF-kappaB signaling) for the cytokine/NF-κB cascade.
- **GO:0002827** (positive regulation of T-helper 1 type immune response) / **GO:0042104** (positive regulation of activated T cell proliferation) for polyclonal T-cell activation.
- **CL:0000084** (T cell), **CL:0000235** (macrophage), **CL:0000738** (leukocyte), **CL:0000115** (endothelial cell), **CL:0002144** (capillary endothelial cell) for cell types involved.
- **CHEBI**: TSST-1 and streptococcal pyrogenic exotoxins are proteins rather than small molecules and are better represented as UniProt/GO molecular entities than CHEBI terms.

---

## 7. Anatomical Structures Affected

### Organ Level
- **Primary**: skin/integument (rash, desquamation), cardiovascular system (hypotension/distributive shock), and the primary infectious site (vaginal mucosa in mTSS; skin/soft tissue, surgical wound, or uterus in nmTSS/STSS).
- **Secondary/multisystem**: kidneys (acute kidney injury, often an *early* sign preceding hypotension), liver (transaminitis, hyperbilirubinemia), hematologic system (thrombocytopenia, DIC), skeletal muscle (myositis, elevated CPK), gastrointestinal tract (vomiting, diarrhea), and central nervous system (encephalopathy/confusion).
- **Body systems involved**: integumentary, cardiovascular, renal, hepatic, hematologic/immune, musculoskeletal, gastrointestinal, and (in severe STSS) the deep soft-tissue/fascial plane.

Suggested **UBERON** terms: UBERON:0002097 (skin epidermis), UBERON:0000178 (blood), UBERON:0002113 (kidney), UBERON:0002107 (liver), UBERON:0001134 (skeletal muscle tissue), UBERON:0000948 (heart)/UBERON:0001981 (blood vessel) for the vasculature, UBERON:0000996 (vagina) for the mTSS primary site, UBERON:0002097-adjacent fascia term for STSS necrotizing fasciitis.

### Tissue and Cell Level
- Vaginal squamous epithelium (site of TSST-1 elaboration and CD40-mediated chemokine induction in mTSS).
- Vascular endothelium (aortic/capillary endothelial dysfunction).
- Deep fascia and subcutaneous soft tissue (necrotizing fasciitis in STSS).
- Peripheral blood T lymphocytes and monocytes/macrophages as the principal toxin-responsive cell populations.

### Subcellular Level
- MHC class II molecules at the plasma membrane of antigen-presenting cells (**GO:0042613**, MHC class II protein complex) — the direct molecular docking site for superantigen.
- Signal transduction machinery: NF-κB pathway components (nuclear translocation), MAPK cascade proteins, PI3K/Akt/mTOR pathway components — largely cytoplasmic/nuclear.

### Localization
Bilateral/systemic — TSS is a systemic toxin-mediated disease without lateralization; cutaneous rash is typically diffuse and symmetric.

---

## 8. Temporal Development

### Onset
- **Age**: can occur at any age (neonatal through geriatric); menstrual TSS is essentially confined to menstruating individuals (peak 15–19 years); pediatric non-menstrual TSS and STSS are well documented (PMID:29601458, "Epidemiology and Clinical Relevance of Toxic Shock Syndrome in US Children").
- **Onset pattern**: acute — sudden onset of fever/flu-like prodrome, with hypotension, rash, and multi-organ involvement developing within 24–48 hours.

### Progression
- **Disease course**: rapid and fulminant, particularly STSS with necrotizing fasciitis, which "kills 30–60% of patients in 72–96 hours" absent aggressive intervention.
- **Progression rate**: STSS-associated mortality has been reported to exceed 25% within the first 24 hours in some cohorts.
- **Disease duration**: acute, self-limited illness with appropriate treatment (source control + antibiotics + supportive care); desquamation phase resolves over 1–2+ weeks after the acute illness.
- Recurrence is well documented in menstrual TSS (up to ~14/44 cases in early cohorts having ≥1 recurrence), particularly without antistaphylococcal antibiotic therapy or continued tampon use; recurrence can occur even after tampon cessation in colonized women.

### Patterns
- **Remission**: typically treatment-induced (source control + antibiotics + supportive/ICU care) rather than spontaneous, though the disease is not chronic — surviving patients generally achieve full clinical resolution of the acute episode.
- **Critical periods**: early recognition and rapid initiation of source control (tampon/foreign body removal, wound debridement) plus toxin-suppressing antibiotic therapy (clindamycin) within the first hours of presentation are repeatedly emphasized as the key modifiable window affecting mortality.

---

## 9. Inheritance and Population

### Epidemiology
- **Overall U.S. incidence**: ~0.8–3.4 per 100,000 (StatPearls NBK459345), though estimates vary substantially by era and surveillance method.
- **Menstrual TSS incidence**: historically 6–12/100,000 women aged 12–49 (1980), declining to ~1/100,000 women 15–44 by 1986 following superabsorbent tampon withdrawal; current estimates ~0.5–1.0/100,000; peak incidence 1.52/100,000 in women 15–19.
- **Non-menstrual TSS**: now exceeds menstrual TSS incidence; by 1986, menstrual vs. non-menstrual rates were roughly 1 vs. 0.3/100,000, with the gap subsequently reversing.
- **Streptococcal TSS (STSS)**: annual incidence ~1/300,000–1/1,000,000 per Orphanet; alternative estimates of 2–4 cases per 100,000 per year have also been reported; STSS accounts for ~4% of invasive GAS disease overall.
- **Worldwide bacterial TSS prevalence**: estimated at ~1/30,000 (Orphanet).

### Inheritance Pattern
TSS is **not a Mendelian genetic disease** — there is no inheritance pattern (AD/AR/X-linked/mitochondrial) in the classical sense. Susceptibility is polygenic/immunogenetic, chiefly modulated by **HLA class II genotype**, which affects antibody-mediated protection but does not itself "cause" disease. Penetrance, expressivity, anticipation, germline mosaicism, and carrier-frequency concepts are not applicable.

### Population Demographics
- **Sex ratio**: menstrual TSS is essentially female-only by definition; across all TSS (menstrual + non-menstrual), approximately 85% of cases occur in females and 15% in males (search synthesis).
- **Race/ethnicity**: historical U.S. surveillance found higher menstrual TSS incidence in white women than non-white women (1.21/100,000 vs. 0.34/100,000).
- **Age distribution**: bimodal relevance — menstrual TSS peaks in adolescent/young adult females (15–19 years); non-menstrual and streptococcal TSS occur across the age spectrum, with STSS notably more severe/lethal in elderly patients.
- **Geographic distribution**: occurs worldwide; STSS/invasive GAS disease shows regional variation in dominant *emm* genotypes (e.g., emm1/M1_UK lineage replacement documented in parts of Europe; emm1-global and hypervirulent emm1 lineages highlighted in South American surveillance).
- **Seasonality**: StatPearls notes TSS occurs year-round but with somewhat higher winter prevalence, and increased frequency reported in developing nations.

---

## 10. Diagnostics

### Clinical Case Definition (CDC, 2011 — Staphylococcal TSS)

All five clinical criteria are required for a **confirmed** case (or death before desquamation occurs); four of five plus laboratory criteria define a **probable** case:

1. **Fever**: temperature ≥102.0°F (≥38.9°C)
2. **Rash**: diffuse macular erythroderma
3. **Desquamation**: 1–2 weeks after rash onset (palms/soles classically)
4. **Hypotension**: systolic BP ≤90 mmHg (adults) or <5th percentile for age (children <16)
5. **Multisystem involvement** (≥3 of the following):
   - Gastrointestinal (vomiting or diarrhea at onset)
   - Muscular (severe myalgia or CPK ≥2× ULN)
   - Mucous membrane (vaginal, oropharyngeal, or conjunctival hyperemia)
   - Renal (BUN/creatinine ≥2× ULN, or pyuria ≥5 WBC/hpf without UTI)
   - Hepatic (bilirubin or transaminases ≥2× ULN)
   - Hematologic (platelets <100,000/mm³)
   - CNS (disorientation/altered consciousness without focal signs, in the absence of fever/hypotension)

**Laboratory criteria**: negative blood/CSF cultures (blood culture *may* be positive for *S. aureus*) and negative serologies for Rocky Mountain spotted fever, leptospirosis, and measles. (Source: CDC National Notifiable Diseases case-definition portal, ndc.services.cdc.gov)

**Streptococcal TSS** clinical criteria are analogous but require hypotension **plus** ≥2 of: renal impairment, coagulopathy, hepatic involvement, ARDS, generalized erythematous macular rash, and soft-tissue necrosis/necrotizing fasciitis, together with **isolation of *S. pyogenes*** (from a sterile site for a confirmed case; non-sterile site for probable).

### Laboratory Tests
- No single specific diagnostic test exists; diagnosis is clinical/syndromic per case-definition criteria.
- CBC (leukocytosis or leukopenia with bandemia, thrombocytopenia, anemia), comprehensive metabolic panel (renal/hepatic function), creatine phosphokinase, coagulation studies (PT/PTT, fibrinogen, D-dimer for DIC), blood/wound/vaginal cultures.
- Acute kidney injury is frequently the **earliest** organ-injury sign, often preceding hypotension.
- Hypocalcemia is a notable and prominent laboratory abnormality throughout the illness course.

### Genetic Testing
Not applicable/not indicated for diagnosis — TSS is not diagnosed via genetic testing (no WGS/WES/gene panel/CMA/karyotype role), reflecting its infectious/toxin-mediated (not germline) etiology. HLA typing has research relevance for susceptibility studies but is not part of routine clinical diagnostics.

### Imaging / Other
CT/MRI may be used adjunctively to evaluate for necrotizing fasciitis extent or abscess/retained foreign body in non-menstrual TSS, but imaging is not part of the core case definition.

### Differential Diagnosis
Scarlet fever, Kawasaki disease, meningococcemia, toxic epidermal necrolysis/Stevens-Johnson syndrome, necrotizing fasciitis (as a co-occurring/overlapping entity in STSS), drug eruptions, erythema multiforme, and — in pediatric populations — multisystem inflammatory syndrome in children (MIS-C) (PMC10056689, comparative pediatric study of MIS-C, Kawasaki disease, and TSS).

### Screening
No population-based screening program exists; risk-reduction counseling (tampon absorbency/duration, foreign-body management) functions as informal primary prevention rather than formal screening.

---

## 11. Outcome/Prognosis

### Survival and Mortality
- **Staphylococcal (non-streptococcal) TSS**: case-fatality generally **<3%**, with some modern series citing an overall range of 1.8–12%.
- **Streptococcal TSS (STSS)**: substantially higher mortality — commonly cited as **30–60%**, with some sources reporting up to **80% in adults** versus **5–8% in children**; a Japanese nationwide investigation found an overall mortality rate of **45%**; STSS-associated mortality can **exceed 25% within the first 24 hours**.
- When STSS is complicated by **necrotizing fasciitis**, mortality of **30–60% within 72–96 hours** has been reported.
- STSS accounts for a small fraction (~4%) of invasive GAS disease overall but disproportionately drives GAS-associated mortality (~38% case-fatality cited for STSS specifically in some series).
- Delayed diagnosis/treatment is consistently identified as a major driver of increased mortality across both staphylococcal and streptococcal TSS.

### Morbidity and Long-Term Function
- Reported long-term sequelae in survivors include: late-onset rash, compromised renal function, cyanotic extremities, prolonged neuromuscular abnormalities, dermatitis, new-onset allergies, and **Raynaud phenomenon**.
- Neurocognitive sequelae are notable: EEG abnormalities, difficulty concentrating, headache, and memory lapses are described post-recovery, with one study finding survivors had **reduced left hippocampal volume** compared to healthy controls.
- A recent matched cohort study (J Infect 2024) found TSS "strongly associated with the risk of renal, cardiovascular, and hepatic hospitalization" in the post-acute period.
- Severe complications include digit/limb gangrene (potentially requiring amputation) and renal failure, though these are described as rare with early, aggressive treatment.
- Overall, "most patients recover completely and without any significant long-term handicap" when treated promptly.

### Prognostic Factors
- Organism (streptococcal >> staphylococcal severity), timeliness of diagnosis/source control, presence/extent of necrotizing soft-tissue infection, patient age (elderly patients with STSS fare markedly worse), and *emm* genotype (emm1/emm3/emm89 associated with more severe invasive disease).

---

## 12. Treatment

### Pharmacotherapy
- **Empiric broad-spectrum antibiotics** pending culture identification, typically including **vancomycin or linezolid** for MRSA coverage.
- **Clindamycin** is added specifically as an **antitoxin/protein-synthesis-inhibiting adjunct** — it suppresses toxin (TSST-1/streptococcal exotoxin) and cytokine production independent of its bactericidal action; "studies demonstrate improved outcomes when clindamycin is added" (StatPearls NBK459345). IDSA recommends **penicillin + clindamycin** combination therapy for confirmed streptococcal TSS.
- Once organism/susceptibility is confirmed: **penicillin** for Group A *Streptococcus*; **clindamycin plus an antistaphylococcal penicillin (nafcillin/oxacillin/flucloxacillin)** for MSSA.
- Typical antibiotic duration: **7–14 days**.
- **NCIT term**: NCIT:C15632 (Chemotherapy) is not appropriate; more fitting is **NCIT:C15986** (Pharmacotherapy), with `therapeutic_agent` bindings to CHEBI (e.g., CHEBI for clindamycin, vancomycin, penicillin, linezolid).

### Advanced/Adjunctive Therapeutics
- **Intravenous immunoglobulin (IVIG)**: proposed mechanism is direct **neutralization of circulating superantigen**. Evidence is mixed:
  - A systematic review/meta-analysis of clindamycin-treated STSS patients found mortality fell from **33.7% to 15.7%** with IVIG "with remarkable consistency across the single randomized and four nonrandomized studies" (PMC6186853; Clin Infect Dis, PMID referenced in search).
  - However, a more recent large observational Japanese nationwide study found **no significant survival benefit** of IVIG after adjustment for confounders, and the single multicenter RCT (Darenberg et al.) was **terminated early due to slow recruitment**.
  - Typical proposed dosing: **high-dose IVIG, ~2 g/kg**, though it remains without definitive RCT-level mortality benefit and guideline recommendations vary.
- **Corticosteroids**: **not recommended** — no demonstrated mortality benefit.

### Surgical/Interventional
- **Immediate removal of the inciting foreign body** (tampon, nasal packing, retained barrier contraceptive/surgical material) is a first-line, urgent intervention.
- **Emergent surgical debridement/source control** for infected/necrotic soft tissue, particularly critical in STSS with necrotizing fasciitis — described as "critical to outcomes."
- **NCIT term**: NCIT:C15329 (Surgical Procedure) / NCIT:C154430 (debridement-related term).

### Supportive Care
- Aggressive IV crystalloid fluid resuscitation for hypotension.
- Vasopressors (**norepinephrine preferred**) for fluid-refractory shock.
- Electrolyte repletion, notably for hypocalcemia.
- **ICU admission mandatory for all patients**; severe cutaneous/desquamating cases may require **burn-unit-level care**.
- **NCIT term**: NCIT:C15747 (Supportive Care).

### Experimental / Preventive Immunotherapy
- **rTSST-1v (recombinant detoxified TSST-1 variant) vaccine** — Phase 1 (PMID:27296693, Lancet Infect Dis 2016) and Phase 2 trials (NCT02814708; PMC10808908, eClinicalMedicine) demonstrate the vaccine is **safe, well-tolerated, and highly immunogenic**: "Seroconversion occurred in >81% of subjects within 3 months of the first immunisation, sustained until 18 months after the third immunisation in over 70% of subjects." This represents a first-in-class active immunoprophylaxis approach targeting the core superantigen mechanism.
- Passive **TSST-1-neutralizing monoclonal/single-chain antibody** approaches have shown protective efficacy in animal models even when administered late in toxin exposure (PMC4073126; PMC9617332).

### Treatment Algorithm Summary
Recognize (case-definition criteria) → remove foreign body/source control → empiric broad-spectrum antibiotics (vancomycin/linezolid + clindamycin) → narrow per culture/organism → aggressive fluid resuscitation ± vasopressors → consider IVIG in refractory/severe STSS → ICU-level supportive care → surgical debridement if soft-tissue necrosis.

---

## 13. Prevention

### Primary Prevention
- Avoidance of superabsorbent tampon formulations (regulatory withdrawal of the highest-absorbency products was a landmark U.S. public-health primary-prevention action in the early 1980s, associated with a large decline in menstrual TSS incidence).
- Guidance on tampon use duration/frequency and alternating with pads to reduce continuous high-absorbency exposure.
- Careful surgical technique and judicious nasal-packing use/duration following nasal/sinus surgery.
- **Immunization**: no licensed vaccine yet exists, but the **rTSST-1v** candidate vaccine (Phase 2 completed) represents an active primary-prevention strategy in development, specifically for individuals at recognized risk (e.g., prior TSS survivors, given documented recurrence risk).

### Secondary Prevention / Early Detection
- Clinical vigilance and rapid application of case-definition criteria in any patient with fever + rash + hypotension, particularly post-surgical, postpartum, or menstruating patients, to enable early source control and antibiotic initiation — repeatedly identified as the single greatest modifiable determinant of survival.
- Recommendation for beta-lactamase-resistant antistaphylococcal antibiotic therapy after a first TSS episode to reduce recurrence.

### Tertiary Prevention
- Post-TSS antistaphylococcal therapy and discontinuation of causative tampon/device use to prevent recurrent episodes, recognizing that recurrence can still occur even after risk-factor removal in colonized individuals.

### Public Health / Chemoprophylaxis
- The CDC does **not** recommend routine screening or chemoprophylaxis for household contacts of streptococcal TSS cases; however, providers "may choose to offer chemoprophylaxis to household members aged ≥65 years or those at increased risk," with a suggested regimen of **7–10 days of oral cephalexin** (StatPearls NBK459345).
- Standard/contact/droplet precautions are recommended for the first 24 hours of effective antibiotic therapy in hospitalized STSS patients.

### Counseling
No formal genetic counseling role exists given the non-Mendelian, infectious nature of TSS; counseling is limited to behavioral/device-use risk-reduction education, particularly for TSS survivors regarding recurrence risk.

---

## 14. Other Species / Natural Disease

### Taxonomy
TSS-like disease is described in **domestic dogs (*Canis lupus familiaris*, NCBITaxon:9615)**, driven by superantigen-producing *Staphylococcus* and *Streptococcus* species.

### Natural Disease in Animals
- **Canine Streptococcal Toxic Shock Syndrome (CSTSS)**: primarily caused by ***Streptococcus canis***, described as "a serious often fatal disease syndrome seen in dogs" (Veterinary World review, veterinaryworld.org).
- Case reports document mixed infections, e.g., *S. aureus*, *Streptococcus halichoeri*, and *Dermatophilus* spp. co-infection producing a toxic shock-like syndrome in a dog (Vet Sci 2025, doi:10.3390/vetsci12080764; PMC12390649).
- Clinical presentation parallels the human disease: superantigen-driven massive TNF-α and inflammatory cytokine release, high fever, hypotension, hemoconcentration, thrombosis, and neutrophil/endothelial activation leading to multi-organ failure.
- No OMIA (Online Mendelian Inheritance in Animals) entry was identified for TSS, consistent with its non-heritable, infectious basis — this is expected given TSS is toxin/infection-driven rather than a Mendelian trait, and is flagged as an appropriate "not applicable" rather than a knowledge gap.

### Comparative Biology
The **rabbit** is considered the classic experimental model of choice for human TSS specifically because of its comparable sensitivity to staphylococcal/streptococcal superantigens (see Model Organisms, §15) — this cross-species conservation of superantigen sensitivity underscores that the core MHC-II/TCR superantigen mechanism is broadly conserved across mammals, with canine natural disease representing a spontaneous, naturally occurring parallel to the human syndrome.

### Zoonotic Considerations
TSS itself is not classically zoonotic (human and canine cases arise from largely host-adapted or opportunistic staphylococcal/streptococcal strains rather than direct animal-to-human transmission), though *S. canis* is a recognized opportunistic pathogen that can rarely cause human infection.

---

## 15. Model Organisms

### Rabbit Model (Primary Model)
The rabbit is explicitly identified as **"the experimental model of choice because it is comparable to humans in its sensitivity to superantigens"** (search synthesis; PMC3153295, PMID:22069685).
- **Intravaginal TSST-1 administration** in rabbits produces **100% lethality** in unprotected controls, closely modeling menstrual TSS.
- **Multiple-dose lethal-challenge protocols** (repeated dosing over 5 days) are used to model sustained toxin exposure; **TSST-1-neutralizing antibody treatment is fully protective** in this model, including when administered **late** in the course of exposure (PMC4073126) — directly informing the rationale for passive/active immunotherapy development.
- A chronic-exposure rabbit model further demonstrated that **sustained low-level TSST-1 exposure accelerates atherosclerosis progression** (PMC6933490), illustrating a vascular/endothelial dimension of chronic superantigen exposure beyond acute shock.
- TSST-1 mutant analysis in rabbits established that **T-cell activation is mechanistically required** for the biological effects of the toxin, including the cytokine storm itself (PMC3153295).

### Mouse Models
- Wild-type mice are relatively **resistant** to staphylococcal/streptococcal superantigens due to poor toxin-MHC class II binding affinity — a significant **translational limitation**.
- **HLA class II-transgenic mice** (e.g., **HLA-DQ8 transgenic**) overcome this: "Transgenic expression of human HLA class II can render mice superantigen sensitive and allows investigation of superantigen-associated inflammation without the need for sensitization." Spleen cells from HLA-DQ8 transgenic mice show markedly greater TSST-1 sensitivity than wild-type C57BL/6 cells.
- A **transgenic mouse model of staphylococcal soft-tissue infection** was used to evaluate TSST-1 production in vivo and assess antibiotic impact — early clindamycin treatment altered TSST-1 production in soft tissue and immune organs, directly modeling the toxin-suppression rationale for clindamycin adjunctive therapy in human TSS (PMC6796978, mSphere, "Toxic Shock Syndrome Toxin 1 Evaluation and Antibiotic Impact in a Transgenic Model of Staphylococcal Soft Tissue Infection").

### Model Characteristics: Fidelity and Limitations
- **Recapitulation**: both rabbit and HLA-transgenic mouse models successfully reproduce the core superantigen-driven cytokine storm and lethality; the rabbit model in particular captures the acute lethal shock phenotype with high fidelity.
- **Limitations**: standard (non-transgenic) mouse strains fail to recapitulate human-relevant superantigen sensitivity because murine MHC class II binds staphylococcal/streptococcal superantigens poorly — this is a well-recognized **species-specific translational gap**, addressed only by HLA-humanized transgenic approaches. Rabbit models, while pharmacodynamically closer to human superantigen sensitivity, do not fully capture the human menstrual/vaginal microbiome context in which TSST-1 is naturally elaborated.

### Applications
- Rabbit and HLA-transgenic mouse models have been used to: (1) establish the causal, T-cell-activation-dependent mechanism of superantigen-induced cytokine storm and lethality; (2) test **neutralizing antibody** therapeutics (fully protective even late in exposure); (3) evaluate the **rTSST-1v vaccine candidate's** immunogenicity prior to human trials; and (4) evaluate **antibiotic (clindamycin) impact on in vivo toxin production**, directly supporting current clinical antitoxin treatment strategy.

### Resources
No dedicated TSS-specific model-organism database exists; relevant models are documented in the primary immunology/infectious-disease literature cited above rather than centralized repositories like MGI/IMPC (reflecting that these are typically custom-generated transgenic/challenge models rather than heritable knockout lines cataloged for a Mendelian phenotype).

---

## Summary of Suggested Ontology Term Bindings for KB Curation

| Category | Suggested Term(s) |
|---|---|
| Disease identifiers | ICD-10-CM A48.3; ICD-11 1C45 / 1C45.0; ORPHA:36234 (bacterial TSS); ORPHA:99918 (streptococcal TSS); MONDO term to be confirmed via OLS lookup |
| Causal organisms | NCBITaxon:1280 (*Staphylococcus aureus*); NCBITaxon:1314 (*Streptococcus pyogenes*) |
| Causal gene (bacterial virulence) | *tst* (TSST-1), *sea*/*sec* (staph enterotoxins), *speA*/*speB*/*speC* (strep exotoxins) — bacterial, not HGNC-mapped |
| Host modifier genes | HLA-DRB1, HLA-DQB1 (HGNC) |
| Key phenotypes (HP) | Fever HP:0001945; Hypotension HP:0002615; Strawberry tongue HP:0031013; Myalgia HP:0003326; Diarrhea HP:0002014; Thrombocytopenia HP:0001873 |
| Molecular mechanism (GO) | MHC class II protein complex GO:0042613; TNF-mediated signaling GO:0033209; positive regulation of T cell proliferation GO:0042129/GO:0042104 |
| Cell types (CL) | CL:0000084 T cell; CL:0000235 macrophage; CL:0000115 endothelial cell |
| Anatomy (UBERON) | UBERON:0002097 skin; UBERON:0000996 vagina; UBERON:0002113 kidney; UBERON:0002107 liver |
| Treatments (NCIT) | NCIT:C15986 Pharmacotherapy (clindamycin, vancomycin, penicillin — CHEBI-bound `therapeutic_agent`); NCIT:C15329 Surgical Procedure; NCIT:C15747 Supportive Care |
| Model organisms | Rabbit (*Oryctolagus cuniculus*); HLA-DQ8-transgenic mouse |

**Key knowledge gaps flagged for curation**: no confirmed dedicated MONDO ID was retrieved in this search pass (should be verified directly against the MONDO OLS browser); IVIG mortality benefit remains genuinely contested in the primary literature (meta-analytic pooled benefit vs. large adjusted observational null-result) and should be curated as a `HUMAN_MODEL_MISMATCH`/conflicting-evidence discussion rather than a settled treatment-efficacy claim; no OMIA entry exists for the canine analog, consistent with the non-heritable, infectious nature of the disease.

---

### Sources

- [Toxic Shock Syndrome: A Literature Review (PMC10812596 / PMID:38247655)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10812596/)
- [Toxic Shock Syndrome - StatPearls (NCBI Bookshelf NBK459345)](https://www.ncbi.nlm.nih.gov/books/NBK459345/)
- [Toxic Shock Syndrome (Other Than Streptococcal) 2011 Case Definition | CDC](https://ndc.services.cdc.gov/case-definitions/toxic-shock-syndrome-2011/)
- [Orphanet: Bacterial toxic shock syndrome](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=36234)
- [Orphanet: Streptococcal toxic shock syndrome](https://www.orpha.net/en/disease/detail/99918)
- [2026 ICD-10-CM Diagnosis Code A48.3](https://www.icd10data.com/ICD10CM/Codes/A00-B99/A30-A49/A48-/A48.3)
- [The Superantigen Toxic Shock Syndrome Toxin 1 Alters Human Aortic Endothelial Cell Function (PMID:29229737)](https://pubmed.ncbi.nlm.nih.gov/29229737/)
- [TSST-1 promotes colonization of Staphylococcus aureus within the vaginal tract by activation of CD8+ T cells](https://journals.asm.org/doi/10.1128/iai.00439-24)
- [Staphylococcal Superantigens Stimulate Epithelial Cells through CD40 To Produce Chemokines (PMC6426597)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6426597/)
- [Suppression of Starvation-Induced Autophagy by Recombinant TSST-1 in Epithelial Cells (PMC4234639)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4234639/)
- [Streptococcal Toxic-Shock Syndrome: Spectrum of Disease, Pathogenesis, and New Concepts in Treatment — CDC EID 1995](https://wwwnc.cdc.gov/eid/article/1/3/95-0301_article)
- [Staphylococcal Superantigens: Pyrogenic Toxins Induce Toxic Shock (PMC6468478)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6468478/)
- [PI3K/Akt/mTOR, a Pathway Less Recognized for Staphylococcal Superantigen-Induced Toxicity (PMC3509712)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3509712/)
- [The superantigens SpeC and TSST-1 specifically activate TRBV12-3/12-4+ memory T cells (PMC9854414)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9854414/)
- [Reduced Incidence of Menstrual Toxic-Shock Syndrome — United States, 1980-1990 (CDC MMWR)](https://www.cdc.gov/mmwr/preview/mmwrhtml/00001651.htm)
- [Toxic shock syndrome in the United States: surveillance update, 1979-1996 (PMC2640799)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2640799/)
- [Staphylococcal Toxic Shock Syndrome 2000–2006: Epidemiology, Clinical Features, and Molecular Characteristics (PMC3157910)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3157910/)
- [Device-Associated Menstrual Toxic Shock Syndrome | Clinical Microbiology Reviews](https://journals.asm.org/doi/10.1128/cmr.00032-19)
- [Tampon absorbency, composition and oxygen content and risk of TSS](https://www.sciencedirect.com/science/article/abs/pii/089543569090105X)
- [Toxic shock syndrome after nasal surgery: Case reports and analysis of risk factors (PMID:3942641)](https://pubmed.ncbi.nlm.nih.gov/3942641/)
- [Toxin exposure and HLA alleles determine serum antibody binding to TSST-1 (PMC10507260)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10507260/)
- [Polyspecific IVIG in Clindamycin-treated Patients With Streptococcal TSS: Systematic Review and Meta-analysis (PMC6186853)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6186853/)
- [Clinical Efficacy of IVIG in Management of Toxic Shock Syndrome: Updated Literature Review (PMC7896483)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7896483/)
- [Staphylococcal Superantigen (TSST-1) Mutant Analysis... in the Rabbit (PMC3153295 / PMID:22069685)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3153295/)
- [Chronic S. aureus Superantigen TSST-1 Exposure Accelerates Atherosclerosis in Rabbits (PMC6933490)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6933490/)
- [Toxic Shock Syndrome Toxin 1 Evaluation and Antibiotic Impact in a Transgenic Model of Staphylococcal Soft Tissue Infection (PMC6796978)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6796978/)
- [TSST-1-Mediated Toxicity Inhibited by Neutralizing Antibodies Late in Continual Exposure (PMC4073126 / PMID:24887085)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4073126/)
- [High Titer Persistent Neutralizing Antibodies Induced by TSST-1 Variant Vaccine (PMC7601046 / PMID:33023185)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7601046/)
- [Safety, tolerability, and immunogenicity of rTSST-1 variant vaccine: first-in-man trial (PMID:27296693)](https://pubmed.ncbi.nlm.nih.gov/27296693/)
- [A randomized, double-blind study on safety and immunogenicity of rTSST-1 variant vaccine: phase 2 results (PMC10808908 / PMID:38274114)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10808908/)
- [Clinical Trial of the BioMed rTSST-1 Variant Vaccine — NCT02814708](https://clinicaltrials.gov/study/NCT02814708)
- [Menstrual toxic shock syndrome: case report and systematic review of the literature (PMID:31151811)](https://pubmed.ncbi.nlm.nih.gov/31151811/)
- [Epidemiology and Clinical Relevance of Toxic Shock Syndrome in US Children (PMID:29601458)](https://pubmed.ncbi.nlm.nih.gov/29601458/)
- [Clinical characteristics of children with group A streptococcal TSS admitted to PICUs (PMID:20981441)](https://pubmed.ncbi.nlm.nih.gov/20981441/)
- [Comparison of MIS-C, Kawasaki Disease and Toxic Shock Syndrome in Children (PMC10056689)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10056689/)
- [Streptococcal toxic shock syndrome caused by dissemination of an invasive emm3/ST15 strain (PMC5735678 / PMID:29254479)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5735678/)
- [Toxic Shock Syndrome (TSS) Caused by Group A Streptococcus: Novel Insights (PMC11074494)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11074494/)
- [Genomic epidemiology of invasive GAS infections in Argentina, 2023 (PMC11705883)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11705883/)
- [Clinical and molecular epidemiological features of critically ill patients with invasive GAS infections: Belgian multicenter case-series (PMC10825083)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10825083/)
- [Long-term outcomes of patients with toxic shock syndrome: A matched cohort study — Journal of Infection 2024](https://www.journalofinfection.com/article/S0163-4453(24)00147-6/fulltext)
- [After TSS — toxicshock.com](https://www.toxicshock.com/healthprofessionalsinfo/aftertss.cfm)
- [Case Report of Toxic Shock-like Syndrome in a Dog (Vet Sci 2025 / PMC12390649)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12390649/)
- [Canine Streptococcal Toxic Shock Syndrome — Veterinary World](https://www.veterinaryworld.org/Vol.5/May%202012/Canine%20Streptococcal%20Toxic%20Shock%20Syndrome%20associated%20with.pdf)
- [Structural and functional properties of antibodies to the superantigen TSST-1 (PMID:17340193)](https://pubmed.ncbi.nlm.nih.gov/17340193/)
- [Antibody responses to TSS toxin by patients with TSS and healthy staphylococcal carriers (PMID:6491377)](https://pubmed.ncbi.nlm.nih.gov/6491377/)