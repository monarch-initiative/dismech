# Chronic Pain Disorders — Claim–Evidence Review (2026-07-25)

Correctness review of 10 chronic-pain entries in `kb/disorders/`, focused on
**claim–evidence matching**: does each quoted snippet actually support the claim
it is attached to, and is the `supports` / `evidence_source` classification right?

## Entries reviewed

`Fibromyalgia`, `Migraine`, `Chronic_Pancreatitis`, `Endometriosis`,
`Irritable_Bowel_Syndrome`, `Osteoarthritis`, `erythromelalgia`,
`Ankylosing_Spondylitis`, `Rheumatoid_Arthritis`, `Gout` — 482 evidence items total.

## Mechanical validation: clean

Both automated gates pass on all 10 files, so every issue below is **semantic**, not
something CI would catch.

| Check | Result |
|---|---|
| Snippet-in-source (`linkml-reference-validator` semantics, replicated against `references_cache/`) | **482/482 pass** — every snippet is a verbatim substring of its cached source |
| `linkml-term-validator validate-data --labels` | **10/10 pass** — all ontology IDs/labels correct |

The anti-hallucination stack is doing its job. What it cannot see is whether a
*real, correctly quoted* sentence is *about the claim it is filed under*. That is
where all the defects are. (The `Total checks: 0` line the reference validator prints
is not evidence of a gap — see Method below.)

## A. Confirmed defects (wrong, not merely thin)

### A1. `Rheumatoid_Arthritis`: JIA is declared a subtype of RA, and the entry's own evidence says it isn't

`has_subtypes[2]` is `JIA`. All four attached evidence items fail to support it, and
two explanations state the opposite outright:

- `PMID:35087087` `PARTIAL` — "*However, JIA is not a subtype of Rheumatoid Arthritis…*"
- `PMID:23763801` `NO_EVIDENCE` — "*…does not explicitly define it as a subtype of Rheumatoid…*"
- `PMID:37700346` `PARTIAL` — "*…does not support that JIA [is a subtype]*"
- `PMID:8465574` `NO_EVIDENCE` — snippet is about **late-onset RA after age 60**, entirely unrelated to JIA

Independent confirmation: MONDO does not place JIA (`MONDO:0011429`) under
rheumatoid arthritis — its ancestors reach `MONDO:0005554` *rheumatic disorder*, not
`MONDO:0008383`. JIA also already has its own entry, `kb/disorders/Juvenile_Idiopathic_Arthritis.yaml`.

**Fix:** remove the `JIA` subtype; if a relationship is wanted, model it as a
differential/related disease, not a subtype. Note the subtype `name` is a foreign-key
target — check for `subtype: JIA` references before removing.

### A2. `Endometriosis`: `supports: NO_EVIDENCE` on evidence that fully supports its claim

`pathophysiology[4]` *Immune Dysfunction*, `PMID:16166933`, is marked `NO_EVIDENCE`, yet
the snippet is a direct, complete statement of the node's claim:

> "Increased number and activation of peritoneal macrophages, decreased T cell and natural killer (NK) cell cytotoxicities are the alterations in cellular immunity and result in inadequate removal of ectopic endometrial cells from the peritoneal cavity."

and its own explanation reads "*Immune cell dysfunction leads to impaired clearance of ectopic endometrial cells*". Should be `SUPPORT`.

### A3. `Endometriosis`: `supports: SUPPORT` on evidence the explanation says does not support

`phenotypes[3]` *Infertility*, `PMID:16166933`, is marked `SUPPORT` while its explanation
says "*Snippet supports inflammatory lesion growth mechanisms but **does not directly support infertility***". The snippet is about cytokine-driven implantation and angiogenesis. Should be
`PARTIAL`/`NO_EVIDENCE`, or replaced with an infertility source.

### A4. `Chronic_Pancreatitis`: pancreatic-**cancer** paper cited for acinar injury, self-contradictory support value

`pathophysiology[0]` *Recurrent Acinar Cell Injury*, `PMID:23622130`
("A starring role for stellate cells in the pancreatic cancer microenvironment"),
`supports: NO_EVIDENCE`, snippet:

> "Pancreatic ductal adenocarcinoma is a devastating disease, and patient outcomes have not improved in decades."

The snippet is about PDAC prognosis — nothing about acinar cells, trypsin activation, or
chronic pancreatitis — yet the explanation claims it "supports the inflammatory injury cascade."
The same PDAC paper carries the *Pancreatic Fibrosis* node (`PARTIAL`), where the snippet is
explicitly about "pancreatic **cancer** development" while the explanation asserts it describes
stellate-cell fibrosis "in chronic pancreatitis."

**Fix:** drop the `NO_EVIDENCE` item; replace the fibrosis citation with a chronic-pancreatitis
stellate-cell source (Apte et al. and successors).

### A5. `Irritable_Bowel_Syndrome`: prevalence quote used as evidence for microbiome dysbiosis

`pathophysiology[5]` *Microbiome Dysbiosis*, `PMID:37048642`, `supports: SUPPORT`:

> "It has a prevalence of 10 to 25% in the United States and has a high disease burden…"

Epidemiology cannot support a dysbiosis mechanism, and the explanation concedes as much
("*emphasizing the importance of understanding…*"). The **same PMID** is already quoted
correctly elsewhere in the file (line 109) with a sentence that names "gut microbiota
composition" — that snippet belongs here.

### A6. `Migraine`: three causative gene assignments rest on a snippet that names no gene

`CACNA1A`, `ATP1A2`, and `SCN1A` are each `association: Causative` / `supports: SUPPORT`,
all citing the identical `PMID:38508838` sentence:

> "Some distinct, rare, familial migraine subtypes are caused by pathogenic variants in genes involved in ion transport and neurotransmitter release…"

No gene is named. The gene identities come from the curator's explanations, not the source.
The facts are correct, but "causative gene" is the highest-stakes claim class in the KB and
here it is unsourced. `TRPM8` has the mirror problem: its snippet supports *expression* in
pain circuitry, while the `LRP1` entry's snippet is the one that actually names
`rs10166942 (2q37.1, TRPM8)` as a GWAS hit.

### A7. `Migraine`: "central sensitization" node evidenced by *peripheral* sensitization data

`pathophysiology[2]` *Central Sensitization* claims "sensitization of trigeminal nucleus and
thalamic neurons" — i.e. second-order CNS neurons. Both evidence items are `PMID:37487740`,
about **meningeal primary afferent** mechanical sensitization, which is peripheral. The
explanation bridges the gap by calling afferent sensitization "a key component of central
sensitization." The entry has correct central-sensitization evidence available elsewhere
(`PMID:30982963`, cutaneous allodynia → TNC neurons).

### A8. `Migraine`: sleep-disturbance trigger evidenced by a quote that never mentions sleep

`environmental[1]` *Sleep Disturbance*, `PMID:1525797`:

> "One or more precipitating factor was present in 61% with MA and in 90% with MO."

A count of "some trigger exists" is used to support a *specific* trigger.

### A9. `Rheumatoid_Arthritis`: 19 `NO_EVIDENCE` items retained, 9 with explanations that argue *for* the claim

This is a systematic pattern, not isolated. Examples where the snippet is about the wrong
analyte or wrong disease while the explanation asserts support:

| Claim | Ref | Snippet is about | Explanation says |
|---|---|---|---|
| ESR elevated | `PMID:19788068` | homocysteine, ADA, MDA — ESR not mentioned | "ESR … is elevated" |
| CRP elevated | `PMID:29256110` | serum **substance P** | "markers like CRP would typically be elevated" |
| Symmetric polyarthritis | `PMID:11358413` | HLA-DRB1 shared epitope | "thus supporting the statement" |
| Fatigue | `PMID:26803313` | fatigue in *all* chronic inflammatory disease | "supports … in rheumatoid arthritis" |
| RF positive | `PMID:37475055` | RF-positive **JIA** | "supports the presence of RF" |
| Morning stiffness | `PMID:24461540` | **polymyalgia rheumatica** | "…which includes RA" |

Two Morning Stiffness items (`PMID:30936222`, `PMID:25437284`) have **empty snippets**
(`snippet: ''`). These render as evidence rows on the disorder page.

**Fix:** delete `NO_EVIDENCE` items whose snippet is off-topic; where a paper genuinely
doesn't support the claim, that belongs in `notes`, not an evidence block.

### A10. `Ankylosing_Spondylitis`: an entire pathophysiology node evidenced by a five-word fragment

`pathophysiology[6]` *TNF-Mediated Inflammation* — a node asserting TNF's pivotal recruiting
role and the rationale for TNF inhibitors — is supported by:

> "IL-22, and tumor necrosis factor α (TNF-α)."

A mid-sentence list fragment with no subject, verb, or disease context. Two neighbours are
similar: *Mechanical Stress at Entheses* cites "genetic predisposition, environmental factors
(infections and mechanical stress), or innate and acquired immune mechanisms." for a node
claiming microtrauma, cartilage-peptide release and neovascularization; the *IL-23/IL-17 Axis*
node's first item is an abbreviation-expansion list ("PsA, Psoriasis, Psoriatic Arthritis; AS,
Ankylosing Spondylitis; …").

### A11. `Ankylosing_Spondylitis`: duplicate uveitis phenotypes with conflicting frequencies

`Uveitis` (`FREQUENT`, notes "25-40%", evidence "pooled prevalence … 25.8%") and
`Anterior uveitis` (`FREQUENT`, evidence "occurs in up to 50% of the patients") are two
entries for the same manifestation carrying incompatible numbers. Both also appear as
separate `downstream` targets of the TNF node. Collapse to one.

### A12. `Rheumatoid_Arthritis`: a duplicated interstitial-lung phenotype

`Interstitial pneumonitis` duplicates the existing `Interstitial Lung Disease` phenotype —
same manifestation, two entries, both sourced from `PMID:33609792`.

*(Correction to the first draft of this review: `Myocardial infarction` vs `Accelerated
Atherosclerosis` and `Pleuritis` vs `Pleural Effusion` were also called duplicates here. On
closer reading they are distinct entities — an event versus the process producing it, and
serosal inflammation versus its fluid consequence — and have been kept. Only the interstitial
pair was a true duplicate.)*

### A13. `Osteoarthritis`: guideline snippet truncated past the clause that carries its polarity

`treatments` *Duloxetine*, `PMID:31908149`:

> "topical capsaicin for knee OA, acetaminophen, duloxetine, and tramadol."

The governing clause in the ACR guideline abstract is "**Conditional recommendations were
made for** …". As quoted, the snippet cannot distinguish a recommendation from a
recommendation *against*. Every other treatment in this file quotes the "Strong
recommendations were made for…" clause in full. Extend the snippet.
(Same file: this item is `evidence_source: OTHER` while the other five items from the same
guideline are `HUMAN_CLINICAL`.)

## B. Evidence-source misclassification (animal/in-vitro data typed as human)

`evidence_source` is absent on **339 of 482** items (70%), so they default to
`HUMAN_CLINICAL`. Mostly harmless for review articles, but it is actively wrong where the
snippet is explicitly non-human — and CLAUDE.md requires model-organism evidence to stay
distinguishable:

| File | Ref | Snippet | Should be |
|---|---|---|---|
| `Migraine` | `PMID:37495957` (×3, incl. `Headache` phenotype) | "In both WT and FHM1 mutant **mice**, CSDs induced headache-related behaviour…" | `MODEL_ORGANISM` |
| `Migraine` | `PMID:39080518` | "Studies in **rodents** have demonstrated…" | `MODEL_ORGANISM` |
| `Irritable_Bowel_Syndrome` | `PMID:17241857` (×3) | "…excite **rat** nociceptive visceral sensory nerves"; "Ca²⁺ in dorsal root ganglia neurons" | `IN_VITRO`/`MODEL_ORGANISM` |
| `Fibromyalgia` | `PMID:21684692` (×2, incl. `Chronic Widespread Pain` phenotype) | "**GAD65 knockout mice** … supraspinal hyperalgesia" | `MODEL_ORGANISM` |

`Migraine` is internally inconsistent about this: the *same* `PMID:37495957` Panx1 snippet is
correctly tagged `MODEL_ORGANISM` on the CSD→Trigeminovascular `downstream` edge but untagged
on the parent node.

Conversely, `Osteoarthritis` `PMID:40621694` tags a general conclusion sentence
`MODEL_ORGANISM` while the sibling item from the same human single-cell abstract is
`HUMAN_CLINICAL`.

## C. Ontology bindings that undersell the claim

Term validation passes (the labels are correct), but three bindings are needlessly coarse
and a better HPO term exists:

| File | Phenotype | Current | Better |
|---|---|---|---|
| `Migraine` | Visual Aura (notes: "Scintillating scotoma, fortification spectra") | `HP:0000505` Visual impairment | `HP:0010822` **Scintillating scotoma** |
| `Endometriosis` | Painful Bowel Movements (`preferred_term: Dyschezia`) | `HP:0002027` Abdominal pain | `HP:6000222` **Painful defecation** |
| `Fibromyalgia` | — | `Glutamate` biochemical `context: Insula levels on MRS` cites a GAD conceptual-model paper that reports no MRS data | cite an insula-MRS study (e.g. Harris et al.) or drop the MRS context |

## D. Uncited claim blocks

### D1. Genetics — 49 of 70 gene entries carry no evidence at all

| File | genes | no evidence | no `gene_term` |
|---|---|---|---|
| `Rheumatoid_Arthritis` | 23 | 18 | 23 |
| `Ankylosing_Spondylitis` | 16 | 13 | 16 |
| `Fibromyalgia` | 9 | 9 | 9 |
| `Endometriosis` | 4 | 4 | 4 |
| `Gout` | 3 | 3 | 0 |
| `Irritable_Bowel_Syndrome` | 2 | 2 | 2 |

**11 genes appear in both RA and AS with byte-identical `notes` strings** (`BACH2`,
`TNFAIP3`, `STAT3`, `IL10`, `CD28`, `EGR2`, `ETS1`, `IRF8`, `SATB1`, `IKZF1`, `PRDM1`), all
`association: GWAS`, none cited in either file — a copied block rather than per-disease curation.

Separately, RA misuses the `association` slot for function rather than gene–disease
relationship: `TNF` → "Central proinflammatory cytokine", `IL6R` → "Mediates IL-6 signaling".
Neither file sets `relationship_type` anywhere.

### D2. Pathophysiology nodes with zero evidence

`Rheumatoid_Arthritis` has five: *NF-κB Activation*, *Neutrophil Extracellular Trap
Formation*, *B Cell and Plasma Cell Responses*, *Mucosal Origins and Dysbiosis*, *Epigenetic
Dysregulation of T Cell Function*. `Endometriosis` has *Adhesion Formation*.

### D3. Frequency bands

Per `docs/frequency-evidence-guidelines.md`, a `frequency:` value is a separate quantitative
claim. Most bands in this set have no supporting quote. Two are contradicted by their own
evidence:

- `Rheumatoid_Arthritis` *Cervical Spine Instability* = `OCCASIONAL` (5–29%), evidence says
  RA "can compromise the cervical spine in **up to 80%** of the cases."
- `Migraine` *Visual Aura* = `OCCASIONAL`, but the file's own evidence gives aura in
  "one-third of patients" with visual aura in "90% of subjects with MA" → `FREQUENT`.

`Fibromyalgia` subtype shares are also mutually inconsistent: `FM-CS` "50–60%", `FM-SFN`
"40–55%", pathophysiology node "approximately 50%", none cited.

### D4. Missing `prevalence` blocks

8 of 10 entries have none (`Osteoarthritis` and `Rheumatoid_Arthritis` are the exceptions) —
including `Migraine` and `Irritable_Bowel_Syndrome`, which already quote the numbers inside
evidence snippets (MA 5% / MO 8% lifetime; IBS 10–25% US) but never record them structurally.

## E. Module-conformance gap

`kb/modules/cellular_senescence.yaml` (line 34) and `CLAUDE.md` both advertise
"Worked conformers: **Osteoarthritis** (senescent chondrocytes; PMID:28436958)", but
`kb/disorders/Osteoarthritis.yaml` has no `conforms_to` on its *Chondrocyte Senescence*
node — its only conformance is to `osteoarthritis_cartilage_degradation`. The documentation
overstates the KB. Either add
`conforms_to: "cellular_senescence#Senescent Cell Accumulation"` or correct the module docs.

`Osteoarthritis` also under-links its module: *Subchondral Bone Remodeling* and the catabolic
chondrocyte state map onto `osteoarthritis_cartilage_degradation` nodes that are left
unconnected.

## Per-entry summary

| Entry | Evidence items | Verdict |
|---|---|---|
| `Gout` | 40 | **Strongest.** Clean causal chain, reference ranges with interpretation bands, computational model. Gaps: *Hyperuricemia* and *Inflammasome Activation* nodes have no snippet naming urate elevation or NLRP3/IL-1β respectively; `Nephrolithiasis` edge and phenotype uncited. |
| `Endometriosis` | 33 | **Strong.** Best pain-mechanism modelling in the set (neuroangiogenesis → peripheral → central sensitization, with a hypothesis group and a negative P2X3 trial cited as a qualifier). Two support-value errors (A2, A3). |
| `erythromelalgia` | 15 | **Clean.** Every item verifiable and appropriately hedged. Marking the 2004 "single common pathogenetic mechanism — microvascular arteriovenous shunting" claim `SUPPORT` is generous given Nav1.7; `PARTIAL` fits better. |
| `Osteoarthritis` | 26 | **Strong.** Only file with `evidence_source` on 100% of items. Issues: A13, E. |
| `Migraine` | 72 | **Good mechanism, weak genetics.** Issues: A6, A7, A8, B, C, D3, D4. |
| `Irritable_Bowel_Syndrome` | 33 | **Good.** Issues: A5, B. Also `geo:GSE36701` is titled "…**rectal** mucosa…" but described and tissue-bound as **jejunum** (`UBERON:0002115`) — the jejunal study is GSE14841. Both microbiome datasets set `organism.preferred_term: human gut metagenome` against `NCBITaxon:9606`, and type 16S amplicon runs as `data_type: WGS`. |
| `Fibromyalgia` | 25 | **Mixed.** *Descending Pain Modulation Dysfunction* claims reduced serotonin/norepinephrine but both citations are about glutamate/GABA; `Serotonin: Decreased` is uncited. Plus B, C, D1, D3. |
| `Chronic_Pancreatitis` | 32 | **Mixed.** A4 is the main defect. Two `biological_processes` (`Extracellular Matrix Organization`, `Digestive System Process`) have no `term:` binding though `GO:0030198`/`GO:0022600` exist. Explanations cite numbers absent from their snippets ("35-62% prevalence", "68.9% osteopenia", "diabetes HR 2.3"). `PRSS1` is `Causative` on a snippet that says "associated with the risk of". |
| `Ankylosing_Spondylitis` | 40 | **Weak sourcing.** A10, A11, D1. `HLA-B27 … Present in 90-95% of patients` is uncited. No prevalence block despite `PMID:32712723` (already cached for RA) giving AS at 0.20–0.25%. |
| `Rheumatoid_Arthritis` | 166 | **Most content, most defects.** A1 (nosology), A9 (19 `NO_EVIDENCE`, 2 empty snippets), A12, D1, D2. Breadth is excellent; evidence hygiene has not kept up with it. |

## Recommended fix order

1. **A1** — remove the JIA subtype from RA (nosologically wrong, self-contradicted, MONDO-contradicted).
2. **A2, A3, A4, A5** — support-value errors and wrong-disease citations; each is a 1–5 line edit.
3. **A9** — sweep RA's 19 `NO_EVIDENCE` items: delete the off-topic ones, move real caveats to `notes`, and fix the two empty snippets.
4. **A6, A7, A8, A13** — re-source or re-quote; all have a correct source already present in the same file or one `just fetch-reference` away.
5. **B** — set `evidence_source: MODEL_ORGANISM` / `IN_VITRO` on the ~10 explicitly non-human snippets.
6. **C, E** — swap the two HPO bindings; resolve the `cellular_senescence` conformance claim.
7. **D** — larger curation projects: cite or drop the uncited gene blocks, add the missing `prevalence` records, audit `frequency` bands.

## Method

- Snippet fidelity was checked by replicating `SupportingTextValidator.normalize_text` and
  `_split_query` from the installed `linkml-reference-validator` against `references_cache/`
  (punctuation-stripping, `...`-splitting, order-independent substring match) to get a
  per-snippet accounting. Note that `linkml-reference-validator validate data` reports
  "Total checks: 0" on a clean file because that counter reports *issues found*, not
  snippets examined — the affirmative signal is the `Snippets checked: N/N verified
  against cached references` line, available standalone via
  `just count-verified-snippets <file>` (see CLAUDE.md, "Reading the reference-validation
  summary", and issue #7252). An earlier draft of this report read the zero as evidence
  that validation was running vacuously; that was wrong, and no validator change is needed.
- Term validation used `scripts/run_term_validator.sh validate-data … --labels`.
- Alternative HPO terms were located with `runoak -i sqlite:obo:hp search`; MONDO placement
  with `runoak -i sqlite:obo:mondo ancestors`.
- Claim–evidence matching was done by reading each entry in full.

## Status: fixes applied

All findings in sections A–C and E were applied in the follow-up commit on this branch, plus
the two contradicted frequency bands and the three prevalence blocks whose numbers were already
present in cached snippets (D3, D4 partial). Section D1/D2 (uncited gene blocks and
evidence-free pathophysiology nodes) remains open — those need per-disease literature curation
rather than an edit.

Subsequent review rounds on PR #7476 corrected three things in the fixes themselves: the
`evidence_source: OTHER` tags on the new prevalence records were retagged `HUMAN_CLINICAL`
(pooled human epidemiology is clinical evidence regardless of publication format); curation
meta-commentary was removed from user-facing `description`/`notes`/`context` fields, which
render on the public disorder pages; and the mechanistic biology this review had deleted from
the Ankylosing_Spondylitis "Mechanical Stress at Entheses" node was restored with a real
supporting citation rather than left excised — a better resolution than removal. Part of D1 is
now closed: the five Migraine gene entries carry HGNC `gene_term` bindings, and the mixed
human/mouse Fibromyalgia snippet was split so each item carries one `evidence_source`.

Post-fix validation: schema 10/10 `No issues found`; term validation 10/10 passed; full
`tests/test_data.py` suite 16,782 passed; every snippet verifying via
`just count-verified-snippets`; reference-cache frontmatter contract OK. Three references were
newly fetched via the project's fetch path (`PMID:15753610`, `PMID:32430436`, `PMID:33547227`);
no cache file was hand-edited.
