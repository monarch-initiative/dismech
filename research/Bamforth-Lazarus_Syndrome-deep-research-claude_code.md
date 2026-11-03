---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-02T00:04:33.517970'
end_time: '2026-11-02T00:11:06.123193'
duration_seconds: 392.61
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Bamforth-Lazarus Syndrome
  mondo_id: MONDO:0009437
  category: Mendelian
  causal_genes: FOXE1
  omim_id: OMIM:241850
  synonyms: Athyroidal hypothyroidism-spiky hair-cleft palate syndrome; Bamforth syndrome;
    hypothyroidism-cleft palate syndrome
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
  num_turns: 26
  total_cost_usd: 2.6316243000000004
  session_id: 2ccff955-20d8-5bb4-8e86-b52d55e2a947
  stop_reason: end_turn
  permission_denials: 5
  denied_tools:
  - Bash
  assistant_text_blocks: 4
citation_count: 13
reference_validation:
  total_references: 28
  verified: 28
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 11
  quotes_valid: 8
  quotes_unsupported: 3
  unsupported_quote_references:
  - PMID:2918525
  - PMID:39360443
  - PMID:36156081
  relevance_assessed: 28
  on_topic: 17
  needs_review: true
  validator_version: 0.4.0
term_validation:
  total_terms: 31
  verified: 29
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 2
  unresolvable_prefixes:
  - ORPHA
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Bamforth-Lazarus Syndrome
- **MONDO ID:** MONDO:0009437 (if available)
- **Causal gene(s):** FOXE1
- **OMIM:** OMIM:241850
- **Synonyms:** Athyroidal hypothyroidism-spiky hair-cleft palate syndrome; Bamforth syndrome; hypothyroidism-cleft palate syndrome
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Bamforth-Lazarus Syndrome** covering all of the
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

Querying PubMed through NCBI's E-utilities to pin down FOXE1/Bamforth-Lazarus citations.

Still pulling primary citations (mouse model, original 1989 report, recent cases) before writing the report.

Checking a few remaining HPO labels (spiky hair, bifid epiglottis, ectopic thyroid) in the local cache, then writing the report.

# Bamforth-Lazarus Syndrome (MONDO:0009437; OMIM #241850): research report

## How this report was built

- **Sources:** Primary-literature metadata and abstract sentences came from the Europe PMC REST API. The R73S paper (PMID:24219130) was read in full text on PMC.
- **Blocked or unread sources:** PubMed's web pages, OMIM and one Springer page refused automated access. Anything I report from them comes from search-result summaries and is marked unverified.
- **Ontology terms:** Every term marked "(cache-verified)" was checked against the repository's `cache/<prefix>/terms.csv`. Terms marked "(lookup required)" were *not* found in a source. Look them up before binding them.
- **Existing KB entry:** `kb/disorders/Bamforth-Lazarus_Syndrome.yaml` already exists. It is a 51-line skeleton binding MONDO:0009437, hgnc:3806, HP:0000851, HP:0000175 and HP:0000007, with no evidence. `stubs/Bamforth-Lazarus_Syndrome.yaml` is also still present, at priority HIGH.
- **Quotes:** Text in quotation marks is taken from Europe PMC abstract text. Before using any quote as a `snippet:`, check it with `just fetch-reference` and `just count-verified-snippets`.

---

## 1. Disease information

**Overview.** Bamforth-Lazarus syndrome (BLS) is a rare autosomal recessive syndromic form of primary congenital hypothyroidism. It is caused by **biallelic variants in *FOXE1*** (forkhead box E1, also called TTF-2, TITF2 or FKHL15; HGNC:3806, written `hgnc:3806` in this repository; chromosome 9q22.33).

- **Defining features:**
  - congenital hypothyroidism from thyroid dysgenesis, usually athyreosis
  - cleft palate
  - "spiky" (stiff, upright) scalp hair
  - variably, bilateral choanal atresia and bifid epiglottis
- **First description:** Bamforth et al. in 1989 described "Two brothers … with athyroidal hypothyroidism, spiky hair, choanal atresia, cleft palate, and bifid epiglottis" (PMID:2918525, *J Med Genet* 1989).
- **Molecular basis:** established in 1998 by Clifton-Bligh et al. (PMID:9697705). In the same issue of *Nat Genet*, De Felice et al. described the *Titf2*-null mouse (PMID:9697704).

**Identifiers**

| Resource | ID | Status |
|---|---|---|
| MONDO | MONDO:0009437 "Bamforth-Lazarus syndrome" | verified (stub/KB) |
| OMIM (phenotype) | #241850 BAMLAZ | given; OMIM page not reachable |
| OMIM (gene) | *602617 FOXE1 | search result |
| HGNC | hgnc:3806 FOXE1 | verified (repo cache / ClinGen row "HGNC:3806") |
| ClinGen GDV | FOXE1–BLS, **Definitive, AR**, Craniofacial Malformations GCEP, 2024-05-16; CGGV:assertion_0a00a763-90dc-4d36-8b34-54cf4f477269-2024-05-16T160000.000Z | verified in `cache/clingen/gene_validity.csv` |
| Orphanet | ORPHA:1226 is the commonly cited code | **unverified**; no ORPHA cache file matched "bamforth"; confirm with `just fetch-reference ORPHA:1226` |
| ICD-10 | falls under E03.1 (congenital hypothyroidism without goitre); no specific code | inference |
| MeSH | no dedicated descriptor known; possibly a Supplementary Concept | unverified |

**Synonyms:** Bamforth syndrome; athyroidal hypothyroidism–spiky hair–cleft palate syndrome; hypothyroidism–cleft palate syndrome; "thyroid agenesis, cleft palate and choanal atresia" (from the 1998 paper title). The literature also uses "syndromic congenital hypothyroidism due to FOXE1/TTF-2 mutation".

**Kind of data.** All knowledge comes from individual case reports and small family studies: about a dozen probands in total. There is no registry or EHR cohort. Sarma et al. (2022) state that "To date, seven pathogenic variants have been reported in the FOXE1 gene causing Bamforth-Lazarus syndrome" (PMID:35963604).

---

## 2. Etiology

- **Cause:** Biallelic pathogenic *FOXE1* variants. Most are missense changes in the forkhead DNA-binding domain; one is a frameshift. Sarma 2022 states the disease is "caused by biallelic loss-of-function variants in the FOXE1 gene" (PMID:35963604).
- **Genetic risk factors:**
  - **Consanguinity.** Most probands are born to consanguineous parents: Egyptian first cousins in Carré 2014, a consanguineous family in Castanet 2002, a Turkish family in Baris 2006.
  - **Uniparental isodisomy.** One case became homozygous through **maternal isodisomy of chromosome 9**. In that family the father was wild type (PMID:20484477).
- **Modifiers and susceptibility (not BLS itself):**
  - *FOXE1 polyalanine-tract length.* Most alleles carry 14 or 16 alanines.
    - Carré 2007 found that "the presence of 16 alanines in the tract protect against the occurrence of TD" (thyroid dysgenesis) (PMID:17717707).
    - Grassi 2023 found that "The CH group with thyroid dysgenesis was largely and significantly enriched with the 14-Alanine-FOXE1 homozygosity" (PMID:37008944).
    - These findings concern non-syndromic thyroid dysgenesis. Their effect within BLS families has not been studied.
  - *Common FOXE1 variants* are associated with non-syndromic orofacial clefting: "FOXE1 is a major gene for CL/P" (PMID:19779022). The 9q22.33 locus near FOXE1 is also associated with papillary and follicular thyroid cancer (PMID:19198613). Both are separate phenotypes, not BLS.
- **Environmental and protective factors:** None are documented for BLS. The cause is monogenic and fully genetic.
- **Gene–environment interaction (model organism only):** *foxe1* mutant zebrafish showed "increased sensitivity to ethanol for craniofacial malformations" (PMID:39360443). This has not been shown in humans.

---

## 3. Phenotypes

Frequencies are approximate counts across about 10 published molecularly confirmed probands and sibships:

- Clifton-Bligh 1998: 2 siblings
- Castanet 2002: 2 siblings
- Baris 2006: 1 proband
- Castanet 2010: 1 proband
- Carré 2014: 1 proband
- Sarma 2022: 1 proband
- Al-Araimi preprint: 2 siblings
- the original Bamforth 1989 brothers, not genotyped

Sample sizes are too small for reliable percentages.

| Phenotype | Type / onset | Frequency (approx.) | Suggested HPO |
|---|---|---|---|
| Congenital primary hypothyroidism (TSH >100 µU/mL, undetectable T4 in the R73S case) | lab/clinical, neonatal | essentially all | HP:0000851 Congenital hypothyroidism (cache-verified) |
| Thyroid agenesis/athyreosis (no gland on ultrasound or scintigraphy) | anatomical, congenital | most; **not** universal (R102C: "congenital hypothyroidism but not athyreosis", PMID:16882747) | HP:0008191 Thyroid agenesis (cache-verified) |
| Cleft palate | congenital malformation | nearly all | HP:0000175 Cleft palate (cache-verified) |
| Spiky/stiff, upright scalp hair | ectodermal | frequent (Bamforth 1989; Baris 2006; Sarma 2022 "scalp hair abnormalities") | No specific "spiky hair" term found in cache. The coarse fallback is HP:0001595 Abnormal hair morphology (cache-verified), which needs a `coarse_binding_basis`. HP:0002208 Coarse hair (cache-verified) is a possible narrower option. Search HPO for "spiky". (lookup required) |
| Choanal atresia, bilateral or partial | congenital | about half (1989 brothers; A65V sibs; R102C "bilateral choanal atresia"; R73S "partial choanal atresia") | HP:0000453 Choanal atresia (cache-verified) |
| Bifid epiglottis | congenital | a minority (1989 brothers; reviews list it as variable) | (lookup required) |
| Neonatal hypothyroid signs: excessive sleepiness, poor feeding, prolonged jaundice | symptom, first month | common if screening is delayed | HP:0001508 Failure to thrive (cache-verified) for poor growth; jaundice term (lookup required) |
| Neurodevelopmental delay, if treatment starts late | outcome | variable; treatment-dependent | HP:0001263 Global developmental delay (cache-verified) |
| Expanded phenotype in the frameshift case: small areolae, café-au-lait spots, mild bilateral hearing loss, skin abnormalities, facial dysmorphism; Sarma also describes a phenotype that changes with age | single case | 1 case | HP:0000957 Cafe-au-lait spot; HP:0000365 Hearing impairment (both cache-verified) |

- **Severity and progression:** The hypothyroidism is severe and permanent. The craniofacial malformations are present at birth and do not progress.
- **Quality of life:** No QoL instruments have been applied to BLS. The burden comes from:
  - lifelong levothyroxine therapy
  - palate repair, with risks of speech and feeding problems
  - airway compromise from choanal atresia in the neonatal period
- **Two clinical points:**
  - In the R73S case, cleft palate and choanal atresia were seen at birth, but hypothyroid symptoms appeared at one month.
  - A cleft palate with thyroid dysgenesis should therefore prompt FOXE1 testing.

---

## 4. Genetic and molecular information

**Gene.** *FOXE1*: a single-exon gene encoding a forkhead/winged-helix transcription factor of 373 amino acids, with a variable polyalanine tract after the forkhead domain.

**Protein function (GO suggestions, cache-verified):**
- GO:0003700 DNA-binding transcription factor activity
- GO:0000978 RNA polymerase II cis-regulatory region sequence-specific DNA binding
- GO:0006357 regulation of transcription by RNA polymerase II

Reported BLS variants (all homozygous; RefSeq NM_004473):

| Variant | Domain | Population / setting | Functional effect | PMID |
|---|---|---|---|---|
| p.Ala65Val (A65V) | forkhead | 2 sibs (UK report) | "impaired DNA binding and loss of transcriptional function" | 9697705 |
| p.Ser57Asn (S57N) | forkhead | 2 sibs, consanguineous | "impaired DNA binding and partial loss of transcriptional function" | 12165566 |
| p.Arg102Cys (R102C) | forkhead | Turkish girl; gland present (no athyreosis) | "loss of DNA binding and was transcriptionally inactive" | 16882747 |
| c.412T>C p.Phe137Ser (F137S) | forkhead | maternal UPD9 | "failed to bind DNA and showed negligible transcriptional activity" | 20484477 |
| c.217C>A p.Arg73Ser (R73S) | forkhead | Egyptian, first-cousin parents | **increased** TG/TPO promoter activity (1.7–2.2×) with normal DNA binding; **gain of function** | 24219130 |
| c.141dupC p.(Leu49Profs*75) | truncating, before the forkhead domain | Indian proband | predicted loss of function | 35963604 |
| p.Phe89Leu (F89L) | forkhead | 2 Omani siblings | in silico only | Al-Araimi et al., Research Square preprint (2025) and a 2026 Springer article (doi:10.1007/s40142-026-00256-3); **not verified**, no PMID found |

Variants that are **not** BLS but are relevant:

- **Kang 2010 (PMID:20094846):** one heterozygous forkhead variant in a Malaysian thyroid-dysgenesis cohort, with slightly reduced activity.
- **Grassi 2023 (PMID:37008944):** heterozygous p.L107V segregating with 14-Ala homozygosity in five siblings with athyreosis. "The p.L107V variant demonstrated to significantly reduce the FOXE1 transcriptional activity."

**Classification and population data:**
- ClinVar classifications and gnomAD frequencies for each variant were not retrieved. Check ClinVar before recording a `clinical_significance`.
- All reported variants are rare or private. There is no founder variant.
- All variants are germline. Somatic *FOXE1* changes (promoter methylation, for example) occur in cancers and have nothing to do with BLS.

**Mechanism class:**
- Mostly loss of function: S57N is partial loss of function, the frameshift is predicted loss of function.
- R73S is a documented exception with increased activity: "enhanced gene activity should be considered among the mechanisms underlying Bamforth–Lazarus syndrome" (PMID:24219130, paraphrased conclusion).
- This fits evidence that FOXE1 dosage must be tightly controlled: *overexpression* of mouse TTF-2 also causes cleft palate (Meng 2012, PMID:22304410).

**Other genetic features:**
- **Heterozygotes** (parents) are euthyroid and have no malformations (Carré 2014).
- **Modifier genes:** the polyalanine tract length is the only proposed candidate (see §2).
- **Epigenetics:** nothing is documented for BLS.
- **Chromosomal:** uniparental disomy 9 is one mechanism that produces homozygosity (PMID:20484477). There are no copy-number cases.

---

## 5. Environmental information

There are no known environmental, lifestyle or infectious causes. The only gene–environment finding is the zebrafish ethanol sensitivity result (PMID:39360443, model organism). Iodine status does not apply, because the defect is in thyroid development.

---

## 6. Mechanism / pathophysiology

### Causal chain

1. **Biallelic *FOXE1* variant**, homozygous through consanguinity or UPD9. This **results in** a forkhead-domain protein that cannot bind DNA, has reduced transactivation or, for R73S, has excess transactivation.
   - The human molecular finding is demonstrated (PMIDs 9697705, 12165566, 16882747, 20484477, 24219130).
2. **Branch A: thyroid.** Loss of FOXE1 in thyroid precursor cells of the foregut endoderm **leads to** failure of the thyroid bud to migrate down from the pharyngeal floor.
   - Mouse evidence: "Titf2-null mutant mice exhibit cleft palate and either a sublingual or completely absent thyroid gland" (PMID:9697704).
   - Human *migration* failure is inferred from the mouse model. Humans show agenesis, and in R102C a gland in place.
   - FOXE1 sits in a thyroid transcription-factor network with NKX2-1, PAX8 and HHEX (Parlato 2004, PMID:15581879).
   - Recent stem-cell work adds a thyroid fate-choice role: "Foxe1 knockout impairs Nkx2-1+ cell differentiation and maturation into thyroid follicular-like cells", and the knockout cells drift toward a lung fate, with reduced chromatin accessibility at the *Pax8* locus (PMID:42324400, IN_VITRO, mouse ESC organoids).
3. **The thyroid is absent or dysplastic**, which **results in** no thyroxine synthesis, raised TSH and **congenital hypothyroidism**. In the R73S case the gland was absent even though thyroid gene activity was increased; why gain of function causes agenesis is not explained.
   - FOXE1 also controls genes in the differentiated gland: it binds the *TG* and *TPO* promoters (PMID:24219130).
   - Deleting *Foxe1* in the adult mouse causes hypothyroidism: "Plasma TSH was elevated … as early as 4 weeks" (PMID:36156081).
   - This explains hypothyroidism in R102C patients whose gland is present.
4. **Untreated hypothyroidism** during the critical neonatal window **leads to** impaired brain development (neurodevelopmental delay). This step is prevented by early levothyroxine.
5. **Branch B: palate.** FOXE1 in palatal-shelf epithelium directly activates **MSX1** and **TGFB3**. Loss of FOXE1 **leads to** their loss: "Tgf-β3 and Msx1 mRNAs were almost absent in palatal shelves" of Foxe1-null embryos, and "all the known forkhead-domain mutations … affect the FOXE1 ability" to activate them (PMID:21177256). This **results in** failed palatal-shelf fusion and **cleft palate**. It is demonstrated in the mouse and in vitro. Overexpression also causes clefting (PMID:22304410).
6. **Branch C: hair.** FOXE1 is a target of Sonic hedgehog/Gli in the lower hair-follicle compartment. "Foxe1-null skin displays aberrant hair formation with the production of thinner and curly pelage hairs" (PMID:15367491). This plausibly **leads to** abnormal hair-shaft growth and orientation, seen clinically as **spiky hair**. The step from mouse to human is inferred.
7. **Branch D: choanae and epiglottis.** FOXE1 is expressed in the foregut endoderm and pharyngeal/craniofacial structures (Dathan 2002, PMID:12203737). Defective development there is the presumed cause of **choanal atresia** and **bifid epiglottis**. This mechanism has **not been demonstrated**.

### Checklist detail

**Pathways:**
- Shh–Gli → FOXE1 (hair follicle)
- FOXE1 → MSX1 / TGF-β3 (palate)
- the NKX2-1/PAX8/FOXE1/HHEX thyroid transcription-factor network
- FOXE1 → TG / TPO (thyroid hormone synthesis)

**GO process terms (cache-verified):**
- GO:0030878 thyroid gland development
- GO:0060021 roof of mouth development
- GO:0031069 hair follicle morphogenesis
- GO:0001942 hair follicle development
- GO:0006590 thyroid hormone generation (downstream)

**Cell types (CL, cache-verified):**
- CL:0002258 thyroid follicular cell
- CL:0002559 hair follicle cell
- CL:0000008 migratory cranial neural crest cell (palatal mesenchyme context; FOXE1 itself is epithelial, so bind this with care)
- A specific CL term for palatal epithelium was not looked up.

**Other categories:**
- **Protein dysfunction:** loss of DNA binding by the forkhead domain; R73S is hypermorphic.
- **Metabolic:** hypothyroxinemia.
- **Immune:** none intrinsic. One adult-deletion mouse study notes "an increase in thyroidal mast cells" (PMID:36156081); its relevance to humans is unknown.
- **Omics, single-cell, spatial:** no human BLS datasets are known. The ESC-organoid chromatin and transcriptome data are in PMID:42324400.

---

## 7. Anatomical structures affected

**Primary:**
- thyroid gland (UBERON:0002046)
- secondary palate / roof of mouth
- scalp hair follicles
- choanae / posterior nasal aperture
- epiglottis

All UBERON IDs need lookup except the commonly cited thyroid gland ID, which should still be verified.

**Body systems:** endocrine, craniofacial/oral, upper airway, integument. CNS involvement is secondary, through hypothyroidism.

**Cellular level:**
- thyroid follicular cells, which are absent
- palatal-shelf epithelium
- outer root sheath and lower follicle compartment

**Subcellular:** nucleus. FOXE1 is a nuclear transcription factor; the zebrafish mutant disrupts its nuclear localization signal (PMID:36994096).

**Lateralization:** midline structures. Choanal atresia is usually bilateral (R102C) but can be partial or unilateral (R73S, right side).

---

## 8. Temporal development

- **Onset:** congenital. The malformations are present at birth. Hypothyroidism is detected by newborn screening, or clinically within weeks if screening is missed (sleepiness and poor feeding at one month in Carré 2014).
- **Course:** a lifelong, stable condition with no progression. Sarma 2022 notes a phenotype that changes with age in one case.
- **Critical period:** the first weeks of life. Levothyroxine started within the first 2 weeks prevents neurocognitive damage (ESPE consensus, PMID:24446653). Neonatal airway management for choanal atresia is also time-critical.
- **Remission:** none. The hypothyroidism is permanent.

---

## 9. Inheritance and population

- **Inheritance:** autosomal recessive (HP:0000007, cache-verified). ClinGen rates FOXE1 Definitive for AR.
- **Penetrance:** complete among biallelic cases reported so far. Expressivity varies, for example in the presence of choanal atresia or bifid epiglottis and in gland status.
- **Anticipation:** none.
- **Uniparental disomy:** documented (UPD9).
- **Prevalence:** unknown, ultra-rare. Probably fewer than 20 genotyped individuals have been published. Orphanet likely lists it as "<1/1,000,000" or by case count; this is not verified. Record it as `CASES_IN_LITERATURE`.
- **Populations:** British, French, Turkish, Egyptian, Indian and Omani families. No founder allele.
- **Sex ratio:** no bias expected; both sexes reported.
- **Carrier frequency:** not established.

---

## 10. Diagnostics

**Laboratory:**
- newborn TSH screening
- confirmatory serum TSH and free T4 (raised TSH, low or undetectable T4)
- serum thyroglobulin: undetectable in true athyreosis, which helps separate agenesis from ectopy or dyshormonogenesis

LOINC codes need lookup through `just loinc-seed-cache`. Do not type them by hand.

**Imaging:**
- thyroid ultrasound plus ^99mTc or ^123I scintigraphy: no uptake in athyreosis; a sublingual focus would suggest ectopy
- CT or nasal endoscopy for choanal atresia
- airway endoscopy for the epiglottis

**Genetic testing:**
- single-gene *FOXE1* sequencing (one coding exon, GC-rich, includes the polyalanine tract), or
- a congenital hypothyroidism / thyroid dysgenesis panel (*TSHR, PAX8, NKX2-1, FOXE1, NKX2-5, GLIS3, JAG1, CDCA8* …), or
- exome sequencing

If only one allele is found, or homozygosity with only one carrier parent, look for UPD9 with SNP array or microsatellites.

**Clinical criteria:** No formal criteria exist. In practice the diagnosis rests on congenital hypothyroidism from thyroid dysgenesis plus cleft palate, with or without spiky hair or choanal atresia, plus biallelic *FOXE1* variants. The ESPE congenital hypothyroidism guideline recommends genetic testing for syndromic congenital hypothyroidism (PMID:24446653).

**Differential diagnosis:**

| Condition | Distinguishing features |
|---|---|
| *NKX2-1* (brain–lung–thyroid) syndrome | chorea, respiratory distress |
| *PAX8* thyroid dysgenesis | renal/urogenital anomalies |
| *GLIS3* | neonatal diabetes, congenital glaucoma, kidney cysts |
| CHARGE (*CHD7*) | choanal atresia, but coloboma, heart and ear anomalies |
| Kabuki and 22q11.2 deletion | can combine clefting and hypothyroidism |
| isolated cleft palate with unrelated congenital hypothyroidism | — |

**Screening:** Universal newborn TSH screening detects the hypothyroidism. Cascade carrier testing and prenatal or preimplantation testing are possible once the familial variants are known.

---

## 11. Outcome and prognosis

- There are no survival data. Life expectancy is expected to be normal with early levothyroxine and airway/cleft management. This is inferred; no natural history study exists.
- **Main threats:**
  - neonatal airway obstruction from bilateral choanal atresia
  - neurodevelopmental impairment if thyroid replacement is delayed
  - speech, feeding and middle-ear problems related to the cleft
- **Prognostic factors:** age at starting levothyroxine and adequacy of the dose; severity of the airway malformation.

---

## 12. Treatment

| Intervention | Notes | NCIT `treatment_term` | Agent |
|---|---|---|---|
| Levothyroxine replacement, lifelong, started at newborn diagnosis (ESPE: 10–15 µg/kg/day initially, PMID:24446653) | core therapy | NCIT:C15986 Pharmacotherapy (cache-verified) | CHEBI:18332 L-thyroxine (cache-verified); `therapeutic_modality: SMALL_MOLECULE` |
| Cleft palate repair (around 2 months of age in the R73S case) | surgical | NCIT:C15329 Surgical Procedure (cache-verified); `SURGERY` | — |
| Choanal atresia repair (endoscopic transnasal) plus neonatal airway support | surgical | NCIT:C15329 | — |
| Speech-language therapy, multidisciplinary cleft-team care | supportive | NCIT:C159273 (from CLAUDE.md list; confirm label) | `BEHAVIORAL` |
| Genetic counseling | — | NCIT:C15240 Genetic Counseling (cache-verified) | — |

- **Pharmacogenomics:** none.
- **Gene or cell therapy:** none.
- **Clinical trials:** none found. A ClinicalTrials.gov search was not run separately, but no BLS-specific trial is expected.

---

## 13. Prevention

- **Primary prevention:** carrier testing in consanguineous families; prenatal or preimplantation genetic diagnosis once the familial variants are known; genetic counseling (25% recurrence risk per pregnancy for carrier couples).
- **Secondary prevention:** universal newborn congenital hypothyroidism screening, which prevents intellectual disability.
- **Tertiary prevention:** prompt levothyroxine with TSH/fT4 monitoring; airway assessment at birth; cleft-team follow-up; hearing checks (hearing loss was reported in Sarma 2022).

---

## 14. Other species / natural disease

- No naturally occurring animal BLS has been found. OMIA was not searched.
- *FOXE1* is conserved across vertebrates.
  - The Eh1 (engrailed homology) repression motif was lost from FoxE1 in the lineage leading to placental mammals (PMID:38150428).
  - Orthologs: mouse *Foxe1* (MGI), zebrafish *foxe1* (ZFIN). IDs need lookup.

---

## 15. Model organisms

| Model | Phenotype | Fidelity / limits | PMID |
|---|---|---|---|
| Mouse *Titf2/Foxe1* null (germline) | cleft palate; thyroid absent or sublingual (failed migration); neonatal death | **High** for thyroid and palate. Neonatal lethality limits postnatal study. Mice lack choanal atresia and spiky hair as phenotypes. | 9697704 |
| Mouse *Foxe1*-null skin | thinner, curly pelage hair; Foxe1 downstream of Shh/Gli | partial model for spiky hair | 15367491 |
| Mouse *Foxe1*-null palatal shelves | loss of Msx1 and Tgfb3 | mechanistic | 21177256 |
| Mouse TTF-2 overexpression | cleft palate | supports dosage sensitivity | 22304410 |
| Mouse adult inducible *Foxe1* deletion (Foxe1^flox/flox; Cre-TAM) | smaller follicles, raised TSH, more mast cells | postnatal thyroid function role | 36156081 |
| Zebrafish *foxe1* mutant (NLS disrupted) | ceratohyal cartilage and skeletal defects; "thyroid follicle morphology or differentiation were unaffected" in larvae | **partial/low** for the thyroid in larvae (`HUMAN_MODEL_MISMATCH` candidate) | 36994096 |
| Zebrafish *foxe1*, adult | signs of hypothyroidism; scale mineralization defects; craniofacial sensitivity to ethanol | adult thyroid phenotype emerges | 39360443 |
| Mouse ESC-derived thyroid organoids, *Foxe1* KO | impaired thyroid differentiation; lung-like fate | IN_VITRO | 42324400 |

Resources: MGI, IMSR/MMRRC (for *Foxe1* alleles), ZFIN.

---

## Curation notes for the dismech entry

1. **Gene validity.** Record a `gene_disease_validity` entry: DEFINITIVE / CLINGEN, using the CGGV ID above. Quote the cached row after `just fetch-reference CGGV:…`.
2. **Gain-of-function variant.** R73S needs `functional_impact_category: GAIN_OF_FUNCTION` (or HYPERMORPHIC) on its own record. The other variants are LOSS_OF_FUNCTION, or PARTIAL_LOSS_OF_FUNCTION for S57N. Do not collapse them into one record.
3. **Spiky hair and bifid epiglottis.** No specific HPO term for either was confirmed. If you use HP:0001595, declare a `coarse_binding_basis`, probably `NO_HPO_TERM` if a search confirms there is none. Record the query you ran.
4. **Unconfirmed items.** Treat the F89L Omani report (preprint/2026) and ORPHA:1226 as unconfirmed until fetched.
5. **Separate entities.** Keep polyalanine-tract susceptibility, non-syndromic cleft lip/palate and thyroid-cancer GWAS signals out of this entry's causal genetics. They are separate entities. At most, mention them as notes or modifiers.

---

## Key references (PMIDs verified through Europe PMC)

- Bamforth JS et al. 1989 *J Med Genet*. Congenital hypothyroidism, spiky hair, and cleft palate. **PMID:2918525**
- Clifton-Bligh RJ et al. 1998 *Nat Genet* 19:399. Mutation of the gene encoding human TTF-2 associated with thyroid agenesis, cleft palate and choanal atresia. **PMID:9697705**
- De Felice M et al. 1998 *Nat Genet*. A mouse model for hereditary thyroid dysgenesis and cleft palate. **PMID:9697704**
- Castanet M et al. 2002 *Hum Mol Genet*. S57N loss-of-function TTF-2. **PMID:12165566**
- Dathan N et al. 2002 *Dev Dyn*. Titf2/Foxe1 expression in foregut endoderm, palate, hair. **PMID:12203737**
- Brancaccio A et al. 2004 *Hum Mol Genet*. Foxe1, a Shh target, in hair follicle morphogenesis. **PMID:15367491**
- Parlato R et al. 2004 *Dev Biol*. Thyroid organogenesis regulatory network. **PMID:15581879**
- Baris I et al. 2006 *JCEM*. R102C, congenital hypothyroidism without athyreosis. **PMID:16882747**
- Carré A et al. 2007 *Hum Genet*. FOXE1 polyalanine length and thyroid dysgenesis. **PMID:17717707**
- Moreno LM et al. 2009 *Hum Mol Genet*. FOXE1 and CL/P and CP. **PMID:19779022**
- Gudmundsson J et al. 2009 *Nat Genet*. 9q22.33 (FOXE1) and thyroid cancer. **PMID:19198613**
- Castanet M et al. 2010 *JCEM*. Maternal UPD9, F137S. **PMID:20484477**
- Castanet M, Polak M 2010 *Horm Res Paediatr*. Spectrum of human Foxe1/TTF2 mutations. **PMID:20453517**
- Kang IN et al. 2010 *Biochem Genet*. Malaysian congenital hypothyroidism cohort. **PMID:20094846**
- Venza I et al. 2011 *Hum Mol Genet*. MSX1 and TGF-β3 as FOXE1 targets. **PMID:21177256**
- Meng T et al. 2012 *J Cell Mol Med*. TTF-2 overexpression causes cleft palate. **PMID:22304410**
- Carré A et al. 2014 *Thyroid* 24:649. R73S gain of function in BLS. **PMID:24219130** ([PMC3993030](https://pmc.ncbi.nlm.nih.gov/articles/PMC3993030/))
- Léger J et al. 2014 *JCEM*. ESPE congenital hypothyroidism consensus guidelines. **PMID:24446653**
- Sarma AS et al. 2022 *Eur J Med Genet*. c.141dupC frameshift; expanded phenotype. **PMID:35963604**
- Lim G et al. 2022 *Endocrinology*. Adult Foxe1 deletion. **PMID:36156081**
- Raterman ST et al. 2023 *Front Cell Dev Biol*. foxe1 zebrafish. **PMID:36994096**
- Grassi ES et al. 2023 *Front Endocrinol*. Polyalanine tract and L107V. **PMID:37008944**
- Sharma M et al. 2023 *PLoS One*. Loss of the Eh1 motif in placental FoxE1. **PMID:38150428**
- Raterman ST et al. 2025 *Dev Dyn*. foxe1 zebrafish hypothyroidism and ethanol sensitivity. **PMID:39360443**
- Fonseca BF et al. 2026 *EMBO Rep*. Foxe1 deficiency and thyroid versus lung fate. **PMID:42324400**
- Al-Araimi M et al. Novel FOXE1 mutation in an Omani family. Research Square preprint 2025; [Springer 2026](https://link.springer.com/article/10.1007/s40142-026-00256-3). **Unverified**

## Sources

- [OMIM #241850](https://omim.org/entry/241850) (not reachable; cited from search results)
- [OMIM *602617 FOXE1](https://www.ncbi.nlm.nih.gov/omim/602617)
- [Sarma 2022, PubMed 35963604](https://pubmed.ncbi.nlm.nih.gov/35963604/)
- [Carré 2014, PMC3993030](https://pmc.ncbi.nlm.nih.gov/articles/PMC3993030/)
- [Carré 2014, Thyroid](https://journals.sagepub.com/doi/10.1089/thy.2013.0417)
- [Castanet & Polak 2010, PubMed 20453517](https://pubmed.ncbi.nlm.nih.gov/20453517)
- [Venza 2011, Hum Mol Genet](https://academic.oup.com/hmg/article/20/5/1016/2386230)
- [Clifton-Bligh 1998, Nature Genetics](https://www.nature.com/articles/ng0898_395)
- [GenCC submission SGC-116909.1](https://thegencc.org/submissions/SGC-116909.1)
- [Al-Araimi, Springer](https://link.springer.com/article/10.1007/s40142-026-00256-3)
- [MalaCards](https://www.malacards.org/card/bamforth_lazarus_syndrome)
- [DocCheck Flexikon](https://flexikon.doccheck.com/de/Bamforth-Lazarus-Syndrom)
- [Europe PMC REST API](https://www.ebi.ac.uk/europepmc/webservices/rest/search)
- Repository caches: `cache/clingen/gene_validity.csv`, `cache/{hp,go,cl,ncit,chebi}/terms.csv`

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 28 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 11 |
| Quoted claims found in source | 8 |
| Quoted claims **not** found in source | 3 |
| References weighed for topical relevance | 28 |
| On topic | 17 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:2918525` *(abstract only)*: "Two brothers … with athyroidal hypothyroidism, spiky hair, choanal atresia, cleft palate, and bifid epiglottis"
  - closest text in source: "Two brothers are described with athyroidal hypothyroidism, spiky hair, choanal atresia, cleft palate, and bifid epiglottis"
- `PMID:39360443` *(abstract only)*: "increased sensitivity to ethanol for craniofacial malformations"
  - closest text in source: "We here investigated whether ethanol exposure increases the risk of developing craniofacial malformations in foxe1 mutant larvae that we compared to wild types"
- `PMID:36156081` *(abstract only)*: "Plasma TSH was elevated … as early as 4 weeks"
  - closest text in source: "Plasma TSH was elevated in Foxe1flox/flox/Cre-TAM mice as early as 4 weeks and T4 was lower in pooled samples from 12 and 20 weeks"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 31 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 2 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 0 |

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.

29 of 31 terms resolved to a current term; the rest could not be looked up either way.