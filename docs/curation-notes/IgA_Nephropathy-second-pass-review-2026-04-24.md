# IgA Nephropathy Second-Pass Review

Date: 2026-04-14

## Scope

Second-pass review of the existing `IgA_Nephropathy` disorder entry with explicit
lump/split assessment against IgA vasculitis.

## Initial audit of the pre-existing entry

Before revision, the live YAML had several issues relative to the requested bar:

- The pathograph had only three nodes and no explicit `downstream` edges.
- The entry did not represent the IgA vasculitis boundary anywhere in disease content.
- The MONDO anchor was present in `disease_term` but not mirrored in `mappings`.
- The genetics section was too thin and included a likely misleading claim that the
  `CFHR1/CFHR3` deletion is a risk factor; current literature instead treats the
  common deletion as protective in IgAN.
- Evidence typing was inconsistent with study type; many mechanistic statements were
  supported only by reviews but were not explicitly treated that way in the overall
  framing.

## MONDO / Monarch cross-check

Repo-local OAK check plus current external MONDO/Monarch-facing resources were aligned on
the key disease identifiers:

- `MONDO:0005342` has label `IgA glomerulonephritis` with exact synonyms including
  `IgA nephropathy` and `Berger's disease`.
- `MONDO:0019167` has label `immunoglobulin A vasculitis` with exact synonyms including
  `IgA vasculitis` and `Henoch-Schonlein purpura`.

Implication for curation:

- The current ontology does not collapse IgAN into IgA vasculitis or vice versa.
- A subtype fold-in of IgA vasculitis under IgA nephropathy would work against the
  existing MONDO split and against common clinical naming.

Useful links:

- MONDO IgA glomerulonephritis:
  https://bioportal.bioontology.org/ontologies/MONDO/?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMONDO_0005342
- MONDO immunoglobulin A vasculitis:
  https://bioportal.bioontology.org/ontologies/MONDO/?p=classes&conceptid=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMONDO_0019167

## KDIGO / CureGN / literature consistency check

Three external framing sources were especially important:

1. KDIGO 2025 IgAN/IgAV guideline
   - KDIGO publishes a combined guideline for `IgAN/IgAV`, which acknowledges
     deep mechanistic overlap.
   - At the same time, KDIGO's evaluation chapter for IgAN still instructs
     curators/clinicians to consider secondary causes including `IgA vasculitis`.
   - This supports a "jointly discussed but not ontologically collapsed" view.

2. CureGN
   - CureGN operationalizes IgAN and IgA vasculitis nephritis together in the same
     research program but still names them as distinct study diseases/populations.
   - This is consistent with a shared-mechanism, separate-diagnosis approach.

3. Pillebout review (`PMID:40069065`)
   - This review states that IgA vasculitis can be considered a systemic form of IgAN,
     that the two diseases share the four-hit model, and that kidney biopsy can be
     indistinguishable.
   - The same abstract also states that chronic lesions are more frequent in IgAN,
     proliferative lesions are more frequent in IgAVN, and the characteristic rash of
     IgAVN drives earlier diagnosis.
   - That combination argues against treating IgA vasculitis as a mere subtype of
     IgAN inside a kidney-focused disorder file.

Useful links:

- KDIGO guideline PDF:
  https://kdigo.org/wp-content/uploads/2024/08/KDIGO-2025-IgAN-IgAV-Guideline.pdf
- CureGN about page:
  https://www.curegn.org/about
- CureGN study summary:
  https://www.curegn.org/studies/study-participation

## ClinGen cross-check

ClinGen was checked specifically to avoid drifting into false monogenic framing.

Findings:

- No dedicated ClinGen gene-disease validity curation surfaced for IgA nephropathy
  or immunoglobulin A vasculitis as primary monogenic disease entities.
- The disease does appear in genetics literature and in pathway-oriented discussion,
  but the ClinGen landscape did not justify `CAUSATIVE` framing for any single gene
  in this disorder entry.

Implication for curation:

- Keep pathway mediators like `TNFSF13` and `TNFSF13B` on mechanism nodes.
- Keep the `genetic` section limited to susceptibility/protective loci and explicitly
  polygenic language.
- Do not narrate IgAN as a monogenic disease.

ClinGen search entrypoint:

- https://search.clinicalgenome.org/kb/gene-validity

## Lump / split decision

Decision: keep **related-but-separate**, not subtype structure, and do not introduce a
paired root in this PR.

Reasoning:

- `IgA vasculitis` is a systemic small-vessel vasculitis in MONDO, not a child of
  `IgA glomerulonephritis`.
- The kidney lesion is strongly overlapping and often histologically indistinguishable,
  but the systemic phenotype boundary matters clinically and ontologically.
- A subtype representation would wrongly imply that IgA vasculitis is just a renal
  subtype of IgAN.
- A new paired-root umbrella strategy might be defensible in a future broader curation
  effort, but it would require introducing a new umbrella disease concept and matching
  ontology strategy. That is out of scope for a second-pass fix of the existing IgAN file.

Practical encoding in the YAML:

- The main disease remains anchored to `MONDO:0005342`.
- `IgA vasculitis` is represented in `differential_diagnoses` with `MONDO:0019167`.
- The top-level notes make the split explicit.

## Mechanism curation choices

The revised pathograph was rebuilt around a seven-step kidney mechanism chain:

1. Mucosal immune dysregulation and BAFF/APRIL-driven B-cell activation
2. Galactose-deficient IgA1 overproduction
3. Anti-Gd-IgA1 autoantibody formation and immune complex assembly
4. Mesangial immune complex deposition and complement activation
5. Mesangial proliferation and inflammatory amplification
6. Podocyte damage and filtration barrier failure
7. Chronic complement-linked progression and kidney failure risk

To make the graph fully connected and browser/demo-safe without inventing shortcut
biology:

- the renal phenotypes were hung off the kidney injury chain rather than left as
  isolated symptom cards
- the treatment nodes were linked to explicit target phenotypes or mechanisms
- the MHC, glycosylation, and complement-locus susceptibility nodes were aligned
  to matching mechanism steps
- the old standalone `environmental` node was dropped because the current graph
  extractor cannot represent an upstream exposure cleanly without creating an
  orphaned node
- the protective complement signal was encoded as a `CFH`-anchored protective
  locus with notes about the `CFHR1-CFHR3` deletion-tagging haplotype, which is
  more honest than treating the deletion itself as a standalone gene node

This avoids:

- dangling nodes
- direct "IgA deposits -> ESRD" shortcuts
- monogenic overstatement
- dishonest evidence-source tagging

## Key references used for the second pass

- `PMID:38362118` BAFF/APRIL and mucosal hyper-responsiveness
- `PMID:39095059` Gd-IgA1 glycosylation and immune complexes
- `PMID:22904352` anti-Gd-IgA1 autoantibodies in human disease
- `PMID:39188719` mesangial proliferation, podocyte damage, and progression framing
- `PMID:38053977` complement pathway framing
- `PMID:38182298` mesangial C3 deposition and alternative/lectin pathway context
- `PMID:35781866` C3 deposition and severity/progression
- `PMID:39003309` complement-pathic prognosis subset
- `PMID:38438966` biopsy-level IgA deposits / hypercellularity / C3 deposits
- `PMID:40069065` IgAN vs IgAV split boundary
- `PMID:21399633` polygenic susceptibility architecture
