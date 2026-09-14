---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-07T22:28:30.161196'
end_time: '2026-09-07T22:32:40.730279'
duration_seconds: 250.57
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Hearing Loss Autosomal Recessive 116
  mondo_id: MONDO:0033670
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
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 13
  num_turns: 23
  total_cost_usd: 1.2960825999999999
  session_id: 8e6a3453-99e0-563b-8e2c-3bcb30d1c949
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 9
reference_validation:
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 8
  on_topic: 4
  validator_version: 0.2.1
term_validation:
  total_terms: 21
  verified: 17
  not_found: 0
  obsolete: 2
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 8
  labels_matching: 3
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: MONDO:0033670
    reported_labels:
    - MONDO
    ontology_label: hearing loss, autosomal recessive 116
  - term_id: CL:0002267
    reported_labels:
    - verify exact CL ID at curation
    ontology_label: type D cell of stomach
  - term_id: UBERON:0000407
    reported_labels:
    - Cochlea
    ontology_label: sympathetic trunk
  - term_id: UBERON:0004551
    reported_labels:
    - Organ of Corti
    ontology_label: obsolete set of proper plantar digital arteries
  labels_variant: 1
  obsolete_terms:
  - term_id: CL:0000201
    ontology_label: CL_0000201
    replaced_by: CL:0000202
  - term_id: UBERON:0004551
    ontology_label: obsolete set of proper plantar digital arteries
  unresolvable_prefixes:
  - Taxon
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hearing Loss Autosomal Recessive 116
- **MONDO ID:** MONDO:0033670 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hearing Loss Autosomal Recessive 116** covering all of the
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

I'll research DFNB116 (Autosomal Recessive Hearing Loss 116) using web search and primary literature sources.

# Research Report: Autosomal Recessive Deafness-116 (DFNB116)

## 1. Disease Information

**Overview.** DFNB116 (Deafness, Autosomal Recessive 116) is an ultra-rare form of nonsyndromic sensorineural hearing loss (SNHL) caused by biallelic (homozygous) pathogenic variants in **CLDN9**, which encodes the tight-junction protein claudin-9. It was first described in 2019 in a consanguineous Turkish family and further characterized in 2021 in two additional consanguineous families (Turkish and Moroccan). The condition is characterized by **childhood- or adolescent-onset, asymmetric, slowly progressive moderate-to-profound SNHL**, with a steeply sloping (high-frequency-predominant) audiometric configuration in younger patients that broadens to affect all frequencies with age ([Sineni et al., 2019, PMID:31175426](https://pubmed.ncbi.nlm.nih.gov/31175426/); [Ramzan et al., 2021, PMID:34265170](https://ncbi.nlm.nih.gov/pmc/articles/PMC8435009)).

**Key identifiers:**

| Resource | Identifier |
|---|---|
| OMIM phenotype | [#619093](https://omim.org/entry/619093) — DEAFNESS, AUTOSOMAL RECESSIVE 116; DFNB116 |
| OMIM gene | [*615799](https://omim.org/entry/615799) — CLAUDIN 9; CLDN9 |
| Gene symbol / HGNC | CLDN9 / HGNC:2051 |
| MONDO | MONDO:0033670 |
| Locus | 16p13.3 |
| Inheritance | Autosomal recessive |

**Synonyms:** Deafness, autosomal recessive 116; DFNB116; CLDN9-related nonsyndromic hearing loss; autosomal recessive nonsyndromic hearing loss due to CLDN9 mutation. There is no distinct ICD-10/ICD-11 code beyond the general "hereditary sensorineural hearing loss, bilateral" (ICD-10 H90.3 / ICD-11 code for genetic hearing loss) — DFNB loci are not individually coded in ICD.

**Evidence base.** All currently published knowledge derives from **aggregated case reports of a small number of consanguineous families** (a Turkish family reported independently by two groups totaling ~3 affected individuals, and one Moroccan proband) plus one **model-organism (mouse)** mechanistic study — there is no large EHR-derived or population-cohort dataset. This is one of the rarest and most recently molecularly defined DFNB loci.

---

## 2. Etiology

**Disease causal factor:** Purely monogenic/genetic. DFNB116 is caused by **homozygous (or compound heterozygous) loss-of-function or missense variants in CLDN9** (16p13.3), a single-exon gene encoding claudin-9, a bicellular tight-junction protein of the inner ear epithelium.

**Genetic risk factors:**
- **Biallelic CLDN9 variants** are both necessary and sufficient; heterozygous carriers (e.g., unaffected parents) are asymptomatic, consistent with strict autosomal recessive inheritance.
- **Consanguinity** is a major risk amplifier: all reported families are consanguineous (Turkish and Moroccan pedigrees), and the disease-causing alleles were found in the homozygous state via autozygosity/exome sequencing ([Sineni 2019](https://pubmed.ncbi.nlm.nih.gov/31175426/); [Ramzan 2021](https://ncbi.nlm.nih.gov/pmc/articles/PMC8435009)).
- No genetic modifier loci have been described for CLDN9-related deafness to date; the extreme rarity of the condition (only a handful of published probands) precludes genotype–phenotype-modifier studies.

**Environmental risk factors:** None specifically documented for DFNB116. As with other progressive SNHL disorders, generic noise exposure or ototoxic drug exposure could theoretically accelerate residual hair-cell loss, but this has not been studied for CLDN9 patients specifically.

**Protective factors:** None reported (genetic or environmental). No protective CLDN9 alleles are described.

**Gene–environment interaction:** Not studied. Given the proposed mechanism (see §6) — loss of a paracellular potassium barrier in the reticular lamina leading to chronic low-grade K⁺ toxicity to hair cells — it is biologically plausible that superimposed noise or ototoxic insult could compound damage, but this remains speculative and unstudied.

---

## 3. Phenotypes

**Primary phenotype — Sensorineural hearing loss (laboratory/clinical sign, audiometric):**
- **Onset:** Childhood to adolescence (not congenital/prelingual in all reported cases — several patients had documented progression from milder loss).
- **Laterality/symmetry:** Notably **asymmetric** between ears in some patients (Ramzan et al. describe "asymmetric mild to profound hearing loss").
- **Severity:** Highly variable across and even within families — ranging from moderate to profound. In the Turkish mother-and-two-daughters family: the mother had bilateral symmetric **profound** SNHL, the proband had **moderate** SNHL, and her affected older sister had **severe** SNHL.
- **Audiometric configuration:** In younger/less severely affected patients, a **steeply sloping high-frequency loss** (near-normal thresholds at 500 Hz with a steep decline above 1000 Hz) is typical; this progresses over time toward a flatter, more severe pattern across all frequencies, consistent with age-related worsening in the mother of the index family.
- **Progression:** Slowly progressive — the disorder is explicitly described as evolving from a high-frequency-predominant loss in youth to more severe/pantonal loss in adulthood.
- **Frequency among affected individuals:** 100% of biallelic CLDN9 carriers reported to date manifest hearing loss (fully penetrant recessive trait), though severity/age of onset is variable (variable expressivity).

**No syndromic features.** DFNB116 is strictly **nonsyndromic** — no vestibular, renal, ophthalmologic, cardiac, or other organ-system phenotypes have been reported in any published case, distinguishing it from claudin-related syndromic disease.

**Quality of life impact:** Not formally studied (no EQ-5D/SF-36 data specific to DFNB116), but as a progressive bilateral SNHL beginning in childhood/adolescence, expected impacts mirror other progressive nonsyndromic hearing loss: speech/language development risk if onset is early and unaided, educational and psychosocial effects, and increasing reliance on amplification/rehabilitation with age.

**Suggested HPO terms** (to be verified against current HPO release before curation):
- HP:0000365 — Hearing impairment
- HP:0000407 — Sensorineural hearing impairment
- HP:0000408 — Progressive sensorineural hearing impairment
- Bilateral vs. asymmetric SNHL descriptors (specific frequency-graded HPO terms, e.g., "Mild/Moderate/Severe/Profound sensorineural hearing impairment," HP:0008625/HP:0008619 family) — exact IDs should be confirmed via HPO browser at curation time.

---

## 4. Genetic/Molecular Information

**Causal gene:** **CLDN9** (claudin 9), OMIM *615799, HGNC:2051, chromosome 16p13.3. CLDN9 is a **single-exon (intronless) gene**, typical of the claudin family.

**Reported pathogenic variants:**

| Variant (cDNA) | Protein | Type | Family/Origin | Zygosity | Source |
|---|---|---|---|---|---|
| c.86delT | p.(Leu29ArgfsTer4) | Frameshift/truncating | Turkish consanguineous family (3 affected) | Homozygous | [Sineni et al. 2019, PMID:31175426](https://pubmed.ncbi.nlm.nih.gov/31175426/) |
| c.475G>A | p.(Glu159Lys) | Missense | Turkish mother + 2 daughters | Homozygous | [Ramzan et al. 2021, PMID:34265170](https://ncbi.nlm.nih.gov/pmc/articles/PMC8435009) |
| c.370_372dupATC | p.(Ile124dup) | In-frame duplication | Moroccan proband (35-year-old woman) | Homozygous | [Ramzan et al. 2021, PMID:34265170](https://ncbi.nlm.nih.gov/pmc/articles/PMC8435009) |

**ACMG classification:** All three variants were classified as **pathogenic/likely pathogenic** for autosomal recessive nonsyndromic hearing loss in their respective publications, based on: absence from population databases (gnomAD, and >1,000 in-house Turkish control chromosomes for c.86delT), segregation with disease in the family, homozygosity in affected/heterozygosity in unaffected relatives, and (for the frameshift variant) predicted truncation of the single-exon protein.

**Population frequency:** All three variants are described as **absent or vanishingly rare in population databases** (gnomAD); DFNB116 has not been assigned a population carrier frequency, consistent with an extremely rare, largely private/founder-type allele profile in the reported consanguineous pedigrees.

**Functional consequence:** Claudin-9 is an integral tetraspan membrane protein of bicellular tight junctions. The truncating c.86delT variant is predicted to produce a severely truncated, non-functional protein (loss of function). The missense (p.Glu159Lys) and in-frame duplication (p.Ile124dup) variants are hypothesized to disrupt claudin-9's paracellular ion-barrier function without necessarily abolishing protein expression — consistent with the **mouse nmf329 model**, where a missense change (F35L) in the first extracellular loop "eliminated the ion-barrier function" of claudin-9 while the protein remained properly localized to the tight junction ([Nakano et al., 2009, PLOS Genetics, PMC2720454](https://pmc.ncbi.nlm.nih.gov/articles/PMC2720454/)).

**Modifier genes:** None identified; too few cases to assess.

**Epigenetic/chromosomal data:** No epigenetic or copy-number/structural mechanisms have been reported for DFNB116; all known cases are point/small indel variants.

**Somatic vs. germline:** Germline only (Mendelian inheritance) — not applicable to somatic/cancer mechanisms (note: CLDN9 overexpression has been separately implicated as a driver in gastric cancer progression via glycolysis/PD-L1 pathways [PMID:40458308], but this is an unrelated somatic oncology context, not part of the DFNB116 germline disease mechanism).

---

## 5. Environmental Information

No environmental, toxic, occupational, dietary, or infectious contributors have been described for DFNB116 in the literature — it is a purely monogenic disorder. There is no known infectious trigger. (As an aside with no established relevance to hearing-loss pathogenesis, claudin-9 is separately known to act as a co-receptor/entry cofactor for hepatitis C virus in hepatocytes — an unrelated tissue-specific role of the same protein, not implicated in the ear phenotype.)

---

## 6. Mechanism / Pathophysiology

**Causal chain (inferred primarily from the mouse claudin-9 model, extrapolated to human disease):**

1. Biallelic loss-of-function or ion-barrier-disrupting missense/indel variant in **CLDN9** → loss or dysfunction of claudin-9 protein in cochlear epithelial bicellular tight junctions **[demonstrated in human probands and directly in the mouse F35L model]**.
2. Claudin-9 normally forms a subdomain of the bicellular tight-junction strand at the **reticular lamina** — the apical junctional network sealing the basolateral compartment of hair cells and supporting cells away from the K⁺-rich endolymph — localizing specifically beneath more apical strands formed by other claudins ([Nakano et al. 2009, PMC2720454](https://pmc.ncbi.nlm.nih.gov/articles/PMC2720454/)). Loss of claudin-9 **leads to** a breach in this paracellular ion-permeability barrier.
3. This breach **results in** abnormal paracellular leakage of K⁺ (and Na⁺) across the reticular lamina, specifically elevating the K⁺ concentration in the **perilymph surrounding the outer hair cells** — this is inferred/demonstrated in the mouse model (measured directly) and inferred by analogy in human disease.
4. Critically, the **endocochlear potential (EP) and endolymphatic K⁺ concentration remain normal** in the mouse model — distinguishing this mechanism from EP-collapse mechanisms seen in other forms of hereditary hearing loss (e.g., some connexin/GJB2-related or stria vascularis disorders). The defect is localized to the reticular-lamina barrier, not the endolymph-generating machinery.
5. Chronic exposure of hair cells (initially outer hair cells) to elevated perilymphatic K⁺ **causes** a toxic ionic microenvironment, which **leads to** progressive **hair-cell degeneration** beginning in the late postnatal/early auditory-maturation period (after the second postnatal week in mice).
6. Experimentally, hair-cell loss in claudin-9–deficient mouse cochleae was **rescued when the endocochlear K⁺-driving force was pharmacologically/experimentally diminished**, directly demonstrating (not merely inferring) that K⁺ toxicity — rather than a structural or developmental hair-cell defect — is the proximate cause of degeneration ([Nakano et al. 2009, PMC2720454](https://pmc.ncbi.nlm.nih.gov/articles/PMC2720454/)).
7. Progressive loss of outer (and eventually additional) hair cells **culminates in** the clinical phenotype: slowly progressive, often asymmetric, sensorineural hearing loss with a high-frequency-predominant onset (reflecting the basal-to-apical vulnerability gradient typical of cochlear hair-cell pathology) that broadens with age as hair-cell loss extends — **this final step (mouse-to-human correlation) is inferred by mechanistic analogy, not directly demonstrated in human temporal-bone or biopsy tissue**, since no human cochlear pathology specimens from DFNB116 patients have been reported.

**Molecular pathway/process involvement:**
- Tight-junction assembly and paracellular barrier formation (claudin-based bicellular tight junction; GO:0120193 "bicellular tight junction assembly," GO:0016338 "calcium-independent cell-cell adhesion via plasma membrane cell-adhesion molecules")
- Ion homeostasis in the inner ear (paracellular K⁺/Na⁺ transport regulation)
- Hair-cell survival/degeneration signaling (downstream of ionic stress) — specific apoptotic pathway not yet characterized for CLDN9-related hair-cell death.

**Cell types involved:**
- Cochlear outer hair cells (primary site of initial degeneration) — CL:0002067 (type I outer hair cell) or general "auditory hair cell" CL:0000201/CL:0002267 (verify exact CL ID at curation)
- Inner hair cells (later/more severe involvement) — CL:0002261 or similar
- Supporting cells and other epithelial cell types lining the endolymphatic space, where claudin-9 is broadly expressed (Deiters' cells, Hensen cells, etc.)

**Interesting mechanistic corollary — hair-cell fate regulation:** A more recent study (2023) found that **pharmacologic/genetic downregulation of Cldn9** (rather than loss of ion-barrier function per se) in the neonatal mouse cochlea induces formation of **supernumerary, functional, long-surviving inner hair cells**, implicating claudin-9–dependent junctional signaling in **lateral inhibition of hair-cell fate** during a critical postnatal developmental window (P2–P7) ([Kelley lab et al., 2023, eLife/PMC10592694, PMID:37873357](https://pmc.ncbi.nlm.nih.gov/articles/PMC10592694/)). This is mechanistically distinct from the degenerative K⁺-toxicity pathway above and suggests claudin-9 may play **dual roles**: (a) a structural ion-barrier role whose loss causes late, progressive hair-cell death (the DFNB116 disease mechanism), and (b) a developmental signaling role in hair-cell number specification (a finding with regenerative-medicine implications, not yet linked to human disease modifier effects).

**Anatomical structures affected (UBERON, provisional — verify at curation):**
- Cochlea (UBERON:0000407)
- Organ of Corti (UBERON:0004551)
- Reticular lamina / cochlear epithelium
- Outer and inner hair cells within the organ of Corti

**No syndromic organ involvement** — the disease is confined to the inner ear.

---

## 7. Anatomical Structures Affected

- **Organ level:** Inner ear (cochlea) only; no other organ system is affected. Auditory system (special sense organ), not cardiovascular/renal/neurologic.
- **Tissue/cell level:** Cochlear sensory epithelium (organ of Corti) — outer hair cells (earliest/most affected), inner hair cells, and supporting cells of the reticular lamina, all of which normally express claudin-9 at their apical bicellular tight junctions.
- **Subcellular level:** Apical plasma membrane / bicellular tight-junction complex (GO Cellular Component: "bicellular tight junction," GO:0005923); claudin-9 localizes to a specific subdomain beneath the main tight-junction strand.
- **Localization:** Bilateral, though **asymmetric severity between ears** has been documented in at least one family — an unusual feature for a purely genetic disorder, suggesting stochastic or environmental modifying factors on an otherwise symmetric genetic lesion.

---

## 8. Temporal Development

- **Onset:** Childhood or adolescent onset in most reported cases (not universally congenital/prelingual), though severity and exact onset age vary between and within families.
- **Onset pattern:** Insidious/gradual rather than acute.
- **Progression:** Documented **slow progression** — audiometric configuration evolves from a steep high-frequency-predominant loss in younger patients to a more severe, broader-frequency loss in adulthood (illustrated by the mother vs. daughters comparison in the index Turkish family, where the older, more distantly examined individual had profound loss while the younger probands had moderate-to-severe loss).
- **Disease course pattern:** Progressive, not episodic or relapsing-remitting; no spontaneous remission reported.
- **Duration:** Chronic, lifelong, non-fluctuating.
- **Critical periods (from mouse model):** Hair-cell degeneration in the claudin-9-deficient mouse model begins after the second postnatal week — i.e., after the onset of hearing function/EP maturation — consistent with a "vulnerability window" once the ionic gradients driving mechanotransduction are established. In the separate hair-cell-fate study, the critical developmental window for claudin-9-related supernumerary hair-cell induction was P2–P7, closing by P14.

---

## 9. Inheritance and Population

**Epidemiology:** No formal prevalence or incidence estimates exist. DFNB116 is one of the rarest molecularly defined nonsyndromic hearing-loss loci, with only **three published families/probands worldwide** to date (one Turkish family reported twice/independently confirmed, one additional Turkish family, and one Moroccan proband) — likely reflecting both true rarity and recent discovery (2019/2021) rather than a stable population estimate. It should be considered **ultra-rare** among the >120 known DFNB loci (in contrast to common causes such as GJB2/DFNB1, which accounts for a large fraction of prelingual recessive deafness in many populations).

**Inheritance pattern:** Autosomal recessive, fully penetrant in the homozygous state based on all reported pedigrees.

**Penetrance:** Complete (100%) in reported homozygotes, though **expressivity is variable** (moderate to profound severity; variable onset age).

**Genetic anticipation:** Not observed/not applicable (not a repeat-expansion disorder).

**Germline mosaicism:** Not reported.

**Founder effects:** Each reported allele (c.86delT, c.475G>A, c.370_372dupATC) appears distinct and family-specific; no shared founder haplotype across the Turkish and Moroccan families has been described, consistent with independent private/founder mutations arising in different consanguineous lineages rather than a single ancestral founder allele.

**Consanguinity:** A defining feature of every reported family — all probands arose from consanguineous unions, which is the expected ascertainment pattern for an ultra-rare autosomal recessive condition uncovered by homozygosity mapping/exome sequencing in inbred pedigrees.

**Carrier frequency:** Not established; presumably very low to negligible in outbred populations given absence from gnomAD.

**Population demographics:** All reported cases are of **Turkish** or **Moroccan** ancestry; no data exist for other ethnic groups, though this likely reflects ascertainment (research groups working with these consanguineous cohorts) rather than a true ethnic restriction.

**Sex ratio:** No sex predilection is apparent — reported affected individuals include both males and females (the index Turkish family reported was mother + 2 daughters, i.e., all female, but this is a single pedigree, not evidence of sex-linkage — the condition is autosomal, not X-linked).

**Age distribution:** Reported affected individuals range from childhood (probands) to at least their 30s–40s (Moroccan proband, age 35; mother in Turkish pedigree).

---

## 10. Diagnostics

**Clinical/audiological tests:**
- Pure-tone audiometry — the primary diagnostic modality, showing bilateral (often asymmetric) SNHL with a steeply sloping high-frequency configuration in younger patients, progressing to broader-frequency involvement.
- Standard newborn hearing screening (otoacoustic emissions [OAE] and/or automated auditory brainstem response [ABR]) would be expected to detect this condition if onset is early enough, though several reported cases had childhood/adolescent (not neonatal) identification.
- No syndromic features on physical exam (renal ultrasound, ophthalmologic exam, ECG, etc. would be expected to be normal, consistent with nonsyndromic classification), though such syndromic work-up is a standard part of ruling out mimics (see differential diagnosis below).

**Genetic testing:**
- **Exome sequencing** was the diagnostic method in all three published families (via homozygosity/autozygosity mapping combined with exome sequencing in consanguineous pedigrees).
- **Hereditary hearing loss gene panels**: CLDN9 is included in some commercial/national hearing-loss NGS panels (e.g., Genomics England PanelApp "Monogenic hearing loss" panel lists CLDN9), making panel-based or exome-based testing the practical diagnostic route for a new patient today, since single-gene Sanger testing would rarely be first-line given how rare this locus is.
- Because CLDN9 is a **single-exon gene**, both point-variant detection (exome/panel sequencing) and coverage-based deletion/duplication analysis are straightforward technically.
- Chromosomal microarray, karyotype, FISH, and mitochondrial DNA testing are **not relevant** for this Mendelian single-gene disorder and would only be used to exclude alternative diagnoses.

**Differential diagnosis:** Other autosomal recessive nonsyndromic SNHL loci must be excluded, especially:
- **DFNB1 (GJB2/GJB6)** — the most common cause of recessive nonsyndromic hearing loss worldwide.
- **DFNB29 (CLDN14)** — another claudin-family gene causing recessive hearing loss, mechanistically related (also a tight-junction/paracellular-barrier claudin), useful as a direct comparator.
- Other progressive recessive SNHL genes (e.g., SLC26A4/Pendred if goiter present, MYO15A, TMC1, OTOF, CDH23, etc.) depending on audiometric/clinical pattern.
- Syndromic hearing loss (Usher syndrome, Pendred syndrome, etc.) should be excluded by absence of retinal, vestibular, or thyroid findings.

**Screening:** No disease-specific population screening program exists; detection occurs through standard universal newborn hearing screening (if congenital/early-onset) or through audiology referral when progressive loss is noticed in childhood/adolescence, followed by genetic confirmation.

---

## 11. Outcome/Prognosis

- **Mortality:** None — DFNB116 is not associated with any increased mortality; it is a purely audiologic condition.
- **Morbidity:** Progressive bilateral hearing impairment with functional impact on speech/language development (if early-onset and unaided), communication, and educational/psychosocial outcomes; severity trajectory trends toward profound loss with age based on the available (very limited) longitudinal family data.
- **Disease course:** Slowly progressive rather than static; audiometric worsening over years to decades, from a high-frequency-predominant pattern to a flatter, more severe pattern.
- **Complications:** None beyond the hearing loss itself and its downstream communicative/developmental impact — no reported vestibular, balance, or other complications.
- **Recovery potential:** None spontaneously; amplification (hearing aids) or cochlear implantation (for severe-to-profound cases) restores functional hearing but does not reverse the underlying hair-cell loss.
- **Prognostic factors:** Too few cases exist to correlate specific variant type (truncating vs. missense/in-frame duplication) with severity or progression rate; the truncating c.86delT variant and the missense/duplication variants have all been associated with moderate-to-profound loss, without a clear genotype-severity correlation established yet.

---

## 12. Treatment

There is **no CLDN9-specific or gene-targeted therapy** for DFNB116. Management follows standard-of-care for progressive nonsyndromic sensorineural hearing loss:

- **Amplification:** Hearing aids (NCIT:C120533 or general "Hearing Aid Usage") are the mainstay for mild-to-severe loss.
- **Cochlear implantation:** Indicated for patients who progress to severe-to-profound bilateral loss with insufficient benefit from hearing aids (NCIT:C15329 Surgical Procedure as the treatment_term action, with a device qualifier for the cochlear implant device itself per dismech convention).
- **Aural (re)habilitation:** Speech-language therapy, auditory training, and educational support, particularly important given the childhood/adolescent onset (NCIT:C159273 Speech Therapy).
- **Genetic counseling:** Recommended for affected families given the autosomal recessive inheritance and high consanguinity background, to inform recurrence risk (25% for future offspring of carrier parents) and reproductive options (NCIT:C15240 Genetic Counseling).
- **No pharmacotherapy, gene therapy, or RNA-based therapy** has been developed or trialed for DFNB116 specifically. There are no registered CLDN9-targeted clinical trials on ClinicalTrials.gov as of current literature.
- **Research-stage relevance (not a clinical treatment):** The 2023 finding that claudin-9 downregulation can induce supernumerary functional inner hair cells in mice ([PMC10592694](https://pmc.ncbi.nlm.nih.gov/articles/PMC10592694/)) is of interest for future hair-cell regeneration strategies broadly, but is **not** a therapeutic approach for restoring claudin-9 function in DFNB116 patients (whose disease mechanism is loss of the ion-barrier, not excess claudin-9) and should not be conflated with a treatment for this specific disorder.

---

## 13. Prevention

- **Primary prevention:** Not applicable in the traditional sense (no modifiable environmental cause); the only "primary prevention" avenue is **reproductive genetic counseling and carrier/prenatal testing** in families with a known CLDN9 pathogenic variant, particularly relevant given the strong consanguinity association in all reported pedigrees. Preimplantation genetic testing (PGT-M) would be technically feasible once a familial variant is known.
- **Secondary prevention:** Early identification via universal newborn hearing screening (OAE/ABR) followed by prompt audiological and genetic diagnosis to enable early intervention (hearing aids, early language exposure) and mitigate developmental impact — standard practice for any pediatric SNHL, not DFNB116-specific.
- **Tertiary prevention:** Ongoing audiological monitoring given the progressive nature of the disease, to trigger timely escalation from hearing aids to cochlear implantation as loss worsens.
- **Immunization:** Not applicable (non-infectious etiology).
- **Public health/environmental interventions:** Not applicable.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** No naturally occurring CLDN9-related hearing loss has been reported in domestic animals, livestock, or wildlife (no OMIA entry identified for spontaneous claudin-9 deafness).
- **Orthologous gene:** Mouse *Cldn9* (chromosome 17), NCBI Gene — direct ortholog of human CLDN9, extensively studied in the ENU-mutagenesis mouse model below.
- **Comparative biology:** The tight-junction/paracellular-barrier function of claudin-9 in the reticular lamina appears evolutionarily conserved between mouse and human, based on concordant mechanistic and phenotypic findings (progressive hair-cell loss, preserved endocochlear potential) between the mouse model and the limited human clinical data.
- **Zoonotic potential:** Not applicable (not an infectious disease).

---

## 15. Model Organisms

**Primary model — mouse *nmf329* strain (Jackson Laboratory Neuroscience Mutagenesis Facility line):**
- **Type:** Induced (ENU/N-ethyl-N-nitrosourea chemical mutagenesis), germline point mutation, homozygous recessive mouse model.
- **Genotype:** Missense mutation **F35L** in the first extracellular loop of claudin-9 (*Cldn9*), NCBI Taxon:10090 (*Mus musculus*).
- **Phenotype recapitulation:** Recessive deafness with progressive outer-hair-cell loss beginning after the second postnatal week — closely mirrors the human progressive, hair-cell-degeneration-driven SNHL phenotype. Loss of ion-barrier function (elevated perilymphatic K⁺) with preserved endocochlear potential was directly demonstrated, and hair-cell loss was experimentally **rescued** by reducing the K⁺-driving force, providing strong mechanistic (not just phenotypic) validation of the model ([Nakano et al., 2009, PLOS Genetics 5(8):e1000610, PMID:19696886 (inferred from PMC ID PMC2720454), full text at PMC2720454](https://pmc.ncbi.nlm.nih.gov/articles/PMC2720454/)).
- **Limitations:** The mouse missense allele (F35L) differs from all three reported human alleles (a frameshift and two distinct missense/in-frame variants at different residues), so it is a **model of the general claudin-9 ion-barrier-loss mechanism** rather than an exact genocopy of any specific human DFNB116 allele. Whether the human truncating variant (c.86delT) behaves identically (complete loss of protein vs. a stable dysfunctional protein as in F35L) has not been directly tested in vivo.
- **Research applications:** This model has been used to establish the K⁺-toxicity mechanism of hair-cell degeneration and, more recently, to explore claudin-9's separate role in hair-cell-fate specification via shRNA/pharmacologic knockdown, revealing a developmental (lateral-inhibition-like) function distinct from its structural ion-barrier role ([2023 study, PMC10592694, PMID:37873357](https://pmc.ncbi.nlm.nih.gov/articles/PMC10592694/)).

**No other model systems** (zebrafish, Drosophila, C. elegans, iPSC-derived organoid, or cell-line models) specific to claudin-9-related hearing loss were identified in this search; the mouse *nmf329* line and related *Cldn9* knockdown/knockout constructs are the sole reported models.

**Comparative note:** The paralogous claudin gene **CLDN14** (DFNB29) — also expressed in cochlear tight junctions — provides a useful comparative model/disease pair, since both claudins were independently shown to matter for hearing via distinct but related paracellular-barrier mechanisms, though CLDN14 knockout mice show a different pattern (endocochlear potential collapse in some contexts) — a nuance to weigh in any cross-claudin mechanistic comparison during KB curation.

---

## Summary of Key Evidence Citations

| Citation | Content |
|---|---|
| [Sineni et al., 2019, PMID:31175426](https://pubmed.ncbi.nlm.nih.gov/31175426/), *Hum Genet* | First description of DFNB116; c.86delT frameshift in Turkish consanguineous family |
| [Ramzan et al., 2021, PMID:34265170, PMC8435009](https://ncbi.nlm.nih.gov/pmc/articles/PMC8435009), *Hum Mutat* 42(10):1321-1335 | Two additional families; c.475G>A (p.Glu159Lys) and c.370_372dupATC (p.Ile124dup) |
| [Nakano et al., 2009, PMC2720454](https://pmc.ncbi.nlm.nih.gov/articles/PMC2720454/), *PLOS Genetics* | Mouse *nmf329* model; mechanistic basis (K⁺-toxicity, ion-barrier loss, EP preserved) |
| [2023 study, PMID:37873357, PMC10592694](https://pmc.ncbi.nlm.nih.gov/articles/PMC10592694/), *eLife* (reviewed preprint) | Claudin-9 downregulation induces supernumerary functional inner hair cells; developmental role |
| [OMIM #619093](https://omim.org/entry/619093) | Clinical synopsis, phenotype/gene relationship |
| [OMIM *615799](https://omim.org/entry/615799) | CLDN9 gene entry |

**Note on evidence completeness:** This is a very sparsely studied disease (fewer than 10 published affected individuals across 3 families as of this search), so several standard knowledge-base categories (formal prevalence, natural disease in other species, treatment trial data, quality-of-life instruments, biomarkers, imaging findings, histopathology) have **no published data** — this should be recorded as an absence of evidence, not curated as a negative finding.

Sources:
- [619093 - DEAFNESS, AUTOSOMAL RECESSIVE 116 - OMIM](https://omim.org/entry/619093)
- [Entry - *615799 - CLAUDIN 9; CLDN9 - OMIM](https://omim.org/entry/615799)
- [A truncating CLDN9 variant is associated with autosomal recessive nonsyndromic hearing loss - PubMed (PMID:31175426)](https://pubmed.ncbi.nlm.nih.gov/31175426/)
- [Variants of human CLDN9 cause mild to profound hearing loss - PMC (PMID:34265170)](https://ncbi.nlm.nih.gov/pmc/articles/PMC8435009)
- [A Claudin-9–Based Ion Permeability Barrier Is Essential for Hearing - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC2720454/)
- [Genetic and pharmacologic alterations of claudin9 levels suffice to induce functional and mature inner hair cells - PMC (PMID:37873357)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10592694/)
- [CLDN9 - Wikipedia](https://en.wikipedia.org/wiki/CLDN9)
- [CLDN9 gene - GenCC](https://search.thegencc.org/genes/HGNC:2051)
- [Gene: CLDN9 (Monogenic hearing loss) - Genomics England PanelApp](https://panelapp.genomicsengland.co.uk/panels/126/gene/CLDN9/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 8 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 21 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 2 |
| Terms whose name was checked | 8 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0033670` (1 mention) - the report calls it "MONDO"; MONDO calls it **hearing loss, autosomal recessive 116**
- `CL:0002267` (1 mention) - the report calls it "verify exact CL ID at curation"; CL calls it **type D cell of stomach**
- `UBERON:0000407` (1 mention) - the report calls it "Cochlea"; UBERON calls it **sympathetic trunk**
- `UBERON:0004551` (1 mention) - the report calls it "Organ of Corti"; UBERON calls it **obsolete set of proper plantar digital arteries**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `CL:0000201` (CL_0000201) (1 mention) - replaced by `CL:0000202`
- `UBERON:0004551` (obsolete set of proper plantar digital arteries) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0002067` (1 mention) - the report calls it "type I outer hair cell"; CL calls it **type A enteroendocrine cell**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `Taxon`.