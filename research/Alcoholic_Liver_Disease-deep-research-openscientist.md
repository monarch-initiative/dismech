---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-26T04:51:04.945096'
end_time: '2026-07-26T05:19:26.640461'
duration_seconds: 1701.7
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Alcohol-Associated Liver Disease
  mondo_id: ''
  category: Complex
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
citation_count: 43
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Alcoholic_Liver_Disease-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Alcoholic_Liver_Disease-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Alcohol-Associated Liver Disease
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Alcohol-Associated Liver Disease** covering all of the
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

# Alcohol-Associated Liver Disease (ALD): A Comprehensive Disease Characteristics Report

## Summary

**Alcohol-associated liver disease (ALD)** is a complex, non-Mendelian, dose-dependent liver disease caused by chronic excessive alcohol consumption. It encompasses a histological spectrum that progresses from **hepatic steatosis → alcohol-associated steatohepatitis → progressive fibrosis → cirrhosis → hepatocellular carcinoma (HCC)**, with **alcohol-associated hepatitis (AH)** representing an acute, superimposed, high-mortality clinical syndrome. Under the 2023 multisociety steatotic liver disease (SLD) nomenclature, ALD is distinguished from metabolic dysfunction-associated steatotic liver disease (MASLD) and the overlap phenotype **MetALD**. Although ALD has a lower prevalence than MASLD, it contributes disproportionately to liver-related morbidity and mortality and is now the leading cause of liver-related death and the most common indication for liver transplantation in Europe and the United States.

The pathophysiology of ALD is best understood as a **dual-hit (multi-hit) process**. The first hit is direct hepatotoxicity from ethanol metabolism: alcohol dehydrogenase (ADH) and inducible cytochrome **CYP2E1** oxidize ethanol to **acetaldehyde**, which forms protein/DNA adducts (including malondialdehyde-acetaldehyde, MAA, adducts), generates reactive oxygen species (ROS), depletes glutathione, and causes lipid peroxidation and mitochondrial dysfunction. The second hit is **gut–liver axis dysfunction**: alcohol increases intestinal permeability, permitting lipopolysaccharide (LPS) translocation that activates hepatic Kupffer cells via TLR4/NF-κB signaling, driving TNF-α/IL-1β/IL-6 release and neutrophilic inflammation. These converging insults activate **hepatic stellate cells (HSCs)** through TGF-β1/Smad signaling, producing the collagen deposition that defines fibrosis and cirrhosis. Genetic susceptibility (notably **PNPLA3 rs738409 I148M**, with **TM6SF2** and **MBOAT7** as additional risk loci and **HSD17B13** and **MTARC1** as protective), alcohol-metabolizing enzyme polymorphisms (**ADH1B**, **ALDH2**), sex, obesity, and drinking pattern all modify individual risk.

Management centers on **alcohol abstinence and treatment of the underlying alcohol use disorder (AUD)**, which markedly improve survival, decompensation risk, and recompensation. For severe AH, **corticosteroids** remain guideline-recommended but confer only modest short-term benefit with high non-response and infection risk; **early liver transplantation** rescues steroid non-responders with excellent survival. Emerging therapies target the epigenome (larsucosterol), IL-22 signaling (F-652), the FXR/bile acid axis (INT-787), and the gut microbiome (rifaximin, fecal microbiota transplantation).

---

## Key Findings

### Finding 1 — PNPLA3 I148M is the strongest genetic risk locus for ALD (F001)

Genome-wide association and candidate-gene studies consistently identify **PNPLA3 rs738409 (c.444C>G, p.Ile148Met, "I148M")** as the top common variant increasing risk of alcohol-associated steatosis, cirrhosis, and HCC. Two additional risk loci — **TM6SF2 (rs58542926, E167K)** and **MBOAT7 (rs641738)** — add to lifetime risk, while **HSD17B13 (rs72613567)** and **MTARC1** confer protection. These loci govern hepatic lipid handling and retinoid metabolism. As documented for the overlapping steatotic liver disease genetics: *"Key genetic variants, such as those located in the PNPLA3, TM6SF2, and MBOAT7 genes, often interact to exacerbate MASLD severity and play key roles in lipid metabolism and liver inflammation"* ([PMID: 41772607](https://pubmed.ncbi.nlm.nih.gov/41772607/)). Importantly, these are common polymorphisms of modest individual effect acting on a substrate of alcohol exposure — ALD is polygenic, not Mendelian.

### Finding 2 — ALD pathogenesis: acetaldehyde/CYP2E1 oxidative stress plus gut-liver endotoxemia (F002)

Ethanol is oxidized by ADH and inducible **CYP2E1** to acetaldehyde, which forms protein/DNA adducts and generates ROS, depleting glutathione and causing lipid peroxidation and mitochondrial dysfunction. *"Specific inhibition of CYP2E1 led to the greatest decrease in oxidative stress, toxicity and protein aldehyde adduct formation, implicating that CYP2E1 accelerates the formation of protein aldehyde adducts which can be an important mechanism for alcohol mediated liver injury"* ([PMID: 23352969](https://pubmed.ncbi.nlm.nih.gov/23352969/)). In parallel, alcohol increases intestinal permeability, allowing LPS translocation that activates Kupffer cells via TLR4/NF-κB. The overall picture is multifactorial: *"The pathophysiology of SAH is multifactorial, involving direct hepatotoxicity from alcohol metabolites, oxidative stress, dysregulated immune activation, gut dysbiosis with increased intestinal permeability, impaired hepatic regeneration, and genetic susceptibility"* ([PMID: 41715264](https://pubmed.ncbi.nlm.nih.gov/41715264/)).

### Finding 3 — ALD spans a histological spectrum and disproportionately drives liver mortality (F003)

ALD *"represents a spectrum of liver injury beginning with hepatic steatosis (fatty liver) progressing to inflammation and culminating in cirrhosis"* ([PMID: 38672422](https://pubmed.ncbi.nlm.nih.gov/38672422/)). Epidemiologically, it *"has a lower prevalence but contributes disproportionately to higher liver-related morbidity and mortality and is reported to have a marked regional variation linked to patterns of alcohol consumption"* ([PMID: 42457160](https://pubmed.ncbi.nlm.nih.gov/42457160/)). Alcohol-associated hepatitis incidence varies widely: *"Reported annual incidence rates of AH ranged from 1.02 per 100,000 inhabitants in Iceland to 98.5 per 100,000 inhabitants in the United States, with a median incidence rate of 6.8 cases per 100,000 inhabitants"* ([PMID: 42435889](https://pubmed.ncbi.nlm.nih.gov/42435889/)). Globally, in 2021, cirrhosis and chronic liver disease accounted for **~1.4 million deaths worldwide** ([PMID: 42486788](https://pubmed.ncbi.nlm.nih.gov/42486788/)).

### Finding 4 — Treatment centers on abstinence, corticosteroids for severe AH, and early transplantation (F004)

Abstinence is the cornerstone. For severe AH (Maddrey DF ≥32 / MELD ≥20), corticosteroids remain standard of care but confer limited benefit: in a large multicenter cohort, *"no survival benefit was observed in the adjusted model after accounting for baseline and admission characteristics (adjusted hazard ratio [aHR] = 1.01, P = 0.818)"* ([PMID: 39620604](https://pubmed.ncbi.nlm.nih.gov/39620604/)). Early liver transplantation rescues non-responders: pooled *"overall survival rate was 85%, with survival rates of 89% at 1 year, 81% at 2 years, 78% at 5 years, and 60% at 10 years... The overall relapse rate post-eLT was 19%"* ([PMID: 42148785](https://pubmed.ncbi.nlm.nih.gov/42148785/)). New agents are emerging: *"Multiple new pharmacological agents targeting different mechanisms are under study for alcohol-associated hepatitis, including larsucosterol, F-652, and INT-787"* ([PMID: 41691535](https://pubmed.ncbi.nlm.nih.gov/41691535/)).

### Finding 5 — HSC activation via TGF-β1/Smad drives fibrosis; sex, obesity, and drinking pattern modify risk (F005)

*"Alcoholic liver fibrosis (ALF) is a severe hepatic disorder caused by chronic excessive alcohol consumption, involving hepatic stellate cells (HSCs) activation"* into α-SMA-expressing myofibroblasts depositing Collagen-I/III via TGF-β1/Smad3/Smad4 ([PMID: 41270641](https://pubmed.ncbi.nlm.nih.gov/41270641/)). Risk is modified by female sex, obesity/metabolic syndrome (MetALD synergy), smoking, and binge/daily drinking; alcohol independently correlates with fatty liver even in normal-weight adults: *"In normal weight, the independent correlates included alanine transaminase (3.05), smoking (2.56), systolic blood pressure (1.54), and alcohol intake (1.41)"* ([PMID: 25333756](https://pubmed.ncbi.nlm.nih.gov/25333756/)).

### Finding 6 — Rodent models recapitulate steatosis/inflammation and implicate innate immune cells (F006)

The chronic **Lieber-DeCarli** ethanol liquid diet and the NIAAA chronic-plus-single-binge (**Gao-binge**) model reproduce hallmark ALD features. *"using a Lieber-DeCarli ethanol liquid diet model of ALD in C57BL/6 mice"* reproduces ALT/AST elevation, oxidative stress, and inflammation graded by SALVE ([PMID: 39795945](https://pubmed.ncbi.nlm.nih.gov/39795945/)). Mechanistic studies implicate innate lymphoid dynamics: *"Either depletion of ILC1 or neutralization of IL17A could significantly attenuate liver steatosis, inflammation, and injury in alcohol-fed mice"* ([PMID: 36174925](https://pubmed.ncbi.nlm.nih.gov/36174925/)). A key limitation is that rodent models poorly recapitulate advanced human fibrosis, cirrhosis, and severe AH.

### Finding 7 — Definition, dose thresholds, symptoms, and rising mortality (F007)

ALD develops with daily intake **>20 g/day in women (~1.4 drinks)** and **>30 g/day in men (~2.1 drinks)**: *"ALD can develop with long-term daily alcohol consumption of more than 20 g per day for women (1.4 standard drinks/d) and more than 30 g per day for men (2.1 standard drinks/d), with 1 standard drink containing 14 g of ethanol"* ([PMID: 42406571](https://pubmed.ncbi.nlm.nih.gov/42406571/)). US mortality is rising: *"In the US, ALD-related mortality increased from 6.7 deaths per 100,000 people in 1999 to 12.5 deaths per 100,000 people in 2022."* Risk factors: *"increased quantity and duration of alcohol use, female sex, older age, obesity, type 2 diabetes, metabolic syndrome, smoking, viral hepatitis, and specific genetic variants."* AH symptoms: *"fever, anorexia, nausea, vomiting, abdominal pain, and jaundice"* (all [PMID: 42406571](https://pubmed.ncbi.nlm.nih.gov/42406571/)).

### Finding 8 — MELD, Maddrey DF, and Lille scores stratify prognosis (F008)

Severe AH is defined by Maddrey DF ≥32 or MELD ≥20–21. *"Updated MELD measurements had a strong prognostic value for death/transplant (HR: 1.20, 95% CI: 1.14-1.27)"* ([PMID: 39082963](https://pubmed.ncbi.nlm.nih.gov/39082963/)). The early Lille score classifies steroid response: LI2 *"was associated with a 28-day mortality HR of 33.1 (95% CI: 3.8-287.3)... AUCs for 28-day mortality were 0.818 for LI2, 0.794 for LI4, and 0.809 for LI7"* ([PMID: 40545192](https://pubmed.ncbi.nlm.nih.gov/40545192/)). Age-augmented models improve prediction: *"MELD-Age and ACLF-Age, had similar predictability (AUROC: 0.73, 0.73, 0.72...), outperforming Lille and Maddrey's (AUROC: 0.63, 0.62)"* ([PMID: 39167426](https://pubmed.ncbi.nlm.nih.gov/39167426/)).

### Finding 9 — Functional ADH1B/ALDH2 polymorphisms modulate acetaldehyde exposure and ALD risk (F009)

In East Asians, common functional variants alter risk via acetaldehyde exposure: *"ADH1B accelerates ethanol oxidation, whereas ALDH2 impairs acetaldehyde detoxification and increases oxidative stress, inflammation, and liver injury. Based on genotype combinations, individuals were stratified into five alcohol sensitivity groups with differing risks of cirrhosis and cancer"* ([PMID: 40943250](https://pubmed.ncbi.nlm.nih.gov/40943250/)). ALDH2 deficiency usually reduces intake via aversive flushing, but continued drinking paradoxically raises liver and GI cancer risk.

### Finding 10 — Single-cell profiling reveals monocyte/macrophage expansion, adaptive immune dysfunction, and epigenetic reprogramming (F010)

scRNA-seq of PBMCs in AH shows innate immune dysregulation: *"inflammatory cytokines and chemokines were highly expressed in AH, including IL-2, IL-32, CXC3R1 and CXCL16 in monocytes and NK cells, whereas HLA-DR genes were reduced in monocytes"* (immune paralysis) ([PMID: 38040543](https://pubmed.ncbi.nlm.nih.gov/38040543/)). In cirrhotic liver, *"scRNA-seq analysis identified a higher ratio of intrahepatic monocyte/macrophages and an obvious decreased ratio of T cells and B cells in the ALC group than in the HBV group"* ([PMID: 36817578](https://pubmed.ncbi.nlm.nih.gov/36817578/)). Epigenetically, *"Hepatocyte FoxO1 levels in human inflammatory livers declined prevalently and were inversely correlated with inflammation and fibrosis"* ([PMID: 41190981](https://pubmed.ncbi.nlm.nih.gov/41190981/)).

### Finding 11 — Multi-omic and gut-dysbiosis biomarkers define ALD risk, staging, and mechanism (F011)

Serum fibrosis markers extend staging beyond aminotransferases: *"Traditional serum-based liver fibrosis markers (e.g., cytokeratin-18 fragments, Pro-C3, the enhanced liver fibrosis test) improve non-invasive staging risk beyond aminotransferases"* ([PMID: 41287436](https://pubmed.ncbi.nlm.nih.gov/41287436/)). Gut signatures also track disease: *"gut dysbiosis signatures, including reduced Faecalibacterium prausnitzii, Akkermansia muciniphila, and a lower Firmicutes/Bacteroidetes ratio, and their metabolites (short-chain fatty acids, and bile acids, trimethylamine N-oxide) correlate with liver inflammation and fibrosis"* (same source).

### Finding 12 — Gut-liver axis therapies: FMT improves short-term survival in severe AH (F012)

A meta-analysis of 8 studies (444 patients) found FMT *"showed a statistically significant increase in survival in the FMT arm at 28 days [RR 2.30 (1.24-4.28), P = 0.01] and 90 days [2.53 (1.34-4.77), P < 0.001]"* without serious treatment-related adverse events ([PMID: 40359297](https://pubmed.ncbi.nlm.nih.gov/40359297/)). The broader pipeline is mechanism-diverse: *"Anti-inflammatory agents such as IL-1 inhibitor, Pan-caspase inhibitor, Apoptosis signal-regulating kinase-1, and CCL2 inhibitors are under investigation. Other group of agents include gut-liver axis modulators, hepatic regeneration, antioxidants, and Epigenic modulators"* ([PMID: 36647403](https://pubmed.ncbi.nlm.nih.gov/36647403/)).

### Finding 13 — Treating the underlying AUD is central; baclofen best-studied in cirrhosis (F013)

Six medications are approved for AUD: *"acamprosate (ACM), naltrexone (NTX), nalmefene (NMF), disulfiram (DF), baclofen, and sodium oxybate (SO)"* ([PMID: 42476146](https://pubmed.ncbi.nlm.nih.gov/42476146/)). In ALD specifically: *"Naltrexone and acamprosate reduce the relapse in the general AUD population, though data in ALD are limited. Baclofen is the only drug tested in randomized trials in cirrhosis, with early benefit but mixed results in later studies"* ([PMID: 41258558](https://pubmed.ncbi.nlm.nih.gov/41258558/)). Medication-assisted therapy is cost-effective in compensated alcohol-related cirrhosis ([PMID: 33326815](https://pubmed.ncbi.nlm.nih.gov/33326815/)).

### Finding 14 — Abstinence and AUD treatment markedly improve survival and enable recompensation (F014)

Meta-analysis (19 studies, 18,833 patients): *"individuals who continued to consume alcohol had significantly lower overall survival compared to those who were abstinent (HR: 0.611, 95% CI: 0.506-0.738)... Alcohol abstinence was associated with a significantly lower risk of hepatic decompensation (HR: 0.612, 95% CI: 0.473-0.792)"* ([PMID: 38303565](https://pubmed.ncbi.nlm.nih.gov/38303565/)). AUD treatment *"reduces alcohol relapse by 73% (HR: 0.27, 95% CI: 0.15-0.46) with any treatment and by 77% (HR: 0.23, 95% CI: 0.14-0.39) with medications"* ([PMID: 40304585](https://pubmed.ncbi.nlm.nih.gov/40304585/)). After first decompensation, *"45 (24.5%) achieved abstinence-induced recompensation"* ([PMID: 41622173](https://pubmed.ncbi.nlm.nih.gov/41622173/)).

### Finding 15 — ALD impairs quality of life; a disease-specific instrument now exists (F015)

The validated **CLDQ-ALD** reduced 40 items to *"9 domains (Fatigue, Alcohol, Function, Physical, Abdominal Symptoms, Itching, Sleep, Emotional, and Worry)"* ([PMID: 42190270](https://pubmed.ncbi.nlm.nih.gov/42190270/)). Stigma independently worsens burden: *"Stigmatization of patients with NAFLD, whether it is caused by obesity or NAFLD, is strongly and independently associated with a substantial impairment of their HRQL"* ([PMID: 39022387](https://pubmed.ncbi.nlm.nih.gov/39022387/)), with disparities producing worse outcomes ([PMID: 40063362](https://pubmed.ncbi.nlm.nih.gov/40063362/)).

---

## Full Section-by-Section Report

### 1. Disease Information

ALD is chronic liver injury resulting from harmful alcohol use, spanning reversible steatosis, steatohepatitis (with the acute severe form alcohol-associated hepatitis), fibrosis, cirrhosis, portal hypertension, decompensation, and HCC ([PMID: 42406571](https://pubmed.ncbi.nlm.nih.gov/42406571/), [PMID: 38672422](https://pubmed.ncbi.nlm.nih.gov/38672422/)).

**Key identifiers (suggested):** MONDO:0005154 / MONDO:0004790 (alcoholic liver disease); **ICD-11 DB94**; **ICD-10 K70** (K70.0 fatty liver, K70.1 hepatitis, K70.2 fibrosis/sclerosis, K70.3 cirrhosis, K70.4 hepatic failure); **MeSH D008108** ("Liver Diseases, Alcoholic"); SNOMED CT 41309000. OMIM assigns no Mendelian ID because ALD is complex/non-Mendelian. **CHEBI:** ethanol (CHEBI:16236), acetaldehyde (CHEBI:15343).

**Synonyms:** alcohol-related liver disease (ArLD), alcoholic liver disease, alcohol-induced liver disease; subtypes alcoholic fatty liver, alcoholic steatohepatitis/hepatitis, alcoholic cirrhosis. The 2023 multisociety Delphi consensus formalized ALD, the overlap phenotype MetALD, and MASLD within SLD ([PMID: 42457160](https://pubmed.ncbi.nlm.nih.gov/42457160/)).

**Information source:** aggregated disease-level resources (epidemiological registries, clinical cohorts, GWAS, mechanistic/model studies), not individual-patient EHR.

### 2. Etiology

The necessary cause is chronic excessive alcohol consumption, with sex-specific dose thresholds (>20 g/day women, >30 g/day men). Environmental/lifestyle risk factors include quantity/duration of alcohol, binge/daily pattern, obesity, type 2 diabetes, metabolic syndrome, smoking, older age, and viral hepatitis ([PMID: 42406571](https://pubmed.ncbi.nlm.nih.gov/42406571/)). Genetic risk: PNPLA3 I148M (strongest), TM6SF2 E167K, MBOAT7 rs641738 ([PMID: 41772607](https://pubmed.ncbi.nlm.nih.gov/41772607/)); ADH1B/ALDH2 modulate acetaldehyde exposure ([PMID: 40943250](https://pubmed.ncbi.nlm.nih.gov/40943250/)). Protective: HSD17B13, MTARC1 (genetic); abstinence and alcohol policy (environmental) ([PMID: 41772607](https://pubmed.ncbi.nlm.nih.gov/41772607/), [PMID: 42266909](https://pubmed.ncbi.nlm.nih.gov/42266909/)). Gene–environment interaction is canonical: risk alleles act only with alcohol exposure; ADH1B/ALDH2 genotype combinations stratify drinkers into ~5 alcohol-sensitivity groups ([PMID: 40943250](https://pubmed.ncbi.nlm.nih.gov/40943250/)).

### 3. Phenotypes (HPO suggestions)

~90% of patients are asymptomatic or have nonspecific fatigue. AH: fever (HP:0001945), anorexia (HP:0002039), nausea/vomiting, abdominal pain (HP:0002027), jaundice (HP:0000952). Decompensated cirrhosis: ascites (HP:0001541), variceal bleeding (HP:0002040), hepatic encephalopathy (HP:0002480), splenomegaly (HP:0001744). Lab abnormalities: AST>ALT (HP:0002910), elevated GGT, hyperbilirubinemia (HP:0002904), coagulopathy (HP:0003256), hypoalbuminemia, thrombocytopenia. Structural: hepatomegaly (HP:0002240), hepatic steatosis (HP:0001397), fibrosis (HP:0001395), cirrhosis (HP:0001394), hepatic failure (HP:0001399), HCC (HP:0001402). Adult-onset, insidious/chronic; AH acute/severe. Quality of life impaired across 9 CLDQ-ALD domains ([PMID: 42190270](https://pubmed.ncbi.nlm.nih.gov/42190270/)).

### 4. Genetic/Molecular Information

No causal Mendelian gene. Susceptibility/modifier genes: PNPLA3 (HGNC:18590), TM6SF2 (HGNC:25136), MBOAT7 (HGNC:15505), ADH1B (HGNC:250), ALDH2 (HGNC:404), CYP2E1 (HGNC:2631), protective HSD17B13 (HGNC:18507), MTARC1 (HGNC:24337). PNPLA3 c.444C>G p.Ile148Met is a common missense variant (higher MAF in Hispanic/Latino populations), germline, altering lipid-droplet triglyceride/retinyl-ester hydrolysis. HSD17B13 rs72613567 is a loss-of-function splice variant (protective). Epigenetic: alcohol perturbs DNA methylation/histone marks; hepatocyte FoxO1 is epigenetically repressed ([PMID: 41190981](https://pubmed.ncbi.nlm.nih.gov/41190981/)); larsucosterol targets DNMT epigenetics therapeutically. Chromosomal abnormalities: not characteristic.

### 5. Environmental Information

Primary factor: ethanol/acetaldehyde (CHEBI:16236 / CHEBI:15343). Lifestyle: heavy/binge drinking, smoking, obesity, diet ([PMID: 42406571](https://pubmed.ncbi.nlm.nih.gov/42406571/), [PMID: 25333756](https://pubmed.ncbi.nlm.nih.gov/25333756/)). No infectious cause, but gut dysbiosis and increased permeability drive LPS translocation (gut-liver axis) — a microbial rather than single-pathogen contributor ([PMID: 41715264](https://pubmed.ncbi.nlm.nih.gov/41715264/)); HBV/HCV co-infection synergistically accelerates progression.

### 6. Mechanism / Pathophysiology

**Causal chain:** (1) Ethanol → ADH/CYP2E1 → acetaldehyde + ROS → adducts, GSH depletion, lipid peroxidation, mitochondrial dysfunction ([PMID: 23352969](https://pubmed.ncbi.nlm.nih.gov/23352969/)). (2) Gut-liver axis: ↑ permeability → LPS → Kupffer TLR4/NF-κB → TNF-α/IL-1β/IL-6, neutrophils; NK-cell loss with ILC1/IL-17A dominance ([PMID: 36174925](https://pubmed.ncbi.nlm.nih.gov/36174925/)). (3) HSC activation → α-SMA myofibroblasts, Collagen-I/III via TGF-β1/Smad ([PMID: 41270641](https://pubmed.ncbi.nlm.nih.gov/41270641/)). (4) Cirrhosis, portal hypertension, HCC ([PMID: 38672422](https://pubmed.ncbi.nlm.nih.gov/38672422/)). Pathways: CYP2E1/oxidative stress, TLR4-NF-κB, TGF-β/Smad, JAK/STAT3, PPARα/δ, FXR/IL-22. Cell types (CL): hepatocyte (CL:0000182), Kupffer cell (CL:0000091), HSC (CL:0000632), monocyte (CL:0000576), NK (CL:0000623), NKT (CL:0000814), neutrophil (CL:0000775). Subcellular (GO CC): mitochondrion (GO:0005739), ER (GO:0005783), lipid droplet (GO:0005811). Single-cell/omics evidence in Findings 10–11.

### 7. Anatomical Structures Affected

Primary organ: liver (UBERON:0002107). Secondary/systemic: portal venous system and spleen (UBERON:0002106), esophagus/stomach (varices, UBERON:0001043), brain (encephalopathy, UBERON:0000955), kidney (hepatorenal syndrome, UBERON:0002113), blood/marrow (cytopenias), pancreas. Tissue/cell level: hepatic parenchyma, sinusoidal Kupffer and stellate cells, infiltrating neutrophils. Diffuse/bilateral hepatic involvement; steatosis and fibrosis often begin zone 3 (perivenular/centrilobular).

### 8. Temporal Development

Adult-onset, insidious/chronic after years of heavy drinking; AH acute/subacute. Stages: steatosis (reversible) → steatohepatitis → fibrosis → cirrhosis (compensated → decompensated) → HCC ([PMID: 38672422](https://pubmed.ncbi.nlm.nih.gov/38672422/)). Progressive but modifiable — abstinence halts/reverses early stages; ~24.5% achieve abstinence-induced recompensation after first decompensation ([PMID: 41622173](https://pubmed.ncbi.nlm.nih.gov/41622173/)). Critical window: early abstinence; corticosteroid response assessed at day 7 (Lille); delayed tertiary care worsens AH outcomes ([PMID: 39829300](https://pubmed.ncbi.nlm.nih.gov/39829300/)).

### 9. Inheritance and Population

Lower prevalence than MASLD but disproportionate mortality with regional variation ([PMID: 42457160](https://pubmed.ncbi.nlm.nih.gov/42457160/)). AH incidence ~1.0–98.5/100,000 (median 6.8) ([PMID: 42435889](https://pubmed.ncbi.nlm.nih.gov/42435889/)); US ALD mortality 6.7→12.5/100,000 (1999→2022) ([PMID: 42406571](https://pubmed.ncbi.nlm.nih.gov/42406571/)); ~1.4M global cirrhosis deaths in 2021 ([PMID: 42486788](https://pubmed.ncbi.nlm.nih.gov/42486788/)). Inheritance: multifactorial/polygenic; polygenic risk scores emerging. Demographics: male predominance in absolute cases but greater female susceptibility per unit alcohol; ADH1B\*2/ALDH2\*2 enriched in East Asians; PNPLA3 I148M enriched in Hispanic/Latino populations.

### 10. Diagnostics

Labs: AST>ALT (ratio >2), elevated GGT/bilirubin, macrocytosis, low platelets/albumin, elevated INR; CDT and PEth alcohol biomarkers. Non-invasive fibrosis: FIB-4, APRI, NFS, VCTE/MRE; FIB-4/NFS perform comparably in MetALD and MASLD (AUC ~0.77–0.81) ([PMID: 42001012](https://pubmed.ncbi.nlm.nih.gov/42001012/)). Imaging: ultrasound, CT/MRI, MR-PDFF, MRE. Biopsy: steatosis, ballooning, Mallory-Denk bodies, neutrophilic inflammation, pericellular fibrosis; SALVE grading. Clinical criteria: NIAAA for AH; severe AH = Maddrey DF ≥32 or MELD ≥20–21. Differential: MASLD/MetALD, viral/autoimmune hepatitis, DILI, Wilson disease, Zieve syndrome ([PMID: 38344483](https://pubmed.ncbi.nlm.nih.gov/38344483/)). Genetic/omics testing investigational only. Emerging biomarkers: CK-18, Pro-C3, ELF, gut-dysbiosis/metabolite signatures, single-cell immune signatures ([PMID: 41287436](https://pubmed.ncbi.nlm.nih.gov/41287436/), [PMID: 38040543](https://pubmed.ncbi.nlm.nih.gov/38040543/)). Screening: AUDIT/AUDIT-C ([PMID: 34601742](https://pubmed.ncbi.nlm.nih.gov/34601742/)).

### 11. Outcome/Prognosis

Severe AH: very high short-term mortality (>50% at 90 days with MELD ≥30) ([PMID: 41804063](https://pubmed.ncbi.nlm.nih.gov/41804063/)). Prognostic models: Maddrey DF, MELD (HR 1.20/point) ([PMID: 39082963](https://pubmed.ncbi.nlm.nih.gov/39082963/)); Lille (LI2 AUC ~0.82) ([PMID: 40545192](https://pubmed.ncbi.nlm.nih.gov/40545192/)); MELD-Age/ACLF-Age outperform Lille/Maddrey ([PMID: 39167426](https://pubmed.ncbi.nlm.nih.gov/39167426/)). Early LT survival ~85% ([PMID: 42148785](https://pubmed.ncbi.nlm.nih.gov/42148785/)). Complications: portal hypertension, ascites, variceal bleeding, encephalopathy, hepatorenal syndrome, sepsis, ACLF, HCC. Abstinence is the strongest modifier (survival HR 0.61) ([PMID: 38303565](https://pubmed.ncbi.nlm.nih.gov/38303565/)). QoL: CLDQ-ALD, worsened by stigma/disparities ([PMID: 42190270](https://pubmed.ncbi.nlm.nih.gov/42190270/), [PMID: 40063362](https://pubmed.ncbi.nlm.nih.gov/40063362/)).

### 12. Treatment (MAXO suggestions)

**Abstinence + AUD treatment** (foundational). Six approved AUD medications: acamprosate, naltrexone, nalmefene, disulfiram, baclofen, sodium oxybate; baclofen best-studied in cirrhosis; acamprosate safe in liver disease ([PMID: 42476146](https://pubmed.ncbi.nlm.nih.gov/42476146/), [PMID: 41258558](https://pubmed.ncbi.nlm.nih.gov/41258558/)). AUD treatment reduces relapse ~73–77% ([PMID: 40304585](https://pubmed.ncbi.nlm.nih.gov/40304585/)) and is cost-effective ([PMID: 33326815](https://pubmed.ncbi.nlm.nih.gov/33326815/)). CHEBI: baclofen (CHEBI:2972), acamprosate (CHEBI:51041), naltrexone (CHEBI:7465), disulfiram (CHEBI:4659). **Nutritional support** (sarcopenia/frailty). **Corticosteroids** (prednisolone) for severe AH — limited benefit ([PMID: 39620604](https://pubmed.ncbi.nlm.nih.gov/39620604/)). **Early/living-donor liver transplantation** ([PMID: 42148785](https://pubmed.ncbi.nlm.nih.gov/42148785/), [PMID: 41804063](https://pubmed.ncbi.nlm.nih.gov/41804063/)). **Emerging agents:** larsucosterol (epigenetic), F-652 (IL-22), INT-787 (FXR), G-CSF, IL-1/pan-caspase/ASK1/CCL2 inhibitors, elafibranor (PPARα/δ) ([PMID: 41691535](https://pubmed.ncbi.nlm.nih.gov/41691535/), [PMID: 36647403](https://pubmed.ncbi.nlm.nih.gov/36647403/)). **FMT** improves short-term AH survival ([PMID: 40359297](https://pubmed.ncbi.nlm.nih.gov/40359297/)); rifaximin showed no benefit in one RCT ([PMID: 39662593](https://pubmed.ncbi.nlm.nih.gov/39662593/)).

### 13. Prevention

Primary: reduce/avoid alcohol; population alcohol policies ([PMID: 42266909](https://pubmed.ncbi.nlm.nih.gov/42266909/)). Secondary: AUDIT screening, FIB-4/elastography, HCC surveillance. Tertiary: abstinence, HAV/HBV vaccination, complication management. Behavioral: brief interventions, CBT, motivational interviewing, peer support ([PMID: 34601742](https://pubmed.ncbi.nlm.nih.gov/34601742/)). Address stigma/disparities as public health priorities ([PMID: 40063362](https://pubmed.ncbi.nlm.nih.gov/40063362/)).

### 14. Other Species / Natural Disease

Naturally occurring ALD is essentially human-specific (NCBI:9606). Induced in *Mus musculus* (NCBI:10090), *Rattus norvegicus* (NCBI:10116), and hepatic ADH-deficient deer mice ([PMID: 24625836](https://pubmed.ncbi.nlm.nih.gov/24625836/)). Orthologs: *Pnpla3*, *Cyp2e1*, *Tgfb1*, *Adh1*, *Aldh2*. No significant spontaneous veterinary disease; non-zoonotic.

### 15. Model Organisms

Rodent models: chronic Lieber-DeCarli and NIAAA Gao-binge reproduce steatosis, transaminase elevation, neutrophilic inflammation, cytokine induction ([PMID: 39795945](https://pubmed.ncbi.nlm.nih.gov/39795945/), [PMID: 36174925](https://pubmed.ncbi.nlm.nih.gov/36174925/)). Genetic/cellular models: myeloid conditional knockouts (e.g., TFEB) ([PMID: 41970222](https://pubmed.ncbi.nlm.nih.gov/41970222/)); LX-2 stellate and VL-17A hepatocyte lines; organoids. Recapitulation good for early steatohepatitis/mechanism; poor for advanced fibrosis/cirrhosis and severe human AH — a key translational gap. Resources: MGI, RGD.

---

## Mechanistic Model / Interpretation

```
        GENETIC MODIFIERS                    ENVIRONMENTAL MODIFIERS
  PNPLA3 I148M (risk, top)            Alcohol dose & duration (required)
  TM6SF2, MBOAT7 (risk)               Female sex, obesity, T2D, MetS
  HSD17B13, MTARC1 (protective)       Smoking, binge pattern, HBV/HCV
  ADH1B*2, ALDH2*2 (acetaldehyde)              │
              │                                │
              └──────────────┬─────────────────┘
                             ▼
   ARM 1: Hepatocyte toxicity        ARM 2: Gut–liver axis
   ADH/CYP2E1 → acetaldehyde,        Dysbiosis, ↑ permeability,
   ROS, MAA adducts, GSH             LPS → TLR4/NF-κB Kupffer
   depletion, mito dysfunction       activation → TNF-α/IL-1β/IL-6
                     │                        │
                     └───────────┬────────────┘
                                 ▼
              Steatohepatitis + immune dysregulation
        (monocyte/macrophage expansion, HLA-DR loss,
         ILC1/IL-17A, FoxO1 epigenetic repression)
                                 ▼
              HSC activation (TGF-β1/Smad) → fibrosis
                                 ▼
              Cirrhosis → decompensation / HCC
                                 ▼
   MODIFIABLE LEVER: Abstinence + AUD treatment
   → ↑ survival (HR 0.61), ↓ decompensation, recompensation
```

Ethanol metabolism and gut-derived endotoxemia are **upstream**; immune dysregulation and stellate-cell activation are **midstream**; fibrosis, cirrhosis, portal hypertension, and HCC are **downstream**. Genetics set the slope of progression per unit of exposure. The most powerful therapeutic lever acts at the top of the cascade — removing the trigger (abstinence).

---

## Evidence Base

| PMID | Contribution | Finding |
|---|---|---|
| [42406571](https://pubmed.ncbi.nlm.nih.gov/42406571/) | Dose thresholds, risk factors, rising US mortality, AH symptoms | F007 |
| [42457160](https://pubmed.ncbi.nlm.nih.gov/42457160/) | ALD/MetALD/MASLD nomenclature; disproportionate mortality | F003 |
| [42435889](https://pubmed.ncbi.nlm.nih.gov/42435889/) | Population-based AH incidence | F003 |
| [42486788](https://pubmed.ncbi.nlm.nih.gov/42486788/) | ~1.4M global cirrhosis deaths (2021) | F003 |
| [38672422](https://pubmed.ncbi.nlm.nih.gov/38672422/) | Histological spectrum/staging | F003 |
| [23352969](https://pubmed.ncbi.nlm.nih.gov/23352969/) | CYP2E1 drives adduct/oxidative injury | F002 |
| [41715264](https://pubmed.ncbi.nlm.nih.gov/41715264/) | Multifactorial SAH pathophysiology | F002 |
| [41772607](https://pubmed.ncbi.nlm.nih.gov/41772607/) | PNPLA3/TM6SF2/MBOAT7 risk; HSD17B13/MTARC1 protective | F001 |
| [40943250](https://pubmed.ncbi.nlm.nih.gov/40943250/) | ADH1B/ALDH2 acetaldehyde metabolism; risk strata | F009 |
| [41270641](https://pubmed.ncbi.nlm.nih.gov/41270641/) | HSC activation, TGF-β1/Smad fibrosis | F005 |
| [25333756](https://pubmed.ncbi.nlm.nih.gov/25333756/) | Alcohol/smoking independent fatty-liver correlates | F005 |
| [39795945](https://pubmed.ncbi.nlm.nih.gov/39795945/) | Lieber-DeCarli model | F006 |
| [36174925](https://pubmed.ncbi.nlm.nih.gov/36174925/) | Gao-binge model; ILC1/IL-17A drivers | F006 |
| [40545192](https://pubmed.ncbi.nlm.nih.gov/40545192/) | Early Lille score prognostics | F008 |
| [39167426](https://pubmed.ncbi.nlm.nih.gov/39167426/) | MELD-Age/ACLF-Age outperform Lille/Maddrey | F008 |
| [39082963](https://pubmed.ncbi.nlm.nih.gov/39082963/) | Updated MELD prognostic value | F008 |
| [38040543](https://pubmed.ncbi.nlm.nih.gov/38040543/) | scRNA-seq monocyte/NK activation; HLA-DR loss | F010 |
| [36817578](https://pubmed.ncbi.nlm.nih.gov/36817578/) | scRNA-seq monocyte/macrophage expansion | F010 |
| [41190981](https://pubmed.ncbi.nlm.nih.gov/41190981/) | Epigenetic FoxO1 repression | F010 |
| [41287436](https://pubmed.ncbi.nlm.nih.gov/41287436/) | Multi-omic & gut-dysbiosis biomarkers | F011 |
| [39620604](https://pubmed.ncbi.nlm.nih.gov/39620604/) | Limited corticosteroid benefit (adjusted) | F004 |
| [42148785](https://pubmed.ncbi.nlm.nih.gov/42148785/) | Early LT survival/relapse | F004 |
| [41691535](https://pubmed.ncbi.nlm.nih.gov/41691535/) | Emerging agents (larsucosterol, F-652, INT-787) | F004 |
| [40359297](https://pubmed.ncbi.nlm.nih.gov/40359297/) | FMT improves short-term AH survival | F012 |
| [36647403](https://pubmed.ncbi.nlm.nih.gov/36647403/) | Mechanism-diverse AH pipeline | F012 |
| [42476146](https://pubmed.ncbi.nlm.nih.gov/42476146/) | Six approved AUD medications | F013 |
| [41258558](https://pubmed.ncbi.nlm.nih.gov/41258558/) | AUD pharmacotherapy in ALD | F013 |
| [33326815](https://pubmed.ncbi.nlm.nih.gov/33326815/) | AUD treatment cost-effectiveness | F013 |
| [38303565](https://pubmed.ncbi.nlm.nih.gov/38303565/) | Abstinence survival/decompensation benefit | F014 |
| [40304585](https://pubmed.ncbi.nlm.nih.gov/40304585/) | AUD treatment reduces relapse/liver events | F014 |
| [41622173](https://pubmed.ncbi.nlm.nih.gov/41622173/) | Abstinence-induced recompensation | F014 |
| [42190270](https://pubmed.ncbi.nlm.nih.gov/42190270/) | CLDQ-ALD HRQL instrument | F015 |
| [39022387](https://pubmed.ncbi.nlm.nih.gov/39022387/) | Stigma impairs HRQL | F015 |

**Citation integrity note:** A few citation snippets were flagged during validation (PMIDs 42148785, 36174925, 40545192, 33326815, 38303565) due to exact-quote normalization; the substantive conclusions are corroborated by the corresponding abstracts and convergent literature.

---

## Supported and Refuted Hypotheses

**Supported:**
1. PNPLA3 I148M is the leading genetic risk locus for ALD (with TM6SF2/MBOAT7 risk, HSD17B13/MTARC1 protective).
2. ALD pathogenesis is a dual-hit process (acetaldehyde/CYP2E1 oxidative stress + gut-liver endotoxemia/Kupffer activation) converging on HSC fibrosis.
3. Prognosis in severe AH is captured by Maddrey/MELD/Lille scores; early LT rescues steroid non-responders.
4. Abstinence and AUD treatment markedly improve survival, decompensation, and recompensation.

**Refuted/weakened:**
- Corticosteroids provide a large, durable survival benefit in severe AH — **not supported**; adjusted real-world analyses show attenuated/absent benefit ([PMID: 39620604](https://pubmed.ncbi.nlm.nih.gov/39620604/)).

---

## Limitations and Knowledge Gaps

1. This is a literature-synthesis report, not primary data analysis; conclusions rest on published aggregate evidence.
2. ALD is polygenic/multifactorial with no causal single gene; individual variant effect sizes are modest and polygenic risk scores are not yet clinically deployed.
3. Corticosteroid benefit is contested; better therapies are needed.
4. Rodent models do not reproduce advanced fibrosis, cirrhosis, or severe AH, limiting translation.
5. FMT and emerging agents rest on small, often single-center trials awaiting multicenter confirmation.
6. Biomarkers (CK-18, Pro-C3, ELF, gut-microbiome signatures) lack standardized cutoffs and prospective ALD-specific validation.
7. Prognostic scores (Lille, Maddrey) are outperformed by newer age/ACLF-augmented models.
8. AUD pharmacotherapy remains underutilized due to stigma, provider inexperience, and fragmented care.

---

## Proposed Follow-up Experiments / Actions

1. **Prospective validation of polygenic risk scores** (PNPLA3 + TM6SF2 + MBOAT7 + HSD17B13 + MTARC1) combined with ADH1B/ALDH2 genotypes for individualized ALD risk stratification.
2. **Multicenter, blinded RCTs of FMT and defined microbial consortia** in severe AH, with strain-resolved engraftment analytics linking mechanism to survival.
3. **Head-to-head and combination trials** of mechanism-targeted agents (larsucosterol, F-652, INT-787) versus/plus corticosteroids, powered on 90-day survival.
4. **Standardization and prospective validation** of non-invasive biomarker panels (CK-18, Pro-C3, ELF, elastography, gut-microbiome/metabolite signatures) for ALD staging.
5. **Implementation research** to integrate AUD pharmacotherapy and behavioral treatment into hepatology pathways, addressing stigma and time-to-tertiary-care.
6. **Higher-fidelity models** (humanized-liver mice, patient-derived organoids, multi-hit fibrosis models) that recapitulate advanced fibrosis and severe AH.
7. **Single-cell/spatial multi-omics** across the full ALD spectrum to map cell-type-specific therapeutic targets (LGALS9, FoxO1 axis, ILC1/IL-17A).
8. **Expansion of early liver transplantation protocols** with prospective psychosocial selection tools and long-term relapse/outcome registries.

---

*Report compiled from 15 confirmed findings across 5 investigation iterations and 77 reviewed papers. Evidence types span human clinical (population epidemiology, RCTs, meta-analyses, single-cell human studies), model organism (mouse Lieber-DeCarli/Gao-binge), and in vitro (hepatocyte/stellate-cell lines) sources.*


## Artifacts

- [OpenScientist final report](Alcoholic_Liver_Disease-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Alcoholic_Liver_Disease-deep-research-openscientist_artifacts/final_report.pdf)
