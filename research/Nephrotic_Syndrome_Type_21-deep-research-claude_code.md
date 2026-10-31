---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-15T11:20:25.013608'
end_time: '2026-10-15T11:22:54.077796'
duration_seconds: 149.06
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Nephrotic Syndrome Type 21
  mondo_id: MONDO:0032826
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
  web_search_requests: 2
  num_turns: 12
  total_cost_usd: 2.0240694
  session_id: 72a04544-6208-46ac-8c85-ab7323f2edb6
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  assistant_text_blocks: 2
citation_count: 13
reference_validation:
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 8
  on_topic: 5
  validator_version: 0.3.0
term_validation:
  total_terms: 33
  verified: 31
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 3
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: HP:0000007
    reported_labels:
    - 'ClinGen: "AR"; segregation consistent in families with parental DNA'
    ontology_label: Autosomal recessive inheritance
  labels_variant: 2
  unresolvable_prefixes:
  - CCID
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Nephrotic Syndrome Type 21
- **MONDO ID:** MONDO:0032826 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Nephrotic Syndrome Type 21** covering all of the
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

Reading the last cached reference, then checking for newer AVIL literature.

# Nephrotic Syndrome Type 21 (NPHS21; AVIL-related steroid-resistant nephrotic syndrome): research report

**Target:** Nephrotic syndrome, type 21 (MONDO:0032826) · **Category:** Mendelian · **Prepared:** 2026-10-15

> **Evidence base caveat.** Almost everything known about this disorder comes from one paper: Rao, Ashraf et al., *J Clin Invest* 2017 (PMID:29058690). It describes four variants in three probands from three families. ClinGen's 2024 re-curation states: *"This curation includes four variants (frameshift and missense) identified in three probands, all described in a single publication (Rao et al., PMID: 29058690). No additional evidence is available in the literature."* ClinGen classifies the gene–disease pair as **Limited**. One 2026 Indonesian cohort (PMID:42420527) lists AVIL among genes carrying a P/LP variant, but its abstract gives no per-patient detail. Many template sections therefore have **no disease-specific data**, and this report says so where that applies rather than borrowing from SRNS in general without saying so.

Quotes from PMID:29058690 are taken from the cached full text (`references_cache/PMID_29058690.md`). Quotes from ClinGen and GeneReviews come from the local cache files `CGGV_assertion_04806c21-…md` and `url_…NBK573219_.md`.

---

## 1. Disease information

**Overview.** NPHS21 is an autosomal recessive form of steroid-resistant nephrotic syndrome (SRNS). It is caused by biallelic loss-of-function variants in *AVIL*, which encodes advillin, an actin-regulatory protein in the gelsolin/villin family. In the two probands with clinical detail, nephrotic syndrome began in the first year of life, biopsy showed diffuse mesangial sclerosis (DMS), and kidney failure followed before age 3. Some patients also had extrarenal features: retinal dystrophy, deafness, cataract, microcephaly, intellectual disability and short stature.

- PMID:29058690: *"we identified recessive mutations in the gene encoding the actin-binding protein advillin (AVIL) in 3 unrelated families with SRNS."*
- ClinGen: *"Nephrotic syndrome type 21 (congenital nephrotic syndrome) is characterized by significant proteinuria during the first months or years of life, leading to generalized edema."*

**Identifiers**

| System | ID | Note |
|---|---|---|
| MONDO | MONDO:0032826 "nephrotic syndrome, type 21" | Verified against the ClinGen row |
| OMIM (phenotype) | 618594 | Cited by ClinGen and GeneReviews |
| OMIM (gene) | *613397 ADVILLIN; AVIL | [OMIM](https://omim.org/entry/613397) |
| HGNC | HGNC:14188 (written `hgnc:14188` in dismech) | |
| ClinGen GCEP | CGGV:assertion_04806c21-071c-4a74-96c2-ab89ef5ba0e0-2024-08-27T180000.000Z (CCID:008997) | AR, Limited, SOP10, re-evaluated 2024-08-27 |
| Orphanet | No disorder-specific ORPHA code found | Likely falls under a generic "genetic SRNS" grouping. Not verified, so do not bind |
| ICD-10-CM | N04.x (nephrotic syndrome), e.g. N04.1/N04.9 | Non-specific |
| ICD-11 | GB41 (nephrotic syndrome) | Non-specific |
| MeSH | D009404 Nephrotic Syndrome | Non-specific |

**Synonyms.** NPHS21; AVIL-related nephrotic syndrome; nephrotic syndrome caused by mutation in AVIL. The founding paper proposed **"NPHS25"**: *"We thereby identified recessive mutations in AVIL as a cause of recessive NS and introduce the term 'NPHS25' for this variant of monogenic SRNS."* OMIM and MONDO number it type 21. Expect this discrepancy in the literature.

**Data provenance.** All phenotype data are individual-patient data from research sequencing (3 probands), compiled by aggregate resources (OMIM, ClinGen, GeneReviews). There are no EHR-derived or registry data.

---

## 2. Etiology

- **Cause.** Germline biallelic (homozygous or compound heterozygous) *AVIL* variants. Proposed mechanism (ClinGen): *"The proposed mechanism of pathogenicity is loss of function."*
- **Genetic risk factors.** Parental consanguinity: the homozygous index family (A2438, Turkey) was consanguineous. Two of the three probands are of Turkish descent.
- **Environmental risk factors.** None known.
- **Protective factors.** None known, genetic or environmental.
- **Modifier genes.** None reported. The extrarenal phenotype varies between probands (retinal dystrophy in one; deafness, cataract, microcephaly and intellectual disability in another), but the paper did not exclude a second diagnosis in these consanguineous families. Treat the syndromic features as **attributed, not proven**.
- **Gene–environment interactions.** None described. In the podocyte model, EGF stimulation partly compensates for AVIL knockdown (see §6), but that is a cell-culture finding, not a clinical exposure.

---

## 3. Phenotypes

The denominator is tiny: the frequencies below are counts out of 3 probands, and clinical detail exists for only 2.

| Phenotype | Suggested HPO | Type | Onset / course | Frequency | Source |
|---|---|---|---|---|---|
| Steroid-resistant nephrotic syndrome | HP:0012588 Steroid-resistant nephrotic syndrome | Clinical/lab | Infantile (<1 yr); rapidly progressive | 3/3 | PMID:29058690 |
| Nephrotic-range proteinuria | HP:0000093 Proteinuria *(verify)* | Lab | Infancy | 3/3 (implied) | ClinGen summary |
| Generalized edema | HP:0007430 Generalized edema *(verify)* | Sign | Infancy | Not individually reported | ClinGen summary |
| Diffuse mesangial sclerosis | HP:0001967 Diffuse mesangial sclerosis | Histopathology | — | 2/2 biopsied | PMID:29058690 |
| Podocyte foot process effacement | HP:0031266 Podocyte foot process effacement | Ultrastructure | — | 1/1 with EM | PMID:29058690 |
| Kidney failure | HP:0003774 Stage 5 chronic kidney disease | Clinical | 22 months and 3 years | 2/2 with data | PMID:29058690 |
| Retinal dystrophy | HP:0000556 Retinal dystrophy | Sign | NR | 1/3 (A913_21, UK) | PMID:29058690 |
| Deafness (type not stated) | HP:0000365 Hearing impairment | Sign | NR | 1/3 (A2438_22) | PMID:29058690 |
| Cataract | HP:0000518 Cataract | Sign | NR | 1/3 | PMID:29058690 |
| Microcephaly | HP:0000252 Microcephaly | Sign | NR | 1/3 | PMID:29058690 |
| Intellectual disability | HP:0001249 Intellectual disability | Behavioral/cognitive | NR | 1/3 | PMID:29058690 |
| Short stature | HP:0004322 Short stature | Growth | NR | 1/3 (Table 1) | PMID:29058690 Table 1; GeneReviews |
| "Pervasive refusal syndrome" | No good HPO term; leave free-text or omit | Behavioral | NR | 1/3 | PMID:29058690 |

Key quotes (PMID:29058690):
- *"The renal histological analyses for individuals A2438_22 and A913_21 revealed diffuse mesangial sclerosis (DMS)"*
- *"The 2 individuals manifested signs of NS before 1 year of age and progressed to ESRD before 3 years of age"*
- *"Individual A2438_22 had severe SRNS combined with deafness, cataracts, microcephaly, and intellectual disability. Individual A913_21 had severe NS combined with retinal dystrophy and pervasive refusal syndrome."*
- The authors also describe a spectrum: *"A spectrum ranging from severe early-onset NS with DMS to a later-onset form with FSGS was observed here, as has also been described in phospholipase C ϵ1 (PLCE1) mutations."* The third proband (A2647_21) has no onset age or histology in Table 1, so the "later-onset FSGS" end of the spectrum is **not documented** for any specific AVIL patient.
- GeneReviews' Genetic SRNS Overview (NBK573219) lists AVIL's extrarenal features as *"Microcephaly, short stature, retinal dystrophy, cataracts, deafness, & DD (OMIM 618594)"*.

**Quality of life.** No disease-specific data. General pediatric SRNS and dialysis QoL literature applies only by extrapolation.

---

## 4. Genetic and molecular information

**Causal gene.** *AVIL* (advillin), 12q14.1, HGNC:14188, RefSeq NM_006576. It has six gelsolin homology (GH/S1–S6) domains and a C-terminal villin-type headpiece (HP).

**Reported variants** (all from PMID:29058690, Table 1)

| Proband (origin) | Genotype | cDNA | Protein | Type | Domain | ExAC homozygotes |
|---|---|---|---|---|---|---|
| A2438_22 (Turkey, consanguineous) | Homozygous; segregates (M, P het) | c.1273C>A | p.Leu425Met | Missense | GH4 | None (A = 5/120,708) |
| A913_21 (UK) | Compound het, confirmed in trans by TA cloning | c.404G>A + c.1964dupT | p.Arg135Gln + p.Phe656Valfs*7 | Missense + frameshift | GH2; truncates S6+HP | None |
| A2647_21 (Turkey) | Compound het; phase not assessed (parents NA) | c.1273C>A + c.1337G>A | p.Leu425Met + p.Arg446His | Missense ×2 | GH4 | p.Arg446His not present in ExAC |

- ClinVar lists p.Arg446His (RCV000845156) for SRNS ([ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/RCV000845156.1/)). Per-variant ACMG classifications in ClinVar were not reviewed for this report; check each before quoting a classification.
- p.Leu425Met occurs in two unrelated Turkish probands. That suggests a possible founder allele, but no haplotype analysis was done.
- **Origin:** germline. **Functional class:** loss of function (bundling lost for all alleles; binding and severing lost only for the truncating allele; see §6).
- **Gene–disease validity:** ClinGen **Limited** (Genetic 3.1 + Experimental 2.0 = 5.1 points). From the ClinGen record: *"This classification reflects the fact that the association has not yet been repeatedly demonstrated in both research and clinical diagnostic settings over time."*
- **Replication.** Fahlevi et al. 2026 (PMID:42420527) report that 9 of 60 Indonesian children with primary SRNS *"harbored pathogenic or likely pathogenic variants across 8 genes (CUBN, AVIL, TRPC6, INF2, COL4A4, LAMA5, INVS, and FGA)"*. The abstract does not give the AVIL genotype, zygosity, phenotype, or whether "microcephaly with short stature" belongs to that child. **Obtain the full text before using this as a second AVIL proband.**
- **Modifier genes, epigenetics, chromosomal abnormalities.** None reported. CNV analysis in the founding cohort found *"no deleterious CNV."*

---

## 5. Environmental information

There are no environmental, lifestyle or infectious factors. This is a monogenic disorder with infantile onset. Intercurrent infections and nephrotic complications (thrombosis, infection from hypogammaglobulinemia) are general features of nephrotic syndrome, not documented for AVIL patients.

---

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic germline *AVIL* variants** → advillin loses function. *(Human genetic; mechanism per ClinGen.)*
2. **Loss of F-actin bundling** by advillin. All three tested patient alleles (R135Q, L425M, F656Vfs*7) bundle poorly in a low-speed sedimentation assay. Only the truncating allele also loses actin binding and severing. *(In vitro, demonstrated.)*
   - *"in all 3 AVIL mutants … a majority of the actin filaments now appeared in the supernatant (S) fraction, demonstrating a severe defect in actin bundling."*
   - *"Whereas the WT AVIL and 2 mutants representing missense alleles showed normal actin-severing function, the truncating mutant exhibited a complete loss of the actin-severing ability of AVIL"*
   - Molecular-dynamics modelling suggests R135Q (GH2, near the type-2 Ca²⁺ site) and L425M (GH4, actin-binding α-helix) increase local flexibility *(computational)*.
3. **The interaction of advillin with PLCE1 and ARP2/3 is weakened.** AVIL colocalizes with PLCE1 and ARP3 at the podocyte periphery and lamellipodia, and co-immunoprecipitates with PLCE1, ACTR2 and ACTR3. *"the mutants Leu425Met and Phe656Valfs*7 … weakened this interaction"* *(in vitro, HEK293T)*. **Inferred step:** whether loss of bundling itself causes step 4, rather than some other property of the mutant protein, is not shown.
4. **PLCE1 is not recruited to lamellipodia and does not produce DAG.** On EGF stimulation, AVIL-depleted podocytes fail to recruit PLCE1 to ARP3-rich lamellipodia, and EGF-induced diacylglycerol (DAG) generation is blocked. Wild-type AVIL rescues this; none of the three patient alleles does. *(In vitro, human immortalized podocytes.)*
   - *"Knockdown of AVIL in human podocytes reduced actin stress fibers at the cell periphery, prevented recruitment of PLCE1 to the ARP3-rich lamellipodia, blocked EGF-induced generation of diacylglycerol (DAG) by PLCE1, and attenuated the podocyte migration rate (PMR). These effects were reversed by overexpression of WT AVIL but not by overexpression of any of the 3 patient-derived AVIL mutants."*
5. **ARP2/3-dependent lamellipodia formation fails and podocyte migration rate falls.** Epistasis places PLCE1 downstream of AVIL (PLCE1 overexpression rescues AVIL knockdown, but not the reverse) and ARP2/3 downstream of both (the inhibitor CK666 abolishes the pro-migratory effect). *(In vitro.)*
   - *"this increased PMR was ameliorated by inhibition of the ARP2/3 complex, indicating that ARP-dependent lamellipodia formation occurs downstream of AVIL and PLCE1 function."*
6. **Podocyte foot-process effacement and glomerular filtration barrier failure.** *(Inferred.)* The link from a culture migration defect to foot-process injury in vivo rests on PMR being used as an "intermediate phenotype" across monogenic SRNS. It has not been shown for AVIL: *"a defect in the podocyte migration rate (PMR) in cell culture has been established as a reliable intermediate phenotype in monogenic forms of SRNS"* (background statement). Human EM does show diffuse effacement in A2438_22.
7. **Clinical result.** Nephrotic-range proteinuria → hypoalbuminemia and edema → DMS → kidney failure in early childhood. *(Human clinical, n = 2.)*

**Branch (unexplained).** Extrarenal features (retina, lens, hearing, brain growth) are not mechanistically linked to *AVIL*. Advillin is otherwise known mainly from peripheral sensory neurons (see §15). There is no evidence connecting AVIL to the eye or inner ear.

**Shared pathway.** This chain converges on the **PLCE1** axis. PLCE1 (NPHS3) causes DMS/FSGS SRNS with a similar early-onset spectrum, so NPHS21 belongs with the actin-cytoskeleton / Rho-GTPase cluster of podocytopathies.

### Ontology suggestions

| Concept | Term | Modifier |
|---|---|---|
| Actin filament bundle assembly | GO:0051017 actin filament bundle assembly | DECREASED |
| Actin filament binding | GO:0051015 actin filament binding | DECREASED (truncating allele) |
| Actin filament severing | GO:0051014 actin filament severing *(verify label)* | DECREASED (truncating only) |
| PLCE1 activity | GO:0004435 phosphatidylinositol-4,5-bisphosphate phospholipase C activity | DECREASED |
| Lamellipodium assembly | GO:0030032 lamellipodium assembly | DECREASED |
| Podocyte migration | GO:0090521 podocyte cell migration | DECREASED |
| Arp2/3 complex-mediated actin nucleation | GO:0034314 *(verify)* | — |
| Cell type | CL:0000653 podocyte | — |
| Interacting genes | PLCE1 hgnc:17175; ACTR2, ACTR3 (look up HGNC IDs) | — |
| Chemical | diacylglycerol, CHEBI:18035 *(verify)* | DECREASED |

Not available for this disease: metabolomic, proteomic, transcriptomic, single-cell, spatial or CRISPR-screen data. There is no immune involvement; this is a primary podocytopathy and is not immune-mediated, which is consistent with steroid resistance.

---

## 7. Anatomical structures affected

- **Primary organ:** kidney, specifically the glomerulus. Suggested terms: UBERON:0002113 kidney, UBERON:0000074 renal glomerulus; glomerular visceral epithelium / podocyte layer *(look up the UBERON ID)*.
- **Cell:** podocyte (CL:0000653). AVIL was detected in cultured human podocytes and in WT1-positive podocytes of 2-day-old rat glomeruli: *"AVIL localized to the cytoplasm of podocytes in rat glomeruli."*
- **Subcellular:** lamellipodium (GO:0030027), actin cytoskeleton/stress fibers, focal adhesion (GO:0005925), cell cortex/periphery. Look up the GO CC IDs.
- **Secondary (in single patients):** retina, lens, inner ear (auditory system), brain (microcephaly, intellectual disability).
- **Laterality:** bilateral kidney involvement (systemic glomerular disease). Ocular laterality was not reported.

---

## 8. Temporal development

- **Onset:** infantile (<12 months) in 2/2 with data. The index homozygous patient had onset of nephrotic syndrome at about 6 months, according to Table 1. Re-read Table 1 before encoding: the column alignment is ambiguous in text extraction.
- **Progression:** rapid. Kidney failure at 22 months (A2438_22) and 3 years (A913_21).
- **Course:** progressive and lifelong. No spontaneous or treatment-induced remission has been reported.
- **Critical periods:** infancy. Early genetic diagnosis may spare children ineffective immunosuppression (general genetic-SRNS principle).
- **Stages:** the general CKD trajectory (nephrotic syndrome → CKD → kidney failure) applies. There are no disease-specific stages.

---

## 9. Inheritance and population

- **Inheritance:** autosomal recessive, HP:0000007 (ClinGen: "AR"; segregation consistent in families with parental DNA).
- **Penetrance and expressivity:** unknown. Expressivity appears variable for extrarenal features, n = 2–3.
- **Anticipation and mosaicism:** not applicable or not reported.
- **Founder effect:** possible for p.Leu425Met in Turkey (2 of 3 probands); not formally tested.
- **Consanguinity:** present in the homozygous family.
- **Epidemiology:** ultra-rare, about 3–4 reported probands worldwide. No prevalence or incidence estimate exists. Use `CASES_IN_LITERATURE` / `ULTRA_RARE` rather than a numeric band. Context: in a 1,780-family SRNS cohort, about 30% had a monogenic cause among the 26 genes known at the time (PMID:29058690, citing PMID:25467131 per the paper's reference list; verify). AVIL was found in 3 of about 800+ resequenced SRNS individuals.
- **Geography and sex:** Turkey (2), UK (1), probably Indonesia (1, unconfirmed). Sexes: 1 M, 2 F.
- **Carrier frequency:** not established. Population allele counts are very low (e.g. ExAC A = 5/120,708 for c.1273C>A). gnomAD v4 was not consulted for this report.

---

## 10. Diagnostics

- **Laboratory:** urine protein/creatinine ratio, serum albumin, lipids, creatinine/eGFR. These are generic nephrotic-syndrome tests; no AVIL-specific biomarker exists.
- **Biopsy:** DMS on light microscopy; diffuse foot-process effacement on EM.
- **Genetic testing (key test):** an SRNS multigene panel or exome sequencing. AVIL is listed in GeneReviews' syndromic genetic-SRNS gene table. Indonesian data argue for exome sequencing in early-onset or atypical SRNS: *"Genetic testing should be integrated into routine SRNS evaluation, especially in atypical presentations or early-onset of the disease"* (PMID:42420527). CMA, karyotype, FISH, mtDNA and repeat-expansion testing are not indicated for this gene. Because ClinGen rates the gene Limited, an *AVIL* finding should be interpreted cautiously and may be reported as a VUS-level gene.
- **Extrarenal work-up** (justified by the reported features): ophthalmology (fundus/ERG, slit lamp), audiology, head circumference, developmental assessment.
- **Differential diagnosis:**
  - Other DMS/early-onset SRNS genes: *PLCE1* (closest phenocopy, same pathway), *WT1* (Denys-Drash; genital and Wilms features), *LAMB2* (Pierson; microcoria).
  - Congenital nephrotic syndrome genes: *NPHS1*, *NPHS2*.
  - Other syndromic SRNS: *COQ2/COQ6/COQ8B* (SNHL, neurologic; CoQ10-responsive, so important to exclude), Galloway-Mowat genes (*WDR73*, *OSGEP*/KEOPS; microcephaly plus SRNS, a key phenocopy of the A2438_22 picture), *NUP107/NUP93*.
  - Secondary/infectious congenital NS (CMV, syphilis, toxoplasmosis).
- **Screening:** no newborn screening. Cascade carrier testing and prenatal or preimplantation testing are possible once familial variants are known.

---

## 11. Outcome and prognosis

- **Survival and mortality:** no data. Kidney failure is expected in early childhood.
- **Morbidity:** dialysis dependence; complications of nephrotic syndrome (edema, infection, thrombosis, dyslipidemia, growth failure); neurodevelopmental and sensory disability in syndromic cases.
- **Recurrence after transplant:** not reported for AVIL. Genetic SRNS generally has a low risk of post-transplant recurrence (GeneReviews).
- **Prognostic factors:** DMS histology and infantile onset predict rapid progression (inferred from the 2 cases and general DMS literature). No prognostic biomarkers exist.

---

## 12. Treatment

| Intervention | NCIT suggestion | Evidence for AVIL | Notes |
|---|---|---|---|
| Kidney transplantation | NCIT:C15289 Organ Transplantation *(used in draft; a more specific "Kidney Transplantation" NCIT term may exist, look up)* | A913_21 was transplanted; outcome not reported | GeneReviews: *"All genetic SRNS can be corrected with kidney transplantation."* |
| Dialysis (PD/HD) | Look up NCIT dialysis term | Implied by ESRD at <3 years | Bridge to transplant |
| RAAS blockade (ACE inhibitor) | NCIT:C15986 Pharmacotherapy + therapeutic_agent (ACE inhibitor class) | A2438_22 received an ACE inhibitor (Table 1) | Antiproteinuric; no outcome data |
| Supportive care (albumin infusion, diuretics, nutrition, thromboprophylaxis, vaccination) | NCIT:C15747 Supportive Care | General | — |
| Calcineurin inhibitors / steroids | — | **No AVIL data** | Monogenic SRNS rarely responds. In the Indonesian cohort, 53.3% of all SRNS (not AVIL-specific) responded to cyclosporin, so do not attribute that figure to AVIL |
| Genetic counseling | NCIT:C15240 Genetic Counseling | — | AR, 25% recurrence risk |

- **Pharmacogenomics, gene therapy, ASO/siRNA, cell therapy, clinical trials:** none for AVIL. No ClinicalTrials.gov trials target AVIL-SRNS.
- **Speculative targets:** the authors suggest the EGF–AVIL–PLCE1–ARP2/3 axis *"may represent drug targets for SRNS"*. This is hypothesis only.

---

## 13. Prevention

- **Primary:** none, beyond reproductive options.
- **Secondary:** early molecular diagnosis in infantile SRNS avoids unnecessary immunosuppression.
- **Tertiary:** standard CKD care (blood pressure, growth, bone mineral, anemia), plus infection and thrombosis prophylaxis in nephrotic syndrome.
- **Genetic counseling:** carrier testing of relatives; prenatal or preimplantation genetic testing for known familial variants.
- **Vaccines and public-health measures:** not applicable, beyond routine immunization of children with nephrotic syndrome or on dialysis.

---

## 14. Other species and natural disease

No naturally occurring AVIL-associated nephropathy is known in animals; no OMIA entry was found. Orthologs exist in mouse (*Avil*, MGI), rat (*Avil*, [RGD 620301](https://rgd.mcw.edu/rgdweb/report/gene/main.html?id=620301)) and zebrafish (*avil*, [ZFIN via Alliance](https://www.alliancegenome.org/gene/ZFIN:ZDB-GENE-060421-6683)). Leu425 is conserved back to *Ciona intestinalis* and Arg446 to *C. elegans* (Table 1). Not zoonotic.

---

## 15. Model organisms

| Model | Finding | Fidelity to NPHS21 |
|---|---|---|
| **Zebrafish *avil* CRISPR knockdown** (Rao 2017; reported in ClinGen) | *"our initial experiments did not show a larval edema phenotype"* | **Fails to recapitulate.** Candidate for a `FAILS_TO_RECAPITULATE` link or a `HUMAN_MODEL_MISMATCH` discussion. The authors attribute earlier positive SRNS zebrafish models to unreliable morpholinos |
| **Mouse *Avil* null / knock-in** (Hasegawa et al. 2007, *J Neurosci*; Avil-hPLAP knock-in) | Expression almost exclusively in peripheral sensory neurons. Null mice show shortened regenerative axon growth and reduced barrelette plasticity | **No kidney phenotype reported.** Glomerular phenotyping not described. Advillin-Cre lines are widely used sensory-neuron drivers; their expression also reaches autonomic neurons postnatally ([eNeuro 2018](https://www.eneuro.org/content/5/5/ENEURO.0077-18.2018)) |
| **Human immortalized podocytes** (Saleem line) with siRNA/shRNA knockdown and rescue | Loss of stress fibers, PLCE1 mislocalization, loss of DAG, reduced migration; WT rescues, patient alleles do not | In vitro mechanism model; migration rate is a proxy readout. Mechanism node at CELLULAR scale, extrapolated upward to TISSUE |
| **Recombinant protein assays** | Bundling, binding and severing defects (§6) | MOLECULAR |
| Related biochemistry | George et al. 2020, *Mol Biol Cell* (PMID:32520642): conserved F-actin-bundling residues in villin-type headpiece domains, tested in advillin | Supports headpiece-dependent bundling; not disease-specific |

**Gaps.** No podocyte-specific *Avil* conditional knockout. No patient iPSC-derived podocytes or kidney organoids. Whether there is real AVIL protein expression in the adult human glomerulus needs confirming; the Human Protein Atlas was not checked here.

---

## Key gaps and curation recommendations

1. **The single-publication evidence base** (ClinGen Limited) should appear in the entry's description, and the `gene_disease_validity` LIMITED row should be kept.
2. **Fetch the full text of PMID:42420527** to see whether a second AVIL proband (Indonesia) is described, with genotype and phenotype.
3. **The syndromic features are n = 1 each** and come from consanguineous families. Encode them as reported, without implying they are core features.
4. **Encode the zebrafish null result** as a negative model finding.
5. **Possible duplicate entry.** The worktree contains both `Nephrotic_Syndrome_Type_21.yaml` and `AVIL-Related_Steroid-Resistant_Nephrotic_Syndrome.yaml`. They appear to be the same disease (MONDO:0032826), and only one should be kept.
6. **CURIEs marked *(verify)*** above were not looked up in this session. Each must be resolved with `runoak`/OLS before binding.

---

## Sources

- Rao J, Ashraf S, et al. Advillin acts upstream of phospholipase C ε1 in steroid-resistant nephrotic syndrome. *J Clin Invest* 2017;127(12):4257–4269. PMID:29058690. [PubMed](https://pubmed.ncbi.nlm.nih.gov/29058690/) · [PMC5707164](https://pmc.ncbi.nlm.nih.gov/articles/PMC5707164/) · [JCI figure 4](https://www.jci.org/articles/view/94138/figure/4)
- Heintze JM. AVIL mutations reduce podocyte migration rate in SRNS (research highlight). *Nat Rev Nephrol* 2018. PMID:29129927.
- ClinGen Glomerulopathy GCEP. AVIL / nephrotic syndrome, type 21: Limited (2023-06-27; re-evaluated 2024-08-27). [ClinGen report](https://search.clinicalgenome.org/kb/gene-validity/CGGV:assertion_04806c21-071c-4a74-96c2-ab89ef5ba0e0-2024-08-27T180000.000Z)
- GeneReviews. Genetic Steroid-Resistant Nephrotic Syndrome Overview (NBK573219; PMID:34436835). https://www.ncbi.nlm.nih.gov/books/NBK573219/
- Fahlevi R, et al. Genetic mutation patterns in Indonesian children with primary SRNS. *Pediatr Nephrol* 2026. PMID:42420527.
- George SP, et al. F-actin-bundling sites are conserved in proteins with villin-type headpiece domains. *Mol Biol Cell* 2020. PMID:32520642.
- [OMIM *613397 AVIL](https://omim.org/entry/613397) · [ClinVar RCV000845156 (p.Arg446His)](https://www.ncbi.nlm.nih.gov/clinvar/RCV000845156.1/) · [GeneCards AVIL](https://genecards.org/cgi-bin/carddisp.pl?gene=AVIL)
- Hasegawa H, et al. Analyzing somatosensory axon projections with the sensory neuron-specific Advillin gene. *J Neurosci* 2007. PMID not verified here; look it up before citing. [Duke Scholars record](https://scholars.duke.edu/publication/804862)
- Advillin expression in neural-crest-derived neurons: [eNeuro 2018, ENEURO.0077-18.2018](https://www.eneuro.org/content/5/5/ENEURO.0077-18.2018); Advillin-Cre usage example: [PMC5346175](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5346175/)
- [RGD Avil](https://rgd.mcw.edu/rgdweb/report/gene/main.html?id=620301) · [Alliance/ZFIN avil](https://www.alliancegenome.org/gene/ZFIN:ZDB-GENE-060421-6683)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 8 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 33 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 3 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000007` (1 mention) - the report calls it "ClinGen: "AR"; segregation consistent in families with parental DNA"; HP calls it **Autosomal recessive inheritance**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000653` (2 mentions) - the report calls it "Cell:** podocyte"; CL calls it **podocyte**, and lists "renal podocyte" among its other names
- `GO:0030027` (1 mention) - the report calls it "Subcellular:** lamellipodium"; GO calls it **lamellipodium**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `CCID`.