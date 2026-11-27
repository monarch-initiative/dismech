---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-26T03:52:28.383790'
end_time: '2026-11-26T03:54:39.929654'
duration_seconds: 131.55
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Tuberculous Salpingitis
  mondo_id: MONDO:0000271
  category: Infectious Disease
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
  web_search_requests: 12
  num_turns: 14
  total_cost_usd: 0.644202
  session_id: 0591df07-95c3-40c4-97a1-5e098efb09aa
  stop_reason: end_turn
  tool_calls: 13
  retrieval_calls: 13
  assistant_text_blocks: 1
citation_count: 36
reference_validation:
  total_references: 20
  verified: 20
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 0
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMC:PMC3901176
  - PMC:PMC9699775
  relevance_assessed: 20
  on_topic: 9
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 24
  verified: 24
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 12
  labels_matching: 4
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: MONDO:0000271
    reported_labels:
    - MONDO
    ontology_label: tuberculous salpingitis
  - term_id: DOID:0050166
    reported_labels:
    - Disease Ontology
    ontology_label: tuberculous salpingitis
  - term_id: HP:0008222
    reported_labels:
    - Clinical sign
    ontology_label: Female infertility
  labels_variant: 5
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Tuberculous Salpingitis
- **MONDO ID:** MONDO:0000271 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** not recorded
- **Category:** Infectious Disease

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Tuberculous Salpingitis** covering all of the
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

I have the sources I need and am writing the report now.

# Tuberculous Salpingitis (MONDO:0000271): Disease Characteristics Report

**How I read the request.** Tuberculous salpingitis has no causal human gene; its cause is infectious. I researched it as tuberculous infection of the fallopian tubes, caused by *Mycobacterium tuberculosis* complex. Clinically it almost never occurs apart from female genital tuberculosis (FGTB), so most of the evidence below is FGTB literature in which the tubes are the main site.

**Causal gene: none.** It is not a Mendelian disease, and no OMIM entry or causal human gene was found. The causal agent is *M. tuberculosis* (NCBI Taxon 1773), and occasionally *M. bovis*.

**Coverage.** This was a single, limited search session. Many template sections (omics, epigenetics, variants, pharmacogenomics) had nothing specific to this disease, and I say so where that applies. PMIDs are marked **verified** only when the search results showed them. Abstract quotes are short excerpts from the search snippets and should be checked against the source before going into the knowledge base.

---

## 1. Disease Information

**Overview**
- MONDO:0000271 defines tuberculous salpingitis as a urogenital tuberculosis with an inflammatory response in the fallopian tube. It cross-references DOID:0050166 ([SAIL concept library](https://conceptlibrary.saildatabank.com/api/v1/ontology/node/MONDO:0000271/); [DrugMap](https://drugmap.idrblab.net/data/disease/details/DISFW7FV)).
- It is the most common form of FGTB. Tubal involvement is reported in 92–100% of FGTB cases ([PMC3901176](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3901176/); [PMC9699775](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9699775/)).

**Identifiers**

| System | ID | Source |
|---|---|---|
| MONDO | MONDO:0000271 | SAIL concept library |
| Disease Ontology | DOID:0050166 | [MGI/DO browser](https://informatics.jax.org/disease/DOID:0050166) |
| ICD-10-CM | A18.17 (tuberculous female pelvic inflammatory disease) | [icdlist](https://icdlist.com/icd-10/diseases-injuries/term/salpingitis-catarrhal-fallopian-tube-nodular-pseudofollicular-purulent-septic); [AutoICD](https://autoicdapi.com/reference/icd-10/A18.17) |
| ICD-10 (WHO) | A18.1† (tuberculosis of genitourinary system), with N74.1* | [gesund.bund.de](https://gesund.bund.de/en/icd-code-search/a18-1); [NHS ICD-10 5th ed.](https://classbrowser.nhs.uk/ICD-10-5TH-Edition/vol1/block-n70-n77.htm) |
| MalaCards | tuberculous_salpingitis | [MalaCards](https://malacards.org/card/tuberculous_salpingitis) |
| OMIM / Orphanet | Not found | — |
| ICD-11 / MeSH | Not retrieved | — |

**Synonyms:** tubal tuberculosis; tuberculous endosalpingitis; genital tuberculosis of the fallopian tube; tuberculous female pelvic inflammatory disease (the ICD-10-CM grouping).

**Data provenance:** The evidence is disease-level: reviews, meta-analyses and case series, mostly from India and Iran. It does not come from individual-patient EHR data.

## 2. Etiology

**Causal factor**
- The cause is infection with *M. tuberculosis* complex.
- Spread to the tube is usually secondary, through the blood from a focus elsewhere. One review states that "tuberculous involvement of the fallopian tube occurs by the hematogenous route from a TB focus elsewhere, usually pulmonary or osseous" ([PMC3901176](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3901176/)).
- Lymphatic spread and direct extension from abdominal or peritoneal TB also occur ([Sharma et al., Indian J Med Res 2018, PMID 30964083, verified](https://pubmed.ncbi.nlm.nih.gov/30964083/)).

**Risk factors**
- Living in a high-TB-burden setting. Reported prevalence is higher in low-income countries ([Ahmed et al., SQUMJ 2022, PMC9423760](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9423760/)).
- Reproductive age.
- Previous pulmonary or extrapulmonary TB.
- Immunosuppression (e.g., HIV) is a general extrapulmonary TB risk factor; I found no data on it specific to salpingitis.

**Genetic risk factors:** None specific to this disease were found. General TB host-susceptibility loci exist, but none were retrieved or validated for genital or tubal TB.

**Protective factors:** No disease-specific data. Plausible general factors are TB control, early treatment of primary TB, and BCG; none were evaluated for this outcome in the sources retrieved.

**Gene–environment interactions:** No data.

## 3. Phenotypes

Frequencies come mainly from FGTB cohorts of infertile women, which inflates the share presenting with infertility.

| Phenotype | Type | Suggested HPO | Frequency / notes | Source |
|---|---|---|---|---|
| Female infertility | Clinical sign | HP:0008222 | Most common presentation. Among FGTB cases in the meta-analysis: 66% primary, 34% secondary infertility (not checked against full text) | [PMID 36438172, verified](https://pubmed.ncbi.nlm.nih.gov/36438172/); [PMC9423760](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9423760/) |
| Tubal occlusion / blocked fallopian tube | Imaging sign | Suggest "Fallopian tube obstruction"; HPO ID not verified | Unilateral or bilateral tubal block in about 58% on HSG (secondary citation) | [PMC4515237](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4515237/) |
| Hydrosalpinx | Imaging sign | Suggest "Hydrosalpinx"; HPO ID not verified | 12.6–19% | [PMC4515237](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4515237/); [J Hum Reprod Sci 2022](https://doaj.org/article/396c63263a10465385d90b3ba732ea0d) |
| Beaded, pipestem, golf-club, cobblestone or leopard-skin tube; Maltese cross sign | Imaging (HSG) | — | Characteristic but less common (beading about 2–5%) | [PMC3901176](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3901176/) |
| Peritubal adhesions (corkscrew tube, loculated spill, halo sign) | Imaging / operative | Pelvic adhesions | Common in chronic disease | [PMC3901176](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3901176/) |
| Pelvic / abdominal pain | Symptom | HP:0034267 (pelvic pain), HP:0002027 (abdominal pain) | Common; no reliable frequency found | [PMC9699775](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9699775/) |
| Menstrual disturbance (oligo-, hypo-, amenorrhoea; menorrhagia; postmenopausal bleeding) | Symptom | HP:0000141 (amenorrhea), HP:0000876 (oligomenorrhea) | Common | [PMC9699775](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9699775/) |
| Intrauterine adhesions (Asherman syndrome), when the endometrium is involved | Sign | — | Endometrium involved in 50–80% of FGTB | [PMC4666212](https://pmc.ncbi.nlm.nih.gov/articles/PMC4666212/) |
| Asymptomatic | — | — | Up to about 11% | [PMC4666212](https://pmc.ncbi.nlm.nih.gov/articles/PMC4666212/) |
| Ectopic pregnancy and early pregnancy loss | Complication | HP:0005268 (miscarriage) | Reported association | [PMC6943800](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6943800/) |

- **Onset and course:** reproductive age; insidious, chronic and progressive.
- **Quality of life:** dominated by infertility. No validated QoL data (EQ-5D or SF-36) were found.

## 4. Genetic / Molecular Information

Causal genes, pathogenic variants, modifier genes, epigenetic changes and chromosomal abnormalities are all **not applicable**, because the disease is infectious. No ClinVar, GWAS or epigenomic data specific to this disease were found.

## 5. Environmental Information

- **Infectious agents:** *M. tuberculosis* (NCBITaxon:1773); *M. bovis* (NCBITaxon:1765) rarely.
- **Toxins and lifestyle:** no disease-specific data. Undernutrition, crowding and HIV are general TB drivers but were not quantified for this outcome.

## 6. Mechanism / Pathophysiology

**Causal chain** (based on human histopathology and imaging; the molecular steps are inferred from general TB biology)

1. A primary *M. tuberculosis* infection, usually pulmonary, **leads to** bacteraemic or lymphatic seeding of distant organs ([PMID 30964083](https://pubmed.ncbi.nlm.nih.gov/30964083/)).
2. The richly vascular tubal mucosa and submucosa, often on both sides, receive the bacilli, which **results in** endosalpingitis ([PMC3901176](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3901176/)).
   - *Branch:* direct extension from peritoneal TB instead **results in** exosalpingitis or perisalpingitis.
3. Macrophage uptake and a T-cell (Th1) response **lead to** granuloma formation in the mucosa and on the serosal surface. The immune detail is inferred from general TB biology.
4. Caseous necrosis and ulceration **lead to** mucosal destruction.
5. Healing fibrosis, calcification and repeated flare-ups then **result in** the structural damage below ([PMC3901176](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3901176/)):
   - tubal occlusion (often cornual or isthmic), a rigid pipestem tube and beading;
   - fimbrial blockage leading to hydrosalpinx or pyosalpinx;
   - peritubal adhesions.
6. These changes **result in** blocked gamete transport, causing infertility and ectopic pregnancy ([PMID 36438172](https://pubmed.ncbi.nlm.nih.gov/36438172/)).
7. Descending spread to the endometrium **leads to** intrauterine adhesions and poor endometrial receptivity. This adds to infertility and causes hypomenorrhoea or amenorrhoea.
   - *Branch:* spread to the ovary reduces ovarian reserve ([PMID 36438172](https://pubmed.ncbi.nlm.nih.gov/36438172/)).

**Ontology suggestions**
- GO biological processes: granuloma formation (GO:0002432); inflammatory response (GO:0006954); defense response to bacterium (GO:0042742); tissue remodeling (GO:0048771); collagen fibril organization (GO:0030199). These are suggested terms whose IDs have not been checked against the ontology.
- CL cell types: macrophage (CL:0000235); epithelioid cell; Langhans giant cell; CD4⁺ T cell (CL:0000624); fibroblast (CL:0000057); fallopian tube ciliated epithelial cell.

**Molecular profiling, omics, single-cell and CRISPR data:** none found for this disease.

## 7. Anatomical Structures Affected

- **Primary organ:** fallopian tube (UBERON:0003889). Involvement is usually bilateral but asymmetric ([PMC3901176](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3901176/)).
- **Secondary organs:**
  - endometrium (UBERON:0001295), 50–60%;
  - ovary (UBERON:0000992), 10–30%;
  - peritoneum (UBERON:0002358);
  - cervix and vulva, rarely ([PMC9699775](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9699775/)).
- **Body system:** female reproductive system.
- **Tissues:** tubal mucosal epithelium, lamina propria and muscularis; granulomatous inflammatory tissue.
- **Subcellular:** *M. tuberculosis* lives inside macrophage phagosomes (GO:0045335). This is general TB biology.

## 8. Temporal Development

- **Onset:** usually ages 20–40 (reproductive age); insidious and chronic.
- **Course:** from early mucosal granulomas to chronic fibrosis with adhesions and occlusion ([PMC3901176](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3901176/)).
- **Remission:** treatment cures the infection, but established tubal and endometrial damage is largely permanent.
- **Critical window:** diagnosis before structural damage. Outcomes are reported to be better when disease is diagnosed early and treated before fertility therapy ([preprint](https://essopenarchive.org/users/502862/articles/648135-female-genital-tuberculosis-in-infertile-women-a-practical-paradigm-for-management-based-on-reproductive-outcome-on-retrospective-analysis-of-various-subfertility-therapies-following-anti-tubercular-therapy)).

## 9. Inheritance and Population

- **Inheritance:** not applicable (acquired infection).
- **Prevalence:** in a 2022 meta-analysis, pooled FGTB prevalence among infertile women was about 20% (95% CI 15–25%), with very high heterogeneity (I² ≈ 99.9%). This figure comes from a secondary snippet and was not checked against the full text ([Ahmed et al., PMC9423760; probable PMID 36072071](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9423760/)). The abstract says "the biggest burden of the disease is present in low-income countries."
- **Geography:** highest in South Asia (India) and sub-Saharan Africa; rare in high-income countries.
- **Sex and age:** female by definition; reproductive age.
- **Population incidence:** no figure per 100,000 was found.

## 10. Diagnostics

The disease is paucibacillary, so diagnosis relies on a combination of tests ([PMID 36438172](https://pubmed.ncbi.nlm.nih.gov/36438172/)).

| Test | Performance / role | Source |
|---|---|---|
| Endometrial biopsy or aspirate (premenstrual): histopathology, AFB smear, liquid/solid culture | Highly specific; sensitivity about 22–42% for conventional methods | [PMC4029782](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4029782/) |
| Xpert MTB/RIF (CBNAAT) | Pooled specificity 100%, sensitivity 14%; endometrial specimen judged most suitable | [Meta-analysis, PMC12162420](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12162420/); [PMC12372248](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12372248/) |
| TB-PCR | Positives may be false; not sufficient alone | [PMC4666212](https://pmc.ncbi.nlm.nih.gov/articles/PMC4666212/) |
| Laparoscopy (tubercles, caseous nodules, adhesions, beaded or retort tubes) with biopsy | Highest yield in composite-reference studies (15 positive vs 2–3 by culture or histology) | [DOAJ 2020](https://doaj.org/article/50dbcce9ddd4488a939672580b702762) |
| Hysterosalpingography | Signs listed in §3. HSG is contraindicated in active disease because it can spread infection | [PMC3901176](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3901176/); [PMC4515237](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4515237/) |
| Hysteroscopy | Intrauterine adhesions, pale endometrium | [PMC4666212](https://pmc.ncbi.nlm.nih.gov/articles/PMC4666212/) |
| Chest X-ray, IGRA / tuberculin test | Supportive; cannot localise disease | General |

- **Genetic testing, omics and newborn screening:** not applicable.
- **Differential diagnosis:**
  - non-TB pelvic inflammatory disease (chlamydia, gonorrhoea);
  - endometriosis;
  - salpingitis isthmica nodosa (also shows a beaded tube on HSG);
  - ovarian cancer with ascites and raised CA-125, which can mimic peritoneal and adnexal TB;
  - Asherman syndrome from other causes.

## 11. Outcome / Prognosis

- **Mortality:** low; the infection is curable.
- **Main morbidity:** permanent tubal-factor infertility.
- **Conception after treatment:** reviews describe the rate after anti-TB treatment as "not very encouraging" ([PMC9699775](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9699775/)).
- **IVF pregnancy rates:** 7.7–68.8% across studies ([Obstet Gynecol Sci review](https://synapse.koreamed.org/articles/1516090256)).
  - In an IVF-centre cohort of 443 women, early treatment based on a positive endometrial PCR gave pregnancy rates similar to PCR-negative women (59.8% vs 60.9%) ([Jindal, Hum Reprod 2012, doi:10.1093/humrep/des076](https://academic.oup.com/humrep/article/27/5/1368/700843)).
  - Severe endometrial damage gives a poor IVF prognosis ([PMC9486627](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9486627/)).
- **Complications:** hydro- or pyosalpinx, tubo-ovarian abscess, ectopic pregnancy, recurrent pregnancy loss ([PMC6943800](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6943800/)), and Asherman syndrome. After hysteroscopic treatment of Asherman syndrome, only 14.7% reported menstrual correction ([PMID 38326846](https://pubmed.ncbi.nlm.nih.gov/38326846/); this cohort includes non-TB cases).
- **Prognostic factors:** extent of tubal and endometrial damage, and timing of diagnosis.

## 12. Treatment

**Pharmacotherapy**
- Treatment follows the standard 6-month regimen for drug-susceptible TB ([PMC9699775](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9699775/); [ICMR STW](https://icmr.gov.in/icmrobject/uploads/STWs/1725964688_8_fgtm_15032022.pdf)):
  - 2 months of isoniazid, rifampicin, pyrazinamide and ethambutol (2HRZE);
  - then 4 months of isoniazid, rifampicin and ethambutol (4HRE, under the Indian programme).
- Suggested NCIT terms: Isoniazid, Rifampin, Pyrazinamide, Ethambutol, Antitubercular Agent.
- Pharmacogenomics: NAT2 acetylator status affects isoniazid toxicity. This is general knowledge and was not retrieved in this session.

**Effect on fertility**
- The effect of anti-TB treatment on pregnancy outcomes is "very uncertain". Very-low-certainty evidence from one RCT suggests little or no benefit in women without structural damage ([Fernandez-Guzman et al., BMJ Open 2023;13:e070456, PMID 37758670 inferred from the MEDLINE record](https://doaj.org/article/927f6b4468514e85b8dafc18ba74058b)).
- Over-treatment based on PCR alone is a concern.

**Surgery and assisted reproduction**
- Salpingectomy or proximal tubal occlusion for hydrosalpinx before IVF may improve pregnancy rates ([PMID 36438172](https://pubmed.ncbi.nlm.nih.gov/36438172/)).
- Hysteroscopic adhesiolysis for Asherman syndrome.
- IVF/ET, including frozen embryo transfer after treatment ([PMC7340987](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7340987/)).
- Suggested NCIT terms: Salpingectomy; In Vitro Fertilization; Hysteroscopy; Laparoscopy.

**Experimental:** [NCT05311423](https://clinicaltrials.gov/study/NCT05311423) is an observational study of prevalence and reproductive outcome. Gene, cell and RNA therapies are not applicable.

## 13. Prevention

- **Primary:** control pulmonary TB (case finding, treatment, contact tracing). Neonatal BCG vaccination protects mainly against disseminated childhood TB; no tubal-TB-specific data were found.
- **Secondary:** screen infertile women in endemic areas with endometrial sampling plus a composite of tests, and treat early, before structural damage.
- **Tertiary:** complete anti-TB therapy; avoid HSG and hydrotubation during active disease; remove hydrosalpinges before IVF.
- **Genetic counselling:** not applicable.

## 14. Other Species / Natural Disease

- **Cattle (*Bos taurus*, NCBITaxon:9913):** *M. bovis* genital infection is rare; infection "rarely occurs through the skin... or genital tract (at breeding)" ([NAP](https://www.nap.edu/read/9144/chapter/4); [CFSPH fact sheet](https://www.cfsph.iastate.edu/Factsheets/pdfs/bovine_tuberculosis.pdf)).
  - A 1989 *J Comp Pathol* study described uterine and tubal epithelium in five cows with genital TB; I did not retrieve its details.
  - Most bovine salpingitis is non-mycobacterial ([PMC6659645](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6659645/)).
- **Zoonosis:** *M. bovis* is zoonotic, spread through unpasteurised milk and contact with animals.
- **OMIA / breed / orthologous genes:** not applicable.

## 15. Model Organisms

- **No dedicated tubal-TB model was found.**
- **C57BL/6 mice infected intravenously with *M. tuberculosis*:** bacilli were found in the uterine horns at day 90, with nonspecific acute and chronic inflammation of the reproductive tract. This is a partial model of hematogenous genital seeding ([Russian group, Bull Exp Biol Med; e.g., PMID 27165069, unverified match](https://www.pubmed.gov/27165069/); [Springer](https://link.springer.com/doi/10.1007/s10517-016-3310-9)).
- **Aerosol- or intratracheal-infected mice:** no genital bacilli were detected in early infection ([Springer 2019](https://link.springer.com/content/pdf/10.1007/s10517-019-04589-8.pdf)).
- **Limitations:** mice do not form human-like caseous granulomas, the mouse oviduct anatomy differs, and none of these models shows tubal occlusion or infertility.
- **Resources:** MGI lists DOID:0050166, but I found no curated models.

---

### Key references with verified PMIDs
- Sharma JB et al. Female genital tuberculosis: Revisited. *Indian J Med Res* 2018. **PMID 30964083**
- Tjahyadi D et al. Female genital tuberculosis: clinical presentation, current diagnosis, and treatment. *Infect Dis Obstet Gynecol* 2022. **PMID 36438172**
- Asherman syndrome in a low-resource setting. *BMC Womens Health* 2024. **PMID 38326846**

### PMIDs that are probable but unconfirmed
- Ahmed et al., *SQUMJ* 2022: **36072071**
- Fernandez-Guzman et al., *BMJ Open* 2023: **37758670**
- Mouse genital-TB study: **27165069**

Other sources are cited by PMC ID or DOI above.

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 20 |
| Resolved | 20 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 20 |
| On topic | 9 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

1 of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMC:PMC3901176` *(abstract only)*: "tuberculous involvement of the fallopian tube occurs by the hematogenous route from a TB focus elsewhere, usually pulmonary or osseous"
  - closest text in source: "Part I presents specific findings of tuberculosis related to tubes such as "beaded tube", "golf club tube", "pipestem tube", "cobble stone tube" and "leopard skin tube""
- `PMC:PMC9699775`: "not very encouraging"
  - Text part not found as substring: 'not very encouraging'

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 24 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 12 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0000271` (5 mentions) - the report calls it "MONDO"; MONDO calls it **tuberculous salpingitis**
- `DOID:0050166` (5 mentions) - the report calls it "Disease Ontology"; DOID calls it **tuberculous salpingitis**
- `HP:0008222` (1 mention) - the report calls it "Clinical sign"; HP calls it **Female infertility**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `NCBITaxon:1773` (1 mention) - the report calls it "M. tuberculosis"; NCBITaxon calls it **Mycobacterium tuberculosis**, and lists "Bacterium tuberculosis" among its other names
- `NCBITaxon:1765` (1 mention) - the report calls it "M. bovis"; NCBITaxon calls it **Mycobacterium tuberculosis variant bovis**, and lists "Mycobacterium bovis" among its other names
- `GO:0002432` (1 mention) - the report calls it "GO biological processes: granuloma formation"; GO calls it **granuloma formation**
- `CL:0000235` (1 mention) - the report calls it "CL cell types: macrophage"; CL calls it **macrophage**
- `UBERON:0003889` (1 mention) - the report calls it "Primary organ:** fallopian tube"; UBERON calls it **fallopian tube**