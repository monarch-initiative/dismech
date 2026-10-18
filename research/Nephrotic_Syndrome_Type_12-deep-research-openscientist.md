---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-17T00:52:08.100424'
end_time: '2026-10-17T01:16:07.342917'
duration_seconds: 1439.24
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Nephrotic Syndrome Type 12
  mondo_id: MONDO:0014817
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
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderAuthError
  status_code: 403
  remedy: the API key is missing, invalid, or lacks access to this endpoint
  retryable: false
- provider: openscientist
  succeeded: true
citation_count: 14
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Nephrotic_Syndrome_Type_12-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Nephrotic_Syndrome_Type_12-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Nephrotic Syndrome Type 12
- **MONDO ID:** MONDO:0014817 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Nephrotic Syndrome Type 12** covering all of the
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

# Nephrotic Syndrome Type 12 (NPHS12): A Comprehensive Disease Characterization

**Disease:** Nephrotic Syndrome Type 12 (NPHS12)
**MONDO ID:** MONDO:0014817 · **OMIM:** #616892 · **Causal gene:** *NUP93*
**Category:** Mendelian (autosomal recessive)
**Report date:** 2026-10-17

---

## Summary

**Nephrotic Syndrome Type 12 (NPHS12; MONDO:0014817, OMIM #616892) is an autosomal-recessive, steroid-resistant, kidney-limited podocytopathy caused by biallelic hypomorphic variants in *NUP93***, a gene encoding a central scaffold protein of the inner ring of the nuclear pore complex (NPC). It is one of a growing family of "nucleoporinopathies" — monogenic steroid-resistant nephrotic syndromes (SRNS) caused by mutations in genes encoding NPC subunits (*NUP93, NUP205, NUP107, NUP133, NUP160, NUP85, XPO5*). Clinically, NPHS12 presents in early childhood with proteinuria progressing to the full nephrotic syndrome, resists corticosteroids and other immunosuppressants, shows focal segmental glomerulosclerosis (FSGS) on biopsy, and progresses rapidly to kidney failure.

**A critical correction established during this investigation:** The MONDO term MONDO:0014817 "nephrotic syndrome, type 12" maps specifically to OMIM:616892 and the *NUP93*-associated disease. The gene *NUP107* — which is superficially similar and causes a closely related nucleoporin SRNS — is responsible for the **distinct** entity NPHS11 (OMIM 616730), not NPHS12. Early iterations of this investigation incorrectly assigned NPHS12 to *NUP107*; ontology verification against EBI OLS4 corrected the gene assignment to *NUP93*. Both genes remain biologically and clinically adjacent (both NPC nucleoporinopathies causing childhood SRNS/FSGS), and much of the shared mechanistic and management narrative applies to both, but the identifiers, onset profile, and molecular partners differ. *NUP93* encodes an **inner-ring** NPC scaffold protein; *NUP107* encodes an **outer-ring (Y-complex)** component.

**Mechanistically**, mutant NUP93 disrupts nuclear-pore assembly and the NUP93–NUP205 inner-ring interaction. This impairs the NPC-dependent nucleocytoplasmic transport of key podocyte signaling effectors, including SMAD proteins downstream of BMP7 signaling, and (as shown across the nucleoporin-SRNS family) dysregulates CDC42 and the Hippo-pathway effectors YAP/TAZ. The net result is podocyte injury — foot-process effacement, loss of the glomerular filtration barrier, massive proteinuria, and FSGS. NUP93-SRNS is the most aggressive nucleoporin subtype, with a median age at onset of ~3 years and a median time to kidney failure of ~3.7 years. Because the disease is an intrinsic genetic podocytopathy rather than a circulating-factor-mediated disorder, post-transplant recurrence is rare.

---

## 1. Disease Information

**Overview.** Nephrotic Syndrome Type 12 is a Mendelian, autosomal-recessive form of steroid-resistant nephrotic syndrome. It belongs to the hereditary podocytopathies and, more specifically, to the subgroup of **nucleoporin-associated SRNS**. Affected children develop heavy proteinuria, hypoalbuminemia, and edema that does not respond to corticosteroid therapy; kidney biopsy typically shows focal segmental glomerulosclerosis (FSGS) with podocyte foot-process effacement. The disease is kidney-limited (non-syndromic) in its classic form.

**Key identifiers.**

| Resource | Identifier |
|---|---|
| MONDO | MONDO:0014817 ("nephrotic syndrome, type 12") |
| OMIM (phenotype) | #616892 |
| Causal gene | *NUP93* (OMIM *614351) |
| HGNC | HGNC:28958 |
| UniProt | Q8N1F7 (NUP93_HUMAN) |
| Cytoband | 16q13 |
| Disease synonym | "NUP93 familial nephrotic syndrome" |

**Synonyms / alternative names.** NPHS12; NUP93-associated steroid-resistant nephrotic syndrome; NUP93 familial nephrotic syndrome; nucleoporin-93 nephrotic syndrome. Within the broader clinical literature it is classified under hereditary/genetic SRNS and FSGS.

**Important disambiguation.** MONDO:0014817 / OMIM 616892 = **NPHS12 = *NUP93***. The adjacent entity NPHS11 (OMIM 616730) = ***NUP107***. These should not be conflated despite shared biology (see Finding F008).

**Data provenance.** Information in this report is derived from **aggregated, disease-level resources** (OMIM, MONDO, UniProt, gnomAD, ClinVar) and from **primary clinical literature** describing individual patient cohorts (whole-exome/whole-genome sequencing case series). No single EHR-derived patient dataset underlies this report; the evidence is literature- and database-aggregated.

---

## 2. Etiology

**Primary cause — genetic.** NPHS12 is caused by **biallelic (homozygous or compound heterozygous) pathogenic variants in *NUP93***. Braun et al. (2016) established *NUP93* — together with its interaction partner *NUP205* and *XPO5* (exportin-5) — as a hitherto unrecognized monogenic cause of SRNS in eight families:

> "we identify in eight families with SRNS mutations in NUP93, its interaction partner NUP205 or XPO5 (encoding exportin 5) as hitherto unrecognized monogenic causes of SRNS" — [PMID: 26878725](https://pubmed.ncbi.nlm.nih.gov/26878725/)

**Genetic risk factors.** The disease requires two deleterious *NUP93* alleles. There are no established common susceptibility loci or modifier-gene associations specific to NPHS12. The principal "risk factor" for an affected child is therefore carrier status of both parents. **Consanguinity** substantially increases risk because it raises the probability of homozygosity for a rare recessive allele; nucleoporin-SRNS is over-represented in consanguineous cohorts (e.g., Saudi Arabian and Egyptian series — [PMID: 41141495](https://pubmed.ncbi.nlm.nih.gov/41141495/), [PMID: 40402239](https://pubmed.ncbi.nlm.nih.gov/40402239/)).

**Environmental risk factors.** None established. Unlike acquired (idiopathic, immune-mediated) nephrotic syndrome, NPHS12 is a monogenic disorder; environmental exposures, infections, age, and sex are not causal. There is a reported female predominance in small nucleoporin-SRNS case series (see §9), but this is likely a reporting/ascertainment observation rather than a true sex-linked risk.

**Protective factors.** No genetic or environmental protective factors are established. Theoretically, any residual (hypomorphic) NUP93 function preserved by a milder allele would be "protective" in the sense of attenuating severity, consistent with the recessive, hypomorphic disease model.

**Gene–environment interactions.** None documented for NPHS12. The disorder is essentially fully genetically determined; disease expression does not appear to require an environmental trigger.

---

## 3. Phenotypes

NPHS12 presents as classic nephrotic syndrome with the following core phenotypes. Frequencies are drawn from nucleoporin-SRNS cohorts; "variable" indicates limited sample sizes.

| Phenotype | Type | HPO term | Onset | Severity / frequency |
|---|---|---|---|---|
| Steroid-resistant nephrotic syndrome | Clinical/laboratory | HP:0012588 | Early childhood (~3 y for NUP93) | Severe; defining feature (100%) |
| Proteinuria / nephrotic-range proteinuria | Laboratory | HP:0000093 | Early childhood | Severe; near-universal |
| Hypoalbuminemia | Laboratory | HP:0003073 | Concurrent with proteinuria | Moderate–severe |
| Edema | Clinical sign | HP:0000969 | Concurrent | Variable |
| Focal segmental glomerulosclerosis (FSGS) | Histopathology | HP:0000097 | At biopsy | ~89% of nucleoporin-SRNS biopsies |
| Podocyte foot-process effacement | Ultrastructural | HP:0031266 | At biopsy | Characteristic |
| Progression to stage 5 CKD / kidney failure | Clinical | HP:0003774 | Median ~3.7 y after onset (NUP93) | High |

**Phenotype characteristics.**
- **Age of onset:** Early childhood. For *NUP93*-associated SRNS the median age at onset is ~3 years — the earliest and most aggressive among the nucleoporin subtypes:
  > "The median ages at onset of NUP85-, NUP93-, NUP107-, NUP133-, NUP160-, and NUP205-associated SRNS are 7, 3, 4.1, 9, 7, and 2 years, respectively" — [PMID: 39331077](https://pubmed.ncbi.nlm.nih.gov/39331077/)
- **Severity:** Severe and treatment-refractory.
- **Progression:** Progressive, typically reaching kidney failure within a few years of onset. One reported *NUP93* patient developed kidney failure just six months after diagnosis at age 1 year 2 months ([PMID: 39814977](https://pubmed.ncbi.nlm.nih.gov/39814977/)).
- **Frequency among affected individuals:** Proteinuria and steroid resistance are universal; FSGS is seen in ~89% of biopsied nucleoporin-SRNS patients.

**Quality-of-life impact.** Substantial. Progression to dialysis-dependent kidney failure in early childhood imposes major burdens: dialysis or transplantation, growth impairment, chronic medication, dietary restriction, and repeated hospitalization. No NPHS12-specific EQ-5D/SF-36/PROMIS data exist; QoL inference is drawn from the pediatric kidney-failure literature.

**Extrarenal phenotypes.** Classic NPHS12 is kidney-limited. (Note: the *NUP107*/*NUP133* nucleoporinopathies can extend to the syndromic Galloway–Mowat phenotype with microcephaly and brain anomalies — relevant to the adjacent NPHS11, not to kidney-limited NPHS12.)

---

## 4. Genetic / Molecular Information

**Causal gene.** ***NUP93*** (nucleoporin 93 kDa).

| Attribute | Value |
|---|---|
| Gene symbol | *NUP93* |
| HGNC | HGNC:28958 |
| OMIM (gene) | *614351 |
| UniProt | Q8N1F7 |
| Cytoband | 16q13 |
| Protein | Nucleoporin NUP93, a scaffold component of the NPC inner ring |
| RefSeq transcript | NM_014669.5 |

**Population constraint (gnomAD).** *NUP93* shows strong loss-of-function (LoF) constraint at the gene level — **LoF Z = 4.32, LOEUF = 0.639** — indicating depletion of LoF variants in the general population, yet **pLI ≈ 0**, consistent with a gene that is intolerant of complete LoF but causes disease through a **recessive, hypomorphic mechanism** (two partial-loss alleles required). This constraint profile fits a dosage-sensitive scaffold protein essential for NPC assembly.

**Pathogenic variants.** ClinVar lists ~380 *NUP93* variants (NM_014669.5), of which ~53 are classified pathogenic/likely pathogenic. Reported disease variants are predominantly **missense** affecting protein stability and the NUP93–NUP205 interaction, with additional splice and truncating alleles:
- Missense examples c.1655A>G and c.1604A>C were shown to disrupt NUP93 protein stability by immunohistochemistry of kidney biopsy, with ultrastructural "severe vacuolization and deformed nucleus in podocytes, torn and dissolved glomerular basement membrane, and diffuse foot process effacement" — [PMID: 39814977](https://pubmed.ncbi.nlm.nih.gov/39814977/).

**Variant classification.** Per ACMG/AMP criteria, disease alleles are classified pathogenic or likely pathogenic; many novel variants reported in consanguineous cohorts are supported by segregation and functional/in-silico evidence ([PMID: 38650033](https://pubmed.ncbi.nlm.nih.gov/38650033/), [PMID: 40402239](https://pubmed.ncbi.nlm.nih.gov/40402239/)).

**Allele frequency.** Pathogenic *NUP93* alleles are individually rare (consistent with strong LoF constraint); gnomAD shows depletion of LoF variants. No common high-frequency pathogenic allele is established, though founder alleles may exist in consanguineous populations.

**Somatic vs germline.** **Germline** exclusively. No somatic/cancer role.

**Functional consequence.** **Loss of function / hypomorphic**, acting through impaired NPC assembly and disrupted NUP93–NUP205 inner-ring scaffolding; dominant-negative mechanisms are not established.

**Modifier genes.** None validated specific to NPHS12. The broader nucleoporin network (*NUP205*, *XPO5*) is mechanistically linked but represents separate causal loci rather than modifiers.

**Epigenetics / chromosomal abnormalities.** No disease-specific DNA-methylation or histone signatures reported. NPHS12 is a single-gene disorder; large-scale chromosomal abnormalities are not a typical cause, though rare copy-number events affecting the locus are theoretically possible.

---

## 5. Environmental Information

NPHS12 has **no established environmental, lifestyle, or infectious contributors**. It is a monogenic, fully genetically determined podocytopathy. Toxin exposure, pollution, occupational exposures, smoking, diet, alcohol, and infectious agents are **not applicable** as causes. (Environmental and immune factors dominate *acquired*/idiopathic nephrotic syndrome, which is a distinct differential diagnosis — see §10.)

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **Biallelic hypomorphic *NUP93* variants** (germline) **lead to** reduced/destabilized NUP93 scaffold protein in podocytes.
2. Destabilized NUP93 **impairs** the NUP93–NUP205 inner-ring interaction and **disrupts** proper nuclear pore complex (NPC) assembly in the nuclear envelope (demonstrated via protein-stability and ultrastructural studies).
3. Defective NPCs **result in** abnormal nucleocytoplasmic transport of signaling effectors in podocytes. *(Branch point.)*
   - **Branch A — SMAD/BMP7 axis (inferred for NUP93 from the Braun 2016 framework):** impaired nuclear import of SMAD proteins **abrogates** BMP7-induced SMAD signaling required for podocyte homeostasis.
   - **Branch B — CDC42 dysregulation (demonstrated across nucleoporin family):** loss of outer-ring/scaffold nucleoporins **dysregulates** CDC42, an effector of SRNS pathogenesis ([PMID: 30179222](https://pubmed.ncbi.nlm.nih.gov/30179222/); *NUP160* mouse model [PMID: 40298220](https://pubmed.ncbi.nlm.nih.gov/40298220/)).
   - **Branch C — Hippo/YAP-TAZ axis (demonstrated for NUP205/NUP107):** impaired NUP-dependent nuclear import **dysregulates** YAP/TAZ transcriptional activity critical for maintaining the glomerular filter ([PMID: 37565816](https://pubmed.ncbi.nlm.nih.gov/37565816/)).
4. Converging signaling dysregulation **leads to** podocyte injury — cytoskeletal disruption and cellular stress (vacuolization, deformed nuclei, extended/dilated ER observed ultrastructurally).
5. Podocyte injury **results in** **foot-process effacement** and breakdown of the slit-diaphragm/glomerular filtration barrier.
6. Loss of filtration-barrier integrity **causes** massive **proteinuria → hypoalbuminemia → edema** (clinical nephrotic syndrome), which is **steroid-resistant** because the defect is intrinsic/structural rather than immune-mediated.
7. Ongoing podocyte loss **leads to** **focal segmental glomerulosclerosis (FSGS)** and progressive nephron dropout.
8. Progressive glomerulosclerosis **results in** chronic kidney disease and **end-stage kidney failure** (median ~3.7 y after onset for NUP93).

### Mechanistic detail by category

- **Molecular pathways:** BMP7–SMAD signaling (nuclear import of SMADs); CDC42 (Rho-family GTPase) signaling; Hippo pathway effectors YAP/TAZ. All converge on podocyte cytoskeletal and transcriptional homeostasis.
- **Cellular processes:** Nuclear pore complex assembly (GO:0051292); nucleocytoplasmic transport (GO:0006913); protein import into nucleus (GO:0006606); podocyte injury and apoptosis.
- **Protein dysfunction:** Loss-of-function/destabilization of the NUP93 scaffold; impaired NUP93–NUP205 binding; faulty NPC architecture. Ultrastructurally, mutant NUP93 produces "severe vacuolization and deformed nucleus in podocytes" ([PMID: 39814977](https://pubmed.ncbi.nlm.nih.gov/39814977/)).
- **Immune involvement:** None primary — distinguishes NPHS12 from immune-mediated nephrotic syndrome and explains immunosuppressant resistance.
- **Tissue damage mechanisms:** Podocyte depletion → glomerular basement membrane disruption → segmental sclerosis/fibrosis.
- **Molecular profiling:** Single-cell transcriptomic/proteomic work in the related *Nup160*-knockout podocyte model shows decreased CDC42 protein with reduced CDC42 activity despite normal/elevated transcript — illustrating a post-transcriptional mechanism ([PMID: 40298220](https://pubmed.ncbi.nlm.nih.gov/40298220/)).

### Ontology suggestions
- **GO biological process:** nuclear pore complex assembly (GO:0051292), nucleocytoplasmic transport (GO:0006913), protein import into nucleus (GO:0006606), nephron development (GO:0072006).
- **GO cellular component:** nuclear pore (GO:0005643), nuclear envelope (GO:0005635), nuclear pore inner ring.
- **CL cell type:** podocyte / glomerular visceral epithelial cell (CL:0000653).
- **UBERON anatomy:** renal glomerulus (UBERON:0000074), kidney (UBERON:0002113).

---

## 7. Anatomical Structures Affected

**Organ level.** Primary organ: **kidney** (UBERON:0002113), specifically the **renal glomerulus** (UBERON:0000074). Secondary/systemic consequences of nephrotic syndrome include edema, hyperlipidemia, thromboembolic risk, and infection susceptibility; end-stage disease affects the whole organism through uremia. Body system: **urinary/renal system**.

**Tissue and cell level.** The target cell is the **podocyte** (glomerular visceral epithelial cell, CL:0000653) — a specialized epithelial cell forming the filtration barrier. The glomerular basement membrane and slit diaphragm are secondarily disrupted. Although NUP93 is ubiquitously expressed, the clinical phenotype is podocyte-predominant, reflecting the podocyte's unique vulnerability to NPC/transport dysfunction.

**Subcellular level.** The **nuclear envelope** (GO:0005635) and **nuclear pore complex** (GO:0005643) are the primary subcellular targets. Secondary ultrastructural abnormalities include deformed nuclei, cytoplasmic vacuolization, and extended/dilated endoplasmic reticulum in podocytes ([PMID: 39814977](https://pubmed.ncbi.nlm.nih.gov/39814977/)).

**Localization / lateralization.** Bilateral and diffuse (both kidneys); glomerular involvement is focal and segmental at the histologic level (FSGS pattern) but systemic across the glomerular population.

---

## 8. Temporal Development

**Onset.** Early-childhood onset; insidious to subacute presentation with proteinuria/edema. For *NUP93* specifically, median age at onset ≈ **3 years** ([PMID: 39331077](https://pubmed.ncbi.nlm.nih.gov/39331077/)).

**Progression.** Progressive and typically rapid. NUP93-SRNS is the **most aggressive** nucleoporin subtype, with a **median time to kidney failure of ~3.7 years** from onset. Disease stages run from early proteinuria → nephrotic syndrome → CKD stages → end-stage kidney failure. One case progressed to kidney failure within six months of diagnosis ([PMID: 39814977](https://pubmed.ncbi.nlm.nih.gov/39814977/)).

**Course and duration.** Chronic, lifelong; relentlessly progressive without spontaneous remission. Because the disease is intrinsic, immunosuppression-induced remission is unexpected.

**Critical periods.** The key intervention window is at/near diagnosis — early genetic diagnosis prevents futile immunosuppression and guides transplant planning. There is no known "protective" developmental window.

---

## 9. Inheritance and Population

**Inheritance.** **Autosomal recessive** (biallelic, homozygous or compound heterozygous) — [PMID: 26878725](https://pubmed.ncbi.nlm.nih.gov/26878725/).

**Penetrance / expressivity.** Penetrance appears high in biallelic carriers; expressivity is variable with respect to age at kidney failure, likely reflecting allele severity (hypomorphic spectrum).

**Consanguinity and founder effects.** Consanguinity is a major contributing factor, enriching nucleoporin-SRNS in Middle Eastern, North African, and South/East Asian cohorts (Saudi [PMID: 41141495](https://pubmed.ncbi.nlm.nih.gov/41141495/); Egyptian [PMID: 40402239](https://pubmed.ncbi.nlm.nih.gov/40402239/); Chinese [PMID: 38650033](https://pubmed.ncbi.nlm.nih.gov/38650033/)). Population-specific founder alleles plausibly exist but are not catalogued as a single dominant allele.

**Carrier frequency.** Not precisely established; expected to be low given strong LoF constraint and rarity of pathogenic alleles in gnomAD.

**Epidemiology.** NPHS12 is **ultra-rare**. Nucleoporin variants are described as "extremely rare" causes of hereditary SRNS ([PMID: 38650033](https://pubmed.ncbi.nlm.nih.gov/38650033/)). No reliable prevalence/incidence figures per 100,000 exist; cases are reported as individual families or small series. Within monogenic SRNS cohorts, nucleoporin genes collectively account for a small minority of diagnoses, and *NUP93* is one member of that minority.

**Sex ratio.** Small case series note a **female predominance** (e.g., all four nucleoporin-SRNS patients in [PMID: 38650033](https://pubmed.ncbi.nlm.nih.gov/38650033/) were female), but numbers are too small to establish a true skewed sex ratio; recessive inheritance predicts equal sex distribution.

**Age distribution.** Affected individuals are predominantly young children (onset ~3 y; kidney failure often in childhood).

---

## 10. Diagnostics

**Clinical/laboratory tests.**
- **Urinalysis:** nephrotic-range proteinuria (HP:0000093); urine protein/creatinine ratio.
- **Serum:** hypoalbuminemia (HP:0003073), hyperlipidemia; renal function (creatinine, eGFR) to stage CKD.
- **Biopsy/histopathology:** FSGS on light microscopy; **electron microscopy** shows diffuse podocyte **foot-process effacement**, and in NUP93 disease, podocyte vacuolization, deformed nuclei, GBM disruption, and dilated ER ([PMID: 39814977](https://pubmed.ncbi.nlm.nih.gov/39814977/)). Immunohistochemistry can show reduced/destabilized NUP93 protein.

**Genetic testing (the definitive diagnostic).**
- **Recommended approach:** Next-generation sequencing using a **targeted SRNS/podocytopathy gene panel** that includes *NUP93* and other nucleoporin genes — "Next-generation sequencing using a targeted gene panel is recommended" ([PMID: 39331077](https://pubmed.ncbi.nlm.nih.gov/39331077/)).
- **WES/WGS:** High-yield in early-onset SRNS. Whole-genome sequencing identified a monogenic cause in 56.1% of early-onset SRNS families, including *NUP93* among causal genes ([PMID: 40402239](https://pubmed.ncbi.nlm.nih.gov/40402239/)); exome sequencing yields 40–45% in consanguineous/pediatric kidney-failure cohorts ([PMID: 41141495](https://pubmed.ncbi.nlm.nih.gov/41141495/), [PMID: 37850020](https://pubmed.ncbi.nlm.nih.gov/37850020/)).
- **Confirmatory:** Sanger sequencing with family segregation; minigene/cDNA assays for splice variants.

**Clinical criteria.** Diagnosis of SRNS requires nephrotic syndrome with failure to achieve remission after an adequate corticosteroid course; the genetic diagnosis is established by identifying biallelic pathogenic *NUP93* variants.

**Differential diagnosis.** Other genetic SRNS/FSGS causes must be distinguished — *NPHS1*, *NPHS2*, *WT1*, *PLCE1*, *LAMB2*, *PAX2* ([PMID: 31001663](https://pubmed.ncbi.nlm.nih.gov/31001663/)), *COL4A3-5* ([PMID: 36847718](https://pubmed.ncbi.nlm.nih.gov/36847718/)), *SMARCAL1*, and other nucleoporins (*NUP107/NPHS11*, *NUP205*, *NUP160*, *NUP85*, *NUP133*). Immune-mediated/idiopathic steroid-sensitive nephrotic syndrome and secondary FSGS are also differentials; genetic testing resolves these and avoids unnecessary immunosuppression.

**Screening.** Cascade carrier testing of relatives and genetic counseling are appropriate once a familial variant is known; prenatal/preimplantation testing is feasible for known biallelic variants.

---

## 11. Outcome / Prognosis

**Renal prognosis — poor.** NPHS12 progresses to kidney failure, typically in childhood. NUP93-SRNS has the shortest median time to kidney failure among nucleoporin subtypes (~3.7 years), and is described as rapidly progressive to ESKD ([PMID: 39331077](https://pubmed.ncbi.nlm.nih.gov/39331077/), [PMID: 38650033](https://pubmed.ncbi.nlm.nih.gov/38650033/)).

**Mortality/survival.** No disease-specific survival statistics; prognosis is dominated by kidney failure and is favorable for survival with renal replacement therapy (dialysis/transplant). The disease is kidney-limited, so extrarenal mortality drivers are absent (unlike syndromic nucleoporinopathies).

**Morbidity/QoL.** High morbidity from childhood kidney failure: dialysis dependence, transplant, growth and developmental impact, and chronic immunosuppression burden post-transplant.

**Complications.** Nephrotic-syndrome complications (infection, thromboembolism, hyperlipidemia, malnutrition) plus CKD/ESKD complications.

**Transplant outcome — favorable with low recurrence.** Because NPHS12 is an intrinsic genetic podocytopathy (not circulating-factor-mediated), **post-transplant recurrence is rare**. A critical re-analysis found only one plausible biallelic *NUP93* recurrence case; overall "post-transplantation recurrence remains very rare in patients with genetic SRNS" ([PMID: 34031708](https://pubmed.ncbi.nlm.nih.gov/34031708/)). Reported recurrence for nucleoporin-SRNS is ~12.5%, essentially limited to NUP93.

**Prognostic factors.** Earlier onset and more deleterious (truncating/strongly destabilizing) alleles predict faster progression. Genotype (NUP93 among the most aggressive nucleoporin subtypes) is itself prognostic.

---

## 12. Treatment

**No curative or disease-specific therapy exists.** Management is supportive and focused on renal replacement.

**Pharmacotherapy.**
- **Corticosteroids and immunosuppressants are ineffective** — the disease is steroid-resistant by definition, and "Most affected individuals are resistant to immunosuppressants" ([PMID: 39331077](https://pubmed.ncbi.nlm.nih.gov/39331077/)). Establishing a genetic diagnosis is important precisely to **avoid** futile, toxic immunosuppression.
- **RAAS blockade** (ACE inhibitors / ARBs) is used as **antiproteinuric/nephroprotective** supportive therapy, as in other genetic podocytopathies; partial/complete remission on RAAS antagonists has been reported in a minority of monogenic proteinuria patients generally ([PMID: 36847718](https://pubmed.ncbi.nlm.nih.gov/36847718/)) (NCIT: angiotensin-converting enzyme inhibitor therapy).
- **Supportive care:** diuretics for edema, lipid management, anticoagulation prophylaxis where indicated, nutrition, infection prevention.

**Renal replacement therapy.**
- **Dialysis** at end-stage kidney failure (NCIT: dialysis).
- **Kidney transplantation** — treatment of choice for ESKD in genetic SRNS, with generally good graft outcomes and low recurrence risk ([PMID: 34031708](https://pubmed.ncbi.nlm.nih.gov/34031708/)) (NCIT: kidney transplantation).

**Advanced/experimental therapeutics.** No approved gene, cell, or RNA therapies for NPHS12. Mechanistic insights (CDC42, YAP/TAZ, SMAD/BMP7 axes) suggest future targeted strategies but none are clinically validated.

**Pharmacogenomics.** Not applicable/established.

---

## 13. Prevention

**Primary prevention** of this monogenic disorder is limited to **reproductive genetic counseling**: carrier screening of at-risk families (especially consanguineous couples), prenatal diagnosis, and preimplantation genetic testing once a familial biallelic *NUP93* variant is identified. There is no vaccine, lifestyle, or environmental prevention because the disease is not environmentally triggered.

**Secondary prevention** — early genetic diagnosis via NGS panels enables prompt, appropriate management: avoiding ineffective immunosuppression, initiating nephroprotection (RAAS blockade), and planning transplantation. Genetic diagnosis "is crucial to inform clinical decision making, genetic counseling, transplantation strategy and prenatal diagnosis" ([PMID: 40402239](https://pubmed.ncbi.nlm.nih.gov/40402239/)).

**Tertiary prevention** — CKD complication management, nutrition, infection and thrombosis prophylaxis in the nephrotic state, and optimization of transplant outcomes.

**Counseling.** Autosomal-recessive recurrence risk of 25% per pregnancy for carrier couples; cascade testing of relatives is recommended.

---

## 14. Other Species / Natural Disease

**Taxonomy / orthologs.** *NUP93* is evolutionarily conserved with clear orthologs in mouse (*Nup93*), rat, zebrafish, and other vertebrates (NPC subunits are deeply conserved from yeast to human). No naturally occurring companion-animal or wildlife disease specifically attributed to *NUP93* nephrotic syndrome is catalogued in OMIA at this time.

**Comparative biology.** The podocyte filtration barrier and NPC biology are conserved across vertebrates, making model-organism findings translatable. Within the nucleoporin-SRNS family, zebrafish and Xenopus morphant/knockdown studies of related nucleoporins (*nup107*, *nup133*) reproduce glomerular/podocyte defects ([PMID: 30427554](https://pubmed.ncbi.nlm.nih.gov/30427554/), [PMID: 30179222](https://pubmed.ncbi.nlm.nih.gov/30179222/)), demonstrating conserved disease mechanisms.

**Zoonotic potential.** None — not an infectious disease.

---

## 15. Model Organisms

**Direct *Nup93* models.** A dedicated *Nup93* podocyte-specific mouse recapitulating NPHS12 was not identified in this investigation; however, the nucleoporin-SRNS family is well-modeled and the mechanisms are shared.

**Family-level models (mechanistically informative for NPHS12).**
- **Mouse:** A **podocyte-specific *Nup160* knockout mouse** (CRISPR/Cas9 + Cre/loxP) develops progressive proteinuria and podocyte foot-process effacement — faithfully recapitulating the human nephrotic phenotype — and demonstrates CDC42 protein/activity dysregulation via single-cell transcriptomics and proteomics ([PMID: 40298220](https://pubmed.ncbi.nlm.nih.gov/40298220/)). This is the strongest in-vivo demonstration of the nucleoporin → CDC42 → podocyte-injury mechanism.
- **In-vitro podocytes:** CRISPR/Cas9 knockout of *NUP107/NUP85/NUP133* in immortalized human podocytes activates CDC42 ([PMID: 30179222](https://pubmed.ncbi.nlm.nih.gov/30179222/)); interactome studies in podocytes link *NUP107/133/205/XPO5* to YAP/TAZ regulation ([PMID: 37565816](https://pubmed.ncbi.nlm.nih.gov/37565816/)).
- **Zebrafish/Xenopus:** Morpholino knockdown of *nup107* and *nup133* produces hypoplastic glomeruli and podocyte foot-process fusion, rescuable by wild-type but not mutant human mRNA — establishing causality ([PMID: 30427554](https://pubmed.ncbi.nlm.nih.gov/30427554/)).

**Phenotype recapitulation.** These models reproduce the core human phenotype (proteinuria, foot-process effacement, glomerular injury) and the molecular mechanism (CDC42/YAP-TAZ dysregulation downstream of NPC disruption). **Limitation:** they target *paralogous* nucleoporins rather than *NUP93* itself, and the kidney-limited human phenotype may not be fully captured where models cause broader developmental defects.

**Resources.** MGI (mouse *Nup93*), ZFIN (zebrafish *nup* genes), Alliance of Genome Resources for orthology; immortalized human podocyte lines and iPSC-derived podocytes/kidney organoids are suitable in-vitro platforms for future *NUP93*-specific modeling.

---

## Mechanistic Model (synthesis)

```
Biallelic hypomorphic NUP93 variants (germline, AR)
            │  (destabilized NUP93 scaffold protein)
            ▼
Impaired NUP93–NUP205 inner-ring binding → defective NPC assembly
            │  (nuclear envelope / nuclear pore defect; GO:0051292)
            ▼
Disrupted nucleocytoplasmic transport in podocytes (GO:0006913)
      ├── Branch A: ↓ SMAD nuclear import → impaired BMP7–SMAD signaling (inferred)
      ├── Branch B: CDC42 dysregulation (demonstrated in NUP160/107/85/133 models)
      └── Branch C: YAP/TAZ mislocalization (demonstrated for NUP205/107)
            │
            ▼
Podocyte injury (vacuolization, deformed nuclei, dilated ER, cytoskeletal failure)
            │
            ▼
Foot-process effacement → loss of glomerular filtration barrier (CL:0000653, UBERON:0000074)
            │
            ▼
Nephrotic-range proteinuria → hypoalbuminemia → edema  [STEROID-RESISTANT]
            │
            ▼
Focal segmental glomerulosclerosis (FSGS, ~89%)
            │
            ▼
Rapid progression → end-stage kidney failure (median ~3.7 y; NUP93 = most aggressive)
            │
            ▼
Kidney transplant → LOW recurrence (intrinsic genetic podocytopathy)
```

---

## Evidence Base

| PMID | Study | How it supports the findings |
|---|---|---|
| [26878725](https://pubmed.ncbi.nlm.nih.gov/26878725/) | Braun et al. 2016 — *Mutations in nuclear pore genes NUP93, NUP205 and XPO5 cause SRNS* | **Landmark** — establishes *NUP93* (with *NUP205*, *XPO5*) as monogenic SRNS cause; defines NPHS12's causal gene and NPC/SMAD mechanism |
| [39331077](https://pubmed.ncbi.nlm.nih.gov/39331077/) | Yao 2025 — *Nucleoporin-associated SRNS* (review) | Median onset ages (NUP93 ≈ 3 y), aggressive course, FSGS ~89%, immunosuppressant resistance, panel-based diagnosis, low transplant recurrence |
| [39814977](https://pubmed.ncbi.nlm.nih.gov/39814977/) | 2025 cohort — NUP85/93/107/160 SRNS | Direct NUP93 patient: kidney failure 6 mo after diagnosis; missense variants destabilize NUP93; podocyte vacuolization, deformed nuclei, GBM disruption, foot-process effacement |
| [38650033](https://pubmed.ncbi.nlm.nih.gov/38650033/) | 2024 Chinese cohort — NUP93/107/160 SRNS | Biallelic variants cause severe early-onset SRNS → rapid ESKD; FSGS; expands variant spectrum |
| [30179222](https://pubmed.ncbi.nlm.nih.gov/30179222/) | Braun et al. 2018 — *Multiple NPC components cause nephrotic syndrome* | CRISPR KO of nucleoporins in podocytes activates CDC42 — shared mechanism |
| [40298220](https://pubmed.ncbi.nlm.nih.gov/40298220/) | 2025 — Podocyte-specific *Nup160* KO mouse | In-vivo model: proteinuria + foot-process effacement; CDC42 dysregulation (single-cell omics) |
| [37565816](https://pubmed.ncbi.nlm.nih.gov/37565816/) | 2023 — NUP205 regulates YAP/TAZ | Links NPC dysfunction to Hippo-effector mislocalization in podocytes |
| [34031708](https://pubmed.ncbi.nlm.nih.gov/34031708/) | 2021 — Re-analysis of post-transplant recurrence in genetic NS | One plausible biallelic *NUP93* recurrence; genetic SRNS recurrence very rare |
| [40402239](https://pubmed.ncbi.nlm.nih.gov/40402239/) | 2025 — WGS Egyptian SRNS cohort | Monogenic cause in 56.1% of families incl. *NUP93*; value of genetic diagnosis |
| [41141495](https://pubmed.ncbi.nlm.nih.gov/41141495/) | 2025 — Saudi pediatric kidney disease exome cohort | Consanguinity (54%), founder effects, genetic diagnostic yield context |
| [26411495](https://pubmed.ncbi.nlm.nih.gov/26411495/) | Miyake et al. 2015 — *NUP107* SRNS | Defines the **adjacent** entity (NPHS11/*NUP107*) — key for disambiguation from NPHS12 |
| [30427554](https://pubmed.ncbi.nlm.nih.gov/30427554/) | 2018 — *NUP133* GAMOS, zebrafish model | Conserved NPC → podocyte mechanism; rescue by WT not mutant mRNA |

---

## Limitations and Knowledge Gaps

1. **Gene-assignment correction.** This investigation initially (iterations 1–4) misassigned NPHS12 to *NUP107*; ontology verification (EBI OLS4) corrected it to *NUP93* (MONDO:0014817 → OMIM 616892). Readers and downstream knowledge bases must use the corrected *NUP93* assignment. Several cited mechanistic papers describe *paralogous* nucleoporins (*NUP107/160/205*) rather than *NUP93* directly; mechanism is inferred by family analogy where NUP93-specific data are lacking.
2. **Rarity.** NPHS12 is ultra-rare; most evidence is from small case series and consanguineous cohorts. No population-level prevalence/incidence, penetrance quantification, or carrier-frequency estimates exist.
3. **Branch-specific uncertainty.** The SMAD/BMP7 branch is inferred for NUP93 from the original Braun framework; CDC42 and YAP/TAZ branches are best demonstrated in *other* nucleoporins. Which branch dominates in NUP93 podocytes is not firmly established.
4. **No dedicated *NUP93* animal model** was identified; recapitulation evidence relies on paralog models (*Nup160* mouse; *nup107/133* fish/frog).
5. **No disease-specific QoL, mortality, or natural-history registry data**; prognosis is inferred from pooled nucleoporin-SRNS and genetic-SRNS literature.
6. **No veterinary/natural-disease counterpart** catalogued.

---

## Proposed Follow-up Experiments / Actions

1. **Confirm and propagate the corrected identifier mapping** (NPHS12 = MONDO:0014817 = OMIM 616892 = *NUP93*; NPHS11 = OMIM 616730 = *NUP107*) throughout the knowledge base, with an explicit disambiguation note.
2. **Generate a podocyte-specific *Nup93* conditional-knockout (or hypomorphic knock-in) mouse** to test whether NUP93 disease proceeds through CDC42, YAP/TAZ, and/or SMAD branches, mirroring the *Nup160* mouse design.
3. **iPSC-derived podocyte / kidney-organoid models** carrying patient *NUP93* variants (e.g., c.1655A>G, c.1604A>C) to assay NPC assembly, nucleocytoplasmic transport of SMAD/YAP/TAZ, and CDC42 activity.
4. **Genotype–phenotype meta-analysis** aggregating published *NUP93* patients to quantify onset, time-to-kidney-failure, and allele-severity correlations with adequate power.
5. **Evaluate CDC42/Rho-pathway or YAP-TAZ-directed small molecules** in NUP93 podocyte models as candidate targeted therapies.
6. **Prospective transplant-outcome registry** for genetic nucleoporin-SRNS to firm up the ~12.5% NUP93 recurrence signal.
7. **Deep-variant curation** of *NUP93* in ClinVar/gnomAD and consanguineous cohorts to identify founder alleles and refine ACMG classifications.

---

*Report compiled from aggregated database resources (MONDO, OMIM, UniProt, gnomAD, ClinVar, HGNC) and primary literature. Evidence source types span human clinical cohorts, model-organism studies, and in-vitro functional work, as indicated per claim.*


## Artifacts

- [OpenScientist final report](Nephrotic_Syndrome_Type_12-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Nephrotic_Syndrome_Type_12-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 8 |
| Quoted claims found in source | 8 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 15 |
| On topic | 13 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 19 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 13 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 8 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014817` (8 mentions) - the report calls it "if available", "nephrotic syndrome, type 12"; MONDO calls it **nephrotic syndrome, type 12**
- `HP:0012588` (1 mention) - the report calls it "Clinical/laboratory"; HP calls it **Steroid-resistant nephrotic syndrome**
- `HP:0000093` (2 mentions) - the report calls it "Laboratory", "Urinalysis:** nephrotic-range proteinuria"; HP calls it **Proteinuria**
- `HP:0003073` (2 mentions) - the report calls it "Laboratory", "Serum:** hypoalbuminemia"; HP calls it **Hypoalbuminemia**
- `HP:0000969` (1 mention) - the report calls it "Clinical sign"; HP calls it **Edema**
- `HP:0000097` (1 mention) - the report calls it "Histopathology"; HP calls it **Focal segmental glomerulosclerosis**
- `HP:0031266` (1 mention) - the report calls it "Ultrastructural"; HP calls it **Podocyte foot process effacement**
- `HP:0003774` (1 mention) - the report calls it "Clinical"; HP calls it **Stage 5 chronic kidney disease**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0051292` (3 mentions) - the report calls it "Cellular processes:** Nuclear pore complex assembly", "GO biological process:** nuclear pore complex assembly"; GO calls it **nuclear pore complex assembly**
- `GO:0005643` (2 mentions) - the report calls it "GO cellular component:** nuclear pore", "nuclear pore complex"; GO calls it **nuclear pore**
- `UBERON:0000074` (3 mentions) - the report calls it "UBERON anatomy:** renal glomerulus", "renal glomerulus"; UBERON calls it **renal glomerulus**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0014817` - called "if available", "nephrotic syndrome, type 12"
- `HP:0000093` - called "Laboratory", "Urinalysis:** nephrotic-range proteinuria"
- `HP:0003073` - called "Laboratory", "Serum:** hypoalbuminemia"
- `GO:0051292` - called "Cellular processes:** Nuclear pore complex assembly", "GO biological process:** nuclear pore complex assembly"
- `GO:0005643` - called "GO cellular component:** nuclear pore", "nuclear pore complex"
- `UBERON:0000074` - called "UBERON anatomy:** renal glomerulus", "renal glomerulus"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.
