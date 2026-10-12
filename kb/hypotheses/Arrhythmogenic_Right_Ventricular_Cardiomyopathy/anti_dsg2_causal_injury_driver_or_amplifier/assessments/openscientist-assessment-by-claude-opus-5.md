# Assessment — OpenScientist, anti-DSG2 as causal injury driver or amplifier in ARVC

**Assessor:** claude-opus-5 · **Assessed:** 2026-10-12 · **Verdict:** WEAKLY_SUPPORTED_UNRESOLVED

The YAML sidecar beside this file is authoritative. This narrative explains how the
checks were run and what they turned up, for a reader deciding whether to act on the
report. A second assessment of the same report by `codex` already exists; this one was
written independently and overlaps it only where both reach the same conclusion.

## What held up

The report's directional conclusion survives checking. Anti-DSG2 antibodies occur in
clinically defined ARVC, are not specific to it against myocarditis or dilated
cardiomyopathy, and no published study supplies the perturbation experiments a causal
claim would need. Its operative recommendation — keep the hypothesis emerging, wire no
causal edge, claim no ARVC-specific biomarker, propose no immune-directed therapy — is
the right call on this evidence.

Two things were checked that an assessment could easily skip, and both came back clean.

**Citation integrity.** All eighteen cited identifiers resolve, and every title matches
what the report attributes to it. Thirteen were already in `references_cache`; five were
fetched. The five 2026 identifiers are the ones worth checking hardest, because a
well-formed recent PMID is the easiest thing for a literature-only run to invent, and
none was invented.

**Negative-existence claims.** The report asserts, with a search date, that no passive
transfer study, no Fc or complement dissection, no anti-DSG2 monoclonal study, and no
independent epitope reproduction exists. These are the assertions no validator can
reach, so each was re-run. All held. The DSG2 Fc-and-complement search returns eight
records, every one of them an adenovirus-receptor study — DSG2 is an adenovirus
serotype receptor — with no cardiac autoantibody content. The passive-transfer search
returns one pemphigus review. The monoclonal search returns nothing.

## What needs narrowing

**The strongest pro-hypothesis row cannot be verified here.** PMID:42233375 has no
PubMed abstract. Its cached record is 1,876 bytes of citation metadata and author
affiliations. The AUC of 0.823, the OD > 0.774 cut-off, and the hazard ratio of 4.56 —
the figures the comparator reconciliation and the whole prognostic argument rest on —
are nowhere in this repository. The report disclosed the missing abstract, which is to
its credit, but the consequence is larger than the disclosure suggests: those numbers
would fail exact-quote validation if promoted today. The paper is real and sits in PMC,
so this is a verification gap, not a fabrication concern.

**The assay-artifact argument runs backwards.** The report treats two groups' failure to
detect anti-DSG2 binding as a sign the signal may be artifactual, and places that
concern "upstream of all causal interpretation". But PMID:37450050 explains its own
non-detection differently: the authors propose that the antibodies modify the epitope
structure, which would interfere with detection by ELISA or Western blot. On their
reading the non-detection is what catalytic activity predicts, which is compatible with
pathogenicity rather than evidence against it. The unresolved cross-laboratory
disagreement is real and the recommended ring trial is still the right remedy; what does
not follow is that the disagreement points toward artifact.

**DSG2 binding has been independently reproduced.** The report says the
antigen-specificity premise has no independent reproduction. That is true of the mapped
epitope. It is too strong for binding itself, because the report's own PMID:42219531
reports pathogenic autoantibodies bound to DSG2 in hiPSC-derived cardiomyocytes and
reduced DSG2 interaction by atomic force microscopy — from the same group whose earlier
non-detection the report cites as grounds for doubt. That is the most informative
available update on this exact question, and the report does not use it here.

## The paper the report missed

Re-running the report's own search terms recovers PMID:36977772, a prospective 46-dog
study across five groups published in March 2023, three years before the report's search
date. No evidence row cites it. It found anti-DSG2 antibodies in every dog, no
difference between groups, and concluded they were not disease specific — by Western
blot, the original study's own modality, and with non-ARVC cardiac comparators that
neither Boxer cohort the report relies on included.

It cuts both ways, which is why it matters.

It **strengthens** the non-specificity conclusion: canine non-replication is a
three-study finding reaching back to 2023, not a 2025 development, and the earliest
study had the best comparator design for the specificity question. The report's "now
fails to replicate" misdates the record, and the codex assessment's careful
within-modality argument was available three years earlier than that assessment locates
it.

It **weakens** the dysfunction-not-arrhythmia asymmetry. The same study reports a strong
correlation with ventricular arrhythmia complexity among affected Boxers, echoing the
PVC-burden correlation in the 2018 discovery study. Two independent reports of an
arrhythmia-severity correlation among affected subjects sit awkwardly beside an argument
built on the absence of an arrhythmic association. The two are reconcilable — a
within-affected severity gradient and a between-group association answer different
questions, and neither canine correlation is severity-adjusted — but the asymmetry is
softer than the report presents and should not help rank the biomarker-only null against
the amplifier model.

## Do not copy the ontology block

Every CURIE offered resolves, but four of the eight pair a real identifier with the wrong
label or the wrong concept. Labels below were read from the committed term caches, not
recalled.

| Offered as | Actually is | Use instead |
|---|---|---|
| `GO:0005922` as fascia adherens | connexin complex | not the fascia adherens |
| `GO:0038061` as NIK/NF-κB signaling | non-canonical NF-kappaB signal transduction | `GO:0007249` or `GO:0043123` for the canonical pathway the cited papers describe |
| `GO:0072559` as a process | NLRP3 inflammasome complex, a cellular component | `GO:0044546`, NLRP3 inflammasome complex assembly |
| `CL:0000746` labelled cardiomyocyte | cardiac muscle cell | keep "cardiomyocyte" in `preferred_term` |

`GO:0014704`, `GO:0005921`, `GO:0098609` and `GO:0006956` carry their canonical labels
correctly. The two concept errors are the dangerous ones: the NF-κB substitution would
bind the non-canonical branch to pan-inflammatory canonical NF-κB biology, and a label
copied from the ontology would make it self-consistent and silent.

## Artifacts and auditability

Frontmatter declares two rendered artifacts under `openscientist_artifacts/`. Neither the
directory nor either file is committed, so both links in the report are dead and nothing
the run rendered can be inspected. There is no canonical `MANIFEST.yaml`, so the
hypothesis-analysis-run gate does not apply and was not run. For a literature-only run
this costs little scientifically — the Markdown is self-contained and the claims trace to
PMIDs — but the declared provenance overstates what is auditable.

The run claims no computation, so its single analysis is recorded `REPORTED_ONLY` and
`UNVERIFIABLE`. That reflects the run as designed, not a failure.

## Reference-cache changes made for this assessment

Six references were fetched with `just fetch-reference` so the claims above could be
checked offline by the next reader: PMID:34345905, PMID:39786454, PMID:34993452,
PMID:42193878, PMID:39786662, and PMID:36977772. Nothing in `references_cache` was
hand-edited. These remain review context; promoting any of them to a disease entry still
requires normal evidence validation.
