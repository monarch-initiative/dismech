# OpenScientist TDAR report: what each finding implies for dismech

A checklist over the report's twelve finding sections, plus its limitations and
proposed follow-ups. For each: what it claims, whether it has been checked, and
what — if anything — it implies as work in this repository.

**Most of these are not dismech work.** Several findings are about the state of
the AOP framework rather than about this knowledge base, and the honest entry for
them is "nothing to do here". They are marked **AOP-only** and listed anyway, so
nobody re-derives them looking for an action that was never there.

Source report: [`openscientist-tdar-aop-network.md`](openscientist-tdar-aop-network.md).
Verification detail: [`failed-claims.md`](failed-claims.md) and the verification
record in [`../TDAR_AOP.md`](../TDAR_AOP.md).

Legend — **Checked** ✅ verified · ❌ fails verification · ◐ partly checked · ○ unchecked

---

## Findings with dismech actions

### F009 — Mechanistic and clinical evidence close the infection end ◐

Prompted the reframing from TDAR to *impaired antibody response*, which is where
the good evidence turned out to be.

- [x] Record the quantitative human dose-response (Orange 2010, `PMID:20675197`)
      in the project page — done in #11857
- [ ] **Add the missing downstream edge** on `germinal_center_reaction`, from
      *Durable Protective Humoral Immunity* to an infection outcome, carrying
      Orange 2010 — **issue #11907**, open and unclaimed
- [ ] Verify Bohrer 2018 (`PMID:30068597`) and Cippà 2015 (`PMID:26430088`)
      against their abstracts; so far they have only been assessed for *what they
      bear on*, not checked as sources

### F001 — Three AOP-Wiki pathways converge on impaired TDAR ✅

The convergence is real and it is what made the module comparison possible. Its
dismech consequence was the conformer audit.

- [x] Audit which antibody-deficiency entries conform to
      `germinal_center_reaction` — **issue #11897**, closed
- [x] XLA and Hyper-IgM 2 now declare conformance; Selective IgA Deficiency
      deliberately does not; module description updated to name both

### F006, F013 — The 2026 PAC study anchors the network with in vivo TDAR data ○

The one finding with a clear curation payload that nobody has looked at. If the
benzo[a]pyrene result holds, it is an environmental-exposure mechanism with a
quantified endpoint.

- [ ] Check the claims against `PMID:40115130` — ~75% TDAR suppression at
      9 mg/kg/day, and "33 times more sensitive than changes in liver weight"
- [ ] Decide whether a PAC immunotoxicity entry or an `environmental[]` block with
      `influences_mechanisms` is warranted anywhere in `kb/`
- [ ] Note that dismech currently holds **no** drug- or chemical-induced
      immunosuppression disease entries, so this would be a first

### F012, F014 — An AhR branch integrates the PAC chemical class ○

- [ ] Check the four supporting papers (North 2009, Zhang 2010, Yuan 2021,
      Chen 2013)
- [ ] If it holds, this is the natural content for the *iatrogenic B-cell
      depletion / chemical immunosuppression* module that
      `germinal_center_reaction`'s notes already reserve as out of scope and
      "to be argued as its own module"

### F004 — Every Key Event has a defined measurement assay ○

- [ ] Check the assay table against the KE records' `measurement_method` fields
- [ ] If it holds, assess whether any of those assays should ground
      `ExperimentalReadout` entries — noting that OBI is not in
      `conf/oak_config.yaml` and has no enum cache, so assay terms cannot be
      validated today

---

## Findings that are AOP-only

Real observations, useful to the AOP community, with **no dismech action**.

### F002 — The AOP 277 review supplies the TDAR → infection bridge ❌ · AOP-only

The bridge measures ConA proliferation rather than TDAR, and the edge it supports
does not exist as a KER. Interesting to whoever maintains AOP 277; implies
nothing for `kb/`.

### F005 — A glucocorticoid-receptor branch bridges to the infection outcome ❌ · AOP-only

KE323 has no incoming relationship at all and KER570's four evidence blocks are
empty. A gap in AOP 14, not in dismech.

### F010 — KER weight-of-evidence into TDAR is High/High ❌ · AOP-only

No ratings tables, no rating tokens in any of the three KERs or their parent AOPs;
AOP 154 carries only *Moderate*. Worth reporting upstream, since the report's
stated extraction method cannot have produced the figures. Nothing follows for
this repository.

- [ ] *(optional)* Check whether the ratings exist outside the XML export — in a
      field the export does not carry, or on the rendered KER pages

### F003 — TDAR is among the most predictive assays for altered host resistance ❌ · AOP-only

The claim mis-traces its own citation chain. Matters to anyone citing Luster for
TDAR's predictive value; changes nothing in `kb/`.

### F007 — Convergent literature validates TDAR as a first-line assay ○ · AOP-only

- [ ] Check Burleson 2008, Descotes 2006, White 1994 — but note that even if all
      three hold, they concern assay selection in immunotoxicology testing, which
      dismech does not model

### F008 — A 2024 mapping independently confirms the four-AOP network ○ · AOP-only

- [ ] Check the *Front. Toxicol.* 2024 claim, since it is the report's only
      external corroboration. Its stated gap — that none of the immunosuppression
      AOPs covers innate immunity, cell-mediated immunity, or direct B-cell
      effects — is an AOP-side observation

### F011 — The network contextualizes test guidelines and enables NAM 3R refinement ○ · AOP-only

ICH S8, EPA OCSPP 870.7800, OECD TG 443. dismech does not model regulatory test
guidelines, so this is context rather than content.

---

## The report's own limitations and proposed work

Five limitations and six proposed follow-up experiments, none assessed.

- [ ] Review the five limitations — at least two are already independently
      confirmed by this project's own checking (that the TDAR → infection KER is
      anchored by a single historical dataset, and that the AhR branch is not a
      curated AOP)
- [ ] Review the six proposed experiments. All six are proposals for the **AOP
      and NAM community** — formalize an AhR AOP, add innate/cell-mediated Key
      Events, re-derive the quantitative KER, prototype a NAM battery, run a
      benchmark-dose concordance, validate hub Key Events. None is dismech work,
      and the checklist entry is to confirm that reading rather than to act on
      them

---

## Summary

| Category | Count |
|---|---|
| Findings with dismech actions | 5 (F001, F004, F006/F013, F009, F012/F014) |
| AOP-only findings | 7 (F002, F003, F005, F007, F008, F010, F011) |
| Verified ✅ | 1 · **Failed ❌** 4 · Partly ◐ 1 · Unchecked ○ 6 |
| Open dismech issues arising | 1 (#11907) |
| Closed | 1 (#11897) |

The asymmetry is the point. The report was commissioned to establish a causal
linkage, and the linkage is the part that failed; what it produced of durable
value to dismech was a module conformance audit and one well-evidenced edge that
nobody had drawn.
