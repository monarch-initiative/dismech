---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-11-11T22:37:38.450262'
end_time: '2026-11-11T22:57:03.455076'
duration_seconds: 1165.0
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Postinfectious Cerebellitis
  mondo_id: MONDO:0850107
  category: Autoimmune
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
  - claude-haiku-4-5-20251001
  - claude-opus-5[1m]
  web_search_requests: 36
  num_turns: 100
  total_cost_usd: 10.315798999999998
  session_id: d11f4297-d87a-4563-94b6-bdbc8ac62feb
  stop_reason: end_turn
  permission_denials: 4
  denied_tools:
  - Bash
  assistant_text_blocks: 2
citation_count: 35
reference_validation:
  total_references: 47
  verified: 44
  not_found: 3
  unverifiable: 0
  confabulation_rate: 0.064
  relevance_assessed: 44
  on_topic: 35
  unresolved_references:
  - PMID:33457189
  - PMC:PMC12420292
  - PMC:PMC6978293
  needs_review: true
  validator_version: 0.5.1
term_validation:
  total_terms: 142
  verified: 139
  not_found: 1
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.007
  labels_checked: 19
  labels_matching: 15
  labels_variant: 4
  unresolved_terms:
  - RO:0004003
  obsolete_terms:
  - term_id: GO:0070997
    ontology_label: obsolete neuron death
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Postinfectious Cerebellitis
- **MONDO ID:** MONDO:0850107 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** not recorded
- **Category:** Autoimmune

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Postinfectious Cerebellitis** covering all of the
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

I'll research this now. Loading web tools first.

# Research Report: Postinfectious Cerebellitis (MONDO:0850107)

**Prepared:** 11 November 2026 · **Target concept:** MONDO:0850107 *postinfectious cerebellitis* · **Causal gene: none — this is a non-Mendelian, immune-mediated acquired disorder.**

---

## 0. Scope note, and how to read the citations

**This disease has no causal gene.** The research template asks for causal gene(s), OMIM entry, variant classification, inheritance pattern, penetrance and carrier frequency. None of those apply: postinfectious cerebellitis is an acquired, immune-mediated inflammatory syndrome of the cerebellum triggered by an antecedent infection (rarely a vaccination). MONDO records no `RO:0004003` causal gene for MONDO:0850107, there is no OMIM entry, and MedGen types it only as "Disease or Syndrome". Sections 4 and 9 below are therefore answered with what *is* true (candidate autoantigens, HLA/immunogenetic data, epidemiology) and with explicit statements of non-applicability where the template presumes a Mendelian architecture. Do not let a serial-numbered-disease heuristic pull this entry toward a gene — there isn't one to find.

**Verification tags.** Every quotation below carries a tag saying how strongly it is sourced, because the project rule is that a research report's quotes are *leads*, not evidence:

| Tag | Meaning |
|---|---|
| **[V]** | Verbatim abstract text pulled this session from NCBI E-utilities (`efetch`, `retmode=xml`). Highest confidence. Still must be re-verified against a committed `references_cache/` file via `just fetch-reference` before it enters a `snippet:`. |
| **[P]** | Extracted through a summarising fetch of a publisher or PMC page. The wording may have been smoothed. **Re-read the source before quoting.** |
| **[S]** | Seen only in a search-engine summary; the primary source was not opened. A lead only — never cite from this. |

Every CURIE in this report was read from a source in this session (the repository's `cache/<prefix>/terms.csv` files, the EBI OLS4 API, or the HGNC REST API). CURIEs I could **not** resolve are listed explicitly in §16 as outstanding lookups rather than guessed.

---

## 1. Disease Information

### 1.1 Overview

Postinfectious cerebellitis is an immune-mediated inflammatory syndrome of the cerebellum that begins after a latent interval following an infection — most often a common childhood viral illness — or, rarely, after a vaccination. It is the commonest cause of acute ataxia in children. Clinically it spans a severity continuum: a pure, self-limiting cerebellar syndrome with normal imaging at one end, through a cerebellitis with MRI-visible cerebellar inflammation and extracerebellar features, to a rare fulminant form in which cerebellar swelling obstructs the fourth ventricle and threatens life.

The authoritative one-line definition is Orphanet's, served through MedGen:

> "A rare cerebellar ataxia characterised by cerebellar inflammation caused by viral or bacterial infection-triggered, immune-mediated mechanisms." **[P]** — ORPHA:624244, via MedGen C5575321 (https://www.ncbi.nlm.nih.gov/medgen/1843009)

The most current synthesis of the whole concept is a 2026 PRISMA systematic review, whose opening sentences define the spectrum precisely:

> "Post-infectious cerebellitis is an immune-mediated cerebellar inflammatory syndrome that follows a preceding infection (or, rarely, vaccination) after a latent interval. It spans a spectrum from benign post-infectious/acute cerebellar ataxia (ACA) through more severe acute cerebellitis (AC) with leptomeningeal enhancement and mass effect, to rare, life-threatening acute fulminant cerebellitis (AFC) with hydrocephalus risk." **[V]** — Gowda N, Harish S, Joy J, Tej G. *Cerebellum* 2026;25(5):134. PMID:42649322, doi:10.1007/s12311-026-02074-3

### 1.2 The nomenclature problem — and why it matters for a KB entry

Three overlapping names are in circulation and they are **not** synonyms in every author's hands:

| Term | What it denotes in the strict usage |
|---|---|
| Acute postinfectious cerebellar ataxia (APCA / ACA) | A **pure** cerebellar syndrome, usually with a normal MRI, no headache/vomiting, benign course |
| Acute cerebellitis (AC) | MRI evidence of predominantly **cerebellar inflammation**, usually with extracerebellar features (headache, vomiting, meningism), leptomeningeal enhancement, mass effect |
| Acute fulminant cerebellitis (AFC) | AC plus diffuse swelling, fourth-ventricular obstruction, hydrocephalus, herniation risk |

> "Acute postinfectious cerebellar ataxia is a pure cerebellar syndrome often with normal MRI at onset, while acute cerebellitis denotes an infection that directly affects the cerebellum often with abnormal magnetic resonance imaging (MRI) and with symptoms and signs beyond a pure cerebellar syndrome." **[S]**

> "Some authors feel that acute cerebellitis and acute postinfectious cerebellar ataxia are, in fact, a spectrum of the same disease." **[S]**

The decisive clinical discriminator reported in the literature is the presence of extracerebellar symptoms:

> "The diagnosis of acute cerebellitis rather than acute postinfectious cerebellar ataxia should be considered when headache and vomiting accompany ataxia in a child." **[V]** — Yildirim M, Gocmen R, Konuskan B, Parlak S, Yalnizoglu D, Anlar B. *J Child Neurol* 2020;35(6):380-388. PMID:32160830, doi:10.1177/0883073820901407

**Recommendation for the KB:** MONDO:0850107 is the correct anchor for the whole spectrum (MedGen lists `Acute cerebellar ataxia`, `Acute postinfectious cerebellar ataxia`, `APCA`, `ACA`, `PIC`, `Post-infectious cerebellitis` and `Para-infectious cerebellitis` all as aliases of this one concept). The three severity tiers — ACA, AC, AFC — are the natural `has_subtypes` rows, because Gowda 2026 classifies its whole pooled cohort by exactly those three and reports subtype-specific outcomes. One caution: **"para-infectious" is listed as a synonym by MedGen but is used as a *contrast* by at least one series**, where the para-infectious group had a significantly shorter latency (p=0.001) and more frequent concurrent fever (p=0.02) than the post-infectious group **[S]** (Tunisian series, *Mult Scler Relat Disord* 2023). A `notes:` line recording that the concept lumps what some authors split would be honest.

### 1.3 Identifiers

| Resource | Identifier | Source read this session |
|---|---|---|
| MONDO | **MONDO:0850107** — label `postinfectious cerebellitis` | OLS4 API |
| Orphanet | **ORPHA:624244** | MONDO xref; MedGen |
| UMLS | **C5575321** | MONDO xref; MedGen |
| MedGen | **1843009** | MONDO xref; MedGen page |
| GARD | **0022502** / 22502 | MONDO xref; MedGen |
| SNOMED CT | **1366187006** | MedGen |
| MalaCards | `postinfectious_cerebellitis` | MONDO `curated content resource` |
| OMIM | **none** (not a Mendelian disorder) | — |
| MeSH | **no exact term identified.** Closest indexing concepts are *Cerebellar Ataxia* and *Encephalitis*; nothing in MedGen's xref block gives a MeSH ID | MedGen (MeSH "not explicitly listed") |
| ICD-10 | **no specific code identified.** Coding in practice falls to generic ataxia/encephalitis codes | Orphanet page unreachable (DNS failure on `orpha.net`); ICD-10-CM search of the repo cache returned nothing relevant |
| ICD-11 | **no specific code identified.** `8A44` is *leukodystrophies* (Pelizaeus-Merzbacher, adrenoleukodystrophy, Alexander disease) and is **not** the right code — do not use it | Verified by search; ICD-11 Foundation cache holds no cerebellitis term |

> ⚠️ **Open item.** The ICD-10 and ICD-11 codes could not be established. `orpha.net` was unresolvable from this environment and the ICD-11 browser was not reached. Orphanet's own disease page carries both, so the way to close this is a direct Orphadata pull (`just refresh-orphadata` then `just structured-rebuild-orphanet --id 624244`), which also gives a citable `ORPHA:624244` cache file for the definition quote above. **Do not write an ICD code from memory.**

### 1.4 Synonyms (from MedGen 1843009) **[P]**

`Postinfectious cerebellitis` (preferred) · `Post-infectious cerebellitis` · `PIC` · `Acute postinfectious cerebellar ataxia` · `APCA` · `Acute cerebellar ataxia` · `ACA` · `Acute cerebellar ataxia following infectious disease` · `Para-infectious cerebellitis`

Additional names in the literature, not in MedGen: *acute cerebellitis*, *acute fulminant cerebellitis*, *post-viral cerebellar ataxia*, *hemicerebellitis* (the unilateral variant), *varicella cerebellitis*.

### 1.5 Data provenance

The evidence base is **aggregated and case-level literature, not EHR-derived**. Gowda 2026 states the limitation plainly:

> "Evidence is largely limited to individual case reports and small case series, and no prior review has systematically pooled patient-level data across etiologies." **[V]** PMID:42649322

There is no disease registry, no natural-history cohort study, and no randomised trial. The largest single-institution paediatric series are 124 children (Italy, 11 years, 12 hospitals), 76 children (Serbia), 73 children (St Louis, 23 years), 39 children (Israel), 37 children (Tunisia) and 15 children (Turkey, acute cerebellitis only); the largest adult series is a 35-patient literature review. Every frequency figure in §3 therefore carries selection bias toward hospitalised and published cases.

---

## 2. Etiology

### 2.1 Primary causal factor: an antecedent infection

The disorder is defined by its trigger. The pathogen is **not** usually recoverable from the CNS; the inference of an immune rather than infectious mechanism rests on (a) the latent interval, (b) negative CSF PCR in most cases, and (c) the detection of anti-neuronal antibodies.

**Pooled trigger frequencies — the most recent and largest synthesis:**

> "SARS-CoV-2 (n = 24, 32.9%) was the most frequently identified trigger, followed by patients with no pathogen identified (n = 18, 24.7%), varicella-zoster virus (n = 8, 11.0%), Epstein-Barr virus (n = 5, 6.8%), and influenza (n = 5, 6.8%)." **[V]** — Gowda 2026, PMID:42649322

⚠️ **Read that figure carefully.** The SARS-CoV-2 predominance is a **publication artefact**, not an epidemiological fact: the review pools case reports, and the 2020–2024 case-report literature is saturated with COVID-19 associations. It is also adult-skewed (mean age 24.5 years). It is not the trigger distribution a paediatrician sees.

**Trigger frequencies in unselected paediatric cohorts — these are the clinically representative numbers:**

| Cohort | Trigger distribution |
|---|---|
| Connolly 1994, n=73 children, 23 years, St Louis **[V]** | "Twenty-six percent had chickenpox, 52% had other illnesses that were presumed to be viral, and in 3% the ataxia was related to immunization. Nineteen percent had no definite prodrome." |
| Nussinovitch 2003, n=39 children **[V]** | "A prodromal febrile illness was noted in 74.4%: varicella, 31%; mumps, 20%; nonspecific viral infection, 15.4%; mycoplasma, 5%; Epstein Barr virus, 3%." |
| Lancella 2017, n=124 children, Italy **[P]** | "VZV infection was diagnosed in 66 cases (53%)" |
| Yildirim 2020, n=15 children with AC **[V]** | "Etiologic workup for infectious pathogens revealed Mycoplasma pneumoniae, influenza A virus, cytomegalovirus, and varicella zoster virus in 1 case each." (i.e. 11/15 had no pathogen identified) |
| Tunisian series 2023, n=37 children **[S]** | "Aetiology was unknown in 51% of cases (19 patients)." |

**The varicella-vaccine era has changed the picture.** The Australian national active-surveillance series is the decisive evidence:

> "Varicella has historically been the most common cause, associated with up to 25% of cases in large cohorts. This study aimed to describe the spectrum of syndromes in a setting with high varicella vaccine coverage." … "A total of 20 cases (65% were vaccinated for varicella) were included … An acute febrile illness was noted in 55% and none were related to varicella or were temporally related to varicella vaccination or other childhood vaccines." … "The study provides an overall description of this uncommon spectrum of neurologic syndromes and shows the infrequency of varicella zoster virus as a cause in a vaccinated population." **[V]** — Gunaratna GPS, Mohammad SS, Blyth CC, Clark J, Crawford N, Marshall H, Dale RC, Jones CA, Britton PN; PAEDS network. *J Child Neurol* 2022;37(7):617-623. PMID:35546546, doi:10.1177/08830738221093209

> "In the age of varicella vaccination, studies have shown a predominance of acute cerebellar ataxia after respiratory illnesses." **[S]**

### 2.2 Full list of reported triggers, with NCBITaxon bindings

All taxon CURIEs below were read from `cache/ncbitaxon/terms.csv` or the OLS4 NCBITaxon index this session.

| Agent | NCBITaxon | Evidence strength for this disease |
|---|---|---|
| Varicella-zoster virus | **NCBITaxon:10335** `Human alphaherpesvirus 3` | Strongest historical association; 26–53% of paediatric cases pre-vaccine **[V/P]** |
| Epstein–Barr virus | **NCBITaxon:10376** `human gammaherpesvirus 4` | Well established in both children and adults **[V]** |
| Influenza A virus | **NCBITaxon:11320** | Established; CSF-PCR-positive cases exist (see §2.3) **[V/P]** |
| SARS-CoV-2 | **NCBITaxon:2697049** | Dominant in the post-2020 case literature **[V]** |
| *Mycoplasma pneumoniae* | **NCBITaxon:2104** `Mycoplasmoides pneumoniae` | Established; immune-mediated mechanism specifically argued **[V/S]** |
| Mumps virus | **NCBITaxon:2560602** `Mumps orthorubulavirus` | 20% of one pre-MMR-era series; longest recorded symptom duration (24 d) **[V]** |
| Human herpesvirus 6 | **NCBITaxon:10368** (`6A` = 32603, `6B` = 32604) | Case-level; one report with adenovirus co-infection **[P]** |
| Cytomegalovirus | *needs lookup* | 1/15 in Yildirim 2020 **[V]**; also post-infectious CMV rhombencephalitis **[S]** |
| Measles virus | **NCBITaxon:11234** `Measles morbillivirus` | Historical **[P]** |
| Rubella virus | **NCBITaxon:11041** | Historical **[P]** |
| Coxsackievirus / enteroviruses | **NCBITaxon:138950** `Enterovirus C`, `31704`, `39054`, `86107`, `42789` | Historical and case-level **[P]** |
| Rotavirus | **NCBITaxon:28875** `Rotavirus A` | Case-level **[S]** |
| Dengue virus | **NCBITaxon:12637** | Case report with EBV co-infection **[S]** |
| Parvovirus B19 | **NCBITaxon:10798** `Human parvovirus B19` | Case-level **[S]** |
| *Salmonella* Typhimurium | **NCBITaxon:90371** | Single adult case report **[S]** |
| *Streptococcus pyogenes* / haemolytic streptococcus | **NCBITaxon:1314** | Case report **[S]** |
| *Borrelia* spp. | **NCBITaxon:138** | Differential rather than established trigger **[S]** |
| Adenovirus, pertussis, diphtheria | *need lookup* | Historical lists **[P]** |

Montenegro's imaging series gives the classic historical list verbatim: "Varicella zoster, Epsten-Barr, rubeola, pertussis, diphtheria, and coxsackie viruses" **[P]** — note the source's own typographical error in "Epsten-Barr"; **a snippet never corrects the source it quotes.**

### 2.3 Para-infectious vs post-infectious, and the direct-invasion exception

A minority of cases are *not* post-infectious. Influenza A(H1N1)pdm09 cerebellitis has been documented with virus **in the CSF**, which makes those cases directly infectious rather than immune-mediated:

> "RT-PCR for influenza A(H1N1)pdm09 virus RNA was positive in the nasopharyngeal swab sample and CSF specimens." **[P]** — *Emerg Infect Dis* 2014;20(9):1578-1580, PMID:25153508

For *Mycoplasma pneumoniae*, the opposite holds and is the basis for the immune interpretation:

> "the detection rate of M. pneumoniae in CSF by PCR is relatively low (0%–14%), which suggests an immune-mediated pathogenesis in most cases." **[S]**

**Implication for curation:** a CSF-PCR-positive case is *infectious* cerebellitis and arguably belongs outside MONDO:0850107. This is a real scope boundary worth stating in `notes:`.

### 2.4 Vaccination as a trigger

Reported after varicella, influenza, meningococcal C conjugate and meningococcal B vaccines. Quantified risk:

> "Acute cerebellar ataxia after varicella vaccination is estimated at 1.5 in 1,000,000 doses." … "The association of acute cerebellar ataxia with varicella infection is at least 35 times higher than after vaccination." **[S]**

> "However, available data are insufficient to determine a causal association between acute cerebellar ataxia and single-antigen varicella vaccine." **[S]**

Connolly's series attributed 3% of 73 cases to immunisation **[V]**; the Australian active-surveillance series found **none** temporally related to any childhood vaccine **[V]**. ⚠️ The "1.5 per million doses" figure appears only in review summaries here — trace it to the primary VAERS/Vaccine Safety Datalink analysis before using it, and record the uncertainty. This is exactly the kind of number that should not be asserted from a secondary source.

### 2.5 Risk factors

**Genetic risk factors.** None established. No GWAS, no HLA association study, and no monogenic susceptibility locus for this disease was found. The template's `ClinVar / ClinGen / GWAS Catalog / PheGenI` searches have no target. One adjacent observation is worth noting as a *lead, not a finding*: the mouse work on inflammation-triggered cerebellar hyperexcitability used "an autoimmune-prone T-cell receptor transgenic mouse (2D2)" **[P]**, implying host autoimmune predisposition modulates the response — but that is a model-organism inference about susceptibility in general, not a human risk allele.

**Environmental / demographic risk factors.**

| Factor | Direction | Evidence |
|---|---|---|
| Young age (preschool) | ↑ risk, and ↑ proportion of all acute ataxia | median onset 3 y (n=257) **[P]**; mean 4.8 ± 3.8 y **[V]**; mean 5.3 ± 3.3 y **[P]**; mean 5.7 y **[V]** |
| Male sex | modest ↑ | 54% male **[V]**; 55% male **[P]**; M:F 1.14:1 **[P]**; sex ratio 1.17 **[S]**; 10/15 boys **[V]** |
| Natural varicella infection | ↑ risk | "Approximately one in 4,000 children with varicella will develop acute cerebellar ataxia." **[S]** ⚠️ widely repeated, primary source not opened |
| Absence of varicella vaccination | ↑ risk of the VZV-triggered form | **[V]** PMID:35546546 |
| Winter/spring seasonality of triggers | plausible ↑ | not quantified in any source read |
| Immunocompromise | changes the *differential* rather than raising risk of the post-infectious form; raises risk of direct infectious cerebellitis (opportunistic infection, lymphoma) | **[S]** |

**Not** risk factors on current evidence: toxins, radiation, occupational exposure, pollution, smoking, alcohol, diet, obesity. Searches for these returned nothing specific to this disease. **Say so rather than leaving the section blank** — an absent environmental factor with a recorded search is a curation fact.

**Protective factors.**
- **Varicella vaccination** is the single documented protective exposure, acting by removing the commonest trigger. The at-least-35-fold risk differential **[S]** is the quantitative claim; the Australian surveillance data **[V]** is the stronger evidence that it works.
- No genetic protective variant is known; no gnomAD-detectable protective allele exists to look for.
- No dietary or lifestyle protective factor is established.

**Gene–environment interactions.** None demonstrated in humans. Mechanistically, the proposition is that the trigger supplies the mimicking epitope and host immunogenetics determines whether tolerance breaks — but no study read here tests it. CTD and PheGenI have nothing for this concept.

---

## 3. Phenotypes

### 3.1 Core cerebellar phenotypes

Frequencies from Lancella 2017 (n=124 Italian children, mixed ACA/AC). ⚠️ These percentages were extracted from the **full text**, not the verbatim abstract (which names the symptoms without numbers) — tag **[P]**, and re-read the paper's Table before committing them.

| Phenotype | Frequency | HPO suggestion (verified) | Note on the mapping |
|---|---|---|---|
| Broad-based gait disturbance | 92% | **HP:0002066** `Gait ataxia` | the single most characteristic sign **[V]** |
| Balance disturbance | 68% | **HP:0002078** `Truncal ataxia` | ⚠️ approximate — "balance disturbance" is broader than truncal ataxia; **HP:0001288** `Gait disturbance` is the safer coarse alternative |
| Dysmetria | 35% | **HP:0001310** `Dysmetria` | — |
| Slurred speech | 27% | **HP:0001260** `Dysarthria` | **HP:0002168** `Scanning speech` where specified |
| Nystagmus | 12% | **HP:0000639** `Nystagmus` | one of the two commonest associated findings in Nussinovitch 2003 **[V]** |
| Intention tremor | not quantified | **HP:0002080** `Intention tremor` | listed among isolated cerebellar signs **[V]** |
| Dysdiadochokinesis | not quantified | **HP:0002075** `Dysdiadochokinesis` | **[V]** PMID:38008790 |
| Hypotonia | not quantified | **HP:0001252** `Hypotonia` | a documented "red flag" when present **[V]** |
| Titubation | case-level | **HP:0030187** `Titubation`; **HP:0002599** `Head titubation` | — |
| Ataxia (generic) | defining | **HP:0001251** `Ataxia` | use the specific terms above in preference |

Kravljanac 2024 gives the canonical list of isolated cerebellar signs verbatim: "ataxic gait, dysmetria, dysdiadochokinesia, intention tremor, dysarthria, and nystagmus" **[V]**, present in isolation in "Forty-two (56%) cases".

### 3.2 Extracerebellar phenotypes — the AC / AFC discriminators

| Phenotype | Frequency | HPO suggestion (verified) |
|---|---|---|
| Vomiting | 42% (n=124) **[P]**; >80% in adults **[P]** | **HP:0002013** `Vomiting` |
| Fever | 34% (n=124) **[P]**; 55% acute febrile illness **[V]** | **HP:0001945** `Fever` |
| Headache | 30% (n=124) **[P]**; >80% in adults **[P]** | **HP:0002315** `Headache` |
| Tonsillar herniation | **73.3%** of AC (n=15) **[V]** | *no HPO term found* — record in prose; **HP:0002516** `Increased intracranial pressure` is the closest consequence |
| Obstructive hydrocephalus | **26.6%** of AC (n=15) **[V]**; 9/35 adults **[P]** | **HP:0000238** `Hydrocephalus` |
| Reduced consciousness | **29%** of adults (10/35) **[P]** | **HP:0004372** `Reduced consciousness`; **HP:0001254** `Lethargy` |
| Nuchal rigidity / meningism | in the Orphanet clinical description **[S]** | **HP:0031179** `Nuchal rigidity` |
| Papilledema | AFC | **HP:0001085** `Papilledema` |
| Diplopia | case-level | **HP:0000651** `Diplopia` |
| Dysphagia | case-level | **HP:0002015** `Dysphagia` |
| Seizures, altered mental status | in the Orphanet clinical description **[S]** | **HP:0001298** `Encephalopathy`; **HP:0006846** `Acute encephalopathy` |

Kravljanac's "cerebellar plus" definition is the best structured statement of these, verbatim:

> "CS-plus symptoms which included CS associated with any of other symptoms such as encephalopathy (GCS < 15), awareness disturbances, vomiting, headache, a new onset limb or facial paresis, torticollis, hypotonia, and opsoclonus." **[V]** PMID:38008790

And the red-flag list, verbatim:

> "'The red flags' associated with cerebellar signs are limbs or facial palsy, hypotonia, GCS < 15, vomiting, opsoclonus, headache, myoclonus, visual impairment, torticollis, and vertigo." **[V]** PMID:38008790

### 3.3 Laboratory and imaging phenotypes

| Phenotype | Frequency | HPO suggestion (verified) |
|---|---|---|
| CSF pleocytosis | LP done in 24/124 (19.5%); pathological in 8 (33%); "pleocytosis in 8 cases (mean 51 cells/mmc, range 7–150)" **[P]** | **HP:0012229** `CSF pleocytosis` |
| CSF oligoclonal bands | **31.2%** of 77 APCA patients tested **[P]** — and predictive of relapse | **HP:6000397** `CSF oligoclonal immunoglobulin G bands` |
| Cerebellar oedema / swelling | defining for AC | **HP:0030915** `Cerebellar edema` |
| Cerebellar cortical T2 hyperintensity | MRI pathological in 6/61 (10%) of mixed ACA/AC **[P]**; near-universal in AC **[V]** | **HP:0001317** `Abnormal cerebellum morphology` (coarse) |
| Cerebellar atrophy (follow-up) | **9/12** with follow-up MRI in an AC series **[V]**; ~25% in long-term series **[S]**; up to half in hemicerebellitis **[S]** | **HP:0001272** `Cerebellar atrophy`; **HP:0008278** `Cerebellar cortical atrophy`; **HP:0012082** `Cerebellar Purkinje layer atrophy` |

The CSF-OCB finding is new and clinically consequential:

> "Among APCA cases tested (n=77), 31.2% were CSF OCB-positive, with 'significantly increased relapse rate (5/24, 20.8% vs. 0/53, 0%, P=0.001).'" **[P]** — Zhao Q, Gao C, Wang L, Liu C, Sun S, Li B. *Front Pediatr* 2025. PMID:41321459, doi:10.3389/fped.2025.1613558

### 3.4 Onset, severity, progression

| Characteristic | Value |
|---|---|
| **Age of onset** | Overwhelmingly early childhood. Median 3 y (n=257) **[P]**; mean 4.8 ± 3.8 y (n=39) **[V]**; mean 4.9 ± 3.8 y (n=58) **[S]**; mean 5.3 ± 3.3 y (n=124) **[P]**; mean 5.7 y, IQR 2.1–8.3 (n=76) **[V]**. The AC subtype skews older — median 9.5 y, range 3–15 (n=15) **[V]**. Adults occur: median 36 y in the adult literature review (n=35) **[P]**; the pooled range is "7 months-74 years" **[V]** |
| **Onset pattern** | **Acute** — "Onset was acute in 89% of cases in both groups" **[S]**. Inclusion criteria typically require evolution within 72 h **[V]** |
| **Latency from trigger** | **8.8 ± 7.4 days** **[V]** (Nussinovitch 2003). Shorter in para-infectious cases (p=0.001) **[S]** |
| **Severity** | Variable by definition — the three-tier ACA/AC/AFC classification *is* the severity axis. Pooled: 46.6% ACA, 35.6% AC, 17.8% AFC **[V]** (publication-biased toward severity); 70% ACA, 20% AC, 10% AFC in population surveillance **[V]** |
| **Progression** | **Monophasic and self-limited** in the large majority. "Acute cerebellar ataxia in childhood is a self-limited disease." **[V]** Relapse occurs and is associated with CSF OCB positivity (20.8% vs 0%) **[P]**. A biphasic worsening on re-infection is documented in a GluRδ2-antibody case: "although cerebellar ataxia gradually improved, it worsened yet again following mumps and varicella virus infection" **[P]** |
| **Duration** | Days to weeks. "Full gait recovery took less than 2 weeks on average, and the longest duration of neurologic signs was 24 days (mumps-related)." **[V]** "The majority (91%) recovered within 30 days." **[S]** Median hospital stay 11 days (range 1–29) **[P]** |

### 3.5 Quality-of-life impact

No EQ-5D, SF-36 or PROMIS data for this disease were found. Two instruments *were* used:

- **Liverpool Outcome Scale** at 12 months in the Australian surveillance series: "A subset (total of 7 children) followed up at 12 months all showed reduced Liverpool Outcome Scale scores." **[V]** — a striking result, since every one of seven survivors scored below normal at a year.
- **Parental cognitive questionnaires** in Hennes 2012: "cognitive deficits were found in six patients" of eleven, affecting "spatial visualization ability, language skills, and concentration" **[V]**.

Per-phenotype QoL impact:
- *Gait ataxia* — the dominant functional burden acutely; drives the inability to walk unaided and hospitalisation.
- *Dysarthria* — persistent in a minority; "significant dysarthria" in 1 of 3 patients who developed atrophy **[S]**.
- *Cognitive/affective sequelae* — the under-recognised burden. "Among the long-term effects of acute cerebellitis, poor spatial visualization, decreased language skills, and concentration impairment can be seen." **[S]** This maps onto the **cerebellar cognitive affective (Schmahmann) syndrome** — "deficits in executive function, visuospatial function, linguistic processing, and affect regulation" **[S]** — and cerebellitis is a listed cause of CCAS **[S]**. School performance is the practical endpoint: "only 5 of the 60 children demonstrated sustained learning problems" **[V]**, against "One fifth of the children followed for more than 4 months experienced transient behavioral or intellectual difficulties" **[V]**.

The authors' own conclusion is the quotable one:

> "neurological and cognitive sequelae are common in children with AC and underline the role of the cerebellum in cognition." **[V]** — Hennes E, Zotter S, Dorninger L, Hartmann H, Häusler M, Huppke P, Jacobs J, Kraus V, Makowski C, Schlachter K, Ulmer H, van Baalen A, Koch J, Gotwald T, Rostasy K. *Neuropediatrics* 2012;43(5):240-8. PMID:22936351, doi:10.1055/s-0032-1324732

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes: none

**There is no causal gene, no OMIM entry, no pathogenic variant, no variant classification, no allele frequency, no germline/somatic distinction, no modifier gene, and no chromosomal abnormality associated with postinfectious cerebellitis.** MONDO records no `RO:0004003` relation for MONDO:0850107. Every subsection of the template's §4 that presumes a Mendelian architecture is **not applicable** and should be recorded as such rather than left empty.

Genetic testing has a role in this disease only as a **differential-diagnostic exclusion** — see §10.

### 4.2 What *is* molecular here: candidate autoantigens

The molecular content of this entry is the set of cerebellar self-antigens against which antibodies have been reported. Every gene CURIE below was resolved this session (repository `cache/hgnc/terms.csv` or the HGNC REST API).

| Autoantigen | Gene | HGNC | Evidence in *this* disease | Tag |
|---|---|---|---|---|
| **Glutamate receptor δ2 (GluRδ2 / GluD2)** | `GRID2` | **hgnc:4576** | **The best-supported target.** Detected in serum *and* CSF in post-infectious ACA progressing to cerebellitis, and in acute cerebellitis with obstructive hydrocephalus. Predominantly expressed in Purkinje cells | **[P]** PMID:17049194; PMID:17008044 |
| **Pericentrin / centrosome antigens** | `PCNT` | **hgnc:16068** | Post-varicella ACA specifically: antibodies to ≥1 centrosome antigen in 11/12 children; pericentrin antibodies in 5/12 and **in no other group tested**; punctate cerebellar staining co-localising with pericentrin | **[P]** Fritzler MJ, Zhang M, Stinton LM, Rattner JB. *BMC Pediatr* 2003;3:11. PMID:14503922 |
| **GAD65** | `GAD2` | **hgnc:4093** (GAD1 = hgnc:4092) | Established in immune-mediated cerebellar ataxia broadly; mechanism worked out (↓GABA release → glutamate excitotoxicity) | **[P]** |
| **Homer-3** | `HOMER3` | **hgnc:17514** | "Cerebellar Purkinje cells highly express a scaffold molecule Homer-3, and its antibodies also induce cerebellitis and ataxia." | **[P]** |
| **Caspr2** | `CNTNAP2` | **hgnc:13830** | Listed among immune-mediated ataxia targets | **[P]** |
| **ITPR1** | `ITPR1` | **hgnc:6180** | Listed among immune-mediated ataxia targets | **[P]** |
| **AP3B2 (NAPB)** | `AP3B2` | **hgnc:567** | Listed among immune-mediated ataxia targets | **[P]** |
| **mGluR1** | `GRM1` | **hgnc:4593** | mGluR1 antibody ataxia is a demonstrated passive-transfer disease; mGluR1 is also the receptor mediating the TNF-α effect (§6) | **[S]** |
| **mGluR2, NIF** | *mGluR2 = `GRM2`, NIF needs resolution* | *needs lookup* | Listed among immune-mediated ataxia targets | **[P]** |
| **GQ1b (a ganglioside, not a gene product)** | — | — | Anti-GQ1b IgG reported in isolated pancerebellar syndrome; 1.2% of 257 acute-ataxia children had anti-GQ1b syndrome. "Clinicians should consider anti-GQ1b testing in cases of acute cerebellar ataxia following infection." | **[P/S]** PMID:40787651 |
| **Glycine receptor α1** | `GLRA1` | **hgnc:4326** | In **opsoclonus-myoclonus**, not in this disease — keep separate | **[P]** |
| Anti-amphiphysin, anti-Ri | *need lookup* | — | One report of paraneoplastic antibodies in a postinfectious cerebellar syndrome, explicitly framed as possibly coincidental | **[S]** PMID:33029469 |

**How often are antibodies found?** "As many as 28% of children with acute cerebellar ataxia may have detectable autoantibodies." **[S]** ⚠️ Review-level; find the primary cohort before citing.

**Non-specific serological finding:** antiphospholipid antibodies were reported in 75% of post-varicella ataxia sera **[P]** (Fritzler 2003) — interesting but of unclear mechanistic significance.

### 4.3 Genes relevant to the *mechanism* (not to causation)

These are wild-type genes whose products carry the effector mechanism, and they belong on pathophysiology nodes, not in a `genetic:` block. All CURIEs verified this session.

`TNF` **hgnc:11892** · `TNFRSF1A` **hgnc:11916** · `TLR4` **hgnc:11850** · `IL6` **hgnc:6018** · `IL1B` **hgnc:5992** · `GRM1` **hgnc:4593** · `KCNN2` **hgnc:6291** (SK2) · `KCNN3` **hgnc:6292** (SK3) · `GRIA1` **hgnc:4571**

### 4.4 Epigenetics, chromosomal abnormalities, molecular profiling of human tissue

- **Epigenetics:** nothing. No DNA-methylation, histone-modification or chromatin study of this disease exists in ENCODE, Roadmap, MethBase or DiseaseMeth, and none was found in the literature.
- **Chromosomal abnormalities:** not applicable. No aneuploidy, translocation or CNV association.
- **Human transcriptomics / proteomics / metabolomics / lipidomics / single-cell / spatial:** **no human dataset for this disease was identified.** GEO, ArrayExpress, PRIDE, MetaboLights and the Human Cell Atlas yield nothing specific. The disease is diagnosed clinically and radiologically; tissue is almost never obtained, and when it is (resection for fulminant swelling, or autopsy) the material has been used for histology, not omics.
- **Animal-model transcriptomics does exist** and is the only molecular profiling available: influenza-A inoculation of 2D2 mice "induced a temporal transcriptomic alteration in the cerebellum", with "several chemokines, including CCL6, CCL17, CCL25, CCL28, and C-X-C motif chemokine 5 (CXCL5), increased, while CCL27a and CX3CL1 decreased" **[P]**. In DENV-3-infected mice, "The infection elicits significant increases in IFN-γ, TNF-α, CCL2, CCL5, CXCL1, and CXCL2." **[P]**
- **One human cytokine observation** is reported, tied to the atrophy outcome: "Pro-inflammatory cytokines, including IL-6, IL-9, IL-12, IL-13, GM-CSF, and macrophage inflammatory proteins-1α (MIP-1α/CCL3), increased in patients with cerebellar atrophy and induced inflammation in the cerebellum." **[P]** ⚠️ The "and induced inflammation" clause is a causal claim the correlational observation does not license — if this sentence is quoted, the `explanation` must not inherit that inference.
- **Functional genomics screens (CRISPR/RNAi):** none for this disease.

---

## 5. Environmental Information

- **Environmental factors:** none established. No toxin, radiation, pollutant or occupational exposure is linked to postinfectious cerebellitis. CTD and EPA databases have nothing for this concept. ⚠️ Note for curation: `check-environmental-evidence` will flag any `environmental[]` entry here. The honest encoding is a **single** environmental entry for the antecedent infection/vaccination exposure, linked to the initiating pathophysiology node with `environmental_effect: TRIGGERS`. For any exposure genuinely uncitable, use the `Left deliberately uncited.` `review_notes:` waiver with the ECTO searches written out — do not leave it bare.
- **Lifestyle factors:** none. No diet, smoking, alcohol, exercise or sleep association was found. For a disease of 3-to-5-year-olds this is unsurprising and should be stated rather than searched again.
- **Infectious agents:** this *is* the environmental exposure. See §2.2 for the full taxon list with NCBITaxon bindings.
- **ECTO binding:** an exposure term for "exposure to varicella-zoster virus" or "exposure to a vaccine" would be needed. ⚠️ **Do not assert ECTO has no such term without running the searches.** Run `l~virus`, `l~varicella`, `l~vaccin`, `l~infectio`, `l~pathogen` against the ECTO build and record verbatim what each returns — the repository's own history records three separate cases where a note claiming "no ECTO term exists" was refuted by re-running one of the queries it cited, and one where only the British spelling found the term.

---

## 6. Mechanism / Pathophysiology

### 6.1 The causal chain

Steps marked **[inferred]** are reasoned, not demonstrated, in this disease.

**1.** An antecedent infection (VZV, EBV, influenza, *M. pneumoniae*, SARS-CoV-2, HHV-6, mumps…) — or, rarely, a vaccination — delivers a systemic antigen load and activates innate immunity.
→ **leads to**

**2.** Over a latent interval averaging **8.8 ± 7.4 days** **[V]**, an adaptive immune response is primed that cross-reacts with cerebellar self-antigens. **[inferred — molecular mimicry is the accepted framework but no mimicking epitope pair has been demonstrated for any trigger of this disease.]** The accepted framing: "A widely accepted mechanism for viral-induced autoimmunity is molecular mimicry." **[S]** Mitoma is blunter: "Autoimmune mechanisms remain obscure…the exact mechanisms remain unclear." **[P]**
→ **leads to**

**3.** Circulating pro-inflammatory mediators increase blood–brain-barrier permeability, admitting antibody, complement and leukocytes to the cerebellar compartment:
> "The production of inflammatory mediators, such as TNF-α, IL-6, IFN-γ, granulocyte-macrophage colony-stimulating factor (GM-CSF), and IL-1, possibly promotes the breakdown of the blood–brain barrier's (BBB) integrity; increases the permeability; leads to the infiltration of mediators, immune cells, and microorganisms." **[P]**
> "IL-1β induces the expression of matrix metalloproteinase-9 (MMP-9) and indirectly destabilizes the BBB." **[P]**
→ **branches into 4a and 4b**

**4a. Humoral branch.** IgG binds Purkinje-cell surface and cytoplasmic antigens — GluRδ2 most directly evidenced, plus pericentrin, GAD65, Homer-3, Caspr2, ITPR1, AP3B2, mGluR1; GQ1b in overlap cases (§4.2). In mild disease the consequence is **reversible synaptic dysfunction rather than cell death** — receptor internalisation, not degeneration **[P, Mitoma 2021]**. This is why most patients recover completely with an unremarkable MRI.
→ **leads to 7**

**4b. Cellular branch.** Cytotoxic T cells and activated microglia infiltrate the cerebellar cortex. In resected and autopsy tissue:
> "Microscopic examination of a cerebellar biopsy section from a patient with acute near-fatal cerebellar swelling demonstrated intense T-cell infiltration in the molecular layer and marked evacuation at the interface of the molecular and granular layers." **[S]**
> "In the cerebellar cortex, there was patchy infiltration by CD3-positive T cells spatially corresponding to areas of Purkinje cell loss, with CD8 T-cell infiltration identified in areas of Purkinje cell loss." **[S]**
> "This inflammation has been noted to spare the cerebellar white matter." **[S]**
→ **leads to 5 and 6**

**5. Microglia–glia–neuron effector cascade** (demonstrated in rodent, not human):
Microglial TLR4 engagement → TNF-α release → TNFR1 on **Bergmann glia** → glutamate release → **mGluR1** on Purkinje cells → phosphatase activation → downregulation of **SK (KCa2) channels** → **potentiation of Purkinje-cell intrinsic excitability**.
> "An inflammatory cytokine, tumor necrosis factor alpha (TNF-α), released from microglia via toll-like receptor 4, triggers this plasticity." **[V]** — Yamamoto M, Kim M, Imai H, Itakura Y, Ohtsuki G. *Cell Rep* 2019;28(11):2923-2938.e8. PMID:31509752
> "In the cerebellar Purkinje cells, acute inflammation by LPS or heat-killed Gram-negative bacteria induces hyperexcitability through akin signaling of the intrinsic plasticity. There, small conductance Ca2+-activated K+-channel (SK channel) function is downregulated." **[P]**
> "the effect of TNF-α on the intrinsic excitability of PCs was abolished under a condition in which the type1 TNF receptor (TNFR1) in Bergmann glia (BG) was genetically suppressed" … "Pharmacological inhibition of mGluR1, indeed, prevented the TNF-α-mediated elevation of the intrinsic excitability in PCs." **[P]** — Shim HG, Jang SS, Kim SH, et al. *Sci Rep* 2018;8. PMID:30072733, doi:10.1038/s41598-018-29786-9

**⚠️ 5 → 7 is an explicit, published gap, and this is the most important mechanistic honesty in the entry.** The LPS model produces hyperexcitability and *psychiatric* phenotypes but **not ataxia**, while blocking SK channels directly *does* produce ataxia:
> "In our animal model of the acute inflammation of the cerebellar cortex, animals did not show any ataxia but hyperexcitability in the cerebellar cortex and depression-like behaviors. In contrast, animal models with neurodegeneration of the cerebellar Purkinje cells and hypoexcitability of the neurons show cerebellar ataxia. The suppression of the Ca2+-activated K+ channels in vivo is associated with a type of ataxia. Therefore, there is a gap in our interpretation between the very early phase of cerebellar inflammation and the emergence of cerebellar ataxia." **[P]** — Parvez MSA, Ohtsuki G. *Brain Sci* 2022;12(3):367. PMID:35326323, doi:10.3390/brainsci12030367
> "Stimulation of microglia by LPS-exposure in the cerebellar cortex and the resultant hyperexcitability of Purkinje cells were not sufficient to induce cerebellar ataxia, although the injection of 200 nM apamin to the cerebellar anterior lobes induced ataxia." **[P]**

**6. Purkinje-cell injury or loss** where the cellular branch dominates:
> "A child with fatal cerebellar swelling showed prominent loss of Purkinje cells, suggesting this may be the target of the inflammatory response." **[S]**
Downstream of the antibody branch, GAD65 antibodies supply a parallel route: "GAD antibodies (GAD Abs) disturb the cerebellar activity by the suppression of GABA release, which leads to cerebellar ataxia." … "Thus, GAD Abs alter the balance between glutamate and GABA and induce glutamate excitotoxicity." **[P]**
→ **leads to 7**

**7. Loss of patterned Purkinje-cell output** from cerebellar cortex to the deep cerebellar nuclei → disordered dentate/interposed nucleus firing → loss of feed-forward and error-correcting control of movement.
> "Activated microglia and excessive inflammatory mediators cause neurophysiological modulation of synaptic transmission, plasticity induction of Purkinje cells, and disruption of Ca²⁺ homeostasis, leading to the loss of Purkinje neurons, dysfunction of the cerebellar cortex, and excess DCN activity, followed by tremorogenic oscillation and emergence of ataxia." **[S]**
→ **results in** gait ataxia, truncal ataxia, dysmetria, dysdiadochokinesis, intention tremor, dysarthria, nystagmus, hypotonia (§3.1)

**8. Mass-effect branch** (AC → AFC only). Cytokine-driven oedema of the cerebellar cortex and leptomeninges increases infratentorial volume inside a non-compliant posterior fossa:
> "The fulminant type of acute cerebellitis usually involves diffuse cerebellar swelling with increased pressure in the infratentorial compartment, causing compression of the brainstem, hydrocephalus, and downward or upward herniation of the posterior fossa structures." **[S]**
→ fourth-ventricular compression → **obstructive hydrocephalus** → raised intracranial pressure → papilledema, tonsillar herniation, brainstem compression → reduced consciousness → death in the fulminant form (1/73 pooled **[V]**).
Note this branch is **physical, not immunological**, which is why it is the one branch answered by surgery rather than by immunotherapy.

**9. Resolution vs sequelae** — the outcome fork, governed by *cerebellar reserve*:
- If the immune process halts while reserve is intact → **complete recovery** (64.4% pooled **[V]**; 91% in unselected paediatric cohorts **[V]**).
- If Purkinje-cell loss has occurred → **cerebellar cortical atrophy** on follow-up MRI → persistent ataxia, dysarthria, tremor and cerebellar cognitive affective features.
> "The restorable stage is defined as the period associated with intact cerebellar reversal capacity, i.e., cerebellar reserve" … "patients with immune-mediated cerebellar ataxias (IMCAs) in early stages with no or mild cerebellar atrophy had their ataxias partially or completely improved by immunotherapy." **[S]** — Mitoma H, Manto M, et al. *Consensus Paper. Cerebellar Reserve.* *Cerebellum* 2020. PMID:31879843
> "The presence of residual cerebellar atrophy on follow-up neuroimaging is almost always associated with long-term motor and/or cognitive deficits." **[S]**

**A second branch out of step 5** deserves recording because it is the mechanistic basis for the cognitive/affective sequelae: "Region-specific inflammation in the cerebellum in vivo shows depression- and autistic-like behaviors. Furthermore, both TNF-α inhibition and microglia depletion revert such behavioral abnormality. Resting-state functional MRI reveals overconnectivity between the inflamed cerebellum and the prefrontal neocortical regions." **[V]** PMID:31509752

### 6.2 Checklist coverage against the template's categories

| Category | Content |
|---|---|
| **Molecular pathways** | TLR4/NF-κB innate signalling; TNF-α/TNFR1; mGluR1 (Gq) signalling; complement classical pathway (inferred); MAPK in microglia ("microglia may use specific combinations of MAPKs to induce different inflammatory cytokines" **[P]**); type-I/II interferon (STAT1, IFIT1) **[P]**. No KEGG/Reactome pathway is annotated to this disease. |
| **Cellular processes** | Microglial activation; astrocyte/Bergmann-glial activation; leukocyte transmigration; antigen processing and presentation; antibody-mediated receptor internalisation; T-cell-mediated cytotoxicity; neuronal apoptosis; vasogenic and cytotoxic oedema |
| **Protein dysfunction** | **No protein misfolding or aggregation.** The dysfunction is *extrinsic* — antibody occupancy or loss of a channel's surface expression, not a mutant protein. SK-channel downregulation is the key functional lesion identified; GAD65 enzymatic blockade reduces GABA synthesis |
| **Metabolic changes** | Glutamate/GABA imbalance with glutamate excitotoxicity **[P]**. Also reported: "activated microglia and excessive proinflammatory cytokines release cause the downregulation of glial glutamate transporter GLT-1 expression" **[P]**. No systemic metabolic abnormality; no HMDB signature |
| **Immune involvement** | The entire mechanism. Post-infectious autoimmunity with both humoral and cellular arms; not an immunodeficiency; not a chronic inflammatory state |
| **Tissue damage mechanisms** | Immune-mediated cytolysis of Purkinje cells; oedema; raised intracranial pressure with mechanical compression and herniation; **no** fibrosis, **no** primary ischaemia (though herniation can cause secondary ischaemia — one case report describes "Acute Fulminant Viral Cerebellitis With Hypoxic-Ischemic Encephalopathy" **[S]**) |
| **Biochemical abnormalities** | SK (KCa2) channel downregulation; mGluR1 over-activation; GAD65 inhibition. No enzyme deficiency |
| **Epigenetic changes** | None reported |

### 6.3 Suggested GO and CL terms

All verified from `cache/go/terms.csv` and `cache/cl/terms.csv` this session.

**Biological processes (GO).** `GO:0019882` antigen processing and presentation · `GO:0002474` antigen processing and presentation of peptide antigen via MHC class I · `GO:0002495` …via MHC class II · `GO:0002455` humoral immune response mediated by circulating immunoglobulin · `GO:0006958` complement activation, classical pathway · `GO:0001913` T cell mediated cytotoxicity · `GO:0001788` antibody-dependent cellular cytotoxicity · `GO:0001774` microglial cell activation · `GO:0048143` astrocyte activation · `GO:0061900` glial cell activation · `GO:0150076` neuroinflammatory response · `GO:0019221` cytokine-mediated signaling pathway · `GO:1905605` positive regulation of blood-brain barrier permeability · `GO:0002523` leukocyte migration involved in inflammatory response · `GO:0035249` synaptic transmission, glutamatergic · `GO:0051966` regulation of synaptic transmission, glutamatergic · `GO:0060292` long-term synaptic depression · `GO:0051402` neuron apoptotic process · `GO:0043525` positive regulation of neuron apoptotic process

⚠️ `GO:0070997` is **obsolete** (`obsolete neuron death`) — do not bind it. Terms still needing lookup: *small conductance calcium-activated potassium channel activity*, *regulation of membrane potential*, *molecular mimicry* (likely has no GO term at all — if so, record the search).

**Cell types (CL).** `CL:0000121` Purkinje cell *(the principal target)* · `CL:0000644` Bergmann glial cell *(the TNF-α→glutamate relay)* · `CL:0000129` microglial cell *(the TNF-α source)* · `CL:0000794` CD8-positive, alpha-beta cytotoxic T cell · `CL:0000624` CD4-positive, alpha-beta T cell · `CL:0000786` plasma cell · `CL:0001031` cerebellar granule cell · `CL:0000127` astrocyte · `CL:0000542` lymphocyte · `CL:0000118` basket cell

⚠️ Note the "logical rules" trap: a node asserting Purkinje-cell injury together with a GO process whose substrate CL disqualifies is a `check-logical-rules` finding. Here the risky pairing would be binding `CL:0000644` Bergmann glial cell on a node whose process is a neuronal one — keep the glial relay and the neuronal consequence as separate nodes.

---

## 7. Anatomical Structures Affected

### 7.1 Organ level

- **Primary organ: the cerebellum.** The disease is defined by confinement to it. "Acute cerebellitis (AC) is characterized by cerebellar symptoms and magnetic resonance imaging (MRI) changes primarily confined to the cerebellum." **[V]** PMID:22936351
- **Secondary involvement:** the ventricular system (fourth ventricle obstruction → hydrocephalus); the brainstem (compression, not primary inflammation); the leptomeninges (enhancement; "leptomeningeal exudates of lymphoplasmacytic and mononuclear cells" **[S]**); the supratentorial compartment indirectly via hydrocephalus.
- **An important scope boundary:** when inflammation extends beyond the cerebellum the entity changes. One of the three recognised MRI patterns is "acute cerebellitis with encephalitis, demonstrating additional inflammation in extracerebellar areas" **[S]**, and at least one paper argues such cases are a *concurrent encephalitis*, "not a subtype of ADEM" **[S]**. A case with brainstem extension is a rhombencephalitis, which is a different concept.
- **Body system:** nervous system (central). No other system is affected by the disease itself.

### 7.2 Tissue and cell level, with laminar specificity

The laminar pattern is one of the most distinctive features and is worth encoding precisely. Inflammation targets the **cerebellar cortex** and **spares the white matter** — the inverse of ADEM.

| Structure | UBERON (verified) | Involvement |
|---|---|---|
| Cerebellum | **UBERON:0002037** | The primary site |
| Cerebellar cortex | **UBERON:0002129** | Grey-matter T2 hyperintensity is the imaging signature |
| Molecular layer of cerebellar cortex | **UBERON:0002974** | Site of "intense T-cell infiltration" **[S]** |
| Purkinje cell layer of cerebellar cortex | **UBERON:0002979** | Site of Purkinje-cell loss; `HP:0012082` atrophy |
| Granular layer of cerebellar cortex | **UBERON:0002956** | "marked evacuation at the interface of the molecular and granular layers" **[S]** |
| White matter of cerebellum | **UBERON:0002317** | **Relatively spared** — a negative finding worth recording |
| Cerebellar vermis | **UBERON:0004720** | Resected in fulminant cases to decompress |
| Dentate nucleus | **UBERON:0002132** | Downstream of Purkinje output loss ("excess DCN activity" **[S]**) |
| Fourth ventricle | **UBERON:0002422** | Compressed → obstructive hydrocephalus |
| Leptomeninx | **UBERON:0000391** | Leptomeningeal enhancement; inflammatory exudate |
| Brainstem | **UBERON:0002298** | Compressed in AFC |
| Superior / middle cerebellar peduncle | **UBERON:0002150** / **UBERON:0002152** | One paediatric case showed "a lesion suggestive of demyelination in the cerebellar peduncle" **[P]** |

⚠️ **Outstanding lookup: "cerebellar hemisphere".** It is not in `cache/uberon/terms.csv` and did not appear in the OLS cerebellar-layer query. Needed for the bihemispheric vs hemicerebellitis distinction — resolve it before binding.

### 7.3 Subcellular level

No subcellular compartment is primarily implicated. Two incidental relevancies: the autoantigen pericentrin localises to the **centrosome** (and to axons in cerebellum **[P]**), and GluRδ2 and mGluR1 are **plasma-membrane** proteins. GO Cellular Component terms would need lookup; given how peripheral this is to the disease, leaving the subcellular slot empty with a recorded reason is the better call.

### 7.4 Localisation and lateralisation

Three MRI patterns, each with its own laterality:

> "MRI findings in acute cerebellitis are categorized as one of three presenting patterns: bihemispheric lesions, hemicerebellitis, and acute cerebellitis with encephalitis, demonstrating additional inflammation in extracerebellar areas." **[S]**

- **Bilateral and symmetrical is the rule.** "Magnetic resonance imaging (MRI) generally showed bilateral symmetrical T2 hyperintense changes with moderate swelling in the cerebellar cortex." **[V]** PMID:32160830
- **Hemicerebellitis is the rare unilateral variant** — "an extremely rare unilateral presentation of cerebellitis mimicking a tumour" **[S]** — with "unilateral cerebellar swelling with foliaform enhancement" **[S]** and a distinctive sequela: "ipsilateral hemicerebellar atrophy develops in up to half of cases" **[S]**. This is a strong candidate for a `has_subtypes` row on anatomical rather than severity grounds.

---

## 8. Temporal Development

### 8.1 Onset

- **Age:** see §3.4. Early childhood predominance; AC skews older than ACA; adult cases exist across the lifespan (pooled range "7 months-74 years" **[V]**).
- **Pattern: acute**, usually over hours to 72 h. Afebrile at onset in the classic ACA presentation (Orphanet's description is "acute-onset afebrile gait ataxia" **[S]**), though fever was present in 34% of one paediatric cohort **[P]** and defines the para-infectious subgroup.
- **The latent interval is the diagnostic signature:** 8.8 ± 7.4 days from prodrome to ataxia **[V]**. "Acute cerebellar ataxia usually develops days to weeks after an illness." **[S]**

### 8.2 Progression and staging

There is **no formal staging system**. The operative staging is the severity classification plus Mitoma's physiological staging:

| Axis | Stages |
|---|---|
| **Severity (clinical/radiological)** | ACA → AC → AFC. Used for classification and outcome stratification in Gowda 2026 **[V]** and Gunaratna 2022 **[V]** |
| **Clinical score** | Lancella 2017 built one: "A score based on both cerebellar and extracerebellar signs/symptoms was computed for each patient. One point was given for each sign/symptom reported. Severity was divided in three classes: low, moderate, severe." **[V]** It predicted treatment allocation ("Patients with a higher clinical score on admission had a higher probability of receiving intravenous steroids" **[V]**) but not outcome |
| **Physiological (cerebellar reserve)** | "Restorable stage" — reserve intact, immunotherapy can reverse the deficit — vs the stage past the reserve threshold, where loss is fixed **[S]** |

- **Progression rate:** rapid onset then **monophasic resolution**. In AFC the deterioration can be hours: "All three children in the series experienced rapidly deteriorating neurological status, progressing from mild symptoms including headache, vomiting, and cerebellar signs, to somnolence, with radiological evidence of obstruction of CSF pathways." **[S]**
- **Course pattern:** monophasic and self-limited in the large majority; relapsing in a CSF-OCB-positive minority (20.8% **[P]**); progressive only in the sense of the acute fulminant deterioration.
- **Duration:** self-limited. Gait recovery typically under two weeks **[V]**; 91% recovered within 30 days **[S]**; median hospital stay 11 days **[P]**.

### 8.3 Patterns

- **Remission:** predominantly **spontaneous**. "Acute cerebellar ataxia in childhood is a self-limited disease" and "The recovery was faster than that reported in previous publications and was complete in all children without any neurologic sequelae." **[V]** Treatment-induced remission is claimed for steroids in AC but is not trial-supported (§12).
- **Critical period for intervention — the single most actionable concept in the disease.** Two independent windows:
  1. **Immunological:** "Early therapeutic intervention at the time when cerebellar reserve is preserved is highly recommended." … "for those cerebellar disorders that can be treated emergently, therapy must be introduced while cerebellar reserve is still present, and clinicians are urged to not miss this window of opportunity." **[S]** The clinical corollary: "early steroid treatment for acute cerebellitis might have been effective to prevent the progress of the disease and improve the prognosis." **[P]** PMID:17008044
  2. **Mechanical:** the window before herniation in AFC. "Different therapeutic pathways include early posterior fossa decompression, early cerebrospinal fluid diversion, and delayed intervention after neurological deterioration with markedly different outcomes." **[S]**
- **Developmental vulnerability:** the 2–6-year peak coincides with first exposure to common childhood viruses, and plausibly with a developmental window of cerebellar plasticity — but no source read establishes a developmental-biology basis, so this must be recorded as a hypothesis, not a finding.

---

## 9. Inheritance and Population

### 9.1 Inheritance: not applicable

**There is no inheritance pattern.** No penetrance, no expressivity, no anticipation, no germline mosaicism, no founder effect, no consanguinity role, no carrier frequency. The entry should carry **no `inheritance:` block at all** — not an `Unknown` one, which would imply an unresolved Mendelian question. Familial recurrence has not been reported.

### 9.2 Epidemiology

| Measure | Value | Source and caveat |
|---|---|---|
| Orphanet prevalence class | **Unknown** | **[S]** — Orphanet does not assign a prevalence band |
| Incidence of acute cerebellar ataxia | "estimated at 1:100,000 to 1:500,000 children per year" | **[S]** ⚠️ Repeated across reviews; primary source **not** located. Treat as uncited until traced. Normalises to roughly **0.2–1.0 per 100,000 children per year** (`measure_type: ANNUAL_INCIDENCE`, `rate_denominator: POPULATION_PER_YEAR`) |
| Share of all childhood acute ataxia | **61.1%** (157/257), China, 2025 | **[P]** PMID:41321459 — the largest single-centre series |
| Share of all childhood acute ataxia | **38.0%** (95% CrI 35.3–40.8%) | **[S]** Jones C, Amendum P, DelVecchio M, Aronoff S. *Etiologies of Acute Ataxia in Children: A Systematic Review of 1167 Subjects.* *J Child Neurol* 2025, doi:10.1177/08830738251396192. ⚠️ Figure from a search summary only |
| Share of all childhood acute ataxia | **35.5%** (27/76), Serbia | **[V]** PMID:38008790 ("immune-mediated/infective cerebellar ataxia") |
| Share of all childhood acute ataxia | "approximately 50% to 60% of total cases" / "30% to 50%" | **[S]** review-level ranges |
| Risk after natural varicella | "one in 4,000 children with varicella" | **[S]** ⚠️ untraced |
| Risk after varicella vaccination | "1.5 in 1,000,000 doses" | **[S]** ⚠️ untraced |
| Share of progressive cerebellar ataxias | "approximately 1%" | **[S]** ⚠️ From a MalaCards/Orphanet-derived summary. **Logically suspect**: this disease is not progressive, so the denominator does not contain it. Do not use |

⚠️ **The three "untraced" rows above are the weakest numbers in this report and the most likely to be copied uncritically into a KB entry.** Each is a quantitative claim circulating through secondary reviews. If a primary source cannot be found, the correct encoding is `prevalence_class: NOT_YET_DOCUMENTED` with the figures recorded in `notes:` and attributed to the review that carried them — not a `rate_per_100000` presented as measured.

### 9.3 Population demographics

- **Sex ratio:** a consistent, modest male excess. 54% male (n=39) **[V]**; 55% male (n=124) **[P]**; M:F 1.14:1 (n=257) **[P]**; sex ratio 1.17 (n=37) **[S]**; 10 boys : 5 girls (n=15) **[V]**; 35 boys : 23 girls (n=58) **[S]**. ⚠️ The pooled case-report figure is far more extreme — "of 70 patients with sex reported, 51 (72.9%) were male" **[V]** — and that is **publication bias, not biology**. Record the cohort figures (~1.1–1.2:1), not the pooled one.
- **Age distribution:** see §3.4. Age-stratified aetiology from the 257-patient series **[P]**: 0–3 y — APCA 66.1%, drug intoxication 14.3%, ADEM 8%; 4–6 y — APCA 62.9%, ADEM 13.5%, AC 7.9%; 7–14 y — APCA 48.2%, AC 21.4%, drug intoxication 14.3%. **The APCA share falls and the AC share rises with age** — a genuine, useful gradient.
- **Affected populations / ethnic groups:** no ethnic or ancestry predilection reported. Cohorts come from Italy, Turkey, Tunisia, Serbia, Israel, Australia, China and the USA, with broadly similar pictures. There is nothing to bind to HANCESTRO and **nothing should be**.
- **Geographic distribution:** worldwide, with no endemic focus. The only true geographic variation is **secondary to vaccination policy** — in high-varicella-vaccine-coverage settings VZV essentially disappears as a trigger **[V]** and respiratory pathogens take over **[S]**. This is a health-system variable, not a geographic one.
- **Variant geography:** not applicable.

---

## 10. Diagnostics

### 10.1 The diagnosis is clinical, by exclusion

There are **no validated, society-published diagnostic criteria**. What exists is a recurring operational definition. Nussinovitch's is the clearest statement of the exclusion logic:

> "The diagnosis of acute cerebellar ataxia was based on the following criteria: acute onset of ataxia with or without nystagmus; absence of known genetic predisposing factors, such as familial degenerative disorders; and absence of drug intoxication, bacterial meningitis, and metabolic disorders." **[V]** PMID:14552515

And for the cerebellitis end of the spectrum:

> "the term acute cerebellitis is now defined as 'an acute neurologic condition characterized by cerebellar ataxia or dysfunction that is attributable to recent or concurrent infective illness, a recent vaccination, or ingestion of medication, and in which there is MRI evidence of predominantly cerebellar inflammation'." **[S]**

**Note what the second definition includes that the first excludes: "ingestion of medication".** The two operational definitions disagree on whether a drug-associated case counts. Worth a `notes:` line.

### 10.2 Clinical tests

| Modality | Role and findings |
|---|---|
| **MRI brain, with contrast** — `NCIT:C16809` | The pivotal investigation. Normal in ACA; in AC, "hyperintense signal of cerebellar gray matter in T2-weighted sequences, which is a strong indication of a diagnosis of acute cerebellitis" **[P]** PMID:11826604; bilateral symmetrical cortical T2 hyperintensity with swelling **[V]**; leptomeningeal enhancement; three patterns (§7.4). **Its real diagnostic job is excluding a posterior-fossa tumour** — "Acute cerebellitis is a severe subtype of acute cerebellar ataxia that includes MRI changes that may be confused with tumors" **[S]** — and the discriminator is serial imaging: "Clinical improvement and regression of the pathological findings on serial MRI can help to differentiate acute hemicerebellitis from a neoplastic process" **[S]** |
| **CT head** | Used where MRI is unavailable or urgency demands; pathological in 2/28 in one cohort **[P]** |
| **Lumbar puncture** — `NCIT:C15327` | ⚠️ **Contraindicated until mass effect is excluded** — tonsillar herniation was present in 73.3% of one AC series **[V]**. When done: mild lymphocytic pleocytosis, normal or mildly raised protein, normal glucose. Only 19.5% of one paediatric cohort had an LP **[P]**. CSF findings did **not** correlate with outcome: "There was no correlation among symptoms, cerebrospinal fluid findings, clinical outcome." **[V]** |
| **CSF oligoclonal bands** | The most interesting newer test — positive in 31.2% of APCA and predictive of relapse (20.8% vs 0%, P=0.001) **[P]**. ⚠️ Single-centre, needs replication |
| **Pathogen testing** | Serology and PCR for VZV, EBV, *M. pneumoniae*, influenza, SARS-CoV-2, HHV-6, enteroviruses, CMV; throat swab and CSF PCR. **Expect a negative result** — aetiology unidentified in 51% **[S]**, 24.7% **[V]**, and 11/15 **[V]**. "The cause of acute cerebellitis remains unknown in about two-thirds of the cases." **[S]** |
| **Autoantibody panel** | Anti-GluRδ2 (serum and CSF), anti-GQ1b, anti-GAD65, paraneoplastic/neuronal-surface panel. Detected in up to 28% **[S]**; anti-GQ1b testing specifically recommended after infection **[S]**. ⚠️ Anti-GluRδ2 is a research assay, not routinely available |
| **EEG** | Non-contributory: EEG findings showed no correlation with sequelae (P > 0.05) **[V]** |
| **Biopsy / histopathology** | **Not a diagnostic test.** Tissue comes only from decompressive resection or autopsy. Findings in §6.1 step 4b: T-cell infiltration of the molecular layer, CD8 T cells co-localising with Purkinje-cell loss, leptomeningeal lymphoplasmacytic exudate, white matter spared **[S]** |
| **Urine/serum toxicology** | Essential — intoxication is the second commonest cause of paediatric acute ataxia (10.9% **[P]**, 31.6% **[V]**) |
| **Urinary catecholamines + abdominal/thoracic imaging** | Required whenever opsoclonus or myoclonus is present — see §10.4 |

**LOINC codes:** ⚠️ **None are supplied here, deliberately.** CSF cell count, CSF protein, CSF oligoclonal bands, VZV IgM/IgG and *M. pneumoniae* IgM all have LOINC codes, but the repository's LOINC prefix is not yet routed in `conf/oak_config.yaml`, so a typed label fails `test_committed_loinc_labels_match_the_cache` even when correct. Run `just loinc-seed-cache <file>` then `just normalize-cache` and commit `cache/loinc/terms.csv` with the entry.

### 10.3 Genetic testing

**No genetic test diagnoses this disease.** Genetic testing appears only in the differential: WES/WGS, ataxia gene panels, repeat-expansion testing and mitochondrial DNA testing are used to **exclude** inherited ataxias when the course is atypical or recovery does not occur. Nussinovitch's rule is the practical one:

> "Imaging studies are needed only in atypical presentation or if there is no spontaneous improvement after 1 to 2 weeks." **[V]**

By the same logic genetic testing is indicated only once the presumption of a self-limited post-infectious process has failed. Chromosomal microarray, karyotyping and FISH have no role. **No newborn or carrier screening applies.**

### 10.4 Differential diagnosis

Ranked by frequency from the two largest paediatric aetiology series (**[P]** n=257; **[V]** n=76):

| Alternative diagnosis | Frequency | Distinguishing features |
|---|---|---|
| **Drug/toxin intoxication** | 10.9% **[P]**; 31.6% **[V]** | Toxicology; altered consciousness out of proportion to ataxia; no prodrome |
| **ADEM** | 9.7% **[P]** | Multifocal white-matter lesions; encephalopathy is required for the diagnosis; MOG-IgG |
| **Acute cerebellitis** (vs ACA) | 8.2% **[P]** | Headache + vomiting + abnormal MRI — the discriminator in PMID:32160830 **[V]** |
| **Opsoclonus–myoclonus–ataxia syndrome** | 1.2% (as anti-GQ1b) / listed **[V]** | **Opsoclonus is the red flag.** "Opsoclonus-myoclonus-ataxia syndrome is associated with a tumor, such as a neuroblastoma or ganglioneuroma, in 40-50% of cases." **[S]** Missing it means missing a tumour — one reported patient "was diagnosed with neuroblastoma upon third relapse" **[S]**. Bind `HP:0010543` Opsoclonus, `HP:0001336` Myoclonus |
| **Posterior fossa tumour** | 2.3% **[P]** | MRI; progressive rather than monophasic; "AA might be the first manifestation of CNS neoplasm or paraneoplastic phenomena" **[V]** |
| **Genetic/metabolic ataxia (incl. episodic ataxia)** | 2.7% **[P]** | Family history; recurrence; no prodrome; failure to recover |
| **Vestibular ataxia / labyrinthitis** | listed **[V]** | Vertigo, hearing symptoms, no limb dysmetria |
| **Guillain–Barré / Miller Fisher / Bickerstaff** | — | Areflexia, ophthalmoplegia, anti-GQ1b. ⚠️ Overlap is real — anti-GQ1b has been reported in *isolated* cerebellar ataxia, so this boundary is genuinely blurred **[P]** |
| **Infectious cerebellitis / rhombencephalitis** | — | CSF PCR positive; *Listeria* rhombencephalitis "most frequently seen in immunocompetent young adults" **[S]**; brainstem signs |
| **Cerebellar stroke / haemorrhage** | — | Sudden onset, vascular territory; `HP:0011695` Cerebellar hemorrhage |
| **Enteroviral transverse myelitis presenting as acute ataxia** | case series **[S]** | Spinal cord MRI |
| **Myositis mimicking ataxia** | case report **[P]** | One HHV-6/adenovirus case presented with "lower limbs pain" and hypotonia and was initially taken for myositis — PMID:25425177 |
| **Conversion/functional and post-ictal ataxia** | excluded by definition **[V]** | — |
| **Paraneoplastic cerebellar degeneration** | — | Progressive, antibody-positive, tumour present |

**Adult-specific additions** **[S]**: "metabolic, vascular, neoplastic, inflammatory, autoimmune and infective causes"; in HIV, "opportunistic infections, non-Hodgkin lymphoma and metastases, paraneoplastic diseases and postinfectious immune-mediated processes"; Wernicke encephalopathy and alcohol-related cerebellar degeneration should be added on clinical grounds though no source read names them.

### 10.5 Screening

**No screening programme exists and none is appropriate.** The disease is acute, sporadic, unpredictable and self-limited; there is no presymptomatic state to detect, no genetic risk to cascade, and no asymptomatic carrier. Newborn screening, carrier screening, PGD and prenatal testing are all **not applicable**. The one legitimate "screening" activity is **tumour screening for neuroblastoma when opsoclonus-myoclonus is present** — but that screens for a different disease.

---

## 11. Outcome / Prognosis

### 11.1 Survival and mortality

**Mortality is very low but not zero, and is concentrated entirely in the fulminant subtype.**

> "Complete recovery occurred in 47/73 patients (64.4%), partial recovery/residual deficit in 15/73 (20.5%), outcome was not stated for 10/73 (13.7%), and one death (1.4%) was recorded (COVID-19-associated necrotizing encephalopathy) - the only fatality, occurring in an adult." **[V]** PMID:42649322

Subtype-resolved: "34 patients (46.6%) were classified as acute cerebellar ataxia (ACA), 26 (35.6%) as acute cerebellitis (AC), and 13 (17.8%) as acute fulminant cerebellitis (AFC), with complete recovery in 58.8%, 69.2%, and 69.2% of each subtype, respectively, and the cohort's only death occurring in the AFC subgroup." **[V]**

⚠️ Note the counter-intuitive result: complete recovery was *higher* in AC and AFC (69.2%) than in ACA (58.8%). The likeliest reading is ascertainment — mild ACA cases are published only when something goes wrong — but the review does not explain it, and **it should not be reported as evidence that severe disease does better**.

Other mortality data: zero deaths in 35 adults ("All patients survived" **[P]**); zero in 15 children with AC ("The absence of fatalities in our series" **[V]**); zero in 124 Italian children **[V]**; zero in 73 and 39 children **[V]**. Against this, "Pediatric Fulminant Cerebellitis Is Still a Fatal Disease that We Know Little About!" **[V]** PMID:33454719, and AFC carries "a high risk of death due to compression of the posterior fossa, acute hydrocephalus, and intracranial hypertension" **[S]**.

No 5- or 10-year survival figure exists or is meaningful: the disease is acute and non-recurrent, and survivors have normal life expectancy. SEER, GBD and CDC Wonder hold nothing for it.

### 11.2 Morbidity, function and recovery

**The sequelae rate depends entirely on which end of the spectrum is counted — this is the single most important prognostic fact.**

| Population | Sequelae rate |
|---|---|
| Mixed ACA/AC paediatric, n=124 | "Neurological sequelae were reported in 6 cases (5%)" **[V]** |
| ACA only, n=39, ≥1 y follow-up | "complete in all children without any neurologic sequelae" **[V]** |
| ACA/mixed, n=73 → 60 followed ≥4 mo | "Ninety-one percent (55/60) of these, including all children with chickenpox, recovered completely from ataxia." **[V]** |
| Mixed acute ataxia, n=76 | "Complete recovery was experienced by 62 (81.6%) patients." **[V]** |
| **Acute cerebellitis only, n=15** | **"Acute cerebellitis heals with sequelae in about one-third of cases."** / 27% at median 12 months **[V]** |
| **Acute cerebellitis only, n=11** | **Neurological sequelae in 5/11; cognitive deficits in 6/11** **[V]** |
| **Adults, n=35** | **"14 out of 30 patients (47%) ended up with neurological sequelae."** **[P]** |
| Pooled case-level, n=73 | 20.5% partial recovery/residual deficit **[V]** |

So: **~5–9% after ACA, ~27–45% after AC, ~47% in adults.** Any single sequelae figure for "postinfectious cerebellitis" without the subtype attached is misleading.

**Nature of the sequelae:**
- Motor — persistent ataxia (commonest), balance disturbance, dysarthria, hypotonia, tremor. The Italian series lists them individually: "ataxia in 3 cases, balance disturbances and dysarthria in 1 case, ataxia and balance disturbances in 1 case, and ataxia and hypotonia in 1 case" **[P]**.
- Cognitive/affective — "cognitive deficits were found in six patients" of eleven, affecting "spatial visualization ability, language skills, and concentration" **[V]**; and the Liverpool Outcome Scale was reduced in all 7 children followed to 12 months **[V]**. These are CCAS-pattern deficits.
- Radiological — cerebellar atrophy. 9/12 on follow-up MRI in an AC series **[V]**; ~25% long-term **[S]**; up to half in hemicerebellitis **[S]**; follow-up MRI abnormal in 71% of adults **[P]**.
- Relapse — in the CSF-OCB-positive subgroup (20.8% vs 0%) **[P]**.

**Recovery timeline:** "Full gait recovery took less than 2 weeks on average, and the longest duration of neurologic signs was 24 days" **[V]**; "full gait recovery required about 2 months in most cases" in the IMCA review **[P]** — note these two disagree, the second being drawn from a severity-enriched population. "The symptoms of CCAS are often moderately severe following acute injury in adults and children, but tend to lessen with time." **[S]**

**Formal outcome instruments used:** Liverpool Outcome Scale **[V]**; parental cognitive questionnaires **[V]**. No EQ-5D, SF-36, PROMIS, SARA or ICARS data for this disease were found. No ICF-coded disability data.

### 11.3 Prognostic factors

**Favourable:**
- Pure cerebellar syndrome without extracerebellar signs — "Forty-two (56%) cases experienced isolated CS" and isolated CS predicted good outcome **[V]**
- Normal MRI/CT at admission **[V]**
- Varicella as the trigger — "all children with chickenpox, recovered completely" **[V]**; 100% in post-varicella vs 89% in non-varicella **[S]**
- Younger age (paediatric vs adult: 5–27% vs 47% sequelae)
- Early treatment while cerebellar reserve is preserved **[S]**

**Unfavourable — the two statistically confirmed factors:**
> "multivariate logistic regression analysis which also showed that presence of 'cerebellar plus symptoms' (p = 0.021) and structural abnormalities (p = 0.002) is related to a poor outcome." **[V]** PMID:38008790

> "Children with pathological magnetic resonance imaging (MRI) or computed tomography (CT) had a higher probability of having clinical sequelae." … "Pathological MRI or CT findings at admission correlate to neurological sequelae." **[V]** PMID:28606112

Also unfavourable: **cerebellar atrophy on follow-up** ("almost always associated with long-term motor and/or cognitive deficits" **[S]**; all 3 of 8 AC patients who developed atrophy had persistent sequelae **[S]**); adult age; fulminant presentation with hydrocephalus; CSF OCB positivity (for relapse) **[P]**.

**⚠️ A direct contradiction in the literature that must be recorded, not resolved by preference.** Lancella 2017 found abnormal admission imaging predicted sequelae **[V]**; Yildirim 2020 found the opposite for follow-up imaging — "MRI results were not found to be predictive of outcome." **[V]** These are not the same claim (admission vs follow-up imaging; mixed ACA/AC vs AC-only; n=124 vs n=15), and the honest encoding is both statements with their populations attached.

**Prognostic biomarkers:** CSF oligoclonal bands for relapse **[P]** is the only candidate. No FDA-listed biomarker. No validated prognostic model or clinical calculator.

---

## 12. Treatment

### 12.1 The evidence situation

**There is no randomised controlled trial of any treatment for this disease, and no validated protocol.**

> "There is currently no standardized or validated treatment protocol for pediatric acute cerebellitis, with management based on immunomodulatory agents including corticosteroids and IVIG." **[S]**

> "Treatment was decided independently case by case." … "Randomized controlled trials are needed to confirm these observations. The ultimate goal of these studies could be to develop a standardized protocol on AC/ACA." **[V]** PMID:28606112

Everything below is practice, not evidence. **This should be said plainly in the entry rather than implied by hedged `description` wording.**

### 12.2 Treatment algorithm

**Tier 0 — Observation and supportive care.** The default for ACA.
> "The treatment of acute cerebellar ataxia is largely supportive, and because it is a self-resolving condition, no treatment is usually warranted. However, the role of steroids or antivirals is controversial and often utilized on a case-by-case basis." **[S]**
> "Since PIC is self-limiting, close observation of the patient is recommended." **[P]**
> "Close observation and checking for stabilization and improvement (for instance following surgical intervention in case of edema of the posterior fossa) are recommended. Antibiotics may be required. Only when the symptoms persist, immunotherapies using corticosteroids, IVIg, immunosuppressants, and/or plasma exchange, either alone or in combination, are indicated." **[P]** — Mitoma H, Manto M, Hampe CS. *Curr Neuropharmacol* 2019;17(1):33-58. PMID:30221603
→ `NCIT:C15747` Supportive Care

**Tier 1 — Corticosteroids.** The commonest intervention, and the only one with any consistent claim of benefit.
- Frequency: 74.0% (54/73) pooled **[V]**; 14/15 in an AC series **[V]**; 46% (16/35) of adults **[P]**; 33% (41/124) of mixed paediatric cases **[V]**
- Claimed benefit: "The absence of fatalities in our series suggests early diagnosis, and steroid treatment can increase the chance of recovery." **[V]** / "early steroid treatment for acute cerebellitis might have been effective to prevent the progress of the disease and improve the prognosis." **[P]**
- ⚠️ Both are **uncontrolled inferences from single-arm series**. The repository's own evidence rules mean such a claim is `directness: INDIRECT` at best.
→ `NCIT:C122080` Systemic Corticosteroid Therapy; `NCIT:C15986` Pharmacotherapy; agents `CHEBI:6888` (label `6alpha-methylprednisolone`), `CHEBI:41879` dexamethasone, `CHEBI:8378` prednisolone, class `CHEBI:50858` corticosteroid; NCIT drugs `NCIT:C647` Methylprednisolone, `NCIT:C422` Dexamethasone, `NCIT:C769` Prednisolone
- ⚠️ **Do not bind `NCIT:C2322` Corticosteroid as a `therapeutic_agent`** — the repository's `ChemicalEntityTerm` enum is rooted at `NCIT:C1909` Pharmacologic Substance and NCIT files C2322 under Hormone, so it fails term validation. Use `CHEBI:50858`.

**Tier 2 — IVIG.** Second-line or added to steroids.
- Frequency: 26.0% (19/73) pooled **[V]**; 8/15 in an AC series **[V]**
- ⚠️ **The one negative signal in the whole treatment literature:** "In another series, approximately half of the patients with acute cerebellitis were treated with IVIG with no additional benefit." **[S]** This is a `REFUTE`-direction observation and should be carried as such, not omitted.
→ `NCIT:C121331` Intravenous Immunoglobulin Therapy; `NCIT:C62710` Immunoglobulin Therapy; agent `NCIT:C80829` Human Immunoglobulin G

**Tier 3 — Plasma exchange.** Refractory cases only. "plasma exchange was given for refractory cases." **[V]**
→ `NCIT:C15304` Plasmapheresis

**Tier 4 — Other immunosuppression.** Rituximab and other immunosuppressants are named in the IMCA framework ("corticosteroids, IVIg, plasmapheresis, and rituximab, either alone or in combination" **[P]**), but no case series of their use in this disease was found.
→ `NCIT:C15261` Immunosuppressive Therapy; `NCIT:C1702` Rituximab; `NCIT:C290` Azathioprine

**Tier 5 — Pathogen-directed therapy.** Given on suspicion rather than proof, since the mechanism is post-infectious.
- Aciclovir in 65% (81/124) of the Italian cohort **[P]** — a striking figure given VZV was diagnosed in 53%
- Antivirals in 47.9% (35/73) pooled **[V]**
- Oseltamivir for influenza: "given oseltamivir, 75 mg orally twice daily for 5 days" **[P]**
- Macrolide/tetracycline for *M. pneumoniae* (implied; no dosing source read)
→ `NCIT:C205` Acyclovir; `CHEBI:2453` acyclovir; `CHEBI:35854` valacyclovir. ⚠️ Oseltamivir, azithromycin and doxycycline CURIEs **need lookup**.

**Tier 6 — Neurosurgical rescue.** For AFC only, and this is where the time pressure is.
> "In cases of severe hydrocephalus in acute cerebellitis, it is recommended to immediately undergo neurosurgical treatments, such as external ventricular drainage, ventricular peritoneal shunt, and posterior fossa decompression." **[S]**
> "In acute cerebellitis with a fulminant course, the life-threatening volume and pressure increase in the posterior fossa could be controlled by resection of the cerebellar vermis with a favourable neurologic prognosis, and decompressive surgery may be life-saving in selected cases of cerebellitis with a fulminant course." **[S]**
> "However, functional outcomes after posterior fossa decompression surgery are generally not good." **[S]**
> Adjuncts reported: "neuroprotective measures, osmotherapy, broad-spectrum antibiotics, and CSF diversion" **[P]** PMID:33454719
- Reassuringly, "No patient required surgical decompression" in the 15-patient AC series **[V]** — the intervention is for the 10–18% fulminant tail.
→ `NCIT:C15656` Neurosurgical Procedure; `NCIT:C168483` Ventriculoperitoneal Shunt Placement; `NCIT:C182204` Third Ventriculostomy; `NCIT:C51791` Craniectomy; `NCIT:C15329` Surgical Procedure. ⚠️ External ventricular drainage and suboccipital/posterior-fossa decompression CURIEs **need lookup**.

**Tier 7 — Rehabilitation.** Underdocumented but relevant given a ~27–47% sequelae rate. A COVID-19-associated cerebellitis rehabilitation outcome case report exists **[S]**.
→ `NCIT:C15315` Rehabilitation; `NCIT:C15302` Physical Therapy. Speech and occupational therapy CURIEs are in CLAUDE.md's mechanical-backfill table (`NCIT:C159273`, `NCIT:C121351`) but were **not verified this session** — look them up.

### 12.3 Advanced and experimental therapeutics

- **Gene therapy, cell therapy, RNA-based therapy, targeted therapy, checkpoint immunotherapy:** **none, and none in development.** Not applicable to an acute self-limited immune syndrome.
- **Pharmacogenomics:** nothing specific. No PharmGKB or CPIC guidance.
- **Clinical trials:** **no interventional trial for this disease was identified** on ClinicalTrials.gov, the EU register or WHO ICTRP. There is no NCT number to record.
- **One case-report-level novel agent:** efgartigimod (an FcRn antagonist) in acute cerebellar ataxia — "The utilization of efgartigimod in the treatment of acute cerebellar ataxia: a case report" **[S]**, PMC12420292. Mechanistically coherent (accelerates IgG clearance) in an antibody-mediated disease. **n=1 — a lead, not a treatment.**
- **Preclinical targets from the mechanistic work** (all animal/in-vitro, none translated): rifampicin and trans-cinnamaldehyde ("Rifampicin and trans-cinnamaldehyde (TCA) inhibit microglial activity by blocking the NF-kB signaling pathway" **[P]**); rifaximin ("the infiltration of T-lymphocytes and macrophages into the cerebellum can be prevented by an antibiotic Rifaximin" **[P]**); microglia inhibitors; oxytocin; potassium-channel blockers, with an explicit caution — "4-AP treatment may cause the modification of the activity of Purkinje neurons and induce serious side effects" **[P]**. ⚠️ These are hypotheses from a review of a rodent model. **If any of this enters the entry it must be as a `discussions:` knowledge gap or a `proposed_experiments` block, never as a treatment row.**

### 12.4 Adverse events

No disease-specific adverse-event data. The relevant class effects (corticosteroid toxicity, IVIG thrombosis/aseptic meningitis/renal, plasma exchange line and haemodynamic complications, surgical morbidity) are not documented in any source read here for this population. FAERS holds nothing specific. **Say "not reported for this disease" rather than importing generic class toxicity as if it were disease-specific.**

---

## 13. Prevention

### 13.1 Primary prevention

**Varicella vaccination is the only established primary-prevention measure, and it works.** The mechanism is trigger removal, and the Australian national surveillance data is the evidence: in a population with 65% varicella vaccination among cases, "none were related to varicella or were temporally related to varicella vaccination or other childhood vaccines" **[V]**, against a historical baseline where varicella accounted for up to 25% of cases **[V]** and 26–53% in individual series **[V/P]**.

Quantitatively: "The association of acute cerebellar ataxia with varicella infection is at least 35 times higher than after vaccination." **[S]** ⚠️ untraced.

→ `NCIT:C15346` Vaccination (⚠️ **not verified this session** — look it up); modality `VACCINE`
→ The varicella vaccine itself is a residual, far smaller risk (§2.4), so the honest framing is **net strongly protective**, not risk-free.

Other immunisations plausibly reduce risk by removing triggers — MMR (mumps caused 20% of one pre-MMR-era series **[V]** and the longest symptom duration recorded, 24 days **[V]**), influenza vaccine, and COVID-19 vaccine. **No source read demonstrates a reduction in cerebellitis incidence for any of these**, so the claim must be recorded as inference, not finding.

No risk-factor modification, behavioural intervention, dietary intervention or chemoprophylaxis exists. **No prophylactic medication.**

### 13.2 Secondary prevention

No screening programme is possible (§10.5). What functions as secondary prevention is **early recognition and early treatment within the cerebellar-reserve window** — the practice argument for prompt MRI and, in the AC/AFC tiers, prompt immunotherapy and prompt CSF diversion. The relevant published recommendation is the Italian one:

> "These findings suggest the indication to perform an instrumental evaluation in all patients with AC/ACA at admission to identify those at higher risk of neurological outcome. These patients may benefit from a more aggressive therapeutic strategy and should have a closer follow-up." **[V]** PMID:28606112

**Risk stratification tool:** the Lancella clinical score (§8.2) plus the Kravljanac red-flag list (§3.2) are the two published stratification instruments. Neither is externally validated.

### 13.3 Tertiary prevention

Preventing complications in established disease: monitoring for hydrocephalus in AC with a low threshold for CSF diversion; avoiding lumbar puncture before mass effect is excluded; rehabilitation to limit functional consequences of residual ataxia; and neuropsychological follow-up, since cognitive sequelae are both common and easily missed. For the OCB-positive subgroup, awareness of the relapse risk **[P]**.

### 13.4 Genetic counselling and public health

- **Genetic counselling: not applicable.** No heritable risk, no recurrence risk, no family planning implication. `NCIT:C15240` Genetic Counseling should **not** appear in this entry.
- **Public health interventions:** childhood immunisation programmes (the effective lever); general respiratory-infection control measures. No vector control, sanitation or environmental intervention applies.

---

## 14. Other Species / Natural Disease

**There is no recognised naturally occurring animal counterpart of human postinfectious *immune-mediated* cerebellitis.** What the veterinary literature offers is a set of **contrasts** — infectious cerebellar diseases with different mechanisms — and they are genuinely informative as comparative pathology, but they are not models of this disease and should not be curated as if they were.

| Species | NCBITaxon (verified) | Disease | Mechanism — and why it is *not* this disease |
|---|---|---|---|
| Cat | **NCBITaxon:9685** `Felis catus` | Feline panleukopenia virus cerebellar hypoplasia | **Direct viral destruction of proliferating cells**, not immune-mediated: "Perinatal infections with feline panleukopenia virus (FPV) have long been known to be associated with cerebellar hypoplasia in kittens due to productive infection of dividing neuroblasts." "FPV may induce a granuloprival cerebellar hypoplasia in cats when the virus infects fetuses during the last 3 weeks of gestation or kittens during the 3 first weeks of life." **[S]** FPV proteins have been identified in Purkinje-cell nuclei **[S]**. The target is the proliferating **external granular layer**, the timing is developmental, and the outcome is hypoplasia — all three differ from the human disease |
| Cattle | **NCBITaxon:9913** `Bos taurus` | BVDV cerebellar hypoplasia | **Transplacental teratogenesis**: "Bovine viral diarrhea (BVD) has been associated to acquired cerebellar hypoplasia due to viral infection during the second trimester of pregnancy." "The most frequent lesion was cerebellar hypoplasia, being present in 25 out of 33 (76%) of the animals." **[S]** Again developmental, not post-infectious autoimmune |
| Dog | **NCBITaxon:9615** `Canis lupus familiaris` | Canine distemper virus CNS disease | **Demyelinating leukoencephalitis** — the *opposite* lesion distribution: "Acute and chronic demyelinated plaques were observed in the white matter, while apoptosis occurred particularly in the granular layer of grey matter." **[S]** The human disease spares white matter |
| Dog | **NCBITaxon:9615** | *Neospora caninum* non-suppurative cerebellitis | A single documented case of "Non-suppurative cerebellitis and cerebellar atrophy due to Neospora caninum infection in a Labrador Retriever mix" **[S]** — the closest veterinary analogue in lesion type, but parasitic and directly infectious |

- **Breed (VBO):** no breed predisposition to an immune cerebellitis is recorded. Note the *genetic* traps here: hereditary cerebellar cortical abiotrophy and the Coton de Tulear hereditary cerebellitis/ataxia are **inherited** diseases and must not be conflated with this one.
- **Orthologous genes:** not applicable in the causal sense. For mechanism genes, mouse orthologs would be needed on any `animal_models[].genes` — and ⚠️ `cache/mgi/terms.csv` holds **none** of `Grid2`, `Gad2`, `Tnf`, `Kcnn2`, `Grm1` or `Tlr4`. Every MGI ID must be looked up at the Alliance and the cache rows committed; `just check-gene-namespaces` will not catch a wrong MGI label offline, and the repository's history records three MGI bindings reaching `main` with the right symbol on the wrong gene.
- **OMIA:** no OMIA phene for an immune-mediated post-infectious cerebellitis was identified.
- **Evolutionary conservation:** the cerebellar circuit (Purkinje → deep nuclei), SK-channel control of Purkinje firing, and the microglia–Bergmann glia–mGluR1 relay are all conserved across mammals, which is what makes the rodent work in §15 relevant at all.
- **Zoonotic potential / cross-species transmission:** **not applicable.** The disease is not transmissible. Several *triggers* are zoonotic or have animal reservoirs, but that is a property of the pathogens, not of this syndrome. **Do not record a `transmission` route for this entry** — per the infectious-disease granularity ladder (design decisions §3e), a post-infectious immune sequela is out of scope for the microbial-entry requirements and is "counted, not assessed" by `check-granularity`.

---

## 15. Model Organisms

### 15.1 The honest summary

**There is no animal model of postinfectious cerebellitis that reproduces the human disease.** What exists is a model of *acute cerebellar inflammation* that produces the wrong phenotype, plus a set of passive-transfer antibody models for *other* immune cerebellar ataxias. Both are useful; neither recapitulates this entry's defining feature, which is ataxia following an infection.

### 15.2 The LPS acute cerebellar inflammation model — and its explicit failure to recapitulate

**System:** direct cerebellar-cortical exposure to lipopolysaccharide or heat-killed Gram-negative bacteria in mouse (`NCBITaxon:10090`) and rat (`NCBITaxon:10116`), with two-photon FRET ATP imaging, slice electrophysiology and resting-state fMRI.

> "Activated microglia via exposure to bacterial endotoxin lipopolysaccharide or heat-killed Gram-negative bacteria induce a potentiation of the intrinsic excitability in Purkinje neurons, which is suppressed by microglia-activity inhibitor and microglia depletion. An inflammatory cytokine, tumor necrosis factor alpha (TNF-α), released from microglia via toll-like receptor 4, triggers this plasticity. Our two-photon FRET ATP imaging shows an increase in ATP concentration following endotoxin exposure. Both TNF-α and ATP secretion facilitate synaptic transmission. Region-specific inflammation in the cerebellum in vivo shows depression- and autistic-like behaviors. Furthermore, both TNF-α inhibition and microglia depletion revert such behavioral abnormality. Resting-state functional MRI reveals overconnectivity between the inflamed cerebellum and the prefrontal neocortical regions. Thus, immune activity in the cerebellum induces neuronal hyperexcitability and disruption of psychomotor behaviors in animals." **[V]** PMID:31509752

**What it recapitulates:** the microglial activation, the TNF-α/TLR4 effector step, the SK-channel downregulation, and plausibly the cognitive/affective sequelae.

**What it fails to recapitulate — stated by the authors themselves:** "animals did not show any ataxia but hyperexcitability in the cerebellar cortex and depression-like behaviors" **[P]**. And the control experiment sharpens it: "Stimulation of microglia by LPS-exposure in the cerebellar cortex and the resultant hyperexcitability of Purkinje cells were not sufficient to induce cerebellar ataxia, although the injection of 200 nM apamin to the cerebellar anterior lobes induced ataxia." **[P]**

**This is a textbook case for `relationship: FAILS_TO_RECAPITULATE`** on an `Ataxia`/`Gait ataxia` node (with the required `limitations` and `evidence`), alongside `relationship: RECAPITULATES` on the microglia/TNF-α mechanism nodes. The scale slots matter here too: the model observes `CELLULAR` and `MOLECULAR` state, so linking it to an organism-level ataxia node is an upward extrapolation requiring a caveat, and a `SCALE_EXTRAPOLATION` divergence would have to agree with the scale slots. The accompanying `discussions:` entry should be `kind: HUMAN_MODEL_MISMATCH`, not `KNOWLEDGE_GAP` — evidence exists in the model; what is open is whether the mechanism explains the human ataxia. The authors frame it exactly that way: "there is a gap in our interpretation between the very early phase of cerebellar inflammation and the emergence of cerebellar ataxia." **[P]**

### 15.3 The TNF-α / Bergmann glia slice model

**System:** acute cerebellar slices from juvenile male rat (`NCBITaxon:10116`), plus dissociated cerebellar cortical astrocyte culture; AAV-delivered TNFR1-shRNA for genetic suppression in Bergmann glia.

> "we suggest that tumor necrosis factor α (TNF-α), a key inflammatory cytokine, alters the neural activity of the cerebellar Purkinje cells (PCs) by facilitating gliotransmission in the juvenile male rat cerebellum. A bath application of TNF-α (100 ng/ml) in acute cerebellar slices elevates spiking activity of PCs with no alterations in the regularity of PC firings. Interestingly, the effect of TNF-α on the intrinsic excitability of PCs was abolished under a condition in which the type1 TNF receptor (TNFR1) in Bergmann glia (BG) was genetically suppressed by viral delivery of an adeno-associated virus (AAV) containing TNFR1-shRNA. … Pharmacological inhibition of mGluR1, indeed, prevented the TNF-α-mediated elevation of the intrinsic excitability in PCs." **[P]** PMID:30072733

This is the cleanest mechanistic dissection available and supplies two necessity results (TNFR1 on Bergmann glia; mGluR1 on Purkinje cells). `evidence_source: IN_VITRO` for the slice and culture work.

### 15.4 Viral-infection models with cerebellar involvement

| Model | Species | What it shows |
|---|---|---|
| Influenza A inoculation of 2D2 TCR-transgenic mice | mouse | "the viral infection increased T-cells in the choroid plexus and induced a temporal transcriptomic alteration in the cerebellum" **[P]**; chemokine profile shifts. Closest to a *post-infectious* model, in an autoimmune-prone host |
| DENV-3 infection | mouse | "Cytokine and chemokine levels increase in brain tissue from DENV-3 infected mice. The infection elicits significant increases in IFN-γ, TNF-α, CCL2, CCL5, CXCL1, and CXCL2." **[P]** |
| HCoV-OC43 infection | mouse | "activated microglia and excessive proinflammatory cytokines release cause the downregulation of glial glutamate transporter GLT-1 expression" **[P]** |

None of these is characterised for ataxia.

### 15.5 Passive-transfer antibody models — for *other* immune cerebellar ataxias

These demonstrate that antibody can be directly pathogenic in the cerebellum, which is the key enabling premise for the humoral branch in §6.1 — but **none uses an antibody from a postinfectious cerebellitis patient.**

- **Anti-Cav2.1:** "An anti-Cav2.1 antibody conferred an ataxic phenotype by passive transfer in mice, and mice infused with D-III antibody exhibited cerebellar ataxia, characterized by irregular and excessive steps and skips." **[S]**
- **GAD65:** "intracerebellar administration of GAD65Ab in rats and mice induced ataxic symptoms" **[S]**
- **mGluR1:** "passive transfer experiments in mice strongly indicated a direct pathogenic effect of the antibody with the development of ataxia in the case of mGluR1-associated cerebellar ataxia" **[S]**
- **Sez6L2:** "Immunization with human Sez6L2 induces a moderate ataxia phenotype in mice" **[S]** (2025)
- **Anti-Yo — a documented failure worth recording:** "injection of PCD IgG to mouse brain resulted in IgG uptake by Purkinje cells but without Purkinje cell loss, and injection of PCD IgG together with complement or activated macrophages to rat ventricles did not cause Purkinje cell loss." **[S]** Antibody binding is not sufficient for Purkinje-cell death — which is consistent with the human observation that most cases recover without atrophy.

### 15.6 Genetic models of the autoantigens

`Grid2` (GluRδ2) mouse mutants — *lurcher* and *hotfoot* — have severe cerebellar ataxia and Purkinje-cell degeneration. This is **not** a model of postinfectious cerebellitis, but it establishes that GluRδ2 loss of function produces ataxia, which is what makes the anti-GluRδ2 antibody mechanistically plausible. ⚠️ **No source read this session documents the *lurcher* phenotype** — I know of it, but that is exactly the kind of recalled fact this report must not assert. Verify against MGI before use, and get the `MGI:` ID from the Alliance.

Also relevant: "A transgenic mouse model expressing SK3-1B-GFP, which dominant-negatively suppresses SK channel function, shows the ataxia phenotype." **[P]** — and the contrasting negative: "using Purkinje cell-specific promoter L7, SK2-deletion mice have neither major impairment in locomotion nor show ataxia-like tremors." **[P]**

### 15.7 What is missing, and resources

**No model exists of:** infection → latent interval → cerebellar autoantibody → ataxia → recovery. Building one would need an infectious trigger in an autoimmune-permissive host with ataxia as the readout — the 2D2/influenza work is the nearest start. This is the single most important model-system gap in the disease and belongs in the entry as a `KNOWLEDGE_GAP` discussion with `proposed_experiments`.

**Resources:** MGI, IMPC, IMSR, Alliance of Genome Resources for the mouse lines; no disease-specific model repository, no iPSC or organoid model, and no cell line for this disease. The non-animal (NAM) model space here is empty.

---

## 16. Outstanding lookups, and notes for the curation step

### 16.1 CURIEs that must be resolved before binding — do not write these from memory

| Need | Prefix | Note |
|---|---|---|
| cerebellar hemisphere | UBERON | Absent from `cache/uberon/terms.csv` and from the OLS layer query |
| Cytomegalovirus; adenovirus; *Bordetella pertussis*; *Corynebacterium diphtheriae* | NCBITaxon | Named triggers, not in the repository cache |
| mGluR2 (`GRM2`); NIF | HGNC | The last two names in the autoantibody list |
| SK/KCa channel activity; regulation of membrane potential; molecular mimicry | GO | If no GO term for molecular mimicry exists, **record the search verbatim** rather than writing "no term exists" |
| Oseltamivir; azithromycin; doxycycline; mannitol; hypertonic saline | CHEBI / NCIT | Treatments named in sources |
| External ventricular drainage; posterior-fossa / suboccipital decompression; Vaccination (`NCIT:C15346`); Speech-language therapy (`NCIT:C159273`); Occupational therapy (`NCIT:C121351`) | NCIT | The last three appear in CLAUDE.md's backfill table but were **not** verified this session |
| Mouse orthologs `Grid2`, `Gad2`, `Tnf`, `Kcnn2`, `Grm1`, `Tlr4` | MGI | **None** in `cache/mgi/terms.csv`. Offline validation will not catch a wrong label — use `just check-gene-namespaces-online` and commit the cache rows |
| CSF cell count, CSF protein, CSF oligoclonal bands, VZV IgM/IgG, *M. pneumoniae* IgM | LOINC | LOINC is not routed in `conf/oak_config.yaml`; use `just loinc-seed-cache` then `just normalize-cache` |
| ICD-10 and ICD-11 codes | — | Get from Orphadata, not from a web page. `just refresh-orphadata` → `just structured-rebuild-orphanet --id 624244` |
| ECTO exposure term for viral infection / vaccination | ECTO | ⚠️ Run `l~virus`, `l~varicella`, `l~vaccin`, `l~infectio`, `l~pathogen` and `l~anaesthetic`-style spelling variants, and **write down what each returned** |

### 16.2 Quotes needing re-verification before use as a `snippet:`

Everything tagged **[P]** or **[S]**. In particular, re-read before quoting: all Lancella 2017 symptom percentages (full-text, not abstract); all Fritzler 2003 antibody fractions (the fetch returned fragments with character counts appended); the Mitoma 2021 "reversible AMPA receptor endocytosis" phrasing; the Van Samkar 2017 adult figures; and every row marked **[S]**. The three untraced epidemiology figures in §9.2 are the highest-risk items in this report.

### 16.3 Observations relevant to the entry's structure

- **MONDO's placement is arguably wrong.** MONDO:0850107's hierarchical ancestors are `MONDO:0005550` *infectious disease* → `MONDO:0020010` *infectious disorder of the nervous system* → `MONDO:7770010` *disease of primarily extrinsic mechanism*. It is **not** under `MONDO:0002427` *cerebellar disorder* or under any autoimmune/immune-mediated branch. For a disease whose own Orphanet definition says "immune-mediated mechanisms", classifying it purely as an infectious disease misses the mechanism, and a reader querying MONDO for cerebellar disorders will not find it. This is a candidate for an upstream MONDO report rather than something to work around locally.
- **`has_subtypes` structure:** ACA / AC / AFC (severity, per Gowda 2026's own classification, with subtype-resolved recovery rates) and arguably hemicerebellitis (anatomical, with its own sequela profile). Several phenotypes and the whole prognosis section stratify by these, so the `subtype:` foreign keys will carry real information rather than sitting unused.
- **Granularity ladder (design decisions §3e):** a post-infectious immune sequela is correctly its own entry, not a phase of chickenpox, influenza or COVID-19 — and it is **out of scope** for the ladder's `infectious_agent` + `transmission` requirements, so `check-granularity` should count rather than assess it. Do not add a `transmission:` route.
- **Related entries already in `kb/disorders/`** that this entry will want to sit beside: `Opsoclonus_Myoclonus_Syndrome`, `Acute_Disseminated_Encephalomyelitis`, `Guillain_Barre_Syndrome`, `Paraneoplastic_Cerebellar_Degeneration`, `Autoimmune_Encephalitis`, `Chickenpox`, `Influenza`, `COVID-19`, `Mycoplasma_Encephalitis`, `Viral_Encephalitis`, `Episodic_Ataxia`. A grouping over immune-mediated cerebellar ataxias is a plausible follow-up but is not this entry's job.
- **Three genuine contradictions to carry rather than resolve:** (i) admission imaging predicts sequelae **[V]** vs follow-up imaging does not **[V]**; (ii) complete recovery higher in AC/AFC than ACA in pooled data **[V]**, which contradicts every cohort series; (iii) gait recovery "less than 2 weeks" **[V]** vs "about 2 months in most cases" **[P]**. Each pair differs in population — record both with their populations attached, which is what `subtype:` and `population:` slots are for.

---

## Sources

**Primary literature — verbatim abstracts retrieved this session (NCBI E-utilities)**

- [Post-Infectious Cerebellitis: A Systematic Review of Aetiology, Clinical Presentation, Treatment, and Outcomes — PMID:42649322](https://pubmed.ncbi.nlm.nih.gov/42649322/) · Gowda N, Harish S, Joy J, Tej G. *Cerebellum* 2026;25(5):134. doi:10.1007/s12311-026-02074-3
- [Acute Cerebellitis or Postinfectious Cerebellar Ataxia? Clinical and Imaging Features in Acute Cerebellitis — PMID:32160830](https://pubmed.ncbi.nlm.nih.gov/32160830/) · Yildirim M, et al. *J Child Neurol* 2020;35(6):380-388
- [Acute cerebellitis in children: an eleven year retrospective multicentric study in Italy — PMID:28606112](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5469162/) · *Ital J Pediatr* 2017;43(1):54
- [Postinfectious Acute Cerebellar Syndromes in Children: A Nationally Ascertained Case Series From Australia 2013–2018 — PMID:35546546](https://pubmed.ncbi.nlm.nih.gov/35546546/) · Gunaratna GPS, et al. *J Child Neurol* 2022;37(7):617-623
- [Course and outcome of acute cerebellar ataxia — PMID:8210223](https://pubmed.ncbi.nlm.nih.gov/8210223/) · Connolly AM, Dodson WE, Prensky AL, Rust RS. *Ann Neurol* 1994;35:673-679
- [Post-infectious acute cerebellar ataxia in children — PMID:14552515](https://pubmed.ncbi.nlm.nih.gov/14552515/) · Nussinovitch M, et al. *Clin Pediatr* 2003;42(7):581-584
- ["The Red Flags" in Clinical Approach to Acute Ataxia — PMID:38008790](https://pubmed.ncbi.nlm.nih.gov/38008790/) · Kravljanac R, et al. *Cerebellum* 2024;23(4):1321-1327
- [Long-term outcome of children with acute cerebellitis — PMID:22936351](https://pubmed.ncbi.nlm.nih.gov/22936351) · Hennes E, et al. *Neuropediatrics* 2012;43(5):240-8
- [Microglia-Triggered Plasticity of Intrinsic Excitability Modulates Psychomotor Behaviors in Acute Cerebellar Inflammation — PMID:31509752](https://pubmed.ncbi.nlm.nih.gov/31509752/) · Yamamoto M, Kim M, Imai H, Itakura Y, Ohtsuki G. *Cell Rep* 2019;28(11):2923-2938.e8
- [Pediatric Fulminant Cerebellitis Is Still a Fatal Disease that We Know Little About! — PMID:33454719](https://pmc.ncbi.nlm.nih.gov/articles/PMC7816662/) · *Am J Case Rep* 2021;22:e928370

**Primary literature — extracted via publisher/PMC fetch (re-verify before quoting)**

- [Acute Cerebellar Inflammation and Related Ataxia: Mechanisms and Pathophysiology — PMID:35326323](https://pmc.ncbi.nlm.nih.gov/articles/PMC8946185/) · Parvez MSA, Ohtsuki G. *Brain Sci* 2022;12(3):367
- [TNF-α increases the intrinsic excitability of cerebellar Purkinje cells through elevating glutamate release in Bergmann Glia — PMID:30072733](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6072779/) · *Sci Rep* 2018
- [Spectrum of centrosome autoantibodies in childhood varicella and post-varicella acute cerebellar ataxia — PMID:14503922](https://pubmed.ncbi.nlm.nih.gov/14503922/) · Fritzler MJ, Zhang M, Stinton LM, Rattner JB. *BMC Pediatr* 2003;3:11
- [Acute cerebellar ataxia and consecutive cerebellitis produced by glutamate receptor delta2 autoantibody — PMID:17049194](https://pubmed.ncbi.nlm.nih.gov/17049194/) · Shiihara T, et al. *Brain Dev* 2007;29(4):254-6
- [A case of acute cerebellitis accompanied by autoantibodies against glutamate receptor delta2 — PMID:17008044](https://pubmed.ncbi.nlm.nih.gov/17008044/) · Shimokaze T, et al. *Brain Dev* 2007;29(4):224-6
- [Neuroimaging of acute cerebellitis — PMID:11826604](https://pubmed.ncbi.nlm.nih.gov/11826604/) · Montenegro MA, et al. *J Neuroimaging* 2002;12(1):72-4
- [Acute ataxia in children: etiological spectrum and clinical characteristics — PMID:41321459](https://pmc.ncbi.nlm.nih.gov/articles/PMC12657339/) · Zhao Q, et al. *Front Pediatr* 2025
- [Acute cerebellitis in adults: a case report and review of the literature — PMID:29166939](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5700531/) · Van Samkar A, et al. *BMC Res Notes* 2017
- [Cerebellitis Associated with Influenza A(H1N1)pdm09, United States, 2013 — PMID:25153508](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4178382/) · *Emerg Infect Dis* 2014;20(9):1578-1580
- [Acute post-infectious cerebellar ataxia due to co-infection of human herpesvirus-6 and adenovirus mimicking myositis — PMID:25425177](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4255938/) · *Ital J Pediatr* 2014
- [Immune-mediated Cerebellar Ataxias: Practical Guidelines and Therapeutic Challenges — PMID:30221603](https://pmc.ncbi.nlm.nih.gov/articles/PMC6341499/) · Mitoma H, Manto M, Hampe CS. *Curr Neuropharmacol* 2019;17(1):33-58
- [Immune-Mediated Cerebellar Ataxias: Clinical Diagnosis and Treatment Based on Immunological and Physiological Mechanisms — PMID:33457189](https://www.e-jmd.org/journal/view.php?doi=10.14802%2Fjmd.20040) · *J Mov Disord* 2021

**Leads seen only in search summaries — do not cite from these**

- [Consensus Paper. Cerebellar Reserve: From Cerebellar Physiology to Cerebellar Disorders — PMID:31879843](https://pmc.ncbi.nlm.nih.gov/articles/PMC6978437/)
- [Etiologies of Acute Ataxia in Children: A Systematic Review of 1167 Subjects](https://journals.sagepub.com/doi/10.1177/08830738251396192) · *J Child Neurol* 2025
- [Differentiating Acute Infectious and Post-Infectious Cerebellitis: A Tunisian Pediatric Case Series](https://www.msard-journal.com/article/S2211-0348(22)00846-X/abstract) · *Mult Scler Relat Disord* 2023
- [Isolated Pancerebellar Syndrome With anti-GQ1b IgG Positivity — PMID:40787651](https://pmc.ncbi.nlm.nih.gov/articles/PMC12328339/)
- [Postinfectious Cerebellar Syndrome With Paraneoplastic Antibodies: An Association or Coincidence? — PMID:33029469](https://pubmed.ncbi.nlm.nih.gov/33029469/)
- [Acute fulminant cerebellitis in children: a case series and literature review](https://pmc.ncbi.nlm.nih.gov/articles/PMC13544665/)
- [The Cerebellar Cognitive Affective/Schmahmann Syndrome: a Task Force Paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6978293/)
- [Acute cerebellar ataxia in children (MedLink Neurology)](https://www.medlink.com/articles/acute-cerebellar-ataxia-in-children) — HTTP 403, not opened; several review-level figures above trace to its search summary
- [Acute Ataxia in Children (Pediatrics in Review 2019)](https://publications.aap.org/pediatricsinreview/article/40/7/332/35300/Acute-Ataxia-in-Children) — HTTP 403, not opened

**Ontology and terminology resources queried**

- [EBI OLS4 API](https://www.ebi.ac.uk/ols4/) — MONDO:0850107 metadata and ancestors; UBERON cerebellar layers; NCIT acyclovir; NCBITaxon HHV-6
- [MedGen: Postinfectious cerebellitis (C5575321 / UID 1843009)](https://www.ncbi.nlm.nih.gov/medgen/1843009) — definition, synonyms, SNOMED/Orphanet/GARD xrefs
- [HGNC REST API](https://rest.genenames.org/) — GRID2, GAD2, HOMER3, GRIA1
- Repository term caches read directly: `cache/hp/`, `cache/uberon/`, `cache/cl/`, `cache/go/`, `cache/ncit/`, `cache/chebi/`, `cache/hgnc/`, `cache/mgi/`, `cache/ncbitaxon/`, `cache/icd10cm/`, `cache/icd11f/`
- [Orphanet ORPHA:624244](https://orpha.net/consor/cgi-bin/OC_Exp.php?Expert=624244&lng=EN) — **not reachable** (DNS failure); definition obtained via MedGen instead. ICD codes remain outstanding.

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 47 |
| Resolved | 44 |
| Unresolved (possible confabulation) | 3 |
| Unverifiable | 0 |
| References weighed for topical relevance | 44 |
| On topic | 35 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `PMID:33457189` (1 mention) - Identifier did not resolve to a record
- `PMC:PMC12420292` (1 mention) - Identifier did not resolve to a record
- `PMC:PMC6978293` (2 mentions) - Identifier did not resolve to a record

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 142 |
| Resolved | 139 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 19 |
| Terms named correctly | 15 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 4 |

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `RO:0004003` (2 mentions) - RO does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0070997` (obsolete neuron death) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `NCBITaxon:2697049` (1 mention) - the report calls it "SARS-CoV-2"; NCBITaxon calls it **Severe acute respiratory syndrome coronavirus 2**, and lists "SARS-CoV-2" among its other names
- `NCBITaxon:90371` (1 mention) - the report calls it "Salmonella* Typhimurium"; NCBITaxon calls it **Salmonella enterica subsp. enterica serovar Typhimurium**, and lists "Salmonella typhimurium" among its other names
- `NCBITaxon:1314` (1 mention) - the report calls it "Streptococcus pyogenes* / haemolytic streptococcus"; NCBITaxon calls it **Streptococcus pyogenes**, and lists "Streptococcus hemolyticus" among its other names
- `NCBITaxon:138` (1 mention) - the report calls it "Borrelia* spp"; NCBITaxon calls it **Borrelia**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.