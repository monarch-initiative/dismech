# FOXE3: an ICD mapping conflict and a separate disease-scope question

**The confidence-0.5 result is a conflict between two MONDO-to-ICD-11
mappings.** Both best solutions accept the FOXE3 entry's mapping to MONDO.
Current WHO definitions and hierarchy support retaining the anterior segment
dysgenesis mapping and changing the mapping to its broader ICD parent from
identity to a broader-target relationship. A proxy merge would erase a useful
scope distinction.

**The FOXE3 entry also needs an explicit scope qualification, but should retain
its combined cataract/aphakia spectrum.** ClinGen deliberately groups those
FOXE3 presentations together and uses the same broad MONDO identifier. That
explains the grounding choice; it does not make every anterior segment dysgenesis
FOXE3-related.

This investigation checks the saved input against current source context on
2026-09-20. All proposed changes below remain proposals. Production KB records,
Boomer inputs, and saved solutions are unchanged.

## Entities in play

| ID | Source label | Gene context | Relevant parent or scope |
|---|---|---|---|
| `dismech:FOXE3_Anterior_Segment_Dysgenesis` | FOXE3-Related Anterior Segment Dysgenesis | FOXE3 | Entry includes dominant cataract/anterior-segment presentations and recessive primary aphakia |
| `MONDO:0019503` | anterior segment dysgenesis | Genetically heterogeneous; child examples include FOXE3, PITX3, CPAMD8 | Explicit `disease_grouping` in current MONDO; the entry's present grounding |
| `DOID:0060648` | anterior segment dysgenesis | Not independently reviewed here | One of the unopposed exact mappings in the saved analysis |
| `ORDO:88632` | Anterior segment developmental anomaly | Not independently reviewed here | MONDO records this as an Orphanet group of disorders; label from saved input |
| `icd11f:1182282997` | Anterior segment dysgenesis | No gene restriction stated in the retrieved WHO definition | Child of the next ICD category |
| `icd11f:943599144` | Structural developmental anomalies of the anterior segment of eye | No gene restriction stated in the retrieved WHO definition | Broader category; children also include Blue sclera and Heterochromia |
| `MONDO:0012456` / `OMIM:610256` | congenital primary aphakia | Direct FOXE3 gene annotation in MONDO | Anterior segment dysgenesis child; covers only part of the dismech spectrum |
| `MONDO:0013067` / `OMIM:612968` | cataract 34 multiple types | Direct FOXE3 gene annotation in MONDO | Child of cataract; covers the other named presentation |
| `MONDO:0007138` / `OMIM:107250` | anterior segment dysgenesis 1 | Direct PITX3 gene annotation in MONDO | Non-FOXE3 child of the anterior segment dysgenesis grouping |
| `MONDO:0015017` / `OMIM:617319` | anterior segment dysgenesis 8 | Direct CPAMD8 gene annotation in MONDO | Another non-FOXE3 child of the grouping |

The grouping's gene examples come from its child records; they are neither an
exhaustive gene list nor predictions by Boomer. Current MONDO stanzas, OAK context,
and versioned WHO responses are preserved in [source-context.json](source-context.json).

## Source context and curation judgment

### ICD: prefer a directional mapping to the parent

The [WHO anterior segment dysgenesis record](https://icd.who.int/browse/2026-01/foundation/en#1182282997)
describes an antenatal developmental condition with characteristic iris, pupil,
corneal, and iridocorneal abnormalities. Its [parent category](https://icd.who.int/browse/2026-01/foundation/en#943599144)
covers anterior-segment developmental anomalies generally. The same parent also
contains [Blue sclera](https://icd.who.int/browse/2026-01/foundation/en#1050179356)
and [Heterochromia](https://icd.who.int/browse/2026-01/foundation/en#84750333).
These provide positive scope context beyond the existence of a hierarchy edge:
the parent organizes several different kinds of anomaly. This does not assert
that its children are disjoint or cannot coexist in a patient.

Current MONDO still marks **both** ICD xrefs `MONDO:equivalentTo`. The parent's
xref cites Orphanet:88632 and a curator ORCID; neither ICD target is marked
`MONDO:preferredExternal`. There is no automatic proxy permission for the pair.

**Recommended MONDO change:** keep equivalence to the ICD anterior segment
dysgenesis concept, and replace equivalence to the structural-anomalies parent
with `MONDO:mondoIsNarrowerThanSource`. The target is broader than MONDO, which
corresponds to `skos:broadMatch` from MONDO to ICD. This is a source-informed
curation recommendation, not something the solver can choose from its score.
The scope of the retained exact match can still receive ophthalmology review;
the evidence does not justify merging the two WHO concepts.

### FOXE3: preserve the combined clinical spectrum and qualify the grounding

[ClinGen's FOXE3 curation](https://search.clinicalgenome.org/kb/gene-validity/CGGV:assertion_d9cf89fb-ebb9-4c38-8b8c-97d9ce5af270-2023-07-20T160000.000Z)
explicitly combines anterior segment dysgenesis 2 (OMIM:610256) and cataract 34
(OMIM:612968) into a single FOXE3-related entity. It uses MONDO:0019503 and records
semidominant inheritance and a definitive association. Its rationale is the
clinical spectrum across the historically separate diagnoses. This supports
keeping the scope of our entry rather than narrowing it to primary aphakia.
The [primary clinical/functional study](https://pubmed.ncbi.nlm.nih.gov/34046667/)
also distinguishes severe recessive presentations from dominant extension-allele
presentations while studying them within FOXE3-related ocular disease.

The MONDO grouping includes PITX3- and CPAMD8-associated diseases as well as
FOXE3-associated primary aphakia. A gene-disease association using the grouping
is not an equivalence between the grouping and one gene's disease spectrum.
The current generator nevertheless gives an unqualified `disease_term` mapping
an identity prior of 0.9.

**Recommended dismech follow-up:** retain the broad term as a grounding, but
record explicitly that the MONDO target is broader (`skos:broadMatch`, from the
entry to MONDO), with the ClinGen scope rationale. Consider binding the two
named subtypes to the checked aphakia and cataract terms after reviewing their
coverage. A dedicated MONDO FOXE3-related ocular-disease term would be a better
long-term match for the combined spectrum; its introduction needs upstream
curation, not a unilateral relabeling of the existing grouping.

A search of every term frame in the pinned current MONDO source for `FOXE3` or
its HGNC URI found primary aphakia, cataract 34, the broad grouping (with a
related/excluded FOXE3 synonym), and aortic-aneurysm susceptibility. It did not
find a dedicated combined ocular-spectrum class. The query and complete hits
are recorded in the source artifact. Lack of an asserted cataract-to-ASD path
is not itself evidence that cataract lies outside the clinical spectrum.

## What the solver actually distinguishes

The seven-hypothesis input has **48** consistent complete assignments. The two
best have the same whole-assignment prior (0.034804709438) and posterior
(0.391553372725 each). They differ only in the ICD equivalence they accept:

| Distinct solution | MONDO = ICD anterior segment dysgenesis | MONDO = ICD structural-anomalies parent | FOXE3 entry = MONDO grouping | Whole-solution posterior |
|---|---|---|---|---:|
| Saved optimum | Reject | Accept | Accept | 0.391553372725 |
| Equally good alternative | Accept | Reject | Accept | 0.391553372725 |

Both ICD hypotheses have prior **0.95** and marginal posterior
**0.487179487179**. Confidence is `P(best)/(P(best)+P(next best)) = 0.5`.
Independent exhaustive enumeration reproduces the saved assignments, confidence,
posterior, all seven marginals, and number of consistent solutions. This is a
real tie between different solutions, not duplicated search paths.

### Controlled changes on copies of the input

| Experiment | Confidence | Consistent assignments | Interpretation |
|---|---:|---:|---|
| Original saved input | 0.5 | 48 | Two competing ICD equivalences |
| Qualify only the dismech grounding as broad match | 0.5 | 48 | Resolves the separate gene-scope assumption; ICD tie remains |
| Replace the parent ICD equivalence with proper subsumption at the same 0.95 prior | 0.9 | 64 | Both ICD relationships can be accepted |
| Make both directional changes | 0.9 | 64 | Both scope distinctions represented |
| Remove only the parent ICD equivalence from the saved model | 0.9 | 32 | Illustrates excluding the disputed exact link |

The first directional experiment preserves all other priors and hard facts.
The dismech experiment uses the generator's existing broad-match prior triple:
identity 0.05, entry narrower than MONDO 0.90, reverse direction 0.03. The full
hypothesis lists, top five distinct assignments, and marginals are in
[experiments.json](experiments.json).

**Pipeline limitation:** the cross-source generator currently reads MONDO's
confirmed exact matches. Annotating an xref as broader does not automatically
produce the seven-hypothesis directional experiment above; that experiment is
an explicit counterfactual. Removing an exact xref can also change which external
terms and constraints are gathered on regeneration. The removal experiment
keeps the saved hard facts and therefore is not claimed as a complete regenerated
input. A future refresh must inspect the generated facts before reporting a new
production confidence.

<details>
<summary>Provenance, reproducibility, and separate curation follow-ups</summary>

- Dismech checkout: `b08020effcb` (fresh from main after the analysis and skill PRs merged).
- MONDO source: `eeb1a1b1d89d740e522225b1a5e4a516fa7f6a0a`,
  [pinned mondo-edit.obo](https://github.com/monarch-initiative/mondo/blob/eeb1a1b1d89d740e522225b1a5e4a516fa7f6a0a/src/ontology/mondo-edit.obo).
  The source artifact includes its checksum and grammar-parsed selected stanzas.
- WHO Foundation: release `2026-01`, English, API v2; request URLs and returned
  records are saved. The public browser's session authentication was used;
  no authentication material is retained.
- Local OAK context has separate version IRIs and database checksums. It is
  supporting context, not a claim that today's databases produced the historical
  input. The saved input itself is the solver baseline.
- Input SHA-256:
  `f701d83511d37b2fc769a9d2c090fc59e25faf1e3d8b7a9be686599e8015f154`.
- Solver: clean Boomer checkout `744038e30741009930f57919ca2f03c6473ed198`.
- Enumeration has a 60-second limit per scenario and reads production files
  without modifying them. The script checks their bytes again after execution.

Run from the repository root with the normal dismech Python environment:

```bash
PYTHONPATH=src uv run --with networkx python analyses/boomer/foxe3/investigate.py \
  --boomer-src /path/to/boomer-py/src
```

The report also exposes two **separate** evidence-maintenance issues:

- The entry cites a cached 2025 ClinGen assertion as Moderate/undetermined
  inheritance. Its linked live page currently returns an invalid-identifier
  error; the checked 2023 assertion is a different accession. This discrepancy
  needs a source/cache audit, not an assumption that one record superseded the
  other. No cache or evidence item was changed here.
- ClinGen's narrative associates MONDO:0014508 with anterior segment dysgenesis 2,
  but current MONDO assigns that ID to IMPG1-related vitelliform macular dystrophy
  4. The matching OMIM:610256 xref is on MONDO:0012456; the narrative ID should
  not be copied into a binding. The selected source stanzas permit that check.

The entry's simple dominant-haploinsufficiency explanation also warrants a
separate mechanism review: [functional work](https://pubmed.ncbi.nlm.nih.gov/25504734/)
distinguishes altered dominant protein function from simple haploinsufficiency.
That question does not determine which ICD mapping caused this tie.

</details>
