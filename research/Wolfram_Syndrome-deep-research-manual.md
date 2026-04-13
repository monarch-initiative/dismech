# Wolfram syndrome manual research notes

Date: 2026-04-13
Issue: #1174

## Disease framing

- Curated the disease root as `MONDO:0018105` `Wolfram syndrome`.
- Included two recessive subtypes under this root:
  - `MONDO:0009101` `Wolfram syndrome 1` (`WFS1`)
  - `MONDO:0011502` `Wolfram syndrome 2` (`CISD2`)
- Explicitly excluded monoallelic `WFS1` `Wolfram-like syndrome` (`MONDO:0013673`) because MONDO and the literature treat it as a split concept rather than the same disease root.

## Main mechanistic story selected for the YAML

- Shared syndrome-level frame: organelle homeostasis failure centered on ER and
  mitochondria-associated membrane calcium handling.
- WS1 (`WFS1`) branch:
  - ER localization and ER calcium homeostasis role of wolframin:
    `PMID:11181571`
  - ER stress responsiveness in pancreatic beta cells: `PMID:15994758`
  - ER calcium depletion, inflammatory signaling, and beta-cell death:
    `PMID:35399956`
  - ER-mitochondria calcium transfer defect via the `WFS1-NCS1-IP3R` complex:
    `PMID:30352948`
  - Neuronal mitochondrial dysfunction in patient-derived cells:
    `PMID:37163979`
  - Optic-pathway dysfunction with retinal ER stress in `Wfs1`-deficient mice:
    `PMID:24823368`
  - Human neuroimaging evidence for hypomyelination / neurodegeneration:
    `PMID:26888576`, `PMID:30979932`, `PMID:31796109`
- WS2 (`CISD2`) branch:
  - Distinguishing clinical features and split from WS1:
    `PMID:35055657`, `PMID:29774890`
  - Direct disease-relevant neuronal mechanism for reduced ER-mitochondrial
    calcium transfer, increased autophagic flux, and mitochondrial failure:
    `PMID:41299767`

## Curation choices

- Used subtype tags on most mechanistic nodes because the strongest mechanistic
  literature is heavily weighted toward `WFS1` disease.
- Kept the shared middle of the graph at the level of impaired ER-mitochondria
  calcium signaling and mitochondrial dysfunction, because that is where the
  `WFS1` and `CISD2` branches most credibly converge.
- Used exact PMID-backed quotes only; no unsupported full-text paraphrases were
  carried into the YAML.

## Claims intentionally not encoded

- Specific repurposed agents such as dantrolene, sodium valproate, ibudilast,
  GLP-1 receptor agonists, or gene-therapy candidates were not added to the
  YAML because the available abstract-level support was either too indirect,
  too review-heavy, or not sufficiently disease-specific for clean
  validator-safe evidence items.
- Broader psychiatric and urologic phenotype detail was left out of the YAML
  despite being part of the syndrome spectrum because the exact-quote evidence
  available in the cached literature was weaker than for the core endocrine,
  optic, hearing, neurodegenerative, and WS2-specific bleeding/ulcer features.
- Histopathology was represented indirectly through pathophysiology nodes
  instead of a dedicated `histopathology` section because the strongest
  quotable support came from mechanistic model and imaging papers rather than
  biopsy-centric human pathology abstracts.
