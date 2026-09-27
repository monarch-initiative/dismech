---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-10T03:44:23.766730'
end_time: '2026-08-10T03:49:17.982753'
duration_seconds: 294.22
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Pericarditis
  mondo_id: ''
  category: Complex
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
  web_search_requests: 15
  num_turns: 19
  total_cost_usd: 1.8004848000000004
  session_id: ccd9973f-d61b-50a6-8cfe-0a77b122d0f2
  stop_reason: end_turn
citation_count: 3
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Pericarditis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Pericarditis** covering all of the
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

I have sufficient sourced material. Given this task calls for producing the research report directly (not curating the KB), I won't pursue further repo tool access and will proceed to write the full report, flagging ontology terms as suggestions for curator verification (per this repo's own anti-hallucination policy).

# Pericarditis: Comprehensive Disease Characteristics Research Report

## 1. Disease Information

**Overview.** Pericarditis is inflammation of the pericardium — the fibroserous sac (visceral + parietal layers separated by a potential space normally containing 15–50 mL of fluid) surrounding the heart. It is the most common disease of the pericardium and presents across a clinical spectrum: acute pericarditis, incessant pericarditis (>4–6 weeks but <3 months, continuous), recurrent pericarditis (relapse after a symptom-free interval of ≥4–6 weeks), chronic pericarditis (>3 months), and, as a downstream sequela, constrictive pericarditis (fibrotic, calcified, non-compliant pericardium impairing diastolic filling). The 2025 ESC Guidelines for the management of myocarditis and pericarditis (the first *integrated* ESC guideline covering both conditions) introduce the umbrella concept of "inflammatory myopericardial syndrome" (IMPS) reflecting shared etiopathogenesis and frequent myopericardial overlap (myopericarditis/perimyocarditis) (Eur Heart J 2025; https://academic.oup.com/eurheartj/article/46/40/3952/8234483).

**Key identifiers** (to be OAK-verified before KB entry, per dismech policy):
- **MONDO:** MONDO:0004770 (pericarditis) — suggested; a specific-form request would need e.g. constrictive pericarditis, tuberculous pericarditis, uremic pericarditis as related/child terms
- **OMIM:** No single-gene OMIM disease entry for idiopathic/common pericarditis; monogenic *periodic-fever* syndromes that present with recurrent pericarditis have their own OMIM numbers (TRAPS: OMIM #142680; FMF: OMIM #249100)
- **ICD-10-CM:** I30 (Acute pericarditis) — I30.0 (Acute nonspecific idiopathic pericarditis), I30.1 (Infective pericarditis), I30.8/I30.9; I31 (Other diseases of pericardium) — I31.0 (Chronic adhesive pericarditis), I31.1 (Chronic constrictive pericarditis), I31.3 (Pericardial effusion, noninflammatory), I31.4 (Cardiac tamponade); I32 (Pericarditis in diseases classified elsewhere, e.g., uremic, TB)
- **ICD-11:** BB21 (Pericarditis), BB21.0 (Acute pericarditis), BB21.1 (Chronic pericarditis), BB23 (Constrictive pericarditis)
- **MeSH:** D010493 (Pericarditis); D010496 (Pericarditis, Constrictive); D010494 (Pericarditis, Tuberculous)
- **Orphanet:** ORPHA:98915 (Recurrent pericarditis) is a listed rare-disease entity for the recurrent/autoinflammatory form

**Synonyms/alternative names:** inflammation of the pericardium; pericardial inflammation; acute idiopathic pericarditis; Dressler syndrome (post-myocardial-infarction pericarditis, a subtype); postpericardiotomy syndrome; post-cardiac injury syndrome (umbrella term for post-MI, post-surgical, and post-traumatic pericarditis); tuberculous pericarditis; uremic/dialysis-associated pericarditis; effusive-constrictive pericarditis; transient constrictive pericarditis.

**Evidence basis:** This entry synthesizes aggregated disease-level clinical, epidemiological, genetic, and mechanistic literature (cohort studies, RCTs, systematic reviews, guideline documents) rather than a single-patient/EHR source.

---

## 2. Etiology

**Disease causal factors** — pericarditis is fundamentally a **stereotypical inflammatory response of the pericardium to injury**, regardless of trigger. Recognized categories:

- **Infectious**
  - *Viral* (most common identifiable cause in high-income settings): enteroviruses (coxsackievirus, echovirus), adenovirus, parvovirus B19, herpesviruses (EBV, CMV, HHV-6), influenza, and SARS-CoV-2 (both from infection and, rarely, post-mRNA-vaccination myopericarditis).
  - *Bacterial*: *Mycobacterium tuberculosis* — the dominant cause of pericarditis and constrictive pericarditis in Africa/Asia, especially with HIV co-infection (JACC Adv 2024; https://www.jacc.org/doi/10.1016/j.jacadv.2024.101427); purulent bacterial pericarditis (*Staphylococcus*, *Streptococcus*, *Pneumococcus*) — rare but high mortality.
  - *Fungal/parasitic*: rare, seen in immunocompromised hosts.
- **Idiopathic** — the largest single category in immunocompetent patients in developed countries (up to 80–90% of ambulatory cases), presumed largely post-viral/autoimmune but without an identified trigger.
- **Autoimmune/systemic inflammatory disease**: systemic lupus erythematosus, rheumatoid arthritis, systemic sclerosis, Sjögren syndrome, sarcoidosis, IBD, vasculitides (e.g., polyarteritis nodosa, eosinophilic granulomatosis with polyangiitis).
- **Autoinflammatory (monogenic)**: TNF receptor-associated periodic syndrome (TRAPS, *TNFRSF1A*), familial Mediterranean fever (FMF, *MEFV*) — see Section 4.
- **Post-cardiac injury syndrome (PCIS)** — umbrella for:
  - *Post-myocardial infarction pericarditis* — early peri-infarction pericarditis (direct extension of necrosis, days) vs. **Dressler syndrome** (delayed, immune-mediated, weeks–months post-MI) (PMC9681686).
  - *Postpericardiotomy syndrome* — after cardiac surgery.
  - *Post-traumatic/post-procedural* — after PCI, pacemaker/device implantation, catheter ablation, thoracic trauma (PMC8887692).
  - Mechanism: anti-actin/anti-myosin autoantibodies following mesothelial/myocardial injury with immune-complex deposition in pericardium/pleura/lung, producing a delayed hypersensitivity-like polyserositis (ScienceDirect 2024, PMID:38559602).
- **Neoplastic**: primary pericardial tumors (rare, e.g., mesothelioma) or, far more commonly, metastatic disease (lung, breast cancer, lymphoma, melanoma) causing malignant pericardial effusion/pericarditis via direct invasion, lymphatic dissemination, or hematogenous spread (5–20% of patients with metastatic cancer have pericardial involvement; tamponade in up to 50% of malignant effusions).
- **Metabolic**: **uremic pericarditis** (pre-dialysis or early-dialysis ESRD, from toxic metabolite accumulation and increased microvascular permeability) and **dialysis-associated pericarditis** (from underdialysis in patients on chronic renal replacement) — occurring in up to 14% (range 2–21%) of ESRD patients (PMID:28873222).
- **Radiation-induced**: mediastinal radiotherapy (e.g., for lymphoma, breast cancer) — acute or delayed (years later) fibrosing pericarditis/constriction with particularly poor pericardiectomy outcomes (PMID:34547827).
- **Drug-induced**: procainamide, hydralazine, isoniazid (lupus-like), anticoagulants (hemopericardium), immune checkpoint inhibitors (irAE pericarditis/myopericarditis).
- **Traumatic**: blunt or penetrating chest trauma.

**Genetic risk factors:**
- *TNFRSF1A* (HGNC:11916) pathogenic/likely-pathogenic and low-penetrance variants — found in ~6% of idiopathic recurrent pericarditis (IRP) cohorts (PMID:23745996); TRAPS patients have pericarditis in ~30% of cases (JACC Case Rep 2024).
- *MEFV* (HGNC:6998) — rare deleterious variants (including the low-penetrance R202Q) enriched in IRP cohorts vs. ancestry-matched controls (~3.9–5%) (PMC11508427; PMID:35658515).
- Family history/familial clustering of recurrent pericarditis can unmask TRAPS (PMID:20497634).
- No common-variant GWAS signal specific to idiopathic pericarditis is well established in the literature to date (a genuine gap — see Section 4).

**Environmental risk factors:** male sex (2-fold higher incidence), age (bimodal — viral/idiopathic peaks in younger adults; malignant/uremic causes skew older), recent viral respiratory/GI illness, cardiac surgery/PCI/device implantation (procedural exposure), thoracic radiotherapy, tuberculosis exposure/endemicity and HIV co-infection (Africa/Asia), chronic kidney disease/dialysis dependence, autoimmune disease diagnosis, malignancy, and (rare) mRNA COVID-19 vaccination (myopericarditis, predominantly young males, self-limited).

**Protective factors:** Colchicine as secondary chemoprophylaxis after a first episode substantially reduces recurrence (see Section 12) — a pharmacologic rather than a constitutional protective factor. No robust genetic protective variant is established. Adequate/intensified dialysis reduces uremic pericarditis risk. Complete TB treatment reduces progression to constriction. No specific dietary/lifestyle protective factor is well characterized in the primary literature.

**Gene–environment interactions:** The clearest example is autoinflammatory-gene-primed inflammasome hyperresponsiveness (TNFRSF1A/MEFV variant carriers) interacting with a nonspecific inflammatory trigger (viral illness, minor injury, cold exposure — classic "stress trigger" reported by TRAPS patients) to precipitate a pericarditis flare, rather than a single environmental agent being sufficient on its own.

---

## 3. Phenotypes

| Phenotype (category) | Description | Onset/frequency | Suggested HP term* |
|---|---|---|---|
| Pericarditic chest pain (symptom) | Sharp, pleuritic, retrosternal/left precordial pain, worse supine and with inspiration, relieved by sitting forward | Present in vast majority of acute episodes (>90%) | HP:0100749 (Chest pain) |
| Pericardial friction rub (clinical sign) | Triphasic (atrial systole, ventricular systole, early diastole), scratchy, left-sternal-border sound; pathognomonic but transient/positional | ~35% at any single exam (intermittent) | consider HP:0031653 (Pericardial friction rub) or free text if unmapped |
| ECG changes (lab/instrument finding) | Diffuse concave ST-elevation + PR-segment depression (stage I), evolving through 4 classic stages; distinguishes from STEMI by lack of reciprocal changes | Frequent early finding | HP:0003115 (Abnormal EKG) as parent; more specific ST-elevation term if available |
| Pericardial effusion (imaging finding) | New or worsening fluid in pericardial space on echo/CT/MRI; ranges from trace to tamponade-causing | Variable, up to ~60% | HP:0001698 (Pericardial effusion) |
| Elevated CRP/inflammatory markers (lab abnormality) | CRP elevation supports diagnosis and guides duration of anti-inflammatory therapy/recurrence risk | Common, near-universal in active inflammation | consider generic elevated CRP term |
| Cardiac tamponade (clinical sign/complication) | Elevated JVP, pulsus paradoxus, hypotension (Beck triad in severe cases); life-threatening | Uncommon in idiopathic/viral (<5%), more frequent in malignant/TB/purulent | HP:0025091 (Pulsus paradoxus); consider cardiac tamponade term |
| Constrictive physiology (late complication) | Elevated/equalized diastolic pressures, ventricular interdependence, Kussmaul sign, pericardial knock, ascites/peripheral edema mimicking right heart failure | Develops in a minority (~1–2% after non-TB pericarditis; up to 17–40% after TB pericarditis) over months–years | consider constrictive pericarditis term |
| Fever, myalgia (systemic/constitutional) | Low-grade fever common, especially viral/idiopathic and autoinflammatory forms | Frequent | HP:0001945 (Fever); HP:0003326 (Myalgia) |
| Dyspnea (symptom) | From effusion, tamponade, or constrictive physiology | Variable, common with significant effusion | HP:0002094 (Dyspnea) |
| Troponin elevation (lab, indicates myopericardial overlap) | Reflects concomitant epicardial myocarditis (myopericarditis); does not by itself worsen prognosis if regional wall motion normal | ~15–30% of acute pericarditis cases | consider elevated troponin term |

*HP term suggestions are drawn from domain knowledge and should be OAK-verified (`runoak -i sqlite:obo:hp info <ID> -O obo`) against canonical labels before KB entry, per this repository's anti-hallucination protocol — several (friction rub, tamponade, constriction) I could not confirm exist as exact HPO leaf terms without direct OAK lookup and are flagged for curator verification rather than asserted.

**Onset:** Acute pericarditis can occur at any age but idiopathic/viral forms peak in young-to-middle-aged adults; malignant and uremic forms skew older; autoinflammatory-gene-associated recurrent pericarditis often begins in childhood/adolescence.

**Severity/progression/course:** Most acute idiopathic/viral pericarditis is self-limited (days to a few weeks) with NSAID/colchicine therapy. ~15–30% of a first episode recur; of those, further relapses are common, and a subset become colchicine-resistant/corticosteroid-dependent, driving IL-1-blockade candidacy. Recurrence overall approaches ~30% after a first episode. Progression to constrictive pericarditis is course-dependent: low risk (<1%) after viral/idiopathic pericarditis, intermediate (2–5%) after autoimmune/neoplastic, and high (20–30%) after bacterial/purulent or tuberculous pericarditis (Imazio et al., summarized in AFP 2024 review).

**Quality-of-life impact:** Recurrent pericarditis is associated with substantial QoL impairment — chronic pain, fatigue, activity limitation, anxiety about recurrence, and school/work absenteeism; IL-1-blockade trials (RHAPSODY, AIRTRIP) used patient-reported QoL instruments as secondary endpoints and demonstrated meaningful improvement with anti-IL-1 therapy (NEJM 2021, PMID:33200890).

---

## 4. Genetic/Molecular Information

Pericarditis is overwhelmingly a **non-Mendelian, acquired inflammatory condition**; monogenic contribution is confined to a minority of recurrent/idiopathic cases explained by autoinflammatory-disease genes.

**Causal/associated genes:**
- ***TNFRSF1A*** (HGNC:11916; OMIM *191190) — encodes TNF receptor superfamily member 1A (p55 TNF receptor). Missense variants (e.g., cysteine-disrupting variants affecting extracellular disulfide bonds, and low-penetrance variants such as R92Q) impair receptor shedding/protein folding, causing TRAPS (OMIM #142680). Found in ~6% of idiopathic recurrent pericarditis cohorts (PMID:23745996); low-penetrance variants specifically implicated in adult-onset recurrent inflammatory attacks including pericarditis.
- ***MEFV*** (HGNC:6998; OMIM *608107) — encodes pyrin. Pathogenic/likely-pathogenic variants cause FMF (OMIM #249100, AR); the low-penetrance **R202Q** variant has been specifically linked to anakinra-dependent recurrent pericarditis (PMC11508427). Rare deleterious MEFV variants enriched (~3.9%) in idiopathic recurrent pericarditis vs. ancestry-matched controls (PMID:35658515).
- Other periodic-fever-syndrome genes (*NLRP3*/CAPS, *MVK*/hyper-IgD syndrome) are plausible but less specifically documented for pericarditis as the dominant phenotype; extrapolate cautiously.

**Pathogenic variant characteristics:**
- *Classification*: predominantly missense (TNFRSF1A cysteine and non-cysteine variants; MEFV exon 10 and low-penetrance variants); ACMG/AMP tiers range from pathogenic (classic TRAPS-causing cysteine variants) to VUS/low-penetrance risk alleles (R92Q in TNFRSF1A, R202Q/E148Q in MEFV) — these lower-penetrance alleles act more as susceptibility/modifier variants than fully deterministic Mendelian causes, consistent with variable expressivity in adult-onset presentations.
- *Population allele frequency*: low-penetrance variants (e.g., MEFV E148Q, R202Q) are relatively common polymorphisms in general population databases (gnomAD) with much lower penetrance than classic exon-10 FMF variants — curators should check gnomAD allele frequency directly per variant.
- *Origin*: germline (autoinflammatory-gene variants); somatic variants are not a recognized mechanism in pericarditis.
- *Functional consequence*: TNFRSF1A variants are broadly considered **dominant-negative/gain-of-function** for inflammatory signaling (impaired receptor shedding → sustained TNF signaling; also intracellular receptor misfolding triggering an unfolded-protein-response-linked pro-inflammatory state) rather than simple loss-of-function. MEFV pathogenic variants cause **gain-of-function** pyrin inflammasome activation.

**Modifier genes:** Not well characterized specifically for pericarditis; in the broader autoinflammatory-disease literature, additional NLRP3-pathway and cytokine-gene variants are proposed modifiers of clinical severity/penetrance, but pericarditis-specific modifier data are sparse — a knowledge gap.

**Epigenetic information:** No disease-specific pericarditis epigenetic dataset was identified in this search; broadly, inflammatory-disease epigenomic resources (ENCODE, Roadmap Epigenomics) have not to our knowledge been applied specifically to pericardial tissue in pericarditis.

**Chromosomal abnormalities:** Not a recognized feature of pericarditis; no aneuploidy/translocation association identified.

**Suggested GO/molecular annotations for curation:** GO:0043123 (positive regulation of canonical NF-kappaB signal transduction) for TNFRSF1A/pyrin-driven signaling; GO:0002218 (activation of innate immune response); NLRP3 inflammasome activation (GO:0043123-adjacent; consider GO term for "NLRP3 inflammasome complex assembly" if present in the ontology) — verify exact GO IDs via OAK before use.

---

## 5. Environmental Information

- **Environmental/toxic factors:** thoracic irradiation (mediastinal RT for lymphoma/breast cancer) is the best-documented environmental trigger outside infection, causing both acute pericarditis and delayed (sometimes decades-later) fibrosing constrictive pericarditis with disproportionately poor surgical outcomes (PMID:34547827). No specific chemical toxin/pollutant is robustly linked in CTD/TOXNET-style evidence at the level of a primary etiologic driver (distinct from generalized cardiovascular risk).
- **Lifestyle factors:** No strong dedicated lifestyle-modification literature (diet, exercise) for primary prevention of idiopathic pericarditis; post-diagnosis, **strenuous physical activity is specifically discouraged during the acute/active phase** until symptom and CRP normalization (guideline-level recommendation, ESC 2025) because of a theoretical/observed association with recurrence and to reduce arrhythmia risk in concurrent myocarditis.
- **Infectious agents:** the best-characterized "environmental" driver class.
  - *Viral*: coxsackievirus B (classic), echovirus, adenovirus, parvovirus B19, EBV, CMV, HHV-6, influenza, SARS-CoV-2.
  - *Bacterial*: *Mycobacterium tuberculosis* (leading global cause of pericarditis/constriction, especially sub-Saharan Africa with HIV co-infection — mortality 8–34%, rising to ~40% in untreated HIV co-infection) (JACC Adv 2024); *Staphylococcus aureus*, *Streptococcus pneumoniae*, and other pyogenic bacteria (purulent pericarditis, high mortality if untreated); *Coxiella burnetii*, *Borrelia burgdorferi* (rare).
  - *Fungal*: *Histoplasma*, *Aspergillus*, *Candida* — rare, immunocompromised hosts.
  - *Parasitic*: *Echinococcus*, *Entamoeba histolytica* — rare, endemic-region case reports.

---

## 6. Mechanism / Pathophysiology

**Causal chain overview (general/idiopathic-viral pericarditis):**
1. **Trigger** (viral infection, cardiac injury, autoimmune activation, uremic toxin accumulation, or malignant infiltration) →
2. **Pericardial mesothelial cell injury/stress** →
3. **Innate immune sensing and NLRP3 inflammasome activation** in pericardial (and epicardial) tissue — central, converging mechanistic node across etiologies (JACC Basic Transl Sci 2020; https://www.jacc.org/doi/10.1016/j.jacbts.2020.11.016) →
4. **IL-1β (and IL-1α) release** → downstream NF-κB-driven cytokine cascade (IL-6, TNF, chemokines) →
5. **Local vascular/mesothelial inflammatory response**: increased microvascular permeability, leukocyte (neutrophil, then lymphocyte/macrophage) infiltration, fibrin deposition on pericardial surfaces →
6. **Clinical phase**: pericardial friction rub (fibrin-roughened surfaces), pericardial effusion (increased permeability + reduced lymphatic clearance), pleuritic chest pain (irritation of pain-sensitive parietal pericardium/pleura), diffuse ST-elevation (subepicardial inflammation) →
7. **Resolution or chronicity**: in most cases inflammation resolves; in a subset, recurrent inflammatory cycling occurs (IL-1-driven, explaining efficacy of IL-1 blockade), or **fibrotic organization and calcification** of the pericardium develop over months–years → **constrictive pericarditis** (loss of pericardial compliance → equalization of diastolic pressures across chambers → ventricular interdependence → right-heart-failure phenotype).

**Etiology-specific mechanistic branches:**
- **Autoimmune/post-cardiac-injury syndrome**: mesothelial/myocardial injury exposes normally sequestered cardiac antigens → anti-actin/anti-myosin (anti-heart) autoantibody formation → immune-complex deposition in pericardium/pleura/lung → delayed (weeks-months) hypersensitivity-type serositis, classically Dressler syndrome post-MI (PMC10978175, PMID:38559602).
- **Autoinflammatory (monogenic)**: TNFRSF1A misfolded-receptor retention/impaired shedding or MEFV pyrin gain-of-function → constitutively primed innate immune cells (monocytes/macrophages) → recurrent, stereotyped IL-1β-driven flares independent of adaptive immunity, explaining corticosteroid- or colchicine-refractory but IL-1-blockade-responsive disease.
- **Tuberculous pericarditis**: classic four-stage pathogenesis (fibrinous exudation → serosanguinous effusion with high lymphocyte/monocyte content → organization with granuloma/caseation → constrictive scarring) driven by delayed-type (Th1) hypersensitivity to mycobacterial antigens, worsened by HIV-associated immune dysregulation; fibrocalcific encasement impedes diastolic filling (Circulation 2005; ScienceDirect immunopathogenesis review).
- **Uremic/dialysis-associated pericarditis**: accumulation of uremic toxins (urea, other nitrogenous solutes) causes direct pericardial inflammation and increased microvascular permeability; underdialysis is the proposed proximate mechanism for the dialysis-associated form; intensified dialysis often resolves it, supporting a toxin-clearance-dependent mechanism (PMID:28873222).
- **Neoplastic**: tumor cells reach the pericardium by direct invasion, lymphatic dissemination, or hematogenous spread; disrupt capillary/venule integrity → exudative or hemorrhagic effusion; separately, neoplastic infiltration causes pericardial scarring/loss of elasticity that can mimic constriction.

**Cell types involved:** pericardial mesothelial cells (primary site of injury/inflammasome activation), monocytes/macrophages, neutrophils (early), T lymphocytes (delayed/autoimmune phase), fibroblasts (fibrotic/constrictive phase), and — in myopericarditis overlap — cardiomyocytes.

**Suggested ontology terms for curation** (verify via OAK before use):
- GO biological processes: "NLRP3 inflammasome complex assembly," "positive regulation of interleukin-1 beta production," "positive regulation of canonical NF-kappaB signal transduction," "fibrosis"/extracellular matrix remodeling terms for the constrictive-progression node.
- CL cell types: mesothelial cell (relevant pericardial mesothelium term), macrophage, neutrophil, fibroblast, CD4-positive T cell.
- UBERON: pericardium, pericardial cavity/space, epicardium, parietal pericardium, visceral pericardium.

**Molecular/omics profiling:** Dedicated transcriptomic/proteomic/single-cell atlases of human pericarditis tissue are sparse in the literature relative to myocarditis; most mechanistic insight instead derives from (a) pericardial/pleural fluid cytokine profiling (elevated IL-1β, IL-6, TNF in inflammatory effusions) and (b) the interferon-γ-knockout mouse model (Section 15) demonstrating that loss of IFN-γ regulation shifts an autoimmune cardiac response toward a constrictive-pericarditis phenotype (PMID:15505106) — a genuine translational/human-model-fidelity gap worth flagging for a dismech `HUMAN_MODEL_MISMATCH` discussion if curated.

---

## 7. Anatomical Structures Affected

**Organ level:**
- Primary: pericardium (parietal and visceral layers), pericardial space/cavity.
- Secondary/complication-driven: myocardium (myopericarditis/perimyocarditis overlap), right and left ventricles (diastolic filling impairment in constriction/tamponade), lungs and pleura (co-occurring pleuritis/pleural effusion, especially PCIS), liver (passive congestion, "cardiac cirrhosis" in chronic constriction), and systemic venous system (elevated JVP, peripheral edema, ascites in constrictive physiology).
- Body systems: cardiovascular system primarily; secondary respiratory (pleuritic pain, pleural effusion) and, in autoimmune/uremic forms, renal and immune systems as upstream drivers rather than affected targets.

**Tissue/cell level:** mesothelial lining of the pericardium (site of primary injury and inflammasome activation); subserosal connective tissue (site of fibrosis/calcification in constrictive disease); in the myopericardial-overlap subset, subepicardial myocardium.

**Subcellular level:** NLRP3 inflammasome assembly at the level of the cytosol/mitochondria-associated membranes in mesothelial and macrophage populations (GO Cellular Component: inflammasome complex); disrupted TNFRSF1A intracellular trafficking/ER retention in TRAPS-associated cases.

**Localization/laterality:** Diffuse, non-lateralized process (unlike myocardial infarction) — a key clinical distinguishing feature (diffuse concave ST elevation vs. territorial STEMI changes). No meaningful unilateral/bilateral distinction applies to the pericardium itself, though co-occurring pleural effusions in PCIS can be unilateral or bilateral.

**Suggested UBERON terms:** pericardium, pericardial cavity, parietal pericardium, visceral pericardium (epicardium), fibrous pericardium, myocardium (for overlap phenotype), pleura (for PCIS co-involvement). Verify exact UBERON IDs via OAK before curation.

---

## 8. Temporal Development

**Onset:** Acute pericarditis can present at any age; peak incidence in young-to-middle-aged adults for idiopathic/viral forms; malignant, uremic, and radiation-associated forms occur predominantly in older or comorbid populations. Onset pattern is typically **acute** (days), though **incessant** (continuous >4–6 weeks but <3 months) and **chronic** (>3 months) courses occur, and tuberculous/uremic forms may present more insidiously.

**Disease stages / progression:**
- *Acute*: days to a few weeks, self-limited in the majority with NSAID/colchicine therapy.
- *Incessant*: continuous symptoms beyond the expected acute window without a symptom-free interval.
- *Recurrent*: relapse after a documented symptom-free interval of ≥4–6 weeks; occurs in ~15–30% after a first episode, and in a subgroup evolves into multiple relapses requiring escalation to corticosteroids and ultimately IL-1 blockade.
- *Chronic*: persistent (>3 months) low-grade inflammation.
- *Constrictive* (late structural sequela): can develop as **transient constrictive pericarditis** (reversible with anti-inflammatory therapy, associated with CMR pericardial late gadolinium enhancement and elevated inflammatory markers predicting reversibility — Circulation, PMID underlying PMC3860810) or as fixed, fibrocalcific constriction requiring pericardiectomy.

**Progression rate/course pattern:** Highly etiology-dependent — viral/idiopathic pericarditis is typically monophasic-to-relapsing but rarely progresses to constriction; tuberculous and purulent bacterial pericarditis progress to constriction in a substantial minority (17–40% for TB) over months if inadequately treated; radiation-associated constriction can manifest years to decades after exposure.

**Remission patterns:** Spontaneous remission is common in viral/idiopathic acute pericarditis; treatment-induced remission is the norm with NSAID + colchicine; IL-1 blockade (rilonacept, anakinra) induces treatment-dependent remission in colchicine-resistant/steroid-dependent recurrent disease, with recurrence typically resuming on drug withdrawal in trial data (RHAPSODY).

**Critical periods:** Early initiation of colchicine (from the first episode) is the key intervention window for reducing recurrence risk; in tuberculous pericarditis, early diagnosis and antitubercular therapy (± adjunctive corticosteroids) is the critical window for preventing progression to constriction; in transient constrictive pericarditis, early aggressive anti-inflammatory therapy (guided by CMR LGE/CRP) can prevent the need for pericardiectomy.

---

## 9. Inheritance and Population

**Epidemiology:**
- Incidence of acute pericarditis: ~27.7 per 100,000 person-years overall (commonly cited estimate); a Finnish population study reported 4.52/100,000 person-years in men vs. 2.11/100,000 in women. Acute pericarditis accounts for ~4.4% of ED presentations for non-ischemic chest pain, with an estimated 0.1% of all-cause and ~5% of chest-pain-related hospital admissions.
- Recurrence after a first episode: ~15–30%.
- Constrictive pericarditis incidence after non-TB pericarditis: <1–2%; after tuberculous pericarditis: 17–40%.

**Inheritance pattern (for the genetic/autoinflammatory subset only — the great majority of pericarditis is acquired/non-Mendelian):**
- TRAPS (*TNFRSF1A*-associated): autosomal dominant, OMIM #142680.
- FMF (*MEFV*-associated): classically autosomal recessive, OMIM #249100, though low-penetrance heterozygous variants (e.g., R202Q, E148Q) have been reported with apparent semi-dominant/reduced-penetrance patterns in recurrent-pericarditis cohorts.
- **Penetrance**: incomplete and variable — particularly pronounced for the "low-penetrance" TNFRSF1A (R92Q) and MEFV (E148Q, R202Q) variants, which are relatively frequent in the general population but confer disease only in a minority of carriers, consistent with a susceptibility-allele rather than fully penetrant Mendelian model.
- **Expressivity**: variable — even within TRAPS/FMF families, phenotype ranges from isolated recurrent pericarditis to full periodic-fever syndrome with polyserositis/rash/myalgia.
- **Genetic anticipation, germline mosaicism, founder effects**: not specifically documented for pericarditis; FMF overall shows well-known founder-mutation enrichment in Mediterranean/Middle Eastern populations (Sephardic Jewish, Armenian, Turkish, Arab ancestries) — relevant background for MEFV-positive idiopathic recurrent pericarditis case ascertainment, though this is population structure of FMF broadly rather than pericarditis-specific.
- **Consanguinity**: relevant to recessive FMF ascertainment generally, not documented as pericarditis-specific.
- **Carrier frequency**: MEFV pathogenic-variant carrier frequency is notably elevated (~1 in 5–7) in some Mediterranean populations reflecting FMF founder effects — again, general-FMF-population data rather than pericarditis-cohort-specific.

**Population demographics:**
- **Sex ratio**: male predominance overall, incidence ratio ~1.7–2.0:1 (men:women), with the largest sex gap in young adults; constrictive pericarditis specifically shows ~3:1 male:female predominance.
- **Geographic distribution**: idiopathic/viral pericarditis predominates in high-income settings with low TB burden; tuberculous pericarditis dominates in sub-Saharan Africa and parts of Asia, where it is the leading cause of pericardial constriction, strongly modulated by HIV co-prevalence.
- **Age distribution**: bimodal-ish — younger adults for idiopathic/viral/post-vaccination myopericarditis; older, comorbid populations for malignant, uremic, radiation-associated, and post-cardiac-surgery pericarditis.

---

## 10. Diagnostics

**Clinical diagnostic criteria (ESC, reaffirmed 2025):** ≥2 of 4 —
1. Typical pericarditic chest pain (pleuritic, positional)
2. Pericardial friction rub
3. New widespread ST-elevation or PR-depression on ECG
4. New or worsening pericardial effusion

Supportive findings: elevated CRP/inflammatory markers, evidence of pericardial inflammation on imaging.

**Laboratory tests:**
- CRP/ESR — supports diagnosis, tracks disease activity, guides duration of anti-inflammatory therapy and tapering; LOINC-codable inflammatory markers.
- Troponin — elevated in myopericarditis overlap (~15–30%); does not independently worsen prognosis absent regional wall-motion abnormality.
- Complete blood count, renal function (to identify uremic etiology), autoimmune serologies (ANA, RF, ANCA) when systemic disease suspected.
- Pericardial fluid analysis when pericardiocentesis performed: cell count/differential, protein, LDH (Light's-criteria-type exudate/transudate distinction), cytology (malignancy), ADA and mycobacterial culture/PCR (TB), Gram stain/culture (purulent).

**Imaging:**
- **Echocardiography**: first-line, detects effusion, tamponade physiology, and (with Doppler) constrictive hemodynamics (respirophasic septal shift, hepatic vein flow reversal).
- **Cardiac CT**: pericardial thickening/calcification, especially useful pre-pericardiectomy.
- **Cardiac MRI (CMR)**: pericardial **late gadolinium enhancement (LGE)** is a sensitive marker of active pericardial inflammation; elevated inflammatory markers plus pericardial LGE predict *reversibility* of constrictive physiology with anti-inflammatory therapy, distinguishing "transient constrictive pericarditis" from fixed fibrocalcific constriction requiring surgery (Circulation, PMID underlying PMC3860810/PMID:22262690-type series).
- Chest X-ray: may show cardiomegaly ("water-bottle" silhouette) with large effusion; limited standalone diagnostic value.

**Functional/electrophysiologic tests:** ECG (4-stage evolution: diffuse ST-elevation + PR-depression → normalization → T-wave inversion → normalization); cardiac catheterization with simultaneous right/left heart pressure tracings for hemodynamic confirmation of constriction (equalized diastolic pressures, discordant respiratory variation in LV/RV systolic pressure — distinguishing constriction from restrictive cardiomyopathy).

**Biopsy/pathology:** Pericardial biopsy reserved for diagnostic uncertainty (suspected TB, malignancy, or purulent pericarditis) or at the time of pericardiectomy — histopathology shows fibrinous exudate (acute), granulomatous inflammation with caseation (TB), or dense fibrosis/calcification (chronic constrictive).

**Genetic testing:** Targeted *TNFRSF1A* and *MEFV* sequencing (single-gene or as part of a periodic-fever/autoinflammatory-disease gene panel) is reasonable in recurrent, colchicine-resistant/corticosteroid-dependent pericarditis, especially with a suggestive personal/family history of periodic fevers, serositis, rash, or relevant ancestry (Mediterranean for MEFV). Whole-exome/genome sequencing is not first-line but may be used in atypical multisystem presentations. No CMA, karyotype, FISH, mitochondrial, or repeat-expansion testing role is established for pericarditis.

**Differential diagnosis:** acute coronary syndrome/STEMI (most critical to exclude), aortic dissection, pulmonary embolism, pleuritis/pneumonia, costochondritis, esophageal disease (GERD, spasm), myocarditis (may coexist), restrictive cardiomyopathy (vs. constrictive pericarditis — key differential requiring invasive hemodynamics/CMR/CT tissue characterization).

**Screening:** No population-level screening program exists (acquired, largely sporadic disease); "screening" in practice is case-finding for underlying secondary causes (autoimmune serologies, TB testing, malignancy workup, renal function) once pericarditis is diagnosed, and cascade genetic counseling/testing of relatives when a monogenic autoinflammatory cause is confirmed.

---

## 11. Outcome/Prognosis

**Survival/mortality:** Idiopathic/viral acute pericarditis carries an excellent prognosis with mortality close to that of the general population. Prognosis is markedly etiology-dependent — purulent bacterial pericarditis and tuberculous pericarditis carry substantially higher mortality (TB pericarditis: >1 in 4 patients die within 6 months of diagnosis; mortality rises to ~40% with untreated HIV co-infection). Malignant pericardial effusion/tamponade is associated with poor prognosis reflecting the underlying cancer stage rather than the pericardial process per se.

**Recurrence and chronicity:** ~15–30% recurrence after a first episode; of recurrent cases, a meaningful subset become colchicine-resistant and corticosteroid-dependent, prompting escalation to IL-1 blockade.

**Constrictive pericarditis outcomes (post-pericardiectomy):**
- Contemporary in-hospital/30-day mortality: ~2–8% (improved from historical rates of ~11–13.5%); actuarial survival ~91%, 85%, and 81% at 1, 5, and 10 years respectively.
- Functional improvement (≥1 NYHA class) in ~80% of surviving patients.
- Etiology strongly predicts surgical outcome: idiopathic and post-surgical constriction have the best outcomes; **radiation-associated** and **neoplastic** constriction have the worst long-term survival; need for reoperation and low cardiac output are additional adverse prognostic factors.

**Morbidity/QoL:** Recurrent pericarditis imposes significant chronic-pain and QoL burden (addressed above, Section 3); constrictive pericarditis produces a right-heart-failure-like disability burden (edema, ascites, exercise intolerance, hepatic congestion) until surgically corrected.

**Prognostic factors/biomarkers:** Persistently elevated CRP and pericardial LGE on CMR predict ongoing/recurrent inflammatory activity and identify the "transient" (reversible) constrictive phenotype amenable to medical therapy rather than surgery. High-risk features for a complicated first episode (per ESC criteria) include fever >38°C, subacute onset, large effusion/tamponade, failure to respond to NSAIDs within a week, myopericarditis, immunosuppression, trauma, and oral anticoagulant therapy.

---

## 12. Treatment

**First-line pharmacotherapy (acute and first-recurrence pericarditis):**
- **NSAIDs** (ibuprofen, aspirin — aspirin preferred post-MI to avoid impairing infarct healing) — mainstay for pain/inflammation control. *(NCIT:C15986 Pharmacotherapy; specific agent — CHEBI id per drug)*
- **Colchicine** — added to NSAID therapy from the *first episode* to reduce recurrence risk; foundational trial evidence:
  - **COPE** (2005) — colchicine + conventional therapy reduced recurrence in first-episode acute pericarditis (PMID:16186437).
  - **ICAP** (NEJM 2013, PMID:23992557) — colchicine added to standard anti-inflammatory therapy significantly reduced incessant/recurrent pericarditis in first-episode disease.
  - **CORP** (Ann Intern Med 2011) and **CORP-2** (Lancet 2014) — colchicine reduced recurrence by >30% in patients with a first recurrence and in multiple-recurrence pericarditis, respectively.
  - Colchicine is now guideline-recommended as **standard-of-care adjunct** at every stage from first episode onward. *(therapeutic_agent: CHEBI colchicine ID; treatment_term: NCIT:C15986 Pharmacotherapy)*
- **Corticosteroids** — reserved as second-line (NSAID/colchicine-refractory, contraindication to NSAIDs, or autoimmune-disease-associated pericarditis) because of an association with higher recurrence risk when used as first-line therapy; low-to-moderate dose with slow taper is preferred over high-dose pulses.

**IL-1 pathway blockade (colchicine-resistant/corticosteroid-dependent recurrent pericarditis):**
- **Rilonacept** (ARCALYST) — soluble IL-1 receptor chimeric fusion protein neutralizing both IL-1α and IL-1β. Phase II (2020, PMC7925818) and pivotal Phase 3 **RHAPSODY** trial (NEJM 2021, PMID:33200890) demonstrated rapid resolution of pericarditis pain/inflammation and marked reduction in recurrence during randomized withdrawal. **FDA-approved March 2021** — the first and only FDA-approved therapy specifically for recurrent pericarditis, for adults and children ≥12 years (weekly subcutaneous injection). *(therapeutic_modality: MONOCLONAL_ANTIBODY-adjacent fusion protein — classify per dismech convention, likely OTHER/biologic; treatment_term: NCIT:C15986; therapeutic_agent: search NCIT/CHEBI for rilonacept)*
- **Anakinra** — recombinant IL-1 receptor antagonist; the **AIRTRIP** RCT demonstrated efficacy in colchicine-resistant, corticosteroid-dependent recurrent pericarditis. A systematic review/meta-analysis (PMC9730293) and review (PMC9152656) confirm efficacy of both anakinra and rilonacept, with anti-IL-1 therapy improving both QoL and clinical recurrence outcomes.
- Mechanistic rationale directly ties to Section 6: NLRP3-inflammasome/IL-1β is the convergent pathway across etiologies, making IL-1 blockade a targeted (not merely empiric) therapy — an excellent candidate for a dismech `target_mechanisms` drug-mechanism edge onto an "NLRP3 Inflammasome Activation"/"IL-1β Release" pathophysiology node.

**Etiology-directed therapy:**
- Tuberculous pericarditis: standard 4-drug antitubercular regimen ± adjunctive corticosteroids (evidence mixed/context-dependent, especially by HIV status); colchicine adjunct studied but not clearly beneficial in TB pericarditis specifically (PMC5412665).
- Uremic/dialysis-associated pericarditis: intensified/optimized dialysis is first-line; NSAIDs/colchicine adjunctive; pericardiocentesis for tamponade.
- Purulent bacterial pericarditis: targeted IV antibiotics + pericardial drainage (often surgical, given loculation risk).
- Malignant pericardial effusion: pericardiocentesis ± pericardial window/sclerotherapy, and treatment of the underlying malignancy (chemotherapy/targeted therapy per tumor type).
- Autoinflammatory-gene-positive recurrent pericarditis: IL-1 blockade is particularly rational and effective (anakinra specifically shown effective in MEFV R202Q-positive cases, PMC11508427).

**Surgical/interventional:**
- **Pericardiocentesis** — for tamponade or large symptomatic/diagnostic effusion. *(NCIT surgical/procedural term — verify)*
- **Pericardial window** — for recurrent/malignant effusions.
- **Pericardiectomy** — definitive therapy for fixed constrictive pericarditis; outcomes summarized in Section 11 (best for idiopathic/post-surgical etiology, worst for radiation/neoplastic).

**Supportive care:** activity restriction until symptom/CRP resolution; analgesia; management of tamponade as an emergency.

**Experimental/emerging:**
- Additional IL-1-pathway and broader anti-inflammatory agents continue to be studied for recurrent pericarditis (search ClinicalTrials.gov for current NCT-registered trials, e.g., colchicine-formulation and other anti-inflammatory candidates such as the CardiolRx/MAvERIC-Pilot program referenced in trial registries).
- Ongoing refinement of CMR-LGE-guided therapy duration/tapering strategies.

**Treatment algorithm (guideline-level, ESC 2025):** NSAID + colchicine from first episode → corticosteroids only if NSAID-refractory/contraindicated → IL-1 blockade (rilonacept or anakinra) for colchicine-resistant, corticosteroid-dependent recurrent disease → surgical pericardiectomy reserved for fixed constrictive physiology unresponsive to anti-inflammatory therapy (with CMR/CRP used to first distinguish reversible "transient constriction" from fixed disease).

---

## 13. Prevention

**Primary prevention:** No population-level primary-prevention program exists for idiopathic/viral pericarditis (sporadic, largely unpredictable trigger). Etiology-specific primary prevention is more concrete:
- TB pericarditis: TB control programs, HIV testing/ART access, and (where relevant) latent-TB treatment in high-risk populations.
- Uremic pericarditis: adequate/timely dialysis initiation and dose optimization.
- Post-cardiac-injury syndrome: no established primary prophylaxis, though perioperative colchicine has been studied to reduce postpericardiotomy syndrome incidence after cardiac surgery in some trial literature (not exhaustively reviewed here — worth a dedicated search if curating this specific claim).
- Radiation-associated pericarditis: radiotherapy planning to minimize cardiac/pericardial dose (modern conformal/IMRT techniques).

**Secondary prevention (recurrence prevention — the best-evidenced prevention domain in this disease):**
- **Colchicine started at first-episode diagnosis** is the single best-evidenced secondary-prevention intervention (COPE, ICAP, CORP, CORP-2 — Section 12), reducing recurrence by roughly one-third to one-half across trials.
- **IL-1 blockade** (rilonacept, anakinra) functions as tertiary/secondary prevention specifically in the colchicine-resistant subgroup, with RHAPSODY demonstrating markedly reduced time-to-recurrence during drug-withdrawal periods.
- Avoidance of high-dose corticosteroid monotherapy as first-line, since it is itself associated with *higher* recurrence risk relative to colchicine-based regimens.

**Screening/early detection:** CRP-guided activity restriction and treatment-duration decisions function as a form of tertiary prevention (of both symptomatic relapse and progression to constriction). Early CMR characterization of "transient" vs. fixed constrictive physiology allows early aggressive medical therapy to prevent the need for pericardiectomy.

**Genetic counseling:** For confirmed *TNFRSF1A*/*MEFV*-associated recurrent pericarditis, standard autoinflammatory-disease genetic counseling applies — informing relatives of inheritance pattern (AD for TRAPS, AR/reduced-penetrance for MEFV), variable penetrance/expressivity, and the availability of targeted IL-1-blockade therapy for confirmed carriers with recurrent symptoms.

**Public health:** TB control and HIV treatment access are the dominant public-health lever globally, given tuberculous pericarditis's outsized contribution to pericarditis morbidity/mortality and constriction burden in endemic, high-HIV-prevalence regions.

---

## 14. Other Species / Natural Disease

Naturally occurring pericarditis is recognized in veterinary medicine, most notably:
- **Traumatic reticulopericarditis ("hardware disease") in cattle** — a well-known naturally occurring bovine pericarditis caused by ingested metallic foreign bodies migrating from the reticulum through the diaphragm into the pericardial sac, producing purulent/fibrinous pericarditis and, if chronic, constrictive physiology — a genuine natural-disease veterinary analog (relevant OMIA/veterinary literature, not deeply searched here but well established in veterinary cardiology).
- **Idiopathic pericardial effusion in dogs** (and pericardial mesothelioma-associated effusion, notably in Golden Retrievers) is a recognized clinical entity in small-animal cardiology, though its mechanistic overlap with human idiopathic pericarditis is not well characterized at the molecular level in the literature surveyed here.
- No specific NCBI Taxon-indexed comparative-genomics ortholog analysis for pericarditis susceptibility genes (*TNFRSF1A*, *MEFV*) across species was identified in this search; both genes are broadly conserved across mammals given their fundamental roles in TNF signaling and inflammasome biology, but disease-specific cross-species susceptibility data are not established in the pericarditis literature specifically.
- No zoonotic transmission concern applies to pericarditis itself (it is a tissue-response phenotype, not a transmissible entity), though the causal pathogens in infectious pericarditis (e.g., some *Coxiella burnetii* cases) do have zoonotic origins.

---

## 15. Model Organisms

Compared with myocarditis, dedicated pericarditis-specific animal models are relatively sparse in the literature; most mechanistic animal data derive from cardiac-injury or autoimmune-myocarditis models with secondary pericardial involvement:

- **Interferon-γ-knockout (IFN-γ KO) mouse model of cardiac-myosin-induced experimental autoimmune myocarditis** — the most directly relevant genetic model identified: cardiac myosin immunization in IFN-γ-KO mice produces a **novel model of constrictive pericarditis** with grossly detectable pericarditis, decreased cardiac output, increased chamber stiffness, preserved ejection fraction, and impaired diastolic filling — recapitulating the human constrictive-physiology phenotype (Circulation 2004, PMID:15505106). This demonstrates that loss of IFN-γ-mediated immune regulation shifts an autoimmune cardiac inflammatory response toward pericardial constriction rather than isolated myocarditis, a mechanistically informative but human-fidelity-uncertain finding (candidate for a `HUMAN_MODEL_MISMATCH` framing if curated, since knockout of a single regulatory cytokine in mice is a strong artificial perturbation not established as directly translatable to sporadic human constrictive pericarditis).
- **Experimental autoimmune myocarditis (EAM)** — induced by subcutaneous immunization with cardiac myosin/α-myosin heavy chain peptide in complete Freund's adjuvant, strain-dependent susceptibility (A/J, BALB/c) — the parent model from which the IFN-γ-KO pericarditis-specific variant was derived; primarily a myocarditis model with pericardial involvement as a secondary/associated finding rather than the primary phenotype.
- **Coxsackievirus B3 (CVB3)-induced murine myocarditis** — models the viral-infection → myocarditis → chronic fibrosis/pericarditis → dilated cardiomyopathy sequence relevant to the viral-etiology branch of human pericarditis, though again pericarditis is a secondary/associated feature of a primarily myocardial model.
- **Model limitations:** no widely used model isolates pericardial-mesothelial NLRP3-inflammasome activation as the primary, independent phenotype (i.e., a "pure" pericarditis model without concomitant myocarditis); this is a genuine translational gap, and current mechanistic inference about NLRP3/IL-1β centrality in human pericarditis rests more on (a) clinical biomarker/effusion cytokine data and (b) the strong clinical-trial efficacy signal of IL-1 blockade (RHAPSODY, AIRTRIP) than on a dedicated animal model recapitulating idiopathic recurrent pericarditis end-to-end.
- **Applications:** existing models are primarily used to study autoimmune mechanisms of cardiac inflammation broadly and the transition from inflammation to fibrosis/constriction, rather than to test pericarditis-specific therapeutics — IL-1-blockade drug development for pericarditis instead proceeded largely from mechanistic/biomarker rationale directly into human trials.

---

## Summary of Suggested Ontology Terms for Curation (require OAK verification before entry)

| Domain | Suggested term(s) |
|---|---|
| MONDO | MONDO:0004770 (pericarditis) — and disambiguate constrictive/tuberculous/uremic subtype terms if present |
| HGNC | TNFRSF1A (HGNC:11916), MEFV (HGNC:6998) |
| GO (biological process) | NLRP3 inflammasome activation/assembly; positive regulation of IL-1β production; positive regulation of canonical NF-κB signal transduction |
| CL | mesothelial cell, macrophage, neutrophil, fibroblast, CD4+ T cell |
| UBERON | pericardium, pericardial cavity, parietal/visceral pericardium, myocardium, pleura |
| HP | chest pain, fever, dyspnea, pulsus paradoxus, pericardial effusion (and verify exact leaf terms for friction rub, tamponade, constrictive pericarditis) |
| CHEBI | colchicine, ibuprofen, aspirin |
| NCIT | C15986 (Pharmacotherapy) as the generic treatment_term for NSAID/colchicine/steroid/biologic pharmacotherapy; verify specific NCIT codes for rilonacept/anakinra as therapeutic_agent |

---

## Key Citations (PMID-anchored where available)

1. Colchicine for acute pericarditis (COPE trial) — PMID:16186437
2. Colchicine for recurrent pericarditis (CORP trial) — Ann Intern Med 2011
3. Colchicine for acute pericarditis (ICAP trial) — PMID:23992557
4. Rilonacept Phase 3 (RHAPSODY) — PMID:33200890
5. Interleukin-1 antagonists for recurrent pericarditis (review) — PMC9152656
6. Rilonacept and anakinra meta-analysis — PMC9730293
7. TNFRSF1A mutation spectrum in idiopathic recurrent acute pericarditis — PMID:23745996
8. Recurrent pericarditis: autoimmune or autoinflammatory? — PMID:22884556
9. Pericarditis and autoinflammation — monogenic autoinflammatory disease screening — PMID:35658515
10. Anakinra-dependent recurrent pericarditis and MEFV R202Q — PMC11508427
11. Familial clustering of recurrent pericarditis unmasking TRAPS — PMID:20497634
12. NLRP3 inflammasome role in pericarditis (mechanistic review) — https://www.jacc.org/doi/10.1016/j.jacbts.2020.11.016
13. Post-cardiac injury syndrome: evidence-based approach — PMID:38559602
14. Dressler syndrome: not just a relic of the past — PMC9681686
15. Cardiovascular involvement in TB patients treated in Southern Africa — JACC Adv 2024
16. Uremic pericarditis, pericardial effusion, and constriction in ESRD — PMID:28873222
17. CMR pericardial LGE predicts reversibility of constrictive pericarditis — Circulation (PMC3860810)
18. Long-term outcomes of pericardiectomy for constrictive pericarditis — PMC4662820
19. FDA approval of rilonacept for recurrent pericarditis (2021) — Kiniksa/FDA press release
20. Novel model of constrictive pericarditis in IFN-γ-knockout mice — PMID:15505106
21. 2025 ESC Guidelines for the management of myocarditis and pericarditis — Eur Heart J 2025 (https://academic.oup.com/eurheartj/article/46/40/3952/8234483)

**Note on evidence gaps:** Several sections (epigenetics, single-cell/spatial transcriptomics of human pericardial tissue, modifier genes beyond TNFRSF1A/MEFV, pericarditis-specific animal models isolating pericardial inflammation from myocarditis, and comparative/veterinary molecular data) have thin or absent dedicated literature and are flagged rather than fabricated — consistent with this KB's evidence-discipline requirement to omit or flag unsupported claims rather than invent citations.