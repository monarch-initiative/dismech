# Claims in the OpenScientist TDAR report that fail verification

Four of the report's numbered findings do not survive checking against their own
sources, and so does the summary sentence that frames the whole report. Each
entry below gives the report's claim in its own words, what was checked, and what
the source actually says.

Source report: [`openscientist-tdar-aop-network.md`](openscientist-tdar-aop-network.md)
(OpenScientist job `7e9ef238-7aae-4374-b936-1d312f62c1d5`). AOP-Wiki figures are
from the `09-15-2026` export unless stated; literature was checked against
PubMed abstracts.

Nothing here impugns the report as a whole. Its network structure (F001) is
correct, its assay mapping and chemical-branch sections have not been checked at
all, and the failures cluster in one place: the claims that carry the causal
weight.

---

## 1. The framing claim — "seven independent evidence streams"

> "The causal linkage from impaired TDAR to increased infection susceptibility is
> supported by **seven independent evidence streams**…"

**Fails.** The streams are not all about the linkage they are offered for. At
least three are about something else:

| Stream | What it actually connects |
|---|---|
| IL-1R1 deficiency → *M. tuberculosis* susceptibility (Bohrer 2018) | the AOP 277 **MIE** → infection, skipping the TDAR node entirely |
| Calcineurin-inhibitor immunosuppression → transplant infection deaths (Cippà 2015) | the AOP 154 **MIE**/stressor → infection, likewise skipping TDAR |
| The 6.4% / 10% *Listeria* figure | **ConA-induced T-cell proliferation**, not TDAR — one Key Event upstream |

A stream that runs from the initiating event to the outcome does not evidence the
terminal edge between them. Removing those leaves the linkage resting on
Luster 1993 and, more loosely, the observation that a TDAR readout can be
embedded inside a host-resistance challenge (Burleson 2008).

---

## 2. F002 — "The AOP 277 scientific review supplies the TDAR → infection quantitative bridge"

**Fails twice.**

*The bridge measures a different assay.* The quantified example preserved in the
review is a 6.4% decrease in **ConA-induced T-cell proliferation** associated
with a 10% increased risk of *Listeria* infection. That is splenocyte
proliferation, not the T-dependent antibody response. AOP-Wiki's own record makes
the same substitution: the only quantitative text in the cluster is KER2928's
`quantitative_understanding` field, 207 characters, and it too describes
Concanavalin A response rather than TDAR.

*And the edge it is offered as evidence for does not exist.* KE984 (AOPs 154,
277) and KE1719 (AOP 315) are both terminal Adverse Outcomes with **zero
downstream Key Event Relationships**. There is no curated TDAR → infection KER
anywhere in AOP-Wiki, so there is no relationship for a quantitative bridge to
support. This is a consequence of the OECD review itself: AOP 277 originally
ended at "increased susceptibility to infection", that outcome was replaced by
the measurable TDAR endpoint, and nothing re-attached the infection outcome
downstream.

---

## 3. F003 — "TDAR is among the most predictive immune assays for altered host resistance"

**Fails.** The claim rests on a phrase from
[PMID:8365588](https://pubmed.ncbi.nlm.nih.gov/8365588/) (Luster 1993) —
*"enumeration of lymphocyte populations and quantitation of the T-dependent
antibody response were particularly beneficial"* — read as being about host
resistance. Three things contradict that reading, all in the abstracts
themselves.

**The same abstract says the opposite about host resistance.** Conclusion (2):

> "No single immune test could be identified which was fully predictive for
> altered host resistance, although most assays were relatively good indicators
> (i.e., > 70%)."

**The quoted phrase is about a different endpoint, and points elsewhere.** It
describes predicting **immunotoxicants**, and the 1993 abstract cites the 1992
companion paper for it by name — *"(Luster et al., Fundam. Appl. Toxicol., 18,
200-210, 1992)"*. Following that citation to
[PMID:1534777](https://pubmed.ncbi.nlm.nih.gov/1534777/):

> "The tests that showed the highest association with immunotoxicity were the
> splenic antibody plaque forming cell response (78%) and cell surface marker
> analysis (83%)."

The splenic antibody plaque-forming cell response *is* the TDAR assay. At 78% it
is **outscored by cell surface marker analysis at 83%**, so TDAR ranks second of
the two tests named — and the 78% measures detection of immunotoxic compounds,
not susceptibility to infection.

**In 1992 the host-resistance question was explicitly still open:**

> "Efforts are currently underway using this database to determine the
> relationships between these immune tests and susceptibility to challenge with
> infectious agents or transplantable tumor cells."

That work became the 1993 paper, whose conclusion (2) declines to name any single
test. So the chain of attribution closes without establishing the claim at any
point along it.

**What does hold, and is worth keeping:** the 1993 abstract's conclusion (3) —
*"The ability to resist infectious agent challenge is dependent upon the degrees
of immunosuppression and the quantity of infectious agent administered"* — is a
real dose-dependence claim about immunosuppression and host resistance. It simply
names no assay as the measure of "degrees of immunosuppression".

---

## 4. F005 — "A glucocorticoid-receptor branch bridges the network to the infection outcome"

**Undermined.** The bridge is asserted through AOP 14, whose chain is said to
reach AO323 *Increased, Disease susceptibility*. In the export:

- **KE323 has no incoming Key Event Relationship at all.** The pathway's final
  step is not curated as a relationship, so there is nothing there to evidence.
- **KER570** (*Suppression, Immune system → Increased, Viral susceptibility*, AOPs
  84/85), the only curated KER into an immunosuppression-adjacent infection node,
  has **all four evidence blocks empty**.

The shared KE202 hub the report relies on is real, so the branch exists as a
topology. What it does not do is deliver an evidenced route to an infection
outcome.

---

## 5. F010 — "KER weight-of-evidence into TDAR is High/High across all three AOPs"

**Fails.** The report introduces a ratings table as *"Extraction of the AOP-Wiki
Key Event Relationship (KER) weight-of-evidence tables"* and asserts Evidence
**High** / Quantitative Understanding **High** for the terminal KER of all three
AOPs, concluding this gives the convergence node *"exceptional confidence"*.

No such tables are present. In the `09-15-2026` export (character counts measured
after HTML stripping):

| KER | AOP | `weight_of_evidence` | `quantitative_understanding` | tables | rating tokens |
|---|---|---|---|---|---|
| KER1510 | 154 | **0 chars** | **0 chars** | none | none |
| KER2928 | 277 | 1,506 chars | 207 chars | none | none |
| KER2027 | 315 | 260 chars | 292 chars | none | none |

`has_any_tables` is `false` on all three, and no `High` / `Moderate` / `Low` token
appears anywhere in any of the three records. Nor on the parent AOPs, whose
`woe_evidence` is narrative prose: AOP 277 and AOP 315 contain no rating token,
and **AOP 154 contains only *Moderate*, never High**.

KER1510 is the sharpest case. AOP 154 is the OECD-endorsed pathway of the three
(`WPHA/WNT Endorsed`), and its terminal KER carries no evidence text whatsoever.
AOP 315, by contrast, is still `Under Development`.

**Caveat, stated deliberately:** this establishes that the ratings are not
extractable from the XML export by the method the report states. They may exist
in a structured field the export does not carry, or be visible on the rendered
AOP-Wiki KER pages. That check remains undone.

---

## Reproducing the AOP-Wiki figures

See the *Reproducing it* section of [`../TDAR_AOP.md`](../TDAR_AOP.md) for the
CLI pin, the command that materializes a dated snapshot, and the filter applied
to the resulting cache.
