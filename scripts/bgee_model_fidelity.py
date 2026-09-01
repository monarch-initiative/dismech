#!/usr/bin/env python3
"""Cross-species expression check on curated animal-model fidelity claims (Bgee).

PROTOTYPE. This is a *curation aid*, not an evidence source. Nothing it emits may
be written into a KB entry as an ``EvidenceItem``: Bgee curates healthy wild-type
expression only, so a Bgee call describes the normal baseline a mechanism departs
from, never the mechanism itself. See ``docs/bgee-integration-proposal.md``.

What it checks
--------------
A dismech ``animal_models[].modeled_mechanisms[]`` link asserts that a model in
some species is informative for a named pathophysiology node, with a ``fidelity``
grade and free-text ``limitations``. When that node carries UBERON/CL anatomy and
the disease carries HGNC genes, one necessary (never sufficient) condition is
checkable against an expression atlas:

    is the model species' ortholog of the disease gene actually expressed in the
    anatomy where the human mechanism operates?

If the ortholog is absent there -- or there is no ortholog at all -- the model
cannot recapitulate that node by that gene's action, whatever the curated grade
says. That is a real translational caveat with data behind it, and it is exactly
what ``FAILS_TO_RECAPITULATE`` / ``PARTIALLY_RECAPITULATES`` and the
``HUMAN_MODEL_MISMATCH`` discussion kind exist to record.

Pipeline
--------
1. ``hgnc:NNNN``            -> Ensembl human gene   (HGNC REST, rest.genenames.org)
2. ENSG + model species     -> ortholog             (Ensembl Compara REST)
3. [human, ortholog] pair   -> homologous anatomy   (Bgee expression_comparison)
4. intersect with the target node's own UBERON/CL terms -> verdict

Step 3 is why this uses Bgee rather than a generic atlas: Bgee already computes
cross-species anatomical homology and returns present/absent/no-data per gene per
homologous condition, so no anatomy mapping has to be invented here.

Verdicts
--------
``ORTHOLOG_NOT_1TO1``  paralog expansion/loss; the model gene is not a clean substitute
``DIVERGENT_ABSENT``   human present, model ortholog *absent* in the homologous anatomy
``ORTHOLOG_LOOKUP_EMPTY``  Ensembl returned no ortholog -- NOT a finding, see below
``CONSERVED``          both expressed there -- the necessary condition holds
``MODEL_NO_DATA``      Bgee has no call for the ortholog there
``HUMAN_NO_DATA``      Bgee has no call for the human gene there
``ANATOMY_UNMATCHED_CL``      node is bound only to cell types Bgee has no condition for
``ANATOMY_UNMATCHED_TISSUE``  node's UBERON tissues have no multi-species condition

Only ``ORTHOLOG_NOT_1TO1`` and ``DIVERGENT_ABSENT`` are findings. ``CONSERVED`` is
not a validation of the fidelity grade -- shared expression is a precondition, not
evidence that the model reproduces the mechanism.

``ORTHOLOG_LOOKUP_EMPTY`` is deliberately NOT a finding
------------------------------------------------------
An empty ortholog list from Ensembl REST cannot be trusted as "this species has no
ortholog". ``homology/id/human/ENSG00000171862`` (PTEN) returns ``homologies: []``
against mouse at HTTP 200, and so does the reverse lookup from mouse
``ENSMUSG00000013663`` -- yet mouse *Pten* plainly exists and PTEN/Pten is among
the best-established orthologies there is. VHL behaves the same way. Whatever the
cause, the endpoint's silence is not evidence of absence, so this verdict is a
prompt to verify by hand, never a fidelity caveat to act on.

This is why the proposal asks the Bgee team whether ``expression_comparison`` does
its own orthology grouping (question 3): a single authoritative orthology source
inside Bgee would be better than this one.

Cell-type coverage is the binding constraint
--------------------------------------------
Bgee's multi-species comparison conditions are overwhelmingly UBERON tissues: in
our sampling only ~4% of conditions carried a CL term at all. dismech nodes are
predominantly CL-bound, so a strict cell-type match yields ``ANATOMY_UNMATCHED_CL``
for most links. ``--tissue-fallback`` therefore re-tries an unmatched CL node
against that node's *own* UBERON ``locations``, when it has any.

That fallback is a genuine loss of resolution and is reported as such: matched
rows are marked ``granularity=TISSUE`` rather than ``CELL_TYPE``. It is sound for
*this* check because the comparison is human-vs-model at whatever granularity Bgee
holds -- it never asserts the gene is expressed in the cell type, which would
invert Bgee's present-call propagation. Do not reuse the fallback for any check
that makes a claim about the cell type itself.

The governing asymmetry: Bgee propagates *present* calls to ancestor structures and
*absent* calls to direct descendants. So a present call at a coarse tissue must never
be read down onto a specific cell type.

Usage
-----
    uv run python scripts/bgee_model_fidelity.py --limit 20
    uv run python scripts/bgee_model_fidelity.py --file kb/disorders/Duchenne_Muscular_Dystrophy.yaml
    uv run python scripts/bgee_model_fidelity.py --all --tsv /tmp/bgee_fidelity.tsv
    uv run python scripts/bgee_model_fidelity.py --all --findings-only --tissue-fallback

Network: rest.genenames.org, rest.ensembl.org, www.bgee.org. Cached and resumable
via --cache (default tmp/bgee_cache.json); re-runs are offline for cached lookups.
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter

from dismech.yaml_io import safe_load

UA = (
    "Mozilla/5.0 (compatible; dismech-bgee-audit/0.1; "
    "+https://github.com/monarch-initiative/dismech)"
)

# dismech free-text species -> (Ensembl Compara species name, Bgee/NCBI taxon id).
# Bgee covers 52 species; every animal model species used in kb/ today is present.
SPECIES = {
    "mouse": ("mus_musculus", 10090),
    "mus musculus": ("mus_musculus", 10090),
    "mouse (mus musculus)": ("mus_musculus", 10090),
    "zebrafish": ("danio_rerio", 7955),
    "danio rerio": ("danio_rerio", 7955),
    "zebrafish (danio rerio)": ("danio_rerio", 7955),
    "rat": ("rattus_norvegicus", 10116),
    "rattus norvegicus": ("rattus_norvegicus", 10116),
    "dog": ("canis_lupus_familiaris", 9615),
    "canine": ("canis_lupus_familiaris", 9615),
    "cat": ("felis_catus", 9685),
    "pig": ("sus_scrofa", 9823),
    "cattle": ("bos_taurus", 9913),
    "cow": ("bos_taurus", 9913),
    "sheep": ("ovis_aries", 9940),
    "rabbit": ("oryctolagus_cuniculus", 9986),
    "guinea pig": ("cavia_porcellus", 10141),
    "chicken": ("gallus_gallus", 9031),
    "drosophila melanogaster": ("drosophila_melanogaster", 7227),
    "fruit fly": ("drosophila_melanogaster", 7227),
    "caenorhabditis elegans": ("caenorhabditis_elegans", 6239),
    "c. elegans": ("caenorhabditis_elegans", 6239),
    # Xenopus laevis is in Bgee (taxon 8355) but NOT in the Ensembl vertebrates
    # division, so Compara cannot supply an ortholog and these links are skipped
    # as SPECIES_UNMAPPED rather than silently mis-mapped to X. tropicalis.
    "xenopus tropicalis": ("xenopus_tropicalis", 8364),
    "macaque": ("macaca_mulatta", 9544),
    "rhesus macaque": ("macaca_mulatta", 9544),
    "naked mole-rat": ("heterocephalus_glaber_female", 10181),
    "naked mole rat": ("heterocephalus_glaber_female", 10181),
    "turquoise killifish (nothobranchius furzeri)": ("nothobranchius_furzeri", 105023),
    "nothobranchius furzeri": ("nothobranchius_furzeri", 105023),
    "opossum": ("monodelphis_domestica", 13616),
    "platypus": ("ornithorhynchus_anatinus", 9258),
}

FINDING_VERDICTS = {"ORTHOLOG_NOT_1TO1", "DIVERGENT_ABSENT"}


# --------------------------------------------------------------------------- io


class Cache:
    """Tiny JSON-backed memo so re-runs are offline and the APIs stay unhammered."""

    def __init__(self, path: str):
        self.path = path
        self.data: dict[str, object] = {}
        if path and os.path.exists(path):
            try:
                self.data = json.load(open(path))
            except Exception:
                self.data = {}
        self._dirty = 0

    def get(self, key):
        return self.data.get(key)

    def put(self, key, value):
        self.data[key] = value
        self._dirty += 1
        if self._dirty >= 25:
            self.flush()

    def flush(self):
        if not self.path:
            return
        os.makedirs(os.path.dirname(self.path) or ".", exist_ok=True)
        tmp = self.path + ".tmp"
        json.dump(self.data, open(tmp, "w"))
        os.replace(tmp, self.path)
        self._dirty = 0


def fetch_json(url: str, accept: str = "application/json", retries: int = 3):
    """GET one JSON document. Raises on exhausted retries -- never returns a fake empty."""
    last = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": accept})
            with urllib.request.urlopen(req, timeout=60) as fh:
                return json.loads(fh.read())
        except Exception as exc:  # noqa: BLE001 - retried, then re-raised
            last = exc
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"fetch failed after {retries} attempts: {url}: {last}")


# ------------------------------------------------------------------- resolution


def hgnc_to_ensembl(hgnc_id: str, cache: Cache) -> str | None:
    key = f"hgnc2ens::{hgnc_id.lower()}"
    hit = cache.get(key)
    if hit is not None:
        return hit or None
    num = hgnc_id.split(":", 1)[1]
    doc = fetch_json(f"https://rest.genenames.org/fetch/hgnc_id/{num}")
    docs = doc.get("response", {}).get("docs") or []
    ens = docs[0].get("ensembl_gene_id") if docs else None
    cache.put(key, ens or "")
    return ens


def ortholog(ensg: str, target_species: str, cache: Cache) -> tuple[str | None, str | None]:
    """Return (ortholog_gene_id, orthology_type) in the target species, or (None, None)."""
    key = f"ortho::{ensg}::{target_species}"
    hit = cache.get(key)
    if hit is not None:
        return (hit[0] or None, hit[1] or None)
    url = (
        f"https://rest.ensembl.org/homology/id/human/{ensg}"
        f"?target_species={target_species};type=orthologues;format=condensed"
    )
    # A fetch failure must NEVER be cached as "no ortholog" -- that makes a
    # transient rate-limit indistinguishable from a real absence, and poisons
    # the cache so re-runs reproduce it offline. Let it raise.
    doc = fetch_json(url)
    data = doc.get("data") or []
    homs = data[0].get("homologies") if data else []
    if not homs:
        cache.put(key, ["", ""])
        return (None, None)
    # Prefer a one2one ortholog when one exists.
    best = next((h for h in homs if h.get("type") == "ortholog_one2one"), homs[0])
    out = [best.get("id") or "", best.get("type") or ""]
    cache.put(key, out)
    return (out[0] or None, out[1] or None)


def expression_comparison(genes: list[str], cache: Cache) -> list[dict]:
    """Bgee multi-species expression comparison over homologous anatomy."""
    key = "cmp::" + "|".join(sorted(genes))
    hit = cache.get(key)
    if hit is not None:
        return hit
    gene_list = urllib.parse.quote("\n".join(genes))
    url = (
        "https://www.bgee.org/api/?page=expression_comparison"
        f"&action=submit_expression_comparison&display_type=json&gene_list={gene_list}"
    )
    doc = fetch_json(url)
    results = doc.get("data", {}).get("comparisonResults") or []
    slim = []
    for r in results:
        cond = r.get("multiSpeciesCondition") or {}
        anat = [a.get("id") for a in (cond.get("anatEntities") or []) if a.get("id")]
        anat += [c.get("id") for c in (cond.get("cellTypes") or []) if c.get("id")]
        names = [a.get("name") for a in (cond.get("anatEntities") or [])]
        slim.append(
            {
                "anat": anat,
                "name": names[0] if names else "",
                "conservation": r.get("conservationScore"),
                "present": [g.get("geneId") for g in (r.get("genesExpressionPresent") or [])],
                "absent": [g.get("geneId") for g in (r.get("genesExpressionAbsent") or [])],
                "nodata": [g.get("geneId") for g in (r.get("genesNoData") or [])],
            }
        )
    cache.put(key, slim)
    return slim


# ----------------------------------------------------------------------- verdict


def _verdict_over(matched: list[dict], ensg: str, orth: str) -> tuple[str, str]:
    """Reduce the matched multi-species conditions to a single verdict."""
    for c in matched:
        if ensg in c["present"] and orth in c["absent"]:
            return (
                "DIVERGENT_ABSENT",
                f"{c['name'] or c['anat'][0]}: human expressed, ortholog reported absent",
            )
    for c in matched:
        if ensg in c["present"] and orth in c["present"]:
            return ("CONSERVED", f"{c['name'] or c['anat'][0]}: both expressed")
    for c in matched:
        if orth in c["nodata"]:
            return ("MODEL_NO_DATA", f"{c['name'] or c['anat'][0]}: no call for ortholog")
    return ("HUMAN_NO_DATA", f"{matched[0]['name']}: no call for human gene")


def classify(
    node_anat: list[str],
    ensg: str,
    orth: str,
    orth_type: str,
    comps: list[dict],
    tissue_fallback: bool = False,
) -> tuple[str, str, str]:
    """Return (verdict, detail, granularity) for one model-mechanism link."""
    if orth_type and orth_type != "ortholog_one2one":
        return ("ORTHOLOG_NOT_1TO1", f"orthology type {orth_type}", "GENE")

    cell_terms = {a for a in node_anat if a.startswith("CL:")}
    tissue_terms = {a for a in node_anat if a.startswith("UBERON:")}

    # Prefer an exact match at whatever granularity the node was curated at.
    wanted = set(node_anat)
    matched = [c for c in comps if wanted & set(c["anat"])]
    if matched:
        verdict, detail = _verdict_over(matched, ensg, orth)
        hit = set().union(*(set(c["anat"]) for c in matched)) & wanted
        return (verdict, detail, "CELL_TYPE" if hit & cell_terms else "TISSUE")

    # Nothing matched. Distinguish "Bgee has no condition for these cell types"
    # from "no condition for these tissues" -- they are different problems.
    if cell_terms and not tissue_terms:
        if not tissue_fallback:
            return (
                "ANATOMY_UNMATCHED_CL",
                f"no Bgee multi-species condition for {sorted(cell_terms)}",
                "NONE",
            )
        return (
            "ANATOMY_UNMATCHED_CL",
            f"cell-type only, no UBERON location on node to fall back to: {sorted(cell_terms)}",
            "NONE",
        )

    if cell_terms and tissue_fallback and tissue_terms:
        matched = [c for c in comps if tissue_terms & set(c["anat"])]
        if matched:
            verdict, detail = _verdict_over(matched, ensg, orth)
            return (verdict, f"[tissue-level] {detail}", "TISSUE")

    label = "ANATOMY_UNMATCHED_CL" if cell_terms else "ANATOMY_UNMATCHED_TISSUE"
    return (label, f"no Bgee multi-species condition for {sorted(wanted)}", "NONE")


# -------------------------------------------------------------------- extraction


def candidates_from(path: str) -> list[dict]:
    """Pull every (animal model -> mechanism link) whose target node carries anatomy."""
    try:
        doc = safe_load(open(path))
    except Exception:
        return []
    if not isinstance(doc, dict):
        return []

    genes = []
    for g in doc.get("genetic") or []:
        if isinstance(g, dict) and isinstance(g.get("gene_term"), dict):
            term = g["gene_term"].get("term") or {}
            gid = str(term.get("id", ""))
            if gid.lower().startswith("hgnc:"):
                genes.append((gid, term.get("label")))
    if not genes:
        return []

    nodes: dict[str, list[tuple[str, str]]] = {}
    for node in doc.get("pathophysiology") or []:
        if not isinstance(node, dict):
            continue
        anat = []
        for key in ("cell_types", "locations"):
            for item in node.get(key) or []:
                if isinstance(item, dict) and isinstance(item.get("term"), dict):
                    tid = str(item["term"].get("id", ""))
                    if tid.startswith(("CL:", "UBERON:")):
                        anat.append((tid, item["term"].get("label")))
        if anat:
            nodes[node.get("name")] = anat

    out = []
    for model in doc.get("animal_models") or []:
        if not isinstance(model, dict):
            continue
        for link in model.get("modeled_mechanisms") or []:
            if not isinstance(link, dict):
                continue
            target = link.get("target")
            if target not in nodes:
                continue
            out.append(
                {
                    "file": os.path.basename(path)[:-5],
                    "species": model.get("species"),
                    "genotype": model.get("genotype"),
                    "relationship": link.get("relationship"),
                    "fidelity": link.get("fidelity"),
                    "target": target,
                    "anat": nodes[target],
                    "genes": genes[:4],
                }
            )
    return out


# ---------------------------------------------------------------------- driver


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--file", action="append", help="specific kb/disorders/*.yaml (repeatable)")
    ap.add_argument("--all", action="store_true", help="every disorder with animal models")
    ap.add_argument("--limit", type=int, default=0, help="stop after N checked links")
    ap.add_argument("--tsv", help="write results to this TSV")
    ap.add_argument("--findings-only", action="store_true", help="print only actionable verdicts")
    ap.add_argument(
        "--tissue-fallback",
        action="store_true",
        help="when a CL-bound node has no Bgee condition, retry against that node's own "
        "UBERON locations; matched rows are reported with granularity=TISSUE",
    )
    ap.add_argument("--cache", default="tmp/bgee_cache.json")
    ap.add_argument("--sleep", type=float, default=0.34, help="pause between Bgee calls")
    args = ap.parse_args()

    if args.file:
        paths = args.file
    elif args.all:
        paths = sorted(glob.glob("kb/disorders/*.yaml"))
    else:
        ap.error("pass --file or --all")

    cache = Cache(args.cache)
    cands: list[dict] = []
    for path in paths:
        # cheap prefilter: skip files that cannot contribute
        try:
            head = open(path, encoding="utf-8").read()
        except OSError:
            continue
        if "modeled_mechanisms:" not in head or "animal_models:" not in head:
            continue
        cands.extend(candidates_from(path))

    print(f"# {len(cands)} model-mechanism links with anatomy + genes", file=sys.stderr)

    rows, stats = [], Counter()
    for cand in cands:
        if args.limit and len(rows) >= args.limit:
            break
        species_key = str(cand["species"] or "").strip().lower()
        mapping = SPECIES.get(species_key)
        if not mapping:
            stats["SPECIES_UNMAPPED"] += 1
            continue
        ens_species, _taxon = mapping

        hgnc_id, symbol = cand["genes"][0]
        try:
            ensg = hgnc_to_ensembl(hgnc_id, cache)
        except RuntimeError:
            stats["LOOKUP_ERROR"] += 1
            continue
        if not ensg:
            stats["NO_ENSEMBL"] += 1
            continue

        try:
            orth, orth_type = ortholog(ensg, ens_species, cache)
        except RuntimeError as exc:
            # A lookup failure is not a fidelity signal, and must not abort the
            # sweep -- one bad species or a rate-limit would lose the whole run.
            stats["ORTHOLOG_FETCH_ERROR"] += 1
            print(f"  ! {cand['file']}: ortholog lookup failed: {exc}", file=sys.stderr)
            continue
        if not orth:
            verdict, detail, gran = (
                "ORTHOLOG_LOOKUP_EMPTY",
                f"Ensembl returned no {ens_species} ortholog of {symbol} -- VERIFY",
                "GENE",
            )
            comps = []
        else:
            try:
                comps = expression_comparison([ensg, orth], cache)
            except RuntimeError as exc:
                stats["BGEE_ERROR"] += 1
                print(f"  ! {cand['file']}: {exc}", file=sys.stderr)
                continue
            verdict, detail, gran = classify(
                [a for a, _ in cand["anat"]], ensg, orth, orth_type, comps, args.tissue_fallback
            )
            time.sleep(args.sleep)

        stats[verdict] += 1
        rows.append(
            {
                "file": cand["file"],
                "species": cand["species"],
                "gene": symbol,
                "ensg": ensg,
                "ortholog": orth or "",
                "orthology": orth_type or "",
                "node": cand["target"],
                "anatomy": ";".join(a for a, _ in cand["anat"]),
                "relationship": cand["relationship"] or "",
                "fidelity": cand["fidelity"] or "",
                "verdict": verdict,
                "granularity": gran,
                "detail": detail,
            }
        )

        if not args.findings_only or verdict in FINDING_VERDICTS:
            flag = "**" if verdict in FINDING_VERDICTS else "  "
            print(
                f"{flag} {verdict:18} {cand['file'][:30]:32} {symbol:8} "
                f"{str(cand['species'])[:10]:12} {str(cand['relationship'])[:22]:24} "
                f"{gran:9} {detail[:52]}"
            )

    cache.flush()

    print("\n# verdicts:", file=sys.stderr)
    for verdict, count in stats.most_common():
        mark = " <- finding" if verdict in FINDING_VERDICTS else ""
        print(f"#   {verdict:20} {count:5}{mark}", file=sys.stderr)

    if args.tsv:
        cols = list(rows[0].keys()) if rows else []
        os.makedirs(os.path.dirname(args.tsv) or ".", exist_ok=True)
        with open(args.tsv, "w", encoding="utf-8") as fh:
            fh.write("\t".join(cols) + "\n")
            for row in rows:
                fh.write("\t".join(str(row[c]).replace("\t", " ") for c in cols) + "\n")
        print(f"# wrote {len(rows)} rows to {args.tsv}", file=sys.stderr)


if __name__ == "__main__":
    main()
