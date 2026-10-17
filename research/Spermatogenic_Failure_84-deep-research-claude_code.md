---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-16T13:11:56.314437'
end_time: '2026-10-16T13:13:28.451833'
duration_seconds: 92.14
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Spermatogenic Failure 84
  mondo_id: MONDO:0957301
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
  web_search_requests: 5
  num_turns: 12
  total_cost_usd: 0.8073137999999999
  session_id: e0e00ff6-67e7-5e60-9592-3e4cb1004f09
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 12
reference_validation:
  total_references: 7
  verified: 6
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.143
  relevance_assessed: 6
  on_topic: 4
  unresolved_references:
  - DOI:10.1242/dev.199805/2120252/dev199805.pdf
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 1
  verified: 1
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
- **Disease Name:** Spermatogenic Failure 84
- **MONDO ID:** MONDO:0957301 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spermatogenic Failure 84** covering all of the
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

I'm still gathering primary-literature details on CFAP61 (the gene behind SPGF84). The PubMed and PMC pages are blocked, so I'm looking for PMIDs and abstracts elsewhere.

# Spermatogenic Failure 84 (SPGF84): research report

**Reliability note.** This report comes from web searches only. PubMed, PMC and the Development PDF were blocked or rate-limited, so I read no abstract or full text directly. The facts below come from search-result summaries and aggregator pages.

- **No quotes:** I give no exact abstract quotes. Any snippet written for the KB must be taken from `just fetch-reference` output.
- **PMIDs:** only PMID 35387802 was seen in a search result. The other papers are cited by DOI or title, and their PMIDs still need to be fetched.
- **Ontology IDs:** I give only labels for HPO, GO, CL, UBERON and NCIT terms. Look up every CURIE with `runoak` or the cache before binding it.

## 1. Disease information

SPGF84 is an autosomal recessive form of male infertility caused by biallelic loss-of-function variants in **CFAP61**. The main feature is **multiple morphological abnormalities of the sperm flagella (MMAF)**, which severely reduce motility. Some men also have reduced sperm counts.

- **Identifiers** ([NCBI MedGen C5830562](https://https.ncbi.nlm.nih.gov/medgen/C5830562)):
  - OMIM #620409
  - MONDO:0957301
  - gene locus 20p11.23
- **Ontology placement:** MONDO places it under spermatogenic failure, as a reproductive system disorder ([SAIL Concept Library](https://conceptlibrary.saildatabank.com/api/v1/ontology/node/MONDO:0957301/)).
- **Other resources:** [KEGG spermatogenic failure H01282](https://www.kegg.jp/entry/H01282) and [MalaCards](https://malacards.org/card/spermatogenic_failure_84) list the entry.
- **Synonyms and series:** SPGF84; CFAP61-related MMAF; asthenoteratozoospermia due to CFAP61. It belongs to the numbered SPGF series, which is heterogeneous, and many of its members are flagellar or MMAF genes.
- **Source type:** disease-level and aggregated, built from small family and cohort studies.
- **Not found:** Orphanet and ICD identifiers. Check these directly.

## 2. Etiology

- **Cause:** homozygous or compound heterozygous CFAP61 variants ([MalaCards via Disease Ontology](https://malacards.org/card/spermatogenic_failure_84)).
- **Environmental risk factors:** none established. Other causes of male infertility must be excluded in the differential.
- **Protective factors and gene-environment interactions:** none reported.
- **Possible modifiers:** other axonemal genes, such as CFAP251, appear to be involved downstream. That is a mechanistic link, not a demonstrated modifier effect.

## 3. Phenotypes

Male-limited phenotypes (candidate HPO labels, all to be verified):

| Phenotype | Notes |
|---|---|
| Male infertility | Universal. Onset becomes apparent in adulthood. Stable. |
| Asthenozoospermia | Severely reduced progressive motility. |
| Teratozoospermia, with short, absent, coiled, bent or irregular flagella (MMAF) | Core feature ([MedGen](https://https.ncbi.nlm.nih.gov/medgen/C5830562)). |
| Oligozoospermia | Seen in some men, so the sperm count varies. |

- **Cohort observation:** in the [J Med Genet cohort](https://pubmed.ncbi.nlm.nih.gov/35387802/), two of 325 men with oligoasthenoteratozoospermia (OAT), 0.62%, carried biallelic CFAP61 variants.
- **Other organs:** no primary ciliary dyskinesia (PCD) features are described. The mouse knockout lacks the usual PCD symptoms.
- **Frequencies and quality of life:** no per-phenotype frequencies or quality-of-life data are available. Infertility is expected to have psychosocial impact, but I found no study.

## 4. Genetic and molecular information

- **Gene:** CFAP61 (cilia and flagella associated protein 61, also C20orf26), 20p11.23. A homolog of the radial spoke protein Rsp19. HGNC ID not retrieved. Look it up and write it in lowercase `hgnc:` form.
- **Reported variants:**
  - **Pakistani families (Ma et al., Frontiers in Cell and Developmental Biology, [DOI 10.3389/fcell.2021.803818](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8841411/)):**
    - 11 infertile men in three unrelated families.
    - c.451_452del (p.I151Nfs*4) in family 1.
    - c.847C>T (p.R283*) in families 2 and 3.
    - Both variants truncate the protein.
  - **Splice variant:** c.143+5G>A causes exon skipping (Liu et al., Development 2021, [DOI 10.1242/dev.199805](https://cob.silverchair.com/dev/article-pdf/doi/10.1242/dev.199805/2120252/dev199805.pdf)).
  - **Later reports:** a novel homozygous splicing variant ([J Assist Reprod Genet 2024](https://link.springer.com/article/10.1007/s10815-024-03139-0)) and two of 325 OAT men in the J Med Genet cohort.
- **Consequence:** loss of function (truncation or exon skipping). No dominant-negative or gain-of-function mechanism is known.
- **Origin:** germline.
- **Not retrieved:** ClinVar and ClinGen classifications, gnomAD frequencies, ClinGen gene-disease validity, and epigenetic or chromosomal findings. Check `just check-gene-validity` and ClinGen before recording any tier.

## 5. Environmental information

None known. No infectious agents and no lifestyle factors are linked.

## 6. Mechanism and pathophysiology

1. Biallelic CFAP61 loss-of-function variants (truncating or splicing) reduce or abolish CFAP61 protein in the testis.
2. CFAP61 is a component of the calmodulin- and radial-spoke-associated complex (CSC) in the axoneme. This is a conserved role, described in a [bioRxiv preprint of the Development paper](https://www.biorxiv.org/content/10.1101/2021.03.04.433881.full.pdf).
3. Early in spermiogenesis, radial spoke assembly is impaired in Cfap61-/- mice (preprint, mouse data).
4. The axoneme becomes unstable and scatters. The distribution of intraflagellar transport (IFT) proteins is disrupted (preprint, mouse data).
5. In patient sperm, the central pair and radial spokes are missing and the axonemes are disorganized. CFAP61 and CFAP251 signals are absent from the tail (Frontiers 2021). The J Med Genet cohort also found missing central pair microtubules and mitochondrial sheath malformation.
6. The result is short, coiled or absent flagella with no progressive motility, which leads to male infertility. The step from structural defect to loss of motility is inferred, not separately demonstrated.

- **Cells:** spermatid and spermatozoon, in the seminiferous epithelium of the testis.
- **Cell component:** the sperm flagellar axoneme, radial spoke and central pair (GO labels to verify).
- **Not available:** omics, single-cell, metabolomic and CRISPR screen data.
- **Possible Leydig cell link:** one paper reports that CFAP61 knockdown reduced Leydig cell testosterone via the MAPK/COX-2 pathway ([Funct Integr Genomics 2023](https://link.springer.com/article/10.1007/s10142-023-01271-1)). This is a cell-line finding that needs corroboration.

## 7. Anatomical structures affected

Testis and seminiferous tubules, with spermatids as the target cells. The sperm flagellum (axoneme, mitochondrial sheath) is the affected structure. The condition is male-limited and systemic involvement is not described.

## 8. Temporal development

Congenital genotype. Infertility presents in adulthood, during attempts to conceive. It does not progress and is lifelong. No remission is reported.

## 9. Inheritance and population

- **Inheritance:** autosomal recessive.
- **Consanguinity:** the Pakistani families suggest a role for consanguinity (homozygous variants), but I did not verify this in the paper.
- **Population:** Pakistani families, Chinese cohorts and others.
- **Prevalence:** not established. About 0.6% of OAT men in one cohort.
- **Sex ratio:** affects males only.
- **Not retrieved:** carrier frequency, founder effects, penetrance and expressivity.

## 10. Diagnostics

- **Semen analysis:** severe asthenoteratozoospermia, with a high proportion of MMAF flagella. Counts vary.
- **Electron microscopy:** disorganized axonemes. Findings in the cohorts include missing central pair, radial spokes and inner dynein arms.
- **Immunofluorescence:** absent CFAP61 and CFAP251 signals in sperm tails.
- **Genetic testing:** exome or MMAF/asthenoteratozoospermia gene panel with CFAP61 included. Confirm biallelic variants. A [sample report from Arcensus Diagnostics](https://www.arcensus-diagnostics.com/wp-content/uploads/Arcensus_SampleReport_WGS-Positive.pdf) notes ICSI is likely to be effective. It is a commercial sample, not primary evidence.
- **Differential:**
  - Other MMAF genes (DNAH1, CFAP43, CFAP44, CFAP69, CFAP251 and others).
  - PCD (check for respiratory symptoms).
  - Acquired causes of OAT.

## 11. Outcome and prognosis

Fertility is impaired, but general health is not affected as far as is known. Natural fertilization is unlikely. No survival or mortality data are available.

## 12. Treatment

- **ICSI** (intracytoplasmic sperm injection; NCIT term to look up) is the main option. One affected man fathered a healthy baby by ICSI in the J Med Genet cohort ([PMID 35387802](https://pubmed.ncbi.nlm.nih.gov/35387802/)). The Arcensus report cites 100% fertilization in treated probands, which is a weak source.
- **Genetic counseling.** There is no drug, gene or cell therapy and no clinical trial that I found.
- **Possible concern:** whether sperm quality can support ICSI success depends on the individual. The outcomes cited are from very small numbers.

## 13. Prevention

There is no primary prevention. Options are genetic counseling and carrier testing of relatives. For couples using ICSI, preimplantation or prenatal testing is possible, though the heritable risk to a child is that of a carrier (recessive), and a male child homozygous for the variant would also be infertile.

## 14. Other species and natural disease

I found no natural disease report (not checked in OMIA). The mouse ortholog is Cfap61 (NCBI Gene IDs not retrieved).

## 15. Model organisms

- **Mouse knockout (Cfap61-/-):**
  - Male sterility with MMAF (Liu et al., Development 2021, [DOI 10.1242/dev.199805](https://cob.silverchair.com/dev/article-pdf/doi/10.1242/dev.199805/2120252/dev199805.pdf); [preprint](https://www.biorxiv.org/content/10.1101/2021.03.04.433881.full.pdf)).
  - An earlier knockout paper ([ScienceDirect, "Absence of murine CFAP61 causes male infertility due to MMAF"](https://www.sciencedirect.com/science/article/abs/pii/S2095927320300475)).
  - The J Med Genet cohort paper used knockout mice with an OAT phenotype.
  - The preprint says the mice lack the PCD symptoms usually seen with cilia genes.
- **Fidelity:** the mouse reproduces the male-infertility MMAF phenotype well. It is a loss-of-function model and does not cover human genotype-specific variation.
- **Not checked:** MGI or IMPC records, zebrafish and other models, and organoids.

## Suggested KB follow-ups

1. Run `just fetch-reference` for each paper (PMID 35387802 first, then look up the PMIDs of the Ma 2021/2022, Liu 2021 and 2024 splice-variant papers).
2. Quote evidence snippets only from the cached text.
3. Look up every ontology CURIE (MONDO:0957301 is from MedGen and MONDO's own listing) and the lowercase `hgnc:` ID for CFAP61.
4. Check ClinGen, GeneReviews and Orphanet before adding gene validity or a baseline phenotype.

## Sources

- [NCBI MedGen C5830562](https://https.ncbi.nlm.nih.gov/medgen/C5830562)
- [SAIL Concept Library: MONDO:0957301](https://conceptlibrary.saildatabank.com/api/v1/ontology/node/MONDO:0957301/)
- [MalaCards: SPGF84](https://malacards.org/card/spermatogenic_failure_84)
- [KEGG H01282](https://www.kegg.jp/entry/H01282)
- [Ma et al. 2021, Frontiers (PMC8841411)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8841411/)
- [Liu et al. 2021, Development](https://cob.silverchair.com/dev/article-pdf/doi/10.1242/dev.199805/2120252/dev199805.pdf) and its [bioRxiv preprint](https://www.biorxiv.org/content/10.1101/2021.03.04.433881.full.pdf)
- [J Med Genet, PMID 35387802](https://pubmed.ncbi.nlm.nih.gov/35387802/)
- [Splice variant report, J Assist Reprod Genet 2024](https://link.springer.com/article/10.1007/s10815-024-03139-0)
- [CFAP61 knockdown and Leydig cells, 2023](https://link.springer.com/article/10.1007/s10142-023-01271-1)
- [Murine CFAP61 knockout, ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S2095927320300475)
- [Arcensus sample WGS report](https://www.arcensus-diagnostics.com/wp-content/uploads/Arcensus_SampleReport_WGS-Positive.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 4 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `DOI:10.1242/dev.199805/2120252/dev199805.pdf` (4 mentions) - Identifier did not resolve to a record

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 1 |
| Resolved | 1 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.