# Pediatric epilepsies in dismech: census, AAP coverage, and the mechanism-module gap

*2026-09-10. Landscape analysis plus one KB addition (a module collection). The
disorder-level census itself is generated, not hand-written: see
[`research/pediatric_epilepsy_census.md`](../../research/pediatric_epilepsy_census.md)
and the script that produces it,
[`scripts/pediatric_epilepsy_census.py`](../../scripts/pediatric_epilepsy_census.py).*

## Summary

dismech has 109 disorder entries inside the MONDO epilepsy closure
(`MONDO:0005027`), and 84 of them are pediatric. Another 26 entries are named as
epilepsies or DEEs but sit outside that closure in MONDO, and 48 more carry
seizures as an obligate or very frequent phenotype without being epilepsy
entries. The American Academy of Pediatrics list of pediatric epilepsy types is
almost fully covered: 20 of 23 types have a dedicated entry, and the remaining
three are partial rather than absent.

The gap is not coverage. It is mechanism. Of the 183 entries in the census, 83
conform to `epilepsy_excitation_inhibition_imbalance`, and for 71 of them it is
the only module they conform to. That module is a five-node generic chain from
ion-channel dysfunction to recurrent seizures. Whatever is specific about SCN1A
in Dravet, about thalamocortical circuits in absence epilepsy, about pyridoxine
responsiveness,
or about immune-driven epileptogenesis in Rasmussen encephalitis, none of it is
in the module layer. It is prose in individual entries.

This report records what is there, what the AAP list asks for, and which
mechanism lanes deserve modules. It also adds one thing to the KB: the
`Mechanisms of the Epilepsies` module collection, which groups the six existing
modules that are genuine routes to seizures.

## How the census decides what counts

Three tiers, applied by script so the answer survives the next curation wave.

| Tier | Test | Count |
| --- | --- | --- |
| 1 | The entry's `disease_term`, a `has_subtypes[].subtype_term`, or an exact/narrow MONDO mapping is an `is_a` descendant of `MONDO:0005027` | 109 |
| 2 | Named *epilepsy*, *seizure*, or *DEE* but MONDO does not place the term under epilepsy | 26 |
| 3 | Outside tiers 1 and 2, a phenotype bound to an HP seizure term with `frequency` OBLIGATE or VERY_FREQUENT | 48 |

Tier 2 is the interesting one. It is where the KB and MONDO disagree about what
an epilepsy is. `CDKL5_Deficiency_Disorder` is a member of the
`Early_Infantile_Developmental_and_Epileptic_Encephalopathies` grouping and is
not in MONDO's epilepsy subtree. Neither UNC13A entry is, though both are listed
in the `Epilepsy_Excitation_Inhibition_Imbalance_Disorders` grouping. Most of the
rest are neurodevelopmental disorders whose MONDO label happens to end in "with
or without seizures". None of this is an error to fix. It is a boundary worth
knowing about before anyone writes a query that trusts the closure alone.

Age is then assigned from the ILAE 2022 Task Force position papers rather than
from the entries' own annotations, because the annotations are mostly absent: 28 of the
109 tier-1 entries carry an `onset_category` at all. The script keys each named syndrome to its ILAE age group (neonatal and infantile,
PMID:35503712; childhood, PMID:35503717; idiopathic generalized, PMID:35503716;
variable age, PMID:35503725) and treats numbered gene-defined DEEs as
infancy-or-early-childhood by definition. Sixteen tier-1 entries are ILAE
variable-age syndromes and are reported as VARIABLE, not as pediatric. Six are
UNKNOWN: they are in the closure, they are not named ILAE syndromes, and they
carry no onset data.

**This is a place the KB could be improved cheaply.** The onset information
exists in the source literature for nearly all of these entries and the schema
already has the slot. Populating `onset_category` on the tier-1 entries would
make the age question answerable from the KB rather than from a hard-coded map
inside a script.

## AAP coverage

20 of the 23 types on the
[AAP pediatric epilepsy types page](https://www.aap.org/en/patient-care/epilepsy/understanding-pediatric-epilepsy/understanding-pediatric-epilepsy-types-of-pediatric-epilepsy/)
have a dedicated entry. The full table is in the generated census. The three
partial ones:

- **Reflex epilepsies.** Only the photosensitive forms are curated
  (`Photosensitive_Epilepsy`, `Photosensitive_Occipital_Lobe_Epilepsy`). The
  reflex-epilepsy umbrella `MONDO:0017768` has no entry, and reading epilepsy,
  startle epilepsy, and hot-water epilepsy are absent.
- **Self-limited familial and non-familial neonatal-infantile seizures.** SeLNE
  and SeLIE are curated. The SCN2A self-limited familial neonatal-infantile form
  appears only as a phenotype-spectrum sentence inside the SCN2A DEE entry.
- **Sleep-related hypermotor epilepsy.** The familial form is curated. Sporadic
  SHE is not a separate entry.

Two things the AAP page names that are worth a note. Its "Epileptic
Encephalopathy with Continuous Spike and Wave during Sleep (CSWS)" maps to two
dismech entries, because ILAE 2022 folded Landau-Kleffner syndrome into DEE-SWAS
and both are kept here. Its "Doose Syndrome" also maps to two, and both carry
`MONDO:0014633` as `disease_term`, which is the duplicate-`disease_term` pattern
tracked in issue #10113.

## The mechanism gap

Module conformance across all 183 census entries:

| Module | Conformers |
| --- | --- |
| `epilepsy_excitation_inhibition_imbalance` | 83 |
| `synaptic_vesicle_cycle` | 8 |
| `congenital_disorder_of_glycosylation` | 7 |
| `microtubule_dependent_neuronal_migration_failure` | 4 |
| everything else | 1 to 2 each |

73 of the 183 declare no `conforms_to` at all.

The shape of that table is the finding. One module absorbs the whole population,
and it is the most generic one available. `epilepsy_excitation_inhibition_imbalance`
has five nodes and no treatments, no mechanistic hypotheses, and no discussions.
It says that something goes wrong with channels or synapses, then excitation
exceeds inhibition, then neurons fire together, then seizures. That is true of
every epilepsy, which is why 83 entries reach it, and it is why reaching it
distinguishes nothing.

Meanwhile the recurring mechanism themes are visible in the entries' own
pathophysiology node names and have no module to conform to:

| Theme | Tier-1 entries whose pathophysiology nodes name it | Module? |
| --- | --- | --- |
| Developmental and epileptic encephalopathy (seizures worsening development) | 26 | No |
| Thalamocortical spike-wave oscillation | 12 | No |
| Potassium-channel excitability | 10 | No |
| Interneuron dysfunction | 9 | Partly (developmental module only) |
| mTOR pathway | 7 | Yes (`pi3k_akt_mtor_cortical_overgrowth`) |
| Sodium-channel excitability | 6 | No |
| Neuroinflammation in epileptogenesis | 6 | No |
| Blood-brain barrier disruption | 6 | No |
| NMDA receptor dysfunction | 5 | Only the hypofunction direction |
| GABA-A receptor dysfunction | 3 | No |
| Vitamin B6 dependence | 2 | No |

### Modules worth writing, in order

1. **`developmental_and_epileptic_encephalopathy`.** The highest-value one. It
   is the concept that makes a DEE a DEE: the epileptic activity itself
   contributes to developmental impairment beyond what the etiology alone would
   cause. 26 entries already model it as a node, and the ILAE definition papers
   plus PMID:41014440 give it an evidence base. It is also the piece that would
   let the two existing DEE groupings audit their members against a criterion
   instead of a name.
2. **`thalamocortical_spike_wave_oscillation`.** The absence-epilepsy circuit:
   T-type calcium currents in thalamic relay neurons, GABA-B-mediated reticular
   inhibition, and the generalized 3 Hz spike-wave discharge. It has 12 candidate
   conformers, a distinct treatment logic (ethosuximide targets the T-type
   current; carbamazepine worsens absence), and it is a genuine circuit-level
   mechanism rather than a restatement of hyperexcitability.
3. **`voltage_gated_sodium_channel_neuronal_excitability`.** The single most
   therapeutically loaded lane in pediatric epilepsy, because the
   gain-of-function and loss-of-function directions demand opposite drugs. SCN1A
   loss in Dravet contraindicates sodium-channel blockers; SCN2A and SCN8A gain
   of function calls for them. That inversion is currently prose in each entry
   and would be one module with two branches.
4. **`neuroinflammatory_epileptogenesis`.** IL-1beta, HMGB1-TLR4, and
   blood-brain barrier breakdown as a route from insult to chronic epilepsy.
   Covers FIRES, Rasmussen encephalitis, post-traumatic epilepsy, and the
   BBB content currently sitting in the umbrella `Epilepsy` entry. Needs careful
   scoping: it is the lane most prone to being overstated as a universal
   explanation, and the existing epilepsy project brief already says so.
5. **`vitamin_b6_dependent_epilepsy`.** Small, but the cleanest treatable
   mechanism in the whole pool: an enzymatic block starves pyridoxal
   5'-phosphate-dependent decarboxylases, and the seizures answer to the vitamin
   rather than to antiseizure medication. Two conformers today
   (`Pyridoxine-Dependent_Epilepsy`, `PNPO_Deficiency`), more later.

A sixth candidate, a GABA-A receptor module, is real but thin at three entries;
it may be better as a branch of the sodium-channel module's successor rather
than its own file.

### What was added

[`kb/module_collections/Mechanisms_of_the_Epilepsies.yaml`](../../kb/module_collections/Mechanisms_of_the_Epilepsies.yaml),
a `MECHANISTIC_FAMILY` collection with six members: the
excitation-inhibition convergence module plus five upstream lanes
(interneuron specification and tangential migration failure, the synaptic
vesicle cycle, excitatory synapse scaffold disruption, PI3K-AKT-mTOR cortical
overgrowth, and FAME pentanucleotide repeat RNA toxicity).

Three modules that recur in epilepsy entries were deliberately left out, and the
collection's `notes` records why. `glutamate_excitotoxicity` ends in neuronal
death rather than in epileptogenesis. `metabolic_intoxication_decompensation`
ends in acute encephalopathy. `epigenetic_machinery_neurodevelopmental_dysregulation`
and `congenital_disorder_of_glycosylation` are general neurodevelopmental
modules in which seizures are one output among many. A collection that admitted
those would be an inventory of modules epilepsy entries happen to touch, which
is the failure mode the create-module skill warns about.

The collection is not pediatric-only, on purpose. Mechanism lanes are shared
across ages and age at onset is a property of the disease entries. That is why
the FAME module is a member despite familial adult myoclonus epilepsy being
adult-onset.

## Follow-ups

- Populate `onset_category` on the tier-1 entries that lack it, so the pediatric
  verdict comes from the KB rather than from the script's ILAE map.
- Write the five proposed modules, highest value first, and retrofit conformance.
- Decide whether tier-2 entries such as CDKL5 deficiency disorder should carry a
  `mappings.mondo_mappings` entry that places them under epilepsy, or whether the
  MONDO boundary is correct and the KB grouping is the right home.
- Resolve the two entries sharing `MONDO:0014633` (issue #10113).
- Curate the reflex-epilepsy umbrella and sporadic SHE if the AAP list is to be
  fully covered.
