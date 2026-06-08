# H3Africa

Reviewed: 2026-05-29

## Why This Is Mechanistically Valuable

H3Africa is mechanistically important because it helps prevent a common failure
mode in disease interpretation: treating European-biased genomic resources as
universal. The Common Fund global health page describes H3Africa as building
African scientific capacity to study genomics and environmental determinants of
disease and use that knowledge to improve African population health. Fogarty
describes H3Africa as a partnership among NIH, the African Society of Human
Genetics, and Wellcome/AESA.

For dismech, H3Africa should enhance population-aware curation without turning
ancestry into a mechanism by itself.

## Dismech Interpretation Pattern

Use H3Africa to add population, environment, and variant-context layers:

`variant or exposure observed in African cohorts -> gene or pathway mechanism
supported by biology -> disease risk, progression, treatment response, or
phenotype in a population context`

Ancestry is context. The mechanism remains the gene, pathway, cell type,
exposure, pathogen, or tissue process.

## Concrete Implementation Plan

**Mode:** teach dismech evidence context. H3Africa should teach dismech to
separate ancestry, geography, environment, pathogen exposure, and access-to-care
context from the actual biological mechanism.

**Required datasets and access path:**

- Use the H3Africa Data and Biospecimen Catalogue:
  https://catalog.h3africa.org/ and its guide:
  https://h3abionet.github.io/catalogue/.
- Use H3ABioNet's H3Africa catalogue page:
  https://www.h3abionet.org/h3africa-catalogue/. It states that the catalogue
  identifies datasets, EGA accession numbers, and biospecimen storage locations,
  and that access is controlled by the Data and Biospecimen Access Committee
  (DBAC).
- Treat most individual-level genomic and phenotype data as controlled access.
  Use catalogue metadata and publications for planning; use EGA/DBAC workflows
  only with approved access.
- For dismech curation, capture accession, cohort/population description,
  phenotype, sequencing/genotyping assay, and data use limitations, but never
  store individual-level genotype or phenotype data.

**Tools and environment:**

- Metadata curation can be done with the catalogue export plus Python
  `pandas`.
- Approved genomic analysis would use standard tools such as PLINK, Hail,
  BGEN/VCF tooling, EGA download client, and ancestry-aware association or
  fine-mapping workflows.
- Variant interpretation should use HGNC canonical transcript resources,
  ClinVar where relevant, gnomAD
  ancestry frequencies as context, and disease-specific publications. Do not
  infer mechanism from allele frequency alone.

**Curation targets:**

- `Chronic_Kidney_Disease` and `Focal_Segmental_Glomerulosclerosis`: APOL1 risk
  alleles, podocyte injury, proteinuria, glomerulosclerosis, and CKD
  progression.
- `Essential_Hypertension`: vascular resistance, RAAS, salt handling,
  inflammation, and environmental context.
- `Type_2_Diabetes_Mellitus`: African cohort variant interpretation and
  cardiometabolic environmental modifiers.
- `Tuberculosis`, `Acquired_Immunodeficiency_Syndrome`, `Sickle_Cell_Disease`,
  and `Malaria`: host-pathogen and host-genotype mechanisms with population
  context.

**Code to write:**

- Add `src/dismech/commonfund/h3africa.py` to turn catalogue metadata into a
  study manifest with EGA accession, phenotype, country/region summary,
  assay type, access route, and candidate dismech disease.
- Add `scripts/h3africa_context_audit.py` to scan YAML for ancestry language
  and flag any pathophysiology node where ancestry is written as if it were the
  causal mechanism.
- Add schema-review notes for population context, cohort geography, data use
  limitations, and controlled-access repository fields.

**Graduate-student first pass:**

1. Search the catalogue for kidney disease/APOL1, hypertension, diabetes, HIV,
   TB, sickle cell, and malaria datasets; record accessions and access status.
2. Pick one disease and write a two-column table: population/context facts
   versus biological mechanism claims.
3. Add only the biological mechanism claims to pathophysiology; keep ancestry,
   country, and cohort as evidence context or dataset metadata.

## Dismech Disease and Mechanism Exemplars

| Disease | Current or candidate mechanism | How H3Africa helps |
|---------|--------------------------------|--------------------|
| `Chronic_Kidney_Disease` | Curated nodes: `Nephron Loss`, `Glomerulosclerosis`, `Tubulointerstitial Fibrosis`, `RAAS Activation`; genetic factor `APOL1` | Strong pilot for ancestry-aware risk interpretation, especially APOL1-associated kidney disease mechanisms and progression. |
| `Focal_Segmental_Glomerulosclerosis` | Current disease file exists | Candidate addition: APOL1 risk variant -> podocyte injury -> segmental sclerosis -> proteinuria and CKD progression. |
| `Essential_Hypertension` | Curated nodes: `Vascular Resistance`, `Renin-Angiotensin-Aldosterone System Dysregulation`, `Sympathetic Nervous System Overactivity`, `Immune and Inflammatory Activation`, `Oxidative Stress` | Use African cohort data to refine gene-environment and salt/vascular mechanisms without reducing hypertension to ancestry. |
| `Type_2_Diabetes_Mellitus` | Curated nodes: `Insulin Resistance`, `Beta Cell Dysfunction`, `Hepatic Glucose Overproduction`, `Mitochondrial Dysfunction and Oxidative Stress` | H3Africa can improve non-European variant interpretation and environmental context for metabolic disease. |
| `Acquired_Immunodeficiency_Syndrome` | Curated nodes: `CD4 T-cell Depletion`, `Immune System Collapse`, `CNS Reservoir and Neuroinflammation`, `Host Restriction Factor Defense` | Population-specific host variation and co-infection context can refine HIV progression and restriction factor mechanisms. |
| `Tuberculosis` | Current disease file exists | Candidate additions: host macrophage immunity, granuloma formation, HIV co-infection, and population/environmental susceptibility context. |
| `Sickle_Cell_Disease` | Curated nodes: `Hemoglobin Polymerization`, `Red Blood Cell Sickling`, `Vaso-Occlusion`, `Chronic Hemolysis`, `Chronic Organ Damage` | H3Africa can strengthen modifier-gene, malaria-selection, and clinical heterogeneity interpretation. |
| `Malaria` | Current disease file exists | Candidate additions: erythrocyte invasion, hemolysis, inflammatory endothelial activation, and host genetic protection mechanisms. |

## High-Value Curation Work

- Add H3Africa-backed datasets to `Chronic_Kidney_Disease`,
  `Essential_Hypertension`, `Type_2_Diabetes_Mellitus`, `Tuberculosis`,
  `Acquired_Immunodeficiency_Syndrome`, `Sickle_Cell_Disease`, and `Malaria`
  when stable study accessions are selected.
- Add a population-context curation rule: population can qualify an evidence
  claim, but the pathophysiology node should still name the causal biological
  process.
- Prioritize H3Africa for genes and variants with different frequencies,
  linkage disequilibrium, or effect sizes in African cohorts.
- Use H3Africa with GTEx only carefully, because GTEx tissue-expression data is
  not a substitute for ancestry-matched disease cohorts.

## Fit for RFA-RM-26-017

Best partner datasets:

- H3Africa + GTEx: variant interpretation with tissue-expression plausibility.
- H3Africa + Metabolomics Workbench: population-aware metabolic signatures.
- H3Africa + HMP/iHMP: microbiome and infectious/environmental interactions.
- H3Africa + UDN: rare disease diagnosis and variant interpretation in
  underrepresented populations.

## Sources

- NIH Common Fund global health/H3Africa: https://commonfund.nih.gov/globalhealth/
- Fogarty H3Africa page: https://www.fic.nih.gov/Funding/Pages/collaborations-h3africa.aspx
- H3ABioNet: https://h3abionet.org/
- H3Africa catalogue: https://catalog.h3africa.org/
- H3ABioNet H3Africa catalogue page: https://www.h3abionet.org/h3africa-catalogue
