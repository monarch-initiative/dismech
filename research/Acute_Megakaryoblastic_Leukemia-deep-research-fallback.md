# Acute Megakaryoblastic Leukemia Deep Research Fallback

## Provider Attempts

- 2026-05-08T18:00Z: `just research-disorder asta Acute_Megakaryoblastic_Leukemia`
  failed because `ASTA_API_KEY` was not set; the runner reported
  `ERROR - No research providers available. Please set API keys`.
- 2026-05-08T18:00Z: `just research-disorder openai Acute_Megakaryoblastic_Leukemia`
  failed for the same reason (no `OPENAI_API_KEY`).
- 2026-05-08T18:00Z: `just research-disorder perplexity Acute_Megakaryoblastic_Leukemia`
  failed for the same reason (no `PERPLEXITY_API_KEY`).
- 2026-05-08T18:00Z: `just research-disorder falcon Acute_Megakaryoblastic_Leukemia`
  failed for the same reason (no Edison/Falcon API key, and `agentapi` is not
  available in PATH on the worktree host).

No provider-generated research artifact was available. Curation therefore
proceeded from cached PubMed references already pinned to this disorder, with
no hand-edited `references_cache/*.md` files.

## Evidence Scope Used For Curation

- PMID:8069184 — Phenotypic characteristics of AMKL and TAM (Sato 1994).
  Establishes that AMKL/TAM blasts are immature, MEP-like progenitor cells
  with megakaryocytic differentiation potential.
- PMID:26186939 — The biology of pediatric AMKL (review). Frames pediatric
  AMKL as 4-15% of childhood AML and identifies CBFA2T3-GLIS2 as the most
  frequent chimeric oncogene of non-DS pediatric AMKL.
- PMID:12172547 — Wechsler 2002 (Nat Genet). Establishes near-universal
  acquired GATA1 mutations in DS-AMKL, with N-terminal premature stop codons
  preserving the GATA1s short isoform.
- PMID:14636651 — Hitzler 2003 (Blood). Documents GATA1 mutations as
  initiating lesions in transient myeloproliferative disorder (TAM/TMD), and
  quantifies TAM incidence (~10% of DS newborns) and ~30% AMKL progression.
- PMID:16166640 — Kuhl 2005 (Mol Cell Biol). IN_VITRO mouse fetal
  megakaryocyte study mechanistically dissecting GATA1 domain function.
  Removed during this revision because the snippet originally cited from this
  paper was background HUMAN_CLINICAL context already evidenced more directly
  by PMID:12172547. Cache file retained because the PMID is still cited here
  in the curation history.
- PMID:15849773 — Hsiao 2005 (Am J Hematol). Defines the t(1;22)(p13;q13)
  RBM15-MKL1 (OTT-MAL) fusion oncogene and its restriction to infant/young
  child AMKL.
- PMID:23153540 — Gruber 2012 (Cancer Cell). Identifies the cryptic
  inv(16)(p13.3q24.3) CBFA2T3-GLIS2 fusion in 27% of pediatric AMKL and shows
  in Drosophila and murine models that the fusion induces BMP signaling and
  enhances hematopoietic self-renewal.
- PMID:28063190 — Masetti 2017 review of molecular profiles in pediatric
  non-DS AMKL. Establishes CBFA2T3-GLIS2 and NUP98-KDM5A as poor-prognosis
  recurrent fusions.
- PMID:27114462 — de Rooij 2016 (Blood). Pediatric AMKL intergroup risk
  stratification on 153 cases: CBFA2T3-GLIS2 16%, RBM15-MKL1 12%, NUP98-KDM5A
  9%, KMT2A-rearranged 9%, monosomy 7 6%; mutually exclusive; NUP98-KDM5A,
  CBFA2T3-GLIS2, KMT2A-rearranged, and monosomy 7 independently predict poor
  outcome.
- PMID:28112737 — de Rooij 2017 (Nat Genet). Defines seven genomic subgroups
  of pediatric non-DS-AMKL by RNA + exome sequencing of 99 patients (75
  pediatric, 24 adult), including the previously unrecognized HOX-rearranged
  (HOXr) subgroup (~14% of cases) with characteristic activating MPL
  mutations and superior clinical outcomes. Quantifies cooperating mutations
  in JAK/STAT (16.9%), cohesin/CTCF (18.1%), RAS pathway (15.7%), and MPL
  pathway, plus the near-universal RB1 deletion in NUP98-KDM5A AMKL.
- PMID:28400376 — Uffmann 2017 (Blood). International ML-DS 2006 trial
  reporting superior outcomes with reduced-intensity chemotherapy in ML-DS,
  exploiting the heightened cytarabine sensitivity conferred by GATA1s and
  trisomy 21.

## Curation Conclusions

The accepted disease model is that AMKL is heterogeneous in origin but
convergent in output: a block of terminal megakaryocyte differentiation with
retained megakaryoblast self-renewal, plus marrow stromal fibrosis driven by
megakaryocyte-derived growth factors. Two clinically distinct contexts
dominate: (1) Down syndrome-associated myeloid leukemia (ML-DS), driven by
GATA1 truncating mutations on a constitutional trisomy 21 background and
preceded by transient abnormal myelopoiesis; and (2) non-DS AMKL, dominated
in infants by the t(1;22) RBM15-MKL1 fusion and in older children by the
recurrent fusion oncogenes CBFA2T3-GLIS2 (most common, very poor prognosis),
NUP98-KDM5A (high relapse risk, near-universal cooperating RB1 loss),
KMT2A rearrangements, and HOX-cluster fusions (HOXr; ~14%, favorable
prognosis with cooperating MPL mutations). Cooperating SNVs/indels in
JAK/STAT, cohesin/CTCF, and RAS pathways further stratify outcome within
fusion subgroups. Treatment is risk-adapted: reduced-intensity
cytarabine-based chemotherapy for ML-DS (5-year OS approaching 90%), full
intensity multi-agent AML induction for non-DS AMKL with allogeneic HSCT in
first remission considered for high-risk fusion subgroups.

The curation reflects this model with structured pathophysiology nodes for
each major fusion oncogene, a node for cooperating mutations, an
accumulation/marrow failure node, structured subtypes with MONDO grounding
where available, and treatment evidence. The originally cited PMID:16166640
IN_VITRO evidence item was removed because its snippet conveyed
HUMAN_CLINICAL background context that is more appropriately and directly
evidenced by PMID:12172547.
