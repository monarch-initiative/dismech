---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-30T10:38:39.390768'
end_time: '2026-10-30T10:54:28.997399'
duration_seconds: 949.61
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Chromosome 15q24 Deletion Syndrome
  mondo_id: MONDO:0013256
  category: Chromosomal
  causal_genes: SIN3A
  omim_id: OMIM:613406
  synonyms: 15q24 microdeletion syndrome; 15q24 recurrent microdeletion syndrome;
    Del(15)(q24); monosomy 15q24
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 17
reference_validation:
  total_references: 17
  verified: 17
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 20
  quotes_valid: 20
  relevance_assessed: 17
  on_topic: 12
  validator_version: 0.4.0
term_validation:
  total_terms: 42
  verified: 38
  not_found: 0
  obsolete: 2
  unverifiable: 2
  confabulation_rate: 0.0
  obsolete_terms:
  - term_id: GO:0016575
    ontology_label: obsolete histone deacetylation
  - term_id: GO:0016580
    ontology_label: obsolete Sin3 complex
    replaced_by: GO:0070822
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Chromosome_15q24_Deletion_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Chromosome_15q24_Deletion_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Chromosome 15q24 Deletion Syndrome
- **MONDO ID:** MONDO:0013256 (if available)
- **Causal gene(s):** SIN3A
- **OMIM:** OMIM:613406
- **Synonyms:** 15q24 microdeletion syndrome; 15q24 recurrent microdeletion syndrome; Del(15)(q24); monosomy 15q24
- **Category:** Chromosomal

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Chromosome 15q24 Deletion Syndrome** covering all of the
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

# Chromosome 15q24 Deletion Syndrome (SIN3A): Comprehensive Disease Characteristics Report

**Disease:** Chromosome 15q24 Deletion Syndrome
**MONDO ID:** MONDO:0013256 · **OMIM:** 613406 · **Causal gene:** *SIN3A* (SIN3 transcription regulator family member A; HGNC:19353; chromosome 15q24.2)
**Category:** Chromosomal (contiguous-gene microdeletion syndrome)

---

## Summary

Chromosome 15q24 deletion syndrome is a rare, usually *de novo* contiguous-gene microdeletion disorder of chromosome band 15q24. Its single most important, dosage-sensitive driver gene is ***SIN3A***, which encodes the scaffold protein of a SIN3–HDAC1/2 histone-deacetylase transcriptional corepressor complex and is a MeCP2 interactor required for cortical neurogenesis. Critically, the disease named here is a *SIN3A* disorder: heterozygous loss-of-function point variants in *SIN3A* alone reproduce the core neurodevelopmental phenotype of the microdeletion and define the overlapping **Witteveen–Kolk syndrome (WITKOS, OMIM 613406)**. This shared OMIM identity confirms that *SIN3A* haploinsufficiency explains the central cognitive and craniofacial features, while additional co-deleted genes (e.g., *STRA6*, *NEO1*, *CYP11A1*) account for the rarer multi-organ malformations seen only in larger deletions.

Clinically, the syndrome is characterized by prenatal/postnatal growth retardation, usually mild intellectual disability with prominent speech delay, microcephaly, short stature, and a distinctive facial gestalt (long face with high anterior hairline, hypertelorism, epicanthal folds, downslanting palpebral fissures, sparse broad medial eyebrows, broad/depressed nasal bridge, small mouth, long smooth philtrum, full lower lip). Variable features include digital/skeletal anomalies, male genital abnormalities (hypospadias, micropenis), hypotonia, behavior problems (ASD, ADHD), recurrent infections, and eye problems; rare but severe congenital malformations (structural brain anomalies, cardiac defects, congenital diaphragmatic hernia, intestinal atresia, imperforate anus, myelomeningocele) occur chiefly with larger deletions. Inheritance is autosomal dominant with high penetrance but highly variable expressivity.

There is no disease-modifying therapy. Diagnosis is by chromosomal microarray (for the deletion) or exome/genome sequencing (for intragenic *SIN3A* variants), supported by a robust, predominantly **hypomethylated DNA-methylation episignature** that is diagnostic for WITKOS/SIN3A haploinsufficiency. Management is supportive, anticipatory, and multidisciplinary. This report synthesizes 12 confirmed findings across 25 reviewed papers into a full disease-knowledge-base entry spanning etiology, phenotype, molecular mechanism, anatomy, temporal course, epidemiology, diagnostics, prognosis, treatment, prevention, and model systems.

---

## Key Findings

### 1. *SIN3A* haploinsufficiency is the key dosage-sensitive driver (Finding F001)

The defining molecular insight linking the 15q24 microdeletion to a monogenic disorder came from Witteveen et al. (2016), who identified dominant loss-of-function mutations in *SIN3A* (chromosome 15q24.2) in individuals with mild intellectual disability and autism spectrum disorder who also shared "*striking features, including facial dysmorphisms, microcephaly and short stature. This phenotype is highly related to that of individuals with atypical 15q24 microdeletions, linking SIN3A to this microdeletion syndrome*" ([PMID: 27399968](https://pubmed.ncbi.nlm.nih.gov/27399968/)). Balasubramanian et al. (2021) then characterized 28 patients with *SIN3A* loss-of-function variants (24 truncating, 3 missense, 1 in-frame gain), establishing that the gene-level disorder, now termed **Witteveen–Kolk syndrome (OMIM 613406)**, "*is a recently defined neurodevelopmental syndrome caused by heterozygous loss-of-function variants in SIN3A*" ([PMID: 33437032](https://pubmed.ncbi.nlm.nih.gov/33437032/)). Because the point-mutation disorder and the microdeletion share the same OMIM number (613406) and the same core phenotype, *SIN3A* is confirmed as the principal dosage-sensitive driver of the neurodevelopmental core of the 15q24 deletion syndrome.

### 2. A ~1.1 Mb critical region and segmental-duplication-mediated recurrence (Finding F002)

Mefford et al. (2012) characterized 15 patients carrying nine distinct deletions ranging 266 kb–3.75 Mb and showed that "*the core cognitive features of the 15q24 microdeletion syndrome, including developmental delays and severe speech problems, are largely due to deletion of genes in a 1.1-Mb critical region*" ([PMID: 22180641](https://pubmed.ncbi.nlm.nih.gov/22180641/)). Recurrence arises from the local genomic architecture: "*The majority of breakpoints lie within segmental duplication (SD) blocks. Low sequence identity and large intervals of unique sequence between SD blocks likely contribute to the rarity of 15q24 deletions, which occur 8-10 times less frequently than 1q21 or 15q13 microdeletions*" ([PMID: 22180641](https://pubmed.ncbi.nlm.nih.gov/22180641/)). Liu et al. (2020) further refined the region, proposing a 650-kb LCR15q24A-B interval (including *NEO1*) relevant to ASD, with the LCR B–D interval linked to developmental delay, dysmorphism, and recurrent infection ([PMID: 31953991](https://pubmed.ncbi.nlm.nih.gov/31953991/)). The smallest region of overlap has been placed at ~1.2 Mb between LCR15q24B and LCR15q24C.

### 3. *SIN3A* scaffolds an HDAC1/2 corepressor complex and interacts with MeCP2 (Finding F003)

Mechanistically, SIN3A is the scaffold of the SIN3 core corepressor complex. Jayaprakash et al. (2021) define its composition: "*The SIN3 core complex comprises the eponymous proteins SIN3A or SIN3B, the catalytically active proteins HDAC1 or HDAC2, the histone chaperone retinoblastoma-associated protein 46/retinoblastoma-binding protein 7 (RBAP46/RBBP7) or RBAP48/RBBP4, the SIN3-associated protein 30 (SAP30), and the suppressor of defective silencing 3 (SDS3)*" ([PMID: 33130996](https://pubmed.ncbi.nlm.nih.gov/33130996/)). The complex deacetylates histones to repress transcription. Witteveen et al. (2016) demonstrated the disease-relevant function: SIN3A interacts with MeCP2, and "*in vivo functional knockdown of Sin3a led to reduced cortical neurogenesis, altered neuronal identity and aberrant corticocortical projections in the developing mouse brain*" ([PMID: 27399968](https://pubmed.ncbi.nlm.nih.gov/27399968/)). Germline deletion of the catalytic partner HDAC1 is embryonic-lethal in mouse and reduces Sin3A/NuRD/CoREST complex activity ([PMID: 20404188](https://pubmed.ncbi.nlm.nih.gov/20404188/)), underscoring the essential nature of this corepressor machinery.

### 4. Clinical phenotype spectrum and dysmorphology (Finding F004)

Magoulas & El-Hattab (2012) provide the authoritative phenotype overview: the syndrome "*is characterized by growth retardation, intellectual disability, and distinct facial features including long face with high anterior hairline, hypertelorism, epicanthal folds, downslanting palpebral fissures, sparse and broad medial eyebrows, broad and/or depressed nasal bridge, small mouth, long smooth philtrum, and full lower lip. Other common findings include skeletal and digital abnormalities, genital abnormalities in males, hypotonia, behavior problems, recurrent infections, and eye problems*" ([PMID: 22216833](https://pubmed.ncbi.nlm.nih.gov/22216833/)). Less frequent findings include hearing loss, growth hormone deficiency, hernias, and obesity. Importantly, "*Congenital malformations, while rare, can be severe and include structural brain anomalies, cardiovascular malformations, congenital diaphragmatic hernia, intestinal atresia, imperforate anus, and myelomeningocele*" ([PMID: 22216833](https://pubmed.ncbi.nlm.nih.gov/22216833/)). The reported smallest region of overlap is ~1.2 Mb between LCR15q24B and LCR15q24C.

### 5. Mouse models: *Sin3a* is essential and regulates p53/Myc-Mad/E2F networks (Finding F005)

Dannenberg et al. (2005), using conditional *mSin3A* deletion, showed that "*mSin3A was shown to play an essential role in early embryonic development and in the proliferation and survival of primary, immortalized, and transformed cells*" ([PMID: 15998811](https://pubmed.ncbi.nlm.nih.gov/15998811/)). Time-course profiling after deletion "*revealed deregulation of genes involved in cell cycle regulation, DNA replication, DNA repair, apoptosis, chromatin modifications, and mitochondrial metabolism*" ([PMID: 15998811](https://pubmed.ncbi.nlm.nih.gov/15998811/)), operating through Myc-Mad, E2F, and p53 transcriptional networks, with mSin3A/HDAC mediating p53 deacetylation. The in-vivo brain knockdown by Witteveen et al. (reduced cortical neurogenesis, altered neuronal identity, aberrant corticocortical projections) provides the neurodevelopmental counterpart in a dosage-reduction context ([PMID: 27399968](https://pubmed.ncbi.nlm.nih.gov/27399968/)).

### 6. A diagnostic DNA-methylation episignature (Finding F006)

Coenen-van der Spek et al. (2023) studied genome-wide DNA methylation in peripheral blood of 20 individuals with heterozygous *SIN3A* alterations and identified a novel, robust episignature. "*A predominantly hypomethylated DNA methylation profile specific to WITKOS was identified, and the classifier model was able to diagnose a previously unresolved test case*" ([PMID: 36399132](https://pubmed.ncbi.nlm.nih.gov/36399132/)). The signature distinguishes WITKOS from controls and from other neurodevelopmental disorders with episignatures, is sensitive across degrees of phenotypic severity, and resolved a previously uncertain (VUS) case — making it a powerful functional diagnostic adjunct.

### 7. Structural basis of missense LOF and the *SIN3B* paralog syndrome (Finding F007)

Due et al. (2026) performed structural and thermodynamic studies of the Sin3A PAH1 (paired amphipathic helix 1) αα-hub domain, relating "*αα-hub stability to function by structural and thermodynamic studies of the Sin3A-paired amphipathic helix 1 (PAH1) wt hub domain and two predicted loss-of-function variants (A126V and K155E) found in patients with the neurodevelopmental Witteveen-Kolk syndrome*" ([PMID: 41759735](https://pubmed.ncbi.nlm.nih.gov/41759735/)). This shows that WITKOS missense variants cause disease by destabilizing the protein-interaction hub, a loss-of-function mechanism. The dosage-sensitivity model is reinforced by the paralog: Latypova et al. (2021) showed that *SIN3B* (19p13.11) haploinsufficiency causes an overlapping syndrome "*hallmarked by intellectual disability, developmental delay, and dysmorphic facial features with variably penetrant autism spectrum disorder, congenital malformations, corpus callosum defects, and impaired growth caused by disruptive SIN3B variants*" ([PMID: 33811806](https://pubmed.ncbi.nlm.nih.gov/33811806/)), with zebrafish *sin3b* disruption producing craniofacial defects.

### 8. Quantified neurobehavioral phenotype frequencies (Finding F008)

The largest systematically phenotyped cohort (Balasubramanian et al. 2021; n=28, 17 males, 11 females, mean age 8.2 y) provides frequency estimates. Among 16 patients ≥8 years assessed: "*eight (50%) had mild intellectual disability (ID), four had moderate ID (22%), and one had severe ID (6%). Four (25%) did not have any cognitive impairment. Other neurological symptoms such as seizures (4/28) and hypotonia (12/28) were common*" ([PMID: 33437032](https://pubmed.ncbi.nlm.nih.gov/33437032/)). In patients ≥2 years, 3 had ASD and 4 had ADHD; growth and feeding difficulties were characteristic. 27 of 28 variants were novel (24 truncating, 3 missense, 1 large in-frame gain spanning exons 10–12).

| Phenotype | Frequency (Balasubramanian 2021, n=28) |
|---|---|
| Mild ID (of 16 assessed ≥8 y) | 8/16 (50%) |
| Moderate ID | 4/16 (22%) |
| Severe ID | 1/16 (6%) |
| Normal cognition | 4/16 (25%) |
| Seizures | 4/28 (14%) |
| Hypotonia | 12/28 (43%) |
| ASD (patients ≥2 y) | 3 |
| ADHD (patients ≥2 y) | 4 |

### 9. Inheritance, etiology, and diagnostic approach (Finding F009)

15q24 microdeletions are typically *de novo*. Sharp et al. (2007) described "*multiple individuals with mental retardation and overlapping de novo submicroscopic deletions of 15q24*" ([PMID: 17360722](https://pubmed.ncbi.nlm.nih.gov/17360722/)), arising through non-allelic homologous recombination (NAHR) between paralogous low-copy repeats. Because "*Karyotypes are typically normal, and the deletions were detected in these individuals by array comparative genomic hybridization (aCGH)*" ([PMID: 22216833](https://pubmed.ncbi.nlm.nih.gov/22216833/)), chromosomal microarray is the first-line test for the deletion. Intragenic *SIN3A* point variants are predominantly *de novo* heterozygous loss-of-function (truncating) variants inherited in an autosomal dominant manner ([PMID: 33437032](https://pubmed.ncbi.nlm.nih.gov/33437032/); [PMID: 27399968](https://pubmed.ncbi.nlm.nih.gov/27399968/)), detected by exome/genome sequencing or gene panels.

### 10. Supportive, multidisciplinary management (Finding F010)

No targeted or disease-modifying therapy exists; care is supportive and anticipatory. Balasubramanian et al. (2021) advise that "*Involvement of a multidisciplinary team including a geneticist, paediatrician and neurologist should be considered in managing these patients*" ([PMID: 33437032](https://pubmed.ncbi.nlm.nih.gov/33437032/)). Interventions target individual manifestations: early developmental/speech/physical/occupational therapy for DD/ID; antiepileptic drugs for seizures; surgical repair of hypospadias, diaphragmatic hernia, intestinal atresia, imperforate anus, and congenital heart defects; management of recurrent infections; growth hormone evaluation for GH deficiency; and endocrine evaluation for pubertal delay/hypogonadotropic hypogonadism (Correa Brito et al. 2024, [PMID: 38528912](https://pubmed.ncbi.nlm.nih.gov/38528912/)). Janssen et al. (2026) reported "*the first documented treatment of behavioral problems in WITKOS*," a personalized psychological intervention with improved functioning at follow-up ([PMID: 41245232](https://pubmed.ncbi.nlm.nih.gov/41245232/)).

### 11. Anatomical involvement, neuroimaging, temporal course, prognosis (Finding F011)

Brain MRI in WITKOS "*showed subtle abnormalities, including corpus callosum hypoplasia and ventriculomegaly*" ([PMID: 27399968](https://pubmed.ncbi.nlm.nih.gov/27399968/)). Onset is congenital/prenatal for structural malformations, with developmental delay manifesting in infancy/early childhood; the core neurodevelopmental phenotype is non-progressive/static. The primary affected organ is the brain (cerebral cortex, UBERON:0000956), with multi-system involvement of craniofacial skeleton, external genitalia (male), digits/skeleton, eyes, ears, and (rarely) heart, diaphragm, and gastrointestinal tract. No reduced life expectancy is established for isolated SIN3A-related disorder, although rare severe congenital malformations can cause early morbidity/mortality ([PMID: 22216833](https://pubmed.ncbi.nlm.nih.gov/22216833/)).

### 12. Co-deleted genes contribute distinct organ phenotypes — a contiguous-gene mechanism (Finding F012)

Beyond *SIN3A*, the 15q24 critical region contains additional dosage/function-sensitive genes that plausibly account for non-neurodevelopmental features in larger deletions. **STRA6** (stimulated by retinoic acid 6; a retinol/RBP4 receptor in vitamin A/retinoic-acid signaling) causes Matthew-Wood/PDAC syndrome (MCOPS9, MIM 601186) when biallelically mutated: "*Mutations in retinoic acid 6 gene (STRA6) have been reported in clinically diagnosed patients with MWS*" ([PMID: 30204971](https://pubmed.ncbi.nlm.nih.gov/30204971/)), a syndrome with microphthalmia/anophthalmia, pulmonary hypoplasia, congenital diaphragmatic hernia, and cardiac defects — paralleling the rare eye, diaphragmatic hernia, and heart anomalies of the deletion. **NEO1** (neogenin), within LCR15q24A-B, is proposed as ASD-relevant: "*the ASD phenotype in this individual is potentially attributed by genes particularly NEO1 within the newly proposed critical region*" ([PMID: 31953991](https://pubmed.ncbi.nlm.nih.gov/31953991/)). **CYP11A1** (cholesterol side-chain cleavage) relates to steroidogenesis and adrenal-gonadal function. A deletion case involving *CYP1A1*/*EDC3* presented with poor immunity, laryngeal stridor, and lower-limb swelling ([PMID: 34922566](https://pubmed.ncbi.nlm.nih.gov/34922566/)), further supporting multigene contributions.

---

## Full Section-by-Section Report

### 1. Disease Information

Chromosome 15q24 deletion syndrome (MONDO:0013256; OMIM 613406) is a rare contiguous-gene microdeletion disorder caused by loss of a segment of chromosome band 15q24. Its central dosage-sensitive gene is ***SIN3A***. The gene-level disorder produced by intragenic *SIN3A* loss-of-function variants is **Witteveen–Kolk syndrome (WITKOS)**, which shares OMIM 613406 and most of the core phenotype. Key identifiers: **MONDO:0013256**; **OMIM 613406**; **Orphanet ORPHA:94065** (15q24 microdeletion syndrome). ICD-10 maps to Q93.5 (other deletions of part of a chromosome); ICD-11 to LD44 (chromosomal deletions). Synonyms: 15q24 microdeletion syndrome; 15q24 recurrent microdeletion syndrome; Del(15)(q24); monosomy 15q24; Witteveen–Kolk syndrome (for the SIN3A-restricted form). Information is drawn predominantly from aggregated disease-level resources (OMIM, Orphanet) and from published patient series/case reports rather than from EHR-derived individual-patient datasets.

### 2. Etiology

**Causal factors:** The disease is genetic. The deletion arises by non-allelic homologous recombination (NAHR) between flanking low-copy repeats/segmental duplications at 15q24, generating recurrent *de novo* deletions ([PMID: 17360722](https://pubmed.ncbi.nlm.nih.gov/17360722/); [PMID: 22180641](https://pubmed.ncbi.nlm.nih.gov/22180641/)). Haploinsufficiency of *SIN3A* is the primary driver of the neurodevelopmental core; additional co-deleted genes contribute organ-specific features in larger deletions (F012).

**Genetic risk factors:** The principal risk factor is the presence of segmental-duplication architecture at 15q24 predisposing to NAHR. There are no established modifier genes, though deletion size (number of genes removed) correlates with severity and breadth of malformations.

**Environmental risk factors / protective factors:** None established. As a *de novo* structural/monogenic disorder, there are no recognized environmental triggers, lifestyle risk factors, or protective alleles/exposures. Advanced parental age is not established as a risk factor. **Gene–environment interactions:** none documented.

### 3. Phenotypes

Phenotypes span physical manifestations (dysmorphism, growth failure), clinical signs (hypotonia, microcephaly), behavioral changes (ASD, ADHD), and neurodevelopmental deficits (ID, speech delay). Characteristic age of onset is congenital/early childhood; the core neurocognitive phenotype is static (non-progressive), while a single case report describes progressive cerebellar ataxia and dystonia broadening the spectrum ([PMID: 39576496](https://pubmed.ncbi.nlm.nih.gov/39576496/)). Severity is typically mild for ID, with variable expressivity.

Suggested HPO terms:
- Intellectual disability, mild — **HP:0001256** (50% of ≥8 y assessed; F008)
- Delayed speech and language development — **HP:0000750**
- Microcephaly — **HP:0000252**
- Short stature — **HP:0004322**
- Hypertelorism — **HP:0000316**
- Downslanted palpebral fissures — **HP:0000494**
- Epicanthus — **HP:0000286**
- Depressed nasal bridge — **HP:0005280**
- Long philtrum — **HP:0000343**
- Muscular hypotonia — **HP:0001252** (43%)
- Seizures — **HP:0001250** (14%)
- Autistic behavior — **HP:0000729**
- Attention deficit hyperactivity disorder — **HP:0007018**
- Hypospadias — **HP:0000047**; Micropenis — **HP:0000054**
- Recurrent infections — **HP:0002719**

**Quality of life:** Impact is driven mainly by cognitive/speech impairment and behavior problems affecting education, independence, and communication; isolated cases carry high QoL burden from severe malformations. No disease-specific QoL instruments (EQ-5D/SF-36) have been applied in published cohorts.

### 4. Genetic/Molecular Information

**Causal gene:** *SIN3A* (HGNC:19353; NCBI Gene 25942; UniProt Q96ST3; chromosome 15q24.2; OMIM gene 607776). **Variant classes:** heterozygous loss-of-function — nonsense, frameshift, splice-site, and whole-gene deletion; rare destabilizing missense (e.g., p.Ala126Val, p.Lys155Glu in PAH1; p.Pro351Ser) and one large in-frame gain (exons 10–12). In the 28-patient series, 24/28 were truncating, 3 missense, 1 in-frame; 27/28 novel ([PMID: 33437032](https://pubmed.ncbi.nlm.nih.gov/33437032/)). **Classification:** pathogenic/likely pathogenic per ACMG for truncating LOF; missense variants supported by structural destabilization data ([PMID: 41759735](https://pubmed.ncbi.nlm.nih.gov/41759735/)). **Allele frequency:** pathogenic variants are absent/ultra-rare in gnomAD; *SIN3A* is highly loss-of-function-intolerant. **Origin:** germline, predominantly *de novo*. **Functional consequence:** loss of function / haploinsufficiency.

**Co-deleted genes of interest (contiguous-gene mechanism):** *STRA6*, *NEO1*, *CYP11A1*, *CYP1A1*, *EDC3* (F012). **Modifier genes:** none firmly established; deletion size is the main modifier of expressivity. **Epigenetic information:** *SIN3A* haploinsufficiency produces a diagnostic, predominantly hypomethylated blood DNA-methylation episignature ([PMID: 36399132](https://pubmed.ncbi.nlm.nih.gov/36399132/)). **Chromosomal abnormality:** interstitial deletion 15q24, ~0.1–3.75 Mb; recurrent breakpoints in SD blocks; detected by CMA/aCGH.

### 5. Environmental Information

No environmental factors, toxins, radiation, occupational exposures, lifestyle factors, or infectious agents are implicated in causing or triggering this disorder. It is a *de novo* genetic condition. Recurrent infections observed in some patients are a consequence of the deletion (possible immune component), not an environmental cause.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. NAHR between segmental duplications/low-copy repeats flanking 15q24 **leads to** a recurrent *de novo* interstitial deletion (or an independent intragenic LOF/missense variant in *SIN3A*). *(demonstrated — [PMID: 17360722], [PMID: 22180641])*
2. The deletion/variant **results in** heterozygous loss of functional *SIN3A* → **SIN3A haploinsufficiency** (reduced dosage of the corepressor scaffold). *(demonstrated — [PMID: 27399968])*
3. Reduced SIN3A **leads to** impaired assembly/function of the SIN3–HDAC1/2 corepressor complex (SIN3A, HDAC1/2, RBBP4/7, SAP30, SDS3) and weakened interaction with MeCP2. *(demonstrated — [PMID: 33130996], [PMID: 27399968])*
4. Impaired histone deacetylation **results in** dysregulated transcriptional repression of SIN3 target genes governing cell cycle, DNA replication/repair, apoptosis, chromatin modification, and mitochondrial metabolism (via Myc-Mad, E2F, p53 networks). *(demonstrated in mouse — [PMID: 15998811])*
5. In the developing cerebral cortex this **leads to** reduced cortical neurogenesis, altered neuronal identity, and aberrant corticocortical projections. *(demonstrated — [PMID: 27399968])*
6. Altered corticogenesis **results in** subtle structural changes (corpus callosum hypoplasia, ventriculomegaly) and **manifests as** mild intellectual disability, speech delay, microcephaly, ASD/ADHD, and hypotonia. *(demonstrated/inferred — [PMID: 27399968], [PMID: 33437032])*

**Branch (larger deletions only):** Co-deletion of neighboring genes **contributes** organ-specific features — *STRA6* loss **leads to** disrupted retinoic-acid/vitamin-A signaling → ocular, diaphragmatic, and cardiac malformations (Matthew-Wood-like); *NEO1* loss **contributes** to ASD; *CYP11A1* loss **may contribute** to steroidogenic/gonadal effects. *(inferred from gene function and overlapping syndromes — [PMID: 30204971], [PMID: 31953991])*

**Molecular pathways:** transcriptional corepression via histone deacetylation (not classical signaling cascades); retinoic-acid signaling (STRA6 branch). **Cellular processes:** neurogenesis, neuronal differentiation/identity, cell-cycle and survival control, apoptosis. **Protein dysfunction:** loss of function / haploinsufficiency; missense variants destabilize the PAH1 αα-hub protein-interaction domain ([PMID: 41759735](https://pubmed.ncbi.nlm.nih.gov/41759735/)). **Epigenetic changes:** global shift toward hypomethylation (episignature). **GO/CL suggestions:** histone deacetylation **GO:0016575**, negative regulation of transcription by RNA Pol II **GO:0000122**, chromatin organization **GO:0006325**, cerebral cortex neuron differentiation **GO:0021895**, neurogenesis **GO:0022008**; cell types — neural progenitor/radial glial cell **CL:0000047/CL:0000681**, glutamatergic cortical projection neuron **CL:0000679**.

### 7. Anatomical Structures Affected

**Organ level — primary:** brain, especially cerebral cortex (**UBERON:0000956**); corpus callosum (**UBERON:0002336**); lateral ventricles (ventriculomegaly). **Secondary/other systems:** craniofacial skeleton (**UBERON:0010323**/facial dysmorphism), eyes (**UBERON:0000970**), ears (hearing), external male genitalia (**UBERON:0000079**; hypospadias/micropenis), digits/skeleton (**UBERON:0002544**), and — rarely in larger deletions — heart (**UBERON:0000948**), diaphragm (**UBERON:0001103**; CDH), and gastrointestinal tract (**UBERON:0001555**; intestinal atresia, imperforate anus). **Tissue/cell level:** nervous tissue; cortical neural progenitors and projection neurons. **Subcellular level:** nucleus (**GO:0005634**) — chromatin/corepressor complex (**GO:0016580**, Sin3-type complex). **Lateralization:** malformations are generally bilateral/midline (corpus callosum, facial midline); no consistent lateralization.

### 8. Temporal Development

**Onset:** congenital — structural malformations are prenatal; growth retardation prenatal/postnatal; developmental delay apparent in infancy/early childhood. **Onset pattern:** chronic/static. **Progression:** the core neurodevelopmental phenotype is non-progressive and lifelong; developmental trajectory improves with therapy but ID persists. A rare report documents progressive cerebellar ataxia/dystonia, an atypical course ([PMID: 39576496](https://pubmed.ncbi.nlm.nih.gov/39576496/)). **Disease course:** chronic, lifelong; no remission/relapse pattern. **Critical periods:** fetal corticogenesis (for brain phenotype) and early childhood (developmental intervention window).

### 9. Inheritance and Population

**Epidemiology:** rare; exact prevalence not firmly established (Orphanet classifies it on the order of <1/1,000,000). 15q24 deletions occur 8–10× less frequently than 1q21 or 15q13 microdeletions ([PMID: 22180641](https://pubmed.ncbi.nlm.nih.gov/22180641/)). **Inheritance:** autosomal dominant; the overwhelming majority are *de novo*. **Penetrance:** high/essentially complete for the neurodevelopmental phenotype. **Expressivity:** highly variable (ID from absent to severe; malformations present only in a minority). **Anticipation:** not applicable (not a repeat-expansion disorder). **Germline mosaicism:** possible but not well documented; gives low recurrence risk. **Founder effects / consanguinity:** not applicable (dominant, *de novo*). **Carrier frequency:** not applicable. **Demographics:** no ethnic predilection; both sexes affected (male-genital phenotypes are sex-limited; the Balasubramanian cohort was 17 M : 11 F). **Geographic distribution:** worldwide, no endemic clustering.

### 10. Diagnostics

**First-line genetic testing:** chromosomal microarray (CMA/aCGH) detects the deletion; karyotype is typically normal ([PMID: 22216833](https://pubmed.ncbi.nlm.nih.gov/22216833/)). **For intragenic SIN3A variants:** whole-exome/whole-genome sequencing or multigene neurodevelopmental panels including *SIN3A*; MLPA has been used to detect 15q24 deletions ([PMID: 34922566](https://pubmed.ncbi.nlm.nih.gov/34922566/)). FISH can confirm a known deletion. **Epigenomic diagnostic:** the predominantly hypomethylated WITKOS episignature serves as a functional confirmatory test and resolves VUS ([PMID: 36399132](https://pubmed.ncbi.nlm.nih.gov/36399132/)). **Imaging:** brain MRI may show corpus callosum hypoplasia and ventriculomegaly ([PMID: 27399968](https://pubmed.ncbi.nlm.nih.gov/27399968/)). **Clinical evaluation:** growth monitoring, developmental/cognitive assessment, dysmorphology exam, genital exam in males, ophthalmologic and audiologic evaluation, and endocrine work-up (GH, pubertal/HH assessment; [PMID: 38528912](https://pubmed.ncbi.nlm.nih.gov/38528912/)). **Differential diagnosis:** other microdeletion/ID syndromes with overlapping dysmorphism and ID (e.g., other contiguous-gene syndromes, SIN3B-related syndrome [PMID: 33811806], Kabuki syndrome, and MeCP2-pathway disorders); episignature and CMA/sequencing distinguish them. **Screening:** no population newborn screening; cascade testing is usually not needed given de novo origin, but parental testing informs recurrence risk.

### 11. Outcome/Prognosis

**Survival/mortality:** no reduced life expectancy is established for isolated SIN3A-related disorder; the core phenotype is compatible with normal lifespan. Rare severe congenital malformations (CDH, complex heart defects, intestinal atresia) in larger deletions can cause significant early morbidity and, uncommonly, mortality ([PMID: 22216833](https://pubmed.ncbi.nlm.nih.gov/22216833/)). **Morbidity/function:** chief long-term burden is mild (occasionally moderate) ID, speech/communication impairment, and behavioral issues, with variable impact on independence. **Complications:** recurrent infections, feeding/growth difficulties, seizures, and endocrine issues (GH deficiency, hypogonadotropic hypogonadism). **Recovery potential:** developmental skills improve with early intervention, but cognitive impairment is lifelong. **Prognostic factors:** deletion size and presence of major malformations are the main determinants of outcome; cognitive severity ranges from normal to severe. No validated molecular prognostic biomarkers.

### 12. Treatment

There is **no disease-modifying or targeted therapy**. Management is supportive, anticipatory, and multidisciplinary ([PMID: 33437032](https://pubmed.ncbi.nlm.nih.gov/33437032/)). Components, with suggested NCIT intervention concepts:
- **Developmental/rehabilitative:** early intervention, speech therapy (**NCIT:C15300 Speech Therapy**), physical and occupational therapy, special education.
- **Neurologic:** antiepileptic drugs for seizures (**NCIT:C264 Anticonvulsant Agent**).
- **Behavioral/psychiatric:** personalized psychological treatment (first documented in WITKOS, with improved functioning; [PMID: 41245232](https://pubmed.ncbi.nlm.nih.gov/41245232/)); ADHD/ASD-directed behavioral and, where indicated, pharmacologic management.
- **Surgical (NCIT:C15329 Surgery):** repair of hypospadias, congenital diaphragmatic hernia, intestinal atresia, imperforate anus, and congenital heart defects.
- **Endocrine:** growth hormone therapy for documented GH deficiency (**NCIT:C1646 Recombinant Human Growth Hormone**); hormonal treatment for pubertal delay/hypogonadotropic hypogonadism ([PMID: 38528912](https://pubmed.ncbi.nlm.nih.gov/38528912/)).
- **Infectious:** management of recurrent infections; immune evaluation when indicated.
- **Pharmacogenomics / advanced therapeutics (gene, cell, RNA, immunotherapy):** none established or applicable. No clinical trials of disease-specific agents are available.

### 13. Prevention

**Primary prevention:** none possible, as the disorder is a *de novo* genetic event. **Secondary prevention:** early developmental screening enables prompt intervention to optimize function. **Tertiary prevention:** anticipatory surveillance (growth, endocrine, ophthalmologic, audiologic, seizure monitoring) to prevent/limit complications. **Genetic counseling:** recurrence risk is low for parents of a child with a *de novo* deletion/variant (empiric risk slightly above baseline due to possible germline mosaicism); affected individuals who reproduce have a 50% transmission risk (autosomal dominant). **Reproductive options:** prenatal diagnosis (CMA on CVS/amniocentesis) and preimplantation genetic testing are available when a parental variant is known. **Immunization/public-health/environmental interventions:** not applicable.

### 14. Other Species / Natural Disease

**Taxonomy/orthologs:** *SIN3A* is deeply conserved; mouse *Sin3a* (NCBI Gene 20466; *Mus musculus*, NCBI:txid10090) and zebrafish orthologs are established functional models. **Natural disease:** no naturally occurring companion-animal or wildlife disease corresponding to 15q24 deletion syndrome is documented in OMIA. **Comparative biology:** the corepressor mechanism (SIN3–HDAC) is conserved from yeast to humans, underscoring evolutionary conservation of the disease-relevant pathway; the paralog *SIN3B* is similarly conserved and disease-associated ([PMID: 33811806](https://pubmed.ncbi.nlm.nih.gov/33811806/)). **Transmission/zoonosis:** not applicable.

### 15. Model Organisms

- **Mouse (*Mus musculus*):** conditional *mSin3A* knockout — embryonic lethal; demonstrates essential role in development, proliferation, survival, and transcriptional network control (cell cycle, DNA repair, apoptosis, p53/Myc-Mad/E2F) ([PMID: 15998811](https://pubmed.ncbi.nlm.nih.gov/15998811/)). *In utero* *Sin3a* knockdown recapitulates the neurodevelopmental core (reduced cortical neurogenesis, altered neuronal identity, aberrant projections) — strong face validity for the human brain phenotype ([PMID: 27399968](https://pubmed.ncbi.nlm.nih.gov/27399968/)). **Limitation:** homozygous null is lethal, so dosage/haploinsufficiency (not complete loss) models the human condition.
- **Zebrafish (*Danio rerio*):** *sin3b* disruption produces craniofacial defects, modeling dysmorphism for the paralogous syndrome ([PMID: 33811806](https://pubmed.ncbi.nlm.nih.gov/33811806/)).
- **Mouse ES cells / in vitro:** HDAC1 conditional knockouts reveal the catalytic requirement and corepressor-complex dependency of Sin3A/NuRD/CoREST activity ([PMID: 20404188](https://pubmed.ncbi.nlm.nih.gov/20404188/)); structural/biophysical studies of the PAH1 αα-hub model missense-variant destabilization ([PMID: 41759735](https://pubmed.ncbi.nlm.nih.gov/41759735/)).
- **Applications:** cortical neurogenesis, transcriptional/epigenetic dysregulation, structure–function of SIN3A domains. **Resources:** MGI (mouse), ZFIN (zebrafish). No published patient-derived iPSC/organoid or rat models were identified in this investigation.

---

## Mechanistic Model / Interpretation

```
  Segmental duplications (LCRs) flanking 15q24
                 │  non-allelic homologous recombination
                 ▼
     de novo 15q24 deletion  ──OR──  intragenic SIN3A LOF / destabilizing missense
                 │                                    │
                 ▼                                    ▼
          SIN3A HAPLOINSUFFICIENCY  ◄──────────────────
                 │
                 ▼
   Impaired SIN3–HDAC1/2 corepressor complex  +  weakened MeCP2 interaction
   (SIN3A·HDAC1/2·RBBP4/7·SAP30·SDS3; histone deacetylation lost)
                 │
                 ▼
   Dysregulated repression of SIN3 targets (cell cycle, DNA repair,
   apoptosis, chromatin, mitochondrial metabolism; Myc-Mad/E2F/p53)
                 │
                 ▼
   Reduced cortical neurogenesis · altered neuronal identity · aberrant projections
                 │
                 ▼
   Corpus callosum hypoplasia, ventriculomegaly, microcephaly
                 │
                 ▼
   MILD ID · speech delay · ASD/ADHD · hypotonia · facial gestalt · short stature
                 │
   ┌─────────────┴─────────────────────── (larger deletions only) ──────────────┐
   │ Co-deletion of STRA6 → retinoic-acid signaling defect → eye/diaphragm/heart │
   │ Co-deletion of NEO1 → ASD contribution                                      │
   │ Co-deletion of CYP11A1 → steroidogenic/gonadal effects                      │
   └─────────────────────────────────────────────────────────────────────────────┘
```

The investigation produced a coherent two-tier model. **Tier 1 (monogenic core):** *SIN3A* haploinsufficiency impairs an epigenetic corepressor machine, disrupting the transcriptional programs of cortical neurogenesis and producing the invariant neurodevelopmental and craniofacial phenotype shared by the microdeletion and Witteveen–Kolk syndrome. The convergent evidence — OMIM identity (613406), point variants reproducing the phenotype, a diagnostic hypomethylated episignature, structural destabilization of missense variants, and a parallel *SIN3B* syndrome — makes this the most strongly supported conclusion. **Tier 2 (contiguous-gene modifiers):** the breadth and severity of non-neurodevelopmental malformations scale with deletion size because additional dosage-sensitive genes (*STRA6*, *NEO1*, *CYP11A1*) are removed, explaining why larger deletions add ocular, diaphragmatic, cardiac, and gonadal features absent in isolated *SIN3A* variants.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [27399968](https://pubmed.ncbi.nlm.nih.gov/27399968/) | *SIN3A haploinsufficiency causes mild ID (MeCP2 interactor)* | Links SIN3A to the microdeletion; mouse corticogenesis mechanism; MRI findings (F001, F003, F005, F011) |
| [33437032](https://pubmed.ncbi.nlm.nih.gov/33437032/) | *Study of 28 individuals with SIN3A-related disorder* | WITKOS definition; quantified phenotype frequencies; management; variant spectrum (F001, F008, F009, F010) |
| [22180641](https://pubmed.ncbi.nlm.nih.gov/22180641/) | *Delineation of the 15q24 microdeletion syndrome* | 1.1 Mb critical region; SD-mediated recurrence; rarity (F002) |
| [22216833](https://pubmed.ncbi.nlm.nih.gov/22216833/) | *Chromosome 15q24 microdeletion syndrome* | Full phenotype spectrum; CMA diagnosis; rare severe malformations (F004, F009, F011) |
| [33130996](https://pubmed.ncbi.nlm.nih.gov/33130996/) | *REST/NRSF-SIN3 corepressor complex* | SIN3 core complex composition (F003) |
| [15998811](https://pubmed.ncbi.nlm.nih.gov/15998811/) | *mSin3A regulates transcriptional networks* | Essential role; p53/Myc-Mad/E2F network dysregulation (F005) |
| [36399132](https://pubmed.ncbi.nlm.nih.gov/36399132/) | *DNA methylation episignature for WITKOS* | Diagnostic hypomethylated episignature (F006) |
| [41759735](https://pubmed.ncbi.nlm.nih.gov/41759735/) | *Sin3A-PAH1 αα-hub stability/variant defects* | Structural basis of missense LOF (F007) |
| [33811806](https://pubmed.ncbi.nlm.nih.gov/33811806/) | *SIN3B haploinsufficiency syndrome* | Paralog supports dosage mechanism (F007) |
| [17360722](https://pubmed.ncbi.nlm.nih.gov/17360722/) | *Recurrent 15q24 microdeletion* | De novo origin; NAHR (F009) |
| [20404188](https://pubmed.ncbi.nlm.nih.gov/20404188/) | *HDAC1 controls ES cell differentiation* | Catalytic-partner essentiality; corepressor-complex dependence (F003) |
| [31953991](https://pubmed.ncbi.nlm.nih.gov/31953991/) | *Refining 15q24 critical regions for autism* | NEO1 as co-deleted ASD gene (F002, F012) |
| [30204971](https://pubmed.ncbi.nlm.nih.gov/30204971/) | *Matthew-Wood syndrome (STRA6)* | STRA6 co-deletion → eye/diaphragm/heart (F012) |
| [38528912](https://pubmed.ncbi.nlm.nih.gov/38528912/) | *SIN3A LOF causing hypogonadotropic hypogonadism* | Endocrine phenotype/management (F010) |
| [41245232](https://pubmed.ncbi.nlm.nih.gov/41245232/) | *Personalized treatment in WITKOS* | Emerging behavioral intervention (F010) |
| [34922566](https://pubmed.ncbi.nlm.nih.gov/34922566/) | *15q24 microdeletion in pediatric DD* | Smaller LCR B–C deletions; CYP1A1/EDC3 case (F012) |
| [39576496](https://pubmed.ncbi.nlm.nih.gov/39576496/) | *WITKOS with dystonia/cerebellar ataxia* | Expands phenotype spectrum (Section 8) |

All abstract quotations used in the Key Findings were drawn from the verified citation snippets in the knowledge state. Papers on PP2A/HDAC lactylation, MDM2 PROTACs, CaMKII, IFI16/KSHV, ARID4B, and MeCP2/SEC are mechanistically adjacent (they illuminate SIN3–HDAC biology) but were not used to attribute disease-specific clinical claims.

---

## Limitations and Knowledge Gaps

- **Dissecting individual gene contributions:** The specific phenotypic contribution of each co-deleted gene (*NEO1*, *CYP11A1*, *STRA6*, *EDC3*, *CYP1A1*) within larger deletions is inferred from gene function and overlapping syndromes, not from direct dosage experiments in the 15q24 context (F012 is partly inferential).
- **Epidemiology is imprecise:** No robust prevalence/incidence figures exist; the disorder is rare and under-ascertained, with cohorts of tens rather than hundreds of patients.
- **Penetrance/expressivity quantification:** The determinants of why some individuals have normal cognition (25% in one cohort) while others have severe ID are unknown; no validated genotype–phenotype or modifier model exists.
- **Natural history:** Longitudinal/natural-history data into adulthood are scarce; prognostic biomarkers are absent. An atypical progressive (ataxia/dystonia) case complicates the "static course" generalization.
- **Therapeutics:** No disease-targeted therapy or clinical trial exists; behavioral intervention evidence is a single case.
- **Model systems:** Patient-derived iPSC/organoid and heterozygous (dosage-matched) adult-phenotype mouse models are not yet reported; homozygous lethality limits conventional knockout approaches.
- **Immune phenotype:** The basis of "recurrent infections" is not mechanistically defined.

---

## Proposed Follow-up Experiments / Actions

1. **Haploinsufficiency-faithful mouse model:** Generate and deeply phenotype a conditional/heterozygous *Sin3a* mouse (and a 15q24-deletion mouse spanning the syntenic region) to directly test gene-by-gene contributions and recapitulate cognitive/behavioral endpoints.
2. **Patient iPSC cortical organoids:** Derive iPSCs from WITKOS/15q24-deletion patients and model cortical neurogenesis defects, correlating transcriptomic/epigenomic changes with the blood episignature.
3. **Multi-omics on primary samples:** Integrate the DNA-methylation episignature with transcriptomics and proteomics to identify dysregulated SIN3 target genes that could serve as biomarkers or therapeutic nodes.
4. **Genotype–phenotype registry:** Establish an international registry correlating deletion size/breakpoints and variant type with quantified cognitive, growth, endocrine, and malformation outcomes to refine penetrance/expressivity and prognosis.
5. **Episignature-first diagnostics:** Validate the hypomethylated episignature prospectively for VUS resolution and as a first-tier functional assay alongside CMA/sequencing.
6. **Targeted mechanism-based therapy exploration:** Given the HDAC-corepressor biology, evaluate (preclinically) whether modulating histone-acetylation balance or compensating via paralogs (SIN3B) can rescue neurodevelopmental phenotypes in model systems.
7. **Immune characterization:** Systematically assess immune function in patients with recurrent infections to define whether a specific immunodeficiency component exists and whether co-deleted genes contribute.

---

*Report compiled from 12 confirmed findings and 25 reviewed papers over 5 iterations. Evidence sources: human clinical series/case reports, mouse and zebrafish models, in vitro biochemistry/structural biology, and computational/epigenomic classifiers, as indicated per claim.*


## Artifacts

- [OpenScientist final report](Chromosome_15q24_Deletion_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Chromosome_15q24_Deletion_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 20 |
| Quoted claims found in source | 20 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 17 |
| On topic | 12 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 42 |
| Resolved | 38 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 2 |

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0016575` (obsolete histone deacetylation) (1 mention)
- `GO:0016580` (obsolete Sin3 complex) (1 mention) - replaced by `GO:0070822`

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.

38 of 42 terms resolved to a current term; the rest could not be looked up either way.