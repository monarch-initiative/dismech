---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-23T01:55:40.337681'
end_time: '2026-10-23T01:59:20.125991'
duration_seconds: 219.79
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Intellectual Developmental Disorder With Autism And Dysmorphic Facies
  mondo_id: MONDO:0859281
  category: Mendelian
  causal_genes: PDZD8
  omim_id: not recorded
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
  web_search_requests: 2
  num_turns: 19
  total_cost_usd: 2.4199349
  session_id: 54f4a4e4-e5da-468d-ab2e-93a2587bc019
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  - mcp__pubmed__search_articles
  assistant_text_blocks: 4
citation_count: 18
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 4
  quotes_valid: 3
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMC:PMC7486383
  relevance_assessed: 9
  on_topic: 8
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 78
  verified: 78
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 7
  labels_matching: 2
  labels_variant: 5
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Intellectual Developmental Disorder With Autism And Dysmorphic Facies
- **MONDO ID:** MONDO:0859281 (if available)
- **Causal gene(s):** PDZD8
- **OMIM:** not recorded
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Intellectual Developmental Disorder With Autism And Dysmorphic Facies** covering all of the
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

I'm reading the two key PDZD8 papers from the repository's cache. Next I'll pull the family C clinical details, then write the report.

PubMed search access was denied. I'm checking the stub file, then running a web search for newer PDZD8 papers.

I have the clinical and model-organism data. Now I'm checking the suggested ontology terms against the repository's term caches so the report doesn't list identifiers from memory.

# PDZD8-related intellectual developmental disorder with autism and dysmorphic facies (IDDADF): research report

**Target:** MONDO:0859281 · causal gene **PDZD8** (hgnc:26974) · OMIM #620021
**Prepared:** 2026-10-23

---

## How this report was built

- **Primary sources.** Almost all of the content comes from the only two clinical papers on this disease. Both are already in this worktree's `references_cache/` as full text:
  - **PMID:35227461**, Al-Amri et al., *Biol Psychiatry* 2022. Families A and B, plus fly and mouse models.
  - **PMID:40016860**, Pantiru et al., *Mol Autism* 2025. Family C, a six-patient summary table, and further mouse work.
- **No search for newer patients.** Permission to use the PubMed search tool was denied, so I could not search PubMed for patient reports after 2025. A web search ([PMC11866840](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11866840/), [Springer](https://link.springer.com/article/10.1186/s13229-025-00650-8), [MedGen C5774206 mirror](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/commit/bd92c530490f55ed2fd68cfd16ea8c327904c65c/www.ncbi.nlm.nih.gov/medgen/C5774206/index.html)) found nothing beyond these three families. The count of six patients is the count as of the 2025 paper.
- **Ontology terms.** Every HP, GO, CL, UBERON, NCIT and CHEBI identifier below was read from the repository's `cache/<prefix>/terms.csv` files. Where a term could not be found that way, I say so.
- **Unverified PMIDs.** The basic cell-biology papers on PDZD8 are cited by the clinical papers, but I could not confirm their PMIDs. They are listed in §6 as leads to fetch.

> ⚠️ **Easy disease to confuse.** `cache/mondo/terms.csv` holds **MONDO:0014017, "intellectual developmental disorder with autism and macrocephaly"**. That is a different disease. Do not bind it to this entry. **MONDO:0859281 has no row in the MONDO cache yet**, so `just validate-terms` will need to resolve it.

---

## 1. Disease information

**Overview.** IDDADF is an ultra-rare autosomal recessive form of intellectual disability that comes with other features (a "syndromic" ID). It is caused by **homozygous premature termination codons (PTCs) in *PDZD8***. PDZD8 is a protein embedded in the endoplasmic reticulum (ER) membrane that transfers lipids between membranes and helps hold organelles together at contact sites.

> "Intellectual developmental disorder with autism and dysmorphic facies (IDDADF; OMIM #620021) is a very rare syndromic ID caused by homozygous premature termination codons (PTCs) in PDZD8, encoding PDZ domain-containing protein 8 (PDZD8)" — PMID:40016860

**Identifiers**

| Resource | ID |
|---|---|
| MONDO | MONDO:0859281 (parent in stub: MONDO:0003847 hereditary disease) |
| OMIM | #620021 |
| MedGen | C5774206 |
| Gene | PDZD8 (formerly PDZK8), hgnc:26974, 10q25.3–q26.11, 5 exons, 1,154 aa; UniProt Q8NEN9 |
| Orphanet / ICD-10 / ICD-11 / MeSH | No disease-specific code found. It would fall under the general intellectual disability codes. |

**Synonyms.** IDDADF; PDZD8-related syndromic intellectual disability.

**Source of the data.** All data are case-level: three consanguineous families, six affected people. There is no registry and no EHR-derived data.

## 2. Etiology

- **Cause.** Biallelic (homozygous) loss-of-function PTC variants in *PDZD8*. In every family the variant was found by homozygosity mapping plus exome sequencing, and it segregated with the disease.
- **Genetic risk factors.**
  - **Parental consanguinity:** 6/6 cases, all children of first-cousin parents.
  - **Ancestry:** Omani, Emirati and Afghan.
- **Possible second variant in family A.** Family A is also homozygous for *ANKRD2* c.982C>T p.(R328W). The authors think this variant is unlikely to cause the ID, but it "may contribute to myopathy in family A" (PMID:35227461). This matters when scoring the muscle phenotype.
- **Modifier, protective, environmental and gene-environment factors.** None reported.

## 3. Phenotypes

Frequencies are taken from the six-patient table in PMID:40016860 (Table 1, column "Incidence in all IDDADF cases"), with the family A/B details from PMID:35227461 Table 1.

> "permitted identification of a core clinical phenotype consisting of developmental delay, ID, autism, and facial dysmorphism" — PMID:40016860

| Phenotype | Frequency | Notes | HPO (cache-verified) |
|---|---|---|---|
| Developmental delay | 6/6 | Congenital or early-childhood onset | HP:0001263 Global developmental delay |
| Intellectual disability | 6/6 (severe 4/6, moderate 2/6) | Stanford-Binet IQ testing in family C | HP:0001249 not in cache. Severity-specific terms were not checked; look them up |
| Autism / autistic behavior | 6/6 (formal ASD diagnosis 5/6) | Diagnosed by DSM-5, CARS2 or ADOS-2 in family C. Family C has *severe* ASD | HP:0000717 Autism; HP:0000729 Autistic behavior |
| Facial dysmorphism | 6/6 | See facial features below | HP:0001999 Abnormal facial shape (coarse, so it needs a `coarse_binding_basis` if used) |
| Hypertelorism (widely spaced eyes) | 4/6 | Families A and B | HP:0000316 Hypertelorism |
| Malar flattening (flat cheekbones) | Family A (3) and family C (2) | | HP:0000272 Malar flattening |
| Open mouth | Family A and family C | | HP:0000194 Open mouth |
| High-arched palate | Family A | | HP:0000218 High palate |
| Myopathic / hypotonic face | Families A and C | | HP:0002058 Myopathic facies; HP:0000338 Hypomimic face |
| Narrow ("thin") palpebral fissures | Family C (2) | | HP:0045025 Narrow palpebral fissure |
| Myopathy / myasthenia (mild weakness) | 5/6 (mild 3/6) | Family C has a limited walking distance. Family A may be confounded by the *ANKRD2* variant | HP:0003198 Myopathy; HP:0001324 Muscle weakness |
| Epilepsy | 3/6 | Generalized epilepsy in C.IV.1, treated with valproate and levetiracetam. One family A patient is "controlled" | HP:0001250 Seizure; HP:0002197 Generalized-onset seizure |
| Absent or delayed speech | Family C: no functional language (2). Family B: delayed speech | | HP:0001344 Absent speech; HP:0000750 Delayed speech and language development |
| Echolalia, hand flapping, poor eye contact | Family B (1) | | HP:0010529 Echolalia (no cache rows for the other two) |
| ADHD | 2/6 | | HP:0007018 Attention deficit hyperactivity disorder |
| OCD | 1/6 | | Not in cache |
| Insomnia | 1/6 | | HP:0100785 Insomnia |
| Aggression | 1/6 | | HP:0000718 Aggressive behavior |
| Short stature | 2/6 | Family C only, more than 3 SD below the mean and proportionate | HP:0004322 Short stature; HP:0003510 Severe short stature |
| Marfanoid habitus | 2/6 | | Not in cache |
| Scoliosis | 2/6 | | HP:0002650 Scoliosis |
| Myopia | 2/6 | | HP:0000545 Myopia |
| Amblyopia, astigmatism | 1/6 each | | HP:0000646 Amblyopia; HP:0000483 Astigmatism |
| Ptosis (bilateral) | 1/6 | | HP:0000508 Ptosis |
| Low-set ears with simple helix | 1/6 | | HP:0000369 Low-set ears; HP:0020206 Simple ear |
| Cleft palate | 1/6 | | HP:0000175 Cleft palate |
| Congenital heart defect | 1/6 | Type not specified | HP:0001627 Abnormal heart morphology |
| Overlapping toes | 1/6 | | HP:0001845 Overlapping toe |
| Hypoplasia of the splenium of the corpus callosum | 1/6 | Patient A.IV.5. B.IV.2's scan was normal | HP:0002079 Hypoplasia of the corpus callosum |
| Demyelinating cortico-subcortical lesions; gliotic lesions | 2/6 | Family C | HP:0002500 Abnormal cerebral white matter morphology; HP:0002171 Gliosis |
| Mild cerebellar hemispheric atrophy | 1/6 | | HP:0001272 Cerebellar atrophy |

**Mode of inheritance:** HP:0000007 Autosomal recessive inheritance.

**Carriers in family A.** Both parents had mild myopathy and reduced facial expression. The father and one unaffected brother had mild autistic features. The authors still conclude that "PDZD8 haploinsufficiency is unlikely to have a major impact" (PMID:35227461). In family C, all heterozygous relatives are asymptomatic.

**Quality of life.** No formal measures (EQ-5D, SF-36) have been reported. Severe ID, lack of functional language and severe ASD imply lifelong dependence.

## 4. Genetic and molecular information

All variants are on transcript NM_173791.5.

| Family | Ancestry | Variant | Exon | gnomAD | CADD | Source |
|---|---|---|---|---|---|---|
| A (3 affected) | Omani | c.2197_2200del p.(S733*) (4-bp deletion causing a frameshift and PTC) | 5 (last exon) | absent | 35 | PMID:35227461 |
| B (1 affected) | Emirati | c.894C>G p.(Y298*) | 2 | absent | 37 | PMID:35227461 |
| C (2 affected) | Afghan | c.88C>T p.(Q30*), chr10-117375140-G-A (GRCh38) | 1 | 6.29×10⁻⁷, no homozygotes (v4.1.0) | 35.0 | PMID:40016860 |

**Origin and zygosity.** All three variants are germline and homozygous.

**Functional consequence.** Loss of function is predicted for all three:
- p.(Q30*) and p.(Y298*) are expected to trigger nonsense-mediated mRNA decay (NMD).
- p.(S733*) sits in the last exon, so it may escape NMD. Even then, the resulting protein would lack the C1 and coiled-coil domains that bind Rab7 and the endosomal lipids PS and PI4P.

> "If the p.(Q30*) mRNA transcript evades nonsense-mediated decay, it may be translated into a truncated, non-functional PDZD8 protein lacking 1,125 C-terminal amino acids (97.5%)" — PMID:40016860

**Gene constraint.**

> "gnomAD control datasets list five other predicted loss-of-function variants in PDZD8, none homozygous, and constraint metrics indicate that PDZD8 is extremely intolerant to loss-of-function variation" — PMID:35227461

**Variant classification.** I did not check ClinVar or ClinGen, and no ClinGen gene-disease validity record is known. Leave `gene_disease_validity` absent.

**Protein domains** (PMID:35227461):
- ER transmembrane domain (aa 2–24)
- SMP lipid-binding domain (91–294)
- PDZ domain (366–449)
- Proline-rich region (551–626)
- C1 domain (840–891)
- Coiled-coil domain (1028–1063)

**Chromosomal abnormalities.** PDZD8 lies within the region sometimes lost in distal 10q deletion syndrome. The healthy heterozygous carriers argue against haploinsufficiency explaining that syndrome (PMID:35227461).

**Epigenetics and modifier genes.** None reported. *ANKRD2* is a possible contributor to the muscle phenotype in family A only.

## 5. Environmental information

Not applicable. No environmental, lifestyle or infectious factors are known.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Biallelic PTC in *PDZD8*.** This leads to **loss of full-length PDZD8**, through NMD or truncation.
   - *Demonstrated in mouse:* full-length protein is absent in Pdzd8^tm1b^ brain (PMID:35227461).
   - *Inferred in humans:* PDZD8 protein cannot be detected in blood.
2. **Loss of PDZD8 at ER contact sites.** This impairs two things:
   - (a) **Lipid transfer from the ER to late endosomes and lysosomes**, and therefore endosome maturation (branch A).
   - (b) **ER–mitochondria tethering**, and therefore **mitochondrial Ca²⁺ uptake** after synaptically triggered Ca²⁺ release from the ER (branch B).
   - Both roles come from cell-biology work cited in the clinical papers. Their role in the human disease is inferred.
3. **Branch A.** Defective endosomal homeostasis leads to **abnormal vacuoles and impaired neuronal integrity**.
   - Shown in cultured neurons; not studied in patients.
4. **Branch B.** Mitochondria take up less Ca²⁺, which leads to **higher cytosolic Ca²⁺ in dendrites** and likely impairs synaptic Ca²⁺ buffering and ATP supply.
   - The ATP effect is the authors' hypothesis (PMID:35227461, Discussion).
5. **Synaptic dysfunction.** In mouse hippocampus there is **reduced saturated LTP** (long-term potentiation, the strengthening of synapses with use) after 3× theta-burst stimulation, **lower paired-pulse facilitation**, and **increased dendritic spine density**.
   - These lead to **long-term memory deficits** in mouse (Barnes maze) and fly (48-hour courtship memory).
   - Source: model organisms, PMID:35227461 and PMID:40016860.
6. **Altered brain development.** In mouse, total brain volume is smaller; relative corpus callosum volume is lower and relative hippocampal volume higher; the accessory olfactory bulb and primary olfactory cortex are larger; the cerebellar nuclei are smaller; and **adult neurogenesis is reduced**.
   - The mouse corpus callosum change mirrors the splenium hypoplasia in patient A.IV.5.
7. **Clinical outcome.** Steps 5 and 6 lead to **ID, autism/ASD, and impaired social recognition**. The mouse shows social-recognition and social-odor-discrimination deficits and repetitive hindlimb jumping (a stereotypy).
   - The authors frame the disorder as a synaptopathy (a disease of synapse function).
   - The step from the mouse to patients is **inferred**.
8. **Parallel systemic branch.** Loss of PDZD8 affects cell metabolism. The paper notes that AMPK phosphorylates PDZD8 at T527, which is needed for glutaminolysis during low glucose. In mice this leads to **higher metabolic rate, low body weight, lower plasma triglyceride in males, and smaller body size**.
   - This may relate to the short stature in family C, but the link is inferred.
9. **Stress and organelle readouts.** Mouse brain shows **more ER-stress and mitochondrial-fusion transcripts** (*Atf4*, *Hspa5*, *Mfn1/2*, *Opa1* were measured).
   - Measured at the mRNA level only, which the authors list as a limitation.
   - The white-matter lesions in family C are unexplained. PDZD8 is expressed in oligodendrocytes, but no mechanism is shown.

> "In neurons, depletion of PDZD8 has been shown to impair endosomal homeostasis (13), decrease the proximity of the ER and mitochondria (14), and decrease calcium ion (Ca2+) uptake by mitochondria following synaptic transmission–induced Ca2+ release from the ER (15)." — PMID:35227461

> "the cognitive impairment associated with PDZD8 disruption is therefore likely to represent a synaptopathy resulting from synaptic dysfunction" — PMID:35227461

### Suggested terms (cache-verified)

- **GO processes:**
  - GO:0006869 lipid transport; GO:0120013 lipid transfer activity (molecular function)
  - GO:0007032 endosome organization; GO:0008333 endosome to lysosome transport
  - GO:0006851 mitochondrial calcium ion transmembrane transport
  - GO:0051480 regulation of cytosolic calcium ion concentration; GO:0055074 calcium ion homeostasis
  - GO:0060291 long-term synaptic potentiation (modifier DECREASED)
  - GO:0007613 memory; GO:0007611 learning or memory; GO:0050890 cognition
  - GO:0035176 social behavior
  - GO:0097061 dendritic spine organization; GO:0060996 dendritic spine development
  - GO:0022008 neurogenesis
  - GO:0034976 response to endoplasmic reticulum stress
  - GO:0008053 mitochondrial fusion
- **GO cellular components:** GO:0005789 endoplasmic reticulum membrane; GO:0005770 late endosome.
  - The ER–mitochondria and ER–endosome **membrane-contact-site** terms are **not in the cache**. Look them up with OAK before binding.
- **CL:** CL:0000540 neuron; CL:0000598 pyramidal neuron; CL:0000679 glutamatergic neuron; CL:0000617 GABAergic neuron; CL:0000128 oligodendrocyte.

### Mechanism papers to fetch with `just fetch-reference`

These are cited as refs 13–15 in PMID:35227461. None are confirmed.

- **Hirabayashi et al., *Science* 2017**, "ER-mitochondria tethering by PDZD8 regulates Ca²⁺ dynamics in mammalian neurons." Likely PMID:29097544 (SGD reference ID; [yeastgenome](https://www.yeastgenome.org/reference/29097544), [Polleux lab](https://www.polleuxlab.zi.columbia.edu/ermitochondria-tethering-by-pdzd8-regulates-ca2-dynamics-in-mammalian-neurons), [PMC5818999](https://pmc.ncbi.nlm.nih.gov/articles/PMC5818999)). **Confirm.**
- **Elbaz-Alon et al., *Nat Commun* 2020**, "PDZD8 interacts with Protrudin and Rab7 at ER-late endosome membrane contact sites associated with mitochondria" ([PMC7486383](https://pmc.ncbi.nlm.nih.gov/articles/PMC7486383), [Springer](https://link.springer.com/10.1038/s41467-020-18413-9), [IUCC](https://cris.iucc.ac.il/en/publications/pdzd8-interacts-with-protrudin-and-rab7-at-er-late-endosome-membr-2/)). PMID not confirmed; PMID:32917905 appears on the [MIT gene page](https://affinage.wi.mit.edu/gene/PDZD8) but is not tied to this paper.
- **Shirane et al., 2020**, Protrudin and PDZD8 lipid extraction for endosome maturation. PMID not obtained.
- **AMPK–PDZD8 pT527 glutaminolysis paper.** PMID not obtained.

## 7. Anatomical structures affected

- **Primary organ:** the brain (UBERON:0000955). The nervous system is the main system involved.
  - Specific regions: corpus callosum (UBERON:0002336), cerebral white matter, and cerebellum (UBERON:0002037).
  - Hippocampus and olfactory bulb (UBERON:0002264) are affected in the mouse. The hippocampus term was not in the cache.
- **Secondary organs:**
  - Skeletal muscle (myopathy)
  - Spine (scoliosis)
  - Face and palate
  - Eye (myopia, ptosis, amblyopia)
  - Heart (1 case)
  - Linear growth (short stature)
- **Subcellular:** ER membrane, late endosome/lysosome, mitochondria, and the contact sites between them.
- **Laterality:** facial and ocular features are bilateral (e.g. bilateral ptosis).

## 8. Temporal development

- **Onset:** congenital or infantile. Developmental delay is present in all patients, who were assessed between ages 4 and 30.
- **Course:** a fixed neurodevelopmental disorder. No regression has been reported.
- **Possible progressive features (open question):** scoliosis was worse at age 18 than at 13 in C.IV.1. The demyelinating lesions in C.IV.1 raise the possibility of a progressive white-matter process. With no natural-history data, this remains unanswered.
- **Critical periods:** PDZD8 expression is stable from 8 weeks after conception to age 23 (BrainSpan data), which suggests a role throughout neurodevelopment (PMID:35227461).

## 9. Inheritance and population

- **Inheritance:** autosomal recessive. Penetrance in homozygotes is 6/6 within the three families.
- **Expressivity:** variable. ID ranges from moderate to severe, epilepsy is present in 3/6, and the non-core features differ between families.
- **Prevalence:** unknown, with 6 published cases in 3 families. Suggested `prevalence_class`: `CASES_IN_LITERATURE` with `ULTRA_RARE`.
- **Population factors:** no founder variant is known; each family has its own variant. All families are consanguineous, from the Arabian Peninsula and Afghanistan.
- **Sex:** 4 male, 2 female.
- **Not reported:** anticipation, germline mosaicism, carrier frequency.

## 10. Diagnostics

- **Diagnosis is genetic:** exome sequencing, combined with homozygosity mapping in consanguineous families. Confirmation and segregation testing use Sanger sequencing. Exome CNV analysis (ExomeDepth) excluded deletions in family C.
- **Clinical evaluation:**
  - IQ: Stanford-Binet
  - Adaptive behavior: Vineland-II, PEP-3
  - Autism: CARS2 and ADOS-2 against DSM-5 criteria
  - Brain MRI
  - EEG where seizures occur
  - Spine radiographs
  - Ophthalmologic exam
- **Biomarkers:** none. PDZD8 protein is not detectable in blood.
- **Differential diagnosis:**
  - Other autosomal recessive syndromic ID/ASD genes in consanguineous populations
  - Congenital myopathies (myopathic face)
  - Distal 10q deletion syndrome
  - Disorders of the PDZD8 partners: *ZFYVE27*/protrudin (spastic paraplegia) and *RAB7A* (CMT2B)
- **Screening:** no newborn screening. Carrier testing and cascade testing are possible in families with a known variant.

## 11. Outcome and prognosis

- **Survival and life expectancy:** no data. The oldest reported patient is 30 years old.
- **Pregnancy losses:** family B had two in-utero deaths, but it is unknown whether they relate to PDZD8. In mice, survival to weaning was 36–48% lower than expected.
- **Morbidity:** lifelong ID; severe ASD in family C; epilepsy; limited mobility (walking distance) in family C.
- **Prognostic factors:** none established.

## 12. Treatment

There is no disease-specific therapy. Care is supportive and treats symptoms.

| Intervention | Terms (cache-verified) | Basis |
|---|---|---|
| Antiseizure medication | Valproic acid CHEBI:39867; levetiracetam CHEBI:6437 / NCIT:C47581 as `therapeutic_agent` on Pharmacotherapy NCIT:C15986 | C.IV.1 (PMID:40016860) |
| Speech-language therapy | NCIT:C159273 | General care for ID/ASD; not reported in these papers |
| Occupational therapy | NCIT:C121351 | General care for ID/ASD |
| Physical therapy (myopathy, scoliosis) | NCIT:C15302 | General care |
| Genetic counseling / carrier testing | NCIT:C15240 | Recommended in PMID:35227461 |

- **Experimental:** the authors suggest that p.(Y298*) "is potentially amenable to novel nonsense suppression therapies" (PMID:35227461). This is speculative; no trials exist.
- **Pharmacogenomics, gene therapy, cell therapy, clinical trials:** none.

## 13. Prevention

- **Primary prevention:** genetic counseling, carrier testing, and prenatal or preimplantation diagnosis for families with a known variant. Carrier screening can be offered in consanguineous communities.
- **Tertiary prevention:**
  - Seizure management
  - Scoliosis surveillance
  - Ophthalmologic follow-up
  - Cardiac evaluation, given the one case with a heart defect
- **Vaccines and public-health measures:** not applicable.

## 14. Other species / natural disease

- **Natural disease:** none reported. OMIA was not searched.
- **Orthologs:**
  - Mouse *Pdzd8*: 1,147 aa, 87% amino-acid conservation with human.
  - *Drosophila* CG10362 (FBgn0030358): 24% identity, lacks the coiled-coil domain.
- **Yeast:** the SGD reference at 29097544 suggests PDZD8 is studied as an analog of the yeast ERMES ER–mitochondria tethering complex. This is not verified here.

## 15. Model organisms

| Model | Genotype | What it reproduces | Limitations | Source |
|---|---|---|---|---|
| Mouse Pdzd8^tm1b(EUCOMM)Wtsi^ (C57BL/6NTac) | Exon-3 replaced by lacZ, giving p.F333Nfs1* (homozygous) | Repetitive hindlimb jumping (stereotypy); less habituation; less anxiety-like behavior; impaired long-term spatial memory (Barnes probe); lower 3×TBS LTP and paired-pulse facilitation; brain-volume changes, including relative corpus callosum reduction; impaired social recognition and social odor discrimination; more dendritic spines; less adult neurogenesis; higher ER-stress and mitochondrial-fusion transcripts; hyperactivity in the dark phase; higher metabolic rate; low body weight and size; lower plasma triglyceride in males; reduced pre-weaning viability | No facial-dysmorphism equivalent. Sociability itself is intact. Unbalanced sex groups in some experiments. ER-stress and mitochondrial markers measured as mRNA only | PMID:35227461; PMID:40016860 |
| *Drosophila* Act5C-Gal4 > UAS-CG10362-RNAi (VDRC v8317) | Ubiquitous knockdown, about 56% transcript reduction | Impaired long-term (48-hour) courtship memory; learning and short-term memory intact | Low conservation with human; partial knockdown only | PMID:35227461 |

> "Mice homozygous for a premature termination codon in Pdzd8 exhibited brain structural, hippocampal spatial memory, and synaptic plasticity deficits." — PMID:35227461

> "Our finding that the Pdzd8tm1b mouse model and all six known cases of IDDADF exhibit autistic behavior, with ASD diagnosed in five cases, identifies this trait as a common outcome of biallelic disruption of PDZD8 in humans and mice." — PMID:40016860

**Resources:**
- Mouse: EMMA strain 14234 (MRC Harwell); IMPC phenotyping data at mousephenotype.org.
- Fly: VDRC line v8317.

---

### Notes for the curator

- **Evidence grading.** Clinical rows are `HUMAN_CLINICAL`. Mouse and fly rows are `MODEL_ORGANISM`.
- **Background quotes.** The mechanistic sentences quoted from the introductions of the two clinical papers are background citations. Mark them `quote_role: BACKGROUND`, or better, quote the primary cell-biology papers once they are fetched.
- **Myopathy.** Consider a note on the myopathy phenotype because of the *ANKRD2* variant in family A.
- **MONDO term.** MONDO:0859281 is uncached; MONDO:0014017 is the wrong disease and must not be used.

### Sources
- PMID:35227461 — Al-Amri AH et al. *Biol Psychiatry* 2022. doi:10.1016/j.biopsych.2021.12.017
- PMID:40016860 — Pantiru AD et al. *Mol Autism* 2025. doi:10.1186/s13229-025-00650-8 ([PMC11866840](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11866840/); [Springer](https://link.springer.com/article/10.1186/s13229-025-00650-8))
- Web: [MedGen C5774206 mirror](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/commit/bd92c530490f55ed2fd68cfd16ea8c327904c65c/www.ncbi.nlm.nih.gov/medgen/C5774206/index.html); [White Rose eprint](https://eprints.whiterose.ac.uk/id/eprint/223375); [ORA Oxford](https://ora.ox.ac.uk/objects/uuid:0acf5689-c19a-46ce-8c24-1c8e0f774fde); [NDCN Oxford](https://www.ndcn.ox.ac.uk/publication/2092658); [Pantiru thesis](https://etheses.whiterose.ac.uk/id/eprint/32930/); [Mol Autism mirror](https://biomedcentral-molecularautism.publicaciones.saludcastillayleon.es/articles/10.1186/s13229-025-00650-8); [Mol Autism PDF mirror](https://biomedcentral-molecularautism.publicaciones.saludcastillayleon.es/counter/pdf/10.1186/s13229-025-00650-8.pdf); [Elbaz-Alon 2020, Springer](https://link.springer.com/10.1038/s41467-020-18413-9); [PMC7486383](https://pmc.ncbi.nlm.nih.gov/articles/PMC7486383); [IUCC record](https://cris.iucc.ac.il/en/publications/pdzd8-interacts-with-protrudin-and-rab7-at-er-late-endosome-membr-2/); [PMC5818999](https://pmc.ncbi.nlm.nih.gov/articles/PMC5818999); [Polleux lab](https://www.polleuxlab.zi.columbia.edu/ermitochondria-tethering-by-pdzd8-regulates-ca2-dynamics-in-mammalian-neurons); [Polleux lab page 2](https://www.polleuxlab.zi.columbia.edu/new-page-3); [SGD 29097544](https://www.yeastgenome.org/reference/29097544); [ERMES topic, SciSpace](https://scispace.com/topics/ermes-2md5p8us); [MIT PDZD8](https://affinage.wi.mit.edu/gene/PDZD8)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 4 |
| Quoted claims found in source | 3 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 9 |
| On topic | 8 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMC:PMC7486383`: "PDZD8 interacts with Protrudin and Rab7 at ER-late endosome membrane contact sites associated with mitochondria"
  - closest text in source: "Endosome maturation depends on membrane contact sites (MCSs) formed between endoplasmic reticulum (ER) and endolysosomes (LyLEs)"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 78 |
| Resolved | 78 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 7 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 5 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0000955` (1 mention) - the report calls it "Primary organ:** the brain"; UBERON calls it **brain**, and lists "the brain" among its other names
- `UBERON:0002336` (1 mention) - the report calls it "Specific regions: corpus callosum"; UBERON calls it **corpus callosum**
- `UBERON:0002264` (1 mention) - the report calls it "Hippocampus and olfactory bulb"; UBERON calls it **olfactory bulb**
- `NCIT:C15302` (1 mention) - the report calls it "Physical therapy (myopathy, scoliosis)"; NCIT calls it **Physical Therapy**
- `NCIT:C15240` (1 mention) - the report calls it "Genetic counseling / carrier testing"; NCIT calls it **Genetic Counseling**

Every term resolved, and every label the report gave matched.