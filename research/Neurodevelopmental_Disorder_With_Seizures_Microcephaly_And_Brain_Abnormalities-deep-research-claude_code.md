---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-15T13:53:00.036638'
end_time: '2026-10-15T13:56:25.254817'
duration_seconds: 205.22
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Neurodevelopmental Disorder with Seizures, Microcephaly, and Brain
    Abnormalities
  mondo_id: MONDO:0859283
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
  num_turns: 18
  total_cost_usd: 2.0543303
  session_id: f78782e5-8ed8-472b-a248-21df2c138ea2
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  assistant_text_blocks: 2
citation_count: 7
reference_validation:
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 4
  quotes_valid: 4
  relevance_assessed: 13
  on_topic: 5
  validator_version: 0.3.0
term_validation:
  total_terms: 70
  verified: 70
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 8
  labels_matching: 6
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neurodevelopmental Disorder with Seizures, Microcephaly, and Brain Abnormalities
- **MONDO ID:** MONDO:0859283 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Neurodevelopmental Disorder with Seizures, Microcephaly, and Brain Abnormalities** covering all of the
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

I've read the cached references and am now confirming the PMIDs for the model-organism and first-report papers.

I've finished the lookups and am writing up the report.

# Research report: Neurodevelopmental disorder with seizures, microcephaly, and brain abnormalities (NEDSMBA; *PPFIBP1*-related)

**Scope of the evidence.** The human literature on this disorder is small:
- One defining cohort study (Rosenhahn et al. 2022, PMID:35830857), which reports 16 individuals from 12 families plus one fetus.
- One family report (Waqas et al. 2023, PMID:36527195).
- An earlier paper that named *PPFIBP1* as a candidate gene (Shaheen et al. 2019, PMID:30214071).
- A prenatal case series that lists a *PPFIBP1* variant (Wang et al. 2023, PMID:37229200).

A PubMed search on 2026-10-15 found no later case series. Many sections of the template therefore have to say "no data". The direct quotes below come from the cached abstract or full text in `references_cache/`, or from PubMed abstracts I fetched in this session.

---

## 1. Disease information

**Overview.** NEDSMBA is an autosomal recessive neurodevelopmental disorder caused by loss of function of both copies of *PPFIBP1*. It is defined by:
- moderate to profound global developmental delay or intellectual disability;
- early-onset epilepsy, often drug-resistant;
- primary and/or progressive microcephaly;
- brain abnormalities on imaging, chiefly leukoencephalopathy, ventriculomegaly, cortical malformations and periventricular intracranial calcifications.

> "we establish bi-allelic loss-of-function variants in PPFIBP1 as a cause of an autosomal recessive severe neurodevelopmental disorder with early-onset epilepsy, microcephaly, and periventricular calcifications." (PMID:35830857)

**Identifiers**

| Resource | ID |
|---|---|
| MONDO | MONDO:0859283, "neurodevelopmental disorder with seizures, microcephaly, and brain abnormalities". OLS records no synonyms, definition or xrefs. |
| OMIM (phenotype) | #620024 (per PanelApp's cross-references) |
| OMIM (gene) | *603141 *PPFIBP1* |
| MedGen | 1823982 (per PanelApp) |
| Orphanet | No specific ORPHA code found. It is probably covered by a generic "rare genetic intellectual disability / epilepsy" grouping. |
| ICD-10/11, MeSH | No disease-specific code. Nearest are G40.x/F7x, and the MeSH headings *Neurodevelopmental Disorders*, *Microcephaly* and *Epilepsy*. |

**Synonyms:** NEDSMBA; *PPFIBP1*-related neurodevelopmental disorder; *PPFIBP1*-associated NDD; liprin-β1 deficiency.

**Source type:** The data are aggregated from published case series (individual patient tables), not from EHRs.

## 2. Etiology

- **Cause:** Homozygous loss-of-function variants in *PPFIBP1*, which encodes the scaffold protein liprin-β1. 14 of the 16 individuals were born to consanguineous parents, according to the PanelApp curator summary of PMID:35830857.
- **Genetic risk factors:** Parental consanguinity and founder alleles. For example, p.(Tyr885Leufs\*4) occurs in more than one family in the cohort table.
- **Environmental risk, protective factors and gene-environment interaction:** None are known, and none would be expected for a fully penetrant recessive disorder.
- **Phenocopy to exclude:** Congenital TORCH infection, especially CMV, which also causes intracranial calcifications. Infection was actively excluded in several cases:

> "In both affected siblings of family 5 and in individual 6-2, a screening for infections of the TORCH spectrum was performed with negative results and also the fetus was tested negative for CMV." (PMID:35830857)

## 3. Phenotypes

Frequencies are from PMID:35830857: n=16 for clinical features, n=14 for MRI, n=9 for CT.

| Phenotype | Frequency | Suggested HPO |
|---|---|---|
| Global developmental delay / ID, severe to profound | 15/16 | HP:0001263 Global developmental delay; HP:0010864 Intellectual disability, severe |
| Absent speech | 15/16 | HP:0001344 Absent speech |
| Impaired motor development | 15/16 | HP:0001270 Motor delay |
| Epilepsy, onset from day 1 to 4 years | 16/16 | HP:0001250 Seizure |
| Focal seizures | 11/16 | HP:0007359 Focal-onset seizure |
| Generalized-onset seizures | 7/16 | HP:0002197 Generalized-onset seizure |
| Epileptic spasms | 7/16 | HP:0011097 Epileptic spasm |
| Myoclonic seizures | 6/16 | HP:0032794 Myoclonic seizure |
| Tonic seizures | 3/16 | HP:0032792 Tonic seizure |
| Hypsarrhythmia / West syndrome | 4/14 | HP:0002521 Hypsarrhythmia |
| Drug-resistant epilepsy | 13/16 | HP:0010818 Generalized tonic seizure ✗ — use **HP:0033726? (verify)**; otherwise "Drug-resistant epilepsy" — **look this term up, do not bind from memory** |
| Microcephaly (OFC ≤ −2 SD) | 15/16 | HP:0000252 Microcephaly |
| Primary microcephaly | 9/16 | HP:0011451 Primary microcephaly |
| Progressive microcephaly | 11/16 | HP:0000253 Progressive microcephaly |
| Hypertonia | 10/16 | HP:0001276 Hypertonia |
| Spastic tetraplegia | 6/16 | HP:0002510 Spastic tetraplegia |
| Hypotonia | 5/16 | HP:0001252 Hypotonia |
| Dystonia | 3/16 | HP:0001332 Dystonia |
| Nystagmus | 4/16 | HP:0000639 Nystagmus |
| Small for gestational age | 9/16 | HP:0001518 Small for gestational age |
| Failure to thrive / low weight | 8/16 | HP:0001508 Failure to thrive |
| Short stature | 7/16 | HP:0004322 Short stature |
| Feeding difficulties (3 with dysphagia) | 7/16 | HP:0011968 Feeding difficulties |
| Ophthalmologic abnormalities: optic atrophy, coloboma, chorioretinal degeneration, abnormal VEPs | 8/16 | HP:0000648 Optic atrophy, etc. |
| Hearing impairment | 4/16 | HP:0000365 Hearing impairment |
| Cryptorchidism | 3/10 males | HP:0000028 Cryptorchidism |
| Congenital heart defects | 7/16 | HP:0001627 Abnormal heart morphology |
| – Patent ductus arteriosus | 6/16 | HP:0001643 |
| – ASD | 3/16 | HP:0001631 |
| – VSD | 2/16 | HP:0001629 |
| Leukoencephalopathy, mostly periventricular | 11/14 | HP:0002352 Leukoencephalopathy |
| Ventriculomegaly | 10/14 | HP:0002119 Ventriculomegaly |
| Cortical malformation | 7/14 | HP:0002539 Cortical dysplasia |
| – Pachygyria | 3/14 | HP:0001302 |
| – Polymicrogyria | 1/14 | HP:0002126 |
| – Periventricular heterotopia | 1/14 | HP:0007165 |
| Hypoplastic corpus callosum | 7/14 | HP:0002079 |
| Cerebellar vermis hypoplasia | 2/14 | HP:0001320 |
| Intracranial calcifications on CT, all periventricular; basal ganglia in 5/9 | 9/9 | HP:0002514 Cerebral calcification; HP:0002135 Basal ganglia calcification |
| Fetal case: IUGR, intracranial calcifications | 1 fetus | HP:0001511 IUGR |

*Correction to the drug-resistant epilepsy row:* I do not have a verified HPO ID for drug-resistant epilepsy. Look it up with `runoak -i sqlite:obo:hp search "drug-resistant"` before binding anything. The same applies to every CURIE in this table: the project's rule is that a CURIE must be read from a lookup when it is written, not taken from memory or from this report.

Key quotes (PMID:35830857):
- "All individuals were affected by epilepsy: most commonly with focal seizures (11/16)"
- "In the majority, the epilepsy was drug-resistant (13/16)"
- "Head CT scan, performed in eight individuals, revealed bilateral intracranial calcifications (ICCs) in all of them (9/9)."
- "Ventriculomegaly of variable degree (10/14) was a common finding."

The Waqas 2023 family (PMID:36527195) had a milder picture: "phenotypes such as global developmental delay (GDD), intellectual disability (ID), microcephaly and speech delay". That report notes no epilepsy and no calcifications, which suggests the condition varies more clinically than the first cohort showed: "loss-of-function variants cause clinically variable neurodevelopmental phenotypes."

**Quality of life:** No formal measures have been published. The burden is severe: 15/16 had no speech, many could not sit, and most had daily seizures (12/16).

## 4. Genetic and molecular information

- **Gene:** *PPFIBP1*, hgnc:9249 (verify against `cache/hgnc/terms.csv`), on 12p11.22. It encodes liprin-β1, which has coiled-coil N-terminal domains and three C-terminal SAM domains. Reference transcript: NM_003622.4.
- **Variant classes:**
  - Nine homozygous truncating variants (nonsense and frameshift) in 16 individuals. Examples: p.(Arg135\*), p.(Gln434\*), p.(Ala473Lysfs\*20), p.(Gln490\*), p.(Arg877\*), p.(Tyr885Leufs\*4).
  - One homozygous missense variant, p.(Gly726Val), in a fetus. It lies in SAM domain 2.
  - Waqas 2023 added c.466C>T p.(Gln156\*).
- **Predicted consequence:** Nonsense-mediated decay leading to loss of function.

  > "Because all of these variants lead to premature termination codons > 50 nucleotides upstream of the last exon-exon splice junction … they are predicted to undergo nonsense-mediated mRNA decay (NMD)."

  For the missense variant:

  > "The Gly726Val exchange is located in the second SAM domain of PPFIBP1 destabilizing both the second SAM domain and the interaction between the second and third SAM domain."

- **Population data:** LoF variants are rare in gnomAD. The paper reports a low observed/expected LoF ratio. The exact o/e value is truncated in the cache, so check it in gnomAD. All alleles were absent or ultra-rare in the homozygous state.
- **Variant origin:** Germline, biallelic. Variants were deposited in ClinVar.
- **Gene–disease validity:**
  - Genomics England PanelApp rates the gene **green** (biallelic) for severe microcephaly and related panels.
  - I did not find a ClinGen GCEP classification. Run `just check-gene-validity` or `just clingen-list` to confirm. Per the repo's own rule, leave `gene_disease_validity` absent unless an external source assigns a tier.
- **Modifier genes, epigenetics:** None reported.
- **Chromosomal abnormalities:** *PPFIBP1* falls inside the 12p11.2 interstitial deletion region (PMIDs 41595523, 37563198). That is a heterozygous contiguous-gene deletion, not this recessive disorder.
- **Somatic context, not relevant to NEDSMBA:** *PPFIBP1* is a recurrent fusion partner in tumours, including *PPFIBP1::ALK* in epithelioid fibrous histiocytoma (PMID:29327718) and *PPFIBP1::ROS1*. This is a likely source of entity confusion during literature screening.

## 5. Environmental information

There are no environmental, lifestyle or infectious causes. Congenital CMV/TORCH infection matters only as a **differential diagnosis**, because it also produces intracranial calcifications and microcephaly.

## 6. Mechanism and pathophysiology

**Causal chain** (inferred steps are marked):

1. **Biallelic truncating *PPFIBP1* variants** lead to premature stop codons. *Predicted:* NMD and absence of liprin-β1. Patient-cell transcript or protein studies have not been reported.
2. **Loss of liprin-β1** removes a scaffold that binds liprin-α through SAM-domain interactions and forms a ternary complex with liprin-α2 and CASK.
   > "Liprins are highly conserved scaffold proteins that regulate cell adhesion, cell migration, and synapse development" (Wei 2011, PMID:21855798)

   The missense variant p.Gly726Val is *predicted* by structural modelling to disrupt SAM-domain topology and protein–protein binding.
3. **Impaired assembly of the presynaptic active zone and neuromuscular junction** leads to defective synaptic vesicle release. This is *shown in invertebrate models only* (see §15):
   > "These findings provide evidence that a defect arises in the presynaptic, but not postsynaptic, apparatus of C. elegans as a result of hlb-1 LoF." (PMID:35830857)
4. **Abnormal axon targeting and synapse formation during neurodevelopment.** *Shown in Drosophila* (PMID:21084592): "Liprin-β mutant R7 axons grow beyond their target layer."
5. **Branch A, network excitability:** presynaptic dysfunction leads to early-onset, drug-resistant epilepsy and epileptic encephalopathy (spasms, hypsarrhythmia). *Inferred* from worm data plus the clinical pattern.
6. **Branch B, impaired brain growth and cortical development:** this leads to primary and progressive microcephaly, cortical malformations (pachygyria, polymicrogyria, heterotopia) and corpus callosum hypoplasia. *Mechanism not established.* A cell-migration or adhesion role is plausible, because liprin-β1 localizes to focal adhesions and promotes migration and invasion in cancer cells (PMID:34480020, PMID:26663347).
7. **Branch C, white matter injury and dystrophic calcification:** periventricular leukoencephalopathy, ventriculomegaly and periventricular/basal ganglia calcification. Fetal histopathology showed "predominant macrocalcification and rare necrotic foci in the process of calcification in the germinative and periventricular areas". The authors suggest a degenerative or necrotic process in germinal-zone tissue. The *upstream link to liprin-β1 is unknown*.
8. **Clinical outcome:** profound GDD/ID, absent speech, spasticity, cortical visual impairment and failure to thrive.
9. **Extra-neural:** congenital heart defects (PDA, ASD, VSD) and short stature. *Mechanism unknown.* Liprin-β1 is highly expressed in lymphatic endothelium and is needed for lymphatic vessel integrity in *Xenopus* (Norrmén 2010, PMID:19965622), so a vascular or endothelial role exists but has not been linked to these features.

Clinical overlap with **CASK**-related microcephaly with pontocerebellar hypoplasia supports a shared presynaptic-scaffold mechanism. The authors note: "it seems possible that PPFIBP1 and CASK are involved in similar biological functions such as protein assembly in the presynaptic active zone."

**Suggested GO and CL terms** (verify each by lookup):

| Category | Terms |
|---|---|
| GO, biological process | presynaptic active zone assembly; synapse assembly (GO:0007416); neuromuscular junction development (GO:0007528); synaptic vesicle exocytosis (GO:0016079); axon guidance (GO:0007411); cell-matrix adhesion (GO:0007160); cerebral cortex development (GO:0021987) |
| GO, cellular component | presynaptic active zone (GO:0048786); focal adhesion (GO:0005925) |
| CL | neuron (CL:0000540); cerebral cortex neuron; radial glial cell (CL:0000681); oligodendrocyte (CL:0000128) for the leukoencephalopathy |

**Omics, single-cell, CRISPR screens:** No disease-specific data exist.

## 7. Anatomical structures affected

- **Primary:** brain (UBERON:0000955), specifically:
  - cerebral cortex (UBERON:0000956)
  - periventricular white matter / cerebral white matter (UBERON:0002437)
  - lateral ventricles (UBERON:0002285)
  - corpus callosum (UBERON:0002336)
  - basal ganglia (UBERON:0010011)
  - cerebellar vermis (UBERON:0004720)
  - germinal matrix and periventricular zone in the fetus
- **Secondary:** heart and ductus arteriosus; eye (optic nerve, retina); inner ear; testis; somatic growth.
- **Subcellular:** presynaptic active zone; focal adhesions and cell periphery, where liprin-β1 co-localizes with liprin-α1.
- **Lateralization:** calcifications are bilateral and symmetric.

## 8. Temporal development

- **Onset:** congenital or neonatal.
  - Microcephaly is often present at birth (9/16 primary).
  - Fetal involvement includes IUGR and calcifications detectable by 22–25 weeks' gestation.
  - Seizure onset ranges from the first week of life to 4 years, mostly in the first months.
- **Course:** Microcephaly is progressive (11/16). Epilepsy is chronic and mostly refractory, with no regression-remission pattern reported. Disability is lifelong.
- **Critical period:** fetal and early-infant brain development.

## 9. Inheritance and population

- **Inheritance:** autosomal recessive (HP:0000007), biallelic and fully penetrant in reported families. Expressivity varies: compare the milder Waqas family with the severe AJHG cohort.
- **Prevalence:** unknown. Fewer than 25 individuals have been published, so `prevalence_class` would be `CASES_IN_LITERATURE` or `NOT_YET_DOCUMENTED`.
- **Populations:** mostly consanguineous families from the Middle East and North Africa. These include Saudi, Egyptian, Iranian and Pakistani families, plus European families from Germany, France, Sweden and Italy, and a Chinese prenatal case (PMID:37229200).
- **Sex ratio:** both sexes affected.
- **Anticipation and mosaicism:** not applicable or not reported.
- **Carrier frequency:** unknown, but low in outbred populations.

## 10. Diagnostics

- **Genetic testing:** Exome or genome sequencing is the diagnostic method. The gene is on PanelApp microcephaly, epilepsy and HSP panels. Trio exome sequencing has identified it prenatally in fetal microcephaly (PMID:37229200: "The gene variant involved included … PPFIBP1"). CMA has low yield for this condition, apart from rare deletion/LoF compound states.
- **Imaging:**
  - Brain MRI: leukoencephalopathy, ventriculomegaly, cortical malformations, thin corpus callosum.
  - **Head CT** (or SWI MRI) to detect periventricular and basal ganglia calcifications.
  - Prenatal ultrasound or postmortem X-ray: microcephaly, IUGR, calcifications.
- **EEG:** focal or multifocal discharges, and hypsarrhythmia in infants with spasms.
- **Laboratory:** no biomarker exists. TORCH/CMV testing is used to exclude infection.
- **Differential diagnosis:**
  - congenital CMV/TORCH infection
  - pseudo-TORCH syndromes and type I interferonopathies (Aicardi–Goutières syndrome, *OCLN*, *USP18*)
  - *CASK* disorder
  - other primary microcephalies (MCPH)
  - developmental and epileptic encephalopathies

  Calcifications together with refractory epilepsy and progressive microcephaly, in a TORCH-negative child of consanguineous parents, should prompt *PPFIBP1* analysis.
- **Screening:** No newborn screening exists. Carrier, cascade and prenatal testing are possible once the familial variants are known.

## 11. Outcome and prognosis

- There are no survival data. The cohort included children and some adolescents, and one pregnancy was terminated (the fetus with p.Gly726Val).
- Morbidity is severe: profound ID, non-ambulant spastic tetraplegia in a subset, cortical visual impairment and feeding problems.
- The 2/16 with drug-responsive epilepsy point to some variability. No prognostic biomarkers are known.

## 12. Treatment

There is no disease-specific therapy. Management is supportive and follows standard care for developmental and epileptic encephalopathy.

| Intervention | Suggested NCIT (verify) |
|---|---|
| Antiseizure medication (multiple ASMs; standard infantile-spasm therapy such as ACTH/prednisolone or vigabatrin where indicated) | NCIT:C15986 Pharmacotherapy + `therapeutic_agent` |
| Physical therapy for spasticity | NCIT:C15302 Physical Therapy |
| Occupational/speech therapy | NCIT:C121351 / NCIT:C159273 |
| Nutritional support / gastrostomy for dysphagia | NCIT:C15433 Nutritional Support (needs case-by-case review) |
| Cardiac surgical or catheter closure of PDA/septal defects | NCIT:C15329 Surgical Procedure |
| Genetic counseling | NCIT:C15240 Genetic Counseling |

- **Treatment-response data:** none beyond the report that 13/16 had drug-resistant epilepsy.
- **Clinical trials:** none found. ClinicalTrials.gov has no *PPFIBP1* trials.
- **Advanced therapeutics:** gene, cell and ASO therapies do not exist for this disorder.

## 13. Prevention

- **Primary:** none.
- **Recurrence prevention:**
  - Genetic counseling (25% recurrence risk for carrier parents).
  - Carrier testing of relatives, especially in consanguineous families.
  - Prenatal diagnosis or PGT.
- **Tertiary:** seizure control, prevention of aspiration, cardiac follow-up, orthopedic care for spasticity.

## 14. Other species and natural disease

- **Naturally occurring animal disease:** none reported. OMIA has no entry.
- **Orthologs:**
  - mouse *Ppfibp1*
  - zebrafish *ppfibp1a/b*
  - *Drosophila* *liprin-β*
  - *C. elegans* *hlb-1*
- **Conservation:** The SAM domains are highly conserved. Murine PPFIBP1 has 97% identity to human across that region (PDB 3TAD).

## 15. Model organisms

| Model | Phenotype | Fidelity / limitations |
|---|---|---|
| ***C. elegans* *hlb-1(syb4896)* knockout** (PMID:35830857) | Increased body curvature; increased head acceleration after light stimulation; reduced pharyngeal pumping; **aldicarb resistance but normal levamisole sensitivity** (a presynaptic defect) | Models the presynaptic mechanism. No brain, so microcephaly, cortex and calcification cannot be modelled. "Loss of hlb-1 did not result in developmental delay or a growth defect in C. elegans". Its relevance to epilepsy is indirect: "indirectly suggests some elements of a mild epileptic phenotype". |
| ***C. elegans* *hlb-1* deletion** (Wang & Wang 2009, PMID:19290026) | Abnormal localization of SNB-1 (synaptobrevin) and UNC-49 puncta; NMJ dysfunction | "Loss of HLB-1 function did not result in defects in neuronal outgrowth or neuronal loss". This paper reported levamisole resistance, which conflicts with the 2022 result. |
| ***Drosophila* *liprin-β* null** (Astigarraga 2010, PMID:21084592) | R7 photoreceptor axons overshoot their target layer; reduced larval NMJ size | Shows a developmental synapse and axon-targeting role. Invertebrate. |
| ***Xenopus* liprin-β1 knockdown** (Norrmén 2010, PMID:19965622) | Defects in lymphatic vessel integrity | Non-neural. Possibly relevant to the cardiovascular or vascular features. |
| **Mouse** | I found no published *Ppfibp1* knockout phenotype (MGI and IMPC were not confirmed in this search). | This is a gap. No mammalian model of microcephaly or calcification exists. Record it as a `HUMAN_MODEL_MISMATCH` or `KNOWLEDGE_GAP` discussion. |

No patient iPSC or organoid models have been reported.

---

## Knowledge gaps worth recording in the entry

1. NMD and protein loss have not been tested in patient cells.
2. The mechanism linking liprin-β1 loss to the intracranial calcifications and leukoencephalopathy is unknown.
3. There is no vertebrate or mammalian model.
4. The basis of the congenital heart defects is unknown.
5. Natural history and survival data are lacking.
6. The difference between the Waqas family's mild phenotype and the severe AJHG cohort (variant position, missense versus truncating) is unexplained.

## Sources
- Rosenhahn E et al. *Am J Hum Genet* 2022;109(8):1421–35. PMID:35830857. [PMC9388382](https://pmc.ncbi.nlm.nih.gov/articles/PMC9388382) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/35830857/)
- Waqas A et al. *Int J Dev Neurosci* 2023. PMID:36527195
- Shaheen R et al. *Genet Med* 2019;21:1209–21. PMID:30214071
- Wang Y et al. *Front Genet* 2023;14:1112153. PMID:37229200
- Astigarraga S et al. *J Neurosci* 2010. PMID:21084592
- Wang DY, Wang Y. *Neurosci Bull* 2009. PMID:19290026 ([Springer](https://link.springer.com/doi/10.1007/s12264-009-0119-9))
- Wei Z et al. *Mol Cell* 2011. PMID:21855798
- Norrmén C et al. *Blood* 2010. PMID:19965622
- Dong C et al. *Cell Death Dis* 2021. PMID:34480020
- [Genomics England PanelApp – PPFIBP1](https://panelapp.genomicsengland.co.uk/panels/162/gene/PPFIBP1/) · [PanelApp Australia](https://panelapp-aus.org/panels/entities/PPFIBP1)
- [medRxiv preprint of Rosenhahn et al.](https://www.medrxiv.org/content/10.1101/2022.04.04.22273309.full.pdf)
- MONDO:0859283 via [EBI OLS](https://www.ebi.ac.uk/ols4/)

**Note for curation.** All ontology CURIEs above are leads to check, not checked bindings. Look each one up with `runoak` or the cache before writing it into the YAML. Fetch PMIDs 30214071, 21084592, 19290026, 21855798 and 19965622 with `just fetch-reference` before quoting them, because only the first three references are cached in this worktree so far.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 4 |
| Quoted claims found in source | 4 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 13 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 70 |
| Resolved | 70 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 8 |
| Terms named correctly | 6 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 2 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0000955` (1 mention) - the report calls it "Primary:** brain"; UBERON calls it **brain**
- `UBERON:0002437` (1 mention) - the report calls it "periventricular white matter / cerebral white matter"; UBERON calls it **cerebral hemisphere white matter**, and lists "cerebral white matter" among its other names

Every term resolved, and every label the report gave matched.