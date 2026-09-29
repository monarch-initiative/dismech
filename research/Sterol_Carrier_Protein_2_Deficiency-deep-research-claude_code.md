---
provider: claude_code
model: claude-fable-5, claude-haiku-4-5-20251001
cached: false
start_time: '2026-09-19T02:24:54.860464'
end_time: '2026-09-19T02:27:41.493668'
duration_seconds: 166.63
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: Sterol Carrier Protein 2 Deficiency
  mondo_id: MONDO:0013391
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
  - claude-fable-5
  - claude-haiku-4-5-20251001
  web_search_requests: 3
  num_turns: 8
  total_cost_usd: 4.360779000000001
  session_id: 048d4255-db07-4f05-afc1-cccbde7d1658
  stop_reason: end_turn
  assistant_text_blocks: 3
citation_count: 9
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 11
  quotes_valid: 10
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:15574183
  relevance_assessed: 14
  on_topic: 10
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 36
  verified: 34
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 13
  labels_matching: 4
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: MONDO:0013391
    reported_labels:
    - sterol carrier protein 2 deficiency
    - all quoted sentences above were validated as exact substrings of the cached
      source abstracts
    ontology_label: sterol carrier protein 2 deficiency
  - term_id: HP:0000709
    reported_labels:
    - infection-triggered episodic psychosis
    ontology_label: Psychosis
  - term_id: HP:0034721
    reported_labels:
    - "marked in patients 1\u20132, only mild in patient 3"
    ontology_label: Elevated circulating pristanic acid concentration
  - term_id: HP:6001007
    reported_labels:
    - patient 1
    ontology_label: Elevated urinary bile alcohol level
  labels_variant: 5
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Sterol Carrier Protein 2 Deficiency
- **MONDO ID:** MONDO:0013391 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Sterol Carrier Protein 2 Deficiency** covering all of the
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

I'll research Sterol Carrier Protein 2 Deficiency. This worktree already contains a curated knowledge-base entry for this disease with verified citations, so I'll mine that alongside fresh literature searches.

The local KB entry is thorough and citation-verified. Now let me fill gaps it deliberately left out (OMIM/Orphanet identifiers, patient origins, recent literature) with web searches.

# Research Report: Sterol Carrier Protein 2 Deficiency (SCP2/SCPx Deficiency)

**MONDO:0013391 · Ultra-rare autosomal recessive peroxisomal β-oxidation defect · 3 confirmed patients in the world literature**

An important framing note up front: this is one of the rarest Mendelian disorders described — **only three patients with confirmed biallelic SCP2 variants have ever been published** (2006, 2015, 2023), plus a fourth, disputed, heterozygous case (2022). Nearly every "typical feature," frequency, prognosis, or epidemiology question therefore has the honest answer "not measurable at n=3." The ClinGen Peroxisomal Gene Curation Expert Panel classified the SCP2 gene–disease relationship as **Moderate** (10 points; PMID:37236006), and any knowledge-base entry should be written to that standard. This report flags inference vs. demonstration explicitly throughout.

---

## 1. Disease Information

**Overview.** Sterol carrier protein 2 deficiency is an autosomal recessive, single-enzyme defect of peroxisomal β-oxidation caused by biallelic loss-of-function variants in *SCP2*. The *SCP2* locus is transcribed from two promoters and produces two proteins: the 58-kDa peroxisomal 3-ketoacyl-CoA thiolase **SCPx** and the small (13-kDa) non-specific lipid-transfer protein **SCP2**. The human disease is loss of the thiolase arm (SCPx), which catalyzes the final thiolytic cleavage step of peroxisomal β-oxidation for 2-methyl-branched substrates — pristanic acid degradation and side-chain shortening of C27 bile-acid intermediates. The founding report describes "the first known patient with a deficiency of sterol carrier protein X (SCPx), a peroxisomal enzyme with thiolase activity, which is required for the breakdown of branched-chain fatty acids" (Ferdinandusse et al., *Am J Hum Genet* 2006; **PMID:16685654**).

**Identifiers.**

| Resource | ID |
|---|---|
| MONDO | MONDO:0013391 (sterol carrier protein 2 deficiency) |
| OMIM (phenotype) | [613724 — Leukoencephalopathy with dystonia and motor neuropathy](https://omim.org/entry/613724) |
| OMIM (gene) | [*184755 — SCP2](https://omim.org/entry/184755) |
| Orphanet | ORPHA:163684 |
| ICD-10-CM | No specific code; closest is E71.548 (Other peroxisomal disorders) — a broad residual category, not an asserted cross-reference |
| HGNC | hgnc:10606 (SCP2), chromosome 1p32.3 |

**Synonyms:** SCP2 deficiency; SCPx deficiency; sterol carrier protein X deficiency; leukoencephalopathy with dystonia and motor neuropathy (LKDMN); leukoencephalopathy-dystonia-motor neuropathy syndrome. The ClinGen Peroxisomal GCEP deliberately renamed the entity: "the disorder associated with SCP2 variants was termed SCP2 deficiency to replace the phenotype-based nomenclature, leukoencephalopathy-dystonia-motor neuropathy syndrome" (**PMID:37236006**) — explicitly to leave room for the phenotype to expand beyond the founding case's features.

**Data derivation:** All clinical knowledge derives from three individually published case reports (individual-patient level), one expert-panel gene curation, and reviews. No registry, cohort, or EHR-level data exist.

## 2. Etiology

**Causal factor:** Biallelic loss-of-function variants in *SCP2*, specifically abolishing (or in one case reducing) SCPx thiolase. Purely genetic; no environmental, infectious, or somatic etiology is known.

**Risk factors:** Parental consanguinity/carrier status is the only established risk context (two of three patients were homozygous). No susceptibility loci, modifier genes, or population risk factors are known. No protective genetic or environmental factors have been reported.

**Gene–environment interaction (inferred, not demonstrated):** The accumulating metabolite, pristanic acid, derives ultimately from dietary phytol/phytanic acid (dairy, ruminant fat, fish), so dietary branched-chain lipid intake is the substrate load on the blocked pathway — the rationale for the phytanic-acid-restricted diet tried in patient 3 (**PMID:37905191**). Additionally, in patient 3 "each episode was triggered by an acute upper respiratory tract infection" (**PMID:37905191**), a pattern reminiscent of infection-triggered metabolic decompensation in other IEMs, but nothing was measured during an episode, so this remains an observation, not a mechanism.

## 3. Phenotypes

With three patients, no frequency bands are meaningful; each feature below is tagged by which patient(s) showed it. The 2023 report's cross-patient comparison identifies only three shared features: "these shared clinical features in SCPx deficiency include stutter, tremors, and symmetrical lesions in the thalamus and brainstem without gadolinium enhancement" (**PMID:37905191**).

**Shared across all 3 patients:**
- **Symmetrical thalamic T2-hyperintense lesions** — HP:0012692 (Focal T2 hyperintense thalamic lesion); bilateral, non-enhancing
- **Brainstem (pontine, "butterfly-like") lesions** — HP:0012748 (Focal T2 hyperintense brainstem lesion)
- **Tremor** — HP:0002346 (Head tremor, dystonic in patient 1); HP:0002080 (Intention tremor)
- **Stuttering** — HP:0025268

**Patient 1 (male, onset ~age 7, reported at 45; PMID:16685654):** "The patient presented with torticollis and dystonic head tremor as well as slight cerebellar signs with intention tremor, nystagmus, hyposmia, and azoospermia." — Torticollis HP:0000473; Nystagmus HP:0000639; Hyposmia HP:0004409; Azoospermia HP:0000027; Leukoencephalopathy HP:0002352; plus a **predominantly motor neuropathy with tibial conduction blocks** (HP:0007178, Motor polyneuropathy) — explicitly *absent* in patients 2 and 3.

**Patient 2 (male, onset in his 30s; PMID:26497993):** hand clumsiness → gait disturbance (Ataxia HP:0001251), deafness (HP:0000365), and MRI changes of **neurodegeneration with brain iron accumulation** (HP:0012675); later an unusual retinal phenotype was described in the same patient (**PMID:28033445**).

**Patient 3 (male, young adult; PMID:37905191):** recurrent **infection-triggered episodic psychosis** (HP:0000709) — "delusions, irritability, aggressive behavior, bursts of uncontrollable laughter, crying, and talking to himself" — and convulsive **status epilepticus** lasting 18 hours (Bilateral tonic-clonic seizure HP:0002069). Previously misdiagnosed as viral encephalitis, cerebral infarction, and mitochondrial encephalopathy across three admissions.

**Laboratory phenotypes (the diagnostic handle):** Elevated circulating pristanic acid HP:0034721 (marked in patients 1–2, only mild in patient 3); mildly elevated phytanic acid HP:0010571; **normal plasma VLCFA**; elevated urinary bile alcohol glucuronides HP:6001007 (patient 1).

**Quality of life:** No formal QoL instruments have ever been applied. The documented burden is chronic neurological disease in all three, disabling motor/psychiatric syndromes in two, and a multi-year diagnostic odyssey in patient 3.

## 4. Genetic/Molecular Information

**Causal gene:** *SCP2* (HGNC:10606; OMIM *184755; 1p32.3). Two promoters, two products: full-length 58-kDa SCPx (thiolase domain + SCP2 domain) and 13-kDa SCP2 (lipid transfer). All three disease genotypes fall in the SCPx-coding region; SCP2 remains transcribed from its own promoter — which is why "SCP2 deficiency" and "SCPx deficiency" name the same disease.

**Reported pathogenic variants (all germline, loss-of-function):**

| Variant | Patient | Zygosity | Consequence |
|---|---|---|---|
| c.545_546insA (p.I184fsX7; ClinVar: NM_002979.5 c.550dup) | 1 | Homozygous | Frameshift/PTC; "no SCPx protein could be detected by western blotting" and absent thiolytic activity in fibroblasts (PMID:16685654) |
| c.121G>T + c.349C>T | 2 | Compound het | Both initially VUS; diagnosis established by near-absent SCPx on immunoblot (PMID:37905191; PMID:38693715) |
| c.674+1G>C | 3 | Homozygous | Splice-donor; "RNA sequencing revealed exon 8 skipping in the mature transcripts of SCP2" — in-frame deletion overlapping the thiolase N-domain, arguably retaining partial function, consistent with the only marginal pristanic elevation (PMID:37905191) |

A fourth, **disputed** case (Alshehri et al. 2022, **PMID:35996156**) carried a single *heterozygous* missense VUS with brainstem neurodegeneration, cardiac dysrhythmia, muscle wasting, and azoospermia; a subsequent review states "it remains to be established whether this patient is truly affected by SCPx deficiency" (**PMID:38693715**), and ClinGen scored only two individuals. Inheritance should be recorded as recessive.

**Population allele frequencies:** No recurrent variant; no gnomAD carrier-frequency estimate has been published. **Modifier genes, epigenetics, chromosomal abnormalities:** none reported (one 1p33-p32.2 contiguous deletion including *SCP2* has been reported with a complex syndromic phenotype, but that is a multi-gene deletion, not this disease — [PMC7647596](https://pmc.ncbi.nlm.nih.gov/articles/PMC7647596/)).

## 5. Environmental Information

No environmental cause. Dietary phytol/phytanic acid is the substrate source for the accumulating metabolite (relevant to management, not causation). Acute respiratory infections preceded each psychotic episode in patient 3 (trigger association only). No toxin, occupational, or lifestyle factor reported.

## 6. Mechanism / Pathophysiology

**Causal chain:**

1. Biallelic *SCP2* loss-of-function variants **lead to** absent (or reduced) peroxisomal 3-ketoacyl-CoA thiolase SCPx — *demonstrated* at protein and activity level in patient fibroblasts (PMID:16685654). [GO:0003988 acetyl-CoA C-acyltransferase activity; GO:0005777 peroxisome]
2. SCPx loss **results in** a block of the thiolytic cleavage of 2-methyl-branched 3-ketoacyl-CoA — the final step of each peroxisomal β-oxidation cycle for branched substrates. *Directly demonstrated in mouse* ("defective thiolytic cleavage of 3-ketopristanoyl-CoA," PMID:9553048); *inferred in humans* from absent fibroblast thiolase activity plus the substrate pattern. [GO:0006635 fatty acid beta-oxidation]
3. The block **causes** (branch A) plasma **pristanic acid accumulation** with only mildly raised phytanic acid and normal VLCFA (PMID:16685654; PMID:38693715) [CHEBI:51340 pristanic acid; CHEBI:16285 phytanic acid], and (branch B) **incomplete side-chain shortening of C27 bile-acid intermediates**, read out as abnormal urinary bile alcohol glucuronides (PMID:16685654) [GO:0006699 bile acid biosynthetic process]. Branch B has been biochemical only — no liver disease reported in any patient.
4. The metabolic derangement **is attributed to cause** the symmetrical thalamic/brainstem/white-matter lesions and the neurological syndrome. **This final step is an attribution, not a demonstrated mechanism**: no neuropathology, brain metabolite measurement, spectroscopy, or metabolite–imaging correlation exists in any patient; indeed patient 3 had the same lesion pattern with only marginally elevated pristanic acid, arguing against simple dose–response. This is the field's principal knowledge gap.

**Differential biochemistry within the pathway:** the profile (pristanic ↑↑, phytanic ~normal/mild ↑, VLCFA normal) distinguishes SCPx deficiency from adult Refsum disease (α-oxidation block one step earlier — phytanic accumulates) and from D-bifunctional protein deficiency/X-ALD (VLCFA accumulate). "Pristanic acid was markedly elevated in the patient's plasma, whereas phytanic acid was only mildly elevated. Plasma VLCFA were normal" (**PMID:38693715**).

**Cell types/subcellular:** the lesion is in the peroxisomal matrix (GO:0005777) of essentially all cells; fibroblasts are the diagnostic cell system. *SCP2* is most highly expressed in cholesterol-trafficking tissues (liver, adrenal, testis — plausibly relevant to azoospermia, but untested). No transcriptomic, proteomic, single-cell, or spatial profiling of any patient tissue has been published (the disputed heterozygous case included fibroblast lipidomics/transcriptomics, PMID:35996156, but that case's status is uncertain).

## 7. Anatomical Structures Affected

- **Primary:** central nervous system — thalamus (UBERON:0001897), pons/brainstem (UBERON:0000988, UBERON:0002298), cerebral white matter (UBERON:0002437). Lesions are bilateral and symmetrical.
- **Variably:** peripheral motor nerves (patient 1); inner ear (patient 2, deafness); retina (patient 2); testis (patient 1, azoospermia; UBERON:0000473).
- **Biochemically:** liver/bile-acid synthesis (urinary bile alcohols) without clinical liver disease.
- **Subcellular:** peroxisome (GO:0005777).

## 8. Temporal Development

Onset spans childhood to adulthood: age 7 (patient 1), age 30 (patient 2), "young, not clear" (patient 3, whose stutter and tremor predated the first documented episode) (comparison table, PMID:37905191). Course: slowly progressive dystonia/ataxia in patients 1–2 over decades; episodic-relapsing psychiatric course in patient 3, each episode remitting over 3–6 months. No staging, no natural-history study, no established critical windows.

## 9. Inheritance and Population

- **Inheritance:** Autosomal recessive (HP:0000007). Penetrance and expressivity: unknown (no unaffected biallelic carrier known to argue from; phenotypes too dissimilar to characterize a range). No anticipation, founder effect, or germline mosaicism reported.
- **Epidemiology:** No prevalence or incidence estimate exists; the literature contains 3 confirmed patients (all male) plus 1 disputed. Orphanet-style class would be <1/1,000,000, but no figure has been published — a KB should record `CASES_IN_LITERATURE`.
- **Carrier frequency, population/geographic distribution:** never measured; no claims should be made.

## 10. Diagnostics

1. **Plasma branched-chain fatty-acid profile** (first-line, and the step commonly skipped): raised pristanic acid, disproportionately low phytanic acid, **normal VLCFA** — meaning a VLCFA-only peroxisomal screen will *miss* this disease. ACMG technical standard: "The current diagnostic approach relies heavily on biochemical genetic tests measuring peroxisomal metabolites, including very long-chain and branched-chain fatty acids in plasma and plasmalogens in red blood cells" (**PMID:31822849**). Pristanic elevation localizes the pathway, not the gene (ACOX2, D-bifunctional protein, and AMACR defects share the stream).
2. **Urinary bile alcohol glucuronides** (supportive; reported in patient 1).
3. **Fibroblast SCPx immunoblot + thiolytic activity assay** — the confirmatory test, and what converted two VUS into a diagnosis in patient 2. Per ACMG: "When next-generation sequencing is used as a first-tier test, evaluation of peroxisome metabolism is often necessary to assess the significance of unknown variants" (**PMID:31822849**).
4. **Molecular testing:** WES identified the variant in patient 3; *SCP2* appears on Genomics England PanelApp inherited-white-matter-disorders and hereditary-neuropathy panels ([PanelApp](https://panelapp.genomicsengland.co.uk/panels/42/gene/SCP2/)). RNA sequencing proved the splice consequence in patient 3.
5. **Brain MRI:** symmetrical, non-enhancing T2-hyperintense thalamic and pontine ("butterfly") lesions — not diagnostic alone, but the pattern that should trigger the metabolic workup; it was repeatedly misread in patient 3.

**Differential diagnosis:** adult Refsum disease, AMACR deficiency, D-bifunctional protein deficiency, X-ALD, Leigh syndrome/mitochondrial encephalopathy (patient 3's initial misdiagnosis), viral encephalitis, NBIA disorders (patient 2). No newborn or carrier screening exists.

## 11. Outcome/Prognosis

No survival, mortality, or disability data exist — no patient death has been reported and no natural history described. Documented courses: decades-long slowly progressive movement disorder (patients 1–2); remitting-relapsing psychiatric episodes responsive to antipsychotics (patient 3). The only prognostic hypothesis in the literature is genotype-based: residual enzyme function (patient 3's in-frame splice product) may correlate with milder biochemistry — a single-patient inference.

## 12. Treatment

No disease-modifying therapy is established. What has been tried:

- **Phytanic-acid-restricted diet** (NCIT:C15447, Dietary Intervention): "the patient was discharged while being placed on a phytanic acid-restricted diet" (**PMID:37905191**). Mechanistically reasonable (limits substrate for pristanic acid formation, by analogy with Refsum disease), but **no outcome has ever been reported** in this disease.
- **Symptomatic pharmacotherapy** (NCIT:C15986): "Psychiatric symptoms gradually improved after 3-6 months of treatment with antipsychotic drugs such as olanzapine or quetiapine" (**PMID:37905191**); status epilepticus terminated with diazepam.
- No gene therapy, ERT, RNA therapy, transplant, or clinical trial (no NCT/ICTRP registration) exists for this disease.

## 13. Prevention

No primary prevention. Genetic counseling for autosomal recessive recurrence (25%) and cascade carrier testing in affected families are the applicable measures; prenatal/preimplantation diagnosis is technically feasible once familial variants are known (standard practice, not disease-specific literature). Dietary restriction is at best tertiary prevention, unproven here.

## 14. Other Species / Natural Disease

No naturally occurring SCPx deficiency has been reported in any non-human species (nothing in OMIA). Orthologs are conserved across vertebrates (mouse *Scp2*, MGI-listed). No zoonotic dimension.

## 15. Model Organisms

- **Scp2⁻/⁻ mouse (combined SCP2+SCPx knockout)** — Seedorf et al. 1998, **PMID:9553048**: "the gene disruption led to inefficient import of phytanoyl-CoA into peroxisomes and to defective thiolytic cleavage of 3-ketopristanoyl-CoA," with "up to 10-fold accumulation of… phytanic acid," gene-expression changes, peroxisome proliferation, hypolipidemia, impaired weight control, and neuropathy. **Critical limitations:** it deletes *both* gene products (not the human lesion — human patients retain SCP2 from its own promoter) and accumulates **phytanic** acid where the human disease accumulates **pristanic** acid. Mouse findings should not be imported as human mechanism without naming the model.
- **SCP-x-null mouse (thiolase-selective; the genotype-matched model)** — Atshaves et al. 2007, **PMID:17068117**: "demonstrates, for the first time, a direct physiological relationship between lack of SCP-x and decreased ability to metabolize branched-chain lipids," and showed SCPx ablation does not reduce SCP2 expression. Characterized under phytol-diet challenge; phenotypes were hepatic/nutritional — **no brain phenotype has ever been reported for this model**, which is the outstanding experiment (brain imaging/pathology ± phytol load in SCPx-null mice).
- **Cardiac phenotype:** phytol-fed Scp2⁻/⁻ mice show "bradycardia and impaired AV nodal and intraventricular impulse conduction… sudden cardiac death" (**PMID:15574183**) — no counterpart in any confirmed patient (only the disputed heterozygous case had dysrhythmia).
- **Cellular model:** patient-derived skin fibroblasts (diagnostic and functional workhorse). No iPSC, organoid, zebrafish, or invertebrate disease model published.

---

## Key open questions (for KB knowledge-gap records)

1. **Mechanism of the CNS lesion** — no route from the β-oxidation block to the symmetrical thalamic/brainstem lesions has been demonstrated; patient 3's near-normal pristanic acid with identical imaging argues against simple metabolite toxicity.
2. **Validity of the mouse model** — the standard knockout deletes both products and accumulates the wrong metabolite; the genotype-matched SCPx-null mouse has no reported brain phenotype.
3. **True phenotypic spectrum** — three patients share almost nothing beyond MRI pattern, stutter, and tremor; ClinGen's rename to "SCP2 deficiency" anticipates expansion.
4. **The heterozygous fourth case** — dominant-negative/haploinsufficiency remains unexcluded but unaccepted.

## Primary citations

- Ferdinandusse S, et al. *Am J Hum Genet* 2006 — founding case. **PMID:16685654**
- Horvath R, et al. *Neurology* 2015 — patient 2, NBIA phenotype. **PMID:26497993**
- Kono S, et al. 2017 — retinal phenotype in patient 2. **PMID:28033445**
- Alshehri A, et al. *Hum Genomics* 2022 — disputed heterozygous case. **PMID:35996156**
- Wang Y, et al. *Front Neurol* 2023 — patient 3, episodic psychosis; three-patient comparison. **PMID:37905191**
- Cheillan D, et al. ClinGen peroxisomal gene curation. 2023. **PMID:37236006**
- Ferdinandusse S, Wanders RJA. Disorders of fatty acid homeostasis (review). 2024. **PMID:38693715**
- ACMG technical standard, peroxisomal laboratory diagnosis. **PMID:31822849**
- Mouse models: **PMID:9553048**, **PMID:17068117**, **PMID:15574183**

Sources: [OMIM 613724](https://omim.org/entry/613724) · [OMIM *184755](https://omim.org/entry/184755) · [ClinVar RCV000013658](https://www.ncbi.nlm.nih.gov/clinvar/RCV000013658/) · [Ferdinandusse 2006 (AJHG)](https://www.cell.com/ajhg/fulltext/S0002-9297(07)63925-1) · [Wang 2023 case report (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10613489/) · [Alshehri 2022 (Human Genomics)](https://humgenomics.biomedcentral.com/articles/10.1186/s40246-022-00408-w) · [Seedorf 1998 (Genes Dev)](https://genesdev.cshlp.org/content/12/8/1189.full) · [Genomics England PanelApp — SCP2](https://panelapp.genomicsengland.co.uk/panels/42/gene/SCP2/)

*Method note: this report was grounded in the repository's snippet-verified curation of MONDO:0013391 (all quoted sentences above were validated as exact substrings of the cached source abstracts) and cross-checked against current OMIM, ClinVar, PanelApp, and 2023–2025 literature searches, which found no additional confirmed patients beyond the three described.*

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 11 |
| Quoted claims found in source | 10 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 14 |
| On topic | 10 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:15574183` *(abstract only)*: "bradycardia and impaired AV nodal and intraventricular impulse conduction… sudden cardiac death"
  - closest text in source: "CONCLUSION: Accumulation of phytanic acid in myocardial phospholipid membranes is associated with bradycardia and impaired AV nodal and intraventricular impulse conduction, which could provide an explanation for sudden cardiac death in this model."

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 36 |
| Resolved | 34 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 13 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0013391` (3 mentions) - the report calls it "sterol carrier protein 2 deficiency", "all quoted sentences above were validated as exact substrings of the cached source abstracts"; MONDO calls it **sterol carrier protein 2 deficiency**
- `HP:0000709` (1 mention) - the report calls it "infection-triggered episodic psychosis"; HP calls it **Psychosis**
- `HP:0034721` (1 mention) - the report calls it "marked in patients 1–2, only mild in patient 3"; HP calls it **Elevated circulating pristanic acid concentration**
- `HP:6001007` (1 mention) - the report calls it "patient 1"; HP calls it **Elevated urinary bile alcohol level**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002346` (1 mention) - the report calls it "Head tremor, dystonic in patient 1"; HP calls it **Head tremor**
- `HP:0012675` (1 mention) - the report calls it "neurodegeneration with brain iron accumulation"; HP calls it **Iron accumulation in brain**
- `GO:0005777` (3 mentions) - the report calls it "Subcellular:** peroxisome"; GO calls it **peroxisome**
- `UBERON:0001897` (1 mention) - the report calls it "Primary:** central nervous system — thalamus"; UBERON calls it **dorsal plus ventral thalamus**
- `NCIT:C15986` (1 mention) - the report calls it "Symptomatic pharmacotherapy"; NCIT calls it **Pharmacotherapy**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0013391` - called "sterol carrier protein 2 deficiency", "all quoted sentences above were validated as exact substrings of the cached source abstracts"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.
