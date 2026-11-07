---
name: extract-tg-method
description: >
  Turn an OECD Test Guideline's paragraph index into one record per validated
  test method, with every fact carrying the guideline's own sentence and the
  paragraph it came from. Use when extracting test-method details from a TG
  (442D first), when deciding which paragraph supports which fact, when a
  `just check-tg-extraction` run passes but the record still looks wrong, when
  recording a method the guideline only cites as a comparator, or when carrying
  an extracted method into a disease entry or module. Not for fetching or
  re-indexing the PDF — that is `just extract-oecd-tg`.
---

# Extracting a test method from an OECD Test Guideline

An OECD Test Guideline is the authoritative statement of what a validated test
method measures, and it is unstructured prose. `scripts/extract_oecd_tg.py` has
already turned the PDF into a citable paragraph index; this skill is the layer
above it, which the script deliberately cannot do.

**The contract: every extracted fact carries three things — the value, the
guideline's own sentence, and the paragraph number.** A field holding
`"key_event": 2` is a paraphrase that nothing can check. The same field carrying
its sentence and `442D/IA/1` can be checked by a script and by any reader with
the PDF.

Read [`docs/oecd-tg-extraction.md`](../../../docs/oecd-tg-extraction.md) first
if you have not. It covers the citation-key grammar, the scope decision, and the
two extraction traps (pypdf `layout` mode, per-division paragraph numbering).

## Step 1 — confirm the index covers what you are about to extract

```bash
just check-tg-extraction                    # paragraph count, no records yet
```

The index holds the General Introduction plus, in each appendix, `Initial
Considerations` and `Principle of the Test`. `PROCEDURE`, `DATA AND REPORTING`,
the prediction model and the annexes are **out of scope** and are not in the
index. A fact that lives only in `PROCEDURE` cannot be cited: widen the scope
in the extractor and re-index, or leave the field out. Do not cite a paragraph
you have not read in the index.

## Step 2 — one record per test method, not per appendix

**An appendix is not a method.** TG 442D has four appendices and five methods:
Appendix IC describes **EpiSensA and Epi2SensA together**, and separates them
only in its third paragraph. A record per appendix would fuse two methods that
differ in tissue model and in validation status.

| Appendix | Method(s) |
|---|---|
| IA | KeratinoSens™ |
| IB | LuSens |
| IC | EpiSensA **and** Epi2SensA |
| ID | α-Sens® |

So a paragraph can be shared by two records, and the same sentence can be cited
by both — correctly. What must not be shared is a value the sentence assigns to
one of them.

## Step 3 — the fields

**Biology and materials first. The regulatory skeleton is secondary.** A method's
name tells you nothing; what distinguishes it is the cell or tissue it runs in,
the construct or transcript it reads, and the chemistry it can and cannot see.
Extract that before validation status and performance, and order the record so it
reads as science rather than as paperwork. Validation and performance matter, but
a record with a validation route and no substrate describes a certificate, not an
assay.

**Biology and materials — the substrate:**

| Field | What it holds | Typically found in |
|---|---|---|
| `method_family` | the guideline's own grouping of its methods | GI ¶2 |
| `measurement_basis` | reporter transgene, or endogenous transcript | appendix ¶1, ¶9 |
| `key_event` | which AOP key event it addresses | appendix ¶1 |
| `mechanism` | the biology the readout depends on | appendix ¶1 |
| `initiating_chemistry` | the chemical reaction the method detects | appendix ¶5 |
| `response_arms` | which biological response(s) the readout spans | appendix ¶1 |
| `host_cell_line` | the named line, if the guideline names one | appendix ¶3, ¶8 |
| `tissue_matrix` | 2D culture, or a named 3D model and its interface | appendix ¶3, ¶5 |
| `regulatory_element` | the response element, **and its species** | appendix ¶8 |
| `reporter_construct` | reporter gene(s) and promoter arrangement | appendix ¶8 |
| `internal_viability_control` | a second reporter in the same cells | appendix ¶8 |
| `marker_genes` | the endogenous genes quantified | appendix ¶1, ¶3 |
| `marker_gene_interpretation` | what each gene reports biologically | appendix ¶1 |
| `readout` | the measured quantity and the assay | appendix ¶8, ¶9 |
| `exposure_route` | in the medium, or applied to the tissue surface | appendix ¶4, ¶5 |
| `culture_conditions` | serum, xeno-free, and similar | appendix ¶2 |

**Domain of applicability — what the substrate lets it see:**

| Field | What it holds | Typically found in |
|---|---|---|
| `metabolic_competence` | the system's capacity to activate chemicals | appendix ¶5 |
| `prohapten_detection` | whether pro-/pre-haptens are caught or missed | appendix ¶5 |
| `mechanistic_blind_spot` | chemistry the mechanism cannot register | appendix ¶5 |
| `assay_interference` | artefacts arising from the readout itself | appendix ¶5 |
| `lipophilicity_limit` | the LogP / logKow range that can be tested | appendix ¶3, ¶4 |
| `cytotoxicity_threshold` | the viability floor for a valid call | appendix ¶9 |
| `positive_call` | the decision rule and its cut-offs | appendix ¶9 |

**Regulatory standing — secondary:**

| Field | What it holds | Typically found in |
|---|---|---|
| `validation_route` | validation study, then which peer review | appendix ¶2 |
| `validation_status` | VRM, validated similar method, or PS-based | appendix ¶3, GI ¶3 |
| `reviewing_body` | the named body that peer-reviewed it | appendix ¶2 |
| `regulatory_use` | what the method is valid *for* | appendix ¶2 |
| `performance_vs_<comparator>` | accuracy / sensitivity / specificity | appendix ¶3 |
| `performance_caveat` | the guideline's own limit on those figures | appendix ¶3 |
| `reproducibility_within_laboratory` | within-laboratory, separately | appendix ¶3 |
| `reproducibility_between_laboratory` | between-laboratory, separately | appendix ¶3 |
| `proficiency_substances` | how many a laboratory must demonstrate | appendix ¶10 |

These are the fields TG 442D supports; another guideline will support a different
set, and the vocabulary should grow by reading rather than by anticipation.

**A supplier is not a material fact, but it can index one.** The RhE model a
method uses is part of its identity — EpiSensA and Epi2SensA differ in tissue
model and nothing else biologically — and each model has a sole supplier. Record
the **model**, which is biology; leave licences, material transfer agreements and
reagent sourcing out, which are procurement. In TG 442D those sit in `PROCEDURE`
and the annexes, outside the extracted scope, and there is nowhere in the dismech
or NAMO schema to put them.

Record shape, one object per field:

```json
{
  "methods": [
    {
      "method": "KeratinoSens",
      "guideline": "OECD TG 442D",
      "appendix": "IA",
      "fields": {
        "key_event": {
          "value": 2,
          "quote": "addresses the second key event of the skin sensitisation AOP (1), namely keratinocytes activation",
          "paragraph": "442D/IA/1"
        }
      }
    }
  ]
}
```

## Step 4 — quote from the index, never from memory

Copy the sentence out of the index entry you are citing. Do not retype it, and
do not reconstruct it from the PDF you read earlier: the index is what the
checker compares against, and a quote assembled from recall is the failure this
whole exercise exists to prevent.

```bash
just check-tg-extraction --records data/oecd_tg/tg442d-methods.json
```

The checker rejects a quote that is not a substring of the cited paragraph, and
says where the sentence actually is when it finds it elsewhere. It also rejects
three shapes that would otherwise pass as citations without being any: a bare
value with no quote (`"key_event": 2`), a quote that normalises to nothing
(`"(TM)"`), and a quote below the five-word floor.

Typography does not decide a match. `KeratinoSens`, `KeratinoSens(TM)` and
`KeratinoSens™` all verify; `α-Sens®` folds to `alpha-sens`. A **mid-word gap**
(`con sidered`) does not fold and must not be worked around — it means the index
was built with pypdf's default mode instead of `layout`.

## Step 5 — the judgement the checker cannot make

**A quote can be verbatim, correctly located, and cited for a claim it does not
make.** Nothing in the tooling objects; `test_the_checker_cannot_tell_whether_a_quote_supports_its_value`
pins the limitation so a green run is not mistaken for a correct extraction.
These are the four shapes it takes in this guideline.

**A performance figure without its comparator is a misrepresentation.** TG 442D
paragraph IA/3 reads: "The accuracy (77% - 155/201), sensitivity (78% - 71/91)
and specificity (76% - 84/110) of the KeratinoSens™ test method for
discriminating skin sensitisers (i.e. UN GHS Cat. 1) from non-sensitisers **when
compared to LLNA results**". Those numbers are agreement with a mouse assay, not
accuracy against human outcomes.

So the comparator goes in the **field name**, not in a neighbouring field:
`performance_vs_llna`, `performance_vs_human`. EpiSensA and α-Sens® each carry
both, and they differ sharply — EpiSensA is 67.6% specific against the LLNA and
52.9% against human data. A single `performance` field would have to pick one,
and a separate `performance_comparator` field can be dropped while the number
survives. Extend the quote through the comparator clause, and record the
guideline's own `performance_caveat` beside it; every method here has one.

**A quote must carry its own subject, and a field must not outrun it.** Both
failures got past the checker on the first pass of this guideline. A quote
beginning "is in the order of 85% within and between laboratories" verifies and
names nothing; a `reproducibility` value stating both a within- and a
between-laboratory figure was cited to a sentence giving only one of them.
Quote the whole clause including what it is about, and split a field whose value
needs two sentences — that is why reproducibility is two fields above.

**"Respectively" assigns two values by word order.** Paragraph IC/3: "The RhE
models used are the LabCyte EPI-MODEL24 and the EpiDerm™ model (EPI-200) in the
EpiSensA and the Epi2SensA test methods, respectively." Cited for EpiSensA's
`test_system` the quote is correct and the value must be `LabCyte EPI-MODEL24`.
Swap them and every check still passes.

**Modal strength is part of the claim.** Appendix IA/1 says KeratinoSens™
"addresses" the second key event; IC/1 says EpiSensA and Epi2SensA "are
**proposed** to address" it. Do not normalise the second into the first.

**A gene symbol carries no key event.** IL-8 is one of four marker genes at Key
Event 2 in TG 442D's EpiSensA and Epi2SensA, and it names a luciferase reporter
assay at Key Event 3 in TG 442E. Both are correct and they are not
interchangeable. This is the error that was made while the proposal for this
work was being written — see `docs/oecd-tg-extraction.md` — and it is why the
paragraph travels with the fact.

Then read the record back against the index one field at a time and ask only:
*does this sentence say this value?* That pass is the deliverable. The script
run before it is a precondition.

## Step 6 — a method the guideline only cites

TG 442D names the animal methods it was validated against — GPMT, Buehler
(TG 406), LLNA (TG 429), and TG 442A/442B — without describing them. Extracting
them from TG 442D would build a record out of another guideline's framing.

Record a **stub**: identity, the guideline that defines it, and the guideline
that cites it, under `status: CITED_COMPARATOR`.

```json
{
  "method": "LLNA",
  "guideline": "OECD TG 429",
  "status": "CITED_COMPARATOR",
  "cited_by": "OECD TG 442D",
  "note": "The comparator behind every performance_vs_llna figure here. Not described by TG 442D; needs TG 429.",
  "fields": {
    "phases_assessed": {
      "value": "Induction only",
      "quote": "all assess the induction response exclusively",
      "paragraph": "442D/GI/4"
    }
  }
}
```

A stub **may** carry fields, but only for what the citing guideline states in
its own voice, quoted and cited like any other fact. TG 442D's paragraph GI/4
says the guinea pig tests assess induction and elicitation while the murine ones
assess induction exclusively — a real distinction, verifiable, and worth
keeping. What `status` prevents is reading the record as an extraction of TG 429.

Do not go further than the citing guideline's sentence. A property you know from
elsewhere, or infer because it is a mouse assay, does not belong here. Promote
the stub by extracting its own guideline.

## Step 7 — carrying a method into the KB

An extracted record is not KB content. It becomes content as an
`experimental_models` entry on a disease entry or module, which keeps its own
prose and carries the method's identity so two entries citing one method are
checkably citing the same thing:

- `name`: the method as the guideline writes it, trademark included. The
  trademark can be load-bearing: α-Sens and α-Sens® are two different
  constructs, and `442D/ID/3` is where the guideline says so
- `experimental_model_type`: `CELL_LINE` for KeratinoSens™, LuSens and α-Sens®.
  For the RhE-based EpiSensA and Epi2SensA use `OTHER`, with the tissue model
  named in `description`. **Not `ORGANOID`**, which the enum defines as a
  self-organising culture; a reconstructed human epidermis is keratinocytes
  seeded on a membrane and lifted to an air–liquid interface. `Contact_Dermatitis`
  already files EpiSensA as `OTHER`, so this is also the consistent choice
- `modeled_mechanisms`: the keratinocyte-activation node, with `model_scale`
  — these assays observe `MOLECULAR` or `CELLULAR` state, so a link to a
  tissue- or organism-level node is an upward extrapolation and needs
  `limitations` or a typed `divergences` entry
- `divergences`: prefer a typed entry over prose wherever one fits. A transgenic
  reporter standing in for endogenous pathway activity is `PROXY_QUANTITY`;
  LuSens's rat *NQO1* element in a human cell is `SPECIES_MISMATCH`; the absent
  dendritic-cell and lymph-node compartments are `BOUNDARY_OMISSION`

**Evidence cannot yet come from the guideline.** `just fetch-reference
DOI:10.1787/9789264229822-en` resolves and titles correctly but caches with
`content_type: unavailable`, so there is no body for a snippet to match and an
exact-quote evidence item citing that DOI cannot verify. Until a structured
source exists for the guideline (see `docs/oecd-tg-extraction.md`), cite the
method's **primary literature** — the validation and inter-laboratory papers the
guideline's own reference list names — and keep the extracted record as the
audited statement of what the guideline says.

Do not work around this by quoting another paper's introduction *as though* it
were the guideline. Where a paper does restate a regulatory fact, that is a real
citation and takes `quote_role: BACKGROUND`; what it is not is a substitute for
the guideline on facts no paper states.

Do not copy the extraction JSON into the entry. The record is the audited
source; the entry states what that disease's curator needs from it.

## What this skill does not cover

Re-indexing a PDF (`just extract-oecd-tg`), the manifest's checksum pinning, or
the question of whether extracted methods should eventually become a standalone
`kb/` record type rather than per-entry `experimental_models`. That last one is
open: today the identity is the guideline number plus the method name, carried
on an ordinary inline record, which is reuse by identity rather than by entity.

Tracked in [#16338](https://github.com/monarch-initiative/dismech/issues/16338).
