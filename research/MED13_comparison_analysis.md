# MED13 three-way comparison analysis

Date: 2026-04-14

## What Is Being Compared

This is now a **three-way** comparison among three different kinds of MED13 work:

1. **Nico PR `#1304`**
   - `kb/disorders/MED13_Syndrome.yaml`
   - `research/MED13_Syndrome-deep-research-perplexity.md`
   - This is a **standalone MED13 disorder YAML proposal**.

2. **Our historical MED13 research branch**
   - branch: `research/med13`
   - now exposed as draft PR `#1320`
   - files:
     - `research/MED13-related_Neurodevelopmental_Disorder-deep-research-codex.md`
     - `research/MED13-related_Neurodevelopmental_Disorder-deep-research-codex.md.citations.md`
     - `research/MED13-related_Neurodevelopmental_Disorder-curation-notes.md`
   - This is **docs-only research and curation guidance**, not a YAML entry.

3. **What is actually merged on `main`**
   - `kb/disorders/Mediator_Complex_Neurodevelopmental_Disorder.yaml`
   - This is **not** a standalone MED13 disorder entry.
   - It is a **grouping / mediatoropathy entry** that already contains:
     - a MED13 subtype anchored to `MONDO:0032485`
     - MED13-relevant phenotype contexts
     - a MED13-specific cortical neuron pathophysiology node

## Bottom line

The original comparison I wrote was incomplete because it compared Nico's PR against our older MED13 research docs, not against the already merged mediator-complex entry on `main`.

Once the merged entry is included, the picture changes:

- Our historical `research/med13` branch was **not orphaned**. It was a pushed branch with docs-only MED13 research, and it is now visible as PR `#1320`.
- Much of the strongest content from that historical branch has **already been absorbed into the merged mediator-complex grouping entry** on `main`.
- The real remaining delta is therefore mostly between:
  - Nico's **standalone MED13 YAML**
  - the **already merged grouped mediatoropathy model**

So the comparison is not just "Nico vs us." It is really:

- **Nico's standalone MED13 entry**
- **our older docs-only standalone thinking**
- **the current grouped implementation already merged into the knowledge base**

## What each artifact is trying to do

| Artifact | Primary goal | Strength | Limitation |
|---|---|---|---|
| Nico PR `#1304` | Create a standalone MED13 disease YAML | Broad MED13-specific phenotype coverage; genetics/treatments scaffolded | Disease mapping is off; mechanism is less specific than current `main` |
| Historical `research/med13` branch / PR `#1320` | Establish anchor choice and mechanism framing for MED13 | Strong on disease identity, boundary-setting, and cortical-development mechanism | Docs only; not YAML-grade; some repo-state assumptions are now stale |
| Merged `Mediator_Complex_Neurodevelopmental_Disorder.yaml` on `main` | Represent mediatoropathies as a grouped disorder with subtypes | Already integrates MED13 subtype and MED13 cortical-neuron mechanism into the knowledge base | Not a standalone MED13 entry; some MED13-specific phenotype granularity is flattened into the group model |

## Mechanism framing

### Nico PR `#1304`

Nico's MED13 entry uses two main mechanism nodes:

1. `Disrupted Mediator complex transcriptional regulation`
2. `MED13 phosphodegron disruption and impaired protein turnover`

This is directionally right. It captures:

- Mediator / CDK8 kinase module biology
- RNA polymerase II transcription
- an allele-specific phosphodegron / SCF-Fbw7 degradation hypothesis

What it does **not** do well is localize the disease trunk downstream into specific neurodevelopmental processes such as cortical neuron migration, callosal projection, and dendritic maturation.

### Historical `research/med13` branch / PR `#1320`

Our older research branch framed MED13 as:

1. heterozygous pathogenic `MED13` variation
2. altered dosage/function in the `MED12`-`MED13`-`CDK8`-`CCNC` module
3. dysregulated developmental transcription
4. impaired cortical neuron migration, projection, and maturation
5. core neurodevelopmental phenotypes

This was more specific than Nico's YAML on the **disease trunk**. It also explicitly argued that:

- MED13 should not be framed as a primary mitochondrial disease
- severe cardiac / mitochondrial presentations should be treated cautiously
- the strongest first mechanism is cortical-developmental, not a broad phenotype list

### Merged `main` entry

The merged mediator-complex entry already contains much of this historical framing:

- `CDK8 Kinase Module Dysfunction`
- `Neurodevelopmental Transcriptional Dysregulation`
- `Cortical Neuron Migration and Projection Defects`

It also already includes the key MED13 model-organism evidence:

- `PMID:41663567` supporting impaired radial migration, contralateral projection, and dendritic complexity in cortical neurons

### Mechanism comparison

| Aspect | Nico PR `#1304` | Historical `research/med13` | Merged `main` entry |
|---|---|---|---|
| Mediator / CDK8 module framing | Yes | Yes | Yes |
| Cortical neuron migration / projection specificity | No | Yes | Yes |
| Phosphodegron / turnover mechanism | Yes | Acknowledged but not central | No explicit dedicated MED13 phosphodegron node |
| Shared mediatoropathy framing | No | No, disease-specific | Yes |

## Disease anchoring

This is the clearest modeling difference.

### Nico PR `#1304`

Uses:

- `disease_term: MONDO:0001071`
- label: `intellectual disability`

This is too broad for a MED13 disorder entry. `MONDO:0001071` is a parent disease class, not the MED13-specific disease concept.

### Historical `research/med13`

Argued for:

- `MONDO:0032485` `intellectual developmental disorder 61`

and documented the split between:

- G2P: MED13-specific disorder anchor `MONDO:0032485`
- ClinGen cache: broader umbrella `MONDO:0100038` `complex neurodevelopmental disorder`

### Merged `main` entry

The grouped mediatoropathy entry already uses this distinction correctly at the subtype level:

- MED13 subtype term: `MONDO:0032485`

At the top level, the grouped entry uses the broader placeholder:

- `MONDO:0002320` `congenital nervous system disorder`

That top-level mapping is broad, but in this case it is a deliberate compromise because the notes explicitly say a dedicated MONDO grouping class is pending.

## Evidence overlap and divergence

### Shared across Nico PR and historical branch

- `PMID:29740699`
- `PMID:36087421`
- `PMID:38745205`
- `PMID:41561257`

These remain the core human MED13 evidence set.

### Nico-only evidence in the standalone YAML

- `PMID:33258286` - Kabuki-like / dysmorphism-focused case framing
- `PMID:33390853` - review used for cardiac/phosphodegron mechanism context
- `PMID:38854223` - ASD-focused case report
- `PMID:41195223` - later review / family report used for rarity and inheritance summary

### Historical `research/med13` branch additions

- `PMID:41130977` - severe case with mitochondrial/cardiomyopathy/hepatomegaly features, treated cautiously
- DOI `10.1038/s42003-026-09704-w` - cortical-neuron mechanistic paper
- repo-specific G2P / ClinGen context

### What merged `main` already uses

The merged grouped entry already absorbed several of the most important MED13-specific citations, including:

- `PMID:29740699`
- `PMID:36087421`
- `PMID:38745205`
- `PMID:41195223`
- `PMID:41663567`
- `PMID:33258286`

That means the strongest historical MED13 thinking is no longer only in the old docs branch. A substantial fraction is already in production content on `main`.

## Phenotype coverage

### Nico PR `#1304`

Nico's standalone MED13 YAML is stronger on **MED13-specific phenotype granularity**. It explicitly models:

- intellectual disability
- global developmental delay
- speech/language delay
- hypotonia
- facial dysmorphism
- congenital heart defects
- autism spectrum disorder
- ADHD
- seizures / epileptic encephalopathy
- optic nerve abnormalities
- microcephaly
- corpus callosum abnormalities
- sensorineural hearing loss
- Duane anomaly

It also includes a genetics section and supportive-care treatment placeholders.

### Historical `research/med13`

Our older docs separated phenotypes into:

- **core**: ID, developmental delay, speech impairment, hypotonia, behavioral/autism-spectrum features
- **secondary/spectrum-expanding**: seizures, heart disease, hearing loss, ocular findings, corpus callosum abnormalities, dysmorphism, growth issues

This was a cautious framing document rather than a complete phenotype inventory.

### Merged `main` entry

The grouped mediatoropathy entry already covers many MED13-relevant phenotypes, but usually in one of two ways:

1. as shared group phenotypes with subtype contexts
2. as broader mediatoropathy phenotype classes with MED13 notes

For MED13 specifically, `main` already carries or references:

- speech and language delay
- autism spectrum disorder
- ADHD
- hypotonia
- seizures
- hearing impairment
- corpus callosum abnormalities
- ocular anomalies
- congenital heart defects
- growth restriction
- skeletal involvement
- constipation / obstipation

### Phenotype comparison

| Feature | Nico PR `#1304` | Historical `research/med13` | Merged `main` entry |
|---|---|---|---|
| MED13-specific granularity | Strongest | Moderate | Moderate |
| Core-vs-spectrum distinction | Weak | Strongest | Moderate |
| Shared mediatoropathy context | None | None | Strongest |
| Individual rare ocular findings like Duane anomaly / optic nerve abnormalities | Explicit | Only as grouped ocular expansion | Mostly folded into broader ocular / phenotype-context framing |

## What Nico still contributes beyond current `main`

Even after looking at the merged grouped entry, Nico's PR still contributes real information:

1. **A standalone MED13 YAML shape**
   - If the repo eventually wants a dedicated MED13 disease entry, Nico's PR is closer to that artifact type than the grouped mediatoropathy entry.

2. **A dedicated phosphodegron / protein-turnover branch**
   - Current `main` does not have an explicit MED13 phosphodegron node.

3. **More explicit MED13-specific phenotype naming**
   - especially `sensorineural hearing loss`, `optic nerve abnormalities`, `Duane anomaly`, and a direct standalone MED13 phenotype list

4. **Supportive-care treatment placeholders**
   - speech therapy
   - genetic counseling
   - supportive care

## What current `main` already covers that reduces the novelty of Nico's PR

The merged mediator-complex entry already captures several points that originally came from the older MED13 research effort and that now matter more than Nico's current generic transcription node:

1. **Correct MED13 subtype anchor**
   - `MONDO:0032485`

2. **A better disease trunk**
   - CDK8 kinase module dysfunction
   - neurodevelopmental transcriptional dysregulation
   - cortical neuron migration and projection defects

3. **MED13-specific cortical-development evidence**
   - `PMID:41663567`

4. **Subtype-aware phenotype modeling**
   - MED13 as one subtype among overlapping mediatoropathies rather than an isolated entry with no system-level context

## Quality issues

### Nico PR `#1304`

1. **Wrong / too-broad disease mapping**
   - `MONDO:0001071` should not anchor a MED13 disorder entry.

2. **Mechanism is less specific than current `main`**
   - The merged grouped entry already has a better MED13 cortical-neuron mechanism trunk.

3. **Frequency confidence may exceed snippet support**
   - Several bands look plausible, but many evidence snippets support association more directly than exact frequency bins.

4. **The branch research markdown is unreliable**
   - `research/MED13_Syndrome-deep-research-perplexity.md` contains template boilerplate and wrong identifiers, including:
     - `MONDO:0700197` = porcine leukemia
     - `HGNC:6974` = MDM4, not MED13

### Historical `research/med13` branch / PR `#1320`

1. **Docs only, no YAML**
   - It is research-grade, not ingest-ready.

2. **Repo-state assumptions are now stale**
   - For example, the docs say the repo had no relevant disorder entry; that is no longer true because the mediator-complex grouping entry is now merged.

3. **Standalone-entry bias**
   - The docs assume the right destination is a MED13-specific first disease anchor, whereas the repo has since implemented a grouped mediatoropathy strategy.

### Merged `main` entry

1. **Not a standalone MED13 disease**
   - This is a strength for grouping, but a limitation if users want direct MED13 disease pages and YAMLs.

2. **Some MED13-specific details are flattened into the group model**
   - Nico's dedicated phenotype list is more immediately readable as a MED13-centered artifact.

3. **Top-level MONDO term is broad**
   - but this appears intentional and documented pending a proper grouping term.

## Best synthesis

The best synthesis depends on the modeling direction the repo wants.

### If the grouped mediatoropathy model remains the preferred design

Then the best next step is **not** to merge Nico's PR as-is. It is to mine it for additions to the existing grouped entry:

- add a MED13-specific phosphodegron / turnover branch if desired
- consider whether MED13-specific treatment/supportive-care content belongs in subtype contexts
- pull in any MED13 phenotype granularity currently missing from `main`

### If the repo wants a future standalone MED13 entry

Then the ideal standalone MED13 YAML would combine:

- Nico's phenotype breadth and treatment placeholders
- the historical branch's anchor decision and core-vs-spectrum caution
- the merged `main` entry's better cortical-development pathophysiology

In that case the standalone entry should:

1. use `MONDO:0032485`
2. keep the cortical neuron migration / projection / dendrite trunk
3. retain the phosphodegron node as an allele-specific branch
4. clearly distinguish core phenotypes from spectrum-expanding ones
5. avoid relying on the contaminated Perplexity research markdown

## Final assessment

The important clarification is that we do **not** have just a duplicate standalone MED13 effort versus another duplicate standalone MED13 effort.

We have:

- a historical docs-only MED13 branch, now transparent as PR `#1320`
- a merged grouped mediatoropathy entry on `main` that already absorbed much of that historical work
- Nico's standalone MED13 YAML PR `#1304`, which still adds some useful MED13-specific granularity but is no longer novel on the core mechanism or disease anchor

So the strongest current conclusion is:

- **Nico's PR is most valuable as a source of MED13-specific additions to the already merged grouped entry, not as a clean standalone entry ready to merge unchanged.**
