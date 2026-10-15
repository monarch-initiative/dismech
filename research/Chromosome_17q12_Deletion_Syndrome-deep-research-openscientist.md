---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-09-03T14:40:20.275387'
end_time: '2026-09-03T15:20:38.243766'
duration_seconds: 2417.97
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: chromosome 17q12 deletion syndrome (HNF1B microdeletion, renal cysts
    and diabetes syndrome)
  mondo_id: MONDO:0013797
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
  path: Chromosome_17q12_Deletion_Syndrome-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Chromosome_17q12_Deletion_Syndrome-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** chromosome 17q12 deletion syndrome (HNF1B microdeletion, renal cysts and diabetes syndrome)
- **MONDO ID:** MONDO:0013797 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **chromosome 17q12 deletion syndrome (HNF1B microdeletion, renal cysts and diabetes syndrome)** covering all of the
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

# Chromosome 17q12 Deletion Syndrome (HNF1B Microdeletion / Renal Cysts and Diabetes Syndrome): A Comprehensive Disease Characterization

**MONDO:** MONDO:0013797 · **OMIM:** 614527 (17q12 recurrent deletion syndrome) / 137920 (RCAD, *HNF1B*) · **Orphanet:** ORPHA:261265 (17q12 microdeletion) / ORPHA:93111 (RCAD)
**Category:** Mendelian (autosomal-dominant contiguous-gene microdeletion / single-gene haploinsufficiency)
**Prepared:** 2026-09-03 · Iterations 1–5 (final) · 8 confirmed findings, 35 references reviewed

---

## Summary

Chromosome 17q12 deletion syndrome is a recurrent, autosomal-dominant contiguous-gene microdeletion spanning approximately **1.4–1.8 Mb** at chromosome band 17q12. The deletion is generated by **non-allelic homologous recombination (NAHR)** between flanking low-copy repeats and removes one copy of **HNF1B** (hepatocyte nuclear factor 1 homeobox B) together with roughly **15 neighboring genes** (including *ACACA, ZNHIT3, CCL3L1, PIGW, AATF, DDX52*). Haploinsufficiency of the transcription factor *HNF1B* is the principal driver of the renal, pancreatic, hepatic, genital, and electrolyte phenotypes, while the co-deleted genes contribute the neurodevelopmental and neuropsychiatric burden (developmental delay, autism spectrum disorder, schizophrenia). The disorder is clinically equivalent, at the renal/endocrine level, to intragenic *HNF1B* mutations — together labeled **HNF1B-associated disease** or **Renal Cysts and Diabetes syndrome (RCAD)**, and the diabetes form is **MODY5**.

*HNF1B* is a master regulator of nephron, pancreas, biliary and Müllerian-duct development. It directly transactivates cystic-kidney genes **PKHD1** and **UMOD**, the distal-tubule magnesium gene **FXYD2**, and cooperates with developmental patterning genes (**pax2, wt1, pdx1, shh**) demonstrated in a zebrafish *vhnf1/hnf1b* model. Loss of one functional copy therefore produces a stereotyped multi-organ picture: **renal cysts/dysplasia with progressive tubulointerstitial chronic kidney disease** (CKD stage 3–4 in ~44%, end-stage renal disease in ~21% of adults), **MODY5 diabetes with pancreatic hypoplasia** (usually insulin-requiring, ~79% on insulin at follow-up), **renal magnesium wasting/hypomagnesemia** (50–60%), **genital-tract Müllerian malformations**, **hyperuricemia/gout**, and **liver-enzyme abnormalities**. There is no clear genotype–phenotype correlation, consistent with haploinsufficiency, and expressivity is highly variable with incomplete penetrance.

Population prevalence of the 17q12 deletion is approximately **1 in 4,000 newborns**, with roughly **one-third arising de novo**. Diagnosis relies on chromosomal microarray/CNV sequencing (for the deletion) or *HNF1B* sequencing (for intragenic variants), guided by the validated **HNF1B clinical score** (AUC 0.78; a score <8 rules out disease with negative predictive value >99%). Management is entirely organ-directed and supportive — insulin for diabetes, magnesium repletion, urate-lowering therapy, nephrology/CKD care, and genetic counseling with prenatal and preimplantation testing options. No disease-specific or curative therapy exists.

---

## Key Findings

### Finding 1 — The 17q12 deletion is a recurrent NAHR-mediated CNV encompassing *HNF1B* and ~15 genes

The core lesion is a **recurrent ~1.4–1.8 Mb deletion** at 17q12, mediated by non-allelic homologous recombination between segmental duplications flanking the interval. In a large neurodevelopmental cohort, the deletion was detected in **18/15,749 patients versus 0/4,519 controls**, with follow-up enrichment in autism spectrum disorder (2/1,182) and schizophrenia (4/6,340) versus 0/47,929 controls (corrected p = 7.37×10⁻⁵) ([PMID: 21055719](https://pubmed.ncbi.nlm.nih.gov/21055719/)). The deleted interval harbors *HNF1B* — "the gene responsible for renal cysts and diabetes syndrome (RCAD)" — plus approximately 15 genes, and the authors proposed that "one or more of the 15 genes in the deleted interval is dosage sensitive and essential for normal brain development and function," establishing the contiguous-gene syndrome model.

Reported deletion sizes cluster between **1.4 and 1.9 Mb** across cohorts (e.g., 1.494–1.66 Mb; 1.46 Mb; a prototypical 1.4 Mb interval `arr 17q12(34,850,785_36,248,926)x1`). The genes recurrently cited within the interval include *HNF1B, ACACA, ZNHIT3, CCL3L1, PIGW* (5 OMIM genes) and up to 17 protein-coding genes including *AATF* and *DDX52*. This dual architecture — a single dosage-critical developmental transcription factor (*HNF1B*) plus additional dosage-sensitive neurodevelopmental genes — explains why the deletion phenotype is broader than that of intragenic *HNF1B* variants.

### Finding 2 — Microdeletions, but not reciprocal microduplications, drive the diabetes phenotype

Dosage directionality matters. In UK Biobank (**450,993 individuals**), 11 microdeletions and 106 microduplications at 17q12 were identified; **microdeletions were strongly associated with diabetes**, whereas the reciprocal **microduplications were associated with renal disease but not diabetes** ([PMID: 36109160](https://pubmed.ncbi.nlm.nih.gov/36109160/)). The paper concludes: "We demonstrate 17q12 microdeletions but not microduplications are associated with diabetes in a population-based cohort." This confirms that the diabetes/MODY5 component is specifically a **loss-of-dosage (haploinsufficiency)** phenomenon of *HNF1B*, and it distinguishes the clinical consequences of the reciprocal CNVs at this locus.

### Finding 3 — HNF1B → FXYD2 axis explains renal magnesium wasting

*HNF1B* directly regulates **FXYD2**, the γ-subunit of the Na⁺,K⁺-ATPase, in the **distal convoluted tubule (DCT)**. HNF1B, together with cofactor **PCBD1**, co-stimulates the *FXYD2* promoter, and FXYD2 activity "is instrumental in Mg²⁺ reabsorption in the DCT" ([PMID: 24204001](https://pubmed.ncbi.nlm.nih.gov/24204001/)). Consequently, **50–60% of ADTKD-HNF1B patients develop hypomagnesemia** ([PMID: 26340261](https://pubmed.ncbi.nlm.nih.gov/26340261/)), and the biochemical signature is distinctive: "All patients presented with hypomagnesemia with a high fractional excretion of Mg²⁺ and hypocalciuria." Hypomagnesemia may be the **first clinical manifestation** of HNF1B disease, giving it a Gitelman-like electrolyte profile (hypomagnesemia, hypokalemic alkalosis, hypocalciuria). This provides a mechanistically-defined biomarker for the syndrome.

### Finding 4 — Population prevalence ~1:4,000 newborns, ~one-third de novo

In a large newborn trio study (**12,252 MoBa trios**), the 17q12 deletion prevalence was estimated at **~1:4,000**, in the context of an overall recurrent neurodevelopmental CNV prevalence of ~0.48% (1 in 200) ([PMID: 32778765](https://pubmed.ncbi.nlm.nih.gov/32778765/)). Approximately **34% (20/59) of recurrent NDD CNVs were de novo**. Prenatally, the detection rate among fetuses with urinary tract anomalies was ~6.5% (3/46), and other prenatal series report ~0.36% among fetuses undergoing CNV testing for ultrasound anomalies — of whom the vast majority present with **bilateral hyperechogenic kidneys**. These figures anchor recurrence-risk counseling: an affected parent transmits with 50% probability, but a substantial fraction of index cases are new mutations.

### Finding 5 — Quantitative phenotype frequencies and long-term renal prognosis

The largest adult cohort (**201 adults** with *HNF1B* molecular defects; Dubois-Laforgue 2017) quantifies the mature phenotype ([PMID: 28420700](https://pubmed.ncbi.nlm.nih.gov/28420700/)):

| Phenotype | Frequency | HPO term |
|---|---|---|
| Diabetes mellitus | 159/201 | HP:0000819 |
| Renal cysts | 122/166 (73%) | HP:0000107 |
| CKD stage 3–4 | 75/169 (44%) | HP:0012622 |
| End-stage renal disease | 36/169 (21%) | HP:0003774 |
| Diabetic retinopathy/neuropathy | 46/114 | HP:0000488 / HP:0000762 |
| On insulin at follow-up | 111/140 (79%) | — |

"Chronic kidney disease stages 3-4 (CKD3-4) in 75 of 169 (44%), and end-stage renal disease (ESRD) in 36 of 169 (21%)" and "111 of 140 patients (79%) were treated with insulin at follow-up" quantify the two dominant clinical burdens. Molecularly, whole-gene deletion (i.e., the 17q12 deletion) and intragenic *HNF1B* mutations "each account for ∼50% of all cases of HNF1B-associated disease," and importantly "there is no clear genotype-phenotype correlation, consistent with haploinsufficiency as the disease mechanism" ([PMID: 25536396](https://pubmed.ncbi.nlm.nih.gov/25536396/)). This lack of genotype–phenotype correlation is a defining feature — the deletion and point mutations produce clinically indistinguishable renal/endocrine disease.

### Finding 6 — The HNF1B score rationalizes genetic testing

Because the phenotype is protean, Faguer et al. developed a **17-item HNF1B score** (antenatal discovery, family history, and kidney/pancreas/liver/genital involvement). In a **433-individual cohort with 56 HNF1B cases**, "the HNF1B score efficiently and significantly discriminated between mutated and nonmutated cases (AUC 0.78)," and "the optimal cutoff threshold for the negative predictive value to rule out HNF1B mutations in a suspected individual was 8 (sensitivity 98.2%, specificity 41.1%, and negative predictive value over 99%)" ([PMID: 24897035](https://pubmed.ncbi.nlm.nih.gov/24897035/)). The same work confirms "an autosomal-dominant inheritance, a 50% rate of de novo mutations, and a highly variable phenotype." A score below 8 effectively excludes disease, sparing unnecessary sequencing.

### Finding 7 — HNF1B regulates PKHD1 and UMOD; biallelic loss drives chromophobe RCC

*HNF1B* directly regulates the cystic-kidney genes **PKHD1** (the ARPKD gene) and **UMOD** (uromodulin). In renal tumorigenesis, "biallelic HNF1beta inactivation was found in two of 12 chromophobe renal carcinomas by association of a germline mutation and a somatic gene deletion. In these cases, the expression of PKHD1 … and UMOD …, two genes regulated by HNF1beta, was turned off" ([PMID: 15649945](https://pubmed.ncbi.nlm.nih.gov/15649945/)). This defines a co-regulated **HNF1B–PKHD1–UMOD** transcriptional cluster central to tubular/cystic biology. A broader survey of **130 kidney tumors** found decreased *HNF1B* expression associated with higher grade/stage in clear cell RCC, supporting that "in ccRCC and chRCC it may act in a tumour suppressive fashion" ([PMID: 33051485](https://pubmed.ncbi.nlm.nih.gov/33051485/)). Clinically, this links the germline haploinsufficiency of the syndrome to a theoretical (though not established as high-frequency) renal-tumor predisposition via second-hit somatic inactivation.

### Finding 8 — Zebrafish hnf1b (vhnf1) model recapitulates the syndrome via patterning-gene regulation

The developmental mechanism is directly demonstrated in a model organism. Insertional zebrafish **vhnf1 (hnf1b) mutants** show "formation of kidney cysts, underdevelopment of the pancreas and the liver, and reduction in size of the otic vesicles" — a striking recapitulation of human MODY5/RCAD ([PMID: 11731484](https://pubmed.ncbi.nlm.nih.gov/11731484/)). Mechanistically, "vhnf1 is required for the proper expression of pdx1 and shh (sonic hedgehog) in the gut endoderm, pax2 and wt1 in the pronephric primordial, and valentino (val) in the hindbrain." This places *HNF1B* upstream of the master patterning genes for pancreas (**pdx1**), pronephros/kidney (**pax2, wt1**), and hindbrain (**valentino/mafba**), providing the causal bridge from transcription-factor haploinsufficiency to organ malformation.

---

## Mechanistic Model / Interpretation

### Ordered causal chain (initiating lesion → clinical manifestation)

1. **NAHR between flanking low-copy repeats at 17q12** → **generates a recurrent ~1.4–1.8 Mb heterozygous deletion** (de novo in ~1/3, inherited AD in ~2/3).
2. The deletion **removes one copy of *HNF1B* plus ~15 contiguous genes** → **HNF1B haploinsufficiency** (≈50% dosage of the transcription factor).
3. Reduced HNF1B dosage → **failure to maintain normal transcription of direct target genes** in a tissue-specific manner. This branches:
   - **Kidney branch:** ↓ regulation of *PKHD1*, *UMOD*, and patterning genes *pax2/wt1* → **abnormal nephron/tubule development, tubular dilatation and cyst formation, dysplasia** → **progressive tubulointerstitial fibrosis** → **CKD → ESRD** (*inferred causal chain from direct-target regulation + zebrafish model + human frequencies*).
   - **DCT electrolyte branch:** ↓ HNF1B/PCBD1 co-stimulation of *FXYD2* → **impaired Na,K-ATPase γ-subunit function in the DCT** → **reduced Mg²⁺ reabsorption** → **renal Mg wasting → hypomagnesemia with high fractional Mg excretion and hypocalciuria** (*demonstrated*).
   - **Pancreas branch:** ↓ *pdx1/shh*-dependent pancreatic patterning → **pancreatic (body/tail) hypoplasia** → **β-cell deficiency + exocrine insufficiency** → **MODY5 diabetes, usually insulin-requiring** (*inferred from model + clinical correlation*).
   - **Hepatobiliary branch:** HNF1B loss in biliary/hepatic epithelium → **liver-enzyme elevations, biliary abnormalities** (*observed clinically*).
   - **Genital branch:** ↓ Müllerian-duct development → **uterine/genital-tract malformations (e.g., bicornuate/incomplete uterus), genital anomalies** (*observed clinically*).
   - **Metabolic branch:** tubular dysfunction → **hyperuricemia/gout** (*observed clinically*).
   - **Neurodevelopmental branch (co-deleted genes, not HNF1B):** haploinsufficiency of ≥1 of the other ~15 dosage-sensitive genes → **developmental delay, learning difficulty, autism spectrum disorder, schizophrenia risk** (*inferred; specific gene not resolved*).
4. In a subset of renal epithelial cells, a **somatic second hit inactivating the remaining *HNF1B* allele** → **biallelic HNF1B loss** → **loss of PKHD1/UMOD expression** → **contribution to chromophobe/clear-cell renal carcinoma** (*demonstrated in tumors; population-level cancer risk in syndrome not quantified*).

### Upstream vs downstream

- **Most upstream:** the NAHR deletion and resulting *HNF1B* haploinsufficiency (and co-deletion of neurodevelopmental genes).
- **Intermediate:** dysregulation of direct targets (*PKHD1, UMOD, FXYD2*) and patterning genes (*pax2, wt1, pdx1, shh*).
- **Downstream:** organ malformation (cysts, pancreatic hypoplasia, Müllerian defects), tubular electrolyte handling defects, and progressive fibrosis/CKD.

### Text schematic

```
   NAHR at 17q12 low-copy repeats
              │
   ~1.4–1.8 Mb heterozygous deletion
        ┌─────┴───────────────┐
   HNF1B haploinsufficiency    ~15 co-deleted genes
        │                           │
  ┌─────┼───────┬────────┬──────┐   └─► neurodevelopment:
  ▼     ▼       ▼        ▼      ▼         DD / ASD / schizophrenia
PKHD1  UMOD   FXYD2   pax2/wt1  pdx1/shh
  │     │       │        │        │
 cysts/dysplasia   ↓Mg²⁺     kidney    pancreas
   → CKD → ESRD  reabsorption  malform.  hypoplasia
                    │                      │
              hypomagnesemia          MODY5 diabetes
              (Gitelman-like)        (insulin-requiring)
```

### Ontology annotations

- **Gene:** HNF1B (HGNC:11630; NCBI Gene 6928; UniProt P35680; OMIM 189907)
- **GO biological process:** regionalization (GO:0003002), metanephros development (GO:0001656), pronephros development (GO:0048793), mesonephric tubule development (GO:0072164), endocrine pancreas development (GO:0031018), positive regulation of transcription by RNA polymerase II (GO:0045944), magnesium ion transmembrane transport (GO:1903830).
- **GO cellular component:** nucleus (GO:0005634); basolateral plasma membrane / Na,K-ATPase complex for FXYD2 (GO:0005890).
- **Cell types (CL):** kidney distal convoluted tubule epithelial cell (CL:1000849), kidney collecting duct epithelial cell (CL:1000454), pancreatic A/B cell (CL:0000171 / CL:0000169), hepatocyte (CL:0000182), epithelial cell (CL:0000066).
- **UBERON anatomy:** kidney (UBERON:0002113), renal tubule/nephron (UBERON:0001231 / UBERON:0001285), distal convoluted tubule (UBERON:0001292), pancreas (UBERON:0001264), liver (UBERON:0002107), uterus (UBERON:0000995), Müllerian duct (UBERON:0003890).
- **CHEBI:** magnesium(2+) (CHEBI:18420), uric acid/urate (CHEBI:27226 / CHEBI:17775), D-glucose (CHEBI:17234), insulin (peptide hormone).

---

## Evidence Base

| PMID | Title (abbrev.) | Evidence type | How it supports the model |
|---|---|---|---|
| [21055719](https://pubmed.ncbi.nlm.nih.gov/21055719/) | Deletion 17q12 confers high risk of autism/schizophrenia | Human case-control genomics | Defines recurrent ~1.4 Mb deletion, ~15-gene content, case enrichment (F001) |
| [36109160](https://pubmed.ncbi.nlm.nih.gov/36109160/) | 17q12 microduplications contribute to renal disease not diabetes | Human population cohort (UK Biobank) | Dosage directionality: deletion → diabetes, duplication → renal (F002) |
| [24204001](https://pubmed.ncbi.nlm.nih.gov/24204001/) | PCBD1 mutations cause hypomagnesemia | In vitro / human genetics | Establishes HNF1B/PCBD1→FXYD2 axis for Mg handling (F003) |
| [26340261](https://pubmed.ncbi.nlm.nih.gov/26340261/) | Hypomagnesemia as first manifestation of ADTKD-HNF1B | Human case series | Quantifies hypomagnesemia (50–60%) and its biochemical signature (F003) |
| [30175537](https://pubmed.ncbi.nlm.nih.gov/30175537/) | Renal Mg handling, FXYD2, Na,K-ATPase | Review / mechanism | Mechanistic detail on FXYD2 regulatory role (supports F003) |
| [35894287](https://pubmed.ncbi.nlm.nih.gov/35894287/) | Genetic spectrum of Gitelman-like syndromes | Review | Places HNF1B among Gitelman-like DCT electrolyte disorders (supports F003) |
| [32778765](https://pubmed.ncbi.nlm.nih.gov/32778765/) | Population prevalence of recurrent CNVs in newborns | Human newborn trios | Prevalence ~1:4,000; ~34% de novo (F004) |
| [28420700](https://pubmed.ncbi.nlm.nih.gov/28420700/) | 201 adults with HNF1B — long-term prognosis | Human clinical cohort | Quantitative phenotype frequencies, renal/diabetes prognosis (F005) |
| [25536396](https://pubmed.ncbi.nlm.nih.gov/25536396/) | HNF1B disease — expanding spectrum | Review | ~50/50 deletion vs intragenic; haploinsufficiency, no genotype-phenotype correlation (F005) |
| [24897035](https://pubmed.ncbi.nlm.nih.gov/24897035/) | HNF1B score for patient selection | Human diagnostic study | Score AUC 0.78; cutoff 8, NPV >99% (F006) |
| [15649945](https://pubmed.ncbi.nlm.nih.gov/15649945/) | Germline HNF1α/β mutations in RCC | Human tumor genetics | Biallelic HNF1B loss in chromophobe RCC; PKHD1/UMOD regulation (F007) |
| [33051485](https://pubmed.ncbi.nlm.nih.gov/33051485/) | HNF1B in 130 kidney tumors | Human tumor genomics | Tumor-suppressive role in ccRCC/chRCC (F007) |
| [11731484](https://pubmed.ncbi.nlm.nih.gov/11731484/) | Zebrafish vhnf1 regulates gut/pronephros/hindbrain | Model organism | Phenotype recapitulation + downstream patterning targets (F008) |
| [20378824](https://pubmed.ncbi.nlm.nih.gov/20378824/) | Reduced Notch → renal cysts, microadenomas | Mouse model | Contextual: cyst/tumor biology intersecting HNF1B (TCF2) pathway |
| [30525249](https://pubmed.ncbi.nlm.nih.gov/30525249/) | Acetylation drives HNF1β stability | In vitro | Protein-level regulation of HNF1B stability (mechanistic detail) |

Multiple recent case reports ([PMID: 41924323](https://pubmed.ncbi.nlm.nih.gov/41924323/), [38432894](https://pubmed.ncbi.nlm.nih.gov/38432894/), [38044981](https://pubmed.ncbi.nlm.nih.gov/38044981/), [41694676](https://pubmed.ncbi.nlm.nih.gov/41694676/), [37799485](https://pubmed.ncbi.nlm.nih.gov/37799485/)) corroborate the multi-organ spectrum including hyperuricemia, hypomagnesemia, muscle-mass loss, nephrocalcinosis, and elevated liver enzymes (MODY5). Prenatal series ([PMID: 35232906](https://pubmed.ncbi.nlm.nih.gov/35232906/), [38957807](https://pubmed.ncbi.nlm.nih.gov/38957807/), [37212013](https://pubmed.ncbi.nlm.nih.gov/37212013/), [32219821](https://pubmed.ncbi.nlm.nih.gov/32219821/), [41999034](https://pubmed.ncbi.nlm.nih.gov/41999034/)) consistently identify **bilateral hyperechogenic/cystic kidneys** as the dominant prenatal presentation and confirm chromosomal microarray/CNV-seq as the pivotal diagnostic tool. A novel HNF1B-disrupting **inversion** ([PMID: 41703530](https://pubmed.ncbi.nlm.nih.gov/41703530/)) and an intragenic hotspot deletion p.(Gly239del) ([PMID: 31498910](https://pubmed.ncbi.nlm.nih.gov/31498910/)) broaden the variant spectrum.

---

## Section-by-Section Synthesis

### 1. Disease Information
17q12 deletion syndrome is a recurrent contiguous-gene microdeletion causing a multisystem disorder dominated by renal, endocrine (diabetes), and neurodevelopmental features. **Identifiers:** MONDO:0013797; OMIM 614527 (deletion) and 137920 (RCAD); Orphanet ORPHA:261265 / ORPHA:93111; MeSH aligns with "Chromosome Deletion" + "HNF1B." **Synonyms:** HNF1B microdeletion syndrome; Renal Cysts and Diabetes syndrome (RCAD); MODY5; HNF1B-associated disease; ADTKD-HNF1B (when tubulointerstitial). Information derives from **aggregated disease-level resources** (OMIM/Orphanet) and **individual clinical cohorts/case reports**, not EHR-scale phenotyping.

### 2. Etiology
**Primary cause:** heterozygous 17q12 deletion (NAHR-mediated) or, in ~50% of HNF1B-disease cases, intragenic *HNF1B* variants. **Genetic risk:** essentially the deletion/variant itself; there are no well-established susceptibility modifier loci. **Environmental risk factors, protective factors, and gene-environment interactions are not established** for this Mendelian disorder — onset and organ involvement track the germline lesion, not exposures. De novo occurrence (~1/3 of deletions; ~50% of intragenic variants) means absence of family history does not exclude the diagnosis.

### 3. Phenotypes
Key phenotypes with HPO suggestions and frequencies (from F003, F005): renal cysts (HP:0000107, 73%), CKD (HP:0012622, ~44% stage 3–4), ESRD (HP:0003774, ~21%), diabetes mellitus/MODY (HP:0000819 / HP:0004904, majority), hypomagnesemia (HP:0002917, 50–60%), pancreatic hypoplasia (HP:0002983), Müllerian/uterine malformation (HP:0000130 / HP:0000132), hyperuricemia/gout (HP:0002149 / HP:0001997), elevated liver enzymes (HP:0002910), developmental delay (HP:0001263), autism (HP:0000717), and hypocalciuria (HP:0003169). **Onset spans prenatal (hyperechogenic kidneys) through childhood/adult (MODY5 typically diagnosed in adolescence/early adulthood).** Severity and progression are **highly variable** with incomplete penetrance; renal disease is typically **progressive**. Quality-of-life impact is driven chiefly by CKD/dialysis burden, insulin-dependent diabetes, and (in deletion cases) neurodevelopmental/psychiatric morbidity; formal EQ-5D/SF-36 data specific to the syndrome were not identified.

### 4. Genetic/Molecular Information
**Causal gene:** *HNF1B* (HGNC:11630; OMIM 189907). **Variant classes:** whole-gene deletion (the 17q12 CNV, ~50%), and intragenic pathogenic/likely-pathogenic variants (missense, nonsense, frameshift, splice, in-frame deletions such as p.(Gly239del) in the DNA-binding domain hotspot; also point substitutions e.g. C295R) per ACMG/AMP. A novel **inversion disrupting HNF1B** (GRCh38:17:g.36934029_37729559inv) has also been reported. **Functional consequence:** loss of function → haploinsufficiency; **no clear genotype–phenotype correlation.** **Origin:** germline (frequently de novo). **Chromosomal abnormality:** recurrent 17q12 interstitial deletion, ~1.4–1.8 Mb. **Modifier genes/epigenetics:** not established, though HNF1β protein stability is modulated post-translationally by acetylation ([PMID: 30525249](https://pubmed.ncbi.nlm.nih.gov/30525249/)).

### 5. Environmental Information
Not applicable as a cause. No toxin, infectious agent, or lifestyle factor is established in disease causation. Standard diabetes/CKD lifestyle management applies to complication control but does not modify the germline etiology.

### 6. Mechanism / Pathophysiology
Presented as the ordered causal chain above. Core: *HNF1B* haploinsufficiency → dysregulation of direct targets **PKHD1, UMOD, FXYD2** and patterning genes **pax2, wt1, pdx1, shh** → renal cysts/dysplasia + tubulointerstitial fibrosis, DCT magnesium wasting, pancreatic hypoplasia, and Müllerian defects; co-deleted genes add neurodevelopmental risk. Molecular/omics-specific profiling of the syndrome (transcriptomics, proteomics, single-cell) is limited; the strongest mechanistic evidence is transcription-factor–target regulation plus the zebrafish model.

### 7. Anatomical Structures Affected
**Primary organs:** kidney (UBERON:0002113; bilateral, often symmetric), pancreas (UBERON:0001264), liver/biliary tract (UBERON:0002107), female genital tract/uterus (UBERON:0000995). **Body systems:** urinary, endocrine, hepatobiliary, reproductive, and (via co-deleted genes) central nervous system. **Tissue/cell level:** renal tubular epithelium — especially **DCT epithelial cells** (CL:1000849) and collecting duct — pancreatic islet and acinar cells, hepatocytes/cholangiocytes, Müllerian-duct epithelium. **Subcellular:** nucleus (transcription factor, GO:0005634); DCT basolateral Na,K-ATPase complex (FXYD2, GO:0005890). **Lateralization:** renal involvement is typically **bilateral**.

### 8. Temporal Development
**Onset:** congenital/prenatal renal structural abnormality (hyperechogenic kidneys detectable on second-trimester ultrasound) through adolescent/adult-onset diabetes. **Course:** renal disease is chronic and **progressive** toward CKD/ESRD; diabetes is progressive and usually insulin-requiring. **Critical periods:** fetal organogenesis (kidney/pancreas/Müllerian development) is the vulnerable window; postnatally, management targets complication prevention. Disease is **lifelong**; no spontaneous remission.

### 9. Inheritance and Population
**Inheritance:** autosomal dominant; **~50% de novo** for intragenic variants and **~1/3 de novo** for deletions. **Penetrance:** incomplete and variable; **expressivity highly variable** even within families (multigenerational reports show renal cysts, stones, diabetes, pancreatic dysfunction in different relatives). **Prevalence:** ~1:4,000 newborns for the deletion; HNF1B disease overall is a leading monogenic cause of developmental kidney disease. **Sex:** both sexes affected; females may present additionally with Müllerian anomalies. Founder effects, consanguinity, and anticipation are **not features** (dominant, often de novo).

### 10. Diagnostics
**Genetic testing is definitive:** chromosomal microarray (CMA)/CNV-seq detects the deletion; *HNF1B* sequencing (single-gene or panel) detects intragenic variants; whole-genome sequencing can resolve complex structural variants (e.g., inversion). **Clinical labs/biomarkers:** hypomagnesemia with high fractional Mg excretion + hypocalciuria (distinctive); hyperuricemia; elevated liver enzymes; abnormal glucose/HbA1c; anti-GAD negativity helps distinguish MODY5 from type 1 diabetes. **Imaging:** renal ultrasound/MRI showing bilateral cysts, hyperechogenic/dysplastic kidneys; pancreatic imaging showing body/tail hypoplasia. **Clinical criterion/tool:** the **HNF1B score** (cutoff 8; NPV >99%) selects candidates for testing. **Differential diagnosis:** ADPKD, ARPKD (differentiated by targeted sequencing and family pattern), other ADTKD subtypes, Gitelman syndrome (for the electrolyte picture), and type 1 diabetes (for MODY5). **Screening:** prenatal CMA for fetuses with bilateral echogenic kidneys; cascade family testing.

### 11. Outcome/Prognosis
**Renal:** ~44% reach CKD 3–4 and ~21% ESRD in adulthood — the principal driver of morbidity and the main determinant of life expectancy (dialysis/transplant needs). **Diabetes:** usually insulin-requiring (~79%), with risk of microvascular complications. **Overall mortality** is not sharply elevated with modern renal replacement/diabetes care, but the disorder is chronic and lifelong. **Prognostic factors:** degree of renal impairment at diagnosis, rate of eGFR decline, and diabetes control. There is a theoretical renal-tumor consideration (chromophobe/clear-cell RCC via biallelic HNF1B loss), though population-level cancer risk in the syndrome is not established.

### 12. Treatment
**No disease-specific or curative therapy.** Management is organ-directed and supportive:
- **Diabetes/MODY5:** insulin is the mainstay (NCIT: Insulin Therapy); a subset respond to sulfonylureas/repaglinide (~29/51 tested in the 201-adult cohort), but most are insulin-dependent at follow-up.
- **Electrolytes:** oral/IV **magnesium** repletion for hypomagnesemia (CHEBI:18420); potassium citrate for stones/tubular acidosis.
- **Hyperuricemia/gout:** urate-lowering therapy (e.g., allopurinol; NCIT: Allopurinol).
- **CKD:** standard nephroprotection, and renal replacement (dialysis/transplant) for ESRD (NCIT: Renal Dialysis, Kidney Transplantation).
- **Structural/genital anomalies:** surgical correction as indicated.
- **Neurodevelopmental:** educational and behavioral support.
No gene therapy, RNA therapy, or targeted molecular therapy exists; pharmacogenomics is limited to the sulfonylurea-responsiveness observation.

### 13. Prevention
No primary prevention (germline etiology). **Secondary prevention:** prenatal detection (CMA for echogenic kidneys), cascade family testing, and early metabolic/renal surveillance. **Genetic counseling** is central — 50% transmission risk from an affected parent, high de novo rate, variable expressivity; **preimplantation genetic testing (PGT)** and prenatal diagnosis are available for at-risk families. **Tertiary prevention:** aggressive CKD and diabetes complication management.

### 14. Other Species / Natural Disease
**Orthologs:** zebrafish *hnf1b/vhnf1*, mouse *Hnf1b* (NCBI Gene 21410). No prominent naturally-occurring companion-animal disease is catalogued; relevance is chiefly experimental. Evolutionary conservation of HNF1B's developmental role (kidney/pancreas/hindbrain patterning) is strong across vertebrates.

### 15. Model Organisms
- **Zebrafish** *vhnf1/hnf1b* insertional mutant — recapitulates kidney cysts, pancreatic/hepatic hypoplasia, reduced otic vesicles; reveals downstream targets *pdx1, shh, pax2, wt1, valentino* ([PMID: 11731484](https://pubmed.ncbi.nlm.nih.gov/11731484/)). Strong developmental recapitulation; limitation — does not model adult-onset diabetes progression or human neuropsychiatric features.
- **Mouse** *Hnf1b* conditional/knockout models — used to study nephrogenesis and cystogenesis; homozygous null is embryonic lethal, requiring conditional/tissue-specific approaches. A reduced-Notch mouse model produced renal cysts and papillary microadenomas with links to TCF2/HNF1β biology ([PMID: 20378824](https://pubmed.ncbi.nlm.nih.gov/20378824/)).
- **Cellular/in vitro** — HNF1β-expressing lines (ES2, HEPG2, HK2) used to study protein stability/acetylation and target-gene regulation.

---

## Limitations and Knowledge Gaps

1. **Neurodevelopmental gene not resolved.** The specific dosage-sensitive gene(s) among the ~15 co-deleted loci responsible for autism/schizophrenia/developmental delay remain unidentified; the contiguous-gene model is supported statistically but not gene-resolved.
2. **No genotype–phenotype correlation** limits prognostic precision — the deletion vs point mutation, and specific variants, do not reliably predict organ burden or severity.
3. **Penetrance/expressivity quantitatively uncertain.** Incomplete penetrance is documented, but robust penetrance estimates per organ system by variant type are lacking.
4. **Omics profiling of the human syndrome is sparse** — transcriptomic/proteomic/single-cell datasets specific to HNF1B-deleted human kidney/pancreas are limited; most mechanism is inferred from target-gene regulation and model organisms.
5. **Cancer risk unquantified.** Biallelic HNF1B loss occurs in chromophobe RCC, but the lifetime renal-tumor risk for germline 17q12-deletion carriers is not established.
6. **Quality-of-life and mortality data** specific to the syndrome (as opposed to CKD/diabetes generally) are limited; no syndrome-specific EQ-5D/SF-36 datasets were identified.
7. **Ascertainment bias.** Much of the cohort data comes from nephrology/genetics referral populations, likely over-representing severe renal phenotypes.

## Proposed Follow-up Experiments / Actions

1. **Resolve the neurodevelopmental driver** via dosage analysis of individual 17q12 genes (e.g., CRISPR dosage models, or association testing of atypical smaller deletions) to pinpoint the ASD/schizophrenia gene(s).
2. **Prospective natural-history registry** stratified by variant type (deletion vs intragenic) to derive organ-specific penetrance, eGFR-decline trajectories, and mortality — addressing the genotype–phenotype and prognosis gaps.
3. **Single-cell/spatial transcriptomics** of HNF1B-deficient human kidney organoids and patient biopsies to map cell-type-specific dysregulation of PKHD1/UMOD/FXYD2 and validate the causal chain in human tissue.
4. **Quantify renal-tumor risk** through long-term surveillance imaging in a large carrier cohort and molecular characterization of any tumors for second-hit HNF1B inactivation.
5. **Pharmacogenomic trial of sulfonylurea/repaglinide responsiveness** to identify predictors of insulin-sparing response in HNF1B-MODY5.
6. **Systematic QoL assessment** (EQ-5D/PROMIS) across renal, endocrine, and neurodevelopmental domains to inform holistic management.
7. **Magnesium-repletion outcome study** to determine whether early correction of hypomagnesemia alters renal or metabolic trajectory.

---

*Report compiled from 8 confirmed findings and 35 reviewed papers over a 5-iteration autonomous investigation. Evidence types span human clinical cohorts, human population genomics, tumor genetics, in vitro studies, and model-organism (zebrafish, mouse) work, as annotated in the Evidence Base.*


## Artifacts

- [OpenScientist final report](Chromosome_17q12_Deletion_Syndrome-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Chromosome_17q12_Deletion_Syndrome-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 27 |
| Resolved | 27 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 5 |
| Quoted claims found in source | 3 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 27 |
| On topic | 22 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:24204001` *(abstract only)*: "is instrumental in Mg²⁺ reabsorption in the DCT"
  - closest text in source: "Overexpression in a human kidney cell line showed that wild-type PCBD1 binds HNF1B to costimulate the FXYD2 promoter, the activity of which is instrumental in Mg(2+) reabsorption in the DCT"
- `PMID:15649945` *(abstract only)*: "biallelic HNF1beta inactivation was found in two of 12 chromophobe renal carcinomas by association of a germline mutation and a somatic gene deletion. In these cases, the expression of PKHD1 … and UMOD …, two genes regulated by HNF1beta, was turned off"
  - closest text in source: "Biallelic HNF1beta inactivation was found in two of 12 chromophobe renal carcinomas by association of a germline mutation and a somatic gene deletion"
