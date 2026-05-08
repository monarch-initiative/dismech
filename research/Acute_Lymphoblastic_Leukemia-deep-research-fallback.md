# Acute Lymphoblastic Leukemia Deep Research Fallback

## Provider Attempts

- 2026-05-08T13:00Z: `just research-disorder asta Acute_Lymphoblastic_Leukemia`
  failed: `agentapi not found in PATH` and no provider API keys configured
  (OPENAI_API_KEY, EDISON_API_KEY, ASTA_API_KEY, PERPLEXITY_API_KEY all unset
  in this environment).
- 2026-05-08T13:00Z: `just research-disorder openai Acute_Lymphoblastic_Leukemia`
  failed for the same reason.
- 2026-05-08T13:00Z: `just research-disorder perplexity Acute_Lymphoblastic_Leukemia`
  failed for the same reason.
- 2026-05-08T13:00Z: `just research-disorder falcon Acute_Lymphoblastic_Leukemia`
  failed for the same reason.

No provider-generated research artifact was available to integrate. Curation
therefore proceeded from previously fetched PubMed abstracts and full-text
caches in `references_cache/`, without hand-editing any cache files.

## Evidence Scope Used For Curation

- PMID:23523389 (Inaba H, Greaves M, Mullighan CG. Lancet 2013) — comprehensive
  Lancet Seminar review on ALL biology, genetics, treatment, and outcomes.
  Used to anchor:
  - founding-lesion model (genome-wide profiling, recurrent translocations and
    aneuploidy)
  - prenatal/in-utero initiation language for the "Acquisition of Initiating
    Genetic Lesion" pathophysiology node
  - differentiation block (PAX5, IKZF1, EBF1 alterations in >2/3 of B-ALL)
  - bone marrow failure (induction therapy "restores normal haematopoiesis")
  - Ph-like / BCR-ABL1-like ALL subtype definition (10-12% of B-ALL,
    BCR-ABL1-negative, IKZF1-altered, poor outcome)
- PMID:15472075 (Weng AP et al. Science 2004) — the landmark NOTCH1 paper,
  used to anchor activating NOTCH1 mutations as the dominant driver in T-ALL
  (>50% of cases).
- PMID:19129520 (Mullighan CG et al. NEJM 2009) — IKZF1 deletion as an
  independent predictor of poor outcome in B-cell ALL.
- PMID:41251904 (recent Ph+ ALL review) — used to anchor the BCR-ABL1 fusion
  defining the Ph+ ALL subtype.

## Curation Conclusions

The accepted disease model for ALL is a multi-step transformation in which a
founding cytogenetic lesion (translocation creating a chimeric oncogene or
aneuploidy) is acquired in a B- or T-lymphoid progenitor — often in utero in
B-ALL — followed by acquisition of cooperating mutations that:
- corrupt lymphoid transcriptional programs (chimeric TFs; KMT2A-driven HOXA
  upregulation; NOTCH1 in T-ALL)
- block differentiation (IKZF1, PAX5, EBF1 lesions in B-ALL; CDKN2A/B loss
  most prominent in T-ALL)
- drive constitutive proliferation/survival signaling (BCR-ABL1 RAS/PI3K/JAK,
  NOTCH1-MYC, KMT2A-HOXA9/MEIS1)

The clonal lymphoblast population then expands in the marrow and disseminates
to extramedullary sites, producing two dominant clinical axes:
1. Bone marrow failure with pancytopenia (anemia, bleeding from
   thrombocytopenia, infections from neutropenia)
2. Extramedullary disease (lymphadenopathy, hepatosplenomegaly, anterior
   mediastinal mass in T-ALL, CNS infiltration as a sanctuary site).

Risk stratification, treatment choice (TKIs in Ph+ and Ph-like ALL, JAK
inhibitors in CRLF2-rearranged disease, blinatumomab/inotuzumab/CAR-T in
relapsed B-ALL, allogeneic HSCT for highest-risk groups), and prognosis are
governed largely by molecular subtype and MRD response.

## Subtypes

Curated subtypes in the YAML:
- B-ALL with ETV6-RUNX1 (favorable)
- B-ALL with TCF3-PBX1 (intermediate, historical CNS relapse risk)
- B-ALL with KMT2A rearrangement (high-risk; infant-predominant)
- Ph+ ALL (BCR-ABL1) (TKI-targetable)
- Ph-like ALL (BCR-ABL1-like) (high-risk; kinase-rearranged; partly
  TKI/JAK-targetable)
- T-ALL (NOTCH1-driven; mediastinal mass; ETP-ALL subset)

## Items Intentionally Skipped

- icdo_morphology was left as the broad "Leukemia" classification because
  splitting into subtype-specific codes (e.g., 9811/3 B-ALL NOS, 9837/3 T-ALL)
  on a parent disorder would require either duplicating the parent or moving
  the field per subtype. Worth revisiting if ICDO subtyping at the subtype
  level is later added to the schema.
- Each fusion `genetic` entry was given a single canonical `gene_term` (the
  more clinically central partner: ABL1 for BCR-ABL1, RUNX1 for ETV6-RUNX1,
  PBX1 for TCF3-PBX1). The `gene_term` slot is single-valued, so the second
  partner is documented inline in `notes` with its hgnc: ID for traceability.
