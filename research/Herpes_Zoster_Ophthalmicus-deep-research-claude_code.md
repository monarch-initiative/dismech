---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-25T22:37:13.700334'
end_time: '2026-11-25T22:42:22.433498'
duration_seconds: 308.73
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Herpes Zoster Ophthalmicus
  mondo_id: MONDO:0005883
  category: ''
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
  web_search_requests: 5
  num_turns: 15
  total_cost_usd: 0.959310305
  session_id: 77c804c1-9e29-485c-b035-e3d2540fc756
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  tool_calls: 82
  retrieval_calls: 80
  assistant_text_blocks: 1
citation_count: 33
reference_validation:
  total_references: 36
  verified: 36
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 27
  quotes_valid: 27
  relevance_assessed: 36
  on_topic: 28
  validator_version: 0.8.0
term_validation:
  total_terms: 23
  verified: 23
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 9
  labels_matching: 5
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0005883
    reported_labels:
    - MONDO
    ontology_label: ophthalmic herpes zoster
  - term_id: UBERON:0001711
    reported_labels:
    - Skin of the forehead, scalp and eyelid
    ontology_label: eyelid
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Herpes Zoster Ophthalmicus
- **MONDO ID:** MONDO:0005883 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** not recorded
- **Category:** 

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Herpes Zoster Ophthalmicus** covering all of the
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

**Herpes Zoster Ophthalmicus (HZO): Disease Characteristics Report**

**Scope and limits.** HZO (MONDO:0005883 as supplied; I could not retrieve the MONDO record) is an infectious disease, not a Mendelian one. It is caused by reactivation of latent varicella-zoster virus (VZV; *Human alphaherpesvirus 3*) in the ophthalmic (V1) division of the trigeminal nerve. **There is no causal human gene.** Host genetics (HLA region, *HCP5*, *POLR3A* and *POLR3C*) modify susceptibility to zoster or to severe VZV infection only.

How this report was built:
- PubMed article pages were behind a cookie wall, so abstracts were retrieved through NCBI E-utilities (efetch). All quotes are verbatim from those abstracts, and some are fragments.
- I did not retrieve records from Orphanet, OMIM, HPO, GO, CL, UBERON, CHEBI or NCIT. Every ontology ID below is a **suggestion to verify**, not a retrieved fact.
- Background statements that I did not retrieve in this session are marked *[background, not retrieved]*.

---

## 1. Disease Information

- **Definition.** "HZO occurs when the virus involves the ophthalmic division of the trigeminal cranial nerve" (StatPearls, [NBK557779](https://www.ncbi.nlm.nih.gov/books/NBK557779/)).
- **Share of zoster cases.** HZO accounts for about 10–20% of herpes zoster (HZ) cases ([Kalogeropoulos, PMID 27800502](https://pmc.ncbi.nlm.nih.gov/articles/PMC5087099); [Tran 2016, PMID 27067924](https://pmc.ncbi.nlm.nih.gov/articles/PMC4921261)). A 2024 review puts it at 4–20% of HZ ([Litt 2024, PMID 38834857](https://pmc.ncbi.nlm.nih.gov/articles/PMC11219696/)).
- **Rate of eye disease.** Litt 2024 (PMID 38834857): "Approximately 50% of patients with HZO develop ocular disease, among whom up to 25% develop chronic or recurrent disease."

**Identifiers**

| Resource | ID | Status |
|---|---|---|
| MONDO | MONDO:0005883 | As supplied; not verified |
| MeSH | D006563, "Herpes Zoster Ophthalmicus" (introduced 1990; entry terms "Herpes Zoster, Ocular" and "Ocular Herpes Zoster") | [MeSH record](https://meshb.nlm.nih.gov/record/ui?ui=D006563) |
| ICD-10 | B02.3, "Zoster ocular disease" | [gesund.bund.de](https://gesund.bund.de/en/icd-code-suche/b02-3); check against the WHO browser |
| ICD-11, OMIM, Orphanet | Not retrieved | OMIM and Orphanet are not expected to have entries for an infectious disease |

- **Synonyms:** ophthalmic zoster, ocular herpes zoster, zoster ophthalmicus, herpes zoster, ocular.
- **Type of source data:** the evidence below is aggregated disease-level data. It comes from cohorts, claims and electronic health records (EHR), randomized controlled trials (RCTs) and reviews, not from individual patients.

---

## 2. Etiology

**Causal factor.** VZV reactivates from latency in the trigeminal ganglion. "Latent VZV is predominantly located in human ganglionic neurons" and "establishes a latent infection in trigeminal and dorsal root ganglia" ([Kennedy & Cohrs 2010, PMID 20874010](https://pubmed.ncbi.nlm.nih.gov/20874010/)).

**Risk factors**

- **Age.**
  - "The main risk factor for PHN [postherpetic neuralgia] is advancing age" ([Liesegang 2008, PMID 18243930](https://pubmed.ncbi.nlm.nih.gov/18243930/)).
  - HZO incidence is 104.6 per 100,000 person-years at age ≥65, against 30.9 overall ([Borkar 2013, PMID 23207173](https://pubmed.ncbi.nlm.nih.gov/23207173/)).
- **Lifetime zoster risk.** "Herpes zoster affects 20% to 30% of the population at some point in their lifetime" (PMID 18243930).
- **Immunosuppression.** This is a recognized risk factor in reviews (PMID 38834857). I did not retrieve a quantified HZO-specific estimate; an HIV-specific search returned nothing usable.
- **Rising incidence over time.** US HZO incidence "increased 3.6% per year from 1994 to 2018" ([Kong 2020, PMID 31668889](https://pubmed.ncbi.nlm.nih.gov/31668889/)). In Olmsted County, HZ eye involvement rose "23% by decade from 1980 to 2007" ([Yawn 2013, PMID 23664666](https://pmc.ncbi.nlm.nih.gov/articles/PMC3788821)).
- **Factors for recurrent or chronic disease.** Ocular hypertension and uveitis "increased the risk of recurrent and chronic disease" (Tran 2016, PMID 27067924).

**Genetic susceptibility (zoster in general, not HZO-specific)**

- **HLA region / *HCP5*.**
  - A genome-wide association study in "22,981 participants (2280 shingles cases)" found a locus that "tags the non-coding gene HCP5 (HLA Complex P5) in the major histocompatibility complex" ([Crosslin 2015, PMID 25297839](https://pubmed.ncbi.nlm.nih.gov/25297839/)).
  - The eMERGE imputation study replicated an HLA-B association (PMID 30298529).
- ***POLR3A* / *POLR3C*.** "monogenic or digenic POLR3A and POLR3C deficiencies confer increased susceptibility to severe VZV disease" ([Ogunjimi 2017, PMID 28783042](https://pubmed.ncbi.nlm.nih.gov/28783042/)). These cases involved the central nervous system and lungs, not HZO specifically.

**Protective factors.** Vaccination (see §13) and prompt antiviral treatment, which protects against complications (§12). No protective genetic variants were identified.

**Gene–environment interaction.** Not characterized for HZO. A plausible model is that host innate DNA sensing (for example, RNA polymerase III) interacts with age- or immunosuppression-related decline in VZV-specific T-cell immunity. *This is inferred, not demonstrated.*

---

## 3. Phenotypes

HPO IDs are suggestions to verify.

| Phenotype | Suggested HPO | Frequency / characteristics | Source |
|---|---|---|---|
| Dermatomal vesicular rash in V1 (forehead, scalp, eyelid) | Vesicular rash (ID not retrieved) | Defining feature; acute onset | NBK557779 |
| Hutchinson sign (nasal tip / nasociliary lesions) | — | Predicts ocular involvement: OR 6.51 (4.09–10.34); specificity 89.2% | [Mihalache 2026, PMID 41223901](https://pubmed.ncbi.nlm.nih.gov/41223901/) |
| Any ocular disease | — | About 50% of HZO cases | PMID 38834857; PMID 18243930 |
| Uveitis / iritis | Uveitis HP:0000554 | 413/869 (47.6%) of HZO cases | [Meyer 2024, PMID 39307262](https://pubmed.ncbi.nlm.nih.gov/39307262/) |
| Keratitis (epithelial, stromal, disciform) | Keratitis HP:0000491 | Common; recurrent | PMID 35194502; PMID 40048183 |
| Reduced corneal sensation / neurotrophic keratopathy | Corneal ulceration HP:0012804 | Strongly correlated with nerve loss; bilateral nerve changes seen on in vivo confocal microscopy (IVCM) | [Hamrah 2013, PMID 22999636](https://pubmed.ncbi.nlm.nih.gov/22999636/) |
| Ocular hypertension / glaucoma | Glaucoma HP:0000501 | Risk factor for chronicity | PMID 27067924 |
| Ophthalmoplegia (cranial nerve III, IV, VI palsy) | Ophthalmoplegia HP:0000602 | Rare | [Shahriari 2025, PMID 40596424](https://pubmed.ncbi.nlm.nih.gov/40596424/) |
| Acute retinal necrosis (ARN) / progressive outer retinal necrosis (PORN) | Retinal necrosis (ID not retrieved) | Rare; among the most severe complications | PMID 27800502; [Gu 2024, PMID 39141752](https://pubmed.ncbi.nlm.nih.gov/39141752/) |
| Postherpetic neuralgia | Neuralgia (ID not retrieved) | 21% (Borkar); 14% of the ZEDS cohort | PMID 23207173; PMID 40048191 |
| Severe vision loss (≤20/200) | Visual impairment HP:0000505 | 3.3% of eye-involved cases | PMID 23664666 |
| Stroke (later) | Stroke HP:0001297 | 8.1% vs 1.7% in controls | [Lin 2010, PMID 20200348](https://pubmed.ncbi.nlm.nih.gov/20200348/) |

**Corneal nerve loss (Hamrah 2013, PMID 22999636).** Unilateral HZO produced "profound and significant bilateral loss of the corneal nerve plexus." Total nerve length was 595.8 vs 2258.4 μm/frame in controls.

**Quality of life.** PHN is "the most debilitating" sequela (PMID 27800502). Vision loss and chronic disease drive morbidity. No EQ-5D or SF-36 data for HZO were retrieved.

---

## 4. Genetic / Molecular Information

- **Causal genes:** none. There are no pathogenic variants under ACMG criteria, no ClinVar entries, and no chromosomal abnormalities.
- **Susceptibility and modifier genes:**
  - Common variation at *HCP5* / HLA-B (PMID 25297839).
  - Rare *POLR3A* / *POLR3C* deficiency, which causes severe VZV disease. "Leukocytes from all 4 patients tested exhibited poor IFN induction in response to synthetic or VZV-derived DNA" (PMID 28783042).
- **Viral genetics.**
  - Latency involves restricted gene expression: "with expression of gene 63 being the hallmark of latency" (PMID 20874010).
  - The latency-associated transcript (VLT) is "antisense to VZV open reading frame 61 (ORF61)." A VLT isoform "specifically suppresses ORF61 gene expression" ([Depledge 2018, PMID 29563516](https://pubmed.ncbi.nlm.nih.gov/29563516/)).
- **Epigenetics:** host epigenetic data for HZO were not retrieved.

---

## 5. Environmental Information

- **Infectious agent:** VZV, *Human alphaherpesvirus 3* (NCBI Taxon 10335; verify). It is an alphaherpesvirus.
- **Other environmental and lifestyle factors** (smoking, diet, occupation): no HZO-specific evidence was retrieved. Iatrogenic immunosuppression (for example, JAK inhibitors) raises zoster risk generally. In a 1,000-patient tofacitinib series, herpes zoster occurred in 1.5% (PMID 43048738); this was not HZO-specific.

---

## 6. Mechanism / Pathophysiology

**Causal chain**

1. Primary VZV infection (varicella) **leads to** retrograde or hematogenous seeding of sensory ganglia, including the trigeminal ganglion (PMID 20874010).
2. Seeding **results in** lifelong latency in ganglionic neurons. Gene expression is restricted, with ORF63 and VLT expressed and VLT repressing ORF61 (PMIDs 20874010, 29563516).
3. Decline in VZV-specific cell-mediated immunity (age, immunosuppression) **permits** reactivation. CD4 T-cell immunity is critical in the simian varicella virus (SVV) model ([Mahalingam 2019, PMID 31159224](https://pubmed.ncbi.nlm.nih.gov/31159224/)). *The human link is inferred from animal data and epidemiology.*
4. Reactivated virus travels anterogradely along V1 axons, which **results in** dermatomal vesicular rash and acute neuritis (pain).
5. Branch A, nasociliary involvement: this **leads to** ocular-surface and intraocular infection and inflammation. Hutchinson sign predicts this branch (PMIDs 12644941, 41223901).
   - **5a.** Direct viral cytopathic effect on the corneal epithelium **leads to** epithelial (pseudodendritic) keratitis.
   - **5b.** Immune-mediated stromal and uveal inflammation **leads to** stromal or disciform keratitis, iritis or uveitis, and trabeculitis with ocular hypertension or glaucoma (PMIDs 39307262, 27067924). *The immune mechanism is inferred.*
   - **5c.** Damage to corneal sensory nerves **leads to** loss of corneal sensation and then neurotrophic keratopathy, ulceration and scarring (PMID 22999636).
6. Branch B, posterior segment (rare, often in immunocompromised patients): this **leads to** retinitis (ARN/PORN) and **results in** severe vision loss (PMID 27800502).
7. Branch C, neural damage: this **leads to** PHN, which is age-dependent (PMID 18243930), and to cranial nerve palsies (PMID 40596424).
8. Branch D, vascular: VZV spreads into cerebral or temporal arteries, which **leads to** vasculopathy and raises the risk of stroke (HR 4.52; PMID 20200348). VZV antigen was found in "61/82 (74%) GCA-positive TAs compared with 1/13 (8%) normal TAs" ([Gilden 2015, PMID 25695965](https://pubmed.ncbi.nlm.nih.gov/25695965/)); TAs are temporal arteries and GCA is giant cell arteritis. *That VZV causes GCA is proposed, not established.*
9. Untreated or recurrent inflammation **results in** chronic or recurrent disease. Recurrence rates are 8%, 17% and 25% at 1, 3 and 5 years (PMID 27067924).

**Suggested ontology terms (verify)**
- **GO:** viral latency (GO:0019042), reactivation of latent virus (GO:0019046), inflammatory response (GO:0006954), type I interferon production (GO:0032606).
- **CL:** neuron (CL:0000540), sensory neuron (CL:0000101), corneal epithelial cell (CL:0000575), CD4-positive alpha-beta T cell (CL:0000624).

**Molecular profiling.** Metagenomic sequencing and dynamic viral load were used in VZV ARN (PMID 39141752). No transcriptomic, proteomic or single-cell studies specific to HZO were retrieved.

---

## 7. Anatomical Structures Affected

UBERON IDs are suggestions to verify.

- **Primary sites:**
  - Trigeminal ganglion (UBERON:0001675)
  - Ophthalmic nerve (UBERON:0000348)
  - Skin of the forehead, scalp and eyelid (UBERON:0001711)
  - Cornea (UBERON:0000964)
  - Uvea (UBERON:0001768)
- **Secondary sites:**
  - Retina (UBERON:0000966) and optic nerve
  - Extraocular muscles via cranial nerves III, IV and VI
  - Cerebral and temporal arteries
- **Body systems:** nervous, visual and integumentary; vascular when vasculopathy is present.
- **Subcellular:** viral replication in the nucleus (GO:0005634, background).
- **Lateralization:** strictly unilateral, following the dermatome. However, corneal nerve changes are bilateral on IVCM (PMID 22999636).

---

## 8. Temporal Development

- **Onset:**
  - Typically in older adults; the incidence peak is at ≥65 years (PMID 23207173).
  - Acute onset, with a prodrome then rash. *Prodrome detail is background, not retrieved.*
  - Occurs in children, including "immunocompetent children without any identifiable risk factor" (PMID 37822380).
- **Course:**
  - The acute phase lasts weeks. VZV ARN retinitis lasted 5 ± 3 weeks (PMID 39141752).
  - Chronic or recurrent disease affects up to 25% of those with ocular disease (PMID 38834857). Late recurrences reach 25% at 5 years (PMID 27067924).
- **Critical window:** antivirals are "mainly useful in preventing ocular involvement when begun within 72 hours after the onset of the rash" (PMID 27800502). "Prompt antiviral was associated with a lower rate of moderate vision loss among eyes with uveitis" (PMID 39307262).

---

## 9. Inheritance and Population

- **Inheritance:** not applicable (infectious disease). Polygenic susceptibility comes from the HLA region; rare cases involve Mendelian immunodeficiency (*POLR3A* / *POLR3C*).

**Incidence**

| Setting | Incidence | Source |
|---|---|---|
| Kaiser Hawaii | 30.9 per 100,000 person-years; Pacific Islanders 19.0 | PMID 23207173 |
| United States, 1994–2018 | Rose by about 1.1 per 100,000 person-years annually | PMID 31668889 |
| Unvaccinated adults ≥50 | 76.7 per 100,000 person-years | [Lu 2021, PMID 33892049](https://pubmed.ncbi.nlm.nih.gov/33892049/) |

- **Period prevalence:** HZ in any dermatome was 1.1% in a hospital population (PMID 27067924).
- **Share of zoster with eye involvement:** 9.0% (184/2035) of HZ cases had eye involvement (PMID 23664666).
- **Trend by age:** "Since 2008, HZO incidence declined in individuals younger than 21 years and older than 60 years" (PMID 31668889).
- **Sex ratio and geographic distribution:** no HZO-specific data were retrieved.

---

## 10. Diagnostics

- **Clinical diagnosis:**
  - A V1 dermatomal rash is the basis of diagnosis.
  - Hutchinson sign has high specificity but low-certainty evidence: "Very low to low-certainty evidence supports HS as a predictive factor for ocular involvement in HZO" (PMID 41223901).
  - An earlier study found HS "a powerful predictor of ocular inflammation and corneal denervation," with RR 3.35 and 4.02 (PMID 12644941).
- **Eye examination:** slit lamp, intraocular pressure, corneal esthesiometry, and IVCM of the subbasal nerves (PMID 22999636).
- **Laboratory:** VZV PCR of lesion or ocular fluid. For ARN, intraocular viral load and metagenomic next-generation sequencing (PMID 39141752).
- **Imaging:** MRI or vascular imaging when vasculopathy or stroke is suspected *(background)*.
- **Genetic testing:** not routine. Consider an inborn-error-of-immunity workup (for example, *POLR3A* / *POLR3C*) for severe or atypical VZV in young patients (PMID 28783042).
- **Differential diagnosis** *(background)*: herpes simplex keratitis, contact dermatitis, impetigo, preseptal or orbital cellulitis.
- **Screening:** none.

---

## 11. Outcome / Prognosis

- **Mortality:** low. Stroke risk is raised: 8.1% vs 1.7%, HR 4.52 (PMID 20200348).
- **Vision:** 3.3% developed new vision of 20/200 or worse (PMID 23664666). "Eyes with uveitis were more likely to have other ocular complications and loss of vision" (PMID 39307262).
- **Healthcare use:** complications "result in considerable health care use" (PMID 23664666).
- **Prognostic factors:**
  - Age, for PHN.
  - Hutchinson sign.
  - Uveitis and ocular hypertension, for chronicity (PMID 27067924).
  - Timing of antivirals.
- **Biomarkers:** none validated.

---

## 12. Treatment

NCIT terms are suggestions only; IDs were not retrieved.

**Acute antivirals** (NCIT: "Antiviral Agent"; CHEBI: acyclovir, valacyclovir)

- In the 1985 placebo-controlled trial of 55 patients, oral acyclovir "resulted in more prompt resolution of signs and symptoms" and "shortened the duration of viral shedding (P = 0.02)" ([Cobo 1985, PMID 3001610](https://pubmed.ncbi.nlm.nih.gov/3001610/)).
- Litt 2024 (PMID 38834857): "Early recognition and timely treatment with antivirals may prevent ocular complications."

**Suppressive valacyclovir: Zoster Eye Disease Study (ZEDS; NCT03134196)**

- **Design:** 527 participants randomized to valacyclovir 1 g/day or placebo for 12 months ([Cohen 2025, PMID 40048183](https://pubmed.ncbi.nlm.nih.gov/40048183/); [design paper, PMID 35090154](https://pubmed.ncbi.nlm.nih.gov/35090154/)).
- **Primary endpoint:** "primary end points occurred in 86 participants (33%) assigned to placebo and 74 (28%) assigned to valacyclovir." The primary outcome "did not show a benefit."
- **Secondary endpoints:** "treatment superiority at the 18-month end point" and a "reduced number of multiple episodes of keratitis or iritis at both 12 and 18 months."
- **PHN substudy:** 12-month PHN prevalence was not reduced. However, valacyclovir "was associated with a lower dosage of neuropathic pain medication" ([Warner 2025, PMID 40048191](https://pubmed.ncbi.nlm.nih.gov/40048191/)).

**Topical and systemic corticosteroids** (for stromal keratitis and uveitis; background). In zoster ophthalmoplegia, "corticosteroid treatment may be more effective for visual outcomes," and "longer antiviral therapy duration is linked to better extraocular motor outcomes" (PMID 40596424).

**Neurotrophic keratopathy**
- Autologous serum tears: "All patients demonstrated significant nerve regeneration by IVCM within 3-7 months" ([Abazari 2024, PMID 39145285](https://pubmed.ncbi.nlm.nih.gov/39145285/)).
- Caution from the same study: "3 of 4 patients developed stromal keratitis with ulceration within weeks of corneal reinnervation."
- Surgical options (tarsorrhaphy, amniotic membrane, keratoplasty) are background, not retrieved.

**Other areas**
- **PHN management:** neuropathic pain agents (PMID 40048191).
- **Pharmacogenomics:** none established.
- **Gene, cell and RNA therapies:** none.

---

## 13. Prevention

**Primary prevention: vaccination**

- **Recombinant zoster vaccine (RZV, Shingrix; NCIT "Zoster Vaccine Recombinant, Adjuvanted").**
  - Effectiveness against HZO was 89.1% (82.9–93.0%) in adults ≥50 (PMID 33892049).
  - Trial efficacy against all HZ was 89.8% in adults ≥70 ([ZOE-70, PMID 27626517](https://pubmed.ncbi.nlm.nih.gov/27626517/)).
- **Live zoster vaccine (ZVL).**
  - Effectiveness against HZO was 45% overall. It "waned from 71%" in the first year to "29%" at 5–8 years ([Klein 2023, PMID 37940142](https://pubmed.ncbi.nlm.nih.gov/37940142/)).
  - "RZV is more effective than ZVL" (PMID 38834857).
- **Uptake gap:** only 3.7% of eligible adults had two RZV doses in 2018–2019 (PMID 33892049).

**Secondary prevention.** Recognize HZO early and start antivirals within 72 hours. Refer to ophthalmology when Hutchinson sign or eye symptoms are present.

**Tertiary prevention.** Consider one year of suppressive valacyclovir (ZEDS). Monitor intraocular pressure and corneal sensation over the long term.

**Genetic counseling:** not applicable.

---

## 14. Other Species / Natural Disease

- VZV is human-restricted. It is not zoonotic.
- **Comparative disease:** simian varicella virus (SVV) in rhesus macaques (*Macaca mulatta*, NCBI Taxon 9544). Its infection "closely resembles both human primary VZV infection" and reactivation (PMID 31159224).
- **Other animal herpesviruses:** analogous veterinary herpesviral eye diseases exist, such as feline herpesvirus-1 keratitis *(background, not retrieved)*.
- **OMIA:** not applicable.

---

## 15. Model Organisms

- **SVV in rhesus macaques** is the main in vivo model of latency and reactivation. It identified "a critical role for CD4 T-cell immunity" (PMID 31159224).
- **Limitation:** "An understanding of VZV neurotropism in humans has long been hampered by the lack of an adequate animal model" (PMID 31159224).
- **Other models named in the same review:** guinea pig and SCID-hu xenograft models, and in vitro human neuron cultures. *The review was retrieved, but I did not retrieve details for these models.*
- **No HZO-specific ocular model** was identified.
- **Genetic knockout models:** not applicable, beyond host-immunity studies.

---

**Sources:** [Litt 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11219696/) · [Kalogeropoulos](https://pmc.ncbi.nlm.nih.gov/articles/PMC5087099) · [Yawn 2013](https://pmc.ncbi.nlm.nih.gov/articles/PMC3788821) · [Tran 2016](https://pmc.ncbi.nlm.nih.gov/articles/PMC4921261) · [ZEDS JAMA Ophthalmol](https://jamanetwork.com/journals/jamaophthalmology/article-abstract/2830901) · [ZEDS NCT03134196](https://clinicaltrials.gov/study/NCT03134196) · [ZEDS design](https://pubmed.ncbi.nlm.nih.gov/35090154/) · [Lu 2021](https://www.escholarship.org/content/qt8s25h0p5/qt8s25h0p5.pdf) · [MeSH D006563](https://meshb.nlm.nih.gov/record/ui?ui=D006563) · [ICD-10 B02.3](https://gesund.bund.de/en/icd-code-suche/b02-3) · [StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK557779/) · NCBI E-utilities abstracts for all other PMIDs cited above.

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 36 |
| Resolved | 36 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 27 |
| Quoted claims found in source | 27 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 36 |
| On topic | 28 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 23 |
| Resolved | 23 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 9 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0005883` (2 mentions) - the report calls it "MONDO"; MONDO calls it **ophthalmic herpes zoster**
- `UBERON:0001711` (1 mention) - the report calls it "Skin of the forehead, scalp and eyelid"; UBERON calls it **eyelid**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0019042` (1 mention) - the report calls it "GO:** viral latency"; GO calls it **viral latency**
- `CL:0000540` (1 mention) - the report calls it "CL:** neuron"; CL calls it **neuron**