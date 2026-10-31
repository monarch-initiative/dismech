---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-17T03:12:27.994966'
end_time: '2026-10-17T03:13:54.786710'
duration_seconds: 86.79
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Achalasia-Progeroid Syndrome
  mondo_id: MONDO:0700300
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
  - claude-haiku-5-5
  - claude-sonnet-5-5
  web_search_requests: 6
  num_turns: 13
  total_cost_usd: 0.9418138
  session_id: 22ddb4e8-5468-52f0-b814-e169ed516ce0
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  - Read
  assistant_text_blocks: 3
citation_count: 9
reference_validation:
  total_references: 3
  verified: 1
  not_found: 0
  unverifiable: 2
  confabulation_rate: 0.0
  relevance_assessed: 1
  on_topic: 1
  validator_version: 0.3.0
term_validation:
  total_terms: 2
  verified: 2
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
- **Disease Name:** Achalasia-Progeroid Syndrome
- **MONDO ID:** MONDO:0700300 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Achalasia-Progeroid Syndrome** covering all of the
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

I'll start by searching for what's published on this syndrome.

Next I'll pull the primary paper and the OMIM entry.

# Research report: Achalasia-Progeroid Syndrome (ACHPS)

**Verification limits.** Web search worked. Direct fetches of OMIM, MalaCards and the Genetics in Medicine full text were refused by the proxy, so I didn't read the primary paper myself. Everything below comes from search-result summaries, including quoted fragments of the paper. I did not check any PMID, exact abstract quote or HPO/GO/CL/UBERON/NCIT CURIE against a source. Before any of it goes into a KB entry, quotes need `just fetch-reference` and snippet verification. CURIEs need a lookup in the same step they are written.

The disease is currently documented by essentially one primary paper, and I found no independent replication.

## 1. Disease information

**Overview.** ACHPS is a rare autosomal recessive developmental disorder. Lipodystrophy begins in childhood and gives a progeroid appearance. It comes with corneal clouding, cataract, progressive sensorineural hearing loss and achalasia. OMIM describes it as "onset of lipodystrophy in childhood resulting in a progeroid appearance, associated with corneal clouding, cataracts, hearing loss, and achalasia" ([OMIM #621123](https://omim.org/entry/621123), per search summary).

**Identifiers.**
- OMIM phenotype #621123, "ACHALASIA-PROGEROID SYNDROME; ACHPS". The gene entry is OMIM *620691 (BUD13) ([OMIM *620691](https://omim.org/entry/620691)).
- The MONDO ID in the template (MONDO:0700300) could not be confirmed. A search for it returned nothing relevant. Resolve it through OLS or the MONDO release.
- Orphanet, ICD-10/11 and MeSH identifiers were not found. A "no Orphanet entry" claim would be unverified.
- MalaCards lists the entry ([MalaCards](https://malacards.org/card/achalasia_progeroid_syndrome)). It sits in the progeroid syndrome class (MONDO:0015333) ([Monarch](https://monarchinitiative.org/MONDO:0015333)).

**Synonyms.** The paper's title uses "developmental disorder with lipodystrophy and progeroid features". The MalaCards/OMIM name is "Achalasia-progeroid syndrome". The earlier Refubium thesis title is "A recurrent homozygous mutation affects the BUD13 gene whose residual expression correlates with the severity of a novel human progeroid disorder" ([Refubium](https://refubium.fu-berlin.de/handle/fub188/32282)).

**Data origin.** The data are individual-patient clinical and molecular findings from published case descriptions. They are not aggregated EHR data.

**Key paper.** Kornak U, et al. "Alternative splicing of BUD13 determines the severity of a developmental disorder with lipodystrophy and progeroid features." *Genet Med* 2022;24:1927–1940 ([Genetics in Medicine](https://www.gimjournal.org/article/S1098-3600(22)00759-6/fulltext)). A Rat Genome Database annotation list suggests PMID:35670808, but this is unconfirmed. Check it in PubMed.

## 2. Etiology

- **Cause.** Biallelic loss-of-function-type variation in *BUD13* (11q23). All five reported patients carry the same homozygous nonsense variant, c.688C>T (p.Arg230*), per a search summary of the paper.
- **Risk factors.** No environmental or other genetic risk factors are described. Parental consanguinity (Algerian families) is the practical risk factor for homozygosity.
- **Protective factors / modifiers.** The one modifier-like finding is molecular. The nonsense allele also activates a cryptic splice site, giving a stable truncated hypomorphic isoform ("S1"). Higher S1 levels correlated with milder disease and longer survival (patients A4, A5), and lower levels with severe disease and early death (A1–A3). The cause of the between-patient variation in isoform level is not established in what I could access.
- **Gene–environment interactions.** None reported.

## 3. Phenotypes

Source: the search summary of Kornak 2022, n=5. Frequencies are the cohort counts as I could infer them, not confirmed against the paper's tables.

| Phenotype | Frequency | Suggested HPO (lookup required) |
|---|---|---|
| Corneal clouding | all 5 | Corneal opacity |
| Cataract | at least 1 (A3) | Cataract |
| Sensorineural hearing loss, progressive | reported in the cohort; 2 had cochlear implants | Sensorineural hearing impairment |
| Achalasia, causing feeding problems | reported in the cohort | Achalasia |
| Lipodystrophy / progeroid appearance | defining feature | Generalized lipodystrophy; Progeroid facial appearance |
| Muscular hypotonia | reported | Hypotonia |
| Sensory neuropathy | reported | Sensory neuropathy |
| Stunted growth | 3 of 5 (A1–A3) | Growth delay |
| Intellectual disability | A1–A3; the adults A4–A5 have normal intellect | Intellectual disability |

- **Onset.** Childhood; OMIM/MalaCards place onset from about the second year of life into late childhood.
- **Severity and progression.** Variable, with an early-death subgroup and a milder adult subgroup. Hearing loss and lipodystrophy are progressive.
- **Quality of life.** No validated instruments were found. Qualitative burden includes feeding difficulty from achalasia, deafness needing cochlear implants, and visual impairment.

## 4. Genetic/molecular information

- **Gene.** *BUD13* (BUD13 homolog; OMIM 620691). The HGNC ID was not retrieved, so look it up for the `hgnc:` CURIE.
- **Variant.** NM transcript not confirmed. c.688C>T, p.Arg230*. ACMG classification and gnomAD frequency were not checked.
- **Origin.** Germline, homozygous.
- **Consequence.** The nonsense variant triggers use of a cryptic splice site, giving a truncated, stable protein with partial function. This turns what would be a null allele into a hypomorph.
- **Founder effect.** The same variant occurs in Algerian (two consanguineous families, three patients) and Portuguese (two adults) families. A founder or recurrent-variant explanation is plausible, but I saw no haplotype data.
- **Modifiers, epigenetics, chromosomal abnormalities.** None reported.

## 5. Environmental information

No environmental, lifestyle or infectious factors are reported. Leave `environmental:` empty.

## 6. Mechanism / pathophysiology

**Causal chain (the inferred steps are marked).**
1. A homozygous *BUD13* c.688C>T (p.Arg230*) variant arises in a consanguineous or founder context. Demonstrated.
2. The nonsense variant leaves little full-length BUD13 and activates a cryptic splice site, producing a truncated protein (S1) that is stable and partly functional. Demonstrated in patient cells per the summary.
3. Reduced BUD13 function impairs the RES (retention and splicing) complex. RES has three components: BUD13, Snu17/RBMX2 and Pml1/SNIP1. This step is inferred from the yeast and zebrafish literature and was not directly measured in the patients.
4. Impaired RES function causes widespread splicing defects. These are concentrated in introns that are short and GC-rich, which points to a defect in intron definition. Shown in zebrafish RES mutants ([Fernandez et al., PLoS Genet 2018](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6047831/)). Applying it to human tissue is an inference.
5. Splicing disruption leads to tissue-specific dysfunction (inferred). The affected tissues are adipose (lipodystrophy), cornea and lens, cochlea, esophageal myenteric neurons, and the nervous system. Which transcripts matter is not identified in what I read.
6. The result is the clinical syndrome. Residual S1 isoform level modulates severity (branch: low S1 gives early death and intellectual disability, high S1 gives survival to adulthood with normal intellect).

**Model evidence.**
- The RES complex is required in zebrafish early embryogenesis. Loss-of-function mutants for each of its three components showed early developmental defects, with more brain cell death and fewer differentiated neurons ([PMC6047831](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6047831/)).
- In mice, reduced Bud13 expression caused early embryonic lethality. A line with an N-terminal frameshift produced viable chimeras that developed lipoatrophy and early death, per a search summary of a source whose journal was not named.

**Not found.** Any transcriptomic, proteomic, single-cell or other omics data on patient tissue was not seen beyond the splicing analysis above.

**Suggested ontology terms (all need lookup).**
- GO: mRNA splicing, via spliceosome; the RES complex cellular component.
- CL: adipocyte, corneal endothelial cell, cochlear hair cell, enteric neuron. These are hypotheses, not shown for this disease.

## 7. Anatomical structures affected

- **Organs and systems.** Eye (cornea, lens), ear (cochlea), esophagus (lower esophageal sphincter), subcutaneous adipose tissue, and the nervous system.
- **Distribution.** Presumably bilateral and systemic. No lateralization is reported.

## 8. Temporal development

- **Onset.** Childhood. Lipodystrophy and corneal clouding appear early.
- **Course.** Progressive. Three patients died in childhood (first decade), and two reached adulthood.
- **Remission or critical periods.** None described.

## 9. Inheritance and population

- **Inheritance.** Autosomal recessive.
- **Epidemiology.** Prevalence and incidence are unknown. Only five patients from four families are reported.
- **Population.** Algerian and Portuguese families. No sex ratio data.
- **Penetrance and expressivity.** Complete in these families, with variable expressivity linked to S1 isoform level.
- **Carrier frequency.** Not available.

## 10. Diagnostics

- **Genetic testing.** Exome or genome sequencing, or a gene panel covering *BUD13*. Targeted testing for c.688C>T is reasonable in families of Algerian or Portuguese origin, though this is an inference from a very small cohort.
- **Clinical workup.** Ophthalmology (slit lamp), audiometry, esophageal manometry or barium swallow for achalasia, and growth and body composition assessment.
- **Differential diagnosis.** Triple A syndrome (*AAAS*), Wiedemann–Rautenstrauch/neonatal progeroid syndrome, Hutchinson–Gilford progeria and other laminopathies, mandibuloacral dysplasia, *GMPPA*-CDG (infantile achalasia with alacrima, no progeroid features), and *SLC4A11* corneal dystrophy with deafness. Distinguishing features are not systematically described in the sources I saw.
- **Not found.** Biomarkers, GeneReviews chapter, screening programs and diagnostic criteria. A GeneReviews chapter was not found in my searches, but that is not a verified absence.

## 11. Outcome/prognosis

Three of five patients died in the first decade of life. The two adults had normal intellectual development ([Genet Med 2022](https://www.gimjournal.org/article/S1098-3600(22)00759-6/fulltext), per the search summary). Prognostic factor: residual S1 isoform expression. There are no registry, survival-curve or quality-of-life data.

## 12. Treatment

- **Disease-specific therapy.** None. No clinical trials were found.
- **Supportive care.** Cochlear implantation for hearing loss (two patients). Management of achalasia, such as pneumatic dilation, Heller myotomy or POEM, is standard practice for achalasia but is not documented for these patients. Ophthalmic management of corneal clouding and cataract, and nutritional support.
- **Suggested NCIT terms (lookup required).** Surgical procedure, rehabilitation, supportive care.
- **Speculative.** The S1 isoform finding suggests that splice-modulating approaches, such as antisense oligonucleotides that favor cryptic-site use, are conceivable. This is my inference, and nothing in the literature I found proposes it.

## 13. Prevention

- Genetic counseling and cascade testing in families with a known variant.
- Carrier testing and prenatal or preimplantation diagnosis once a familial variant is known.
- No primary prevention.

## 14. Other species / natural disease

- *BUD13* orthologs exist in zebrafish, mouse, rat ([RGD](https://rgd.mcw.edu/rgdweb/report/gene/main.html?id=1308076)) and yeast (Bud13p).
- I found no naturally occurring animal disease (OMIA not checked).

## 15. Model organisms

- **Zebrafish.** RES loss-of-function mutants (including *bud13*) have early developmental defects, with neuronal cell death and widespread splicing defects ([PLoS Genet 2018](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6047831/)). These are null-type models, so they capture severe loss of function but not the human hypomorph.
- **Mouse.** CRISPR-engineered lines produced truncated Bud13 variants. Reduced Bud13 expression gave early embryonic lethality. One N-terminal frameshift line gave viable chimeras with lipoatrophy and early death, which resembles the human lipodystrophy. This is the model closest to human disease. It comes from a summary I could not trace to a named paper, so identify the paper before citing it.
- **Yeast.** The RES complex acts in the first catalytic step of splicing and affects splicing across the transcriptome.
- **Limitations.** The N-terminus of BUD13 is poorly conserved and absent in yeast, so model fidelity to the human truncated isoform is uncertain. For the KB this fits a `HUMAN_MODEL_MISMATCH` discussion and `modeled_mechanisms` links with a limitations note.

## Gaps to close before curation

1. Read the Kornak 2022 abstract and full text from PubMed and PMC, and confirm the PMID. Check patient counts, per-feature frequencies, ages and the lipodystrophy description.
2. Resolve the MONDO ID, Orphanet code and HGNC ID.
3. Identify the mouse paper behind the CRISPR/chimera findings.
4. Search for any further patients since 2022.

**Sources**
- [OMIM #621123](https://omim.org/entry/621123)
- [OMIM *620691](https://omim.org/entry/620691)
- [MalaCards](https://malacards.org/card/achalasia_progeroid_syndrome)
- [Genetics in Medicine](https://www.gimjournal.org/article/S1098-3600(22)00759-6/fulltext)
- [Refubium](https://refubium.fu-berlin.de/handle/fub188/32282)
- [PLoS Genet 2018](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6047831/)
- [RGD](https://rgd.mcw.edu/rgdweb/report/gene/main.html?id=1308076)
- [Monarch](https://monarchinitiative.org/MONDO:0015333)
- [GMPPA-CDG case report](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9283290/)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 3 |
| Resolved | 1 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 2 |
| References weighed for topical relevance | 1 |
| On topic | 1 |
| Off topic | 0 |

1 of 3 references resolved; the rest could not be looked up either way.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 2 |
| Resolved | 2 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.