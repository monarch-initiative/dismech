---
provider: claude_code
model: claude-haiku-5-5, claude-opus-4-8, claude-opus-5-5
cached: false
start_time: '2026-11-04T11:55:03.891278'
end_time: '2026-11-04T12:00:27.675479'
duration_seconds: 323.78
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Rift Valley Fever
  mondo_id: MONDO:0017880
  category: Infectious
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: RVF
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
  - claude-opus-4-8
  - claude-opus-5-5
  web_search_requests: 3
  num_turns: 12
  total_cost_usd: 2.5974716999999994
  session_id: fa05644f-0adb-4c06-8197-ccfff32bc0c7
  stop_reason: end_turn
  permission_denials: 1
  denied_tools:
  - Bash
  assistant_text_blocks: 3
citation_count: 6
reference_validation:
  total_references: 4
  verified: 4
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 4
  on_topic: 3
  validator_version: 0.5.1
term_validation:
  total_terms: 45
  verified: 44
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 6
  labels_matching: 4
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: NCBITaxon:11588
    reported_labels:
    - Bunyavirales
    ontology_label: Rift Valley fever virus
  - term_id: UBERON:0002107
    reported_labels:
    - Liver
    - Primary organ:** **Liver
    ontology_label: liver
  obsolete_terms:
  - term_id: HP:0001146
    ontology_label: obsolete Pigmentary retinal degeneration
    replaced_by: HP:0000580
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Rift Valley Fever
- **MONDO ID:** MONDO:0017880 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** RVF
- **Category:** Infectious

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Rift Valley Fever** covering all of the
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

Rift Valley Fever is a legitimate zoonotic viral disease, and this is a standard clinical/epidemiological research report for a medical knowledge base. I'll proceed with the research using the cached literature and web sources.

Most cached files only mention RVF in passing. Let me do targeted web research for authoritative, citable facts.

I have enough authoritative material from the literature and the successful searches to produce the report. (One web search's summarizer layer refused on an incidental classifier flag; the vaccine/diagnostic facts below are standard public-health literature and I've drawn them from the established record, flagging where I could not re-verify an exact quote.)

---

# Rift Valley Fever — Disease Characteristics Research Report

**Target:** Rift Valley Fever (RVF) · **MONDO:0017880** · Category: Infectious · Synonym: RVF
**Causal agent (not a host gene):** *Rift Valley fever virus* (RVFV) — an enveloped, tri‑segmented, negative‑/ambisense ssRNA virus, genus *Phlebovirus* (now *Phlebovirus riftense*), family **Phenuiviridae**, order **Bunyavirales** (NCBITaxon:11588). RVF is a zoonotic arboviral disease, **not** a Mendelian disorder; it has no causal human gene. The "causal gene(s): not recorded / OMIM: not recorded" fields in the template are therefore expected and correct — the pathogenesis is driven by the **viral** genome, whose S‑segment **NSs** protein is the principal virulence determinant.

A well‑curated dismech entry already exists (`kb/disorders/Rift_Valley_Fever.yaml`); this report is organized to validate and extend it.

---

## 1. Disease Information

RVF is a mosquito‑borne, zoonotic viral disease primarily of domestic ruminants (sheep, cattle, goats) in Africa and the Arabian Peninsula, with humans infected as epizootic spillover hosts. In animals it causes **"abortion storms"** and high neonatal mortality; in humans the great majority of infections are a self‑limiting febrile illness, with a minority progressing to one of three severe syndromes: **(i)** viral hemorrhagic fever with hepatic necrosis, **(ii)** delayed retinitis, and **(iii)** meningoencephalitis (Ikegami & Makino, *Viruses* 2011, PMID **21666766**; Bird et al., *JAVMA* 2009, PMID **19335238**).

**Key identifiers:** MONDO:0017880; ICD‑11 **1D49** (Rift Valley fever); ICD‑10 **A92.4**; MeSH **D012295** ("Rift Valley Fever"); the agent is NCBITaxon:11588. There is no OMIM entry (not a heritable human disorder). **Synonyms/alternative names:** RVF; enzootic hepatitis (historical, in livestock).

**Data provenance:** Information is derived from **aggregated, disease‑level resources** — outbreak investigations, hospital case series, serosurveys, WHO/CDC/OIE (WOAH) surveillance, and virological reviews — not individual‑patient EHR records.

---

## 2. Etiology

**Disease causal factor — infectious.** The sole cause is infection with RVFV. Transmission to humans is by **(a)** bites of infected mosquitoes — floodwater *Aedes* spp. (notably *Aedes mcintoshi/ochraceus*), which maintain the virus **transovarially** in desiccation‑resistant eggs and are the presumed reservoir, and *Culex* spp. (e.g. *Cx. pipiens*, *Cx. tritaeniorhynchus*), which amplify epidemics; and **(b)** direct contact with blood, body fluids, tissues, and aborted fetal material of viraemic livestock during slaughter, butchering, birthing, and veterinary handling, including **aerosol** exposure (Pepin et al., *Vet Res* 2010, PMID **21188836**; Linthicum et al., *Annu Rev Entomol* 2016, PMID **26497313**).

**Environmental / behavioural risk factors (the dominant axis for this disease):**
- **Heavy rainfall and flooding** (El Niño/Southern Oscillation–linked) that flood *dambo* habitats and produce explosive mosquito emergence — the single strongest epidemic driver; satellite NDVI/rainfall anomalies can predict outbreaks (Anyamba et al., *PNAS* 2009, PMID **19144928**; Linthicum et al., *Science* 1999, PMID **10411503**).
- **Occupational contact** with livestock — herders, pastoralists, abattoir/slaughterhouse workers, veterinarians (identified as risk factors in the Kenya 2006–07 investigation: *"Of these, 52 (26%) had severe RVF disease characterized by hemorrhagic manifestations or death"* — Anyangu et al., *Am J Trop Med Hyg* 2010, PMID **20682902**).
- **Consumption/handling of sick animals; drinking raw milk; sheltering animals in the home.**
- **Male sex and adult age** (occupational exposure pattern).

**Protective factors:** Avoidance of contact with viraemic animal tissues, personal protective equipment at slaughter, vector avoidance, and **livestock vaccination** (indirect human protection by suppressing amplification). No human protective genetic variant is established. There is biological rationale (and mouse/in‑vitro data) that an intact **type I interferon** response is protective, since the viral NSs protein exists specifically to defeat it, but a validated *human* genetic protective locus is **not available**.

**Gene–environment interactions:** Not applicable in the human‑Mendelian sense. The relevant "G×E" is **viral‑genotype × ecological**: NSs/NSm virulence determinants interacting with vector ecology and rainfall.

---

## 3. Phenotypes

Human RVF is clinically staged: a common self‑limiting febrile phase, and uncommon severe syndromes. Severe disease affects roughly **1–3%** of infections in population terms (up to ~8% attack rates reported), but hospital series are heavily biased toward severe cases.

| Phenotype | Type | HPO suggestion | Timing / frequency |
|---|---|---|---|
| Fever | symptom | **HP:0001945** Fever | Acute phase; near‑universal |
| Myalgia | symptom | **HP:0003326** Myalgia | Acute phase; common |
| Headache | symptom | **HP:0002315** Headache | Acute phase; common |
| Arthralgia | symptom | **HP:0002829** Arthralgia | Acute phase; common |
| Photophobia | sign | **HP:0000613** Photophobia | Acute phase |
| Hepatitis / hepatic necrosis | sign | **HP:0012115** Hepatitis | Severe form |
| Elevated transaminases | lab | **HP:0002910** Elevated circulating hepatic transaminase concentration | Marker of hepatic involvement |
| Jaundice | sign | **HP:0000952** Jaundice | Severe hepatic form |
| Hemorrhage (epistaxis, GI bleeding, petechiae) | sign | **HP:0001892** Abnormal bleeding | ~2–4 d after onset in hemorrhagic form |
| Thrombocytopenia | lab | **HP:0001873** Thrombocytopenia | Severe form |
| Disseminated intravascular coagulation | lab | **HP:0005521** DIC | Hemorrhagic form |
| Retinitis / retinal hemorrhage | sign | **HP:0000573** Retinal hemorrhage; (retinitis: **HP:0007973** Retinal vasculitis / **HP:0001146** Pigmentary retinopathy as scarring correlate) | **1–3 weeks** after fever; ~1–10% |
| Permanent vision loss (macular scar / central scotoma) | sign | **HP:0000618** Blindness | Late sequela of macular retinitis |
| Meningoencephalitis / encephalitis | sign | **HP:0002383** Infectious encephalitis; **HP:0001298** Encephalopathy | Days–weeks after acute phase |

**Severity / progression characteristics:** Onset is **acute** after a short incubation of ~**2–6 days** (range up to ~1 week). Most patients recover in 4–7 days. The three severe syndromes are largely **temporally distinct**: the hemorrhagic‑hepatic form appears **2–4 days** into illness; retinitis is **delayed 1–3 weeks** and often follows apparent recovery; encephalitis can accompany a second febrile phase. Macular retinitis is the leading cause of **permanent** morbidity in survivors.

**Supporting quotes (verified):** Al‑Hazmi et al. (Saudi Arabia 2000, prospective series of 165 hospitalized patients): *"Sixteen patients had retinitis and 7 patients had meningoencephalitis"* (Clin Infect Dis 2003, PMID **12539063**); overall in that series 56/165 (33.9%) died and hemorrhagic manifestations occurred in 32 (19.4%).

**Quality‑of‑life impact:** Dominated by **permanent visual impairment** from macular/paramacular retinitis (central scotoma), and by neurological sequelae in encephalitic survivors (focal deficits, cognitive impairment). No disease‑specific EQ‑5D/SF‑36 instrument is established for RVF; impact is reported qualitatively in case series.

---

## 4. Genetic / Molecular Information

**No human causal or susceptibility gene** is established (no OMIM, no ClinVar/HGMD entries — expected for an arboviral zoonosis). The relevant genetics is **viral**:

- **Genome:** three negative‑sense/ambisense RNA segments. **L** encodes the RdRp (L protein); **M** encodes a polyprotein yielding the glycoproteins **Gn** and **Gc** plus the non‑structural **NSm** and a 78‑kDa protein; **S** uses an **ambisense** strategy to encode the **nucleoprotein (N)** and the non‑structural **NSs** (Bouloy & Weber, *Open Virol J* 2010, PMID **20517490**; Ikegami & Makino 2011, PMID **21666766**).
- **NSs — principal virulence factor** (analogous to a viral "oncogene‑like" effector). It forms nuclear filaments and defeats innate immunity by three documented mechanisms:
  1. **Suppression of host general transcription** by sequestering the **p44/TFIIH** subunit and degrading **TFIIH p62** → shutoff of interferon‑β induction (Le May et al., *Cell* 2004, PMID **14980221**; Billecocq et al., *J Virol* 2004, PMID **15479799**).
  2. **Promoting post‑transcriptional degradation of PKR** (dsRNA‑activated protein kinase), relieving translational block (Ikegami et al., *PLoS Pathog* 2009, PMID **19197350**; Habjan et al., *J Virol* 2009, PMID **19570864**).
  3. Downregulation of IFN‑β at the promoter level via repression of the host SAP30/YY1 complex.
- **NSm** is anti‑apoptotic and supports vector infection; deletion attenuates (Won et al., *J Virol* 2007, PMID **17596309**).
- **Attenuating viral variants:** the naturally attenuated **Clone 13** carries a large **in‑frame deletion in the NSs ORF** (Muller et al., *Am J Trop Med Hyg* 1995, PMID **7872449**) — the molecular basis of a leading veterinary vaccine.

**Functional consequence:** NSs is a **gain‑of‑virulence / immune‑antagonist**; its loss (Clone 13, MP‑12 partially) is **loss‑of‑function → attenuation**. Modeled in dismech as pathway‑state `modifier: DECREASED` on type I IFN induction (GO:0032480), which is correct — there is no host variant to carry `functional_impact_category`.

**Epigenetics / chromosomal abnormalities:** Not applicable (host). RVFV biology is RNA‑segment‑based; **reassortment** between co‑infecting strains is the principal source of genetic novelty (analogous to influenza), documented in field isolates.

---

## 5. Environmental Information

- **Climatic:** Excess rainfall/flooding (ENSO‑linked), elevated NDVI, and *dambo*/pan flooding drive mosquito emergence and epizootics (Anyamba et al., *PNAS* 2009, PMID **19144928**).
- **Ecological/agricultural:** Irrigation schemes and dam construction (e.g. the 1987 Mauritania outbreak after the Diama dam on the Senegal River) create permanent vector habitat.
- **Occupational/lifestyle:** Livestock husbandry, slaughter, and consumption/handling of sick animals (Section 2).
- **Infectious agent (CHEBI/NCBITaxon):** RVFV, **NCBITaxon:11588**. Vectors: *Aedes* spp. and *Culex* spp. (Culicidae). Amplifying hosts: Bovidae (NCBITaxon:9895), especially *Ovis aries* (NCBITaxon:9940), *Bos taurus* (NCBITaxon:9913), *Capra hircus* (NCBITaxon:9925).

Suggested exposure terms (ECTO): exposure via mosquito bite; occupational exposure to animal blood/tissue; aerosol exposure. (Verify exact ECTO CURIEs at binding time per `dismech-terms` — do not bind from memory.)

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Inoculation** of RVFV (mosquito bite or mucocutaneous/aerosol contact with viraemic tissue) **→ leads to** local replication in dermal/regional cells.
2. Viral replication **→ leads to** expression of **NSs**, which **suppresses host transcription and type I IFN induction** and **degrades PKR** (demonstrated in vitro and in mouse models; PMID **14980221**, **19197350**).
3. Defeat of the interferon response **→ results in** uncontrolled early replication and **high‑titre viraemia** with hepatotropic dissemination (viraemia magnitude correlates with severity — *inferred correlation from human/animal data*).
4. Viraemia **→ leads to** preferential infection of **hepatocytes and Kupffer cells**, producing **midzonal→massive hepatic necrosis** (the pathological hallmark of fatal RVF).
   - **Branch 4a (hepatic):** Hepatocellular necrosis **→ results in** release of transaminases and **impaired synthesis of clotting factors**, and **→ leads to** jaundice.
   - **Branch 4b (vascular):** Systemic infection + cytokine response **→ leads to** **endothelial activation and increased vascular permeability** (the rate‑limiting lesion shared with other viral hemorrhagic fevers).
5. Impaired hepatic factor synthesis + endothelial injury + platelet consumption **→ results in** **consumptive coagulopathy / DIC** → **thrombocytopenia** and **hemorrhage** → multi‑organ failure and death in the severe hemorrhagic form.
6. **Delayed branch (ocular):** 1–3 weeks after the acute phase, a **largely immune‑mediated retinitis** (vasculitis, retinal hemorrhage, macular edema) develops **→ leads to** permanent **vision loss** when the macula scars. (Immune‑mediated mechanism is **inferred** from its post‑viraemic timing, not demonstrated by biopsy.)
7. **Delayed branch (neurological):** days–weeks later, **neuroinvasion** produces **meningoencephalitis → encephalitis** with headache, confusion, focal deficits.

### Supporting detail by category
- **Molecular pathways:** RIG‑I/MAVS → IRF3/IRF7 → IFN‑β induction (antagonized by NSs); PKR–eIF2α translational control (antagonized); JAK‑STAT ISG signaling (blunted downstream of IFN suppression). GO: **GO:0032480** (negative regulation of type I IFN production), **GO:0019079** (viral genome replication), **GO:0039548** (suppression by virus of host IRF3 activity, conceptually), **GO:0060337** (type I interferon signaling pathway).
- **Cellular processes:** hepatocyte apoptosis/necrosis (**GO:0097284** hepatocyte apoptotic process), endothelial activation, inflammation/cytokinemia, neuronal infection.
- **Protein dysfunction:** NSs‑driven degradation of **TFIIH p62** and **PKR**; glycoprotein Gn/Gc mediate entry (receptor candidates include **LRP1**, DC‑SIGN for dendritic cells — Ganaie et al., *Cell* 2021, PMID **34320407** identified LRP1 as an RVFV entry receptor).
- **Tissue damage mechanisms:** direct viral cytopathology (liver), immunopathology (retina), vascular leak and DIC (hemostatic failure).
- **Cell types (CL):** hepatocyte **CL:0000182**; Kupffer cell **CL:0000091**; endothelial cell **CL:0000115**; dendritic cell **CL:0000451**; neuron **CL:0000540**.

### Molecular profiling
Transcriptomic/proteomic data exist largely from **animal models and cell lines** (mouse, rat, NHP challenge; GEO deposits for RVFV‑infected hepatocytes/macrophages). Human multi‑omics is limited by the sporadic, outbreak‑based nature of cases. CRISPR screens identified host entry/replication factors including **LRP1** (PMID **34320407**). Note evidence‑source discipline: these are predominantly **MODEL_ORGANISM / IN_VITRO**, not human clinical.

---

## 7. Anatomical Structures Affected

- **Primary organ:** **Liver** (UBERON:0002107) — hepatocytes and Kupffer cells; the principal target in fatal disease.
- **Vascular system / blood** (UBERON:0000178; endothelium UBERON:0001986) — the hemostatic/vascular lesion.
- **Eye / retina** (UBERON:0000970 eye; **UBERON:0000966** retina; macula UBERON:0004862) — delayed retinitis, typically **bilateral** but can be asymmetric; macular involvement causes permanent loss.
- **Central nervous system / brain** (UBERON:0000955; meninges UBERON:0002360) — meningoencephalitis.
- **Spleen** (UBERON:0002106) — replication site.
- **Body systems:** hepatobiliary, cardiovascular/hematologic, nervous, ocular.
- **Subcellular (GO CC):** viral replication is cytoplasmic; **NSs filaments are nuclear** (GO:0005634 nucleus) — a distinctive feature; Golgi (GO:0005794) for glycoprotein maturation and budding.

---

## 8. Temporal Development

- **Incubation:** ~**2–6 days** (up to ~1 week) after exposure.
- **Onset:** **acute**.
- **Course:** Most cases are **self‑limited** (recovery ~4–7 days). Severe syndromes follow distinct windows: hemorrhagic‑hepatic at **day 2–4**; retinitis at **1–3 weeks** (often after apparent recovery); encephalitis days–weeks later, sometimes as a **biphasic** fever.
- **Critical period for intervention:** the early viraemic phase (supportive escalation, isolation); there is no licensed antiviral, so timing is about supportive intensity and complication surveillance (serial ophthalmologic and neurological evaluation).
- **Epidemic tempo at population level:** explosive, rainfall‑driven epizootic/epidemic peaks over weeks to a few months, then quiescence (inter‑epidemic maintenance in *Aedes* eggs).

---

## 9. Inheritance and Population

**Not genetic** — no inheritance pattern, penetrance, carrier frequency, founder effect, or consanguinity role applies.

**Epidemiology:**
- **Geographic distribution:** sub‑Saharan and North Africa, Madagascar, Egypt, and the **Arabian Peninsula** (Saudi Arabia/Yemen since 2000 — the first spread outside Africa). Repeated large outbreaks: Egypt 1977–78; Kenya 1997–98 and **2006–2007**; Saudi Arabia/Yemen 2000; Mauritania (recurrent, incl. 2010, 2015, 2020); Mayotte; Niger 2016; Mauritania/Mali.
- **Human burden is epidemic, not steady‑endemic.** During the Kenya 2006–07 outbreak WHO reported, verbatim: *"From 30 November 2006 to 12 March 2007, a total of 684 cases including 155 deaths (case‑fatality ratio, 23%) of RVF was reported in Kenya."* (WHO DON, 2007).
- **Case‑fatality:** community‑/population‑wide ~**0.5–2%**; **hospitalized/severe series much higher** (e.g. Saudi Arabia 2000 series 33.9%; Kenya 2006–07 ~23%; Tanzania 2007 ~28%; Mauritania 2022 letter ~49%). Large serosurveys imply **up to ~180,000** mild/asymptomatic infections in the Kenya outbreak region, confirming the hospitalized CFR is upward‑biased (Nguku et al., *Am J Trop Med Hyg* 2010, PMID **20682901**).
- **Demographics:** higher incidence in **adult males** reflecting occupational animal contact; no ethnic genetic predisposition.

---

## 10. Diagnostics

- **Molecular:** **RT‑PCR / real‑time RT‑PCR** on serum during the viraemic phase — the mainstay of early confirmation (Bird et al., *J Clin Microbiol* 2007, PMID **17913929** describes a diagnostic RT‑PCR assay).
- **Serology:** **IgM capture ELISA** (recent infection) and **IgG ELISA / seroconversion**; **plaque‑reduction neutralization (PRNT)** as reference. Antigen‑detection ELISA is used in animals.
- **Virus isolation:** possible in BSL‑3+ settings from serum/tissue (RVFV is a high‑containment select agent; isolation is restricted to appropriately biosafe laboratories).
- **Supportive laboratory findings:** elevated AST/ALT (often markedly), thrombocytopenia, leukopenia then leukocytosis, coagulopathy (prolonged PT/aPTT, elevated D‑dimer, DIC), hyperbilirubinemia; LOINC‑codable analytes (ALT, AST, platelet count, PT, fibrinogen, bilirubin).
- **Histopathology:** hepatic **midzonal necrosis** with **Councilman‑like acidophilic bodies** and minimal inflammatory infiltrate; immunohistochemistry/IHC for viral antigen.
- **Imaging/functional:** ophthalmologic exam and **fluorescein angiography/OCT** for retinitis; neuroimaging/EEG and CSF analysis (lymphocytic pleocytosis) for encephalitis.
- **Clinical criteria / case definition:** WHO/CDC outbreak case definitions combine acute febrile illness in an epizootic setting with laboratory confirmation.
- **Differential diagnosis:** other viral hemorrhagic fevers (Crimean‑Congo HF, Ebola/Marburg, yellow fever, dengue), leptospirosis, severe malaria, Q fever, brucellosis, typhoid, viral hepatitis.

---

## 11. Outcome / Prognosis

- **Mild/uncomplicated RVF:** full recovery in days; excellent prognosis.
- **Hemorrhagic‑hepatic form:** high mortality (hospital series 10–50%); death from hepatic failure, hemorrhage, DIC, and multi‑organ failure.
- **Ocular form:** often **permanent central vision loss** when the macula is involved; ~50% of patients with macular retinitis retain a permanent deficit. Rarely fatal.
- **Encephalitic form:** significant mortality and frequent neurological sequelae in survivors.
- **Prognostic factors:** magnitude/duration of viraemia, degree of transaminase elevation, thrombocytopenia/DIC, presence of hemorrhage, encephalopathy, and hepatorenal failure predict death (Kenya and Saudi series). No validated molecular prognostic biomarker beyond viral load and hepatic/hemostatic markers.

---

## 12. Treatment

- **No licensed specific human antiviral or therapeutic.** Management is **supportive** (NCIT:C15747 Supportive Care): fluid/electrolyte management, correction of coagulopathy, transfusion support, organ‑failure management, and management in an appropriate **isolation/high‑containment** setting for hemorrhagic cases.
- **Investigational antivirals:** **ribavirin** has in‑vitro and animal activity but no proven human benefit and raises concern for CNS disease in some models; **favipiravir (T‑705)** shows activity in rodent models (favipiravir: Caroline et al. / Scharton et al., *Antimicrob Agents Chemother* 2014, PMID **24395232**). These remain experimental.
- **Ocular/neurological:** corticosteroids are used empirically for severe immune‑mediated retinitis/encephalitis, without controlled‑trial support.
- **Vaccines:** no licensed **human** vaccine. Candidates include the inactivated **TSI‑GSD‑200** (investigational, used for at‑risk laboratory/veterinary personnel under special protocols), the live‑attenuated **MP‑12**, and the chimpanzee‑adenovirus‑vectored **ChAdOx1 RVF**, which has entered early‑phase human trials (Warimwe/Jenner Institute programme). **Veterinary** vaccines are established and central to control: the live **Smithburn** strain, the inactivated vaccine, and **Clone 13** (NSs‑deletion) and MP‑12.
- **Treatment strategy:** early recognition in an outbreak, supportive escalation, complication surveillance (serial ophthalmologic/neurologic review), and strict infection control. (NCIT suggestions at binding: C15747 Supportive Care; C15986 Pharmacotherapy only if an agent is used off‑label; C15313 is not applicable.)

---

## 13. Prevention

- **Primary prevention (the core of RVF control):**
  - **Livestock vaccination** ahead of predicted outbreaks (Smithburn / Clone 13 / inactivated) to suppress amplification — the keystone intervention.
  - **Early warning / forecasting** using rainfall and NDVI satellite anomalies to pre‑position response (Anyamba et al., PMID **19144928**).
  - **Vector control** (larval source reduction, insecticides) during high‑risk periods; personal protection (repellents, bed nets).
  - **Safe animal‑handling practices** — PPE at slaughter/birthing, avoiding contact with abortus material, **avoiding raw milk**, and **movement restrictions/slaughter bans** during epizootics.
- **Secondary prevention:** outbreak surveillance (sentinel herds, human case detection) and rapid laboratory confirmation for early response.
- **Tertiary prevention:** complication surveillance and supportive care to limit mortality and permanent sequelae.
- **Public health / One Health:** integrated human–animal–environment surveillance, abattoir regulation, and community health education; environmental management of irrigation/dam habitats.
- **Prophylaxis:** investigational human vaccination restricted to high‑risk laboratory and veterinary personnel.

---

## 14. Other Species / Natural Disease

- **Species affected (natural amplifying/clinical hosts):** domestic ruminants are most susceptible — **sheep** (*Ovis aries*, NCBITaxon:9940) and **goats** (*Capra hircus*, NCBITaxon:9925) most severely, **cattle** (*Bos taurus*, NCBITaxon:9913); also camels (*Camelus dromedarius*). Wild ruminants and rodents show infection/seropositivity; buffalo and some wildlife amplify.
- **Natural disease in animals:** characteristic **"abortion storms"** (near‑100% abortion in pregnant ewes) and **very high mortality in newborn lambs/kids** (often >90%), with hepatic necrosis — more severe than typical human disease. This is of major **veterinary and economic** importance (Bird et al., *JAVMA* 2009, PMID **19335238**).
- **Comparative pathology:** liver is the shared primary target across species; neonatal animals and humans both show massive hepatic necrosis, but the **abortifacient** effect is an animal‑specific hallmark.
- **Transmission / zoonotic potential:** strongly **zoonotic**; humans are **incidental dead‑end hosts** (viraemia insufficient for onward mosquito transmission). Cross‑species susceptibility spans many mammals.
- **OMIA:** RVF is catalogued as an infectious (non‑Mendelian) condition of livestock rather than an OMIA Mendelian trait.

---

## 15. Model Organisms

- **Mouse** (*Mus musculus*): the principal small‑animal model; wild‑type mice are highly susceptible, developing early hepatic necrosis and, in survivors, delayed encephalitis — recapitulating the biphasic human severe disease. **Type I IFN‑receptor knockout (IFNAR⁻/⁻)** mice are uniformly, rapidly susceptible, confirming the IFN axis NSs targets (Bouloy et al., *J Virol* 2001, PMID **11152510**).
- **Rat** (*Rattus norvegicus*): strain‑dependent susceptibility (Lewis vs Wistar‑Furth) models hepatic vs encephalitic outcomes.
- **Non‑human primates** (rhesus macaque, marmoset, common marmoset): model hemorrhagic and febrile disease for vaccine/therapeutic testing.
- **Induced/genetic models:** the attenuating **NSs‑deletion (Clone 13)** and **MP‑12** reverse‑genetics systems are core tools; recombinant RVFV with NSs/NSm deletions dissect virulence.
- **In vitro:** hepatocyte and macrophage/dendritic‑cell lines; CRISPR screens (host factor **LRP1**, PMID **34320407**).
- **Phenotype recapitulation / limitations:** mice over‑recapitulate lethality relative to average human infection; NHP are closest to human disease but scarce; **retinitis — the signature human sequela — is poorly modeled** in rodents, a key translational gap (relevant to any dismech `FAILS_TO_RECAPITULATE` / `HUMAN_MODEL_MISMATCH` annotation for the ocular node).
- **Resources:** MGI (mouse), RGD (rat), and the RVFV reverse‑genetics literature.

---

## Citation notes and evidence‑discipline flags

- **Verified exact quotes** (safe to use as dismech `snippet:` after re‑fetching the source into `references_cache/`): the WHO Kenya statement ("*From 30 November 2006 to 12 March 2007, a total of 684 cases including 155 deaths (case‑fatality ratio, 23%)*"); Al‑Hazmi ("*Sixteen patients had retinitis and 7 patients had meningoencephalitis*", PMID 12539063); Kenya risk‑factor study ("*Of these, 52 (26%) had severe RVF disease characterized by hemorrhagic manifestations or death*").
- **PMIDs cited from the established literature** (confirm each with `just fetch-reference PMID:…` before binding — do not enter a snippet unverified): 21666766 (Ikegami & Makino 2011), 19335238 (Bird 2009), 21188836 (Pepin 2010), 20517490 (Bouloy & Weber 2010), 14980221 (Le May 2004), 19197350 (Ikegami 2009 PKR), 19570864 (Habjan 2009), 12539063 (Al‑Hazmi 2003), 14523773 (Madani 2003), 20682901 / 20682902 (Kenya 2006‑07 series), 19144928 (Anyamba 2009), 10411503 (Linthicum 1999), 34320407 (Ganaie 2021 LRP1), 24395232 (favipiravir), 11152510 (Bouloy 2001 IFNAR mouse), 7872449 (Muller 1995 Clone 13).
- **Per‑CLAUDE.md:** this is a microbial/infectious entry — on binding, ensure ≥1 NCBITaxon `infectious_agent` and ≥1 `transmission` route (already present), and consider conformance to the `viral_hemorrhagic_fever_syndrome` module (already used for the viraemia and vascular‑leak nodes). Model‑organism evidence (mouse/NHP) must be graded `MODEL_ORGANISM` and not stand alone for human phenotypes.

**Sources (web):**
- [Frontiers in Immunology 2022 — RVFV/host innate immunity review (PMC9813963)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9813963)
- [WHO Disease Outbreak News — RVF Kenya 2007](https://www.who.int/emergencies/disease-outbreak-news/item/2007_05_09-en)
- [Nguku et al., Kenya 2006‑07 outbreak investigation (PMC2913492)](https://pmc.ncbi.nlm.nih.gov/articles/PMC2913492)
- [Al‑Hazmi et al. 2003, Saudi Arabia series (qxmd/PMID 12539063)](https://www.qxmd.com/r/12539063)
- [Epidemiologic and clinical aspects of the Tanzania 2007 RVF outbreak (ILRI)](https://www.ilri.org/knowledge/publications/epidemiologic-and-clinical-aspects-rift-valley-fever-outbreak-humans)
- ["The challenging management of Rift Valley fever in humans" (Javelle et al.)](https://typeset.io/pdf/the-challenging-management-of-rift-valley-fever-in-humans-lyubffn7fw.pdf)

This report mirrors and is consistent with the existing `kb/disorders/Rift_Valley_Fever.yaml` entry; the main extensions beyond the current entry are the **ocular/encephalitic timing detail**, the **LRP1 entry receptor** (PMID 34320407), **favipiravir/ribavirin** investigational status, the **vaccine landscape** (Clone 13, MP‑12, ChAdOx1 RVF), and the **retinitis modeling gap** worth recording as a `HUMAN_MODEL_MISMATCH`.

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

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
| Terms checked | 45 |
| Resolved | 44 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 6 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `NCBITaxon:11588` (3 mentions) - the report calls it "Bunyavirales"; NCBITaxon calls it **Rift Valley fever virus**
- `UBERON:0002107` (1 mention) - the report calls it "Liver", "Primary organ:** **Liver"; UBERON calls it **liver**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0001146` (obsolete Pigmentary retinal degeneration) (1 mention) - replaced by `HP:0000580`

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `UBERON:0002107` - called "Liver", "Primary organ:** **Liver"