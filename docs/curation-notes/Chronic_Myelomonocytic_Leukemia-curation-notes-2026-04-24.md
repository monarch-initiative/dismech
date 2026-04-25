# Chronic Myelomonocytic Leukemia Curation Notes

## Modeling decisions

- The dismech unit is one disease-level CMML page, not separate pages for each ontology subclass.
- `disease_term` is anchored to `MONDO:0020311` and paired with `NCIT:C3178` at mapping level.
- Subtypes are modeled as flat facet axes rather than separate disorders.
- The first subtype axis is blast percentage: `CMML-0`, `CMML-1`, and `CMML-2`.
- The second subtype axis is leukocyte-count phenotype: myelodysplastic CMML and myeloproliferative CMML.
- NCIT subtype mappings were added because MONDO currently does not provide corresponding CMML subtype classes for this slice.
- The subtype mappings are ontology-grounding only and do not imply separate dismech pages or Not Yet Curated placeholders.

## Key literature used in curation

- `PMID:38450850` for disease overview, revised diagnostic criteria, MP-CMML versus MD-CMML split, and high-level treatment framing.
- `PMID:34985762` for mutation frequencies, monocytosis plus marrow dysplasia, and hypomethylating-agent response rates.
- `PMID:35377828` for IDO-positive dendritic-cell aggregates, regulatory T-cell expansion, and T-cell exhaustion in the marrow microenvironment.
- `PMID:40644618` for RAS-pathway mutation frequency, proliferative phenotype, and transformation risk.
- `PMID:36455187` for randomized phase III DACOTA treatment data in advanced proliferative CMML.
- `PMID:33039516` for higher-risk transplant benefit.
- `PMID:37096522` for CMML-0/1/2 and MD-CMML/MP-CMML clinical subtype usage plus common presenting phenotypes.
- `PMID:37223910` for GM-CSF hypersensitivity as a CMML hallmark.

## Atomic pathophysiology framing

- Clonal hematopoietic stem-cell transformation
- Early epigenetic and splicing-gene lesions
- Persistent monocytosis
- RAS pathway-driven proliferative phenotype
- IDO-positive dendritic-cell aggregates
- Immune tolerance and T-cell exhaustion
- AML transformation propensity

## Notes

- CMML-0/1/2 and MD-CMML/MP-CMML are kept in one file because they reflect subtype facets within a shared CMML causal program rather than fully distinct disease mechanisms.
- The curation emphasizes PMID-backed abstract quotes for validator-friendly evidence.
