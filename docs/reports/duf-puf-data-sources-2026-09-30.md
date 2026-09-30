# Data sources for domains and proteins of unknown function

**Date:** 2026-09-30
**Question:** Which public data sources should DUFMech use to find domains of
unknown function and proteins of unknown function, then attach structural,
genomic, and functional clues to them?

## Verdict

Use **InterPro/Pfam as the DUF family catalog**, keyed first by Pfam accession.
Pfam is queried through the InterPro API now, and the endpoint already exposes
the pieces needed for DUF discovery: Pfam entry metadata, integrated InterPro
entries, member signatures from CDD, PANTHER, SFLD, CATH-Gene3D, SUPERFAMILY,
HAMAP, PIRSF, PRINTS, PROSITE, SMART, and NCBIFAM, protein members, matched
structures, domain architectures, taxonomic counters, and AlphaFold/BFVD model
counters. See the [InterPro API docs](https://interpro-documentation.readthedocs.io/en/latest/api.html)
and [Pfam API notes](https://pfam-docs.readthedocs.io/en/latest/api.html).

There is no equivalent canonical catalog for **proteins of unknown function**
(PUFs). Build that set as a release-specific predicate over complete or
metagenomic protein universes: sequences from UniProtKB Reference Proteomes,
representative MGYP clusters from MGnify Proteins, and, where permanence
matters, UniParc sequence identities. Text such as "uncharacterized protein" is
a useful weak flag, but it must be crossed with absence of curated function,
GO/Rhea/EC evidence, high-specificity conserved-domain hits, and solved or
confidently transferable structures.

The first-pass ingestion should be:

1. Search Pfam entries in InterPro for DUF-like families.
2. Normalize to `PFxxxxx`, attach any integrated `IPRxxxxxx` parent and Pfam
   clan/set, and keep InterPro/Pfam descriptions as metadata, not as facts.
3. Pull UniProtKB members and collapse redundancy with UniRef clusters.
4. Pull MGnify cluster representatives for the same Pfam accessions to recover
   environmental proteins and biome context.
5. Join PDB, PDBe-KB, 3D-Beacons, AlphaFold DB, CATH-Gene3D, CDD, STRING,
   eggNOG, EFI-GNT, JGI IMG, Rhea, and QuickGO as evidence layers.
6. Score the family or protein as "still unknown", "partially characterized",
   or "known but historically named DUF" instead of assuming that a DUF short
   name still means no function is known.

That last caveat is important. A live InterPro query on this date:

```bash
curl 'https://www.ebi.ac.uk/interpro/api/entry/pfam/?page_size=5&search=DUF&extra_fields=entry_id,short_name,description,counters'
```

returned 6,558 Pfam records. This is intentionally a broad seed set, not a
truth set: one of the early hits is `PF01784`, `DUF34`, whose current
description already points to a conserved metal-binding protein family.

## Source classes

| Source | Access | DUF/PUF contribution | Join keys | Caveat |
|---|---|---|---|---|
| InterPro / Pfam | InterPro REST API; Pfam-specific examples in the Pfam docs | Primary DUF family registry, entry descriptions, InterPro integration, protein and structure counters | `PFxxxxx`, `IPRxxxxxx`, UniProt accession, PDB ID | DUF names are historical and string search is over-inclusive |
| UniProtKB, Proteomes, UniRef | UniProt REST, SPARQL, FTP reference-proteome downloads | Protein universe for organisms with sequenced genomes; function names, catalytic activity, GO, EC, Rhea, InterPro features, UniRef50/90/100 clustering | UniProt accession, proteome ID, taxon, UniRef cluster, `UPI` via UniParc | TrEMBL entries are not all unknown, and low annotation score is not itself evidence of unknown function |
| UniParc | UniProt REST and RDF | Permanent sequence identity for proteins removed from UniProtKB or found in non-reference/excluded proteomes | `UPI`, checksum, cross-references | Sequence archive only; most functional context must be rejoined from elsewhere |
| MGnify Proteins | [MGnify Proteins API](https://docs.mgnify.org/src/docs/mgnify-proteins-api.html), Transfer Services bulk files, remote Parquet/DuckDB | Environmental cluster representatives, biome occurrence, Pfam hits, assembly and contig provenance | `MGYP`, Pfam accession, biome ID, study/assembly/contig accession | The JSON API is for individual lookups and small result sets; detailed records exist only for cluster representatives |
| AlphaFold DB | [prediction API](https://alphafold.ebi.ac.uk/api-docs), downloads, similar-structure and AFDB cluster data | Predicted monomer models, pLDDT/PAE confidence, structure-neighbor clues for DUF members | UniProt accession, AlphaFold model URL, PDB/mmCIF/CIF URLs | Low-confidence or disordered regions can create false fold analogies |
| PDB, RCSB, PDBe-KB, 3D-Beacons | [RCSB Search API](https://search.rcsb.org/), [RCSB Data API](https://data.rcsb.org/), [PDBe-KB services](https://www.ebi.ac.uk/pdbe/pdbe-kb/services), [3D-Beacons Hub API](https://www.ebi.ac.uk/pdbe/pdbe-kb/3dbeacons/api/) | Experimental structures, ligand and assembly metadata, residue-level structural/functional annotations, model inventory for a UniProt accession | PDB ID, polymer entity, UniProt accession, residue number | A solved structure often covers one domain boundary, not the whole PUF |
| CATH-Gene3D | InterPro member signatures plus [CATH-Gene3D downloads](https://cathdb.info/download) | Domain superfamily and FunFam placement, structural homology, fold-level analogies | Gene3D/CATH IDs, UniProt accession, PDB domain | Homologous superfamily membership can be much broader than one biochemical function |
| NCBI CDD and NCBIFAM | [CDD/CD-Search](https://www.ncbi.nlm.nih.gov/Structure/cdd/cdd_help.shtml), downloadable RPS-BLAST databases, InterPro member signatures | Independent PSSM/HMM assignments, NCBI-curated families, local annotation of proteins with no existing InterPro hit | CDD accession, NCBIFAM accession, query protein | Specific hits are high-confidence; superfamily-level hits should be treated as remote context |
| STRING and eggNOG | [STRING APIs/downloads](https://string-db.org/cgi/download) | Functional association networks, orthology, hierarchical clusters, COG mappings, sequence and network embeddings | STRING protein ID, taxon, eggNOG/COG | STRING edges include indirect functional associations as well as direct physical interactions |
| EFI-GNT and JGI IMG | [EFI-GNT](https://efi.igb.uiuc.edu/efi-gnt/), [IMG functions](https://img.jgi.doe.gov/data-analysis.html), [IMG data sources](https://img.jgi.doe.gov/datasource.html) | Genome-neighborhood evidence, Pfam/InterPro neighborhood profiles, KEGG/IMG/COG context for microbes | UniProt/UniRef/NCBI IDs, Pfam, InterPro, contig/genome | Powerful for hypothesis generation, but less convenient as a bulk API-backed source |
| Rhea, GO, QuickGO | [Rhea REST](https://www.rhea-db.org/help/rest-api), [QuickGO REST](https://www.ebi.ac.uk/QuickGO/api/) | Reaction, catalytic-activity, molecular-function, and GOA evidence that can demote a candidate from "unknown" to "known" | `RHEA:nnnnn`, `GO:nnnnnnn`, EC, UniProt accession, ECO evidence | Mostly validation and known-function filters, not a DUF discovery source |

## InterPro and Pfam

The InterPro `entry/pfam` endpoint is the right starting point for DUF family
seeds. It supports `search=`, `type=`, `group_by=type`, `page_size` up to 200,
sorting, HMM annotation filters, and an `extra_fields` list that can add
counters, the public entry name, hierarchy, literature, cross-references,
descriptions, and overlapping entries. `tigrfams` was replaced by `ncbifam` in
InterPro 94.0, so new calls should use `ncbifam` when member signatures are
needed.

Useful calls:

```text
https://www.ebi.ac.uk/interpro/api/entry/pfam/?search=DUF&extra_fields=entry_id,short_name,description,counters
https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01519?extra_fields=entry_id,short_name,description,counters
https://www.ebi.ac.uk/interpro/api/protein/entry/pfam/PF01519/
```

Recommended local fields for a DUF seed:

| Field | Why it matters |
|---|---|
| Pfam accession | Stable family key and MGnify search key |
| Pfam short name and description | The best available human label, with the historical-DUF caveat |
| Integrated InterPro accession | Higher-level family or domain roll-up |
| Pfam clan / InterPro set | De-duplication across related HMMs |
| Source databases that also hit | CDD, Gene3D, SUPERFAMILY, PANTHER, SMART, and PROSITE can imply fold or function |
| Protein, structure, AlphaFold, and taxonomy counters | Cheap triage before pulling every member |
| Literature and cross-references | Evidence anchors when a DUF has partial experimental resolution |

Keep the seed query broad, then make the evidence model narrower downstream.
Some families lose the original mystery while retaining the `DUF` mnemonic; the
pipeline needs to preserve that as a finding instead of discarding the family or
silently treating it as solved.

## UniProt, UniRef, and UniParc

The UniProt REST API and SPARQL endpoint are the main source for proteins from
complete genomes: product names, reviewed/unreviewed status, proteome
membership, taxonomy, sequence, cross-references, catalytic-activity comments,
GO terms, EC numbers, Rhea reactions, and InterPro/Pfam feature annotations all
meet at the UniProt accession.

For PUF discovery, start from Reference Proteomes rather than every historical
UniProtKB/TrEMBL sequence. The UniProt proteome help page explicitly recommends
FTP downloads of precomputed Reference Proteome sets over very large HTTP
streams. UniRef90 or UniRef50 should be added immediately to avoid counting the
same uncharacterized family thousands of times.

The unknown-function predicate should stay explicit and auditable:

| Signal | Suggested interpretation |
|---|---|
| Product names like "uncharacterized protein", "hypothetical protein", or "protein of unknown function" | Weak positive seed |
| DUF Pfam or InterPro hit | Strong family seed, weak proof of ignorance |
| No experimentally supported GO molecular function | Weak positive, because absence of evidence is common |
| No Rhea, EC, catalytic-activity comment, or curated Swiss-Prot function | Stronger positive |
| Specific CDD/NCBIFAM, Rhea/EC, or experimental GOA hit | Demote to partially characterized or known |
| Reference Proteome membership and full-length ORF | Promote over fragments and singletons |
| UniRef cluster size and taxonomic span | Prioritize families with breadth |

Use UniParc only when the sequence itself is the stable object. That becomes
useful for proteins outside Reference Proteomes, for sequences removed from
UniProtKB during the 2026 TrEMBL reorganization, or for cross-release
deduplication.

Primary access points:

```text
https://rest.uniprot.org/
https://sparql.uniprot.org/sparql
https://ftp.uniprot.org/pub/databases/uniprot/current_release/
```

## MGnify Proteins

MGnify Proteins is the obvious environmental complement to UniProtKB. The API is
read-only, requires no authentication, and exposes only two endpoints:
`GET /protein/{mgyp}` and `GET /protein/search`. Search accepts exactly one of
`biome_id`, `biome_lineage`, or `pfam_accession`; the Pfam parameter accepts
either `PF00005` or `5`.

Detail responses are compact but unusually useful for DUF work:

| Field | DUFMech use |
|---|---|
| `mgyp` | Stable representative protein accession |
| `sequence` and `full_length` | FASTA output and fragment filtering |
| `cluster_size` | Non-redundant abundance proxy |
| `biomes` | Environmental distribution and hypothesis generation |
| `pfam_annotations` | DUF family matches with coordinates and scores |
| `study_assembly_contigs` | Assembly/contig provenance for neighborhood recovery |

The search endpoint is capped at one page and a `limit` of 1000. That is fine
for spot checks such as:

```bash
curl 'https://www.ebi.ac.uk/metagenomics/proteins/api/v1/protein/search?pfam_accession=PF00005&limit=5'
```

but not for enumerating all environmental representatives of every DUF. Do the
catalog build from MGnify bulk downloads or the Parquet/DuckDB path documented
by MGnify, then use the JSON API for drill-down and verification.

## Structure evidence

Structure can rescue DUF and PUF families when sequence annotation stalls.
AlphaFold DB provides predicted model metadata by UniProt accession, including
the current model version, model creation date, pLDDT fractions, and direct PDB,
mmCIF, PAE, and pLDDT file URLs:

```text
https://alphafold.ebi.ac.uk/api/prediction/P01308
```

Three uses are worth separating:

| Question | Source |
|---|---|
| Does this UniProt accession have a model and which residues are confident? | AlphaFold DB prediction API |
| Does any solved PDB domain match this DUF? | RCSB sequence/structure search and PDBe-KB |
| Does this fold place in a broader family with functional residues? | CATH-Gene3D and InterPro Gene3D/SUPERFAMILY member signatures |

Predicted structure is a clue layer. Low average pLDDT, missing confident
active-site residues, and domain-swapped or multimeric biology can all make a
monomeric structure neighbor misleading. Store the aligned residue interval and
confidence metrics with any structure-derived hypothesis.

## Sequence, neighborhood, and network inference

CDD and Batch CD-Search give an independent RPS-BLAST view over curated
position-specific scoring matrices. The scripted Batch API is useful for
moderate validation jobs, and the downloadable databases plus standalone
RPS-BLAST are the better path for a local all-vs-CDD annotation pass. Treat
specific CDD hits as much stronger than broad superfamily hits.

STRING and eggNOG are useful after each candidate protein has a taxon-aware
identifier. STRING offers bulk scored networks, physical-only networks,
orthology, hierarchical eggNOG groups, COG mappings, hierarchical STRING
clusters, sequence embeddings, and network embeddings. Those files are
excellent feature tables for prioritization, but their association scores
should become hypotheses, not direct physical-interaction claims.

EFI-GNT is the richest off-the-shelf tool for the enzymology pattern: cluster a
family by sequence, then inspect whether neighboring Pfam families recur in the
same operon-sized windows. It currently exposes both a current UniProt database
and a legacy UniProt 2025_03 / InterPro 106 option, which is helpful while
curating across the UniProtKB Reference Proteome transition. The form-driven
interface makes it better for expert review or ad hoc hypothesis generation
than for the first bulk ingestion.

JGI IMG adds a microbe-centered warehouse that already connects genes to Pfam,
InterPro, COG, GO, KEGG, Enzyme, MetaCyc, IMG Terms, and gene neighborhoods.
That is valuable for checking prokaryotic PUF neighborhoods, especially when IMG
has JGI-specific genome context that did not flow cleanly into UniProt.

## Reaction and GO validation

Rhea and QuickGO should be used mostly as negative filters for "unknown" status
and as controlled vocabularies once a function is inferred.

Rhea is the target reaction vocabulary for enzyme and transporter function. Its
REST API can return individual reactions in RXN/RD or query results in
customizable TSV; UniProtKB links catalytic-activity comments to Rhea, so a
`cc_catalytic_activity:"rhea:*"` query is a direct way to find accessions whose
biochemistry is no longer unknown.

QuickGO exposes both ontology terms and GOA protein annotations with ECO
evidence. Separate experimentally supported molecular-function annotations from
IEA annotations: an electronic GO transfer is a useful candidate demotion, but
it should not outrank a DUF-specific biochemical paper or a CDD specific hit.

## First local schema sketch

A small, release-aware DUF seed record should be enough to start:

```yaml
family_id: PF01519
source: pfam
source_release_date: 2026-09-30
name: DUF16
interpro_id: null
unknown_status: UNKNOWN_CANDIDATE
candidate_reason:
  - name_matches_duf
protein_counters:
  uniprot: 26
structure_counters:
  pdb: 1
  alphafold: 26
source_urls:
  - https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01519
```

The status should be allowed to change after evidence aggregation:

| Status | Meaning |
|---|---|
| `UNKNOWN_CANDIDATE` | Name, family metadata, or product labels suggest an unknown function and no stronger evidence has been attached |
| `PARTIALLY_CHARACTERIZED` | Some structure, reaction, binding, fold, localization, or pathway evidence exists, but the molecular role is incomplete |
| `KNOWN_HISTORICAL_DUF` | The family still has a DUF-style name but its function is now known |
| `FALSE_POSITIVE_TEXT_HIT` | `search=DUF` matched text that is not a domain of unknown function |

For PUFs, keep the same status on the protein-family assignment rather than on
the UniProt or MGYP accession alone. A multidomain protein can contain one DUF
and one characterized catalytic domain; the protein is not globally unknown
even if one region remains unresolved.

## Sources to defer

Several familiar sources are better treated as later validation or display
layers:

| Source | Defer because |
|---|---|
| KEGG Orthology | High-value pathway labels, but API/licensing constraints make it less attractive as the first open ingestion source |
| MetaCyc / EcoCyc | Excellent curated reactions and pathways; use once candidate enzymes emerge |
| NCBI RefSeq/Protein | Redundant with UniProt for the first pass; pull later for RefSeq-specific product names and assemblies |
| HHpred, Phyre2, SWISS-MODEL, ModelArchive | Excellent expert tools, but better run on prioritized families than on every DUF seed |
| Literature text mining | Best used after structured databases shrink the search space |

## Minimum viable pipeline

1. Fetch `entry/pfam?search=DUF` from InterPro with counters and descriptions.
2. Drop false-positive text hits, normalize Pfam IDs, and attach InterPro
   integrated entries and clans.
3. For each Pfam, fetch UniProtKB members from InterPro and write a UniRef90
   non-redundant member table.
4. For each Pfam, fetch MGnify MGYP representatives from the bulk Proteins
   release or Parquet endpoint and keep `cluster_size`, `full_length`, and
   biome counts.
5. Join known-function evidence from UniProt catalytic activity, EC, Rhea, GOA,
   CDD specific hits, and Gene3D/SUPERFAMILY.
6. Join structure coverage from AlphaFold DB and PDB/PDBe-KB.
7. Emit a ranked table:
   `pfam_id`, `interpro_id`, `name`, `unknown_status`, `uniref90_count`,
   `mgyp_cluster_count`, `biome_count`, `pdb_count`, `alphafold_count`,
   `strongest_known_function_signal`, `top_function_hypothesis`.

That pipeline yields a tractable first DUFMech worklist: families still labeled
as DUF, present in reference proteomes or large MGnify clusters, with enough
structure or neighborhood context to support an evidence-backed functional
hypothesis.
