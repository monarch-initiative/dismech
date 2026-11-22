# Citations for Research Query

**Query:** # NAM Mining Research Template

## The single paper under study

- **Reference:** PMID:37418196; DOI 10.1021/acs.jmedchem.3c00647; PMC10833105; J Med Chem 2023;66(14):9853-9865.
- **Access:** Not open access, but PMC full text is cached and quotable (references_cache/PMID_37418196.md, full_text_xml). A claim supported only by the full text is usable -- say which claims came from the full text and which from the abstract.

A medicinal-chemistry lead-optimisation study, not a disease study. The authors synthesise spiro imidazobenzodiazepine analogues of MIDD0301 and screen them for GABA_A receptor (GABA_AR) affinity, physicochemical properties, metabolic stability and bronchodilator activity. Asthma is the indication the compounds are being developed for; the paper does not model asthma pathogenesis, and nothing in it is an asthma disease model. What it does assert and measure is a *pharmacological* mechanism: GABA_ARs carrying alpha4 and alpha5 subunits are present on airway smooth muscle, and ligands binding the allosteric benzodiazepine site relax that muscle and reverse bronchoconstriction. The compounds are deliberately engineered NOT to cross the blood-brain barrier, which is the paper's safety argument and is tested separately. Treat this as a paper about a drug's point of attack, in the same sense as the existing "Beta2 Agonist Occupancy of Airway Smooth Muscle Receptors" node in the Asthma entry -- not as a paper about how asthma arises.

**Confine the research to THIS paper's own findings.** Use other literature only to
judge validity or divergence, and when you do, cite it separately and say so. Do not
attribute another paper's result to this one.

## Goal

Decide, from this paper, **what each of its biological systems models, what it does
not, and how faithfully** — so that:

1. a mechanism knowledge base can link each system to the mechanism nodes it informs,
   with a relationship verb, a fidelity tier, the scale the system actually observes,
   and the translational caveats that must travel with each link; and
2. a method registry can hold each system as a method in its own right, with what it
   is used for and what it cannot show.

A system that supports no mechanism link is still a result. Say so plainly and give
the reason, rather than reaching for the nearest node.

## The biological systems, which must be kept separate in your answer

Nine separable systems. Most are registry NAM records; several are animal.
Judge each one on its own -- do not collapse them into "the study".

1. **Molecular docking** -- in silico, MOLECULAR scale. GABA_AR crystal
   structure 6HUO (alpha1beta3gamma2 with alprazolam), MOE software, rigid
   receptor and induced fit, scored against a pharmacophore requiring a
   halogen bond to His102 and a hydrogen bond to Ser206. Correlated against
   the empirical binding data.
2. **GABA_AR radioligand competition binding** -- in vitro. Displacement of
   3H-flunitrazepam from **rat brain extract**, run by the NIMH PDSP program
   at UNC Chapel Hill. Note the tissue and species carefully (see
   `does_not_model`).
3. **PAMPA permeability** -- in chemico / cell-free. Parallel artificial
   membrane permeability assay, hexane/hexadecane layer, 18 h equilibrium.
4. **Shake-flask aqueous solubility** -- bioanalytical, pH 7.2.
5. **HEK293 cytotoxicity** -- in vitro, CellTiter-Glo, LD50.
6. **Microsomal stability** -- in vitro ADME, human and mouse liver
   microsomes (Table 2).
7. **Guinea pig tracheal ring organ bath** -- ex vivo tissue. Hartley guinea
   pig tracheal rings, **epithelium removed with a cotton swab**, pretreated
   with tetrodotoxin and pyrilamine to remove nerve and histamine
   contributions, indomethacin in the buffer, contracted with substance P,
   force recorded on a Grass FT03 transducer.
8. **Rotarod sensorimotor assay** -- in vivo mouse. The blood-brain barrier
   test, with diazepam as the positive control.
9. **A/J mouse double-chamber plethysmography** -- in vivo mouse. Conscious,
   non-invasive airway mechanics; nebulised compound then five nebulised
   methacholine challenges; specific airway resistance (sRaw) as the readout.

Each system gets its own section. Do not merge them, and do not attribute a readout
taken in one system to another. Where one system is built from another (an organoid
grafted into an animal, a monoculture combined into a co-culture), the combination is
its own system and its readouts belong to it.

If the paper describes a system not listed above, add it with a note that it was not
in the brief. If a listed system turns out not to be in the paper, say so.

## The candidate mechanism nodes to test each system against

Report, for each system, which of these it bears on and how. Use these exact node
names:

**Read this first: the mechanism this paper measures has no node.** dismech
carries a pharmacology module for each of the other two inhaled bronchodilator
classes and none for this one:

- `beta2_adrenergic_receptor_agonism` -- receptor occupancy -> Gs/adenylate
  cyclase/cAMP -> airway smooth muscle relaxation -> bronchodilation.
- `muscarinic_receptor_antagonism` -- antagonist occupancy -> loss of
  Gq/PLC/calcium signalling -> withdrawal of cholinergic contraction ->
  bronchodilation.

There is **no GABA_A receptor module**, and no node named for GABA_A anywhere
in `kb/modules/`. A GABA_AR ligand-gated chloride channel on airway smooth
muscle is a third, mechanistically disjoint route to the same effector, and
nothing in the KB holds it.

So the primary task here is to **characterise the gap, not to force a link**.
State what a `gaba_a_receptor_agonism` module would have to contain for this
paper's systems to attach to it -- trigger, transducer, effector, apical node
-- following the shape the two sibling modules already set.

Nodes that DO exist and are worth testing the paper's systems against, with
the caution that most of them are the near-misses listed in
`anchors_to_avoid`:

- **Asthma#Bronchoconstriction** -- the state these compounds reverse. The
  ex vivo and in vivo systems both act on it. This is the only existing node
  the paper's functional data plausibly bears on, and even here the relation
  is reversal, not causation. The existing beta2 node in this same entry is
  explicit that a drug's point of attack "carries no downstream edge",
  because a downstream edge would assert the drug causes the obstruction it
  relieves. Respect that.
- **Asthma#Beta2 Agonist Occupancy of Airway Smooth Muscle Receptors** --
  cite this as the **shape precedent only**, never as a link target. It is
  what a GABA_AR occupancy node in this entry would look like.

**Anchors to avoid, and why:**

Every one of these shares vocabulary with the paper and asserts a mechanism
the paper did not measure. Name-matching onto one of them is the failure this
run most likely produces.

- **`beta2_adrenergic_receptor_agonism#Airway Smooth Muscle Relaxation`** --
  the single most dangerous anchor in the KB for this paper, because the node
  name is almost exactly the paper's own phrase. **Do not link to it.** That
  module's declared scope is the beta2 chain only, and its relaxation node
  sits downstream of Gs-coupled adenylate cyclase and cAMP. GABA_ARs are
  ligand-gated chloride channels; the paper measures no cAMP, no Gs, and no
  beta2 engagement. Linking here would assert a transducer the paper never
  touched.
- **`beta2_adrenergic_receptor_agonism#Bronchodilation and Relief of Airflow
  Obstruction`** -- same objection. The apical effect is shared between drug
  classes, but the node lives inside a beta2-scoped module, so a link asserts
  the beta2 route.
- **`beta2_adrenergic_receptor_agonism#Beta2 Adrenergic Receptor Agonist
  Occupancy`** -- wrong receptor entirely.
- **`muscarinic_receptor_antagonism#Withdrawal of Cholinergic Airway Smooth
  Muscle Contraction`** -- wrong receptor, and the direction is different:
  muscarinic antagonism removes a contractile drive, whereas these compounds
  are reported to relax muscle already contracted by substance P.
- **`chemical_respiratory_allergy#Airway Hyperresponsiveness and Variable
  Airflow Limitation`** -- shares the words "airway hyperresponsiveness" with
  the paper's AHR readout, but that module is about sensitiser-driven
  allergic airway disease. The A/J mouse exhibits methacholine AHR **without
  any allergen sensitisation or challenge**, by the authors' own statement.
  This is a pharmacological challenge readout, not chemical respiratory
  allergy.
- **Asthma#Airway Inflammation**, **Asthma#Airway Remodeling**,
  **Asthma#Mucus Overproduction** -- the paper measures none of these. It
  cites *prior* work that a different compound reduced lung eosinophils; that
  is background, not a finding of this paper, and must not become a link.
- Any CNS GABA / benzodiazepine anchor (the KB has GABAergic nodes in
  neurodevelopmental and epilepsy modules). The entire design goal here is to
  **avoid** CNS GABA_AR engagement, and the rotarod result is a negative.
  A CNS link would invert the paper's claim.

Do not select an anchor because its name resembles the paper's wording. A node is
right only if the paper's finding is the mechanism the node asserts. Where no listed
node fits a mechanism the paper does establish, report it under the gaps section
instead of forcing a link.

## What each pairing row must contain

Every (system → node) pairing you assert is one link object, and the definitions
below are that object's own, from the schema the answer has to land in. Fill each
field on its own terms: they are four different questions, not four chances to say
the same thing. In particular, note what the schema says about `limitations` and
`divergences` — the second is the typed form of the first, so a caveat belongs in
both as one account, not as two differently worded ones.

Links an experimental (NAM), animal, or computational model to a specific
pathophysiology mechanism node, recording which facet of that mechanism the
model recapitulates, perturbs, or reads out; how faithfully it does so; and
the outcome measures that ground the claim.

> Two evidence layers, deliberately separate. Evidence on the link attests
> that the model is informative for the node; evidence on each readout attests
> that a specific measurement was made, in a specific direction.

> Readouts belong on the link rather than on the model, because one model
> typically measures different things for different mechanism nodes.

> A FAILS_TO_RECAPITULATE link is a substantive negative claim and should
> carry both `limitations` and `evidence`; it usually pairs with a
> HUMAN_MODEL_MISMATCH discussion.

> A link is a *context-of-use* statement in the sense of the model-credibility
> literature: it asserts that this model is informative for this specific
> mechanism, which is a narrower and more checkable claim than "this model is
> good". `divergences` is the corresponding applicability analysis. The
> framing is borrowed from ASME V&V 40 and the FDA credibility guidance (both
> written for medical-device submissions) and from the healthcare-wide ten
> rules of credible practice, whose rule 1 is "define context clearly" and
> rule 4 "list limitations explicitly".

> `model_scale` records the scale the model observes, against which the target
> node's own `biological_scale` can be compared. The comparison is directional
> and the two directions mean different things: a model BELOW its target's
> scale is extrapolating upward — it cannot observe the outcome it is cited
> for — whereas a model ABOVE its target's scale contains that scale and is
> normally unremarkable (a whole animal can report a molecular readout). Do
> not store the comparison; derive it.

### `relationship`

What this model does to the linked mechanism: reproduces it, manipulates it,
measures it, rescues it, or fails to reproduce it.

One of:
  - `RECAPITULATES` — The model reproduces the linked mechanism, such that observations in the model are taken to be informative about the human mechanism.
  - `PARTIALLY_RECAPITULATES` — The model reproduces some but not all of the linked mechanism. Use `limitations` to state which facets are and are not reproduced.
  - `FAILS_TO_RECAPITULATE` — The model does NOT reproduce the linked mechanism. This is a substantive negative claim and the structural signal for a HUMAN_MODEL_MISMATCH discussion; it requires `limitations` and supporting `evidence`.
  - `PERTURBS` — The model manipulates the linked mechanism (knockout, knockdown, overexpression, chemical challenge) without itself being a claim that the full mechanism is reproduced.
  - `MEASURES` — The model provides a readout of the linked mechanism without claiming to reproduce or perturb it.
  - `RESCUES` — The model demonstrates reversal or correction of the linked mechanism, typically a genetic-correction, drug-rescue, or isogenic-repair arm.

### `description`

Brief assertion-level note describing what facet of the linked mechanism the
model captures or assays.

### `readouts`

Outcome measures through which this model reports on the linked mechanism,
each optionally grounded to an OBI assay, an HP phenotype, a biomarker, or a
GO process, with a measured direction and its own evidence. Each readout's own
`target` is required and must repeat the link's `target`, so a readout stays
self-describing when lifted out of its link by the graph and KGX exporters.

A structured readout or outcome measured in an experiment or reported by a
model. Use descriptor slots to ground readouts to phenotypes, biomarkers,
biological processes, and assays.

> Reached from Experiment.readouts for a proposed or executed experiment, and
> from ModelMechanismLink.readouts for the outcome measures a curated model
> reports on a pathophysiology node. Reusing one class keeps a proposed
> experiment and a realized model directly comparable.

- **`direction`** — Direction of the measured or expected effect. Accepts ModelReadoutDirectionEnum (INCREASED, DECREASED, UNCHANGED, RESTORED, ABOLISHED, ALTERED) for an experimental measurement relative to its comparator, and BiomarkerReadoutDirectionEnum for a readout expressed as the direction of association with an endpoint. Prefer the model enum for a measurement made in a model system.
- **`interpretation`** — Curator-facing explanation of how this readout would be interpreted relative to the experiment's decision criterion, or of what the measured value says about the linked mechanism.

### `fidelity`

Curator assessment of how faithfully this model captures the linked human
mechanism. A translational-validity caveat, not a metric.

One of:
  - `HIGH` — Human-derived or otherwise closely matched system reproducing the mechanism with well-characterized correspondence to human disease.
  - `MODERATE` — Reproduces the mechanism with known and material divergences from human biology (species differences, supraphysiological expression, reduced cellular complexity).
  - `LOW` — Informative but with divergences substantial enough that findings should not be transferred to human disease without corroboration.
  - `UNKNOWN` — Correspondence to the human mechanism has not been established. Prefer this over guessing a tier.

### `limitations`

Specific caveats on transferring findings from this model to the human
mechanism: species divergence, supraphysiological expression, absent cell
types, missing immune or vascular compartments, and similar.

### `model_scale`

Biological scale at which this model actually represents or measures the
linked target — molecular, cellular, tissue/organ, or organism. Records what
the model *observes*, which is not always the scale of the mechanism it is
cited for: a signalling-network model whose output node is named for a tissue-
level outcome still observes only molecular state. Compared against the target
node's own `biological_scale`, this makes the scale gap computable rather than
leaving it buried in `limitations` prose. Reuses BiologicalScaleEnum so the
two are directly comparable.

One of:
  - `MOLECULAR` — Molecular scale — molecular activities (kinase activity, transcription factor binding, ion transport, catalysis) or molecular states (a fusion protein exists, a chemical accumulates, an enzyme is functionally deficient, a gene carries a variant burden). Substrate is a molecule, complex, or genetic element.
  - `CELLULAR` — Cellular scale — cellular processes (differentiation, apoptosis, autophagy, intracellular signaling) or cellular states (a cell population is in a maintained aberrant condition, an organelle is structurally disrupted, a cell type has accumulated). Substrate is a single cell or cell type.
  - `TISSUE` — Tissue / organ scale — tissue processes (inflammation, fibrosis, granuloma formation, neoplastic outgrowth) or tissue states (an ectopic tissue persists, an organ is malformed, a structural lesion exists). Substrate is a tissue, organ, or anatomical structure.
  - `ORGANISM` — Organism scale — systemic / multi-organ / whole-body processes (DIC, cytokine storm, fever, cachexia) or systemic states (a metabolite is chronically elevated, the microbiome is dysbiotic, a syndromic developmental phenotype bundles multi-organ features). Substrate is the whole organism.

### `divergences`

Typed, individually explained ways in which this model departs from the
mechanism it is linked to. The structured counterpart of the free-text
`limitations` summary: each entry names a kind from a fixed taxonomy, says in
the curator's own words why that kind of gap applies *here*, and optionally
records whether it bears on this link's claim. Multivalued because a real
caveat is usually several kinds at once.

One typed way in which a model departs from the mechanism node it is linked
to, with the curator's explanation of why that gap applies to this particular
claim.

> The point of the type is queryability -- "which models are limited by
> calibration provenance rather than by species" is not answerable against a
> prose `limitations` string. The point of the required `description` is that
> the type alone is never the argument: BOUNDARY_OMISSION says a component is
> missing, not which one or why it matters here.

> Orthogonal to `relationship` and `fidelity`. A link can be RECAPITULATES
> with several QUALIFYING divergences, or PARTIALLY_RECAPITULATES for a reason
> that is not a divergence in this taxonomy at all.

- **`divergence_type`** — Kind of departure between the model and the mechanism it is linked to
    - `BOUNDARY_OMISSION` — A component, cell type, compartment, or process the mechanism requires lies outside the model boundary. The commonest kind. Contrast PROXY_QUANTITY, where the thing is in the model but stands in for something else.
    - `PROXY_QUANTITY` — The model's variable is a stand-in of a different quantity from the one the mechanism node describes -- transcriptional regulation of dopamine synthesis for striatal dopamine concentration, an imaging signal for the tissue property it correlates with. Can occur at the same biological scale, so it is not recoverable from `model_scale`.
    - `CALIBRATION_PROVENANCE` — Parameters, training data, or validation derive from a system, cohort, or measurement type that does not match the claim -- fitted to cultured epithelia, parameterized from mouse fibroblasts, validated against aggregate rather than individual outcomes.
    - `CAUSE_UNREPRESENTED` — The disease lesion is not encoded; the mechanism is imposed phenomenologically instead of arising from the allele, exposure, or perturbation that causes it. Also covers a perturbation that cannot be applied in isolation.
    - `STRUCTURAL_IDEALIZATION` — Geometry, topology, or spatial organisation is idealized rather than anatomically or patient-derived -- a symmetric airway tree, a one-dimensional strand standing for a reconstructed outflow tract, spatially uniform fields.
    - `TEMPORAL_SCOPE` — The model's time horizon or dynamic resolution does not match the mechanism's: an acute-injury window standing for chronic progression, or a parameter-free qualitative model that reaches reachability but not magnitude or timing.
    - `CONTESTED_ASSUMPTION` — The model encodes a mechanistic assumption that independent or later evidence disputes, or that rests on a structure not experimentally known. Distinct from the other kinds in that the model may be internally sound and still wrong about the biology.
    - `SCALE_EXTRAPOLATION` — The model observes below the biological scale of the node it is cited for and infers the higher-scale outcome. Derivable from `model_scale` versus the target's `biological_scale`; record it explicitly when the curator wants to state why it matters here.
    - `SPECIES_MISMATCH` — The model, or the data behind it, derives from a non-human system. Marginal among computational models and dominant among animal models, where it is the principal translational caveat.
    - `POPULATION_MISMATCH` — The modelled cohort, subtype, or indication is not the one this entry describes -- a generic model standing for a genotype-defined disorder, or a cohort that mixes in cases outside the entry's molecular criteria.
    - `OTHER` — A divergence that does not fit the values above. Requires a `description` that states the kind plainly, and is a signal the taxonomy may need a value.
- **`description`** — Why this kind of divergence applies to this link, in specific terms -- which component is outside the boundary, which quantity is standing in for which, which cohort the calibration came from. Never a restatement of the enum value.
- **`materiality`** — Whether this specific divergence bears on the specific claim the link makes. Per-divergence, where `fidelity` is per-link.
    - `INVALIDATING` — The claim should not be transferred to human disease on this model alone. Usually pairs with PARTIALLY_RECAPITULATE or FAILS_TO_RECAPITULATE and a low fidelity tier.
    - `QUALIFYING` — The claim holds, but in a narrower form than the link's `description` would suggest on its own. The commonest value.
    - `IMMATERIAL` — A real divergence that does not bear on this particular claim. Worth recording precisely because it stops a reader inferring that a known limitation of the model undermines this use of it.
    - `UNKNOWN` — Bearing on the claim has not been assessed. Prefer this over guessing.

### Also required on every pairing

- **a verbatim quote** — an exact substring of the paper that supports the pairing,
  with its PMID or DOI. Do not paraphrase. If a claim is supported only by the full
  text and not the abstract, say so. Never invent an identifier or a quote.
- **one line on why that relationship verb and not its neighbours.** The verbs are
  close together, and the reason you rejected the adjacent one is what a curator
  needs in order to check the choice.

A **FAILS_TO_RECAPITULATE** pairing is as valuable as a positive one, and so is a
**RESCUES** pairing where a system restores a node. Report both as first-class
findings rather than omitting them.

## What each system needs for a registry record

Separately from the pairings, and for every system whether or not it supports a
pairing, report:

- **what the system is** — its cells or organism, their species and source
  (pluripotent stem cell, adult tissue, cell line, primary cell, tumour tissue), its
  format, and the exposure or culture conditions that define it.
- **applications** — what the paper uses it to do, one entry per distinct use.
- **limitations** — what the system cannot show, in the paper's own terms where it
  states them.
- **characterization and validation readouts** — the assays run *on* the system.
  These are readouts, not systems of their own; keep them here rather than listing
  each as a model.
- **named variants** — where the paper describes variants of one protocol, say
  whether each is a variant of a single system or a system in its own right, and why.

## Specific claims from the paper to find, quote and verify

For each, give the exact supporting sentence and its location (abstract or full text):

Quote from the cached full text. The compound numbering (3a-g, 4a-i, 5a-j)
matters -- most claims are compound-specific and do not generalise.

- Compound **5c** binds GABA_ARs with an **IC50 of 9 nM**, the best in the
  series, and was the most promising compound overall.
- GABA_AR binding was measured by **competition of 3H-flunitrazepam using rat
  brain extract**, by the PDSP program at UNC Chapel Hill; compounds were
  screened at 10 uM and those exceeding 50% inhibition taken to dose response.
- Other affinities: 3c 42 nM, 3b 134 nM, 3g 665 nM, 4c 87 nM, 4i 509 nM,
  5h 55 nM, 5b 145 nM, 5j 289 nM. 3e, 3f, 4e, 4f showed no significant
  binding. Binding diminished with increasing spiro ring size.
- Docking used crystal structure **6HUO** of alpha1beta3gamma2 GABA_AR in
  complex with alprazolam; 5c docked in the alpha1+/gamma2- interface with a
  **halogen bond to His102** and hydrogen bonds to **Ser206 and Ser205**. A
  **moderate** correlation between docking score and % GABA_AR binding was
  observed, with poor correlation for weak binders.
- GABA_AR subtypes with **alpha4 and alpha5 subunits are present on airway
  smooth muscle**; **alpha2 and alpha3 subunits on inflammatory cells**.
  (Check whether the paper measures this or cites it -- references 6 and 7.)
- Compounds 5a-j have the lowest permeabilities of all tested compounds, in a
  narrow range **between -6.4 and -7.1 log Pe (cm/s)**, attributed to the
  charged carboxylate at neutral pH.
- **None** of the imidazodiazepine acids impaired trained mice on a rotating
  rod at an oral dose of **40 mg/kg**; diazepam, of similar GABA_AR affinity
  to 5c but BBB-penetrant, caused rapid significant loss of sensorimotor
  coordination at **8 mg/kg**.
- Ex vivo: **25 uM** of **5c, 5f, 5h and 5j** caused significant relaxation of
  substance-P-constricted guinea pig tracheal rings at **30 min**, with 5c
  strongest (**p < 0.001** at 30 min); weak relaxation for 5b and 5d at
  60 min. The vehicle shows a typical time-dependent force reduction from the
  limited half-life of substance P -- note that this is why comparison is
  against vehicle, not against baseline.
- In vivo: **A/J mice**, chosen because they exhibit severe methacholine AHR
  **without preexisting allergen sensitisation and challenge**; compounds
  nebulised at **7.2 mg/kg**. **5b, 5c, 5h and 5j** reduced sRaw within the
  first methacholine challenge; weak binders **5a and 5d-f** showed little to
  no change versus vehicle.
- A **discordance worth capturing**: **5f showed a much stronger ex vivo
  effect than in vivo effect**. The authors flag this themselves. It is a
  direct statement about the limits of the ex vivo system as a predictor.
- The authors' mechanistic conclusion: the allosteric benzodiazepine binding
  site **between the alpha and gamma subunits** can only accommodate
  spiro-imidazodiazepines with a **three-membered ring**.

## What the systems do NOT model

State these explicitly and attribute each to the right system:

Per system. The authors' own caveats first, then the ones the design forces.

- **The paper models no asthma pathogenesis at all.** Not inflammation, not
  remodelling, not mucus, not sensitisation, not any endotype. Asthma is the
  indication, not the object of study. Any link must be to the drug's point
  of attack, reversing bronchoconstriction -- never to a step in how asthma
  arises.
- **Binding (system 2) is measured in rat brain extract, not airway tissue,
  and not on the airway subtypes.** The paper states the airway target is
  alpha4/alpha5, while flunitrazepam competition reports a *mixture* of
  brain-expressed subtypes (alpha1-3,5,6 beta1-3 gamma1-3/delta), of which
  the brain composition is given as 43% alpha1beta2gamma2 and only 4%
  alpha5beta3gamma2. So the headline **9 nM affinity is a proxy on the wrong
  tissue and the wrong species**, dominated by subtypes that are not the
  therapeutic target. This is both a species divergence and a proxy-quantity
  divergence, and it must not be reported as airway GABA_AR affinity.
- **Docking (system 1) is on alpha1beta3gamma2**, again not the alpha4/alpha5
  airway subtypes, and the correlation to measured binding is only moderate.
  It is a design-guidance tool here, not evidence of an airway interaction.
- **The ex vivo trachea (system 7) has had its epithelium removed**, and
  nerves (tetrodotoxin), histamine (pyrilamine) and prostanoids
  (indomethacin) blocked. It is deliberately reduced to smooth muscle, so it
  cannot speak to epithelial, neural or inflammatory contributions to airway
  tone. It is also **guinea pig**, and the contractile agonist is
  **substance P**, which is not the stimulus of clinical bronchoconstriction.
- **The in vivo AHR model (system 9) is methacholine challenge in a strain
  with innate hyperresponsiveness and no allergen sensitisation.** It is a
  bronchoconstriction-reversal assay, not a model of asthma. sRaw from
  double-chamber plethysmography in conscious mice is an indirect,
  non-invasive measure.
- **The rotarod (system 8) is a negative result** -- absence of sensorimotor
  impairment. It supports the absence of CNS GABA_AR engagement at the dose
  tested; it does not measure brain concentration directly, and a negative
  behavioural assay is weaker than a pharmacokinetic measurement.
- **PAMPA (system 3) is an artificial lipid membrane**, not a cell monolayer
  and not a blood-brain barrier model. Permeability here is a physicochemical
  property, not a statement about tissue distribution.
- **Cytotoxicity (system 5) is HEK293**, a human embryonic kidney line with no
  airway relevance. It bounds general toxicity only.

Add any others the paper's own discussion or limitations section states. A caveat the
authors raise themselves is the most citable kind.

## Mechanisms with no candidate node

List every mechanism the paper establishes that none of the candidate nodes above
covers. For each: what the mechanism is, the quote establishing it, and what kind of
node would be needed to hold it. This list is the input to a knowledge-base gap
issue, so a mechanism omitted here is one that gets lost.

## Output

A structured report with:

1. One section per biological system, each containing its pairing rows as specified
   above, its registry-record fields, and a short "does not model" subsection.
2. A consolidated table of every pairing: system → node → relationship → fidelity →
   model_scale → readout direction → quote.
3. The mechanisms-with-no-node list.
4. An overall statement of which systems support a mechanism link and which do not,
   with the reason for each that does not.

Every factual claim carries a PMID or DOI and a verbatim quote.

**Provider:** openscientist
**Generated:** 2026-11-19T16:41:37.853894

1. PMID:37418196
2. PMID:18408071
3. PMID:26405827
4. PMID:25659897
5. PMID:25462015
6. PMID:9309991
7. PMID:40946659