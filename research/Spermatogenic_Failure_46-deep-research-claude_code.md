---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-14T20:31:19.281301'
end_time: '2026-10-14T20:32:43.602874'
duration_seconds: 84.32
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Spermatogenic Failure 46
  mondo_id: MONDO:0033673
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
  - claude-sonnet-5-5
  web_search_requests: 3
  num_turns: 10
  total_cost_usd: 0.7752555999999998
  session_id: e0e00ff6-67e7-5e60-9592-3e4cb1004f09
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 11
reference_validation:
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 7
  on_topic: 6
  validator_version: 0.3.0
term_validation:
  total_terms: 4
  verified: 4
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 4
  labels_matching: 1
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0033673
    reported_labels:
    - MONDO
    ontology_label: spermatogenic failure 46
  - term_id: HP:0012206
    reported_labels:
    - Asthenozoospermia
    ontology_label: Abnormal sperm motility
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spermatogenic Failure 46
- **MONDO ID:** MONDO:0033673 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spermatogenic Failure 46** covering all of the
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

I'm pulling the abstracts of the other DNAH8 papers to get variant details and ICSI outcomes. Then I'll write the report.

# Spermatogenic Failure 46 (SPGF46; DNAH8-related MMAF): research report

**Evidence limits.** The OMIM entry returned HTTP 403, so I could not read it. Its details (phenotype description, HPO annotations, allelic variants) come from search-result snippets and PubMed abstracts. PMIDs below were confirmed through PubMed E-utilities. Quotes marked "snippet" come from search-result text, not from a PubMed record I read in full. Anything I did not find is marked "not found".

## 1. Disease information

**Overview.** SPGF46 is an autosomal recessive form of primary male infertility. It is caused by bi-allelic loss-of-function or missense variants in *DNAH8*, which encodes an axonemal outer-arm dynein heavy chain. Affected men have asthenoteratozoospermia with multiple morphological abnormalities of the sperm flagella (MMAF). The MMAF phenotype combines absent, short, coiled, angulated and irregular-caliber flagella. The defect is restricted to the sperm tail, and ICSI can bypass it.

**Identifiers**

| Item | Value | Source |
|---|---|---|
| OMIM phenotype | #619095 | [LOVD](https://databases.lovd.nl/shared/diseases/06933) |
| MONDO | MONDO:0033673 | [DrugMap](https://drugmap.idrblab.net/data/disease/details/DISU4WQ1); only one source paired it with this disease, so check it in MONDO |
| MedGen | 1726728 | DrugMap |
| Gene | *DNAH8* (OMIM gene 603337, 6p21.2) | OMIM-based gene table in search results |
| Orphanet, ICD-10/11, MeSH | Not found | |

**Synonyms.** SPGF46; spermatogenic failure, type 46; DNAH8-related MMAF; MMAF with *DNAH8* variants.

**Data source.** The case reports are individual patients (exome sequencing plus semen and EM analysis). The OMIM, MONDO and LOVD entries are aggregated disease-level resources.

## 2. Etiology

- **Cause.** Bi-allelic *DNAH8* variants. The discovery paper reported that "Two cases (2.2%) were identified as carrying bi-allelic missense DNAH8 variants" among 90 Chinese MMAF men (snippet, [PMID:32619401](https://pubmed.ncbi.nlm.nih.gov/32619401/), Liu et al., Am J Hum Genet 2020). It also found a homozygous frameshift in a second cohort of 167 men from France, Iran and North Africa.
- **Gene-disease validity.** DrugMap lists *DNAH8* as "Strong" with autosomal recessive inheritance. The source of that tier is not stated; the label is consistent with a ClinGen-style classification. Check ClinGen directly before recording a `gene_disease_validity` entry. It must be copied from a source record and not assigned.
- **Risk and protective factors.** None identified. No modifier genes, gene-environment interactions or protective variants were found for male infertility. A 2026 paper links *DNAH8* dysfunction and DEHP exposure to hypospadias ([PMID:42480140](https://pubmed.ncbi.nlm.nih.gov/42480140/)). I read only its title, so I make no claim about its content. It concerns a different phenotype and should not be merged into SPGF46.

## 3. Phenotypes

All phenotypes below are male-limited and restricted to the reproductive system. Frequencies are not quantified in the sources I read. Every patient described had the sperm phenotype.

| Phenotype | HPO (verify by lookup before binding) | Notes |
|---|---|---|
| Male infertility | HP:0003251 | Primary; present at reproductive age |
| Asthenozoospermia | HP:0012206 | Reduced motility ([PMID:32681648](https://pubmed.ncbi.nlm.nih.gov/32681648/), [PMID:33611675](https://pubmed.ncbi.nlm.nih.gov/33611675/)) |
| Teratozoospermia / MMAF | HP:0012864 (teratozoospermia) | Flagella absent, short, coiled, angulated or irregular caliber |
| Abnormal sperm flagellum ultrastructure | Likely a child of HP:0012206 or HP:0012864; look up | Disorganized axoneme and periaxonemal structures on EM |

- There is no consistent respiratory, laterality or other ciliary phenotype in the reports I read. *DNAH8* was initially proposed as a candidate primary ciliary dyskinesia gene, but later studies showed MMAF in infertile men (snippet from the follow-up abstract).
- Quality-of-life data were not found.
- HPO term IDs above are from memory. Per the project rules, confirm each one with a lookup before binding it.

## 4. Genetic and molecular information

- **Gene.** *DNAH8*, 6p21.2, encoding dynein axonemal heavy chain 8. Confirm the HGNC ID by lookup, in the lowercase `hgnc:` form. I did not retrieve it.
- **Inheritance.** Autosomal recessive.
- **Reported variants** (from the abstracts I read):

| Variant | Type | Zygosity | Source |
|---|---|---|---|
| c.6311-2A>G (predicted p.G2104Efs*19, exon 45 skipping) | Splice acceptor | Homozygous, two brothers, consanguineous family | [PMID:33611675](https://pubmed.ncbi.nlm.nih.gov/33611675/) |
| c.6158_6159insT | Frameshift | Homozygous, two brothers, consanguineous Pakistani family | [PMID:36308074](https://pubmed.ncbi.nlm.nih.gov/36308074/) |
| Two missense variants (HGVS not in the abstract) | Missense | Bi-allelic, 2 of 90 Chinese men | [PMID:32619401](https://pubmed.ncbi.nlm.nih.gov/32619401/) |
| Homozygous frameshift (HGVS not in the abstract) | Frameshift | Homozygous, 1 of 167 men | [PMID:32619401](https://pubmed.ncbi.nlm.nih.gov/32619401/) |
| Compound heterozygous (HGVS not in the abstract) | Not specified | Two patients | [PMID:33704367](https://pubmed.ncbi.nlm.nih.gov/33704367/) |
| Loss-of-function (HGVS not in the abstract) | Not specified | One patient | [PMID:32681648](https://pubmed.ncbi.nlm.nih.gov/32681648/) |

- **Consequence.** Loss of function. mRNA decay was shown for the frameshift in [PMID:36308074](https://pubmed.ncbi.nlm.nih.gov/36308074/), and DNAH8 protein is absent or reduced in patient sperm.
- **Not found.** ClinVar classifications, gnomAD allele frequencies, epigenetic data, chromosomal abnormalities. This is a germline monogenic disorder.

## 5. Environmental information

No environmental, lifestyle or infectious causes are established for SPGF46. The DEHP/hypospadias paper above is outside this phenotype.

## 6. Mechanism and pathophysiology

**Causal chain**

1. Bi-allelic loss-of-function or missense variants in *DNAH8* are the initiating lesion (demonstrated, [PMID:32619401](https://pubmed.ncbi.nlm.nih.gov/32619401/)).
2. These lead to reduced or absent DNAH8 protein in the sperm flagellum. The evidence is immunofluorescence plus mRNA decay (demonstrated, [PMID:36308074](https://pubmed.ncbi.nlm.nih.gov/36308074/), [PMID:33704367](https://pubmed.ncbi.nlm.nih.gov/33704367/)).
3. Loss of DNAH8 also reduces DNAH17, an associated dynein heavy chain, in sperm. This points to destabilization of outer dynein arm components (demonstrated for the association, per the discovery abstract; the exact mechanism is inferred).
4. Axonemal and periaxonemal organization is disrupted during spermiogenesis, producing MMAF flagella (demonstrated by EM).
5. Sperm motility is lost, which causes asthenoteratozoospermia and male infertility.

**Branching.** There is no demonstrated branch. Whether DNAH8 loss also affects motile cilia is unresolved. The reports show no strong ciliary phenotype.

**Ontology suggestions (look up before binding).** GO: axonemal dynein complex / outer dynein arm; sperm flagellum assembly; sperm axoneme assembly. CL: spermatid, spermatozoon. Uberon: testis, sperm flagellum.

**Omics, single-cell and functional screens.** Not found.

## 7. Anatomical structures affected

- **Organ.** Testis and male reproductive tract. Spermatogenesis proceeds, but the sperm are defective.
- **Cells.** Late spermatids and spermatozoa.
- **Subcellular.** Sperm flagellum axoneme, outer dynein arms, periaxonemal structures.
- **Lateralization.** Not applicable (bilateral germ-cell phenotype).

## 8. Temporal development

- **Onset.** Presents in adulthood as infertility. Congenital cause, with no childhood manifestations reported.
- **Progression.** Not described as progressive. Longitudinal data were not found.
- **Remission.** None reported.

## 9. Inheritance and population

- **Inheritance.** Autosomal recessive. Both homozygous variants (in consanguineous families) and compound heterozygous variants are reported.
- **Consanguinity.** Two of the reported families were consanguineous ([PMID:33611675](https://pubmed.ncbi.nlm.nih.gov/33611675/), [PMID:36308074](https://pubmed.ncbi.nlm.nih.gov/36308074/)).
- **Population.** Chinese, Pakistani and North African/Iranian/French cohorts. About 2.2% of the Chinese MMAF cohort carried bi-allelic missense variants. Prevalence, carrier frequency, founder effects and the share of MMAF explained by *DNAH8* were not established in what I read.
- **Sex.** Males only.

## 10. Diagnostics

- **Semen analysis.** Asthenoteratozoospermia with an MMAF pattern.
- **Electron microscopy.** Disorganized axoneme and periaxonemal structures.
- **Immunofluorescence.** Absent or reduced DNAH8 and DNAH17 in sperm.
- **Genetic testing.** Exome sequencing found the variants in the cohort studies. A male-infertility or MMAF gene panel that includes *DNAH8*, or targeted sequencing, would be the practical approach. Specific panels and GTR listings were not retrieved.
- **Differential diagnosis.** Other MMAF genes (the search results name *DNAH2*, *DNAH6*, *DNAH11* and *CFAP61*) and primary ciliary dyskinesia.
- **Screening.** None.

## 11. Prognosis

Fertility is not spontaneously restored. The disorder appears to cause no systemic disease in the reports I read, but long-term follow-up data were not found.

## 12. Treatment

- **ICSI works.** [PMID:33611675](https://pubmed.ncbi.nlm.nih.gov/33611675/) reports that ICSI produced a healthy child for the proband. [PMID:33704367](https://pubmed.ncbi.nlm.nih.gov/33704367/) reports a clinical pregnancy with ICSI. Per the discovery abstract, ICSI with sperm from *Dnah8*-knockout mice "resulted in good pregnancy outcomes".
- **Suggested NCIT terms (verify by lookup):** assisted reproductive technology / intracytoplasmic sperm injection. Choose the most specific NCIT term under the clinical-intervention root, and if none fits, keep a free-text `preferred_term`.
- **Not found.** Drug therapy, gene therapy, clinical trials, pharmacogenomics. No evidence-based medical therapy exists in what I read.
- **Counseling.** Genetic counseling is appropriate. This is my inference from recessive inheritance and not a cited guideline.

## 13. Prevention

There is no primary prevention. Genetic counseling and carrier testing in relatives of known families are the relevant measures, again as inference. I found no guideline source.

## 14. Other species

Not found: OMIA entries, breeds, NCBI Taxon or Gene IDs for natural disease in other species.

## 15. Model organisms

- **Mouse.** The *Dnah8* knockout shows MMAF and male sterility, and ICSI with its sperm gives good pregnancy outcomes ([PMID:32619401](https://pubmed.ncbi.nlm.nih.gov/32619401/), MODEL_ORGANISM evidence). It closely recapitulates the human sperm phenotype.
- **Limitations.** I did not retrieve the knockout design, MGI or IMPC records, or any data on non-reproductive phenotypes.
- **A caution for evidence grading.** The mouse ICSI result is model-organism evidence. It should not be used as the only support for the human ICSI claim, which has its own human reports above.

## Open items before curation

- Look up HGNC, HPO, GO, CL and NCIT identifiers. I recalled the HPO IDs above from memory.
- Fetch the references with `just fetch-reference` and quote snippets from the cache. The snippets in this report come from search-result text, and I did not read the abstracts verbatim.
- Check MONDO:0033673 directly in MONDO.
- Check the ClinGen validity record for *DNAH8*.

Sources:
- [LOVD disease entry SPGF46](https://databases.lovd.nl/shared/diseases/06933)
- [DrugMap disease record](https://drugmap.idrblab.net/data/disease/details/DISU4WQ1)
- [Liu et al. 2020, AJHG (PMID 32619401)](https://www.cell.com/ajhg/fulltext/S0002-9297(20)30192-0)
- [Weng et al. 2021 (PMID 33704367)](https://academic.oup.com/abbs/article/53/4/472/6168168)
- [Dil et al. 2023 (PMID 36308074)](https://doi.org/10.4103/aja202274)
- [Yang et al. 2020 (PMID 32681648)](https://pubmed.ncbi.nlm.nih.gov/32681648/)
- [Zhou et al. 2021 (PMID 33611675)](https://pubmed.ncbi.nlm.nih.gov/33611675/)
- [Li et al. 2026 (PMID 42480140)](https://pubmed.ncbi.nlm.nih.gov/42480140/)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 7 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 4 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0033673` (2 mentions) - the report calls it "MONDO"; MONDO calls it **spermatogenic failure 46**
- `HP:0012206` (2 mentions) - the report calls it "Asthenozoospermia"; HP calls it **Abnormal sperm motility**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0012864` (2 mentions) - the report calls it "teratozoospermia"; HP calls it **Abnormal sperm morphology**, and lists "Teratozoospermia" among its other names