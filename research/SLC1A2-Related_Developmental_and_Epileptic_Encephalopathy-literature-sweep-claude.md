---
provider: claude
model: claude-sonnet-5, claude-haiku-4-5-20251001
harness: dismech PR #8035 targeted literature-gap sweep (WebSearch/WebFetch + NCBI e-utilities verification)
cached: false
generated: '2026-09-05T00:00:00Z'
template_variables:
  disease_name: SLC1A2-Related Developmental and Epileptic Encephalopathy
  mondo_id: MONDO:0014916
  category: Mendelian
verification:
  searches_run: 8
  sources_fetched: 6
  primary_papers_found_new: 3
  primary_papers_cited_before: 7
  new_primary_papers_added: 3
note: >
  Provenance artifact generated to close the mandatory new-entry deep-research
  gate flagged in PR #8035 review. The full fan-out deep-research workflow
  errored out on a StructuredOutput schema bug in its scoping step, so this is
  a targeted literature-gap sweep run directly against PubMed/NCBI rather than
  the generic disease-characteristics harness: it was scoped specifically to
  the reviewer's stated concern (a suspected earlier Kovermann et al. Brain
  paper reporting the SLC1A2 anion-current gain-of-function) plus a broader
  check for post-2022 clinical/pharmacology literature. All PMIDs below were
  independently confirmed real by fetching the abstract/full text with
  `just fetch-reference` (not just search-engine snippets) before any claim
  from them was used in the entry. This file documents research provenance
  only; the authoritative, snippet-validated evidence lives in
  kb/disorders/SLC1A2-Related_Developmental_and_Epileptic_Encephalopathy.yaml.
  Do not import claims from this file without re-verifying the snippet against
  the cited primary source via `just fetch-reference` +
  `just validate-references`.
---

# SLC1A2-Related Developmental and Epileptic Encephalopathy (DEE41) — Literature Sweep

**Disease:** SLC1A2-Related Developmental and Epileptic Encephalopathy (DEE41; EAAT2/GLT-1)
**MONDO:** MONDO:0014916 &nbsp;|&nbsp; **Gene:** SLC1A2 (hgnc:10940) &nbsp;|&nbsp;
**Inheritance:** autosomal dominant (de novo), rare recessive form also reported

## Why this sweep was run

The entry (PR #8035) originally cited 7 references and modeled three competing
mechanistic hypotheses for how SLC1A2 missense variants cause disease: (1) canonical
dominant-negative transport loss-of-function, (2) an alternative anion-pore
glutamate-efflux gain-of-function, supported only by Kovermann et al. 2022
(PMID:34961934), and (3) an emerging STIM1/Orai1 SOCE-disruption arm. A reviewer
(`ai4c-reviewer`) flagged, **as an unverified lead**, a recollection of "an earlier
Kovermann et al. paper in *Brain* (~2017) on the p.Pro289Arg variant" that might be the
primary source for the anion-pore mechanism, and treated the single-paper support for
that hypothesis as evidence of broader literature under-consumption for a well-studied
gene.

## 1. Resolving the "Kovermann *Brain* ~2017" lead

**No such paper exists.** PubMed searches for "Kovermann SLC1A2 Brain",
"Kovermann EAAT2 anion current epileptic encephalopathy", and related terms turn up no
2017 *Brain* paper on SLC1A2/EAAT2. The reviewer's recollection is most consistent with
a real but different paper:

- **PMID:23107647** — Winter N, Kovermann P, Fahlke C. "A point mutation associated
  with episodic ataxia 6 increases glutamate transporter anion currents." *Brain*.
  2012 Nov;135(Pt 11):3416-25.
  - This paper *is* the first report of glutamate-transporter anion-channel gain of
    function as a disease mechanism, matching "Kovermann", "Brain", and "anion current
    gain-of-function" in the reviewer's recollection — but the gene is **SLC1A3/EAAT1**
    (not SLC1A2/EAAT2), the variant is **P290R** (not P289R), and the disease is
    **episodic ataxia 6** (not DEE41). It is a paralogous-gene precedent, not a source
    for this entry's evidence chain, and was **not** added to the KB entry.

The actual, and only, primary source for the SLC1A2 anion-pore gain-of-function finding
remains PMID:34961934 (Kovermann, Kolobkova, Franzen, Fahlke; *Epilepsia* 2022),
already cited. That single-paper support is genuine (not an oversight), but see §2 for
independent corroboration found by this sweep.

## 2. New primary literature added to the entry

| PMID | Authors | Year | Venue | Role in entry |
|------|---------|------|-------|----------------|
| 40174554 | Kovermann P, Bayat A, Fenger CD, et al. | 2025 | EBioMedicine | ✅ Added — independent 18-patient/13-variant cohort |
| 33507976 | Ramandi D, Elahdadi Salmani M, et al. | 2021 | PLoS One | ✅ Added — ceftriaxone/GLT-1 rodent TLE model |
| 34571003 | Green JL, Dos Santos WF, Fontana ACK | 2021 | Biochem Pharmacol | ✅ Added — EAAT2-directed therapeutics review |

**PMID:40174554 is the most valuable finding of this sweep.** It is a large
multi-center genotype-phenotype cohort (18 individuals, 13 SLC1A2 variants — more than
double the 6-individual Stergachis 2019 cohort already cited) that:

- Reports a **fourth pore-lining variant, p.Leu85Arg (L85R)**, functionally grouped
  with Gly82Arg/Leu85Pro/Pro289Arg in the same "mixed loss-of-transport/gain-of-anion-
  channel function" molecular category — now added to the `genetic` section.
- Directly and independently corroborates the anion-pore/gain-of-function hypothesis
  **at the clinical level**: "the disease symptoms of individuals harbouring variants
  causing 'mixed loss-of-transport/gain-of-anion-channel function' are more severe than
  symptoms caused by the 'loss-of-function' variants, suggesting that anion channel gain
  of function is an important pathogenic factor." This is exactly the kind of second,
  independent line of evidence the reviewer's concern was pointing at — now added as
  evidence on the `anion_pore_glutamate_efflux_model` hypothesis.
- Also reports two novel variants (I276S, G360A) causing a third, milder "mild
  gain-of-anion-channel-function" molecular phenotype with no transport loss. These are
  **not** added to the KB entry: no case-level phenotype detail comparable to the
  recurrent dominant alleles is available for them individually, and adding them would
  require re-deriving frequency/severity claims this sweep did not verify in full.

PMID:33507976 and PMID:34571003 were added to the Ceftriaxone treatment section: the
former is an independent rodent temporal-lobe-epilepsy model showing ceftriaxone's
GLT-1-upregulation mechanism works as intended in another epilepsy context (supporting
why the DEE41 trial was mechanistically well-motivated even though it failed); the
latter is a 2021 pharmacology review noting EAAT2 positive allosteric modulation as an
alternative to transcriptional upregulation — not yet reported as tested in DEE41
specifically, but noted for completeness of the treatment landscape.

## 3. Additional case reports and studies: not added

Two additional SLC1A2 case reports were referenced in secondary search results (a SAGE
Open Medical Case Reports item from Nov 2024, and an International Journal of
Contemporary Pediatrics case report), plus a tangential astrocytic-YAP/EAAT2/ischemic-
stroke apoptosis paper. **None of these could be independently resolved to a verified
PMID with fetchable abstract text**, so none were added — they are flagged here as
unconfirmed leads for a future sweep, not as citations.

## 4. Cell death mechanism (apoptosis vs. necrosis)

The entry previously removed a `GO:0006915 apoptotic process` annotation for lack of
support. This sweep found no SLC1A2/EAAT2-specific primary paper establishing apoptotic
(as opposed to necrotic or unspecified excitotoxic) neuronal death. PMID:36543780
(Qu et al., already cited, the actual functional-mechanism paper for this disease's
variants) does not report a cell-death readout at all. **No change made** — the prior
removal stands correct.

## 5. EAAT anion-channel blockers: a genuine literature gap, not an omission

No PubMed-indexed paper was found reporting a selective EAAT2 anion-channel blocker
tested against the disease-associated efflux variants (G82R/L85P/L85R/P289R), in vitro
or in vivo. PMID:34961934's own Significance section only speculates that such
antagonists "could serve as therapeutic agents in the future" — a forward-looking
statement, not a tested compound. This is recorded here so a future reviewer does not
re-flag it as an under-searched gap: it was searched, and nothing exists yet.

## Summary of entry changes made after this sweep

1. `mechanistic_hypotheses[anion_pore_glutamate_efflux_model]`: added PMID:40174554
   evidence + description update (independent clinical severity corroboration, L85R).
2. `genetic[SLC1A2]`: added PMID:40174554 evidence + notes update (L85R variant).
3. `treatments[Ceftriaxone]`: added PMID:33507976 (rodent proof-of-concept) and
   PMID:34571003 (PAM alternative) evidence + description update.
4. Unrelated to this sweep: three `supports: PARTIAL` values left over from before the
   #10003 enum narrowing (merged into `main` after this PR's last update) were migrated
   to `SUPPORT` + `directness: INDIRECT` (two cases) or plain `SUPPORT` (one case, where
   the quoted text directly supported the actual claim being made) per the CLAUDE.md
   migration table, and `main` was re-merged to pick up all schema/policy drift since
   2026-08-08.
