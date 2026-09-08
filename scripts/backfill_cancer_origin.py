#!/usr/bin/env python3
"""Mark the somatic origin lesion on neoplasm entries that already describe one.

``scripts/check_cancer_origin.py`` derives a cancer's cell of origin from the
pathophysiology node carrying ``genetic_context.variant_origin: SOMATIC``. When
that marking was introduced, almost no entry had it -- not because the entries
lack the information, but because it lived only in prose. This script moves it
into structure.

**It invents nothing.** A node is only marked when its own ``name`` already
states a somatic genetic lesion in as many words --
mutation, fusion, translocation, rearrangement, amplification, biallelic
inactivation, loss of heterozygosity. A node saying merely that a pathway is
active is not a lesion and is left alone, and any node whose text says the
variant is germline, inherited or constitutional is excluded outright. So the
edit is a transcription of what the curator already wrote, not a new claim.

Candidate selection, per unmarked somatic-neoplasm entry:

1. the node's **name** states a genetic lesion (``LESION_RE``). Matching the
   description too was tried and rejected: it pulled in pathway and consequence
   nodes whose description merely mentions the driver ("MAPK/ERK Pathway
   Activation", "Erythroid Maturation Arrest at the Proerythroblast Stage"),
   and stamping ``variant_origin: SOMATIC`` on those asserts a lesion the node
   does not carry, even when the cell it binds happens to be the right one;
2. the node's text states neither a germline/inherited origin (``GERMLINE_RE``)
   nor a viral oncoprotein mechanism (``VIRAL_RE``) -- HPV E7 inactivating pRB
   is not a host genetic lesion, and there is no variant for ``variant_origin``
   to describe. Those cancers derive their origin from the exposure rule;
3. the node is neither a microenvironment node (macrophage, Treg and fibroblast
   are where the tumor lives, not where it came from) nor an acquired-resistance
   or progression node -- those carry lesion vocabulary and are real somatic
   events, but they happen long after the disease starts;
4. the node binds at least one CL term, so the derivation actually yields a
   cell. ``--bind-single-cell`` relaxes this one case: when the lesion node
   binds nothing but the entry as a whole names exactly one cell type, that cell
   is bound onto the lesion node as well. The entry is then already asserting a
   single lineage, and the only thing being added is *where* in the graph it
   belongs. Entries naming several cells are left alone: choosing among them is
   the curator's call, not a script's;
5. root nodes win when the entry has any, since the origin lesion is the one
   nothing upstream causes.

An entry with exactly one surviving candidate is applied automatically. An entry
with several candidates binding **different** cells is left for a human: that is
either a genuine multi-lineage entry (a grouping in disguise) or a curation
error, and this script must not decide which.

Usage::

    just backfill-cancer-origin              # dry run: proposals + counts
    just backfill-cancer-origin --apply      # write the single-candidate cases
    just backfill-cancer-origin --format tsv
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))

from check_cancer_origin import (
    _downstream_targets,
    _terms,
    assess,
    iter_paths,
)

from dismech.yaml_io import safe_load_path

# Vocabulary of an actual genetic lesion. "Activation" and "signaling" are
# deliberately absent: a pathway running hot is a state, not a lesion, and the
# node describing it is downstream of the event we are looking for.
LESION_RE = re.compile(
    r"\bmutation|\bmutant|\bmutated|missense|nonsense|frameshift|\bfusion\b"
    r"|translocation|translocated|rearrangement|rearranged|amplification|amplified"
    r"|\bdeletion\b|\bduplication\b|copy[- ]number|loss of heterozygosity|\bLOH\b"
    r"|biallelic|oncohistone|\bsomatic\b|\bacquired\b"
    # Bare "hypermethylation" is a chromatin state that is routinely downstream
    # of the lesion (Epithelioid_Sarcoma's H3K27 hypermethylation sits under
    # SMARCB1 loss), so only promoter-level silencing of a gene counts.
    r"|promoter hypermethylation|epigenetic silencing|promoter methylation|\bt\(\d+;\d+\)|internal tandem"
    r"|\bITD\b|hotspot|truncating|splice[- ]site|oncogene formation"
    # "Inactivation" and "loss" are lesion words only when they qualify a gene
    # or an allele. "TP53 Pathway Inactivation" and "Loss of p53-Dependent
    # Checkpoint Control" are downstream states, and marking them would assert
    # a lesion the node does not carry.
    r"|(?<!pathway )(?<!signaling )inactivation of\b"
    r"|(?<!pathway )(?<!signaling )(?<!axis )inactivation\b(?! of (a |the )?(pathway|signaling|checkpoint))"
    r"|loss of function|loss[- ]of[- ]function"
    r"|(tumou?r[- ]suppressor|second[- ]hit|biallelic|allelic|homozygous|gene)\s+loss"
    # "SMARCB1 (INI1) Loss" -- a gene symbol, optionally with a parenthetical
    # alias, immediately before "loss".
    r"|\b[A-Z][A-Z0-9-]{2,}\d?\b(?:\s*\([A-Z0-9/-]+\))?\s+loss\b"
    r"|\bdriver (lesion|alteration|mutation|event)|oncogenic (lesion|alteration)"
    r"|(genetic|genomic|molecular|chromosomal|cytogenetic|epigenetic[- ]regulator)"
    r"\s+(alteration|lesion|abnormalit)",
    re.IGNORECASE,
)

# A node naming the setting rather than the lesion. The checker no longer needs
# this -- it reads structured markers only -- but a *proposal* pass does, because
# a microenvironment node can carry lesion vocabulary ("stromal MYC
# amplification") while binding macrophage and fibroblast.
CONTEXT_NODE_RE = re.compile(
    r"microenvironment|immune (evasion|escape|suppress|surveillance)"
    r"|immunosuppress|t-?cell exhaustion|desmoplas|tumou?r stroma"
    r"|stromal (remodel|activation|reaction)|angiogen|myeloid suppression",
    re.IGNORECASE,
)

# Acquired-resistance and relapse nodes carry lesion vocabulary ("ESR1
# Mutation-Driven Endocrine Resistance", "Acquired MAPK Reactivation") and are
# genuinely somatic events, but they happen years after the disease starts. A
# curator may still mark one; a script proposing them would systematically
# mistake progression for origin.
RESISTANCE_RE = re.compile(
    r"resistan|relapse|refractory|selection pressure|escape|reactivation"
    r"|bypass|progression|metasta|transformation to|richter",
    re.IGNORECASE,
)

# A viral oncoprotein inactivating a host tumor suppressor is not a host
# genetic lesion -- there is no variant for `variant_origin` to describe. This
# is the HTLV-1 Tax situation CLAUDE.md already rules on, and it is how four HPV
# entries (E6/E7-mediated p53 and pRB inactivation) were wrongly marked: the
# bare `inactivation` branch matched the *protein* being inactivated. Such
# cancers derive their origin through the ENVIRONMENTAL_TRIGGER rule instead.
VIRAL_RE = re.compile(
    r"\boncoprotein|\bE6\b|\bE7\b|\bHPV\b|papillomavirus|\bEBV\b|epstein"
    r"|\bHTLV|\bHBV\b|\bHCV\b|hepatitis [BC]\b|\bKSHV\b|\bHHV-?8\b"
    r"|\bTax\b|viral (protein|oncogene|oncoprotein)|virus-mediated",
    re.IGNORECASE,
)

# Any hint that the variant is inherited rather than acquired. Conservative on
# purpose: a false exclusion costs one manual entry, a false inclusion asserts
# the wrong variant origin.
GERMLINE_RE = re.compile(
    r"germline|inherited|heritable|hereditary|constitutional|familial"
    r"|de novo|autosomal|carrier|predispos",
    re.IGNORECASE,
)


@dataclass
class Proposal:
    path: Path
    node_name: str
    cell_ids: list[str]
    # Two different strings on purpose: `cell_names` is what the source
    # descriptor's `preferred_term` says (a hedge, sometimes), `cell_labels` is
    # the canonical ontology label. A borrowed binding has to reproduce both, in
    # their own slots -- writing the name into `term.label` breaks the ontology
    # term contract and fails `just validate-terms`.
    cell_names: list[str]
    cell_labels: list[str]
    is_root: bool
    matched: str
    has_genetic_context: bool = False
    borrowed_cell: bool = False


# CL's two generic transformed-cell terms. They name "a neoplastic cell", which
# is true of every tumor and identifies no lineage, so they cannot answer "what
# did this arise from".
GENERIC_CELLS = {"CL:0001063", "CL:0001064"}


def _node_text(node: dict) -> str:
    return f"{node.get('name', '')} {node.get('description', '') or ''}"


def propose(path: Path, *, bind_single_cell: bool = False) -> tuple[list[Proposal], str]:
    """Return candidate origin nodes for one entry, plus a status word."""
    report = assess(path)
    if report is None or not report.is_neoplasm or report.is_predisposition:
        return [], "skipped"
    if any(o.rule == "SOMATIC_LESION" for o in report.origins):
        return [], "already-marked"

    data = safe_load_path(path)
    nodes = [n for n in (data.get("pathophysiology") or []) if isinstance(n, dict)]
    targeted = _downstream_targets(nodes)

    candidates: list[Proposal] = []
    for node in nodes:
        name = str(node.get("name", ""))
        # The lesion must be in the NAME. A description mentioning the driver
        # does not make a downstream node the site of the lesion.
        match = LESION_RE.search(name)
        if not match:
            continue
        # Germline wording is checked against name AND description: excluding
        # too much costs one manual entry, including too much asserts the wrong
        # variant origin.
        if GERMLINE_RE.search(_node_text(node)):
            continue
        if CONTEXT_NODE_RE.search(name) or RESISTANCE_RE.search(name):
            continue
        if VIRAL_RE.search(_node_text(node)):
            continue
        cells = [
            (cid, cell_name)
            for cid, cell_name in _terms(node.get("cell_types"))
            if cid not in GENERIC_CELLS
        ]
        labels = dict(_terms(node.get("cell_types"), display=False))
        borrowed = False
        if not cells and bind_single_cell:
            entry_cells = {
                cid: cell_name
                for other in nodes
                for cid, cell_name in _terms(other.get("cell_types"))
                if cid not in GENERIC_CELLS
            }
            if len(entry_cells) == 1:
                cells = list(entry_cells.items())
                labels = {
                    cid: label
                    for other in nodes
                    for cid, label in _terms(other.get("cell_types"), display=False)
                }
                borrowed = True
        if not cells:
            continue
        candidates.append(
            Proposal(
                path=path,
                node_name=str(node.get("name", "")),
                cell_ids=[c for c, _ in cells],
                cell_names=[cell_name for _, cell_name in cells],
                # `labels` is keyed by the same `term.id` guard `cells` is,
                # and is unfiltered, so it is a superset -- never a miss.
                cell_labels=[labels[c] for c, _ in cells],
                is_root=node.get("name") not in targeted,
                matched=match.group(0),
                has_genetic_context=isinstance(node.get("genetic_context"), dict),
                borrowed_cell=borrowed,
            )
        )

    if not candidates:
        return [], "no-candidate"

    # The origin lesion is the one nothing upstream causes.
    roots = [c for c in candidates if c.is_root]
    if roots:
        candidates = roots

    distinct_cells = {tuple(sorted(set(c.cell_ids))) for c in candidates}
    if len(candidates) > 1 and len(distinct_cells) > 1:
        return candidates, "ambiguous"
    return candidates, "ready"


def _name_line_pattern(name: str) -> re.Pattern:
    escaped = re.escape(name)
    return re.compile(rf"^- name: (?:{escaped}|\"{escaped}\"|'{escaped}')\s*$", re.MULTILINE)


def _scalar(value: str) -> str:
    """Emit `value` as a YAML scalar, quoted whenever plain would not survive.

    This script writes YAML as text, and since `preferred_term` became curator
    free text rather than an ontology label the character surface is wide enough
    to matter: the KB already holds values like `EMG: myopathic abnormalities`,
    where an unquoted colon-space makes a nested mapping instead of a string.
    (`ATP:ADP antiporter activity` is fine plain -- only `: ` separates a
    mapping -- and PyYAML knows the difference, which is why the decision is
    delegated to it rather than to a hand-written character test.)
    """
    dumped = yaml.safe_dump(
        {"v": value}, default_flow_style=False, allow_unicode=True, width=10**9
    )[len("v: ") :].rstrip("\n")
    # A value containing a newline dumps across lines, which would not survive
    # being spliced into a fixed indentation. JSON's double-quoted form is a
    # valid YAML scalar and stays on one line.
    return json.dumps(value) if "\n" in dumped else dumped


def _cell_block(proposal: Proposal) -> str:
    """The `cell_types` YAML for a borrowed binding, or nothing."""
    if not proposal.borrowed_cell:
        return ""
    out = "  cell_types:\n"
    for cid, name, label in zip(
        proposal.cell_ids, proposal.cell_names, proposal.cell_labels
    ):
        out += (
            f"  - preferred_term: {_scalar(name)}\n"
            f"    term:\n      id: {_scalar(cid)}\n      label: {_scalar(label)}\n"
        )
    return out


def apply_proposal(path: Path, proposals: list[Proposal]) -> bool:
    """Insert `genetic_context.variant_origin: SOMATIC` after each node's name.

    Text insertion rather than a YAML round-trip: ruamel would reflow quoting
    and folded scalars across the whole file, burying a two-line change in a
    thousand-line diff.
    """
    text = path.read_text()
    for proposal in proposals:
        pattern = _name_line_pattern(proposal.node_name)
        matches = list(pattern.finditer(text))
        if len(matches) != 1:
            # Zero means a multi-line or quoted name this script should not
            # rewrite; more than one means the name is ambiguous in the file.
            print(
                f"  skip (name matched {len(matches)}x): "
                f"{path.name}: {proposal.node_name!r}",
                file=sys.stderr,
            )
            return False
        match = matches[0]
        if proposal.has_genetic_context:
            # The node already carries a genetic_context (gene, allele type,
            # functional impact) that simply never recorded variant_origin.
            # Adding a second block would be a duplicate YAML key: legal to
            # PyYAML, which silently keeps the last one, and fatal to the
            # ruamel-based reference validator (dismech#8623). Merge instead.
            block = re.compile(r"^  genetic_context:\s*$", re.MULTILINE)
            existing = block.search(text, match.end())
            if existing is None:
                print(
                    f"  skip (genetic_context not found): "
                    f"{path.name}: {proposal.node_name!r}",
                    file=sys.stderr,
                )
                return False
            insert_at = existing.end() + 1
            text = text[:insert_at] + "    variant_origin: SOMATIC\n" + text[insert_at:]
            # ...and then fall through to the borrowed-cell write. Returning
            # early here silently dropped it, leaving the node marked but
            # unbound while the run still reported success.
            text = text[: match.end() + 1] + _cell_block(proposal) + text[match.end() + 1 :]
            continue
        insertion = "  genetic_context:\n    variant_origin: SOMATIC\n" + _cell_block(
            proposal
        )
        text = text[: match.end() + 1] + insertion + text[match.end() + 1 :]
    path.write_text(text)
    return True


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("files", nargs="*")
    parser.add_argument(
        "--apply", action="store_true", help="write the single-candidate cases"
    )
    parser.add_argument("--format", choices=("summary", "tsv"), default="summary")
    parser.add_argument(
        "--bind-single-cell",
        action="store_true",
        help="also bind the entry's sole cell type onto a lesion node that has none",
    )
    args = parser.parse_args(argv)

    ready: dict[Path, list[Proposal]] = {}
    ambiguous: dict[Path, list[Proposal]] = {}
    no_candidate: list[Path] = []
    already = 0

    for path in iter_paths(args.files):
        proposals, status = propose(path, bind_single_cell=args.bind_single_cell)
        if status == "ready":
            ready[path] = proposals
        elif status == "ambiguous":
            ambiguous[path] = proposals
        elif status == "no-candidate":
            no_candidate.append(path)
        elif status == "already-marked":
            already += 1

    if args.format == "tsv":
        print("status\tpath\tnode\tcells\tmatched\troot")
        for status, group in (("ready", ready), ("ambiguous", ambiguous)):
            for path, proposals in group.items():
                for p in proposals:
                    cells = ";".join(
                        f"{i} {name}" for i, name in zip(p.cell_ids, p.cell_names)
                    )
                    print(
                        f"{status}\t{path.relative_to(ROOT)}\t{p.node_name}\t"
                        f"{cells}\t{p.matched}\t{p.is_root}"
                    )
        for path in no_candidate:
            print(f"no-candidate\t{path.relative_to(ROOT)}\t\t\t\t")
        return 0

    print(f"already marked:            {already}")
    print(f"ready (one candidate):     {len(ready)}")
    print(f"ambiguous (several cells): {len(ambiguous)}")
    print(f"no candidate in prose:     {len(no_candidate)}")
    print()

    if ambiguous:
        print("-- ambiguous, left for a human --")
        for path, proposals in ambiguous.items():
            print(f"  {path.relative_to(ROOT)}")
            for p in proposals:
                cells = "; ".join(p.cell_names)
                print(f"     {p.node_name!r}: {cells}")
        print()

    if not args.apply:
        print("Dry run. Re-run with --apply to write the ready cases.")
        return 0

    written = 0
    for path, proposals in ready.items():
        if apply_proposal(path, proposals):
            written += 1
    print(f"Marked {written} entry(ies).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
