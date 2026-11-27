---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-26T03:54:58.517405'
end_time: '2026-11-26T03:58:59.180365'
duration_seconds: 240.66
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Laryngeal Tuberculosis
  mondo_id: MONDO:0005819
  category: Infectious Disease
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: larynx tuberculosis; tuberculous laryngitis
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
  web_search_requests: 6
  num_turns: 13
  total_cost_usd: 0.7414081450000001
  session_id: bb2e431b-7e12-4cd4-98a5-f43d5a6e4e66
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  tool_calls: 27
  retrieval_calls: 25
  assistant_text_blocks: 3
citation_count: 15
reference_validation:
  total_references: 27
  verified: 27
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 27
  on_topic: 9
  validator_version: 0.8.0
term_validation:
  total_terms: 1
  verified: 1
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0005819
    reported_labels:
    - MONDO
    ontology_label: laryngeal tuberculosis
  obsolescence_unchecked: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Laryngeal Tuberculosis
- **MONDO ID:** MONDO:0005819 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** larynx tuberculosis; tuberculous laryngitis
- **Category:** Infectious Disease

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Laryngeal Tuberculosis** covering all of the
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

Let me try PubMed E-utilities directly for abstracts.

I've gathered the key sources (Rubin 2024 SWiM review, Gao 2024 cohort, case series, identifiers, WHO data). Now I'm doing one last search on animals and models, and then I'll write the report.

# Laryngeal Tuberculosis (MONDO:0005819): Disease Characteristics Report

**Scope and limitations:**
- **Interpretation.** Laryngeal tuberculosis (LTB) is an infectious disease caused by *Mycobacterium tuberculosis* complex. **No causal human gene exists** (the template lists "not recorded"). The pathogen is the cause. Host genes only change susceptibility, and no laryngeal-specific genetic data were found.
- **Retrieval limits.** PubMed's E-utilities and some PubMed pages were blocked or behind cookie walls during this run. Abstracts therefore came through Europe PMC and PMC, and several were available only as paraphrases.
- **Quotations.** Verbatim abstract quotes appear only where the exact text was retrieved. All other summaries are marked "paraphrased".
- **Ontology IDs.** Term **labels** are suggested for HPO, GO, CL, UBERON, CHEBI and NCIT. Their numeric IDs were **not retrieved** in this session and must be checked before curation.

---

## 1. Disease Information

**Overview.** LTB is extrapulmonary tuberculosis of the larynx. It is the most common granulomatous disease of the larynx. It is rare, cited as about 1% of TB cases or under 1% of extrapulmonary TB, and it often mimics laryngeal cancer.
- Migliorelli et al. 2022 (PMID 36541378) state: *"Laryngeal tuberculosis (LTB) is a rare manifestation of tuberculosis (TB), accounting for 1% of all TB cases."* and *"Most cases involved the true vocal folds."* These are fragments of the abstract from a search snippet.
- The MeSH scope note defines LTB as *"Tuberculosis involving the larynx, producing ulceration of the VOCAL CORDS and the LARYNGEAL MUCOSA."* ([MeSH D014387](https://meshb.nlm.nih.gov/record/ui?ui=D014387))
- A 2023 case report describes LTB as the most common granulomatous laryngeal disease, usually linked to pulmonary TB but able to present as primary disease (Achache 2023, PMID 38133296; [PMC10745871](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10745871/)).

**Identifiers**

| System | ID | Notes |
|---|---|---|
| MONDO | MONDO:0005819 | Supplied in the template |
| MeSH | D014387 "Tuberculosis, Laryngeal" | Entry terms include "Laryngeal Tuberculosis" and "Tuberculosis of Larynx" ([MeSH](https://meshb.nlm.nih.gov/record/ui?ui=D014387)) |
| ICD-10 | A15.5 | "Tuberculosis of larynx, trachea and bronchus", confirmed bacteriologically, molecularly or histologically. Inclusion terms are bronchus, glottis, larynx and trachea ([NHS ICD-10 browser](https://classbrowser.nhs.uk/ICD-10-5TH-Edition/vol1/block-a15-a19.htm); [gesund.bund.de](https://gesund.bund.de/en/icd-code-search/a15-5)) |
| ICD-10 | A16.5 | The same sites without bacteriological or histological confirmation ([NHS](https://classbrowser.nhs.uk/ICD-10-5TH-Edition/vol1/block-a15-a19.htm)) |
| ICD-11 | 1B10.0 (respiratory TB, confirmed) | **Unverified**; the mapping comes from a third-party site ([autoicdapi](https://autoicdapi.com/reference/icd-10/A15.5)) |
| OMIM / Orphanet | Not applicable or not found | Infectious, non-Mendelian disease |

**Synonyms:** larynx tuberculosis; tuberculous laryngitis; tuberculosis of larynx; laryngeal TB (LTB).

**Data source type:** The evidence is aggregated from case series, retrospective cohorts and literature reviews, not from EHR-level data.

## 2. Etiology

**Cause:** infection of the laryngeal mucosa by *M. tuberculosis*. There are two recognised forms:
- **Secondary LTB.** This is the classic form. It comes from bronchogenic spread of bacilli-laden sputum from active pulmonary TB.
- **Primary LTB.** This is isolated laryngeal disease with no pulmonary focus.

Primary cases are increasingly reported. Guan 2022 (PMID 35634235) describes three primary cases in which *"The routine workup for pulmonary tuberculosis was unremarkable."* Nerurkar 2024 (PMID 38440428) reported 2 primary and 1 secondary case among 890 voice-clinic patients (paraphrased).

**Risk factors.** The main pooled source is the Rubin 2024 SWiM review of 119 articles (PMID 38238187, paraphrased).
- Smoking was reported in 41% of cases.
- 20% had prior lung TB.
- 18% had immunodepression.
- 3% had HIV.

Other risk factors:
- **Active pulmonary TB.** Lung involvement was present in 54% (Rubin 2024) and 56.0% (Gao 2024, n=134, PMID 37979215, paraphrased). In the Teixeira Marques 2024 series (PMID 39111930), all but 1 of 10 patients had active pulmonary TB.
- **HIV and immunosuppression.** These are general TB risk factors. The Pang 2018 head and neck TB literature analysis reports *"465 patients were positive according to a HIV test"* (PMID 29323108).
- **Male sex.** The Teixeira Marques series had 8 males and 2 females.
- **High-burden settings.** In a prospective South African study, 5 of 80 biopsied adults (6.25%) had LTB (Matimba 2020, PMID 32328767; paraphrased and unverified).

**Genetic risk and protective factors:** No laryngeal-specific host genetic data were retrieved. General TB-susceptibility genetics were not searched in this session and are not reported here.

**Protective factors:**
- Treatment of pulmonary TB, and the resulting fall in prevalence, is protective at the population level. Secondary LTB made up 15–40% of pulmonary TB cases before antibiotics and fell below 1% with routine antitubercular therapy (review cited at [PMC5446342](https://pmc.ncbi.nlm.nih.gov/articles/PMC5446342)).
- No data on BCG protection against laryngeal disease specifically were retrieved.

**Gene–environment interactions:** No data were retrieved.

## 3. Phenotypes

| Phenotype | Suggested HPO label | Frequency | Evidence |
|---|---|---|---|
| Hoarseness / dysphonia | Hoarse voice; Dysphonia | 97.0% (Gao, n=134); 9/10 (Teixeira Marques); voice impairment 86% (Rubin, pooled) | PMIDs 37979215, 39111930, 38238187 |
| Odynophagia | Odynophagia | Second most common symptom (qualitative) | [PMC9103562](https://pmc.ncbi.nlm.nih.gov/articles/PMC9103562) |
| Foreign-body sensation in the throat | Globus sensation (closest term) | Common (qualitative) | Same source |
| Lesion of the true vocal folds (ulcer, irregular mucosa, exophytic mass) | Vocal cord lesion; Laryngeal ulcer (verify) | Glottis involved in 87.3% (Gao); true vocal cords were the most common site (Teixeira Marques) | PMIDs 37979215, 39111930, 36541378 |
| Absent mucosal wave on stroboscopy | n/a | Typical in primary LTB (Guan: *"Mucosal waves were typically absent on laryngostroboscopy examination."*) | PMID 35634235 |
| Impaired vocal fold mobility | Vocal cord paresis/paralysis | 6% (Rubin) | PMID 38238187 |
| Airway obstruction / dyspnoea needing tracheotomy | Stridor; Dyspnea | Tracheotomy in 1% (Rubin) | PMID 38238187 |
| Constitutional symptoms (fever, weight loss, night sweats) | Fever; Weight loss; Night sweats | Often absent; none of the 3 Nerurkar patients had them | PMID 38440428 |
| Cough / pulmonary findings | Cough | Abnormal chest CT in 71.2% vs abnormal chest X-ray in 25.6% (Gao) | PMID 37979215 |

**Phenotype characteristics:**
- **Onset:** adults, with a subacute or chronic course.
- **Time to diagnosis:** median 3 months (Rubin).
- **Severity:** usually mild to moderate. Airway compromise is rare.
- **Quality of life:** dysphonia is the main burden. A 2024 PRISMA review of 36 articles reports lasting dysphonia, mainly from vocal fold involvement ([Redalyc](https://www.redalyc.org/journal/817/81782334017/81782334017.pdf)). No EQ-5D or SF-36 data were found.

## 4. Genetic / Molecular Information

- **Causal genes:** none in the human host. The disease is infectious.
- **ClinVar, gnomAD, pathogenic variants, modifier genes, epigenetics, chromosomal abnormalities:** not applicable or not available for LTB specifically.
- **Pathogen genetics:** drug resistance in the infecting strain is relevant clinically. Resistance was reported in 0.5% of pooled cases (Rubin 2024, PMID 38238187). Strain-level data specific to laryngeal TB were not retrieved.

## 5. Environmental Information

- **Infectious agent:** *Mycobacterium tuberculosis* (*M. tuberculosis* complex). The NCBI Taxon ID was not retrieved in this session and needs verification.
- **Lifestyle:** smoking was reported in 41% of pooled cases (PMID 38238187). Alcohol was not quantified in the retrieved sources.
- **Population context:**
  - The WHO Global TB Report 2024 counted 8.2 million people newly diagnosed with TB in 2023 and about 1.25 million TB deaths in 2023 ([WHO](https://www.who.int/teams/global-tuberculosis-programme/tb-reports/global-tuberculosis-report-2024); [CIDRAP](https://www.cidrap.umn.edu/tuberculosis/who-report-shows-global-tuberculosis-cases-are-rising)).
  - The later WHO release reported 1.23 million deaths in 2024 ([UN News](https://news.un.org/en/story/2025/11/1166349)).

## 6. Mechanism / Pathophysiology

**Causal chain.** Steps marked *[inferred]* are extrapolated from general TB biology and were not shown specifically in the larynx.

1. **Initiating infection.** Bacilli reach the laryngeal mucosa. There are two branches:
   - **1a (secondary LTB).** Expectorated sputum from active pulmonary (often cavitary) TB is deposited on the posterior glottis and vocal folds. This leads to direct mucosal inoculation. The mechanism is the classic one and is supported by the 54–56% rate of co-existing lung disease (PMIDs 38238187, 37979215).
   - **1b (primary LTB).** Inhaled droplets seed the larynx directly, or bacilli spread by blood or lymph from an occult focus. This leads to isolated laryngeal disease with a negative pulmonary workup (PMID 35634235). *[The route is inferred.]*
2. **Uptake by macrophages.** *M. tuberculosis* is taken up by and resides in macrophages within the laryngeal lesions. This was **demonstrated** by immunofluorescence and in situ hybridization in a human biopsy (Achache 2023, PMID 38133296, paraphrased).
3. **Granuloma formation.** Infected macrophages trigger cell-mediated immunity, with T-cell recruitment, epithelioid transformation and Langhans giant cells. This produces granulomatous inflammation. *[The T-cell steps are inferred from general TB biology; the granuloma itself is shown on histology.]*
4. **Caseous necrosis.** Central necrosis follows, leading to mucosal ulceration of the vocal folds and laryngeal mucosa (demonstrated histologically, PMID 38133296; MeSH scope note).
5. **Clinical expression.** Glottic lesions, oedema and ulceration cause stiffness of the vocal fold cover. This leads to an absent mucosal wave and **hoarseness**. Supraglottic or epiglottic ulceration leads to **odynophagia** (PMIDs 35634235, 37979215).
6. **Complications.** Two downstream outcomes branch from here:
   - **6a.** Deep or advanced disease leads to impaired fold mobility (6%) and to airway compromise or a need for tracheotomy (1%).
   - **6b.** Healing with fibrosis leads to scar-like mucosa (34.4% at follow-up in Gao) and persistent dysphonia or other laryngeal sequelae (5%, Rubin).
7. **Transmission.** Laryngeal disease produces highly infectious aerosols, leading to onward transmission (Braden 1995, PMID 8527545: *"The source case was highly infectious; transmission following only a few hours of exposure was documented."*).

**Checklist coverage:**
- **Cellular processes and immune involvement:** granuloma formation, macrophage-resident intracellular bacteria, Th1-type cell-mediated immunity *[inferred]*, and caseous necrosis.
- **Tissue damage:** necrosis, ulceration and fibrosis.
- **Molecular pathways, proteomics, metabolomics, single-cell data, and other omics:** **no laryngeal-specific data were retrieved.**
- **Suggested GO labels (IDs unverified):** granuloma formation; macrophage activation; response to bacterium; inflammatory response; necrotic cell death; T cell mediated immunity.
- **Suggested CL labels:** macrophage; epithelioid cell; multinucleated giant cell (Langhans); T cell (CD4+); squamous epithelial cell (vocal fold).

## 7. Anatomical Structures Affected

- **Primary organ:** larynx (UBERON label "larynx").
- **Sites:**
  - The true vocal folds are the most frequent site. The glottis was involved in 87.3% in Gao; Migliorelli notes *"Most cases involved the true vocal folds."*
  - Other sites are the false folds, ventricle, epiglottis (Raj 2022, PMID 35131802) and subglottis (PMID 39559153, title only).
- **Suggested UBERON labels:** larynx; vocal cord; vestibular fold; epiglottis; laryngeal mucosa.
- **Secondary involvement:** lungs, in about 54–56% of cases. Disseminated TB can occur; one of Guan's 3 patients *"developed disseminated tuberculosis despite optimal therapy."*
- **Body systems:** respiratory system (upper and lower airway).
- **Tissue and cell level:** laryngeal mucosa (stratified squamous and respiratory epithelium) and lamina propria. The cells involved are macrophages and granuloma cells.
- **Subcellular level:** bacteria reside inside macrophages, in the phagosome *[inferred]*. Suggested GO cellular component label: phagocytic vesicle.
- **Laterality:** lesions can be unilateral or bilateral. Raj 2022 describes bilateral true-cord involvement; Guan 2022 describes irregular lesions on one fold.

## 8. Temporal Development

- **Onset:** adults. Case ages range from 24 to 73 years in the retrieved reports (PMIDs 35131802, 37927677, 35634235). The onset is insidious, subacute or chronic.
- **Diagnostic delay:** median 3 months (PMID 38238187).
- **Course:** without treatment the disease progresses. With standard therapy, symptoms resolve 4–16 weeks after starting treatment (PMID 39111930). No formal staging system exists.
- **Remission:** remission is treatment-induced; pooled cure was 99% (PMID 38238187).
- **Critical period:** early diagnosis, before biopsy under general anaesthesia, matters for infection control. Teixeira Marques advises a chest X-ray before rigid laryngoscopy for any suspicious laryngeal lesion (PMID 39111930).

## 9. Inheritance and Population

- **Inheritance, penetrance and related genetic features:** not applicable. The disease is infectious.
- **Epidemiology:** no population prevalence or incidence figures specific to LTB were found. Proportional estimates are below.

| Measure | Value | Source |
|---|---|---|
| Share of all TB | About 1% | PMID 36541378 |
| Share of extrapulmonary TB | Under 1% | [PMC10624933](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10624933/) |
| Share of head and neck TB, pooled meta-analysis (57 studies) | 8.7% (second after cervical nodes) | Qian 2019, PMID 31080090, paraphrased |
| Share of head and neck TB, literature analysis | 38.92% (larynx was the most common site, alongside cervical nodes at 38.28%) | Pang 2018, PMID 29323108 |
| Share of head and neck TB, single centres | 4.8% (India, n=104; [PMC5446342](https://pmc.ncbi.nlm.nih.gov/articles/PMC5446342)); 25.5% (Japan, n=47); 27.4% (Warsaw, n=73) | Search-retrieved series |
| Voice-clinic prevalence | 3/890 (0.3%) | PMID 38440428 |

- **Sex:** male predominance (8:2 in PMID 39111930).
- **Geography:** follows the TB burden, with high-burden areas in South and Southeast Asia, China and sub-Saharan Africa (PMIDs 32328767, 37979215).
- **Trend:** the pattern is reported to be changing, with more primary and atypical presentations and fewer classic constitutional symptoms (PMID 38440428).

## 10. Diagnostics

- **Laryngoscopy and stroboscopy:** irregular, ulcerative, exophytic or oedematous lesions with an absent mucosal wave. The appearance is often taken for cancer; in Migliorelli's review the initial suspicion was laryngeal cancer in 64 cases (snippet; denominator unknown).
- **Biopsy and histopathology (reference standard):**
  - Findings are granulomatous inflammation with caseous necrosis, plus Ziehl–Neelsen acid-fast bacilli (PMIDs 38133296, 35131802).
  - Bacteriological confirmation was achieved in only 28% of pooled cases (PMID 38238187).
  - Nerurkar considers excisional biopsy with histology essential in primary LTB (PMID 38440428).
- **Molecular testing:**
  - Xpert MTB/RIF on biopsy tissue gave a result within 24 h in Guan 2022.
  - Xpert was positive in only 1 of 5 LTB cases in the South African study (PMID 32328767, unverified summary).
  - Mycobacterial identification on homogenised biopsy speeds diagnosis (Yu 2020, PMID 33336005).
- **Sputum AFB smear and culture:** positive mainly in secondary LTB. Sputum tests perform poorly in head and neck TB overall (PMID 31080090).
- **Imaging:**
  - Chest CT detects lung involvement better than chest X-ray: 71.2% vs 25.6% positive (PMID 37979215).
  - Laryngeal CT may mimic carcinoma (El Kettani 2010, PMID 20351985).
  - ¹⁸F-FDG PET/CT can show avid uptake that mimics carcinoma (PMID 29889030, title only).
- **Immunological tests:** tuberculin skin test or IGRA. The Mantoux test was negative in Guan's primary cases.
- **Genetic, omics and liquid-biopsy testing:** not applicable.
- **Differential diagnosis:**
  - Laryngeal squamous cell carcinoma, the main mimic.
  - Other granulomatous diseases: sarcoidosis, granulomatosis with polyangiitis, fungal infection (histoplasmosis), syphilis, leprosy.
  - Non-tuberculous laryngeal granulomas (PMID 41001724, title only).
  - Contact granuloma, and laryngitis or leukoplakia.
- **Screening:** none for asymptomatic individuals. Contact investigation uses TST or IGRA (see §13).

## 11. Outcome / Prognosis

The pooled outcomes below come from Rubin 2024 (PMID 38238187, paraphrased).

| Outcome | Rate |
|---|---|
| Cure | 99% |
| Death | 0.5% |
| Drug resistance | 0.5% |
| Treatment adverse events | 6% |
| Laryngeal sequelae | 5% |

- **Follow-up in Gao 2024 (n=42 followed):** 73.8% improved significantly. Mucosa returned to normal in 59.4% and became scar-like in 34.4% (PMID 37979215).
- **Complications:**
  - Persistent dysphonia and vocal fold scarring.
  - Glottic or subglottic stenosis and airway obstruction needing tracheotomy (1%; PMID 28215824, title).
  - Disseminated TB (PMID 35634235).
  - Transmission to contacts.
- **Prognostic factors:**
  - **Inferred:** deeper or extensive lesions, delayed diagnosis, drug resistance, and HIV or immunosuppression predict worse outcomes.
  - **Not inferred:** no validated prognostic biomarkers were retrieved.

## 12. Treatment

- **Pharmacotherapy:**
  - Standard first-line regimen is 2 months of isoniazid, rifampicin, pyrazinamide and ethambutol (HRZE), then 4 months of isoniazid and rifampicin (HR). Median treatment duration was 6 months, and a 4-drug regimen was used in 80% of cohorts (PMID 38238187).
  - The case reports used RIPE or HRZE for 6 months (PMIDs 35131802, 37927677).
  - Drug-resistant TB requires WHO regimens for MDR or rifampicin-resistant TB (not retrieved in detail).
- **Suggested NCIT and CHEBI labels:** isoniazid; rifampicin; pyrazinamide; ethambutol. NCIT labels: Antitubercular Agent; Directly Observed Therapy.
- **Pharmacogenomics:** NAT2 acetylator status affects isoniazid toxicity in general TB treatment. This was **not retrieved in this session**, so it needs verification.
- **Surgical and interventional:**
  - Diagnostic biopsy or microlaryngoscopic excision (PMID 38440428).
  - Tracheotomy for airway obstruction (PMID 28215824).
  - Late phonosurgery or airway surgery for sequelae.
- **Supportive and rehabilitative:** voice therapy and voice assessment after treatment (MDVP analysis in PMID 35131802; voice focus in PMID 36541378). No outcome data on speech therapy were retrieved.
- **Advanced or experimental therapies (gene, cell, RNA, immunotherapy):** not applicable. No LTB-specific trials or NCT IDs were found.
- **Response:** symptoms resolve within 4–16 weeks (PMID 39111930). Lesions showed *"almost complete resolution"* in Raj 2022 (PMID 35131802). In Gautam 2023 (PMID 37927677), ulcers regressed by 2 months.

## 13. Prevention

- **Primary prevention:**
  - Early detection and treatment of pulmonary TB, which prevents secondary LTB.
  - BCG vaccination, mainly protective against severe childhood TB. No LTB-specific data were retrieved.
  - Smoking cessation (inferred from the 41% smoking rate).
  - HIV control.
- **Infection control:**
  - LTB is highly infectious. In Braden 1995, *"TST conversions were documented in 23 students; eight had, at most, 5 hours of classroom contact"* (PMID 8527545).
  - Airborne precautions are needed for laryngoscopy and biopsy. A decision tree for protecting healthcare workers exists (Roberts 2008, PMID 18596478).
  - Chest imaging before rigid endoscopy is advised (PMID 39111930).
- **Secondary prevention:** contact tracing with TST or IGRA, and preventive treatment of contacts with latent infection.
- **Tertiary prevention:** completing therapy, and monitoring the airway and voice for stenosis.
- **Genetic counseling:** not applicable.

## 14. Other Species / Natural Disease

- **Animal laryngeal TB:** no reports of naturally occurring laryngeal TB in animals were retrieved.
- **Mycobacterium bovis in cattle:** causes granulomatous disease, and atypical granulomas have been described in calves ([PMC6629060](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6629060/)). Laryngeal lesions were not specifically described in that source.
- **Zoonotic potential:** *M. bovis* is a recognised zoonotic member of the *M. tuberculosis* complex. Its role in laryngeal disease was not documented in the retrieved sources.
- **OMIA:** not applicable.

## 15. Model Organisms

- **Laryngeal-specific models:** none were found.
- **General TB models:**
  - **Guinea pig.** Granulomas progress from macrophage aggregates to caseous necrosis with abundant acid-fast bacilli. Unlike in humans, *"Multinucleated giant cells are very rare and fibrotic capsules are not formed"* ([PMC10556493](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10556493/)). These data come from lung infection.
  - **Mouse, non-human primate and zebrafish** (*M. marinum*) models are standard in TB research. They were not retrieved in this session.
- **Limitations:** no model reproduces laryngeal involvement, vocal fold lesions or voice outcomes. Human biopsy studies remain the main evidence for laryngeal pathology (PMID 38133296).

---

### Key PMIDs (retrieved this session)

| PMID | First author, year | Study |
|---|---|---|
| 38238187 | Rubin 2024 | SWiM review, 119 articles |
| 37979215 | Gao 2024 | Cohort, n=134 |
| 39111930 | Teixeira Marques 2024 | Series, n=10 |
| 38440428 | Nerurkar 2024 | Voice-clinic series |
| 36541378 | Migliorelli 2022 | Case report and review |
| 35634235 | Guan 2022 | Primary LTB, 3 cases |
| 35131802 | Raj 2022 | Case report |
| 37927677 | Gautam 2023 | Case report |
| 38133296 | Achache 2023 | Macrophage localisation |
| 29323108 | Pang 2018 | Head and neck TB series and review |
| 31080090 | Qian 2019 | Head and neck TB meta-analysis |
| 32328767 | Matimba 2020 | High-burden-area diagnosis |
| 33336005 | Yu 2020 | Homogenised biopsy |
| 20351985 | El Kettani 2010 | CT features |
| 8527545 | Braden 1995 | Infectiousness |
| 18596478 | Roberts 2008 | Healthcare worker protection |
| 26628760 | Lodha 2015 | Secondary LTB |

**Sources (web):**
- [MeSH D014387](https://meshb.nlm.nih.gov/record/ui?ui=D014387)
- [NHS ICD-10 A15–A19](https://classbrowser.nhs.uk/ICD-10-5TH-Edition/vol1/block-a15-a19.htm)
- [gesund.bund.de A15.5](https://gesund.bund.de/en/icd-code-search/a15-5)
- [autoicdapi A15.5](https://autoicdapi.com/reference/icd-10/A15.5)
- [WHO Global TB Report 2024](https://www.who.int/teams/global-tuberculosis-programme/tb-reports/global-tuberculosis-report-2024)
- [CIDRAP](https://www.cidrap.umn.edu/tuberculosis/who-report-shows-global-tuberculosis-cases-are-rising)
- [UN News 2025](https://news.un.org/en/story/2025/11/1166349)
- [PMC9103562](https://pmc.ncbi.nlm.nih.gov/articles/PMC9103562)
- [PMC10624933](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10624933/)
- [PMC5446342](https://pmc.ncbi.nlm.nih.gov/articles/PMC5446342)
- [PMC5837174](https://pmc.ncbi.nlm.nih.gov/articles/PMC5837174)
- [PMC10745871](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10745871/)
- [PMC10556493](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10556493/)
- [PMC6629060](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6629060/)
- [Redalyc voice-outcome review](https://www.redalyc.org/journal/817/81782334017/81782334017.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 27 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 27 |
| On topic | 9 |
| Off topic | 0 |

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
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0005819` (2 mentions) - the report calls it "MONDO"; MONDO calls it **laryngeal tuberculosis**

### Terms whose obsolescence could not be checked

1 term(s) resolved, so they exist, but the ontology service was unreachable for the deprecation check -- treat their obsolescence as unknown rather than clean, and re-run to confirm:

- `MONDO:0005819` (2 mentions)