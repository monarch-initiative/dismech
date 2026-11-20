---
title: Model-Organism Assays
status: PLANNED
tags:
- models
- animal-models
- assays
- impress
- mammalian-phenotype
- behavior
description: Give the readouts on animal-model records a standard identity for the test that was run (IMPReSS parameters for mouse first) and an organism-appropriate phenotype term for the result (MP first), so a model's evidence can be queried and compared across entries instead of read as free text.
diseases:
- Trichotillomania
- Major_Depressive_Disorder
- Generalized_Anxiety_Disorder
- Obsessive-Compulsive_Disorder
- Amyotrophic_Lateral_Sclerosis
- Dominant_Deafness-Onychodystrophy_Syndrome
- SNF8-Related_Neurodevelopmental_Disorder
- Alopecia-Intellectual_Disability_Syndrome_4
- Brain_Small_Vessel_Disease_2
---

# Model-Organism Assays

## Goal

An animal-model record links a model to the mechanism node it informs through
`modeled_mechanisms`, and each link can carry `readouts`: the measurements that
ground the claim. Today those readouts are almost entirely free text. Nothing
says which test produced a measurement or which ontology term describes the
result in the animal, so two entries that cite the same mouse open-field result
cannot be recognised as citing the same thing.

This project gives a readout two structured parts:

| Part | Question it answers | Mouse source | Analogue for human measurements |
|---|---|---|---|
| assay identity | which test, run how | an IMPReSS procedure and parameter | a LOINC code (`projects/LOINC_DIAGNOSTICS.md`) |
| result term | what was observed, in the animal's own vocabulary | a Mammalian Phenotype (MP) term | an HPO term |

Mouse first, because IMPReSS already pairs the two: every measured parameter
names the MP terms a significant result is annotated with. Other organisms
follow once the mouse pattern works (Phase 4).

## Current state

Counts are from a parse of every `animal_models:` block in `kb/disorders/`,
`kb/modules/` and `kb/comorbidities/` on 2026-11-10. They drift with every
merge; read them as a scoping snapshot.

| Measure | Count |
|---|---:|
| animal-model records | 3,385 (in 1,731 files) |
| records with `modeled_mechanisms` | 2,941 |
| model-to-mechanism links | 4,546 |
| readouts on those links | 2,221 |
| readouts with an `assays` binding | 0 |
| readouts with a `phenotype_term` | 7 (all HP) |
| readouts with `biological_processes` | 23 |
| records with free-text `associated_phenotypes` | 327 |
| distinct `species` strings | 102 |
| records whose text mentions IMPC or KOMP | 17 |

Three gaps follow from the schema rather than from curation effort:

- **The assay slot cannot be filled for an animal test.**
  `ExperimentalReadout.assays` is bound to `AssayTerm`, rooted at OBI
  `OBI:0000070` (assay). OBI has no adapter in `conf/oak_config.yaml` and no
  enum cache, so an OBI binding cannot be validated. OBI does not identify a
  specific standardised mouse protocol either.
- **The result slot only accepts human terms.** A readout's `phenotype_term`
  is a `PhenotypeDescriptor` bound to `PhenotypeTerm`, rooted at HP
  `HP:0000118` and MONDO. MP is not configured anywhere; MP IDs appear in the
  KB only inside prose fields of three entries.
- **The organism is a free string.** The laboratory mouse appears under six
  spellings across 2,460 records, chiefly `Mouse` (1,995), `Mus musculus` (359)
  and `Mouse (Mus musculus)` (77). An IMPReSS parameter is
  only meaningful on a mouse, so a check that the two agree needs a bound
  organism. That is issue #13768.

## What IMPReSS provides

IMPReSS (International Mouse Phenotyping Resource of Standardised Screens) is
the International Mouse Phenotyping Consortium's registry of phenotyping
protocols, the successor to EMPReSS. It defines pipelines (the IMPC adult
pipeline is the consortium-agreed core), procedures within them (mandatory or
optional, versioned), and parameters within each procedure. Its REST API at
`https://api.mousephenotype.org/impress/` serves each level by ID:
`procedure/<id>`, `parameter/<id>`, `parammpterm/<id>` and `ontologyterm/<id>`.

Behavioural and sensory procedures in the IMPC adult pipeline, as the API
returns them:

| Procedure | Key | Status | Version | Parameters |
|---|---|---|---|---:|
| Open Field | `IMPC_OFD_001` | mandatory | 1.10 | 52 |
| Acoustic Startle and Pre-pulse Inhibition (PPI) | `IMPC_ACS_003` | mandatory | 3.4 | 39 |
| Combined SHIRPA and Dysmorphology | `IMPC_CSD_003` | mandatory | 3.9 | 86 |
| Light-Dark Test | `IMPC_LDT_001` | optional | 1.1 | 34 |
| Auditory Brain Stem Response | `IMPC_ABR_002` | mandatory | 2.5 | 53 |

The parameter count includes procedure metadata as well as measurements. Of
Open Field's 52 parameters, 22 are metadata such as arena size, light
intensity in the centre of the arena and wall height, and carry no MP term.
Of the 30 measurements, 29 carry three MP terms, one for each
`selectionOutcome` (`INCREASED`, `DECREASED`, `ABNORMAL`); the exception,
Whole arena permanence (`IMPC_OFD_008_001`), carries none:

| Parameter | Key | INCREASED | DECREASED | ABNORMAL |
|---|---|---|---|---|
| Center permanence time | `IMPC_OFD_016_001` | MP:0020870 decreased thigmotaxis | MP:0002797 increased thigmotaxis | MP:0001362 abnormal anxiety-related response |
| Number of center entries | `IMPC_OFD_019_001` | MP:0001399 hyperactivity | MP:0001402 hypoactivity | MP:0003313 abnormal locomotor activation |
| Percentage center time | `IMPC_OFD_022_001` | MP:0004924 abnormal behavior | MP:0004924 abnormal behavior | MP:0004924 abnormal behavior |

**Standardising the test does not settle what it means.** The Open Field
procedure description says the test "is used to assess anxiety and exploratory
behaviors", on the premise that a normal mouse spends more time in the
periphery than in "the center (the most anxiogenic area)". But the
direction-specific MP terms IMPReSS assigns describe the observed behaviour
(thigmotaxis, activity), and the anxiety term appears only as the
non-directional `ABNORMAL` call. The separation between what was measured and
what it is taken to indicate already exists in IMPReSS and MP. dismech should
keep it: an IMPReSS parameter and MP term record the observation, and the
inference to a human construct stays in the link's `divergences`
(`PROXY_QUANTITY`, and `CONTESTED_ASSUMPTION` where the field disputes the
reading). `Major_Depressive_Disorder` (the daf-2 C. elegans foraging model) and
`Trichotillomania` (the Sapap3 overgrooming model) show how that caveat is
written today.

## Decisions to make

These go through the `extend-schema` skill and, once settled, the decision
register (`docs/explanation/design-decisions.md`).

1. **Where the assay identity lives.** IMPReSS is a protocol registry, not an
   OBO ontology, so it does not fit `AssayTerm` and has no OAK adapter. The
   closer precedent is a dataset accession: an identifier fetched once into
   `references_cache/` (as `GEO_<ID>.md` is) and validated by the cache file's
   presence. Options are a new prefix accepted by `assays`, or a separate
   readout slot for a standardised protocol parameter. The parameter key
   (`IMPC_OFD_016_001`) carries its procedure, so the procedure does not need
   its own slot.
2. **Where the result term lives.** Widening `PhenotypeTerm` to MP would let
   mouse terms into the human phenotype slots of every disease entry. A
   readout-only slot for a model-organism phenotype term, bound to MP first,
   keeps the two apart. MP is on OLS, so `ols:mp` in `conf/oak_config.yaml`
   would give it cache-first validation like HP.
3. **Direction.** IMPReSS `INCREASED` and `DECREASED` map onto the readout
   `direction` values of the same names. `ABNORMAL` has no direction and maps
   to `ALTERED`.
4. **Comparison with the human phenotype.** Whether a readout's MP term
   corresponds to one of the entry's HP phenotypes is a curator judgement.
   MP-HP mappings, for example through uPheno, can propose candidates for that
   judgement but should not decide it.
5. **Organism binding.** IMPReSS identifiers on a record whose organism is a
   free string cannot be checked against it. Either this project waits for
   #13768, or it checks against the normalised species strings in the interim.

## Phases

### Phase 0: scope and decide

- [ ] Add a report-only census recipe that reproduces the counts above.
- [ ] Settle decisions 1 to 5 and record them in the decision register.
- [ ] Confirm the IMPReSS API's terms of use and whether a bulk download
      exists, so the cache can be built without one request per parameter.

### Phase 1: MP terms on readouts

- [ ] Add MP to `conf/oak_config.yaml` and the readout slot from decision 2.
- [ ] Bind MP terms on the readouts of the worked examples below, reading each
      term from OLS in the step it is written.
- [ ] Extend `just model-scale-audit` or a sibling recipe to report readouts
      with and without a result term.

### Phase 2: IMPReSS parameter identifiers

- [ ] Write the fetcher and cache format for IMPReSS parameters (key, name,
      procedure, version, MP terms per outcome), following the GEO pattern.
- [ ] Add the slot from decision 1 and a gate that the cached MP terms for a
      parameter include the readout's MP term when both are given.
- [ ] Pilot on the 17 records that mention IMPC or KOMP. First sort them into
      records that cite IMPC phenotyping data, which can take an IMPReSS
      parameter, and records that only use an IMPC-made allele, which cannot.

### Phase 3: IMPC data

- [ ] Coordinate with `projects/COMMONFUND/KOMP2.md`, whose plan is to pull
      significant IMPC calls with their procedure, parameter, zygosity, sex
      and MP term. With Phase 2 in place those calls can land as structured
      readouts.
- [ ] Update the KOMP2 project's evidence wording, which still describes IMPC
      evidence as `PARTIAL`, a `supports` value retired in #7439.

### Phase 4: other organisms

- [ ] Assess, per organism, what plays the IMPReSS and MP roles. Candidates to
      evaluate include ZP and ZECO for zebrafish, WormBase's phenotype
      ontology for C. elegans, FlyBase's controlled vocabularies for
      Drosophila, the RGD measurement and trait ontologies (MMO, CMO, VT) for
      rat, and NBO for behaviour across species. Zebrafish (386 records under
      six spellings of the species) and Drosophila (110 records under five)
      are the next largest groups after mouse.

## Worked examples

| Entry | Model | Readout today | What the project adds |
|---|---|---|---|
| `Dominant_Deafness-Onychodystrophy_Syndrome` | Atp6v1b2 p.Arg506* knock-in, one line phenotyped through the IMPC pipeline | "auditory brainstem responses were normal at 14 weeks" in `limitations` prose | an `IMPC_ABR_002` parameter with `direction: UNCHANGED`; a normal result has no MP term, which is why the assay identity matters on its own |
| `Generalized_Anxiety_Disorder` | larval and adult zebrafish anxiolytic assays | named in free text ("Novel-tank bottom dwelling under diazepam") | a Phase 4 zebrafish assay identity; the existing `PROXY_QUANTITY` caveat stays |
| `Trichotillomania` | Sapap3 knockout mouse | "Facial hair loss and skin lesions from compulsive grooming" | an MP grooming term; no IMPReSS parameter, since the result comes from a published study rather than the IMPC pipeline |
| `Major_Depressive_Disorder` | daf-2 C. elegans foraging immobility | free-text readout plus typed divergences | a Phase 4 worm phenotype term; the divergences stay as written |
| `Amyotrophic_Lateral_Sclerosis` | canine SOD1 E40K and equine motor neuron disease | histology readouts in free text | Phase 4; shows that dog and horse models have no IMPReSS equivalent |
| `SNF8-Related_Neurodevelopmental_Disorder`, `Alopecia-Intellectual_Disability_Syndrome_4`, `Brain_Small_Vessel_Disease_2` | mice carrying IMPC-produced alleles | the IMPC origin is recorded only in the model's name, genotype or prose | the Phase 2 sorting of IMPC phenotyping data from IMPC alleles |

## Related

- #13768: a bound `organism` and a structured non-genetic perturbation on
  `AnimalModel`. Decision 5 depends on it.
- #11743: a divergence type for a model that reproduces only part of the
  phenotype.
- #13754 and #14274: stress-paradigm models of mood disorders, where the
  assay-versus-construct separation matters most.
- #16387: whole model organisms from a developmental neurotoxicity paper.
- `projects/LOINC_DIAGNOSTICS.md`: the same identity-of-a-measurement problem
  for human tests, solved with LOINC.
- `projects/COMMONFUND/KOMP2.md` and `projects/NAMO_RD_MODELS.md`: neighbouring
  model-organism projects.
- `docs/explanation/model-credibility.md`: what a model-to-mechanism link does
  and does not claim.
