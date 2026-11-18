---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-16T09:28:30.131029'
end_time: '2026-11-16T09:30:40.291590'
duration_seconds: 130.16
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Autosomal Recessive Nonsyndromic Hearing Loss 63
  mondo_id: MONDO:0012670
  category: Mendelian
  causal_genes: LRTOMT
  omim_id: OMIM:611451
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
  web_search_requests: 8
  num_turns: 11
  total_cost_usd: 1.7761046
  session_id: c09f72b6-1f70-44a3-8f39-1d48e94caabd
  stop_reason: end_turn
  permission_denials: 1
  denied_tools:
  - Bash
  assistant_text_blocks: 1
citation_count: 24
reference_validation:
  total_references: 10
  verified: 10
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 10
  on_topic: 7
  validator_version: 0.6.0
term_validation:
  total_terms: 25
  verified: 23
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0012670
    reported_labels:
    - MONDO
    ontology_label: autosomal recessive nonsyndromic hearing loss 63
  labels_variant: 1
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
- **Disease Name:** Autosomal Recessive Nonsyndromic Hearing Loss 63
- **MONDO ID:** MONDO:0012670 (if available)
- **Causal gene(s):** LRTOMT
- **OMIM:** OMIM:611451
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Autosomal Recessive Nonsyndromic Hearing Loss 63** covering all of the
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

# Research Report: Autosomal Recessive Nonsyndromic Hearing Loss 63 (DFNB63; MONDO:0012670; OMIM:611451)

> **How to use this report:** These findings came from web searches only. I did not open full texts or PubMed abstracts. Abstract-level wording below is quoted from search-result summaries and must be re-quoted from `just fetch-reference` cache files before it goes into `snippet:` fields. PMIDs marked **[verify]** were not confirmed against a source. Ontology CURIEs come from memory and must be looked up with `runoak` or the `cache/*/terms.csv` files before binding, as the project rules require.

---

## 1. Disease Information

**Overview.** DFNB63 is an autosomal recessive, nonsyndromic sensorineural hearing loss. It is caused by biallelic pathogenic variants in **LRTOMT** (leucine-rich transmembrane and O-methyltransferase), on chromosome 11q13.3–q13.4. Patients typically have congenital or prelingual, bilateral, severe-to-profound deafness, with no syndromic features.

- **Gene naming.** In humans, LRTOMT is a fusion of the ancestral *LRRC51* and *TOMT* genes. Rodents carry them as two separate genes, *Lrrc51* and *Tomt* (also called *Comt2*). The disease-relevant product is the TOMT moiety, LRTOMT2 (Ahmed et al. 2008; [PMC3404732](https://pmc.ncbi.nlm.nih.gov/articles/PMC3404732)). Recent literature often calls the human disease "TOMT-related hearing loss".

| Identifier | Value |
|---|---|
| MONDO | MONDO:0012670 |
| OMIM (phenotype) | 611451 — Deafness, autosomal recessive 63; DFNB63 ([OMIM mirror](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/commit/16b4b23030b9c25e5a647a69ebd82dc9aecccaad/www.ncbi.nlm.nih.gov/omim/611451)) |
| OMIM (gene) | LRTOMT, 612414 **[verify]** |
| Orphanet | Grouped under ORPHA:90636 "Rare autosomal recessive non-syndromic sensorineural deafness type DFNB" **[verify]** |
| ICD-10 | H90.3 / H90.5 (sensorineural hearing loss, nonspecific) |
| MeSH | Hearing Loss, Sensorineural; Deafness |
| Synonyms | DFNB63; deafness, autosomal recessive 63; LRTOMT-related / TOMT-related nonsyndromic hearing loss |

**Source type.** All information comes from aggregated family and case reports (linkage, exome sequencing, case series), not from EHR data.

## 2. Etiology

- **Cause.** The disease is monogenic: biallelic germline LRTOMT variants, mostly homozygous in consanguineous families.
- **Genetic risk factors:**
  - Parental consanguinity.
  - Founder alleles, especially c.242G>A (p.Arg81Gln) in North Africa ([Mosrati et al. 2021, PMC8580077](https://pmc.ncbi.nlm.nih.gov/articles/PMC8580077)).
- **Environmental, protective and gene–environment factors.** None are reported. No modifier genes are documented.

## 3. Phenotypes

| Phenotype | Type | Onset / severity / course | Frequency | Suggested HPO **[verify all]** |
|---|---|---|---|---|
| Bilateral sensorineural hearing impairment | sign | Congenital/prelingual; usually severe–profound; generally non-progressive | ~100% of reported cases | HP:0000407 Sensorineural hearing impairment; HP:0008527 Congenital sensorineural hearing impairment |
| Profound hearing loss | sign | Congenital | Most families (Khan 2007: "congenital bilateral profound hearing loss" in all affected) | HP:0012715 Profound hearing impairment |
| Prelingual onset with sign-language use | functional | Prelingual | Kalay 2007 Turkish family (via OMIM) | HP:0000365 Hearing impairment plus an onset qualifier |
| Later-onset, ski-slope (high-frequency) loss | sign | Onset at about age 11 | Rare; one compound heterozygote with p.Arg52Trp/p.Arg54Gln ([Wikipedia LRTOMT](https://en.wikipedia.org/wiki/LRTOMT), citing Ahmed 2008) | HP:0005101 High-frequency hearing impairment |
| Absence of vestibular / syndromic findings | — | — | Defining feature (nonsyndromic) | Not applicable |

- **Vestibular function in humans.** This is not well characterized. Vestibular dysfunction is clear in the *add* mouse (Du et al. 2008), so it is worth recording as a `HUMAN_MODEL_MISMATCH` / `KNOWLEDGE_GAP`.
- **Quality of life.** The main burden is communication and educational impact typical of prelingual deafness. No DFNB63-specific QoL data exist.

## 4. Genetic / Molecular Information

**Causal gene: LRTOMT** (HGNC symbol LRTOMT; HGNC ID not verified, look it up as lowercase `hgnc:`). Alternative reading frames give two proteins:
- **LRTOMT1** is LRRC51-like.
- **LRTOMT2** contains the leucine-rich region plus the TOMT methyltransferase.

Exons 5, 7 and 8 have dual reading frames. "All of the mutations primarily affect the LRTOMT2 protein" (Ahmed 2008).

**Reported variants:**

| Variant | Population | Notes | Source |
|---|---|---|---|
| c.242G>A, p.Arg81Gln | Tunisian (FT1), Libyan | Founder variant. Homozygous in 5.02% of 179 Tunisian and 2.94% of 34 Libyan ARNSHL families. Proposed as a "useful deafness biomarker for North African ARNSHL patients". | Ahmed 2008; Mosrati 2021 (MGGM, PMC8580077) |
| c.328G>A, p.Glu110Lys | Pakistani (PKDF702) | Missense | Ahmed 2008 table ([PMC3404732/T1](https://pmc.ncbi.nlm.nih.gov/articles/PMC3404732/table/T1)) |
| p.Arg52Trp / p.Arg54Gln (compound heterozygous) | — | Milder, later-onset ski-slope phenotype | Ahmed 2008 |
| Nonsense variant in human COMT2/LRTOMT | Families screened by Du et al. | Nonsense | Du 2008 PNAS, PMID 18794526 |
| c.?_? 16-bp deletion, p.Ala170Alafs*20 (exon 6) | Iranian, consanguineous | Homozygous frameshift; ACMG pathogenic; co-segregates | Sarmadi et al. 2020 BMC Med Genet ([PMC7285524](https://pmc.ncbi.nlm.nih.gov/articles/PMC7285524)); PMID **[verify]** |

- **Variant classes.** Missense, nonsense and frameshift. All are germline and act by loss of function.
- **Allele frequency.** These variants are rare or absent in gnomAD (none were seen in ethnically matched controls in Ahmed 2008). Check gnomAD for c.242G>A.
- **Epigenetics and structural variants.** None reported.
- **Gene-disease validity.** Check whether ClinGen has a CGGV record for LRTOMT–DFNB63 (Hearing Loss GCEP). If one exists, copy its tier and do not assign one yourself.

## 5. Environmental Information

Not applicable. No environmental, lifestyle or infectious contributors are known.

## 6. Mechanism / Pathophysiology

**Causal chain:**
1. Biallelic loss-of-function variants in LRTOMT remove functional TOMT (LRTOMT2) protein in cochlear and vestibular hair cells.
2. Loss of TOMT **leads to** failed trafficking of TMC1/TMC2 out of the secretory pathway (Golgi) into the stereocilia hair bundle. TOMT localizes to the Golgi and binds TMC1, and the interaction is modulated by TOMT His183. Without Tomt, "Tmc1/2 are specifically excluded from the hair bundle", while other MET complex proteins still localize there (Erickson et al. 2017, eLife; PMID 28534737; [PMC5462536](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5462536/)). Evidence is from zebrafish and HEK293 cells.
3. Without bundle TMCs, the mechanoelectrical transduction (MET) channel is not assembled, which **results in** abolished MET currents in cochlear hair cells. mTOMT "is essential for mechanotransduction"; this role is **independent of its methyltransferase activity**, and COMT cannot substitute for it (Cunningham et al. 2017, eLife 6:e24318; PMID 28504928 from Addgene, **[verify]**). Evidence is from mouse.
4. Loss of transduction **leads to** progressive degeneration of the organ of Corti and hair cells. The *add* (Tomt p.R48L) mouse shows "profound sensorineural deafness, and progressive degeneration of the organ of Corti" plus vestibular impairment (Du et al. 2008, PMID 18794526). Evidence is from mouse.
5. These steps **result in** congenital, severe-to-profound bilateral sensorineural hearing loss in humans. Steps 2–4 in human tissue are inferred from the models; no human temporal-bone data exist.

**Rejected alternative.** The original hypothesis was a catecholamine-degradation defect: TOMT is a catechol-O-methyltransferase with reduced activity in the *add* mouse. Later work argues against it. Zebrafish *tomt* mutants are rescued by Tomt or mouse TOMT but not by Comt, and Erickson et al. conclude "DFNB63 is unlikely to be a disease involving catecholamine metabolism". Record this as a refuted or alternative `mechanistic_hypotheses` group.

**Suggested terms [verify]:**
- GO:
  - GO:0050910 detection of mechanical stimulus involved in sensory perception of sound
  - GO:0007605 sensory perception of sound
  - GO:0016206 catechol O-methyltransferase activity (enzymatic; dispensable for MET)
  - A protein-transport-to-stereocilium term: look up candidates such as "protein localization to stereocilium"
  - GO:0042490 mechanoreceptor differentiation (probably not appropriate)
- Cellular component: Golgi apparatus (GO:0005794), stereocilium (GO:0032420), mechanotransducer channel complex (look up).
- CL: CL:0000589 cochlear inner hair cell; CL:0000601 cochlear outer hair cell; CL:0000202 auditory hair cell; vestibular hair cell (look up).
- Biological scale: TOMT–TMC trafficking is CELLULAR; MET loss is CELLULAR; organ of Corti degeneration is TISSUE.

## 7. Anatomical Structures

- **Organ.** Inner ear: the cochlea (UBERON:0001844) and its spiral organ / organ of Corti (UBERON:0002227). Vestibular involvement is shown in mice only.
- **Body system.** Auditory (sensory nervous) system.
- **Cells.** Inner and outer hair cells. TOMT expression is hair-cell-specific (supported by Du 2008: "highly expressed in sensory hair cells").
- **Subcellular.** Golgi apparatus and hair-bundle stereocilia (MET complex at stereocilia tips).
- **Laterality.** Bilateral and symmetric.

## 8. Temporal Development

- **Onset.** Congenital or prelingual in nearly all cases; one adolescent-onset compound heterozygote is reported.
- **Course.** Usually stable, profound loss. The mouse shows progressive hair-cell degeneration, but human progression data are sparse.
- **Duration and remission.** Lifelong; no spontaneous remission.
- **Critical period.** Early auditory intervention (hearing aids or cochlear implant in the first 1–2 years) is the window for language development.

## 9. Inheritance and Population

- **Inheritance.** Autosomal recessive (HP:0000007). Penetrance is complete for biallelic null or missense alleles. Expressivity is mostly consistent, with rare milder allele combinations. There is no anticipation and no mosaicism reported.
- **Prevalence.** No population estimate exists; the disease is ultra-rare.
- **Families and populations reported.** Pakistani (Khan 2007; Ahmed 2008), Turkish (Kalay 2007), Tunisian (Tlili 2007), Iranian (Sarmadi 2020) and Libyan (Mosrati 2021).
  - The highest mutation frequency reported is in Tunisian families, followed by Iranian, Turkish and Pakistani families.
  - c.242G>A shares a founder haplotype across North Africa.
- **Locus-mapping papers:**
  - Khan et al. 2007, Hum Genet 120:789–793 (four Pakistani families; 11q13.2–q13.3); PMID **[verify]**.
  - Kalay et al. 2007, J Mol Med 85:397–404 (Turkish family TR57); PMID **[verify]**.
  - Tlili et al. 2007, Ann Hum Genet 71:271–275 (Tunisian family; LOD 5.33 at D11S916/D11S4207); PMID **[verify]**.
- **Sex ratio.** 1:1, as expected for autosomal recessive inheritance.
- **Prevalence encoding.** Use `measure_type: CASES_IN_LITERATURE` or `UNKNOWN`; don't invent a rate.

## 10. Diagnostics

- **Audiology.** Pure-tone audiometry, ABR (auditory brainstem response) and OAE (otoacoustic emissions). Newborn hearing screening detects congenital cases.
- **Genetics.**
  - Multigene hearing-loss panels, or exome sequencing, which is how the Iranian case was solved.
  - Targeted c.242G>A testing is proposed as first-tier for North African patients.
  - Exclude GJB2 first, as it is the most common cause.
- **Imaging.** CT/MRI of the temporal bone is expected to be normal, and is useful before implantation.
- **Differential diagnosis.** Other DFNB loci (GJB2, TMC1/DFNB7/11, which shares the downstream MET defect, and others). Also syndromic deafness: Usher syndrome (vestibular/retinal), Pendred syndrome (enlarged vestibular aqueduct/goiter) and Jervell and Lange-Nielsen syndrome (long QT).

## 11. Outcome / Prognosis

- **Survival.** Normal life expectancy; the disease causes no mortality.
- **Morbidity.** Permanent profound deafness with communication and educational impact if untreated.
- **Cochlear implant outcomes.** These are expected to be favourable because spiral ganglion neurons are presumably spared, but there are no series. One Iranian child was implanted at 1 year 5 months (Sarmadi 2020).

## 12. Treatment

| Treatment | Suggested NCIT term [verify] | Modality |
|---|---|---|
| Cochlear implantation | NCIT:C15329 Surgical Procedure, with a NCIT:C157820 Cochlear Implant device qualifier (per CLAUDE.md pattern) | SURGERY |
| Hearing aids / auditory rehabilitation | NCIT:C15315 Rehabilitation | DEVICE / BEHAVIORAL |
| Sign language and speech therapy | NCIT:C159273 speech language therapy | BEHAVIORAL |
| Genetic counseling | NCIT:C15240 Genetic Counseling | — |

- **Pharmacotherapy and pharmacogenomics.** None exist.
- **Experimental gene therapy (preclinical only).**
  - In mice, AAV delivery of TOMT through ubiquitous or off-target promoters was toxic and killed inner hair cells.
  - A hair-cell-specific promoter construct given to newborn mice restored hearing and balance.
  - An RNID-funded project (Cunningham and Moatti, University of Pittsburgh; March 2026–February 2029) and an NIH-funded project are pursuing translation ([RNID](https://rnid.org.uk/what-we-do/biomedical-research/research-we-fund/restoring-hearing/developing-gene-therapy-for-tomt-linked-hearing-loss); [findatrial](https://www.findatrial.com/research/gene-therapy-for-hearing-loss-caused-by-tomt-mutations-NIH-11066259); [Eye and Ear 2026](https://eyeandear.org/2026/06/gene-therapies-for-hearing-loss-treating-defective-genes-and-beyond/)).
  - I found no clinical trial (no NCT number).
  - The RNID page states that "Up to 8% of all genetic forms of hearing loss are due to mutations in TOMT". This is unsourced and implausibly high, so don't cite it as epidemiology.

## 13. Prevention

- **Primary prevention.** Carrier testing and genetic counseling in consanguineous families; prenatal or preimplantation genetic diagnosis for known familial variants.
- **Secondary prevention.** Universal newborn hearing screening, then early genetic diagnosis.
- **Tertiary prevention.** Early amplification or implantation to protect language development.

## 14. Other Species

- No naturally occurring animal disease is reported in OMIA.
- **Orthologs.** Mouse *Tomt* (*Comt2*; MGI ID to be looked up). Zebrafish *tomt* (ZFIN). Rodents carry *Lrrc51* and *Tomt* as separate genes.
- **Conservation.** TOMT's role in TMC trafficking and MET is conserved from zebrafish to mouse.

## 15. Model Organisms

| Model | Genotype | Recapitulation | Limitations | Source |
|---|---|---|---|---|
| *add* mouse (ENU-induced) | Tomt/Comt2 p.R48L homozygous | Profound deafness, vestibular dysfunction, progressive organ of Corti degeneration; reduced COMT2 enzymatic activity | Vestibular phenotype not documented in humans; its catecholamine interpretation was later disfavoured | Du et al. 2008 PNAS, PMID 18794526 ([PMC2567147](https://pmc.ncbi.nlm.nih.gov/articles/PMC2567147)) |
| *Tomt* mouse models | Loss of mTOMT | Absent MET currents in cochlear hair cells; methyltransferase-independent; COMT cannot rescue | — | Cunningham et al. 2017 eLife 24318 ([link](https://elifesciences.org/articles/24318v1)) |
| Zebrafish *tomt* mutant (*mercury*) | Loss of function | Absent lateral-line and inner-ear hair-cell MET; Tmc1/2 excluded from the bundle; rescued by Tomt or mouse TOMT, not by Comt | Non-mammalian; lateral-line hair cells differ from cochlear ones | Erickson et al. 2017 eLife, PMID 28534737 |
| HEK293 co-expression | TOMT + TMC1 | Direct interaction modulated by His183 | Heterologous cells (IN_VITRO) | Erickson et al. 2017 |

- **Relationship slots.** All three animal models would be `RECAPITULATES` against the MET-loss node. The mouse vestibular phenotype supports a `HUMAN_MODEL_MISMATCH` discussion.
- **Resources.** MGI, ZFIN and IMPC.

---

## Key Citations (to fetch and verify before curation)

| Citation | Topic | PMID / status |
|---|---|---|
| Ahmed ZM et al. 2008 Nat Genet 40:1335–1340, doi:10.1038/ng.245 | Gene discovery | 18953341 **[verify]** |
| Du X et al. 2008 PNAS 105:14609–14614 | *add* mouse; human nonsense allele | 18794526 |
| Cunningham CL et al. 2017 eLife 6:e24318 | Mouse MET; methyltransferase-independent | 28504928 **[verify]** |
| Erickson T et al. 2017 eLife 6:e28474 | Tmc1/2 trafficking in zebrafish | 28534737 |
| Khan SY et al. 2007 Hum Genet 120:789 | Locus mapping, Pakistani families | **[verify]** |
| Kalay E et al. 2007 J Mol Med 85:397 | Locus mapping, Turkish family | **[verify]** |
| Tlili A et al. 2007 Ann Hum Genet 71:271 | Locus mapping, Tunisian family | **[verify]** |
| Sarmadi A et al. 2020 BMC Med Genet | Iranian frameshift | PMC7285524; PMID **[verify]** |
| Mosrati MA et al. 2021 Mol Genet Genomic Med | North African c.242G>A founder | PMC8580077; PMID **[verify]** |

**Gaps for the curator.** I found no LRTOMT variant reports from 2022–2024, no ClinGen tier, no GeneReviews chapter specific to DFNB63 (check `just check-genereviews`), and no human vestibular or natural-history data.

Sources:
- [LRTOMT — Wikipedia](https://en.wikipedia.org/wiki/LRTOMT)
- [Ahmed 2008 PMC3404732](https://pmc.ncbi.nlm.nih.gov/articles/PMC3404732) · [Table 1](https://pmc.ncbi.nlm.nih.gov/articles/PMC3404732/table/T1) · [doi:10.1038/ng.245](https://dx.doi.org/10.1038/ng.245)
- [AudiologyOnline/NIDCD release](https://www.audiologyonline.com/releases/one-gene-two-proteins-researchers-3435)
- [Erickson 2017 PMC5462536](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5462536/) · [eLife 28474](https://elifesciences.org/articles/28474) · [PubMed 28534737](https://pubmed.ncbi.nlm.nih.gov/28534737)
- [Du 2008 PubMed 18794526](https://pubmed.ncbi.nlm.nih.gov/18794526/) · [PMC2567147](https://pmc.ncbi.nlm.nih.gov/articles/PMC2567147) · [Scripps news](https://www.scripps.edu/newsandviews/e_20080922/beutler.html)
- [Cunningham 2017 eLife 24318](https://elifesciences.org/articles/24318v1) · [Addgene PMID listing](https://addgene.org/browse/pubmed/28504928)
- [OMIM 611451 mirror](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/commit/16b4b23030b9c25e5a647a69ebd82dc9aecccaad/www.ncbi.nlm.nih.gov/omim/611451)
- [Khan 2007 Hum Genet](https://link.springer.com/doi/10.1007/s00439-006-0275-1) · [Kalay 2007 record](https://avesis.ktu.edu.tr/yayin/17aa77fe-3aed-4f2f-aae6-e0972ad59c6c/a-novel-locus-for-autosomal-recessive-nonsyndromic-hearing-impairment-dfnb63-maps-to-chromosome-11q13-2-q13-4) · [Tlili record](https://bvbvf1.bib-bvb.de/vufind/PrimoRecord/cdi_proquest_miscellaneous_69033121)
- [Sarmadi 2020 PMC7285524](https://pmc.ncbi.nlm.nih.gov/articles/PMC7285524) · [BMC PDF](https://bmcmedgenet.biomedcentral.com/track/pdf/10.1186/s12881-020-01061-7)
- [Mosrati 2021 PMC8580077](https://pmc.ncbi.nlm.nih.gov/articles/PMC8580077) · [DOAJ](https://doaj.org/article/29daf1cf4ebf4f7b903815af2e77e718)
- [RNID TOMT gene therapy](https://rnid.org.uk/what-we-do/biomedical-research/research-we-fund/restoring-hearing/developing-gene-therapy-for-tomt-linked-hearing-loss) · [findatrial NIH project](https://www.findatrial.com/research/gene-therapy-for-hearing-loss-caused-by-tomt-mutations-NIH-11066259) · [Mass Eye and Ear 2026](https://eyeandear.org/2026/06/gene-therapies-for-hearing-loss-treating-defective-genes-and-beyond/)

## Reference Validation

Checked with `linkml-reference-validator` 0.6.0.

| Outcome | Count |
| --- | --- |
| References checked | 10 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 10 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 25 |
| Resolved | 23 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 2 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0012670` (2 mentions) - the report calls it "MONDO"; MONDO calls it **autosomal recessive nonsyndromic hearing loss 63**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0005794` (1 mention) - the report calls it "Cellular component: Golgi apparatus"; GO calls it **Golgi apparatus**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `ORPHA`.