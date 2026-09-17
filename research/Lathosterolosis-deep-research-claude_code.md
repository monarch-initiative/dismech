---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-27T18:52:31.252259'
end_time: '2026-08-27T18:57:25.698580'
duration_seconds: 294.45
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Lathosterolosis
  mondo_id: ''
  category: ''
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
  num_turns: 36
  total_cost_usd: 1.2145058
  session_id: 00937d02-a143-56ac-a731-3747f9ee4c64
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 21
reference_validation:
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 11
  on_topic: 10
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Lathosterolosis
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Lathosterolosis** covering all of the
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

I now have enough comprehensive, well-sourced material to compile the full report.

# Lathosterolosis: Comprehensive Research Report

## 1. Disease Information

**Overview.** Lathosterolosis (LATHOS) is an ultra-rare, autosomal recessive inborn error of post-squalene cholesterol biosynthesis caused by deficiency of sterol-C5-desaturase (lathosterol oxidase), which catalyzes the penultimate step of cholesterol synthesis — dehydrogenation of lathosterol to 7-dehydrocholesterol (7-DHC). It presents as a multiple-congenital-anomaly/intellectual-disability syndrome with a phenotype that overlaps substantially with Smith-Lemli-Opitz syndrome (SLOS), the biosynthetic-pathway neighbor caused by 7-dehydrocholesterol reductase (DHCR7) deficiency one step downstream ([Wikipedia](https://en.wikipedia.org/wiki/Lathosterolosis); [PMC3897790](https://pmc.ncbi.nlm.nih.gov/articles/PMC3897790/)).

**Key identifiers:**
- **OMIM disease:** #607330 (LATHOS) ([OMIM](https://omim.org/entry/607330))
- **OMIM gene:** *602286 (SC5D, formerly SC5DL) ([OMIM](https://www.omim.org/entry/602286))
- **Orphanet:** ORPHA:46059 ([Orphanet](https://www.orpha.net/en/disease/detail/46059))
- **MONDO:** MONDO:0011816
- **MedGen:** C1846421
- **Gene location:** SC5D, 11q23.3 (per GeneReviews; some sources cite 11q23.3-q24.1)
- **Synonyms/alt names:** Sterol-C5-desaturase deficiency; SC5D deficiency; lathosterol oxidase deficiency; 3β-hydroxysteroid-Δ5-desaturase deficiency

**Nature of evidence base.** All information derives from aggregated case reports (individual-patient case series and reviews), not large disease registries or EHR aggregation — the condition is defined almost entirely by a handful of published cases plus a knockout mouse model and, more recently, cell-line (CRISPR knockout) mechanistic work.

Sources: [OMIM #607330](https://omim.org/entry/607330), [GeneReviews NBK597809](https://www.ncbi.nlm.nih.gov/sites/books/NBK597809/), [Orphanet ORPHA:46059](https://www.orpha.net/en/disease/detail/46059), [GARD](https://rarediseases.info.nih.gov/diseases/9711/lathosterolosis)

---

## 2. Etiology

**Primary cause.** Biallelic pathogenic variants in *SC5D* (11q23.3), encoding lathosterol oxidase (EC 1.14.19.20), an ER-membrane iron-dependent oxidoreductase of the sterol desaturase family. Loss of enzymatic activity blocks the lathosterol→7-DHC step, causing lathosterol accumulation with variably reduced downstream cholesterol synthesis ([GeneCards SC5D](https://www.genecards.org/cgi-bin/carddisp.pl?gene=SC5D); [Reactome R-HSA-195662](https://reactome.org/content/detail/R-HSA-195662)).

**Genetic risk factors.** Purely monogenic/Mendelian — no known susceptibility loci or modifier genes have been reported; the extreme rarity (fewer than a dozen molecularly confirmed patients worldwide as of 2023) precludes genotype-phenotype correlation studies. Reported pathogenic alleles include:
- p.Arg29Gln (R29Q) and p.Gly211Asp (G211D) — original index patient, compound heterozygous (Brunetti-Pierri et al. 2002, PMID: [12189593](https://pubmed.ncbi.nlm.nih.gov/12189593/))
- p.Lys148Glu (K148E) and p.Asp210Glu (D210E) — Rossi et al. 2007 fetal case, PMID: [17853487](https://pubmed.ncbi.nlm.nih.gov/17853487/)
- p.Pro160Arg (c.479C>G) and p.Asp210Glu (c.630C>A) — Anderson et al. 2019, PMID: [30097991](https://pubmed.ncbi.nlm.nih.gov/30097991/)
- p.Asn71Ile (c.212A>T) and p.Gln72* nonsense (c.214C>T) — Yaplito-Lee/Verma et al. 2020, PMID: [33204591](https://pubmed.ncbi.nlm.nih.gov/33204591/)
- p.Leu219Ser (biallelic missense, c.656T>C) — Söbü et al. 2023, PMID: [36607840](https://pubmed.ncbi.nlm.nih.gov/36607840/)

Population frequency data are sparse; individual reported SC5D variants appear in gnomAD only as ultra-rare singletons (e.g., allele frequency ~7×10⁻⁶ for specific alleles such as rs104894297), consistent with a disease affecting well under 1 in 1,000,000 births, though under-ascertainment of mild cases is suspected.

**Environmental/infectious risk factors.** None identified — this is a pure inborn metabolic error with no known environmental trigger, teratogen interaction, or infectious contribution.

**Protective factors.** None reported (genetic or environmental); no protective alleles or exposures are documented.

**Gene-environment interaction.** Not applicable/undocumented; disease expressivity variation (from prenatal-lethal to mild adult-surviving phenotypes) is presumed related to residual enzyme activity from the specific allele combination rather than to environmental modulation.

Sources: [GeneReviews NBK597809](https://www.ncbi.nlm.nih.gov/sites/books/NBK597809/), [PubMed 12189593](https://pubmed.ncbi.nlm.nih.gov/12189593/), [17853487](https://pubmed.ncbi.nlm.nih.gov/17853487/), [30097991](https://pubmed.ncbi.nlm.nih.gov/30097991/), [33204591](https://pubmed.ncbi.nlm.nih.gov/33204591/), [36607840](https://pubmed.ncbi.nlm.nih.gov/36607840/)

---

## 3. Phenotypes

Lathosterolosis spans a continuum from prenatal-lethal multiple-malformation syndrome to a mild, largely neurodevelopmental/ophthalmologic phenotype recognized only in later childhood. GeneReviews summarizes: *"global developmental delays, intellectual disability, microcephaly, characteristic facial features... bilateral cataracts; digit anomalies... and variable liver disease ranging from asymptomatic elevation of liver enzymes to cirrhosis and liver failure"* ([NBK597809](https://www.ncbi.nlm.nih.gov/sites/books/NBK597809/)).

### Craniofacial
- Microcephaly (congenital; suggested term: **HP:0000252** Microcephaly)
- Bitemporal narrowing (**HP:0000341**)
- Sloping/narrow forehead (**HP:0000340**)
- Ptosis (**HP:0000508**)
- Puffy cheeks
- Micrognathia (**HP:0000347**)
- Epicanthal folds (**HP:0000286**)
- Downslanting palpebral fissures (**HP:0000494**)
- Anteverted nares (**HP:0000463**)
- Broad/bulbous nasal tip (**HP:0000414**)
- Long philtrum (**HP:0000343**)
- High-arched palate (**HP:0000218**)
- Cleft palate — reported in the mouse model and general SC5D-mutant craniofacial literature, but notably **absent** in the human index case series reviewed in PMC3897790, distinguishing it somewhat from SLOS

### Ocular
- Bilateral (or unilateral) posterior cataracts (**HP:0000519**/HP:0000665) — a relatively distinguishing feature versus SLOS, present in most surviving cases including the "relatively mild" Anderson et al. 2019 patient, who presented at age 5 with cataracts and learning difficulties and had a full-scale IQ of 64 at age 11 ([PubMed 30097991](https://pubmed.ncbi.nlm.nih.gov/30097991/))
- Microcornea (**HP:0000482**)
- Corneal stromal opacity (**HP:0007957**)

### Neurological
- Global developmental delay / intellectual disability (**HP:0001263**/HP:0001249) — present in essentially all reported living patients, variable severity from mild learning difficulty to severe delay
- Hypotonia (**HP:0001252**) — in most cases
- Seizures (**HP:0001250**) — reported in the 2023 case (8-month-old with seizures and brain atrophy, PMID: [36607840](https://pubmed.ncbi.nlm.nih.gov/36607840/))
- Cerebellar cortical atrophy, cerebral calcification, Chiari malformation, myoclonus — reported in the aggregate GARD symptom list

### Skeletal/limb
- Postaxial polydactyly (upper and/or lower limb, predominantly feet) (**HP:0100259**/HP:0012470)
- Bilateral 2nd–3rd or 2nd–4th toe syndactyly (**HP:0001770**)
- Bilateral clubfoot/talipes (**HP:0001762**)
- 5th finger clinodactyly (**HP:0030084**)

### Hepatic
- Elevated liver transaminases (asymptomatic to marked): e.g., ALT 321–364 IU/L, GGT 317–414 U/L in the Verma/Yaplito-Lee case ([PMC7653246](https://pmc.ncbi.nlm.nih.gov/articles/PMC7653246/))
- Progressive fibrosis to cirrhosis and liver failure in severe cases (Fibroscan 15.6 kPa vs. normal 2.5–8.5 kPa in one case)
- This spectrum is the principal severity-determining organ system: prognosis tracks liver involvement more than any other feature

### Other/systemic
- Failure to thrive (**HP:0001508**)
- Kidney anomalies (**HP:0000077**)
- Hearing impairment (**HP:0000365**)
- Thrombocytopenia (**HP:0001873**)
- Lysosomal/mucolipidosis-like storage — lamellar cytoplasmic inclusions on ultrastructural/histopathological exam (Rossi et al. 2007, PMID: [17853487](https://pubmed.ncbi.nlm.nih.gov/17853487/)), a distinctive secondary storage phenomenon
- Neural tube defect and prenatal liver involvement reported in a fetal case (Rossi et al. 2007)

**Onset:** Congenital/neonatal for the classic severe phenotype (recognizable pattern of malformation at birth); later childhood presentation (age ~5–8 years, via cataracts/learning difficulty) in mild cases — indicating a true clinical spectrum rather than a single fixed presentation.

**Progression:** Variable — stable/mild in some, progressive hepatic fibrosis/cirrhosis in others. Neurodevelopmental impairment appears nonprogressive once established but is present from early childhood in nearly all cases.

**Frequency (population-level):** With only ~7 molecularly confirmed reported patients as of the most recent GeneReviews update, per-symptom frequency percentages are not statistically meaningful; qualitative frequency terms ("most," "all reported," "variable") are used throughout the literature instead of numeric percentages.

**Quality of life impact:** Not formally studied with validated instruments (no EQ-5D/SF-36 data identified); qualitatively, developmental/intellectual disability and progressive liver disease are the dominant drivers of long-term burden, with milder patients able to reach adulthood.

Sources: [GeneReviews NBK597809](https://www.ncbi.nlm.nih.gov/sites/books/NBK597809/), [Orphanet ORPHA:46059](https://www.orpha.net/en/disease/detail/46059), [PMC3897790](https://pmc.ncbi.nlm.nih.gov/articles/PMC3897790/), [PMC7653246](https://pmc.ncbi.nlm.nih.gov/articles/PMC7653246/), [GARD](https://rarediseases.info.nih.gov/diseases/9711/lathosterolosis), PMIDs 12189593, 17853487, 24142275, 30097991, 31259789, 33204591, 36607840

---

## 4. Genetic/Molecular Information

**Causal gene:** SC5D (HGNC:10547; formerly SC5DL), OMIM *602286, chromosome 11q23.3, encoding lathosterol oxidase / sterol-C5-desaturase (UniProt O75845).

**Variant spectrum:** All reported disease alleles to date are **missense** or one **nonsense** variant, in compound-heterozygous or (rarely) homozygous configuration — no large deletions/duplications have been identified by deletion/duplication analysis in the diagnosed cases (per GeneReviews). Representative pathogenic variants (NM_006918 transcript numbering where given):

| Study | Variant 1 | Variant 2 | PMID |
|---|---|---|---|
| Brunetti-Pierri 2002 (index case) | p.R29Q | p.G211D | [12189593](https://pubmed.ncbi.nlm.nih.gov/12189593/) |
| Rossi 2007 (fetal case) | p.K148E | p.D210E | [17853487](https://pubmed.ncbi.nlm.nih.gov/17853487/) |
| Anderson 2019 (mild case) | c.479C>G p.(P160R) | c.630C>A p.(D210E) | [30097991](https://pubmed.ncbi.nlm.nih.gov/30097991/) |
| Yaplito-Lee/Verma 2020 | c.212A>T p.(N71I) | c.214C>T p.(Q72*) | [33204591](https://pubmed.ncbi.nlm.nih.gov/33204591/) |
| Söbü 2023 | c.656T>C p.(L219S) | (biallelic, homozygous) | [36607840](https://pubmed.ncbi.nlm.nih.gov/36607840/) |

Note: p.D210E recurred independently in two unrelated families (Rossi 2007 and Anderson 2019), suggesting it may be a recurrent or mutational-hotspot allele, though this has not been formally established as a founder variant.

**Variant classification:** Per ClinVar, several SC5D variants are submitted with classifications ranging from pathogenic to variants of uncertain significance (e.g., RCV000401412, RCV000340453); given the extreme rarity of ascertained cases, ACMG/AMP classification confidence intervals are wide, and functional/fibroblast enzyme assay confirmation (elevated lathosterol, blocked conversion to 7-DHC) remains the most robust classification evidence.

**Population/allele frequency:** Individual SC5D pathogenic alleles are essentially private, ultra-rare variants in gnomAD (allele frequency ~7×10⁻⁶ reported for specific alleles such as rs104894297 and rs1313359281) — consistent with autosomal recessive disease well below 1:1,000,000 birth prevalence, though possible underascertainment of milder cases is repeatedly flagged in the literature.

**Somatic vs. germline:** Exclusively germline; no somatic/mosaic cases reported.

**Functional consequences:** Missense variants are presumed to reduce or abolish lathosterol-oxidase catalytic activity (loss-of-function mechanism), confirmed functionally via fibroblast sterol profiling (elevated lathosterol, near-absent conversion to 7-DHC) rather than by direct enzymatic assay of recombinant protein in most reports.

**Modifier genes:** None identified.

**Epigenetics/chromosomal abnormalities:** No epigenetic or large chromosomal (aneuploidy/translocation) mechanism has been reported; disease is exclusively due to point/small-indel-type coding variants in SC5D.

**Molecular mechanism (protein level):** SC5D/lathosterol oxidase is an ER-membrane, iron-binding, C-5(6) sterol desaturase (EC 1.14.19.20) that introduces a Δ5,6 double bond into lathosterol to yield 7-dehydrocholesterol — the penultimate step of the Kandutsch–Russell branch of cholesterol biosynthesis, immediately upstream of the DHCR7-catalyzed step defective in Smith-Lemli-Opitz syndrome ([GeneCards](https://www.genecards.org/cgi-bin/carddisp.pl?gene=SC5D); [Reactome R-HSA-195662](https://reactome.org/content/detail/R-HSA-195662)).

Suggested ontology bindings: **HGNC:10547** (SC5D); **GO:0006695** (cholesterol biosynthetic process); **GO:0016132** (brassinosteroid — n/a) — more precisely **GO:0000247** (C-5 sterol desaturase activity) and **GO:0000253** (3-keto-sterol reductase — n/a, adjacent pathway step); protein term **CHEBI:17168** (lathosterol) → **CHEBI:17759** (7-dehydrocholesterol) → **CHEBI:16113** (cholesterol).

Sources: [OMIM *602286](https://www.omim.org/entry/602286), [GeneCards SC5D](https://www.genecards.org/cgi-bin/carddisp.pl?gene=SC5D), [UniProt O75845](https://www.uniprot.org/uniprotkb/O75845/entry), [Reactome R-HSA-195662](https://reactome.org/content/detail/R-HSA-195662), PMIDs 12189593, 17853487, 30097991, 33204591, 36607840

---

## 5. Environmental Information

Lathosterolosis is a purely monogenic inborn error of metabolism; no environmental factors (toxins, occupational exposures), lifestyle factors, or infectious agents have been implicated as causal or risk-modifying in any published report. This section is essentially **not applicable** for this disease — a search of CTD/TOXNET-type literature and the primary case reports returned no gene-environment or exposure findings.

---

## 6. Mechanism / Pathophysiology

### Molecular pathway
SC5D acts in the post-squalene, post-lanosterol segment of the Kandutsch–Russell cholesterol biosynthetic pathway (KEGG map00100, "Steroid biosynthesis"), immediately downstream of lanosterol 14α-demethylase (CYP51A1) and upstream of 7-dehydrocholesterol reductase (DHCR7). Loss of SC5D activity blocks lathosterol → 7-dehydrocholesterol conversion, causing:
1. **Substrate accumulation**: marked elevation of lathosterol (and, to lesser degree, its metabolites 24-dehydrolathosterol and zymostenol) in plasma, fibroblasts, and tissues.
2. **Product deficiency**: reduced flux to 7-DHC and downstream cholesterol, though — importantly — total plasma cholesterol is typically **normal**, distinguishing lathosterolosis biochemically from SLOS, where cholesterol is characteristically low ([PMC3897790](https://pmc.ncbi.nlm.nih.gov/articles/PMC3897790/)).

### Causal chain — from initial defect to clinical manifestation
Loss-of-function SC5D variant → reduced/absent lathosterol oxidase activity → lathosterol accumulation + reduced distal-pathway sterol flux → (a) direct lathosterol/intermediate cytotoxicity and lysosomal storage-like lamellar inclusions; (b) impaired cholesterol-dependent Hedgehog signaling during embryogenesis (cholesterol is required for post-translational modification and signaling range of Sonic hedgehog, SHH) → limb patterning defects (polydactyly, syndactyly), craniofacial malformation, and CNS developmental anomalies; (c) hepatocyte lipid/sterol stress → progressive liver injury/fibrosis/cirrhosis.

The Krakowiak et al. 2003 mouse knockout study (PMID: [12812989](https://pubmed.ncbi.nlm.nih.gov/12812989/)) established that malformations in *Sc5d*-null mice — stillbirth, cleft palate, micrognathia, and limb defects — occur despite normal/near-normal residual cholesterol in some tissues, arguing that **reduced cholesterol availability during embryogenesis, rather than lathosterol toxicity per se, drives the malformation phenotype**, while intracellular sterol/lathosterol storage represents an additional, largely postnatal pathology (a distinct storage-disease-like component).

### Cellular/mechanistic detail from recent (2024) work
A CRISPR-Cas9 SC5D-knockout HepG2 hepatoma cell model (part of a broader CYP51A1/DHCR24/SC5D knockout comparison, PMC11387598, 2024) found:
- ~100-fold accumulation of lathosterol, with secondary elevation of 24-dehydrolathosterol (~10-fold) and zymostenol (~6-fold)
- Slower proliferation and G0/G1 cell-cycle arrest, especially under lipid-depleted conditions
- Activation of ER-stress (XBP1) and SREBF1/2 (cholesterol/lipid-sensing) transcriptional programs, with CCND1/EGR1 modulation of the G1/S transition
- Upregulated fatty-acid metabolism and PPAR-signaling genes (FADS2, ELOVL6, HSD17B12, CYP2J2), suggesting a compensatory metabolic shift when sterol synthesis is blocked

This is the most direct recent (2024) molecular-mechanism evidence and is classified as **IN_VITRO/cell-line** evidence — it models a plausible hepatocellular contribution to the clinical liver phenotype but has not been directly confirmed in patient liver tissue.

### Immune/tissue-damage mechanisms
No autoimmune or classical inflammatory mechanism is implicated. Tissue injury appears driven by (1) developmental morphogen (Hedgehog) signaling disruption during embryogenesis and (2) chronic sterol/lipid metabolic stress in postnatal hepatocytes leading to fibrosis.

### Suggested ontology terms
- **GO:0006695** cholesterol biosynthetic process
- **GO:0016125** sterol metabolic process
- **GO:0007224** smoothened signaling pathway (Hedgehog pathway proxy)
- **GO:0034976** response to endoplasmic reticulum stress
- **CL:0000182** hepatocyte
- **CL:0000586** germ cell / **CL:0000047** neural stem cell (embryonic limb/CNS morphogenesis context — refine per specific node)
- **UBERON:0002107** liver; **UBERON:0002101** limb; **UBERON:0000411** vertebrate limb bud

Sources: [PMC3897790](https://pmc.ncbi.nlm.nih.gov/articles/PMC3897790/), Krakowiak et al. 2003 PMID [12812989](https://pubmed.ncbi.nlm.nih.gov/12812989/) (Human Molecular Genetics), [PMC11387598 (2024, iScience)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11387598/), [Reactome R-HSA-195662](https://reactome.org/content/detail/R-HSA-195662)

---

## 7. Anatomical Structures Affected

**Organ level (primary):**
- **Liver** — the dominant morbidity/mortality-determining organ; ranges from asymptomatic transaminitis to cirrhosis/liver failure (UBERON:0002107)
- **Eye/lens** — cataracts (UBERON:0000965 lens of camera-type eye)
- **CNS/brain** — developmental delay, seizures, cerebellar atrophy, calcifications, Chiari malformation (UBERON:0000955 brain; UBERON:0002037 cerebellum)
- **Skeletal system, especially craniofacial and limb** — micrognathia, malformed facies, polydactyly/syndactyly, clubfoot (UBERON:0001456 face; UBERON:0002101 limb)
- **Kidney** — structural anomalies (UBERON:0002113)
- **Ear** — hearing impairment (UBERON:0001690)

**Secondary/complication-level involvement:** Hematologic (thrombocytopenia), consistent with hepatic synthetic/portal-hypertension sequelae in severe cases.

**Body systems:** Hepatobiliary, skeletal/musculoskeletal, ophthalmologic, nervous, urogenital, integumentary (in the mouse model — skin barrier).

**Tissue/cell level:**
- Hepatocytes (CL:0000182) — lipid/sterol storage, fibrosis
- Lens epithelial cells — cataract formation
- Chondrocytes/osteoblasts in limb bud mesenchyme — polydactyly/limb patterning (Hedgehog-dependent)
- Neural progenitor cells — CNS developmental anomalies

**Subcellular level:**
- Endoplasmic reticulum (site of SC5D enzymatic activity; GO:0005789 ER membrane)
- Lysosome-like storage vesicles — lamellar inclusions on electron microscopy (mucolipidosis-like storage), suggesting secondary lysosomal/autophagic pathway involvement (GO:0005764 lysosome)

**Localization/laterality:** Cataracts and limb anomalies reported as both unilateral and bilateral across cases; no consistent lateralization pattern.

Sources: [GeneReviews NBK597809](https://www.ncbi.nlm.nih.gov/sites/books/NBK597809/), [PMC3897790](https://pmc.ncbi.nlm.nih.gov/articles/PMC3897790/), Rossi et al. 2007 PMID [17853487](https://pubmed.ncbi.nlm.nih.gov/17853487/)

---

## 8. Temporal Development

**Onset:** Congenital for the classic multiple-malformation phenotype (recognizable at birth or prenatally via ultrasound anomalies in the most severe/fetal cases); however, milder patients are first recognized later — bilateral cataracts and learning difficulty identified around age 5 years in the Anderson et al. 2019 patient, and seizures/brain atrophy noted at 8 months in the Söbü et al. 2023 patient.

**Onset pattern:** Generally insidious for the neurodevelopmental/hepatic components; can be acute in fetal/perinatal lethal presentations (stillbirth in the mouse model and presumably in the most severe human end of the spectrum, though a live-born severely affected human case has not been separately documented as stillborn in the literature reviewed here — the mouse null is embryonic/perinatal lethal).

**Progression:**
- Liver disease is the most clearly progressive feature — documented natural progression from elevated transaminases to fibrosis (Fibroscan-confirmed) to cirrhosis/liver failure in the most severe reported cases, with two cases requiring/undergoing liver transplantation (per GeneReviews management section, citing Ho et al. 2014 and related cases).
- Neurodevelopmental impairment is present from early life and is not clearly progressive once established (static encephalopathy-like course), though seizures may emerge later.
- With simvastatin treatment, biochemical (lathosterol) normalization and histologic (fibrosis) improvement have been documented over a ~2-year follow-up in one case ([PMC7653246](https://pmc.ncbi.nlm.nih.gov/articles/PMC7653246/)).

**Disease course pattern:** Chronic, with a spectrum from static/stable (mild cases reaching adulthood) to progressive hepatic deterioration (severe cases).

**Critical periods:** Embryonic/fetal period is critical for the Hedgehog-signaling-dependent malformation component (limb, craniofacial, neural tube); this window is not modifiable postnatally. Early childhood appears to be a window where statin therapy has been trialed with apparent biochemical and modest developmental benefit, though causality is unproven (single-patient experience, per GeneReviews).

Sources: [GeneReviews NBK597809](https://www.ncbi.nlm.nih.gov/sites/books/NBK597809/), [PMC7653246](https://pmc.ncbi.nlm.nih.gov/articles/PMC7653246/), PMID [36607840](https://pubmed.ncbi.nlm.nih.gov/36607840/)

---

## 9. Inheritance and Population

**Epidemiology:** Extremely rare — GeneReviews states only **seven individuals** have been molecularly/biochemically confirmed and reported in the literature to date (as of its most recent update), with likely underdiagnosis of milder phenotypes given nonspecific presentation (learning difficulty + cataracts). No formal prevalence or incidence estimate (cases per 100,000) exists; the disease is best characterized as "ultra-rare, case-report-level" rather than registry-quantified.

**Inheritance pattern:** Autosomal recessive (**HP:0000007**). For carrier (heterozygous) × carrier matings: 25% affected, 50% carrier, 25% unaffected/non-carrier per pregnancy (Mendelian expectation, per GeneReviews).

**Penetrance:** Full penetrance is presumed for biallelic loss-of-function combinations causing the classic severe phenotype; however, the existence of "relatively mild" cases identified only via cataracts/learning difficulty in later childhood suggests substantial variable expressivity depending on residual enzyme activity from specific missense combinations (e.g., hypomorphic alleles like p.D210E, recurrent across two unrelated mild-to-moderate cases).

**Expressivity:** Highly variable — from prenatal/perinatal-lethal multiple-malformation syndrome to a mild neurodevelopmental/ophthalmologic phenotype recognized in later childhood; likely genotype-dependent (missense vs. nonsense, position/severity of the substitution) though formal genotype-phenotype correlation has not been statistically established given small case numbers.

**Genetic anticipation:** Not applicable — not a repeat-expansion disorder.

**Germline mosaicism, founder effects:** Not documented in the literature reviewed; p.D210E's recurrence in two unrelated families (Rossi 2007, Anderson 2019) could suggest a mutational hotspot, but no formal founder-haplotype study has been published.

**Consanguinity:** Not specifically flagged as a major risk factor across the reported cases reviewed (most cases were compound heterozygous, implying non-consanguineous or at least non-obviously consanguineous unions in most families, though this is not exhaustively confirmed here).

**Carrier frequency:** Not established at a population level; individual known pathogenic SC5D alleles are present in gnomAD only as private/ultra-rare variants (allele frequency on the order of 10⁻⁶), consistent with a carrier frequency far below that of common recessive conditions.

**Population demographics:** No specific ethnic or geographic enrichment has been reported; cases have been described in multiple ancestries/countries (Italy — Brunetti-Pierri/Rossi groups; UK — Anderson et al.; Hong Kong — Ho et al.; USA — Prasun et al.; Australia — Yaplito-Lee/Verma et al.; Turkey — Söbü et al.), suggesting pan-ethnic occurrence without an identified founder population.

**Sex ratio:** No consistent sex predominance reported across the small case series (both male and female patients described).

Sources: [GeneReviews NBK597809](https://www.ncbi.nlm.nih.gov/sites/books/NBK597809/), [Orphanet ORPHA:46059](https://www.orpha.net/en/disease/detail/46059)

---

## 10. Diagnostics

### Clinical/biochemical tests
- **Plasma sterol profiling (GC/MS)** — the primary diagnostic biochemical test: markedly elevated lathosterol (reported values as high as 54–82 μmol/L vs. normal <10–18 μmol/L depending on the reference lab), with **normal or low 7-dehydrocholesterol and normal total cholesterol** — this normal-cholesterol pattern is a key distinguishing feature from SLOS.
- Fibroblast sterol analysis — demonstrates block in lathosterol→7-DHC conversion; filipin staining may show a "variant" cholesterol storage pattern.
- Liver enzymes (ALT, GGT) — elevated in hepatic involvement; used for both diagnosis and longitudinal monitoring.
- Fibroscan/elastography — used to quantify and monitor hepatic fibrosis (e.g., 15.6 kPa vs. normal 2.5–8.5 kPa in one reported case).
- Histopathology/electron microscopy — lamellar cytoplasmic inclusions (mucolipidosis-like lysosomal storage pattern) on liver or other tissue biopsy.

### Genetic testing
- **Single-gene SC5D sequencing** or **multigene sterol-biosynthesis-disorder panel** (including SC5D, DHCR7, DHCR24, MSMO1, CYP51A1, LSS, and related genes) or **exome/genome sequencing** — GeneReviews states sequence analysis detects essentially all known pathogenic variants; no deletion/duplication (CNV) pathogenic variant has yet been identified in this gene for this disease.
- Chromosomal microarray/karyotype: not informative (this is a point-variant, not a CNV, disorder).

### Differential diagnosis
The central differential is **Smith-Lemli-Opitz syndrome (SLOS, DHCR7 deficiency)**, sharing developmental delay, microcephaly, and facial dysmorphism, but distinguishable because:
- Cataracts and liver disease are common in lathosterolosis but relatively uncommon in SLOS
- Cholesterol is typically low in SLOS but normal in lathosterolosis
- 7-DHC is markedly elevated in SLOS but normal in lathosterolosis
- Cleft palate is common in SLOS but was absent across the reviewed lathosterolosis case series

Other differentials in the sterol-biosynthesis-disorder category: squalene synthase deficiency, lanosterol synthase deficiency, desmosterolosis (DHCR24 deficiency), CHILD syndrome (NSDHL), and CK syndrome/other X-linked sterol disorders (per GeneReviews).

### Screening
No newborn screening or population carrier-screening program exists for this ultra-rare condition; diagnosis is case-by-case based on clinical suspicion (malformation pattern, cataracts + developmental delay + liver disease) followed by targeted sterol/molecular testing.

Sources: [GeneReviews NBK597809](https://www.ncbi.nlm.nih.gov/sites/books/NBK597809/), [PMC3897790](https://pmc.ncbi.nlm.nih.gov/articles/PMC3897790/), [PMC7653246](https://pmc.ncbi.nlm.nih.gov/articles/PMC7653246/)

---

## 11. Outcome/Prognosis

**Survival/mortality:** No formal survival statistics exist given the tiny case count. GeneReviews notes prognosis depends heavily on liver disease severity: individuals with mild hepatic involvement may reach adulthood, while those with progressive cirrhosis/liver failure have poorer outcomes; two reported cases underwent (or were candidates for) liver transplantation, after which plasma lathosterol normalized and quality of life reportedly improved.

**Morbidity:** Chronic developmental/intellectual disability is near-universal among survivors; hepatic morbidity (fibrosis/cirrhosis) is the dominant driver of serious long-term complications and mortality risk.

**Prognostic factors:** Degree of residual SC5D enzymatic activity (genotype-dependent), severity/timing of liver disease onset, and response to statin therapy appear to be the principal modifiers of outcome, though this is based on very limited case experience rather than statistically validated prognostic modeling.

**Complications:** Cirrhosis, liver failure (requiring transplantation in severe cases), thrombocytopenia (likely secondary to portal hypertension/hypersplenism in advanced liver disease), seizures, hearing impairment.

Sources: [GeneReviews NBK597809](https://www.ncbi.nlm.nih.gov/sites/books/NBK597809/), [PMC7653246](https://pmc.ncbi.nlm.nih.gov/articles/PMC7653246/)

---

## 12. Treatment

### Pharmacotherapy
- **Simvastatin** (HMG-CoA reductase inhibitor), dosed roughly **0.2–1 mg/kg/day**, is the principal reported targeted therapy. Rationale: inhibiting upstream HMG-CoA reductase reduces overall flux through the sterol pathway, thereby lowering substrate (lathosterol) accumulation.
  - Ho et al. 2014: simvastatin normalized blood lathosterol and was associated with improved neurodevelopmental profile ([PMID 24142275](https://pubmed.ncbi.nlm.nih.gov/24142275/)).
  - Yaplito-Lee/Verma et al. 2020 (PMC7653246): simvastatin 5→10 mg/day (0.2→0.4 mg/kg/day) normalized plasma lathosterol, reduced ALT (364→69 IU/L) and GGT (414→136 U/L) over 2 years, and improved liver fibrosis on Fibroscan (15.6→12.8 kPa) — the most detailed documented biochemical/hepatic response to date.
  - Prasun et al. 2019: first documented therapeutic statin trial in this specific patient, reducing lathosterol from 81.6 to 7.2 μmol/L within 4 weeks at 1 mg/kg/day, with developmental quotient improvement from 55 to 64 (causality uncertain, single-case).
  - GeneReviews explicitly notes: efficacy remains **unproven in controlled trials** — all evidence is single-patient, uncontrolled, observational.
- Creatine kinase monitoring is used for statin-related myopathy surveillance in the pediatric off-label use context.

### Advanced/definitive therapy
- **Liver transplantation** — used in at least two reported cases with progressive/severe hepatic failure, resulting in normalization of plasma lathosterol (since the graft liver has functional SC5D) and reported improvement in quality of life. This is the only "curative" intervention for the hepatic component but does not address extrahepatic (CNS, skeletal) manifestations, which are fixed by the time of any intervention.
- No gene therapy, enzyme replacement, RNA-based therapy, or cell therapy has been developed or trialed for this condition — it remains an off-label small-molecule (statin) management approach plus organ transplantation for end-stage liver disease.

### Supportive/rehabilitative care
- Developmental/early intervention therapy for intellectual disability
- Ophthalmology management (cataract surgery as needed) — suggested NCIT term: **NCIT:C15329** (Surgical Procedure) for cataract extraction
- Orthopedic intervention for limb anomalies (e.g., polydactyly correction, clubfoot management) — **NCIT:C16186** (Orthopedic Surgical Procedure)
- Hepatology coordination/monitoring
- Educational support services

### Surveillance (per GeneReviews management guidelines)
- Developmental milestone assessment at each visit
- Annual ophthalmology evaluation
- Liver enzymes at each visit; liver imaging every 6 months

### Suggested treatment ontology terms
- **NCIT:C15986** Pharmacotherapy (simvastatin) with `therapeutic_agent` → **CHEBI:9150** simvastatin
- **NCIT:C15289** Organ Transplantation (liver transplantation)
- **NCIT:C15302** Physical Therapy / **NCIT:C121351** Occupational Therapy (developmental support)
- **NCIT:C15240** Genetic Counseling

Sources: [GeneReviews NBK597809](https://www.ncbi.nlm.nih.gov/sites/books/NBK597809/), [PMC7653246](https://pmc.ncbi.nlm.nih.gov/articles/PMC7653246/), PMID [24142275](https://pubmed.ncbi.nlm.nih.gov/24142275/), PMID [31259789](https://pubmed.ncbi.nlm.nih.gov/31259789/) (Prasun et al., "Lathosterolosis: An Extremely Rare Inherited Condition Associated With Progressive Liver Disease")

---

## 13. Prevention

**Primary prevention:** None possible for de novo occurrence given the recessive Mendelian mechanism; no vaccination, risk-factor modification, or environmental intervention applies (this is not an environmentally modifiable disease).

**Secondary prevention / screening:**
- Carrier testing for at-risk family members once familial pathogenic variants are identified (per GeneReviews genetic counseling section)
- Prenatal diagnosis (chorionic villus sampling/amniocentesis with molecular testing) and preimplantation genetic testing (PGT) are technically available once the familial SC5D variants are known
- No population-based newborn or carrier screening program exists given the extreme rarity

**Genetic counseling:** Standard autosomal recessive counseling — 25% recurrence risk per pregnancy for carrier couples; GeneReviews explicitly recommends DNA banking of affected individuals' samples given the likelihood that testing methodology will continue to improve for this rare condition.

**Tertiary prevention:** Early biochemical/molecular diagnosis followed by simvastatin initiation and close hepatology surveillance is the closest analog to tertiary prevention (aiming to slow or prevent progression to cirrhosis), though as noted, efficacy is not established in controlled trials.

Sources: [GeneReviews NBK597809](https://www.ncbi.nlm.nih.gov/sites/books/NBK597809/)

---

## 14. Other Species / Natural Disease

No naturally occurring veterinary/companion-animal or wildlife cases of SC5D-deficiency disease have been reported in the literature reviewed (no OMIA entry or veterinary case series identified). All non-human data derive from **engineered laboratory models** (see Section 15) rather than natural disease.

---

## 15. Model Organisms

### Mouse (Mus musculus) — primary model
- **Sc5d knockout mouse** (targeted homologous recombination in ES cells; Krakowiak et al. 2003, PMID [12812989](https://pubmed.ncbi.nlm.nih.gov/12812989/), *Human Molecular Genetics*): *Sc5d⁻/⁻* pups are **stillborn**, with micrognathia, cleft palate, and limb-patterning defects (postaxial polydactyly), plus elevated tissue/serum lathosterol and reduced cholesterol.
  - **Phenotype recapitulation:** High fidelity for the craniofacial/limb malformation spectrum (micrognathia, abnormal nasal structure, cleft palate, postaxial polydactyly), and for the core biochemical signature (elevated lathosterol, reduced cholesterol). The paper's central conclusion — that malformations are driven more by **reduced cholesterol** (impairing Hedgehog signaling) than by lathosterol accumulation per se — was a key mechanistic insight informing understanding of the human disease and of SLOS more broadly.
  - **Limitation:** The mouse model is embryonic/perinatal lethal (stillborn), so it cannot model the postnatal, milder end of the human clinical spectrum (later-childhood cataracts/learning-difficulty presentation) or the progressive liver disease course seen in surviving human patients — this is a clear human-model fidelity gap between the severe (embryonic-lethal, mouse-modeled) and mild (postnatally surviving, human-only) ends of the phenotypic spectrum.
- A related **keratinocyte-specific Sc5d-deleted mouse model** was used to study attenuation of UVR-induced vitamin D3 synthesis in skin, reflecting the enzyme's additional dermatologic/vitamin-D-synthesis role (a tissue-specific, disease-adjacent application rather than a direct disease model) — Sigma-Aldrich/ScienceDirect summary.

### Cell-based / in vitro models
- **CRISPR-Cas9 SC5D-knockout HepG2 hepatoma cell line** (2024, PMC11387598) — models cholesterol-pathway disruption at the hepatocyte level; recapitulates lathosterol/24-dehydrolathosterol/zymostenol accumulation and reveals downstream ER-stress (XBP1), SREBF, cell-cycle, and fatty-acid-metabolism pathway perturbations. This is the most direct available cellular model of the hepatic component of human disease, though it has not been benchmarked against patient liver tissue for fidelity.
- Patient-derived skin fibroblasts (used diagnostically across essentially all reported human cases) also serve as a natural "disease-in-a-dish" model confirming the enzymatic block (lathosterol accumulation, blocked 7-DHC synthesis) and abnormal filipin-staining cholesterol storage pattern.

### Applications
The mouse model has been central to (1) confirming SC5D as the causal gene in parallel with human genetic discovery, (2) establishing the "cholesterol deficiency vs. lathosterol toxicity" mechanistic question central to understanding both lathosterolosis and SLOS pathogenesis via Hedgehog signaling, and (3) providing embryonic material for developmental-biology dissection of limb/craniofacial patterning defects. The HepG2 knockout model is beginning to open a route to studying hepatocyte-intrinsic disease mechanisms and potential pharmacologic (e.g., statin) rescue at a cellular level.

Sources: Krakowiak et al. 2003, PMID [12812989](https://pubmed.ncbi.nlm.nih.gov/12812989/); [PMC11387598 (2024)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11387598/); [ScienceDirect keratinocyte Sc5d model](https://www.sciencedirect.com/science/article/abs/pii/S0960076017300821)

---

## Summary Table — Key Ontology Term Suggestions for KB Curation

| Category | Suggested term |
|---|---|
| Disease | MONDO:0011816; OMIM:607330; ORPHA:46059 |
| Gene | hgnc:10547 (SC5D) |
| Molecular function | GO:0000247 (C-5 sterol desaturase activity) |
| Biological process | GO:0006695 (cholesterol biosynthetic process); GO:0007224 (smoothened/Hedgehog signaling) |
| Cellular component | GO:0005789 (endoplasmic reticulum membrane) |
| Chemicals | CHEBI:17168 (lathosterol); CHEBI:17759 (7-dehydrocholesterol); CHEBI:16113 (cholesterol); CHEBI:9150 (simvastatin) |
| Phenotypes (HP) | HP:0000252 microcephaly; HP:0000519/0000665 cataract; HP:0001263 global developmental delay; HP:0100259/0012470 postaxial polydactyly; HP:0001770 syndactyly; HP:0001762 talipes; HP:0000347 micrognathia; HP:0001250 seizure |
| Cell types | CL:0000182 hepatocyte |
| Anatomy | UBERON:0002107 liver; UBERON:0000965 lens; UBERON:0002101 limb; UBERON:0001456 face |
| Treatment | NCIT:C15986 Pharmacotherapy; NCIT:C15289 Organ Transplantation |

---

## Notes on Evidence Gaps for Curation

- **No large-scale registry or systematic-review-level prevalence data exist** — all epidemiology is case-report aggregation (n≈7–10 reported patients total worldwide).
- **No controlled treatment trial** — simvastatin efficacy claims all derive from single-patient, uncontrolled observational reports; this should be flagged explicitly if curated (`derivation_basis`/evidence caveats).
- **Human-model mismatch**: the Sc5d-null mouse is embryonic/perinatal lethal and does not model the surviving, milder human phenotype spectrum — a good candidate for a `HUMAN_MODEL_MISMATCH` discussion if curated per the dismech schema conventions.
- Full-text access to several primary PMIDs (12189593, 12812989, 24142275, 17853487, 31259789, 30097991) was limited by publisher access barriers during this research; abstracts were retrieved via Europe PMC and secondary reviews (GeneReviews, PMC3897790, PMC7653246) that quote and cite them — exact-quote verification against the primary abstract/full text is still recommended before using any of the above as curated evidence snippets.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 11 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.