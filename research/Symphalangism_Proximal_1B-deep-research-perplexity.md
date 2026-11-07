---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-10-22T14:12:13.422392'
end_time: '2026-10-22T14:17:10.496537'
duration_seconds: 297.07
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Symphalangism Proximal 1B
  mondo_id: MONDO:0014125
  category: Mendelian
  causal_genes: GDF5
  omim_id: not recorded
  synonyms: not recorded
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 69
reference_validation:
  total_references: 20
  verified: 19
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.05
  quotes_checked: 3
  quotes_valid: 2
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:29371961
  relevance_assessed: 19
  on_topic: 12
  unresolved_references:
  - DOI:10.1371/journal.pgen.1000747&type=printable
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 64
  verified: 60
  not_found: 0
  obsolete: 1
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 23
  labels_matching: 9
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: MONDO:0014125
    reported_labels:
    - MONDO
    ontology_label: symphalangism, proximal, 1B
  - term_id: HP:0025233
    reported_labels:
    - Foot pain
    ontology_label: Sleep paralysis
  - term_id: GO:0061317
    reported_labels:
    - "GO\u2014joint morphogenesis"
    ontology_label: obsolete canonical Wnt signaling pathway involved in cardiac muscle
      cell fate commitment
  labels_variant: 11
  obsolete_terms:
  - term_id: GO:0061317
    ontology_label: obsolete canonical Wnt signaling pathway involved in cardiac muscle
      cell fate commitment
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
- **Disease Name:** Symphalangism Proximal 1B
- **MONDO ID:** MONDO:0014125 (if available)
- **Causal gene(s):** GDF5
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

Please provide a comprehensive research report on **Symphalangism Proximal 1B** covering all of the
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

# Symphalangism, Proximal, 1B — Comprehensive Disease Report

**Symphalangism, proximal, 1B (SYM1B)** is a rare, congenital Mendelian skeletal-joint disorder caused by heterozygous gain-of-function variants in **GDF5** (*growth differentiation factor 5*; HGNC:4220). The defining lesion is failed formation or later ossification of proximal interphalangeal joints, producing stiff, fused proximal and middle phalanges, often accompanied by carpal or tarsal coalitions. The disease corresponds to **MONDO:0014125 and OMIM 615298**, notwithstanding the source template’s statement that OMIM was unrecorded. It must not be confused with clinically similar **NOG-related proximal symphalangism 1A**, OMIM 185800. OMIM explicitly maps SYM1B to heterozygous *GDF5* variants at 20q11.22. [OMIM, updated July 21, 2024](https://omim.org/entry/615298). [2]

**Evidence date:** October 22, 2026. Disease-specific human evidence remains limited to a few pedigrees and case reports; no SYM1B-specific therapeutic trial, population registry, prospective natural-history study, or 2023–2024 clinical cohort was found.

---

## 1. Disease information

### 1.1 Definition and classification

Proximal symphalangism means congenital absence, ankylosis, or fusion of a proximal interphalangeal joint, usually between a proximal and middle phalanx. Clinically, this appears as an immobile straight finger, absent flexion crease, and inability to flex the affected joint. SYM1B is specifically the *GDF5*-caused subtype. Mondo defines it as “Any proximal symphalangism in which the cause of the disease is a mutation in the GDF5 gene.” [MedGen/MONDO, updated October 17, 2026](http://www.ncbi.nlm.nih.gov/medgen/815434). [1]

Orphanet’s broader **proximal symphalangism** entity includes both *NOG*- and *GDF5*-associated disease and defines the disorder as proximal interphalangeal ankylosis with carpal/tarsal fusion and, in some patients, conductive hearing loss. Consequently, its phenotype frequencies should not automatically be interpreted as *GDF5*-specific. [Orphanet, accessed October 2026](https://www.orpha.net/en/disease/detail/3250). [121]

### 1.2 Identifiers and synonyms

| System | Identifier or term | Scope/qualification |
|---|---|---|
| MONDO | **MONDO:0014125** | Gene-specific SYM1B |
| OMIM phenotype | **615298** | Symphalangism, proximal, 1B |
| OMIM gene | **601146** | *GDF5* |
| Orphanet | **ORPHA:3250** | Broader proximal-symphalangism entity; not strictly *GDF5*-specific |
| MedGen | **C3809104**, UID 815434 | SYM1B |
| UMLS | **C3809104** | Disease concept |
| Disease Ontology | **DOID:0080788** (“proximal symphalangism 2”) | Corresponds to OMIM 615298 |
| ICD-10-CM | No gene-specific code; **Q70.9** is sometimes used for unspecified syndactyly/symphalangism | Approximate, nonspecific |
| ICD-11 | No gene-specific code; **LB90.Y**, other specified defects of joint formation | Approximate, nonspecific |
| MeSH | No dedicated gene-specific descriptor; proximal symphalangism has been represented as supplementary concept **C536223** | Broad concept rather than SYM1B |
| Preferred name | Symphalangism, proximal, 1B |  |
| Synonyms | **SYM1B; GDF5 proximal symphalangism; proximal symphalangism caused by mutation in GDF5; proximal symphalangism type 1B** | Mondo/NORD synonyms [112] |

The disease-level information is aggregated from OMIM, Mondo, Orphanet, ClinVar, case reports, and pedigree studies. It is **not** derived from an EHR cohort or population-level clinical database.

---

## 2. Etiology, risk factors, and protective factors

### 2.1 Primary cause

The established cause is a **germline heterozygous activating missense variant in *GDF5***. Three variants have been specifically associated with the gene-defined SYM1B phenotype:

- c.1313G>T, p.Arg438Leu
- c.1471G>A, p.Glu491Lys
- c.1118T>G, p.Leu373Arg

Orphanet classifies proximal symphalangism-associated *GDF5* mutations as germline gain-of-function mutations. [Orphanet gene page, updated June 20, 2025](https://www.orpha.net/en/disease/gene/GDF5). [4]

### 2.2 Risk, protective, and interaction factors

| Factor class | Finding |
|---|---|
| Major genetic risk | Carrying a pathogenic heterozygous activating *GDF5* allele |
| Family history | Strong risk indicator because inheritance is autosomal dominant; each child of an affected heterozygous parent has a 50% transmission probability |
| Sex | No evidence of sex-limited inheritance or a materially different male:female risk |
| Age | The developmental lesion originates prenatally; age affects radiographic visibility, ossification, pain, and secondary osteoarthritis rather than genetic susceptibility |
| Common susceptibility loci | Common *GDF5* regulatory alleles influence osteoarthritis and joint traits, but they are not established causes or modifiers of SYM1B |
| Modifier genes | No validated SYM1B modifier gene |
| Protective genetic variants | None established |
| Environmental risk factors | None established for disease occurrence |
| Protective diet/lifestyle | None known to prevent the congenital malformation |
| Gene–environment interaction | No demonstrated etiologic interaction. Mechanical loading, footwear, activity, body weight, and injury may plausibly modify pain or secondary degeneration but not the embryonic joint defect |
| Infection/toxin/radiation | No causal association |
| Consanguinity | Not relevant to the usual heterozygous dominant form |
| Smoking/alcohol/diet | No evidence that these cause SYM1B |

The absence of environmental risk factors is consistent with SYM1B being an embryonic, allele-driven joint-patterning disorder rather than an acquired arthropathy.

---

## 3. Phenotypic spectrum

### 3.1 Gene-specific human findings

The earliest *GDF5* p.Arg438Leu family had inability to bend digits IV and V, absent flexion creases, complete fusion of proximal and middle phalanges of digit V, and less extensive fusion of digit IV. [Seemann et al., *J Clin Invest*, August 25, 2005, PMID 16127465](https://pmc.ncbi.nlm.nih.gov/articles/PMC1190374/). [47]

Two five-generation Chinese p.Glu491Lys families contained **17 diagnosed individuals**. Reported features included fusion of interphalangeal joints of fingers 2–4, distal interphalangeal fusion, absence of the cuboid, flat feet, and no shortening of the first and fifth metacarpals. Fusions and malformations were reportedly more severe with increasing age. [Wang et al., *Am J Med Genet A*, September 1, 2006, PMID 16892395](https://pubmed.ncbi.nlm.nih.gov/16892395/). [76][85]

A British p.Arg438Leu family demonstrated marked variable expressivity: two children had bilateral fifth-finger proximal symphalangism, while the mother and another child had brachydactyly without hand symphalangism; all four had multiple, generally bilateral, tarsal coalitions. None had conductive hearing loss. Foot pain, fixed planovalgus deformity, and secondary subtalar osteoarthritis caused more morbidity than the hand anomaly. [Leonidou et al., *World J Orthop*, December 18, 2016, PMID 28032038](https://pmc.ncbi.nlm.nih.gov/articles/PMC5155261/). [20]

### 3.2 Phenotype table

Frequencies below distinguish **direct SYM1B evidence** from broader ORPHA:3250 annotations, which mix molecular subtypes.

| Phenotype/type | HPO suggestion | Onset and course | Frequency/evidence in SYM1B | Functional or quality-of-life effect |
|---|---|---|---|---|
| Proximal symphalangism—physical sign | **HP:0100264** | Congenital developmental defect; initially fibrous/cartilaginous and may become radiographically bony with age | Defining feature, but variable expressivity can leave some variant carriers with brachydactyly rather than overt finger fusion | Reduced PIP flexion, inability to make a full fist, handwriting or fine-motor difficulty |
| Fifth-finger proximal symphalangism | **HP:0009177** | Congenital; stable after fusion, although ossification becomes clearer with age | Present bilaterally in 2/4 members of the British p.Arg438Leu family | Usually mild hand impairment |
| Fourth-finger proximal symphalangism | Relevant digit-specific HPO term; broader HP:0100264 | Congenital | Reported with p.Arg438Leu | Reduced ring-finger flexion |
| Absent/reduced finger flexion crease | **HP:0006191** or abnormal finger flexion crease **HP:0006143** | Evident clinically in childhood, sometimes before diagnostic radiographic fusion | Reported in the original p.Arg438Leu family | Useful bedside diagnostic sign |
| Distal symphalangism | **HP:0100263** | Congenital; may become more extensive with age | Reported with p.Glu491Lys; not universal | Additional loss of digital motion |
| Carpal synostosis | **HP:0005048** | Developmental; usually stable | Broader proximal symphalangism: very frequent; direct gene-specific data are sparse | Wrist stiffness may occur |
| Tarsal synostosis/coalition | **HP:0008368** | Congenital; often becomes symptomatic in later childhood/adolescence as coalitions ossify and activity rises | All 4 p.Arg438Leu British family members; broader Orphanet: very frequent | Flatfoot, stiffness, activity-limiting pain; potentially the main morbidity |
| Pes planus/planovalgus | **HP:0001763** | Childhood onward; pain and deformity may worsen | Reported in p.Glu491Lys and p.Arg438Leu families | Reduced walking/exercise tolerance; orthotic or surgical treatment may be required |
| Brachydactyly | **HP:0001156** | Congenital, nonprogressive morphology | 2/4 British p.Arg438Leu carriers; broader Orphanet: frequent | Usually limited functional impact |
| Abnormal metacarpal morphology | **HP:0005916** | Congenital | Broader Orphanet: frequent; p.Glu491Lys families specifically lacked first/fifth metacarpal shortening | Usually mild |
| Finger clinodactyly | **HP:0040019**; fifth finger **HP:0004209** | Congenital | Frequent/occasional in broad Orphanet entity; gene-specific frequency unknown | Usually cosmetic or mildly functional |
| Camptodactyly | **HP:0100490** | Congenital/childhood | Very frequent in broad Orphanet entity; not established as very frequent specifically in molecularly confirmed SYM1B | Fine-motor limitation if severe |
| Metacarpophalangeal synostosis | **HP:0005880** | Congenital | More characteristic of the overlapping *GDF5*-related multiple-synostoses spectrum; broad Orphanet: frequent | Greater hand stiffness |
| Elbow ankylosis/dislocation | **HP:0003070**, **HP:0003042** | Congenital | Broad proximal-symphalangism annotation; uncommon or unreported in the three canonical SYM1B pedigrees | Limits upper-limb range of motion |
| Conductive hearing impairment | **HP:0000405** | Congenital or childhood; attributable in related syndromes to ossicular/stapes fixation | Recognized in broad proximal symphalangism, but absent in all 4 tested British *GDF5* carriers; *GDF5*-specific frequency unknown | Communication and educational impact if present |
| Sensorineural hearing impairment | **HP:0000407** | Variable | Marked “frequent” by Orphanet for the broad entity, but this conflicts with classic descriptions emphasizing conductive loss; not established in canonical SYM1B reports | Hearing-related QOL impact |
| Foot pain | **HP:0025233** | Often later childhood or adulthood; activity related | Major presenting problem in the British family | Limits activities of daily living and exercise |
| Secondary osteoarthritis | **HP:0002758** | Adult complication rather than congenital feature | Subtalar osteoarthritis in the 40-year-old British p.Arg438Leu carrier | Chronic pain; can necessitate fusion |
| Finger syndactyly | **HP:0006101** | Congenital | Occasional in broad Orphanet entity; not a core gene-specific finding | Variable |
| Strabismus | **HP:0000486** | Variable | Occasional broad Orphanet annotation; causal relationship to *GDF5*-SYM1B uncertain | Usually unrelated to core skeletal morbidity |

Orphanet’s complete broad-entity frequency assignments are: very frequent—camptodactyly, proximal symphalangism, carpal synostosis and tarsal synostosis; frequent—abnormal metacarpals, brachydactyly, elbow ankylosis/dislocation, clinodactyly, metacarpophalangeal synostosis and sensorineural hearing impairment; occasional—wrist abnormality, fifth-finger clinodactyly, syndactyly and strabismus. [Orphanet clinical signs, updated July 1, 2026](https://www.orpha.net/en/disease/sign/3250). [120]

No validated SYM1B-specific EQ-5D, SF-36, PROMIS, or disease-specific quality-of-life study has been published.

---

## 4. Genetic and molecular information

### 4.1 Gene and protein

| Attribute | Annotation |
|---|---|
| Gene | **GDF5**, growth differentiation factor 5 |
| HGNC | **HGNC:4220** |
| NCBI Gene | **8200** |
| Ensembl | **ENSG00000125965** |
| OMIM gene | **601146** |
| Chromosome | **20q11.22** |
| MANE transcript | **NM_000557.5** |
| Protein | **NP_000548.2**, 501-aa preproprotein |
| UniProt | **P43026** |
| Synonyms | BMP14, CDMP1, LAP4 |
| Protein class | Secreted BMP/TGF-β-superfamily growth factor |
| Principal receptors | BMPR1B preferentially; BMPR1A at lower affinity; type-II receptors including BMPR2/ACVR2A |
| Main inhibitor | NOG/Noggin |

NCBI lists NM_000557.5 and NP_000548.2 as the MANE transcript and 501-aa preproprotein. [NCBI Datasets, updated October 11, 2026](https://www.ncbi.nlm.nih.gov/datasets/gene/id/8200/products/). [144] UniProt describes GDF5 as a bone/cartilage growth factor acting through BMPR1B/BMPR1A and SMAD1/5/8. [UniProt P43026, updated September 19, 2026](https://www.uniprot.org/uniprotkb/P43026/entry). [136]

### 4.2 Pathogenic variants specifically reported for SYM1B

| Variant, domain | ClinVar status | Population evidence | Human evidence | Functional consequence |
|---|---|---|---|---|
| **NM_000557.5:c.1313G>T; p.Arg438Leu; rs74315388**; mature ligand/receptor-interaction surface | Pathogenic, one OMIM submission, 0-star/no assertion criteria; RCV000008893.4 | No ClinVar gnomAD frequency displayed | Segregated in original US family and recurrent British family; also reported in overlapping SYNS2 | Germline missense **gain of function**: retains BMPR1B and Noggin binding but gains strong BMPR1A binding and BMP2-like activity |
| **NM_000557.5:c.1471G>A; p.Glu491Lys; rs74315389**; mature TGF-β domain | Pathogenic, one OMIM submission, 0-star; RCV000008897.4 | Absent from 200 contemporaneous controls; no ClinVar gnomAD frequency displayed | Cosegregated in two five-generation Chinese families; complete penetrance reported | Presumed/established activating allele; later assays found receptor signaling similar to wild type, so its precise gain-of-function biochemistry is less fully resolved than p.Arg438Leu |
| **NM_000557.5:c.1118T>G; p.Leu373Arg; rs121909349**; prodomain | Pathogenic, one OMIM submission, 0-star; RCV000008900.3 | Absent from 50 controls and 3 unaffected relatives; no ClinVar gnomAD frequency displayed | Heterozygous in a four-generation Han Chinese family | Increased proteolytic processing, GDF5–BMPR1B interaction, pSMAD1/5/8 signaling and chondrogenic output |

ClinVar’s classifications are old literature-only assertions without contemporary expert-panel review; therefore, “pathogenic” is well supported by segregation and functional evidence, but the records themselves do not represent three-star ClinGen adjudications. [ClinVar p.Arg438Leu](https://www.ncbi.nlm.nih.gov/clinvar/RCV000008893/), [p.Glu491Lys](https://www.ncbi.nlm.nih.gov/clinvar/RCV000008897/), and [p.Leu373Arg](https://www.ncbi.nlm.nih.gov/clinvar/RCV000008900/). [106][107][126]

### 4.3 Variant interpretation cautions

- **Allele mechanism is critical.** *GDF5* loss-of-function variants cause brachydactyly or recessive acromesomelic dysplasias, while activating alleles cause joint-fusion phenotypes.
- A truncating or deletion variant in *GDF5* should therefore **not** automatically be classified as causative of SYM1B merely because *GDF5* is a disease gene.
- The three canonical SYM1B alleles are missense variants in the prodomain or mature signaling domain.
- Germline, not somatic, origin is expected.
- No repeat expansion, mitochondrial mutation, aneuploidy, or recurrent structural rearrangement causes canonical SYM1B.
- No disease-specific methylation signature, chromatin abnormality, or epigenetic biomarker is known.
- No validated modifier locus or protective allele has been identified.

GenCC now records the *GDF5*–SYM1B autosomal-dominant relationship as **definitive**. [GenCC, evaluations through July 2025](https://thegencc.org/genes/HGNC:4220). [108]

---

## 5. Environmental and lifestyle information

SYM1B is not caused by infection, toxicant exposure, radiation, nutrition, smoking, alcohol, occupation, or physical activity. These factors do not explain familial cosegregation and cannot prevent the embryonic joint-development defect.

After birth, mechanical factors may affect **morbidity**:

- Repetitive load and rigid flatfoot can aggravate coalition-related pain.
- Obesity could plausibly increase load on painful tarsal coalitions, but no SYM1B-specific study demonstrates this.
- Supportive footwear, orthoses, activity modification and maintenance of general fitness may reduce symptoms but are not disease-modifying.
- Trauma through an ankylosed joint can cause fracture or delayed union, although this complication is documented mainly in broader symphalangism rather than molecularly confirmed SYM1B.

No CTD-supported disease-specific gene–environment interaction or infectious trigger was identified.

---

## 6. Mechanism and pathophysiology

### 6.1 Ordered causal chain

1. A **heterozygous activating germline *GDF5* missense variant** leads to altered processing or receptor-binding behavior of secreted GDF5.
2. Altered GDF5 leads to **excessive or spatially inappropriate BMP-family signaling** in embryonic joint-forming regions.
   - **p.Arg438Leu branch:** loss of receptor specificity leads to acquired BMPR1A binding while BMPR1B and Noggin binding remain intact.
   - **p.Leu373Arg branch:** increased prodomain processing and inferred increased ligand availability lead to stronger GDF5–BMPR1B interaction and SMAD1/5/8 phosphorylation.
   - **p.Glu491Lys branch:** clinical/segregation evidence indicates an activating joint-fusion allele, but the exact biochemical perturbation is less definitively demonstrated.
3. Excess or ectopic receptor activation leads to increased phosphorylation of **SMAD1/5/8**, SMAD4-complex formation and altered transcription of chondrogenic genes.
4. Altered transcription leads to abnormal persistence, proliferation, differentiation or maturation of **GDF5-lineage interzone/chondroprogenitor cells**.
5. Abnormal interzone behavior leads to failure to form or maintain a normal noncartilaginous joint cavity between developing skeletal elements.
6. Persistent cartilage across the presumptive joint leads to a cartilaginous bridge and, with endochondral maturation, **bony synostosis**.
7. Synostosis results in congenital immobility of proximal interphalangeal joints and, where carpal/tarsal sites are involved, wrist/foot stiffness and flatfoot.
8. Abnormal load distribution and restricted motion may subsequently lead to pain, reduced activity and secondary osteoarthritis; this final degenerative step is clinically observed but not experimentally proven as a uniform SYM1B pathway.

### 6.2 Variant-specific experimental evidence

For p.Arg438Leu, biosensor experiments found normal BMPR1B and Noggin binding but increased BMPR1A binding. ATDC5 and C2C12 assays showed stronger, BMP2-like biological activity. Chick limb overexpression of wild-type or p.Arg438Leu GDF5 caused thickened skeletal anlagen and joint fusions. The authors’ abstract states:

> “The symphalangism phenotype (R438L) is caused by a loss of receptor-binding specificity, resulting in a gain of function by the acquisition of BMP2-like properties.”

[Seemann et al., *J Clin Invest*, published online August 25, 2005; PMID 16127465](https://pubmed.ncbi.nlm.nih.gov/16127465/). [45]

For p.Leu373Arg, ATDC5-cell work showed increased proteolytic efficiency, increased GDF5–BMPR1B proximity, increased pSMAD1/5/8, and increased *SMURF1*, *COL2A1* and *SOX9*. The orthologous mouse knock-in caused joint stiffness and fusion. The abstract reports:

> “The variant caused proteolysis efficiency of GDF5 increased in ATDC5 cells” and caused “upregulation of SMAD1/5/8 phosphorylation.”

[Zhang et al., *Oncotarget*, December 8, 2017; PMID 29371961](https://pubmed.ncbi.nlm.nih.gov/29371961/). [66]

### 6.3 Pathways, processes, cells and ontology suggestions

| Mechanistic level | Annotation |
|---|---|
| Upstream pathway | BMP signaling, Reactome **R-HSA-201451**; KEGG TGF-β signaling **hsa04350** |
| Receptors | BMPR1B/ALK6, BMPR1A/ALK3, BMPR2/ACVR2-family receptors |
| Canonical signaling | SMAD1/5/8 phosphorylation → SMAD4 complex → nuclear transcription |
| Key target/readout genes | *SOX9, COL2A1, ACAN, SMURF1*; *ID1* results were context-dependent |
| GO—BMP signaling | **GO:0030509** |
| GO—SMAD signal transduction | **GO:0060395**, SMAD protein signal transduction |
| GO—chondrocyte differentiation | **GO:0002062** |
| GO—cartilage development | **GO:0051216** |
| GO—joint morphogenesis | **GO:0061317** |
| GO—skeletal system development | **GO:0001501** |
| GO—endochondral ossification | **GO:0001958** |
| GO molecular function | Growth factor activity **GO:0008083**; TGF-β receptor binding **GO:0005160** |
| Primary cells | Joint-interzone mesenchymal progenitors; chondroblasts **CL:0000058**; chondrocytes **CL:0000138**; mesenchymal stem/progenitor cells **CL:0000134**; osteoblasts **CL:0000062** |
| Primary cellular processes | Mesenchymal condensation, chondrogenic differentiation, cartilage-matrix production, hypertrophy and endochondral maturation |
| Protein compartment | Secretory pathway, extracellular space and extracellular ligand–receptor complex; GO suggestions: extracellular region **GO:0005576**, Golgi apparatus **GO:0005794**, endoplasmic reticulum **GO:0005783** |
| Metabolism/immune system | No primary metabolic deficiency, immune dysregulation, inflammation, oxidative stress or ischemic mechanism demonstrated |

### 6.4 Molecular profiling and advanced technologies

No SYM1B-patient transcriptome, proteome, metabolome, lipidome, single-cell dataset or spatial-transcriptomic dataset has been reported.

Related developmental studies are nevertheless informative:

- Mouse single-cell RNA sequencing shows that Gdf5-lineage cells contribute to articular cartilage, ligaments, meniscus and synovium. [Bian et al., 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7390639/). [306]
- A 2023 “digits in a dish” system identified a *Jun/Gdf5/Hoxd13*-enriched cluster resembling the embryonic joint interzone, providing a possible future platform for variant testing. [Published March 13, 2023](https://www.frontiersin.org/articles/10.3389/fcell.2023.1135025/full). [305]
- A 2024 multi-omic atlas of 12 human embryonic donors, 5–11 postconception weeks, identified GDF5-high interzone populations using paired snRNA-seq/snATAC-seq. This advances normal human joint biology but did not study SYM1B variants. [Published November 20, 2024](https://www.nature.com/articles/s41586-024-08189-z). [313]

---

## 7. Anatomical structures affected

| Level | Primary structures/cells | Ontology suggestions |
|---|---|---|
| Organ/body-system | Appendicular musculoskeletal system; no primary visceral-organ disease | Appendicular skeleton **UBERON:0002091** |
| Hand | Proximal interphalangeal joints, especially fourth/fifth digits; proximal and middle phalanges; sometimes carpal/metacarpophalangeal joints | Hand/manus **UBERON:0002398**; manual digit **UBERON:0002389**; middle phalanx of manus **UBERON:0003864**; fifth-finger PIP joint **UBERON:0016426** |
| Foot | Tarsal bones and joints, metatarsal–cuneiform, calcaneocuboid and talonavicular regions; phalanges in some families | Foot/pes **UBERON:0002387** |
| Connective tissue | Embryonic cartilage anlage and joint interzone; later bony bridge/synostosis | Cartilage tissue, bone tissue and synovial-joint structures |
| Cells | GDF5-positive interzone progenitors and chondrocytes | **CL:0000134**, **CL:0000058**, **CL:0000138** |
| Secondary sites | Subtalar joint and surrounding foot structures affected by altered mechanics/osteoarthritis | Subtalar region |
| Ear | Middle-ear ossicles/stapes in hearing-associated proximal-symphalangism syndromes; direct frequency in SYM1B uncertain | Middle ear/ossicle ontology terms |
| Lateralization | Finger and tarsal findings are commonly **bilateral**, but severity and the exact coalitions can be asymmetric; e.g., a right-only talonavicular coalition occurred in one British family member | **HP:0012837**, bilateral; asymmetric severity may be captured separately |

---

## 8. Temporal development and natural history

- **Initiation:** prenatal, during embryonic segmentation and synovial-joint formation.
- **Clinical onset:** congenital, although recognition may occur in childhood when absent creases or immobility become apparent.
- **Radiographic onset:** early fusion may be fibrous or cartilaginous and radiolucent. Progressive joint-space narrowing and bony bridging can become clearer later in childhood.
- **Course:** lifelong and nonremitting. The developmental malformation itself is stable once ossified, but anatomic fusion may appear more severe with age.
- **Pain:** generally not intrinsic to an immobile finger but can develop in tarsal coalitions during later childhood/adolescence.
- **Adult complications:** altered mechanics can produce osteoarthritis and chronic foot pain.
- **Disease stages:** a practical radiographic scheme used for symphalangism is grade I fibrous, grade II cartilaginous and grade III bony fusion. Grade III consists of complete osseous bridging with no motion. [Clinical review/case report, September 28, 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9542568/). [183]
- **Remission:** none expected; symptomatic relief is possible.
- **Critical period:** embryonic joint formation is the causal developmental window. For selected grade I–II hand procedures, younger age has sometimes been associated with better mobility outcomes, but evidence is weak and not genotype-specific.

---

## 9. Inheritance and population characteristics

| Characteristic | Best-supported conclusion |
|---|---|
| Inheritance | **Autosomal dominant** |
| Recurrence risk | 50% for each pregnancy when one parent is heterozygous |
| Penetrance | Complete in the two p.Glu491Lys pedigrees; overall penetrance is probably high but cannot be assumed absolutely complete for every allele |
| Expressivity | Markedly variable, including within a family: proximal fusion, brachydactyly, different tarsal coalitions and differing pain severity |
| Anticipation | Not reported; no repeat-expansion mechanism |
| Germline mosaicism | Not specifically documented for canonical SYM1B; biologically possible and reported for other activating *GDF5* synostosis alleles |
| Founder effect | None established; p.Arg438Leu is recurrent in unrelated US/British families |
| Consanguinity | No established role |
| Carrier frequency | Unknown; “carrier” is not an asymptomatic recessive state because a heterozygous pathogenic allele is sufficient |
| Sex ratio | No measured ratio; autosomal inheritance predicts broadly equal susceptibility |
| Ethnic/geographic distribution | Families reported from the United States, China and the United Kingdom; no proven high-risk population |
| Prevalence | Unknown; no reliable cases-per-100,000 estimate for molecularly confirmed SYM1B |
| Incidence | Unknown |
| Minimum published case burden | More than 20 affected/variant-positive individuals across the reported pedigrees, but the literature does not support a definitive exhaustive count |

The p.Glu491Lys mutation cosegregated with all affected members in two five-generation families and was absent from 200 controls; penetrance was described as complete despite inter- and intrafamilial phenotypic variation. [ClinVar/Wang et al., PMID 16892395](https://www.ncbi.nlm.nih.gov/clinvar/RCV000008897/). [75]

The often-quoted estimate that symphalangism represents approximately 0.03% of congenital upper-limb anomalies applies to all symphalangism and is not a prevalence estimate for genetically confirmed SYM1B. [Case review, November 10, 2020](https://journals.sagepub.com/doi/10.1177/2513826X20970355). [127]

---

## 10. Diagnosis

### 10.1 Clinical and imaging diagnosis

A practical evaluation includes:

1. Document congenital finger/toe stiffness and family history.
2. Examine active and passive PIP range of motion and flexion creases.
3. Assess fist closure, dexterity, handwriting, gait, hindfoot valgus and pes planus.
4. Obtain bilateral hand and foot radiographs.
5. If coalition anatomy or surgical planning remains uncertain, use CT; MRI may identify nonossified fibrous/cartilaginous coalition.
6. Perform audiometry if hearing symptoms exist or as a baseline because hearing impairment is part of the broader proximal-symphalangism differential.
7. Refer to clinical genetics for molecular confirmation and family testing.

No blood chemistry, enzyme assay, biopsy, EMG, ECG or disease-specific biochemical biomarker diagnoses SYM1B.

### 10.2 Genetic testing strategy

| Clinical situation | Recommended approach |
|---|---|
| Classic phenotype plus known familial variant | Targeted familial-variant testing |
| Classic phenotype, no familial variant | Sequence *GDF5* and **NOG**, preferably on a congenital limb/joint-fusion panel |
| Broad or overlapping phenotype | Panel including at least *GDF5, NOG, FGF9, GDF6, BMPR1B* and other skeletal-patterning genes |
| Negative panel but strong Mendelian phenotype | Trio exome or genome sequencing with CNV analysis and phenotype-driven reanalysis |
| Isolated pathogenic *GDF5* variant | Interpret in an allele-specific manner; establish whether its known mechanism matches activating SYM1B rather than loss-of-function brachydactyly |
| CMA/karyotype/FISH | Low yield for classic familial SYM1B; use if multiple congenital anomalies suggest a chromosomal disorder |
| mtDNA/repeat-expansion testing | Not indicated |
| RNA-seq/proteomics/metabolomics | Not established diagnostically |

GTR lists a clinical *GDF5* NGS test including deletion/duplication analysis for SYM1B, although the canonical alleles are SNVs. [GTR000599400.1, updated April 7, 2025](https://www.ncbi.nlm.nih.gov/gtr/tests/599400.1/). [314] *GDF5* is also a green/established gene on Genomics England limb and skeletal-dysplasia panels. [PanelApp](https://panelapp.genomicsengland.co.uk/panels/entities/GDF5). [316]

### 10.3 Differential diagnosis

| Disorder | Gene | Distinguishing considerations |
|---|---|---|
| Proximal symphalangism 1A | **NOG** | Most important phenocopy; conductive hearing loss/stapes ankylosis may be prominent |
| Multiple synostoses syndrome 1 | **NOG** | More extensive, progressive fusion involving elbows and other joints |
| Multiple synostoses syndrome 2 | **GDF5** | Allelic continuum with SYM1B; more extensive proximal/distal, carpal/tarsal, MCP and larger-joint synostoses |
| Multiple synostoses syndrome 3 | **FGF9** | Broader synostosis pattern |
| Multiple synostoses syndrome 4 | **GDF6** | Multiple-joint involvement; different gene |
| Brachydactyly A2 | **BMPR1B** or specific *GDF5* loss-of-function alleles | Short/angulated middle phalanges rather than the canonical activating-joint-fusion phenotype |
| Brachydactyly C / A1C | **GDF5** | Shortening/hypoplasia predominates; usually loss-of-function mechanism |
| Grebe/Hunter–Thompson acromesomelic dysplasia | Biallelic **GDF5** | Severe recessive limb shortening and dysplasia |
| Distal symphalangism | Various/heterogeneous | DIP rather than PIP fusion |
| Tarsal coalition without syndromic hand findings | Heterogeneous | Foot-only presentation; no defining familial proximal symphalangism |
| Acquired PIP ankylosis | Trauma, infection, inflammatory arthritis | Acquired history, pain/inflammation and absence of congenital/familial pattern |

### 10.4 Screening

There is no newborn population screen. Appropriate strategies are:

- **Cascade testing** of first-degree relatives after a familial pathogenic variant is established.
- Childhood examination/radiographs and audiology as clinically indicated.
- Prenatal or preimplantation testing only after the familial variant is known.
- Population carrier screening is not justified.

---

## 11. Outcome and prognosis

- **Life expectancy and survival:** presumed normal; no disease-specific mortality or reduced-survival signal.
- **Mortality:** no deaths directly attributable to SYM1B have been documented.
- **Major morbidity:** fixed finger motion, painful tarsal coalition, planovalgus foot, difficulty with prolonged walking/exercise, and secondary osteoarthritis.
- **Hand function:** often surprisingly well preserved through adaptation, although writing, grip or fist formation can be impaired.
- **Hearing:** prognosis depends on whether ossicular hearing loss is present; no hearing loss occurred in the four-member British *GDF5* family.
- **Recovery:** spontaneous restoration of a missing/fused joint does not occur. Symptoms can improve with orthoses, therapy, analgesia or selected surgery.
- **Prognostic factors:** number and location of fused joints, degree of planovalgus deformity, coalition type, residual motion, pain, and presence of secondary arthritis. No molecular prognostic biomarker exists.
- **Quality-of-life data:** no standardized SYM1B cohort data.

In the British family, the mother developed painful fixed valgus and subtalar osteoarthritis requiring fusion, whereas all three children were managed with orthotics alone. [Leonidou et al., PMID 28032038](https://www.wjgnet.com/2218-5836/full/v7/i12/839.htm). [27]

---

## 12. Treatment and real-world implementation

There is no treatment that reverses the embryonic joint-patterning defect and no approved genotype-targeted drug, gene therapy, RNA therapy or cell therapy.

| Intervention | Indication/evidence | Outcome/limitations | NCIt term suggestion |
|---|---|---|---|
| Observation/clinical surveillance | Mild, well-adapted hand disease without pain | Many patients require no intervention | **NCIT:C15747**, observation |
| Occupational therapy | Dexterity, writing, grip adaptation | May optimize function; cannot mobilize a complete bony bridge | **NCIT:C15310**, occupational therapy |
| Physical therapy/exercise | Foot mechanics, strength, postoperative rehabilitation; selected partially mobile joints | Does not reverse established bony fusion | **NCIT:C15311**, physical therapy |
| Orthoses/arch supports | Painful flatfoot or tarsal coalition | Used successfully as conservative management in three British children | **NCIT:C19332**, orthopedic device/intervention |
| Activity modification | Activity-provoked foot pain | Symptomatic only | Supportive care |
| Acetaminophen/paracetamol | Episodic musculoskeletal pain | No disease-modifying effect | **NCIT:C198**, acetaminophen |
| NSAID, e.g. ibuprofen | Pain/inflammation from secondary degeneration | Standard class risks; no SYM1B-specific trial | **NCIT:C257**, ibuprofen; NSAID class |
| Image-guided/local injection | Persistent coalition-related pain | Temporary symptomatic relief; used in the British mother | **NCIT:C15403**, injection procedure |
| Capsulotomy/collateral-ligament release | Selected grade I–II fibrous/cartilaginous symphalangism with significant disability | Better results before complete bony fusion; evidence is small and nongene-specific | **NCIT:C51981**, capsulotomy |
| Interposition or PIP arthroplasty | Rare, carefully selected severe hand dysfunction | Re-ankylosis, stiffness and poor range-of-motion outcomes are common | **NCIT:C51573**, arthroplasty |
| Corrective osteotomy/arthrodesis | Digit fused in an unusable position | Improves position rather than recreating a normal joint | **NCIT:C51905**, osteotomy; **NCIT:C52009**, arthrodesis |
| Tarsal-coalition resection | Symptomatic localized coalition without advanced arthritis, after conservative failure | Preserves motion where anatomically feasible; no SYM1B response-rate data | **NCIT:C15773**, surgical resection |
| Subtalar or other fusion | Severe deformity, broad coalition or secondary arthritis | Relieves painful motion at the cost of further joint motion; performed in one reported p.Arg438Leu adult | Arthrodesis |
| Hearing aids/ossicular surgery | Documented hearing loss | Individualized by audiology/otology; not studied specifically in SYM1B | **NCIT:C16696**, hearing aid; otologic surgery |

AAOS recommends initial orthotics/physical therapy for symptomatic tarsal coalition, with resection, reconstruction or fusion according to coalition size, deformity and arthritis when conservative treatment fails. [AAOS OrthoInfo, current October 2026](https://www.orthoinfo.org/diseases--conditions/tarsal-coalition/). [220]

### Trials and experimental therapy

- No interventional trial specifically tests treatment of SYM1B.
- **NCT00001754**, “Study of Skeletal Disorders and Short Stature,” includes proximal symphalangism but is an observational natural-history/genetic study, not a treatment trial. [ClinicalTrials.gov, updated January 28, 2026](https://clinicaltrials.gov/study/NCT00001754). [202]
- Trials of recombinant human GDF5 for disc disease are **not** treatments for SYM1B and should not be extrapolated to an activating *GDF5* disorder.
- Because SYM1B is caused by excess/misdirected signaling during embryogenesis, postnatal GDF5 supplementation is mechanistically inappropriate.
- Editing or allele-specific silencing remains theoretical and would face the additional challenge that the critical pathogenic period is prenatal.

---

## 13. Prevention

### Primary prevention

There is no vaccine, medication, diet, toxin avoidance or behavioral intervention that prevents a de novo or inherited pathogenic *GDF5* allele.

### Genetic and reproductive prevention

- Provide genetic counseling explaining autosomal-dominant inheritance and the **50% transmission risk**.
- Test an affected parent/proband first to establish the exact variant.
- Offer targeted testing to at-risk relatives.
- Reproductive options include natural conception with prenatal diagnosis, IVF with **PGT-M**, donor gametes or adoption.
- PGT-M requires a previously identified pathogenic/likely pathogenic familial variant. [Genetic-counseling review, published December 15, 2023](https://www.frontiersin.org/journals/reproductive-health/articles/10.3389/frph.2023.1213546/full). [365]
- Targeted prenatal testing can use chorionic villus or amniotic-fluid DNA; ultrasound may miss mild isolated digital fusion, especially when the joint is still cartilaginous.
- A prenatal molecular diagnosis has been demonstrated for *NOG*-related proximal symphalangism; the same targeted-testing principle is technically applicable to a known familial *GDF5* variant, although direct SYM1B prenatal series are absent. [Published November 6, 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6836329/). [368]

### Secondary and tertiary prevention

- Early clinical recognition avoids misdiagnosis as inflammatory or post-traumatic stiffness.
- Early identification of painful tarsal coalition can support orthotic treatment before fixed deformity and secondary arthritis become advanced.
- Audiologic screening can detect treatable hearing impairment.
- Occupational/physical therapy and ergonomic adaptation may prevent avoidable functional limitation.
- Weight management, suitable footwear and low-impact conditioning are reasonable for reducing load-related symptoms, although not studied specifically in SYM1B.

---

## 14. Other species and natural disease

No well-established naturally occurring veterinary disorder has been shown to be the exact ortholog of human *GDF5* gain-of-function SYM1B.

| Species | Taxon | Ortholog/resource | Natural or experimental findings | Relevance/limitation |
|---|---:|---|---|---|
| Human | **9606** | *GDF5*, NCBI 8200 | Natural autosomal-dominant SYM1B | Target disease |
| Mouse, *Mus musculus* | **10090** | *Gdf5*, NCBI 14563; MGI:95688 | Spontaneous brachypodism alleles and induced alleles cause shortened digits and missing/fused joints; L367R knock-in models human SYM1B | Best mechanistic model; classic brachypodism is loss-of-function and therefore not the same allele mechanism |
| Rat, *Rattus norvegicus* | **10116** | *Gdf5*, NCBI 252835 | Ortholog conserved; no established natural SYM1B equivalent | Comparative molecular resource |
| Chicken, *Gallus gallus* | **9031** | *GDF5*, NCBI 374249 | RCAS-mediated overexpression of wild-type or p.Arg438Leu-like GDF5 causes enlarged cartilage and joint fusion | Strong embryonic limb assay but induced, not natural disease |
| Zebrafish, *Danio rerio* | **7955** | *gdf5*, ZFIN:ZDB-GENE-990415-39; NCBI 30195 | CRISPR mutants alter fin endoskeletal segmentation and radials; joints/mineralization may be less affected | Useful for conserved endoskeletal development, but fin anatomy and loss-of-function phenotype do not closely recapitulate SYM1B |

Zebrafish homozygous *gdf5* mutants lose posterior pectoral-fin radials and have disorganized median-fin elements, while joint and mineralization phenotypes differ from the human disorder. [ZFIN](https://zfin.org/ZDB-PUB-210710-11). [255]

There is no zoonotic potential, infectious transmission or cross-species contagion.

---

## 15. Model organisms and experimental systems

| Model | Type | Phenotype and application | Limitations/resource |
|---|---|---|---|
| **Gdf5 L367R/+ knock-in mouse** | Humanized-equivalent activating allele | Straight, inflexible digits; proximal phalanx adhesions/fusions; abnormal embryonic joint development and absent/delayed primary ossification centers; closest SYM1B model | Hearing not formally characterized; small study; some internal inconsistencies in *Sox9/Col2a1* expression reporting |
| **Gdf5 L367R/L367R mouse** | Homozygous knock-in | More extensive metacarpal, proximal and distal phalangeal fusion resembling multiple synostoses | Homozygous state does not represent usual heterozygous human SYM1B |
| **Gdf5 brachypodism mouse** | Spontaneous/null loss-of-function | More than 30% of limb synovial joints disrupted, with digit/wrist/ankle fusion | Models GDF5 deficiency and recessive dysplasia better than activating SYM1B [231] |
| **Gdf5 W408R ENU mouse** | Induced dominant-negative | Brachypodism and ankylosis in heterozygotes; severe ankylosis and early elbow osteoarthritis in homozygotes | Different mechanism from canonical SYM1B [242] |
| Chick limb RCAS overexpression | In ovo developmental model | Wild-type and p.Arg438Leu GDF5 cause thick skeletal elements and joint fusion; allows receptor/antagonist mechanism testing | Supraphysiologic overexpression, species/anatomical differences |
| Chicken limb-bud micromass | Primary-cell in vitro model | Measures Alcian-blue cartilage matrix and ALP differentiation after mutant GDF5 expression | Does not recreate full joint architecture |
| ATDC5 cells | Murine chondrogenic cell line | Used to test ligand processing, GDF5–BMPR1B interaction, pSMAD1/5/8 and chondrogenic genes | Transformed/in vitro context |
| C2C12 cells | Mesenchymal/myoblast line | Demonstrated BMP2-like activity of p.Arg438Leu | Not a joint-interzone cell |
| “Digits in a dish” | 3D/in vitro embryonic-limb culture | Produces Gdf5-positive interzone-like regions and allows single-cell analysis | No published SYM1B variant correction or drug screen yet |
| Zebrafish *gdf5* CRISPR mutant | Vertebrate loss-of-function | Fin endoskeletal segmentation and cartilage/ossification studies | Limited direct phenotypic similarity |

The L367R knock-in abstract reports:

> “*Gdf5* L367R/+ and *Gdf5* L367R/L367R mice displayed stiffness and adhesions across the proximal phalanx joint which were in complete accord with SYM1.”

[Zhang et al., 2017, PMID 29371961](https://pmc.ncbi.nlm.nih.gov/articles/PMC5768378/). [60]

---

## Recent developments and expert assessment

1. **2023 nosology:** The International Skeletal Dysplasia Society’s 2023 revision adopted gene–phenotype dyadic naming to reduce ambiguity among clinically similar skeletal disorders—directly supporting use of “*GDF5*-related proximal symphalangism” rather than the phenotype name alone. The revision contains 771 disorders associated with 552 genes. [Published February 13, 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10081954/). [374][380]

2. **2023 GDF5 allelic-spectrum report:** A p.Ser475Asn family had combined brachydactyly A1 and multiple synostoses syndrome 2. This is not canonical SYM1B, but it reinforces the expert view that *GDF5* disorders form a mechanism-dependent continuum and that activating mature-domain variants can produce overlapping joint-fusion phenotypes. [Published online November 28, 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10782059/). [19]

3. **2024 human developmental multi-omics:** A multi-omic human embryonic skeletal atlas resolved GDF5-high interzone populations during the 5–11-week postconception period, strengthening the cellular context in which activating *GDF5* variants are expected to act. It did not include SYM1B patients. [Published November 20, 2024](https://www.nature.com/articles/s41586-024-08189-z). [313]

4. **Current expert gene validity:** GenCC regards the autosomal-dominant *GDF5*–SYM1B relationship as definitive, and clinical skeletal-dysplasia/limb panels consistently include *GDF5*. [108][316]

5. **Major evidence gap:** No 2023–2024 SYM1B-specific cohort, interventional trial, patient-derived iPSC model, organoid, CRISPR rescue study, single-cell patient analysis or prospective natural-history study was identified. The core clinical evidence therefore still rests on the 2005, 2006, 2008 and 2016 pedigrees, supported by functional studies and the 2017 knock-in mouse.

---

## Knowledge-base summary

- **Disease:** Symphalangism, proximal, 1B  
- **MONDO:** MONDO:0014125  
- **OMIM:** 615298  
- **Causal gene:** **GDF5**, HGNC:4220, OMIM 601146  
- **Inheritance:** autosomal dominant  
- **Mechanism:** heterozygous activating/gain-of-function missense variants  
- **Core phenotype:** congenital proximal interphalangeal fusion with variable carpal/tarsal synostosis  
- **Canonical pathogenic variants:** p.Arg438Leu, p.Glu491Lys and p.Leu373Arg  
- **Primary pathway:** GDF5–BMPR1B/BMPR1A–SMAD1/5/8 signaling  
- **Primary cells:** embryonic joint-interzone mesenchymal progenitors and chondrocytes  
- **Diagnosis:** examination and radiography plus allele-aware molecular testing of *GDF5*; include *NOG* in the differential  
- **Treatment:** symptom-directed orthoses, rehabilitation, analgesia, and selected orthopedic procedures  
- **Prognosis:** normal survival; variable lifelong limb stiffness, with foot pain and secondary arthritis representing the main morbidity in some families  
- **Prevention:** genetic counseling, cascade testing, and optional targeted prenatal diagnosis or PGT-M  
- **Best disease model:** heterozygous *Gdf5* p.Leu367Arg knock-in mouse.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 20 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| Quoted claims checked | 3 |
| Quoted claims found in source | 2 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 19 |
| On topic | 12 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `DOI:10.1371/journal.pgen.1000747&type=printable` (1 mention) - Identifier did not resolve to a record

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:29371961` *(abstract only)*: "*Gdf5* L367R/+ and *Gdf5* L367R/L367R mice displayed stiffness and adhesions across the proximal phalanx joint which were in complete accord with SYM1."
  - closest text in source: "Gdf5L367R/+ and Gdf5L367R/L367R mice displayed stiffness and adhesions across the proximal phalanx joint which were in complete accord with SYM1"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 64 |
| Resolved | 60 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 3 |
| Terms whose name was checked | 23 |
| Terms named correctly | 9 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 11 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014125` (3 mentions) - the report calls it "MONDO"; MONDO calls it **symphalangism, proximal, 1B**
- `HP:0025233` (1 mention) - the report calls it "Foot pain"; HP calls it **Sleep paralysis**
- `GO:0061317` (1 mention) - the report calls it "GO—joint morphogenesis"; GO calls it **obsolete canonical Wnt signaling pathway involved in cardiac muscle cell fate commitment**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0061317` (obsolete canonical Wnt signaling pathway involved in cardiac muscle cell fate commitment) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0100264` (2 mentions) - the report calls it "Proximal symphalangism—physical sign"; HP calls it **Proximal symphalangism**
- `HP:0005048` (1 mention) - the report calls it "Carpal synostosis"; HP calls it **Synostosis of carpal bones**
- `HP:0008368` (1 mention) - the report calls it "Tarsal synostosis/coalition"; HP calls it **Tarsal synostosis**
- `HP:0001763` (1 mention) - the report calls it "Pes planus/planovalgus"; HP calls it **Pes planus**
- `HP:0100490` (1 mention) - the report calls it "Camptodactyly"; HP calls it **Camptodactyly of finger**, and lists "Camptodactyly of hands" among its other names
- `HP:0002758` (1 mention) - the report calls it "Secondary osteoarthritis"; HP calls it **Osteoarthritis**
- `GO:0030509` (1 mention) - the report calls it "GO—BMP signaling"; GO calls it **BMP signaling pathway**
- `GO:0002062` (1 mention) - the report calls it "GO—chondrocyte differentiation"; GO calls it **chondrocyte differentiation**
- `GO:0051216` (1 mention) - the report calls it "GO—cartilage development"; GO calls it **cartilage development**
- `GO:0001501` (1 mention) - the report calls it "GO—skeletal system development"; GO calls it **skeletal system development**
- `GO:0001958` (1 mention) - the report calls it "GO—endochondral ossification"; GO calls it **endochondral ossification**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.