---
provider: openai
model: gpt-5.4
cached: false
start_time: "2026-04-13T01:21:32Z"
end_time: "2026-04-13T01:21:32Z"
duration_seconds: 0.0
template_file: codex_manual_curation
template_variables:
  disease_name: Bardet-Biedl Syndrome
  mondo_id: MONDO:0015229
  category: Mendelian
citation_count: 17
---

## Question

Manual deep-research synthesis for disease-level dismech curation of Bardet-Biedl
syndrome, with emphasis on disease framing, atomic pathophysiology, validated
PMID evidence, phenotype frequencies, and treatment-relevant mechanism mapping.

## Output

# Bardet-Biedl syndrome curation notes

## Disease framing

- Curate this as classic syndromic Bardet-Biedl syndrome, not as a loose bucket
  for every "BBS-like" ciliopathy.
- Keep the disease-level entry unified because the core mechanistic story is
  shared across established BBS genes: defective BBSome-dependent ciliary cargo
  trafficking.
- Capture genotype-specific severity differences in `genetic:` notes rather than
  exploding the entry into dozens of gene-specific subtypes. The strongest
  repeatedly supported contrasts are BBS1 versus BBS10.
- Useful framing papers for this boundary:
  - PMID:30614526 states BBS is a heterogeneous ciliopathy with "22 known genes"
    and retains the classic syndrome definition.
  - PMID:41219488 and PMID:37031301 show continued heterogeneity across recent
    molecular cohorts.

## Core mechanistic backbone

1. Biallelic pathogenic variants in established BBS genes initiate disease.
   Representative human cohort support: PMID:30614526, PMID:41219488.
2. These defects impair BBSome assembly or its chaperonin-assisted maturation.
   Best mechanistic assembly papers: PMID:22500027 and PMID:20080638.
3. An incompletely assembled BBSome disrupts ciliary cargo trafficking.
   Neuronal GPCR-trafficking support: PMID:36699005.
4. Tissue-specific consequences then branch:
   - Hypothalamus: impaired LepR trafficking/signaling drives leptin resistance,
     hyperphagia, and obesity (PMID:19150989, PMID:21209035, PMID:23776152,
     PMID:32700463).
   - Retina: rhodopsin mislocalization and photoreceptor death drive the
     invariant retinal dystrophy phenotype and progressive visual loss
     (PMID:15539463, PMID:35886001, PMID:22358239, PMID:41219488).
   - Kidney: renal dysmorphism, impaired function, and chronic
     tubulointerstitial disease are frequent and prognostically important
     (PMID:20876674, PMID:41219488).
   - Limb bud: altered Sonic hedgehog-dependent patterning explains postaxial
     polydactyly (PMID:18381349).

## Human phenotype and genotype highlights

- Retinal dystrophy is the most stable phenotype anchor.
  - PMID:35886001: all patients in the German ophthalmic cohort had retinal
    dystrophy.
  - PMID:41219488: retinal dystrophy 94.1%.
- Polydactyly and obesity are frequent but less invariant than retinal disease.
  - PMID:41219488: polydactyly 88.0%, obesity 68.0%.
  - PMID:32700463: overweight/obesity exceeded 90% after age 5 in the large
    pediatric registry.
- Kidney disease is common but more variable across cohorts.
  - PMID:20876674: renal abnormalities in 82%.
  - PMID:41219488: renal anomalies in 52.0%.
  - PMID:37031301: renal anomalies only 7.1% in that Chinese cohort, which is a
    reminder not to overstate invariance.
- BBS1 and BBS10 are the most reproducibly common genotype groups in many
  cohorts.
  - PMID:35886001: BBS10 32.8%, BBS1 24.6%.
  - PMID:21209035: BBS10 30%, BBS1 27%.
  - PMID:28143435: BBS1 followed by BBS10.
- BBS10 is the clearest severity signal.
  - PMID:28143435 links BBS10 to worse renal and ocular outcomes.
  - PMID:20876674 links BBS6/BBS10/BBS12 genotypes to more severe renal disease.

## Treatment curation choices

- Include setmelanotide because it has direct BBS phase 3 human evidence and a
  clear mechanistic rationale as downstream MC4R agonism (PMID:36356613).
- Include kidney transplantation because registry data support it for the ESRD
  subset (PMID:27245600).
- Do not overspecify generic supportive care unless the claim is directly
  abstract-supported for BBS itself.

## Evidence-quality decisions

- Prefer exact PMID-backed quotations from cohort abstracts or mechanistic
  abstracts over generic review prose.
- Use `HUMAN_CLINICAL` for patient cohorts, registries, transplant series, and
  trials.
- Use `MODEL_ORGANISM` for mouse or zebrafish mechanism papers.
- Use `OTHER` only where the abstract itself mixes multiple experimental modes
  and cannot be cleanly split without misclassifying the publication-level
  evidence.

## Claims intentionally downweighted or excluded

- Broad "all BBS genes" lists beyond clearly established syndrome genes were not
  overexpanded into the YAML because the disease entry should stay syndrome-level
  and mechanistically coherent.
- Behavioral, craniofacial, cardiac, and hearing findings were not made central
  pathophysiology nodes because the strongest disease-level mechanistic evidence
  is still the retina-hypothalamus-kidney-limb axis.
- Histopathology was not added as a standalone section even though
  PMID:20876674 supports chronic interstitial nephropathy of dysplastic nature;
  the evidence is used directly in the renal pathophysiology and phenotype
  instead.
