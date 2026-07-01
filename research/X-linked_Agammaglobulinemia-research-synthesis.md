# X-linked Agammaglobulinemia Research Synthesis

## Scope and provenance

This is a **manually authored curation synthesis** for the X-linked
agammaglobulinemia (XLA) entry (`kb/disorders/X-linked_Agammaglobulinemia.yaml`),
not a reconciliation of automated deep-research (Falcon/OpenScientist/etc.) tool
dumps — no such tool artifact was generated for this disorder. Every claim below
is anchored to a reference whose abstract was fetched into `references_cache/`
and whose quoted snippet was verified as an exact substring per the dismech
anti-hallucination SOP.

- Disease: X-linked agammaglobulinemia (XLA / Bruton agammaglobulinemia)
- MONDO: `MONDO:0010421` (Bruton-type agammaglobulinemia)
- Gene: **BTK** (`hgnc:1133`), OMIM:300755
- Inheritance: X-linked recessive

### NEC (named-entity-confusion) preflight

Before curation, the disease identity was confirmed against the MONDO record:
the causal gene **BTK** and **OMIM:300755** match the intended entity. The
synonyms (XLA, Bruton agammaglobulinemia, BTK deficiency) resolve to the same
MONDO term, with no aliasing to a distinct agammaglobulinemia entity (the
autosomal forms — e.g. mu heavy chain, BLNK, Igβ — are explicitly out of scope
for this X-linked entry). During curation the SOP caught a mis-recalled PMID
(an unrelated adenovirus paper) that was replaced with the correct landmark
citation.

## Verified reference set

| PMID | Role | Evidence type | Anchors |
|------|------|---------------|---------|
| 8380905 | Vetrie 1993, *Nature* — gene identification | HUMAN_CLINICAL | BTK is the XLA gene; failure of pre-B cells to develop into circulating mature B cells |
| 8425221 | Tsukada 1993, *Cell* — companion gene identification | HUMAN_CLINICAL | Deficient BTK (BPK) kinase expression/activity in XLA pre-B and B cells; severe deficit of B and plasma cells + profound hypogammaglobulinemia |
| 16862044 | Winkelstein 2006 — US registry of 201 patients | HUMAN_CLINICAL | Phenotype frequencies (otitis 70%, pneumonia 62%, sinusitis 60%, etc.); disseminated enterovirus as a leading cause of death |
| 8332901 | Rawlings 1993 — Xid mouse model | MODEL_ORGANISM | BTK kinase loss underlies XLA, characterized by failure to produce B cells |
| 34241796 | Cardenas-Morales 2022 — review | HUMAN_CLINICAL | B-cell developmental defect → absent/diminished immunoglobulin production |
| 37454339 | Nishimura 2023 — international HCT survey | HUMAN_CLINICAL | Lifelong IgRT standard of care; allogeneic HCT reserved for severe complications |

## Mechanistic synthesis (pathophysiology graph)

The curated causal chain is fully connected from molecular lesion to clinical
output:

1. **BTK loss of function impairs B-cell receptor signaling** (Tsukada 1993;
   Rawlings 1993 Xid model) →
2. **Arrest of B-cell development at the pre-B stage** (Vetrie 1993: "failure of
   pre-B cells in the bone marrow to develop into circulating mature B cells") →
3. branches to **decreased total B-cell count** (phenotype) and
   **panhypogammaglobulinemia from absent plasma cells** (Cardenas-Morales 2022) →
4. panhypogammaglobulinemia branches to **recurrent infections** (Winkelstein
   2006, infection the presenting feature in 85%) and to **susceptibility to
   disseminated enteroviral infection** (Winkelstein 2006, disseminated
   enterovirus a leading cause of death) — the absent neutralizing antibody is
   the shared intermediate for both downstream arms.

This graph was the focus of the pathophysiology fixes in this PR: two dangling
edge targets were corrected to their canonical node names, one misdirected edge
was repointed from the *phenotype* "Panhypogammaglobulinemia" to the
*pathophysiology node* "Panhypogammaglobulinemia from Absent Plasma Cells", and
a previously orphaned "Susceptibility to Disseminated Enteroviral Infection"
node was given an incoming edge from the panhypogammaglobulinemia node.

## Curation implications and follow-up checks

- The current entry models the core BTK → pre-B arrest → panhypogammaglobulinemia
  → infection chain. Remaining (non-blocking) enrichment opportunities flagged in
  PR review: an IUIS `classifications` block (predominantly antibody
  deficiencies), the decreased circulating IgM phenotype (HP:0002850), the
  >10% registry phenotypes conjunctivitis (21%, HP:0000509) and pyoderma/
  cellulitis (18%, HP:0100658), and active mining of the XLA GeneReviews article.
- Do not promote report prose directly into YAML evidence; keep every snippet
  tied to fetched reference-cache text and re-validate with
  `just validate-references` before committing.
