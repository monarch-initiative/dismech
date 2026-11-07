# KEAP1–NRF2–ARE module: coverage assessment and plan

**Status:** draft plan, no KB content written yet.
**Seed reference:** Sharma et al. 2026, *Deciphering the quantitative relationship
between NRF2 and SRXN1 through semi-mechanistic computational modeling*,
Toxicology 519:154284, doi:10.1016/j.tox.2025.154284, **PMID:40972999**
(cached as `references_cache/PMID_40972999.md`, abstract only).

## Why a module

The NRF2 antioxidant response turns up in a dozen disease entries. In some it is
switched off (Cockayne syndrome, PARK7 Parkinson disease, pachyonychia
congenita, RCBTB1 retinopathy, both SQSTM1 entries, MMDS9B). In others it is
switched on (hepatoblastoma, HLRCC, KEAP1- or NFE2L2-mutant lung and oesophageal
cancers). Each entry describes it in its own way, and no module gives them a
common node to conform to. The NRF2 activation inside
`oncometabolite_dioxygenase_inhibition` covers only the case where fumarate
succinates KEAP1. The current form also hides the gene from the graph: none of
these nodes binds NFE2L2 as a node gene, and each is labelled with the generic GO
term *response to oxidative stress*.

The mechanism passes the module test in the `create-module` skill. It is one
conserved chain: a sensor is modified, NRF2 escapes degradation, NRF2 drives
transcription from the antioxidant response element (ARE), and the target-gene
products act. Every case runs through one rate-limiting step, NRF2-driven
transcription from ARE genes. Diseases differ in which way that step goes and
in what pushes it there. They do not differ in the chain itself.

## Coverage assessment (2026-11-07)

**The seed paper is not cited anywhere in DisMech:** not by DOI, not by PMID,
and not by title, in `kb/`, `references_cache/`, `research/`, `docs/` or
`projects/`.

| Item | What exists |
|---|---|
| NFE2L2 (`hgnc:7782`) | Bound in 5 disorders, no modules. Mentioned in text in 41 disorders and 5 modules |
| KEAP1 (`hgnc:23177`) | Bound in 3 disorders. Mentioned in text in 15 disorders and 2 modules |
| SRXN1 | Absent from the KB and from `cache/hgnc/terms.csv` |
| ARE targets | HMOX1 (`hgnc:5013`), NQO1 (`hgnc:2874`), GCLC/GCLM (`hgnc:4311`/`hgnc:4312`) are each bound in 1–2 disorders. TXNRD1, PRDX1, MAFG/F/K and BACH1 are not bound anywhere |
| NRF2-named nodes | About 12 disorder nodes and 1 module node (`oncometabolite_dioxygenase_inhibition#KEAP1 Succination and NRF2 Antioxidant Pathway Activation`, whose only conformer is HLRCC) |
| Electrophile sensing | `Contact_Dermatitis` has a keratinocyte electrophile-sensing node and the Keap1–Nrf2–ARE reporter assays (KeratinoSens, LuSens) as experimental models |
| Seed paper's compounds | Sulforaphane in 3 entries, CDDO-methyl (bardoxolone) in 2, andrographolide in 1, ethacrynic acid in none. Omaveloxolone in 4 |
| Computational models of NRF2 | None in `kb/` or `models/` |
| Sibling modules | `cul3_substrate_adaptor_dysfunction` (KEAP1 is one CRL3 adaptor), `drug_induced_liver_injury` (reactive metabolites, almost no NRF2), `mitochondrial_dysfunction` (oxidative stress), `disabled_macroautophagy` (p62) |

## Proposed module

Working slug `keap1_nrf2_are_signaling`. Categories `TOXICOLOGY` and
`PHARMACOLOGY`, plus `ONCOLOGY` if the deep research confirms that
NRF2-addicted tumours belong in scope.

### Provisional node chain

| # | Node (working name) | Role | Candidate GO bindings | Genes |
|---|---|---|---|---|
| 1 | Modification of KEAP1 sensor cysteines | trigger | GO:0071466 *cellular response to xenobiotic stimulus*; GO:0034599 *cellular response to oxidative stress* | KEAP1 |
| 2 | NRF2 escape from KEAP1–CUL3 ubiquitination and nuclear accumulation | amplifier | GO:0016567 *protein ubiquitination* (DECREASED) | KEAP1, CUL3 (`hgnc:2553`), NFE2L2 |
| 3 | **NRF2 transcriptional activation of ARE genes** | central effector (**key conformance target**) | GO:0001228 *DNA-binding transcription activator activity, RNA polymerase II-specific* | NFE2L2, small MAF partners |
| 4 | ARE gene products restore redox balance | effector | GO:0032542 *sulfiredoxin activity*; GO:0098869 *cellular oxidant detoxification* | SRXN1, NQO1, HMOX1, GCLC, GCLM |
| 5 | Cytoprotection, or its failure | consequence | to be chosen after the deep research | — |

The GO IDs above came from OLS searches made while drafting this plan. They are
candidates, not chosen bindings, and `just validate-terms` decides membership in
the dynamic enums. **SRXN1's HGNC ID is unconfirmed**: the HGNC and UniProt APIs
were blocked from the drafting environment and EBI Search returned an error.
Resolve it with a real lookup before binding.

**One module handles both directions.** Hypoactive diseases conform to node 3
with `DECREASED`. Diseases with constitutive activation (KEAP1/NFE2L2-mutant
cancers, HLRCC) conform with `INCREASED`, or with `GAIN_OF_FUNCTION` where NRF2
has escaped host control. Splitting the module by direction would put the same
mechanism in two places.

**A non-canonical branch** is a candidate for node 1b: p62/SQSTM1 sequestering
KEAP1. It is the link to autophagy that the abstract names, and both SQSTM1
entries need it. Include it if the deep research supports it as a conserved
alternative way in.

### Where the seed paper fits

The abstract supports three things, all at node 3 or on the 3→4 edge:

1. **SRXN1 is an NRF2 target gene** ("a bona fide key NRF2 target gene"). The
   paper asserts this rather than tests it, so record it with
   `quote_role: BACKGROUND`.
2. **NRF2 protein alone does not account for SRXN1 induction.** A cofactor or a
   post-translational modification is needed. This is a conclusion inferred
   from a model fitted to HepG2 data, so grade it `COMPUTATIONAL`, likely with
   `directness: INDIRECT`.
3. **The modulation depends on time, compound and exposure pattern.** The data
   cover sulforaphane, andrographolide, ethacrynic acid and CDDO-me, given as
   single or repeated doses.

The paper's model belongs in the module's `computational_models`, with a
`modeled_mechanisms` link to node 3:

- `relationship: PARTIALLY_RECAPITULATES` and `model_scale: MOLECULAR`.
- A `BOUNDARY_OMISSION` divergence: the cofactor appears only as an inferred
  term, not as an explicit species in the model.
- A `POPULATION_MISMATCH` divergence: the data are from a single hepatoblastoma
  cell line.

The sentence listing oxidative stress, autophagy, proliferation and apoptosis
is background framing in the paper. It is not that paper's result and must not
be the only support for any edge to those processes.

## Phase 2: deep research to check the paper's claims

The seed is one modelling paper from one cell line, so every claim the module
takes from it needs independent backing. The deep research has two jobs: check the
paper's specific claims, and settle the module's scope, nodes and term bindings
against the wider literature before any node is committed.

The module research recipe needs the module file to exist first, so the order is:

1. Write a minimal skeleton `kb/modules/keap1_nrf2_are_signaling.yaml` with the
   name, description, category, and the five provisional nodes above (prose
   only, no term bindings yet). Validate it against `Disease`.
2. Run the deep research against that skeleton, with more than one provider so
   claims can be cross-checked:

   ```bash
   just research-module <provider> keap1_nrf2_are_signaling
   ```

   Reports land in `research/modules/`. Treat them as leads, not content.
3. Read each report's `## Reference Validation` and `## Term Validation`
   sections. Never bind a CURIE a report lists as unresolved, and re-run
   `just validate-research-terms <report>` on any report that predates that
   section.

Questions for the deep research to settle:

- **SRXN1 as an NRF2/ARE target.** Independent primary evidence that SRXN1
  transcription is ARE-driven and NRF2-dependent, beyond the seed paper's
  assertion.
- **The cofactor / post-translational-modification claim.** Is NRF2 needing a
  partner or modification to drive ARE transcription supported outside this one
  HepG2 model? Which partners (small MAFs, and any others) are documented?
- **Scope of node 5.** Which downstream outcomes are conserved enough to be in
  the module (cytoprotection, and its failure), and which — autophagy,
  proliferation, apoptosis — are context-specific and should stay out or become
  gene-specific branches.
- **The non-canonical p62/SQSTM1 branch.** Is KEAP1 sequestration by p62 a
  conserved alternative trigger worth a node 1b.
- **Direction and the cancer case.** Whether constitutively active
  NRF2 in KEAP1/NFE2L2-mutant tumours belongs in this module (and so whether
  `ONCOLOGY` is a category), or stays with the oncometabolite module.
- **Ontology bindings.** GO biological-process and molecular-function terms, CL
  cell types, and the ARE target genes' HGNC IDs, each confirmed by lookup.

A useful cross-check alongside the literature search is AOP-Wiki: the KEAP1–NRF2
axis is a documented molecular initiating event in several adverse outcome
pathways (`aop-wiki` skill, `mie-ker-capture`, `ker-evidence-triage`). Those can
corroborate the causal edges with an independent, curated source.

## Phase 3: draft the module and wire conformers

1. Fill the skeleton's nodes with the confirmed bindings and verified evidence.
   Every snippet an exact substring of a cached abstract. Grade the seed paper's
   items `COMPUTATIONAL`; grade independent human or in-vitro support on its own
   terms.
2. Add the seed paper's model to `computational_models` with the
   `modeled_mechanisms` link and divergences described above.
3. Validate: `linkml-validate`, `linkml-term-validator`,
   `run_reference_validator.sh`, then `just validate-modules` and the gate
   checks the references skill lists.
4. Scaffold a history record:
   `just new-history --kind module --slug keap1_nrf2_are_signaling --event CREATE ...`.
5. Wire real conformers by adding `conforms_to: "keap1_nrf2_are_signaling#NRF2
   transcriptional activation of ARE genes"` (final node name) to the matching
   pathophysiology nodes in the disorder entries listed in the coverage table,
   with the right `modifier`. A node already conforming to another module keeps
   that reference and gains this one as a list — never repoint it. Re-validate
   each changed entry.
6. Small fix alongside: bind `hgnc:7782` (NFE2L2) as a node gene on the existing
   NRF2 nodes so the graph can find it, and add SRXN1 once its ID is confirmed.

## Decisions a curator still owns

- Final module name and slug (the deep research may argue for a clearer one).
- Which of the ~12 NRF2-themed entries become conformers now vs later.
- Whether the cancer activation case is in scope here or stays with
  `oncometabolite_dioxygenase_inhibition`.
- Whether to keep `oncometabolite_dioxygenase_inhibition#KEAP1 Succination...`
  as its own node or make it a conformer of node 1 of the new module.
