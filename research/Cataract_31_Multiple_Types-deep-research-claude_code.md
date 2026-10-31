---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-27T21:59:31.979490'
end_time: '2026-10-27T22:04:36.223900'
duration_seconds: 304.24
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Cataract 31 Multiple Types
  mondo_id: MONDO:0011547
  category: Mendelian
  causal_genes: CHMP4B
  omim_id: OMIM:605387
  synonyms: CHMP4B early-onset non-syndromic cataract; CTRCT31; early-onset non-syndromic
    cataract caused by mutation in CHMP4B
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
  num_turns: 25
  total_cost_usd: 2.4129324999999993
  session_id: 0bfb328d-96db-5dca-803a-342a247b0264
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  assistant_text_blocks: 4
citation_count: 12
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 3
  quotes_valid: 3
  relevance_assessed: 14
  on_topic: 14
  validator_version: 0.4.0
term_validation:
  total_terms: 24
  verified: 22
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 2
  unresolvable_prefixes:
  - OMIM
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cataract 31 Multiple Types
- **MONDO ID:** MONDO:0011547 (if available)
- **Causal gene(s):** CHMP4B
- **OMIM:** OMIM:605387
- **Synonyms:** CHMP4B early-onset non-syndromic cataract; CTRCT31; early-onset non-syndromic cataract caused by mutation in CHMP4B
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Cataract 31 Multiple Types** covering all of the
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

Still researching: PMC pages are blocked and shell network calls need approval, so I'm switching to PubMed pages through the web fetch tool.

Checking the HPO term IDs against the repository's local term cache, since the two Monarch answers disagreed.

The repo already has a `Cataract_31_Multiple_Types.yaml` entry. Next I'm searching for any further CHMP4B variants reported beyond D129V, E161K and S196C.

# Cataract 31, Multiple Types (CTRCT31; MONDO:0011547; OMIM:605387): research report

## Scope and verification status

- **The disease.** Cataract 31, multiple types, is early-onset, non-syndromic, autosomal dominant cataract caused by heterozygous variants in **CHMP4B**. CHMP4B (charged multivesicular body protein 4B, earlier called chromatin modifying protein 4B; HGNC:16171, OMIM gene *610897) sits on chromosome 20q11.22. Every claim below concerns CHMP4B.
- **An entry already exists.** `kb/disorders/Cataract_31_Multiple_Types.yaml` is in the KB. Use this report to check and extend that entry, not to start a new one.
- **How the sources were read.** PubMed and PMC returned verification screens, OMIM returned HTTP 403, and shell network calls needed approval that was not given. Abstracts were therefore read through the Europe PMC REST API, and identifiers through the Monarch v3 API.
- **The quotes need re-checking.** The fetch tool would only return abstract text in short fragments. The quotes below are contiguous fragments. Before using any of them as an evidence `snippet`, run `just fetch-reference PMID:…` and `just count-verified-snippets`.
- **Unchecked identifiers.** Terms marked ⚠ were not found in the repository's `cache/` CSVs. Look each one up before binding it.

---

## 1. Disease information

- **Overview.** CTRCT31 is a rare Mendelian lens opacity. The founding family had "progressive childhood posterior subcapsular" cataract, and a Japanese family had posterior polar cataract. Later reports describe several morphologies, hence "multiple types".
- **Identifiers (from the Monarch MONDO record):**
  - MONDO:0011547 *cataract 31, multiple types*
  - OMIM:605387
  - DOID:0110265
  - UMLS C1854311
  - MeSH C535343
  - GARD 0010227
  - MedGen 343089
  - Monarch lists no Orphanet code and no ICD code. In ICD-10 terms it falls under Q12.0 (congenital cataract), but that is not an exact mapping.
- **MONDO definition:** "Early-onset non-syndromic cataract caused by a mutation in the CHMP4B gene."
- **Synonyms:** CTRCT31; CHMP4B early-onset non-syndromic cataract; early-onset non-syndromic cataract caused by mutation in CHMP4B. Older OMIM names include "Cataract, posterior polar, 3" (CPP3), which OMIM later folded into CTRCT31. Confirm that history on OMIM before recording it as a synonym.
- **Kind of data.** Everything comes from aggregated disease-level resources and a handful of family reports. There are no EHR or cohort data.

## 2. Etiology

- **Cause.** Heterozygous germline missense variants in CHMP4B. CHMP4B is a core subunit of ESCRT-III, the machinery that cuts membranes during multivesicular body formation, cytokinetic abscission, and nuclear-envelope and plasma-membrane repair.
- **Genetic risk factors.** The only one known is a family history of autosomal dominant transmission. No GWAS or susceptibility loci are known for this entity.
- **Environmental, protective and gene–environment factors.** None reported. There is mechanistic context from age-related cataract research: HSP90β, a chaperone that is lower in human cataract and in aging lenses, regulates CHMP4B (PMID:37487085, see §6). That is not evidence about CTRCT31 itself.

## 3. Phenotypes

| Phenotype | HPO term | Onset / course | Source |
|---|---|---|---|
| Posterior subcapsular cataract | HP:0007787 *Posterior subcapsular cataract* (in local cache) | Childhood, progressive | PMID:17701905 (D129V family) |
| Posterior polar cataract | ⚠ HP:0010696 *Polar cataract* or a posterior polar child term; look it up | Congenital or early childhood | PMID:17701905 (E161K Japanese family); PMID:10682967 |
| Nuclear cataract | HP:0100018 *Nuclear cataract* (in local cache) | Early onset | Monarch/OMIM annotation (no PMID on the association) |
| Anterior subcapsular cataract | ⚠ HP:0010923; the two Monarch answers gave different labels for it, so check | Early onset | Monarch/OMIM annotation |
| Total, Y-sutural/fetal nuclear, or subcapsular cataract (gene not assigned per family in the abstract) | HP:0000519 *Developmental cataract* (in local cache) | "at a young age" | PMID:34722561 |
| Visual impairment (consequence) | HP:0000505 (in local cache) | Progressive without surgery | Inferred; not quoted in any source |
| Mode of inheritance | HP:0000006 *Autosomal dominant inheritance* (in local cache) | — | PMID:17701905 |

- **Frequency.** No penetrance or frequency figures have been published. All reported carriers in the segregating families were affected.
- **Quality of life.** No disease-specific data. The impact is the general one of paediatric cataract: amblyopia risk and reduced visual acuity, which surgery removes.

**Key quotes from PMID:17701905** (Shiels et al., 2007, *Am J Hum Genet*):
- "Here we report linkage of autosomal dominant "progressive childhood posterior subcapsular" cataracts"
- "cosegregating with autosomal dominant posterior polar cataracts in a Japanese family"

## 4. Genetic and molecular information

**Gene:** CHMP4B, `hgnc:16171` (⚠ not in the local HGNC cache; confirm with `just validate-terms`). The protein has an ESCRT-III/Snf7 domain with an N-terminal core that forms polymers and a C-terminal autoinhibitory helix.

**Published variants (all missense, heterozygous, germline):**

| Variant | Family | Phenotype | Evidence |
|---|---|---|---|
| c.386A>T, p.(Asp129Val), exon 3 | 6-generation white family; LOD 5.50 at D20S847 (θ=0) | Progressive childhood posterior subcapsular | PMID:17701905 |
| c.481G>A, p.(Glu161Lys), exon 3 | Japanese 4-generation family (first reported by Yamada et al., 2000) | Posterior polar | PMID:17701905, PMID:10682967 |
| c.587C>G, p.(Ser196Cys) | One of six Chinese Han families with autosomal dominant cataract | Early-onset; the abstract does not say which morphology this family had | PMID:34722561 |

- **Quotes.**
  - PMID:17701905: "detected a heterozygous transversion (c.386A-->T) in exon 3" … "a phylogenetically conserved aspartic acid residue at codon 129 (p.D129V)."
  - PMID:34722561: "two novel missense variants (GJA8: c.64G > C/p. G22R, and CHMP4B: c.587C > G/p. S196C)".
- **Classification.** D129V was absent from 384 control chromosomes. I could not retrieve ClinVar or ACMG classifications or gnomAD frequencies. Check ClinVar for 610897.0001 and 610897.0002.
- **Functional effect.** The D129V change behaves as a **gain of function, possibly dominant-negative**. PMID:17701905 reports that a truncated recombinant D129V protein "had a different subcellular distribution than wild type and an increased capacity to inhibit release of virus-like particles" … "consistent with deleterious gain-of-function effects." The original paper did not test E161K and S196C functionally. PMID:24741567 reports that a CHMP4B mutation associated with posterior polar cataract "abolishes the ability of CHMP4B to localize to micronuclei."
- **Gene–disease validity.** No ClinGen CGGV record was found. Leave `gene_disease_validity` empty unless one is located.
- **Not applicable / no data:** modifier genes, epigenetic changes, and chromosomal abnormalities. A separate infantile cataract locus at 20p12.1–p11.23 (PMID:18958302) is a different locus; do not conflate it with this one.

## 5. Environmental information

None. There are no environmental factors, lifestyle factors or infectious agents. Leave the section empty and record a note.

## 6. Mechanism / pathophysiology

### Causal chain (✱ = inferred rather than shown in human lens)

1. A heterozygous CHMP4B missense variant (D129V, E161K or S196C) alters conserved residues in the ESCRT-III subunit.
2. The mutant protein is mislocalised and has gain-of-function or inhibitory activity on ESCRT-III membrane scission. This was shown for D129V in transfected cells: inhibition of virus-like-particle budding (PMID:17701905; in vitro).
3. ✱ ESCRT-III activity is disrupted in lens epithelial cells and in elongating fiber cells at the equator, where *Chmp4b* is expressed (PMID:31404815; mouse in situ hybridisation). From here the mechanism branches:
   - **3a. Cell division.** Lens epithelial cytokinetic abscission fails, leading to premature senescence (PMID:34882480).
     - The evidence runs through pathway partners, not through CHMP4B variants. Loss of PI3K-C2α, PI(3,4)P2 or VPS36 "led to impaired cytokinesis, triggering premature senescence" in fish, mice and humans.
     - The reverse direction also disturbs the lens: in a separate study, upregulating CHMP4B "induces excessive division of lens epithelial cells" (PMID:37487085). Correct CHMP4B dosage or activity therefore matters in either direction.
   - **3b. Fiber cell membranes.** CHMP4B normally forms complexes with Cx46 and Cx50 in outer-cortex fiber cell membranes, and depends on Cx50 to reach the membrane (PMID:36880430; mouse). ✱ Disrupting this may impair fiber cell differentiation and gap-junction coupling.
   - **3c. Micronuclei and autophagy.** CHMP4B localises to micronuclei and may target them for autophagolysosomal clearance, and the cataract mutant loses this ability (PMID:24741567; in vitro). ✱ Defective clearance of chromatin or organelles could leave light-scattering debris.
4. ✱ Fiber cell differentiation becomes abnormal or fiber cells degenerate. In mouse: AQP0 immunostaining showed fiber cell degeneration in homozygous D129V embryos and in lens conditional-knockdown mice, with TUNEL-positive cell death (PMID:31404815).
5. Opacities form, posterior subcapsular or posterior polar, with nuclear or anterior subcapsular forms in some reports. The result is progressive visual impairment in childhood.

### Caveats
- In knock-in mice, heterozygous D129V gave grossly normal lenses: "heterozygous, germ-line mutations in Chmp4b may not manifest as cataract" (PMID:31404815). This is a `HUMAN_MODEL_MISMATCH` for steps 3–5.
- Homozygous D129V is lethal by E15.5.

### Suggested terms (⚠ check all before binding)
- **GO:**
  - ESCRT III complex GO:0000815
  - multivesicular body assembly GO:0036258
  - mitotic cytokinetic process / abscission GO:0061952 (midbody abscission)
  - lens fiber cell differentiation GO:0070306
  - lens development in camera-type eye GO:0002088
  - cellular senescence GO:0090398
  - plasma membrane repair GO:0001778
- **CL:** lens epithelial cell CL:0002224; lens fiber cell CL:0011004.
- **Biological scale** for pathophysiology nodes: MOLECULAR for steps 1–2, CELLULAR for 3–4, TISSUE for 5.
- **Module.** The KB's cataract "disease-like phenotype" module is a candidate `conforms_to` target. Check with `just list-modules cataract`.

## 7. Anatomical structures affected

- **Organ and tissue:** lens of camera-type eye (⚠ UBERON:0000965), including the posterior subcapsular region, posterior pole and nucleus. Lens epithelium (⚠ UBERON:0005614) and lens fiber (⚠ UBERON:0002924?).
- **Cells:** lens epithelial cells at the equator and elongating cortical fiber cells.
- **Subcellular:** ESCRT-III complex, the midbody/intercellular bridge, fiber cell plasma membrane (with connexins), and micronuclei.
- **Laterality:** bilateral in reported families. This is typical of the condition but is not quoted in the retrieved abstracts.
- **Other organs:** no systemic involvement (non-syndromic).

## 8. Temporal development

- **Onset:** congenital to childhood. The D129V family was described as "progressive childhood"; the S196C report says "at a young age".
- **Progression:** progressive opacification in the posterior subcapsular phenotype. Posterior polar opacities are often stationary but can progress.
- **Duration:** lifelong until surgery.
- **No data:** staging, remission patterns or natural-history cohorts.
- **Critical period:** the amblyopia-sensitive period in infancy and early childhood is the window that decides surgical timing. This is general paediatric-cataract practice, not CTRCT31-specific evidence.

## 9. Inheritance and population

- **Inheritance:** autosomal dominant (HP:0000006), with apparently full penetrance in the reported families. Expressivity varies in morphology across families (subcapsular, polar, nuclear).
- **Not reported:** anticipation and mosaicism.
- **Epidemiology:** extremely rare, with three published families (white/European, Japanese, Chinese Han). Use `measure_type: CASES_IN_LITERATURE` with a qualitative class such as ULTRA_RARE. There are no prevalence, sex-ratio or founder data.
- **Context:** CHMP4B accounted for one of six families in a Chinese autosomal dominant cataract series (PMID:34722561). In a northern Chinese panel study, 1 of 13 solved families (7.7%) carried a variant in "a chromatin-modifying protein gene" (PMID:30078984). The CHMP4B attribution there comes from MeSH indexing; the abstract does not name the gene.

## 10. Diagnostics

- **Clinical:** slit-lamp biomicroscopy to classify morphology, and red-reflex testing in newborns and infants.
- **No biomarkers:** there are no laboratory or omics markers.
- **Genetic testing:**
  - Multigene congenital cataract panels that include CHMP4B (for example PreventionGenetics test 3877), or exome sequencing. PMID:34722561 used exome sequencing of probands and parents with Sanger confirmation.
  - Single-gene testing suits known familial variants.
  - CMA, karyotype and FISH are not indicated.
- **Differential diagnosis:**
  - Other autosomal dominant cataract genes: CRYAA/CRYBB2/CRYGD, GJA3/GJA8, MIP, PITX3 (posterior polar), EPHA2.
  - Syndromic, metabolic (galactosaemia) and infectious (TORCH) cataract.
- **Screening:** newborn red-reflex screening, and cascade testing in families.

## 11. Outcome and prognosis

- Life expectancy is normal because the disease is non-syndromic.
- Morbidity comes from visual impairment and, if surgery is delayed, amblyopia.
- After surgery, complications include aphakic/pseudophakic glaucoma, visual axis opacification and posterior capsule opacification. These are general paediatric-cataract data.
- No CTRCT31-specific outcome or QoL studies exist.

## 12. Treatment

- **Surgery:** cataract extraction (lensectomy with or without IOL implantation, often with posterior capsulotomy and anterior vitrectomy in young children). ⚠ NCIT term: look up "Cataract Extraction" or fall back to `NCIT:C15329` Surgical Procedure. Set `therapeutic_modality: SURGERY`.
- **Supportive:** aphakic correction with contact lenses or glasses, and amblyopia therapy (occlusion). ⚠ NCIT term to look up. Set `therapeutic_modality: DEVICE` or `BEHAVIORAL` as appropriate.
- **Other options:** no pharmacotherapy, gene therapy or clinical trials. Two experimental findings sit outside this disease: HSP90β regulation of CHMP4B (PMID:37487085) concerns aging cataract, and rapamycin rescue is reported only for an unrelated Gja8b zebrafish model.

## 13. Prevention

- **Primary prevention:** none.
- **Secondary prevention:** neonatal red-reflex screening and early ophthalmic examination of at-risk relatives.
- **Genetic counselling:** 50% recurrence risk for offspring of an affected parent. Prenatal or preimplantation testing is technically possible once the familial variant is known.

## 14. Other species

- No naturally occurring CHMP4B cataract was found in OMIA.
- **Orthologues:** mouse *Chmp4b*. Zebrafish ⚠ (not checked).
- ESCRT-III is conserved through yeast Snf7.

## 15. Model organisms

| Model | Phenotype | Fit to the human disease | Reference |
|---|---|---|---|
| Mouse *Chmp4b* D129V knock-in, heterozygous (D/V) | Viable, fertile, lenses grossly normal | **FAILS_TO_RECAPITULATE** the dominant cataract (species mismatch or incomplete phenotype) | PMID:31404815 |
| Mouse *Chmp4b* D129V homozygous (V/V) | Dead by E15.5; abnormal eye and brain histology; fiber cell degeneration; global TUNEL+ cell death | Partially recapitulates fiber cell degeneration, but in a lethal, systemic context | PMID:31404815 |
| Mouse lens conditional knockdown (Chmp4b-CKD) | Variable lens dysmorphology up to lens ablation; fiber cell degeneration; lens-restricted cell death; CD68+ immune response | Loss-of-function model; PARTIALLY_RECAPITULATES lens degeneration (the human mechanism is likely gain of function) | PMID:31404815 |
| Cx46-KO and Cx50-KO mouse lenses | CHMP4B membrane localisation lost in Cx50-KO only | Mechanistic (CHMP4B–connexin complexes) | PMID:36880430 |
| Cultured cells (transfection) | D129V mislocalised; inhibits virus-like-particle release; posterior polar mutant fails to localise to micronuclei | IN_VITRO | PMID:17701905, PMID:24741567 |

**Quotes from PMID:31404815:**
- "Heterozygous Chmp4b-mutant (D/V) mice were viable and fertile with lenses grossly similar to those of wild-type."
- "Chmp4b-CKD mice displayed variable degrees of lens dysmorphology including lens ablation."
- "In situ hybridization localized Chmp4b transcripts to lens epithelial cells and elongating fiber cells at the lens equator."

**Pathway models outside CHMP4B variants:** PI3K-C2α / VPS36 loss in zebrafish and mouse (PMID:34882480) and HSP90β (PMID:37487085). Grade both as `INDIRECT`.

---

## Key references

| PMID | Citation | Evidence type |
|---|---|---|
| 17701905 | Shiels A et al. "CHMP4B, a novel gene for autosomal dominant cataracts linked to chromosome 20q." *Am J Hum Genet* 2007 | HUMAN_CLINICAL + IN_VITRO (split the items) |
| 10682967 | Yamada K et al. Autosomal dominant posterior polar cataract in a Japanese family. *Am J Ophthalmol* 2000 | HUMAN_CLINICAL |
| 34722561 | Wang X et al. "Broadening the Mutation Spectrum in GJA8 and CHMP4B…" *Front Med* 2021 | HUMAN_CLINICAL |
| 30078984 | Zhang XH et al. Mutation profiles of congenital cataract genes in 21 northern Chinese families. *Mol Vis* 2018 | HUMAN_CLINICAL (CHMP4B only in indexing) |
| 31404815 | Zhou Y, Bennett TM, Shiels A. "A charged multivesicular body protein (CHMP4B) is required for lens growth and differentiation." *Differentiation* 2019 | MODEL_ORGANISM |
| 36880430 | Zhou Y et al. CHMP4B complexes with gap junction proteins. *FASEB J* 2023 | MODEL_ORGANISM / IN_VITRO |
| 24741567 | Sagona AP et al. "Association of CHMP4B and autophagy with micronuclei…" *Biomed Res Int* 2014 | IN_VITRO |
| 34882480 | Gulluni F et al. "PI(3,4)P2-mediated cytokinetic abscission prevents early senescence and cataract formation." *Science* 2021 | MODEL_ORGANISM (pathway context) |
| 37487085 | Fu JL et al. HSP90β prevents aging-related cataract via CHMP4B and p53. *PNAS* 2023 | MODEL_ORGANISM / IN_VITRO (context) |
| 34126080, 31525139, 38927721 | Shiels A reviews on inherited cataract genetics (2019–2024) | Reviews |

## Sources
- [Europe PMC REST API](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=CHMP4B%20AND%20(cataract%20OR%20lens)) (the source of the abstract quotes)
- [PubMed search "CHMP4B cataract"](https://pubmed.ncbi.nlm.nih.gov/?term=CHMP4B+cataract)
- [Monarch MONDO:0011547](https://api-v3.monarchinitiative.org/v3/api/entity/MONDO:0011547)
- [PMC1950844 (Shiels 2007)](https://pmc.ncbi.nlm.nih.gov/articles/PMC1950844)
- [PMC6815251 (Zhou 2019)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6815251)
- [PMC10101236 (Zhou 2023)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10101236)
- [PMC8554029 / Frontiers (Wang 2021)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8554029/)
- [WUSTL profile: CHMP4B required for lens growth](https://profiles.wustl.edu/en/publications/a-charged-multivesicular-body-protein-chmp4b-is-required-for-lens/)
- [MalaCards CTRCT31](https://www.malacards.org/card/cataract_31_multiple_types)
- [PreventionGenetics test 3877](https://www.preventiongenetics.com/testInfo?val=3877)
- [DisGeNET CHMP4B](https://www.disgenet.org/browser/0/1/1/C0086543/geneid__128866-source__ALL/)
- [Alliance HGNC:16171](https://alliancegenome.org/gene/HGNC:16171)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 3 |
| Quoted claims found in source | 3 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 14 |
| On topic | 14 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 24 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 2 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 0 |

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.

22 of 24 terms resolved to a current term; the rest could not be looked up either way.