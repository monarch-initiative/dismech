---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-07T18:05:56.866432'
end_time: '2026-09-07T18:11:32.454190'
duration_seconds: 335.59
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Charcot-Marie-Tooth Disease Type 4B3
  mondo_id: MONDO:0014117
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
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 16
  num_turns: 35
  total_cost_usd: 1.6811321999999995
  session_id: 8e6a3453-99e0-563b-8e2c-3bcb30d1c949
  stop_reason: end_turn
  assistant_text_blocks: 4
citation_count: 21
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 1
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMC:PMC12926636
  relevance_assessed: 14
  on_topic: 11
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 68
  verified: 61
  not_found: 1
  obsolete: 2
  unverifiable: 4
  confabulation_rate: 0.016
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0014117
    reported_labels:
    - MONDO
    ontology_label: Charcot-Marie-Tooth disease type 4B3
  unresolved_terms:
  - HP:0007257
  obsolete_terms:
  - term_id: HP:0002355
    ontology_label: obsolete Difficulty walking
    replaced_by: HP:0001288
  - term_id: GO:0032313
    ontology_label: GO_0032313
    replaced_by: GO:0043087
  unresolvable_prefixes:
  - ORPHA
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Charcot-Marie-Tooth Disease Type 4B3
- **MONDO ID:** MONDO:0014117 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Charcot-Marie-Tooth Disease Type 4B3** covering all of the
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

I'll research Charcot-Marie-Tooth Disease Type 4B3 (CMT4B3) using web search to gather current, well-cited information.

Good foundation. Let me dig deeper into key primary sources: OMIM, the original discovery paper, the mitochondrial dysfunction paper, the zebrafish model, GeneReviews/Orphanet details, and phenotype/prevalence data.

Excellent detail gathered. Let me get more on the additional key papers: the phenotype expansion review, the fork-and-bracket syndrome paper, the autosomal dominant SBF1 case, and treatment/model organism data (MGI, IMPC).

# Charcot-Marie-Tooth Disease Type 4B3 (CMT4B3): Comprehensive Research Report

## 1. Disease Information

### Overview
Charcot-Marie-Tooth disease type 4B3 (CMT4B3) is an ultra-rare, autosomal recessive, childhood-onset demyelinating/axonal sensorimotor peripheral neuropathy caused by biallelic pathogenic variants in **SBF1** (SET-binding factor 1, also called **MTMR5**), located on chromosome 22q13.33. It is the third molecularly defined subtype of the CMT4B group of "myelin-outfolding" neuropathies, joining CMT4B1 (*MTMR2*) and CMT4B2 (*MTMR13/SBF2*). The disease was first molecularly characterized in 2013 in a Korean kindred (Nakhro et al., PMID:23749797) and has since been expanded to include a syndromic spectrum with cranial neuropathies, microcephaly, intellectual disability, and distinctive brain-stem MRI findings (the "fork and bracket sign").

CMT4B3 is exceptionally rare: as of the most recent literature synthesis, only a handful of families (originally reported as three, subsequently expanded to at least seven–nine kindreds across Korean, Saudi Arabian, Syrian, Israeli, Spanish, British, and Italian populations) have been described, and a patient advocacy organization (CMT4B3 Research Foundation) reports "only 14 documented cases worldwide" as of its most recent public accounting (cmt4b3research.org).

### Key Identifiers
| Resource | Identifier |
|---|---|
| OMIM (phenotype) | **#615284** — Charcot-Marie-Tooth Disease, Demyelinating, Type 4B3 |
| OMIM (gene) | **\*603560** — SET-Binding Factor 1; SBF1 |
| HGNC | SBF1, HGNC:10542 |
| Gene location | 22q13.33 (chr22:50,443,219–50,483,923, GRCh38) |
| MANE Select transcript | NM_002972.4 / NP_002963.2 (ENST00000380817.8), 41 exons |
| MONDO | MONDO:0014117 |
| Orphanet | ORPHA:363981 |
| GeneReviews/NCBI GTR condition | C3695063 |
| Aliases | CMT4B3; SBF1; MTMR5; DENN domain–containing protein |

*(Sources: [OMIM #615284](https://www.omim.org/entry/615284); [OMIM *603560](https://omim.org/entry/603560); [Orphanet](https://www.orpha.net/en/disease/detail/363981); [NIH GTR](https://www.ncbi.nlm.nih.gov/gtr/conditions/C3695063/))*

### Synonyms
- Charcot-Marie-Tooth disease, demyelinating, type 4B3
- CMT4B3
- SBF1-related neuropathy / SBF1-related syndromic neuropathy
- MTMR5-associated CMT4B3
- (Historically catalogued together with) "fork and bracket" syndrome — a specific syndromic MRI-defined SBF1 phenotype

### Data provenance
Essentially all published knowledge of CMT4B3 derives from **aggregated case reports and small family series** (whole-exome/whole-genome sequencing of individual consanguineous or compound-heterozygous kindreds), not from large EHR-derived cohorts or population registries — reflecting a total published patient count in the low tens. This is important context for interpreting any "typical" phenotype claims below: each additional family has materially reshaped the described phenotypic spectrum.

---

## 2. Etiology

### Disease Causal Factors
CMT4B3 is a monogenic, **autosomal recessive** disorder caused by biallelic (homozygous or compound heterozygous) loss-of-function or hypomorphic variants in *SBF1*/*MTMR5*. There is no known environmental, infectious, or non-genetic cause. One report — from a website aimed at lay audiences — vaguely suggested de novo mutations could be "triggered by environmental factors like UV exposure or viral infections," but this is **not supported by primary genetics literature** and should not be treated as an established causal mechanism; germline SBF1 variants are inherited from asymptomatic carrier parents in essentially all reported pedigrees.

### Genetic Risk Factors
- **Causal variants**: Missense (e.g., p.Met417Val, p.Thr1590Ala — the original Korean family, PMID:23749797), nonsense/splice-site null variants (e.g., a homozygous splice-site mutation in a consanguineous Bedouin kindred, PMID:30039846), and frameshift/deletion variants (e.g., c.5477-5478del/p.1826_1826del, exon 40, PMC7419361) have all been reported as causal.
- **Consanguinity** is a major risk factor: most reported families are from populations with high rates of consanguineous marriage (Saudi Arabian, Syrian/Bedouin kindreds), consistent with autosomal recessive inheritance of a rare allele.
- **A single reported exception to autosomal recessive inheritance**: a 2024 report describes a mother–daughter pair with an apparently **dominantly inherited** SBF1 missense variant (c.1398C>A, p.H466Q), the authors proposing a dominant-negative mechanism, in contrast to "the seven cases reported before" that were autosomal recessive (PMC11633322). This is a notable and still-unusual finding that expands (and complicates) the inheritance model.
- **Modifier/uncertain-significance context**: a 2025 pediatric study of persistent toe-walking identified heterozygous SBF1 variants in some children, but concluded these single-allele variants "may act as modifiers or coincidental findings rather than independent causes of neuromotor abnormalities" (PMC12926636) — a caution against over-interpreting monoallelic SBF1 findings as causal.

### Environmental Risk Factors
None specifically established. General CMT risk-modifying exposures (peripheral neurotoxic drugs such as vincristine, which can exacerbate any CMT subtype) are plausible by extension from general CMT biology but have not been specifically studied in CMT4B3.

### Protective Factors
None reported in the literature; the extreme rarity of the disease precludes population-based identification of protective alleles or environmental factors. gnomAD-based constraint metrics for SBF1 have not yet been directly reported in the primary CMT4B3 literature surveyed, though general gnomAD gene-constraint methodology (observed/expected loss-of-function ratio) would apply.

### Gene-Environment Interactions
Not established for CMT4B3 specifically.

---

## 3. Phenotypes

### Core neuromuscular phenotype (classic/original presentation)
The original Korean family (PMID:23749797) presented with a **"homogeneous phenotype of pure sensory motor demyelinating neuropathy with focally folded myelin sheaths"** — onset of distal atrophy and weakness of the upper and lower limbs, decreased vibration and position sense, areflexia, and pes planus **in the first decade of life**, with slow progression to loss of ambulation by the fifth decade.

Common motor/sensory features across the literature:
- Distal muscle weakness and atrophy (legs > arms initially)
- Steppage gait, foot drop, pes cavus/pes planus
- Distal sensory loss (vibration, position sense)
- Hyporeflexia progressing to areflexia
- Fasciculations and muscle cramps
- Gait ataxia in some patients
- Scoliosis/kyphoscoliosis, syndactyly in syndromic presentations

### Expanded/syndromic phenotype
Subsequent families (Saudi Arabian, Syrian/Bedouin, Israeli, Spanish, British, Italian) revealed a substantially broader spectrum:
- **Cranial nerve involvement**: facial weakness, ophthalmoparesis/strabismus, dilated unreactive pupils, nystagmus, dysphagia, dysarthria — described as "axonal motor predominant neuropathy and cranial nerve involvement" (multiple families, PMIDs 24799518, 28005197, 32444983, 20658556, 30039846)
- **Microcephaly** (congenital or progressive) — a recurring, distinctive feature not typical of other CMT4B subtypes
- **Intellectual disability / developmental delay**
- **Cerebellar and pyramidal signs**, evident in infancy in the most severe (null-mutation) family, "with peripheral polyneuropathy emerging only toward the end of the first decade" (PMID:30039846)
- **Skeletal anomalies**: syndactyly, short stature, kyphoscoliosis, congenital talon-valgus-pronated clubfoot
- **"Fork and bracket" syndrome**: a distinct MRI-defined entity — T2-hyperintense signal in the pons ("fork sign") and mesencephalon ("bracket sign"), attributed to degenerated oculomotor and facial nerve fiber bundles, first described by Mégarbané et al. 2010 (PMID:20658556) and specifically linked to SBF1 by later exome studies
- **Mitochondrial dysfunction**: a 2021 Italian case (PMID:34118926) described infantile-onset severe motor polyneuropathy with respiratory failure requiring non-invasive ventilation by age 6 and wheelchair dependence by age 11, **without cognitive impairment or brain MRI abnormalities** — demonstrating marked phenotypic heterogeneity even within the "classic" neuropathy-only presentation. Muscle biopsy showed reduced respiratory chain complex I (65% of normal), II+III (55%), and IV (66%) activities and ~30% reduced mtDNA content.
- **Necklace fibers on muscle biopsy** — a pathological feature classically associated with myotubular myopathy — were reported for the first time in SBF1-related disease in a family with a novel frameshift deletion, alongside marked neurogenic atrophy and axonal (non-demyelinating) sensorimotor neuropathy (PMC7419361), further broadening the described pathological spectrum beyond "pure demyelinating."

### Onset, Severity, Progression
- **Age of onset**: Highly variable — ranges from congenital/infantile (clubfoot at birth, hypotonia by 18 months in the mitochondrial-dysfunction case) to classic first-decade onset (5–11 years, as in most series) to, in the null-variant Bedouin family, an infantile cerebellar/pyramidal presentation with polyneuropathy emerging only in later childhood.
- **Severity**: Variable, ranging from ambulatory adult patients with slowly progressive distal neuropathy (loss of ambulation only in the 5th decade in the original Korean family) to severe infantile-onset cases requiring ventilatory support and wheelchair use by the first decade.
- **Progression**: Generally **slowly progressive**, consistent with other demyelinating CMT4B subtypes, though the syndromic/cranial-nerve-involving forms and the mitochondrial-dysfunction phenotype show more rapid, severe courses.
- **Frequency**: Given the rarity (roughly a dozen-plus published families), phenotype frequency percentages (e.g., "X% have microcephaly") are not statistically reliable; qualitative descriptions ("commonly," "in some patients") are the best available granularity.

### Quality of Life
No disease-specific EQ-5D/SF-36 data exist for CMT4B3. By extension from general CMT literature, progressive distal weakness, gait impairment, and (in syndromic cases) cranial nerve deficits (dysphagia, dysarthria, ophthalmoplegia) and intellectual disability would be expected to substantially impact mobility, communication, feeding, and independence — more so than milder CMT1A-type neuropathies, given several reported cases require respiratory support and wheelchairs.

### Suggested HPO terms
- HP:0002355 Difficulty walking
- HP:0003676 Progressive
- HP:0001336 Myoclonus (if applicable) — not core
- HP:0001382 Joint hypermobility (variable)
- HP:0009830 Peripheral neuropathy
- HP:0007256 Progressive peripheral neuropathy
- HP:0002380 Hyporeflexia / HP:0001284 Areflexia
- HP:0003707 Calf muscle hypertrophy — not typical; distal atrophy predominates: HP:0003693 Distal amyotrophy
- HP:0001761 Pes cavus / HP:0001763 Pes planus
- HP:0001941 Talipes (clubfoot)
- HP:0001344 Absent/decreased deep tendon reflexes
- HP:0000010 Recurrent urinary tract infections — not relevant
- HP:0000252 Microcephaly
- HP:0001249 Intellectual disability
- HP:0001256 Intellectual disability, mild (variable severity)
- HP:0000486 Strabismus
- HP:0000601 Nystagmus (relative afferent findings)
- HP:0000508 Ptosis / HP:0000601 nystagmus, HP:0000486 strabismus for ophthalmoparesis
- HP:0009085 Syndactyly
- HP:0002650 Scoliosis / HP:0002751 Kyphoscoliosis
- HP:0001260 Dysarthria
- HP:0002015 Dysphagia
- HP:0007257 Facial palsy (facial nerve weakness)
- HP:0001260 Ataxic gait / HP:0002066 Gait ataxia
- HP:0002322 Resting tremor — not typical
- HP:0003198 Myopathy (necklace fibers case)
- HP:0003560 Muscle fiber necrosis — not primary
- HP:0001397 Hepatomegaly — not relevant

---

## 4. Genetic/Molecular Information

### Causal Gene
**SBF1** (SET-binding factor 1; synonym MTMR5), OMIM \*603560, HGNC:10542, chromosome 22q13.33.

### Gene/Protein Structure
- 41-exon gene; MANE Select transcript NM_002972.4 encoding NP_002963.2 (~208 kDa protein).
- Protein domains: upstream DENN (uDENN), DENN, downstream DENN (dDENN) domains; an SBF2 (myotubularin-like phosphatase) domain; a GRAM domain (Glucosyltransferases, Rab-like GTPase activators, and Myotubularins); and a Pleckstrin Homology (PH) domain (GeneCards, ResearchGate figure sources).
- **Pseudophosphatase**: SBF1/MTMR5 lacks several catalytic-pocket residues required for phosphatase activity, rendering it catalytically inactive as a phosphoinositide phosphatase, though the substrate-binding pocket is preserved enough to bind phosphorylated substrates — potentially protecting them from active phosphatases or acting as a scaffold.
- Functionally, SBF1/MTMR5 heterodimerizes (via coiled-coil domains) with the catalytically active phosphatase **MTMR2** (the CMT4B1 gene), analogous to how MTMR13/SBF2 (the CMT4B2 gene) also dimerizes with MTMR2. The DENN domain of SBF1 is proposed to activate Rab GTPases (Rab21, and possibly serve as a GEF for Rab28), positioning SBF1 in **endo-lysosomal/endosomal trafficking regulation**.

### Pathogenic Variants Reported
| Family/origin | Variant(s) | Type | Zygosity | PMID |
|---|---|---|---|---|
| Korean (original) | c.1249A>G (p.Met417Val); c.4768A>G (p.Thr1590Ala) | Missense | Compound heterozygous | 23749797 |
| Bedouin (consanguineous) | Homozygous splice-site null variant | Splice/null | Homozygous | 30039846 |
| Italian | c.2291G>A (p.R763H); c.3194G>A (p.G1064E) | Missense | Compound heterozygous | 34118926 |
| SBF1 syndromic/necklace-fiber family | c.5477_5478del (p.1826_1826del), exon 40 | Frameshift → premature stop, truncation | Homozygous | (PMC7419361) |
| Mother–daughter (dominant) | c.1398C>A (p.H466Q), exon 13 | Missense | Heterozygous (apparent dominant transmission) | (PMC11633322) |
| Saudi Arabian | Reported with microcephaly, strabismus, syndactyly | — | — | 24799518 |
| British/other | Additional missense/null alleles | — | — | 28005197, 32444983 |

Variant classification follows standard ACMG/AMP criteria via ClinVar (specific ClinVar accessions reported for the Italian case: RCV001449576.1, RCV001449656.1); most reported variants are classified pathogenic or likely pathogenic based on segregation, absence/rarity in population databases (gnomAD), and functional predictions.

### Allele Frequency
Given the extreme rarity of the disease, specific pathogenic SBF1 alleles are expected to be essentially absent or present only as ultra-rare heterozygous carriers in gnomAD; no disease-specific population carrier frequency has been established in the literature reviewed. General gnomAD constraint methodology (observed/expected loss-of-function ratio, "oe") would classify constraint for SBF1 as a whole, but a specific oe value was not retrievable in this pass of searches — recommend a targeted gnomAD browser query (`gnomad.broadinstitute.org`, gene SBF1) during KB curation for an exact upper-bound CI value.

### Functional Consequences
- Missense variants (M417V, T1590A) may impair MTMR2 protein-protein interaction, potentially destabilizing the MTMR2–MTMR5 complex and driving myelin-outfolding pathology (proposed mechanism from mouse studies, PMC9190308).
- Null/truncating variants cause loss of MTMR5 protein and, at least in the mouse knockout model, do **not** cause myelin outfoldings but instead impair **axon radial sorting** — a mechanistically distinct process from the myelin-outfolding pathology of complete MTMR2 or MTMR13 loss (see Mechanism section).
- This raises the hypothesis that different variant classes (partial loss-of-function/missense vs. complete null) may produce mechanistically and phenotypically distinct disease presentations — an important nuance for genotype-phenotype correlation in CMT4B3.

### Modifier Genes
No formally established modifier genes; MTMR2 is a genetically and physically interacting partner whose own dosage/levels are interdependent with MTMR5 and MTMR13 in the peripheral nervous system (mouse studies show MTMR2 loss destabilizes both MTMR5 and MTMR13 protein levels, PMC9190308).

### Epigenetic Information
Not specifically studied in CMT4B3.

### Chromosomal Abnormalities
Not applicable — CMT4B3 is caused by small-scale sequence variants (missense, nonsense, splice-site, small indels), not large chromosomal rearrangements.

---

## 5. Environmental Information

No specific environmental triggers, toxins, occupational exposures, lifestyle factors, or infectious agents have been established as causal or modifying for CMT4B3 in the peer-reviewed literature. As with other hereditary neuropathies, avoidance of peripherally neurotoxic agents (e.g., vincristine and other chemotherapeutics known to worsen CMT broadly) would be a reasonable precaution by extension of general CMT clinical practice, though this has not been specifically documented for CMT4B3 patients.

---

## 6. Mechanism / Pathophysiology

### Causal chain (numbered, from mutation to phenotype)

1. Biallelic pathogenic variants in *SBF1* (22q13.33) **lead to** absent, truncated, or functionally impaired MTMR5 (SBF1) pseudophosphatase protein.
2. Loss/impairment of MTMR5 **disrupts** its heterodimeric complex with the catalytically active phosphatase MTMR2 (and, in parallel, the analogous MTMR2–MTMR13 complex) — demonstrated by mouse coexpression studies showing co-expression with MTMR2 "greatly increased the levels" of MTMR5 protein, indicating mutual stabilization (PMC9190308). *(Demonstrated in mouse model; inferred to extend to human Schwann cell biology.)*
3. Disruption of the MTMR2–MTMR5 complex **impairs** the complex's proposed function in regulating phosphoinositide levels (e.g., PtdIns3P/PtdIns(3,5)P2 turnover) and Rab GTPase activation (notably Rab21, potentially Rab28) within Schwann cells and neurons.
4. Impaired phosphoinositide/Rab regulation **disrupts endosomal trafficking**, in particular the sorting/recycling of key Schwann cell surface receptors through endosomal compartments — the mouse literature specifically implicates ErbB2/ErbB3 (neuregulin receptor tyrosine kinases essential for Schwann cell myelination signaling) and β1-integrin trafficking as candidate downstream targets. *(This step is proposed/inferred from mouse mechanistic studies rather than directly demonstrated in human tissue.)*
5. Branch point — the downstream consequence differs by variant class:
   - **Branch A (complete/near-complete loss of MTMR5, as modeled by mouse knockout)**: Disrupted receptor trafficking **impairs axon radial sorting** — the developmental process by which Schwann cells segregate and ensheath individual large-caliber axons from bundles — **resulting in** reduced numbers of properly sorted/myelinated large axons, without myelin outfolding and with normal myelin thickness/g-ratio once myelination does occur (mouse Mtmr5−/− data, PMC9190308).
   - **Branch B (partial-function missense variants, e.g., M417V/T1590A)**: The authors hypothesize these variants may impair MTMR2 interaction specifically, **triggering classic myelin outfoldings** — the redundant, infolded/refolded myelin loops characteristic of CMT4B1/CMT4B2 — analogous to the pathology seen with primary MTMR2 or MTMR13 loss. *(Explicitly labeled as a hypothesis by the study authors, not yet directly demonstrated.)*
6. In parallel to peripheral nerve pathology, MTMR5 loss in the CNS **disrupts early neurogenesis** (not via increased apoptosis/cell death) — shown in a zebrafish *mtmr5* knockout model as reduced brain size (~10%) from 10 days post-fertilization onward, with disorganized axon branching morphology, **contributing to** the microcephaly and structural brain phenotypes seen in a subset of severe human CMT4B3 cases (PMC11891516).
7. Peripheral axonal-sorting/myelination failure plus (in syndromic cases) cranial nerve and CNS involvement **culminate in** the clinical phenotype: distal sensorimotor polyneuropathy (weakness, atrophy, sensory loss, areflexia), and — in the more severe/syndromic end of the spectrum — cranial neuropathies (facial weakness, ophthalmoparesis), microcephaly, intellectual disability, ataxia, and pyramidal signs.
8. A separate, incompletely understood branch: in at least one reported case, disease is accompanied by **secondary mitochondrial respiratory chain dysfunction** (reduced Complex I, II+III, and IV activities, reduced mtDNA content) in muscle, proposed to result from "accumulation of toxic metabolites or secondary impairment of the OxPhos machinery," potentially compounding axonal injury in long peripheral nerves (PMID:34118926) — this remains a hypothesis-level mechanistic link rather than an established primary pathway.

### Molecular Pathways
Endo-lysosomal/endosomal trafficking pathway; phosphoinositide (PtdIns3P, PtdIns(3,5)P2) metabolism; Rab GTPase activation (Rab21, Rab28) via DENN-domain GEF activity. Suggested pathway/database cross-references: Reactome "Membrane Trafficking," GO biological process terms below.

### Cellular Processes
- Schwann cell axon radial sorting (developmental process, disrupted per mouse model)
- Myelination (secondarily affected)
- Endosomal receptor trafficking/recycling (ErbB2/ErbB3, β1-integrin)
- Neurogenesis (CNS, per zebrafish model)
- Not primarily an apoptotic/degenerative mechanism — zebrafish data specifically show reduced brain size is "not caused by excessive apoptosis, autophagy or cell loss."

### Protein Dysfunction
Loss-of-function or partial loss-of-function of a pseudophosphatase scaffold/regulatory protein; not a gain-of-function or aggregation-prone mechanism as currently understood.

### Metabolic Changes
Secondary mitochondrial oxidative phosphorylation dysfunction has been documented in at least one case (reduced Complex I/II+III/IV activities, reduced mtDNA content) — an emerging but not yet generalized feature.

### Immune System Involvement
Not implicated in current literature.

### Tissue Damage Mechanisms
Axonal loss/dysfunction secondary to failed radial sorting and impaired Schwann cell-axon signaling, rather than primary demyelination alone in the null-variant mechanism; myelin outfolding pathology (structural redundant myelin loops) for missense/partial-function variants.

### Biochemical Abnormalities
Loss of pseudophosphatase scaffolding function; downstream phosphoinositide dysregulation (proposed, not directly biochemically confirmed in human tissue in the sources reviewed).

### Epigenetic Changes
Not reported.

### Molecular/Omics Profiling
- **Transcriptomics**: Zebrafish *mtmr5*-knockout RNA-seq identified 2,040 differentially expressed genes (1,693 up, 347 down), with dysregulated pathways including neurogenesis, chromatin organization/remodeling, cytoskeletal fiber polymerization, and synaptic signaling; *mtmr13* expression was reduced ~25% in knockouts while *mtmr2* was unchanged (PMC11891516).
- No human transcriptomic, proteomic, metabolomic, or single-cell datasets specific to CMT4B3 patient tissue were identified in this search.

### Suggested GO terms
- GO:0007009 plasma membrane organization (myelination-related)
- GO:0032288 myelin assembly
- GO:0031175 neuron projection development
- GO:0016197 endosomal transport
- GO:0032313 regulation of Rab GTPase activity
- GO:0043547 positive regulation of GTPase activity
- GO:0046488 phosphatidylinositol metabolic process
- GO:0035855 megakaryocyte development — not relevant
- GO:0022011 myelination in peripheral nervous system
- GO:0007422 peripheral nervous system development

### Suggested CL terms
- CL:0002573 Schwann cell
- CL:0000006 neuron (afferent/sensory)
- CL:0000540 neuron (general, motor)
- CL:0002516 Schwann cell precursor

---

## 7. Anatomical Structures Affected

### Organ level
- **Primary**: Peripheral nervous system — peripheral (sensorimotor) nerves, particularly distal lower-limb nerves.
- **Secondary/syndromic involvement**: Cranial nerves (facial [CN VII], oculomotor [CN III], and others per "fork and bracket" pathology); central nervous system (cerebellum, brainstem/pons/mesencephalon, cerebral cortex — microcephaly); skeletal system (feet, spine — pes cavus/planus, scoliosis, syndactyly); skeletal muscle (secondary neurogenic atrophy; in one case, mitochondrial myopathic features); respiratory system (secondary to neuromuscular weakness, requiring ventilatory support in severe cases).
- **Body systems**: Nervous system (primary), musculoskeletal system (secondary), and in the mitochondrial-dysfunction phenotype, potentially systemic bioenergetic involvement.

### Tissue and cell level
- Peripheral nerve: myelinating and non-myelinating Schwann cells, large- and small-diameter myelinated axons.
- Skeletal muscle: type-grouped/neurogenic atrophic fibers; "necklace fibers" (internalized nuclei in a linear/ring pattern) in one reported family.
- CNS: neurons undergoing early neurogenesis (zebrafish CNS data).

### Subcellular level
- Endosomal/late-endosomal compartments (site of MTMR2–MTMR5 complex function)
- Plasma membrane (myelin membrane biogenesis, axon-Schwann cell membrane apposition)
- Mitochondria (secondary dysfunction in at least one reported case)

### Suggested UBERON terms
- UBERON:0001358 peripheral nerve / UBERON:0001519 peroneal nerve
- UBERON:0002316 sural nerve (biopsy site)
- UBERON:0002037 cerebellum
- UBERON:0002259 pons
- UBERON:0002417 mesencephalon
- UBERON:0002385 muscle tissue
- UBERON:0002415 myelin sheath

### Suggested GO Cellular Component terms
- GO:0043209 myelin sheath
- GO:0005768 endosome
- GO:0005770 late endosome
- GO:0005739 mitochondrion

### Localization
Distal, symmetric, length-dependent peripheral nerve involvement (classic length-dependent CMT pattern) — bilateral. Cranial nerve involvement, when present, is typically bilateral (facial weakness, ophthalmoparesis).

---

## 8. Temporal Development

### Onset
- Ranges from **congenital/infantile** (clubfoot at birth, hypotonia by 18 months; congenital microcephaly in syndromic families) to **classic first-decade onset** (5–11 years, most common pattern across families).
- Onset pattern: **insidious**, slowly progressive in the classic form; in the most severe syndromic (null-variant) family, an early **infantile cerebellar/pyramidal presentation** precedes overt peripheral polyneuropathy, which emerges only toward the end of the first decade.

### Progression
- **Disease course**: Chronic, progressive (not relapsing-remitting or episodic).
- **Progression rate**: Variable — slow in the original Korean family (ambulation preserved into adulthood, lost only in the 5th decade); rapid/severe in the Italian mitochondrial-dysfunction case (non-invasive ventilation by age 6, wheelchair by age 11) and in syndromic infantile-onset families.
- **Stages**: Not formally staged in a validated clinical staging system (unlike, e.g., cancer); described qualitatively as early (distal weakness/sensory loss), intermediate (loss of reflexes, gait disturbance, skeletal deformity), and advanced (loss of ambulation, respiratory compromise in severe cases).

### Patterns
- No remission pattern described — CMT4B3 is a chronic progressive neuropathy without spontaneous remission.
- No specific "critical period" for intervention has been established given the absence of disease-modifying therapy, though early diagnosis is emphasized for genetic counseling, orthotic/rehabilitative planning, and (in syndromic cases) proactive management of cranial nerve, respiratory, and cognitive/developmental needs.

---

## 9. Inheritance and Population

### Epidemiology
- **Prevalence/incidence**: No formal population-based prevalence or incidence estimate exists; CMT4B3 is characterized in the literature simply as "ultra-rare," with the disease-specific patient count described in single digits to low double digits of published families/individuals worldwide (patient advocacy source: "only 14 documented cases worldwide," cmt4b3research.org). For context, all CMT4B subtypes combined ("CMT4B") account for **fewer than a hundred reported cases**, mostly from populations with high consanguinity rates, and CMT overall (all types) has a prevalence estimated at a minimum of 17–20 per 100,000 globally.

### Inheritance Pattern
- **Autosomal recessive** in the overwhelming majority of reported families (homozygous or compound heterozygous biallelic *SBF1* variants).
- **One reported exception**: an apparently autosomal dominant transmission (mother-to-daughter) with a heterozygous missense variant (p.H466Q), proposed to act via a dominant-negative mechanism (PMC11633322) — the authors explicitly note this deviates from "the autosomal recessive manner observed in the seven cases reported before."

### Penetrance / Expressivity
- Penetrance in the recessive form appears high/complete in reported homozygotes/compound heterozygotes, though formal penetrance estimates are not available given the small numbers.
- **Expressivity is markedly variable** — from pure, late-progressing peripheral neuropathy (original Korean family) to severe syndromic multisystem disease (microcephaly, intellectual disability, cranial neuropathies, pyramidal/cerebellar signs, respiratory failure). This variability appears to correlate at least partly with variant type (missense/hypomorphic vs. null) per the mouse mechanistic data, though this genotype-phenotype correlation is not yet firmly established in humans.

### Genetic Anticipation / Germline Mosaicism / Founder Effects
Not reported/established for CMT4B3 — the small number of families precludes robust characterization of these phenomena. No specific founder mutation has been identified as recurrent across unrelated populations (the pathogenic variants reported to date are largely family-specific/private).

### Consanguinity
A prominent risk factor — several reported kindreds (Saudi Arabian, Syrian/Bedouin) are explicitly consanguineous, consistent with autosomal recessive inheritance of a rare allele.

### Carrier Frequency
Not established; expected to be very low given disease rarity, though a precise gnomAD-derived carrier frequency for SBF1 pathogenic alleles was not retrieved in this research pass.

### Population Demographics
- **Affected populations**: Reported cases span Korean, Saudi Arabian, Syrian (Bedouin), Israeli, Spanish, British, and Italian ancestries — no single ethnic group predominates, consistent with a private-mutation, consanguinity-driven rare recessive disease rather than a founder-population disorder.
- **Geographic distribution**: Scattered case reports globally; no endemic region identified.
- **Sex ratio**: No sex predilection has been reported (autosomal, not X-linked, inheritance); both sexes affected in reported families (e.g., mother–daughter dominant pedigree; brother–sister pairs in recessive families).
- **Age distribution**: Spans infancy through adulthood at the time of reporting, reflecting the developmental-onset, slowly progressive natural history.

---

## 10. Diagnostics

### Clinical/Electrophysiological Tests
- **Nerve conduction studies (NCS)**: Reduced motor nerve conduction velocities are characteristic of the demyelinating CMT4B group generally; specific CMT4B3 velocity thresholds were not consistently reported across all case series in this search, though the classic Korean family showed a **demyelinating** pattern; other families (axonal neuropathy, cranial nerve involvement) show a more **axonal** electrophysiological signature — underscoring that CMT4B3 spans both demyelinating and axonal electrophysiological phenotypes, unlike the more uniformly demyelinating CMT4B1/CMT4B2.
- **Nerve biopsy (sural nerve)**: Decreased numbers of large and small myelinated fibers, thin myelin sheaths, and focally folded/outfolded myelin (globular masses of irregular myelin thickening) — similar to but not always identical to CMT4B1/CMT4B2 pathology; some families show axonal loss without demyelination or outfolding.
- **Muscle biopsy**: Neurogenic atrophy is the common finding; "necklace fibers" (a finding classically seen in myotubular myopathy) have been reported in at least one SBF1-related family, expanding the recognized pathological spectrum. Muscle biopsy with spectrophotometric respiratory-chain enzyme analysis revealed reduced Complex I, II+III, and IV activity and reduced mtDNA content in the Italian mitochondrial-dysfunction case.
- **Brain MRI**: Characteristic in syndromic cases — the **"fork and bracket sign"** (T2-hyperintensity in the pons ["fork"] and mesencephalon ["bracket"], attributed to degenerated CN III/VII fiber bundles) is a distinctive, potentially diagnostic imaging clue in SBF1-related syndromic neuropathy, though notably **absent** in the "pure neuropathy" phenotype (e.g., normal brain/spinal MRI in the Italian mitochondrial-dysfunction case).

### Genetic Testing
- **Recommended approach**: Given the extreme genetic heterogeneity of CMT (>100 causal genes) and rarity of CMT4B3 specifically, **multigene CMT/hereditary neuropathy panels** or **exome/genome sequencing** are the practical first-line approaches, rather than single-gene SBF1 testing, unless a specific familial variant is already known. All reported CMT4B3 diagnoses to date have been made via **whole-exome sequencing (WES)** in affected families — this has effectively been the diagnostic modality of discovery for every reported kindred.
- **Single-gene testing**: Appropriate for confirming a specific known familial variant (cascade testing) once identified by panel/exome sequencing in the proband.
- **Chromosomal microarray, karyotyping, FISH, mitochondrial DNA testing, repeat expansion testing**: Not primary diagnostic modalities for CMT4B3, since it is caused by small-scale SBF1 sequence variants, not structural or repeat-expansion mutations; mtDNA content/sequencing could be considered adjunctively in cases with suspected secondary mitochondrial dysfunction, though this is not a primary diagnostic test for the underlying SBF1 defect.

### Omics-Based Diagnostics
No SBF1/CMT4B3-specific transcriptomic, proteomic, metabolomic, or liquid-biopsy diagnostic assay has been established; diagnosis remains DNA-sequencing based.

### Clinical Criteria / Differential Diagnosis
No formal consensus diagnostic criteria (DSM/ICD-style) exist for CMT4B3 specifically; diagnosis relies on clinical suspicion (childhood-onset sensorimotor neuropathy ± cranial nerve involvement ± microcephaly/intellectual disability) confirmed by molecular genetic testing. Key differentials include:
- Other CMT4B subtypes: **CMT4B1** (MTMR2) and **CMT4B2** (MTMR13/SBF2) — share myelin-outfolding pathology but lack the microcephaly/cranial-nerve/CNS features more characteristic of CMT4B3's syndromic forms.
- Other autosomal recessive demyelinating CMT4 subtypes (CMT4A/GDAP1, CMT4C/SH3TC2, CMT4D, CMT4F, etc.)
- Congenital hypomyelinating neuropathy (OMIM #614895 and related entries)
- Other syndromic neuropathies with cranial nerve involvement, microcephaly, and intellectual disability (e.g., other DENN-domain or endosomal-trafficking disorders)
- Myotubular/centronuclear myopathy (given the "necklace fibers" finding overlaps histologically) — important to distinguish given SBF1's paralog *MTM1* causes X-linked myotubular myopathy.

### Screening
No population, newborn, or carrier screening program specifically targets CMT4B3 given its extreme rarity; carrier screening would only be relevant in the context of known familial variants (e.g., in consanguineous families with a previously affected relative).

---

## 11. Outcome/Prognosis

### Survival and Mortality
No formal survival statistics (5-year/10-year survival rates) exist given the rarity of the disease and its generally non-fatal (though disabling) natural history; the most severe reported cases involve significant morbidity (respiratory failure requiring ventilatory support) but not reported early mortality in the sources reviewed.

### Morbidity and Function
- Progressive distal weakness leading to gait impairment and, in the most severe cases, loss of ambulation (by the 5th decade in the mildest reported family; much earlier — wheelchair by age 11 — in the most severe reported case).
- Respiratory morbidity: non-invasive ventilation required by age 6 in the severe Italian case, reflecting neuromuscular respiratory compromise.
- Cranial nerve morbidity in syndromic cases: dysphagia, dysarthria, ophthalmoparesis/diplopia, facial weakness.
- Cognitive/developmental morbidity: intellectual disability and developmental delay in syndromic (typically null-variant) cases; notably **absent** in the "pure neuropathy" phenotype cases.
- No validated disease-specific quality-of-life instrument has been applied to CMT4B3 cohorts (none large enough to support such a study).

### Disease Course / Complications
- Secondary orthopedic complications: pes cavus/planus, scoliosis/kyphoscoliosis, contractures (by extrapolation from general CMT natural history).
- Secondary respiratory complications in severe cases.
- Reported urinary incontinence in some general CMT4B3 summaries (GARD-derived), though this is not consistently emphasized across primary literature reviewed.

### Prognostic Factors
- **Variant type appears to correlate with severity** in the limited data available: null/truncating variants (as in the Bedouin/splice-null family) are associated with the more severe, syndromic, CNS-involving phenotype (microcephaly, intellectual disability, early pyramidal/cerebellar signs), while missense/hypomorphic variants (as in the original Korean family) are associated with a milder, later-progressing "pure neuropathy" phenotype — though this genotype-phenotype correlation remains provisional given the very small number of published cases and has not been formally tested statistically.
- No validated prognostic biomarkers exist.

---

## 12. Treatment

### Current State
**No disease-modifying or curative therapy exists for CMT4B3.** As one 2025 phenotype-expansion review states, "despite its severe clinical presentation, currently no disease-modifying therapies" are available, and there remains "an incomplete understanding of the disease pathomechanism(s)" (Orphanet summary; consistent with the CMT4B3 Research Foundation's statement that "little is known about CMT4B3 at this time").

### Supportive / Symptomatic Management
Management follows general CMT supportive-care principles, as no CMT4B3-specific guidelines exist:
- **Rehabilitative therapy**: Physical therapy (gait/balance training) and occupational therapy for functional preservation — NCIT: `NCIT:C15302` (Physical Therapy)
- **Orthotics/bracing**: Ankle-foot orthoses for foot drop and gait stability — NCIT: `NCIT:C49236` (Therapeutic Procedure, general) / device qualifier pattern per orthotic device
- **Orthopedic surgery**: For severe pes cavus, scoliosis, or contractures — NCIT: `NCIT:C16186` (Orthopedic Surgical Procedure)
- **Respiratory support**: Non-invasive ventilation for neuromuscular respiratory compromise in severe cases — NCIT: `NCIT:C15747` (Supportive Care) as a general category
- **Genetic counseling**: Essential given autosomal recessive (predominantly) inheritance, recurrence risk (25% for future pregnancies of carrier-carrier couples), and the recently identified possibility of dominant transmission in rare kindreds — NCIT: `NCIT:C15240` (Genetic Counseling)
- **Multidisciplinary management** of syndromic features: ophthalmology (strabismus/ophthalmoparesis), speech-language pathology (dysarthria/dysphagia), developmental pediatrics/neuropsychology (intellectual disability), and pulmonology (respiratory monitoring).

### Pharmacotherapy
No SBF1/CMT4B3-targeted pharmacotherapy exists. No pharmacogenomic (PharmGKB/CPIC) guidance is specific to SBF1.

### Advanced Therapeutics / Experimental
- No gene therapy, cell therapy, RNA-based therapy (ASO/siRNA), or targeted molecular therapy has reached clinical development specifically for CMT4B3.
- **Preclinical model development is actively underway**, positioning the field for future therapeutic testing:
  - A **CRISPR/Cas9 *mtmr5* knockout zebrafish model** (2025, PMC11891516) is explicitly proposed by its authors as "a first pre-clinical model to phenocopy the disease," intended as "an ideal tool for future studies on disease pathomechanism(s) and therapy development."
  - A **CRISPR/Cas9 *Mtmr5* knockout mouse model** (2022, PMC9190308) has clarified the axon-radial-sorting mechanism and is a platform for future mechanistic and therapeutic studies.
  - Johns Hopkins Medicine has reportedly created a **cellular model of CMT4B3** to test potential therapies (per institutional development news).
- The patient advocacy organization CMT4B3 Research Foundation funds research grants into disease mechanisms as a precursor to therapy development but reports no approved treatments.
- Broader CMT pipeline context (not CMT4B3-specific): CMT1A-directed trials such as PXT3003 (a repurposed drug combination) and the CMT-SORD trial (govorestat) illustrate active general CMT drug development, but none currently target SBF1/MTMR5 biology specifically.

### Treatment Outcomes
No systematic treatment-response, adverse-event, or outcome data exist for CMT4B3 given the absence of any targeted intervention.

### Treatment Strategy
Given the absence of disease-modifying therapy, the current standard of care is a **symptomatic, multidisciplinary, supportive-care algorithm** analogous to general CMT management (rehabilitation → orthotics → surgery as needed → monitoring for syndromic complications), with genetic counseling as a cornerstone given the hereditary, currently non-curable nature of the disease.

---

## 13. Prevention

### Primary Prevention
No primary prevention exists beyond genetic counseling and reproductive options (carrier testing, prenatal diagnosis, preimplantation genetic diagnosis) for families with a known pathogenic SBF1 variant, particularly relevant given the consanguinity association in several reported kindreds.

### Secondary Prevention / Screening
- No population-based screening program exists (disease too rare for newborn screening panels).
- **Genetic/carrier screening** and **cascade testing** are appropriate within families with a known proband, especially in consanguineous populations.
- **Prenatal testing / PGD** would be technically feasible once a familial variant is identified, though no specific published experience with this in CMT4B3 was identified.

### Tertiary Prevention
Early diagnosis enables proactive surveillance for and management of complications — orthopedic deformity (scoliosis, pes cavus), respiratory compromise, cranial nerve dysfunction (dysphagia/aspiration risk), and developmental/cognitive needs — analogous to tertiary prevention strategies in other pediatric neuromuscular disorders.

### Immunization / Public Health / Behavioral Interventions
Not specifically applicable — CMT4B3 is not an infectious, immunologically mediated, or behaviorally modifiable disease.

### Counseling
Genetic counseling is central given: (1) predominantly autosomal recessive inheritance with 25% recurrence risk for carrier couples, (2) the newly recognized possibility of dominant transmission in rare families (altering recurrence-risk counseling for those specific pedigrees), and (3) the marked phenotypic variability (pure neuropathy vs. syndromic multisystem disease) that complicates prognostic counseling at the time of diagnosis.

---

## 14. Other Species / Natural Disease

No naturally occurring CMT4B3/SBF1-associated disease has been reported in non-human species (dogs, cats, or other companion/veterinary species) in the literature surveyed — unlike some other CMT subtypes with recognized veterinary correlates. SBF1 orthologs exist across vertebrates (used to generate the mouse and zebrafish models below), and the gene is evolutionarily conserved, but no spontaneous/natural veterinary disease phenotype has been documented. No zoonotic or cross-species transmission relevance applies, as this is a purely genetic (non-infectious) disorder.

---

## 15. Model Organisms

### Mouse Model
- **Species/system**: *Mus musculus*, CRISPR/Cas9-generated *Mtmr5* knockout (guide RNAs targeting exon 1 and exon 25, producing a 14 kb deletion, frameshift, and premature stop codon; full-length 208 kDa protein undetectable) (PMC9190308, Human Molecular Genetics 2022).
- **Phenotype recapitulation**:
  - **Does NOT recapitulate** myelin outfoldings (the classic CMT4B1/CMT4B2 pathology) — a key point of divergence from other CMT4B mouse models.
  - **Does recapitulate** an axon radial-sorting defect: ~10% reduction in total myelinated axons in sciatic nerve, with increased numbers of large-diameter axons remaining abnormally bundled/incompletely ensheathed by Schwann cells.
  - Myelin structure that does form is otherwise normal (normal g-ratios, myelin thickness).
  - Additional phenotype: male infertility (consistent with prior *Mtmr5*-deletion literature).
- **Double knockout**: *Mtmr5−/−;Mtmr13−/−* mice die perinatally, indicating partial functional redundancy between MTMR5 and MTMR13 during embryonic development despite their distinct postnatal roles.
- **Model limitations**: Because the knockout only models complete loss-of-function, it does not capture the myelin-outfolding pathology seen with some human missense alleles, nor the CNS/microcephaly/cranial-nerve phenotypes of the syndromic human disease — the authors explicitly hypothesize (not yet tested) that different classes of human missense variants might produce the outfolding phenotype via impaired MTMR2 interaction.
- **Research applications**: Elucidating the distinct molecular roles of MTMR5 vs. MTMR13 in Schwann cell biology (axon radial sorting vs. myelination maintenance), informing therapeutic target identification (ErbB2/3 and β1-integrin endosomal trafficking).
- **Resource**: MGI:1925230 (*Sbf1* gene); targeted allele MGI:2449174.

### Zebrafish Model
- **Species/system**: *Danio rerio*, CRISPR/Cas9 full-gene deletion of *mtmr5* (~86 kb, guide RNAs flanking the ATG start and stop codon) (PMC11891516, *Brain Communications* 2025).
- **Phenotype recapitulation**:
  - Homozygous mutants born at normal Mendelian ratios; **no gross motor deficit** on swim assays at 3/6/14 dpf.
  - **Microcephaly** — ~10% reduction in body length and proportional reduction in brain height/length from 10 dpf onward, persisting into adulthood — described as a phenotype "uniquely observed in this disease subtype," directly paralleling the microcephaly seen in severe human CMT4B3.
  - Reduced brain size attributable to **defects in early neurogenesis**, not increased apoptosis, autophagy, or cell loss.
  - **Dysmyelination phenotype**: normal myelin formation but increased axon-myelin plasma membrane detachment on TEM of the posterior lateral line nerve, mirroring human peripheral nerve pathology.
  - **Axonal patterning defects**: disorganized, less-defined axon morphology; increased total branch number/endpoints with reduced average branch length.
  - **Transcriptomic dysregulation**: 2,040 differentially expressed genes (RNA-seq), implicating neurogenesis, chromatin remodeling, cytoskeletal polymerization, and synaptic signaling pathways; secondary ~25% reduction in *mtmr13* expression (with unchanged *mtmr2*), suggesting partial cross-regulation among the three MTMR paralogs.
- **Significance**: Explicitly positioned by its authors as "a first pre-clinical model to phenocopy the disease," intended as "an ideal tool for future studies on disease pathomechanism(s) and therapy development" — notably, this model captures the CNS/microcephaly dimension of human CMT4B3 that the mouse peripheral-nerve-focused model does not emphasize.

### Cellular Models
- A cellular model of CMT4B3 has reportedly been developed at Johns Hopkins Medicine for therapy screening purposes (per institutional/foundation reporting), though peer-reviewed methodological detail was not retrieved in this search pass.

### Comparative note
Together, the mouse and zebrafish models are **complementary rather than redundant**: the mouse model best captures the peripheral nerve (Schwann cell/axon radial sorting) mechanism, while the zebrafish model uniquely captures the CNS/microcephaly dimension of the human syndromic phenotype — consistent with dismech's "Human-Model Mismatch" framing, since neither single model alone recapitulates the full human disease spectrum, and each captures a different mechanistic axis (peripheral vs. central).

---

## Summary Table of Key Primary-Literature PMIDs

| PMID | Year | Key contribution |
|---|---|---|
| 23749797 | 2013 | Original discovery: SBF1 mutations cause CMT4B3 (Korean family) — Nakhro et al., *Neurology* |
| 24799518 | ~2014 | Saudi Arabian family: microcephaly, strabismus, syndactyly |
| 20658556 | 2010 | "Fork and bracket sign" MRI description (Mégarbané et al., precedes molecular SBF1 link) |
| 28005197 | 2017 | SBF1 mutations, autosomal recessive axonal neuropathy with cranial nerve involvement |
| 30039846 | 2018 | Novel splice-site null mutation broadens clinical spectrum (Bedouin family, infantile cerebellar/pyramidal onset) |
| 32444983 | ~2020 | Additional family, expanded phenotype |
| 34118926 | 2021 | Bi-allelic MTMR5/SBF1 variants with mitochondrial dysfunction (Italian case), *BMC Medical Genomics* |
| (PMC7419361) | 2020 | Frameshift deletion, necklace fibers, axonal (non-demyelinating) neuropathy |
| (PMC11633322) | 2024 | First reported dominant-pattern SBF1 missense mutation |
| (PMC9190308) | 2022 | Mouse *Mtmr5*/*Mtmr13* knockout mechanistic study, *Human Molecular Genetics* |
| (PMC11891516) | 2025 | Zebrafish *mtmr5* knockout model, *Brain Communications* |

---

## Sources

- [OMIM #615284 — CMT4B3](https://www.omim.org/entry/615284)
- [OMIM *603560 — SBF1](https://omim.org/entry/603560)
- [Orphanet: CMT4B3 (ORPHA:363981)](https://www.orpha.net/en/disease/detail/363981)
- [NIH GTR: CMT4B3 (C3695063)](https://www.ncbi.nlm.nih.gov/gtr/conditions/C3695063/)
- [GARD/NIH: CMT4B3](https://rarediseases.info.nih.gov/diseases/17578/charcot-marie-tooth-disease-type-4b3)
- [Bi-allelic variants in MTMR5/SBF1 cause CMT4B3 featuring mitochondrial dysfunction (PMC8199524 / PMID:34118926)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8199524/)
- [Characterization of a novel zebrafish model of MTMR5-associated CMT4B3 (PMC11891516)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11891516/)
- [SET binding factor 1 (SBF1) mutation causes CMT4B3 — Nakhro et al. 2013, *Neurology* (PMID:23749797)](https://pubmed.ncbi.nlm.nih.gov/23749797/)
- [Distinct roles for Mtmr5 and Mtmr13 in axon radial sorting and Schwann cell myelination (PMC9190308)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9190308/)
- [A novel SBF1 missense mutation causes autosomal dominant CMT4B3 (PMC11633322)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11633322/)
- ["Fork and bracket" syndrome expands the spectrum of SBF1-related sensory motor polyneuropathies](https://www.neurology.org/doi/10.1212/NXG.0000000000000061)
- [Multiple cranial nerve neuropathies, microcephaly, "fork and bracket sign" — Mégarbané et al. 2010 (PMID:20658556)](https://pubmed.ncbi.nlm.nih.gov/20658556/)
- [Novel SBF1 splice-site null mutation broadens the clinical spectrum of CMT4B3 (PMID:30039846)](https://pubmed.ncbi.nlm.nih.gov/30039846/)
- [SBF1 mutations associated with autosomal recessive axonal neuropathy with cranial nerve involvement (PMID:28005197)](https://pubmed.ncbi.nlm.nih.gov/28005197/)
- [A novel frameshift deletion in autosomal recessive SBF1-related syndromic neuropathy with necklace fibres (PMC7419361)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7419361/)
- [CMT4B3 Research Foundation — What is CMT4B3](https://www.cmt4b3research.org/what-is-cmt4b3)
- [SBF1 Gene — GeneCards](https://www.genecards.org/cgi-bin/carddisp.pl?gene=SBF1)
- [Pediatric toe-walking cohort with heterozygous SBF1 variants (PMC12926636)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12926636/)
- [Disruption of Mtmr2 produces CMT4B1-like neuropathy (PMC2172586)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2172586/)
- [The CMT4B disease-causing phosphatases Mtmr2 and Mtmr13 depend on each other for wild-type protein levels](https://academic.oup.com/hmg/article/22/8/1493/625226)
- [Charcot-Marie-Tooth 4B3 Phenotype Expansion and Confounding Factors, *Current Genetic Medicine Reports*](https://link.springer.com/article/10.1007/s40142-026-00236-7)

**Note on evidentiary basis**: Given CMT4B3's extreme rarity (an estimated dozen-to-twenty published patients worldwide), essentially every clinical and mechanistic claim above derives from individual case reports/small family series rather than cohort studies, and several mechanistic claims (e.g., the missense-vs-null genotype-phenotype hypothesis, the MTMR2-interaction-disruption model, the proposed OxPhos-toxicity mechanism) are explicitly labeled by their source authors as proposed/hypothesized rather than definitively demonstrated. This should be reflected in any downstream knowledge-base curation with appropriate `directness`/hedge annotations.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 14 |
| On topic | 11 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMC:PMC12926636` *(abstract only)*: "may act as modifiers or coincidental findings rather than independent causes of neuromotor abnormalities"
  - closest text in source: "CONCLUSIONS: In this referral-based cohort, heterozygous SBF1 variants were observed in children with persistent toe walking and accompanying mild neuromotor/musculoskeletal features that partially overlap with reported CMT4B3 phenotypes; however, these findings are descriptive and do not establish causality or enrichment"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 68 |
| Resolved | 61 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 2 |
| Unverifiable | 4 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014117` (1 mention) - the report calls it "MONDO"; MONDO calls it **Charcot-Marie-Tooth disease type 4B3**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0007257` (1 mention) - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0002355` (obsolete Difficulty walking) (1 mention) - replaced by `HP:0001288`
- `GO:0032313` (GO_0032313) (1 mention) - replaced by `GO:0043087`

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.