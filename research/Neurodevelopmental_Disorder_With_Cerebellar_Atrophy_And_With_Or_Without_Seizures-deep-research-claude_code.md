---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-24T16:18:10.073306'
end_time: '2026-11-24T16:23:53.116328'
duration_seconds: 343.04
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Neurodevelopmental Disorder With Cerebellar Atrophy And With Or Without
    Seizures
  mondo_id: MONDO:0020841
  category: Mendelian
  causal_genes: BRAT1
  omim_id: OMIM:618056
  synonyms: NEDCAS
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
  web_search_requests: 15
  num_turns: 24
  total_cost_usd: 1.0460327750000002
  session_id: 80b4d5d3-bbac-42e8-ba9d-c4877fc1e15b
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  tool_calls: 44
  retrieval_calls: 42
  assistant_text_blocks: 2
citation_count: 2
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 2
  relevance_assessed: 14
  on_topic: 8
  validator_version: 0.8.0
term_validation:
  total_terms: 46
  verified: 44
  not_found: 1
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.022
  labels_checked: 11
  labels_matching: 7
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0020841
    reported_labels:
    - MONDO
    ontology_label: neurodevelopmental disorder with cerebellar atrophy and with or
      without seizures
  labels_variant: 3
  unresolved_terms:
  - HP:0002541
  unresolvable_prefixes:
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neurodevelopmental Disorder With Cerebellar Atrophy And With Or Without Seizures
- **MONDO ID:** MONDO:0020841 (if available)
- **Causal gene(s):** BRAT1
- **OMIM:** OMIM:618056
- **Synonyms:** NEDCAS
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Neurodevelopmental Disorder With Cerebellar Atrophy And With Or Without Seizures** covering all of the
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

Still gathering sources; PMC blocked automated access, so I'm pulling abstracts from Europe PMC and PubMed instead.

Writing the report now, from the abstracts and secondary sources I could reach.

# BRAT1-related Neurodevelopmental Disorder with Cerebellar Atrophy and With or Without Seizures (NEDCAS): Research Report

**How this was researched.** The direct sources were mostly blocked. PubMed Central, PubMed, Nature, OMIM and HAL returned CAPTCHA, cookie, login or 403 pages. Most evidence below therefore comes from search-engine snippets of abstracts, the MedGen record, and the Frontiers full text of Qi et al. (2022). The quotes are as returned by those tools. Re-check them against the PubMed abstracts before loading them into a knowledge base. Wherever a fact could not be retrieved, the report says so rather than filling it from memory.

---

## 1. Disease Information

**Overview.** NEDCAS is caused by **biallelic pathogenic variants in *BRAT1*** (BRCA1-associated ATM activator 1; 7p22.3; NCBI Gene 221927). MedGen/OMIM defines it as:

> "an autosomal recessive disorder characterized by intellectual disability associated with ataxia (summary by Engel et al., 2023)" — MedGen 1648373 (https://www.ncbi.nlm.nih.gov/medgen/1648373)

It is the milder, non-lethal end of the BRAT1 disease spectrum. The severe end is **RMFSL** (lethal neonatal rigidity and multifocal seizure syndrome, OMIM #614498; PMID 27282546). Engel et al. (2023) state:

> "BRAT1 biallelic variants are associated with rigidity and multifocal seizure syndrome, lethal neonatal (RMFSL), and neurodevelopmental disorder associating cerebellar atrophy with or without seizures syndrome (NEDCAS)" (PMID 37344571)

The literature also describes a related milder presentation, **nonprogressive cerebellar ataxia (NPCA)** (PMID 31742228; Qi 2022, PMC8960271).

**Identifiers**

| Resource | ID | Status |
|---|---|---|
| OMIM (phenotype) | 618056 | confirmed (MedGen) |
| MONDO | MONDO:0020841 | confirmed (MedGen) |
| UMLS CUI | C4748032 | confirmed (MedGen) |
| MedGen | 1648373 | confirmed |
| OMIM (gene) | 614506 | unverified (from a summarized part of MedGen) |
| Orphanet | — | not listed on the MedGen page; not retrieved |
| ICD-10 / ICD-11 / MeSH | — | no disease-specific code retrieved; likely mapped only to generic ataxia/ID codes (unverified) |

**Synonyms.** NEDCAS. Also used in the literature: "BRAT1-related NEDCAS" and "BRAT1-related nonprogressive cerebellar ataxia/NPCA" (a subset).

**Evidence base.** Aggregated case reports and case series. The largest is a multicentre cohort of 97 patients (PMID 37344571). There are no EHR or registry data.

---

## 2. Etiology

- **Causal factor.** Germline, biallelic (homozygous or compound heterozygous) *BRAT1* variants. Disease is caused by loss or reduction of BRAT1 function, which impairs the Integrator complex (see section 6).
- **Genetic risk factors and genotype–phenotype correlation.** Engel et al. (2023), PMID 37344571:
  > "biallelic nonsense, frameshift or inframe deletion/insertion variants result in the severe BRAT1-related RMFSL phenotype (46/46; 100%). In contrast, genotypes with at least one missense were more likely associated with NEDCAS (28/34; 82%)."

  A systematic review (Acta Neurol Belg 2024; PMID 38607605) reported that "homozygous mutations in BRAT1 presented a more severe phenotype than those who are compound heterozygotes."
- **Modifiers.** Siblings with the same *BRAT1* genotype can have discordant phenotypes ("two families differ in clinical presentation despite a common genotype at the BRAT1 locus"; Nuovo 2022, PMID 34747546). This implies unidentified modifiers. No modifier gene has been identified.
- **Environmental risk or protective factors and gene–environment interactions.** None are reported. This is not applicable to a monogenic recessive disorder.
- **Protective genetic factors.** None reported. Residual BRAT1 protein (missense or leaky splice alleles) is associated with milder disease. One mild patient had about 15–20% of control BRAT1 protein (Meossi 2026, PMID 42930560).

---

## 3. Phenotypes

**Cohort figures.**
- OMIM, as relayed in search results, reports that Engel et al. described **38 NEDCAS patients from 29 families**.
- In that group, "Seventy-six percent ... were able to walk and 68% were able to say at least a few words" (PMID 37344571).
- Across the whole 97-patient cohort, figures cited from Engel include cerebellar ataxia 82%, axial hypotonia 79% and cerebellar atrophy 100%. These attributions are unverified, and the group they refer to is unclear.
- Qi et al. (2022, Discussion) state: "Epilepsy occurs in 41.6% of NEDCAS/NPCA patients, mostly before 3 years of age."
- A figure of 6 patients with epilepsy (about 16%) attributed to OMIM is unverified and conflicts with the 41.6% above.

| Phenotype | HPO | Frequency / notes | Source |
|---|---|---|---|
| Intellectual disability (mild to severe) | HP:0001249 | Defining feature; nearly universal | MedGen; 37344571 |
| Global developmental delay | HP:0001263 | Common; onset in infancy | MedGen; Qi 2022 |
| Cerebellar atrophy | HP:0001272 | Defining feature on MRI; usually stable (9→16 y in PMID 31742228; 4→9 y in Qi 2022) | 31742228 |
| Gait ataxia / cerebellar ataxia | HP:0002066 / HP:0001251 | Common; NPCA is nonprogressive | 31742228 |
| Delayed walking | HP:0031936 | 76% eventually walk | 37344571 |
| Delayed speech / absent speech | HP:0000750 / HP:0001344 | 68% say at least a few words; dysarthria | 37344571; Qi 2022 |
| Seizures (incl. focal impaired-awareness) | HP:0001250 / HP:0002384 | About 42% ("with or without seizures"); mostly onset before 3 y | Qi 2022 |
| Axial hypotonia | HP:0008936 | Frequent (see caveat above) | MedGen |
| Limb hypertonia / rigidity | HP:0002509 | Mild; "later-onset spasticity is extremely rare" | Qi 2022 |
| Nystagmus (horizontal jerk, pendular) | HP:0000666 / HP:0000641 | Reported | MedGen; Qi 2022 |
| Dysmetria, truncal titubation, tremor | HP:0001310 / HP:0002541 / HP:0001337 | Reported | MedGen |
| Secondary microcephaly | HP:0005484 | Reported in a subset (frequent in RMFSL: 91%) | MedGen; 37344571 |
| Hypoplasia of the corpus callosum | HP:0002079 | Reported | MedGen |
| Feeding difficulties | HP:0011968 | Reported | MedGen |
| Exaggerated startle, apnea | HP:0002267 / HP:0002104 | Reported; overlaps RMFSL | MedGen |
| Hyperreflexia, agitation | HP:0001347 / HP:0000713 | Reported | MedGen |
| Visual impairment | HP:0000505 | Reported | MedGen |
| Mild dysmorphism (high palate, epicanthus, long philtrum, thin vermilion, broad face, 5th-finger clinodactyly) | HP:0000218, HP:0000286, HP:0000343, HP:0000233, HP:0000283, HP:0004209 | Occasional | MedGen |

- **Onset, severity and progression.** Onset is in infancy, with developmental delay. Severity is variable. The course is generally static or nonprogressive, although some cases in Qi 2022 Table 1 show progressive atrophy.
- **Adult outcome.** One patient reported in 2026 had relatively preserved autonomy in late adolescence (SARA 8.5/40; FARS-ADL 11/36; PMID 42930560).
- **Quality of life.** No formal studies such as EQ-5D or SF-36 were retrieved.

---

## 4. Genetic / Molecular Information

- **Gene.** *BRAT1* (HGNC symbol BRAT1; NCBI Gene 221927; 7p22.3). The HGNC ID was not retrieved.
- **Variant spectrum.** Missense, frameshift, splice and synonymous-splice variants, usually with at least one hypomorphic allele.

| Variant | Type | Context | Source |
|---|---|---|---|
| c.638dup / c.638_639insA, p.(Val214Glyfs*189) | Frameshift | Most frequent (16 cases in a review); seen in both RMFSL and NEDCAS when paired with a hypomorphic allele | 38607605; 34747546; Qi 2022 Table 1 |
| c.1395G>A | Splice (exon 10 skipping) | NEDCAS; 5 cases | 34747546; 38607605 |
| c.294dup(A) | Frameshift | 4 cases; also paired with p.(Glu595Val) in a mild patient | 38607605; 42930560 |
| c.185T>A, p.(Val62Glu) | Missense, homozygous | NPCA in two brothers | 31742228 |
| c.1014A>C, p.(Pro338=) in trans with c.706delC, p.(Leu236Cysfs*5) | Synonymous causing intron 7 retention, plus frameshift | NPCA in a 10-year-old Chinese girl | Qi 2022, PMC8960271 |
| c.1784A>T, p.(Glu595Val) | Missense | Mild NEDCAS | 42930560 |
| p.Glu522Lys (E522K) | Missense | Abolishes binding to INTS11/INTS9 (bioRxiv preprint, not peer-reviewed) | Dokaneheifard 2023 preprint |

- **Classification and frequency.** Data on ACMG classification, ClinVar counts and gnomAD allele frequencies were not retrieved.
- **Functional consequence.** Loss of function or hypomorphism. Patient cells from the Val62Glu brothers showed markedly reduced BRAT1 protein with normal ATM activation and normal mitochondrial respiration (PMID 31742228).
- **Origin.** All variants are germline.
- **Epigenetic or chromosomal changes.** None reported.

---

## 5. Environmental Information

Environmental, lifestyle and infectious factors are not applicable; none have been reported.

---

## 6. Mechanism / Pathophysiology

**Causal chain**

1. Biallelic *BRAT1* loss-of-function or hypomorphic variants **lead to** reduced or absent BRAT1 protein (demonstrated in patient cells: PMID 31742228, 42930560).
2. Loss of BRAT1 **results in** destabilization of the Integrator endonuclease module INTS11/INTS9. BRAT1 "tightly interacts with INTS9/INTS11 subunits of the Integrator complex"; INTS11 levels fall in BRAT1-deleted U2OS cells (PMID 36028512).
   - Structural data show BRAT1 acting as a mostly cytoplasmic chaperone that "stabilizes INTS11 in the cytoplasm and is required for Integrator function in the nucleus." Its conserved C-terminus inserts into the INTS11 active site (PMID 39032490; *Drosophila* ortholog CG7044).
3. Reduced Integrator activity **leads to** defective 3′-end processing of UsnRNAs (especially U1), snoRNAs and replication-dependent histone pre-mRNAs, and to altered protein-coding gene expression (PMID 36028512). Unprocessed U1 snRNA accumulates in the nucleus (Valtorta 2026, PMID 42116163; PMID unverified).
4. **Branch (inferred):** defective snRNA biogenesis and transcription termination **are thought to impair** gene expression programmes during neurodevelopment, particularly in cerebellar neurons. A preprint also proposes that BRAT1 recruits INTS11 to neuronal gene promoters. This step has not been shown directly in human neurons.
5. Neuronal dysfunction or loss **results in** cerebellar atrophy (cerebellar hypoplasia/atrophy on MRI), ataxia, intellectual disability and, in some patients, seizures.
6. **Severity gradient (demonstrated):** residual function determines phenotype. Biallelic null alleles give RMFSL; missense or leaky alleles give NEDCAS or NPCA. "the magnitude of U1 snRNA misprocessing closely correlates with clinical severity across the BRAT1 cohort" (Valtorta 2026).

**Historical hypotheses.**
- BRAT1 was first described as a BRCA1 BRCT-domain and ATM binder that regulates ATM.
- BRAT1 knockdown in HeLa cells raised glucose uptake and mitochondrial ROS, and was linked to mTOR destabilization (secondary summaries; the primary PMIDs were not retrieved).
- Patient-cell data argue against ATM or mitochondrial causation: "ATM kinase activation following ionizing radiation was NOT different between patient and control cells, and no differences in PDH phosphorylation or oxygen consumption" were found (PMID 31742228).

**Suggested GO terms**
- snRNA 3′-end processing: GO:0034472
- Integrator complex: GO:0032039
- snRNA processing: GO:0016180
- Histone mRNA metabolic process: GO:0008334
- Cerebellum development: GO:0021549
- Protein stabilization: GO:0050821

**Suggested CL terms**
- Cerebellar Purkinje cell: CL:0000121
- Cerebellar granule cell: CL:0001031
- Neuron: CL:0000540

**Metabolic, immune and omics findings.** None reported, beyond RNA-processing assays and the RNA-seq in Qi 2022 (intron retention).

---

## 7. Anatomical Structures Affected

- **Primary site.** Central nervous system, specifically the cerebellum (UBERON:0002037), including the cerebellar vermis and hemispheres. The corpus callosum (UBERON:0002336) is thin in some patients.
- **Secondary sites.** Cerebral cortex (seizures, microcephaly) and eyes (nystagmus, visual impairment).
- **Subcellular level.** Cytoplasm (GO:0005737; BRAT1 is predominantly cytoplasmic per PMID 39032490) and nucleus (GO:0005634; site of Integrator activity).
- **Laterality.** Findings are bilateral and symmetric.

---

## 8. Temporal Development

- **Onset.** Infancy, with insidious developmental delay. Seizure onset is usually before 3 years (Qi 2022).
- **Course.** Typically static or nonprogressive. Cerebellar atrophy was stable on serial MRI (PMID 31742228; Qi 2022). Patients survive into adolescence and adulthood (PMID 42930560; PMC9126772 describes a DEE patient surviving to adulthood).
- **Stages, remission, critical periods.** None defined.

---

## 9. Inheritance and Population

- **Inheritance.** Autosomal recessive. Parents are heterozygous carriers (PMID 31742228; Qi 2022).
- **Penetrance and expressivity.** Penetrance appears complete for biallelic genotypes. Expressivity is variable even within families (PMID 34747546).
- **Anticipation and mosaicism.** None reported.
- **Epidemiology.** Ultra-rare: about 97 published BRAT1 patients by 2023, 38 of them NEDCAS. Prevalence, incidence and carrier frequency were not retrieved.
- **Consanguinity, founder effects and geography.**
  - The NPCA brothers were children of carrier parents; their ethnicity was not retrieved.
  - c.638dup is the most frequent allele, but no founder study was retrieved.
  - The RMFSL founder in the Amish (Puffenberger 2012) could not be verified.
- **Sex ratio.** No evidence of a sex bias.

---

## 10. Diagnostics

- **Genetic testing.** Exome sequencing is the main diagnostic route (all key reports, e.g. PMID 31742228, 34747546). Genome sequencing or RNA-seq helps with deep-intronic, splice and synonymous variants (Qi 2022 used RNA-seq to confirm intron 7 retention). *BRAT1* is included in ataxia and epilepsy panels; the specific panels were not retrieved. CMA, karyotype, FISH, mtDNA and repeat-expansion testing are not diagnostic but may be used to exclude differentials.
- **Functional biomarker (emerging).** Unprocessed U1 snRNA in patient fibroblasts or lymphoblastoid cells. It scales with severity and has been proposed as a diagnostic marker (Valtorta 2026). BRAT1 protein can be measured by immunoblot (PMID 42930560).
- **Imaging.** MRI shows cerebellar atrophy, sometimes with a thin corpus callosum.
- **EEG.** May be normal (Qi 2022) or show focal or multifocal discharges in patients with epilepsy.
- **Routine workup.** Metabolic and CSF testing is normal (Qi 2022).
- **Differential diagnosis.**
  - RMFSL (same gene, lethal neonatal course)
  - Pontocerebellar hypoplasias
  - Ataxia-telangiectasia (*ATM*; excluded by normal ATM function and lack of telangiectasia)
  - Other congenital ataxias
  - INTS11-related neurodevelopmental disorder (the closest mechanistic overlap)
  - Developmental and epileptic encephalopathies, including EIMFS (PMC9126772)
- **Formal criteria.** No standardized diagnostic criteria exist.
- **Screening.** Prenatal diagnosis by chorionic villus sampling in families with known variants (Qi 2022). Newborn screening is not available.

---

## 11. Outcome / Prognosis

- **Survival.** NEDCAS is non-lethal by definition, in contrast to RMFSL, where 93% "died prematurely" (PMID 37344571). Life expectancy is not quantified.
- **Function.** In NEDCAS, 76% walk and 68% speak at least a few words. The degree of intellectual disability varies from mild (NPCA) to severe.
- **Prognostic factors.** Genotype (at least one missense or hypomorphic allele means a milder course), residual protein level, and U1 snRNA misprocessing burden (Valtorta 2026).
- **Complications.** Epilepsy, feeding difficulties, gait disability.
- **Quality of life.** No formal QoL data were found.

---

## 12. Treatment

- **Disease-modifying therapy.** None. No trials were found (no ClinicalTrials.gov searches returned BRAT1 trials).
- **Supportive care.**
  - Antiseizure medication: no BRAT1-specific drug-response data were retrieved. RMFSL seizures are typically drug-resistant (Qi 2022 Table 1).
  - Physiotherapy, occupational therapy and speech therapy for ataxia and dysarthria.
  - Feeding support.
  - Suggested NCIT terms: Anticonvulsant (C264), Physical Therapy (C15458), Speech Therapy (C15385). These codes were not verified in this session.
- **Experimental and preclinical.** In an *ints11* zebrafish model, neurotrophic modulation restored motor and developmental defects (PMID 41837557). This suggests Integrator-pathway rescue strategies, but there is no BRAT1 human data.
- **Pharmacogenomics, gene therapy, ASOs.** None reported. A splice-switching ASO is theoretically plausible for splice alleles such as c.1395G>A, but this is speculative.

---

## 13. Prevention

- Genetic counselling: 25% recurrence risk for carrier couples.
- Carrier testing of relatives.
- Prenatal diagnosis by CVS (Qi 2022) or preimplantation genetic testing.
- Tertiary prevention: seizure control and rehabilitation.
- No vaccines, lifestyle measures or public-health measures are applicable.

---

## 14. Other Species / Natural Disease

- No naturally occurring animal disease was found; OMIA was not searched successfully.
- **Orthologs:** mouse *Brat1* (MGI:1891679) and *Drosophila* CG7044 (PMID 39032490).
- **Conservation:** the BRAT1–INTS11 interaction is conserved, including the C-terminal cysteine that coordinates INTS11 metal ions.
- No zoonotic relevance.

---

## 15. Model Organisms

| Model | Findings | Source |
|---|---|---|
| Mouse *Brat1*^em1(IMPC)Bay^ (null) | Homozygotes show embryonic growth retardation, abnormal placenta size and "preweaning lethality, incomplete penetrance"; heterozygotes have abnormal embryo size at E18.5 | IMPC (https://mousephenotype.org/data/genes/MGI:1891679) |
| Mouse *Brat1* conditional (MEFs) | Deletion suppressed serum-induced cycling and destabilized mTOR (secondary report) | search summary |
| Human BRAT1-deleted U2OS cells and patient fibroblasts/LCLs | INTS11 loss, UsnRNA and histone 3′-end misprocessing | PMID 36028512; Valtorta 2026 |
| *Drosophila* CG7044 | Cytoplasmic INTS11 chaperone | PMID 39032490 |
| Zebrafish *ints11* knockout (pathway model, not *brat1*) | Microcephaly, neurodevelopmental defects, U snRNA processing defects | Valtorta 2026; PMID 41837557 |

**Limitations.** No published model recapitulates cerebellar atrophy with ataxia specifically for *BRAT1*. The mouse null is closer to the RMFSL/lethal end, and no hypomorphic knock-in has been reported.

---

## Key references

- Engel C et al. *Eur J Hum Genet* 2023;31:1023–31. **PMID 37344571**
- Srivastava S et al. *Am J Med Genet A* 2016;170:2265–73. **PMID 27282546**
- Mahjoub A et al. *Neurol Genet* 2019. **PMID 31742228**
- Nuovo S et al. *Hum Mutat* 2022;43:67–73. **PMID 34747546**
- Qi Y et al. *Front Genet* 2022;13:821587, doi:10.3389/fgene.2022.821587 (PMC8960271; PMID not retrieved)
- Cihlarova Z et al. *Nat Commun* 2022;13:5026. **PMID 36028512**
- Lin MH et al. *Mol Cell* 2024;84:2900. **PMID 39032490**
- Systematic review, *Acta Neurol Belg* 2024. **PMID 38607605**
- Valtorta B et al. *Genome Med* 2026, doi:10.1186/s13073-026-01667-1 (PMID 42116163, unverified)
- Meossi C et al. *Med Sci (Basel)* 2026. **PMID 42930560**
- Pistocchi A et al. *J Neurochem* 2026. **PMID 41837557**
- BRAT1 adult DEE review, PMC9126772
- MedGen 1648373

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 14 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 46 |
| Resolved | 44 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 11 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0020841` (1 mention) - the report calls it "MONDO"; MONDO calls it **neurodevelopmental disorder with cerebellar atrophy and with or without seizures**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0002541` (1 mention) - HP does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001249` (1 mention) - the report calls it "Intellectual disability (mild to severe)"; HP calls it **Intellectual disability**
- `HP:0031936` (1 mention) - the report calls it "Delayed walking"; HP calls it **Delayed ability to walk**, and lists "Delayed walking" among its other names
- `HP:0002509` (1 mention) - the report calls it "Limb hypertonia / rigidity"; HP calls it **Limb hypertonia**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MGI:1891679` - called "Brat1", "Orthologs:** mouse *Brat1"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`.