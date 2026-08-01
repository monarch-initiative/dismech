# Ten Proposed Mechanism-Based Classification Nodes for MONDO, Derived from dismech

**Date:** 2026-08-01
**Status:** Proposal for MONDO review — no MONDO edits made
**Source KB:** dismech (`kb/modules/`, `kb/disorders/`, `kb/groupings/`)
**MONDO snapshot:** local OAK `sqlite:obo:mondo` (`~/.data/oaklib/mondo.db`, fetched 2026-08-01)

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
  synonym `disorder of Ras protein signal transduction`. Nine of the ten
  proposals below can be minted the same way, and each cites a **verified GO term**.
- **proteostasis deficiencies** (`MONDO:0021179`) carries *no* `RO:0004021`
  axiom — it is a textual grouping with asserted children. That is the precedent
  for proposal #3, whose mechanism (toxic-metabolite accumulation under catabolic
  stress) is a convergence pattern rather than one GO process.

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

**Candidates excluded by the filter** (recorded so the work isn't repeated):

| dismech module | Conformers | Excluded because MONDO already has |
|---|---|---|
| `lysosomal_substrate_accumulation` | 85 | `lysosomal storage disease` |
| `ciliopathy_dysfunction` | 68 | `MONDO:0005308 ciliopathy` |
| `complex_iv_assembly_deficiency` | 61 | `mitochondrial complex IV deficiency` |
| `congenital_disorder_of_glycosylation` | 26 | `MONDO:0017740` / CDG classes |
| `amyloidogenesis` | 39 | `MONDO:0019065 amyloidosis` (under proteostasis deficiencies) |
| `heme_biosynthesis_porphyria` | 10 | `porphyria` |
| `microtubule_dependent_neuronal_migration_failure` | 22 | `MONDO:0100153 tubulinopathy` |
| `er_protein_storage_disease` | — | `MONDO:0027749 serpinopathy` |
| `cranial_suture_premature_fusion` | 5 | `craniosynostosis` |
| `renal_cystogenesis` | 7 | `cystic kidney disease` |
| `drug_hypersensitivity_scar` | 9 | `MONDO:0005594 severe cutaneous adverse reaction` |
| `granuloma_formation` | 7 | `granulomatous disease` classes |

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

**Why this is a genuine mechanism class.** This is the *Saudubray* axis, the
single most operationally important division in clinical metabolic medicine: it
separates disorders that present as an acute reversible crisis requiring emergency
protocols (stop protein, give glucose, scavenge ammonia, dialyse) from the
"energy-deficiency" and "complex-molecule" classes that do not. MONDO currently
scatters these diseases across `urea cycle disorder`, `classic organic aciduria`,
`disorder of fatty acid oxidation and ketogenesis`, and amino-acid disorders —
partitioned by *which substrate* rather than by *how the disease behaves*. The
intoxication axis cuts across all four.

**dismech provenance.** `kb/modules/metabolic_intoxication_decompensation.yaml` —
node chain: Enzymatic Block in Intermediary Metabolism → Toxic Metabolite
Accumulation and Energy Deficit → Acute Metabolic Decompensation → Acute Metabolic
Encephalopathy → Neurological Injury and Multiorgan Crisis. **19 conforming
disorder entries** — the largest non-excluded module in the KB.

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
a shared therapeutic strategy — the CNP/NPR2 analogue vosoritide and FGFR-pathway
antagonists work across the class, which is the practical payoff of naming it.
MONDO currently has ~30 `FGFR*-related` per-gene terms and no class over them.

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
entries.** Related dismech groupings: `Primary_Microcephaly_Spectrum`,
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

### 3.7 Hedgehog pathway signaling disease

- **Proposed label:** `Hedgehog pathway signaling disease`
- **Synonyms:** Hedgehog-driven neoplasm; disorder of smoothened signaling pathway; Hedgehog pathway activation disease
- **Proposed parents:** `MONDO:7770011 disease by molecular mechanism`
- **Logical definition:** `MONDO:0000001 and (RO:0004021 some GO:0007224)`
  — *`GO:0007224 smoothened signaling pathway`* ✅ verified.

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
Tumorigenesis. **5 conforming disorder entries.**

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
Damage and Age-Related Disease. **5 conforming disorder entries.**

**Candidate MONDO members (5 in dismech).**
`MONDO:0008178` / `MONDO:0000507` inclusion body myopathy with Paget disease of
bone and frontotemporal dementia (*VCP*) · `MONDO:0008029` Bethlem myopathy ·
`MONDO:0004976` amyotrophic lateral sclerosis · `MONDO:0005180` Parkinson disease.
Recommended additions per the caveat above: Vici syndrome (*EPG5*), BPAN
(*WDR45*), *ATG7*-related disorder.

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
- **Logical definition:** `MONDO:0000001 and (RO:0004021 some GO:0032465)` is **not**
  recommended. Prefer a complex-scoped textual definition, or — if GO gains a
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
| 7 | Hedgehog pathway signaling disease | `RO:0004021 some GO:0007224` | `MONDO:7770011` | `hedgehog_pathway_activation` | 5 | 0 / 0 / 0 |
| 8 | polyglutamine expansion disease | *textual* (synucleinopathy precedent) | `MONDO:0021179` | `polyglutamine_expansion_proteotoxicity` | 4 (+grouping) | 0 / 0 / 0 |
| 9 | macroautophagy deficiency disorder | `RO:0004021 some GO:0016236` | `MONDO:0021179` | `disabled_macroautophagy` | 5 | 0 / 0 / 0 |
| 10 | BBSome-opathy | complex-scoped; GO process term needed | `MONDO:0005308 ciliopathy` | `bbsome_trafficking` | 3 (+grouping) | 0 / 0 / 0 |

Adopting all ten would take `MONDO:7770011 disease by molecular mechanism` from
5 children to 12 direct children (8 of the 10 attach there; #8 and #9 attach under
`proteostasis deficiencies`, #4 under `synaptopathy`, #10 under `ciliopathy` — all
of which are themselves already on the mechanism axis).

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

**Side finding — three dismech entries lack a `disease_term`**, surfaced while
assembling §3.5's member list: `NDE1-related_Microcephaly_Lissencephaly`,
`KATNB1-related_Cortical_Malformation`, `TUBB_TUBB5-related_Microcephaly`. Also
`MCM9-related_gametogenic_failure` (§3.6). These are either unmapped-to-MONDO
dismech entries or genuine MONDO new-term candidates; either way they are dismech
curation gaps worth their own issue.

---

## 6. Reproducing this analysis

```bash
# MONDO mechanism axis — direct children
uv run python -c "
import sqlite3; c=sqlite3.connect('/root/.data/oaklib/mondo.db')
for r in c.execute(\"SELECT e.subject,s.value FROM edge e LEFT JOIN rdfs_label_statement s ON s.subject=e.subject WHERE e.object='MONDO:7770011' AND e.predicate='rdfs:subClassOf'\"): print(r)"

# dismech module backing — conforming disorder files per module
grep -rl "conforms_to:.*<module_name>#" kb/disorders/

# GO anchor verification
uv run runoak -i sqlite:obo:go info GO:0086001
```

The three-pass MONDO exclusion check (label / synonym / definition text) is the
step that matters most and is the one to re-run before filing any new-term
request, since MONDO moves quickly.

---

## 7. Suggested next steps

1. **Review and prune.** Ten is the requested count, not a claim that all ten are
   equally ready. #1–#7 are the strong set. #9 needs the scope decision described
   in its caveat; #10 may need a paired GO process request.
2. **Mint dismech `kb/groupings/` entries for the four proposals that lack one** —
   #1 intoxication-type IEM, #5 centrosomopathy, #7 Hedgehog pathway signaling
   disease, #9 macroautophagy deficiency — with `membership_criteria` + `logic`
   so membership is machine-auditable via `just check-groupings` before anything
   goes upstream. The other six already have a dismech grouping backing them:

   | Proposal | Existing dismech grouping |
   |---|---|
   | #2 cardiac channelopathy | `Inherited_Arrhythmia_Syndromes` (N&S criteria) |
   | #3 FGFR-opathy | `FGFR_Related_Skeletal_Dysplasias` |
   | #4 synaptic vesicle cycle disorder | `Synaptic_Vesicle_Cycle_Disorders` |
   | #6 meiotic recombination failure | `Meiotic_Gametogenic_Failure` |
   | #8 polyglutamine expansion disease | `Polyglutamine_Disorders` |
   | #10 BBSome-opathy | `BBSome-opathies` (already records the MONDO gap) |

   Note #5's nearest existing groupings — `Primary_Microcephaly_Spectrum` and
   `Lissencephaly_and_Neuronal_Migration_Disorders` — are phenotype-scoped, not
   centrosome-scoped, so a new grouping is genuinely needed rather than an edit.
3. **File MONDO new-term requests** one per node, each carrying: label, synonyms,
   textual definition, the `RO:0004021` logical definition with its verified GO
   term, proposed parentage, and the candidate member list from §3.
4. **Record `skos:` mappings back into dismech** once terms are minted, following
   the pattern the `BBSome-opathies` grouping already uses
   (`skos:broadMatch` → `MONDO:0005308` with a written justification).
