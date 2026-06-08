# Glycoscience / GlyGen

Reviewed: 2026-05-29

## Why This Is Mechanistically Valuable

Glycoscience is mechanistically valuable because many disease mechanisms depend
on modified molecules, not just genes or proteins. Glycans alter protein
folding, trafficking, receptor binding, immune recognition, mucin barrier
properties, coagulation factors, viral entry, and tumor biomarkers. The Common
Fund Glycoscience page describes the program as creating resources, tools, and
methods that make glycans more accessible to the broader biomedical research
community.

GlyGen and related glycoscience resources can help dismech represent the actual
glycoprotein, glycan, or glycosylation defect that mediates disease biology.

## Dismech Interpretation Pattern

Use glycoscience data to add the modified-molecule layer:

`glycosylation gene or pathway defect -> altered glycan/glycoprotein structure
or trafficking -> receptor, immune, coagulation, mucin, lysosomal, or matrix
defect -> phenotype`

This is especially important where a disease currently stops at a gene name but
the disease mechanism is carried by a glycan-modified protein or lipid.

## Concrete Implementation Plan

**Mode:** teach dismech. GlyGen should teach dismech to represent the modified
molecule, glycosylation site, glycan identifier, and biomarker readout that sit
between a gene defect and a phenotype.

**Required datasets and access path:**

- Use the GlyGen portal and data services:
  https://glygen.org/, https://data.glygen.org/, https://api.glygen.org/, and
  https://sparql.glygen.org/.
- Use GlyGen Wiki API documentation as the practical starting point:
  https://wiki.glygen.org/Main_Page. The wiki states that GlyGen APIs provide
  programmatic access to glycan, protein, and glycoprotein objects and are
  documented with Swagger.
- For each disease use case, choose stable identifiers before curation:
  UniProt accession for protein, GlyTouCan/GlyGen glycan accession for glycan,
  site position when a glycosylation site is relevant, and CHEBI only when the
  entity is a small molecule represented there.
- Use GlyGen disease and biomarker APIs to find candidate associations, then
  verify mechanism claims from primary disease literature before writing YAML.

**Tools and environment:**

- Python `requests` client for GlyGen REST plus optional SPARQL queries for
  batch crosswalks.
- Identifier normalization against UniProt, GlyTouCan, CHEBI, HGNC, and GO.
- For CDG entries, spreadsheet-level review is enough for the first pass; do
  not attempt glycan structure rendering until the disease mechanism text has
  stable identifiers.

**Curation targets:**

- Congenital disorders of glycosylation: `ALG12_Congenital_Disorder_of_Glycosylation`,
  `COG7-Congenital_Disorder_of_Glycosylation`, and
  `COG1-congenital_disorder_of_glycosylation` first.
- `Cystic_Fibrosis`: mucin glycosylation as a modifier of airway mucus and
  infection only when supported by CF-specific evidence.
- `Influenza` and `Gastric_Cancer_H_pylori_Associated`: glycan-mediated host
  attachment/tropism mechanisms.
- `Pancreatic_Ductal_Adenocarcinoma`: CA 19-9 and mucin/glycan biomarkers as
  tumor/stromal readouts, not standalone causal nodes.

**Code to write:**

- Add `src/dismech/commonfund/glygen.py` with lookup helpers for protein
  glycosylation, glycan details, disease associations, and biomarker records.
- Add `scripts/glygen_cdg_audit.py` to compare CDG disease files against
  available GlyGen identifiers and produce missing glycan/glycoprotein fields.
- Add schema-review notes for glycan identifiers, glycosylation sites,
  glycoprotein biomarkers, and whether `biochemical` needs a glycan-specific
  substructure.

**Graduate-student first pass:**

1. Pick three CDG files and list the causal gene, enzyme activity, affected
   glycan pathway, diagnostic glycoprotein readout, and major phenotype.
2. For each gene/protein, query GlyGen and record UniProt, glycan, and disease
   association URLs.
3. Draft mechanism edits that say exactly what glycan processing step is
   impaired and which biomarker demonstrates it.

## Dismech Disease and Mechanism Exemplars

| Disease | Current or candidate mechanism | How GlyGen/Glycoscience helps |
|---------|--------------------------------|-------------------------------|
| `ALG12_Congenital_Disorder_of_Glycosylation` | Curated nodes: `ALG12 mannosyltransferase deficiency`, `N-glycan precursor formation defect`, `Abnormal serum and IgG N-glycosylation`, `Neurodevelopmental and brain involvement` | Direct glycan structure and glycoprotein annotation can make the N-glycan defect machine-readable. |
| `COG7-Congenital_Disorder_of_Glycosylation` | Curated nodes: `COG7 Loss Destabilizes the Conserved Oligomeric Golgi Complex`, `Mislocalized Golgi Glycosylation Machinery`, `Combined N- and O-glycosylation Defect` | GlyGen can help distinguish N-glycan, O-glycan, sialylation, and Golgi trafficking readouts. |
| `COG1-congenital_disorder_of_glycosylation` | Curated nodes: `COG1 Deficiency Disrupts the Conserved Oligomeric Golgi Complex`, `Retrograde Golgi trafficking delay`, `Defective N- and O-glycosylation`, `Abnormal serum N- and O-glycan processing` | Good pilot for adding specific glycoprotein biomarkers such as transferrin and apolipoprotein C-III forms. |
| `Cystic_Fibrosis` | Current disease file exists | Candidate addition: mucin glycosylation and mucus barrier properties as modifiers of airway obstruction, infection, and inflammation. |
| `Influenza` | Current disease file exists | Candidate addition: viral hemagglutinin binding to sialylated glycans -> epithelial tropism -> respiratory infection phenotype. |
| `Pancreatic_Ductal_Adenocarcinoma` | Curated nodes: `KRAS Oncogene Activation`, `Desmoplastic Stroma`, `CAF-Mediated T Cell Exclusion`; biomarker `CA 19-9` | Glycoscience can ground CA 19-9 and mucin/glycan biomarkers in tumor/stromal mechanisms. |
| `Gastric_Cancer_H_pylori_Associated` | Curated nodes: `CagA-Mediated Oncogenic Signaling`, `VacA-Induced Cellular Damage`, `Chronic Inflammation (Correa Cascade)` | Candidate addition: mucin glycosylation and microbial adhesion in gastric epithelial colonization and inflammation. |

## High-Value Curation Work

- Add explicit glycan/glycoprotein notes to congenital disorders of
  glycosylation entries that currently contain generic "abnormal glycosylation"
  language.
- Define a narrow pattern for glycan identifiers. Use CHEBI where possible for
  small glycans/metabolites, and add stable external mappings only when the
  target resource has durable identifiers.
- Curate diagnostic glycoprotein biomarkers such as transferrin glycoforms,
  apolipoprotein C-III isoforms, CA 19-9, mucins, and IgG N-glycans as
  mechanism readouts.
- Add glycan-mediated host-pathogen mechanisms to `Influenza`,
  `Acquired_Immunodeficiency_Syndrome`, and `Gastric_Cancer_H_pylori_Associated`
  only when the glycan interaction is disease-specific.

## Fit for RFA-RM-26-017

Best partner datasets:

- GlyGen/Glycoscience + Metabolomics Workbench: glycan and metabolite
  biochemical signatures.
- GlyGen/Glycoscience + HMP/iHMP: microbial glycan interactions and mucosal
  barrier biology.
- GlyGen/Glycoscience + HuBMAP: glycoprotein localization in tissue context.
- GlyGen/Glycoscience + exRNA: multimodal biofluid biomarkers.

## Sources

- NIH Common Fund Glycoscience: https://commonfund.nih.gov/Glycoscience
- GlyGen: https://glygen.org/
- GlyGen data repository: https://data.glygen.org/
- GlyGen API: https://api.glygen.org/
- GlyGen Wiki/API documentation: https://wiki.glygen.org/Main_Page
- NCBI Glycans: https://www.ncbi.nlm.nih.gov/glycans/
