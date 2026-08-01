"""Statistical phenotype distributions: loading, linting, and evidence export.

A *phenotype distribution collection* is a YAML file conforming to
``src/dismech/schema/phenotype_distribution.yaml``. Each collection holds
records, and each record is one estimand for one phenotype in one disease in
one stratum.

This module does three things:

1. **Load** collections from ``kb/phenotype_distributions/`` (and the worked
   examples under ``examples/phenotype_distributions/``).
2. **Lint** them for the consistency the LinkML schema cannot express —
   duplicate record ids, an ``evidence_reference`` that disagrees with its
   record id, a ``target_entry`` that does not resolve to a real kb file, a
   matrix whose value count contradicts its declared dimensions, an interval
   that does not bracket its point estimate, an identity attestation that
   contradicts itself, and a proportion banded into an HPO frequency class its
   own point estimate does not support.
3. **Export** each record as a ``references_cache/PHENODIST_<record_id>.md``
   file, so a dismech entry can cite ``PHENODIST:<record_id>`` and quote a row
   as an evidence ``snippet:`` — the same line-oriented flat-file mechanism the
   Orphanet, ClinGen, and ICEES structured sources use.

The generated body is deterministic: the same collection always renders the
same bytes, so a curator-quoted snippet keeps matching across regenerations.

Like every other file in ``references_cache/``, these are generated artifacts.
Never hand-write or hand-edit one — regenerate with
``just phenodist-rebuild``.
"""

from __future__ import annotations

import argparse
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

#: ``target_kind`` -> directory holding the target entries.
_TARGET_DIRS = {
    "DISEASE": REPO_ROOT / "kb" / "disorders",
    "MODULE": REPO_ROOT / "kb" / "modules",
    "GROUPING": REPO_ROOT / "kb" / "groupings",
    "COMORBIDITY": REPO_ROOT / "kb" / "comorbidities",
}

#: HPO frequency bands as half-open proportion intervals ``[lower, upper)``.
#: OBLIGATE is the closed point 1.0 and is handled separately.
_FREQUENCY_BANDS = {
    "VERY_RARE": (0.0, 0.05),
    "OCCASIONAL": (0.05, 0.30),
    "FREQUENT": (0.30, 0.80),
    "VERY_FREQUENT": (0.80, 1.0),
}

#: Estimands whose values are proportions, and so can imply a frequency band.
_PROPORTION_MEASURES = {"PHENOTYPE_PROPORTION", "PENETRANCE"}

#: Estimands that may describe a whole latent mixture rather than one phenotype.
_MIXTURE_MEASURES = {"LATENT_PHENOTYPE_WEIGHT", "CODE_PROBABILITY"}

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
    def records(self) -> list[dict[str, Any]]:
        return list(self.data.get("distributions") or [])


def load_collection(path: Path) -> Collection:
    """Load one collection YAML file."""
    with path.open(encoding="utf-8") as fh:
        data = _yaml.load(fh)
    if not isinstance(data, dict):
        raise ValueError(f"{path}: expected a mapping at the top level")
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
            raise FileNotFoundError(p)
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


def iter_records(
    collections: Iterable[Collection],
) -> Iterator[tuple[Collection, dict[str, Any]]]:
    """Yield ``(collection, record)`` for every record in every collection."""
    for coll in collections:
        for record in coll.records:
            yield coll, record


# ---------------------------------------------------------------------------
# Linting
# ---------------------------------------------------------------------------


@dataclass
class Issue:
    """One lint finding."""

    path: Path
    record_id: str
    severity: str  # ERROR | WARNING
    message: str

    def format(self) -> str:
        loc = f"{self.path.name}:{self.record_id}" if self.record_id else self.path.name
        return f"[{self.severity}] {loc}: {self.message}"


@dataclass
class LintResult:
    """Aggregate lint outcome."""

    issues: list[Issue] = field(default_factory=list)
    n_collections: int = 0
    n_records: int = 0

    @property
    def errors(self) -> list[Issue]:
        return [i for i in self.issues if i.severity == "ERROR"]

    @property
    def warnings(self) -> list[Issue]:
        return [i for i in self.issues if i.severity == "WARNING"]


def _entry_names(directory: Path) -> set[str]:
    """File stems of the YAML entries in a kb directory."""
    if not directory.is_dir():
        return set()
    return {
        p.stem
        for p in directory.glob("*.yaml")
        if not p.name.endswith(".history.yaml")
    }


def _check_matrix(param: dict[str, Any]) -> str | None:
    """Return an error message if a matrix parameter is self-inconsistent."""
    matrix = param.get("matrix_value")
    if not isinstance(matrix, dict):
        return None
    rows = matrix.get("n_rows")
    cols = matrix.get("n_columns")
    values = matrix.get("values") or []
    if isinstance(rows, int) and isinstance(cols, int):
        expected = rows * cols
        if len(values) != expected:
            return (
                f"matrix parameter {param.get('parameter_name')!r} declares "
                f"{rows}x{cols} = {expected} entries but lists {len(values)}"
            )
    for axis, labels, n in (
        ("row_labels", matrix.get("row_labels"), rows),
        ("column_labels", matrix.get("column_labels"), cols),
    ):
        if labels and isinstance(n, int) and len(labels) != n:
            return (
                f"matrix parameter {param.get('parameter_name')!r} has "
                f"{len(labels)} {axis} for {n} entries on that axis"
            )
    return None


def _check_interval(
    summary: dict[str, Any],
) -> str | None:
    """Return an error message if an interval fails to bracket its estimate."""
    lower = summary.get("interval_lower")
    upper = summary.get("interval_upper")
    point = summary.get("point_estimate")
    # Degrade to a lint finding rather than a traceback if YAML hands us a
    # string where a number belongs.
    for name, val in (("interval_lower", lower), ("interval_upper", upper), ("point_estimate", point)):
        if val is not None and not isinstance(val, (int, float)):
            return f"{name} is {val!r}, which is not a number"
    if lower is not None and upper is not None and lower > upper:
        return f"interval bounds are inverted ({lower} > {upper})"
    if point is None:
        return None
    if lower is not None and point < lower:
        return f"point estimate {point} lies below the interval lower bound {lower}"
    if upper is not None and point > upper:
        return f"point estimate {point} lies above the interval upper bound {upper}"
    return None


def _implied_band(value: float) -> str | None:
    """HPO frequency band a proportion falls in, or None if it has none.

    A point estimate of exactly zero has no band: "never observed in this
    cohort" is a different claim from VERY_RARE's "<5%", and collapsing the two
    would let a null observation assert a frequency.
    """
    if value < 0.0 or value > 1.0:
        return None
    if value == 0.0:
        return None
    if value >= 1.0:
        return "OBLIGATE"
    for band, (lo, hi) in _FREQUENCY_BANDS.items():
        if lo <= value < hi:
            return band
    return None


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
    record: dict[str, Any],
    cache_dir: Path,
) -> list[tuple[str, str]]:
    """Verify quoted evidence items against the reference cache.

    Returns ``(severity, message)`` pairs. A ``DataItem`` that cites a fetchable
    document is a verbatim quote, and ``render_body`` writes it into the
    generated PHENODIST cache file. Without this check a curator could later
    cite ``PHENODIST:<id>`` and quote that rendered row, and
    ``validate-references`` would verify it happily — laundering an unverified
    quote into a validated-looking snippet. So the quote is checked here, at the
    point it enters the system.
    """
    out: list[tuple[str, str]] = []
    for line in record.get("evidence_lines") or []:
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


def iter_terms(node: Any, where: str = "record") -> Iterator[tuple[dict, str]]:
    """Yield every ``{term_id, term_label}`` mapping in a record, with a path."""
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
        for record in coll.records:
            rid = str(record.get("record_id", ""))
            for term, where in iter_terms(record):
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
                            f"{where}: could not resolve {term_id} ({exc}); "
                            "term left unverified",
                        )
                    )
                    continue
                if actual is None:
                    issues.append(
                        Issue(coll.path, rid, "ERROR", f"{where}: {term_id} does not exist")
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
                    f"could not load the {prefix} adapter ({exc}); every "
                    f"{prefix} term in this run was left unchecked"
                ),
            )
        )
    return issues


def lint_record(
    coll: Collection,
    record: dict[str, Any],
    known_entries: dict[str, set[str]],
    cache_dir: Path = DEFAULT_CACHE_DIR,
) -> list[Issue]:
    """Lint one record. Returns the issues found."""
    rid = str(record.get("record_id", ""))
    out: list[Issue] = []

    def err(msg: str) -> None:
        out.append(Issue(coll.path, rid, "ERROR", msg))

    def warn(msg: str) -> None:
        out.append(Issue(coll.path, rid, "WARNING", msg))

    if not record.get("phenotype") and not record.get("latent_phenotype"):
        # A record over a whole latent mixture legitimately has no single
        # subject phenotype — but only if the model that defines the
        # components is declared, otherwise the component indices mean nothing.
        if record.get("measure_type") in _MIXTURE_MEASURES:
            if not coll.data.get("model"):
                err(
                    "record describes a latent mixture but its collection "
                    "declares no `model`, so the components are uninterpretable"
                )
        else:
            err("record has neither a `phenotype` nor a `latent_phenotype`")

    dist = record.get("distribution") or {}

    for param in dist.get("parameters") or []:
        msg = _check_matrix(param)
        if msg:
            err(msg)

    summary = dist.get("summary") or {}
    msg = _check_interval(summary)
    if msg:
        err(msg)
    if (
        summary.get("interval_lower") is not None
        or summary.get("interval_upper") is not None
    ) and not summary.get("interval_type"):
        warn(
            "summary reports an interval without an `interval_type`; a "
            "confidence and a credible interval are not interchangeable"
        )

    # Bins that claim to partition the cohort should roughly sum to 1.
    bins = dist.get("bins") or []
    proportions = [b.get("proportion") for b in bins if b.get("proportion") is not None]
    if len(proportions) == len(bins) and len(bins) > 1:
        total = sum(proportions)
        if abs(total - 1.0) > 0.02 and dist.get("family") != "CATEGORICAL":
            warn(
                f"bin proportions sum to {total:.3f}, not 1.0; if the bins are a "
                "partial tabulation rather than a partition, say so in `notes`"
            )

    # Identity attestations must not contradict themselves.
    for att, where in _iter_attestations(record):
        rows = att.get("row_count")
        persons = att.get("unique_person_count")
        one_per = att.get("one_row_per_person")
        if one_per and rows is not None and persons is not None and rows != persons:
            err(
                f"{where}: identity attestation claims one row per person but "
                f"reports {rows} rows for {persons} persons"
            )
        if persons is not None and rows is not None and persons > rows:
            err(f"{where}: attestation reports more persons ({persons}) than rows ({rows})")

    # A proportion's implied frequency band must match its own point estimate.
    band = record.get("implied_frequency_class")
    if band:
        if record.get("measure_type") not in _PROPORTION_MEASURES:
            warn(
                "`implied_frequency_class` is set on a record whose measure_type "
                f"is {record.get('measure_type')!r}; frequency bands describe "
                "proportions"
            )
        point = summary.get("point_estimate")
        if isinstance(point, (int, float)):
            expected = _implied_band(float(point))
            if expected and expected != band:
                err(
                    f"implied_frequency_class is {band} but the point estimate "
                    f"{point} falls in the {expected} band"
                )
        if not record.get("implied_frequency_basis"):
            warn("`implied_frequency_class` is set without an `implied_frequency_basis`")

    for binding in record.get("dismech_bindings") or []:
        ref = binding.get("evidence_reference")
        if ref and ref != f"{PREFIX}:{rid}":
            err(
                f"binding evidence_reference {ref!r} does not match this record; "
                f"expected {PREFIX}:{rid}"
            )
        kind = binding.get("target_kind")
        entry = binding.get("target_entry")
        if kind and entry:
            names = known_entries.get(kind, set())
            if names and entry not in names:
                err(
                    f"binding targets {kind} entry {entry!r}, which does not "
                    f"resolve to a file in {_TARGET_DIRS[kind].relative_to(REPO_ROOT)}"
                )
        if binding.get("import_status") in {"REJECTED", "DEFERRED", "SUPERSEDED"} and not (
            binding.get("binding_notes")
        ):
            warn(
                f"binding is {binding.get('import_status')} without "
                "`binding_notes` explaining why"
            )

    for severity, message in _check_quoted_items(record, cache_dir):
        out.append(Issue(coll.path, rid, severity, message))

    if not record.get("bias_risks") and not record.get("caveats"):
        warn(
            "record declares neither `bias_risks` nor `caveats`; 'nobody checked' "
            "and 'checked and clean' should not look the same"
        )

    return out


def _iter_attestations(node: Any, where: str = "record") -> Iterator[tuple[dict, str]]:
    """Yield every identity attestation in a record, with a location label."""
    if isinstance(node, dict):
        for key, value in node.items():
            if key == "identity_attestation" and isinstance(value, dict):
                yield value, where
            else:
                yield from _iter_attestations(value, f"{where}.{key}")
    elif isinstance(node, list):
        for i, item in enumerate(node):
            yield from _iter_attestations(item, f"{where}[{i}]")


def lint_collections(
    collections: Iterable[Collection],
    cache_dir: Path = DEFAULT_CACHE_DIR,
) -> LintResult:
    """Lint a set of collections, including cross-collection id uniqueness."""
    collections = list(collections)
    known_entries = {kind: _entry_names(d) for kind, d in _TARGET_DIRS.items()}
    result = LintResult(n_collections=len(collections))

    seen: dict[str, Path] = {}
    for coll, record in iter_records(collections):
        result.n_records += 1
        rid = str(record.get("record_id", ""))
        if rid in seen:
            result.issues.append(
                Issue(
                    coll.path,
                    rid,
                    "ERROR",
                    f"duplicate record_id, already used in {seen[rid].name}; ids "
                    "are cited from kb entries and must be stable and unique",
                )
            )
        else:
            seen[rid] = coll.path
        result.issues.extend(lint_record(coll, record, known_entries, cache_dir))

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


def _interval_text(node: dict[str, Any]) -> str:
    """Render an interval as ``95% CREDIBLE_EQUAL_TAILED 0.84-0.88``."""
    lower = node.get("interval_lower")
    upper = node.get("interval_upper")
    if lower is None and upper is None:
        return "-"
    level = node.get("interval_level")
    kind = node.get("interval_type") or "INTERVAL"
    prefix = f"{level * 100:g}% " if isinstance(level, (int, float)) else ""
    return f"{prefix}{kind} {_fmt(lower)}-{_fmt(upper)}"


def _stratum_text(record: dict[str, Any]) -> str:
    strata = record.get("strata") or []
    if not strata:
        return "whole cohort"
    parts = []
    for s in strata:
        label = s.get("variable_label") or s.get("variable")
        parts.append(f"{label}={_fmt(s.get('stratum_value'))}")
    return "; ".join(parts)


def summary_row(record: dict[str, Any]) -> str:
    """The one-line quotable summary of a record.

    This is the row a curator is most likely to quote as an evidence
    ``snippet:``, so its column order is part of the cache contract and must
    not be reordered.
    """
    dist = record.get("distribution") or {}
    summary = dist.get("summary") or {}
    n = dist.get("n_observations")
    return _row(
        [
            record.get("record_id"),
            record.get("measure_type"),
            dist.get("family"),
            summary.get("point_estimate"),
            _interval_text(summary),
            f"n={n}" if n is not None else "-",
            _stratum_text(record),
        ]
    )


def _phenotype_name(record: dict[str, Any]) -> str:
    pheno = record.get("phenotype") or {}
    if pheno:
        return _fmt(pheno.get("preferred_term") or _term(pheno.get("phenotype_term")))
    latent = record.get("latent_phenotype") or {}
    if latent:
        return _fmt(latent.get("label") or latent.get("component_id"))
    return "-"


def render_body(coll: Collection, record: dict[str, Any]) -> str:
    """Render the deterministic markdown body for one record's cache file."""
    lines: list[str] = []
    dist = record.get("distribution") or {}
    disease = coll.data.get("disease") or {}
    source = coll.data.get("source") or {}

    lines.append("## Distribution summary")
    lines.append("")
    lines.append("| RECORD | MEASURE | FAMILY | ESTIMATE | INTERVAL | N | STRATUM |")
    lines.append(summary_row(record))
    lines.append("")

    lines.append("## Subject")
    lines.append("")
    lines.append("| FIELD | VALUE |")
    lines.append(_row(["Disease", disease.get("disease_name")]))
    lines.append(_row(["Disease term", _term(disease.get("disease_term"))]))
    if disease.get("subtype"):
        lines.append(_row(["Subtype", disease.get("subtype")]))
    lines.append(_row(["Phenotype", _phenotype_name(record)]))
    pheno = record.get("phenotype") or {}
    if pheno.get("phenotype_term"):
        lines.append(_row(["Phenotype term", _term(pheno.get("phenotype_term"))]))
    if pheno.get("loinc_term"):
        lines.append(_row(["LOINC term", _term(pheno.get("loinc_term"))]))
    lines.append(_row(["Measure", record.get("measure_type")]))
    if record.get("measure_description"):
        lines.append(_row(["Measure description", record.get("measure_description")]))
    if record.get("unit"):
        lines.append(_row(["Unit", record.get("unit")]))
    if pheno.get("phenotype_definition"):
        lines.append(_row(["Phenotype definition", pheno.get("phenotype_definition")]))
    lines.append("")

    cohort = record.get("cohort") or {}
    if cohort:
        lines.append("## Cohort")
        lines.append("")
        lines.append("| FIELD | VALUE |")
        for label, key in (
            ("Name", "name"),
            ("Data source type", "data_source_type"),
            ("Data source", "data_source_name"),
            ("Ascertainment", "ascertainment"),
            ("Case definition", "case_definition"),
            ("Geography", "geography"),
            ("Care setting", "care_setting"),
            ("Individuals", "n_individuals"),
            ("Observation start", "observation_start"),
            ("Observation end", "observation_end"),
        ):
            if cohort.get(key) is not None:
                lines.append(_row([label, cohort.get(key)]))
        if cohort.get("person_time") is not None:
            lines.append(
                _row(
                    [
                        "Person-time",
                        f"{_fmt(cohort.get('person_time'))} "
                        f"{_fmt(cohort.get('person_time_unit') or '')}".strip(),
                    ]
                )
            )
        att = cohort.get("identity_attestation") or {}
        if att:
            lines.append(
                _row(
                    [
                        "Identity attestation",
                        (
                            f"rows={_fmt(att.get('row_count'))} "
                            f"persons={_fmt(att.get('unique_person_count'))} "
                            "one_row_per_person="
                            f"{_fmt(att.get('one_row_per_person'))}"
                        ),
                    ]
                )
            )
        lines.append("")

    if record.get("strata"):
        lines.append("## Stratum")
        lines.append("")
        lines.append("| VARIABLE | LABEL | VALUE | LOWER | UPPER | UNIT |")
        for s in record["strata"]:
            lines.append(
                _row(
                    [
                        s.get("variable"),
                        s.get("variable_label"),
                        s.get("stratum_value"),
                        s.get("lower_bound"),
                        s.get("upper_bound"),
                        s.get("unit"),
                    ]
                )
            )
        lines.append("")

    lines.append("## Distribution")
    lines.append("")
    lines.append("| FIELD | VALUE |")
    for label, key in (
        ("Family", "family"),
        ("Parameterization", "parameterization_note"),
        ("Estimation framework", "estimation_framework"),
        ("Observations", "n_observations"),
        ("Events", "n_events"),
        ("Censored", "n_censored"),
        ("Unit", "unit"),
        ("Software", "software"),
    ):
        if dist.get(key) is not None:
            lines.append(_row([label, dist.get(key)]))
    lines.append("")

    summary = dist.get("summary") or {}
    if summary:
        lines.append("## Summary statistics")
        lines.append("")
        lines.append("| STATISTIC | VALUE |")
        for label, key in (
            ("Point estimate", "point_estimate"),
            ("Point estimate type", "point_estimate_type"),
            ("Standard deviation", "standard_deviation"),
            ("Variance", "variance"),
            ("Median", "median"),
            ("IQR lower", "iqr_lower"),
            ("IQR upper", "iqr_upper"),
            ("Minimum observed", "minimum_observed"),
            ("Maximum observed", "maximum_observed"),
            ("Skewness", "skewness"),
        ):
            if summary.get(key) is not None:
                lines.append(_row([label, summary.get(key)]))
        if summary.get("interval_lower") is not None or summary.get("interval_upper") is not None:
            lines.append(_row(["Interval", _interval_text(summary)]))
        lines.append("")

    params = dist.get("parameters") or []
    if params:
        lines.append("## Parameters")
        lines.append("")
        lines.append("| PARAMETER | SYMBOL | VALUE | SE | INTERVAL |")
        for p in params:
            value = p.get("value")
            if value is None and p.get("vector_value"):
                value = "[" + ", ".join(_fmt(v) for v in p["vector_value"]) + "]"
            elif value is None and p.get("matrix_value"):
                m = p["matrix_value"]
                value = (
                    f"{_fmt(m.get('matrix_kind'))} "
                    f"{_fmt(m.get('n_rows'))}x{_fmt(m.get('n_columns'))}"
                )
            lines.append(
                _row(
                    [
                        p.get("parameter_name"),
                        p.get("symbol"),
                        value,
                        p.get("standard_error"),
                        _interval_text(p),
                    ]
                )
            )
        lines.append("")

        for p in params:
            labels = p.get("index_labels")
            if p.get("vector_value") and labels:
                lines.append(f"### Parameter {_fmt(p.get('parameter_name'))} by component")
                lines.append("")
                lines.append("| COMPONENT | VALUE |")
                for label, value in zip(labels, p["vector_value"]):
                    lines.append(_row([label, value]))
                lines.append("")
            matrix = p.get("matrix_value")
            if isinstance(matrix, dict) and matrix.get("values"):
                lines.append(f"### Parameter {_fmt(p.get('parameter_name'))} matrix")
                lines.append("")
                rows = matrix.get("n_rows") or 0
                cols = matrix.get("n_columns") or 0
                row_labels = matrix.get("row_labels") or [f"r{i + 1}" for i in range(rows)]
                col_labels = matrix.get("column_labels") or [f"c{i + 1}" for i in range(cols)]
                lines.append("| | " + " | ".join(_fmt(c) for c in col_labels) + " |")
                values = matrix["values"]
                for i, rlabel in enumerate(row_labels):
                    chunk = values[i * cols : (i + 1) * cols]
                    lines.append(_row([rlabel, *chunk]))
                if matrix.get("reference_component"):
                    lines.append("")
                    lines.append(
                        f"Reference component: {_fmt(matrix['reference_component'])}"
                    )
                lines.append("")

    bins = dist.get("bins") or []
    if bins:
        lines.append("## Bins")
        lines.append("")
        lines.append("| BIN | LOWER | UPPER | COUNT | PROPORTION | SUPPRESSED |")
        for b in bins:
            lines.append(
                _row(
                    [
                        b.get("bin_label"),
                        b.get("lower_bound"),
                        b.get("upper_bound"),
                        b.get("count"),
                        b.get("proportion"),
                        b.get("suppressed"),
                    ]
                )
            )
        lines.append("")

    quantiles = dist.get("quantiles") or []
    if quantiles:
        lines.append("## Quantiles")
        lines.append("")
        lines.append("| QUANTILE | VALUE | UNIT |")
        for q in quantiles:
            lines.append(_row([q.get("quantile"), q.get("value"), q.get("unit")]))
        lines.append("")

    tte = dist.get("time_to_event") or {}
    if tte:
        lines.append("## Time to event")
        lines.append("")
        lines.append("| FIELD | VALUE |")
        for label, key in (
            ("Time unit", "time_unit"),
            ("Median time to event", "median_time_to_event"),
            ("Restricted mean", "restricted_mean"),
            ("Restricted mean horizon", "restricted_mean_horizon"),
            ("Cumulative incidence", "cumulative_incidence"),
        ):
            if tte.get(key) is not None:
                lines.append(_row([label, tte.get(key)]))
        if tte.get("interval_lower") is not None or tte.get("interval_upper") is not None:
            lines.append(_row(["Interval", _interval_text(tte)]))
        lines.append("")
        if tte.get("curve"):
            lines.append("| TIME | AT_RISK | EVENTS | PROBABILITY | CI_LOWER | CI_UPPER |")
            for pt in tte["curve"]:
                lines.append(
                    _row(
                        [
                            pt.get("time"),
                            pt.get("at_risk"),
                            pt.get("events_at_time"),
                            pt.get("probability"),
                            pt.get("interval_lower"),
                            pt.get("interval_upper"),
                        ]
                    )
                )
            lines.append("")

    effects = record.get("covariate_effects") or []
    if effects:
        lines.append("## Covariate effects")
        lines.append("")
        lines.append("| COVARIATE | LEVEL | REFERENCE | COMPONENT | COEFFICIENT | SE | SCALE |")
        for e in effects:
            lines.append(
                _row(
                    [
                        e.get("covariate"),
                        e.get("covariate_level"),
                        e.get("reference_level"),
                        e.get("component"),
                        e.get("coefficient"),
                        e.get("standard_error"),
                        e.get("coefficient_scale"),
                    ]
                )
            )
        lines.append("")

    comparison = record.get("comparison") or {}
    if comparison:
        lines.append("## Comparison")
        lines.append("")
        lines.append("| FIELD | VALUE |")
        ref = comparison.get("reference_group") or {}
        if ref.get("name"):
            lines.append(_row(["Reference group", ref.get("name")]))
        for label, key in (
            ("Effect measure", "effect_measure"),
            ("Effect value", "effect_value"),
            ("P value", "p_value"),
            ("FDR", "fdr"),
        ):
            if comparison.get(key) is not None:
                lines.append(_row([label, comparison.get(key)]))
        if (
            comparison.get("interval_lower") is not None
            or comparison.get("interval_upper") is not None
        ):
            lines.append(_row(["Interval", _interval_text(comparison)]))
        if comparison.get("adjusted_for"):
            lines.append(_row(["Adjusted for", "; ".join(comparison["adjusted_for"])]))
        lines.append("")

    latent = record.get("latent_phenotype") or {}
    if latent:
        lines.append("## Latent phenotype")
        lines.append("")
        lines.append("| FIELD | VALUE |")
        lines.append(_row(["Component", latent.get("component_id")]))
        if latent.get("label"):
            lines.append(_row(["Label", latent.get("label")]))
        for label, key in (
            ("Quality", "component_quality"),
            ("Estimation scope", "estimation_scope"),
            ("Estimation scope size", "estimation_scope_size"),
            ("Corpus prevalence", "corpus_prevalence"),
        ):
            if latent.get(key) is not None:
                lines.append(_row([label, latent.get(key)]))
        if latent.get("mapping_basis"):
            lines.append(_row(["Mapping basis", latent.get("mapping_basis")]))
        for mapped in latent.get("mapped_phenotype_terms") or []:
            lines.append(
                _row(
                    [
                        "Mapped term",
                        (
                            f"{_fmt(mapped.get('preferred_term'))} "
                            f"({_term(mapped.get('term'))})"
                        ),
                    ]
                )
            )
        lines.append("")
        if latent.get("top_features"):
            lines.append("| FEATURE | LABEL | WEIGHT | DOMAIN |")
            for f in latent["top_features"]:
                lines.append(
                    _row(
                        [
                            f.get("feature_id"),
                            f.get("label"),
                            f.get("weight"),
                            f.get("domain_name"),
                        ]
                    )
                )
            lines.append("")

    domains = coll.data.get("domains") or []
    if domains:
        lines.append("## Domain reliability")
        lines.append("")
        lines.append("| DOMAIN | VOCABULARY | FEATURES | BASIS | SCORE |")
        for d in domains:
            rel = d.get("reliability") or {}
            lines.append(
                _row(
                    [
                        d.get("domain_name"),
                        d.get("vocabulary"),
                        d.get("n_features"),
                        rel.get("reliability_basis"),
                        rel.get("reliability_score"),
                    ]
                )
            )
        lines.append("")

    model = coll.data.get("model") or {}
    if model:
        lines.append("## Model")
        lines.append("")
        lines.append("| FIELD | VALUE |")
        for label, key in (
            ("Name", "model_name"),
            ("Family", "model_family"),
            ("Version", "version"),
            ("Components", "n_components"),
            ("Vocabulary size", "vocabulary_size"),
            ("Covariate formula", "covariate_formula"),
            ("Inference", "inference_method"),
            ("Contains patient data", "contains_patient_data"),
            ("Artifact", "artifact_url"),
        ):
            if model.get(key) is not None:
                lines.append(_row([label, model.get(key)]))
        lines.append("")
        if model.get("model_properties"):
            lines.append("| PROPERTY | VALUE |")
            for prop in model["model_properties"]:
                lines.append(_row([prop.get("name"), prop.get("property_value")]))
            lines.append("")

    risks = record.get("bias_risks") or []
    caveats = record.get("caveats") or []
    if risks or caveats:
        lines.append("## Caveats")
        lines.append("")
        if risks:
            lines.append(_row(["Bias risks", "; ".join(risks)]))
            lines.append("")
        for c in caveats:
            lines.append(f"- {_fmt(c)}")
        lines.append("")

    for line_ in record.get("evidence_lines") or []:
        prop = line_.get("target_proposition") or {}
        lines.append("## Evidence line")
        lines.append("")
        lines.append("| FIELD | VALUE |")
        lines.append(_row(["Direction", line_.get("direction_of_evidence_provided")]))
        lines.append(_row(["Strength", line_.get("strength_of_evidence_provided")]))
        if line_.get("evidence_line_type"):
            lines.append(_row(["Type", line_.get("evidence_line_type")]))
        if prop.get("statement_text"):
            lines.append(_row(["Proposition", prop.get("statement_text")]))
        items = line_.get("has_evidence_items") or []
        if items:
            lines.append("")
            lines.append("| ITEM_TYPE | DOCUMENT | DOCUMENT_TYPE | VALUE |")
            for item in items:
                doc = item.get("reported_in") or {}
                lines.append(
                    _row(
                        [
                            item.get("data_type"),
                            doc.get("id"),
                            doc.get("document_type"),
                            item.get("item_value"),
                        ]
                    )
                )
        lines.append("")

    bindings = record.get("dismech_bindings") or []
    if bindings:
        lines.append("## dismech bindings")
        lines.append("")
        lines.append("| KIND | ENTRY | SECTION | PATH | PROPOSED | STATUS |")
        for b in bindings:
            lines.append(
                _row(
                    [
                        b.get("target_kind"),
                        b.get("target_entry"),
                        b.get("target_section"),
                        b.get("target_path"),
                        b.get("proposed_value"),
                        b.get("import_status"),
                    ]
                )
            )
        lines.append("")

    lines.append("## Source")
    lines.append("")
    lines.append("| FIELD | VALUE |")
    lines.append(_row(["Collection", coll.collection_id]))
    for label, key in (
        ("Source", "source_name"),
        ("Source type", "source_type"),
        ("Source version", "source_version"),
        ("URL", "url"),
        ("Retrieved", "retrieved_date"),
        ("License", "license"),
    ):
        if source.get(key) is not None:
            lines.append(_row([label, source.get(key)]))
    for ref in source.get("primary_references") or []:
        lines.append(_row(["Primary reference", ref]))
    lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def cache_entry(coll: Collection, record: dict[str, Any]) -> ReferenceCacheEntry:
    """Build the reference-cache entry for one record."""
    rid = str(record["record_id"])
    disease = (coll.data.get("disease") or {}).get("disease_name") or ""
    subject = _phenotype_name(record)
    if subject == "-":
        # A whole-mixture record has no single phenotype subject.
        subject = "Latent phenotype mixture"
    title = f"{subject} {record.get('measure_type')} distribution"
    if disease:
        title = f"{title} in {disease}"
    return ReferenceCacheEntry(
        reference_id=f"{PREFIX}:{rid}",
        title=title,
        body=render_body(coll, record),
        content_type="structured_record",
    )


def write_cache_files(
    collections: Iterable[Collection],
    cache_dir: Path = DEFAULT_CACHE_DIR,
    prune: bool = True,
) -> tuple[list[Path], list[Path]]:
    """Write one cache file per record, pruning orphans.

    Returns ``(written, pruned)``. Pruning matters because a renamed or deleted
    ``record_id`` would otherwise leave its old ``PHENODIST_<old_id>.md`` in the
    cache forever, still resolvable and still citable from a kb entry — a
    citation to a record that no longer exists.
    """
    collections = list(collections)
    illustrative = [
        c.path.name for c in collections if c.data.get("provenance_tier") == "ILLUSTRATIVE"
    ]
    if illustrative:
        raise ValueError(
            "refusing to render ILLUSTRATIVE collections into the reference "
            f"cache: {', '.join(sorted(illustrative))}. Synthetic numbers must "
            "never become citable."
        )

    written: list[Path] = []
    cache_dir.mkdir(parents=True, exist_ok=True)
    for coll, record in iter_records(collections):
        entry = cache_entry(coll, record)
        path = cache_dir / entry.filename()
        text = entry.render()
        if path.exists() and path.read_text(encoding="utf-8") == text:
            written.append(path)
            continue
        tmp = path.with_suffix(path.suffix + ".tmp")
        tmp.write_text(text, encoding="utf-8")
        tmp.replace(path)
        written.append(path)

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
            "Lint statistical phenotype-distribution collections and export "
            "their records as citable reference-cache files."
        )
    )
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        help="Collection files or directories (default: kb/ and examples/ dirs).",
    )
    parser.add_argument(
        "--write-cache",
        action="store_true",
        help="Write references_cache/PHENODIST_<record_id>.md for each record.",
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

    collections = discover_collections(args.paths or None)
    prune = _is_full_rebuild(args.paths) and not args.no_prune
    if not collections:
        print("No phenotype-distribution collections found.")
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
        f"Checked {result.n_records} record(s) in {result.n_collections} "
        f"collection(s): {len(result.errors)} error(s), "
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
