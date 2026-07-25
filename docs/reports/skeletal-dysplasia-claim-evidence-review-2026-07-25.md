# Skeletal dysplasia claim–evidence review (2026-07-25)

Correctness review of ten skeletal dysplasia entries, focused on whether each curated
claim is actually supported by the evidence attached to it.

## Scope and method

Entries reviewed (chosen to span the mechanistic classes: FGFR3 gain of function,
type II/X collagenopathy, sulfate transport, osteoclast protease, mineralization,
transcription factor):

| Entry | Gene | Mechanism class |
|---|---|---|
| Achondroplasia | FGFR3 | RTK gain of function |
| Thanatophoric Dysplasia Type 1 | FGFR3 | RTK gain of function (severe allele) |
| Kniest Dysplasia | COL2A1 | Type II collagenopathy / ER stress |
| Spondyloepiphyseal Dysplasia Congenita | COL2A1 | Type II collagenopathy / ER stress |
| Metaphyseal Chondrodysplasia, Schmid Type | COL10A1 | Type X collagenopathy / UPR |
| Diastrophic Dysplasia | SLC26A2 | Sulfate transport / PG undersulfation |
| Campomelic Dysplasia | SOX9 | Transcription factor haploinsufficiency |
| Cleidocranial Dysplasia | RUNX2 | Transcription factor haploinsufficiency |
| Pycnodysostosis | CTSK | Osteoclast protease deficiency |
| Hypophosphatasia | ALPL | Mineralization / enzyme deficiency |

Checks run:

1. `linkml-term-validator validate-data … --labels` over all ten — **all 10 pass**;
   every HP/GO/CL/CHEBI/MAXO/NCIT/HGNC id and label is correct.
2. `linkml-reference-validator validate data …` over all ten — **all 10 pass**;
   every `snippet:` is an exact substring of its cached reference.
3. Reference-cache existence check over all ~800 evidence items — **no missing cache
   files**, so no fabricated PMID/DOI/ORPHA/CGGV identifiers.
4. Manual claim-vs-evidence reading of every pathophysiology node, causal edge,
   prevalence record, inheritance block, and quantitative assertion.

Because (1)–(3) are clean, **every finding below is semantic**: the quote is real and
the term is real, but the claim attached to it goes beyond what the quote says. These
are exactly the failures the mechanical validators cannot catch.

## Findings

### 1. Unsourced iPSC/UPR claim propagated across two entries — **highest priority**

Both `Kniest_Dysplasia.yaml:184` and `Spondyloepiphyseal_Dysplasia_Congenita.yaml:169`
assert:

> "recent iPSC-derived human cartilage models show that some COL2A1 mutations cause ER
> procollagen storage without engaging canonical UPR" (Kniest)
>
> "human iPSC-derived cartilage models suggest that ER retention can occur without
> robust canonical UPR activation, consistent with an ER procollagen storage disorder
> rather than a classical UPR-driven apoptosis pathway" (SEDC)

**No reference cited in either file mentions iPSC-derived cartilage.** (Verified by
grepping every cached reference in both entries for `iPSC`/`induced pluripotent`:
zero hits.) The claim materially qualifies the entries' central mechanism — it is the
sole basis for hedging the ER-stress/UPR-apoptosis model — so it should not stand
unsourced. Either attach the primary source or remove the hedge.

### 2. Explanations over-claiming beyond truncated snippets (Hypophosphatasia)

Four evidence items quote a fragment and then assert something the fragment does not
say. All four pass substring validation.

| Location | Snippet | Explanation claims | Problem |
|---|---|---|---|
| `Failure to thrive in infancy` | `"CLINICAL CHARACTERISTICS: Hypophosphatasia is characterized by defective"` | "describes infantile HPP as presenting with rickets-like features and metabolic complications that lead to failure to thrive" | The quoted text (and the sentence it truncates) says none of this. |
| `Hypotonia` | `"children, clinical features include skeletal, respiratory and neurologic"` | "Review identifies neurologic features **including hypotonia**" | Source says "neurologic complications"; hypotonia is never named. |
| `Narrow chest` | `"most severe perinatal and infantile forms, results in 50-100% mortality,"` | "thoracic hypomineralization causing respiratory compromise, consistent with narrow chest as a key morphological driver" | Source sentence is about mortality; it says nothing about the thorax. |
| `Bowing of the long bones` | `"of TNAP and potent inhibitor of mineralization. Thus, HPP features rickets or"` | "Rickets and osteomalacia … underlie the bowing deformities of long bones" | Inference, not evidence; the quote never mentions bowing. |

A fifth is a near-miss worth fixing while in the file: the `Hypercalcemia` snippet
`"vitamin B6-dependent seizures, hypercalcemia with"` truncates one word short of
`"hypercalcemia with high morbidity, and mortality"` — the explanation's "high
morbidity" claim *is* in the source but was cut out of the quote.

### 3. Prevalence record internally contradicts its own class (Hypophosphatasia)

`Hypophosphatasia.yaml:65-70`, adult forms:

```yaml
prevalence_class: ABOVE_1_IN_1000
rate_low: 32.258065        # = 1 in 3,100
rate_high: 196.850394      # = 1 in 508
```

`ABOVE_1_IN_1000` means >100 per 100,000, but `rate_low` is 32.3 per 100,000. The
source range straddles the class boundary, so a single class cannot be correct for it.
The arithmetic is right; the class assignment is not.

### 4. Mechanism generalized from a different disease entity (Campomelic Dysplasia)

The pathophysiology node `Reduced SOX9 Stability and Matrix Defects`
(`Campomelic_Dysplasia.yaml:119-157`) rests entirely on PMID:39854231, and asserts five
downstream CD-specific radiographic features (bell-shaped thorax, 11 rib pairs,
hypoplastic scapulae, cervical spine instability, scoliosis).

That paper studied a congenital-vertebral-malformation cohort and explicitly reports a
TAM-domain variant "associated with **mild skeletal dysplasia and scoliosis**" — it
positions these patients as a *distinct, milder* point on the SOX9 spectrum, not as
campomelic dysplasia. The protein-stability mechanism may well generalize, but no
CD-specific evidence is offered, and the node reads as though it were established in CD.

Also in this entry: the first evidence item of `SOX9-Mediated Chondrogenesis Disruption`
(line 95-104) quotes a generic background sentence ("SOX9 is a crucial transcriptional
regulator of cartilage development and homeostasis") and tags it `HUMAN_CLINICAL`; it
is background prose, not clinical data.

### 5. A superseded mechanism presented as current (Schmid MCDS)

`Metaphyseal_Chondrodysplasia_Schmid_Type.yaml:310` carries a `Functional
Haploinsufficiency` node stating haploinsufficiency "is considered a proximate cause of
the clinical phenotype", cited to a 2005 review (PMID:15880705).

The same entry's own evidence undercuts it: PMID:17403716's snippet reads "**Unlike
Col10a1 null mutants**, transgenic mice (FCdel) … displayed typical characteristics of
MCDS" — i.e. haploinsufficient/null animals do *not* phenocopy MCDS, which is the
classic argument against the haploinsufficiency model. The rest of the entry (ER stress
sufficiency, PERK/ATF4/Sox9, carbamazepine and PERK-inhibitor rescue) correctly models
gain of function.

This is a case the schema already handles: the two competing models should be
`mechanistic_hypotheses` groups (as `Achondroplasia.yaml` does for FGFR3 constitutive
vs. ligand-dependent activation), not two co-equal nodes.

### 6. Frequency evidence attached to causal-link claims (Cleidocranial Dysplasia)

The `RUNX2 Haploinsufficiency` node carries eight `downstream` edges (lines 118-214),
each with `causal_link_type: UNKNOWN` and evidence consisting solely of an Orphanet
frequency row, e.g.:

```yaml
- target: Carious Teeth
  causal_link_type: UNKNOWN
  evidence:
  - reference: ORPHA:1452
    snippet: "HP:0000670 | Carious teeth | Very frequent (99-80%)"
    explanation: Orphanet records carious teeth as very frequent in CCD.
```

A frequency row supports the *phenotype* and its *frequency band*; it says nothing
about a causal edge from RUNX2 haploinsufficiency. All eight are duplicated verbatim in
the `phenotypes:` block, where the same evidence is entirely appropriate. The edges
should either get mechanistic evidence or be dropped.

Also: `penetrance: COMPLETE` (line 46) has no supporting evidence — the cited snippet
establishes autosomal dominant inheritance only. (The same unsupported-`penetrance`
pattern appears at `Thanatophoric_Dysplasia_Type_1.yaml:35`, where the cited snippet
describes mutation counts and does not address penetrance or heterozygosity.)

### 7. Non-endochondral phenotypes parented to endochondral-ossification nodes

- `Diastrophic_Dysplasia.yaml:~316-355`: `Impaired Endochondral Ossification` fans out
  to ~21 targets including **Cleft Palate, Bifid Uvula, Absent Uvula, and
  Tracheobronchomalacia**. Palatal-shelf fusion failure and airway (non-endochondral)
  cartilage softening derive from the general proteoglycan-undersulfation matrix defect,
  not from failed endochondral bone formation. Nineteen of these edges are
  `INDIRECT_UNKNOWN_INTERMEDIATES` with no edge-level evidence.
- `Spondyloepiphyseal_Dysplasia_Congenita.yaml:~262-275`: `Impaired Growth Plate
  Organization` → **Cleft Palate** and **Flat Face**, same issue.

Re-parenting these to the upstream matrix-defect node would be more accurate and costs
nothing structurally.

### 8. Quantitative claims in `notes`/`description` with no supporting quote

| Entry | Claim | Status |
|---|---|---|
| Schmid MCDS `:54` | "estimated incidence of approximately 3-6 per million" | **Not present in any of the entry's cited references.** The two evidence items support only "rare" and "most common subtype". The record is `prevalence_class: UNKNOWN`, so the figure also contradicts its own structured field. |
| Schmid MCDS `:526` | "Adult height is typically more than 3.5 standard deviations below the mean" | Unsupported. The nearest datum in the entry (PMID:41454937) is a −3.62 height Z-score for the *missense subgroup at first presentation* (vs −1.99 for truncating), not adult height for all patients. |
| Diastrophic `:52,:82` | Finnish incidence "~1:22,000" | Unsupported; the cited snippet says only that incidence "has significantly decreased". |
| Pycnodysostosis `:27,:64,:874` | "37% from Europe and 31% from Asia"; "70% mature domain, 24% proregion, 6% preregion" | **Correct** — all figures verified present in cited PMID:21569238. Nit only: not captured in any `snippet:`, so a reader cannot trace them. |

### 9. Mechanistic assertions in prose without evidence items

- `Pycnodysostosis.yaml:10-11,129-131`: "osteoclasts … can acidify the resorption lacuna
  normally but cannot degrade the demineralized organic matrix" — the defining
  distinction from osteopetrosis, and the node's only evidence is "cathepsin K is a
  major protease in bone resorption". This is a well-established fact that deserves its
  own citation.
- `Hypophosphatasia`: `Craniosynostosis` downstream edge (`:325`) has no evidence,
  though a supporting quote is already used elsewhere in the file.

### 10. Population transfer between related diseases (SEDC)

- Prevalence 3.4/million is quoted for "spondyloepiphysal dysplasia (SED)" — congenita
  *and* tarda combined — then recorded as the SEDC rate. The `notes` field discloses
  this honestly, which is good practice; flagging only so the limitation stays visible.
  The `explanation` calls PMID:31523532 "this review"; it is a case report.
- `Vitreous Collagen Abnormality` (`:290`) states myopia ≈45% / retinal detachment ≈12%
  "of SEDC patients". Those figures are correctly evidenced elsewhere in the file
  (PMID:25604898) but come from a mixed 93-patient COL2A1 cohort, and the node itself
  carries no citation for them.

## Verified-good patterns worth preserving

Several entries handle exactly these hazards well and are worth citing as models:

- **Achondroplasia** is the strongest entry reviewed. It uses `mechanistic_hypotheses`
  to avoid asserting strict constitutive FGFR3 activation, explicitly annotates
  vosoritide/navepegritide as accelerated approvals on a surrogate endpoint, and flags
  the 5.75 cm height gain as an *external-control* (not randomized) comparison. It also
  reconciles a conflict openly: an older paper's ">90% sporadic" is quoted, with the
  explanation stating the structured `de_novo_rate` is calibrated to the current ~80%.
- **Thanatophoric Dysplasia Type 1** marks the TD2-equivalent mouse (PMID:9887329) as
  `supports: PARTIAL` and says why in the explanation.
- **Cleidocranial Dysplasia** declines to assign a `frequency` to short stature because
  two cohorts disagree (71% vs 28.6%), and shows both — the correct response to
  conflicting frequency evidence.
- **Kniest Dysplasia** and **Pycnodysostosis** transparently disclose grounding
  compromises (e.g. acroosteolysis mapped to the HPO hand-specific osteolysis term).
- **Achondroplasia** correctly does *not* declare `conforms_to` the module's
  "Constitutive FGFR Activation" node, consistent with its own hedged receptor model,
  while TD1 does — the conformance edges track the biology.

## Gaps noted (not errors)

- **Hypophosphatasia**: bisphosphonates are contraindicated (they are pyrophosphate
  analogues and worsen the mechanism); this safety-relevant fact is not curated.
- **Pycnodysostosis**: growth hormone therapy is not curated as a treatment even though
  PMID:11474477 — already cited eleven times in the entry — is titled "…linear growth
  after growth hormone therapy".
- **Cleidocranial Dysplasia**: wide pubic symphysis / symphysis diastasis appears inside
  a quoted snippet but is not curated as a phenotype.
- **Achondroplasia**: 30 evidence items cite a bare GeneReviews/FDA `url:`, which the
  reference validator cannot check against a cached abstract. Defensible where the
  quote is from chapter body text unavailable in the PubMed record, but it does mean a
  meaningful share of this entry's evidence is outside the automated safety net.

## Suggested priority

1. Finding 1 (unsourced iPSC claim, 2 entries) — remove or cite.
2. Finding 2 (four over-claiming explanations, Hypophosphatasia) — re-quote or re-word.
3. Findings 3, 8 (prevalence class contradiction; unsupported figures) — mechanical fixes.
4. Findings 4, 5 (Campomelic mechanism transfer; MCDS superseded mechanism) — need a
   curator decision on framing, likely via `mechanistic_hypotheses`.
5. Findings 6, 7 (edge evidence and edge parenting) — structural cleanup.
