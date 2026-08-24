---
provider: claude
model: claude-opus-4-8
harness: dismech curation-scanner literature sweep (targeted PubMed + web cross-check)
cached: false
generated: '2026-07-13T00:00:00Z'
template_variables:
  disease_name: Neuronal Intranuclear Inclusion Disease
  mondo_id: MONDO:0011327
  category: Mendelian
  gene: NOTCH2NLC (hgnc:53924)
  inheritance: autosomal dominant (repeat expansion)
verification:
  searches_run: 2
  sources_fetched: 4
  primary_papers_found: 4
  primary_papers_cited_before: 4
  new_primary_papers_added: 0
note: >
  Provenance artifact generated to satisfy the new-entry research requirement
  for PR #6120 (issue #6112), which the code review flagged as the sole open
  blocker. This is a targeted literature-completeness sweep produced by the
  automated high-effort curation scanner — NOT a full fan-out adversarial
  deep-research-provider run. Its purpose is to (1) document the provenance of
  the four primary papers already cited in the entry and confirm they are the
  correct landmark references for the NOTCH2NLC discovery and clinical
  spectrum, and (2) map the established downstream (polyglycine / uN2CpolyG)
  mechanism and emerging therapeutics as leads for the next curation pass.
  The four discovery/spectrum papers (PMID:31332381, PMID:31178126,
  PMID:31332380, PMID:42428984) were fetched and every snippet used in the KB
  entry was verified as an exact substring of the cached abstract. The
  downstream-mechanism and therapeutic references in the "Gaps / follow-up"
  section below were surfaced by web search and are NOT yet fetched or
  snippet-verified — they are LEADS ONLY. Do not import any claim from this
  file into the KB YAML without re-verifying the snippet against the cited
  primary source via `just fetch-reference` + `just validate-references`. The
  authoritative, snippet-validated evidence lives in
  kb/disorders/Neuronal_Intranuclear_Inclusion_Disease.yaml.
---

# Neuronal Intranuclear Inclusion Disease (NIID) — Literature Sweep

**Disease:** Neuronal intranuclear inclusion disease (NIID / NIID-related
disorders, NIIDRD)
**MONDO:** MONDO:0011327 &nbsp;|&nbsp; **OMIM:** 603472 &nbsp;|&nbsp;
**Gene:** NOTCH2NLC (hgnc:53924; MIM 618025) &nbsp;|&nbsp;
**Lesion:** expanded GGC trinucleotide repeat in the 5′ region / 5′UTR &nbsp;|&nbsp;
**Inheritance:** autosomal dominant (repeat-expansion, mostly sporadic on ascertainment)

## Executive Summary

NIID is a slowly progressive, clinically heterogeneous multisystem
neurodegenerative disease defined pathologically by eosinophilic, ubiquitin- and
p62-positive hyaline **intranuclear inclusions** in central, peripheral, and
autonomic neurons and in visceral/somatic (including dermal) cells. In 2019 three
independent groups identified an expanded **GGC repeat in the 5′ region of the
human-specific gene NOTCH2NLC** as the genetic cause, using long-read genome
sequencing to resolve a repeat that short-read exome sequencing had missed. The
same expansion underlies a broader "NIID-related disorder" (NIIDRD) spectrum that
can present as dementia, parkinsonism, leukoencephalopathy, or peripheral
neuropathy, and expansions were even found in a minority of families ascertained
as Alzheimer disease or parkinsonism.

The molecular lesion behaves as a **toxic gain of function**. The expanded GGC
repeat is not appreciably methylated and does not silence NOTCH2NLC; instead the
repeat RNA and, most importantly, **repeat-associated translation of an upstream
open reading frame into a polyglycine protein (uN2CpolyG / N2NLCpolyG)** drive the
formation of the p62-positive intranuclear inclusions and downstream neuronal
toxicity. Diagnosis has shifted from post-mortem brain examination to an
ante-mortem triad — **skin biopsy** (dermal intranuclear inclusions), the
characteristic **symmetrical corticomedullary-junction DWI hyperintensity**, and
confirmatory **NOTCH2NLC GGC-repeat molecular testing** (the most sensitive test,
since only ~37% of confirmed cases show the typical MRI features). There is no
disease-modifying therapy; management is supportive.

## Primary evidence base (verified — cached and snippet-checked)

1. **Sone et al., 2019 — Nat Genet (PMID:31332381).** Long-read (nanopore)
   sequencing identified the GGC repeat expansion in the 5′ region of NOTCH2NLC
   in all affected members of NIID families; cosegregation supports autosomal
   dominant transmission. Frames the ascertained population as predominantly
   sporadic with mean onset ~59.7 y across ~140 cases. *Used in the KB entry for
   the driver lesion, inheritance, and prevalence claims.*

2. **Tian et al., 2019 — Am J Hum Genet (PMID:31178126).** Independent
   identification of the expanded GGC repeat in a five-generation Chinese Han NIID
   family; defines the NIIDRD spectrum (dementia/parkinsonism/AD overlap),
   documents the ubiquitin/p62/SUMO1/FUS/MYO6/OPTN immunoprofile of the
   inclusions, the DWI corticomedullary-junction sign, subgroup leukoencephalopathy
   frequencies (~all dementia-dominant, ~40% limb-weakness-dominant), the
   three-subgroup onset classification, and the unmethylated/normal-expression
   status favoring an RNA/RAN-translation mechanism. *This full-text paper is the
   richest single source and underpins most phenotype, diagnosis, and mechanism
   claims in the KB entry.*

3. **Ishiura et al., 2019 — Nat Genet (PMID:31332380).** Reported noncoding
   CGG/GGC repeat expansions in NBPF19 (NOTCH2NLC) as causative for NIID,
   oculopharyngodistal myopathy, and an overlapping disease — independent
   confirmation and an early pointer to the shared polyglycine-disease family.
   *Used for the genetic causation claim.*

4. **Xia et al., 2026 — Case Rep Neurol Med (PMID:42428984).** The case report
   that seeded issue #6112: multisystem clinical summary, diagnosis via skin
   biopsy + genetic testing. *Used for the clinical-manifestation and
   supportive-care claims.* (Weak stand-alone evidence — a single case report —
   but consistent with and subordinate to the discovery literature above.)

## Clinical spectrum (from PMID:31178126, Table 1 and text)

- **Cognitive:** dementia (dementia-dominant subgroup; the most prominent symptom
  in sporadic cases), abnormal behavior.
- **Movement:** parkinsonism (tremor, rigidity, bradykinesia), cerebellar ataxia.
- **Peripheral/motor:** muscle weakness (limb-weakness-dominant subgroup, distal
  onset), sensory disturbance; nerve-conduction slowing (MCV/SCV).
- **Autonomic:** bladder dysfunction (~56%), miosis (~17%).
- **Paroxysmal:** disturbance of consciousness, stroke-like and encephalitic
  episodes (episodic encephalopathy — a frequent source of misdiagnosis).
- **Neuroimaging:** severe FLAIR/T2 leukoencephalopathy and DWI corticomedullary
  U-fiber high signal (present in only ~37% of confirmed familial cases → MRI is
  specific but not sensitive).

## Established downstream mechanism (LEADS — verify before KB import)

The 2019 discovery abstracts proposed, but did not establish, the toxic mechanism.
Subsequent work (surfaced by web search; **not yet fetched/snippet-verified**)
converges on a **polyglycine proteinopathy**:

- Repeat-associated translation of an **upstream ORF** produces a toxic
  **polyglycine protein (uN2CpolyG / N2NLCpolyG)** that accumulates in
  **p62-positive intranuclear inclusions** in patient tissue, cultured cells, and
  mouse models. → *"GGC repeat expansions within new open reading frames are
  translated into toxic polyglycine proteins…" (Nat Genet, nature.com/articles/s41588-026-02507-z);
  "Neuronal intranuclear inclusion disease: Polyglycine protein is the culprit"
  (PMC10773977).*
- polyG triggers **nucleolar stress** via nucleocytoplasmic translocation of
  **nucleophosmin (NPM1)**, disrupting DNA-damage repair and 3D genome
  architecture. → *"Upstream open reading frame with NOTCH2NLC GGC expansion
  generates polyglycine aggregates and disrupts nucleocytoplasmic transport."*
- A GGC-expansion **mouse model** reproduces behavioral deficits and
  neurodegeneration. → *Science Advances, science.org/doi/10.1126/sciadv.add6391.*
- **Mitochondrial dysfunction** in a Drosophila model. → *PNAS,
  pnas.org/doi/10.1073/pnas.2208649119.*

This is a strong candidate to deepen the entry's `pathophysiology` chain: insert a
distinct **"uN2CpolyG polyglycine translation"** node between the repeat-expansion
driver and the inclusion-formation node, and add an **NPM1 nucleolar-stress /
nucleocytoplasmic-transport** node downstream — each with its own fetched,
snippet-verified primary reference. Note the model-organism evidence should carry
`evidence_source: MODEL_ORGANISM` and should not be the sole support for human
phenotypes.

## Emerging therapeutics (LEADS — verify before KB import)

- **Antisense oligonucleotide (ASO)** therapy rescuing GGC-expansion-induced
  genomic damage / 3D chromatin abnormalities / senescence. → *Nat Commun,
  nature.com/articles/s41467-026-71516-7.* (Would map to the
  `antisense_oligonucleotide_therapy` module if/when a human-relevant, verifiable
  source supports it.)
- **CRISPR/Cas9 precise excision** of the expanded GGC repeat. → *Nat Commun,
  nature.com/articles/s41467-026-68385-5.*

Both are preclinical; keep them out of the KB `treatments:` block until there is a
snippet-verifiable human-relevant source, or curate them explicitly as
`evidence_source: IN_VITRO` / `MODEL_ORGANISM` experimental strategies.

## Gaps / open questions for the next curation pass

1. **polyG mechanism nodes** — add the uN2CpolyG translation and NPM1/nucleolar
   stress steps (see above) with verified primary citations; the current entry
   correctly conforms to `loss_of_proteostasis` but stops at "inclusion
   formation."
2. **Human-model-mismatch caveat** — NOTCH2NLC is human-specific, so mouse/fly
   models cannot fully recapitulate the human gene context; consider a
   `HUMAN_MODEL_MISMATCH` discussion entry rather than a generic knowledge gap.
3. **Trinucleotide-repeat-disorder / polyglycine-disease grouping** — NIID,
   oculopharyngodistal myopathy (already in the KB), and other polyG diseases
   share the uORF-polyglycine mechanism and could motivate a `kb/groupings/`
   union keyed on `CONFORMS_TO_MODULE` + shared mechanism.
4. **Genotype–phenotype** — repeat size correlates loosely with subgroup
   (parkinsonism 66–102; dementia 91–268; muscle-weakness 118–517) but not
   cleanly with severity/onset; worth a structured note if a verifiable source
   is quoted.

## Method / provenance

Two targeted searches were run (PubMed-style discovery-paper confirmation, and a
web search for the downstream polyglycine mechanism and emerging therapy). The
four discovery/spectrum papers were fetched into `references_cache/` and every
snippet quoted in the KB entry was confirmed as an exact substring of the cached
abstract. This sweep documents research provenance only; it is deliberately
conservative about the post-2019 mechanism/therapy literature, marking it as
unverified leads rather than importing it. Treat every citation here as a lead to
re-verify, per the dismech deep-research SOP.
