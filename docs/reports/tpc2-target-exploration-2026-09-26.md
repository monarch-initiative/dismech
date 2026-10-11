# TPC2 as a therapeutic target: exploration

Target exploration, 2026-09-26. Follow-on from
[the chlorpromazine ALS hypothesis investigation](chlorpromazine-als-repurposing-hypothesis-2026-09-21.md),
which concluded "the interesting target here is TPC2, not chlorpromazine."

Curated artifacts:
`controversy_tpc2_direction_of_modulation` in
[`kb/modules/lysosomal_substrate_accumulation.yaml`](../../kb/modules/lysosomal_substrate_accumulation.yaml),
and three added evidence items plus a revised rationale on
`hyp_als_phenothiazine_autophagy_repurposing` in
[`kb/disorders/Amyotrophic_Lateral_Sclerosis.yaml`](../../kb/disorders/Amyotrophic_Lateral_Sclerosis.yaml).

## The headline, which revises last week's conclusion

**"TPC2 is the interesting target" was half right, and the half it got wrong matters.**

TPC2's ion selectivity is not fixed — it is set by which ligand opens the channel. A
NAADP-mimetic agonist gives non-selective cation currents and strong Ca²⁺ signals; a
PI(3,5)P₂-mimetic gives Na⁺-selective currents and weak ones; and the two are "coupled to
opposing changes in lysosomal pH and exocytosis" (PMID:32167471). So "a TPC2 agonist"
names at least two different drugs.

Once you split the arms, the evidence sorts cleanly, and chlorpromazine lands on the wrong
side:

| Arm | Compounds | In vivo efficacy |
|---|---|---|
| **NAADP-mimetic, Ca²⁺-permeable agonism** | NAADP, TPC2-A1-N, **chlorpromazine** | **none anywhere** |
| **PI(3,5)P₂-mimetic, Na⁺-biased agonism** | TPC2-A1-P; the LRRK2 "biased agonist" | MLIV mouse (rotarod, P62, astrogliosis); LRRK2 *Drosophila* behaviour |
| **Antagonism** | trans-Ned-19, tetrandrine, SG-094 | rat tMCAO infarct reduction; LRRK2 correction |

The chlorpromazine ALS paper benchmarks its evoked current against "TPC2 endogenous agonist
NAADP and its mimetic agent TPC2-A1-N", blocked by trans-Ned-19 (PMID:40796055). That is
the NAADP arm. Meanwhile the landmark storage-rescue paper — the one that made TPC2 look
like a drug target — used **TPC2-A1-P throughout**: 115 mentions of A1-P, zero of A1-N,
cells through iPSC neurons through the MLIV mouse. And in LRRK2 Parkinson's models,
"reducing Ca²⁺ permeability with a novel biased TPC2 agonist corrected deviant Ca²⁺ entry
and behavioral defects" (PMID:40279672).

So the ALS hypothesis runs through the one mode of the one channel for which no animal has
yet been shown to benefit. That is a sharper objection than any in last week's report, and
it is also more actionable: it names a different compound to try rather than just a reason
to stop.

## The direction of benefit is genuinely disputed

Three in vivo results, three directions, same channel:

- **Activate.** Small-molecule TPC2 activation "results in an amelioration of cellular
  phenotypes associated with LSDs such as cholesterol or lipofuscin accumulation"
  across mucolipidosis type IV, Niemann-Pick C1 and Batten patient fibroblasts and
  iPSC-derived neurons, with rotarod rescue, reduced P62 aggregates and reduced cerebellar
  astrogliosis in the MLIV mouse (PMID:35929194).
- **Inhibit.** "The pharmacological inhibition of TPC2 lysosomal channel by Ned-19 protects
  from focal ischemia by hampering a hyperfunctional autophagy" — reduced infarct volume
  and neurological deficit after rat tMCAO (PMID:36708960).
- **TPC2 is the disease.** Expressing human TPC2 in *Drosophila*, which lack TPCs,
  "phenocopied LRRK2 G2019S in perturbing dopaminergic-dependent vision and movement in
  vivo." The authors' own summary: "**Thus, both inhibition and select activation of TPC2
  are beneficial**" (PMID:40279672).

These are reconcilable, and the reconciling principle is not disease-specificity. The
stroke paper states it: "the role of autophagy in Stroke is controversial since excessive
or prolonged autophagy activation exacerbates ischemic brain injury." If autophagic flux
has an optimum, the therapeutic direction depends on which side of it the cell starts —
and neither a module node nor a target name records that.

This is the same shape as the pre-existing `gap_tfeb_direction_of_dysregulation_in_storage`
on the storage module, which asks whether TFEB should be raised or normalized. TPC2 sits
one step upstream and adds a dimension TFEB does not have: a biased agonist can move it in
two pharmacologically distinct directions, not just up or down. The new discussion says so
and cross-references the TFEB gap rather than restating it.

## What is genuinely attractive about the target

**Human loss of function is tolerated.** gnomAD v4 for TPCN2 (queried 2026-09-26):
pLI ≈ 6.1 × 10⁻²⁶, LOEUF 0.98, 92 observed pLoF variants against 111 expected
(o/e = 0.83). Monarch reports **zero** gene-to-phenotype and zero gene-to-disease
associations for HGNC:20820. There is no Mendelian TPCN2 disease. For an *antagonist*
programme that is close to an ideal safety prior — people who lack the channel are walking
around undiagnosed.

**The antagonist arm is structurally enabled.** SG-094, "a synthetic analog of the Chinese
alkaloid medicine tetrandrine with increased potency and reduced toxicity", has a solved
mechanism: it arrests the IIS4 voltage sensor in a downward state, resembling gating
modifiers of canonical voltage-gated channels (PMID:38815576). Tetrandrine itself came out
of the Ebola-entry work. This is real medicinal chemistry, not a tool compound.

**It is a convergence point across several dismech modules.** TPC2 activation rescues
diseases conforming to `lysosomal_substrate_accumulation`; its autophagy role sits on
`disabled_macroautophagy`; and melanosomes are lysosome-related organelles, so the
pigmentation phenotype touches `lysosome_related_organelle_biogenesis`. That is why the
curated artifact is a discussion on an existing module rather than a new module —
TPC2 dysfunction is not itself an established disease mechanism, it is an intervention
point on mechanisms already curated.

## What is genuinely unattractive

**Both arms have an on-target liability, and they are different liabilities.**

*Agonism* promotes exactly what the antagonist programmes are built to block. TPC2 loss
attenuates cancer cell migration and metastasis, impairs choroidal neovascularization and
iPSC-derived endothelial tube formation (PMID:42584788), and reduces infectivity for
cholera toxin and Ebola virus (PMID:33465068). A chronic systemic TPC2 agonist is a
pro-angiogenic, pro-migratory, pro-viral-entry drug by construction.

*Antagonism* has metabolic and — critically for ALS — neurodevelopmental costs.
TPC2⁻/⁻ mice "show defects in cholesterol degradation, leading to hypercholesterinemia;
TPC2 absence also results in mature-onset obesity, and a role in glucagon secretion and
diabetes has been proposed" (PMID:33465068). And in motor neurons specifically, TPC2 is
*required*: trans-Ned-19 and TPC2 knockout "attenuated CaP Ca²⁺ signaling and inhibited
axon extension" in zebrafish caudal primary motor neurons (PMID:32546534), and TPC2
inhibition "decreased the normal ipsilateral correlation and contralateral
anti-correlation, indicating a disruption in normal spinal circuitry maturation"
(PMID:29577882).

That last pair is the sharpest thing in this exploration. **In a motor-neuron disease, the
better-developed arm of TPC2 pharmacology acts against the arm of TPC2 biology that motor
neurons demonstrably need — using the very same compound.** trans-Ned-19 is neuroprotective
in stroke, corrective in LRRK2 models, and blocks motor axon extension. Whichever way you
push TPC2 in ALS, you pay.

**Most people do not carry reference TPC2.** "Surprisingly, one variation, L564P, was found
to be the predominant TPC2 isoform on a global scale", and L564P is a *prerequisite* for
the blond-hair-associated M484L gain-of-function effect (PMID:33465068). Any construct,
screen or potency measurement built on the reference sequence is measuring a minority
allele. This is a target-validation hazard that would be easy to miss.

**The best agonist is a poor drug.** TPC2-A1-P was "rapidly eliminated, being undetectable
by 240 min", and 20 mg/kg was chosen "to avoid off-target activity while providing a
therapeutic dose for > 20 min." The MLIV mouse rescue was achieved with roughly twenty
minutes of daily exposure. That is an encouraging efficacy signal and a discouraging
pharmacokinetic one, and it means sustained TPC2 activation has not actually been tested
for safety or sufficiency.

**The field says so itself.** "Despite its potential as a drug target, TPC2 is still in the
early stages of therapeutic development", with the major challenge being "achieving high
target specificity without inducing unintended effects on other endolysosomal channels"
(PMID:39978661). TRPML1/ML-SA1 is the obvious comparator and was run head-to-head in the
storage paper.

## Loose ends worth knowing about

**The gating controversy may have just been resolved.** A 2026 preprint reports that NAADP
"elicits two-pore channel currents by lifting Lsm12-mediated inhibition of PI(3,5)P₂
activation" (PMID:42039649) — i.e. one activation pathway with a removable brake rather
than two independent ligands. If that holds, the two-arm model above is a description of
two points on one mechanism rather than two mechanisms, which would change how a biased
agonist should be designed. **It is a bioRxiv preprint and not peer-reviewed**; it is
deliberately cited here and not in the KB.

**A new regulatory layer.** Mucin-type O-linked glycosylation at luminal Ser612/Ser613 acts
as a "structural gating brake" — "genetic, enzymatic, or pharmacological glycan removal
enhances basal and ligand-evoked TPC2 activity", driving lysosomal tubulation and cancer
cell migration reversible by tetrandrine (PMID:42270676). A post-translational set point
means TPC2 activity is not inferable from expression, which is worth remembering when
reading the one existing dismech mention of TPC2 as a protein-level readout
(`Dominant_Deafness-Onychodystrophy_Syndrome`, where TPC1/TPC2 are reported *upregulated*
in a lysosomal-acidification defect).

## Where this leaves the ALS hypothesis

Revised, not abandoned, and the revision is a different first experiment.

Last week's window study asked whether chlorpromazine's TPC2/TFEB engagement is reachable
below the motor-toxicity threshold. It should now also read out the **PI(3,5)P₂-biased
mode**, because if motor-neuron TDP-43 clearance tracks that mode instead, the useful
compound is TPC2-A1-P or a successor — not an antipsychotic, and none of the dopaminergic
window problem applies. That is a strictly better experiment and roughly the same cost.

And the obvious alternative — block TPC2, since that arm is better developed and human LoF
is tolerated — is specifically contraindicated in a motor-neuron disease by the zebrafish
axon-extension result. Both of those are now recorded on the ALS discussion.

## Sources

Twelve TPC2 references cached under `references_cache/`; all snippets quoted in the KB are
exact-quote verified (243/243 in the ALS entry, 23/23 in the module).

| PMID | Role |
|---|---|
| 32167471 | Ion selectivity is set by the activating ligand; opposing effects on lysosomal pH and exocytosis |
| 35929194 | TPC2-A1-P rescues MLIV/NPC1/Batten; MLIV mouse in vivo; PK and ML-SA1 comparison |
| 36708960 | trans-Ned-19 inhibition is neuroprotective in rat tMCAO |
| 40279672 | TPC2 is pathogenic in LRRK2-PD; both inhibition and biased activation beneficial |
| 40796055 | Chlorpromazine's TPC2 current benchmarked against NAADP / TPC2-A1-N |
| 39978661 | Drug-development review: early stage, selectivity is the main challenge |
| 38815576 | SG-094 / tetrandrine antagonist structural mechanism |
| 33465068 | L564P is the predominant global isoform; TPC2⁻/⁻ mouse metabolic phenotypes |
| 42270676 | O-glycan gating brake; lysosomal tubulation; migration reversible by tetrandrine |
| 42584788 | TPC2 loss impairs choroidal angiogenesis and endothelial tube formation |
| 32546534 | TPC2 required for motor axon extension; trans-Ned-19 blocks it |
| 29577882 | TPC2 required for spinal circuit synchronization in primary motor neurons |
| 42039649 | *Preprint, not peer-reviewed.* NAADP acts by lifting Lsm12 inhibition of PI(3,5)P₂ activation |

Identity and constraint checked 2026-09-26: HGNC:20820 `TPCN2`, "two pore segment channel
2", 11q13.3, UniProt Q8NHX9, OMIM 612163 (gene). gnomAD and Monarch figures as quoted
above.
