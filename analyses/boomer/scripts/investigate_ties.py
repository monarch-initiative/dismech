"""Enumerate three small tied KBs and isolate their namespace constraints.

Counterfactuals are in-memory experiments; saved inputs and solutions are read-only.
"""

from __future__ import annotations

import argparse
from copy import deepcopy
import hashlib
from itertools import product
import json
from math import isclose, prod
from pathlib import Path
import subprocess
import sys

from dismech import kb_cache

REPO = Path(__file__).resolve().parents[3]
CASES = {
    "ADan_amyloidosis": ("icd11f:2086401830", "icd11f:54507082"),
    "CANVAS": ("ORDO:139564", "ORDO:504476"),
    "Methylcobalamin_Deficiency_Type_cblE": ("DOID:0050732", "DOID:0112255"),
}


def enumerate_worlds(kb, model, reasoner):
    worlds = []
    for values in product((False, True), repeat=len(kb.pfacts)):
        if reasoner.reason(kb, list(enumerate(values))).satisfiable:
            probability = prod(
                f.prob if value else 1 - f.prob
                for f, value in zip(kb.pfacts, values, strict=True)
            )
            worlds.append((probability, values))
    worlds.sort(reverse=True)
    total = sum(p for p, _ in worlds)
    best = worlds[0][0]
    optimal = [values for p, values in worlds if isclose(p, best, rel_tol=1e-12)]
    return {
        "distinct_solutions": len(worlds),
        "confidence": round(best / sum(p for p, _ in worlds[:2]), 12),
        "best_posterior": round(best / total, 12),
        "top_solutions": [
            {
                "prior": round(p, 12),
                "posterior": round(p / total, 12),
                "assignment": list(values),
            }
            for p, values in worlds[:5]
        ],
        "optimal_assignments": [list(values) for values in optimal],
        "rejected_high_prior_indices": [
            [
                i
                for i, value in enumerate(values)
                if not value and kb.pfacts[i].prob >= 0.5
            ]
            for values in optimal
        ],
        "marginals": [
            round(sum(p for p, values in worlds if values[i]) / total, 12)
            for i in range(len(kb.pfacts))
        ],
    }


def investigate(base, model, reasoner):
    results = {}
    for slug, pair in CASES.items():
        folder = base / "proxy-merges/baseline" / slug
        if not (folder / "solution.yaml").exists():
            folder = base / "disorders" / slug
        path = folder / "kb.yaml"
        original = path.read_bytes()
        data = kb_cache.load_document(path)
        kb = model.KB.model_validate(data)
        indices = [
            i
            for i, pf in enumerate(kb.pfacts)
            if pf.fact.fact_type == "EquivalentTo" and pf.fact.equivalent in pair
        ]
        assert len(indices) == 2
        memberships = [
            fact
            for fact in kb.facts
            if fact.fact_type == "MemberOfDisjointGroup" and fact.sub in pair
        ]
        assert len(memberships) == 2
        assert memberships[0].group == memberships[1].group
        assert (
            sum(
                f.fact_type == "MemberOfDisjointGroup"
                and f.group == memberships[0].group
                for f in kb.facts
            )
            == 2
        )
        core = model.KB(facts=memberships, pfacts=[kb.pfacts[i] for i in indices])
        assert not reasoner.reason(core, [(0, True), (1, True)]).satisfiable
        # Every assertion is necessary: removing any one restores satisfiability.
        for i in range(2):
            reduced = core.model_copy(deep=True)
            del reduced.facts[i]
            assert reasoner.reason(reduced, [(0, True), (1, True)]).satisfiable
            reduced = core.model_copy(deep=True)
            del reduced.pfacts[i]
            assert reasoner.reason(reduced, [(0, True)]).satisfiable
        baseline = enumerate_worlds(kb, model, reasoner)
        saved = kb_cache.load_document(folder / "solution.yaml")
        baseline["saved_assignment"] = [
            f["truth_value"] for f in saved["solved_pfacts"]
        ]
        assert baseline["saved_assignment"] in baseline["optimal_assignments"]
        assert len({tuple(s["assignment"]) for s in baseline["top_solutions"]}) == len(
            baseline["top_solutions"]
        )
        assert baseline["confidence"] == saved["confidence"] == 0.5
        assert (
            baseline["distinct_solutions"]
            == saved["number_of_satisfiable_combinations"]
        )
        assert isclose(
            baseline["best_posterior"], saved["posterior_prob"], abs_tol=1e-11
        )
        for marginal, fact in zip(
            baseline["marginals"], saved["solved_pfacts"], strict=True
        ):
            assert isclose(marginal, fact["posterior_prob"], abs_tol=1e-11)
        relaxed = kb.model_copy(deep=True)
        relaxed.facts.remove(memberships[0])
        relaxed_result = enumerate_worlds(relaxed, model, reasoner)
        assert relaxed_result["rejected_high_prior_indices"] == [[]]
        # Independent intervention: remove the first mapping hypothesis entirely.
        dropped = kb.model_copy(deep=True)
        del dropped.pfacts[indices[0]]
        dropped_result = enumerate_worlds(dropped, model, reasoner)
        assert dropped_result["rejected_high_prior_indices"] == [[]]
        results[slug] = {
            "input_sha256": hashlib.sha256(original).hexdigest(),
            "competing_targets": list(pair),
            "competing_indices": indices,
            "hypotheses": [
                {"index": i, "fact": pf.fact.model_dump(), "prior": pf.prob}
                for i, pf in enumerate(kb.pfacts)
            ],
            "labels": deepcopy(data.get("labels", {})),
            "minimal_conflict": core.model_dump(exclude_none=True),
            "baseline": baseline,
            "relax_first_target_namespace_membership": relaxed_result,
            "remove_first_mapping_hypothesis": {
                "removed_original_index": indices[0],
                "remaining_original_indices": [
                    i for i in range(len(kb.pfacts)) if i != indices[0]
                ],
                **dropped_result,
            },
        }
        assert path.read_bytes() == original
    return results


def current_alternatives(base, model, reasoner):
    """Independently verify and display the current CANVAS and cblE optima."""
    results = {}
    for slug in ("CANVAS", "Methylcobalamin_Deficiency_Type_cblE"):
        folder = base / "disorders" / slug
        data = kb_cache.load_document(folder / "kb.yaml")
        saved = kb_cache.load_document(folder / "solution.yaml")
        metadata = json.loads((folder / "solve.json").read_text())
        input_hash = hashlib.sha256((folder / "kb.yaml").read_bytes()).hexdigest()
        assert metadata["input_sha256"] == input_hash
        assert metadata["status"] in {"ALL_MAPPINGS_CONSISTENT", "RETRACTED"}
        assert not saved.get("timed_out")
        kb = model.KB.model_validate(data)
        result = enumerate_worlds(kb, model, reasoner)
        result["saved_assignment"] = [p["truth_value"] for p in saved["solved_pfacts"]]
        assert result["saved_assignment"] in result["optimal_assignments"]
        assert result["confidence"] == saved["confidence"]
        assert (
            result["distinct_solutions"] == saved["number_of_satisfiable_combinations"]
        )
        assert isclose(result["best_posterior"], saved["posterior_prob"], abs_tol=1e-11)
        for marginal, fact in zip(
            result["marginals"], saved["solved_pfacts"], strict=True
        ):
            assert isclose(marginal, fact["posterior_prob"], abs_tol=1e-11)
        results[slug] = {
            "input_sha256": input_hash,
            "hypotheses": [
                {"index": i, "fact": pf.fact.model_dump(), "prior": pf.prob}
                for i, pf in enumerate(kb.pfacts)
            ],
            "labels": deepcopy(data.get("labels", {})),
            "baseline": result,
        }
    return results


def render_alternatives(slug, entry):
    """Show complete distinct assignments, with input priors separate from marginals."""
    baseline = entry["baseline"]
    saved = baseline["saved_assignment"]
    solutions = sorted(
        baseline["top_solutions"],
        key=lambda s: (-s["prior"], s["assignment"] != saved),
    )
    lines = [
        f"# {slug}: top five distinct solutions",
        "",
        "Generated by exhaustive Boolean enumeration of the saved input. Each row",
        "in the summary is a different complete assignment, counted once. Ties",
        "have no preferred order; the saved optimum is displayed first.",
        "Five are shown; equal-scoring alternatives may extend beyond the cutoff.",
        "",
        "| Solution | Whole-assignment prior | Whole-assignment posterior | Changes from saved assignment |",
        "|---|---:|---:|---|",
    ]
    for rank, solution in enumerate(solutions, 1):
        differences = [
            f"H{i + 1} → {value}"
            for i, value in enumerate(solution["assignment"])
            if value != saved[i]
        ]
        name = f"{rank} (saved)" if solution["assignment"] == saved else str(rank)
        lines.append(
            f"| {name} | {solution['prior']:.12f} | {solution['posterior']:.12f} | {', '.join(differences) or 'None'} |"
        )
    lines += [
        "",
        f"Confidence = P(solution 1) / (P(solution 1) + P(solution 2)) = **{baseline['confidence']}**.",
        f"The posterior denominator includes all **{baseline['distinct_solutions']}** satisfiable assignments, not just these five.",
        "",
        "## Complete assignments",
        "",
        "**Input prior** is the assigned probability that a mapping is true before",
        "conditioning on consistency. **Marginal posterior** is its probability of",
        "being true across all consistent assignments. **True/False** in a solution",
        "column is that solution's choice, not a claim that its probability is 1/0.",
        "A false choice contributes `1 − prior` to that assignment's weight.",
        "",
        "| Hypothesis | Mapping | Input prior P(true) | Marginal posterior P(true) | S1 | S2 | S3 | S4 | S5 |",
        "|---|---|---:|---:|---|---|---|---|---|",
    ]
    for i, hypothesis in enumerate(entry["hypotheses"]):
        fact = hypothesis["fact"]
        obj = fact.get("equivalent", fact.get("sup"))
        relation = "≡" if fact["fact_type"] == "EquivalentTo" else "⊂"
        mapping = f"`{fact['sub']}` {relation} `{obj}`"
        choices = " | ".join(str(s["assignment"][i]) for s in solutions)
        lines.append(
            f"| H{i + 1} | {mapping} | {hypothesis['prior']} | {baseline['marginals'][i]:.12f} | {choices} |"
        )
    lines += ["", "## Labels", ""]
    for curie, label in entry["labels"].items():
        lines.append(f"- `{curie}`: {label}")
    lines += ["", f"Input SHA-256: `{entry['input_sha256']}`.", ""]
    return "\n".join(lines)


def main():
    kb_cache.default_off()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--boomer-src", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument(
        "--current",
        action="store_true",
        help="Show current CANVAS/cblE alternatives instead of historical interventions",
    )
    args = parser.parse_args()
    source = args.boomer_src.expanduser().resolve()
    commit = subprocess.check_output(
        ["git", "-C", str(source), "rev-parse", "HEAD"], text=True
    ).strip()
    assert not subprocess.check_output(
        ["git", "-C", str(source), "status", "--porcelain"], text=True
    ).strip()
    sys.path.insert(0, str(source))
    from boomer import model, search

    reasoner = search.get_reasoner(model.SearchConfig().reasoner_class)
    result = {
        "boomer_commit": commit,
        "method": "exhaustive Boolean enumeration",
        "cases": (current_alternatives if args.current else investigate)(
            REPO / "analyses/boomer", model, reasoner
        ),
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2) + "\n")
    for slug, entry in result["cases"].items():
        (args.out.parent / f"{slug}-alternatives.md").write_text(
            render_alternatives(slug, entry)
        )
        if args.current:
            print(slug, entry["baseline"]["confidence"])
            continue
        print(
            slug,
            entry["baseline"]["confidence"],
            "->",
            entry["relax_first_target_namespace_membership"]["confidence"],
        )


if __name__ == "__main__":
    main()
