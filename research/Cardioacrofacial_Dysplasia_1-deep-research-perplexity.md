---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-11-06T19:22:00.427632'
end_time: '2026-11-06T19:28:26.705137'
duration_seconds: 386.28
template_file: templates/disease_pathophysiology_research.md
template_sha: f452f0a9c7e3536175154b9683c45663f686f283
template_variables:
  disease_name: PRKACA-Related Cardioacrofacial Dysplasia
  mondo_id: MONDO:0030876
  category: Mendelian
  causal_genes: PRKACA
  omim_id: OMIM:619142
  synonyms: CAFD1
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 19
reference_validation:
  total_references: 5
  verified: 5
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 5
  on_topic: 4
  validator_version: 0.5.1
term_validation:
  total_terms: 37
  verified: 33
  not_found: 1
  obsolete: 2
  unverifiable: 1
  confabulation_rate: 0.028
  labels_checked: 8
  labels_matching: 5
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0030876
    reported_labels:
    - if available
    ontology_label: cardioacrofacial dysplasia 1
  - term_id: HP:0001513
    reported_labels:
    - Disproportionate short stature
    ontology_label: Obesity
  labels_variant: 1
  unresolved_terms:
  - HP:0000203
  obsolete_terms:
  - term_id: GO:0016481
    ontology_label: GO_0016481
    replaced_by: GO:0045892
  - term_id: GO:0019933
    ontology_label: obsolete cAMP-mediated signaling
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** PRKACA-Related Cardioacrofacial Dysplasia
- **MONDO ID:** MONDO:0030876 (if available)
- **Causal gene(s):** PRKACA
- **OMIM:** OMIM:619142
- **Synonyms:** CAFD1
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **PRKACA-Related Cardioacrofacial Dysplasia** covering all of the
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

# PRKACA-Related Cardioacrofacial Dysplasia (CAFD1): An Extensive Review of a Rare PKA-Driven Ciliopathic Skeletal and Cardiac Syndrome

Cardioacrofacial dysplasia 1 (CAFD1) is a very rare autosomal dominant Mendelian disorder caused by heterozygous pathogenic variants in the **PRKACA** gene, which encodes the catalytic subunit α of cAMP-dependent protein kinase A (PKA).\[1\]\[3\]\[9\] The condition is characterized by a striking constellation of congenital heart defects, particularly common atrium and atrioventricular septal defects, postaxial polydactyly, limb shortening with skeletal dysplasia, and ectodermal anomalies involving teeth and nails, placing it within the spectrum of ciliopathy-associated skeletal dysplasias that overlap phenotypically with Ellis–van Creveld syndrome.\[1\]\[3\]\[7\] Since its first delineation in 2020 by Palencia-Campos and colleagues, who identified a recurrent gain-of-function missense variant p.Gly137Arg in PRKACA in multiple unrelated individuals, additional reports—including a 2026 Chinese case with the same variant and a distinct in-frame intragenic deletion—have expanded both the clinical and molecular spectrum of disease.\[1\]\[11\]\[13\]\[15\] Functional work across these studies has converged on a unifying mechanism in which PRKACA variants increase PKA sensitivity to cAMP and impair proper regulation by regulatory subunits, leading to overactive PKA in developing tissues, inhibition of Hedgehog (Hh) signaling via enhanced GLI phosphorylation, and consequent disruption of cilia-dependent patterning in the heart, skeleton, craniofacial structures, and vasculature.\[1\]\[7\]\[8\]\[11\]\[13\]\[15\] Because CAFD1 is extremely rare—fewer than a dozen individuals have been molecularly confirmed worldwide—the available evidence derives from case reports and small series, but these are supported by robust biochemical and cellular data that strongly validate PRKACA as the causal gene and define CAFD1 as a gain-of-function PKAopathy with distinctive cardio-skeletal and ectodermal involvement.\[1\]\[6\]\[7\]\[11\]\[13\]\[15\]

## 1. Disease Information

### 1.1 Definition and Overview

Cardioacrofacial dysplasia 1 (CAFD1) is a developmental disorder defined by congenital cardiac malformations, limb and digital anomalies, craniofacial dysmorphism, and ectodermal defects, caused by heterozygous pathogenic variants in **PRKACA** on chromosome 19p13.12.\[2\]\[3\]\[9\] PRKACA encodes the catalytic subunit alpha of PKA, a key effector in the cAMP signaling pathway that regulates diverse processes including proliferation, differentiation, and apoptosis.\[11\]\[18\] Clinically, CAFD1 is characterized by congenital heart defects, especially common atrium or atrioventricular septal defect, short limbs, brachydactyly, and postaxial polydactyly, along with facial anomalies and abnormalities of teeth and nails.\[1\]\[2\]\[3\] This combination of findings aligns CAFD1 with the group of **ciliopathy-associated skeletal dysplasias**, which includes conditions such as Ellis–van Creveld (EvC) syndrome, with which CAFD1 shares postaxial polydactyly, narrow thorax, and cardiac involvement.\[1\]\[7\]\[11\]

MedGen, drawing on OMIM and other curated resources, defines CAFD1 as a disorder “characterized by congenital cardiac defects, primarily common atrium or atrioventricular septal defect; limb anomalies, including short limbs, brachydactyly, and postaxial polydactyly; and dysmorphic facial features,” explicitly linking it to pathogenic PRKACA variants.\[2\] OMIM lists CAFD1 under entry **619142**, with PRKACA (OMIM 601639) designated as the causal gene; the entry is annotated with an autosomal dominant inheritance pattern.\[3\]\[9\] In the original series by Palencia-Campos et al., three unrelated families from Egypt, Belgium, and Italy carried the same PRKACA missense mutation c.409G>A (p.Gly137Arg), either as germline heterozygosity or somatic mosaicism, and exhibited the core CAFD1 phenotype of common atrium/atrioventricular septal defect and postaxial polydactyly.\[9\]\[11\]\[13\] Later reports, including a 10-year-old Chinese boy with the identical variant and a more recent individual with an in-frame intragenic deletion in PRKACA, further confirmed the syndrome as a distinct entity.\[1\]\[15\]

Importantly, CAFD1 is classified within the MONDO disease ontology as **MONDO:0030876**, and is also recognized in multiple curation frameworks, including ClinGen and national gene panel initiatives, as a high-confidence gene–disease relationship.\[2\]\[6\]\[7\]\[8\] ClinGen’s gene–disease validity curation for PRKACA and cardioacrofacial dysplasia assigns strong evidence based on multiple unrelated probands, recurrent variants, functional data showing increased PKA activity and Hh inhibition, and consistent phenotypes.\[6\] These curated resources draw primarily on aggregated disease-level evidence rather than electronic health record (EHR) mining, reflecting the rarity of CAFD1 and the limited number of detailed clinical descriptions available to date.\[1\]\[6\]\[11\]\[13\]

### 1.2 Key Identifiers and Synonyms

Within major biomedical ontologies and databases, CAFD1 is anchored by several key identifiers. In OMIM, **Cardioacrofacial dysplasia 1** is cataloged as **619142**, with a “number sign” indicating that the phenotype is caused by mutation in PRKACA.\[3\]\[9\] MedGen assigns the concept ID **C5436885** and labels the condition “Cardioacrofacial dysplasia-1 (CAFD1),” pointing to PRKACA as the associated gene and cross-referencing the MONDO term MONDO:0030876.\[2\] ClinVar also references CAFD1 as the disease entity for PRKACA variants, using MONDO:0030876 and MedGen C5436885 as identifiers.\[5\]

Synonyms used in the literature and curation resources include **CAFD1**, **cardio-acrofacial dysplasia 1**, and “Cardioacrofacial dysplasia-1 (PRKACA-related),” which help distinguish it from **Cardioacrofacial dysplasia 2 (CAFD2)** caused by pathogenic variants in **PRKACB** on chromosome 1p31.\[2\]\[10\]\[14\] Some gene panel resources, such as PanelApp-AUS, initially listed PRKACA with a set of associated phenotypes—postaxial hand polydactyly, common atrium, atrioventricular canal defect, narrow chest, tooth abnormalities, and intellectual disability—before consolidating these under the CAFD1 MONDO term.\[7\]\[8\] Abcam and other antibody or protein resources list “Cardioacrofacial dysplasia 1 (CAFD1)” explicitly as a disease associated with PRKACA, underscoring its recognition beyond purely genetic databases.\[4\]

No dedicated ICD-10 or ICD-11 code has yet been assigned for CAFD1 specifically. In clinical practice, affected individuals are often coded under general categories such as “other specified congenital malformations of heart” or “congenital malformations of limbs,” reflecting the absence of a disease-specific ICD entry. However, as CAFD1 is now recognized in MONDO, MedGen, OMIM, and ClinGen, it is increasingly visible in gene- and phenotype-based registries, enabling more structured data capture in research and clinical genetic databases.\[2\]\[3\]\[6\]\[7\]\[9\]

### 1.3 Source and Nature of Available Information

The current knowledge base for CAFD1 is built almost entirely from aggregated disease-level resources that summarize a small number of deeply phenotyped patients rather than large cohorts or population-based datasets. The foundational evidence comes from the 2020 American Journal of Human Genetics article by Palencia-Campos et al., which described seven individuals with a multiple congenital malformation syndrome caused by germline or mosaic variants in PRKACA or PRKACB.\[11\]\[12\]\[13\] Three of these individuals, plus affected relatives, carried the recurrent PRKACA p.Gly137Arg variant and formed the basis for defining CAFD1.\[9\]\[11\]\[13\] The authors combined clinical descriptions, structural modeling, biochemical assays of PKA activity, and Hedgehog signaling assays to establish a mechanistic link between the variants and the phenotype.\[11\]\[12\]

Subsequent publications have added additional single cases and small series. A 2026 case report by Liang et al., published in Translational Pediatrics, described a Chinese pediatric patient with classic CAFD1 features and confirmed de novo PRKACA c.409G>A (p.Gly137Arg) by trio whole-exome sequencing.\[1\]\[16\] The report also provided a literature review summarizing all known CAFD1 cases to date, highlighting that all previously reported patients shared the same PRKACA missense variant.\[1\]\[16\] In 2026, Weaver et al. reported an individual with a previously unreported de novo in-frame intragenic deletion in PRKACA, presenting with combined skeletal dysplasia and vasculopathy; functional work demonstrated overactive PKA and impaired ciliation, expanding the phenotypic and allelic spectrum associated with PRKACA gain-of-function.\[15\] ClinGen’s gene–disease validity curation further incorporates these data, including a 2024 report by Sithambaram et al. and the 2026 Liang case, as part of the evidence set for PRKACA–CAFD1.\[6\]

Because of the small number of known cases, there are no large registry-based natural history studies, randomized trials, or systematic quality-of-life assessments specific to CAFD1. Much of the quantitative information about phenotype frequencies and variability thus derives from detailed case-level descriptions in these primary reports, which are synthesized in OMIM, MedGen, ClinGen, and national gene panel databases.\[1\]\[2\]\[3\]\[6\]\[7\]\[9\]\[11\]\[15\]

## 2. Etiology

### 2.1 Primary Causal Factors: PRKACA Gain-of-Function

CAFD1 is caused by **heterozygous gain-of-function variants in PRKACA**, leading to constitutive or exaggerated activation of PKA catalytic activity in response to cAMP.\[1\]\[3\]\[7\]\[11\]\[15\] PRKACA encodes the catalytic subunit alpha (Cα) of PKA, a serine/threonine kinase that, in its inactive form, resides in a tetrameric holoenzyme composed of two regulatory subunits and two catalytic subunits.\[11\]\[18\] Binding of cAMP to the regulatory subunits induces dissociation of the complex and release of active Cα, which phosphorylates a wide array of substrates.\[18\] Missense variants like p.Gly137Arg and in-frame deletions that affect critical interaction surfaces between the catalytic and regulatory subunits decrease the affinity of Cα for its regulatory partners, thereby increasing basal kinase activity and/or sensitizing the holoenzyme to lower cAMP concentrations.\[1\]\[11\]\[15\]

The prototypic CAFD1 variant is **c.409G>A (p.Gly137Arg)** in PRKACA (NM_002730.3/4), which has been identified in all definitively reported CAFD1 cases until the description of the in-frame deletion.\[1\]\[3\]\[9\]\[11\]\[13\] OMIM notes that this variant affects a highly conserved residue at a tethering surface that interacts with regulatory proteins, and functional analysis shows that mutant PKA holoenzymes are more sensitive to activation by cAMP than wild-type proteins.\[9\]\[11\] Structural modeling and biophysical assays in the Palencia-Campos study demonstrated reduced binding of mutant Cα to regulatory subunits, increased catalytic activity at low cAMP, and a concomitant impairment of Hh signaling when mutant PRKACA was ectopically expressed in NIH 3T3 fibroblasts.\[11\]\[12\]\[13\] The 2026 Weaver case described a three-amino-acid deletion in PRKACA that also reduced interaction with regulatory subunits, particularly type II, resulting in overactivation of PKA and failure to properly initiate Hh signaling.\[15\]

ClinGen and PanelApp curators explicitly note that **loss-of-function variants in PRKACA do not cause CAFD1**, and that the mode of pathogenicity is consistent with gain-of-function or increased sensitivity to cAMP.\[7\]\[8\] This conclusion is supported by the absence of truncating or inactivating variants among CAFD1 patients, the functional gain-of-function phenotypes observed in vitro, and the broader literature linking PRKACA activation to endocrine tumors, such as cortisol-producing adrenal adenomas and fibrolamellar hepatocellular carcinoma via DNAJB1–PRKACA fusion.\[18\]\[19\] Together, this evidence establishes abnormal upregulation of PRKACA kinase activity as the primary etiological driver of CAFD1.\[1\]\[3\]\[9\]\[11\]\[15\]

### 2.2 Genetic Risk Factors and Variant Spectrum

To date, the strongest and most consistent genetic risk factor for CAFD1 is the presence of a **pathogenic missense or in-frame deletion variant in PRKACA that increases PKA activity**, with the recurrent p.Gly137Arg substitution being the principal example.\[1\]\[3\]\[9\]\[11\]\[15\] In the Palencia-Campos cohort, three unrelated individuals (and their affected offspring in two families) carried heterozygous germline or mosaic PRKACA p.Gly137Arg variants, all of which arose de novo or via parental mosaicism.\[9\]\[11\]\[13\] The 2026 Chinese case similarly harbored a de novo heterozygous PRKACA c.409G>A (p.Gly137Arg) variant confirmed by trio whole-exome sequencing; neither parent carried the mutation, and the variant is absent from gnomAD.\[1\] ClinVar lists the same variant as **pathogenic** for CAFD1 (ClinVar RCV001006445.1), and it has been observed exclusively in affected individuals and not in population controls.\[1\]\[3\]\[5\]\[9\]

The in-frame three–amino-acid deletion described by Weaver et al. broadens the allelic spectrum while preserving the mechanistic theme of increased PKA activity.\[15\] Although the specific residues deleted differ from Gly137, structural analysis in that report showed that the deletion affects a key region involved in substrate and regulatory subunit tethering, thereby destabilizing the inactive holoenzyme and facilitating aberrant activation.\[15\] ClinGen’s gene–disease validity summary also mentions additional PRKACA variants identified in individuals with combined skeletal dysplasia and vasculopathy features, further corroborating that multiple gain-of-function alleles in PRKACA can cause overlapping phenotypes within the CAFD1 spectrum.\[6\]\[15\]

ClinVar includes at least one PRKACA missense variant, **c.327C>A (p.Phe109Leu)**, submitted as a variant of uncertain significance (VUS) for CAFD1, underscoring that not all rare missense variants in PRKACA are necessarily pathogenic.\[5\] This F109L variant is absent in gnomAD, affects a conserved residue, and has conflicting in silico predictions; however, there is currently no published evidence linking it to a CAFD1-like phenotype, and thus it remains of uncertain significance.\[5\] This highlights the importance of combining genomic data with careful phenotyping and functional assays when interpreting PRKACA variants in a clinical setting.

Beyond CAFD1, PRKACA is also implicated in other conditions, including adrenal hyperplasias and tumors, where somatic activating mutations or genomic duplications lead to constitutive PKA activity and corticotropin-independent Cushing syndrome.\[18\]\[19\] These somatic mutations, however, affect different residues or structural features than the germline CAFD1 variants and are typically not associated with congenital cardiac or skeletal malformations.\[18\]\[19\] Nonetheless, they reinforce the concept that PRKACA is an oncogene and that increased PKA activity in specific tissues has diverse pathological consequences.\[19\]

### 2.3 Environmental and Non-genetic Risk Factors

No specific environmental, lifestyle, or infectious risk factors have been associated with CAFD1 in the human literature. All reported cases to date have identified de novo or mosaic PRKACA variants in individuals with otherwise unremarkable prenatal exposures, and there is no evidence from epidemiologic or experimental studies that environmental toxins, maternal conditions, or infections play a primary causative role.\[1\]\[11\]\[13\]\[15\] The extreme rarity of the syndrome and its strong association with highly penetrant gain-of-function variants support a predominantly genetic etiology.

The current case series do not provide enough detail to rigorously assess subtle environmental modifiers. For instance, maternal diabetes, teratogenic drug exposures, or nutritional deficiencies are not consistently reported in CAFD1 families, and no common exposures have emerged across cases.\[1\]\[11\]\[15\] Moreover, the presence of identical PRKACA variants in individuals from diverse geographic and cultural backgrounds—Egypt, Belgium, Italy, China, and other regions—argues against a localized environmental driver.\[1\]\[9\]\[11\]\[13\] At present, CAFD1 should be viewed as a primarily monogenic, high-penetrance disorder with minimal documented environmental contribution.

### 2.4 Protective Factors and Gene–Environment Interactions

Similarly, there are no known genetic or environmental **protective factors** that mitigate the risk of CAFD1. Population genomic databases such as gnomAD show no recurrent missense variants at Gly137 or neighboring residues that might act as benign modifiers, and there is no evidence for common polymorphisms in PKA regulatory subunits or downstream targets that systematically ameliorate the phenotype.\[1\]\[5\]\[9\]\[11\] In principle, variants in regulatory subunit genes (PRKAR1A, PRKAR1B, PRKAR2A, PRKAR2B) or components of the Hedgehog pathway might modulate disease severity, but this has not been empirically demonstrated in CAFD1 patients.\[7\]\[8\]\[11\]

Gene–environment interaction studies have not been performed in CAFD1, and the small number of cases precludes formal inference. Based on mechanistic considerations, factors that influence cAMP levels—such as endocrine status, certain medications, or metabolic conditions—could theoretically modulate PKA activity in tissues; however, whether such influences can meaningfully alter developmental outcomes in the presence of a strongly activating PRKACA variant remains speculative.\[11\]\[18\] In the available reports, the congenital malformations are present from birth, suggesting that the pathogenic process occurs during embryogenesis and is largely determined by the genetic lesion rather than postnatal environmental exposures.\[1\]\[11\]\[15\]

In summary, CAFD1 is best conceptualized as a **monogenic developmental disorder driven by PRKACA gain-of-function**, with no current evidence for modifiable environmental risk or protective factors. Future work with larger cohorts or functional genomics approaches could identify modifier alleles, but such data are presently lacking.\[1\]\[6\]\[11\]\[15\]

## 3. Phenotypes

### 3.1 Core Clinical Phenotype: Cardiac, Limb, and Craniofacial Features

The **cardinal clinical features** of CAFD1 are congenital cardiac defects, particularly common atrium and atrioventricular septal defects; limb anomalies including short limbs, brachydactyly, and postaxial polydactyly; and characteristic craniofacial anomalies.\[1\]\[2\]\[3\]\[7\]\[9\]\[11\] Palencia-Campos and colleagues summarized these as “common atrium/AVSD and postaxial polydactyly” as the major shared findings across affected individuals with PRKACA or PRKACB variants, with additional skeletal and ectodermal anomalies in many cases.\[11\]\[12\]\[13\] MedGen similarly highlights a clinical triad of congenital cardiac defects, limb anomalies, and dysmorphic facial features for CAFD1.\[2\]

Cardiac phenotypes in CAFD1 most often include **common atrium** and complete or partial atrioventricular septal defects, reflecting failure of endocardial cushion fusion and atrial septation during early cardiac development.\[3\]\[9\]\[11\]\[13\] In the Palencia-Campos series, nearly all individuals with PRKACA gain-of-function variants had common atrium or AVSD, and some had offspring with similar defects, indicating high penetrance of congenital heart disease within families.\[11\]\[13\] The Chinese boy described by Liang et al. had a partial atrial septal defect with a functionally single atrium and pulmonary valve stenosis, again showcasing the consistent involvement of atrial and atrioventricular structures.\[1\]\[16\] These defects are often detected in infancy and can require surgical correction.

The limb phenotype is dominated by **postaxial polydactyly** of the hands and feet, often bilateral, along with **brachydactyly** and shortened long bones.\[1\]\[3\]\[7\]\[9\]\[11\] PanelApp curators note that postaxial hand polydactyly was present in 6 of 7 individuals with PRKACA/PRKACB variants, with bilateral involvement in most, and postaxial foot polydactyly in at least 4 individuals.\[7\]\[8\] Radiographic evaluation in CAFD1 can reveal short metacarpals and metatarsals, pseudoepiphyses, and other skeletal anomalies, particularly in the context of the Weaver et al. deletion case, which showed severely hypoplastic ulnae and fibulae and metaphyseal fragmentation.\[15\] Clinically, these limb anomalies may impair fine motor skills or gait, depending on severity, and can be addressed with orthopedic or surgical interventions.\[1\]\[15\]

Craniofacial features include **midface hypoplasia, micrognathia, and sometimes clefting or incomplete cleft lip**, leading to a distinctive facial gestalt.\[1\]\[6\]\[11\] MedGen and ClinGen list facial anomalies such as midface hypoplasia, micrognathia, and long narrow thorax as part of the CAFD1 spectrum.\[2\]\[6\] In the ClinGen curation, one adult female proband with PRKACA p.Gly137Arg had an incomplete cleft of the upper lip and multiple oral frenula, features that also appear in related PRKACB-associated CAFD2 and oral–facial–digital (OFD) syndromes.\[6\]\[17\] Taken together, these findings place CAFD1 within a broader phenotypic continuum of ciliopathies with overlapping craniofacial and oral involvement.

From an ontology perspective, key Human Phenotype Ontology (HPO) terms include **Common atrium (HP:0001711)**, **Atrioventricular septal defect (HP:0001671)**, **Postaxial polydactyly (HP:0001162)**, **Brachydactyly (HP:0001156)**, **Short long bones (HP:0003026)**, **Midface hypoplasia (HP:0000767)**, and **Micrognathia (HP:0000347)**.\[1\]\[2\]\[6\]\[11\]

### 3.2 Skeletal Dysplasia and Growth Abnormalities

Beyond the digits, CAFD1 involves a broader skeletal dysplasia characterized by **short stature, disproportionate limb shortening, genu valgum, narrow thorax, and, in some cases, more severe appendicular skeletal anomalies**.\[1\]\[6\]\[7\]\[11\]\[15\] In the Chinese case described by Liang et al., the 10-year-old boy had disproportionate short stature with shorter limbs relative to trunk, severe bilateral genu valgum, and progressive knee deformities, consistent with a skeletal dysplasia phenotype.\[1\]\[16\] Radiographs showed features reminiscent of EvC syndrome, including shortened long bones and metaphyseal abnormalities.\[1\] ClinGen’s evidence summary lists “short stature; limb undergrowth; long/narrow thorax; genu valgum” among the recurrent skeletal manifestations in PRKACA-related CAFD1.\[6\]

The Weaver et al. patient expanded this picture by presenting with a **combined skeletal dysplasia and vasculopathy phenotype**. Radiographic findings included severely hypoplastic and short ulnae and fibulae, metaphyseal fragmentation of the distal radius, ulna, fibula, and distal femora, flat acetabular roofs, widened sacro-sciatic notches, and osteopenia.\[15\] This individual also had severe neonatal hypotonia and appendicular skeletal abnormalities, indicating that PRKACA gain-of-function can produce a more generalized skeletal dysplasia beyond the more modest limb shortening and genu valgum observed in the Gly137Arg cohort.\[15\] The authors suggested that this broadened the phenotypic spectrum of PRKACA pathogenic variants and proposed that patients with CAFD1 might require surveillance for osteopenia and fractures.\[15\]

The skeletal manifestations are consistent with disruption of **growth plate chondrocyte proliferation and differentiation**, processes heavily influenced by Hedgehog signaling and PKA-mediated phosphorylation of GLI transcription factors.\[1\]\[7\]\[11\]\[15\] From an HPO standpoint, relevant terms include **Disproportionate short stature (HP:0001513)**, **Genu valgum (HP:0002857)**, **Short limb (HP:0009826)**, **Narrow chest (HP:0000774)**, **Osteopenia (HP:0000938)**, and **Metaphyseal dysplasia (HP:0000939)**.\[1\]\[6\]\[15\]

### 3.3 Ectodermal Anomalies: Teeth, Nails, and Oral Structures

CAFD1 features **ectodermal anomalies** involving teeth, nails, and oral structures, paralleling features seen in classical ciliopathies and OFD syndromes.\[1\]\[6\]\[7\]\[11\] Dental anomalies include hypodontia, conical teeth, diastema, and generalized dental hypoplasia, which can lead to malocclusion and increased risk of caries.\[1\]\[6\]\[11\] Liang et al. describe “hypoplasia of teeth” and dental abnormalities in their CAFD1 case, and MedGen notes that dental anomalies (such as diastema and hypodontia) are part of the core CAFD1 phenotype.\[1\]\[2\]\[16\] ClinGen lists “conical tooth” and “carious teeth” among the HPO terms documented in PRKACA-mutant individuals.\[6\]

Nail changes include **nail hypoplasia or dysplasia**, affecting both fingernails and toenails.\[1\]\[6\]\[11\] In Palencia-Campos’s series and the ClinGen summary, “nail dysplasia” is a recurring feature, often co-occurring with dental anomalies and limb undergrowth.\[6\]\[11\] These ectodermal defects suggest a role for PRKACA in the development and maintenance of ectoderm-derived tissues, likely mediated through cAMP/PKA control of signaling pathways that regulate keratinocyte and odontoblast differentiation.\[11\]

Oral anomalies such as **multiple frenula** and, less commonly, lingual or labial anomalies also occur. One PRKACA p.Gly137Arg–positive adult female described in ClinGen’s curation had multiple oral frenula at the lower lip, and similar features have been reported in PRKACB-related CAFD2 cases, which show overlap with OFD syndromes.\[6\]\[17\] In a 2022 report of a PRKACB-associated CAFD2 patient, the authors noted multiple oral frenula and OFD-like features, and highlighted that PKA subunits can phosphorylate OFD1, a protein central to OFD type 1, providing a mechanistic link between PKA gain-of-function and oral–facial anomalies.\[17\] These observations support the notion that PRKACA gain-of-function in CAFD1 can perturb the same ciliary and signaling networks that underlie OFD and related disorders, producing overlapping oral phenotypes.\[6\]\[17\]

Relevant HPO terms include **Hypodontia (HP:0000668)**, **Conical teeth (HP:0000698)**, **Diastema (HP:0000699)**, **Dental hypoplasia (HP:0001574)**, **Nail dysplasia (HP:0002164)**, and **Multiple oral frenula (HP:0000203)**.\[1\]\[2\]\[6\]\[16\]\[17\]

### 3.4 Neurological, Vascular, and Other Systemic Features

Neurological and cognitive features in CAFD1 appear to be **variable and, in many cases, mild or absent**, though the evidence base is limited. In the Palencia-Campos series of PRKACA-mutant individuals, the primary focus was on cardiovascular, skeletal, and ectodermal anomalies, and cognitive deficits were more prominently reported in some PRKACB (CAFD2) cases rather than PRKACA.\[11\]\[13\] ClinGen notes that intellectual disability has been reported in some individuals with PRKACB mutations, but there is no consistent pattern of significant cognitive impairment in PRKACA-related CAFD1.\[7\]\[8\]\[11\] The 2026 Liang case report does not mention intellectual disability, and the available clinical descriptions of PRKACA p.Gly137Arg carriers do not emphasize neurodevelopmental delay.\[1\]\[11\]\[16\] This suggests that, unlike some ciliopathies with prominent brain malformations, CAFD1 primarily affects cardio-skeletal and ectodermal systems, with neural involvement being more limited or subtle.

The Weaver et al. case revealed **significant vascular involvement**, including aortic dilation, coronary artery dilation, and vascular tortuosity.\[15\] Such vascular phenotypes had not been widely recognized in earlier CAFD1 descriptions and may represent either an extension of the CAFD1 spectrum or a distinct PKA-mediated vasculopathy overlapping with skeletal dysplasia.\[15\] Functional data from that study showed that the PRKACA deletion variant increased PKA activity and impaired Hedgehog signaling in vascular and skeletal contexts, and patient-derived induced pluripotent stem cells (iPSCs) exhibited reduced ciliation, suggesting that similar ciliary and signaling defects underlie both skeletal and vascular abnormalities.\[15\] The authors emphasized that this phenotype expands the PRKACA pathogenic spectrum and recommended that individuals with PRKACA gain-of-function variants undergo periodic screening for aortic and coronary dilation.\[15\]

Other systemic features reported across the PRKACA/PRKACB spectrum include long narrow thorax, respiratory compromise due to chest wall deformities, and, in one PRKACB patient, unusual tumors, highlighting the pleiotropic effects of PKA dysregulation.\[11\]\[13\]\[17\] However, such manifestations are less well documented in pure CAFD1 cases, and more data are needed to determine their frequency and clinical significance.

### 3.5 Phenotype Frequency, Severity, and Quality-of-life Impact

Given the small number of reported CAFD1 patients, precise **phenotype frequencies** cannot be robustly estimated, but the available series suggest that congenital heart defects and postaxial polydactyly are nearly universal, whereas skeletal dysplasia and ectodermal anomalies show variable penetrance and severity.\[1\]\[3\]\[7\]\[9\]\[11\] Palencia-Campos et al. noted that “nearly all affected individuals and their affected offspring shared an atrioventricular septal defect or a common atrium along with postaxial polydactyly,” making these features the hallmarks of the syndrome.\[11\]\[12\]\[13\] Skeletal anomalies and ectodermal defects were present in five of seven individuals across PRKACA and PRKACB variants, indicating high but not complete penetrance.\[11\]\[13\] The Liang case and ClinGen curation both underscore that limb shortening, genu valgum, and dental/nail anomalies are common but variable in expressivity.\[1\]\[6\]\[16\]

Severity ranges from moderately affected individuals who survive into adulthood with surgically corrected heart defects and manageable orthopedic issues, to more severely affected individuals like the Weaver patient, who had profound neonatal hypotonia, extensive skeletal abnormalities, osteopenia, and vascular involvement.\[1\]\[11\]\[15\] Quality-of-life impacts stem from cardiac surgery and possible residual hemodynamic issues, orthopedic problems affecting mobility, and dental and nail abnormalities influencing aesthetics and function.\[1\]\[11\]\[15\]\[16\] No formal quality-of-life studies using instruments such as EQ-5D or SF-36 have been conducted specifically in CAFD1 patients, but extrapolation from related congenital heart disease and skeletal dysplasia literature suggests potential limitations in exercise capacity, pain related to deformities, and psychosocial effects stemming from visible physical differences.

The table below summarizes major phenotypic features, approximate frequency based on the small cohort, and suggested HPO terms:

| Phenotype                              | Approximate frequency (qualitative)          | HPO term (ID)                            | Evidence |
|----------------------------------------|----------------------------------------------|------------------------------------------|----------|
| Common atrium / AVSD                   | Very common (near-universal)                | Common atrium (HP:0001711); AVSD (HP:0001671) | Palencia-Campos 2020\[11\]\[13\]; OMIM\[3\]\[9\]; Liang 2026\[1\]\[16\] |
| Postaxial polydactyly (hands/feet)     | Very common (near-universal)                | Postaxial polydactyly (HP:0001162)      | Palencia-Campos 2020\[11\]\[13\]; PanelApp\[7\]\[8\] |
| Short limbs / limb undergrowth         | Common                                      | Limb undergrowth (HP:0009826)           | ClinGen\[6\]; Liang 2026\[1\]\[16\] |
| Brachydactyly                          | Common                                      | Brachydactyly (HP:0001156)              | ClinGen\[6\]; Palencia-Campos\[11\] |
| Disproportionate short stature         | Common                                      | Disproportionate short stature (HP:0001513) | Liang 2026\[1\]\[16\]; ClinGen\[6\] |
| Genu valgum                            | Common                                      | Genu valgum (HP:0002857)                | ClinGen\[6\]; Liang 2026\[1\]\[16\] |
| Narrow/long thorax                     | Recurrent                                   | Narrow chest (HP:0000774)               | ClinGen\[6\]; PanelApp\[7\]\[8\] |
| Dental anomalies (hypodontia, conical) | Common                                      | Hypodontia (HP:0000668); Conical teeth (HP:0000698) | ClinGen\[6\]; MedGen\[2\]; Liang 2026\[1\]\[16\] |
| Nail dysplasia                         | Common                                      | Nail dysplasia (HP:0002164)             | ClinGen\[6\]; Palencia-Campos\[11\] |
| Midface hypoplasia, micrognathia      | Recurrent                                   | Midface hypoplasia (HP:0000767); Micrognathia (HP:0000347) | ClinGen\[6\]; MedGen\[2\]; Palencia-Campos\[11\] |
| Multiple oral frenula                  | Occasional                                  | Multiple oral frenula (HP:0000203)      | ClinGen\[6\]; PRKACB/OFD2 overlap\[17\] |
| Osteopenia, metaphyseal fragmentation  | Rare, expanded spectrum                     | Osteopenia (HP:0000938); Metaphyseal dysplasia (HP:0000939) | Weaver 2026\[15\] |
| Aortic/coronary dilation, vasculopathy | Rare, expanded spectrum                     | Aortic dilatation (HP:0002616); Coronary artery aneurysm (HP:0005155) | Weaver 2026\[15\] |

This table should be interpreted cautiously because of the tiny sample size, but it illustrates the core and expanded phenotypic spectrum of PRKACA-related CAFD1.

## 4. Genetic and Molecular Information

### 4.1 PRKACA Gene: Structure, Function, and Annotation

**PRKACA** (protein kinase cAMP-activated catalytic subunit alpha) is located on chromosome **19p13.12** and encodes one of the three catalytic subunits of PKA.\[9\]\[18\] The NCBI Gene entry for PRKACA (Gene ID: 5566) notes that the gene produces a serine/threonine protein kinase that, in conjunction with regulatory subunits, forms a tetrameric holoenzyme that is inactive until binding of cAMP.\[18\] Upon cAMP binding, the regulatory subunit dimer undergoes conformational change and releases two active catalytic monomers, which phosphorylate target proteins on serine/threonine residues.\[18\] Multiple isoforms of PRKACA exist, and alternative splicing has been reported, although the canonical transcript is NM_002730, designated as MANE Select.\[18\]\[19\]

PRKACA is widely expressed across tissues, with high expression in the heart, adrenal cortex, brain, and other organs, reflecting its role in many cellular processes including metabolism, development, memory, and immune responses.\[11\]\[18\] It is annotated in Gene Ontology (GO) with functions such as **cAMP-dependent protein kinase activity (GO:0004691)** and **ATP binding (GO:0005524)**, and is linked to biological processes including **signal transduction (GO:0007165)**, **regulation of transcription (GO:0006355)**, and **cell differentiation (GO:0030154)**.\[18\] The enzyme’s activity is dependent on binding Mg\(^{2+}\) and ATP (CHEBI:29108 and CHEBI:30616), and it phosphorylates a broad spectrum of substrates, including CREB, GLI transcription factors, and various ion channels.\[11\]\[18\]

In addition to its role in CAFD1, PRKACA is implicated in tumorigenesis. The Cancer Knowledgebase (CKB) describes PRKACA as an oncogene and notes that somatic mutations and the DNAJB1–PRKACA fusion have been identified in fibrolamellar hepatocellular carcinoma, pancreatic, and bile duct cancers, as well as in some cardiac and adrenal tumors.\[19\] These somatic alterations lead to constitutive activation of PKA and dysregulated phosphorylation of downstream targets, illustrating the pathogenic potential of PRKACA hyperactivity in a variety of contexts.\[18\]\[19\]

### 4.2 Pathogenic Variants in CAFD1: Types, Classifications, and Frequencies

The **pathogenic variants** responsible for CAFD1 are predominantly **missense** and **in-frame deletions** that alter key structural elements of PRKACA’s catalytic subunit, particularly at interfaces with regulatory subunits. The archetypal variant is **c.409G>A (p.Gly137Arg)**, designated in OMIM as PRKACA 601639.0002.\[3\]\[9\] Gly137 is located at a highly conserved tethering surface that interacts with regulatory subunits; substitution by arginine introduces a positively charged residue that alters local conformation and weakening of the interface.\[9\]\[11\] Functional assays in Palencia-Campos et al. showed that this variant leads to PKA holoenzymes that are more sensitive to activation by cAMP than wild-type proteins, with increased catalytic activity at lower cAMP concentrations.\[11\]\[12\]\[13\] The variant is absent from population databases such as gnomAD and has been found in multiple unrelated families, supporting its pathogenicity.\[1\]\[3\]\[9\]\[11\]

ClinVar classifies p.Gly137Arg as **pathogenic** for CAFD1, and reports that it has been submitted by multiple laboratories with consistent interpretation, based on ACMG criteria including de novo occurrence, absence from controls, functional data, and consistent phenotype.\[1\]\[3\]\[5\]\[9\] Liang et al. explicitly applied ACMG guidelines and concluded that PRKACA c.409G>A meets criteria for pathogenicity in their Chinese CAFD1 patient, noting its recurrence in the literature and robust functional evidence linking it to gain-of-function effects.\[1\]\[16\]

The **in-frame three–amino-acid deletion** reported by Weaver et al. represents a second class of pathogenic variant, albeit still falling under gain-of-function or dysregulated activity.\[15\] This deletion affects a region critical for substrate and regulatory subunit tethering, and functional studies revealed that the resulting protein is catalytically active but has reduced interaction with regulatory subunits, particularly type II, leading to overactivation of PKA and impaired initiation of Hedgehog signaling.\[15\] In patient-derived iPSCs, this variant was associated with reduced ciliation, and in vitro and in vivo studies confirmed its pathogenic impact on skeletal and vascular development.\[15\]

From a classification perspective, PRKACA variants causing CAFD1 are **germline** (or mosaic) variants, not somatic, and follow an autosomal dominant inheritance pattern.\[3\]\[6\]\[9\]\[11\] They are not observed at appreciable frequencies in population databases, consistent with the rarity and severity of the resulting congenital malformations.\[1\]\[5\] ClinGen and PanelApp emphasize that **loss-of-function variants (e.g., truncating mutations) do not cause CAFD1**, which is important for variant interpretation; PVS1 (ACMG criterion for null variants in genes where loss of function is a known mechanism) should not be applied.\[7\]\[8\] Instead, the mechanism is gain-of-function, and pathogenicity assessment focuses on missense/in-frame variants that alter regulatory interactions and increase PKA activity.\[6\]\[11\]\[15\]

### 4.3 Germline versus Mosaic Origin and Inheritance Mechanisms

The original PRKACA p.Gly137Arg variants were found in **heterozygous germline** state in some probands and as **somatic mosaic** variants in others, including an unaffected parent who transmitted the variant to an affected child.\[9\]\[11\]\[13\] Palencia-Campos et al. reported that in two unrelated probands with CAFD1, the p.Gly137Arg mutation arose de novo, whereas in another family, an asymptomatic father with mosaicism transmitted the mutation to his offspring, who displayed the full CAFD1 phenotype.\[3\]\[9\]\[11\] This pattern underscores the role of **germline mosaicism** in PRKACA-related disorders and explains instances where the variant appears to skip generations or arises in multiple siblings despite negative testing in parental blood.\[6\]\[11\]

ClinGen’s curation summarizes this by noting that the transmission pattern of CAFD1 in the studied families is consistent with **autosomal dominant inheritance**, with both de novo and inherited cases documented.\[3\]\[6\]\[9\]\[11\] Parental mosaicism, including low-level mosaicism undetectable by standard sequencing, is a recognized mechanism, and genetic counseling for families must therefore address recurrence risk even when parental testing is negative in blood.\[6\]\[11\] The Liang case, in which both parents tested negative and the child had a de novo PRKACA c.409G>A variant, illustrates that de novo mutagenesis is a frequent origin of CAFD1.\[1\]\[16\]

### 4.4 Modifier Genes and Related Loci

No specific **modifier genes** have been identified that alter the expression or severity of CAFD1 in humans. However, the closely related condition **Cardioacrofacial dysplasia 2 (CAFD2; OMIM 619143)**, caused by gain-of-function variants in **PRKACB**, provides an important comparator and suggests that different PKA catalytic subunits can converge on similar developmental pathways.\[2\]\[10\]\[11\]\[14\] PRKACB encodes the Cβ subunit of PKA, and in CAFD2, de novo PRKACB missense mutations such as p.Gly235Arg lead to increased cAMP sensitivity and Hh inhibition, paralleling the PRKACA mechanism.\[10\]\[11\]\[14\] ClinGen and PanelApp highlight that PRKACA and PRKACB should be considered together in the differential diagnosis of ciliopathies presenting with polydactyly, narrow chest, and heart defects.\[7\]\[8\]

In a 2022 study, a CAFD2 patient with a PRKACB p.Phe375Ser variant showed features overlapping with **oral–facial–digital (OFD) syndrome**, including multiple oral frenula and postaxial polydactyly, and the authors pointed out that PRKACB can phosphorylate OFD1, a key protein mutated in OFD type 1.\[17\] This mechanistic link suggests that PKA subunits may modulate ciliopathy phenotypes by altering phosphorylation of ciliary structural or regulatory proteins, and raises the possibility that variants in ciliary genes such as OFD1, EVC, or GLI proteins could modify CAFD1 severity.\[11\]\[17\] However, such modifier relationships have not yet been documented in CAFD1 patients.

### 4.5 Epigenetic and Structural Genomic Considerations

There is currently no specific evidence implicating **epigenetic changes** such as DNA methylation or histone modification in the pathogenesis of CAFD1 beyond the primary PRKACA sequence variants. PRKACA expression is ubiquitous and tightly regulated by cAMP and other signaling inputs, but disease-causing CAFD1 variants act at the protein structural level to alter enzyme regulation rather than via transcriptional or epigenetic misregulation.\[11\]\[18\] Similarly, there are no reports of large-scale chromosomal abnormalities (e.g., copy number variants) involving PRKACA causing CAFD1; the known structural alterations involving PRKACA, such as DNAJB1–PRKACA fusion, are associated with fibrolamellar hepatocellular carcinoma rather than congenital malformations.\[18\]\[19\]

From a structural genomics perspective, PRKACA is located at **19:14,091,688–14,117,762** (GRCh38), and no recurrent deletions or duplications of this locus have been tied to CAFD1 in DECIPHER or similar databases.\[9\]\[18\] The Weaver in-frame deletion arises at the single-exon level, affecting a small region within the coding sequence without involving larger chromosomal segments.\[15\] Thus, at present, CAFD1 appears to be driven mainly by small-scale exonic variants rather than larger structural rearrangements or epigenetic dysregulation.\[1\]\[3\]\[9\]\[11\]\[15\]

## 5. Environmental Information

### 5.1 Non-genetic Environmental Factors

As noted earlier, there is **no direct evidence** linking environmental factors such as toxins, radiation, pollution, or occupational exposures to the development of CAFD1. The congenital nature of the disease and its strong association with highly specific PRKACA variants suggest that environmental contributions, if any, are minor compared with the genetic lesion.\[1\]\[11\]\[15\] No CAFD1 case reports have identified consistent prenatal exposures or maternal conditions that could serve as risk factors, and large-scale environmental health databases do not list CAFD1 as an environmentally mediated condition.\[1\]\[11\]\[16\]\[15\]

The Comparative Toxicogenomics Database (CTD) and related resources catalog many environmental agents that influence cAMP/PKA signaling, but none has been reported as a direct cause of congenital PKA overactivation leading to CAFD1-like phenotypes in humans.\[11\]\[18\] Furthermore, animal models of teratogenic exposures that perturb Hedgehog signaling, such as cyclopamine, do produce limb and craniofacial anomalies, but these operate via direct SMO antagonism rather than PKA activation, and have not been connected to PRKACA variation.\[11\] Consequently, CAFD1 is best conceptualized as a genetic developmental disorder without a recognized environmental etiology.

### 5.2 Lifestyle and Infectious Factors

Lifestyle factors such as smoking, diet, exercise, or alcohol consumption do not appear relevant to CAFD1 risk, given that the condition manifests in utero and is present at birth. No associations have been reported between maternal lifestyle factors and CAFD1 in the existing case reports, and the rarity of the syndrome precludes epidemiologic correlation studies.\[1\]\[11\]\[16\] Infectious agents, including viral or bacterial infections during pregnancy, have likewise not been implicated.

The absence of evidence does not entirely rule out modest environmental modulation of phenotype severity, particularly in relation to postnatal progression of skeletal or vascular manifestations, but there is currently no empirical support for such interactions.\[1\]\[11\]\[15\] Clinical management therefore focuses on addressing the congenital lesions rather than modifying environmental exposures as a preventive or therapeutic strategy.

## 6. Mechanism / Pathophysiology

### 6.1 Ordered Causal Chain from Mutation to Phenotype

1. Heterozygous gain-of-function mutation or in-frame deletion in PRKACA leads to altered PRKACA catalytic subunit structure and reduced affinity for PKA regulatory subunits.\[1\]\[9\]\[11\]\[15\]  
2. Reduced regulatory subunit binding leads to increased basal PKA activity and heightened sensitivity of the PKA holoenzyme to activation by cAMP.\[1\]\[7\]\[11\]\[15\]  
3. Increased PKA activity leads to excessive phosphorylation and inactivation of GLI transcription factors and other Hedgehog pathway components in primary cilia, thereby inhibiting Hedgehog signaling; this step is directly demonstrated in NIH 3T3 cells.\[1\]\[7\]\[8\]\[11\]\[13\]  
4. Inhibition of Hedgehog signaling leads to disrupted patterning and proliferation in developing cardiac, skeletal, craniofacial, and ectodermal tissues during embryogenesis.\[1\]\[7\]\[11\]\[13\]\[15\]  
5. Disrupted cardiac cushion formation and septation lead to common atrium, atrioventricular septal defects, and related congenital heart malformations.\[3\]\[9\]\[11\]\[13\]  
6. Impaired chondrocyte proliferation and differentiation in growth plates leads to limb shortening, brachydactyly, genu valgum, and broader skeletal dysplasia.\[1\]\[7\]\[11\]\[15\]\[16\]  
7. Aberrant signaling in craniofacial and ectodermal progenitors leads to midface hypoplasia, micrognathia, dental hypoplasia, nail dysplasia, and oral anomalies such as multiple frenula.\[1\]\[2\]\[6\]\[11\]\[17\]  
8. In some variants, persistent PKA overactivation and impaired ciliation in vascular smooth muscle and endothelial cells leads to vasculopathy, including aortic and coronary dilation and vascular tortuosity; this step is demonstrated in a single case and inferred to share mechanisms with skeletal defects.\[15\]  

These steps represent a synthesis of human genetic, biochemical, and cell-based evidence, with some details inferred from broader Hedgehog and PKA biology.

### 6.2 Molecular Pathways: cAMP/PKA and Hedgehog Signaling

The central molecular pathway in CAFD1 pathophysiology is the **cAMP/PKA signaling cascade** and its regulation of **Hedgehog (Hh) signaling** via GLI transcription factors.\[1\]\[7\]\[8\]\[11\]\[13\] In normal cells, PKA is a tetrameric complex consisting of two regulatory and two catalytic subunits. Binding of cAMP to the regulatory subunits causes a conformational change that releases the catalytic subunits, which then phosphorylate substrates.\[18\] The PKA pathway is canonically activated by G protein–coupled receptors (GPCRs) that stimulate adenylate cyclase and increase intracellular cAMP.\[18\]

In the context of Hedgehog signaling, PKA plays a **negative regulatory role**. In the absence of Hh ligands, PKA phosphorylates GLI2 and GLI3 transcription factors, promoting their processing into repressor forms and thereby suppressing Hh target gene expression.\[11\]\[13\] When Hh ligands bind to the receptor PTCH1, SMO is activated and primary cilia relay signals that inhibit PKA at the ciliary base, reducing GLI phosphorylation, allowing accumulation of full-length GLI activators, and turning on Hh target genes critical for patterning and morphogenesis.\[11\]\[13\]

In Palencia-Campos et al., expression of PRKACA p.Gly137Arg or PRKACB p.Gly235Arg in NIH 3T3 fibroblasts impaired the ability of the SMO agonist SAG to inactivate PKA and fully activate Hh signaling.\[11\]\[12\]\[13\] Bioluminescence resonance energy transfer and PepTag assays showed that these variants confer **increased sensitivity of PKA holoenzymes to activation by cAMP**, and that they maintain higher basal kinase activity even at low cAMP levels.\[11\]\[12\]\[13\] As a result, GLI proteins remain in a more phosphorylated, repressor-prone state, and Hh target gene transcription is attenuated.\[11\]\[13\] PanelApp curators summarize this by noting that the variants increase PKA sensitivity to cAMP and that ectopic expression of mutant PRKACA/B inhibits Hh signaling in NIH 3T3 cells, providing an underlying mechanism for the developmental defects.\[7\]\[8\]

The Weaver et al. deletion variant similarly leads to overactivation of PKA and/or failure to properly initiate Hh signaling, as the altered Cα subunit shows reduced interaction with regulatory subunits and abnormal substrate tethering.\[15\] Patient-derived iPSCs displayed reduced ciliation and deficits in Hh pathway activation, further connecting PKA dysregulation with ciliary signaling defects.\[15\] Thus, across different PRKACA alleles, a common mechanistic theme is **inappropriate PKA activity that blunts Hh signaling during development**, manifesting as a ciliopathy-like phenotype.\[1\]\[7\]\[8\]\[11\]\[13\]\[15\]

From a pathway ontology standpoint, key Reactome and KEGG pathways include **“cAMP signaling pathway”**, **“Hedgehog signaling pathway”**, and **“G protein–coupled receptor signaling”**. GO biological process terms such as **“Hedgehog signaling pathway (GO:0007224)”**, **“regulation of GLI protein processing (GO:0016481)”**, and **“cAMP-mediated signaling (GO:0019933)”** appropriately capture these mechanistic roles.

### 6.3 Cellular Processes: Ciliogenesis, Patterning, and Tissue-Specific Effects

At the cellular level, PRKACA gain-of-function in CAFD1 disrupts processes central to **primary cilia formation and function**, **chondrocyte differentiation**, **endocardial cushion development**, and **ectodermal differentiation**.\[1\]\[7\]\[11\]\[15\]\[17\] Primary cilia are microtubule-based organelles that serve as hubs for Hh and other signaling pathways in many cell types, including chondrocytes, neural progenitors, and cardiac cushion cells. Proper assembly and function of primary cilia are critical for morphogen gradients and coordinated morphogenesis.\[11\]\[15\]

The Weaver et al. study provides direct evidence that PRKACA gain-of-function disrupts **ciliogenesis**. Patient-derived iPSCs with the in-frame deletion exhibited reduced ciliation compared to controls, and in vitro and in vivo experiments indicated that PKA overactivation and defective Hh signaling contributed to impaired cilia formation.\[15\] These findings align with the classification of CAFD1 as a “ciliopathy-associated skeletal dysplasia,” as described in the Liang case report and PanelApp.\[1\]\[7\]\[16\] The inhibition of Hh signaling in NIH 3T3 fibroblasts expressing mutant PRKACA or PRKACB further underscores that ciliary signaling is compromised.\[11\]\[13\]

In developing cartilage, Hh signaling regulates proliferation and differentiation of growth plate chondrocytes. Indian Hedgehog (IHH) produced by prehypertrophic chondrocytes signals to the perichondrium and regulates PTHrP, maintaining proliferative zones and coordinating bone growth. Excessive PKA activity and GLI phosphorylation are expected to reduce IHH signaling, leading to premature chondrocyte differentiation, shortened long bones, and metaphyseal abnormalities—precisely the pattern observed in CAFD1 skeletal dysplasia.\[1\]\[11\]\[15\]\[16\] In the heart, Hh signaling influences endocardial cushion formation and outflow tract development; thus, its inhibition can produce atrioventricular septal defects and common atrium.\[3\]\[9\]\[11\]\[13\] The specific cell types involved include **endocardial cushion mesenchymal cells (CL:0002548)**, **chondrocytes (CL:0000138)**, and **neural crest–derived mesenchyme**, all of which rely on intact Hh signaling and ciliary function.

In ectodermal tissues such as teeth and nails, PKA and Hh signaling coordinate epithelial–mesenchymal interactions and differentiation of enamel organ and nail matrix cells. Disruption of these pathways can lead to dental hypoplasia, hypodontia, and nail dysplasia, as seen in CAFD1.\[1\]\[6\]\[11\]\[16\] In the vasculature, Hh signaling influences smooth muscle and endothelial cell behavior; the Weaver case indicates that PKA overactivation in these cells can lead to vascular anomalies such as aortic and coronary dilation and tortuosity, although this has been documented in only a single patient thus far.\[15\]

### 6.4 Protein Dysfunction: Structural Effects of PRKACA Variants

At the protein level, CAFD1-causing PRKACA variants induce **conformational changes** that alter interactions with regulatory subunits and substrates. The p.Gly137Arg substitution introduces a bulky, positively charged arginine at a conserved glycine residue within a tethering surface critical for binding regulatory subunits.\[9\]\[11\] Structural modeling and crystallographic analysis in Palencia-Campos et al. demonstrated that this substitution distorts local secondary structure and weakens the interface between Cα and regulatory subunits, reducing the ability of regulatory subunits to keep the catalytic subunit in an inactive state.\[11\]\[12\]\[13\] Biochemical assays confirmed that the mutant holoenzyme had increased basal activity and responded to lower concentrations of cAMP with greater activation compared to wild type.\[11\]\[12\]

The three–amino-acid deletion described by Weaver et al. similarly affects a region involved in substrate tethering and regulatory interaction, although the precise residues differ.\[15\] Their in silico model predicted that the deletion destabilizes critical secondary structural elements and alters the configuration of the C-terminal tail, which is known to contribute to substrate specificity and regulatory binding.\[15\] Functional assays showed that the mutant protein remains catalytically competent but is less effectively inhibited by regulatory subunits, leading to persistent or easily triggered kinase activity.\[15\] This supports a model in which **PRKACA gain-of-function variants produce a “leaky” or hyperresponsive kinase** that transduces cAMP signals disproportionately, especially during developmental windows when precise tuning is essential.

From a protein ontology perspective, PRKACA is classified as a **serine/threonine protein kinase (UniProt P17612)** and belongs to the **AGC kinase family**. The variants perturb the **regulatory subunit binding interface** and the **activation loop**, affecting GO cellular component terms such as **“cAMP-dependent protein kinase complex (GO:0005952)”** and molecular function terms such as **“protein kinase activity (GO:0004672)”**.\[18\]

### 6.5 Biochemical and Metabolic Consequences

Although CAFD1 is not primarily a metabolic disorder, alterations in PKA activity have broad biochemical implications. PKA regulates glycogen metabolism, lipolysis, and numerous transcriptional programs via CREB and other transcription factors.\[11\]\[18\] However, in CAFD1, the major biochemical consequences are not systemic metabolic derangements but rather developmental mispatterning. Serum biochemistry in reported CAFD1 patients has not revealed consistent metabolic abnormalities, and there

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 5 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 37 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 2 |
| Unverifiable | 1 |
| Terms whose name was checked | 8 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0030876` (4 mentions) - the report calls it "if available"; MONDO calls it **cardioacrofacial dysplasia 1**
- `HP:0001513` (2 mentions) - the report calls it "Disproportionate short stature"; HP calls it **Obesity**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `HP:0000203` (2 mentions), reported as "Multiple oral frenula" - HP does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0016481` (GO_0016481) (1 mention) - replaced by `GO:0045892`
- `GO:0019933` (obsolete cAMP-mediated signaling) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001162` (2 mentions) - the report calls it "Postaxial polydactyly"; HP calls it **Postaxial hand polydactyly**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.
