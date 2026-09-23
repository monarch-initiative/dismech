---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-19T04:18:57.392435'
end_time: '2026-09-19T04:24:43.461336'
duration_seconds: 346.07
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Local Anesthetic Systemic Toxicity
  mondo_id: MONDO:0100335
  category: Environmental
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
  web_search_requests: 14
  num_turns: 18
  total_cost_usd: 1.3881792000000002
  session_id: dc83c613-1fba-53b8-9741-f63fb2448a6e
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 35
reference_validation:
  total_references: 25
  verified: 25
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 25
  on_topic: 18
  validator_version: 0.2.1
term_validation:
  total_terms: 33
  verified: 33
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Local Anesthetic Systemic Toxicity
- **MONDO ID:** MONDO:0100335 (if available)
- **Category:** Environmental

## Research Objectives

Please provide a comprehensive research report on **Local Anesthetic Systemic Toxicity** covering all of the
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

**Present this section as an ordered causal chain first, then the detail below.**
Open with a numbered sequence of mechanistic steps running from the initiating
lesion (mutation, exposure, infection) to the clinical manifestation, one step per
line, each naming what it causes next. State the causal verb explicitly ("leads
to", "results in") and say where a step is inferred rather than demonstrated.
Where the mechanism branches, show the branch. The categories below are a
checklist of what to cover within those steps, not the organizing structure —
a step may draw on several of them, and a category may contribute to several
steps.

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

# Local Anesthetic Systemic Toxicity (LAST): Comprehensive Research Report

## Note on ontology term suggestions
Per standard curation practice, every ontology identifier (HP, GO, CL, UBERON, CHEBI, NCIT, MONDO) suggested below is a **lead only** and has not been verified against a live ontology lookup (e.g., OAK/OLS) in this session. Anyone using these terms to populate a structured knowledge base entry should independently confirm the CURIE and canonical label before binding it — do not treat any ID below as verified.

---

## 1. Disease Information

**Overview.** Local anesthetic systemic toxicity (LAST) is a potentially life-threatening, iatrogenic/procedural drug-toxicity syndrome that occurs when the circulating unbound (free) plasma concentration of a local anesthetic (LA) — most often an amide agent such as bupivacaine, ropivacaine, or lidocaine — rises high enough to impair central nervous system (CNS) and cardiovascular function. It is a complication of regional anesthesia (peripheral nerve blocks, neuraxial/epidural blocks, paravertebral blocks), local infiltration, tumescent anesthesia, topical/mucosal application, and intravenous lidocaine infusion, rather than a disease with an independent genetic etiology in the classic Mendelian sense — dismech's "Environmental" category designation reflects that the primary driver is drug exposure/dose, modulated by patient physiology and (in rare cases) genetic susceptibility ([StatPearls NBK499964](https://www.ncbi.nlm.nih.gov/books/NBK499964/); [PMID:35777259](https://pubmed.ncbi.nlm.nih.gov/35777259/)).

**Key identifiers:**
- **MONDO:** MONDO:0100335 (as supplied; not independently re-verified here — confirm before use)
- **ICD-10-CM:** T41.3X1A (Poisoning by local anesthetics, accidental/unintentional, initial encounter); T41.3X5A (Adverse effect of local anesthetics, initial encounter) ([icd10data.com](https://www.icd10data.com/ICD10CM/Codes/S00-T88/T36-T50/T41-/T41.3X1A))
- **MeSH:** Consider "Anesthetics, Local/adverse effects" (D000777) or a poisoning/toxicity qualifier; there is no single dedicated MeSH descriptor for "LAST" as a named syndrome.
- **OMIM/Orphanet:** No dedicated OMIM or Orphanet entry was found for LAST as a discrete disease; it is catalogued in clinical toxicology and anesthesiology references (StatPearls, UpToDate, NYSORA) rather than as a rare/genetic disease registry entry.

**Synonyms/alternative names:** Local anesthetic toxicity; systemic local anesthetic toxicity; LA-induced cardiotoxicity/neurotoxicity; bupivacaine cardiotoxicity (agent-specific); "cardiac arrest following regional anesthesia."

**Data derivation:** Most epidemiological knowledge comes from **aggregated, disease/event-level resources** rather than individual EHR-linked cohorts: national/international case registries and pharmacovigilance databases (e.g., the FDA Adverse Event Reporting System, FAERS), multicenter simulation collaboratives, systematic reviews of published case reports, and a small number of retrospective EHR cohort studies using federated networks such as TriNetX (e.g., the 2024 pregnancy cohort study) ([PMID:39398741](https://pubmed.ncbi.nlm.nih.gov/39398741/); BJA 2025 editorial, Schwenk/Sneyd/Wu).

---

## 2. Etiology

**Disease causal factors.** LAST is fundamentally a **pharmacologic/toxicologic** disorder: excessive systemic (blood/plasma) exposure to a local anesthetic molecule, arising from (a) **inadvertent intravascular injection** during a nerve block or epidural, (b) **rapid systemic absorption** from a highly vascular injection site (e.g., intercostal or paracervical blocks), (c) **cumulative overdose** exceeding weight-based maximum recommended doses, especially with repeated dosing or continuous infusions, or (d) **impaired clearance/altered protein binding** that raises the free (unbound, pharmacologically active) fraction of drug for a given total dose ([StatPearls NBK499964](https://www.ncbi.nlm.nih.gov/books/NBK499964/); NYSORA LAST topic page).

**Genetic risk factors:**
- **Inherited fatty-acid β-oxidation defects**, especially **carnitine palmitoyltransferase II (CPT II) deficiency** and other carnitine-cycle disorders. Because bupivacaine impairs the mitochondrial carnitine-acylcarnitine translocase and fatty-acid-supported oxidative phosphorylation, patients whose myocardium already relies precariously on fatty-acid oxidation are more susceptible to LA-induced cardiotoxicity at sub-toxic doses. CPT II deficiency is autosomal recessive; case literature reports that "carnitine deficiency reportedly produces ventricular arrhythmia and hypotension induced by subtoxic doses of bupivacaine," implicating this pathway directly ([PMID: review — Anesthetic management of patients with carnitine deficiency, PMC9282055](https://pmc.ncbi.nlm.nih.gov/articles/PMC9282055/)).
- **Cardiac sodium-channelopathy variants (SCN5A).** Pathogenic *SCN5A* variants (the gene encoding cardiac Nav1.5, the principal off-target cardiac channel for LAs), including those underlying **Brugada syndrome** and other conduction-system disease, have been associated in case reports with exaggerated cardiotoxic responses to LA exposure — e.g., a loss-of-function *SCN5A* variant associated with lidocaine-induced ventricular fibrillation after a therapeutic antiarrhythmic dose in a myocardial-infarction patient ([PMID:24445991](https://pubmed.ncbi.nlm.nih.gov/24445991/)), and case reports of epidural/neuraxial LA use in parturients with known *SCN5A* mutations requiring modified management (van der Knijff-van Dortmont et al., *Case Reports in Anesthesiology* 2016).
- **Local anesthetic *resistance* variants** have also been reported at the opposite end of the spectrum: a whole-exome sequencing study of a family with clinical local-anesthetic resistance (requiring unusually high doses for adequate block) identified a shared voltage-gated sodium channel gene variant, illustrating that *SCN* family variation modulates LA pharmacodynamics bidirectionally ([PMID:27243970](https://pubmed.ncbi.nlm.nih.gov/27243970/) — note: exact channel isoform and variant should be re-verified from the primary source before citation as fact).
- **Pseudocholinesterase (BCHE) variants** are relevant to *ester*-type LA metabolism (e.g., chloroprocaine, tetracaine, cocaine); atypical or deficient plasma cholinesterase activity slows hydrolysis and can prolong systemic exposure, though this is a much smaller contributor to LAST than amide-LA pharmacokinetics in modern practice.

**Environmental/procedural risk factors:**
- **Injection site vascularity** (intercostal > caudal/epidural > brachial plexus > femoral/sciatic, in classic teaching on absorption rank order), with paravertebral blocks now reported as carrying among the highest LAST incidence of common block types.
- **Dose and concentration** exceeding recommended maxima; use of long-acting, highly lipophilic and cardiotoxic agents (bupivacaine >> ropivacaine > lidocaine in intrinsic cardiotoxic potency).
- **Non-anesthesiologist administration** (dentists, emergency physicians, paramedics, cosmetic/dermatologic proceduralists) with less formal LAST training — a 2025 editorial analysis found up to 10% of surveyed cosmetic surgeons exceeded maximum recommended tumescent lidocaine doses, and only ~25% of non-anesthesia postgraduate trainees correctly identified toxic lidocaine dose thresholds (BJA 2025 editorial, Schwenk/Sneyd/Wu, PMC12674017).
- **Extremes of age** (neonates/infants have immature hepatic clearance and lower plasma protein [α1-acid glycoprotein] levels; the elderly have reduced clearance and cardiac reserve).
- **Pregnancy** — reduced plasma protein binding, increased cardiac output/absorption, and aortocaval compression alter presentation and risk (see Section 9).
- **Reduced muscle mass, low plasma protein (albumin, α1-acid glycoprotein) concentration, hepatic dysfunction, cardiac disease (conduction defects, ischemic heart disease), renal impairment, and metabolic or respiratory acidosis** — acidosis in particular increases the free fraction of LA and enhances ion trapping in tissue, compounding toxicity (NYSORA; StatPearls NBK499964).
- **Liposomal bupivacaine (Exparel) co-administration with additional amide LAs** within a 96-hour window — labeled as an additive-toxicity risk requiring dose adjustment ([EMA Exparel SmPC](https://www.ema.europa.eu/en/documents/product-information/exparel-liposomal-epar-product-information_en.pdf)).

**Protective factors:**
- **Ultrasound-guided regional anesthesia** — associated with a reduced risk of LAST versus landmark/nerve-stimulator techniques, attributed to more accurate needle placement, reduced total dose, and earlier recognition of intravascular puncture ([PMID:23788067](https://pubmed.ncbi.nlm.nih.gov/23788067/)).
- **Incremental (aliquoted) injection with intermittent aspiration** and **epinephrine-containing test dosing** (10–15 μg), which allows early detection of intravascular placement via a heart-rate rise ≥10 bpm or systolic BP rise ≥15 mmHg before a full dose is delivered.
- **Benzodiazepine premedication** may raise the seizure threshold, delaying/attenuating the CNS-excitatory phase.
- No specific *genetic* protective variant for LAST has been characterized in the literature reviewed (in contrast to the resistance-variant case above, which is pharmacodynamic rather than protective in a health sense).

**Gene–environment interactions.** The clearest documented interaction is between an **underlying mitochondrial fatty-acid oxidation defect (CPT II deficiency or related carnitine-cycle disorders)** and **standard/subtoxic doses of bupivacaine**, where the genetic lesion converts an otherwise safe dose into a cardiotoxic one by removing the myocardium's metabolic reserve for handling LA-induced mitochondrial stress. Similarly, **SCN5A conduction-disease variants** interact with amide LAs (which are themselves sodium-channel blockers) to produce exaggerated or atypical (bradyarrhythmic rather than tachyarrhythmic) cardiac presentations even at doses tolerated by patients with normal cardiac conduction.

---

## 3. Phenotypes

LAST classically presents along a **CNS-then-cardiovascular continuum**, though **atypical presentations occur in nearly 50% of reported cases** — i.e., cardiovascular signs may appear without preceding neurologic prodrome, or the two systems may be involved simultaneously ([PMID:35777259](https://pubmed.ncbi.nlm.nih.gov/35777259/); Formosan J Surg 2025 review).

### CNS phenotypes (excitatory phase, low-to-moderate plasma concentration)
- **Perioral/circumoral numbness and tingling** (paresthesia) — HP term: consider `HP:0040194` (Paresthesia)
- **Metallic taste** — no precise HPO term identified; record as free text/notes
- **Tinnitus** — `HP:0000360` (Tinnitus)
- **Visual disturbance** (blurred/tunnel vision) — `HP:0000505` (Visual impairment, generic)
- **Lightheadedness / dizziness** — `HP:0002321` (Vertigo) or a dizziness-specific term
- **Agitation, confusion, dysarthria (slurred speech)** — `HP:0031466` (Confusion, if it exists in current HPO release); `HP:0001260` (Dysarthria)
- **Muscle twitching / myoclonus**, progressing to **generalized tonic-clonic seizures** — `HP:0001336` (Myoclonus); `HP:0001250` (Seizure)

### CNS phenotypes (depressive phase, higher concentration)
- **Drowsiness progressing to unresponsiveness/coma**, **respiratory depression/apnea** — `HP:0001259` (Coma, generic term to be confirmed); `HP:0002105` (Respiratory failure)

### Cardiovascular phenotypes
- **Excitatory phase:** hypertension, tachycardia, ventricular ectopy/ventricular tachycardia
- **Depressive/collapse phase:** progressive **conduction delay** (PR/QRS widening), **bradycardia**, **hypotension**, **ventricular arrhythmias** (including polymorphic VT/torsades in some case reports), and **cardiovascular collapse/cardiac arrest**, sometimes with **pulseless electrical activity** refractory to standard ACLS ([PMC6068002](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6068002/); [PMC9566458](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9566458/)).
  - Candidate HP terms: `HP:0011675` (Arrhythmia), `HP:0001662` (Sinus bradycardia), `HP:0004756` (Ventricular tachycardia — verify exact code), `HP:0001695` (Cardiac arrest), `HP:0002615` (Hypotension), `HP:0001657` (Prolonged QT interval — if QT prolongation specifically implicated with certain agents/metabolites).
- **Delayed presentation:** cardiac events (including arrest) have been reported hours after the causative block (e.g., 5 hours post continuous femoral nerve block in one case, [PMC9566458](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9566458/)), underscoring the need for extended monitoring.

### Laboratory abnormalities
- **Metabolic/respiratory acidosis** (both a risk factor and a consequence, since acidosis potentiates further LA toxicity in a feed-forward loop).
- **Elevated free (unbound) LA plasma concentration** on assay, where available — toxic effects of bupivacaine have been documented at plasma concentrations as low as **800 ng/mL**, while early subjective CNS symptoms are typically reported at higher concentrations of **2500–4000 ng/mL** (Exparel/EMA labeling data).
- **Methemoglobinemia** can occur with certain LA classes/metabolites (notably prilocaine and, less commonly, benzocaine and its metabolite o-toluidine), presenting as **cyanosis unresponsive to supplemental oxygen** with a characteristic "chocolate brown" arterial blood sample — treated with **methylene blue**.

### Phenotype characteristics
- **Onset:** Typically rapid — seconds to a few minutes after intravascular injection; delayed onset (minutes to several hours) is well described with slower systemic absorption from tissue depots (e.g., continuous peripheral nerve block catheters, tumescent infiltration, topical/mucosal application).
- **Severity:** Highly variable, from isolated perioral numbness to fatal cardiac arrest; severity correlates with peak free plasma concentration, agent lipophilicity/potency, and patient risk factors.
- **Progression:** Classically progressive along the excitatory→depressive continuum, but course can be non-linear; nearly half of reported cases skip or truncate the classical sequence.
- **Frequency:** Systemic toxicity from local anesthetics has been estimated in **~0.03% of peripheral nerve blocks (0.27 episodes/1000 blocks)**; more recent pooled estimates place major LAST events at **0.04–1.8 per 1000 peripheral nerve blocks**, and overall incidence across high-risk procedures at **1–3 per 1000** ([NYSORA](https://www.nysora.com/topics/complications/local-anesthetic-systemic-toxicity/); UpToDate; PMID:35777259).

### Quality of life impact
Acute LAST events, when survived, are generally not associated with chronic disability if promptly treated; however, cardiac arrest with prolonged resuscitation carries the same post-cardiac-arrest morbidity risk (hypoxic-ischemic brain injury, reduced functional status) as arrest from any other cause. Data specifically quantifying QoL instruments (EQ-5D, SF-36) post-LAST were not identified in the literature searched — this is likely a genuine data gap given the acute, procedural nature of the condition and the rarity of long-term follow-up cohorts.

---

## 4. Genetic/Molecular Information

LAST is not a monogenic disease, so this section addresses (a) genes implicated in **modifying susceptibility** and (b) the **molecular drug targets** whose engagement constitutes the toxic mechanism.

**Modifier/susceptibility genes:**
- **CPT2** (Carnitine Palmitoyltransferase 2; HGNC gene) — biallelic pathogenic variants cause CPT II deficiency; implicated in increased bupivacaine cardiotoxicity susceptibility at otherwise sub-toxic doses.
- **SLC22A5 (OCTN2)** and other carnitine-cycle genes (CPT1A, CACT/SLC25A20) — broader fatty-acid oxidation pathway; theoretically relevant by the same mitochondrial mechanism, though direct LAST case evidence is sparser than for CPT2.
- **SCN5A** (cardiac Nav1.5 gene) — pathogenic/likely pathogenic variants (Brugada syndrome, progressive cardiac conduction disease, dilated cardiomyopathy with conduction defect) confer heightened cardiac sensitivity to sodium-channel-blocking LAs. Suggested reference: ClinVar/ClinGen SCN5A-Brugada syndrome gene-disease validity assertions (dismech `CGGV:` structured-source citation pattern would apply if curating).
- **BCHE** (butyrylcholinesterase/pseudocholinesterase) — variants affecting ester-LA hydrolysis rate; more classically linked to succinylcholine sensitivity but mechanistically analogous for ester-type LAs.

**Molecular drug targets (the toxicity mechanism itself, not inherited variants):**
- **Voltage-gated sodium channels (Nav)** — the primary target. LAs bind the intracellular pore-lining domain, producing tonic and **use-dependent block**; cardiac Nav1.5 is the dominant cardiac isoform, and bupivacaine's high lipophilicity and slow "fast-in/slow-out" channel kinetics ("fast in, slow out" dissociation from the inactivated state) account for its disproportionate cardiotoxic potency relative to lidocaine ([PMID:25008571](https://pubmed.ncbi.nlm.nih.gov/25008571/)). Bupivacaine also accelerates development of Nav1.5 open-state slow inactivation.
- **Voltage-gated potassium channels** — TREK-1 (two-pore-domain K+ channel), KATP, and SK2 channels are all inhibited by bupivacaine, contributing to membrane excitability changes and impaired ischemic myocardial protection ([PMID:42589553](https://pubmed.ncbi.nlm.nih.gov/42589553/); *Int J Mol Sci* 2025 molecular mechanisms review).
- **Voltage-gated calcium channels (CaV1.3 and related L-type channels)** — suppressed by bupivacaine, impairing excitation-contraction coupling.
- **Mitochondrial carnitine-acylcarnitine translocase** — directly inhibited by bupivacaine, blocking long-chain fatty-acid entry into the mitochondrial matrix and impairing fatty-acid-supported oxidative phosphorylation, the myocardium's dominant energy source.
- **Cardiolipin** (inner mitochondrial membrane phospholipid) — bupivacaine, but not lidocaine, disrupts cardiolipin-containing membranes/liposomes, degrading respiratory-chain organization ([PMID:17643405](https://pubmed.ncbi.nlm.nih.gov/17643405/)).
- **GABA-A receptors and NMDA/non-NMDA glutamate receptors** — LA-mediated disinhibition of GABAergic tone plus glutamatergic receptor involvement underlies the CNS excitatory (seizure) phase.

**Variant classification / allele frequency:** Because LAST susceptibility variants are drawn from rare-disease genes (CPT2, SCN5A) rather than a LAST-specific gene, standard ClinVar/gnomAD resources apply to the underlying conditions (CPT II deficiency, Brugada syndrome/SCN5A-related disease) rather than to a LAST-specific allele. No LAST-specific pathogenic allele frequency data were identified.

**Epigenetics / chromosomal abnormalities:** No literature was identified describing epigenetic regulation or chromosomal-abnormality contributions specific to LAST susceptibility; this reflects the condition's fundamentally pharmacologic/toxicologic rather than developmental-genetic nature.

---

## 5. Environmental Information

- **Primary environmental factor: the local anesthetic drug itself**, administered via injection, infiltration, or topical/mucosal/transdermal application, functions as the causal exposure. Relevant CHEBI entities include bupivacaine, levobupivacaine, ropivacaine, lidocaine, mepivacaine, prilocaine, chloroprocaine, and tetracaine (amide and ester classes).
- **Route and setting of exposure** matter greatly: peripheral nerve block, epidural/neuraxial, paravertebral block, tumescent liposuction infiltration, dental nerve block, topical anesthesia prior to endoscopy/transesophageal echocardiography (documented case: ~3000 mg topical lidocaine causing cardiac arrest requiring ECMO, [PMC6068002](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6068002/)), and perioperative/ERAS intravenous lidocaine infusions.
- **Out-of-hospital/non-monitored settings**: an estimated **23% of LAST cases occur outside the hospital** (e.g., dental offices, outpatient cosmetic clinics), where rescue resources (lipid emulsion, advanced airway, ACLS) may be less immediately available (BJA 2025 editorial).
- **Lifestyle/behavioral factors**: none specific to LAST causation itself have been identified (unlike chronic diseases influenced by smoking/diet); the principal modifiable "behavioral" factor is **clinician practice** — dose calculation errors, failure to aspirate before injection, and lack of ultrasound guidance.
- **Infectious agents:** not applicable — LAST is not an infectious disease.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. A local anesthetic (e.g., bupivacaine) is administered for regional/local anesthesia and **enters the systemic circulation** in excess — via inadvertent intravascular injection, rapid absorption from a vascular tissue bed, or cumulative/absolute overdose. *(Demonstrated — the defining initiating event.)*
2. The rising **free (unbound) plasma concentration** of the drug **leads to** engagement of voltage-gated sodium channels throughout excitable tissue, with the CNS and heart affected earliest owing to their high perfusion and channel density. *(Demonstrated.)*
3. In the **CNS**, LA blockade **preferentially inhibits inhibitory GABAergic interneurons** before excitatory glutamatergic pathways (differential susceptibility of inhibitory pathways), which **results in** a net disinhibition of cortical excitatory circuits — **leading to** the excitatory phenotype (perioral numbness, tinnitus, agitation, myoclonus, seizures). *(Demonstrated in animal/ex vivo pharmacology; the differential-sensitivity account is a long-standing accepted model.)*
4. With continued rising concentration, **global sodium (and other ion) channel blockade** in the CNS **causes** widespread neuronal conduction failure, **resulting in** the depressive phase (coma, respiratory depression/apnea). *(Demonstrated.)*
5. In parallel, in the **heart**, LA binding to cardiac Nav1.5 **produces tonic and use-dependent sodium-channel blockade**, which **slows phase-0 depolarization and impairs conduction** — **leading to** PR/QRS prolongation, bradyarrhythmia, and re-entrant ventricular arrhythmias (including ventricular tachycardia/fibrillation). Bupivacaine's high lipophilicity causes disproportionately **slow dissociation ("fast-in, slow-out")** from the inactivated channel state relative to lidocaine, **explaining** its greater arrhythmogenic potency at equi-analgesic doses. *(Demonstrated via electrophysiology studies, [PMID:25008571](https://pubmed.ncbi.nlm.nih.gov/25008571/).)*
6. Concurrently, LA molecules **inhibit cardiac potassium channels (TREK-1, KATP, SK2) and L-type calcium channels**, which **further destabilizes membrane excitability and impairs excitation-contraction coupling**, **contributing to** contractile dysfunction independent of the sodium-channel effect. *(Demonstrated in cellular electrophysiology models; translational magnitude in vivo is less certain — flagged as partially inferred.)*
7. At the mitochondrial level, bupivacaine **inhibits the carnitine-acylcarnitine translocase**, which **blocks long-chain fatty acid entry into the mitochondrial matrix**, **impairing** the myocardium's primary (fatty-acid-based) route of ATP generation. Bupivacaine additionally **disrupts cardiolipin-containing inner mitochondrial membranes**, which **degrades respiratory-chain (electron transport chain) organization**, **compounding** the energy-production failure. Together these **result in** progressive **myocardial bioenergetic failure**, which **potentiates** the electrophysiological effects above and **drives** the transition from arrhythmia to pump failure and cardiovascular collapse. *(Demonstrated in isolated mitochondria/cardiomyocyte models; the *quantitative* contribution relative to direct channel block in whole-organism toxicity is inferred rather than fully resolved — an open mechanistic question.)*
8. **Systemic physiological derangements** — hypoxia, acidosis, and reduced tissue perfusion arising from the seizure and/or the evolving cardiovascular collapse — **create a feed-forward loop**: acidosis increases the ionized (protonated) fraction of LA trapped intracellularly ("ion trapping") and increases the free fraction available to bind channels, **amplifying** both CNS and cardiac toxicity and **worsening** resuscitation difficulty. *(Demonstrated clinically and pharmacologically — this is the physiological basis for aggressive airway/ventilation management as first-line LAST treatment.)*
9. In patients with a **pre-existing mitochondrial fatty-acid oxidation defect (e.g., CPT II deficiency)** or a **cardiac sodium-channelopathy (SCN5A variant)**, the above cascade **is triggered at markedly lower LA doses/concentrations** than in the general population, because the myocardium's metabolic reserve (step 7) or baseline channel function (step 5) is already compromised. *(Demonstrated via case reports; not systematically quantified.)*
10. Without intervention, the terminal common pathway is **refractory ventricular arrhythmia, pulseless electrical activity, or asystole — cardiac arrest**, which in a minority of cases is resistant to standard resuscitation and lipid emulsion, **necessitating** extracorporeal cardiopulmonary resuscitation (ECPR/ECMO) as rescue. *(Demonstrated in multiple case reports, e.g., [PMC6068002](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6068002/).)*

### Molecular pathways
No single canonical signaling pathway (Wnt/MAPK/mTOR/PI3K-AKT) drives LAST; the dominant "pathways" are **ion-channel electrophysiology** (Nav1.5/Nav1.1 family, Kv/TREK-1/KATP/SK2, CaV1.3) and **mitochondrial bioenergetics** (fatty-acid β-oxidation entry via carnitine shuttle, oxidative phosphorylation/electron transport chain). Suggested GO Biological Process terms: `GO:0086006` (voltage-gated sodium channel activity involved in cardiac muscle cell action potential), `GO:0034642`/oxidative-phosphorylation-related terms, `GO:0006635` (fatty acid beta-oxidation).

### Cellular processes
- **Excitotoxicity/seizure generation** in cortical neurons (GABAergic disinhibition + NMDA receptor involvement).
- **Apoptosis** in neuronal cell models: in SH-SY5Y neuroblastoma cells, bupivacaine induces apoptosis via reactive oxygen species (ROS) production, mitochondrial complex I/III impairment, and loss of mitochondrial membrane potential ([PMID:42589553](https://pubmed.ncbi.nlm.nih.gov/42589553/)).
- **Endoplasmic reticulum (ER) stress** — activation of ATF6, IRE1, and PERK arms of the unfolded protein response, with downstream Bcl-2 family dysregulation and caspase activation, has been demonstrated across multiple LA-exposed cell models.
- Suggested GO terms: `GO:0006915` (apoptotic process), `GO:0034976` (response to endoplasmic reticulum stress), `GO:0006979` (response to oxidative stress).

### Protein dysfunction
LA binding does not cause classical misfolding/aggregation; rather it produces **acute, reversible functional inhibition** (channel block) of Nav/Kv/CaV channels and the carnitine-acylcarnitine translocase, and disruption of the cardiolipin lipid microenvironment that organizes electron-transport-chain complexes.

### Metabolic changes
**Impaired fatty-acid oxidation** and **reduced ATP availability** in cardiac and neural tissue are central; amide LAs "acutely inhibit myocardial oxygen consumption," with bupivacaine producing stronger respiratory-chain inhibition than lidocaine ([PMID:42589553](https://pubmed.ncbi.nlm.nih.gov/42589553/)).

### Immune system involvement
Not a primary feature; LAST is not classically an immune-mediated or inflammatory condition (in contrast to true LA hypersensitivity/allergic reactions, which are a distinct, much rarer entity, typically to ester LAs or amide-LA preservatives).

### Tissue damage mechanisms
**Oxidative stress** (ROS generation, complex I/III impairment) and **bioenergetic failure** rather than classical ischemia/fibrosis/necrosis dominate the acute injury; myocardial and neuronal injury is primarily **functional/electrophysiological** rather than structural in the acute phase, though prolonged arrest can secondarily cause hypoxic-ischemic injury to brain and other organs.

### Biochemical abnormalities
Direct **ion channel dysfunction** (Nav, Kv, CaV) and **enzyme inhibition** (carnitine-acylcarnitine translocase) constitute the core biochemical lesions, rather than an inherited enzyme deficiency (except in the CPT II-deficient subgroup, where the LA effect is superimposed on a baseline enzymatic deficiency).

### Molecular profiling / advanced technologies
No transcriptomic, proteomic, metabolomic, lipidomic, single-cell, or spatial-transcriptomic dataset specific to human LAST was identified in this search — this is an area of the mechanism space that remains largely uncharacterized at the -omics level in humans, with mechanistic insight instead derived from targeted electrophysiology and isolated-mitochondria/cell-line studies (SH-SY5Y neuroblastoma cells, isolated cardiomyocytes, Xenopus oocyte channel expression systems).

**Cell types implicated (suggested CL terms):** cardiac muscle cell/cardiomyocyte (`CL:0000746`), Purkinje myocyte, GABAergic interneuron (`CL:0000617` or more specific), glutamatergic neuron, neuroblastoma-derived neuron-like cell (SH-SY5Y, a model system rather than a native cell type).

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Central nervous system (brain/cortex) and heart (myocardium and cardiac conduction system) — the two most richly perfused, ion-channel-dense organ systems.
- **Secondary:** Respiratory system (apnea/respiratory failure secondary to CNS depression or seizure), vasculature (hypotension from combined direct vasodilation and myocardial depression).
- **Body systems:** Nervous system, cardiovascular system, and secondarily the respiratory system.
- Suggested UBERON terms: `UBERON:0000955` (brain), `UBERON:0000948` (heart), `UBERON:0001987` (placenta, relevant in the pregnancy-specific pharmacokinetic discussion).

**Tissue and cell level:**
- **Cardiac conduction tissue** (SA/AV node, His-Purkinje system) and **ventricular myocardium** (cell type: cardiomyocyte).
- **Cortical and subcortical neurons**, with particular vulnerability of **inhibitory GABAergic interneurons** in the early excitatory phase.
- Suggested CL terms: cardiac muscle cell (`CL:0000746`), Purkinje myocyte of heart conducting system, cortical GABAergic interneuron, cortical glutamatergic neuron.

**Subcellular level:**
- **Plasma membrane** (site of Nav/Kv/CaV channel blockade) — GO Cellular Component `GO:0005886` (plasma membrane).
- **Mitochondria**, specifically the **inner mitochondrial membrane** (cardiolipin disruption, electron transport chain) and **mitochondrial matrix** (carnitine-acylcarnitine translocase site) — GO terms `GO:0005743` (mitochondrial inner membrane), `GO:0005759` (mitochondrial matrix).
- **Endoplasmic reticulum** (ER-stress pathway activation) — `GO:0005783`.

**Localization:** LAST is a **systemic/generalized** process rather than a laterality-defined disease; it is not unilateral or asymmetric, given hematogenous distribution of the causative drug throughout the CNS and myocardium.

---

## 8. Temporal Development

**Onset:** LAST has no age-of-onset in the developmental sense (it is not a genetic/developmental disease); rather, it can occur at **any age**, from neonates (e.g., inadvertent intravenous levobupivacaine infusion in infants, [PMC10221613](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10221613/); LAST after caudal block in an infant, [PMC11830499](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11830499/)) through late adulthood, whenever a local anesthetic is administered. **Onset pattern is typically acute**, occurring within seconds to minutes of intravascular injection, though **delayed presentations of minutes to several hours** are well documented with slower absorption routes (continuous infusion catheters, tumescent infiltration, topical/mucosal application).

**Progression:** No formal disease-staging system exists (unlike cancer staging); clinically, LAST is often described along a **severity continuum** from mild prodromal symptoms → CNS excitation → CNS depression, and, on the cardiovascular axis, from excitation (hypertension/tachyarrhythmia) → depression (bradycardia/hypotension/conduction block) → collapse/cardiac arrest. **Progression rate is variable** — some cases progress from first symptom to cardiac arrest within minutes; others plateau at mild prodromal symptoms if the anesthetic is stopped and supportive care instituted promptly. The **disease course is acute and self-limited** once the causative exposure is terminated and the drug is redistributed/metabolized/cleared (aided by lipid emulsion sequestration) — LAST does not have a chronic or relapsing-remitting natural history.

**Patterns:**
- **Remission** is generally **treatment-induced** (cessation of LA administration, airway/ventilatory support, benzodiazepines for seizures, lipid emulsion, and ACLS as needed) rather than spontaneous, though very mild cases (isolated perioral numbness) may resolve without specific intervention as the drug redistributes.
- **Critical/vulnerable periods:** the **immediate post-injection window** (first several minutes) is the period of highest vulnerability for rapid-onset cardiovascular collapse from intravascular injection; a **second, distinct** vulnerable window exists **hours after** block placement or catheter initiation, when slow absorption from a tissue depot or continuous infusion can produce delayed-onset toxicity — this underlies ASRA's post-stabilization monitoring recommendations (see Section 12).

---

## 9. Inheritance and Population

**Epidemiology:**
- Estimated incidence: **1–3 per 1000 high-risk procedures** overall; **0.04–1.8 per 1000 peripheral nerve blocks** for major LAST events; an older but frequently cited estimate places systemic toxicity at **0.03% of peripheral nerve blocks (0.27/1000 blocks)**.
- **Paravertebral nerve blocks** carry the highest reported incidence among common block types, followed by upper-extremity and trunk/lower-extremity blocks (NYSORA; PMID:35777259).
- **Ultrasound guidance has reduced incidence** from peripheral nerve blocks compared with a decade ago, but **incidence from infiltrative anesthesia in non-operating-room settings has remained static** — an important recent (2025) epidemiological finding highlighting a shift in the risk landscape toward office-based and non-anesthesiologist-administered LA use (PMC12674017, BJA 2025 editorial).
- **Mortality data (FAERS, 1968–2023):** 1,473 total reported LAST deaths across all local anesthetics; **813 (55%) attributed to lidocaine**, averaging **49 lidocaine-related deaths/year** versus 13/year for all other agents combined over the past three years — a marked and unexpected shift, since bupivacaine-associated deaths fell substantially after the 2010-era practice advisories while lidocaine deaths remained essentially unchanged (BJA 2025 editorial, PMC12674017). In a parallel literature review of case reports from 2011 onward, **69 deaths** were identified, with **lidocaine responsible for 74%**.
- **Lipid emulsion was administered in only ~12% of documented LAST cases**, indicating a substantial treatment/education gap.

**For genetic etiology (in the susceptibility-modifier sense):**
- **CPT II deficiency:** autosomal recessive inheritance; the most common inherited long-chain fatty-acid oxidation defect, though still individually rare.
- **SCN5A-related cardiac disease (e.g., Brugada syndrome):** typically autosomal dominant with **incomplete penetrance** and **variable expressivity** — well documented for the underlying channelopathy, though penetrance/expressivity data specific to "LAST susceptibility" (as opposed to the channelopathy's primary arrhythmic phenotype) have not been separately quantified.
- **Founder effects / carrier frequency:** Not established for a LAST-specific allele; carrier frequency data would need to be drawn from the underlying CPT2 or SCN5A disease-gene literature (gnomAD) rather than from a LAST-specific registry.
- **Consanguinity:** relevant only insofar as it increases the prior probability of biallelic CPT2 (or other autosomal recessive metabolic) variants in a given patient/population.

**Population demographics:**
- No specific ethnic or geographic predisposition to LAST itself has been described (as expected for a predominantly iatrogenic/pharmacologic condition), though the prevalence of underlying susceptibility genotypes (e.g., specific SCN5A variants more common in certain Southeast Asian populations in the context of Brugada syndrome) could theoretically skew regional risk — this has not been formally studied for LAST outcomes specifically.
- **Sex ratio:** Not clearly reported as skewed in the general LAST literature; the 2024 pregnancy-focused cohort study specifically examined a **female (pregnant vs. non-pregnant)** comparison rather than an overall male:female LAST ratio (PMID:39398741).
- **Pregnancy-specific findings** (TriNetX retrospective cohort, 2013–2023, n=276 matched pregnant vs. 276 non-pregnant LAST patients): pregnant patients had **significantly higher risk of cardiac depression** (RR 1.96, 95% CI 1.44–2.66, p<0.01) and **significantly lower risk of** cardiac excitation (RR 0.38), prodromal symptoms (RR 0.17), CNS excitation (RR 0.44), and CNS depression (RR 0.24) compared with non-pregnant patients — i.e., pregnant patients with LAST are more likely to present with **direct cardiac depression, skipping the classical prodrome and excitatory phases** ([PMID:39398741](https://pubmed.ncbi.nlm.nih.gov/39398741/)). This atypical presentation pattern has direct clinical-recognition implications and reflects pregnancy-associated physiologic changes (increased cardiac output, aortocaval compression, reduced plasma protein binding capacity, and possibly altered receptor sensitivity).
- **Age distribution:** LAST is reported across the full age spectrum, from neonates/infants (caudal block, IV infiltration errors) to elderly patients undergoing regional anesthesia for orthopedic and other procedures; extremes of age are independently identified risk factors rather than age itself defining a typical "affected population."

---

## 10. Diagnostics

LAST is fundamentally a **clinical diagnosis** made on the basis of a temporally plausible LA exposure plus compatible CNS and/or cardiovascular signs; there is no single confirmatory laboratory test used in real time.

**Clinical tests:**
- **Continuous ECG monitoring** is the standard of care during and after any regional anesthesia procedure, allowing detection of PR/QRS widening, arrhythmia, and ST/T-wave changes.
- **Continuous pulse oximetry and blood pressure monitoring** to detect hypoxia and hemodynamic compromise.
- **Plasma/serum local anesthetic level assay** (where available, typically in specialized/research settings rather than routine point-of-care practice) can retrospectively confirm elevated total or free LA concentration; not useful for real-time diagnosis given turnaround time.
- **Arterial blood gas** to assess for acidosis, which both signals severity and worsens further toxicity if uncorrected.
- **Co-oximetry** if methemoglobinemia is suspected (cyanosis unresponsive to oxygen, "chocolate brown" blood) — relevant particularly for prilocaine and benzocaine exposures.

**Genetic testing:** Not part of acute LAST diagnosis. It becomes relevant **retrospectively or prospectively** in two scenarios: (1) **after an unexplained severe/refractory LAST event at a sub-toxic dose**, prompting consideration of an underlying **fatty-acid oxidation disorder (CPT2 gene sequencing)** or **cardiac channelopathy (SCN5A and related arrhythmia gene panel)**; (2) **before regional anesthesia in a patient with a known family history** of a fatty-acid oxidation disorder or inherited arrhythmia syndrome, to inform anesthetic risk stratification and dose conservatism.

**Clinical criteria / differential diagnosis:** No DSM/ICD-based formal diagnostic criteria exist; clinicians rely on **temporal association with LA administration** plus **exclusion of alternative causes** of seizure (epilepsy, hypoglycemia, eclampsia in obstetric patients, high/total spinal anesthesia) and of cardiac arrest/arrhythmia (myocardial infarction, pulmonary embolism, anaphylaxis, vasovagal collapse, primary arrhythmic disease). **High/total spinal anesthesia** is an important mimic/co-occurring differential in the neuraxial setting, since it also produces hypotension, bradycardia, and loss of consciousness without necessarily reflecting systemic LA toxicity per se (distinguished by the mechanism — neuraxial sympathetic blockade vs. systemic drug toxicity — though clinically the two can be difficult to distinguish acutely and management overlaps).

**Screening:** No population-level screening program exists for LAST susceptibility; the closest analog is **pre-procedural risk-factor assessment** (age, pregnancy, hepatic/renal/cardiac disease, personal/family history of unexplained anesthesia complications or metabolic myopathy) rather than a formal genetic or biomarker screening test.

**Diagnostic guideline references:** The current reference frameworks are professional society guidelines rather than diagnostic-code-based criteria — principally the **ASRA (American Society of Regional Anesthesia and Pain Medicine) Practice Advisories** (2010 original; Third Practice Advisory Executive Summary, 2018, [PMID:29356773](https://pubmed.ncbi.nlm.nih.gov/29356773/)) and the **ASRA LAST Checklist, 2020 version** ([PMID:33148630](https://pubmed.ncbi.nlm.nih.gov/33148630/)), plus emergency-medicine-oriented narrative reviews ([PMID:35777259](https://pubmed.ncbi.nlm.nih.gov/35777259/)) and specialty protocols such as the International Pain and Spine Intervention Society's LAST emergency protocol.

---

## 11. Outcome/Prognosis

**Survival and mortality:** With prompt recognition and treatment (cessation of LA, airway management, benzodiazepines, lipid emulsion, ACLS as needed), the majority of LAST events **resolve without permanent sequelae**. However, LAST remains a recognized cause of **anesthesia-related death**: FAERS data (1968–2023) recorded **1,473 LAST-attributed deaths**, with lidocaine now responsible for the majority (55% of FAERS deaths; 74% of recent case-report deaths) despite its reputation as a "safer" agent — reflecting both its widespread, often less-supervised use and possibly under-recognition of its cardiotoxic potential at high cumulative/infusion doses (BJA 2025 editorial).

**Morbidity and function:** Acute morbidity is dominated by the direct consequences of seizure (aspiration risk, injury) and of cardiac arrest/hypotension (organ hypoperfusion, and — in prolonged arrest — hypoxic-ischemic brain injury). There is no described chronic LAST-specific disability syndrome in survivors who receive timely treatment; outcomes in refractory cases requiring ECMO-supported resuscitation mirror those of cardiac arrest from other causes and depend heavily on time-to-ECMO cannulation and total downtime.

**Disease course / complications:** Documented complications include **refractory ventricular arrhythmia**, **pulseless electrical activity/asystole**, **aspiration pneumonitis** (from seizure-associated loss of airway protection), and, in the methemoglobinemia subgroup, **tissue hypoxia** from impaired oxygen-carrying capacity if unrecognized/untreated. **Extracorporeal cardiopulmonary resuscitation (ECPR)** has emerged in case reports as a rescue therapy for LAST-associated cardiac arrest refractory to lipid emulsion and standard ACLS ([PMC6068002](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6068002/)).

**Recovery potential:** Generally favorable when treatment is initiated promptly (within the first few minutes of symptom onset), given the pharmacokinetically reversible nature of LA channel blockade once tissue/plasma drug concentration falls (aided by lipid-emulsion-facilitated redistribution/clearance — see Section 12). Recovery potential is markedly worse in delayed-recognition or refractory-arrest scenarios.

**Prognostic factors:** Time to cessation of LA administration and time to initiation of lipid emulsion/ACLS are the most clinically actionable prognostic determinants; presence of underlying cardiac disease, pregnancy (via atypical presentation delaying recognition), and extremes of age are additional adverse prognostic modifiers. A 2023 multicenter simulation initiative (the **LAST Collaborative**, 10 hospitals) found that **simulation-based training reduced time to lipid emulsion administration by ~30% on average** after a single drill, directly linking systems-level preparedness to a key prognostic time-interval.

---

## 12. Treatment

### Pharmacotherapy
- **20% intravenous lipid emulsion (ILE)** is the specific antidote and first-line pharmacologic treatment. **ASRA 2020 dosing:** for patients <70 kg, a bolus of **1.5 mL/kg over 2–3 minutes**, followed by an infusion of **0.25 mL/kg/min**; for patients >70 kg, a bolus of **100 mL over 2–3 minutes**, followed by an infusion of **250 mL over 15–20 minutes**. Continue the infusion for at least 15 minutes after achieving hemodynamic stability; if inadequate, repeat the bolus or double the infusion rate. **Upper dosing limit: ~12 mL/kg.** The order of bolus vs. infusion administration and the specific infusion method are not considered critical (ASRA 2020 Checklist, [PMID:33148630](https://pubmed.ncbi.nlm.nih.gov/33148630/); NYSORA).
- Suggested NCIT term for lipid emulsion therapy: consider `NCIT:C15986` (Pharmacotherapy) as the generic treatment_term with a therapeutic_agent binding for the lipid emulsion product (verify a specific NCIT CHEBI/agent code before curation use).
- **Benzodiazepines** are the drugs of choice for seizure termination (e.g., midazolam, lorazepam); propofol is discouraged as an anticonvulsant in this setting due to its own cardiodepressant potential compounding LAST-induced cardiac depression.
- **Epinephrine**, when needed for severe arrhythmia or hypotension, should be given in **small bolus doses (≤1 mcg/kg)** rather than standard ACLS doses, per ASRA guidance, given evidence that larger doses may worsen outcomes in the lipid-emulsion-treated LAST arrest model.
- **Avoid:** vasopressin, calcium-channel blockers, beta-blockers, and additional local anesthetics (including as antiarrhythmics) during LAST management, per ASRA 2020.
- **Methylene blue (1–2 mg/kg IV over 5 minutes)** is used specifically for **LA-associated methemoglobinemia** (notably prilocaine, benzocaine).

### Advanced therapeutics
- **Extracorporeal membrane oxygenation (ECMO)/ECPR** is reserved for **refractory cardiac arrest** unresponsive to lipid emulsion and standard ACLS — documented as successful rescue in case reports of severe LAST (e.g., topical lidocaine-induced arrest before transesophageal echocardiography, [PMC6068002](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6068002/)).
- No gene therapy, cell therapy, RNA-based therapy, targeted therapy, or immunotherapy is applicable to LAST, consistent with its acute pharmacotoxicologic (rather than molecular-genetic) disease mechanism.

### Surgical/interventional
Not applicable as primary treatment; the causative regional-anesthesia procedure itself is, of course, surgical/interventional in origin but is not a "treatment" for LAST.

### Supportive and rehabilitative
- **Airway management and 100% oxygen/ventilatory support** to prevent hypoxia and acidosis, both of which potentiate further LA toxicity — this is emphasized as a **first-line, arguably highest-priority** intervention in all major guidelines, preceding even lipid emulsion in sequence (though both should be pursued in parallel when possible).
- **Correction of acidosis** (via adequate ventilation ± sodium bicarbonate) to reduce ion trapping and free LA fraction.
- Standard **ACLS/CPR** for cardiac arrest, modified per the epinephrine-dosing and drug-avoidance guidance above.
- **Rehabilitation** (physical/occupational therapy) is relevant only in the rare setting of post-arrest hypoxic-ischemic injury, and is not disease-specific to LAST.

### Experimental
No LAST-specific investigational drug trials were identified in the search (ClinicalTrials.gov results returned were primarily about *causes* of neurologic events after regional anesthesia rather than LAST-treatment trials, e.g., NCT07238933). Current "experimental" activity in this space is concentrated on **refining lipid-emulsion mechanistic understanding and dosing** (the emerging "lipid shuttle/lipid subway" model, described below) rather than novel pharmacologic agents.

### Treatment outcomes and gaps
- **Lipid emulsion was used in only ~12% of documented LAST cases**, and only **~25% of non-anesthesia postgraduate trainees** correctly identified toxic lidocaine dose thresholds in surveys — indicating substantial gaps in both treatment application and provider knowledge, particularly outside anesthesiology (BJA 2025 editorial).
- A 2023 multicenter simulation collaborative (**LAST Collaborative**, 10 hospitals) demonstrated that a **single simulation drill per site reduced time-to-lipid-emulsion-administration by ~30% on average**, supporting simulation-based training as an effective systems intervention.

### Mechanism of lipid emulsion (relevant to understanding treatment rationale)
The classical **"lipid sink" model** holds that IV lipid emulsion creates an expanded intravascular lipid phase that sequesters lipophilic LA molecules away from cardiac and neural tissue. More recent mechanistic work refines this into a **"lipid shuttle"/"lipid subway" model**, in which the lipid compartment **scavenges LA from high-blood-flow, sensitive organs (heart, brain)** and **redistributes it to muscle for storage and to the liver for detoxification**, rather than simply acting as a static reservoir. Lipid emulsion also exerts **direct cardiotonic effects** — increasing myocardial contractility and cardiac output, partly via enhanced fatty-acid substrate delivery for mitochondrial ATP production (counteracting the carnitine-shuttle blockade described in Section 6) and partly via volume-expansion-mediated preload augmentation, along with modulatory effects on cardiac ion channels. A meta-analysis of animal LAST models found lipid emulsion **reduced the odds of death in resuscitative models (OR 0.24, 95% CI 0.1–0.56, p=0.0012)** ([PMID:28346007](https://pubmed.ncbi.nlm.nih.gov/28346007/)).

### Therapeutic modality mapping (for structured curation)
- Lipid emulsion therapy: `therapeutic_modality: OTHER` (or a lipid-based pharmacotherapy category if a more specific value exists in the target schema) — not a standard small-molecule/biologic category.
- Benzodiazepines, epinephrine, methylene blue: `SMALL_MOLECULE`.
- ECMO: `DEVICE`.

---

## 13. Prevention

**Primary prevention** is the dominant prevention strategy for LAST, since there is no vaccine or population-level primary-prevention program analogous to infectious or chronic disease prevention:

- **Dose vigilance:** calculating the **cumulative dose of all local anesthetics** to be administered (accounting for any prior or concurrent LA exposure, including liposomal bupivacaine's 96-hour additive-toxicity window) and selecting the **lowest effective dose**.
- **Ultrasound guidance** for peripheral nerve blocks, associated with reduced LAST incidence ([PMID:23788067](https://pubmed.ncbi.nlm.nih.gov/23788067/)).
- **Incremental injection** in small aliquots (3–5 mL) with **15–30 second pauses** between injections, combined with **frequent aspiration** to detect inadvertent intravascular needle/catheter placement.
- **Epinephrine-containing test dosing** (10–15 μg) in selected higher-risk techniques (e.g., epidural), using a heart-rate increase ≥10 bpm or systolic BP increase ≥15 mmHg as a positive intravascular marker.
- **Patient-specific risk-factor evaluation** before block placement (extremes of age, pregnancy, hepatic/renal/cardiac disease, low plasma protein states, personal/family history suggestive of a fatty-acid oxidation disorder or inherited arrhythmia syndrome).

**Secondary prevention (early detection):**
- **Continuous vital-sign and ECG monitoring** throughout LA administration and for an appropriate post-procedure window (ASRA recommends observation for **at least 2 hours after a seizure** and **4–6 hours after cardiovascular instability**, with longer critical-care-level monitoring after cardiac arrest or persistent symptoms).
- Institutional **immediate availability of 20% lipid emulsion and a LAST rescue kit/checklist** at any site where LA is administered, including non-operating-room and outpatient settings.

**Tertiary prevention:** Prompt, guideline-concordant treatment (Section 12) to prevent progression to refractory arrest and to minimize post-arrest morbidity in patients who do experience a severe event.

**Genetic counseling:** Relevant in the narrow context of a patient or family member with known **CPT II deficiency** or an inherited **cardiac channelopathy (SCN5A-related disease)** — pre-procedural genetic counseling and anesthesia-risk discussion, along with conservative LA dosing/monitoring plans, would be the applicable preventive genetic intervention, though this is not a formal, guideline-codified "genetic screening" program specific to LAST.

**Public health/systems interventions:**
- **Simulation-based training programs** (e.g., the 2023 LAST Collaborative) as an institutional-level intervention proven to shorten time-to-treatment.
- **Educational initiatives targeting non-anesthesiologist prescribers/proceduralists** (dentistry, emergency medicine, dermatology/cosmetic surgery, paramedicine) given the documented knowledge gaps and the rising share of LAST events and deaths attributable to lidocaine used by these groups.
- **Standardized maximum-dose labeling/decision-support tools** (e.g., electronic health record dose-calculators/alerts) to reduce the cosmetic-surgery-reported ~10% rate of exceeding maximum recommended tumescent lidocaine doses.

**Prophylaxis:** No pre-procedural prophylactic medication is used to prevent LAST in standard practice; prevention is procedural/behavioral rather than pharmacologic.

---

## 14. Other Species / Natural Disease

LAST is **not a naturally occurring disease entity** documented in veterinary case series or wildlife populations in the way inherited or infectious diseases are catalogued in OMIA; rather, it is an **iatrogenic complication that can occur in any species receiving local anesthetics**, including in veterinary clinical practice (e.g., inadvertent overdose or intravascular injection of lidocaine/bupivacaine in dogs, cats, and horses during regional anesthesia or dental procedures). No taxonomy-specific "natural disease" registry entry (OMIA) was identified for LAST, consistent with its classification as a drug-toxicity syndrome rather than a heritable veterinary disease. Veterinary relevance is chiefly as a **procedural safety consideration** analogous to human practice (weight-based dosing limits, aspiration before injection), rather than as a model of spontaneous animal disease.

**Comparative biology:** The core molecular targets (voltage-gated sodium channels, cardiac Nav1.5, mitochondrial fatty-acid oxidation machinery) are **highly evolutionarily conserved** across mammals, which is precisely why rodent and other mammalian models (see Section 15) are considered informative for human LAST mechanism and lipid-emulsion treatment efficacy.

---

## 15. Model Organisms

**Model types and specific systems:**
- **Rodent (rat, primarily Sprague-Dawley and Wistar) models** are the dominant *in vivo* model system. Examples: a study of 100 male Sprague-Dawley rats randomized to lidocaine, levobupivacaine, or ropivacaine examined lipid emulsion's mitigating effect on LA-induced CNS toxicity ([PMID:26622452](https://pubmed.ncbi.nlm.nih.gov/26622452/)); a Wistar rat model examined **intrathecal** lipid emulsion for total-spinal-block-induced hemodynamic instability.
- **Isolated/perfused rat heart models** have been used to demonstrate the lipid-sink mechanism directly — bupivacaine combines with infused lipid molecules and is cleared more rapidly from isolated hearts under lipid treatment.
- **Xenopus oocyte heterologous expression systems** for cardiac sodium channels (Nav1.5) have been used to characterize the voltage- and use-dependent block by bupivacaine at the single-channel/whole-cell electrophysiology level ([PMID:25008571](https://pubmed.ncbi.nlm.nih.gov/25008571/)).
- **Cell-line models:** SH-SY5Y human neuroblastoma cells for studying LA-induced apoptosis, ROS generation, and mitochondrial dysfunction in a neuronal context ([PMID:42589553](https://pubmed.ncbi.nlm.nih.gov/42589553/)).
- **Isolated mitochondria preparations** (cardiac) for direct study of carnitine-acylcarnitine translocase inhibition and cardiolipin membrane disruption ([PMID:17643405](https://pubmed.ncbi.nlm.nih.gov/17643405/)).

**Induced models:** All LAST animal models are **induced/pharmacological** (drug-treatment models) rather than genetic knockout/transgenic models, since LAST is fundamentally a toxic drug-exposure phenomenon rather than a gene-driven disease. This is a key distinction from most dismech-style Mendelian disease entries.

**Genetic models:** Not a primary modeling approach for LAST itself, though **Scn5a knockout/knock-in mouse models** (developed originally for Brugada syndrome/cardiac conduction disease research) could in principle be used to study genotype-dependent LA cardiotoxicity susceptibility — no specific published study combining an *Scn5a* genetic model with LA-challenge toxicity testing was identified in this search, representing a plausible translational research gap.

**Model characteristics:**
- **Phenotype recapitulation:** Rodent and isolated-heart models reproduce the key electrophysiological (conduction block, arrhythmia) and CNS-excitatory (seizure) phenotypes of human LAST reasonably well, and have been the primary evidence base for lipid-emulsion efficacy — a **meta-analysis of animal LAST models found lipid emulsion reduced mortality odds (OR 0.24, 95% CI 0.1–0.56)** in resuscitative protocols ([PMID:28346007](https://pubmed.ncbi.nlm.nih.gov/28346007/)).
- **Model limitations:** Rodent cardiac electrophysiology (heart rate, ion channel kinetics, and relative Nav/Kv channel density) differs quantitatively from human cardiac physiology, so absolute dose/concentration thresholds for toxicity and lipid-emulsion dosing extrapolated from rodent data require clinical calibration — this is an important, generically acknowledged translational caveat rather than one specifically quantified in the literature reviewed here. Isolated-organ and cell-line models cannot capture the systemic feed-forward effects of acidosis/hypoxia described in Section 6, step 8.

**Applications:** These models have been used to (a) establish and refine the "lipid sink"/"lipid shuttle" mechanistic model of lipid-emulsion rescue, (b) characterize agent-specific cardiotoxic potency differences (bupivacaine > ropivacaine > lidocaine) at the channel and mitochondrial level, and (c) test alternative rescue strategies (e.g., intrathecal lipid emulsion for spinal-anesthesia-associated hemodynamic collapse).

**Resources:** No LAST-specific model-organism database exists; relevant data are distributed across general pharmacology/toxicology literature (PubMed/PMC) rather than a dedicated registry such as MGI, RGD, or ZFIN, reflecting the acute-pharmacologic (rather than developmental-genetic) nature of the condition.

---

## Summary of Key Evidence Gaps (for curation notes)

1. No dedicated OMIM/Orphanet entry exists for LAST; MONDO:0100335 should be independently verified.
2. No population-level denominator data exist for total LA administrations, limiting precise incidence/mortality-rate calculation (explicitly flagged as a limitation in the 2025 BJA editorial).
3. No -omics (transcriptomic/proteomic/metabolomic) profiling of human LAST tissue was identified — mechanistic evidence is drawn from targeted electrophysiology and cell/mitochondria models.
4. No genetic (Scn5a) mouse model study specifically combining channelopathy genotype with LA-challenge toxicity was identified — a plausible research gap.
5. Quality-of-life instrument data specific to LAST survivors were not identified.
6. The exact HPO term IDs suggested in Section 3 are provisional and require confirmation against a current HPO release before use in formal curation.

---

## Sources

- [Local anesthetic systemic toxicity: A comprehensive review for surgeons (2025)](https://journals.lww.com/fjs/fulltext/2025/09000/local_anesthetic_systemic_toxicity__a.1.aspx)
- [International Pain and Spine Intervention Society Emergency Protocols: LAST](https://www.sciencedirect.com/science/article/pii/S2772594426000439)
- [Local anesthetic systemic toxicity induced by penile nerve block: systematic review](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12440524/)
- [APSF: LAST Revisited — A Paradigm in Evolution](https://www.apsf.org/article/local-anesthetic-systemic-toxicity-last-revisited-a-paradigm-in-evolution/)
- [UpToDate: Local anesthetic systemic toxicity](https://www.uptodate.com/contents/local-anesthetic-systemic-toxicity)
- [NYSORA: Local Anesthetic Systemic Toxicity](https://www.nysora.com/topics/complications/local-anesthetic-systemic-toxicity/)
- [PubMed: LAST narrative review for emergency clinicians (PMID:35777259)](https://pubmed.ncbi.nlm.nih.gov/35777259/)
- [StatPearls: Local Anesthetic Toxicity (NBK499964)](https://www.ncbi.nlm.nih.gov/books/NBK499964/)
- [APSF: Checklist for Treating LAST](https://www.apsf.org/article/a-checklist-for-treating-local-anesthetic-systemic-toxicity/)
- [ASRA LAST checklist 2020 version (PMID:33148630)](https://pubmed.ncbi.nlm.nih.gov/33148630/)
- [Third ASRA Practice Advisory on LAST: Executive Summary 2017 (PMID:29356773)](https://pubmed.ncbi.nlm.nih.gov/29356773/)
- [Intravenous lipid emulsion for LAST in pregnant women: scoping review](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10865663/)
- [Successful LAST Management with Intralipid: 2020 ASRA Updates](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12234403/)
- [Lipid emulsion treatment for LAST in pediatric patients: systematic review](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10939516/)
- [LAST in Pregnancy: A Retrospective Cohort Analysis (PMID:39398741)](https://pubmed.ncbi.nlm.nih.gov/39398741/)
- [The state of LAST in 2025: emergence of lidocaine as the next challenge (PMC12674017)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12674017/)
- [Morbidity and mortality from local anesthetics: localized and systemic toxicity](https://pmc.ncbi.nlm.nih.gov/articles/PMC13502390/)
- [Molecular Mechanisms of Local Anesthetic Toxicity (PMID:42589553)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13466980/)
- [Voltage-dependent blockade by bupivacaine of cardiac Nav1.5 (PMID:25008571)](https://pubmed.ncbi.nlm.nih.gov/25008571/)
- [Bupivacaine disrupts cardiolipin-containing liposomes (PMID:17643405)](https://pubmed.ncbi.nlm.nih.gov/17643405/)
- [Anesthetic management of patients with carnitine/FAO defects: narrative review (PMC9282055)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9282055/)
- [A rare loss-of-function SCN5A variant and lidocaine-induced VF (PMID:24445991)](https://pubmed.ncbi.nlm.nih.gov/24445991/)
- [Whole-exome sequencing of a family with local anesthetic resistance (PMID:27243970)](https://pubmed.ncbi.nlm.nih.gov/27243970/)
- [Ultrasound guidance reduces LAST risk (PMID:23788067)](https://pubmed.ncbi.nlm.nih.gov/23788067/)
- [Lipid emulsion improves survival in animal models of LAST: meta-analysis (PMID:28346007)](https://pubmed.ncbi.nlm.nih.gov/28346007/)
- [Direct effect of lipid emulsion treatment on LAST (PMC11700683)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11700683/)
- [LAST-induced cardiac arrest after TEE topicalization, treated with ECPR (PMC6068002)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6068002/)
- [Cardiac Arrest after Small Doses Ropivacaine (PMC9566458)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9566458/)
- [LAST following inadvertent IV levobupivacaine in infants (PMC10221613)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10221613/)
- [LAST in an infant following caudal block (PMC11830499)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11830499/)
- [ICD-10-CM T41.3X1A / T41.3X5A](https://www.icd10data.com/ICD10CM/Codes/S00-T88/T36-T50/T41-/T41.3X1A)
- [EMA Exparel (liposomal bupivacaine) product information](https://www.ema.europa.eu/en/documents/product-information/exparel-liposomal-epar-product-information_en.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 25 |
| Resolved | 25 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 25 |
| On topic | 18 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 33 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.