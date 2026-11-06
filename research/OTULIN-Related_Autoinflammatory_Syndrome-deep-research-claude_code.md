---
provider: claude_code
model: claude-haiku-5-5, claude-opus-4-8, claude-opus-5-5
cached: false
start_time: '2026-11-01T04:37:26.117369'
end_time: '2026-11-01T04:47:52.461436'
duration_seconds: 626.34
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: OTULIN-Related Autoinflammatory Syndrome
  mondo_id: MONDO:0014912
  category: Mendelian
  causal_genes: OTULIN
  omim_id: OMIM:617099
  synonyms: AIPDS; ORAS; otulin deficiency; otulipenia
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
  - claude-opus-4-8
  - claude-opus-5-5
  web_search_requests: 1
  num_turns: 45
  total_cost_usd: 3.7867626000000003
  session_id: 2ccff955-20d8-5bb4-8e86-b52d55e2a947
  stop_reason: end_turn
  permission_denials: 6
  denied_tools:
  - Bash
  assistant_text_blocks: 9
citation_count: 4
reference_validation:
  total_references: 34
  verified: 34
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 34
  on_topic: 22
  validator_version: 0.4.0
term_validation:
  total_terms: 99
  verified: 96
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 16
  labels_matching: 11
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: NCIT:C15620
    reported_labels:
    - antibiotic therapy
    - Haploinsufficiency-specific supportive care:** aggressive **antibiotic therapy
    ontology_label: Antibiotic Therapy
  labels_variant: 4
  unresolvable_prefixes:
  - OMIM
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** OTULIN-Related Autoinflammatory Syndrome
- **MONDO ID:** MONDO:0014912 (if available)
- **Causal gene(s):** OTULIN
- **OMIM:** OMIM:617099
- **Synonyms:** AIPDS; ORAS; otulin deficiency; otulipenia
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **OTULIN-Related Autoinflammatory Syndrome** covering all of the
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

Checking the existing OTULIN entry in the repo, then I'll look up the primary literature.

The existing entry is only a skeleton, so the report has to come from the primary literature. Next I'll pull the abstracts from PubMed.

I have the candidate paper list. Next, the abstracts of the clinical and mechanistic papers, so the quotes I give are exact.

The fetch tool only returns short excerpts, so I'll download the abstracts directly to get exact wording.

Direct download needs approval, so I'll collect several short exact quotes per paper instead.

I've got the founding case series. Now checking identifiers (Orphanet, ClinGen, GeneReviews) and the haploinsufficiency papers.

Looking up ontology terms in the local caches one at a time.

# OTULIN-Related Autoinflammatory Syndrome (ORAS / otulipenia): research report

**Target:** MONDO:0014912 · OMIM:617099 · causal gene **OTULIN** (HGNC:25118, formerly FAM105B, 5p15.2)
**Prepared:** 2026-11-01

---

## How this report was made, and its limits

- **Where the facts come from.**
  - PubMed records via E-utilities.
  - Europe PMC records.
  - Full text where it is open access: PMC12309049, PMC5002269, PMC5018768 and PMC9233084.
  - The MONDO record on OLS, HGNC REST, and the ClinGen gene page.
- **Quotes.** My fetch tool only returns quotes of up to 125 characters. Every snippet below was returned as an exact excerpt, but treat each as a lead. Before using one as dismech evidence, run `just fetch-reference PMID:<id>` and then `just count-verified-snippets`. None of these PMIDs is in `references_cache/` yet.
- **Ontology IDs.** Every HP, GO, CL, UBERON and NCIT ID below was read from the committed `cache/*/terms.csv` files. HGNC:25118 comes from HGNC REST. IDs marked **(not looked up)** must be checked before they are bound.
- **No abstract was available for:**
  - PMID:30796585 (Nabavi 2019)
  - PMID:38578307 (Batlle-Masó 2024)
  - PMID:40795218 (Unal 2025)

  Facts attributed to these come from secondary tables and are marked as such.
- **The existing KB entry is a skeleton.** `kb/disorders/OTULIN-Related_Autoinflammatory_Syndrome.yaml` has one pathophysiology node, one phenotype, and no evidence.

---

## 1. Disease information

**Overview.** ORAS is a rare autoinflammatory disease caused by **biallelic loss-of-function variants in OTULIN**. Onset is usually in the neonatal period or early infancy. The main features are:
- recurrent fever
- neutrophilic dermatosis and panniculitis
- diarrhoea
- arthritis
- failure to thrive
- in some patients, lipodystrophy

OTULIN is the only deubiquitinase that specifically cleaves **Met1-linked (linear) polyubiquitin**, which is made by LUBAC (HOIP/RNF31, HOIL-1/RBCK1 and SHARPIN). When OTULIN is missing, linear ubiquitin builds up and TNF-driven NF-κB signalling and cell death become dysregulated.

Two groups described it independently in 2016:
- **Damgaard et al. 2016** (PMID:27523608): *"A homozygous hypomorphic mutation in human OTULIN causes a potentially fatal autoinflammatory condition"*.
- **Zhou et al. 2016** (PMID:27559085): *"an autoinflammatory disease caused by loss-of-function mutations in OTULIN (FAM105B)"*.

**An important scope point.** Three further OTULIN-linked presentations have since been described:
- **Heterozygous OTULIN haploinsufficiency** (Spaan 2022, PMID:35587511). This causes episodic necrosis of the skin and lungs, often triggered by *S. aureus*. It is not spontaneous systemic autoinflammation.
- **Heterozygous dominant-negative variants** causing typical ORAS:
  - p.Cys129Ser (Davidson 2024, PMID:38630025)
  - p.Arg306Gln (Takeda 2024, PMID:38652464)
- **Homozygous p.Arg57Cys** causing isolated pyoderma gangrenosum (Swaminathan 2026, PMID:42297973).

MONDO:0014912 and OMIM:617099 are the **autosomal recessive** entity. How to handle the dominant-negative and haploinsufficiency forms (subtypes, or a separate entry) is a lump/split decision for the curator (see section 9).

**Identifiers** (from the MONDO xrefs on OLS):

| Resource | ID |
|---|---|
| MONDO | MONDO:0014912, "autoinflammation, panniculitis, and dermatosis syndrome, autosomal recessive" |
| OMIM (phenotype) | 617099 (AIPDS) |
| OMIM (gene) | 615712 (OTULIN) |
| Orphanet | ORPHA:500062, "Infantile-onset periodic fever-panniculitis-dermatosis syndrome" |
| UMLS / MedGen | C4310614 / 934581 |
| SNOMED CT | 765435009 |
| GARD | 0013198 |
| DOID | 0080163 |
| ICD-10 / ICD-11 / MeSH | No xref in MONDO. Not found. |

**Synonyms:** AIPDS; ORAS; OTULIN deficiency; otulipenia; OTULIN-related autoinflammatory syndrome.

**Kind of data.** Almost all of it comes from case reports and small case series, about 15–20 biallelic or dominant-negative patients in total. There are no registries or EHR cohorts.

---

## 2. Etiology

**Primary cause.**
- **Classical ORAS:** germline biallelic LoF/hypomorphic OTULIN variants, autosomal recessive.
- **Dominant-negative ORAS:** monoallelic catalytic-dead or catalytically attenuated variants. These are dominant.

**Genetic risk factors**
- **Consanguinity.** Nearly every recessive family reported is consanguineous. These include Pakistani, Turkish, Arab, Iranian and Moroccan families (PMID:27559085, PMID:27523608, PMID:40734169, PMID:38914362).
- **Haploinsufficiency is a separate susceptibility state.** Spaan 2022 (PMID:35587511): *"We describe patients with haploinsufficiency for the linear deubiquitinase OTULIN, encoded by a gene on chromosome 5p."* The same paper: *"The disorder is phenocopied in patients with the 5p- (Cri-du-Chat) chromosomal deletion syndrome."*

**Environmental and infectious triggers.** These matter mainly for haploinsufficiency:
- *Staphylococcus aureus* α-toxin (PMID:35587511): *"Patients suffer from episodes of life-threatening necrosis, typically triggered by S. aureus infection."*
- A wider set of triggers (van der Linden 2025, PMID:41293556): *"previously underappreciated triggers, including mechanical or iatrogenic traumas"* and *"pseudomonal or clostridial infections"*.
- A post-surgical presentation (PMID:40084498).

**Protective factors.** Naturally acquired anti-α-toxin antibodies (PMID:35587511): *"Naturally elicited antibodies against α-toxin contribute to incomplete clinical penetrance."* No protective genetic modifiers have been identified.

**Gene–environment interaction.** In haploinsufficient carriers, disease appears only after a trigger (bacterial toxin, trauma or surgery) acts on non-haematopoietic cells that have reduced OTULIN dosage (PMID:35587511, PMID:41293556). In an Otulin+/- mouse, LPS challenge caused hyperinflammation (Staels 2024, PMID:38827742): *"We observed a hyperinflammatory signature in LPS-provoked"*.

---

## 3. Phenotypes

The frequencies come from the pooled 13-patient table in AlSaleem 2025 (PMID:40734169, PMC12309049, Table 2): 3 new patients plus 10 from the literature. Some denominators in that table are 11, not 13, so treat the percentages as approximate.

| Phenotype | HPO (from cache) | Frequency (n≈13) | Onset / course | Key source |
|---|---|---|---|---|
| Recurrent fever | HP:0001954 Recurrent fever | 100% | Neonatal to infancy; episodic or persistent | PMID:27559085 |
| Panniculitis (neutrophilic, septal or lobular) | HP:0012490 Panniculitis | Nodular rash 72% | Infancy; relapsing | PMID:27559085, 35170849 |
| Neutrophilic dermatosis / pustular or erythematous rash | HP:0031234 Neutrophilic infiltration of the skin; HP:0000988 Skin rash; HP:0010783 Erythema | Cutaneous involvement 100% | Infancy | PMID:27559085 |
| Skin abscesses (sterile) | HP:0031292 Cutaneous abscess | 54% | Childhood; "atypical ORAS" | PMID:35170849, 40734169 |
| Splenic abscesses | HP:0025059 Splenic abscess | All 3 AlSaleem patients | Childhood | PMID:40734169 |
| Lung involvement or abscess | HP:0025044 Lung abscess; HP:0002090 Pneumonia | 36% | Variable | PMID:40734169, 35587511 |
| Failure to thrive | HP:0001508 Failure to thrive | 82% | Infancy; reversible with anti-TNF | PMID:27559085 |
| Lipodystrophy | HP:0009125 Lipodystrophy | 45% | Progressive after panniculitis | PMID:27559085 |
| Diarrhoea / GI inflammation | HP:0002014 Diarrhea; HP:0002027 Abdominal pain; HP:0002013 Vomiting | GI 72% | Episodic | PMID:35170849, 27523608 |
| Arthritis / arthralgia | HP:0001369 Arthritis; HP:0002829 Arthralgia | Musculoskeletal 45% | Episodic | PMID:35170849 |
| Lymphadenopathy, hepatosplenomegaly | HP:0002716; HP:0001433 | Several case reports | — | PMID:27559085, 40734169 |
| Hepatic steatosis progressing to steatohepatitis | HP:0001397 Hepatic steatosis | 1 patient documented | 10–13 months | PMID:32231246 |
| Recurrent infections | — | 54% | — | PMID:40734169 |
| Premature birth | HP:0001622 | 3 of 3 in the Damgaard family; 1 of 3 in Zhou | Birth | PMID:27523608, 27559085 |
| Sialadenitis / parotitis | HP:0031281 | 1 patient | During a flare | PMID:27559085 |
| Developmental delay, seizures | HP:0001263; HP:0001250 | 1 patient (Zhou patient 3; possibly related to treatment or encephalitis) | — | PMID:27559085 |
| Pyoderma gangrenosum (R57C only) | HP:0025452 | 3 of 3 R57C patients | — | PMID:42297973 |
| Skin and lung necrosis (haploinsufficiency) | HP:0200042 Skin ulcer; HP:0100658 Cellulitis | about 30% penetrance in carriers | Adolescence, after a trigger | PMID:35587511 |

**Laboratory phenotypes**

| Finding | HPO | Frequency | Detail |
|---|---|---|---|
| Leukocytosis / neutrophilia | Not cached (HP:0001974 Leukocytosis, HP:0011897 Neutrophilia: **not looked up**) | 100% | WBC 56–64 ×10⁹/L in two AlSaleem patients |
| Raised CRP / ESR | HP:0011227; HP:0003565 | 100% | CRP up to 300 mg/L |
| Thrombocytosis | HP:0001894 | Reported | Platelets above 1,100 ×10⁹/L |
| Hypergammaglobulinaemia, autoantibodies | HP:0003493 Antinuclear antibody positivity | Damgaard family | — |
| Cytokines | — | — | Raised IL-1β, IL-6, IL-12, IL-18, IFN-γ and TNF in patient blood or monocytes (PMID:27559085) |

Supporting quotes:
- PMID:27559085: *"Patients presented with neonatal-onset fever, neutrophilic dermatitis/panniculitis, and failure to thrive"*.
- PMID:35170849: classical ORAS is *"characterized by fever, panniculitis, diarrhea, and arthritis."*
- PMID:32231246: *"In an ORAS patient, OTULIN deficiency caused spontaneous and progressive steatotic liver disease at 10-13 months of age."*

**Quality of life.** No EQ-5D, SF-36 or other formal instruments have been reported. Failure to thrive, chronic inflammation and the burden of immunosuppression dominate. Growth normalised on anti-TNF in Zhou patient 1 and AlSaleem patient I.

---

## 4. Genetic and molecular information

**Gene:** OTULIN (HGNC:25118; Entrez 90268; UniProt Q96BN8; Ensembl ENSG00000154124; 5p15.2). The protein has an N-terminal PIM (PUB-interacting motif), which binds the HOIP PUB domain, and a C-terminal OTU catalytic domain (catalytic Cys129).

**ClinGen.** The gene–disease validity page (Monogenic Autoinflammatory Disease GCEP) shows **Definitive, autosomal recessive**, for MONDO:0014912, dated 2026-05-19. No dosage-sensitivity classification is listed. No `CGGV:` record is cached locally. Run `just fetch-reference` on the assertion ID before recording `gene_disease_validity`.

**Reported pathogenic variants** (NM_138348; zygosity as reported)

| Variant | Zygosity / mode | Ancestry | Functional effect | Source |
|---|---|---|---|---|
| c.815T>C p.Leu272Pro | Homozygous, AR | Pakistani, consanguineous (3 affected; 2 died) | Unstable; 1,000–10,000× less active on M1 chains | PMID:27523608, 27559085 |
| c.731A>G p.Tyr

# Research Report: OTULIN-Related Autoinflammatory Syndrome (ORAS)

**Causal gene:** *OTULIN* (OTU deubiquitinase with linear linkage specificity; formerly *FAM105B*; alias *gumby*), HGNC:25118, chromosome **5p15.2**, UniProt **Q96BN8**, Entrez Gene 90268, Ensembl ENSG00000154124.
**MONDO:** MONDO:0014912 · **OMIM (phenotype):** 617099 · **OMIM (gene):** 615712 · **Orphanet:** ORPHA:500062 · **UMLS:** C4310614 · **MedGen:** 934581 · **GARD:** 0013198 · **DOID:** 0080163 · **SNOMED CT:** 765435009

> **Scope note / anti-confusion check.** This report concerns the autoinflammatory disease caused by biallelic (and, more recently, monoallelic) variants in **OTULIN**, the Met1(linear)-specific deubiquitinase. It is distinct from the clinically overlapping "relopathies" caused by *RBCK1*/*RNF31* (HOIL-1/HOIP, LUBAC components; a different OMIM gene set) and from *RIPK1* deficiency. All claims below were taken from primary literature retrieved during this session (PubMed/EuropePMC, 2013–2026), and source quotes are flagged as abstract- or full-text-derived. **Important terminology caveat:** two mechanistically different OTULIN diseases now exist — recessive **loss-of-function ORAS/otulipenia** and dominant **OTULIN haploinsufficiency** — and a subset of dominant-negative heterozygous presentations. These must not be conflated in a KB entry (see §4 and §6).

---

## 1. Disease Information

**Overview.** OTULIN-Related Autoinflammatory Syndrome (ORAS), also called **otulipenia** or **autoinflammation, panniculitis, and dermatosis syndrome, autosomal recessive (AIPDS)**, is a monogenic systemic autoinflammatory disease. The classical recessive form presents in the **neonatal period or early infancy** with recurrent fever, neutrophilic dermatitis/panniculitis, lipodystrophy, diarrhea, arthritis/arthralgia, and failure to thrive, driven by dysregulated NF-κB signalling and excess M1(linear)-linked polyubiquitin. It was described essentially simultaneously in 2016 by two groups.

- Zhou et al. (PNAS 2016, **PMID:27559085**): *"Biallelic hypomorphic mutations in a linear deubiquitinase define otulipenia, an early-onset autoinflammatory disease."* Abstract: *"Patients presented with neonatal-onset fever, neutrophilic dermatitis/panniculitis, and failure to thrive"* (abstract-derived).
- Damgaard et al. (Cell 2016, **PMID:27523608**): *"A homozygous hypomorphic mutation in human OTULIN causes a potentially fatal autoinflammatory condition"* termed OTULIN-related autoinflammatory syndrome (ORAS) (full-text-derived).

**Synonyms / alternative names:** otulipenia; ORAS; OTULIN deficiency; AIPDS / AIPDSB; "autoinflammation, panniculitis, and dermatosis syndrome, autosomal recessive"; "Infantile-onset periodic fever–panniculitis–dermatosis syndrome" (Orphanet preferred label). The condition belongs to the **"relopathies"** / "ubiquitin-related autoinflammatory diseases" group (Steiner, Curr Rheumatol Rep 2018, PMID:29846841; Aksentijevich & Zhou, Front Immunol 2017, PMID:28469620).

**Information source.** Aggregated from disease-level resources (OMIM, Orphanet, ClinGen) and from individual patient case reports/series (PMID:27559085, 27523608, 30804083, 30796585, 35170849, 38914362, 40734169, 41293556). This is a rare disease documented through small case series, not EHR-scale cohorts.

---

## 2. Etiology

**Primary cause — genetic.** ORAS is a monogenic disease caused by variants in *OTULIN*. Two genetic/inheritance architectures are now recognised:

1. **Recessive loss-of-function (classical otulipenia/ORAS):** biallelic hypomorphic or amorphic variants → reduced OTULIN catalytic activity/stability → accumulation of M1-linked polyubiquitin and spontaneous NF-κB activation. *"an autoinflammatory disease caused by loss-of-function mutations in OTULIN (FAM105B)"* (PMID:27559085, abstract).

2. **Dominant OTULIN haploinsufficiency:** heterozygous deleterious variants (or 5p chromosomal loss) causing a *different*, infection/trauma-triggered necrosis syndrome (Spaan et al., Science 2022, **PMID:35587511**).

3. **Dominant-negative heterozygous ORAS:** rare heterozygous variants (e.g. p.Cys129Ser, p.Arg306Gln) that poison the pathway and produce a spontaneous-inflammation ORAS phenotype despite one normal allele (Davidson, PMID:38630025; Takeda, PMID:38652464).

**Genetic risk factors.** The disease-causing variant *is* the cause; **consanguinity** is a major risk factor for the recessive form (multiple consanguineous Arab, Turkish, Pakistani, Iranian, Moroccan families — PMID:27559085, 40734169, 38914362). No separate susceptibility loci or modifier genes are established, though background LUBAC-pathway genes (*RNF31*/HOIP [hgnc:16031], *RBCK1*/HOIL-1, *SHARPIN* [hgnc:25321]) are mechanistically related.

**Environmental risk / trigger factors.** Central to the **haploinsufficiency** form: *"episodes of life-threatening necrosis, typically triggered by S. aureus infection"* (PMID:35587511, abstract). Broader triggers were later reported: *"previously underappreciated triggers, including mechanical or iatrogenic traumas"* and *"pseudomonal or clostridial infections"* (van der Linden, J Hum Immun 2025, **PMID:41293556**, abstract). Surgery/wound healing is a documented trigger (Nguyen, ACR Open Rheumatol 2025, PMID:40084498, post-operative necrosis). Staels (Front Immunol 2024, PMID:38827742): *"OTULIN haploinsufficiency predisposes to environmentally directed inflammation."*

**Protective factors.** For the α-toxin/staphylococcal haploinsufficiency phenotype, **naturally acquired anti-α-toxin antibodies** are protective and explain incomplete penetrance: *"Naturally elicited antibodies against α-toxin contribute to incomplete clinical penetrance"* (PMID:35587511, abstract). No dietary/lifestyle protective factors are established.

**Gene–environment interaction.** The haploinsufficiency phenotype is the clearest G×E example in the group: a germline heterozygous OTULIN defect is clinically silent until an environmental insult (S. aureus α-toxin, trauma, surgery) precipitates tissue necrosis, and anti-toxin humoral immunity modifies penetrance.

---

## 3. Phenotypes

Frequencies below are pooled from a 13-patient table (3 new + 10 literature) in AlSaleem et al. (Pediatr Rheumatol 2025, **PMID:40734169**, full-text, Table 2) for the recessive form, supplemented by the founding series. **Interpret pooled percentages cautiously** — total documented classical cases number only in the low dozens.

### Classical recessive ORAS (neonatal/infantile autoinflammation)

| Phenotype | Type | Frequency (pooled) | HPO suggestion |
|---|---|---|---|
| Recurrent fever / fever | Symptom | 13/13 (100%) | **HP:0001954** Recurrent fever; HP:0001945 Fever |
| Neutrophilic dermatitis / skin rash | Clinical sign | ~100% cutaneous | **HP:0000988** Skin rash; **HP:0031234** Neutrophilic infiltration of the skin; HP:0010783 Erythema |
| Panniculitis (often septal, neutrophilic) | Clinical sign | high (nodular rash 72%) | **HP:0012490** Panniculitis |
| Lipodystrophy | Physical manifestation | 5/11 (~45%) | **HP:0009125** Lipodystrophy |
| Failure to thrive | Physical manifestation | 9/11 (82%) | **HP:0001508** Failure to thrive |
| Diarrhea / GI involvement | Symptom | 8/11 (72%) | **HP:0002014** Diarrhea |
| Arthritis / arthralgia | Clinical sign | ~45% musculoskeletal | **HP:0001369** Arthritis; HP:0002829 Arthralgia |
| Leukocytosis / neutrophilia | Lab abnormality | 11/11 (100%) | HP:0001974 Leukocytosis; HP:0011897 Neutrophilia |
| Elevated CRP / ESR | Lab abnormality | 11/11 (100%) | **HP:0011227** Elevated CRP; **HP:0003565** Elevated ESR |
| Thrombocytosis | Lab abnormality | common (plt >1000×10⁹/L in acute cases) | HP:0001894 Thrombocytosis |
| Lymphadenopathy | Clinical sign | reported | HP:0002716 Lymphadenopathy |
| Hepatosplenomegaly / splenomegaly | Clinical sign | reported | HP:0001433 Hepatosplenomegaly; HP:0001744 Splenomegaly |
| Sterile abscesses (skin, splenic, pulmonary) | Clinical sign | abscesses 54% (AlSaleem series) | HP:0031292 Cutaneous abscess; HP:0025059 Splenic abscess; HP:0025044 Lung abscess |
| Recurrent infections | Clinical sign | 6/11 (54%) | HP:0002719 Recurrent infections |
| Autoantibodies (ANA, dsDNA) | Lab abnormality | reported (Damgaard) | HP:0003493 Antinuclear antibody positivity |
| Progressive steatotic liver disease | Physical manifestation | ≥1 patient (10–13 mo) | HP:0001397 Hepatic steatosis |

Quotes: *"Patients presented with neonatal-onset fever, neutrophilic dermatitis/panniculitis, and failure to thrive"* (PMID:27559085); *"fever, panniculitis, diarrhea, and arthritis"* (Zinngrebe, PMID:35170849). Liver: *"OTULIN deficiency caused spontaneous and progressive steatotic liver disease at 10-13 months of age"* (Damgaard, Cell Death Differ 2020, **PMID:32231246**).

**Atypical / late-onset recessive:** Zinngrebe (PMID:35170849) reported a 7-year-old with *"a life-threatening autoinflammatory episode with sterile abscess formation"* (compound-het p.M86I/p.W167S) and proposed splitting ORAS into **classical** and **atypical (fulminant late-onset)** forms. AlSaleem's 3 Arab patients (p.Val185Phe) also had **non-neonatal onset** (12 mo, 24 mo, 4 y): *"none of our patients had an early or neonatal onset."*

### OTULIN haploinsufficiency (distinct phenotype)

| Phenotype | Type | HPO suggestion |
|---|---|---|
| Life-threatening skin necrosis | Clinical sign | HP:0200042 Skin ulcer; HP:0100659 (necrosis) |
| Pulmonary necrosis / necrotizing pneumonia | Clinical sign | HP:0002090 Pneumonia; HP:0025044 Lung abscess |
| Severe staphylococcal (±Pseudomonas/clostridial) disease | Clinical sign | HP:0002719 Recurrent infections |
| Fasciitis / necrotizing soft-tissue infection | Clinical sign | — (HP:0100536 inflammation) |
| Onset usually **adolescence**, trauma/surgery-triggered | Temporal | — |

*"Patients suffer from episodes of life-threatening necrosis, typically triggered by S. aureus infection"* (PMID:35587511). *"six unrelated patients who carry rare, predicted deleterious variants"* with skin/lung necrosis (PMID:41293556).

### Isolated pyoderma gangrenosum (newest allelic presentation)

Swaminathan et al. (Nat Immunol 2026, **PMID:42297973**): three patients from two kindreds with **homozygous p.R57C**, an isolated PG phenotype. *"OTULIN-R57C is catalytically active but is unable to bind the linear ubiquitin assembly complex"*; *"Patient monocytes show heightened expression of IL1B"* (abstract). HPO: **HP:0025452** Pyoderma gangrenosum.

**Quality-of-life impact.** Not formally quantified with EQ-5D/SF-36 in the literature. Qualitatively severe: classical cases require chronic biologic therapy, cause growth failure and lipodystrophy; untreated disease is potentially fatal; haploinsufficiency carries risk of life-threatening necrotic episodes.

---

## 4. Genetic / Molecular Information

**Causal gene.** *OTULIN* (HGNC:25118, 5p15.2). Encodes a 352-aa OTU-family deubiquitinase that is **exquisitely specific for Met1 (linear/M1) polyubiquitin** (Keusekotten, Cell 2013, **PMID:23746843**: *"specifically hydrolyzing Met1-linked polyubiquitin"*). GO suggestions: **GO:0101005** deubiquitinase activity; **GO:0004843** cysteine-type deubiquitinase activity; **GO:0016579** protein deubiquitination (with M1/linear specificity noted in `preferred_term`); **GO:0097039** protein linear polyubiquitination (the substrate it reverses).

### Pathogenic variants — recessive ORAS (biallelic)

| Variant (protein) | cDNA | Family/ancestry | Zygosity | Ref |
|---|---|---|---|---|
| **p.Leu272Pro** | c.815T>C | Pakistani (3 sibs) | Homozygous | PMID:27523608, 27559085 |
| **p.Tyr244Cys** | c.731A>G | Turkish | Homozygous | PMID:27559085 |
| **p.Gly174Aspfs*2** | c.517delC (frameshift) | Turkish | Homozygous | PMID:27559085 |
| **p.Gly281Arg** | — | Arab | Homozygous | PMID:30804083 |
| **p.Trp199Arg** | c.595T>A | Moroccan | Homozygous | PMID:38914362 |
| **p.Val185Phe** | c.553G>T | Arab (3 families) | Homozygous | PMID:40734169 |
| **p.Met86Ile / p.Trp167Ser** | c.258G>A / c.500G>C | Greek | Compound het (atypical) | PMID:35170849 |
| splice **c.864+2T>C** | — | Iranian | Homozygous | (literature table, PMID:40734169) |

Variant classes: predominantly **missense hypomorphs**, one **frameshift**, one **splice-site**. Functional consequence = **loss of function / hypomorph**: p.L272P is *"less stable and 1,000–10,000 times less active against M1-linked di- and tetraubiquitin"* (PMID:27523608, full text); mutant OTULIN *"had decreased enzyme activity relative to cells transfected with WT OTULIN"* (PMID:27559085). All founding variants were **absent from ExAC** and ethnically matched controls.

### Variants — dominant OTULIN haploinsufficiency

Spaan (PMID:35587511): six heterozygous variants in 7 patients / 6 kindreds — **p.Asp246Val, p.Glu95X (nonsense), p.Asp268TfsX5 (frameshift), p.Asn341Asp, p.Pro254Ser, p.Arg263Gln**. Alleles were hypomorphic/amorphic (<25% WT NF-κB inhibition); cumulative population frequency of such alleles ≈ **6×10⁻⁵**; constraint metrics LoFtool 0.115, CoNeS −0.78 (intolerant to haploinsufficiency). The disorder is **phenocopied by the 5p−/Cri-du-Chat deletion** when it removes one *OTULIN* copy. Additional haploinsufficiency variant: **p.Arg263Trp** (post-surgical necrosis; PMID:40084498).

### Dominant-negative heterozygous ORAS

- **p.Cys129Ser** — abolishes DUB activity without destabilising protein; *"the first dominant-negative mutation linked to ORAS"*; *"Altered ubiquitination of LUBAC inhibits its recruitment to the TNF receptor signaling complex"* (Davidson, J Exp Med 2024, **PMID:38630025**).
- **p.Arg306Gln** (de novo) + p.Pro152Leu — *"the de novo p.R306Q variant exhibits attenuated deubiquitination activity"* and acts dominant-negatively (Takeda, J Exp Med 2024, **PMID:38652464**).
- **p.R57C** — catalytically intact but LUBAC-binding-deficient (PUB-interacting motif); isolated PG (PMID:42297973).

**Modifier genes / epigenetics / chromosomal.** No modifier genes established. The main **chromosomal abnormality** relevant is the **5p terminal deletion (Cri-du-Chat)** acting as a haploinsufficiency phenocopy (PMID:35587511). No disease-specific epigenetic mechanism reported.

---

## 5. Environmental Information

- **Infectious triggers:** *Staphylococcus aureus* (α-toxin) is the paradigmatic trigger of haploinsufficiency necrosis (**NCBITaxon:1280**); also *Pseudomonas* and *Clostridium* species (PMID:41293556). A tubercular cutaneous abscess has been reported in a haploinsufficient infant (Ks, Indian J Pediatr 2025, PMID:40711650).
- **Physical/iatrogenic:** mechanical trauma and **surgery/wound healing** precipitate necrotic episodes (PMID:41293556; PMID:40084498 "Failure to Close").
- **Lifestyle factors:** none established.
- For classical **recessive** ORAS, inflammation is largely **spontaneous/constitutive** rather than environmentally triggered, though LPS amplifies cytokine output ex vivo.

---

## 6. Mechanism / Pathophysiology

### Causal chain (recessive loss-of-function ORAS)

1. **Biallelic hypomorphic OTULIN variant** → reduced OTULIN catalytic activity/stability (*leads to*) failure to hydrolyse Met1-linked polyubiquitin. (Demonstrated: PMID:27523608, 27559085.)
2. **Loss of M1-chain editing** → **accumulation of M1-linked polyubiquitin**, especially on/around LUBAC (HOIP/HOIL-1/SHARPIN) signalling complexes. *"accumulation of M1-linked polyubiquitin and spontaneous NF-κB activation in myeloid cells"* (PMID:27523608). (Demonstrated.)
3. **Spontaneous, ligand-independent activation of canonical NF-κB** in **myeloid cells (monocytes/macrophages)** → constitutive transcription of proinflammatory cytokines. (*results in*) (Demonstrated in patient monocytes and mouse BMDMs.)
4. **Overproduction of TNF, IL-1β, IL-6, IL-12/IL-18, IFN-γ** → systemic autoinflammation (fever, panniculitis, FTT). *"higher IL-1β, IL-6, IL-12, IL-18, and IFN-γ"* (PMID:27559085, full text). (Demonstrated.)
5. **Branch A — cell-type-specific LUBAC degradation:** in **B and T cells**, OTULIN loss paradoxically causes *"downregulation of M1-polyubiquitin signaling by degradation of LUBAC"* (HOIP and SHARPIN reduced, proteasome-dependent) (PMID:27523608; Damgaard EMBO Mol Med 2019, **PMID:30804083**: *"loss of OTULIN in patient-derived fibroblasts leads to a reduction in LUBAC levels"*). (Demonstrated.)
6. **Branch B — sensitisation to TNF-induced cell death:** *"both patient-derived fibroblasts and OTULIN-deficient monocytes are sensitised to certain types of TNF-induced death"*; *"apoptotic cells are evident in ORAS patient skin lesions"* (PMID:30804083). Cell death (apoptosis/necroptosis) further amplifies inflammation. (Demonstrated.)
7. **Branch C — hepatic:** hepatocyte OTULIN loss → aberrant **mTOR activation** and FADD/RIPK1-kinase-dependent hepatocyte apoptosis → steatosis→steatohepatitis→fibrosis→HCC (mouse + 1 patient). *"steatohepatitis in OTULIN-deficient livers is associated with aberrant mTOR activation"* and *"inhibition of mTOR by rapamycin...significantly reduces the liver pathology"* (PMID:32231246); *"OTULIN Prevents Liver Inflammation and Hepatocellular Carcinoma by Inhibiting FADD- and RIPK1 Kinase-Mediated Hepatocyte Apoptosis"* (Verboom, Cell Rep 2020, **PMID:32075762**). (Model-organism + case.)
8. **Clinical manifestation:** recurrent fever, neutrophilic dermatosis/panniculitis, lipodystrophy, arthritis, diarrhea, FTT.

**Note the cell-type paradox (key mechanistic insight):** OTULIN loss is *not* uniformly pro- or anti-inflammatory — it increases M1-Ub/NF-κB in myeloid cells but degrades LUBAC in lymphocytes. *"OTULIN deficiency in ORAS causes cell type-specific LUBAC degradation, dysregulated TNF signalling and cell death"* (PMID:30804083).

### Causal chain (dominant haploinsufficiency necrosis)

1. Heterozygous OTULIN LOF (50% dosage) → *"accumulation of linear ubiquitin in dermal fibroblasts"* (**CL:0002551** fibroblast of dermis) (PMID:35587511).
2. → **OTULIN-dependent accumulation of caveolin-1 (CAV1, hgnc:1527)** high-MW K63-ubiquitinated complexes at the fibroblast surface.
3. → caveolin-1 facilitates **α-toxin binding and ADAM10 (hgnc:188) retention** at the surface → heightened susceptibility to *S. aureus* **α-toxin** cytotoxicity. *"facilitates the cytotoxic damage inflicted by the staphylococcal virulence factor α-toxin"* (PMID:35587511).
4. → trauma/infection trigger → **tissue necrosis of skin and lungs**; modified by anti-α-toxin antibody titres (penetrance ≈30%).

This is a **non-hematopoietic (stromal)** mechanism in humans — PBMCs and NF-κB signalling in blood cells were largely normal — contrasting with the hematopoietic-driven inflammation of mouse models (PMID:38827742).

### Mechanistic modules / pathways (for KB linking)

- **Molecular pathways:** canonical NF-κB (**GO:0007249**; dysregulated positive **GO:0043123**), TNF-mediated signalling (**GO:0033209**), mTOR/TORC1 (**GO:0038202**, **GO:0032006**), NLRP3 inflammasome assembly (**GO:0044546**), Wnt/angiogenesis (developmental *gumby* role, **GO:0001525**, **GO:0016055**; PMID:23708998).
- **Cellular processes:** inflammatory response (**GO:0006954**), extrinsic apoptosis (**GO:0097191**), necroptosis (**GO:0070266** / **GO:0097300**), TNF/IL-1β/IL-6 production (GO:0032640/0032611/0032635), neutrophil chemotaxis (**GO:0030593**). Doglio (Sci Immunol 2023, **PMID:38000038**): myeloid OTULIN loss *"couples RIPK3-dependent cell death to Nlrp3 inflammasome activation and IL-1β secretion."*
- **Protein dysfunction:** loss of OTU-domain M1-Ub hydrolase function; LUBAC (**GO:0071797** LUBAC complex) dysregulation (OTULIN normally restrains LUBAC autoubiquitination — Heger, Nature 2018, **PMID:29950720**; Lyu, Mol Cell 2026, PMID:42880249).
- **Cell types (CL):** monocyte **CL:0000576** / classical monocyte CL:0000860; macrophage **CL:0000235**; neutrophil **CL:0000775**; dermal fibroblast **CL:0002551**; keratinocyte **CL:0000312** (Schünke, Nat Commun 2021, PMID:34625557 — RIPK1-mediated keratinocyte necroptosis); hepatocyte **CL:0000182**; B cell CL:0000236; T cell CL:0000084.

---

## 7. Anatomical Structures Affected

- **Primary:** skin (**UBERON:0002097** skin of body; **UBERON:0002067** dermis), subcutaneous adipose tissue / panniculus (**UBERON:0002190**, **UBERON:0002072** hypodermis), joints, gastrointestinal tract (**UBERON:0000160** intestine).
- **Secondary / systemic:** liver (**UBERON:0002107**) — steatosis→HCC; lung (**UBERON:0002048**) — necrosis/abscess (haploinsufficiency); spleen (**UBERON:0002106**) — abscesses/splenomegaly; blood/bone marrow (**UBERON:0000178** / **UBERON:0002371**) — leukocytosis, thrombocytosis.
- **Body systems:** integumentary, musculoskeletal, digestive, hematologic/immune, hepatic, respiratory.
- **Subcellular:** cytoplasmic ubiquitin–proteasome/signalling machinery; plasma-membrane caveolae (caveolin-1) in the haploinsufficiency mechanism. GO cellular components: plasma membrane caveola, cytosol.
- **Lateralization:** systemic/bilateral; abscesses and necrotic lesions are focal/multifocal.

---

## 8. Temporal Development

- **Onset:** Classical recessive — **neonatal to early infancy** (first weeks of life; often premature birth, HP:0001622). Atypical/late-onset recessive — childhood (e.g. 7 y; or 1–4 y in the p.V185F families). Haploinsufficiency necrosis — typically **adolescence**, trigger-dependent.
- **Onset pattern:** recurrent/episodic flares of systemic inflammation (recessive); acute trigger-provoked necrotic crises (haploinsufficiency).
- **Progression:** without effective therapy, potentially **fatal** (septicaemia, multiorgan inflammation, renal failure, pulmonary edema — deaths at 16 mo and 5 y in the founding Pakistani family, PMID:27523608; a fatal Iranian splice-variant case). Chronic relapsing course with growth failure and lipodystrophy if untreated; liver disease can progress steatosis→fibrosis→HCC.
- **Remission:** treatment-induced remission achievable with anti-TNF/anti-IL-1 (recessive) and with HSCT (see §12). Haploinsufficiency episodes are acute and recurrent.
- **Critical window:** early diagnosis and TNF blockade (or definitive HSCT) before irreversible organ damage.

---

## 9. Inheritance and Population

- **Inheritance:** **Autosomal recessive** for classical ORAS/otulipenia (ClinGen Gene–Disease Validity: *OTULIN – AIPDS, AR, **Definitive**, Monogenic Autoinflammatory Disease GCEP, 2026-05-19*). **Autosomal dominant** for OTULIN haploinsufficiency and for the dominant-negative variants (p.C129S, p.R306Q).
- **Penetrance:** complete-to-high for biallelic LOF; **incomplete (~30%)** for haploinsufficiency, modified by anti-α-toxin antibodies (PMID:35587511: *"3 of 10"* ORAS-parent carriers had a milder phenotype).
- **Expressivity:** variable (classical vs atypical/fulminant; isolated PG).
- **Consanguinity:** major driver of recessive cases (Arab, Turkish, Pakistani, Iranian, Moroccan consanguineous families).
- **Carrier/allele frequency:** cumulative deleterious-allele frequency ≈ **6×10⁻⁵** (haploinsufficiency alleles; PMID:35587511).
- **Epidemiology:** **Orphanet prevalence "Not yet documented"**; **ultra-rare**, <50 classical patients reported worldwide. Orphanet notes "At least four cases" originally; literature now totals a few dozen across both forms. No reliable incidence/prevalence per 100,000 exists. PrevalenceClass suggestion: `NOT_YET_DOCUMENTED`; qualitative `ULTRA_RARE`.
- **Founder effects:** recurrent ancestry-specific homozygous variants reflect consanguinity rather than classic founder haplotypes. **Sex ratio:** no sex bias established (X-autosome: gene is autosomal). **Geographic:** cases concentrated in consanguineous populations of the Middle East, North Africa, South Asia, Turkey; haploinsufficiency cases more geographically dispersed.

---

## 10. Diagnostics

- **Laboratory (LOINC-codable):** persistently elevated **CRP** and **ESR**, **leukocytosis/neutrophilia**, **thrombocytosis**, elevated serum proinflammatory cytokines (TNF, IL-6, IL-18, IL-1β), hypergammaglobulinemia and autoantibodies (ANA/dsDNA) in some; negative microbial cultures during sterile flares. Research assay: **elevated free M1(linear)-linked polyubiquitin chains** in patient leukocytes (diagnostic hallmark; PMID:27523608).
- **Functional immunology:** increased basal/LPS-stimulated cytokine production by patient monocytes; reduced LUBAC (HOIP/SHARPIN) in lymphocytes; NF-κB reporter assays showing reduced inhibition by mutant OTULIN.
- **Histopathology:** neutrophilic dermatosis / septal or lobular **panniculitis**, sometimes with small/medium-vessel vasculitis; sterile abscesses.
- **Imaging:** CT for pulmonary/splenic/hepatic abscesses; characterises necrotic lesions in haploinsufficiency.
- **Genetic testing (diagnostic gold standard):** single-gene *OTULIN* sequencing, autoinflammatory **gene panels**, or **WES/WGS** (most founding cases found by exome). Chromosomal microarray/karyotype where a 5p deletion (Cri-du-Chat phenocopy) is suspected. GTR lists clinical *OTULIN* testing.
- **Clinical criteria:** no formal consensus diagnostic criteria; diagnosis = compatible autoinflammatory phenotype + biallelic (or relevant heterozygous) pathogenic *OTULIN* variant + supportive functional data. Screened at autoinflammatory-disease registries (Infevers *OTULIN* variant database).
- **Differential diagnosis:** other relopathies/LUBAC defects (HOIL-1/*RBCK1*, HOIP/*RNF31* deficiency), RIPK1 deficiency (PMID:31213653), DIRA (IL1RN), DITRA (IL36RN), CANDLE/PRAAS, Mevalonate kinase deficiency/HIDS, TRAPS, FMF, CINCA/NOMID, deficiency of ADA2, and (for necrosis form) primary necrotizing soft-tissue infection. Distinguishing feature: M1-polyubiquitin accumulation and *OTULIN* genotype.
- **Screening:** carrier/cascade testing in consanguineous families; prenatal/preimplantation testing feasible for known familial variants.

---

## 11. Outcome / Prognosis

- **Mortality:** historically high in untreated classical disease — e.g. two of three affected siblings in the founding family died (pneumococcal sepsis at 16 mo; systemic inflammation with ARF/pulmonary edema at age 5) before anti-TNF was available (PMID:27523608, full text); a homozygous splice-variant Iranian patient died. Haploinsufficiency necrosis is **life-threatening** during crises.
- **With treatment:** prognosis is substantially improved by **TNF inhibition** and transformed by **HSCT** (potentially curative for the hematopoietic-driven recessive disease). Patient V:2 (p.L272P) *"alive at age 11 with well-controlled disease"* on infliximab; HSCT gave *"complete resolution of inflammatory symptoms"* (PMID:30804083).
- **Morbidity:** growth failure/FTT, lipodystrophy, joint disease, recurrent abscesses, and (long-term) risk of hepatic fibrosis/HCC; necrotic tissue loss and post-surgical complications in haploinsufficiency.
- **Prognostic factors:** genotype (amorph vs hypomorph), time to diagnosis/treatment, organ involvement (liver, lung), anti-α-toxin antibody status (haploinsufficiency penetrance). No validated prognostic biomarker beyond inflammatory markers and M1-Ub load.

---

## 12. Treatment

Suggested NCIT terms in brackets; most pharmacotherapy uses generic action **NCIT:C15986 (Pharmacotherapy)** + a `therapeutic_agent`.

- **TNF inhibitors — mainstay of recessive ORAS.** *"treatment with anti-TNF neutralizing antibodies ameliorates inflammation in ORAS patients and rescues mouse phenotypes"* (PMID:27523608).
  - **Infliximab** [NCIT:C1789] — complete response in p.L272P patient (resolution within ~1 month; PMID:27559085).
  - **Adalimumab** [NCIT:C65216] — remission in the AlSaleem p.V185F patients (monotherapy maintenance; PMID:40734169).
  - **Etanercept** [NCIT:C2381] — partial response (p.G174fs; PMID:27559085). Therapeutic modality: `MONOCLONAL_ANTIBODY` (infliximab/adalimumab) vs soluble receptor (etanercept).
  - Fasciitis/skin necrosis in haploinsufficiency: *"excessive inflammation in OTULIN haploinsufficiency can be effectively treated by TNF inhibition"* (Arts, PMID:38129331); post-operative necrosis improved on glucocorticoids + infliximab (PMID:40084498).
- **IL-1 inhibition — variable.** **Anakinra** [NCIT:C38717] gave complete response in one Turkish patient (p.Y244C) but was ineffective in others; **canakinumab** [NCIT:C80971] precipitated macrophage activation syndrome in one patient (PMID:27559085). IL-1β blockade proposed for the PG phenotype (PMID:42297973).
- **Glucocorticoids** [NCIT:C2323 / prednisolone NCIT:C769, prednisone NCIT:C770] — control acute flares; used as bridge/adjunct.
- **Other immunomodulators:** methotrexate [NCIT:C642] (adjunct to infliximab), azathioprine (ineffective alone), ruxolitinib [NCIT:C77888] (JAK inhibitor, tried in a dominant case).
- **mTOR inhibition (mechanistic rationale, hepatic):** **rapamycin/sirolimus** [NCIT:C1212; CHEBI:9168] reduced liver pathology in OTULIN-deficient mice — a candidate for hepatic involvement, not yet standard clinical practice (PMID:32231246).
- **Definitive / curative:** **Allogeneic HSCT** [NCIT:C46089 / Hematopoietic Cell Transplantation NCIT:C15431] — complete resolution in a transplanted ORAS patient; rationale that *"haematopoietic cells are necessary for clinical manifestation of ORAS"* (PMID:30804083). (Note: one literature case failed HSCT and responded instead to etanercept — PMID:40734169 Table.)
- **Haploinsufficiency-specific supportive care:** aggressive **antibiotic therapy** [NCIT:C15620] for staphylococcal infection, surgical **debridement** [NCIT:C51682] of necrotic tissue, and proposed (investigational) **α-toxin-neutralizing monoclonal antibodies** ± steroids (PMID:35587511). ADAM10 inhibition / cyclodextrin protected cells in vitro only.
- **Genetic counseling** [NCIT:C15240] for families (AR recurrence risk, consanguinity).

**Treatment strategy:** distinguish the two diseases — recessive ORAS → cytokine blockade (TNF first-line) ± HSCT; haploinsufficiency → trigger avoidance, prompt anti-staphylococcal therapy, TNF blockade for the hyperinflammatory component. **Pharmacogenomics:** none established.

---

## 13. Prevention

- **Primary:** no population prevention; **genetic counseling and carrier/cascade screening** in consanguineous families; prenatal/preimplantation genetic diagnosis for known familial variants.
- **Secondary:** early genetic diagnosis in a neonate/infant with recurrent fever + neutrophilic panniculitis + FTT, enabling early anti-TNF before organ damage.
- **Tertiary:** chronic cytokine blockade to prevent flares; hepatic surveillance (steatosis→HCC risk); for haploinsufficiency — **trigger avoidance** (wound/surgical prophylaxis, prompt treatment of *S. aureus*), and antibody-mediated protection concepts.
- **Immunization:** no disease-specific vaccine; standard immunisation with attention to live-vaccine caution under biologics; anti-α-toxin vaccination is a theoretical research direction for haploinsufficiency.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** mechanistic/genetic models in **mouse** (*Mus musculus*, **NCBITaxon:10090**). The gene was first characterised in mouse as ***gumby*/*Fam105b*** (Rivkin et al., Nature 2013, PMID:23708998 — angiogenesis/*Otulin* developmental role). Human pathogen relevant to the haploinsufficiency form: *Staphylococcus aureus* (NCBITaxon:1280).
- **Orthologous gene:** mouse *Otulin* (Entrez 71753). Strong evolutionary conservation of the OTU domain and M1-Ub machinery (LUBAC/OTULIN axis conserved across vertebrates).
- **Natural animal disease:** no naturally occurring OTULIN autoinflammatory disease is catalogued in OMIA for companion animals/livestock (based on this literature review); disease knowledge in animals is from engineered models, not spontaneous disease.
- **Comparative pathology caveat:** mouse haploinsufficiency inflammation is **hematopoietic-driven**, whereas human haploinsufficiency necrosis is **non-hematopoietic/stromal** — an explicit human–model mismatch (PMID:38827742 vs 35587511), important for KB `HUMAN_MODEL_MISMATCH` annotation.
- **Zoonosis:** not applicable (the disease is genetic; the *trigger* S. aureus is a common commensal/pathogen, not a zoonotic transmission of the disease).

---

## 15. Model Organisms

- **Germline knockout mouse (*Otulin* LacZ / *gumby*):** homozygous loss is **embryonic lethal (~E12.5–E14)**, with angiogenesis/Wnt defects (PMID:23708998; PMID:27523608 full text). Models early developmental OTULIN function; not viable for inflammation study.
- **Catalytically inactive knock-in (*Otulin* C129A/gumby-type):** Heger et al. (Nature 2018, **PMID:29950720**) — *"Catalytically inactive OTULIN knock-in mice died midgestation from TNFR1- and RIPK1-kinase-dependent cell death"*; rescued by co-deletion of *Casp8*/*Ripk3*; elevated type I IFN. Establishes OTULIN restrains LUBAC and limits cell death/inflammation.
- **Conditional (Cre-lox) tissue-specific deletions** (key for dissecting cell-type contributions; PMID:27523608 full text):
  - **LysM-Cre (myeloid):** viable; splenomegaly/hepatomegaly, leukocytosis, elevated serum cytokines (TNF, IL-6, IL-1β, G-CSF), fibrosis, autoantibodies — **recapitulates systemic autoinflammation**.
  - **CD4-Cre (T cell) and MB1-Cre (B cell):** no overt inflammatory phenotype → inflammation is myeloid-driven.
  - **CreERT2 (tamoxifen-inducible, bone-marrow chimera):** rapid wasting, neutrophilia, high TNF/IL-6/G-CSF; anti-TNF prevents wasting — supports anti-TNF efficacy.
  - **Epidermis-specific (keratinocyte):** skin inflammation via TNFR1/RIPK1-kinase-dependent **necroptosis** (Schünke, Nat Commun 2021, **PMID:34625557**).
  - **Hepatocyte-specific:** steatohepatitis→fibrosis→HCC, FADD/RIPK1-dependent, mTOR-associated (PMID:32231246, 32075762).
  - **Myeloid (RIPK3/Nlrp3 axis):** PMID:38000038.
- **Haploinsufficient mouse (*Otulin*+/−):** LPS-provoked hyperinflammation driven by CD64+ monocytes/macrophages — but **hematopoietic-driven, unlike human** (PMID:38827742) — a documented translational limitation.
- **Patient iPSC model:** iPSC line from a patient homozygous for **L272P** (Chen, Stem Cell Res 2020, PMID:32721894; line NIHTVBi014-A) — a human cellular NAM for mechanism/drug studies.
- **Resources:** MGI (mouse *Otulin*), IMPC/KOMP (knockout alleles), Cellosaurus (iPSC line).
- **Model recapitulation summary:** tissue-specific conditional KOs faithfully reproduce organ-specific disease (skin, liver, myeloid inflammation) and validate TNF/RIPK1 as drivers; whole-body null is lethal (developmental confounder); haploinsufficiency mouse diverges from the human stromal/α-toxin mechanism.

---

## Key Evidence Citations (PMIDs)

| PMID | Role | Evidence type |
|---|---|---|
| 27559085 | Founding description, otulipenia, variants L272P/Y244C/G174fs | HUMAN_CLINICAL |
| 27523608 | Founding ORAS, L272P, anti-TNF, LysM-Cre mouse | HUMAN_CLINICAL + MODEL_ORGANISM (split) |
| 23746843 | OTULIN = Met1-specific DUB, structure, LUBAC | IN_VITRO |
| 23708998 | *gumby*/Fam105b, angiogenesis, mouse | MODEL_ORGANISM |
| 30804083 | Cell-type-specific LUBAC degradation, G281R, HSCT cure | HUMAN_CLINICAL + IN_VITRO |
| 30796585 | Novel homozygous mutation case (abstract not public) | HUMAN_CLINICAL |
| 35170849 | Atypical late-onset ORAS, M86I/W167S | HUMAN_CLINICAL |
| 38914362 | New case W199R + GenIA review | HUMAN_CLINICAL |
| 40734169 | 3 Arab patients V185F + 13-patient pooled table | HUMAN_CLINICAL |
| 32231246 | Liver disease, mTOR/rapamycin | HUMAN_CLINICAL + MODEL_ORGANISM |
| 32075762 | Hepatocyte apoptosis→HCC, FADD/RIPK1 | MODEL_ORGANISM |
| 29950720 | Catalytic-dead KI mouse, LUBAC regulation | MODEL_ORGANISM |
| 34625557 | Keratinocyte necroptosis mouse | MODEL_ORGANISM |
| 38000038 | Myeloid RIPK3→NLRP3→IL-1β | MODEL_ORGANISM |
| 35587511 | **Haploinsufficiency**, caveolin-1/α-toxin, 5p−, penetrance | HUMAN_CLINICAL + IN_VITRO |
| 41293556 | Haploinsufficiency, broadened triggers, 6 patients | HUMAN_CLINICAL |
| 38578307 | Haploinsufficiency hyperinflammation | HUMAN_CLINICAL |
| 38129331 | Haploinsufficiency fasciitis treated by TNF inhibition | HUMAN_CLINICAL |
| 40084498 | Post-surgical necrosis, R263W | HUMAN_CLINICAL |
| 38630025 | Dominant-negative C129S | HUMAN_CLINICAL + IN_VITRO |
| 38652464 | Dominant-negative R306Q (de novo) | HUMAN_CLINICAL + IN_VITRO |
| 42297973 | Isolated pyoderma gangrenosum, R57C | HUMAN_CLINICAL + IN_VITRO |
| 32721894 | Patient iPSC (L272P) | IN_VITRO |
| 38827742 | *Otulin*+/− mouse (human-model mismatch) | MODEL_ORGANISM |

---

## Curation notes / flags for KB entry

1. **The existing `kb/disorders/OTULIN-Related_Autoinflammatory_Syndrome.yaml` is a bare skeleton** (name, synonyms, MONDO:0014912, one empty pathophysiology node, one phenotype stub) with **no evidence**. This report provides the content to populate it.
2. **Two (arguably three) distinct diseases share this gene.** Recommend modelling classical **recessive ORAS** as the primary entry, with **OTULIN haploinsufficiency** either as a `has_subtypes` stratum or (given two divergent axes — inheritance AD vs AR, and a distinct stromal/α-toxin mechanism and necrosis phenotype) a candidate separate entry per the Mendelian lump/split rules. Capture the dominant-negative heterozygous ORAS (C129S, R306Q) via an `Inheritance` block + `variant_origin`/`functional_impact_category: DOMINANT_NEGATIVE`.
3. **Inheritance:** bind AR as primary (ClinGen **Definitive**, AR, 2026-05-19 — record as `gene_disease_validity` with `classified_by: CLINGEN`, quoting the CGGV row after fetching it). Add a separate AD mode for haploinsufficiency.
4. **Human–model mismatch** (PMID:38827742 vs 35587511) is a clean `HUMAN_MODEL_MISMATCH` discussion candidate.
5. **Cancer link:** hepatocellular carcinoma via chronic hepatocyte death (mouse + case) — note but do not over-claim in humans (single patient with steatotic liver disease, HCC shown in mouse).
6. **Before curating:** run `just fetch-reference` for each PMID above, `ORPHA:500062`, and the ClinGen CGGV assertion; verify every snippet as an exact substring per the `dismech-references` workflow (the short quotes in this report are abstract/full-text excerpts gathered via EuropePMC and must be re-verified against the fetched cache before use as evidence `snippet:` values).

**Sources:** [Orphanet ORPHA:500062 / Infevers](https://infevers.umai-montpellier.fr/web/web_ressources.php?n=29) · [MONDO:0014912 (OLS4)](https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms?obo_id=MONDO:0014912) · [ClinGen OTULIN (HGNC:25118)](https://search.clinicalgenome.org/kb/genes/HGNC:25118) · [MalaCards AIPDSB](https://malacards.org/card/autoinflammation_panniculitis_and_dermatosis_syndrome_autosomal_recessive) · PubMed/EuropePMC records for the PMIDs cited above.

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 34 |
| Resolved | 34 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 34 |
| On topic | 22 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 99 |
| Resolved | 96 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 16 |
| Terms named correctly | 11 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `NCIT:C15620` (1 mention) - the report calls it "antibiotic therapy", "Haploinsufficiency-specific supportive care:** aggressive **antibiotic therapy"; NCIT calls it **Antibiotic Therapy**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0014912` (9 mentions) - the report calls it "OLS4"; MONDO calls it **autoinflammation, panniculitis, and dermatosis syndrome, autosomal recessive**, and lists "ORAS" among its other names
- `HP:0031281` (1 mention) - the report calls it "Sialadenitis / parotitis"; HP calls it **Sialadenitis**
- `HP:0025452` (2 mentions) - the report calls it "Pyoderma gangrenosum (R57C only)"; HP calls it **Pyoderma gangrenosum**
- `NCIT:C642` (1 mention) - the report calls it "Other immunomodulators:** methotrexate"; NCIT calls it **Methotrexate**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `NCIT:C15620` - called "antibiotic therapy", "Haploinsufficiency-specific supportive care:** aggressive **antibiotic therapy"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `ORPHA`.