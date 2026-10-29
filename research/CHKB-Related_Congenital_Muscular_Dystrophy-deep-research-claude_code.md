---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: true
start_time: '2026-10-29T04:06:43.239848'
end_time: '2026-10-29T04:06:43.245909'
duration_seconds: 0.01
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: CHKB-Related Congenital Muscular Dystrophy
  mondo_id: MONDO:0010923
  category: Mendelian
  causal_genes: CHKB
  omim_id: OMIM:600706
  synonyms: megaconial congenital muscular dystrophy; CHKB-related muscular dystrophy;
    congenital muscular dystrophy, megaconial type
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
  num_turns: 39
  total_cost_usd: 3.0537004999999993
  session_id: 0bfb328d-96db-5dca-803a-342a247b0264
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  assistant_text_blocks: 3
citation_count: 10
reference_validation:
  total_references: 32
  verified: 32
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 6
  quotes_valid: 6
  relevance_assessed: 32
  on_topic: 28
  validator_version: 0.4.0
term_validation:
  total_terms: 70
  verified: 63
  not_found: 0
  obsolete: 0
  unverifiable: 7
  confabulation_rate: 0.0
  labels_checked: 10
  labels_matching: 6
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: GO:0005829
    reported_labels:
    - where CHKB itself is
    ontology_label: cytosol
  - term_id: CHEBI:295975
    reported_labels:
    - both from UniProt Rhea
    ontology_label: choline phosphate(1-)
  labels_variant: 2
  unresolvable_prefixes:
  - OMIM
  - ORPHA
  - Rhea
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** CHKB-Related Congenital Muscular Dystrophy
- **MONDO ID:** MONDO:0010923 (if available)
- **Causal gene(s):** CHKB
- **OMIM:** OMIM:600706
- **Synonyms:** megaconial congenital muscular dystrophy; CHKB-related muscular dystrophy; congenital muscular dystrophy, megaconial type
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **CHKB-Related Congenital Muscular Dystrophy** covering all of the
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

Identifiers are settled: OMIM:600706 is the adult allelic form of the same CHKB disease. I've listed the CHKB literature and am now pulling abstracts of the key papers to quote.

Abstracts for the key clinical, mechanism and model papers are in hand. Two last lookups: the OMIM record for the identifier history, and CHKB gene/protein facts.

# CHKB-Related Congenital Muscular Dystrophy (megaconial congenital muscular dystrophy): research report

*Prepared 2026-10-29 for the dismech entry `kb/disorders/CHKB-Related_Congenital_Muscular_Dystrophy.yaml`.*

**Causal gene: *CHKB*** (choline kinase β; HGNC:1938, `hgnc:1938`; gene OMIM 612395; chromosome 22q13.33; UniProt Q9Y259). Biallelic loss-of-function variants cause a single disease spectrum. At the severe end is a congenital muscular dystrophy with intellectual disability. At the mild end is an adolescent- or adult-onset proximal myopathy with normal cognition.

---

## ⚠️ Identifier issue to resolve before curating

The MONDO ID and OMIM number in the brief do not name the classic congenital disease. They name its adult-onset allelic form.

| Identifier | Resolves to (checked on OLS4) | Relationship to CHKB |
|---|---|---|
| **MONDO:0010923** / **OMIM:600706** / ORPHA:521305 / MeSH C563453 / GARD 0017956 / UMLS C1833453 | "proximal myopathy with focal depletion of mitochondria" | Adult-onset, cognitively normal **allelic form**, shown to be *CHKB*-related by Brady et al. 2016 (PMID:26782016) |
| **MONDO:0011246** / **OMIM:602541** / ORPHA:280671 / MeSH C566527 / DOID:0110632 / GARD 0010317 / UMLS C1865233 / MedGen 355943 | "megaconial type congenital muscular dystrophy" (MDCMC) | The **canonical CHKB disease**, the one the entry name, synonyms and gene describe |

**Recommendation:**
- Make MONDO:0011246 the primary `disease_term`. The entry name, its synonyms and the gene all match it.
- Record MONDO:0010923 as a `has_subtypes` row for the mild form (for example `name: Adult-onset proximal myopathy`), or as a mapping with an explicit predicate. Under the repo's rules for MONDO coverage, a `has_subtypes` term counts as curated.
- The draft YAML currently binds MONDO:0010923 with the label "proximal myopathy with focal depletion of mitochondria" while its `preferred_term` says "CHKB-related congenital muscular dystrophy". That is a self-consistent but wrong binding, and it should be fixed.

**Sources checked:** OLS4 MONDO term records for MONDO:0010923 and MONDO:0011246; [MSeqDR disease 00412](https://mseqdr.org/MITO2023/diseases/00412); the [GARD record 17956](https://rarediseases.info.nih.gov/assets/singles/17956.json); and [Global Genes](https://globalgenes.org/?p=614506), which reproduces Orphanet's description of ORPHA:521305.

---

## How the quotes were gathered (read this before copying any into YAML)

- The abstracts were read through the Europe PMC REST API using a fetch tool, which returns text in segments of at most 125 characters. **Quotes below are verbatim abstract segments as returned. They have not yet been checked against `references_cache/`.**
- Before any quote becomes a `snippet:`, run `just fetch-reference PMID:<id>` and then `just count-verified-snippets`.
- Every ontology CURIE suggested here is a **lead, not a checked binding**. The repo requires each one to be looked up (with `runoak` or a cache file) in the same step it is written. CURIEs marked † are ones I am less sure of.
- I could not retrieve the full GeneReviews chapter text (NCBI showed a bot check). Its PubMed abstract (PMID:37011121) was retrieved.

---

## 1. Disease information

**What it is.**
- An autosomal recessive muscular dystrophy caused by loss of choline kinase β. This enzyme catalyses the first step of de novo phosphatidylcholine (PC) synthesis through the Kennedy (CDP-choline) pathway.
- The disease has a pathognomonic muscle biopsy: enlarged ("megaconial") mitochondria crowd the periphery of each fibre, and the fibre centre has none.

**Original descriptions.**
- Nishino et al. 1998, *Muscle Nerve* 21:40–47 (PMID:9427222, citation per OMIM): "A new congenital muscular dystrophy with mitochondrial structural abnormalities", four patients from three families, merosin-positive.
- The gene was identified by Mitsuhashi et al. 2011 (PMID:21665002).

**Identifiers.**
- MONDO:0011246; OMIM #602541; ORPHA:280671; MeSH C566527; DOID:0110632; UMLS C1865233.
- Allelic adult form: MONDO:0010923 / OMIM 600706 / ORPHA:521305.
- No specific ICD-10 code was found. G71.2 (congenital myopathies) or G71.0x (muscular dystrophy) are plausible broad codes but were not verified.

**Synonyms (from MONDO).** MDCMC; congenital megaconial myopathy; congenital muscular dystrophy due to phosphatidylcholine biosynthesis defect; congenital muscular dystrophy with mitochondrial structural abnormalities; megaconial congenital muscular dystrophy; CHKB-related muscular dystrophy (CHKB-MD).

**Source of information.** Aggregated disease-level resources (OMIM, Orphanet, GeneReviews) plus case series and case reports. There are no EHR cohorts.

**GeneReviews (Chan SHS & Nishino I, first posted 2023-03-30; PMID:37011121).**
> "CHKB-related muscular dystrophy (CHKB-MD), reported in 47 individuals to date" … "comprises congenital muscular dystrophy (CMD) (44 individuals)" … "and adolescent-onset limb-girdle muscular dystrophy (LGMD) (3 individuals)."

## 2. Etiology

- **Cause.** Biallelic (homozygous or compound heterozygous) loss-of-function variants in *CHKB*.
  - PMID:21665002: "identified homozygous or compound heterozygous mutations in the gene encoding choline kinase beta (CHKB)".
  - GeneReviews: "biallelic loss-of-function pathogenic variants in CHKB identified by molecular genetic testing."
- **Genetic risk factors.**
  - Parental consanguinity: most reported patients are homozygous.
  - Wu et al. 2023 (PMID:36896673): "of which 40 patients showed homozygosity." The same paper warns that apparent homozygosity can be a large deletion on one allele or uniparental isodisomy: "homozygous variants can be masqueraded by uniparental disomy or large deletions in offspring of non-consanguineous parents."
  - No modifier genes have been established.
- **Environmental triggers that worsen established disease.** None cause the disease; these exacerbate it.
  - Intercurrent infection and general anaesthesia. Quinlivan 2013 (PMID:23692895): "there appeared to be acute deterioration with infection/general anaesthesia."
  - Cabrera-Serrano 2015 (PMID:25187204): "sudden and transient deteriorations of muscle strength with acute intercurrent illnesses."
  - Strenuous exercise. GeneReviews: "Avoid strenuous exercise and viral infections, which may exacerbate muscle weakness."
  - In the adult form, exercise precipitates myalgia and rhabdomyolysis (PMID:26782016; Orphanet's description of ORPHA:521305).
- **Protective factors.** No genetic or environmental protective factors are documented in humans.
  - Choline kinase α (CHKA) partly compensates in mice, and is thought to explain the forelimb-sparing rostrocaudal gradient there (see §15).
  - Upregulating CHKA was proposed as a therapy (PMID:31216357). This is model-organism evidence only.
- **Gene–environment interaction.** The only evidence is that stressors with high metabolic demand (illness, anaesthesia, exercise) unmask weakness or rhabdomyolysis. There is no formal G×E data.
- **Unrelated association to keep separate.** A common variant between *CPT1B* and *CHKB* is associated with narcolepsy susceptibility (PMID:18820697). This is not part of this disease.

## 3. Phenotypes

The best-quantified series is Haliloglu et al. 2015, 15 patients from 14 families (PMID:26067811). Other series: Mitsuhashi 2011 (n=15), Zemorshidi 2023 (13 Iranian patients), Bardhan 2021 (5 Indian children), and the GeneReviews totals. HPO suggestions are leads to be verified.

| Phenotype | Frequency / characteristics | Key quote (PMID) | HPO lead |
|---|---|---|---|
| Global developmental delay | All CMD cases (15/15); gross motor and language most affected | "Core clinical phenotype included global developmental delay prominent in gross-motor and language domains" (26067811) | HP:0001263 Global developmental delay |
| Intellectual disability | 15/15 in CMD form ("severe ID… in all cases"); absent in the adult form | "severe intellectual disability (ID), and/or muscle weakness in all cases." (26067811) | HP:0001249 Intellectual disability; HP:0010864 Intellectual disability, severe† |
| Speech delay / absent speech | All CMD cases have speech delay; some have no speech | "All affected children have developmental delay and speech delay"; "some have no speech." (37011121) | HP:0000750 Delayed speech and language development; HP:0001344 Absent speech† |
| Muscle weakness, proximal / limb-girdle | Universal; slowly progressive (13/15) or static (2/15); later loss of ambulation | "gross motor milestones are delayed with subsequent loss of ambulation over time." (37011121) | HP:0003701 Proximal muscle weakness; HP:0003202 Skeletal muscle atrophy |
| Neonatal / infantile hypotonia | 3/15 neonatal (Haliloglu); "hypotonia from birth" in other series | "muscle weakness and hypotonia in early infancy" (21665002) | HP:0001319 Neonatal hypotonia; HP:0001252 Hypotonia |
| Elevated serum CK | 12/15; usually mild to moderate | "increased serum CK levels (n = 12)" (26067811) | HP:0003236 Elevated circulating creatine kinase concentration |
| Ichthyosis-like skin changes | 11/15 (Haliloglu); "common" (GeneReviews); psoriasiform in some cases | "ichthyosis-like skin changes (n = 11)" (26067811) | HP:0008064 Ichthyosis |
| Dilated cardiomyopathy | 2/15 (Haliloglu); 14/47 in GeneReviews, with 5 heart-failure deaths and 1 transplant; ~50% per OMIM/UniProt summary | "Dilated cardiomyopathy, seen in 14 children, resulted in death from heart failure in five" (37011121) | HP:0001644 Dilated cardiomyopathy |
| Cardiac conduction disease | Case report: LAFB plus complete RBBB | "a left anterior fascicular block, and a complete right bundle branch block." (39465137) | HP:0011712 Right bundle branch block†; HP:0011706 Left anterior fascicular block† |
| Congenital heart defects | 3/15 | "congenital heart defects (n = 3)" (26067811) | HP:0001627 Abnormal heart morphology† |
| Autistic features / ASD; ADHD | Common; Rett-like stereotypies in Indian cohort | "Autism spectrum disorder or attention-deficit/hyperactivity disorder is common." (37011121); "moderate-to-severe autistic behavior, hand stereotypies" (33712684) | HP:0000729 Autistic behavior; HP:0007018 Attention deficit hyperactivity disorder; HP:0000733 Motor stereotypy† |
| Microcephaly | 6/15 | "microcephaly (n = 6)" (26067811) | HP:0000252 Microcephaly |
| Seizures / epileptiform EEG | 3/15 seizures; 2/15 EEG abnormality without seizures | "seizures (n = 3)" (26067811) | HP:0001250 Seizure |
| Dysmorphic facial features | 7/15 | "dysmorphic facial features (n = 7)" (26067811) | HP:0001999 Abnormal facial shape |
| Hearing loss | 1 sensorineural, 1 conductive (of 15) | "sensorineural (n = 1), and conductive hearing loss (n = 1)." (26067811) | HP:0000407; HP:0000405 |
| Lack of sphincter control | Most of the Indian series | "the majority did not attain sphincter control." (33712684) | HP:0000020 Urinary incontinence† |
| Gastrointestinal features | 2/3 British patients | "Gastrointestinal features occurred in two patients" (23692895) | HP:0011024 Abnormality of the gastrointestinal tract† |
| Jordans anomaly (vacuolated leukocytes) | 1 patient | "Blood smear in one patient showed Jordans anomaly (vacuolated leukocytes)." (23692895) | HP:0001880? (verify) |
| Reduced brain choline on MRS | Most MRIs normal; low choline:Cr / choline:NAA in some | "significant reduction in choline:N-acetyl aspartate and choline:creatine ratios" (23692895) | (lab/imaging; no HP lead) |
| Scoliosis, hip subluxation | Individual cases | "scoliosis, hip subluxation and early loss of ambulation" (31926838) | HP:0002650 Scoliosis |
| **Adult form:** mild non-progressive weakness, exercise myalgia, rhabdomyolysis | 2 siblings aged 37 and 40; 2/3 LGMD-onset cases in GeneReviews had rhabdomyolysis | "cognitively normal with mild non-progressive muscle weakness" "and a susceptibility to rhabdomyolysis." (26782016) | HP:0003201 Rhabdomyolysis; HP:0003738 Exercise-induced myalgia† |

**Course.** Haliloglu: "Evolution was progressive (n = 13) and static (n = 2)." Intrafamilial variability was seen in 4 families.

**Quality of life.** No EQ-5D, SF-36 or PROMIS data exist. The main burdens are severe intellectual disability with no speech, autism, loss of ambulation, and cardiomyopathy.

## 4. Genetic / molecular information

- **Gene and protein.**
  - *CHKB*: HGNC:1938; OMIM 612395; 22q13.33. It sits head-to-tail with *CPT1B*, and the two are co-regulated (PMID:33058877).
  - Protein: choline/ethanolamine kinase, 395 aa, UniProt Q9Y259.
  - Activities: choline kinase, Rhea:12837, EC 2.7.1.32 (choline + ATP → phosphocholine + ADP); and ethanolamine kinase, Rhea:13069, EC 2.7.1.82.
  - Forms homodimers and heterodimers with CHKA.
  - GO terms per UniProt: GO:0004103 choline kinase activity; GO:0004305 ethanolamine kinase activity; GO:0006657 CDP-choline pathway; GO:0006646 phosphatidylethanolamine biosynthetic process; GO:0005829 cytosol.
- **Variant spectrum.** Predominantly null alleles (nonsense, frameshift, canonical splice), plus missense and intronic splice variants. Examples:
  - Recurrent frameshift c.598del p.(Gln200Argfs*11): two unrelated Chinese patients (PMID:31926838) and a cardiomyopathy-dominant 13-year-old (PMID:39465137).
  - c.810T>A p.(Tyr270*): Spanish (PMID:26006750). c.648C>A p.(Tyr216*): Italian (PMID:25187204). c.248_249insT p.(Arg84Profs*209): heart-transplant case (PMID:26855408).
  - Missense: c.722A>G p.(Asn241Ser), mild phenotype (PMID:26548592); c.581G>A p.(Arg194Gln) (PMID:33712684); c.1060G>C p.(Gly354Arg) (PMID:36175989).
  - Indian null alleles: c.1027dupA, c.224+1G>T, c.1123C>T (PMID:33712684).
  - Deep or intronic: c.448-56_29del causes partial retention of intron 3 and is missed by standard exon sequencing (PMID:36175989). Splicing effects of three rare variants were characterised by Cotrina-Vinagre 2025 (PMID:41026188).
  - Adult form: compound heterozygous c.263C>T + c.950T>A (PMID:26782016).
  - Copy number and UPD: a maternal large deletion encompassing *CHKB*, and paternal uniparental isodisomy (PMID:36896673).
- **Functional consequence.** Loss of function.
  - PMID:21665002: "choline kinase activities were undetectable".
  - PMID:23692895: "CHKB activity was reduced in all three patients".
  - For a `genetic_context` this means `LOSS_OF_FUNCTION`, germline, biallelic.
- **Genotype–phenotype.** Only tentative.
  - Missense or hypomorphic genotypes are reported in milder or later-onset cases (PMID:26782016, 26548592).
  - Magri 2022: "The clinical outcome of MCMD patients seems to be influenced by CHKB molecular defects."
  - The same null allele can give different severity (PMID:31926838, 26006750).
- **Classification resources.** ClinVar carries multiple Pathogenic/Likely pathogenic *CHKB* entries, but counts were not retrieved. *CHKB* was not found in the local ClinGen gene-validity cache. Genomics England PanelApp lists *CHKB* on mitochondrial panels ([panel 112](https://panelapp.genomicsengland.co.uk/panels/112/gene/CHKB/)).
- **Allele frequency.** No founder allele frequency was found in gnomAD queries (not retrieved). Most variants are private.
- **Somatic vs germline.** Germline only.
- **Epigenetics and chromosomal abnormalities.** None disease-specific, apart from UPD and deletion as ways a variant becomes homozygous (PMID:36896673).

## 5. Environmental information

There are no causal environmental, lifestyle or infectious factors. Infections, general anaesthesia and strenuous exercise are **exacerbating** factors (§2). If these are curated under `environmental:`, use `EXACERBATES`, not `TRIGGERS`, and target a weakness or rhabdomyolysis node.

## 6. Mechanism / pathophysiology

### Ordered causal chain

1. **Biallelic *CHKB* loss-of-function variants** lead to absent or near-absent choline kinase β protein and activity in skeletal muscle. *Human: PMID:21665002, 23692895.*
2. **Loss of choline kinase activity** reduces the phosphorylation of choline to phosphocholine, which is the first committed step of the Kennedy/CDP-choline pathway. Choline accumulates and phosphocholine falls. *Mouse: PMID:19236939, "with an accumulation of choline and decreased amount of phosphocholine."*
3. **Reduced de novo PC synthesis**, together with a compensatory rise in PC breakdown (phospholipase C and A2), lowers phosphatidylcholine in muscle and in mitochondrial membranes.
   - Human: "phosphatidylcholine levels were decreased" (21665002).
   - Mouse: "Muscle mitochondria in rmd mice exhibited significantly decreased PC levels" (21750112); "attenuated PC biosynthesis and enhanced catabolism of PC" (19236939).
4. **Altered mitochondrial membrane lipid composition** leads to loss of inner membrane potential, respiratory-chain and ATP-synthase defects, and increased superoxide.
   - Mouse: "impaired respiratory chain enzyme activities", "decreased mitochondrial ATP synthesis", "increased superoxide production", "decreased coenzyme Q" (21750112).
   - Human cells: altered inner membrane potential (30986505).
   - Human heart: incomplete complex V assembly (26855408).
   - The link from step 3 to step 4 is inferred: every one of these papers frames it as a hypothesis.
5. **Branch A, mitochondrial dynamics:** reduced fission (DRP1, MFF, FIS1 down) leads to enlarged mitochondria. *Human myoblasts and muscle: PMID:34518586; DRP1 also down in PMID:36175989.*
6. **Branch B, quality control:** depolarised mitochondria are cleared by PINK1/Parkin mitophagy. This leaves central depletion and a residue of enlarged peripheral "megaconial" mitochondria, with lower mtDNA copy number in the mouse.
   - "selective autophagic elimination of mitochondria" (21750112).
   - In the human heart, mtDNA was not depleted (26855408).
   - The idea that mitophagy explains the peripheral distribution is a proposed model (review PMID:23945283).
7. **Branch C, sarcolemmal integrity:** low PC disrupts PI(4,5)P2 membrane clusters. That leads to failure of the α7β1 integrin complex (vinculin, α-actinin) and its actin attachment, and then to sarcolemmal fragility. *Mouse and cells: PMID:38749543.* Proteomics of human myoblasts points the same way, showing cytoskeletal and contractile protein changes (PMID:42449274; exploratory, n=1 patient).
8. **Energy failure plus membrane fragility** produce myofibre necrosis, poor regeneration and fat infiltration, i.e. a dystrophic myopathy.
   - "regeneration of hindlimb muscles of Chkb -/- mice was impaired when challenged with cardiotoxin" (19236939).
   - Fat accumulation and muscle injury (42292914).
9. **The dystrophic myopathy** leads to proximal weakness, raised CK, and progressive loss of ambulation. Under metabolic stress (illness, anaesthesia, exercise) it leads to acute deterioration or rhabdomyolysis.
10. **Extramuscular branches.** The mechanism is inferred, by analogy with membrane PC deficiency:
    - **Heart:** the same mitochondrial lesion leads to dilated cardiomyopathy and conduction block (26855408, 39465137).
    - **Brain:** reduced choline and phosphocholine substrate (low choline on MRS, 23692895) leads to intellectual disability, autism and seizures. The causal link is not demonstrated.
    - **Skin:** ichthyosis or psoriasiform dermatosis. The mechanism is unknown; a 2026 paper links CHKB to sphingolipid metabolism in psoriasis (PMID:42034255).

**Cell autonomy.** Restoring Chkb in muscle alone rescues the mouse: "confirming the cell-autonomous nature of the disease" (PMID:31216357).

### Checklist annotations (leads to verify)

- **Pathways:** Kennedy/CDP-choline pathway, GO:0006657; Reactome "Synthesis of PC". Mitophagy, GO:0000423†. Mitochondrial fission, GO:0000266†.
- **Molecular function:** GO:0004103 choline kinase activity (modifier DECREASED or LOSS_OF_FUNCTION); GO:0004305 ethanolamine kinase activity.
- **Processes:**
  - Phosphatidylcholine biosynthetic process, GO:0006656† (DECREASED).
  - Mitochondrial ATP synthesis coupled electron transport, GO:0042775† (DECREASED).
  - Integrin-mediated signalling or cell–matrix adhesion, GO:0007160† (DECREASED).
  - Skeletal muscle tissue regeneration, GO:0043403† (DECREASED).
- **Chemicals:** choline CHEBI:15354; phosphocholine CHEBI:295975 (both from UniProt Rhea); phosphatidylcholine CHEBI:64482†; coenzyme Q.
- **Cell types:** skeletal muscle fibre CL:0008002†; skeletal muscle myoblast CL:0000515†; cardiac muscle cell CL:0000746†.
- **Cellular component:** mitochondrial inner membrane GO:0005743†; sarcolemma GO:0042383†; cytosol GO:0005829 (where CHKB itself is).
- **Immune involvement:** none intrinsic. Note the separate acquired disorder IMMM in the differential diagnosis (§10).
- **Molecular profiling:**
  - Metabolomics and fluxomics of patient myotubes show lower phosphonucleotides, Krebs-cycle intermediates and ATP (34518586).
  - Proteomics shows 218 differentially abundant proteins, mostly reduced (42449274).
  - No GEO transcriptome dataset specific to this disease was identified.

## 7. Anatomical structures affected

- **Primary:** skeletal muscle (UBERON:0001134†). Proximal and limb-girdle pattern; facial weakness per OMIM synopsis.
  - Muscle MRI: "involvement mainly of the quadriceps femoris, sartorius, and adductor magnus, with selective sparing of the gracilis, hamstrings, and adductor longus and brevis" (PMID:26548592).
  - Relative sparing of adductor longus and extensor digitorum longus (PMID:31926838).
  - Distribution is bilateral and symmetric.
- **Secondary:**
  - Heart (UBERON:0000948): dilated cardiomyopathy, conduction system. Novel cardiac MRI findings are reported (PMID:34962344).
  - Brain (UBERON:0000955): intellectual disability, autism, seizures. Structural MRI is usually normal.
  - Skin (UBERON:0002097): ichthyosis or psoriasiform lesions.
  - Peripheral nerve: one case with neurogenic EMG and biopsy (PMID:26006750).
  - Leukocytes: Jordans anomaly; giant mitochondria visible in lymphocytes (PMID:36896673).
- **Subcellular:** mitochondria (enlarged, peripheral, with complex cristae); mitochondrial inner membrane; sarcolemma.

## 8. Temporal development

- **Onset.**
  - CMD form: congenital or early infancy, with hypotonia and delayed milestones (OMIM synopsis: "onset at birth").
  - LGMD form: adolescence, after normal early motor development (GeneReviews).
  - Adult form: adulthood (PMID:26782016).
- **Progression.** Slow, with plateaus. Loss of ambulation typically comes in late childhood or adolescence.
  - OMIM follow-up of the 1998 patients: survivors aged 29 and 22; one died at 23; one died of DCM at 13.
  - Cardiomyopathy can appear in the first or second decade.
- **Episodic features.** Acute deterioration with intercurrent illness or anaesthesia; rhabdomyolysis in the mild form.
- **Remission.** None.
- **Critical windows.** Cardiac surveillance from diagnosis onward. Peri-operative care around anaesthesia.

## 9. Inheritance and population

- **Inheritance:** autosomal recessive (HP:0000007). GeneReviews: "CHKB-MD is inherited in an autosomal recessive manner."
- **Penetrance and expressivity:** apparently complete for biallelic null genotypes. Expressivity varies, including within families (4 of 14 families in PMID:26067811).
- **Anticipation, germline mosaicism:** none reported.
- **Prevalence:** ultra-rare.
  - Reported counts: 21 cases (2015, PMID:26006750), 35 (2021, PMID:33712684), 47 (GeneReviews 2023), 49 (PMID:36896673). The Iranian series (13 patients, 2023) raises the total to probably more than 60.
  - No population prevalence estimate exists.
  - GARD's "~1,000 US" figure for ORPHA:521305 is not a sourced estimate and should not be used.
  - `prevalence_class: ULTRA_RARE`, `measure_type: CASES_IN_LITERATURE`.
- **Populations and geography.**
  - Turkey (10 of 11 unrelated families in PMID:21665002; 14 families in PMID:26067811); Japan (the original cohort); Iran (13); India (5.5% of genetically confirmed CMD in one Indian centre, PMID:33712684); also UK, Spain, Italy, China and Sri Lanka.
  - Concentrated where consanguinity is high.
- **Sex ratio:** no sex bias is expected or reported.
- **Carrier frequency and founder alleles:** not established. c.598del recurs in Chinese patients (PMID:31926838), but no founder effect has been demonstrated.

## 10. Diagnostics

- **Muscle biopsy (the key test).** Enlarged mitochondria at the periphery and a central sarcoplasm devoid of mitochondria, on NADH-TR, SDH, COX and modified Gomori trichrome stains and on electron microscopy. COX-deficient fibres and myopathic or dystrophic changes also occur.
  - "Megaconial pathology was considered pathognomonic of congenital muscular dystrophy due to biallelic pathogenic variants in CHKB" (PMID:39475687).
  - Sarcolemmal utrophin overexpression has been noted (PMID:25187204).
- **Laboratory.**
  - CK mildly to moderately raised; lactate and AST sometimes raised.
  - Reduced CHKB enzyme activity in muscle.
  - Respiratory-chain complex I and V deficits in some patients.
  - Blood smear for Jordans anomaly.
  - Giant mitochondria in immortalised lymphocytes when no muscle sample is available (PMID:36896673).
- **Imaging.**
  - Muscle MRI: quadriceps, sartorius and adductor magnus involved; gracilis, hamstrings and adductor longus/brevis spared.
  - Brain MRI usually normal. MRS may show low choline.
  - Echocardiography or cardiac MRI and ECG for cardiomyopathy and conduction block.
- **EMG.** Usually myopathic. Neurogenic in one case.
- **Genetic testing.**
  - Exome or genome sequencing, or a CMD/LGMD panel that includes *CHKB*. Many cases were diagnosed by WES (PMID:25187204, 25740612, 24997086).
  - Add CNV analysis (deletions) and SNP-array or UPD testing when a variant looks homozygous in a child of non-consanguineous parents.
  - Use RNA studies for intronic variants (PMID:36175989, 41026188).
  - mtDNA testing is not causal, but it is often sent because of the mitochondrial biopsy findings.
- **Diagnostic criteria.** No formal criteria. GeneReviews: diagnosis is "established in a proband with suggestive findings and biallelic loss-of-function pathogenic variants in CHKB."
- **Differential diagnosis.**
  - Dystrophinopathy, dystroglycanopathy and myotonic dystrophy (PMID:26548592).
  - Rett syndrome or atypical Rett (PMID:33712684).
  - Primary mitochondrial myopathies.
  - Other phospholipid-synthesis disorders.
  - TRAPPC11-CMD.
  - **Immune-mediated megaconial myopathy (IMMM):** acquired, adult onset (19–45 years), necrotizing, responsive to immunotherapy, *CHKB*-negative (PMID:39475687).
  - Hypotonia–cystinuria syndrome mimic (PMID:35707590).
  - Late-onset megaconial myopathy in *Pak1/Pak2*-deficient mice is a model-only differential (PMID:30791960).
- **Screening.** No newborn screening. Cascade carrier testing is possible once the familial variants are known.

## 11. Outcome / prognosis

- **Mortality** is driven by dilated cardiomyopathy.
  - GeneReviews: 14/47 with DCM, 5 deaths from heart failure, 1 heart transplant.
  - Haliloglu: two sibling deaths, at 2 years 1 month and 7 years 4 months.
  - Some patients survive into their 20s. Adult-form patients are well at 37–40.
- **Morbidity:** loss of ambulation, severe intellectual disability with absent speech, autism, scoliosis.
- **Prognostic factors:** presence of cardiomyopathy, and genotype (null versus hypomorphic), the latter tentatively.
- **Quality of life:** no formal measures exist.

## 12. Treatment

- **No disease-modifying therapy is approved.** GeneReviews: "There is no cure for CHKB-MD." Supportive care is multidisciplinary: neurology, orthopaedics, physical, occupational and speech therapy, cardiology, dermatology, and genetics.
- **Cardiac care.**
  - Standard heart-failure pharmacotherapy.
  - Heart transplantation (PMID:26855408).
  - Cardiac resynchronization therapy proposed for conduction block (PMID:39465137, a single case).
- **Dermatological.** Ustekinumab (an anti-IL-12/23 monoclonal antibody) worked in one patient with ichthyosis-like or psoriasiform scaling: "successfully responded to ustekinumab" (PMID:39143029). Single case.
- **Substrate supplementation (experimental).**
  - Citicoline (CDP-choline) was tried in a patient (Castro-Gago 2018, PMID:29923598; Spanish-language paper with no abstract, so the outcome is unverified).
  - The rationale is from mice: "Injection of CDP-choline increased PC content of hindlimb muscle and decreased creatine kinase activity in plasma" (PMID:19236939).
- **Gene therapy (preclinical).**
  - AAV6-Chkb given intramuscularly after onset rescues the rmd mouse (PMID:31216357).
  - Systemic AAV9-CHKB (human CHKB) at three doses made treated mice "biochemically and phenotypically indistinguishable from the wild type mice" (PMID:42292914, 2026).
  - AAV upregulation of CHKA is an alternative strategy (PMID:31216357).
- **Clinical trials:** none found. ClinicalTrials.gov was not exhaustively searched.
- **Avoid:** strenuous exercise and viral infections. Take anaesthetic precautions.
- **NCIT leads (verify; must sit under C25218):**

  | Intervention | NCIT lead |
  |---|---|
  | Physical therapy | NCIT:C15302 |
  | Supportive care | NCIT:C15747 |
  | Genetic counseling | NCIT:C15240 |
  | Gene therapy | NCIT:C15238 (`therapeutic_modality: GENE_THERAPY`) |
  | Pharmacotherapy (ustekinumab, citicoline) | NCIT:C15986, with ustekinumab and citicoline as `therapeutic_agent` |
  | Heart transplantation | NCIT:C15289 Organ Transplantation, or a specific heart-transplant term† |

## 13. Prevention

- **Primary:** genetic counseling. The recurrence risk is 25% per pregnancy for carrier parents. Carrier testing, prenatal diagnosis and preimplantation genetic testing are possible once the variants are known (GeneReviews).
- **Secondary:** early molecular diagnosis, and cardiac surveillance from diagnosis.
- **Tertiary:** avoid exercise and infection triggers, anaesthetic precautions, orthopaedic and respiratory care.
- **Vaccination:** no disease-specific vaccine. Routine vaccination is sensible given that viral infections exacerbate the disease, but this is inferred, not studied.

## 14. Other species / natural disease

- No naturally occurring animal disease was identified (OMIA not searched in depth).
- **Orthologues:** mouse *Chkb* (the rmd spontaneous deletion); also present in rat and zebrafish (not verified).
- The pathway is conserved: a two-gene choline kinase family (Chka/Chkb) in mammals.
- No zoonotic relevance.

## 15. Model organisms

| Model | Genotype | Recapitulation | Limitations | PMID |
|---|---|---|---|---|
| **rmd mouse** (rostrocaudal muscular dystrophy; *Mus musculus*, NCBITaxon:10090) | Spontaneous 1.6-kb intragenic *Chkb* deletion, recessive | "rapidly progressive muscular dystrophy and a neonatal forelimb bone deformity"; dystrophy "in an unusual rostral-to-caudal gradient" | Hindlimb-predominant, which does not match the human proximal pattern; no intellectual disability or cardiomyopathy reported; forelimb bone deformity has no human counterpart | 16371353 |
| rmd mouse, mitochondrial studies | same | Megaconial peripheral mitochondria, low mitochondrial PC, respiratory-chain and ATP defects, ROS, PINK1/Parkin mitophagy | Mouse mtDNA was depleted; the human heart was not (26855408) | 21750112, 19236939 |
| *Chkb*−/− mouse (rescue and gene therapy) | Knockout or rmd | Weakness, fibre atrophy, megaconia, intramyocellular fat; integrin complex failure; rescued by a muscle transgene, AAV6 or AAV9 | Preclinical only | 31216357, 38749543, 42292914 |
| *Chkb*−/− bone | same | Radius and ulna growth-plate defect; phosphocholine down ~75% in chondrocytes | Not a human disease feature | 24637075 |
| Patient primary myoblasts and fibroblasts (in vitro) | Human biallelic *CHKB* | Abnormal mitochondrial network, low fission proteins, low ATP, membrane-potential defect, proteome remodelling | Few patients (n=1 in proteomics) | 34518586, 30986505, 42449274 |
| Immortalised patient lymphocytes | Human | Giant mitochondria, low CHKB expression | Diagnostic use only | 36896673 |
| *Pak1/Pak2* double knockout (differential) | Mouse | Late-onset megaconial myopathy without *Chkb* mutation | A different gene, so it shows megaconia is not exclusive to CHKB | 30791960 |

Resources: MGI (*Chkb* rmd allele), IMSR/JAX.

---

## Key references (PMID)

- **Gene discovery:** 21665002 (Mitsuhashi 2011 AJHG); 9427222 (Nishino 1998 Muscle Nerve; not retrieved, citation per OMIM)
- **Review / GeneReviews:** 37011121 (Chan & Nishino 2023); 23945283 (Mitsuhashi & Nishino 2013)
- **Clinical series:** 26067811 (Haliloglu 2015, n=15); 37393748 (Zemorshidi 2023, n=13); 33712684 (Bardhan 2021, n=5); 23692895 (Quinlivan 2013, n=3); 31926838; 36175989; 26548592 (MRI); 25187204; 26006750; 26855408 (heart); 39465137 (DCM plus conduction block); 36896673 (UPD/deletion); 39143029 (ustekinumab)
- **Adult allelic form:** 26782016 (Brady 2016)
- **Mechanism:** 21750112; 19236939; 34518586; 30986505; 38749543; 42449274
- **Models and therapy:** 16371353; 31216357; 42292914; 24637075
- **Differential:** 39475687 (IMMM); 30791960

**Web sources:**
- [MSeqDR disease 00412](https://mseqdr.org/MITO2023/diseases/00412)
- [GARD 17956](https://rarediseases.info.nih.gov/assets/singles/17956.json)
- [Global Genes: proximal myopathy with focal depletion of mitochondria](https://globalgenes.org/?p=614506)
- [MeSH C563453](https://meshb.nlm.nih.gov/record/ui?ui=C563453)
- [MalaCards](https://malacards.org/card/proximal_myopathy_with_focal_depletion_of_mitochondria) (returned 403)
- [GeneReviews biopsy figure](https://www.ncbi.nlm.nih.gov/books/NBK589929/bin/chkb-md-skeletal_muscle_biopsy.pdf)
- [PanelApp CHKB, panel 112](https://panelapp.genomicsengland.co.uk/panels/112/gene/CHKB/)
- [PanelApp CHKB, panel 539](https://panelapp.genomicsengland.co.uk/panels/539/gene/CHKB/)
- [OMIM 602541 mirror](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/602541)
- [UniProt Q9Y259](https://rest.uniprot.org/uniprotkb/Q9Y259.txt)
- Europe PMC REST API (abstracts)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 32 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 6 |
| Quoted claims found in source | 6 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 32 |
| On topic | 28 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 70 |
| Resolved | 63 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 7 |
| Terms whose name was checked | 10 |
| Terms named correctly | 6 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `GO:0005829` (2 mentions) - the report calls it "where CHKB itself is"; GO calls it **cytosol**
- `CHEBI:295975` (1 mention) - the report calls it "both from UniProt Rhea"; CHEBI calls it **choline phosphate(1-)**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0002097` (1 mention) - the report calls it "Skin"; UBERON calls it **skin of body**, and lists "skin" among its other names
- `NCIT:C15238` (1 mention) - the report calls it "therapeutic_modality: GENE_THERAPY"; NCIT calls it **Gene Therapy**, and lists "Molecular Biology, Gene Therapy" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `ORPHA`, `Rhea`.