---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-04T11:37:17.521827'
end_time: '2026-09-04T11:49:54.296464'
duration_seconds: 756.77
template_file: /tmp/abc_prompt.md
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 2
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 29
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Aneurysmal_Bone_Cyst-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Aneurysmal_Bone_Cyst-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Aneurysmal Bone Cyst
- **MONDO ID:** MONDO:0018815 (if available)
- **Category:** Locally aggressive USP6-rearranged bone neoplasm

## Research Objectives

Please provide a comprehensive research report on **Aneurysmal Bone Cyst** covering all of the
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

# Aneurysmal Bone Cyst (ABC): A Comprehensive Disease Characteristics Report

**MONDO ID:** MONDO:0018815 · **Category:** Locally aggressive USP6-rearranged bone neoplasm

---

## Summary

Aneurysmal bone cyst (ABC) is a benign but **locally aggressive, expansile osteolytic neoplasm** of bone that predominantly affects children and young adults in the first two decades of life. It most commonly arises in the metaphysis of long bones (especially around the knee) and in the posterior elements of the vertebrae, and is defined histologically by blood-filled cystic spaces separated by fibrous septa containing bland spindle (myofibroblastic) cells, osteoclast-like multinucleated giant cells, and reactive woven bone. For most of the 20th century ABC was considered a reactive or vascular malformation of uncertain cause, but molecular cytogenetics has redefined the majority of cases as a **true clonal neoplasm**.

The central mechanistic insight, established over the past two decades, is that **primary ABC (~70% of cases) is driven by somatic promoter-swap rearrangements of the *USP6* gene** (ubiquitin-specific protease 6, also called TRE2/TRE17, at 17p13.2). These rearrangements place the full-length *USP6* coding sequence under the control of a constitutively active partner-gene promoter (classically *CDH11*, but now dozens of partners are known), driving *USP6* overexpression. USP6 in turn activates NF-κB signaling to induce matrix metalloproteinases (MMP-9, MMP-10), promotes angiogenesis, and drives RANKL-mediated osteoclast recruitment — together producing the characteristic vascular, cystic, bone-destroying lesion. Crucially, the *USP6* rearrangement is confined to the neoplastic myofibroblastic spindle cell and is **absent in secondary ABC-like changes** (~30% of cases) that arise within other bone tumors (e.g., giant cell tumor, chondroblastoma, fibrous dysplasia, osteosarcoma).

This molecular understanding has clinical consequences. USP6 FISH/RNA-sequencing is now used to confirm primary ABC and to distinguish it from mimics (including telangiectatic osteosarcoma). The NF-κB/RANKL axis provides a rationale for **denosumab** (anti-RANKL monoclonal antibody) as targeted systemic therapy, particularly for surgically challenging spinal/sacral lesions. Treatment remains dominated by curettage (± adjuvants) with recurrence rates of ~25–31%, but minimally invasive **image-guided doxycycline sclerotherapy** now achieves ~99% success with low morbidity. ABC does not metastasize and mortality is negligible; the principal adverse outcome is local recurrence, usually within 2 years.

---

## Key Findings

### Finding 1 — Primary ABC is a *USP6*-rearranged mesenchymal neoplasm, and the neoplastic cell is the myofibroblastic spindle cell

The landmark work of Oliveira and colleagues transformed the conceptual status of ABC from a reactive lesion to a bona fide neoplasm. Clonal chromosomal translocations at **17p13** were shown to place the *USP6* (TRE2/TRE17) coding region under the control of the highly active *CDH11* (osteoblast cadherin) promoter, producing a **promoter-swap fusion** that drives overexpression of full-length USP6 protein. In their series, *USP6* and/or *CDH11* rearrangements were detected in **36 of 52 (69%) primary ABCs**.

Decisively, these rearrangements were **restricted to the spindle (myofibroblastic) cells** of the lesion and were **not** present in the multinucleated giant cells, inflammatory cells, endothelial cells, or osteoblasts — identifying the myofibroblastic spindle cell as the neoplastic cell of origin and framing the giant cells and vascular spaces as reactive/recruited secondary components ([PMID: 15509545](https://pubmed.ncbi.nlm.nih.gov/15509545/)).

> *"USP6 and CDH11 rearrangements were restricted to spindle cells in the ABC and were not found in multinucleated giant cells, inflammatory cells, endothelial cells, or osteoblasts."* — Oliveira et al.

This same study established that so-called **secondary ABC** — ABC-like cystic change occurring within another primary bone lesion — **lacks** the *USP6* rearrangement (0/17 secondary ABCs), providing a molecular criterion that separates the two entities. A modern review reaffirms the proportions: **primary ABC accounts for ~70% of cases and is a true neoplasm, whereas ABC-like (secondary) changes account for the remaining ~30%** ([PMID: 35941207](https://pubmed.ncbi.nlm.nih.gov/35941207/)).

> *"ABC, which accounts for approximately 70% of the cases, is now recognized to be a true neoplasm, whereas ABC-like changes associated to other bone neoplasms (also referred in the literature as secondary ABC) accounts for the remaining 30%."* — Restrepo et al.

**Fusion partner diversity.** Although *CDH11::USP6* is the classic fusion, the partner repertoire is broad and continues to expand. A morphomolecular study of 175 "USP6-associated neoplasms" (nodular fasciitis, myositis ossificans, ABC) found *USP6* rearrangement in the great majority and identified **22 novel fusion partners**, with the observation that the partner gene depends strongly on tumor morphology and anatomic location — supporting the idea that partner diversity may reflect the cell of origin ([PMID: 41293881](https://pubmed.ncbi.nlm.nih.gov/41293881/)). Case reports and small series document a growing list of ABC partners including *FAT1::USP6* and *MIR22HG::USP6* in solid-variant craniofacial ABC ([PMID: 35102523](https://pubmed.ncbi.nlm.nih.gov/35102523/)), *AHNAK::USP6* in polyostotic solid-variant vertebral ABC ([PMID: 35717456](https://pubmed.ncbi.nlm.nih.gov/35717456/)), *PAFAH1B1::USP6* (chromothripsis-induced) in periosteal solid ABC ([PMID: 38979775](https://pubmed.ncbi.nlm.nih.gov/38979775/)), *FGFR1::USP6* in orbital ABC ([PMID: 36356178](https://pubmed.ncbi.nlm.nih.gov/36356178/)), and *SEC24D::USP6*, *HNRNPC::USP6*, and *ERRFI1::USP6* in pediatric long-bone ABC ([PMID: 41432301](https://pubmed.ncbi.nlm.nih.gov/41432301/)). All converge on a single functional outcome: **transcriptional upregulation of full-length USP6.**

### Finding 2 — USP6 drives tumorigenesis via NF-κB-mediated matrix metalloproteinase production

The functional mechanism linking *USP6* overexpression to the ABC phenotype was defined experimentally by Ye and colleagues. Overexpression of TRE17/USP6 is **sufficient to induce expression of MMP-9 and MMP-10**, in a manner that requires the enzyme's ubiquitin-specific protease (USP/deubiquitinase) catalytic activity but **not** its ability to bind the small GTPase Arf6. Mechanistically, USP6 induces **MMP-9 transcription through activation of NF-κB**, mediated in part by the GTPase **RhoA and its effector kinase ROCK** ([PMID: 20418905](https://pubmed.ncbi.nlm.nih.gov/20418905/)).

> *"TRE17 is sufficient to induce expression of MMP-9 and MMP-10, in a manner requiring its USP activity, but not its ability to bind Arf6. TRE17 induces transcription of MMP-9 through activation of nuclear factor-kappaB (NF-kappaB), mediated in part by the GTPase RhoA and its effector kinase, ROCK."* — Ye et al.

Critically, **xenografts of TRE17-expressing cells formed vascularized tumors that reproduced key features of ABC**, and tumorigenesis was dependent on the intact USP catalytic domain. This provides direct causal evidence that USP6's deubiquitinase activity — not merely its overexpression as a bystander — drives the matrix-degrading, angiogenic, osteolytic program that defines the lesion.

### Finding 3 — Recurrence rates are modality-dependent, and minimally invasive sclerotherapy rivals surgery

ABC is non-metastatic and rarely fatal, so the dominant clinical outcome measure is **local recurrence**, which typically occurs within 2 years of treatment. Recurrence varies substantially by treatment modality:

| Treatment modality | Recurrence / reintervention | Cohort | Source |
|---|---|---|---|
| Standard curettage ± bone grafting | ~25–31% | Retrospective, 265 patients | [PMID: 37638388](https://pubmed.ncbi.nlm.nih.gov/37638388/) |
| Image-guided doxycycline sclerotherapy | 16% recurred (all resolved with repeat doxycycline); 99% ultimately successful | 77 appendicular/pelvic lesions | [PMID: 39265785](https://pubmed.ncbi.nlm.nih.gov/39265785/) |
| Modified single-session sclerograft (doxycycline ± cryoablation + regenerative grafting) | 25.9% reintervention (7/27) at median 1.88 yr | 27 patients | [PMID: 42477120](https://pubmed.ncbi.nlm.nih.gov/42477120/) |
| Pediatric spinal ABC — 4-step curettage (curettage + high-speed burr + electrocautery + grafting) | 19% (4/21) | Comparative series | [PMID: 32986586](https://pubmed.ncbi.nlm.nih.gov/32986586/) |
| Pediatric spinal ABC — traditional curettage | 50% (4/8) | Comparative series | [PMID: 32986586](https://pubmed.ncbi.nlm.nih.gov/32986586/) |

> *"The standard of care cure for ABC has been curettage with or without bone grafting of the defect but is burdened by recurrence rates of approximately 25%-31%."* — Cevolani et al. ([PMID: 37638388](https://pubmed.ncbi.nlm.nih.gov/37638388/))

> *"Of the 77 lesions, 76 (99%) were successfully treated. Twelve lesions (16%) recurred but resolved with additional doxycycline treatment."* — Wong et al. ([PMID: 39265785](https://pubmed.ncbi.nlm.nih.gov/39265785/))

> *"The recurrence rate was 50% (4/8 patients) with the traditional technique (group 1) and 19% (4/21) in the 4-step technique (group 2)."* — Grigoriou et al. ([PMID: 32986586](https://pubmed.ncbi.nlm.nih.gov/32986586/))

The takeaway is that **aggressive local control** — whether by adjuvant-augmented curettage (burr, electrocautery, phenol) or by percutaneous sclerotherapy — substantially reduces recurrence relative to simple curettage, and minimally invasive doxycycline sclerotherapy has emerged as a highly effective, low-morbidity alternative to open surgery, particularly at anatomically difficult sites.

---

## Detailed Section-by-Section Report

### 1. Disease Information

**Overview.** Aneurysmal bone cyst is a benign, locally aggressive, expansile, osteolytic bone tumor characterized by blood-filled cystic spaces separated by fibrous septa containing myofibroblastic spindle cells, osteoclast-like giant cells, and reactive bone. Despite the name, it is neither an aneurysm nor a simple cyst; primary ABC is a clonal neoplasm. Lesions can grow rapidly and cause pain, swelling, pathologic fracture, and (in the spine) neurologic compromise ([PMID: 22474093](https://pubmed.ncbi.nlm.nih.gov/22474093/); [PMID: 35941207](https://pubmed.ncbi.nlm.nih.gov/35941207/)).

**Key identifiers.**
- **MONDO:** MONDO:0018815
- **ICD-O:** 9260/0 (aneurysmal bone cyst)
- **ICD-10:** M85.5 (aneurysmal bone cyst); **ICD-11:** relevant benign bone neoplasm code
- **MeSH:** "Bone Cysts, Aneurysmal" (D017824)
- **Orphanet:** relevant rare bone tumor entry
- **Causal gene:** *USP6* (HGNC:12629; NCBI Gene 9098; OMIM *604334; locus 17p13.2)

**Synonyms / alternative names.** Aneurysmal bone cyst; ABC; primary aneurysmal bone cyst; solid variant of ABC (SVABC); giant cell reparative granuloma (historical term for some jaw lesions). "USP6-associated neoplasm" is the broader molecular family (with nodular fasciitis and myositis ossificans).

**Data provenance.** Information here is derived from **aggregated disease-level resources** — pathology case series, molecular cytogenetic studies, treatment cohorts, and review articles — not from individual EHR-derived patient records.

### 2. Etiology

**Primary cause (genetic, somatic).** Primary ABC is caused by a **somatic clonal rearrangement of *USP6***, a promoter-swap event that drives overexpression of full-length USP6 protein ([PMID: 15509545](https://pubmed.ncbi.nlm.nih.gov/15509545/); [PMID: 35941207](https://pubmed.ncbi.nlm.nih.gov/35941207/)). This is an acquired somatic event confined to lesional tissue — **not inherited** and not present in the germline.

**Secondary ABC.** ~30% of ABC-like lesions are **secondary**: cystic, blood-filled change superimposed on a pre-existing bone lesion (giant cell tumor of bone, chondroblastoma, fibrous dysplasia, osteoblastoma, osteosarcoma). These lack *USP6* rearrangement and are driven by the underlying primary lesion ([PMID: 15509545](https://pubmed.ncbi.nlm.nih.gov/15509545/)).

**Risk factors.**
- *Genetic:* No inherited susceptibility loci or germline risk variants are established. The driver is a somatic structural rearrangement acquired in a single myofibroblastic clone.
- *Environmental / demographic:* Young age (first two decades) is the dominant demographic risk factor. A history of **trauma** has long been anecdotally associated, and older "vascular/traumatic" hypotheses invoked a local hemodynamic disturbance, but these remain unproven and are now largely superseded by the neoplastic (USP6) model ([PMID: 22474093](https://pubmed.ncbi.nlm.nih.gov/22474093/)).

**Protective factors.** None established (genetic or environmental).

**Gene–environment interactions.** No validated gene–environment interaction is described. The disease is initiated by a stochastic somatic rearrangement; environmental modulation of that event is not characterized.

### 3. Phenotypes

| Phenotype | Type | Characteristics | Suggested HPO |
|---|---|---|---|
| Bone pain | Symptom | Common presenting feature; insidious or progressive; localized to lesion | HP:0002653 (Bone pain) |
| Localized swelling / palpable mass | Clinical sign | Rapidly enlarging expansile mass | Local swelling / mass |
| Pathologic fracture | Physical manifestation | Through weakened cortex; can be presenting event | HP:0002659 (Abnormal fracture susceptibility) |
| Osteolysis / bone destruction | Radiographic sign | Expansile lytic lesion, cortical thinning | HP:0002797 (Osteolysis) |
| Neurologic deficit (spinal ABC) | Clinical sign | Radiculopathy, cord compression, deficit | Focal neurologic signs |
| Proptosis / visual disturbance (orbital ABC) | Clinical sign | Site-specific; ptosis, diplopia, decreased vision | HP:0000520 (Proptosis) |
| Joint stiffness / reduced mobility | Physical manifestation | When juxta-articular | HP:0001387 (Joint stiffness) |

**Onset:** childhood/adolescence predominant. **Severity:** variable — from incidental to severely destructive. **Progression:** often rapidly progressive/expansile; can be episodic with growth spurts. **Frequency:** pain and swelling are the most common presentations across series ([PMID: 22474093](https://pubmed.ncbi.nlm.nih.gov/22474093/); [PMID: 18761766](https://pubmed.ncbi.nlm.nih.gov/18761766/)).

**Quality of life.** After appropriate surgical treatment, functional outcomes are generally good. In pediatric pelvic ABC treated with extended curettage and grafting, mean Toronto Extremity Salvage Score (TESS) was 95, MSTS'93 was 93%, and SF-36 self-rated general health was 87% of maximum at ~11 years follow-up ([PMID: 24817630](https://pubmed.ncbi.nlm.nih.gov/24817630/)). Suggested QoL tools: SF-36, MSTS'93, TESS.

### 4. Genetic / Molecular Information

**Causal gene.** *USP6* (ubiquitin-specific peptidase 6; aliases TRE2, TRE17; HGNC:12629; OMIM *604334; locus **17p13.2**). ABC is defined by structural rearrangement of *USP6*, not point mutation.

**Variant type / class.** The pathogenic event is a **balanced (or complex) chromosomal translocation / gene fusion** — a **promoter-swap** in which the *USP6* coding sequence is juxtaposed to a partner-gene promoter/enhancer, driving overexpression of full-length USP6. It is a **gain-of-function** mechanism (overexpression of intact protein), distinct from missense/frameshift point mutations.

**Fusion partners.** *CDH11::USP6* is classic. Documented and novel partners include *MYH9* (common in nodular fasciitis), *FAT1*, *MIR22HG*, *AHNAK*, *PAFAH1B1*, *FGFR1*, *SEC24D*, *HNRNPC*, *ERRFI1*, and ≥22 additional partners reported in USP6-associated neoplasms ([PMID: 41293881](https://pubmed.ncbi.nlm.nih.gov/41293881/); [PMID: 35102523](https://pubmed.ncbi.nlm.nih.gov/35102523/); [PMID: 35717456](https://pubmed.ncbi.nlm.nih.gov/35717456/); [PMID: 38979775](https://pubmed.ncbi.nlm.nih.gov/38979775/); [PMID: 41432301](https://pubmed.ncbi.nlm.nih.gov/41432301/)).

**Somatic vs germline.** **Somatic** — clonal, lesion-restricted; not heritable. **Classification:** the *USP6* rearrangement is a diagnostic, pathogenic somatic driver (COSMIC/somatic domain; not an ACMG germline classification).

**Allele frequency.** Not applicable — a somatic structural event, absent from population germline databases (gnomAD, 1000 Genomes).

**Functional consequence.** Gain of function through overexpression of catalytically active USP6 deubiquitinase, activating downstream NF-κB and matrix-degrading programs ([PMID: 20418905](https://pubmed.ncbi.nlm.nih.gov/20418905/)).

**Chromosomal abnormalities.** 17p13 translocations; in at least one reported case, *USP6* rearrangement was generated by **chromothripsis** (*PAFAH1B1::USP6*), producing a solid periosteal ABC initially mistaken for osteosarcoma ([PMID: 38979775](https://pubmed.ncbi.nlm.nih.gov/38979775/)).

**Modifier genes / epigenetics.** Not established for ABC.

### 5. Environmental Information

No validated environmental etiologic agents. Trauma has been historically proposed as a trigger but is unproven and not required for the USP6-driven neoplastic model ([PMID: 22474093](https://pubmed.ncbi.nlm.nih.gov/22474093/)). **Lifestyle factors:** none established. **Infectious agents:** none — ABC is not an infectious disease.

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. A somatic **chromosomal rearrangement at 17p13.2** juxtaposes the *USP6* coding sequence to an active partner-gene promoter (e.g., *CDH11*) in a single **myofibroblastic spindle cell** → **results in** clonal overexpression of full-length USP6 protein. *(Demonstrated — Oliveira 2004, PMID 15509545.)*
2. Overexpressed USP6, via its **ubiquitin-specific protease (deubiquitinase) activity**, → **activates the RhoA–ROCK pathway and NF-κB signaling.** *(Demonstrated — Ye 2010, PMID 20418905.)*
3. NF-κB activation → **induces transcription of matrix metalloproteinases MMP-9 and MMP-10** (and other targets). *(Demonstrated — Ye 2010.)*
4. MMP-mediated extracellular-matrix degradation, together with USP6-driven **pro-angiogenic signaling**, → **leads to** local matrix remodeling and formation of the vascular, blood-filled cystic spaces characteristic of ABC. *(Demonstrated in xenograft; USP-domain-dependent.)*
5. The neoplastic myofibroblasts and lesional stroma → **produce RANKL**, which → **recruits and activates osteoclast-like multinucleated giant cells.** *(Inferred from ABC/GCT biology and denosumab response — not fully proven in ABC.)*
6. RANKL-driven osteoclastic activity → **results in** progressive **osteolysis, cortical expansion and thinning** → **leads to** the clinical manifestations: pain, swelling, pathologic fracture, and (site-dependent) neurologic or ophthalmic compromise. *(Demonstrated clinically/radiographically.)*

**Branch point:** at steps 5–6 the mechanism converges on the **RANK/RANKL/osteoclast** axis, which is the pharmacologic target of **denosumab**; devascularization and calcification on denosumab therapy support this branch ([PMID: 26730528](https://pubmed.ncbi.nlm.nih.gov/26730528/); [PMID: 36282899](https://pubmed.ncbi.nlm.nih.gov/36282899/)).

**Molecular pathways:** NF-κB signaling (KEGG hsa04064), RhoA/ROCK; RANK–RANKL–OPG axis; ubiquitin-proteasome/deubiquitination. **Cellular processes (GO):** extracellular matrix disassembly (GO:0022617), positive regulation of NF-κB transcription factor activity (GO:0051092), osteoclast differentiation (GO:0030316), angiogenesis (GO:0001525), bone resorption (GO:0045453). **Protein dysfunction:** gain of function via USP6 deubiquitinase overexpression. **Immune/inflammatory:** NF-κB-driven inflammatory milieu and osteoclast recruitment. **Tissue damage:** MMP-mediated matrix degradation and osteoclastic bone resorption.

**Cell types (CL):** neoplastic **myofibroblast** (CL:0000186 / fibroblast CL:0000057); reactive **osteoclast** (CL:0000092); **endothelial cell** (CL:0000115, reactive); **osteoblast** (CL:0000062, reactive). **Molecular profiling:** whole-transcriptome RNA-sequencing is the most informative modality and now routinely detects *USP6* fusions and identifies novel partners ([PMID: 41432301](https://pubmed.ncbi.nlm.nih.gov/41432301/); [PMID: 41293881](https://pubmed.ncbi.nlm.nih.gov/41293881/)).

### 7. Anatomical Structures Affected

- **Organ / system level:** skeletal system (musculoskeletal). Primary structure = **bone** (UBERON:0002481, bone tissue; UBERON:0001474, bone element). Secondary involvement by mass effect: spinal cord/nerve roots (spinal ABC), orbit/eye (orbital ABC), paranasal sinuses and jaw (craniofacial ABC).
- **Common sites:** metaphysis of long bones — especially about the **knee** (distal femur UBERON:0002862, proximal tibia); also humerus, pelvis, and **posterior elements of vertebrae** (UBERON:0002412) ([PMID: 22474093](https://pubmed.ncbi.nlm.nih.gov/22474093/); [PMID: 35941207](https://pubmed.ncbi.nlm.nih.gov/35941207/)).
- **Uncommon sites:** mandible/maxilla ([PMID: 18761766](https://pubmed.ncbi.nlm.nih.gov/18761766/); [PMID: 16609883](https://pubmed.ncbi.nlm.nih.gov/16609883/)), orbit ([PMID: 36356178](https://pubmed.ncbi.nlm.nih.gov/36356178/)), skull base, and other flat/craniofacial bones (often solid variant).
- **Tissue level:** connective tissue / bone; fibrous septa with myofibroblasts. **Subcellular (GO CC):** cytoplasm (GO:0005737), nucleus (GO:0005634, site of NF-κB action); extracellular region/matrix (GO:0005576) for secreted MMPs.
- **Localization / lateralization:** usually **solitary and unilateral / monostotic**; rare **polyostotic** and synchronous presentations are reported (e.g., multi-vertebral solid variant, [PMID: 35717456](https://pubmed.ncbi.nlm.nih.gov/35717456/)).

### 8. Temporal Development

- **Onset:** predominantly **pediatric/adolescent** (first two decades); can occur in young adults. Onset is typically **subacute to chronic** with progressive pain and swelling; occasionally acute presentation via pathologic fracture ([PMID: 22474093](https://pubmed.ncbi.nlm.nih.gov/22474093/)).
- **Progression:** locally aggressive and often **rapidly expansile**, but benign (non-metastasizing). No formal malignant staging applies.
- **Disease course:** effectively curable with adequate local control; the natural risk is **local recurrence, usually within 2 years** ([PMID: 36356178](https://pubmed.ncbi.nlm.nih.gov/36356178/)).
- **Remission:** achieved by treatment (surgery, sclerotherapy, denosumab). Rare spontaneous regression is described but not the norm. **Critical window:** recurrence surveillance is most important in the first 2 years post-treatment.

### 9. Inheritance and Population

- **Epidemiology:** ABC is rare, comprising roughly 1–2% of primary bone tumors; commonly cited incidence is on the order of ~0.1–0.15 per 100,000/year. Peak incidence in the first two decades of life ([PMID: 22474093](https://pubmed.ncbi.nlm.nih.gov/22474093/); [PMID: 35941207](https://pubmed.ncbi.nlm.nih.gov/35941207/)).
- **Inheritance:** **not inherited.** The driver is a somatic *USP6* rearrangement; there is no Mendelian inheritance pattern, no penetrance/expressivity, no anticipation, no founder effect, and no carrier frequency to report.
- **Sex ratio:** approximately equal, with a slight female predominance in some series.
- **Age distribution:** heavily skewed toward children and adolescents.
- **Geographic distribution:** no defined endemic distribution; occurs worldwide.

### 10. Diagnostics

**Imaging.** Radiography shows an eccentric, expansile, radiolucent (lytic) metaphyseal lesion with cortical thinning. **MRI** classically demonstrates **fluid-fluid levels** from layering of blood components — a hallmark but not pathognomonic feature (also seen in telangiectatic osteosarcoma). CT delineates cortical integrity ([PMID: 22474093](https://pubmed.ncbi.nlm.nih.gov/22474093/); [PMID: 30413280](https://pubmed.ncbi.nlm.nih.gov/30413280/)). RadLex/Radiopaedia are relevant imaging references.

**Histopathology / biopsy.** Blood-filled cystic spaces separated by fibrous septa containing bland spindle (myofibroblastic) cells, osteoclast-like multinucleated giant cells, and reactive woven bone; myofibroblastic cells are smooth-muscle-actin (SMA) positive ([PMID: 41432301](https://pubmed.ncbi.nlm.nih.gov/41432301/)). The **solid variant** lacks prominent cystic spaces and can closely mimic other tumors ([PMID: 30413280](https://pubmed.ncbi.nlm.nih.gov/30413280/); [PMID: 35102523](https://pubmed.ncbi.nlm.nih.gov/35102523/)).

**Molecular (definitive).** **USP6 FISH (break-apart)** and **targeted RNA-sequencing / NGS** detect the *USP6* rearrangement and confirm **primary ABC**, distinguishing it from secondary ABC-like change and from mimics. RNA-seq is especially valuable in solid variants and unusual locations where FISH may miss atypical fusions ([PMID: 15509545](https://pubmed.ncbi.nlm.nih.gov/15509545/); [PMID: 35102523](https://pubmed.ncbi.nlm.nih.gov/35102523/); [PMID: 41432301](https://pubmed.ncbi.nlm.nih.gov/41432301/)). Nanopore/long-read DNA sequencing can resolve complex rearrangements (e.g., chromothripsis-generated fusions) ([PMID: 38979775](https://pubmed.ncbi.nlm.nih.gov/38979775/)).

**Differential diagnosis.** Telangiectatic osteosarcoma (critical malignant mimic), giant cell tumor of bone, unicameral (simple) bone cyst, chondroblastoma with ABC-like change, fibrous dysplasia, osteoblastoma; solid-variant ABC additionally mimics Ewing sarcoma, Langerhans cell histiocytosis, and metastasis. **USP6 status is the key molecular discriminator** for primary ABC ([PMID: 35102523](https://pubmed.ncbi.nlm.nih.gov/35102523/); [PMID: 22474093](https://pubmed.ncbi.nlm.nih.gov/22474093/)).

**Screening:** none — ABC is somatic, non-heritable, and sporadic; population/genetic screening is not applicable.

### 11. Outcome / Prognosis

- **Survival / mortality:** ABC is benign and **does not metastasize**; disease-specific mortality is negligible. Life expectancy is normal.
- **Morbidity:** driven by local destruction — pain, pathologic fracture, growth disturbance (when the physis/triradiate cartilage is involved), and neurologic/ophthalmic deficits at spinal/orbital sites. With modern treatment, functional outcomes are generally excellent (TESS 95, MSTS 93% in pediatric pelvic ABC; [PMID: 24817630](https://pubmed.ncbi.nlm.nih.gov/24817630/)).
- **Principal adverse outcome — recurrence:** ~25–31% after simple curettage, reduced with adjuvants or sclerotherapy (see Finding 3). Recurrences usually manifest within 2 years ([PMID: 37638388](https://pubmed.ncbi.nlm.nih.gov/37638388/); [PMID: 36356178](https://pubmed.ncbi.nlm.nih.gov/36356178/)).
- **Prognostic factors:** anatomic site (spine, pelvis, juxta-articular = higher morbidity and technical difficulty), completeness of local control/resection, and lesion size. Molecular prognostic biomarkers beyond the diagnostic *USP6* fusion are not established.

### 12. Treatment

**Surgical / interventional (mainstay).**
- **Intralesional curettage ± bone grafting** — standard of care; recurrence ~25–31% ([PMID: 37638388](https://pubmed.ncbi.nlm.nih.gov/37638388/)). NCIT: Curettage; Bone Graft.
- **Extended/adjuvant curettage** — high-speed burr, electrocautery, phenol, cryotherapy reduce recurrence (e.g., 4-step spinal technique: 19% vs 50%; [PMID: 32986586](https://pubmed.ncbi.nlm.nih.gov/32986586/); pediatric pelvic extended curettage with excellent outcomes, [PMID: 24817630](https://pubmed.ncbi.nlm.nih.gov/24817630/); femoral head/neck salvage, [PMID: 29416170](https://pubmed.ncbi.nlm.nih.gov/29416170/)).
- **En bloc resection / reconstruction** — for aggressive or recurrent lesions; **Ilizarov bone transport** for large defects ([PMID: 39600861](https://pubmed.ncbi.nlm.nih.gov/39600861/)); avascular/vascular bone grafting ([PMID: 28463677](https://pubmed.ncbi.nlm.nih.gov/28463677/)).
- **Selective arterial embolization** — as adjunct or primary therapy, especially for hypervascular spinal lesions ([PMID: 37638388](https://pubmed.ncbi.nlm.nih.gov/37638388/)).

**Minimally invasive / percutaneous.**
- **Image-guided doxycycline sclerotherapy** — 99% ultimate success, 16% recurrence resolved with repeat treatment; effective for appendicular, pelvic, mandibular, and recurrent lesions ([PMID: 39265785](https://pubmed.ncbi.nlm.nih.gov/39265785/); [PMID: 39311568](https://pubmed.ncbi.nlm.nih.gov/39311568/); [PMID: 39637081](https://pubmed.ncbi.nlm.nih.gov/39637081/)). CHEBI: doxycycline (CHEBI:50845).
- **Percutaneous cryoablation ± protective doxycycline sclerotherapy** — for lesions near critical neurovascular structures ([PMID: 38567007](https://pubmed.ncbi.nlm.nih.gov/38567007/)).
- **Modified single-session sclerograft** (doxycycline ± cryoablation + regenerative grafting) — 25.9% reintervention ([PMID: 42477120](https://pubmed.ncbi.nlm.nih.gov/42477120/)).
- **Osteoconductive cement injection** (e.g., Cerament) for select spinal lesions ([PMID: 24186854](https://pubmed.ncbi.nlm.nih.gov/24186854/)).

**Pharmacotherapy / targeted (mechanism-based).**
- **Denosumab** — human monoclonal anti-**RANKL** antibody. Targets the RANK/RANKL osteoclast axis implicated in ABC bone destruction. Produces symptomatic relief, calcification, size reduction, and devascularization; used as **rescue therapy for recurrent/unresectable disease** and as **neoadjuvant** to enable safer resection of spinal ABC ([PMID: 26730528](https://pubmed.ncbi.nlm.nih.gov/26730528/); [PMID: 36282899](https://pubmed.ncbi.nlm.nih.gov/36282899/); [PMID: 27244112](https://pubmed.ncbi.nlm.nih.gov/27244112/); scoping review [PMID: 39445490](https://pubmed.ncbi.nlm.nih.gov/39445490/)). NCIT: Denosumab (C2724). Caution: rebound and long-term efficacy after cessation remain under study.

> *"The bone destruction in both giant cell tumors of bone and ABCs is mediated by RANK ligand (RANKL) produced by the tumor cells. Denosumab, a human monoclonal antibody to RANKL, is effective in the treatment of giant cell tumors of bone."* — [PMID: 26730528](https://pubmed.ncbi.nlm.nih.gov/26730528/)

**Treatment strategy.** Choice depends on site, size, and aggressiveness. Long-bone/appendicular lesions: curettage + adjuvant or doxycycline sclerotherapy. Spinal/sacral/pelvic lesions: embolization, extended curettage, and/or neoadjuvant denosumab to reduce vascularity and morbidity. Orbital/craniofacial: surgery, embolization, and RANKL inhibition ([PMID: 36356178](https://pubmed.ncbi.nlm.nih.gov/36356178/)).

### 13. Prevention

No primary prevention exists — ABC arises from a sporadic somatic rearrangement with no known modifiable risk factors and no infectious or hereditary basis. **Secondary/tertiary prevention** focuses on early diagnosis and complete local control to prevent recurrence and complications: aggressive adjuvant curettage, sclerotherapy, and post-treatment imaging surveillance (particularly within 2 years). Genetic counseling, carrier/prenatal screening, immunization, and public-health interventions are **not applicable**.

### 14. Other Species / Natural Disease

- **Taxonomy / natural disease:** Aneurysmal bone cysts occur naturally in domestic animals (notably **horses**, *Equus caballus*, NCBI Taxon 9796; and **dogs**, *Canis lupus familiaris*, NCBI Taxon 9615), where they present as expansile, blood-filled osteolytic bone lesions analogous to the human disease (veterinary/OMIA literature). Detailed molecular (USP6) characterization in animals is limited.
- **Orthology:** *USP6* is notable as a **primate-specific/hominoid gene** that arose via a chimeric duplication event; a true one-to-one rodent ortholog is lacking, which constrains conventional mouse modeling (see Section 15).
- **Zoonosis:** not applicable — ABC is neoplastic, not transmissible.

### 15. Model Organisms

- **Xenograft / cell models (primary evidence):** Overexpression of **TRE17/USP6** in cultured cells and **xenograft tumors** recapitulates key ABC features — vascularized, matrix-degrading tumor formation dependent on the USP catalytic domain and NF-κB activation ([PMID: 20418905](https://pubmed.ncbi.nlm.nih.gov/20418905/)). This in vitro/xenograft system is the principal functional model of ABC pathogenesis.
- **Genetic engineering:** transgenic/inducible *USP6*-overexpression constructs are used to study downstream signaling (NF-κB, MMP-9/10, RhoA-ROCK).
- **Limitation:** because *USP6* is essentially primate-specific and acts through a promoter-swap overexpression mechanism, standard rodent knockout models do not naturally reproduce the disease; models rely on **forced human USP6 overexpression** rather than endogenous orthologous mutation. This is a recognized gap.
- **Applications:** these models establish causality of the USP6→NF-κB→MMP axis and provide a platform to test USP6-deubiquitinase inhibitors, NF-κB inhibitors, and RANKL-targeted agents.

---

## Mechanistic Model / Interpretation

```
  Somatic 17p13.2 rearrangement (promoter swap)
  e.g. CDH11 / MYH9 / FAT1 / AHNAK / PAFAH1B1 / FGFR1 promoter  ──►  USP6 (full-length)
                        │  (in myofibroblastic SPINDLE cell only — the neoplastic cell)
                        ▼
             USP6 overexpression  (gain of function; requires deubiquitinase/USP activity)
                        │
             ┌──────────┴───────────┐
             ▼                      ▼
     RhoA / ROCK              NF-κB activation
             └──────────┬───────────┘
                        ▼
        Transcription of MMP-9 / MMP-10  +  pro-angiogenic signaling
                        │
                        ▼
   ECM degradation → blood-filled cystic vascular spaces (aneurysmal architecture)
                        │
                        ▼
     Lesional RANKL production  ──►  recruitment/activation of osteoclast-like GIANT CELLS
                        │                         │
                        ▼                         ▼
              Osteoclastic bone resorption → OSTEOLYSIS, cortical expansion/thinning
                        │
                        ▼
   CLINICAL: pain, swelling, pathologic fracture, neurologic/ophthalmic compromise

      Targeted intervention points:
        • RANKL  ──► DENOSUMAB (blocks osteoclast axis; devascularization/calcification)
        • Cyst cavity ──► DOXYCYCLINE sclerotherapy (also an MMP inhibitor) / cryoablation
        • Whole lesion ──► curettage + adjuvants / embolization / resection
```

Two features of this model are worth emphasizing for a knowledge base. First, the **single-cell specificity** of the driver — *USP6* rearrangement occurs only in the myofibroblastic spindle cell — reframes the giant cells and vascular spaces as **reactive, recruited components** downstream of a myofibroblast-intrinsic oncogenic program. Second, the model unifies **diagnosis and therapy**: the same USP6 lesion that defines primary ABC molecularly (FISH/RNA-seq) sits upstream of the RANKL axis that denosumab targets and the MMP/matrix program that doxycycline sclerotherapy disrupts (doxycycline is itself a known MMP inhibitor, an appealing mechanistic congruence).

---

## Evidence Base

| PMID | Title (abbrev.) | Contribution |
|---|---|---|
| [15509545](https://pubmed.ncbi.nlm.nih.gov/15509545/) | *USP6/CDH11 identify the neoplastic cell in primary ABC* | **Foundational** — clonal 17p13 fusion in 69% of primary ABCs; restricted to spindle cells; absent in secondary ABC. Establishes neoplastic nature and cell of origin. |
| [20418905](https://pubmed.ncbi.nlm.nih.gov/20418905/) | *TRE17/USP6 induces MMPs via NF-κB* | **Foundational mechanism** — USP6 (USP-activity-dependent) activates NF-κB via RhoA/ROCK to induce MMP-9/10; xenografts reproduce ABC. |
| [35941207](https://pubmed.ncbi.nlm.nih.gov/35941207/) | *Update on ABC: pathophysiology, imaging, treatment* | Modern review; 70/30 primary/secondary split; clinical and radiologic synthesis. |
| [41293881](https://pubmed.ncbi.nlm.nih.gov/41293881/) | *Morphomolecular study of 175 USP6-associated neoplasms* | Fusion-partner diversity (22 novel); partner depends on morphology/location. |
| [41432301](https://pubmed.ncbi.nlm.nih.gov/41432301/) | *3 ABCs with novel USP6 partners* | *SEC24D/HNRNPC/ERRFI1::USP6*; all upregulate full-length USP6; SMA+ myofibroblasts. |
| [35102523](https://pubmed.ncbi.nlm.nih.gov/35102523/) | *Solid-variant craniofacial ABC* | *FAT1/MIR22HG::USP6*; NGS superior to FISH for atypical fusions. |
| [38979775](https://pubmed.ncbi.nlm.nih.gov/38979775/) | *Chromothripsis-induced PAFAH1B1::USP6* | Complex rearrangement; solid ABC mimicking osteosarcoma; long-read sequencing. |
| [26730528](https://pubmed.ncbi.nlm.nih.gov/26730528/) | *Response of ABC to denosumab* | RANKL-driven osteolysis; denosumab yields new bone, loss of giant cells. |
| [36282899](https://pubmed.ncbi.nlm.nih.gov/36282899/) | *Neoadjuvant denosumab* | Calcification/devascularization enabling safer spinal resection. |
| [27244112](https://pubmed.ncbi.nlm.nih.gov/27244112/) | *Denosumab for spinal GCT/ABC* | Anti-RANKL reduces tumor size and enables surgery. |
| [37638388](https://pubmed.ncbi.nlm.nih.gov/37638388/) | *Embolization vs curettage* | Baseline curettage recurrence ~25–31%. |
| [39265785](https://pubmed.ncbi.nlm.nih.gov/39265785/) | *Doxycycline sclerotherapy, 14-yr experience* | 99% success; 16% recurrence resolved with repeat doxycycline. |
| [32986586](https://pubmed.ncbi.nlm.nih.gov/32986586/) | *4-step technique, pediatric spinal ABC* | Adjuvant curettage cuts recurrence 50%→19%. |
| [42477120](https://pubmed.ncbi.nlm.nih.gov/42477120/) | *Modified sclerograft* | Single-session; 25.9% reintervention. |
| [24817630](https://pubmed.ncbi.nlm.nih.gov/24817630/) | *Pelvic ABC QoL* | Excellent long-term function (TESS 95, MSTS 93%, SF-36 87%). |
| [22474093](https://pubmed.ncbi.nlm.nih.gov/22474093/) | *Aneurysmal bone cyst (review)* | Clinical/radiologic overview; differential diagnosis; fluid-fluid levels. |

**Evidence source types:** human clinical/pathology series (majority); in vitro + xenograft functional biology ([PMID: 20418905](https://pubmed.ncbi.nlm.nih.gov/20418905/)); molecular cytogenetics ([PMID: 15509545](https://pubmed.ncbi.nlm.nih.gov/15509545/)) and NGS/RNA-seq case series.

---

## Limitations and Knowledge Gaps

1. **No native animal genetic model.** *USP6* is primate/hominoid-specific, so there is no straightforward orthologous rodent knock-in; mechanistic data derive from human-USP6 overexpression and xenografts rather than an endogenous-mutation animal model.
2. **RANKL step is inferred, not fully proven in ABC.** The osteoclast/RANKL branch is strongly supported by denosumab response and analogy to giant cell tumor, but a direct, quantitative demonstration that USP6-driven myofibroblasts produce RANKL to recruit ABC giant cells is less rigorously established than the upstream USP6→NF-κB→MMP steps.
3. **Denosumab durability unknown.** Reported responses are largely from case reports/small series; rebound after discontinuation, optimal duration, and long-term recurrence are not well quantified.
4. **Secondary ABC pathophysiology.** The ~30% of ABC-like lesions lack USP6 and are mechanistically heterogeneous (driven by the host lesion); their biology is under-characterized in this report.
5. **Epidemiology precision.** Prevalence/incidence figures are approximate; ABC is rare and under-registered, and no large population registry estimate was independently derived here.
6. **Fusion-partner functional consequences.** Whether different partners (beyond driving overexpression) confer distinct clinical behavior (e.g., solid variant, site, recurrence) is an open question raised by the partner-diversity literature.
7. **Genotype–phenotype/prognostic biomarkers.** Beyond the diagnostic USP6 fusion, no validated molecular prognostic markers stratify recurrence risk.

---

## Proposed Follow-up Experiments / Actions

1. **Quantify RANKL in USP6-driven ABC** — measure RANKL/OPG expression in laser-capture-microdissected spindle cells vs giant cells to close the inferential gap in the osteoclast branch; correlate with denosumab response.
2. **Prospective denosumab trial with defined stopping rules** — track rebound, radiographic recurrence, and time-to-recurrence after cessation across anatomic sites, especially spine/sacrum.
3. **Partner-stratified outcome study** — pool RNA-seq-characterized ABCs to test whether specific *USP6* partners (e.g., *FGFR1*, *AHNAK*, chromothriptic fusions) associate with solid variant, atypical sites, or recurrence risk.
4. **Head-to-head modality comparison** — prospective/registry comparison of doxycycline sclerotherapy vs adjuvant curettage vs denosumab for matched lesions, with recurrence and QoL (TESS/MSTS/SF-36) endpoints.
5. **Target the USP6 deubiquitinase** — screen USP6 catalytic-domain inhibitors in the TRE17 xenograft model, exploiting the demonstrated dependence of tumorigenesis on USP activity.
6. **Standardize molecular diagnostics** — adopt reflex RNA-seq (not FISH alone) for solid-variant and atypically located lesions to capture non-classical fusions and avoid misdiagnosis as osteosarcoma.
7. **Build a longitudinal ABC registry** to firm up incidence, sex ratio, site distribution, and recurrence timelines with modern molecular confirmation.

---

*Report compiled from molecular cytogenetic, functional, and clinical literature (33 papers reviewed; 3 confirmed findings). Evidence is predominantly human clinical/pathological with supporting in vitro/xenograft functional data. ABC is benign and non-metastatic; the dominant clinical concern is local recurrence, and the unifying biology is somatic USP6 overexpression driving an NF-κB/MMP/RANKL osteolytic program in myofibroblastic spindle cells.*


## Artifacts

- [OpenScientist final report](Aneurysmal_Bone_Cyst-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Aneurysmal_Bone_Cyst-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:15509545
2. PMID:35941207
3. PMID:41293881
4. PMID:35102523
5. PMID:35717456
6. PMID:38979775
7. PMID:36356178
8. PMID:41432301
9. PMID:20418905
10. PMID:37638388
11. PMID:39265785
12. PMID:42477120
13. PMID:32986586
14. PMID:22474093
15. PMID:18761766
16. PMID:24817630
17. PMID:26730528
18. PMID:36282899
19. PMID:16609883
20. PMID:30413280
21. PMID:29416170
22. PMID:39600861
23. PMID:28463677
24. PMID:39311568
25. PMID:39637081
26. PMID:38567007
27. PMID:24186854
28. PMID:27244112
29. PMID:39445490