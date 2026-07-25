# Neuroimmune Entry Review: Claim–Evidence Correctness Audit

**Date:** 2026-07-25
**Scope:** 10 neuroimmune disorder entries in `kb/disorders/`
**Focus:** correctness of claim↔evidence matches (does the cited snippet actually
support the claim it is attached to?)

## Entries reviewed

| Entry | Lines | Evidence items | Verdict |
|---|---:|---:|---|
| `Multiple_Sclerosis` | 1576 | 156 | **Needs work** — 14 non-supporting items, 1 retired nosology claim |
| `Stiff_Person_Syndrome` | 1599 | 95 | Minor — 1 unsupported + internally inconsistent genetic claim |
| `Guillain_Barre_Syndrome` | 795 | 37 | Minor — 1 materially reversed claim–evidence match |
| `Chronic_Inflammatory_Demyelinating_Polyneuropathy` | 467 | 20 | Minor — 1 meaning-altering truncation, 1 source misclass |
| `Neurosarcoidosis` | 1668 | 67 | Minor — 2 content-free snippets used as SUPPORT; module gap |
| `Neuromyelitis_Optica_Spectrum_Disorder_with_Anti-AQP4_Antibodies` | 978 | 40 | Minor — MOA-as-mechanism, 1 overread sequence claim |
| `Myasthenia_Gravis` | 1234 | 72 | Good — 1 `evidence_source` misclass |
| `Anti-NMDA_Receptor_Encephalitis` | 1316 | 72 | **Good** |
| `Acute_Disseminated_Encephalomyelitis` | 2046 | 111 | **Good** |
| `Rasmussen_Encephalitis` | 390 | 7 | Structurally sound but thin (4/7 pathophysiology nodes uncited) |

## Method

Three passes:

1. **Snippet-substring check** against `references_cache/` (ellipsis-aware,
   Unicode-normalized), replicating what `linkml-reference-validator` does.
2. **Automated semantic checks**: `reference_title` drift vs cached title
   (wrong-PMID detector), `supports:` enum vs explanation wording
   (self-contradiction detector), and snippet species/setting vs
   `evidence_source`.
3. **Manual read** of every `pathophysiology` node and its evidence in all
   10 entries, plus targeted reads of flagged sections.

**Note on tooling:** `linkml-reference-validator` reports `Total checks: 0` in a
network-restricted environment (it fails to fetch full text and silently
performs no snippet checks). Do not treat a passing run in that setting as
evidence that snippets were verified.

## Findings

Ordered most to least severe.

### 1. MS: "Progressive-Relapsing" course is retired nosology with zero supporting evidence

`kb/disorders/Multiple_Sclerosis.yaml` — `progression[3]`
(`phase: Progressive-Relapsing`) carries **five** evidence items, and *all five*
are tagged `supports: NO_EVIDENCE` with explanations that explicitly say the
reference does not address PRMS:

- `PMID:37068931` — "does not mention progressive-relapsing multiple sclerosis (PRMS)"
- `PMID:17884680` — "does not address progressive-relapsing multiple sclerosis (PRMS)"
- `PMID:31397221` — "does not mention progressive-relapsing multiple sclerosis"
- `PMID:11207871` — "does not specifically address progressive-relapsing multiple sclerosis (PRMS)"
- `PMID:24722325` — "does not specifically mention progressive-relapsing multiple sclerosis"

Separately, PRMS was **eliminated** as a clinical course descriptor by the 2013
Lublin revision (Lublin et al., *Neurology* 2014;83:278–286); those patients are
now classified as PPMS with activity. So the entry asserts a category that is
both retired and unsupported by anything it cites.

**Recommendation:** remove the `Progressive-Relapsing` progression phase (and its
five non-evidence items), or retain it only as an explicitly historical
descriptor citing the Lublin revision that retired it.

### 2. GBS: complement evidence cites a study whose headline result is negative

`kb/disorders/Guillain_Barre_Syndrome.yaml:215` — pathophysiology node
**"Complement-Mediated Nerve Damage"**, `PMID:10355667`.

The cited paper is titled *"Anti-ganglioside antibodies can bind peripheral nerve
nodes of Ranvier and activate the complement cascade **without inducing acute
conduction block in vitro**"*. Its conclusion is that the node of Ranvier is
"relatively resistant to acute antiganglioside antibody mediated injury" and that
"this in vitro sciatic nerve model appears of limited use".

The dismech explanation reads: *"…establishing the complement-mediated mechanism
of nerve damage."* The paper establishes complement **fixation** and explicitly
fails to demonstrate nerve **damage** — the explanation inverts the study's
conclusion. `supports: PARTIAL` is the right tag; the explanation is not.

Compounding this: the study is **mouse sciatic nerve, ex vivo**, but
`evidence_source` is unset (defaults to `HUMAN_CLINICAL`). Should be
`MODEL_ORGANISM` or `IN_VITRO`.

**Recommendation:** rewrite the explanation to state what the study actually
shows (antibody binding + complement fixation at nodes of Ranvier, *without*
acute electrophysiological deterioration), and set `evidence_source`.

### 3. MS: 14 `NO_EVIDENCE` items, 5 with explanations that claim the opposite

`Multiple_Sclerosis.yaml` is the only entry of the 10 carrying a large
`NO_EVIDENCE` population (14; SPS has 2, the other eight have none). Five pair
`supports: NO_EVIDENCE` with an explanation asserting support — a direct internal
contradiction:

| Line | Reference | Location | Explanation says |
|---|---|---|---|
| 591 | `PMID:23153835` | phenotypes > Gait and Balance Issues | "This reference **supports** the statement…" |
| 998 | `PMID:22919874` | biochemical > Oligoclonal Bands | "This reference **supports** the detection of oligoclonal bands…" |
| 1448 | `PMID:15575796` | treatments > Symptomatic Treatments | "This reference **supports** the statement…" |
| 1515 | `PMID:10073279` | treatments > Corticosteroids | "…indirectly **supports** the use of other treatments like corticosteroids" |
| 620 | `PMID:10101582` | phenotypes > Muscle Weakness | "…**supporting** the frequency of muscle-related issues" |

`PMID:10073279` is the worst: an **interferon beta** efficacy paper attached to
the **Corticosteroids** treatment, justified as "indirectly supports the use of
other treatments". An interferon paper is not evidence about corticosteroids.

The remaining nine `NO_EVIDENCE` items are honestly labelled (their explanations
correctly say the reference does not support the claim) but add noise without
adding evidence.

**Recommendation:** delete these items rather than re-tagging them. Per
`CLAUDE.md` §"When Evidence Cannot Be Verified", the fix for an unsupportable
claim is to move it to `notes` or drop the evidence block — not to keep a
citation that does not support it.

### 4. Neurosarcoidosis: content-free snippets used as `SUPPORT`

`kb/disorders/Neurosarcoidosis.yaml` — `PMID:30167654` (Neurosarcoidosis
Consortium consensus criteria) is cited seven times. Two of those are quoting
sentences that carry no claim content:

- Pathophysiology **"Nervous System Granulomatous Inflammation"** — snippet:
  *"Diverse disease presentations and lack of specificity of relevant diagnostic
  tests contribute to diagnostic uncertainty."* This is about **diagnostic
  uncertainty**; it says nothing about granulomatous inflammation of neural
  tissue, which is the node's claim.
- Pathophysiology **"Neurologic Dysfunction"** — snippet: *"The work of this
  collaboration included a review of the manifestations of neurosarcoidosis and
  the establishment of an approach to the diagnosis of this disorder."* This is a
  **scope sentence about the paper itself**, not a finding. It cannot support a
  node claiming cranial neuropathy / visual pathway / meningeal / peripheral
  nerve involvement.

Both are tagged `SUPPORT`. The same PMID is used correctly elsewhere in the file
(e.g. the `DIAGNOSTIC_CRITERIA` definition at line 127), so this is snippet
selection, not a wrong PMID.

**Additional gap:** Neurosarcoidosis declares no `conforms_to`, despite
`kb/modules/granuloma_formation.yaml` naming sarcoidosis as a target conformer.
Its pathophysiology (antigen presentation → Th1/Th17 → granulomatous
inflammation) maps directly onto the module chain.

### 5. CIDP: truncation that changes a diagnostic definition

`Chronic_Inflammatory_Demyelinating_Polyneuropathy.yaml:177` — `PMID:38330421`,
phenotypes > Sensory Loss.

Snippet: *"Sensory CIDP was diagnosed when two inclusion criteria are met: 1)
acquired, chronic progressive or relapsing symmetrical or asymmetrical sensory
polyneuropathy that had progressed for >2 months."*

Abstract: *"…progressed for >2 months; **and 2) definite electrophysiological
and/or biopsy evidence of demyelinating neuropathy.**"*

The snippet announces "two inclusion criteria" and then supplies only one,
replacing the semicolon with a period. A reader would take the clinical criterion
as sufficient when the source requires electrophysiological/biopsy confirmation.
This also fails substring validation.

Also at line 111 (`PMID:36645654`, Macrophage-Mediated Myelin Stripping): snippet
truncated at *"…downregulation of macrophage activation."* where the abstract
reads *"…downregulation of macrophage activation **or co-stimulatory and adhesion
molecules**."* Milder, but the truncation makes macrophage downregulation look
like the terminal mechanism — precisely the claim being supported.

At line 74 (`PMID:36346134`): snippet says "cytotoxic effects **in vitro**" but
`evidence_source` is unset → should be `IN_VITRO`.

### 6. NMOSD: drug design intent used as mechanistic evidence

`Neuromyelitis_Optica_Spectrum_Disorder_with_Anti-AQP4_Antibodies.yaml` —
pathophysiology node **"AQP4-Reactive B Cell Autoantibody Production"**:

- `PMID:36933107` snippet: *"which is designed to suppress autoantibody production
  by blocking the interleukin-6 (IL-6) receptor"* — explanation calls this
  *"directly supports autoantibody production as an upstream therapeutic target"*.
  A statement of what a drug **is designed to do** is not evidence that the
  mechanism operates. Reasonable as `PARTIAL` with a hedged explanation; not
  "directly supports".
- `PMID:31495497` snippet is a mid-sentence fragment (*"of inebilizumab, an
  anti-CD19…"*) — a trial-efficacy result used to infer an upstream mechanism.

Separately, node **"Secondary Demyelination and Neuronal Injury"** cites
`DOI:10.4103/nrr.nrr-d-23-01325` with the explanation *"Supports the downstream
**sequence** from astrocytopathy to demyelination and neuronal loss."* The
snippet is an unordered **list** of features that animal models reproduce
("aquaporin-4 loss, astrocytopathy, granulocyte and macrophage infiltration,
complement activation, demyelination, and neuronal loss") — it carries no causal
ordering. The `MODEL_ORGANISM` tagging here is correct.

### 7. SPS: HLA claim unsupported and names the wrong gene

`Stiff_Person_Syndrome.yaml` — `genetic > HLA-DRB1`:

- `notes` claims *"The **DQB1\*0201** allele is present in approximately 70% of
  SPS patients"* — but the entry is keyed to **HLA-DRB1**. DQB1 is a different
  gene (HLA-DQB1). Gene/allele mismatch within one record.
- Its only evidence item (`PMID:35084720`) is tagged `NO_EVIDENCE`, and the
  snippet is about clinical overlap across GAD-spectrum disorders — it mentions
  no HLA allele. The explanation concedes the inference: *"…**implies** common
  genetic susceptibility factors including HLA associations."* Inference, not
  evidence.

**Recommendation:** either cite a real HLA association study for the 70%
DQB1\*0201 figure and re-key the record to `HLA-DQB1`, or move the claim to
`notes` without an evidence block.

### 8. `evidence_source` misclassifications (4 total)

All four are non-human evidence defaulting to `HUMAN_CLINICAL`:

| File | Line | Reference | Snippet setting | Should be |
|---|---|---|---|---|
| `Guillain_Barre_Syndrome` | 215 | `PMID:10355667` | mouse sciatic nerve, "in vitro" | `MODEL_ORGANISM`/`IN_VITRO` |
| `Myasthenia_Gravis` | 256 | `PMID:29266249` | "Studies in animals… EAMG" | `MODEL_ORGANISM` |
| `Multiple_Sclerosis` | 1127 | `PMID:35963325` | "preclinical MS model… (EAE)" | `MODEL_ORGANISM` |
| `Chronic_Inflammatory_Demyelinating_Polyneuropathy` | 74 | `PMID:36346134` | "cytotoxic effects in vitro" | `IN_VITRO` |

Per `CLAUDE.md`, model-organism evidence should not be the sole support for human
phenotype claims — untagged, these read as human clinical evidence. Note the MG
and MS cases are the *only* animal-derived support for their respective nodes'
specific sub-claims.

### 9. Terminal-punctuation truncations (cosmetic, 12 items)

Twelve snippets fail substring validation only because the curator truncated
mid-sentence and appended a period where the source has a comma or semicolon.
Examples: `PMID:32388832` (×2, MS), `PMID:24314688` (also swaps the source's
curly double quotes around *"multiple"* for straight single quotes),
`PMID:32560364`, `PMID:37059571`, `PMID:31971066`, `PMID:32408148`,
`PMID:29452342` (MS); `PMID:37869140` (MG); `PMID:37108447` (GBS);
`PMID:36645654`, `PMID:38330421` (CIDP).

Ten are harmless. Two — `PMID:38330421` and `PMID:36645654`, both CIDP — change
meaning and are written up separately in finding 5.

### 10. Weak-attribution and coverage notes (no action required)

- **MS prevalence, Europe** (`PMID:37059571`): a review of **Chinese and Asian**
  MS epidemiology is cited for a European prevalence of 115/100,000. The figure
  appears in the abstract, but as a comparator for "countries with predominantly
  white populations" — not a European estimate. A primary European
  epidemiological source would be better.
- **MS oligoclonal bands** (`PMID:32408148`): a 6-patient **Baló's concentric
  sclerosis** series used for OCB in MS. Correctly tagged `PARTIAL`.
- **Rasmussen encephalitis**: 4 of 7 pathophysiology nodes (Microglial
  Activation, Cortical Hyperexcitability, Drug-Resistant Focal Seizures,
  Progressive Neurological Decline) carry no evidence at all. Nothing incorrect —
  just thin. The two `conforms_to` declarations against
  `epilepsy_excitation_inhibition_imbalance` are correctly formed.
- **CIDP** declares no `conforms_to` despite
  `peripheral_axonal_degeneration#Distal Axonal Degeneration and Demyelination`
  being an obvious fit.

## What checked out clean

- **No wrong-PMID / named-entity-confusion errors.** Every `reference_title` in
  all 10 entries matches its cached PubMed title. No fabricated PMIDs: the two
  high-numbered 2026 references (`PMID:42093930` anti-GQ1b spectrum review,
  `PMID:41750202` ADEM review) are both real and correctly quoted.
- **`Anti-NMDA_Receptor_Encephalitis`** — the strongest of the ten. Clean
  separation of `IN_VITRO` (Dalmau rat hippocampal culture work) from
  `HUMAN_CLINICAL` (paired CSF/serum), and every snippet is a faithful quote
  carrying the claim it supports.
- **`Acute_Disseminated_Encephalomyelitis`** — 111 evidence items, zero
  substring failures, appropriate `PARTIAL`/`OTHER` tagging, and mechanistic
  nodes correctly framed as *proposed* hypotheses rather than established fact.
- **`Myasthenia_Gravis`, `Neuromyelitis_Optica_…AQP4`, `Neurosarcoidosis`** —
  100% `SUPPORT` with no `NO_EVIDENCE` padding.

## Recommended priority

1. Remove the MS `Progressive-Relapsing` phase (finding 1) — retired nosology,
   zero support.
2. Fix the GBS `PMID:10355667` explanation (finding 2) — currently inverts the
   cited study's conclusion.
3. Delete MS's 14 `NO_EVIDENCE` items (finding 3).
4. Repair the CIDP `PMID:38330421` snippet (finding 5) — restore the second
   inclusion criterion.
5. Replace the two Neurosarcoidosis content-free snippets (finding 4).
6. Set the four `evidence_source` values (finding 8).
7. Resolve the SPS HLA-DRB1 / DQB1\*0201 inconsistency (finding 7).
8. Optional: add `conforms_to` for Neurosarcoidosis → `granuloma_formation` and
   CIDP → `peripheral_axonal_degeneration`.

## Cross-cutting observation

Defects cluster almost entirely in the **older, larger** entries
(`Multiple_Sclerosis`, and to a lesser degree `Stiff_Person_Syndrome`,
`Chronic_Inflammatory_Demyelinating_Polyneuropathy`). The recently curated
entries (`Anti-NMDA_Receptor_Encephalitis`, `Acute_Disseminated_Encephalomyelitis`,
`Neuromyelitis_Optica_Spectrum_Disorder_with_Anti-AQP4_Antibodies`,
`Rasmussen_Encephalitis`) set `evidence_source` consistently, avoid
`NO_EVIDENCE` padding, and quote faithfully. The failure mode being cleaned up is
recognizable: **"cite something adjacent and explain the gap away"** — an
explanation that argues for relevance rather than a snippet that carries the
claim. The `supports:` enum is doing its job (curators tagged these honestly);
the explanations are where the drift lives.
