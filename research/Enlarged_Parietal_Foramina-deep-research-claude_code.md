---
provider: claude_code
model: claude-fable-5-1, claude-haiku-5-5
cached: false
start_time: '2026-10-15T11:39:59.178504'
end_time: '2026-10-15T11:55:14.864157'
duration_seconds: 915.69
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Enlarged Parietal Foramina
  mondo_id: MONDO:0018953
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
  - claude-fable-5-1
  - claude-haiku-5-5
  web_search_requests: 5
  num_turns: 166
  total_cost_usd: 9.396986499999999
  session_id: e0f8498f-2348-4e7a-a58e-4bd14c409d83
  stop_reason: end_turn
  permission_denials: 7
  denied_tools:
  - Bash
  assistant_text_blocks: 3
reference_validation:
  total_references: 69
  verified: 69
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 2
  relevance_assessed: 69
  on_topic: 37
  validator_version: 0.3.0
term_validation:
  total_terms: 81
  verified: 75
  not_found: 0
  obsolete: 0
  unverifiable: 6
  confabulation_rate: 0.0
  labels_checked: 6
  labels_matching: 2
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0018953
    reported_labels:
    - MONDO
    - parietal foramina
    ontology_label: parietal foramina
  - term_id: DOID:0060285
    reported_labels:
    - DOID
    ontology_label: parietal foramina
  labels_variant: 2
  unresolvable_prefixes:
  - ORPHA
  - GARD
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Enlarged Parietal Foramina
- **MONDO ID:** MONDO:0018953 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Enlarged Parietal Foramina** covering all of the
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

I'll research Enlarged Parietal Foramina across OMIM, GeneReviews, PubMed, and ontology resources, then write the full report inline.

Direct PubMed pages are blocked by a cookie wall. I'll pull abstracts through NCBI E-utilities instead, and fetch OMIM, Orphanet, and OLS term records in parallel.

Research is complete. I'm now writing the full report from the gathered sources (local reference cache, PubMed E-utilities, OMIM mirror, Orphadata, ClinGen, UniProt, OLS term lookups).

# Enlarged Parietal Foramina (EPF) — Disease Characteristics Research Report

**Target:** Enlarged Parietal Foramina · **MONDO:0018953** (label: *parietal foramina*) · Category: Mendelian (autosomal dominant)
**Report date:** 2026-10-15

**Sourcing note.** Quotations marked **[verbatim]** are copied exactly from a cached abstract or full text read directly in this session (`references_cache/PMID_10742103.md`, `PMID_11137991.md`, `PMID_16319823.md` [full text], `PMID_10742104.md`, `PMID_20301307.md`, `PMID_11106354.md`). All other abstract content was retrieved through NCBI E-utilities or Europe PMC via a summarizing fetch tool and is **paraphrased**; before using it as a KB `snippet`, run `just fetch-reference PMID:<id>` and quote from the cache. Every ontology CURIE below was looked up in EBI OLS4 (or OMIM/ClinGen/UniProt for non-ontology IDs) during this session; none is written from memory. A CURIE's presence here says the term exists with that label; it does not establish dynamic-enum membership (run `just validate-terms`).

---

## 1. Disease Information

### Overview
Enlarged parietal foramina (EPF; also PFM, foramina parietalia permagna, FPP, "Catlin marks", hereditary cranium bifidum) are symmetric, paired, oval radiolucent defects of the parietal bones, located on either side of the posterior sagittal suture near its intersection with the lambdoid sutures. They result from deficient intramembranous ossification around the parietal notch, a fetal gap that is normally obliterated during the fifth month of gestation. GeneReviews states: *"Enlarged parietal foramina are characteristic symmetric, paired radiolucencies of the parietal bones, located close to the intersection of the sagittal and lambdoid sutures, caused by deficient ossification around the parietal notch. Enlarged parietal foramina are usually asymptomatic."* **[verbatim, PMID:20301307]**

The condition is a dosage-sensitive transcription-factor disorder: heterozygous loss-of-function of either **MSX2** (PFM1) or **ALX4** (PFM2) produces a clinically indistinguishable skull phenotype. A third locus (PFM3, 4q21-q23) is mapped but not cloned. EPF also occurs as a mandatory component of **Potocki-Shaffer syndrome** (11p11.2 contiguous-gene deletion including ALX4 and EXT2) and as the allelic condition **parietal foramina with cleidocranial dysplasia** (PFMCCD, MSX2).

### Identifiers

| Resource | Identifier | Notes |
|---|---|---|
| MONDO | MONDO:0018953 | label *parietal foramina*; the umbrella concept. Children/related: MONDO:0008197 *parietal foramina 1*, MONDO:0012309 *parietal foramina 2*, MONDO:0012302 *parietal foramina 3*, MONDO:0008198 *parietal foramina with cleidocranial dysplasia*, MONDO:0011022 *Potocki-Shaffer syndrome* (OLS4 lookup) |
| OMIM | PS168500 (phenotypic series); #168500 PFM1 (MSX2, 5q35.2); #609597 PFM2 (ALX4, 11p11.2); %609566 PFM3 (4q21-q23); #168550 PFMCCD (MSX2) | OMIM mirror text; omim.org returned HTTP 403 |
| Orphanet | ORPHA:60015 *Enlarged parietal foramina*; related ORPHA:251290 *Parietal foramina with clavicular hypoplasia*; ORPHA:52022 *Potocki-Shaffer syndrome* | MONDO xref; Orphadata API |
| ICD-11 | LB70.Y (Structural developmental anomalies of cranium, other specified) — per KEGG H00475; ICD-11 foundation entity 905361904 (MONDO xref) | ICD-10 code not listed in KEGG or MONDO; **not verified** |
| MeSH | C566826 (PFM1); C566825 (KEGG also lists) | |
| DOID | DOID:0060285 | |
| SNOMED CT | 718099006 | |
| UMLS/MedGen | MedGen 505331 (grouping); MedGen C1868599 (PFM1); UMLS CN002451 (GARD) | |
| GARD | GARD:0016662 | |
| KEGG DISEASE | H00475 *Enlarged parietal foramina/cranium bifidum* | |
| HPO (phenotype) | HP:0002697 *Parietal foramina*; HP:0004423 *Cranium bifidum occultum* | |
| GeneReviews | NBK1128, PMID:20301307 (Mavrogiannis LA, Wilkie AOM; chapter "Enlarged Parietal Foramina") | **A GeneReviews chapter exists** — mandatory phenotype baseline |

### Synonyms
From MONDO/GARD: enlarged parietal foramina; symmetric parietal foramina; foramina parietalia permagna (FPP); fenestrae parietales symmetricae; hereditary cranium bifidum; cranium bifidum occultum; Catlin marks (also misspelled "caitlin marks"); giant parietal foramina; "holes in parietal bones". OMIM alternative titles: PFM; Parietal foramina, symmetric; Cranium bifidum, hereditary. Spanish: foramina parietal ampliada.

### Data provenance
All information below is **aggregated disease-level** (OMIM, Orphanet, GeneReviews, published family series, case reports). No EHR-derived or individual-patient cohort datasets were identified.

---

## 2. Etiology

### Causal factors
EPF is a **monogenic, autosomal dominant** disorder of calvarial ossification caused by **haploinsufficiency of a homeodomain transcription factor**:

- **MSX2 (hgnc:7392), 5q35.2 — PFM1.** Wilkie et al. 2000: *"We describe here heterozygous mutations of the homeobox gene MSX2 (located on 5q34-q35) in three unrelated families with PFM. One is a deletion of approximately 206 kb including the entire gene and the others are intragenic mutations of the DNA-binding homeodomain (RK159-160del and R172H) that predict disruption of critical intramolecular and DNA contacts. Mouse Msx2 protein with either of the homeodomain mutations exhibited more than 85% reduction in binding to an optimal Msx2 DNA-binding site."* **[verbatim, PMID:10742103]** Independently, Wuyts et al. 2000 (Hum Mol Genet, PMID:10767351) found MSX2 mutations in 4 of 5 FPP families and concluded (paraphrase) that FPP is caused by haploinsufficiency of MSX2.
- **ALX4 (hgnc:450), 11p11.2 — PFM2.** Mavrogiannis et al. 2001: *"Here we identify ALX4, which encodes a paired-related homeodomain transcription factor, as the PFM disease gene in P11pDS."* **[verbatim, PMID:11137991]** Wuyts et al. 2000 (J Med Genet): *"Mutation analysis of the ALX4 gene in three unrelated FPP families without the MSX2 mutation identified mutations in two families, indicating that mutations in ALX4 could be responsible for these skull defects and suggesting further genetic heterogeneity of FPP."* **[verbatim, PMID:11106354]** Wu et al. 2000 (PMID:11017806) proposed ALX4 as the PFM gene in the 11p11.2 deletion syndrome by FISH (ALX4 deleted in two Potocki-Shaffer patients; expression confined to bone).
- **PFM3 locus, 4q21-q23.** Chen et al. 2003 (PMID:12905082): in a large Chinese AD pedigree with MSX2 and ALX4 excluded, genome-wide linkage gave a maximum two-point LOD of 3.87 at D4S2961 (20 cM interval); no exonic mutations in BMPR1B, PP1, IBSP (paraphrase). Gene still unidentified.
- **Contiguous-gene deletion:** 11p11.2 (Potocki-Shaffer syndrome; ALX4 + EXT2 ± PHF21A) and distal 5q deletion including MSX2 (Aftimos 2010, PMID:19952731, no abstract).

Relative contribution: *"Overall, we identified ALX4 or MSX2 mutations (six each) in 11/13 familial but only 1/6 sporadic PFM cases, suggesting that the two genes contribute approximately equally to the mutation spectrum."* **[verbatim, PMID:16319823]**

### Risk factors
- **Genetic:** having an affected parent (most cases inherited; de novo fraction appears small — GeneReviews **[verbatim]**: *"Most individuals diagnosed with enlarged parietal foramina have an affected parent. The proportion of individuals with enlarged parietal foramina caused by a de novo pathogenic variant appears to be small."*).
- **Modifiers:** Mavrogiannis 2006 typed the reciprocal gene in non-penetrant carriers and found no explanatory coding variants; variability "compatible with the influence of genetic modifiers" (see §9). Mouse data show **Msx1** and **Twist1** dosage modify the Msx2 foramen (PMID:10742104, PMID:14597577), and **Alx4/Msx2 double heterozygotes** have additive defects (PMID:15198690). In humans, co-inherited heterozygous **ALX4 + TWIST1** variants produced a much larger calvarial defect than ALX4 alone (Walters 2021, PMID:33369125 — *"This report demonstrates comorbid disorders of Saethre-Chotzen syndrome and EPF in a mother and her child"*, quote via Europe PMC). The **ALX4 p.R218Q** allele is associated with persistent cranium bifidum and posterior-fossa anomalies (possible dominant-negative effect; §4).
- **Environmental:** none identified. No exposure, toxin, infectious, or lifestyle risk factor is reported in the literature for isolated EPF. A single Goldenhar-syndrome case with *asymmetric* EPF speculated about assisted reproduction and parental exposures (PMID:29416828) — not evidence for a mechanism.
- **Age/sex:** no sex predilection reported; defect size is age-dependent (shrinks with age; §8).

### Protective factors
None known. No protective alleles or exposures are described.

### Gene–environment interactions
None described. Not applicable for this disorder on current evidence.

---

## 3. Phenotypes

Frequencies below are Orphanet's HPO annotations for ORPHA:60015 (as mirrored in GARD) unless a primary source is cited. "Scale" uses Orphanet bands: Very frequent 80–99%, Occasional 5–29%, Uncommon <1–4%.

| Phenotype | Type | HPO term (verified in OLS) | Onset / course | Frequency | Notes & sources |
|---|---|---|---|---|---|
| Symmetric oval parietal bone defects (the defining feature) | Physical/imaging sign | **HP:0002697** Parietal foramina | Congenital (visible prenatally from ~18–20 wk); defects **shrink with age**, may close → non-penetrance | Very frequent (80–99%); "relatively high, but not full penetrance" | *"Typical PFM are bilateral oval or round openings in the parietal bones on either side of the posterior sagittal suture."* **[verbatim PMID:16319823]** Defect size negatively correlates with age (ANCOVA, PMID:16319823). |
| Cranium bifidum (midline defect between anterior and posterior fontanelles in infancy) | Physical sign | **HP:0004423** Cranium bifidum occultum | Infancy; usually resolves into paired foramina via a midline bony bridge | Common in infancy; persistent CB esp. with ALX4 p.R218Q | *"Frequently, PFM can be traced back to a central defect in infancy, extending between the anterior and posterior fontanelles; when this persists it is termed cranium bifidum (CB)."* **[verbatim PMID:16319823]** |
| Enlarged/persistent posterior fontanelle, delayed ossification | Physical sign | HP:0000260 Wide anterior fontanel (for anterior involvement); UBERON:0006683 posterior fontanelle (anatomy) | Neonatal | Variable | Family 12 son "had an enlarged posterior fontanelle" (PMID:16319823). |
| Headache, local pain, scalp tenderness | Symptom | **HP:0002315** Headache | Childhood–adult | Occasional (5–29%) | *"In a minority of individuals, headaches, vomiting, or intense local pain are sometimes associated with the defects, especially on application of mild pressure to the unprotected cerebral cortex."* **[verbatim PMID:20301307]** MSX2 R172H and c.468_484dup families reported headaches (Table 1, PMID:16319823). |
| Vomiting | Symptom | **HP:0002013** Vomiting | — | Occasional | GeneReviews, as above. |
| Seizures / epilepsy | Clinical sign | **HP:0001250** Seizure | Childhood (neonatal convulsions in ALX4 R218Q family) | Uncommon (<1–4%) | *"Meningeal, cortical, and vascular malformations of the posterior fossa occasionally accompany the bone defects and may predispose to epilepsy."* **[verbatim PMID:20301307]**; Kite 1961 (OMIM); Gopal 2020 case (PMID:33269135); Bello 2009 (PMID:20306736). |
| Persistent falcine sinus / persistent median prosencephalic vein; hypoplastic or absent straight sinus | Imaging sign (vascular) | **HP:6000295** Persistent falcine venous sinus; **HP:0012480** Abnormal cerebral vein morphology; **HP:0033723** Abnormal cerebral venous sinus morphology | Congenital | Reddy 2000: 6/7 imaged patients had a persistent falcine sinus (paraphrase, PMID:10720293); Orphanet "Venous malformation" Occasional | Also Fink 2006 (PMID:16775301, 2/2 fetal/neonatal MRI), Valente 2004 (PMID:15569759), Morita 2016 (PMID:27349084), Yang 2013 (PMID:23559396), Umehara 2026 (PMID:42371125). Umehara's histology study suggests persistent falcine venous structures sit at the defect (PMID:41832921). |
| Occipital cortical infolding / polymicrogyria / ulegyria | Imaging sign (cortical malformation) | **HP:0002126** Polymicrogyria | Congenital | Reddy 2000: 3/6 had occipital cortical infolding; Orphanet "Encephalomalacia" Uncommon | *"…neuroimaging demonstrated malformations of the posterior fossa, with polymicrogyria, wide spacing of the occipital lobes, persistence of the embryonic median prosencephalic vein with hypoplasia of the straight sinus, and high insertion of the tentorium cerebelli."* **[verbatim PMID:16319823, ALX4 p.R218Q family]** |
| Posterior fossa anomalies (high tentorial insertion, large posterior fossa) | Imaging sign | **HP:0000932** Abnormal posterior cranial fossa morphology; **HP:0005445** Enlarged posterior fossa | Congenital | Occasional | PMID:16319823; PMID:33269135. |
| Atretic occipital encephalocele / encephalocele mimic | Physical/imaging sign | **HP:0002085** Occipital encephalocele; HP:0004470 Atretic occipital cephalocele; **HP:0002084** Encephalocele | Prenatal/neonatal | Uncommon | Reddy 2000 (1 patient); prenatal EPF can mimic encephalocele (PMID:27080046; PMID:16775301). |
| Scalp defects (aplasia cutis), hair agenesis over defect | Physical sign (skin) | **HP:0007385** Aplasia cutis congenita of scalp; HP:0004476 Aplasia cutis congenita over parietal area | Congenital | Uncommon | OMIM clinical synopsis "scalp defect"; MSX2 p.W115X *"PFM, scalp defects, meningeal, venous, and cortical abnormalities"* (Table 1, PMID:16319823); family 20 "hair agenesis in the overlying skin" (PMID:16319823). |
| Cleft lip and/or palate | Physical sign | **HP:0000204** Cleft upper lip; **HP:0000175** Cleft palate | Congenital | Uncommon | Hollender 1967; Irvine & Taylor 1936 (OMIM 168500). |
| Short/hypoplastic clavicles (PFMCCD, MSX2) | Physical/imaging sign | **HP:0000894** Short clavicles; HP:0006608 Midclavicular hypoplasia | Congenital | Uncommon; allelic subtype | Garcia-Miñaur 2003: *"short abnormal clavicles with tapering lateral ends"* (OMIM paraphrase; PMID:14571277). |
| Broad/short thumbs and halluces (subtle preaxial polydactyly) — ALX4 | Physical sign | **HP:0011304** Broad thumb; **HP:0010055** Broad hallux; HP:0100258 Preaxial polydactyly | Congenital | Uncommon ("Broad thumb" Orphanet) | Family 10, ALX4 p.S207X: *"short, broad thumbs"* **[verbatim PMID:16319823]**; also Bertola 2013 (PMID:23401352). |
| Dental anomalies (malposition, missing incisors) — ALX4 | Physical sign | **HP:0006482** Abnormal dental morphology (coarse; use with `coarse_binding_basis` if bound) | Childhood | Uncommon | Family 10 (PMID:16319823); MSX2 dental defects segregated *independently* of the mutation. |
| Mild facial dysmorphism / frontonasal features (ALX4 heterozygotes) | Physical sign | **HP:0000316** Hypertelorism | Congenital | Uncommon | Bertola 2013 (PMID:23401352), Altunoglu 2014 (PMID:24764194): mild nasal clefting, broad columella with PFM. |
| Intellectual disability / developmental delay | Behavioral/cognitive | **HP:0001249** Intellectual disability; **HP:0001263** Global developmental delay | Childhood | Uncommon in isolated EPF; frequent in Potocki-Shaffer (PHF21A-dependent) | *"Mental development was within normal limits in all affected individuals"* in isolated families **[verbatim PMID:16319823]**; MR in P11pDS maps to a proximal 1.1 Mb interval (PHF21A). |
| Multiple exostoses | Physical sign | **HP:0002762** Multiple exostoses | Childhood | Uncommon (only with 11p11.2 deletion incl. EXT2) | Potocki-Shaffer differential. |
| Craniosynostosis | Physical sign | **HP:0001363** Craniosynostosis | — | Uncommon; occurs in P11pDS and with co-inherited TWIST1 variants; **not** caused by intragenic ALX4/MSX2 LoF | *"…intragenic mutations of either gene are not common causes of CRS and are not worth screening for routinely."* **[verbatim PMID:16319823]** |
| Ventricular septal defect | Physical sign | **HP:0001629** Ventricular septal defect | Congenital | Single family (MSX2 c.456_465dup) | Table 1, PMID:16319823 — likely coincidental. |
| Myelomeningocele / spina bifida occulta | Physical sign | HP (Orphanet lists "Myelomeningocele", Uncommon) | — | Uncommon | Terrafranca & Zellis 1953 (OMIM). |
| Microcephaly | Physical sign | **HP:0000252** Microcephaly | — | Coincidental in one family | PMID:16319823 notes microcephaly also in PFM-negative mother. |

**Quality of life.** No EQ-5D/SF-36/PROMIS data exist. Impact is dominated by (a) anxiety about penetrating injury and sports restriction while the midline defect persists, (b) headaches in a minority, (c) epilepsy where cortical malformation coexists. GeneReviews: *"The risk for penetrating injury to the brain is small but may cause anxiety; education of parents, teachers, and the affected child to avoid risky behaviors that could result in injury suffices in most circumstances."* **[verbatim PMID:20301307]**

---

## 4. Genetic / Molecular Information

### Causal genes

| Gene | HGNC | NCBI Gene | Location (GRCh38) | Protein (UniProt) | OMIM gene | Disease |
|---|---|---|---|---|---|---|
| MSX2 (msh homeobox 2) | hgnc:7392 | 4488 | chr5:174,724,551–174,730,896 (+) | P35548, Homeobox protein MSX-2, 267 aa, homeobox 142–201, nuclear | 123101 | PFM1 (#168500); PFMCCD (#168550); Boston-type craniosynostosis 2 (gain-of-function) |
| ALX4 (ALX homeobox 4) | hgnc:450 | 60529 | chr11:44,260,440–44,310,139 (−) | Q9H161, Homeobox protein aristaless-like 4, 411 aa, homeobox 214–273, nuclear | 605420 | PFM2 (#609597); Potocki-Shaffer (deletion); frontonasal dysplasia 2 (AR, biallelic) |

Sources: Alliance of Genome Resources gene API; UniProt REST; OMIM mirror.

### Gene–disease validity (copied, not assigned)
- **ClinGen (Craniofacial Malformations GCEP):** MSX2 – *parietal foramina* (MONDO:0018953): **Definitive**, AD, 2020-07-08. MSX2 – *craniosynostosis 2* (MONDO:0011481): Definitive, AD, 2020-09-28. ALX4 – *frontonasal dysplasia with alopecia and genital anomaly* (MONDO:0013268): Definitive, **AR**, 2023-01-19. **No ClinGen validity curation for ALX4–parietal foramina 2 was listed** (search.clinicalgenome.org, retrieved 2026-10-15). Neither gene is in the repository's committed `cache/clingen/gene_validity.csv` export or `references_cache/CGGV_*.md`; a `just clingen-refresh` would be needed before citing a CGGV: record.
- **ClinGen Dosage Sensitivity:** ALX4 haploinsufficiency score **3** (Sufficient Evidence), for parietal foramina 2 (MONDO:0012309), 2020-07-22; triplosensitivity 0. MSX2 haploinsufficiency score **1** (Little Evidence) for parietal foramina 1, 2023-06-28; triplosensitivity 0. *(Note the tension: ClinGen's validity panel rates MSX2–PFM Definitive while the dosage group scored haploinsufficiency only "1"; the whole-gene 206 kb deletion in PMID:10742103 is relevant evidence to review.)*
- GenCC API returned 404; not retrieved.

### Pathogenic variant spectrum
From Table 1 of Mavrogiannis et al. 2006 **[verbatim table, PMID:16319823]** (numbering from GenBank AJ404888 for ALX4, D89377 for MSX2):

**ALX4 (intragenic, heterozygous):** c.343_344insC p.Q115PfsX43 (PFM); c.385_394del p.C129PfsX49 (PFM); c.418C>T p.Q140X (PFM/CB); c.504del p.D169TfsX12 (PFM); c.620C>A p.S207X (PFM/CB, dental defects, facial dysmorphism, broad short thumbs/halluces); **c.653G>A p.R218Q** (PFM/CB, meningeal defects, neonatal convulsions; two unrelated families); c.736C>T p.Q246X (PFM/CB); c.815G>C p.R272P (PFM). Later: c.646C>G p.Arg216Gly (Altunoglu 2014, PMID:24764194, PFM + mild nasal clefting); c.1080_1089delins… p.Asp326fsX21 (Bertola 2013, PMID:23401352, PFM + frontonasal features; C-terminal aristaless domain lost, homeodomain preserved; proposed dominant-negative); c.793C>T p.Arg265Ter (nonsense; heterozygous in Umehara 2026 familial EPF + AVM, PMID:42371125; **homozygous** in FND2, Goswami 2024, PMID:39157323); c.291delG homozygous → FND2 with parietal foramina in heterozygous parents (El-Ruby 2018, PMID:29681084); an undescribed ALX4 variant in a Spanish family (Bote Gascón 2021, PMID:34315693; abstract not retrievable).

**MSX2 (intragenic, heterozygous):** c.265_266delinsTA p.A89X (PFM); c.345del p.W115X (PFM, scalp defects, meningeal/venous/cortical abnormalities); c.417_418del p.H139QfsX105 (PFM); c.456_465dup p.A156PfsX92 (PFM, VSD); c.461T>C p.L154P (PFM); c.468_484dup p.R162PfsX24 (PFM, headaches, venous malformations); c.475_480del p.R159_K160del (PFM); c.505_508dup p.A170DfsX76 (**PFMCCD**); **c.515G>A p.R172H** (PFM, headaches; two unrelated families); an 8-bp deletion (Spruijt 2005; OMIM 123101.0008). Contrast: **c.443C>A p.P148H** → Boston-type craniosynostosis (gain of DNA-binding affinity; PMID:8968743), and c.443C>T p.P148L (Florisson 2013, PMID:23949913).

**Whole-gene / contiguous deletions:** ~206 kb deletion including all of MSX2 (PMID:10742103); 11p11.2 deletions 2.1 Mb to >29 Mb encompassing ALX4 ± EXT2 ± PHF21A (Potocki-Shaffer; PMID:15852040, PMID:34879425); distal 5q deletions (PMID:19952731).

**Variant classes:** nonsense and frameshift predominate; missense clustered in the homeodomain (MSX2 R172H, L154P; ALX4 R218Q, R272P, R216G); in-frame homeodomain deletion (MSX2 RK159-160del); whole-gene deletion. *"Loss-of-function follows directly for the various nonsense and frameshift mutations, some of which may target transcripts for nonsense-mediated decay, although this is less likely for the changes occurring within the second (and terminal) exon of MSX2."* **[verbatim PMID:16319823]**

**ClinVar (E-utilities, 2026-10-15):** 244 records for ALX4 or MSX2 with condition "parietal foramina"; 23 of these Pathogenic/Likely pathogenic. Gene-wide P/LP counts: ALX4 43, MSX2 31 (all conditions). Umehara 2026 notes no exact ClinVar match for p.Arg265Ter at time of writing.

**Population frequency:** Pathogenic alleles are private/ultra-rare; no gnomAD constraint metrics were retrieved in this session (not checked). Common ALX4 polymorphisms (p.R35T 0.48, p.P102S 0.43; rs3824915, rs12421995) complicate DHPLC screening (Table 2, PMID:16319823).

**Origin:** germline, heterozygous. No somatic/mosaic EPF reported. Not a repeat-expansion disorder.

### Functional consequence
Loss of function / haploinsufficiency for both genes: *"Although haploinsufficiency is clearly the major genetic mechanism in PFM, the p.R218Q mutation may exert additional, dominant-negative effects."* **[verbatim PMID:16319823]** For the KB: `functional_impact_category: LOSS_OF_FUNCTION` on the gene; `HAPLOINSUFFICIENT`/dominant-negative nuance for R218Q (and the Bertola frameshift) belongs in variant `description`/`notes`, not asserted as established.

### Modifier genes
Human: TWIST1 (co-inheritance → large calvarial defect; PMID:33369125); reciprocal MSX2/ALX4 coding variants excluded as modifiers (PMID:16319823). Mouse: Msx1 (PMID:10742104), Twist1 (PMID:14597577), Alx4↔Msx2 (PMID:15198690), Cart1/Alx1 (PMID:9847249), strain background for Alx4 (PMID:9636085).

### Epigenetics
No disease-specific DNA methylation, histone, or chromatin data were identified (searched PubMed; none). Not applicable.

### Chromosomal abnormalities
11p11.2 interstitial deletions (Potocki-Shaffer; the 1.1 Mb MR-critical interval D11S554–D11S1319 containing PHF21A lies proximal to ALX4 — PMID:16319823, PMID:15852040, PMID:22770980); distal 5q35 deletions including MSX2 (PMID:19952731). Reciprocal dosage: MSX2 duplication/triplication (dup 5q35) → craniosynostosis (PMID:18000908, PMID:24666290), confirming the dosage model.

---

## 5. Environmental Information
- **Environmental factors:** none identified.
- **Lifestyle factors:** none identified (only secondary avoidance of head trauma/contact sports while the defect is open).
- **Infectious agents:** not applicable.
For the KB, leave `environmental:` empty; do not fabricate an exposure.

---

## 6. Mechanism / Pathophysiology

### Causal chain (initiating lesion → clinical manifestation)
1. **Heterozygous loss-of-function variant in MSX2 or ALX4** (nonsense, frameshift, homeodomain missense, or whole-gene deletion) **leads to** ~50% reduction of functional homeodomain transcription factor (haploinsufficiency; for MSX2 R172H/RK159-160del, >85% loss of DNA binding demonstrated in vitro **[PMID:10742103]**).
2. Reduced MSX2/ALX4 **results in** impaired BMP/FOXC1-dependent **proliferation of osteoprogenitor cells at the osteogenic fronts** of the calvarial (ectomeninx-derived) mesenchyme. *"This phenotype results from defective proliferation of osteoprogenitors at the osteogenic front during calvarial morphogenesis, and closely resembles that associated with human MSX2 haploinsufficiency in parietal foramina (PFM)."* **[verbatim, Msx2-null mouse, PMID:10742104]** Foxc1 is required for BMP induction of both Msx2 and Alx4 in calvarial mesenchyme (Rice 2003, PMID:14512019, paraphrase). The two genes cross-regulate and act additively (Antonopoulou 2004, PMID:15198690, paraphrase) and Msx2 acts at the same level as Twist1 (Ishii 2003, PMID:14597577). *Demonstrated in mouse; inferred for human.*
3. Deficient osteoprogenitor expansion **leads to** delayed/deficient **intramembranous ossification** of the parietal bone during the period of rapid calvarial expansion, specifically around the **parietal notch**. *"…are caused by delayed ossification during rapid calvarial expansion."* **[verbatim PMID:16319823]** Histology of adult EPF shows abrupt cortical thinning with fibrovascular tissue at the margin and no erosion or inflammation, supporting a congenital ossification defect (Seltzer 2026, PMID:41832921, paraphrase).
4. Persistence of the unossified parietal notch **results in** a midline **cranium bifidum** in infancy, which through circumferential bone growth **becomes** paired symmetric **enlarged parietal foramina** that **shrink with age** and may close (clinical non-penetrance). **[PMID:16319823]**
5. **Branch — dura/venous:** Because Alx4 and Msx2 are both expressed in the **ectomeninx**, the common primordium of the calvarial bones and dura, reduced dosage **is inferred to** cause a parallel patterning defect of the dura/falx, **manifesting as** persistent falcine sinus / median prosencephalic vein, hypoplastic straight sinus, and high tentorial insertion. *"The similarity of the dural and calvarial abnormalities consequent upon reduced expression of both ALX4 or MSX2 suggests that a comparable defect in patterning of the ectomeninx underlies both disorders."* **[verbatim PMID:16319823]** *Inferred.*
6. **Branch — cortex:** Posterior-fossa and occipital **cortical malformation (polymicrogyria, ulegyria, cortical infolding)** co-occurs, especially with ALX4 p.R218Q and 11p deletions; mechanism unknown (possibly secondary to abnormal venous drainage/dura, or a direct neural-crest/meningeal effect). **Leads to** epilepsy in a minority. *Associational; mechanism not demonstrated.*
7. **Branch — exposed cortex:** The unprotected brain beneath the defect **results in** pressure-induced headache/local pain and a small risk of penetrating injury; rare subjacent vascular lesions (AVM) have been reported, with inflammatory tissue in the defect, *"hypothesis-generating rather than causal"* (Umehara 2026, PMID:42371125).

### Contrast with gain of function
*"…PFM and craniosynostosis result, respectively, from loss and gain of activity in an MSX2-mediated pathway of calvarial osteogenic differentiation."* **[verbatim PMID:10742103]** P148H increases DNA-binding affinity (PMID:8968743); transgenic Msx2 overexpression causes premature suture closure and expands proliferative osteogenic cells (PMID:7597092, PMID:9917362); MSX2 duplication/triplication causes craniosynostosis in humans (PMID:18000908). (One study argues P148H is unstable and dominant-negative, PMID:18786927 — note the disagreement.)

### Molecular pathways and processes (GO/CL/UBERON suggestions, all OLS-verified)
- **Molecular function:** GO:0000981 *DNA-binding transcription factor activity, RNA polymerase II-specific* (`modifier: DECREASED`); MSX2 acts as a transcriptional repressor (represses ALPL, osteocalcin FRE, Runx2 activity — UniProt P35548; Shirakabe 2001, PMID:11683913); ALX4 is a transcriptional activator (Hudson 1998, PMID:9786416).
- **Cellular component:** GO:0005634 *nucleus*.
- **Biological processes:** GO:0033687 *osteoblast proliferation* (DECREASED; the key node); GO:0001649 *osteoblast differentiation* (dysregulated — Msx2 normally maintains proliferation and delays differentiation, PMID:10328922, PMID:19860126); GO:0001957 *intramembranous ossification* (DECREASED); GO:0048704 *embryonic skeletal system morphogenesis*. Upstream signaling: BMP (Bmp4 induces Msx2/Alx4; PMID:14512019), FGF/FGFR1-2 (reduced in both mutants, PMID:15198690; FGF induces Msx2, PMID:12674336), TGFβR2 (PMID:19699732), FOXC1, TWIST1.
- **Cell types:** CL:2000058 *calvarial osteoblast*; CL:0007010 *preosteoblast*; CL:0000335 *mesenchyme condensation cell*; CL:0000008 *migratory cranial neural crest cell* (frontal bone/ectomeninx lineage; Alx4 conditional deletion in cranial neural crest reproduces craniofacial defects — Lan 2024, PMID:38481039). Note the parietal bone is mesoderm-derived in mouse, while the dura beneath it is neural crest-derived; the human parietal lineage is inferred.
- **Metabolic, immune, epigenetic:** no primary metabolic or immune mechanism. No omics (transcriptomic/proteomic/single-cell/spatial) datasets specific to EPF were found in GEO searches reported in the literature; none identified.

---

## 7. Anatomical Structures Affected

- **Primary organ/structure:** skull vault — **UBERON:0004339** *vault of skull*; **UBERON:0000210** *tetrapod parietal bone*; **UBERON:0006274** *tetrapod parietal bone primordium*. Site: posterior parasagittal parietal bone adjacent to **UBERON:0002492** *sagittal suture* and **UBERON:0002491** *lambdoid suture*, near **UBERON:0013424** (lambda) / **UBERON:0006683** *posterior fontanelle*.
- **Secondary structures:** dura and falx — **UBERON:0002363** *dura mater*, **UBERON:0006059** *falx cerebri* (Alx4 expressed in falx; PMID:16319823); dural venous sinuses (persistent falcine sinus; straight sinus hypoplasia — UBERON straight sinus term not found in OLS search; use HP:6000295 on the phenotype side); occipital cortex; scalp (**UBERON:0000403** *scalp*) and hair; clavicle (PFMCCD); thumbs/halluces and teeth (ALX4).
- **Body systems:** skeletal (primary); nervous and cerebrovascular (secondary); integumentary (rare).
- **Tissue/cell level:** intramembranous bone / osteogenic mesenchyme; calvarial osteoblasts and preosteoblasts (CL terms above); meningeal mesenchyme (ectomeninx).
- **Subcellular:** nucleus (GO:0005634) — transcription-factor defect.
- **Lateralization:** **bilateral and symmetric** by definition (asymmetric EPF is atypical and should prompt consideration of other diagnoses, e.g., PMID:29416828).

---

## 8. Temporal Development

- **Onset:** congenital; defects are detectable on fetal ultrasound at 18–20 weeks and fetal MRI (GeneReviews **[verbatim]**: *"Detailed fetal ultrasound examination at 18 to 20 weeks' gestation can usually detect the defects in a fetus at risk; fetal MRI is also an option."*). Orphanet: onset antenatal/neonatal. Pattern: a static developmental defect, not acquired.
- **Progression:** **regressive, not progressive.** Infant cranium bifidum → bony bridge → paired foramina → progressive shrinkage with age through circumferential growth; complete closure possible. *"There is a significant negative correlation with age for mutations in either gene."* **[verbatim PMID:16319823]** Spontaneous regression is common but *"closure is rarely complete"* (Wallace 2023, PMID:37126764, paraphrase). Adult skulls with 12 mm defects are documented (PMID:40411931; 4000-year-old archaeological case PMID:39729874).
- **Stages (for `progression:`):** (1) fetal/neonatal midline defect (cranium bifidum); (2) early childhood bridging into bilateral foramina (typically by ~10 months to 5 years; Spruijt 2005: narrowed to bilateral ~2 cm foramina by 10 months); (3) childhood–adolescent shrinkage; (4) adult residual foramina (variable size) or closure.
- **Disease duration:** lifelong anatomical variant; symptomatic manifestations (headache) may persist in adults.
- **Remission patterns:** spontaneous shrinkage as above; no treatment-induced remission other than surgical closure.
- **Critical periods:** fifth fetal month (normal obliteration of the parietal notch); the period of persistent midline defect (infancy/early childhood) is the window of injury risk and the only window in which surgical closure is usually considered.

---

## 9. Inheritance and Population

### Epidemiology
- **Orphanet (Orphadata epidemiology, ORPHA:60015):** point prevalence class **1–9 / 100,000**, Europe 4.3 per 100,000 and Worldwide 3.7 per 100,000, both "Validated", attributed to PMID:23543411 — a Greek dry-skull case report (Piagkou 2013) that itself states no prevalence figure. **Treat the Orphanet numeric values as weakly sourced**; the class band is the defensible claim. Map to `prevalence_class: BAND_1_9_PER_100000`, `measure_type: POINT_PREVALENCE`.
- **Secondary sources:** MedlinePlus Genetics gives 1 in 15,000–50,000; Wikipedia and a 2018 J Morphol Sci review give 1:15,000–1:25,000; a 2012 Folia Morphologica paper says <1:25,000. The 1:15,000–1:25,000 figure is widely repeated but a primary epidemiological source was not identified in this search (GeneReviews full text could not be fetched; its prevalence sentence should be checked in the NBK1128 cache).
- **Anatomical surveys (small foramina, not EPF):** ordinary parietal foramina are present in ~40–84% of skulls (PMID:40193663, PMID:33399919, PMID:42857514); **EPF (>5 mm) found in 2/250 adult skulls (0.8%)** in one osteological series (Seltzer 2026, PMID:41832921) — a skull-collection figure, not a population prevalence.
- **Incidence:** no incidence data.

### Genetics
- **Inheritance:** autosomal dominant (all forms: PFM1, PFM2, PFM3, PFMCCD). HPO mode-of-inheritance term for the `inheritance:` block should be looked up (Autosomal dominant inheritance) at the time of writing.
- **Penetrance:** high but incomplete; age-dependent (closure → non-penetrance). *"The skull defects in mutation-positive cases show relatively high, but not full penetrance, and their severity and presentation may vary."* **[verbatim PMID:16319823]** Morita 2016: grandmother carried the ALX4 mutation without skull defects (PMID:27349084).
- **Expressivity:** highly variable, including intrafamilial (OMIM: "considerable intrafamilial variability", Spruijt 2005; Goldsmith 1922 described 16 cases over 5 generations of the Catlin family).
- **Anticipation:** none; not a repeat disorder.
- **Germline mosaicism:** not reported.
- **Founder effects:** none; most variants private. Two unrelated families each share MSX2 R172H and ALX4 R218Q (recurrent, not founder).
- **Consanguinity:** irrelevant for AD EPF; relevant for the AR allelic condition FND2 (homozygous ALX4), where heterozygous parents may show PFM (PMID:29681084, PMID:39157323).
- **Carrier frequency:** not applicable (dominant).
- **Mutation detection:** *"Mutation screening has a high pickup rate in PFM, especially in familial cases, but is not indicated in CRS."* **[verbatim PMID:16319823]** (11/13 familial vs 1/6 sporadic.)

### Demographics
Reported worldwide (UK, Czech, Brazilian, Spanish, Chinese, Japanese, Nigerian, Turkish, Egyptian, Bangladeshi, Greek, Serbian, US families). No ethnic predilection; no sex difference reported; age distribution reflects congenital onset with lifelong persistence.

---

## 10. Diagnostics

- **Imaging (primary diagnostic modality):** plain skull radiograph (postero-anterior view; defect width measured as fraction of skull width), **CT with 3D reconstruction** (NCIT:C17204 *Computed Tomography*), **brain MRI/MR venography** (NCIT:C16809 *Magnetic Resonance Imaging*) to assess cortical and venous anomalies — Reddy 2000 recommends brain and vascular imaging for foramina >5 mm (PMID:10720293, paraphrase). Prenatal: detailed fetal ultrasound at 18–20 weeks (NCIT:C222238 *Fetal Ultrasound Imaging*) and fetal MRI (PMID:16775301). Pitfalls: EPF mislabeled as burr holes (PMID:31427498), mistaken for encephalocele prenatally (PMID:27080046), or for gunshot wounds forensically (PMID:40411931). An AI image tool suggested the diagnosis in one 2026 case (PMID:41543485).
- **Laboratory tests / biomarkers:** none; no biochemical marker. Not applicable (no LOINC analyte).
- **Electrophysiology:** EEG only if seizures.
- **Histopathology:** rarely obtained; defect margin shows abrupt cortical thinning with fibrovascular tissue and no erosion/inflammation (PMID:41832921); inflammatory infiltrate reported in one AVM case post-rupture (PMID:42371125).
- **Genetic testing:** diagnosis established by characteristic imaging plus a heterozygous pathogenic variant in **ALX4 or MSX2** **[verbatim PMID:20301307]**. Recommended approach: sequencing of both genes (direct sequencing preferred over DHPLC because of ALX4 polymorphisms) **plus** deletion/duplication analysis (MLPA P080 craniofacial kit, or CMA) — *"dosage analysis should be part of any testing strategy"* **[verbatim PMID:16319823]**. Multigene craniofacial panels or exome (NCIT:C101295 *Whole Exome Sequencing*) are appropriate when atypical. **CMA** is indicated when exostoses, intellectual disability, or dysmorphism suggest Potocki-Shaffer (11p11.2). Karyotype/FISH historically used for 11p deletions. Mitochondrial, repeat-expansion, omics-based diagnostics: not applicable.
- **Clinical criteria:** no formal consensus criteria; definition in the literature is bilateral symmetric parietal defects **>5 mm** (PMID:10720293, PMID:33269135).
- **Differential diagnosis:** Potocki-Shaffer syndrome (EPF + multiple exostoses ± ID; 11p11.2 deletion); PFMCCD (clavicular hypoplasia; MSX2); classic cleidocranial dysplasia (RUNX2; delayed fontanel closure, wormian bones); ALX4-related frontonasal dysplasia 2 (biallelic; large skull defects, alopecia, hypertelorism); CDAGS syndrome (AR, 22q12-q13, craniosynostosis + parietal foramina + imperforate anus; MSX2-negative, PMID:15924278); Saethre-Chotzen/TWIST1 (co-occurrence, PMID:33369125); Adams-Oliver syndrome (scalp aplasia cutis + skull defects; MSX2 excluded in AOS, PMID:16319823); ZIC1-related caput membranaceum (PMID:32975022); CDC42BPB-related Chilton-Okur-Chung syndrome with EPF (single case, PMID:41543485); FG syndrome (Chrzanowska 1998 case); encephalocele/cephalocele; burr holes/trephination; lytic calvarial lesions (histiocytosis, metastasis — PMID:34197249).
- **Screening:** no population or newborn screening. Cascade imaging/genetic testing of first-degree relatives is reasonable given high familial pickup.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** no excess mortality reported; life expectancy normal. No disease-specific mortality data (not applicable).
- **Morbidity:** generally benign. *"…the phenotypic outcome of heterozygous mutations is surprisingly similar, and is usually benign. In particular, we note that all affected individuals in the two families transmitting the ALX4 p.R218Q mutation have been managed conservatively without significant problems, despite the persistently large skull defects."* **[verbatim PMID:16319823]** Morbidity when present: headaches, epilepsy (with cortical malformation), injury risk, anxiety/activity restriction, surgical complications (graft failure, infection).
- **Disability/QoL:** no ICF or validated QoL data.
- **Complications:** epilepsy; rare intracranial hemorrhage from a subjacent AVM (single 2026 case, PMID:42371125); theoretical penetrating injury; posterior fossa venous anomalies are generally asymptomatic.
- **Recovery potential:** defects spontaneously shrink; complete closure uncommon but functional outcome excellent with or without surgery.
- **Prognostic factors:** gene does not predict severity (ALX4 vs MSX2 P = 0.30); **ALX4 p.R218Q** predicts larger, persistent defects (P < 0.001, post hoc) and posterior-fossa anomalies; presence of cortical malformation predicts epilepsy risk; 11p deletion extent (PHF21A involvement) predicts intellectual disability (PMID:33126574, PMID:30487643). No molecular prognostic biomarkers beyond genotype.

---

## 12. Treatment

Treatment is **conservative by default**; EPF has no disease-modifying pharmacotherapy. GeneReviews **[verbatim PMID:20301307]**: *"Treatment is generally conservative. Persistent cranium bifidum may warrant operative closure… Treatment of seizures per neurologist; symptomatic treatment of headaches. Surveillance: Assess osseous defect every six to 12 months until natural history is established… Agents/circumstances to avoid: Contact sports in those with a persistent midline bony defect."*

| Treatment | Modality | NCIT suggestion (OLS-verified) | Notes / evidence |
|---|---|---|---|
| Conservative management, surveillance imaging q6–12 months, protective education (helmet/avoid contact sports while midline defect persists) | BEHAVIORAL / supportive | NCIT:C16959 *Patient Education*; NCIT:C15747 Supportive Care (listed in CLAUDE.md; verify label at binding time) | PMID:20301307; PMID:20306736 ("health education and reassurance are generally sufficient"); PMID:23559396 |
| Surgical closure of persistent cranium bifidum / large foramina (autologous bone graft, titanium mesh, custom porous polyethylene implant, split-bone technique) | SURGERY | NCIT:C15329 *Surgical Procedure* (NCIT has **no** "cranioplasty" term per OLS search; carry specificity in `preferred_term`); NCIT:C116464 *Bone Graft* | Family 11: titanium mesh at age 5; family 12: bone grafting before age 1 (PMID:16319823). Porous polyethylene implant (PMID:37126764). Risks: *"notably, graft failure and infection"* **[verbatim PMID:16319823]**. Indication is individualized; benefit is protection, not function. |
| Antiseizure medication for associated epilepsy | SMALL_MOLECULE | NCIT:C64172 *Anticonvulsant Therapy*; agent class NCIT:C264 *Anticonvulsant Agent* | Symptomatic; per neurologist (PMID:20301307). |
| Analgesics for headache | SMALL_MOLECULE | NCIT:C15986 Pharmacotherapy (verify) | Symptomatic. |
| Genetic counseling; prenatal/preimplantation testing | counseling | NCIT:C15240 *Genetic Counseling* | 50% recurrence risk; PGT/prenatal testing possible when variant known (PMID:20301307; PMID:33269135 recommends considering PGD). |
| Microsurgical resection of a subjacent AVM | SURGERY | NCIT:C15214 *Craniotomy* (approach through the defect) | Single case (PMID:42371125). |

- **Advanced therapeutics (gene/cell/RNA/targeted/immunotherapy):** none; not applicable. No clinical trials for EPF were identified (ClinicalTrials.gov search term "parietal foramina" was not run; none cited in any retrieved paper).
- **Pharmacogenomics:** not applicable.
- **Treatment outcomes:** surgical series are anecdotal (case reports); no response rates. Conservative management outcomes are uniformly good in the Oxford series.
- **Treatment algorithm:** imaging confirmation → brain MRI/MRV → genetic testing (ALX4/MSX2 sequencing + dosage; CMA if syndromic) → conservative management with surveillance; surgery only for persistent large midline defects or patient/family preference after weighing graft failure/infection risk.

---

## 13. Prevention

- **Primary prevention:** not possible for an inherited germline variant other than reproductive options (preimplantation genetic testing, prenatal diagnosis).
- **Secondary prevention (early detection):** fetal ultrasound 18–20 weeks / fetal MRI in at-risk pregnancies; neonatal skull assessment and imaging of at-risk relatives; brain MRI to detect cortical/venous anomalies that predispose to epilepsy (Reddy 2000 recommendation; Gopal 2020).
- **Tertiary prevention:** head-injury avoidance (contact sports) while midline defect persists; seizure management; surveillance until natural history (closure trajectory) is established.
- **Immunization, public health, behavioral, prophylaxis:** not applicable beyond the injury-avoidance counseling above.
- **Genetic counseling:** AD; 50% risk to each child; variable expressivity and incomplete penetrance must be conveyed; parents should be imaged (an "unaffected" parent may have closed foramina or indentations — family 13 mother had "bilateral indentations of both parietal areas", PMID:16319823). Counseling is complicated in ALX4 because heterozygotes in FND2 families may show PFM or mild nasal clefting (PMID:24764194, PMID:29681084).

---

## 14. Other Species / Natural Disease

- **Taxonomy:** *Homo sapiens* (NCBITaxon:9606). No naturally occurring EPF is recorded in companion animals or livestock; OMIA was not searched directly in this session. A feline litter with cranium bifidum/meningocele after gestational progestin exposure (PMID:42050592) is a teratogenic midline defect, not EPF. Canine cranium bifidum appears only as a definition in a meningocele review (PMID:40201081).
- **Orthologs:** mouse *Msx2* — NCBI Gene 17702, MGI:97169 (chr13); mouse *Alx4* — NCBI Gene 11695, MGI:108359 (chr2) (NCBI E-utilities; mygene.info). Chick Alx-4 (PMID:9778501).
- **Comparative biology:** the parietal foramen/ossification-defect phenotype is conserved in Msx2-null mice (persistent calvarial foramen) but **species-specific dosage sensitivity** differs: Alx4+/- mice have polydactyly but essentially no skull defect, whereas human ALX4 heterozygotes have EPF (PMID:11017806; Oxford thesis via search). Alx4 haploinsufficiency in mouse is strongly strain-modified (PMID:9636085). The paleopathological record documents EPF in a ~4000 BP Chinchorro individual (PMID:39729874).
- **Zoonotic potential / cross-species transmission:** not applicable.

---

## 15. Model Organisms

| Model | Genotype | Phenotype recapitulation | Limitations | Key refs |
|---|---|---|---|---|
| **Msx2-null mouse** (knockout) | Msx2−/− | *"Msx2-deficient mice have defects of skull ossification and persistent calvarial foramen… resembles that associated with human MSX2 haploinsufficiency in parietal foramina (PFM)… Msx2-mutant mice also display defective tooth, hair follicle and mammary gland development, and seizures, the latter accompanied by abnormal development of the cerebellum."* **[verbatim PMID:10742104]** Recapitulates foramen, seizures/cerebellar anomaly (posterior fossa parallel), scalp/hair and dental features. Calvarial osteoblast cultures show reduced proliferation, accelerated differentiation (PMID:19860126). | Homozygous loss needed for robust foramen (human disease is heterozygous); frontal rather than parietal localization in Ishii 2003; pleiotropic endochondral/Pthr defects not seen in humans. `relationship: PARTIALLY_RECAPITULATES`, `fidelity: MODERATE`, `divergences: SPECIES_MISMATCH` (dosage) | PMID:10742104; PMID:14597577; PMID:19860126 |
| **Msx2;Msx1 compound mutants** | Msx2−/−;Msx1+/− etc. | Calvarial defects enhanced — *"Msx gene dosage can modify expression of the PFM phenotype."* **[verbatim PMID:10742104]** | Modifier model only | PMID:10742104 |
| **Msx2;Twist1 double mutants** | Msx2−/−;Twist1+/− | Enlarged foramen from reduced skeletogenic mesenchyme proliferation/differentiation; Msx2 and Twist act at same level (PMID:14597577) | Frontal bone focus | PMID:14597577 |
| **Alx4-null / Strong's luxoid (lst) mice** | Alx4−/−; lst alleles (incl. 16-bp homeobox deletion lst^J) | Reduced parietal bone size, preaxial polydactyly, ventral body-wall defects; heterozygotes: polydactyly with strain-dependent penetrance but **no skull defect** | Fails to recapitulate heterozygous skull phenotype → `relationship: FAILS_TO_RECAPITULATE` at heterozygous dose for the parietal node; `SPECIES_MISMATCH` | PMID:9374397; PMID:9636085; PMID:9778501; PMID:11017806 |
| **Alx4;Msx2 double heterozygous/homozygous mice** | Alx4+/−;Msx2+/− etc. | *"Our observations suggest that Alx4 and Msx2 are partially functionally redundant"* (quote via Europe PMC, PMID:15198690); skull vault defects worsen additively with allele loss; reciprocal expression dependence; Fgfr1/2 reduced; Spp1 delayed; ALP reduced | Additivity demonstrates the shared pathway behind the "clinically indistinguishable" human phenotype | PMID:15198690 |
| **Alx4 conditional (floxed) mice** | Wnt1-Cre or Prx1-Cre; Alx4 flox | Neural crest-specific deletion reproduces craniofacial defects and anterior-skull hair loss; lineage-specific, partly redundant roles | Newer resource (2024); parietal phenotype detail per lineage to be confirmed | PMID:38481039 |
| **Foxc1 (congenital hydrocephalus, ch) mutant** | Foxc1−/− | Calvarial mesenchyme fails to express Msx2 and Alx4; BMP cannot induce them → arrested calvarial osteogenesis | Upstream-regulator model, not an EPF model | PMID:14512019 |
| **Msx2 transgenic / P148H transgenic mice** | Msx2 overexpression; human MSX2 P148H | Craniosynostosis, ectopic cranial bone, expanded osteogenic proliferation — the reciprocal (gain) phenotype | Models craniosynostosis, not EPF; useful as `REFUTE`/contrast evidence for dosage | PMID:7597092; PMID:9917362; PMID:9147639 |
| **Chick calvarial osteoblast culture** | Retroviral Msx2 sense/antisense | Msx2 maintains proliferation and blocks differentiation at osteogenic fronts | In vitro, avian | PMID:10328922 |

- **IMPC:** no genotype-phenotype records for Alx4 or Msx2 in the IMPC Solr endpoint (2026-10-15).
- **Resources:** MGI (MGI:97169 Msx2; MGI:108359 Alx4); IMSR/MMRRC for Msx2 tm1 and Alx4 lst strains (not individually verified here).
- **Research applications:** calvarial osteogenesis, suture biology, BMP/FGF/FOXC1/TWIST regulatory network, ectomeninx/dura patterning, dosage-dependent transcription factor disease.

---

## Key Primary References (PMID)

| PMID | First author, year | Role |
|---|---|---|
| 20301307 | Mavrogiannis & Wilkie (GeneReviews) | Clinical baseline; diagnosis; management; counseling |
| 10742103 | Wilkie 2000, Nat Genet | MSX2 haploinsufficiency discovery; DNA-binding assays |
| 10767351 | Wuyts 2000, Hum Mol Genet | MSX2 mutations in 4/5 FPP families |
| 11106354 | Wuyts 2000, J Med Genet | ALX4 cloning; mutations in 2/3 MSX2-negative families |
| 11017806 | Wu 2000, AJHG | ALX4 deleted in 11p11.2 syndrome; bone-restricted expression |
| 11137991 | Mavrogiannis 2001, Nat Genet | ALX4 haploinsufficiency established |
| 16319823 | Mavrogiannis 2006, EJHG (full text cached) | Genotype–phenotype; mutation table; penetrance; R218Q; ectomeninx hypothesis; management advice |
| 14571277 | Garcia-Miñaur 2003, EJHG | PFMCCD caused by MSX2 |
| 12905082 | Chen 2003, J Hum Genet | PFM3 locus 4q21-q23 |
| 10720293 | Reddy 2000, Neurology | Venous/cortical anomalies in 7 imaged patients |
| 15569759 | Valente 2004, AJNR | Cortical & vascular malformation in ALX4 family |
| 16775301 | Fink 2006, AJNR | Fetal/neonatal MRI features |
| 10742104 | Satokata 2000, Nat Genet | Msx2-null mouse |
| 15198690 | Antonopoulou 2004, J Anat | Alx4/Msx2 additive roles |
| 14597577 | Ishii 2003, Development | Msx2–Twist cooperation |
| 14512019 | Rice 2003, Dev Biol | Foxc1 → Msx2/Alx4 via BMP |
| 9374397 / 9636085 | Qu 1997/1998, Development | Alx4 null & luxoid mice |
| 38481039 | Lan 2024, Dev Dyn | Conditional Alx4 |
| 8968743 / 7597092 / 18000908 | Ma 1996; Liu 1995; Bernardini 2007 | MSX2 gain-of-function contrast |
| 15852040 / 22770980 / 33126574 | Wakui 2005; Kim 2012; Trajkova 2020 | Potocki-Shaffer critical regions; PHF21A |
| 23401352 / 24764194 / 29681084 / 39157323 | Bertola 2013; Altunoglu 2014; El-Ruby 2018; Goswami 2024 | ALX4 allelic spectrum (dominant frontonasal features; AR FND2 with PFM in carriers) |
| 33369125 | Walters 2021, AJMG A | ALX4 + TWIST1 synergy |
| 27349084 / 33269135 / 42371125 / 38447947 / 37126764 / 41832921 | Morita 2016; Gopal 2020; Umehara 2026; Kahl 2024; Wallace 2023; Seltzer 2026 | Recent cases, histology, surgery |
| 23543411 | Piagkou 2013 | Orphanet's cited (weak) prevalence source |

**Not retrieved / caveats:** OMIM.org and Orphanet.org pages returned 403 / bot-check (OMIM mirror and Orphadata API used instead); OMIM %609566 (PFM3) text not available (Chen 2003 abstract used); GenCC API 404; gnomAD constraint not queried; GeneReviews full text (NBK1128) not accessible beyond the cached abstract, so the often-quoted "1:15,000–1:25,000" prevalence remains without a verified primary source; ClinicalTrials.gov not searched (no trials cited anywhere in the retrieved literature).

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 69 |
| Resolved | 69 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 69 |
| On topic | 37 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 81 |
| Resolved | 75 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 6 |
| Terms whose name was checked | 6 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0018953` (3 mentions) - the report calls it "MONDO", "parietal foramina"; MONDO calls it **parietal foramina**
- `DOID:0060285` (1 mention) - the report calls it "DOID"; DOID calls it **parietal foramina**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0005634` (2 mentions) - the report calls it "Subcellular:** nucleus"; GO calls it **nucleus**, and lists "cell nucleus" among its other names
- `NCBITaxon:9606` (1 mention) - the report calls it "Homo sapiens", "Taxonomy:** *Homo sapiens"; NCBITaxon calls it **Homo sapiens**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0018953` - called "MONDO", "parietal foramina"
- `NCBITaxon:9606` - called "Homo sapiens", "Taxonomy:** *Homo sapiens"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `GARD`, `MGI`.