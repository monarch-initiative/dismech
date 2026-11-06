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

## DisMech Interpretation Pattern

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

## DisMech Disease and Mechanism Exemplars

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

## Pilot: Glycan Biomarkers with the bGSL Lexicon

The biomarker Glycan Structure Lexicon (bGSL,
https://github.com/clinical-biomarkers/bGSL-data, release 2026-10-08, 973
terms) is a curated dictionary of glycan names: canonical terms,
abbreviations, synonym classes, and cross-references to GlyTouCan, GlyGen
(GSD) and GlycoMotif. This pilot tests whether it helps dismech represent the
glycan behind a glycan biomarker.

### Why a glycan lexicon is needed

ChEBI, which dismech uses for chemical entities, does cover the important
glycan biomarkers, but under IUPAC-style structure labels rather than the
names clinicians and papers use. A curator searching ChEBI for "sialyl Lewis
x" or "globotriaosylceramide" by label does not find:

| Biomarker name | ChEBI term | ChEBI label |
|---|---|---|
| sialyl Lewis x (CD15s) | CHEBI:61711 | alpha-Neup5Ac-(2->3)-beta-D-Galp-(1->4)-[alpha-L-Fucp-(1->3)]-D-GlcpNAc |
| sialyl Lewis a (CA 19-9 epitope) | CHEBI:61793 | alpha-Neu5Ac-(2->3)-beta-D-Gal-(1->3)-[alpha-L-Fuc-(1->4)]-D-GlcNAc |
| Gb3 / globotriaosylceramide | CHEBI:18313 | alpha-D-galactosyl-(1->4)-beta-D-galactosyl-(1->4)-beta-D-glucosylceramide |
| Tn antigen (protein-bound) | CHEBI:53604 | O-(N-acetyl-alpha-D-galactosaminyl)-L-serine residue |
| ganglioside GM3 | CHEBI:84118 | ganglioside GM3 |

`runoak -i ols:chebi search "l~sialyl-Lewis X"` and `"l~globotriaosylceramide"`
return nothing; the OLS full-text search finds them through synonyms. A
name-to-structure lexicon is the missing step between a biomarker as written
in a paper and a structure identifier, and that step is what bGSL provides.

### What the KB currently carries

A token-level scan of every `kb/disorders/` file against bGSL terms, exact
synonyms and abbreviations (hidden terms excluded) matched 1,022 of 3,757
files. Restricted to the glycan-specific bGSL classes (1A to 2E), 357 files
match 77 terms; most matches in the generic classes are monosaccharides such
as glucose that ChEBI already handles. The glycan-specific matches fall where
expected: the Glc3Man9GlcNAc2 precursor in N-glycosylation CDGs (ALG1, MOGS,
MPDU1, PMM2, STT3A), core 1 O-glycan in Golgi CDGs (COG1, COG4, GALNT2,
CAMLG), sialyl Lewis x in LAD-II and SLC35A1-CDG, Gb3 in Fabry disease, GM3
in GM3 synthase deficiency and the sialidoses, and CA 19-9 in biliary cancers.

Before this pilot every one of these was free text. Glycan biomarkers in
`biochemical:` carried no structure identifier, and several (PMM2-CDG
transferrin pattern, IgAN galactose-deficient IgA1, PDAC CA 19-9) carried no
term binding at all.

The same scan over the 72,519 files in `references_cache/` matched 12,425
files, 3,356 of them on glycan-specific terms. That count is inflated by
abbreviations that collide with common non-glycan uses (see the suggestions
file below), so the publication cache is a candidate generator only after
those abbreviations are filtered.

### Pilot edits

| Entry | Biomarker | Change |
|---|---|---|
| `Leukocyte_Adhesion_Deficiency_Type_II` | Neutrophil sialyl-Lewis X (CD15s) | New `biochemical:` record, mapped to CHEBI:61711, read out to `Loss of Sialyl-Lewis X Selectin Ligands` |
| `IgA_Nephropathy` | Galactose-deficient IgA1 | Mapped to the protein-bound Tn antigen CHEBI:53604, read out to `Galactose-deficient IgA1 overproduction` |
| `Pancreatic_Ductal_Adenocarcinoma` | CA 19-9 | Bound to NCIT:C81982, mapped to sialyl Lewis a CHEBI:61793 with evidence that sLea is the CA 19-9 epitope (PMID:32527016) |
| `Fabry_Disease` | Renal globotriaosylceramide | Mapped to CHEBI:18313 |
| `PMM2-Congenital_Disorder_of_Glycosylation` | Serum transferrin isoform pattern | Bound to HP:0003642 Type I transferrin isoform profile |

Glycan structures go in the `biochemical[].mappings_list` slot with ChEBI
CURIEs. GlyTouCan and bGSL identifiers are **not** written into the KB yet.
They are recorded in the crosswalk below instead, for the reason given under
*Validating GlyTouCan accessions*.

### Crosswalk

Every GlyTouCan accession in this table resolves in GNOme (see below).

| dismech biomarker | ChEBI (dismech) | bGSL term | bGSL ChEBI | GlyTouCan (bGSL) | Agreement |
|---|---|---|---|---|---|
| LAD-II neutrophil sLeX | CHEBI:61711 | sialyl Lewis x | structure in description only, no CURIE | G00054MO; G96401FK | Same structure; bGSL lacks the CURIE |
| PDAC CA 19-9 | CHEBI:61793 | CA19-9 and sialyl Lewis a (two terms) | CHEBI:62681 on sialyl Lewis a only | G00053MO (both) | Compatible (62681 is the beta anomer of 61793); CA19-9 term has no ChEBI |
| IgAN Gd-IgA1 | CHEBI:53604 | Tn antigen | CHEBI:40356 (free GalNAc) | G57321FI; G61406KC | Disagree on form: bGSL maps the monosaccharide, dismech the Ser-linked residue |
| Fabry Gb3 | CHEBI:18313 | Gb3 | none | G00059MO | bGSL lacks the CURIE |
| Fabry lyso-Gb3 | none in ChEBI | none | none | none | Gap in both |
| GM3 synthase deficiency GM3 | CHEBI:84118 | GM3 | none | G91237TK; G56516VH | bGSL lacks the CURIE |
| CDG Glc3Man9GlcNAc2 | not bound | Glc3Man9GlcNAc2 | none | none | bGSL term carries no identifier |
| PMM2-CDG / SLC35A2-CDG transferrin glycoforms | HP profile terms only | none | none | none | Gap in bGSL |

### Findings

- bGSL is most useful as a **name resolver**: it reaches the right structure
  from the names papers use (CD15s, sLeX, CA19-9, GL3, Tn) where a ChEBI label
  search does not.
- It is **not yet a binding target** for dismech: identifiers live in an
  unprefixed TSV with UUID primary keys, ChEBI appears only inside free-text
  descriptions, and nothing in dismech's validation stack can check a bGSL or
  GlyTouCan CURIE.
- The clinically central glycoform biomarkers of the CDGs (transferrin
  glycoforms, apolipoprotein C-III isoforms) and storage-disease markers
  (lyso-Gb3, urinary oligosaccharides) are absent from bGSL. These are
  glycoconjugate measurements rather than free glycans, which may be outside
  bGSL's intended scope; either way they are the biomarkers this KB most
  needs to represent.

### Validating GlyTouCan accessions

GNOme, the Glycan Naming and Subsumption Ontology, uses GlyTouCan accessions
as its identifiers (`GNO:G00059MO` is GlyTouCan `G00059MO`) and is served by
the EBI Ontology Lookup Service (release V2.7.0, 2026-07-24, at the time of
this pilot). `runoak -i ols:gno labels GNO:<accession>` therefore confirms
that an accession exists, and an unknown accession returns HTTP 404. GNOme
term labels are the accession itself, so this checks existence, not the
name. Recursive lookups (`ancestors`) are not available through the OLS
adapter.

Of the 534 distinct GlyTouCan accessions in bGSL 2026-10-08, 508 resolve in
GNOme. The 26 that do not are all polysaccharides or repeat-unit glycans
(chondroitin sulfates, hyaluronan, keratan sulfate, amylose, xyloglucan and
similar), which appear to be outside GNOme's coverage rather than invalid
accessions.

Adding `GNO: ols:gno` to `conf/oak_config.yaml` is not enough on its own to
validate a GlyTouCan CURIE in the KB. The term validator checks only slots
bound to a dynamic enum, and `biochemical[].mappings_list` is deliberately
unbound. A test with a wrong label and a nonexistent accession in
`mappings_list` passed with and without the `GNO` line. Validated GlyTouCan
identifiers need a bound slot: for example a label-match `GlycanTerm` enum on
a new `Biochemical` slot, the same pattern as `LoincTerm`. That is a schema
change and goes through the `extend-schema` process.

Concrete corrections and additions for the bGSL maintainers are in
[`GLYGEN_bGSL_dictionary_suggestions.md`](GLYGEN_bGSL_dictionary_suggestions.md).

### Next steps

- Extend the mapping to the remaining CDG and glycosphingolipid storage
  entries found by the KB scan, starting with Glc3Man9GlcNAc2 in the ALG CDGs
  and core 1 O-glycan in the COG CDGs.
- Decide, through the `extend-schema` process, whether a glycan biomarker
  needs its own identifier slot (GlyTouCan, with a resolver) or whether
  `mappings_list` with ChEBI is sufficient.
- Re-run the publication-cache scan with the ambiguous abbreviations removed
  and use it to propose new glycan-disease pairs.

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
