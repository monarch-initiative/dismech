---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5-5
cached: false
start_time: '2026-10-05T13:59:38.771543'
end_time: '2026-10-05T14:00:42.140922'
duration_seconds: 63.37
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: 5-Fluorouracil Poisoning
  mondo_id: MONDO:0016312
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
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5-5
  web_search_requests: 3
  num_turns: 5
  total_cost_usd: 0.725805
  session_id: 68ee5478-082d-5a81-aae3-c2c1854f6b8b
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 15
reference_validation:
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 11
  on_topic: 2
  off_topic: 2
  off_topic_references:
  - PMC:PMC7013286
  - PMC:PMC4170068
  needs_review: true
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 4
  verified: 4
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 1
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** 5-Fluorouracil Poisoning
- **MONDO ID:** MONDO:0016312 (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **5-Fluorouracil Poisoning** covering all of the
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

# 5-Fluorouracil Poisoning: Research Report for dismech Curation

**Scope and verification.** I ran three web searches (below). Claims tied to a URL come from those results. PMIDs appear only where a source showed them: PMID:29152729 and PMID:23988873. Items marked **[background, unverified]** come from general pharmacology knowledge, not from a source I retrieved. They need `just fetch-reference` and exact-snippet verification before they go into the KB. All CURIEs here are suggestions that have not been looked up. Per the dismech rules, look each one up with `runoak`, the term caches or `just validate-terms` before binding it. I deliberately give no MONDO label or CURIE for the disease. The MONDO ID in the template (MONDO:0016312) needs a lookup before use. Check whether the entry is a toxicity or poisoning entity rather than a drug-class grouping.

## 1. Disease Information
- 5-FU poisoning is toxicity from fluorouracil overdose, or from severe early-onset toxicity at standard doses. Capecitabine, a 5-FU prodrug, behaves the same way.
- **Overdose:** dosing or infusion-pump errors.
- **Standard-dose toxicity:** reduced detoxification, usually DPD deficiency.
- The only approved antidote is uridine triacetate. In pooled studies it was started within 96 h of overdose or early-onset severe toxicity. 30-day survival was 94% overall (96% in overdose, 81% in early-onset severe toxicity), against 16% in a historical best-supportive-care cohort. [Ison et al., Clin Cancer Res 2016 (FDA approval summary), via JHU Pure](https://pure.johnshopkins.edu/en/publications/fda-approval-uridine-triacetate-for-the-treatment-of-patients-fol), [Drugs & Therapy Perspectives guide](https://link.springer.com/article/10.1007/s40267-016-0367-5). Treat the 16% comparator as a historical control, not a randomized one.
- **Synonyms:** fluorouracil overdose or toxicity, capecitabine toxicity, fluoropyrimidine toxicity.
- **Data level:** disease-level, aggregated from case reports and trials. This is not EHR-derived.

## 2. Etiology
- **Causal factors (environmental/iatrogenic):** overdose, or standard dosing in a patient who cannot clear the drug.
- **Genetic risk factors:**
  - DPYD variants reduce DPD activity. Poor metabolizers have complete DPD deficiency and risk severe or fatal toxicity. CPIC advises avoiding fluoropyrimidines in them and using reduced starting doses in partial deficiency. [CPIC 2017 update, PMID:29152729](https://ascopubs.org/doi/10.1002/cpt.911) (URL as returned by search: [Wiley](https://ascpt.onlinelibrary.wiley.com/doi/10.1002/cpt.911)); earlier guideline PMID:23988873.
  - The Dutch Pharmacogenetics Working Group has a parallel guideline: [PMC7080718](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7080718/).
  - TYMS variation is also implicated: [PMC7713499](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7713499/), and [uridine triacetate in a TYMS-variant patient, PubMed 30013790](https://pubmed.ncbi.nlm.nih.gov/30013790).
  - Specific alleles such as DPYD*2A, c.1679T>G, c.2846A>T and HapB3 are **[background, unverified]**. Quote them from the CPIC table.
- **Other risk factors [background, unverified]:** renal impairment, drug interactions (for example with capecitabine or brivudine/sorivudine), and dosing errors.
- **Protective factors:** none well established. Normal DPD activity is the default state.
- **Gene–environment:** DPYD genotype determines how a given dose or exposure behaves. This is a pharmacogenetic interaction, not a classic GxE one.

## 3. Phenotypes (suggested HP terms; verify each before binding)
Frequencies are not sourced, so I give none.
- Diarrhea (HP:0002014) and mucositis/stomatitis.
- Myelosuppression: neutropenia, pancytopenia.
- **Hyperammonemic encephalopathy.** It presents as sudden altered mental status, lactic acidosis and respiratory alkalosis with high ammonia. Onset is 0.5–5 days after starting 5-FU. [French national survey](https://www.researchgate.net/publication/339591778_5-Fluorouracil-induced_hyperammonaemic_encephalopathy_A_French_national_survey), [case report PMC7013286](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7013286/).
- **Cardiotoxicity.** It often presents as myocardial ischemia, with less common arrhythmia, hypo- or hypertension, LV dysfunction, cardiac arrest and sudden death. [Systematic review PMC4170068](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4170068/).
- Hand-foot syndrome, nausea/vomiting and alopecia **[background, unverified]**.
- Onset is acute: early-onset severe toxicity, and delayed-onset cases are also reported ([PMC9490183](https://pmc.ncbi.nlm.nih.gov/articles/PMC9490183/)). Quality-of-life data were not searched.

## 4. Genetic/Molecular
- **DPYD** (the lowercase `hgnc:` CURIE must be looked up; I did not verify one). Loss of function of the catabolic enzyme. Classification and allele frequencies: CPIC and gnomAD, not retrieved.
- **TYMS** is a modifier, as the TYMS-variant case above shows.
- Germline origin. Epigenetic and chromosomal data: none sought.

## 5. Environmental
The exposure is iatrogenic. In the KB, `environmental` would be the drug exposure, and an ECTO term needs a re-run search (for example `l~fluorouracil`) before binding. There are no lifestyle or infectious factors.

## 6. Mechanism / Pathophysiology
**Causal chain (inferred steps are marked):**
1. Excess 5-FU exposure follows overdose, or standard dosing with deficient DPD clearance. DPD normally catabolizes most of a dose.
2. High exposure produces more active metabolites and thymidylate synthase inhibition (**[background, unverified]**; classic mechanism).
3. Metabolites are incorporated into RNA and DNA (**[background, unverified]**). This injures rapidly dividing cells, causing mucositis, diarrhea and myelosuppression.
4. Uridine triacetate works because uridine competes with the toxic metabolites. Its efficacy in this setting supports an RNA-directed toxicity component. This is inferred from the antidote's clinical effect, not directly demonstrated here.
5. **Branch, neurologic:** catabolites (fluoro-β-alanine, monofluoroacetate) depress TCA-cycle flux and ATP. This secondarily impairs the urea cycle, leading to hyperammonemia and then encephalopathy ([PMC7013286](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7013286/)). The fluoroacetate/fluorocitrate step is postulated, not proven.
6. **Branch, cardiac:** proposed mechanisms are endothelial injury with thrombosis, energy depletion and ischemia, oxidative stress, coronary spasm, and reduced red-cell oxygen transfer. There is no evidence for a single mechanism. One source: [rat cardiocyte oxidative stress and apoptosis, PMC3461434](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3461434/) (in vivo/in vitro rat data).
- **Suggested GO/CL terms (verify):** apoptotic process, response to oxidative stress, the citrate cycle and urea cycle. Cell types: intestinal epithelial cell, hematopoietic progenitor, cardiac muscle cell, hepatocyte.

## 7. Anatomical Structures
- **Primary:** GI tract mucosa, bone marrow.
- **Secondary:** heart and brain; liver (the site of DPD detoxification).
- Suggested UBERON terms: look up small intestine, bone marrow, heart, brain, liver. The condition is bilateral and systemic.

## 8. Temporal Development
Acute. The encephalopathy appears at 0.5–5 days. Early-onset severe toxicity and delayed onset are both described. Recovery with prompt antidote is substantial per the figures above. Stages and critical periods: the 96-hour antidote window is the key one.

## 9. Inheritance and Population
- **Inheritance:** DPD deficiency is autosomal recessive for complete deficiency. Partial deficiency is intermediate **[background, unverified]**; confirm against CPIC.
- **Prevalence, incidence, sex ratio and ancestry:** not retrieved. I did not find numbers, so none are stated.

## 10. Diagnostics
- **Clinical:** history of exposure plus toxicity pattern. Check ammonia and lactate if neurologic changes appear.
- **Genetic:** DPYD genotyping before therapy ([CPIC](https://ascpt.onlinelibrary.wiley.com/doi/10.1002/cpt.911), [DPWG](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7080718/)). Universal pre-treatment testing is promoted by some groups ([NCODA](https://ncoda.org/news/universal-dpyd-testing-prior-to-5-fu-and-capecitabine-therapy/)). Other approaches (phenotyping, uracil levels) are **[background, unverified]**.
- **Differential:** sepsis, other chemotherapy toxicities, and other causes of encephalopathy. Nothing in the sources retrieved distinguishes these.

## 11. Outcome/Prognosis
With uridine triacetate started within 96 h, 30-day survival was 94% versus 16% for historical controls. Complete DPD deficiency risks fatal toxicity (CPIC). Other prognostic data were not retrieved.

## 12. Treatment
- **Antidote:** uridine triacetate (Vistogard), FDA-approved for overdose and early-onset severe toxicity ([Ison 2016](https://pure.johnshopkins.edu/en/publications/fda-approval-uridine-triacetate-for-the-treatment-of-patients-fol)). Delayed-onset use was reported in [PMC9490183](https://pmc.ncbi.nlm.nih.gov/articles/PMC9490183/). Its use in a TYMS-variant patient is described in [PubMed 30013790](https://pubmed.ncbi.nlm.nih.gov/30013790). The CHEBI/NCIT agent CURIE needs lookup.
- **Supportive care:** fluids, antiemetics, antidiarrheals, G-CSF, transfusion, ICU care **[background, unverified]**. Suggested NCIT action terms (verify): `NCIT:C15986` Pharmacotherapy and `NCIT:C15747` Supportive Care. These appear in the CLAUDE.md list and should still be looked up.
- **Prevention-linked dosing:** DPYD-guided dose reduction or avoidance (CPIC).
- Trials: none retrieved. [NCT07158164](https://clinicaltrials.gov/study/NCT07158164) surfaced, a DPYD-guided dosing study. I did not read it, so check it before citing.

## 13. Prevention
- **Primary:** pre-treatment DPYD genotyping with dose adjustment, plus pump and dosing safeguards (the latter **[background, unverified]**).
- **Secondary:** early recognition of toxicity within the antidote window.
- No vaccine or public-health program applies.

## 14. Other Species
Not researched. Fluoropyrimidine toxicity in dogs and cats (topical 5-FU is especially toxic to them) is **[background, unverified]**. Check OMIA and PubMed before adding it.

## 15. Model Organisms
- Rat cardiocyte oxidative-stress and apoptosis data ([PMC3461434](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3461434/)). Grade these `MODEL_ORGANISM` or `IN_VITRO` depending on the quoted sentence.
- Dpyd-deficient mouse models are **[background, unverified]**. Search MGI before adding any.

## Gaps and next steps
1. Fetch the PMIDs for the Ison 2016 paper, the French national survey and the cardiotoxicity review. I did not retrieve them, so I give no numbers.
2. Take allele frequencies and CPIC tier tables from the CPIC supplement.
3. Take epidemiology from a primary source.
4. Look up every suggested CURIE.
5. Run `just preflight-dr` on this report.

**Sources used:** [CPIC 2017 (Wiley)](https://ascpt.onlinelibrary.wiley.com/doi/10.1002/cpt.911), [DPWG](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7080718/), [PMC7713499](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7713499/), [NCODA](https://ncoda.org/news/universal-dpyd-testing-prior-to-5-fluorouracil-and-capecitabine-therapy/), [Ison 2016 record](https://pure.johnshopkins.edu/en/publications/fda-approval-uridine-triacetate-for-the-treatment-of-patients-fol), [uridine triacetate guide](https://link.springer.com/article/10.1007/s40267-016-0367-5), [delayed-onset case PMC9490183](https://pmc.ncbi.nlm.nih.gov/articles/PMC9490183/), [TYMS case 30013790](https://pubmed.ncbi.nlm.nih.gov/30013790), [French survey](https://www.researchgate.net/publication/339591778_5-Fluorouracil-induced_hyperammonaemic_encephalopathy_A_French_national_survey), [PMC7013286](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7013286/), [cardiotoxicity review PMC4170068](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4170068/), [PMC3461434](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3461434/).

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 11 |
| On topic | 2 |
| Off topic | 2 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMC:PMC7013286` (7 mentions) - A 5-Fluorouracil-Induced Hyperammonemic Encephalopathy Challenged with Capecitabine.
  - shared terms: encephalopathy
- `PMC:PMC4170068` (5 mentions) - A systematic review of the pathophysiology of 5-fluorouracil-induced cardiotoxicity.
  - shared terms: none

Weighed against this report's own most characteristic terms: `toxicity`, `unverified`, `cpic`, `dpd`, `uridine`, `triacetate`, `dosing`, `severe`, `antidote`, `dose`, `overdose`, `deficiency`, `dpyd`, `early-onset`, `exposure`, `curie`, `appear`, `check`, `encephalopathy`, `verify`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 0 |

Every term resolved, and every label the report gave matched.