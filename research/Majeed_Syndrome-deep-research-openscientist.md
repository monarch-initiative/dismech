---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-08T14:50:49.556467'
end_time: '2026-09-08T15:09:00.138005'
duration_seconds: 1090.58
template_file: /tmp/majeed_prompt.md
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
  path: Majeed_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Majeed_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Majeed Syndrome
- **MONDO ID:** MONDO:0012316 (if available)
- **Category:** Autosomal recessive autoinflammatory syndrome from LPIN2 deficiency with sterile osteomyelitis and dyserythropoietic anemia

## Research Objectives

Please provide a comprehensive research report on **Majeed Syndrome** covering all of the
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

# Majeed Syndrome: A Comprehensive Disease Characterization

**Disease:** Majeed Syndrome
**MONDO ID:** MONDO:0012316 · **OMIM:** #609628 · **Orphanet:** ORPHA:77297
**Gene:** *LPIN2* (OMIM \*605519; HGNC:14100)
**Category:** Autosomal-recessive systemic autoinflammatory disease (NLRP3 inflammasomopathy) caused by LPIN2 deficiency, characterized by sterile osteomyelitis and congenital dyserythropoietic anemia

---

## Summary

Majeed syndrome is an ultra-rare, autosomal-recessive systemic autoinflammatory disease caused by biallelic loss-of-function mutations in **LPIN2** (chromosome 18p11.31; HGNC:14100; OMIM \*605519), which encodes the phosphatidic-acid-phosphatase and transcriptional co-regulator **lipin-2**. The disease was genetically defined by homozygosity mapping in two consanguineous Arab families, localizing the locus to a 1.8 Mb interval on chromosome 18p and identifying segregating homozygous LPIN2 mutations ([PMID: 15994876](https://pubmed.ncbi.nlm.nih.gov/15994876/)). It presents in infancy — typically before age three — with a defining triad: **chronic recurrent multifocal osteomyelitis (CRMO)**, **congenital dyserythropoietic anemia (CDA)**, and, with or without, a **neutrophilic dermatosis** (Sweet-like), accompanied by recurrent fevers and growth failure ([PMID: 33670882](https://pubmed.ncbi.nlm.nih.gov/33670882/)).

Mechanistically, the loss of lipin-2 de-represses the **NLRP3 inflammasome**. Lipin-2 normally restrains IL-1β production by inhibiting activation and sensitization of the purinergic **P2X7 receptor** and by limiting MAPK-driven pro-IL-1β synthesis during priming; its loss over-activates NLRP3, driving excess **IL-1β** ([PMID: 28031477](https://pubmed.ncbi.nlm.nih.gov/28031477/)). This places Majeed syndrome formally among the **NLRP3 inflammasomopathies** ([PMID: 29912021](https://pubmed.ncbi.nlm.nih.gov/29912021/)). In bone, LPIN2 mutations skew macrophages toward a pro-osteoclastogenic phenotype and accelerate osteoclastogenesis, connecting the molecular lesion to the sterile bone disease ([PMID: 33314777](https://pubmed.ncbi.nlm.nih.gov/33314777/), [PMID: 33809261](https://pubmed.ncbi.nlm.nih.gov/33809261/)). Consistent with the central role of IL-1, **IL-1 blockade (anakinra, canakinumab) is the most effective therapy**, producing dramatic and sustained remission, whereas NSAIDs, corticosteroids, methotrexate and TNF inhibitors give only partial responses ([PMID: 41113563](https://pubmed.ncbi.nlm.nih.gov/41113563/), [PMID: 39255247](https://pubmed.ncbi.nlm.nih.gov/39255247/)).

The disease is extraordinarily rare — as of 2023 only ~31 individuals from 18 families had been reported, rising to ~35 patients by 2025 — and is strongly linked to parental consanguinity ([PMID: 37865862](https://pubmed.ncbi.nlm.nih.gov/37865862/), [PMID: 41113563](https://pubmed.ncbi.nlm.nih.gov/41113563/)). The principal unresolved mechanistic gap is the molecular basis of the congenital dyserythropoietic anemia, which — unlike the bone and skin inflammation — is not explained by a defined pathway, though its reversal by IL-1 blockade implies a substantial inflammation-driven component ([PMID: 39255247](https://pubmed.ncbi.nlm.nih.gov/39255247/)).

---

## 1. Disease Information

Majeed syndrome is a monogenic, multi-system autoinflammatory disorder of the innate immune system. As summarized in a comprehensive review, *"Majeed syndrome is a multi-system inflammatory disorder affecting humans that presents with chronic multifocal osteomyelitis, congenital dyserythropoietic anemia, with or without a neutrophilic dermatosis"* ([PMID: 33670882](https://pubmed.ncbi.nlm.nih.gov/33670882/)).

**Key identifiers**
| Resource | Identifier |
|---|---|
| MONDO | MONDO:0012316 |
| OMIM (disease) | #609628 |
| OMIM (gene) | \*605519 (LPIN2) |
| Orphanet | ORPHA:77297 |
| MeSH | Majeed syndrome / autoinflammatory syndromes |
| HGNC (gene) | HGNC:14100 (LPIN2) |

**Synonyms / alternative names:** Chronic recurrent multifocal osteomyelitis and congenital dyserythropoietic anemia (CRMO with CDA); CRMO–CDA syndrome; LPIN2-related autoinflammatory syndrome.

**Data source type:** The disease-level knowledge in this report is derived from **aggregated disease-level resources** (OMIM, Orphanet, MONDO) supplemented by **individual patient case reports and small case series** in the primary literature. There is no large EHR-derived cohort; because only ~31–35 patients have ever been reported, all epidemiologic and phenotypic estimates rest on aggregated case reports.

---

## 2. Etiology

**Disease causal factors — genetic.** Majeed syndrome is a **monogenic** disease caused by biallelic (homozygous or compound-heterozygous) loss-of-function mutations in **LPIN2**. Homozygosity mapping in six affected individuals from two unrelated consanguineous Arab families mapped the locus to a 5.5 cM (1.8 Mb) interval on chromosome 18p; *"Examination of genes in this interval led to the identification of homozygous mutations in LPIN2 in affected individuals from the two families"* ([PMID: 15994876](https://pubmed.ncbi.nlm.nih.gov/15994876/)). The gene *"was mapped to a 5.5 cM interval (1.8 Mb) on chromosome 18p."* Inheritance is autosomal recessive.

**Genetic risk factors.** The single causal locus is LPIN2. **Consanguinity** is the dominant risk factor because the disease is recessive: in a multicenter Arab pediatric autoinflammatory cohort, parental consanguinity was 74.6% ([PMID: 31741047](https://pubmed.ncbi.nlm.nih.gov/31741047/)). No independent susceptibility loci or modifier genes have been established.

**Environmental / lifestyle risk factors.** No environmental exposure is required to cause the disease. However, a well-defined **gene–environment interaction** exists: in murine and human macrophages, *"Depletion of lipin-2 promotes the increased expression of the proinflammatory genes Il6, Ccl2, and Tnfα, which depends on the overstimulation of the JNK1/c-Jun pathway by saturated fatty acids"* ([PMID: 22334674](https://pubmed.ncbi.nlm.nih.gov/22334674/)). Thus dietary **saturated fatty acids** amplify inflammation specifically in a lipin-2-deficient background. In the related *cmo* mouse model of CRMO, *"dietary manipulation can alter the microbiome and protect these mice from the development of sterile osteomyelitis in vivo"* ([PMID: 28361334](https://pubmed.ncbi.nlm.nih.gov/28361334/)), suggesting diet/microbiome as environmental modifiers of disease expression.

**Protective factors.** No human genetic protective variants are documented. The murine data above indicate that a low-saturated-fat diet or microbiome modulation could be **environmentally protective**, but this has not been validated in patients.

---

## 3. Phenotypes

Onset is typically in infancy, usually **before age three**: a review of 35 reported patients found *"most presented before age three with CRMO and recurrent fever, but the severity of CDA varied widely"* ([PMID: 41113563](https://pubmed.ncbi.nlm.nih.gov/41113563/)) — documenting both the neonatal/early-childhood onset and the marked variable expressivity of the anemia.

| Phenotype | Type | HPO term | Onset | Severity / course | Frequency |
|---|---|---|---|---|---|
| Chronic recurrent multifocal osteomyelitis (sterile) | Clinical sign / imaging | HP:0040211 (Recurrent multifocal osteomyelitis) | Infancy (<3 y) | Recurrent, relapsing; episodic flares | Near-universal (defining) |
| Bone pain | Symptom | HP:0002653 | Infancy/childhood | Episodic, painful | Very frequent |
| Congenital dyserythropoietic anemia (microcytic) | Laboratory abnormality | HP:0001939 / HP:0001935 | Congenital/neonatal | Variable — mild to transfusion-dependent | Frequent; severity variable |
| Neutrophilic dermatosis (Sweet-like) | Physical manifestation | HP:0025573 (Neutrophilic dermatosis) | Infancy/childhood | Variable; "with or without" | Subset of patients |
| Recurrent fever | Symptom | HP:0001954 | Infancy | Episodic | Frequent |
| Growth failure / failure to thrive | Clinical sign | HP:0001508 | Infancy/childhood | Progressive if untreated | Frequent |
| Joint swelling/contractures, arthralgia | Clinical sign | HP:0001386 / HP:0002829 | Childhood | Episodic | Variable |
| Neutropenia (in some) | Laboratory abnormality | HP:0001875 | Infancy | Variable | Occasional (PMID 31727123) |
| Psychomotor/developmental delay (CNS involvement) | Behavioral/neurological | HP:0001263 | Childhood | Variable | Occasional (PMID 34365623) |

Additional features reported in individual cases include muscle involvement adjacent to osteomyelitis, delayed language/motor development, and (rarely) severe neutropenia ([PMID: 34365623](https://pubmed.ncbi.nlm.nih.gov/34365623/), [PMID: 31727123](https://pubmed.ncbi.nlm.nih.gov/31727123/)).

**Quality of life impact.** No formal EQ-5D/SF-36/PROMIS studies exist for this ultra-rare disease. Qualitatively, untreated disease causes chronic bone pain, recurrent fevers, transfusion dependence in severe anemia, growth failure, and functional impairment from bone lesions and joint contractures — with substantial improvement reported after IL-1 blockade.

---

## 4. Genetic / Molecular Information

**Causal gene.** **LPIN2** (HGNC:14100; OMIM \*605519; chromosome 18p11.31), encoding **lipin-2**, a member of the lipin/Pah family of Mg²⁺-dependent phosphatidic acid phosphatases (PAP1) that also act as transcriptional co-regulators of lipid metabolism.

**Pathogenic variants.** Both homozygous (in consanguineous families) and compound-heterozygous variants are reported, spanning missense, frameshift, nonsense, and splice-site classes:
- Original homozygous mutations in Arab families ([PMID: 15994876](https://pubmed.ncbi.nlm.nih.gov/15994876/)).
- Compound heterozygous c.1966A>G and c.2534delG in a Han Chinese boy ([PMID: 34365623](https://pubmed.ncbi.nlm.nih.gov/34365623/)).
- Splice-donor c.2327+1G>C (paternal) with frameshift c.1691_1694delGAGA (p.Arg564Lysfs\*3, maternal), associated with a mild phenotype plus severe neutropenia ([PMID: 31727123](https://pubmed.ncbi.nlm.nih.gov/31727123/)).
- Homozygous p.S734L reported in siblings from Qatar ([PMID: 27860302](https://pubmed.ncbi.nlm.nih.gov/27860302/)).
- Novel variants from Indian families ([PMID: 37865862](https://pubmed.ncbi.nlm.nih.gov/37865862/), [PMID: 33993107](https://pubmed.ncbi.nlm.nih.gov/33993107/)).

**Variant classification & functional consequence.** Reported disease variants are classified **pathogenic/likely pathogenic** (ACMG/AMP) and are **loss-of-function**. Structurally, disease mutations cluster within the conserved N-Lip and C-Lip regions: *"Disease-mutations cluster within the conserved N-Lip and C-Lip regions that are separated by 500-residues in humans"* and act by two routes — *"Disease-mutations disrupt catalysis or destabilize the protein fold"* ([PMID: 32161260](https://pubmed.ncbi.nlm.nih.gov/32161260/)).

**Allele frequency / origin.** Pathogenic LPIN2 alleles are extremely rare in population databases (gnomAD); several are private founder-like alleles in consanguineous families. Origin is **germline**; no somatic/mosaic contribution is described.

**Modifier genes / epigenetics / chromosomal abnormalities.** No validated modifier genes, disease-specific epigenetic marks, or chromosomal abnormalities are reported. Lipin-2 is itself IFN/STAT-1-regulated ([PMID: 37929625](https://pubmed.ncbi.nlm.nih.gov/37929625/)), an expression-level regulatory context rather than a heritable modifier.

---

## 5. Environmental Information

- **Environmental factors / toxins:** None required for disease causation. Dietary **saturated fatty acids** act as a proinflammatory amplifier in lipin-2 deficiency via JNK1/c-Jun ([PMID: 22334674](https://pubmed.ncbi.nlm.nih.gov/22334674/)).
- **Lifestyle factors:** Diet (saturated fat load) is the only mechanistically supported lifestyle modifier; microbiome composition modulates sterile osteomyelitis in the murine model ([PMID: 28361334](https://pubmed.ncbi.nlm.nih.gov/28361334/)).
- **Infectious agents:** None. The osteomyelitis is **sterile/culture-negative** — a defining feature distinguishing it from bacterial osteomyelitis. Lipin-2 also modulates antiviral/TLR3 responses ([PMID: 37929625](https://pubmed.ncbi.nlm.nih.gov/37929625/)), but no pathogen triggers the disease.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic LOF mutation in LPIN2** results in loss of functional lipin-2 protein (via disrupted HAD-like catalysis or destabilized protein fold) ([PMID: 15994876](https://pubmed.ncbi.nlm.nih.gov/15994876/), [PMID: 32161260](https://pubmed.ncbi.nlm.nih.gov/32161260/)).
2. Loss of lipin-2 **de-represses the purinergic P2X7 receptor**, enhancing its activation/sensitization and K⁺ efflux, and removes a brake on MAPK-driven pro-IL-1β synthesis during priming: *"Lipin-2 also inhibits the activation and sensitization of the purinergic receptor P2X7"* ([PMID: 28031477](https://pubmed.ncbi.nlm.nih.gov/28031477/)).
3. This **over-activates the NLRP3 inflammasome** in macrophages/monocytes — *"lipin-2 controls excessive IL-1β formation in primary human and mouse macrophages by several mechanisms, including activation of the inflammasome NLRP3"* ([PMID: 28031477](https://pubmed.ncbi.nlm.nih.gov/28031477/)). An additional branch: lipin-2 loss increases ROS generation and mtDNA release (partly via TLR3 signaling) that further activate NLRP3 — *"lipin-2 also acts as a regulator of inflammation in a viral context by reducing the signaling through TLR3 and the generation of ROS and release of mtDNA that ultimately activate the NLRP3 inflammasome"* ([PMID: 37929625](https://pubmed.ncbi.nlm.nih.gov/37929625/)).
4. NLRP3 activation → **caspase-1 activation → excess mature IL-1β secretion** (elevated caspase-1 activity and IL-1β in patient monocytes) ([PMID: 28031477](https://pubmed.ncbi.nlm.nih.gov/28031477/), [PMID: 33314777](https://pubmed.ncbi.nlm.nih.gov/33314777/)).
5. **Branch A — Bone:** Excess IL-1β plus a lipin-2-deficient, pro-osteoclastogenic macrophage program and enhanced NF-κB signaling **accelerate osteoclastogenesis**, leading to **sterile CRMO**. Patient M2-like macrophages *"released higher levels of osteoclastogenic mediators (IL-8, IL-6, tumor necrosis factor, CCL2, macrophage inflammatory protein 1α/β, CXCL8, and CXCL1) compared to NOMID patients and healthy controls"* ([PMID: 33314777](https://pubmed.ncbi.nlm.nih.gov/33314777/)); independently, *"Deficiency of Lipin2 Results in Enhanced NF-κB Signaling and Osteoclast Formation in RAW-D Murine Macrophages"* ([PMID: 33809261](https://pubmed.ncbi.nlm.nih.gov/33809261/)).
6. **Branch B — Skin:** IL-1-driven neutrophil recruitment produces **neutrophilic dermatosis** (Sweet-like) (inferred from IL-1 biology; clinically responsive to IL-1 blockade).
7. **Branch C — Systemic:** IL-1β drives **recurrent fever, acute-phase response, and growth failure**.
8. **Branch D — Marrow/erythroid (partly inferred):** Inflammation contributes to **congenital dyserythropoietic anemia**; the precise molecular link from lipin-2 loss to dyserythropoiesis is unresolved, but anemia and marrow dyserythropoiesis reverse with IL-1 blockade, implicating inflammation ([PMID: 39255247](https://pubmed.ncbi.nlm.nih.gov/39255247/)).
9. **Environmental amplifier:** Dietary saturated fatty acids augment steps 3–7 via JNK1/c-Jun overstimulation ([PMID: 22334674](https://pubmed.ncbi.nlm.nih.gov/22334674/)).

```
 LPIN2 LOF  ──►  loss of lipin-2  ──►  P2X7 sensitization + ↓MAPK restraint
                                      + ROS/mtDNA release (TLR3 branch)
                                            │
                                            ▼
                                   NLRP3 inflammasome ↑
                                            │
                                     caspase-1 → IL-1β ↑↑
                 ┌──────────────┬───────────┼──────────────┬───────────────┐
                 ▼              ▼            ▼              ▼               ▼
        pro-osteoclast    neutrophil     fever /       dyserythropoietic  (SFA diet
        macrophages +     recruitment    acute-phase    anemia            amplifies
        NF-κB → osteoclast   → skin       + growth       (inflammation-    via JNK1/
        ↑ → STERILE CRMO   NEUTROPHILIC   failure        driven, partly    c-Jun)
                            DERMATOSIS                    inferred)
```

**Molecular pathways:** P2X7–K⁺ efflux–NLRP3 inflammasome; MAPK/JNK1–c-Jun; NF-κB; IL-1β signaling; type-I IFN/STAT-1 (regulates lipin-2). **Cellular processes:** innate immune activation, sterile inflammation, osteoclast differentiation, dyserythropoiesis. **Protein dysfunction:** loss of PAP1 (phosphatidic-acid-phosphatase) catalysis / protein destabilization. **Metabolic:** lipin-2 converts phosphatidic acid → diacylglycerol; its loss alters glycerolipid/TAG homeostasis and reduces TAG buffering of saturated-fatty-acid overload — *"the absence of lipin-2 reduces the cellular content of triacylglycerol in saturated fatty acid-overloaded macrophages"* ([PMID: 22334674](https://pubmed.ncbi.nlm.nih.gov/22334674/)). **Immune involvement:** chronic IL-1β-driven autoinflammation (not autoimmunity/immunodeficiency).

**Suggested ontology terms:** GO:0006954 (inflammatory response); GO:0032611 (IL-1β production); GO:0072559 (NLRP3 inflammasome complex assembly); GO:0002548 (monocyte chemotaxis); GO:0045453 (bone resorption); GO:0016311 (dephosphorylation). **Cell types (CL):** CL:0000235 (macrophage), CL:0000576 (monocyte), CL:0000092 (osteoclast), CL:0000775 (neutrophil), CL:0000764 (erythroid lineage cell). **Chemical entities (CHEBI):** CHEBI:16337 (phosphatidic acid), CHEBI:18035 (diacylglycerol), CHEBI:26607 (saturated fatty acid), CHEBI:29108 (Mg²⁺).

---

## 7. Anatomical Structures Affected

- **Primary organ / system — Skeleton (musculoskeletal system):** metaphyses of long bones (tibia, femur, fibula), and other multifocal sites; sacroiliac joints; adjacent soft tissue/muscle ([PMID: 34365623](https://pubmed.ncbi.nlm.nih.gov/34365623/), [PMID: 27860302](https://pubmed.ncbi.nlm.nih.gov/27860302/)). UBERON:0002481 (bone tissue), UBERON:0001474 (bone element), UBERON:0002217 (long bone), UBERON:0000979 (tibia).
- **Bone marrow / hematopoietic system:** dyserythropoiesis; UBERON:0002371 (bone marrow).
- **Skin (integumentary system):** neutrophilic dermatosis; UBERON:0002097 (skin of body).
- **Secondary/occasional — CNS:** developmental/psychomotor delay in some patients ([PMID: 34365623](https://pubmed.ncbi.nlm.nih.gov/34365623/)); UBERON:0001017 (central nervous system).
- **Tissue types affected:** bone/connective tissue, hematopoietic tissue, skin epithelium/dermis, skeletal muscle (peri-osteomyelitic).
- **Cell populations (CL):** macrophages, monocytes, osteoclasts, neutrophils, erythroid precursors (see §6).
- **Subcellular compartments (GO CC):** GO:0072559 (NLRP3 inflammasome complex); GO:0005741 (mitochondrial outer membrane — ROS/mtDNA source); GO:0005886 (plasma membrane — P2X7); lipin-2 localizes to ER membrane/cytosol and nucleus.
- **Lateralization:** Bone lesions are typically **multifocal and often bilateral/symmetric** (characteristic of CRMO), though individual lesions may be asymmetric.

---

## 8. Temporal Development

- **Onset:** Congenital anemia present at/near birth; osteomyelitis and fevers usually manifest in **infancy, before age three** ([PMID: 41113563](https://pubmed.ncbi.nlm.nih.gov/41113563/)). Onset pattern is **chronic with recurrent acute flares**.
- **Progression / course:** **Relapsing–remitting/episodic** bone disease with painful flares; **chronic lifelong** without effective therapy. If untreated, cumulative complications include growth failure, bone deformity/contractures, and transfusion dependence.
- **Disease duration:** Chronic, lifelong.
- **Remission patterns:** Predominantly **treatment-induced remission** on IL-1 blockade, which can be dramatic and sustained ([PMID: 31598604](https://pubmed.ncbi.nlm.nih.gov/31598604/), [PMID: 39255247](https://pubmed.ncbi.nlm.nih.gov/39255247/)). Spontaneous durable remission is not characteristic.
- **Critical periods / window of opportunity:** Early molecular diagnosis and initiation of IL-1 blockade in infancy/early childhood is the key intervention window to prevent cumulative bone damage and growth failure.

---

## 9. Inheritance and Population

- **Inheritance:** **Autosomal recessive** (biallelic LPIN2). Requires two pathogenic alleles.
- **Prevalence / incidence:** No reliable population prevalence; the disease is **ultra-rare**. *"only 31 individuals from 18 families have been reported with this rare condition"* as of 2023 ([PMID: 37865862](https://pubmed.ncbi.nlm.nih.gov/37865862/)); a 2025 review tallied ~35 patients ([PMID: 41113563](https://pubmed.ncbi.nlm.nih.gov/41113563/)).
- **Penetrance / expressivity:** Penetrance of the biallelic genotype appears complete for the autoinflammatory phenotype, but **expressivity is variable**, especially for CDA severity (mild to transfusion-dependent) and presence/absence of the neutrophilic dermatosis ([PMID: 41113563](https://pubmed.ncbi.nlm.nih.gov/41113563/)).
- **Genetic anticipation:** Not applicable (not a repeat-expansion disorder).
- **Founder effects / consanguinity:** Strong association with **consanguinity**; several private/founder-like alleles in Middle Eastern and Indian families. In an Arab pediatric SAID cohort, *"Consanguinity rate among parents was 74.6%"* ([PMID: 31741047](https://pubmed.ncbi.nlm.nih.gov/31741047/)).
- **Carrier frequency:** Not established; expected very low, elevated within consanguineous kindreds.
- **Population demographics:** Reported predominantly in populations with high consanguinity (Arab/Middle Eastern, South Asian/Indian), with additional cases across ancestries including East Asian ([PMID: 34365623](https://pubmed.ncbi.nlm.nih.gov/34365623/)) and the first patient of central-European ancestry ([PMID: 39255247](https://pubmed.ncbi.nlm.nih.gov/39255247/)). No strong sex bias is established given small numbers.

---

## 10. Diagnostics

**Laboratory tests / biomarkers.** Elevated acute-phase reactants (ESR, CRP); microcytic anemia with bone marrow showing **dyserythropoiesis**; occasional neutropenia ([PMID: 31727123](https://pubmed.ncbi.nlm.nih.gov/31727123/)). Elevated caspase-1 activity and IL-1β in patient monocytes are research biomarkers ([PMID: 33314777](https://pubmed.ncbi.nlm.nih.gov/33314777/)). Bone cultures are **negative** (sterile osteomyelitis).

**Imaging.** MRI is the favored modality: multifocal osteomyelitic lesions appear as high-signal (STIR/SPAIR) marrow lesions with surrounding soft-tissue/muscle edema; common sites include tibia, femur, fibula, talar bones and sacroiliac joints ([PMID: 34365623](https://pubmed.ncbi.nlm.nih.gov/34365623/), [PMID: 27860302](https://pubmed.ncbi.nlm.nih.gov/27860302/)).

**Biopsy/pathology.** Bone lesions show sterile chronic inflammation without organisms; marrow aspirate shows dyserythropoietic changes.

**Genetic testing (definitive).** Molecular confirmation is by identifying biallelic pathogenic LPIN2 variants, most efficiently via an **autoinflammatory NGS gene panel that includes LPIN2**, or WES/WGS. Because patients present across specialties, *"Patients with MJS may present initially to different specialists, and thus it is important to create awareness in the medical community"* ([PMID: 33993107](https://pubmed.ncbi.nlm.nih.gov/33993107/)). Single-gene LPIN2 sequencing is appropriate when the phenotype is classic.

**Clinical criteria / differential diagnosis.** No formal consensus diagnostic criteria; diagnosis rests on the clinical triad plus biallelic LPIN2 variants. Key differentials:
- **Non-syndromic CRMO/CNO** — no CDA, no biallelic LPIN2.
- **DIRA (IL1RN deficiency)** — CRMO-like with pustulosis; different gene.
- **Juvenile idiopathic arthritis (JIA)** — frequent misdiagnosis (see below).
- **RETREG1/FAM134B-related disease (HSAN2B)** — can mimic Majeed with recurrent osteomyelitis and microcytic anemia, but LPIN2 sequencing is negative ([PMID: 35332675](https://pubmed.ncbi.nlm.nih.gov/35332675/)).

**Diagnostic delay.** Majeed syndrome is frequently misdiagnosed: *"Its rarity and overlap with juvenile idiopathic arthritis (JIA) often lead to delayed or incorrect diagnoses"* ([PMID: 41113563](https://pubmed.ncbi.nlm.nih.gov/41113563/)). In an Arab SAID cohort the initial diagnosis was inaccurate in 49.3% with a median time-to-diagnosis of 2.5 years ([PMID: 31741047](https://pubmed.ncbi.nlm.nih.gov/31741047/)).

**Screening.** Cascade genetic testing and carrier testing within affected families; prenatal/preimplantation diagnosis is feasible once the family's biallelic variants are known.

---

## 11. Outcome / Prognosis

- **Survival / mortality:** No formal survival statistics; the disease is generally not directly life-limiting when the inflammation is controlled, but untreated disease causes substantial morbidity. Severe transfusion-dependent anemia and complications contribute to burden.
- **Morbidity / disability:** Chronic bone pain, recurrent fevers, growth failure, bone deformity/contractures, and, in severe CDA, transfusion dependence and iron overload. CNS involvement in some cases can cause developmental delay ([PMID: 34365623](https://pubmed.ncbi.nlm.nih.gov/34365623/)).
- **Disease course / recovery:** Chronic lifelong disease with **excellent response to IL-1 blockade**; anakinra produced *"resolution of MRI findings, microcytic anaemia and dyserythropoiesis at bone marrow aspirate"* ([PMID: 39255247](https://pubmed.ncbi.nlm.nih.gov/39255247/)), indicating substantial recovery potential with targeted therapy. Response to TNF inhibitors and corticosteroids is only partial.
- **Prognostic factors:** Time to correct molecular diagnosis and initiation of IL-1 blockade; CDA severity; extent of skeletal involvement. IL-1-pathway responsiveness is the key favorable prognostic determinant.

---

## 12. Treatment

**First-line / most effective — IL-1 blockade.** Across the reported experience, *"IL-1 blockade remains the most effective treatment"* ([PMID: 41113563](https://pubmed.ncbi.nlm.nih.gov/41113563/)).
- **Anakinra** (recombinant IL-1 receptor antagonist; NCIT:C1839): *"Treatment with anakinra was started with a prompt resolution of the clinical picture"* ([PMID: 39255247](https://pubmed.ncbi.nlm.nih.gov/39255247/)); *"We observed a significant clinical response to biologic anti-interleukin-1 (IL-1) therapy in our patients"* ([PMID: 31598604](https://pubmed.ncbi.nlm.nih.gov/31598604/)).
- **Canakinumab** (anti-IL-1β monoclonal antibody; NCIT:C71355): long-lasting remission reported ([PMID: 33314777](https://pubmed.ncbi.nlm.nih.gov/33314777/), [PMID: 27860302](https://pubmed.ncbi.nlm.nih.gov/27860302/)).

**Partially effective / adjunctive.**
| Therapy | Class (NCIT) | Efficacy in Majeed |
|---|---|---|
| Anakinra / canakinumab | IL-1 blockers | **Most effective**; dramatic/sustained remission |
| Corticosteroids | Glucocorticoid (NCIT:C381) | Partial |
| NSAIDs | Anti-inflammatory | Partial/symptomatic |
| Methotrexate | Antimetabolite (NCIT:C642) | Partial/ineffective |
| TNF inhibitors (adalimumab, etanercept, infliximab) | TNF blockers | Partial, variable |
| Bisphosphonates | Bone resorption inhibitor | Adjunctive for bone disease ([PMID: 31377798](https://pubmed.ncbi.nlm.nih.gov/31377798/)) |
| RBC transfusion / supportive | Supportive care | For severe CDA |

**Pharmacogenomics / advanced therapeutics:** None specific. No approved gene, cell, or RNA therapy exists; the strong mechanistic rationale (single-gene recessive LOF) makes LPIN2 an in-principle candidate for future gene-replacement, but no clinical program is reported. **Personalized approach:** genotype-driven — confirming biallelic LPIN2 LOF directs treatment toward IL-1 blockade.

---

## 13. Prevention

- **Primary prevention:** Not preventable in a genetically affected individual. **Genetic counseling** for consanguineous couples and families with an affected child is the principal preventive tool; recurrence risk is 25% per pregnancy for carrier couples.
- **Secondary prevention:** Early molecular diagnosis (autoinflammatory panels including LPIN2) to shorten the ~2.5-year diagnostic delay and enable prompt IL-1 blockade ([PMID: 31741047](https://pubmed.ncbi.nlm.nih.gov/31741047/), [PMID: 33993107](https://pubmed.ncbi.nlm.nih.gov/33993107/)).
- **Tertiary prevention:** Sustained IL-1 blockade to prevent cumulative bone damage, growth failure, and transfusion-related complications; bisphosphonates as bone-protective adjuncts.
- **Genetic screening:** Cascade carrier testing, prenatal diagnosis, and preimplantation genetic testing once familial variants are identified.
- **Behavioral/environmental:** Mechanistically, limiting dietary saturated-fat load could reduce inflammatory amplification ([PMID: 22334674](https://pubmed.ncbi.nlm.nih.gov/22334674/)), but this is not clinically validated.
- **Immunization / public health / prophylaxis:** No vaccine or infectious-prophylaxis relevance (disease is sterile/genetic).

---

## 14. Other Species / Natural Disease

- **Taxonomy:** Human disease (NCBI:txid9606). LPIN2 orthologs exist across mammals; the closely related PAP function is conserved from yeast (*Pah1*) to plants (*Arabidopsis PAH1/2*) and mammals ([PMID: 40680843](https://pubmed.ncbi.nlm.nih.gov/40680843/), [PMID: 41604448](https://pubmed.ncbi.nlm.nih.gov/41604448/)).
- **Orthologous genes:** Mouse *Lpin2* (NCBI Gene 64898). The lipin family (lipin-1/2/3) has partially redundant and distinct roles ([PMID: 27344312](https://pubmed.ncbi.nlm.nih.gov/27344312/)).
- **Natural disease in animals:** No well-characterized naturally occurring LPIN2 Majeed-equivalent in companion animals is documented here; the related sterile osteomyelitis phenotype occurs in the murine *Pstpip2* (*cmo*) model (a different gene), and canine sterile osteomyelitis has been noted in the broader CRMO literature ([PMID: 23917160](https://pubmed.ncbi.nlm.nih.gov/23917160/)).
- **Evolutionary conservation:** The HAD-like catalytic PAP mechanism is deeply conserved; disease-relevant active-site motifs (e.g., DxDxT) are shared from yeast Pah1 to human lipins ([PMID: 40680843](https://pubmed.ncbi.nlm.nih.gov/40680843/), [PMID: 32161260](https://pubmed.ncbi.nlm.nih.gov/32161260/)).
- **Zoonotic potential:** None (non-infectious genetic disease).

---

## 15. Model Organisms

- **Mouse models:** The **cmo (chronic multifocal osteomyelitis)** mouse — driven by *Pstpip2* mutation, not *Lpin2* — is the principal in-vivo model of sterile CRMO and demonstrated that dietary/microbiome manipulation protects against osteomyelitis ([PMID: 28361334](https://pubmed.ncbi.nlm.nih.gov/28361334/)). It recapitulates the sterile bone-inflammation phenotype but not the LPIN2 lesion or the CDA.
- **Cellular models:** **RAW-D murine macrophages** with Lipin2 deficiency show enhanced NF-κB signaling and osteoclast formation, modeling the bone-directed mechanism ([PMID: 33809261](https://pubmed.ncbi.nlm.nih.gov/33809261/)). **Primary human and mouse macrophages/monocytes** (patient-derived and lipin-2-depleted) recapitulate NLRP3/P2X7-driven IL-1β overproduction and the pro-osteoclastogenic secretome ([PMID: 28031477](https://pubmed.ncbi.nlm.nih.gov/28031477/), [PMID: 33314777](https://pubmed.ncbi.nlm.nih.gov/33314777/), [PMID: 22334674](https://pubmed.ncbi.nlm.nih.gov/22334674/)).
- **Structural / biochemical surrogates:** *Tetrahymena* **Pah2** and yeast **Pah1** crystal structures and mutagenesis define the catalytic architecture and the impact of disease-type mutations ([PMID: 32161260](https://pubmed.ncbi.nlm.nih.gov/32161260/), [PMID: 40680843](https://pubmed.ncbi.nlm.nih.gov/40680843/), [PMID: 41109341](https://pubmed.ncbi.nlm.nih.gov/41109341/)).
- **Recapitulation / limitations:** Cellular and *cmo* models capture the **innate-immune/IL-1 and osteoclast** arms well, but **no model faithfully reproduces the congenital dyserythropoietic anemia**, which remains the least-modeled feature. There is no widely used *Lpin2*-knockout mouse that reproduces the full human triad.
- **Resources:** MGI (mouse *Lpin2*), and lipin structural/biochemical literature.

---

## Mechanistic Model / Interpretation

Majeed syndrome is best understood as a **loss-of-brake autoinflammatory disease**: lipin-2 is not itself inflammatory but is a negative regulator that normally keeps the P2X7→NLRP3→IL-1β axis in check while also buffering lipid stress. Removing that brake (biallelic LOF) yields chronic IL-1β excess that fans out into tissue-specific manifestations — bone (via a pro-osteoclastogenic macrophage program and NF-κB), skin (neutrophilic dermatosis), and systemic (fever, growth failure). The therapeutic logic follows directly: because IL-1β is the convergent downstream effector, **IL-1 blockade collapses the entire phenotype**, and its efficacy is itself strong in-vivo confirmation of the model. This is why the disease has been formally reclassified as an NLRP3 inflammasomopathy: *"LIPIN2 deficiency can activate the NLRP3 inflammasome through alterations in the function of P2X7 receptor providing evidence that Majeed syndrome is an NLRP3 inflammasomopathy"* ([PMID: 29912021](https://pubmed.ncbi.nlm.nih.gov/29912021/)).

Two features refine this picture. First, the **environmental modifier axis** (saturated fatty acids via JNK1/c-Jun; microbiome/diet in the murine model) shows the disease is a gene-by-environment product, not a purely fixed genotype effect — offering non-pharmacologic levers. Second, the **anemia sits outside the well-mapped chain**: it is described phenotypically as congenital, microcytic and dyserythropoietic, yet no pathway from lipin-2 loss to erythroid maturation failure has been demonstrated. Its reversibility with anakinra reframes it as at least partly an **inflammation-driven (IL-1-mediated) anemia** rather than a fixed cell-intrinsic erythroid defect — a hypothesis that would reconcile it with the rest of the mechanism.

---

## Evidence Base

| PMID | Contribution | Evidence type |
|---|---|---|
| [15994876](https://pubmed.ncbi.nlm.nih.gov/15994876/) | Identifies LPIN2 as causal gene via homozygosity mapping (chr 18p) | Human genetics |
| [33670882](https://pubmed.ncbi.nlm.nih.gov/33670882/) | Defines clinical triad; clinical/genetic/immunologic review | Human clinical review |
| [41113563](https://pubmed.ncbi.nlm.nih.gov/41113563/) | 35-patient review: onset <3 y, variable CDA, IL-1 blockade most effective, JIA misdiagnosis | Human clinical review |
| [28031477](https://pubmed.ncbi.nlm.nih.gov/28031477/) | Lipin-2 restrains NLRP3 via P2X7/MAPK | In vitro (human+mouse macrophages) |
| [29912021](https://pubmed.ncbi.nlm.nih.gov/29912021/) | Classifies Majeed as an NLRP3 inflammasomopathy | Review/synthesis |
| [33314777](https://pubmed.ncbi.nlm.nih.gov/33314777/) | Pro-osteoclastogenic M2 macrophages; canakinumab remission | In vitro + human clinical |
| [33809261](https://pubmed.ncbi.nlm.nih.gov/33809261/) | Lipin2 loss → NF-κB and osteoclast formation | In vitro (RAW-D) |
| [22334674](https://pubmed.ncbi.nlm.nih.gov/22334674/) | SFA amplify inflammation via JNK1/c-Jun in lipin-2 deficiency | In vitro |
| [37929625](https://pubmed.ncbi.nlm.nih.gov/37929625/) | Lipin-2 limits TLR3/ROS/mtDNA → NLRP3; IFN-regulated | In vitro |
| [39255247](https://pubmed.ncbi.nlm.nih.gov/39255247/) | Anakinra resolves MRI, anemia and marrow dyserythropoiesis | Human clinical case |
| [31598604](https://pubmed.ncbi.nlm.nih.gov/31598604/) | Anti-IL-1 response in familial cases | Human clinical |
| [31741047](https://pubmed.ncbi.nlm.nih.gov/31741047/) | Consanguinity 74.6%; diagnostic delay | Human epidemiology |
| [37865862](https://pubmed.ncbi.nlm.nih.gov/37865862/) | ~31 individuals/18 families reported | Human clinical review |
| [32161260](https://pubmed.ncbi.nlm.nih.gov/32161260/) | Structural basis: disease mutations disrupt catalysis or fold | Structural biology |
| [33993107](https://pubmed.ncbi.nlm.nih.gov/33993107/) | Multi-specialty presentation; awareness/panel testing | Human clinical |
| [28361334](https://pubmed.ncbi.nlm.nih.gov/28361334/) | Diet/microbiome modulates sterile osteomyelitis in cmo mouse | Model organism |
| [31377798](https://pubmed.ncbi.nlm.nih.gov/31377798/) | Bisphosphonate + anakinra novel-mutation case | Human clinical |
| [35332675](https://pubmed.ncbi.nlm.nih.gov/35332675/) | RETREG1/HSAN2B mimic (LPIN2-negative) — differential dx | Human genetics |

---

## Limitations and Knowledge Gaps

1. **Unexplained anemia mechanism (primary gap).** No primary study mechanistically links lipin-2 loss to dyserythropoiesis. The anemia is characterized only phenotypically (congenital, microcytic, dyserythropoietic, variable severity). Its reversibility with IL-1 blockade ([PMID: 39255247](https://pubmed.ncbi.nlm.nih.gov/39255247/)) implicates inflammation, but a cell-intrinsic erythroid contribution has not been excluded.
2. **Ultra-small sample size.** All clinical conclusions rest on ~31–35 patients in case reports/series; no controlled trials, no reliable prevalence/incidence, penetrance, or sex-ratio estimates.
3. **No faithful whole-animal LPIN2 model.** In-vivo mechanistic work leans on the *Pstpip2* cmo mouse (different gene) and cellular systems; the human triad, especially CDA, is not fully recapitulated.
4. **Modifier genes / genotype–phenotype correlation** are not established despite clear variable expressivity of CDA and dermatosis.
5. **Environmental modifiers** (saturated fat, microbiome) are mechanistically supported but not clinically tested in patients.

---

## Proposed Follow-up Experiments / Actions

1. **Dissect the anemia:** Generate lipin-2-deficient erythroid models (patient-derived iPSC → erythroid differentiation; conditional Lpin2 knockout in erythroid lineage) and test whether dyserythropoiesis is cell-intrinsic vs. IL-1/inflammation-driven, including IL-1β rescue experiments.
2. **Build a faithful mouse model:** Create and characterize a constitutive/conditional *Lpin2* LOF mouse to test recapitulation of CRMO + CDA + dermatosis and to serve as a preclinical therapeutic platform.
3. **Genotype–phenotype registry:** Establish an international Majeed registry to correlate specific LPIN2 variant classes (catalysis-disrupting vs. fold-destabilizing) with CDA severity and treatment response.
4. **Prospective IL-1 blockade study:** Standardized outcome capture (bone MRI, hemoglobin/transfusion needs, growth, PROMIS) for anakinra vs. canakinumab, including effect on marrow dyserythropoiesis.
5. **Test dietary modifier clinically:** Pilot evaluation of saturated-fat reduction as an adjunct, given the JNK1/c-Jun amplification data.
6. **Diagnostic uplift:** Ensure LPIN2 is on all autoinflammatory/CRMO NGS panels and disseminate awareness to rheumatology, hematology and neurology to shorten the ~2.5-year diagnostic delay.

---

*Evidence source legend:* Human genetics/clinical (case reports, series, reviews, cohorts); in vitro (primary human/mouse macrophages, RAW-D, patient monocytes); model organism (cmo mouse); structural biology (lipin/Pah crystallography). No large-scale omics dataset specific to Majeed syndrome was available for primary analysis; conclusions synthesize published primary literature.


## Artifacts

- [OpenScientist final report](Majeed_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Majeed_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:15994876
2. PMID:33670882
3. PMID:28031477
4. PMID:29912021
5. PMID:33314777
6. PMID:33809261
7. PMID:41113563
8. PMID:39255247
9. PMID:37865862
10. PMID:31741047
11. PMID:22334674
12. PMID:28361334
13. PMID:34365623
14. PMID:31727123
15. PMID:27860302
16. PMID:33993107
17. PMID:32161260
18. PMID:37929625
19. PMID:31598604
20. PMID:35332675
21. PMID:31377798
22. PMID:40680843
23. PMID:41604448
24. PMID:27344312
25. PMID:23917160
26. PMID:41109341