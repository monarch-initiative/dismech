---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-29T18:37:12.232873'
end_time: '2026-10-29T18:42:47.892386'
duration_seconds: 335.66
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Xia-Gibbs Syndrome
  mondo_id: MONDO:0014358
  category: Mendelian
  causal_genes: AHDC1
  omim_id: OMIM:615829
  synonyms: autosomal dominant intellectual disability 25
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
  web_search_requests: 6
  num_turns: 40
  total_cost_usd: 3.2806725999999995
  session_id: d766227f-70b4-5440-ab6b-6f5a6ed9d934
  stop_reason: end_turn
  permission_denials: 7
  denied_tools:
  - Bash
  assistant_text_blocks: 6
citation_count: 14
reference_validation:
  total_references: 42
  verified: 42
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 42
  on_topic: 33
  validator_version: 0.4.0
term_validation:
  total_terms: 95
  verified: 93
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 20
  labels_matching: 18
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0014358
    reported_labels:
    - MONDO
    ontology_label: AHDC1-related intellectual disability - obstructive sleep apnea
      - mild dysmorphism syndrome
  - term_id: NCBITaxon:10090
    reported_labels:
    - Chimeric CRISPR *Ahdc1* mutant mice
    ontology_label: Mus musculus
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Xia-Gibbs Syndrome
- **MONDO ID:** MONDO:0014358 (if available)
- **Causal gene(s):** AHDC1
- **OMIM:** OMIM:615829
- **Synonyms:** autosomal dominant intellectual disability 25
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Xia-Gibbs Syndrome** covering all of the
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

An existing entry exists. Let me read it and find cached AHDC1 refs.

Still gathering sources — reading the cached AHDC1 abstracts before running web searches for gaps.

Pulling the full abstracts of the 2024–2026 papers so I can quote them exactly.

Checking the ontology IDs I plan to suggest against the local term caches.

Pulling phenotype frequencies out of the Khayat 2021 full text, then I'll write the report.

# Xia-Gibbs Syndrome (AHDC1): Research Report for a Knowledge-Base Entry

**Disease:** Xia-Gibbs syndrome (XGS; OMIM #615829; MONDO:0014358)
**Causal gene:** ***AHDC1*** (AT-hook DNA-binding motif-containing 1; HGNC:25230, written `hgnc:25230` in this repository; OMIM *615790; locus 1p36.11)
**Category:** Mendelian, autosomal dominant, almost always *de novo*

All the identifiers above agree. The disease researched here is the AHDC1 disorder. ClinGen classifies AHDC1 for this MONDO ID as **Definitive** (autosomal dominant). Its former OMIM name, "mental retardation, autosomal dominant 25", is a numbered series name and could be confused with other disorders in that series. AHDC1 is the gene to follow.

> **Note for curators:** `kb/disorders/Xia-Gibbs_Syndrome.yaml` already exists (about 1,100 lines, citing the core references below). This report is therefore most useful for augmenting that entry. In particular, the 2024–2026 literature (§2, §3, §4, §6) is mostly not yet cited in it.
>
> **Two kinds of quote appear below.** Quotes marked **[cache]** were copied from `references_cache/` files and are exact. Quotes marked **[PubMed]** are fragments under 120 characters retrieved through a summarising web tool. Re-check those against the abstract before using them as evidence snippets, and run `just fetch-reference PMID:<n>` first.

---

## 1. Disease Information

**Overview.** XGS is a neurodevelopmental disorder. Its main features are:
- hypotonia in infancy;
- global developmental delay, with motor milestones especially late;
- severely limited or absent expressive speech;
- moderate-to-severe intellectual disability;
- structural brain anomalies, most often a thin corpus callosum;
- mild, nonspecific facial dysmorphism.

Variable additional features include obstructive sleep apnea (OSA), movement disorders (ataxia, tremor, bradykinesia), seizures, short stature, scoliosis, strabismus, autism spectrum disorder and laryngomalacia.

- GeneReviews (Murdock et al., PMID:34902026) [cache]: *"The main features of Xia-Gibbs syndrome (XGS), present in a majority of affected individuals, include delayed motor milestones, speech delay with severely limited or absent speech, moderate-to-severe cognitive impairment, hypotonia, structural brain anomalies, and nonspecific dysmorphic features."*
- The discovery paper (Xia et al. 2014, PMID:24791903) [cache]: *"we identified AHDC1 de novo truncating mutations that most likely cause this genetic syndrome."*

**Identifiers**

| System | ID | Status |
|---|---|---|
| OMIM (phenotype) | 615829 (XIGIS; formerly MRD25) | verified |
| OMIM (gene) | 615790 (AHDC1) | verified |
| MONDO | MONDO:0014358 | verified (ClinGen record) |
| Orphanet | ORPHA:412069, "AHDC1-related intellectual disability–obstructive sleep apnea–mild dysmorphism syndrome" | reported by MedGen and the Belgian gentest registry; build the `ORPHA:412069` cache before citing it |
| UMLS / MedGen | C4014419 | from MedGen |
| HGNC | 25230 | verified (ClinGen) |
| ClinGen GDV | CGGV:assertion_59a6c010-…-2021-11-16T170000.000Z — Definitive, AD, ID/Autism GCEP | cached |
| ICD-10 / ICD-11 / MeSH | No disease-specific code found; MeSH indexes these papers under "Abnormalities, Multiple", "Intellectual Disability" and "DNA-Binding Proteins/genetics" | not verified; leave unbound |

**Synonyms:** Xia-Gibbs syndrome; XGS; XIGIS; autosomal dominant intellectual disability 25 (MRD25); AHDC1-related intellectual disability–obstructive sleep apnea–mild dysmorphism syndrome.

**Data provenance:** Most information is aggregated at disease level from case series, the Baylor XGS Registry, GeneReviews, OMIM and Orphanet. There are no EHR-derived cohorts.

**Case counts:**
- more than 270 individuals by 2021 (PMID:34950897 [cache]: *"More than 270 individuals have been diagnosed with XGS worldwide."*);
- more than 390 by 2025 (PMID:39835152 [cache]: *"Whole-exome sequencing has identified more than 390 individuals worldwide with XGS"*).

---

## 2. Etiology

**Primary cause:** heterozygous, usually *de novo*, pathogenic variants in *AHDC1*:
- **Protein-truncating variants (most cases):** nonsense and frameshift variants in the single coding exon.
- **Missense variants:** a minority, clustered in conserved domains (PMID:34950897).
- **Deletions:** whole-gene or partial *AHDC1* deletions and 1p36.11 contiguous deletions (PMID:36054313, PMID:39359946, PMID:30152016).
- **Structural rearrangement:** one *de novo* balanced translocation with a breakpoint in *AHDC1* intron 1, in a boy with a bicuspid aortic valve, aortic coarctation and PDA (Quintero-Rivera et al. 2015, PMID:25574029). The paper's title centres on MATR3; secondary sources attribute the AHDC1 breakpoint to it. Verify before citing.

**Genetic risk factors**
- **Causal:** *AHDC1* is the only established gene.
- **Modifier genes:** none established.
- **Co-occurring diagnoses:** a second Mendelian diagnosis can deepen the phenotype. A Turkish cohort of 5 patients had one with a concurrent *CDK13* diagnosis that explained a more severe presentation (PMID:42136190, 2026).
- **Obstructive sleep apnea:** one study reported rare *AHDC1* variants in patients with OSA (PMID:31737670, Biomed Res Int 2019). This is not established as a susceptibility locus.

**Environmental risk factors:** none known. Parental age has not been shown to matter.

**Protective factors:** none known, genetic or environmental.

**Gene–environment interactions:** none described.

**Parental mosaicism:**
- Maternal germline mosaicism caused recurrence: a prenatal phenotype of hypoplastic corpus callosum recurred in two pregnancies (PMID:31812316, Eur J Obstet Gynecol Reprod Biol 2020).
- Somatic mosaicism in a proband (PMID:34229113 [cache]): *"we present a case of Xia-Gibbs syndrome caused by mosaicism for an AHDC1 variant."*
- "Double mosaicism": two adjacent *de novo* AHDC1 variants lying *in trans* on the same parental haplotype, which implies a post-zygotic origin (PMID:41738116, 2026).

---

## 3. Phenotypes

The two main frequency sources are:
- **Jiang 2018** (PMID:29696776, n=20, registry) [cache full text];
- **Khayat 2021** (PMID:33644933, n=34) [cache]: *"five core phenotypes (delayed motor milestones, speech delay, low muscle tone, ID, and hypotonia) in more than 80% of individuals and an additional 12 features that occurred more variably."*

### Phenotype table

| Phenotype | Suggested HPO (checked in `cache/hp/terms.csv`) | Frequency | Onset / course |
|---|---|---|---|
| Hypotonia | HP:0001252 Hypotonia (or HP:0001290 Generalized hypotonia) | 90% (18/20, Jiang); >80% (Khayat) | Neonatal/infantile; often improves |
| Global developmental delay | HP:0001263 | >80% | Infancy |
| Delayed gross motor development | HP:0002194 | >80%; walking 80% at median 2.5 y (range 1.5–6); all non-walkers male | Infancy |
| Delayed speech and language development | HP:0000750 | >80% | Childhood |
| Absent speech | HP:0001344 | 40% no speech; 20% fewer than 50 words; 30% full sentences (Jiang) | Lifelong |
| Intellectual disability | HP:0001249 | >80%; moderate–severe | Childhood; stable |
| Thin corpus callosum | HP:0033725 (or HP:0002079 Hypoplasia of the corpus callosum) | 6/6 re-reviewed MRIs; 60% abnormal MRI (Jiang); the most frequent finding in the Italian cohort (PMID:42059486) | Congenital; can be seen prenatally |
| Posterior fossa cyst | not found in cache (look up) | several (Jiang) | Congenital |
| Delayed CNS myelination; simplified gyral pattern | HP:0002188; HP:0009879 | OMIM synopsis; rare | Congenital |
| Ataxia | HP:0001251 | 65% (13/20, Jiang) | Childhood/adolescence |
| Tremor; bradykinesia | HP:0001337; HP:0002067 | variable (GeneReviews) | Childhood/adolescence |
| Seizure | HP:0001250 | 30% (Jiang), median onset 4 y (9 mo–12 y); onset 2–9 y in the Italian cohort, with posterior epileptiform EEG discharges activated by sleep | Childhood |
| Obstructive sleep apnea | HP:0002870 (HP:0025267 Snoring) | 45% (9/20); 3 of the 9 used respiratory support | Childhood |
| Laryngomalacia | HP:0001601 | variable | Infancy |
| Strabismus / esotropia | HP:0000486 / HP:0000565 | 40% | Childhood |
| Scoliosis | HP:0002650 | 20% (aged 10–21 y; 3 of 4 operated); more common with truncations in the N-terminal half | Adolescence; progressive |
| Autism / autistic behavior | HP:0000717 / HP:0000729 | 25% had a prior diagnosis; M-CHAT shows substantial overlap | Childhood |
| ADHD; anxiety | HP:0007018; HP:0000739 | variable (GeneReviews) | Childhood |
| Short stature | HP:0004322 | variable; partial GH deficiency in some (PMID:30729726) | Childhood |
| Failure to thrive; feeding difficulties; GERD | HP:0001508; HP:0011968; HP:0002020 | variable | Infancy |
| Dysmorphism: hypertelorism, micrognathia, low-set ears, flat/wide nasal bridge | HP:0000316; HP:0000347; HP:0000369; HP:0005280 / HP:0000431 | common, nonspecific | Congenital |
| Joint hypermobility | HP:0001382 | OMIM synopsis | — |
| Craniosynostosis | HP:0001363 | rare (PMID:30152016; PMID:30858058) | Congenital |
| Aplasia cutis congenita | HP:0001057 | rare (PMID:30152016; PMID:33464633) | Congenital |
| Bicuspid aortic valve | HP:0001647 | rare | Congenital |
| Hearing impairment | HP:0000365 | rare | — |
| Macular dystrophy | HP:0007754 | rare (OMIM) | — |
| Developmental regression | HP:0002376 | associated with variant position in the Brazilian cohort (PMID:40501103) | — |
| Hyperphagia / obesity | look up "Hyperphagia"; HP:0001513 | newly reported as frequent in the Brazilian cohort; mirrors the *Ahdc1*-deficient mouse | — |

**Additional supporting details**
- Sex effect (Jiang 2018 [cache]): *"Data from developmental milestones showed evidence for delayed speech and that males were more severely affected."*
- Neuroimaging (Jiang 2018 [cache]): *"Neuroimaging from six available patients showed an associated thinning of the corpus callosum and posterior fossa cysts."*
- Rare manifestations at a single children's hospital (CHOP, PMID:30152016 [cache]): craniosynostosis, sensorineural hearing loss with a bicuspid aortic valve, cutis aplasia, soft loose skin, and lipoma.
- The Brazilian cohort (n=16) reported three frequent features not described before (PMID:40501103 [PubMed]: *"Three frequent phenotypes, not previously reported, were identified:"*): hyperphagia, male genital anomalies, and Achilles tendon shortening.

**Phenotypic subtypes.** A latent class analysis of 85 published cases (Jiang N et al., Eur J Hum Genet 2025, PMID:39648204) found three classes: an ataxia subtype, a sleep-apnea/short-stature subtype, and a neuropsychological subtype. [PubMed]: *"Age and variant type were identified as predictors of class membership."*

**Psychiatric features.** Challenging behaviour and psychotic-like symptoms have been reported in adolescents (PMID:42366360, 2026; PMID:32816441). An adult natural-history case report exists (PMID:30622101).

**Quality of life.** No EQ-5D, SF-36 or PROMIS studies exist. The largest daily-functioning impacts are:
- lack of speech, which drives communication dependence;
- ID combined with behavioural problems;
- sleep-disordered breathing, which may need CPAP;
- progressive movement disorders and scoliosis in adolescence.

---

## 4. Genetic / Molecular Information

**Gene structure:**
- *AHDC1*, chr1p36.11; NCBI Gene ID for human AHDC1 not checked (look up).
- The whole open reading frame is in **one coding exon**. Pathogenic truncations therefore fall in the last coding exon and are expected to escape nonsense-mediated decay (NMD).
- PMID:39835152 [cache]: *"Notably, only the sixth exon of the AHDC1 gene encodes protein, while the rest are non-coding regions."*

**Protein:** AHDC1/"Gibbin" is a 1,603-aa nuclear protein with AT-hook DNA-binding motifs. Its functional domains are poorly defined (PMID:39835152).

**Variant spectrum**

| Class | Notes | Key PMIDs |
|---|---|---|
| Frameshift / nonsense (de novo) | Most common. Reported positions span about codon 262–1,330. Recurrent p.Cys791Trpfs\*57 (c.2373_2374delTG) in 4/20 registry patients. | 24791903, 29696776, 27148574, 33644933 |
| Missense (de novo) | 10 individuals; a subset cluster in two conserved regions; phenotypes consistent with XGS | 34950897 |
| Whole-gene or 5′ deletions | Support haploinsufficiency | 39359946, 36054313, 30152016, 30615951 |
| Balanced translocation | Breakpoint in intron 1 | 25574029 |
| Mosaic / double mosaic | Somatic and post-zygotic | 34229113, 41738116, 31812316 |

- **Classification:** most variants are ClinVar pathogenic or likely pathogenic under ACMG/AMP criteria (PS2 *de novo*, PVS1). Missense calls need domain-aware *in silico* analysis. PMID:34950897 [cache]: *"de novo missense variants in AHDC1 are likely diagnostic of XGS when in silico analysis of their position relative to conserved regions is considered together with disease trait manifestations."*
- **Population frequency:** pathogenic variants are absent from gnomAD. The gene is highly constrained against loss of function; exact pLI/LOEUF values not retrieved.
- **Origin:** germline, typically *de novo*. Somatic or post-zygotic mosaicism has been documented.
- **Somatic cancer context (not XGS):** AHDC1 appears in Sézary syndrome mutational landscapes (PMID:26415585), medulloblastoma constraint analyses (PMID:37549291) and Ewing sarcoma (PMID:36194562). This is not relevant to XGS causation.

**Functional consequence (contested)**
- **Haploinsufficiency / loss of function:** supported by whole-gene deletions (PMID:39359946) and the original interpretation (Yang 2015, PMID:27148574).
- **Dominant-negative or neomorphic effect of NMD-escaping truncated protein:**
  - Truncated products show abnormal nuclear localisation: a diffuse pattern for the short form and nucleolar aggregation for mid-protein truncations (PMID:33644933 [cache]: *"Transient expression of wild type and different patient truncated AHDC1 protein forms in human cell lines revealed abnormal patterns of nuclear localization including a diffuse distribution of a short truncated form and nucleolar aggregation in mid-protein truncated forms."*).
  - A Japanese cohort gave direct evidence of NMD escape (PMID:41653504 [PubMed]: *"This study provides direct evidence of nonsense-mediated mRNA decay escape."*).
- **Deletion paradox:** in one individual with a deletion, AHDC1 expression was compensated. PMID:36054313 [cache]: *"AHDC1 exhibited a mono-allelic expression pattern with no deficiency in overall AHDC1 expression levels."*

**Genotype–phenotype correlations**
- Truncations in the N-terminal half are associated with seizures and scoliosis (PMID:33644933 [cache]: *"Seizures and scoliosis were more frequently associated with truncations that arise before the midpoint of the protein"*).
- Variant location is associated with epilepsy, scoliosis and regression in the Brazilian cohort (PMID:40501103).
- The same recurrent variant can produce markedly different phenotypes. Two Danish patients share c.2849del (PMID:34229113), and monozygotic twins had discordant epilepsy courses (PMID:35636160).

**Epigenetics:**
- Gibbin loss raises DNA methylation at GATA3-dependent mesodermal genes (PMID:35585237).
- No published blood DNA-methylation episignature for XGS was found. This is a knowledge gap.

**Chromosomal abnormalities:** 1p36.11 interstitial deletions and duplications that include *AHDC1* (PMID:30615951, PMID:28841002, PMID:36054313). Distal 1p36 deletion syndrome and Radio-Tartaglia syndrome (*SPEN*) are the differential diagnoses for this region.

---

## 5. Environmental Information

No environmental, lifestyle or infectious causes or triggers are known. XGS is a purely genetic, developmental disorder. A curator could record a `review_notes` waiver stating that no environmental factor has been reported.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Heterozygous *de novo* *AHDC1* variant (initiating lesion)**
   - Truncating variants in the single coding exon are the commonest; missense variants and deletions also occur.
   - This **leads to** either reduced functional Gibbin (haploinsufficiency) or production of NMD-escaping truncated Gibbin. *(Demonstrated: NMD escape, PMID:41653504; deletions causal, PMID:39359946.)*
2. **The mechanism branches here:**
   - **2a. Truncated Gibbin mislocalises** (diffuse nuclear distribution, or nucleolar aggregation). This **results in** loss of normal chromatin-associated function, and possibly interference with the wild-type allele. *(The localisation is demonstrated in vitro by overexpression, PMID:33644933. Dominant-negative action is inferred, not shown.)*
   - **2b. Reduced Gibbin dosage** (deletions) **results in** the same downstream loss of function. *(Inferred; one deletion showed compensated expression, PMID:36054313.)*
3. **Loss of Gibbin at enhancers and promoters, where it interacts with zinc-finger transcription factors and methyl-CpG-binding proteins, leads to** aberrant gene-specific DNA hypermethylation and disrupted promoter–enhancer contacts.
   - PMID:35585237 [cache]: *"The loss of Gibbin causes an increase in DNA methylation at GATA3-dependent mesodermal genes, resulting in a loss of signalling between developing dermal and epidermal cell types."*
   - *(Demonstrated in hESC/organoid and mouse; neural tissue not yet studied.)*
4. **Dysregulated transcription of lineage-specification genes leads to** abnormal mesoderm maturation and defective signalling between mesoderm and ectoderm. This **results in** patterning defects affecting craniofacial structure, the epidermis and the abdominal wall.
   - These correspond to the dysmorphism, aplasia cutis and craniosynostosis seen in patients.
   - PMID:35585237 [cache]: *"In vivo chimeric CRISPR mouse mutants reveal a spectrum of Gibbin-dependent developmental patterning defects affecting craniofacial structure, abdominal wall closure and epidermal stratification that mirror patient phenotypes."*
5. **Chromatin and transcriptional dysregulation in the developing brain is proposed to lead to** abnormal neurodevelopment: corpus callosum hypoplasia, posterior fossa anomalies and delayed myelination. These in turn **result in** developmental delay, ID, absent speech, autism, seizures and later ataxia or tremor.
   - *(Largely inferred. PMID:39835152 proposes an analogy with MECP2 and ADNP. No neural-specific mechanistic study exists.)*
6. **Branch — airway, tone and growth:**
   - Hypotonia together with upper-airway anomalies (laryngomalacia) **leads to** OSA. *(Clinically inferred.)*
   - Partial GH deficiency in some patients **leads to** short stature (PMID:30729726).
7. **Branch — metabolism:**
   - In mice, *Ahdc1* deficiency **leads to** reduced energy expenditure, then adiposity and obesity with hyperleptinemia, insulin resistance and fatty liver (PMID:37819197 [cache]).
   - This may relate to the hyperphagia reported in humans (PMID:40501103). *(The link is inferred.)*

### Checklist detail

- **Pathways:** GATA3- and p63-dependent epithelial programmes, and mesodermal lineage genes. No canonical signalling pathway (Wnt, MAPK, mTOR) is implicated.
- **Cellular processes:** transcriptional regulation, chromatin organisation, DNA methylation, epidermal stratification.
- **Protein dysfunction:** truncation, mislocalisation and nucleolar aggregation. The Nature 2023 study of phase separation and nucleolar dysfunction in frameshift variants (Mensah et al., PMID:36755093) lists AHDC1 in its gene data, but the relevance is unconfirmed.
- **Metabolic changes:** murine obesity phenotype (above).
- **Immune involvement:** none.
- **Tissue damage:** none. The disorder is developmental, not degenerative, although the movement disorders do emerge later.
- **Omics:**
  - Blood RNA expression of a deletion carrier (PMID:36054313).
  - Gibbin ChIP and interactome, and methylome, in hESC skin organoids (PMID:35585237).
  - No single-cell or spatial studies of neural tissue; no XGS datasets confirmed in GEO. Run `just discover-datasets` before adding any.

**Suggested GO terms (from `cache/go/terms.csv`):**
- GO:0006325 chromatin organization
- GO:0006357 regulation of transcription by RNA polymerase II
- GO:0003677 DNA binding; GO:0003682 chromatin binding
- GO:0007498 mesoderm development
- GO:0008544 epidermis development; GO:0030216 keratinocyte differentiation
- GO:0007420 brain development; GO:0022038 corpus callosum development; GO:0042552 myelination
- GO:0097009 energy homeostasis (mouse)
- *Not in cache, look up:* "DNA methylation" or "regulation of DNA methylation".

**Suggested CL terms:**
- CL:0002322 embryonic stem cell
- CL:0002551 fibroblast of dermis
- CL:0002187 basal cell of epidermis; CL:0000312 keratinocyte
- CL:0000540 neuron; CL:0011020 neural progenitor cell; CL:0000128 oligodendrocyte (inferred)
- CL:0000136 adipocyte (mouse)

---

## 7. Anatomical Structures Affected

- **Primary:** central nervous system.
  - UBERON:0000955 brain; UBERON:0002336 corpus callosum; UBERON:0008788 posterior cranial fossa; UBERON:0002037 cerebellum (ataxia); UBERON:0002316 white matter (myelination).
- **Secondary:**
  - Upper airway (UBERON:0001737 larynx)
  - Musculoskeletal (UBERON:0001130 vertebral column, for scoliosis)
  - Skin (UBERON:0002097 skin of body; UBERON:0002067 dermis)
  - Eye (UBERON:0000966 retina; UBERON:0000053 macula lutea)
  - Cranium and face; endocrine (GH axis); heart (rare BAV/ASD)
- **Subcellular:** GO:0005634 nucleus; GO:0005654 nucleoplasm; GO:0005730 nucleolus (aggregation of mutant protein).
- **Lateralisation:** bilateral and symmetric. Eye asymmetry has been reported once (PMID:38357260).

---

## 8. Temporal Development

- **Onset:** congenital. Corpus callosum hypoplasia can be detected prenatally (PMID:31812316). Hypotonia and feeding problems appear in the neonatal or infantile period.
- **Course:** a static neurodevelopmental disorder overall, with features emerging over time:
  - movement disorders (ataxia, tremor, bradykinesia) in childhood or adolescence;
  - scoliosis at 10–21 years;
  - seizures at a median of 4 years;
  - regression in a subset (PMID:40501103).
- **Duration:** lifelong. Adults have been described (PMID:30622101; the age range widened in Jiang 2018).
- **Critical periods:**
  - early childhood, for speech, communication and AAC therapy;
  - childhood, for sleep-apnea screening;
  - adolescence, for scoliosis and movement-disorder surveillance.
- **Remission:** none.

---

## 9. Inheritance and Population

- **Inheritance:** autosomal dominant (HP:0000006); almost all cases *de novo*.
- **Somatic mosaicism:** documented in probands (PMID:34229113, PMID:41738116), so HP:0001442 is a candidate. Apply the `somatic-mosaicism` skill tiers before binding it, because parental germline mosaicism (PMID:31812316) must not be bound.
- **Penetrance:** presumed complete for truncating variants. **Expressivity:** highly variable, including between identical twins (PMID:35636160).
- **Anticipation:** none. **Founder effects:** none. **Consanguinity:** not relevant. **Carrier frequency:** not applicable.
- **Prevalence:** unknown. There are about 390 or more reported cases worldwide (2025), across many countries: USA, Europe, China, Japan, Brazil, India, Turkey, Iran and the DR Congo. A suitable `prevalence_class` is `NOT_YET_DOCUMENTED`, or `RARE` with `measure_type: CASES_IN_LITERATURE`.
- **Sex ratio:**
  - Roughly balanced: 9 female and 11 male in Jiang 2018.
  - Males may be more severely affected (Jiang 2018), but this is not consistently replicated.
- **Ethnicity:** the registry was 90% White (ascertainment bias). Cohorts are now published from multiple ancestries.

---

## 10. Diagnostics

- **Clinical criteria:** none. Diagnosis is genetic, because the phenotype is nonspecific.
  - Jiang 2018 [cache]: *"making DNA testing and the establishment of molecular diagnosis the primary diagnostic tool for XGS."*
  - GeneReviews [cache]: *"The diagnosis of XGS is established in a proband with suggestive clinical findings and a heterozygous pathogenic variant in AHDC1 that is predicted to lead to a truncated protein, identified by molecular genetic testing"*
- **Genetic testing:**
  - First tier: exome or genome sequencing (trio preferred), or an ID/autism/neurodevelopmental gene panel that includes *AHDC1*.
  - Chromosomal microarray detects 1p36.11 deletions. Genome sequencing detects small intragenic or 5′ deletions (PMID:39359946), and long-read sequencing resolves complex cases (PMID:36054313, PMID:41738116).
  - Low-level mosaicism may need deep sequencing.
  - Karyotype and FISH have little role, except for balanced rearrangements.
- **Imaging:** brain MRI (thin corpus callosum, posterior fossa cysts, ventricular anomalies, delayed myelination).
- **Other tests:**
  - Polysomnography for OSA. Suggested NCIT term: verify "Polysomnography" before binding.
  - EEG.
  - Spine radiographs.
  - Ophthalmology and audiology.
  - GH stimulation testing when growth velocity is poor.
- **Biomarkers:** none. No methylation episignature has been published.
- **Differential diagnosis:**
  - 1p36 deletion syndrome
  - Angelman syndrome (absent speech, ataxia, seizures)
  - Pitt-Hopkins syndrome
  - Prader-Willi syndrome (hypotonia, hyperphagia, OSA)
  - Other chromatin-regulator neurodevelopmental disorders: *ADNP*, *MECP2*, *PRR12* (PMID:38798311), *SPEN*/Radio-Tartaglia (DOI:10.26815/acn.2024.00717)
  - *RNU4-2*-related neurodevelopmental disorder (PMID:38821540)
  - Mitochondrial and connective-tissue disorders, considered in the CHOP series
- **Screening:** no newborn or carrier screening. Prenatal or preimplantation testing is possible once the familial variant is known.

---

## 11. Outcome / Prognosis

- **Survival:** no mortality data. Survival into adulthood is documented (PMID:30622101), and life expectancy is not known to be reduced.
- **Morbidity:**
  - lifelong ID and limited speech;
  - 80% achieve independent walking (median 2.5 y);
  - 90% follow simple commands.
  - Main complications: OSA (45%; some need CPAP), seizures (about 30%), scoliosis (20%, often surgical), movement disorders, behavioural and psychiatric problems.
- **Prognostic factors:**
  - Male sex: possibly more severe.
  - N-terminal truncation: associated with seizures and scoliosis.
  - Age and variant type: predict phenotypic class (PMID:39648204).
- **Recovery:** not applicable. Function improves with therapy, but the core deficits persist.

---

## 12. Treatment

There is **no disease-modifying therapy** and there are no clinical trials. ClinicalTrials.gov shows no XGS-specific registrations; re-check this. Management follows GeneReviews (PMID:34902026), which states [cache]: *"Treatment is symptomatic"*.

| Intervention | NCIT (checked in `cache/ncit/terms.csv`) | Modality | Notes |
|---|---|---|---|
| Speech/language therapy, AAC | NCIT:C159273 Speech Language Therapy | BEHAVIORAL | Core intervention |
| Physical therapy | NCIT:C15302 Physical Therapy | BEHAVIORAL | Hypotonia, motor delay |
| Occupational therapy | NCIT:C121351 Occupational Therapy | BEHAVIORAL | |
| CPAP for OSA | NCIT:C124040 Continuous Positive Airway Pressure | DEVICE | "Many requiring continuous positive airway pressure at night" (Jiang 2018) |
| Adenotonsillectomy | NCIT:C51684 Tonsillectomy with Adenoidectomy | SURGERY | Standard OSA care; not XGS-specific evidence |
| Antiseizure medication | NCIT:C15986 Pharmacotherapy + agent (e.g., CHEBI:6437 levetiracetam) | SMALL_MOLECULE | Standard care; no XGS-specific drug data |
| Growth hormone (in documented GH deficiency) | NCIT:C15986 + therapeutic_agent CHEBI:749556 somatropin / NCIT:C837 Somatropin | PROTEIN_REPLACEMENT | Two patients with partial GHD treated for 24 and 9 months (PMID:30729726); outcome data are limited |
| Spinal fusion for scoliosis | NCIT:C157986 Spinal Fusion | SURGERY | 3 of 4 scoliosis patients operated (Jiang 2018) |
| Melatonin for sleep | CHEBI:16796 melatonin | SMALL_MOLECULE | Typical practice; not XGS-specific evidence |
| Behavioural/psychiatric management | NCIT:C15747 Supportive Care | OTHER | Integrative care case (PMID:42366360) |
| Genetic counseling | NCIT:C15240 Genetic Counseling | BEHAVIORAL | |

- **Anaesthesia:** a latex-free anaesthesia approach was reported for craniosynostosis surgery (PMID:37927632). Airway caution is warranted because of laryngomalacia and OSA.
- **Pharmacogenomics:** none.
- **Gene, RNA or cell therapy:** none. Because the truncated protein may act dominantly, allele-specific silencing would be a theoretical option, but it is entirely speculative.

---

## 13. Prevention

- **Primary prevention:** not possible, because the variants are *de novo*.
- **Recurrence risk:** low, but higher than the population risk because of parental germline mosaicism (PMID:31812316). Prenatal or preimplantation testing can be offered once the variant is known.
- **Tertiary prevention (surveillance, per GeneReviews):**
  - growth and nutrition at every visit;
  - seizures and movement disorders;
  - scoliosis checks until skeletal maturity;
  - annual vision and hearing;
  - sleep and respiratory assessment;
  - GH levels if growth velocity is poor.
- **Vaccines, prophylaxis, public health:** not applicable.

---

## 14. Other Species / Natural Disease

- No naturally occurring animal disease was found in OMIA.
- *AHDC1* is conserved across vertebrates: mouse *Ahdc1* and zebrafish *ahdc1*. Look up NCBI Gene, MGI and ZFIN IDs before binding.
- PMID:24791903 noted that the coding sequence and the 3′ non-coding exons are highly conserved.

---

## 15. Model Organisms

| Model | Phenotype recapitulation | Limitations | PMID |
|---|---|---|---|
| Chimeric CRISPR *Ahdc1* mutant mice (NCBITaxon:10090) | Craniofacial, abdominal wall and epidermal stratification defects that "mirror patient phenotypes" | Chimeric; neural and behavioural phenotypes not reported | 35585237 |
| *Ahdc1*-deficient mouse line | Adiposity from weaning, obesity, reduced energy expenditure, hyperleptinemia, insulin resistance, fatty liver | Neurodevelopmental phenotype not characterised; obesity is not a core human feature | 37819197 |
| Zebrafish *ahdc1* 4-bp insertion (CRISPR; NCBITaxon:7955) | Fertile; Mendelian ratios; phenotype not yet described | Not yet phenotyped; deposited in ZFIN | 37054903 |
| Patient iPSC lines (3 LoF variants; hpscreg.eu) | Pluripotent; trilineage-competent | No disease phenotype reported yet | 37054903 |
| Patient iPSC line FDCHi010-A (c.2062C>T) | Resource only | Not phenotyped | 37216737 |
| Gibbin-mutant hESC-derived skin organoids | Lack dermal maturation; defective keratinocyte stratification; GATA3-target hypermethylation | Skin rather than brain | 35585237 |
| Transient overexpression in human cell lines | Mislocalisation and nucleolar aggregation of truncated forms | Supraphysiological expression | 33644933 |

- **Applications:** chromatin and methylation mechanism, epithelial and craniofacial patterning, metabolic regulation, and iPSC-derived neural models (not yet published).
- **Model–human mismatch:** no model yet recapitulates the core neurodevelopmental phenotype (ID, absent speech, thin corpus callosum). This would be a good `HUMAN_MODEL_MISMATCH` or `KNOWLEDGE_GAP` discussion.

---

## Key Knowledge Gaps

1. Whether XGS is caused by haploinsufficiency, by a dominant-negative effect of NMD-escaping protein, or by both (allelic heterogeneity). The deletion data and the NMD-escape data point in different directions.
2. Gibbin's neural targets. No brain-specific ChIP, methylome or single-cell data exist.
3. No blood DNA-methylation episignature, which would help classify missense VUS.
4. No natural-history or prevalence data, and no quality-of-life instruments.
5. The hyperphagia and obesity link between the mouse and the Brazilian cohort needs confirmation.

---

## Key References

| PMID | Citation | Type |
|---|---|---|
| 24791903 | Xia F et al. *Am J Hum Genet* 2014. Discovery paper | Human clinical |
| 27148574 | Yang H et al. *Cold Spring Harb Mol Case Stud* 2015. Seven additional cases | Human clinical |
| 29696776 | Jiang Y et al. *Am J Med Genet A* 2018. XGS Registry phenotypic spectrum | Human clinical |
| 30152016 | Gumus E et al. *Am J Med Genet A* 2018. CHOP series | Human clinical |
| 33644933 | Khayat MM et al. *Hum Mutat* 2021. n=34; protein localisation | Human clinical + in vitro |
| 34950897 | Khayat MM et al. *HGG Adv* 2021. Missense variants | Human clinical + computational |
| 34229113 | Danish cohort, *Eur J Med Genet* 2021. Mosaicism | Human clinical |
| 34902026 | Murdock D et al. *GeneReviews* 2021 | Review / baseline |
| 35585237 | Collier A et al. *Nature* 2022. Gibbin and DNA methylation | In vitro / model organism |
| 36054313 | Chander V et al. *Hum Mutat* 2022. Deletions; long-read sequencing | Human clinical |
| 37054903 | Carvalho LML et al. *Gene* 2023. iPSC and zebrafish | Model resources |
| 37819197 | *Am J Physiol Endocrinol Metab* 2023. *Ahdc1* mouse obesity | Model organism |
| 39359946 | *Mol Syndromol* 2024. Genome-sequencing deletions | Human clinical |
| 39648204 | Jiang N et al. *Eur J Hum Genet* 2025. Latent class subtypes (n=85) | Computational/clinical |
| 39835152 | Li et al. *Front Neurol* 2025. Gibbin chromatin review | Review |
| 40501103 | Sennes MGS et al. *Clin Genet* 2025. Brazilian cohort (n=16) | Human clinical |
| 40844525 | *Hum Genet* 2025. AHDC1 molecular-features review | Review |
| 41653504 | Shirai H et al. *Brain Dev* 2026. Japanese cohort; NMD escape | Human clinical |
| 41738116 | *Am J Med Genet A* 2026. Double mosaicism | Human clinical |
| 42059486 | Cinelli G et al. *Am J Med Genet A* 2026. Italian cohort (n=15) plus systematic review | Human clinical |
| 42136190 | *Dev Neurobiol* 2026. Turkish cohort | Human clinical |
| 30729726 | Cheng X et al. *Mol Genet Genomic Med* 2019. Partial GH deficiency | Human clinical |
| 31812316 | *Eur J Obstet Gynecol Reprod Biol* 2020. Maternal germline mosaicism | Human clinical |
| CGGV:assertion_59a6c010… | ClinGen GDV, Definitive (2021-11-16) | Structured source |

## Sources

- [PubMed AHDC1 search](https://pubmed.ncbi.nlm.nih.gov/?term=AHDC1)
- [Jiang N 2025, latent class analysis (PMID 39648204)](https://pubmed.ncbi.nlm.nih.gov/39648204/)
- [Sennes 2025, Brazilian cohort (PMID 40501103)](https://pubmed.ncbi.nlm.nih.gov/40501103/)
- [Shirai 2026, Japanese cohort (PMID 41653504)](https://pubmed.ncbi.nlm.nih.gov/41653504/)
- [Yang 2015 (PMID 27148574)](https://pubmed.ncbi.nlm.nih.gov/27148574/)
- [Cheng 2019, GH deficiency (PMID 30729726)](https://pubmed.ncbi.nlm.nih.gov/30729726/)
- [AHDC1/Gibbin review, Front Neurol 2025 (PMC11743279)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11743279/)
- [AHDC1 missense mutations (PMC8694554)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8694554/)
- [MedGen C4014419](https://ncbi.nlm.nih.gov/medgen/C4014419)
- [Belgian gentest registry, ORPHA 412069](https://gentest.healthdata.be/disease/2502)
- [OMIM 615829 mirror](https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/615829)
- [Cinelli 2026, Italian cohort (IRIS Unimore)](https://iris.unimore.it/handle/11380/1406570)
- [Polish case report, aplasia of the scalp](https://www.termedia.pl/Diagnostic-and-clinical-approach-to-a-paediatric-patient-with-skin-aplasia-of-the-head-as-a-rare-manifestation-of-Xia-Gibbs-syndrome-caused-by-a-new-potentially-pathogenic-de-novo-mutation-in-the-AHDC,127,55842,0,1.html)
- [Wikipedia: Xia–Gibbs syndrome](https://en.wikipedia.org/wiki/Xia%E2%80%93Gibbs_syndrome)
- Local `references_cache/` files for PMIDs 24791903, 29696776, 30152016, 33644933, 34229113, 34902026, 34950897, 35585237, 36054313, 37054903, 37819197 and 39835152, plus the ClinGen CGGV record

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 42 |
| Resolved | 42 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 42 |
| On topic | 33 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 95 |
| Resolved | 93 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 20 |
| Terms named correctly | 18 |
| Terms named as a **different** term | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014358` (2 mentions) - the report calls it "MONDO"; MONDO calls it **AHDC1-related intellectual disability - obstructive sleep apnea - mild dysmorphism syndrome**
- `NCBITaxon:10090` (1 mention) - the report calls it "Chimeric CRISPR *Ahdc1* mutant mice"; NCBITaxon calls it **Mus musculus**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.