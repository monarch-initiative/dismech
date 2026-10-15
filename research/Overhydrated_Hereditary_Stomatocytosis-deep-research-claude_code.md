---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-15T03:58:15.561289'
end_time: '2026-10-15T03:59:15.357506'
duration_seconds: 59.8
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Overhydrated Hereditary Stomatocytosis
  mondo_id: MONDO:0008493
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
  web_search_requests: 3
  num_turns: 5
  total_cost_usd: 0.7966371999999999
  session_id: 6f407ab6-10d8-510b-8a76-b165dbc02479
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 9
reference_validation:
  total_references: 5
  verified: 5
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 0
  quotes_valid: 0
  quotes_not_checkable: 1
  relevance_assessed: 5
  on_topic: 2
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
- **Disease Name:** Overhydrated Hereditary Stomatocytosis
- **MONDO ID:** MONDO:0008493 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Overhydrated Hereditary Stomatocytosis** covering all of the
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

# Overhydrated Hereditary Stomatocytosis (OHSt): research report

**Scope and verification.** I ran three web searches and read search summaries only. I did not open the full text of any paper. These items came back from search results:
- Bruce 2009, PMID 18931342.
- The Haematologica 2011 metabolomics report.
- The 2018 Frontiers review.
- The 2019 *J Blood Med* review (PMC6613601).
- The GeneBe/ClinGen-style gene summary.

Everything else is background knowledge and is marked **[unverified]**. Treat it as a lead until a snippet has been checked with `just fetch-reference`. I did not retrieve exact abstract quotes, so none appear below. I did not look up any ontology identifier, so every HP, GO, CL, UBERON, CHEBI and NCIT term is a **search suggestion by label only** and has no CURIE. Look each one up with OAK or the term caches before binding it.

## 1. Disease information

- OHSt is a rare, autosomal dominant congenital hemolytic anemia. It belongs to the "cation-leak" hereditary stomatocytoses, together with dehydrated stomatocytosis (xerocytosis, mainly PIEZO1) and the other leak forms. ([Frontiers 2018](https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2018.00367/full))
- Red cells are swollen (high MCV, low MCHC). A summary of the pathogenesis says: "The influx of Na+ exceeds the loss of K+ causing water influx and resulting in swollen erythrocytes, hemolysis, and stomatocyte formation." ([Frontiers 2018](https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2018.00367/full))
- **Identifiers.** The MONDO ID you gave (MONDO:0008493) was not checked. OMIM, Orphanet, ICD-10/11 and MeSH identifiers are not verified either; look them up directly. KEGG has an entry (H01979), found by search: [KEGG](https://www.kegg.jp/entry/H01979).
- **Synonyms:** overhydrated stomatocytosis; hydrocytosis; OHSt; hereditary stomatocytosis with overhydration. Related labels you will meet in the same sources are "Rh-null disease, regulator type" and "Rh deficiency syndrome". These are separate recessive conditions, not synonyms.
- **Data level:** the evidence is aggregated disease-level resources and case series. It is not EHR-derived.

## 2. Etiology

- **Cause:** heterozygous missense variants in *RHAG*, which encodes the Rh-associated glycoprotein. Search results describe overhydrated stomatocytosis as "mainly caused by RHAG gene mutations, and milder forms have been linked to SLC4A1 variants". ([J Blood Med 2019, PMC6613601](https://pmc.ncbi.nlm.nih.gov/articles/6613601/))
- **Landmark paper:** Bruce LJ et al., *Blood* 2009, PMID 18931342, "The monovalent cation leak in overhydrated stomatocytic red blood cells results from amino acid substitutions in the Rh-associated glycoprotein." ([abstract mirror](https://www.qxmd.com/r/18931342))
  - Search results report that "DNA analysis revealed that the OHSt patients have 1 of 2 heterozygous mutations (t182g, t194c) in RHAG that lead to substitutions of 2 highly conserved amino acids (Ile61Arg, Phe65Ser)."
  - They also report that expressing the mutant proteins in *Xenopus* oocytes gave a cation leak about six times greater than wild type.
- **Further variants:** later reports describe additional *RHAG* missense variants (for example p.Phe65Ser and others) **[unverified]**. Please search ClinVar and the literature for the current list.
- **Risk and protective factors:**
  - No environmental risk factors or protective factors are known **[unverified]**.
  - No gene–environment interaction data were found.
  - Inheritance is dominant, and many cases are reported as de novo **[unverified]**.
- **Modifiers:** not characterised in anything I retrieved.

## 3. Phenotypes

Clinical features reported for the stomatocytosis group ([J Blood Med 2019](https://pmc.ncbi.nlm.nih.gov/articles/6613601/)):
- jaundice
- pallor
- fatigue
- splenomegaly
- gallstones

Suggested HPO labels (look up IDs):
- Hemolytic anemia
- Macrocytosis, with high MCV
- Low MCHC
- Stomatocytosis / abnormal erythrocyte morphology
- Splenomegaly
- Jaundice
- Cholelithiasis
- Reticulocytosis
- Neonatal hyperbilirubinemia **[unverified]**
- Iron overload **[unverified]**

Other points:
- **Severity** is variable, from compensated hemolysis to transfusion-dependent anemia.
- **Onset** is neonatal to childhood.
- **Frequencies** and **quality-of-life data** were not found. Do not invent them.
- Perinatal fluid effusions and thrombosis are mentioned in the 2019 review for the stomatocytosis group. I could not tell from the summary which subtype each applies to.

## 4. Genetic and molecular information

- **Gene:** *RHAG* (chromosome 6p21.3 **[unverified]**). Use the lowercase `hgnc:` form in the KB, and look up the HGNC ID rather than writing it from memory.
- **Variants:** Ile61Arg (c.182T>G) and Phe65Ser (c.194T>C), both affecting conserved transmembrane residues. ([Bruce 2009](https://www.qxmd.com/r/18931342))
- **Functional consequence:** the mutant protein induces a monovalent cation leak. The authors note that RhAG belongs to the ammonium transporter family, whose members form pore-like structures. Their modelling suggested the mutations open that pore. ([Bruce 2009](https://www.qxmd.com/r/18931342))
  - Candidate class: a gain-of-function neomorphic leak, not simple loss of function. Bind `functional_impact_category` only if a source states it.
- **Allelic disease:** biallelic *RHAG* variants cause Rh-null (regulator type) hemolytic anemia, which is autosomal recessive and a different entity. ([GeneBe summary](https://genebe.net/gene/hg38/RHAG))
- **Origin:** germline.
- **Allele frequency:** not retrieved.
- **Other genes:** *SLC4A1* has been linked to milder overhydrated-like phenotypes. ([J Blood Med 2019](https://pmc.ncbi.nlm.nih.gov/articles/6613601/)) A second report says OHSt is "frequently linked to mutations in genes that encode components of the band 3 complex, such as RHAG". ([Haematologica 2011](https://haematologica.org/article/view/5311/23268)) Check whether any of these belong in separate entries.
- **Epigenetic or chromosomal features:** none identified.

## 5. Environmental information

None are known. There are no established toxin, lifestyle or infectious triggers in anything retrieved.

## 6. Mechanism and pathophysiology

**Ordered causal chain**
1. A heterozygous missense variant in *RHAG* (Ile61Arg or Phe65Ser) alters a conserved transmembrane residue. This is demonstrated. ([Bruce 2009](https://www.qxmd.com/r/18931342))
2. The altered Rh-associated glycoprotein, which is part of the Rh/ankyrin-R/band 3 complex, forms or opens a pore-like cation pathway. This is demonstrated by *Xenopus* oocyte expression (about 6-fold leak) and supported by structural modelling.
3. The pathway lets monovalent cations (Na⁺ and K⁺) cross the red cell membrane.
4. Na⁺ influx exceeds K⁺ loss, so net cation gain draws water into the cell. This is demonstrated. ([Frontiers 2018](https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2018.00367/full))
5. Compensatory Na⁺/K⁺-ATPase activity rises. It consumes ATP and glycolytic capacity, and a 2011 metabolomic study of four patients reported "glycolysis is exhausted", with ADP, pyruvate, lactate and malate accumulating. ([Haematologica 2011](https://haematologica.org/article/view/5311/23268)) That study also suggests transporter abnormalities or unrecognised oxidative stress. This step is inferred from small-sample data.
6. The cells swell, take a cup shape (stomatocytes) and have reduced deformability. Why the cup shape forms is unknown.
7. The spleen removes the abnormal cells, which leads to extravascular hemolysis. This is inferred.
8. Chronic hemolysis causes anemia, jaundice, splenomegaly and pigment gallstones. Iron overload can follow **[unverified]**.

**Suggested terms (labels only):**
- GO: monovalent inorganic cation transport; ammonium transmembrane transport; cell volume homeostasis; potassium ion import across plasma membrane.
- CL: erythrocyte.
- Cellular component: plasma membrane, and the Rh complex if a GO term exists.

**Not available:** no transcriptomics, proteomics, single-cell or CRISPR-screen data were found.

## 7. Anatomical structures affected

- **Primary:** red blood cell membrane. Blood and bone marrow are the main systems involved.
- **Secondary:** spleen (extravascular hemolysis), liver and biliary tract (gallstones), and liver, heart and endocrine organs if iron overload develops **[unverified]**.
- **Subcellular:** plasma membrane.
- Suggested UBERON terms (labels): blood, spleen, gallbladder.
- **Lateralization:** not applicable.

## 8. Temporal development

- **Onset:** congenital, with variable presentation from neonatal to childhood.
- **Course:** lifelong, chronic, and stable or episodic with infections **[unverified]**.
- **Remission:** none.
- **Critical periods:** not described in the retrieved material.

## 9. Inheritance and population

- **Inheritance:** autosomal dominant. Bind the HPO mode-of-inheritance term after looking it up.
- **Prevalence:** very rare. The prevalence of the stomatocytosis disorders is uncertain because diagnosis is difficult. ([Marcello, Pediatr Blood Cancer 2023](https://iris.unisr.it/retrieve/13484c22-40b0-4f7f-9e32-eb4416cbf3ca/Marcello_Pediatric%20Blood%20Cancer_2023.pdf)) Do not put a number in `rate_per_100000` unless Orphanet gives one. Orphanet was not reached.
- **Penetrance, expressivity, founder effects, sex ratio:** not retrieved.

## 10. Diagnostics

- **Blood film:** stomatocytes. Reported lab findings, which I did not verify in detail, are high MCV, low MCHC, reticulocytosis and raised bilirubin.
- **Osmotic fragility / ektacytometry:** the osmotic gradient ektacytometry curve is shifted. Specialised tests are needed to separate this from other stomatocytoses **[unverified]**.
- **Red cell cation content and flux:** high Na⁺ with low K⁺ is described for the group **[unverified]**.
- **Genetic testing:** a gene panel for hereditary hemolytic anemia including *RHAG*, *PIEZO1*, *KCNN4*, *GARDOS*-related genes and *SLC4A1* is the usual approach **[unverified]**. Check GTR and ClinGen for panels.
- **Differential diagnosis:** dehydrated stomatocytosis (PIEZO1), hereditary spherocytosis, Rh-null disease, and acquired stomatocytosis (for example alcohol-related).
- **Screening:** no newborn screening program is known.

## 11. Outcome and prognosis

- Prognosis is variable and survival data were not retrieved.
- Complications reported for the group include gallstones, iron overload and thrombosis. ([J Blood Med 2019](https://pmc.ncbi.nlm.nih.gov/articles/6613601/))
- Prognostic factors and biomarkers: not found.

## 12. Treatment

- **Supportive care:** transfusion when needed, folate supplementation **[unverified]**, monitoring for iron overload, and chelation if iron overload develops **[unverified]**. Suggested NCIT labels: Supportive Care, Red Blood Cell Transfusion, Iron Chelation Therapy.
- **Splenectomy should be avoided.** A 2019 review says no specific treatment for symptomatic hemolysis exists and that splenectomy "should be avoided as it seems to aggravate the risk of thrombosis". ([J Blood Med 2019](https://dx.doi.org/10.2147/jbm.s179764)) A 1999 case report describes portal vein thrombosis after splenectomy in a child with dehydrated stomatocytosis. ([PMID 10445340](https://www.qxmd.com/r/10445340)) A gene summary notes that individuals with OHSt may be prone to iron overload and post-splenectomy thrombotic complications, and that splenectomy may be less beneficial in this form. ([GeneBe](https://genebe.net/gene/hg38/RHAG)) The evidence is mostly case reports and case series.
- No gene therapy, targeted therapy or clinical trial was identified. I did not search ClinicalTrials.gov.
- Do not add a `therapeutic_agent` unless a source names one.

## 13. Prevention

- Genetic counselling for an autosomal dominant condition.
- Avoid splenectomy as above, and use thrombosis precautions if it cannot be avoided **[unverified]**.
- Iron-overload surveillance.
- No vaccination or public health measures are known to be relevant.

## 14. Other species

I did not search OMIA, so nothing is established here. A naturally occurring stomatocytosis exists in dogs (Alaskan malamute and Drentse patrijshond) with a different mechanism **[unverified]**. Check OMIA before using it.

## 15. Model organisms

- The *Xenopus laevis* oocyte expression system was used to show the 6-fold cation leak. This is a heterologous in vitro system, so grade it `IN_VITRO` and not `MODEL_ORGANISM`. ([Bruce 2009](https://www.qxmd.com/r/18931342))
- I found no knockin mouse, zebrafish or iPSC model of OHSt. Check MGI and the Alliance of Genome Resources before stating that none exists.
- Limitations to record: oocytes lack the red cell cytoskeleton and Rh/ankyrin-R/band 3 complex context, so they are a boundary-omission divergence.

## Gaps to close before curation

1. Pull the Bruce 2009 abstract with `just fetch-reference PMID:18931342` and quote it verbatim.
2. Look up the Orphanet and OMIM entries for the identifiers, prevalence and phenotype frequencies.
3. Read GeneReviews and ClinGen for the *RHAG* gene–disease validity tier. Copy the tier, do not assign it.
4. Look up every ontology CURIE with OAK.
5. Confirm the splenectomy claims with abstract-level snippets. The 2019 review and the 1999 case report concern the wider stomatocytosis group, so check what applies to OHSt specifically.

## Sources

- [Bruce et al., Blood 2009 (PMID 18931342)](https://www.qxmd.com/r/18931342)
- [Haematologica 2011 report](https://haematologica.org/article/view/5311/23268)
- [Frontiers in Physiology 2018 review](https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2018.00367/full)
- [J Blood Med 2019 review (PMC6613601)](https://pmc.ncbi.nlm.nih.gov/articles/6613601/)
- [J Blood Med 2019, full text](https://dx.doi.org/10.2147/jbm.s179764)
- [Splenectomy case report, 1999 (PMID 10445340)](https://www.qxmd.com/r/10445340)
- [Marcello, Pediatr Blood Cancer 2023](https://iris.unisr.it/retrieve/13484c22-40b0-4f7f-9e32-eb4416cbf3ca/Marcello_Pediatric%20Blood%20Cancer_2023.pdf)
- [GeneBe, RHAG](https://genebe.net/gene/hg38/RHAG)
- [KEGG H01979](https://www.kegg.jp/entry/H01979)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 0 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 0 |
| Quoted claims with nothing to check against | 1 |
| References weighed for topical relevance | 5 |
| On topic | 2 |
| Off topic | 0 |

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `DOI:10.3389/fphys.2018.00367`: "The influx of Na+ exceeds the loss of K+ causing water influx and resulting in swollen erythrocytes, hemolysis, and stomatocyte formation."
  - Reference resolved but exposes no abstract or full text to search

All extracted references resolved successfully.

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