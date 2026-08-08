---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-31T17:30:34.776807'
end_time: '2026-07-31T17:50:31.447597'
duration_seconds: 1196.67
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Charcot-Marie-Tooth Disease X-linked Recessive 4
  mondo_id: ''
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
citation_count: 28
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Charcot-Marie-Tooth_Disease_X-linked_Recessive_4-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Charcot-Marie-Tooth_Disease_X-linked_Recessive_4-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Charcot-Marie-Tooth Disease X-linked Recessive 4
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Charcot-Marie-Tooth Disease X-linked Recessive 4** covering all of the
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

# Charcot-Marie-Tooth Disease X-linked Recessive 4 (CMTX4 / Cowchock Syndrome): A Comprehensive Disease Characterization

**Disease:** Charcot-Marie-Tooth Disease X-linked Recessive 4 (CMTX4)
**Synonyms:** Cowchock syndrome; Cowchock-Aita-Cann syndrome; X-linked motor-sensory neuropathy type II with deafness and mental retardation; CMT4X
**Causal gene:** *AIFM1* (apoptosis-inducing factor mitochondria-associated 1), Xq26.1
**OMIM:** 310490 (Cowchock/CMTX4 phenotype); 300169 (*AIFM1* gene)
**Category:** Genetic (X-linked recessive, mitochondrial-associated)

---

## Summary

Charcot-Marie-Tooth disease X-linked recessive 4 (CMTX4), historically named **Cowchock syndrome**, is an ultra-rare, slowly progressive, X-linked recessive **axonal sensorimotor peripheral neuropathy** distinguished from most other CMT subtypes by its consistent association with **sensorineural (auditory-neuropathy type) deafness** and **cognitive impairment**. It is caused by hemizygous missense variants in *AIFM1* (Xq26.1), the gene encoding **apoptosis-inducing factor (AIF)**, a FAD-containing, NADH-dependent mitochondrial oxidoreductase that operates as a redox-controlled switch between mitochondrial biogenesis and caspase-independent cell death. Affected males typically present from infancy or childhood with distal limb weakness and atrophy, distal sensory loss, areflexia, pes cavus and hammer toes, together with variable hearing loss, intellectual disability, cerebellar ataxia, pyramidal signs, tremor, and color-vision deficiency.

Mechanistically, CMTX4-causing variants do **not** typically produce overt respiratory-chain (OXPHOS) failure. Instead, they **destabilize the AIF protein, alter its redox properties, and weaken the AIF:CHCHD4/MIA40 interaction** that is required for mitochondrial protein import and the assembly of respiratory complex I and respiratory supercomplexes. This converts AIF from a pro-survival, biogenesis-supporting factor into a driver of increased apoptotic cell death, with prominent, length-dependent effects on peripheral axons, auditory neurons, and central neurons (cerebellum, thalamus, striatum, cortex). *AIFM1* mutations cause a broad **allelic spectrum**, from the relatively mild CMTX4/Cowchock phenotype to severe infantile mitochondrial encephalomyopathy (COXPD6), auditory neuropathy (DFNX5), spondyloepimetaphyseal dysplasia with neurodegeneration, motor-neuron/anterior-horn disease, and cardiomyopathy.

There is **no disease-specific or curative therapy** for CMTX4. Management is entirely supportive and rehabilitative: ankle-foot orthoses, physical/occupational therapy, orthopedic surgery for foot deformities, hearing aids or cochlear implants for the auditory component, and deep-brain stimulation (DBS) of the ventral intermediate thalamic nucleus for disabling AIFM1-related tremor. Prevention centers on genetic counseling, cascade carrier testing, and prenatal or preimplantation genetic diagnosis, with attention to the possibility of manifesting female carriers via skewed X-inactivation. This report synthesizes 12 confirmed findings and 34 reviewed papers into a comprehensive knowledge-base entry structured by disease characteristic.

---

## Key Findings

### Finding 1 — CMTX4/Cowchock syndrome is caused by hemizygous *AIFM1* missense variants at Xq26.1

Exome sequencing of an affected individual from the originally described Cowchock family identified a missense change **c.1478A>T (p.Glu493Val)** in *AIFM1*, the gene encoding apoptosis-inducing factor (AIF), which cosegregated with the phenotype ([PMID: 23217327](https://pubmed.ncbi.nlm.nih.gov/23217327/)). This built upon earlier linkage work that had mapped the locus to Xq24–q26: *"DXS425 (Xq24) and HPRT (Xq26.1) are flanking markers and that the disease gene is closely linked to the markers DXS1122, DXS994, DXS737, DXS1206, and DXS1047"* ([PMID: 8666389](https://pubmed.ncbi.nlm.nih.gov/8666389/)).

*AIFM1* (**HGNC:8768**, cytoband **Xq26.1**, NCBI Gene **9131**) encodes a FAD-dependent NADH oxidase that is imported into mitochondria. The disease phenotype carries **OMIM 310490** (Cowchock/CMTX4), with the gene at **OMIM 300169**. Additional pathogenic missense variants have since been reported across multiple families worldwide, confirming *AIFM1* as the single causal gene for this subtype.

**Ontology anchors:** MONDO — Charcot-Marie-Tooth disease X-linked recessive 4 / Cowchock syndrome; gene *AIFM1* (HGNC:8768).

### Finding 2 — Core phenotype: axonal sensorimotor neuropathy + sensorineural deafness + cognitive impairment, with variable cerebellar ataxia

The original 1985 description documented severe distal weakness, muscle atrophy, sensory loss, areflexia, pes cavus, and hammer toes from infancy, with **5 of 7 affected males** exhibiting deafness and **3 of 5** showing intellectual disability ([PMID: 3856385](https://pubmed.ncbi.nlm.nih.gov/3856385/); [PMID: 8666389](https://pubmed.ncbi.nlm.nih.gov/8666389/)). The authors emphasized *"the observation that males are severely affected from infancy, and the frequent association of deafness and/or mental retardation with the neuromuscular disorder."*

The clinical spectrum was substantially expanded by an Irish family (7 affected males; onset ranging from 18 months to 39 years; SARA ataxia scores 2–23/40; CMTNS2 scores 7–13/36), in which *"All developed variably present sensorineural deafness, peripheral neuropathy, cerebellar ataxia, and pyramidal involvement. In addition, three had colour vision deficiency"* ([PMID: 31523922](https://pubmed.ncbi.nlm.nih.gov/31523922/)). Nerve conduction studies show a length-dependent large-fibre axonal sensorimotor neuropathy with markedly abnormal sensory responses.

**Suggested HPO terms:** HP:0003477 (Peripheral sensorimotor neuropathy), HP:0000407 (Sensorineural hearing impairment), HP:0001272/HP:0001251 (Cerebellar atrophy/Ataxia), HP:0007256/HP:0001347 (Pyramidal/Hyperreflexia), HP:0001761 (Pes cavus), HP:0001284 (Areflexia), HP:0001256 (Intellectual disability, mild), HP:0000551 (Abnormality of color vision), HP:0001337 (Tremor).

### Finding 3 — Mechanism: *AIFM1* variants impair AIF redox/import functions rather than causing overt OXPHOS failure

The p.Glu493Val CMTX4 mutation *"alters the redox properties of the AIF protein and results in increased cell death via apoptosis, without affecting the activity of the respiratory chain complexes"* ([PMID: 23217327](https://pubmed.ncbi.nlm.nih.gov/23217327/)). This is a critical distinction: unlike the severe infantile encephalomyopathies at the other end of the *AIFM1* spectrum, CMTX4 is driven by a **subtler redox/apoptotic imbalance** rather than a wholesale collapse of oxidative phosphorylation.

AIF supports respiration indirectly by promoting the import of MIA40 (**CHCHD4** in humans) and the assembly of complex I; it functions as a *"redox-controlled gear box to switch between mitochondrial biogenesis and cell death"* ([PMID: 32769219](https://pubmed.ncbi.nlm.nih.gov/32769219/)). Supporting the neurodegenerative relevance, AIF-deficient Harlequin mice show a 40–50% reduction in complex I with progressive multifocal neurodegeneration prominent in the cerebellum ([PMID: 17805014](https://pubmed.ncbi.nlm.nih.gov/17805014/); [PMID: 19280713](https://pubmed.ncbi.nlm.nih.gov/19280713/)).

**Suggested GO terms:** GO:0006915 (apoptotic process), GO:0032981 (mitochondrial respiratory chain complex I assembly), GO:0045333 (cellular respiration), GO:0016651 (oxidoreductase activity), GO:0006626 (protein targeting to mitochondrion).

### Finding 4 — AIF is a FAD/NADH oxidoreductase whose redox-linked dimerization couples metabolism to caspase-independent apoptosis

AIF is a FAD-containing, NADH-dependent oxidoreductase resident in the mitochondrial intermembrane space. Upon apoptotic insult it is proteolyzed and translocates to the nucleus to trigger caspase-independent chromatin condensation and DNA degradation. Its redox activity *"is essential for optimal oxidative phosphorylation. Additionally, the protein is proposed to regulate the respiratory chain indirectly, through assembly and/or stabilization of complexes I and III"* ([PMID: 20868295](https://pubmed.ncbi.nlm.nih.gov/20868295/)).

X-ray crystallography reveals the structural basis of the switch: NADH reduction drives formation of a tight FADH2–NAD charge-transfer complex, and *"redox changes in the active site are transmitted to the surface, promoting AIF dimerization and restricting access to a primary nuclear localization signal through which the apoptogenic form is transported to the nucleus"* ([PMID: 19447115](https://pubmed.ncbi.nlm.nih.gov/19447115/)). Pathological-equivalent mutations in the adenylate-binding site (e.g., murine G307E, equivalent to human G308E) *"decrease the affinity and association rate of NAD(+)/H, which, in turn, perturbs CT complex formation and protein dimerization"* ([PMID: 26535916](https://pubmed.ncbi.nlm.nih.gov/26535916/)). These structural insights explain how single missense substitutions perturb AIF's dual life/death functions.

**Suggested CHEBI terms:** CHEBI:16238 (FAD), CHEBI:16908 (NADH), CHEBI:15846 (NAD+).

### Finding 5 — Mechanism refined: CMTX4 variants destabilize AIF, deplete CHCHD4, and impair respiratory supercomplex assembly

A hemizygous *AIFM1* **c.1006G>A (p.Glu336Lys)** variant in a male with childhood-onset progressive axonal sensorimotor polyneuropathy and sensorineural hearing loss — a canonical CMTX4 phenotype — provided direct mechanistic evidence. Patient-derived fibroblasts *"exhibited reduced AIF protein stability despite preserved mRNA expression, impaired growth in OXPHOS-dependent conditions, decreased basal respiration, and altered assembly of mitochondrial respiratory supercomplexes. These defects were accompanied by reduced CHCHD4 protein levels and mitochondrial content"* ([PMID: 41957773](https://pubmed.ncbi.nlm.nih.gov/41957773/)).

Biophysical characterization of purified protein showed the *"E336K protein exhibited compromised FAD retention, decreased thermal stability, impaired NADH affinity, destabilization of the charge-transfer complex crucial for sustaining the AIF:CHCHD4 interaction"* with a shift toward NADPH and remodeling of the NADH-binding cleft ([PMID: 41957773](https://pubmed.ncbi.nlm.nih.gov/41957773/)). This unifies the CMTX4 pathomechanism: **protein destabilization → weakened AIF:CHCHD4/MIA40 import machinery → impaired complex I/supercomplex assembly → mitochondrial dysfunction and neurodegeneration**, consistent with the redox mechanism first shown for p.Glu493Val.

### Finding 6 — The Harlequin (Hq) mouse is the principal AIF-deficiency model, recapitulating cerebellar/sensory neurodegeneration and complex I loss

The **Harlequin (Hq)** mouse carries a proviral insertion that downregulates *Aif* by ~80% and develops severe mitochondrial complex I deficiency (40–50% reduction), degenerating mitochondria, and progressive multifocal neurodegeneration. Notably, *"Neurodegeneration was not restricted to the cerebellum but progressively affected thalamic, striatal, and cortical regions as well"* ([PMID: 17805014](https://pubmed.ncbi.nlm.nih.gov/17805014/)), tracking along somatosensory-motor pathways relevant to the human disease.

Hq mice also display retinal photoreceptor degeneration that is rescued by the redox compound **methylene blue** ([PMID: 30300862](https://pubmed.ncbi.nlm.nih.gov/30300862/)), and heightened susceptibility to complex I neurotoxins (MPTP) that is reversible by the antioxidant **tempol** ([PMID: 20695011](https://pubmed.ncbi.nlm.nih.gov/20695011/)), illustrating a gene–environment interaction and candidate redox-protective strategies. Cross-breeding with P301L tau mice aggravates tau pathology and neurodegeneration, linking AIF deficiency to broader neurodegenerative processes ([PMID: 19942317](https://pubmed.ncbi.nlm.nih.gov/19942317/)). Mouse ortholog: *Aifm1* (NCBI Gene **26926**); human *AIFM1* (NCBI Gene **9131**).

### Finding 7 — CMTX4 hearing loss reflects auditory neuropathy; *AIFM1* causes auditory neuropathy spectrum disorder (DFNX5)

The sensorineural deafness in CMTX4 is best characterized as **auditory neuropathy**. Auditory neuropathy spectrum disorder (ANSD) *"represents a variety of sensorineural deafness conditions characterized by abnormal inner hair cells and/or auditory neurons"* with preserved outer hair cell function, accounting for up to ~15% of hearing-impaired patients; *AIFM1* variants have been identified in ANSD families and sporadic cases ([PMID: 36751702](https://pubmed.ncbi.nlm.nih.gov/36751702/)). *AIFM1*-associated X-linked deafness is catalogued as **DFNX5/AUNX1 (OMIM 300614)**. This explains why the hearing loss in CMTX4 is a neural (retrocochlear) phenomenon consistent with the broader axonopathy, and it has direct implications for choosing cochlear implantation over conventional amplification in some patients.

**Suggested UBERON/CL terms:** UBERON:0001844 (cochlea), UBERON:0002227 (spiral ganglion), CL:0000601 (cochlear inner hair cell), CL:0000103 (bipolar neuron/auditory neuron).

### Finding 8 — CMTX4 is an ultra-rare X-linked recessive subtype within CMT

CMT overall *"are the most frequent genetically-determined peripheral neuropathies, with a global prevalence between 4.7 and 36/100,000"* ([PMID: 20929675](https://pubmed.ncbi.nlm.nih.gov/20929675/)); e.g., population-based prevalence *"in Cyprus… is estimated to be 16 per 100,000"* ([PMID: 20571287](https://pubmed.ncbi.nlm.nih.gov/20571287/)). The most common subtypes are CMT1A (PMP22 duplication) and CMTX1 (GJB1/Cx32). **CMTX4/*AIFM1* is not among the frequent genotypes** and has been described only in a small number of families worldwide (the original US family, plus Irish, Han-Chinese, Italian, and other kindreds; [PMID: 3856385](https://pubmed.ncbi.nlm.nih.gov/3856385/), [PMID: 31523922](https://pubmed.ncbi.nlm.nih.gov/31523922/), [PMID: 37173762](https://pubmed.ncbi.nlm.nih.gov/37173762/), [PMID: 30031633](https://pubmed.ncbi.nlm.nih.gov/30031633/), [PMID: 26173962](https://pubmed.ncbi.nlm.nih.gov/26173962/)).

No formal prevalence/incidence figure exists for CMTX4 specifically; Orphanet lists it as a very rare disorder. Inheritance is X-linked recessive, with affected hemizygous males and typically asymptomatic obligate carrier females.

### Finding 9 — Diagnosis relies on nerve conduction studies (axonal pattern) plus molecular confirmation of *AIFM1*

CMTX4 is an **axonal (CMT2-type)** neuropathy: nerve conduction shows length-dependent large-fibre sensorimotor axonal neuropathy with normal-to-mildly reduced motor conduction velocity and markedly abnormal sensory responses ([PMID: 8666389](https://pubmed.ncbi.nlm.nih.gov/8666389/); [PMID: 31523922](https://pubmed.ncbi.nlm.nih.gov/31523922/)). Calf MRI reveals fatty infiltration/atrophy predominantly of the peroneal compartment. Nerve and muscle pathology in one Chinese family showed *"abnormal mitochondrial morphology and accumulation in axoplasm of nerve fiber and subsarcolemmal area of muscle. A hemizygous variant (c.513G>A, p.Met171Ile)… was classified as likely pathogenic according to the standards and guidelines of the American College of Medical Genetics and Genomics"* ([PMID: 30031633](https://pubmed.ncbi.nlm.nih.gov/30031633/)).

Molecular diagnosis is by NGS/exome or gene-panel testing. A comprehensive next-generation-sequencing approach is the practical diagnostic route for axonal CMT, where *"almost half of axonal CMT families had at least a possible diagnosis with the comprehensive NGS panel"* ([PMID: 32506583](https://pubmed.ncbi.nlm.nih.gov/32506583/)). Whole-exome/whole-genome sequencing identified variants across multiple CMTX4 families ([PMID: 23217327](https://pubmed.ncbi.nlm.nih.gov/23217327/); [PMID: 37173762](https://pubmed.ncbi.nlm.nih.gov/37173762/); [PMID: 31523922](https://pubmed.ncbi.nlm.nih.gov/31523922/)).

### Finding 10 — No disease-specific therapy; management is supportive/rehabilitative, with DBS effective for AIFM1-related tremor

*"At present, there is no drug therapy for Charcot-Marie-Tooth disease, and rehabilitation therapy and surgical procedures for skeletal deformities are the only available treatments"* ([PMID: 19539237](https://pubmed.ncbi.nlm.nih.gov/19539237/)). Care is delivered in a multidisciplinary setting involving neurologists, physiatrists, orthopedic surgeons, therapists, and orthotists ([PMID: 18334132](https://pubmed.ncbi.nlm.nih.gov/18334132/)). Experimental CMT approaches (ascorbic acid, curcumin, progesterone antagonists) target **demyelinating CMT1A**, not *AIFM1* axonal disease, and are not applicable here.

For AIFM1-related disabling tremor, *"Deep brain stimulation (DBS) of the ventral intermediate thalamic nucleus ameliorated contralateral tremor and improved their quality of life; this suggests the beneficial role for DBS in treatment-resistant tremor within AIFM1-related disorders"* ([PMID: 36907087](https://pubmed.ncbi.nlm.nih.gov/36907087/)). Hearing aids or cochlear implants address the sensorineural/auditory-neuropathy component.

**Suggested NCIT terms:** NCIT:C15275 (Physical Therapy), NCIT:C15329 (Rehabilitation Therapy), Orthotic Device, NCIT:C38013 (Deep Brain Stimulation), Cochlear Implant.

### Finding 11 — *AIFM1* disease is an allelic spectrum; carrier females can manifest via skewed X-inactivation

*AIFM1* variants cause a wide allelic spectrum spanning from the milder CMTX4/Cowchock phenotype to severe COXPD6 mitochondrial encephalomyopathy, DFNX5 auditory neuropathy, spondyloepimetaphyseal dysplasia with neurodegeneration ([PMID: 27102849](https://pubmed.ncbi.nlm.nih.gov/27102849/)), infantile motor-neuron/anterior-horn disease ([PMID: 26173962](https://pubmed.ncbi.nlm.nih.gov/26173962/); [PMID: 39601015](https://pubmed.ncbi.nlm.nih.gov/39601015/)), neonatal seizures ([PMID: 37644805](https://pubmed.ncbi.nlm.nih.gov/37644805/)), and cardiomyopathy. As one review states, *"Pathogenic variants in AIFM1 have been associated with a wide spectrum of disorders, spanning from CMT4X to mitochondrial encephalopathy"* ([PMID: 37644805](https://pubmed.ncbi.nlm.nih.gov/37644805/)).

Although X-linked recessive, a heterozygous female can manifest disease: *"Genetic testing identified a heterozygous AIFM1 variant, c.506C>T (p.Pro169Leu), with extremely skewed X-inactivation (98:2) in a female"* who developed infantile mitochondrial encephalomyopathy and cardiomyopathy ([PMID: 42329587](https://pubmed.ncbi.nlm.nih.gov/42329587/)). Intrafamilial variability is marked even for the same variant ([PMID: 39601015](https://pubmed.ncbi.nlm.nih.gov/39601015/); [PMID: 31523922](https://pubmed.ncbi.nlm.nih.gov/31523922/)).

### Finding 12 — Genetic counseling and prevention framework (X-linked recessive)

CMTX4 follows X-linked recessive transmission: carrier mothers pass the *AIFM1* variant to 50% of offspring; sons inheriting it are affected, daughters are carriers; affected males transmit to all daughters (obligate carriers) and to no sons. Identification of the familial variant enables downstream prevention — *"The results of our study may also be useful for genetic counseling, embryo screening of in vitro fertilization embryos, and prenatal genetic diagnosis"* ([PMID: 37173762](https://pubmed.ncbi.nlm.nih.gov/37173762/)). Counseling must account for manifesting female carriers with skewed X-inactivation ([PMID: 42329587](https://pubmed.ncbi.nlm.nih.gov/42329587/)). No population-level primary prevention exists; secondary prevention is cascade testing plus early audiologic and neurophysiologic surveillance of at-risk relatives.

---

## Section-by-Section Knowledge Base Content

### 1. Disease Information
CMTX4 is an X-linked recessive axonal Charcot-Marie-Tooth neuropathy defined by peripheral sensorimotor neuropathy combined with sensorineural (auditory-neuropathy) deafness and, frequently, cognitive impairment and cerebellar/pyramidal features. **Identifiers:** OMIM 310490 (phenotype), gene *AIFM1* OMIM 300169; Orphanet lists it as a rare CMT/Cowchock entity; MeSH maps to Charcot-Marie-Tooth Disease (D002607) with X-linked qualifiers; ICD-10 G60.0 (hereditary motor and sensory neuropathy). **Synonyms:** Cowchock syndrome; CMT4X; X-linked motor-sensory neuropathy type II with deafness and mental retardation. Information is derived from **aggregated disease-level resources and small family case series**, not EHR/individual-patient registries.

### 2. Etiology
**Causal factor:** monogenic — hemizygous missense variants in *AIFM1* (Xq26.1). **Genetic risk:** being hemizygous male for a pathogenic *AIFM1* allele confers disease; female carriers are usually unaffected but may manifest with skewed X-inactivation. No environmental risk factors are established for the human disease, though model data show AIF deficiency **sensitizes neurons to environmental complex I toxins (MPTP)** — a demonstrated gene–environment interaction ([PMID: 20695011](https://pubmed.ncbi.nlm.nih.gov/20695011/)). No protective alleles or environmental protective factors are documented. Consanguinity is not required (X-linked). No infectious etiology.

### 3. Phenotypes
| Phenotype | Type | HPO | Onset | Severity/Progression | Frequency |
|---|---|---|---|---|---|
| Distal weakness & atrophy | Physical/motor | HP:0007107 / HP:0003693 | Infancy–childhood | Severe, progressive | Core (near-universal in males) |
| Distal sensory loss | Sensory sign | HP:0002936 | Childhood | Progressive | High |
| Areflexia | Clinical sign | HP:0001284 | Early | Stable/progressive | High |
| Pes cavus / hammer toes | Skeletal | HP:0001761 / HP:0001765 | Infancy | Progressive | High |
| Sensorineural (auditory neuropathy) deafness | Lab/clinical | HP:0000407 | Variable | Variable/progressive | 5/7 in original family (~70%) |
| Cognitive impairment | Behavioral/cognitive | HP:0001256 | Childhood | Stable | 3/5 in original family (~60%) |
| Cerebellar ataxia | Clinical sign | HP:0001251 | Variable | Progressive | Frequent in expanded families |
| Pyramidal signs | Clinical sign | HP:0007256 | Variable | Progressive | Frequent |
| Color-vision deficiency | Sensory | HP:0000551 | — | Stable | 3/7 (Irish family) |
| Tremor | Clinical sign | HP:0001337 | Variable | Progressive | Subset |

Quality-of-life impact is dominated by loss of ambulation (foot deformity, distal weakness), communication difficulty (deafness), and, in a subset, tremor-related disability responsive to DBS ([PMID: 36907087](https://pubmed.ncbi.nlm.nih.gov/36907087/)).

### 4. Genetic/Molecular Information
**Causal gene:** *AIFM1* (HGNC:8768; Xq26.1; OMIM 300169). **Reported pathogenic/likely-pathogenic variants (all missense, germline, hemizygous):** c.1478A>T p.Glu493Val (founding Cowchock variant, [PMID: 23217327](https://pubmed.ncbi.nlm.nih.gov/23217327/)); c.1006G>A p.Glu336Lys ([PMID: 41957773](https://pubmed.ncbi.nlm.nih.gov/41957773/)); c.513G>A p.Met171Ile (ACMG likely pathogenic, [PMID: 30031633](https://pubmed.ncbi.nlm.nih.gov/30031633/)); p.Asp237Gly (SEMD-neurodegeneration, [PMID: 27102849](https://pubmed.ncbi.nlm.nih.gov/27102849/)); c.506C>T p.Pro169Leu (manifesting female, [PMID: 42329587](https://pubmed.ncbi.nlm.nih.gov/42329587/)); c.5T>C p.Phe2Ser (neonatal, targeting sequence, [PMID: 37644805](https://pubmed.ncbi.nlm.nih.gov/37644805/)). **Variant class:** predominantly missense (± one intronic/splice variant reported in the broader spectrum). **Functional consequence:** protein destabilization with altered redox properties and weakened AIF:CHCHD4 interaction — a partial loss of function with a pro-apoptotic gain of harmful activity. Allele frequencies in gnomAD are effectively absent/ultra-rare, consistent with high pathogenicity. No recurrent modifier genes are established, though CHCHD4/MIA40 abundance is mechanistically downstream. Epigenetic contributions to disease are limited to **skewed X-inactivation** modulating female expression.

### 5. Environmental Information
No environmental, lifestyle, or infectious factors cause CMTX4 in humans. The only relevant environmental interaction is experimental: AIF-deficient neurons are hypersensitive to the mitochondrial complex I neurotoxin MPTP, reversible by the antioxidant tempol ([PMID: 20695011](https://pubmed.ncbi.nlm.nih.gov/20695011/)).

### 6. Mechanism / Pathophysiology
**Causal chain:** *AIFM1* missense variant → reduced AIF protein stability (mRNA preserved) → compromised FAD retention and altered NAD(H) redox switch → weakened charge-transfer complex and loss of the AIF:CHCHD4/MIA40 interaction → impaired mitochondrial intermembrane-space import and defective assembly of respiratory complex I and supercomplexes → decreased basal respiration, reduced mitochondrial content, and a shift toward apoptotic cell death → length-dependent axonal degeneration of peripheral sensory/motor neurons, degeneration of auditory neurons, and central neuronal loss (cerebellum, thalamus, striatum, cortex) → clinical neuropathy, deafness, ataxia, and cognitive impairment. Upstream = AIF destabilization/redox defect; downstream = complex I/supercomplex failure and neurodegeneration ([PMID: 23217327](https://pubmed.ncbi.nlm.nih.gov/23217327/); [PMID: 41957773](https://pubmed.ncbi.nlm.nih.gov/41957773/); [PMID: 32769219](https://pubmed.ncbi.nlm.nih.gov/32769219/)). **Cell types:** peripheral sensory/motor neurons and their long axons, cochlear/auditory neurons, cerebellar neurons; Schwann cells are relatively spared (axonal, not demyelinating). **Subcellular compartment:** mitochondrion / intermembrane space (GO:0005758), inner membrane (GO:0005743). **Biochemical defect:** FAD/NAD(H) oxidoreductase dysfunction.

### 7. Anatomical Structures Affected
**Primary:** peripheral nerves (UBERON:0001021), especially long, distal, large-fibre motor and sensory axons of the lower limbs (bilateral, length-dependent, symmetric). **Secondary/associated:** cochlea and auditory pathway (UBERON:0001844), cerebellum (UBERON:0002037), corticospinal/pyramidal tracts, and cerebral cortex (cognitive involvement). **Body systems:** peripheral and central nervous system; musculoskeletal (secondary foot deformities). **Cell level:** neurons (CL:0000540) and their axons; auditory neurons/inner hair cells. **Subcellular:** mitochondria (GO:0005739).

### 8. Temporal Development
**Onset:** typically **infancy to childhood** in the classic form, but the expanded spectrum spans 18 months to ~39 years ([PMID: 31523922](https://pubmed.ncbi.nlm.nih.gov/31523922/)). **Onset pattern:** insidious, chronic. **Course:** slowly progressive, chronic and lifelong; no relapsing-remitting pattern and no spontaneous remission. Progression rate is variable, ranging from mild neuropathy to wheelchair dependence and respiratory involvement in severe intrafamilial cases ([PMID: 39601015](https://pubmed.ncbi.nlm.nih.gov/39601015/)).

### 9. Inheritance and Population
**Inheritance:** X-linked recessive; affected hemizygous males, carrier females usually asymptomatic but occasionally manifesting via skewed X-inactivation ([PMID: 42329587](https://pubmed.ncbi.nlm.nih.gov/42329587/)). **Penetrance:** high in hemizygous males; **expressivity:** highly variable, even within families. No genetic anticipation (not a repeat-expansion disorder). **Epidemiology:** no CMTX4-specific prevalence figure; it is an ultra-rare subtype within CMT (overall CMT prevalence 4.7–36/100,000; [PMID: 20929675](https://pubmed.ncbi.nlm.nih.gov/20929675/)). **Sex ratio:** strongly male-predominant. Families reported are geographically diverse (US, Ireland, China, Italy) with no established founder effect.

### 10. Diagnostics
**Electrophysiology:** nerve conduction studies show axonal sensorimotor neuropathy (large-fibre, length-dependent) with markedly abnormal sensory responses; audiology/ABR shows auditory-neuropathy pattern. **Imaging:** calf MRI shows fatty infiltration of the peroneal compartment ([PMID: 30031633](https://pubmed.ncbi.nlm.nih.gov/30031633/)); brain MRI may be normal or show mild cerebellar atrophy. **Pathology:** nerve/muscle biopsy shows abnormal mitochondrial morphology and accumulation ([PMID: 30031633](https://pubmed.ncbi.nlm.nih.gov/30031633/)). **Genetic testing:** exome/genome sequencing or a comprehensive inherited-neuropathy NGS panel is the definitive route ([PMID: 32506583](https://pubmed.ncbi.nlm.nih.gov/32506583/)); single-gene *AIFM1* testing confirms known familial variants. **Differential diagnosis:** CMTX1 (GJB1), other CMT2 subtypes, mitochondrial neuropathies, and syndromic deafness-neuropathy conditions; the combination of axonal neuropathy + auditory neuropathy + ataxia + X-linked male-limited inheritance is the diagnostic signature.

### 11. Outcome / Prognosis
CMTX4 is a chronic, progressive but generally non-fatal neurodegenerative condition; life expectancy is not markedly reduced in the classic form, though the severe end of the *AIFM1* spectrum (infantile encephalomyopathy, respiratory failure) carries high mortality. **Morbidity** is driven by progressive disability from distal weakness, sensory loss, hearing impairment, and ataxia; some patients progress to wheelchair dependence and respiratory compromise ([PMID: 39601015](https://pubmed.ncbi.nlm.nih.gov/39601015/)). No validated CMTX4-specific prognostic biomarkers exist; disease severity correlates broadly with the specific *AIFM1* variant and, in females, with the degree of X-inactivation skewing.

### 12. Treatment
No disease-specific/curative therapy exists ([PMID: 19539237](https://pubmed.ncbi.nlm.nih.gov/19539237/)). **Supportive/rehabilitative:** ankle-foot orthoses, physical and occupational therapy, orthopedic surgery for pes cavus/hammer toes, mobility aids. **Sensory:** hearing aids or cochlear implants for the auditory-neuropathy component. **Tremor:** DBS of the ventral intermediate thalamic nucleus for treatment-resistant AIFM1-related tremor ([PMID: 36907087](https://pubmed.ncbi.nlm.nih.gov/36907087/)). Established CMT1A experimental drugs (ascorbic acid, curcumin, antiprogesterone) are mechanistically inapplicable to axonal *AIFM1* disease. Redox-protective compounds (methylene blue, tempol) are promising only at the preclinical/model stage ([PMID: 30300862](https://pubmed.ncbi.nlm.nih.gov/30300862/); [PMID: 20695011](https://pubmed.ncbi.nlm.nih.gov/20695011/)).

### 13. Prevention
No primary prevention. **Secondary/tertiary prevention:** cascade genetic testing of at-risk relatives, early audiologic and neurophysiologic surveillance, and proactive management of foot deformities and hearing loss. **Reproductive prevention:** genetic counseling, preimplantation genetic testing of IVF embryos, and prenatal diagnosis once the familial *AIFM1* variant is known ([PMID: 37173762](https://pubmed.ncbi.nlm.nih.gov/37173762/)), with counseling that accounts for potential manifesting female carriers.

### 14. Other Species / Natural Disease
The mouse ortholog *Aifm1* (NCBI Gene 26926) underlies the naturally arising **Harlequin (Hq)** mouse mutant, the principal comparative model. No naturally occurring companion-animal or wildlife equivalent of CMTX4 is catalogued in OMIA at the level documented here. AIF is evolutionarily conserved (a FAD/NADH oxidoreductase with orthologs across metazoans), supporting cross-species mechanistic conservation. No zoonotic relevance.

### 15. Model Organisms
The **Harlequin mouse** (proviral insertion reducing *Aif* ~80%) is a spontaneous mammalian model recapitulating complex I deficiency, cerebellar and multifocal neurodegeneration, retinal degeneration, and neurotoxin susceptibility ([PMID: 17805014](https://pubmed.ncbi.nlm.nih.gov/17805014/); [PMID: 19280713](https://pubmed.ncbi.nlm.nih.gov/19280713/); [PMID: 30300862](https://pubmed.ncbi.nlm.nih.gov/30300862/); [PMID: 20695011](https://pubmed.ncbi.nlm.nih.gov/20695011/)). Patient-derived **fibroblasts** provide a cellular model demonstrating AIF destabilization, CHCHD4 loss, and impaired respiratory-supercomplex assembly ([PMID: 41957773](https://pubmed.ncbi.nlm.nih.gov/41957773/)). **Limitations:** the Hq mouse is a knockdown (loss-of-expression) rather than a knock-in of specific human missense variants, so it models AIF deficiency more than the redox-shift mechanism of CMTX4; it also emphasizes central/retinal phenotypes over the human peripheral-neuropathy-plus-deafness presentation.

---

## Mechanistic Model / Interpretation

```
   AIFM1 missense variant (e.g., p.Glu493Val, p.Glu336Lys, p.Met171Ile)
                              |
                              v
      Reduced AIF protein stability (mRNA preserved)
      Compromised FAD retention; impaired NADH affinity
                              |
                              v
   Destabilized FADH2-NAD charge-transfer complex  <-- redox switch broken
                              |
              +---------------+----------------+
              v                                v
  Weakened AIF:CHCHD4/MIA40 interaction    Shift toward pro-apoptotic state
  (impaired IMS protein import)            (increased caspase-independent
              |                             cell death)
              v                                |
  Defective complex I / respiratory           |
  supercomplex assembly; low mito content     |
              |                                |
              +---------------+----------------+
                              v
       Mitochondrial dysfunction in long-axon neurons,
       auditory neurons, cerebellar/central neurons
                              |
                              v
   Length-dependent axonal neuropathy + auditory-neuropathy deafness
   + cerebellar ataxia + pyramidal signs + cognitive impairment + tremor
```

The unifying theme is that AIF is a **redox-controlled hub** linking mitochondrial biogenesis (complex I assembly via CHCHD4 import) to programmed cell death. CMTX4 variants tip this balance: they are severe enough to destabilize the protein and impair its import/assembly function, yet (in the classic phenotype) mild enough to avoid the catastrophic OXPHOS collapse that characterizes the infantile-encephalopathy end of the *AIFM1* allelic spectrum. Neuronal vulnerability is greatest in cells with the highest metabolic and axonal-transport demands — long peripheral axons, auditory neurons, and cerebellar circuits — explaining the characteristic clinical triad. Variant severity plus (in females) X-inactivation skewing accounts for the striking phenotypic range from mild neuropathy to lethal encephalomyopathy.

---

## Evidence Base

| PMID | Title (abbrev.) | Role in this report |
|---|---|---|
| [23217327](https://pubmed.ncbi.nlm.nih.gov/23217327/) | *Cowchock syndrome is associated with a mutation in AIF* | Founding causal-gene identification; redox mechanism without OXPHOS failure |
| [8666389](https://pubmed.ncbi.nlm.nih.gov/8666389/) | *Locus maps to Xq24-q26* | Original linkage mapping of the CMTX4 locus |
| [3856385](https://pubmed.ncbi.nlm.nih.gov/3856385/) | *X-linked MSN type-II with deafness and MR* | Original clinical description of core phenotype |
| [31523922](https://pubmed.ncbi.nlm.nih.gov/31523922/) | *Clinical spectrum in an Irish family* | Expanded phenotype (ataxia, pyramidal, color blindness) |
| [37173762](https://pubmed.ncbi.nlm.nih.gov/37173762/) | *Novel AIFM1 variant, Han-Chinese family* | Diagnostics + reproductive prevention utility |
| [30031633](https://pubmed.ncbi.nlm.nih.gov/30031633/) | *Novel AIFM1 mutation, Chinese family (CMT4X)* | Biopsy mitochondrial pathology, calf MRI, ACMG classification |
| [41957773](https://pubmed.ncbi.nlm.nih.gov/41957773/) | *E336K mutation, mitochondrial dysfunction* | Refined mechanism: AIF destabilization, CHCHD4 loss, supercomplex defect |
| [32769219](https://pubmed.ncbi.nlm.nih.gov/32769219/) | *AIF redox-controlled gear boxes* | AIF role in CHCHD4/MIA40 import and complex I assembly |
| [20868295](https://pubmed.ncbi.nlm.nih.gov/20868295/) | *AIF: structure, function, redox regulation* | AIF dual redox/respiratory-assembly role |
| [19447115](https://pubmed.ncbi.nlm.nih.gov/19447115/) | *Redox-linked conformational dynamics in AIF* | Structural basis of the redox switch perturbed by mutations |
| [26535916](https://pubmed.ncbi.nlm.nih.gov/26535916/) | *Adenylate moiety and NAD(H) binding to AIF* | Pathological-equivalent mutation effects on NAD(H) binding |
| [17805014](https://pubmed.ncbi.nlm.nih.gov/17805014/) | *AIF deficiency, mitochondrial degeneration* | Harlequin mouse neurodegeneration pattern |
| [19280713](https://pubmed.ncbi.nlm.nih.gov/19280713/) | *ROS regulation in AIF-/complex I-depleted mito* | Hq complex I deficiency quantification |
| [30300862](https://pubmed.ncbi.nlm.nih.gov/30300862/) | *AIF deficiency, retinal degeneration, methylene blue* | Model retinal phenotype; candidate redox therapy |
| [20695011](https://pubmed.ncbi.nlm.nih.gov/20695011/) | *AIF deficiency sensitizes DA neurons to neurotoxins* | Gene–environment interaction; tempol rescue |
| [36907087](https://pubmed.ncbi.nlm.nih.gov/36907087/) | *DBS for AIFM1-related tremor* | Effective symptomatic intervention for tremor |
| [19539237](https://pubmed.ncbi.nlm.nih.gov/19539237/) | *Diagnosis, natural history, management of CMT* | No drug therapy; supportive-care standard |
| [18334132](https://pubmed.ncbi.nlm.nih.gov/18334132/) | *Charcot-Marie-Tooth disease* | Multidisciplinary management framework |
| [36751702](https://pubmed.ncbi.nlm.nih.gov/36751702/) | *Auditory neuropathy spectrum disorder* | Links AIFM1 to ANSD (DFNX5) mechanism |
| [20929675](https://pubmed.ncbi.nlm.nih.gov/20929675/) | *CMT: an update* | Overall CMT prevalence context |
| [20571287](https://pubmed.ncbi.nlm.nih.gov/20571287/) | *CMT in Cyprus* | Population-based CMT prevalence example |
| [32506583](https://pubmed.ncbi.nlm.nih.gov/32506583/) | *Diagnostic yield of NGS panels* | NGS/exome as diagnostic route for axonal CMT |
| [27102849](https://pubmed.ncbi.nlm.nih.gov/27102849/) | *SEMD with neurodegeneration, AIFM1* | Allelic spectrum (skeletal + neurodegeneration) |
| [26173962](https://pubmed.ncbi.nlm.nih.gov/26173962/) | *AIFM1 infantile motor neuron disease* | Allelic spectrum (motor neuron involvement) |
| [39601015](https://pubmed.ncbi.nlm.nih.gov/39601015/) | *Novel AIFM1 variant, siblings* | Intrafamilial variability; ataxia + auditory neuropathy |
| [37644805](https://pubmed.ncbi.nlm.nih.gov/37644805/) | *Neonatal-onset AIFM1 disorders* | Allelic spectrum; CMT4X-to-encephalopathy statement |
| [42329587](https://pubmed.ncbi.nlm.nih.gov/42329587/) | *Female child with heterozygous AIFM1 variant* | Manifesting female via skewed X-inactivation |

---

## Limitations and Knowledge Gaps

1. **No CMTX4-specific epidemiology.** Prevalence, incidence, sex-stratified age distribution, and geographic/founder patterns are unknown; the disease is described only in scattered small families, so all population statements are extrapolated from the broader CMT literature.
2. **Genotype–phenotype correlation is incomplete.** Why some *AIFM1* variants produce mild CMTX4 while others cause lethal encephalopathy is not fully resolved; systematic biophysical characterization exists for only a few variants (e.g., E493V, E336K).
3. **Human mechanistic data are limited** to a handful of patient fibroblast studies; the dominant animal model (Harlequin) is a knockdown, not a knock-in of human CMTX4 missense alleles, and emphasizes central/retinal over peripheral phenotypes.
4. **No natural-history study or validated outcome measures** specific to CMTX4; progression rates, disability trajectories, and prognostic biomarkers are anecdotal.
5. **No therapeutics targeting the AIF:CHCHD4 axis** have been tested in humans; redox-protective compounds are only preclinical.
6. **Female carrier risk quantification is poor** — the frequency of manifesting carriers and the X-inactivation thresholds for symptom emergence are undefined.

---

## Proposed Follow-up Experiments / Actions

1. **Establish a CMTX4/*AIFM1* patient registry** to define natural history, penetrance, sex ratio, and genotype–phenotype correlations, using standardized CMTNS and SARA scores plus audiometric/ABR endpoints.
2. **Generate knock-in mouse or iPSC-derived motor/sensory neuron models** carrying specific human CMTX4 variants (e.g., p.Glu493Val, p.Glu336Lys) to model the redox-shift mechanism rather than mere AIF deficiency, and to compare peripheral vs. central vulnerability.
3. **Systematic biophysical variant panel:** express and purify a series of reported *AIFM1* missense proteins to quantify FAD retention, NADH affinity, charge-transfer stability, and CHCHD4 binding, building a predictive severity scale for VUS classification.
4. **Test AIF:CHCHD4-restoring or redox-stabilizing therapeutics** (e.g., methylene blue, tempol, FAD-supporting agents, CHCHD4 overexpression) in patient fibroblasts and neuron models for rescue of respiration/supercomplex assembly.
5. **Characterize the auditory-neuropathy phenotype prospectively** to define optimal timing and outcomes of cochlear implantation in CMTX4 patients.
6. **Quantify female-carrier risk** by correlating X-inactivation ratios with clinical status across carrier cohorts, to refine genetic counseling.
7. **Evaluate DBS more broadly** for AIFM1-related tremor with prospective multi-patient outcome data, given the encouraging case series.

---

*Evidence source types: human clinical (family case series, patient fibroblasts), model organism (Harlequin mouse), in vitro biochemistry/structural biology, and computational variant prediction. This report is compiled from disease-level resources and primary literature; it does not derive from individual EHR data.*


## Artifacts

- [OpenScientist final report](Charcot-Marie-Tooth_Disease_X-linked_Recessive_4-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Charcot-Marie-Tooth_Disease_X-linked_Recessive_4-deep-research-openscientist_artifacts/final_report.pdf)