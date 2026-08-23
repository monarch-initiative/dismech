# Lysosomal storage grouping review: completeness, members, literature and gaps

*2026-08-20. Scope: the `Lysosomal Storage Disorders` grouping and its three
nested groupings — `Mucopolysaccharidoses`, `Mucolipidoses`, `Niemann-Pick
Diseases`. 48 disease entries reviewed. Literature scanned to August 2026.*

## Summary

The tree was structurally incomplete rather than merely under-populated. The LSD
grouping carries a `NECESSARY_AND_SUFFICIENT` criterion, which makes an unlisted
conforming disorder a **contradiction**, not a backlog item — and the audit
reported **30 unlisted candidates against 14 listed members**. Two further
classes of defect sat underneath that count: four entries were invisible to the
criteria machinery because they declared no conformance to the shared module,
and one grouping criterion contradicted a member it should have admitted.

All of this is now fixed (commit `cd53785`, plus the joint-criterion refinement
that follows it). The grouping audit reports **48/48 members SATISFIED, no
contradictions, and an empty candidate list**.

The content review is a different story. The structural tree is now sound; the
*entries* it points at are, for the MPS / mucolipidosis / Niemann-Pick branches,
substantially out of date with 2025–2026 literature, and 15 of 48 are stubs of
under 450 lines. Details and a prioritized worklist below.

---

## 1. Completeness audit

### 1.1 What was missing

| Grouping | Before | After | Added |
|---|--:|--:|---|
| Lysosomal Storage Disorders | 14 immediate | 36 immediate | 1 nested grouping (NCL), 22 diseases, −1 redundant |
| Mucopolysaccharidoses | 4 | 7 | MPS VI, MPS VII, MPS IX |
| Mucolipidoses | 3 | 4 | ML III alpha/beta |
| Niemann-Pick Diseases | 4 | 5 | NPD type E |

**LSD grouping.** The `Neuronal Ceroid Lipofuscinoses` grouping already existed
with 7 members and was simply not wired in; nesting it removed 7 of the 30
candidates in one edit. The remaining 22 were added as direct DISEASE members,
chosen to close a systematic bias — the original list was sphingolipidosis- and
MPS-weighted, and carried almost nothing from the other arms of the LSD
definition:

| Arm of the definition | Previously | Now |
|---|---|---|
| Primary hydrolase deficiency | 8 members | + GM1 ×3, LIPA ×2, NAGA ×3, ACP2, Pompe subtypes ×2 |
| Activator / cofactor deficiency | none | PSAP saposin disorders ×3, GM2A (Tay-Sachs AB variant) |
| Protective-protein deficiency | none | Galactosialidosis (CTSA) |
| Oligosaccharidosis / glycoproteinosis | sialidoses only | + alpha-mannosidosis, aspartylglucosaminuria, glycoproteinoses |
| Trafficking failure, normal hydrolases | none | MPS-plus syndrome (VPS33A), HSP48 (AP5Z1) |

The grouping's own description promises "hydrolase, activator, membrane
transporter, or trafficking protein"; before this review only the first of those
four was represented.

**One redundancy removed.** `Niemann-Pick Disease Type C` was listed as a direct
DISEASE member *and* covered by the nested Niemann-Pick grouping, contradicting
the grouping's stated rationale that Niemann-Pick subtypes are not mixed in at
the LSD level. Dropped as a direct member.

**Two stale notes corrected.** The Niemann-Pick grouping recorded NPD-E as
"intentionally not listed in this batch because an open PR already exists". That
PR merged; the entry exists. Both the note and the MONDO consistency note were
rewritten, and the consistency note now also records why NPD type D has no
separate entry (an NPC1 Nova Scotia founder haplotype, covered by type C).

### 1.2 Entries invisible to the criteria machinery

Four entries could not satisfy criteria they were asserted against — the exact
hazard `CLAUDE.md` warns about, where a drifted or absent `conforms_to` silently
drops an entry out of a criterion it is supposed to satisfy.

| Entry | Was | Now |
|---|---|---|
| Maroteaux-Lamy (MPS VI) | `mps_gag_storage` only | + `lysosomal_substrate_accumulation#Lysosomal Hydrolase or Cofactor Deficiency` |
| Sly (MPS VII) | `mps_gag_storage` only | + same |
| MPS IX | `mps_gag_storage` only | + same |
| ML III alpha/beta | **no `conforms_to` at all** | + hydrolase-deficiency and substrate-accumulation nodes, mirroring ML II |

Each declaration restates what the node's own prose already says (ARSB, GUSB and
HYAL1 deficiency *are* lysosomal hydrolase deficiencies), so this is wiring, not
a new mechanistic claim.

### 1.3 A module hierarchy that was implicit

`mps_gag_storage#Lysosomal GAG Accumulation` is a specialization of
`lysosomal_substrate_accumulation#Lysosomal Substrate Accumulation` and did not
say so. It now declares conformance, following the existing module-to-module
pattern (7 prior instances, e.g. `er_protein_storage_disease` →
`fibrotic_response`).

**Note for tooling, not fixed here:** `groupings.py` matches a
`CONFORMS_TO_MODULE` criterion on the module **stem only** — it ignores the
`#Node` anchor, and it does **not** follow module→module conformance. So this
declaration documents the hierarchy correctly but does not by itself make
`mps_gag_storage` conformers satisfy a `lysosomal_substrate_accumulation`
criterion. That is why the four entries above needed direct declarations. Worth
an issue: transitive module conformance would make the MPS-branch wiring
unnecessary and would prevent this class of silent drop-out recurring.

### 1.4 A criterion that contradicted a correct member

Adding MPS IX produced a `NOT_SATISFIED` contradiction. The cause was not the
entry: **MPS IX genuinely has neither coarse facies nor dysostosis multiplex**.
It stores hyaluronan rather than a sulfated GAG and presents with periarticular
soft-tissue masses and short stature. The two-hallmark criterion encoded the
classic MPS picture as necessary, and MPS IX is the counterexample.

The hallmark branch now carries two further operands — structural joint disease
(`HP:0001367`) and restricted joint mobility (`HP:0011729`). These are kept
separate deliberately: HPO splits joint *structure* from joint *function*, and
the two MPS joint phenotypes fall on opposite sides of that split (MPS IX's
joint swelling is morphological; the near-universal MPS joint stiffness is not).
A single operand would have silently failed half the members.

---

## 2. Member-by-member review

`Cited 2024+` counts evidence PMIDs ≥ 39000000 as a proxy for recency. ⚠️ marks
entries under 450 lines.


#### Lysosomal Storage Disorders (direct members)

| Entry | Lines | Evidence items | Cited 2024+ | Phenotypes | Treatments | Trials | Models | Gaps |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| `Lysosomal_Acid_Phosphatase_Deficiency` ⚠️ | 175 | 9 | 0 | 1 | 0 | 0 | 1 | 0 |
| `Hereditary_Spastic_Paraplegia_48` ⚠️ | 251 | 12 | 1 | 6 | 1 | 0 | 0 | 0 |
| `Congenital_Sialidosis_Type_2` ⚠️ | 256 | 13 | 0 | 3 | 1 | 0 | 0 | 0 |
| `Gaucher_Disease_Due_To_Saposin_C_Deficiency` ⚠️ | 256 | 13 | 0 | 2 | 1 | 0 | 0 | 0 |
| `Krabbe_Disease_Due_To_Saposin_A_Deficiency` ⚠️ | 275 | 11 | 0 | 5 | 1 | 0 | 0 | 0 |
| `Combined_Saposin_Deficiency` ⚠️ | 283 | 12 | 0 | 4 | 1 | 0 | 0 | 0 |
| `GM1_Gangliosidosis_Type_3` ⚠️ | 287 | 14 | 0 | 4 | 1 | 0 | 0 | 0 |
| `Schindler_Disease` ⚠️ | 307 | 20 | 1 | 7 | 1 | 0 | 0 | 0 |
| `Glycoprotein_Storage_Disease` ⚠️ | 326 | 18 | 14 | 7 | 2 | 0 | 0 | 0 |
| `Tay-Sachs_Disease_AB_Variant` ⚠️ | 326 | 15 | 0 | 6 | 1 | 0 | 0 | 0 |
| `Cholesteryl_Ester_Storage_Disease` ⚠️ | 327 | 17 | 13 | 6 | 2 | 0 | 0 | 0 |
| `Kanzaki_Disease` ⚠️ | 335 | 20 | 1 | 7 | 2 | 0 | 0 | 0 |
| `NAGA_Deficiency_Type_3` ⚠️ | 349 | 15 | 1 | 10 | 1 | 0 | 0 | 0 |
| `Spinal_Muscular_Atrophy_Progressive_Myoclonic_Epilepsy` ⚠️ | 358 | 21 | 9 | 8 | 1 | 0 | 0 | 0 |
| `Juvenile_Sialidosis_Type_2` ⚠️ | 436 | 26 | 0 | 14 | 1 | 0 | 0 | 0 |
| `GM1_Gangliosidosis_Type_2` | 527 | 33 | 0 | 12 | 1 | 2 | 0 | 0 |
| `Galactosialidosis` | 547 | 16 | 0 | 12 | 1 | 0 | 0 | 0 |
| `Metachromatic_Leukodystrophy` | 649 | 40 | 21 | 6 | 2 | 0 | 0 | 0 |
| `GM1_Gangliosidosis_Type_1` | 984 | 61 | 2 | 19 | 4 | 4 | 0 | 0 |
| `Pompe_Disease` | 1362 | 85 | 13 | 17 | 8 | 0 | 0 | 0 |
| `Krabbe_Disease` | 1397 | 62 | 0 | 8 | 5 | 0 | 0 | 0 |
| `Tay-Sachs_Disease` | 1456 | 71 | 10 | 21 | 6 | 2 | 0 | 0 |
| `Sandhoff_Disease` | 1464 | 80 | 20 | 6 | 3 | 0 | 0 | 0 |
| `Sialidosis_Type_1` | 1468 | 97 | 13 | 20 | 8 | 0 | 0 | 0 |
| `Wolman_Disease` | 1542 | 119 | 42 | 13 | 5 | 0 | 2 | 2 |
| `Infantile-Onset_Pompe_Disease` | 1548 | 114 | 12 | 18 | 7 | 2 | 1 | 1 |
| `Gaucher_Disease` | 1641 | 95 | 6 | 19 | 6 | 0 | 0 | 0 |
| `Aspartylglucosaminuria` | 1827 | 58 | 0 | 41 | 4 | 1 | 0 | 0 |
| `Late-Onset_Pompe_Disease` | 1905 | 119 | 22 | 11 | 4 | 4 | 0 | 2 |
| `Mucopolysaccharidosis-Plus_Syndrome` | 2124 | 129 | 19 | 34 | 6 | 0 | 0 | 3 |
| `Fabry_Disease` | 2690 | 138 | 34 | 24 | 5 | 0 | 5 | 0 |
| `Alpha_Mannosidosis` | 2715 | 63 | 5 | 71 | 4 | 3 | 1 | 1 |

#### Mucopolysaccharidoses

| Entry | Lines | Evidence items | Cited 2024+ | Phenotypes | Treatments | Trials | Models | Gaps |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| `Mucopolysaccharidosis_type_IX` ⚠️ | 398 | 17 | 0 | 3 | 1 | 0 | 0 | 0 |
| `Maroteaux-Lamy_syndrome` | 615 | 37 | 0 | 11 | 3 | 0 | 0 | 0 |
| `Sly_syndrome` | 826 | 34 | 0 | 8 | 3 | 0 | 0 | 0 |
| `Hurler_syndrome` | 1242 | 66 | 0 | 16 | 3 | 0 | 0 | 0 |
| `Morquio_syndrome` | 1470 | 98 | 1 | 11 | 4 | 0 | 0 | 0 |
| `Sanfilippo_syndrome` | 1522 | 74 | 0 | 18 | 3 | 0 | 0 | 0 |
| `Hunter_syndrome` | 1646 | 80 | 3 | 13 | 4 | 0 | 0 | 0 |

#### Mucolipidoses

| Entry | Lines | Evidence items | Cited 2024+ | Phenotypes | Treatments | Trials | Models | Gaps |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| `Mucolipidosis_Type_IV` ⚠️ | 278 | 13 | 0 | 6 | 1 | 0 | 0 | 0 |
| `GNPTG-Mucolipidosis` ⚠️ | 422 | 24 | 0 | 9 | 4 | 0 | 0 | 0 |
| `Mucolipidosis_Type_II` | 519 | 27 | 0 | 10 | 2 | 0 | 0 | 0 |
| `Mucolipidosis_Type_III_Alpha_Beta` | 1836 | 82 | 0 | 36 | 5 | 0 | 0 | 0 |

#### Niemann-Pick Diseases

| Entry | Lines | Evidence items | Cited 2024+ | Phenotypes | Treatments | Trials | Models | Gaps |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| `Niemann-Pick_Disease_Type_E` ⚠️ | 182 | 8 | 0 | 2 | 0 | 0 | 0 | 1 |
| `Chronic_Neurovisceral_Acid_Sphingomyelinase_Deficiency` ⚠️ | 363 | 20 | 0 | 4 | 2 | 0 | 0 | 0 |
| `Niemann-Pick_Disease_Type_B` ⚠️ | 376 | 16 | 0 | 7 | 2 | 0 | 0 | 0 |
| `Niemann-Pick_Disease_Type_A` ⚠️ | 397 | 20 | 0 | 6 | 2 | 0 | 0 | 0 |
| `Niemann_Pick_Disease_Type_C` | 1344 | 61 | 4 | 22 | 6 | 0 | 0 | 0 |


### 2.1 What the table shows

**Recency is the dominant problem, and it is branch-specific.** Every MPS entry
except Hunter (3) and Morquio (1) cites nothing from 2024 onward. All four
mucolipidosis entries cite nothing recent. Four of five Niemann-Pick entries
cite nothing recent. The direct-LSD members are healthier — Fabry (34), Wolman
(42), Late-Onset Pompe (22), MLD (21), Sandhoff (20) are current — but that is
the exception across the tree, not the rule.

**Clinical trials are almost entirely absent.** All 7 MPS entries, all 4
mucolipidosis entries and all 5 Niemann-Pick entries carry **zero**
`clinical_trials` records, despite these being among the most trial-active rare
diseases in medicine. Section 3 lists specific trials that belong in them.

**Knowledge gaps were essentially unrecorded.** Before this review, 6 of 48
entries carried any `KNOWLEDGE_GAP` or `HUMAN_MODEL_MISMATCH` discussion
(Alpha-mannosidosis 1, Wolman 2, IOPD 1, LOPD 2, MPS-plus 3, NPD-E 1). The other
42 carried none. Three cross-cutting gaps have now been added to the shared
module (section 4); entry-specific gaps remain open work.

**Models are nearly absent.** 5 of 48 entries declare any animal or experimental
model. For a disease group whose therapeutic pipeline is built on mouse, sheep,
canine and iPSC models, and where `ModelMechanismLink` exists precisely to carry
them, this is a large structural gap.

**Two spot findings worth fixing directly:**

- `Lysosomal_Acid_Phosphatase_Deficiency` has **zero treatments** and one
  phenotype across 175 lines — the thinnest member of the tree.
- `Sly_syndrome` carried no joint phenotype at all, though joint stiffness and
  contracture are cardinal MPS VII features. It satisfied the grouping criteria
  via dysostosis multiplex, so nothing flagged it; the criteria audit surfaced it
  incidentally. **Fixed in this branch** — `HP:0001387` Joint stiffness added
  with GeneReviews evidence (PMID:38190471).

---

## 3. Latest publications (2025–2026)

Verified against PubMed; each PMID was resolved and its abstract read. Items
marked **★** are, in my judgement, the ones that change what an entry should
say.

### 3.1 The headline: brain-penetrant enzyme replacement is now approved

**★ PMID:42313339** — *Tividenofusp Alfa: First Approval* (Mol Diagn Ther, Jun
2026). Tividenofusp alfa (AVLAYAH), iduronate-2-sulfatase fused to a
transferrin-receptor-binding Fc domain, received **US accelerated approval in
March 2026** for the neurologic manifestations of MPS II. This is the first
approved therapy that delivers a replacement lysosomal enzyme across the blood–
brain barrier, and it directly addresses the defining therapeutic limitation of
this entire disease group. `Hunter_syndrome` does not mention it.

The approval rests on **reduction of CSF heparan sulphate**, not on a
neurocognitive outcome; continued approval is contingent on a confirmatory
trial. That distinction is now recorded as a module-level knowledge gap
(section 4.1) and must not be collapsed when curating.

Adjacent: **PMID:42527655** (IGF2-tagged lentiviral gene therapy for Hunter
syndrome), **PMID:42496452** (combined intracerebroventricular ERT and cord
blood transplantation in newborn-screened neuronopathic MPS II),
**PMID:42323476** (oral nanoparticle-encapsulated ERT for MPS I, proof of
concept), **PMID:42281208** (CSF-delivered bidirectional AAV9 improving optic
nerve and retinal pathology in a **sheep** Tay-Sachs model).

### 3.2 Therapy: durability, discontinuation and long-term outcome

- **★ PMID:42047222** — ASCEND final results: adults with ASMD sustained
  improvement over **up to 5 years** of olipudase alfa; DLCO 50.1%→66.5%
  predicted, spleen volume −57.5%, liver −36.8%, plasma lyso-sphingomyelin −72%.
  None of the three SMPD1 entries cites olipudase long-term data.
- **★ PMID:42541184** — AAV9-GAA gene therapy **after ERT discontinuation** in
  six children with infantile-onset Pompe (ChiCTR2200065664): all remained
  ventilator-free at 12 months with reduced muscle glycogen, but lung and
  cardiac structure showed no *further* improvement. A carefully hedged result
  that belongs in `Infantile-Onset_Pompe_Disease` with its limitations intact.
- **PMID:42538546** — position statement defining the "therapeutic corridor of
  stability" for ERT in Pompe disease.
- **★ PMID:42551329** — 4-year real-world arimoclomol outcomes in NPC (US early
  access programme).
- **PMID:42421116** — idursulfase beta 2-year phase 3 extension in MPS II,
  including patients switched from idursulfase.
- **★ PMID:42617290** — International LAL-D Registry longitudinal lipid data on
  sebelipase alfa across paediatric and adult patients — directly relevant to
  both `Wolman_Disease` and `Cholesteryl_Ester_Storage_Disease`.
- **PMID:42504165** — early versus late ERT in Morquio A **siblings**: early
  treatment attenuated spinal and upper-body disease but did not prevent lower
  limb skeletal progression. A rare within-family natural-history control.
- **PMID:42547363**, **PMID:42526029** — HSC gene therapy and cross-correction
  in metachromatic leukodystrophy.

### 3.3 Mechanism

- **★ PMID:42587127** — targeting **CD44** reverses sphingomyelin-induced
  oligodendrocyte maturation arrest in ASMD (EMBO Mol Med). A candidate
  mechanism for the neuronopathic arm that ERT does not reach.
- **★ PMID:42157966** — sinbaglustat is efficacious in GM2 gangliosidosis
  **primarily through GBA2 inhibition rather than GCS**. A target reassignment
  for a substrate-reduction agent; if the benefit is not glucosylceramide
  synthase inhibition, the substrate-reduction rationale for that class needs
  restating.
- **★ PMID:42467639** — levacetylleucine normalizes TFEB by *reducing* nuclear
  TFEB in an NPC cell model where it is already over-activated by lysosomal
  stress; the effect is stereospecific. See section 4.3.
- **PMID:42585307** — Mito-TEMPO improves survival in npc1-knockout zebrafish
  via Sod2-dependent mitophagy (Sci Adv).
- **PMID:42511762** — autophagy–lysosomal dysfunction as a **converging**
  cardiomyopathy mechanism across LSDs. A candidate for a new shared module, or
  for an additional node on the existing one.
- **PMID:42574251** — mucolipidosis II novel variants plus HAP1 cells as a
  disease model.

### 3.4 Nosology and phenotype expansion

- **★ PMID:42557761** — rare heterozygous **MCOLN1** loss-of-function variants in
  two patients with α-synucleinopathies (MSA, early-onset PD), with reduced
  lysosomal currents on patch clamp. Extends the GBA1 carrier paradigm to the
  mucolipidosis IV gene. See section 4.2.
- **★ PMID:41830174**, **PMID:40081374**, **PMID:42568187** — biallelic
  **AP5Z1**/AP5B1 variants cause retinal degeneration and hereditary macular
  dystrophy. `Hereditary_Spastic_Paraplegia_48` is curated as a pure spastic
  paraplegia and carries no retinal phenotype; this is a direct phenotype
  expansion for a member added in this review.
- **PMID:42351339** — biallelic **HGSNAT** variants causing autosomal recessive
  retinitis pigmentosa **without overt Sanfilippo syndrome**, with reduced
  enzyme activity. Relevant to `Sanfilippo_syndrome` as an attenuated
  non-syndromic allelic presentation.
- **PMID:42580759** — progressive myoclonic ataxia due to late-onset sialidosis.
- **PMID:42008923** — glycoproteinoses review covering clinical features,
  therapeutic landscape and regulatory pathways; the single best entry point for
  the six thin oligosaccharidosis members.
- **PMID:42482083** — systematic review of therapeutic approaches in
  alpha-mannosidosis.
- **PMID:42190545** — ClinGen lysosomal diseases VCEP **ACMG/AMP specification
  for IDUA**, with 131 variants classified. Authoritative variant-interpretation
  source for `Hurler_syndrome`.
- **PMID:42496454** — first-year results of MLD newborn screening in Lombardy.

---

## 4. Knowledge gaps

Three cross-cutting gaps were added to
`kb/modules/lysosomal_substrate_accumulation.yaml` as `KNOWLEDGE_GAP`
discussions with verified evidence (14/14 snippets verified). They are placed on
the shared module rather than on individual entries because each applies across
the whole tree, and every member conforms to it.

### 4.1 CNS delivery: corrected biomarker ≠ neurologic benefit

`gap_cns_delivery_biomarker_versus_clinical_benefit`, attached to *Lysosomal
Substrate Accumulation* and *Progressive Multisystem and Neurodegenerative
Disease*.

The first brain-penetrant ERT is approved on a CSF storage biomarker sitting at
this module's own central effector node, with clinical benefit explicitly
unverified. The same surrogate governs intrathecal and intracerebroventricular
routes and CNS-directed gene therapy. The curation rule that follows: record the
biomarker claim and the clinical-benefit claim as **separate assertions**, and
never curate CSF substrate correction as evidence of neurologic efficacy.
Evidence: PMID:42313339 (×2), PMID:42525369.

### 4.2 Heterozygous carriers and adult neurodegeneration

`gap_heterozygous_lsd_carrier_neurodegeneration_risk`, attached to
*Autophagic-Lysosomal Dysfunction* and *Storage-Cell Cytotoxicity*.

GBA1 established that a single loss-of-function allele — carrier status for a
member of this group — is among the strongest genetic risk factors for Parkinson
disease without causing Gaucher disease. Whether that is a GBA1 peculiarity or a
general property of partial lysosomal dysfunction is unresolved, and it
determines whether carrier status belongs in the other members' entries at all.
The proposed lesion is reduced lysosomal function *without* demonstrable
storage, so it does not travel down this module's chain and must not be modelled
as if it did. Evidence: PMID:42557761 (SUPPORT for the gap, PARTIAL for the
association — the authors themselves call MCOLN1 a candidate needing cohort
confirmation).

### 4.3 Which direction is TFEB dysregulated?

`gap_tfeb_direction_of_dysregulation_in_storage`, attached to
*Autophagic-Lysosomal Dysfunction and Secondary Cascade*.

TFEB **activation** has been pursued as a substrate-clearing strategy across
this group on the assumption that storage suppresses it. In an NPC cell model
the baseline is the opposite — TFEB already over-activated and nuclear from
chronic lysosomal stress — and levacetylleucine, an approved NPC therapy, works
by *lowering* nuclear TFEB. If the baseline direction differs by disorder, cell
type or stage, "TFEB activation" is not a coherent shared rationale, and a
conforming entry should curate the measured direction in its own cells rather
than inherit a directional assumption. Caveat preserved in the entry: the
finding is from a HeLa model, not patient neurons. Evidence: PMID:42467639.

### 4.4 Gaps identified but not curated

These are real and evidenced but are entry-level rather than module-level, so
they belong in the disorder entries and are left as work:

1. **Substrate-reduction target ambiguity** — if sinbaglustat acts via GBA2
   rather than GCS (PMID:42157966), the mechanism of benefit for
   substrate-reduction therapy in the gangliosidoses is unsettled. Belongs on
   `Tay-Sachs_Disease` / `Sandhoff_Disease`.
2. **Genotype–phenotype discontinuity in the allelic series** — NAGA
   (Schindler / Kanzaki / type 3), LIPA (Wolman / CESD), GAA (infantile /
   late-onset) and GNPTAB (ML II / ML III alpha/beta) each span extreme
   phenotypic ranges from one locus. The residual-activity threshold model is
   assumed across the tree and directly tested nowhere in it.
3. **Cardiomyopathy as a convergent LSD endpoint** (PMID:42511762) — currently
   modelled, if at all, per-disease. Candidate for a shared node or module,
   alongside `cardiomyopathy_maladaptive_remodeling`.
4. **Non-syndromic allelic presentations** — HGSNAT retinitis pigmentosa without
   Sanfilippo (PMID:42351339), AP5Z1 macular dystrophy (PMID:41830174).
   Storage-gene variants presenting as isolated organ disease are a systematic
   ascertainment gap in a KB organized around syndromic entries.

---

## 5. Prioritized worklist

**P1 — the entry is now wrong or materially incomplete**

1. `Hunter_syndrome`: add tividenofusp alfa (PMID:42313339) with
   `therapeutic_modality`, `target_mechanisms` on the CNS storage node, and the
   accelerated-approval caveat. Add idursulfase beta extension (PMID:42421116).
2. `Hereditary_Spastic_Paraplegia_48`: add the AP5Z1 retinal/macular phenotype
   (PMID:41830174, PMID:40081374).
3. Three SMPD1 entries: add ASCEND 5-year olipudase outcomes (PMID:42047222).
4. `Infantile-Onset_Pompe_Disease`: add the AAV9-GAA post-ERT-discontinuation
   trial with its negative cardiopulmonary finding intact (PMID:42541184).
5. `Wolman_Disease` / `Cholesteryl_Ester_Storage_Disease`: LAL-D Registry
   longitudinal sebelipase data (PMID:42617290).
6. `Lysosomal_Acid_Phosphatase_Deficiency`: has no treatments and one phenotype.
7. ~~`Sly_syndrome`: no joint phenotype annotated.~~ **Done in this branch.**

**P2 — structural**

8. Populate `clinical_trials` across the MPS, mucolipidosis and Niemann-Pick
   branches (all currently zero).
9. Open an issue for transitive module conformance in `groupings.py` (§1.3).
10. Resolve the **umbrella Disease entries**, of which this tree has two, both
    tracked on issue [#4490](https://github.com/monarch-initiative/dismech/issues/4490):
    - `Mucopolysaccharidosis` (`MONDO:0019249`) holds the same MONDO term the MPS
      *grouping* maps to with `skos:exactMatch`, so the concept exists twice in
      the KB, as a Disease and as a Grouping.
    - `Glycoprotein_Storage_Disease` (`MONDO:0009296`) self-describes as "a group
      of autosomal recessive lysosomal storage disorders" and is now listed in
      the LSD grouping *beside* `Aspartylglucosaminuria` and `Alpha-mannosidosis`,
      two of the things it is an umbrella for — structurally the same duplication
      this review removed for Niemann-Pick type C. Caught in review of this work,
      not by the audit.

    Both are grandfathered rather than fixed. The LSD criterion is
    `NECESSARY_AND_SUFFICIENT` and both the umbrella and its constituents conform
    to the module, so dropping either side would create a contradiction — worse
    than the redundancy. Note both have **empty `has_subtypes`**, so the
    duplication is invisible from the umbrella entry and only appears once a
    grouping lists umbrella and constituents as siblings; the `has_subtypes`
    check proposed on #4490 would catch neither. This is a lump/split decision
    for a curator, not a side-effect of a completeness pass.
11. Add `modeled_mechanisms`-linked models: 5 of 48 entries declare any.

**P3 — content depth**

12. The 15 sub-450-line entries, using PMID:42008923 (glycoproteinoses) and
    PMID:42482083 (alpha-mannosidosis) as entry points for the oligosaccharidosis
    cluster.
13. Entry-level knowledge gaps from §4.4.

---

## 6. Verification

| Check | Result |
|---|---|
| `just check-groupings` (4 groupings) | 48/48 members SATISFIED, 0 contradictions, 0 unlisted candidates |
| `just validate-grouping` ×4 | passed |
| `just validate-disorders` (4 changed entries) | passed, 224/231 snippets verified (7 skipped by prefix) |
| `just validate` (module) | passed |
| `just count-verified-snippets` (module) | 14/14 verified |
| `just check-duplicate-keys` | clean |
| `just validate-history-all` | 5828 records, no issues |
| `pytest -k "conforms"` | 2238 passed |

Literature: PubMed E-utilities, `pdat` 2024-01-01 to 2026-12-31, ~25 queries
across therapy, mechanism, delivery, screening and per-member axes. Every PMID
cited above was resolved and its abstract read; the six used as evidence were
cached via `just fetch-reference` and their snippets verified against the cache.
