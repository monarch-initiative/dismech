---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-09T09:10:13.824856'
end_time: '2026-09-09T09:25:51.877833'
duration_seconds: 938.05
template_file: /tmp/ha20_prompt.md
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
  path: A20_Haploinsufficiency-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: A20_Haploinsufficiency-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** A20 Haploinsufficiency
- **MONDO ID:** MONDO:0100222 (if available)
- **Category:** Autosomal dominant autoinflammatory disease from TNFAIP3 haploinsufficiency with Behcet-like phenotype

## Research Objectives

Please provide a comprehensive research report on **A20 Haploinsufficiency** covering all of the
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

# A20 Haploinsufficiency (HA20): A Comprehensive Disease Characterization

**Disease:** A20 Haploinsufficiency (HA20)
**MONDO ID:** MONDO:0100222 · **OMIM:** #616744 · **Gene:** *TNFAIP3* (HGNC:11896)
**Category:** Autosomal-dominant systemic autoinflammatory disease (inborn error of immunity) with a Behçet-like phenotype

---

## Summary

A20 Haploinsufficiency (HA20) is a rare, early-onset, autosomal-dominant systemic autoinflammatory disease caused by heterozygous germline loss-of-function (LOF) variants in *TNFAIP3*, the gene encoding the ubiquitin-editing enzyme A20. First defined in 2016 in six unrelated families with early-onset systemic inflammation resembling Behçet's disease, HA20 has since evolved into a recognized "complex inborn error of immunity" with a broad spectrum of autoinflammatory and autoimmune phenotypes ([PMID: 26642243](https://pubmed.ncbi.nlm.nih.gov/26642243/); [PMID: 38451381](https://pubmed.ncbi.nlm.nih.gov/38451381/)). The core molecular lesion is a ~50% reduction in functional A20, which impairs removal of Lys63-linked polyubiquitin from key NF-κB regulators (TRAF6, NEMO, RIP1) and de-represses both canonical NF-κB signaling and the NLRP3 inflammasome. This yields excess pro-inflammatory cytokines (TNF, IL-1β, IL-6) and a type I interferon signature that together drive chronic multi-organ inflammation.

Clinically, HA20 is dominated by mucocutaneous involvement (recurrent oral and genital ulcers), recurrent fever, gastrointestinal (IBD-like) inflammation, cytopenias, arthritis/arthralgia, and a wide range of autoimmune features — including a subset (~8%) that meet criteria for systemic lupus erythematosus (monogenic lupus). The disease is female-predominant (M:F ~1:2), has a ubiquitous geographic distribution, and typically begins in early childhood (median onset ~3–5.5 years). It follows a chronic, relapsing, lifelong course, with hierarchical clustering separating patients into autoinflammation-predominant and autoimmune-predominant poles.

HA20 is a biologic-responsive disease. Anti-TNF agents are the most effective single class (efficacy ~60%), with IL-1 blockade (anakinra, canakinumab), IL-6 inhibition (tocilizumab), and JAK inhibitors used for refractory disease; hematopoietic cell transplantation (HCT) can ameliorate autoinflammation and be curative in refractory monogenic-IBD phenotypes. The type I IFN signature serves as a biomarker of disease activity and predicts response to JAK inhibition. This report synthesizes 11 confirmed findings across 41 reviewed papers into a complete disease-knowledge-base entry spanning all 15 requested domains.

---

## Key Findings

### F001 — HA20 is an autosomal-dominant autoinflammatory disease caused by heterozygous LOF *TNFAIP3* variants

The disease was originally described by Zhou et al. (2016) as arising from "high-penetrance heterozygous germline mutations in *TNFAIP3*, which encodes the NF-κB regulatory protein A20, in six unrelated families with early-onset systemic inflammation" ([PMID: 26642243](https://pubmed.ncbi.nlm.nih.gov/26642243/)). The mechanism is haploinsufficiency rather than dominant-negative action: "Mutant, truncated A20 proteins are likely to act through haploinsufficiency because they do not exert a dominant-negative effect in overexpression experiments." A 2024 review reframes the condition beyond its Behçet-like origins: "Originally described as an autosomal dominant form of Behcet's disease, HA20 is now considered a complex inborn error of immunity with a broad spectrum of immunologic and clinical phenotypes" ([PMID: 38451381](https://pubmed.ncbi.nlm.nih.gov/38451381/)). Evidence type: **human clinical / genetic**.

### F002 — Mechanism: loss of A20 ubiquitin-editing activity drives NF-κB and NLRP3 inflammasome hyperactivation

A20 is a ubiquitin-editing enzyme that terminates NF-κB signaling. In patient cells, Zhou et al. showed "defective removal of Lys63-linked ubiquitin from TRAF6, NEMO and RIP1 after stimulation with tumor necrosis factor (TNF)," accompanied by increased IκBα degradation, nuclear translocation of NF-κB p65, and elevated NF-κB-dependent cytokines ([PMID: 26642243](https://pubmed.ncbi.nlm.nih.gov/26642243/)). Steiner et al. (2018) confirmed that HA20 patients "display excessive ubiquitination and increased activity of NF-κB and of NLRP3 inflammasome activation" ([PMID: 29846841](https://pubmed.ncbi.nlm.nih.gov/29846841/)). A parallel necroptosis branch operates through the zinc-finger 7 (ZnF7) ubiquitin-binding domain: "A20 prevents inflammasome-dependent arthritis by inhibiting macrophage necroptosis and that this function depends on its zinc finger 7 (ZnF7)" ([PMID: 31086261](https://pubmed.ncbi.nlm.nih.gov/31086261/)) — notably, this anti-inflammatory function does not require A20's deubiquitinase catalytic activity. Evidence type: **human clinical + model organism + in vitro**.

### F003 — Clinical spectrum: mucocutaneous ulcers dominate, with fever, GI inflammation, cytopenia, arthritis, and autoimmunity

The largest international multicenter cohort (He et al. 2026; n=185, 41 clinics, 7 countries; median age at onset 3.3 yr) reports: "Common clinical features were mucocutaneous involvement (80.5%), recurrent fever (63.3%), gastrointestinal symptoms (58.6%), cytopenia (56.6%), arthritis/arthralgia (46.7%), and recurrent infections (35.5%)" ([PMID: 41692116](https://pubmed.ncbi.nlm.nih.gov/41692116/)). Hierarchical clustering "identified two major clusters, an autoinflammation-predominant phenotype and an autoimmune-predominant phenotype." An independent Italian series (De Nardi et al. 2026; n=17) found "oral aphthosis (88%), recurrent fever (53%), gastrointestinal inflammation (53%), autoimmunity (47%), genital ulcers (47%), neuropsychiatric symptoms (41%)," with early onset (<5 yr) associated with more lifetime neuropsychiatric involvement (p=0.004) ([PMID: 42128528](https://pubmed.ncbi.nlm.nih.gov/42128528/)). Evidence type: **human clinical**.

| Phenotype | He 2026 (n=185) | De Nardi 2026 (n=17) | Berteau 2018 (n=45) | Suggested HPO term |
|---|---|---|---|---|
| Oral/mucocutaneous ulcers | 80.5% | 88% | 87% (oral) | HP:0000155 (Oral ulcer) |
| Genital ulcers | — | 47% | 67% | HP:0100728 (Genital ulcers) |
| Recurrent fever | 63.3% | 53% | 62% | HP:0001954 (Recurrent fever) |
| GI inflammation | 58.6% | 53% | 60% (abdominal) | HP:0002037 (Inflammation of the large intestine) |
| Cytopenia | 56.6% | — | — | HP:0001875 (Neutropenia) / HP:0001873 (Thrombocytopenia) |
| Arthritis/arthralgia | 46.7% | 18% | 42% | HP:0001369 (Arthritis) |
| Skin inflammation | — | 12% | 53% | HP:0000988 (Skin rash) |
| Neuropsychiatric | — | 41% | — | HP:0000708 (Behavioral abnormality) |
| Recurrent infections | 35.5% | — | — | HP:0002719 (Recurrent infections) |

### F004 — Treatment: HA20 is biologic-responsive; anti-TNF most effective, with IL-1/IL-6 blockade, JAK inhibitors, and HCT for refractory disease

A Japanese national survey (Shiraki 2025; 72 patients, 54 analyzed) found "Molecular target drugs (MTDs) were administered in 44.4% of patients, among which anti-tumor necrosis factor (TNF)-α agents showed efficacy in 59.5% of patients" ([PMID: 40574834](https://pubmed.ncbi.nlm.nih.gov/40574834/)). Secondary failure (anti-drug antibodies, infusion reactions) was common, managed by switching agents, adding a JAK inhibitor/immunomodulator, or allogeneic HCT. A 2026 review confirms that HA20 and related monogenic conditions "are now recognized as biologic-responsive diseases" ([PMID: 41620931](https://pubmed.ncbi.nlm.nih.gov/41620931/)). For refractory monogenic IBD phenotypes, "Monogenic IBDs include those that are refractory to traditional treatment and can be cured by allogeneic hematopoietic cell transplantation (HCT)" ([PMID: 37899202](https://pubmed.ncbi.nlm.nih.gov/37899202/)), and HCT has been shown to ameliorate autoinflammation in HA20 ([PMID: 34427832](https://pubmed.ncbi.nlm.nih.gov/34427832/)). Evidence type: **human clinical**.

| Therapy | NCIT suggestion | Role in HA20 | Key evidence |
|---|---|---|---|
| Anti-TNF (infliximab, adalimumab, etanercept) | NCIT:C2861 (TNF Inhibitor) | First-line targeted; ~60% efficacy | [PMID: 40574834](https://pubmed.ncbi.nlm.nih.gov/40574834/) |
| IL-1 blockade (anakinra, canakinumab) | NCIT:C2707 (Interleukin-1 Antagonist) | Autoinflammation/inflammasome-driven disease | [PMID: 41620931](https://pubmed.ncbi.nlm.nih.gov/41620931/) |
| IL-6 inhibition (tocilizumab) | NCIT:C165258 (IL-6 Inhibitor) | Refractory/systemic inflammation | [PMID: 41620931](https://pubmed.ncbi.nlm.nih.gov/41620931/) |
| JAK inhibitors (baricitinib, tofacitinib, ruxolitinib) | NCIT:C142883 (JAK Inhibitor) | IFN-high/refractory disease | [PMID: 31767699](https://pubmed.ncbi.nlm.nih.gov/31767699/) |
| Colchicine | NCIT:C819 (Colchicine) | Inconstant response (~24%) | [PMID: 29890348](https://pubmed.ncbi.nlm.nih.gov/29890348/) |
| Allogeneic HCT | NCIT:C15431 (Allogeneic HSCT) | Curative for refractory disease | [PMID: 34427832](https://pubmed.ncbi.nlm.nih.gov/34427832/); [PMID: 37899202](https://pubmed.ncbi.nlm.nih.gov/37899202/) |

### F005 — Diagnostic biomarkers: elevated type I IFN signature and IFN-γ-inducible chemokines mark disease activity and predict JAK-inhibitor response

De Nardi et al. found higher type 1 IFN signature (IS) levels in patients with active disease (p<0.01) and concluded "type 1 IS may represent a potential biomarker of disease activity in HA20," alongside evaluation of IFN-γ-inducible chemokines CXCL9/CXCL10 ([PMID: 42128528](https://pubmed.ncbi.nlm.nih.gov/42128528/)). Schwartz et al. established that the "Type I interferon signature predicts response to JAK inhibition in haploinsufficiency of A20" ([PMID: 31767699](https://pubmed.ncbi.nlm.nih.gov/31767699/)). Importantly, the signature can be elevated even in quiescent disease: "Half of the patients examined in this study, with undifferentiated inflammatory diseases, clinically quiescent A20 haploinsufficiency, or idiopathic pulmonary hemosiderosis, had an elevated type I IFN signature" ([PMID: 36211342](https://pubmed.ncbi.nlm.nih.gov/36211342/)). Evidence type: **human clinical**.

### F006 — Genetics: germline heterozygous LOF variants (truncating dominant, plus OTU/ZnF missense); phenotype spans autoinflammation to monogenic lupus

The international cohort revealed a "novel genetic architecture and phenotypic evolution" across 185 patients with pathogenic/likely-pathogenic *TNFAIP3* variants ([PMID: 41692116](https://pubmed.ncbi.nlm.nih.gov/41692116/)). Variant classes include truncating (nonsense, frameshift) variants causing haploinsufficiency, plus pathogenic missense variants in the catalytic OTU deubiquitinase domain — e.g., "a heterozygous c.608T>G (p.Leu203Arg) missense variant in *TNFAIP3*, located within the OTU domain" ([PMID: 40719110](https://pubmed.ncbi.nlm.nih.gov/40719110/)) and c.1804A>T p.T602S causing over-activation of canonical NF-κB signaling ([PMID: 34808442](https://pubmed.ncbi.nlm.nih.gov/34808442/)). A systematic review documented the lupus overlap: "Among all the 191 HA20 patients reported in the literature, we identified 16 patients (8.4%) with a compatible diagnosis of SLE," with frequent ANA/anti-dsDNA, renal (56.3%), cutaneous (81.3%), and musculoskeletal (56.3%) involvement ([PMID: 39672252](https://pubmed.ncbi.nlm.nih.gov/39672252/)). Evidence type: **human clinical / genetic + in vitro**.

### F007 — Organ involvement and gut dysbiosis: IBD-like GI inflammation, chronic liver disease, and altered gut microbiota

Elhani et al. (2026; 16 HA20 patients vs 22 controls) documented multi-organ pathology and microbiome changes: "The fecal microbiota of HA20 patients was characterized by marked alterations, including a reduction in microbial diversity and an increase in the pro-inflammatory bacterium *Ruminococcus gnavus*" ([PMID: 41991504](https://pubmed.ncbi.nlm.nih.gov/41991504/)). The same study found that "Liver imaging revealed chronic liver disease in 3/5 patients, showing as liver dysmorphia and portal hypertension," with histology showing lymphoplasmocytic infiltrate of the GI tract and liver, impaired microbial bile-acid deconjugation/desulfation, and a shift of tryptophan metabolism toward the kynurenine pathway. Evidence type: **human clinical + microbiome/metabolomic**.

### F008 — Model organisms: A20/*Tnfaip3* mouse models recapitulate HA20

Cell-specific and domain-mutant mouse models reproduce major HA20 features. Myeloid-specific deletion produces arthritis: "Myeloid-cell-specific deletion of the rheumatoid arthritis susceptibility gene A20/Tnfaip3 in mice (A20(myel-KO) mice) triggers a spontaneous erosive polyarthritis that resembles rheumatoid arthritis in patients," and this "crucially relies on the Nlrp3 inflammasome and interleukin-1 receptor signalling" ([PMID: 25043000](https://pubmed.ncbi.nlm.nih.gov/25043000/)). Intestinal models reproduce the IBD phenotype: "Combining IEC and myeloid A20 deletion induces ileitis and severe colitis" ([PMID: 25267258](https://pubmed.ncbi.nlm.nih.gov/25267258/)). The ZnF7 ubiquitin-binding mutation alone causes arthritis ([PMID: 31086261](https://pubmed.ncbi.nlm.nih.gov/31086261/)); additional cell-specific effects appear in airway club cells ([PMID: 26815999](https://pubmed.ncbi.nlm.nih.gov/26815999/)), pancreatic β-cells, and enthesitis via STAT1 ([PMID: 27551052](https://pubmed.ncbi.nlm.nih.gov/27551052/)). Evidence type: **model organism**.

### F009 — Epidemiology & temporal course: rare, ubiquitous, female-predominant, early-childhood onset, chronic relapsing course

Berteau et al. (2018; systematic review of 45 cases) established key epidemiology: "sex ratio is inversed (one man for two women), first symptoms occur in early childhood (median age = 5.5 years; interquartile range: 1-10) instead of adulthood" ([PMID: 29890348](https://pubmed.ncbi.nlm.nih.gov/29890348/)). HA20 "differs from classical BD because its geographical distribution is ubiquitous," and "response to colchicine in HA20 is inconstant (24%) unlike classical BD." The international cohort reports an even earlier median onset (3.3 yr) ([PMID: 41692116](https://pubmed.ncbi.nlm.nih.gov/41692116/)). Evidence type: **human clinical / epidemiological**.

### F010 — Prognosis & complications: chronic lifelong disease with autoimmune, vascular, and lymphoproliferative complications

HA20 predisposes to lymphoproliferation: "A20 haploinsufficiency disturbs immune homeostasis and drives the transformation of lymphocytes with permissive antigen receptors" ([PMID: 39167656](https://pubmed.ncbi.nlm.nih.gov/39167656/)). Vasculitis is a recognized complication in which "type I interferon-enhanced autoimmune mechanisms and/or dysregulated adaptive immune responses have an important role in the development of immune-mediated endothelial dysfunction and vascular damage" ([PMID: 40369133](https://pubmed.ncbi.nlm.nih.gov/40369133/)). Systemic autoimmunity complications include autoimmune cytopenias, thyroiditis, and lupus/glomerulonephritis (renal 56.3% in the SLE subset; [PMID: 39672252](https://pubmed.ncbi.nlm.nih.gov/39672252/)). No formal survival/mortality statistics are established; most patients survive with chronic morbidity, though severe refractory disease, macrophage activation syndrome/HLH, and HCT-related risks contribute to mortality in a minority. Evidence type: **human clinical**.

### F011 — HA20 is distinct from classic Behçet disease and from somatic *TNFAIP3*-driven lymphoma

HA20 differs from classical Behçet disease on multiple axes: "HA20 differs from classical BD because its geographical distribution is ubiquitous, sex ratio is inversed (one man for two women), first symptoms occur in early childhood" ([PMID: 29890348](https://pubmed.ncbi.nlm.nih.gov/29890348/)); HLA-B51 is uncommon and colchicine response inconstant. Germline vs somatic *TNFAIP3* lesions produce distinct diseases: "A20 germline variants are associated with a wide range of inflammatory diseases, while somatic mutations promote development of B cell lymphomas" ([PMID: 38451381](https://pubmed.ncbi.nlm.nih.gov/38451381/)). Evidence type: **human clinical / genetic**.

---

## Section-by-Section Disease Characterization

### 1. Disease Information

HA20 is a monogenic, autosomal-dominant systemic autoinflammatory disease (an inborn error of immunity) caused by haploinsufficiency of the ubiquitin-editing enzyme A20. It presents with early-onset, recurrent, Behçet-like inflammation and a broad autoinflammatory–autoimmune phenotypic spectrum.

- **Identifiers:** MONDO:0100222; OMIM #616744 ("Autoinflammatory syndrome, familial, Behçet-like 1", AISBL1); Gene *TNFAIP3* (OMIM *191163; HGNC:11896). Orphanet lists it under autoinflammatory syndromes. MeSH is best approximated by "Hereditary Autoinflammatory Diseases" (D056660). ICD-11 maps under immune dysregulation/autoinflammatory disorders (4A60 group).
- **Synonyms:** Haploinsufficiency of A20; A20 haploinsufficiency; TNFAIP3 haploinsufficiency; Familial Behçet-like autoinflammatory syndrome 1 (AISBL1); autosomal-dominant familial Behçet disease.
- **Data source:** Disease-level aggregated resources (OMIM, Orphanet) plus published patient cohorts and case series — not single-EHR-derived.

### 2. Etiology

- **Causal factor:** Heterozygous germline LOF variants in *TNFAIP3* (genetic; high penetrance) — F001, F006.
- **Genetic risk factors:** The pathogenic variant itself is causal and dominant. Modifier genes and co-occurring autoinflammatory VUS may shape phenotype (mixed autoinflammatory disorders; [PMID: 41191928](https://pubmed.ncbi.nlm.nih.gov/41191928/)).
- **Environmental risk factors:** Not clearly established as disease-*causing*; however, infection/inflammatory triggers (TNF, LPS, IL-1β) provoke flares by engaging the very pathways A20 fails to restrain (F002). Gut dysbiosis (increased *R. gnavus*) is associated with the intestinal phenotype (F007) and may act as a gene–environment interface. Female sex is associated with higher prevalence (F009).
- **Protective factors:** No validated genetic or environmental protective alleles reported for HA20 specifically. (Data not available.)
- **Gene–environment interaction:** Loss of A20 lowers the threshold for NF-κB/inflammasome activation by microbial and cytokine stimuli, so environmental triggers (microbiota, infection) interact with the genetic lesion to precipitate flares (inferred from F002, F007, F008).

### 3. Phenotypes

See the frequency table under F003. Phenotype **types** span clinical signs (mucocutaneous ulcers, arthritis), symptoms (fever, abdominal pain), laboratory abnormalities (cytopenias, autoantibodies, elevated inflammatory markers/IFN signature), and behavioral/neuropsychiatric changes. **Onset** is typically pediatric (median 3.3–5.5 yr). **Severity** is variable, ranging from mild recurrent aphthosis to severe multi-organ disease and monogenic lupus. **Progression** is chronic-relapsing/episodic with lifelong activity. **Quality-of-life impact** is substantial through recurrent painful ulcers, chronic GI disease, arthritis, and treatment burden, though formal EQ-5D/SF-36 data specific to HA20 are not available.

### 4. Genetic / Molecular Information

- **Causal gene:** *TNFAIP3* (chromosome 6q23.3), encoding A20 (F001).
- **Variant classes:** Truncating nonsense and frameshift variants (dominant, produce haploinsufficiency; F001) plus pathogenic missense variants in the catalytic OTU deubiquitinase domain (e.g., p.Leu203Arg; p.T602S) and zinc-finger domains (F006).
- **Classification:** Pathogenic/likely-pathogenic per ACMG/AMP; truncating LOF in a haploinsufficient gene supports PVS1-level evidence. Rare missense variants require functional confirmation (NF-κB over-activation assays; F006).
- **Allele frequency:** Pathogenic variants are private/ultra-rare and essentially absent from population databases (gnomAD), consistent with high-penetrance disease.
- **Origin:** Germline (contrast with somatic *TNFAIP3* mutations in B-cell lymphoma; F011).
- **Functional consequence:** Loss of function / haploinsufficiency (no dominant-negative effect; F001).
- **Epigenetics / chromosomal abnormalities:** No recurrent epigenetic signature or large-scale chromosomal abnormality is specific to HA20 (not applicable / data not available).

### 5. Environmental Information

No specific toxin, radiation, occupational, or infectious agent has been established as a primary cause. The gut microbiome is altered (reduced diversity, increased pro-inflammatory *Ruminococcus gnavus*, impaired bile-acid metabolism; F007), likely acting as a downstream/modifying environmental factor rather than a primary cause. Microbial and cytokine stimuli (LPS, TNF, IL-1β) trigger flares in vitro and in vivo (F002, F008).

### 6. Mechanism / Pathophysiology

**Ordered causal chain (initiating lesion → clinical manifestation):**

1. A heterozygous germline LOF variant in *TNFAIP3* **leads to** ~50% reduction in functional A20 protein (haploinsufficiency) — *demonstrated* (F001).
2. Reduced A20 **results in** impaired removal of Lys63-linked polyubiquitin from TRAF6, NEMO, and RIP1 after TNF/TLR stimulation, and impaired ZnF7-dependent ubiquitin binding — *demonstrated* (F002).
3. Excess K63-ubiquitination **leads to** increased IκBα degradation and nuclear translocation of NF-κB p65 — *demonstrated* (F002).
4. NF-κB hyperactivation **results in** transcription of pro-inflammatory cytokines (TNF, IL-6, IL-1β precursors) — *demonstrated* (F002).
   - **Branch A (inflammasome):** Loss of A20 restraint **leads to** NLRP3 inflammasome hyperactivation and mature IL-1β release — *demonstrated in patient cells and mouse models* (F002, F008).
   - **Branch B (necroptosis):** Loss of ZnF7 function **leads to** RIPK1/RIPK3-MLKL-dependent macrophage necroptosis and inflammasome-dependent arthritis — *demonstrated in mice* (F002, F008).
   - **Branch C (interferon):** Downstream signaling **results in** an elevated type I IFN signature and IFN-γ-inducible chemokines (CXCL9/CXCL10) — *demonstrated as a biomarker* (F005).
5. Sustained cytokine excess (TNF/IL-1β/IL-6/type I IFN) **leads to** chronic multi-organ inflammation: mucocutaneous ulcers, IBD-like gut inflammation, arthritis, cytopenias, vasculitis, and autoimmunity — *demonstrated clinically* (F003, F007, F010).
6. Immune dysregulation additionally **leads to** transformation of lymphocytes with permissive antigen receptors, contributing to autoimmunity and lymphoproliferation risk — *demonstrated/inferred* (F010).

**Pathways & processes:** NF-κB signaling (KEGG hsa04064; Reactome R-HSA-975138), NLRP3 inflammasome (GO:0072559), TNF signaling, type I IFN signaling, necroptosis (GO:0070266). **Cellular processes:** inflammation (GO:0006954), positive regulation of NF-κB (GO:0051092), inflammasome-mediated signaling, apoptosis/necroptosis, autophagy (A20–DEPTOR complex restrains inflammasome via autophagy; [PMID: 29940800](https://pubmed.ncbi.nlm.nih.gov/29940800/)). **Cell types (CL):** macrophage (CL:0000235), monocyte (CL:0000576), intestinal epithelial cell (CL:0002563), neutrophil (CL:0000775), T cell (CL:0000084), B cell (CL:0000236). **Suggested GO biological process:** GO:0043123 (positive regulation of canonical NF-κB signal transduction); GO:0032611 (IL-1β production).

### 7. Anatomical Structures Affected

- **Primary organs/systems:** skin and mucosa (oral, genital), gastrointestinal tract, joints, hematologic/immune system.
- **Secondary involvement:** liver (chronic liver disease, portal hypertension — F007), blood vessels (vasculitis of all sizes — F010), kidney (glomerulonephritis in lupus subset — F006), CNS (neuropsychiatric — F003), eyes (uveitis), thyroid (autoimmune thyroiditis).
- **UBERON terms:** oral mucosa (UBERON:0002424), skin (UBERON:0002097), large intestine (UBERON:0000059), small intestine/ileum (UBERON:0002116), liver (UBERON:0002107), synovial joint (UBERON:0002217), blood vessel (UBERON:0001981).
- **Tissue/cell level:** epithelial (intestinal, mucosal), immune (myeloid, lymphoid), endothelial. **CL terms** as above.
- **Subcellular (GO CC):** cytoplasm/cytosol (GO:0005829, site of A20 ubiquitin editing and NF-κB regulation), inflammasome complex (GO:0061702).
- **Lateralization:** Bilateral/systemic; ulcers and arthritis are typically multifocal rather than lateralized.

### 8. Temporal Development

- **Onset:** Congenital predisposition, clinical onset usually early childhood (median 3.3–5.5 yr; F009); onset pattern chronic/insidious with recurrent acute flares.
- **Progression:** Chronic, relapsing-remitting/episodic course; lifelong. Rate variable. Early onset (<5 yr) associated with more lifetime neuropsychiatric involvement (F003).
- **Patterns:** Treatment-induced remission achievable with biologics; spontaneous remissions uncommon. Early childhood is a critical window given cumulative organ damage.

### 9. Inheritance and Population

- **Epidemiology:** Rare (ultra-rare); precise prevalence/incidence not established. Ubiquitous geographic distribution (F009, F011).
- **Inheritance:** Autosomal dominant, high penetrance (F001), with variable expressivity even within families. De novo variants occur. Founder effects/consanguinity not central (dominant disease).
- **Penetrance:** High but with intra-familial variable expressivity.
- **Sex ratio:** Female-predominant, M:F ~1:2 (F009).
- **Carrier frequency:** Not applicable (dominant, ultra-rare pathogenic alleles; largely absent from gnomAD).

### 10. Diagnostics

- **Genetic testing (definitive):** Molecular confirmation of a pathogenic/likely-pathogenic *TNFAIP3* variant via single-gene testing, autoinflammatory/immune-dysregulation gene panels, or whole-exome/whole-genome sequencing (F001, F006). Functional confirmation (NF-κB over-activation, ubiquitination assays) supports novel missense variants.
- **Laboratory/biomarkers:** Elevated acute-phase reactants during flares; cytopenias; autoantibodies (ANA, anti-dsDNA in lupus-overlap); **type I IFN signature** and IFN-γ-inducible chemokines (CXCL9/CXCL10) as activity and therapy-selection biomarkers (F005).
- **Imaging/endoscopy:** GI endoscopy shows ileocolonic ulcers (IBD-like); liver imaging may show dysmorphia/portal hypertension (F007).
- **Histopathology:** Lymphoplasmocytic infiltrate of GI tract and liver (F007).
- **Clinical criteria & differential diagnosis:** Distinguish from classic Behçet disease (ubiquitous distribution, early onset, inverted sex ratio, uncommon HLA-B51, inconstant colchicine response; F011) and from DADA2, monogenic IBD (IL-10/IL-10R, XIAP), FMF/periodic fevers, SAVI, VEXAS, monogenic lupus/ALPS (F011). Overlapping/mixed autoinflammatory presentations occur ([PMID: 41191928](https://pubmed.ncbi.nlm.nih.gov/41191928/); [PMID: 39360366](https://pubmed.ncbi.nlm.nih.gov/39360366/)).
- **Screening:** Cascade genetic testing of at-risk relatives after a proband variant is identified.

### 11. Outcome / Prognosis

Chronic, lifelong disease with substantial morbidity but generally survivable with modern biologic therapy. **Complications:** autoimmune cytopenias, IBD/chronic liver disease, vasculitis (F010), MAS/HLH, monogenic lupus with glomerulonephritis (F006), and predisposition to lymphocyte transformation/lymphoproliferation (F010). No formal survival/mortality statistics exist. **Prognostic factors:** age of onset (earlier → more neuropsychiatric involvement), disease cluster (autoinflammatory vs autoimmune), and type I IFN signature (activity/therapy response). **Prognostic biomarker:** type I IFN signature (F005).

### 12. Treatment

See the treatment table under F004. Strategy: control autoinflammation with targeted biologics, escalate for refractory disease, and reserve HCT for refractory monogenic-IBD/severe phenotypes. **Personalized medicine:** IFN-high patients preferentially respond to JAK inhibition (F005); anti-TNF is the most broadly effective class (F004). Colchicine is inconstantly effective (~24%; F009). Anti-drug antibody-mediated secondary failure is a common practical challenge (F004).

### 13. Prevention

No primary prevention exists for this monogenic disease. Prevention is centered on: **genetic counseling** for affected families (AD inheritance, 50% transmission risk, variable expressivity); **prenatal/preimplantation genetic testing** where a familial variant is known; **cascade screening** of relatives; and **tertiary prevention** (early biologic therapy to prevent cumulative organ damage, vigilance for autoimmune, vascular, and lymphoproliferative complications). Novel-variant identification has been proposed to enable prenatal diagnosis and reduce disease burden in newborns ([PMID: 34808442](https://pubmed.ncbi.nlm.nih.gov/34808442/)).

### 14. Other Species / Natural Disease

- **Taxonomy/orthologs:** Human *TNFAIP3* (NCBI Gene 7128); mouse *Tnfaip3* (NCBI Gene 21929). The gene and its NF-κB-regulatory function are evolutionarily conserved.
- **Natural disease:** No well-characterized spontaneous HA20 equivalent in companion animals is documented (data not available). Disease is primarily modeled experimentally (Section 15).
- **Comparative biology:** Cell-specific mouse deletions recapitulate distinct human phenotypes, demonstrating conserved mechanisms (F008).

### 15. Model Organisms

- **Type:** Mammalian (mouse, *Mus musculus*), plus in vitro cell systems (THP-1 monocytes, patient PBMCs, iPSC-derived cells).
- **Genetic models:** Germline *Tnfaip3* knockout is perinatal-lethal with multi-organ inflammation; conditional/cell-specific knockouts (myeloid, intestinal epithelial, airway club cell, β-cell) and domain-specific knock-ins (ZnF7 mutant) are used (F008).
- **Phenotype recapitulation:** Myeloid-specific KO → NLRP3/IL-1-dependent erosive polyarthritis (F008); IEC+myeloid KO → ileitis/severe colitis with dysbiosis (F008); ZnF7 mutant → arthritis (F008); myeloid KO → STAT1-dependent enthesitis ([PMID: 27551052](https://pubmed.ncbi.nlm.nih.gov/27551052/)).
- **Limitations:** Human HA20 is heterozygous haploinsufficiency, whereas most informative mouse models use complete cell-specific deletion; no single model captures the full multi-organ human spectrum.
- **Resources:** MGI (*Tnfaip3*), IMPC, IMSR.

---

## Mechanistic Model / Interpretation

```
 Germline heterozygous TNFAIP3 LOF variant
                │  (haploinsufficiency, ~50% A20)   [F001]
                ▼
 Impaired removal of K63-Ub from TRAF6/NEMO/RIP1
 + impaired ZnF7 ubiquitin binding                [F002]
                │
      ┌─────────┼───────────────────────────┐
      ▼         ▼                           ▼
 NF-κB p65   NLRP3 inflammasome      RIPK1/RIPK3-MLKL
 activation   hyperactivation         necroptosis (ZnF7)
   [F002]      → IL-1β  [F002/F008]     → arthritis [F008]
      │            │                         │
      └──────┬─────┴─────────────┬───────────┘
             ▼                    ▼
   TNF/IL-6/IL-1β excess    Type I IFN signature
                             + CXCL9/CXCL10   [F005]
             │                    │
             └────────┬───────────┘
                      ▼
   Chronic multi-organ inflammation & autoimmunity   [F003/F007/F010]
   (oral/genital ulcers, IBD, arthritis, cytopenia,
    vasculitis, monogenic lupus, lymphoproliferation)
                      │
                      ▼
  Therapeutic reversal by anti-TNF / IL-1 / IL-6 / JAK-i / HCT  [F004]
```

The unifying interpretation is that HA20 is a "de-repression" disease: A20 is a critical negative feedback brake on innate immune signaling, and losing half of it lowers the activation threshold across multiple downstream nodes (NF-κB, inflammasome, necroptosis, type I IFN). Because the lesion sits at a hub with several effector branches, the clinical phenotype is heterogeneous — patients partition into autoinflammation-predominant vs autoimmune-predominant clusters (F003) depending on which branch dominates. This directly rationalizes the therapeutic landscape: cytokine-directed biologics neutralize individual effector arms, anti-TNF works broadly because TNF sits both upstream and downstream of A20-regulated signaling, and JAK inhibition is best matched to IFN-high patients (F004, F005).

---

## Evidence Base

| PMID | Title (abbrev.) | Supports |
|---|---|---|
| [26642243](https://pubmed.ncbi.nlm.nih.gov/26642243/) | LOF *TNFAIP3* → early-onset autoinflammation (Zhou 2016) | F001, F002 (causal gene, haploinsufficiency, K63-Ub defect) |
| [38451381](https://pubmed.ncbi.nlm.nih.gov/38451381/) | Complexity of being A20 (Karri 2024 review) | F001, F011 (IEI concept; germline vs somatic) |
| [29846841](https://pubmed.ncbi.nlm.nih.gov/29846841/) | Relopathies update (Steiner 2018) | F002 (NF-κB + NLRP3 hyperactivation) |
| [31086261](https://pubmed.ncbi.nlm.nih.gov/31086261/) | A20 ZnF7 prevents necroptosis/arthritis (Polykratis 2019) | F002, F008 (necroptosis branch) |
| [41692116](https://pubmed.ncbi.nlm.nih.gov/41692116/) | International cohort n=185 (He 2026) | F003, F006 (frequencies, clusters, genetic architecture) |
| [42128528](https://pubmed.ncbi.nlm.nih.gov/42128528/) | Italian case series (De Nardi 2026) | F003, F005 (frequencies; IFN biomarker) |
| [40574834](https://pubmed.ncbi.nlm.nih.gov/40574834/) | Japan national survey (Shiraki 2025) | F004 (anti-TNF efficacy 59.5%) |
| [41620931](https://pubmed.ncbi.nlm.nih.gov/41620931/) | Biologics in autoinflammatory disorders (Koga 2026) | F004 (biologic-responsive) |
| [37899202](https://pubmed.ncbi.nlm.nih.gov/37899202/) | HCT for monogenic IBD (Kanegane 2023) | F004 (HCT curative for refractory) |
| [34427832](https://pubmed.ncbi.nlm.nih.gov/34427832/) | HCT ameliorates HA20 autoinflammation (Shiraki 2021) | F004 |
| [31767699](https://pubmed.ncbi.nlm.nih.gov/31767699/) | IFN signature predicts JAK-i response (Schwartz 2020) | F004, F005 |
| [36211342](https://pubmed.ncbi.nlm.nih.gov/36211342/) | Type I IFN signatures (Miyamoto 2022) | F005 (IFN elevated even in quiescent HA20) |
| [40719110](https://pubmed.ncbi.nlm.nih.gov/40719110/) | Novel OTU-domain missense (Potjewijd 2025) | F006 (p.Leu203Arg, STAT1/mTOR) |
| [34808442](https://pubmed.ncbi.nlm.nih.gov/34808442/) | Novel missense p.T602S (Jiang 2022) | F006 (NF-κB over-activation; prenatal implication) |
| [39672252](https://pubmed.ncbi.nlm.nih.gov/39672252/) | HA20 beyond SLE systematic review (Philip 2025) | F006 (8.4% meet SLE criteria) |
| [41991504](https://pubmed.ncbi.nlm.nih.gov/41991504/) | Gut microbiota & intestinal phenotype (Elhani 2026) | F007 (dysbiosis, liver disease) |
| [25043000](https://pubmed.ncbi.nlm.nih.gov/25043000/) | A20/NLRP3 & arthritis mouse (Vande Walle 2014) | F008 (myeloid-KO arthritis) |
| [25267258](https://pubmed.ncbi.nlm.nih.gov/25267258/) | A20 intestinal homeostasis (Vereecke 2014) | F008 (ileitis/colitis model) |
| [27551052](https://pubmed.ncbi.nlm.nih.gov/27551052/) | A20/STAT1 enthesitis (De Wilde 2017) | F008 (enthesitis branch) |
| [26815999](https://pubmed.ncbi.nlm.nih.gov/26815999/) | A20 in lung club cells (Maelfait 2016) | F008 (airway-epithelial model) |
| [29890348](https://pubmed.ncbi.nlm.nih.gov/29890348/) | HA20 vs Behçet review (Berteau 2018) | F009, F011 (epidemiology; distinction) |
| [39167656](https://pubmed.ncbi.nlm.nih.gov/39167656/) | A20 & lymphocyte transformation (Schultheiss 2024) | F010 (lymphoproliferation risk) |
| [40369133](https://pubmed.ncbi.nlm.nih.gov/40369133/) | Monogenic vasculitis (Gül 2025) | F010 (vasculitis, endothelial damage) |
| [29940800](https://pubmed.ncbi.nlm.nih.gov/29940800/) | TNFAIP3–DEPTOR autophagy (AS monocytes) | Mechanism (autophagy restraint of inflammasome) |
| [41191928](https://pubmed.ncbi.nlm.nih.gov/41191928/) | Mixed autoinflammatory disorders | Differential/overlap diagnosis |

---

## Limitations and Knowledge Gaps

- **No formal survival/mortality or population-level prevalence/incidence statistics** exist for HA20; epidemiology derives from case series and systematic reviews, subject to ascertainment bias toward severe cases.
- **Genotype–phenotype correlation is incomplete.** The two-cluster (autoinflammation vs autoimmune) framework is data-driven but the molecular determinants of cluster membership remain undefined.
- **Model-organism caveat:** Most mechanistic mouse data use complete cell-specific deletion, not the heterozygous haploinsufficiency seen in patients; no single model captures the full human spectrum.
- **Microbiome/metabolomic findings** (F007) are from a single small study (n=16) and require replication before causal claims about dysbiosis can be made.
- **Type I IFN biomarker** utility is promising but not yet standardized or prospectively validated as a treatment-selection tool at scale.
- **Quality-of-life data** specific to HA20 (EQ-5D/SF-36/PROMIS) are absent.
- **Prognostic modeling** for lymphoproliferation/malignancy risk is qualitative; absolute risks are unknown.

---

## Proposed Follow-up Experiments / Actions

1. **Prospective natural-history registry** with standardized organ-damage indices and QoL instruments to establish prevalence, mortality, and long-term outcomes.
2. **Genotype–phenotype and multi-omics integration** (single-cell transcriptomics of monocytes/T/B/NK cells) to define molecular determinants of the autoinflammatory vs autoimmune clusters and to nominate cluster-specific therapies.
3. **Prospective validation of the type I IFN signature** as a treatment-stratification biomarker (IFN-high → JAK inhibitor) in a controlled trial.
4. **Microbiome replication and interventional studies** (larger cohorts; assessment of whether modulating *R. gnavus*/bile-acid metabolism alters GI disease).
5. **Heterozygous, patient-variant knock-in mouse and iPSC models** that faithfully replicate haploinsufficiency (rather than full deletion) for mechanism and drug testing.
6. **Systematic surveillance protocol** for lymphoproliferation/malignancy and standardized long-term follow-up of HCT-treated patients.
7. **Functional-assay framework** for classifying novel *TNFAIP3* missense VUS (NF-κB reporter, ubiquitination, STAT1/mTOR readouts) to support ACMG classification and cascade counseling.

---

*Report compiled from 11 confirmed findings across 41 reviewed papers. Evidence types are annotated per finding (human clinical, model organism, in vitro, computational). All quoted text is drawn verbatim from the cited abstracts.*


## Artifacts

- [OpenScientist final report](A20_Haploinsufficiency-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](A20_Haploinsufficiency-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:26642243
2. PMID:38451381
3. PMID:29846841
4. PMID:31086261
5. PMID:41692116
6. PMID:42128528
7. PMID:40574834
8. PMID:41620931
9. PMID:37899202
10. PMID:34427832
11. PMID:31767699
12. PMID:29890348
13. PMID:36211342
14. PMID:40719110
15. PMID:34808442
16. PMID:39672252
17. PMID:41991504
18. PMID:25043000
19. PMID:25267258
20. PMID:26815999
21. PMID:27551052
22. PMID:39167656
23. PMID:40369133
24. PMID:41191928
25. PMID:29940800
26. PMID:39360366