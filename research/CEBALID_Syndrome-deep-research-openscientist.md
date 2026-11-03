---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-30T17:54:47.615753'
end_time: '2026-10-30T18:33:59.175419'
duration_seconds: 2351.56
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: CEBALID Syndrome
  mondo_id: MONDO:0032908
  category: Mendelian
  causal_genes: MN1
  omim_id: OMIM:618774
  synonyms: MCTT; MN1 C-Terminal Truncation Syndrome
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
citation_count: 7
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: CEBALID_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: CEBALID_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** CEBALID Syndrome
- **MONDO ID:** MONDO:0032908 (if available)
- **Causal gene(s):** MN1
- **OMIM:** OMIM:618774
- **Synonyms:** MCTT; MN1 C-Terminal Truncation Syndrome
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **CEBALID Syndrome** covering all of the
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

# CEBALID Syndrome (MN1 C-Terminal Truncation Syndrome): A Comprehensive Disease Characterization

**Disease:** CEBALID Syndrome | **Synonyms:** MN1 C-Terminal Truncation (MCTT) Syndrome; MCTT
**Causal gene:** *MN1* (Meningioma-1 / meningioma translocation 1), 22q12.1 | **MONDO:** MONDO:0032908 | **OMIM:** #618774
**Inheritance:** Autosomal dominant (de novo) | **Category:** Mendelian, rare neurodevelopmental/craniofacial malformation syndrome

---

## Summary

**CEBALID syndrome is an ultra-rare, congenital, autosomal-dominant neurodevelopmental and craniofacial malformation disorder caused by de novo C-terminal truncating variants in *MN1* (Meningioma-1), a two-exon transcriptional co-regulator gene on chromosome 22q12.1.** The acronym CEBALID captures the core clinical domains: **C**raniofacial defects, dysmorphic **E**ars, **B**rain **A**bnormalities, **L**anguage delay, and **I**ntellectual **D**isability. The disorder was first delineated in 2020 through two landmark reports and has fewer than ~30 published cases worldwide as of 2025, so reliable population-level epidemiology is unavailable.

The defining molecular lesion is a truncating (nonsense or frameshift) *MN1* variant located in the terminal exon or the extreme 3′ end of exon 1. Because of this position, the mutant transcript **escapes nonsense-mediated mRNA decay (NMD)** and produces a stabilized, aggregation-prone, C-terminally truncated protein. Functional studies demonstrate this acts through a **gain-of-function / dominant change-of-function mechanism** rather than haploinsufficiency—a critical distinction, because whole-gene *MN1* deletions produce a milder, different phenotype. A recurrent hotspot variant, **p.Arg1295\***, accounts for roughly one-third of reported probands.

The recognizable clinical gestalt is **midface hypoplasia** combined with **severe expressive language delay and intellectual disability**, dysmorphic/low-set ears, and a distinctive brain malformation—**partial (atypical) rhombencephalosynapsis**—frequently accompanied by perisylvian polymicrogyria, corpus callosum anomalies, and craniofacial skeletal abnormalities. Mechanistically, MN1 functions as a **retinoic-acid-receptor (RAR/RXR) transcriptional coactivator** (working with p160/p300 coactivators) and acts **upstream of *Tbx22*** in posterior palate development; mouse *Mn1* knockouts die of cleft palate with agenesis of membranous cranial bones, linking MN1 dysfunction directly to the craniofacial phenotype. There is currently no disease-specific or curative therapy; diagnosis is by whole-exome/whole-genome sequencing plus characteristic brain MRI, and management is supportive and multidisciplinary.

---

## 1. Disease Information

CEBALID syndrome (also termed **MN1 C-terminal truncation [MCTT] syndrome**) is a Mendelian, congenital neurodevelopmental and craniofacial malformation disorder. It was independently described in 2020 by Mak et al. (*Brain*) and Miyake et al. (*American Journal of Human Genetics*), who both identified clusters of individuals with de novo C-terminal truncating *MN1* variants sharing a remarkably consistent phenotype.

**Key identifiers:**

| Resource | Identifier |
|----------|-----------|
| MONDO | MONDO:0032908 |
| OMIM | #618774 |
| Gene | *MN1* (HGNC:7180), chromosome 22q12.1 |
| Synonyms | MN1 C-terminal truncation syndrome; MCTT; CEBALID syndrome |

As Dirani et al. (2025) state, *"CEBALID syndrome (Craniofacial defects, dysmorphic Ears, Brain Abnormalities, Language delay, and Intellectual Disability) is caused by C-terminal truncated transcriptional activator MN1"* and *"This novel syndrome ... was recently identified in 2020. Since then, less than 30 cases have been reported worldwide"* ([PMID: 40713540](https://pubmed.ncbi.nlm.nih.gov/40713540/)).

**Information source:** The knowledge base is derived from aggregated, disease-level resources—primarily small case series and individual case reports (Mak n=23; Miyake n=3; Dirani n=1) combined with mechanistic model-organism and in vitro studies. There is no EHR/registry-scale dataset.

---

## 2. Etiology

**Disease causal factor — genetic (de novo, dominant).** CEBALID is a monogenic disorder caused by heterozygous **truncating variants in *MN1***. Mak et al. identified *"a cluster of de novo truncating mutations in MN1 in a cohort of 23 individuals"* ([PMID: 31834374](https://pubmed.ncbi.nlm.nih.gov/31834374/)), and Miyake et al. described *"three individuals who have de novo MN1 variants that lead to a protein lacking the carboxyl (C) terminus"* ([PMID: 31839203](https://pubmed.ncbi.nlm.nih.gov/31839203/)). The variants arise **de novo**, so affected individuals typically have unaffected parents.

**Genetic risk factors.** The sole established genetic risk factor is the presence of a de novo C-terminal truncating *MN1* variant. The recurrent **p.Arg1295\*** variant represents a CpG-associated mutational hotspot rather than a founder allele. No susceptibility loci or modifier genes have been identified.

**Environmental risk factors / protective factors / gene–environment interactions.** None are established. As a de novo dominant malformation syndrome, there are **no known environmental risk factors, protective factors, lifestyle contributors, or gene–environment interactions**. Advanced paternal age is a general (not disease-specific) consideration for de novo variants but has not been formally studied here.

---

## 3. Phenotypes

The phenotype is **congenital/neonatal in onset**, **variable in severity but generally severe**, and **non-progressive (malformative/static)** with lifelong disability. Frequencies below derive chiefly from the Mak cohort (n=23) and the Miyake series (n=3).

### Neurodevelopmental phenotypes
- **Intellectual disability** (HP:0001249) — core, high frequency
- **Severe expressive/speech language delay** (HP:0002474, HP:0000750) — hallmark, nearly universal
- **Global developmental delay** (HP:0001263)
- **Hypotonia** (HP:0001252)

Mak et al.: *"strikingly similar dysmorphic facial features, especially midface hypoplasia, and intellectual disability with severe expressive language delay"* ([PMID: 31834374](https://pubmed.ncbi.nlm.nih.gov/31834374/)).

### Brain malformation phenotypes
- **Partial/atypical rhombencephalosynapsis** (cerebellar vermis hypoplasia/aplasia with hemispheric fusion) — **8/10 imaged individuals** in Mak et al.
- **Perisylvian polymicrogyria** (HP:0032420 / HP:0002126)
- **Corpus callosum anomalies** including agenesis of the genu (HP:0001273)
- **Ventriculomegaly** (HP:0002119)
- **Abnormal posterior clinoid processes; persistent trigeminal artery**

Mak et al. identified *"an atypical form of rhombencephalosynapsis, a distinctive brain malformation characterized by partial or complete loss of the cerebellar vermis with fusion of the cerebellar hemispheres, in 8/10 individuals"* ([PMID: 31834374](https://pubmed.ncbi.nlm.nih.gov/31834374/)). Dirani et al. documented a neonate whose MRI *"revealed polymicrogyri, agenesis of the genu of the corpus callosum and rhombencephalosynapsis"* ([PMID: 40713540](https://pubmed.ncbi.nlm.nih.gov/40713540/)).

### Craniofacial phenotypes
- **Midface hypoplasia** (HP:0011800) — hallmark gestalt feature
- **Hypertelorism** (HP:0000316); **downslanting palpebral fissures** (HP:0000494)
- **Proptosis / shallow orbits** (HP:0000520)
- **Depressed/broad nasal bridge** (HP:0005280)
- **Small, dysmorphic, low-set ears** (HP:0000369, HP:0000368)
- **High-arched or cleft palate** (HP:0000218 / HP:0000175)
- **Craniosynostosis and abnormal skull shape** (HP:0001363)

### Other systemic phenotypes
- **Conductive and/or sensorineural hearing loss** (HP:0000405 / HP:0000407)
- **Feeding difficulties** (HP:0011968)
- **Multiple joint contractures / arthrogryposis** (HP:0002804) — severe neonatal presentation
- **Poor cardiopulmonary adaptation** in severe neonatal cases

Dirani et al. described a severe neonatal case in which *"the patient had poor extra-uterine cardiopulmonary adaptation that required mechanical ventilation, and feeding difficulties were noted with hypotonicity"* ([PMID: 40713540](https://pubmed.ncbi.nlm.nih.gov/40713540/)), expanding the phenotype to include congenital arthrogryposis.

**Quality-of-life impact:** Severe expressive language impairment and intellectual disability substantially affect communication, education, and independent daily functioning. Hearing loss, feeding difficulties, and motor/contracture involvement add to care burden. No formal EQ-5D/SF-36/PROMIS data exist for this ultra-rare disorder.

---

## 4. Genetic / Molecular Information

**Causal gene:** ***MN1*** (Meningioma-1), chromosome **22q12.1**, HGNC:7180. *MN1* has an unusual **two-exon structure**, and its coding sequence is largely within the terminal exon.

**Pathogenic variant class and location.** All reported CEBALID-causing variants are **truncating (nonsense or frameshift)** and cluster in the **terminal exon or the extreme 3′ region of exon 1**. This genomic location is central to pathogenesis: it causes **escape from nonsense-mediated mRNA decay (NMD)**, so a truncated protein is actually produced. Mak et al.: *"All mutations, including the recurrent variant p.Arg1295\* observed in 8/21 probands, fall in the terminal exon or the extreme 3' region of exon 1, and are therefore predicted to result in escape from nonsense-mediated mRNA decay"* ([PMID: 31834374](https://pubmed.ncbi.nlm.nih.gov/31834374/)); NMD-escape was confirmed in patient fibroblasts.

**Recurrent variant.** **p.Arg1295\*** (c.3883C>T) is a recurrent hotspot, present in 8/21 probands in Mak et al.—consistent with a CpG-dinucleotide mutational hotspot, not a population founder effect.

**Functional consequence — gain/change of function.** Miyake et al. demonstrated that *"the deletion of the C-terminal region led to increased protein stability, an inhibitory effect on cell proliferation, and enhanced MN1 aggregation in nuclei compared to what occurred in the wild type, suggesting that a gain-of-function mechanism is involved in this disease"* ([PMID: 31839203](https://pubmed.ncbi.nlm.nih.gov/31839203/)). Mutant MN1 showed **impaired binding to ZBTB24 and to RING1** (an E3 ubiquitin ligase), proposed to interfere with ubiquitin-mediated proteasomal degradation and thereby increase the amount of the stabilized mutant protein.

**Variant classification (ACMG/AMP):** De novo truncating *MN1* variants in the NMD-escape region are classified **pathogenic/likely pathogenic** (standard PVS1 loss-of-function logic must be applied cautiously because canonical LOF is *not* the mechanism—position-aware interpretation is essential). Importantly, **MN1 whole-gene deletions cause a milder/different phenotype**, underscoring that variant *position and type* drive the CEBALID phenotype.

**Allele frequency:** Absent from population databases (gnomAD); these are private, de novo variants.

**Somatic vs germline:** The CEBALID variants are **germline (de novo)**. Separately—and distinct from CEBALID—*MN1* is a known somatic oncogene in acute myeloid leukemia (overexpression and *MN1* fusions such as MN1-ETV6/MN1-TEL), but this involves full-length/N-terminal MN1 overexpression, a different mechanism unrelated to the germline C-terminal truncation syndrome.

**Modifier genes / epigenetics / chromosomal abnormalities:** No disease-specific modifier genes or epigenetic signatures have been reported for CEBALID. No recurrent chromosomal abnormalities are associated (contrast: 22q microdeletions involving *MN1* produce a distinct, milder presentation).

---

## 5. Environmental Information

**Not applicable.** CEBALID is a purely genetic, de novo dominant malformation syndrome. No environmental factors, toxins, lifestyle factors, or infectious agents are implicated in its causation or triggering.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. A **de novo truncating variant** (nonsense/frameshift) arises in the terminal exon / extreme 3′ of exon 1 of *MN1* → **leads to** a transcript with a premature stop codon positioned to **escape NMD** (demonstrated in patient fibroblasts).
2. NMD escape → **results in** translation of a **C-terminally truncated MN1 protein** (rather than no protein).
3. Loss of the C-terminus → **impairs binding to RING1 (E3 ubiquitin ligase) and ZBTB24** → **leads to** reduced ubiquitin-mediated proteasomal degradation → **increased mutant protein stability** (demonstrated in vitro).
4. Stabilized mutant MN1 → **results in** **enhanced nuclear aggregation** and an **inhibitory effect on cell proliferation** (demonstrated in vitro) — a **gain/change-of-function** state, not haploinsufficiency.
5. Altered MN1 coactivator activity → **dysregulates MN1-dependent transcriptional programs**, including **retinoic-acid-receptor (RAR/RXR) signaling** (MN1 synergizes with p160/p300 coactivators) and the **MN1→*Tbx22* axis** in palate development (*inferred* link from model organisms to the human phenotype).
6. Disrupted transcriptional programs during embryogenesis → **impair intramembranous ossification of cranial bones and posterior palate growth** (demonstrated in *Mn1* mouse knockouts) and **perturb hindbrain/forebrain patterning** → **results in** the clinical malformations.
7. **Branch A (craniofacial):** → midface hypoplasia, dysmorphic ears, cleft/high-arched palate, craniosynostosis.
   **Branch B (brain):** → partial rhombencephalosynapsis, perisylvian polymicrogyria, corpus callosum anomalies → intellectual disability and severe expressive language delay.

```
 de novo MN1 truncating variant (terminal exon / 3' exon 1)
            │  escapes NMD (confirmed in fibroblasts)
            ▼
 C-terminally truncated MN1 protein produced
            │  loses RING1 / ZBTB24 binding → less proteasomal degradation
            ▼
 ↑ protein stability + nuclear aggregation (GAIN/CHANGE OF FUNCTION)
            │
            ▼
 Dysregulated MN1 transcriptional coactivation
   ├── RAR/RXR + p160/p300 retinoic-acid signaling (in vitro)
   └── MN1 → Tbx22 posterior-palate program (mouse)
            │
            ▼
 Impaired membranous ossification / palate growth / hindbrain patterning
            │
     ┌──────┴───────┐
     ▼              ▼
 CRANIOFACIAL     BRAIN
 midface hypo-    rhombencephalo-
 plasia, ears,    synapsis, PMG,
 palate, cranio-  CC anomalies
 synostosis       → ID + language delay
```

### Molecular pathways and protein function
MN1 is a **transcriptional coactivator**, not a sequence-specific transcription factor. van Wely et al. showed that *"MN1 is a transcription coactivator rather than a sequence-specific transcription factor, and that it may stimulate RAR/RXR-mediated transcription through interaction with p160 and p300"* and that *"The combination of MN1 and ligand-activated retinoic acid receptor leads to a synergistic induction of expression directed by the LTR"* ([PMID: 12569362](https://pubmed.ncbi.nlm.nih.gov/12569362/)). This places MN1 within **retinoic acid / nuclear-receptor signaling** (RAR-RXR; CHEBI:26536 retinoic acid), a pathway central to craniofacial and neural development—offering a plausible mechanistic bridge to the CEBALID phenotype. MN1 additionally interacts with homeodomain transcription factors **PBX1 and PKNOX1** and with **ZBTB24**.

### Developmental genetics of the palate
Liu et al. demonstrated that *"mice lacking the transcription factor Mn1 have defects in posterior but not anterior palatal growth"* and *"identified Tbx22, the mouse homolog of the human X-linked cleft palate gene, as a putative downstream target of Mn1 transcriptional activation"* ([PMID: 18948418](https://pubmed.ncbi.nlm.nih.gov/18948418/)). MN1 activated human and mouse *Tbx22* promoters and dose-dependently increased endogenous *Tbx22* mRNA, defining an **MN1 → Tbx22** axis for posterior palate development.

### Cranial bone development
Meester-Smoor et al. showed *Mn1*-null mice *"die at birth or shortly thereafter as the result of a cleft palate"* and concluded *"Mn1 is an important factor in development of membranous bones"* ([PMID: 15870292](https://pubmed.ncbi.nlm.nih.gov/15870292/)). Null mice show agenesis of the alisphenoid, squamosal and vomer bones (formed almost exclusively by intramembranous ossification), with hypoplasia of frontal/parietal/interparietal bones—paralleling the human craniofacial skeletal phenotype.

### Cell types and processes (ontology suggestions)
- **Cellular processes:** transcriptional coactivation (GO:0003713), RAR/RXR-mediated signaling, regulation of osteoblast differentiation (GO:0045667), intramembranous ossification (GO:0001957), cerebellum/hindbrain development (GO:0021549, GO:0030902), palate development (GO:0060021), protein stabilization/aggregation, ubiquitin-dependent protein catabolism (GO:0006511).
- **Cell types (CL):** osteoblast (CL:0000062), cranial neural crest cell (CL:0000333), cerebellar/hindbrain neuronal progenitors, palatal mesenchymal cells.
- **Subcellular (GO CC):** nucleus (GO:0005634) — site of mutant MN1 aggregation.

---

## 7. Anatomical Structures Affected

**Primary organs/systems:**
- **Brain / central nervous system** (UBERON:0000955) — cerebellum and vermis (UBERON:0002037 / UBERON:0004086) with rhombencephalosynapsis; cerebral cortex perisylvian region (polymicrogyria); corpus callosum (UBERON:0002336).
- **Craniofacial skeleton** (UBERON:0010363 skeleton of skull) — midface, cranial membranous bones, palate (UBERON:0001716), orbits.
- **Ears** (UBERON:0001690) — external ear dysmorphism; auditory apparatus (hearing loss).

**Secondary/associated involvement:**
- **Musculoskeletal system** — joint contractures (arthrogryposis) in severe cases; hypotonia.
- **Cardiopulmonary system** — poor neonatal adaptation in severe presentations (secondary).
- **Cerebral vasculature** — persistent trigeminal artery.

**Tissue/cell level:** connective/skeletal tissue (membranous bone, osteoblasts), neural tissue (cerebellar and cortical neurons/progenitors), neural-crest-derived craniofacial mesenchyme.

**Subcellular:** nucleus (mutant protein aggregation).

**Lateralization:** Brain malformations are typically **midline/bilateral** (vermis, corpus callosum) or **bilateral** (perisylvian polymicrogyria); craniofacial features are **bilateral and symmetric**.

---

## 8. Temporal Development

- **Onset:** **Congenital** (prenatal/neonatal). Structural malformations are established during embryogenesis; dysmorphism and brain anomalies are present at birth, with developmental delay apparent in infancy/early childhood.
- **Onset pattern:** Insidious with respect to neurodevelopment (delays recognized over time); malformations are present from birth.
- **Progression:** The disorder is **static/non-progressive (malformative)**. There is no neurodegeneration; disability is **lifelong and stable** rather than worsening.
- **Disease course:** Chronic, lifelong. No relapsing-remitting or episodic pattern. Severe neonatal presentations (e.g., arthrogryposis with cardiopulmonary maladaptation) carry higher early morbidity/mortality risk.
- **Critical period:** The structural/developmental window is **embryonic craniofacial and hindbrain morphogenesis** (already passed by birth), making structural prevention impossible post-natally; early-childhood developmental intervention is the actionable window for functional outcomes.

---

## 9. Inheritance and Population

- **Inheritance pattern:** **Autosomal dominant**, essentially always **de novo**. Mak et al.: *"We identified a cluster of de novo truncating mutations in MN1"* ([PMID: 31834374](https://pubmed.ncbi.nlm.nih.gov/31834374/)). Recurrence risk for parents of an affected child is low (apart from rare germline mosaicism).
- **Penetrance:** Appears **complete** for the recognizable gestalt among carriers of the specific C-terminal truncating variants.
- **Expressivity:** **Variable**, ranging from the "classic" gestalt to severe neonatal arthrogryposis presentations.
- **Genetic anticipation:** Not applicable (not a repeat-expansion disorder).
- **Germline mosaicism:** Theoretically possible but not well documented; relevant for rare recurrence.
- **Founder effects / consanguinity:** None. The recurrent **p.Arg1295\*** reflects a **CpG mutational hotspot**, not a founder allele; consanguinity is irrelevant for a de novo dominant disorder.
- **Carrier frequency:** Not applicable (de novo, not inherited).

**Epidemiology / demographics:**
- **Prevalence/incidence:** Unknown—ultra-rare. Dirani et al.: *"less than 30 cases have been reported worldwide"* ([PMID: 40713540](https://pubmed.ncbi.nlm.nih.gov/40713540/)).
- **Sex ratio:** No established sex predilection.
- **Ethnic/geographic distribution:** No established predilection; cases reported across multiple populations.

---

## 10. Diagnostics

**Recommended approach:** Clinical suspicion from the gestalt (**midface hypoplasia + severe expressive language delay + partial rhombencephalosynapsis on MRI**), confirmed by **molecular detection of a heterozygous truncating *MN1* variant in the terminal exon or extreme 3′ of exon 1**.

**Genetic testing:**
- **Whole-exome sequencing (WES)** — the principal confirmatory test. Dirani et al.: *"Whole exome sequencing confirmed the diagnosis of CEBALID syndrome"* ([PMID: 40713540](https://pubmed.ncbi.nlm.nih.gov/40713540/)).
- **Whole-genome sequencing (WGS)** — also effective.
- **Single-gene / targeted *MN1* sequencing** — appropriate when the phenotype is strongly suggestive.
- **Interpretation caveat:** Variant **position and type are decisive**—3′ truncating (NMD-escape) variants cause CEBALID, whereas **whole-gene deletions produce a different, milder phenotype**. A chromosomal microarray detecting an *MN1* deletion should *not* be equated with CEBALID.

**Imaging:**
- **Brain MRI** is the key diagnostic adjunct, demonstrating **partial rhombencephalosynapsis** (vermian hypoplasia with cerebellar hemisphere fusion), **perisylvian polymicrogyria**, corpus callosum anomalies, abnormal posterior clinoid processes, and persistent trigeminal artery.

**Other clinical tests:**
- **Audiologic evaluation** (conductive/sensorineural hearing loss).
- **Ophthalmologic assessment** (shallow orbits/proptosis).
- No specific biochemical biomarker or metabolic test exists.

**Differential diagnosis:** Other causes of rhombencephalosynapsis (e.g., Gómez-López-Hernández syndrome, VACTERL-H), other midface-hypoplasia syndromes, and other polymicrogyria syndromes. The specific combination of midface hypoplasia, severe expressive language delay, and partial rhombencephalosynapsis plus a 3′ truncating *MN1* variant is distinguishing.

**Screening:** No population or newborn screening exists (ultra-rare, de novo). Cascade testing of parents is generally uninformative given the de novo origin but may be offered for recurrence-risk counseling and mosaicism assessment.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** No formal survival statistics exist. The disorder is **not inherently lethal** in classic presentations; most reported individuals survive with lifelong disability. **Severe neonatal presentations** (arthrogryposis with cardiopulmonary maladaptation requiring mechanical ventilation) carry elevated early morbidity and potential mortality.
- **Morbidity/function:** Substantial, driven by **intellectual disability and severe expressive language impairment**, with additional impact from hearing loss, feeding difficulties, motor involvement, and craniofacial anomalies.
- **Disease course:** Static/non-progressive; disability is stable and lifelong.
- **Complications:** Feeding difficulties, hearing impairment, sequelae of cleft palate/craniosynostosis, and in severe cases respiratory compromise.
- **Prognostic factors:** Severity of brain malformation and neonatal cardiopulmonary/contracture involvement likely predict outcome, though no validated prognostic model exists for this small case set.

---

## 12. Treatment

**There is no disease-specific or curative pharmacotherapy.** Management is **supportive and multidisciplinary**, targeting individual manifestations:

| Domain | Intervention | NCIT concept (suggested) |
|--------|--------------|--------------------------|
| Developmental | Early intervention, special education | Developmental therapy |
| Communication | Speech/language therapy (severe expressive delay) | Speech Therapy (NCIT:C15336) |
| Motor | Physical & occupational therapy (hypotonia, contractures) | Physical Therapy (NCIT:C15368); Occupational Therapy (NCIT:C15337) |
| Hearing | Audiologic evaluation, hearing aids | Audiologic assessment |
| Vision | Ophthalmologic monitoring | Ophthalmologic examination |
| Craniofacial | Surgical repair of cleft palate; craniosynostosis surgery | Surgical Procedure (NCIT:C15329) |
| Feeding | Feeding support / nutritional management | Nutritional Support (NCIT:C15335) |
| Neonatal (severe) | Respiratory support/mechanical ventilation as needed | Mechanical Ventilation (NCIT:C70902) |
| Family | Genetic counseling | Genetic Counseling (NCIT:C15648) |

- **Pharmacogenomics / targeted / gene / cell / RNA therapies:** None currently applicable or in trials for CEBALID.
- **Experimental treatments:** No disease-specific clinical trials (no NCT identifiers) are available.
- **Personalized medicine:** Limited to position-aware genetic diagnosis for counseling and anticipatory care.

---

## 13. Prevention

- **Primary prevention:** Not possible—de novo variant; no modifiable risk factors.
- **Secondary prevention:** Early developmental intervention and anticipatory management of hearing, feeding, vision, and craniofacial complications to optimize functional outcomes.
- **Tertiary prevention:** Multidisciplinary management of complications (cleft palate repair, craniosynostosis surgery, hearing/feeding support).
- **Genetic counseling:** Essential. Because variants are de novo, **recurrence risk for parents is low** (rare germline mosaicism excepted). Prenatal/preimplantation testing is feasible for a known familial variant but rarely indicated given the low recurrence risk.
- **Immunization / public health / behavioral / environmental interventions:** Not applicable.

---

## 14. Other Species / Natural Disease

- **Orthologous gene:** Mouse ***Mn1*** (human *MN1* NCBI Gene ID 4330). The gene and its developmental roles are **evolutionarily conserved**.
- **Natural disease in other species:** No naturally occurring CEBALID-equivalent disease is documented in companion animals or wildlife (no OMIA entry for a spontaneous *MN1* truncation disorder). The animal evidence comes from **engineered mouse models** rather than natural disease.
- **Comparative pathology:** *Mn1*-null mice recapitulate the **craniofacial/palate** component (cleft palate, membranous bone agenesis) but model loss of function rather than the human gain-of-function truncation—an important caveat for cross-species comparison.
- **Zoonotic/transmission:** Not applicable (genetic disorder).

---

## 15. Model Organisms

- **Mouse (*Mus musculus*):** The principal model. **Constitutive *Mn1* knockout** mice (Meester-Smoor et al.) die at birth from cleft palate and show agenesis/hypoplasia of intramembranous cranial bones; heterozygotes show hypoplastic membranous bones with incomplete-penetrance cleft palate, and *Mn1*+/− animals followed to 30 months showed no increased tumor incidence ([PMID: 15870292](https://pubmed.ncbi.nlm.nih.gov/15870292/)). These models established MN1's role in **membranous bone and palate development** and the downstream **MN1→*Tbx22*** axis ([PMID: 18948418](https://pubmed.ncbi.nlm.nih.gov/18948418/)).
- **In vitro / cellular models:** Transfection assays (e.g., NIH3T3) demonstrated **MN1 coactivation of RAR/RXR via p160/p300** ([PMID: 12569362](https://pubmed.ncbi.nlm.nih.gov/12569362/)) and, for the disease variants, **increased protein stability, nuclear aggregation, proliferation inhibition, and altered interactor binding (RING1, ZBTB24, PBX1, PKNOX1)** ([PMID: 31839203](https://pubmed.ncbi.nlm.nih.gov/31839203/)). Patient-derived **fibroblasts** confirmed NMD escape of the mutant transcript.
- **Phenotype recapitulation / limitations:** Mouse *Mn1* knockouts reproduce the **craniofacial/palatal** phenotype well but model **loss of function**, whereas human CEBALID is a **gain/change-of-function** truncation. **No mouse model expressing the human C-terminal truncation has been reported**, and the **brain malformation (rhombencephalosynapsis)** is not captured by existing knockouts—key gaps for mechanistic study.

---

## Key Findings (Consolidated)

| # | Finding | Primary evidence (PMID) |
|---|---------|-------------------------|
| F1 | CEBALID is caused by de novo C-terminal truncating *MN1* variants acting via gain-of-function | 31839203, 31834374 |
| F2 | Variants escape NMD; recurrent p.Arg1295\* in 8/21 probands; truncated protein produced | 31834374 |
| F3 | Truncated MN1 shows ↑stability, nuclear aggregation, ↓proliferation, impaired RING1/ZBTB24 binding | 31839203 |
| F4 | Hallmark gestalt: midface hypoplasia + severe expressive language delay + ID | 31834374 |
| F5 | Distinctive brain malformation: partial rhombencephalosynapsis (8/10 imaged) | 31834374, 40713540 |
| F6 | MN1 is a RAR/RXR transcriptional coactivator synergizing with p160/p300 | 12569362 |
| F7 | MN1 acts upstream of *Tbx22*, regulating posterior palate growth | 18948418 |
| F8 | MN1 essential for intramembranous ossification of cranial bones (mouse null → cleft palate) | 15870292 |
| F9 | Ultra-rare (<30 cases); AD de novo; WES-confirmed; supportive management | 40713540, 31834374 |

---

## Mechanistic Model / Interpretation (Synthesis)

CEBALID is best understood as a **dominant "toxic/altered-product" disorder of a developmental transcriptional coactivator**. The unusual two-exon architecture of *MN1* means that truncating variants in the terminal exon escape NMD and produce a stable, C-terminally truncated protein. Loss of the C-terminus disrupts interactions (RING1, ZBTB24) that normally promote MN1's proteasomal turnover, so the aberrant protein **accumulates and aggregates in the nucleus**, producing a gain/change-of-function rather than simple loss. Because wild-type MN1 normally **coactivates retinoic-acid-receptor signaling** and drives developmental programs including the **MN1→Tbx22** posterior-palate axis and **intramembranous ossification**, the dysregulated mutant perturbs **craniofacial morphogenesis** (midface hypoplasia, ears, palate, cranial bones) and **hindbrain/forebrain patterning** (rhombencephalosynapsis, polymicrogyria), yielding the paired craniofacial–brain phenotype and its neurodevelopmental consequences. The strongest-evidence links are the human genetic/functional data (Mak, Miyake) and the mouse craniofacial data (Meester-Smoor, Liu); the retinoic-acid and *Tbx22* connections to the full human brain phenotype remain **plausible but partly inferred**.

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | Contribution |
|------|-----------------|---------------|--------------|
| [31834374](https://pubmed.ncbi.nlm.nih.gov/31834374/) | *MN1 C-terminal truncation syndrome ... with partial rhombencephalosynapsis* (Mak 2020) | Human clinical (n=23) | Defines phenotype gestalt, recurrent p.Arg1295\*, NMD-escape mechanism, rhombencephalosynapsis |
| [31839203](https://pubmed.ncbi.nlm.nih.gov/31839203/) | *Gain-of-Function MN1 Truncation Variants...* (Miyake 2020) | Human + in vitro (n=3) | Establishes de novo causation and gain-of-function mechanism (↑stability, aggregation) |
| [40713540](https://pubmed.ncbi.nlm.nih.gov/40713540/) | *Extremely rare case of CEBALID presenting as congenital arthrogryposis* (Dirani 2025) | Human case report | CEBALID acronym, rarity (<30 cases), WES diagnosis, severe neonatal/arthrogryposis spectrum |
| [15870292](https://pubmed.ncbi.nlm.nih.gov/15870292/) | *Targeted disruption of Mn1... membranous bones* (Meester-Smoor 2005) | Mouse model | MN1 essential for membranous bone & palate development |
| [18948418](https://pubmed.ncbi.nlm.nih.gov/18948418/) | *Mn1 acts upstream of Tbx22...* (Liu 2008) | Mouse model | MN1→Tbx22 axis for posterior palate growth |
| [12569362](https://pubmed.ncbi.nlm.nih.gov/12569362/) | *MN1 oncoprotein synergizes with RAC3 and p300...* (van Wely 2003) | In vitro | MN1 is RAR/RXR coactivator via p160/p300 |

**Context literature (not CEBALID-causal):** Multiple papers ([PMID: 33542482](https://pubmed.ncbi.nlm.nih.gov/33542482/), [26927674](https://pubmed.ncbi.nlm.nih.gov/26927674/), [22905229](https://pubmed.ncbi.nlm.nih.gov/22905229/), [22488406](https://pubmed.ncbi.nlm.nih.gov/22488406/), [23646898](https://pubmed.ncbi.nlm.nih.gov/23646898/), [19379599](https://pubmed.ncbi.nlm.nih.gov/19379599/)) document *MN1*'s **somatic oncogenic role in AML** (overexpression, MN1 fusions, poor prognosis). These are mechanistically distinct from the germline C-terminal truncation syndrome but reinforce MN1's biology as a dosage-sensitive transcriptional coactivator.

---

## Limitations and Knowledge Gaps

1. **Tiny evidence base:** Fewer than ~30 reported cases; all epidemiology (prevalence, incidence, sex/ethnic distribution, survival) is unavailable or estimated.
2. **No humanized model:** No mouse or organoid model expressing the human C-terminal truncation; the hallmark **rhombencephalosynapsis** is not recapitulated by existing *Mn1* knockouts.
3. **Mechanistic inference:** The RAR/RXR-coactivation and *Tbx22* pathways are established for wild-type MN1 and palate, but their precise disruption by the truncated protein—and their link to the human brain malformation—remains partly inferred.
4. **Genotype–phenotype detail:** Why some variants (e.g., arthrogryposis presentations) are more severe is unknown; no validated modifier genes.
5. **No biomarkers or targeted therapy:** No molecular diagnostic biomarker beyond sequencing; no disease-specific treatment or clinical trials.

---

## Proposed Follow-up Experiments / Actions

1. **Generate a knock-in mouse (or human iPSC-derived organoid)** carrying the recurrent **p.Arg1295\*** truncation to test whether the stabilized mutant produces rhombencephalosynapsis and midface hypoplasia—directly modeling gain-of-function.
2. **Cerebellar/cortical organoids** from patient iPSCs to dissect hindbrain patterning defects and screen for pathway rescue (e.g., retinoic-acid signaling modulators).
3. **Transcriptomic/ChIP profiling** of mutant vs wild-type MN1 in neural-crest and neural progenitor cells to define dysregulated target genes (test *TBX22* and RAR/RXR targets).
4. **Establish an international CEBALID registry** to capture natural history, genotype–phenotype correlations, and outcomes across the <30 known cases and future diagnoses.
5. **Degradation-targeting proof of concept:** Since the pathogenic protein is abnormally stabilized, test whether restoring its proteasomal turnover (e.g., modulating RING1-mediated ubiquitination) reduces nuclear aggregation in cellular models.

---

*Report compiled from 8 confirmed findings across 5 investigation iterations and 13 reviewed papers. Evidence types span human clinical case series, mouse genetic models, and in vitro functional assays.*


## Artifacts

- [OpenScientist final report](CEBALID_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](CEBALID_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 12 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.
