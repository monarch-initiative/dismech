# MED13 comparison analysis

Date: 2026-04-14
PR under review: https://github.com/monarch-initiative/dismech/pull/1304
Compared sources:
- Nico PR branch `kb/disorders/MED13_Syndrome.yaml`
- Nico PR branch `research/MED13_Syndrome-deep-research-perplexity.md`
- Our prior research docs in `/Users/cjm/worktrees/dismech-med13/research/`
  - `MED13-related_Neurodevelopmental_Disorder-deep-research-codex.md`
  - `MED13-related_Neurodevelopmental_Disorder-deep-research-codex.md.citations.md`
  - `MED13-related_Neurodevelopmental_Disorder-curation-notes.md`

## Bottom line

The two efforts are substantially aligned on the high-level disease story: MED13 is a Mediator/CDK8 kinase-module disease gene, and the core syndrome is a dominantly inherited neurodevelopmental disorder with intellectual disability, developmental delay, speech impairment, hypotonia, and behavioral features.

The main difference is emphasis. Nico's YAML is broader on observed human phenotype coverage and already shaped like a dismech entry. Our earlier research is narrower, more conservative on phenotype boundaries, and stronger on the disease anchor decision and on a cortical-neurodevelopment mechanism trunk. The best merged entry would keep Nico's human phenotype breadth and genetics/treatment scaffolding, but replace the disease mapping and re-center the pathophysiology on the more specific cortical-development framing from our research.

## 1. Mechanism framing

| Aspect | Nico PR YAML | Our prior research | Comparison |
|---|---|---|---|
| Core disease concept | "MED13 syndrome" as a rare AD neurodevelopmental disorder | "MED13-related neurodevelopmental disorder" / `intellectual developmental disorder 61` | Similar syndrome concept, but our framing is more ontology-specific |
| Primary mechanistic center | Disrupted Mediator complex transcriptional regulation | Dosage-sensitive Mediator kinase-module dysfunction causing developmental transcriptional dysregulation | Strong overlap |
| Downstream biological specificity | Generic neurodevelopment and transcription | Explicit cortical neuron migration, contralateral projection, dendritic maturation, and cortical circuit formation | Our framing is more mechanistically specific |
| Variant-specific mechanism | Separate phosphodegron / SCF-Fbw7 turnover node | Missense-vs-truncating mechanism treated as unresolved; phosphodegron mechanism acknowledged but not made the central trunk | Nico is stronger on allele-specific detail |
| Phenotype-boundary stance | More inclusive phenotype inventory | Conservative core-vs-spectrum split; severe cardiac/mitochondrial findings treated as possible outliers or allele-specific extensions | Our framing is more cautious |

### Interpretation

Both approaches agree that the disease should be modeled as a transcriptional-regulation disorder in the Mediator kinase module rather than as a primary mitochondrial disorder or isolated malformation syndrome.

The strongest difference is that our prior work adds a sharper causal chain:

1. heterozygous pathogenic `MED13` variation
2. altered MED13 dosage/function in the `MED12`-`MED13`-`CDK8`-`CCNC` module
3. dysregulated RNA polymerase II-associated developmental transcription
4. impaired cortical neuron migration/projection/maturation
5. core neurodevelopmental phenotypes

Nico's YAML instead uses:

1. disrupted Mediator complex transcriptional regulation
2. phosphodegron disruption and impaired protein turnover
3. clinical phenotypes

That second Nico node is useful, but it reads more like a variant-class branch than the universal disease trunk.

## 2. Evidence overlap and divergence

### Overlap

Both efforts rely on the same core human disease papers:

- `PMID:29740699` - syndrome-defining cohort
- `PMID:36087421` - epileptic encephalopathy / infantile spasms spectrum expansion
- `PMID:38745205` - severe congenital-anomaly case
- `PMID:41561257` - hearing-loss case and truncating-variant haploinsufficiency interpretation

### Nico-only evidence in the YAML

- `PMID:33258286` - Kabuki-like / dysmorphism-oriented case framing
- `PMID:33390853` - review on MED13 in cardiac disease, used for structural/phosphodegron mechanism context
- `PMID:38854223` - ASD-focused case report
- `PMID:41195223` - later review/family report used for prevalence and inheritance summary

### Our-only evidence or source context

- `PMID:41130977` - severe case with infantile spasms, cardiomyopathy, hepatomegaly, and mitochondrial abnormalities; our notes treat this as important but not yet a safe core-mechanism anchor
- DOI `10.1038/s42003-026-09704-w` - cortical-neuron mechanistic study linking Med13 loss to radial migration and contralateral projection defects via `PLXNA4`
- Local repo context that Nico's YAML does not use:
  - `docs/research/g2p_all_genes_row_triage_2026_03_28.tsv` identifies `MED13-related neurodevelopmental disorder` at `MONDO:0032485`
  - `cache/clingen/gene_validity.csv` points to broader `MONDO:0100038` `complex neurodevelopmental disorder`

### Assessment

Nico's evidence set is better for expanding the human phenotype list. Our evidence set is better for deciding how to anchor and structure the disease mechanistically.

## 3. Phenotype, cell type, and biological process coverage

### Nico PR YAML

Phenotypes covered:
- intellectual disability
- global developmental delay
- delayed speech and language development
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

Cell types covered:
- neuron

Biological processes covered:
- transcription by RNA polymerase II
- nervous system development
- SCF-dependent proteasomal ubiquitin-dependent protein catabolic process
- protein ubiquitination

### Our prior research

Phenotypes explicitly recommended as core:
- developmental delay / global developmental delay
- intellectual disability
- speech and language impairment
- hypotonia
- autism-spectrum or behavioral abnormalities

Phenotypes treated as secondary or spectrum-expanding:
- seizures, including infantile spasms
- congenital heart disease or cardiomyopathy
- hearing impairment
- ocular abnormalities
- corpus callosum abnormalities
- growth restriction or feeding difficulty
- mild dysmorphic facial features

Cell types proposed:
- neural progenitor cell
- neuron
- cerebral cortex neuron

Biological processes proposed:
- regulation of transcription by RNA polymerase II
- cerebral cortex development
- neuron migration
- neuron projection development
- dendrite development

### Comparison

Nico covers more observed phenotype breadth. Our research covers more disease-relevant cell and process specificity.

If the goal is a robust dismech pathophysiology model rather than a phenotype checklist, the missing pieces in Nico's YAML are not more symptoms; they are the cortical-neurodevelopment nodes and cell/process annotations that connect MED13 dysfunction to the phenotype trunk.

## 4. What Nico has that ours does not

- A nearly complete first-pass dismech entry with genetics and treatment sections already scaffolded.
- Better direct coverage of later human phenotype-expansion papers.
- Explicit supportive-care/treatment placeholders:
  - speech therapy
  - genetic counseling
  - supportive care
- A useful variant-specific phosphodegron / Fbw7 turnover hypothesis node.
- Cleaner phenotype-level evidence blocks for ASD, Duane anomaly, optic nerve abnormalities, and hearing loss.

## 5. What ours has that Nico does not

- A defendable disease anchor strategy:
  - use `MONDO:0032485` `intellectual developmental disorder 61`
  - keep `MONDO:0100038` `complex neurodevelopmental disorder` only as broader ClinGen context
- Stronger mechanistic specificity around cortical development and neuronal connectivity.
- Explicit recognition that severe cardiac / mitochondrial presentations may be spectrum extensions or allele-specific outliers, not the core default disease frame.
- Candidate cell types and processes that are much closer to how the ideal pathophysiology graph should be structured.
- Explicit preservation of unresolved modeling decisions for future curators.

## 6. Quality issues

### Nico YAML: substantive issues

1. **Disease ontology mapping is too broad and likely wrong for the disorder entry.**
   The YAML uses `MONDO:0001071` `intellectual disability`, which is a broad parent concept, not the MED13-specific disease. Our prior research and the local G2P row both point to `MONDO:0032485` `intellectual developmental disorder 61` as the better disease anchor.

2. **The mechanism is under-specified downstream of Mediator dysfunction.**
   The YAML captures "transcriptional regulation" and a phosphodegron node, but it misses the stronger cortical-neurodevelopment bridge from our prior research: cortical neuron migration, projection, and dendritic maturation.

3. **Frequency bands may be more confident than the supplied evidence snippets justify.**
   Several frequencies are plausible, but the quoted snippets often support association only, not the exact `VERY_FREQUENT` / `FREQUENT` / `OCCASIONAL` band.

4. **Some phenotype mappings are broad parent terms.**
   Examples include `Facial dysmorphism` mapped to `HP:0000271` `Abnormality of the face` and `Congenital heart defects` mapped to `HP:0001627` `Abnormal heart morphology`. These are not necessarily invalid, but they leave specificity on the table.

### Nico PR branch: research markdown issues

The accompanying `research/MED13_Syndrome-deep-research-perplexity.md` is not reliable provenance in its current form. It contains:

- large blocks of prompt/template boilerplate
- a wrong MONDO identifier: `MONDO:0700197`, which is `porcine leukemia`
- a wrong HGNC identifier: `HGNC:6974`, which is `MDM4`, not `MED13`

Those problems do not all appear in the YAML itself, but they are important because they show the branch's research artifact is contaminated and should not be treated as trustworthy support for future curation.

### Our prior research: limitations

1. **It is strategy-grade, not YAML-grade.**
   Our documents do not yet contain validator-ready evidence snippets, final ontology mappings, or treatment sections.

2. **Phenotype breadth is intentionally conservative.**
   That makes the disease trunk cleaner, but it means Nico's YAML is better than our notes at capturing the broader published human phenotype spectrum.

3. **The strongest new mechanistic paper still needs dismech-style evidence packaging.**
   We cite the 2026 cortical-neuron study by DOI and use it conceptually, but it still needs exact evidence extraction and formal integration into a future YAML entry.

## 7. Best synthesis

The ideal merged MED13 entry would look like this:

1. Use `MONDO:0032485` `intellectual developmental disorder 61` as the disease anchor, with a note that ClinGen validity sits on broader `MONDO:0100038`.
2. Keep Nico's genetics section, including de novo predominance, truncating-versus-missense spectrum, and haploinsufficiency support.
3. Keep Nico's broad human phenotype coverage, but split it into:
   - core phenotypes: ID, developmental delay, speech/language delay, hypotonia, behavioral/autism-spectrum features
   - secondary/spectrum phenotypes: seizures, heart disease, hearing loss, optic/ocular findings, corpus callosum abnormalities, microcephaly, Duane anomaly
4. Replace the current generic pathophysiology center with a more specific trunk:
   - MED13 kinase-module dysfunction
   - dysregulated developmental transcription
   - impaired cortical neuron migration/projection/dendritic maturation
   - neurodevelopmental phenotypes
5. Keep the phosphodegron / impaired turnover mechanism, but clearly position it as an allele-specific or missense-enriched branch rather than the whole disease mechanism.
6. Add richer cell/process annotations from our research:
   - cell types: neural progenitor cell, neuron, cerebral cortex neuron
   - processes: regulation of transcription by RNA polymerase II, cerebral cortex development, neuron migration, neuron projection development, dendrite development
7. Use Nico's treatment placeholders as supportive management content.
8. Revisit phenotype frequency tags only where there is direct quantitative support.

## Final assessment

Nico's PR is not redundant in the sense of "nothing to learn here." It contributes real value on phenotype breadth, genetics scaffolding, and practical entry completeness. Our earlier research contributes the stronger disease anchor, the stronger mechanistic trunk, and the more careful boundary-setting around what is core versus spectrum-extending.

If we merge the strongest parts of both, the result should be a MED13 entry that is:

- anchored to the right disease term
- broader than our initial conservative notes on phenotype coverage
- more mechanistically specific than Nico's current YAML
- explicit about unresolved allele-specific and spectrum-boundary questions
