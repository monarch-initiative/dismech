# LOINC Tranche D Closing Ledger: Enzyme Activity and Metabolite Assays

**Date:** 2026-10-16
**Scope:** `projects/LOINC_DIAGNOSTICS.md` Phase 3, Tranche D — lysosomal-storage
and inborn-error-of-metabolism groupings, bounded by `kb/disorders/` entries
already carrying an enzyme-deficiency or metabolite-storage mechanism.
**PRs:** #14481, #14491, #14494, #14561, #14617 (all open, none merged as of
2026-10-16 — every "already bound on the sibling entry" fact below is
cross-branch, not cross-`main`, as of that date, and should be re-checked
against `origin/main` once any of these PRs lands).

## Census: entries examined and their outcome

| Entry | Outcome | Code / reason |
|---|---|---|
| Fabry_Disease | Bound | `LOINC:LP14012-6` Alpha galactosidase A |
| Gaucher_Disease | Bound | `LOINC:LP15604-9` Glucosylceramidase |
| Tay-Sachs_Disease | Bound | `LOINC:LP14296-5` Beta-N-acetylhexosaminidase.A |
| Infantile-Onset_Pompe_Disease | Bound | `LOINC:LP14013-4` Acid alpha glucosidase; `LOINC:55827-0` DBS activity |
| Metachromatic_Leukodystrophy | Bound | `LOINC:LP14023-3` Arylsulfatase A |
| Niemann-Pick_Disease_Type_A | Bound | `LOINC:LP14035-7` Acid sphingomyelinase |
| Niemann-Pick_Disease_Type_B | Bound | `LOINC:LP14035-7` Acid sphingomyelinase |
| Sandhoff_Disease | Bound | `LOINC:LP14022-5` Beta-N-acetylhexosaminidase (plain, total A+B) |
| Krabbe_Disease_Due_To_Saposin_A_Deficiency | Bound | specimen-specific galactosylceramidase fibroblast codes (not the Part code `LP14027-4`, per that entry's own notes) |
| Farber_Disease | **Declined** | no LOINC code exists for acid ceramidase / ASAH1 / C26-ceramide |
| Attenuated_Mucopolysaccharidosis_Type_I | Bound | `LOINC:LP14016-7` Alpha-L-iduronidase |
| Sanfilippo_syndrome | Bound (4-way split) | `LOINC:LP14028-2` (IIIA, sulfamidase), `LOINC:LP21324-6` (IIIB, alpha-N-acetylglucosaminidase), `LOINC:LP14461-5` (IIIC, acetyl-CoA transferase), `LOINC:LP14033-2` (IIID, N-acetylglucosamine-6-sulfatase) |
| Alpha_Mannosidosis | Bound | `LOINC:LP14014-2` Alpha-mannosidase |
| Beta_Mannosidosis | Bound | `LOINC:LP14020-9` Beta-mannosidase |
| Mucopolysaccharidosis | **Declined** | grouping-level entry; no single enzyme to bind |
| Tay-Sachs_Disease_AB_Variant | Bound | `LOINC:LP14296-5` (the HexA assay the row performs; GM2A activator codes exist but no cited activator assay is run) |
| Gaucher_Disease_Due_To_Saposin_C_Deficiency | Bound | `LOINC:LP15604-9` (the glucocerebrosidase assay the row performs; saposin-C activator codes exist but no cited activator assay is run) |
| Kanzaki_Disease | Bound | `LOINC:LP14015-9` Alpha-N-acetylgalactosaminidase |
| Late-Onset_Pompe_Disease | Bound | `LOINC:LP14013-4` + `LOINC:55827-0`, reused from Pompe_Disease.yaml |
| Chronic_Neurovisceral_Acid_Sphingomyelinase_Deficiency | Bound | `LOINC:LP14035-7` Acid sphingomyelinase |
| Carbonic_Anhydrase_VA_Deficiency | **Declined** | diagnosis is a multi-analyte metabolic panel plus CA5A sequencing, none of it CA-VA-specific; no LOINC code for CA-VA/CA5A exists, and the biotinidase mention is a differential (multiple carboxylase deficiency) |
| DTYMK-Related_Neurodegeneration | **Declined** | dTMPK fibroblast assay is explicitly "a research method, not a clinical service"; no LOINC code exists |
| Autosomal_Recessive_Non-Syndromic_Intellectual_Disability | **Declined** | biotinidase mention is inside a normal newborn-screening exclusion panel |
| Christianson_Syndrome | **Declined** | hexosaminidase mention is a `MODEL_ORGANISM` mouse-histochemistry finding, not a human test; diagnosis is SLC9A6 sequencing |
| Combined_Saposin_Deficiency | **Declined** | arylsulfatase A mention is in the MLD differential; own biochemical finding (IHC saposin panel) has no LOINC code; PSAP gene codes exist only at method-specific granularity |
| Schindler_Disease | Bound | `LOINC:LP14015-9`, same Part code as allelic Kanzaki disease |
| Sea-Blue_Histiocyte_Syndrome | Bound | `LOINC:LP14035-7`; verified the row is this entry's own secondary-cause workup, not a differential mention |
| Maroteaux-Lamy_syndrome | **Declined** | no `diagnosis:` section; only biochemical marker is the dermatan sulfate substrate; no Part-level LOINC code exists for arylsulfatase B (only specimen-specific codes) |
| Mucopolysaccharidosis_type_X | **Declined** | entry's own text: "There is no clinically available ARSK enzyme assay"; no LOINC code for ARSK exists |
| X-linked_Chondrodysplasia_Punctata_1 | **Declined** | entry's own evidence: "Testing of ARSL enzymatic activity is not currently available on a clinical basis" |
| Kufor-Rakeb_syndrome | **Declined** | glucocerebrosidase mention is a mechanism claim on an iPSC/cell-line biochemical marker explicitly flagged "not established as a routine clinical diagnostic biomarker"; no `diagnosis:` section |
| EDEM3-Congenital_Disorder_of_Glycosylation | **Declined** | "mannosidase" names the gene's own enzymatic identity, not a measured analyte; the real diagnostic test (plasma N-glycan ratio profiling) has no LOINC code |
| MOGS-Congenital_Disorder_of_Glycosylation | **Declined** | "mannosidase" is mechanism prose for the compensatory bypass pathway; the entry's own `notes:` already correctly states no LOINC code exists for the diagnostic analyte (urinary Glc3Man), verified independently |
| Action_Myoclonus-Renal_Failure_Syndrome | **Declined** | the entry's own diagnosis row states a leukocyte glucocerebrosidase assay "must not be used to exclude the diagnosis" (tissue-specific mistrafficking can give a false-normal result); diagnosis is SCARB2 sequencing |
| Hereditary_Spastic_Paraplegia_46 | **Declined** | a genuine GBA2 activity diagnosis row exists, but GBA2 is a distinct non-lysosomal enzyme from GBA1 (classic Gaucher glucocerebrosidase); no GBA2-specific LOINC code exists, and reusing the GBA1 code would misidentify the analyte |
| Autosomal_Recessive_Cerebellar_Ataxia_With_Late_Onset_Spasticity | **Declined** | same GBA2/GBA1 situation as SPG46 — this entry states it is the same biallelic GBA2 disease spectrum |
| Hypertrophic_Cardiomyopathy_21 | **Declined** | alpha-galactosidase A mention is a Fabry phenocopy-exclusion test, explicitly stated to reclassify the patient *out* of this entry if positive; the entry itself has no identified gene or biochemical marker |
| SLC5A6-Related_Multivitamin_Transporter_Deficiency | **Declined** | biotinidase activity is explicitly an exclusion finding — normal/near-normal biotinidase is what distinguishes this disease *from* biotinidase deficiency, which it mimics |
| Spinal_Muscular_Atrophy_Progressive_Myoclonic_Epilepsy | **Declined** | genuine diagnostic marker (acid ceramidase activity / C26-ceramide, ASAH1), but no LOINC code exists — same absence as the allelic Farber_Disease entry |

Every code above was read directly from the branch that carries it
(`origin/loinc-d-batch1` through `loinc-d-batch4`, and `loinc-d-batch6`) in
the same step this table was written, not from an earlier summary.

Across 39 entries examined, 20 bindings landed and 19 declines were recorded
with a stated reason. That ratio is itself informative: this tranche's
entries disproportionately describe tests by their *absence* (a research-only
assay, a method that exists but carries no LOINC identity code, an enzyme
that must not be used diagnostically) rather than by a clean clinical test
with an obvious code.

## Finding 1: the candidate filter's false-positive rate

The candidate pool for this tranche was built by matching lysosomal/IEM enzyme
names against `kb/` text. Two successive filters were tried, and both
over-matched in a tranche-specific way:

- **Whole-file matching** (tranche D batch 5): every one of five candidates
  was a false positive, and each failed for a different reason. Biotinidase
  sat in a differential or a normal-exclusion panel on three entries —
  `Carbonic_Anhydrase_VA_Deficiency`, `DTYMK-Related_Neurodegeneration`, and
  `Autosomal_Recessive_Non-Syndromic_Intellectual_Disability` — plus an
  enzyme name inside a `MODEL_ORGANISM` mouse-histochemistry finding
  (`Christianson_Syndrome`) and an enzyme named only in another disease's
  differential-diagnosis block (`Combined_Saposin_Deficiency`). None was the
  entry's own test.
- **Section-scoped matching** (`diagnosis:`/`biochemical:` only, tranche D
  batch 6 onward): better, but still not clean. Two of the batch-5 entries
  already declined above — `Autosomal_Recessive_Non-Syndromic_Intellectual_Disability`
  and `DTYMK-Related_Neurodegeneration` — kept resurfacing as candidates even
  under the improved filter, because their biotinidase mention genuinely sits
  *inside* a `diagnosis:` section — as a normal exclusion panel, not as the
  entry's own positive finding. Section membership does not distinguish
  "this section names the test that diagnoses this disease" from "this
  section names a test that was run and came back normal, ruling out
  something else." (Both batch-7 declines — `Kufor-Rakeb_syndrome` and the
  eight other entries in that batch — are a separate set; neither
  `Autosomal_Recessive_Non-Syndromic_Intellectual_Disability` nor
  `DTYMK-Related_Neurodegeneration` is among them.)

**The recommendation for whoever extends this tranche:** filter the
candidate pool on the enzyme appearing as a *measured analyte* — a
`biomarker_term`, a `measurements` row, or a named assay with its own
evidence — not on the word appearing anywhere in a section. That distinction
cannot be made by string matching alone; every one of the 19 declines above
needed the row read in context (whose test is this, and does the row's own
evidence describe a result for *this* disease or for the thing it is being
distinguished from).

## Finding 2: enzyme-family name collisions that validate perfectly while being wrong

Two gene/enzyme families in this tranche share a name stem across genuinely
different molecular entities, and binding the wrong family member's code
validates perfectly while being wrong.

- **ARSA / ARSB / ARSE (ARSL) / ARSK.** Four distinct arylsulfatases, and the
  four entries that depend on them took four different paths. ARSA has a
  Part-level identity code (`LOINC:LP14023-3`, bound on
  `Metachromatic_Leukodystrophy`). ARSB (Maroteaux-Lamy syndrome) has **no**
  Part-level code at all — only specimen-specific result codes exist, and
  `Maroteaux-Lamy_syndrome` was declined on that basis, with no `diagnosis:`
  section to attach even a specimen-specific code to. Searched and confirmed
  **no** code exists at any granularity for ARSE/ARSL
  (`X-linked_Chondrodysplasia_Punctata_1`) or ARSK
  (`Mucopolysaccharidosis_type_X`). A search for "arylsulfatase" without the
  letter suffix returns only ARSA and ARSB/ARSC hits — it will not surface
  the absence of ARSE/ARSK coverage, so a future search needs to check each
  letter explicitly rather than trusting a generic "arylsulfatase" query.

  `Krabbe_Disease_Due_To_Saposin_A_Deficiency` (galactosylceramidase, not an
  arylsulfatase, but the same specimen-granularity question) is the
  instructive contrast to Maroteaux-Lamy's decline: it also declined the
  Part-level code, but for the opposite reason — not because no code exists,
  but because the entry's own diagnostic claim is specifically the
  leukocyte-versus-fibroblast activity *discordance* that distinguishes this
  activator-deficiency variant from classic GALC-deficient Krabbe disease. A
  single Part-level code would have erased exactly the fact the row exists to
  state, so two specimen-specific codes were bound instead. Maroteaux-Lamy
  has no code of any granularity to choose between; Krabbe has one and
  deliberately did not use it. Both are specimen-level decisions, reached for
  opposite reasons.
- **GBA1 / GBA2.** Two distinct glucosylceramidases (lysosomal vs.
  non-lysosomal), sharing enough vocabulary ("glucocerebrosidase",
  "glucosylceramidase", "beta-glucosidase") that a GBA2 diagnostic row reads,
  at a skim, like a GBA1/Gaucher mention. `Hereditary_Spastic_Paraplegia_46`
  and `Autosomal_Recessive_Cerebellar_Ataxia_With_Late_Onset_Spasticity` both
  carry a genuine, cited GBA2 enzyme-activity diagnosis row — not a mechanism
  mention, not a differential — and both were still correctly declined,
  because no GBA2-specific LOINC code exists and the GBA1 code
  (`LOINC:LP15604-9`) names the wrong gene product. This is the one
  methodological case in the tranche where the *candidate* was right (a real
  test exists) and the *binding* would still have been wrong.

## Closing summary

39 stratum entries were examined in this tranche: 20 carry a new LOINC
binding, and 19 were declined with a stated reason, across PRs #14481,
#14491, #14494, #14561 and #14617 (all open as of 2026-10-16). Both counts
are denominators worth stating explicitly rather than quoting a bare total
later — 20 bound, 19 declined, 39 examined, and all three numbers should
still add up for anyone re-deriving them from the table above. The declines
are recorded here with their reason so the next pass over this tranche — or
the next tranche that touches a lysosomal-storage or IEM entry — does not
re-derive the same conclusions from scratch.
