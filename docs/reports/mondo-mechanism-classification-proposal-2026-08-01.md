# Ten Proposed Mechanism-Based Classification Nodes for MONDO, Derived from dismech

**Date:** 2026-08-01
**Status:** Proposal for MONDO review — no MONDO edits made
**Source KB:** dismech (`kb/modules/`, `kb/disorders/`, `kb/groupings/`)
**MONDO snapshot:** local OAK `sqlite:obo:mondo`, fetched 2026-08-01 — 31,886
labelled `MONDO:` classes, 3,968 deprecated. See §6 for the fingerprint check and
reproduction commands; re-verify before filing any new-term request.

---

## 1. Why there is room for this

MONDO already carries a dedicated mechanism axis, `MONDO:7770011 disease by molecular
mechanism`. It is the branch that holds exactly the kind of class the user of a
mechanism-based nosology reaches for — "ciliopathy", "RASopathy".

That branch currently has **five children**:

| MONDO ID | Label |
|---|---|
| `MONDO:0005308` | ciliopathy |
| `MONDO:0021060` | RASopathy |
| `MONDO:0019119` | muscular channelopathy |
| `MONDO:0021179` | proteostasis deficiencies |
| `MONDO:0005574` | tauopathy |

Five nodes is a very thin axis for ~25,000 disease classes. The gap is not that MONDO
lacks mechanism knowledge — 240 MONDO terms carry a
`RO:0004021 basis_in_disruption_of_process` axiom — but that almost all of those
axioms sit on **single diseases or single enzymes** (`Fabry disease` →
`GO:0004557 alpha-galactosidase activity`) or on very broad metabolic-process
containers (`amino acid metabolism disease` → `GO:0006520`). The intermediate
tier — the "this is one recognisable mechanistic family of ~10–30 diseases that
clinicians and researchers name and study as a unit" tier that ciliopathy and
RASopathy occupy — is nearly empty.

dismech is a good source for filling it because its `kb/modules/` layer was built
for precisely this purpose: 118 conserved mechanism modules, each a curated
trigger→consequence pathophysiology chain with evidence, and each with disorder
entries that declare `conforms_to: <module>#<node>`. A module with many
independent conformers is direct evidence that the mechanism is a real
cross-disease family rather than a one-off.

### Two structural precedents this proposal leans on

- **RASopathy** is logically defined:
  `MONDO:0000001 and (RO:0004021 some GO:0007265)`, with the
  `MONDO:patterns/basis_in_disruption_of_process` design pattern generating the
  synonym `disorder of Ras protein signal transduction`. **Seven** of the ten
  proposals below can be minted the same way (#2, #3, #4, #5, #6, #7, #9), and
  each cites a **verified GO term**. The remaining three (#1, #8, #10)
  deliberately propose no `RO:0004021` axiom — see the next bullet and their
  individual entries.
- **proteostasis deficiencies** (`MONDO:0021179`) carries *no* `RO:0004021`
  axiom — it is a textual grouping with asserted children. That is the precedent
  for proposal #1, whose mechanism (toxic-metabolite accumulation under catabolic
  stress) is a convergence pattern rather than one GO process, and for proposal #8.

### `RO:0004021` is direction-agnostic — read the axioms as necessary conditions

This constrains every logical definition below and is stated once here rather
than repeated ten times. `RO:0004021 basis_in_disruption_of_process` says the
disease has its basis in a *disruption of* the named process; it does not encode
**which direction** the process is perturbed. A proposed axiom therefore cannot
distinguish gain from loss of function, and will admit disorders that perturb the
same process the opposite way from the textual definition:

- **#7 (`GO:0007224` smoothened signaling pathway)** — the textual definition says
  "constitutive activation", but the loss-of-signaling disorders satisfy the axiom
  equally. This KB already contains such counterexamples annotated with
  `GO:0007224`: `Holoprosencephaly_12_With_or_Without_Pancreatic_Agenesis`,
  `Brachydactyly_Type_A1`, and `Smith-Lemli-Opitz_syndrome`.
- **#3 (`GO:0008543` FGFR signaling pathway)** — the definition says
  "constitutively active or ligand-hypersensitive", but FGFR *loss*-of-function
  disease (`Kallmann_Syndrome`, FGFR1 LOF) satisfies the axiom.
- **#9 (`GO:0016236` macroautophagy)** — §3.9's own gap evidence notes that
  MONDO's existing `autophag*` terms describe *excessive* autophagy; those satisfy
  the axiom too.

**Consequence for the new-term requests:** either write the textual definitions
direction-neutrally, or state explicitly in each NTR that the `RO:0004021` axiom
is a **necessary condition only** and that directionality is carried by the
textual definition. Do not present these axioms as equivalence axioms. Where MONDO
wants direction encoded, a `positive/negative regulation of ...` GO child (e.g.
`GO:0045879 negative regulation of smoothened signaling pathway`, already used by
the dismech module) is the better anchor.

---

## 2. How candidates were selected and filtered

**Sourcing.** Primary source was `kb/modules/`, ranked by the number of *distinct
disorder files* declaring `conforms_to` against the module (not raw node counts,
which overcount multi-node conformers). Cross-disorder pathophysiology patterns
without a module were also considered; none displaced a module-backed candidate.

**MONDO exclusion filter** (as agreed: *exclude only on an exact or near-synonym
match; a partial/phenotype-based/anatomy-based MONDO grouping does not disqualify,
but must be disclosed*). Each candidate was tested three ways against the MONDO
snapshot:

1. **Label match** — all `rdfs:label` values.
2. **Synonym match** — all exact/related/broad/narrow synonyms.
3. **Definition-text match** — all `IAO:0000115` definitions, to catch classes
   whose label hides the mechanism.

All ten proposals returned **zero hits on all three passes** for their mechanism
phrase. The searches that *did* hit are reported per-node under "MONDO gap
evidence", because those adjacent classes are what a MONDO curator will need to
reconcile against.

**Candidates excluded by the filter** (recorded so the work isn't repeated). The
**Conformers** column is distinct-file counts, the same metric used in §3 and §4;
the node-occurrence count is shown alongside because the two differ substantially
and an earlier draft of this table mistakenly reported nodes:

| dismech module | Conformers (files) | (nodes) | Excluded because MONDO already has |
|---|---|---|---|
| `lysosomal_substrate_accumulation` | 44 | 85 | `lysosomal storage disease` |
| `ciliopathy_dysfunction` | 28 | 68 | `MONDO:0005308 ciliopathy` |
| `complex_iv_assembly_deficiency` | 23 | 61 | `mitochondrial complex IV deficiency` |
| `congenital_disorder_of_glycosylation` | 11 | 26 | `MONDO:0017740` / CDG classes |
| `microtubule_dependent_neuronal_migration_failure` | 9 | 22 | `MONDO:0100153 tubulinopathy` |
| `amyloidogenesis` | 5 | 39 | `MONDO:0019065 amyloidosis` (under proteostasis deficiencies) |
| `heme_biosynthesis_porphyria` | 3 | 10 | `porphyria` |
| `cranial_suture_premature_fusion` | 2 | 5 | `craniosynostosis` |
| `renal_cystogenesis` | 2 | 7 | `cystic kidney disease` |
| `drug_hypersensitivity_scar` | 2 | 9 | `MONDO:0005594 severe cutaneous adverse reaction` |
| `granuloma_formation` | 2 | 7 | `granulomatous disease` classes |
| `er_protein_storage_disease` | 1 | 1 | `MONDO:0027749 serpinopathy` |

Note that on the corrected metric several excluded modules are **smaller** than
the proposals in §3 — `amyloidogenesis` has 5 conforming files, fewer than seven
of the ten proposals. This does not change any exclusion: every row above was
excluded because MONDO already carries an equivalent class, never because of its
size. Size is used only to *rank* the surviving candidates.

---

## 3. The ten proposed nodes

Ranked by strength of dismech backing. Each entry gives a proposed label,
definition, logical definition, parentage, the mechanism rationale, the candidate
member set, and the MONDO gap evidence.

---

### 3.1 Intoxication-type inborn error of metabolism

- **Proposed label:** `intoxication-type inborn error of metabolism`
- **Synonyms:** intoxication-type inborn error of intermediary metabolism; intoxication-type metabolic disease; toxic-metabolite accumulation disorder
- **Proposed parents:** `MONDO:7770011 disease by molecular mechanism`; `MONDO:0019052 inborn errors of metabolism`
- **Logical definition:** *none proposed* — follow the `MONDO:0021179 proteostasis deficiencies` precedent of a textually-defined grouping with asserted children. No single GO process captures "toxic metabolite accumulates behind an enzymatic block and is unmasked by catabolic stress"; forcing `GO:0006082 organic acid metabolic process` would both over- and under-generate.

**Definition.** An inborn error of intermediary metabolism in which a deficient
enzyme or transporter causes accumulation of an upstream toxic metabolite and/or
an energy deficit that is clinically silent at baseline and is unmasked by
catabolic stress (intercurrent illness, fasting, surgery, or a protein load),
precipitating acute metabolic decompensation — metabolic acidosis, hyperammonemia,
and/or hypoglycemia — and consequent acute encephalopathy and multiorgan crisis.

**Why this is a genuine mechanism class.** The clinically decisive division in
metabolic medicine is not *which substrate* accumulates but *how the disease
behaves*: whether it presents as an acute, potentially reversible crisis requiring
emergency protocols (stop protein, reverse catabolism with glucose, scavenge
ammonia, dialyse). MONDO currently scatters these disorders across `urea cycle
disorder`, `classic organic aciduria`, `disorder of fatty acid oxidation and
ketogenesis`, and amino-acid disorders — a substrate partition that cross-cuts the
behavioural one, so no MONDO query can currently return "the disorders that
decompensate acutely."

**Naming caveat — do not label this "Saudubray group 1" without narrowing it.**
An earlier draft leaned on the Saudubray classification, which is the standard
reference for this axis. That attribution is only partly accurate for the member
list as curated: Saudubray places fatty-acid-oxidation and ketogenesis defects in
the **energy-deficiency** group, not the intoxication group, yet `MONDO:0015515`
(CPT II) and `MONDO:0011614` (HMG-CoA synthase) are listed below; and
`MONDO:0018820` (TANGO2) fits neither classical group. Two honest options for the
NTR, and MONDO should pick one explicitly:

1. **Keep the broader membership and use a behaviour-based label** — e.g. *acute
   metabolic decompensation disorder* — dropping the claim of strict Saudubray
   equivalence. This is the option the member list below actually supports, and is
   the one recommended here.
2. **Keep the "intoxication-type" label** and drop the FAO/ketogenesis members
   plus TANGO2, aligning the class strictly with Saudubray group 1.

The dismech grouping `kb/groupings/Intoxication-Type_Inborn_Errors_of_Metabolism.yaml`
(added in this PR) has **already adopted option 1**: its `display_name` reads
"(Acute Metabolic Decompensation)" rather than claiming Saudubray group 1
equivalence, and its `grouping_rationale` names the three members
(`MONDO:0015515` CPT II, `MONDO:0011614` HMG-CoA synthase, `MONDO:0018820` TANGO2)
that would have to be reconsidered if option 2 is ever preferred instead. The
MONDO label proposed above should be decided the same way.

**dismech provenance.** `kb/modules/metabolic_intoxication_decompensation.yaml` —
node chain: Enzymatic Block in Intermediary Metabolism → Toxic Metabolite
Accumulation and Energy Deficit → Acute Metabolic Decompensation → Acute Metabolic
Encephalopathy → Neurological Injury and Multiorgan Crisis. **19 conforming
disorder entries** — the largest non-excluded module in the KB. Backing dismech
grouping: `Intoxication-Type_Inborn_Errors_of_Metabolism` (added in this PR;
19 members, `NECESSARY`, `skos:broadMatch` → `MONDO:0019052`).

**Candidate MONDO members (19).**
`MONDO:0009520` 3-hydroxy-3-methylglutaric aciduria ·
`MONDO:0011614` 3-hydroxy-3-methylglutaryl-CoA synthase deficiency ·
`MONDO:0018950` 3-methylcrotonyl-CoA carboxylase deficiency ·
`MONDO:0009610` 3-methylglutaconic aciduria type 1 ·
`MONDO:0008814` arginase deficiency ·
`MONDO:0008815` argininosuccinic aciduria ·
`MONDO:0008760` beta-ketothiolase deficiency ·
`MONDO:0009376` carbamoyl phosphate synthetase I deficiency ·
`MONDO:0014332` hyperammonemic encephalopathy due to carbonic anhydrase VA deficiency ·
`MONDO:0015515` carnitine palmitoyltransferase II deficiency ·
`MONDO:0016602` citrin deficiency ·
`MONDO:0008988` citrullinemia type I ·
`MONDO:0009666` holocarboxylase synthetase deficiency ·
`MONDO:0009475` isovaleric acidemia ·
`MONDO:0009109` lysinuric protein intolerance ·
`MONDO:0009563` maple syrup urine disease ·
`MONDO:0002012` methylmalonic acidemia ·
`MONDO:0010703` ornithine carbamoyltransferase deficiency ·
`MONDO:0018820` recurrent metabolic encephalomyopathic crises-rhabdomyolysis (TANGO2)

Note for curators: `MONDO:0018820` (TANGO2) appears in **both** this proposal and
#2 (cardiac channelopathy) — it causes metabolic crises *and* a
QT-prolonging ventricular arrhythmia. That is biologically correct and an argument
for multi-parenting rather than a conflict, exactly as flagged for
`MONDO:0008222` Andersen-Tawil syndrome in §3.2.

**MONDO gap evidence.** `"intoxication"` matches 24 MONDO terms — *all* are
exogenous poisoning (lead, cocaine, botulinum toxin, ackee fruit, digitalis); none
is an inborn error. `"metabolic decompensation"` and `"metabolic crisis"`: 0 hits.
`"toxic metabolite"` in definition text: 0 hits. Substrate-partitioned neighbours
that would become *siblings*, not parents: `MONDO:0004739` urea cycle disorder,
`MONDO:0019215` classic organic aciduria, `MONDO:0017713` disorder of fatty acid
oxidation and ketogenesis.

---

### 3.2 Cardiac channelopathy

- **Proposed label:** `cardiac channelopathy`
- **Synonyms:** inherited arrhythmia syndrome; cardiac ion channelopathy; disorder of cardiac muscle cell action potential
- **Proposed parents:** `MONDO:7770011 disease by molecular mechanism`; `MONDO:0005267 heart disorder`
- **Logical definition:** `MONDO:0000001 and (RO:0004021 some GO:0086001)`
  — *`GO:0086001 cardiac muscle cell action potential`* ✅ verified. (`GO:0086009 membrane repolarization` ✅ is the alternative if a repolarization-specific axiom is preferred; `GO:0086001` is recommended because it also admits the depolarization/pacemaker branch.)

**Definition.** A disease caused by disturbed function of ion channels or
calcium-handling proteins of the cardiomyocyte, altering the cardiac action
potential and/or intracellular calcium handling, producing an arrhythmogenic
substrate and triggered activity in a structurally normal heart.

**Why this is a genuine mechanism class — and the strongest structural argument
in this document.** MONDO's generic `channelopathy` class, `MONDO:0021016`, is
**obsolete**. What survived obsoletion is `MONDO:0019119 muscular channelopathy`,
which sits directly under `disease by molecular mechanism` with 12 children and
its own per-ion-species subclasses (sodium/chloride/calcium/potassium). So MONDO
has already accepted the modelling pattern "channelopathy of *tissue X*" as a
mechanism-axis class — it just never minted the cardiac sibling, even though the
cardiac channelopathies are, if anything, the better-known half of the field.
This proposal is a direct structural completion, not a novel construct.

**dismech provenance.** `kb/modules/cardiac_ion_channel_repolarization.yaml` —
Cardiac Ion-Channel or Calcium-Handling Variant → Altered Action Potential and
Calcium Handling → Arrhythmogenic Substrate and Triggered Activity → Ventricular
Tachyarrhythmia → Syncope and Sudden Cardiac Death, with a parallel Sinoatrial
Node Pacemaker Dysfunction branch. **12 conforming disorder entries.** dismech
also carries the `Inherited_Arrhythmia_Syndromes` grouping with
`NECESSARY_AND_SUFFICIENT` membership criteria — i.e. this class already has a
machine-checkable boolean definition on the dismech side.

**Candidate MONDO members (12).**
`MONDO:0008222` Andersen-Tawil syndrome · `MONDO:0015263` Brugada syndrome ·
`MONDO:0018054` familial atrial fibrillation · `MONDO:0012061` familial sick sinus
syndrome · `MONDO:0019171` familial long QT syndrome · `MONDO:0100234` paroxysmal
familial ventricular fibrillation · `MONDO:0017990` catecholaminergic polymorphic
ventricular tachycardia · `MONDO:0000453` short QT syndrome · `MONDO:0013960`
sinoatrial node dysfunction and deafness · `MONDO:0010979` Timothy syndrome ·
`MONDO:0013317` torsade-de-pointes syndrome with short coupling interval ·
`MONDO:0018820` TANGO2 deficiency disorder

**MONDO gap evidence.** `"cardiac channelopathy"` across labels + synonyms: **0
hits**. `"cardiac action potential"` in definition text: 0 hits. `"repolarization"`
in definition text: 3 hits, all individual diseases (`MONDO:0100234`,
`MONDO:0005478` torsades de pointes, and a rabbit model), no grouping.
Note for curators: `MONDO:0008222` Andersen-Tawil syndrome is currently a child of
`muscular channelopathy` — it is genuinely both, and should become multi-parented
rather than moved.

---

### 3.3 FGFR-opathy

- **Proposed label:** `FGFR-opathy`
- **Synonyms:** FGFR-related disorder; fibroblast growth factor receptor signaling disease; disorder of fibroblast growth factor receptor signal transduction
- **Proposed parents:** `MONDO:7770011 disease by molecular mechanism`; `MONDO:0003847 hereditary disease`
- **Logical definition:** `MONDO:0000001 and (RO:0004021 some GO:0008543)`
  — *`GO:0008543 fibroblast growth factor receptor signaling pathway`* ✅ verified.

**Definition.** A hereditary disease caused by a germline variant in a fibroblast
growth factor receptor gene (most often *FGFR3*, less often *FGFR2* or *FGFR1*)
that produces a constitutively active or ligand-hypersensitive receptor, with
sustained downstream MAPK/ERK and STAT signaling acting on growth-plate
chondrocytes and cranial suture osteogenic fronts.

**Why this is a genuine mechanism class.** This is the closest available analogue
to RASopathy anywhere in the ontology and the most obviously missing sibling: a
named receptor-tyrosine-kinase signaling family, with a shared gain-of-function
direction, a shared downstream cascade (which is *literally the RAS-MAPK cascade*
that RASopathy is defined on), a coherent two-compartment skeletal phenotype, and
a shared therapeutic *strategy* — FGFR-pathway antagonism. That payoff should be
stated carefully: the CNP/NPR2 analogue vosoritide is approved for achondroplasia
only, and its extension to hypochondroplasia and the craniosynostosis members is
under investigation rather than established. The class-level claim is that these
disorders share a druggable node, not that any one drug is approved across them.
MONDO currently has ~30 `FGFR*-related` per-gene terms and no class over them.

*Why not a child of RASopathy?* The shared downstream cascade invites the
question. The answer is ontological: `GO:0008543` (FGFR signaling pathway) is not
a subclass of `GO:0007265` (Ras protein signal transduction) in GO, so the axioms
do not subsume, and the two classes are distinguished by the *lesion* (receptor
tyrosine kinase vs. RAS-pathway component) rather than by the shared effector arm.
They should be siblings on the mechanism axis, not parent and child.

**dismech provenance.** `kb/modules/fgfr_gain_of_function_skeletal_dysplasia.yaml`
— Constitutive FGFR Activation → Sustained MAPK/STAT Signaling → {Growth-Plate
Chondrocyte Dysregulation, Cranial Suture Osteogenic Acceleration} → {Impaired
Endochondral Ossification, Premature Suture Fusion}, plus a CNP-NPR2
counter-regulation/therapy node. **11 conforming disorder entries.** dismech also
carries the `FGFR_Related_Skeletal_Dysplasias` grouping.

**Candidate MONDO members (11).**
`MONDO:0007037` achondroplasia · `MONDO:0007041` Apert syndrome · `MONDO:0007405`
Crouzon syndrome · `MONDO:0012833` Crouzon syndrome-acanthosis nigricans syndrome ·
`MONDO:0007793` hypochondroplasia · `MONDO:0007400` Jackson-Weiss syndrome ·
`MONDO:0011274` Muenke syndrome · `MONDO:0007043` Pfeiffer syndrome ·
`MONDO:0014658` SADDAN · `MONDO:0008546` thanatophoric dysplasia type 1 ·
`MONDO:0008547` thanatophoric dysplasia type 2

**MONDO gap evidence.** `"FGFR"` matches 30 terms — all per-gene or per-disease
(`FGFR3-related chondrodysplasia`, `FGFR1-related Pfeiffer syndrome`,
`FGFR2-related bent bone dysplasia`), no cross-gene grouping. `"fibroblast growth
factor receptor"` in definition text: 1 hit (`MONDO:0014658` SADDAN), a single
disease. Adjacent but non-blocking: `MONDO:0019685 FGFR3-related chondrodysplasia`
is gene-scoped and would become a child.

---

### 3.4 Synaptic vesicle cycle disorder

- **Proposed label:** `synaptic vesicle cycle disorder`
- **Synonyms:** presynaptic vesicle cycle disease; SV-opathy; disorder of the synaptic vesicle cycle
- **Proposed parents:** `MONDO:0021017 synaptopathy`; `MONDO:7770011 disease by molecular mechanism`
- **Logical definition:** `MONDO:0000001 and (RO:0004021 some GO:0099504)`
  — *`GO:0099504 synaptic vesicle cycle`* ✅ verified.

**Definition.** A synaptopathy caused by deficiency of a protein of the presynaptic
synaptic vesicle cycle, disrupting vesicle docking and priming, calcium-triggered
SNARE-mediated fusion, or vesicle endocytosis and recycling, and producing
neurotransmitter release failure.

**Why this is a genuine mechanism class.** This is the single most productive
gene-discovery family in developmental and epileptic encephalopathy of the last
decade — *STXBP1*, *SNAP25*, *STX1B*, *SYT1*, *VAMP2*, *DNM1*, *UNC13A*, *SYN1*,
*CPLX1* are curated, reviewed, and increasingly *treated* as one group, because
they converge on one biochemical cycle with step-resolved lesions
(docking/priming vs. fusion vs. endocytosis). MONDO scatters every one of them
into numbered `developmental and epileptic encephalopathy, N` classes where the
shared presynaptic mechanism is completely invisible.

**Relationship to existing MONDO coverage — disclosed.** MONDO *does* have
`MONDO:0021017 synaptopathy` ("a disease caused by dysfunction of synapses").
That term is far broader — it spans pre- and post-synaptic, central and
neuromuscular — and currently has exactly **one** child,
`MONDO:0020124 neuromuscular junction disease`. This proposal is a **child of it**,
not a competitor, and would be its first central-synapse subclass. This passes the
agreed filter (no exact/near-synonym), but the parentage should be explicit.

**dismech provenance.** `kb/modules/synaptic_vesicle_cycle.yaml` — Synaptic Vesicle
Cycle Protein Deficiency → {Impaired Docking and Priming, Impaired Ca²⁺-Triggered
SNARE-Mediated Fusion, Impaired Endocytosis and Recycling} → Neurotransmitter
Release Failure. **9 conforming disorder entries.** dismech also carries the
`Synaptic_Vesicle_Cycle_Disorders` grouping.

**Candidate MONDO members (9).**
`MONDO:0012812` developmental and epileptic encephalopathy 4 (*STXBP1*) ·
`MONDO:0014598` DEE 31A (*DNM1*) · `MONDO:0033372` DEE 63 (*CPLX1*) ·
`MONDO:0032678` DEE 71 (*SNAP25*) · `MONDO:0014517` generalized epilepsy with
febrile seizures plus type 9 (*STX1B*) · `MONDO:0010339` epilepsy X-linked 1
(*SYN1*) · `MONDO:0033864` infantile hypotonia-oculomotor anomalies-hyperkinetic
movements (*SYT1*, Baker-Gordon) · `MONDO:0980940` NDD with hypotonia and epilepsy
(*UNC13A*) · `MONDO:0032900` NDD with hypotonia and autistic features (*VAMP2*)

**MONDO gap evidence.** `"synaptic vesicle"` across labels + synonyms: **0 hits**;
in definition text: **0 hits**. `"synaptopathy"` returns only `MONDO:0021017` and
two *DLG4* synonyms (a postsynaptic scaffold gene — different arm).

---

### 3.5 Centrosomopathy

- **Proposed label:** `centrosomopathy`
- **Synonyms:** centrosome-spindle disorder; disorder of centrosome cycle; mitotic spindle disorder
- **Proposed parents:** `MONDO:7770011 disease by molecular mechanism`; `MONDO:0003847 hereditary disease`
- **Logical definition:** `MONDO:0000001 and (RO:0004021 some GO:0007098)`
  — *`GO:0007098 centrosome cycle`* ✅ verified. (Alternatives, both ✅ verified, if the
  intended scope is spindle-centric or centriole-centric: `GO:0051225 spindle assembly`,
  `GO:0007099 centriole replication`.)

**Definition.** A hereditary disease caused by dysfunction of the centrosome,
centriole, or mitotic spindle apparatus, in which perturbed progenitor cell
division alters the balance of proliferative versus differentiative divisions and
distorts the progenitor pool — most prominently in cortical neurogenesis,
producing primary microcephaly, microlissencephaly, and simplified gyration, and
in some members a systemic growth defect (primordial dwarfism).

**Why this is a genuine mechanism class.** "Centrosomopathy" is standard,
long-established usage in the developmental neurogenetics literature for the
*MCPH*/*MOPD* gene families (*ASPM*, *WDR62*, *CENPJ*, *CEP152*, *PCNT*, *NDE1*,
*KATNB1*). It is also the natural structural sibling of two classes MONDO
*already* has: `ciliopathy` (basal body — the centriole in its non-mitotic role)
and `tubulinopathy` (the microtubule polymer). MONDO has the organelle-in-cilium
class and the polymer class but not the organelle-in-mitosis class, which is what
leaves *ASPM*-type primary microcephaly with no mechanistic home.

**dismech provenance.**
`kb/modules/neural_progenitor_centrosome_spindle_dysfunction.yaml` — Centrosome and
Mitotic Spindle Perturbation → Abnormal Progenitor Division and Fate Choice →
Progenitor Pool Distortion → Abnormal Cortical Neuron Output and Gyration, with
programmed-cell-death and viral-cytopathy branches. **8 conforming disorder
entries.** Backing dismech grouping: `Centrosomopathies` (added in this PR;
8 members, `NECESSARY`, no MONDO mapping because no equivalent term exists).
Related but phenotype-scoped groupings: `Primary_Microcephaly_Spectrum`,
`Lissencephaly_and_Neuronal_Migration_Disorders`.

**Candidate MONDO members (5 mapped of 8 dismech conformers).**
`MONDO:0016660` autosomal recessive primary microcephaly · `MONDO:0018838`
lissencephaly spectrum disorders · `MONDO:0008872` microcephalic osteodysplastic
primordial dwarfism type II · `MONDO:0013785` intellectual disability, autosomal
recessive 34 (*CRADD*) · `MONDO:0020491` subcortical band heterotopia (*EML1*).
Three dismech conformers — `NDE1-related_Microcephaly_Lissencephaly`,
`KATNB1-related_Cortical_Malformation`, `TUBB/TUBB5-related_Microcephaly` — carry
no `disease_term`; these are candidate MONDO **new-term** requests in their own
right, flagged separately below (§5).

**MONDO gap evidence.** `"centrosomopath"`, `"centriolopath"`, `"centriole"`,
`"pericentriolar"`, `"centrosome amplification"`: **0 hits** across labels and
synonyms. `"centrosome"` and `"spindle assembly"` in definition text: **0 hits**.
All 95 `"spindle"` label hits are spindle-*cell* neoplasms — a homonym, not a
conflict.

---

### 3.6 Meiotic recombination failure disorder

- **Proposed label:** `meiotic recombination failure disorder`
- **Synonyms:** meiotic prophase I failure; synaptonemal complex disorder; disorder of meiotic recombination
- **Proposed parents:** `MONDO:7770011 disease by molecular mechanism`; `MONDO:0005039 reproductive system disorder` (or `MONDO:0005047 infertility disorder`)
- **Logical definition:** `MONDO:0000001 and (RO:0004021 some GO:0007131)`
  — *`GO:0007131 reciprocal meiotic recombination`* ✅ verified.
  (`GO:0007130 synaptonemal complex assembly` ✅ verified, for a synapsis-scoped
  variant if MONDO prefers to split the two.)

**Definition.** A disease caused by disruption of meiotic prophase I chromosome
synapsis or homologous recombination in germ cells, producing pachytene-checkpoint
arrest and germ-cell apoptosis, and manifesting sex-dimorphically as ovarian
follicle depletion with primary ovarian insufficiency in 46,XX individuals and
spermatogenic arrest with non-obstructive azoospermia in 46,XY individuals.

**Why this is a genuine mechanism class.** This class has an unusual and
compelling property: **one mechanism, two clinical presentations that current
nosology files in different places entirely.** The same *STAG3*, *SYCE1*, *HFM1*,
*MCM8/9*, *HROB* lesion causes "premature ovarian failure N" in one sex and
"spermatogenic failure N" in the other, and MONDO's numbered series place these in
unrelated branches. A mechanism node is the only way to state that they are one
disease family. Several members additionally carry a somatic DNA-repair deficiency
with cancer predisposition (*MCM8/MCM9*), which the mechanism node explains and
the phenotype-based classes cannot.

**dismech provenance.** `kb/modules/meiotic_prophase_failure.yaml` — Meiotic
Prophase I Entry and Homolog Pairing → Synaptonemal Complex Assembly → Homologous
Recombination Repair of Meiotic DNA Breaks → Pachytene Checkpoint Arrest and Germ
Cell Apoptosis → {Ovarian Follicle Depletion/POI, Spermatogenic Arrest/NOA}, plus a
Somatic DNA Repair Deficiency and Cancer Predisposition branch. **7 conforming
disorder entries.** dismech also carries the `Meiotic_Gametogenic_Failure` grouping.

**Candidate MONDO members (6 mapped of 7).**
`MONDO:0014322` premature ovarian failure 9 (*HFM1*) · `MONDO:0971176` ovarian
dysgenesis 11 (*HROB*) · `MONDO:0044776` premature ovarian failure 10 (*MCM8*) ·
`MONDO:0014321` premature ovarian failure 8 (*STAG3*) · `MONDO:1060214`
SYCE1-related gametogenic failure · `MONDO:0010052` spermatogenic failure 4
(*SYCP3*). (`MCM9-related gametogenic failure` unmapped in dismech.)

**MONDO gap evidence.** `"meiotic recombination"`, `"synaptonemal"`: **0 hits**
across labels, synonyms, and definitions. `"meiotic"`/`"meiosis"`: 1 hit,
`MONDO:0044626 female infertility due to oocyte meiotic arrest` — a single
sex-specific disease with an `RO:0004021 GO:0051321 meiotic cell cycle` axiom,
which would become a child.

---

### 3.7 Hedgehog pathway activation disease

- **Proposed label:** `Hedgehog pathway activation disease`
- **Synonyms:** Hedgehog-driven neoplasm; disorder of constitutive smoothened signaling; Hedgehog pathway signaling disease
- **Proposed parents:** `MONDO:7770011 disease by molecular mechanism`
- **Logical definition:** `MONDO:0000001 and (RO:0004021 some GO:0007224)`
  — *`GO:0007224 smoothened signaling pathway`* ✅ verified.
  Per §1's necessary-condition caveat, this axiom is **direction-agnostic** and so
  does not by itself exclude the loss-of-signaling disorders
  (`Greig_Cephalopolysyndactyly`, `Pallister-Hall_Syndrome`, the
  `Holoprosencephaly_9/12` entries, `Smith-Lemli-Opitz_syndrome`); the activation
  direction is asserted textually. If MONDO prefers the direction encoded in the
  axiom, `GO:0045879 negative regulation of smoothened signaling pathway` — already
  used by the dismech module — is the better anchor. The label is deliberately
  narrowed to `activation` to match the backing dismech grouping
  `Hedgehog_Pathway_Activation_Disorders`, which scopes loss-of-signaling out.

**Definition.** A disease caused by ligand-independent constitutive activation of
the Hedgehog signaling pathway, arising either from loss of function of a negative
regulator (*PTCH1*, *PTCH2*, *SUFU*) or gain of function of the positive
transducer *SMO*, converging on constitutive GLI transcriptional output and
Hedgehog-dependent proliferation.

**Why this is a genuine mechanism class.** Like RASopathy, this is a named
developmental signaling pathway whose disorders are recognised as a unit — and
here the therapeutic argument is decisive: the SMO inhibitors vismodegib and
sonidegib are approved *on the basis of pathway membership*, and *SUFU*-mutant
tumours are known to be intrinsically resistant because the lesion is downstream
of the drug target. That distinction is a pure mechanism-graph fact and is
unrepresentable in a phenotype- or histology-based classification. The class also
usefully unifies germline (Gorlin) and somatic (sporadic BCC, SHH-medulloblastoma)
disease.

**dismech provenance.** `kb/modules/hedgehog_pathway_activation.yaml` — Loss of
Hedgehog Pathway Negative Regulation → Constitutive Smoothened Activity →
Constitutive GLI Transcriptional Output → Hedgehog-Driven Proliferation and
Tumorigenesis. **5 conforming disorder entries.** Backing dismech grouping:
`Hedgehog_Pathway_Activation_Disorders` (added in this PR; 5 members,
`NECESSARY_AND_SUFFICIENT` — the only N&S class of the four, since the defining
lesion is a discrete molecular state — no MONDO mapping because no equivalent term
exists). Note the 5 members are 3 disease-level entities: `Gorlin Syndrome` plus
its own `PTCH1-` and `SUFU-related` molecular subdivisions, which the grouping's
own member `notes` concede are not independent diseases.

**Candidate MONDO members (5).**
`MONDO:0007187` nevoid basal cell carcinoma syndrome (Gorlin) · `MONDO:0958174`
basal cell nevus syndrome 1 (*PTCH1*) · `MONDO:0958189` basal cell nevus syndrome 2
(*SUFU*) · `MONDO:0005341` skin basal cell carcinoma · `MONDO:0850197`
medulloblastoma SHH activated.
Strong further candidates not yet in dismech: rhabdomyosarcoma subsets, Curry-Jones
syndrome (*SMO* mosaic), and — as a *loss*-of-signaling counterpart worth
considering for a sibling node rather than this one — holoprosencephaly.

**MONDO gap evidence.** `"hedgehog"` across labels + synonyms: 2 hits, both
veterinary (`ataxia, middle-African hedgehog`; `cardiomyopathy, hedgehogs`) — the
animal, not the pathway. `"smoothened"`, `"sonic hedgehog"`, `"GLI3"`: **0 hits**.
`"hedgehog signaling"` and `"smoothened"` in definition text: **0 hits**.

---

### 3.8 Polyglutamine expansion disease

- **Proposed label:** `polyglutamine expansion disease`
- **Synonyms:** polyQ disease; polyglutamine disorder; translated CAG repeat expansion disease
- **Proposed parents:** `MONDO:0021179 proteostasis deficiencies`; `MONDO:0005559 neurodegenerative disease`
- **Logical definition:** *none proposed via `RO:0004021`* — the defining feature is a
  variant class (a translated CAG/polyQ tract expansion conferring a dominant toxic
  gain of function), not a disrupted GO process. Recommend a textual grouping in the
  `proteostasis deficiencies` style, or a `has_material_basis_in` pattern if MONDO
  wishes to model repeat-expansion variant classes generally.

**Definition.** An autosomal dominant neurodegenerative disease caused by
expansion of a translated CAG trinucleotide repeat encoding an elongated
polyglutamine tract, which confers a dominant toxic gain of function on the host
protein — misfolding and aggregation with neuronal intranuclear inclusions,
sequestration of transcriptional co-activators, overload of ubiquitin-proteasome
and autophagic clearance, and mitochondrial bioenergetic impairment — producing
region-specific selective neuronal loss.

**Why this is a genuine mechanism class.** "The polyglutamine diseases" is one of
the most firmly established mechanism-based groupings in all of neurology — nine
diseases (HD, DRPLA, SBMA, SCA1/2/3/6/7/17) taught, reviewed, and drug-screened as
one family, with a shared repeat-length/age-of-onset relationship and shared
anticipation. MONDO has **no term for it and no term for repeat expansion at all**.
Notably, MONDO already accepted the two structurally identical siblings —
`MONDO:0000510 synucleinopathy` and `MONDO:0700038 TDP-43 proteinopathy`, both
"aggregating protein defines the class" nodes under `proteostasis deficiencies` —
so the modelling precedent is exact.

**dismech provenance.** `kb/modules/polyglutamine_expansion_proteotoxicity.yaml` —
Translated CAG/PolyQ Repeat Expansion → Misfolded PolyQ Protein Aggregation →
{Transcriptional Dysregulation, Proteostasis Network Overload, Mitochondrial and
Bioenergetic Dysfunction} → Selective Neuronal Dysfunction and Loss. **4 conforming
disorder entries**, plus the `Polyglutamine_Disorders` grouping
(`grouping_basis: SHARED_MECHANISM`).

**Candidate MONDO members (4 in dismech; the class is larger).**
`MONDO:0007739` Huntington disease · `MONDO:0007182` Machado-Joseph disease
(SCA3) · `MONDO:0011781` spinocerebellar ataxia type 17 · `MONDO:0007435`
dentatorubral-pallidoluysian atrophy.
Established members not yet curated in dismech that MONDO should include:
SCA1, SCA2, SCA6, SCA7, and spinal-bulbar muscular atrophy (Kennedy disease).

**MONDO gap evidence.** `"polyglutamine"`, `"repeat expansion"`, `"trinucleotide"`,
`"triplet repeat"`: **0 hits** across labels, synonyms, *and* definition text.
`"CAG repeat"` in definitions: **0 hits**. `"proteinopathy"`: 3 hits, all
neighbours (`TDP-43 proteinopathy`, `SQSTM1-related multisystem proteinopathy`,
`proteostasis deficiencies`) — the proposed parent and siblings.

---

### 3.9 Macroautophagy deficiency disorder

- **Proposed label:** `macroautophagy deficiency disorder`
- **Synonyms:** disabled macroautophagy; autophagy deficiency disease; disorder of macroautophagy
- **Proposed parents:** `MONDO:0021179 proteostasis deficiencies`; `MONDO:7770011 disease by molecular mechanism`
- **Logical definition:** `MONDO:0000001 and (RO:0004021 some GO:0016236)`
  — *`GO:0016236 macroautophagy`* ✅ verified. (`GO:0006914 autophagy` ✅ verified, if a
  broader scope including chaperone-mediated autophagy is wanted.)

**Definition.** A disease caused by decline or disruption of the macroautophagy
machinery, impairing lysosomal sequestration and recycling of dysfunctional
organelles and aggregated proteins, with consequent failure of cytoplasmic quality
control and accumulation of cellular damage.

**Why this is a genuine mechanism class.** Macroautophagy is the *clearance* arm of
proteostasis, and `MONDO:0021179 proteostasis deficiencies` explicitly names
"degradation or clearance of misfolded proteins" in its own definition — yet all
four of its current children (synucleinopathy, amyloidosis, TDP-43 proteinopathy,
SQSTM1 multisystem proteinopathy) are *aggregating-substrate* classes. The
machinery side of the parent's own definition has no representative. This node
also gives *VCP*/*SQSTM1* multisystem proteinopathy a mechanistic (rather than
purely substrate-based) home, and is a designated hallmark of aging
(López-Otín et al. 2023), which matters for MONDO's aging-related content.

**Caveat, stated honestly:** at 5 conformers this is the thinnest of the ten on
dismech backing, and its members are common complex diseases (ALS, Parkinson) where
autophagy failure is one contributing mechanism among several rather than *the*
defining lesion. MONDO may prefer to scope the initial class tightly to the
monogenic autophagy-machinery disorders (*EPG5*/Vici syndrome, *WDR45*/BPAN,
*VCP*, *SQSTM1*, *ATG7*) and admit the complex diseases only via
`contributes_to`-style relations rather than `is_a`. That would be a sounder
class, and dismech should follow suit.

**dismech provenance.** `kb/modules/disabled_macroautophagy.yaml` — Autophagy
Machinery Decline → Failure of Cytoplasmic Quality Control → Accumulated Cellular
Damage and Age-Related Disease. **5 conforming disorder entries.** Backing dismech
grouping: `Macroautophagy_Deficiency_Disorders` (added in this PR; 5 members,
`NECESSARY`, `skos:broadMatch` → `MONDO:0021179`, explicitly provisional pending
the scoping decision in the caveat above). Note the 5 members are 4 distinct
diseases — the VCP-MSP / IBMPFD pair is flagged in-file as substantially
overlapping — and, counted at that same disease level, only 2 of the 4 carry no
partial-mechanism caveat (3 of the 5 member entries, before the VCP pair collapses).

**Candidate MONDO members (5 in dismech).**
`MONDO:0008178` / `MONDO:0000507` inclusion body myopathy with Paget disease of
bone and frontotemporal dementia (*VCP*) · `MONDO:0008029` Bethlem myopathy ·
`MONDO:0004976` amyotrophic lateral sclerosis · `MONDO:0005180` Parkinson disease.
Recommended additions per the caveat above: Vici syndrome (*EPG5*), BPAN
(*WDR45*), *ATG7*-related disorder. Conversely, `MONDO:0008029` Bethlem myopathy
is the first member that should **drop** under the tight-scoping recommendation:
it is a COL6 extracellular-matrix defect in which the autophagy block is a
downstream consequence rather than a primary lesion in the machinery. Note also
that `MONDO:0008178` and `MONDO:0000507` are two distinct MONDO classes curated as
two distinct dismech entries, not one entry with two ids.

**MONDO gap evidence.** `"macroautophagy"`, `"autophagy disorder"`: **0 hits**
across labels, synonyms, and definitions. `"autophag"` matches only 3 individual
diseases (X-linked myopathy with excessive autophagy; infantile-onset autophagic
vacuolar myopathy; one obsolete term) — and note these are *excessive* autophagy,
the opposite direction, so they are not even candidate members.

---

### 3.10 BBSome-opathy

- **Proposed label:** `BBSome-opathy`
- **Synonyms:** BBSome complex disorder; BBSome trafficking disorder; disorder of BBSome-dependent ciliary trafficking
- **Proposed parents:** `MONDO:0005308 ciliopathy`
- **Logical definition:** no axiom recommended. (`GO:0032465` — *regulation of
  cytokinesis* — appeared in an earlier draft and is simply wrong for this class;
  it is named here only so the discarded option is not re-proposed.) Prefer a complex-scoped textual definition, or — if GO gains a
  suitable term — a `BBSome-mediated ciliary trafficking` process. GO currently has
  `GO:0034464 BBSome` as a **cellular component** ("a ciliary protein complex
  involved in cilium biogenesis"), not a process, so the cleanest logical form is
  `MONDO:0000001 and (RO:0004021 some <BBSome-dependent trafficking process>)`
  pending a GO process term; a MONDO new-term request may need a paired GO request.

**Definition.** A ciliopathy caused by deficiency of a subunit, chaperonin-like
assembly factor, or dedicated operator of the BBSome — the obligate eight-subunit
complex that escorts signaling receptors and other cargo into and out of the
primary cilium — producing failure of BBSome-dependent ciliary cargo trafficking.

**Why this is a genuine mechanism class.** MONDO's `ciliopathy` class is large and
mechanistically heterogeneous: it lumps the motile-cilia dyskinesias, the
transition-zone/IFT disorders, and the BBSome trafficking disorders into one
undifferentiated bucket of 36 asserted children. The BBSome is a discrete,
well-delimited molecular machine with a defined membership (*BBS1, 2, 4, 5, 7,
TTC8/8, 9, BBIP1/18*; assembly factors *MKKS/6, BBS10, BBS12*; operators
*ARL6/3, LZTFL1/17*), and its disorders share a distinctive phenotype — obesity,
retinal degeneration, polydactyly, renal anomaly — that the transition-zone
ciliopathies do not. This is the first natural molecular-machine subdivision of
`ciliopathy`, and would set the pattern for IFT-opathy and transition-zone-opathy
siblings.

**dismech provenance.** `kb/modules/bbsome_trafficking.yaml` — BBSome Subunit
Deficiency / BBS Chaperonin Assembly Defect → Defective BBSome Assembly → BBSome
Membrane Recruitment and Retrograde IFT Coupling → BBSome-Dependent Ciliary Cargo
Trafficking Failure. **3 conforming disorder entries**, plus the dismech
`BBSome-opathies` grouping — which already records the gap explicitly, mapping to
`MONDO:0005308 ciliopathy` with `skos:broadMatch` and the justification *"MONDO
has no dedicated 'BBSome machine disorder' node and the parent ciliopathy class is
broader than this BBSome-scoped union."*

**Candidate MONDO members.** Direct: `MONDO:0015229` Bardet-Biedl syndrome ·
`MONDO:0009367` McKusick-Kaufman syndrome · `MONDO:0019200` retinitis pigmentosa
(BBSome-related subset — narrow to the *TTC8*/*BBS* forms, not the whole class).
MONDO's existing per-gene terms make this class immediately populous:
`MONDO:1040043` BBS1-related ciliopathy, `MONDO:1040044` BBS4-related ciliopathy,
`MONDO:1040045` BBS12-related ciliopathy, `MONDO:0700236` BBS9-related ciliopathy,
plus the numbered Bardet-Biedl syndrome 1–22 series (restricted to BBSome-component
genes; the non-BBSome BBS loci such as *CEP290*, *SDCCAG8*, *IFT27* should stay
under `ciliopathy` only).

**MONDO gap evidence.** `"BBSome"` / `"bbsome"`: **0 hits** across labels,
synonyms, and definition text — despite MONDO carrying 25+ Bardet-Biedl and
`BBS*-related ciliopathy` terms.

---

## 4. Summary table

| # | Proposed label | Logical definition (verified GO) | Proposed parent | dismech module | Conformers | MONDO hits (label/syn/def) |
|---|---|---|---|---|---|---|
| 1 | intoxication-type inborn error of metabolism | *textual* (proteostasis-deficiencies precedent) | `MONDO:7770011` + IEM | `metabolic_intoxication_decompensation` | 19 | 0 / 0 / 0 |
| 2 | cardiac channelopathy | `RO:0004021 some GO:0086001` | `MONDO:7770011` + heart disorder | `cardiac_ion_channel_repolarization` | 12 | 0 / 0 / 0 |
| 3 | FGFR-opathy | `RO:0004021 some GO:0008543` | `MONDO:7770011` + hereditary disease | `fgfr_gain_of_function_skeletal_dysplasia` | 11 | 0 / 0 / 1 (single disease) |
| 4 | synaptic vesicle cycle disorder | `RO:0004021 some GO:0099504` | `MONDO:0021017 synaptopathy` | `synaptic_vesicle_cycle` | 9 | 0 / 0 / 0 |
| 5 | centrosomopathy | `RO:0004021 some GO:0007098` | `MONDO:7770011` + hereditary disease | `neural_progenitor_centrosome_spindle_dysfunction` | 8 | 0 / 0 / 0 |
| 6 | meiotic recombination failure disorder | `RO:0004021 some GO:0007131` | `MONDO:7770011` + reproductive | `meiotic_prophase_failure` | 7 | 0 / 0 / 0 |
| 7 | Hedgehog pathway activation disease | `RO:0004021 some GO:0007224` | `MONDO:7770011` | `hedgehog_pathway_activation` | 5 | 0 / 0 / 0 |
| 8 | polyglutamine expansion disease | *textual* (proteostasis-deficiencies style; synucleinopathy/TDP-43 sibling precedent) | `MONDO:0021179` | `polyglutamine_expansion_proteotoxicity` | 4 (+grouping) | 0 / 0 / 0 |
| 9 | macroautophagy deficiency disorder | `RO:0004021 some GO:0016236` | `MONDO:0021179` | `disabled_macroautophagy` | 5 | 0 / 0 / 0 |
| 10 | BBSome-opathy | complex-scoped; GO process term needed | `MONDO:0005308 ciliopathy` | `bbsome_trafficking` | 3 (+grouping) | 0 / 0 / 0 |

Eight of the ten list `MONDO:7770011` among their proposed parents — #1, #2, #3,
#4, #5, #6, #7, and #9 — so adopting all ten would take
`MONDO:7770011 disease by molecular mechanism` from **5 to 13 direct children**.
Several are deliberately multi-parented: #4 also under `MONDO:0021017
synaptopathy`, #9 also under `MONDO:0021179 proteostasis deficiencies`. Only two
do **not** attach to the mechanism axis directly — #8 (under `proteostasis
deficiencies`) and #10 (under `MONDO:0005308 ciliopathy`).

Of those secondary parents, `proteostasis deficiencies` and `ciliopathy` are
themselves children of `MONDO:7770011`, but **`MONDO:0021017 synaptopathy` is
not** — it currently sits only under `MONDO:0005071 nervous system disorder`.
Whether to place `synaptopathy` on the mechanism axis as part of adopting #4 is a
separate question for MONDO, not something this proposal assumes.

---

## 5. Runners-up and side findings

**Runners-up** — real gaps, held back only by thinner dismech backing. All returned
0 MONDO hits on all three passes:

| Candidate | dismech module | Conformers | GO anchor |
|---|---|---|---|
| somite segmentation clock disorder | `axial_segmentation_serial_homology` | 3 | `GO:0001756 somitogenesis` ✅ |
| ectodysplasin-NF-κB pathway disease | `eda_edar_nfkb_ectodermal_appendage` | 4 | GO term needs selection |
| molecular-mimicry post-infectious autoimmune disease | `molecular_mimicry_autoimmunity` | 3 | — (only an *obsolete* MONDO term exists) |
| epithelial barrier dysfunction disease | `epithelial_barrier_dysfunction` | 4+1 | — |
| serial-homology limb/digit patterning disorder | `limb_digit_patterning_serial_homology` | 3 | — |

The segmentation-clock candidate is the strongest of these on the *MONDO* side
despite thin dismech backing: MONDO already has spondylocostal dysostosis 1–6
typed by the exact segmentation-clock genes (*DLL3*, *MESP2*, *LFNG*, *HES7*,
*TBX6*), so the member set is pre-built and only the parent class is missing.

**Side finding — unmapped dismech entries.** Assembling the member lists surfaced
entries that cannot be aligned to MONDO. Two distinct gaps, which an earlier draft
conflated:

- **No top-level `disease_term:` at all — 19 files** across the KB, including
  `NDE1-related_Microcephaly_Lissencephaly`, `KATNB1-related_Cortical_Malformation`,
  and `TUBB_TUBB5-related_Microcephaly` (all §3.5 members).
- **A `disease_term:` with a `preferred_term` but no bound `term:` id — e.g.
  `MCM9-related_gametogenic_failure`** (§3.6), which carries
  `disease_term: {preferred_term: MCM9-related gametogenic failure}` and so is
  *not* missing the slot, only the identifier. An earlier draft wrongly listed it
  in the first category.

Measured against the KB at the time of writing (1,795 disorder files): 19 files
with no top-level `disease_term:`, and 17 with no `MONDO:` identifier anywhere in
the file. Both counts move as curation proceeds — re-measure before filing. These
are dismech curation gaps (or genuine MONDO new-term candidates) and are worth
their own issue, quoting the re-measured numbers rather than these.

---

## 6. Reproducing this analysis

**Snapshot provenance.** Every MONDO claim in this document (the five children of
`MONDO:7770011`, the 240 `RO:0004021` axioms, the obsoletion of `MONDO:0021016`,
and all zero-hit results) was computed against a single local snapshot. MONDO
publishes no version IRI date in the OAK SQLite build, so the snapshot is
identified by fingerprint:

| Property | Value |
|---|---|
| Source | OAK `sqlite:obo:mondo` (downloads the then-current release) |
| Fetched | 2026-08-01 |
| Local path | `$HOME/.data/oaklib/mondo.db` (`/root/.data/oaklib/mondo.db` in this environment) |
| Labelled `MONDO:` classes | 31,886 |
| Deprecated `MONDO:` classes | 3,968 |

Re-running against a later release may give different counts. **Re-verify before
filing any new-term request** — the three-pass exclusion check below is the step
that matters most, and it is only meaningful if it can actually be re-run.

```bash
# 0. Fingerprint the snapshot you are actually using, and compare to the table above.
MONDO_DB="$HOME/.data/oaklib/mondo.db"
uv run python -c "
import sqlite3, sys; c = sqlite3.connect(sys.argv[1])
q = lambda s: c.execute(s).fetchone()[0]
print('labelled classes:', q(\"SELECT count(*) FROM rdfs_label_statement WHERE subject LIKE 'MONDO:%'\"))
print('deprecated      :', q(\"SELECT count(*) FROM statements WHERE predicate='owl:deprecated' AND subject LIKE 'MONDO:%'\"))
" "$MONDO_DB"

# 1. MONDO mechanism axis — direct children of 'disease by molecular mechanism'
uv run python -c "
import sqlite3, sys; c = sqlite3.connect(sys.argv[1])
for r in c.execute(\"\"\"SELECT e.subject, s.value FROM edge e
  LEFT JOIN rdfs_label_statement s ON s.subject = e.subject
  WHERE e.object = 'MONDO:7770011' AND e.predicate = 'rdfs:subClassOf'\"\"\"): print(r)
" "$MONDO_DB"

# 2. Three-pass exclusion check for one mechanism phrase (label / synonym / definition)
uv run python -c "
import sqlite3, sys; c = sqlite3.connect(sys.argv[1]); pat = sys.argv[2].lower()
rows = c.execute(\"\"\"SELECT subject, value FROM statements WHERE value IS NOT NULL
  AND subject LIKE 'MONDO:%' AND predicate IN ('rdfs:label','oio:hasExactSynonym',
  'oio:hasRelatedSynonym','oio:hasBroadSynonym','oio:hasNarrowSynonym','IAO:0000115')\"\"\").fetchall()
hits = {s for s, v in rows if pat in v.lower()}
print(f'{sys.argv[2]!r}: {len(hits)} hit(s)'); [print(' ', h) for h in sorted(hits)[:10]]
" "$MONDO_DB" "BBSome"

# 3. dismech module backing — DISTINCT FILE count (the metric used in §2, §3 and §4)
grep -rl "conforms_to:.*bbsome_trafficking#" kb/disorders/ | wc -l

# 4. GO anchor verification
uv run runoak -i sqlite:obo:go info GO:0086001
```

---

## 7. Suggested next steps

1. **Review and prune.** Ten is the requested count, not a claim that all ten are
   equally ready. #1–#7 are the strong set. #9 needs the scope decision described
   in its caveat; #10 may need a paired GO process request.
2. ~~**Mint dismech `kb/groupings/` entries for the four proposals that lack one.**~~
   **Done in this PR.** All ten proposals now have a dismech grouping backing them,
   so membership is machine-auditable via `just check-groupings` before anything
   goes upstream:

   | Proposal | Backing dismech grouping | Status |
   |---|---|---|
   | #1 intoxication-type IEM | `Intoxication-Type_Inborn_Errors_of_Metabolism` (19 members, NECESSARY) | **added here** |
   | #2 cardiac channelopathy | `Inherited_Arrhythmia_Syndromes` (N&S criteria) | pre-existing |
   | #3 FGFR-opathy | `FGFR_Related_Skeletal_Dysplasias` | pre-existing |
   | #4 synaptic vesicle cycle disorder | `Synaptic_Vesicle_Cycle_Disorders` | pre-existing |
   | #5 centrosomopathy | `Centrosomopathies` (8 members, NECESSARY) | **added here** |
   | #6 meiotic recombination failure | `Meiotic_Gametogenic_Failure` | pre-existing |
   | #7 Hedgehog pathway activation disease | `Hedgehog_Pathway_Activation_Disorders` (5 members, N&S) | **added here** |
   | #8 polyglutamine expansion disease | `Polyglutamine_Disorders` | pre-existing |
   | #9 macroautophagy deficiency | `Macroautophagy_Deficiency_Disorders` (5 members, NECESSARY) | **added here** |
   | #10 BBSome-opathy | `BBSome-opathies` (already records the MONDO gap) | pre-existing |

   Note #5's nearest existing groupings — `Primary_Microcephaly_Spectrum` and
   `Lissencephaly_and_Neuronal_Migration_Disorders` — are phenotype-scoped, not
   centrosome-scoped, which is why `Centrosomopathies` was minted as a new grouping
   rather than an edit to either. The four new groupings audit clean
   (37/37 members SATISFIED, zero violations, no unlisted candidates on the one
   N&S class).
3. **File MONDO new-term requests** one per node, each carrying: label, synonyms,
   textual definition, the `RO:0004021` logical definition with its verified GO
   term, proposed parentage, and the candidate member list from §3.
4. **Record `skos:` mappings back into dismech** once terms are minted, following
   the pattern the `BBSome-opathies` grouping already uses
   (`skos:broadMatch` → `MONDO:0005308` with a written justification).
