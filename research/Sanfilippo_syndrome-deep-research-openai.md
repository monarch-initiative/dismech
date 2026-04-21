# Sanfilippo syndrome deep research

Date: 2026-04-14

## Scope and final framing

- Target disease: **Sanfilippo syndrome / mucopolysaccharidosis type III / MPS III**
- Final root MONDO anchor: `MONDO:0018937`
- Final subtype MONDO anchors:
  - `MPS IIIA` -> `MONDO:0009655`
  - `MPS IIIB` -> `MONDO:0009656`
  - `MPS IIIC` -> `MONDO:0009657`
  - `MPS IIID` -> `MONDO:0009658`
- Final subtype gene framing:
  - `MPS IIIA` -> `SGSH` / `hgnc:10818`
  - `MPS IIIB` -> `NAGLU` / `hgnc:7632`
  - `MPS IIIC` -> `HGSNAT` / `hgnc:26527`
  - `MPS IIID` -> `GNS` / `hgnc:4422`

## MONDO / Monarch cross-check

I explicitly re-checked the disease anchors rather than trusting the helper note on issue `#1312`.

### Local MONDO check

On **2026-04-14**, local OAK/MONDO resolution returned:

- `MONDO:0018937 ! mucopolysaccharidosis type 3`
- `MONDO:0009655 ! mucopolysaccharidosis type 3A`
- `MONDO:0009656 ! mucopolysaccharidosis type 3B`
- `MONDO:0009657 ! mucopolysaccharidosis type 3C`
- `MONDO:0009658 ! mucopolysaccharidosis type 3D`

Important correction:

- The issue-helper suggestion that root Sanfilippo syndrome should use `MONDO:0001074` was incorrect.
- On the same 2026-04-14 MONDO check, `MONDO:0001074` resolved to **chronic tic disorder**, not Sanfilippo syndrome.

### Why I used the root MONDO term

`MONDO:0018937` is the correct umbrella disease anchor for the shared MPS III / Sanfilippo mechanism. The four enzymatic diseases remain represented explicitly as `has_subtypes` with their own subtype MONDO terms.

## ClinGen cross-check

I cross-checked subtype/gene pairing against the local ClinGen gene-validity cache:

- `SGSH` -> `mucopolysaccharidosis type 3A` / `MONDO:0009655` -> **Definitive**
  - assertion date: `2022-06-15`
- `NAGLU` -> `mucopolysaccharidosis type 3B` / `MONDO:0009656` -> **Definitive**
  - assertion date: `2022-08-22`
- `HGSNAT` -> `mucopolysaccharidosis type 3C` / `MONDO:0009657` -> **Definitive**
  - assertion date: `2023-12-04`
- `GNS` -> `mucopolysaccharidosis type 3D` / `MONDO:0009658` -> **Definitive**
  - assertion date: `2022-09-02`

Interpretation:

- ClinGen validity is **subtype-specific**, not a single root-level one-gene assertion for all of Sanfilippo syndrome.
- That is exactly the modeling pattern I used in the YAML:
  - one shared disease-level root entry for the convergent mechanism,
  - four subtype records for the etiologic gene split.

## Lump vs split reasoning

I intentionally **lumped at the Sanfilippo root** and split only in the subtype block.

Why this is the right level:

- All four diseases are defined by failure of **sequential lysosomal heparan-sulfate degradation**.
- The dominant shared clinical trajectory is a **CNS-predominant neurodegenerative syndrome** with developmental regression, behavioral disturbance, sleep problems, and shortened survival.
- ClinGen still forces subtype-aware gene framing, so the root cannot erase subtype structure.

Why I did **not** preserve the subtype-A graph as a separate disease-level entry:

- The merged subtype-A work in PR `#1185` is biologically solid, but its proximal node is necessarily **SGSH-specific**.
- For a demo-ready root entry, the first mechanism node should be the shared pathway lesion, not one subtype's enzyme.
- The subtype-A work is therefore best reused as biology to **abstract upward**, not copied literally.

## What I reused from PR #1185

I reused the strongest pieces of the subtype-A curation:

- the emphasis on **lysosomal heparan-sulfate storage** as the proximal lesion,
- the decision to keep **neuroinflammation** explicit,
- the treatment logic that **enzyme/gene restoration** should point back to the storage lesion,
- the general preference for atomic graph structure.

I changed the granularity in three important ways:

1. I replaced the SGSH-only upstream node with a **shared four-enzyme heparan-sulfate catabolism defect**.
2. I made the middle of the graph shared and conservative:
   - `Lysosomal heparan sulfate accumulation`
   - `Neuroinflammatory cascade`
   - `Cortical synaptic dysfunction`
   - `Progressive central neurodegeneration`
3. I did **not** keep standalone nodes for autophagy failure, ganglioside storage, or axonal dystrophy because the exact abstract-level support was either weaker, more subtype-limited, or would have made the root graph more brittle for tomorrow's demo.

## Final mechanistic graph

The final pathograph is:

1. **Lysosomal heparan sulfate catabolism defect**
2. **Lysosomal heparan sulfate accumulation**
3. **Neuroinflammatory cascade**
4. **Cortical synaptic dysfunction**
5. **Progressive central neurodegeneration**
6. Downstream phenotypes and treatment targets

This graph is fully connected and avoids shortcutting:

- I did **not** jump directly from the enzyme defect to phenotypes.
- I did **not** leave `Neuroinflammatory cascade` or `Cortical synaptic dysfunction` dangling.
- I did **not** wire storage straight to regression/ID while also claiming the intermediary neuronal dysfunction nodes were important.

## Key evidence anchors used in YAML

### 1. Shared root disease and subtype logic

PMID:25851924

> "Mucopolysaccharidosis type III (MPS III, Sanfilippo syndrome) is a lysosomal storage disorder, caused by a deficiency in one of the four enzymes involved in the catabolism of glycosaminoglycan heparan sulfate."

- Use: root disease definition and shared upstream mechanism
- Evidence source in YAML: `OTHER`
- Reason: review-level synthesis, not a primary cohort

PMID:31536183

> "The diagnosis of MPS III is established in a proband with suggestive clinical and laboratory findings in whom either biallelic pathogenic variants in one of four genes (GNS, HGSNAT, NAGLU, and SGSH) or deficiency of the respective lysosomal enzyme has been identified."

- Use: confirm four-gene etiologic split under the root entry
- Evidence source in YAML: `OTHER`

### 2. Shared clinical course

PMID:31536183

> "Mucopolysaccharidosis type III (MPS III) is a multisystem lysosomal storage disease characterized by progressive central nervous system degeneration manifest as severe intellectual disability (ID), developmental regression, and other neurologic manifestations including autism spectrum disorder (ASD), behavioral problems, and sleep disturbances."

- Use: progressive central neurodegeneration node plus intellectual disability, developmental regression, and sleep disturbance phenotypes
- Evidence source in YAML: `OTHER`

PMID:25851924

> "It is characterized by progressive cognitive decline and severe hyperactivity, with relatively mild somatic features."

- Use: root disease description and `Hyperactivity`
- Evidence source in YAML: `OTHER`

PMID:31536183

> "Disease onset is typically before age ten years."

- Use: progression note for childhood onset
- Evidence source in YAML: `OTHER`

PMID:31536183

> "Death usually occurs in the second or third decade of life secondary to neurologic regression or respiratory tract infections."

- Use: progression / shortened survival note
- Evidence source in YAML: `OTHER`

### 3. Shared storage lesion

PMID:36306823

> "Enzyme deficiency results in accumulation of partially degraded HS within lysosomes throughout the body, leading to a progressive severe neurological disease."

- Use: defect -> storage edge and storage node
- Evidence source in YAML: `MODEL_ORGANISM`
- Reason: subtype-A mouse ERT paper, but the quoted biochemical lesion is the same shared proximal consequence expected across the spectrum

### 4. Storage to inflammation

PMID:37794029

> "The lack of functional enzyme in MPS IIIB patients leads to the progressive accumulation of heparan sulfate throughout the body and triggers a cascade of neuroinflammatory and other biochemical processes ultimately resulting in severe mental impairment and early death in adolescence or young adulthood."

- Use: storage -> neuroinflammatory cascade
- Also used as partial support for neuroinflammation -> progressive neurodegeneration
- Evidence source in YAML: `MODEL_ORGANISM`

### 5. Storage to neuronal/synaptic dysfunction

PMID:19386237

> "Clearance of heparan sulfate oligosaccharides in cultured embryonic MPSIIIB cortical neurons or treatment with proteasome inhibitors restored normal synaptophysin levels indicating that heparan sulfate oligosaccharides activate the degradation of synaptophysin by the proteasome with consequences on synaptic vesicle components that are relevant to clinical manifestations."

- Use: storage -> cortical synaptic dysfunction
- Evidence source in YAML: `MODEL_ORGANISM`

PMID:22558223

> "Quantitative immunohistochemistry showed significantly increased lysosomal compartment, GM2 ganglioside storage, neuroinflammation, decreased and mislocalised synaptic vesicle associated membrane protein, (VAMP2), and decreased post-synaptic protein, Homer-1, in layers II/III-VI of the primary motor, somatosensory and parietal cortex."

- Use: node-level support for both `Neuroinflammatory cascade` and `Cortical synaptic dysfunction`
- Evidence source in YAML: `MODEL_ORGANISM`
- Value: stronger than subtype-A-only evidence because this paper compares **IIIA and IIIB**

PMID:19386237

> "Behavioural manifestations are prominent at disease onset, suggesting possible early synaptic defects in cortical neurons."

- Use: partial support for the synaptic dysfunction -> hyperactivity link
- Evidence source in YAML: `MODEL_ORGANISM`

### 6. Treatment anchors

PMID:22008915

> "In contrast, AAV8-mediated liver-directed gene transfer achieved high and sustained levels of circulating active sulfamidase, which reached normal levels in females and was fourfold higher in males, and completely corrected lysosomal GAG accumulation in most somatic tissues. Remarkably, a 50% reduction of GAG accumulation was achieved throughout the entire brain of males, which correlated with a partial improvement of the pathology of cerebellum and cortex."

- Use: investigational gene therapy -> inhibition of storage
- Evidence source in YAML: `MODEL_ORGANISM`

PMID:21152017

> "We report here that high doses of genistein aglycone, given continuously over a 9 month period to MPSIIIB mice, significantly reduce lysosomal storage, heparan sulphate substrate and neuroinflammation in the cerebral cortex and hippocampus, resulting in correction of the behavioural defects observed."

- Use: substrate reduction therapy -> inhibition of storage and neuroinflammation
- Evidence source in YAML: `MODEL_ORGANISM`

PMID:31536183

> "Treatment of manifestations: Supportive therapies for neurodevelopmental delays, hearing loss, and visual impairment; medications (rather than behavioral therapy) for psychiatric/behavioral issues; physical therapy and/or orthopedic management of musculoskeletal manifestations; and management as prescribed by consulting specialists for seizures, cardiac involvement, sleep disorders, feeding difficulties."

- Use: supportive symptomatic care
- Evidence source in YAML: `OTHER`

## Evidence-source decisions

I was intentionally strict here:

- `PMID:25851924` and `PMID:31536183` are review / GeneReviews sources, so I tagged them `OTHER`, not `HUMAN_CLINICAL`.
- `PMID:22008915`, `PMID:21152017`, `PMID:22558223`, `PMID:19386237`, `PMID:36306823`, and `PMID:37794029` are all preclinical model papers, so I tagged them `MODEL_ORGANISM`.
- I did **not** upgrade review statements to `HUMAN_CLINICAL` just because they summarize human disease.

## Claims I intentionally left out

- **Aggressive behavior** as a structured phenotype:
  - true for some subtypes and supported in subtype-A papers,
  - but I did not need it for the root demo once hyperactivity and sleep disturbance were already supported cleanly.
- **Standalone autophagy impairment node**:
  - plausible and well-known in the broader Sanfilippo literature,
  - but I did not have abstract-level support strong enough to justify a separate root node without weakening the graph.
- **Standalone ganglioside storage node**:
  - present in the literature and seen in PMID:22558223,
  - but I kept it as supporting context inside the synaptic / neuropathology logic rather than adding another node tomorrow's demo does not need.

## Final curation decision

- Build **one root disease entry** at `kb/disorders/Sanfilippo_syndrome.yaml`
- Encode subtype structure in `has_subtypes`
- Use the shared HS-storage neurodegenerative pathograph at the root
- Keep subtype-aware gene framing aligned with ClinGen definitive assertions
- Prefer a smaller number of strongly connected, exact-quote-supported nodes over a larger but less defensible graph
