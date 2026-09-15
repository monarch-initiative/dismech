---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-23T19:04:30.494131+00:00'
end_time: '2026-08-23T19:24:35.168699+00:00'
duration_seconds: 1204.67
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Epilepsy
  mondo_id: ''
  category: Complex
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    model: null
    system_prompt: null
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
run_metadata:
  openscientist_job_id: bdf24227-454c-4702-ab34-6d86082a31c9
citation_count: 55
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Epilepsy-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Epilepsy-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Epilepsy
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Epilepsy** covering all of the
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

# Epilepsy: A Comprehensive Disease Characterization

*Autonomous discovery report — 15 confirmed findings, 62 papers reviewed across 5 iterations*

**Disease:** Epilepsy | **Category:** Complex (multifactorial, genetically heterogeneous) | **Suggested MONDO:** MONDO:0005027

---

## Summary

**Epilepsy is a common, chronic, and etiologically heterogeneous brain disorder affecting roughly 50–70 million people worldwide, defined by an enduring predisposition to recurrent unprovoked seizures arising from abnormal, hypersynchronous neuronal discharge** ([PMID: 41306289](https://pubmed.ncbi.nlm.nih.gov/41306289/)). Despite dozens of distinct etiologies—monogenic channelopathies, polygenic susceptibility, structural brain lesions, perinatal injury, stroke, traumatic brain injury (TBI), CNS infection, autoimmune processes, and metabolic disease—the disorder converges mechanistically on a single core theme: **a shift in the excitation/inhibition (E/I) balance toward excitation**. This shift is driven by ion-channel and neurotransmitter-receptor dysfunction, loss or silencing of GABAergic inhibitory interneurons, microglial pruning of inhibitory synapses, neuroinflammation, blood–brain-barrier (BBB) disruption, and maladaptive epigenetic and circuit reorganization.

Epilepsy's genetic architecture is predominantly **polygenic** (overall heritability ≈ 32%; 26 genome-wide-significant loci converging on synaptic genes in excitatory and inhibitory neurons), with important **monogenic subsets**—most notably *SCN1A* loss-of-function variants that cause > 95% of Dravet syndrome and span a phenotypic continuum from mild febrile seizures (GEFS+) to severe developmental and epileptic encephalopathy. Clinically, **antiseizure medications (ASMs) control seizures in ~70–80% of patients, while ~30% have drug-resistant epilepsy** requiring surgery, neuromodulation, dietary therapy, or emerging precision/gene therapies. Sudden unexpected death in epilepsy (**SUDEP**) is the leading cause of premature mortality in refractory disease (8–17% of epilepsy-related deaths).

A crucial public-health message emerges from this work: **a large fraction of the global epilepsy burden is preventable.** The four leading modifiable etiologic categories—perinatal insults, TBI, CNS infection (notably neurocysticercosis), and stroke—are addressable through obstetric care, injury prevention, sanitation/vaccination, and vascular risk control. Global incidence and prevalence are rising (driven disproportionately by acquired/secondary epilepsy), even as age-standardized DALYs and mortality decline—an epidemiologic transition with major implications for low- and middle-income countries (LMICs). Cutting-edge epigenetic, single-cell, and spatial-transcriptomic studies are now resolving epileptogenesis at cellular and molecular resolution, identifying "epilepsy-associated microglia," complement activation, and an epigenetic "cellular memory" that together offer new biomarkers and therapeutic targets.

---

## Disease Information (Section 1)

Epilepsy is a **chronic neurological disorder** characterized by an enduring predisposition to recurrent, unprovoked seizures resulting from abnormal, excessive, and hypersynchronous neuronal discharges. It is not a single disease but a family of syndromes classified by seizure type (focal, generalized, combined, unknown) and etiology (genetic, structural, metabolic, immune, infectious, unknown), per the International League Against Epilepsy (ILAE) framework.

**Key identifiers (aggregated disease-level resources):**

| Resource | Identifier(s) |
|---|---|
| MONDO | MONDO:0005027 (epilepsy) |
| MeSH | D004827 (Epilepsy) |
| ICD-11 | 8A6 (Epilepsy and seizures) |
| ICD-10 | G40 |
| Orphanet | Rare genetic subtypes, e.g., Dravet ORPHA:33069 |
| OMIM | Multiple loci (GEFS+ %604233; Dravet #607208; DEE series) |
| Disease Ontology | DOID:1826 |

**Synonyms / alternative names:** seizure disorder; "the epilepsies"; historically "falling sickness." Subtype names include genetic generalized epilepsy (GGE), temporal lobe epilepsy (TLE), developmental and epileptic encephalopathy (DEE), Dravet syndrome, Lennox–Gastaut syndrome (LGS), and genetic epilepsy with febrile seizures plus (GEFS+).

**Data source note:** This report is derived primarily from **aggregated, disease-level resources** (GWAS meta-analyses, GBD modeling, ILAE task-force reports, systematic reviews, model-organism studies) rather than individual patient EHR records, though several cited studies are single-center clinical cohorts.

---

## Key Findings

### F001 — Epilepsy is a common chronic brain disorder with rising global burden

Epilepsy affects **approximately 70 million individuals globally**, with pathogenesis primarily attributed to recurrent seizures caused by abnormal neuronal discharges ([PMID: 41306289](https://pubmed.ncbi.nlm.nih.gov/41306289/)). GBD 2023–based deep-learning modeling projects that the **age-standardized prevalence rate in LMICs will reach 907.22 per 100,000 by 2050** (95% UI 731.01–1083.56), a **33.32% increase from 2023** ([PMID: 42541262](https://pubmed.ncbi.nlm.nih.gov/42541262/)). Critically, the increase in **secondary (acquired) epilepsy is more than 7-fold that of idiopathic epilepsy** since 2023, signaling a shift in the etiologic composition of the global burden toward preventable, acquired causes.

> *"Epilepsy is a prevalent chronic neurological disorder, affecting approximately 70 million individuals globally, with its pathogenesis primarily attributed to recurrent seizures caused by abnormal neuronal discharges in the brain."* — [PMID: 41306289](https://pubmed.ncbi.nlm.nih.gov/41306289/)

### F002 — *SCN1A* loss-of-function causes >95% of Dravet syndrome

Dravet syndrome (DS), the prototypical genetic epileptic encephalopathy, is caused by **heterozygous loss-of-function variants in *SCN1A***, encoding the voltage-gated sodium channel α-1 subunit (Naᵥ1.1); **over 95% of cases** carry such variants ([PMID: 41712149](https://pubmed.ncbi.nlm.nih.gov/41712149/), [PMID: 40836583](https://pubmed.ncbi.nlm.nih.gov/40836583/)). Naᵥ1.1 is preferentially expressed in GABAergic interneurons, so its loss selectively impairs inhibition—a molecular explanation for the E/I imbalance. Computational stability analysis found **pathogenic missense variants significantly more destabilizing than benign variants (FoldX ΔΔG 2.61 vs 0.31 kcal/mol)** ([PMID: 42490276](https://pubmed.ncbi.nlm.nih.gov/42490276/)), yet variants at the *same codon* can produce divergent gain- vs complete loss-of-function effects (e.g., I1347T/V/F mixed function vs I1347N complete LoF), cautioning against position-based effect prediction ([PMID: 41718449](https://pubmed.ncbi.nlm.nih.gov/41718449/)).

> *"Over 95% of cases are caused by loss-of-function pathogenic variants in SCN1A, the gene encoding the voltage-gated sodium channel alpha-1 subunit."* — [PMID: 41712149](https://pubmed.ncbi.nlm.nih.gov/41712149/)

**HGNC/gene annotation:** *SCN1A* (HGNC:10585), *SCN1B* (HGNC:10586), *SCN2A*, *GABRB3*, *GABRA1*, *GRIN1*, *GRIN2B*, *CACNA1A*, *CHD2*, *MTOR*, *ALG13*, *DEPDC5*.

### F003 — Epileptogenesis involves E/I imbalance, microglial pruning of inhibitory synapses, and neuroinflammation

In epileptic mice, hyperactive inhibitory neurons activate microglia via GABAergic signaling, and these **activated microglia preferentially phagocytose inhibitory synapses**, disrupting E/I balance and amplifying network excitability ([PMID: 40425792](https://pubmed.ncbi.nlm.nih.gov/40425792/)). Pro-inflammatory cytokines reinforce this: **IL-1β promotes neuronal hyperexcitability, IL-6 mediates neuroinflammation, and TNF-α disrupts the E/I balance** ([PMID: 41306289](https://pubmed.ncbi.nlm.nih.gov/41306289/)). In focal cortical dysplasia (FCD) models, the balance of inhibitory/excitatory synaptic currents shifts toward excitation in perilesional cortex, rendering it seizure-prone ([PMID: 40003890](https://pubmed.ncbi.nlm.nih.gov/40003890/)).

> *"these activated microglia preferentially phagocytose inhibitory synapses, disrupting the balance between excitatory and inhibitory synaptic transmission and amplifying network excitability."* — [PMID: 40425792](https://pubmed.ncbi.nlm.nih.gov/40425792/)

**GO terms:** GABAergic synaptic transmission (GO:0051932), synapse pruning (GO:0098883), microglial cell activation (GO:0001774), inflammatory response (GO:0006954). **CL terms:** GABAergic interneuron (CL:0000617), microglial cell (CL:0000129), glutamatergic neuron (CL:0000679), astrocyte (CL:0000127).

### F004 — SUDEP is the leading cause of epilepsy-related premature mortality

**SUDEP accounts for 8–17% of epilepsy-related deaths** ([PMID: 42617006](https://pubmed.ncbi.nlm.nih.gov/42617006/)). Risk is elevated by refractory epilepsy, poor seizure control (frequent generalized tonic-clonic seizures), polytherapy, nocturnal/sleep-related seizures, and genetic predisposition. Mechanisms center on **neuro-cardio-respiratory dysfunction**: autonomic dysfunction, impaired heart-rate variability, seizure-related tachy-/bradyarrhythmias, and altered QT dynamics. Molecular autopsy implicates channelopathy genes *DEPDC5*, *SCN1A*, and cardiac ion-channel genes. Stress and HPA-axis dysfunction further contribute to SUDEP risk ([PMID: 42556144](https://pubmed.ncbi.nlm.nih.gov/42556144/)).

> *"Sudden unexpected death in epilepsy (SUDEP) represents a major cause of mortality in individuals with epilepsy, accounting for 8-17% of epilepsy-related deaths."* — [PMID: 42617006](https://pubmed.ncbi.nlm.nih.gov/42617006/)

### F005 — Acquired epilepsies follow brain insults via inflammation, neuron loss, and circuit reorganization

The most common acquired epilepsies arise after **acute brain insults—TBI, stroke, or CNS infections** ([PMID: 29247482](https://pubmed.ncbi.nlm.nih.gov/29247482/)). Shared cross-etiology risk factors include **intracranial bleeding, blood–brain-barrier disruption, more severe injury, and early seizures within 1 week of injury**; common histopathology includes microglial activation, astrogliosis, heterotopic white-matter neurons, neuron loss, and inflammatory infiltrates. Temporally, **most seizure recurrences occur within 1–2 years of the insult**, with risk declining sharply thereafter—defining a critical window for anti-epileptogenic intervention ([PMID: 40824375](https://pubmed.ncbi.nlm.nih.gov/40824375/)).

> *"Risk factors for developing epilepsy that appear common to multiple acute injury etiologies include intracranial bleeding, disruption of the blood-brain barrier, more severe injury, and early seizures within 1 week of injury."* — [PMID: 29247482](https://pubmed.ncbi.nlm.nih.gov/29247482/)

### F006 — High burden of bidirectional psychiatric, cognitive, and neurodevelopmental comorbidities

People with epilepsy (PWE) have disproportionately high rates of **depression, anxiety, ADHD, autism spectrum disorder, functional/dissociative seizures, and cognitive impairment**, many with **bidirectional relationships** with epilepsy ([PMID: 41868310](https://pubmed.ncbi.nlm.nih.gov/41868310/)). In structured inpatient screening, **~1 in 5 patients received a psychiatric diagnosis, and 37% of those had not been previously diagnosed** ([PMID: 41235437](https://pubmed.ncbi.nlm.nih.gov/41235437/)). Pediatric epilepsy is commonly accompanied by anxiety, depression, attention difficulties, and executive dysfunction ([PMID: 40612818](https://pubmed.ncbi.nlm.nih.gov/40612818/)). Post-surgical memory decline affects 40–60% of patients ([PMID: 41427594](https://pubmed.ncbi.nlm.nih.gov/41427594/)).

> *"Many of these disorders have bidirectional relationships with epilepsy, reflecting overlapping biological, psychological, and social mechanisms."* — [PMID: 41868310](https://pubmed.ncbi.nlm.nih.gov/41868310/)

### F007 — Genetic mouse models recapitulate Dravet syndrome and enable precision therapy

**Scn1a⁺/⁻ (haploinsufficient) mice** model *SCN1A*-derived epilepsy with spontaneous seizures and susceptibility to hyperthermia-, 6 Hz-, and PTZ-induced seizures, and are used to test intranasal nanoparticle-encapsulated neuropeptide Y (NP-NPY) and interneuron-targeted AAV gene therapy ([PMID: 41074603](https://pubmed.ncbi.nlm.nih.gov/41074603/), [PMID: 40106582](https://pubmed.ncbi.nlm.nih.gov/40106582/)). **Scn1b-null mice** model DS with spontaneous generalized seizures beginning in the second week of life plus ataxia from cerebellar Purkinje-cell hypoexcitability ([PMID: 40923316](https://pubmed.ncbi.nlm.nih.gov/40923316/)). DS carries a **10–20% rate of premature death**, recapitulated in models ([PMID: 40106582](https://pubmed.ncbi.nlm.nih.gov/40106582/)).

> *"Scn1b null mice model DS, with spontaneous generalized seizures that start in the second week of life."* — [PMID: 40923316](https://pubmed.ncbi.nlm.nih.gov/40923316/)

### F008 — Complex polygenic architecture with monogenic subsets converging on synaptic/ion-channel genes

A multi-ancestry GWAS meta-analysis of **29,944 cases and 52,538 controls identified 26 genome-wide-significant loci** (19 specific to genetic generalized epilepsy, GGE) and **29 likely causal genes**; common variants explain **39.6–90% of genetic risk for GGE**, with gene-set analyses implicating **synaptic processes in both excitatory and inhibitory neurons** ([PMID: 37653029](https://pubmed.ncbi.nlm.nih.gov/37653029/)). Overall epilepsy heritability is **~32%** ([PMID: 39904507](https://pubmed.ncbi.nlm.nih.gov/39904507/)), with ≥ 400 estimated common causal variants ([PMID: 25063994](https://pubmed.ncbi.nlm.nih.gov/25063994/)). Exome sequencing of epileptic encephalopathies found excess de novo mutations in intolerant genes including *GABRB3*, *ALG13*, *CACNA1A*, *CHD2*, *GABRA1*, *GRIN1*, *GRIN2B*, *MTOR*, *SCN2A* ([PMID: 41726570](https://pubmed.ncbi.nlm.nih.gov/41726570/)).

> *"We identify 26 genome-wide significant loci, 19 of which are specific to genetic generalized epilepsy (GGE). We implicate 29 likely causal genes underlying these 26 loci."* — [PMID: 37653029](https://pubmed.ncbi.nlm.nih.gov/37653029/)

### F009 — ASMs control ~70–80% of patients; ~30% are drug-resistant

Conventional ASMs (phenytoin, valproate, levetiracetam, lamotrigine, carbamazepine) control seizures in **70–80% of patients**, while **~30% experience drug resistance** or intolerable side effects ([PMID: 41496926](https://pubmed.ncbi.nlm.nih.gov/41496926/)). For drug-resistant epilepsy (DRE): resective surgery, ketogenic diet, vagus nerve stimulation (VNS), **responsive neurostimulation (RNS, 50–70% efficacy)**, deep brain stimulation (DBS), and **cannabidiol (~30–50% seizure reduction)**. **Everolimus (mTOR inhibitor) is the only precision therapy with class I evidence** for seizures (in tuberous sclerosis complex, TSC) ([PMID: 40411479](https://pubmed.ncbi.nlm.nih.gov/40411479/)). A **~75% treatment gap** persists in low-income countries ([PMID: 41496926](https://pubmed.ncbi.nlm.nih.gov/41496926/)).

> *"Cannabidiol (CBD) demonstrates a 30-50% seizure reduction, while responsive neurostimulation (RNS) achieves 50-70% efficacy, especially in drug-resistant epilepsy."* — [PMID: 41496926](https://pubmed.ncbi.nlm.nih.gov/41496926/)

### F010 — Canine idiopathic epilepsy is a naturally occurring cross-species model

**Idiopathic epilepsy (IE) is the most common chronic neurological disease in dogs and an established natural model** for human epilepsy of genetic/unknown etiology ([PMID: 40707505](https://pubmed.ncbi.nlm.nih.gov/40707505/), [PMID: 39804158](https://pubmed.ncbi.nlm.nih.gov/39804158/)). Dogs resemble humans in etiology and disease course; **BBB dysfunction was detected by DCE-MRI in 37% of seizing dogs**, with TGF-β pathway activation in piriform cortex ([PMID: 31032909](https://pubmed.ncbi.nlm.nih.gov/31032909/)). Canine IE plasma/fecal metabolomes show altered oxidative stress, inflammation, amino-acid metabolism (lower vitamin B6), and gut-microbiome shifts paralleling human findings.

> *"Idiopathic epilepsy (IE) is the most common chronic neurological disease in dogs, and a natural animal model for human epilepsy types with genetic and unknown etiology."* — [PMID: 40707505](https://pubmed.ncbi.nlm.nih.gov/40707505/)

### F011 — A substantial fraction of epilepsy is preventable

The **ILAE Prevention Task Force identifies four preventable etiologic categories: perinatal insults, TBI, CNS infection, and stroke** ([PMID: 29637551](https://pubmed.ncbi.nlm.nih.gov/29637551/)). **Perinatal brain insults are the largest attributable fraction in children (~15% HIC, 17% LMIC); stroke accounts for ≥50% of new-onset cases in older adults; TBI ~5%; CNS infections ~5% in LMIC.** Median active-epilepsy prevalence is **7.0/1000 in high-income and 11.1/1000 in low/middle-income countries.** **Neurocysticercosis** is a leading preventable cause in endemic regions, addressable via sanitation and clean water ([PMID: 40347840](https://pubmed.ncbi.nlm.nih.gov/40347840/)).

> *"Perinatal brain insults were the largest attributable fraction of preventable etiologies in children, with median estimated fractions of 17% in LMIC and 15% in HIC. Stroke was the most common preventable etiology among older adults."* — [PMID: 29637551](https://pubmed.ncbi.nlm.nih.gov/29637551/)

### F012 — *SCN1A* variants span a phenotypic continuum (GEFS+ → Dravet)

**Genetic epilepsy with febrile seizures plus (GEFS+) is an autosomal dominant disorder** with febrile or afebrile seizures exhibiting marked phenotypic variability, forming part of the *SCN1A* spectrum ([PMID: 35627139](https://pubmed.ncbi.nlm.nih.gov/35627139/)). The same gene thus produces a **severity continuum from mild febrile seizures (GEFS+) to severe DEE (Dravet)**, with **incomplete penetrance and highly variable expressivity**, and same-codon variants yielding divergent functional effects ([PMID: 41718449](https://pubmed.ncbi.nlm.nih.gov/41718449/)).

### F013 — Rising incidence/prevalence but falling age-standardized DALYs and mortality; secondary epilepsy grows fastest

From 1990–2021, both China and the world showed **increasing incidence and prevalence, while DALYs and mortality decreased significantly** (global AAPC −0.525% DALYs, −0.535% mortality), with projected continued increases in incidence/prevalence but ongoing DALY/mortality declines to 2045 ([PMID: 42404107](https://pubmed.ncbi.nlm.nih.gov/42404107/)). GBD 2023 modeling projects LMIC age-standardized prevalence of 907/100,000 by 2050, with **idiopathic and secondary epilepsy ASPRs of 323 and 584 per 100,000** respectively ([PMID: 42541262](https://pubmed.ncbi.nlm.nih.gov/42541262/)).

> *"From 1990 to 2021, both China and the world showed increasing trends in incidence and prevalence. In contrast, DALYs and mortality decreased significantly."* — [PMID: 42404107](https://pubmed.ncbi.nlm.nih.gov/42404107/)

### F014 — Epigenetic reprogramming forms a "cellular memory" of epileptogenesis

The **ILAE Genetics/Epigenetics Task Force** established epigenetics—DNA methylation, histone post-translational modification, and noncoding RNAs—as important mechanisms controlling gene activity in epilepsy, with potential as **biomarkers and novel therapies** ([PMID: 32301721](https://pubmed.ncbi.nlm.nih.gov/32301721/)). Experimental status epilepticus triggers spatiotemporal hypo- and hypermethylation genome-wide, and **manipulations that alter DNA methylation ameliorate cognitive and hyperexcitability phenotypes** ([PMID: 30159897](https://pubmed.ncbi.nlm.nih.gov/30159897/)). In a hippocampal neuron model, glutamate-driven excitation produced lasting histone modifications and promoter hypermethylation repressing glutamate-receptor genes *Gria2* and *Grin2a*, forming a **"cellular memory of epileptogenesis"** ([PMID: 29089052](https://pubmed.ncbi.nlm.nih.gov/29089052/)). MicroRNAs (e.g., miR-134) are candidate biomarkers and antiseizure targets.

> *"we hypothesized that epigenetic modifications may form the basis for a cellular memory of epileptogenesis."* — [PMID: 29089052](https://pubmed.ncbi.nlm.nih.gov/29089052/)

### F015 — Single-cell/spatial transcriptomics reveals cell-type-specific hippocampal remodeling in TLE

Single-nucleus RNA-seq of hippocampus after pilocarpine status epilepticus showed **reductions in specific Cck and Lamp5-Lhx6 GABAergic interneuron subclusters**, increases in Cajal–Retzius cells and dentate granule-cell precursors, and a **markedly expanded microglial subcluster termed "epilepsy-associated microglia" (EAM)** whose profile overlaps microglia in Alzheimer's disease and TBI models ([PMID: 41867871](https://pubmed.ncbi.nlm.nih.gov/41867871/)). Integrative single-cell + spatial transcriptomics in TLE with hippocampal sclerosis (TLE-HS) found **complement activity elevated and higher in sclerotic than normal hippocampus** ([PMID: 42458112](https://pubmed.ncbi.nlm.nih.gov/42458112/)). Bulk + snRNA-seq implicate myeloid/microglial immune infiltration and hub genes (*PSD4*, *P2RY13*) in hippocampal sclerosis ([PMID: 41456035](https://pubmed.ncbi.nlm.nih.gov/41456035/)).

> *"Complement activity was elevated in epilepsy. The levels were higher in hippocampal sclerosis (HS) tissue than in normal hippocampus."* — [PMID: 42458112](https://pubmed.ncbi.nlm.nih.gov/42458112/)

---

## Detailed Section-by-Section Characterization

### Section 2 — Etiology, Risk & Protective Factors

**Causal factors** span genetic (channelopathies, synaptopathies, polygenic risk), structural (FCD, hippocampal sclerosis, tumors, malformations), infectious (neurocysticercosis, meningitis/encephalitis), metabolic, immune (autoimmune encephalitis), and unknown categories.

- **Genetic risk factors:** Monogenic causal variants (*SCN1A*, *SCN2A*, *KCNQ2*, *GABRB3*, *DEPDC5*, *MTOR*, *GRIN2B*), 26 GGE susceptibility loci, and polygenic risk scores (≥400 common causal variants; heritability ~32%) (F008; [PMID: 37653029](https://pubmed.ncbi.nlm.nih.gov/37653029/), [PMID: 25063994](https://pubmed.ncbi.nlm.nih.gov/25063994/)).
- **Environmental/acquired risk factors:** TBI, stroke, CNS infection, perinatal insults, early-life seizures, intracranial bleeding, BBB disruption, febrile seizures (F005, F011). Age (bimodal: young children and elderly), family history, and stress/HPA-axis dysfunction ([PMID: 42556144](https://pubmed.ncbi.nlm.nih.gov/42556144/)).
- **Protective/modifiable factors:** Vaccination and sanitation (against neurocysticercosis/CNS infection), obstetric care, injury prevention, vascular risk-factor control, and seizure-control measures reducing SUDEP risk (F011).
- **Gene–environment interactions:** Genetic susceptibility (e.g., low seizure threshold) interacts with environmental triggers (fever in Dravet/GEFS+; stress; sleep deprivation). Gut-microbiota–host epigenetic interactions may modulate treatment response ([PMID: 42236101](https://pubmed.ncbi.nlm.nih.gov/42236101/)).

### Section 3 — Phenotypes (with HPO terms)

| Phenotype | HPO term | Type | Onset | Frequency |
|---|---|---|---|---|
| Seizures (core) | HP:0001250 | Clinical sign | Any age; bimodal | ~100% (defining) |
| Generalized tonic-clonic seizures | HP:0002069 | Clinical sign | Variable | Common |
| Focal-onset seizures | HP:0007359 | Clinical sign | Variable | Common |
| Febrile seizures | HP:0002373 | Clinical sign | Infancy/childhood | GEFS+/Dravet |
| Status epilepticus | HP:0002133 | Clinical sign | Variable | Subset |
| Intellectual disability | HP:0001249 | Neurodevelopmental | Childhood | DEE subtypes |
| Developmental regression | HP:0002376 | Neurodevelopmental | Infancy | Dravet/DEE |
| Ataxia | HP:0001251 | Physical | Variable | Dravet (adult) |
| Anxiety | HP:0000739 | Behavioral | Any | High in PWE |
| Depression | HP:0000716 | Behavioral | Any | High in PWE |
| Cognitive impairment | HP:0100543 | Behavioral/lab | Any | Common |
| EEG abnormality | HP:0002353 | Lab | Any | Diagnostic |

**Characteristics:** Onset ranges from neonatal to geriatric; severity from mild (self-limited GEFS+) to severe (DEE with premature death). Course is typically **episodic/fluctuating** (seizures) superimposed on a chronic disorder; some DEEs are progressive. **Quality-of-life impact** is substantial—driving restrictions, employment barriers, stigma, psychiatric comorbidity, and cognitive decline (F006).

### Section 4 — Genetic / Molecular Information

**Causal genes** (F002, F008): *SCN1A* (Naᵥ1.1, Dravet/GEFS+), *SCN1B*, *SCN2A*, *KCNQ2*, *GABRB3*, *GABRA1*, *GRIN1*, *GRIN2B*, *CACNA1A*, *CHD2*, *MTOR* (mTORopathies/FCD), *DEPDC5*, *ALG13*, *TSC1/TSC2* (TSC). **Variant types:** missense (often destabilizing), frameshift, nonsense, splice-site, and structural. **Functional consequences:** predominantly loss-of-function in Dravet (Naᵥ1.1 in interneurons → disinhibition), but gain-of-function in some *SCN2A/SCN8A* and *GRIN* variants. Same-codon divergence complicates ACMG/AMP classification ([PMID: 41718449](https://pubmed.ncbi.nlm.nih.gov/41718449/)). **Somatic mosaicism** in *MTOR* drives FCD (non-cell-autonomous epileptogenesis; [PMID: 34180075](https://pubmed.ncbi.nlm.nih.gov/34180075/)). **Epigenetic:** DNA methylation, histone modification, ncRNA dysregulation (F014). **Chromosomal:** microdeletions/duplications (e.g., 15q13.3) detectable by CMA; pathogenic CNVs found in 52% of an ASD-epilepsy overlap cohort by microarray ([PMID: 42207445](https://pubmed.ncbi.nlm.nih.gov/42207445/)).

### Section 5 — Environmental Information

Toxins/withdrawal (alcohol), perinatal hypoxia-ischemia, TBI, radiation, and pollution contribute. **Lifestyle factors:** sleep deprivation, alcohol, and stress are seizure triggers; the gut–brain axis and diet modulate seizure susceptibility ([PMID: 42236101](https://pubmed.ncbi.nlm.nih.gov/42236101/)). Climate change is an emerging environmental influence on neurological burden ([PMID: 42626786](https://pubmed.ncbi.nlm.nih.gov/42626786/)). **Infectious agents:** *Taenia solium* (neurocysticercosis; leading preventable cause in endemic regions), bacterial/viral meningoencephalitis (F011; [PMID: 40347840](https://pubmed.ncbi.nlm.nih.gov/40347840/)).

### Section 6 — Mechanism / Pathophysiology

The unifying mechanism is **excitation/inhibition imbalance** (see Mechanistic Model). **Molecular pathways:** GABAergic/glutamatergic signaling, **mTOR pathway** (TSC/FCD mTORopathies; [PMID: 34298906](https://pubmed.ncbi.nlm.nih.gov/34298906/), [PMID: 34180075](https://pubmed.ncbi.nlm.nih.gov/34180075/)), **TGF-β/BBB** signaling, complement cascade, and cytokine (IL-1β/IL-6/TNF-α) signaling. **Cellular processes:** microglial synapse pruning, astrogliosis, neuroinflammation, neuronal loss, aberrant neurogenesis, synaptic reorganization (mossy-fiber sprouting). **Protein dysfunction:** Naᵥ1.1 loss-of-function/misfolding (F002). **Metabolic changes:** oxidative stress, altered amino-acid metabolism, vitamin B6 depletion (canine parallel; F010). **Immune involvement:** autoimmune epilepsy responsive to immunotherapy ([PMID: 40249641](https://pubmed.ncbi.nlm.nih.gov/40249641/)); NORSE responsive to IL-6 blockade (tocilizumab; [PMID: 40100558](https://pubmed.ncbi.nlm.nih.gov/40100558/)); Mendelian randomization links polymyositis to epilepsy via T-cell/microglial neuroinflammation ([PMID: 41466027](https://pubmed.ncbi.nlm.nih.gov/41466027/)). **Molecular profiling:** single-cell/spatial transcriptomics reveal EAM and complement activation (F015).

**Ontology annotation:** GO:0006954 (inflammatory response), GO:0098883 (synapse pruning), GO:0051932 (GABAergic transmission), GO:0032526 (response to fever), CL:0000617 (GABAergic interneuron), CL:0000129 (microglia), UBERON:0001954 (Ammon's horn/hippocampus). **CHEBI:** GABA (CHEBI:16865), glutamate (CHEBI:14321), cannabidiol (CHEBI:69478).

### Section 7 — Anatomical Structures Affected

- **Organ:** brain (UBERON:0000955); body system: nervous system (UBERON:0001016). Secondary: cardiovascular (SUDEP arrhythmias), respiratory (peri-ictal apnea), endocrine (HPA axis).
- **Tissue/cell:** nervous tissue; GABAergic interneurons (CL:0000617), glutamatergic pyramidal neurons (CL:0000679), microglia (CL:0000129), astrocytes (CL:0000127), cerebellar Purkinje cells (CL:0000121, Dravet ataxia).
- **Subcellular:** ion channels at the plasma membrane/axon initial segment (GO:0043194); nucleus (epigenetic/DNA methylation); mitochondria (metabolic/oxidative stress).
- **Localization:** commonly **hippocampus** (UBERON:0001954), temporal lobe (UBERON:0001871), neocortex; often unilateral in mesial TLE-HS, bilateral/generalized in GGE. FCD is focal.

### Section 8 — Temporal Development

**Onset:** bimodal—early childhood (genetic/DEE, perinatal) and older adults (stroke-related). **Onset pattern:** may be acute (post-insult) or insidious (genetic). **Progression:** most epilepsies are chronic/lifelong with an episodic seizure course; DEEs may be progressive with developmental plateau/regression; adult Dravet shows accelerated-aging neuropathology ([PMID: 40956029](https://pubmed.ncbi.nlm.nih.gov/40956029/)). **Critical periods:** acquired-epilepsy recurrence risk peaks within 1–2 years of insult (F005), defining an anti-epileptogenic intervention window. **Remission:** ~65–70% achieve treatment-induced remission; some childhood syndromes remit spontaneously.

### Section 9 — Inheritance and Population

- **Epidemiology:** ~50–70 million affected worldwide; active-epilepsy prevalence 7.0/1000 (HIC) and 11.1/1000 (LMIC) (F001, F011). Rising incidence/prevalence, falling age-standardized DALYs/mortality (F013).
- **Inheritance:** predominantly **multifactorial/polygenic**; monogenic subsets are **autosomal dominant** (GEFS+, most Dravet as de novo), with **incomplete, age-dependent penetrance** and **highly variable expressivity** (F012). Some AR and mitochondrial forms exist. De novo mutations are common in DEEs (F008).
- **Demographics:** slight variation by sex/geography; LMICs bear disproportionate acquired burden; neurocysticercosis endemic in Latin America, sub-Saharan Africa, and parts of Asia ([PMID: 8490989](https://pubmed.ncbi.nlm.nih.gov/8490989/)).

### Section 10 — Diagnostics

- **Electrophysiology:** EEG is the cornerstone; abnormal EEG is the strongest independent predictor of epilepsy (OR 48.96 in an ASD cohort; [PMID: 42207445](https://pubmed.ncbi.nlm.nih.gov/42207445/)); intracranial EEG for surgical planning.
- **Imaging:** MRI (FCD, hippocampal sclerosis, lesions), PET, DCE-MRI for BBB (translational; [PMID: 31032909](https://pubmed.ncbi.nlm.nih.gov/31032909/)).
- **Genetic testing:** gene panels, WES, WGS, CMA/karyotype; high yield in DEE and early-onset epilepsy (GTR/ClinVar/GeneReviews). Molecular autopsy for SUDEP.
- **Labs/biomarkers:** autoantibody panels (autoimmune epilepsy), metabolic workup; emerging miRNA (miR-134) and complement biomarkers (F014, F015).
- **Clinical criteria:** ILAE operational definition and classification; differential diagnosis includes syncope, functional/dissociative seizures ([PMID: 39510015](https://pubmed.ncbi.nlm.nih.gov/39510015/)), migraine, and movement disorders.

### Section 11 — Outcome / Prognosis

**~70–80% achieve seizure control; ~30% remain drug-resistant** (F009). **SUDEP** is the leading cause of premature death (8–17% of epilepsy deaths; F004). DS carries 10–20% premature mortality (F007). Morbidity is driven by injury, psychiatric/cognitive comorbidity (F006), and reduced QoL. **Prognostic factors:** etiology, seizure frequency/type (GTCS), drug response, EEG/imaging findings, and genetic diagnosis. Post-surgical memory decline affects 40–60% ([PMID: 41427594](https://pubmed.ncbi.nlm.nih.gov/41427594/)).

### Section 12 — Treatment (with NCIT suggestions)

| Modality | Examples | Efficacy/Notes | NCIT |
|---|---|---|---|
| ASMs (broad) | levetiracetam, valproate, lamotrigine, carbamazepine, phenytoin | 70–80% control | NCIT:C264 (Anticonvulsant Agent) |
| Newer ASMs | cenobamate, clobazam, perampanel, fenfluramine | CNB+CLB: 72–82% responders in DRE ([PMID: 41919359](https://pubmed.ncbi.nlm.nih.gov/41919359/)) | — |
| Cannabidiol | Epidiolex | 30–50% seizure reduction | NCIT:C81660 |
| Precision (mTOR) | everolimus (TSC) | Only class I precision therapy | NCIT:C48387 |
| Surgery | resection, corpus callosotomy | Effective in focal DRE/LGS | NCIT:C15329 |
| Neuromodulation | VNS, RNS (50–70%), DBS | For DRE | NCIT:C99924 (VNS) |
| Diet | ketogenic diet | Broad efficacy, esp. DEE/LGS | NCIT:C92877 |
| Immunotherapy | IV methylprednisolone, IVIG, tocilizumab | Autoimmune/NORSE ([PMID: 40249641](https://pubmed.ncbi.nlm.nih.gov/40249641/), [PMID: 40100558](https://pubmed.ncbi.nlm.nih.gov/40100558/)) | — |
| Gene/RNA therapy | AAV interneuron-targeted, ASOs, NP-NPY | Preclinical/emerging ([PMID: 40106582](https://pubmed.ncbi.nlm.nih.gov/40106582/), [PMID: 41074603](https://pubmed.ncbi.nlm.nih.gov/41074603/)) | — |

Treatment strategy: mechanism/syndrome-guided (e.g., avoid sodium-channel blockers in Dravet); seizure-type-specific in LGS ([PMID: 40409093](https://pubmed.ncbi.nlm.nih.gov/40409093/), [PMID: 41391422](https://pubmed.ncbi.nlm.nih.gov/41391422/)); precision therapy by genotype ([PMID: 40411479](https://pubmed.ncbi.nlm.nih.gov/40411479/)).

### Section 13 — Prevention

**Primary:** obstetric/perinatal care, TBI prevention, stroke risk-factor control, vaccination and sanitation against CNS infection/neurocysticercosis (F011; [PMID: 29637551](https://pubmed.ncbi.nlm.nih.gov/29637551/), [PMID: 40347840](https://pubmed.ncbi.nlm.nih.gov/40347840/)). **Secondary:** early seizure detection, EEG screening in high-risk groups (e.g., ASD; [PMID: 42207445](https://pubmed.ncbi.nlm.nih.gov/42207445/)). **Tertiary:** SUDEP risk communication and safety counseling ([PMID: 42208388](https://pubmed.ncbi.nlm.nih.gov/42208388/), [PMID: 42435512](https://pubmed.ncbi.nlm.nih.gov/42435512/)), medication adherence, comorbidity management, and genetic counseling for heritable subtypes.

### Section 14 — Other Species / Natural Disease

**Dogs (*Canis lupus familiaris*, NCBI:txid9615)** develop naturally occurring idiopathic epilepsy—the most common canine chronic neurological disease—recapitulating human etiology, disease course, BBB dysfunction, and metabolomic shifts (F010; [PMID: 40707505](https://pubmed.ncbi.nlm.nih.gov/40707505/), [PMID: 31032909](https://pubmed.ncbi.nlm.nih.gov/31032909/), [PMID: 42280378](https://pubmed.ncbi.nlm.nih.gov/42280378/)). This provides strong evolutionary conservation of epileptogenic mechanisms and translational value. Orthologous *SCN1A* exists across mammals. Epilepsy itself is non-transmissible; its infectious *cause* neurocysticercosis is transmitted via the *T. solium* lifecycle involving pigs.

### Section 15 — Model Organisms

- **Mouse (*Mus musculus*, NCBI:txid10090):** Scn1a⁺/⁻ and Scn1b-null Dravet models (F007); pilocarpine/kainate chemoconvulsant TLE models; freeze-lesion FCD models; MTOR-mosaic FCD models ([PMID: 34180075](https://pubmed.ncbi.nlm.nih.gov/34180075/)). Genetic tools: knockout, conditional, humanized. Resources: MGI, IMPC.
- **Rat:** freeze-induced neocortical malformation, pilocarpine status epilepticus ([PMID: 40003890](https://pubmed.ncbi.nlm.nih.gov/40003890/), [PMID: 29089052](https://pubmed.ncbi.nlm.nih.gov/29089052/)); RGD.
- **In vitro/cellular:** cultured hippocampal neurons (epigenetic memory; [PMID: 29089052](https://pubmed.ncbi.nlm.nih.gov/29089052/)), iPSC-derived neurons, organoids.
- **Phenotype recapitulation:** models reproduce spontaneous seizures, interneuron dysfunction, premature death (Dravet), and BBB/inflammation; **limitations** include incomplete replication of the human cognitive/behavioral comorbidity spectrum and genetic-background effects.

---

## Mechanistic Model / Interpretation

The findings cohere into a **convergent E/I-imbalance model** in which diverse etiologies funnel into a common final pathway of hyperexcitable, hypersynchronous networks:

```
   ETIOLOGIC TRIGGERS (upstream, heterogeneous)
   ┌───────────────────────────────────────────────────────────┐
   │ Genetic          Acquired insults        Structural/Immune  │
   │ • SCN1A LoF       • TBI                   • FCD (MTOR mosaic)│
   │ • GABRB3, GRIN…   • Stroke                • Hippocampal scler│
   │ • Polygenic (26   • CNS infection         • Autoimmune (Ab)  │
   │   GWAS loci)      • Perinatal insult      • NORSE (IL-6)     │
   └───────────────┬───────────────────┬───────────────────────┘
                   │                   │
      Loss of interneuron       BBB disruption + TGF-β
      inhibition (Nav1.1↓)      + cytokines (IL-1β,IL-6,TNF-α)
                   │                   │
                   ▼                   ▼
        ┌─────────────────────────────────────────┐
        │   NEUROINFLAMMATION & GLIAL REMODELING   │
        │  • Microglial pruning of INHIB. synapses │
        │  • "Epilepsy-associated microglia" (EAM) │
        │  • Astrogliosis, complement activation   │
        └───────────────────┬─────────────────────┘
                            ▼
        ┌─────────────────────────────────────────┐
        │   E / I  IMBALANCE  → NET EXCITATION      │  ← core convergent node
        └───────────────────┬─────────────────────┘
                            ▼
        ┌─────────────────────────────────────────┐
        │  EPIGENETIC "CELLULAR MEMORY"            │  (feed-forward, self-reinforcing)
        │  • DNA methylation of Gria2/Grin2a       │
        │  • Histone modifications, miR-134        │
        │  • Circuit reorganization (sprouting)    │
        └───────────────────┬─────────────────────┘
                            ▼
   HYPERSYNCHRONOUS DISCHARGE → RECURRENT SEIZURES (clinical epilepsy)
                            │
          ┌─────────────────┼──────────────────────┐
          ▼                 ▼                      ▼
   Psychiatric/cognitive  Drug resistance     SUDEP (neuro-cardio-
   comorbidity (bidir.)   (~30%)              respiratory failure)
```

**Upstream vs downstream:** Etiologic triggers and interneuron/inhibition loss are **upstream**; neuroinflammation and glial synapse-pruning are **intermediate amplifiers**; the epigenetic "cellular memory" and circuit reorganization are **feed-forward mechanisms** that render epilepsy self-sustaining and chronic; seizures, comorbidity, drug resistance, and SUDEP are **downstream clinical manifestations**. This model explains why a single mechanism (disinhibition) can arise from a sodium-channel mutation, a somatic mTOR mutation, a stroke, or an autoimmune attack—and why immunomodulation, neuromodulation, dietary, and precision-genetic approaches can each intercept the pathway at different nodes.

---

## Evidence Base

| PMID | Finding(s) | Contribution |
|---|---|---|
| [41306289](https://pubmed.ncbi.nlm.nih.gov/41306289/) | F001, F003 | Global prevalence (70M); cytokine mechanisms of hyperexcitability |
| [42541262](https://pubmed.ncbi.nlm.nih.gov/42541262/) | F001, F013 | GBD 2050 LMIC projections; secondary epilepsy rising 7× faster |
| [41712149](https://pubmed.ncbi.nlm.nih.gov/41712149/) / [40836583](https://pubmed.ncbi.nlm.nih.gov/40836583/) | F002 | *SCN1A* LoF >95% of Dravet; Naᵥ1.1 |
| [42490276](https://pubmed.ncbi.nlm.nih.gov/42490276/) / [41718449](https://pubmed.ncbi.nlm.nih.gov/41718449/) | F002, F012 | Variant destabilization; same-codon functional divergence |
| [40425792](https://pubmed.ncbi.nlm.nih.gov/40425792/) | F003 | Microglial pruning of inhibitory synapses |
| [40003890](https://pubmed.ncbi.nlm.nih.gov/40003890/) | F003 | E/I shift toward excitation in FCD perilesional cortex |
| [42617006](https://pubmed.ncbi.nlm.nih.gov/42617006/) | F004 | SUDEP 8–17% of deaths; neuro-cardio-respiratory mechanism |
| [29247482](https://pubmed.ncbi.nlm.nih.gov/29247482/) / [40824375](https://pubmed.ncbi.nlm.nih.gov/40824375/) | F005 | Acquired etiologies; 1–2-yr critical window |
| [41868310](https://pubmed.ncbi.nlm.nih.gov/41868310/) / [41235437](https://pubmed.ncbi.nlm.nih.gov/41235437/) | F006 | Bidirectional comorbidities; 1-in-5 undiagnosed psychiatric |
| [40923316](https://pubmed.ncbi.nlm.nih.gov/40923316/) / [41074603](https://pubmed.ncbi.nlm.nih.gov/41074603/) / [40106582](https://pubmed.ncbi.nlm.nih.gov/40106582/) | F007 | Mouse Dravet models; precision therapy testing |
| [37653029](https://pubmed.ncbi.nlm.nih.gov/37653029/) / [39904507](https://pubmed.ncbi.nlm.nih.gov/39904507/) / [25063994](https://pubmed.ncbi.nlm.nih.gov/25063994/) / [41726570](https://pubmed.ncbi.nlm.nih.gov/41726570/) | F008 | GWAS 26 loci; heritability 32%; ≥400 variants; DEE de novo genes |
| [41496926](https://pubmed.ncbi.nlm.nih.gov/41496926/) / [40411479](https://pubmed.ncbi.nlm.nih.gov/40411479/) | F009 | 70–80% control; RNS/CBD figures; everolimus class I |
| [40707505](https://pubmed.ncbi.nlm.nih.gov/40707505/) / [31032909](https://pubmed.ncbi.nlm.nih.gov/31032909/) / [39804158](https://pubmed.ncbi.nlm.nih.gov/39804158/) | F010 | Canine natural model; BBB dysfunction; metabolome |
| [29637551](https://pubmed.ncbi.nlm.nih.gov/29637551/) / [40347840](https://pubmed.ncbi.nlm.nih.gov/40347840/) | F011 | ILAE preventable etiologies; neurocysticercosis |
| [42404107](https://pubmed.ncbi.nlm.nih.gov/42404107/) | F013 | Rising incidence, falling DALYs/mortality |
| [32301721](https://pubmed.ncbi.nlm.nih.gov/32301721/) / [30159897](https://pubmed.ncbi.nlm.nih.gov/30159897/) / [29089052](https://pubmed.ncbi.nlm.nih.gov/29089052/) | F014 | Epigenetics as mechanism/biomarker; cellular memory |
| [41867871](https://pubmed.ncbi.nlm.nih.gov/41867871/) / [42458112](https://pubmed.ncbi.nlm.nih.gov/42458112/) / [41456035](https://pubmed.ncbi.nlm.nih.gov/41456035/) | F015 | EAM; complement activation; HS hub genes |

**Supporting/converging evidence:** Autoimmune epilepsy responsive to immunotherapy ([PMID: 40249641](https://pubmed.ncbi.nlm.nih.gov/40249641/)), NORSE responsive to tocilizumab ([PMID: 40100558](https://pubmed.ncbi.nlm.nih.gov/40100558/)), and Mendelian-randomization linking polymyositis to epilepsy via neuroinflammation ([PMID: 41466027](https://pubmed.ncbi.nlm.nih.gov/41466027/)) all reinforce the inflammatory arm of the model. Non-cell-autonomous FCD epileptogenesis ([PMID: 34180075](https://pubmed.ncbi.nlm.nih.gov/34180075/)) illustrates how few mutant neurons induce network-level hyperexcitability.

---

## Limitations and Knowledge Gaps

1. **Mechanism causality vs correlation:** Much single-cell/epigenetic data (F014, F015) is associative or from rodent status-epilepticus models; whether EAM and complement activation are drivers or consequences of seizures requires causal perturbation in humans.
2. **Genetic architecture incompleteness:** Despite 26 GWAS loci and heritability of 32%, substantial "missing heritability" remains; ≥400 causal variants are estimated but most are unidentified (F008).
3. **Variant interpretation:** Same-codon functional divergence (F002/F012) undermines position-based prediction, leaving many *SCN1A* variants as VUS and complicating precision therapy.
4. **Model-organism translation:** Mouse Dravet models recapitulate seizures and premature death but incompletely model human cognitive/behavioral comorbidities and genetic-background modifiers (F007).
5. **Comorbidity underdiagnosis:** 37% of psychiatric comorbidity is undetected in routine care (F006), and QoL data are heterogeneous and often not phenotype-specific.
6. **LMIC data gaps:** GBD projections rely on modeling with wide uncertainty intervals (F001, F013); primary epidemiologic data from LMICs remain sparse.
7. **Precision therapy scarcity:** Only everolimus has class I precision evidence (F009); gene/RNA therapies remain largely preclinical.
8. **Report scope:** This is a literature-synthesis report (no primary dataset analyzed); citation snippets were validated against abstracts, but some claims rest on single studies.

---

## Proposed Follow-up Experiments / Actions

1. **Causal test of microglial pruning:** Conditional depletion or complement (C1q/C3) blockade in Dravet and post-TBI models to determine whether preventing inhibitory-synapse phagocytosis is anti-epileptogenic (extends F003, F015).
2. **Epigenetic therapy trials:** Test DNA-methylation modulators and antimiR-134 in the 1–2-year post-insult critical window (F005, F014) as anti-epileptogenic interventions after TBI/stroke.
3. **Functional variant screening:** High-throughput deep mutational scanning of *SCN1A* to resolve VUS and enable genotype-matched precision therapy, addressing same-codon divergence (F002, F012).
4. **Biomarker validation:** Prospectively validate circulating miR-134, complement components, and BBB permeability (DCE-MRI) as predictive biomarkers of epileptogenesis and drug resistance across species (F010, F014, F015).
5. **Preventive public-health modeling:** Quantify epilepsy cases avertable by scaling perinatal care, TBI prevention, stroke control, and neurocysticercosis elimination in LMICs to guide investment (F011, F013).
6. **SUDEP risk stratification:** Combine molecular-autopsy channelopathy panels with wearable cardio-respiratory monitoring to build predictive SUDEP-risk models (F004).
7. **Comorbidity integration:** Embed structured psychiatric/cognitive screening (shown to detect 1-in-5 cases, 37% previously undiagnosed) into standard epilepsy care pathways and measure QoL outcomes (F006).
8. **Cross-species translational pipeline:** Leverage naturally epileptic dogs for anti-epileptogenic drug trials before human translation (F010).

---

*Report compiled from 15 confirmed findings and 62 reviewed papers. All quantitative claims are traceable to the cited PMIDs and validated abstract quotes.*


## Artifacts

- [OpenScientist final report](Epilepsy-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Epilepsy-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 55 |
| Resolved | 55 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 55 |
| On topic | 27 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:42626786` (2 mentions) - Climate Change, Neurological Disorders and Brain Health: To-Know Concepts and Future Actions by the EAN Environmental Influences in Neurology Task Force.
  - shared terms: model

Weighed against this report's own most characteristic terms: `epilepsy`, `seizure`, `genetic`, `dravet`, `gene`, `model`, `scn1a`, `epigenetic`, `sudep`, `variant`, `control`, `mechanism`, `dysfunction`, `neurocysticercosis`, `risk`, `bbb`, `interneuron`, `death`, `lmic`, `neuron`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.
