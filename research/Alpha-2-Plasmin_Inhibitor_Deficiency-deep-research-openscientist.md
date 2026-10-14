---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-12T18:23:31.321077'
end_time: '2026-10-12T18:40:22.282345'
duration_seconds: 1010.96
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Alpha-2-Plasmin Inhibitor Deficiency
  mondo_id: MONDO:0009883
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
citation_count: 19
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Alpha-2-Plasmin_Inhibitor_Deficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Alpha-2-Plasmin_Inhibitor_Deficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Alpha-2-Plasmin Inhibitor Deficiency
- **MONDO ID:** MONDO:0009883 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Alpha-2-Plasmin Inhibitor Deficiency** covering all of the
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

# Alpha-2-Plasmin Inhibitor Deficiency (α2-Antiplasmin Deficiency): A Comprehensive Disease Characterization

**Disease:** Alpha-2-Plasmin Inhibitor Deficiency (α2-antiplasmin deficiency; plasmin inhibitor deficiency)
**MONDO ID:** MONDO:0009883 · **OMIM:** 262850 (disease), 613168 (gene) · **Orphanet:** ORPHA:465 · **Gene:** *SERPINF2* (17p13.3)
**Category:** Mendelian (autosomal recessive)

---

## Summary

Alpha-2-plasmin inhibitor (α2-antiplasmin, α2-AP) deficiency is a rare, autosomal-recessive bleeding disorder caused by biallelic loss-of-function variants in *SERPINF2*, the gene encoding the principal physiological inhibitor of the fibrinolytic protease plasmin. In the normal hemostatic system, α2-antiplasmin restrains clot breakdown by three complementary mechanisms: it forms a rapid, covalent serpin–plasmin complex that neutralizes circulating plasmin; it competitively blocks plasminogen binding to fibrin; and it is cross-linked into the forming fibrin network by activated coagulation factor XIII (FXIIIa), hardening clots against local lysis. When α2-antiplasmin is absent or non-functional, plasmin activity goes unopposed and fibrin clots—though formed normally—are dissolved prematurely. The clinical consequence is a hyperfibrinolytic bleeding diathesis characterized by delayed bleeding after trauma, surgery, or dental extraction, mucosal bleeding, and, in severely affected homozygotes, spontaneous and potentially life-threatening hemorrhage.

The disorder is strongly gene-dose dependent. Homozygous (or compound heterozygous) individuals typically present in early childhood with severe bleeding, while heterozygous individuals may be asymptomatic or bleed excessively only after invasive procedures or trauma later in life. A distinctive and diagnostically useful manifestation is the intramedullary hematoma of long bones, well visualized on MRI. A central diagnostic challenge is that routine coagulation screening tests—prothrombin time (PT), activated partial thromboplastin time (aPTT), platelet count/function, and von Willebrand factor—are all normal, so the disease is frequently misdiagnosed or recognized only after decades of diagnostic delay. Specific diagnosis requires an α2-antiplasmin functional activity assay or *SERPINF2* sequencing; global viscoelastic tests (thromboelastography/ROTEM) showing accelerated clot lysis can prompt detection.

Prognosis is generally favorable once the diagnosis is made, because antifibrinolytic agents (tranexamic acid, ε-aminocaproic acid) that prevent plasminogen binding to fibrin effectively stabilize clots and permit even major surgery to be performed safely with planned prophylaxis. Beyond hemostasis, α2-antiplasmin has emerged as a pleiotropic regulator of tissue remodeling—promoting fibrosis and endothelial-to-mesenchymal transition and modulating ischemic brain injury—making it both a disease gene and a therapeutic target of growing interest. A naturally occurring *SERPINF2* missense variant causes an analogous delayed postoperative hemorrhage syndrome in Scottish deerhounds, and α2-antiplasmin knockout mice recapitulate key aspects of the human biology, providing validated comparative and model systems.

---

## Section 1 — Disease Information

**Overview.** Alpha-2-antiplasmin deficiency is the most severe inherited disorder of the fibrinolytic system. It results from the inability to inhibit plasmin, leading to excess (unregulated) fibrinolysis and premature clot breakdown ([PMID: 31427261](https://pubmed.ncbi.nlm.nih.gov/31427261/); [PMID: 42257473](https://pubmed.ncbi.nlm.nih.gov/42257473/)). As stated in the literature, *"The most severe clinical phenotype is caused by α2-Antiplasmin (α2-AP) deficiency which results in excess fibrinolysis due to the inability to inhibit plasmin"* ([PMID: 31427261](https://pubmed.ncbi.nlm.nih.gov/31427261/)).

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0009883 |
| OMIM (disease) | 262850 |
| OMIM (gene) | 613168 |
| Orphanet | ORPHA:465 (prevalence listed <1/1,000,000) |
| Gene / HGNC | *SERPINF2* (alias α2-AP, PLI, AAP, API) |
| Cytogenetic locus | 17p13.3 |

**Synonyms / alternative names.** Alpha-2-antiplasmin deficiency; α2-plasmin inhibitor deficiency; plasmin inhibitor deficiency; congenital α2-AP deficiency; "Miyasato disease" (historical name for the first reported homozygous case). Named variant alleles include "α2AP Enschede" and "α2AP Artas."

**Source of information.** The characterization is derived predominantly from aggregated disease-level resources (OMIM, Orphanet) and from the primary literature consisting of individual case reports and small case series, consolidated by a 2020 literature survey of 123 cases across 33 publications ([PMID: 33337837](https://pubmed.ncbi.nlm.nih.gov/33337837/)). There is no large EHR-derived cohort; the evidence base is necessarily patient-level and aggregated from scattered reports.

---

## Section 2 — Etiology

**Primary cause (genetic).** The disease is monogenic and Mendelian: biallelic pathogenic variants in *SERPINF2* cause the severe (homozygous) phenotype, while a single pathogenic allele produces a milder, often provoked bleeding tendency. *"Both these disorders are rare and have an autosomal recessive pattern of inheritance"* ([PMID: 31427261](https://pubmed.ncbi.nlm.nih.gov/31427261/)). There is no infectious or environmental cause of the inherited disease; the molecular lesion is a loss of α2-antiplasmin function.

**Genetic risk factors.** The causal variants are the *SERPINF2* pathogenic alleles themselves. Variants are largely private to individual families (see Section 4). No independent susceptibility loci or validated modifier genes have been established for the Mendelian disorder.

**Environmental / lifestyle risk factors.** These are better described as *triggers of bleeding episodes* rather than causes of disease: trauma, surgery, dental extraction, and other invasive procedures provoke the characteristic delayed bleeding ([PMID: 33337837](https://pubmed.ncbi.nlm.nih.gov/33337837/)). Consanguinity increases the likelihood of homozygous severe disease.

**Protective factors.** The pharmacological "protective" factor against bleeding is antifibrinolytic therapy (functionally restoring the fibrinolytic brake). No naturally occurring genetic protective modifier alleles have been defined. Conversely—and notably for the inverse disease biology—reduced α2-antiplasmin is *protective* against fibrosis and may enhance thrombolysis (see Section 6).

**Gene–environment interactions.** The dominant interaction is genotype × hemostatic challenge: homozygotes bleed spontaneously and after minor insults; heterozygotes typically bleed only when a procedural or traumatic challenge is superimposed on their partial deficiency ([PMID: 33337837](https://pubmed.ncbi.nlm.nih.gov/33337837/)).

---

## Section 3 — Phenotypes

The core phenotype is a hemorrhagic diathesis. Severity is gene-dose dependent, and routine laboratory screens are characteristically normal, making the *absence* of standard laboratory abnormalities itself a clinical clue.

| Phenotype | Type | Onset / severity / frequency | Suggested HPO term |
|---|---|---|---|
| Delayed post-surgical / post-traumatic bleeding | Clinical sign | Hallmark; homozygotes from early childhood | HP:0004846 / HP:0011889 (abnormal bleeding/diathesis) |
| Prolonged bleeding after dental extraction | Clinical sign | Common provoked manifestation | HP:0006298 (prolonged bleeding following procedure) |
| Mucosal / gingival bleeding, epistaxis | Clinical sign | Variable | HP:0000421 (epistaxis), HP:0000225 (gingival bleeding) |
| Intramedullary hematoma of long bones | Physical/imaging manifestation | Distinctive; reported in children | HP:0001892 context (abnormal bleeding of bone) |
| Intracranial hemorrhage | Clinical sign | Rare, severe, homozygotes | HP:0002170 (intracranial hemorrhage) |
| Hemarthrosis / soft-tissue hematoma | Clinical sign | Variable | HP:0003261 relevant |
| Low α2-antiplasmin activity | Laboratory abnormality | Diagnostic; constant | (diagnostic assay) |

**Age of onset / severity / progression.** *"Homozygous patients develop symptomatology in early childhood, while heterozygous individuals may be asymptomatic or bleed profusely following invasive dental procedures, surgery or trauma late in life"* ([PMID: 33337837](https://pubmed.ncbi.nlm.nih.gov/33337837/)). The disease is chronic and lifelong; bleeding is episodic and provoked rather than steadily progressive.

**Distinctive manifestation — intramedullary hematoma.** *"Intramedullary hematomas of long bones have been described in α2-plasmin inhibitor or fibrinogen deficiencies"* ([PMID: 21873355](https://pubmed.ncbi.nlm.nih.gov/21873355/)). A detailed pediatric case described a 6-year-old boy with intramedullary hematoma of the left femoral diaphysis, presenting with pain without swelling and no trauma ([PMID: 9880645](https://pubmed.ncbi.nlm.nih.gov/9880645/)).

**Quality-of-life impact.** Disease-specific QoL instruments have not been reported for this ultra-rare disorder. QoL impact derives from unpredictable bleeding, transfusion dependence in unrecognized disease, and procedural risk; with antifibrinolytic prophylaxis, most patients function well.

---

## Section 4 — Genetic / Molecular Information

**Causal gene.** *SERPINF2* (serpin family F member 2), 17p13.3; OMIM gene 613168. It encodes α2-antiplasmin, a secreted serpin.

**Pathogenic variants — heterogeneity and classes.** Disease-causing variants are typically *private* to each family—no single recurrent founder allele dominates globally—and span the full spectrum of classes: missense, nonsense, frameshift (insertion/deletion), and splice-site mutations ([PMID: 10583218](https://pubmed.ncbi.nlm.nih.gov/10583218/); [PMID: 12544738](https://pubmed.ncbi.nlm.nih.gov/12544738/)).

| Variant (name) | Class | Functional consequence | Evidence |
|---|---|---|---|
| p.Val384Met | Missense (P8′, near reactive site) | Activity 49–66% of normal; antigen 57–68%; bleeding | [PMID: 10583218](https://pubmed.ncbi.nlm.nih.gov/10583218/) |
| Intron 6 splice-donor ("α2AP Artas") | Splice-site → exon 6 skipping | Heterozygous deficiency, bleeding | [PMID: 12544738](https://pubmed.ncbi.nlm.nih.gov/12544738/) |
| "α2AP Enschede" | Frameshift (insertion) | Dysfunctional protein secreted but non-inhibitory | historical classic variant |
| p.Arg6Trp | Polymorphism (allele freq ~0.19) | Affects N-terminal cleavage; benign | [PMID: 33992873](https://pubmed.ncbi.nlm.nih.gov/33992873/) |

The P1 reactive-center residue is Arg376: *"The amino acid Val384 is located eight residues C-terminal (P8′) of the P1 residue (Arg376) in the reactive site"* ([PMID: 10583218](https://pubmed.ncbi.nlm.nih.gov/10583218/)), and heterozygous carriers showed that *"The plasma plasmin inhibitor activities of the affected family members were reduced to 49–66% of normal"* ([PMID: 10583218](https://pubmed.ncbi.nlm.nih.gov/10583218/)). A splice mechanism is documented as *"a splicing donor site mutation of intron 6, leading to exon 6 skipping"* ([PMID: 12544738](https://pubmed.ncbi.nlm.nih.gov/12544738/)).

**Functional consequences.** Variants act by loss of function—either quantitative deficiency (reduced secretion/antigen) or qualitative dysfunction (normal secretion but loss of plasmin-inhibitory activity, as in Enschede). Origin is germline.

**Benign polymorphisms.** p.Arg6Trp, p.Ala-26Val, p.Arg407Lys are population polymorphisms; p.Arg6Trp modulates the rate of N-terminal proteolytic processing but is not disease-causing.

**Modifier genes / epigenetics / chromosomal abnormalities.** No validated disease-modifier genes, disease-specific epigenetic marks, or recurrent chromosomal abnormalities have been established for this Mendelian disorder (not applicable / not available).

---

## Section 5 — Environmental Information

The inherited disease has no environmental, toxic, or infectious cause. Environmental factors are relevant only as **bleeding triggers** (trauma, surgery, dental procedures). Of note, an *acquired*, phenocopy state of low α2-antiplasmin/hyperfibrinolysis can arise from malignancy (e.g., disseminated adenocarcinoma with hyperfibrinogenolysis, [PMID: 9663712](https://pubmed.ncbi.nlm.nih.gov/9663712/)) and from severe factor XIII deficiency (which impairs α2-AP cross-linking to fibrin), but these are distinct from the congenital *SERPINF2* disorder. No infectious agents are implicated.

---

## Section 6 — Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic loss-of-function variant in *SERPINF2*** leads to **absent or non-functional α2-antiplasmin protein** (quantitative deficiency or dysfunctional secreted serpin). *[demonstrated]*
2. **Loss of α2-antiplasmin** removes all three physiological brakes on plasmin — it can no longer (i) form a covalent serpin–plasmin complex, (ii) block plasminogen binding to fibrin, or (iii) be FXIIIa-cross-linked into fibrin ([PMID: 42257473](https://pubmed.ncbi.nlm.nih.gov/42257473/)). → **results in unopposed, unregulated plasmin activity.** *[demonstrated]*
3. **Unopposed plasmin** → clots form normally but are **prematurely degraded (hyperfibrinolysis)** ([PMID: 42257473](https://pubmed.ncbi.nlm.nih.gov/42257473/)). *[demonstrated]*
4. **Premature clot breakdown** → **delayed bleeding** after an initial hemostatic plug forms and then dissolves, and spontaneous hemorrhage in severe deficiency. *[demonstrated clinically]*
5. **Branch (gene dose):** homozygotes → severe early-childhood/spontaneous bleeding; heterozygotes → provoked bleeding ([PMID: 33337837](https://pubmed.ncbi.nlm.nih.gov/33337837/)). *[demonstrated]*
6. **Branch (pleiotropy, inferred from models):** reduced α2-AP → altered VEGF/angiogenesis in wound healing; reduced fibrosis/EndoMT; enhanced thrombolysis and modulated reperfusion brain injury ([PMID: 16839360](https://pubmed.ncbi.nlm.nih.gov/16839360/); [PMID: 34709571](https://pubmed.ncbi.nlm.nih.gov/34709571/); [PMID: 42589214](https://pubmed.ncbi.nlm.nih.gov/42589214/)). *[model-based]*

### Molecular detail

The three-pronged inhibitory mechanism is the heart of the pathophysiology: *"α2AP restrains fibrinolysis by (i) forming a covalent serpin complex with plasmin, (ii) blocking plasminogen binding to fibrin, and (iii) undergoing factor XIIIa-mediated cross-linking into fibrin to harden clots against local lysis"* ([PMID: 42257473](https://pubmed.ncbi.nlm.nih.gov/42257473/)). Deficiency produces *"a rare fibrinolytic disorder characterized by unregulated plasmin activity and premature clot breakdown"* ([PMID: 42257473](https://pubmed.ncbi.nlm.nih.gov/42257473/)).

**Protein structure–function.** The 2.65 Å crystal structure shows α2-antiplasmin is an unusual serpin with long N- and C-terminal extensions flanking the central serpin domain: *"The N-terminal sequence is crosslinked to fibrin by factor XIIIa, whereas the C-terminal region mediates the initial interaction with plasmin"* ([PMID: 18063751](https://pubmed.ncbi.nlm.nih.gov/18063751/)). The serpin reactive-center loop presents P1 Arg376 to plasmin's active site. Circulating α2-AP is heterogeneous: *"C-terminal cleavage converts the plasminogen-binding form (PB-α2-PI) to a non-plasminogen-binding form (NPB-α2-PI)"* ([PMID: 33992873](https://pubmed.ncbi.nlm.nih.gov/33992873/)); N-terminal cleavage by fibroblast activation protein yields a shorter form cross-linked to fibrin faster.

**Pathway / process / cell types.** Core pathway: the plasminogen–plasmin fibrinolytic system intersecting with FXIIIa-mediated fibrin stabilization. Cell types: hepatocytes (synthesis of plasma α2-AP), platelets (FXIII-A pool contributing to cross-linking), endothelium and fibroblasts (pleiotropic remodeling roles). Suggested GO terms: **GO:0042730 (fibrinolysis)**, **GO:0051918 (negative regulation of fibrinolysis)**, **GO:0010951 (negative regulation of endopeptidase activity)**, **GO:0007596 (blood coagulation)**. Suggested CL terms: **CL:0000182 (hepatocyte)**, **CL:0000233 (platelet)**, **CL:0000115 (endothelial cell)**, **CL:0000057 (fibroblast)**. Chemical entities (CHEBI): tranexamic acid (**CHEBI:48669**), ε-aminocaproic acid (**CHEBI:28483**).

**Pleiotropy beyond hemostasis (model evidence).** α2-AP regulates cell differentiation, cytokine production, ECM metabolism, and endothelial homeostasis. *"the blockade of α2-antiplasmin suppresses fibrosis progression and vascular dysfunction in systemic sclerosis model mice"* ([PMID: 35330147](https://pubmed.ncbi.nlm.nih.gov/35330147/)); *"α2AP deficiency attenuated EndoMT and fibrosis progression in DN model mice"* ([PMID: 34709571](https://pubmed.ncbi.nlm.nih.gov/34709571/)); and in stroke, *"inhibition of α2AP with a specific monoclonal antibody caused a synergistic increase in TNK-tPA-mediated clot dissolution"* ([PMID: 42589214](https://pubmed.ncbi.nlm.nih.gov/42589214/)). These establish that α2-AP loss is deleterious for hemostasis but beneficial in fibrotic/thrombotic contexts—a therapeutic double-edged sword.

---

## Section 7 — Anatomical Structures Affected

- **Body system:** hematologic / cardiovascular (blood and vasculature). Suggested UBERON: **UBERON:0000178 (blood)**, **UBERON:0001969 (blood plasma)**.
- **Primary sites of bleeding:** mucosal surfaces (oral/gingival, nasal), skin and soft tissue (hematoma), joints (hemarthrosis), **bone marrow cavity of long bones** (intramedullary hematoma — a distinctive localization; **UBERON:0002371 bone marrow**, long bone diaphysis), and the central nervous system (intracranial hemorrhage, severe cases).
- **Secondary involvement:** organs subject to post-procedural bleeding (e.g., prostate after prostatectomy, lung during transplantation).
- **Tissue/cell level:** no fixed tissue lesion; the "target" is the fibrin clot wherever it forms. Relevant cells: hepatocyte (source), platelet/endothelium/fibroblast (modulators).
- **Subcellular / localization:** α2-AP is a secreted, extracellular plasma protein (GO cellular component **GO:0005615 extracellular space**); it acts in plasma and within the fibrin matrix. Bleeding lateralization is not fixed—manifestations are determined by site of hemostatic challenge.

---

## Section 8 — Temporal Development

- **Onset:** congenital/genetic; clinical onset in **early childhood** for homozygotes, later and provoked for heterozygotes ([PMID: 33337837](https://pubmed.ncbi.nlm.nih.gov/33337837/)).
- **Onset pattern of bleeds:** characteristically **delayed** after the inciting event (clot forms, then lyses).
- **Course:** chronic, lifelong; **episodic/provoked** bleeding rather than continuous progression. No disease "stages" in the oncologic sense.
- **Remission patterns:** bleeding episodes resolve with antifibrinolytic treatment (treatment-induced control); the underlying deficiency does not remit.
- **Critical periods / windows for intervention:** peri-procedural and peri-traumatic windows are the key opportunities—prophylaxis before surgery/dental work prevents the delayed bleed ([PMID: 15357795](https://pubmed.ncbi.nlm.nih.gov/15357795/)).

---

## Section 9 — Inheritance and Population

- **Inheritance:** autosomal recessive; severe disease in homozygotes/compound heterozygotes, mild/variable in heterozygotes ([PMID: 31427261](https://pubmed.ncbi.nlm.nih.gov/31427261/)).
- **Epidemiology:** ultra-rare; Orphanet lists prevalence **<1/1,000,000** (ORPHA:465). No formal incidence established. A 2020 survey found only **123 patients in 33 publications** ([PMID: 33337837](https://pubmed.ncbi.nlm.nih.gov/33337837/)): *"Thirty-three publications were identified encompassing one hundred twenty-three patients."*
- **History / geography:** first discovered in **Japan** (Koie, Aoki and colleagues; first homozygous case "Miyasato disease," 1978–1979). Reported subsequently across multiple ethnicities (Japanese, Indian, Sudanese, European, UK), with **consanguineous families enriched** among severe homozygous cases ([PMID: 19141165](https://pubmed.ncbi.nlm.nih.gov/19141165/)): *"Congenital deficiency of alpha(2)-antiplasmin causes a rare bleeding disorder because of increased fibrinolysis."*
- **Penetrance / expressivity:** homozygous disease is highly penetrant for bleeding; expressivity is **variable** and strongly gene-dose dependent. Heterozygotes show reduced penetrance (often only provoked bleeding).
- **Founder effects / recurrent alleles:** none dominant; variants are largely private (Section 4).
- **Sex ratio / age distribution:** no strong sex predilection reported (autosomal); affected individuals span childhood (homozygotes) to adulthood (heterozygotes diagnosed after procedures).

---

## Section 10 — Diagnostics

**The central diagnostic pitfall:** routine coagulation screening is **normal**. *"Her evaluation showed normal coagulation studies, platelet function, and von Willebrand factor assays, with persistently low α2AP activity and a homozygous SERPINF2 variant confirming the diagnosis"* ([PMID: 42257473](https://pubmed.ncbi.nlm.nih.gov/42257473/)). This causes frequent misdiagnosis (e.g., as von Willebrand disease) and diagnostic delay often spanning decades.

**Recommended diagnostic approach.**

| Test | Role | Expected result |
|---|---|---|
| PT, aPTT, platelet count/function, VWF | Screening | **Normal** (hence misleading) |
| **α2-antiplasmin functional activity assay** | **Confirmatory** | **Low / absent** |
| α2-AP antigen (ELISA) | Distinguishes quantitative vs dysfunctional | Low (type I) or normal (type II dysfunctional) |
| **Thromboelastography / ROTEM** | Global screen that can flag the defect | **Accelerated clot lysis** |
| ***SERPINF2* sequencing** | **Definitive genetic diagnosis** | Biallelic (severe) or single pathogenic variant |
| MRI (for intramedullary hematoma) | Imaging of distinctive lesion | T1/T2 hyperintense medullary signal |

Viscoelastic testing can be the entry point to diagnosis: a novel *SERPINF2* variant was detected after *"Abnormal fibrinolysis recognized by thromboelastography in a case of severe bleeding with normal coagulation and platelet function"* ([PMID: 31282989](https://pubmed.ncbi.nlm.nih.gov/31282989/)). For the intramedullary hematoma, *"MRI is diagnostic with the haematoma generating a specific hyperintense signal on T1-weighted and T2-weighted spin-echo images"* ([PMID: 9880645](https://pubmed.ncbi.nlm.nih.gov/9880645/)).

**Genetic testing utility.** Single-gene *SERPINF2* testing is the targeted approach once the functional assay points to α2-AP deficiency; WES/WGS or small bleeding-disorder gene panels are useful when the phenotype is undifferentiated. CMA, karyotyping, FISH, mtDNA, and repeat-expansion testing are not applicable.

**Differential diagnosis.** Plasminogen activator inhibitor-1 (PAI-1) deficiency (the other inherited hyperfibrinolytic bleeding disorder), factor XIII deficiency (impaired α2-AP cross-linking; also normal PT/aPTT), mild von Willebrand disease, and acquired hyperfibrinolysis (malignancy, liver disease, DIC "bleeding type").

---

## Section 11 — Outcome / Prognosis

Prognosis is **generally good when the diagnosis is known and antifibrinolytic prophylaxis is applied.** The disorder is chronic and lifelong, but major surgery can be performed safely: a congenital α2-PI-deficient patient underwent single-lung transplantation with prophylactic fresh frozen plasma plus tranexamic acid and ROTEM monitoring, with an uneventful course—*"Lung transplantation for a patient with α2-PI deficiency was safely performed with the use of planned FFP transfusion and tranexamic acid"* ([PMID: 40589561](https://pubmed.ncbi.nlm.nih.gov/40589561/)).

The **principal danger is unrecognized disease**: severe bleeding with normal screening tests leads to diagnostic delay, transfusion dependence, and risk of life-threatening hemorrhage (including intracranial and intramedullary bleeds) in homozygotes. *"Management of such patients may be challenging especially when the diagnosis of alpha-2 antiplasmin deficiency is not known"* ([PMID: 33337837](https://pubmed.ncbi.nlm.nih.gov/33337837/)).

- **Mortality / survival:** no formal survival statistics for this ultra-rare disease; mortality risk is driven by severe unrecognized hemorrhage, which is largely preventable with treatment.
- **Morbidity:** bleeding-related disability, anemia, transfusion burden; well controlled once recognized.
- **Prognostic factors:** genotype (homozygous vs heterozygous), residual α2-AP activity, and—critically—whether the diagnosis is established before a major hemostatic challenge.

---

## Section 12 — Treatment

**Mainstay — antifibrinolytics.** Tranexamic acid and ε-aminocaproic acid are first-line and mechanistically rational, substituting pharmacologically for the missing fibrinolytic brake: *"Antifibrinolytic agents, such as tranexamic acid or ε-aminocaproic acid, are the mainstays of treatment which inhibit fibrinolysis by preventing the binding of plasminogen to fibrin and thereby stabilizing the fibrin clot"* ([PMID: 31427261](https://pubmed.ncbi.nlm.nih.gov/31427261/)).

**Evidence-based procedural dosing (dental extraction).** *"we advocate that 7.5–10 mg kg⁻¹ of tranexamic acid be administered orally every 6 h, starting 3 h before surgery and continuing for about 7 days"* ([PMID: 15357795](https://pubmed.ncbi.nlm.nih.gov/15357795/)); continuous post-extraction bleeding is managed with IV tranexamic acid ~20 mg/kg.

**Major surgery.** Perioperative management combines prophylactic FFP plus tranexamic acid with viscoelastic (ROTEM) monitoring ([PMID: 40589561](https://pubmed.ncbi.nlm.nih.gov/40589561/)).

**Suggested NCIT terms:** tranexamic acid (**NCIT:C47748**), aminocaproic acid (**NCIT:C28987**), fresh frozen plasma transfusion.

**Not applicable / none established:** no gene therapy, cell therapy, RNA therapy, targeted biologic, or α2-AP replacement product is approved for this indication. (Interestingly, α2-AP *inhibition* is being explored as a therapy for other diseases—stroke, fibrosis—the therapeutic inverse of this deficiency.) Pharmacogenomics: none specific.

---

## Section 13 — Prevention

- **Primary prevention:** not possible for a congenital genetic disorder; **genetic counseling** and carrier assessment in consanguineous or affected families are the key tools. Prenatal/preimplantation testing is feasible when the familial *SERPINF2* variant is known.
- **Secondary prevention (early detection):** recognizing the phenotype (bleeding with normal screens) and confirming with α2-AP activity assay / sequencing prevents morbidity; **cascade testing** of relatives identifies at-risk individuals.
- **Tertiary prevention (preventing complications):** **peri-procedural antifibrinolytic prophylaxis** is the central preventive intervention—administering tranexamic acid before dental work, surgery, or after trauma prevents the delayed bleed ([PMID: 15357795](https://pubmed.ncbi.nlm.nih.gov/15357795/)).
- **Immunization / public health / environmental:** not applicable.

---

## Section 14 — Other Species / Natural Disease

A naturally occurring, closely analogous disorder exists in dogs. Whole-genome-sequencing GWAS in **269 Scottish deerhounds** mapped **delayed postoperative hemorrhage (DEPOH)** to a chromosome-9 locus, with ***SERPINF2*** as the causal gene: *"One of these genes (SERPINF2 encoding alpha-2 antiplasmin) was directly linked to the pathophysiology of DEPOH"* ([PMID: 36780177](https://pubmed.ncbi.nlm.nih.gov/36780177/)). The missense variant **c.605C>T (p.A202V)** shows a strong gene-dose effect: *"the likelihood of DEPOH was significantly higher for dogs with the T/T genotype (odds ratio [OR] = 1235; 95% confidence interval [CI] = 23–6752; P = 0.0005)"* ([PMID: 36780177](https://pubmed.ncbi.nlm.nih.gov/36780177/)); heterozygotes OR = 28 (95% CI 1.4–542, P = 0.03).

- **Taxonomy:** *Canis lupus familiaris* (NCBI Taxon 9615); model mouse *Mus musculus* (NCBI Taxon 10090).
- **Breed:** Scottish deerhound (VBO term applicable).
- **Orthologous gene:** canine and murine *Serpinf2*.
- **Comparative biology:** the canine disorder recapitulates the human delayed-bleeding, gene-dose-dependent phenotype, confirming evolutionary conservation of α2-AP's hemostatic role and offering a naturally occurring veterinary model. No zoonotic potential (genetic disease).

---

## Section 15 — Model Organisms

**α2-antiplasmin knockout mouse (α2AP⁻/⁻).** This is the principal validated mammalian model. Beyond confirming the hemostatic phenotype, it revealed pleiotropic roles: *"an accelerated wound closure was observed in alpha(2)AP-deficient (alpha(2)AP⁻/⁻) mice in comparison with wild type (WT) mice"* and *"The lack of alpha(2)AP markedly causes an over-release of VEGF from the fibroblasts in cutaneous wound lesions, thereby inducing angiogenesis around the area"* ([PMID: 16839360](https://pubmed.ncbi.nlm.nih.gov/16839360/)). The same genetic model has been used to show reduced fibrosis/EndoMT in diabetic nephropathy ([PMID: 34709571](https://pubmed.ncbi.nlm.nih.gov/34709571/)) and attenuated fibrosis in systemic-sclerosis models ([PMID: 35330147](https://pubmed.ncbi.nlm.nih.gov/35330147/)).

| Model | Type | Recapitulation | Use | Resource |
|---|---|---|---|---|
| α2AP⁻/⁻ mouse | Knockout, mammalian | Hyperfibrinolytic tendency; +wound-healing/angiogenesis, −fibrosis phenotypes | Mechanism, therapeutics | MGI |
| Scottish deerhound (natural) | Spontaneous, canine | Delayed postoperative hemorrhage, gene-dose | Natural disease, genetics | OMIA/VetCompass |
| Murine crystal structure (protein) | In vitro/structural | Serpin domain architecture | Structure–function | PDB |

**Limitations of models:** mouse and dog capture hemostatic and remodeling biology, but species differences in fibrinolytic kinetics and clinical bleeding thresholds mean human dosing/management cannot be read directly from models.

---

## Mechanistic Model / Interpretation

```
  SERPINF2 biallelic LOF variant
            │ (demonstrated)
            ▼
  Absent / non-functional α2-antiplasmin
            │  removes 3 brakes on plasmin:
            │   (i) covalent plasmin inhibition
            │   (ii) block plasminogen→fibrin binding
            │   (iii) FXIIIa cross-link into fibrin
            ▼
  Unopposed, unregulated plasmin activity
            │
            ▼
  Fibrin clots form normally → prematurely LYSED (hyperfibrinolysis)
            │
   ┌────────┴─────────────┐
   ▼                      ▼
 HOMOZYGOTE             HETEROZYGOTE
 severe, early-childhood,   mild / provoked bleeding
 spontaneous bleeding       (surgery, dental, trauma)
 (incl. intracranial,
  intramedullary hematoma)
            │
            ▼
  DELAYED bleeding (plug forms, then dissolves)
  with NORMAL PT/aPTT/platelets/VWF  → diagnostic delay
            │
            ▼
  Treatment: antifibrinolytics (TXA / EACA)
  pharmacologically restore the fibrinolytic brake → good prognosis

  PLEIOTROPY (model-based): ↓α2-AP → ↑VEGF/angiogenesis (wound healing),
  ↓fibrosis/EndoMT, ↑thrombolysis — therapeutic inverse of the deficiency
```

The unifying concept is a **quantitative imbalance in fibrinolysis**: α2-AP is the dominant, fastest-acting plasmin inhibitor, and its loss shifts the clot formation↔dissolution equilibrium toward dissolution. Because coagulation itself is intact, standard tests are normal and the defect is "invisible" unless fibrinolysis is specifically interrogated. The same biology that makes α2-AP essential for clot stability makes it a liability in fibrotic and thrombotic disease—explaining the active interest in α2-AP inhibition as therapy elsewhere.

---

## Evidence Base

| PMID | Role in this report |
|---|---|
| [31427261](https://pubmed.ncbi.nlm.nih.gov/31427261/) | Defines α2-AP deficiency as most severe inherited fibrinolytic disorder; AR inheritance; antifibrinolytic mainstay |
| [42257473](https://pubmed.ncbi.nlm.nih.gov/42257473/) | Three-mechanism model; premature clot breakdown; diagnostic delay case with normal screens + homozygous *SERPINF2* |
| [33337837](https://pubmed.ncbi.nlm.nih.gov/33337837/) | Literature survey of 123 cases; gene-dose phenotype; management challenge when undiagnosed |
| [15357795](https://pubmed.ncbi.nlm.nih.gov/15357795/) | Evidence-based tranexamic acid dosing for dental extractions |
| [31282989](https://pubmed.ncbi.nlm.nih.gov/31282989/) | TEG/thromboelastography detection leading to novel *SERPINF2* variant |
| [16839360](https://pubmed.ncbi.nlm.nih.gov/16839360/) | α2AP⁻/⁻ mouse: accelerated wound healing via VEGF/angiogenesis |
| [36780177](https://pubmed.ncbi.nlm.nih.gov/36780177/) | Natural canine disease (Scottish deerhound DEPOH); *SERPINF2* p.A202V; OR quantification |
| [18063751](https://pubmed.ncbi.nlm.nih.gov/18063751/) | Crystal structure; N-terminal FXIIIa cross-link vs C-terminal plasmin binding |
| [33992873](https://pubmed.ncbi.nlm.nih.gov/33992873/) | PB→NPB heterogeneity; polymorphisms affecting processing |
| [19141165](https://pubmed.ncbi.nlm.nih.gov/19141165/) | Rarity; increased fibrinolysis mechanism; historical context |
| [9880645](https://pubmed.ncbi.nlm.nih.gov/9880645/) | Intramedullary hematoma case; MRI diagnostic |
| [10583218](https://pubmed.ncbi.nlm.nih.gov/10583218/) | Missense p.Val384Met near reactive-site Arg376; 49–66% activity |
| [12544738](https://pubmed.ncbi.nlm.nih.gov/12544738/) | Splice-site variant (Artas) → exon 6 skipping |
| [21873355](https://pubmed.ncbi.nlm.nih.gov/21873355/) | Intramedullary hematoma as rare manifestation |
| [35330147](https://pubmed.ncbi.nlm.nih.gov/35330147/) | α2-AP blockade antifibrotic in systemic sclerosis model |
| [34709571](https://pubmed.ncbi.nlm.nih.gov/34709571/) | α2-AP deficiency attenuates EndoMT/fibrosis (diabetic nephropathy) |
| [42589214](https://pubmed.ncbi.nlm.nih.gov/42589214/) | α2-AP limits thrombolysis; anti-α2AP synergizes with tenecteplase |
| [40589561](https://pubmed.ncbi.nlm.nih.gov/40589561/) | Safe lung transplant with FFP + TXA (favorable prognosis) |

Evidence source types span **human clinical** (case reports/series, surveys), **model organism** (knockout mouse, natural canine disease), **in vitro/structural** (crystal structure, cross-linking biochemistry), and **computational/aggregated** (GWAS, literature survey).

---

## Limitations and Knowledge Gaps

1. **Ultra-rarity and evidence quality.** The entire human evidence base rests on ~123 reported patients and scattered case reports; there are no randomized trials, no prospective natural-history cohorts, and no formal incidence/prevalence or survival statistics.
2. **Genotype–phenotype correlation is incomplete.** Variants are largely private; residual-activity thresholds that predict spontaneous vs provoked bleeding are not precisely defined.
3. **No validated modifiers / epigenetics.** Disease-modifier genes and epigenetic contributions are unexplored.
4. **QoL and long-term outcomes** are undocumented with standardized instruments.
5. **Dosing evidence** is extrapolated from small series; optimal long-term antifibrinolytic regimens and thrombotic risk of chronic prophylaxis are not rigorously established.
6. **Pleiotropy** findings derive mainly from mouse models; their relevance to human α2-AP-deficient patients (e.g., altered wound healing or fibrosis) has not been systematically assessed in patients.

---

## Proposed Follow-up Experiments / Actions

1. **Establish an international patient registry** for *SERPINF2* deficiency to capture genotype, residual α2-AP activity, bleeding phenotype, treatment, and outcomes—enabling genotype–phenotype and natural-history analyses.
2. **Standardize diagnostics:** promote reflex α2-AP functional activity testing (and TEG/ROTEM screening) in patients with bleeding plus normal PT/aPTT/VWF to shorten the diagnostic delay; curate a *SERPINF2* variant database with ACMG classifications.
3. **Characterize residual-activity thresholds** correlating α2-AP activity with spontaneous-bleeding risk to guide prophylaxis intensity.
4. **Prospective evaluation of antifibrinolytic prophylaxis** regimens (dose, duration, route) around surgery and dental procedures, including thrombotic safety.
5. **Leverage the Scottish deerhound natural model and α2AP⁻/⁻ mouse** for preclinical testing of α2-AP repletion strategies and to study the pleiotropic wound-healing/fibrosis phenotypes relevant to human patients.
6. **Clinical awareness in human/veterinary cross-talk:** apply the canine *SERPINF2* p.A202V finding to screen at-risk deerhound lines, and use comparative data to refine human variant interpretation.

---

*Report prepared from a 5-iteration autonomous investigation (13 confirmed findings, 54 papers reviewed). Evidence is drawn exclusively from the cited primary literature; claims are attributed only to papers whose abstracts/quotes were verified during the investigation.*


## Artifacts

- [OpenScientist final report](Alpha-2-Plasmin_Inhibitor_Deficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Alpha-2-Plasmin_Inhibitor_Deficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 19 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 19 |
| On topic | 11 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 26 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 1 |
| Terms whose name was checked | 13 |
| Terms named correctly | 11 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0009883` (3 mentions) - the report calls it "if available", "MONDO"; MONDO calls it **alpha-2-plasmin inhibitor deficiency**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005615` (obsolete extracellular space) (1 mention) - replaced by `GO:0005576`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0006298` (1 mention) - the report calls it "prolonged bleeding following procedure"; HP calls it **Prolonged bleeding after dental extraction**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0009883` - called "if available", "MONDO"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.
