---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-23T01:55:08.377729'
end_time: '2026-10-23T01:58:50.461462'
duration_seconds: 222.08
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Brunet-Wagner Neurodevelopmental Syndrome
  mondo_id: MONDO:0859217
  category: Mendelian
  causal_genes: RBL2
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
  web_search_requests: 3
  num_turns: 23
  total_cost_usd: 2.1869748
  session_id: 556cb493-7595-491e-83fc-7d98f62de147
  stop_reason: end_turn
  permission_denials: 4
  denied_tools:
  - Bash
  - mcp__ols-mcp__search_all_ontologies
  - mcp__pubmed__search_articles
  assistant_text_blocks: 3
citation_count: 14
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 12
  on_topic: 7
  validator_version: 0.3.0
term_validation:
  total_terms: 62
  verified: 61
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0859217
    reported_labels:
    - MONDO
    ontology_label: Brunet-Wagner neurodevelopmental syndrome
  labels_variant: 1
  unresolvable_prefixes:
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Brunet-Wagner Neurodevelopmental Syndrome
- **MONDO ID:** MONDO:0859217 (if available)
- **Causal gene(s):** RBL2
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

Please provide a comprehensive research report on **Brunet-Wagner Neurodevelopmental Syndrome** covering all of the
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

Let me fetch the large cohort paper for detail.

I've collected the key papers (Brunet 2020, Samra 2021, Rips 2022, Aughey 2024/25 Brain, plus the mouse and neuronal p130 studies). Next I'm checking the ontology IDs before writing the report.

I've checked the term IDs; now writing the report.

# Brunet-Wagner Neurodevelopmental Syndrome (BRUWAG; *RBL2*): Research Report

**Target:** Brunet-Wagner neurodevelopmental syndrome, MONDO:0859217, causal gene **RBL2** (encoding p130, also called RB transcriptional corepressor-like 2). Cytogenetic location 16q12.2; gene OMIM *180203; disease OMIM #619690.

**How the identifiers were checked.** I took HPO, GO and CL IDs and labels from this repository's committed term caches (`cache/hp`, `cache/go`, `cache/cl/terms.csv`). The **RBL2 HGNC ID (`hgnc:9894`) is from memory and is not in `cache/hgnc/terms.csv`.** It must be confirmed with `just validate-terms` before it is bound. The MONDO ID is as given in the brief and in the draft entry. The OLS and PubMed tools were not authorised in this session, so I did not resolve terms live. Literature came from Europe PMC, PMC and web searches. The quotes below are from the cached full text of PMID:32105419 or from short verbatim excerpts I saw. **Re-verify every snippet** with `just fetch-reference` and `just count-verified-snippets`; for the papers other than PMID:32105419 I only saw summaries.

---

## 1. Disease information

**Overview.** BRUWAG is an autosomal recessive neurodevelopmental disorder caused by biallelic predicted loss-of-function (pLOF) variants in *RBL2*. Its main features are:
- global developmental delay with moderate-to-profound intellectual disability
- infantile hypotonia
- absent speech and frequent inability to walk
- postnatal (often progressive) microcephaly
- stereotypies and aggressive or self-injurious behaviour
- sleep disturbance
- eye findings (strabismus, nystagmus, optic atrophy)
- seizures in about one-third of patients
- brain atrophy on MRI and, in a subset, regression

The largest series describes it as progressive, with a neurodegenerative component (Aughey et al. 2025, PMID:39692517).

**Identifiers**

| Resource | ID |
|---|---|
| MONDO | MONDO:0859217 |
| OMIM (phenotype) | #619690 Brunet-Wagner neurodevelopmental syndrome |
| OMIM (gene) | *180203 RBL2 |
| Disease Ontology | DOID:0061126 (synonym BRUWAG) |
| KEGG Disease | H02613 |
| MedGen | C5562056 |
| Orphanet / ICD-10 / ICD-11 / MeSH | No specific entry found; it falls under general intellectual-disability codes |

**Synonyms:** BRUWAG; RBL2-related neurodevelopmental disorder; autosomal recessive RBL2-associated progressive neurodevelopmental disorder.

**Source of the information:** published patient-level case series (2 + 3 + 1 + 35 individuals), summarised by aggregate resources (OMIM, KEGG, MalaCards). There are no EHR data.

**Literature base (complete as far as I found)**
1. **Brunet et al. 2020**, *Ann Clin Transl Neurol* 7:390 — PMID:32105419, doi:10.1002/acn3.50992. Founding report: 2 siblings, compound heterozygous.
2. **Samra et al. 2021**, *J Hum Genet* 66:1101–1112 — PMID:33980986, doi:10.1038/s10038-021-00931-z. Three patients from two families, with fibroblast studies of DNA methylation and telomeres.
3. **Rips et al. 2022**, *Eur J Med Genet* 65:104513 — PMID:35487417, doi:10.1016/j.ejmg.2022.104513. One child with a homozygous frameshift and orbital nodular fasciitis.
4. **Aughey, Cali, Maroofian et al. 2025**, *Brain* 148(4):1194–1211 (online 18 Dec 2024) — PMID:39692517, PMC11967543, doi:10.1093/brain/awae363. 35 patients from 20 families plus a *Drosophila* model. **This is the primary source for phenotype frequencies.**

## 2. Etiology

- **Cause:** germline biallelic pLOF variants in *RBL2* (Mendelian, autosomal recessive). There is no environmental or infectious cause.
- **Genetic risk factors:**
  - Parental consanguinity was present in 17/20 families (85%) (PMID:39692517).
  - Each pLOF allele is individually rare. Brunet et al. calculated a combined gnomAD LoF allele frequency of 0.00027 and so a minimal birth risk of about 1 in 13.2 million in outbred populations (PMID:32105419).
- **Common-variant link:** GWAS associate the *RBL2* locus with intelligence and educational attainment. This is a common-variant association, not a protective or modifier allele for BRUWAG.
- **Protective factors and gene–environment interactions:** none known.
  - Brunet et al. speculated that seizures might act as a stress "trigger" for neuronal death. They wrote: "One could speculate that the seizures in individual II:2 may have acted as a trigger for neuronal death at some point." This is a hypothesis only.

## 3. Phenotypes

Frequencies are from Aughey et al. 2025 (PMID:39692517) unless stated otherwise. Age at last evaluation was 2–36 years (median 13).

| Phenotype | Frequency | HPO term (verified in cache) | Notes |
|---|---|---|---|
| Global developmental delay / intellectual disability | 35/35 (100%) | HP:0001263 Global developmental delay; HP:0010864 Severe intellectual disability | Moderate to profound. Quote: "Global developmental delay and intellectual disability were observed uniformly, ranging from moderate to profound" |
| Motor delay | 35/35 | HP:0001263 | |
| Never walked independently | 21/34 (62%) | HP:0002540 Inability to walk | |
| Absent speech | 25/34 (74%) | HP:0001344 Absent speech | |
| Infantile/neonatal hypotonia | 31/35 (89%) | HP:0008947 Floppy infant; HP:0001252 Hypotonia | Brunet: "After birth, she was noted to be floppy" |
| Microcephaly at last evaluation | 28/33 (85%) | HP:0000252 Microcephaly; HP:0000253 Progressive microcephaly | Postnatal and progressive; normal birth measurements in the Brunet siblings |
| Seizures | 13/35 (37%) | HP:0001250 Seizure; HP:0032794 Myoclonic seizure | Myoclonic, drug-resistant seizures in Brunet II:2 |
| Regression | 5/29 (17%) | HP:0002376 Developmental regression | Brunet II:2 lost head control and the ability to sit by 15 years |
| Behavioural abnormality | 31/35 (89%) | — | |
| Stereotypies | 21/31 (68%) | HP:0000733 Motor stereotypy | |
| Aggressive behaviour | 17/21 (81%) | HP:0000718 Aggressive behavior | Self-injury in both Brunet siblings: HP:0100716 Self-injurious behavior |
| Autistic features | 9/25 (36%) | HP:0000729 Autistic behavior | |
| Sleep difficulties | 12/15 (80%) | HP:0002360 Sleep disturbance | Matches the fly sleep phenotype |
| Dystonia | 8/27 (30%) | HP:0001332 Dystonia | |
| Tremor | 6/27 (22%) | HP:0001337 Tremor | |
| Strabismus | 9/21 (43%) | HP:0000486 Strabismus; HP:0000577 Exotropia | Brunet: "Strabismus divergens" |
| Nystagmus | 7/28 (25%) | HP:0000639 Nystagmus; HP:0000666 Horizontal nystagmus | |
| Optic atrophy / optic nerve thinning | 5/15 MRI (33%) | HP:0000648 Optic atrophy | |
| Myopia | Reported (OMIM summary) | HP:0000545 Myopia | No frequency available |
| Dysmorphic features | ~90%, no recognisable gestalt | HP:0000316 Hypertelorism; HP:0000431 Wide nasal bridge; HP:0045075 Sparse eyebrow; HP:0012471 Thick vermilion border (full lips) | Facial features are nonspecific |

**MRI findings** (15 scans reviewed in PMID:39692517):

| Finding | Frequency | HPO term |
|---|---|---|
| Thin corpus callosum | 11/15 (73%) | HP:0033725 |
| White-matter signal abnormality | 9/15 (60%) | HP:0002500 |
| Cerebellar atrophy | 7/15 (47%) | HP:0001272 |
| Cerebral atrophy with an anteroposterior gradient (the most frequent finding) | — | HP:0002059 |
| Skull hyperostosis (Brunet siblings) | — | HP:0002684 Thickened calvaria |

- **Onset:** neonatal or infantile (hypotonia and delay).
- **Course:** static-to-progressive. Microcephaly progresses after birth, and a minority regress, often around the time seizures start.
- **Severity:** severe; patients are lifelong dependent.
- **Quality of life:** no formal measures have been reported. Patients are fully dependent. The Brunet siblings "did not receive any special education and were cared for at home."
- **Non-neurological finding:** one child had orbital nodular fasciitis at age 6 (PMID:35487417). The authors raised a possible tumour link, but no malignancy has been reported across the cohorts. Samra et al. likewise reported none.

## 4. Genetics and molecular findings

- **Gene:** *RBL2* (RB transcriptional corepressor-like 2; p130), 16q12.2, 22 exons, NM_005611.3. HGNC: `hgnc:9894`, not yet verified (see the note at the top).
- **gnomAD constraint:** "ratio observed/expected count of LoF variants in RBL2 = 0.15 (90% CI: 0.09–0.27)", with no homozygous null variants in gnomAD (PMID:32105419).
- **Variant spectrum** (20 variants in total after Aughey et al.):
  - Types: nonsense 5, frameshift 6, splice 7, large deletions 2.
  - ACMG classification: 6 pathogenic, 13 likely pathogenic, 1 VUS.
  - Zygosity: 31 patients homozygous, 4 compound heterozygous.
- **Specific variants:**
  - **c.556C>T p.(Arg186Ter)** in exon 3. Maternal allele in the Brunet family, CADD 37, absent from gnomAD.
  - **Deletion of exons 13–17** (≥5.479 kb, chr16:53499350–53504833 on hg19). Paternal allele in the Brunet family. It is in-frame and removes 335 amino acids (residues 567–901) of the pocket domain.
  - Further variants named in Aughey et al.: c.1510G>T, c.1179+1G>A, c.1179+1_1179+5del, c.2717A>G, c.2703+1G>A.
  - c.901dupT, a frameshift (Rips et al.).
  - **Splicing confirmed by RT-PCR:** c.2717A>G causes exon skipping, and c.1179+1G>A causes a 41-bp exon extension.
- **Origin:** germline. All variants are inherited from heterozygous carrier parents, who are unaffected.
- **Functional consequence:** loss of function (most alleles are predicted to undergo nonsense-mediated decay). Aughey et al. note that it is unclear whether every allele is completely null.
- **Modifiers:** none identified. Variable microcephaly may reflect genetic background (Aughey et al.).
- **Epigenetics:** Samra et al. found no change in DNMT expression, in genome-wide DNA methylation (including pericentromeric repeats and subtelomeres), or in telomere maintenance (no ALT-like telomeric recombination) in RBL2-null fibroblasts. These were hypotheses carried over from mouse p130/p107 studies, and the result is a negative one (PMID:33980986).
- **Founder variants:** none reported. The high consanguinity points to recurrence within families rather than founder alleles.
- **Chromosomal abnormalities:** not applicable, apart from intragenic multi-exon deletions. CNV calling (for example ExomeDepth) is needed to detect these.

## 5. Environmental factors

None known. There are no environmental, lifestyle or infectious causes.

## 6. Mechanism and pathophysiology

**Ordered causal chain**

1. **Biallelic *RBL2* pLOF variants** (nonsense, frameshift, splice, multi-exon deletion) cause **loss of p130 protein**, by nonsense-mediated decay or by deletion of the pocket domain. *Partly demonstrated:* RT-PCR confirmed aberrant splicing; protein loss is inferred.
2. **Loss of p130** removes the main pocket-protein repressor of **E2F4**. In neurons this leads to **de-repression of E2F target genes (cell-cycle genes)**. p130 recruits chromatin modifiers (HDAC, SUV39H1) to E2F sites. *Demonstrated in rodent neurons:* Liu et al. 2005, *Genes Dev*, PMID:15769944, "Regulation of neuron survival and death by p130 and associated chromatin modifiers." *Inferred in patients:* no transcriptome data from patients exist.
3. **The pathway then branches:**
   - **3a. Developmental branch.** Cell-cycle dysregulation in neural progenitors (p130 is enriched in basal progenitors) leads to **apoptosis of neuronal precursors and reduced neurogenesis**, which results in **microcephaly, a thin corpus callosum and global delay**.
     - *Model evidence:* *Rbf* mutant flies have smaller optic lobes and more apoptotic (DCP1+) cells in the larval brain (PMID:39692517). p130−/− mice show impaired neurogenesis and extensive apoptosis in the neural tube and brain (LeCouter et al. 1998, *Development*, PMID:9806916).
   - **3b. Maintenance branch.** In **post-mitotic neurons**, ongoing p130 loss leads to **aberrant re-expression of cell-cycle genes**, disturbed neuronal function and excitability, and eventually **neuronal death**. This results in **progressive microcephaly, cerebral and cerebellar atrophy, optic atrophy and regression**.
     - *Evidence:* p130 or E2F4 knockdown kills cortical neurons (PMID:15769944). In flies, neuron-specific knockdown in adults causes locomotor defects, and re-expressing *Rbf* in adult neurons rescues them. The authors wrote that "continued Rbf expression is also required in fully differentiated post-mitotic neurons." A neurodegenerative mechanism in humans is *inferred* from imaging and clinical course.
4. **Neuronal dysfunction** (glutamatergic neurons were most sensitive in flies) leads to **hypotonia, motor impairment, dystonia or tremor, sleep and circadian disruption, and seizures**. *Fly evidence:* reduced activity, impaired climbing, loss of evening anticipation, reduced night sleep. The human correlation is inferred.
5. **Seizures may accelerate neuronal loss**, which would explain regression. This is *speculative* (PMID:32105419).

**Supporting detail**
- **Pathway:** RB/E2F cell-cycle control (KEGG hsa04110 "Cell cycle"; Reactome "G0 and Early G1", where the DREAM complex contains p130/E2F4). It is also a component of the **DREAM complex** (DP, RB-like, E2F4 and MuvB), which represses cell-cycle genes in quiescent cells.
- **GO process terms** (verified in cache):

  | Term | Role in the chain |
  |---|---|
  | GO:0045786 negative regulation of cell cycle | Lost function |
  | GO:0000122 negative regulation of transcription by RNA polymerase II | p130 corepressor function |
  | GO:0022008 neurogenesis | Impaired |
  | GO:0048666 neuron development | Impaired |
  | GO:0051402 neuron apoptotic process | Increased |
  | GO:0043523 regulation of neuron apoptotic process | Regulatory term |
  | GO:0021987 cerebral cortex development | Affected |
  | GO:0007049 cell cycle | General term |

- **CL cell-type terms** (verified in cache):

  | Term | Role |
  |---|---|
  | CL:0011020 neural progenitor cell | Developmental branch |
  | CL:0000047 neural stem cell | Developmental branch |
  | CL:0000117 CNS neuron (sensu Vertebrata) | Maintenance branch |
  | CL:0000540 neuron | General term |

- **Protein:** a pocket protein with A-box, spacer and B-box (small pocket) plus a C-terminal domain. The deletion of exons 13–17 removes much of the pocket domain, and the pocket domain is what binds E2F.
- **Not involved:** the immune system, metabolism, DNA methylation, and telomeres (the last two tested negative, PMID:33980986).
- **Omics:** no patient transcriptomics, proteomics or single-cell data have been published. This is a knowledge gap.

## 7. Anatomical structures affected

- **Primary:** the central nervous system:
  - cerebral cortex and white matter
  - corpus callosum
  - cerebellum
  - optic nerve
- **Secondary:** eye (strabismus, nystagmus, myopia) and skull (hyperostosis in the Brunet siblings).
- **Suggested UBERON terms** (not verified in cache): brain UBERON:0000955; cerebral cortex UBERON:0000956; corpus callosum UBERON:0002336; cerebellum UBERON:0002037; optic nerve UBERON:0000941.
- **Cells:** neural progenitors and post-mitotic neurons; glutamatergic neurons were most sensitive in the fly.
- **Subcellular:** nucleus (p130/E2F4 repressive complexes on chromatin). Suggested term: GO:0005634 nucleus (not checked).
- **Laterality:** bilateral and diffuse.

## 8. Temporal development

- **Onset:** congenital or neonatal hypotonia. Delay is evident in infancy. Birth measurements are normal and microcephaly develops after birth.
- **Course:** chronic and lifelong.
  - Progressive in some patients: postnatal microcephaly, atrophy, regression in 17%.
  - Regression in Brunet II:2 began with seizure onset at age 10 and worsened after pneumonia at 15.
- **Remission:** none.
- **Critical period:** the fly data suggest that function in mature neurons can be restored even after development is complete. This raises the possibility of a postnatal therapeutic window, which is untested in humans.

## 9. Inheritance and population

- **Inheritance:** autosomal recessive (HP:0000007 Autosomal recessive inheritance). Penetrance appears complete in biallelic carriers. Expressivity varies within and between families (in the Brunet family only the brother had seizures, optic atrophy and a thin corpus callosum). There is no anticipation, and germline mosaicism has not been reported.
- **Prevalence:** ultra-rare. About 41 published patients (6 before 2024, then 35 more). ERN ITHACA has reported more than 15 further families with biallelic LoF variants in its collaboration call.
- **Minimal birth incidence:** about 1 in 13.2 million in outbred populations (PMID:32105419). Mapped to dismech's structured fields: `measure_type: BIRTH_PREVALENCE`, `prevalence_class: BELOW_1_IN_1000000`; the count of published patients would be a separate `CASES_IN_LITERATURE` record.
- **Demographics:** sex ratio about 1:1 (17 female, 18 male). Strongly enriched in consanguineous families (85%). The cohorts include European (German, Norwegian) and Middle Eastern (Israeli Arab and others) families.
- **Carrier frequency:** the summed LoF allele frequency is about 0.027%.

## 10. Diagnostics

- **Approach:** exome or genome sequencing in a child with severe global delay, hypotonia, microcephaly and absent speech.
  - Include CNV analysis. The deletion of exons 13–17 was found by ExomeDepth.
  - Use RNA studies or RT-PCR for splice variants.
  - Chromosomal microarray may miss small intragenic deletions.
- **Supportive tests:**
  - Brain MRI: thin corpus callosum, cerebral and cerebellar atrophy, white-matter changes, optic nerve thinning.
  - EEG: background slowing and spikes in patients with seizures.
  - Eye examination.
- **Biomarkers:** none. Methylation episignatures and telomere testing are not informative (PMID:33980986).
- **Differential diagnosis:** other recessive severe intellectual-disability and progressive-microcephaly disorders, and Rett-like phenotypes with stereotypies and absent speech (MECP2, FOXG1, CDKL5). Pontocerebellar or neurodegenerative leukoencephalopathies should also be considered.
- **Screening:** none at population level. Carrier, prenatal or preimplantation testing is possible once the familial variants are known.

## 11. Prognosis

- **Survival:** the oldest reported patient was 36. No formal survival or mortality data exist.
- **Function:** lifelong severe disability. Most patients are non-ambulatory and non-verbal.
- **Complications:** drug-resistant epilepsy (2 patients in the Aughey cohort; Brunet II:2), and regression after intercurrent illness (pneumonia in Brunet II:2). One patient had an orbital fasciitis mass.
- **Prognostic factors:** seizure onset may mark the start of a decline (single observation). Otherwise none are known.

## 12. Treatment

No disease-modifying therapy exists. Management is supportive.

| Treatment | Evidence | Suggested NCIT term |
|---|---|---|
| Antiseizure medication (valproate, levetiracetam) | Seizures controlled in many patients; 2 intractable (PMID:39692517) | NCIT:C15986 Pharmacotherapy, plus `therapeutic_agent` (CHEBI terms for valproic acid and levetiracetam; look them up before binding) |
| Physical, occupational and speech therapy | Standard care for intellectual disability and hypotonia | NCIT:C15302 Physical Therapy; NCIT:C121351 Occupational Therapy; NCIT:C159273 Speech Language Therapy |
| Supportive care (feeding, sleep, behaviour) | Standard | NCIT:C15747 Supportive Care |
| Genetic counselling | Recurrence risk 25% per pregnancy | NCIT:C15240 Genetic Counseling |
| **Gene therapy (hypothetical)** | Supported only by the *Drosophila* rescue in adult neurons. Aughey et al. suggest restoring *RBL2* in neurons; this is untested | NCIT:C15238 Gene Therapy |

The NCIT IDs above come from this repository's CLAUDE.md lists and were not re-checked against the term caches. There are no clinical trials (no NCT or ICTRP records found) and no pharmacogenomic data.

## 13. Prevention

- **Primary prevention:** carrier testing in at-risk relatives and consanguineous couples; preimplantation genetic testing or prenatal diagnosis once the familial variants are known. Consanguinity counselling is relevant given the 85% rate.
- **Tertiary prevention:** seizure control (seizures possibly drive regression), prevention of respiratory infection and aspiration, and management of orthopaedic and sleep problems.
- **Not applicable:** vaccines, public-health measures and environmental measures.

## 14. Other species

- No naturally occurring disease is recorded in OMIA (not checked exhaustively).
- **Orthologues:** mouse *Rbl2* (MGI:105085, from memory; verify before use); *Drosophila Rbf* (one orthologue covering RB1, RBL1 and RBL2).
- **Conservation:** the RB/E2F pathway is conserved from flies to humans.

## 15. Model organisms

| Model | Phenotypes | Fidelity and limitations | Reference |
|---|---|---|---|
| **Mouse *Rbl2*−/− (p130 null)** | Embryonic lethality that depends on strain (BALB/c background); growth arrest; impaired neurogenesis and myogenesis; fewer spinal motor neurons and DRG sensory neurons; extensive apoptosis in the neural tube and brain; thin myocardium | On other backgrounds (e.g. C57BL/6) mice are viable with little phenotype because p107 compensates. The heart phenotype has no human counterpart (no cardiomyopathy in patients). A likely `HUMAN_MODEL_MISMATCH` | LeCouter et al. 1998, PMID:9806916 |
| **Rat cortical neurons with p130 or E2F4 siRNA** (in vitro) | Neuronal death; p130/E2F4 recruit HDAC and SUV39H1 to repress pro-apoptotic and cell-cycle genes | Primary culture only | Liu et al. 2005, PMID:15769944 |
| ***Drosophila Rbf*** (hypomorph Rbf¹²⁰ᵃ, null Rbf¹⁴; pan-neuronal nSyb-Gal4 RNAi; tub-Gal80ts temporal control) | Smaller eyes and optic lobes; more larval apoptosis; ~1.5-day developmental delay; reduced activity and climbing; sleep and circadian defects. Glutamatergic neurons are most sensitive. Adult neuronal re-expression rescues locomotion | Partly recapitulates microcephaly (optic lobe only), motor and sleep phenotypes. *Rbf* is the single orthologue of all three RB-family genes. Adult knockdown does not cause apoptosis, so neurodegeneration is not reproduced | Aughey et al. 2025, PMID:39692517 |
| Patient fibroblasts (in vitro) | Normal methylation and telomeres | Negative result; a non-neural tissue | Samra et al. 2021, PMID:33980986 |

No iPSC or organoid models have been published. This is a gap; a neuronal model would be needed to test E2F-target de-repression in human neurons.

---

## Knowledge gaps

1. No human neuronal data show E2F-target de-repression or neuronal loss; the mechanism is inferred from rodent and fly work.
2. It is not known whether the in-frame exon 13–17 deletion and the splice alleles are complete nulls, and there is no genotype–phenotype correlation.
3. Neurodegeneration versus developmental hypoplasia: neuropathology is missing.
4. Whether *RBL2* loss raises tumour risk (one case of fasciitis, no malignancies).
5. Natural history and survival.

## Sources

- Brunet T et al. 2020. PMID:32105419. https://onlinelibrary.wiley.com/doi/full/10.1002/acn3.50992 ; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7086002/
- Samra N et al. 2021. PMID:33980986. https://www.nature.com/articles/s10038-021-00931-z
- Rips J et al. 2022. PMID:35487417. https://www.sciencedirect.com/science/article/abs/pii/S1769721222000945
- Aughey GN et al. 2025. PMID:39692517. https://pmc.ncbi.nlm.nih.gov/articles/PMC11967543/
- LeCouter JE et al. 1998. PMID:9806916
- Liu DX et al. 2005. PMID:15769944
- [OMIM 619690](https://0-www-ncbi-nlm-nih-gov.brum.beds.ac.uk/omim/619690)
- [KEGG H02613](https://www.kegg.jp/entry/H02613+-ja)
- [MedGen C5562056](https://https.ncbi.nlm.nih.gov/medgen/C5562056)
- [Disease Ontology DOID:0061126](https://disease-ontology.org/term/DOID:0061126/owl)
- [MalaCards](https://www.malacards.org/card/brunet_wagner_neurodevelopmental_syndrome)
- [ERN ITHACA call for collaboration](https://ern-ithaca.eu/for-clinicians/calls-for-collaboration/clinical-and-genetic-delineation-of-recessive-rbl2-related-neurodevelopmental-syndrome/)
- [Genomics England PanelApp: RBL2](https://nhsgms-panelapp.genomicsengland.co.uk/entities/RBL2)
- [Tel Aviv University record for Samra et al.](https://cris.tau.ac.il/en/publications/rbl2-bi-allelic-truncating-variants-cause-severe-motor-and-cognit/)
- [ResearchGate record](https://www.researchgate.net/publication/380363912_Clinical_and_neurogenetic_characterisation_of_autosomal_recessive_RBL2-associated_progressive_neurodevelopmental_disorder)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 12 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 62 |
| Resolved | 61 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 2 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0859217` (2 mentions) - the report calls it "MONDO"; MONDO calls it **Brunet-Wagner neurodevelopmental syndrome**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `DOID:0061126` (4 mentions) - the report calls it "synonym BRUWAG"; DOID calls it **Brunet-Wagner neurodevelopmental syndrome**, and lists "BRUWAG" among its other names

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `MGI`.