---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-28T15:18:49.739361'
end_time: '2026-11-28T15:22:01.959650'
duration_seconds: 192.22
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Chalazion
  mondo_id: MONDO:0005844
  category: Infectious Disease
  causal_genes: not recorded
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
  web_search_requests: 18
  num_turns: 25
  total_cost_usd: 1.0492408000000002
  session_id: 2628b978-ff9a-4655-9195-d993d078849b
  stop_reason: end_turn
  permission_denials: 4
  denied_tools:
  - Bash
  tool_calls: 24
  retrieval_calls: 19
  assistant_text_blocks: 2
citation_count: 35
reference_validation:
  total_references: 21
  verified: 21
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 7
  quotes_valid: 4
  quotes_unsupported: 3
  unsupported_quote_references:
  - PMID:35291979
  - PMC:PMC8925234
  - PMID:35296627
  relevance_assessed: 21
  on_topic: 10
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 1
  verified: 1
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0005844
    reported_labels:
    - MONDO
    ontology_label: chalazion
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Chalazion
- **MONDO ID:** MONDO:0005844 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** not recorded
- **Category:** Infectious Disease

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Chalazion** covering all of the
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

Bash can't run here, so I'm using web search for the PubMed lookups instead.

# Chalazion: Disease Characteristics Research Report

**How I scoped this and what limited it**
- **Scope.** This report covers MONDO:0005844, chalazion: a chronic, sterile lipogranulomatous swelling of the eyelid that centres on a meibomian gland (or, more rarely, a Zeis gland).
- **No causal gene.** None was supplied and none exists. Chalazion is not a Mendelian disorder, and I found no OMIM entry, ClinVar variant or GWAS-level susceptibility locus.
- **Category label.** The template files chalazion under "Infectious Disease", but the evidence I found does not support that. Chalazion is mainly a sterile, obstruction-driven inflammatory lesion. A microbial contribution (*Cutibacterium acnes*, *Demodex* mites) is suspected but not proven (Section 5).
- **Tool limits.** My shell and PubMed API access were blocked, so all evidence comes from web search snippets of PubMed records, journal pages and indexing mirrors. I could not quote abstracts word for word; quoted text is from snippets. Where I could not see a PMID, I say so.
- **Ontology IDs.** I verified only the MeSH and ICD-10 codes. HPO, GO, CL, UBERON and NCIT terms are given as labels only, because I did not check their numeric IDs. Map them before loading.

---

## 1. Disease Information

**Overview.** MeSH defines chalazion as "a non-neoplastic cyst of the meibomian glands of the eyelid" ([MeSH D017043](https://meshb.nlm.nih.gov/record/ui?ui=D017043)).
- **Usual cause.** It is usually described as arising "secondary to non-infectious obstruction of sebaceous gland ducts". Lipid then leaks into the surrounding tissue and provokes a foreign-body lipogranulomatous reaction ([StatPearls NBK499889](https://www.ncbi.nlm.nih.gov/books/NBK499889/); [EyeWiki](https://eyewiki.aao.org/Chalazion)).
- **How it differs from hordeolum.** A hordeolum (stye) is an acute, usually staphylococcal infection of the same glands. A chalazion is chronic and painless.

| Identifier | Value | Source |
|---|---|---|
| MONDO | MONDO:0005844 | supplied |
| MeSH | **D017043** (tree numbers C04.182.197, C11.338.300) | [MeSH](https://meshb.nlm.nih.gov/record/ui?ui=D017043) |
| ICD-10 | **H00.1** Chalazion, under the parent H00 "Hordeolum and chalazion" | [gesund.bund.de](https://gesund.bund.de/en/icd-code-suche/h00-1) |
| ICD-10-CM | H00.1x by eyelid (e.g., H00.11 = right upper eyelid) | [AAPC](https://www.aapc.com/codes/icd-10-codes/H00.11) |
| ICD-11 | Not retrieved; verify in the WHO browser | — |
| OMIM / Orphanet | None. It is not a rare or genetic disease | — |

**Synonyms:** meibomian cyst; tarsal cyst; chalazia (plural); lipogranulomatous blepharitis (veterinary usage) ([Guelph AHL](https://www.uoguelph.ca/ahl/node/12041)).

**Type of evidence:** mostly aggregated and clinical. The sources are retrospective EHR and claims cohorts (US Veterans Affairs, Israel's Clalit health service, Japan's national claims database), hospital case series, and a small number of randomized trials.

## 2. Etiology

**Causes.** The leading model is mechanical:
1. Meibomian duct obstruction, often from meibomian gland dysfunction (MGD) or blepharitis.
2. This leads to retained, then extravasated meibum.
3. The leaked lipid triggers a granulomatous foreign-body response.

Infection is not the primary cause. A histology series concluded that infectious etiology was ruled out ([Moran CORE](https://morancore.utah.edu/?p=119380)). Possible microbial co-factors are covered in Section 5.

**Risk factors (human clinical, observational):**
- **Blepharitis.** This is the strongest association: OR 6.2 in an Israeli case-control study of 9,119 cases and 9,119 controls (Nemet, Vinker & Kaiserman, *Cornea* 2011;30:1376-81, PMID 21993469). The same study found rosacea (OR 2.9), gastritis, anxiety, irritable bowel syndrome and smoking to be significantly more common in cases. Diabetes and hypothyroidism were *less* common in cases ([TAU CRIS](https://cris.tau.ac.il/en/publications/associated-morbidity-of-chalazia/); [EyeWiki](https://eyewiki.aao.org/Chalazion)).
- **Rosacea, periocular skin disease and tear-film disease.** In 3,453,944 US veterans, 208,720 (6.04%) had a chalazion diagnosis. Rosacea had OR 2.50 (p<0.0005). The authors concluded that "periocular skin, eyelid margin and tear film abnormalities were most strongly associated with risk for chalazion" ("Prevalence and risk factors for chalazion in an older veteran population", *BJO* 2021, doi:10.1136/bjophthalmol-2020-318420; [BJO](https://bjo.bmj.com/node/234134)). I did not retrieve its PMID. A separate 2023 study found that a rosacea diagnosis increased the odds of surgical excision ([PubMed 37032590](https://www.pubmed.gov/37032590/)).
- **Demodex (children).** Mites were found in 236 of 446 paediatric chalazion patients (52.9%) and in no controls. Infestation was linked to recurrence, multiple lesions, MGD and skin involvement. The authors concluded that "demodicosis should be considered a risk factor for chalazia in children" (Huang et al., *BMC Ophthalmol* 2022, PMID 35291979; [PMC8925234](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8925234/)). A second paediatric series found Demodex in 73.3% of cases versus 35.7% of controls ([Springer](https://link.springer.com/article/10.1186/s12886-022-02261-w)).
- **Low vitamin A.**
  - Low serum vitamin A was linked to *recurrent, multiple* chalazia (P=0.026). The authors suggested chalazion could be "one of the ocular presentations of vitamin A deficiency" (Malekahmadi et al. 2017, PMID 29392144).
  - Chinese children with chalazion had lower serum vitamin A than controls (0.54 vs 0.60 µmol/L) and more deficiency (52.2% vs 28.6%) (*Optom Vis Sci* 2022; [Healio](https://cm.healio.com/news/optometry/20220526/low-serum-vitamin-a-levels-linked-to-chalazion-in-children)).
- **Drugs.** Repeated case reports and series link the proteasome inhibitor bortezomib to chalazia. In a Mount Sinai series of 17 myeloma patients on proteasome inhibitors with eyelid complications, 14 (87.5%) had chalazia. Chalazia relapsed when bortezomib was restarted (PMID 36593601; [Hematol Rep 2015](https://doaj.org/article/48e30629710641309b29a7ffdeb5241f); [Harvard Eye](https://eye.hms.harvard.edu/publications/chalazia-associated-bortezomib-therapy-multiple-myeloma)).
- **Demographics.** Being Hispanic/Latino, American Indian/Alaska Native or Asian was associated with higher paediatric rates (PMID 34062122). Lower socioeconomic status and urban residence were risk factors in the Israeli study (PMID 21993469).

**Genetic risk and protective factors:** none established; no ClinVar or GWAS Catalog associations were found. One Mendelian-randomization study proposed gut-microbial taxa as causal factors. *Catenibacterium* and "Family XIII" appeared to raise risk, and *Veillonella* appeared protective. This is computational genetic-association evidence only ([Front Med 2024](https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2024.1411271/text)).

**Environmental protective factors:** no strong data. Lid hygiene and treating MGD, rosacea or Demodex are logical, but no trials show they prevent first episodes. A trial comparing omega-3, anti-Demodex treatment and an eyelid cleanser in children is registered as NCT07496515 ([protocol](https://cdn.clinicaltrials.gov/large-docs/15/NCT07496515/Prot_001.pdf)).

**Gene–environment interactions:** none described.

## 3. Phenotypes

| Phenotype | Type | Frequency / characteristics | Suggested HPO label |
|---|---|---|---|
| Painless eyelid nodule, firm and rubbery, in the tarsal plate | Sign | Defining (~100%); slowly enlarges over weeks | Chalazion; Eyelid nodule |
| Eyelid swelling or erythema (inflamed or early lesion) | Sign | Common early on | Eyelid oedema; Erythema of the eyelid |
| Multiple or recurrent chalazia | Course | 31% had more than one if no MGD/blepharitis, versus 56% with them (PMID 34062122) | Recurrent chalazion |
| Blepharitis, MGD or Demodex as coexisting signs | Sign | Strongest association (OR 6.2) | Blepharitis; Meibomian gland dysfunction |
| Induced astigmatism or blurred vision (large upper-lid lesions) | Sign | Occasional; risk factors studied in children ([Rev Optom](https://www.reviewofoptometry.com/news/article/study-identifies-risk-factors-for-chalaziainduced-astigmatism)) | Astigmatism; Blurred vision |
| Pyogenic granuloma on the conjunctival surface | Complication | 22 of 82 surgical specimens in one series (PMID 37934292) | Pyogenic granuloma |
| Ptosis or mechanical eyelid effect | Sign | Occasional | Ptosis |

- **Onset:** any age. Paediatric first onset peaks at 2–5 years (PMID 34062122). Procedures peak at 15–19 and 30–39 years (Japan NDB study, below).
- **Severity:** usually mild.
- **Course:** episodic or recurrent.
- **Quality of life:** no EQ-5D or SF-36 data found. The burden is mainly cosmetic, mild discomfort, possible astigmatism or amblyopia risk in young children, and in children the need for general anaesthesia for surgery.

## 4. Genetic/Molecular Information

- **Causal genes, pathogenic variants, modifier genes, chromosomal abnormalities:** not applicable. None are reported, and there are no ClinVar, ClinGen or OMIM entries.
- **Somatic changes:** none. The important molecular differential is sebaceous carcinoma, which is a separate neoplasm.
- **Epigenetics:** no data.

## 5. Environmental Information

- **Lifestyle factors:** smoking (associated in PMID 21993469), poor lid hygiene and low dietary vitamin A (PMID 29392144).
- **Drugs:** bortezomib (PMID 36593601).
- **Infectious and microbial agents (none proven causal):**
  - *Cutibacterium acnes* was detected inside the granulomas of 20 histologically confirmed chalazia, which suggests a possible role in forming the granuloma ([Rev Optom 2021](https://reviewofoptometry.com/article/possible-involvement-of-c-acnes-in-pathogenesis-of-chalazion); review: Suzuki & Kinoshita, *Microorganisms* 2024, [PMC11356515](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11356515/)).
  - In 7 patients studied by 16S rDNA sequencing, culture was negative, but the lid microbiome differed from healthy controls ([BJO 2025](https://bjo-bmj-com.bibliotheek.ehb.be/content/early/2025/04/21/bjo-2024-325988)).
  - *Demodex folliculorum/brevis* infestation is a risk factor (PMID 35291979).
  - *Staphylococcus* mainly causes hordeolum, not chalazion.
  - A UCSF review found antibiotics were "frequently prescribed" but "unlikely to improve resolution" (PMID 35296627).

## 6. Mechanism / Pathophysiology

**Causal chain:**
1. Predisposing lid-margin disease leads to keratinised or thickened meibum and narrowing of the duct. Possible triggers are MGD, blepharitis, rosacea, Demodex, low vitamin A and bortezomib. This step is supported by association studies; the step from vitamin A loss to keratinisation is inferred from known effects of vitamin A deficiency.
2. Duct obstruction results in meibum building up within the acinus or duct.
3. The gland wall ruptures, so lipid escapes into the tarsal stroma. This is shown histologically; the trigger for rupture is inferred.
4. Free lipid acts as a foreign body and leads to recruitment of macrophages, which form epithelioid histiocytes and multinucleated giant cells, including the Langhans and Touton types. Neutrophils and lymphocytes gather around lipid vacuoles ([Moran CORE](https://morancore.utah.edu/?p=119380); [StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK499889/)).
   - *Possible branch (inferred):* microbial antigens such as *C. acnes* or Demodex debris may amplify the granuloma.
5. A T-cell-driven granuloma results. In 82 specimens, T cells predominated and CD4 cells outnumbered CD8 cells, which the authors suggested "may be closely related to the pathological mechanisms" (Nemoto et al., *Graefes Arch* 2024, PMID 37934292). An older small abstract instead reported mostly CD8 and CD45RO cells ([CORE](https://core.ac.uk/works/125389897)), so the data conflict.
6. A fibrous pseudocapsule forms, producing a chronic, firm, painless nodule. Two branches follow:
   - **(a)** spontaneous drainage or resorption leads to resolution;
   - **(b)** the lesion breaks through the conjunctiva, leading to pyogenic granuloma; or it presses on the cornea, leading to astigmatism.

- **Pathways:** no specific signalling pathway has been characterised. The lesion is a lipid-induced foreign-body granulomatous inflammation.
- **Suggested GO process labels:** granuloma formation; inflammatory response; T cell activation; macrophage activation; lipid metabolic process (meibum).
- **Suggested CL cell-type labels:** meibocyte (sebocyte); macrophage; multinucleated giant cell; CD4-positive alpha-beta T cell; neutrophil; plasma cell.
- **Omics, single-cell or spatial data:** none found. The only profiling data are the flow cytometry and immunohistochemistry immunophenotyping in PMID 37934292.

## 7. Anatomical Structures Affected

- **Primary site:** eyelid, specifically the meibomian (tarsal) gland within the tarsal plate. It occurs less often in the Zeis gland. Suggested UBERON labels: meibomian gland, tarsal plate, eyelid, upper eyelid, lower eyelid.
- **System:** eye and adnexa. MeSH places it under both eye diseases and skin diseases (C11, C04).
- **Tissues affected:** sebaceous glandular epithelium and the surrounding dense connective tissue of the tarsus, plus conjunctiva if a granuloma forms.
- **Subcellular:** the main compartment is extracellular lipid. Suggested GO cellular-component label: lipid droplet, within meibocytes.
- **Secondary involvement:** cornea, through induced astigmatism.
- **Lateralization:** usually one lesion on one eye, but multiple and both-eye lesions occur (for example, bilateral lesions with bortezomib, [PMC7520400](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7520400/)).

## 8. Temporal Development

- **Onset:** subacute to insidious. It may start as an inflamed swelling that becomes a chronic, non-tender nodule.
- **Duration:** self-limited in most cases. StatPearls states that most "resolve within one month" with conservative measures ([NBK499889](https://www.ncbi.nlm.nih.gov/books/NBK499889/)).
- **Pattern:** can be relapsing, especially with MGD or blepharitis (PMID 34062122) and with Demodex (PMID 35291979).
- **Staging:** no formal staging system exists.
- **Critical period:** early childhood. Persistent large upper-lid lesions can cause astigmatism that risks amblyopia.

## 9. Inheritance and Population

- **Inheritance:** not heritable in a Mendelian sense; risk is multifactorial.
- **Prevalence and incidence:**
  - 6.04% of veterans had a diagnosis (BJO 2021).
  - About 2% of paediatric eye-clinic patients in Wisconsin (PMID 34062122).
  - 0.57% of about 2 million new patients at an Indian eye hospital ([Clin Ophthalmol 2020](https://doaj.org/article/ca062ad8d4484736836cd2c54fdfa03b)).
  - 1.56 per 1,000 in a São Paulo population sample, with more cases in women ([Rev Bras Oftalmol 2015](https://scite.ai/reports/10.5935/0034-7280.20150045)).
- **Age and sex from procedure claims (Japan, 9 years, *Ophthalmol Sci* 2026, [PMC12887806](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12887806/)):** rates of chalazion procedures had two peaks in each sex.

  | Group | Peak ages | Rate per 100,000 person-years |
  |---|---|---|
  | Women, first peak | 15–19 | 80.6 |
  | Men, first peak | 15–19 | 40.9 |
  | Women, second peak | 30–34 | not retrieved |
  | Men, second peak | 35–39 | 56.0 |

  Procedure rates fell over the study decade.
- **Ethnicity (children):** Hispanic/Latino 3.8% versus non-Hispanic 1.8%; American Indian/Alaska Native 4.3%; Asian 4.0%; White 1.7%. Race did not predict surgery (PMID 34062122).
- **Geography:** higher in coastal US regions (BJO 2021).
- **Sex ratio:** varies by study and setting, from female-predominant (Brazil; Japanese teenagers) to the male-dominated veteran cohort.

## 10. Diagnostics

- **Clinical diagnosis:** a firm, non-tender nodule in the tarsal plate on examination with lid eversion and slit lamp. Histopathology "is rarely needed" for typical lesions (StatPearls).
- **Histopathology:** lipogranulomatous inflammation with lipid vacuoles, epithelioid histiocytes, Langhans and Touton giant cells, neutrophils, lymphocytes and plasma cells, often inside a fibrous pseudocapsule ([Moran CORE](https://morancore.utah.edu/?p=119380); [TAU WebPath](https://www.tau.ac.il/medicine/tau-only/webpath/labs/ophthlab/ophtha02.htm)).
- **Missed malignancy:** in a large series of specimens sent as chalazion, 1.1% were sebaceous carcinoma, 0.3% basal cell carcinoma and 0.2% premalignant. The authors recommended sending *all* specimens, primary or recurrent, for histology (PMID 14762403; [Eye](https://www.nature.com/articles/6700603)).
- **When to biopsy:** recurrent lesions in the same place, lash loss (madarosis) or older age call for a full-thickness biopsy rather than a shave ([Eye](https://www.nature.com/articles/6701330)).
- **Ancillary tests:**
  - Lash epilation and microscopy for Demodex.
  - Meibography to assess MGD.
  - Serum vitamin A in recurrent paediatric cases (research use).
  - Culture is usually unhelpful.
  - Imaging is only for atypical lesions.
- **Genetic and omics testing:** not indicated.
- **Differential diagnosis:**
  - hordeolum (acute and painful);
  - sebaceous carcinoma;
  - basal or squamous cell carcinoma;
  - pyogenic granuloma;
  - tuberculous or other granulomatous blepharitis (one case was confirmed by PCR, [Pan-Am J Ophthalmol 2022](https://doaj.org/article/7ba9739d12704db0996898c800d4e117));
  - Merkel cell carcinoma and lymphoma (atypical cases).
- **Screening:** none.

## 11. Outcome/Prognosis

- **Mortality:** none attributable to chalazion itself. Mortality is relevant only when a misdiagnosed sebaceous carcinoma is missed.
- **Recovery:** excellent; most lesions resolve with conservative care or a procedure.
- **Recurrence after treatment:** 34.6% after triamcinolone injection versus 8% after incision and curettage (PMID 31528769).
- **Prognostic factors for recurrence:**
  - MGD or blepharitis (PMID 34062122);
  - Demodex (PMID 35291979);
  - rosacea, which also raises the chance of needing surgery (PMID 37032590);
  - low vitamin A with multiple lesions (PMID 29392144).
- **Complications:**
  - pyogenic granuloma;
  - astigmatism;
  - secondary infection or preseptal cellulitis;
  - after steroid injection, skin depigmentation and fat atrophy. Rare ocular complications such as intravascular embolisation have been reported (PMID 14700103).
- **Quality-of-life instruments:** none validated for this condition.

## 12. Treatment

| Intervention | Suggested NCIT label | Evidence |
|---|---|---|
| Warm compresses, lid massage, lid hygiene | Heat therapy; Hygiene | First-line; StatPearls suggests 15 min, 2–4 times a day. In an RCT, warm compresses alone were as effective as warm compresses plus tobramycin or tobramycin/dexamethasone (Wu et al., *Acta Ophthalmol* 2018, PMID 29338124) |
| Intralesional triamcinolone acetonide | Intralesional injection; Triamcinolone acetonide | RCT: 61.5% complete resolution vs 84% with incision and curettage (P=0.072), but more recurrence (PMID 31528769). Another early RCT found incision and curettage gave "a significantly higher rate of resolution by two weeks" (Jacobs et al., *BJO* 1984, PMID 6498138). In a third study, injection resolved 77% but 54% needed repeat injections (Watson & Austin 1984, PMID 6498137) |
| Incision and curettage (trans-conjunctival) | Incision and drainage; Curettage | Standard for lesions that persist past 4–6 weeks; 84–90% resolution (above) |
| Treating the underlying lid disease | Doxycycline; Tea tree oil; Ivermectin | Logical choice for rosacea, MGD or Demodex; the trial NCT07496515 is ongoing |
| Systemic antibiotics | Antibiotic therapy | Not helpful for uncomplicated chalazion (PMID 35296627) |
| Stopping bortezomib or switching proteasome inhibitor | Drug withdrawal | In one series, 80% of episodes resolved with eye treatment plus omitting bortezomib (PMID 36593601) |
| Oral probiotics (experimental) | Probiotic | 20-patient pilot study ([IJO 2022](https://iris.uniroma1.it/retrieve/699a403e-6f15-4467-80b1-119c6bb1055e/Filippelli_Effectiveness-of%20oral-probiotics-supplementation_2022.pdf)) |

- **Systematic reviews:** none found. The Cochrane review CD007742 covers *hordeolum* only and excluded chalazia ([Cochrane](https://www.cochrane.org/CD007742/EYES_interventions-acute-internal-hordeolum)).
- **Usual treatment sequence:**
  1. Conservative care for about 2–6 weeks ([AAO EyeNet](https://www.aao.org/eyenet/article/chalazion-management-evidence-questions)).
  2. Then a steroid injection or incision and curettage.
  3. Histology for recurrent or atypical lesions.
- **Not applicable:** pharmacogenomics, gene therapy, cell therapy, RNA therapy, immunotherapy.

## 13. Prevention

- **Primary prevention:** no vaccine. Daily lid hygiene, treating MGD, rosacea or Demodex, and adequate vitamin A intake are reasonable but not proven by trials.
- **Secondary prevention:** early warm-compress treatment.
- **Tertiary prevention:**
  - Treat lid-margin disease to reduce recurrence.
  - Send recurrent lesions for histology to exclude sebaceous carcinoma.
  - Monitor eyelid status in patients on bortezomib.
- **Not relevant:** genetic counselling, screening programmes, public-health measures.

## 14. Other Species / Natural Disease

- **Dogs:** chalazion is recognised in dogs, often called lipogranulomatous blepharitis, and it is "frequently an accompanying diagnosis" with meibomian gland adenomas. A gland obstructed by an adenoma ruptures and leaks secretion, so most cases are in older animals ([Guelph AHL](https://www.uoguelph.ca/ahl/node/12041); [Today's Veterinary Practice](https://todaysveterinarypractice.com/observations-in-ophthalmology-clinical-approach-to-canine-eyelid-disease-blepharitis/)).
- **Course and treatment in dogs:** lesions are often self-limiting. Treatment is chalazion clamp plus curettage.
- **Cats:** reported in reviews of eyelid tumours ([TVP](https://todaysveterinarypractice.com/ophthalmology/eyelid-tumors-dogs-cats/)).
- **Comparative pathology:** the same lipogranulomatous reaction to escaped meibum as in humans.
- **Not applicable:** zoonotic transmission, OMIA entries, breed predispositions (none established). NCBI Taxon IDs were not retrieved.

## 15. Model Organisms

I found no dedicated genetic or induced chalazion models. Possible relevant approaches, which are inferred and were not verified in this session:
- MGD models, such as duct-obstruction or keratinisation models in mice and rabbits;
- lipid-injection granuloma models.

The dog with spontaneous disease is the closest natural analogue. No MGI, IMPC or ZFIN chalazion models were identified.

---

### Main evidence gaps
- No population incidence studies outside claims and hospital data.
- No systematic review of chalazion treatment.
- Conflicting T-cell subset data (CD4- versus CD8-dominant).
- The roles of *C. acnes* and Demodex are only associations.
- No genetic, omics or model-organism data.

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 21 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 7 |
| Quoted claims found in source | 4 |
| Quoted claims **not** found in source | 3 |
| References weighed for topical relevance | 21 |
| On topic | 10 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:35291979` *(abstract only)*: "demodicosis should be considered a risk factor for chalazia in children"
  - closest text in source: "Demodicosis should be considered as a risk factor of chalazia"
- `PMC:PMC8925234` *(abstract only)*: "demodicosis should be considered a risk factor for chalazia in children"
  - closest text in source: "Demodicosis should be considered as a risk factor of chalazia"
- `PMID:35296627` *(abstract only)*: "unlikely to improve resolution"
  - Text part not found as substring: 'unlikely to improve resolution' (note: only abstract available for PMID:35296627, full text may contain this excerpt)

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 1 |
| Resolved | 1 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0005844` (2 mentions) - the report calls it "MONDO"; MONDO calls it **chalazion**