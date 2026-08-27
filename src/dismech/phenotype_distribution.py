"""EHR-derived phenotype profiles: loading, linting, and evidence export.

A *profile set* is a YAML file conforming to
``src/dismech/schema/phenotype_distribution.yaml``. Each set is about one
disease and holds profiles; each profile is one interpretable pattern — a
label and one weighted-code distribution per clinical domain.

This module does three things:

1. **Load** sets from ``kb/phenotype_distributions/`` (and the worked example
   under ``examples/phenotype_distributions/``).
2. **Lint** what the LinkML schema cannot express — duplicate profile ids, code
   weights summing above 1, a truncated distribution that does not say so, a
   description misstating its own sum, a set whose weights exceed the mass they
   divide, and a quoted evidence item that is not a verbatim substring of its
   cited reference.
3. **Export** each profile as a ``references_cache/PHENODIST_<profile_id>.md``
   file, so a dismech entry can cite ``PHENODIST:<profile_id>`` and quote a row
   as an evidence ``snippet:`` — the same line-oriented flat-file mechanism the
   Orphanet, ClinGen, and ICEES structured sources use, and the same direction:
   the entry cites the source, not the other way round.

The generated body is deterministic: the same set always renders the same
bytes, so a curator-quoted snippet keeps matching across regenerations.

Like every other file in ``references_cache/``, these are generated artifacts.
Never hand-write or hand-edit one — regenerate with
``just phenodist-rebuild``.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections.abc import Iterable, Iterator
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from ruamel.yaml import YAML

from dismech.structured_sources.base import ReferenceCacheEntry

PREFIX = "PHENODIST"

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_COLLECTION_DIRS = (
    REPO_ROOT / "kb" / "phenotype_distributions",
    REPO_ROOT / "examples" / "phenotype_distributions",
)
DEFAULT_CACHE_DIR = REPO_ROOT / "references_cache"

#: Document prefixes whose quoted text must be verifiable against the cache.
#: Clinical trials are cited as ``clinicaltrials:NCT12345678`` and cached as
#: ``clinicaltrials_NCT12345678.md`` — a bare ``NCT`` prefix would both miss the
#: real citation form (silently skipping the check) and manufacture a
#: never-existing ``NCT12345678.md`` path for the wrong one.
_VERIFIABLE_PREFIXES = (
    "PMID:",
    "DOI:",
    "clinicaltrials:",
    "ORPHA:",
    "CGGV:",
    "CGDS:",
    "ICEES:",
    "NCIT:",
    "PHENODIST:",
)

#: Phrases marking an issue as "the lookup did not happen" rather than "the
#: term is wrong". `check_terms` draws that distinction by severity too, but
#: severity alone is not enough for a caller: WARNING also covers findings that
#: *were* checked. Shared as constants because a consumer would otherwise match
#: the message text, and a reword here would silently change its behaviour —
#: `tests/test_phenotype_distributions.py` skips on exactly this, and would
#: quietly go back to failing on a flaky network. A test pins the coupling.
UNPERFORMED_RESOLVE = "could not resolve"
UNPERFORMED_ADAPTER = "could not load"

_yaml = YAML(typ="safe")
_yaml.allow_duplicate_keys = False


# ---------------------------------------------------------------------------
# Loading
# ---------------------------------------------------------------------------


@dataclass
class Collection:
    """One loaded collection, with the path it came from."""

    path: Path
    data: dict[str, Any]

    @property
    def collection_id(self) -> str:
        return str(self.data.get("collection_id", self.path.stem))

    @property
    def profiles(self) -> list[dict[str, Any]]:
        """EHR-derived profiles, for a `ProfileSet` rather than a collection."""
        return list(self.data.get("profiles") or [])


def load_collection(path: Path) -> Collection:
    """Load one collection YAML file."""
    with path.open(encoding="utf-8") as fh:
        data = _yaml.load(fh)
    if not isinstance(data, dict):
        raise ValueError(f"{path}: expected a mapping at the top level")
    # A YAML file that is a mapping but not a collection would otherwise sail
    # through as "a set with 0 profiles" and be reported as checked. Naming
    # the wrong file is the easy mistake here — the schema itself is a mapping,
    # and passing it produces a clean-looking summary that verified nothing.
    if "collection_id" not in data and "profiles" not in data:
        raise ValueError(
            f"{path}: not a phenotype profile set "
            "(no `collection_id` and no `profiles`)"
        )
    return Collection(path=path, data=data)


def discover_collections(
    paths: Iterable[Path] | None = None,
) -> list[Collection]:
    """Load every collection under ``paths`` (default: the standard dirs).

    A path may be a file or a directory; directories are globbed for
    ``*.yaml``. Missing directories are skipped rather than raising, so the
    production directory can be empty while only examples exist.
    """
    search = list(paths) if paths is not None else list(DEFAULT_COLLECTION_DIRS)
    files: list[Path] = []
    for p in search:
        if p.is_dir():
            files.extend(sorted(p.glob("*.yaml")))
        elif p.is_file():
            files.append(p)
        elif p.suffix:
            # A named file that is missing is an error; a missing directory is
            # simply a collection set that does not exist yet.
            raise FileNotFoundError(f"{p}: no such collection file")
    return [load_collection(f) for f in files]


def _is_full_rebuild(paths: list[Path] | None) -> bool:
    """Whether the given paths represent a complete collection set.

    Pruning deletes every cache file not in the current write set, which is
    only correct when the write set is complete. Rebuilding a single collection
    by filename must not delete the others' cache files.
    """
    if not paths:
        return True
    return all(not p.suffix for p in paths)


# ---------------------------------------------------------------------------
# Linting
# ---------------------------------------------------------------------------


@dataclass
class Issue:
    """One lint finding."""

    path: Path
    profile_id: str
    severity: str  # ERROR | WARNING
    message: str

    def format(self) -> str:
        loc = (
            f"{self.path.name}:{self.profile_id}" if self.profile_id else self.path.name
        )
        return f"[{self.severity}] {loc}: {self.message}"


@dataclass
class LintResult:
    """Aggregate lint outcome."""

    issues: list[Issue] = field(default_factory=list)
    n_collections: int = 0
    n_profiles: int = 0

    @property
    def errors(self) -> list[Issue]:
        return [i for i in self.issues if i.severity == "ERROR"]

    @property
    def warnings(self) -> list[Issue]:
        return [i for i in self.issues if i.severity == "WARNING"]


def _cache_path_for(document_id: str, cache_dir: Path) -> Path | None:
    """Cache file a document identifier resolves to, if it is a fetchable one.

    Mirrors the normalization used by ``ReferenceCacheEntry.filename``.
    """
    if not any(document_id.startswith(p) for p in _VERIFIABLE_PREFIXES):
        return None
    stem = (
        document_id.replace(":", "_")
        .replace("/", "_")
        .replace("?", "_")
        .replace("=", "_")
    )
    return cache_dir / f"{stem}.md"


def _check_quoted_items(
    profile: dict[str, Any],
    cache_dir: Path,
) -> list[tuple[str, str]]:
    """Verify quoted evidence items against the reference cache.

    Returns ``(severity, message)`` pairs. A ``DataItem`` that cites a fetchable
    document is a verbatim quote. Without this check a curator could later
    cite ``PHENODIST:<id>`` and quote that rendered row, and
    ``validate-references`` would verify it happily — laundering an unverified
    quote into a validated-looking snippet. So the quote is checked here, at the
    point it enters the system.
    """
    out: list[tuple[str, str]] = []
    for line in profile.get("evidence_lines") or []:
        for item in line.get("has_evidence_items") or []:
            doc = item.get("reported_in") or {}
            doc_id = str(doc.get("id") or "")
            path = _cache_path_for(doc_id, cache_dir)
            if path is None:
                continue
            value = str(item.get("item_value") or "").strip()
            if not value:
                continue
            if not path.exists():
                out.append(
                    (
                        "ERROR",
                        (
                            f"evidence item quotes {doc_id} but {path.name} is "
                            "not cached; run `just fetch-reference` first"
                        ),
                    )
                )
                continue
            body = path.read_text(encoding="utf-8")
            if _normalize_quote(value) not in _normalize_quote(body):
                out.append(
                    (
                        "ERROR",
                        (
                            f"evidence item quoting {doc_id} is not a verbatim "
                            f"substring of {path.name}"
                        ),
                    )
                )
    return out


def _normalize_quote(text: str) -> str:
    """Collapse whitespace so YAML folding does not break substring matching."""
    return " ".join(text.split())


def iter_terms(node: Any, where: str = "set") -> Iterator[tuple[dict, str]]:
    """Yield every ``{term_id, term_label}`` mapping under a node, with a path."""
    if isinstance(node, dict):
        if "term_id" in node and "term_label" in node:
            yield node, where
        for key, value in node.items():
            yield from iter_terms(value, f"{where}.{key}")
    elif isinstance(node, list):
        for i, item in enumerate(node):
            yield from iter_terms(item, f"{where}[{i}]")


def check_terms(
    collections: Iterable[Collection],
    oak_config: Path = REPO_ROOT / "conf" / "oak_config.yaml",
) -> list[Issue]:
    """Verify every ontology term against its authoritative source via OAK.

    This is the check that catches the classic hallucinated-CURIE failure: an
    identifier that exists but names something else entirely, carrying a label
    that was never its own. Without it a distribution can assert any CURIE with
    any label and pass the rest of QC — and since the whole value of this schema
    is machine-readable, ontology-anchored statistics, that gap would undercut
    the point of it.

    Prefixes absent from the OAK config are skipped, matching the behaviour of
    the repo's other term validation.
    """
    from oaklib import get_adapter

    with oak_config.open(encoding="utf-8") as fh:
        adapters_cfg = (_yaml.load(fh) or {}).get("ontology_adapters", {}) or {}

    issues: list[Issue] = []
    adapters: dict[str, Any] = {}
    unloadable: dict[str, str] = {}
    for coll in collections:
        # Walk the whole set, not just its profiles. Lifting `disease` to the
        # set level put the one term every set carries outside the profile
        # loop, which would have left the disease CURIE — the term the citation
        # bridge keys on — as the only unchecked one in the file.
        scopes: list[tuple[str, Any]] = [
            ("", {k: v for k, v in coll.data.items() if k != "profiles"})
        ]
        scopes += [(str(p.get("profile_id", "")), p) for p in coll.profiles]
        for rid, scope in scopes:
            for term, where in iter_terms(scope):
                term_id = str(term.get("term_id") or "")
                label = str(term.get("term_label") or "")
                prefix = term_id.split(":", 1)[0] if ":" in term_id else ""
                spec = adapters_cfg.get(prefix)
                if not spec:
                    continue
                if prefix not in adapters:
                    try:
                        adapters[prefix] = get_adapter(spec)
                    except Exception as exc:  # pragma: no cover - env dependent
                        adapters[prefix] = None
                        # Report once per ontology, not per term. This is the
                        # more consequential failure of the two — every term for
                        # the ontology goes unchecked — so it must not be
                        # quieter than a single failed lookup.
                        unloadable[prefix] = str(exc)
                adapter = adapters[prefix]
                if adapter is None:
                    continue
                try:
                    actual = adapter.label(term_id)
                except Exception as exc:
                    # Network-backed adapters (MONDO resolves via `ols:`) fail
                    # transiently. A lookup that could not be performed is not
                    # evidence that the term is wrong, so it must not read as a
                    # data error.
                    issues.append(
                        Issue(
                            coll.path,
                            rid,
                            "WARNING",
                            f"{where}: {UNPERFORMED_RESOLVE} {term_id} ({exc}); "
                            "term left unverified",
                        )
                    )
                    continue
                if actual is None:
                    issues.append(
                        Issue(
                            coll.path,
                            rid,
                            "ERROR",
                            f"{where}: {term_id} does not exist",
                        )
                    )
                elif actual != label:
                    issues.append(
                        Issue(
                            coll.path,
                            rid,
                            "ERROR",
                            f"{where}: {term_id} is {actual!r}, not {label!r}",
                        )
                    )

    for prefix, exc in sorted(unloadable.items()):
        issues.append(
            Issue(
                # A run-level condition, so attribute it to the adapter config
                # that failed rather than to an arbitrary collection file.
                oak_config,
                "",
                "WARNING",
                (
                    f"{UNPERFORMED_ADAPTER} the {prefix} adapter ({exc}); every "
                    f"{prefix} term in this run was left unchecked"
                ),
            )
        )
    return issues


def lint_profile(
    coll: Collection,
    profile: dict[str, Any],
    cache_dir: Path = DEFAULT_CACHE_DIR,
) -> list[Issue]:
    """Lint one EHR-derived profile.

    Few rules, which is the point of the shape: a profile is a label and
    weighted codes, so most of what can go wrong is a code whose vocabulary is
    unstated or a weight vector that does not say it was truncated.
    """
    pid = str(profile.get("profile_id", ""))
    out: list[Issue] = []

    def err(msg: str) -> None:
        out.append(Issue(coll.path, pid, "ERROR", msg))

    def warn(msg: str) -> None:
        out.append(Issue(coll.path, pid, "WARNING", msg))

    # A share without its denominator is uninterpretable, and silently
    # incomparable with the next set's — the exact hazard the slot is named
    # `profile_weight` rather than `prevalence` to avoid.
    if profile.get("profile_weight") is not None:
        source = profile.get("profile_source") or coll.data.get("profile_source") or {}
        if not source.get("weight_basis"):
            err(
                "profile declares a `profile_weight` but its source declares no "
                "`weight_basis`; a share over a whole corpus and a share "
                "over one disease arm can differ by orders of magnitude and "
                "look identical"
            )

    for dist in profile.get("code_distributions") or []:
        codes = dist.get("weighted_codes") or []
        domain = dist.get("clinical_domain")
        total = sum(
            c["code_weight"]
            for c in codes
            if isinstance(c.get("code_weight"), (int, float))
        )
        # Weights that do not sum to 1 are fine for a top-N export and wrong for
        # a complete one, and only `truncated` tells the two apart.
        if total > 1.001:
            err(
                f"{domain} distribution weights sum to {total:.3f}, above 1.0; "
                "a categorical distribution cannot carry more than its own mass"
            )
        # A description that states its own sum must state it correctly. This
        # number has drifted twice by hand — a code was added and the sentence
        # was not — and unlike a prose keyword it is derivable from the same
        # file, so the claim can simply be checked.
        #
        # The switch is "sum to <number>", tilde optional. It was `~` only,
        # which made the opt-in the tilde rather than the claim: writing "the
        # weights sum to 0.73" bought silence, and silence is indistinguishable
        # from a passing check.
        #
        # A decimal point is required, and that is the second half of the same
        # decision. It keeps "do not sum to 1" and "rather than 1" — both live
        # phrasings — from being read as claims, and it drops integer claims,
        # which under the half-a-unit rule would have carried a useless +/- 0.5
        # tolerance. A distribution asserting it sums to 1 is already covered by
        # the truncation warning below.
        #
        # Known and deliberate: the exclusion is by decimal point, not by
        # negation, so "do not sum to 1.0" would be read as a claim and flagged.
        # No description in the tree phrases it that way, and the failure is a
        # loud false positive a curator resolves by rewording — the direction
        # this check chose over silence. Detecting negation in prose is the kind
        # of cleverness that fails quietly, which is the worse trade here.
        #
        # `[\d.]+` would swallow a sentence-final period and hand `float()` a
        # string like "0.73.", turning a lint finding into a traceback out of a
        # `just qc` gate — a worse failure than the drift being guarded against.
        claimed = re.search(r"sum to ~?(\d+\.\d+)", dist.get("description") or "")
        if claimed:
            text = claimed.group(1)
            # Judge the claim at the precision it was written to. A fixed
            # tolerance cannot: 0.005 is *exactly* the largest legitimate
            # rounding error for a two-decimal claim, so `>= 0.005` rejects a
            # correct round-half-up (0.7350 written "~0.74") — and the same
            # fixed number is far too strict for a one-decimal claim, where
            # "~0.7" against 0.7269 is right and would have been flagged.
            # Half a unit in the last written place is the rule that makes both
            # cases come out correctly. The epsilon is load-bearing rather than
            # defensive: 0.74 - 0.735 evaluates to 0.005000000000000004, so
            # relaxing `>=` to `>` alone would still have rejected the halfway
            # case.
            decimals = len(text.partition(".")[2])
            tolerance = 0.5 * 10**-decimals + 1e-9
            if abs(float(text) - total) > tolerance:
                # Quote the number as written, without re-adding the `~`: the
                # tilde is optional in the claim, so putting it back would make
                # the diagnostic misquote the file. A message about prose that
                # says what the file does not should not be one.
                err(
                    f"{domain} distribution description says the weights sum to "
                    f"{text}, but they sum to {total:.5f}"
                )

        if total < 0.999 and not dist.get("truncated"):
            warn(
                f"{domain} distribution weights sum to {total:.3f} but the "
                "distribution is not marked `truncated: true`; a top-N export "
                "should say so rather than look like a distribution that lost mass"
            )
        seen: set[tuple[str, Any]] = set()
        for c in codes:
            key = (str(c.get("code")), c.get("value_qualifier"))
            if key in seen:
                err(
                    f"{domain} distribution lists code {c.get('code')!r} twice "
                    "with the same value qualifier"
                )
            seen.add(key)

    for severity, message in _check_quoted_items(profile, cache_dir):
        out.append(Issue(coll.path, pid, severity, message))

    return out


def lint_collections(
    collections: Iterable[Collection],
    cache_dir: Path = DEFAULT_CACHE_DIR,
) -> LintResult:
    """Lint a set of collections, including cross-collection id uniqueness."""
    collections = list(collections)
    result = LintResult(n_collections=len(collections))

    seen: dict[str, Path] = {}
    for coll in collections:
        # The disease is declared once for the set, not per profile: a dismech
        # entry associates with the whole set, and any nesting between cohorts
        # is MONDO's own subclass tree.
        if not (coll.data.get("disease") or {}).get("disease_term"):
            result.issues.append(
                Issue(
                    coll.path,
                    "",
                    "WARNING",
                    "profile set declares no `disease.disease_term`; the MONDO "
                    "term is what associates it with a dismech entry",
                )
            )
        weights = [
            p["profile_weight"]
            for p in coll.profiles
            if isinstance(p.get("profile_weight"), (int, float))
        ]
        # Only an upper bound is meaningful: real exports are top-N, so shares
        # falling short of 1 is the normal case, but exceeding it is not.
        if weights and sum(weights) > 1.001:
            result.issues.append(
                Issue(
                    coll.path,
                    "",
                    "ERROR",
                    f"profile weights sum to {sum(weights):.3f}, above 1.0; "
                    "weights divide one fit's mass and cannot total more than it",
                )
            )
        for profile in coll.profiles:
            result.n_profiles += 1
            pid = str(profile.get("profile_id", ""))
            if not pid:
                result.issues.append(
                    Issue(
                        coll.path,
                        "",
                        "ERROR",
                        "profile has no `profile_id`, so nothing can cite it",
                    )
                )
            elif pid in seen:
                result.issues.append(
                    Issue(
                        coll.path,
                        pid,
                        "ERROR",
                        f"duplicate profile_id, already used in {seen[pid].name}",
                    )
                )
            else:
                seen[pid] = coll.path
            result.issues.extend(lint_profile(coll, profile, cache_dir))

    return result


# ---------------------------------------------------------------------------
# Reference-cache export
# ---------------------------------------------------------------------------


def _fmt(value: Any) -> str:
    """Render a scalar for a table cell, deterministically.

    Newlines are collapsed and pipes escaped, so a value containing either
    cannot break the row structure that curator-quoted snippets rely on. The
    escaping is deterministic, so a snippet quoted from a generated file keeps
    matching — but prefer values without pipes, since the quote a curator
    copies is the escaped form.
    """
    if value is None:
        return "-"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, float):
        # `repr` gives the shortest string that round-trips, so a tight alpha or
        # a small p-value is not silently truncated in the row curators cite.
        # Integral floats render without the trailing `.0`.
        if value.is_integer() and abs(value) < 1e16:
            return str(int(value))
        return repr(value)
    return str(value).replace("\n", " ").replace("|", r"\|").strip()


def _row(cells: Iterable[Any]) -> str:
    return "| " + " | ".join(_fmt(c) for c in cells) + " |"


def _term(descriptor: Any) -> str:
    """Render a term reference as ``ID Label``."""
    if not isinstance(descriptor, dict):
        return "-"
    tid = descriptor.get("term_id")
    label = descriptor.get("term_label")
    if tid and label:
        return f"{tid} {label}"
    return _fmt(tid or label)


def render_profile_body(coll: Collection, profile: dict[str, Any]) -> str:
    """Render the deterministic markdown body for one profile's cache file.

    Stable bytes, line-oriented, so a curator-quoted snippet keeps matching
    across regenerations.
    """
    lines: list[str] = []
    src = profile.get("profile_source") or coll.data.get("profile_source") or {}
    # The disease is declared once for the set, but every cache file has to
    # stand alone: a curator reads one file and must see which disease it is
    # about without opening the set it came from.
    disease = coll.data.get("disease") or {}

    lines.append("## Profile")
    lines.append("")
    lines.append("| FIELD | VALUE |")
    lines.append(_row(["Label", profile.get("profile_label")]))
    if profile.get("profile_id"):
        lines.append(_row(["Profile", profile.get("profile_id")]))
    if disease:
        lines.append(
            _row(
                [
                    "Disease",
                    (
                        f"{_fmt(disease.get('disease_name'))} "
                        f"({_term(disease.get('disease_term'))})"
                    ),
                ]
            )
        )
    if profile.get("profile_weight") is not None:
        lines.append(_row(["Profile weight", profile.get("profile_weight")]))
    if profile.get("description"):
        lines.append(_row(["Description", profile.get("description")]))
    lines.append("")

    for dist in profile.get("code_distributions") or []:
        lines.append(f"## {_fmt(dist.get('clinical_domain'))} codes")
        lines.append("")
        lines.append("| FIELD | VALUE |")
        lines.append(_row(["Vocabulary", dist.get("code_vocabulary")]))
        if dist.get("code_vocabulary_version"):
            lines.append(
                _row(["Vocabulary version", dist.get("code_vocabulary_version")])
            )
        if dist.get("truncated") is not None:
            lines.append(_row(["Truncated", dist.get("truncated")]))
        lines.append("")
        lines.append("| CODE | LABEL | WEIGHT | QUALIFIER |")
        for c in dist.get("weighted_codes") or []:
            lines.append(
                _row(
                    [
                        c.get("code"),
                        c.get("code_label"),
                        c.get("code_weight"),
                        c.get("value_qualifier") or "-",
                    ]
                )
            )
        lines.append("")

    if src:
        lines.append("## Source")
        lines.append("")
        lines.append("| FIELD | VALUE |")
        for label, key in (
            ("Resource", "resource"),
            ("Method", "method"),
            ("Dataset", "dataset"),
            ("Dataset version", "dataset_version"),
            ("Model version", "model_version"),
            ("Cohort size", "cohort_size"),
            ("URL", "url"),
        ):
            if src.get(key) is not None:
                lines.append(_row([label, src.get(key)]))
        lines.append("")
        if src.get("profile_metadata"):
            lines.append("| PROPERTY | VALUE |")
            for item in src["profile_metadata"]:
                lines.append(
                    _row([item.get("metadata_key"), item.get("metadata_value")])
                )
            lines.append("")

    if profile.get("notes"):
        lines.append("## Notes")
        lines.append("")
        lines.append(_fmt(profile.get("notes")))
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def profile_cache_entry(
    coll: Collection, profile: dict[str, Any]
) -> ReferenceCacheEntry:
    """Build the reference-cache entry for one profile."""
    pid = str(profile["profile_id"])
    disease = (coll.data.get("disease") or {}).get("disease_name") or ""
    title = f"{_fmt(profile.get('profile_label'))} phenotype profile"
    if disease:
        title = f"{title} in {disease}"
    return ReferenceCacheEntry(
        reference_id=f"{PREFIX}:{pid}",
        title=title,
        body=render_profile_body(coll, profile),
        content_type="structured_record",
    )


def write_cache_files(
    collections: Iterable[Collection],
    cache_dir: Path = DEFAULT_CACHE_DIR,
    prune: bool = True,
) -> tuple[list[Path], list[Path]]:
    """Write one cache file per profile, pruning orphans.

    Returns ``(written, pruned)``. Pruning matters because a renamed or deleted
    ``profile_id`` would otherwise leave its old ``PHENODIST_<old_id>.md`` in
    the cache forever, still resolvable and still citable from a kb entry — a
    citation to a profile that no longer exists.
    """
    collections = list(collections)
    illustrative = [
        c.path.name
        for c in collections
        if c.data.get("provenance_tier") == "ILLUSTRATIVE"
    ]
    if illustrative:
        raise ValueError(
            "refusing to render ILLUSTRATIVE collections into the reference "
            f"cache: {', '.join(sorted(illustrative))}. Synthetic numbers must "
            "never become citable."
        )

    written: list[Path] = []
    cache_dir.mkdir(parents=True, exist_ok=True)

    def emit(entry: ReferenceCacheEntry) -> None:
        path = cache_dir / entry.filename()
        text = entry.render()
        if not (path.exists() and path.read_text(encoding="utf-8") == text):
            tmp = path.with_suffix(path.suffix + ".tmp")
            tmp.write_text(text, encoding="utf-8")
            tmp.replace(path)
        written.append(path)

    for coll in collections:
        for profile in coll.profiles:
            emit(profile_cache_entry(coll, profile))

    pruned: list[Path] = []
    if prune:
        keep = {p.name for p in written}
        for stale in sorted(cache_dir.glob(f"{PREFIX}_*.md")):
            if stale.name not in keep:
                stale.unlink()
                pruned.append(stale)
    return written, pruned


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Lint EHR-derived phenotype profile sets and export their profiles "
            "as citable reference-cache files."
        )
    )
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        help="Profile-set files or directories (default: kb/ and examples/ dirs).",
    )
    parser.add_argument(
        "--write-cache",
        action="store_true",
        help="Write references_cache/PHENODIST_<profile_id>.md for each profile.",
    )
    parser.add_argument(
        "--cache-dir",
        type=Path,
        default=DEFAULT_CACHE_DIR,
        help="Cache directory to write into.",
    )
    parser.add_argument(
        "--no-prune",
        action="store_true",
        help=(
            "Never delete orphaned cache files. Pruning is on only for a full "
            "rebuild (no paths, or directory paths); naming individual "
            "collection files never prunes."
        ),
    )
    parser.add_argument(
        "--check-terms",
        action="store_true",
        help=(
            "Also verify every ontology term against OAK. Off by default "
            "because it needs the ontology databases; on in `just qc`."
        ),
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit nonzero on warnings as well as errors.",
    )
    args = parser.parse_args(argv)

    try:
        collections = discover_collections(args.paths or None)
    except (ValueError, FileNotFoundError) as exc:
        # Same treatment as the tier guard below: a mistyped path is a likelier
        # user error than a tier violation, so it should read like every other
        # failure in this CLI rather than as an unhandled traceback.
        print(f"[ERROR] {exc}")
        return 1
    prune = _is_full_rebuild(args.paths) and not args.no_prune
    if not collections:
        print("No phenotype profile sets found.")
        # A full rebuild that finds nothing still has orphans to clear: the case
        # where every curated collection was deleted is exactly when stale
        # citable cache files would otherwise linger.
        if args.write_cache and prune:
            _written, pruned = write_cache_files([], args.cache_dir, prune=True)
            for stale in pruned:
                print(f"Pruned orphaned cache file {stale.name}")
        return 0

    result = lint_collections(collections)
    if args.check_terms:
        result.issues.extend(check_terms(collections))
    for issue in result.issues:
        print(issue.format())

    print(
        f"Checked {result.n_profiles} profile(s) in {result.n_collections} "
        f"profile set(s): {len(result.errors)} error(s), "
        f"{len(result.warnings)} warning(s)."
    )

    if args.write_cache:
        if result.errors:
            print("Refusing to write cache files while errors remain.")
            return 1
        try:
            paths, pruned = write_cache_files(collections, args.cache_dir, prune=prune)
        except ValueError as exc:
            # Report the tier guard the way every other failure in this CLI
            # reads, rather than as an unhandled traceback.
            print(f"[ERROR] {exc}")
            return 1
        print(f"Wrote {len(paths)} cache file(s) to {args.cache_dir}.")
        for stale in pruned:
            print(f"Pruned orphaned cache file {stale.name}")

    if result.errors:
        return 1
    if args.strict and result.warnings:
        return 1
    return 0


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
