#!/usr/bin/env python3
"""Bind ``AnimalModel`` free text to ontologies: ``species`` -> NCBITaxon,
``associated_phenotypes`` -> MP.

Why
---
``AnimalModel`` is the least ontologically grounded class in the model stack.
``ExperimentalModel`` — the *non-animal* NAM class — carries an
``organism: OrganismDescriptor`` bound to NCBITaxon, while ``AnimalModel.species``
is a plain string. The result, measured over the KB before this migration: 487
species assertions across 50 distinct spellings, with a single taxon written four
different ways (``Mouse`` / ``Mus musculus`` / ``mouse`` / ``Mouse (Mus musculus)``),
and 725 ``associated_phenotypes`` strings with zero ontology grounding.

Meanwhile ``NCBITaxon:10090`` appears 175 times elsewhere in the KB — entirely on
``datasets[].organism``. Mouse-the-dataset-organism is grounded; mouse-the-model is
a string. That asymmetry is what this script closes, and closing it is what makes a
dismech animal model joinable to an MGI/IMPC/ZFIN/RGD record.

MP specifically, and not HP, for the phenotype half: MP is the vocabulary MGI, IMPC
and RGD assert against. ``kb/disorders/SNF8-Related_Neurodevelopmental_Disorder.yaml``
is the proof that the grounding is being *discarded on ingest* rather than being
unavailable — its curator queried the IMPC API live and then wrote the results down
as three plain strings, one of which (``preweaning lethality, complete penetrance``)
is an exact MP label (MP:0011100).

What it will not do
-------------------
This is a binding pass, not a curation pass, so every rule is biased toward
refusing to guess. In this repository a wrong CURIE is worse than no CURIE
(``.claude/skills/dismech-terms``: *no term beats a bad one*), and a mechanical
migration is exactly where a plausible-looking wrong term gets laundered into
data that later validation confirms rather than catches.

Concretely:

* **Phenotype matching is exact-only** — normalized label or normalized exact
  synonym. No partial, prefix, or fuzzy matching. ``Skeletal defects`` finding no
  MP class is the correct outcome, not a reason to loosen the rule.
* **Species with more than one surviving candidate are left alone.** ``Fruit fly``
  exact-searches to *Tephritidae* **first**, ahead of *Drosophila melanogaster* —
  auto-taking the top hit would assert the wrong family. Reported ``AMBIGUOUS``.
* **NCBI homonym nodes are filtered out.** NCBITaxon disambiguates genus/family
  homonyms with angle brackets (``Mus <genus>``, ``Drosophila <flies,genus>``);
  those labels are never a species and are dropped before the candidate count.
* **Multi-species strings are refused** (``Mouse and rat``,
  ``Drosophila melanogaster and Xenopus laevis``). One ``species_term`` cannot
  represent two organisms; splitting the model entry is a curator's call.
* **Human is never auto-bound.** ``Human (patient-derived)`` resolves cleanly to
  NCBITaxon:9606, but ``AnimalModel`` is documented as a *whole-organism animal*
  model — a human entry here is misfiled and belongs in ``experimental_models``.
  Reported ``MISFILED_HUMAN`` for a curator rather than silently grounded.
* **The free text is never deleted.** Both deprecated slots stay, and the original
  wording is preserved as the descriptor's ``preferred_term``. MOD phenotype calls
  carry penetrance and zygosity qualifiers that no single MP class captures, so the
  string is not redundant with the binding.

The corroboration rule
----------------------
Parenthetical species strings are self-checking, and the script exploits it. Both
``Mouse (Mus musculus)`` (common name outside, binomial inside) and
``Danio rerio (zebrafish)`` (the reverse) yield two independently resolvable
fragments. When both resolve to the *same* taxon, that is two agreeing lookups
rather than one, and the row is marked ``AUTO(corroborated)``. When they disagree,
the row is ``CONFLICT`` and nothing is written.

Alias table
-----------
``CURATOR_ALIASES`` below handles strings the automatic rule cannot settle but a
human can, each with its reason in-line. It is deliberately tiny and deliberately
in the source where a reviewer sees it, rather than in a data file. Adding an entry
is a curation decision under review, not configuration.

Usage
-----
    uv run python scripts/backfill_animal_model_terms.py                  # dry run
    uv run python scripts/backfill_animal_model_terms.py --apply
    uv run python scripts/backfill_animal_model_terms.py --report out.tsv
    uv run python scripts/backfill_animal_model_terms.py --species-only
    uv run python scripts/backfill_animal_model_terms.py --strict         # exit 1 on any unresolved

Resolution is cached to ``--cache`` (default ``.animal_model_term_cache.json``,
gitignored) because every uncached lookup is an OLS round trip of roughly two
seconds and there are 667 distinct phenotype strings. Delete the cache to re-derive.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
KB_GLOBS = ("kb/disorders/*.yaml", "kb/modules/*.yaml", "kb/comorbidities/*.yaml")

TAXON_ADAPTER = "ols:ncbitaxon"
MP_ADAPTER = "ols:mp"

HUMAN = "NCBITaxon:9606"

# Strings the automatic rule cannot settle, resolved by a curator. Each entry
# records why the automatic path fails, and each CURIE is still verified against
# NCBITaxon at run time -- the table supplies the *name*, never an unchecked ID.
CURATOR_ALIASES: dict[str, tuple[str, str]] = {
    # abbreviated genus: exact search cannot expand "C." to "Caenorhabditis"
    "c. elegans": ("Caenorhabditis elegans", "abbreviated genus initial"),
    # "Fruit fly" exact-matches Tephritidae (true fruit flies) ahead of
    # Drosophila. Every KB use of the bare common name is a Drosophila model --
    # verified against each model's own genotype/description text.
    "fruit fly": ("Drosophila melanogaster", "common name collides with Tephritidae"),
    # "Roundworm" is a common name shared across nematodes; the KB usage is
    # C. elegans, stated in the same entry.
    "roundworm": ("Caenorhabditis elegans", "common name shared across nematodes"),
    # Bare "Rat" exact-matches both the genus Rattus and Rattus norvegicus, and
    # the genus label carries no NCBI homonym marker to filter on. Every rat
    # model in the KB is the laboratory rat.
    "rat": ("Rattus norvegicus", "common name also matches the genus Rattus"),
    # "Medaka fish" -- NCBITaxon label is the binomial; the common name maps to
    # the genus as well as the species.
    "medaka fish": ("Oryzias latipes", "common name also matches the genus"),
    "medaka": ("Oryzias latipes", "common name also matches the genus"),
    # "Guinea pig" resolves to Cavia porcellus but also to the genus Cavia.
    "guinea pig": ("Cavia porcellus", "common name also matches the genus"),
}

# Species strings that are refused outright, with the reason reported.
MULTI_SPECIES_RE = re.compile(r"\b(?:and|,|/|\+|&)\b", re.IGNORECASE)

PAREN_RE = re.compile(r"^(?P<outer>[^(]*)\((?P<inner>[^)]*)\)\s*$")
HOMONYM_RE = re.compile(r"<[^>]*>")


def normalize(text: str) -> str:
    """Lowercase, collapse whitespace, drop a trailing period."""
    return re.sub(r"\s+", " ", text.strip().rstrip(".")).lower()


@dataclass
class Resolution:
    """One free-text string and what it resolved to."""

    raw: str
    verdict: str
    curie: str | None = None
    label: str | None = None
    detail: str = ""
    candidates: list[str] = field(default_factory=list)

    @property
    def bindable(self) -> bool:
        return self.verdict.startswith("AUTO") and self.curie is not None


class Resolver:
    """Exact-match resolution against an OAK adapter, with an on-disk cache."""

    def __init__(self, adapter_string: str, cache: dict, offline: bool = False):
        self._adapter_string = adapter_string
        self._adapter = None
        self._cache = cache
        self._offline = offline

    @property
    def adapter(self):
        if self._adapter is None:
            from oaklib import get_adapter

            self._adapter = get_adapter(self._adapter_string)
        return self._adapter

    def label(self, curie: str) -> str | None:
        key = f"label::{curie}"
        if key not in self._cache:
            if self._offline:
                return None
            try:
                self._cache[key] = self.adapter.label(curie)
            except Exception as exc:  # noqa: BLE001 - network/adapter failures are reportable, not fatal
                self._cache[key] = None
                print(f"  ! label lookup failed for {curie}: {exc}", file=sys.stderr)
        return self._cache[key]

    def ancestors(self, curie: str) -> list[str]:
        key = f"anc::{curie}"
        if key not in self._cache:
            if self._offline:
                return []
            try:
                self._cache[key] = [str(a) for a in
                                    self.adapter.ancestors([curie], predicates=["rdfs:subClassOf"])]
            except Exception as exc:  # noqa: BLE001
                self._cache[key] = []
                print(f"  ! ancestor lookup failed for {curie}: {exc}", file=sys.stderr)
        return list(self._cache[key])

    def search_exact(self, text: str) -> list[str]:
        """Exact (non-partial) search over labels and aliases."""
        key = f"search::{normalize(text)}"
        if key not in self._cache:
            if self._offline:
                return []
            from oaklib.datamodels.search import (
                SearchConfiguration,
                SearchProperty,
                SearchTermSyntax,
            )

            cfg = SearchConfiguration(
                properties=[SearchProperty.LABEL, SearchProperty.ALIAS],
                syntax=SearchTermSyntax.PLAINTEXT,
                is_partial=False,
            )
            try:
                self._cache[key] = list(self.adapter.basic_search(text, config=cfg))
            except Exception as exc:  # noqa: BLE001
                self._cache[key] = []
                print(f"  ! search failed for {text!r}: {exc}", file=sys.stderr)
        return list(self._cache[key])


# ---------------------------------------------------------------------------
# species
# ---------------------------------------------------------------------------


def _taxon_candidates(resolver: Resolver, fragment: str) -> list[tuple[str, str]]:
    """Exact-search a name fragment, dropping NCBI homonym (non-species) nodes."""
    out: list[tuple[str, str]] = []
    for curie in resolver.search_exact(fragment):
        if not str(curie).startswith("NCBITaxon:"):
            continue
        label = resolver.label(curie)
        if not label or HOMONYM_RE.search(str(label)):
            # "Mus <genus>", "Drosophila <flies,genus>" -- NCBI's homonym
            # disambiguator, never the species a model is described in.
            continue
        out.append((str(curie), str(label)))
    return out


def resolve_species(resolver: Resolver, raw: str) -> Resolution:
    text = raw.strip()
    norm = normalize(text)

    alias = CURATOR_ALIASES.get(norm)
    if alias is not None:
        name, reason = alias
        cands = _taxon_candidates(resolver, name)
        if len(cands) == 1:
            return Resolution(raw, "AUTO(alias)", cands[0][0], cands[0][1],
                              f"curator alias -> {name!r} ({reason})")
        return Resolution(raw, "UNRESOLVED", detail=f"alias {name!r} did not resolve uniquely",
                          candidates=[c[0] for c in cands])

    match = PAREN_RE.match(text)
    fragments = [text]
    if match:
        # "Mouse (Mus musculus)" and "Danio rerio (zebrafish)" both give two
        # independently resolvable names; agreement between them is corroboration.
        fragments = [f for f in (match.group("outer"), match.group("inner")) if f.strip()]
    elif MULTI_SPECIES_RE.search(text):
        return Resolution(raw, "MULTI_SPECIES",
                          detail="names more than one organism; one species_term cannot represent both")

    resolved: dict[str, str] = {}
    all_candidates: list[str] = []
    for frag in fragments:
        frag = frag.strip()
        if not frag:
            continue
        cands = _taxon_candidates(resolver, frag)
        all_candidates.extend(c[0] for c in cands)
        if len(cands) == 1:
            resolved[frag] = cands[0][0]

    distinct = set(resolved.values())
    if len(distinct) == 1:
        curie = next(iter(distinct))
        if curie == HUMAN:
            return Resolution(raw, "MISFILED_HUMAN", curie, resolver.label(curie),
                              "AnimalModel is for whole-organism ANIMAL models; "
                              "a human entry belongs in experimental_models")
        verdict = "AUTO(corroborated)" if len(resolved) > 1 else "AUTO"
        return Resolution(raw, verdict, curie, resolver.label(curie),
                          f"resolved from {sorted(resolved)}")
    if len(distinct) > 1:
        # A common name is often a *higher taxon* than the binomial beside it:
        # "Roundworm (Caenorhabditis elegans)" resolves Nematoda against
        # C. elegans. When one candidate is an ancestor of the other, the pair is
        # not a disagreement -- it is one organism named at two ranks, and the
        # more specific name is the one the model is. This deliberately does NOT
        # rescue sibling species: "Vervet monkey (Chlorocebus sabaeus)" resolves
        # two different Chlorocebus species, neither an ancestor of the other,
        # and stays a CONFLICT for a curator.
        specific = [c for c in distinct
                    if not any(c in resolver.ancestors(other) for other in distinct if other != c)]
        if len(specific) == 1:
            curie = specific[0]
            return Resolution(raw, "AUTO(most-specific)", curie, resolver.label(curie),
                              f"fragments name one organism at two ranks: {resolved}")
        return Resolution(raw, "CONFLICT", detail=f"fragments disagree: {resolved}",
                          candidates=sorted(distinct))
    if len(set(all_candidates)) > 1:
        return Resolution(raw, "AMBIGUOUS", detail=f"{len(set(all_candidates))} exact matches survive filtering",
                          candidates=sorted(set(all_candidates)))
    return Resolution(raw, "UNRESOLVED", detail="no exact NCBITaxon match")


# ---------------------------------------------------------------------------
# phenotypes
# ---------------------------------------------------------------------------


def resolve_phenotype(resolver: Resolver, raw: str) -> Resolution:
    text = raw.strip()
    cands = [c for c in resolver.search_exact(text) if str(c).startswith("MP:")]
    uniq = sorted(set(str(c) for c in cands))
    if len(uniq) == 1:
        return Resolution(raw, "AUTO", uniq[0], resolver.label(uniq[0]), "exact MP label/synonym match")
    if len(uniq) > 1:
        return Resolution(raw, "AMBIGUOUS", detail=f"{len(uniq)} exact MP matches", candidates=uniq)
    return Resolution(raw, "NO_MATCH", detail="no exact MP label or synonym")


# ---------------------------------------------------------------------------
# file rewriting
# ---------------------------------------------------------------------------


# A ruamel round-trip re-emits the whole document, and on the minority of KB
# files that carry hand-wrapped plain scalars it unwraps them: an early version
# of this script produced 6,342 lines of pure re-wrapping noise against 4,000
# lines of actual insertion. CLAUDE.md warns specifically that gratuitous churn
# causes conflicts across concurrent curation PRs, so this writes by inserting
# text at a line anchor instead, leaving every untouched byte untouched -- and
# then proves the result semantically identical apart from the new keys
# (`verify_only_additions`).
#
# The anchor has two shapes, because a key may be the first in its list item:
#     - species: Mus musculus      <- on the dash line
#       species: Dog               <- a later key
# and the sequence itself may be flush with its parent key or indented under it
# (both styles are in the KB), so the dash indent is measured, never assumed.
KEY_LINE_RE_TEMPLATE = r"^(?:{dash}- |{body}){key}:(?P<rest>.*)$"
BLOCK_SCALAR_RE = re.compile(r"^\s*[>|&*]")


def _emit_block(value, indent: int) -> list[str]:
    """Render a value as YAML lines at the given indent, using safe quoting."""
    import yaml as pyyaml

    text = pyyaml.safe_dump(value, sort_keys=False, allow_unicode=True,
                            default_flow_style=False, width=10**6)
    pad = " " * indent
    return [(pad + line).rstrip() + "\n" if line.strip() else "\n"
            for line in text.rstrip("\n").split("\n")]


def _descriptor(preferred: str, curie: str, label: str) -> dict:
    return {"preferred_term": preferred, "term": {"id": curie, "label": label}}


def _animal_models_span(lines: list[str]) -> tuple[int, int] | None:
    """Line span (start, end) of the top-level ``animal_models:`` block."""
    for i, line in enumerate(lines):
        if line.rstrip("\n") == "animal_models:":
            for j in range(i + 1, len(lines)):
                if lines[j][:1] not in (" ", "-", "\n", "#"):
                    return i + 1, j
            return i + 1, len(lines)
    return None


def _item_spans(lines: list[str], start: int, end: int) -> tuple[list[tuple[int, int]], int]:
    """Spans of each list item in the block, plus the measured dash indent.

    Both sequence styles occur in the KB -- flush (``- name:`` at column 0) and
    indented (``  - name:`` under ``animal_models:``) -- so the indent of the
    first dash defines the block and every other item must match it.
    """
    dash_indent = None
    for i in range(start, end):
        match = re.match(r"^( *)- ", lines[i])
        if match:
            dash_indent = len(match.group(1))
            break
    if dash_indent is None:
        return [], 0
    prefix = " " * dash_indent + "- "
    starts = [i for i in range(start, end) if lines[i].startswith(prefix)]
    spans = [(s, starts[k + 1] if k + 1 < len(starts) else end)
             for k, s in enumerate(starts)]
    return spans, dash_indent


def _find_key(lines: list[str], span: tuple[int, int], key: str, dash_indent: int):
    """Locate a direct child key of a list item; returns (index, match) or None."""
    pattern = re.compile(KEY_LINE_RE_TEMPLATE.format(
        dash=" " * dash_indent, body=" " * (dash_indent + 2), key=re.escape(key)))
    for i in range(span[0], span[1]):
        match = pattern.match(lines[i].rstrip("\n"))
        if match:
            return i, match
    return None


def _list_end(lines: list[str], first: int, end: int, body_indent: int) -> int:
    """End of the block sequence whose items begin at ``first``."""
    item = " " * body_indent + "- "
    cont = " " * (body_indent + 2)
    i = first
    while i < end and (lines[i].startswith(item) or lines[i].startswith(cont)
                       or not lines[i].strip()):
        i += 1
    return i


def verify_only_additions(original: str, updated: str, added_keys: tuple[str, ...]) -> str | None:
    """Prove the rewrite added only ``added_keys`` and changed nothing else.

    Strips the new keys back out of the updated document and compares the parsed
    result against the parsed original. This is the check that makes line-level
    text surgery safe: a misplaced insertion changes the parse, and a mangled
    anchor makes the file fail to load. Returns an error string, or None if clean.
    """
    import yaml as pyyaml

    try:
        before = pyyaml.safe_load(original)
        after = pyyaml.safe_load(updated)
    except Exception as exc:  # noqa: BLE001
        return f"updated file does not parse: {exc}"
    for model in (after or {}).get("animal_models") or []:
        if isinstance(model, dict):
            for key in added_keys:
                model.pop(key, None)
    if before != after:
        return "rewrite changed content beyond the added keys"
    return None


def process_file(path: Path, species_res: dict[str, Resolution],
                 pheno_res: dict[str, Resolution], do_species: bool, do_phenos: bool,
                 apply: bool) -> Counter:
    import yaml as pyyaml

    stats: Counter = Counter()
    original = path.read_text()
    try:
        doc = pyyaml.safe_load(original)
    except Exception:  # noqa: BLE001
        return stats
    if not isinstance(doc, dict) or not doc.get("animal_models"):
        return stats

    lines = original.splitlines(keepends=True)
    span = _animal_models_span(lines)
    if span is None:
        stats["files_skipped_no_block"] += 1
        return stats

    models = [m for m in doc["animal_models"] if isinstance(m, dict)]
    item_spans, dash_indent = _item_spans(lines, *span)
    body_indent = dash_indent + 2
    if len(item_spans) != len(models):
        # Structure this scanner does not understand (flow style, a nested
        # sequence). Refuse rather than insert at a guessed offset.
        stats["files_skipped_unparsed_structure"] += 1
        return stats

    # Collect insertions as (line_index_to_insert_after, rendered_lines), then
    # apply them from the bottom up so earlier indices stay valid.
    insertions: list[tuple[int, list[str]]] = []

    for model, item_span in zip(models, item_spans):
        if do_species and model.get("species") is not None:
            if "species_term" in model:
                stats["species_already_bound"] += 1
            else:
                raw = str(model["species"]).strip()
                res = species_res.get(raw)
                if res is not None and res.bindable:
                    found = _find_key(lines, item_span, "species", dash_indent)
                    if found is None or BLOCK_SCALAR_RE.match(found[1].group("rest")):
                        stats["species_skipped_unanchorable"] += 1
                    else:
                        idx, _ = found
                        insertions.append(
                            (idx, _emit_block(
                                {"species_term": _descriptor(raw, res.curie, res.label)},
                                body_indent))
                        )
                        stats["species_bound"] += 1
                else:
                    stats[f"species_skipped_{res.verdict if res else 'UNKNOWN'}"] += 1

        if do_phenos and model.get("associated_phenotypes"):
            if "associated_phenotype_terms" in model:
                stats["phenotypes_already_bound"] += 1
                continue
            bound = []
            for raw in model["associated_phenotypes"]:
                if not isinstance(raw, str):
                    continue
                res = pheno_res.get(raw.strip())
                if res is not None and res.bindable:
                    bound.append(_descriptor(raw.strip(), res.curie, res.label))
                    stats["phenotypes_bound"] += 1
                else:
                    stats[f"phenotypes_skipped_{res.verdict if res else 'UNKNOWN'}"] += 1
            if bound:
                found = _find_key(lines, item_span, "associated_phenotypes", dash_indent)
                if found is None:
                    stats["phenotypes_skipped_unanchorable"] += 1
                else:
                    end = _list_end(lines, found[0] + 1, item_span[1], body_indent)
                    insertions.append(
                        (end - 1, _emit_block({"associated_phenotype_terms": bound},
                                              body_indent))
                    )

    if not insertions:
        return stats

    updated_lines = list(lines)
    for idx, block in sorted(insertions, key=lambda pair: -pair[0]):
        updated_lines[idx + 1:idx + 1] = block
    updated = "".join(updated_lines)

    problem = verify_only_additions(original, updated,
                                    ("species_term", "associated_phenotype_terms"))
    if problem:
        stats["files_rejected_verification"] += 1
        print(f"  ! {path.name}: {problem} — not written", file=sys.stderr)
        return stats

    if apply:
        path.write_text(updated)
        stats["files_written"] += 1
    else:
        stats["files_would_change"] += 1
    return stats


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------


def collect_strings(paths: list[Path]) -> tuple[Counter, Counter, dict]:
    import yaml as pyyaml

    species: Counter = Counter()
    phenos: Counter = Counter()
    where: dict[str, set] = defaultdict(set)
    for path in paths:
        try:
            doc = pyyaml.safe_load(path.read_text())
        except Exception:  # noqa: BLE001
            continue
        if not isinstance(doc, dict):
            continue
        for model in doc.get("animal_models") or []:
            if not isinstance(model, dict):
                continue
            if model.get("species"):
                key = str(model["species"]).strip()
                species[key] += 1
                where[key].add(path.name)
            for raw in model.get("associated_phenotypes") or []:
                if isinstance(raw, str):
                    phenos[raw.strip()] += 1
    return species, phenos, where


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="*", type=Path, help="KB files (default: all animal-model-bearing files)")
    ap.add_argument("--apply", action="store_true", help="write changes (default: dry run)")
    ap.add_argument("--species-only", action="store_true")
    ap.add_argument("--phenotypes-only", action="store_true")
    ap.add_argument("--report", type=Path, help="write a per-string TSV resolution report")
    ap.add_argument("--cache", type=Path, default=REPO_ROOT / ".animal_model_term_cache.json")
    ap.add_argument("--offline", action="store_true", help="use only the cache; never call OAK")
    ap.add_argument("--strict", action="store_true", help="exit 1 if any string is unresolved")
    args = ap.parse_args(argv)

    do_species = not args.phenotypes_only
    do_phenos = not args.species_only

    paths = args.files or sorted(
        {p for pattern in KB_GLOBS for p in REPO_ROOT.glob(pattern)}
    )

    cache: dict = {}
    if args.cache and args.cache.exists():
        cache = json.loads(args.cache.read_text())

    species_strings, pheno_strings, where = collect_strings(paths)
    print(f"scanned {len(paths)} files: "
          f"{sum(species_strings.values())} species assertions ({len(species_strings)} distinct), "
          f"{sum(pheno_strings.values())} phenotype strings ({len(pheno_strings)} distinct)")

    tax = Resolver(TAXON_ADAPTER, cache, args.offline)
    mp = Resolver(MP_ADAPTER, cache, args.offline)

    species_res: dict[str, Resolution] = {}
    if do_species:
        print(f"\nresolving {len(species_strings)} distinct species strings against NCBITaxon...")
        for raw in sorted(species_strings):
            species_res[raw] = resolve_species(tax, raw)

    pheno_res: dict[str, Resolution] = {}
    if do_phenos:
        print(f"resolving {len(pheno_strings)} distinct phenotype strings against MP...")
        for i, raw in enumerate(sorted(pheno_strings), 1):
            pheno_res[raw] = resolve_phenotype(mp, raw)
            if i % 100 == 0:
                print(f"   {i}/{len(pheno_strings)}")
                if args.cache:
                    args.cache.write_text(json.dumps(cache))

    if args.cache:
        args.cache.write_text(json.dumps(cache))

    # ---- report -----------------------------------------------------------
    def summarize(title: str, res: dict[str, Resolution], counts: Counter) -> None:
        if not res:
            return
        verdicts = Counter(r.verdict for r in res.values())
        inst = Counter()
        for raw, r in res.items():
            inst[r.verdict] += counts[raw]
        print(f"\n{title}")
        for v, n in verdicts.most_common():
            print(f"  {v:22s} {n:4d} distinct  {inst[v]:4d} instances")
        for v in sorted(verdicts):
            if v.startswith("AUTO"):
                continue
            examples = [r for r in res.values() if r.verdict == v]
            print(f"  -- {v} --")
            for r in sorted(examples, key=lambda r: -counts[r.raw])[:8]:
                extra = f" [{', '.join(r.candidates[:4])}]" if r.candidates else ""
                print(f"     {counts[r.raw]:3d}x {r.raw!r}: {r.detail}{extra}")
            if len(examples) > 8:
                print(f"     ... and {len(examples) - 8} more")

    summarize("SPECIES -> NCBITaxon", species_res, species_strings)
    summarize("ASSOCIATED PHENOTYPES -> MP", pheno_res, pheno_strings)

    if args.report:
        with args.report.open("w") as fh:
            fh.write("kind\tinstances\traw\tverdict\tcurie\tlabel\tdetail\tcandidates\tfiles\n")
            for kind, res, counts in (("species", species_res, species_strings),
                                      ("phenotype", pheno_res, pheno_strings)):
                for raw, r in sorted(res.items()):
                    fh.write("\t".join([
                        kind, str(counts[raw]), raw, r.verdict, r.curie or "", r.label or "",
                        r.detail, ";".join(r.candidates),
                        ";".join(sorted(where.get(raw, []))[:5]),
                    ]) + "\n")
        print(f"\nwrote resolution report: {args.report}")

    # ---- rewrite ----------------------------------------------------------
    totals: Counter = Counter()
    for path in paths:
        totals.update(process_file(path, species_res, pheno_res,
                                   do_species, do_phenos, args.apply))

    print("\n" + ("APPLIED" if args.apply else "DRY RUN — no files written"))
    for key in sorted(totals):
        print(f"  {key:38s} {totals[key]}")

    if args.strict:
        unresolved = sum(1 for r in list(species_res.values()) + list(pheno_res.values())
                         if not r.bindable)
        if unresolved:
            print(f"\nstrict: {unresolved} distinct strings unresolved", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
