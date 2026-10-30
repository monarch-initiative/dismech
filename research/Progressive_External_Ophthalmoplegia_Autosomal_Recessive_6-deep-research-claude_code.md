---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-29T06:06:35.016777'
end_time: '2026-10-29T06:10:37.769810'
duration_seconds: 242.75
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Progressive External Ophthalmoplegia Autosomal Recessive 6
  mondo_id: MONDO:0957993
  category: Mendelian
  causal_genes: RRM1
  omim_id: OMIM:620647
  synonyms: PEOB6
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
  num_turns: 21
  total_cost_usd: 1.0273114
  session_id: 0bfb328d-96db-5dca-803a-342a247b0264
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  assistant_text_blocks: 3
citation_count: 15
reference_validation:
  total_references: 3
  verified: 3
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 3
  on_topic: 3
  validator_version: 0.4.0
term_validation:
  total_terms: 46
  verified: 43
  not_found: 0
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 4
  labels_matching: 1
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0957993
    reported_labels:
    - MONDO
    ontology_label: progressive external ophthalmoplegia with mitochondrial dna deletions,
      autosomal recessive 6
  - term_id: NCBITaxon:4932
    reported_labels:
    - yeast RNR1 and RNR3
    ontology_label: Saccharomyces cerevisiae
  labels_variant: 1
  obsolete_terms:
  - term_id: GO:0000002
    ontology_label: obsolete mitochondrial genome maintenance
  unresolvable_prefixes:
  - ORPHA
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Progressive External Ophthalmoplegia Autosomal Recessive 6
- **MONDO ID:** MONDO:0957993 (if available)
- **Causal gene(s):** RRM1
- **OMIM:** OMIM:620647
- **Synonyms:** PEOB6
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Progressive External Ophthalmoplegia Autosomal Recessive 6** covering all of the
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

Still researching: I'm pulling the PubMed abstract and gene and model-organism details for RRM1.

Researching: reading the JCI paper's discussion for the structural mechanism and treatment implications.

# Progressive External Ophthalmoplegia, Autosomal Recessive 6 (PEOB6; RRM1): Research Report

## Summary

- **The disease and its gene.** PEOB6 (MONDO:0957993; OMIM #620647) is an autosomal recessive mitochondrial DNA (mtDNA) maintenance disorder. It is caused by homozygous variants in **RRM1** (hgnc:10451; OMIM *180410; 11p15.4). RRM1 is the catalytic subunit of ribonucleotide reductase (RNR), the enzyme that makes DNA building blocks (dNTPs) from scratch.
- **The evidence base is one paper.** It rests entirely on Shintaku et al., *J Clin Invest* 2022, PMID:35617047 (PMC9246377). The recessive disease covers 5 patients from 3 families, all homozygous for a change at arginine 381.
- **The search found no later case reports or treatment studies (2023–2026).**
- **Dominant p.N427K is a separate disease.** The same paper reports a heterozygous catalytic-site variant, p.N427K, in one British family. OMIM's gene-map row for RRM1 lists both AD and AR inheritance. **That dominant family is not PEOB6** and should not be lumped into this entry.

**Before any of this goes into the KB:**

- **Snippets.** The fetch tools would not return abstracts word for word, so only short fragments from the PMID:35617047 abstract are quoted here. Use `just fetch-reference PMID:35617047` and copy snippets from the cached text.
- **Ontology IDs.** Every HP, GO, CL, UBERON and NCIT ID below is a lead written from memory. Look each one up before binding it, as the repo's CURIE rule requires.

---

## 1. Disease information

**What it is.** Adult-onset (in one patient, childhood-onset) ptosis and progressive external ophthalmoplegia. It comes with variable myopathy, gut dysmotility and cachexia, neuropathy, and multiple mtDNA deletions in skeletal muscle.

| Identifier | Value | Source |
|---|---|---|
| MONDO | MONDO:0957993 | MedGen C5882731 |
| OMIM | #620647 | MedGen / OMIM |
| MedGen | UID 1847098; CUI C5882731 | [MedGen](https://www.ncbi.nlm.nih.gov/medgen/1847098) |
| Orphanet | None specific to PEOB6 was found. The broader autosomal recessive PEO class applies (ORPHA:254892 — verify). | — |
| ICD-10 | H49.4 (progressive external ophthalmoplegia, nonspecific) | — |
| ICD-11 | No specific code | — |
| MeSH | D017246 Ophthalmoplegia, Chronic Progressive External (broader term — verify) | — |
| KEGG | H01395, autosomal recessive PEO (lists RRM1 among its genes) | [KEGG](https://www.kegg.jp/entry/H01395) |

**Synonyms:** PEOB6; progressive external ophthalmoplegia with mitochondrial DNA deletions, autosomal recessive 6.

**Type of source.** All information comes from individual patient case descriptions in one multicentre paper. There are no registry or EHR data.

**Key abstract statements (PMID:35617047):**
- "5 probands from 4 families who presented with ptosis and ophthalmoplegia as well as other clinical manifestations and multiple mtDNA deletions in muscle"
- "Our data reveal that primary RRM1 deficiency and, by extension, impaired de novo nucleotide synthesis are causes of MDDS."

## 2. Etiology

- **Cause.** Biallelic (homozygous) loss-of-function missense variants in RRM1. Both known recessive variants change arginine 381:
  - c.1142G>A, p.R381H
  - c.1141C>T, p.R381C
  - The abstract describes them as "RRM1 loss-of-function variants … 2 homozygous recessive variants at p.R381."
- **Risk factors.**
  - Parental consanguinity: the Saudi family 1 (probands 1a and 1b) is consanguineous.
  - Recurrence of p.R381C in two apparently unrelated Northern European families (Dutch family 2; family 4).
- **Environmental risk factors:** none known.
- **Protective factors and gene–environment interactions:** none reported.
- **Plausible but unproven modifier:** factors that raise dNTP demand or block de novo synthesis. Hydroxyurea and gemcitabine directly inhibit RNR. This is an inference, not a documented interaction (see §5).

## 3. Phenotypes

The 5 recessive patients are 1a, 1b, proband 2, proband 2's brother, and proband 4. Clinical detail is from the JCI full text; proband 2's brother is described only as "similarly affected."

| Phenotype | Suggested HP term (verify) | Frequency | Onset and course |
|---|---|---|---|
| Ptosis | HP:0000508 Ptosis | 5/5 | Adult; progressive |
| External ophthalmoplegia / ophthalmoparesis | HP:0000590 Progressive external ophthalmoplegia; HP:0000602 Ophthalmoplegia | 5/5 | Adolescence (1a, age 17) to age 61 |
| Diplopia | HP:0000651 Diplopia | Probands 2 and 4 (and proband 3 in the dominant family) | Often the first symptom in late-onset cases |
| Myopathy / proximal limb weakness (trouble climbing stairs or standing; gait impairment) | HP:0003701 Proximal muscle weakness; HP:0003198 Myopathy | 1a, 2, 4 | Progressive. Proband 4 recalled weakness since childhood |
| Muscle atrophy | HP:0003202 Skeletal muscle atrophy | 1a | — |
| Nausea, vomiting, diarrhea; intestinal dysmotility | HP:0002018 Nausea; HP:0002013 Vomiting; HP:0002014 Diarrhea; HP:0002579 Gastrointestinal dysmotility | 1a, 1b | 1a: vomiting from age 7, diarrhea from age 14. The family 1 picture resembles MNGIE |
| Weight loss / cachexia | HP:0001824 Weight loss; HP:0004326 Cachexia | 1a (17 kg lost), 1b | — |
| Axonal sensorimotor neuropathy; areflexia | HP:0007141 Sensorimotor neuropathy (or the axonal term); HP:0001284 Areflexia | 1a (mild, confirmed by nerve conduction and EMG) | — |
| Raised CK (697 U/L in 1a) and raised AST/ALT (OMIM synopsis) | HP:0003236 Elevated circulating creatine kinase concentration; transaminase terms | 1a | — |
| COX-deficient fibers | HP:0003688 Cytochrome C oxidase-negative muscle fibers | 1a (50–60%), 4 | — |
| Ragged-red fibers | HP:0003200 Ragged-red muscle fibers | 1a (3–4%), 4 (30%) | — |
| Central nuclei, regenerating and necrotic fibers | Centrally nucleated fibers term | 1a | — |
| Multiple mtDNA deletions in muscle | HPO term to be identified | 4/4 biopsied recessive probands | — |
| Muscle mtDNA depletion (10–30% of control) | — | Proband 2 | — |
| Dysphagia | HP:0002015 Dysphagia | Listed in the MedGen/OMIM synopsis; in the paper it is clearly in proband 3 (dominant) | — |
| Sensorineural hearing loss | HP:0000407 Sensorineural hearing loss | Listed by MedGen; in the paper it is in proband 3 (dominant) | — |
| Gastroparesis, loss of ambulation, intellectual disability | — | Listed in the MedGen HPO annotation, but not found in the JCI text that was read | Treat as low-confidence until checked against the OMIM synopsis |

**Quality of life.** The main burdens are visual (diplopia, ptosis), mobility (proximal weakness, gait), and nutrition (cachexia in family 1). No validated quality-of-life instrument data exist.

## 4. Genetic and molecular information

**Gene.** RRM1, ribonucleotide reductase catalytic subunit M1.
- IDs: hgnc:10451; NCBI Gene 6240; UniProt P23921; Ensembl ENSG00000167325; OMIM 180410; 11p15.4 (HGNC REST).
- The protein is the large R1 subunit of class Ia RNR. It holds:
  - the catalytic site;
  - the allosteric specificity site (loop 2), which sets the dNTP balance;
  - the activity (ATP-cone) site.
- It pairs with RRM2 (in S phase) or with RRM2B/p53R2 (outside S phase and in post-mitotic tissues).

**Variants** (transcript NM_001033; protein NP_001024.1):

| Variant | Zygosity | Families | gnomAD | ClinVar (per GeneCards) | Structural effect |
|---|---|---|---|---|---|
| c.1142G>A p.(Arg381His) | Homozygous | Family 1: Saudi, consanguineous (1a, 1b) | Absent (v2.1.1) | Likely pathogenic | Breaks a hydrogen-bond network linking R381 to the catalytic-site "gating" residue R293. R293 swings away from GDP. TTP binding and dimer-interface contact are predicted to drop. |
| c.1141C>T p.(Arg381Cys) | Homozygous | Family 2: Dutch (proband + brother); Family 4 | 1 × 10⁻⁴ heterozygous; no homozygotes | Pathogenic | Hydrogen-bond network intact, but flexibility falls and inter-protomer buried surface area drops by about 100 Å². Predicted to impair dimerization. |
| c.1281C>A p.(Asn427Lys) | Heterozygous | Family 3: White British | Absent | — | In the catalytic site; N427 hydrogen-bonds the substrate ribose 2′/3′-OH. **Belongs to the dominant phenotype, not PEOB6.** |

- **Where R381 sits.** R381 lies near the specificity site, as "an extension of loop 1." It interacts with S260.
- **Functional effect.** Loss of function: RNR activity ([¹⁴C]CDP → dCDP) was reduced in patient fibroblasts, while RRM1 protein levels were normal. That means reduced catalytic function, not protein instability.
- **Variant class:** missense only. All variants are germline.
- **Modifier genes:** none known.
- **Epigenetics and chromosomal abnormalities:** none reported or relevant.

## 5. Environmental information

- No environmental, lifestyle or infectious causes are known.
- **Inferred pharmacological concern:** RNR inhibitors (hydroxyurea, gemcitabine, clofarabine, cladribine) act on RRM1. In theory they could worsen dNTP depletion in carriers or patients. This is not documented.

## 6. Mechanism and pathophysiology

**Causal chain:**

1. **Lesion.** Homozygous missense at RRM1 Arg381 (p.R381H or p.R381C) changes the local structure near loop 1, the specificity site and the dimer interface. This step is inferred from molecular dynamics simulations (computational evidence).
2. → **Reduced RNR catalytic activity.** Less ribonucleoside diphosphate (NDP) is turned into deoxyribonucleoside diphosphate (dNDP). This was shown in patient fibroblasts (in vitro).
3. → **Abnormal nucleotide pools.** NDPs are raised and mitochondrial dGTP and dTTP are lowered. Shown in fibroblasts: the pool changes were clearest in probands 2 and 3 and were not seen in 1a/1b.
4. → **More ribonucleotides built into mtDNA**, because the dNTP:rNTP ratio falls. Shown by alkaline hydrolysis and denaturing Southern blot.
5. → **Impaired mtDNA replication in cells that depend on de novo dNTP synthesis.** mtDNA depletion appears in proliferating fibroblasts, but not in quiescent ones, which rely on the salvage pathway. Expression of salvage-pathway genes was normal.
6. → **Stalled replication and faulty repair in post-mitotic muscle produce multiple mtDNA deletions.** This step is inferred by analogy with RRM2B, TK2 and POLG. Long-range PCR found no deletions in cultured fibroblasts; deletions were found only in muscle.
7. → **Clonal build-up of deleted mtDNA** gives mosaic respiratory chain deficiency: COX-negative and ragged-red fibers, and reduced activity of complex IV and complexes II+III.
8. → **Energy failure in high-demand, long-lived cells**, branching into three outcomes:
   - 8a. extraocular and levator muscles → ptosis and progressive external ophthalmoplegia;
   - 8b. limb skeletal muscle → proximal myopathy, atrophy, raised CK;
   - 8c. enteric smooth muscle or neurons, and peripheral nerve → GI dysmotility, cachexia, axonal neuropathy. This branch was seen only in family 1 (R381H) and is a mechanistic inference.

**Mechanism categories:**

- **Molecular pathway:** de novo dNTP synthesis (Reactome "Synthesis of dNTPs"; KEGG purine and pyrimidine metabolism).
- **Suggested GO terms:**
  - GO:0009263 deoxyribonucleotide biosynthetic process (DECREASED);
  - GO:0004748 ribonucleoside-diphosphate reductase activity, thioredoxin disulfide as acceptor (DECREASED);
  - GO:0000002 mitochondrial genome maintenance;
  - GO:0006264 mitochondrial DNA replication;
  - cellular component GO:0005971 ribonucleoside-diphosphate reductase complex; GO:0005829 cytosol; GO:0005739 mitochondrion (where the defect shows).
- **Cell types (CL):** skeletal muscle fiber (CL:0008002 or CL:0000188); extraocular muscle fibers; fibroblast (CL:0000057; the in vitro model); possibly enteric neurons or smooth muscle.
- **Immune involvement:** none.
- **Tissue damage:** respiratory chain failure, fiber necrosis and regeneration, atrophy.
- **Omics, single-cell, CRISPR screens:** none disease-specific. RRM1 is pan-essential in DepMap, which fits the total-knockout lethality below.
- **Context from mouse (PMID:20724444, Ylikallio 2010).** Overexpressing RNR subunits does not raise mtDNA copy number. Imbalanced dNTP pools from overexpressing two subunits caused progressive mtDNA depletion in muscle. This supports dNTP balance, not just quantity, as the critical variable.

## 7. Anatomical structures affected

- **Primary:**
  - extraocular muscles (UBERON:0001601 extra-ocular muscle);
  - levator palpebrae superioris / upper eyelid;
  - skeletal muscle (UBERON:0001134 skeletal muscle tissue).
- **Secondary:**
  - gastrointestinal tract (small intestine motility);
  - peripheral nerves (UBERON:0001021 nerve);
  - inner ear / cochlea (only in the dominant family).
- **Subcellular:** mitochondrion and mitochondrial nucleoid (GO:0042645).
- **Laterality:** bilateral, symmetric ptosis and ophthalmoplegia.

## 8. Temporal development

- **Onset:**
  - usually adulthood (early 40s to 61);
  - adolescence in family 1 (GI symptoms at 7, ophthalmoparesis at 17);
  - proband 4 reported subjective weakness since childhood.
- **Course:** insidious, slowly progressive, and lifelong. Diplopia → ptosis → complete ophthalmoplegia → limb weakness and gait difficulty.
- **Remission:** none.
- **Natural-history data:** none.

## 9. Inheritance and population

- **Inheritance:** autosomal recessive (HP:0000007).
- **Penetrance:** apparently complete in homozygotes; no heterozygous carrier was affected.
- **Expressivity:** variable. R381H (family 1) gives an earlier, more multisystem, MNGIE-like picture. R381C gives late-onset ocular myopathy.
- **Anticipation and germline mosaicism:** none.
- **Founder effect:** possible for R381C in Northern Europeans (two families). Not formally tested.
- **Consanguinity:** present in family 1.
- **Prevalence:** unknown. Ultra-rare, with 5 patients reported (Orphanet-style class "<1/1,000,000"; measure type CASES_IN_LITERATURE). Carrier frequency of R381C is about 1 in 10,000.
- **Sex:** both affected (3 men, including the brother; 2 women).
- **Geography:** Saudi Arabia; the Netherlands; family 4 of unstated ancestry.

## 10. Diagnostics

**Clinical and laboratory:**
- CK, which may be raised.
- Lactate.
- Muscle biopsy with COX/SDH histochemistry (COX-negative and ragged-red fibers).
- Respiratory chain enzyme assays.
- **Long-range PCR or Southern blot of muscle mtDNA for multiple deletions:** the hallmark.
- qPCR for mtDNA copy number.

**Electrophysiology:** nerve conduction and EMG (axonal sensorimotor neuropathy, myopathic EMG).

**Genetic testing:**
- Exome or genome sequencing, or a nuclear mtDNA-maintenance gene panel.
- RRM1 is on PanelApp Australia's mitochondrial disease panel (#203).
- Analyse a blood sample for nuclear genes. Muscle mtDNA analysis shows the deletions, but blood mtDNA testing will be normal.

**Supporting functional assays (research):**
- RNR activity in fibroblasts;
- dNTP pools;
- mtDNA depletion in proliferating, but not quiescent, fibroblasts;
- mtDNA ribonucleotide content.

**Differential diagnosis** (other nuclear causes of PEO with multiple mtDNA deletions):

| Gene | Disease | Distinguishing note |
|---|---|---|
| POLG | PEOA1 / PEOB1 | Commonest cause |
| TWNK | PEOA3 | — |
| SLC25A4 | PEOA2 | — |
| RRM2B | PEOA5 / PEOB5 | Same enzyme complex as RRM1 |
| TK2 | PEOB3 | Has a deoxynucleoside therapy |
| DGUOK | PEOB4 | — |
| TYMP | MNGIE | Closest mimic of family 1. Plasma thymidine and deoxyuridine are raised in MNGIE and not expected in RRM1 disease |
| POLG2, OPA1, MGME1, DNA2, others | — | — |
| — | Myasthenia gravis; oculopharyngeal muscular dystrophy (PABPN1) | Non-mitochondrial mimics |

**Screening:** no newborn or population screening. Carrier and cascade testing is possible within families.

## 11. Outcome and prognosis

- No survival data exist. Patients survive into their 30s–60s with progressive disability.
- Cachexia and GI dysmotility (family 1) are the probable life-limiting complications.
- Other complications: aspiration from dysphagia, falls, and exposure keratopathy from ptosis.
- No prognostic biomarkers are known.

## 12. Treatment

No disease-specific therapy has been reported. Management is supportive, following general guidance for primary mitochondrial myopathy.

| Intervention | Suggested NCIT term (verify) | Notes |
|---|---|---|
| Ptosis surgery (frontalis sling or levator resection) | NCIT:C15329 Surgical Procedure (no specific term identified) | Avoid overcorrection because of poor eye closure |
| Prisms for diplopia | Supportive care | — |
| Physical therapy / exercise | NCIT:C15302 Physical Therapy | Endurance training is used in mitochondrial myopathy generally |
| Nutritional support / enteral feeding for cachexia | NCIT:C15433 Nutritional Support | Relevant to the family 1 phenotype |
| Genetic counseling | NCIT:C15240 Genetic Counseling | 25% recurrence risk for siblings of a patient |
| Supportive care | NCIT:C15747 Supportive Care | — |

- **Experimental / theoretical: deoxynucleoside supplementation.** dC/dT therapy is effective in TK2 deficiency (doxecitine/doxribtimine). It might bypass the de novo block through salvage enzymes, which stay intact in RRM1 patient cells. This is a hypothesis that has not been tested; the search found no trials or case reports.
- **Clinical trials:** none for RRM1 (ClinicalTrials.gov search for "RRM1 ophthalmoplegia" returns none).
- **Pharmacogenomics:** avoid RNR inhibitors where possible. This is inferred, not established.

## 13. Prevention

- **Primary prevention:** carrier testing in at-risk relatives, especially in the consanguineous family. Prenatal or preimplantation diagnosis once both variants in a family are known.
- **Tertiary prevention:**
  - watch for dysphagia, nutrition, cardiac and respiratory status (generic mitochondrial surveillance);
  - corneal protection after ptosis surgery.
- **Vaccination, public health and environmental measures:** not applicable.

## 14. Other species and natural disease

- **OMIA:** no naturally occurring RRM1 disease is known in animals.
- **Orthologs:**
  - mouse Rrm1 (MGI:98180; NCBITaxon:10090);
  - zebrafish rrm1 (ZFIN:ZDB-GENE-990415-247; NCBITaxon:7955);
  - Drosophila RnrL;
  - yeast RNR1 and RNR3 (NCBITaxon:4932).
- RRM1 is highly conserved: the class Ia R1 catalytic machinery is shared from *E. coli* NrdA to humans.
- **Zoonotic relevance:** none.

## 15. Model organisms

| Model | Phenotype | Fit to human disease |
|---|---|---|
| Mouse Rrm1 knockout (MGI / IMPC) | Embryonic lethal before E3.5 / pre-implantation, complete penetrance | Shows the gene is essential. Fails to recapitulate the disease: total loss is lethal, whereas patients carry hypomorphic missense alleles |
| Mouse Rrm1-W688G knock-in (Specks et al., *Mol Cell Biol* 2015) | Loses RRM2 binding; embryonic lethal | Fails to recapitulate; mechanistic only |
| Transgenic Rrm1 / Rrm2 / p53R2 overexpressing mice (PMID:20724444) | No rise in mtDNA copy number. dNTP imbalance → progressive muscle mtDNA depletion | Supports dNTP imbalance as the driver of mtDNA loss; partial mechanistic model |
| Patient primary skin fibroblasts (PMID:35617047) | Reduced RNR activity, abnormal NDP/dNTP pools, mtDNA depletion only when cycling, mtDNA ribonucleotide incorporation, complex II+III defect | Best existing model. Lacks deletions and post-mitotic muscle biology |

- **Main gap:** no knock-in mouse or zebrafish model carries R381H or R381C. A homozygous R381 knock-in, or patient iPSC-derived myotubes, would be the natural next model.
- **Resources:** MGI, IMPC, ZFIN, Cellosaurus (no patient lines deposited).

---

## Knowledge gaps

1. Only 5 patients are known; the phenotype spectrum and natural history are undefined.
2. How depletion in proliferating cells leads to deletions in post-mitotic muscle has not been demonstrated (§6, step 6).
3. Why only family 1 has GI involvement (R381H versus R381C, or background) is unexplained.
4. Whether deoxynucleoside therapy rescues the defect, in fibroblasts or in patients, has not been tested.
5. The source of several MedGen/OMIM-listed features (intellectual disability, gastroparesis, loss of ambulation) is unclear; they may belong to the dominant family.

## Sources

- Shintaku J, Pernice WM, Eyaid W, … Taylor RW, Hirano M. "RRM1 variants cause a mitochondrial DNA maintenance disorder via impaired de novo nucleotide synthesis." *J Clin Invest*. 2022 Jul 1;132(13):e145660. PMID:35617047; PMC9246377. [JCI](https://www.jci.org/articles/view/145660) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/35617047/) · [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9246377/)
- Ylikallio E, et al. "Ribonucleotide reductase is not limiting for mitochondrial DNA copy number in mice." *Nucleic Acids Res*. 2010;38(22). PMID:20724444.
- [MedGen C5882731 / UID 1847098 (PEOB6)](https://www.ncbi.nlm.nih.gov/medgen/1847098)
- [OMIM Clinical Synopsis #620647](https://www.omim.org/clinicalSynopsis/620647?highlight=None) (blocked by HTTP 403; content seen through search snippets only)
- [OMIM *180410 RRM1](https://omim.org/entry/180410)
- [HGNC REST: RRM1](https://rest.genenames.org/fetch/symbol/RRM1)
- [KEGG H01395](https://www.kegg.jp/entry/H01395)
- [PanelApp Australia, panel 203, RRM1](https://panelapp-aus.org/panels/203/gene/RRM1/)
- [GeneCards RRM1](https://www.genecards.org/cgi-bin/carddisp.pl?gene=RRM1)
- [NIH GTR RRM1](https://www.ncbi.nlm.nih.gov/gtr/genes/6240/)
- [MGI Rrm1](https://www.informatics.jax.org/marker/MGI:98180) · [IMPC Rrm1](https://www.mousephenotype.org/data/genes/MGI:98180) · [Alliance](https://alliancegenome.org/gene/MGI:98180)
- [ZFIN rrm1](https://franklin.zfin.org/ZDB-GENE-990415-247)
- Specks J, et al. *Mol Cell Biol* 2015 (Rrm1-W688G knock-in; PMID not retrieved)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 3 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 3 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 46 |
| Resolved | 43 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 4 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0957993` (2 mentions) - the report calls it "MONDO"; MONDO calls it **progressive external ophthalmoplegia with mitochondrial dna deletions, autosomal recessive 6**
- `NCBITaxon:4932` (1 mention) - the report calls it "yeast RNR1 and RNR3"; NCBITaxon calls it **Saccharomyces cerevisiae**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0000002` (obsolete mitochondrial genome maintenance) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0042645` (1 mention) - the report calls it "Subcellular:** mitochondrion and mitochondrial nucleoid"; GO calls it **mitochondrial nucleoid**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.