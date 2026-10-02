---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-01T21:10:30.077047'
end_time: '2026-10-01T21:24:16.418886'
duration_seconds: 826.34
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Severe X-linked Mitochondrial Encephalomyopathy
  mondo_id: MONDO:0010437
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
citation_count: 17
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Severe_X-linked_Mitochondrial_Encephalomyopathy-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Severe_X-linked_Mitochondrial_Encephalomyopathy-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Severe X-linked Mitochondrial Encephalomyopathy
- **MONDO ID:** MONDO:0010437 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Severe X-linked Mitochondrial Encephalomyopathy** covering all of the
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

# Severe X-linked Mitochondrial Encephalomyopathy (AIFM1-related, COXPD6): A Comprehensive Disease Characterization

**Disease:** Severe X-linked Mitochondrial Encephalomyopathy
**MONDO ID:** MONDO:0010437 · **OMIM:** #300816 (Combined Oxidative Phosphorylation Deficiency 6, COXPD6)
**Causal gene:** *AIFM1* (Xq26.1; HGNC:8768) · **Inheritance:** X-linked recessive
**Category:** Mendelian, ultra-rare primary mitochondrial disorder

---

## Summary

Severe X-linked mitochondrial encephalomyopathy (MONDO:0010437; OMIM #300816, **Combined Oxidative Phosphorylation Deficiency 6, COXPD6**) is an ultra-rare, X-linked recessive primary mitochondrial disease caused by pathogenic variants in ***AIFM1*** on chromosome Xq26.1. *AIFM1* encodes **Apoptosis-Inducing Factor (AIF)**, a 613-amino-acid, FAD-dependent NADH oxidoreductase that resides in the mitochondrial intermembrane space. The index "severe" allele is the in-frame deletion **p.Arg201del (R201del)**, identified by Ghezzi and colleagues in 2010 in two male infants with progressive mitochondrial encephalomyopathy born to monozygotic twin sisters and unrelated fathers — a pedigree that established the X-linked trait ([PMID: 20362274](https://pubmed.ncbi.nlm.nih.gov/20362274/)).

The disease arises from a **dual (two-branch) pathomechanism**. The first branch is **loss of AIF's vital, non-apoptotic role in supporting mitochondrial oxidative phosphorylation (OXPHOS)**: AIF promotes the mitochondrial import of MIA40/CHCHD4 and the assembly/stability of respiratory chain complexes, so its deficiency produces a combined OXPHOS defect (reduced complex I, III and IV activities), an energy deficit, and oxidative stress. The second branch is a **gain in regulated cell death via parthanatos** — a PARP-1 → poly(ADP-ribose) (PAR) → AIF/MIF → large-scale DNA fragmentation cascade that culminates in caspase-independent neuronal and myocyte death. Together these branches generate a typically fatal **infantile- or neonatal-onset encephalomyopathy** (developmental regression, drug-resistant seizures, hypotonia, lactic acidosis), frequently with **cardiomyopathy** and **sensorineural hearing loss**, within a broader *AIFM1* allelic spectrum that extends to milder, later-onset axonal neuropathy (Cowchock syndrome/CMTX4) and riboflavin-responsive cerebellar ataxia.

There is **no curative therapy**. Management is supportive and includes genotype-informed candidate cofactor/redox agents (riboflavin, Coenzyme Q10, thiamine — a "mito cocktail"), seizure control, cardiac heart-failure therapy, nutritional support, and rehabilitation, with careful perioperative/anesthetic planning. The **Harlequin (Hq) mouse**, which carries a proviral insertion that reduces AIF by 80–90%, is the key animal model: it reproduces complex I deficiency and progressive, cerebellum- and retina-predominant neurodegeneration, and has been used to demonstrate that mitochondrial injury is causal (upstream) to neuronal death and to test redox/antioxidant interventions.

---

## Key Findings

### Finding 1 — *AIFM1* mutations cause the disease (COXPD6, OMIM #300816)

Ghezzi et al. (2010) identified a disease-segregating X-linked *AIFM1* mutation — **c.601_603del, p.Arg201del (R201del)** — in two male infants with progressive mitochondrial encephalomyopathy. The pedigree (two affected boys born to monozygotic twin sisters and **unrelated** fathers) pointed unambiguously to X-linked inheritance rather than a shared autosomal or environmental cause. Patient fibroblasts showed a **combined respiratory chain defect with reduced complex III and complex IV but preserved complex I activities** at the fibroblast level, and re-expression of wild-type AIF rescued the biochemical defect. *AIFM1* maps to **Xq26.1**, and the clinical entity is catalogued as **Combined Oxidative Phosphorylation Deficiency 6 (COXPD6, OMIM #300816; MONDO:0010437)**.

> "We found a disease-segregating mutation in the X-linked AIFM1 gene, encoding the Apoptosis-Inducing Factor (AIF) mitochondrion-associated 1 precursor that deletes arginine 201 (R201 del)." — [PMID: 20362274](https://pubmed.ncbi.nlm.nih.gov/20362274/)

> "Fibroblasts from both showed reduction of respiratory chain (RC) cIII and cIV, but not of cI activities." — [PMID: 20362274](https://pubmed.ncbi.nlm.nih.gov/20362274/)

This is the foundational, human-clinical evidence establishing *AIFM1* R201del as the causal lesion for severe X-linked mitochondrial encephalomyopathy.

### Finding 2 — Dual pathomechanism: loss of OXPHOS support **plus** enhanced parthanatos

The same study demonstrated both arms of the mechanism. In AIF(R201del) fibroblasts, **staurosporine-induced parthanatos** (caspase-independent chromatin fragmentation) was **markedly increased**, and **re-expression of wild-type AIF restored respiratory chain activities** — simultaneously proving a pro-death gain of function and a loss of the OXPHOS-supporting function. Patient muscle showed numerous **TUNEL-positive, caspase-3-negative nuclei**, the histological signature of parthanatos in a disease-critical tissue. In vitro, R201del **decreases the stability of both mitochondrial AIF(mit) and soluble AIF(sol)** and **increases AIF(sol) DNA-binding affinity** (a prerequisite for the nuclear, pro-death activity). Mechanistically, AIF supports complex I assembly/stability by promoting mitochondrial import of **MIA40/CHCHD4**.

> "In AIF(R201 del) fibroblasts, staurosporine-induced parthanatos was markedly increased, whereas re-expression of AIF(wt) induced recovery of RC activities." — [PMID: 20362274](https://pubmed.ncbi.nlm.nih.gov/20362274/)

> "they channel electrons into the respiratory chain and, at least in animals, promote the import of Mia40 (named MIA40 or CHCHD4 in humans) and the assembly of complex I" — [PMID: 32769219](https://pubmed.ncbi.nlm.nih.gov/32769219/)

### Finding 3 — Broad allelic spectrum, from lethal infantile encephalomyopathy to later-onset neuropathy/ataxia

*AIFM1* variants produce a **phenotypic continuum** rather than a single syndrome:

| Phenotype | Representative variant | Key features | Evidence |
|---|---|---|---|
| Severe infantile mitochondrial encephalomyopathy (COXPD6) | p.Arg201del | Regression, seizures, lactic acidosis, early death | [PMID: 20362274](https://pubmed.ncbi.nlm.nih.gov/20362274/) |
| Early-onset axonal sensorimotor neuropathy with hearing loss | (various) | Neuropathy + deafness | [PMID: 28967629](https://pubmed.ncbi.nlm.nih.gov/28967629/) |
| Cowchock syndrome / CMTX4 | p.Glu493Val | Slowly progressive X-linked axonal neuropathy, deafness, cognitive impairment | [PMID: 23217327](https://pubmed.ncbi.nlm.nih.gov/23217327/) |
| Riboflavin-responsive X-linked cerebellar ataxia | p.Met340Thr, p.Thr141Ile | Childhood ataxia, partial riboflavin response | [PMID: 28967629](https://pubmed.ncbi.nlm.nih.gov/28967629/) |
| Severe multisystem disease, metabolic acidosis, early death | (X-linked *AIFM1*) | Multisystem pathology | [PMID: 34117073](https://pubmed.ncbi.nlm.nih.gov/34117073/) |

> "Mutations in the X-linked AIFM1 were reported in relation to two main phenotypes: a severe infantile mitochondrial encephalomyopathy and an early-onset axonal sensorimotor neuropathy with hearing loss." — [PMID: 28967629](https://pubmed.ncbi.nlm.nih.gov/28967629/)

> "Cowchock syndrome (CMTX4) is a slowly progressive X-linked recessive disorder with axonal neuropathy, deafness, and cognitive impairment." — [PMID: 23217327](https://pubmed.ncbi.nlm.nih.gov/23217327/)

Importantly, the ataxia end of the spectrum is **partially riboflavin-responsive**: in two patients, riboflavin (up to 200 mg/day for 12 months) decreased the ICARS ataxia score by 39% and 20%, respectively.

> "Ataxia score, decreased by 39% in patient 1 and 20% in patient 2" — [PMID: 28967629](https://pubmed.ncbi.nlm.nih.gov/28967629/)

### Finding 4 — The Harlequin (Hq) mouse recapitulates complex I deficiency and progressive neurodegeneration

The **Harlequin mouse** carries a proviral insertion in *Aifm1* that reduces AIF by **80–90%**, producing **severe complex I deficiency (40–50% reduction in complex I level/activity)** and **progressive neurodegeneration beginning ~3 months of age**, most pronounced in **cerebellum and retina** and extending to cortex, striatum, and thalamus, accompanied by oxidative-stress markers. Critically, El Ghouzzi et al. (2007) showed that **early mitochondrial degeneration precedes multifocal neuropathology**, establishing mitochondrial injury as a **cause rather than a consequence** of neuronal death — directly supporting the "upstream bioenergetic lesion" model of AIFM1 disease. AIF deficiency also **sensitizes dopaminergic neurons to MPTP** (a gene–environment interaction), reinforcing that AIF-linked complex I defects lower the threshold for neurodegeneration.

> "harlequin mice exhibiting an 80-90% global reduction in AIF protein are resistant to numerous forms of acute brain injury, they paradoxically undergo slow, progressive neurodegeneration beginning at three months of age" — [PMID: 23246553](https://pubmed.ncbi.nlm.nih.gov/23246553/)

> "degenerating mitochondria were observed in most cells in these structures, even in nondegenerating neurons, a finding that indicates mitochondrial injury is a cause rather than an effect of neuronal cell death" — [PMID: 17805014](https://pubmed.ncbi.nlm.nih.gov/17805014/)

### Finding 5 — Cardiomyopathy and manifesting heterozygous females with skewed X-inactivation

Although X-linked recessive, AIFM1 disease can manifest in **heterozygous females** when X-inactivation is skewed. Sandmann et al. (2026) reported the **first affected female** with a heterozygous *AIFM1* variant **c.506C>T (p.Pro169Leu)** and **extremely skewed X-inactivation (98:2)**, presenting with infantile-onset mitochondrial encephalomyopathy **and cardiomyopathy**: marked left-ventricular hypertrophy with preserved systolic function at 8 months, progressing to **dilated cardiomyopathy with systolic dysfunction** by 2.5 years, requiring heart-failure therapy. Cardiac involvement had previously been described in a handful of AIFM1 patients, predominantly as ventricular hypertrophy.

> "We report the first affected female with a heterozygous AIFM1 variant who developed infantile-onset mitochondrial encephalomyopathy and cardiomyopathy with initial ventricular hypertrophy, that progressed to left ventricular dilation and chronic heart failure." — [PMID: 42329587](https://pubmed.ncbi.nlm.nih.gov/42329587/)

> "Genetic testing identified a heterozygous AIFM1 variant, c.506C > T (p.Pro169Leu), with extremely skewed X-inactivation (98:2) in a female." — [PMID: 42329587](https://pubmed.ncbi.nlm.nih.gov/42329587/)

### Finding 6 — Neonatal-onset presentation, characteristic MRI, and the diagnostic pathway

Zambon et al. (2023) expanded the neonatal-onset spectrum, describing **drug-resistant multifocal seizures 6 hours after birth**, with brain MRI showing **prominent bilateral hemispheric brain swelling and widespread cortical and thalamic signal alteration with sparing of the basal nuclei**. Clinical exome sequencing identified a likely pathogenic variant **c.5T>C p.(Phe2Ser)** in the **mitochondrial targeting sequence**. Functional fibroblast studies showed **reduced AIFM1 protein and defective complex I, III and IV activities** (without protein mislocalization or precursor accumulation). The diagnostic workup integrated EEG, brain MRI/MR spectroscopy, metabolic screening, echocardiography, and clinical exome sequencing — a template for diagnosing this disease.

> "The patient presented with drug-resistant, electro-clinical, multifocal seizures 6 h after birth. Brain MRI revealed prominent brain swelling of both hemispheres and widespread signal alteration in large part of the cortex and of the thalami, with sparing of the basal nuclei." — [PMID: 37644805](https://pubmed.ncbi.nlm.nih.gov/37644805/)

> "Functional studies on cultured fibroblast showed a clear reduction in AIFM1 protein amount and defective activities of respiratory chain complexes I, III and IV." — [PMID: 37644805](https://pubmed.ncbi.nlm.nih.gov/37644805/)

### Finding 7 — The parthanatos cascade and AIF's reframing as an "OXPHOS-inducing factor"

Liu et al. (2022) detail **parthanatos** as a regulated cell-death program: **PARP-1 overactivation → PAR accumulation → PAR binding to AIF → AIF release from mitochondria → nuclear translocation of the AIF/MIF complex → MIF-mediated large-scale DNA fragmentation**. In parallel, Wischhof et al. (2022) reframe AIF as an **"OXPHOS-inducing factor"** whose principal physiological role is to promote the biogenesis and maintenance of the OXPHOS system — recasting AIFM1 disease as **primarily a bioenergetic disorder** on which a cell-death liability is superimposed.

> "PARP-1) overactivation, PAR accumulation, PAR binding to apoptosis-inducing factor (AIF), AIF release from the mitochondria, nuclear translocation of the AIF/macrophage migration inhibitory factor (MIF) complex, and MIF-mediated large-scale DNA fragmentation" — [PMID: 35000037](https://pubmed.ncbi.nlm.nih.gov/35000037/)

> "AIF contributes to cell survival by promoting biogenesis and maintenance of the mitochondrial oxidative phosphorylation (OXPHOS) system" — [PMID: 35994922](https://pubmed.ncbi.nlm.nih.gov/35994922/)

### Finding 8 — Genetics and inheritance

*AIFM1* (apoptosis-inducing factor mitochondria-associated 1; **UniProt O95831; NCBI Gene 9131; Ensembl ENSG00000156709; Xq26.1**) encodes a **613-amino-acid FAD-dependent NADH oxidoreductase**. Disease is **X-linked recessive**: affected males typically inherit the variant from carrier mothers; the founding Ghezzi pedigree demonstrated transmission through monozygotic twin sisters to sons by unrelated fathers. Reported pathogenic variants are **predominantly missense or small in-frame deletions** affecting the **FAD/NAD(H) oxidoreductase domain or the mitochondrial targeting sequence**: p.Arg201del (severe encephalomyopathy), p.Glu493Val (Cowchock/CMTX4), p.Met340Thr and p.Thr141Ile (riboflavin-responsive ataxia), p.Phe2Ser (neonatal, MTS), p.Pro169Leu (manifesting female, cardiomyopathy), and p.Gly308Glu. The disease is **ultra-rare** (fewer than ~30 families/individuals reported worldwide). Pathogenic/likely-pathogenic variants are classified per ACMG/AMP and are **essentially absent from gnomAD population controls**.

> "These patients were born from monozygotic twin sisters and unrelated fathers, suggesting an X-linked trait." — [PMID: 20362274](https://pubmed.ncbi.nlm.nih.gov/20362274/)

> "The disease locus was previously mapped to an 11 cM region at chromosome X: q24-q26." — [PMID: 23217327](https://pubmed.ncbi.nlm.nih.gov/23217327/)

### Finding 9 — Management is supportive; candidate redox/cofactor therapies only

No disease-modifying therapy is approved. Reported interventions include **riboflavin (vitamin B2, a FAD precursor)** up to 200 mg/day, which partially improved ataxia (ICARS −39% / −20%; Heimer 2018), and a combined **riboflavin + Coenzyme Q10 + thiamine "mito cocktail"** associated with clinical stabilization in a neonatal case (Zambon 2023). Preclinical candidates include the redox compound **methylene blue** (protective of AIF-deficient photoreceptors; Mekala 2019), the **SOD-mimetic tempol** (reversed MPTP susceptibility in Harlequin mice; Perier 2010), and **NADH supplementation** (proposed for mitochondrial-dysfunction neurodegeneration; Chen 2024). Supportive care encompasses antiepileptic drugs (seizures are frequently drug-resistant), nutritional/feeding support, heart-failure therapy for cardiomyopathy, and physical/occupational/speech rehabilitation. **Anesthetic caution is required**: total intravenous anesthesia with remimazolam has been reported for COXPD6 (Olakunle 2025).

> "Riboflavin, Coenzyme Q10 and thiamine supplementation was therefore given. At 6 months of age, the patient exhibited microcephaly but did not experience any further deterioration." — [PMID: 37644805](https://pubmed.ncbi.nlm.nih.gov/37644805/)

> "The protective role of the redox compound methylene blue" — [PMID: 30300862](https://pubmed.ncbi.nlm.nih.gov/30300862/)

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. A germline **pathogenic *AIFM1* variant** (e.g., p.Arg201del) is present on the X chromosome → **leads to** an altered AIF protein with reduced stability and altered redox/DNA-binding properties.
2. Reduced/dysfunctional AIF in the mitochondrial intermembrane space → **results in** impaired **MIA40/CHCHD4 import** and defective **respiratory-chain complex assembly/stability** (branch point A).
3. **Branch A (bioenergetic):** Defective OXPHOS → **leads to** a **combined complex I/III/IV deficiency**, reduced ATP output, and increased reactive oxygen species (oxidative stress) → **results in** energy failure in high-demand tissues (brain, heart, skeletal muscle, inner ear).
4. **Branch B (cell-death / parthanatos):** Cellular stress and PARP-1 overactivation → **leads to** PAR accumulation → PAR binds AIF → **AIF release from mitochondria** → nuclear translocation of the **AIF/MIF** complex → **MIF-mediated large-scale DNA fragmentation** → **results in** caspase-independent neuronal and myocyte death (evidenced by TUNEL+, caspase-3− nuclei in patient muscle). *This branch's quantitative contribution in human tissue is partly inferred from in-vitro and model data.*
5. Convergence of Branch A (energy failure) and Branch B (parthanatos) in the CNS → **leads to** encephalopathy: developmental regression, drug-resistant seizures, hypotonia, and characteristic MRI changes (hemispheric swelling, cortical/thalamic signal change, basal-nuclei sparing).
6. Energy failure and cell death in cardiomyocytes → **results in** cardiomyopathy (hypertrophic → dilated with heart failure).
7. Involvement of cochlear/neural tissue → **leads to** sensorineural hearing loss; involvement of peripheral axons (in milder alleles) → axonal sensorimotor neuropathy.
8. Progressive multi-organ bioenergetic failure with lactic acidosis → **results in** early death in severe infantile/neonatal cases.

```
        AIFM1 pathogenic variant (e.g., p.Arg201del) @ Xq26.1
                         │
            Unstable / dysfunctional AIF (IMS)
                         │
        ┌────────────────┴─────────────────┐
   BRANCH A                            BRANCH B
 (bioenergetic)                      (parthanatos)
        │                                  │
 ↓ MIA40/CHCHD4 import           PARP-1 overactivation
        │                                  │
 defective complex I/III/IV        PAR accumulation → binds AIF
 assembly & stability                      │
        │                          AIF released → nucleus
 ↓ ATP, ↑ ROS                      AIF/MIF complex
        │                                  │
 energy failure                    large-scale DNA fragmentation
        └───────────────┬──────────────────┘
                        ▼
        Neuronal + cardiomyocyte + myocyte death
                        ▼
   Encephalomyopathy · cardiomyopathy · hearing loss
   seizures · regression · lactic acidosis · early death
```

### Upstream vs. downstream

- **Upstream (initiating):** the *AIFM1* variant and the resulting loss of AIF's OXPHOS-supporting function. The Harlequin model confirms that mitochondrial injury is *causal* and precedes overt neuropathology ([PMID: 17805014](https://pubmed.ncbi.nlm.nih.gov/17805014/)).
- **Downstream (effector):** OXPHOS deficiency → ATP deficit/ROS; parthanatos → DNA fragmentation and caspase-independent death; organ-level manifestations (encephalopathy, cardiomyopathy, deafness, neuropathy).

### Cell types, compartments, and ontology suggestions

- **Subcellular (GO Cellular Component):** mitochondrial intermembrane space (GO:0005758), mitochondrial inner membrane (GO:0005743), respiratory chain complex I (GO:0005747), nucleus (GO:0005634, for the pro-death translocation).
- **Biological processes (GO):** mitochondrial electron transport / OXPHOS (GO:0006119), mitochondrial respiratory chain complex assembly (GO:0033108), parthanatos / DNA-damage-induced caspase-independent apoptosis, protein import into mitochondrial intermembrane space (GO:0045041), response to oxidative stress (GO:0006979), FAD binding / NADH dehydrogenase activity (GO:0003954).
- **Cell types (CL):** neuron (CL:0000540), cerebellar Purkinje cell (CL:0000121), retinal photoreceptor cell (CL:0000210), cardiac muscle cell / cardiomyocyte (CL:0000746), skeletal muscle fiber (CL:0000188), cochlear hair cell (CL:0000855).
- **Anatomy (UBERON):** brain (UBERON:0000955), cerebral cortex (UBERON:0000956), thalamus (UBERON:0001897), cerebellum (UBERON:0002037), heart / cardiac ventricle (UBERON:0000948 / UBERON:0002082), skeletal muscle (UBERON:0001134), cochlea (UBERON:0001844), retina (UBERON:0000966), peripheral nerve (UBERON:0001021).
- **Chemical entities (CHEBI):** FAD (CHEBI:16238), NADH (CHEBI:16908), riboflavin (CHEBI:17015), ubiquinone/CoQ10 (CHEBI:46245), thiamine (CHEBI:18385), methylene blue (CHEBI:6872), L-lactate (CHEBI:16651).
- **Treatment (NCIT):** Riboflavin (C737), Coenzyme Q10 (C1198), Thiamine (C933), Methylene Blue (C61585), Anticonvulsant Agent (C264), Supportive Care (C15184).

---

## Section-by-Section Synthesis

### 1. Disease Information
A concise overview: a severe, X-linked, infantile/neonatal-onset primary mitochondrial encephalomyopathy due to *AIFM1* deficiency, biochemically a combined OXPHOS deficiency (COXPD6). **Identifiers:** MONDO:0010437; OMIM #300816; gene *AIFM1* (HGNC:8768). **Synonyms/related:** Combined Oxidative Phosphorylation Deficiency 6 (COXPD6); AIFM1-related mitochondrial encephalomyopathy; AIF deficiency. The milder allelic entities (Cowchock syndrome/CMTX4; AIFM1-related ataxia) are distinct but share the gene. Information is derived from **aggregated disease-level resources and small case series/reports** rather than EHR-scale cohorts, reflecting the ultra-rare nature of the disease.

### 2. Etiology
**Primary cause:** monogenic — pathogenic *AIFM1* variants (X-linked recessive). **Genetic risk factors:** hemizygous pathogenic *AIFM1* variants in males; in females, a heterozygous variant **plus skewed X-inactivation** (e.g., 98:2) can manifest disease ([PMID: 42329587](https://pubmed.ncbi.nlm.nih.gov/42329587/)). **Environmental/modifier factors:** limited human data, but model data show AIF deficiency **sensitizes neurons to exogenous complex I inhibitors (MPTP)** — a demonstrated **gene–environment interaction** that lowers the neurodegeneration threshold ([PMID: 20695011](https://pubmed.ncbi.nlm.nih.gov/20695011/)). **Protective factors:** none genetically established; redox/antioxidant interventions (tempol in mice) partially protect in models. **Sex** is a strong determinant (males predominantly affected).

### 3. Phenotypes
Core phenotypes (with suggested HPO terms): developmental regression (HP:0002376), **seizures/drug-resistant epilepsy** (HP:0001250), **hypotonia** (HP:0001252), **lactic acidosis** (HP:0003128), **sensorineural hearing loss** (HP:0000407), **cardiomyopathy** (HP:0001638; hypertrophic HP:0001639, dilated HP:0001644), **psychomotor/developmental delay** (HP:0001263), **microcephaly** (HP:0000252), **cerebellar ataxia** (HP:0001251, milder alleles), **axonal sensorimotor neuropathy** (HP:0007002, milder alleles), **abnormal brain MRI** (HP:0002543). **Onset:** neonatal to infantile in the severe form; childhood/adult in milder alleles. **Severity:** severe to variable. **Progression:** progressive, often rapidly fatal in the severe form; slowly progressive in Cowchock/ataxia alleles. **Quality-of-life impact:** profound in the severe form (loss of milestones, refractory seizures, feeding difficulty, cardiac failure).

### 4. Genetic/Molecular Information
**Causal gene:** *AIFM1* (Xq26.1; OMIM *300169). **Protein:** AIF, 613 aa, FAD-dependent NADH oxidoreductase (UniProt O95831). **Variant classes:** predominantly **missense and small in-frame deletions** in the FAD/NAD(H) oxidoreductase domain or MTS; representative alleles listed in Finding 8. **Classification:** pathogenic/likely pathogenic (ACMG/AMP); **absent from gnomAD**. **Origin:** germline. **Functional consequence:** combined loss of OXPHOS support (loss of function for the vital role) with an **altered pro-death / DNA-binding gain** for the soluble form. **Epigenetic modifier:** **X-inactivation skewing** critically determines female manifestation. No recurrent large chromosomal abnormality is characteristic.

### 5. Environmental Information
No established infectious or primary environmental cause. The relevant environmental dimension is **gene–environment interaction**: in AIF-deficient models, **complex I inhibitor exposure (MPTP)** precipitates dopaminergic neurodegeneration that spares wild-type animals ([PMID: 20695011](https://pubmed.ncbi.nlm.nih.gov/20695011/)), implying mitochondrial toxins and metabolic stressors may aggravate the human phenotype in principle.

### 6. Mechanism / Pathophysiology
See the ordered causal chain and diagram above. Key pathways/processes: **OXPHOS/electron transport (complex I/III/IV)**, **MIA40/CHCHD4 mitochondrial import pathway**, **parthanatos (PARP-1/PAR/AIF/MIF)**, **oxidative stress**. AIF additionally participates in the **KEAP1/PGAM5/AIFM1 oxeiptosis axis** implicated in ROS-induced, caspase-independent cell death ([PMID: 41338468](https://pubmed.ncbi.nlm.nih.gov/41338468/)). AIF's redox chemistry (NADH/FAD charge-transfer complex, dimerization) governs the switch between its biogenesis-supporting and cell-death roles ([PMID: 26535916](https://pubmed.ncbi.nlm.nih.gov/26535916/), [PMID: 32769219](https://pubmed.ncbi.nlm.nih.gov/32769219/)).

### 7. Anatomical Structures Affected
**Primary organs:** brain (cortex, thalamus, cerebellum), heart (ventricular myocardium), skeletal muscle, inner ear (cochlea), retina (prominent in models), peripheral nerve (milder alleles). **Body systems:** nervous, cardiovascular, musculoskeletal, special sensory. **Subcellular:** mitochondria (intermembrane space, inner membrane), with nuclear translocation of AIF in the death branch. **Lateralization:** bilateral/symmetric CNS involvement (e.g., bilateral hemispheric swelling on MRI).

### 8. Temporal Development
**Onset:** congenital/neonatal to infantile in the severe form (e.g., seizures 6 h after birth); childhood–adult in milder alleles. **Course:** rapidly progressive and often fatal in infancy for severe alleles; slowly progressive for Cowchock/ataxia alleles. **Critical window:** early infancy is both the period of greatest vulnerability and the plausible window for cofactor/redox intervention; riboflavin responsiveness in ataxia patients suggests a treatable component for specific genotypes.

### 9. Inheritance and Population
**Inheritance:** X-linked recessive; manifesting heterozygous females occur with skewed XCI. **Penetrance:** high in hemizygous males carrying severe alleles; **expressivity is variable** (strong genotype–phenotype correlation across the allelic series). **Epidemiology:** ultra-rare (<~30 families/individuals reported worldwide); precise prevalence/incidence unknown (below Orphanet reporting thresholds). **Sex ratio:** strongly male-predominant. **Founder effects / consanguinity:** not a prominent feature (X-linked, private variants). **Carrier frequency:** not established; variants essentially absent from gnomAD.

### 10. Diagnostics
**Biochemistry:** elevated lactate; **respiratory-chain enzymology** in fibroblasts/muscle showing combined complex I/III/IV deficiency; **reduced AIFM1 protein** on immunoblot. **Histopathology:** TUNEL-positive/caspase-3-negative nuclei (parthanatos signature) in muscle. **Imaging:** brain MRI (bilateral hemispheric swelling, cortical/thalamic signal change with basal-nuclei sparing); MR spectroscopy (lactate peak). **Electrophysiology:** EEG (multifocal epileptiform activity); nerve conduction studies for neuropathy alleles. **Cardiac:** echocardiography (hypertrophic/dilated cardiomyopathy). **Genetic testing (recommended first-line):** clinical **exome (WES)** or **genome (WGS)** sequencing, or a mitochondrial/encephalopathy **gene panel** including *AIFM1*; single-gene *AIFM1* testing and segregation/X-inactivation studies to confirm. **Differential diagnosis:** other combined OXPHOS deficiencies, Leigh syndrome and Leigh-like disorders, mtDNA-encoded mitochondrial encephalomyopathies, and other X-linked encephalopathies.

### 11. Outcome / Prognosis
**Severe form:** poor — typically **early death in infancy/childhood** with multisystem failure and metabolic acidosis ([PMID: 34117073](https://pubmed.ncbi.nlm.nih.gov/34117073/)); high morbidity (refractory seizures, profound developmental impairment, cardiomyopathy). **Milder alleles:** prolonged survival with chronic disability (neuropathy, deafness, ataxia). **Prognostic factors:** genotype (specific allele), age at onset, and severity/rate of cardiac and metabolic decompensation. No validated molecular prognostic biomarker beyond genotype.

### 12. Treatment
No curative/disease-modifying therapy. **Pharmacotherapy/cofactors (NCIT where applicable):** riboflavin (NCIT:C737), Coenzyme Q10 (NCIT:C1198), thiamine (NCIT:C933), antiepileptic drugs (NCIT:C264). **Preclinical/experimental redox agents:** methylene blue (NCIT:C61585), tempol, NADH. **Supportive/rehabilitative:** nutritional/feeding support, heart-failure therapy for cardiomyopathy, physical/occupational/speech therapy. **Perioperative:** mitochondrial-safe anesthesia (e.g., total intravenous anesthesia with remimazolam reported for COXPD6; [PMID: 41211097](https://pubmed.ncbi.nlm.nih.gov/41211097/)). **Pharmacogenomics / personalized medicine:** genotype-guided trial of riboflavin for riboflavin-responsive alleles. No approved gene, cell, or RNA therapy exists.

### 13. Prevention
**Primary prevention:** not applicable (monogenic); **genetic counseling** for X-linked recurrence risk is central. **Secondary:** carrier testing in at-risk female relatives, cascade testing, and prenatal/preimplantation genetic testing where a familial variant is known. **Tertiary:** proactive seizure control, cardiac surveillance/heart-failure management, nutritional support, avoidance of mitochondrial toxins and risky anesthetics. No vaccination or population screening applies.

### 14. Other Species / Natural Disease
**Model/ortholog species:** mouse (*Mus musculus*, NCBI Taxon 10090; *Aifm1*, NCBI Gene 26926). The **Harlequin mouse** is a naturally arising hypomorphic *Aifm1* model. No prominent naturally occurring companion-animal/wildlife disease is established; the mechanism (AIF-dependent OXPHOS support) is **evolutionarily conserved** across animals, underpinning cross-species modeling.

### 15. Model Organisms
**Primary model:** Harlequin (Hq) mouse — hypomorphic *Aifm1* (80–90% AIF reduction) with complex I deficiency and progressive cerebellar/retinal neurodegeneration ([PMID: 23246553](https://pubmed.ncbi.nlm.nih.gov/23246553/), [PMID: 17805014](https://pubmed.ncbi.nlm.nih.gov/17805014/)). Used to demonstrate causal upstream mitochondrial injury, ROS regulation, MPTP sensitization ([PMID: 20695011](https://pubmed.ncbi.nlm.nih.gov/20695011/)), tau interaction ([PMID: 19942317](https://pubmed.ncbi.nlm.nih.gov/19942317/)), and redox rescue (tempol, methylene blue). **Phenotype recapitulation:** reproduces complex I deficiency and progressive neurodegeneration. **Limitations:** a hypomorph (not an allele-specific knock-in of human severe variants); does not fully capture the human infantile encephalopathy/cardiomyopathy severity or the allele-specific gain-of-function (DNA-binding) biology. Patient-derived **fibroblasts and iPSCs** serve as complementary in-vitro models.

---

## Evidence Base

| PMID | Title (abbrev.) | Source type | Contribution |
|---|---|---|---|
| [20362274](https://pubmed.ncbi.nlm.nih.gov/20362274/) | *Severe X-linked mitochondrial encephalomyopathy assoc. with AIF mutation* | Human clinical + in vitro | Establishes *AIFM1* R201del as causal; dual mechanism (OXPHOS loss + parthanatos); X-linked inheritance |
| [32769219](https://pubmed.ncbi.nlm.nih.gov/32769219/) | *AIF and mitochondrial NADH dehydrogenases: redox-controlled gear boxes* | Review | AIF promotes MIA40/CHCHD4 import and complex I assembly; redox switch |
| [28967629](https://pubmed.ncbi.nlm.nih.gov/28967629/) | *AIFM1 cause X-linked childhood cerebellar ataxia partially responsive to riboflavin* | Human clinical | Defines allelic spectrum; quantifies riboflavin response (ICARS −39%/−20%) |
| [23217327](https://pubmed.ncbi.nlm.nih.gov/23217327/) | *Cowchock syndrome assoc. with AIF mutation* | Human clinical | Milder CMTX4 end of spectrum; Xq24–q26 mapping |
| [34117073](https://pubmed.ncbi.nlm.nih.gov/34117073/) | *Severe multisystem pathology, metabolic acidosis, early death (X-linked)* | Human clinical | Severe multisystem phenotype, early death |
| [42329587](https://pubmed.ncbi.nlm.nih.gov/42329587/) | *Cardiomyopathy and encephalomyopathy in a female with heterozygous AIFM1* | Human clinical | Manifesting female; skewed XCI (98:2); cardiomyopathy progression |
| [37644805](https://pubmed.ncbi.nlm.nih.gov/37644805/) | *Expanding neonatal-onset AIFM1 disorders* | Human clinical + in vitro | Neonatal seizures, MRI pattern, MTS variant; mito cocktail stabilization |
| [23246553](https://pubmed.ncbi.nlm.nih.gov/23246553/) | *AIF, ROS, and neurodegeneration* | Model/review | Harlequin model: 80–90% AIF loss, progressive neurodegeneration |
| [17805014](https://pubmed.ncbi.nlm.nih.gov/17805014/) | *AIF deficiency induces early mitochondrial degeneration* | Model organism | Mitochondrial injury is causal/upstream of neuronal death |
| [20695011](https://pubmed.ncbi.nlm.nih.gov/20695011/) | *AIF deficiency sensitizes dopaminergic neurons to parkinsonian neurotoxins* | Model organism | Gene–environment interaction (MPTP); tempol rescue |
| [35000037](https://pubmed.ncbi.nlm.nih.gov/35000037/) | *Key players of parthanatos* | Review | Defines PARP-1→PAR→AIF/MIF→DNA fragmentation cascade |
| [35994922](https://pubmed.ncbi.nlm.nih.gov/35994922/) | *AIFM1 beyond cell death: OXPHOS-inducing factor* | Review | Reframes disease as primarily bioenergetic |
| [30300862](https://pubmed.ncbi.nlm.nih.gov/30300862/) | *AIF deficiency causes retinal photoreceptor degeneration; methylene blue* | Model organism | Candidate redox therapy (methylene blue) |
| [26535916](https://pubmed.ncbi.nlm.nih.gov/26535916/) | *Adenylate moiety and NAD(+)/H binding to AIF* | In vitro/structural | Redox/cofactor mechanism; G308E pathophysiology |
| [19942317](https://pubmed.ncbi.nlm.nih.gov/19942317/) | *Tau + Harlequin mutation increases mito dysfunction/neurodegeneration* | Model organism | Mitochondrial dysfunction ↔ tauopathy interaction |
| [41338468](https://pubmed.ncbi.nlm.nih.gov/41338468/) | *Oxeiptosis: KEAP1/PGAM5/AIFM1 axis in PD* | Review | AIFM1 in ROS-induced caspase-independent death |
| [41211097](https://pubmed.ncbi.nlm.nih.gov/41211097/) | *Perioperative care in COXPD6: TIVA with remimazolam* | Case report | Anesthetic management guidance |
| [38297850](https://pubmed.ncbi.nlm.nih.gov/38297850/) | *Therapeutic potential of NADH* | Review | NADH as candidate for mito-dysfunction neurodegeneration |

**Evidence-source balance:** The causal genetics and dual-mechanism are supported by **human clinical + in-vitro patient-cell data** (strong). The upstream-causality and therapeutic-rescue claims rest substantially on **model-organism (Harlequin mouse)** and **in-vitro** evidence. Treatment efficacy data are limited to **small case reports and n=2 cohorts** — hypothesis-generating rather than definitive.

---

## Limitations and Knowledge Gaps

- **Ultra-rarity limits epidemiology:** fewer than ~30 reported families/individuals preclude reliable prevalence, incidence, penetrance-by-allele, and natural-history quantification.
- **Mechanistic weighting is unresolved:** the relative contribution of **Branch A (OXPHOS loss)** versus **Branch B (parthanatos)** to human tissue damage is inferred largely from in-vitro and mouse data; the parthanatos contribution in patient CNS/heart is not quantified in vivo.
- **Biochemical heterogeneity:** fibroblast enzymology is inconsistent across patients (complex III/IV reduced with preserved complex I in the index family; complex I/III/IV all reduced in the neonatal case), complicating a single unifying biochemical signature.
- **Model limitations:** the Harlequin mouse is a **hypomorph**, not an allele-specific knock-in; it under-represents the severe human infantile encephalopathy/cardiomyopathy and the gain-of-function (DNA-binding) biology of specific alleles.
- **No controlled therapeutic data:** riboflavin and the "mito cocktail" responses are anecdotal/small-n; there are **no randomized trials** and no approved disease-modifying therapy.
- **Genotype–phenotype gaps:** predictive rules linking specific *AIFM1* variants to severity, riboflavin-responsiveness, or cardiac risk remain incompletely defined.
- **Female manifestation:** the threshold of X-inactivation skewing required for disease, and its tissue-specific variability, are documented in only a single case.

---

## Proposed Follow-up Experiments / Actions

1. **Allele-specific knock-in models:** Generate mouse (or iPSC-derived neuron/cardiomyocyte/organoid) knock-ins of human severe alleles (p.Arg201del, p.Pro169Leu) to dissect Branch A vs. Branch B contributions and to model cardiomyopathy.
2. **Quantify parthanatos in patient tissue:** Use PAR, PARP-1, and nuclear AIF/MIF markers in patient muscle/brain autopsy material to establish the in-vivo magnitude of the death branch and its therapeutic tractability (e.g., PARP inhibitors, MIF-nuclease inhibitors).
3. **Genotype-stratified cofactor trials:** Build an international registry and run small, biomarker-anchored n-of-1 or basket trials of riboflavin ± CoQ10 ± thiamine, stratified by allele and by FAD-domain impact, using ICARS/clinical and lactate/respirometry endpoints.
4. **Redox therapeutics translation:** Advance methylene blue, tempol, and NADH from Harlequin-model efficacy toward patient-derived cardiomyocyte/neuron testing, with mitochondrial respirometry and ROS readouts.
5. **X-inactivation and female risk:** Systematically measure tissue-specific XCI skewing in heterozygous females to define the manifestation threshold and inform counseling.
6. **Natural-history and biomarker study:** Pool cases to define age-specific survival, cardiac trajectory, seizure burden, and candidate prognostic biomarkers (lactate, FGF21, neurofilament), enabling clinical-trial readiness.
7. **Gene/RNA therapy feasibility:** Evaluate AIFM1 gene replacement or variant-specific correction given the loss-of-vital-function component, balancing against the gain-of-function (DNA-binding) risk of over-expression.

---

*Report compiled from 9 confirmed findings and 26 reviewed papers across 5 investigation iterations. Evidence sources are distinguished as human clinical, model organism, in vitro, or computational/review throughout.*


## Artifacts

- [OpenScientist final report](Severe_X-linked_Mitochondrial_Encephalomyopathy-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Severe_X-linked_Mitochondrial_Encephalomyopathy-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 18 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 19 |
| Quoted claims found in source | 18 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 18 |
| On topic | 13 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:30300862` *(abstract only)*: "The protective role of the redox compound methylene blue"
  - closest text in source: "We investigated the effect of mitochondrial OXPHOS deficiency on retinal photoreceptors in a model of mitochondrial complex I defect (apoptosis inducing factor, AIF-deficient mice, Harlequin mice), and tested the protective effect of a mitochondrial redox compound (methylene blue, MB) on mitochondrial and photoreceptor integrity"
