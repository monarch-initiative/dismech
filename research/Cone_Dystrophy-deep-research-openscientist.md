---
title: Cone dystrophy pathophysiology for dismech curation
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-27T20:09:06.274088'
end_time: '2026-08-27T20:30:15.163312'
duration_seconds: 1268.89
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Cone Dystrophy
  mondo_id: MONDO:0000455
  category: Inherited retinal dystrophy / progressive cone photoreceptor degeneration
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 10
    use_hypotheses: true
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 5400
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 36
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Cone_Dystrophy-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Cone_Dystrophy-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cone Dystrophy
- **MONDO ID:** MONDO:0000455 (if available)
- **Category:** Inherited retinal dystrophy / progressive cone photoreceptor degeneration

## Research Objectives

Please provide a comprehensive research report on **Cone Dystrophy** covering all of the
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

# Cone Dystrophy: A Comprehensive Disease Characteristics Report

**Disease:** Cone Dystrophy (and Cone-Rod Dystrophy) · **MONDO:** MONDO:0000455 · **Category:** Inherited retinal dystrophy / progressive cone photoreceptor degeneration

**Identifiers:** MONDO:0000455 · MeSH: Cone-Rod Dystrophies · OMIM (representative): CDSRR 610356; multiple CORD/COD phenotype numbers · ICD-11: hereditary retinal dystrophy range (9B70.x) · Orphanet: cone/cone-rod dystrophy entries

---

## Summary

Cone dystrophy (CD) is a genetically heterogeneous inherited retinal dystrophy (IRD) defined by primary dysfunction and progressive degeneration of the cone photoreceptors that populate the fovea and macula. Clinically, patients present with decreased central visual acuity, dyschromatopsia (color-vision loss), photophobia/hemeralopia (day-blindness and glare intolerance), and — in early-onset forms — nystagmus. When rod photoreceptors are secondarily involved, the disorder is termed cone-rod dystrophy (CORD), which adds nyctalopia (night blindness) and peripheral field loss to the phenotype. Estimated prevalence is approximately **1 in 30,000–40,000** for progressive cone dystrophy, making cone/cone-rod dystrophy one of the more common IRDs after retinitis pigmentosa and Stargardt disease.

Mechanistically, a large fraction of cone dystrophies converge on dysregulation of the **cGMP/Ca²⁺ phototransduction node** in cone outer segments. Dominant gain-of-function mutations in *GUCA1A* (GCAP1) and *GUCY2D* (retinal guanylate cyclase, RetGC-1) cause aberrantly sustained cGMP synthesis; recessive mutations in *PDE6C/PDE6H* (cGMP phosphodiesterase) and *CNGA3/CNGB3* (cone CNG channel) disrupt the same pathway. Excess cGMP over-activates cyclic nucleotide-gated channels, producing Na⁺/Ca²⁺ influx and Ca²⁺ overload that triggers a downstream **calpain/PARP cell-death cascade** — a genotype-agnostic execution mechanism that is an attractive neuroprotective drug target. Other forms act through ciliary/structural trafficking defects (*RPGR*, *RPGRIP1*, *CDHR1*, *CEP290*), visual-cycle/RPE dysfunction (*ABCA4*), transcriptional dysregulation (*CRX*), or ion-channel modification (*KCNV2*, which produces the pathognomonic "supernormal rod" ERG of CDSRR).

Diagnosis rests on a **photopic-selective ERG signature** — reduced/extinguished light-adapted single-flash and 30-Hz flicker responses with relatively preserved scotopic (rod) responses — combined with SD-OCT (ellipsoid-zone/outer-retinal loss), fundus autofluorescence (central or bull's-eye maculopathy), and gene-panel/exome sequencing. No approved cure exists; management is largely supportive (tinted/edge-filter lenses, low-vision aids, refractive correction, genetic counseling). The most advanced therapeutic frontier is **AAV-mediated gene supplementation for CNGA3/CNGB3 achromatopsia**, which is safe and produces modest but statistically significant functional gains (pooled +2.65 ETDRS letters), with greater benefit for *CNGA3* and when treatment occurs in childhood. Accurate early molecular diagnosis and genetic counseling are therefore the pivotal intervention levers.

---

## Key Findings

### 1. Epidemiology: prevalence ~1:14,000–1:40,000

Cone dystrophy and cone-rod dystrophy rank among the more common inherited retinal diseases. A nationwide Israeli IRD study (n=9,396 diagnosed individuals) found cone-rod dystrophy prevalence of approximately **1:14,000**, the second most common IRD after retinitis pigmentosa (~1:2,400), with Stargardt disease at ~1:16,000 and all IRDs combined at 1:1,043 ([PMID: 38753338](https://pubmed.ncbi.nlm.nih.gov/38753338/)). The GeneReviews-level estimate for progressive cone dystrophy specifically is **1 in 30,000–40,000** ([PMID: 40736814](https://pubmed.ncbi.nlm.nih.gov/40736814/)).

A notable feature is the comparatively **low genetic diagnostic yield** for cone/cone-rod dystrophy relative to other IRD subphenotypes. In a Finnish cohort, "the lowest rates of causative variant identification were observed in cone or cone-rod dystrophy and macular dystrophy" ([PMID: 40571344](https://pubmed.ncbi.nlm.nih.gov/40571344/)), reflecting the extensive genetic heterogeneity and the existence of causative variants (e.g., in the repetitive *RPGR-ORF15* region) that are difficult to detect with standard short-read sequencing.

### 2. Core pathophysiology: dysregulated cGMP/Ca²⁺ phototransduction

The unifying molecular theme across many cone dystrophies is disruption of the cGMP/Ca²⁺ second-messenger cycle in cone photoreceptors. In dominant disease, **GCAP1 (GUCA1A)** mutations in the EF-hand Ca²⁺-binding motifs (e.g., L151F in EF4, Y99C, E111A) reduce Ca²⁺ affinity so that GCAP1 fails to switch off retinal guanylate cyclase (RetGC-1/GUCY2D) at the high Ca²⁺ concentrations found in dark-adapted photoreceptors. Enzymatic work showed that "GCAP1-L151F stimulation of photoreceptor guanylate cyclase was not completely inhibited at high physiological [Ca²⁺], consistent with a lowered affinity for Ca²⁺-binding to EF4" ([PMID: 15790869](https://pubmed.ncbi.nlm.nih.gov/15790869/)).

Analogously, **GUCY2D** mutations at the dimerization domain (R838C/R838S; CORD6) act as dominant gain-of-function alleles: the R838C substitution "increases the apparent affinity of RetGC-1 for GCAP-1 and alters the Ca²⁺ sensitivity of the GCAP-1 response, allowing the mutant to be stimulated by GCAP-1 at higher Ca²⁺ concentrations than wild type" ([PMID: 10430891](https://pubmed.ncbi.nlm.nih.gov/10430891/)). Both mechanisms produce persistent cyclase stimulation and cGMP overproduction. Recessive *PDE6C/PDE6H* (which degrade cGMP) and *CNGA3/CNGB3* (the cone CNG channel) disrupt the same node from the opposite direction. Elevated cGMP and consequent Ca²⁺ influx is cytotoxic, driving cone (then rod) degeneration.

### 3. Diagnostic signature: photopic-selective ERG deficit

The hallmark electrophysiologic finding is a **cone-selective (photopic) ERG deficit with preserved rod (scotopic) responses**. Genetically confirmed cone dystrophy cases show "severe cone dysfunction, characterized by markedly reduced light-adapted single-flash responses and near-extinguished 30 Hz flicker responses, with relatively preserved rod-mediated scotopic responses" ([PMID: 42525358](https://pubmed.ncbi.nlm.nih.gov/42525358/)). SD-OCT shows foveal ellipsoid-zone attenuation/loss with relative RPE preservation early in disease, and FAF shows central or bull's-eye abnormality.

A special case is **KCNV2/CDSRR**, which shows a pathognomonic delayed "supernormal" rod b-wave with a squared a-wave: "the ERG showed a delayed and supernormal b-wave with a 'squaring (trough-flattened)' a-wave in the DA-30 ERG, and CDSRR was diagnosed" ([PMID: 38630375](https://pubmed.ncbi.nlm.nih.gov/38630375/)).

### 4. Natural history and prognosis: progressive central vision loss; EZ length as an early biomarker

Cone and cone-rod dystrophies follow a chronic, progressive course centered on the macula. In an RPGR cohort (n=50; 357 microperimetry assessments), cone-rod dystrophy central sensitivity declined faster than rod-cone disease: **10.8%/yr (MS16)** and 14.9%/yr (MS4) in CORD versus 5.1% and 4.1%/yr in rod-cone (P=.02 and P<.001), with median survival age to total central sensitivity loss of 25.1 years (CORD) vs 33.1 years (rod-cone) ([PMID: 41237986](https://pubmed.ncbi.nlm.nih.gov/41237986/)).

Structural biomarkers precede functional decline. In autosomal recessive *PROM1* IRD (n=6, median 11.8-year follow-up), "best-corrected visual acuity (BCVA) was maintained until a steep decline around 15 years of age. This was preceded by contraction of the subfoveal ellipsoid zone length (EZL), measured on OCT" ([PMID: 40494823](https://pubmed.ncbi.nlm.nih.gov/40494823/)). Disease is lifelong/chronic and legally blinding but not directly life-limiting; onset in most progressive cone dystrophies is in the first-to-third decade.

### 5. RPGR-ORF15 glutamylation defect drives X-linked cone/cone-rod dystrophy

X-linked cone dystrophy caused by *RPGR* involves a post-translational modification defect. **TTLL5 glutamylates RPGR-ORF15** in its Glu-Gly-rich repeat region; loss of this modification causes photoreceptor degeneration. The "Ttll5 mutant mouse develops slow photoreceptor degeneration with early mislocalization of cone opsins, features resembling those of Rpgr-null mice" ([PMID: 27162334](https://pubmed.ncbi.nlm.nih.gov/27162334/)). Distal truncating *RPGR-ORF15* variants that impair glutamylation associate with a cone-dominated phenotype: "impaired glutamylation caused by distal truncating variants in RPGR ORF15 and its association with the cone-dominated phenotype have provided the first molecular evidence of a genotype-phenotype correlation" ([PMID: 41481301](https://pubmed.ncbi.nlm.nih.gov/41481301/)).

### 6. Treatment landscape: no approved cure; AAV gene supplementation and CRISPR

No approved pharmacologic cure exists. Management is supportive (tinted/edge-filter glasses and photochromic lenses for photophobia, refractive correction, low-vision aids, UV protection, genetic counseling). The most advanced therapeutic is AAV subretinal gene supplementation for recessive disease: "rAAV-mediated gene replacement therapy with different forms of the human red cone opsin promoter led to the restoration of cone function and day vision in two canine models of CNGB3 achromatopsia" ([PMID: 20378608](https://pubmed.ncbi.nlm.nih.gov/20378608/)).

For **autosomal-dominant gain-of-function GUCY2D CORD**, simple gene supplementation is insufficient; editing strategies are required. A dual-AAV "ablate-and-replace" (AAV-SaCas9) approach "preserved outer nuclear layer thickness for up to 24 weeks" in mice, whereas ablation alone did not restore function ([PMID: 42264060](https://pubmed.ncbi.nlm.nih.gov/42264060/)).

### 7. Downstream cell-death cascade: cGMP → CNG channel → Ca²⁺ → calpain/PARP

Elevated photoreceptor cGMP over-activates CNG channels, causing Na⁺/Ca²⁺ influx, membrane depolarization, and Ca²⁺ overload that triggers excessive activation of calpain proteases and poly(ADP-ribose) polymerase (PARP), executing photoreceptor death. This pathway is druggable: cGMP accumulation is "associated with the excessive activation of calpain and poly (ADP-ribose) polymerase (PARP). Inhibitors of calpain or PARP have shown promise in preventing photoreceptor cell death" ([PMID: 35327647](https://pubmed.ncbi.nlm.nih.gov/35327647/)).

Some CNG channel variants classically labeled loss-of-function are in fact gain-of-function: "CNGA3_R410W/CNGB3 and TAX4_R421W channels are spontaneously active without cGMP and induce cell death, suggesting cone degeneration triggered by spontaneous CNG channel activity as a possible cause of achromatopsia" ([PMID: 35233102](https://pubmed.ncbi.nlm.nih.gov/35233102/)).

### 8. Phenotype spectrum and symptom frequencies

In the KCNV2 Study Group cohort (n=117), mean age of onset was **3.9 years** and all patients were symptomatic before 12 years. **Decreased visual acuity was present in 100%**; reduced color vision in 78.6%; photophobia in 53.5%; nyctalopia in 43.6%; and nystagmus in 38.6% ([PMID: 33309813](https://pubmed.ncbi.nlm.nih.gov/33309813/)). A genetically confirmed achromatopsia cohort (n=21) found that all patients had color-vision difficulty, 20/21 (95.2%) had photosensitivity, 18/21 (85.7%) had congenital nystagmus, and one-third had nyctalopia ([PMID: 41867372](https://pubmed.ncbi.nlm.nih.gov/41867372/)).

| Symptom / Sign | KCNV2 cohort (n=117) | ACHM cohort (n=21) | HPO term |
|---|---|---|---|
| Decreased visual acuity | 100% | — | HP:0007663 (reduced visual acuity) |
| Reduced color vision / dyschromatopsia | 78.6% | 100% | HP:0000551 (abnormality of color vision) |
| Photophobia / photosensitivity | 53.5% | 95.2% | HP:0000613 |
| Nyctalopia (night blindness) | 43.6% | ~33% | HP:0000662 |
| Nystagmus | 38.6% | 85.7% | HP:0000639 |

### 9. Genetic heterogeneity, allelism, and syndromic differential diagnosis

The same gene often produces a phenotypic continuum. **CNGA3/CNGB3** cause both stationary achromatopsia and progressive cone/cone-rod dystrophy: "In rare cases, variants in CNGA3 are also associated with cone dystrophy, Leber's congenital amaurosis and oligo cone trichromacy" ([PMID: 25052312](https://pubmed.ncbi.nlm.nih.gov/25052312/)). *GUCY2D* underlies both recessive Leber congenital amaurosis and dominant CORD6.

Syndromic cone-rod dystrophy occurs in **Alström syndrome (ALMS1)**, where "age of symptom onset (i.e. nystagmus and photophobia) was at 6-9 months in all patients. These symptoms mostly mislead to the diagnosis of congenital achromatopsia (ACHM), Leber congenital amaurosis (LCA), isolated CORD or Bardet-Biedl syndrome" ([PMID: 29193673](https://pubmed.ncbi.nlm.nih.gov/29193673/)); as well as Bardet-Biedl syndrome (BBS1) and Spinocerebellar ataxia type 7. Non-syndromic causal genes span phototransduction (*GUCA1A, GUCY2D, PDE6C, PDE6H, CNGA3, CNGB3, GNAT2, KCNV2*), visual cycle/RPE (*ABCA4, RPGR*), transcription factors (*CRX*), and ciliary/structural/trafficking genes (*RPGRIP1, RIMS1, RAB28, C8orf37, POC1B, TTLL5, CDHR1, PROM1, RP1L1, CEP290, ADAM9, UNC119*).

### 10. Inheritance, founder effects, and consanguinity

Inheritance is **autosomal dominant** (*GUCA1A, GUCY2D/CORD6, some CRX, RIMS1, PROM1, AIPL1*), **autosomal recessive** (*CNGA3, CNGB3, PDE6C, PDE6H, ABCA4, RPGRIP1, CDHR1, C8orf37, POC1B, RAB28, ADAM9, CERKL*, etc.), or **X-linked** (*RPGR/COD1, CACNA1F*). Recessive forms are enriched by consanguinity and founder effects: "Two CNGA3 founder mutations underlie >50% of cases. These mutations lead to a high ACHM prevalence of ∼1:5000 among Arab-Muslims residing in Jerusalem" ([PMID: 25616768](https://pubmed.ncbi.nlm.nih.gov/25616768/)) — versus ~1:30,000 generally. In Newfoundland, "recurrent mutations p.T383fsX and p.L527R were due to a founder effect" ([PMID: 23362848](https://pubmed.ncbi.nlm.nih.gov/23362848/)). The CNGB3 founder allele is also famous in the Pingelapese ("island of the colorblind"). Dominant *GUCA1A/GUCY2D* disease shows variable expressivity and incomplete/age-dependent penetrance; X-linked *RPGR* shows variable manifestation in female carriers.

### 11. Diagnostic imaging pattern (OCT/FAF)

Full-field ERG shows reduced/extinguished photopic responses with preserved scotopic responses. In a genetically confirmed cohort (n=21), "most patients [had] a normal scotopic response and absent photopic response on electroretinogram, macular hyperfluorescence on fundus autofluorescence, and normal optical coherence tomography imaging" ([PMID: 41867372](https://pubmed.ncbi.nlm.nih.gov/41867372/)). Adult-onset CD/CRD frequently shows "a bull's eye pattern with foveal sparing, consistent with perifoveal photoreceptor loss on optical coherence tomography" ([PMID: 38091967](https://pubmed.ncbi.nlm.nih.gov/38091967/)). SD-OCT documents "loss of the ellipsoid zone line and collapse of the outer nuclear segment" with extinguished photopic ERG ([PMID: 39100576](https://pubmed.ncbi.nlm.nih.gov/39100576/)).

### 12. AAV gene therapy for CNGA3/CNGB3 achromatopsia

A genotype-aware systematic review/meta-analysis of 9 human AAV gene therapy studies found: "Pooled analysis showed modest, but statistically significant, improvement in best-corrected visual acuity, with a mean difference of **2.65 ETDRS letters**, and significant improvement in contrast sensitivity. Retinal sensitivity did not improve significantly, whereas color discrimination showed small but significant improvement" ([PMID: 42542214](https://pubmed.ncbi.nlm.nih.gov/42542214/)). The same analysis found an "approximate adverse-event probability of 29%, with events generally mild, transient, and manageable." Benefit is mainly in *CNGA3*, with a non-linear dose response. Achromatopsia is a leading gene-therapy target because "Up to 80% of the patients carry mutations in the genes CNGA3 and CNGB3 encoding the two subunits of the cone cyclic nucleotide-gated channel" ([PMID: 28095637](https://pubmed.ncbi.nlm.nih.gov/28095637/)). Treating in childhood may restore temporal resolution, with flicker-fusion approaching control levels only in a treated child ([PMID: 42602306](https://pubmed.ncbi.nlm.nih.gov/42602306/)).

### 13. Animal and cellular models

Naturally occurring and engineered models recapitulate the disease across species. "Naturally occurring mouse models with mutations in Cnga3 (cpfl5 mice) and Gnat2 (cpfl3 mice) were discovered at The Jackson Laboratory. A natural occurring canine model with CNGB3 mutations has also been found" ([PMID: 20238068](https://pubmed.ncbi.nlm.nih.gov/20238068/)). The **Cdhr1 knockout** recapitulates shortened/disorganised photoreceptor outer segments and is rescued by gene therapy: "AAV gene supplementation therapy delivered by subretinal injection can lead to long-term morphological, structural, functional and behavioural improvements in the Cdhr1 knockout mouse model... CDHR1 supplementation restored full-length photoreceptor outer segments" ([PMID: 42562233](https://pubmed.ncbi.nlm.nih.gov/42562233/)). The canine **RPGRIP1 cord1** model in English Springer Spaniels shows "insidious pathology with delayed-onset visual defects" ([PMID: 39428496](https://pubmed.ncbi.nlm.nih.gov/39428496/)) — a naturally occurring large-animal model. Patient-derived iPSC/retinal organoids (e.g., for KCNV2, CEP290) are also established.

### 14. KCNV2/CDSRR: a distinct subtype

Biallelic **KCNV2** (Kv8.2) variants cause "cone dystrophy with nyctalopia and supernormal rod responses" (CDSRR; OMIM 610356), autosomal recessive, "featuring pathognomonic findings on electroretinography (ERG)" ([PMID: 38630375](https://pubmed.ncbi.nlm.nih.gov/38630375/)). Kv8.2 co-assembles with Kv2.1 in photoreceptor inner segments; mouse Kcnv2 knockouts model the disorder.

### 15. Anatomical structures affected

Cone dystrophy primarily affects the **neural retina — cone photoreceptors of the fovea centralis** within the macula: "Fovea centralis, located at the center of the macula, is packed with cone photoreceptors and is responsible for central visual acuity" ([PMID: 36934831](https://pubmed.ncbi.nlm.nih.gov/36934831/)). SD-OCT localizes pathology to the outer retinal bands: in CORD (n=24 eyes), "A ring maculopathy appearance involving the fovea area was observed in all study eyes. There was an absence of interdigitation zone in the entire length of SD-OCT scan, including the foveal area, in all 24 study eyes" ([PMID: 23648999](https://pubmed.ncbi.nlm.nih.gov/23648999/)). The RPE becomes secondarily involved as disease advances; involvement is bilateral.

---

## Section-by-Section Synthesis (Research Template)

### 1. Disease Information
Cone dystrophy is an inherited retinal dystrophy of primary cone photoreceptor dysfunction/degeneration, distinguished from retinitis pigmentosa (a rod-cone disorder) by its cone-first pathology. It is classified along two axes: (i) course — stationary/congenital cone dysfunction syndromes (achromatopsia, blue-cone monochromatism) vs progressive cone dystrophy; and (ii) rod involvement — pure cone dystrophy vs cone-rod dystrophy (CORD; primary cone loss with secondary rod degeneration): "Cone and cone-rod dystrophies can be divided according to the disease course into stationary and progressive disorders or by the genetic mode of inheritance into autosomal-recessive, autosomal-dominant, and X-linked traits" ([PMID: 19184602](https://pubmed.ncbi.nlm.nih.gov/19184602/)). **Identifiers:** MONDO:0000455; OMIM CDSRR 610356 and multiple CORD entries; MeSH "Cone-Rod Dystrophies"; Orphanet cone/cone-rod dystrophy entries; ICD-11 9B70-range. **Synonyms:** progressive cone dystrophy, cone-rod dystrophy (CORD/CoRD), COD. Information is drawn from **aggregated disease-level resources** (OMIM, Orphanet, GeneReviews) and cohort/registry studies, not single-patient EHR ([PMID: 40736814](https://pubmed.ncbi.nlm.nih.gov/40736814/)).

### 2. Etiology
Cone dystrophy is a **Mendelian genetic disorder**; there are no established environmental or infectious causes. Causal factors are pathogenic variants in ≥20 genes (see Section 4). Genetic risk is defined by the causal variant and inheritance mode; **consanguinity** and **founder effects** are the dominant population-level risk amplifiers for recessive forms ([PMID: 25616768](https://pubmed.ncbi.nlm.nih.gov/25616768/), [PMID: 23362848](https://pubmed.ncbi.nlm.nih.gov/23362848/)). No robust environmental protective factors are established; UV protection and light avoidance are symptomatic rather than disease-modifying. Gene-environment interactions are minimal for this monogenic disorder, though light exposure may modulate the rate of cGMP/CNG-driven photoreceptor stress.

### 3. Phenotypes
Core phenotypes are **reduced central visual acuity** (HP:0007663), **dyschromatopsia** (HP:0000551), **photophobia** (HP:0000613), **nyctalopia** in cone-rod forms (HP:0000662), **nystagmus** in early-onset forms (HP:0000639), and **central/paracentral scotoma** (visual field defect, HP:0001123). Frequencies are quantified in Finding 8. Onset ranges from infancy (syndromic/achromatopsia-overlap forms, <1 year) to mid-teens/adulthood (progressive cone dystrophy). Severity is variable and progression is typically slow but relentless, ending in legal blindness (20/200 or worse). Quality-of-life impact centers on loss of reading/central vision, disabling glare, and color-discrimination failure; formal per-phenotype QOL instruments are underused in this population.

### 4. Genetic/Molecular Information
**Causal genes** by functional class: phototransduction — *GUCA1A, GUCY2D, PDE6C, PDE6H, CNGA3, CNGB3, GNAT2, KCNV2*; visual cycle/RPE — *ABCA4, RPGR*; transcription — *CRX*; ciliary/structural/trafficking — *RPGRIP1, RIMS1, RAB28, C8orf37, POC1B, TTLL5, CDHR1, PROM1, RP1L1, CEP290, ADAM9, UNC119*. **Variant types** include missense (e.g., GUCA1A L151F/Y99C, GUCY2D R838C/S, CNGA3 p.Cys319Arg), frameshift (CNGB3 p.T383fs), nonsense/truncating (RPGR-ORF15 distal truncations), and structural variants. **Functional consequences** are gain-of-function for dominant *GUCA1A/GUCY2D* (sustained cGMP synthesis) and for certain CNG variants (constitutive channel opening; [PMID: 35233102](https://pubmed.ncbi.nlm.nih.gov/35233102/)); loss-of-function for most recessive alleles. **Modifier genes:** *KCNV2* itself acts as a channel modifier subunit; *TTLL5* modifies RPGR via glutamylation. Epigenetic and large-scale chromosomal abnormalities are not major contributors, though structural variants at loci such as RP17/CEP290 require careful classification ([PMID: 42545071](https://pubmed.ncbi.nlm.nih.gov/42545071/)).

### 5. Environmental Information
Not applicable as primary cause — cone dystrophy is monogenic. No toxins, radiation, lifestyle factors, or infectious agents are established causes. Bright-light exposure and lack of UV/glare protection worsen symptoms but do not initiate disease.

### 6. Mechanism/Pathophysiology
The dominant pathway is **cGMP/Ca²⁺ dysregulation → CNG-channel over-activation → Ca²⁺ overload → calpain/PARP-mediated photoreceptor death** (see Mechanistic Model below). Relevant **GO biological processes:** phototransduction (GO:0007602), cGMP metabolic process (GO:0046068), regulation of cytosolic calcium ion concentration (GO:0051480), photoreceptor cell maintenance (GO:0045494), neuron apoptotic process (GO:0051402). **GO cellular components:** photoreceptor outer segment (GO:0001750), photoreceptor connecting cilium (GO:0032391), cyclic nucleotide-gated ion channel complex. **Cell type (CL):** retinal cone cell (CL:0000573). Additional mechanisms include ciliary transport defects (RPGR/RPGRIP1/CEP290), outer-segment structural failure (CDHR1), visual-cycle toxicity (ABCA4 lipofuscin/bisretinoid accumulation), and transcriptional dysregulation (CRX).

### 7. Anatomical Structures Affected
**Primary:** cone photoreceptors of the fovea centralis (UBERON:0001786 fovea centralis) within the macula lutea (UBERON:0005388), in the neural retina (UBERON:0003902). **Outer-retinal bands** affected on OCT: external limiting membrane, ellipsoid zone (IS/OS), interdigitation zone, and secondarily the retinal pigment epithelium (UBERON:0001782). **Subcellular:** photoreceptor outer segment and connecting cilium. Body system: nervous/visual system. Involvement is **bilateral** ([PMID: 23648999](https://pubmed.ncbi.nlm.nih.gov/23648999/), [PMID: 36934831](https://pubmed.ncbi.nlm.nih.gov/36934831/)).

### 8. Temporal Development
Onset is bimodal: infancy/early childhood for achromatopsia-overlap and syndromic forms (mean 3.9 years in KCNV2; [PMID: 33309813](https://pubmed.ncbi.nlm.nih.gov/33309813/)), and mid-teens/adulthood for classic progressive cone dystrophy. Onset pattern is insidious/chronic. Progression is generally slow but relentless; CORD progresses faster centrally than rod-cone disease (10.8%/yr vs 5.1%/yr; [PMID: 41237986](https://pubmed.ncbi.nlm.nih.gov/41237986/)). Disease course is progressive and lifelong; there is no spontaneous remission. Ellipsoid-zone contraction marks a critical structural window preceding acuity collapse ([PMID: 40494823](https://pubmed.ncbi.nlm.nih.gov/40494823/)).

### 9. Inheritance and Population
Prevalence ~1:30,000–40,000 (progressive CD) to ~1:14,000 (CORD in Israel) ([PMID: 40736814](https://pubmed.ncbi.nlm.nih.gov/40736814/), [PMID: 38753338](https://pubmed.ncbi.nlm.nih.gov/38753338/)). Inheritance is AD, AR, or X-linked. Penetrance is complete for most recessive forms but may be incomplete/age-dependent for dominant *GUCA1A/GUCY2D*. Founder effects and consanguinity elevate local prevalence markedly (ACHM ~1:5,000 in Arab-Muslim Jerusalem; [PMID: 25616768](https://pubmed.ncbi.nlm.nih.gov/25616768/)). Sex ratio is roughly equal for autosomal forms; X-linked *RPGR* disease predominantly affects males with variable female-carrier manifestation.

### 10. Diagnostics
Diagnosis integrates **full-field ERG** (photopic-selective loss; pathognomonic supernormal-rod ERG in CDSRR), **SD-OCT** (ellipsoid-zone/outer-nuclear-layer loss, bull's-eye maculopathy), **fundus autofluorescence** (central/ring hyperfluorescence), color-vision testing, and **molecular genetic testing** (gene panels, WES, and — for RPGR-ORF15 — long-read sequencing). Differential diagnosis includes Stargardt disease (ABCA4), occult macular dystrophy, hydroxychloroquine toxicity, and syndromic CORD (Alström, Bardet-Biedl). Because ABCA4 disease alleles are common in the population, overlap with Stargardt disease is frequent — "Fourteen probands (35%) were found to have a potentially disease-causing ABCA4 sequence variant on at least one allele" in a bull's-eye maculopathy series ([PMID: 18024811](https://pubmed.ncbi.nlm.nih.gov/18024811/)). Genetic diagnostic yield is comparatively low, arguing for comprehensive/long-read approaches ([PMID: 40571344](https://pubmed.ncbi.nlm.nih.gov/40571344/), [PMID: 42525358](https://pubmed.ncbi.nlm.nih.gov/42525358/), [PMID: 38091967](https://pubmed.ncbi.nlm.nih.gov/38091967/)).

### 11. Outcome/Prognosis
Cone dystrophy is not life-limiting; mortality is unaffected. Morbidity is defined by progressive central-vision loss to legal blindness (20/200 or worse, sometimes counting fingers), disabling photophobia, and eventual peripheral field loss in cone-rod forms ([PMID: 40736814](https://pubmed.ncbi.nlm.nih.gov/40736814/)). Prognostic factors include genotype, age of onset, and structural biomarkers (ellipsoid-zone length). Recovery is not spontaneous; gene therapy offers partial, genotype-specific functional stabilization/gain in select forms.

### 12. Treatment
No approved cure. **Supportive:** tinted/red-filter and photochromic lenses, refractive correction, low-vision aids, UV protection (NCIT: supportive care; low vision aids). **Advanced:** AAV gene supplementation for CNGA3/CNGB3 achromatopsia (safe, +2.65 ETDRS letters pooled; [PMID: 42542214](https://pubmed.ncbi.nlm.nih.gov/42542214/)); CRISPR "ablate-and-replace" for dominant GUCY2D CORD ([PMID: 42264060](https://pubmed.ncbi.nlm.nih.gov/42264060/)); genotype-agnostic neuroprotection via calpain/PARP inhibitors (preclinical; [PMID: 35327647](https://pubmed.ncbi.nlm.nih.gov/35327647/)). Pediatric CNGA3/CNGB3 trials are in Phases 1–2 ([PMID: 42627399](https://pubmed.ncbi.nlm.nih.gov/42627399/)). NCIT terms: Gene Therapy (NCIT:C15254), Adeno-associated Virus Vector, Supportive Care (NCIT:C15274).

### 13. Prevention
Classical primary prevention (vaccination/lifestyle) is not applicable. Prevention is **reproductive/genetic**: carrier and cascade testing (high-yield in founder/consanguineous populations), preimplantation and prenatal genetic diagnosis, and genetic counseling. "Accurate diagnosis is essential for accessing emerging gene-targeted treatments for inherited retinal diseases (IRDs), but many minoritised communities face additional barriers to diagnosis" ([PMID: 40513990](https://pubmed.ncbi.nlm.nih.gov/40513990/)). Tertiary prevention is supportive management to preserve residual function and quality of life.

### 14. Other Species / Natural Disease
Naturally occurring cone/cone-rod disease is well documented in **dogs** (NCBI Taxon 9615): CNGB3 day-blind dogs (Alaskan Malamute, German Shorthaired Pointer) and RPGRIP1 *cord1* progressive retinal atrophy in English Springer Spaniels ([PMID: 39428496](https://pubmed.ncbi.nlm.nih.gov/39428496/)). Orthologous genes (*Cnga3, Cngb3, Gnat2, Rpgr, Rpgrip1, Cdhr1*) are conserved across mouse (NCBI Taxon 10090) and dog, enabling comparative pathology and gene-therapy proof-of-concept. Disease mechanisms are evolutionarily conserved across mammals; no zoonotic potential (non-infectious).

### 15. Model Organisms
**Mouse:** *Cnga3* (cpfl5), *Gnat2* (cpfl3), *Cngb3* knockout, *Pde6c* (cpfl1), *Ttll5*-mutant, *Rpgr*-null, *Cdhr1* knockout, *Kcnv2* knockout, and CRX-mutant CORD models ([PMID: 20238068](https://pubmed.ncbi.nlm.nih.gov/20238068/), [PMID: 27162334](https://pubmed.ncbi.nlm.nih.gov/27162334/), [PMID: 42562233](https://pubmed.ncbi.nlm.nih.gov/42562233/)). **Dog:** natural CNGB3 and RPGRIP1 models. **Cellular:** patient-derived iPSC and retinal organoids (KCNV2, CEP290). Models faithfully reproduce absent photopic ERG, day-blindness, photophobia, and cone-opsin mislocalization; limitations include species differences in macular/foveal structure (mice lack a fovea), which constrains modeling of human central-vision phenotypes. Resources: MGI, IMPC, IMSR (mouse); OMIA (dog); Cellosaurus (cell lines).

---

## Mechanistic Model / Interpretation

The central pathophysiologic engine of many cone dystrophies is a **cGMP/Ca²⁺ imbalance** in the cone outer segment that converges on a common execution pathway:

```
   UPSTREAM (genotype-specific triggers)
   ┌─────────────────────────────────────────────────────────┐
   │  GUCA1A (GCAP1) gain-of-function ─┐                       │
   │  GUCY2D (RetGC-1) gain-of-function├─► ↑ cGMP synthesis    │
   │  PDE6C / PDE6H loss-of-function ──┘   (impaired breakdown)│
   └─────────────────────────────────────────────────────────┘
                          │
                          ▼
            ┌──────────────────────────────┐
            │   ELEVATED cGMP in cone OS    │
            └──────────────────────────────┘
                          │
        ┌─────────────────┴───────────────────┐
        ▼                                     ▼
  Over-activation of                Constitutive CNG opening
  CNGA3/CNGB3 channels              (gain-of-function variants,
  (excess ligand)                    e.g. CNGA3 R410W)
        └─────────────────┬───────────────────┘
                          ▼
            ┌──────────────────────────────┐
            │  Na⁺/Ca²⁺ INFLUX → Ca²⁺       │
            │  OVERLOAD + depolarization    │
            └──────────────────────────────┘
                          │
                          ▼
   DOWNSTREAM (genotype-agnostic executioner)
            ┌──────────────────────────────┐
            │  Calpain + PARP activation    │  ◄── DRUGGABLE
            │  → photoreceptor cell death   │      NODE
            └──────────────────────────────┘
                          │
                          ▼
   CLINICAL MANIFESTATION
   Cone loss → ↓ acuity, dyschromatopsia, photophobia
   (± secondary rod loss → nyctalopia, peripheral field loss = CORD)
```

**Parallel/alternative mechanisms** feed into the same end-stage cone death without traversing the cGMP node:

| Mechanism class | Representative genes | Effect |
|---|---|---|
| cGMP/Ca²⁺ dysregulation | GUCA1A, GUCY2D, PDE6C/H, CNGA3/B3 | ↑cGMP → CNG over-activation → Ca²⁺ death cascade |
| Ciliary/OS transport | RPGR, RPGRIP1, CEP290, TTLL5 | Opsin mislocalization, cilium dysfunction |
| Outer-segment structure | CDHR1, PROM1 | Shortened/disorganized OS, failed disc morphogenesis |
| Visual cycle / RPE | ABCA4 | Bisretinoid/lipofuscin toxicity |
| Transcription | CRX | Failed photoreceptor gene expression/maintenance |
| Ion-channel modifier | KCNV2 (Kv8.2) | Altered inner-segment K⁺ handling (CDSRR, supernormal rod ERG) |

The **calpain/PARP node is genotype-agnostic**, making it the most attractive target for a broadly applicable neuroprotective small-molecule therapy, complementary to gene-specific AAV/CRISPR approaches. Upstream, gain-of-function dominant disease (GUCA1A/GUCY2D and certain CNG variants) requires *silencing/editing* rather than simple *supplementation*, explaining why "ablate-and-replace" strategies are needed for CORD6.

---

## Evidence Base

| PMID | Title (abbrev.) | Supports finding |
|---|---|---|
| [38753338](https://pubmed.ncbi.nlm.nih.gov/38753338/) | Nationwide IRD prevalence, Israel | Epidemiology (CORD ~1:14,000) |
| [40736814](https://pubmed.ncbi.nlm.nih.gov/40736814/) | Progressive Cone & Cone-Rod Dystrophy (GeneReviews) | Prevalence ~1:30–40k, onset, prognosis |
| [40571344](https://pubmed.ncbi.nlm.nih.gov/40571344/) | Finnish IRD prevalence | Low diagnostic yield in CD/CRD |
| [15790869](https://pubmed.ncbi.nlm.nih.gov/15790869/) | GCAP1 L151F adCORD | GUCA1A gain-of-function mechanism |
| [10430891](https://pubmed.ncbi.nlm.nih.gov/10430891/) | RetGC-1 dimerization mutation | GUCY2D R838C gain-of-function |
| [42525358](https://pubmed.ncbi.nlm.nih.gov/42525358/) | PDE6C progressive cone dystrophy | Photopic-selective ERG signature |
| [38630375](https://pubmed.ncbi.nlm.nih.gov/38630375/) | KCNV2 siblings | Pathognomonic CDSRR ERG |
| [41237986](https://pubmed.ncbi.nlm.nih.gov/41237986/) | RPGR central sensitivity decline | CORD faster central decline |
| [40494823](https://pubmed.ncbi.nlm.nih.gov/40494823/) | PROM1 longitudinal study | EZ length as early biomarker |
| [27162334](https://pubmed.ncbi.nlm.nih.gov/27162334/) | TTLL5/RPGR glutamylation | X-linked cone dystrophy mechanism |
| [41481301](https://pubmed.ncbi.nlm.nih.gov/41481301/) | RPGR-ORF15 female carriers | Genotype-phenotype correlation |
| [20378608](https://pubmed.ncbi.nlm.nih.gov/20378608/) | Gene therapy in canine CNGB3 | AAV restores cone function |
| [42264060](https://pubmed.ncbi.nlm.nih.gov/42264060/) | CRISPR for CORD/ACHM | Ablate-and-replace for dominant GUCY2D |
| [35327647](https://pubmed.ncbi.nlm.nih.gov/35327647/) | PARP/calpain in IRD | cGMP death cascade & druggability |
| [35233102](https://pubmed.ncbi.nlm.nih.gov/35233102/) | ACHM channel mutation | CNG gain-of-function |
| [33309813](https://pubmed.ncbi.nlm.nih.gov/33309813/) | KCNV2 Study Group | Symptom frequencies |
| [41867372](https://pubmed.ncbi.nlm.nih.gov/41867372/) | Achromatopsia cohort | Phenotype frequencies, imaging |
| [25052312](https://pubmed.ncbi.nlm.nih.gov/25052312/) | CNGA3 cone-rod dystrophy | Allelic continuum |
| [29193673](https://pubmed.ncbi.nlm.nih.gov/29193673/) | ALMS1 cone-rod dystrophy | Syndromic differential |
| [25616768](https://pubmed.ncbi.nlm.nih.gov/25616768/) | CNGA3 achromatopsia genetics | Founder effect, elevated prevalence |
| [23362848](https://pubmed.ncbi.nlm.nih.gov/23362848/) | Newfoundland achromatopsia | Founder effects |
| [23648999](https://pubmed.ncbi.nlm.nih.gov/23648999/) | Outer retina OCT in CORD | Foveal/macular band pathology |
| [36934831](https://pubmed.ncbi.nlm.nih.gov/36934831/) | Foveal photoreceptor OCT | Fovea/macula as target |
| [42542214](https://pubmed.ncbi.nlm.nih.gov/42542214/) | AAV meta-analysis (ACHM) | Efficacy +2.65 letters, safety |
| [28095637](https://pubmed.ncbi.nlm.nih.gov/28095637/) | Gene therapy for achromatopsia | 80% CNGA3/CNGB3 |
| [20238068](https://pubmed.ncbi.nlm.nih.gov/20238068/) | Achromatopsia gene therapy candidate | Animal models |
| [42562233](https://pubmed.ncbi.nlm.nih.gov/42562233/) | CDHR1 degeneration | Knockout model + gene therapy rescue |
| [39428496](https://pubmed.ncbi.nlm.nih.gov/39428496/) | Canine cord1 RPGRIP1 | Large-animal CORD model |
| [18024811](https://pubmed.ncbi.nlm.nih.gov/18024811/) | ABCA4 bull's-eye maculopathy | ABCA4/Stargardt overlap |
| [19184602](https://pubmed.ncbi.nlm.nih.gov/19184602/) | Genetics of cone/cone-rod dystrophies | Classification framework |
| [40513990](https://pubmed.ncbi.nlm.nih.gov/40513990/) | IRD in Indigenous populations | Diagnosis as prevention lever |
| [42627399](https://pubmed.ncbi.nlm.nih.gov/42627399/) | Pediatric gene therapy trials | CNGA3/CNGB3 trials Phase 1–2 |
| [42602306](https://pubmed.ncbi.nlm.nih.gov/42602306/) | Temporal vision in ACHM | Childhood treatment restores flicker fusion |
| [38091967](https://pubmed.ncbi.nlm.nih.gov/38091967/) | Adult-onset CD/CRD | Bull's-eye maculopathy, presenting symptom |
| [39100576](https://pubmed.ncbi.nlm.nih.gov/39100576/) | CORD case | OCT EZ loss + extinguished photopic ERG |

**How the evidence coheres:** The mechanistic papers (10430891, 15790869, 35327647, 35233102) establish the cGMP→CNG→Ca²⁺→calpain/PARP causal chain; the cohort/imaging papers (42525358, 33309813, 41867372, 23648999) establish the clinical/diagnostic phenotype; the epidemiology/genetics papers (38753338, 40736814, 25616768, 23362848) establish population parameters; and the therapeutic papers (42542214, 20378608, 42264060, 42562233) establish the treatment frontier. No papers in the reviewed set directly contradict the core model, though the low diagnostic yield (40571344) and difficulty resolving RPGR-ORF15 variants flag that the known genetic spectrum is incomplete.

---

## Limitations and Knowledge Gaps

1. **No primary experimental dataset.** This report is a literature-synthesis of published cohorts, mechanistic studies, and reviews; no independent statistical analysis of raw patient data was performed. All effect sizes and prevalence figures are as reported in the primary literature.
2. **Genetic diagnostic gap.** Cone/cone-rod dystrophy has among the lowest causative-variant identification rates of all IRD subphenotypes ([PMID: 40571344](https://pubmed.ncbi.nlm.nih.gov/40571344/)). Hidden causes include structural variants, deep-intronic/pseudoexon variants (e.g., CEP290; [PMID: 42545071](https://pubmed.ncbi.nlm.nih.gov/42545071/)), and the repetitive RPGR-ORF15 region that eludes short-read sequencing.
3. **Prevalence heterogeneity.** Estimates range from ~1:14,000 (CORD, Israel) to ~1:30,000–40,000 (progressive CD), reflecting differences in ascertainment, definition (cone vs cone-rod vs achromatopsia), and population structure (founder/consanguineous enrichment). A single global figure is not well established.
4. **Therapeutic evidence is genotype-narrow.** Robust human gene-therapy data exist essentially only for CNGA3/CNGB3 achromatopsia; efficacy for CNGB3 is uncertain, and dominant gain-of-function forms (GUCA1A/GUCY2D) lack approved editing therapies. Calpain/PARP neuroprotection remains preclinical.
5. **Quality-of-life data are thin.** Formal per-phenotype QOL instruments (EQ-5D, SF-36, PROMIS) are rarely applied specifically to cone dystrophy cohorts; QOL impact is inferred from functional endpoints.
6. **Model organism limitations.** Mice lack a fovea, limiting fidelity for the central-vision phenotype that dominates human disease; large-animal (dog) models better capture cone-directed pathology but are resource-intensive.
7. **Natural-history endpoints.** Sensitive, validated structural/functional endpoints (e.g., ellipsoid-zone length, microperimetry) are still being standardized for trial readiness across genotypes.

---

## Proposed Follow-up Experiments / Actions

1. **Deploy long-read and structural-variant-aware sequencing** (e.g., nanopore RPGR-ORF15, optical genome mapping) systematically in genetically unsolved cone/cone-rod dystrophy cohorts to close the diagnostic gap and enable therapy eligibility.
2. **Advance genotype-agnostic neuroprotection to trials.** Given the convergent calpain/PARP death cascade, formally test calpain and PARP inhibitors (and CNG-channel/voltage-gated Ca²⁺/Na⁺ channel blockers) in cone-directed IRD explant and large-animal models, then early-phase human trials, as a broad add-on to gene-specific therapy.
3. **Develop editing therapy for dominant GUCA1A/GUCY2D CORD.** Optimize dual-AAV "ablate-and-replace" or base/prime-editing approaches to raise editing efficiency and durability beyond the ~24-week ONL preservation demonstrated in mice.
4. **Standardize natural-history endpoints.** Establish multicenter, genotype-stratified longitudinal cohorts using ellipsoid-zone length, microperimetry, adaptive-optics cone density, and FST as validated endpoints to power future trials.
5. **Expand carrier/cascade screening** in defined founder and consanguineous populations (e.g., Arab-Muslim Jerusalem, Pingelapese, Newfoundland) where recessive alleles are enriched, coupled with equitable access to diagnosis in underserved communities.
6. **Extend gene-therapy age-window studies.** The observation that only a treated child regained near-normal flicker-fusion argues for prospective pediatric-versus-adult comparative trials to define the critical treatment window.
7. **Integrate patient-derived retinal organoids** (iPSC) for high-throughput variant functional classification (VUS resolution) and preclinical drug screening across the diverse cone-dystrophy gene spectrum.

---

*Report compiled from 20 confirmed findings, 10 supported hypotheses, and 94 reviewed papers across 10 investigation iterations. Evidence source types span human clinical cohorts, model organism studies (mouse, dog), in vitro/iPSC systems, and computational modeling, as annotated per citation.*


## Artifacts

- [OpenScientist final report](Cone_Dystrophy-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Cone_Dystrophy-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:38753338
2. PMID:40736814
3. PMID:40571344
4. PMID:15790869
5. PMID:10430891
6. PMID:42525358
7. PMID:38630375
8. PMID:41237986
9. PMID:40494823
10. PMID:27162334
11. PMID:41481301
12. PMID:20378608
13. PMID:42264060
14. PMID:35327647
15. PMID:35233102
16. PMID:33309813
17. PMID:41867372
18. PMID:25052312
19. PMID:29193673
20. PMID:25616768
21. PMID:23362848
22. PMID:38091967
23. PMID:39100576
24. PMID:42542214
25. PMID:28095637
26. PMID:42602306
27. PMID:20238068
28. PMID:42562233
29. PMID:39428496
30. PMID:36934831
31. PMID:23648999
32. PMID:19184602
33. PMID:42545071
34. PMID:18024811
35. PMID:42627399
36. PMID:40513990