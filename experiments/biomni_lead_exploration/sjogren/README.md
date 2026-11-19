# Sjögren's syndrome: mechanism-led drug candidates

Started from Biomni Target Atlas's TNFAIP3 (A20) hypothesis (see
`../../blinded_hypothesis_recovery/sjogren_tnfaip3/`). This run asks a wider question:
which drugs act on the mechanisms our entry records, or that the blinded OpenScientist runs
proposed, and which of them have never been tried in Sjögren's? Done 2026-11-06.

## Method

1. `genes.tsv`: 18 mechanism genes, each with the reason it is on the list. Sources are the
   dismech entry's own nodes (type I interferon, JAK-STAT, xerostomia), the leads from the
   blinded OpenScientist runs, and the top genetic hits for MONDO:0010030 in Open Targets.
2. `../repurposing_candidates.py` asks the Open Targets Platform GraphQL API for every drug
   or clinical candidate acting on each gene, in any disease, with its highest clinical stage
   and its action type on that gene. It then marks a drug as already tested in Sjögren's if
   Open Targets lists it against MONDO_0010030 or ClinicalTrials.gov has a trial of it whose
   title or conditions match `sj[oö]gren|sicca`. Output: `opentargets/candidates.tsv`.
3. Four candidates were assessed by OpenScientist with `../repurposing_template.md`, which
   asks whether the mechanism is active in the disease, whether blocking it has helped, and
   why it might fail. Reports are in `reports/`.


## Untested drug classes

Drugs acting in the useful direction (inhibitor or antagonist; agonist for CHRM3), at phase 2
or beyond somewhere, with no Sjögren's record in either source:

| Gene | Already tested in Sjögren's | Not tested, phase 2 or beyond elsewhere |
|---|---|---|
| IL12B / IL-23 | ustekinumab | risankizumab, guselkumab, tildrakizumab, mirikizumab (all approved or phase 4) |
| TLR7 | hydroxychloroquine | enpatoran (phase 3), afimetoran, bazlitoran (phase 2) |
| TNFSF13B (BAFF) | belimumab, tibulizumab; telitacicept via the disease list | atacicept, blisibimod, tabalumab (phase 3) |
| BTK | branebrutinib, tirabrutinib, remibrutinib | rilzabrutinib, acalabrutinib, orelabrutinib (approved) |
| PIK3CD | leniolisib, parsaclisib, seletalisib | duvelisib, copanlisib (approved) |
| CD40 | iscalimab, dazodalibep (via CD40LG) | bleselumab, dacetuzumab, lucatumumab (phase 2) |
| JAK1 / TYK2 | tofacitinib, baricitinib, upadacitinib, filgotinib, deucravacitinib | ruxolitinib, brepocitinib, peficitinib, abrocitinib |

## Limits of the table

- **Salt forms count separately.** "Filgotinib maleate" appears untested although filgotinib
  was tested. Read the untested column by active ingredient.
- **Some key genes have no mapped drugs**, although drugs exist: TNFAIP3, TNIP1, MALT1,
  IKZF1, IL7R and CXCR5. Iberdomide acts on IKZF1 through cereblon, safimaltib inhibits MALT1
  and the anti-IL-7R antibody GSK2618960 appears in the Sjögren's drug list with no target.
- **ClinicalTrials.gov search** matches by drug name. A trial registered only under a
  development code can be missed.
- **Agonists are listed** in the full table (interferons under IFNAR1, imiquimod under TLR7)
  and must be read as the wrong direction.

## OpenScientist assessments

All four reports had every cited PMID verified. One anifrolumab quote failed
the quote check only because of the bracketed "[95% CI]"; it matches the cached abstract of
PMID:41466456 exactly.

| Drug | Mechanism | Verdict |
|---|---|---|
| anifrolumab | type I interferon receptor blockade | Moderately to strongly supported, in the anti-SSA-positive, interferon-high subgroup. Rests on ANISE-II (NCT05383677, n=30), reported as meeting its endpoint (80% vs 30%) at EULAR 2026; that result is a conference abstract with no PMID, and ClinicalTrials.gov lists the trial status as unknown. Gland pathology is dominated by type II interferon, which the drug does not block. |
| atacicept | BAFF and APRIL neutralisation | Right target, drug never trialled. Telitacicept, a near-identical TACI-Ig, lowered ESSDAI in a phase 2 Sjögren's trial (PMID:37399108). The main risk is endpoint failure, a common fate of Sjögren's trials; infection risk; lymphoma prevention unproven. |
| enpatoran | TLR7/8 antagonism | Moderate to weak. Pathway active only in the interferon-positive subgroup; human genetics point to IRF5/STAT4 downstream, not TLR7. Hydroxychloroquine lowered the interferon signature without clinical benefit in JOQUER (PMID:25027140). Never trialled in Sjögren's. |
| MALT1 inhibitor (safimaltib) | CBM/NF-κB, lymphoma prevention | Weak. The premise that MALT1 translocations drive Sjögren's-associated MALT lymphoma is wrong: these lymphomas mostly lack them. MALT1 protease inhibition depletes regulatory T cells and causes autoimmunity in animals. The A20 loss itself holds up. |

## Recurring themes

- **Subgroup, not the whole disease.** All four point to roughly half of patients
  (anti-SSA-positive, interferon-high, early, systemically active) as the population where
  these mechanisms are active.
- **Biomarker change without clinical benefit** recurs: hydroxychloroquine (JOQUER),
  rituximab, remibrutinib (ESSDAI improved, symptoms did not).
- **Type II interferon (IFN-γ) and CD8 T cells** in the gland are named twice as the part of
  the disease these drugs do not reach. Our entry has no node for them.

## Leads for the dismech entry

- TNFAIP3 susceptibility row and the two A20 nodes (epithelial, B cell), as planned.
- A type II interferon / CD8 T-cell glandular node, with evidence from PMID:33572487 and
  PMID:41162286 (both cited by the enpatoran report; not yet read).
- BAFF transgenic sialadenitis (PMID:11781351) as model-organism evidence on Epithelial Cell
  Dysfunction, which already names BAFF.
- Treatments: telitacicept (phase 2 RCT, PMID:37399108) and the anifrolumab trial once
  published.
