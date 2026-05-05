---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-05-05T07:01:43.636638'
end_time: '2026-05-05T07:40:59.484883'
duration_seconds: 2355.85
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Arterial Tortuosity Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 1
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 15
    timeout: 5400
citation_count: 26
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Arterial Tortuosity Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Arterial Tortuosity Syndrome** covering all of the
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

# Comprehensive Disease Characteristics Report: Arterial Tortuosity Syndrome

---

## Summary

**Arterial Tortuosity Syndrome (ATS; OMIM #208050)** is an ultra-rare autosomal recessive connective tissue disorder caused by biallelic loss-of-function mutations in *SLC2A10*, which encodes the facilitative glucose transporter GLUT10. GLUT10 functions as a dehydroascorbic acid (DAA) transporter across endomembranes, and its deficiency leads to impaired intracellular ascorbate compartmentalization. This molecular defect triggers a cascade of downstream pathology including oxidative stress, defective extracellular matrix (ECM) assembly with fragmented elastic fibers and disorganized collagen, compromised mitochondrial function in vascular smooth muscle cells, and dysregulated TGF-β signaling — collectively resulting in the hallmark vascular phenotype of tortuosity, elongation, stenosis, and aneurysm formation of large and medium-sized arteries.

Clinically, ATS presents in infancy or early childhood with widespread arterial tortuosity and stenoses, connective tissue manifestations (skin hyperextensibility, joint hypermobility, keratoconus), and additional features such as diaphragmatic hernia. As of 2023, approximately 106 genetically confirmed individuals have been reported worldwide, establishing ATS as one of the rarest heritable connective tissue disorders. The largest cohort study (102 patients) demonstrated that cardiovascular prognosis is more favorable than initially believed, with the neonatal and infancy period representing the most critical window for life-threatening events. No unequivocal vascular dissections or ruptures have been documented. Management centers on cardiovascular surveillance, beta-blocker therapy to reduce hemodynamic stress, and surgical or catheter-based intervention for complications such as pulmonary artery stenosis or aortic root aneurysm.

This report synthesizes evidence from 39 primary literature sources, structured databases (OMIM, Orphanet, HPO, ClinVar), and clinical cohort studies to provide a comprehensive disease knowledge base entry covering all 15 mandated disease characteristic domains.

---

## 1. Disease Information

### Overview

Arterial Tortuosity Syndrome is a rare, monogenic connective tissue disorder primarily affecting the vascular system. It was first described clinically approximately 55 years ago (Ertugrul, 1967) and its genetic basis was elucidated in 2006 when Coucke et al. identified mutations in *SLC2A10* as the causative defect ([PMID: 16550171](https://pubmed.ncbi.nlm.nih.gov/16550171/)). ATS is characterized by generalized tortuosity, elongation, and stenosis of large and medium-sized arteries, with a propensity for aneurysm formation. Patients also display connective tissue features overlapping with Ehlers-Danlos syndromes and Loeys-Dietz syndrome.

### Key Identifiers

| Database | Identifier |
|----------|-----------|
| **OMIM** | #208050 |
| **Orphanet** | ORPHA:3342 |
| **MONDO** | MONDO:0009005 |
| **ICD-10** | Q27.8 (Other specified congenital malformations of peripheral vascular system) |
| **MeSH** | C537373 |
| **Gene (HGNC)** | SLC2A10 (HGNC:13445) |
| **NCBI Gene** | 81031 |
| **UniProt** | O95528 (GTR10_HUMAN) |
| **Chromosomal Location** | 20q13.12 |

### Synonyms and Alternative Names

- Arterial Tortuosity Syndrome (ATS)
- Tortuosity of systemic arteries
- Arterial tortuosity (MeSH)

### Information Sources

Information is derived from **aggregated disease-level resources** (OMIM, Orphanet, GeneReviews) and individual case reports/series from published literature. The largest systematic cohort study encompasses 102 patients from 92 families (Beyens et al. 2018, [PMID: 29323665](https://pubmed.ncbi.nlm.nih.gov/29323665/)). A 2025 longitudinal study (CLARITY) provides the most recent prospective cardiovascular data on 14 patients ([PMID: 40613586](https://pubmed.ncbi.nlm.nih.gov/40613586/)).

---

## 2. Etiology

### Disease Causal Factors

ATS is a **monogenic (Mendelian) disorder** caused by biallelic (homozygous or compound heterozygous) loss-of-function mutations in the *SLC2A10* gene. There are no known environmental or infectious causes.

As stated in the original discovery paper: *"Mutations in one of these genes, SLC2A10, encoding the facilitative glucose transporter GLUT10, were identified in six ATS families. GLUT10 deficiency is associated with upregulation of the TGFbeta pathway in the arterial wall"* ([PMID: 16550171](https://pubmed.ncbi.nlm.nih.gov/16550171/)).

### Risk Factors

#### Genetic Risk Factors
- **Biallelic pathogenic variants in SLC2A10**: The sole known cause. Over 30 distinct pathogenic variants have been reported across different ethnic groups.
- **Consanguinity**: Significantly increases risk given autosomal recessive inheritance. Multiple reported families are consanguineous, particularly in Middle Eastern, North African, South Asian, and Mediterranean populations ([PMID: 29323665](https://pubmed.ncbi.nlm.nih.gov/29323665/); [PMID: 37619836](https://pubmed.ncbi.nlm.nih.gov/37619836/)).
- **Carrier status in parents**: Both parents must be carriers (heterozygous) for affected offspring; 25% recurrence risk per pregnancy.

#### Environmental Risk Factors
- No environmental risk factors have been identified for ATS development. As a fully penetrant Mendelian disorder, the disease is determined by genotype.

### Protective Factors

#### Genetic Protective Factors
- No specific modifier alleles or protective variants have been identified in humans.
- Notably, the ability of mice to endogenously synthesize ascorbic acid (via L-gulonolactone oxidase, encoded by *Gulo*) appears to protect Slc2a10 knockout mice from the full ATS phenotype. Humans lack functional *GULO* and cannot synthesize ascorbate, contributing to disease severity ([PMID: 32307537](https://pubmed.ncbi.nlm.nih.gov/32307537/)).

#### Environmental Protective Factors
- No confirmed environmental protective factors. It has been hypothesized that adequate ascorbic acid intake may have modifying effects given the ascorbate compartmentalization hypothesis, but this has not been clinically validated.

### Gene-Environment Interactions

The interplay between GLUT10 deficiency and the human inability to synthesize ascorbic acid represents a critical gene–environment (nutrient) interaction that likely determines disease severity. Mice with intact ascorbic acid synthesis via *Gulo* are protected from the full disease phenotype even when lacking GLUT10, while Gulo;Slc2a10 double knockout mice that cannot synthesize ascorbate show compromised ECM and mitochondrial defects: *"Altogether, our data add evidence that ATS is an ascorbate compartmentalization disorder, but additional factors underlying the observed phenotype in humans remain to be determined"* ([PMID: 32307537](https://pubmed.ncbi.nlm.nih.gov/32307537/)).

---

## 3. Phenotypes

### Cardiovascular Phenotypes

| Phenotype | HPO Term | Frequency | Onset | Severity | Progression |
|-----------|----------|-----------|-------|----------|-------------|
| Arterial tortuosity (large/medium arteries) | HP:0005116 | >95% | Congenital/neonatal | Moderate-severe | Stable to progressive |
| Aortic root dilation/aneurysm | HP:0002616 | ~71.4% (CLARITY) | Infancy-childhood | Variable | Progressive (stable z-scores) |
| Pulmonary artery stenosis | HP:0004415 | Frequent | Infancy | Moderate-severe | May require intervention |
| Aortic coarctation | HP:0001680 | Occasional | Congenital | Severe | May require surgery |
| Intracranial arterial tortuosity | HP:0005116 | Common | Congenital | Variable | Stable |
| Ischemic stroke | HP:0002140 | Rare | Childhood-young adult | Severe | Episodic |
| Neonatal intracranial bleeding | HP:0007420 | Rare | Neonatal | Severe | Acute |

The CLARITY longitudinal study reported that *"aortic root dilation was present in 71.4%; branch pulmonary artery (BPA) dimensions were mixed between dilated and hypoplastic"* ([PMID: 40613586](https://pubmed.ncbi.nlm.nih.gov/40613586/)). The largest cohort study documented: *"Stenoses, tortuosity, and aneurysm formation are widespread occurrences. Severe but rare vascular complications include early and aggressive aortic root aneurysms, neonatal intracranial bleeding, ischemic stroke, and gastric perforation"* ([PMID: 29323665](https://pubmed.ncbi.nlm.nih.gov/29323665/)).

### Connective Tissue Phenotypes

| Phenotype | HPO Term | Frequency | Onset | Severity |
|-----------|----------|-----------|-------|----------|
| Skin hyperextensibility | HP:0001030 | Very frequent | Congenital | Mild-moderate |
| Joint hypermobility | HP:0001382 | Very frequent | Congenital | Mild-moderate |
| Dysmorphic facial features | HP:0001999 | Frequent | Congenital | Mild |
| Keratoconus | HP:0000563 | Occasional | Childhood-adolescence | Progressive |
| Diaphragmatic hernia | HP:0000776 | Frequent (~15-20%) | Congenital/neonatal | Severe |
| Inguinal/umbilical hernia | HP:0000023 / HP:0001537 | Frequent | Infancy | Mild-moderate |
| Skeletal abnormalities | HP:0000924 | Frequent | Childhood | Variable |
| Microcephaly | HP:0000252 | Occasional | Congenital | Mild |
| Congenital contractures | HP:0002803 | Occasional | Congenital | Variable |

### Respiratory Phenotypes

| Phenotype | HPO Term | Frequency | Onset | Severity |
|-----------|----------|-----------|-------|----------|
| Infant respiratory distress syndrome (IRDS) | HP:0002643 | Frequent | Neonatal | Severe |
| Dyspnea/cyanosis (from PA involvement) | HP:0002094 | Occasional | Infancy | Variable |

### Other Rare Phenotypes

| Phenotype | HPO Term | Frequency |
|-----------|----------|-----------|
| Complex uropathy | HP:0000079 | Rare |
| Bilateral hip dislocation | HP:0001374 | Rare |
| Stomach displacement into thorax | HP:0002579 | Rare |
| Gastric perforation | — | Very rare |

*"A patient with microcephaly and a complex uropathy and two cases with diaphragmatic hernia are noticed."* ([PMID: 37619836](https://pubmed.ncbi.nlm.nih.gov/37619836/))

### Quality of Life Impact

ATS significantly impacts quality of life, particularly in childhood, due to:
- Cardiovascular surveillance burden (repeated imaging, echocardiography)
- Potential need for surgical interventions (pulmonary artery reconstruction, aortopexy)
- Joint laxity affecting mobility and musculoskeletal function
- Risk of cerebrovascular events limiting physical activity
- Respiratory complications in the neonatal period
- Psychosocial burden of a chronic rare disease

No formal QoL studies (EQ-5D, SF-36, PROMIS) specific to ATS have been published. This represents a significant gap in the literature.

---

## 4. Genetic/Molecular Information

### Causal Gene

- **Gene**: *SLC2A10* (Solute Carrier Family 2 Member 10)
- **HGNC ID**: HGNC:13445
- **NCBI Gene ID**: 81031
- **OMIM Gene**: *606145
- **Chromosomal Location**: 20q13.12
- **Protein**: GLUT10 (Facilitative Glucose Transporter Member 10), 541 amino acids, 12 predicted transmembrane domains
- **UniProt**: O95528

### Pathogenic Variants

#### Variant Types Reported

ATS-causing variants span the full spectrum of loss-of-function mutations:

| Variant (cDNA) | Protein Change | Type | Population | Reference |
|----------------|---------------|------|------------|-----------|
| c.243C>G | p.Ser81Arg (rs80358230) | Missense | Arab | [PMID: 36578839](https://pubmed.ncbi.nlm.nih.gov/36578839/) |
| c.173C>T | p.Ala58Val | Missense | — | [PMID: 40027906](https://pubmed.ncbi.nlm.nih.gov/40027906/) |
| c.899T>G | p.Leu300Trp | Missense | — | [PMID: 37619836](https://pubmed.ncbi.nlm.nih.gov/37619836/) |
| c.1309G>A | p.Glu437Lys | Missense | — | [PMID: 31203799](https://pubmed.ncbi.nlm.nih.gov/31203799/) |
| c.417T>A | p.Tyr139Ter | Nonsense | — | [PMID: 37619836](https://pubmed.ncbi.nlm.nih.gov/37619836/) |
| c.510G>A | p.Trp170Ter | Nonsense | — | [PMID: 37619836](https://pubmed.ncbi.nlm.nih.gov/37619836/) |
| c.756C>A | p.Cys252Ter | Nonsense | Kurdish | [PMID: 18818946](https://pubmed.ncbi.nlm.nih.gov/18818946/) |

Additional frameshift and splice-site variants have been reported (see ClinVar entries for *SLC2A10*).

#### Variant Classification
- All disease-causing variants are classified as **pathogenic** or **likely pathogenic** per ACMG/AMP guidelines.
- The disorder shows strict genotype-phenotype correlation: biallelic loss-of-function variants are required for disease manifestation.

#### Allele Frequency
- Pathogenic variants in *SLC2A10* are extremely rare or absent in population databases (gnomAD, 1000 Genomes).
- Some founder mutations are enriched in specific populations (e.g., p.Ser81Arg in Arab populations; [PMID: 35302653](https://pubmed.ncbi.nlm.nih.gov/35302653/)).

#### Functional Consequences
All known pathogenic variants result in **loss of function** of GLUT10 through:
- Premature protein truncation (nonsense, frameshift)
- Misfolding or impaired membrane insertion (missense)
- Loss of substrate transport activity
- Re-expression of GLUT10 in patient fibroblasts rescues the cellular phenotype ([PMID: 26376865](https://pubmed.ncbi.nlm.nih.gov/26376865/))

All pathogenic variants are **germline** in origin. No somatic mutations have been reported.

### Modifier Genes

No specific modifier genes have been identified in humans. However, the variable expressivity observed even among siblings with identical mutations suggests genetic modifiers or stochastic developmental factors influence disease severity. At the species level, *GULO* (L-gulonolactone oxidase) status serves as a major modifier — humans are pseudogene carriers (non-functional *GULO*), exacerbating GLUT10 deficiency effects compared to mice that retain functional Gulo ([PMID: 32307537](https://pubmed.ncbi.nlm.nih.gov/32307537/)).

### Epigenetic Information

No specific epigenetic modifications (DNA methylation, histone modifications, chromatin changes) have been described in ATS. Transcriptomic studies show dysregulation of genes involved in oxidative stress response and ECM homeostasis, but dedicated epigenomic profiling has not been performed.

### Chromosomal Abnormalities

ATS is not caused by chromosomal abnormalities. No large-scale structural variants (aneuploidy, translocations, inversions) are associated with the disease. All causative mutations are point mutations or small indels within *SLC2A10*.

---

## 5. Environmental Information

### Environmental Factors

ATS is a purely genetic disorder. **No environmental toxins, radiation, pollution, or occupational exposures** are known to cause or contribute to disease development.

### Lifestyle Factors

While no lifestyle factors cause ATS, clinical management recommends:
- **Avoidance of contact sports and intense isometric exercise** to reduce hemodynamic stress on weakened arterial walls
- **Blood pressure management** to reduce risk of aneurysm progression
- Adequate vitamin C intake may be theoretically important given the ascorbate compartmentalization hypothesis, but this remains clinically unvalidated

### Infectious Agents

Not applicable. ATS is not caused or triggered by any infectious agent.

---

## 6. Mechanism / Pathophysiology

### Overview: The Pathophysiological Cascade

The pathogenesis of ATS involves a multi-layered molecular cascade from the primary genetic defect to clinical manifestation:

```
SLC2A10 biallelic mutations
        ↓
GLUT10 protein loss-of-function
        ↓
Impaired dehydroascorbic acid (DAA) transport across endomembranes
        ↓
Reduced intracellular ascorbate in ER/mitochondria
        ↓
┌───────────────────┬────────────────────────┬──────────────────────┐
│                   │                        │                      │
▼                   ▼                        ▼                      ▼
Defective collagen  Impaired elastin     Oxidative stress     Mitochondrial
hydroxylation       assembly             (↑ ROS, ↑ lipid      dysfunction
(↓ prolyl/lysyl    (fragmented           peroxidation)        (compromised
hydroxylase         elastic fibers)      via altered PPARγ     respiration in
activity)                                                      VSMCs)
│                   │                        │                      │
└───────────────────┴────────────────────────┘                      │
                    ↓                                               │
        ECM disorganization                                         │
        (↑ collagen deposition,                                     │
         ↓ elastic fiber integrity)                                 │
                    ↓                                               │
        Non-canonical TGF-β signaling  ←────────────────────────────┘
        (αvβ3 integrin → p125FAK → p60Src → p38 MAPK)
                    ↓
        Vascular wall weakening
                    ↓
        Arterial tortuosity, elongation, stenosis, aneurysm
```

### Molecular Pathways

#### TGF-β Signaling (GO:0007179)

The original discovery paper demonstrated *"GLUT10 deficiency is associated with upregulation of the TGFbeta pathway in the arterial wall"* ([PMID: 16550171](https://pubmed.ncbi.nlm.nih.gov/16550171/)). However, subsequent work has significantly refined this understanding. In ATS fibroblasts, the primary TGF-β dysregulation occurs through a **non-canonical pathway** mediated by the αvβ3 integrin, involving p125FAK, p60Src, and p38 MAPK signaling, rather than the canonical SMAD2/3 pathway ([PMID: 29587413](https://pubmed.ncbi.nlm.nih.gov/29587413/); [PMID: 26376865](https://pubmed.ncbi.nlm.nih.gov/26376865/)).

Importantly, histological analysis of end-stage skin and vascular tissue from ATS patients did **not** show increased canonical TGF-β signaling markers (pSMAD2/CTGF) ([PMID: 29323665](https://pubmed.ncbi.nlm.nih.gov/29323665/)), and TGF-β signaling was unaltered in the Gulo;Slc2a10 double knockout mouse ([PMID: 32307537](https://pubmed.ncbi.nlm.nih.gov/32307537/)). This suggests tissue-specific and temporal differences in TGF-β pathway involvement, and that canonical TGF-β upregulation may not be the primary driver of disease in all contexts.

#### Ascorbate Metabolism (GO:0019852)

GLUT10 has been confirmed as a DAA transporter: *"The present results demonstrate that GLUT10 is a DAA transporter and DAA transport is diminished in the endomembranes of fibroblasts from ATS patients"* ([PMID: 27153185](https://pubmed.ncbi.nlm.nih.gov/27153185/)). Intracellular ascorbate is required as a cofactor for prolyl and lysyl hydroxylases that catalyze collagen cross-linking and for enzymes involved in elastin assembly. ATS has accordingly been characterized as an **"ascorbate compartmentalization disorder"** ([PMID: 31621376](https://pubmed.ncbi.nlm.nih.gov/31621376/); [PMID: 32307537](https://pubmed.ncbi.nlm.nih.gov/32307537/)).

- **CHEBI Terms**: CHEBI:29073 (L-ascorbic acid), CHEBI:17242 (dehydroascorbic acid)

#### Oxidative Stress (GO:0006979)

Studies on ATS fibroblasts demonstrated *"a marked increase in ROS-induced lipid peroxidation sustained by altered PPARγ function, which contributes to the redox imbalance and the compensatory antioxidant activity of ALDH1A1"* ([PMID: 26376865](https://pubmed.ncbi.nlm.nih.gov/26376865/)). The oxidative stress is a direct consequence of impaired intracellular ascorbate, which normally serves as a major intracellular antioxidant.

#### Integrin Signaling (GO:0007229)

In ATS fibroblasts, the αvβ3 integrin is preferentially recruited due to loss of the fibronectin-ECM and its canonical α5β1 integrin receptor. This integrin activates downstream signaling through p125FAK, p60Src, and p38 MAPK, contributing to ECM disarray and altered cell behavior ([PMID: 29587413](https://pubmed.ncbi.nlm.nih.gov/29587413/)).

### Cellular Processes

#### Extracellular Matrix Organization (GO:0030198)

Electron microscopy of ATS skin biopsies revealed: *"Large spaces were observed among the collagen fibrils…suggesting disorganization of the collagen structures. Furthermore, elastin fiber contents and their thickness are reduced…In small muscular arteries in the skin from ATS patients, discontinuous internal elastic lamina, lack of myofilaments, and disorganized medial smooth muscle cells with vacuolated cytoplasm are present"* ([PMID: 35302653](https://pubmed.ncbi.nlm.nih.gov/35302653/)). The largest cohort study confirmed: *"EM of skin EF shows a fragmented elastin core and a peripheral mantle of microfibrils of random directionality"* ([PMID: 29323665](https://pubmed.ncbi.nlm.nih.gov/29323665/)).

#### Mitochondrial Function (GO:0007005)

Zebrafish studies showed that *"a large proportion of the genes, which were specifically dysregulated after glut10 depletion gene and not by tgfbr1 inhibition, play a major role in mitochondrial function"* ([PMID: 22116938](https://pubmed.ncbi.nlm.nih.gov/22116938/)). The Gulo;Slc2a10 double knockout mouse confirmed compromised mitochondrial respiration in smooth muscle cells ([PMID: 32307537](https://pubmed.ncbi.nlm.nih.gov/32307537/)).

### Protein Dysfunction

GLUT10 is a 541-amino acid transmembrane protein with 12 predicted transmembrane domains. In silico modeling identified potential substrate binding site residues including PRO531, GLU507, GLU437, and TRP432, with a highly recurrent point mutation (c.1309G>A, p.Glu437Lys) located directly in the predicted binding site region ([PMID: 31203799](https://pubmed.ncbi.nlm.nih.gov/31203799/)).

### Metabolic Changes

- Perturbation of pathways controlling cell energy balance ([PMID: 26376865](https://pubmed.ncbi.nlm.nih.gov/26376865/))
- Altered glucose metabolism (GLUT10 belongs to the glucose transporter family, though its primary in vivo substrate appears to be DAA)
- Impaired ascorbate-dependent hydroxylation reactions affecting collagen and elastin biosynthesis

### Immune System Involvement

No primary immune dysfunction is described in ATS. Arterial wall inflammation may be secondary to ECM disruption and oxidative stress, but this has not been formally studied.

### Tissue Damage Mechanisms

- **Oxidative stress**: ROS-induced lipid peroxidation damaging vascular wall
- **Mechanical stress**: Turbulent blood flow through tortuous vessels increases shear stress
- **Elastic fiber fragmentation**: Progressive weakening of arterial wall integrity
- **Fibrosis**: Compensatory collagen deposition with disorganized architecture

### Biochemical Abnormalities

- **Transporter dysfunction**: Loss of GLUT10-mediated DAA transport across endomembranes
- **Functional enzyme deficiency**: Impaired intracellular ascorbate-dependent enzymes (prolyl 4-hydroxylase, lysyl hydroxylase) due to substrate compartmentalization failure (not systemic enzyme deficiency)

### Molecular Profiling

- **Transcriptomics**: Gene expression profiling of ATS fibroblasts revealed dysregulation of genes involved in TGF-β signaling, ECM homeostasis, cell energy balance, and oxidative stress response ([PMID: 26376865](https://pubmed.ncbi.nlm.nih.gov/26376865/)). Zebrafish transcriptome analysis showed high correlation between slc2a10 knockdown and tgfbr1 inhibition profiles, plus specific dysregulation of mitochondrial function genes ([PMID: 22116938](https://pubmed.ncbi.nlm.nih.gov/22116938/)).
- **Proteomics/Metabolomics/Lipidomics**: No systematic studies have been published.
- **Single-cell analysis, spatial transcriptomics, multi-omics**: Not yet applied to ATS.
- **Functional genomics screens**: Not reported for ATS.

### Key GO Terms for Biological Processes

- GO:0030198 — Extracellular matrix organization
- GO:0007179 — Transforming growth factor beta receptor signaling pathway
- GO:0006979 — Response to oxidative stress
- GO:0007229 — Integrin-mediated signaling pathway
- GO:0007005 — Mitochondrion organization
- GO:0019852 — L-ascorbic acid metabolic process
- GO:0071560 — Cellular response to transforming growth factor beta stimulus

### Key Cell Types Involved

| Cell Type | CL Term | Role in Pathogenesis |
|-----------|---------|---------------------|
| Vascular smooth muscle cell | CL:0000359 | Primary affected cell; mitochondrial dysfunction, ECM production defects, disorganized morphology |
| Fibroblast | CL:0000057 | Oxidative stress, non-canonical TGF-β signaling, ECM disarray, altered integrin signaling |
| Vascular endothelial cell | CL:0002543 | Altered angiogenesis, hemodynamic stress response |

---

## 7. Anatomical Structures Affected

### Organ Level

#### Primary Organs

| Organ System | Structures | UBERON Term |
|-------------|-----------|-------------|
| **Cardiovascular** | Aorta, pulmonary arteries, carotid arteries, subclavian arteries, intracranial arteries | UBERON:0000947 (aorta), UBERON:0002012 (pulmonary artery) |
| **Integumentary** | Skin (hyperextensibility) | UBERON:0002097 (skin of body) |
| **Musculoskeletal** | Joints (hypermobility), skeleton | UBERON:0000982 (skeletal joint) |

#### Secondary Organ Involvement

| Organ System | Structures | Mechanism |
|-------------|-----------|-----------|
| **Respiratory** | Lungs (IRDS), diaphragm (hernia) | Connective tissue defect, pulmonary artery stenosis |
| **Nervous** | Brain (stroke, intracranial bleeding) | Cerebrovascular complications from tortuosity |
| **Ocular** | Cornea (keratoconus) | Connective tissue weakness |
| **Gastrointestinal** | Stomach (perforation, displacement) | Connective tissue defect |
| **Urogenital** | Kidneys/ureters (uropathy) | Connective tissue defect |

**Body systems involved**: Cardiovascular (primary), musculoskeletal, integumentary, ocular, respiratory, gastrointestinal, nervous (secondary).

### Tissue and Cell Level

- **Arterial tunica media** (UBERON:0002036): Elastic fibers fragmented, smooth muscle cells disorganized with vacuolated cytoplasm, discontinuous internal elastic lamina, lack of myofilaments ([PMID: 35302653](https://pubmed.ncbi.nlm.nih.gov/35302653/))
- **Dermis**: Collagen fibrils disorganized with large inter-fibrillar spaces; reduced elastin content and thickness
- **Connective tissue** (UBERON:0002384): Systemic ECM disorganization

**Specific cell populations targeted:**
- Vascular smooth muscle cells (CL:0000359): Disorganized, vacuolated, lacking myofilaments
- Fibroblasts (CL:0000057): Altered ECM production, oxidative stress
- Endothelial cells (CL:0002543): Secondary to vascular wall disruption

### Subcellular Level

- **Endoplasmic reticulum** (GO:0005783): Site of collagen hydroxylation requiring ascorbate; GLUT10 transports DHA across ER membranes
- **Mitochondria** (GO:0005739): Compromised respiration in GLUT10-deficient cells
- **Extracellular matrix** (GO:0031012): Fragmented elastic fibers, disorganized collagen
- **Plasma membrane** (GO:0005886): Altered integrin signaling (αvβ3 vs. α5β1)
- **Endomembrane system** (GO:0012505): Impaired DAA transport across endomembranes

### Localization

- **Bilateral and generalized**: Arterial tortuosity affects arteries throughout the body symmetrically
- **Predominantly supra-aortic involvement** noted in some patients: *"Regarding the vascular involvement, a predominant supra-aortic involvement stands out...All presented severe tortuosity of the intracranial arteries"* ([PMID: 37619836](https://pubmed.ncbi.nlm.nih.gov/37619836/))
- **Specific UBERON terms**: UBERON:0000947 (aorta), UBERON:0002012 (pulmonary artery), UBERON:0001624 (carotid artery), UBERON:0001533 (subclavian artery), UBERON:0003496 (head blood vessel)

---

## 8. Temporal Development

### Onset

- **Typical age of onset**: **Congenital** — arterial tortuosity is present from birth
- **HPO**: HP:0003577 (Congenital onset)
- **Onset pattern**: Congenital/chronic — the structural vascular defect is developmental, though clinical complications may present acutely
- Prenatal detection is possible via ultrasound as early as 22 weeks' gestation: *"Prenatal ultrasound scanning at 29 weeks of gestation of the first fetus showed obvious tortuous and elongated of the aortic arch, ductus arteriosus, left and right pulmonary arteries"* ([PMID: 34384376](https://pubmed.ncbi.nlm.nih.gov/34384376/))
- Clinical diagnosis typically occurs in infancy-early childhood (median diagnosis age 3.3 years per CLARITY study, [PMID: 40613586](https://pubmed.ncbi.nlm.nih.gov/40613586/))

### Progression

- **Disease course**: Chronic, lifelong
- **Progression rate**: Variable; aortic dimensions increase with somatic growth but z-scores remain relatively stable
- **Disease course pattern**: Progressive structural changes superimposed on a chronic baseline
- **Disease duration**: Chronic lifelong; no remission

**Critical period**: The **neonatal and infancy period** (first 1-2 years of life) is the most critical for life-threatening events. As stated by Callewaert et al.: *"Our data confirm that the cardiovascular prognosis in ATS is less severe than previously reported and that the first years of life are the most critical for possible life-threatening events"* ([PMID: 25373504](https://pubmed.ncbi.nlm.nih.gov/25373504/)).

### Patterns

- **No spontaneous remission**: ATS does not remit
- **Stability**: After surviving infancy, many patients stabilize clinically. Some arterial stenoses may improve over time, though tortuosity is permanent.
- Connective tissue features (joint laxity, skin hyperextensibility) persist lifelong
- Keratoconus may progress during childhood/adolescence
- Risk of cerebrovascular events may extend into young adulthood ([PMID: 34847858](https://pubmed.ncbi.nlm.nih.gov/34847858/))

---

## 9. Inheritance and Population

### Epidemiology

- **Prevalence**: Ultra-rare; estimated <1 per 1,000,000. Orphanet classifies prevalence as <1/1,000,000.
- As of 2023, only **~106 individuals** with genetically confirmed ATS had been reported worldwide ([PMID: 37619836](https://pubmed.ncbi.nlm.nih.gov/37619836/)).
- **Incidence**: Unknown; no population-based incidence data available.

### Inheritance and Genetic Features

| Feature | Detail |
|---------|--------|
| **Inheritance pattern** | Autosomal recessive (AR); HP:0000007 |
| **Penetrance** | Complete for vascular features (tortuosity) in individuals with biallelic variants |
| **Expressivity** | Highly variable — even among siblings with identical mutations |
| **Genetic anticipation** | Not observed (not a repeat expansion disorder) |
| **Germline mosaicism** | Not documented, though theoretically possible |
| **Consanguinity role** | Significant — many reported families are consanguineous |
| **Carrier frequency** | Unknown; extremely low given disease rarity |

*"Arterial tortuosity syndrome (ATS) is a rare congenital disorder characterized by elongation and tortuosity of the aorta and mid-sized arteries. Additional features typical of connective tissue disorders are usually present, but the clinical presentation of the syndrome can extensively change."* ([PMID: 39827853](https://pubmed.ncbi.nlm.nih.gov/39827853/))

### Founder Effects

The **p.Ser81Arg (c.243C>G, rs80358230)** variant appears to be a founder mutation in Arab populations. Faiyaz-Ul-Haque et al. studied 48 patients with this specific mutation from Arab families ([PMID: 35302653](https://pubmed.ncbi.nlm.nih.gov/35302653/); [PMID: 36578839](https://pubmed.ncbi.nlm.nih.gov/36578839/)). Enrichment of ATS cases in populations with high rates of consanguinity (Middle Eastern, North African, South Asian, Mediterranean) is well documented.

### Population Demographics

- **Affected populations**: Reported worldwide across diverse ethnic groups including Arab, Kurdish, Turkish, Italian, Macedonian, Indian, Japanese, Qatari, and European populations
- **Geographic distribution**: Global, but clusters in regions with higher consanguinity rates
- **Sex ratio**: Both sexes equally affected. In the CLARITY study, 64% were male (9/14), but the small sample size limits interpretation ([PMID: 40613586](https://pubmed.ncbi.nlm.nih.gov/40613586/)).
- **Age distribution**: Diagnosis typically in infancy-early childhood; some patients now diagnosed prenatally

---

## 10. Diagnostics

### Clinical Tests

#### Imaging Studies (Primary Diagnostic Modality)

- **CT Angiography (CTA)**: Gold standard for demonstrating arterial tortuosity, elongation, stenosis, and aneurysm formation. Shows tortuosity of aorta, pulmonary arteries, carotid arteries, subclavian arteries, and intracranial vessels.
- **Echocardiography**: Essential for monitoring aortic root dimensions and pulmonary artery gradients. Serial measurements allow z-score tracking.
- **MR Angiography (MRA)**: Non-ionizing alternative for vascular imaging, particularly useful in children and for intracranial vasculature.
- **Prenatal ultrasound**: Can detect arterial tortuosity as early as 22 weeks' gestation. *"The key points of prenatal ultrasound diagnosis of ATS are the elongation and tortuosity of the large and medium sized arteries"* ([PMID: 34384376](https://pubmed.ncbi.nlm.nih.gov/34384376/)).

#### Laboratory Tests

- No specific blood biomarkers for ATS diagnosis or monitoring
- Routine metabolic panel typically normal
- No validated circulating biomarkers exist

#### Biopsy/Pathology Findings

Skin biopsy with electron microscopy shows disease-specific abnormalities:
- Fragmented elastic fibers with fragmented elastin core
- Peripheral mantle of microfibrils with random directionality
- Disorganized collagen fibrils with increased inter-fibrillar spacing
- In small muscular arteries: discontinuous internal elastic lamina, lack of myofilaments, disorganized medial smooth muscle cells with vacuolated cytoplasm ([PMID: 35302653](https://pubmed.ncbi.nlm.nih.gov/35302653/))

### Genetic Testing

#### Recommended Approach

1. **First-line**: Targeted *SLC2A10* gene sequencing when ATS is clinically suspected
2. **Alternative**: Connective tissue disorder / hereditary thoracic aortic disease (HTAD) gene panel including *SLC2A10* alongside *FBN1*, *TGFBR1/2*, *SMAD3*, *COL3A1*, etc. ([PMID: 39456956](https://pubmed.ncbi.nlm.nih.gov/39456956/))
3. **Whole exome sequencing (WES)**: Useful when clinical presentation is atypical or broader differential needed. *"Whole exome sequencing (WES) was performed eight months after birth, two heterozygous variants of SLC2A10 gene was detected in newborn and their father and mother, respectively"* ([PMID: 34384376](https://pubmed.ncbi.nlm.nih.gov/34384376/))
4. **Whole genome sequencing (WGS)**: Also effective but not typically first-line
5. **Prenatal genetic testing**: Available for families with known mutations (CVS, amniocentesis)

CMA, karyotyping, FISH, mitochondrial DNA testing, and repeat expansion testing are not applicable to ATS diagnosis.

### Clinical Criteria and Differential Diagnosis

No formal standardized diagnostic criteria (e.g., Ghent-like criteria) exist for ATS. Diagnosis is based on:
1. Clinical features: Generalized arterial tortuosity on imaging + connective tissue features
2. Genetic confirmation: Biallelic pathogenic variants in *SLC2A10*

**Key differential diagnoses:**

| Condition | Distinguishing Features | Gene(s) |
|-----------|------------------------|---------|
| **Loeys-Dietz syndrome** | AD inheritance; hypertelorism, cleft palate/bifid uvula, more aggressive aortopathy | *TGFBR1*, *TGFBR2*, *SMAD3*, *TGFB2*, *TGFB3* |
| **Marfan syndrome** | AD inheritance; lens subluxation, tall stature, arachnodactyly | *FBN1* |
| **Vascular EDS (type IV)** | AD; thin translucent skin, arterial/organ rupture | *COL3A1* |
| **Cutis laxa syndromes** | More prominent skin laxity, may have systemic features | *ELN*, *FBLN4*, *FBLN5*, *ATP6V0A2* |
| **Homocystinuria** | AR; intellectual disability, lens subluxation, thromboembolism | *CBS* |

([PMID: 25821090](https://pubmed.ncbi.nlm.nih.gov/25821090/); [PMID: 29979900](https://pubmed.ncbi.nlm.nih.gov/29979900/); [PMID: 37692180](https://pubmed.ncbi.nlm.nih.gov/37692180/))

### Screening

- **Newborn screening**: Not included in standard newborn screening programs
- **Carrier screening**: Available for at-risk family members; *"Notably, carrier testing for at-risk relatives is recommended to identify family members that may be affected by this condition"* ([PMID: 36578839](https://pubmed.ncbi.nlm.nih.gov/36578839/))
- **Cascade screening**: Recommended for at-risk family members once an index case is identified
- **Prenatal diagnosis**: Possible via CVS or amniocentesis when familial mutations are known, and via detailed fetal echocardiography/ultrasound

---

## 11. Outcome / Prognosis

### Survival and Mortality

- Earlier literature described ATS as having a high mortality rate due to major cardiovascular malformations
- More recent data demonstrate that the prognosis is **less severe than previously reported**: *"Our data confirm that the cardiovascular prognosis in ATS is less severe than previously reported and that the first years of life are the most critical for possible life-threatening events"* ([PMID: 25373504](https://pubmed.ncbi.nlm.nih.gov/25373504/))
- **First years of life** carry the highest risk of mortality from pulmonary artery stenosis, respiratory distress, intracranial hemorrhage, or aortic complications
- **No unequivocal vascular dissections or ruptures** have been documented, which is a critical distinguishing feature from vascular EDS and Loeys-Dietz syndrome ([PMID: 29323665](https://pubmed.ncbi.nlm.nih.gov/29323665/))
- No specific survival rate data (5-year, 10-year) are available due to disease rarity
- Many patients survive into adulthood; the oldest reported patients are in their 30s-40s ([PMID: 34847858](https://pubmed.ncbi.nlm.nih.gov/34847858/))

### Morbidity and Function

- Chronic cardiovascular surveillance burden
- Potential need for surgical interventions: *"Three patients underwent repeated BPA interventions, one patient had an aortopexy, and one patient had an aortic valve replacement. No patients had arterial dissections"* ([PMID: 40613586](https://pubmed.ncbi.nlm.nih.gov/40613586/))
- Joint hypermobility may cause chronic musculoskeletal pain
- Visual impairment from keratoconus
- Risk of cerebrovascular events even in young adulthood

### Complications

- Aortic root aneurysm (71.4% in CLARITY; may require valve/root replacement)
- Branch pulmonary artery stenosis (may require repeated catheter interventions or surgery)
- Ischemic stroke / transient ischemic attacks (rare but documented; [PMID: 34847858](https://pubmed.ncbi.nlm.nih.gov/34847858/))
- Neonatal intracranial hemorrhage (rare)
- Gastric perforation (rare)
- Infant respiratory distress syndrome
- Diaphragmatic hernia requiring surgical repair

### Prognostic Factors

- **Severity of neonatal presentation**: IRDS, intracranial bleeding, severe PA stenosis carry worst prognosis
- **Degree of pulmonary artery stenosis**: Determines need for intervention and risk of RV failure
- **Rate of aortic root dilation**: Requires longitudinal z-score monitoring
- **Access to specialized care**: Early referral to high-specialized centers improves outcomes
- **Specific mutation type**: Genotype-phenotype correlations are poorly established due to small numbers

---

## 12. Treatment

### Pharmacotherapy

#### Beta-Adrenergic Blockers (MAXO:0001298)

Beta-blockers (e.g., atenolol, propranolol) are first-line pharmacological treatment to reduce hemodynamic stress on arterial walls. *"To reduce hemodynamic stress on the arterial wall, beta-adrenergic blocking treatment was prescribed"* ([PMID: 37619836](https://pubmed.ncbi.nlm.nih.gov/37619836/)). The rationale is extrapolated from management of Marfan syndrome and other aortopathies — reducing heart rate and blood pressure decreases shear stress on tortuous and dilated vessels.

#### Angiotensin Receptor Blockers (MAXO:0001299)

Losartan (angiotensin II type 1 receptor blocker) has been proposed based on its TGF-β antagonist properties and efficacy in Marfan syndrome mouse models: *"In transgenic mouse models it was shown that losartan, an angiotensin II type 1 receptor with known inhibiting effects on TGFbeta, rescues the aortic phenotype"* ([PMID: 18630721](https://pubmed.ncbi.nlm.nih.gov/18630721/)). Clinical efficacy in ATS specifically is not yet established.

#### Antithrombotic Therapy

May be considered for secondary prevention of cerebrovascular events. One case report described treatment with recombinant tissue plasminogen activator (r-TPA) at 0.9 mg/kg for TIA with complete recovery ([PMID: 34847858](https://pubmed.ncbi.nlm.nih.gov/34847858/)).

#### Pharmacogenomics

No pharmacogenomic data specific to ATS are available.

### Surgical and Interventional (MAXO:0000004)

#### Pulmonary Artery Interventions
- Balloon angioplasty and stenting for pulmonary artery stenosis
- Total pulmonary arterial reconstruction for severe cases: *"underwent a pulmonary arterial surgical reconstruction at the age of 2 years old due to the development of pulmonary artery stenosis"* ([PMID: 38987788](https://pubmed.ncbi.nlm.nih.gov/38987788/))
- Surgical approaches may be preferred over transcatheter approaches, especially when peripheral arteries are involved
- Repeated interventions may be necessary

#### Aortic Surgery
- Aortopexy for symptomatic aortic tortuosity
- Aortic valve replacement when indicated
- Aortic root replacement for progressive aneurysmal dilation
- Coarctation repair when present

#### Diaphragmatic Hernia Repair
- Standard surgical repair when present (congenital diaphragmatic hernia)

### Advanced Therapeutics

#### Gene Therapy (Future Potential)
- No gene therapy trials currently registered for ATS
- In vitro proof-of-concept: re-expression of GLUT10 in patient fibroblasts rescued the cellular phenotype, normalizing redox homeostasis and PPARγ activity ([PMID: 26376865](https://pubmed.ncbi.nlm.nih.gov/26376865/))
- Given the autosomal recessive loss-of-function mechanism, gene replacement therapy is conceptually feasible but has not been developed

#### Ascorbate Supplementation (Hypothetical)
- Based on the ascorbate compartmentalization hypothesis, high-dose ascorbate supplementation could theoretically be beneficial
- However, the defect is in intracellular transport rather than systemic ascorbate levels
- No clinical trials exist

### Supportive and Rehabilitative (MAXO:0000502)

- **Genetic counseling** (MAXO:0000079): Essential for families regarding recurrence risk (25%) and carrier testing
- **Multidisciplinary follow-up**: Cardiology, ophthalmology, orthopedics, genetics, pulmonology
- **Physical therapy**: For joint hypermobility management
- **Ophthalmologic monitoring**: Regular eye examinations for keratoconus progression and management
- **Cardiovascular surveillance** (MAXO:0000127): Regular echocardiography and interval CTA/MRA

### Treatment Strategy

Management requires a **multidisciplinary approach** ([PMID: 37692180](https://pubmed.ncbi.nlm.nih.gov/37692180/)):
- Close monitoring of aortic root early in life
- Extensive vascular imaging afterwards
- Surveillance and prevention are key
- *"Our findings warrant attention for IRDS and diaphragmatic hernia, close monitoring of the aortic root early in life, and extensive vascular imaging afterwards"* ([PMID: 29323665](https://pubmed.ncbi.nlm.nih.gov/29323665/))

**Relevant MAXO terms:**
- MAXO:0000502 — Counseling
- MAXO:0000127 — Echocardiography
- MAXO:0000004 — Surgical procedure
- MAXO:0010033 — Medical management
- MAXO:0001298 — Beta-adrenergic antagonist therapy
- MAXO:0000079 — Genetic counseling

---

## 13. Prevention

### Primary Prevention

As a Mendelian genetic disorder, primary prevention of disease occurrence is limited to:
- **Genetic counseling** (MAXO:0000079) for consanguineous families and known carriers
- **Preimplantation genetic diagnosis (PGD)** for families with known mutations
- **Prenatal genetic testing** (CVS, amniocentesis) when familial mutations are established
- **Carrier screening** in populations with known founder mutations (e.g., p.Ser81Arg in Arab populations)

### Secondary Prevention (Early Detection)

- **Prenatal ultrasound screening**: Can detect arterial tortuosity as early as 22 weeks' gestation in at-risk pregnancies. *"When ATS is suspected prenatally, the newborn should be referred immediately after birth to a high specialized center for proper neonatal care"* ([PMID: 39827853](https://pubmed.ncbi.nlm.nih.gov/39827853/))
- **Cascade genetic testing**: For siblings and relatives of affected individuals
- **Neonatal vigilance**: Immediate referral to specialized center when ATS is suspected
- *"In case of confirmed ATS, parents should be counseled regarding the recurrence risk in other pregnancies"* ([PMID: 39827853](https://pubmed.ncbi.nlm.nih.gov/39827853/))

### Tertiary Prevention (Preventing Complications)

- Regular cardiovascular surveillance (echocardiography, vascular imaging)
- Beta-blocker therapy to reduce hemodynamic stress
- Activity modification to avoid extreme physical exertion and contact sports
- Ophthalmologic monitoring for keratoconus progression
- Cerebrovascular risk management and antiplatelet prophylaxis when indicated

### Immunization

Not applicable — ATS is not an infectious or immune-mediated disorder.

### Behavioral Interventions

- Avoidance of isometric exercises and contact sports
- Blood pressure monitoring and management
- Regular medical follow-up compliance

### Public Health

Given the ultra-rare nature of ATS (<1/1,000,000), population-level public health interventions are not practical. Awareness among pediatric cardiologists, geneticists, and prenatal sonographers is the most impactful public health measure.

---

## 14. Other Species / Natural Disease

### Naturally Occurring Disease

No naturally occurring animal disease equivalent to human ATS has been reported in veterinary literature or in the OMIA database. This is likely because most animals (including mice, rats, dogs, cats) retain functional L-gulonolactone oxidase (*Gulo*) and can synthesize ascorbic acid endogenously, compensating for any GLUT10 dysfunction.

### Orthologous Genes

| Species | Gene Symbol | NCBI Taxon |
|---------|------------|------------|
| Human (*Homo sapiens*) | *SLC2A10* | 9606 |
| Mouse (*Mus musculus*) | *Slc2a10* | 10090 |
| Zebrafish (*Danio rerio*) | *slc2a10* | 7955 |
| Rat (*Rattus norvegicus*) | *Slc2a10* | 10116 |

### Comparative Biology

The *SLC2A10/GLUT10* gene is highly conserved across vertebrates, suggesting an essential role in development. A critical species difference is that **mice (but not humans) can synthesize their own ascorbic acid** via the gulonolactone oxidase (*Gulo*) pathway. This likely explains why simple Slc2a10 mutant mice fail to recapitulate the human vascular phenotype, while the Gulo;Slc2a10 double knockout (which eliminates both GLUT10 and endogenous ascorbate synthesis) shows a more informative phenotype ([PMID: 32307537](https://pubmed.ncbi.nlm.nih.gov/32307537/)).

**Guinea pigs** and **some primates** share the human inability to synthesize ascorbic acid (non-functional *GULO*) and could theoretically manifest ATS-like phenotypes if *SLC2A10* were disrupted, but no such models exist.

### Transmission / Zoonotic Potential

Not applicable — ATS is a non-infectious genetic disorder with no zoonotic potential or cross-species transmission.

---

## 15. Model Organisms

### Mouse Models

#### Slc2a10 Missense Models (G128E, S150F)

- **Type**: ENU-induced knock-in (missense substitutions)
- **Phenotype recapitulation**: **None** — *"two mouse models, homozygous respectively for G128E and S150F missense substitutions in glut10 do not present any of the vascular, anatomical, or immunohistological abnormalities as encountered in human ATS patients"* ([PMID: 18693279](https://pubmed.ncbi.nlm.nih.gov/18693279/))
- **Limitation**: Mice synthesize endogenous ascorbic acid via Gulo, compensating for GLUT10 deficiency
- **NCBI Taxon**: 10090

#### Gulo;Slc2a10 Double Knockout Model

- **Type**: Double gene knockout (Slc2a10 KO + Gulo KO — abolishes endogenous ascorbate synthesis)
- **Phenotype recapitulation**: Partial — *"While Gulo;Slc2a10 double knock-out mice did not fully phenocopy human ATS, histological and immunocytochemical analysis revealed compromised extracellular matrix formation"* and mitochondrial dysfunction in smooth muscle cells ([PMID: 32307537](https://pubmed.ncbi.nlm.nih.gov/32307537/))
- **Key findings**: TGF-β signaling unaltered; supports ascorbate compartmentalization hypothesis
- **Significance**: Strongest animal model evidence that ATS is fundamentally an ascorbate compartmentalization disorder
- **Limitation**: Does not fully phenocopy human vascular tortuosity, suggesting additional human-specific factors

### Zebrafish Model

#### slc2a10 Morpholino Knockdown

- **Type**: Antisense morpholino oligonucleotide-mediated gene knockdown
- **Phenotype recapitulation**: Good — *"knockdown of slc2a10 using antisense morpholino oligonucleotide injection caused a wavy notochord and cardiovascular abnormalities with a reduced heart rate and blood flow"* ([PMID: 22116938](https://pubmed.ncbi.nlm.nih.gov/22116938/))
- **Key findings**: Cardiovascular phenotype partially phenocopied by TGF-β receptor (tgfbr1/alk5) small-molecule inhibitor; transcriptomic analysis revealed specific dysregulation of mitochondrial function genes distinct from tgfbr1 inhibition
- **NCBI Taxon**: 7955
- **Limitation**: Morpholino effects are transient; long-term vascular remodeling cannot be studied; zebrafish vascular anatomy differs significantly from human

### Cell-Based Models

#### Patient-Derived Dermal Fibroblasts

- **Type**: Primary skin fibroblasts from ATS patients
- **Applications**: Most extensively used in vitro model
- **Key findings**:
  - Demonstrated oxidative stress with ROS-induced lipid peroxidation and altered PPARγ function ([PMID: 26376865](https://pubmed.ncbi.nlm.nih.gov/26376865/))
  - Confirmed impaired DAA transport across endomembranes ([PMID: 27153185](https://pubmed.ncbi.nlm.nih.gov/27153185/))
  - Revealed non-canonical TGF-β signaling via αvβ3 integrin ([PMID: 29587413](https://pubmed.ncbi.nlm.nih.gov/29587413/))
  - GLUT10 re-expression normalizes phenotype (proof of concept for gene therapy)
- **Limitation**: In vitro system; does not capture in vivo hemodynamic forces, developmental context, or cell-cell interactions

### Model Summary

| Model | Species | Vascular Phenotype | ECM Defects | TGF-β Change | Overall Utility |
|-------|---------|--------------------|-------------|--------------|-----------------|
| Slc2a10 G128E/S150F | Mouse | None | None | Not observed | Limited |
| Gulo;Slc2a10 DKO | Mouse | Mild | Yes | Unaltered | Moderate |
| slc2a10 MO | Zebrafish | Yes (CV abnormalities) | Yes (notochord) | Reduced | Good (developmental) |
| Patient fibroblasts | Human | N/A | Yes | Non-canonical ↑ | Good (mechanistic) |

### Key Gap

No single model fully recapitulates the severe human vascular phenotype of ATS. This suggests that additional human-specific factors — including the obligate dependence on dietary ascorbate, hemodynamic forces during human cardiovascular development, and perhaps differences in elastic fiber assembly — contribute to disease manifestation.

---

## Mechanistic Model / Interpretation

### Integrated Mechanistic Framework

Synthesizing all available evidence, ATS is best understood as an **ascorbate compartmentalization disorder** with multi-pathway downstream consequences:

1. **Primary defect (upstream)**: Biallelic loss of GLUT10 → loss of DAA transport across endomembranes
2. **Proximal consequences**: Intracellular ascorbate deficiency in ER and mitochondria
3. **Intermediate pathology (4 parallel arms)**:
   - **ECM arm**: Impaired prolyl/lysyl hydroxylase activity → defective collagen hydroxylation → fragmented elastic fibers + disorganized collagen
   - **Redox arm**: Loss of intracellular antioxidant → ROS accumulation → lipid peroxidation → altered PPARγ function
   - **Mitochondrial arm**: Ascorbate deficiency in mitochondria → compromised electron transport chain → impaired VSMC energy metabolism
   - **Signaling arm**: ECM disarray + fibronectin loss → αvβ3 integrin recruitment → non-canonical TGF-β signaling via FAK/Src/p38 MAPK
4. **Convergent pathology (downstream)**: Vascular wall weakening → arterial tortuosity, elongation, stenosis, and aneurysm formation
5. **Human amplification factor**: Unlike most mammals, humans cannot synthesize ascorbate (non-functional *GULO*), making them uniquely vulnerable to GLUT10 deficiency

The canonical TGF-β/SMAD pathway, while highlighted in the original discovery paper, appears to be a secondary or context-dependent phenomenon rather than the primary driver. This is supported by: (a) absence of pSMAD2/CTGF upregulation in patient tissues, (b) unaltered TGF-β signaling in the Gulo;Slc2a10 double knockout mouse, and (c) non-canonical rather than canonical pathway activation in patient fibroblasts.

---

## Evidence Base

### Landmark Papers

| Paper | PMID | Key Contribution |
|-------|------|-----------------|
| Coucke et al. 2006, *Nat Genet* | [16550171](https://pubmed.ncbi.nlm.nih.gov/16550171/) | Discovery of *SLC2A10* as causative gene |
| Beyens et al. 2018, *Hum Mutat* | [29323665](https://pubmed.ncbi.nlm.nih.gov/29323665/) | Largest cohort (102 patients, 40 new families); comprehensive phenotyping |
| Callewaert et al. 2008, *Hum Mutat* | [18693279](https://pubmed.ncbi.nlm.nih.gov/18693279/) | Mouse model demonstrating species-specific differences |
| Willaert et al. 2012, *Hum Mol Genet* | [22116938](https://pubmed.ncbi.nlm.nih.gov/22116938/) | Zebrafish model; mitochondrial function link |
| Németh et al. 2016, *FEBS Lett* | [27153185](https://pubmed.ncbi.nlm.nih.gov/27153185/) | GLUT10 confirmed as DAA transporter |
| Boel et al. 2020, *Hum Mol Genet* | [32307537](https://pubmed.ncbi.nlm.nih.gov/32307537/) | Double KO mouse model; ascorbate compartmentalization |
| Zoppi et al. 2015, *Hum Mol Genet* | [26376865](https://pubmed.ncbi.nlm.nih.gov/26376865/) | Oxidative stress mechanism and non-canonical TGF-β in fibroblasts |
| Callewaert et al. 2008, *J Med Genet* | [25373504](https://pubmed.ncbi.nlm.nih.gov/25373504/) | Prognosis better than expected; infancy most critical |
| CLARITY study 2025 | [40613586](https://pubmed.ncbi.nlm.nih.gov/40613586/) | Longitudinal cardiovascular data; 71.4% aortic root dilation |
| Al-Khawaga et al. 2022, *Eur J Med Genet* | [35302653](https://pubmed.ncbi.nlm.nih.gov/35302653/) | Ultrastructural analysis of collagen and elastin in Arab patients |
| Zoppi et al. 2018, *Int J Mol Sci* | [29587413](https://pubmed.ncbi.nlm.nih.gov/29587413/) | αvβ3 integrin role in ATS fibroblasts |
| Hosen et al. 2020, *ACS Omega* | [31203799](https://pubmed.ncbi.nlm.nih.gov/31203799/) | In silico GLUT10 structure and substrate binding prediction |

### Supporting Clinical Literature

| Paper | PMID | Contribution |
|-------|------|-------------|
| Esmel-Vilomara et al. 2023 | [37619836](https://pubmed.ncbi.nlm.nih.gov/37619836/) | 4 new patients; novel variant p.Leu300Trp; supra-aortic involvement |
| Ekhator et al. 2023 | [37692180](https://pubmed.ncbi.nlm.nih.gov/37692180/) | Comprehensive review of ATS |
| Cotti Piccinelli et al. 2021 | [34847858](https://pubmed.ncbi.nlm.nih.gov/34847858/) | TIA in young adult with ATS; first r-TPA use |
| Liang et al. 2021 | [34384376](https://pubmed.ncbi.nlm.nih.gov/34384376/) | Prenatal ultrasound diagnosis in 2 siblings |
| Alshair et al. 2024 | [38987788](https://pubmed.ncbi.nlm.nih.gov/38987788/) | Pulmonary arterial reconstruction case report |
| Tunks et al. 2025 | [40027906](https://pubmed.ncbi.nlm.nih.gov/40027906/) | Novel p.Ala58Val variant; prenatal diagnosis keys |
| Ponziani et al. 2025 | [39827853](https://pubmed.ncbi.nlm.nih.gov/39827853/) | Concordant dichorionic twins with ATS |
| Debette & Germain 2014 | [24365320](https://pubmed.ncbi.nlm.nih.gov/24365320/) | Neurologic manifestations of connective tissue disorders |
| Al-Habeeb et al. 2024 | [36578839](https://pubmed.ncbi.nlm.nih.gov/36578839/) | Neonatal ATS case; p.Ser81Arg founder mutation |
| Loeys & De Paepe 2008 | [18630721](https://pubmed.ncbi.nlm.nih.gov/18630721/) | TGF-β pathway and losartan in aortic aneurysms |

---

## Limitations and Knowledge Gaps

1. **Ultra-rare disease with limited natural history data**: With only ~106 confirmed patients, long-term outcomes, genotype-phenotype correlations, and rare complications may be underestimated or incompletely characterized.

2. **No adequate animal model**: No single animal model fully recapitulates human ATS. Mouse models are limited by endogenous ascorbate synthesis, and zebrafish models are limited by developmental and anatomical differences.

3. **Pathomechanism incompletely understood**: The relative contributions of ascorbate compartmentalization, TGF-β signaling (canonical vs. non-canonical), oxidative stress, and mitochondrial dysfunction remain unclear. The observation that end-stage tissue shows no canonical TGF-β upregulation creates an apparent contradiction with the original discovery that needs resolution.

4. **No validated biomarkers**: No circulating biomarkers exist for disease monitoring, progression prediction, or treatment response assessment.

5. **No formal diagnostic criteria**: Unlike Marfan syndrome (Ghent criteria) or EDS (2017 criteria), ATS lacks standardized clinical diagnostic criteria.

6. **Treatment evidence is anecdotal**: No clinical trials have been conducted for any intervention. Beta-blocker and losartan use is extrapolated from other aortopathies. The potential role of ascorbate supplementation is speculative.

7. **No quality-of-life studies**: Formal patient-reported outcome measures (EQ-5D, SF-36, PROMIS) have not been applied to ATS cohorts.

8. **Omics data are sparse**: No large-scale transcriptomic, proteomic, metabolomic, or epigenomic profiling of ATS patient tissues has been published. Single-cell approaches have not been applied.

9. **Genotype-phenotype correlation poorly defined**: While variable expressivity is well documented, specific relationships between mutation type/position and disease severity have not been systematically analyzed.

10. **Prenatal natural history**: Few cases have been diagnosed prenatally, limiting understanding of fetal disease progression and optimal prenatal management strategies.

---

## Proposed Follow-up Experiments / Actions

### Short-Term (1-3 years)

1. **International ATS Registry**: Establish a prospective, multicenter registry to systematically collect phenotypic, genotypic, treatment, and outcome data across all known patients, building on the CLARITY initiative framework.

2. **Genotype-Phenotype Correlation Study**: Using registry data, analyze whether specific mutation types (truncating vs. missense), positions within *SLC2A10*, or zygosity status (homozygous vs. compound heterozygous) predict disease severity, complication rates, or specific phenotypic features.

3. **Circulating Biomarker Discovery**: Profile serum/plasma from ATS patients using targeted proteomics and metabolomics to identify potential biomarkers for disease activity (e.g., ECM turnover markers such as desmosine/isodesmosine for elastin degradation, oxidative stress markers such as 8-isoprostane, TGF-β pathway markers).

4. **Patient-Derived iPSC Vascular Models**: Generate iPSC lines from ATS patients, differentiate into vascular smooth muscle cells and endothelial cells, and use these to study vascular pathomechanisms and screen potential therapeutics in a human-relevant system.

### Medium-Term (3-5 years)

5. **Improved Mouse Model**: Generate a conditional *Slc2a10* knockout on a *Gulo*-null background with vascular-specific and temporally controlled deletion, combined with controlled dietary ascorbate restriction, to better model human ATS.

6. **Ascorbate Supplementation Pilot Study**: Design a controlled clinical study evaluating high-dose ascorbic acid supplementation in ATS patients, monitoring aortic root dimensions, arterial stiffness, vascular tortuosity indices, and circulating biomarkers as endpoints.

7. **Single-Cell RNA Sequencing**: Perform scRNA-seq on ATS patient skin biopsies and available vascular tissue to identify cell-type-specific transcriptional signatures, prioritize therapeutic targets, and understand the cellular heterogeneity of disease.

8. **TGF-β Pathway Dissection**: Use patient-derived fibroblasts and iPSC-derived vascular cells to systematically dissect canonical vs. non-canonical TGF-β signaling across different cell types and developmental stages, resolving the apparent contradiction between in vitro and in vivo findings.

### Long-Term (5+ years)

9. **Gene Therapy Development**: Explore AAV-mediated *SLC2A10* gene replacement in vascular smooth muscle cells, first validating in the improved mouse model, then progressing toward clinical translation. The in vitro proof-of-concept (GLUT10 re-expression rescuing fibroblast phenotype) is encouraging.

10. **Clinical Treatment Trial**: Based on biomarker and mechanistic data, design a randomized controlled trial of pharmacological intervention (losartan, high-dose ascorbate, or novel targeted therapy) in ATS patients, leveraging the international registry for recruitment.

11. **Formal Diagnostic Criteria Development**: Convene an international expert panel to establish standardized diagnostic criteria for ATS, analogous to Ghent criteria for Marfan syndrome, incorporating clinical, imaging, and genetic features.

---

*Report generated: 2026-05-05 | Based on analysis of 39 published studies and structured database resources | MONDO:0009005 | OMIM #208050*
