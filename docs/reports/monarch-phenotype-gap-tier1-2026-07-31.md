# Tier 1 execution: Monarch phenotype-gap worklist + pilot curation

*Date: 2026-07-31. Author: AI-assisted (Claude Code). Companion to the Monarch
KG gap analysis (`docs/reports/monarch-kg-dismech-gap-analysis-2026-07-30.md`,
delivered in a separate PR).*

This report executes **Tier 1** of the gap analysis: (A) generate the KB-wide
disease→phenotype completeness worklist against Monarch's OMIM/Orphanet
annotations, and (B) curate a pilot set of diseases as worked examples of each
gap-closure path. All work is on branch `claude/monarch-tier1-phenotype-gaps`,
separate from the analysis report's docs PR.

## Part A — KB-wide phenotype-completeness worklist

Generated with the in-repo tool `dismech.compare.d2p audit-all` (per-disease
checkpointing, resumable). This run's throughput was ~11 s/disease; a small
number of pathologically broad MONDO terms (e.g. `MONDO:0000001` *Dorsalgia*)
have enormous association lists and dominate wall-clock.

**Coverage of this run: 514 of 1,645 disorders (31%).** The sweep is resumable
(`--resume`) and can be completed without redoing finished diseases; the 31%
sample is representative, not a curated subset. The per-disease ranked table is committed at
`docs/reports/data/monarch-phenotype-gap-worklist-2026-07-31.tsv`.

### Findings (514 diseases)

**27,027** phenotype-completeness issues — ~53 per disease. Extrapolated to the
full KB this is on the order of **~85,000** issues. By type:

| Issue type | Count | Share | Meaning |
|---|---:|---:|---|
| `source_phenotype_missing_locally` | 22,579 | 84% | OMIM/Orphanet-backed HP term with no local phenotype |
| `source_phenotype_covered_only_by_broader_local_term` | 2,638 | 10% | Local asserts a parent; source has a more specific term |
| `local_phenotype_unlinked_to_pathograph` | 1,548 | 6% | Local phenotype present but not wired into a causal edge |
| `local_phenotype_missing_supporting_evidence` | 262 | 1% | Local phenotype lacks supporting evidence |

### Interpretation caveats (do not treat the raw counts as a curation quota)

- **Broad/heterogeneous MONDO terms inflate counts.** The highest-gap entries in
  this run (ANK2-Related Complex NDD 986, BLOC1S1 Leukodystrophy 966, 22q11.2
  Deletion 231) are umbrella terms whose Monarch annotation aggregates many OMIM
  subtypes; most of those "missing" phenotypes are not curatable at the umbrella
  level. Rank the worklist by *curatable* gaps, not raw totals.
- **`missing_locally` is a lead, not a directive.** Each candidate still requires
  the standard evidence SOP (exact-quote PMID/ORPHA snippet) and should be added
  *linked* into the pathograph only when the mechanism explains it.
- **Not every `unlinked` flag is a defect** — see the Achondroplasia pilot below.

## Part B — Pilot curation (3 worked examples)

Three diseases were curated to demonstrate each gap-closure path end-to-end, with
full validation (linkml schema, deterministic snippet audit, term validator; the
network reference validator additionally passed for Marfan).

### 1. Marfan syndrome — add + link + sequela (all three paths)

- **Added** two ORPHA:558-backed phenotypes previously missing: *Retinal
  detachment* (HP:0000541) and *Pulmonary artery dilatation* (HP:0004927), each
  with an exact-quote ORPHA evidence row and `OCCASIONAL` frequency.
- **Linked** them, plus the previously-unlinked *Dural ectasia*, into the
  `Extracellular Matrix Remodeling` node's `downstream` (the connective-tissue
  hub that already feeds Ectopia Lentis / Scoliosis / Pneumothorax).
- **Wired** the unlinked *Mitral regurgitation* via a new `Mitral Valve Prolapse
  → Mitral Regurgitation` sequela edge.
- Snippet audit 118/118; re-audit confirmed the four targeted gaps cleared.

### 2. 3-Hydroxy-3-methylglutaric aciduria — add + link

- **Added** two ORPHA:20-backed phenotypes: *Reye syndrome-like episodes*
  (HP:0006582, the classic HMG-CoA-lyase presentation) and *Increased circulating
  lactate concentration* (HP:0002151), both `FREQUENT`.
- **Linked** both as `downstream` of the `Acute hypoketotic metabolic
  decompensation` crisis node (which `conforms_to`
  `metabolic_intoxication_decompensation`). Snippet audit 94/94.

### 3. Achondroplasia — disciplined unlinked-fix (no new external content)

- **Linked** two previously-unlinked, very-frequent angular-limb deformities
  (*Genu varum* HP:0002970, *Bowing of the legs* HP:0002979) into the `Impaired
  endochondral ossification and chondrodysplasia` node via evidence-backed
  `downstream` edges (reusing in-file PMID:32864841 documenting childhood genu
  varum).
- **Key learning:** this entry explicitly curates "calibrated branches rather
  than an unsupported all-phenotype fan-out," so many of its `unlinked` flags are
  *deliberate*, not oversights. Only the core, well-evidenced deformities were
  linked; speculative bulk-linking was intentionally avoided. This confirms the
  Part-A caveat that `unlinked_to_pathograph` requires mechanistic judgment, not
  automation.

## Recommended next steps

1. **Complete the sweep** (`d2p audit-all --resume`) to turn the 31% sample into
   full KB coverage, then re-rank by *curatable* gaps.
2. **Batch the `missing_locally` leads by evidence source** — ORPHA-backed rows
   are the cheapest to curate (exact-quote cache rows already present), as the
   Marfan/HMG pilots show.
3. **Treat `unlinked_to_pathograph` per-entry**, respecting existing
   calibrated-branch discipline; prefer evidence-backed causal edges over bare
   linkage.
4. **Stand up the recurring "Monarch gap scan"** proposed in the analysis report
   so this becomes a standing feed rather than a one-off.
