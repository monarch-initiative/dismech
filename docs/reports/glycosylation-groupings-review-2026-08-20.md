# Review: Congenital Disorders of Glycosylation (CDG) and Deglycosylation (CDDG) groupings

**Date:** 2026-08-20 · **Scope:** `kb/groupings/Congenital_Disorders_of_Glycosylation.yaml`,
`kb/groupings/Congenital_Disorders_of_Deglycosylation.yaml`, and all their member `Disease`
entries · **Method:** MONDO closure audit (2026-08 release), `just check-groupings`,
`just compliance-weighted`, per-entry section census, and a PubMed sweep (2023–2026).

---

## 1. Headline findings

| # | Finding | Severity |
|---|---|---|
| 1 | **The CDG grouping listed 7 members while the KB held 14 qualifying CDG entries.** Seven curated diseases that satisfy the grouping's own NECESSARY criteria were absent. **Fixed in this change.** | High |
| 2 | The CDDG grouping is **MONDO-complete** (2/2 descendants curated) but holds the two *thinnest* entries in the whole glycosylation family. | Medium |
| 3 | **NGLY1-CDDG is 3 years behind its own literature** — no treatments, no clinical trials, no animal models, and none of the NFE2L1/Nrf1, ENGASE, or AAV9 gene-therapy biology that now defines the field. | High |
| 4 | **MAN2C1-CDDG2 is a single-source entry** (one PMID). A second cohort report published 2026-01 is uncited. | High |
| 5 | **COG1-CDG's evidence is structurally unverifiable**: 50 evidence items cite bare `DOI:` references, which `linkml-reference-validator` skips. All three DOIs resolve to PMIDs. | High |
| 6 | ~~VPS51-PCH-CDG and UGGT1-CDG have no MONDO anchor.~~ **Corrected during follow-up: both terms already existed.** VPS51 disease is `MONDO:0032831` (PCH type 13, causal gene VPS51, xref OMIM:618606 — the same OMIM the entry was seeded from) and UGGT1-CDG is `MONDO:0980705` (CDG type IIcc, causal gene UGGT1). Both are now bound. No term request was needed. | Medium |
| 7 | **Four members** (ALG1, SLC35A2, NGLY1, MAN2C1) do **not** declare `conforms_to` against any module, despite a `congenital_disorder_of_glycosylation` module existing that 12 siblings use. | Medium |
| 8 | **No deglycosylation module exists.** The CDDG pair has nowhere to conform to. | Low |

---

## 2. Membership audit

### 2.1 CDDG — complete

`MONDO:0031376` (congenital disorder of deglycosylation) has exactly **two** `is_a`
descendants in the 2026-08 MONDO release:

| MONDO | Disease | Curated |
|---|---|---|
| `MONDO:0800044` | congenital disorder of deglycosylation 1 (NGLY1) | ✅ |
| `MONDO:0030770` | congenital disorder of deglycosylation 2 (MAN2C1) | ✅ |

**The grouping is MONDO-complete.** That is a statement about the small size of the
concept, not the depth of the entries. This completeness check is now recorded in the
grouping's `notes` so a future reviewer does not have to re-derive it.

### 2.2 CDG — was 7/14, now 14/14

`MONDO:0015286` has **169** `is_a` descendants; 23 KB entries bind one as their primary
`disease_term`. Of those, 14 fall inside this grouping's declared N-glycan boundary. Seven
were missing:

| Added member | Gene | Step | MONDO |
|---|---|---|---|
| ALG1-CDG | ALG1 | first β-1,4-mannosylation of the cytosolic-face LLO (CDG-Ik) | `MONDO:0012052` |
| ALG3-CDG | ALG3 | first luminal-face mannosyltransferase (CDG-Id) | `MONDO:0010998` |
| DPM2-CDG | DPM2 | Dol-P-Man synthase subunit — donor *synthesis* (CDG-Iu) | `MONDO:0014023` |
| MPI-CDG | MPI | GDP-mannose precursor pool (CDG-Ib) — **the treatable CDG** | `MONDO:0011257` |
| PGM1-CDG | PGM1 | UDP-Glc/Gal supply — **mixed type I/II**, galactose-responsive | `MONDO:0013968` |
| SLC35A2-CDG | SLC35A2 | Golgi UDP-galactose transporter (type II), X-linked | `MONDO:0010478` |
| VPS51-PCH-CDG | VPS51 | GARP/EARP retrograde tether → Golgi enzyme positioning | *none* |

All 14 members now return `SATISFIED` against the NECESSARY criteria with no
contradictions (`just check-groupings`).

Twelve of these fourteen already declared `conforms_to` against the
`congenital_disorder_of_glycosylation` module — so the module graph knew they were CDG
while the grouping did not. That divergence is the cleanest signal that the omission was
drift, not a boundary decision.

### 2.3 Boundary — deliberately narrower than the modern CDG nosology

The 2024–2026 CDG literature treats CDG as spanning N-linked, O-linked, GPI-anchor, and
glycosphingolipid defects (>190 genes). This grouping's NECESSARY criteria are
N-glycan-specific (`GO:0006487` OR `GO:0006491`). **Keep that boundary** — the wider
concepts are already held by siblings, so nothing is lost:

| Concept | Where it lives |
|---|---|
| GPI-anchor defects (Mabry/PIGV, CHIME/PIGL, PNH, MCAHS2) | `Disorders_of_GPI_Anchor_Biosynthesis` |
| Precursor-supply / ER-QC multi-pathway (UGDH, UGP2, UGGT1) | `Other_Multiple_Glycosylation_Pathway_Disorders` |
| Folded-TSR O-fucose/glucose QC (Peters plus, Geleophysic) | `tsr_o_glycosylation_quality_control` module |
| Dystroglycan O-mannosylation | `Dystroglycanopathy` entry |

This is now written into `grouping_rationale` so the next reviewer sees why a "missing"
CDG is not missing. **UGGT1-CDG was deliberately not dual-listed** here; it is an ER
re-glucosylation quality-control defect and the sibling grouping is the better home.

---

## 3. Member-by-member completeness

Compliance is the weighted `just compliance-weighted` score. `refs` counts distinct
literature identifiers, not evidence items.

| Member | Lines | Compliance | refs | conforms_to | Tx | Dx | Prev | Trials | Models | Verdict |
|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---|
| COG1-CDG | 1674 | 99.6% | 1 PMID + 50 DOI + 43 ORPHA | ✅ | 3 | 1 | 1 | 0 | 0 | **evidence base unverifiable** |
| ALG12-CDG | 1687 | 99.5% | 8 | ✅ | 1 | 3 | 1 | 1 | 0 | solid |
| ALG9-CDG | 1624 | 99.5% | 8 | ✅ | 0 | 3 | 1 | 1 | 0 | solid; no treatments |
| COG7-CDG | 1436 | 99.5% | 5 | ✅ | 1 | 2 | 0 | 1 | 0 | solid |
| ALG1-CDG | 1322 | 98.9% | 18 | ❌ | 2 | 3 | 1 | 0 | 0 | wire to module |
| MGAT2-CDG | 1029 | 98.7% | 3 | ✅ | 2 | 2 | 0 | 0 | 0 | thin sourcing |
| SLC35A2-CDG | 539 | 96.6% | 10 | ❌ | 3 | 0 | 0 | 2 | 0 | **thin; fast-moving field** |
| MPDU1-CDG | 1367 | 96.4% | 5 | ✅ | 3 | 2 | 0 | 0 | 0 | adequate |
| MPI-CDG | 2446 | 95.8% | 14 | ✅ | 10 | 3 | 2 | 1 | 2 | **best in group** |
| VPS51-PCH-CDG | 523 | 94.7% | 3 | ✅ | 0 | 0 | 0 | 0 | 0 | thin; no MONDO |
| NGLY1-CDDG | 365 | 92.9% | 5 | ❌ | 0 | 0 | 0 | 0 | 0 | **badly out of date** |
| MAN2C1-CDDG2 | 225 | 91.2% | 1 | ❌ | 0 | 0 | 0 | 0 | 0 | **single-source** |
| UGGT1-CDG* | 825 | 90.5% | — | ❌ | 1 | 4 | 0 | 0 | 2 | no MONDO ID |
| DPM2-CDG | 2115 | 90.6% | 14 | ✅ | 5 | 3 | 1 | 0 | 0 | good |
| PGM1-CDG | 2770 | 90.4% | 20 | ✅ | 13 | 3 | 1 | 2 | 0 | **richest; needs 2026 update** |
| ALG3-CDG | 1234 | 83.4% | 10 | ✅ | 5 | 3 | 1 | 0 | 0 | lowest score in group |

\* UGGT1 sits in the sibling grouping, listed here for completeness.

**Cross-cutting gaps.** Zero `datasets:` records anywhere in either grouping. Only MPI-CDG
and UGGT1-CDG carry any model system, despite a 2025 systematic review of zebrafish CDG
models (`PMID:40993721`) and a new hypomorphic *Mpi* mouse (`PMID:40693465`). Only four
of sixteen entries carry `classifications:`.

**The compliance score is misleading here.** COG1-CDG scores 99.6% — the highest in the
group — while resting on one PMID and fifty DOI-cited snippets that no validator ever
checks. Compliance measures *field coverage*, not *evidence verifiability*.

---

## 4. Latest publications (2023–2026) and what each would change

### 4.1 NGLY1 — the largest gap in either grouping

The entry cites 5 references, the newest from 2019. Since then:

| PMID | Year | What it establishes | Would populate |
|---|---|---|---|
| `41468431` | 2026 | **NFE2L1/Nrf1 sequence editing.** NGLY1 converts glycosylated Asn→Asp in Nrf1; editing of Asn574 is required for HCF-C1/OGT binding, chromatin binding, and proteasome-subunit gene expression; other sites drive CREBBP/EP300 coactivator recruitment. | A whole missing `pathophysiology` arm: deglycosylation failure → Nrf1 activation failure → proteasome bounce-back failure |
| `41721346` | 2026 | **Aging Ngly1⁻/⁻ rat.** ~50% dead or euthanized by 9–10 months; ~92% ↓ rotarod latency, ~82% ↓ rearing; widespread neuroinflammation; loss of peripheral axons and spinal motor neurons. | `animal_models` with `modeled_mechanisms` + readouts; supports a *progressive neurodegeneration* node the entry lacks |
| `41176936` | 2025 | **AAV9-hNGLY1 ICV in Ngly1⁻/⁻ rats** suppresses non-epileptic convulsions but **fails** to correct EEG abnormalities or sleep fragmentation. | `treatments` + a `FAILS_TO_RECAPITULATE`/partial-rescue model link; an honest negative result |
| `40687377` | 2025 | IND-enabling preclinical pharmacology/safety for an AAV9 NGLY1 gene-therapy trial. | `treatments`, `clinical_trials` |
| `42114141` | 2026 | **Prospective natural history**, 15 participants (~10% of the known population): widening developmental gap, GlcNAc-Asn (GNA) elevated in all. | `progression`, `biochemical` (the entry has aspartylglycosamine but not the GNA endpoint framing), trial-endpoint context |
| `42361657` | 2026 | **Multicenter cohort, 15 patients / 11 families.** Abnormal EEG 10/15, seizures 9/15, hyperkinetic movement 8/15, feeding difficulty 9/15, scoliosis 7/13, hypo-/alacrima 6/15, transaminase elevation 12/14 (transient in 9/12), **low total cholesterol 7/10 and low HDL 5/10**; two novel variants. | Frequency bands for existing phenotypes; **new phenotypes**: scoliosis, feeding difficulty, auditory neuropathy, hypolipidemia |
| `40773511` | 2025 | Natural **SEL1L** variants rescue an NGLY1-deficiency model and modify ERAD function. | Genetic modifier / `discussions` |
| `28426790` | 2017 | *Engase* deletion partially rescues Ngly1⁻/⁻ mouse lethality. | The canonical modifier axis — **absent from the entry** |
| `40643555` | 2025 | Structure–function of NGLY1 pathogenic variants. | `genetic` variant-level detail |
| `41229635` | 2025 | Tofacitinib improved motor symptoms in parkinsonism with a *heterozygous* NGLY1 variant + autoimmunity (see also `42052850` on NGLY1 in immune function). | `treatments` — but note this is a heterozygote, not classical CDDG; curate as a discussion, not a disease treatment |
| `41917400`, `41096971`, `40730667`, `40602583` | 2025–26 | Four reviews of NGLY1 biology and therapeutic strategy. | Orientation for the rebuild |

The mouse/rat divergence (mouse null embryonically lethal on C57BL/6, rat viable but
progressively degenerating) is a textbook `HUMAN_MODEL_MISMATCH` discussion that the entry
does not carry.

### 4.2 MAN2C1

| PMID | Year | Note |
|---|---|---|
| `41623318` | 2026 | **Second report.** Novel pathogenic MAN2C1 variant *in trans* with a 15q24.1q24.3 microdeletion — the only patient described since the founding cohort. Directly addresses this entry's single-source problem. |
| `37486637` | 2023 | Exome sequencing in polymicrogyria — independent support for the polymicrogyria phenotype the entry cites from one paper. |

### 4.3 CDG members

| PMID | Year | Relevance |
|---|---|---|
| `41807832` | 2026 | **Cryo-EM structures of ALG3/9/12** reconstituting all four mannosylation steps; explains donor selection (Dol-P-Man over Dol-P-Glc) and gives "mechanistic explanations for enzyme dysfunction in CDGs". Directly upgrades the molecular node in **three** members at once. |
| `42269412` | 2026 | **Recurrent HLH in COG deficiency** (COG6/COG7): 3 patients, plus ~40% of published COG patients had unexplained febrile episodes; corticosteroids mitigated neurological impact. A clinically actionable phenotype+treatment absent from COG7-CDG. |
| `42511652` | 2026 | Comprehensive MS N-glycan profiling for CDG type II subtyping — `diagnosis` for MGAT2/COG1/COG7/SLC35A2. |
| `41718976` | 2026 | Review: COG complex in Golgi trafficking and glycosylation. |
| `41867720` | 2026 | **SLC35A2: disrupted O-GalNAc glycosylation** as mechanism *and* biomarker. Mouse forebrain knockout shows a specific O-GalNAc defect (other galactosylated glycoconjugates intact); truncated O-GalNAc glycans on ECM molecules; variant burden correlates with truncation in human epilepsy tissue. Reframes SLC35A2 disease from generic hypogalactosylation to a specific O-glycan lesion. *(Preprint — flag as such.)* |
| `41373710` | 2025 | Review: SLC35A2-related brain disorders — genetics, pathophysiology, therapeutics. |
| `42542984`, `42216953`, `42168328` | 2026 | MOGHE (mild MCD with oligodendroglial hyperplasia) — the somatic-mosaic brain-limited arm of SLC35A2, including Y-chromosome mosaicism and snRNA-seq oligodendrocyte dysregulation. The SLC35A2 entry has no `has_subtypes` for the germline vs somatic-mosaic split. |
| `41723528` / `40631269` | 2026 / 2025 | **PGM1 cardiomyopathy is glycosylation-independent**: patient iPSC-cardiomyocytes show Z-disk depletion via a predicted PGM1–LDB3 (ZASP/Cypher) interaction plus mitochondrial protein loss — explaining why galactose corrects glycosylation but not cardiac disease. A major mechanistic addition. |
| `40242152` | 2025 | Creatine supplementation outcomes in PGM1-CDG. |
| `41018607` | 2025 | LC-MS hexose-phosphate resolution → new PGM1-CDG pathophysiology. |
| `41099230`, `41306474` | 2025–26 | PGM1-CDG misdiagnosed as Laron syndrome; ASD closure for refractory heart failure. |
| `42376639`, `41172867` | 2025–26 | **Two pregnancy-management reports in MPI-CDG**, including oral D-mannose through pregnancy. |
| `40962549` | 2025 | D-mannose treatment outcomes in 5 children with MPI-CDG. |
| `40693465` | 2025 | Hypomorphic *Mpi* mouse — an in vivo tool for global N-glycosylation deficiency. |
| `39984963`, `38876156`, `38717015` | 2024–25 | ALG12-CDG: novel intronic variant with low mRNA; Duane syndrome association; expanded prenatal phenotype incl. bilateral multicystic kidneys. |
| `38831602`, `36755425` | 2023–25 | MPDU1: erythrokeratodermia variabilis presentation; severe ciliopathy-like phenotype. |
| `40902550` | 2025 | Review: genetic disorders of dolichol synthesis and utilization — covers DOLK and MPDU1. |
| `38597022` | 2024 | ALG3-CDG: deficient glycan extension **and ER stress** — a second mechanistic arm. |
| `40743674` | 2025 | **Multi-omics across six CDG** (incl. NGLY1-CDDG and PGM1-CDG): shared disruption of autophagy, vesicle trafficking, and mitochondrial function; EMUDRA-predicted repurposable drug classes. The strongest argument yet for shared module-level biology. |
| `40993721` | 2025 | Systematic review of zebrafish CDG models. |
| `40868218`, `41713138` | 2025–26 | Clinical glycomics/glycoproteomics for CDG; **albumin as a glycoprotein biomarker**. |
| `41554664` | 2026 | CDG due to defective membrane transporters: update — covers SLC35A2. |
| `40119203`, `39236565` | 2024–25 | Diagnostic and therapeutic approaches in CDG; treatment overview. |

**Two literature items to *not* curate as-is.** `42537239` ("COG7 links Golgi integrity to
stress signaling and senescence") is an *Arabidopsis thaliana* study — interesting for the
module, not evidence for human COG7-CDG. `41229635` (tofacitinib) concerns a *heterozygous*
NGLY1 carrier with autoimmune disease, not biallelic NGLY1-CDDG.

---

## 5. Knowledge gaps worth recording as `discussions`

1. **NGLY1: which substrate explains the phenotype?** Nrf1 sequence editing is now
   mechanistically resolved (`41468431`), but no one has shown that Nrf1/proteasome failure
   accounts for alacrima, the movement disorder, or the neuropathy. `KNOWLEDGE_GAP`.
2. **NGLY1: mouse vs rat vs human.** Ngly1⁻/⁻ mice are embryonically lethal on C57BL/6 and
   rescued by *Engase* deletion; rats survive and degenerate progressively; humans have a
   ~13-year median lifespan. `HUMAN_MODEL_MISMATCH`.
3. **NGLY1: gene therapy's partial rescue.** AAV9-hNGLY1 suppressed convulsions without
   correcting EEG or sleep (`41176936`). Curating gene therapy as "effective" would
   overstate the evidence — record the dissociation.
4. **PGM1: two independent disease mechanisms.** Galactose corrects glycosylation;
   cardiomyopathy persists via a Z-disk/mitochondrial axis (`41723528`). This is a
   competing-`mechanistic_hypotheses` shape, not one chain.
5. **SLC35A2: germline hypogalactosylation vs somatic-mosaic O-GalNAc/MOGHE.** Arguably two
   diseases sharing a gene. Needs `has_subtypes` before it needs more phenotypes.
6. **COG deficiency and immune dysregulation.** Why does a Golgi trafficking defect produce
   HLH in ~40% of patients (`42269412`)? Unexplained.
7. **MAN2C1: is free-oligosaccharide accumulation causal?** The founding cohort shows
   accumulation and a phenotype; nothing connects them. The entry's own
   `INDIRECT_UNKNOWN_INTERMEDIATES` edge already admits this — it should be an explicit
   `KNOWLEDGE_GAP` with proposed experiments.
8. **Is there a shared CDG therapeutic axis?** `40743674` finds autophagy, vesicle
   trafficking, and mitochondrial dysfunction shared across six CDG. If it holds, it belongs
   in the `congenital_disorder_of_glycosylation` module, not in six disorder entries.

---

## 6. Recommended follow-up work, in priority order

| # | Action | Why now |
|---|---|---|
| 1 | **Rebuild NGLY1-CDDG** from the 11 references in §4.1 — pathophysiology (Nrf1 arm), treatments, clinical trials, animal models, progression, two discussions. | Biggest single gap; the field moved and the entry did not |
| 2 | **Add the 2026 MAN2C1 report** (`41623318`) so CDDG2 is no longer single-source. | Cheap; removes a structural fragility |
| 3 | **Convert COG1-CDG's 50 `DOI:` references to PMIDs** — `10.1111/cge.13980`→`PMID:33960418`, `10.1186/s12887-021-02922-7`→`PMID:34625039`, `10.1073/pnas.0507685103`→`PMID:16537452` — then re-run `just validate-references`. | 50 evidence snippets currently bypass validation entirely |
| 4 | Add `conforms_to: congenital_disorder_of_glycosylation#…` to ALG1-CDG and SLC35A2-CDG. | Two-line fix; they already satisfy the criteria |
| 5 | Add COG HLH phenotype + corticosteroid prophylaxis to COG7-CDG (`42269412`). | Clinically actionable |
| 6 | Split SLC35A2-CDG into germline and somatic-mosaic/MOGHE subtypes. | Three 2026 papers on the mosaic arm alone |
| 7 | Add the glycosylation-independent cardiomyopathy arm to PGM1-CDG (`41723528`). | Changes what "treated" means for the group's flagship treatable disease |
| 8 | Raise MONDO term requests for **VPS51-related PCH-CDG** and **UGGT1-CDG**. | Both entries are stuck without an ontology anchor |
| 9 | Consider a `cytosolic_deglycosylation` module so the CDDG pair has a conformance target. | The two members share a substrate pool and currently share nothing structural |
| 10 | Add `datasets:` to MPI-CDG and PGM1-CDG (the two with real cohort/omics data). | Zero dataset coverage across both groupings |

---

## 6a. Follow-up: all ten recommendations applied (2026-08-20)

Sections 4 through 6 were written as recommendations. They were subsequently
carried out in full. What follows is what was actually done, including the two
places where doing the work changed the finding.

| # | Recommendation | Outcome |
|---|---|---|
| 1 | Rebuild NGLY1-CDDG | **Done.** 365 → 1,614 lines. Two new pathophysiology nodes (ENGase bypass / GlcNAc-Asn accumulation; failed NFE2L1 sequence editing), 9 new phenotypes with frequency bands from the 2026 cohort, the GNA biomarker as a structured `biochemical` readout, `prevalence`, `progression`, 2 treatments (GS-100 gene therapy with `target_mechanisms`; GlcNAc for alacrima), 3 clinical trials, 3 animal models with `modeled_mechanisms` and readouts, the SEL1L modifier and the recurrent Arg401* allele, 2 GEO datasets, and 3 discussions. |
| 2 | Add the 2026 MAN2C1 report | **Done.** `PMID:41623318` and `PMID:37486637` added; the entry is no longer single-source. A `KNOWLEDGE_GAP` on free-oligosaccharide causality and a note on the 15q24 compound genotype were added with it. |
| 3 | Convert COG1-CDG's DOI references | **Done.** All 50 `DOI:` references converted to `PMID:33960418`, `PMID:34625039`, `PMID:16537452`. On first validation 101 of 103 snippets verified — the curator's DOI-cited quotes had been accurate all along, just unverifiable. The 2 failures were one quote spanning a bracketed HGVS span (`[Arg889Profs*12]`), which the validator strips; it was shortened to a verbatim span that does not cross the bracket. Now 103/103. |
| 4 | `conforms_to` for ALG1 and SLC35A2 | **Done.** ALG1 at three nodes, SLC35A2 at two (the terminal node was left unconformed — SLC35A2 disease is brain-predominant, not multisystem glycoprotein dysfunction). |
| 5 | COG7 HLH arm | **Done.** New pathophysiology node, 2 phenotypes (hemophagocytosis; recurrent unexplained fever at FREQUENT, from the ~40% literature figure), corticosteroid prophylaxis as a treatment with `target_mechanisms`, and a `KNOWLEDGE_GAP` on the unexplained glycosylation-to-immune-dysregulation link. |
| 6 | Split SLC35A2 into subtypes | **Done.** `Germline` and `Somatic MOGHE`. Four phenotypes that depend on body-wide transporter deficiency (transferrin profile, skeletal, dysmorphic, failure to thrive) are tagged to `Germline`; shared phenotypes are deliberately left untagged. A `KNOWLEDGE_GAP` records the O-GalNAc reframing as an unreplicated preprint rather than curating it as mechanism. |
| 7 | PGM1 cardiomyopathy arm | **Done.** New `Z-Disk Destabilization via Loss of PGM1-LDB3 Interaction` node; the existing `galactose_resistant_cardiomyopathy` hypothesis extended with arm (c) and its human-cardiomyocyte evidence; the patient iPSC-cardiomyocyte model added as an `experimental_models` entry with two mechanism links and three readouts. |
| 8 | MONDO term requests | **Not needed — the finding was wrong.** Both terms already exist. `MONDO:0032831` (pontocerebellar hypoplasia type 13) xrefs `OMIM:618606`, the same OMIM this entry was seeded from, and records VPS51 as its causal gene; `MONDO:0980705` (CDG type IIcc) records UGGT1. Both are now **bound** rather than requested. The original finding repeated each entry's own stale note; the earlier VPS51 audit had rejected PCH1A correctly but not gone on through the numbered PCH series. One real upstream gap survives: `MONDO:0032831` sits under pontocerebellar hypoplasia, not under CDG, so VPS51-PCH-CDG is a grouping member without being a descendant of the mapped class. That is a much smaller MONDO ask than a new term. |
| 9 | `cytosolic_deglycosylation` module | **Done.** Five nodes, registered in `CLAUDE.md`, with both CDDG entries wired as conformers. The central node is named *Cytosolic Glycan Catabolite Dysregulation* rather than for free oligosaccharides: MAN2C1 accumulates free oligosaccharides but NGLY1 accumulates a glycoasparagine, and naming it for the pool lets both arms attach without either overstating its catabolite. The NFE2L1 sequence-editing branch is fenced off as NGLY1-only. |
| 10 | Datasets for MPI-CDG and PGM1-CDG | **Partly done, and the negative result is the finding.** Neither disease has a relevant public dataset: `just discover-datasets` returned only `GENE_ONLY` gene-symbol collisions (yeast *PGM1* deletion compendia; a Burkitt lymphoma methylation series and an unrelated liver-fibrogenesis "MPI MT" series), and direct GEO searches for `PGM1-CDG`, `PGM1 deficiency`, `MPI-CDG`, and `MPI deficiency glycosylation` all return zero series. Adding any of them would be Named Entity Confusion reached through dataset search. Both entries now record the search and its date in `notes` and keep `datasets: []`. Four genuinely relevant datasets were found and added elsewhere in the same groupings — `GSE301626` and `GSE295078` to NGLY1, `GSE318030` and `GSE284073` to SLC35A2 — all four resolved by `just verify-datasets`. |

**Two findings changed on contact with the work.** Recommendation 8 dissolved: the
ontology gap did not exist, and the review had propagated the entries' own stale
notes instead of checking MONDO. Recommendation 10 inverted: the gap is real but
unfixable for those two diseases, and the honest output is a recorded negative
search rather than a filled field.

**Validation of the applied work.** `just validate-disorders` over all ten changed
disorder files — the exact command CI runs — passes: 10 files, all validations
passed, **728/728 snippets verified**. Across the ten disorder files plus the new
module, `just count-verified-snippets` reports **744/744**. `just validate` and
`just validate-terms` pass individually on every changed file;
`just validate-grouping` passes on both groupings; `just check-duplicate-keys`
passes over all 4,249 YAML files; `just check-title-snippets` reports no new
title-quoting snippets; `just verify-datasets` resolves all four new accessions;
every `conforms_to` reference in the repository resolves to a real module node.

---

## 7. What this change actually did

**Changed:**

- `kb/groupings/Congenital_Disorders_of_Glycosylation.yaml` — added 7 members with
  `differentiating_mechanisms`; rewrote `grouping_rationale` to state the N-glycan boundary
  and name the sibling groupings that hold the rest; corrected the MONDO consistency note
  from "All 7 listed members" to the verified 13-of-14 with the VPS51 exception explained;
  extended `notes` with the type I/II/mixed axis and the treatability axis.
- `kb/groupings/Congenital_Disorders_of_Deglycosylation.yaml` — recorded the MONDO
  completeness check and the shared free-oligosaccharide-pool rationale in `notes`.
- `cache/hgnc/terms.csv` — one row (`hgnc:7216` MPI) added by the term validator.

**Not changed:** no `kb/disorders/` entry was edited. Everything in §4–§6 is a
recommendation, not an applied change — those need the full fetch-and-verify evidence
workflow, not a review pass.

**Validation run:**

```
just validate-grouping kb/groupings/Congenital_Disorders_of_Glycosylation.yaml    ✅
just validate-grouping kb/groupings/Congenital_Disorders_of_Deglycosylation.yaml  ✅
just check-groupings   kb/groupings/Congenital_Disorders_of_Glycosylation.yaml    ✅ 14/14 SATISFIED, 0 contradictions
just validate-terms    kb/groupings/Congenital_Disorders_of_Glycosylation.yaml    ✅
just check-duplicate-keys (both files)                                            ✅
just check-term-cache-integrity                                                   ✅
just validate-history-all                                                         ✅ 5825 records
just normalize-cache                                                              ✅
```

The grouping member foreign-key check was run as a direct script applying the same rule
as `tests/test_data.py::test_grouping_member_foreign_keys` (every `members[].member` of
type DISEASE/SUBTYPE must resolve to a `Disease.name` or `has_subtypes[].name`): 5,030
names indexed, 14 CDG members and 2 CDDG members, **zero failures**. The pytest node
itself was not run to completion here — building its `_disease_names()` index over
`kb/disorders/` takes several minutes in this environment — so CI remains the
authoritative run of that test.

Literature identifiers in this report were resolved through the PubMed E-utilities API and
titles/abstracts read directly; **they have not been fetched into `references_cache/` or
snippet-verified**, because none of them is cited as evidence in a KB entry yet. Any
curator acting on §4 must run `just fetch-reference` and `just count-verified-snippets`
before committing a snippet.
