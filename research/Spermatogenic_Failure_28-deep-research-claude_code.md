---
provider: claude_code
model: claude-opus-5-5
cached: false
start_time: '2026-10-15T15:31:49.904191'
end_time: '2026-10-15T15:35:23.026995'
duration_seconds: 213.12
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Spermatogenic Failure 28
  mondo_id: MONDO:0054732
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
  - claude-opus-5-5
  num_turns: 20
  total_cost_usd: 2.2906022000000004
  session_id: 3667bf2e-bba4-4f0a-abb0-026f6d0bf32a
  stop_reason: end_turn
  permission_denials: 5
  denied_tools:
  - Bash
  - mcp__pubmed__search_articles
  assistant_text_blocks: 4
reference_validation:
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 12
  quotes_valid: 10
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:30075111
  - PMID:29895858
  relevance_assessed: 7
  on_topic: 7
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 33
  verified: 32
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 4
  labels_matching: 0
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: GO:0043240
    reported_labels:
    - already used in the FA entry
    ontology_label: Fanconi anaemia nuclear complex
  - term_id: CL:0000020
    reported_labels:
    - confirm which label applies
    ontology_label: spermatogonium
  - term_id: UBERON:0000473
    reported_labels:
    - unverified
    ontology_label: testis
  - term_id: HP:0000007
    reported_labels:
    - unverified
    ontology_label: Autosomal recessive inheritance
  obsolete_terms:
  - term_id: HP:0100843
    ontology_label: obsolete Glioblastoma
    replaced_by: HP:0012174
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spermatogenic Failure 28
- **MONDO ID:** MONDO:0054732 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spermatogenic Failure 28** covering all of the
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

Still gathering sources: PubMed and network access are blocked, so I'm working from the repository's local reference cache. I'm now listing which cached papers cover FANCM.

Key cached sources: 30075111, 29895858, 34976027, 38927643, 28837162. Reading them, plus checking ORPHA/related KB entries.

I've read the five core FANCM papers from the local cache. Now I'm pulling FANCM context from the secondary sources: cancer risk, meiosis, and Fanconi anemia reviews.

# Spermatogenic Failure 28 (SPGF28; FANCM-related male infertility): Research Report

**Target:** Spermatogenic failure 28, MONDO:0054732 · **Category:** Mendelian (autosomal recessive) · **Report date:** 2026-10-15

> **How this report was sourced.** In this session PubMed (MCP) and outbound network calls (E-utilities, curl) were blocked. All quotes marked **[cached ✔]** were read word for word from the repository's `references_cache/` and can be used as snippets as they stand. Identifiers or citations marked **[unverified]** come from background knowledge and were **not** checked this session. Before binding or citing them in `kb/`, look each one up (`just fetch-reference PMID:…`, OLS or runoak). This follows CLAUDE.md's rule that every CURIE must be read from a source in the same step it is written.

---

## 1. Disease Information

**Overview.** SPGF28 is an autosomal recessive form of male infertility caused by biallelic loss-of-function (LoF) variants in **FANCM** (FA complementation group M, a DNA translocase). Affected men have non-obstructive azoospermia (NOA). On testicular biopsy this is most often Sertoli cell-only syndrome (SCOS). Some men have severe oligoasthenozoospermia instead. Endocrine function is otherwise largely preserved, and there is no bone-marrow failure.

The defining paper:

> "The study convincingly demonstrates that bi-allelic recessive LoF variants in FANCM cause azoospermia." — Kasak et al. 2018, *Am J Hum Genet*, **PMID:30075111** [cached ✔]

> "These findings revealed male infertility to be a novel phenotype of human patients with a biallelic FANCM PV." — Yin et al. 2019, *Genet Med*, **PMID:29895858** [cached ✔]

**Identifiers**

| Resource | ID | Status |
|---|---|---|
| MONDO | MONDO:0054732 "spermatogenic failure 28" | in draft entry; confirm with `just validate-terms` |
| OMIM (phenotype) | 618086 | [unverified] |
| OMIM (gene) FANCM | 609644 | [cached ✔] (PMID:34976027 cites "FANCM (MIM: 609644)") |
| HGNC | hgnc:23168 FANCM | already bound in `kb/disorders/Fanconi_Anemia.yaml` |
| Orphanet | no SPGF28-specific entry known; falls under NOA due to genetic causes / SCOS | [unverified] |
| ICD-10 / ICD-11 | N46.0 azoospermia (generic) / GB04.0 | [unverified] |
| MeSH | Azoospermia (D053713); Sertoli Cell-Only Syndrome (D050291) | [unverified] |

**Synonyms:** SPGF28; FANCM-related non-obstructive azoospermia; FANCM-associated Sertoli cell-only syndrome.

**Related allelic conditions** (same gene, different MONDO concepts; keep them separate):
- **Premature ovarian failure 15** (POF15; OMIM 618096 [unverified]): FANCM biallelic LoF in women.
- **FANCM-biallelic "FA-like" cancer and chemotherapy-toxicity phenotype:** early-onset cancer and chemotherapy sensitivity without bone-marrow failure (PMID:28837162 [cached ✔]).
- Monoallelic FANCM truncating variants as moderate breast-cancer risk alleles.

**Data provenance.** Everything here is case-level: family and sporadic exome studies reported in the literature. There are no registries or EHR cohorts.

---

## 2. Etiology

**Primary cause:** biallelic germline LoF variants in FANCM (chromosome 14q21.2 [unverified locus]).

**Genetic risk factors**
- Truncating variants: frameshift, nonsense and splice (see §4).
- Possibly biallelic missense variants in the helicase/DEAH domain. This is lower confidence and rests on in-silico prediction only (PMID:34976027, PMID:38927643).

**Environmental risk factors.** None are established. Zhang et al. speculate that DNA interstrand-crosslink (ICL) burden from environmental agents might modify severity:

> "the ICL repair pathway is indispensable in the DNA replication of germ cells, and can be affected by a variety of environmental agents, which have also been proposed as explanations for the clinical variability in male patients suffering from infertility." — PMID:34976027 [cached ✔]

This is hypothesis-level only.

**Protective factors:** none known.

**Gene–environment interaction:** not studied in humans. A plausible but untested axis is ICL-inducing exposures (alkylating chemotherapy, aldehydes) in FANCM-deficient germ cells. Affected individuals do show cellular hypersensitivity to mitomycin C (MMC) (PMID:29895858).

---

## 3. Phenotypes

| Phenotype | Suggested HPO [verify each] | Type / onset | Frequency (n ≈ 11 reported men) | Key evidence |
|---|---|---|---|---|
| Non-obstructive azoospermia | HP:0011961 Non-obstructive azoospermia | Sign; post-pubertal / adult presentation | Most cases (~9/11) | PMID:30075111, 34976027, 38927643 |
| Sertoli cell-only syndrome (testis histology) | HP:0011962 Sertoli cell-only syndrome [unverified] | Biopsy finding | All biopsied cases (Estonian proband, 3 Chinese, 1 Croatian) | PMID:30075111, 34976027, 38927643 |
| Oligoasthenozoospermia / severe oligozoospermia | HP:0000798 Oligospermia; HP:0012207 Reduced sperm motility [unverified] | Sign | 2/3 Pakistani brothers | PMID:29895858 |
| Male infertility | HP:0003251 Male infertility | Adult | 100% | all |
| Elevated FSH | HP:0008232 Elevated circulating follicle stimulating hormone concentration [unverified] | Lab | Common but not universal (3/3 Chinese; borderline to elevated in the Pakistani family; normal in the Croatian case) | PMID:34976027, 29895858, 38927643 |
| Reduced testicular volume | HP:0008734 Decreased testicular size [unverified] | Sign | Variable (8–10 mL in 2 brothers; 12 mL in another) | PMID:34976027 |
| Low/low-normal testosterone | HP:0040171 Decreased serum testosterone concentration [unverified] | Lab | Occasional (1 Croatian case below range) | PMID:38927643 |
| Chromosomal breakage after MMC (lymphocytes) | HP:0003221 Chromosomal breakage induced by crosslinking agents [unverified] | Lab / cellular | In tested patients (2/2) | PMID:29895858 |
| Cancer (variable; incomplete evidence) | e.g., HP:0100843 Glioblastoma not appropriate; diffuse astrocytoma → MONDO-level comorbidity | Adult | 1 reported man (compound heterozygous missense) | PMID:38927643 (case report; causality not shown) |

**Supporting quotes [cached ✔]**
- "Adult FancmΔC/ΔC mice showed spermatogenic failure, with germ cell loss in 50.2% of testicular tubules and round-spermatid maturation arrest in 43.5% of tubules." (PMID:29895858; mouse)
- "H&E staining and immunohistochemistry showed Sertoli cell-only Syndrome (SCOS) in the three patients with NOA." (PMID:34976027)
- "Two of the affected brothers, IV:1 (married for 21 years) and IV:3 (single) were diagnosed with mild and severe oligoasthenospermia, respectively. Both had largely normal plasma levels of testosterone and pituitary hormones." (PMID:29895858)
- "The loss-of-function FANCM PV increased ICL sensitivity in lymphocytes of patients and FancmΔC/ΔC spermatogonia." (PMID:29895858)

**Absent features:**
> "neither bone marrow failure nor cancer/tumor was detected in all the patients or adult FancmΔC/ΔC mice." (PMID:29895858) [cached ✔]

Karyotype was 46,XY with no AZF microdeletions in every reported case.

**Severity and course.** Infertility is the presenting problem and appears stable once established. The mouse data suggest progressive spermatogonial stem cell (SSC) loss (see §6). That fits a spectrum from oligozoospermia to SCOS that may be age-dependent, but this has not been shown in humans.

**Quality of life.** No disease-specific data exist. The burden is infertility-related psychosocial distress, plus the possible downstream cancer-surveillance burden.

---

## 4. Genetic / Molecular Information

**Causal gene:** FANCM (hgnc:23168; MIM 609644). This is a DEAH-box DNA translocase of the FA core complex, with the domains PIP-box, DEAH (aa 77–590), MHF-binding (661–800), MM1 (826–967), MM2 (1218–1251) and ERCC4 (1818–1956). Domain boundaries are as listed in PMID:34976027 [cached ✔].

**Reported variants in SPGF28 (RefSeq NM_020937)**

| Variant | Protein | Zygosity | Population | Phenotype | Source |
|---|---|---|---|---|---|
| c.1491dupA | p.Gln498Thrfs\*7 (rs761250416) | compound het (maternal) | Estonian brothers | NOA/SCOS | PMID:30075111 |
| c.4387-10A>G | splice → premature stop (p.Arg1436_Ser1437insLeuLeu\*) | compound het (paternal) | same family | NOA/SCOS | PMID:30075111 |
| c.5101C>T | p.Gln1701\* (rs147021911) | homozygous | Estonian | NOA | PMID:30075111 |
| c.5791C>T | p.Arg1931\* (rs144567652) | homozygous | Portuguese | NOA | PMID:30075111 |
| c.1946_1958del | p.Pro648Leufs\*16 | homozygous | Pakistani (consanguineous), 3 brothers | 1 azoospermia, 2 oligoasthenozoospermia | PMID:29895858 |
| c.1778delG + c.1663G>T | p.Arg593Glnfs\*76 + p.Val555Phe | compound het | Chinese brothers | NOA/SCOS | PMID:34976027 |
| c.1972C>T | p.Arg658\* | homozygous | Chinese (sporadic, 1/479 NOA) | NOA/SCOS | PMID:34976027 |
| c.170C>T? / c.950A>G? (p.Leu57Phe rs142007602 + p.Gln317Arg rs375644492) | missense | compound het | Croatian | SCOS (+ diffuse astrocytoma) | PMID:38927643 (both VUS/conflicting in ClinVar) |

The cDNA notation for the Croatian missense variants is not given in the cached text. Only the protein changes and rsIDs are reliable.

**Classification.** Truncating alleles behave as LoF and are pathogenic or likely pathogenic for SPGF28 in ClinVar [unverified ClinVar status]. The missense alleles are VUS. Per PMID:38927643, rs142007602 is "probably benign regarding Fanconi anemia, but in relation to spermatogenic failure… of uncertain significance".

**Allele frequency.** The Arg658\* and Gln1701\* alleles also recur in breast-cancer cohorts (e.g., p.Arg658\* has a carrier frequency of about 0.1–0.5% in Finnish and European populations [unverified]). p.Leu57Phe has MAF 0.0017 and p.Gln317Arg has MAF 0.000016 (gnomAD v2.1.1, PMID:38927643 [cached ✔]).

**Origin and mechanism.** All variants are germline, and the functional consequence is LoF. Yin et al. showed no detectable full-length protein in blood, impaired FANCD2 monoubiquitination and foci in FANCM⁻/⁻ HEK293T cells re-expressing the mutant, and increased γH2AX (PMID:29895858, IN_VITRO).

**Modifier genes:** none established. Domain position has been proposed to shape the phenotype:

> "Phenotype severity might correlate with mutation position in the gene." (PMID:28837162) [cached ✔]

**Epigenetic / chromosomal:** none. A normal karyotype is required to make the diagnosis.

**ClinGen gene–disease validity:** not checked this session. Run `just list-gene-validity` or `just fetch-reference CGGV:…` before recording any tier. **Do not assign a tier.**

---

## 5. Environmental Information

No environmental, lifestyle or infectious causes are known. The reported patients had no history of smoking, alcohol, cryptorchidism or varicocele (PMID:29895858, PMID:34976027). This is relevant if the entry later records an exposure; otherwise leave `environmental:` empty.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic FANCM LoF variants** (truncating, or rarely missense in the DEAH/helicase domain) lead to **absent or truncated FANCM protein**. This is demonstrated in blood by western blot (PMID:29895858). Testis IHC shows absent or faint staining in Sertoli cells (PMID:30075111, PMID:38927643).
2. Loss of FANCM produces **loss of stalled-replication-fork recognition and of FA core complex recruitment**. As a result, **FANCD2–FANCI monoubiquitination fails** and **ICL repair is defective**. This is demonstrated in vitro in PMID:29895858.
   - "FANCM is the only protein within the FA core complex that can recognize and bind to stalled replication forks." (PMID:29895858) [cached ✔]
3. Defective ICL repair and replication-fork protection cause **genomic instability and DNA damage accumulation in proliferating germ cells**. Measured readouts are MMC hypersensitivity in patient lymphocytes and in mouse spermatogonia, and increased γH2AX.
4. **Branch A: mitotic germline compartment (dominant branch in humans).** DNA damage in primordial germ cells (PGCs) and SSCs leads to **apoptosis and reduced proliferation**, which causes **progressive SSC depletion**.
   - Mouse: GFRA1⁺/SOX9⁺ ratio halved at 10 weeks and below one quarter at 70 weeks (PMID:29895858).
   - Earlier Fancm mice: reduced PGC proliferation (Bakker et al. 2009 [unverified PMID]).
   - The chain then runs: germ-cell loss → **Sertoli cell-only tubules** → **non-obstructive azoospermia**.
   - The human SCOS endpoint is demonstrated. That the human SCOS arises through *progressive* loss is inferred from mice.
5. **Branch B: meiotic and post-meiotic compartment (model-derived).** FANCM is an anti-crossover helicase with the MHF and BTR (BLM–TOP3A–RMI) complexes, so its loss **dysregulates meiotic recombination/crossover control**. This was established first in *Arabidopsis* (Crismani et al. 2012, *Science* [unverified PMID]), and loss in mice affects crossover number (cited in PMID:38927643). In the mouse model the result is **partial round-spermatid maturation arrest** (43.5% of tubules), which leads to **oligoasthenozoospermia** with abnormal morphology. This may explain the milder oligozoospermic presentations in the Pakistani family. It is inferred; human testis histology was not available for that family.
6. **Systemic consequence (variable; not part of SPGF28 core):** somatic genomic instability may confer cancer predisposition and chemotherapy or radiotherapy toxicity. This is shown in biallelic FANCM women (PMID:28837162) and suggested in one SCOS man with astrocytoma (PMID:38927643, case-level only).

The germ-cell-specific emphasis is supported by expression data:

> "FANCM exhibits enhanced testicular expression… localized FANCM to the Sertoli and spermatogenic cells of seminiferous tubules with increasing intensity through germ cell development. This is consistent with its role in maintaining genomic stability in meiosis and mitosis." (PMID:30075111) [cached ✔]

FANCM is functionally distinct from the canonical FA genes:

> "biallelic FANCM mutations do not cause classical FA, providing proof that FANCM is not a canonical FA gene." (PMID:28837162) [cached ✔]

Yin et al. add that the round-spermatid arrest "has not been mentioned in Fancm mutant mice… suggesting that this role of FANCM could be independent of the canonical FA pathway" (PMID:29895858) [cached ✔].

### Suggested ontology terms (all [unverified]; look each one up before binding)

**GO biological processes**
- interstrand cross-link repair GO:0036297
- replication fork processing GO:0031297
- negative regulation of reciprocal meiotic recombination / meiotic crossover regulation (search "crossover")
- spermatogenesis GO:0007283
- male germ-line stem cell population maintenance GO:0036098
- germ cell proliferation GO:0036093
- apoptotic process GO:0006915
- double-strand break repair via homologous recombination GO:0000724

**GO molecular function / complex**
- ATP-dependent DNA/DNA annealing or translocase activity: check "ATP-dependent activity, acting on DNA" GO:0008094
- Fanconi anaemia nuclear complex GO:0043240 (already used in the FA entry)
- FANCM-MHF complex GO:0071821

**CL cell types**
- spermatogonial stem cell CL:0000020 (or "male germline stem cell")
- spermatogonium CL:0000020 — confirm which label applies
- primordial germ cell CL:0000670
- Sertoli cell CL:0000216
- round spermatid CL:0000018 / spermatid
- spermatocyte CL:0000017

**Modifiers:** use `LOSS_OF_FUNCTION` for `functional_impact_category` on the variant node, and `DECREASED` for the process-level `modifier` values.

**Molecular profiling.** No transcriptomic, proteomic or single-cell datasets specific to FANCM-NOA are known. The Pakistani-family exome data are deposited as **ArrayExpress E-MTAB-6090** (PMID:29895858 [cached ✔]). That is an exome dataset, not an expression dataset, and is a candidate for `datasets:` after `just verify-datasets`.

---

## 7. Anatomical Structures Affected

- **Primary organ:** testis (UBERON:0000473 [unverified]), specifically the seminiferous tubule epithelium (UBERON:0001343 seminiferous tubule of testis [unverified]).
- **Secondary:** none established. Some biopsies show tubular fibrosis ("tubular shadows") and mononuclear infiltrates (PMID:38927643).
- **Body system:** male reproductive system.
- **Cells:** germ cells, which are lost; Sertoli cells, which remain; Leydig cells, which appear normal (PMID:38927643).
- **Subcellular:** nucleus, at replication forks and chromatin (GO:0005634 nucleus). IHC in human testis shows predominantly **cytoplasmic** FANCM staining (PMID:38927643 [cached ✔]), with Golgi localization reported in earlier work.
- **Laterality:** bilateral (both testes SCOS in PMID:38927643; bilateral volumes in PMID:34976027).

---

## 8. Temporal Development

- **Onset:** the defect is likely congenital or developmental, since mouse PGC defects arise in the embryo. Clinically it presents in adulthood at infertility evaluation; reported ages range from 23 to 48 years.
- **Course:** stable infertility. The mouse model shows age-dependent progressive SSC loss (PMID:29895858), which suggests a possible window for **early sperm cryopreservation** in genotype-positive oligozoospermic men. This is an extrapolation, not established practice.
- **Remission:** none.

---

## 9. Inheritance and Population

- **Inheritance:** autosomal recessive (HP:0000007 [unverified]).
- **Penetrance:** apparently complete for male infertility in biallelic-LoF men reported so far. Ascertainment bias is strong, since cases were identified through infertility clinics.
- **Expressivity:** variable, ranging from mild oligoasthenozoospermia to SCOS (PMID:29895858 vs PMID:30075111).
- **Consanguinity:** the Pakistani family was first-cousin (PMID:29895858). The other families were non-consanguineous.
- **Founder effects:** p.Gln1701\* and p.Arg658\* recur in Northern European populations. p.Arg658\* is also recurrent in Chinese NOA (1/479 in PMID:34976027). A formal founder analysis has not been done.
- **Prevalence:** unknown. FANCM accounts for a small fraction of idiopathic NOA: about 1 in 479 Chinese NOA cases from one centre (PMID:34976027). Use `measure_type: CASES_IN_LITERATURE`. Roughly 11 men have been reported across 5 publications (2018–2024).
- **Sex:** this MONDO concept is male-only. Biallelic women have POI or early menopause (POF15; PMID:28837162 mentions "early menopause").
- **Geography:** Estonia, Portugal, Pakistan, China and Croatia.

---

## 10. Diagnostics

- **Semen analysis** (WHO criteria): azoospermia confirmed on at least two centrifuged samples, or severe oligoasthenozoospermia.
- **Hormones:** FSH (often raised), LH, testosterone. LOINC codes for FSH and testosterone must come from `just loinc-seed-cache`; do not type them.
- **Exclusions:** karyotype (46,XY), Y-chromosome AZF microdeletion testing, CFTR testing if obstruction is suspected. All were normal in the reported cases.
- **Testicular biopsy / micro-TESE histology:** SCOS. IHC shows absent DDX4 and UCHL1 germ-cell markers with retained SOX9 and AR (PMID:34976027 [cached ✔]).
- **Genetic testing:** exome sequencing or an NOA gene panel including FANCM. Interpret under a recessive model and check for CNV on the second allele. PMID:34976027 ran a WES-based CNV analysis to exclude a hemizygous deletion.
- **Functional cytogenetics:** an MMC or DEB chromosomal-breakage test on lymphocytes shows increased breaks (PMID:29895858). This supports pathogenicity of VUS. Note that it overlaps the FA diagnostic test (PMID:25827349, DEB analysis).
- **Differential diagnosis:** other monogenic NOA (TEX11, TEX14, TEX15, MEIOB, STAG3, SYCE1, DMC1, SHOC1, HFM1, XRCC2; PMID:34976027, 34429122); Klinefelter syndrome; AZF deletions; classical Fanconi anemia, which differs by marrow failure and malformations; and post-chemotherapy azoospermia.
- **Screening:** no population screening. Cascade testing of sisters is relevant because of POI risk, and of relatives because of breast-cancer risk.

---

## 11. Outcome / Prognosis

- **Survival:** not reduced by SPGF28 itself, as far as is known. A death in the Pakistani family from valvular heart disease was attributed by the authors to another cause, since a heterozygous brother was also affected (PMID:29895858).
- **Fertility prognosis:** poor in the SCOS presentations. No sperm retrieval was reported in the Chinese micro-TESE cases (PMID:34976027 reports SCOS histology; sperm-retrieval outcome not stated).
- **Long-term risk:**
  - Possible cancer predisposition, extrapolated from biallelic FANCM women and monoallelic breast-cancer data (PMID:28837162) and from one astrocytoma case (PMID:38927643).
  - Possible hypersensitivity to chemotherapy and radiotherapy, which matters if cancer develops.
  - Zhang et al. recommend that "future cancer incidence of the patients should be monitored" (PMID:34976027) [cached ✔].

---

## 12. Treatment

No disease-modifying therapy exists. Management is reproductive and preventive.

| Intervention | Suggested NCIT [unverified] | Notes |
|---|---|---|
| Micro-TESE + ICSI | Surgical Procedure NCIT:C15329; ICSI (search NCIT "Intracytoplasmic Sperm Injection") | Low yield expected in SCOS; ICSI possible in oligozoospermic men |
| Sperm cryopreservation | search NCIT "Sperm Banking" | Possibly time-sensitive (mouse SSC loss) |
| Donor sperm / adoption | — | Counselling |
| Genetic counselling | NCIT:C15240 Genetic Counseling | Recessive transmission, sister POI risk, cancer-risk discussion |
| Cancer surveillance / dose-adapted chemo-radiotherapy if cancer arises | Supportive Care NCIT:C15747 | Expert opinion: PMID:38927643 recommends "regular screenings for cancer or hematologic abnormalities" and "dose reductions or alternative regimens" [cached ✔] |

**Pharmacogenomics:** FANCM deficiency may predict sensitivity to ICL agents and PARP inhibitors. This is preclinical or theoretical for SPGF28.

**Gene or cell therapy:** none. There are no clinical trials specific to FANCM-related NOA [unverified search].

---

## 13. Prevention

- **Primary:** none.
- **Reproductive and genetic:** carrier testing of partners. PGT-M is relevant if the offspring of an affected man via ICSI could be at risk (offspring are obligate carriers, and are affected only if the partner is a carrier).
- **Cascade testing:** sisters (POF15 risk) and female relatives (breast-cancer risk, monoallelic).
- **Tertiary:** cancer surveillance, and avoiding unnecessary ICL-agent exposure (expert opinion).

---

## 14. Other Species / Natural Disease

- No naturally occurring FANCM infertility in domestic animals is recorded in OMIA [unverified].
- FANCM is conserved from yeast (Mph1) to plants. In *Arabidopsis thaliana*, FANCM loss increases meiotic crossovers (Crismani et al. 2012 [unverified]), which is the basis for the anti-crossover role.
- Mouse ortholog: *Fancm* (MGI ID to look up).

---

## 15. Model Organisms

| Model | Phenotype | Fidelity / limitation | Source |
|---|---|---|---|
| **Fancm^ΔC/ΔC^ mouse** (p.R638Rfs\*8; mimics human p.P648Lfs\*16) | Subfertile males; testes ~47% smaller; epididymal sperm count reduced 97-fold; SCO (7.6%), germ-cell loss (42.6%) and round-spermatid arrest (43.5%) tubules; progressive SSC loss; spermatogonial MMC hypersensitivity; no marrow failure or tumours to 1 year | MODERATE–HIGH; mice are subfertile rather than sterile, so milder than human SCOS | PMID:29895858 [cached ✔] |
| Fancm^Δ2/Δ2^ knockout mouse | Hypogonadism in both sexes; reduced PGC proliferation; tumour predisposition; non-Mendelian transmission in females | Bakker et al. 2009, *Hum Mol Genet* [unverified PMID] |
| Fancm^C4/C4^ (helicase-domain missense) mouse | Progressive germ-cell depletion approaching SCOS; elevated SCE; tumour susceptibility | Luo et al. 2014 [unverified PMID]; summarized in PMID:38927643 |
| FANCM⁻/⁻ HEK293T + mutant re-expression | Impaired FANCD2 monoubiquitination and foci; increased γH2AX and MMC breaks | IN_VITRO, PMID:29895858 |
| *Arabidopsis* fancm | Increased meiotic crossovers | Crismani 2012 [unverified] |

Key quote:

> "Hence, FancmΔC/ΔC mice phenocopied the clinical phenotypes in our patients" (PMID:29895858) [cached ✔]

The model is reported as `MODEL_ORGANISM` evidence and should not be the sole support for any human phenotype.

---

## Curation notes for the dismech entry

1. **Cached and quotable now:** PMID:30075111, 29895858, 34976027, 38927643, 28837162 (plus the background references PMID:34429122 and 25827349). Run `just count-verified-snippets` after drafting.
2. **To fetch before citing:**
   - Bogliolo et al. 2018 (biallelic truncating FANCM → early-onset cancer, not FA)
   - Fouquet et al. 2017 / Yang et al. 2020 (FANCM POI)
   - Bakker et al. 2009 and Luo et al. 2014 (Fancm mice)
   - Crismani et al. 2012
   - Kasak & Laan review(s)
   - GeneReviews: no SPGF28 chapter is expected; check with `just check-genereviews`.
3. **Scope:** keep POF15 and the FA-like cancer phenotype out of this entry's core phenotypes. Mention them in `notes` or as cross-references, because this MONDO concept is the male spermatogenic failure.
4. **Pathograph wiring:** variant LoF → defective ICL repair / replication fork protection → germ-cell genomic instability → SSC/PGC depletion (→ SCOS → NOA), plus a parallel meiotic crossover / round-spermatid arrest branch (→ oligoasthenozoospermia). Connect each phenotype with a `downstream` edge so it is not stranded (see `just list-disconnected-phenotypes`).
5. **Gene validity:** do not assign a ClinGen tier unless a cached `CGGV:` record exists.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 12 |
| Quoted claims found in source | 10 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 7 |
| On topic | 7 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

1 of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:30075111` *(abstract only)*: "FANCM exhibits enhanced testicular expression… localized FANCM to the Sertoli and spermatogenic cells of seminiferous tubules with increasing intensity through germ cell development. This is consistent with its role in maintaining genomic stability in meiosis and mitosis."
  - closest text in source: "In control subjects, immunohistochemical staining localized FANCM to the Sertoli and spermatogenic cells of seminiferous tubules with increasing intensity through germ cell development"
- `PMID:29895858`: "has not been mentioned in Fancm mutant mice… suggesting that this role of FANCM could be independent of the canonical FA pathway"
  - closest text in source: "Notably, 43.5% of seminiferous tubules displayed maturation arrest at round spermatid stage in FancmΔC/ΔC mice, which has not been mentioned in Fancm mutant mice18,19 or reported in any other FA mouse models,19–22 suggesting that this role of FANCM could be independent of the canonical FA pathway"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 33 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 4 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 4 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `GO:0043240` (1 mention) - the report calls it "already used in the FA entry"; GO calls it **Fanconi anaemia nuclear complex**
- `CL:0000020` (2 mentions) - the report calls it "confirm which label applies"; CL calls it **spermatogonium**
- `UBERON:0000473` (1 mention) - the report calls it "unverified"; UBERON calls it **testis**
- `HP:0000007` (1 mention) - the report calls it "unverified"; HP calls it **Autosomal recessive inheritance**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0100843` (obsolete Glioblastoma) (1 mention) - replaced by `HP:0012174`