---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-16T18:25:54.888162'
end_time: '2026-10-16T18:28:35.664990'
duration_seconds: 160.78
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Chilton-Okur-Chung Neurodevelopmental Syndrome
  mondo_id: MONDO:0859239
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
  - claude-opus-5-5
  web_search_requests: 3
  num_turns: 21
  total_cost_usd: 2.2375174400000004
  session_id: ed72fa8d-69b4-4ffb-bdb1-2469e708b01a
  stop_reason: end_turn
  permission_denials: 5
  denied_tools:
  - Bash
  assistant_text_blocks: 3
citation_count: 9
reference_validation:
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 11
  on_topic: 6
  off_topic: 1
  off_topic_references:
  - PMID:10391936
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 35
  verified: 32
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 7
  labels_matching: 5
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: HP:0001320
    reported_labels:
    - Present (2020)
    ontology_label: Cerebellar vermis hypoplasia
  labels_variant: 1
  unresolvable_prefixes:
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Chilton-Okur-Chung Neurodevelopmental Syndrome
- **MONDO ID:** MONDO:0859239 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Chilton-Okur-Chung Neurodevelopmental Syndrome** covering all of the
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

Now let me read the cached abstracts for the other references.

I've read the local references for this syndrome. Next I'm running a few web searches to fill in identifiers and newer case reports, then I'll write the report.

# Research report: Chilton-Okur-Chung neurodevelopmental syndrome (CHOCNS)

*Compiled 2026-10-16 for the dismech knowledge base, from the reference cache in this worktree (`references_cache/`) plus web searches. Every CURIE suggested below was checked against the committed `cache/*/terms.csv` label caches. Snippets in quotation marks are verbatim from the cached abstracts or full texts.*

---

## Before you use this report: a name that is easy to confuse

**Chilton-Okur-Chung syndrome (CHOCNS, CDC42BPB) is a different disease from Okur-Chung neurodevelopmental syndrome (OCNDS, CSNK2A1).** The names differ by one word, and the same research group named both. Ten of the 18 references cached on this branch are about the wrong disease:

- **About OCNDS or other CK2 disorders, not CHOCNS:** PMID:34041744, 35693553, 36310603, 38711237, 39915227, 40742416, 41395761, 41978434 and 42706398.
- **About the wrong part of the gene family:** PMID:10391936 covers MRCKα, not MRCKβ, in PC12 cells. It is relevant only as gene-family background.

None of these should be cited for CHOCNS phenotypes. Before committing, you could prune their caches if nothing in the entry cites them.

A second confusion appears in the founding abstract itself. It mentions **Takenouchi-Kosaki syndrome**, which is caused by variants in *CDC42*, the GTPase upstream of MRCKβ. It is not caused by *CDC42BPB*.

---

## 1. Disease information

**What it is.** CHOCNS is an autosomal dominant neurodevelopmental disorder caused by heterozygous variants in *CDC42BPB*, which are usually de novo. Its main features are:
- developmental delay or intellectual disability
- autism and ADHD
- hypotonia
- variable structural brain anomalies, mainly of the cerebellum, ventricles and corpus callosum.

**Identifiers**

| System | ID |
|---|---|
| MONDO | MONDO:0859239 *Chilton-Okur-Chung neurodevelopmental syndrome* |
| OMIM | #619841 (phenotype). The gene is at 14q32.32 |
| Gene | *CDC42BPB*, hgnc:1738, protein MRCKβ |
| KEGG Disease | H02666 (search hit, not opened) |
| Orphanet / ICD-10 / ICD-11 / MeSH | No disease-specific code found. It falls under the generic codes for intellectual disability and neurodevelopmental disorders |

**Synonyms:** CHOCNS; *CDC42BPB*-related neurodevelopmental disorder.

**Basis of the knowledge.** Everything comes from aggregated case series and case reports. No EHR or registry data exist.

**Key literature**

| Ref | Type | Content |
|---|---|---|
| Chilton et al. 2020, *Am J Med Genet A*, **PMID:32031333** | Founding case series | 14 individuals, 12 variants |
| Duz, Lasa-Aranzasti, Cazurro … Chung, *BMC Med Genomics* 2026 (published 2026-08-15), DOI 10.1186/s12920-026-02448-w | Largest cohort | 20 new plus 17 previously reported individuals (n=37). **PMID not confirmed. The full text is behind a login, so only the abstract was read** |
| Dutta & Garg 2026, *Clin Dysmorphol*, **PMID:42565347** | Case report | Generalized overgrowth. **The cache has no abstract (`content_type: unavailable`), so it cannot be quoted** |
| Kim et al.? 2025, *Int J Mol Sci*, **PMID:40243517** | Atypical cerebral palsy cohort | One de novo LPV, p.Arg1350Gln |
| 2026 *Hum Mol Genet*, **PMID:42873655** (preprint: bioRxiv PMID:42124667) | Mouse study | *Cdc42bpb* mice and a CDH patient variant |

---

## 2. Etiology

- **Cause:** a heterozygous germline *CDC42BPB* variant, de novo in most tested trios. In the founding series it was de novo in 11 of 14.
  > "We identified 12 heterozygous predicted deleterious variants in CDC42BPB (9 missense, 2 frameshift, and 1 nonsense) in 14 unrelated individuals (confirmed de novo in 11/14) with neurodevelopmental disorders" (PMID:32031333)
- **Incomplete penetrance and variable expressivity.** According to the abstract of the 2026 cohort, some heterozygous predicted loss-of-function variants were found in unaffected parents or in people with only subtle features. For counselling, this means truncating alleles can be inherited.
- **Environmental risk factors, protective factors and gene-environment interactions:** none reported, and none would be expected for this disorder.

---

## 3. Phenotypes

Frequencies come from the 2026 cohort abstract (n=37) unless marked "2020", which refers to the 14-person founding series in PMID:32031333.

| Phenotype | Frequency | Suggested HPO term (cache-verified) | Notes |
|---|---|---|---|
| Developmental delay | 85% | HP:0001263 Global developmental delay | Mostly walking and speech. Onset in infancy or early childhood |
| Intellectual disability | 62% | HP:0001249 Intellectual disability | Variable severity |
| Autism spectrum disorder | 68% | HP:0000717 Autism (or HP:0000729 Autistic behavior) | |
| ADHD | 60% | HP:0007018 Attention deficit hyperactivity disorder | **Missing from the current entry** |
| Dysmorphic features | 83% | No specific gestalt is defined, so leave unbound or use specific features only | |
| Hypotonia | 68% | HP:0001252 Hypotonia | |
| Seizures | 41% (2020: 3 of 14, plus 1 with an abnormal EEG) | HP:0001250 Seizure | **Missing from the entry.** Australian PanelApp rates the gene *amber* for epilepsy |
| Macrocephaly | 38% | HP:0000256 Macrocephaly | **Missing from the entry** |
| Generalized overgrowth | Case report | HP:0001548 Overgrowth | PMID:42565347. No abstract is cached |
| Structural brain anomaly | 48% | See the next rows | Mainly cerebellar and ventricular |
| Cerebellar vermis hypoplasia | Present (2020) | HP:0001320 | |
| Agenesis or hypoplasia of the corpus callosum | Present (2020) | HP:0001274 / HP:0002079 | |
| Ventricular enlargement | Reported (OMIM summary, 2026 cohort) | HP:0002119 Ventriculomegaly | Candidate addition |
| Speech delay | Prominent (2026 cohort) | HP:0000750 Delayed speech and language development | Candidate addition |

**Course:** non-progressive and lifelong. Ages in the 2020 series ranged from 2 to 29 years, per OMIM.

**Quality of life:** no EQ-5D, SF-36 or other QoL data have been published.

**Unverified expansion.** The discussion section of PMID:40243517 claims *CDC42BPB* is linked to early-onset epilepsy, spasticity, profound ID and polymicrogyria or schizencephaly. It cites only its reference 47, and that claim does not match the founding series. Treat it as unverified. That patient's holoprosencephaly is explicitly flagged by the authors as possibly coincidental.

---

## 4. Genetics and molecular information

- **Gene:** *CDC42BPB* (14q32.32), hgnc:1738. It encodes MRCKβ, an AGC-family serine/threonine kinase.
- **Variant spectrum (2020).** There were 9 missense, 2 frameshift and 1 nonsense variants.
  > "All missense variants are located in highly conserved and functionally important protein domains/regions: 3 are found in the protein kinase domain, 2 are in the citron homology domain, and 4 in a 20-amino acid sequence between 2 coiled-coil regions, 2 of which are recurrent."
- **Recurrent variant:** p.Arg867Cys (c.2599C>T, NM_006035.4), found de novo in two unrelated patients. It sits in the coiled-coil segment and is listed in ClinVar as Pathogenic with no assertion criteria (RCV002249554).
- **Other variants:**
  - p.Arg1350Gln (c.4049G>A), de novo, likely pathogenic, in a child with atypical cerebral palsy (PMID:40243517). Table row: "CDC42BPB, c.4049G>A/p.Arg1350Gln | De novo/Het | n.f. | LPV | CHOCNS (# 619841)".
  - p.Thr1179Met (c.3536C>T), de novo, found in a boy with isolated dorsal CDH who had **normal** neurodevelopment (Vineland score 95). This variant does not cause CHOCNS (PMID:42873655).
- **Functional consequence:**
  - Truncating variants are predicted to cause haploinsufficiency through nonsense-mediated decay. The authors expected this from the variant class; it was not measured.
  - The mechanism of the missense variants is unknown. The 2026 cohort reports clinical differences between predicted loss-of-function and missense variants and calls for kinase-activity and substrate-specificity studies. The clustering of missense variants suggests a non-haploinsufficiency effect, but this has not been tested.
  - ClinGen's dosage page states that functional studies would be needed to determine the missense mechanism.
- **Gene-disease validity (GenCC)**

  | Submitter | Classification | Disease | Year |
  |---|---|---|---|
  | Labcorp/Invitae | **Strong** | CHOCNS | 2022 |
  | Ambry | Moderate | complex NDD | 2020 |
  | G2P | **Limited** | CHOCNS (G2P02932) | 2025 |

  No ClinGen GCEP validity assertion was found. Do not record a `gene_disease_validity` tier unless you copy it from one of these sources with `classified_by`. Note that G2P is not in the ClinGen-checked set.
- **Population frequency:** pathogenic variants are absent from gnomAD, as expected for de novo variants. No numbers were retrieved.
- **Modifier genes, epigenetic signature or chromosomal abnormalities:** none reported. No DNA methylation episignature is known.

---

## 5. Environmental factors

None are known, and the disorder is not infectious. **This section is not applicable.**

---

## 6. Mechanism and pathophysiology

**Causal chain** (each step marked as demonstrated or inferred)

1. A heterozygous *CDC42BPB* variant (germline, usually de novo) **is demonstrated** in patients (PMID:32031333).
2. → For truncating alleles, this **is predicted to lead to** nonsense-mediated decay and haploinsufficiency (prediction from variant class; not measured). For missense alleles, the effect is **unknown** and could be partial loss of function or something else (a knowledge gap).
3. → This **is inferred to result in** less MRCKβ phosphorylation of the myosin II regulatory light chain, and therefore weaker actomyosin contractility and actin reorganization. This step rests on the kinase's normal function (PMID:24553779, a review), not on patient cells.
   > "In contrast to the closely related ROCK1 and ROCK2 kinases that are regulated by the RhoA and RhoC GTPases, there is relatively little information about the CDC42-regulated MRCKα, MRCKβ and MRCKγ members of the AGC (PKA, PKG and PKC) kinase family."
4. → In developing neurons, this **is proposed to lead to** impaired dendrite outgrowth and spine formation. The evidence is in vitro normal-function data (PMID:33933448):
   > "Activated MRCKβ in turn phosphorylates a class 2 regulatory myosin light chain, which leads to enhanced actin rearrangement, causing the dendrite outgrowth and spine formation observed before."

   *A possible parallel branch* is defective cytoskeleton-dependent neuronal migration (GO:0016477 cell migration). This is speculative; no data exist.
5. → This **is associated with** abnormal brain development: cerebellar vermis hypoplasia, callosal agenesis or hypoplasia, and ventriculomegaly (demonstrated by imaging). The steps linking 4 to 5 are not established.
6. → This **results in** the clinical picture: developmental delay, ID, autism, ADHD, hypotonia and seizures.

**Checklist**

- **Pathway:** CDC42 → MRCKβ → MLC2 (myosin II), alongside the RhoA → ROCK axis.
- **GO terms (verified):**
  - GO:0004674 protein serine/threonine kinase activity (DECREASED, inferred)
  - GO:0031032 actomyosin structure organization
  - GO:0048813 dendrite morphogenesis
  - GO:0007420 brain development
  - GO:0016477 cell migration (speculative)
- **Cell types:** CL:0000540 neuron is the main candidate. MRCKβ is also needed for phagocytosis in retinal pigment epithelium (RPE) (PMID:36121394). No eye phenotype has been reported in CHOCNS, so do not import that.
- **No data exist for** omics, single-cell or spatial studies, CRISPR screens, or immune or metabolic involvement.

---

## 7. Anatomy

| Level | Finding |
|---|---|
| Main organ | Brain, UBERON:0000955 |
| Structures | Cerebellum (UBERON:0002037), cerebellar vermis (UBERON:0004720), corpus callosum (UBERON:0002336), and the cerebral ventricles |
| Cell type | Neurons (CL:0000540) |
| Subcellular | Cortical actomyosin cytoskeleton and cytoplasm |
| Lateralization | Not applicable; findings are midline or bilateral |

**Diaphragm (UBERON:0001103) and heart are involved only in homozygous mice.** These are not established features of the human syndrome (see §15).

---

## 8. Temporal development

- **Onset:** congenital, recognized in infancy or early childhood through hypotonia and delayed walking and speech.
- **Course:** a static, non-degenerative, lifelong neurodevelopmental disorder.
- **Stages, remission or regression:** none reported. No natural-history study exists.
- **Critical window:** early childhood, for developmental therapies.

---

## 9. Inheritance and population

- **Inheritance:** autosomal dominant, HP:0000006. This is already bound in the entry.
- **Origin:** mostly de novo. Inherited predicted loss-of-function alleles with reduced penetrance are noted in the 2026 abstract.
- **Mosaicism:** parental germline mosaicism is possible, as for any de novo disorder, but it has not been documented.
- **Prevalence:** unknown. About 37 or more individuals have been reported worldwide. Use `CASES_IN_LITERATURE`. Do not assign a numeric prevalence band.
- **Other features:**
  - Anticipation, founder effects, consanguinity and carrier frequency are not applicable.
  - Patients have been reported from Europe and North America (GeneMatcher) and from Korea and India.
  - No sex bias is reported.

---

## 10. Diagnostics

- **Genetic testing:**
  - Exome or genome sequencing is first-tier for NDD/ID/ASD, ideally as a trio.
  - *CDC42BPB* is on intellectual disability panels; PanelApp Australia rates it *green* for ID and *amber* for epilepsy.
  - Chromosomal microarray will not detect point variants, but it could detect a 14q32.32 deletion. No CHOCNS deletions have been reported.
- **Imaging:** brain MRI to look for cerebellar vermis hypoplasia, callosal anomalies and ventriculomegaly.
- **EEG:** if seizures are suspected.
- **Biochemical markers and episignature:** none.
- **Differential diagnosis:**
  - OCNDS (*CSNK2A1*)
  - POBINDS (*CSNK2B*)
  - Takenouchi-Kosaki syndrome (*CDC42*)
  - Other syndromic causes of ID or ASD with macrocephaly or overgrowth, such as *PTEN* hamartoma or Sotos syndrome
- **Screening:** there is no newborn screening. Prenatal or preimplantation testing is possible for families with a known variant.

---

## 11. Prognosis

- **Mortality and life expectancy:** no data. Reported patients range up to 29 years old (2020 series).
- **Morbidity:** lifelong developmental disability, which is variable and ranges from mild to severe. Seizures occur in a minority.
- **Prognostic factors:** possibly variant class (loss of function versus missense; 2026 cohort). The details need the full text.

---

## 12. Treatment

There is no disease-specific or targeted therapy, and no trials are registered. A ClinicalTrials.gov search was not run separately. Management is supportive:

| Intervention | NCIT (verified) | Suggested `therapeutic_modality` |
|---|---|---|
| Physical therapy | NCIT:C15302 | BEHAVIORAL |
| Speech language therapy | NCIT:C159273 | BEHAVIORAL |
| Occupational therapy | NCIT:C121351 | BEHAVIORAL |
| Antiseizure medication | NCIT:C15986 Pharmacotherapy | Agent-specific; no CHOCNS-specific drug |
| ADHD and behavioral pharmacotherapy | NCIT:C15986 | Agent-specific |
| Genetic counseling | NCIT:C15240 | Not mechanically mappable |

**These rows lack CHOCNS-specific evidence.** There are no published management guidelines for this disorder, so only generic NDD evidence is available. Consider leaving treatments out, or adding only those the 2026 full text supports.

---

## 13. Prevention

Primary prevention is not applicable for a de novo disorder. Preventive measures available:
- genetic counseling, with a low but non-zero recurrence risk because of possible germline mosaicism
- parental testing, which matters given inherited loss-of-function alleles
- prenatal or preimplantation testing for a known familial variant.

---

## 14. Other species

No naturally occurring disease has been found (no OMIA entry). The gene is highly conserved: the mouse ortholog is *Cdc42bpb* (MGI:2136459).

---

## 15. Model organisms

There is **one** published model: a *Cdc42bpb* knockout mouse.

| Item | Detail |
|---|---|
| Source | PMID:42873655 (*Hum Mol Genet* 2026); preprint PMID:42124667 |
| Allele | KOMP2 knockout, C57BL6NJ-*Cdc42bpb*^em1(IMPC)J^, exon-2 deletion causing a frameshift; MGI:5812907 |
| Homozygous phenotype | "Homozygous loss of Cdc42bpb leads to large ventral gaps in the diaphragm with high penetrance, minor changes in lung morphology, and lethal heart septation defects." |
| Lethality | Ventricular septal defects in 9 of 9 embryos at E18.5; death on postnatal day 1 |
| Patient-variant knock-in | F0 knock-in of the CDH variant p.Thr1179Met produced only minimal ventral gaps |
| Relevance to CHOCNS | **No neurodevelopmental phenotyping was reported**, and the heterozygous state, which is the genotype of human CHOCNS, had no reported defect |

This fits the entry's existing `HUMAN_MODEL_MISMATCH` discussion. A model could be recorded with `relationship: FAILS_TO_RECAPITULATE` or left out. No zebrafish, fly, iPSC or organoid models of CHOCNS exist.

---

## Suggested changes to the draft entry

1. **Phenotypes to add** with evidence from the 2026 cohort, if you can cache it: ADHD (HP:0007018), Seizure (HP:0001250), Macrocephaly (HP:0000256), possibly Ventriculomegaly (HP:0002119), and Overgrowth (HP:0001548; abstract unavailable, so it cannot be quoted yet). Add frequencies for existing phenotypes from the same source.
   - **Next step:** run `just fetch-reference DOI:10.1186/s12920-026-02448-w`, or find its PMID, before citing it.
2. **Inheritance:** add the incomplete penetrance and variable expressivity of inherited truncating alleles.
3. **Prevalence:** add a `CASES_IN_LITERATURE` record of about 37 individuals.
4. **Clean-up:** remove the 10 cached references for OCNDS or other CK2 disorders that the entry doesn't cite.
5. **Gene-disease validity:** leave it absent unless you copy a GenCC tier with its submitter.

---

## Sources

- [OMIM #619841](https://www.omim.org/entry/619841) (returned 403 to automated fetch; content known only from search snippets)
- [Duz et al. 2026, BMC Med Genomics: Clinical characterization and genotype–phenotype correlations in Chilton-Okur-Chung syndrome](https://link.springer.com/article/10.1186/s12920-026-02448-w) (abstract only)
- [GenCC: CDC42BPB](https://thegencc.org/genes/HGNC:1738)
- [ClinGen Dosage: CDC42BPB](https://search.clinicalgenome.org/kb/gene-dosage/HGNC:1738)
- [ClinVar RCV002249554, p.Arg867Cys](https://www.ncbi.nlm.nih.gov/clinvar/RCV002249554/)
- [PanelApp Australia: Genetic Epilepsy](https://panelapp-aus.org/panels/202/gene/CDC42BPB) and [ID panel](https://panelapp-aus.org/panels/250/gene/CDC42BPB/)
- [MalaCards](https://www.malacards.org/card/chilton_okur_chung_neurodevelopmental_syndrome) and [KEGG H02666](https://www.kegg.jp/entry/H02666) (search hits only)
- Local cache: PMID:32031333, 33933448, 24553779, 36121394, 40243517, 42873655, 42124667, 42565347

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 11 |
| On topic | 6 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:10391936` (1 mention) - The myotonic dystrophy kinase-related Cdc42-binding kinase is involved in the regulation of neurite outgrowth in PC12 cells.
  - shared terms: genetic

Weighed against this report's own most characteristic terms: `cdc42bpb`, `variant`, `disorder`, `abstract`, `chocn`, `syndrome`, `phenotype`, `novo`, `cohort`, `neurodevelopmental`, `allele`, `patient`, `gene`, `brain`, `developmental`, `feature`, `seizure`, `adhd`, `cached`, `genetic`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 35 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 7 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001320` (1 mention) - the report calls it "Present (2020)"; HP calls it **Cerebellar vermis hypoplasia**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `NCIT:C15986` (2 mentions) - the report calls it "ADHD and behavioral pharmacotherapy"; NCIT calls it **Pharmacotherapy**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`.