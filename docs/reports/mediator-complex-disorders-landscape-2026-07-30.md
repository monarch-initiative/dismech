# Mediator Complex Disorders ("MEDopathies") — Landscape & KB Gap Analysis

*Compiled 2026-07-30. Scope: every germline human Mendelian disease associated with a
subunit of the Mediator transcriptional coactivator complex (the "MEDopathies"), plus the
somatic and refuted/provisional associations. This is a research/landscape survey — a map
of the disease space and of the PubMed literature dismech does and does not yet cite. All
PMIDs were verified to exist on PubMed; every PMID marked **NEW** was fetched into
`references_cache/` during this survey and (where cited in the KB) snippet-validated.*

## What the Mediator complex is

The Mediator is a ~30-subunit assembly that bridges gene-specific transcription factors at
enhancers and RNA polymerase II at promoters. It is organised into **head**, **middle**,
**tail**, and a dissociable **CDK8 kinase module (CKM)**. The CKM is a four-part cap:
a kinase (**CDK8** *or* its paralog **CDK19**), **cyclin C (CCNC)**, a scaffold
(**MED12** *or* **MED12L**), and a large subunit (**MED13** *or* **MED13L**). Germline
variants across the complex converge on dysregulated Pol II transcription during
development, producing a family of overlapping neurodevelopmental / neurodegenerative
syndromes now collectively termed **MEDopathies** (Fazio 2025, PMID:41465117; Guillouet
2025, PMID:40081376).

## Master table — germline mediatorpathies

Module abbreviations: CKM = CDK8 kinase module; H = head; M = middle; T = tail; core =
structural core. "In KB?" refers to coverage as of this survey.

| Gene | Module | Disease (abbrev) | OMIM pheno | MONDO | Inh. | In KB? |
|---|---|---|---|---|---|---|
| **MED12** | CKM | FG syndrome 1 / Opitz-Kaveggia (FGS1) | 305450 | MONDO:0010590 | XLR | ✅ subtype |
| **MED12** | CKM | Lujan (Lujan-Fryns) syndrome | 309520 | MONDO:0010655 | XLR | ✅ (noted) |
| **MED12** | CKM | X-linked Ohdo, Maat-Kievit-Brunner type | 300895 | MONDO:0010477 | XLR | ❌ **gap** |
| **MED12** | CKM | Hardikar syndrome (female-specific) | 301068 | MONDO:0012997 | XL (females) | ❌ **gap** |
| **MED12** | CKM | Female syndromic NDD | — | — | XL de novo | ❌ **gap** |
| **MED12** | CKM | X-linked partial epilepsy without ID | — | — | XLR | ❌ **gap** |
| **MED12L** | CKM | Nizon-Isidor syndrome (NIZIDS) | 618872 | MONDO:0030030 | AD | ❌ **gap** |
| **MED13** | CKM | Intellectual dev. disorder 61 (MRD61) | 618009 | MONDO:0032485 | AD | ✅ subtype + own file |
| **MED13L** | CKM | MED13L syndrome (MRFACD) | 616789 | MONDO:0014773 | AD | ✅ subtype |
| **CDK8** | CKM | ID w/ hypotonia & behavioral abn. (IDDHBA) | 618748 | MONDO:0032897 | AD | ❌ **gap** |
| **CDK19** | CKM | Developmental & epileptic enceph. 87 (DEE87) | 618916 | MONDO:0030059 | AD | ❌ **gap** |
| **MED11** | H | Neurodegen. w/ resp. failure, seizures (NDDRSB) | 620327 | MONDO:0957225 | AR | ❌ **gap** |
| **MED17** | H | Infantile cerebral+cerebellar atrophy / MCPHA | 613668 | MONDO:0013351 | AR | ❌ **gap** |
| **MED20** | H | Infantile basal ganglia degeneration + dystonia | — (gene *612915) | — | AR | ❌ **gap** (provisional) |
| **MED27** | core | NDD w/ spasticity, cataracts, cerebellar hypoplasia (NEDSCAC) | 619286 | MONDO:0859137 | AR | ❌ **gap** |
| **MED25** | T | Basel-Vanagaite-Smirin-Yosef syndrome (BVSYS) | 616449 | MONDO:0014643 | AR | ❌ **gap** |
| **MED23** | T | AR intellectual dev. disorder 18 (MRT18) | 614249 | MONDO:0013651 | AR | ✅ subtype |
| **MED16** | T | Guillouet-Gordon syndrome (GGNS) | 621220 | MONDO:0979227 | AR | ❌ **gap** (new 2025 gene) |

## By module — detail and key PubMed anchors

### CDK8 kinase module (CKM)

**MED12** (Xq13.1) is a single gene producing an allelic *series* — model each as a
distinct entity, not a variant of one syndrome, because the mechanism differs by allele
class (male missense hotspots vs. female loss-of-function). GeneReviews: *MED12-Related
Disorders* (NBK1676; PMID:20301719).
- **FGS1 / Opitz-Kaveggia** — recurrent p.R961W. Discovery **PMID:17334363** (Risheg 2007,
  *Nat Genet*) **NEW to KB**; clinical cohort PMID:19938245 (already cited); behavioral
  PMID:18973276.
- **Lujan syndrome** — p.N1007S. PMID:17369503 (already cited).
- **Shared mechanism** — R961W/N1007S disrupt a Mediator constraint on GLI3-dependent SHH
  signalling: **PMID:23091001** (Zhou 2012, *PNAS*) **NEW to KB**.
- **X-linked Ohdo (MKB type)** — **PMID:23395478** (Vulto-van Silfhout 2013, *AJHG*) **NEW**.
- **Hardikar syndrome** (female-specific, LoF) — **PMID:33244166** (Li 2021, *Genet Med*)
  **NEW**; further delineation PMID:41821414 (Warmoeskerken 2026).
- **Female syndromic NDD** — **PMID:33244165** (Polla 2021, *Genet Med*) **NEW**.
- **X-linked partial epilepsy without ID** — PMID:36894399 (Yang 2023) — newest, benign-end phenotype.
- **Somatic MED12** (exon-2 Q44 gain-of-function; keep architecturally separate from
  germline): uterine leiomyoma PMID:21868628 (Mäkinen 2011, *Science*); also breast
  fibroadenoma, phyllodes tumor, leiomyosarcoma/CRC. dismech already models the somatic
  arm in `Uterine_Leiomyoma.yaml` and `Breast_Fibroadenoma.yaml`.

**MED12L** (3q25.1) — **Nizon-Isidor syndrome**: ID, prominent speech delay, hypotonia,
variable congenital heart defects. Discovery **PMID:31155615** (Nizon 2019, *Genet Med*)
**NEW**; case series + mitotic-instability observation PMID:40838347 (Stewart 2026).

**CDK8** (13q12.13) — **IDDHBA**: de novo kinase-domain missense (hypomorphic); hypotonia,
mild-moderate ID, behavioral abnormalities, facial dysmorphism, congenital heart disease.
Discovery **PMID:30905399** (Calpena 2019, *AJHG*) **NEW**; mechanism PMID:33067521;
phenotype expansion PMID:38193604.

**CDK19** (6q21) — **DEE87**: de novo kinase-domain missense; hypotonia, global delay,
epileptic encephalopathy/infantile spasms. Discovery **PMID:32330417** (Chung 2020, *AJHG*)
**NEW**; LoF/GoF dichotomy PMID:33495529; infantile spasms PMID:33568421.

**MED13 / MED13L** — already well covered in the KB. Useful mechanism additions:
MED13L→cyclin C mislocalization/mitochondrial dysfunction **PMID:35198885** (Chang 2022,
*iScience*) **NEW**; cortical-neurogenesis priming PMID:40775066 (already cited).

### Head module

**MED17** (11q21) — **MCPHA / infantile cerebral and cerebellar atrophy with postnatal
progressive microcephaly**: normal at birth, then postnatal microcephaly, spasticity,
epilepsy, profound psychomotor retardation; MRI cerebral+cerebellar atrophy, poor
myelination. Caucasus-Jewish founder p.L371P. Discovery **PMID:20950787** (Kaufmann 2010,
*AJHG*) **NEW**; milder compound-het siblings PMID:26004231; phenotype expansion
PMID:30345598; founder natural history PMID:33756211; novel allele PMID:36508181.

**MED11** (17p13.1) — **NDDRSB** (lethal): congenital microcephaly, neonatal respiratory
failure, refractory myoclonic seizures, exaggerated startle, progressive neurodegeneration,
premature death; recurrent homozygous C-terminal R109X destabilizes the MED11-MED22-MED17
bundle. Single defining paper **PMID:36001086** (Calì 2022, *Genet Med*) **NEW**.

**MED20** (6q22.31) — infantile basal ganglia degeneration + brain atrophy with
infantile-onset spasticity and childhood-onset dystonia. **Provisional**: one family
(2 sibs, homozygous p.G114Ala); the authors state proof of pathogenicity awaits unrelated
patients. **PMID:25446406** (Vodopiutz 2015, *Eur J Pediatr*) **NEW**. No OMIM phenotype #.

### Structural core

**MED27** (9q34.3) — **NEDSCAC**: global developmental delay, ID, axial hypotonia with
distal spasticity, dystonia, cerebellar hypoplasia; congenital cataracts and seizures in
severe cases. Discovery **PMID:33443317** (Meng 2021, ***Ann Neurol***) **NEW** — note the
syndrome-defining paper is *Ann Neurol*, **not** *Brain*; the *Brain* 2023 paper
(PMID:37517035, "ponto-cerebello-lental degeneration") is the follow-up cohort. Further:
PMID:39296199 (Wu 2024); mechanism PMID:41017421 (Yiliyaer 2025).

### Tail module

**MED25** (19q13.33) — **BVSYS** (eye-intellectual-disability syndrome): severe ID with
eye (cataract, microcornea, coloboma), brain (incl. polymicrogyria), cardiac and palatal
anomalies; founder p.Y39C impairs MED25 incorporation into Mediator. Discovery
**PMID:25792360** (Basel-Vanagaite 2015, *Hum Genet*) **NEW**; p.I173T Lebanese founder
PMID:30800049 / PMID:31602195; delineation PMID:32324310; polymicrogyria PMID:32816121.

**MED23** (6q23.2) — already covered (MRT18). Useful additions: ketogenic-diet-responsive
refractory epilepsy **PMID:27311965** (Lionel 2016, *AJMG A*) **NEW**; genotype-phenotype
PMID:39144687 (Bamaga 2024).

**MED16** (19p13.3) — **Guillouet-Gordon syndrome**: a *new (2025)* Mediator disease gene —
biallelic variants → MCA-ID MEDopathy with craniofacial defects, limb anomalies, and heart
defects (predominantly tetralogy of Fallot). Discovery **PMID:40081376** (Guillouet 2025,
*AJHG*) **NEW**.

## Refuted / provisional / negative associations (curate with care)

- **MED25 → CMT2B2 (Charcot-Marie-Tooth 2B2) is REFUTED.** The original p.A335V
  association (Leal 2009, PMID:19290556) was reassigned by the same group to a homozygous
  *PNKP* variant: **PMID:30039206** (Leal 2018, *Neurogenetics*). CMT2B2 (OMIM 605589) is
  now a *PNKP* disorder. dismech's `Charcot-Marie-Tooth_Disease_Type_2.yaml` currently
  lists "CMT2B2 (MED25)" in passing — this should be corrected (MED25 recorded only as a
  historical/refuted association, or the parenthetical updated to PNKP).
- **MED14** (Xp11.4) — **emerging/provisional**, not an established OMIM phenotype. Two
  single-family X-linked reports: T-B+NK+ immunodeficiency (PMID:35967429, Sertori 2022)
  and a VACTERL-like malformation report (Sertori 2025, *Genes & Diseases* — no PubMed PMID
  at survey time). Curate only as candidate.
- **CCNC (cyclin C)** — **no verified germline neurodevelopmental disorder** despite being a
  core CKM subunit. Its only germline human disease link is a contiguous CCNC+PRDM13
  duplication causing North Carolina macular dystrophy (retinal, not NDD; PMID:28973654,
  already reflected in `North_Carolina_Macular_Dystrophy.yaml`). Cyclin C is mechanistically
  implicated *downstream* of MED13L loss (PMID:35198885), not as a primary disease gene.
  Do **not** create a CCNC NDD entry. Watch for confusion with **CCNK** (cyclin K), a
  *different* gene causing a distinct NDD (PMID:29979980) — not part of the CKM.
- **No established germline Mendelian disease** (report as negatives): MED1, MED15
  (within 22q11.2 del region; somatic RCC fusions only), MED19, MED21, MED22, MED26,
  MED28, MED30, MED31. Guard against **MED31 ≠ MRT31** (OMIM 614329 is a different locus).

## KB action summary

**Already covered:** MED13, MED13L, MED12 (FGS1/Lujan), MED23 — as subtypes of
`kb/disorders/Mediator_Complex_Neurodevelopmental_Disorder.yaml`, plus a dedicated
`MED13_Syndrome.yaml`, and the somatic MED12 tumor arm.

**Recommended additions (this survey acts on the germline neurodevelopmental set):** add
**CDK8, CDK19, MED12L, MED11, MED17, MED20, MED27, MED25 (BVSYS), MED16** as subtypes of the
Mediator grouping entry, and enrich the MED12 subtype with the Ohdo / Hardikar / female-NDD
allelic series and the GLI3-SHH mechanism. All defining PMIDs above marked **NEW** were
fetched and, where cited, snippet-validated.

**Deferred (evidence tier / scope):** MED20 and MED14 are single-family/provisional — MED20
is added with an explicit provisional flag; MED14 is left as a candidate note. MED12 somatic
tumors stay in their existing tumor entries. The MED25-CMT2B2→PNKP correction to
`Charcot-Marie-Tooth_Disease_Type_2.yaml` is flagged here for a follow-up.

## Key references (verified)

FGS1 17334363 · Lujan 17369503 · SHH/GLI3 23091001 · Ohdo 23395478 · Hardikar 33244166 ·
female NDD 33244165 · MED12 epilepsy 36894399 · MED12L/Nizon-Isidor 31155615, 40838347 ·
CDK8 30905399, 33067521, 38193604 · CDK19 32330417, 33495529, 33568421 · MED17 20950787,
26004231, 30345598, 33756211, 36508181 · MED11 36001086 · MED20 25446406 · MED27 33443317,
37517035, 39296199, 41017421 · MED25 BVSYS 25792360, 30800049, 31602195, 32324310, 32816121 ·
MED25→PNKP reassignment 30039206 · MED23 21868677, 27311965, 30847200, 36824420, 39144687 ·
MED16 40081376 · MED13L cyclin C 35198885 · umbrella review (Fazio 2025) 41465117 ·
somatic MED12 21868628.
