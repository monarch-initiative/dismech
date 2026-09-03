# Knowledge gaps in curated discussions: a completeness review

**Date:** 2026-09-02
**Scope:** every `discussions[]` entry with `kind: KNOWLEDGE_GAP` in
`kb/disorders/`, `kb/modules/`, `kb/comorbidities/` and `kb/groupings/`
**Regenerate:** `just knowledge-gap-audit` (per-gap detail with
`--format list --state <STATE>`; a table with `--format tsv`)

## Summary

The knowledge-gap layer is large and its prose is good. 1,781 knowledge gaps are
curated across 1,046 entries — more than every other discussion kind combined
(573 `HUMAN_MODEL_MISMATCH`, 181 `CONTROVERSY`, 150 `OPEN_QUESTION`, 112
`INTERPRETATION`, 34 `CURATION_TODO`, 27 `EMERGING_HYPOTHESIS`). Prompts state a
real unanswered question rather than a curation chore, rationales explain what
hangs on the answer, and 1,243 gaps cite evidence.

The *structural* half is weaker, and nothing in `just qc` looks at it. A gap that
anchors to nothing, or that proposes an experiment with no way to tell a
supporting result from a refuting one, validates and renders exactly like a
complete one.

| State | Gaps | Entries |
|---|---:|---:|
| Proposed experiment with no decision logic | 626 | 409 |
| No `status` | 302 | 193 |
| No `attaches_to` | 47 | 36 |
| Evidence prose still arguing the retired `PARTIAL` grade | 66 | 62 |
| Bare-name experiment target (fixed by this change) | 13 | 6 |
| `RESOLVED` with no `resolution_note` (fixed by this change) | 1 | 1 |

945 of the 1,781 gaps are in none of those states.

## Finding 1: experiment targets were unchecked, and 13 were broken

This is the one defect no existing check could see, so it is the one this change
repairs rather than reports.

`CLAUDE.md` states that `discussions[].proposed_experiments[].{perturbations,readouts}[].target`
takes the `<kind>#<name>` entity-reference grammar, unlike the bare names used by
the pathograph slots next to it. Both gates that look at targets decline the job:

- `check-entity-refs` walks `target`, but a value with no `#` in a slot outside
  `KNOWN_KIND_SLOTS` is treated as "not a reference" and skipped, because
  `target` legitimately carries bare names in its `downstream` and
  `target_mechanisms` homes.
- `check-causal-targets` excludes experiment readouts outright, which
  `test_experiment_readout_targets_are_not_checked_here` records deliberately.

So a bare name in these slots pointed at nothing, in silence. Thirteen sites
across six entries were in that state. Eleven named a real pathophysiology node
in the same file and were repaired by prefixing `pathophysiology#`.

The other two, both in `Alcoholic_Liver_Disease`, held a Gene Ontology process
label rather than a node name (`lactate biosynthetic process`,
`aryl hydrocarbon receptor signaling`), each appearing once as a perturbation and
once as a readout. Both arms of that experiment are microbiota-mediated routes
tested against the intestinal barrier, and the discussion already anchors there,
so all four were retargeted to
`pathophysiology#Intestinal Barrier Dysfunction and Endotoxin Translocation`.
That is a curator judgment, not a mechanical re-prefixing; the GO identity is
retained in each item's own `biological_processes` descriptor.

`just knowledge-gap-audit --strict` now exits zero, and fails on any
reintroduction.

## Finding 2: 59% of proposed experiments cannot be decided

Of 1,525 experiments proposed under knowledge gaps, 899 carry nothing beyond
`experiment_id`, `name` and `description`. No `decision_criterion`, no
`would_support`/`would_refute`, no `supporting_outcome`/`refuting_outcome`, and
no `readouts`.

The `Experiment` class exists to say what result would settle the question. The
decision register's `would_support`/`would_refute` entry (#9224) went to some
trouble to separate *what a result bears on* from *what would be observed*, and
that distinction only pays off when one of them is present. Where they are used
they work well:

| Slot | Experiments using it |
|---|---:|
| `decision_criterion` | 438 |
| `would_support` | 290 |
| `readouts` | 183 |
| `supporting_outcome` | 181 |
| `refuting_outcome` | 166 |
| `would_refute` | 82 |

`would_refute` at 82 against `would_support` at 290 is worth noting on its own: a
proposal that names only the confirming direction is weaker than one that says
what would kill the hypothesis.

Worst cases are whole blocks of proposals with no decision logic anywhere:
`Postural_Orthostatic_Tachycardia_Syndrome` (`gap_pots_receptor_autoantibody_causality`,
four of four), `Kawasaki_Disease` (`kd_unknown_trigger_immune_endothelial_link`,
four of four) and `Neurodevelopmental_Disorder_with_Hearing_Loss_and_Spasticity`
(`afg2b_cochlear_mechanism_gap`, four of four). None is a bad experiment; each is
a well-described protocol with no stated stopping rule.

This is a backlog, not breakage, so the audit reports it and does not gate on it.
The cheapest improvement is a `decision_criterion` sentence per experiment,
because it needs no new literature — only a curator deciding what the proposal
was for.

## Finding 3: 301 gaps carry no status

`DiscussionStatusEnum` is what separates an open gap from a resolved or archived
one, and the discussions browser exports the value as a facet. Absent, a gap
cannot be filtered as open. 1,477 gaps say `OPEN`, two say `RESOLVED`, and 302
across 193 entries say nothing.

Two resolved gaps in 1,781 is itself a signal: the layer is effectively
append-only. Nothing yet retires a gap when the literature answers it, and no
workflow does that sweep.

## Finding 4: 47 gaps anchor to nothing

An `attaches_to`-less gap never reaches the pathograph or the attached-node facet
of the browser. Thirty-six are in `kb/disorders/`, eleven in `kb/groupings/`.

Most are not hard to anchor. They cluster into natural-history and epidemiology
questions ("What is the natural history of AIMS across the lifespan",
"What is the true population-level prevalence and incidence of DYRK1A-related
intellectual disability"), management questions, and nosology questions about the
entry's own boundaries. `CLAUDE.md` supplies the empty-anchor idiom exactly for
these — `prevalence#`, `progression#`, `clinical_burden#`, `treatments#` — and
only 36 gaps in the whole KB currently use it. "There was nothing to point at"
is rarely the real answer.

The grouping cases are different and genuinely interesting: several ask whether
the grouping's own membership is right (`iei_tree_coverage_against_iuis_2024`,
`digenic_grouping_coverage_against_olida`,
`alps_umbrella_and_gene_entry_both_listed`). A gap about the shape of a grouping
has no obvious anchor inside it, and that may be a real modeling gap rather than
a curation lapse.

## Finding 5: 66 gaps still argue for a retired evidence grade

Seventy-five evidence items inside knowledge-gap discussions, across 62 entries,
have an `explanation` that justifies the `PARTIAL` grade retired by #10003
("Graded PARTIAL on the word 'many'…", "Marked PARTIAL because the trial was
small…"). The values were migrated; this prose was not, which #10003 recorded as
expected. No gate catches prose naming a retired value, so this is a slice of
that known backlog rather than a new finding — recorded here because it is
concentrated where a reader is most likely to hit it, in the argument for why a
gap exists.

## Finding 6: kind boundaries drift, mostly at the model/translation line

`CLAUDE.md` draws the line as: `KNOWLEDGE_GAP` means evidence is absent;
`HUMAN_MODEL_MISMATCH` means evidence exists in a model and translational
validity is the open question. Scanning gap prose for model-system and fidelity
language returns 24 candidates, of which most are correctly `KNOWLEDGE_GAP` (no
model exists at all — `kfd_no_animal_model`, `afg2b_no_animal_model`,
`ptrhd1_no_animal_or_cellular_model`). A handful read as
`HUMAN_MODEL_MISMATCH` on that test, because a model result exists and its
fidelity is precisely what is being asked:

- `Craniometaphyseal_Dysplasia` / `knowledge_gap_ar_cmd_connexin_mechanism` — the knock-in reproduces the skeletal phenotype while connexin 43 ablation does not phenocopy it.
- `Dilated_Cardiomyopathy_1Y` / `tpm1_pseudophosphorylation_rescue` — an in-vitro rescue whose transgenic mouse is itself cardiomyopathic.
- `POLR-Related_Leukodystrophy` / `polr_hld_ibuprofen_translation_gap` — mouse nonsense alleles versus human hypomorphic missense alleles.
- `WWOX-Related_Developmental_and_Epileptic_Encephalopathy` / `gap_gsk3b_as_a_druggable_node` — provoked-seizure rescue in Wwox-null mice versus spontaneous drug-resistant human seizures.
- `kb/modules/spinal_hsp90_opioid_enhancement` / `gap_hsp90_spinal_translational_selectivity` — the whole module chain is mouse, with the opposite effect systemically.

A smaller set states a live published disagreement in the prompt itself and reads
as `CONTROVERSY`: `ndufa12_assembly_requirement_conflict` ("The knockdown and
patient-cell evidence disagree"), `sdha-ndaxoa-tissue-expression-of-the-enzyme-defect`
("the two published biochemical studies disagree"),
`gap_prenatal_onset_of_brain_involvement` ("a direct disagreement rather than a
silence"), `gap_dusp22_prognostic_reproducibility`, and
`bavm-unruptured-management-controversy`.

These are curatorial calls that change an exported facet, so none was re-kinded
here. They are listed so a curator can decide them as a batch.

## Minor observations

- **Two discussion IDs are reused across files.** `no_disease_specific_management_literature`
  appears in three acromesomelic dysplasia entries, and
  `gap_bip_ocd_3p21_1_effector_gene_and_h3k27ac` in both `Bipolar_Disorder` and
  `Obsessive-Compulsive_Disorder`. IDs are entry-scoped, so this is legal, and
  the second case is a genuinely shared cross-disorder question. It is worth
  knowing that the discussions export keys records on `discussion_id` and builds
  the page anchor from it.
- **158 gaps carry neither evidence nor a proposed experiment.** Prompt and
  rationale only. Legitimate for a gap whose point is that nothing has been
  published, but it is the population to check first for gaps that were simply
  never finished.
- **Prompts are lightly templated**, most visibly eleven that open "What is the
  natural history of…". That is a reasonable recurring question, not a defect,
  but it overlaps almost exactly with the unanchored population in Finding 4.

## What this change did

- Repaired 13 bare experiment targets across six entries (Finding 1).
- Added the missing `resolution_note` to the single `RESOLVED` gap lacking one,
  summarizing the scoping decision already stated in its `rationale`.
- Added `scripts/knowledge_gap_discussion_audit.py` and
  `just knowledge-gap-audit`, report-only by default, with `--strict` covering
  the two states that are breakage rather than backlog.
- Left Findings 2, 3, 4, 5 and 6 as reported backlog. Each is either a curatorial
  judgment or a multi-hundred-entry sweep that should not ride along with a
  review.
