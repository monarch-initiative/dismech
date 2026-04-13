# X-linked adrenoleukodystrophy: manual curation research notes

Date: 2026-04-12
Issue: `#1181`
Disease file: `kb/disorders/X-linked_Adrenoleukodystrophy.yaml`

## Scope and disease framing

- Curated at the disease-spectrum level with `MONDO:0018544` (`adrenoleukodystrophy`), because the core biochemical lesion is shared across the phenotype spectrum.
- Explicit subtype branches retained:
  - `MONDO:0015339` adrenomyeloneuropathy
  - `MONDO:0010247` X-linked cerebral adrenoleukodystrophy
- Addison-only presentations were treated as part of the spectrum rather than a separate top-level disease entry here.
- Inheritance was framed as `HP:0001417` X-linked inheritance rather than forcing an `X-linked recessive` label. This is important because symptomatic heterozygous women are common enough to make the recessive shorthand misleading for disease-level curation.

## Main mechanistic story chosen for the YAML

The curation uses a small number of atomic nodes rather than bundled mechanisms:

1. `ABCD1-mediated peroxisomal VLCFA import failure`
2. `Very-long-chain fatty acid accumulation`
3. `Oxidative stress and mitochondrial dysfunction`
4. `Microglial phagocytic priming`
5. `Spinal cord axonopathy`
6. `Impaired macrophage plasticity`
7. `Cerebral inflammatory demyelination`
8. `Adrenal cortical dysfunction`

This framing reflects the literature better than a single omnibus "ABCD1 deficiency causes neuroinflammation and adrenal failure" node.

## Why the disease was split this way

### Shared upstream core

- `PMID:24316281` and `PMID:23671276` together support the upstream biochemical defect: ABCD1 normally imports CoA-activated VLCFAs into peroxisomes, and human fibroblast experiments show the β-oxidation defect is directly caused by ABCD1 dysfunction.
- `PMID:38034003` and `PMID:25115486` support that VLCFA accumulation is a shared abnormality across tissues and phenotypes.

### AMN/default branch

- `PMID:24316281` is the cleanest disease-level statement that AMN is the default manifestation and is a dying-back spinal cord axonopathy.
- `PMID:21786300` provides model-organism evidence that oxidative stress is a major disease-driving factor in X-AMN.
- `PMID:29059709` supports a distinct phagocytosis/complement/microglial lesion in AMN spinal cord, including human tissue evidence for increased microglial/phagocytic markers without overt inflammation.

### CALD branch

- `PMID:24316281` supports the conversion model from shared VLCFA pathology to cerebral inflammatory demyelination.
- `PMID:29860501` was central for the CALD branch because it links ABCD1 deficiency to impaired macrophage plasticity and incomplete anti-inflammatory resolution, and it includes post-mortem lesion pathology.

### Adrenal branch

- `PMID:38034003` was the most explicit source for adrenal pathophysiology: VLCFA accumulation in adrenal cortex, defective adrenal response to ACTH, progressive membrane dysfunction, and ACTH receptor impairment.
- `PMID:30252065` gave the strongest natural-history numbers for adrenal insufficiency timing and prevalence.

## Genetics and modifier conclusions

- `ABCD1` is the sole causal gene captured at disease level here.
- Strong no-correlation conclusion retained:
  - `PMID:24316281`: "There is no general genotype-phenotype correlation in X-ALD."
  - `PMID:10190819`: "There are no obvious correlations between the phenotypes of patients with ALD and their genotypes..."
- Symptomatic women were explicitly represented:
  - `PMID:24480483` shows 63% myelopathy and 57% peripheral neuropathy in the prospective female-carrier cohort, with strong age dependence.

## Treatment framing

- Restricted disease-modifying therapies to the cerebral inflammatory branch:
  - allogeneic HSCT: `PMID:34781360`
  - autologous lentiviral hematopoietic stem-cell gene therapy: `PMID:28976817`
- Did not claim disease-modifying efficacy for adult AMN/myelopathy because the evidence base here is weaker and more heterogeneous.
- Adrenal treatment was kept as replacement therapy rather than disease modification:
  - glucocorticoid replacement: `PMID:38034003`

## Histopathology retained

- CALD lesions:
  - `PMID:29860501` supports enlarged lipid-laden CD86-positive macrophages in post-mortem cerebral lesions.
- AMN spinal cord:
  - `PMID:29059709` supports mild myelin loss plus marked CD68/IBA1-positive microglial activation in human spinal cord.

## Evidence-source choices

- `IN_VITRO`
  - `PMID:23671276` for direct ABCD1 transporter dysfunction in human fibroblasts.
- `HUMAN_CLINICAL`
  - used for human cohorts, human reviews synthesizing clinical/pathologic disease knowledge, and direct human tissue studies.
- `MODEL_ORGANISM`
  - `PMID:21786300` for antioxidant rescue / oxidative-stress causality in X-AMN mouse models.
- `OTHER`
  - used selectively for mixed human+mouse abstract language in `PMID:29059709` where the quoted sentence itself explicitly spans both species.

## Deep-research workflow actually used

- `just research-disorder asta X-linked_Adrenoleukodystrophy`
- manual PMID vetting from `references_cache/`
- ontology checks with `runoak` for MONDO, GO, CL, UBERON, CHEBI, HPO, and MAXO terms

## Key PMIDs used in the final YAML

- `PMID:23671276`
- `PMID:24316281`
- `PMID:25115486`
- `PMID:29860501`
- `PMID:29059709`
- `PMID:30252065`
- `PMID:38034003`
- `PMID:34781360`
- `PMID:28976817`
- `PMID:24480483`
- `PMID:10190819`
- `PMID:15316978`
