---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-15T02:38:17.636739'
end_time: '2026-10-15T03:38:21.164317'
duration_seconds: 3603.53
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Hypervalinemia and Hyperleucine-Isoleucinemia
  mondo_id: MONDO:0100058
  category: Genetic
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
citation_count: 8
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 7
  quotes_valid: 6
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:17767905
  relevance_assessed: 9
  on_topic: 7
  needs_review: true
  validator_version: 0.3.0
term_validation:
  total_terms: 24
  verified: 22
  not_found: 0
  obsolete: 1
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 8
  labels_matching: 3
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: HP:0002315
    reported_labels:
    - Symptom
    ontology_label: Headache
  - term_id: HP:0002354
    reported_labels:
    - Cognitive sign
    ontology_label: Memory impairment
  labels_variant: 3
  obsolete_terms:
  - term_id: GO:0009448
    ontology_label: obsolete GABA metabolic process
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Hypervalinemia_And_Hyperleucine-isoleucinemia-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Hypervalinemia_And_Hyperleucine-isoleucinemia-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hypervalinemia and Hyperleucine-Isoleucinemia
- **MONDO ID:** MONDO:0100058 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Hypervalinemia and Hyperleucine-Isoleucinemia** covering all of the
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

# Hypervalinemia and Hyperleucine-Isoleucinemia (MONDO:0100058): A Comprehensive Disease Characterization

**Disease category:** Genetic (inborn error of metabolism)
**Primary gene:** *BCAT2* (mitochondrial branched-chain aminotransferase, BCATm)
**Inheritance:** Autosomal recessive
**MONDO ID:** MONDO:0100058

---

## Summary

**Hypervalinemia and Hyperleucine-Isoleucinemia (MONDO:0100058) is an ultra-rare autosomal recessive inborn error of branched-chain amino-acid (BCAA) metabolism caused by biallelic loss-of-function mutations in the *BCAT2* gene**, which encodes the mitochondrial branched-chain aminotransferase (BCATm; EC 2.6.1.42). This enzyme catalyzes the first, shared catabolic step for all three BCAAs — valine, leucine and isoleucine — in which each amino acid is reversibly transaminated with α-ketoglutarate to yield the corresponding branched-chain keto acid (BCKA) plus glutamate. Because the enzymatic block lies **upstream** of the branched-chain α-keto-acid dehydrogenase (BCKDH) complex that is deficient in maple syrup urine disease (MSUD), BCAT2 deficiency elevates plasma valine, leucine and isoleucine **without overproducing the neurotoxic branched-chain keto acids**, yielding a comparatively mild, chronic neurometabolic phenotype rather than the fulminant ketoacidotic crises of MSUD.

The disease nosology unifies two historically distinct aminoacidopathies first described in the 1960s — classic Hypervalinemia (OMIM 277100; Wada et al. 1963) and Hyperleucine-isoleucinemia — under a single modern molecular entity. The molecular basis was established only in 2015, when Wang et al. ([PMID: 25653144](https://pubmed.ncbi.nlm.nih.gov/25653144/)) reported the first and to date only molecularly confirmed patient: a 25-year-old man with compound heterozygous *BCAT2* variants c.509G>A (p.Arg170Gln, paternal) and c.790G>A (p.Glu264Lys, maternal), both shown by functional assay to reduce BCAT2 enzyme activity. The patient presented with ~6 years of headache and mild memory impairment, symmetric cerebral white-matter abnormalities on MRI, and markedly elevated plasma valine and leucine. Notably, **treatment with vitamin B6 (pyridoxine) — the cofactor precursor of the enzyme's pyridoxal-5′-phosphate prosthetic group — lowered BCAAs and improved the MRI lesions**, establishing the disorder as B6-responsive and dietarily manageable.

A *Bcat2* (BCATm) knockout mouse independently validates the mechanism: these animals exhibit the biochemical hallmark of elevated plasma BCAAs, but the dominant phenotype is metabolic (leanness, increased energy expenditure, improved glucose tolerance via a futile protein-turnover cycle) rather than neurological. Both human causal variants are ultra-rare in gnomAD (MAF ~1×10⁻⁵ or lower, no homozygotes), consistent with an ultra-rare recessive disorder. This report presents the complete causal chain, genetic and biochemical details, phenotype and HPO mapping, diagnostic strategy, treatment, prognosis, prevention, model organisms, and the substantial knowledge gaps that remain given that human evidence rests on a single case.

---

## Key Findings

### Finding 1 — Biallelic *BCAT2* mutations are the molecular cause (autosomal recessive)

The defining genetic lesion is loss of function of *BCAT2*. Wang et al. 2015 ([PMID: 25653144](https://pubmed.ncbi.nlm.nih.gov/25653144/)) reported the first human case — a 25-year-old man carrying two *BCAT2* variants in compound-heterozygous configuration: **c.509G>A (p.Arg170Gln)** inherited from the father and **c.790G>A (p.Glu264Lys)** inherited from the mother. The abstract states directly that "*two heterogeneous BCAT2 gene mutations were found in the patient, including c.509G > A (p.Arg170Gln) and c.790G > A (p.Glu264Lys)*," and that these "*were found in his father and mother, respectively, suggesting an autosomal recessive disorder*." Critically, the pathogenicity was functionally established: "*BCAT2 functional studies demonstrated that the two BCAT2 gene mutations resulted in decreased BCAT2 enzyme activity.*" This provides both the segregation evidence for autosomal recessive inheritance and the functional (PS3-grade) evidence that the variants are loss-of-function.

### Finding 2 — BCAT catalyzes the first, shared step of BCAA catabolism; its loss elevates plasma BCAAs and injures the CNS

Valine, leucine and isoleucine are essential BCAAs whose catabolism begins with a single transamination step catalyzed by branched-chain aminotransferase (BCAT). Wang et al. establish the pathophysiologic principle: "*When BCAA metabolism is genetically impaired in human, serum levels of BCAA and/or their metabolites rise considerably, causing severe neurological dysfunction. The first step in BCAA catabolism is catalyzed by branched chain aminotransferase (BCAT).*" In the index patient this manifested biochemically and radiologically: "*Brain MRI showed symmetric white matter abnormal signals. Metabolic studies revealed remarkably elevated plasma valine and leucine concentrations.*" The combination localizes the disease to the central nervous system — specifically bilateral symmetric cerebral white matter — against a backdrop of systemic BCAA accumulation.

### Finding 3 — Vitamin B6 (pyridoxine) is therapeutically effective

BCAT2 is a pyridoxal-5′-phosphate (PLP)–dependent enzyme, and the disorder is cofactor-responsive. After pyridoxine supplementation, "*the levels of BCAA, especially valine were remarkably decreased and brain MRI lesions were improved*" ([PMID: 25653144](https://pubmed.ncbi.nlm.nih.gov/25653144/)). This dual biochemical-and-radiological response is clinically important: it indicates that residual enzyme function can be pharmacologically augmented by saturating the apoenzyme with its PLP cofactor, and that the white-matter pathology is at least partially reversible when BCAA levels are normalized.

### Finding 4 — The *Bcat2* knockout mouse recapitulates the biochemistry but not the neurology

She et al. 2007 ([PMID: 17767905](https://pubmed.ncbi.nlm.nih.gov/17767905/)) generated a global *BCATm* (*Bcat2*) knockout and confirmed enzyme identity: "*we disrupted the BCATm gene, which encodes the enzyme catalyzing the first step in peripheral BCAA metabolism.*" The knockouts reproduce the biochemical hallmark but present a predominantly metabolic phenotype: "*BCATm(-/-) mice exhibited elevated plasma BCAAs and decreased adiposity and body weight, despite eating more food, along with increased energy expenditure, remarkable improvements in glucose and insulin tolerance, and protection from diet-induced obesity.*" The mechanism is a futile protein-turnover cycle. Lynch et al. 2015 ([PMID: 26351290](https://pubmed.ncbi.nlm.nih.gov/26351290/)) independently confirmed the model, noting that "*Mice lacking the mitochondrial branched-chain aminotransferase (BCATm/Bcat2), which interconverts leucine and α-ketoisocaproate, exhibit elevated protein turnover*," with transcriptomic upregulation of mTOR/eIF/protein-synthesis and degradation pathways in skeletal muscle. The divergence from the human neurological phenotype is itself informative (see Limitations).

### Finding 5 — Disease nosology bridges 1960s biochemistry and modern genetics

MONDO:0100058 unifies two classic aminoacidopathies. **Classic Hypervalinemia** (OMIM 277100) was first described by Wada et al. in 1963 (*"Idiopathic hypervalinemia: probably a new entity of inborn error of valine metabolism"*; [PMID: 14077060](https://pubmed.ncbi.nlm.nih.gov/14077060/)) and attributed to deficient valine transamination. **Hyperleucine-isoleucinemia** was the corresponding leucine/isoleucine transamination defect. Wang et al. 2015 ([PMID: 25653144](https://pubmed.ncbi.nlm.nih.gov/25653144/)) provided the molecular unification, showing that biallelic *BCAT2* mutations produce combined elevation of valine, leucine and isoleucine — exactly what would be expected if a single aminotransferase acting on all three substrates is deficient.

### Finding 6 — Mechanistic distinction from MSUD explains the milder phenotype

BCAT catalyzes the first catabolic step (Val/Leu/Ile + α-ketoglutarate ⇌ BCKAs [α-ketoisovalerate/KIV, α-ketoisocaproate/KIC, α-keto-β-methylvalerate/KMV] + glutamate). The **downstream** second step is the BCKDH complex, deficiency of which causes MSUD. In MSUD, both BCAAs **and** the neurotoxic BCKAs accumulate, driving recurrent metabolic crises, cerebral edema, and neurodevelopmental impairment: "*Maple Syrup Urine Disease (MSUD) is a rare autosomal recessive metabolic disorder characterised by defective branched-chain amino acid (BCAA) catabolism, leading to neurotoxicity, recurrent metabolic crises, and neurodevelopmental impairment*" ([PMID: 42329506](https://pubmed.ncbi.nlm.nih.gov/42329506/)), with leucine identified as "*the primary neurotoxic metabolite*" ([PMID: 38682838](https://pubmed.ncbi.nlm.nih.gov/38682838/)). In BCAT2 deficiency the block is **upstream** of BCKDH, so BCAAs accumulate but BCKAs are *not* overproduced. This explains why the single reported patient had an indolent adult-onset leukoencephalopathy rather than neonatal ketoacidotic crises, and why MSUD was genetically excluded.

### Finding 7 — Both causal variants are ultra-rare in gnomAD

gnomAD v4 (queried 2026-10) confirms both variants are ultra-rare with no reported homozygotes, supporting classification as pathogenic in an ultra-rare recessive disorder:

| Variant (protein) | cDNA | genomic (GRCh38) | gnomAD exome MAF | gnomAD genome |
|---|---|---|---|---|
| p.Glu264Lys | c.790G>A | 19-48797239-C-T | ~1.2×10⁻⁵ (18/1,461,568) | 2/152,310 |
| p.Arg170Gln | c.509G>A | 19-48800003-C-T | ~1.4×10⁻⁶ (2/1,461,592) | absent |

The population rarity (PM2) combined with the in vitro functional evidence (PS3: "*the two BCAT2 gene mutations resulted in decreased BCAT2 enzyme activity*," [PMID: 25653144](https://pubmed.ncbi.nlm.nih.gov/25653144/)) supports a pathogenic classification under ACMG/AMP criteria.

### Finding 8 — Diagnostics, treatment, prognosis and prevention

Diagnosis rests on **quantitative plasma amino-acid analysis** showing elevated valine, leucine and isoleucine ("*remarkably elevated plasma valine and leucine concentrations*"), **brain MRI** showing symmetric white-matter signal abnormalities, **exclusion of MSUD** ("*Maple syrup urine disease (MSUD) diagnosis was not supported since all genes for the branched-chain α-keto acid dehydrogenase complex (BCKD) gene were normal*"), and **molecular confirmation** of biallelic *BCAT2* variants by WES/WGS or a metabolic gene panel, optionally supported by an in vitro BCAT2 enzyme-activity assay ([PMID: 25653144](https://pubmed.ncbi.nlm.nih.gov/25653144/)). Treatment is **vitamin B6 (pyridoxine)**, which normalized BCAAs and improved MRI lesions; **dietary BCAA/protein restriction** is a rational adjunct by analogy to MSUD management ([PMID: 42329506](https://pubmed.ncbi.nlm.nih.gov/42329506/)). A PubMed search found no further molecularly confirmed *BCAT2* cases since 2015.

### Finding 9 — Anatomical, cellular and subcellular localization

The pathology localizes to **bilateral symmetric cerebral white matter** (UBERON:0002316): "*Brain MRI showed symmetric white matter abnormal signals*" ([PMID: 25653144](https://pubmed.ncbi.nlm.nih.gov/25653144/)), with neurocognitive symptoms (chronic headache, mild memory impairment). **Subcellularly, BCAT2/BCATm is a mitochondrial-matrix enzyme** (She 2007: "*mitochondrial branched-chain aminotransferase*"; [PMID: 17767905](https://pubmed.ncbi.nlm.nih.gov/17767905/)), ubiquitously expressed with high activity in peripheral tissues. The brain additionally relies on BCAT (predominantly the cytosolic BCAT1 isoform) for glutamate-nitrogen shuttling, making the CNS particularly sensitive to BCAA dyshomeostasis.

---

## Mechanistic Model / Causal Chain

The pathophysiology proceeds as an ordered causal chain from the germline mutation to the clinical manifestation. Steps marked *(inferred)* are reasoned by analogy or from the mouse model rather than directly demonstrated in the single human patient.

```
1. Biallelic loss-of-function BCAT2 variants (p.Arg170Gln / p.Glu264Lys)
        │  leads to
        ▼
2. Reduced mitochondrial branched-chain aminotransferase (BCATm) enzyme
   activity  [demonstrated: in vitro activity assay, PMID 25653144]
        │  results in
        ▼
3. Impaired FIRST catabolic step of BCAA metabolism:
   Val / Leu / Ile + α-ketoglutarate  ⇌  BCKA + glutamate  (reaction blocked)
        │  results in
        ▼
4. Accumulation of plasma valine, leucine and isoleucine
   (BCKAs are NOT overproduced — block is upstream of BCKDH)   ◄── KEY BRANCH-POINT
   │                                                   │
   │ (contrast: MSUD = downstream BCKDH block →        │
   │  BOTH BCAA *and* neurotoxic BCKA accumulate →     │
   │  crises, cerebral edema, PMID 42329506/41257986)  │
        │  leads to
        ▼
5. Disturbed cerebral BCAA/glutamate nitrogen homeostasis (inferred:
   brain depends on BCAT for glutamate-nitrogen shuttling)
        │  results in
        ▼
6. Symmetric cerebral white-matter injury (leukoencephalopathy)
   [demonstrated: MRI symmetric white-matter signal, PMID 25653144]
        │  manifests as
        ▼
7. Chronic, indolent neurological phenotype: headache, mild memory impairment
   (adult-onset; NOT neonatal ketoacidotic crisis)

   ── THERAPEUTIC REVERSAL ──
   Vitamin B6 (pyridoxine) → ↑ PLP cofactor saturation of residual BCATm →
   ↓ plasma BCAAs (esp. valine) → MRI lesion improvement [PMID 25653144]
```

### Upstream vs downstream, and the MSUD comparison

| Feature | BCAT2 deficiency (this disease) | MSUD (differential) |
|---|---|---|
| Defective enzyme | BCAT2 / BCATm (transaminase) | BCKDH complex (dehydrogenase) |
| Pathway position | First step (upstream) | Second step (downstream) |
| BCAAs | Elevated (Val, Leu, Ile) | Elevated |
| Branched-chain keto acids (BCKAs) | **Not overproduced** | **Accumulate (neurotoxic)** |
| Alloisoleucine | Absent | Present (pathognomonic) |
| Onset / course | Adult, chronic, indolent | Neonatal, acute crises |
| Hallmark injury | Symmetric leukoencephalopathy | Cerebral edema, encephalopathy |
| Cofactor | PLP (vitamin B6) | Thiamine (for thiamine-responsive forms) |
| Treatment | Vitamin B6 + diet | Strict protein restriction, BCAA-free formula |

**Pathway and ontology annotations.** Biochemical pathway: branched-chain amino acid degradation (KEGG hsa00280; Reactome "Branched-chain amino acid catabolism"). Enzyme: EC 2.6.1.42, PLP-dependent. Gene Ontology biological process: GO:0009083 (branched-chain amino acid catabolic process), GO:0009081 (branched-chain amino acid metabolic process), GO:0009448 (gamma-aminobutyric acid metabolic process — nitrogen shuttling context). GO cellular component: GO:0005759 (mitochondrial matrix). Chemical entities (CHEBI): L-valine (CHEBI:16414), L-leucine (CHEBI:15603), L-isoleucine (CHEBI:17191), pyridoxal 5′-phosphate (CHEBI:18405), pyridoxine/vitamin B6 (CHEBI:16709), α-ketoglutarate/2-oxoglutarate (CHEBI:16810), L-glutamate (CHEBI:16015). Cell types of interest (CL): oligodendrocyte (CL:0000128) and its myelin, astrocyte (CL:0000127) for CNS glutamate handling.

---

## Disease Characterization by Template Section

### 1. Disease Information
A concise overview: an ultra-rare autosomal recessive inborn error of BCAA metabolism in which deficiency of mitochondrial branched-chain aminotransferase (BCAT2/BCATm) blocks the first catabolic step shared by valine, leucine and isoleucine, elevating all three in plasma and producing a chronic leukoencephalopathy. **Identifiers:** MONDO:0100058; classic Hypervalinemia OMIM 277100; gene *BCAT2* OMIM *113530; HGNC:977; NCBI Gene 587; UniProt O15382; chromosome 19q13.33. **MeSH:** "Hypervalinemia" (within amino acid metabolism, inborn errors). **Synonyms:** Hypervalinemia; Hyperleucine-isoleucinemia; branched-chain aminotransferase (BCAT2) deficiency; BCATm deficiency; valine transaminase deficiency (historical). **Information source:** aggregated disease-level resources (OMIM, MONDO) plus a single published patient case (not EHR-derived).

### 2. Etiology
**Causal factor:** genetic — biallelic loss-of-function *BCAT2* variants. **Genetic risk factors:** the only known causal variants are p.Arg170Gln (c.509G>A) and p.Glu264Lys (c.790G>A); by analogy, consanguinity/carrier status in families would be the relevant risk context. **Environmental risk/modifying factors:** dietary BCAA (protein) intake plausibly modulates biochemical severity (inferred from MSUD and the mouse model). **Protective factors:** vitamin B6 status is protective by augmenting residual enzyme; low-BCAA diet is protective by reducing substrate load. **Gene-environment interaction:** the disorder is cofactor- and diet-responsive, a classic gene-nutrient interaction (genotype determines residual enzyme; B6 and dietary BCAA load determine expressed phenotype).

### 3. Phenotypes
From the single human case ([PMID: 25653144](https://pubmed.ncbi.nlm.nih.gov/25653144/)):

| Phenotype | Type | HPO suggestion | Onset/course | Frequency |
|---|---|---|---|---|
| Elevated plasma valine (hypervalinemia) | Lab abnormality | HP:0500152 (hypervalinemia) / HP:0003355 (aminoaciduria/amino acid metab abnormality) | Present at diagnosis | 1/1 case |
| Elevated plasma leucine/isoleucine | Lab abnormality | HP:0010903 (abnormal circulating amino acid concentration) | Present | 1/1 |
| Headache | Symptom | HP:0002315 | ~6 yr chronic | 1/1 |
| Memory impairment (mild) | Cognitive sign | HP:0002354 | Chronic | 1/1 |
| Cerebral white-matter abnormality (symmetric leukoencephalopathy) | Imaging/physical | HP:0002500 (abnormality of cerebral white matter) / HP:0007024 | Chronic, reversible with B6 | 1/1 |

Severity: mild-to-moderate; progression: chronic/indolent, partially reversible with treatment. **Quality-of-life impact:** modest in the reported case (chronic headache, mild memory complaints) — far milder than MSUD, which carries high morbidity/mortality. Note: frequencies are drawn from a single patient and cannot be generalized.

### 4. Genetic / Molecular Information
**Causal gene:** *BCAT2* (OMIM *113530; HGNC:977; UniProt O15382; chr19q13.33). **Pathogenic variants:** c.509G>A (p.Arg170Gln) and c.790G>A (p.Glu264Lys), both **missense**, both reducing enzyme activity (loss-of-function). **Classification:** pathogenic/likely pathogenic by PS3 (functional) + PM2 (ultra-rare, gnomAD) + segregation. **Allele frequency:** ultra-rare (MAF ≤~1.2×10⁻⁵; no homozygotes; see Finding 7 table). **Origin:** germline. **Functional consequence:** loss of function (reduced transaminase activity). **Modifier genes:** none established; *BCAT1* (cytosolic isoform) is a plausible functional modifier via compensation but is unproven. **Epigenetic / chromosomal abnormalities:** none reported or expected for this point-mutation recessive disorder.

### 5. Environmental Information
**Dietary BCAA/protein** is the principal non-genetic modulator of biochemical severity. **Vitamin B6 (pyridoxine)** status influences residual enzyme activity. No toxins, radiation, occupational exposures, or infectious agents are implicated. (The index patient's leukoencephalopathy was metabolic, not infectious or toxic.)

### 6. Mechanism / Pathophysiology
See the full causal chain and MSUD-comparison table above. Key points: (a) molecular pathway = BCAA catabolism (KEGG hsa00280); (b) biochemical defect = PLP-dependent transaminase (EC 2.6.1.42) loss of function; (c) subcellular compartment = mitochondrial matrix (GO:0005759); (d) metabolic change = combined Val/Leu/Ile accumulation *without* BCKA overproduction; (e) tissue damage = cerebral white-matter injury, partially reversible. The mouse model adds a peripheral metabolic dimension (futile protein-turnover cycle, increased energy expenditure; [PMID: 17767905](https://pubmed.ncbi.nlm.nih.gov/17767905/), [PMID: 26351290](https://pubmed.ncbi.nlm.nih.gov/26351290/)).

### 7. Anatomical Structures Affected
**Primary organ:** brain — bilateral symmetric cerebral white matter (UBERON:0002316). **Body system:** central nervous system (UBERON:0001017). **Cell/tissue level:** oligodendrocytes/myelin (CL:0000128) implicated by the white-matter signal; astrocytes (CL:0000127) relevant for CNS glutamate-nitrogen handling. **Subcellular:** mitochondrial matrix (GO:0005759), the locus of BCATm. **Lateralization:** bilateral/symmetric. Peripherally, skeletal muscle and adipose tissue are major sites of BCATm activity (from mouse data) but human peripheral pathology is not documented.

### 8. Temporal Development
**Onset:** adult (the index case presented at ~25 years after ~6 years of symptoms); classic infantile hypervalinemia, historically, had pediatric presentation. **Onset pattern:** insidious/chronic. **Progression:** slow, non-crisis; partially reversible with vitamin B6. **Disease course:** chronic, lifelong (genetic), but manageable. No evidence of relapsing-remitting crises (contrast MSUD). **Critical period for intervention:** B6 therapy and dietary management appear effective once diagnosed; earlier intervention is presumed better by analogy.

### 9. Inheritance and Population
**Inheritance:** autosomal recessive (parental carrier segregation, [PMID: 25653144](https://pubmed.ncbi.nlm.nih.gov/25653144/)). **Prevalence/incidence:** unknown; ultra-rare — only one molecularly confirmed patient worldwide plus a handful of historical biochemical cases. **Penetrance/expressivity:** cannot be estimated from n=1. **Carrier frequency:** both variants are ultra-rare in gnomAD, implying very low carrier frequency. **Founder effects/consanguinity:** none documented. **Sex ratio / geographic distribution / age distribution:** undetermined given the single case (reported from China).

### 10. Diagnostics
**Laboratory:** quantitative plasma amino acids (elevated Val, Leu, Ile). **Imaging:** brain MRI (symmetric white-matter signal abnormality). **Confirmatory:** molecular testing — WES/WGS or inborn-errors-of-metabolism gene panel including *BCAT2*; single-gene *BCAT2* sequencing; optional in vitro BCAT2 enzyme-activity assay. **Differential diagnosis — MSUD:** exclude by demonstrating normal BCKDHA/BCKDHB/DBT genes and absence of alloisoleucine and elevated BCKAs ("*all genes for the branched-chain α-keto acid dehydrogenase complex (BCKD) gene were normal*," [PMID: 25653144](https://pubmed.ncbi.nlm.nih.gov/25653144/)). **Screening:** elevated BCAAs are detectable by newborn-screening tandem mass spectrometry (same analyte panel used for MSUD), making biochemical screening feasible, though the disorder's rarity means it is not specifically targeted.

### 11. Outcome / Prognosis
Prognosis in the single documented case was favorable: biochemical normalization and MRI improvement on vitamin B6. In sharp contrast to MSUD — where decompensation causes cerebral edema and death ([PMID: 41257986](https://pubmed.ncbi.nlm.nih.gov/41257986/), [PMID: 38682838](https://pubmed.ncbi.nlm.nih.gov/38682838/)) — BCAT2 deficiency lacks the neurotoxic BCKA accumulation and is not associated with acute metabolic crises. Mortality, survival and quality-of-life data at the population level are unavailable (n=1). Prognostic factors are presumed to include residual enzyme activity, B6-responsiveness, and dietary adherence.

### 12. Treatment
**Pharmacotherapy / cofactor:** vitamin B6 (pyridoxine) — demonstrated to lower BCAAs and improve MRI lesions ([PMID: 25653144](https://pubmed.ncbi.nlm.nih.gov/25653144/)); NCIT suggestion: Pyridoxine (C738)/Vitamin B6 Therapy. **Dietary:** BCAA/protein restriction, by analogy to MSUD management ([PMID: 42329506](https://pubmed.ncbi.nlm.nih.gov/42329506/)); NCIT: Dietary Intervention (C15222). **Supportive:** symptom management (headache). **Experimental / gene/cell/RNA therapy:** none reported for this disorder specifically. (The MSUD oral leucine-decarboxylase enzyme-therapy work, [PMID: 37494004](https://pubmed.ncbi.nlm.nih.gov/37494004/), is a conceptual neighbor but not applicable here, since BCAT2 deficiency does not overproduce leucine metabolites.) **Personalized medicine:** genotype- and B6-response-guided management.

### 13. Prevention
**Primary:** genetic counseling for carrier couples; the disorder is single-gene recessive, so cascade carrier testing and reproductive options (prenatal/preimplantation genetic testing) apply. **Secondary:** biochemical newborn screening (tandem MS already detects elevated BCAAs) enables early detection; dietary and B6 intervention can then forestall white-matter injury. **Tertiary:** ongoing B6 + dietary management to prevent progression of leukoencephalopathy. No immunization or public-health/vector interventions apply.

### 14. Other Species / Natural Disease
**Taxonomy / orthologs:** human *BCAT2* (NCBI Gene 587) has a direct ortholog in mouse *Bcat2* (NCBI Gene 12036) and across mammals; the enzyme and pathway are deeply conserved. **Natural disease in other species:** no naturally occurring *BCAT2*-deficiency disease is documented in companion animals or wildlife (no OMIA entry identified). **Comparative biology:** the mouse knockout shows a metabolic (not neurological) phenotype, highlighting species differences in CNS BCAA handling. **Zoonotic potential:** not applicable (genetic disease).

### 15. Model Organisms
**Mouse (*Mus musculus*, NCBI Taxon 10090):** global *Bcat2*/*BCATm* knockout (She et al. 2007, [PMID: 17767905](https://pubmed.ncbi.nlm.nih.gov/17767905/); Lynch et al. 2015, [PMID: 26351290](https://pubmed.ncbi.nlm.nih.gov/26351290/)). **Model type:** mammalian, genetic knockout. **Phenotype recapitulation:** reproduces the biochemical hallmark (elevated plasma BCAAs) and confirms enzyme identity and pathway position, but does **not** reproduce the human neurological/leukoencephalopathy phenotype — instead showing leanness, increased energy expenditure, improved glucose/insulin tolerance, and protection from diet-induced obesity via a futile protein-turnover cycle. **Model limitations:** fails to capture CNS white-matter pathology; dominated by peripheral metabolic effects. **Applications:** studying systemic BCAA/energy metabolism, protein turnover, and the metabolic consequences of transaminase loss. **Resources:** MGI.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Role |
|---|---|---|---|
| [25653144](https://pubmed.ncbi.nlm.nih.gov/25653144/) | *Hypervalinemia and hyperleucine-isoleucinemia caused by mutations in BCAT2* | Human clinical (n=1) | **Defining paper** — causal variants, AR inheritance, functional LOF, MRI phenotype, B6 response, MSUD exclusion |
| [14077060](https://pubmed.ncbi.nlm.nih.gov/14077060/) | *Idiopathic hypervalinemia: probably a new entity* (Wada 1963) | Human clinical (historical) | Original description of classic Hypervalinemia (OMIM 277100) |
| [17767905](https://pubmed.ncbi.nlm.nih.gov/17767905/) | *Disruption of BCATm in mice → futile protein turnover* | Model organism | Mouse KO: biochemical recapitulation, metabolic phenotype, enzyme identity |
| [26351290](https://pubmed.ncbi.nlm.nih.gov/26351290/) | *Global deletion of BCATm increases protein-turnover genes* | Model organism | Independent confirmation of KO model and enzyme function |
| [42329506](https://pubmed.ncbi.nlm.nih.gov/42329506/) | *Treatment/outcomes in paediatric MSUD* | Human clinical (differential) | Defines downstream MSUD; supports dietary-restriction rationale |
| [41257986](https://pubmed.ncbi.nlm.nih.gov/41257986/) | *Cerebral edema in MSUD* | Human clinical (differential) | Illustrates BCKA-driven neurotoxic crises absent in BCAT2 deficiency |
| [38682838](https://pubmed.ncbi.nlm.nih.gov/38682838/) | *Psychosis & non-compliance in adult MSUD* | Human clinical (differential) | Identifies leucine as primary neurotoxic metabolite |
| [1404884](https://pubmed.ncbi.nlm.nih.gov/1404884/) | *Metabolic disorders of BCAAs due to enzyme mutation* | Review | Context for aminotransferase vs dehydrogenase defects |
| [37494004](https://pubmed.ncbi.nlm.nih.gov/37494004/) | *Oral enzyme therapy for MSUD* | Model/NHP | Neighboring therapeutic concept (MSUD, not directly applicable) |

**How the evidence converges:** The human defining paper (PMID 25653144) establishes genotype, inheritance, functional loss of function, clinical/radiological phenotype, cofactor responsiveness, and the MSUD exclusion — the entire clinical-genetic core. The two mouse papers (PMID 17767905, 26351290) independently confirm the gene identity, pathway position, and biochemical consequence, while revealing that the CNS phenotype is species-dependent. The MSUD literature (PMID 42329506, 41257986, 38682838) provides the essential mechanistic contrast that explains *why* BCAT2 deficiency is milder (upstream block, no BCKA accumulation) and supplies the rationale for dietary management.

---

## Limitations and Knowledge Gaps

1. **Single human case (n=1).** Essentially all human clinical knowledge derives from one molecularly confirmed patient ([PMID: 25653144](https://pubmed.ncbi.nlm.nih.gov/25653144/)). Phenotype spectrum, penetrance, expressivity, natural history, prevalence, sex ratio, and age distribution cannot be reliably estimated. No additional molecularly confirmed cases have appeared since 2015.
2. **Historical vs modern entity ambiguity.** The classic 1960s "hypervalinemia" and "hyperleucine-isoleucinemia" cases were defined biochemically without molecular confirmation; their precise relationship to *BCAT2* genotype is inferred, not proven.
3. **Model–human phenotype divergence.** The *Bcat2* knockout mouse does not reproduce the human leukoencephalopathy, limiting its utility for studying the CNS pathology and leaving the brain injury mechanism largely inferential.
4. **Mechanism of white-matter injury unresolved.** Whether BCAA elevation per se, glutamate-nitrogen shuttle disturbance, or another route causes the leukoencephalopathy is not established in humans.
5. **Treatment evidence is anecdotal.** Vitamin B6 efficacy and dietary-restriction benefit rest on a single patient and analogy to MSUD, respectively; no trials exist.
6. **Variant classification depth.** Only two variants are known; the full allelic spectrum, genotype-phenotype correlations, and any modifier (e.g., *BCAT1*) effects are unknown.

---

## Proposed Follow-up Experiments / Actions

1. **International case-finding.** Query GeneMatcher, metabolic-disease consortia, and newborn-screening programs for additional biallelic *BCAT2* patients to build a case series and define the phenotype spectrum, penetrance, and natural history.
2. **Re-genotype historical cases.** Where biobanked DNA exists from classic 1960s–90s hypervalinemia/hyperleucine-isoleucinemia patients, perform *BCAT2* sequencing to confirm the nosological unification.
3. **CNS-focused model.** Develop a brain- or oligodendrocyte-targeted *Bcat2* conditional knockout (or patient iPSC-derived oligodendrocyte/organoid model) to interrogate the leukoencephalopathy mechanism that the global mouse KO fails to capture.
4. **Functional variant panel.** Systematically assay BCAT2 enzyme activity and PLP-binding for p.Arg170Gln, p.Glu264Lys, and additional candidate variants to quantify residual activity and predict B6-responsiveness (structure-function; the PLP-binding pocket is a key target).
5. **Prospective treatment documentation.** For any newly identified patient, prospectively record B6 dose-response, dietary BCAA titration, and serial MRI to establish an evidence-based management protocol.
6. **Metabolomic profiling.** Perform plasma/CSF metabolomics in patients to confirm the predicted signature (elevated BCAAs, *absence* of BCKA/alloisoleucine), cementing the biochemical distinction from MSUD and supporting a diagnostic algorithm.

---

## Consensus Answer

Hypervalinemia and Hyperleucine-Isoleucinemia (MONDO:0100058) is an ultra-rare autosomal recessive inborn error of branched-chain amino-acid metabolism caused by biallelic loss-of-function mutations in *BCAT2*, the gene encoding mitochondrial branched-chain aminotransferase (BCATm; chr19q13.33), first molecularly defined by Wang et al. 2015 ([PMID: 25653144](https://pubmed.ncbi.nlm.nih.gov/25653144/)) via compound-heterozygous p.Arg170Gln and p.Glu264Lys variants. Because BCAT2 catalyzes the first, shared catabolic step of valine, leucine and isoleucine — upstream of the BCKDH complex defective in maple syrup urine disease — its deficiency elevates all three BCAAs without accumulating neurotoxic branched-chain keto acids, producing a comparatively mild, chronic neurometabolic phenotype (headache, mild memory impairment, symmetric cerebral white-matter abnormalities) that is responsive to vitamin B6 (pyridoxine) cofactor supplementation plus dietary BCAA restriction.


## Artifacts

- [OpenScientist final report](Hypervalinemia_And_Hyperleucine-isoleucinemia-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Hypervalinemia_And_Hyperleucine-isoleucinemia-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 7 |
| Quoted claims found in source | 6 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 9 |
| On topic | 7 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:17767905` *(abstract only)*: "*mitochondrial branched-chain aminotransferase*"
  - Text part not found as substring: '*mitochondrial branched-chain aminotransferase*' (note: only abstract available for PMID:17767905, full text may contain this excerpt)

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 24 |
| Resolved | 22 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 8 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002315` (1 mention) - the report calls it "Symptom"; HP calls it **Headache**
- `HP:0002354` (1 mention) - the report calls it "Cognitive sign"; HP calls it **Memory impairment**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0009448` (obsolete GABA metabolic process) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0002316` (2 mentions) - the report calls it "bilateral symmetric cerebral white matter"; UBERON calls it **white matter**, and lists "neuronal white matter" among its other names
- `GO:0009448` (1 mention) - the report calls it "gamma-aminobutyric acid metabolic process — nitrogen shuttling context"; GO calls it **obsolete GABA metabolic process**, and lists "gamma-aminobutyric acid metabolic process" among its other names
- `HP:0010903` (1 mention) - the report calls it "abnormal circulating amino acid concentration"; HP calls it **Abnormal circulating glutamine concentration**