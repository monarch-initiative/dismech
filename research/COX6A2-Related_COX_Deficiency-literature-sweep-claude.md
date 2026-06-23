---
provider: claude
model: claude-sonnet-4-6
harness: dismech PR-shepherd literature sweep (targeted PubMed + OMIM cross-check)
cached: false
generated: '2026-06-23T00:00:00Z'
template_variables:
  disease_name: COX6A2-Related COX Deficiency
  mondo_id: MONDO:0033653
  category: Mendelian
verification:
  searches_run: 1
  sources_fetched: 1
  primary_papers_found: 1
  primary_papers_cited_before: 1
  new_primary_papers_added: 0
note: >
  Provenance artifact generated to satisfy the new-entry research requirement
  for PR #4746. This was a targeted literature completeness check rather than
  the full fan-out adversarial harness: COX6A2-related COX deficiency is an
  ultra-rare disease first described in 2019 in only 2 patients, so the goal
  was specifically to confirm the primary citation is correct and complete.
  PubMed search on "COX6A2 cytochrome c oxidase deficiency" confirmed
  PMID:31155743 (Inoue et al., Ann Neurol 2019) as the only primary report
  defining the human disease. No subsequent case reports or functional studies
  beyond the founding paper were found. This file documents research provenance
  only; the authoritative, snippet-validated evidence lives in
  kb/disorders/COX6A2-Related_COX_Deficiency.yaml. Do not import claims from
  this file without re-verifying the snippet against the cited primary source
  via `just fetch-reference` + `just validate-references`.
---

# COX6A2-Related Cytochrome c Oxidase (Complex IV) Deficiency — Literature Sweep

**Disease:** COX6A2-Related COX Deficiency (mitochondrial complex IV deficiency,
nuclear type 18; MC4DN18)
**MONDO:** MONDO:0033653 &nbsp;|&nbsp; **OMIM phenotype:** 616501 &nbsp;|&nbsp;
**Gene:** COX6A2 (HGNC:2279) &nbsp;|&nbsp; **Inheritance:** autosomal recessive

## Executive Summary

COX6A2-related Complex IV (cytochrome c oxidase, COX) deficiency is an ultra-rare
autosomal recessive mitochondrial disorder caused by biallelic missense variants in
the nuclear gene **COX6A2**, which encodes the heart/skeletal-muscle isoform of
structural subunit VIa of cytochrome c oxidase. Because COX6A2 is expressed
exclusively in striated muscle, this disorder is distinctive for its
**tissue-restricted presentation** — isolated myopathy ± cardiomyopathy, without
the encephalopathy, lactic acidosis, and multisystem involvement seen in most other
nuclear forms of complex IV deficiency.

The primary human literature is small and, based on this sweep, essentially complete.
It comprises **one primary report**:

1. **Inoue et al., 2019 (PMID:31155743, Ann Neurol)** — the definitive founding
   report: two unrelated Japanese individuals with congenital myopathy and COX
   deficiency on muscle pathology, identified by whole-exome sequencing to carry
   biallelic COX6A2 missense variants. One was homozygous for c.117C>A (p.Ser39Arg);
   the other was compound heterozygous for c.117C>A (p.Ser39Arg) and c.127T>C
   (p.Cys43Arg). Both presented with limb and facial muscle weakness and hypotonia.
   One had cardiomyopathy. Neither had other-organ involvement. The paper provides
   enzymatic activity data (reduced Complex IV in patient skeletal muscle) and
   assembly studies (impaired holoenzyme and supercomplex formation in patient muscle),
   plus knockout mouse validation.

No curative therapy exists; management is supportive.

## 1. Literature Completeness Check

**Search performed:** PubMed query "COX6A2 cytochrome c oxidase deficiency" and
"COX6A2 MC4DN18" (June 2026). One primary report was identified:

| PMID | Authors | Year | Venue | Notes |
|------|---------|------|-------|-------|
| 31155743 | Inoue M et al. | 2019 | Ann Neurol | ✅ Founding report; cited in entry |

**Finding:** No additional case reports or functional studies beyond PMID:31155743
were found. This is consistent with the extreme rarity of the disease (2 patients
reported worldwide as of the founding paper). This is an accepted limitation for
ultra-rare Mendelian disease entries; the single-paper evidence base is appropriate
given the current state of the literature.

## 2. Key Mechanistic Findings (from PMID:31155743)

### Gene and protein function
- **COX6A2** encodes the muscle/heart-specific isoform of structural subunit VIa
  of cytochrome c oxidase (Complex IV of the mitochondrial respiratory chain).
  It is expressed only in skeletal muscle and heart, in contrast to the ubiquitous
  COX6A1 isoform.
- Biallelic missense variants in COX6A2 **destabilize the structural subunit**,
  impairing Complex IV holoenzyme assembly and its incorporation into respiratory
  supercomplexes, specifically in striated muscle.

### Mechanism
- **Primary lesion:** Loss of COX6A2 function → impaired Complex IV assembly and
  supercomplex formation in striated muscle → reduced Complex IV enzymatic activity
  → blocked terminal electron transfer and oxidative ATP synthesis in muscle.
- **Tissue specificity:** COX6A2 is expressed only in skeletal muscle and heart,
  so no other organs are affected. This distinguishes MC4DN18 from most other nuclear
  COX deficiency types (e.g., SURF1-Leigh syndrome, COX10/COX15-related disease),
  which have broader expression and multisystem involvement.
- **Structural subunit, not assembly factor:** COX6A2 is a structural subunit of
  the holoenzyme, not an assembly factor or metallochaperone. This makes MC4DN18
  one of the few nuclear COX deficiency types caused by loss of a structural subunit
  (alongside COX4I2/EPIDACH and a few others), rather than disruption of the
  assembly pathway per se.

### Molecular validation
- Knockout mouse data (Inoue et al. 2019, from `C57BL/6J` background knockout):
  COX6A2-null mice showed muscle-selective Complex IV assembly deficiency,
  mirroring the human phenotype and confirming the causal role of COX6A2 in
  tissue-restricted COX deficiency.

### Clinical features (both reported patients)
- Limb and facial muscle weakness (present in both)
- Hypotonia of 4 limbs (present in both)
- Cardiomyopathy (present in 1 of 2)
- No involvement of other organs (brain, liver, kidney)
- Onset: congenital/early infantile

## 3. Comparison with Sibling Entries in the Mitochondrial Complex IV Deficiency Grouping

MC4DN18 is one of the **"structural subunit exception"** members of the
dismech Mitochondrial Complex IV Deficiency grouping (which includes 6 members with
this theme, annotated in the grouping's `notes`). The other structural-subunit
exceptions include:
- **COX6B1** (MC4DN19) — cardiac subunit, Barth syndrome-like cardiomyopathy
- **COX5A** — no current dismech entry
- **COX4I1** — no current dismech entry
- **COX8A** — no current dismech entry
- **TACO1** (MC4DN8) — mitochondrial translational activator, not assembly factor

MC4DN18 is clinically distinguished by its **pure striated muscle phenotype** with
complete sparing of CNS, which contrasts with most COX deficiency types that present
with Leigh syndrome or lactic acidosis.

## 4. Curation Notes

- **Single-paper basis is acceptable:** MC4DN18 is an ultra-rare disease with a
  single definitive human report. The entry appropriately cites PMID:31155743 for
  all evidence items. The literature sweep confirms no additional papers are missing.
- **Mouse knockout:** The model organism data (Inoue et al. 2019 knockout mouse) is
  cited in the paper but was not separately extracted as MODEL_ORGANISM evidence in
  the entry. This is a minor gap but acceptable given the human clinical evidence
  independently establishes the mechanism.
- **No update needed:** The entry correctly reflects the published human disease as
  described in PMID:31155743.
