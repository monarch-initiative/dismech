---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-27T22:00:53.030883'
end_time: '2026-10-27T22:07:59.737146'
duration_seconds: 426.71
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: CACNA2D4-related Retinopathy
  mondo_id: MONDO:0700244
  category: Mendelian
  causal_genes: CACNA2D4
  omim_id: not recorded
  synonyms: retinal cone dystrophy 4; RCD4; CACNA2D4 cone dystrophy
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
  web_search_requests: 4
  num_turns: 50
  total_cost_usd: 3.163764600000001
  session_id: 0bfb328d-96db-5dca-803a-342a247b0264
  stop_reason: end_turn
  permission_denials: 4
  denied_tools:
  - Bash
  assistant_text_blocks: 6
citation_count: 20
reference_validation:
  total_references: 26
  verified: 26
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 22
  quotes_valid: 22
  relevance_assessed: 26
  on_topic: 19
  validator_version: 0.4.0
term_validation:
  total_terms: 46
  verified: 45
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 3
  labels_matching: 2
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0700244
    reported_labels:
    - "Gene\u2013disease validity:** ClinGen Retina GCEP rated *CACNA2D4*\u2013CACNA2D4-related\
      \ retinopathy"
    ontology_label: CACNA2D4-related retinopathy
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** CACNA2D4-related Retinopathy
- **MONDO ID:** MONDO:0700244 (if available)
- **Causal gene(s):** CACNA2D4
- **OMIM:** not recorded
- **Synonyms:** retinal cone dystrophy 4; RCD4; CACNA2D4 cone dystrophy
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **CACNA2D4-related Retinopathy** covering all of the
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

I'm collecting and checking the core CACNA2D4 papers (PMIDs, quotes), then I'll write the report.

Now fetching the key abstracts for exact quotes.

Retrying through the E-utilities endpoint, one paper at a time to avoid rate limits.

Still gathering sources: now the 2025 literature-review table, then the variant and model papers.

Checking the MONDO child term's cross-references and the ClinGen classification next.

I've finished the research; the report follows.

# CACNA2D4-related Retinopathy (MONDO:0700244): Research Report

**Causal gene:** *CACNA2D4* (HGNC:20202, `hgnc:20202` in dismech form), on chromosome 12p13.33. It encodes the α2δ-4 auxiliary subunit of voltage-gated calcium channels (UniProt Q7Z3S7; gene OMIM 608171; Entrez 93589; Ensembl ENSG00000151062) ([HGNC REST](https://rest.genenames.org/fetch/symbol/CACNA2D4)). The disease is autosomal recessive and affects the photoreceptor ribbon synapse. In the retina, α2δ-4 partners with the Cav1.4 pore subunit (*CACNA1F*, `hgnc:1393`). This is not the X-linked *CACNA1F* disease, and it is not the *CACNA2D3*/*CACNA2D1* conditions.

**How the facts were checked.** Quotes marked "abstract" were taken from PubMed E-utilities abstract text. The tool limited each quote to under 125 characters, so every quote is a sentence or fragment. They have **not** been run through `just fetch-reference` or `count-verified-snippets`; cache fetching was blocked in this session. Re-fetch each PMID and confirm each snippet before using it as evidence. Ontology IDs marked ✔ were found in this repo's `cache/*/terms.csv`. IDs marked ⚠ were not cached and need a lookup before binding.

---

## 1. Disease Information

**Overview.** This is a rare autosomal recessive inherited retinal dysfunction. Most reported patients have a cone-dominant disorder. It shows up as:
- reduced central acuity
- photophobia
- poor colour discrimination
- a distinctive full-field ERG

It is usually stable or only slowly progressive. The original report called it a "slowly progressing cone dystrophy" ([PMID:17033974](https://pubmed.ncbi.nlm.nih.gov/17033974)). Later reports described a non-progressive retinal dysfunction ([PMID:26560832](https://pubmed.ncbi.nlm.nih.gov/26560832)). Single-patient reports of retinitis pigmentosa (RP) and cone-rod dystrophy (CRD) exist, but they are weakly supported (see §4).

**MONDO structure.**
- **MONDO:0700244** "CACNA2D4-related retinopathy" is defined as "Any retinopathy caused by variants in the CACNA2D4 gene." MONDO notes it was created in January 2024 as a spectrum parent with one child, at the request of the ClinGen ocular working group, and that it may later be merged with that child ([OLS](https://www.ebi.ac.uk/ols4/api/search?q=CACNA2D4&ontology=mondo&rows=10)).
- **MONDO:0012507** "retinal cone dystrophy 4" is the child: "Any cone dystrophy in which the cause of the disease is a mutation in the CACNA2D4 gene."

**Identifiers on MONDO:0012507** ([OLS term](https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FMONDO_0012507)):

| Source | ID |
|---|---|
| OMIM (phenotype, RCD4) | 610478 |
| UMLS | C1864849 |
| MeSH (supplementary concept) | C566470 |
| MedGen | 355308 |
| GARD | 0010650 |
| DOID | 0081023 |
| Orphanet | not listed on the MONDO term; not verified here |
| ICD-10/ICD-11 | no specific code. Falls under hereditary retinal dystrophy (ICD-10 H35.5); this mapping is mine and unverified |

**Synonyms:** retinal cone dystrophy 4; retinal cone dystrophy type 4; RCD4; CACNA2D4 cone dystrophy; cone dystrophy caused by mutation in CACNA2D4.

**Curation note.** The template lists "OMIM: not recorded". OMIM 610478 sits on the child term (MONDO:0012507), not on MONDO:0700244. If the entry stays on MONDO:0700244, record MONDO:0012507 as a narrower term or as a `has_subtypes` binding.

**Data source.** All knowledge comes from published case reports and small families, about 10 or fewer probands worldwide, plus model organisms. There is no EHR or registry data.

## 2. Etiology

- **Cause:** biallelic loss-of-function variants in *CACNA2D4*. This is purely genetic and monogenic.
- **Gene–disease validity:** ClinGen Retina GCEP rated *CACNA2D4*–CACNA2D4-related retinopathy (MONDO:0700244) **Definitive, AR**, under SOP v9 on 2023-03-02. The GenCC summary says "Over eight probands reported four homozygous variants in this gene including one missense variant, and two large deletions covering multiple exons, as well as one stop gained," and that the association "has been upheld over time." The record cites PMIDs 17033974, 25356976, 26560832, 28041643 and 31834350 ([GenCC submission](https://thegencc.org/submissions/GENCC_000102-HGNC_20202-MONDO_0700244-HP_0000007-GENCC_100001)).
  - ClinGen ID: `CGGV:assertion_f413ef18-b8cf-44c3-abde-b7533e1dd54f-2023-03-02T17:00:00.000Z`.
  - The row is already in `cache/clingen/gene_validity.csv`: `CACNA2D4 | HGNC:20202 | CACNA2D4-related retinopathy | MONDO:0700244 | AR | SOP9 | Definitive`. Build the quotable cache with `just fetch-reference CGGV:…` and record it in `gene_disease_validity` with `classified_by: CLINGEN`.
- **Environmental risk factors, protective factors, gene–environment interactions:** none reported. The genetic or environmental modifiers that could explain differences between siblings are unknown ([PMID:40883544](https://pubmed.ncbi.nlm.nih.gov/40883544)).

## 3. Phenotypes

The cohort is tiny (about 10 or fewer patients), so frequencies are qualitative.

| Phenotype | HPO suggestion | Onset, course, frequency | Evidence |
|---|---|---|---|
| Reduced visual acuity | HP:0007663 Reduced visual acuity ✔ | Childhood. Usually mild to moderate (about 20/30 to 20/40). Stable or slowly progressive. Seen in all reported patients | Smirnov 2025 abstract: "Two siblings presented a reduced visual acuity and light sensitivity." Patient 1 had BCVA 20/40 at age 13 (full text) [PMID:40883544]. Ba-Abbad 2016: lifelong stable VA about 20/30 (letter, no abstract) [PMID:26560832] |
| Photophobia / light sensitivity | HP:0000613 Photophobia ✔ | Childhood. Common | as above |
| Colour vision defect | HP:0000551 Color vision defect ✔ (or HP:0007641 Dyschromatopsia ✔) | Low colour discrimination, reported by Ba-Abbad | PMID:26560832 (full text only) |
| Cone dystrophy / cone dysfunction | HP:0008020 Cone dystrophy ✔. HP:0000548 Cone/cone-rod dystrophy ✔ for the CRD case | Slowly progressive in the original sibs | Wycisk abstract: "Both patients share symptoms of slowly progressing cone dystrophy." [PMID:17033974] |
| Abnormal full-field ERG: reduced light-adapted (cone) responses, "pseudo-electronegative" dark-adapted (DA) response, reduced b/a ratio, multiphasic LA 3.0 b-wave, preserved x-wave | HP:0030466 Abnormal full-field electroretinogram ✔. HP:0007984 ERG: Reduced dark-adapted b-wave amplitude ✔ (patient 1 only). Electronegative-ERG HPO term ⚠ to be looked up | Seen in all patients. Ba-Abbad described it as generalized, predominantly inner-retinal cone-system dysfunction | Smirnov abstract: "ffERG was specific for CACNA2D4-related retinal dysfunction, but amplitudes of responses were different in the two patients"; "there was a reduced b/a ratio to a high intensity (30cd/m2) dark-adapted stimulus"; "an x-wave to a dim red flash was well preserved" [PMID:40883544]. Wycisk's sibs came from a cohort first diagnosed with night blindness and an electronegative ERG [PMID:17033974] |
| Nyctalopia | HP:0000662 ✔ | Uncertain. Present only through the original night-blindness referral cohort; rod function is often relatively preserved | PMID:17033974 (abstract mentions screening "34 patients initially diagnosed with night blindness", per search summary) |
| Foveal hypoplasia (grade I) | HPO foveal hypoplasia term ⚠ | One sibling only (age 35) | PMID:40883544 full text |
| Nystagmus | HP:0000639 ✔ | Single RP case only (with "increased need for light" and oculomotor apraxia) | PMID:33927996 (full text per review). Low confidence |
| Retinitis pigmentosa / rod-cone dystrophy | HP:0000510 Rod-cone dystrophy ✔ | Single report. Weak evidence | PMID:33927996, abstract: "Novel compound heterozygous, deleterious missense variants of the CACNA2D4 gene" |
| Absence of retinal degeneration on long follow-up | (a negative finding, best kept in notes) | — | Smirnov abstract: "During 17 years of follow-up, vision remained stable in patient 1, with no evidence of retinal degeneration." |

**Quality of life.** No QoL instrument data exist. The impact comes from mildly reduced acuity, glare and photophobia, and colour discrimination problems. Patients usually keep independent mobility and normal stereopsis (patient 2 in PMID:40883544).

**Extra-ocular phenotypes.** None are established. *CACNA2D4* deletions and variants have been reported in bipolar disorder and neurodevelopmental contexts, but these are unrelated to this disease and should not be curated as phenotypes. Examples: a 12p13.33 deletion in late-onset bipolar disorder (PMID:22488967), and behavioural phenotypes in α2δ-4 knockout mice (PMID:35353835).

## 4. Genetic / Molecular Information

**Gene:** *CACNA2D4*, `hgnc:20202`, 12p13.33, NM_172364. α2δ-4 has a GPI-anchored extracellular α2δ structure, with VWA and Cache domains.

**Reported variants:**

| Variant (NM_172364) | Type | Zygosity | Phenotype | Source |
|---|---|---|---|---|
| c.2406C>A, p.(Tyr802*) | Nonsense (removes about one-third of the ORF) | Homozygous; 2 sibs, consanguineous | Slowly progressive cone dystrophy | Wycisk 2006 [PMID:17033974]. Abstract: "we detected a homozygous nucleotide substitution (c.2406C-->A) in CACNA2D4"; "The mutation introduces a premature stop codon that truncates one-third of the corresponding open reading frame." Re-reported in 2 French sibs [PMID:40883544]: "Both patients were homozygous for the variant c.2406C > A, p.(Tyr802*) in CACNA2D4." It is unclear whether these are the same family |
| c.1882C>T, p.(Arg628*) | Nonsense | Homozygous | Non-progressive cone-dominant dysfunction | Ba-Abbad 2016 [PMID:26560832] |
| c.1719+2904_2551-27827del35862insTG | Large multi-exon deletion-insertion (about 35.9 kb) | Homozygous | Non-progressive dysfunction | Ba-Abbad 2016 [PMID:26560832]; probably found through the NIHR-BioResource WGS study, Carss 2017 [PMID:28041643] (relationship to confirm) |
| c.2120G>A, p.(Arg707His) | Missense | Homozygous | CRD; minimal clinical data, no functional study | Huang 2015 [PMID:25356976]. The abstract does not name CACNA2D4. LOVD lists the variant as likely pathogenic ([LOVD](https://databases.lovd.nl/shared/variants/0000797958)) |
| c.955G>A p.(Asp319Asn) + c.1822A>C p.(Ile608Leu) | Missense | Compound heterozygous | "arRP" in one Chinese proband | Cheng 2021 [PMID:33927996]. Abstract: "co-segregating with the clinical phenotype in the patient"; "These might be disease-causing mutations." ClinGen did not count it (its four variants are all homozygous) |
| about 30.65 kb deletion | Deletion | **Heterozygous** | RP in a second cousin who also carried a C21orf2 deletion | Gustafson 2017 [PMID:28837078]. Abstract: "a novel 30.651 kb heterozygous deletion in CACNA2D4 in the affected second cousin". A single heterozygous allele, so not explanatory on its own; do not curate as causal |
| One non-canonical splice-site variant | Splicing (minigene-confirmed) | — | IRD | Rodriguez-Muñoz 2022 [PMID:34996991]. Get variant details from the full text |

**Other genetic details:**
- **Functional class:** loss of function, through nonsense, large deletion, and probably missense. Use `functional_impact_category: LOSS_OF_FUNCTION` with `variant_origin: GERMLINE`. No gain-of-function or dominant-negative mechanism has been shown.
- **Population frequency:** no founder variant is known. Get gnomAD frequencies for each variant directly; they were not retrieved here.
- **Modifier genes:** none known. Sibling variability suggests modifiers exist [PMID:40883544].
- **Epigenetics:** nothing disease-specific. *CACNA2D4* methylation turns up in cancer and psychiatric methylome studies; these are not relevant.
- **Chromosomal:** 12p13.33 interstitial deletions that span *CACNA2D4* cause developmental delay (PMID:21144913). These are heterozygous and are not this retinopathy.
- **Somatic:** not applicable.

## 5. Environmental Information

There are no known environmental, lifestyle or infectious contributors. Photophobia leads to light-avoidance behaviour, but that is a consequence, not a cause.

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic *CACNA2D4* LoF variants** (nonsense, multi-exon deletion) **lead to** absent or truncated α2δ-4 protein, probably through NMD or loss of the C-terminal membrane anchor. NMD is inferred, not shown in human tissue. → GO:0005245 voltage-gated calcium channel activity ✔ (decreased). GO:0008331 high voltage-gated calcium channel activity ✔.
2. **Loss of α2δ-4 leads to** failure to traffic and stabilize **Cav1.4 (α1F) L-type channels** at photoreceptor presynaptic active zones, and a progressive loss of channels from terminals.
   - Mouse knockout abstract: "a progressive loss of Cav1.4 channels, first in terminals of rods and later cones" [PMID:29875267].
   - Zebrafish: "Knockout of cacna2d4b reduces the expression of Cacna1fa" [PMID:31834350].
   - Mouse: in cones, α2δ-4 is "essential for CaV1.4 function" [PMID:28262416].
   - Terms: GO:0097470 ribbon synapse ✔, GO:0048786 presynaptic active zone ✔, GO:0005891 voltage-gated calcium channel complex ⚠.
3. **Branch A, rods (strong in mouse, apparently mild in humans).** α2δ-4 forms a trans-synaptic complex with Cav1.4 and **ELFN1**, which aligns with postsynaptic mGluR6 (GRM6, `hgnc:4598` ✔). Losing α2δ-4 **leads to** failure of rod synaptogenesis and ribbon anchoring.
   - Abstract: α2δ4 "complexes with CaV1.4 and the rod synaptogenic mediator, ELFN1"; "Eliminating α2δ4 in mice abolishes rod synaptogenesis and synaptic transmission to rod ON-bipolar cells" [PMID:28262416].
   - Abstract: "rod spherules lack ribbons and other synaptic hallmarks early in development" [PMID:29875267].
   - Terms: GO:0007416 synapse assembly ✔ (decreased). CL:0000604 retinal rod cell ✔.
4. **Branch B, cones (the main human feature).** Reduced Cav1.4 current **leads to** reduced Ca²⁺-triggered glutamate release at cone pedicles. Cone synapse architecture is relatively preserved at first but degrades over time.
   - Abstract: "Although the molecular organization of cone synapses is less affected than rod synapses" [PMID:29875267].
   - The two mouse papers disagree about how much the cone ribbon depends on α2δ-4 (PMID:28262416 vs PMID:29875267).
   - Terms: GO:0007268 chemical synaptic transmission ✔ (decreased), GO:0070588 calcium ion transmembrane transport ✔ (decreased). CL:0000573 retinal cone cell ✔.
5. **Reduced synaptic transmission leads to** impaired signalling to ON- and OFF-bipolar cells (CL:0000749 ON-bipolar cell ✔, CL:0000752 cone retinal bipolar cell ✔). This **results in** an inner-retinal ERG pattern: reduced b/a ratio, abnormal LA b-wave, a "pseudo-electronegative" DA response, with relatively preserved photoreceptor (a-wave) generation. The link from synaptic defect to ERG waveform is inferred from mouse and zebrafish data plus human ERG.
   - Zebrafish: "Only knockout of both paralogs impaired cone-mediated ERG b-wave amplitude" [PMID:31834350].
   - Mouse: "Despite the absence of b-waves in electroretinograms, visually guided behavior is evident in α2δ-4 KO mice" [PMID:29875267].
6. **Loss of cone-pathway signal leads to** reduced acuity, photophobia and dyschromatopsia (GO:0007601 visual perception ✔, decreased).
7. **Branch C, secondary degeneration (variable; prominent in mouse, absent or minimal in most humans).** In mouse, chronic synaptic dysfunction **leads to** internal Ca²⁺-store depletion and compensatory Ca²⁺/Na⁺ influx through non-selective cation channels, then ER stress and rod death. Cone loss comes later.
   - Abstract: "internal calcium stores' depletion and upregulation of calcium entry via non-selective cationic channels (CSC)" [PMID:36361866].
   - Abstract: "The mutation leads to significant loss of rods, whereas the number of cone cells remains unaffected until 6 weeks of age" [PMID:16877424].
   - Cone-rich KO mice: "progressive degeneration with 10% loss by 2-months of age was observed" [PMID:37181655].
   - In humans: "no evidence of retinal degeneration" over 17 years [PMID:40883544]. This step is mostly model evidence; flag `HUMAN_MODEL_MISMATCH`.
8. **Accessory mechanism (model only).** Mislocalization of the TMEM16A Ca²⁺-activated Cl⁻ channel, which associates with Cav1.4 at the terminal. Abstract: "TMEM16A channels lose their characteristic localization"; "TMEM16A associates with the CaV1.4 subunit" [PMID:26557056].

**Upstream and downstream.** The molecular steps (1–2) feed the synaptic and cellular steps (3–5), which produce the clinical findings (6). Degeneration (7) is a downstream branch that depends on the species.

**Cell types:** retinal cone cell (CL:0000573 ✔), retinal rod cell (CL:0000604 ✔), photoreceptor cell (CL:0000210 ✔), ON-bipolar cell (CL:0000749 ✔), cone retinal bipolar cell (CL:0000752 ✔).

**Possible module conformance.** Check `just list-modules synap` and `just list-modules channel` for a photoreceptor synaptopathy or CSNB module. The sibling entry `CACNA1F-Related_Retinopathy.yaml` is the closest mechanistic template. I have not checked which modules exist.

**Omics:** there are no human transcriptomic, proteomic or single-cell disease datasets specific to this condition. Cheng 2021 notes that "The CACNA2D4 mRNA expression showed the highest expression in the retina of humans" [PMID:33927996].

## 7. Anatomical Structures

| Level | Structures |
|---|---|
| Organ | Eye/retina (UBERON:0000966 ✔), bilateral and symmetric. Macula/fovea (UBERON:0000053 macula lutea ✔). No other organ systems |
| Tissue | Photoreceptor layer (UBERON:0001787 ✔), outer nuclear layer (UBERON:0001789 ✔), outer plexiform layer (UBERON:0001790 ⚠, the synaptic site), inner nuclear layer (UBERON:0001791 ✔, bipolar cells) |
| Cell | Cones first; rods in models; bipolar neurons postsynaptically |
| Subcellular | Ribbon synapse (GO:0097470 ✔), presynaptic active zone (GO:0048786 ✔), presynapse (GO:0098793 ✔), voltage-gated calcium channel complex (GO:0005891 ⚠) |

## 8. Temporal Development

- **Onset:** childhood (e.g., presenting at age 13) and probably congenital. The disease is insidious.
- **Course:** mostly stationary or very slowly progressive. Ba-Abbad 2016 and Smirnov 2025 describe it as non-progressive ("nonprogressive character, as previously suggested", per PMC12568804). The original sibs were "slowly progressing" [PMID:17033974]. There are no formal stages. It lasts lifelong, with no remission.
- **Critical period (preclinical):** AAV work in mice found the most complete rescue with neonatal treatment. Later treatment rescued cone function more reliably than rod function (Ung 2026 preprint [PMID:42539265]).

## 9. Inheritance and Population

- **Inheritance:** autosomal recessive (HP:0000007; ClinGen MOI AR). Bind it in the entry's `inheritance` block.
- **Penetrance and expressivity:** penetrance appears complete in biallelic carriers. Expressivity varies even within a family: "Intrafamily clinical and electrophysiological expression of CACNA2D4-associated retinal dysfunction can be variable" [PMID:40883544].
- **Consanguinity:** present in the original family [PMID:17033974].
- **Prevalence:** unknown. Fewer than about 15 patients have been published. Use `prevalence_class` with `measure_type: CASES_IN_LITERATURE`, or `UNKNOWN` (e.g., `RARE`/`ULTRA_RARE`).
- **Geography and populations:** patients have been reported from Germany/Europe, the UK, France and China. No founder effect is known. The sex ratio is not skewed, as expected for AR inheritance.
- **Not applicable:** carrier frequency, anticipation and germline mosaicism are not reported.

## 10. Diagnostics

**Electrophysiology is the most informative test.** ISCEV full-field ERG findings:
- reduced and abnormal LA cone responses, with a multiphasic LA 3.0 b-wave
- reduced b/a ratio to a bright DA flash ("pseudo-electronegative")
- preserved x-wave to a dim red flash

This pattern points to an inner-retinal cone-system defect and separates it from CSNB and photoreceptor cone dystrophies [PMID:40883544, PMID:26560832]. Pattern/multifocal ERG shows macular dysfunction.

**Other tests:**
- **Imaging:** OCT (NCIT:C20828 ✔; SD-OCT NCIT:C162464 ✔) and fundus autofluorescence. Usually normal, or shows mild foveal changes such as grade I foveal hypoplasia.
- **Psychophysics:** colour vision testing; visual fields.
- **Genetic testing:** an IRD multi-gene panel (NCIT:C198412 ✔) that includes *CACNA2D4*, then WES (NCIT:C101295 ✔). **WGS (NCIT:C101294 ✔) or CNV analysis is needed**, because two of the four ClinGen-counted variants are large multi-exon deletions; WES/panel CNV calling can miss them. Gustafson 2017 "demonstrated the value of WGS when WES fails to identify likely disease-causing mutations" [PMID:28837078]. Non-canonical splice variants may need minigene or RNA confirmation [PMID:34996991].
- **Not relevant:** labs, biomarkers, biopsy, CMA/karyotype, mtDNA testing, repeat-expansion testing.

**Differential diagnosis:**
- *CACNA1F* incomplete CSNB (X-linked)
- *CABP4* cone-rod synaptic disorder (very similar ERG)
- *RIMS2*
- complete CSNB genes (*NYX*, *GRM6*, *TRPM1*, *GPR179*, *LRIT3*)
- achromatopsia and other cone dystrophies (*CNGA3*, *CNGB3*, *KCNV2*)
- *KCNV2* "cone dystrophy with supernormal rod responses" (one sibling in Smirnov had supranormal DA amplitudes)

**Screening:** no newborn screening. Cascade carrier testing in families.

## 11. Outcome / Prognosis

- Life expectancy is normal, with no disease-related mortality.
- Morbidity is lifelong mild-to-moderate visual impairment (about 20/30 to 20/40), glare and photophobia, and colour discrimination deficits. Vision can stay stable for decades (17 years in PMID:40883544).
- No validated prognostic biomarkers exist.
- Complications such as cystoid macular edema or cataract have not been reported.

## 12. Treatment

**No disease-specific approved therapy exists.**

**Supportive care** (NCIT:C15747 Supportive Care ✔): refraction, low-vision aids and tinted or filter lenses for photophobia. NCIT device and filter-lens terms ⚠; per CLAUDE.md, devices are not clinical actions. Educational support as needed. Use `therapeutic_modality: DEVICE` or `BEHAVIORAL` where appropriate.

**Genetic counseling** (NCIT:C15240 ✔): AR recurrence risk of 25%, and carrier testing for relatives.

**Gene therapy** (NCIT:C15238 ✔, `GENE_THERAPY`): preclinical only. There are no clinical trials. A ClinicalTrials.gov search is recommended; none was found here.
- **Ung et al. 2026 (bioRxiv, PMID:42539265):** AAV8-GRK1-α2δ4 in α2δ4-KO mice. Abstract: "AAV-mediated α2δ4 expression restored synaptic localization of Cav1.4, ELFN proteins, and mGluR6 at all treatment ages." Neonatal treatment gave the most complete rescue. Adult treatment produced more ectopic synapses.
- **Hasan et al. 2026 (bioRxiv, PMID:42427680):** rod-directed rAAV in adult KO mice prevented rod degeneration and improved acuity, with benefit lasting up to 14 months. Abstract: "synaptic structure and function can be restored in the mature mouse retina."
- These are preprints with `MODEL_ORGANISM` evidence.

**Exon skipping: argued against.** Bacchi 2015 found that "The designed exon-skipping strategy is not applicable because the resulting skipped α2δ4 are nonfunctional" [PMID:26218913].

**Experimental idea (model only):** blocking non-selective cation channels to prevent rod death. Abstract: "Blocking CSC may provide a novel strategy…" [PMID:36361866].

**Pharmacogenomics:** none. Gabapentinoids bind α2δ-1 and α2δ-2, not α2δ-4, so they are not relevant.

## 13. Prevention

- **Primary:** none, beyond reproductive options: carrier testing of partners in consanguineous families, prenatal diagnosis, or PGT once familial variants are known.
- **Secondary:** early ERG and genetic diagnosis in children with photophobia or reduced acuity, to avoid misdiagnosis (e.g., as amblyopia).
- **Tertiary:** low-vision rehabilitation and glare control.
- **Not applicable:** vaccination and public-health measures.

## 14. Other Species / Natural Disease

- **Spontaneous mouse mutant:** a C57BL/10 substrain carrying a *Cacna2d4* frameshift insertion (c.2367insC per Wycisk; described as c.2451insC in later papers). Abstract: "In a spontaneous mutant substrain of C57BL/10 mice, severely affected retinal ribbon-type synapses have been described"; "The Cacna2d4 mutation underlies a novel channelopathy leading to cone-rod dysfunction in the visual system of mice" [PMID:16877424].
- **Dog:** there is no natural canine *CACNA2D4* disease. In a beagle CSNB model, *CACNA2D4* was **excluded** as the cause, although its expression was reduced [PMID:26368928].
- **OMIA:** not checked.
- **Orthologs:** mouse *Cacna2d4* (MGI ⚠); zebrafish *cacna2d4a* and *cacna2d4b* (ZFIN ⚠).
- **Taxa:** NCBITaxon:10090 (mouse), NCBITaxon:7955 (zebrafish). Not cached; verify.
- **Zoonotic potential:** not applicable.

## 15. Model Organisms

| Model | Genotype | Recapitulation | Limitations | Source |
|---|---|---|---|---|
| Spontaneous mutant mouse (C57BL/10 substrain) | *Cacna2d4* frameshift insertion, homozygous | Ribbon synapse disorganization. Abstract: "Rod photoreceptor responses were maintained with reduced amplitude, whereas cone activities were absent" | Rod loss is prominent, unlike human. Phenotype "is closer to congenital stationary night blindness" (PMC12568804) | PMID:16877424; PMID:36361866; PMID:26557056; PMID:26218913 |
| α2δ4 KO mouse (Wang 2017) | Null | No rod synaptogenesis, no rod ON-bipolar transmission. Cone Cav1.4 function lost | Rod defect is more severe than in humans | PMID:28262416 |
| α2δ-4 KO mouse (CRISPR) | Null | Rod spherules lack ribbons. Progressive loss of Cav1.4 from rods, then cones. No ERG b-wave, but visually guided behaviour is preserved | Some disagreement with Wang 2017 about cone ribbons | PMID:29875267 |
| "Conefull" all-cone mouse × α2δ4 KO | RPE65 R91W KI; Nrl KO; α2δ4 KO | Reduced b-wave; about 10% degeneration by 2 months | Artificial cone-only retina | PMID:37181655 |
| Zebrafish *cacna2d4a/b* double KO (CRISPR) | Double null | Lower cone-mediated b-wave with no degeneration. Closest match to the human mild cone dysfunction | Paralog redundancy; differences between fish and mammal synapses | PMID:31834350 |
| AAV rescue models | AAV8-GRK1-α2δ4 or rod-targeted rAAV in KO mice | Restores synapses and ERG. Rescue depends on age | Preprints | PMID:42539265; PMID:42427680 |

**Suggested `modeled_mechanisms`:**
- KO mice `RECAPITULATES` the Cav1.4 synaptic-loss node and `PARTIALLY_RECAPITULATES` the cone phenotype.
- Mouse rod degeneration should be `FAILS_TO_RECAPITULATE` or a `HUMAN_MODEL_MISMATCH` discussion, because humans stay stable for years [PMID:40883544].

---

## Key gaps and cautions for curation

1. **Disease scope.** Decide whether the entry is the spectrum term (MONDO:0700244, which is what ClinGen curated) with RCD4 (MONDO:0012507, OMIM 610478) as a subtype.
2. **Phenotype evidence needs full text.** The Ba-Abbad 2016 letter (PMID:26560832) has no abstract; its acuity, colour-vision and ERG details need full text. Run `just fetch-reference PMID:26560832 --force` only if PMC access exists; it is not in PMC.
3. **RP and CRD reports are weak.** PMID:33927996 (compound heterozygous missense) and PMID:28837078 (heterozygous deletion only) do not belong as core phenotypes. The Huang 2015 abstract (PMID:25356976) does not mention *CACNA2D4*, so it cannot serve as abstract-level evidence.
4. **Terms marked ⚠ need lookup** before binding: an electronegative-ERG HP term, a foveal hypoplasia HP term, GO:0005891, UBERON:0001790, NCBITaxon IDs, and MGI/ZFIN IDs.
5. **Quotes are unverified.** None of the quotes above were checked against `references_cache/`. Fetch every PMID before using a snippet.

## Sources
- [Wycisk 2006 AJHG, PMID:17033974](https://pubmed.ncbi.nlm.nih.gov/17033974) · [PMC1698577](https://pmc.ncbi.nlm.nih.gov/articles/PMC1698577)
- [Wycisk 2006 IOVS, PMID:16877424](https://pubmed.ncbi.nlm.nih.gov/16877424)
- [Ba-Abbad 2016 Ophthalmology, PMID:26560832](https://pubmed.ncbi.nlm.nih.gov/26560832)
- [Smirnov 2025 Doc Ophthalmol, PMID:40883544 / PMC12568804](https://pmc.ncbi.nlm.nih.gov/articles/PMC12568804/)
- [Cheng 2021 3 Biotech, PMID:33927996](https://link.springer.com/10.1007/s13205-021-02761-4)
- [Wang 2017 Neuron, PMID:28262416](https://pubmed.ncbi.nlm.nih.gov/28262416) · [PMC5364038](https://pmc.ncbi.nlm.nih.gov/articles/PMC5364038)
- [Kerov 2018 J Neurosci, PMID:29875267](https://pmc.ncbi.nlm.nih.gov/articles/PMC6031576)
- Schlegel 2019 IOVS, PMID:31834350 · Vellani 2022 IJMS, PMID:36361866 · Caputo 2015, PMID:26557056 · Bacchi 2015, PMID:26218913 · Laird 2023, PMID:37181655 · Gustafson 2017, PMID:28837078 · Kondo 2015, PMID:26368928 · Rodriguez-Muñoz 2022, PMID:34996991 · Huang 2015, PMID:25356976 · Carss 2017, PMID:28041643 · Ung 2026, PMID:42539265 · Hasan 2026, PMID:42427680 (all via [NCBI E-utilities](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/))
- [GenCC / ClinGen Retina GCEP submission](https://thegencc.org/submissions/GENCC_000102-HGNC_20202-MONDO_0700244-HP_0000007-GENCC_100001) · [GenCC gene page](https://search.thegencc.org/genes/HGNC:20202/disease)
- [OLS MONDO search](https://www.ebi.ac.uk/ols4/api/search?q=CACNA2D4&ontology=mondo&rows=10) · [OLS MONDO:0012507](https://www.ebi.ac.uk/ols4/api/ontologies/mondo/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FMONDO_0012507)
- [HGNC CACNA2D4](https://rest.genenames.org/fetch/symbol/CACNA2D4)
- [LOVD p.(Arg707His)](https://databases.lovd.nl/shared/variants/0000797958) · [MalaCards RCD4](https://www.malacards.org/card/retinal_cone_dystrophy_4) · [FindZebra RCD4](https://www.findzebra.com/details/OnLRpGl-retinal-cone-dystrophy-4) · [GeneBe CACNA2D4](https://genebe.net/gene/hg38/CACNA2D4)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 26 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 22 |
| Quoted claims found in source | 22 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 26 |
| On topic | 19 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 46 |
| Resolved | 45 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 3 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0700244` (7 mentions) - the report calls it "Gene–disease validity:** ClinGen Retina GCEP rated *CACNA2D4*–CACNA2D4-related retinopathy"; MONDO calls it **CACNA2D4-related retinopathy**