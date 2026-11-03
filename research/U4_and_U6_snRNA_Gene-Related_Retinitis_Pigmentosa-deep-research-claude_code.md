---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-01T23:02:41.374111'
end_time: '2026-11-01T23:05:31.185045'
duration_seconds: 169.81
template_file: templates/disease_pathophysiology_research.md
template_sha: f452f0a9c7e3536175154b9683c45663f686f283
template_variables:
  disease_name: U4 and U6 snRNA Gene-Related Retinitis Pigmentosa
  mondo_id: ''
  category: Mendelian
  causal_genes: RNU4-2, RNU6-1, RNU6-2, RNU6-8, RNU6-9
  omim_id: not recorded
  synonyms: RNU4-2 and RNU6-related retinitis pigmentosa; RNU4- and RNU6-associated
    retinitis pigmentosa; snRNA-related autosomal dominant retinitis pigmentosa
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
  web_search_requests: 4
  num_turns: 9
  total_cost_usd: 1.8911349
  session_id: d98baee9-c229-5d8a-96f8-a4aee10f9c40
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 20
reference_validation:
  total_references: 4
  verified: 4
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 4
  on_topic: 3
  validator_version: 0.4.0
term_validation:
  total_terms: 33
  verified: 32
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 3
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: GO:0045494
    reported_labels:
    - expected `DECREASED
    ontology_label: photoreceptor cell maintenance
  labels_variant: 2
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** U4 and U6 snRNA Gene-Related Retinitis Pigmentosa
- **MONDO ID:**  (if available)
- **Causal gene(s):** RNU4-2, RNU6-1, RNU6-2, RNU6-8, RNU6-9
- **OMIM:** not recorded
- **Synonyms:** RNU4-2 and RNU6-related retinitis pigmentosa; RNU4- and RNU6-associated retinitis pigmentosa; snRNA-related autosomal dominant retinitis pigmentosa
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **U4 and U6 snRNA Gene-Related Retinitis Pigmentosa** covering all of the
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

I've got enough from the primary paper and its preprint, so I'm writing the report now.

# U4 and U6 snRNA Gene-Related Retinitis Pigmentosa: Research Report

**Causal genes:** RNU4-2 (encodes U4 snRNA) and four RNU6 paralogs, RNU6-1, RNU6-2, RNU6-8 and RNU6-9 (each encodes U6 snRNA).
**Category:** Mendelian, autosomal dominant, non-coding RNA genes.

**What this report rests on.**
- Nearly everything here comes from one research group's work (Quinodoz, Rivolta and colleagues), in two versions:
  - a 2025 preprint, PMID:39830270 (PMC11741465);
  - the peer-reviewed paper, *Nature Genetics* 2026;58(1):169–179, PMID:41513982, DOI [10.1038/s41588-025-02451-4](https://doi.org/10.1038/s41588-025-02451-4).
- I read the preprint full text through PMC's BioC service. For the published paper I saw only the abstract. Variant counts come from the preprint unless marked otherwise, and the published counts are higher.
- Abstract wording below is paraphrased or quoted in short fragments. Before any snippet goes into a KB evidence item, fetch it with `just fetch-reference` and check it.
- **I found no independent replication cohort.** Genomics England PanelApp is the only external expert review.

---

## 1. Disease Information

**Overview.**
- This is non-syndromic retinitis pigmentosa (RP) caused by heterozygous variants in RNU4-2 or in four of the five active RNU6 paralogs.
- These genes make the U4 and U6 small nuclear RNAs (snRNAs). The two pair up into the U4/U6 duplex inside the U4/U6.U5 tri-snRNP, a core part of the major spliceosome.
- The preprint abstract says the variants "invariably cluster in close proximity within the three-way junction" of the U4/U6 duplex (PMID:39830270).
- That region binds the tri-snRNP proteins PRPF3, PRPF8 and PRPF31. All three are already known causes of autosomal dominant RP (adRP). So this disease extends the existing "splicing-factor RP" class from proteins to the snRNAs themselves.

**Identifiers.**

| Resource | Status |
|---|---|
| MONDO | No ID supplied, and I found none. Check `just next-stubs` or OLS before binding one. |
| OMIM | None found. The disease was described in 2025–2026, so it may not be catalogued yet. |
| Orphanet | No specific entry found. The parent is RP, ORPHA:791. |
| ICD-10 / ICD-11 | Parent codes only: H35.52 (hereditary retinal dystrophy); ICD-11 9B70 (retinitis pigmentosa). |
| MeSH | Retinitis Pigmentosa, D012174 (parent term). |
| Gene panels | Genomics England PanelApp, Retinal disorders panel 307: RNU6-1, RNU6-2, RNU6-8 and RNU6-9 are listed. RNU6-1 and RNU6-8 are rated green (diagnostic grade). PanelApp Australia lists RNU6-1 on its RP panel. |

**Synonyms:** RNU4-2 and RNU6-related retinitis pigmentosa; RNU4- and RNU6-associated RP; snRNA-related adRP.

**Source of the data:** cohort and family studies — rare-disease genome sequencing, Genomics England 100,000 Genomes, and international inherited-retinal-disease cohorts. There are no EHR-derived data.

---

## 2. Etiology

**What causes it**
- The cause is a heterozygous germline variant in RNU4-2 or in RNU6-1, -2, -8 or -9. The variant is either inherited or arises de novo.
- The variants are small insertions or single-nucleotide changes, all at the U4/U6 three-way junction (see Section 4).

**Genetic risk factors**
- The causal variants are the only known genetic risk factor. I found no data on modifier loci.
- Penetrance is incomplete (Section 9), so modifiers may exist, but none have been identified.

**Environmental risk factors:** none described. This is a monogenic disease.

**Protective factors**
- None established.
- One finding may matter here. RNU6-7, the fifth active U6 paralog, carries no recurrent pathogenic variants. The same n.55_56insG insertion turns up in RNU6-7 in population controls of African ancestry (gnomAD allele frequency 0.014%; All of Us 0.013%).
- The authors propose that RNU6-7 is only minimally incorporated into the spliceosome. This explains why the same variant in that paralog is tolerated; it is not a protective factor in the usual sense (PMID:39830270).

**Gene–environment interactions:** none reported.

---

## 3. Phenotypes

Source: the preprint's clinical summary (PMID:39830270).

| Phenotype | Suggested HPO term (verify every CURIE) | Frequency / features |
|---|---|---|
| Rod–cone dystrophy / RP | HP:0000510 Rod-cone dystrophy | 100% of affected individuals (defining feature) |
| Nyctalopia (night blindness) | HP:0000662 Nyctalopia | Usually the first symptom; adolescence to early adulthood |
| Constriction of peripheral visual field | HP:0001133 Constriction of peripheral visual field | Early symptom, progressive |
| Cystoid macular edema | HP:0011505 Cystoid macular edema | 55.9% |
| Vitreomacular complications (e.g., epiretinal membrane, vitreomacular traction) | e.g., HP:0100014 Epiretinal membrane; check for a more fitting term | 30.6% (preprint lumps these together) |
| Cataract, not age-related | HP:0000518 Cataract | 23.6%. The authors say cataract appears to be more frequent than in many other RP types. |
| Reduced/abnormal ERG | HP:0000512 Abnormal electroretinogram | ERG shows "classical" RP features |
| Fundus findings: bone-spicule pigmentation, attenuated arterioles, waxy disc pallor | HP:0007737 Bone spicule pigmentation of the retina; HP:0007843 Attenuation of retinal blood vessels | Described only as "classical RP features"; no per-sign frequencies |
| Late central vision loss | HP:0000529 Progressive visual loss (and/or HP:0000572 Visual loss) | Occurs "well beyond reproductive age" |

**Characteristics**
- **Onset:** adolescence to early adulthood. This is earlier than most other adRP forms.
- **Severity:** variable. Penetrance is incomplete.
- **Course:** progressive.

**Not part of this disease**
- **Neurodevelopmental features.** These are absent. RP-causing variants give non-syndromic retinal disease, whereas different RNU4-2 variants cause ReNU syndrome (see Section 4).
- **Lab abnormalities.** None.

**Quality of life:** no disease-specific quality-of-life data. Extrapolating from RP in general, expect loss of night and peripheral vision, mobility limits and later reading impairment. Cataract and cystoid macular edema add treatable reductions in vision.

---

## 4. Genetic / Molecular Information

**Causal genes.** HGNC IDs must be looked up with `runoak`/HGNC; I am not quoting them from memory. Use lowercase `hgnc:` in the KB.
- **RNU4-2:** a U4 snRNA gene on chromosome 12q24.31. It is the same gene that causes ReNU syndrome.
- **RNU6-1, RNU6-2, RNU6-8, RNU6-9:** U6 snRNA paralogs.
- **RNU6-7:** no pathogenic variants.
- **RNU4-1** (the other U4 paralog, which lies next to RNU4-2): no pathogenic variants at the two RP hotspots, and 63 likely-benign variants.

### Pathogenic variants

All variants are germline and heterozygous. Counts are from the preprint.

| Gene | Variant | Families / affected individuals (preprint) | Position in the structure |
|---|---|---|---|
| RNU4-2 | n.18_19insA | Index family (8 affected, plus unaffected carriers); 3 more families (15 affected); plus 1 patient from another cohort | Between stem-II and the U4 5′ stem-loop; disrupts base-pairing and changes stem orientation |
| RNU4-2 | n.56T>C | 4 families / 7 individuals, then 4 more families / 5 affected | Disrupts base-pairing in stem-I. The same change at the equivalent site of RNU4-1 (NR_003925.1:n.56T>C) appears in 2 All of Us individuals of unknown phenotype. |
| **RNU4-2 total** | | **13 families, 36 affected** (+27 untested affected relatives) | |
| RNU6-1, -2, -8, -9 | n.55_56insG | **43 families, 89 individuals.** De novo confirmed in 7 sporadic cases; suspected de novo in 12 more pedigrees. | Adds a G–U wobble pair and extends stem-I |
| RNU6-1, -2, -9 | n.56_57insG | 6 families, 10 individuals. One gnomAD v4.1 carrier in RNU6-2. | Same mechanism as n.55_56insG |
| **RNU6 total** | | **49 families, 99 affected** (+112 untested relatives likely carrying the variant) | |

**Updated counts**
- **Preprint total:** 135 individuals, 62 families.
- **Published paper and PanelApp:** 153 individuals, 67 families. PanelApp reports n.55_56insG in 102 individuals from 47 unrelated families.

**Classification and population data**
- **Uncertain or benign variants (preprint):**
  - RNU4-2: 10 VUS and 17 benign variants.
  - RNU6 paralogs: 20 VUS and 70 benign variants.
- **Benign controls that sit right next to the hotspots:**
  - U6 n.55_56insT, with a cumulative gnomAD frequency of 0.12%;
  - U6 n.57T>G, seen in 21 unaffected people.
  - These show that the exact base inserted matters, not just its position.
- **ClinVar / ClinGen:** I did not check ClinVar entries. There is no ClinGen gene-disease validity curation that I could find, so leave `gene_disease_validity` empty.
- **Constraint (gnomAD v4.1):** cumulative allele frequency is 1.2% for RNU4-2 against 20.4% for RNU4-1. RNU4-2 is therefore far less tolerant of variation.

**Functional consequence**
- The variants are thought to act by a dominant-negative or gain-of-function mechanism, not haploinsufficiency (see Section 6).
- For `functional_impact_category`, DOMINANT_NEGATIVE is the authors' leading interpretation. It is inferred from co-IP data, not proven.

**Modifiers, epigenetics, chromosomal changes**
- None reported.
- Chromatin data (ATAC-seq and H3K27ac) show active marks at RNU4-1/-2 and at RNU6-1, -2, -7, -8 and -9. Of the 105 U4 and 1,312 U6 pseudogenes, only RNU4-8P had active marks, which the authors attribute to its proximity to the ACTR1B promoter.
- This explains why only these few loci cause disease.

**How this differs from ReNU syndrome (RNU4-2 neurodevelopmental disorder)**
- **Variant location:** ReNU variants (e.g., n.64_65insT) sit in **stem III**, a separate region of the duplex; RP variants sit at the three-way junction.
- **Transmission:** ReNU variants are mostly de novo, and when inherited they come mostly through the mother. RP variants are mostly inherited, from either parent.
- **Frequency:** ReNU accounts for about 0.4% of neurodevelopmental disorder cases.
- In the co-IP assay, the ReNU variant did **not** produce the increased SART3/PRPF31 binding seen with RP variants (PMID:39830270).
- **Curation point:** keep this RP entry separate from ReNU. They are allelic but distinct diseases.

---

## 5. Environmental Information

Not applicable. There are no environmental, lifestyle or infectious causes.

---

## 6. Mechanism / Pathophysiology

### Causal chain

1. **A heterozygous variant arises** — an insertion or substitution at the U4/U6 three-way junction (U4 n.18_19insA or n.56T>C; U6 n.55_56insG or n.56_57insG). It is present in every cell, but only some cells take part in the disease.
2. **This changes the duplex shape.** It alters base-pairing in stem-I or stem-II, or the stem orientation of the U4/U6 duplex at the junction of stem-I, stem-II and the U4 5′ stem-loop. *Evidence: structural modelling (computational).*
3. **This disturbs the binding surface for PRPF31, PRPF3 and PRPF8.** In tri-snRNP structures, PRPF31 makes hydrogen bonds with 8 duplex residues in this region and PRPF3 with 3. *Evidence: computational, from published cryo-EM structures.*
4. **Mutant snRNPs stall at the U4/U6 di-snRNP stage.**
   - MS2-tagged mutant U4 or U6 expressed in cultured cells pulls down more SART3 and PRPF31 (di-snRNP markers), and somewhat more SNRNP200 (a U5 marker).
   - Benign controls and the ReNU variant do not do this.
   - *Evidence: in vitro (the preprint text does not name the cell line).*
   - *Inferred:* slower recycling or assembly of the tri-snRNP. Because the mutant RNAs sit alongside normal ones, the effect is dominant-negative or gain-of-function.
5. **Inferred: spliceosome capacity becomes limiting in high-demand cells.** No splicing defect has been shown, either globally or for specific transcripts. The authors suggest RP variants are milder than ReNU variants, delaying assembly without measurable pre-mRNA processing defects.
6. **Inferred: rod photoreceptors degenerate, then cones.** This is the same tissue selectivity seen in PRPF31-, PRPF8- and PRPF3-related RP, and is thought to reflect the very high transcriptional and splicing demand of photoreceptors and the RPE.
   - Retina and RPE express much more of these RNAs than choroid: RNU4 about 2.45-fold and RNU6 about 6.24-fold higher.
7. **Clinical result:** night blindness, then loss of peripheral field, then late loss of central vision. Cystoid macular edema and cataract are frequent extras.

**Where the chain branches**
- The disease is either RNU4-2-driven (2 variants) or RNU6-driven (2 variants across 4 paralogs). Both converge on the same assembly intermediate.
- Whether the primary cell injured is the photoreceptor or the RPE is not settled. In PRPF31 RP the RPE is thought to be affected early.

**Suggested GO terms (verify each)**
- Spliceosomal tri-snRNP complex assembly: GO:0000244
- mRNA splicing, via spliceosome: GO:0000398
- U4/U6 snRNP (cellular component): GO:0071001
- U4/U6 x U5 tri-snRNP complex: GO:0046540
- Photoreceptor cell maintenance: GO:0045494 (expected `DECREASED`)
- Retina homeostasis: GO:0001895

**Suggested CL terms**
- Retinal rod cell: CL:0000604
- Retinal cone cell: CL:0000573
- Retinal pigment epithelial cell: CL:0002586

**Molecular profiling:** no transcriptomic, proteomic, single-cell or CRISPR-screen data are specific to this disease.

---

## 7. Anatomical Structures

| Level | Structure | Suggested ontology term |
|---|---|---|
| Organ | Eye / retina | UBERON:0000966 retina |
| Organ | Lens (cataract) | UBERON:0000965 lens of camera-type eye |
| Organ | Macula (cystoid macular edema) | UBERON:0000053 macula lutea |
| Tissue | Photoreceptor layer; RPE | UBERON:0001782 pigmented layer of retina |
| Subcellular | Nucleus / nuclear speckles, Cajal body (snRNP assembly site) | GO:0005634 nucleus; GO:0015030 Cajal body |

**Laterality:** bilateral and largely symmetric (typical of RP; not quantified for this disease).

---

## 8. Temporal Development

- **Onset:** insidious, in adolescence to early adulthood. It is earlier than most adRP forms.
- **Progression:**
  - The course runs from night blindness, to constricted visual fields, to loss of central vision.
  - The pace is slow; central vision is lost late, "well beyond reproductive age".
  - The disease lasts for life.
- **Remission:** none.
- **Critical windows for intervention:**
  - before photoreceptors are lost, for any future therapy;
  - monitoring for cystoid macular edema, which is common and treatable.

---

## 9. Inheritance and Population

- **Inheritance:** autosomal dominant (HP:0000006). There are frequent de novo cases.
  - In the preprint, 67% of cases were inherited, from either parent.
  - De novo origin was confirmed in 7 cases and suspected in 12 more pedigrees.
  - The somatic-mosaicism term does not apply to this disease.
- **Penetrance:** incomplete.
  - 9 obligate carriers had no visual symptoms (4 of them deceased).
  - Non-penetrance was seen in 5 of 13 informative families (38%).
  - Of the living asymptomatic carriers who were examined, one was subclinically affected and one had no signs; three were not evaluated.
- **Expressivity:** variable.
- **Anticipation:** none. These are not repeat-expansion variants.
- **Founder effects:** not described. The U6 n.55_56insG variant recurs in many unrelated families of diverse ancestry, which points to a mutational hotspot, not a founder.
- **Frequency among RP patients:**
  - Preprint estimate: up to about **1.2% of undiagnosed RP** and about **2.7% of undiagnosed adRP families**. The basis was roughly 5,000 RP cases, about 40% undiagnosed, with about 30% of RP being adRP.
  - Published estimate: up to about **1.4%** of otherwise undiagnosed RP.
- **Population prevalence:** not estimated.
  - Parent RP prevalence is about 1 in 4,000. Multiplying this by the diagnostic-yield fraction would be an inference, not a sourced number. **Do not enter a `rate_per_100000`.**
- **Sex ratio:** not reported. Expect it to be equal for an autosomal disease.

---

## 10. Diagnostics

**Genetic testing**
- **Exome sequencing and most standard RP panels miss these variants.** snRNA genes are not exons, and the RNU6 paralogs are short, multi-copy and hard to map uniquely.
- **Recommended:**
  - genome sequencing with snRNA loci deliberately analysed;
  - or targeted sequencing of RNU4-2 and RNU6-1/2/8/9, now on PanelApp's retinal disorders panel 307;
  - **reanalysis of genome data from unsolved adRP and sporadic RP cases.**
- **Read-mapping:** U6 has more than 1,300 pseudogenes, so mapping must be paralog-aware, and confirmation (e.g., by Sanger sequencing with paralog-specific primers) is prudent.
- **Not useful here:** chromosomal microarray, karyotype, FISH and mtDNA testing.

**Clinical tests**
- full-field ERG (rod-cone pattern);
- fundus photography and autofluorescence;
- OCT (cystoid macular edema, ellipsoid zone loss);
- visual fields (Goldmann or static);
- slit-lamp exam for cataract.
- Possible NCIT diagnosis terms: electroretinography, optical coherence tomography (look up CURIEs; do not use from memory).

**Biomarkers:** none.

**Differential diagnosis**
- other adRP genes — especially PRPF31 (which shares incomplete penetrance), PRPF8, PRPF3, SNRNP200 and RHO;
- ReNU syndrome (has neurodevelopmental features);
- syndromic RP (e.g., Usher, Bardet–Biedl);
- phenocopies (drug toxicity, autoimmune retinopathy).

**Screening:** cascade testing of relatives. Unaffected carriers need counselling because of incomplete penetrance.

---

## 11. Outcome / Prognosis

- **Life expectancy:** normal. No mortality is attributable to the disease.
- **Morbidity:** progressive visual disability, with central vision loss late in life. Cystoid macular edema (around 56%) and cataract (around 24%) cause additional, treatable vision loss.
- **Prognostic factors:** none established. Comparisons by variant or gene (RNU4-2 vs RNU6) have not been reported.

---

## 12. Treatment

There is no disease-specific therapy. Management is the same as for RP in general.

| Intervention | Suggested NCIT approach (verify CURIEs) |
|---|---|
| Treating cystoid macular edema with carbonic anhydrase inhibitors (oral acetazolamide, topical dorzolamide) | NCIT:C15986 Pharmacotherapy + `therapeutic_agent` (CHEBI acetazolamide / dorzolamide) |
| Cataract surgery | NCIT:C15329 Surgical Procedure (or a more specific cataract-extraction term after lookup) |
| Low-vision rehabilitation | NCIT:C15315 Rehabilitation |
| Genetic counselling | NCIT:C15240 Genetic Counseling |

**Experimental therapy and trials**
- No trials target this disease.
- Gene augmentation is conceptually unsuitable for a dominant-negative non-coding RNA. Allele-specific knockdown or editing of the mutant snRNA copy is a theoretical approach, but none has been reported.
- Mutation-independent approaches tested in RP generally (e.g., optogenetics, neuroprotection) could in principle apply.

**Pharmacogenomics:** not applicable.

---

## 13. Prevention

- **Primary:** genetic counselling. Each child of a carrier has a 50% chance of inheriting the variant, with incomplete penetrance. Prenatal testing or preimplantation genetic testing is possible once the familial variant is known.
- **Secondary:** cascade testing of relatives. Carriers should be monitored by ophthalmology.
- **Tertiary:** regular OCT to catch cystoid macular edema, and timely cataract surgery.

---

## 14. Other Species

- **Natural animal disease:** none known. I found no entries in OMIA (Online Mendelian Inheritance in Animals).
- **Conservation:** U4 and U6 snRNAs, and the three-way-junction proteins PRPF31, PRPF3 and PRPF8, are highly conserved across eukaryotes from yeast to human. The U6 sequence is among the most conserved snRNAs.

---

## 15. Model Organisms

- **No animal or iPSC models** of RNU4-2 or RNU6 RP have been reported.
- **Only functional model so far:** ectopic expression of tagged mutant snRNA in cultured cells, followed by co-IP (in vitro; cell line not named in the preprint).
- **Related models that could serve as proxies, with caveats:**
  - **Prpf31 mouse models** show weak retinal phenotypes. This is a known human–model mismatch, and a `HUMAN_MODEL_MISMATCH` discussion would be appropriate.
  - **PRPF31 patient iPSC-derived RPE cells and retinal organoids** do recapitulate splicing-factor RP. Equivalent organoids carrying snRNA variants would be the natural next model.
- **Practical difficulty:** RNU6 is multi-copy, so engineering one paralog is hard to do in mouse. Mouse U6 gene organisation differs from human, which is a species-mismatch caveat.

---

## Notes for KB curation

1. Name the disease as an allelic-but-distinct entity from ReNU syndrome. If MONDO has no term, record that and do not reuse the ReNU or generic RP term as an exact match.
2. Use the published paper (PMID:41513982) as the primary citation and the preprint (PMID:39830270) for detail. Fetch both with `just fetch-reference` and quote only text that is in the cache. The full text is in PMC for the preprint, so detailed snippets may need a `--force` full-text fetch.
3. The mechanism nodes after step 4 are inferences. Tag them with `directness: INDIRECT`, or put them under a `mechanistic_hypotheses` entry with `status: EMERGING`.
4. Classify the evidence:
   - co-IP: `IN_VITRO`;
   - structural mapping: `COMPUTATIONAL`;
   - cohort and family data: `HUMAN_CLINICAL`.
5. Bind the inheritance terms HP:0000006 (autosomal dominant) and HP:0003829 (incomplete penetrance). Verify both, as with every CURIE in this report.

## Sources
- Quinodoz M, et al. *De novo and inherited dominant variants in U4 and U6 snRNA genes cause retinitis pigmentosa.* Nat Genet 2026;58:169–179. PMID:41513982. [DOI](https://doi.org/10.1038/s41588-025-02451-4) · [NLK record](https://dev.nlk.cz/mdv/doc/pmid41513982) · [UCL Discovery OA](https://discovery.ucl.ac.uk/id/eprint/10220052/) · [HUJI CRIS](https://cris.huji.ac.il/en/publications/de-novo-and-inherited-dominant-variants-in-u4-and-u6-snrna-genes-/) · [Oxford ORA](https://ora.ox.ac.uk/objects/uuid:2428ce6c-9be2-4dc6-99f4-53199eeff183) · [BIDMC](https://research.bidmc.org/oscar/publications/de-novo-and-inherited-dominant-variants-u4-and-u6-snrna-genes-cause-retinitis) · [UTHealth](https://digitalcommons.library.tmc.edu/uthsph_docs/1336)
- Quinodoz M, et al. *De novo and inherited dominant variants in U4 and U6 snRNAs cause retinitis pigmentosa.* medRxiv 2025. PMID:39830270, [PMC11741465](https://pmc.ncbi.nlm.nih.gov/articles/11741465) · [NLK record](https://dev.nlk.cz/mdv/doc/pmid39830270)
- Genomics England PanelApp, Retinal disorders (panel 307): [RNU6-1](https://panelapp.genomicsengland.co.uk/panels/307/gene/RNU6-1/), [RNU6-2](https://panelapp.genomicsengland.co.uk/panels/307/gene/RNU6-2/), [RNU6-8](https://panelapp.genomicsengland.co.uk/panels/307/gene/RNU6-8/), [RNU6-9](https://panelapp.genomicsengland.co.uk/panels/307/gene/RNU6-9)
- PanelApp Australia: [RNU6-1, panel 137](https://panelapp-aus.org/panels/137/gene/RNU6-1/) · [RNU6-1, RP panel 277](https://panelapp-aus.org/panels/277/gene/RNU6-1/)
- News coverage, January 2026: [News-Medical (1)](https://www.news-medical.net/news/20260109/Non-coding-RNA-mutations-unveiled-as-new-cause-of-retinitis-pigmentosa.aspx) · [News-Medical (2)](https://www.news-medical.net/news/20260109/RNA-gene-mutations-identified-as-cause-of-inherited-blindness.aspx) · [Eyefox / IOB](https://www.eyefox.com/news/2774/a-new-genetic-cause-of-retinitis-pigmentosa-iob-researchers-carlo-rivolta-and-mathieu-quinodoz-identify-non-coding-rna-variants.html)
- Institutional repository records: [Università della Campania](https://iris.unicampania.it/handle/11591/579744) · [Università di Parma](https://air.unipr.it/handle/11381/3047441)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 4 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 33 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 3 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `GO:0045494` (1 mention) - the report calls it "expected `DECREASED"; GO calls it **photoreceptor cell maintenance**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000006` (2 mentions) - the report calls it "Inheritance:** autosomal dominant", "autosomal dominant"; HP calls it **Autosomal dominant inheritance**, and lists "Autosomal dominant" among its other names
- `HP:0003829` (1 mention) - the report calls it "incomplete penetrance"; HP calls it **Typified by incomplete penetrance**, and lists "Incomplete penetrance" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0000006` - called "Inheritance:** autosomal dominant", "autosomal dominant"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.
