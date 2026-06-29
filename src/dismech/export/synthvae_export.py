"""Pathograph -> per-disease HPO frequency prior, for synthetic-patient generation.

This is the bridge between the dismech pathograph and the synthetic-patient VAE
generator (https://github.com/justaddcoffee/synthetic_vae_generator). It projects
each MONDO-anchored disorder into a compact, sampleable prior:

    {disease MONDO id, label, genes, phenotypes:[{hpo_id, label, probability,
     frequency_source, branch}], excluded:[...]}

* ``probability`` is the curated phenotype frequency converted to a numeric
  Bernoulli parameter (the curated marginal P(phenotype | disease)). It reuses
  the frequency parsing in :mod:`dismech.export.hpoa_export` (literal percent /
  ratio in the description, an HP Frequency term, or the dismech FrequencyEnum)
  and maps HP Frequency bands to their midpoint probability.
* ``branch`` is the nearest upstream ``pathophysiology`` node in the disease's
  pathograph (``pathographs/MONDO_*.json``), i.e. which mechanistic sub-pathway
  the phenotype hangs off. A downstream sampler can use it to induce *curated*
  within-branch co-occurrence (the structure the VAE otherwise has to learn from
  sparse case data) rather than sampling every phenotype independently.

The output is deliberately model-agnostic. It works three ways for the VAE
project: (a) a standalone knowledge-based sampler for cold-start / rare diseases
with no real cases (see ``scripts/synthvae_sampler.py``); (b) a structured prior
to regularize the VAE; (c) a biology-grounded plausibility check on VAE output.

Why a separate exporter from ``hpoa_export``: HPOA is an annotation file (one
row per evidence item, ordinal HP Frequency terms, human-evidence-only rules).
This emits a per-disease *generative* record with numeric probabilities and the
causal-branch grouping a sampler needs. The frequency parsing is shared, not
duplicated.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict, deque
from pathlib import Path
from typing import Any

import yaml

from dismech.export.hpoa_export import normalize_frequency_enum, parse_frequency

# HP Frequency band -> representative (midpoint) probability for sampling.
# Ranges are the HPO canonical bands; midpoints are used so the curated marginal
# is a single defensible number. OBLIGATE=1.0, EXCLUDED=0.0.
HP_FREQ_TO_PROB: dict[str, float] = {
    "HP:0040280": 1.0,    # Obligate (100%)
    "HP:0040281": 0.90,   # Very frequent (80-99%)
    "HP:0040282": 0.55,   # Frequent (30-79%)
    "HP:0040283": 0.17,   # Occasional (5-29%)
    "HP:0040284": 0.025,  # Very rare (1-4%)
    "HP:0040285": 0.0,    # Excluded (0%)
}

_PCT_RANGE = re.compile(r"^(\d+)\s*[-–]\s*(\d+)\s*%$")
_PCT_SINGLE = re.compile(r"^(\d+)\s*%$")
_RATIO = re.compile(r"^(\d+)\s*/\s*(\d+)$")

# Causal predicates along which disease progression flows (used to walk a
# phenotype back to its mechanistic branch). variant_of / treats / targets /
# models are not progression edges and are ignored.
PROGRESSION_PREDICATES = frozenset({"causes", "leads_to", "contributes_to"})


def frequency_to_probability(phenotype: dict[str, Any]) -> tuple[float | None, str]:
    """Return (probability, source_label) for a phenotype's curated frequency.

    Source label records *where* the number came from so consumers can tell a
    literal percent ("12%") from a coarse band ("Frequent") from an unknown.
    Probability is ``None`` when the frequency is genuinely unspecified, leaving
    the choice of a default to the sampler.
    """
    freq = parse_frequency(phenotype)  # "X%" | "X-Y%" | "X/N" | "HP:00402xx" | None
    if freq is None:
        return None, "unknown"
    if freq in HP_FREQ_TO_PROB:
        return HP_FREQ_TO_PROB[freq], "band"
    m = _PCT_RANGE.match(freq)
    if m:
        return (int(m.group(1)) + int(m.group(2))) / 200.0, "literal"
    m = _PCT_SINGLE.match(freq)
    if m:
        return min(int(m.group(1)) / 100.0, 1.0), "literal"
    m = _RATIO.match(freq)
    if m and int(m.group(2)):
        return min(int(m.group(1)) / int(m.group(2)), 1.0), "literal"
    return None, "unknown"


def _genes(data: dict[str, Any]) -> list[dict[str, str]]:
    """Collect HGNC gene descriptors from the genetic + pathophysiology sections."""
    seen: dict[str, dict[str, str]] = {}
    for entry in data.get("genetic") or []:
        term = ((entry.get("gene_term") or {}).get("term") or {})
        gid = term.get("id")
        if gid and gid not in seen:
            seen[gid] = {"id": gid, "label": term.get("label") or ""}
    for node in data.get("pathophysiology") or []:
        for g in node.get("genes") or []:
            term = (g.get("term") or {})
            gid = term.get("id")
            if gid and gid not in seen:
                seen[gid] = {"id": gid, "label": term.get("label") or ""}
    return list(seen.values())


def _branch_index(pathograph_path: Path) -> dict[str, str]:
    """Map each phenotype HP id to its nearest upstream pathophysiology branch.

    Reads the exported pathograph JSON, walks causal edges backwards from each
    phenotype node to the closest ``pathophysiology`` ancestor, and keys the
    result by the phenotype node's HP ``term_id`` so it joins to the YAML.
    """
    try:
        graph = json.loads(pathograph_path.read_text())
    except (OSError, ValueError):
        return {}

    node_type = {n["id"]: n.get("node_type") for n in graph.get("nodes", [])}
    parents: dict[str, list[str]] = defaultdict(list)
    for e in graph.get("edges", []):
        if e.get("predicate") in PROGRESSION_PREDICATES:
            parents[e["target"]].append(e["source"])

    def nearest_branch(start: str) -> str | None:
        seen, q = {start}, deque(parents.get(start, []))
        while q:
            cur = q.popleft()
            if node_type.get(cur) == "pathophysiology":
                return cur
            if cur not in seen:
                seen.add(cur)
                q.extend(parents.get(cur, []))
        return None

    out: dict[str, str] = {}
    for n in graph.get("nodes", []):
        if n.get("node_type") != "phenotype":
            continue
        hp = (n.get("meta") or {}).get("term_id")
        if not hp:
            continue
        branch = nearest_branch(n["id"])
        if branch:
            out[hp] = branch
    return out


def _find_pathograph(disease_id: str, pathograph_dir: Path) -> Path | None:
    """Locate ``pathographs/MONDO_<id>.json`` for a MONDO disease id."""
    stem = disease_id.replace(":", "_")
    exact = pathograph_dir / f"{stem}.json"
    if exact.exists():
        return exact
    matches = sorted(pathograph_dir.glob(f"{stem}*.json"))  # subtype suffixes
    return matches[0] if matches else None


def disease_prior(
    yaml_path: Path, pathograph_dir: Path = Path("pathographs")
) -> dict[str, Any] | None:
    """Project one disorder YAML to a sampleable per-disease prior, or None.

    Returns None when the disorder has no MONDO id (the sampler/VAE world keys
    on MONDO). MONDO-typed phenotype entries are disease-disease comorbidities,
    not features, and are skipped. Phenotypes with an ``EXCLUDED`` frequency are
    split out into ``excluded`` (asserted-absent constraints) rather than the
    sampleable list.
    """
    data = yaml.safe_load(yaml_path.read_text()) or {}
    disease = ((data.get("disease_term") or {}).get("term") or {})
    disease_id = disease.get("id") or ""
    if not disease_id.startswith("MONDO:"):
        return None

    pg = _find_pathograph(disease_id, pathograph_dir)
    branches = _branch_index(pg) if pg else {}

    phenotypes: list[dict[str, Any]] = []
    excluded: list[dict[str, str]] = []
    for phen in data.get("phenotypes") or []:
        term = ((phen.get("phenotype_term") or {}).get("term") or {})
        hpo_id = term.get("id") or ""
        if not hpo_id.startswith("HP:"):
            continue  # untyped/comorbidity entries are not sampleable HP features
        label = term.get("label") or phen.get("name") or ""
        if normalize_frequency_enum(phen.get("frequency")) == "EXCLUDED":
            excluded.append({"hpo_id": hpo_id, "label": label})
            continue
        prob, source = frequency_to_probability(phen)
        phenotypes.append(
            {
                "hpo_id": hpo_id,
                "label": label,
                "name": phen.get("name") or label,
                "probability": prob,
                "frequency_source": source,
                "branch": branches.get(hpo_id),
            }
        )

    if not phenotypes:
        return None

    return {
        "disease_id": disease_id,
        "disease_name": disease.get("label") or data.get("name") or yaml_path.stem,
        "dismech_name": data.get("name") or yaml_path.stem,
        "genes": _genes(data),
        "pathograph": pg.name if pg else None,
        "phenotypes": phenotypes,
        "excluded": excluded,
    }


def export(
    kb_dir: Path, pathograph_dir: Path, out_path: Path
) -> tuple[int, int]:
    """Write a JSON array of per-disease priors. Returns (n_diseases, n_phenotypes)."""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    priors = []
    n_phen = 0
    for yaml_path in sorted(kb_dir.glob("*.yaml")):
        rec = disease_prior(yaml_path, pathograph_dir)
        if rec:
            priors.append(rec)
            n_phen += len(rec["phenotypes"])
    out_path.write_text(json.dumps(priors, indent=2) + "\n")
    return len(priors), n_phen


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Project dismech disorders to per-disease HPO frequency priors for "
            "synthetic-patient generation (the pathograph<->VAE bridge)."
        )
    )
    parser.add_argument("--kb-dir", type=Path, default=Path("kb/disorders"))
    parser.add_argument(
        "--pathograph-dir", type=Path, default=Path("pathographs")
    )
    parser.add_argument(
        "--out", type=Path, default=Path("output/synthvae/disease_priors.json")
    )
    args = parser.parse_args()
    n_dis, n_phen = export(args.kb_dir, args.pathograph_dir, args.out)
    print(f"wrote {n_dis} disease priors ({n_phen} phenotypes) -> {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
