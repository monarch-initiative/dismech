# Metabolomics Workbench

Reviewed: 2026-05-29

## Why This Is Mechanistically Valuable

Metabolomics Workbench is valuable for dismech because metabolites are often
the closest observable readout of a disrupted mechanism. The NIH Common Fund
Metabolomics program established the National Metabolomics Data Repository
(NMDR), RefMet nomenclature, protocols, standards, training resources, and
analysis tools. The Workbench now exposes thousands of metabolomics studies
across cells, tissues, organisms, diseases, treatments, and experimental
conditions.

For dismech, the main opportunity is to move from "this metabolite is altered"
to a causal or interpretive chain: altered enzyme, transport process, microbial
function, diet, drug, or tissue injury -> altered metabolite abundance ->
pathway flux or toxic accumulation -> phenotype, biomarker, or treatment
response.

## Dismech Interpretation Pattern

Use Metabolomics Workbench as a biochemical mechanism layer:

`gene, enzyme, microbe, diet, drug, or tissue injury -> metabolite shift ->
pathway readout or toxic intermediate -> cellular process -> disease phenotype,
biomarker, or treatment-response marker`

Normalize names through RefMet first, then map to CHEBI or other ontology
identifiers where possible. Treat untargeted features as lower confidence until
compound identity is clear.

## Concrete Implementation Plan

**Mode:** teach biochemical mechanism curation and benchmark metabolite-name
normalization. Metabolomics Workbench should teach dismech how to connect
metabolite evidence to enzyme, transport, microbial, diet, drug, or tissue
injury mechanisms.

**Required datasets and access path:**

- Use Metabolomics Workbench data search:
  https://www.metabolomicsworkbench.org/data/ and REST API:
  https://www.metabolomicsworkbench.org/tools/mw_rest.php.
- Use the REST service for reproducible queries. It provides study metadata,
  experimental results, disease-associated study search, named metabolites,
  RefMet lookup, and download of analysis result tables.
- Normalize metabolite names through RefMet first:
  https://www.metabolomicsworkbench.org/databases/refmet/index.php, then map to
  CHEBI/HMDB/KEGG/PubChem where exact identifiers are available.
- Prefer studies with named metabolites and clear biospecimen/disease metadata.
  Untargeted feature tables without confident annotation should remain
  candidate findings, not mechanism evidence.

**Tools and environment:**

- Python `requests`, `pandas`, and `duckdb` for REST harvesting and local
  manifests; R/Bioconductor or MetaboAnalyst only after selected studies are
  downloaded.
- XCMS/MS-DIAL/mzML tooling only if reprocessing raw MS data is needed. For an
  R03-scale dismech pilot, processed tables are sufficient.
- RefMet-to-CHEBI normalization with manual review for ambiguous lipid names,
  adducts, and isomeric species.

**Curation targets:**

- Clean biochemical pilots: `Alkaptonuria`, `MCAD_Deficiency`,
  `VLCAD_Deficiency`, `Mitochondrial_Trifunctional_Protein_Deficiency`, and
  `3-Hydroxy-3-Methylglutaric_Aciduria`.
- Complex disease pilots: `Type_2_Diabetes_Mellitus`, `Crohn_Disease`,
  `Ulcerative_Colitis`, `Sickle_Cell_Disease`, and `Stargardt_Disease`.
- For each disease, identify one mechanism node where a metabolite directly
  reports pathway flux or toxic accumulation.

**Code to write:**

- Add `src/dismech/commonfund/metabolomics_workbench.py` with REST helpers for
  disease, study, analysis, datatable, named metabolite, and RefMet lookups.
- Add `scripts/metabolomics_disease_manifest.py` to produce candidate dataset
  entries with study id, analysis id, biospecimen, disease, assay, named
  metabolites, RefMet names, CHEBI candidates, and dismech mechanism target.
- Add tests using fixed REST response fixtures so the pipeline is reproducible
  without live API dependence.

**Graduate-student first pass:**

1. Query the REST API for one inborn error and one complex disease, then choose
   two studies with named metabolites and clear biospecimen metadata.
2. Normalize 20 metabolites through RefMet and CHEBI. Record unresolved names
   rather than guessing.
3. For each metabolite, write whether it is toxic accumulation, pathway flux,
   microbial output, diet/drug exposure, or nonspecific biomarker.

## Dismech Disease and Mechanism Exemplars

| Disease | Current or candidate mechanism | How Metabolomics Workbench helps |
|---------|--------------------------------|----------------------------------|
| `Alkaptonuria` | Curated nodes: `HGD molecular function deficiency`, `Homogentisic acid accumulation and oxidation`, `Ochronotic connective tissue degeneration`, plus biomarker `Elevated urinary homogentisic acid` | This is the cleanest metabolite-to-mechanism pilot. Workbench/RefMet can normalize homogentisic acid and downstream tyrosine-pathway metabolites for biochemical evidence and treatment response to nitisinone. |
| `MCAD_Deficiency` | Curated nodes: `ACADM molecular function deficiency`, `Impaired medium-chain fatty acid beta-oxidation`, `Hypoketotic hypoglycemia mechanism`, `Toxic metabolite accumulation`, biomarkers including `C8 acylcarnitine` and `Urinary dicarboxylic acids` | Use metabolomics datasets as evidence for acylcarnitine and organic-acid signatures that connect enzyme deficiency to hypoketotic hypoglycemia and crisis risk. |
| `VLCAD_Deficiency` | Curated nodes: `Impaired very-long-chain fatty acid beta-oxidation`, `Lipotoxic metabolite accumulation`, `Secondary mitochondrial dysfunction and OXPHOS impairment`, `Oxidative stress and glutathione vulnerability` | Workbench can support long-chain acylcarnitine profiles, oxidative stress readouts, and exercise/catabolic stress signatures. |
| `Mitochondrial_Trifunctional_Protein_Deficiency` | Curated nodes: `HADHA/HADHB molecular function deficiency in mitochondrial trifunctional protein`, `Impaired mitochondrial long-chain fatty acid beta-oxidation`, `Uncoupling of cardiac oxidative phosphorylation by long-chain 3-hydroxy fatty acids` | Metabolite profiles can make the link from HADHA/HADHB variants to long-chain 3-hydroxyacylcarnitines, cardiomyopathy, neuropathy, and rhabdomyolysis explicit. |
| `Type_2_Diabetes_Mellitus` | Curated nodes: `Insulin Resistance`, `Beta Cell Dysfunction`, `Hepatic Glucose Overproduction`, `Mitochondrial Dysfunction and Oxidative Stress`, `Incretin Axis Dysfunction` | Use plasma, muscle, liver, and microbiome-linked metabolomics to separate insulin-resistance markers from mitochondrial, lipid, amino acid, and bile-acid signatures. |
| `Crohn_Disease` and `Ulcerative_Colitis` | Curated nodes include `Microbiome Imbalance`, `Intestinal Barrier Dysfunction`, `Loss of Keystone SCFA Producers`, `Decreased Butyrate Production`, `Impaired Colonocyte Energy Metabolism`, `NLRP3 Inflammasome-Mediated Pyroptosis` | Pair Workbench with HMP/iHMP to represent microbial metabolite mechanisms rather than taxonomy-only dysbiosis. |
| `Stargardt_Disease` | Curated nodes: `ABCA4 transporter dysfunction`, `Retinoid-adduct retention and bisretinoid precursor formation`, `Lipofuscin and A2E accumulation in RPE`, `RPE endo-lysosomal dysfunction` | A candidate metabolomics-focused extension can track retinoid, bisretinoid, lipid, and oxidative damage readouts. |
| `Sickle_Cell_Disease` | Curated nodes: `Hemoglobin Polymerization`, `Red Blood Cell Sickling`, `Vaso-Occlusion`, `Chronic Hemolysis`, `Chronic Organ Damage`, `Pain Crises` | Add metabolite evidence for hemolysis, oxidative stress, arginine/nitric-oxide metabolism, and ischemia-reperfusion biology. |

## High-Value Curation Work

- Add a metabolite evidence pattern for disorder YAML: metabolite name,
  normalized RefMet name, CHEBI when available, biospecimen, direction of
  change, assay type, and mechanism node supported.
- Start with inborn errors where current dismech entries already have strong
  biochemical nodes: `Alkaptonuria`, `MCAD_Deficiency`, `VLCAD_Deficiency`,
  `Mitochondrial_Trifunctional_Protein_Deficiency`, and
  `3-Hydroxy-3-Methylglutaric_Aciduria`.
- Create a second pilot for complex disease metabolomics using
  `Type_2_Diabetes_Mellitus`, `Crohn_Disease`, `Ulcerative_Colitis`, and
  `Sickle_Cell_Disease`.
- Use metabolomics as mechanism support or biomarker evidence, not as causal
  proof unless the underlying study perturbs the pathway or is supported by
  genetic, model, or treatment-response evidence.

## Fit for RFA-RM-26-017

Best partner datasets:

- Metabolomics Workbench + HMP/iHMP: host-microbiome-metabolite mechanisms.
- Metabolomics Workbench + MoTrPAC: exercise-responsive metabolite transducers.
- Metabolomics Workbench + UDN: rare metabolic diagnosis and pathway rescue.
- Metabolomics Workbench + GTEx/HuBMAP: tissue plausibility for altered
  metabolic pathways.

## Sources

- NIH Common Fund Metabolomics: https://commonfund.nih.gov/metabolomics
- Metabolomics Workbench: https://www.metabolomicsworkbench.org/
- National Metabolomics Data Repository: https://www.metabolomicsworkbench.org/data/
- Metabolomics Workbench REST API: https://www.metabolomicsworkbench.org/tools/mw_rest.php
- RefMet nomenclature: https://www.metabolomicsworkbench.org/databases/refmet/index.php
