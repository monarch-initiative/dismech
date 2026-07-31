---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-31T01:49:16.582871'
end_time: '2026-07-31T02:05:37.324681'
duration_seconds: 980.74
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Primary Erythermalgia
  mondo_id: ''
  category: Mendelian
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
citation_count: 26
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Primary_Erythermalgia-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Primary_Erythermalgia-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Primary Erythermalgia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Primary Erythermalgia** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


## Output

# Primary Erythermalgia (Inherited Erythromelalgia): A Comprehensive Disease Characterization

## Summary

**Primary erythermalgia** — more commonly termed **primary (inherited) erythromelalgia (IEM)** — is a rare, autosomal-dominant Mendelian **sodium channelopathy** caused by gain-of-function missense mutations in **SCN9A**, the gene encoding the peripheral voltage-gated sodium channel **Nav1.7**. Nav1.7 is a threshold channel preferentially expressed in nociceptive dorsal root ganglion (DRG) neurons, trigeminal ganglion neurons, and sympathetic ganglion neurons, where it amplifies subthreshold generator potentials. Pathogenic IEM variants shift the voltage dependence of channel activation in the hyperpolarizing (leftward) direction, slow deactivation, and enhance the channel's ramp response to slow depolarizations. The net effect is hyperexcitability of pain-sensing and vasomotor neurons, producing the disease's defining clinical triad: **episodic burning pain, redness (erythema), and warmth of the distal extremities**, precipitated by mild heat/exercise and relieved by cooling.

The disorder typically begins in early childhood (often before age 10 in the inherited form), follows a chronic, lifelong, episodic/paroxysmal course, and although it is not directly fatal, it causes severe pain, disability, and profound quality-of-life impairment. Management rests on **sodium-channel-blocking drugs** (mexiletine, carbamazepine, lidocaine) and neuropathic pain agents (gabapentin, amitriptyline), together with behavioral cooling; treatment responses are variable, often partial, and increasingly recognized to be **genotype-specific**, opening a path toward precision/personalized medicine. A critical clinical distinction is between **primary (SCN9A-driven) erythromelalgia** and **secondary erythromelalgia**, the latter most notably a microvascular manifestation of myeloproliferative neoplasms (essential thrombocythemia, polycythemia vera, often JAK2-mutation-positive), which is platelet-mediated and dramatically aspirin-responsive.

This report synthesizes 10 confirmed findings across 31 reviewed papers to populate a disease knowledge-base entry, spanning disease identity, etiology, phenotypes, genetics, mechanism, anatomy, temporal development, epidemiology/inheritance, diagnostics, prognosis, treatment, prevention, comparative biology, and model organisms. The strongest, most rigorously established conclusions are the SCN9A/Nav1.7 gain-of-function etiology, the biophysical activation-shift mechanism (validated across heterologous systems, human iPSC-derived sensory neurons with CRISPR correction demonstrating causality, and near-atomic bacterial channel structures), and the allelic spectrum linking Nav1.7 to a continuum of pain disorders (IEM, PEPD) and to loss-of-function congenital insensitivity to pain.

---

## Key Findings

### Finding 1 — Primary erythermalgia is caused by gain-of-function mutations in SCN9A (Nav1.7)

The foundational discovery, from linkage and mutation analysis, mapped primary erythermalgia to chromosome 2q (a 7.94 cM interval; LOD 2.11 for markers D2S2370/D2S2330) and identified missense mutations in **SCN9A** (T2573A segregating in a family; T2543C in a sporadic patient). SCN9A encodes the alpha subunit of the voltage-gated sodium channel **Nav1.7**, which is predominantly expressed in sensory (DRG) and sympathetic neurons — an expression pattern that neatly explains the disease's combined nociceptive (burning pain) and vasomotor (erythema, warmth) features. The disease is inherited in an **autosomal-dominant** fashion.

As the original report states: *"Primary erythermalgia is a rare autosomal dominant disease characterised by intermittent burning pain with redness and heat in the extremities"* and *"Our data suggest that mutations in SCN9A cause primary erythermalgia. SCN9A, encoding a voltage-gated sodium channel alpha subunit predominantly expressed in sensory and sympathetic neurones, may play an important role in nociception and vasomotor regulation"* ([PMID: 14985375](https://pubmed.ncbi.nlm.nih.gov/14985375/)).

**Ontology anchors:** Gene **HGNC:10597 (SCN9A)**; protein UniProt Q15858 (Nav1.7); MONDO concept "erythromelalgia / primary erythromelalgia"; OMIM #133020 (Erythermalgia, primary / Erythromelalgia, hereditary).

### Finding 2 — Biophysical mechanism: hyperpolarized activation, slowed deactivation, enhanced ramp response → DRG hyperexcitability

IEM mutations produce a characteristic gain-of-function biophysical signature: they **hyperpolarize (leftward-shift) the voltage dependence of activation**, **slow deactivation**, and **enhance the ramp response** to slow depolarizations. Because Nav1.7 functions as a "threshold channel" in DRG, trigeminal, and sympathetic nociceptors — amplifying small generator potentials toward the action-potential threshold — these changes lower the firing threshold and produce neuronal hyperexcitability.

Crucially, causality has been demonstrated in a human cellular system. Patient induced-pluripotent-stem-cell (iPSC)-derived sensory neurons carrying a Nav1.7 gain-of-function mutation (A1632G) exhibit hyperexcitability; **CRISPR/Cas9 correction of the mutation reduces the hyperexcitability**, and, conversely, **introducing the mutation into control iPSC neurons generates hyperexcitability**. This bidirectional experiment establishes a direct causal link between the mutation and the cellular pain phenotype: *"using CRISPR/Cas9, we corrected this mutation, which reduced the underlying hyperexcitability, providing a path for personalized medicine to treat these disorders, and we introduced the mutation into control induced pluripotent stem cells, which generated hyperexcitability, providing causality"* ([PMID: 40279376](https://pubmed.ncbi.nlm.nih.gov/40279376/)).

The biophysical definition is summarized concisely: IEM *"is characterized clinically by burning pain and redness that is usually focused on the distal extremities, precipitated by mild warmth and relieved by cooling, and is caused by mutations that hyperpolarize activation, slow deactivation, and enhance the channel ramp response"* ([PMID: 22136189](https://pubmed.ncbi.nlm.nih.gov/22136189/)).

**Ontology anchors:** GO:0086010 membrane depolarization during action potential; GO:0001518 voltage-gated sodium channel complex; GO:0019228 neuronal action potential; GO:0035725 sodium ion transmembrane transport.

### Finding 3 — Epidemiology: erythromelalgia incidence ~0.36–1.3 per 100,000/year with female predominance

Population-based data anchor the disease's rarity. In Olmsted County, Minnesota, the overall age/sex-adjusted incidence was **1.3 per 100,000/year** (95% CI 0.8–1.7), split into **primary EM at 1.1** and **secondary EM at 0.2** per 100,000/year, with higher rates in women (2.0/100,000) than men (0.6/100,000): *"The overall age- and sex-adjusted incidence rate ... was 1.3 (0.8-1.7) per 100,000 people per year. The incidence of primary and secondary erythromelalgia was 1.1 (0.7-1.5) and 0.2 (0.02-0.4) per 100,000 people per year, respectively"* ([PMID: 18713229](https://pubmed.ncbi.nlm.nih.gov/18713229/)).

An independent southern Sweden study estimated incidence at **0.36 per 100,000/year**, with 70% female patients and a mean diagnostic delay of 4.5 years: *"Gender and age adjusted incidence of EM for our region was calculated to be 0.36 per 100 000"* ([PMID: 22247059](https://pubmed.ncbi.nlm.nih.gov/22247059/)). The inherited form shows early onset: *"Sex and age distributions among patients with IEM show a predominance of cases with clinical onset before the age of 10 years, whereas sex differences are not pronounced"* ([PMID: 41190974](https://pubmed.ncbi.nlm.nih.gov/41190974/)). Female predominance in overall EM is corroborated by broader dermatologic epidemiology from the same Rochester Epidemiology Project ([PMID: 27009931](https://pubmed.ncbi.nlm.nih.gov/27009931/)).

| Study | Population | Incidence (/100,000/yr) | Female % | Notes |
|---|---|---|---|---|
| Olmsted County, MN ([PMID: 18713229](https://pubmed.ncbi.nlm.nih.gov/18713229/)) | Population-based | 1.3 overall; 1.1 primary; 0.2 secondary | Women 2.0 vs men 0.6 | Age/sex-adjusted |
| Southern Sweden ([PMID: 22247059](https://pubmed.ncbi.nlm.nih.gov/22247059/)) | Single-center regional | 0.36 | 70% | Mean diagnostic delay 4.5 yr |
| China/worldwide review ([PMID: 41190974](https://pubmed.ncbi.nlm.nih.gov/41190974/)) | IEM case review | — | Not pronounced | Onset predominantly <10 yr |

### Finding 4 — Treatment: genotype-specific sodium-channel blockers plus neuropathic agents; cooling relief

Primary EM management centers on **sodium-channel blockers** (mexiletine; intravenous lidocaine infusions) combined with **neuropathic pain agents** (gabapentin, amitriptyline), plus behavioral cooling. Efficacy is variable, partial, and often transient. Importantly, pharmacotherapy response is **variant-specific**: p.L858F/H responds to mexiletine, whereas V400M, S241T, and I234T respond to carbamazepine — evidence for genotype-guided therapy.

Supporting quotes: *"Some patients with specific pathogenic variants respond to pharmacotherapy, such as p.L858F/H (mexiletine) and V400M, S241T, and I234T (carbamazepine), suggesting potential for personalized therapeutic approaches"* ([PMID: 41190974](https://pubmed.ncbi.nlm.nih.gov/41190974/)); *"The treatment of primitive erythermalgia is based on sodium channel blockers such as mexiletine or lidocaine infusions, and on drugs effective on neuropathic pain, such as gabapentin or amitryptiline"* ([PMID: 35835622](https://pubmed.ncbi.nlm.nih.gov/35835622/)). A single-center cohort found *"The most effective therapies were antihistamines, venlafaxine, and mexiletine"* ([PMID: 37557164](https://pubmed.ncbi.nlm.nih.gov/37557164/)).

A cautionary safety note: mexiletine has a narrow therapeutic index; overdose can be life-threatening with cardiovascular and CNS toxicity ([PMID: 37661688](https://pubmed.ncbi.nlm.nih.gov/37661688/)).

**MAXO/ontology anchors:** MAXO:0000058 pharmacotherapy; "sodium channel blocker therapy"; CHEBI:6916 mexiletine; CHEBI:3387 carbamazepine; CHEBI:6456 lidocaine; CHEBI:42797 gabapentin; CHEBI:2666 amitriptyline; behavioral application of cold.

### Finding 5 — SCN9A allelic spectrum: IEM vs PEPD vs CIP

Nav1.7 sits at the center of a spectrum of Mendelian pain disorders. **Gain-of-function** missense mutations cause **primary erythromelalgia (IEM)** and **paroxysmal extreme pain disorder (PEPD)**, whereas **nonsense/loss-of-function** mutations cause **channelopathy-associated congenital insensitivity to pain (CIP)**. A genotype–phenotype rule generally holds: **IEM mutations enhance activation** (hyperpolarizing shift), while **PEPD mutations impair steady-state fast inactivation** (depolarizing shift, increased persistent/resurgent current).

*"Gain-of-function missense mutations in Na(v)1.7 have been shown to cause primary erythermalgia and paroxysmal extreme pain disorder, while nonsense mutations in Na(v)1.7 result in loss of Na(v)1.7 function and a condition known as channelopathy-associated insensitivity to pain"* ([PMID: 18060017](https://pubmed.ncbi.nlm.nih.gov/18060017/)); *"Gain-of-function mutations are typically pain-causing and have been associated with inherited erythromelalgia (IEM) and paroxysmal extreme pain disorder (PEPD). IEM is usually caused by enhanced NaV1.7 channel activation, whereas mutations that alter steady-state fast inactivation often lead to PEPD"* ([PMID: 25995458](https://pubmed.ncbi.nlm.nih.gov/25995458/)).

The correlation is imperfect: **A1632E** is an "overlap" mutation showing both IEM and PEPD features (a continuum), and **A1632T** causes IEM but does so via a fast-inactivation shift rather than the classic activation shift ([PMID: 24311784](https://pubmed.ncbi.nlm.nih.gov/24311784/)). Resurgent/persistent current biophysics further refine the IEM-vs-PEPD distinction ([PMID: 27174182](https://pubmed.ncbi.nlm.nih.gov/27174182/)).

| Disorder | Nav1.7 mutation class | Biophysical signature | Clinical picture |
|---|---|---|---|
| **IEM** (primary erythromelalgia) | Gain-of-function missense | Hyperpolarized activation, slow deactivation, enhanced ramp | Distal-extremity burning pain, erythema, warmth; heat-triggered |
| **PEPD** | Gain-of-function missense | Impaired fast inactivation; ↑ persistent/resurgent current | Proximal (rectal, ocular, jaw) paroxysmal pain |
| **CIP** | Nonsense / loss-of-function | Loss of channel function | Congenital insensitivity to pain, anosmia |

### Finding 6 — Differential diagnosis: primary (SCN9A) vs secondary erythromelalgia (myeloproliferative neoplasms, JAK2)

**Secondary erythromelalgia** is a recognized microvascular manifestation of **myeloproliferative neoplasms (MPNs)** — essential thrombocythemia (ET) and polycythemia vera (PV) — mediated by **platelet-mediated occlusive thrombosis in the end-arterial circulation**. Unlike primary EM, it responds dramatically to **aspirin** (cyclooxygenase-1 inhibition). Consequently, the workup of suspected erythromelalgia must include a complete blood count and **JAK2 mutation testing** to exclude an underlying MPN.

*"Microvascular disturbances in essential thrombocythemia (ET) and polycythemia vera (PV), including erythromelalgia, and atypical and typical transient cerebral, ocular, and coronary ischemic attacks, are caused by platelet-mediated transient and occlusive thrombosis in the end-arterial circulation"* and *"Inhibition of platelet cyclooxygenase-1 by aspirin is followed by relief of microvascular disturbances"* ([PMID: 16673274](https://pubmed.ncbi.nlm.nih.gov/16673274/)). Contemporary guidance for thrombocytosis workup recommends that *"testing for Janus kinase 2 gene sequence variations should be performed"* ([PMID: 42101597](https://pubmed.ncbi.nlm.nih.gov/42101597/)).

A further differential is **acute monophasic pediatric erythromelalgia**, which can represent post-infectious immune-mediated small-fiber neuropathy rather than inherited channelopathy — distinguished by monophasic course, autoimmune/infectious associations, skin-biopsy small-fiber loss, and response to immunotherapy ([PMID: 32723684](https://pubmed.ncbi.nlm.nih.gov/32723684/)).

### Finding 7 — Model systems: iPSC sensory neurons robustly model IEM; rodent knock-ins recapitulate DRG hyperexcitability but often lack overt pain

Human **iPSC-derived sensory neurons** carrying Nav1.7 gain-of-function mutations (e.g., A1632G, Q875E) reproduce hyperexcitability and are described as *"a robust, scalable and relevant model to study the effects of gain-of-function mutations in ion channels in pain-related disorders"* ([PMID: 40279376](https://pubmed.ncbi.nlm.nih.gov/40279376/)). The Q875E iPSC line has been used for pharmacology (e.g., botulinum toxin studies) ([PMID: 38657946](https://pubmed.ncbi.nlm.nih.gov/38657946/)).

By contrast, **rodent knock-in models incompletely recapitulate the human pain phenotype**. Two independent Nav1.7 **I228M** knock-in mouse lines showed DRG neuron hyperexcitability yet **did not** display mechanical/thermal hyperalgesia or intraepidermal nerve fiber loss: *"Nav1.7 I228M mice do not display mechanical or thermal hyperalgesia or intraepidermal nerve fiber loss in vivo. Therefore, although these 2 Nav1.7 I228M knock-in mouse lines recapitulate the DRG neuron hyperexcitability associated with gain-of-function mutations in Nav1.7, they do not recapitulate the pain or neuropathy phenotypes seen in patients"* ([PMID: 33323889](https://pubmed.ncbi.nlm.nih.gov/33323889/)). A rat Nav1.7 knock-in model was generated for drug development ([PMID: 31550995](https://pubmed.ncbi.nlm.nih.gov/31550995/)), and complementary optogenetic (NaV1.7-ChR2) and heterologous (HEK293, Xenopus oocyte) systems support mechanistic and pharmacological studies ([PMID: 36201719](https://pubmed.ncbi.nlm.nih.gov/36201719/)).

| Model | Type | Recapitulation | Key limitation |
|---|---|---|---|
| Patient iPSC sensory neurons | In vitro, human | Hyperexcitability; CRISPR-correctable | No in-vivo behavior |
| Nav1.7 I228M knock-in mice (×2 lines) | Mammalian, in vivo | DRG hyperexcitability | No hyperalgesia/IENF loss |
| Rat Nav1.7 knock-in | Mammalian, in vivo | Drug-development platform | Genotype-specific |
| HEK293 / Xenopus oocytes | Heterologous | Per-variant biophysics | No neuronal context |

### Finding 8 — Structural basis: IEM voltage-sensor mutations facilitate outward S4 gating-charge movement

Near-atomic structural work using the bacterial channel **NaVAb** engineered with four IEM voltage-sensor mutations recapitulated the hyperpolarizing activation shift seen in human Nav1.7. An **S1-segment mutation widens the pathway for gating-charge translocation**, while **S4-segment mutations modify hydrophobic interactions** with neighboring side chains or membrane phospholipids — both facilitating **outward S4 gating-charge movement**, causing channel hyperactivation, neuronal hyperexcitability, and severe pain.

*"a mutation in the S1 segment of the voltage sensor facilitated the outward movement of S4 gating charges by widening the pathway for gating charge translocation. In contrast, mutations in the S4 segments modified hydrophobic interactions with surrounding amino acid side chains or membrane phospholipids that would enhance the outward movement of the gating charges"* ([PMID: 37903281](https://pubmed.ncbi.nlm.nih.gov/37903281/)). This provides a physical, mutation-specific basis for structure-guided therapeutic design.

### Finding 9 — Prognosis/burden: chronic, lifelong, episodic, severely disabling, but not directly fatal

Primary EM greatly compromises quality of life and causes severe disability, with an episodic/paroxysmal course of burning pain, erythema, and warmth: *"The symptoms greatly compromise the patients' quality of life leading to severe disability"* ([PMID: 37557164](https://pubmed.ncbi.nlm.nih.gov/37557164/)). It is generally **not directly fatal** — the Swedish cohort reported *"there was no mortality directed related to EM"* ([PMID: 22247059](https://pubmed.ncbi.nlm.nih.gov/22247059/)). Burden data from painful small-fiber/idiopathic neuropathy — the broader category encompassing EM pain — quantify substantial comorbidity: sleep disturbance/insomnia 37%, anxiety 34%, depressive symptoms 33%, plus work impairment (~37%) and significant direct/indirect costs: *"Most common comorbidities were sleep disturbance/insomnia (37.0%), anxiety (34.0%), and depressive symptoms (33.0%)"* ([PMID: 24673364](https://pubmed.ncbi.nlm.nih.gov/24673364/)). A 2025 systematic review evaluated comparative treatment efficacy/tolerability, reflecting the absence of a single uniformly effective therapy ([PMID: 40428878](https://pubmed.ncbi.nlm.nih.gov/40428878/)). Notably, some patients resort to extreme cooling/ice immersion, causing skin maceration and secondary complications — a self-inflicted morbidity risk.

### Finding 10 — Variant spectrum and molecular diagnosis: recurrent heterozygous germline SCN9A missense alleles, ultra-rare in population databases

Primary erythermalgia arises from **heterozygous germline missense variants** in SCN9A/Nav1.7. Recurrent/illustrative pathogenic alleles across families and cohorts include **I848T, L858F/H, F1449V, V400M, S241T, I234T, Q875E, I136V, P1308L,** and **A1632G/T/E**, plus novel alleles such as **L1595R (c.4784T>G)** and **F1624S**. Pathogenic alleles are typically **absent from population databases** (e.g., gnomAD) and cosegregate within families, fulfilling ACMG/AMP criteria for pathogenicity: *"The variant was absent from population databases and co-segregated with the phenotype within the family, fulfilling ACMG/AMP criteria for likely pathogenicity"* ([PMID: 41997215](https://pubmed.ncbi.nlm.nih.gov/41997215/)).

Molecular confirmation uses **single-gene SCN9A sequencing** or **hereditary sensory/autonomic neuropathy gene panels**: *"We conducted a gene-panel sequencing targeting 18 genes associated with hereditary sensory and/or autonomic neuropathy"* ([PMID: 37555797](https://pubmed.ncbi.nlm.nih.gov/37555797/)); *"We describe a spectrum of SCN9A variants associated with IEM"* ([PMID: 41190974](https://pubmed.ncbi.nlm.nih.gov/41190974/)). Chromosomal microarray, karyotyping, FISH, mtDNA testing, and repeat-expansion testing are **not indicated** — this is a single-gene point-mutation disorder.

---

## Mechanistic Model / Interpretation

The pathophysiology of primary erythermalgia forms a clean, well-supported causal chain from a single germline point mutation to episodic clinical symptoms:

```
  Germline heterozygous                Biophysical gain-of-function
  SCN9A missense variant   ──────►     • Hyperpolarized (leftward) activation
  (e.g., I848T, L858F,                 • Slowed deactivation
   V400M, A1632G)                      • Enhanced ramp/persistent current
          │                                        │
          ▼                                        ▼
  Structural change in Nav1.7          Nav1.7 = "threshold channel"
  voltage sensor (S1/S4):              amplifies subthreshold generator
  facilitated OUTWARD S4               potentials in DRG / trigeminal /
  gating-charge movement               sympathetic neurons
          │                                        │
          └───────────────┬────────────────────────┘
                          ▼
        DRG NOCICEPTOR + SYMPATHETIC NEURON HYPEREXCITABILITY
        (spontaneous firing, lowered threshold)
                          │
        ┌─────────────────┴───────────────────┐
        ▼                                      ▼
  Nociceptive output                    Vasomotor dysregulation
  → BURNING PAIN                        → ERYTHEMA + WARMTH
        │                                      │
        └──────────────┬───────────────────────┘
                       ▼
        HEAT-TRIGGERED, COOLING-RELIEVED
        EPISODIC ATTACKS IN DISTAL EXTREMITIES
                       │
        (temperature-dependent because warmth further
         shifts channels toward the hyperactivable state)
```

**Upstream vs downstream:** The upstream trigger is the germline SCN9A variant and its structural effect on the voltage sensor (outward S4 gating-charge facilitation, PMID 37903281). The proximate downstream mechanism is altered channel gating (PMID 22136189), which drives sensory/sympathetic neuronal hyperexcitability (causally proven by CRISPR correction in iPSC neurons, PMID 40279376). The most downstream events are the clinical manifestations — burning pain (nociceptive) and erythema/warmth (vasomotor), both explicable by Nav1.7's dual expression in sensory and sympathetic neurons (PMID 14985375).

**Cell types and biological processes (ontology anchors):**
- **CL:0000101** sensory neuron; dorsal root ganglion neuron; **CL:0000198** nociceptor; sympathetic (postganglionic) neuron.
- **GO:0019228** neuronal action potential; **GO:0086010** membrane depolarization during action potential; **GO:0035725** sodium ion transmembrane transport; **GO:0001518** voltage-gated sodium channel complex.

**Anatomical involvement (Section 7):** Primary organ = **skin of the distal extremities** (UBERON:0002097 skin of body; UBERON:0002387 pes/foot; UBERON:0002398 manus/hand), typically **bilateral and symmetric**, with feet more affected than hands. Body systems: **peripheral nervous system** (UBERON:0000010) — specifically DRG (UBERON:0000044) and sympathetic ganglia — and the **cutaneous microvasculature/integumentary system**. Subcellular locus = the neuronal plasma membrane voltage-gated sodium channel (GO:0001518).

**Temporal development (Section 8):** Onset is usually **pediatric/childhood** (often <10 years) in the inherited form, insidious in onset, with a **chronic, lifelong, episodic (paroxysmal)** course punctuated by heat- and exercise-triggered flares and relieved by cooling. There is no established genetic anticipation, and the disorder is not self-limited (contrasting with the acute monophasic post-infectious pediatric form).

**Inheritance and population (Section 9):** **Autosomal dominant**, single-gene (SCN9A), with recurrent private missense alleles that are ultra-rare/absent in gnomAD and cosegregate in families. Both familial and de novo/sporadic cases occur. Penetrance is high but expressivity is variable, including striking intra- and interfamily phenotypic diversity for the same variant (PMID 22136189). Female predominance is seen in overall EM epidemiology, though sex differences are less pronounced in the inherited subtype.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Supports |
|---|---|---|---|
| [14985375](https://pubmed.ncbi.nlm.nih.gov/14985375/) | Mutations in SCN9A cause primary erythermalgia | Human genetic (linkage/mutation) | F1: causal gene, AD inheritance, Nav1.7 expression |
| [22136189](https://pubmed.ncbi.nlm.nih.gov/22136189/) | Phenotypic diversity of a Nav1.7 GoF variant | Human clinical + biophysics | F2: IEM biophysical signature; variable expressivity |
| [40279376](https://pubmed.ncbi.nlm.nih.gov/40279376/) | CRISPR correction in iPSC sensory neurons | In vitro human iPSC | F2, F7: causality; iPSC model validation |
| [18713229](https://pubmed.ncbi.nlm.nih.gov/18713229/) | Incidence in Olmsted County | Population epidemiology | F3: incidence, primary vs secondary |
| [22247059](https://pubmed.ncbi.nlm.nih.gov/22247059/) | EM in Sweden | Population/single-center | F3, F9: incidence, female %, no EM mortality |
| [41190974](https://pubmed.ncbi.nlm.nih.gov/41190974/) | IEM review (China/worldwide) | Review | F3, F4, F10: onset <10 yr; genotype-specific therapy; variant spectrum |
| [35835622](https://pubmed.ncbi.nlm.nih.gov/35835622/) | Paroxysmal vascular acrosyndromes | Clinical review | F4: first-line drug classes |
| [37557164](https://pubmed.ncbi.nlm.nih.gov/37557164/) | Single-center primary EM experience | Clinical cohort | F4, F9: effective therapies; QoL/disability |
| [37661688](https://pubmed.ncbi.nlm.nih.gov/37661688/) | Mexiletine overdose | Clinical case | F4: treatment safety/narrow index |
| [18060017](https://pubmed.ncbi.nlm.nih.gov/18060017/) | SCN9A spectrum of pain disorders | Review | F5: IEM/PEPD/CIP allelic spectrum |
| [25995458](https://pubmed.ncbi.nlm.nih.gov/25995458/) | Novel SCN9A mutations, phenotype correlations | Human + electrophysiology | F5: IEM vs PEPD biophysical rule |
| [24311784](https://pubmed.ncbi.nlm.nih.gov/24311784/) | A1632T causes IEM via fast-inactivation shift | In vitro electrophysiology | F5: imperfect genotype-phenotype correlation |
| [27174182](https://pubmed.ncbi.nlm.nih.gov/27174182/) | Slow inactivation & open-channel block | In vitro biophysics | F5: resurgent/persistent current distinctions |
| [16673274](https://pubmed.ncbi.nlm.nih.gov/16673274/) | Platelet-mediated thrombosis in ET/PV | Clinical/mechanistic | F6: secondary EM mechanism, aspirin response |
| [42101597](https://pubmed.ncbi.nlm.nih.gov/42101597/) | Thrombocytosis evidence review | Clinical guideline | F6: JAK2 testing |
| [32723684](https://pubmed.ncbi.nlm.nih.gov/32723684/) | Pediatric acute monophasic EM = SFN | Clinical case series | F6: immune-mediated differential |
| [33323889](https://pubmed.ncbi.nlm.nih.gov/33323889/) | Two Nav1.7 I228M knock-in mouse lines | Mouse model | F7: incomplete pain-phenotype recapitulation |
| [31550995](https://pubmed.ncbi.nlm.nih.gov/31550995/) | Rat Nav1.7 knock-in | Rat model | F7: drug-development platform |
| [36201719](https://pubmed.ncbi.nlm.nih.gov/36201719/) | NaV1.7-ChR2 optogenetic mice | Mouse model | F7: nociceptor activation tool |
| [38657946](https://pubmed.ncbi.nlm.nih.gov/38657946/) | BoNT/A in Q875E iPSC neurons | In vitro human iPSC | F7: iPSC pharmacology model |
| [37903281](https://pubmed.ncbi.nlm.nih.gov/37903281/) | Structural basis (NaVAb) of IEM voltage-sensor mutations | Structural biology | F8: S4 gating-charge mechanism |
| [24673364](https://pubmed.ncbi.nlm.nih.gov/24673364/) | Burden of painful small-fiber neuropathy | Survey/chart review | F9: comorbidity/cost burden |
| [40428878](https://pubmed.ncbi.nlm.nih.gov/40428878/) | Comparative treatment efficacy (systematic review) | Systematic review | F9: no single uniformly effective therapy |
| [41997215](https://pubmed.ncbi.nlm.nih.gov/41997215/) | Germline SCN9A variant, unilateral erythema | Human clinical/genetic | F10: ultra-rare, cosegregating, ACMG classification |
| [37555797](https://pubmed.ncbi.nlm.nih.gov/37555797/) | Gene-panel study of SCN9A pain disorders | Human genetic | F10: gene-panel diagnostic approach |
| [27009931](https://pubmed.ncbi.nlm.nih.gov/27009931/) | Sex differences in skin diseases (REP) | Epidemiology | F3: female predominance in EM |

**Consistency and conflicts.** The genetic etiology (SCN9A/Nav1.7 gain-of-function) is corroborated by convergent evidence types — human linkage/mutation studies, in-vitro electrophysiology, human iPSC causality experiments, and channel structural biology — with no contradicting evidence in the reviewed literature. The main internal tension is genotype–phenotype: while IEM generally maps to activation-enhancing mutations and PEPD to inactivation-impairing mutations (PMID 25995458), overlap variants (A1632E) and exceptions (A1632T causing IEM via an inactivation shift, PMID 24311784) show the rule is a useful heuristic rather than an absolute law. The second key tension is model fidelity: iPSC neurons faithfully model human hyperexcitability, but mouse knock-ins reproduce cellular hyperexcitability without overt pain behavior (PMID 33323889), a species/context gap important for preclinical drug development.

---

## Section-by-Section Knowledge-Base Annotations

**1. Disease information.** Rare AD Mendelian sodium channelopathy; synonyms: primary/inherited/familial erythromelalgia, IEM, primary erythermalgia, Mitchell disease (historical, for EM broadly), "man on fire" syndrome. Identifiers: **OMIM #133020**; **Orphanet ORPHA:90026 (primary erythromelalgia)**; MeSH "Erythromelalgia"; ICD-10 I73.81; MONDO erythromelalgia concept. Information is derived from aggregated disease-level resources and published case/family cohorts (not primarily EHR).

**2. Etiology.** Primary cause = heterozygous germline gain-of-function SCN9A missense variants (F1, F5, F10). Genetic risk = the causal variant itself (dominant); no established environmental risk factors cause the disease, though **heat, exercise, and warm environments** are potent symptom **triggers**. No robust protective genetic/environmental factors identified; **cooling** is the principal symptom-relieving intervention. Gene–environment interaction is temperature-dependent channel gating: warmth further biases already-hyperactivable channels toward opening.

**3. Phenotypes (HPO).** Core: burning extremity pain (**HP:0012531 Pain**), **erythema** (**HP:0500252 Erythema**), local **skin warmth/increased temperature**, **episodic/paroxysmal** course, heat-triggered, cooling-relieved, distal and typically **bilateral**. Onset childhood (**HP:0011463 Childhood onset**). Severity moderate–severe, variable; progression episodic/fluctuating. QoL impact severe (F9).

**4. Genetic/molecular.** Causal gene **SCN9A (HGNC:10597; OMIM *603415)**, protein Nav1.7 (UniProt Q15858). Variant class: missense, heterozygous, germline, gain-of-function (F1, F5, F10). Illustrative alleles: I848T, L858F/H, F1449V, V400M, S241T, I234T, Q875E, I136V, P1308L, A1632G/T/E, L1595R, F1624S. Allele frequency: absent/ultra-rare in gnomAD; ACMG-classified pathogenic/likely pathogenic via cosegregation and functional data. No causal chromosomal abnormalities or established epigenetic drivers.

**5. Environmental.** No toxic/infectious cause of the primary form; heat/warmth and physical activity are triggers; a distinct **acute post-infectious/immune-mediated pediatric erythromelalgia** exists as a phenocopy (PMID 32723684).

**6. Mechanism.** See Mechanistic Model above (F2, F5, F8). Molecular pathway = voltage-gated sodium channel gating / neuronal excitability; cellular process = altered action-potential threshold and firing; protein dysfunction = gain-of-function voltage-sensor defect. No primary immune/metabolic/fibrotic mechanism.

**7. Anatomy.** Skin of distal extremities (feet > hands), bilateral/symmetric; peripheral sensory (DRG) and sympathetic neurons; cutaneous microvasculature. UBERON/CL/GO anchors listed above.

**8. Temporal.** Childhood onset, insidious, chronic lifelong, episodic/paroxysmal; heat-triggered flares; cooling-induced transient remission.

**9. Inheritance/epidemiology.** AD; incidence ~0.36–1.3/100,000/yr (F3); high penetrance, variable expressivity; female predominance overall.

**10. Diagnostics.** Clinical triad + provocation/relief pattern; CBC and **JAK2 testing** to exclude secondary MPN-associated EM (F6); molecular confirmation by **SCN9A single-gene sequencing** or **HSAN gene panel** (F10). Skin biopsy for small-fiber neuropathy in atypical/acquired presentations. CMA/karyotype/FISH/mtDNA/repeat-expansion testing NOT indicated.

**11. Prognosis.** Chronic, disabling, non-fatal (F9); high psychiatric/functional comorbidity; risk of self-inflicted cooling injury.

**12. Treatment (MAXO).** Sodium-channel blockers (mexiletine, carbamazepine, lidocaine), neuropathic agents (gabapentin, amitriptyline), antihistamines, venlafaxine; behavioral cooling; genotype-guided selection (F4). Emerging: selective Nav1.7 blockers, structure-guided and gene/CRISPR-based precision approaches.

**13. Prevention.** No primary prevention (Mendelian). Genetic counseling for AD 50% recurrence risk; cascade family testing; prenatal/preimplantation options where applicable. Tertiary prevention = trigger avoidance (heat, exertion) and avoidance of cooling-related skin damage.

**14. Other species / natural disease.** Human disease (NCBI Taxon 9606). Ortholog **Scn9a** in mouse (NCBI Gene 20274) and rat; no well-documented naturally occurring companion-animal/wildlife equivalent identified; engineered rodent orthologs used experimentally (F7).

**15. Model organisms.** Human iPSC-derived sensory neurons (preferred, robust; F7); mouse and rat Nav1.7 knock-in lines (cellular hyperexcitability, incomplete pain behavior); optogenetic NaV1.7-ChR2 mice; HEK293/Xenopus oocyte heterologous systems; bacterial NaVAb for structural studies. Resources: MGI, RGD, Cellosaurus/iPSC repositories.

---

## Limitations and Knowledge Gaps

1. **Model fidelity gap.** Mouse Nav1.7 I228M knock-ins recapitulate DRG hyperexcitability but not pain behavior or nerve-fiber loss (PMID 33323889), limiting preclinical predictive validity; iPSC neurons capture excitability but lack in-vivo behavioral read-outs.
2. **Imperfect genotype–phenotype mapping.** The IEM (activation shift) vs PEPD (inactivation shift) dichotomy has documented exceptions and overlap variants (A1632E/T), complicating variant interpretation and prognostication.
3. **Sparse population genetics.** Because pathogenic alleles are private/ultra-rare, formal penetrance estimates, carrier frequencies, and founder effects are not well quantified from population databases.
4. **Epidemiology heterogeneity.** Incidence estimates (0.36 vs 1.3/100,000/yr) mix primary and secondary EM and different ascertainment methods; primary-EM-specific, molecularly confirmed incidence/prevalence is uncertain.
5. **Treatment evidence quality.** Most therapeutic data are from small single-center cohorts and case reports; the 2025 systematic review (PMID 40428878) underscores the lack of a uniformly effective, high-evidence therapy. Genotype-specific responses are promising but not yet validated in prospective randomized trials.
6. **No omics depth.** Transcriptomic/proteomic/metabolomic profiling of patient tissue is limited; QoL is documented qualitatively and via proxy small-fiber-neuropathy burden data rather than EM-specific validated instruments.
7. **Comparative/veterinary biology** for a naturally occurring animal counterpart is essentially absent.

---

## Proposed Follow-up Experiments / Actions

1. **Prospective, genotype-stratified pharmacology trial.** Test the mexiletine-responsive (L858F/H) vs carbamazepine-responsive (V400M, S241T, I234T) hypothesis in a controlled, biophysically phenotyped patient cohort to validate genotype-guided prescribing (extends F4/F5).
2. **iPSC pharmacology panel.** Build an isogenic, CRISPR-engineered iPSC-sensory-neuron library spanning the recurrent allelic spectrum (F10) and screen selective Nav1.7 blockers and existing sodium-channel drugs against multielectrode-array excitability to prioritize variant-specific therapies (extends F7).
3. **Structure-guided drug design.** Leverage the NaVAb/Nav1.7 voltage-sensor structures (F8) to design mutation-specific state-dependent inhibitors that preferentially stabilize the resting (deactivated) voltage sensor.
4. **Improved in-vivo model.** Develop humanized-SCN9A or higher-impact knock-in/conditional models that reproduce pain behavior and intraepidermal nerve-fiber changes, closing the mouse-model gap (addresses F7 limitation).
5. **Molecularly confirmed natural-history registry.** Establish a genotyped primary-EM registry to quantify penetrance, expressivity, incidence/prevalence, progression, and EM-specific QoL with validated instruments (addresses epidemiology and prognosis gaps).
6. **Diagnostic standardization.** Formalize a diagnostic flow-chart combining clinical triad + CBC/JAK2 exclusion of secondary EM + SCN9A/HSAN panel confirmation + skin biopsy for atypical acquired cases (operationalizes F6/F10).

---

*Evidence source types are indicated throughout: human clinical/genetic (e.g., PMIDs 14985375, 22136189, 25995458, 41190974, 41997215, 37555797), in-vitro human iPSC (40279376, 38657946), heterologous/electrophysiology (24311784, 27174182), model organism (33323889, 31550995, 36201719), structural/computational (37903281), and epidemiologic/clinical-review (18713229, 22247059, 16673274, 42101597, 24673364, 40428878, 35835622, 37557164, 27009931).*


## Artifacts

- [OpenScientist final report](Primary_Erythermalgia-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Primary_Erythermalgia-deep-research-openscientist_artifacts/final_report.pdf)