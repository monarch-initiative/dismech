---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-31T13:53:38.157438'
end_time: '2026-10-31T14:07:24.028985'
duration_seconds: 825.87
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Inherited Prekallikrein Deficiency
  mondo_id: MONDO:0012901
  category: Mendelian
  causal_genes: KLKB1
  omim_id: OMIM:612423
  synonyms: fletcher factor (prekallikrein) deficiency; congenital prekallikrein deficiency;
    hereditary prekallikrein deficiency
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
citation_count: 16
reference_validation:
  total_references: 19
  verified: 19
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 19
  on_topic: 13
  validator_version: 0.4.0
term_validation:
  total_terms: 14
  verified: 12
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 7
  labels_matching: 3
  labels_variant: 4
  obsolete_terms:
  - term_id: GO:0005615
    ontology_label: obsolete extracellular space
    replaced_by: GO:0005576
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Inherited_Prekallikrein_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Inherited_Prekallikrein_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Inherited Prekallikrein Deficiency
- **MONDO ID:** MONDO:0012901 (if available)
- **Causal gene(s):** KLKB1
- **OMIM:** OMIM:612423
- **Synonyms:** fletcher factor (prekallikrein) deficiency; congenital prekallikrein deficiency; hereditary prekallikrein deficiency
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Inherited Prekallikrein Deficiency** covering all of the
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

# Inherited Prekallikrein Deficiency (Fletcher Factor Deficiency): A Comprehensive Disease Characterization

**Disease:** Inherited Prekallikrein Deficiency
**MONDO ID:** MONDO:0012901 | **OMIM:** 612423 | **Causal gene:** *KLKB1* (plasma kallikrein B1 / prekallikrein; HGNC:6371; NCBI Gene 3818; OMIM *229000; chromosome 4q35)
**Synonyms:** Fletcher factor deficiency; congenital/hereditary/severe plasma prekallikrein (PK) deficiency

---

## Summary

Inherited prekallikrein deficiency is a rare **autosomal-recessive** disorder of the plasma **contact system**, caused by **biallelic loss-of-function variants in *KLKB1***, the gene that encodes the liver-synthesized zymogen **plasma prekallikrein** (also historically called **Fletcher factor**). Prekallikrein circulates bound to high-molecular-weight kininogen (HK) and, once converted to active plasma kallikrein by activated factor XII (FXIIa), participates in two intertwined cascades: it **reciprocally activates FXII** (amplifying intrinsic contact-phase coagulation) and it **liberates bradykinin** from HK (driving vascular permeability and vasodilation via the B2 receptor).

The defining clinical paradox of this disease is that, despite producing a **markedly prolonged activated partial thromboplastin time (aPTT)** in vitro, it causes **no bleeding diathesis**. This is because FXII can slowly auto-activate on anionic surfaces independently of kallikrein, preserving downstream thrombin generation and hemostasis in vivo. The condition is therefore best understood as a **benign laboratory phenotype rather than a true coagulopathy** — typically discovered incidentally during preoperative or routine coagulation screening in an asymptomatic person. The hallmark laboratory signature is an isolated, severely prolonged aPTT with normal PT that **shortens upon prolonged pre-incubation** of plasma with the contact activator, corrects on mixing with normal plasma but **not** with PK-deficient plasma, and is accompanied by **normal thromboelastography (TEG)**.

Prognosis is excellent: a 111-case meta-analysis found only 4 major bleeding events among 96 individuals (prevalence 4%, annualized rate 0.1% — comparable to the general population). The deficiency does **not** protect against thrombosis, and cardiovascular events accumulate with age. No specific treatment is required; fresh frozen plasma (FFP) is used only to normalize the activated clotting time so that heparin anticoagulation can be monitored during surgery. The disease's underlying biology is clinically consequential far beyond the deficiency itself: plasma kallikrein is a validated drug target in **bradykinin-mediated hereditary angioedema (HAE)**, and agents that lower prekallikrein (e.g., the antisense oligonucleotide **donidalorsen**) or inhibit kallikrein (**lanadelumab, berotralstat, sebetralstat**) pharmacologically **phenocopy the deficiency** while proving safe and effective.

---

## Key Findings

### 1. The disease is an autosomal-recessive contact-system defect causing isolated prolonged aPTT without bleeding

Severe plasma prekallikrein deficiency is inherited as an autosomal-recessive trait and is characterized by **isolated aPTT prolongation**. The largest synthesis to date (Barco et al. 2020) assembled **111 cases from 89 families** and found only **4 major bleeding events among 96 individuals (3 of them provoked), for a prevalence of 4% and an annualized rate of 0.1%** — indistinguishable from the general population.

> *"Severe plasma prekallikrein (PK) deficiency is an autosomal-recessive defect characterized by isolated activated partial thromboplastin time prolongation."* — [PMID: 32202057](https://pubmed.ncbi.nlm.nih.gov/32202057/)

The mechanistic reason bleeding is absent is that **FXII retains the ability to auto-activate**:

> *"Because patients with prekallikrein deficiency have preserved auto-activation of factor XII, they rarely manifest with increased bleeding risk or thrombotic risk."* — [PMID: 40125216](https://pubmed.ncbi.nlm.nih.gov/40125216/)

### 2. Prevalence is low overall but markedly enriched in African ancestry

Using gnomAD allele frequencies and the population-based Gutenberg Health Study, severe PK deficiency prevalence was estimated at **1/155,668 overall and 1/4,725 among individuals of African ancestry** — a ~33-fold enrichment suggesting common/founder loss-of-function *KLKB1* alleles in that population. The ~111 reported cases from 89 families indicate substantial under-ascertainment, consistent with an asymptomatic disorder.

> *"estimated a prevalence of severe PK deficiency of 1/155 668 overall and 1/4725 among Africans"* — [PMID: 32202057](https://pubmed.ncbi.nlm.nih.gov/32202057/)

### 3. Prekallikrein is a multidomain contact-system zymogen with a dual role in coagulation and inflammation

*KLKB1* encodes plasma prekallikrein, a liver-synthesized zymogen that circulates bound to HK. Structurally it comprises **four apple domains plus one catalytic serine-protease domain**. Factor XI (FXI), a homodimer with the same domain architecture, arose evolutionarily through a duplication of *KLKB1*. Functionally, FXIIa converts prekallikrein to kallikrein, which then reciprocally activates FXII and cleaves HK to release bradykinin, and also activates pro-urokinase (linking the system to fibrinolysis).

> *"it converts plasma prekallikrein to kallikrein (PK), which reciprocally activates FXII and liberates bradykinin from high molecular weight kininogen"* — [PMID: 30118759](https://pubmed.ncbi.nlm.nih.gov/30118759/)

> *"the coagulation factor XI (FXI) arose through a duplication of the gene KLKB1, which encodes plasma prekallikrein"* — [PMID: 37874916](https://pubmed.ncbi.nlm.nih.gov/37874916/)

### 4. Diagnosis rests on a characteristic aPTT pattern confirmed by mixing studies and specific assay

Severe PK deficiency produces a markedly prolonged aPTT (reported examples: **87.4 s** [reference 24.5–34.0] and **146 s**) with normal PT, thrombin time, and anti-FXa. The aPTT characteristically **shortens with prolonged pre-incubation** of plasma with contact activator — a diagnostic clue — **corrects on mixing with normal plasma but not with PK-deficient plasma**, and is confirmed by a low specific PK assay. Western immunoblot may show absent PK antigen (cross-reactive-material–negative). Critically, **viscoelastic testing (TEG) is normal**, confirming there is no true in vivo coagulopathy.

> *"The aPTT corrected on mixing with normal pooled plasma but not with PK-deficient plasma."* — [PMID: 42454615](https://pubmed.ncbi.nlm.nih.gov/42454615/)

> *"Despite the prolonged aPTT, TEG 6s parameters were normal, including the citrated kaolin R time"* — [PMID: 42454615](https://pubmed.ncbi.nlm.nih.gov/42454615/)

> *"His PTT characteristically became shorter with prolonged incubation, providing a clue at testing for PK levels"* — [PMID: 32617222](https://pubmed.ncbi.nlm.nih.gov/32617222/)

### 5. Prekallikrein-null mice are hemostatically normal but protected from thromboinflammation

*Klkb1*-knockout (*Klkb1*−/−) mice are viable and fertile with **no spontaneous bleeding**, mirroring the human phenotype. However, they are **protected across multiple thromboinflammatory models**: reduced neurologic deterioration and brain edema in experimental cerebral malaria; attenuated imiquimod-induced psoriatic skin inflammation with abolished bradykinin rise; and protection from extracellular-vesicle–induced pulmonary thrombosis (a protection shared by FXII, HK, and prekallikrein deficiency). Prekallikrein ablation also stabilizes the LDL receptor, lowers LDL cholesterol, and protects against atherosclerosis — revealing unexpected metabolic roles.

> *"Prekallikrein-null (Klkb1-/-), prolylcarboxypeptidase hypomorph ... mice with ECM had reduced neurologic deterioration and brain edema."* — [PMID: 42446942](https://pubmed.ncbi.nlm.nih.gov/42446942/)

> *"Genetic deletion of Factor XII or prekallikrein, attenuated imiquimod-induced psoriatic lesions in mice."* — [PMID: 38872396](https://pubmed.ncbi.nlm.nih.gov/38872396/)

> *"Ablation of PK stabilizes LDLR, decreases LDL cholesterol, and prevents atherosclerotic plaque development."* — [PMID: 35189703](https://pubmed.ncbi.nlm.nih.gov/35189703/)

### 6. Pathogenic *KLKB1* variants are predominantly biallelic truncating/loss-of-function, spread across the gene

Reported pathogenic variants span the gene and include: homozygous **c.417_418insCATTCTTA (p.Arg140Hisfs\*3)** in exon 5; homozygous **c.444_445insT (p.Ser151PhefsTer34)**; and compound heterozygous **1-bp insertion at codon 149 (exon 5)** plus **c.1643G>A (p.Cys548Tyr)** (exon 14). Both **cross-reactive-material–negative** forms (absent antigen; frameshift/nonsense) and **CRM-positive** forms (dysfunctional protein; missense) occur. Variant curation is ongoing: Barco et al. identified new *KLKB1* mutations while reclassifying some previously reported ones as non-pathogenic.

> *"an insertion of 1 bp in codon 149 in exon 5 and, second, a base exchange Cys 548 (TGC) > Tyr (TAC) in exon 14"* — [PMID: 19404525](https://pubmed.ncbi.nlm.nih.gov/19404525/)

> *"We identified new KLKB1 mutations, excluded the pathogenicity of some of the previously described ones"* — [PMID: 32202057](https://pubmed.ncbi.nlm.nih.gov/32202057/)

### 7. Surgery is generally safe without prophylaxis; cardiovascular risk rises with age

Numerous case reports describe **uneventful surgery and procedures** in PK-deficient patients — hallux amputation, kidney biopsy, deep brain stimulator placement, endovascular aortic repair, and heart transplantation. FFP is sometimes given empirically, but reviews conclude **routine prophylaxis is not indicated**. FFP's genuine utility is in **replenishing prekallikrein to normalize the activated clotting time (ACT)**, enabling heparin monitoring during cardiac/vascular surgery. The Barco cohort reported an overall cardiovascular-event prevalence of **15%**, age-stratified at **6% (<40 y), 21% (40–65 y), 33% (>65 y)**.

> *"Our review suggests that routine prophylactic administration of blood products for pre-operative management of this condition is not indicated"* — [PMID: 40125216](https://pubmed.ncbi.nlm.nih.gov/40125216/)

> *"Preoperative prekallikrein replenishment by fresh frozen plasma administration contributed to safe intraoperative anticoagulation management."* — [PMID: 41123211](https://pubmed.ncbi.nlm.nih.gov/41123211/)

### 8. The disease does NOT protect against thrombosis despite a severe in vitro coagulation defect

Girolami et al. analyzed all 75 then-published PK-deficiency cases and identified **9 with thrombosis — 6 arterial (myocardial infarction, ischemic stroke) and 3 venous (DVT ± pulmonary embolism)**; 6 had acquired thrombotic risk factors, and one patient with both stroke and PE died. They concluded the deficiency does not protect from thrombosis. This fits the broader understanding that plasma kallikrein contributes to thrombosis while playing a limited hemostatic role.

> *"prekallikrein deficiency does not protect from thrombosis in spite of the severe in vitro coagulation defect"* — [PMID: 20424433](https://pubmed.ncbi.nlm.nih.gov/20424433/)

> *"Among these patients were 9 with thrombosis, 6 arterial (myocardial infarction and ischemic stroke) and 3 venous (deep vein thrombosis with or without pulmonary embolism)."* — [PMID: 20424433](https://pubmed.ncbi.nlm.nih.gov/20424433/)

### 9. The biology underpins safe, effective hereditary angioedema (HAE) therapeutics

Plasma kallikrein — the activated product of *KLKB1* — is a validated drug target in bradykinin-mediated HAE. Approved/advanced agents include the anti-kallikrein monoclonal antibody **lanadelumab**, oral kallikrein inhibitors **berotralstat** and **sebetralstat**, and the antisense oligonucleotide **donidalorsen**, which lowers prekallikrein production directly in the liver and achieves up to ~90% attack-rate reduction. Donidalorsen thus **pharmacologically phenocopies inherited PK deficiency** and is well tolerated — exactly what the benign natural deficiency predicts.

> *"Donidalorsen is a triantennary N-acetyl galactosamine-conjugated antisense oligonucleotide designed to specifically and reversibly reduce plasma prekallikrein production by binding to plasma prekallikrein messenger RNA in the liver."* — [PMID: 42415941](https://pubmed.ncbi.nlm.nih.gov/42415941/)

> *"the first orally available plasma kallikrein inhibitor, sebetralstat"* — [PMID: 42550203](https://pubmed.ncbi.nlm.nih.gov/42550203/)

### 10. The differential diagnosis of isolated prolonged aPTT is narrow

Isolated prolonged aPTT with normal PT in an asymptomatic patient narrows to: deficiencies of the contact factors **FXII, prekallikrein (*KLKB1*), or HK (*KNG1*)** — all bleeding-silent — plus **lupus anticoagulant** and clinically significant intrinsic-factor deficiencies (FVIII/IX/XI, which usually bleed). Severe HK deficiency (*KNG1*, biallelic truncating variants; prevalence ~1/8 million, higher in Africans) is asymptomatic and also shows **decreased prekallikrein and FXI activity**, which can cause misdiagnosis. PK deficiency is distinguished by aPTT shortening on pre-incubation, non-correction with PK-deficient plasma, normal kininogen activity, and a low specific PK assay; NGS panels resolve ambiguous cases.

> *"Individuals with HK deficiency appeared asymptomatic and had decreased levels of prekallikrein and factor XI, which could lead to misdiagnosis."* — [PMID: 36700498](https://pubmed.ncbi.nlm.nih.gov/36700498/)

### 11. Inheritance and temporal profile

Severe PK deficiency is **autosomal recessive**, requiring two defective *KLKB1* alleles; **heterozygous carriers are asymptomatic with ~50% PK activity** (no dominant phenotype). It is **congenital and lifelong** but, being asymptomatic, is typically discovered **incidentally at any age** (reported probands range from a 14-year-old boy to adults in their 60s–70s). Multiple cases arise in **consanguineous families**. There is **no sex predilection, no genetic anticipation** (not a repeat-expansion disorder), and **no reported chromosomal or epigenetic mechanism**. About one-quarter of PK-deficient individuals also show below-reference FXII activity.

> *"One quarter of individuals had factor XII clotting activity below the reference range."* — [PMID: 32202057](https://pubmed.ncbi.nlm.nih.gov/32202057/)

---

## Section-by-Section Report

### 1. Disease Information
Inherited prekallikrein deficiency (Fletcher factor deficiency) is a rare, benign, autosomal-recessive defect of the plasma contact (kallikrein-kinin) system caused by biallelic *KLKB1* variants. **Identifiers:** MONDO:0012901; OMIM 612423 (phenotype); gene *KLKB1* (OMIM *229000, HGNC:6371, NCBI Gene 3818, chr 4q35). **ICD-10:** D68.8 (other specified coagulation defects). **MeSH:** "Prekallikrein" / contact factor deficiencies. **Synonyms:** Fletcher factor deficiency, congenital/hereditary/severe plasma prekallikrein deficiency. Information derives primarily from **aggregated case series/registries and case reports** (e.g., Barco et al. 111-case meta-analysis), not population EHR.

### 2. Etiology
**Causal factor:** genetic — biallelic loss-of-function variants in *KLKB1*. **Genetic risk:** homozygous or compound-heterozygous pathogenic *KLKB1* alleles; **consanguinity** and **African ancestry** (founder LoF alleles) raise risk. There are **no established environmental risk or protective factors** and no gene-environment interactions for the deficiency per se; the deficiency is fully penetrant at the biochemical (aPTT) level but has essentially no clinical consequence. No protective genetic modifiers are defined. The ~25% of patients with concomitant low FXII is a correlated biochemical finding rather than a modifier of outcome.

### 3. Phenotypes
The **sole reliable phenotype is a laboratory abnormality**: isolated, markedly prolonged aPTT with normal PT (HPO **HP:0003645** "Prolonged partial thromboplastin time"; broadly **HP:0003256** "Abnormality of coagulation"). Onset is **congenital/lifelong**; severity of the lab finding is **severe** (aPTT often 2–5× upper limit) but clinically **asymptomatic and stable (non-progressive)**. Frequency: the aPTT abnormality is present in ~100% of severely deficient individuals; clinically significant bleeding occurs in only ~4% (mostly provoked). **Quality-of-life impact is negligible** — the main burden is diagnostic workup, unnecessary procedure delays, and anxiety from an "abnormal" test.

### 4. Genetic/Molecular Information
**Causal gene:** *KLKB1* (HGNC:6371). **Variant classes:** predominantly truncating/frameshift/nonsense (loss of function) plus some missense (e.g., p.Cys548Tyr) producing dysfunctional protein; documented variants include p.Arg140Hisfs\*3, p.Ser151PhefsTer34, and compound-heterozygous genotypes. **Classification:** per ACMG, truncating variants reach Pathogenic (e.g., PVS1+PM2+PM4). **Allele frequency:** individual variants are rare in gnomAD, but aggregate LoF burden is higher in African-ancestry populations. **Origin:** germline. **Functional consequence:** loss of function (absent or non-functional zymogen). **Modifier genes/epigenetics/chromosomal abnormalities:** none established. Concomitant mild FXII reduction occurs in ~25% of cases but is not a formal modifier.

### 5. Environmental Information
Not applicable as a cause. The deficiency is purely genetic; no toxins, lifestyle factors, or infectious agents cause it. (Contextually, the contact system it belongs to is *activated* by negatively charged surfaces, heme, polyphosphate, nanoparticles, and pathogens in various disease states, but these do not cause the inherited deficiency.)

### 6. Mechanism / Pathophysiology

**Ordered causal chain:**

1. **Biallelic *KLKB1* loss-of-function variants** → *lead to* absent or non-functional plasma prekallikrein zymogen.
2. → *results in* no FXIIa-mediated conversion of prekallikrein to active plasma kallikrein.
3. **Branch A (coagulation):** loss of the reciprocal kallikrein→FXII amplification loop → *slows* contact activation **in vitro** → *produces* a markedly prolonged aPTT. **However**, FXII still slowly auto-activates on anionic surfaces and activates FXI→FIX, so thrombin generation and **hemostasis are preserved in vivo** → **no bleeding** (this redundancy is *inferred* from the absence of bleeding in deficient humans and *Klkb1*−/− mice).
4. **Branch B (kallikrein-kinin):** no kallikrein → no cleavage of HK → **no bradykinin release** → *loss of* B2-receptor signaling (reduced NO/prostacyclin, vasodilation, vascular permeability). This branch explains the thromboinflammation protection of knockout mice but has no overt clinical signature in deficient humans.
5. **Branch C (fibrinolysis):** reduced kallikrein-mediated pro-urokinase/plasminogen activation (minor, *inferred*).

**Molecular pathway:** complement and coagulation cascades / kallikrein-kinin system (KEGG hsa04610). **Cellular processes:** surface-induced contact activation, inflammation. **Protein dysfunction:** loss of serine-protease function of plasma kallikrein. **Biochemical abnormality:** enzyme (zymogen) deficiency. The reciprocal activation loop and bradykinin liberation are **experimentally established**; the in vivo dispensability of PK for hemostasis is **inferred** from phenotype.

> *"The contact system, also named as plasma kallikrein-kinin system, consists of three serine proteinases: coagulation factors XII (FXII) and XI (FXI), and plasma prekallikrein (PK), and the nonenzymatic cofactor high molecular weight kininogen (HK)."* — [PMID: 25949215](https://pubmed.ncbi.nlm.nih.gov/25949215/)

**Suggested GO terms:** GO:0007596 (blood coagulation), GO:0002542 (Factor XII activation), GO:0032277 (regulation of kallikrein-kinin cascade); **CL terms:** CL:0000182 (hepatocyte, site of synthesis), CL:0000115 (endothelial cell, site of surface activation). **CHEBI:** bradykinin (CHEBI:3165).

### 7. Anatomical Structures Affected
There is **no structural organ damage**. The affected "compartment" is the **blood plasma** (UBERON:0001969 blood plasma) within the **cardiovascular/hematologic system** (UBERON:0000178 blood). Site of protein synthesis: **liver** (UBERON:0002107), specifically **hepatocytes** (CL:0000182). Subcellular: secreted protein; relevant GO cellular component GO:0005615 (extracellular space). No tissue/cell type is injured in the inherited deficiency; lateralization is not applicable.

### 8. Temporal Development
**Onset:** congenital (present from birth), lifelong. **Pattern:** stable, non-progressive, asymptomatic. Detected **incidentally at any age** via coagulation screening. No disease stages, no remission/relapse, no critical intervention window. Duration: chronic lifelong but clinically silent.

### 9. Inheritance and Population
**Inheritance:** autosomal recessive; carriers (~50% activity) asymptomatic. **Prevalence:** ~1/155,668 overall; ~1/4,725 in African ancestry. **Penetrance:** complete for the biochemical (aPTT) phenotype; negligible clinical penetrance. **Expressivity:** uniform at the lab level. **No anticipation, no mosaicism reported.** **Founder effect/consanguinity:** likely founder LoF alleles in African populations; multiple consanguineous pedigrees reported (Chinese, Middle Eastern). **Sex ratio:** ~1:1. **Carrier frequency:** elevated in African ancestry per gnomAD.

### 10. Diagnostics
**Core workup:** isolated prolonged aPTT with normal PT → mixing study (corrects with normal plasma, **not** with PK-deficient plasma) → **aPTT shortens on prolonged pre-incubation** → **specific plasma prekallikrein activity assay** (severely low, often <1%). Normal activities of FVIII, FIX, FXI, FXII, vWF and negative lupus anticoagulant screen exclude alternatives; normal kininogen distinguishes from HK deficiency. **Viscoelastic testing (TEG) is normal.** **Genetic confirmation:** single-gene *KLKB1* sequencing or NGS bleeding-disorder panels resolve ambiguous cases. LOINC: aPTT (LOINC 14979-9). Caution: shortening-on-pre-incubation alone is not fully specific and should be confirmed by assay (PMID 35377536).

### 11. Outcome / Prognosis
**Excellent / benign.** Normal life expectancy; no disease-specific mortality. Major bleeding ~4% (0.1%/yr), mostly provoked. **No protection from thrombosis**; cardiovascular events rise with age (6%→21%→33% across age bands). No disability or QoL impairment attributable to the deficiency. Main "complications" are iatrogenic/diagnostic (procedure delays, unnecessary transfusion).

### 12. Treatment
**No specific therapy is needed.** Management is reassurance and avoidance of unnecessary intervention. **FFP** is used selectively to replenish prekallikrein and **normalize ACT for intraoperative heparin monitoring** (not for hemostasis). Suggested NCIT: Fresh Frozen Plasma (transfusion). No pharmacotherapy, gene/cell/RNA therapy is indicated for the deficiency itself. (The inverse — drugs that *reduce* kallikrein/prekallikrein, e.g., lanadelumab, donidalorsen — are therapies for HAE, not for this deficiency.)

### 13. Prevention
Not preventable (genetic). **Genetic counseling** for autosomal-recessive recurrence risk (25% for carrier couples), **cascade testing** of relatives with unexplained prolonged aPTT, and **carrier awareness** in consanguineous/African-ancestry families are appropriate. No newborn screening or prophylaxis is warranted given the benign course. Tertiary "prevention" = avoiding unnecessary transfusion and ensuring correct anticoagulation monitoring during surgery.

### 14. Other Species / Natural Disease
The orthologous gene exists across mammals (mouse *Klkb1*, NCBI Gene 16621). No prominent naturally occurring companion-animal or wildlife disease is established in OMIA for prekallikrein deficiency; the primary cross-species evidence is the engineered mouse knockout. The contact system and its reciprocal activation/bradykinin biology are evolutionarily conserved; FXI is a *KLKB1* gene-duplication paralog.

### 15. Model Organisms
**Primary model:** *Klkb1*−/− knockout mouse (mammalian). **Phenotype recapitulation:** excellent for the *human* phenotype — viable, fertile, normal hemostasis, no spontaneous bleeding. **Added value beyond human data:** reveals protective roles not observable clinically — protection from experimental cerebral malaria (bradykinin-mediated edema), psoriasiform skin inflammation, EV-induced pulmonary thrombosis, and atherosclerosis (via LDLR stabilization). **Limitation:** mouse-human differences in contact-system/FXI biology mean thrombosis-protection findings do not fully transfer to humans (humans are *not* protected from thrombosis). Resources: MGI.

---

## Mechanistic Model / Interpretation

```
   Biallelic KLKB1 loss-of-function variants
                    │
                    ▼
     Absent / non-functional plasma prekallikrein (zymogen)
                    │
                    ▼
     No FXIIa → kallikrein conversion (no active plasma kallikrein)
        │                         │                         │
   BRANCH A                  BRANCH B                   BRANCH C
 (coagulation)          (kallikrein-kinin)           (fibrinolysis)
        │                         │                         │
 Loss of reciprocal        No HK cleavage →          Reduced pro-urokinase
 kallikrein→FXII loop      no bradykinin             activation (minor)
        │                   release                        │
        ▼                         │                        ▼
 Slowed contact                   ▼                 (no clinical signature)
 activation IN VITRO       Loss of B2-receptor
        │                  signaling (↓NO, ↓vasodilation,
        ▼                  ↓vascular permeability)
 PROLONGED aPTT                   │
        │                         ▼
   BUT: FXII auto-         Explains thromboinflammation
   activates on surfaces   PROTECTION in Klkb1-/- mice
        │                  (NOT clinically evident in humans)
        ▼
 Thrombin generation &
 hemostasis PRESERVED
        │
        ▼
   NO BLEEDING  →  Benign laboratory phenotype
```

The central insight is **redundancy**: prekallikrein amplifies but is not required to *initiate* the intrinsic cascade. FXII's independent surface auto-activation provides a parallel route to FXI→FIX→thrombin, decoupling the dramatic in-vitro aPTT prolongation from any in-vivo hemostatic failure. The disease is therefore a textbook example of a **laboratory phenotype without a disease phenotype**.

| Feature | Prekallikrein (KLKB1) deficiency | FXII deficiency | HK (KNG1) deficiency | FXI deficiency |
|---|---|---|---|---|
| Prolonged aPTT | Yes (severe) | Yes | Yes | Yes |
| Bleeding tendency | No | No | No | Variable (yes) |
| aPTT shortens on pre-incubation | **Yes (hallmark)** | No | No | No |
| Corrects with PK-deficient plasma | **No** | Yes | Yes | Yes |
| Kininogen activity | Normal | Normal | **Low** | Normal |
| Inheritance | AR | AR | AR | AR/AD |

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [32202057](https://pubmed.ncbi.nlm.nih.gov/32202057/) | Severe plasma PK deficiency: characteristics, novel KLKB1 mutations, prevalence | Anchor: inheritance, benign bleeding profile, prevalence (1/155,668; 1/4,725 African), CV events, variant discovery |
| [40125216](https://pubmed.ncbi.nlm.nih.gov/40125216/) | Case + review: isolated aPTT prolongation | Mechanism (FXII auto-activation), no prophylaxis needed |
| [30118759](https://pubmed.ncbi.nlm.nih.gov/30118759/) | Factor XII in coagulation, inflammation | Reciprocal activation + bradykinin liberation |
| [37874916](https://pubmed.ncbi.nlm.nih.gov/37874916/) | Biology of factor XI | KLKB1 structure; FXI as gene-duplication paralog |
| [42454615](https://pubmed.ncbi.nlm.nih.gov/42454615/) | Normal TEG with prolonged aPTT in PK deficiency | Mixing-study pattern; normal viscoelastic testing |
| [32617222](https://pubmed.ncbi.nlm.nih.gov/32617222/) | Diagnostic pearls of PK deficiency | aPTT shortening on pre-incubation |
| [42446942](https://pubmed.ncbi.nlm.nih.gov/42446942/) | Bradykinin in cerebral malaria | Klkb1-/- protection from brain edema |
| [38872396](https://pubmed.ncbi.nlm.nih.gov/38872396/) | FXII/prekallikrein in psoriasis | Knockout protection from skin inflammation |
| [35189703](https://pubmed.ncbi.nlm.nih.gov/35189703/) | PK ablation & atherosclerosis | LDLR stabilization, atheroprotection in mice |
| [19404525](https://pubmed.ncbi.nlm.nih.gov/19404525/) | Compound heterozygous KLKB1 | Specific variant documentation |
| [41123211](https://pubmed.ncbi.nlm.nih.gov/41123211/) | Endovascular aortic repair in PK deficiency | FFP for ACT normalization / anticoagulation monitoring |
| [20424433](https://pubmed.ncbi.nlm.nih.gov/20424433/) | Thrombotic events in PK deficiency | No thrombosis protection; 9/75 thrombotic |
| [42415941](https://pubmed.ncbi.nlm.nih.gov/42415941/) | Donidalorsen review | Drug phenocopying deficiency is safe HAE therapy |
| [42550203](https://pubmed.ncbi.nlm.nih.gov/42550203/) | Bradykinin-mediated angioedema therapies | Sebetralstat / kallikrein as drug target |
| [36700498](https://pubmed.ncbi.nlm.nih.gov/36700498/) | Severe HK (KNG1) deficiency | Key differential diagnosis |
| [25949215](https://pubmed.ncbi.nlm.nih.gov/25949215/) | Contact pathway of coagulation | Contact-system components |
| [42755375](https://pubmed.ncbi.nlm.nih.gov/42755375/) | Prekallikrein: crossroads of inflammation & thrombosis | Confirms non-bleeding nature |
| [33807613](https://pubmed.ncbi.nlm.nih.gov/33807613/) | NGS for bleeding-disorder differential diagnosis | Molecular resolution of ambiguous cases |

---

## Limitations and Knowledge Gaps

- **Under-ascertainment:** Only ~111 cases from 89 families are reported for an asymptomatic disorder; true prevalence and the full variant spectrum are uncertain. Prevalence estimates are **model-based** (gnomAD + one German cohort), not from direct population screening.
- **Cardiovascular/thrombotic risk:** Evidence that the deficiency does *not* protect from thrombosis comes from a case-series analysis (inherently subject to reporting bias and confounding by acquired risk factors); no controlled cohort quantifies relative thrombotic risk versus the general population.
- **Mouse-human divergence:** The striking thromboinflammation and atheroprotection phenotypes of *Klkb1*−/− mice do **not** translate to a protected clinical phenotype in deficient humans — contact-system and FXI biology differ across species.
- **Variant curation:** Some historically reported variants have been reclassified; a few assays (e.g., shortening-on-pre-incubation) are not fully specific. Standardized ACMG curation of all *KLKB1* alleles is incomplete.
- **No prospective natural-history or quality-of-life data** exist; QoL impact is inferred as negligible but not formally measured.
- **Epigenetic/modifier biology** of the deficiency is essentially unstudied (and likely uninformative given the benign phenotype).

---

## Proposed Follow-up Actions

1. **Population-scale carrier/prevalence screening** in African-ancestry cohorts (e.g., mining large biobanks: UK Biobank, All of Us, H3Africa) to confirm founder *KLKB1* LoF alleles and refine prevalence beyond model estimates.
2. **Matched-cohort thrombosis study**: compare cardiovascular/thrombotic incidence in biobank-identified biallelic *KLKB1* LoF carriers versus controls to settle the "no protection from thrombosis" question with controlled data.
3. **Systematic ACMG re-curation** of all reported *KLKB1* variants in ClinVar, resolving CRM-positive vs CRM-negative mechanism for each.
4. **Prospective registry** capturing perioperative outcomes to formally establish that FFP prophylaxis is unnecessary and to standardize ACT-monitoring protocols during anticoagulation.
5. **Clinical correlation of pharmacologic phenocopy**: leverage long-term safety data from donidalorsen/lanadelumab-treated HAE patients (who are pharmacologically PK-deficient) as a real-world "experiment" confirming the benign nature of profound prekallikrein/kallikrein suppression.
6. **Diagnostic standardization**: validate a confirmatory algorithm (specific PK assay + *KLKB1* sequencing) to avoid reliance on the non-specific pre-incubation test and prevent misclassification as HK or FXII deficiency.

---

*Evidence source types represented: human clinical (case series, case reports, meta-analysis), model organism (mouse knockouts), and in vitro/biochemical (contact-system activation studies). This report synthesizes 13 confirmed findings across ~40 papers from a five-iteration investigation.*


## Artifacts

- [OpenScientist final report](Inherited_Prekallikrein_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Inherited_Prekallikrein_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 19 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 19 |
| On topic | 13 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 14 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 7 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 4 |

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005615` (obsolete extracellular space) (1 mention) - replaced by `GO:0005576`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0032277` (1 mention) - the report calls it "regulation of kallikrein-kinin cascade"; GO calls it **negative regulation of gonadotropin secretion**, and lists "downregulation of gonadotropin secretion" among its other names
- `CL:0000182` (2 mentions) - the report calls it "hepatocyte, site of synthesis", "hepatocytes"; CL calls it **hepatocyte**
- `CL:0000115` (1 mention) - the report calls it "endothelial cell, site of surface activation"; CL calls it **endothelial cell**
- `GO:0005615` (1 mention) - the report calls it "extracellular space"; GO calls it **obsolete extracellular space**, and lists "intercellular space" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000182` - called "hepatocyte, site of synthesis", "hepatocytes"

12 of 14 terms resolved to a current term; the rest could not be looked up either way.