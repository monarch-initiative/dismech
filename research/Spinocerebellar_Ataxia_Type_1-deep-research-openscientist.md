---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-05T22:53:55.176494'
end_time: '2026-09-05T23:11:12.977721'
duration_seconds: 1037.8
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Spinocerebellar Ataxia Type 1
  mondo_id: MONDO:0008119
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
citation_count: 26
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Spinocerebellar_Ataxia_Type_1-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Spinocerebellar_Ataxia_Type_1-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spinocerebellar Ataxia Type 1
- **MONDO ID:** MONDO:0008119 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spinocerebellar Ataxia Type 1** covering all of the
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

# Spinocerebellar Ataxia Type 1 (SCA1): Comprehensive Disease Characterization

**Disease:** Spinocerebellar Ataxia Type 1
**MONDO ID:** MONDO:0008119 | **OMIM:** #164400 (disease) / *601556 (*ATXN1* gene) | **Orphanet:** ORPHA:98755 | **Category:** Mendelian (autosomal dominant, polyglutamine repeat expansion)

*Evidence base: aggregated disease-level resources (OMIM, Orphanet, GeneReviews) plus primary literature and model-organism studies. Where a claim is inferred rather than directly demonstrated in humans, this is noted.*

---

## Summary

Spinocerebellar ataxia type 1 (SCA1) is a rare (~1–2 per 100,000) autosomal dominant, adult-onset neurodegenerative disorder caused by expansion of a glutamine-encoding CAG repeat in exon 8 of the *ATXN1* gene on chromosome 6p22.3. The expanded repeat produces a polyglutamine (polyQ)-lengthened ataxin-1 protein that acts predominantly through a **toxic gain-of-function** mechanism in the cerebellum, although loss of normal ataxin-1 function contributes to cognitive/cortical abnormalities. SCA1 is one of at least nine polyglutamine diseases and is clinically notable for having the **fastest functional decline among the common SCAs**, ahead of SCA3, SCA2, SCA6, and SCA10.

The mechanistic cascade begins with the CAT-uninterrupted CAG expansion, proceeds through phosphorylation of ataxin-1 at Ser776 by region-specific kinases (MSK1 in cerebellum, RSK3 in brainstem) that stabilizes the toxic protein, and continues through aberrant interaction with the transcriptional repressor CIC (capicua), RBFOX1-mediated alternative splicing dysregulation, repeat-associated non-AUG (RAN) translation of toxic homopolymeric proteins, and non-cell-autonomous oligodendrocyte/glial dysfunction. These converging insults drive progressive degeneration of cerebellar Purkinje cells, brainstem nuclei, and spinocerebellar tracts in an olivopontocerebellar pattern. Clinically this manifests as progressive gait and limb ataxia, dysarthria, oculomotor abnormalities, pyramidal signs, and eventual bulbar failure; death typically results from aspiration and respiratory complications.

Diagnosis rests on targeted molecular testing for the *ATXN1* CAG repeat expansion (with assessment of CAT interruptions), supported by clinical rating (SARA), MRI volumetry/spectroscopy, and blood neurofilament light chain (NfL) as progression biomarkers that change before ataxia onset. There is currently **no approved disease-modifying therapy**; management is multidisciplinary and symptomatic. However, ATXN1-lowering antisense oligonucleotides (ASOs) have rescued motor deficits and premature lethality in knock-in mouse models and represent the leading disease-modifying strategy advancing toward clinical translation, alongside kinase inhibition, autophagy enhancement, and gene-based approaches.

---

## Section 1: Disease Information

**Overview.** SCA1 is an autosomal dominant neurodegenerative disorder belonging to the polyglutamine (CAG-repeat) disease family. It is characterized by progressive cerebellar ataxia with additional brainstem, pyramidal, and later bulbar involvement, and by degeneration concentrated in the cerebellum and brainstem [PMID: 42608759](https://pubmed.ncbi.nlm.nih.gov/42608759/). It affects "one or two individuals per 100,000" [PMID: 37238658](https://pubmed.ncbi.nlm.nih.gov/37238658/).

**Key identifiers:**
- **MONDO:** MONDO:0008119
- **OMIM:** #164400 (disease); *601556 (*ATXN1* gene)
- **Orphanet:** ORPHA:98755
- **Gene:** *ATXN1* (HGNC:10548); chromosome 6p22.3
- **MeSH:** Spinocerebellar Ataxias / Spinocerebellar Degenerations
- **ICD-10:** G11.1 / G11.8; **ICD-11:** 8A03.10 (hereditary ataxia)

**Synonyms and alternative names:** Spinocerebellar ataxia 1; SCA1; olivopontocerebellar atrophy I (OPCA I, historical); Menzel-type OPCA (historical); spinocerebellar degeneration; ataxin-1 polyglutamine disease.

**Information source.** The knowledge in this report is derived predominantly from **aggregated disease-level resources** — OMIM, Orphanet, published cohort/natural-history studies, and mechanistic model-organism and in-vitro literature — rather than from individual patient EHR records.

---

## Section 2: Etiology

**Primary cause (genetic).** SCA1 is caused by expansion of a glutamine-encoding CAG repeat in exon 8 of *ATXN1*. As stated in the literature: *"Ataxin-1 (ATXN1) was originally identified as a gene in which abnormal expansion of glutamine encoding CAG repeats causes inherited neurodegenerative disease spinocerebellar ataxia type 1"* [PMID: 42608759](https://pubmed.ncbi.nlm.nih.gov/42608759/). This is a **monogenic Mendelian** disorder; there are no established environmental or infectious causes.

**Genetic risk factors.**
- **Causal variant:** CAG repeat expansion in *ATXN1*. Normal alleles typically carry ≤35–36 repeats; pathogenic alleles are generally ≥39 CAG. A key structural determinant is the **presence or absence of CAT interruptions**: normal-range alleles contain CAT interruptions that stabilize the repeat tract, whereas expanded pathogenic alleles are typically pure, uninterrupted CAG — *"None of the expanded alleles contained CAT interruptions"* [PMID: 16110192](https://pubmed.ncbi.nlm.nih.gov/16110192/). Loss of CAT interruption itself confers pathogenicity.
- **Repeat length** is the dominant modifier of age at onset and severity: across polyQ SCAs, *"CAG repeat length correlated inversely with age at onset, accounting for 80% of the variability"* [PMID: 19429075](https://pubmed.ncbi.nlm.nih.gov/19429075/).
- A documented case with an intermediate allele (37 CAG, uninterrupted) alongside a large 61-CAG expansion demonstrated early onset and rapid progression, underscoring the importance of interruption status for counseling [PMID: 39289638](https://pubmed.ncbi.nlm.nih.gov/39289638/).

**Environmental risk factors.** None established as causal. Sex, age, and lifestyle are not proven disease-causing factors; the disease is fully genetically determined by the expanded allele. Age modifies **timing of onset** (adult-onset) but not disease occurrence.

**Protective / modifier factors.** CAT interruptions within the repeat tract are protective (stabilizing). A rare SCA1 family showed anticipation *without* CAG expansion, indicating *"factors other than the length of the CAG repeat play a considerable role in determination of the disease course"* [PMID: 16110192](https://pubmed.ncbi.nlm.nih.gov/16110192/). Genetic modifiers set prior risk for progression [PMID: 42677125](https://pubmed.ncbi.nlm.nih.gov/42677125/). No robust environmental protective factor is established.

**Gene–environment interactions.** No well-characterized GxE interactions are established for SCA1; disease penetrance is driven by the germline repeat expansion.

---

## Section 3: Phenotypes

SCA1 presents as an **adult-onset, progressive pan-cerebellar syndrome** with characteristic pyramidal and later brainstem/bulbar features.

| Phenotype | Type | HPO term | Characteristics |
|-----------|------|----------|-----------------|
| Gait ataxia | Clinical sign | HP:0002066 / HP:0001251 (ataxia) | Adult onset, progressive; usually the presenting feature |
| Limb incoordination | Clinical sign | HP:0001251 | Progressive |
| Dysarthria | Clinical sign | HP:0001260 | Progressive slurred speech |
| Nystagmus / oculomotor abnormality | Clinical sign | HP:0000639 (nystagmus); saccadic slowing | Common; early |
| Cerebellar atrophy | Imaging finding | HP:0001272 | Progressive |
| Pyramidal signs (hyperreflexia, spasticity) | Clinical sign | HP:0001347 / HP:0001257 | Characteristic of SCA1 vs other SCAs |
| Dysphagia | Clinical sign | HP:0002015 | Later stage; bulbar involvement, aspiration risk |
| Peripheral neuropathy | Clinical sign | HP:0009830 | Later stage |
| Cognitive impairment | Behavioral/cognitive | HP:0100543 | Present; ATXN1 loss-of-function contributes |
| Depression / mood changes | Behavioral | HP:0000716 | Present |
| Parkinsonism | Clinical sign | HP:0001300 | Non-ataxic feature; most common nonataxic phenotype across SCAs |

SCA1 characteristically adds **pyramidal signs (hyperreflexia, spasticity)** and later **brainstem/bulbar dysfunction (dysphagia, respiratory compromise) plus peripheral neuropathy**; cognition and mood are affected. Across SCAs, *"Parkinsonism was the most common nonataxic phenotype (21.1%)"* in a Taiwanese cohort [PMID: 31523939](https://pubmed.ncbi.nlm.nih.gov/31523939/), and nonmotor symptoms include *"impaired cognition (6.1% of SCA2 and 8.3% of SCA3 patients) and depression"* [PMID: 31523939](https://pubmed.ncbi.nlm.nih.gov/31523939/). Because ATXN1 regulates gene expression broadly, cognitive/mood involvement is mechanistically consistent [PMID: 42608759](https://pubmed.ncbi.nlm.nih.gov/42608759/).

**Progression and severity:** progressive and severe; SCA1 has the fastest functional decline of the common SCAs (see Section 8). **Quality of life impact** is substantial and cumulative — loss of ambulation, communication difficulty from dysarthria, dysphagia with aspiration risk, and dependence in activities of daily living. Per-phenotype QoL instruments specific to SCA1 were not identified in this investigation; generic and ataxia-specific functional staging (SARA-linked) is used.

---

## Section 4: Genetic / Molecular Information

**Causal gene.** *ATXN1* (ataxin-1), chromosome 6p22.3; HGNC:10548; OMIM *601556.

**Pathogenic variant.**
- **Type/class:** Trinucleotide (CAG) repeat expansion — a dynamic mutation, not a point mutation. The expansion resides in coding exon 8 and is translated into an elongated polyglutamine tract.
- **Classification:** Pathogenic (ACMG); repeat length ≥39 CAG (uninterrupted) is considered pathogenic; the intermediate/reduced-penetrance zone and interruption status affect interpretation.
- **Allele architecture:** Pathogenic alleles are **pure CAG lacking CAT interruptions**; normal alleles contain CAT interruptions — *"None of the expanded alleles contained CAT interruptions"* [PMID: 16110192](https://pubmed.ncbi.nlm.nih.gov/16110192/).
- **Origin:** Germline (inherited, autosomal dominant). Not somatic.
- **Functional consequence:** Predominantly **toxic gain-of-function** — *"CAG expansion predominantly causes pathogenic ATXN1 gain-of-function in the cerebellum"* [PMID: 42608759](https://pubmed.ncbi.nlm.nih.gov/42608759/) — with a contributory **loss-of-function** component (loss of ATXN1 also causes cognitive/cortical abnormalities) [PMID: 42608759](https://pubmed.ncbi.nlm.nih.gov/42608759/).

**Modifier genes / molecular modulators.**
- **CIC (capicua):** forms a transcriptional repressor complex with ATXN1; *"The interaction of polyglutamine-expanded ATXN1 with the transcriptional repressor CIC drives cerebellar Purkinje cell pathogenesis"* [PMID: 36577402](https://pubmed.ncbi.nlm.nih.gov/36577402/).
- **RBFOX1:** splicing factor mediating mutant-ATXN1 splicing dysregulation; modulating Rbfox1 modifies neurodegeneration in a Drosophila SCA1 model [PMID: 37802886](https://pubmed.ncbi.nlm.nih.gov/37802886/).
- **MSK1 / RSK3:** kinases phosphorylating ATXN1 at Ser776 (region-specific) [PMID: 33709453](https://pubmed.ncbi.nlm.nih.gov/33709453/).
- **TG5 (transglutaminase 5):** *"TG enzymes catalyzed cross-linking of ATXN1 in a polyQ-length-dependent manner, thereby preferentially modulating mutant ATXN1 stability and oligomerization"* [PMID: 35499073](https://pubmed.ncbi.nlm.nih.gov/35499073/).
- **TCF7L2, HTT:** identified as key regulators in oligodendrocyte-driven pathology [PMID: 42113962](https://pubmed.ncbi.nlm.nih.gov/42113962/).

**Epigenetic information / chromosomal abnormalities.** No large-scale chromosomal abnormalities (aneuploidy, translocations) are associated; SCA1 is a single-locus repeat-expansion disorder. Specific disease-defining epigenetic marks were not established in this investigation.

---

## Section 5: Environmental Information

SCA1 is a **purely genetic Mendelian disorder** with no established environmental, lifestyle, or infectious contributing factors. Toxins, radiation, occupational exposures, diet, smoking, and alcohol are **not implicated** in causation. No infectious agents (bacteria, viruses, fungi, parasites) are involved. Environmental factors do not modify disease occurrence, though supportive/rehabilitative environment influences functional outcome.

---

## Section 6: Mechanism / Pathophysiology

### Ordered causal chain

1. **CAT-uninterrupted CAG repeat expansion in *ATXN1* exon 8** *leads to* a translated polyglutamine-expanded ataxin-1 protein (germline, gain-of-function) [PMID: 42608759](https://pubmed.ncbi.nlm.nih.gov/42608759/), [PMID: 16110192](https://pubmed.ncbi.nlm.nih.gov/16110192/).
2. Expanded ataxin-1 *is phosphorylated at Ser776* by region-specific kinases — **MSK1 in cerebellum, RSK3 in brainstem** — which *stabilizes the protein and promotes toxicity* [PMID: 33709453](https://pubmed.ncbi.nlm.nih.gov/33709453/).
3. Stabilized mutant ataxin-1 *forms nuclear inclusions* (GO:0005634 nucleus) and *engages aberrant protein complexes* — notably with the transcriptional repressor **CIC/capicua** — which *results in* dysregulated transcription in Purkinje cells [PMID: 36577402](https://pubmed.ncbi.nlm.nih.gov/36577402/).
4. **Branch A (transcription/splicing):** Mutant ataxin-1 *causes widespread alternative-splicing dysregulation* via the splicing factor **RBFOX1**, which *contributes to* neurodegeneration [PMID: 37802886](https://pubmed.ncbi.nlm.nih.gov/37802886/).
5. **Branch B (RAN translation):** The expanded repeat *undergoes repeat-associated non-AUG (RAN) translation*, producing sense polyserine and antisense polyleucine aggregates that *impair autophagy* and *accumulate in cerebellum and pons* [PMID: 41422503](https://pubmed.ncbi.nlm.nih.gov/41422503/).
6. **Branch C (non-cell-autonomous glia):** Mutant ataxin-1 in **oligodendrocytes** *is sufficient to drive dysregulated myelination, Purkinje-cell axonal shrinkage, and torpedo formation*, which *impairs motor coordination* [PMID: 42113962](https://pubmed.ncbi.nlm.nih.gov/42113962/).
7. These converging insults *lead to* **mitochondrial/bioenergetic dysfunction, reduced dendritic arborization, and impaired neuronal network activity** (demonstrated in patient iPSC-derived neurons) [PMID: 37278528](https://pubmed.ncbi.nlm.nih.gov/37278528/).
8. The cumulative toxicity *results in* **progressive Purkinje-cell degeneration** (earliest/most severe in posterior cerebellar vermis) and **brainstem neuronal loss** [PMID: 42113962](https://pubmed.ncbi.nlm.nih.gov/42113962/), [PMID: 38750673](https://pubmed.ncbi.nlm.nih.gov/38750673/).
9. Regional neurodegeneration *manifests clinically* as progressive ataxia, dysarthria, oculomotor and pyramidal signs, and — via brainstem involvement — bulbar failure and premature death [PMID: 32791425](https://pubmed.ncbi.nlm.nih.gov/32791425/).

```
CAG expansion (pure, no CAT)
        │
        ▼
 polyQ-ataxin-1  ──► RAN translation ──► polySer/polyLeu aggregates ──► autophagy impairment
        │                                         (Branch B)
        ▼ Ser776 phosphorylation
  (MSK1 cerebellum / RSK3 brainstem)  ── protein stabilization
        │
        ├──► nuclear inclusions + ATXN1–CIC complex ──► transcriptional dysregulation (Branch A)
        │                                   │
        │                                   └──► RBFOX1 ──► aberrant alternative splicing
        │
        └──► oligodendrocyte dysfunction ──► dysmyelination + PC axonopathy/torpedoes (Branch C)
                                   │
                                   ▼
        mitochondrial dysfunction, dendritic loss, network failure
                                   │
                                   ▼
   Purkinje-cell + brainstem degeneration (olivopontocerebellar)
                                   │
                                   ▼
        ataxia, dysarthria, pyramidal/bulbar signs → death
```

**Upstream vs downstream.** The CAG expansion and Ser776 phosphorylation are the most upstream, targetable nodes; CIC binding, RBFOX1 splicing, RAN translation, and oligodendrocyte dysfunction are intermediate; Purkinje-cell/brainstem degeneration and clinical ataxia are downstream.

**Cell types (CL) and processes (GO).** Primary target: **cerebellar Purkinje cell (CL:0000121)**; also **oligodendrocyte (CL:0000128)** and **Bergmann glia (CL:0000644)**. Key GO processes: regulation of transcription (GO:0006355), mRNA splicing (GO:0000398), autophagy (GO:0006914), myelination (GO:0042552). Subcellular: nucleus (GO:0005634), mitochondrion (GO:0005739). Chemical entity: **L-glutamine / polyglutamine (CHEBI:28300)**.

**Molecular profiling.** ASO-mediated Atxn1 reduction *"restored disease-associated transcriptome profiles toward WT"* and reversed neurochemical abnormalities [PMID: 30385727](https://pubmed.ncbi.nlm.nih.gov/30385727/), demonstrating a reversible transcriptomic/neurochemical signature. Alternative-splicing dysregulation is a defined transcriptomic feature [PMID: 37802886](https://pubmed.ncbi.nlm.nih.gov/37802886/).

---

## Section 7: Anatomical Structures Affected

**Organ / body-system level.** Primary organ: **brain**, specifically the **cerebellum (UBERON:0002037)** and **brainstem (UBERON:0002298)** — pons, medulla, and inferior olive (UBERON:0000988). Body system: **central nervous system**. The pattern corresponds to **olivopontocerebellar atrophy** with **spinocerebellar tract** and **dentate nucleus** involvement.

**Tissue / cell level.** Nervous tissue. Principal targets:
- **Cerebellar Purkinje cells (CL:0000121)** — *"progressive motor deficits and Purkinje cell (PC) degeneration, driven by polyglutamine expansion in ataxin-1"* [PMID: 42113962](https://pubmed.ncbi.nlm.nih.gov/42113962/).
- **Oligodendrocytes (CL:0000128)** — dysmyelination contributes non-cell-autonomously [PMID: 42113962](https://pubmed.ncbi.nlm.nih.gov/42113962/).
- **Bergmann glia (CL:0000644)** and other glia show pathology.

**Regional selectivity.** *"We demonstrated earlier and more severe pathology of PCs and glia in the posterior cerebellar vermis of SCA1 mice"* [PMID: 38750673](https://pubmed.ncbi.nlm.nih.gov/38750673/) — posterior vermis > anterior. The **brainstem is the region most closely linked to premature death** [PMID: 33709453](https://pubmed.ncbi.nlm.nih.gov/33709453/).

**Subcellular level.** Mutant ataxin-1 accumulates as **nuclear inclusions (GO:0005634)**; **mitochondrial dysfunction (GO:0005739)** occurs.

**Lateralization.** Bilateral and largely symmetric involvement.

---

## Section 8: Temporal Development

**Onset.** Typically **adult-onset** (commonly 30s–40s), insidious and chronic. Earlier onset occurs with larger, uninterrupted expansions — a 23-year-old with a 61-CAG uninterrupted allele showed early onset and rapid progression [PMID: 39289638](https://pubmed.ncbi.nlm.nih.gov/39289638/).

**Progression.** Chronic, relentlessly progressive. SCA1 has the **fastest functional decline among common SCAs**: *"Natural history studies revealed that SCA1 patients' functional status worsened significantly faster than in other SCA subtypes, followed by SCA3, SCA2, SCA6, and SCA10"* [PMID: 32791425](https://pubmed.ncbi.nlm.nih.gov/32791425/). Progression is quantified clinically by the Scale for Assessment and Rating of Ataxia (SARA), which *"capture[s] genotype-specific trajectories but lose[s] sensitivity at the extremes of the disease course"* [PMID: 42677125](https://pubmed.ncbi.nlm.nih.gov/42677125/).

**Stages.** Early (gait ataxia, mild dysarthria/oculomotor signs) → intermediate (limb ataxia, pyramidal signs, worsening speech) → advanced (bulbar dysfunction, dysphagia, respiratory compromise, loss of ambulation).

**Critical periods / premanifest window.** A quantifiable **premanifest window** exists: *"Volumetric, microstructural, and spectroscopic MRI and blood neurofilament light chain change before ataxia onset and predict subsequent decline, whereas repeat length and genetic modifiers set prior risk"* [PMID: 42677125](https://pubmed.ncbi.nlm.nih.gov/42677125/) — a key therapeutic-intervention window.

**Anticipation.** Genetic anticipation occurs: *"Genetic anticipation was observed in the 80% of transmissions. Repeat instability was greater in paternal transmissions"* [PMID: 19429075](https://pubmed.ncbi.nlm.nih.gov/19429075/). No spontaneous remission; the course is chronic and lifelong.

---

## Section 9: Inheritance and Population

**Epidemiology.** SCA1 prevalence is approximately **1–2 per 100,000** — *"an autosomal dominant neurodegenerative disorder that affects one or two individuals per 100,000"* [PMID: 37238658](https://pubmed.ncbi.nlm.nih.gov/37238658/). Relative frequency among SCAs varies regionally: SCA3 is the most common worldwide; in a northern Chinese cohort **SCA1 accounted for 13.8% (11/80 families)** vs SCA3 57.5% and SCA2 16.3% [PMID: 42474585](https://pubmed.ncbi.nlm.nih.gov/42474585/). SCA1 is generally a smaller fraction than SCA2/SCA3 in most populations.

**Inheritance genetics.**
- **Pattern:** Autosomal dominant [PMID: 37238658](https://pubmed.ncbi.nlm.nih.gov/37238658/).
- **Penetrance:** Age-dependent and high for fully expanded, uninterrupted alleles; influenced by repeat length and interruption status.
- **Expressivity:** Variable (age of onset and severity vary with repeat length and modifiers).
- **Anticipation:** Yes — increasing severity/earlier onset in successive generations, greater with paternal transmission [PMID: 19429075](https://pubmed.ncbi.nlm.nih.gov/19429075/).
- **Founder effects:** Population-specific haplotypes shape geographic distribution of SCA subtypes; well-documented founder effects exist for related SCAs (e.g., SCA2 in Holguin, Cuba) [PMID: 19429075](https://pubmed.ncbi.nlm.nih.gov/19429075/).

**Population demographics.** No strong sex predilection (autosomal). Geographic relative frequency varies (see above). Larger, uninterrupted expansions concentrate in earlier-onset, more severe cases.

---

## Section 10: Diagnostics

**Genetic testing (definitive).** Diagnosis requires **molecular testing for the *ATXN1* CAG repeat expansion**. Standard methods: **fluorescent PCR, triplet-primed PCR (TP-PCR), and enzymatic digestion to detect CAT interruptions** — as applied in a documented case where repeats were *"assessed by fluorescent PCR, tripled-primed PCR and enzymatic digestion for the search of sequence interruption in the CAG repeats"* [PMID: 39289638](https://pubmed.ncbi.nlm.nih.gov/39289638/). SCA1 is included on dominant-ataxia gene panels and NGS ataxia panels. Determining interruption status is clinically important — *"The determination of the absence of CAT interruption brought crucial information concerning this molecular diagnosis, the prediction of the disease and had practical consequences for genetic counseling"* [PMID: 39289638](https://pubmed.ncbi.nlm.nih.gov/39289638/).

**Clinical rating.** **SARA** is the standard clinical progression scale [PMID: 42677125](https://pubmed.ncbi.nlm.nih.gov/42677125/).

**Imaging & fluid biomarkers.** MRI shows cerebellar and brainstem (olivopontocerebellar) atrophy; **volumetric, microstructural, and spectroscopic MRI and blood NfL change before ataxia onset and predict decline** [PMID: 42677125](https://pubmed.ncbi.nlm.nih.gov/42677125/). Wearable-sensor gait/balance metrics detect change earlier than clinical scales.

**Differential diagnosis.** Other dominant SCAs (SCA2, SCA3, SCA6, SCA7, SCA17), the increasingly recognized **SCA27B (FGF14 GAA expansion)** — *"one of the most common forms of adult-onset hereditary ataxia"* [PMID: 38279833](https://pubmed.ncbi.nlm.nih.gov/38279833/), multiple system atrophy-cerebellar type (MSA-C, "hot cross bun" sign) [PMID: 42453830](https://pubmed.ncbi.nlm.nih.gov/42453830/), Friedreich ataxia, and acquired ataxias. A tiered testing algorithm (Friedreich ataxia, common dominant SCAs, then NGS exome/genome) is used [PMID: 42616279](https://pubmed.ncbi.nlm.nih.gov/42616279/).

**Screening.** Predictive/cascade genetic testing is available for at-risk relatives with genetic counseling; prenatal and preimplantation genetic testing are options. No newborn screening.

---

## Section 11: Outcome / Prognosis

**Survival / mortality.** SCA1 is progressive and fatal, with the **fastest decline among common SCAs** [PMID: 32791425](https://pubmed.ncbi.nlm.nih.gov/32791425/). Death typically results from bulbar/respiratory complications; the **brainstem is most closely linked to premature death** [PMID: 33709453](https://pubmed.ncbi.nlm.nih.gov/33709453/).

**Prognostic factors.** *"Number of CAG repeats, age of onset, and ataxia severity at baseline are strong contributors to the risk of death in most SCAs"* [PMID: 32791425](https://pubmed.ncbi.nlm.nih.gov/32791425/). Longer CAG length and earlier onset predict worse outcomes [PMID: 39289638](https://pubmed.ncbi.nlm.nih.gov/39289638/).

**Prognostic biomarkers.** Blood **NfL** and MRI metrics predict subsequent decline and change premanifest [PMID: 42677125](https://pubmed.ncbi.nlm.nih.gov/42677125/).

**Morbidity / function.** Progressive disability: loss of ambulation, communication impairment, dysphagia, aspiration risk. Recovery potential is nil in the absence of disease-modifying therapy; rehabilitation slows functional loss.

---

## Section 12: Treatment

**No approved disease-modifying therapy exists for SCA1.** Management is **multidisciplinary and symptomatic**: *"Rehabilitation and multidisciplinary care remain foundational across all subtypes and are supported by growing clinical trial evidence"* [PMID: 41387161](https://pubmed.ncbi.nlm.nih.gov/41387161/) (NCIT: Rehabilitation Therapy).

**Symptomatic pharmacotherapy (off-label).** Off-label agents with subtype-specific benefit include **riluzole, 4-aminopyridine, and varenicline**; **omaveloxolone** is approved for Friedreich ataxia (not SCA1) [PMID: 41387161](https://pubmed.ncbi.nlm.nih.gov/41387161/). Troriluzole (riluzole prodrug) is *"already in clinical trials for cerebellar ataxia"* [PMID: 40988103](https://pubmed.ncbi.nlm.nih.gov/40988103/).

**Neuromodulation.** tDCS and rTMS show early promise for motor outcomes [PMID: 41387161](https://pubmed.ncbi.nlm.nih.gov/41387161/).

**Disease-modifying strategies in development:**
- **ATXN1-lowering antisense oligonucleotide (leading strategy).** In Atxn1(154Q/2Q) knock-in mice, *"Following a single ASO treatment at 5 weeks of age, mice demonstrated rescue of these disease-associated phenotypes"* and *"these findings support the efficacy and therapeutic importance of directly targeting ATXN1 RNA expression as a strategy for treating both motor deficits and lethality in SCA1"* [PMID: 30385727](https://pubmed.ncbi.nlm.nih.gov/30385727/) (NCIT: Antisense Oligonucleotide).
- **Region-specific kinase inhibition.** *"Reducing Rsk3 rescues brainstem-associated pathologies and deficits, and lowering Rsk3 and Msk1 together improves cerebellar and brainstem function in an SCA1 mouse model"* [PMID: 33709453](https://pubmed.ncbi.nlm.nih.gov/33709453/).
- **Autophagy enhancement.** AUTEN-67/-99 small molecules ameliorate SCA1 symptoms in models [PMID: 41226482](https://pubmed.ncbi.nlm.nih.gov/41226482/).
- **Astrocytic MAO-B inhibition.** Oral **KDS2010** slows deterioration of motor coordination in a transgenic SCA1 model by inhibiting astrocytic MAO-B-mediated inflammation [PMID: 41427729](https://pubmed.ncbi.nlm.nih.gov/41427729/).
- **Gene-based therapies (broad pipeline).** *"molecular and gene-based therapies—including antisense oligonucleotides, viral vector delivery systems, and CRISPR-based strategies—are advancing into preclinical and early-phase clinical studies"* [PMID: 41387161](https://pubmed.ncbi.nlm.nih.gov/41387161/).

**Personalized/pharmacogenomics.** Genotype (repeat length, interruption status) informs prognosis and counseling; no established pharmacogenomic dosing yet.

---

## Section 13: Prevention

Because SCA1 is a highly penetrant (for fully expanded alleles) autosomal dominant disorder with no environmental cause, **primary prevention centers on genetic counseling and reproductive options** rather than lifestyle modification.

- **Primary prevention:** Genetic counseling; **preimplantation genetic testing (PGT)** and **prenatal diagnosis** to prevent transmission of the expanded allele. Assessment of CAT interruption status improves prediction and counseling [PMID: 39289638](https://pubmed.ncbi.nlm.nih.gov/39289638/).
- **Secondary prevention:** Predictive/cascade genetic testing of at-risk relatives, enabling premanifest monitoring using MRI and NfL biomarkers [PMID: 42677125](https://pubmed.ncbi.nlm.nih.gov/42677125/).
- **Tertiary prevention:** Prevention of complications — swallowing evaluation and aspiration precautions, physical/occupational/speech therapy, fall prevention, management of respiratory complications.
- **Immunization / public health / environmental interventions:** Not applicable (no infectious or environmental etiology).

---

## Section 14: Other Species / Natural Disease

- **Taxonomy / orthologs:** *ATXN1* has orthologs across vertebrates (mouse *Atxn1*, NCBI Gene 20238; also studied in *Drosophila* and *C. elegans* via transgenic/humanized approaches).
- **Natural disease:** No well-established naturally occurring SCA1 equivalent in companion animals or wildlife was identified in this investigation; SCA1 models are engineered rather than naturally occurring.
- **Comparative biology:** Disease mechanisms are conserved enough that mouse, *Drosophila*, and *C. elegans* systems faithfully model key aspects — Rbfox1-mediated splicing modification of neurodegeneration was demonstrated *"in a Drosophila model of spinocerebellar ataxia type 1 in vivo"* [PMID: 37802886](https://pubmed.ncbi.nlm.nih.gov/37802886/).
- **Transmission:** Not applicable — non-infectious, non-zoonotic.

---

## Section 15: Model Organisms

SCA1 is modeled across **mouse, *Drosophila*, *C. elegans*, and human iPSC** systems.

| Model | Type | Key features | Reference |
|-------|------|--------------|-----------|
| Atxn1(154Q/2Q) knock-in mouse | Mammalian, knock-in | Motor deficits + premature lethality; rescued by ASO | [PMID: 30385727](https://pubmed.ncbi.nlm.nih.gov/30385727/) |
| Pcp2-ATXN1[82Q] transgenic mouse | Mammalian, Purkinje-cell-targeted transgenic | Purkinje-cell-restricted expression; classic model | Finding F007 |
| SCA1 transgenic mouse (MAO-B study) | Mammalian | Motor coordination deficits; KDS2010 slows decline | [PMID: 41427729](https://pubmed.ncbi.nlm.nih.gov/41427729/) |
| *Drosophila* SCA1 model | Invertebrate | Rbfox1 manipulation modifies neurodegeneration; TG5 screen | [PMID: 37802886](https://pubmed.ncbi.nlm.nih.gov/37802886/), [PMID: 35499073](https://pubmed.ncbi.nlm.nih.gov/35499073/) |
| *C. elegans* SCA1 model | Invertebrate | AUTEN-67/-99 autophagy-enhancer testing | [PMID: 41226482](https://pubmed.ncbi.nlm.nih.gov/41226482/) |
| Patient fibroblasts / iPSC-derived neurons | In vitro (human) | Aggregation, reduced dendrites/branching, mitochondrial dysfunction, delayed network activity | [PMID: 37278528](https://pubmed.ncbi.nlm.nih.gov/37278528/) |

**Phenotype recapitulation.** Knock-in mice reproduce progressive motor deficits, Purkinje-cell/brainstem pathology, transcriptomic/neurochemical abnormalities, and premature lethality, and are reversible with ATXN1 lowering [PMID: 30385727](https://pubmed.ncbi.nlm.nih.gov/30385727/). iPSC-derived neurons show *"reduced dendrite length and number of branching points while MEA recordings identified delayed development in network activity"* [PMID: 37278528](https://pubmed.ncbi.nlm.nih.gov/37278528/). **Genetic models available:** knock-in, transgenic (cell-type-targeted), and humanized/invertebrate systems. **Limitations:** rodent lifespan and cerebellar circuitry differences; models may not capture the full human cognitive/mood spectrum or the decades-long human premanifest evolution. **Resources:** MGI (mouse), FlyBase (Drosophila), WormBase (C. elegans), and translational review [PMID: 41463080](https://pubmed.ncbi.nlm.nih.gov/41463080/).

---

## Key Findings (with statistical evidence)

**F001 — ATXN1 CAG expansion causes SCA1 via toxic gain-of-function.** SCA1 is caused by expansion of glutamine-encoding CAG repeats in *ATXN1* exon 8. Mouse models indicate the expansion predominantly causes ATXN1 gain-of-function in the cerebellum, while loss of ATXN1 contributes to cognitive/cortical abnormalities [PMID: 42608759](https://pubmed.ncbi.nlm.nih.gov/42608759/).

**F002 — SCA1 has the fastest decline among common SCAs; CAG length and onset age predict mortality.** *"SCA1 patients' functional status worsened significantly faster than in other SCA subtypes, followed by SCA3, SCA2, SCA6, and SCA10"* and *"Number of CAG repeats, age of onset, and ataxia severity at baseline are strong contributors to the risk of death"* [PMID: 32791425](https://pubmed.ncbi.nlm.nih.gov/32791425/).

**F003 — ATXN1-lowering ASO rescues motor deficits and prolongs survival.** A single ICV ASO at 5 weeks rescued disease phenotypes and premature lethality in knock-in mice, supporting *"directly targeting ATXN1 RNA expression as a strategy"* [PMID: 30385727](https://pubmed.ncbi.nlm.nih.gov/30385727/).

**F004 — ATXN1–CIC complex, glial/oligodendrocyte dysfunction, and RAN translation.** The ATXN1–CIC interaction *"drives cerebellar Purkinje cell pathogenesis"* [PMID: 36577402](https://pubmed.ncbi.nlm.nih.gov/36577402/); *"mutant ataxin-1 in oligodendrocytes is sufficient to drive aspects of SCA1-related pathology, including dysregulated myelination, PC axonal shrinkage, and torpedo formation"* [PMID: 42113962](https://pubmed.ncbi.nlm.nih.gov/42113962/); RAN proteins are *"a common molecular mechanism shared by the CAG-SCAs"* [PMID: 41422503](https://pubmed.ncbi.nlm.nih.gov/41422503/).

**F005 — CAG-driven anticipation modulated by CAT interruptions and parent-of-origin.** Expanded alleles lack CAT interruptions [PMID: 16110192](https://pubmed.ncbi.nlm.nih.gov/16110192/); CAG length accounts for ~80% of onset variability with anticipation and greater paternal instability [PMID: 19429075](https://pubmed.ncbi.nlm.nih.gov/19429075/).

**F006 — Region-specific Ser776 kinases (MSK1/RSK3) and TG5 govern selective vulnerability.** *"Lowering Rsk3 and Msk1 together improves cerebellar and brainstem function"* [PMID: 33709453](https://pubmed.ncbi.nlm.nih.gov/33709453/); TG enzymes *"catalyzed cross-linking of ATXN1 in a polyQ-length-dependent manner"* [PMID: 35499073](https://pubmed.ncbi.nlm.nih.gov/35499073/).

**F007 — Multi-system models; RBFOX1-mediated splicing dysregulation.** *"Rbfox1 mediates the effect of mutant ataxin-1 on misregulated alternative splicing"* and modifies neurodegeneration in Drosophila [PMID: 37802886](https://pubmed.ncbi.nlm.nih.gov/37802886/); iPSC neurons show dendritic/network deficits [PMID: 37278528](https://pubmed.ncbi.nlm.nih.gov/37278528/).

**F008 — Diagnosis by repeat testing; SARA, MRI, NfL as progression biomarkers.** MRI and NfL *"change before ataxia onset and predict subsequent decline"* [PMID: 42677125](https://pubmed.ncbi.nlm.nih.gov/42677125/).

**F009 — No approved disease-modifying therapy; molecular therapies advancing.** Rehabilitation is foundational; ASO/viral-vector/CRISPR strategies are advancing to early-phase studies [PMID: 41387161](https://pubmed.ncbi.nlm.nih.gov/41387161/).

**F010 — Rare AD polyQ SCA (~1–2/100,000), regionally variable frequency.** ~1–2/100,000 [PMID: 37238658](https://pubmed.ncbi.nlm.nih.gov/37238658/); 13.8% of SCA families in northern China [PMID: 42474585](https://pubmed.ncbi.nlm.nih.gov/42474585/).

**F011 — Core cerebellar syndrome with pyramidal/bulbar and non-ataxic features.** Parkinsonism is the most common nonataxic phenotype (21.1%) with cognitive/mood involvement across SCAs [PMID: 31523939](https://pubmed.ncbi.nlm.nih.gov/31523939/).

**F012 — Purkinje cells, brainstem, and spinocerebellar tracts damaged (olivopontocerebellar).** Purkinje-cell degeneration is central [PMID: 42113962](https://pubmed.ncbi.nlm.nih.gov/42113962/), with earliest/most severe pathology in posterior vermis [PMID: 38750673](https://pubmed.ncbi.nlm.nih.gov/38750673/).

---

## Mechanistic Model / Interpretation

The unifying model for SCA1 is a **toxic gain-of-function polyglutamine cascade with region-specific amplifiers and multi-cellular participation**. The single upstream lesion — a pure (CAT-uninterrupted) CAG expansion — is necessary and sufficient, but the *rate* and *regional pattern* of downstream damage are tuned by modifiers. Ser776 phosphorylation is the pivotal amplifier: because MSK1 predominates in cerebellum and RSK3 in brainstem, the same mutant protein is stabilized to different degrees in different regions, providing a molecular explanation for **selective vulnerability** (posterior vermis Purkinje cells early; brainstem driving lethality). Downstream, the toxicity is not purely cell-autonomous to Purkinje cells: oligodendrocyte dysfunction alone reproduces core pathology, and RAN-translation products plus autophagy failure add a proteostatic burden shared with other CAG-SCAs.

This model has strong therapeutic logic. Because the cascade is gated by the level of the mutant *ATXN1* transcript/protein, interventions at the most upstream node — ASO-mediated ATXN1 lowering — reverse downstream transcriptomic, neurochemical, behavioral, and survival phenotypes in mice, making it the leading candidate. Kinase inhibition (MSK1/RSK3) offers a region-tunable alternative, while autophagy enhancers, MAO-B inhibition, and glial-directed strategies address parallel branches and could complement upstream lowering.

---

## Evidence Base

| PMID | Contribution | Evidence type |
|------|-------------|---------------|
| [42608759](https://pubmed.ncbi.nlm.nih.gov/42608759/) | ATXN1 CAG expansion cause; gain-of-function + loss-of-function | Review/model |
| [32791425](https://pubmed.ncbi.nlm.nih.gov/32791425/) | Fastest decline; mortality predictors | Natural history |
| [30385727](https://pubmed.ncbi.nlm.nih.gov/30385727/) | ASO rescue in knock-in mice | Model organism |
| [36577402](https://pubmed.ncbi.nlm.nih.gov/36577402/) | ATXN1–CIC complex drives PC pathogenesis | Mechanistic |
| [42113962](https://pubmed.ncbi.nlm.nih.gov/42113962/) | Oligodendrocyte dysfunction; PC axonopathy | Model organism |
| [41422503](https://pubmed.ncbi.nlm.nih.gov/41422503/) | RAN translation shared across CAG-SCAs | Mechanistic |
| [16110192](https://pubmed.ncbi.nlm.nih.gov/16110192/) | CAT interruptions absent in expanded alleles | Human genetics |
| [19429075](https://pubmed.ncbi.nlm.nih.gov/19429075/) | CAG-onset correlation, anticipation, paternal instability | Human cohort |
| [33709453](https://pubmed.ncbi.nlm.nih.gov/33709453/) | MSK1/RSK3 Ser776 kinases; therapeutic rescue | Model organism |
| [35499073](https://pubmed.ncbi.nlm.nih.gov/35499073/) | TG5 regulator of mutant ATXN1 | Cross-species screen |
| [37802886](https://pubmed.ncbi.nlm.nih.gov/37802886/) | RBFOX1 splicing dysregulation | Model organism |
| [37278528](https://pubmed.ncbi.nlm.nih.gov/37278528/) | iPSC/fibroblast phenotypes | In vitro human |
| [42677125](https://pubmed.ncbi.nlm.nih.gov/42677125/) | Biomarkers: SARA, MRI, NfL; premanifest window | Review |
| [41387161](https://pubmed.ncbi.nlm.nih.gov/41387161/) | Treatment landscape; molecular therapy pipeline | Review |
| [37238658](https://pubmed.ncbi.nlm.nih.gov/37238658/) | Prevalence ~1–2/100,000; AD inheritance | Review |
| [42474585](https://pubmed.ncbi.nlm.nih.gov/42474585/) | Regional relative frequency (China) | Cohort |
| [31523939](https://pubmed.ncbi.nlm.nih.gov/31523939/) | Nonataxic phenotypes (parkinsonism, cognition, mood) | Cohort |
| [38750673](https://pubmed.ncbi.nlm.nih.gov/38750673/) | Posterior-vermis selective vulnerability | Model organism |
| [39289638](https://pubmed.ncbi.nlm.nih.gov/39289638/) | Diagnostic methods; interruption status; counseling | Case report |
| [41427729](https://pubmed.ncbi.nlm.nih.gov/41427729/) | KDS2010 (MAO-B) slows decline | Model organism |
| [41226482](https://pubmed.ncbi.nlm.nih.gov/41226482/) | AUTEN autophagy enhancers | Model organism |
| [40988103](https://pubmed.ncbi.nlm.nih.gov/40988103/) | Troriluzole in cerebellar ataxia trials | Preclinical/trial |

---

## Limitations and Knowledge Gaps

1. **Prevalence granularity.** SCA1-specific incidence and geographic prevalence figures beyond the ~1–2/100,000 estimate and relative-frequency cohorts are limited; no dedicated global registry data were available in this investigation.
2. **Human trial evidence.** Nearly all disease-modifying evidence (ASO, kinase inhibition, autophagy enhancers, MAO-B inhibition) is preclinical (mouse/Drosophila/C. elegans/iPSC). No completed SCA1-specific disease-modifying human trial data were reviewed.
3. **Precise repeat thresholds.** Exact CAG cutoffs for full penetrance vs reduced penetrance and the intermediate zone were not exhaustively quantified from primary sources here; interruption status complicates simple length cutoffs.
4. **Epigenetics and quantitative QoL.** Disease-specific epigenetic marks and per-phenotype quality-of-life instrument data for SCA1 were not established.
5. **Sex ratio and life-expectancy figures.** Specific numeric survival/life-expectancy values for SCA1 were not extracted; prognostic statements rely on cross-SCA natural-history data.
6. **Somatic mosaicism.** Somatic repeat instability in target tissues (a factor in other repeat disorders) was not directly characterized for SCA1 here.

---

## Proposed Follow-up Experiments / Actions

1. **Translate ATXN1-lowering ASOs to human trials** with premanifest and early-manifest cohorts, using the biomarker-defined premanifest window (NfL, MRI volumetry/MRS) as early-efficacy endpoints [PMID: 30385727](https://pubmed.ncbi.nlm.nih.gov/30385727/), [PMID: 42677125](https://pubmed.ncbi.nlm.nih.gov/42677125/).
2. **Develop brain-penetrant MSK1/RSK3 (Ser776) kinase inhibitors** and test region-specific dual inhibition, given the demonstrated cerebellar + brainstem rescue [PMID: 33709453](https://pubmed.ncbi.nlm.nih.gov/33709453/).
3. **Quantify CAG length/CAT-interruption genotype–phenotype relationships** in a large multi-ethnic SCA1 cohort to refine penetrance, onset prediction, and counseling thresholds [PMID: 16110192](https://pubmed.ncbi.nlm.nih.gov/16110192/), [PMID: 39289638](https://pubmed.ncbi.nlm.nih.gov/39289638/).
4. **Prospective natural-history biomarker study** combining NfL, advanced MRI, wearable gait sensors, and SARA to power future trials and define minimal detectable change [PMID: 42677125](https://pubmed.ncbi.nlm.nih.gov/42677125/).
5. **Target non-cell-autonomous glial pathology** — test oligodendrocyte myelination rescue (TCF7L2/HTT axis) and astrocytic MAO-B inhibition (KDS2010) as combination adjuncts to ATXN1 lowering [PMID: 42113962](https://pubmed.ncbi.nlm.nih.gov/42113962/), [PMID: 41427729](https://pubmed.ncbi.nlm.nih.gov/41427729/).
6. **Autophagy/RAN-translation modulation** — advance AUTEN-67/-99 and RAN-protein-directed strategies, evaluating whether disrupting ATXN1–CIC binding reduces RAN aggregates in vivo [PMID: 41226482](https://pubmed.ncbi.nlm.nih.gov/41226482/), [PMID: 41422503](https://pubmed.ncbi.nlm.nih.gov/41422503/).
7. **Patient iPSC-based drug screening** leveraging the established dendritic/mitochondrial/network phenotypes for high-content compound screens [PMID: 37278528](https://pubmed.ncbi.nlm.nih.gov/37278528/).

---

*Evidence source types are indicated throughout: human clinical/genetics (cohorts, case reports), model organism (mouse, Drosophila, C. elegans), in vitro human (iPSC/fibroblast), and reviews. All mechanistic and clinical claims are cited to primary PMIDs with verbatim abstract support recorded in the knowledge state.*


## Artifacts

- [OpenScientist final report](Spinocerebellar_Ataxia_Type_1-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Spinocerebellar_Ataxia_Type_1-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 26 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 26 |
| On topic | 18 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 28 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 13 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 8 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0008119` (3 mentions) - the report calls it "if available"; MONDO calls it **spinocerebellar ataxia type 1**
- `HP:0001251` (2 mentions) - the report calls it "Clinical sign"; HP calls it **Ataxia**
- `HP:0001260` (1 mention) - the report calls it "Clinical sign"; HP calls it **Dysarthria**
- `HP:0001272` (1 mention) - the report calls it "Imaging finding"; HP calls it **Cerebellar atrophy**
- `HP:0002015` (1 mention) - the report calls it "Clinical sign"; HP calls it **Dysphagia**
- `HP:0009830` (1 mention) - the report calls it "Clinical sign"; HP calls it **Peripheral neuropathy**
- `HP:0000716` (1 mention) - the report calls it "Behavioral"; HP calls it **Depression**
- `HP:0001300` (1 mention) - the report calls it "Clinical sign"; HP calls it **Parkinsonism**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0100543` (1 mention) - the report calls it "Behavioral/cognitive"; HP calls it **Cognitive impairment**, and lists "Abnormality of cognition" among its other names
- `CL:0000644` (2 mentions) - the report calls it "Bergmann glia"; CL calls it **Bergmann glial cell**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HGNC:10548` - called "ATXN1", "Gene:** *ATXN1"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.
