# Retinopathies Curation Project

## Overview

Curate retinopathy and retinal dystrophy branches for the dismech knowledge base
with explicit granularity rules. The goal is to avoid duplicated pathographs
while still separating entities whose proximal pathobiology, diagnosis, or
management genuinely diverge.

This project treats "retinopathy" as a mixed-use term. In some contexts it is a
phenotype label within a broader systemic disease. In others it denotes a
retinal disease family with a shared mechanistic trunk and clinically meaningful
subtypes. The project therefore starts from mechanism-first curation rather than
from ontology depth alone.

## Current Tension

Retinal diseases create a recurring lump-vs-split problem:

1. Broad umbrella terms such as `retinopathy` or `inherited retinal dystrophy`
   are often too heterogeneous for a single disease-level pathograph.
2. Gene-based MONDO descendants can be clinically useful, but creating one file
   per descendant often duplicates most of the mechanistic graph.
3. Some gene-centered families are coherent enough for a shared parent entry,
   but only if the child terms diverge late from a common proximal module.

## Working Granularity Principles

1. **Do not create one dismech file per MONDO term by default.**
   MONDO is multi-level; dismech curation should be guided by mechanism and
   modeling utility, not by ontology descent alone.

2. **Do not treat generic `retinopathy` as a default top-level disease entry.**
   In many contexts it is better modeled as a phenotype within a broader
   disorder.

3. **Use a disease-family umbrella when child entities share a strong proximal
   mechanism.**
   A family entry is justified when most descendants can reuse the same early
   pathograph trunk and differ mainly in retinal cell-type bias, topography,
   inheritance mode, or downstream clinical pattern.

4. **Split into separate top-level entries when the shared pathograph would be
   too thin.**
   Separate entries are favored when proximal pathobiology, diagnostic framing,
   prognosis, or treatment strategy materially differ.

5. **Subtype labels are not the same as severity labels.**
   Different retinal phenotypes may reflect rod-predominant, cone/macular-
   predominant, early severe, or syndromic branches of the same module rather
   than mere differences in degree.

6. **Digenic or inheritance-specific branches can stay under a shared parent.**
   A second-gene interaction or dominant/recessive split can be modeled as a
   meaningful subtype when the affected molecular complex or pathway is still the
   same.

7. **Treat MONDO placement as informative, not decisive.**
   Some ontology descendants may need special review if their canonical
   literature points to a different proximal mechanism than the parent family
   would imply.

## Initial Findings

### Broad project-level conclusions

- `Retinopathy` is already used in the current KB mostly as a phenotype label
  inside broader disorders rather than as a standalone disease.
- `Inherited retinal dystrophy` is too broad to serve as a default disease-level
  dismech entry.
- Gene-centered retinal families are often more useful than phenotype-numbered
  legacy labels when they capture a coherent proximal module.

### PRPH2-related retinopathy

`PRPH2-related retinopathy` is an initial positive test case for a shared
umbrella entry.

Why it looks coherent:

- PRPH2/peripherin-2 is a photoreceptor outer-segment rim/disc protein.
- PRPH2 also functions in a structural complex with ROM1.
- Many descendant diseases appear to share a common proximal trunk involving
  altered PRPH2 dosage, folding/trafficking, oligomerization, or PRPH2-ROM1
  complex assembly.
- Descendant terms such as retinitis pigmentosa 7, vitelliform macular
  dystrophy 3, patterned macular dystrophy 1, central areolar choroidal
  dystrophy 2, and Leber congenital amaurosis 18 look more like downstream
  rod-biased, cone/macular-biased, or early severe branches than entirely
  separate molecular pathways.

Implication for modeling:

- The shared trunk should live in the parent entry.
- Child terms should branch later in the graph where retinal cell type,
  topography, onset, severity, or inheritance context diverge.
- `retinitis pigmentosa 7, digenic` should likely be retained as a subtype or
  explicit genetic-context branch rather than as a fully separate root entry,
  because the additional ROM1 contribution still acts within the same structural
  module.

Caution:

- Terms such as fundus albipunctatus and retinitis punctata albescens require
  extra review before being folded into a PRPH2 family pathograph, because their
  canonical literature often points to visual-cycle mechanisms in other gene
  families.

## Candidate Curation Strategy

### Family umbrellas worth evaluating

| Family / Concept | Proposed modeling | Rationale | Status |
|------------------|-------------------|-----------|--------|
| PRPH2-related retinopathy | Shared parent with subtype branches | Strong common outer-segment structural module | [ ] |
| RPGR-related retinopathy | Shared parent with subtype branches | Multiple clinically distinct descendants on one gene-centered family | [ ] |
| RDH5-related retinopathy | Shared parent with subtype branches | Multiple named descendants, likely shared visual-cycle module | [ ] |
| RLBP1-related retinopathy | Shared parent with subtype branches | Multiple related visual-cycle retinopathy phenotypes | [ ] |

### Likely standalone retinal disease entries

| Disease / Family | Proposed modeling | Rationale | Status |
|------------------|-------------------|-----------|--------|
| Stargardt disease | Standalone disease with subtypes | Existing KB entry; clinically coherent macular dystrophy with ABCA4-centered trunk | [x] |
| RPE65-related recessive retinopathy | Standalone disease or very tight family entry | Strong therapy relevance and clear clinical framing | [ ] |
| Microcephaly and chorioretinopathy syndromes | Standalone syndromic disease entries | Not just retinal disease; broader syndromic mechanism and phenotype | [ ] |

### Concepts to keep as parents / project labels, not default disease files

- `retinopathy`
- `inherited retinal dystrophy`
- `hereditary macular dystrophy`

## Existing Related Entries in KB

| Disease | File | Notes |
|---------|------|-------|
| Stargardt Disease | `Stargardt_Disease.yaml` | Existing retinal dystrophy entry with internal subtype structure |
| Age-Related Macular Degeneration | `Age_Related_Macular_Degeneration.yaml` | Distinct retinal disease with separate clinical framework |
| Pars Planitis | `Pars_Planitis.yaml` | Retinal inflammation/vasculitis context rather than inherited dystrophy |
| Retinoblastoma | `Retinoblastoma.yaml` | Retinal neoplasia, clearly separate from retinopathy families |

---
# STATUS

## Principles and Scoping
- [x] Established a working granularity framework for retinal disease families
- [x] Distinguished phenotype-level retinopathy use from disease-family use
- [x] Identified PRPH2-related retinopathy as a candidate shared-mechanism umbrella
- [x] Flagged fundus albipunctatus / retinitis punctata albescens as caution terms for blind inheritance from ontology structure

## Initial Curation Targets
- [ ] Curate `PRPH2-Related_Retinopathy`
- [ ] Review `RPGR-related retinopathy` branch for family-entry viability
- [ ] Review `RPE65-related recessive retinopathy` for standalone-entry viability
- [ ] Review `RDH5` and `RLBP1` branches with attention to visual-cycle mechanisms

# NOTES

## 2026-03-18

- Added a retinopathy-specific project note to capture general lump-vs-split
  findings before individual disorder curation.
- Recorded the working rule that shared-mechanism retinal families may justify a
  parent entry, but ontology descendants should not automatically become
  top-level dismech files.
- Documented PRPH2-related retinopathy as the first detailed test case for a
  shared-trunk retinal family entry.
