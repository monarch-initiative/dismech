---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-18T22:59:31.016888'
end_time: '2026-11-18T23:04:28.850212'
duration_seconds: 297.83
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: DNAJC6-Related Parkinson Disease
  mondo_id: MONDO:0014231
  category: Mendelian
  causal_genes: DNAJC6
  omim_id: OMIM:615528
  synonyms: juvenile onset Parkinson disease type 19A; DNAJC6 Parkinson disease; Parkinson
    disease caused by mutation in DNAJC6
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
  web_search_requests: 20
  num_turns: 26
  total_cost_usd: 1.2899116800000001
  session_id: 6d8f9f89-c35e-4f9c-95e6-59e4729015be
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  tool_calls: 34
  retrieval_calls: 32
  assistant_text_blocks: 4
citation_count: 23
reference_validation:
  total_references: 22
  verified: 22
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 22
  on_topic: 12
  validator_version: 0.8.0
term_validation:
  total_terms: 2
  verified: 1
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0014231
    reported_labels:
    - MONDO
    ontology_label: juvenile onset Parkinson disease 19A
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** DNAJC6-Related Parkinson Disease
- **MONDO ID:** MONDO:0014231 (if available)
- **Causal gene(s):** DNAJC6
- **OMIM:** OMIM:615528
- **Synonyms:** juvenile onset Parkinson disease type 19A; DNAJC6 Parkinson disease; Parkinson disease caused by mutation in DNAJC6
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **DNAJC6-Related Parkinson Disease** covering all of the
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

Let me try PubMed via E-utilities directly.

Still gathering sources; I have the core clinical and model papers and am now checking identifiers and recent mechanistic work.

I could not read the GeneReviews page. https://www.ncbi.nlm.nih.gov/books/NBK570369/ returned HTTP 200, but the body is a browser-check interstitial ("Checking your browser - reCAPTCHA ... Click here if you are not automatically redirected after 5 seconds"), not the article. The page's actual content was not returned to me.

Because this is a bot-check block rather than a transient failure, fetching the same URL again would likely return the same interstitial. I did not try variant URLs, since the instructions say not to guess at URLs.

Nothing from the requested sections is verified. That covers the authors, dates, summary, clinical characteristics, phenotype table, genotype-phenotype correlations, prevalence, management, genetic counseling, molecular genetics, and PMIDs. I have not filled these in from memory.

Options to get the content:
- Open the URL in a normal browser and paste the text here, or save it and point me to it.
- Use the NCBI E-utilities or the Bookshelf API from an authenticated or proxied client, if one is available.
- Use the PubMed record for the GeneReviews chapter's citation, if you have it, which would cover the abstract and metadata only.

URL read: https://www.ncbi.nlm.nih.gov/books/NBK570369/ (interstitial only, no article content).

# DNAJC6-Related Parkinson Disease (PARK19A / PARK19B): Research Report

**How this report was scoped:** It follows the identifiers you gave: MONDO:0014231, OMIM #615528, causal gene **DNAJC6**. OMIM treats juvenile-onset PARK19A as the main entity and early-adult-onset PARK19B as an included entity, so both are covered.

**Limits of the evidence:**
- Direct PubMed E-utilities queries were blocked in this environment.
- GeneReviews (NBK570369) returned a bot-check page, so only search-snippet text from it is used.
- PMIDs are given only where a retrieved page showed them. Where only a DOI or PMC ID was retrieved, that is what is given.
- Ontology terms (HPO, GO, CL, UBERON, NCIT, CHEBI) are given as **labels only**. Their numeric IDs were not retrieved and must be checked before you load them into the knowledge base.

---

## 1. Disease Information

**Overview.** DNAJC6-related Parkinson disease is an autosomal recessive monogenic parkinsonism. It is caused by biallelic loss-of-function variants in **DNAJC6**, which encodes **auxilin**. Auxilin is a neuron-enriched HSP40 (J-domain) co-chaperone that recruits Hsc70 to strip the clathrin coat from vesicles during synaptic vesicle endocytosis.

OMIM's description (mirror of OMIM 615528, [link](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/615528)) defines two forms:
- **PARK19A:** autosomal recessive parkinsonism with onset in the first or second decade. Some patients also have intellectual disability and seizures.
- **PARK19B:** onset in the third to fifth decade, slowly progressive, resembles late-onset PD, and responds well to dopaminergic therapy.

GeneReviews says "the majority of individuals have juvenile onset" (before age 21 years). It describes the juvenile form as "rapidly progressive with loss of ambulation in mid-adolescence in the majority of individuals" ([GeneReviews NBK570369](https://www.ncbi.nlm.nih.gov/books/NBK570369/), snippet level only).

**Identifiers**

| Resource | ID | Source |
|---|---|---|
| OMIM (phenotype) | #615528 PARK19A (PARK19B included) | OMIM mirror above |
| OMIM (gene) | *608375 DNAJC6 | [OMIM 608375 mirror](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/608375) |
| MONDO | MONDO:0014231 | as provided |
| MedGen | C3809811 | [NCBI Gene 9829](https://www.ncbi.nlm.nih.gov/gene/9829) |
| GeneReviews | NBK570369 ("DNAJC6 Parkinson Disease") | NCBI Bookshelf |
| LOVD | Disease #03989 (PARK19) | [LOVD](https://databases.lovd.nl/shared/diseases/03989) |
| GenCC | "juvenile onset Parkinson disease 19A", AR, Strong (several submitters) | [genebe.net](https://genebe.net/gene/hg38/DNAJC6) |
| Orphanet, ICD-10/11, MeSH | **Not retrieved.** Most likely falls under the general PD codes (ICD-10 G20). Verify. | — |

**Synonyms:** PARK19; PARK19A; PARK19B; juvenile-onset Parkinson disease 19A; DNAJC6 Parkinson disease; auxilin-associated PD; DNAJC6 juvenile parkinsonism-dystonia (Ng 2020).

**Source of the data:** Everything comes from aggregated published case reports and families, plus database curation. Roughly a few dozen patients have been described. No EHR or registry data were found.

---

## 2. Etiology

**Cause.** The disease is purely genetic: biallelic (homozygous in nearly every report) pathogenic DNAJC6 variants. Almost all known families are consanguineous.
- First described by Edvardson et al. 2012 (PMID 22563501, [PMC3341348](https://pmc.ncbi.nlm.nih.gov/articles/PMC3341348)). They used homozygosity mapping and exome sequencing to find a splice variant in DNAJC6 in two patients with juvenile parkinsonism. Abstract: "The mutation was associated with abnormal transcripts and marked reduced DNAJC6 mRNA level."

**Genetic risk factors**
- **Biallelic loss-of-function variants are causal** (see §4).
- **Heterozygous carriers:** no established increase in risk was found.
- **Common or sporadic PD:** a large 2023 rare-variant burden study (7,184 cases; [aminer record](https://aminer.org/pub/64af6fdc3fda6d7f06419fab/large-scale-rare-variant-burden-testing-in-parkinson-s-disease)) was retrieved, but its snippets do not report DNAJC6 as significant. **Population-level DNAJC6 risk evidence is not available.**
- **Expression in sporadic PD (preclinical and postmortem):** Darsono et al. (JCI Insight, [article 194989](https://jci.org/articles/view/194989/pdf)) report that "DNAJC6 expression is significantly downregulated in postmortem substantia nigra tissues and transcriptomic datasets from patients with late-onset sporadic PD." They attribute the loss to "impaired transcription mediated by the midbrain-specific factors NURR1/FOXA2 and reduced protein stability regulated by LRRK2."

**Environmental risk factors, protective factors, and gene–environment interaction (GxE)**
- No human data.
- The only GxE hint comes from flies: Drosophila with reduced auxilin (aux) are "more sensitive to the toxin paraquat, suggesting that genetic and environmental factors intertwine" (Song et al. 2017, PMID 28147270, [FlyBase FBrf0234656](https://flybase.org/reports/FBrf0234656.html)). Fly aux is closest to GAK and shares only 31% identity with DNAJC6.
- **No protective factors are known.**

---

## 3. Phenotypes

Three phenotypic groups are recognized. Manfield et al. 2024 (PMID 39654465, [PMC11952936](https://pmc.ncbi.nlm.nih.gov/articles/PMC11952936/)) list them as:
1. Slowly progressive, levodopa-responsive parkinsonism (PARK19B).
2. Rapidly progressive parkinsonism with intellectual disability, cognitive decline, upper motor neuron signs, dystonia and epilepsy (classic PARK19A).
3. Dystonia-parkinsonism.

The letter notes "Most reported cases are of juvenile onset."

**Phenotype table.** Frequencies come from the reported families. Exact denominators from the MDSGene meta-analysis were not retrieved.

| Phenotype (suggested HPO label) | Type | Onset | Frequency / evidence |
|---|---|---|---|
| Parkinsonism; Bradykinesia; Rigidity | Sign | 7–13 y (PARK19A); 21–42 y (PARK19B) | Universal: all PARK19A families (OMIM; Ng 2020 Table 1 onset 7–13 y) |
| Resting tremor / Tremor | Sign | Childhood | Present in the Turkish family (onset 10–11 y; Köroğlu 2013, PMID 23211418). Absent in the Yemeni girl (Elsayed 2016, PMID 26703368) |
| Postural instability; Shuffling gait | Sign | Adolescence | Common (OMIM clinical synopsis) |
| Dystonia (incl. retrocollis, oculogyric crisis) | Sign | Childhood–adolescence | Prominent in the Ng 2020 cohort and Manfield 2024 |
| Global developmental delay / Intellectual disability | Neurodevelopmental | Infancy | 6/6 in Ng 2020 ("neurodevelopmental delay in infancy"); also the Turkish family |
| Neurodevelopmental regression / Cognitive decline | Behavioral | Childhood | 6/6 Ng 2020; Elsayed 2016 |
| Seizures (absence, generalized), EEG encephalopathy | Sign | 1–5 y in Turkish family | 3/4 Turkish patients; 2/6 Ng 2020; Elsayed 2016 |
| Pyramidal signs / Spasticity / Hyperreflexia | Sign | Childhood | Turkish family; Elsayed 2016 |
| Visual hallucinations / Psychosis | Behavioral | Adolescence | Elsayed 2016 (presenting symptom); dopaminergic psychiatric side effects in PARK19B (Olgiati 2016) |
| Hypometric saccades | Sign | — | 1 of the Edvardson brothers |
| Dysarthria; Hypomimia; Dysphagia | Sign | — | OMIM synopsis; Manfield 2024 |
| Levodopa-induced dyskinesia | Treatment complication | — | PARK19B (Olgiati); some Ng 2020 patients |
| Cerebral / cerebellar atrophy (MRI) | Imaging | — | Usually normal. Diffuse atrophy in 1 Turkish patient; progressive perisylvian and cerebellar atrophy in 1 Ng patient |
| Reduced striatal DaT uptake | Imaging | — | Absent or reduced in 3/3 scanned (Ng 2020) |
| Decreased CSF homovanillic acid | Lab | — | Isolated low HVA (Ng 2020) |
| Gastroparesis | Sign | — | Manfield 2024 (single case) |

**Severity and progression:** PARK19A is severe and rapidly progressive.
- Edvardson brothers: one was wheelchair-bound at 13; the other could not walk by 18.
- Turkish family: all were wheelchair-bound or bedridden 10–15 years after onset (OMIM).
- PARK19B is mild and slowly progressive.

**Quality of life:** No EQ-5D or SF-36 data exist. The functional burden is loss of ambulation, dependence for daily activities, special education needs, and feeding problems (one patient needed a jejunostomy in Manfield 2024).

---

## 4. Genetic / Molecular Information

**Gene.** DNAJC6, DnaJ heat shock protein family (Hsp40) member C6, auxilin.
- HGNC:15469; NCBI Gene 9829; Ensembl ENSG00000116675; chromosome 1p31.3 ([NCBI Gene](https://www.ncbi.nlm.nih.gov/gene/9829)).
- Expression is brain-biased (brain RPKM 55.4; adrenal 6.4) ([MCE gene page](https://www.medchemexpress.com/gene/9829.html)).

**Protein domains:**
- N-terminal PTEN-like domain (about residues 40–421), which recruits auxilin onto coated vesicles.
- Middle clathrin-binding domain.
- C-terminal J-domain (about residues 886–931) with the HPD motif, which binds Hsc70 and stimulates its ATPase activity.

Domain boundaries come from [Roosen 2019 thesis](https://centaur.reading.ac.uk/88071/1/23862437_Roosen_Thesis_Redacted.pdf) and OMIM 608375.

**Reported pathogenic variants (all germline, homozygous)**

| Variant | Type | Phenotype | Population | Reference |
|---|---|---|---|---|
| c.801-2A>G | Splice acceptor; abnormal transcripts, reduced mRNA | PARK19A | Palestinian | Edvardson 2012, PMID 22563501 |
| p.Gln734* (Q734X) | Nonsense; truncates about 20% of the protein, null | PARK19A + ID + epilepsy | Turkish | Köroğlu 2013, PMID 23211418 |
| c.2365C>T p.Gln789* | Nonsense | PARK19A + seizures + psychosis | Yemeni (treated in Sudan) | Elsayed 2016, PMID 26703368 |
| p.Arg927Gly (R927G) | Missense in J-domain HPD region | PARK19B | European (Dutch or Brazilian family) | Olgiati 2016, PMID 26528954 |
| c.2223A>T | Putative splice | PARK19B | European (Dutch or Brazilian family) | Olgiati 2016, PMID 26528954 |
| c.766C>T p.Arg256* | Nonsense | Juvenile parkinsonism-dystonia | Pakistani (2 families) | Ng 2020, PMID 32472658 |
| c.2416C>T p.Arg806* | Nonsense | Juvenile parkinsonism-dystonia | Palestinian | Ng 2020, PMID 32472658 |
| c.1478C>A p.Ser493* (NM_001256864.1) | Nonsense, predicted NMD; ACMG Pathogenic | Dystonia-parkinsonism | Caucasian | Manfield 2024, PMID 39654465 |

- The OMIM summary (not verified verbatim) says PARK19B accounted for 2 of 92 autosomal recessive PD probands sequenced. It also says Olgiati found "significantly decreased, but detectable" auxilin in patient fibroblasts. Olgiati screened 274 early-onset PD patients in total ([record](https://research.uniupo.it/en/publications/dnajc6-mutations-associated-with-early-onset-parkinsons-disease/)).
- **Mechanism:** loss of function. Auxilin protein was reduced in patient fibroblasts and CSF, and CSF GAK was increased (Ng 2020).
- **Genotype–phenotype correlation:** In their reply letter, Olgiati et al. proposed that "milder mutations cause the EOPD phenotype and more severe loss-of-function mutations cause the juvenile phenotype." This is a hypothesis, but it fits the data: truncating variants give PARK19A, while missense or splice variants give PARK19B.
- **Population allele frequencies (gnomAD) and ClinVar classifications:** not retrieved.
- **Somatic variants:** not applicable.
- **Modifier genes:**
  - **GAK** (the paralog cyclin G-associated kinase) partly compensates for auxilin loss. It is up-regulated up to 3-fold in auxilin-knockout mouse brain (Yim et al. 2010, PNAS 107:4412, [PMC2840126](https://omicsdi.org/dataset/biostudies-literature/S-EPMC2840126)) and is increased in patient CSF.
  - **SYNJ1** overexpression rescues defects in a fly model (Jacquemyn 2023).
  - None of these has been proven to modify disease in humans.
- **Epigenetics:** No disease-specific data. CRISPRa-mediated *epigenetic* up-regulation of DNAJC6 was protective in mice (Darsono).
- **Chromosomal and structural variants:** Köroğlu 2013 cites an earlier 80-kb deletion that includes DNAJC6 in a boy with epilepsy but no parkinsonism.

---

## 5. Environmental Information

No environmental, lifestyle or infectious causes are known. This is a Mendelian disorder. The only environmental link is the fly paraquat-sensitivity result in §2, which is relevant only by analogy.

---

## 6. Mechanism / Pathophysiology

### Causal chain

1. Biallelic DNAJC6 nonsense, splice or J-domain missense variants **lead to** absent or reduced auxilin protein. Nonsense-mediated decay is predicted for truncating variants, and the fall in protein is demonstrated in fibroblasts and CSF (PMIDs 22563501, 26528954, 32472658).
2. Loss of auxilin **results in** failure to recruit Hsc70 to clathrin-coated vesicles, which impairs clathrin uncoating. This is demonstrated in knockout mouse synapses, which accumulate clathrin-coated vesicles and empty cages (Yim 2010). Partial GAK compensation may explain why the effect is cell-type selective; this is inferred.
3. Impaired uncoating **leads to** defective clathrin-mediated synaptic vesicle endocytosis and recycling, because coat components stay trapped in assembled coats (Yim 2010; Vidyadhara 2023, PMID 36920906).
4. **Branch A, dopamine handling in the presynaptic terminal.** Poor endocytosis and SV protein sorting **result in**:
   - Dopamine transporter (DAT) being misrouted into axonal membrane deformities.
   - Slower dopamine reuptake.
   - Elevated presynaptic macroautophagy.
   - Inefficient packaging of dopamine into vesicles.

   These **lead to** dopamine dyshomeostasis: striatal dopamine down 14.5% at 3 months and 52% at 9 months, and DOPAC up. This is shown in mice (Vidyadhara 2023). In patients, low CSF HVA and reduced presynaptic dopaminergic proteins point the same way (Ng 2020). In LRRK2 neurons, the same auxilin-dependent endocytic defect causes oxidized dopamine to accumulate, glucocerebrosidase activity to fall and α-synuclein to rise (Nguyen & Krainc 2018, PNAS, DOI 10.1073/pnas.1717590115). That this happens in DNAJC6 patients is inferred.
5. **Branch B, membrane lipids.** J-domain mutations **result in** reduced phosphoinositides and other polyunsaturated membrane lipids. These defects are rescued by Synaptojanin-1, the product of another parkinsonism gene (fly knock-in carrying the human R927G change; Jacquemyn 2023, PMID 36739293).
6. **Branch C, neurodevelopment.** Defective endocytosis **impairs** WNT–LMX1A signaling during midbrain dopaminergic neuron development. This **produces** intrinsically vulnerable dopaminergic neurons and neurodevelopmental defects (CRISPR-edited human embryonic stem cell midbrain organoids; Wulansari 2021, Sci Adv 7:eabb1540, PMID 33597231 as shown in a [BVS record](https://busqueda.bvsalud.org/portal/resource/es/mdl-33597231)). This branch plausibly explains the infantile developmental delay and intellectual disability in PARK19A; that link is inferred.
7. Branches A–C together **lead to** α-synuclein pathology (pSer129), mitochondrial and lysosomal dysfunction, and neuroinflammation (gliosis at 9 months). **The result is** selective loss of substantia nigra dopaminergic neurons, about 40% by 9 months in knockout mice, with the VTA relatively spared (Vidyadhara 2023; Wulansari 2021). Astrocytic DNAJC6 loss adds proinflammatory and phagocytic defects (Darsono, JCI Insight).
8. Nigrostriatal denervation (absent or reduced DaT uptake in patients) **results in** parkinsonism and dystonia. Wider synaptic dysfunction in cortical and hippocampal neurons **is thought to cause** epilepsy, intellectual disability and cognitive decline; this is inferred.

**Upstream vs downstream:** Uncoating and endocytosis failure (steps 2–3) is upstream. Dopamine and lipid dyshomeostasis (steps 4–5) sit in the middle. α-synuclein aggregation, inflammation and neuron death (step 7) are downstream.

**Suggested GO biological-process labels:** clathrin coat disassembly; clathrin-dependent endocytosis; synaptic vesicle endocytosis; synaptic vesicle recycling; dopamine uptake; regulation of dopamine metabolic process; phosphatidylinositol metabolic process; macroautophagy; Wnt signaling pathway; midbrain dopaminergic neuron differentiation.

**Suggested GO molecular-function labels:** Hsp70 protein binding; clathrin binding; ATPase activator activity.

**Suggested CL labels:** dopaminergic neuron (substantia nigra pars compacta); astrocyte; microglial cell.

**Molecular profiling:**
- Proteomics: 22 proteins changed in 3-month knockout mouse brain, including lower ALDH7A1 and lower synaptosomal COMT (Vidyadhara 2023).
- Transcriptomics: DNAJC6 is reduced in sporadic PD substantia nigra datasets (Darsono).
- No single-cell, spatial or CRISPR-screen data specific to this disease were found.

---

## 7. Anatomical Structures Affected

- **Organ:** brain (nervous system). Secondary involvement of the gut has been reported (gastroparesis; Manfield 2024).
- **Primary sites (suggested UBERON labels):** substantia nigra pars compacta; striatum (dorsal striatum); nigrostriatal tract. Cerebral cortex and cerebellum show atrophy in a few patients.
- **Cells:** midbrain dopaminergic neurons and astrocytes.
- **Subcellular (suggested GO cellular-component labels):** clathrin-coated vesicle; presynapse/synaptic vesicle; axon terminal membrane; autophagosome; lysosome; mitochondrion; cytosol.
- **Lateralization:** Bilateral and generalized. No data on asymmetry were found.

---

## 8. Temporal Development

- **Onset:**
  - PARK19A: motor onset at 7–13 years. Developmental delay can be evident in infancy (Ng 2020), and seizures can start at 1–5 years.
  - PARK19B: onset at 21–42 years (Olgiati 2016).
  - Onset is insidious.
- **Progression:**
  - PARK19A is rapidly progressive. Ambulation is lost in mid-adolescence, and patients are wheelchair-bound or bedridden 10–15 years after onset.
  - PARK19B progresses slowly.
  - The course is chronic and lifelong. No remission occurs; levodopa gives only partial or symptomatic benefit.
- **Critical periods:** Organoid data suggest that a developmental window (WNT–LMX1A-dependent dopaminergic neuron specification) is affected before symptoms appear. This is inferred from in vitro work.

---

## 9. Inheritance and Population

- **Inheritance:** autosomal recessive (OMIM; LOVD; GenCC).
- **Penetrance:** appears complete in homozygotes in the reported families. There are not enough data for a formal estimate.
- **Expressivity:** highly variable, ranging from infantile developmental delay with epilepsy to adult PD resembling typical PD.
- **Consanguinity:** present in most families (Palestinian, Turkish, Yemeni, Pakistani).
- **Founder effects:** p.Arg256* was found in two Pakistani families from the same region (Ng 2020). This suggests a founder allele, which is inferred.
- **Anticipation and germline mosaicism:** not reported.
- **Carrier frequency:** not retrieved.
- **Prevalence:** "Rare" (GeneReviews table). No numeric prevalence or incidence exists.
- **Geography:** Mostly Middle Eastern and South Asian families, plus families of European origin ([MDPI Genes review](https://mdpi.com/2073-4425/13/3/471)).
- **Sex ratio:** no bias is evident in this small number of cases.
- **MDSGene review:** pooled DNAJC6 with five other atypical-parkinsonism genes (140 patients from 73 families). Across that group, median onset was 24 years and levodopa response was 49%, compared with 93% in typical monogenic PD (Wittke et al. 2021, Mov Disord, DOI 10.1002/mds.28517, [PMC9070562](https://pmc.ncbi.nlm.nih.gov/articles/PMC9070562)). DNAJC6-specific numbers were not retrieved.

---

## 10. Diagnostics

- **Genetic testing (confirms the diagnosis):** identify biallelic pathogenic DNAJC6 variants. GeneReviews recommends a multigene PD or dystonia panel, or exome/genome sequencing, rather than testing DNAJC6 alone.
  - Variants have been found by WES (Edvardson; Köroğlu), a targeted PD panel (Elsayed) and WGS (Manfield).
  - Olgiati: "Screening of DNAJC6 is warranted in all patients with early-onset PD compatible with autosomal recessive inheritance."
- **Imaging:**
  - DaT-SPECT: absent or reduced basal ganglia uptake (3/3 tested in Ng 2020).
  - PET: nigrostriatal abnormalities in one PARK19B family.
  - MRI: usually normal, sometimes atrophy.
- **CSF neurotransmitters:** isolated low HVA with normal 5-HIAA, a pattern resembling TH deficiency. Ng et al. state that DNAJC6 disease "should be considered as a differential diagnosis for pediatric neurotransmitter disorders associated with low homovanillic acid levels."
- **Research biomarkers:** auxilin is reduced in fibroblasts and CSF, and GAK is raised in CSF.
- **EEG:** diffuse encephalopathy with focal epileptiform activity (Elsayed).
- **Differential diagnosis:**
  - Other recessive juvenile/early-onset PD: PRKN, PINK1, DJ-1, ATP13A2, FBXO7, SYNJ1, VPS13C, PLA2G6.
  - Pediatric neurotransmitter disorders: TH deficiency, AADC deficiency, dopamine transporter deficiency syndrome (SLC6A3).
  - Dopa-responsive dystonia (GCH1).
  - Wilson disease and NBIA.
  - Distinguishing features of DNAJC6: developmental delay with epilepsy, poor or unsustained levodopa response, and isolated low CSF HVA.
- **Omics diagnostics, CMA and karyotype:** no defined role, apart from CMA's potential to detect rare deletions.
- **Screening:** No newborn screening exists. Cascade carrier testing is possible in families.

---

## 11. Outcome / Prognosis

- **Survival:** Life-expectancy and mortality data are not available. No deaths are reported in Ng 2020 (patients aged 10–28 at report).
- **Morbidity:** Severe disability in PARK19A, with loss of walking in adolescence, bedridden state, intellectual disability, epilepsy and dysphagia.
- **Prognostic factors:** Truncating genotypes, juvenile onset and developmental delay predict a severe, pharmacoresistant course. Adult onset and missense or splice variants predict a slower course with good levodopa response. This is an observational correlation.
- **Complications:** levodopa-induced dyskinesia, psychosis or hallucinations, dystonic storms, and feeding difficulties.

---

## 12. Treatment

All treatment is symptomatic. **No disease-modifying therapy or registered clinical trial was found.**

| Intervention (suggested NCIT label) | Evidence | Outcome |
|---|---|---|
| Levodopa/carbidopa | Case series | PARK19B: good response, though limited by dyskinesias and psychiatric side effects (Olgiati). PARK19A: absent, unsustained or mild response (Edvardson; Ng; Elsayed). Turkish family: good response limited by side effects. |
| Dopamine agonists (pramipexole, ropinirole, rotigotine) | Ng 2020; Manfield 2024 | Partial |
| Anticholinergic (trihexyphenidyl); benzodiazepines | Ng 2020; Manfield 2024 | Little benefit |
| Antiseizure drugs (lamotrigine, zonisamide) | Ng 2020 | For epilepsy |
| Subthalamic DBS | 1 Brazilian PARK19B patient (Olgiati, per OMIM) | Marked improvement |
| Pallidal (GPi) DBS | Manfield 2024, PMID 39654465 | At 6 months: UPDRS-III 87→55, oculogyric crises virtually resolved, levodopa withdrawn. A 2026 case also reports sustained tremor reduction ([TOHM](https://reference-global.com/article/10.5334/tohm.1187)). |
| Pallidotomy | 1 adult (cited in Manfield) | — |
| Physical, occupational and speech therapy; special education | GeneReviews | Supportive |

**Experimental and preclinical approaches:**
- CRISPRa-AAV9 up-regulation of DNAJC6 reduced deficits in an α-synuclein mouse model (Darsono, JCI Insight).
- Restoring auxilin rescued phenotypes in LRRK2 neurons (Nguyen & Krainc 2018).
- SYNJ1 overexpression rescued the fly model (PMID 36739293).
- L-DOPA fully restored balance-beam performance in knockout mice (Vidyadhara 2023).

**Pharmacogenomics:** none.

---

## 13. Prevention

- **Primary prevention:** not possible beyond reproductive options.
- **Genetic counseling:** autosomal recessive, so each sibling of a proband has a 25% risk. Carrier testing of relatives is possible, and prenatal or preimplantation testing is possible once the familial variants are known (GeneReviews, snippet level). Counseling is especially relevant in consanguineous families.
- **Tertiary prevention:** seizure control, careful levodopa dosing to limit dyskinesia and psychosis, swallowing and nutrition monitoring, and rehabilitation.
- Vaccines, prophylaxis and public-health measures do not apply.

---

## 14. Other Species / Natural Disease

- **Natural disease in animals:** none found (OMIA was not searched successfully).
- **Orthologs:** mouse *Dnajc6*; Drosophila *aux*. Fly aux is closer to GAK, with 31% identity and 44% similarity to DNAJC6 ([FlyBase](https://flybase.org/reports/FBrf0234656.html)).
- **Conservation:** the auxilin/GAK–Hsc70 clathrin-uncoating mechanism is conserved across species. NCBI Taxon and ortholog Gene IDs were not retrieved.
- **Zoonotic potential:** not applicable.

---

## 15. Model Organisms

| Model | Key phenotypes | How well it matches the human disease | Reference |
|---|---|---|---|
| **Dnajc6 knockout mouse** (Yim 2010) | High early postnatal mortality, low body weight, clathrin-coated vesicle accumulation at synapses, impaired SV endocytosis; GAK up-regulated 3-fold | Synaptic mechanism | PNAS 107:4412, [PMC2840126](https://omicsdi.org/dataset/biostudies-literature/S-EPMC2840126) |
| **Congenic B6-Dnajc6^tm1Legr KO mouse** (3–15 months) | Normal at 3 months. From 9 months: progressive motor deficits, about 40% SNpc TH+ neuron loss, pSer129 α-synuclein, gliosis, L-DOPA-responsive motor deficit, DAT misrouting, slowed DA reuptake | Good. The authors describe it as a model for PARK19. Limit: a full null, whereas patients carry point variants. No seizures or ID were reported. | Vidyadhara 2023, PMID 36920906 |
| **R857G auxilin knock-in mouse** (J-domain) | Clathrin trafficking defects at the synapse and TGN; nigrostriatal lesions | Partial (thesis data) | Roosen 2019 thesis |
| **Drosophila aux RNAi** in dopaminergic neurons | Progressive climbing decline, shorter lifespan, dopaminergic neuron loss, increased α-synuclein toxicity, paraquat sensitivity | Partial; aux is a GAK-like ortholog | Song 2017, PMID 28147270 |
| **Drosophila aux R1119G knock-in** (= human R927G) | Weak hypomorph; synaptic, behavioral and neurodegenerative defects; loss of polyunsaturated phosphoinositide lipids; rescued by Synj1 | Models PARK19B | Jacquemyn 2023, PMID 36739293 |
| **Human ESC (CRISPR) midbrain organoids** | Midbrain dopaminergic neuron loss, α-synuclein aggregation, higher intrinsic firing, mitochondrial and lysosomal dysfunction, WNT–LMX1A neurodevelopmental defect | High for human cell biology and neurodevelopment | Wulansari 2021, Sci Adv, PMID 33597231 |
| **Patient fibroblasts / CSF** | Reduced auxilin; increased GAK | Biomarker validation | Ng 2020; Olgiati 2016 |

**Model resources:** MGI (Dnajc6^tm1Legr) and FlyBase. Repository stock IDs were not retrieved.

---

## Key sources
- Edvardson 2012, PLoS One, PMID 22563501: https://pmc.ncbi.nlm.nih.gov/articles/PMC3341348
- Köroğlu 2013, Parkinsonism Relat Disord 19:320, PMID 23211418
- Olgiati 2016, Ann Neurol 79:244, PMID 26528954, DOI 10.1002/ana.24553
- Elsayed 2016, Ann Neurol 79:335, PMID 26703368, DOI 10.1002/ana.24591
- Ng 2020, Mov Disord 35:1357, PMID 32472658: https://pmc.ncbi.nlm.nih.gov/articles/PMC8425408/
- Manfield 2024, Mov Disord Clin Pract 12:392, PMID 39654465: https://pmc.ncbi.nlm.nih.gov/articles/PMC11952936/
- Vidyadhara 2023, Cell Rep 42:112231, PMID 36920906: https://pmc.ncbi.nlm.nih.gov/articles/PMC10127800/
- Wulansari 2021, Sci Adv 7:eabb1540, PMID 33597231
- Jacquemyn 2023, npj Parkinsons Dis, PMID 36739293: https://pmc.ncbi.nlm.nih.gov/articles/PMC9899244/
- Song 2017, Cell Rep, PMID 28147270
- Yim 2010, PNAS 107:4412: PMC2840126
- Nguyen & Krainc 2018, PNAS 115:5576, DOI 10.1073/pnas.1717590115
- Wittke 2021 (MDSGene), Mov Disord, DOI 10.1002/mds.28517: https://pmc.ncbi.nlm.nih.gov/articles/PMC9070562
- Darsono et al., JCI Insight: https://jci.org/articles/view/194989
- OMIM 615528 / 608375 (mirror); GeneReviews NBK570369; NCBI Gene 9829; LOVD #03989

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 22 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 22 |
| On topic | 12 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 2 |
| Resolved | 1 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014231` (2 mentions) - the report calls it "MONDO"; MONDO calls it **juvenile onset Parkinson disease 19A**