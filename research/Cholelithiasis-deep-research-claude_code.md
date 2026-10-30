---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-30T19:17:15.293324'
end_time: '2026-10-30T19:23:45.916245'
duration_seconds: 390.62
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Cholelithiasis
  mondo_id: MONDO:0012672
  category: Disease
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
  web_search_requests: 1
  num_turns: 23
  total_cost_usd: 2.6730595000000004
  session_id: 07f4758f-171b-5128-8762-a80fdddaf3a5
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  assistant_text_blocks: 4
citation_count: 2
reference_validation:
  total_references: 33
  verified: 33
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 27
  quotes_valid: 25
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:15747383
  - PMID:30504769
  relevance_assessed: 33
  on_topic: 11
  needs_review: true
  validator_version: 0.4.0
term_validation:
  total_terms: 56
  verified: 54
  not_found: 1
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.018
  labels_checked: 4
  labels_matching: 2
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: CHEBI:9907
    reported_labels:
    - PMIDs 37872257, 35704084, 34772614, 18574646
    ontology_label: ursodeoxycholic acid
  labels_variant: 1
  unresolved_terms:
  - RO:0004003
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cholelithiasis
- **MONDO ID:** MONDO:0012672 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** not recorded
- **Category:** Disease

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Cholelithiasis** covering all of the
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

Existing entry exists; this report will extend it. Let me gather sources with verifiable abstracts.

Checking candidate PMIDs against PubMed: five are confirmed, the rest were wrong guesses and are being dropped. Now searching for the missing key papers.

Gathered verified PubMed abstracts for genetics, epidemiology, and prevention trials. Now pulling quotes from the references the existing KB entry already cites, then writing the report.

# Cholelithiasis (MONDO:0012672): research report for the dismech knowledge base

**Scope and identity.** Cholelithiasis means stones in the gallbladder or biliary tree. It is a common disease with many causes, and **no single causal gene is recorded**: MONDO lists no `RO:0004003` causal gene for MONDO:0012672. Its main inherited risk loci are ***ABCG8*** (p.D19H, hgnc:13887) and ***ABCG5*** (hgnc:13886), the hepatic canalicular cholesterol transporter. Other common-variant loci include ***SLC10A2*** (hgnc:10906) and ***UGT1A1*** (hgnc:12530).

The Mendelian form caused by ***ABCB4*** (hgnc:45), low-phospholipid-associated cholelithiasis (LPAC), has its own MONDO class. That class is **gallbladder disease 1, MONDO:0010939**, and it is a child of MONDO:0012672. It sits in the stub queue as `stubs/Gallbladder_Disease_1.yaml`, so it is covered here only as a risk factor.

dismech already has an entry, `kb/disorders/Cholelithiasis.yaml`. It models cholesterol stones only, through five nodes:
- Hepatic Cholesterol Hypersecretion and Biliary Supersaturation
- Mucin-Accelerated Cholesterol Crystal Nucleation
- Gallbladder Hypomotility and Bile Stasis
- Gallstone Growth in the Gallbladder
- Stone Impaction and Biliary Obstruction

The entry's notes say ursodeoxycholic acid (UDCA) was left out for lack of a quotable source. This report points to sources that fill that gap (§12–13).

**How the evidence was checked.** I confirmed every PMID below against PubMed E-utilities in this session, unless it is marked *[unverified]*. Quotes come from PubMed abstracts or the repository's `references_cache/`. Even so, run `just fetch-reference` and `just count-verified-snippets` before any snippet goes into YAML. I took ontology CURIEs from the repository's committed term caches (`cache/*/terms.csv`), not from memory.

---

## 1. Disease information

**Overview.** Gallstones are solid concretions that form in the gallbladder (cholecystolithiasis) or the bile ducts (choledocholithiasis). In Western populations about 80–90% are **cholesterol stones**, made mostly of cholesterol monohydrate crystals. The rest are **black pigment stones** (calcium bilirubinate), seen with chronic haemolysis, cirrhosis and ileal Crohn's disease, and **brown pigment stones**, which form in the ducts with biliary infection.

- "Overall, up to 20% of adults develop gallstones and >20% of those develop symptoms or complications." (PMID:27121416, Lammert et al., *Nat Rev Dis Primers* 2016)
- "For treatment, localization of the gallstones in the biliary tract is more relevant than composition." (PMID:27121416)

**Identifiers**

| System | ID |
|---|---|
| MONDO | MONDO:0012672 *cholelithiasis*. MONDO:0005346 *gallstones* is the precipitate concept, not the clinical condition (the current entry explains this choice) |
| Child (Mendelian) | MONDO:0010939 gallbladder disease 1 / LPAC (*ABCB4*). Its OMIM number is 600803 *[unverified, look it up]* |
| HPO | HP:0001081 Cholelithiasis |
| ICD-10 | K80 (K80.0–K80.8, by site and by whether cholecystitis or cholangitis is present) |
| ICD-11 | DC11 Cholelithiasis *[check against the ICD-11 browser]* |
| MeSH | D002769 Cholelithiasis; D042882 Gallstones *[unverified, look them up]* |
| Orphanet | Common disease, so no Orphanet record. LPAC is ORPHA:69663 *[unverified]* |

**Synonyms.** Gallstone disease (GSD), gallstones, biliary calculi, cholecystolithiasis (gallbladder stones), choledocholithiasis (duct stones, HP:6001269).

**Data provenance.** Most knowledge comes from aggregated, population-level sources: NHANES, ultrasound screening cohorts, twin registries, and GWAS consortia such as UK Biobank, FinnGen and deCODE.

## 2. Etiology

**Causal factors.** No single cause. Disease follows when lithogenic bile meets impaired gallbladder emptying. Lithogenic bile results from hepatic cholesterol hypersecretion, too little bile salt or phospholipid, or a pigment excess. Genetic, metabolic and environmental factors combine to produce both conditions.

**Non-modifiable risk factors**
- "Risk factors for gallstones are female sex, age, pregnancy, physical inactivity, obesity and overnutrition." (PMID:27121416)
- Shanghai population study (n=4,009):
  - age ≥40: OR 3.058
  - family history: OR 2.234
  - waist-to-height ratio ≥0.5: OR 1.656
  - elevated C4: OR 2.232 (C4 is 7α-hydroxy-4-cholesten-3-one, a marker of bile-acid synthesis)
  - Source: PMID:32166900, Song et al., *J Dig Dis* 2020. Quote: "individuals aged ≥40 years (odds ratio [OR] 3.058, 95% confidence interval [CI] 2.110-4.433, P < 0.001)…"
- US NHANES 2017–2020: "female sex, diabetes, liver disease, proton pump inhibitors, abdominal pain, increased age, BMI, and liver stiffness were associated with gallstone disease, and non-Hispanic Black and non-Hispanic Asian race and alcohol were inversely associated." (PMID:36631004, Unalp-Arida & Ruhl, *Hepatology* 2023)

**Modifiable risk factors**
- "Conversely, the modifiable risks for cholesterol gallstones are obesity, rapid weight loss and a sedentary lifestyle." (PMID:22570746, Stinton & Shaffer, *Gut Liver* 2012)
- The metabolic link: "a strong link exists between this disease and highly prevalent metabolic disorders such as obesity, dyslipidemia, type 2 diabetes, hyperinsulinemia, hypertriglyceridemia and the metabolic syndrome." (PMID:26560258, Portincasa et al. 2016)
- Rapid weight loss, including after bariatric surgery: in a meta-analysis of 14 trials, gallstones formed in 38.1% of controls (PMID:37872257).

**Pigment-stone risk factors.** "Diseases like cirrhosis, chronic hemolysis and ileal Crohn's disease are risk factors for black pigment stones." (PMID:22570746)

**Genetic risk factors** (details in §4)
- Twin heritability about 25% (PMID:15747383).
- *ABCG8* D19H: OR about 2.2 overall, 3.3 for cholesterol stones (PMID:17632509).
- The Gilbert variant of *UGT1A1* (PMID:23517300).
- *SLC10A2* missense variants (PMID:30504769).
- 75 GWAS loci in all (PMID:34651315).

**Protective factors**
- Physical activity in men: "multivariate relative risk, 0.58 [95% CI, 0.44 to 0.78]"; "34% of cases of symptomatic gallstone disease in men could be prevented" (PMID:9499324, Leitzmann et al., *Ann Intern Med* 1998).
- Moderate alcohol and non-Hispanic Black or Asian ethnicity were inversely associated in NHANES (PMID:36631004).
- Genetic: ASBT (*SLC10A2*) function. "lower bile acid transport by ASBT is accompanied by greater risk of gallstone disease" (PMID:30504769), so normal enterohepatic bile-acid recirculation protects. One GWAS risk allele lowers hepatic *TMEM147* expression, which implies TMEM147 is protective (PMID:34651315).

**Gene–environment interaction**
- The *ABCG8* D19H effect is stronger with cholesterol stones and in obesity.
- In mice, the oestrogen effect depends on intestinal cholesterol absorption (NPC1L1): ezetimibe "protects against the oestrogen-mediated lithogenic actions on gallstone formation in mice" (PMID:25303682). This makes pregnancy and hormone exposure a G×E axis.
- A twin study (PMID:17908165) related BMI, alcohol and tobacco to symptomatic disease against a shared genetic background. I have the title only and did not read the abstract.

## 3. Phenotypes

| Phenotype | HPO (cache-verified) | Type | Onset / course | Frequency |
|---|---|---|---|---|
| Gallstones (asymptomatic carriage) | HP:0001081 Cholelithiasis | Imaging finding | Adult, rises with age; can stay silent for life | Up to 20% of adults (PMID:27121416); 13.9% of US adults by history (PMID:36631004) |
| Biliary colic (episodic RUQ/epigastric pain) | HP:0002574 Episodic abdominal pain (used in the entry); HP:0002027 Abdominal pain | Symptom | Episodic, often after meals | Most common first symptom. >20% of stone carriers develop symptoms or complications (PMID:27121416) |
| Nausea / vomiting | HP:0002018 / HP:0002013 | Symptom | Accompany colic | Common, frequency not quantified |
| Acute cholecystitis | HP:0001082 Cholecystitis | Complication / sign | Acute | Minority of symptomatic patients |
| Choledocholithiasis | HP:6001269 Choledocholithiasis | Imaging finding | Secondary migration | About 10–20% of symptomatic patients *(textbook range, no PMID verified)* |
| Obstructive jaundice | HP:0000952 Jaundice; HP:0002908 Conjugated hyperbilirubinemia | Sign / lab | Acute | Complication of duct stones |
| Cholestatic enzyme rise | HP:0003155 Elevated circulating alkaline phosphatase concentration | Lab | With duct obstruction | Variable |
| Ascending cholangitis | HP:0030151 Cholangitis; HP:0001945 Fever | Complication | Acute, can be life-threatening | Uncommon |
| Gallstone pancreatitis | HP:0001735 Acute pancreatitis (more specific than the entry's HP:0001733) | Complication | Acute | The leading cause of acute pancreatitis in many series |
| Gallbladder carcinoma (long-term) | none chosen | Late complication | Decades | Rare. Prophylactic cholecystectomy "is not indicated to prevent gallbladder carcinoma (except in cases of porcelain gallbladder)" (PMID:2187558) |
| Comorbid metabolic traits | HP:0001513 Obesity; HP:0000855 Insulin resistance | Risk modifiers | — | — |

**Quality of life.** Biliary colic and its complications cause the acute burden, through emergency visits and hospital admissions. Laparoscopic cholecystectomy is one of the most common abdominal operations. US gallbladder surgery prevalence rose from 6.0% to 11.6% (PMID:36631004). I did not find disease-specific EQ-5D or SF-36 data with verified PMIDs. The GIQLI (Gastrointestinal Quality of Life Index) is the instrument usually used before and after cholecystectomy.

## 4. Genetic and molecular information

**Inheritance.** Multifactorial and polygenic. "Of note, there were no significant sex differences in heritability … genetic effects accounted for 25% (95% CI, 9%-40%)" (PMID:15747383, Swedish twin study of 43,141 pairs).

| Locus / gene | Variant | Effect | Evidence |
|---|---|---|---|
| ***ABCG8*** (hgnc:13887), with ***ABCG5*** (hgnc:13886) | p.Asp19His (D19H, rs11887534) | Probably gain of function: more canalicular cholesterol efflux and biliary cholesterol hypersecretion | GWAS: "overall odds ratio for D19H carriership was 2.2"; "stronger in subjects with cholesterol gallstones (odds ratio = 3.3)" (PMID:17632509, Buch et al., *Nat Genet* 2007). Twins: OR 2.54 (1.33–4.82) (PMID:20497293) |
| ***UGT1A1*** (hgnc:12530) | Gilbert promoter TA repeat (*28) | Partial loss of function, more unconjugated bilirubin, pigment component | "(OR = 1.62, 95% CI 1.00-2.63)"; "These data from Swedish twins confirm the Gilbert variant as risk factor for GD." (PMID:23517300) |
| ***SLC10A2*** (ASBT, hgnc:10906) | Low-frequency missense, e.g. p.Pro290Ser | Loss of function, less ileal bile-acid reabsorption, smaller bile-acid pool | "Pro290Ser: OR = 1.36 [1.25-1.49] … MAF = 1%" (PMID:30504769, Ferkingstad et al., *Nat Commun* 2018, 20 loci) |
| ***ANO1***, ***TMEM147*** (hgnc:21625, hgnc:30414) | Common variants | Smooth-muscle and GI motility (ANO1 is the interstitial-cell-of-Cajal chloride channel). TMEM147 risk allele lowers hepatic expression | "Seventy-five risk loci were identified … of which 46 were new"; top PRS decile "6-fold increased odds" (PMID:34651315, Fairfield et al., *Hepatology* 2022) |
| ***ABCB4*** (MDR3, hgnc:45) | Heterozygous/biallelic missense, truncating, and whole-gene deletions (PMID:21989363) | Loss of function, too little biliary phosphatidylcholine, cholesterol crystals in duct bile | LPAC: "age less than 40 years at onset of symptoms", "recurrence of biliary symptoms after cholecystectomy" (PMID:17562004). This is the separate Mendelian child, MONDO:0010939 |
| Other GWAS candidates | *CYP7A1*, *GCKR*, *SULT2A1*, *ABCB11*, *TM4SF4* | Bile-acid synthesis, glucose/lipid metabolism | Reported in GWAS reviews *[individual PMIDs not verified this session]* |

- **Somatic vs germline.** All the variants above are germline. There is no somatic driver for stone formation.
- **Epigenetics.** No established methylation or histone signature specific to gallstones. Hepatic expression effects (e.g. *TMEM147*) are eQTL findings, not epigenetic ones.
- **Chromosomal abnormalities.** None characteristic.

## 5. Environmental information

- **Diet and lifestyle:**
  - overnutrition, refined carbohydrate, and low fibre
  - physical inactivity (PMID:9499324)
  - rapid weight loss, including very-low-calorie diets and bariatric surgery (PMIDs 37872257, 18574646)
  - prolonged fasting and total parenteral nutrition, which cause gallbladder stasis *(textbook; no PMID verified)*
- **Drugs and hormones:**
  - oestrogens, oral contraceptives and pregnancy
  - fibrates
  - ceftriaxone (biliary pseudolithiasis)
  - somatostatin analogues (octreotide)
  - proton-pump inhibitors, an association in NHANES (PMID:36631004)
  - Only the PPI association has a PMID verified here.
- **Infection.** Brown pigment stones form when bacterial β-glucuronidase deconjugates bilirubin in infected bile (*E. coli*, *Klebsiella*, and in East Asia the liver flukes *Clonorchis sinensis* and *Opisthorchis*). Not relevant to cholesterol stones.
- **Comorbid conditions** (non-genetic): cirrhosis, chronic haemolysis, ileal Crohn's disease or resection (all pigment stones; PMID:22570746), and spinal cord injury.

## 6. Mechanism and pathophysiology

### Ordered causal chain (cholesterol stones)

1. **Initiating metabolic or genetic state.** Obesity, insulin resistance and high caloric intake (environmental), sometimes with gain-of-function *ABCG5/G8* variants, **lead to** hepatic cholesterol hypersecretion into bile. Insulin resistance is thought to upregulate ABCG5/G8 and HMG-CoA reductase while suppressing bile-acid synthesis. *That intermediate is inferred from mouse work and is not directly shown in humans.*
2. **Hypersecretion, or too little bile salt or phosphatidylcholine** (ABCB4 loss of function; ASBT loss of function shrinking the bile-acid pool), **results in** cholesterol-supersaturated bile, with cholesterol saturation index >1.
3. **Supersaturated bile, with pronucleating gallbladder mucin, results in** cholesterol monohydrate crystals precipitating out of unstable phospholipid–cholesterol vesicles (PMID:2210647, gallbladder mucin as a pronucleating agent). Mucin hypersecretion is itself triggered by lithogenic bile and prostaglandins, which forms a positive loop.
4. **Branch: gallbladder hypomotility and stasis.** Excess cholesterol taken up into gallbladder smooth-muscle membranes blunts CCK-receptor signalling and contraction, and fasting, pregnancy and somatostatin add to the stasis. This **gives** crystals time to stay in the gallbladder and aggregate. GWAS motility loci such as *ANO1* (PMID:34651315) support a genetic part to this limb. The causal direction in humans is inferred.
5. **Branch: intestinal factors.** Faster intestinal cholesterol absorption (NPC1L1; PMIDs 18783541, 25303682 in mice) and slow intestinal transit, which raises deoxycholate, **increase** the lithogenic load. Microbiota involvement is emerging and is not well established.
6. **Retained crystals, held in a mucin gel, lead to** macroscopic stone growth.
7. **Most stones stay silent.** "a large majority of patients with such stones will remain asymptomatic" (PMID:2187558).
8. **Stone impaction in the gallbladder neck or cystic duct results in** biliary colic. Persistent obstruction **leads to** gallbladder wall inflammation and acute cholecystitis.
9. **Branch: migration into the common bile duct leads to** obstructive jaundice and cholestasis. Infection of the obstructed bile gives **ascending cholangitis**. Obstruction at the ampulla gives **gallstone pancreatitis**.
10. **Long-term chronic inflammation, including porcelain gallbladder, leads to** a higher risk of gallbladder carcinoma.

### Pigment-stone branch (outside the current entry's scope)
- **Black stones:** haemolysis or ineffective erythropoiesis, sometimes with the *UGT1A1* Gilbert variant, raises unconjugated bilirubin in bile, which precipitates as calcium bilirubinate in the gallbladder.
- **Brown stones:** bacterial deconjugation in stagnant, infected ducts.

### Checklist content for the nodes

| Category | Content | Suggested terms (cache-verified) |
|---|---|---|
| Pathways | Hepatic cholesterol and bile-acid homeostasis (FXR/NR1H4–SHP–CYP7A1 feedback, LXR–ABCG5/G8), enterohepatic circulation | GO:0042632 cholesterol homeostasis; GO:0008206 bile acid metabolic process; GO:0006699 bile acid biosynthetic process; GO:0030301 cholesterol transport; GO:0033344 cholesterol efflux; GO:0032782 bile acid secretion; GO:0015721 bile acid and bile salt transport; GO:0045332 phospholipid translocation (ABCB4) |
| Cellular | Mucin hypersecretion by gallbladder epithelium; failed smooth-muscle contraction | GO:0070254 mucus secretion; GO:0006939 smooth muscle contraction |
| Cell types | Hepatocyte; gallbladder epithelial cell; smooth muscle cell; cholangiocyte; enterocyte (cholesterol absorption) | CL:0000182, CL:1000415, CL:0000192, CL:1000488, CL:0000584 |
| Chemicals | Cholesterol; phosphatidylcholine; bile acids including chenodeoxycholic and ursodeoxycholic acid; oestrogen | CHEBI:16113, CHEBI:64482, CHEBI:16755, CHEBI:9907, CHEBI:50114 |
| Proteins | ABCG5/G8 (overactive), ABCB4/MDR3 (deficient), ABCB11/BSEP, ASBT (deficient), mucins (MUC5AC/MUC5B) | hgnc IDs as in §4 |
| Immune | Low-grade gallbladder inflammation, and acute neutrophilic inflammation in cholecystitis | — |
| Tissue damage | Pressure ischaemia and inflammation of the gallbladder wall; pancreatic autodigestion | — |
| Omics | GWAS: 75 loci, PRS (PMID:34651315). No disease-defining single-cell or spatial dataset found | — |

The research gap is stated in the literature: "the genetic mechanisms that cause supersaturated bile have not been defined yet." (PMID:34367715)

## 7. Anatomical structures

- **Primary:** gallbladder (UBERON:0002110), liver/hepatocytes (UBERON:0002107, the source of lithogenic bile), common bile duct (UBERON:0001174).
- **Secondary:** pancreas (UBERON:0001264; pancreatitis), duodenum (UBERON:0002114; gallstone ileus after fistula), and the ampulla of Vater and cystic duct (no cached UBERON CURIE; look them up before binding).
- **Systems:** digestive (hepatobiliary).
- **Subcellular:** the hepatocyte canalicular membrane (ABC transporters), the ER (cholesterol synthesis, the CYP7A1 bile-acid pathway), and smooth-muscle plasma membrane cholesterol.
- **Laterality:** not applicable (a single midline/right-sided organ).

## 8. Temporal development

- **Onset:** adults, with incidence rising steeply after 40 (PMID:32166900). Pediatric disease is rare and suggests haemolysis, TPN, or an *ABCB4* or *ABCB11* defect. LPAC typically presents before age 40 (PMID:17562004).
- **Pattern:** formation is silent and insidious. Symptoms are episodic.
- **Natural history:** asymptomatic stones carry a low annual risk of symptoms. Gracie & Ransohoff, "The natural history of silent gallstones: the innocent gallstone is not a myth" (PMID:7110244, *NEJM* 1982; abstract not available in this session), is the landmark cohort, with a cumulative symptom rate of about 15–25% over 10–15 years *(figures from secondary sources)*. One small series disagrees: 21.2% developed symptoms over 38 months and "the silent gallstone is not innocent" (PMID:17372404).
- **Stages:** asymptomatic, then symptomatic uncomplicated (colic), then complicated (cholecystitis, choledocholithiasis, cholangitis, pancreatitis).
- **Remission:** cholecystectomy is curative for gallbladder stones. Small cholesterol stones may dissolve with UDCA, but they recur after it is stopped.
- **Windows of risk:** pregnancy and the first months of rapid weight loss, when prophylactic UDCA works (§13).

## 9. Epidemiology and population

- **Prevalence:**
  - Western adults 10–20% (PMID:27121416).
  - US: from 7.4% to 13.9% between 1988–1994 and 2017–2020 (PMID:36631004).
  - Earlier NHANES III: "More than 20 million persons have gallbladder disease in the United States" (PMID:10464139, Everhart et al., *Gastroenterology* 1999).
  - Shanghai: 6.83% (PMID:32166900).
  - Ultrasound is the reference screening method: "The best epidemiological screening method to accurately determine point prevalence of gallstone disease is ultrasonography." (PMID:22570746)
- **Ethnic variation:** highest in Indigenous peoples of the Americas (Pima, Chilean Mapuche) and in Hispanic populations; lower in sub-Saharan African and East Asian populations (PMID:22570746, PMID:10464139; ethnic detail from the full texts).
- **Sex:** female predominance of roughly 2–3:1 in the reproductive years. NHANES III estimated 14.2 million women versus 6.3 million men (PMID:10464139).
- **Mortality associations:** older age, male sex, prediabetes or diabetes, and physical inactivity predicted gallbladder and biliary mortality (PMID:36631004).
- **Genetic architecture:** polygenic, with heritability about 25%. No anticipation, mosaicism, or carrier frequency applies. LPAC follows autosomal dominant inheritance with incomplete penetrance (PMID:31538486).

## 10. Diagnostics

- **Imaging:**
  - **Transabdominal ultrasound** is the first-line test (sensitivity >95% for gallbladder stones). NCIT:C71375 Transabdominal Ultrasound is already in the entry.
  - **MRCP** (NCIT:C113775) and **endoscopic ultrasound** (EUS) for suspected duct stones.
  - **ERCP** (NCIT:C16430) is reserved for therapy.
  - CT is insensitive for cholesterol stones. HIDA scintigraphy is used for acute cholecystitis.
  - The **EASL Clinical Practice Guidelines** (PMID:27085810, *J Hepatol* 2016; PubMed has no abstract, so quote from the PMC full text) set out the diagnostic algorithm, including risk stratification for duct stones.
- **Laboratory:** bilirubin (conjugated), ALP, GGT, ALT/AST, lipase/amylase (pancreatitis), WBC/CRP (cholecystitis, cholangitis).
  - Clinical criteria are the Tokyo Guidelines (TG18) for cholecystitis and cholangitis *[TG18 PMIDs not verified this session]*.
  - Research biomarker: serum C4 (PMID:32166900).
- **Biliary microscopy:** cholesterol crystals in duodenal or bile aspirates. This supports LPAC or microlithiasis.
- **Genetic testing:** not indicated for typical gallstones. ***ABCB4* sequencing and CNV analysis** is indicated for LPAC criteria: onset before 40, recurrence after cholecystectomy, intrahepatic microlithiasis (PMID:17562004, PMID:21989363). Panels for cholestasis (ABCB4/ABCB11/ATP8B1) apply in children. A PRS is a research tool only (PMID:34651315).
- **Differential diagnosis:** peptic ulcer, functional gallbladder disorder, biliary sludge, cholangiocarcinoma or gallbladder cancer, PSC, hepatitis, right lower-lobe pneumonia, myocardial infarction, renal colic.
- **Screening:** population screening of asymptomatic people is not recommended.

## 11. Outcome and prognosis

- **Asymptomatic stones** have a benign course in most people (PMID:2187558, PMID:7110244). "diabetics are at increased risk, as are patients whose stones are detected initially at laparotomy." (PMID:2187558)
- **Mortality:** low overall. Over a median follow-up of 23.3 years there were 72 deaths with gallbladder or biliary tract disease among 18,794 NHANES participants (PMID:36631004). Severe cholangitis and necrotising gallstone pancreatitis drive most deaths.
- **Complications:** acute cholecystitis, empyema or perforation, Mirizzi syndrome, choledocholithiasis, cholangitis, pancreatitis, gallstone ileus, gallbladder carcinoma.
- **After cholecystectomy:** cure is the rule. A minority report persistent symptoms ("post-cholecystectomy syndrome"), and in LPAC the disease recurs in the intrahepatic ducts (PMID:17562004).
- **Prognostic factors:** age, diabetes, stone size and number, duct involvement, and the severity grade of cholecystitis or cholangitis.

## 12. Treatment

| Treatment | Indication / mechanism | Suggested terms | Evidence |
|---|---|---|---|
| **Laparoscopic cholecystectomy** | Symptomatic stones; complicated disease; porcelain gallbladder | NCIT:C51676 Cholecystectomy (in the entry); `therapeutic_modality: SURGERY` | PMID:26560258; PMID:27085810 (EASL) |
| **Expectant management** | Asymptomatic stones | — | "Studies of the natural history of silent gallstones suggest that a large majority of patients with such stones will remain asymptomatic." (PMID:2187558) |
| **ERCP with sphincterotomy and stone extraction**, with EUS or MRCP first | Choledocholithiasis, cholangitis, biliary pancreatitis with obstruction | NCIT:C16430 ERCP | In the entry |
| **Ursodeoxycholic acid (oral dissolution)** | Small (<5–10 mm), radiolucent cholesterol stones in a functioning gallbladder. Lowers cholesterol saturation in bile and allows dissolution. High recurrence after it is stopped | treatment_term NCIT:C15986 Pharmacotherapy; therapeutic_agent CHEBI:9907 ursodeoxycholic acid; SMALL_MOLECULE | Dissolution-efficacy trials were **not read**. Dissolution claims still need their own source (EASL full text, PMID:27085810) |
| **UDCA in LPAC** | ABCB4-related disease | as above | "long-term curative or prophylactic therapy with ursodeoxycholic acid (UDCA) should be initiated early" (PMID:17562004) |
| Extracorporeal shock-wave lithotripsy | Rarely used now; selected solitary stones | (no NCIT CURIE checked) | — |
| Percutaneous cholecystostomy | Acute cholecystitis in patients too ill for surgery | (no NCIT CURIE checked) | Tokyo Guidelines *[unverified]* |
| Supportive care | Analgesia (NSAIDs for colic), antibiotics for cholecystitis or cholangitis, fluids for pancreatitis | NCIT:C15747 Supportive Care | — |
| Experimental | Ezetimibe (NPC1L1 inhibitor) and statins. Ezetimibe prevented stones in mice and reduced biliary cholesterol saturation ("EZET prevented the appearance of cholesterol crystals and gallstones", PMID:18783541); human evidence is limited. FXR and LXR modulators are preclinical | CHEBI:49040 ezetimibe / NCIT:C47529 | Model organism |

- **Pharmacogenomics:** none established.
- **Gene, cell and RNA therapies:** not applicable.

## 13. Prevention

- **Primary prevention:** physical activity (PMID:9499324), avoiding obesity, and gradual rather than rapid weight loss.
- **Chemoprophylaxis during rapid weight loss.** This is the best-supported preventive measure. It needs its own treatment or prevention record in the KB, and it answers the entry's note about UDCA.
  - "Oral UDCA treatment significantly reduces the risks of developing gallstones" — 8.3% vs 38.1%, RR 0.27 (0.18–0.41), 14 trials, 3,619 patients (PMID:37872257, *Obes Surg* 2023).
  - "Prophylactic use of UDCA after bariatric surgery prevents both gallstone formation and symptomatic GD" — gallstone OR 0.25, cholecystectomy OR 0.33 (PMID:35704084, *J Gastroenterol* 2022).
  - 10 RCTs: 24.7% vs 7.3% (PMID:34772614).
  - Earlier meta-analysis: RR 0.43 (PMID:18574646).
  - **Avoid PMID:38229797.** Its abstract reports RR values above 1 that contradict its own conclusion.
- **Secondary prevention:** no screening programme. Incidental stones are managed expectantly.
- **Tertiary prevention:**
  - Cholecystectomy after the first episode of gallstone pancreatitis or cholecystitis, to prevent recurrence.
  - Long-term UDCA in LPAC (PMID:17562004).
- **Genetic counselling:** only for LPAC/ABCB4 families, with autosomal dominant transmission (PMID:31538486).
- **Vaccines:** not applicable.

## 14. Other species

- **Dogs** (*Canis lupus familiaris*, NCBITaxon:9615):
  - Cholelithiasis is uncommon and often incidental.
  - **Gallbladder mucocele** is the main canine gallbladder disease. An *ABCB4* insertion was reported in Shetland Sheepdogs and other breeds, but that association is disputed *[PMID not verified]*.
  - Canine stones are mostly pigment or calcium carbonate rather than cholesterol.
- **Cats:** rare.
- **Cattle and sheep:** mostly pigment stones, from liver-fluke infection (*Fasciola*).
- **Comparative biology:** cholesterol gallstones are mainly a human disease. The cholesterol-transport genes (ABCG5/G8, ABCB4/Abcb4, NPC1L1) are conserved in mammals. **Not zoonotic.**

## 15. Model organisms

- **Lith-gene mice:**
  - Inbred strain differences (C57L/J susceptible, AKR resistant) on a lithogenic diet (high cholesterol and cholic acid) mapped *Lith* QTLs.
  - "Lith genes control mucin accumulation, cholesterol crystallization…" (PMID:12395324).
  - Mouse map and candidate genes (PMID:17087948).
  - Reviews: PMID:20478482 and PMID:34367715.
  - The QTLs include *Lith1* (*Abcb11*) and loci that contain *Abcg5/8*.
  - **Recapitulates** hypersecretion, supersaturation, mucin gel, crystals and stones.
  - **Limitations:** lithogenic diets are supraphysiological (cholic acid), the mouse bile-acid pool is muricholate-rich, and the strain QTLs are not the human GWAS loci.
- **Knockout and transgenic mice:**
  - *Abcb4*⁻/⁻ (*Mdr2*⁻/⁻) models the low-phospholipid bile of LPAC, mainly as cholestatic liver injury and sclerosing cholangitis.
  - *Abcg5/g8*⁻/⁻ and transgenic overexpression show that hepatic ABCG5/G8 controls biliary cholesterol secretion.
  - *Cck* and *Cckar* knockouts show the hypomotility limb.
  - Oestrogen-treated mice show the hormone axis (PMID:25303682).
  - *[Individual knockout PMIDs not verified this session; look them up in MGI.]*
- **Pharmacological models:** ezetimibe prevention in mice (PMIDs 18783541, 25303682). In the KB these would be `modeled_mechanisms` links to the supersaturation node with `relationship: RESCUES`.
- **Other systems:** prairie dog and hamster cholesterol-diet models (historical); in vitro bile models of crystal nucleation, such as the mucin pronucleation assays (PMID:2210647).
- **Resources:** MGI, IMPC, JAX.

---

## Implications for `kb/disorders/Cholelithiasis.yaml`

1. **Add genetics:**
   - `genetic:` rows for *UGT1A1* (PMID:23517300), *SLC10A2* (PMID:30504769) and *ANO1*/*TMEM147* (PMID:34651315), all as `relationship_type: SUSCEPTIBILITY` or `RISK_FACTOR`.
   - Twin-study evidence for the existing *ABCG8* row (PMID:20497293).
   - A polygenic `inheritance` block bound to HP:0010982 (PMID:15747383, PMID:34651315).
2. **Add treatments and prevention:**
   - A UDCA prophylaxis record during rapid weight loss, with `therapeutic_agent` CHEBI:9907 (PMIDs 37872257, 35704084, 34772614, 18574646).
   - UDCA dissolution still needs its own source.
3. **Add a protective environmental factor:** physical activity, `PROTECTS_AGAINST` (PMID:9499324).
4. **Rebinding to consider:** gallstone pancreatitis from HP:0001733 *Pancreatitis* to HP:0001735 *Acute pancreatitis*. Add phenotypes for choledocholithiasis (HP:6001269) and cholangitis (HP:0030151).
5. **Lump/split:** LPAC (MONDO:0010939, *ABCB4*) stays a separate curation target, because it has its own stub. A pigment-stone subtype is still the open question the entry's notes already raise.

### Sources (PubMed, verified this session)
Lammert 2016 PMID:27121416 · EASL CPG 2016 PMID:27085810 · Stinton & Shaffer 2012 PMID:22570746 · Buch 2007 PMID:17632509 · Ferkingstad 2018 PMID:30504769 · Fairfield 2022 PMID:34651315 · Katsika 2005 PMID:15747383 · Katsika 2010 PMID:20497293 · Marschall 2013 PMID:23517300 · Rosmorduc 2007 PMID:17562004 · Pasmant 2012 PMID:21989363 · Miranda-Bautista 2019 PMID:31538486 · Leitzmann 1998 PMID:9499324 · Everhart 1999 PMID:10464139 · Unalp-Arida & Ruhl 2023 PMID:36631004 · Song 2020 PMID:32166900 · Portincasa 2016 PMID:26560258 · Gibney 1990 PMID:2187558 · Gracie & Ransohoff 1982 PMID:7110244 · Jaddou 1996 PMID:17372404 · Sharma 2023 PMID:37872257 · Mulliri 2022 PMID:35704084 · Fearon 2022 PMID:34772614 · Uy 2008 PMID:18574646 · Zúñiga 2008 PMID:18783541 · de Bari 2014 PMID:25303682 · Lammert 2002 PMID:12395324 · Lyons 2006 PMID:17087948 · Wang 2010 PMID:20478482 · Wang 2017 PMID:34367715 · existing entry citation PMID:2210647 (gallbladder mucin pronucleation).

Web: [Fairfield et al. preprint, medRxiv](https://www.medrxiv.org/content/10.1101/2021.07.16.21260637.full.pdf) · [UK Biobank publication record](https://www.ukbiobank.ac.uk/publications/genome-wide-analysis-identifies-gallstone-susceptibility-loci-including-genes-regulating-gastrointestinal-motility/)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 33 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 27 |
| Quoted claims found in source | 25 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 33 |
| On topic | 11 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:15747383` *(abstract only)*: "Of note, there were no significant sex differences in heritability … genetic effects accounted for 25% (95% CI, 9%-40%)"
  - closest text in source: "Of note, there were no significant sex differences in heritability"
- `PMID:30504769` *(abstract only)*: "Pro290Ser: OR = 1.36 [1.25-1.49] … MAF = 1%"
  - closest text in source: "Two distinct low frequency missense variants in SLC10A2, encoding the apical sodium-dependent bile acid transporter (ASBT), associate with an increased risk of gallstone disease (Pro290Ser: OR = 1.36 [1.25-1.49], P = 2.1 × 10-12, MAF = 1%; Val98Ile: OR = 1.15 [1.10-1.20], P = 1.8 × 10-10, MAF = 4%)"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 56 |
| Resolved | 54 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 4 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `CHEBI:9907` (3 mentions) - the report calls it "PMIDs 37872257, 35704084, 34772614, 18574646"; CHEBI calls it **ursodeoxycholic acid**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `RO:0004003` (1 mention) - RO does not contain this term

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0002110` (1 mention) - the report calls it "Primary:** gallbladder"; UBERON calls it **gallbladder**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.