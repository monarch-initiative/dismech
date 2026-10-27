---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-22T05:02:18.760577'
end_time: '2026-08-22T05:07:23.234924'
duration_seconds: 304.47
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Isolated Growth Hormone Deficiency Type IA
  mondo_id: ''
  category: Endocrine
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
  web_search_requests: 13
  num_turns: 21
  total_cost_usd: 1.3211092
  session_id: 6f8bf895-3ab0-55cb-a154-acb932b43f03
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 27
reference_validation:
  total_references: 23
  verified: 23
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 23
  on_topic: 20
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Isolated Growth Hormone Deficiency Type IA
- **MONDO ID:**  (if available)
- **Category:** Endocrine

## Research Objectives

Please provide a comprehensive research report on **Isolated Growth Hormone Deficiency Type IA** covering all of the
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

# Isolated Growth Hormone Deficiency Type IA (IGHD1A) — Comprehensive Research Report

## 1. Disease Information

**Overview:** Isolated growth hormone deficiency type IA (IGHD1A, also written IGHD IA) is the most severe form of isolated GH deficiency. It is an autosomal recessive disorder caused by biallelic (homozygous or compound heterozygous) loss-of-function variants — most often large deletions — in the *GH1* gene (chromosome 17q23.3), resulting in a complete absence of endogenous pituitary GH. Affected infants have essentially undetectable circulating GH, profoundly low IGF-1, and severe postnatal growth failure beginning in the first months of life. A defining clinical feature is the tendency of these GH-naïve patients to mount neutralizing anti-GH antibodies once exposed to exogenous (including recombinant) GH, which can blunt or abolish the growth response to treatment ([OMIM #262400](https://omim.org/entry/262400); [Wagner et al. 1998, PMID:9432120](https://www.nature.com/articles/pr199816)).

**Key identifiers:**
- **OMIM (phenotype):** #262400 — Isolated Growth Hormone Deficiency, Type IA (IGHD1A)
- **OMIM (gene):** *139250 — Growth Hormone 1 (GH1), also GH-N
- **Orphanet:** ORPHA231662 ([Orphanet](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=en&Expert=231662))
- **MONDO:** MONDO:0009876 (isolated growth hormone deficiency type IA) — reported via [NORD/MONDO](https://rarediseases.org/mondo-disease/isolated-growth-hormone-deficiency-type-ia/) and MalaCards
- **MeSH/ICD:** Falls under the broader "Dwarfism, Pituitary" (MeSH D004396) and ICD-10 E23.0 (Hypopituitarism) categories; there is no IGHD1A-specific ICD-10/11 code — it is coded as a subtype of isolated GH deficiency
- **Gene:** GH1, HGNC:4261, chromosome 17q23.3

**Synonyms:** IGHD1A; Growth Hormone Deficiency, Isolated, Type IA; Pituitary Dwarfism I; Panhypopituitary Dwarfism (historical, imprecise); GH1-related isolated growth hormone deficiency, autosomal recessive severe form.

**Source of information:** This report is derived from aggregated disease-level literature (case series, case reports, and review articles) rather than an individual-patient EHR source. Most detailed phenotypic and molecular data come from single-family or small-cohort case reports (n = 1–10 patients), supplemented by larger prevalence surveys (e.g., Wagner et al. 1998, a cohort study of *GH1* alterations in IGHD).

---

## 2. Etiology

### Disease Causal Factors
IGHD1A is caused exclusively by biallelic **null (complete loss-of-function) mutations in *GH1***, resulting in absence of any functional GH protein. This is a purely genetic (Mendelian) etiology; there is no known environmental or infectious cause of the primary defect itself, though environmental/immunologic factors (rhGH exposure) precipitate the secondary anti-GH antibody complication.

### Genetic Risk Factors
- **Whole/partial gene deletions** of *GH1*: the dominant mechanism. Deletion sizes range from **6.5 kb to 45 kb**, arising from unequal homologous recombination within the 47-kb GH gene cluster (which contains five highly homologous paralogs: *GH1–CSHL1–CSH1–GH2–CSH2*) during meiosis. The **6.7-kb deletion is the most common single lesion, accounting for ~78–80% of GH1-deletion cases** ([Alatzoglou & Dattani 2010, PMID:20852587](https://pmc.ncbi.nlm.nih.gov/articles/PMC3965272/); case report data).
- Novel deletions continue to be described: a 22-kb deletion (chr17:61,973,811–61,996,255) in compound heterozygosity with a splice variant ([BMC Med Genomics 2021, PMID:34470639](https://link.springer.com/article/10.1186/s12920-021-01057-z)); a novel ~1.6-kb deletion spanning exons 1–4 ([Clin Case Rep 2025, PMID:39980897](https://pmc.ncbi.nlm.nih.gov/articles/PMC11839734/)).
- **Point mutations**: homozygous/compound heterozygous nonsense mutations, frameshift (e.g., 371delC found in compound heterozygous siblings), and splice-site mutations (e.g., novel c.10+1G>T in intron 1) also cause IGHD1A when they produce a null allele ([BMC Med Genomics 2021, PMID:34470639](https://link.springer.com/article/10.1186/s12920-021-01057-z)).
- **Consanguinity** is a major risk factor given the autosomal recessive inheritance and the rarity of pathogenic alleles — homozygous large deletions and nonsense variants are disproportionately reported in consanguineous kindreds (analogous to the well-documented consanguineous Pakistani *GHRHR* founder mutation causing the related IGHD type IV, PMID for that family: [PMC10029353](https://pmc.ncbi.nlm.nih.gov/articles/PMC10029353/); IGHD1A shows a parallel pattern in multiple consanguineous case series).
- Molecular epidemiology: in a broad IGHD genetic testing cohort, *GH1* variants accounted for a minority of cases overall (~4.8% in one series dominated by *GHRHR* variants at 39.7%), underscoring that IGHD1A is a rare subtype within an already rare disease category.

### Protective Factors
No specific genetic or environmental protective factors against developing IGHD1A itself have been described (it is a fully penetrant recessive null-allele disorder). With respect to the **secondary anti-GH antibody complication**, some genetic/immunologic modifiers likely exist — antibody development is inconsistent even among patients homozygous for the identical 6.7-kb deletion, implying host immunogenetic factors (e.g., HLA type, degree of residual GH gene product, timing/formulation of rhGH exposure) modulate antibody formation, though these have not been systematically characterized.

### Gene-Environment Interactions
The principal gene-environment interaction in IGHD1A is immunological: because the fetus never encounters GH protein in utero (complete *GH1* loss), the immune system fails to establish central tolerance to GH. Subsequent **environmental exposure to exogenous GH (originally pituitary-extracted GH, now recombinant human GH/rhGH)** is recognized as foreign, triggering an antibody response that can neutralize the therapeutic hormone — a striking example of a loss-of-function genotype creating an antigen-naïve immune state that reshapes response to a specific environmental/therapeutic exposure.

---

## 3. Phenotypes

| Phenotype | Type | Onset/Course | Frequency | Suggested HPO term |
|---|---|---|---|---|
| Severe postnatal growth failure (height SDS < −4.5 by 6 months) | Sign/clinical | Onset in first 6 months of life; progressive if untreated | Nearly universal (defining feature) | HP:0008897 (Postnatal growth retardation) / HP:0004322 (Short stature) |
| Undetectable serum GH | Laboratory abnormality | Present from birth | Universal | HP:0000824 (Growth hormone deficiency) |
| Severely low IGF-1 | Laboratory abnormality | Present from birth/infancy | Universal | HP:0040214 (low IGF1) — best available approximation |
| Frontal bossing / prominent forehead | Physical/facial | Present in infancy | Common (classic "Illig-Prader" facies) | HP:0011220 (Frontal bossing) |
| Depressed/saddle nasal bridge | Physical/facial | Congenital-infancy | Common | HP:0000431 (Wide nasal bridge) / HP:0000431-adjacent |
| Truncal obesity/adiposity | Physical | Childhood onset | Common in untreated patients | HP:0009121 / HP:0001956 (truncal obesity) |
| Neonatal hypoglycemia | Sign | Neonatal | Occasional, more typical of combined pituitary hormone deficiency but reported | HP:0001998 (Hypoglycemia) |
| Micropenis (males) | Sign | Congenital | Occasional | HP:0000054 (Micropenis) |
| Sparse/yellowish hair | Physical | Infancy | Reported in case series | HP:0002286 (Sparse hair) |
| Delayed bone age | Radiographic | Childhood | Common | HP:0002750 (Delayed skeletal maturation) |
| Anti-GH neutralizing antibody formation after rhGH exposure | Immunologic/laboratory | Following treatment initiation | Variable/inconsistent even among identical genotypes | (No specific HPO; immunologic complication) |
| Adult metabolic syndrome (T2DM, dyslipidemia, insulin resistance) | Sign/lab | Adulthood, in undertreated/antibody-blocked patients | Common in long-term follow-up | HP:0000842 (Insulin resistance), HP:0003074 (Hyperglycemia) |
| Osteoporosis/low bone mineral density | Sign | Adulthood | Common | HP:0000939 (Osteoporosis) |
| Reduced adult final height (extreme short stature) | Sign | Persistent | Universal without effective treatment | HP:0004322 (Short stature) |
| Pituitary/skull-base morphologic abnormalities (platybasia, short clivus, small posterior fossa, sellar arachnoidocele) | Radiographic | Adulthood (reported) | Reported in longstanding untreated/undertreated adults | HP:0002676 (Platybasia) |
| Reduced quality of life / asthenia | Functional | Adulthood | Documented via QoL-AGHDA scoring | HP:0025406 (or general fatigue term HP:0012378) |

**Severity/progression:** The phenotype is present from birth (biochemically) and clinically evident by 6 months of age with a severity that, untreated, leads to extreme adult short stature (final heights reported around 120–130 cm, SDS as low as −8.5) ([EDM Case Reports 2014, PMID:24683479](https://pmc.ncbi.nlm.nih.gov/articles/PMC3965272/)). The disease course is chronic and lifelong; without effective treatment (or if antibody-mediated resistance develops), growth failure and downstream metabolic/skeletal/cardiovascular sequelae progress into adulthood.

**Quality of life impact:** Adult IGHD1A patients who develop antibody-mediated treatment failure show reduced quality of life, documented using the AGHDA (Assessment of Growth Hormone Deficiency in Adults) questionnaire (QoL-AGHDA score 18/25 in one reported case), alongside musculoskeletal pain and asthenia ([PMID:24683479](https://pmc.ncbi.nlm.nih.gov/articles/PMC3965272/)).

---

## 4. Genetic/Molecular Information

**Causal gene:** GH1 (HGNC:4261; OMIM *139250), located at chromosome 17q23.3, within the 47-kb GH gene cluster.

**Gene cluster architecture:** The human GH locus contains **five tandemly arrayed, highly homologous (90–95% coding-sequence identity) paralogous genes** in the order 5′–*GH1*–*CSHL1*–*CSH1*–*GH2*–*CSH2*–3′, each with 5 exons/4 introns at conserved positions. Only *GH1* is expressed in the pituitary somatotroph; the other four (*CSHL1*, *CSH1*, *GH2*, *CSH2* — chorionic somatomammotropin/placental lactogen genes) are placentally expressed. Pituitary-restricted *GH1* expression is governed by a **distal locus control region (LCR)** located ~14.5 kb upstream of the *GH1* promoter (DNase I hypersensitive site I, HSI), which acts as a long-range enhancer required for somatotroph-specific chromatin activation.

**Pathogenic variant spectrum:**
- **Large gene deletions** (6.5–45 kb) generated by unequal homologous recombination between the paralogous cluster members during meiosis — the single most common mechanism, with the **6.7-kb deletion representing ~78–80% of cases**.
- Novel large deletions continue to be reported: 22-kb deletion (chr17:61,973,811–61,996,255); ~1.6-kb deletion spanning exons 1–4; and the earliest described "double deletion" in the GH gene cluster ([Igarashi et al., PMID:3005356](https://pubmed.ncbi.nlm.nih.gov/3005356/)).
- **Frameshift mutations**, e.g., 1-bp deletion 371delC, reported in compound heterozygous siblings.
- **Nonsense mutations**, homozygous, producing a premature stop codon and null allele.
- **Splice-site mutations**, e.g., the novel c.10+1G>T donor-site variant in intron 1, abolishing normal splicing.

**Variant classification/pathogenicity:** Variants are classified per ACMG/AMP criteria; reported IGHD1A-causing alleles are classified pathogenic based on null-variant type (nonsense, frameshift, canonical splice-site, whole/partial gene deletion), low/absent population frequency in gnomAD, and segregation with the phenotype in affected pedigrees.

**Allele frequency:** Individual pathogenic *GH1* deletion/point-mutation alleles are extremely rare in population databases (gnomAD), consistent with a rare recessive disorder; no single allele reaches carrier frequencies notable at the population level except within specific consanguineous or geographically isolated kindreds where founder effects have been documented for other IGHD genes (e.g., the *GHRHR* p.Glu72* founder mutation in a consanguineous Pakistani family causing the related IGHD type IV; PMC10029353).

**Somatic vs. germline:** IGHD1A variants are constitutional/germline; there is no somatic mosaicism literature specific to this condition.

**Functional consequence:** All IGHD1A-causing variants are **loss-of-function (null)** — either complete absence of the gene (deletion) or absence of any functional protein product (nonsense/frameshift/splice-disrupting). This is mechanistically distinct from the autosomal dominant IGHD type II, which arises from **dominant-negative** *GH1* splice-site mutations causing exon 3 skipping and production of a 17.5-kDa mutant GH isoform that impairs secretion of wild-type GH from heterozygous somatotrophs.

**Modifier genes:** No specific modifier genes for IGHD1A severity have been validated; the marked inter-individual variability in anti-GH antibody development among patients homozygous for the identical 6.7-kb deletion strongly suggests unidentified immunogenetic modifiers (e.g., HLA haplotype), but this has not been resolved in the literature.

**Epigenetic information:** The *GH1* locus is a model system for chromatin-based, cell-type-restricted gene regulation. Studies of the hGH LCR (HSI) show that loss of LCR activity causes a "relaxation" of pituitary somatotroph cell-type specificity, permitting aberrant *GH1* expression in other Pit-1-lineage pituitary cells; SMCHD1 has also been identified as an epigenetic regulator of this autosomal gene cluster. These mechanisms govern normal *GH1* tissue-specificity but are not themselves reported as a cause of IGHD1A (which is driven by coding/structural null mutations, not epimutation).

**Chromosomal abnormalities:** IGHD1A is caused by focal (kb-scale) deletions within the *GH1* locus rather than large chromosomal rearrangements; no aneuploidy or translocation etiology is reported.

**Suggested annotations:** Gene — HGNC:4261 (GH1); Molecular function — GO:0005179 (hormone activity); Biological process — GO:0060396 (growth hormone receptor signaling pathway), GO:0060123 (regulation of growth hormone secretion).

---

## 5. Environmental Information

There are no established primary environmental, toxic, occupational, or infectious causal factors for IGHD1A — it is a monogenic Mendelian disorder. The single well-characterized environmental interaction is **iatrogenic**: exposure to exogenous GH protein (historically cadaveric pituitary-extracted GH, now recombinant human GH) is the trigger for anti-GH antibody formation in a subset of patients (see Etiology, Gene-Environment Interactions above, and Mechanism section below). No lifestyle factors (diet, smoking, alcohol) are known to influence disease onset; secondary lifestyle-modifiable risk factors (diet, physical activity) become relevant later for managing the metabolic complications of long-standing untreated/undertreated GH deficiency (obesity, dyslipidemia, insulin resistance).

---

## 6. Mechanism / Pathophysiology

**Causal chain (initial trigger → clinical manifestation):**

1. **Molecular lesion**: Biallelic null *GH1* variant (deletion, nonsense, frameshift, or splice-disrupting mutation) → complete absence of functional GH-N transcript/protein in pituitary somatotrophs.
2. **Somatotroph/pituitary level**: Absent GH synthesis and secretion despite (in most cases) anatomically present somatotroph cells and intact hypothalamic-pituitary signaling upstream (GHRH, GHRHR, Pit-1/POU1F1 pathway are normal in IGHD1A, distinguishing it from combined pituitary hormone deficiencies).
3. **Endocrine/systemic level**: Undetectable circulating GH → failure of hepatic and peripheral IGF-1 generation (GH receptor signaling has no ligand to act on) → profoundly low serum IGF-1 and IGFBP-3.
4. **Growth plate/skeletal level**: Loss of GH/IGF-1-driven chondrocyte proliferation and longitudinal bone growth at the epiphyseal growth plate → severe postnatal growth failure, delayed bone age.
5. **Metabolic level**: Loss of GH's lipolytic, anti-insulin, and protein-anabolic actions → predisposition to central adiposity, insulin resistance, dyslipidemia, and (in adulthood) type 2 diabetes if under-treated.
6. **Immunologic branch (the antibody complication)**: Because the fetus/infant is never exposed to any GH protein during development (complete absence of self-antigen), central immune tolerance to GH is never established. Upon **first therapeutic exposure to exogenous rhGH**, the immune system recognizes GH as a foreign antigen → B-cell/antibody response → production of **neutralizing anti-GH antibodies** that bind circulating GH and block its coupling to the GH receptor → loss of biological GH signal transduction despite adequate/escalated rhGH dosing → attenuated or abolished IGF-1 generation and growth response, functionally mimicking Laron syndrome (GH receptor defect) even though the receptor itself is structurally normal. Antibody titers can rise dramatically with treatment re-challenge (e.g., from ~101 U/mL at baseline to >200 U/mL after 3 months of rhGH in one adult case), and this blockade is not always overcome by dose escalation up to 1 mg/day ([PMID:24683479](https://pmc.ncbi.nlm.nih.gov/articles/PMC3965272/)).
7. **Bone/cardiometabolic/pituitary-remodeling sequelae (chronic, adult-onset)**: Sustained severe GH/IGF-1 deficiency (either untreated or antibody-blocked) drives osteoporosis (low BMD at lumbar spine/femoral neck), atherosclerotic cardiovascular disease (carotid plaques, elevated Lp(a)), insulin resistance/T2DM, vitamin D deficiency with secondary hyperparathyroidism, and structural skull-base/pituitary remodeling (platybasia, short clivus, small posterior fossa, sellar arachnoidocele) reported in long-term adult follow-up.
8. **Mortality**: Longitudinal outcome data (Besson et al. 2003, PMID:12915652) document markedly reduced survival in IGHD1A patients compared with population controls (**56 vs. 75 years for men; 46 vs. 80 years for women**), with excess deaths attributable predominantly to cardiovascular disease and infection rather than malignancy.

**Upstream vs. downstream:** The *GH1* null mutation is the sole upstream initiating lesion. All phenotypic branches (growth failure, metabolic, skeletal, cardiovascular, and the antibody-mediated treatment-resistance branch) are downstream consequences, with the antibody branch being conditionally activated only upon therapeutic GH exposure (an environmentally triggered, immune-mediated downstream node distinct from — and superimposed upon — the primary endocrine deficiency).

**Cell types/biological processes involved:**
- Pituitary somatotroph cells (CL:0000428) — site of the primary defect (absent hormone synthesis, not necessarily absent cell number)
- Hepatocytes and peripheral GH-target cells — site of failed IGF-1 generation
- Growth plate chondrocytes — site of failed longitudinal growth
- B lymphocytes/plasma cells — site of anti-GH antibody production
- Adipocytes, pancreatic β-cells, vascular endothelium — sites of metabolic/cardiovascular sequelae in chronic disease

**Suggested GO terms:** GO:0060396 (growth hormone receptor signaling pathway, negatively affected), GO:0060123 (regulation of growth hormone secretion), GO:0008283 (cell population proliferation, reduced in growth plate), GO:0006955 (immune response, for the antibody branch).
**Suggested CL terms:** CL:0000428 (somatotroph), CL:0000138 (chondrocyte), CL:0000542 (lymphocyte/B cell for antibody production).

**Molecular profiling / omics:** IGHD1A is not a disease typically characterized by transcriptomic/proteomic/metabolomic profiling in the literature reviewed; molecular characterization is dominated by targeted *GH1* gene sequencing/deletion mapping (Sanger sequencing, MLPA, and increasingly NGS/exome sequencing for deletion breakpoint characterization) rather than omics-scale studies. No single-cell or spatial transcriptomic studies specific to IGHD1A pituitary tissue were identified.

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Anterior pituitary gland (somatotroph population) — UBERON:0000007 (pituitary gland); Endocrine system — UBERON:0001048 (primary organ system affected)
- **Secondary/downstream target organs:** Skeletal system (long bones, growth plates) — UBERON:0002481 (bone tissue), UBERON:0002050 (growth plate cartilage); Liver (hepatic IGF-1 production) — UBERON:0002107; Adipose tissue — UBERON:0001013; Cardiovascular system (carotid arteries, in chronic disease) — UBERON:0001981; Skull base — UBERON:0035632 (basicranium), in the adult platybasia/short clivus phenotype

**Body systems involved:** Endocrine system (primary), skeletal system, cardiovascular system, metabolic/nutritional system, and (secondarily, via the antibody response) the immune system.

**Tissue/cell level:**
- Somatotroph cells of the anterior pituitary (CL:0000428) — site of absent GH synthesis
- Chondrocytes of the epiphyseal growth plate (CL:0000138) — downstream growth failure
- Hepatocytes (CL:0000182) — site of failed IGF-1 synthesis
- B lymphocytes (CL:0000236) — anti-GH antibody-producing plasma cells

**Subcellular level:** GO Cellular Component — secretory granules of somatotrophs (GO:0030141, secretory granule) where GH is normally packaged; endoplasmic reticulum of somatotrophs (site of failed/absent GH protein synthesis when a null allele is transcribed but not translated, in the rare cases of unstable transcript rather than full deletion).

**Localization:** The pituitary defect is centrally located within the sella turcica; in chronic, longstanding/severe adult disease, structural changes have been reported in the **posterior cranial fossa and clivus** (platybasia, short clivus, small posterior fossa, pituitary/sellar arachnoidocele) — likely secondary developmental consequences of chronic severe GH deficiency on skull-base growth rather than a primary structural malformation. No laterality/asymmetry is relevant, as this is a systemic endocrine disorder.

---

## 8. Temporal Development

**Onset:** Biochemically present from birth (GH deficiency is congenital), but clinically apparent growth failure typically manifests within the **first 6 months of life**, with the diagnostic threshold commonly cited as height SD score < −4.5 by 6 months of age. Some case series report normal birth length/weight followed by a rapid decline in growth velocity over the first 6–9 months (e.g., a reported patient: 49 cm at birth → 61 cm, SDS −7.24, by 21 months, having crossed to −5.14 SD by 9 months) ([PMID:34470639](https://link.springer.com/article/10.1186/s12920-021-01057-z)). Onset pattern is **insidious but rapidly progressive** in infancy rather than acute.

**Progression:**
- Untreated, growth failure is progressive and severe throughout childhood, culminating in extreme adult short stature (reported adult heights as low as 120–130 cm; SDS to −8.5).
- Disease course is **chronic and lifelong**, not self-limited; it does not remit spontaneously.
- A distinctive "staged" pattern occurs in a subset of patients: an initial period of good growth response to rhGH treatment, followed by **secondary treatment failure** upon development of neutralizing anti-GH antibodies — effectively converting a treatable condition into a refractory one at an unpredictable later time point.
- In adulthood, if the disease remains under-treated or becomes antibody-refractory, a second "progression phase" unfolds over decades: accumulating metabolic (diabetes, dyslipidemia), skeletal (osteoporosis), and cardiovascular (atherosclerosis) complications, with documented structural pituitary/skull-base changes on serial imaging.

**Patterns:**
- No spontaneous remission is described.
- **Critical treatment window:** early diagnosis and rhGH initiation in infancy/early childhood is critical to maximize catch-up growth and final adult height before the growth plates fuse and before antibody-mediated resistance (if it develops) forecloses the therapeutic window.
- Antibody development itself does not follow a fixed timeline — it has been documented to persist at measurable (if low) titers for **over 50 years** after initial GH exposure and to surge dramatically upon treatment re-challenge in adulthood ([PMID:24683479](https://pmc.ncbi.nlm.nih.gov/articles/PMC3965272/)).

---

## 9. Inheritance and Population

**Epidemiology:**
- Isolated GH deficiency (all types combined) has an estimated incidence of **1 in 4,000 to 1 in 10,000 live births**.
- Familial (genetic) cases constitute an estimated **3–30%** of all IGHD cases; the remainder are sporadic/idiopathic.
- Within genetically solved IGHD cohorts, *GH1*-related disease (types IA, IB, and II combined) represents a minority of cases relative to *GHRHR*-related disease (one cohort: *GHRHR* 39.7% vs. *GH1* 4.8% of genetically characterized cases), and IGHD1A specifically is the rarest and most severe subtype within the *GH1*-related group.
- No population-specific incidence figures for IGHD1A alone (as distinct from the broader IGHD category) were identified in the literature surveyed; it should be considered an ultra-rare disease.

**Inheritance pattern:** **Autosomal recessive.** Both parents are obligate heterozygous carriers (typically asymptomatic, given monoallelic *GH1* function is sufficient for normal GH production), and affected individuals carry homozygous or compound heterozygous null variants.

**Penetrance:** Complete/full penetrance for the core biochemical and growth phenotype in individuals biallelic for null *GH1* variants (this is a classic "simple" recessive Mendelian trait for the primary hormone-deficiency phenotype).

**Expressivity:** **Variable**, particularly with respect to the anti-GH antibody complication — patients homozygous for the *identical* 6.7-kb deletion show inconsistent antibody development and inconsistent growth response even when antibodies are present, indicating variable expressivity governed by unidentified host factors.

**Genetic anticipation:** Not applicable/not described (IGHD1A is not a repeat-expansion disorder).

**Germline mosaicism:** Not specifically documented for *GH1* in the literature reviewed, though it is a theoretical possibility relevant to recurrence-risk counseling in families with an isolated de novo-appearing case.

**Founder effects:** While a well-documented *GHRHR* founder mutation (p.Glu72*) causes the related IGHD type IV in a consanguineous Pakistani population, an analogous population-specific *GH1* founder allele for IGHD1A specifically was not identified in the sources reviewed here, though multiple case reports describe homozygous *GH1* deletions/mutations arising in consanguineous kindreds from various populations (consistent with local founder effects at the family level rather than broad population-level founder alleles).

**Consanguinity:** Plays a substantial role given the rarity of pathogenic alleles and the recessive inheritance; numerous published IGHD1A pedigrees are consanguineous.

**Carrier frequency:** Not established at a population level (individual pathogenic alleles are rare in gnomAD/1000 Genomes-scale databases); carrier frequency would be expected to be markedly elevated in consanguineous or geographically isolated populations with a documented founder allele, though no specific figure was found for IGHD1A.

**Population demographics:** No specific ethnic or geographic predilection is firmly established for IGHD1A broadly (case reports span East Asian, South Asian, European, and other populations), though consanguineous/endogamous communities are over-represented in the literature due to the recessive inheritance mechanism. Sex ratio is expected to be approximately equal (autosomal, not X-linked, inheritance) — in contrast to IGHD type III, which is X-linked (BTK-associated) and thus male-predominant.

---

## 10. Diagnostics

**Clinical/laboratory tests:**
- **Serum GH:** undetectable or extremely low, both randomly and after provocative testing, is the biochemical hallmark. Because GH secretion is pulsatile, a single random GH level is not diagnostic; **provocative (stimulation) testing** is required.
- **GH stimulation tests:** The insulin tolerance test (ITT) remains the historical "gold standard" (peak GH cutoff typically 3–5 μg/L in adults; pediatric cutoffs vary by assay/guideline), but carries hypoglycemia risk. Alternative provocative tests in routine pediatric use include the **GHRH-arginine test**, **glucagon stimulation test**, **clonidine stimulation test**, and **arginine test**; current guidance generally requires **two abnormal provocative tests** (or one plus strongly supportive clinical/auxological/imaging findings) for a pediatric GHD diagnosis. In IGHD1A specifically, GH is essentially undetectable across all provocative tests given the complete absence of the GH1 gene product.
- **IGF-1 and IGFBP-3:** Both are markedly low in IGHD1A but are individually **poor stand-alone screening tests** — IGF-1 is unreliable in infancy/early childhood (<5 years) due to physiologic low levels and nutritional confounding, while IGFBP-3 is comparatively more robust in young children as it is less affected by nutritional status. Low IGF-1/IGFBP-3 supports but does not confirm the diagnosis; combined with undetectable stimulated GH and molecular confirmation, the diagnosis is secured.
- **Bone age radiograph:** typically delayed relative to chronological age.
- **Pituitary MRI:** used to exclude structural/anatomic pituitary abnormalities and combined pituitary hormone deficiency (CPHD) causes; in IGHD1A the pituitary is typically anatomically unremarkable in childhood (distinguishing it from CPHD syndromes with ectopic posterior pituitary, pituitary stalk interruption, etc.), though chronic long-standing adult disease has been associated with secondary skull-base/sellar structural changes (see Mechanism section).

**Genetic testing:**
- **Targeted GH1 sequencing** (Sanger or NGS-based) combined with **deletion/duplication analysis** (MLPA, targeted CGH array, or breakpoint-spanning PCR/NGS) is the recommended approach, since a large proportion of pathogenic alleles are deletions not detectable by sequencing alone.
- **Gene panels** for isolated/combined GH deficiency typically include *GH1*, *GHRHR*, *POU1F1*, *PROP1*, *HESX1*, *LHX3/4*, *SOX2/3*, *BTK* (for IGHD III), and others relevant to the differential diagnosis.
- **Whole exome/genome sequencing** is increasingly used when panel testing is negative or when a novel/complex structural variant (e.g., atypical deletion breakpoints) is suspected, as illustrated by recent case reports characterizing novel 22-kb and ~1.6-kb *GH1* deletions.
- **Anti-GH antibody testing** is not part of the diagnostic workup for GHD itself but becomes clinically relevant during treatment monitoring if a patient shows unexpected loss of growth response to rhGH; however, its clinical utility/interpretation remains debated and it is **not routinely recommended** for screening given inconsistent correlation between antibody titers and clinical resistance.

**Differential diagnosis (key GH1-related and other isolated GHD subtypes):**

| IGHD subtype | Gene | Inheritance | GH level | Key distinguishing feature |
|---|---|---|---|---|
| **IA** | GH1 (null) | AR | Undetectable | Most severe; antibody formation to rhGH |
| IB | GH1 (partial LOF) or GHRHR | AR | Low but detectable | Milder, more variable than IA; better/sustained rhGH response |
| II | GH1 (dominant-negative, exon 3 skipping) | AD | Variable, may not be markedly low | Dominant negative 17.5-kDa GH isoform |
| III | BTK (Xq22.1) | X-linked | Low | Associated with agammaglobulinemia/hypogammaglobulinemia |
| IV | GHRHR | AR | Undetectable/low | GHRH receptor defect (e.g., Pakistani founder mutation) |

Broader differentials include combined pituitary hormone deficiency (CPHD; *POU1F1*, *PROP1*, *HESX1*, *LHX3/4*), Laron syndrome (GH receptor defect, elevated GH with low IGF-1 — biochemically distinguishable from IGHD1A's undetectable GH), and idiopathic/acquired GHD (tumor, trauma, radiation).

**Screening:** No population-based newborn screening exists for IGHD1A; diagnosis relies on clinical recognition of postnatal growth failure triggering endocrine and, subsequently, molecular workup. In known-affected families, cascade genetic testing of at-risk siblings/relatives is appropriate given the recessive inheritance.

---

## 11. Outcome/Prognosis

**Survival and mortality:** The best available longitudinal data (Besson et al. 2003, PMID:12915652, cited via [PMID:24683479](https://pmc.ncbi.nlm.nih.gov/articles/PMC3965272/)) document markedly reduced life expectancy in IGHD1A patients compared to the general population: **reported survival of 56 years (men) and 46 years (women) versus 75 and 80 years, respectively, in controls.** Excess mortality was attributed primarily to **cardiovascular disease and infections**, not malignancy.

**Morbidity/functional outcomes:**
- Without effective, sustained GH (or alternative IGF-1) replacement, patients face lifelong extreme short stature (final adult heights as low as ~120 cm).
- Long-term untreated/antibody-refractory adults accumulate a constellation of morbidities: **type 2 diabetes, dyslipidemia (elevated LDL, low HDL, elevated Lp(a)), insulin resistance, central adiposity, osteoporosis (T-scores in the −2.7 to −3.1 range at spine/femoral neck), vitamin D deficiency with secondary hyperparathyroidism, and atherosclerotic disease (documented carotid plaques).**
- Structural CNS/skull-base findings (platybasia, short clivus, small posterior fossa, sellar arachnoidocele) have been documented on serial imaging in longstanding adult disease.
- **Quality of life** is measurably reduced in adults with treatment-refractory disease (QoL-AGHDA score 18/25 in a reported case), with prominent musculoskeletal pain and asthenia.

**Recovery potential:** With **early diagnosis and prompt, uninterrupted rhGH replacement** (before antibody-mediated resistance develops, if it does at all), growth outcomes can be favorable — some patients achieve good catch-up growth and near-normal stature. However, prognosis is substantially worse in patients who develop high-titer neutralizing anti-GH antibodies, for whom conventional rhGH dose escalation may fail to restore IGF-1 generation or growth velocity, and for whom no FDA/EMA-licensed rescue therapy (e.g., recombinant IGF-1) currently exists for this specific indication in most jurisdictions.

**Prognostic factors:** Timing of diagnosis and treatment initiation (earlier = better height outcome); whether/when neutralizing anti-GH antibodies develop; antibody titer and neutralizing capacity; degree of adherence to and duration of GH replacement; and, in adulthood, aggressiveness of management of the secondary cardiometabolic and skeletal complications.

**Prognostic biomarkers:** Anti-GH antibody titer (though its correlation with clinical resistance is inconsistent and testing is not routinely recommended) and serial IGF-1 response to treatment are the main biomarkers used to gauge ongoing treatment efficacy.

---

## 12. Treatment

**Pharmacotherapy — first-line:**
- **Recombinant human growth hormone (rhGH, somatropin)** is the standard of care and, in antibody-naïve patients, is typically highly effective, producing significant catch-up growth. NCIT term: NCIT:C1723 (Somatropin) under NCIT:C15986 (Pharmacotherapy).
- Historically, patients were treated with **pituitary-extracted human GH**, which was more immunogenic than current recombinant preparations; even modern, "least immunogenic" rhGH formulations can still provoke antibody formation specifically in IGHD1A patients due to their complete absence of prior self-antigen exposure.

**Managing anti-GH antibody-mediated treatment resistance:**
- Dose escalation of rhGH (e.g., from 0.2 mg/day up to 1 mg/day in a reported adult case) may be attempted but can **fail to overcome high-titer neutralizing antibody blockade**, with IGF-1 remaining undetectable despite escalation ([PMID:24683479](https://pmc.ncbi.nlm.nih.gov/articles/PMC3965272/)).
- **Recombinant human IGF-1 (rhIGF-1, mecasermin)** is a theoretically attractive alternative because it bypasses the GH-receptor-antibody blockade entirely, acting downstream. However, it is **not licensed for adult GHD** in most jurisdictions, and pediatric experience shows variable growth response with adverse metabolic effects on lipids/BMI, limiting its use as a routine rescue strategy. NCIT/CHEBI: mecasermin, CHEBI:64252 (an rhIGF-1 preparation).
- Switching GH formulations/reducing immunogenicity is a theoretical strategy but has not been shown to reliably overcome established high-titer neutralizing antibodies.

**Supportive/multifactorial management of adult complications** (illustrated by the reported case, [PMID:24683479](https://pmc.ncbi.nlm.nih.gov/articles/PMC3965272/)):
- **Metformin** for type 2 diabetes/insulin resistance (NCIT:C61612)
- **Statin therapy** for dyslipidemia (NCIT:C29727, HMG-CoA reductase inhibitor class)
- **Calcium and vitamin D3 supplementation** for secondary hyperparathyroidism/bone health (NCIT:C947 area / dietary supplementation)
- **Aspirin** for cardiovascular risk reduction (NCIT:C287)
- **Bisphosphonate therapy** for osteoporosis (declined by the reported patient but a standard consideration)
- After 1 year of multifactorial management in the reported case: HbA1c improved from 6.8% to 6.6%, LDL fell from 182 to 98 mg/dL, and lumbar spine/femoral neck BMD improved by 7.3%/1.9%, respectively — demonstrating that even when GH/IGF-1 axis restoration is not achievable, targeted management of downstream comorbidities meaningfully improves outcomes.

**Surgical/procedural, gene, cell, and RNA-based therapies:** No surgical intervention is directed at the primary GH deficiency. No gene therapy, cell therapy, or RNA-based (ASO/siRNA/mRNA) therapeutics specific to IGHD1A were identified as approved or in advanced clinical development in the literature reviewed; given the "simple" loss-of-function, monogenic, secreted-protein-replaceable nature of the disorder, IGHD1A is in principle well-suited to future gene-replacement or gene-editing approaches, but no such programs were found in this search.

**Experimental/investigational:** Long-acting weekly/monthly rhGH formulations (e.g., somatrogon, lonapegsomatropin) are approved/in development for general pediatric GHD and could theoretically apply to antibody-naïve IGHD1A patients, though no IGHD1A-specific trial data were identified; a broader GHD pediatric trial (e.g., MOD-4023/somatrogon Phase 3, NCT03874013) is illustrative of the class but not disease-specific.

**Treatment monitoring/outcomes:** Growth velocity, height SDS, IGF-1 normalization, and (when clinically indicated) anti-GH antibody titers are used to monitor treatment response; adverse events of rhGH itself are generally mild (injection site reactions, rare intracranial hypertension, glucose intolerance at high doses) but are compounded in IGHD1A by the antibody-mediated efficacy failure specific to this subtype.

**Treatment algorithm summary:** (1) Confirm diagnosis biochemically and molecularly → (2) initiate rhGH promptly in childhood, ideally before growth plate fusion → (3) monitor growth response and IGF-1; if response is inadequate despite adequate dosing/adherence, consider anti-GH antibody testing → (4) if high-titer neutralizing antibodies are confirmed and blocking response, consider dose escalation (often insufficient) or off-label rhIGF-1 (limited evidence, not licensed for this indication in adults) → (5) transition to adult GHD management with attention to metabolic, skeletal, and cardiovascular surveillance and multifactorial pharmacotherapy for comorbidities regardless of GH-axis treatment success.

---

## 13. Prevention

**Primary prevention:** As a monogenic recessive disorder, there is no behavioral/environmental primary prevention of the underlying genetic defect. The principal prevention lever is **genetic counseling and reproductive planning** in families with a known pathogenic *GH1* allele (carrier testing of relatives, discussion of recurrence risk of 25% for future pregnancies of carrier-carrier couples, and options including prenatal diagnosis or preimplantation genetic testing where desired and available).

**Secondary prevention (early detection):** There is no population-based newborn screening program specific to IGHD1A. Early clinical recognition of severe postnatal growth failure (crossing growth percentiles in the first 6 months of life) is the practical secondary-prevention lever, prompting endocrine referral, biochemical confirmation, and prompt treatment initiation to minimize the duration of untreated GH/IGF-1 deficiency and maximize the window for effective rhGH-driven catch-up growth before growth plate fusion.

**Tertiary prevention:** Once the diagnosis is established (and particularly in patients who develop antibody-mediated treatment resistance), tertiary prevention focuses on averting the long-term cardiometabolic and skeletal complications of chronic GH/IGF-1 deficiency: routine screening for diabetes/dyslipidemia, bone density (DEXA) monitoring, cardiovascular risk assessment, and periodic reassessment of pituitary function/imaging, as recommended based on the adult outcome literature cited above.

**Genetic counseling:** Central to prevention in this disorder — affected families should receive counseling on autosomal recessive inheritance, carrier risk to unaffected siblings, recurrence risk, and (where the family's specific pathogenic variant is known) the availability of targeted carrier or prenatal testing.

**Public health/environmental interventions:** Not applicable, as there is no environmental/infectious causal contributor to the primary disease.

**Prophylaxis:** No prophylactic pharmacologic intervention exists to prevent either the genetic defect or (reliably) the secondary anti-GH antibody response; some clinicians consider using the least immunogenic modern rhGH formulation available at treatment initiation as a pragmatic (though not proven) measure to minimize antibody risk, but this is not a formally validated prophylactic strategy in the literature reviewed.

---

## 14. Other Species / Natural Disease

**Taxonomy:** No naturally occurring animal disease directly analogous to human IGHD1A (biallelic *GH1* null mutation) was identified as a well-characterized spontaneous veterinary condition in this search. Canine and other companion-animal pituitary dwarfism syndromes are recognized clinically (e.g., German Shepherd combined pituitary hormone deficiency from *LHX3* mutations), but these represent combined pituitary hormone deficiency rather than an isolated *GH1*-null phenotype, and are mechanistically and genetically distinct from IGHD1A.

**Gene:** Mouse *Gh1* (ortholog of human *GH1*) — MGI database; rat *Gh1* — RGD database. Cross-species conservation of the GH/IGF-1 axis is very high across mammals, supporting the general translational relevance of rodent models even though a direct *Gh1*-null natural-disease correlate was not found.

**Comparative biology:** The GH/IGF-1 signaling axis (GHRH → pituitary somatotroph GH release → hepatic/peripheral IGF-1 generation → growth plate chondrocyte proliferation) is evolutionarily well conserved across vertebrates, supporting strong translational validity of the mouse models described below, even though the specific *GH1*-null genetic lesion of IGHD1A has not been reported as a naturally occurring disease in another species.

**Zoonotic potential/transmission:** Not applicable — this is a non-communicable, non-infectious monogenic endocrine disorder.

---

## 15. Model Organisms

**Model types available:**
- **Mammalian rodent (mouse) genetic models** are the dominant experimental system for the GH/IGF-1 axis, though most well-characterized existing models target upstream regulators (*Ghrhr*, *Ghrh*) rather than *Gh1* itself directly:
  - **GHRH-knockout mouse** (targeted ablation of the *Ghrh* gene) — created by Alba & Salvatori (2004) as a model of isolated GH deficiency arising from loss of the hypothalamic stimulus for pituitary GH synthesis/secretion; recapitulates severe dwarfism and low IGF-1, analogous in downstream phenotype to *GH1*-null IGHD1A even though the lesion is upstream (hypothalamic) rather than at the *Gh1* gene itself.
  - **"Little" (*lit*) mouse** — a naturally occurring/spontaneous *Ghrhr* loss-of-function mutant, a classic model of isolated GH deficiency via GHRH-receptor failure (mechanistically analogous to human IGHD type IV rather than IA).
  - **Heterozygous *Gh* exon-3-deletion mice** — a more direct *Gh1*-proximal model, reported to show growth retardation attributed to reduced *Ghrhr* mRNA expression, illustrating feedback interplay between GH and its own upstream regulatory receptor.
  - Comprehensive reviews of "mouse models of growth hormone deficiency" (e.g., Springer, *Reviews in Endocrine and Metabolic Disorders* 2020; and "Common and Uncommon Mouse Models of Growth Hormone Deficiency," PMC12102728) catalog the full landscape of GHD mouse lines, spanning nearly a century of research, though a direct biallelic *Gh1*-null mouse precisely modeling human IGHD1A (as opposed to *Ghrh*/*Ghrhr* pathway models) was not specifically identified as a named, widely used line in this search.

**Genetic model types:** Targeted knockout (*Ghrh*-KO), spontaneous/induced point mutation (*lit* mouse *Ghrhr*), and targeted exon deletion (heterozygous *Gh* exon 3 deletion) are all represented; a fully humanized or conditional *Gh1*-null model specific to IGHD1A was not identified.

**Phenotype recapitulation:** These models recapitulate the core downstream phenotype of IGHD1A — severe postnatal dwarfism and low IGF-1 — with good fidelity, since they converge on the same final common pathway (absent/deficient pituitary GH output). However, they generally act **upstream** of the *GH1* gene itself (via GHRH/GHRHR pathway disruption) rather than directly modeling a *GH1*-null lesion, and — critically — **rodent models cannot recapitulate the human anti-GH antibody complication**, since that phenomenon depends on human-specific immunological tolerance dynamics to a therapeutically administered human recombinant protein; this is a key **translational limitation** for using these models to study IGHD1A's most clinically distinctive complication.

**Applications:** Mouse GHD models have been used extensively to study the GH/IGF-1 axis's role in growth, metabolism, and (notably) **aging/longevity** — GHRH-knockout and related severe-GHD mouse lines are long-lived compared to wild-type controls, a striking contrast to the **reduced human lifespan** documented in IGHD1A patients (Besson et al., PMID:12915652), highlighting an important species-specific divergence in the long-term systemic consequences of lifelong GH deficiency (this is a notable model-to-human translational caveat worth flagging explicitly for any pathophysiology model incorporating these animal data).

**Resources/databases:** MGI (Mouse Genome Informatics) for *Gh1*/*Ghrh*/*Ghrhr* alleles; IMPC/KOMP for systematic knockout phenotyping data; RGD for rat orthologs.

---

## Summary of Key Ontology Term Suggestions

| Category | Suggested term(s) |
|---|---|
| Disease | MONDO:0009876; OMIM:262400; ORPHA:231662 |
| Gene | HGNC:4261 (GH1); OMIM:139250 |
| Phenotype (HPO) | HP:0000824 (GH deficiency), HP:0004322 (short stature), HP:0008897 (postnatal growth retardation), HP:0011220 (frontal bossing), HP:0001998 (hypoglycemia), HP:0000054 (micropenis), HP:0000939 (osteoporosis), HP:0002750 (delayed bone age) |
| Cell type (CL) | CL:0000428 (somatotroph), CL:0000138 (chondrocyte), CL:0000236 (B lymphocyte) |
| Anatomy (UBERON) | UBERON:0000007 (pituitary gland), UBERON:0002050 (growth plate cartilage), UBERON:0002107 (liver) |
| Biological process (GO) | GO:0060396 (GH receptor signaling pathway), GO:0060123 (regulation of GH secretion) |
| Chemical/drug (CHEBI/NCIT) | Somatropin/rhGH (NCIT:C1723); Mecasermin/rhIGF-1 (CHEBI:64252); Metformin (NCIT:C61612) |

---

## Sources

- [Entry #262400 — Isolated Growth Hormone Deficiency, Type IA (IGHD1A) — OMIM](https://omim.org/entry/262400)
- [Entry *139250 — Growth Hormone 1; GH1 — OMIM](https://www.omim.org/entry/139250)
- [Entry 173100 — Isolated Growth Hormone Deficiency, Type II — OMIM](https://omim.org/entry/173100)
- [Isolated growth hormone deficiency type IA — NORD/MONDO](https://rarediseases.org/mondo-disease/isolated-growth-hormone-deficiency-type-ia/)
- [Isolated Growth Hormone Deficiency, Type Ia — MalaCards](https://www.malacards.org/card/isolated_growth_hormone_deficiency_type_ia)
- [Orphanet: Isolated growth hormone deficiency type IA (ORPHA231662)](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=en&Expert=231662)
- [Clinical challenges in the management of isolated GH deficiency type IA in adulthood — PMC3965272 (PMID:24683479)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3965272/)
- [Isolated growth hormone deficiency type IA due to a novel GH1 variant: a case report — BMC Medical Genomics (PMID:34470639)](https://link.springer.com/article/10.1186/s12920-021-01057-z)
- [Isolated growth hormone deficiency type IA due to a novel GH1 variant: a case report — PMC8411534](https://pmc.ncbi.nlm.nih.gov/articles/PMC8411534/)
- [Isolated Growth Hormone Deficiency IA due to a Novel Homozygous Large Deletion ∼1.6 kb Spanning Exons 1–4 of GH1 Gene — PMC11839734 (PMID:39980897)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11839734/)
- [Different Growth Responses to Recombinant Human Growth Hormone in Three Siblings with IGHD Type 1A due to a 6.7 kb Deletion — PMC8638633](https://pmc.ncbi.nlm.nih.gov/articles/PMC8638633/)
- [Isolated growth hormone (GH) deficiency type 1A associated with a double deletion in the human GH gene cluster — PubMed (PMID:3005356)](https://pubmed.ncbi.nlm.nih.gov/3005356/)
- [GH1 gene deletions and IGHD type 1A — PubMed (PMID:17551470)](https://pubmed.ncbi.nlm.nih.gov/17551470/)
- [Growth Hormone Antibody — ScienceDirect Topics](https://www.sciencedirect.com/topics/medicine-and-dentistry/growth-hormone-antibody)
- [Prevalence of Human GH-1 Gene Alterations in Patients with Isolated Growth Hormone Deficiency — Pediatric Research (PMID:9432120)](https://www.nature.com/articles/pr199816)
- [A GHRHR founder mutation causes isolated growth hormone deficiency type IV in a consanguineous Pakistani family — PMC10029353](https://pmc.ncbi.nlm.nih.gov/articles/PMC10029353/)
- [Novel Deletion in the GH1 Gene Including the IVS3 Branch Site Responsible for Autosomal Dominant IGHD — PubMed (PMID:16368751)](https://pubmed.ncbi.nlm.nih.gov/16368751/)
- [A Molecular Basis for Variation in Clinical Severity of Isolated Growth Hormone Deficiency Type II — PMC2795644](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2795644/)
- [The Role of the hGH Locus Control Region in Somatotrope Restriction of hGH-N Gene Expression — PMC3082332](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3082332/)
- [GH1 Gene — GeneCards](https://www.genecards.org/cgi-bin/carddisp.pl?gene=GH1)
- [Mouse models of growth hormone deficiency — Reviews in Endocrine and Metabolic Disorders (Springer, 2020)](https://link.springer.com/article/10.1007/s11154-020-09601-5)
- [A mouse with targeted ablation of the growth hormone-releasing hormone gene: a new model of isolated growth hormone deficiency — PubMed](https://pubmed.ncbi.nlm.nih.gov/15155578/)
- [Common and Uncommon Mouse Models of Growth Hormone Deficiency — PMC12102728](https://pmc.ncbi.nlm.nih.gov/articles/PMC12102728/)
- [Mice with Heterozygous Deletion of Exon 3 in the Gh Gene Demonstrate Growth Retardation Caused by Reduced Ghrhr mRNA — PMC11817076](https://pmc.ncbi.nlm.nih.gov/articles/PMC11817076/)
- [Diagnosis and testing for growth hormone deficiency across the ages — Endocrine Connections](https://ec.bioscientifica.com/view/journals/ec/12/7/EC-22-0504.xml)
- [Insulin-like growth factor-1 level is a poor diagnostic indicator of growth hormone deficiency — PMC8352887](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8352887/)
- [IGF-1 and IGFBP-3 screening for disorders of growth hormone secretion — PubMed (PMID:8657365)](https://pubmed.ncbi.nlm.nih.gov/8657365/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 23 |
| Resolved | 23 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 23 |
| On topic | 20 |
| Off topic | 0 |

All extracted references resolved successfully.