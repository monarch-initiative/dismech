---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-16T09:28:30.810480'
end_time: '2026-11-16T09:30:38.574055'
duration_seconds: 127.76
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: ZDHHC9-Related X-Linked Intellectual Disability
  mondo_id: MONDO:0010427
  category: Mendelian
  causal_genes: ZDHHC9
  omim_id: OMIM:300799
  synonyms: MRXSR; intellectual disability, X-linked syndromic, Raymond type
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
  web_search_requests: 12
  num_turns: 15
  total_cost_usd: 1.8886894000000005
  session_id: 09dd022c-1a08-4136-94c7-7c1d43a0ca70
  stop_reason: end_turn
  permission_denials: 1
  denied_tools:
  - Bash
  assistant_text_blocks: 1
citation_count: 20
reference_validation:
  total_references: 17
  verified: 17
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 17
  on_topic: 11
  off_topic: 1
  off_topic_references:
  - PMID:25984423
  needs_review: true
  validator_version: 0.6.0
term_validation:
  total_terms: 7
  verified: 6
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 4
  labels_matching: 4
  unresolvable_prefixes:
  - OMIM
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** ZDHHC9-Related X-Linked Intellectual Disability
- **MONDO ID:** MONDO:0010427 (if available)
- **Causal gene(s):** ZDHHC9
- **OMIM:** OMIM:300799
- **Synonyms:** MRXSR; intellectual disability, X-linked syndromic, Raymond type
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **ZDHHC9-Related X-Linked Intellectual Disability** covering all of the
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

I have the core literature and am writing the report now.

# ZDHHC9-Related X-Linked Intellectual Disability: Research Report

**Scope.** This report covers MONDO:0010427 / OMIM:300799 (intellectual disability, X-linked syndromic, Raymond type; MRXSR). The causal gene is **ZDHHC9** at Xq26.1. It encodes zinc finger DHHC-type palmitoyltransferase 9, a Golgi enzyme that adds palmitate to proteins and works in a complex with the accessory protein GCP16 (GOLGA7).

**How far to trust this report:**
- It was assembled from web-search summaries of abstracts and PMC records. I did not read the full texts.
- Quoted phrases are as the search tools returned them. Check each one against `references_cache/` with `just fetch-reference` before using it as a snippet.
- Ontology CURIEs below are **suggestions only**. Under the repo's rule that every CURIE is read from a source in the step it is written, each one must be looked up with OAK or the term caches before it is bound. I give labels without IDs wherever I could not check them.
- I could not inspect the existing draft `kb/disorders/ZDHHC9-Related_X-Linked_Intellectual_Disability.yaml`, because the read was blocked by a permission rule.

---

## 1. Disease information

**Overview.** This is X-linked intellectual disability (XLID) in hemizygous males, caused by loss-of-function variants in ZDHHC9. ZDHHC9 was the first XLID gene found to encode an enzyme that makes a posttranslational modification.

**Core phenotype:**
- Mild to moderate intellectual disability
- Speech and oromotor dyspraxia
- Epilepsy resembling rolandic epilepsy
- Hypoplastic or dysplastic corpus callosum, with smaller thalamus and striatum

A marfanoid habitus was described in the original families but is inconsistent across later reports.

**Identifiers:**
- OMIM: 300799 (phenotype); 300646 (gene)
- MONDO: MONDO:0010427
- HGNC: ZDHHC9 is hgnc:18475. Verify this against `cache/hgnc/terms.csv` before binding it.
- UniProt: Q9Y397 (human); P59268 (mouse Zdhhc9)
- Orphanet and ICD-11: not confirmed in this search. Look them up via `ORPHA:` in the structured cache. ICD-10 F78/Q-codes for syndromic XLID are generic.

**Synonyms:** MRXSR; mental retardation, X-linked, syndromic, Raymond type; X-linked intellectual disability with marfanoid habitus (used historically).

**Data provenance.** The information comes from aggregated, published family and case reports (about 16–20 families) and a few cohort studies. There are no EHR-derived data.

## 2. Etiology

- **Cause:** germline hemizygous variants in ZDHHC9 in males. This is a purely genetic, monogenic disorder.
- **Variant spectrum:** frameshift, splice-site, nonsense, missense, intragenic deletions, and at least one recurrent de novo missense change (p.Arg96Trp).
- **Environmental, protective and gene-environment factors:** none reported.
- **Modifier genes:** none reported. Phenotypes vary even within families, but no modifier has been identified.

**Key studies:**
- **Raymond et al. 2007, AJHG (PMID:17436253).** Screened 250 XLID families and found 4 with ZDHHC9 variants: one frameshift, one splice-site, and two missense changes at conserved residues. None of the four was found in 445 control samples. The search result describes ZDHHC9 as "a palmitoyltransferase that catalyzes the posttranslational modification of NRAS and HRAS."
- **Masurel-Paulet et al. 2014, Am J Med Genet A 164A:789–95 (PMID:24357419).** Found p.Arg298* by sequencing all X-chromosome exons. The variant cosegregated with mild ID and a dysplastic corpus callosum, with no marfanoid habitus or facial dysmorphism.
- **Han et al. 2017, Eur J Med Genet (PMID:28687527; check this PMID).** The first sporadic case, a de novo p.Arg96Trp in a Korean boy. He had global developmental delay but no marfanoid habitus, structural brain anomaly or epilepsy.
- **Schirwani et al. 2018, Am J Med Genet A 176:1238–44 (PMID:29681091).** Reported four patients: three with an intragenic deletion found by array CGH, and one with a de novo missense variant (the first recurrent mutation). In this cohort the patients showed "elongated, down-slanting palpebral fissures and a high hairline", and marfanoid habitus and seizures were absent. The authors counted 11 pathogenic variants reported to date.
- **Mir et al. 2023, BMC Med Genomics (DOI 10.1186/s12920-023-01680-y; PMID not retrieved).** A novel ZDHHC9 p.Leu189Pro in an Iranian XLID family.
- **2023 Am J Med Genet A paper, "ZDHHC9 X-linked intellectual disability: Clinical and molecular characterization" (PMID not confirmed).** A literature review plus a 13-year-old with a splice variant. It states that only 16 families had been described.

## 3. Phenotypes

The HPO labels below are candidates. Resolve the IDs with `runoak` before binding.

| Phenotype | Frequency / notes | Candidate HPO label | Key source |
|---|---|---|---|
| Intellectual disability, mild–moderate | Essentially all males | Intellectual disability, mild / moderate | PMID:17436253, PMID:24357419 |
| Global developmental delay (in early childhood) | Common | Global developmental delay | PMID:28687527 |
| Speech and oromotor dyspraxia | Consistent in the Baker cohort | Developmental verbal dyspraxia / oral-motor apraxia; Delayed speech and language development | PMID:25984423* |
| Epilepsy, rolandic-like (centrotemporal spikes) | 7 of 9 males (Baker 2015); absent in Schirwani's cohort | Seizure; EEG with centrotemporal spikes | PMID:25984423* |
| Corpus callosum hypoplasia or dysplasia | Frequent on MRI | Hypoplasia of the corpus callosum | PMID:25984423*, PMID:24357419 |
| Reduced thalamic and striatal volume | Cohort MRI finding | (thalamus/striatum morphology terms) | PMID:25984423* |
| Reduced inhibitory control / attention deficit | Separated ZDHHC9 cases from IQ-matched XLID controls | Attention deficit / impulsivity terms | PMID:25984423* |
| Marfanoid habitus | 3 of 4 original families; inconsistent later | Marfanoid habitus | PMID:17436253 |
| Facial features (long down-slanting palpebral fissures, high hairline) | Some patients | Downslanted palpebral fissures; High anterior hairline | PMID:29681091 |
| Hypotonia | Seen in the mouse model; rarely reported in humans | Hypotonia | PMID:29944857 (mouse) |

\* **Baker et al. 2015**, "Epilepsy, cognitive deficits and neuroanatomy in males with ZDHHC9 mutations", *Ann Clin Transl Neurol* 2(5):559–569, PMC4435709. The PMID was not returned by the search; 25984423 is a guess and **must be confirmed**. Its findings:
- 7 of 9 males had epilepsy, with seizure histories and EEG features resembling rolandic epilepsy.
- Speech and non-speech oromotor deficits were scored on the VMPAC by raters blind to the genetic diagnosis.
- Inhibitory control was reduced.
- Consistent neuroanatomical findings were "thalamic and striatal volume reductions and hypoplasia of the corpus callosum".

**Onset and course:**
- Onset is congenital or in infancy (developmental delay).
- Seizures start in childhood. By analogy with rolandic epilepsy they may remit, but this is not documented specifically for ZDHHC9.
- The course is static and non-progressive.

**Quality of life:** no formal QoL studies were found. The main functional burdens are lifelong ID and speech impairment.

## 4. Genetic and molecular information

- **Gene:** ZDHHC9 (Xq26.1). The protein is a 4-transmembrane DHHC palmitoyl acyltransferase. The DHHC cysteine-rich domain is catalytic.
- **Inheritance:** X-linked (HP:0001417 X-linked inheritance; verify). Most variants are inherited from carrier mothers who are generally unaffected; de novo cases also occur (PMID:28687527, PMID:29681091).
- **Variant classes:**
  - Truncating: frameshift, nonsense p.Arg298*, splice-site
  - Missense: p.Arg96Trp (recurrent), p.Arg148Trp (from the original 2007 families; check this), p.Leu189Pro
  - Intragenic deletions (PMID:29681091)

  Missense and nonsense variants cluster at arginines in cytoplasmic domains, which the 2023 review suggests may be mutational hotspots.
- **Functional consequence: loss of function.**
  - Mitchell et al. 2014, J Biol Chem 289:18582–92 (PMID:24811172): the XLID alleles lower the steady-state level of the palmitoyl-zDHHC9 autoacylation intermediate, and the alleles do this "by distinct mechanisms".
  - Later work found that the disease variants reduce protein stability and reduce DHHC9–GCP16 complex formation (PMC10076531; PMID not retrieved).
- **Population frequency:** these are rare private variants. gnomAD data were not retrieved, and the hemizygous counts for listed variants should be checked there.
- **Epigenetics and chromosomal anomalies:** no disease-specific epigenetic data were found. Intragenic and Xq26 CNVs are detectable by CMA.
- **Gene-disease validity:** a ClinGen classification was not confirmed. Check with `just list-gene-validity` or the `CGGV:` cache, and copy any tier from there; do not assign one.

## 5. Environmental information

No environmental, lifestyle, or infectious contributors are known. This section does not apply.

## 6. Mechanism and pathophysiology

**Ordered causal chain.** Steps marked "(inferred)" are not demonstrated in humans.

1. A hemizygous ZDHHC9 loss-of-function variant **leads to** absent or unstable ZDHHC9 protein, or to reduced autopalmitoylation and catalytic activity (PMID:24811172).
2. Loss of ZDHHC9 activity **results in** less DHHC9–GCP16 complex formation and stability. GCP16 stabilizes DHHC9 and is not itself catalytic (Yang et al. 2024, NSMB 31:436–446, PMID:38182928). Palmitoylation of DHHC9 at C24, C25 and C288 is required for its activity.
3. Reduced complex activity **leads to** under-palmitoylation of its substrates. From here the mechanism branches:
   - **3a. Neuronal branch.** Less palmitoylation of H/N-Ras **leads to** impaired dendrite outgrowth, and less palmitoylation of TC10 (RHOQ) **leads to** fewer inhibitory (GABAergic) synapses. This was shown in rat/mouse hippocampal cultures (Shimell et al. 2019, Cell Rep 29:2422; DOI 10.1016/j.celrep.2019.10.065; PMID to confirm).
   - **3b. Oligodendrocyte branch.** Less palmitoylation of myelin proteins (MBP, and also MAG, and in some reports MOG and PLP) **leads to** abnormal oligodendrocyte morphology and failure to target Golgi outposts. That in turn **results in** abnormal myelination: unmyelinated large axons, hypermyelinated small axons, and impaired compaction. This comes from mouse KO data (Glia 2025;73(7):1452–66, PMID:40105030; eLife reviewed preprint 97151). ZDHHC9 is the palmitoyltransferase most highly expressed in oligodendrocytes, and it is about 2-fold enriched in the corpus callosum.
   - **3c.** The KO also shifts the balance of mature oligodendrocyte subtypes (MOL5/6 up, MOL2/3 down) and lowers expression of lipid and cholesterol synthesis genes (PMID:40105030).
4. The 3b/3c changes **lead to** reduced white-matter and corpus callosum volume. This is shown in mice (PMID:29944857) and matched by human MRI (Baker 2015).
5. Fewer inhibitory synapses (3a) plus disrupted connectivity **lead to** an excitation/inhibition imbalance and network hyperexcitability **(inferred)**. Clinically this appears as rolandic-like epilepsy; Zdhhc9 KO mice show seizure-like activity.
6. Altered thalamo-cortical and striatal circuitry plus callosal hypoplasia **lead to** ID, oromotor dyspraxia and reduced inhibitory control **(inferred link)**.

**Suggested ontology terms (to verify):**
- GO processes: protein palmitoylation; peptidyl-L-cysteine S-palmitoylation; protein-cysteine S-palmitoyltransferase activity (MF); dendrite morphogenesis; inhibitory synapse assembly; myelination; oligodendrocyte differentiation
- GO cellular component: Golgi apparatus
- CL cell types: oligodendrocyte; neuron; hippocampal pyramidal neuron; GABAergic neuron (postsynaptic partner)
- Not involved: metabolic, immune and tissue-damage mechanisms, apart from the lipid-synthesis gene changes in the mouse.

**Omics:** the only omics data are mouse corpus callosum transcriptomics and proteomics (PMID:40105030). No human omics datasets were found.

## 7. Anatomical structures affected

- **System:** central nervous system only. Skeletal habitus (marfanoid) is a secondary or inconsistent feature.
- **Candidate UBERON terms:** corpus callosum; thalamus; striatum; cerebral white matter; hippocampus (the in vitro model tissue); rolandic/centrotemporal cortex (EEG localization).
- **Subcellular:** Golgi apparatus, including Golgi outposts in oligodendrocyte processes.
- **Laterality:** bilateral or midline.

## 8. Temporal development

- Onset is congenital, recognized as developmental delay in infancy.
- Seizure onset is in childhood.
- The course is non-progressive and lifelong.
- No staging exists.
- The critical window is early myelination and synaptogenesis **(inferred)**.

## 9. Inheritance and population

- X-linked. Affected individuals are males; heterozygous females are generally unaffected carriers.
- Inherited cases are the majority, with some de novo.
- Expressivity is variable (marfanoid habitus, seizures and dysmorphism all vary).
- ZDHHC9 accounted for about 1.6% of the families in the 250-family XLID screen (4/250).
- No population prevalence estimate exists. Use `CASES_IN_LITERATURE` (about 16–20 families as of 2023) rather than inventing a rate.
- No founder effects, anticipation or consanguinity role are known.

## 10. Diagnostics

- **Genetic testing:** exome or genome sequencing, or an XLID/ID gene panel. Use CMA or array CGH to detect intragenic deletions (PMID:29681091). Test the mother for segregation.
- **MRI:** look for corpus callosum hypoplasia and reduced thalamic and striatal volumes.
- **EEG:** look for centrotemporal spikes.
- **Neuropsychology and speech assessment:** the VMPAC was used in the Baker cohort.
- **Biomarkers:** none.
- **Differential diagnosis:**
  - Other XLID genes
  - Marfan syndrome, if habitus is prominent. Patients do not meet Ghent criteria.
  - Lujan-Fryns (MED12)
  - Self-limited epilepsy with centrotemporal spikes (idiopathic)

## 11. Outcome and prognosis

- Lifespan is not reported to be reduced.
- Morbidity comes from lifelong ID, speech impairment and epilepsy.
- No prognostic biomarkers or natural-history studies exist.

## 12. Treatment

There is no disease-specific therapy and no clinical trials. Management is supportive. Suggested NCIT terms below must be verified:

| Need | Approach | Suggested NCIT term |
|---|---|---|
| Seizures | Antiseizure medication | Pharmacotherapy (NCIT:C15986), with the agent in `therapeutic_agent` |
| Speech / oromotor dyspraxia | Speech-language therapy | Speech language therapy (NCIT:C159273) |
| Development | Special education and developmental support; occupational therapy | Occupational therapy (NCIT:C121351) |
| Family | Genetic counseling | Genetic Counseling (NCIT:C15240) |

No published reports of specific antiseizure-drug responses were found.

## 13. Prevention

- Genetic counseling and carrier testing of female relatives.
- Prenatal diagnosis or PGT when the familial variant is known.
- There is no primary prevention and no newborn screening.

## 14. Other species and natural disease

- No naturally occurring animal disease was found; this needs checking in OMIA.
- The orthologs are conserved:
  - Mouse Zdhhc9 (UniProt P59268). The MGI ID must be looked up before binding.
  - Yeast Erf2–Erf4 is the functional counterpart of DHHC9–GCP16 for Ras palmitoylation (PMID:38182928).

## 15. Model organisms

| Model | Findings | Fidelity / limitations | Source |
|---|---|---|---|
| Zdhhc9 mutant/KO mouse | Smaller corpus callosum on MRI; hypotonia; reduced anxiety; altered Morris water maze performance | Recapitulates the white-matter phenotype. Seizure-like activity is attributed to this and later work, which the search did not confirm directly | Kouskou et al. 2018, Exp Neurol 308:35–46, PMC6104741, PMID:29944857 (confirm) |
| Zdhhc9 KO mouse, corpus callosum | Shifted MOL subtypes; reduced lipid/cholesterol synthesis genes; abnormal myelin compaction | Mouse only | PMID:40105030 (Glia 2025) |
| Zdhhc9 KO oligodendrocytes, micro-scale | MBP/MAG palmitoylation loss; unmyelinated large axons and hypermyelinated small axons | Preprint / reviewed preprint | eLife RP 97151; bioRxiv 2023.09.19.558291 |
| Hippocampal neuron culture (knockdown/KO) | Shorter dendrites (via Ras); fewer inhibitory synapses (via TC10) | In vitro; rodent | Shimell et al. 2019, Cell Rep |
| Cell-based enzymology and cryo-EM | Loss of autopalmitoylation for patient alleles; DHHC9–GCP16 structure (PDB 8HF3) | Biochemical | PMID:24811172; PMID:38182928 |

**Model limitations:**
- No mouse model reproduces the human oromotor dyspraxia or the rolandic EEG pattern.
- No human iPSC or organoid model was found.

---

## Items to verify before curation

- Confirm these PMIDs on PubMed: Baker 2015 (PMC4435709), Shimell 2019, Kouskou 2018 (29944857), Han 2017 (28687527), the 2023 AJMG review, Mir 2023, and the GCP16-stability paper (PMC10076531).
- Confirm the specific missense variants from the original 2007 families in the PMID:17436253 full text.
- Get ClinGen and Orphanet records through the structured caches.

## Sources
- [Raymond et al. 2007, PMC1852737](https://pmc.ncbi.nlm.nih.gov/articles/PMC1852737) · [PubMed 17436253](https://www.pubmed.gov/17436253/)
- [Baker et al. 2015, PMC4435709](https://pmc.ncbi.nlm.nih.gov/articles/PMC4435709)
- [Masurel-Paulet 2014 (PMID 24357419)](https://pesquisa.bvsalud.org/portal/resource/en/mdl-24357419)
- [Mitchell et al. 2014, PMC4140262](https://pmc.ncbi.nlm.nih.gov/articles/PMC4140262) · [PubMed 24811172](https://www.pubmed.gov/24811172/)
- [Han et al. 2017](https://read.qxmd.com/read/28687527/the-first-patient-with-sporadic-x-linked-intellectual-disability-with-de-novo-zdhhc9-mutation-identified-by-targeted-next-generation-sequencing)
- [Schirwani et al. 2018, PubMed 29681091](https://pubmed.ncbi.nlm.nih.gov/29681091/)
- [Kouskou et al. 2018, PMC6104741](https://pmc.ncbi.nlm.nih.gov/articles/PMC6104741)
- [Shimell et al. 2019 (DOAJ)](https://doaj.org/article/fb1d68dc9602431a9df8d9734febf116)
- [GCP16 stabilizes DHHC9 subfamily, PMC10076531](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10076531/)
- [Yang et al. 2024 NSMB](https://www.nature.com/articles/s41594-023-01183-5) · [PDB 8HFC](https://www1.rcsb.org/structure/8HFC)
- [Glia 2025, PubMed 40105030](https://pubmed.ncbi.nlm.nih.gov/40105030/) · [PMC12121472](https://pmc.ncbi.nlm.nih.gov/articles/PMC12121472)
- [eLife reviewed preprint 97151](https://elifesciences.org/reviewed-preprints/97151.pdf) · [bioRxiv 2023.08.08.552342](https://www.biorxiv.org/content/10.1101/2023.08.08.552342.full.pdf)
- [Mir et al. 2023 BMC Med Genomics](https://link.springer.com/content/pdf/10.1186/s12920-023-01680-y.pdf)
- [ZDHHC9 XLID clinical and molecular characterization (2023)](https://ersearch2.cvtisr.sk/vufind/SummonRecord/FETCH-LOGICAL-c3642-21442fb2e966bbb3414690b51b25cb2ce3944377fe2948af4cb55b6c9ad2ddad3)
- [DisGeNET Raymond-type XLID](https://www.disgenet.org/browser/1/1/1/51114/_a/_b./)

## Reference Validation

Checked with `linkml-reference-validator` 0.6.0.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 17 |
| On topic | 11 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:25984423` (5 mentions) - Diagnosis of idiopathic pulmonary fibrosis: Current issues.
  - shared terms: none

Weighed against this report's own most characteristic terms: `zdhhc9`, `found`, `callosum`, `corpus`, `xlid`, `gene`, `variant`, `epilepsy`, `familie`, `habitus`, `gcp16`, `genetic`, `mouse`, `reduced`, `marfanoid`, `speech`, `x-linked`, `baker`, `dhhc9`, `seizure`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 7 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 4 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 0 |

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.

6 of 7 terms resolved to a current term; the rest could not be looked up either way.