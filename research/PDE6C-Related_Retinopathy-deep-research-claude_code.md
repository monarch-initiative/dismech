---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-02T00:04:33.510828'
end_time: '2026-11-02T00:10:03.507013'
duration_seconds: 330.0
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: PDE6C-Related Retinopathy
  mondo_id: MONDO:1040028
  category: Mendelian
  causal_genes: PDE6C
  omim_id: not recorded
  synonyms: achromatopsia 5; cone dystrophy 4; PDE6C-related cone dystrophy; PDE6C-related
    cone-rod dystrophy
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
  web_search_requests: 7
  num_turns: 33
  total_cost_usd: 2.7433751
  session_id: 2ccff955-20d8-5bb4-8e86-b52d55e2a947
  stop_reason: end_turn
  permission_denials: 5
  denied_tools:
  - Bash
  assistant_text_blocks: 4
citation_count: 15
reference_validation:
  total_references: 49
  verified: 49
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 8
  quotes_valid: 6
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:31826238
  - PMID:32306724
  relevance_assessed: 49
  on_topic: 35
  needs_review: true
  validator_version: 0.4.0
term_validation:
  total_terms: 42
  verified: 40
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_variant: 1
  unresolvable_prefixes:
  - ORPHA
  - OMIA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** PDE6C-Related Retinopathy
- **MONDO ID:** MONDO:1040028 (if available)
- **Causal gene(s):** PDE6C
- **OMIM:** not recorded
- **Synonyms:** achromatopsia 5; cone dystrophy 4; PDE6C-related cone dystrophy; PDE6C-related cone-rod dystrophy
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **PDE6C-Related Retinopathy** covering all of the
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

Searching PubMed for the main PDE6C papers so I can take quotes straight from their abstracts.

I'm checking the repo's reference cache for these papers, since fetching abstracts from the shell needs approval.

Collected quotes from the main human, mouse, zebrafish and macaque papers. Next I'm checking the repo's local term caches for the ontology IDs.

# PDE6C-Related Retinopathy (MONDO:1040028): research report

## Before you use this report

- **How each quote was obtained:**
  - The Thiadens 2009 quotes (PMID:19615668) are copied from the cached abstract at `references_cache/PMID_19615668.md`, so they are exact.
  - All other quoted fragments (marked "‡") came through a web fetch tool that summarises pages. They are probably verbatim but have **not** been checked character by character. Run `just fetch-reference PMID:<id>` and confirm each one before using it as a `snippet:`.
  - Some fetched fragments were cut off mid-phrase (for example "...cone-rod dystrophy and achromatopsia (ACHM)."). A cut-off fragment is not a complete quote and needs extending from the source.
- **Ontology terms:** CURIEs and labels marked ✓ were read from the repository's `cache/*/terms.csv` in this session. Terms not marked ✓ have not been checked and need a `runoak`/OLS lookup before binding.
- **No live PubMed access from the shell:** `curl`/E-utilities calls needed approval and were not run. Abstracts were reached only through the fetch tool.

---

## 1. Disease Information

**Overview.** PDE6C-related retinopathy is an autosomal recessive disorder of the cone photoreceptors. It is caused by biallelic pathogenic variants in **PDE6C** (phosphodiesterase 6C; hgnc:8787; OMIM *600827; 10q23.33; UniProt P51160; Ensembl ENSG00000095464; MANE transcript NM_006204.4). PDE6C encodes the catalytic α′ subunit of the cone-specific cGMP phosphodiesterase. The clinical picture spans:

- complete and incomplete **achromatopsia (ACHM5)**;
- early-onset **cone dystrophy (COD4)**;
- **cone-rod dystrophy** in some patients.

> "The PDE6C gene encodes the cone alpha subunit of cyclic guanosine monophosphate (cGMP) phosphodiesterase, which converts cGMP to 5'-GMP, and thereby plays an essential role in cone phototransduction." (PMID:19615668, verified)

> "Our findings identify PDE6C as a gene for cone photoreceptor disorders and show that arCD and ACHM constitute genetically and clinically overlapping phenotypes." (PMID:19615668, verified)

**Identifiers**

| System | ID | Notes |
|---|---|---|
| MONDO | MONDO:1040028 *PDE6C-related retinopathy* | the entry's anchor |
| MONDO subtypes | MONDO:0800196 *achromatopsia 5* ✓; MONDO:0013129 *cone dystrophy 4* | both already in the KB entry |
| OMIM (phenotype) | #613093 *Cone dystrophy 4; COD4* | OMIM files ACHM5 inside this entry; it has no separate phenotype number ([OMIM mirror](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/commit/16b4b23030b9c25e5a647a69ebd82dc9aecccaad/www.ncbi.nlm.nih.gov/omim/613093)) |
| OMIM (gene) | *600827 PDE6C | |
| MedGen | 416518 | lists COD4, achromatopsia 5, cone dystrophy 4, PDE6C cone dystrophy |
| ClinGen | Definitive, AR, PDE6C ↔ MONDO:1040028; Retina GCEP; 2023-11-02 | `CGGV:assertion_73ed48ac-bdd6-4608-953d-773da6ade759-2023-11-02T160000.000Z` (from `kb/genes/ingest/clingen_gene_validity.tsv`) |
| Orphanet | not confirmed | the disease likely sits under ORPHA:49382 (achromatopsia) and the cone/cone-rod dystrophy groups. Not verified. |
| ICD-10-CM / ICD-11 | H53.51 (achromatopsia); H35.5 (hereditary retinal dystrophy) | general codes only; nothing specific to PDE6C. Not verified in the repo. |
| MeSH | Color Vision Defects; Cone-Rod Dystrophies | general headings |
| OMIA (animal) | OMIA:002163-9544 *Cone dystrophy 4, PDE6C-related* in rhesus macaque ([OMIA](https://omia.org/4146)) | |

**Synonyms:** achromatopsia 5 (ACHM5); cone dystrophy 4 (COD4); PDE6C-related cone dystrophy; PDE6C-related cone-rod dystrophy; PDE6C-associated achromatopsia; rod monochromacy (PDE6C).

**Source of information:** Aggregated disease-level resources (OMIM, ClinGen, GeneReviews) plus small case series and individual case reports. No EHR-derived data were found.

## 2. Etiology

- **Cause:** Monogenic, autosomal recessive. Patients carry biallelic loss-of-function variants in PDE6C, either homozygous or compound heterozygous.
- **Genetic risk factors:** Only the biallelic causal variants are known. Consanguinity raises the chance of homozygosity. In the original study, homozygous regions were found by homozygosity mapping: "identified large homozygous regions spanning the PDE6C gene in one sibling pair with early-onset arCD and one sibling pair with incomplete ACHM" (PMID:19615668, verified).
- **Modifier genes:** None established in humans. Possible molecular modifiers:
  - Correct maturation of PDE6C depends on the chaperone AIPL1 and the inhibitory γ′ subunit (PDE6H) (PMID:38110033; PMID:28378769, mouse).
  - Mouse data show that the γ′ subunit stabilises the cone PDE6 holoenzyme (PMID:30038560).
- **Environmental risk factors:** None known. Light exposure causes photophobia but has not been shown to change the course of the disease.
- **Protective factors and gene–environment interactions:** None documented in humans.

## 3. Phenotypes

The best human data are two deep-phenotyping series: Georgiou et al. 2019 (n=8; PMID:31826238) and Daich Varela et al. 2020 (n=4; PMID:33001157). Larger genetic cohorts are Grau 2011 (12 patients from 7 families; PMID:21127010) and Weisschuh 2018 (15 index cases; PMID:30080950).

| Phenotype | HPO term | Onset | Frequency | Course | Key evidence |
|---|---|---|---|---|---|
| Colour vision loss (severe; often total) | HP:0000551 Color vision defect ✓; HP:0011516 Achromatopsia ✓ | congenital or infancy | 8/8 (Georgiou) | stable or slowly progressive | "severe color vision loss" ‡ (PMID:31826238) |
| Nystagmus, early onset | HP:0000639 Nystagmus ✓ | first months of life | 8/8; also present in the Daich Varela series | may lessen with age | "early-onset nystagmus" ‡ (PMID:31826238; PMID:33001157) |
| Photophobia / day blindness | HP:0000613 Photophobia ✓ | infancy | 8/8 | lifelong | PMID:31826238 |
| Reduced visual acuity, usually about 20/200 | HP:0007663 Reduced visual acuity ✓; HP:0001141 Severely reduced visual acuity ✓ | infancy | 8/8 | slowly worsens in adults | PMID:31826238 |
| High myopia | HP:0011003 High myopia ✓ | childhood | 5/8 | — | "five of them had high myopia" ‡ (PMID:31826238) |
| Absent or severely reduced cone ERG; rod ERG normal or later reduced | HP:0008275 Abnormal light-adapted electroretinogram ✓; HP:0000512 Abnormal electroretinogram ✓ | infancy | universal | rod responses may decline (cone-rod pattern) | PMID:33001157; PMID:42525358 |
| Foveal outer retinal disruption (absent EZ, hyporeflective zone, or atrophy); **no foveal hypoplasia** | HP:0030613 Abnormal foveal morphology on macular OCT ✓; HP:0000493 Abnormal foveal morphology ✓ | childhood onward | 8/8 abnormal; 0/8 foveal hypoplasia | progressive: EZ lesion grows a mean of 48.3 µm per year | "No subjects had foveal hypoplasia" ‡ (PMID:31826238) |
| Maculopathy / macular atrophy (adults) | HP:0007754 Macular dystrophy ✓; HP:0007401 Macular atrophy ✓ | adulthood | adults in both series | slowly progressive; hypoautofluorescent area grows about 0.13 mm² per year | "the adults had clear macular dystrophy" ‡ (PMID:33001157) |
| Cone-rod dystrophy phenotype | HP:0000548 Cone/cone-rod dystrophy ✓ | childhood to adult | 3/4 (Daich Varela) | progressive | "Three of the four patients had a cone-rod dystrophy" ‡ (PMID:33001157) |
| Central scotoma | HP:0000603 Central scotoma ✓ | — | frequency not reported | — | inferred from maculopathy |

**Quality of life:** No PDE6C-specific quality-of-life studies were found. Achromatopsia generally impairs reading, outdoor and daylight activities, and driving eligibility. Validated instruments exist (for example the NEI-VFQ-25 and achromatopsia-specific instruments used in CNGA3/CNGB3 trials), but none have been applied to PDE6C cohorts.

## 4. Genetic / Molecular Information

- **Gene:** PDE6C. It encodes PDE6α′, the cone-specific catalytic subunit (HGNC previous symbols: PDEA2, ACHM5, COD4). Cone PDE6 is a homodimer of α′ subunits bound to two inhibitory γ′ subunits (PDE6H).
- **Variant spectrum:**
  - Original discovery (PMID:19615668, verified):
    - homozygous missense **p.R29W** and **p.Y323N**;
    - compound heterozygous frameshift + splice variant;
    - splice variant + **p.M455V**.
  - Grau 2011: "Eleven different PDE6C mutations were found" ‡, comprising nonsense, splice (shown by minigene assay), a 1-bp insertion, and missense variants (PMID:21127010).
  - Weisschuh 2018: "The mutation spectrum comprises 18 different alleles, 15 of which are novel" ‡ (PMID:30080950).
  - Georgiou 2019: three further novel variants (PMID:31826238).
  - Later reports: novel variants from Iran, China and Saudi Arabia (PMID:32306724, PMID:32787476, PMID:34720973, PMID:35422133).
  - Nonhuman primate: macaque **p.R565Q** in the catalytic domain (PMID:30667376).
- **Classification:** ClinGen rates the gene–disease relationship **Definitive** (AR). For individual variants, use ClinVar: most protein-truncating and splice alleles are Pathogenic or Likely Pathogenic, and many missense alleles are VUS. One recent report describes a likely-pathogenic frameshift in trans with a VUS (PMID:42525358).
- **Functional consequence:** Loss of function. Most missense variants act as functional nulls: "Four of the six PDE6C missense mutations led to baseline PDE activities" ‡. Two other missense variants showed about 60% and 80% loss of activity together with altered activation properties (PMID:21127010). These partial-loss alleles may underlie the milder, incomplete ACHM or cone dystrophy end of the spectrum. This genotype–phenotype link is inferred, not formally shown.
- **Variant origin:** Germline. No somatic or mosaic reports were found.
- **Allele frequency:** Every allele is rare (check gnomAD per variant). No founder allele has been established.
- **Epigenetics:** None reported in humans. In cpfl1 mice, H3K27 trimethylation and HDAC activity influence cone survival: "Increased H3K27 trimethylation contributes to cone survival" (title of PMID:35810394; mouse); HDAC inhibition protects cones (PMID:28172811).
- **Chromosomal abnormalities:** None characteristic.

## 5. Environmental Information

There are no environmental, lifestyle or infectious causes. Bright light provokes photophobia; tinted or filter lenses manage it but do not change the course of disease. Not applicable otherwise.

## 6. Mechanism / Pathophysiology

**Causal chain**

1. **Biallelic PDE6C loss-of-function variants** (truncating, splice, or catalytically dead missense) **lead to** absent or severely reduced cone PDE6α′ catalytic activity (PMID:21127010; PMID:30667376 shows a stable but catalytically dead protein: "is unable to hydrolyze cyclic GMP (cGMP)" ‡).
2. Loss of cone PDE6 **results in** failure of light-activated cGMP hydrolysis in cone outer segments. Transducin (GNAT2) activates nothing, so the CNG channels (CNGA3/CNGB3) stay open after light: **cone phototransduction fails**.
3. **Branch A (function).** Absent cone light responses **lead to** absent photopic ERG, day blindness, photophobia, loss of colour vision and poor acuity. Without foveal fixation, **nystagmus** develops. This is congenital or infantile.
4. **Branch B (degeneration).** Unhydrolysed cGMP **accumulates** in cones (shown in mouse: "cpfl1 cone photoreceptor cell death was associated with an accumulation of cyclic guanosine monophosphate (cGMP)" ‡, PMID:20593360). This **leads to** excess Ca²⁺ entry through CNG channels and activation of cGMP-dependent protein kinase (PKG), calpain and HDAC activity (PMID:27402880; PMID:25392995; PMID:28172811), and then to non-apoptotic cone death. In zebrafish the death is **RIP3-dependent necroptosis** (PMID:24413151). Whether this happens in human cones is *inferred* from animal models.
5. Progressive cone loss **leads to** expanding foveal ellipsoid-zone loss and outer retinal atrophy, which appears clinically as **progressive maculopathy** (PMID:31826238).
6. **Secondary rod involvement** (a subset of patients) leads to a **cone-rod dystrophy** pattern (PMID:33001157). In macaques, rod responses fall late: "The oldest homozygote (11 years) had reduced rod responses" ‡ (PMID:39641747). In zebrafish, rods die as bystanders through a caspase-dependent pathway (PMID:24413151). The mechanism in humans is unproven.
7. **Myopia** is common (5/8 patients). Its mechanism is unknown; a link to abnormal cone signalling during eye growth is speculative.

**Other mechanistic detail**

- **Protein maturation:** Folding of PDE6C needs the chaperones HSP90 and AIPL1 together with the γ′ subunit. Without Pγ, PDE6C mostly misassembles (PMID:38110033, in vitro). Structural work: "the dynamic nature of PDE6C association with its regulatory γ-subunit" ‡ (cryo-EM; PMID:39739818). Prenylation targets cone PDE6 to the outer segment (PMID:37384398).
- **Trafficking:** In mouse, "functional PDE6 is required for trafficking of M-opsin to cone outer segments" ‡ (PMID:21799013).
- **Immune / inflammatory involvement:** Microglia change state during degeneration and regeneration in zebrafish pde6c mutants (PMID:41995141). STAT3-related genes are induced in cpfl1 cones (PMID:20467778). Neither has been studied in humans.
- **Transcriptomics:** Whole-retina RNA-seq of zebrafish pde6c at 5 dpf (PMID:29231925; check GEO for the accession). No human omics data were found.

**Suggested terms**

- **GO:**
  - GO:0007602 phototransduction ✓ (DECREASED)
  - GO:0047555 3',5'-cyclic-GMP phosphodiesterase activity ✓ (DECREASED / LOSS_OF_FUNCTION)
  - GO:0046068 cGMP metabolic process ✓
  - GO:0050908 detection of light stimulus involved in visual perception ✓
  - GO:0070266 necroptotic process ✓ (zebrafish evidence)
  - GO:0097190 apoptotic signaling pathway ✓ (rod bystander death)
  - GO:0001750 photoreceptor outer segment ✓ (cellular component); also GO:0120199 "cone photoreceptor outer segment" — **not verified**
- **CHEBI:** CHEBI:16356 3',5'-cyclic GMP ✓ (accumulates)
- **CL:** CL:0000573 retinal cone cell ✓ (primary); CL:0000604 retinal rod cell ✓ (secondary)

## 7. Anatomical Structures Affected

- **Organ:** Eye, bilateral and symmetric. Visual system only. No extra-ocular involvement has been reported.
  - The one reported co-occurrence with hearing loss came from a separate PDZD7 variant segregating in the same family (PMID:38956522). It is not part of PDE6C disease.
- **UBERON:** UBERON:0000970 eye ✓; UBERON:0000966 retina ✓; UBERON:0001787 photoreceptor layer of retina ✓; UBERON:0000053 macula lutea ✓; UBERON:0001786 fovea centralis ✓.
- **Cells:** Cone photoreceptors (CL:0000573) primarily; rods (CL:0000604) secondarily.
- **Subcellular:** Cone outer segment disc membranes, where PDE6 is held by prenylation.

## 8. Temporal Development

- **Onset:** Congenital or early infancy. Nystagmus and photophobia appear in the first months. Patients in one cohort were diagnosed between birth and 5 years.
- **Progression:**
  - Children: function is severely reduced from the start, with few structural changes.
  - Adults: progressive maculopathy (EZ lesion grows a mean of 48.3 µm/yr; hypoautofluorescent area grows a mean of 0.13 mm²/yr; PMID:31826238). Some patients develop a cone-rod dystrophy pattern.
  - Older adults: "few or no residual foveal cones" (paraphrase of PMID:31826238).
- **Course:** Lifelong, slowly progressive. There is no remission.
- **Critical window:** Childhood, while cones remain, is the likely window for gene therapy. In macaques, cone ERG is already absent at 3 months but foveal ONL thinning progresses over years (PMID:39641747). In mice, the gene therapy window narrows with age (shown for a related cone disease, PMID:41286353).

## 9. Inheritance and Population

- **Inheritance:** Autosomal recessive (HP:0000007 ✓). Penetrance is complete for biallelic null genotypes. Heterozygous carriers are unaffected: in macaques, "Heterozygotes could not be distinguished from wildtypes in any parameters" ‡ (PMID:39641747).
- **Expressivity:** Variable, from complete ACHM through incomplete ACHM and cone dystrophy to cone-rod dystrophy. Allelic severity probably contributes (PMID:21127010).
- **Anticipation and germline mosaicism:** Not applicable / not reported.
- **Epidemiology:**
  - Achromatopsia overall: about 1 in 30,000 (GeneReviews PMID:20301591; check the exact wording in the cached file).
  - PDE6C accounts for a small share of ACHM: "less than 2% of the cases" (PMID:32306724, secondary statement).
  - In the Tübingen cohort, 15 index cases came from a pre-selected group of 176, within an overall ACHM cohort of 1,074 independent families ‡ (PMID:30080950). That would put PDE6C roughly in the 1–2% range of ACHM; this is my inference, not a figure the paper states.
  - Implied prevalence is well under 1 in 1,000,000 (prevalence class `BELOW_1_IN_1000000`, or report as `CASES_IN_LITERATURE`).
- **Geography / populations:** Reported from Europe (Netherlands, Germany, UK, Denmark), the Middle East (Iran, Saudi Arabia, UAE; PMID:39024658), Pakistan, China, Japan and Korea. Enrichment in consanguineous families is expected; no specific founder alleles have been documented.
- **Sex ratio:** 1:1 (autosomal).

## 10. Diagnostics

- **Clinical examination:** Nystagmus, photophobia, reduced acuity, and colour vision testing (HRR, Farnsworth D-15, anomaloscope).
- **Electrophysiology:** Full-field ERG (ISCEV) shows absent or near-absent light-adapted and 30-Hz flicker responses. Rod responses are normal or later reduced. S-cone ERG is also absent; this separates the disease from blue cone monochromacy.
- **Imaging:** OCT shows EZ disruption, a foveal hyporeflective zone, or atrophy, and typically **no foveal hypoplasia**. This helps distinguish PDE6C disease from ATF6-ACHM, which does show foveal hypoplasia. Fundus autofluorescence shows central hypo- or hyper-autofluorescence. Adaptive optics can quantify residual cones.
- **Genetic testing:** An inherited retinal disease (IRD) gene panel or exome that includes CNGA3, CNGB3, GNAT2, PDE6C, PDE6H, ATF6 and RPGRIP1. GeneReviews: "biallelic pathogenic (or likely pathogenic) variants in ATF6, CNGA3, CNGB3, GNAT2, PDE6C, or PDE6H confirms the clinical diagnosis" (PMID:20301591, cached). Confirm splice variants with minigene or RNA assays (PMID:21127010). CNV analysis is advisable.
- **Differential diagnosis:**
  - other ACHM genes (CNGA3, CNGB3, GNAT2, PDE6H, ATF6, RPGRIP1 exon-18 deletion);
  - blue cone monochromacy (X-linked; S-cone ERG preserved);
  - early cone/cone-rod dystrophies (ABCA4, GUCY2D, CRX, KCNV2);
  - Leber congenital amaurosis;
  - albinism and congenital stationary night blindness (nystagmus with different ERG patterns).
- **Screening:** No newborn screening. Cascade carrier testing within families is possible.
- **LOINC:** None specific to this disease. Measurement codes for ERG or genetic panels would be generic.

## 11. Outcome / Prognosis

- **Life expectancy:** Normal. There is no disease-specific mortality.
- **Morbidity:** Lifelong legal blindness or low vision is common (acuity about 20/200). Patients are photophobic and colour-blind, and adults lose central vision slowly.
- **Prognostic factors:** Probably allele severity (partial versus null), age, and myopia, which is linked to atrophy. Not formally validated.
- **Complications:** High myopia, macular atrophy and amblyopia.

## 12. Treatment

There is **no approved disease-modifying therapy**, and **no PDE6C-specific clinical trial** was found. AAV gene-augmentation trials have run for CNGA3 and CNGB3 achromatopsia (for example NCT02599922, NCT02935517, NCT03758404, NCT03001310), but they do not include PDE6C. Check ClinicalTrials.gov again for any new PDE6C trials.

| Approach | NCIT term | Status / evidence |
|---|---|---|
| Tinted / filter lenses, red contact lenses, low-vision aids | NCIT:C15747 Supportive Care ✓; NCIT:C15315 Rehabilitation ✓ | standard of care (GeneReviews PMID:20301591) |
| Refractive correction of high myopia | (term not looked up) | routine care |
| Genetic counselling | NCIT:C15240 Genetic Counseling ✓ | recommended |
| AAV gene augmentation (PDE6C ± PDE6H) | NCIT:C15238 Gene Therapy ✓; modality `GENE_THERAPY` | preclinical. In rd10/cpfl1 mice, cone rescue needed both PDE6α′ and γ′: "improved photopic cone responses were achieved only after supplementation of both cone PDE6α' and PDE6γ' subunits" (PMID:30038560; quote taken from the search summary, verify) |
| HDAC inhibition (trichostatin A) | Pharmacotherapy | preclinical. "increased cone survival for up to 16 days post-injection" ‡ (PMID:28172811, mouse) |
| Necroptosis inhibition (RIP1/RIP3) | Pharmacotherapy | preclinical (zebrafish, PMID:24413151) |
| CRISPR correction in patient iPSCs | `GENE_EDITING` | in vitro (PMID:36835061, PMID:40083649; check which gene each study corrected; see also review PMID:42264060) |
| Photoreceptor transplantation | `CELL_THERAPY` | preclinical (cpfl1; PMID:25183393, PMID:27367586) |

Pharmacogenomics: none relevant. PDE5 inhibitors (sildenafil) also inhibit PDE6, but there are no data on their use in this disease.

## 13. Prevention

- **Primary prevention:** Genetic counselling. Carrier testing of relatives and partners in consanguineous families. Prenatal diagnosis or PGT when the familial variants are known.
- **Secondary prevention:** Early molecular diagnosis to support enrolment in future gene therapy while cones remain.
- **Tertiary prevention:** Photoprotection and treatment of refractive error and amblyopia. Whether photoprotection slows degeneration is unproven.
- No vaccines or public-health measures apply.

## 14. Other Species / Natural Disease

- **Rhesus macaque** (*Macaca mulatta*, NCBITaxon:9544): naturally occurring homozygous **PDE6C R565Q** (OMIA:002163-9544).
  - "a homozygous R565Q missense mutation in the catalytic domain of PDE6C" ‡ (PMID:30667376). The mutant protein is stable and correctly localised but catalytically dead.
  - Natural history from 102 eyes of 51 animals: cone ERG absent from 3 months, foveal ONL thinning with age, and late rod decline (PMID:39641747).
  - This model has a fovea, which makes it the closest model of the human disease.
- **Evolution:** PDE6 genes are conserved across vertebrates (PMID:27296292). Pde6c has been lost in the common vampire bat (PMID:35333583), and premature termination codons appear in cavefish (PMID:39833658). These are natural gene losses in species adapted to dim light.
- **Zoonotic potential:** None.

## 15. Model Organisms

| Model | Genotype | Recapitulation | Limitations | Key PMIDs |
|---|---|---|---|---|
| **cpfl1 mouse** (*Mus musculus*) | spontaneous Pde6c mutation (CXB-1 strain, chr 19), loss of function | no cone function; rapid cone degeneration that peaks around P24 with cGMP accumulation | mice have no fovea and few cones; degeneration is faster than in humans | 19887631, 20593360, 20238063, 28172811 |
| **rd10/cpfl1 double mutant** | Pde6b + Pde6c loss | both rods and cones degenerate; used for gene therapy | double-mutant background is artificial | 30038560 |
| **Zebrafish pde6c^w59** (*Danio rerio*) | nonsense mutation (Stearns et al. 2007, J Neurosci 27:13866; PMID not confirmed) | rapid cone degeneration from 4 dpf; rod bystander death; RIP3-dependent necroptosis | cone-rich retina that regenerates | 24413151, 20053919, 23365220, 29231925, 41995141 |
| **Rhesus macaque** | PDE6C R565Q homozygous | absent cone ERG; progressive foveal cone loss; late rod decline | colony-limited; few animals | 30667376, 39641747 |
| **Human iPSC / organoids** | patient-derived | CRISPR correction studies | does not reproduce fovea or degeneration timing | 36835061, 40083649 (gene to be confirmed) |
| **In vitro enzymology** | recombinant PDE6C mutants in insect cells | quantifies loss of catalytic activity | lacks cellular context | 21127010, 38110033, 39739818 |

Resources: MGI (cpfl1 allele), ZFIN (ZDB-PUB-071219-20 for pde6c^w59), OMIA, JAX.

---

## Notes for curating the KB entry

The existing `kb/disorders/PDE6C-Related_Retinopathy.yaml` is a 59-line skeleton. It has a gene, one pathophysiology node with no evidence, and one phenotype. Priorities:

1. Add the phenotypes in the §3 table. Each phenotype's evidence can quote PMID:31826238 or PMID:33001157 after `just fetch-reference`.
2. Build the §6 causal chain as pathophysiology nodes wired to the phenotypes, and consider `conforms_to` against `kb/modules/phototransduction_cascade_dysfunction.yaml`.
3. Record the ClinGen Definitive assertion in `gene_disease_validity`.
4. Add the macaque, cpfl1 mouse and zebrafish models under `animal_models` with `modeled_mechanisms`.
5. Find the PMID for Stearns 2007; it was not resolved in this session.

## Sources
- Thiadens et al. 2009, PMID:19615668 (abstract cached locally); [EUR repository](https://pure.eur.nl/en/publications/homozygosity-mapping-reveals-pde6c-mutations-in-patients-with-ear/)
- Chang et al. 2009 PNAS, PMID:19887631; [PMC2780790](https://pmc.ncbi.nlm.nih.gov/articles/PMC2780790)
- Grau et al. 2011 Hum Mol Genet, PMID:21127010; [PMC3269206](https://pmc.ncbi.nlm.nih.gov/articles/PMC3269206)
- Weisschuh et al. 2018 Hum Mutat, PMID:30080950; [PubMed](https://pubmed.ncbi.nlm.nih.gov/30080950/)
- Georgiou et al. 2019 IOVS, PMID:31826238; [PMC6905659](https://pmc.ncbi.nlm.nih.gov/articles/PMC6905659)
- Daich Varela et al. 2020 IOVS, PMID:33001157
- Bushehri et al. 2020, PMID:32306724; [PMC7275818](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7275818/)
- Moshiri et al. 2019 JCI, PMID:30667376; Ardon et al. 2024 IOVS, PMID:39641747; [OMIA 4146](https://omia.org/4146)
- Trifunović et al. 2010, PMID:20593360; Trifunović et al. 2016, PMID:28172811; Viringipurampeer et al. 2014, PMID:24413151; Kolandaivelu et al. 2011, PMID:21799013
- Deng et al. 2018, PMID:30038560; [PMC6046437](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6046437/)
- Singh et al. 2024 JBC, PMID:38110033; Singh et al. 2025 PNAS, PMID:39739818
- O'Connell et al. 2026, PMID:42525358; Lecigne et al. 2026, PMID:42660982 (no abstract available)
- GeneReviews: Achromatopsia, PMID:20301591 (cached locally)
- [OMIM #613093 mirror](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/commit/16b4b23030b9c25e5a647a69ebd82dc9aecccaad/www.ncbi.nlm.nih.gov/omim/613093); [MedlinePlus PDE6C](https://medlineplus.gov/genetics/gene/pde6c); [PanelApp Australia](https://panelapp-aus.org/panels/3762/gene/PDE6C/)
- [ZFIN pde6c^w59 publication](https://www.zfin.org/ZDB-PUB-071219-20); [zebrafish expression profiling, PMC5726315](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5726315/)
- [Frontiers Mol Neurosci 2018 (rd10/cpfl1)](https://www.frontiersin.org/journals/molecular-neuroscience/articles/10.3389/fnmol.2018.00233/full); [BCM AAV therapeutic window, PMC12036465](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12036465/)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 49 |
| Resolved | 49 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 8 |
| Quoted claims found in source | 6 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 49 |
| On topic | 35 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:31826238` *(abstract only)*: "few or no residual foveal cones"
  - closest text in source: "Nonconfocal adaptive optics scanning light ophthalmoscopy revealed residual foveal cones in only one of two cases"
- `PMID:32306724` *(abstract only)*: "less than 2% of the cases"
  - Text part not found as substring: 'less than 2% of the cases' (note: only abstract available for PMID:32306724, full text may contain this excerpt)

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 42 |
| Resolved | 40 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 1 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000573` (2 mentions) - the report calls it "Cells:** Cone photoreceptors"; CL calls it **retinal cone cell**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `OMIA`.

40 of 42 terms resolved to a current term; the rest could not be looked up either way.