---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-22T14:38:41.717214'
end_time: '2026-10-22T14:42:12.564310'
duration_seconds: 210.85
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Spermatogenic Failure 32
  mondo_id: MONDO:0020855
  category: Mendelian
  causal_genes: SOHLH1
  omim_id: not recorded
  synonyms: not recorded
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: low
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 51
reference_validation:
  total_references: 18
  verified: 18
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 18
  on_topic: 7
  validator_version: 0.3.0
term_validation:
  total_terms: 37
  verified: 31
  not_found: 0
  obsolete: 1
  unverifiable: 5
  confabulation_rate: 0.0
  labels_checked: 7
  labels_matching: 4
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0020855
    reported_labels:
    - MONDO
    ontology_label: spermatogenic failure 32
  labels_variant: 2
  obsolete_terms:
  - term_id: GO:0007126
    ontology_label: GO_0007126
    replaced_by: GO:0051321
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
- **Disease Name:** Spermatogenic Failure 32
- **MONDO ID:** MONDO:0020855 (if available)
- **Causal gene(s):** SOHLH1
- **OMIM:** not recorded
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Spermatogenic Failure 32** covering all of the
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

# Spermatogenic Failure 32: disease-characteristics research report

**Spermatogenic failure 32 (SPGF32; MONDO:0020855; OMIM 618115) is a rare Mendelian male-infertility disorder associated with germline variation in the causal gene *SOHLH1*.** Its canonical description is nonobstructive azoospermia (NOA) caused by severe failure of germ-cell development, with reported testicular germ-cell aplasia/Sertoli-cell-only histology. The evidence base is unusually small and centers on one recurrent splice-acceptor variant, **NM_001101677.2:c.346-1G>A (rs140132974)**. Importantly, later human data and population frequency evidence challenge the original autosomal-dominant/de-novo interpretation: homozygosity can cause severe oligozoospermia, whereas heterozygotes may have azoospermia, oligoasthenoteratozoospermia, isolated teratozoospermia, or no recognized phenotype. Thus, the gene–disease association is credible, but penetrance, inheritance, and the pathogenicity of this particular allele remain incompletely resolved. [31][61][109]

**Evidence cutoff:** October 22, 2026. Disease-specific human literature through 2024 remained sparse; the most relevant 2023 publication is an expanded mouse knockout phenotyping study. A small 2025 human study is noted only where it materially updates the phenotype.

---

## 1. Disease information

### 1.1 Definition and scope

SPGF32 is a genetic form of **primary testicular spermatogenic failure**. The defining manifestation in the original disease record is male infertility from NOA, not obstruction of an otherwise normally functioning reproductive tract. The original patients had absence of spermatogenic cells and a Sertoli-cell-only pattern on biopsy. [24]

The record is an **aggregated disease-level construct**, assembled principally from OMIM, MedGen/MONDO, ClinVar and published cohorts—not an individual EHR phenotype. Individual-patient observations underpinning it include two Korean men in the 2010 discovery study, Japanese replication cases, and a later Chinese severe-oligozoospermia case. [114]

### 1.2 Identifiers and names

| Identifier system | Identifier/name | Qualification |
|---|---|---|
| MONDO | **MONDO:0020855** | Requested target identifier |
| OMIM disease | **618115**, Spermatogenic failure 32 | Contrary to the template’s “not recorded,” an OMIM disease entry exists |
| OMIM gene | **610224**, *SOHLH1* | Gene entry, not the disease entry |
| MedGen | UID **1648444**; Concept ID **C4748253** | Disease concept |
| Orphanet | No dedicated SPGF32-specific ORPHAcode identified | ORPHA:399771 is the broader NOA phenotype, not necessarily SPGF32 |
| MeSH | No SPGF32-specific heading | Indexed under terms such as Azoospermia/genetics, Male Infertility, and Basic Helix-Loop-Helix Transcription Factors |
| ICD-10-CM | No gene-specific code; **N46.01** is commonly used for organic azoospermia | Coding is phenotype-level |
| ICD-11 | No SPGF32-specific code identified | Use the appropriate male-infertility/azoospermia category locally |
| Synonyms | **Spermatogenic failure 32; SPGF32** | Canonical disease synonyms |
| Broader descriptive names | *SOHLH1*-related spermatogenic failure; *SOHLH1*-associated male infertility; nonobstructive azoospermia due to *SOHLH1* deficiency | Useful search terms, not necessarily official synonyms |

MedGen confirms MONDO:0020855, OMIM 618115, *SOHLH1* at 9q34.3, and the two canonical synonyms. [31]

---

## 2. Etiology

### 2.1 Primary causal factor

The established initiating factor is a **germline defect affecting *SOHLH1***, which encodes a germ-cell-specific basic helix-loop-helix transcription regulator. The best studied allele, c.346-1G>A, disrupts a splice acceptor, activates a cryptic splice site in exon 4, deletes 18 coding nucleotides, damages the bHLH domain, and reduces transcriptional activation of the *KIT* promoter. [61]

The discovery abstract’s key conclusion was:

> “Our findings indicate that a splice-acceptor site mutation that probably causes a nonfunctional SOHLH1 protein results in nonobstructive azoospermia by the lack of normal spermatogenesis.”  
> — Choi et al., *Human Mutation*, July 2010, PMID: **20506135** [61]

### 2.2 Risk factors and evidence strength

| Factor | Disease-specific evidence | Interpretation |
|---|---|---|
| *SOHLH1* c.346-1G>A, homozygous | One Chinese patient with severe oligozoospermia, sharply reduced/disorganized testicular germ cells and reduced SOHLH1 protein | Stronger evidence for a recessive quantitative spermatogenesis defect, but still a single incompletely segregated case |
| c.346-1G>A, heterozygous | Two Korean NOA cases, two Japanese NOA cases, three Chinese teratozoospermia cases, and two 2025 severe oligoasthenospermia cases | Phenotypically heterogeneous; dominant causality and penetrance remain uncertain |
| Other heterozygous missense variants | c.91T>C/p.Arg37Gln and c.529C>A/p.Pro269Ser did not significantly impair *KIT* transactivation | Not established as causal |
| Male sex | Required for the SPGF32 phenotype as defined | Female biallelic loss of function is associated instead with ovarian dysgenesis 5 |
| Consanguinity/family history | Plausibly increases risk for biallelic disease | No robust SPGF32 prevalence estimate or established founder pedigree |
| Environmental exposures | No exposure has been shown to specifically cause or modify *SOHLH1*-SPGF32 | General NOA risks should not be entered as causes of this Mendelian subtype |

The 2022 human study summarized its revised inheritance interpretation as:

> “the heterozygous mutation of c.346-1G > A in *SOHLH1* is responsible for teratozoospermia, and this homozygous mutation in *SOHLH1* impairs spermatogenesis and further leads to the reduced sperm count.”  
> — Liu et al., *Human Molecular Genetics*, March 31, 2022, PMID: **34448846** [62]

That conclusion is not definitive: the homozygous patient’s father was non-carrier and maternal DNA was unavailable, so parentage, phase and full segregation were not established. [62]

### 2.3 Protective factors and gene–environment interaction

No disease-specific protective allele, modifier gene, diet, medication, or behavioral intervention has been demonstrated. Avoiding gonadotoxic exposures may preserve residual spermatogenesis in male infertility generally, but it cannot correct congenital loss of SOHLH1 transcriptional function.

No controlled human gene–environment interaction study exists for SPGF32. A reasonable but **unproven** model is that fever, testicular heat, chemotherapy, radiation, smoking or other oxidative insults could further reduce an already limited germ-cell reserve.

---

## 3. Phenotypes

Because only a handful of molecularly characterized patients exist, percentages would be misleading. Frequencies below are qualitative and evidence-specific rather than population estimates.

| Phenotype | Type and characteristics | Onset/course | Suggested HPO term | Evidence |
|---|---|---|---|---|
| Male infertility | Clinical outcome; typically recognized after unsuccessful conception | Developmental lesion, usually clinically recognized in adulthood; chronic | **HP:0003251 Male infertility** | Defining feature of SPGF32 [24] |
| Nonobstructive azoospermia | Laboratory/clinical sign: no sperm in centrifuged ejaculate because of impaired production | Apparent after puberty; stable unless rare focal spermatogenesis is found | **HP:0011961 Nonobstructive azoospermia** | Canonical phenotype in Korean/Japanese cases [91][114] |
| Sertoli-cell-only phenotype/germ-cell aplasia | Histopathology: seminiferous tubules lined by Sertoli cells without spermatogenic cells | Developmental, severe, generally persistent | **HP:0034299 Sertoli cell-only phenotype** | Original disease description [93] |
| Severe oligozoospermia | Very low sperm concentration | Adult recognition; likely chronic | **HP:0000798 Oligospermia** | One homozygous c.346-1G>A patient had 4.3 million/mL [62] |
| Asthenozoospermia | Reduced motility | Adult laboratory finding | **HP:0012206 Asthenozoospermia** | Homozygous case 15% motility; heterozygotes 3–28% [62] |
| Teratozoospermia | Abnormal sperm morphology | Adult laboratory finding | **HP:0012864 Abnormal sperm morphology** | Heterozygotes had 0.9–2.5% normal forms [62] |
| Abnormal sperm head | Round, double, tapered, pyriform, irregular or vacuolated heads | Stable laboratory phenotype | **HP:0012865 Abnormal sperm head morphology** | SEM/TEM evidence [62] |
| Abnormal sperm flagellum | Short, bent or coiled tails and irregular axonemal microtubules | Stable laboratory phenotype | **HP:0012867 Abnormal sperm flagellum morphology** | SEM/TEM evidence [62] |
| Reduced germ-cell number/disorganization | Biopsy abnormality | Developmental/chronic | HP:0034299 or a local histopathology term | Homozygous case [62] |
| Primary infertility | Reproductive-history finding | Adult recognition | **HP:0000789 Infertility** | Reported infertility duration 3–8 years in treated cases [62] |

### Quality-of-life consequences

No SPGF32-specific patient-reported outcome study exists. Male infertility generally is associated with psychological distress, relationship burden, invasive fertility procedures and uncertainty about biological parenthood. A 2023 meta-analysis estimated depression in infertile men at **18.3%**, while a 2024 systematic review found reported quality-of-life scores ranging from **55.15 ± 13.52 to 91.45 ± 13.66**, most often 70–80%. These figures should be annotated as indirect male-infertility evidence, not SPGF32-specific estimates. [124][133]

---

## 4. Genetic and molecular information

### 4.1 Gene annotation

| Field | Value |
|---|---|
| Gene | ***SOHLH1*** |
| Full name | Spermatogenesis and oogenesis specific basic helix-loop-helix 1 |
| HGNC | **HGNC:27845** |
| NCBI Gene | **402381** |
| Ensembl | **ENSG00000165643** |
| OMIM gene | **610224** |
| UniProt | **Q5JUK2** |
| Locus | **9q34.3** |
| GRCh38 interval | Approximately chr9:135.69–135.70 Mb |
| Protein class | Germ-cell-enriched bHLH DNA-binding transcription regulator |
| Common gene aliases | SPATA27, TEB2, NOHLH, bHLHe80, C9orf157 |

NCBI/HGNC-linked resources identify the gene as protein coding and provide HGNC:27845, NCBI Gene 402381 and ENSG00000165643. [2]

### 4.2 Reported variants

| Variant | Zygosity/phenotype | Functional evidence | Current interpretation |
|---|---|---|---|
| **NM_001101677.2:c.346-1G>A**, rs140132974; ClinVar VCV000560884.11 | Heterozygous NOA, teratozoospermia or severe oligoasthenospermia; homozygous severe oligozoospermia; population homozygotes also reported | Cryptic splicing/18-bp in-frame deletion, truncated bHLH domain, <50% wild-type transcriptional activity, reduced *KIT* promoter activation | ClinVar aggregate: **conflicting**—1 likely pathogenic, 2 VUS, 1 benign among criteria-bearing submissions; older disease-specific submissions call it pathogenic |
| c.91T>C, p.Arg37Gln | Reported in NOA cohort | No significant reduction of *KIT* transactivation | Not established as pathogenic |
| c.529C>A, p.Pro269Ser | Reported in NOA cohort | No significant reduction of *KIT* transactivation | Not established as pathogenic |

The recurrent allele has a ClinVar global minor allele frequency around **0.003**, with reported database frequencies from 0.00031 to 0.00329 and a Finnish gnomAD frequency around 0.015; gnomAD homozygotes have been reported. Those observations are difficult to reconcile with a fully penetrant dominant cause of severe NOA. [107]

### 4.3 Variant origin and functional class

- Reported variants are **germline**, not somatic.
- The likely molecular mechanism is **loss or marked reduction of transcription-factor function**.
- The splice allele is not a classic whole-protein null: it creates an in-frame deletion that impairs the bHLH region and reduces, rather than necessarily abolishes, transactivation.
- There is no convincing evidence for gain of function or dominant-negative action.
- Large causal deletions, translocations, aneuploidies or repeat expansions specifically defining SPGF32 have not been established.
- No validated modifier gene has been identified; *SOHLH2* is a biologically plausible compensatory partner but is not a proven human clinical modifier.

### 4.4 Epigenetics

SOHLH1 participates in a transcriptional differentiation network, but no reproducible SPGF32-specific DNA-methylation, histone-mark or chromatin signature has been established in patients. Epigenetic assays are therefore research tools, not diagnostic biomarkers.

---

## 5. Environmental and lifestyle information

| Category | SPGF32-specific conclusion |
|---|---|
| Toxins, radiation, pollution | No evidence that they initiate genetically defined SPGF32; they are independent/general causes of impaired spermatogenesis |
| Heat and occupational exposure | No demonstrated interaction with *SOHLH1* genotype |
| Smoking, alcohol, obesity, diet or exercise | No genotype-specific association or treatment effect established |
| Medications | Testosterone/anabolic steroids and gonadotoxic drugs can suppress spermatogenesis generally, potentially compounding infertility, but do not define SPGF32 |
| Infectious agents | No bacterium, virus, fungus or parasite causes SPGF32 |
| Immunity/inflammation | Not a defining human mechanism; mouse knockout work detected systemic immune changes, requiring caution before extrapolation |

The environmental distinction is clinically important: finding a *SOHLH1* variant should not prevent assessment for reversible endocrine, toxic, infectious or obstructive contributors.

---

## 6. Mechanism and pathophysiology

### 6.1 Ordered causal chain

1. **A damaging germline *SOHLH1* allele leads to abnormal SOHLH1 RNA splicing or reduced functional SOHLH1 protein.**
2. **Loss of an intact bHLH DNA-binding/dimerization domain leads to reduced transcriptional regulation of spermatogonial differentiation genes.**
3. **Reduced SOHLH1 activity leads to failure to suppress stem-cell-maintenance programs and failure to activate differentiation programs including *KIT*, *SOX3*, *NGN3/NEUROG3*, *LHX8* and meiotic genes.**
4. **Failure of that transcriptional switch leads to impaired transition of undifferentiated type-A spermatogonia into differentiating KIT-positive spermatogonia and spermatocytes.**
5. **The differentiation block leads to depletion, disorganization and/or apoptosis of developing germ cells; effects on apoptosis and meiotic synaptonemal-complex formation are principally demonstrated in mice and inferred in humans.**
6. **Germ-cell loss leads to hypospermatogenesis, severe oligozoospermia, maturation failure or, at the extreme, Sertoli-cell-only tubules.**
7. **Reduced or absent mature sperm leads to teratozoospermia/oligoasthenozoospermia or nonobstructive azoospermia.**
8. **The semen phenotype results in subfertility or male infertility.**

### 6.2 Mechanistic detail

SOHLH1 and SOHLH2 are germ-cell-specific bHLH factors that form homo-/heterodimeric regulatory complexes. In mouse spermatogonia they directly regulate *Gfra1*, *Sox3*, *Sohlh1*, *Sohlh2* and *Kit*, suppressing spermatogonial stem-cell maintenance while activating differentiation. [51]

The direct *KIT* link is especially relevant to the human splice allele. Deletion of either factor in male mice causes loss of KIT-positive spermatogonia, and promoter studies show that SOHLH1/SOHLH2 stimulate *Kit* transcription during postnatal spermatogonial differentiation. [50]

The landmark mouse abstract states:

> “Loss of Sohlh1 causes infertility by disrupting spermatogonial differentiation into spermatocytes.”  
> — Ballow et al., *Developmental Biology*, June 2006, PMID: **16564520** [47]

In the original human minigene assay, c.346-1G>A produced a shortened transcript and impaired *KIT*-promoter activation, whereas p.Arg37Gln and p.Pro269Ser did not. This is direct in-vitro evidence for the splice defect but not proof of its penetrance in vivo. [61]

### 6.3 Pathways, processes and cell types

| Mechanistic component | Annotation suggestions | Evidence level |
|---|---|---|
| Spermatogonial differentiation | GO:0048515 spermatid differentiation; GO:0007283 spermatogenesis; use the current GO term for spermatogonial differentiation where available | Strong mouse, supportive human |
| DNA-binding transcription regulation | GO:0003700 DNA-binding transcription factor activity; GO:0006355 regulation of DNA-templated transcription | Protein/function evidence |
| KIT signaling | GO:0007169 transmembrane receptor protein tyrosine kinase signaling; KIT receptor pathway | Mouse and in-vitro human |
| Germ-cell development | GO:0007281 germ-cell development | Strong mouse |
| Meiotic progression/synaptonemal complex | GO:0007126 meiotic nuclear division; GO:0000795 synaptonemal complex | Primarily mouse |
| Apoptosis following developmental failure | GO:0006915 apoptotic process | Model evidence; human inference |
| Spermatogonium | **CL:0000020** or the current more specific spermatogonial subtype | Primary affected cell |
| Spermatocyte | **CL:0000017** | Downstream depleted/arrested cell |
| Spermatid | **CL:0000018** | Reduced downstream product |
| Spermatozoon | **CL:0000019** | Absent or abnormal mature cell |
| Sertoli cell | **CL:0000216** | Preserved support cell in Sertoli-cell-only histology [92] |

### 6.4 Metabolic, immune and tissue-damage findings

No characteristic human metabolomic, lipidomic, inflammatory or immune signature is known. The 2023 knockout study detected sex-specific metabolite changes and altered immune-cell profiles, behavior and cognition in mice, despite the apparently gonad-restricted infertility phenotype. These are hypothesis-generating model findings, not established manifestations of human SPGF32. [16]

### 6.5 Molecular profiling and advanced technologies

- **Transcriptomics:** mouse knockout/target studies show decreased differentiation genes and persistence of stem-cell programs; GEO **GSE24816** contains relevant Sohlh1/Sohlh2 germ-cell transcription data. [149]
- **Single-cell analysis:** single-cell RNA sequencing has helped place *Sohlh1* in differentiating spermatogonia and identify upstream regulators such as Dec2, but no patient-specific SPGF32 single-cell atlas has been published. [59]
- **Proteomics/metabolomics:** no validated human diagnostic profile.
- **Spatial transcriptomics/multi-omics:** no disease-specific clinical implementation.
- **CRISPR/RNAi screens:** no clinically actionable SPGF32 result.
- **Organoids/iPSCs:** no validated patient-derived diagnostic or therapeutic platform.

---

## 7. Anatomical structures affected

| Scale | Structure | Suggested ontology | Consequence |
|---|---|---|---|
| Organ | Testis | **UBERON:0000473** | Primary and apparently direct organ involvement |
| Tissue | Seminiferous tubule | **UBERON:0001343** | Germ-cell depletion/Sertoli-cell-only pattern |
| Compartment | Seminiferous epithelium | Current UBERON seminiferous epithelium term | Failed germ-cell differentiation |
| Cell population | Spermatogonia | CL spermatogonium terms | Most upstream affected population |
| Cell population | Spermatocytes and spermatids | CL:0000017; CL:0000018 | Reduced/absent downstream stages |
| Mature cell | Spermatozoa | CL:0000019 | Absent, few, immotile or malformed |
| Supporting cell | Sertoli cells | CL:0000216 | Retained in canonical biopsy pattern |
| Subcellular | Nucleus/chromatin | GO:0005634 nucleus; GO:0000785 chromatin | Site of SOHLH1 transcriptional action |
| Subcellular | bHLH transcription complex | GO:0005667 transcription regulator complex, where appropriate | Impaired DNA binding/dimerization |
| Sperm-specific structures | Nucleus, mitochondria, axoneme, flagellum | GO:0036126 sperm flagellum; GO:0005930 axoneme | Abnormal in heterozygous patients’ sperm |

The process is expected to affect both testes because it is a constitutional germline disorder; unilateral disease is not characteristic. No reproducible secondary-organ involvement has been documented in human males.

---

## 8. Temporal development

- **Biological onset:** developmental, during establishment and postnatal differentiation of the male germ line.
- **Clinical onset:** usually post-pubertal/adult, when semen is assessed because of infertility.
- **Pattern:** insidious and chronic rather than acute or episodic.
- **Course:** generally stable infertility; sperm count may vary between analyses, particularly with severe oligo-/cryptozoospermia.
- **Remission:** spontaneous restoration of a normal sperm output has not been documented.
- **Critical window:** germ-cell differentiation before and after puberty. In adulthood, the main opportunity is identification and cryopreservation of rare ejaculated or surgically retrieved sperm—not restoration of the missing developmental transcription program.
- **Stages:** a formal SPGF32 staging system does not exist. Phenotypic severity can be described as abnormal morphology → oligoasthenoteratozoospermia → severe oligo-/cryptozoospermia → NOA/Sertoli-cell-only histology.

---

## 9. Inheritance and population

### 9.1 Inheritance

GenCC lists a **strong** *SOHLH1*–SPGF32 association and its submitted disease record labels the mode autosomal dominant. [106][32] Nevertheless, current variant-level evidence supports a more cautious entry:

> **Inheritance: unresolved/possibly semidominant or dosage-sensitive; autosomal-recessive loss of function is strongly plausible, while heterozygous c.346-1G>A may confer variably penetrant sperm abnormalities.**

Reasons for caution include:

1. the original heterozygous NOA cases;
2. later heterozygous carriers with normal sperm concentration but abnormal morphology;
3. a homozygous patient with severe quantitative failure;
4. population homozygotes and a relatively high allele frequency;
5. ClinVar’s current conflicting classification. [107]

Penetrance is therefore **incomplete or unknown**, expressivity is clearly variable, and anticipation has not been reported. Germline mosaicism remains theoretically possible but unreported. No robust founder effect or carrier frequency has been established.

### 9.2 Epidemiology and demographics

| Measure | Best available conclusion |
|---|---|
| SPGF32 prevalence | Unknown; no registry-derived cases-per-100,000 estimate |
| SPGF32 incidence | Unknown |
| Azoospermia prevalence | Approximately 1% of men and 10–15% of infertile men, indirect context only [123] |
| NOA fraction | Roughly 60–75% of azoospermia in general series, not SPGF32-specific [130] |
| Discovery cohort yield | 2 heterozygous c.346-1G>A carriers among 96 Korean NOA patients (~2.1%) |
| Japanese replication | 2 carriers among 40 idiopathic NOA patients (5%), but panel/cohort ascertainment was limited [65] |
| Sex ratio | By disease definition, affected individuals are 46,XY males; female biallelic disease is classified separately as ovarian dysgenesis 5 |
| Geographic evidence | Cases reported mainly from Korea, Japan and China; this likely reflects study ascertainment, not proven regional restriction |
| Age distribution | Adult men evaluated for infertility; no childhood clinical series |

The c.346-1G>A population frequency varies by ancestry and may be particularly high in Finns, arguing against a simple fully penetrant dominant model. [107]

---

## 10. Diagnostics

### 10.1 Clinical diagnostic workflow

1. **Confirm azoospermia or quantify severe oligozoospermia** with at least two semen analyses using WHO-standard methods and examination of the centrifuged pellet. EAU guidance defines NOA by no sperm after centrifugation and recommends confirmation in two consecutive samples. [85]
2. **Differentiate NOA from obstruction** using history, physical examination, semen volume and pH, testicular size, and serum FSH; AUA/ASRM recommends this initial combination. [77]
3. **Hormonal assessment:** FSH, LH and morning total testosterone; add prolactin/estradiol when indicated.
4. **Scrotal examination and ultrasound** to assess testicular volume, varicocele or masses; ultrasound is supportive, not diagnostic of SPGF32.
5. **First-tier standard genetics for severe spermatogenic failure:** karyotype and Y-chromosome AZF deletion testing according to sperm-count and guideline thresholds.
6. **Sequence-based testing:** use a validated NOA/severe-oligozoospermia panel or exome/genome analysis that includes *SOHLH1* and other established spermatogenic-failure genes.
7. **Confirm and phase variants** by Sanger or equivalent testing and test parents/siblings where available.
8. **Interpret c.346-1G>A cautiously**, explicitly acknowledging ClinVar conflict and population homozygotes.
9. **Testicular tissue evaluation** should generally accompany therapeutic sperm retrieval rather than be performed solely as a diagnostic biopsy; AUA/ASRM advises against routine diagnostic biopsy to distinguish obstruction from NOA. [76]

### 10.2 Genetic testing modalities

| Test | Utility in suspected SPGF32 |
|---|---|
| Targeted *SOHLH1* sequencing | Appropriate when phenotype/family variant strongly points to *SOHLH1*; include splice boundaries and deletion/duplication analysis |
| Multigene NOA panel | Usually preferable because SPGF32 is phenotypically indistinguishable from many other genetic NOA disorders |
| WES | Useful for coding/splice variants and novel differential diagnoses; identified the Chinese cases |
| WGS | Potentially detects deep-intronic, regulatory and structural variants missed by WES; clinical yield specific to SPGF32 is unknown |
| RNA sequencing | May demonstrate abnormal splicing if a suitable expressing tissue is available; blood expression may be inadequate |
| CMA | Low yield for an isolated single-gene suspicion but can detect pathogenic copy-number changes |
| Karyotype | Essential differential testing for Klinefelter syndrome and structural chromosome abnormalities |
| Y-microdeletion testing | Essential differential testing in severe oligozoospermia/NOA under guideline criteria |
| FISH | Not routine for diagnosing SPGF32 |
| mtDNA/repeat-expansion testing | Not routinely indicated |
| Prenatal/PGT-M testing | Technically possible only after a familial variant has been convincingly classified |

### 10.3 Pathology and biomarkers

The characteristic reported pathology is Sertoli-cell-only seminiferous tubules with absent germ cells. Other possible SOHLH1-associated patterns include sharply reduced and disorganized germ-cell stages. There is no validated serum protein, metabolite or imaging biomarker specific to SPGF32.

### 10.4 Differential diagnosis

| Differential | Distinguishing evaluation |
|---|---|
| Obstructive azoospermia | Normal spermatogenesis/testicular volume and often normal FSH; low-volume acidic semen in distal obstruction |
| Klinefelter syndrome | 47,XXY karyotype, small firm testes, hypergonadotropic profile |
| Y-chromosome AZFa/AZFb/AZFc deletions | Targeted Y-microdeletion assay; complete AZFa/AZFb predicts essentially no retrieval |
| Hypogonadotropic hypogonadism | Low/inappropriately normal FSH/LH and low testosterone; potentially treatable |
| Other monogenic NOA | Panel/WES genes including *TEX11, TEX14, MEIOB, STAG3, SYCE1, M1AP, DMRT1* and others |
| Gonadotoxic exposure, cryptorchidism, torsion or infection | History and examination |
| Oligo-/teratozoospermia without monogenic disease | Repeat semen analysis and broader etiologic assessment |

### 10.5 Screening

There is no newborn or population screening. Appropriate strategies are **cascade testing of adult relatives**, reproductive counseling, and carrier/partner testing when a likely causal familial allele is found. Because c.346-1G>A classification is contested, irreversible reproductive decisions should not rely on that allele without expert re-evaluation.

---

## 11. Outcome and prognosis

- **Survival/life expectancy:** no evidence of reduced survival or disease-specific mortality in humans.
- **Primary morbidity:** infertility and associated psychosocial burden.
- **Endocrine health:** canonical SPGF32 is primarily germ-cell failure; testosterone may be preserved, but all NOA patients require endocrine assessment.
- **Natural recovery:** unlikely for Sertoli-cell-only histology; no curative restoration of spermatogenesis is established.
- **Residual sperm:** genotype alone cannot reliably predict whether focal sperm production will permit retrieval.
- **Prognostic biomarkers:** testicular histology, testis volume, FSH and testosterone may inform general NOA counseling but do not reliably determine individual micro-TESE success; no SOHLH1-specific biomarker exists.
- **Complications:** emotional distress, repeated invasive procedures, and possible transmission of a pathogenic allele through ICSI.

Across heterogeneous NOA—not specifically SPGF32—systematic-review evidence suggests surgical sperm retrieval up to about **50%** and live birth up to **28%** after use of retrieved sperm. These aggregate rates should not be presented as a genotype-specific prognosis. [155]

---

## 12. Treatment

There is **no approved drug, gene therapy, RNA therapy or cell therapy that restores SOHLH1 function**. Management is reproductive rather than disease-modifying.

| Intervention | Role and evidence | Suggested NCIt concept |
|---|---|---|
| Repeat semen search and sperm cryopreservation | Preserve rare ejaculated sperm in severe oligo-/cryptozoospermia | **Sperm Cryopreservation** |
| Microdissection testicular sperm extraction | Preferred retrieval procedure for NOA candidates pursuing ART; outcome in Sertoli-cell-only disease may be poor | **Testicular Sperm Extraction**, **Surgical Procedure** |
| Intracytoplasmic sperm injection | Uses ejaculated or testicular sperm to fertilize an oocyte | **Intracytoplasmic Sperm Injection** |
| IVF | ART framework within which ICSI is performed | **In Vitro Fertilization** |
| Donor sperm | Option if retrieval fails or transmission risk is unacceptable | **Therapeutic Donor Insemination** |
| Adoption or child-free living | Nonmedical family-building options | No specific drug/intervention term |
| Psychological counseling | Addresses distress and decision burden | **Psychological Counseling** |
| Hormonal treatment | Treat documented hypogonadotropic hypogonadism, not primary SOHLH1 deficiency; empiric pretreatment before retrieval has limited evidence | **Hormone Therapy**, **Gonadotropin Therapy** |
| Varicocele repair | Only for an independently indicated clinical varicocele; benefit before ART in NOA is uncertain | **Varicocelectomy** |
| Gene replacement/editing | Preclinical concept only; no trial or validated germline-safe method | **Gene Therapy**, experimental |

AUA/ASRM recommends microdissection TESE for men with NOA undergoing retrieval and permits fresh or cryopreserved sperm for ICSI. [83]

### Patient-specific published outcomes

In the 2022 series, ICSI was attempted in one homozygous severe-oligozoospermia patient and two heterozygous teratozoospermia patients; pregnancies and successful deliveries were reported. In the homozygous case, 7/10 injected oocytes fertilized and transfer of a later 4AB embryo produced a healthy baby. These are uncontrolled individual outcomes, not a response rate. [62]

### Experimental treatment status

No SPGF32-specific ClinicalTrials.gov intervention, gene therapy, ASO, siRNA, stem-cell transplantation or CRISPR trial was identified. Germline editing is not an acceptable clinical prevention or treatment strategy.

---

## 13. Prevention

### Primary prevention

The inherited molecular lesion cannot be prevented by diet, vaccination or lifestyle. Avoiding unnecessary testicular heat, tobacco, anabolic steroids, gonadotoxic chemicals and radiation is reasonable for general fertility preservation but is not proven to prevent SPGF32.

### Secondary prevention

- Early evaluation of men from affected families.
- Semen analysis after puberty when clinically appropriate.
- Cryopreservation if sperm are present.
- Cascade genetic testing after expert variant interpretation.
- Partner testing if a recessive pathogenic allele is confirmed.

### Tertiary prevention

- Avoid prolonged empiric therapies that delay retrieval when residual spermatogenesis may decline.
- Offer fertility-preservation and ART counseling.
- Monitor endocrine and psychological health.
- Provide reproductive genetic counseling before ICSI.

### Reproductive prevention options

For a well-established pathogenic familial genotype, options include natural conception with prenatal diagnosis, IVF with PGT-M, donor gametes or adoption. With c.346-1G>A, counseling must emphasize conflicting pathogenicity and unresolved heterozygous penetrance. No immunization, medication prophylaxis or public-health control program is applicable.

---

## 14. Other species and naturally occurring disease

| Species | Taxonomy/ortholog | Evidence |
|---|---|---|
| Human, *Homo sapiens* | NCBI Taxon **9606**; *SOHLH1*, NCBI Gene **402381** | Natural Mendelian infertility |
| Mouse, *Mus musculus* | NCBI Taxon **10090**; *Sohlh1*, NCBI Gene **227631**, MGI:2684956 | Engineered knockout causes male and female infertility [136] |
| Other mammals | Orthologs are evolutionarily conserved | Functional conservation is inferred, but no well-established breed-specific natural veterinary SPGF32 counterpart was identified |

No breed-associated OMIA disorder, cross-species transmission or zoonotic potential applies. This is a constitutional genetic disorder, not an infectious disease.

---

## 15. Model organisms

### 15.1 Mouse models

| Model | Phenotype recapitulation | Uses and limitations |
|---|---|---|
| ***Sohlh1* targeted null**, MGI allele **Sohlh1^tm1Rajk**, MGI:3629211 | Homozygous males have reduced testis weight, failed differentiation of spermatogonia into spermatocytes and infertility; females rapidly lose oocytes/follicles | Strong mechanistic model of complete loss of function; may be more severe than common human splice alleles [146] |
| *Sohlh1* knockout used in 2023 systemic phenotyping | Impaired spermatogenesis plus immune-profile, metabolite and behavioral/cognitive alterations | Useful for pleiotropy and safety studies; extragonadal findings are not confirmed in humans [16] |
| *Sohlh1-CreER* targeted line, MGI:5548125 | Enables temporally controlled lineage manipulation | Tool model rather than a direct disease model [142] |
| Germ-cell and promoter-reporter systems | Demonstrate direct regulation of *KIT* and interactions with SOHLH2 | Simplified in-vitro systems cannot model human penetrance or complete testicular architecture |

The 2023 mouse study’s abstract states:

> “The Sohlh1 knockout mouse model… presents with… impaired spermatogenesis in males,” but extragonadal phenotyping also found “abnormal immune profiles… sex-specific alterations of metabolites, and behavior and cognition changes.”  
> — Rodríguez-Escribà et al., *Biology of Reproduction*, April 2023, PMID: **36723967** [16]

### 15.2 Model validity

**Strengths**

- Recapitulates germ-cell differentiation failure and infertility.
- Establishes temporal order from transcription-factor loss to spermatogonial arrest.
- Permits testicular histology, cell sorting, ChIP, transcriptomics and fertility studies.
- Demonstrates biologic plausibility for human splice-variant findings.

**Limitations**

- Complete knockout is not equivalent to partial-function c.346-1G>A.
- Human heterozygous penetrance is much less clear than mouse homozygous-null penetrance.
- Mouse spermatogenic timing and genetic background differ from humans.
- Human Sertoli-cell-only pathology and ICSI outcomes cannot be fully modeled.
- Reported systemic mouse phenotypes should not be entered as human SPGF32 manifestations without clinical corroboration.

---

## Overall evidence assessment

| Domain | Assessment |
|---|---|
| Gene–disease relationship | **Supported/strong**, especially by conserved biology, human functional assays and knockout mice |
| Canonical phenotype | Male infertility with severe spermatogenic failure, classically NOA and Sertoli-cell-only histology |
| Key variant | c.346-1G>A is functionally splice-altering but has **conflicting clinical classification** |
| Inheritance | Historically reported autosomal dominant/de novo; current evidence also supports recessive/dosage-dependent disease and incomplete heterozygous penetrance |
| Epidemiology | Unknown at disease-specific level |
| Diagnostic standard | Confirm spermatogenic failure, exclude common cytogenetic/Y-linked/endocrine causes, then panel/WES/WGS with segregation |
| Curative therapy | None |
| Current implementation | Sperm preservation or micro-TESE followed by ICSI; donor sperm if retrieval fails |
| Main research need | Larger ancestry-diverse cohorts with rigorous semen phenotyping, parental phasing, population penetrance analysis and functional comparison of heterozygous versus biallelic alleles |

The principal knowledge-base caution is therefore to **retain *SOHLH1* as the causal gene for MONDO:0020855, but not encode c.346-1G>A as an unquestionably fully penetrant dominant pathogenic allele**. Its molecular effect is well supported; its clinical penetrance and mode of inheritance are not.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 18 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 37 |
| Resolved | 31 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 5 |
| Terms whose name was checked | 7 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0020855` (4 mentions) - the report calls it "MONDO"; MONDO calls it **spermatogenic failure 32**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0007126` (GO_0007126) (1 mention) - replaced by `GO:0051321`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000019` (2 mentions) - the report calls it "Spermatozoon", "Spermatozoa"; CL calls it **sperm**, and lists "spermatozoid" among its other names
- `UBERON:0001343` (1 mention) - the report calls it "Seminiferous tubule"; UBERON calls it **seminiferous tubule of testis**, and lists "seminiferous tubule" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000019` - called "Spermatozoon", "Spermatozoa"
- `CL:0000216` - called "Sertoli cell", "Sertoli cells"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.