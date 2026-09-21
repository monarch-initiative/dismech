# Representing senescent cells in DisMech

Local research and design exploration for Chris Mungall, 2026-09-20.
Repository baseline: `1cc412fddde5aacb0cc66311a96e25d67465fdb9`.
The initial exploration was followed by Chris's explicit request to update the
existing senescence module locally. The bounded curation described below is now
applied to that module; the production schema is unchanged. Chris subsequently
requested a pull request containing the curation and its supporting design record.

## Recommendation

Use **CL identity plus a contextual senescence mechanism** with the existing
schema now. Keep the senescent population, its secretory activity, immune
recognition or escape, clearance, and accumulated burden as distinguishable
claims. Put marker observations in `biochemical.readouts` or model-specific
`ExperimentalReadout` objects; a marker is evidence about a state, not the state
itself. Specialize the existing modules in disease entries rather than creating
a disease called “senescent cell.”

Following Chris's design feedback, **reuse biological processes rather than
introducing a separate cell-state vocabulary**. This also accommodates normal
processes and cell-cycle phases. A future relation qualifier can distinguish
participation or causal involvement from temporal context. The `cell_states`
prototype below is retained as an investigated alternative, not the selected
direction. Reusing BP does not by itself solve which participant the process
applies to on a mixed-cell node; that remains a relation/scoping requirement.

The decisive question is not whether “senescent cell” sounds like a cell type.
It is whether the representation preserves **which cell population has which
state, in which setting, supported by which observation**. The current schema
can communicate that to readers; its automated queries and exports preserve
less of it.

## Paper identity and reading record

The supplied PDF identifies itself on page 1 as:

- **Title:** *Escape and evasion: when immunosurveillance of senescent cells goes wrong*
- **Authors:** Elina Shakur; Abraham Jacobs; Rituparna Ghosh; Matthew J. Yousefzadeh.
- **Publication:** *Frontiers in Genetics*, volume 17, article 1882818; Mini Review;
  published 7 July 2026.
- **DOI:** [10.3389/fgene.2026.1882818](https://doi.org/10.3389/fgene.2026.1882818).
- **Independent identity check:** [PubMed PMID:42518598](https://pubmed.ncbi.nlm.nih.gov/42518598/)
  agrees with the PDF; PMCID: PMC13384439. Identity was read from the PDF before
  looking up these database identifiers.

Source file: the supplied `doc_ac0569aee4af_fgene-17-1882818.pdf`, retained outside
the repository.
SHA-256: `4eec4659227597d37717344de0e6fe527861f78f33cb9834e4f279dd38a53701`.
All nine pages were read, including the references and declarations on pages
7–9. Figures 1 and 2 were inspected as rendered images, not just extracted
captions. Page citations below use the printed PDF pages 01–09, which match
the PDF page indices counted from one. Extracted full text and page images were
kept in `/tmp/dismech-senescence-investigation/`, outside the repository.

This is a narrative mini review, not a new experimental dataset or a validated
senescence classifier. “The review reports” below identifies its claims; the
representation choices and cautions are this investigation's interpretation.

## What the paper contributes to the representation

| Paper claim or distinction | Exact location in supplied PDF | Modeling implication |
|---|---|---|
| Senescent cells remain metabolically active despite impaired proliferation; they can contribute to development, wound healing, and tumor suppression. | p. 1, Abstract and Introduction; p. 6, Conclusion | Cell-cycle behavior, cell identity, and functional consequence are distinct. Senescence is not necessarily deleterious. |
| Durability depends on cell type and stimulus. The review discusses escape from oncogene-induced senescence and contrasts it with more durable replicative arrest. | p. 2, “Senescent cells and their role in inflammaging,” first paragraph | Preserve inducing mechanism and observation context; do not make irreversibility an unconditional property of every record labeled senescent. |
| No universal marker exists. Features include p16INK4a/p21CIP1, DNA-damage signaling, nuclear/chromatin changes, morphology, and SA-beta-gal activity at pH 6.0. | p. 2, same section and Figure 1; figure includes reduced lamin B1, TAFs, SAHF, DNA-SCARS, CCFs, LINE-1 and mitochondrial DNA release | Record assay observations separately. A feature panel is supportive evidence, not an exhaustive definition or a conjunction all cells must satisfy. |
| SASP composition varies with cell type and trigger and includes more than cytokines: chemokines, proteases, growth factors, vesicles, lipids and nucleic acids. | pp. 2–3, same section | SASP is a secretory program; any one mediator or generic cytokine GO term is only a partial description. |
| Secreted factors recruit immune cells, reinforce senescence locally, and induce paracrine senescence. Persistent inflammation and senescence can reinforce one another. | p. 3, same section | Distinguish source and responding populations. Give feedback edges their own evidence; do not collapse recruitment, cytotoxicity and clearance into one event. |
| In acute cutaneous wounds, senescent fibroblast PDGF-AA promotes differentiation of non-senescent fibroblasts into myofibroblasts. | p. 3, “Immune-mediated clearance of senescent cells” | A responding fibroblast does not inherit the source cell's senescent state. A repair response is not automatically pathological fibrosis. |
| NK cells, macrophages, T cells and other immune populations contribute different recognition, recruitment and clearance functions. | pp. 3–5, same section; p. 4, Figure 2 | Record effector identity separately from senescent target identity. NKG2D ligand recognition, granule killing and phagocytosis are different mechanisms. |
| Target-side evasion includes inhibitory ligands, shedding of activating ligands, suppressive secretions and possible matrix effects. | p. 5, “Mechanisms of immune evasion by senescent cells” | Represent specific evasion mechanisms in the context supported by the source, rather than assigning a universal “immune-evasive” senescent subtype. |
| Immunosenescence includes shifts in immune-cell populations and function; exhausted, senescent and otherwise dysfunctional immune cells are explicitly distinguished. | pp. 5–6, “Immunosenescence impairs immunosurveillance” | Organism-level immune aging is not synonymous with cellular senescence of every immune participant. Neither an inhibited NK cell nor an exhausted T cell is automatically senescent. |
| Immune restoration, checkpoint interventions and engineered immune-cell therapies are discussed, but it remains uncertain whether some benefits reflect restored senescent-cell surveillance or other mechanisms. | p. 6, same section and Conclusion | Separate intervention targets, biomarker changes and clinical outcomes. The review does not establish a general human treatment recommendation. |

“Escape” itself needs two meanings: **escape from proliferative arrest** (p. 2)
and **escape from immune elimination while remaining senescent** (p. 5).
They should have different nodes and descriptions.

The page 5 evasion mechanisms also need different participant roles. Except for
the independently checked HLA-E example below, these are review-derived leads
for disease-specific primary-source curation, not completed evidence assertions:

| Review mechanism (p. 5, “Mechanisms of immune evasion by senescent cells”) | Representation to preserve |
|---|---|
| CD47–SIRP-alpha inhibition of phagocytosis | CD47-bearing target and SIRP-alpha-bearing phagocyte; neither receptor alone establishes senescence. |
| HLA-E–NKG2A inhibition | Senescent fibroblast target and NK/CD8 effector are different populations. |
| Shedding of activating NKG2D ligands | Distinguish reduced surface ligand availability from soluble ligand abundance and subsequent effector dysfunction. |
| PD-L1–PD-1 signaling | Keep target checkpoint expression and effector inhibition separate; the review's PD-1-positive macrophage discussion is another context. |
| GD3-associated immune escape | Preserve the cited mouse lung-fibrosis setting; do not silently generalize it to every human senescent cell. |
| FasL-mediated killing of T/NK cells | Here the immune effector dies; this is different from immune killing of the senescent target. |
| IL-10/TGF-beta and myeloid-derived suppressor-cell recruitment | Separate secretion, recruitment and suppressive function; recruited cells do not inherit the source's state. |

The immune-aging discussion on pages 5–6 adds a separate source of impaired
clearance. A larger senescent-cell burden cannot, by itself, distinguish increased
state induction, target-side escape, or reduced effector competence.

### Source details that should not be copied uncritically

1. **HLE-A on page 5 is inconsistent with the cited primary source.** Pereira
   et al. identify **HLA-E**, the ligand for inhibitory NKG2A, in senescent
   dermal fibroblasts and in their endothelial-cell experiments. Their
   perturbation evidence is in vitro; human tissue observations support
   expression/localization, not clinical efficacy of blockade. Read the
   [primary study, Results and Figure 1](https://www.nature.com/articles/s41467-019-10335-5).
   Preserve exact source spelling in any quotation and explain the discrepancy;
   do not reproduce it in a gene or protein binding.
2. **The review's HLA-E/CD4 sentence needs correction against its citation.**
   Page 5 links cytotoxic CD4 recognition to MHC-II and then HLA-E while citing
   Hasegawa et al. That study's abstract instead specifies HCMV glycoprotein B
   and **HLA-II-dependent** recognition of senescent skin fibroblasts. This is
   antigen- and tissue-context-specific clearance, not generic HLA-E recognition
   by CD4 cells. [Hasegawa et al., PMID:37001502](https://pubmed.ncbi.nlm.nih.gov/37001502/).
3. **Figure 2 contains misleading labels.** On p. 4, the senolytic arrow is
   labeled “Induces anti apoptotic pathways,” although the caption describes
   induction of apoptosis and the review's conclusion discusses targeting
   anti-apoptotic pathways. Its MHC-I/CD4 and MHC-II/CD8 labels also appear
   interchanged relative to the conventional pairings and the cited CD4 study.
   Do not transcribe these labels into causal edges. Figure 1 is useful as a
   feature inventory, but neither schematic is experimental evidence.
4. **Other p. 5 claims remain leads.** The CD47 citation is an atherosclerosis
   study, the NKG2D-ligand-shedding citation names multiple myeloma, the GD3
   citation is a commentary, and the ECM example concerns senescent mesenchymal
   stromal/stem cells and breast-cancer behavior. Their bibliography entries
   (pp. 7–9) do not establish that each mechanism applies to all senescent
   fibroblasts. Their underlying experiments were not independently assessed
   here and should be before disease-specific promotion.
5. **The wound-study evidence has a publication-status caveat.** Follow-up
   checking found an [Expression of Concern, PMID:42412492](https://pubmed.ncbi.nlm.nih.gov/42412492/)
   for Demaria et al.'s 2014 study (PMID:25499914), published online 29 May 2026.
   The wound fixture now flags this and remains an illustration of how to encode
   the review's claim, not an established positive-evidence benchmark. The notice
   metadata was verified; no conclusion about misconduct or the validity of each
   individual experimental result is inferred from that metadata.

The [MICSE guidance, PMID:39121846](https://pubmed.ncbi.nlm.nih.gov/39121846/),
cited on p. 8, was also checked. Its recommendations favor at least three markers
from different senescence properties, with at least two co-detected in the same
sample/time, ideally the same cells, and context-dependent arrest evidence. It gives specific
caveats for cancers and non-mammalian systems and stresses uncertainty in human
tissues. This is a useful curation checklist, **not a deterministic three-positive-
markers classifier**. A bulk cytokine signal, two markers measured in different
cell populations, or reduced proliferation alone should not automatically produce
a senescent-cell assertion.

## What DisMech represented at the investigation baseline

The full `CLAUDE.md`, applicable `AGENTS.md`, and the PDF, `extend-schema`,
`dismech-terms`, and `dismech-references` skills were read. The module follow-up
also used `create-module` and the modules-and-conformance primer. The relevant design
constraints are [decision register §§1–6 and §12](../explanation/design-decisions.md):
mechanism-first scope, reuse of ontologies, modules as conformance rather than
inheritance, Biolink at export only, exact evidence quotations, and deferred
decisions about composite measures and context-dependent effects. The
[evidence-model explanation](../explanation/evidence-model.md) further argues
against adding ungrounded confidence grades.

### Baseline content and concrete reuse points

| Existing record | Representation observed | Consequence for this design |
|---|---|---|
| [`cellular_senescence`](../../kb/modules/cellular_senescence.yaml) | Five nodes: inducing stress → arrest → SASP / accumulation → tissue dysfunction; p16 and SA-beta-gal readouts; senolytic target; animal, experimental and computational models | Already the main reusable pathological module. Its SASP node binds “Senescent Fibroblast” to CL fibroblast; there is no need to invent a duplicate module for that representation alone. |
| [`senescence_tumor_suppression`](../../kb/modules/senescence_tumor_suppression.yaml) | Protective arrest and a distinct loss-of-stemness branch converge on a transformation/progression barrier | Preserve the protective/deleterious distinction. Its notes explicitly reject p16/p21/SA-beta-gal alone as proof of the tumor-suppressive arrest. Loss of stemness is not a senescence marker. |
| [`inflammaging`](../../kb/modules/inflammaging.yaml) | SASP is one of several inflammatory inputs; chronic inflammation and propagation are separate nodes | Inflammaging is neither identical to SASP nor proof of a particular senescent cell population. |
| [`Osteoarthritis`](../../kb/disorders/Osteoarthritis.yaml) | “Chondrocyte Senescence,” CL chondrocyte, articular-cartilage location, GO cellular senescence, conformance to accumulation; downstream matrix catabolism | Existing identity + mechanism + tissue pattern works. Its evidence must retain the distinction between experimental OA and human disease. |
| [`Idiopathic_Pulmonary_Fibrosis`](../../kb/disorders/Idiopathic_Pulmonary_Fibrosis.yaml) | “AT2 cell senescence and SASP” and “Senescent myofibroblast persistence and apoptosis resistance” distinguish epithelial and mesenchymal populations; organoid and animal models carry limitations | Already richer than a generic senescent-fibroblast summary. Do not overwrite its immune-free organoid result with a claim that immune recruitment is universally required. |
| [`Activated_PI3K-delta_Syndrome`](../../kb/disorders/Activated_PI3K-delta_Syndrome.yaml) | “Senescent T-cell skewing,” separate CD4/CD8 CL bindings and GO cellular senescence | A real immune-cell-state case. The prose also says “exhausted”; those concepts need independent support rather than automatic equivalence. |
| [`Pilocytic_Astrocytoma`](../../kb/disorders/Pilocytic_Astrocytoma.yaml) | Neural stem-cell identity, oncogene-induced senescence, and a separately evidenced low-grade progression barrier | A disease-specific protective branch; reduced proliferation and tumor progression are different claims. |
| [`Werner_Syndrome`](../../kb/disorders/Werner_Syndrome.yaml) | Skin-fibroblast identity and GO replicative senescence; a separate adipogenic-failure mechanism | Retain replicative specificity and the limits of patient-cell and model evidence. |

The reproducible inventory is [kb-scan.json](senescent-cell-representation/kb-scan.json),
generated by [scan_kb.py](senescent-cell-representation/scan_kb.py).
It scans `pathophysiology` only: case-insensitive `senesc` in a node name, or a
direct binding to one of GO:0090398, GO:0090399, GO:0090400, GO:0090402 and
GO:0090403. It excludes prose-only mentions elsewhere and inferred ontology
closure. Thus these counts are an operational inventory, not a prevalence estimate
or an exhaustive count of senescence biology in the KB.

| Scope | Files scanned | Matching files / nodes | Nodes with cell types | With multiple cell types | With node-level locations | With conformance |
|---|---:|---:|---:|---:|---:|---:|
| Diseases | 3,044 | 39 / 44 | 30 | 8 | 12 | 15 |
| Modules | 177 | 7 / 10 | 2 | 1 | 0 | 0 |

Only one matching module node and no matching disease node put “senesc” into
a cell's `preferred_term`. Consequently, searching display labels alone misses
almost all of this material. Nodes without `cell_types` are not necessarily
defective: some describe a generic stress, burden, or downstream consequence.

Read-only issue searches for `senescence` and `"cell state"` also found relevant
prior work. [#3675](https://github.com/monarch-initiative/dismech/issues/3675)
addresses IPF ordering and feedback;
[#8488](https://github.com/monarch-initiative/dismech/issues/8488) nominates
AEC/immune-remodeling mechanisms. These are curation leads, not ratified
cell-state schema decisions. The searches were limited to 30 results each;
no claim is made that every historical discussion was found.

### Existing slots and their limits

The authoritative source is [`dismech.yaml`](../../src/dismech/schema/dismech.yaml),
especially `Descriptor`, `CellTypeDescriptor`, `Pathophysiology`, `Biochemical`,
`BiomarkerReadout`, `ExperimentalReadout` and `EvidenceItem`.

- **Identity:** `CellTypeDescriptor.term` is constrained to the CL cell hierarchy.
  Its `preferred_term` and `description` can add a justified state; changing the
  canonical `term.label` cannot.
- **Location:** `Pathophysiology.locations` scopes a mechanism. Inherited
  `CellTypeDescriptor.located_in` can locate an individual participant, so tissue
  specificity alone is not a reason for a new class.
- **State/process:** `biological_processes` can bind GO senescence. `modifier`
  expresses a direction or qualitative activity, not a senescent-state tag.
  `biological_scale: CELLULAR` identifies scale, not state.
- **Mechanism context:** descriptions, notes, triggers and model descriptions
  can capture stressor, species, culture/in-vivo setting and time. Disease
  `subtypes` can scope relevant mechanisms, but cellular senescence is not
  itself a disease subtype. Clinical onset/temporality are not a general
  experimental time-since-induction schema.
- **Observations:** `Biochemical` supports `cell_types`, `context`, `assays`,
  `specificity` and observational `readouts`. Model-specific measurements belong
  on `modeled_mechanisms[].readouts`, retaining model context and limitations.
  Do not invent numerical specificity or a comparator the source does not give.
- **Evidence:** nodes, edges and readout links can have separate evidence.
  `CellTypeDescriptor` itself currently has no evidence slot or state slot.
- **Causal wiring:** `downstream.target` uses bare node names. It has no general
  signed-effect slot; express inhibition with a node such as “Reduced NK
  cytotoxicity,” not an invented inhibitory `CausalEdge` property. Treatment
  links have their own `treatment_effect` semantics.

Two independent lists on a node do **not** pair their elements: a node listing
fibroblast and NK cell alongside cellular senescence does not formally say which
cell is senescent. Splitting nodes and explaining participant roles reduces this
ambiguity, but does not make each cell an independently referenceable population.

This matters in export. [`kgx_export.py`](../../src/dismech/export/kgx_export.py)
emits disease→CL `has_participant` and disease→GO associations separately. CL
identity is used as the exported node ID, and a preferred display label can be
used as its name. It does not create a distinct “senescent fibroblast in this
tissue” entity or preserve the cell-state/process pairing. Nested `located_in`
is also not the same export route as `Pathophysiology.locations`.
[`graph.py`](../../src/dismech/graph.py) retains cell labels as mechanism metadata,
rather than giving these populations their own graph identities. A schema
extension would need explicit renderer/export work to improve this.

## Ontology lookup results

Live OLS queries were made on 2026-09-20, using the services selected by
[`conf/oak_config.yaml`](../../conf/oak_config.yaml). The returned CL version was
**2026-06-08**, GO **2026-07-26**, and NCIT **26.02d**. Retrieval date is not the
ontology release date. The selected-term lookup records, parent and ancestor
results, URLs and service metadata are in
[ontology-terms.json](senescent-cell-representation/ontology-terms.json).

| Identifier | Verified canonical label | Appropriate use |
|---|---|---|
| CL:0000057 | fibroblast | Generic identity when tissue is not established |
| CL:0002620 | skin fibroblast | Skin/dermal fibroblast examples |
| CL:0000138 | chondrocyte | OA chondrocyte population |
| CL:0002063 | pulmonary alveolar type 2 cell | IPF epithelial population |
| CL:0000623 | natural killer cell | NK effector, or senescent NK population only if separately supported |
| CL:0000624 | CD4-positive, alpha-beta T cell | CD4 population; cytotoxic or senescent qualification needs its own support |
| CL:0000625 | CD8-positive, alpha-beta T cell | CD8 population; exhaustion is not implicit |
| CL:0000235 | macrophage | Phagocytic effector or a separately evidenced senescent macrophage population |
| GO:0090398 | cellular senescence | General process anchor |
| GO:0090399 | replicative senescence | Specifically replication-associated arrest |
| GO:0090400 | stress-induced premature senescence | Stress-induced route when supported |
| GO:0090402 | oncogene-induced cell senescence | Oncogenic route, not every cancer-associated senescence observation |
| GO:0090403 | oxidative stress-induced premature senescence | Oxidative route when established |
| GO:0006974 | DNA damage response | Possible upstream mechanism; not diagnostic of senescence |
| GO:0001816 | cytokine production | One component of a SASP; not equivalent to the whole SASP |
| GO:0019221 | cytokine-mediated signaling pathway | Recipient signaling, distinct from cytokine secretion |
| GO:0042267 | natural killer cell mediated cytotoxicity | Immune effector function |
| GO:0006911 | phagocytosis, engulfment | Engulfment mechanism, distinct from proliferative arrest |
| GO:0006915 | apoptotic process | Target-cell death, distinct from senescence |
| UBERON:0002097 | skin of body | Location used in the fixtures |
| NCIT:C107438 | Beta-Galactosidase | Protein identity; does not encode SA-beta-gal assay conditions |

All 21 returned non-obsolete records. The eight CL terms reached CL:0000000
through the queried `ancestors` relation; the eleven GO terms reached GO:0008150.
The anatomy term reached the schema's UBERON root. Labels, existence and scope
were checked separately; none of these checks proves a biological claim.

The explicit searches are retained in
[ontology-searches.json](senescent-cell-representation/ontology-searches.json).
Examples that can be rerun:

```bash
uv run runoak -i ols:cl search 'senescent'
uv run runoak -i ols:go search 'senescence'
```

OLS label/synonym searches for `senescent` and `senescence` in CL returned zero
hits. The analogous query for `senescence-associated secretory phenotype`
in GO returned zero hits. These are statements about the recorded queries and
loaded releases, not proof that no relevant class could exist under other wording.
CL does contain some state-qualified classes, so the recommendation is not based
on a claim that CL is universally restricted to immutable lineage identities.

Two cautions emerged from inspecting the actual records:

1. **GO's general definition still says irreversible cell-cycle arrest.** The
   review's conditional escape discussion creates a real conceptual tension.
   Keep the canonical label and record the caveat; do not rewrite the ontology
   definition locally. Senescence-like phenotypes or reversible cytostasis with
   no demonstrated stable arrest should not be forced into this binding. A
   separately modeled escape transition need not assert that the escaped cell
   remains in the original state.
2. **Replicative senescence is not in the queried `is_a` closure of GO:0090398.**
   GO:0090399 instead had GO:0022402 (cell cycle process) as a direct parent.
   Include it explicitly in a senescence retrieval set. Do not assume the
   schema's BP-root validation implies the expected finer senescence hierarchy.

GO:0001816 also carries a caution against direct gene-product annotation;
DisMech's mechanism annotation is a different use. Neither it nor the generic
inflammatory-response term should be presented as an exact SASP ontology match.
OBI assay descriptors exist in the schema, but OBI is absent from the configured
validator adapters. The fixtures therefore retain assay names without claiming
an OBI binding was verified.

## Identity, state, burden, mechanism and marker are different assertions

| Assertion | Example | What it does not establish |
|---|---|---|
| Cell identity | Skin fibroblast | Senescence, abundance, or source-study provenance |
| Cell state | A particular fibroblast population is senescent | Every fibroblast in that tissue is senescent |
| State-inducing mechanism | Oncogenic signaling or telomere dysfunction induces arrest | That the two triggers occurred in the same cells |
| State-associated program | A population produces a specified SASP | A universal set of secreted factors or a uniformly harmful effect |
| Immune interaction | HLA-E on the target inhibits an NKG2A-bearing effector | That the effector is senescent |
| Population burden | More senescent cells persist in tissue | An increased rate of senescence induction; impaired clearance can also increase burden |
| Assay observation | Increased SA-beta-gal activity, measured under stated conditions | Sufficient identification of senescence or a validated clinical surrogate |
| Disease consequence | Context-specific matrix damage or repair | Universal effect direction across organs, ages and disease stages |

Conceptually, burden changes with entry into the state, elimination, and possible
exit from the state. This is a bookkeeping distinction, not a fitted quantitative
model from the review. A clearance intervention can reduce burden without reducing
the rate of senescence induction. A senomorphic intervention can alter secretory
output without eliminating the cells. Neither change necessarily restores
proliferation.

For marker curation, retain at least the cell population, tissue/specimen, assay
and measured entity, direction relative to the stated comparator, observation
time, and evidence limits when the source provides them. Distinguish CDKN2A
transcript from p16INK4a protein and an isoform-specific assay; distinguish GLB1
protein abundance from beta-galactosidase activity at pH 6.0. Cytokines can be both
causal mediators and readouts, but those require two different assertions.
An absent measurement is not a negative result. Loss of a marker is not automatically
senescence reversal, and bulk-tissue expression is not automatically a count of
senescent cells.

The current schema has useful homes for much of this detail, but structured
sample/time/comparator metadata and multi-marker inference remain incomplete.
Do not replace those gaps with invented confidence scores. The decision register
already leaves composite measures and experimental measurement context open.

## Options and concrete YAML

| Option | Benefit | Cost / limitation | Disposition |
|---|---|---|---|
| A. Existing CL descriptor + GO mechanism + contextual prose and readouts | Works now; preserves ontology identity; uses established evidence and graph machinery | Cell-state attribution partly textual; independent lists do not pair cells to states | **Use now** |
| B. Treat “senescent cell” as a single precomposed cell class | Convenient one-term lookup if an appropriate upstream class exists | No matching CL result in the recorded search; a broad state class loses lineage/tissue unless combined; no license to insert NCIT or GO into a CL-only slot | Do not substitute for identity; consider upstream ontology work only for a demonstrated need |
| C. Optional `CellTypeDescriptor.cell_states` assertions | Machine-readable state on the correct participant, with its own evidence; additive | Requires curation rules, display/export support; does not provide cross-node population identity | Investigated alternative; BP reuse selected after design feedback |
| D. Reusable cell-population entities, state transitions and structured marker panels | Could express same-population lineage, interactions, sample-level panels and trajectories | New identifiers, reference resolution, assay semantics, migration and export design; substantial overlap with unsettled evidence/measurement work | Defer pending concrete datasets and queries |

Generic `qualifiers` are not a recommended fifth solution. They are deprecated
for cases that deserve dedicated slots, their generic terms are not checked by
the ordinary dynamic-enum validator, and a GO process attached through an
ambiguous predicate is not automatically a well-defined cell state.

### Option A: current schema

This is the identity/state core of the executable
[existing-schema.yaml](senescent-cell-representation/existing-schema.yaml):

```yaml
pathophysiology:
- name: Senescent skin fibroblast state
  biological_scale: CELLULAR
  cell_types:
  - preferred_term: senescent skin fibroblast
    term:
      id: CL:0002620
      label: skin fibroblast
    located_in:
      preferred_term: skin of body
      term:
        id: UBERON:0002097
        label: skin of body
  biological_processes:
  - preferred_term: cellular senescence
    term:
      id: GO:0090398
      label: cellular senescence
```

The full fixture includes source evidence, a distinct NK-effector node with
decreased GO:0042267, and an SA-beta-gal readout. Its bare-name downstream target
resolves. No `modifier: INCREASED` is added to the senescence process merely
because the cell has the state: a comparative induction or burden claim would
need additional evidence. The assay is explicitly a methodological illustration,
not a claimed measurement or validated diagnostic endpoint.

The second executable fixture,
[wound-context.yaml](senescent-cell-representation/wound-context.yaml), uses the
review's p. 3 PDGF-AA example. A senescent source fibroblast promotes differentiation
of a separate responding fibroblast population. Both share CL:0002620; only the
source carries the senescence process. It illustrates why shared CL identity
must not collapse state or role. Its evidence is `REVIEW_SYNTHESIS`/`OTHER`;
promotion into production should cite and assess the underlying experiment.
That experiment also has a 2026 Expression of Concern, now flagged in the
fixture and above; exact-quote validation does not resolve that evidence concern.

Both fixtures use `category: Module` solely to exercise the existing `Disease`
schema outside `kb/`. Neither is a proposed new production module, disease,
patient record or clinical guideline.

### Option C: investigated alternative, not selected

The proposed delta is
[extension-delta.yaml](senescent-cell-representation/extension-delta.yaml).
It adds optional `cell_states` only to `CellTypeDescriptor`; each assertion has
a required `state`, contextual `description`, and nonempty `evidence` list.
The pilot vocabulary contains `SENESCENT` only. No cell-state ontology CURIE,
GO-state equivalence, diagnostic score, or exhaustive state taxonomy is invented.

An instance would have the following shape (illustrative wound-context fragment):

```yaml
cell_types:
- preferred_term: skin fibroblast
  term:
    id: CL:0002620
    label: skin fibroblast
  cell_states:
  - state: SENESCENT
    description: Senescent source fibroblasts in the review's acute cutaneous wound example.
    evidence:
    - reference: PMID:42518598
      supports: SUPPORT
      quote_role: REVIEW_SYNTHESIS
      evidence_source: OTHER
      snippet: In acute cutaneous wounds, senescent fibroblasts secrete PDGF-AA
```

The general process annotation stays on the mechanism node. A future state tag
must not replace its causal explanation or markers. The validation script builds
a complete candidate from the current-schema fibroblast fixture, moves the
state-supporting evidence onto the particular cell assertion, and checks that
the production schema rejects the new slot while a temporary extended schema
accepts it. The production schema is never changed.

Population guidelines for any pilot:

1. Assign the state only when the source interprets that specified population as
   senescent and its basis has been inspected. Record discordant markers and
   inference limits. A single marker, an old donor, exhausted function, or a
   computational score alone is insufficient for automatic assignment.
2. Preserve CL identity and participant-specific location. On mixed-population
   nodes, attach the assertion only to the supported population. An effector's
   state is independent of its target's state.
3. Keep induction, duration, clearance and disease consequences on their relevant
   mechanisms or observations. Do not infer replicative senescence from age.
4. Leave the list absent when unassessed; absence is not a negative assertion.
   The list permits multiple independently supported states in a future vocabulary,
   but does not imply exclusivity, a developmental trajectory or co-occurrence
   of every state in every individual cell.
5. Start with hand-reviewed skin-fibroblast, IPF AT2/fibroblast, OA chondrocyte
   and immune-T-cell examples. Automated extraction can nominate records, but
   cannot safely backfill state assertions from keyword matches or GO co-occurrence.

Before adoption, test actual consumer queries, wire rendering and exports,
validate generated datamodels, and document the vocabulary's semantics. Keep
the addition optional and old content valid. The extend-schema skill's approval
requirement applies to merging a substantive schema change; it is not a reason
to stop this local exploration or to request approval for these sandbox tests.

## Follow-up: biological phases and developmental stages

Chris's follow-up favors BP reuse for senescence and normal states, with a future
qualifier distinguishing something driving a process from something happening
during it. There is a close GO precedent: the comments on cell-cycle phase terms
recommend temporal annotation extensions, including `happens_during` for a
process and `exists_during` for a cellular-component annotation, instead of
treating a phase as an ordinary direct gene-product annotation target.
See [GO cell cycle phase](https://amigo.geneontology.org/amigo/term/GO%3A0022403).
DisMech is not a gene-product annotation database, but this distinction between
causal/participatory and temporal relationships is useful here.

Live OLS lookup on 2026-09-20 confirmed non-obsolete **GO:0051320 S phase** and
**GO:0000084 mitotic S phase**, both in the GO BP ancestry. It also confirmed
**HsapDv:0000019 Carnegie stage 12**, **UBERON:0000105 life cycle stage**, and
**GO:0021507 posterior neuropore closure**. Queries, definitions, URLs and the
retrieved ancestry records are in
[stage-lookups.json](senescent-cell-representation/stage-lookups.json).
This supplements rather than replaces the earlier 21-term lookup.

Carnegie stages describe human embryonic developmental context using morphology;
they should not be reduced to a fixed number of gestational days. The HDBR
criteria associate caudal neuropore closing with stage 12 and a closed caudal
neuropore with stage 13. A failure during that normal developmental window and
the age at which an abnormality is first observed are different assertions.
The affected morphology may itself compromise stage assignment; record how the
specimen was staged rather than assigning its stage solely from the failed
structure. [HDBR staging criteria](https://hdbratlas.org/staging-criteria/carnegie-staging-orig.html).
The ontology project supplies HsapDv for humans and MmusDv for mice; cross-species
stage correspondence needs an explicit basis rather than equating stage numbers.
[Developmental-stage ontology sources](https://github.com/obophenotype/developmental-stage-ontologies).

### Current DisMech support

| Existing construct | What it can express | Gap for Carnegie-stage mechanism context |
|---|---|---|
| `Disease.stages` / `Stage` | Named disease stages, evidence, descriptions, nested pathophysiology and substages; used for cancer and clinical progression | Structurally a Carnegie-named record could fit, but this does not provide an ontology-bound temporal qualifier on a particular process and conflates disease staging with organism development. `Stage` has no ontology-term slot. |
| `onset: {onset_category: EMBRYONAL}` and related HPO categories | Broad age of clinical onset, with quantitative age fields and notes | Does not identify Carnegie stage or when an initiating mechanism acts. |
| `FunctionalEffect.affected_developmental_stage` | Free-text stage/window for temporally restricted regulatory effects | Narrow to variant functional effects; used for embryonic limb development in `ZRS-Related_Limb_Malformation`. Not a general pathophysiology slot. |
| `AgentLifeCycleStage` / `LifeCycleStageDescriptor` | Infectious-agent life-cycle stages, described as OPL-bound | Not a ready-made human developmental-context field. |
| `PhaseTerm` | An enum declaration described as a phase or stage | Currently an unbound declaration with no consuming descriptor/slot; it is not implemented phase support. |
| Descriptor `temporality` | Acute/chronic/recurrent-style qualifiers | Not an embryological staging system. |

For current curation, keep the stage and its evidence in the relevant mechanism's
description/notes. Use `affected_developmental_stage` only within its existing
regulatory-effect scope. Do not use clinical onset as a proxy for the causal
window, or insert an HsapDv identifier into a GO-only biological-process binding.

**HPO onset placement needs a schema-versus-usage distinction.** `Pathophysiology`
has no direct `onset` slot. However, `BiologicalProcessDescriptor`,
`CellTypeDescriptor`, and the other descriptor subclasses inherit `onset` from
`Descriptor`. Therefore `pathophysiology[].biological_processes[].onset` is
structurally permitted. Phenotypes use `phenotype_term.onset` and/or
`phenotype_contexts[].onset`, not a direct `Phenotype.onset` slot. A scan of
indented `onset:` keys in disorder/module YAML found **533 annotations in 244
files, all under `phenotypes`, none under `pathophysiology`**. The schema's
inherited capacity is broader than observed curation practice. The scan and
exact paths are recorded in [onset-usage.json](senescent-cell-representation/onset-usage.json).
These HPO categories encode onset; structural permission does not make them
equivalent to a process's developmental window or a Carnegie-stage qualifier.

### Small future extension to explore

The useful addition would be **typed temporal context**, such as a
`happens_during` qualifier on a biological-process descriptor or a mechanism.
Its range should admit the relevant GO biological phases and developmental-stage
ontology terms. Exact slot placement remains a design choice: descriptor-level
placement scopes one process; node-level placement scopes the whole mechanism.
The following is a proposed shape only, **not currently valid production YAML**:

```yaml
# Hypothetical developmental defect; illustrates the intended relation only.
biological_processes:
- preferred_term: posterior neuropore closure
  term:
    id: GO:0021507
    label: posterior neuropore closure
  modifier: ABNORMAL
  happens_during:
  - preferred_term: Carnegie stage 12
    term:
      id: HsapDv:0000019
      label: Carnegie stage 12
```

This pairs the affected process with its developmental window; it does not say
that Carnegie stage 12 causes the abnormality. For a failed process, this refers
to the window in which that process would normally occur; the record should say
whether the stage is observed in affected material or inferred from normal
development. Evidence for the defect and its timing must support both claims.
Stage ranges, uncertainty, and partial temporal overlap should be addressed before
assuming that every claim fits a single strict `happens_during` relationship.

Before implementing, define the relation's subject and scope, connect evidence
to timing, and configure the new ontology source. `HsapDv` is currently absent
from `conf/oak_config.yaml`; the queried HsapDv term reaches its own
`HsapDv:0000000` root, not a demonstrated UBERON-root closure. Therefore, the
existing parasite-stage dynamic enum cannot be assumed to validate it simply
because both ontologies describe life-cycle stages. No schema extension or new
adapter was installed in this follow-up.

## Cross-check of the shared findings report

The [shared FINDINGS.md](https://share.onorca.dev/a/DNdT1gKaYZP4) was read in full.
Much of it independently supports the existing-schema recommendation and repeats
the same marker, context and export cautions. The following additions are useful:

- **Cell-scoped process participation is a useful candidate.** The report
  considers `participates_in` on a cell descriptor. This directly addresses
  which participant is involved in which BP and fits the selected ontology-reuse
  direction. It would be a new slot, not existing syntax. Temporal context and
  causal influence still require their own relations; participation alone does
  not establish persistent state or regulation.
- **Concrete ontology counterexamples improve the rationale.** Rechecking OLS
  confirmed PATO:0001487 `senescent` is a broad aging/time quality, while
  CL:0011025 `exhausted T cell` and CL:0020031 `CD8-positive exhausted alpha-beta
  T cell` are real, non-obsolete classes. Thus there is neither an exact PATO
  shortcut nor a blanket rule that CL never includes state-qualified classes.
  Exhaustion still does not establish senescence. Lookup records are in
  [salvage-terms.json](senescent-cell-representation/salvage-terms.json).
- **The IPF measurement example catches a specific error.** Schafer et al.'s
  Results, first paragraph and Figure 1a, associate transcript expression assessed
  by microarray with severity. Immunohistochemistry separately localizes p16
  protein. This was independently rechecked against the existing fetched full-text
  cache for PMID:28230051. A more specific protein identifier still would not
  correctly type that transcript observation. [Primary study](https://www.nature.com/articles/ncomms14532).
- **Arts syndrome supplies a useful uncertainty case.** Its existing “Neural
  Stem Cell Senescence-Like State” node retains patient-derived culture context
  and does not bind GO cellular senescence. It is a useful test that BP reuse
  does not force a stronger categorical claim from marker-like observations.
  The repository entry was inspected; this is not a new appraisal of its primary
  study. [Existing entry](../../kb/disorders/Arts_syndrome.yaml).
- **An executable export check is worth retaining as a method.** The shared
  report describes a probe of CL identity/display names and lost context in KGX.
  Its linked `validation/export-probe.json`, `02-ipf-compatible.yaml`, and
  `VALIDATION.md` returned 404 when resolved against the shared artifact URL.
  Consequently their implementation and claimed validation were not imported or
  endorsed. The equivalent export limitations in this note were independently
  established by inspecting the local source.

The report's broader textual census and this note's name/GO-node census measure
different things; their counts should not be merged. Its separate `cell_states`
proposal remains an unselected alternative after the BP-reuse decision.
Checking its Demaria citation exposed the Expression of Concern described above,
which is absent from the shared report. That source-status correction has been
incorporated into our local wound fixture without altering the source quotation.

## Follow-up curation identified by the exploration

The highest-value initial work is **content refinement using existing slots**:

- Add or sharpen evidenced recognition, impaired clearance and target-side
  evasion nodes where a disease warrants them. The existing senescence module
  mentions immune clearance but has no dedicated clearance node.
- Revisit the generic module's unconditional arrest→SASP phrasing and its
  replicative-senescence binding on the generic arrest node. They can imply
  features or triggers that need not hold for every conformer.
- Make marker scope explicit. The current p16 readout extrapolates an IPF
  severity association into general module prose; the SA-beta-gal block partly
  relies on a consensus-purpose sentence. A result about one marker in one
  disease should not silently become a universal diagnostic/prognostic property.
- Preserve the complementary tumor-suppression module, and model senescence
  bypass separately from the positive barrier. A wound-repair example need not
  conform to the pathological accumulation/dysfunction branch.
- For IPF, preserve separate epithelial and fibroblast populations and the
  existing model limitations. For APDS, adjudicate senescence versus exhaustion
  rather than renaming one to the other.

The module refinements in the first three bullets are now applied as described
below. Disease-specific follow-ups remain unimplemented. A module's `conforms_to`
is not inheritance: disease-specific source evidence and cell/tissue context must
still be present. The inventory and scan counts above describe the repository
baseline before this curation.

## Applied local module curation

Chris authorized updating the existing
[`cellular_senescence` module](../../kb/modules/cellular_senescence.yaml) after
reviewing the exploration. It now has eight pathophysiology nodes, preserving
the names of all five original nodes and adding this context-specific branch:

**Senescence-associated arrest → HLA-E display by senescent skin fibroblasts →
reduced NK-cell cytotoxicity → impaired immune clearance → senescent-cell
accumulation.**

The HLA-E branch is an experimentally supported example, not a universal
requirement for disease conformers. The broader clearance node also represents
the review's immune-aging route to persistence. CL terms identify the target and
effector populations separately; GO biological processes capture senescence and
reduced cytotoxic/immune-effector activity. No `cell_states` field or temporal
qualifier was added.

| Captured result | Local representation | Evidence and scope |
|---|---|---|
| Arrest durability depends on cell type and trigger. | Qualified the arrest description; removed replicative senescence as a universal binding. | Review p. 2, “Senescent cells and their role in inflammaging.” GO:0090398 retains its canonical definition; the escape caveat does not redefine it. |
| SASP varies by context and includes more than cytokines; autocrine and paracrine signaling can reinforce or propagate senescence. | Expanded the SASP description and evidenced its edge to accumulation; separated CL fibroblast identity from GO senescence. | Review pp. 2–3, same section. The accumulation edge is marked indirect because the quoted signaling claim does not measure net population burden. |
| Senescent dermal fibroblasts can evade immune responses through HLA-E/NKG2A. | Added separate HLA-E target-cell and reduced NK-cell-cytotoxicity nodes, with an edge to impaired clearance. | Review p. 5 provides the lead; [Pereira et al., PMID:31160572](https://pubmed.ncbi.nlm.nih.gov/31160572/) provides primary evidence. Functional evidence is classified IN_VITRO; human skin observations do not establish organism-wide clearance efficacy. |
| Impaired immunosurveillance can increase persistence and burden. | Added a general impaired-clearance node and an evidenced edge to accumulation. Removed increased-process modifiers that conflated senescent-cell burden with entry into senescence. | Review abstract p. 1 and “Immunosenescence impairs immunosurveillance,” pp. 5–6; review synthesis is explicit. |
| Individual markers are insufficient to establish senescence. | Qualified p16 and SA-beta-gal readouts. The p16 severity association remains scoped to human IPF transcript measurements; the protein binding and unsupported general prognostic designation were removed. SA-beta-gal is supportive of a senescence-associated state, with pH/assay context and no stand-alone diagnostic designation or universal burden claim. | Review p. 2 and existing [Schafer et al., PMID:28230051](https://pubmed.ncbi.nlm.nih.gov/28230051/), Results/Figure 1. The latter separates transcript profiling from protein staining. |
| Immune-rejuvenation benefits may reflect mechanisms other than senescent-cell clearance. | Added an open knowledge-gap discussion attached to the clearance and accumulation nodes. | Review p. 6, Conclusion. No new treatment recommendation is inferred. |

The newly used [GO:0002252, immune effector process](https://www.ebi.ac.uk/ols4/ontologies/go/terms?obo_id=GO%3A0002252)
was looked up directly in OLS and passed the repository's term validator; its
label, definition, non-obsolete status and retrieval URL are recorded in
[curation-term-lookups.json](senescent-cell-representation/curation-term-lookups.json).
It is a broad binding for the immune-effector component of clearance, not a term
asserting that every immune response is globally reduced. The other CL, GO and
UBERON bindings were verified during the initial exploration and again by the
module term validator. Validation generated one GO term-cache row and one
dynamic-enum membership row; neither was hand-edited.

The Demaria wound-healing result remains in the research discussion with its
expression-of-concern caveat, not newly promoted into this module. Other evasion
routes (CD47/SIRP-alpha, ligand shedding, PD-L1/PD-1, GD3, FasL and suppressive
secretions) remain explicitly identified for source-specific assessment. The
existing treatment and experimental, animal and computational model sections
were preserved. This captures the paper's central distinctions without implying
that every cited primary study has been independently adjudicated.

Module schema and ontology validation passed, and all **46/46 evidence snippets**
verified against cached sources (35/35 in the pre-edit baseline). Duplicate-key,
entity-reference, causal-target and knowledge-gap checks passed. The built graph
has 28 edges and no orphan targets. The repository's citation-title checkers
found no title-only snippets or reference-title mismatches in the changed module;
the history and generated term-cache integrity checks also passed. The detailed
results and content hashes are
recorded in [curation-validation.json](senescent-cell-representation/curation-validation.json).
An append-only [curation history record](../../history/modules/cellular_senescence/2026-09-21T011251Z-codex-01c6b3.yaml)
records the authorized change and its validation.
Before PR preparation, the branch was refreshed to `f3df177789af41976971b15edbb91d65f0c67cc1`.
The module content hash is unchanged. Schema, ontology, reference, fixture and
module-content checks were repeated against that base, and the recorded ontology
searches returned the same counts. See [PR validation](senescent-cell-representation/pr-validation.json).
The earlier KB inventory remains a snapshot of the original investigation base.

## Validation and reproducibility

The companion [validation script](senescent-cell-representation/validate_design.py)
checks structural expressibility, backward compatibility of the two fixtures,
and graph target resolution. It deliberately does not equate successful validation
with biological correctness. Recorded commands and outputs are in
[validation-results.json](senescent-cell-representation/validation-results.json).

- Both complete fixtures validate against the production schema and the
  temporary extended schema. Their three graph edges have no orphan targets.
- A complete candidate with `cell_states` passes the temporary schema and is
  rejected by the production schema for the new slot, as expected.
- The temporary schema rejects an unsupported `EXHAUSTED` value and an empty
  state-evidence list. The script checks the rejection reasons, not just exit codes.
- Both fixtures pass ontology-term validation. The reference validator verifies
  all **four of four** snippets against fetched references.
- These are fixture-level checks. No production datamodel was regenerated and
  no claim is made that existing renderers, exports or reference traversal already
  support the proposed nested state assertion.

From the repository root, the main checks can be rerun with:

```bash
just fetch-reference PMID:42518598 PMID:31160572 PMID:37001502 PMID:39121846
uv run python docs/reports/senescent-cell-representation/validate_design.py
uv run python docs/reports/senescent-cell-representation/scan_kb.py
just validate-terms docs/reports/senescent-cell-representation/existing-schema.yaml
just validate-terms docs/reports/senescent-cell-representation/wound-context.yaml
scripts/run_reference_validator.sh validate data \
  docs/reports/senescent-cell-representation/existing-schema.yaml \
  docs/reports/senescent-cell-representation/wound-context.yaml \
  --schema src/dismech/schema/dismech.yaml --target-class Disease \
  --config conf/reference_validator_config.yaml --no-full-text
```

References were fetched only with `just fetch-reference`, never written or
edited manually. The generated records are PMID:42518598, PMID:31160572,
PMID:37001502 and PMID:39121846. Hasegawa's publisher PDF fetch returned HTTP 403;
its abstract was available and sufficient for the specific HLA-II correction.
No claim is made to have read that entire primary paper. The review's full
bibliography was read, but its dozens of underlying studies were not all
independently verified.

The supplied PDF remains unchanged. The uploaded PDF and its local text
extraction are excluded from the commit. Chris explicitly authorized including
the four standard, tool-generated reference caches in the PR, including their
public full-article content where available. The quoted evidence can therefore
be checked against the committed caches; `fetch-reference` above regenerates
these records when needed.
The initial exploration was entirely local, with no commit, push, PR, publication
or external message. In a subsequent, explicitly authorized follow-up, Chris
requested [issue #12355](https://github.com/monarch-initiative/dismech/issues/12355)
on incorporating PubPeer and publication-status updates, using the Demaria case.
That issue links the existing source-status discussion in #9840 and the published
critique and response surfaced by the PubPeer thread. The later PR request
authorizes publishing the bounded module curation and this supporting record.
The frozen dataset-accession blob was not accessed.

## Remaining decisions and uncertainty

- Which queries require explicit participant/process relations or temporal
  qualifiers beyond the selected BP reuse? Readable mechanism curation already
  works; extra structure should answer a concrete query.
- Should a future population representation distinguish state of an individual
  cell from enrichment of a heterogeneous population? The proposed small state
  assertion deliberately provides no percentage or all-cells quantifier.
- How should escape-capable senescence map to GO's irreversible-arrest
  definition? An upstream ontology discussion may be appropriate, but no term
  request was filed and no local semantic override was made.
- Can marker evidence establish colocalization, durable arrest and cell identity
  in the relevant disease tissue? Many reviews and bulk measurements cannot.
- A lineage that is normally postmitotic presents a special problem: lack of
  proliferation alone cannot establish new senescence-associated arrest.
  Such contexts need source-specific criteria rather than reusing a fibroblast
  classifier.
- The mini review supports investigating immunosurveillance, but it does not
  settle which evasion mechanisms dominate particular human diseases, nor
  whether improved immune function acts through senescent-cell clearance.

The selected direction is **BP reuse with carefully scoped relations**, keeping
the separate cell-state vocabulary as an unselected alternative. A future
temporal qualifier could cover both GO cell-cycle phases and organism-level
developmental stages. A broad new senescent-cell entity model, a universal
marker panel, and a general experimental-evidence redesign are not prerequisites
for representing the paper's central biology faithfully.
