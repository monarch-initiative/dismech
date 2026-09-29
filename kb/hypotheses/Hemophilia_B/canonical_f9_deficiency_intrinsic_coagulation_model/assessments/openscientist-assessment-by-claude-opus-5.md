# OpenScientist report review: canonical F9 deficiency / intrinsic coagulation failure model

**Hypothesis:** `canonical_f9_deficiency_intrinsic_coagulation_model` (Hemophilia B)
**Provider:** openscientist · **Assessor:** claude-opus-5 · **Verdict:** SUPPORTED

## What the report was asked, and what it could add

The seed handed to the provider was the knowledge base's own canonical hypothesis,
already marked CANONICAL. A report cannot support a hypothesis by restating it, so the
question here is narrower than the report's own framing suggests: does it bring
anything the entry did not already have?

It does, and the reason is unusual. The `Hemophilia_B` entry carried a long
`mechanistic_hypotheses` note listing six refinements to the canonical model — the
rebalancing therapies, hemophilia B Leyden, phenotype modifiers, inflammatory
arthropathy, the bone phenotype, and inhibitor development — with not one citation
behind any of them. The report is where those six sentences came from, and it names a
source for each. Most of the review work was therefore checking whether those sources
say what the note assumes they say.

I fetched and read 17 of the 44 cited identifiers. All 17 resolve, including the four
above 41000000 that look implausible at a glance.

## What held up

The load-bearing citations are exact. PMID:41358585 gives the HOPE-B five-year adjusted
bleeding rates verbatim, 4.16 down to 1.52, a 63 percent reduction with a 24-to-82
interval. PMID:40239068 gives the fidanacogene multiyear result. PMID:31219805 states
that FIX-Padua hyperactivity requires factor VIIIa cofactor and is ablated in an
emicizumab-based system. PMID:23472758 identifies ONECUT1 and ONECUT2 as the missing
hemophilia B Leyden regulators with binding loss graded by clinical severity, and
PMID:1631121 gives the HNF-4 half of the same story. PMID:28508290 reports the CRISPR
correction. PMID:42119948 reports the methotrexate arthropathy experiment.
PMID:40053895 reports the fitusiran extension result. PMID:29925096 and PMID:36163649
give the inhibitor incidence and the genotype gradient behind it.

## What did not

Four problems, none of them fatal to the model, all of them consequential for what may
be curated.

**The BENEGENE-2 quotation cannot be checked.** PMID:39321362 fetches with
bibliographic metadata but no abstract text, so the proposed snippet — which is also
stitched across an ellipsis — has nothing in this repository to validate against. The
same trial programme is represented in the integration by PMID:40239068 instead.

**The bone claim inverts its own source.** The report reads the FIX-knockout skeletal
phenotype as evidence that factor IX has a role outside hemostasis. PMID:34117910
concludes the opposite: that its findings, together with parallel ones in
FVIII-deficient mice, point to an effector *downstream of the coagulation cascade*
being necessary for normal skeletal development. That is a claim about thrombin or
something like it, shared with hemophilia A, not about a second job for factor IX. The
report's evidence-matrix row 22 states the inverted version outright.

**The emicizumab claim is true but uncited.** PMID:39613145 never says emicizumab is
inapplicable to hemophilia B. It says factor VIII-mimetic agents transformed hemophilia
A management and that rebalancing agents show promise in hemophilia B. The inference is
the report's own, and is better supported by PMID:31219805 elsewhere in the same
report.

**Two findings are imported from the wrong population.** The FVII 353Q modifier result
(PMID:19686262) comes from a severe-haemophilia cohort whose comparability analysis
reports F8:c activity, and its direction is toward *more* severe disease, not the
milder-than-expected disease the surrounding text is explaining. The X-inactivation
result (PMID:33082527) is an association across two dichotomized strata in a mixed
carrier cohort, which the report reports as the bleeding phenotype being "directly
proportional" to F9 gene dosage.

A fifth item is worth flagging separately because it is a false negative rather than an
overstatement: Gap 8 reports that no ClinGen or GenCC gene-disease validity entry was
identified for F9 and hemophilia B. ClinGen has classified the relationship as
Definitive, and that assertion was already curated in the disorder YAML before this run.

## Integration into the disease YAML

Target: `kb/disorders/Hemophilia_B.yaml`.

**Added.**

- Seven evidence items on the `canonical_f9_deficiency_intrinsic_coagulation_model`
  entry, one per previously uncited assertion in its `notes`: PMID:28508290 for the
  CRISPR clause, then PMID:40053895, PMID:23472758, PMID:19686262, PMID:42119948,
  PMID:34117910 and PMID:29925096 for refinements (1) through (6). The two
  wrong-population caveats above are stated in the relevant `explanation` fields rather
  than left implicit.
- Two pathophysiology nodes, `Intrinsic Tenase Complex Failure` and `Deficient Thrombin
  Generation`, with a new `Factor IX Deficiency` edge into the first. The entry's own
  hypothesis description asserted both steps while its pathograph jumped straight from
  factor IX deficiency to bleeding. Evidence: PMID:31219805 and PMID:11434702 for the
  tenase node, PMID:15735797 for the thrombin node.
- Two trial results on the `Gene Therapy` treatment, PMID:41358585 and PMID:40239068,
  plus a `target_mechanisms` link to `Factor IX Deficiency` and
  `therapeutic_modality: GENE_THERAPY`. The treatment previously rested on a guideline
  sentence that merely listed gene therapy among novel strategies.
- PMID:36163649 on the `F9` genetic entry, for the variant-class gradient in inhibitor
  risk.
- Three discussions: `hemophilia_b_bone_extrahemostatic_role` and
  `hemophilia_b_arthropathy_inflammatory_arm` as `HUMAN_MODEL_MISMATCH`, and
  `hemophilia_b_gene_therapy_durability` as `KNOWLEDGE_GAP`.

**Deliberately not added.**

- *Rebalancing therapies as a treatment.* Fitusiran, concizumab and marstacimab are
  curated on the parent `Hemophilia` entry, with a written rationale that the class acts
  on the anticoagulant side and is therefore indifferent to which subunit is missing, so
  it belongs at the root rather than on either member. Duplicating it here would
  contradict that decision. The mechanistic point it makes is captured as hypothesis
  evidence instead.
- *Hemophilia B Leyden as a subtype.* Already a subtype on the parent entry, which
  records explicitly that Leyden has no dismech entry of its own. Only the ONECUT
  transcriptional mechanism was added, as hypothesis evidence.
- *An inheritance block carrying the X-inactivation result.* The entry has no
  `inheritance` section, and adding one on the strength of an overstated reading of a
  mixed carrier cohort would import the overstatement.
- *The emicizumab asymmetry as a standalone claim.* Real, but not asserted by the source
  cited for it, and already covered by the parent entry's rebalancing rationale.
- *The BENEGENE-2 snippet, the 1,200-variant count, the Italian inhibitor series
  (PMID:23601006), and the two acquired-hemophilia case reports.* Unverifiable here,
  uncited in the report, or not fetched.
- *Any status change.* The report recommends retaining CANONICAL and the entry already
  does.
