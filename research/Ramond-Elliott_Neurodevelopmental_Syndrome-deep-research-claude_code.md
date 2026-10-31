---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-23T01:55:32.081090'
end_time: '2026-10-23T01:58:41.642187'
duration_seconds: 189.56
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Ramond-Elliott Neurodevelopmental Syndrome
  mondo_id: MONDO:0980751
  category: Mendelian
  causal_genes: TRA2B
  omim_id: not recorded
  synonyms: not recorded
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
  web_search_requests: 5
  num_turns: 18
  total_cost_usd: 2.0207005000000002
  session_id: f5646ea6-2421-49e9-8a90-b3b75ae6b2e6
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  - mcp__pubmed__search_articles
  assistant_text_blocks: 3
citation_count: 8
reference_validation:
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 8
  on_topic: 6
  validator_version: 0.3.0
term_validation:
  total_terms: 50
  verified: 50
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 3
  labels_matching: 0
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0980751
    reported_labels:
    - MONDO
    ontology_label: Ramond-Elliott neurodevelopmental syndrome
  - term_id: DOID:0070715
    reported_labels:
    - appears in search results; confirm it is this disease
    ontology_label: Ramond-Elliott neurodevelopmental syndrome
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Ramond-Elliott Neurodevelopmental Syndrome
- **MONDO ID:** MONDO:0980751 (if available)
- **Causal gene(s):** TRA2B
- **OMIM:** not recorded
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Ramond-Elliott Neurodevelopmental Syndrome** covering all of the
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

I'm pulling the full texts of the two TRA2B papers, the 2023 Ramond cohort and the 2023 Shatokhina case report, to get variant and phenotype details.

Try reading the PDF directly.

# Ramond-Elliott Neurodevelopmental Syndrome (RAMELN; TRA2B): Research Report

**Target:** Ramond-Elliott neurodevelopmental syndrome, MONDO:0980751. **Causal gene: *TRA2B*** (transformer 2 beta homolog; OMIM gene 602719; NCBI Gene 6434). The disease is OMIM 621421.

**How this was researched.** My PubMed tool call was declined, so the evidence comes from three places. The first is the full text of the founding paper, Ramond et al. 2023 (CC BY 4.0, read from the Newcastle ePrints PDF). The second is the full text of the second case report on PMC (Shatokhina et al. 2023). The third is database records (KEGG, PanelApp) and the abstracts of two mouse knockout papers. Quotes marked *[abstract]* match the cached `references_cache/PMID_36549593.md` exactly. Other quotes are from full text and should be re-checked before they are used as snippets. **Every ontology CURIE below is a lead written from memory and not looked up.** Under this repo's term contract, each one must be resolved with OAK/OLS before it is bound.

---

## 1. Disease Information

**Overview.** RAMELN is an autosomal dominant neurodevelopmental syndrome. It is caused by heterozygous, predicted loss-of-function variants that cluster in the 5′ coding region of *TRA2B*, upstream of an alternative translation start site in exon 3. Its core features are:
- intellectual disability or developmental delay, usually severe;
- infantile-onset epilepsy, often infantile spasms;
- axial or global hypotonia;
- microcephaly and nonspecific brain anomalies;
- behavioural problems, including autism;
- feeding difficulties and short stature.

It is the first human disease linked to germline variants in a transformer-2 gene.

> "Predicted loss-of-function variants clustered in the 5' portion of TRA2B cause a new neurodevelopmental syndrome through an apparently dominant negative disease mechanism involving the use of an alternative translation start site and the overexpression of a shorter, repressive Tra2β protein." *[abstract, PMID:36549593]*

| Identifier | Value | Source |
|---|---|---|
| MONDO | MONDO:0980751 | task input |
| OMIM (phenotype) | 621421 | KEGG H03032; Disease Ontology xref |
| OMIM (gene) | 602719 | search result |
| KEGG Disease | H03032 | [KEGG](https://www.kegg.jp/entry/H03032) |
| DOID | DOID:0070715 (appears in search results; confirm it is this disease) | [Disease Ontology](https://disease-ontology.org/term/DOID:0070715/owl) |
| ICD-11 | LD90.Y, a nonspecific "conditions with disorders of intellectual development" code | KEGG |
| Orphanet / MeSH / ICD-10 | none found | — |
| HGNC | believed to be hgnc:10781 (**unverified, look up**) | — |

- **Synonyms:** RAMELN; TRA2B-related neurodevelopmental disorder. The name honours the first and last authors, Francis Ramond and David Elliott.
- **Nature of the data:** Everything comes from individual patient case series and reports. One is a GeneMatcher cohort of 12 individuals; the other is a single case. There are no registry or EHR data.
- **No GeneReviews chapter** was found.

## 2. Etiology

- **Cause:** Heterozygous germline variants in the 5′ part of *TRA2B*: start-loss, nonsense, and splice variants at the exon 2/3 boundary.
- **Origin:**
  - De novo in 10 of 11 Ramond families.
  - In one family, an affected father (individual 8, age 31) passed the variant to his affected son (individual 9). Grandparents were not available for testing.
  - The Shatokhina proband's variant was de novo. Parental germline mosaicism was not excluded.
- **Genetic risk factors beyond the causal variant:** none known. No susceptibility loci, modifier genes or protective alleles are reported.
- **Environmental risk, protective factors and gene-environment interactions:** none reported, and none expected for a de novo monogenic developmental disorder.

## 3. Phenotypes

The frequencies below come from Ramond et al. 2023 (n=12: 5 female, 7 male; aged 2–14 years plus one adult aged 31), unless marked as coming from the Shatokhina case (S).

| Phenotype | Frequency / detail | Candidate HPO (verify) |
|---|---|---|
| DD/ID | 12/12 (100%): severe–profound 6, moderate–severe 2, mild–moderate 3, unknown 1 | HP:0001249 Intellectual disability; HP:0001263 Global developmental delay |
| Axial/global hypotonia, neonatal–infantile onset | 10/12 (83%); also S | HP:0001252 Hypotonia (HP:0008936 for axial) |
| Motor delay | 12/12. Walked independently at 20 mo–6 y in 6/11; not yet walking in 5/11. S not walking at 14 mo | HP:0001270 Motor delay |
| Nonverbal (age 3–14 y) | 7/12 (58%); some speech in 4/12 | HP:0001344 Absent speech |
| Behavioural problems | 8/12 (66%) | — |
| Autism spectrum disorder | 4/12 (33%) | HP:0000729 Autistic behavior |
| Self-injury | 4/12 (33%) | HP:0100716 Self-injurious behavior |
| Frustration intolerance | 2/12 | — |
| Epilepsy, onset 3–9 months | 7/12 (58%); also S, onset 5 mo | HP:0001250 Seizure |
| Infantile spasms as first presentation | 6/12 (50%); also S, pharmacoresistant | HP:0012469 Infantile spasms |
| Hypsarrhythmia | 3 individuals; also S | HP:0002521 Hypsarrhythmia |
| Unclassified epileptic encephalopathy | 1 | HP:0200134 Epileptic encephalopathy |
| Evolution to Lennox-Gastaut syndrome | 1 | — |
| Head circumference below average | 10 individuals | — |
| Microcephaly (−2 to −4 SD) | 5/12 (42%) | HP:0000252 Microcephaly |
| Any brain anomaly on MRI | 10/11 (90%) | — |
| Mild diffuse atrophy or ventricular enlargement | 6/11 (54%) | HP:0002059 Cerebral atrophy; HP:0002119 Ventriculomegaly |
| Thin or hypoplastic corpus callosum | 4/11 (36%) | HP:0002079 Hypoplasia of the corpus callosum |
| Delayed myelination | 2; S had abnormal periventricular/subcortical white-matter signal | HP:0012448 Delayed myelination |
| Cerebellar hypoplasia | 1 | HP:0001321 Cerebellar hypoplasia |
| Focal cortical dysplasia (histology-proven, epilepsy surgery) | 1 | look up |
| Feeding difficulties | 7/12 (58%); 1 needed a gastrostomy | HP:0011968 Feeding difficulties |
| Height and weight < −2 SD | 4/12 (33%) | HP:0004322 Short stature |
| Chronic constipation | 5/12 (42%) | HP:0002019 Constipation |
| Sleep disturbance (night waking) | 3/12 (25%); 1 responded to melatonin | HP:0002360 Sleep abnormality |
| Minor cardiac malformations | 2/12 (17%); S had patent foramen ovale and mild left pulmonary artery stenosis | HP:0001627 Abnormal heart morphology |
| Cortical visual impairment | 3 | HP:0100704 Cortical visual impairment |
| Intermittent exotropia | 2 | HP:0000577 Exotropia |
| Astigmatism | 2 | HP:0000483 Astigmatism |
| Hearing | normal in all | — |
| Scoliosis | 4/12 (33%) | HP:0002650 Scoliosis |
| Hand/foot brachydactyly | 3/12 (25%) | HP:0001156 Brachydactyly |
| Cutaneous syndactyly | 2/12 (17%); S had toe 2–3 syndactyly | look up |
| Pectus excavatum | 1 | HP:0000767 Pectus excavatum |
| Fifth-finger clinodactyly | S only | HP:0004209 Clinodactyly of the 5th finger |
| Alopecia areata | S only | look up |

**Facial gestalt.** Features are "common but not constant" and only mildly specific. They include:
- long, slightly upslanting palpebral fissures; deep-set eyes; epicanthus;
- high nasal bridge, bulbous nasal tip, anteverted nares;
- smooth, short philtrum; thin upper lip; fleshy lower lip; open mouth;
- widely spaced teeth; low-set fleshy ears; rectangular chin.

The authors note some resemblance to Angelman syndrome and to chromatinopathies. The S proband also had a high forehead, low-set ears, macrostomia and macroglossia.

**Onset, severity and course.** Onset is congenital or infantile: hypotonia in the neonatal period or infancy, seizures at 3–9 months. Severity is usually severe and varies between patients. The disorder is neurodevelopmental and has not been described as degenerative. In the S proband, skills regressed after spasm onset.

**Quality of life.** No formal QoL instruments have been used. The main burdens are severe ID, the fact that most patients are nonverbal, refractory epilepsy in a subset, and feeding problems, including tube feeding.

## 4. Genetic and Molecular Information

**Gene and protein.** *TRA2B* is on chromosome 3 and has 9 protein-coding exons. It produces two isoforms that matter here:
- **Tra2β-1** (NP_004584.1, from NM_004593.3, the MANE transcript). This is the full-length protein, with domains in the order RS1 – RRM – RS2. It is expressed ubiquitously, including in the developing brain.
- **Tra2β-3** (NP_001230808.1, from NM_001243879.2). This transcript skips exon 2 and starts translation at a downstream ATG in exon 3. The resulting protein keeps the RRM and RS2 but **lacks RS1**. The isoform is normally expressed at low levels and in a tissue-restricted, developmentally regulated way.

**Variants.** Ramond reported 11 variants in 12 individuals, all heterozygous and all on NM_004593.3. All were absent from gnomAD, and none lies downstream of the Tra2β-3 start codon.
- **Start-loss (6):** c.1A>G, c.1A>T, c.2T>C, c.2T>G, c.2_4del, and a small 5′ deletion read from the figure as c.-11_22del. Confirm the exact HGVS against Supplemental Table 2.
- **Nonsense (2):** read from the figure as c.16G>T p.(Glu6Ter) and a second variant near codon 7. Confirm both in Supplemental Table 2.
- **Splice (3):** c.170+1del, c.170+2T>C, c.171-2A>G.
- **Shatokhina:** c.170+1G>A, p.Glu13Valfs*2, ClinVar SCV004032532. Classified pathogenic (PVS1, PS2, PM2). Fibroblast RT-PCR showed an aberrant transcript lacking exon 2 (134 bp shorter).

The authors state that the Ramond variants would meet ACMG criteria for likely pathogenic or pathogenic if *TRA2B* were an established disease gene.

**Functional class.** Each variant looks like loss-of-function on its own, but the authors argue the disease acts through a **dominant-negative** mechanism: Tra2β-1 is lost and the RS1-less Tra2β-3 is relatively overexpressed. They explicitly leave open a **gain-of-function** effect of Tra2β-3 that does not depend on Tra2β-1. Three findings argue against simple haploinsufficiency:
1. Heterozygous *Tra2b* knockout mice appear normal.
2. In individual 5 (c.2_4del), the mutant allele's mRNA is expressed at about 50% and is not degraded by nonsense-mediated decay.
3. The variants cluster tightly in the 5′ region.

**Other genetic categories.** No modifier genes, epigenetic findings, chromosomal abnormalities or somatic contributions are reported. Population carrier frequency is effectively zero, since the variants are absent from gnomAD.

**Panel curation.**
- PanelApp Australia: Green (high evidence), monoallelic, on its ID/epilepsy panels.
- Genomics England "Severe microcephaly" panel: Amber, because only two unrelated cases had severe microcephaly.

## 5. Environmental Information

Not applicable. No environmental, lifestyle or infectious contributors are known.

## 6. Mechanism and Pathophysiology

**Causal chain:**
1. A heterozygous variant in the 5′ coding region (exon 1 to the exon 2/3 boundary) **prevents production of full-length Tra2β-1 from that allele**. It does this by removing the start codon, adding a premature stop, or causing exon 2 to be skipped. This was shown by western blot with an N-terminal antibody in 4 patient cell lines.
2. On the mutant allele, translation **re-initiates at the alternative ATG in exon 3**, which **increases expression of the ~20 kDa Tra2β-3 isoform**. This was shown with a C-terminal antibody in fibroblasts and lymphoblastoid cells. Whether Tra2β-3 comes specifically from the mutant allele is inferred, not proven.
3. Tra2β-3 still has its RRM, so it **binds the same exonic sites (AGAA-rich) as Tra2β-1**. Because it lacks RS1, it cannot recruit the spliceosome. It therefore acts as a **competitive splicing repressor**. This part is demonstrated in vitro: in HEK293 cells, a Tra2β-3-GFP construct reduced *CHEK1* exon 3 inclusion in a dose-dependent way, even when Tra2β-1-GFP was co-expressed.
4. This **reduces inclusion of exons that depend on Tra2β** in patient cells. *CHEK1* exon 3 PSI was 56% in patient lymphoblastoid cells against 88% in controls. The genes whose missplicing actually causes the brain phenotype are **unknown**. The authors suggest candidates whose loss causes overlapping syndromes: *NIPBL* (Cornelia de Lange), *ATRX* (ATR-X) and *SON* (ZTTK). This step is inferred.
5. **Abnormal splicing during brain development** (inferred) leads to:
   - 5a. disturbed cortical and white-matter development, giving microcephaly, atrophy, ventriculomegaly, a thin corpus callosum and delayed myelination. Mouse data suggest **apoptosis of neural progenitors** as one route: neuron-specific *Tra2b* knockout mice show massive apoptosis in the cortical ventricular layers and p21 upregulation (PMID:24586484).
   - 5b. cortical network hyperexcitability, giving infantile spasms and epileptic encephalopathy. The mechanism is unknown.
6. The clinical result is ID/DD, epilepsy, hypotonia, behavioural problems including autism, and feeding difficulties and growth failure. How systemic features such as short stature and skeletal anomalies arise is **not established**.

**Cellular and subcellular context.** Splicing regulation happens in the nucleus; SR-type proteins localise to nuclear speckles. The likely relevant cells are neurons and neural progenitors of the developing cortex. Patient-derived assays used lymphoblastoid cells and fibroblasts. No metabolic, immune or omics signatures have been described beyond RNA-seq in one patient's lymphoblastoid cells, which showed no global change in *TRA2B* expression.

**Candidate ontology terms (verify all):**
- GO biological process: GO:0000381 regulation of alternative mRNA splicing, via spliceosome; GO:0048025 negative regulation of mRNA splicing, via spliceosome; GO:0021987 cerebral cortex development; GO:0006915 apoptotic process.
- GO molecular function / cellular component: GO:0003729 mRNA binding; GO:0016607 nuclear speck.
- Cell types: CL:0000540 neuron; CL:0011020 neural progenitor cell.

## 7. Anatomical Structures Affected

- **Primary site:** the brain. Candidate UBERON terms: cerebral cortex UBERON:0000956, corpus callosum UBERON:0002336, cerebral white matter, cerebellum UBERON:0002037.
- **Secondary involvement:**
  - visual pathways (cortical visual impairment);
  - gastrointestinal tract (feeding problems, constipation);
  - skeleton (scoliosis, brachydactyly, pectus excavatum);
  - heart (minor malformations);
  - growth.
- **Lateralisation:** findings are bilateral and diffuse. The one focal cortical dysplasia was a single lesion.

## 8. Temporal Development

- **Onset:** congenital or infantile. Hypotonia starts in the neonatal period or infancy, and seizures start at 3–9 months.
- **Epilepsy course** in the Ramond cohort:
  - Spasms resolved in late infancy in 3 individuals. Two of them were seizure-free and off medication in adolescence; the third became seizure-free at 6 years after steroids and valproate.
  - Epilepsy evolved unfavourably in 3: one had an unspecified epileptic encephalopathy, one became drug-resistant despite vagus nerve stimulation, and one progressed to Lennox-Gastaut syndrome.
- **Overall course:** lifelong and static. No staging exists. Infancy, when spasms start, is the critical window for treatment.

## 9. Inheritance and Population

- **Inheritance:** autosomal dominant (candidate term HP:0000006). Penetrance was "possibly full" according to the authors, but is unproven with only one transmitting family. Expressivity is variable.
- **Epidemiology:** no prevalence or incidence data. About 13 cases have been published worldwide, which places it in the Orphanet band below 1 in 1,000,000. Record the measure as `CASES_IN_LITERATURE`.
- **Population features:** the 7 males and 6 females come from Europe (France, Germany, Italy, UK, Denmark), Israel, Chile, the USA and Russia. No founder effects, no role for consanguinity, and no carrier frequency are reported.

## 10. Diagnostics

- **Recommended test:** exome or genome sequencing. All cases were found by clinical exome sequencing. *TRA2B* is on ID, epilepsy and microcephaly panels (PanelApp Australia; Genomics England).
- **Supporting tests:**
  - EEG, which may show hypsarrhythmia.
  - Brain MRI, which may show nonspecific atrophy, ventriculomegaly, a thin corpus callosum or delayed myelination.
  - RT-PCR or RNA studies to confirm splice variants, as Shatokhina did with exon 2 skipping.
  - Western blot for the Tra2β-1 to Tra2β-3 ratio. This is research use only.
- **Not useful:** chromosomal microarray, karyotype and FISH, which do not detect point variants.
- **Biomarkers and criteria:** there are no biochemical biomarkers and no formal diagnostic criteria.
- **Differential diagnosis:** the authors tested for and excluded several conditions in some patients:
  - Angelman syndrome (methylation PCR);
  - *ARX* and *MECP2* disorders;
  - Coffin-Siris syndrome and other chromatinopathies;
  - mitochondrial disease (mtDNA sequencing).
  Other infantile spasm aetiologies should also be considered.
- **Screening:** there is no newborn or carrier screening.

## 11. Outcome and Prognosis

- **Survival:** no data on survival or mortality. The oldest known individual is a 31-year-old father with a milder presentation, so survival into adulthood is possible.
- **Morbidity:** severe ID in most patients, a nonverbal majority, delayed or absent walking, and refractory epilepsy in about a quarter of the cohort (3/12).
- **Prognostic factors:** none established. Early resolution of spasms was seen in 3 patients.

## 12. Treatment

There is no disease-specific therapy. Care is symptomatic. Suggested NCIT terms for this care (Supportive Care NCIT:C15747, Physical Therapy NCIT:C15302, Genetic Counseling NCIT:C15240) are listed in section 13.

| Treatment | Evidence | Candidate NCIT term (verify) |
|---|---|---|
| ACTH (tetracosactide) or steroids for spasms | S: seizures controlled for 4 months with tetracosactide plus topiramate, relapsing when topiramate was stopped. Ramond: seizure-free after steroids and valproate | Pharmacotherapy NCIT:C15986 + therapeutic_agent |
| Valproate, topiramate, ethosuximide | anecdotal | as above |
| Ketogenic diet | S: seizures controlled for 5 months, with cognitive gains. Ramond: one patient seizure-free from age 1 to 5 on the diet | Dietary Intervention NCIT:C15447 |
| Vagus nerve stimulation | failed in one patient | — |
| Epilepsy surgery | one resection, with focal cortical dysplasia on histology | Surgical Procedure NCIT:C15329 |
| Gastrostomy | one patient | — |
| Melatonin for sleep | helped one patient | — |
| Physical, occupational and speech therapy | standard care | NCIT:C15302 and others |

- **No clinical trials** were found.
- **Possible future direction:** isoform-switching antisense oligonucleotides that reduce Tra2β-3 or restore Tra2β-1. This is speculation only.

## 13. Prevention

- Prevention is through genetic counselling (NCIT:C15240).
- Recurrence risk is 50% when a parent carries the variant, as in the one transmitting family. In de novo cases it is low, but parental germline mosaicism cannot be excluded.
- Prenatal or preimplantation testing is possible once the family variant is known.
- Tertiary prevention: early treatment of spasms, and surveillance of feeding, vision and the spine.

## 14. Other Species / Natural Disease

No naturally occurring animal disease was found (OMIA not checked). *TRA2B* is conserved across vertebrates: the mouse orthologue *Tra2b* (also called *Sfrs10*) and a zebrafish orthologue in ZFIN (ZDB-GENE-040426-1094). The Tra2 family itself is conserved across the animal kingdom.

## 15. Model Organisms

| Model | Finding | PMID |
|---|---|---|
| Mouse, ubiquitous homozygous *Tra2b* (*Sfrs10*) knockout | Embryonic lethality around E7.5; heterozygotes normal | 20190275 (Mende et al. 2010, Hum Mol Genet; PMID taken from a database RDF link, so confirm it) |
| Mouse, Nestin-Cre neuronal *Tra2b* knockout | Death right after birth, severe cortical abnormalities, massive apoptosis in cortical ventricular layers, p21 upregulation | 24586484 (Storbeck et al. 2014, PLoS ONE) |
| Mouse, cortex-specific knockout | Brain abnormalities, but mice survive to adulthood | cited in Ramond; not retrieved |
| HEK293 overexpression and *CHEK1* exon 3 minigene | Tra2β-3 represses the exon in a dose-dependent way | 36549593 |
| Patient fibroblasts and lymphoblastoid cells | Tra2β-1 reduced, Tra2β-3 increased, *CHEK1* exon 3 PSI reduced | 36549593 |

**Key limitation.** No model carries the patients' allele. Heterozygous knockouts do not reproduce the disease, which supports the dominant-negative model but means causality has not been shown in an animal. This fits the repo's `HUMAN_MODEL_MISMATCH` discussion kind and its `FAILS_TO_RECAPITULATE` model link. A knock-in mouse carrying a start-loss or exon-2 splice variant, or a human iPSC-derived cortical organoid, would be the natural next experiment.

---

### Key References
- Ramond F, et al. Clustered variants in the 5′ coding region of TRA2B cause a distinctive neurodevelopmental syndrome. *Genet Med* 2023;25:100003. PMID:36549593. doi:10.1016/j.gim.2022.100003 ([NCL ePrints](https://apps-eprint4-l.ncl.ac.uk/289418))
- Shatokhina O, et al. TRA2B gene splice variant linked to seizures and neurodevelopmental delay: a second case study. *Int J Mol Sci* 2023;24:15572. PMID:37958557. doi:10.3390/ijms242115572 ([PMC10648248](https://pmc.ncbi.nlm.nih.gov/articles/PMC10648248/))
- Storbeck M, et al. Neuronal-specific deficiency of the splicing factor Tra2b causes apoptosis in neurogenic areas of the developing mouse brain. *PLoS ONE* 2014. PMID:24586484 ([PMC3929626](https://pmc.ncbi.nlm.nih.gov/articles/PMC3929626/))
- Mende Y, et al. Deficiency of the splicing factor Sfrs10 results in early embryonic lethality in mice. *Hum Mol Genet* 2010;19:2154–67. PMID:20190275 (confirm) ([MGI](https://informatics.jax.org/gxdlit/key/101892))
- [KEGG H03032](https://www.kegg.jp/entry/H03032); [PanelApp Australia](https://panelapp-aus.org/panels/202/gene/TRA2B/); [Genomics England PanelApp](https://panelapp.genomicsengland.co.uk/panels/162/gene/TRA2B/)

**Gaps.** My searches found no TRA2B case reports from 2024–2026, but this is not a complete PubMed sweep. There is no Orphanet entry, no GeneReviews chapter, and no ClinGen validity curation was found.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 8 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 50 |
| Resolved | 50 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 3 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0980751` (2 mentions) - the report calls it "MONDO"; MONDO calls it **Ramond-Elliott neurodevelopmental syndrome**
- `DOID:0070715` (3 mentions) - the report calls it "appears in search results; confirm it is this disease"; DOID calls it **Ramond-Elliott neurodevelopmental syndrome**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `NCIT:C15240` (2 mentions) - the report calls it "Prevention is through genetic counselling"; NCIT calls it **Genetic Counseling**