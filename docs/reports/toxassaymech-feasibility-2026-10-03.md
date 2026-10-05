# Feasibility of a ToxAssayMech built with mechmaker

**Asked by** @cmungall, on [PR #13452](https://github.com/monarch-initiative/dismech/pull/13452#issuecomment-5972253222),
the zebrafish VAMR assay report. **Scope.** Whether a dedicated knowledge base for
toxicology assay data — built with [mechmaker](https://github.com/monarch-initiative/mechmaker),
the Copier template that produces a DisMech-pattern "Mech" — is a sound way to hold
the kind of data that three recent dismech efforts have each had to improvise a home
for. Read on **2026-10-03** against mechmaker `main` and the
[MechRegistry](https://monarch-initiative.github.io/mechregistry/) snapshot of the
same date. No `kb/` or schema change is proposed here.

## Bottom line

A dedicated Mech for assay-battery data is technically straightforward to build —
mechmaker's template, ontology catalog and identity-minting fallback cover
everything the schema would need, and its cross-Mech link convention is exactly
the mechanism that would fix the duplication problem dismech has already hit three
times. But before running `copier copy`, two questions need an answer that this
report cannot give on its own, because both are about a different repository:

1. **[SOMAMech](https://github.com/EHS-Data-Standards/somamech) already exists, in
   closely overlapping territory**, and `survey-domain`'s own first rule is to check
   that before starting a new Mech. SOMAMech is not a ToxAssayMech — it extracts one
   publication at a time into bespoke per-assay-type classes, where the gap dismech
   keeps hitting is cross-publication, cross-chemical assay *batteries* (ToxCast,
   DNT-IVB, VAMR) that want one record per **endpoint**, not per paper. The two
   record shapes are different enough to coexist, but not different enough to build
   in isolation from EHS-Data-Standards.
2. **AOP-Wiki's Key Events are the obvious causal skeleton, and they are mostly
   empty.** 65% of Key Event Relationships in the 2026-08-06 snapshot sit at the
   KER evidence floor with zero references, and 69% carry no citation at all. A ToxAssayMech that imported AOP-Wiki's
   graph as curated content would be importing a hypothesis, not evidence — the
   same discipline dismech already built for this (`ker-evidence-triage`,
   `mie-ker-capture`) would have to run inside the new Mech too, record by record,
   not as a bulk load.

Recommendation: run a real `survey-domain` pass — coordinated with
EHS-Data-Standards, and working through two or three real candidate records on
paper, as `design-mech-schema`'s "paper test" asks — before generating a
repository. §5 below is a first-pass sketch of that survey, not a substitute for it.

## 1. What has been improvising a home

Three independent efforts have hit the same wall from different directions:
dismech's disease-centric, one-file-per-disorder schema has no natural place for a
dataset shaped like *many chemicals × many assay endpoints*, where each endpoint
is reusable across chemicals, papers, and diseases.

| Effort | Shape | Where it landed |
|---|---|---|
| [#12682](https://github.com/monarch-initiative/dismech/issues/12682) / [#12858](https://github.com/monarch-initiative/dismech/issues/12858), EPA ToxCast/Tox21 | 1,570 assay endpoints × 496 gene targets | `projects/TOXCAST.md`, a coverage report; candidate join on gene symbol, counted but not curated |
| [`docs/reports/dnt-ivb-pathograph-coverage-2026-10-02.md`](dnt-ivb-pathograph-coverage-2026-10-02.md) | 17 developmental-neurotoxicity battery processes | A coverage report; candidate join on node-name substring match |
| [PR #13452](https://github.com/monarch-initiative/dismech/pull/13452), the VAMR zebrafish behaviour assay | 26 endpoints × 17 chemicals × 2 exposure arms = 884 concentration-response fits | A coverage report plus a committed TSV; four chemicals with a candidate node, the rest with none |

All three are **candidate-matching exercises against the existing pathograph**, not
curated additions to it, and all three say so explicitly: a gene-symbol join or a
name match is "never a mapping," only a lead. None of the three data sets has
become KB content, and `projects/TOXCAST.md` worked one example all the way
through to a schema-valid `experimental_models` block to show what that would
actually cost.

**That worked example is the concrete case for a different home.** Writing the one
ToxCast endpoint TOX21_TRB_COA_Antagonist_Followup_ratio against
`Generalized_Resistance_to_Thyroid_Hormone`'s trigger node produces a valid
`ModelMechanismLink`. The paralogs show what that costs: four of THRB's 13
endpoints (`TOX21_TR_LUC_GH3_Agonist`, `TOX21_TR_LUC_GH3_Antagonist` and their
followups) name THRA and THRB together, so they belong equally in
`Resistance_to_Thyroid_Hormone_Alpha` — a different file, and the two copies
would share no identity. `TOXCAST.md`
states the general problem plainly: "`ModelMechanismLink.target` resolves only
within one disease file, and an `ExperimentalModel` is nested inside one
`Disease`. So the record above lives in
Generalized_Resistance_to_Thyroid_Hormone and nothing else in the repository
knows the endpoint exists." The same shape recurs for the 2,080 candidate
endpoint-node pairs ToxCast offers across 317 disease entries, for the DNT-IVB
battery's 1,157 distinct node links, and for whichever of the VAMR assay's 26
endpoints eventually get written up.

A design comment already on [#12858](https://github.com/monarch-initiative/dismech/issues/12858#issuecomment-5840570294)
proposed one fix that stays inside dismech: ingest ToxCast as a `StructuredSource`
(`TOXCAST:<aeid>`), the same pattern NCIT P302 and ClinGen assertions already use,
so any disease file can cite the same cached row instead of duplicating it. That
is real, available, and cheaper than a new repository. What it does not solve is
the part a Mech is built for: a Mech gives the assay endpoint its own evidence
discipline, its own history, its own review queue, and — through the cross-Mech
link convention in §4 — the same "cite, don't duplicate" fix available to
*every* Mech that wants to point at an assay, not only dismech.

## 2. What mechmaker actually provides

A generated Mech is a sibling repository to dismech, not a module inside it. It
gets: a LinkML schema with per-ontology descriptor classes and dynamic enums; a
`linkml-term-validator` + `linkml-reference-validator` pipeline identical in kind
to dismech's own; one record per YAML file; append-only history; a documentation
site; and optional GitHub automation (review, triage, curation-queue agents) —
the same stack this report is itself produced under.

Twelve Mechs exist today ([MechRegistry](https://monarch-initiative.github.io/mechregistry/registry/mechs.json),
snapshot served on 2026-10-03). Most are microbiology (AntibioticMech, CellStructureMech,
CommunityMech, CultureMech, HabitatMech, MediaIngredientMech, NaturalProductMech,
ProteinTraitsMech, TaxonMech, TraitMech — the `x-mech-suite`/`kg-microbe`
collection). Two sit in dismech's own territory: dismech itself, and **SOMAMech**
(§3).

## 3. SOMAMech is the neighbor this report has to take seriously

[SOMAMech](https://github.com/EHS-Data-Standards/somamech) is "a paper-extraction
knowledge base for environmental health sciences... One record per publication:
each record is a `Container` that holds the paper's study subjects, exposures,
protocols, assays and measurements, linked to Key Events and Adverse Outcome
Pathways." Its ontology list — CHEBI, GO, CL, UBERON, HP, PATO, ENVO, MONDO,
NCBITaxon, OBI, UO, PR, CLO, ECTO, ExO, XCO — is close to what a ToxAssayMech
survey would independently choose, and its schema already has `KeyEvent`,
`KeyEventRelationship`, `AdverseOutcomePathway` and `MolecularInitiatingEvent`
classes.

Two things keep it from being the same project as what dismech's three efforts
need, and one thing means the overlap has to be resolved deliberately rather than
assumed away.

- **The record is a publication, not an assay.** Its assay classes
  (`CiliaryFunctionAssay`, `CFTRFunctionAssay`, `GobletCellAssay`,
  `OxidativeStressAssay`, `EGFRSignalingAssay`, `LungFunctionAssay`,
  `MucociliaryClearanceAssay`, `ASLAssay`, `BALFSputumAssay`, `GeneExpressionAssay`,
  `FoxJExpressionAssay`...) are nested inside a `Container` and bespoke per
  assay type. A ToxCast or VAMR endpoint is the opposite shape: one endpoint
  measured identically across dozens of chemicals and (for ToxCast) more than
  one publication, where the thing worth a stable identity is the endpoint, not
  any one paper that used it. Importing ToxCast into SOMAMech's current schema
  would mean either a new bespoke assay class per endpoint family — `TOXCAST.md`
  names nuclear receptor, DNA-binding and kinase as the largest of several —
  which is the scale SOMAMech's existing per-assay-type classes already sit at,
  so this is not obviously wrong, or loosening `Container`'s publication-keyed
  identity to let an assay be shared across records, which is a bigger schema
  change than it looks from outside.
- **The domain, so far, is airway and pulmonary.** Every current record is a
  PM2.5/smoke/inhalation study. ToxCast is organism- and target-agnostic (nuclear
  receptors, kinases, DNA-binding proteins — thyroid, estrogen, androgen, far
  beyond airway biology); DNT-IVB and VAMR are developmental-neurotoxicity
  batteries. None of the three is SOMAMech's current subject matter, though
  nothing in its schema forbids extending into it.
- **Both projects would reach for the same primitive.** `KeyEvent` and
  `KeyEventRelationship` already exist in SOMAMech's schema. A second Mech
  minting its own Key Event identifiers, independently, is the sort of
  fragmentation MechRegistry's `shares_vocabulary_with` / `consumes` /
  `hands_off_to` relations exist to prevent, and `survey-domain`'s neighbor step
  says plainly: "If an existing Mech already records this entity, say so first.
  Extending it may be better than starting a new one." That conversation has not
  happened yet — this report is not it.

**This is the actual blocker to a go/no-go answer**, not any technical gap in
mechmaker. A scoping conversation with SOMAMech's maintainer (Sierra Moxon,
EHS-Data-Standards) belongs before `copier copy`, not after.

## 4. Cross-Mech linking is the part that actually fixes the duplication problem

`design-mech-schema`'s documented pattern: "A link to another Mech's record is a
`Term`-like pair `{id, label}` where `id` is that Mech's record id. Say in
DOMAIN.md which Mech and how the link is checked." This is precisely what
`TOXCAST.md`'s worked example found missing — a `ModelMechanismLink.target`
inside one dismech disease file has no identity any other file, or any other
Mech, can point at.

If assay endpoints lived in a ToxAssayMech instead, the THRA/THRB duplication in
§1 collapses to one endpoint record cited twice, by id, from two dismech files —
and from SOMAMech, and from any future Mech that wants the same endpoint. That is
the strongest argument for a separate Mech over the in-repo `StructuredSource`
alternative floated on #12858: a `StructuredSource` fixes this for dismech alone,
where cross-Mech linking fixes it for every consumer at once, at the cost of a
second repository to maintain and review.

## 5. A first-pass survey, against `survey-domain`'s six questions

This is a sketch to show the shape of the real decision, not the deliverable
itself — `make-mech`'s own instruction is "do not skip to step 3," and a proper
survey needs the SOMAMech conversation in §3 folded in before it is final.

**1. The record.** "One record is one assay **endpoint**": a named readout, in a
named system, aimed at a named target or process, independent of which chemical
or paper exercised it — not one record per publication (SOMAMech's choice,
appropriate to deep single-paper extraction) and not one record per
chemical-by-endpoint **result** (ToxCast alone is 1,570 endpoints × tens of
thousands of chemicals; #12682 already deferred exactly this as a separate,
much larger question, and a hit-call is a measurement to cite, not a claim
someone argues about mechanistically in the way `survey-domain` asks a record
to be). Three things people might expect to be records that are not: a
chemical (its own record elsewhere — CHEBI, or a future chemical-focused Mech);
a hit-call (a `Dataset`/structured-source fact attached to an endpoint record,
not a record of its own); an Adverse Outcome Pathway (AOP-Wiki's own entity,
consumed, not owned).

**2. Identity.** No single ontology keys "assay endpoint" one-to-one. OBI grounds
the assay *method* (reachable from `OBI:0000070`, already in mechmaker's default
catalog), not a specific endpoint instance; ToxCast's AEIDs are EPA's own
integers with no CURIE; AOP-Wiki's Key Event identifiers
(`aop.events`, registered in Bioregistry) resolve as URLs but have no OAK
adapter or term cache, so `linkml-term-validator` cannot check them the way it
checks an OBI or GO term — the same gap
[`projects/AOP_EMOD_ALIGNMENT.md`](https://github.com/monarch-initiative/dismech/blob/main/projects/AOP_EMOD_ALIGNMENT.md)
(open schema question 3, "Should the AOP-Wiki prefixes be declared in the schema?")
names for dismech's own schema. mechmaker's `identity_prefix` is built for
exactly this case — leave it empty and mint ids in the Mech's own namespace,
the path AntibioticMech already takes for structures with no ChEBI term. A
Key Event's own `aop.events:<n>` identifier is still worth recording, as a
cross-reference field, not as the record's key.

**3. Grounding.** Target/process: GO (already default). System: CL, UBERON.
Species: NCBITaxon. Chemical/stressor: CHEBI. Method: OBI. Quantitative
readout units: UO. Action/qualifier, matching AOP-Wiki's own Key Event
Component model of action+object+process: PATO. All six are in mechmaker's
standard ontology catalog, selected at generation time with no extra work.
Exposure route and context (ECTO, XCO — both already used by dismech's own
`environmental` block and by SOMAMech) are not in the default picklist but are
supported as `extra_ontologies`, same as any OAK-readable source.

**4. Sources.** EPA's CTX API (ToxCast/Tox21 bioactivity, ~1,570 endpoints,
documented in dismech's own `epa-ctx-api` skill, needing a free API key);
AOP-Wiki's bulk XML (already has a working CLI, `aop_wiki_cli`, used by
dismech's `aop-wiki` skill); individual battery papers with supplementary
concentration-response tables, of which the VAMR report is itself one worked
example, and whose own findings — a dataset DOI that does not resolve, a
supplement whose licence terms are unstated — are exactly the kind of
source-quality problem a Mech's evidence pipeline exists to catch rather than
to inherit silently. Whether deep research would help: only weakly — most of
what this domain needs is reading a named, bounded set of agency datasets and
supplementary tables, not a literature sweep across an open question.

**5. Neighbors.** SOMAMech, discussed at length in §3, is the one that
matters. dismech is a consumer (it would cite ToxAssayMech records from
`modeled_mechanisms`, as §4 describes), not a competing scope.

**6. Mechanism.** Yes, clearly — MIE → KE → KER → AO is a causal graph, and
mechmaker's generic causal-graph pattern (`MechanismNode`, `downstream` edges,
evidence per edge) is built to hold exactly that shape; it is the same backbone
dismech's own pathograph uses. The caveat is evidentiary, not structural:
`ker-evidence-triage` found 1,536 of 2,369 AOP-Wiki KERs (65%) sitting at the
record's evidence floor with zero references, and 69% with no citation at all.
A ToxAssayMech cannot bulk-import that graph as curated causal content any more
than dismech could; every edge would need the same per-KER evidence read dismech
already built tooling for, which is real, ongoing curation labor rather than a
one-time ingest.

## 6. What this report does not settle

- **Whether SOMAMech should be extended instead of a new Mech created.** That
  is EHS-Data-Standards' call to make jointly with whoever drives this, not a
  question this document can close alone.
- **The record-granularity question for AOP Key Events specifically** — whether
  a Key Event is its own record type inside the Mech, or purely a
  cross-reference field on an assay-endpoint record, the way §5's sketch
  assumes. `design-mech-schema`'s "paper test" (two real records, one typical
  and one awkward, written out in full) is the way to find out, and it has not
  been run.
- **Licensing of the source data this Mech would quote.** ToxCast/Tox21 is US
  federal public domain; AOP-Wiki's terms were not checked for this report;
  the VAMR article is CC BY but its supplementary workbook's terms are
  "not stated," exactly as that report records. A Mech's evidence pipeline
  needs an answer per source before quoting it, not an assumption.
- **Who would curate it.** A fourth repository with its own review queue and
  automation is ongoing maintenance load, independent of whether the schema
  design is sound.

## Provenance

Read against mechmaker `main` ([`monarch-initiative/mechmaker`](https://github.com/monarch-initiative/mechmaker))
and SOMAMech `main` ([`EHS-Data-Standards/somamech`](https://github.com/EHS-Data-Standards/somamech))
on 2026-10-03, both cloned read-only for this report and not vendored into
dismech. The MechRegistry figures are the `mechs.json` snapshot served at
<https://monarch-initiative.github.io/mechregistry/registry/mechs.json> on the
same date. dismech-side figures are quoted from `projects/TOXCAST.md`,
`docs/reports/dnt-ivb-pathograph-coverage-2026-10-02.md`, the `ker-evidence-triage`
skill, and PR #13452's own report, all as committed or open on 2026-10-03; none
were re-derived independently for this report. Nothing in `kb/`, the schema, or
any cache was read or written.
