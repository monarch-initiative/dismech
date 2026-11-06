"""Loading, slugging, and checking of curation stubs under `stubs/`."""

from __future__ import annotations

import hashlib
import json
import logging
import os
import re
import tempfile
import time
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from dismech.compare.mondo_priority import iter_covered_mondo_ids
from dismech.repo_root import repo_root
from dismech.yaml_io import safe_load

from .obsolescence import proposed_replacement_in

logger = logging.getLogger(__name__)

MONDO_ID_PATTERN = re.compile(r"^MONDO:[0-9]{7}$")

#: MONDO marks retired concepts by prefixing the label. Such a term is not a
#: curation target under any reading, so a stub for one is an error rather than
#: a judgement call. Same backstop the prioritizer config carries, for candidate
#: exports that do not populate `is_obsolete`.
#:
#: This is the *fallback* signal, not the primary one. It only fires when the
#: nominating export captured the label after MONDO prefixed it, which is the
#: unusual case — a stub is normally seeded from a list that predates the
#: retirement, so it keeps the clean label forever and this never matches. Zero
#: of the 1,333 committed stubs match it (dismech#10785). The exact signal is
#: MONDO's own `owl:deprecated` / `IAO:0100001`, written into the stub as
#: `mondo_obsolete` / `mondo_replaced_by` by `just enrich-stubs`; see
#: `dismech.stubs.obsolescence`. The heuristic is kept for stubs enriched before
#: those fields existed, and for anyone working without the MONDO build.
OBSOLETE_LABEL_PATTERN = re.compile(r"^\s*obsolete\b", re.IGNORECASE)

#: A label or synonym has to carry some information before a collision with a KB
#: entry means anything. An acronym -- `AIP`, `Bss`, `CRD` -- collides by
#: coincidence, so short or single-word strings are not compared.
_MIN_INFORMATIVE_CHARS = 8
_MIN_INFORMATIVE_WORDS = 2
_NORMALIZE_STRIP = re.compile(r"[^a-z0-9 ]+")

#: Statuses a stub may carry. Mirrors StubStatusEnum in the schema. There is no
#: CLAIMED: claims live on GitHub as `claim`-labelled issues, because a claim
#: written into YAML only becomes visible when its PR merges. See claims.py.
STATUSES = ("OPEN", "BLOCKED", "DEFERRED")
#: Entry-type decisions. Mirrors StubEntryTypeEnum in the schema.
ENTRY_TYPES = ("UNDECIDED", "DISEASE", "GROUPING", "SUBTYPE", "OUT_OF_SCOPE")
#: Priority bands. Mirrors StubPriorityEnum in the schema.
PRIORITIES = ("HIGH", "NORMAL", "LOW")

_PRIORITY_ORDER = {"HIGH": 0, "NORMAL": 1, "LOW": 2}

# Characters that survive into a filename stem. `kb/disorders/` uses
# Title_Case_With_Underscores and tolerates digits, hyphens, and periods
# (`22q11.2_Deletion_Syndrome.yaml`), so the stub slug uses the same alphabet.
_SLUG_KEEP = re.compile(r"[^A-Za-z0-9.\- ]+")
_SLUG_SPACE = re.compile(r"\s+")


def normalize_label(value: Any) -> str:
    """Casefold and strip punctuation so labels compare across styles.

    `Wilms' tumor` and `Wilms tumor`, `Desanto-Shinawi` and `DeSanto-Shinawi`.
    """
    if not value:
        return ""
    folded = unicodedata.normalize("NFKD", str(value))
    folded = "".join(c for c in folded if not unicodedata.combining(c))
    folded = _NORMALIZE_STRIP.sub(" ", folded.lower())
    return re.sub(r"\s+", " ", folded).strip()


def is_informative_label(normalized: str) -> bool:
    """Whether a normalized label is specific enough to match on."""
    return (
        len(normalized) >= _MIN_INFORMATIVE_CHARS
        and len(normalized.split()) >= _MIN_INFORMATIVE_WORDS
    )


def entry_label_strings(data: dict[str, Any]) -> list[str]:
    """Every name a KB entry answers to: name, display name, term label, synonyms."""
    disease_term = data.get("disease_term") or {}
    labels: list[Any] = [
        data.get("name"),
        data.get("display_name"),
        (disease_term.get("term") or {}).get("label"),
        disease_term.get("preferred_term"),
    ]
    for synonym in data.get("synonyms") or []:
        labels.append(
            synonym if isinstance(synonym, str) else (synonym or {}).get("name")
        )
    return [str(label) for label in labels if label]


def default_repo_root() -> Path:
    """The checkout the command runs in, not the one this file was loaded from (#15109)."""
    return repo_root()


def default_stub_dir() -> Path:
    return default_repo_root() / "stubs"


def default_kb_dirs() -> list[Path]:
    root = default_repo_root()
    return [root / "kb" / "disorders", root / "kb" / "groupings"]


def slugify_label(label: str) -> str:
    """Turn a MONDO label into a `kb/disorders`-style filename stem.

    `alcohol sensitivity, acute` -> `Alcohol_Sensitivity_Acute`. Accents are
    folded rather than dropped so `Behçet` becomes `Behcet`, not `Behet`.

    Deliberately **not** `dismech.export.utils.slugify`, in the same way
    `hpoa_export.slugify` is not. That one turns an entry `name` -- already
    written in the repository's Title_Case style -- into a page filename, and
    must stay byte-identical across the renderer and every exporter or the
    browser index dead-links. This one turns an *ontology label*, which is
    lowercase and carries commas and accents, into a proposed entry name. They
    take different inputs and answer different questions; sharing them would
    couple the page build to MONDO's labelling conventions.
    """
    folded = unicodedata.normalize("NFKD", label)
    folded = "".join(ch for ch in folded if not unicodedata.combining(ch))
    cleaned = _SLUG_KEEP.sub(" ", folded)
    cleaned = _SLUG_SPACE.sub(" ", cleaned).strip()
    if not cleaned:
        return ""
    words = []
    for word in cleaned.split(" "):
        # Leave words that already carry internal capitals or digits alone
        # (`22q11.2`, `IgG4`, `BRAF`); title-case the rest.
        words.append(
            word if any(c.isupper() or c.isdigit() for c in word) else word.capitalize()
        )
    return "_".join(words)


def stub_filename(label: str, mondo_id: str) -> str:
    """Filename for a stub. Falls back to the MONDO ID when the label won't slug."""
    slug = slugify_label(label)
    if not slug:
        return f"{mondo_id.replace(':', '_')}.yaml"
    return f"{slug}.yaml"


@dataclass
class Stub:
    """One stub file, as loaded from disk."""

    path: Path
    data: dict[str, Any]

    @property
    def mondo_id(self) -> str:
        return str(self.data.get("mondo_id") or "")

    @property
    def label(self) -> str:
        return str(self.data.get("label") or "")

    @property
    def status(self) -> str:
        return str(self.data.get("status") or "OPEN")

    @property
    def entry_type(self) -> str:
        return str(self.data.get("entry_type") or "UNDECIDED")

    @property
    def priority(self) -> str:
        return str(self.data.get("priority") or "NORMAL")

    @property
    def mondo_obsolete(self) -> bool:
        """Whether MONDO has retired this stub's term.

        Written by `just enrich-stubs` from the ontology's own `owl:deprecated`
        flag, so the check that reads it needs no ontology. Omitted rather than
        written false on a live term — stating the default on 1,300-odd files
        would be a line of noise in each — so absence means "not flagged", and
        `check_stubs` keeps the label heuristic as its backstop.
        """
        return bool(self.data.get("mondo_obsolete"))

    @property
    def mondo_replaced_by(self) -> str:
        """The live term that absorbed this one (`IAO:0100001`), if any."""
        return str(self.data.get("mondo_replaced_by") or "")

    @property
    def mondo_obsoletion_candidate(self) -> str:
        """MONDO's note about a retirement it has decided on but not yet made.

        Free text, verbatim from MONDO: the scheduled-merge comment plus its
        tracker issue. This fires months before `mondo_obsolete` does, because
        the deprecation flag only appears in a release built after the merge
        lands.
        """
        return str(self.data.get("mondo_obsoletion_candidate") or "")

    @property
    def mondo_successor(self) -> str:
        """The MONDO term this stub's disease has moved, or is moving, to.

        `mondo_replaced_by` once the merge has happened; before that, the
        survivor MONDO's scheduled-merge note names. Empty for a live term with
        no retirement decision, and for one retired or scheduled with no
        replacement.
        """
        if self.mondo_obsolete and self.mondo_replaced_by:
            return self.mondo_replaced_by
        if self.mondo_obsoletion_candidate:
            return proposed_replacement_in(self.mondo_obsoletion_candidate) or ""
        return ""

    @property
    def sort_key(self) -> tuple[int, str]:
        """Priority band, then a stable hash of the MONDO ID.

        Deliberately not alphabetical. Alphabetical order clusters the queue by
        naming convention -- five `10q..` microdeletion syndromes in a row --
        which makes the head of the list look like a recommendation for a
        family of diseases when it is an artifact of sorting. Hashing gives a
        spread that is arbitrary (as it should be, since priority within a band
        is genuinely unranked) but reproducible across runs and machines.
        """
        digest = hashlib.sha256(self.mondo_id.encode("utf-8")).hexdigest()
        return (_PRIORITY_ORDER.get(self.priority, 1), digest)

    @property
    def alpha_sort_key(self) -> tuple[int, str]:
        return (_PRIORITY_ORDER.get(self.priority, 1), self.label.casefold())


@dataclass
class StubIssue:
    """A problem found by :func:`check_stubs`.

    `severity` separates a malformed file from a stale one, and only the first
    gates.

    An `error` means the file itself is broken — unparseable, a malformed MONDO
    ID, a duplicate of another stub, a bad enum value. Only the person who wrote
    that stub sees it, and it is cheap for them to fix.

    An `advisory` means the queue has drifted: the disease got curated by
    somebody else, the MONDO term was retired, a similarly named entry already
    exists. **These must never gate.** Stubs are informative, not curated
    content — a curation PR merging on `main` would otherwise turn every open
    stub PR red through no fault of its author, and curators would spend their
    time servicing a bookkeeping message. Overlap and lag are expected; a
    periodic tidy-up pass (`dismech-stubs tidy`) clears them.
    """

    path: Path | None
    kind: str
    message: str
    severity: str = "error"
    #: The MONDO term the stub's disease has moved or is moving to, on the
    #: findings whose remedy is to repoint or fold the stub there. `next` shows
    #: it beside the kind (`obsolete_term_replaced -> MONDO:NNNNNNN`) and in
    #: `--json`, so a curator sees the live ID before claiming the dead one.
    successor: str | None = None

    def format(self) -> str:
        where = self.path.name if self.path else "stubs/"
        prefix = "" if self.severity == "error" else f"[{self.severity}] "
        return f"{prefix}{where}: {self.kind}: {self.message}"


@dataclass
class CoverageIndex:
    """MONDO IDs already accounted for by a committed KB entry."""

    ids: dict[str, str] = field(default_factory=dict)
    #: Normalized label/synonym -> "disorders/Foo.yaml". Catches a disease the KB
    #: curated under a *different* MONDO ID, which the ID index cannot see.
    labels: dict[str, str] = field(default_factory=dict)

    def covered_by(self, mondo_id: str) -> str | None:
        return self.ids.get(mondo_id)

    def entry_labelled(self, label: str) -> str | None:
        normalized = normalize_label(label)
        if not is_informative_label(normalized):
            return None
        return self.labels.get(normalized)


def _grouping_mondo_ids(data: dict[str, Any]) -> list[str]:
    """MONDO IDs a `kb/groupings/` entry claims.

    Groupings have no `disease_term`; they carry the concept in
    `mappings.mondo_mappings`. `mondo_priority.build_coverage_index` never reads
    this directory, which is why concepts already modelled as groupings kept
    reappearing in the priority queue (dismech#8768).

    Every mapping predicate counts here, unlike `iter_covered_mondo_ids`, which
    honours only exact/narrow. The predicates say different things in the two
    places. On a disease entry a broad/close/related mapping is a cross-reference
    to some *other* concept, so it must not retire that concept. On a grouping it
    records how the grouping sits against the MONDO term it was built around --
    and every one of them in the KB today names a grouping-level concept
    (`ciliopathy`, `RASopathy`, `inborn errors of metabolism`, `microcephaly`),
    which is precisely what should not be sitting in a disorder curation queue.

    This retires the concept from the queue; it does not assert it has been
    curated as a disease. The check message names the grouping file, so a curator
    who disagrees can see what made the call.
    """
    out = []
    for mapping in (data.get("mappings") or {}).get("mondo_mappings") or []:
        if not isinstance(mapping, dict):
            continue
        term_id = (mapping.get("term") or {}).get("id")
        if term_id:
            out.append(str(term_id))
    return out


#: Version of the per-file records in the persistent coverage cache. Bump it
#: whenever a change to `entry_label_strings`, `normalize_label`,
#: `is_informative_label`, `_grouping_mondo_ids` or `iter_covered_mondo_ids`
#: would derive different ids or labels from the same file: the cache is keyed
#: on file content, so without a bump it keeps serving the old derivation.
COVERAGE_CACHE_VERSION = 1

#: Names the persistent coverage cache file, overriding the default under the
#: checkout's gitignored `tmp/`. Tests point it at `tmp_path`.
COVERAGE_CACHE_ENV = "DISMECH_STUB_COVERAGE_CACHE"

#: A file whose mtime is this close to (or after) the start of the run that
#: recorded it is hashed rather than trusted on `(mtime_ns, size)`: a rewrite
#: landing inside the filesystem's timestamp granularity would otherwise look
#: unchanged. Two seconds covers the coarsest common granularity (FAT). This is
#: git's "racily clean" rule.
_RACY_WINDOW_NS = 2_000_000_000


def default_coverage_cache_path() -> Path:
    override = os.environ.get(COVERAGE_CACHE_ENV)
    if override:
        return Path(override).expanduser()
    return repo_root() / "tmp" / "stub_coverage_index.json"


def _coverage_cache_enabled() -> bool:
    """The `DISMECH_KB_CACHE` switch `dismech.kb_cache` reads, with its values."""
    return os.environ.get("DISMECH_KB_CACHE", "1").strip().lower() not in {
        "0",
        "false",
        "no",
        "off",
    }


def _digest(raw: bytes) -> str:
    return hashlib.blake2b(raw, digest_size=16).hexdigest()


def _derive_record(data: Any, *, is_grouping: bool, filename: str) -> dict:
    """The part of one KB file the coverage index needs, in index order."""
    ids: list[str] = []
    labels: list[str] = []
    if isinstance(data, dict):
        for label in entry_label_strings(data):
            normalized = normalize_label(label)
            if is_informative_label(normalized):
                labels.append(normalized)
        if is_grouping:
            ids = _grouping_mondo_ids(data)
        else:
            ids = [mondo_id for mondo_id, _ in iter_covered_mondo_ids(data, filename)]
    return {"ids": ids, "labels": labels}


def _read_coverage_cache(path: Path, dir_keys: list[str]) -> tuple[list[dict], int]:
    """Per-directory file records and the start time of the run that wrote them.

    Anything unusable -- missing, unparsable, another version, or built for
    a different list of directories -- reads as an empty cache.
    """
    empty: list[dict] = [{} for _ in dir_keys]
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return empty, 0
    if (
        not isinstance(payload, dict)
        or payload.get("version") != COVERAGE_CACHE_VERSION
        or [d.get("path") for d in payload.get("dirs") or []] != dir_keys
    ):
        return empty, 0
    return [d.get("files") or {} for d in payload["dirs"]], int(
        payload.get("started_ns") or 0
    )


def _write_coverage_cache(
    path: Path, dir_keys: list[str], records: list[dict], started_ns: int
) -> None:
    """Replace the cache file atomically, so a concurrent reader sees old or new."""
    payload = {
        "version": COVERAGE_CACHE_VERSION,
        "started_ns": started_ns,
        "dirs": [
            {"path": key, "files": files}
            for key, files in zip(dir_keys, records, strict=True)
        ],
    }
    tmp_name = None
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.NamedTemporaryFile(
            "w",
            encoding="utf-8",
            dir=path.parent,
            prefix=f".{path.name}.",
            suffix=".tmp",
            delete=False,
        ) as handle:
            tmp_name = handle.name
            json.dump(payload, handle, separators=(",", ":"))
        os.replace(tmp_name, path)
    except OSError as exc:
        # The cache is an optimisation: an unwritable location costs the next
        # run a cold build, not a wrong answer.
        logger.warning("could not write stub coverage cache %s: %s", path, exc)
        if tmp_name is not None:
            Path(tmp_name).unlink(missing_ok=True)


def _current_record(
    path: Path, cached: dict | None, *, is_grouping: bool, trust_before_ns: int
) -> tuple[dict, bool]:
    """Return ``(record, changed)`` for one KB file, parsing only when needed.

    Matching `(mtime_ns, size)` is trusted when the mtime is safely older than
    the run that recorded it; otherwise the bytes are hashed, and only a
    changed hash parses the file.
    """
    stat = path.stat()
    if (
        cached is not None
        and cached.get("mtime_ns") == stat.st_mtime_ns
        and cached.get("size") == stat.st_size
        and stat.st_mtime_ns < trust_before_ns
    ):
        return cached, False
    raw = path.read_bytes()
    digest = _digest(raw)
    if cached is not None and cached.get("digest") == digest:
        derived = {"ids": cached.get("ids") or [], "labels": cached.get("labels") or []}
    else:
        derived = _derive_record(
            safe_load(raw.decode("utf-8")), is_grouping=is_grouping, filename=path.name
        )
    record = {
        "mtime_ns": stat.st_mtime_ns,
        "size": stat.st_size,
        "digest": digest,
        **derived,
    }
    return record, True


def build_coverage_index(
    kb_dirs: list[Path] | None = None, *, cache_path: Path | None = None
) -> CoverageIndex:
    """Index every MONDO ID a committed KB entry already covers.

    Reads `kb/disorders/` (root `disease_term`, `has_subtypes[].subtype_term`,
    and exact/narrow `mondo_mappings`) *and* `kb/groupings/` — a stub whose
    concept is already a grouping is finished work, not an open gap.

    Parsing every entry takes about half a minute, and `next`, `check` and
    `coverage` are one-shot processes, so the ids and labels each file
    contributes are kept between runs in a small JSON file (default
    `tmp/stub_coverage_index.json`, or `$DISMECH_STUB_COVERAGE_CACHE`). A file
    is re-parsed only when its content hash changes, and only hashed when its
    `(mtime_ns, size)` changes; deleted files drop out. The persistent cache is
    used for the default KB directories or when ``cache_path`` is given, so an
    ad hoc ``kb_dirs`` never overwrites the real one. ``DISMECH_KB_CACHE=0``
    turns it off, as it does `dismech.kb_cache`.
    """
    dirs = kb_dirs or default_kb_dirs()
    persist = _coverage_cache_enabled() and (cache_path is not None or not kb_dirs)
    store = (cache_path or default_coverage_cache_path()) if persist else None
    dir_keys = [str(kb_dir.resolve()) for kb_dir in dirs]

    started_ns = time.time_ns()
    previous, previous_started_ns = (
        _read_coverage_cache(store, dir_keys) if store else ([{} for _ in dirs], 0)
    )
    trust_before_ns = previous_started_ns - _RACY_WINDOW_NS
    dirty = store is not None and previous_started_ns == 0

    index = CoverageIndex()
    records: list[dict] = []
    for kb_dir, old in zip(dirs, previous, strict=True):
        current: dict[str, dict] = {}
        records.append(current)
        if not kb_dir.is_dir():
            dirty = dirty or bool(old)
            continue
        is_grouping = kb_dir.name == "groupings"
        for path in sorted(kb_dir.glob("*.yaml")):
            if path.name.endswith(".history.yaml"):
                continue
            record, changed = _current_record(
                path,
                old.get(path.name),
                is_grouping=is_grouping,
                trust_before_ns=trust_before_ns,
            )
            current[path.name] = record
            dirty = dirty or changed
            rel = f"{kb_dir.name}/{path.name}"
            for normalized in record["labels"]:
                index.labels.setdefault(normalized, rel)
            for mondo_id in record["ids"]:
                index.ids.setdefault(mondo_id, rel)
        dirty = dirty or bool(old.keys() - current.keys())

    if store is not None and dirty:
        _write_coverage_cache(store, dir_keys, records, started_ns)
    return index


def iter_stub_files(stub_dir: Path | None = None) -> list[Path]:
    directory = stub_dir or default_stub_dir()
    if not directory.is_dir():
        return []
    return sorted(directory.glob("*.yaml"))


def load_stub(path: Path) -> Stub:
    data = safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"Stub at {path} must be a YAML object")
    return Stub(path=path, data=data)


def load_stubs(stub_dir: Path | None = None) -> list[Stub]:
    return [load_stub(path) for path in iter_stub_files(stub_dir)]


def load_stubs_reporting_errors(
    stub_dir: Path | None = None,
) -> tuple[list[Stub], list[StubIssue]]:
    """Load every stub, turning a parse failure into a finding rather than a raise.

    Anyone can add a stub by pull request, so a malformed one is a normal thing
    to encounter. Letting it propagate meant a single bad file aborted the whole
    check with a traceback and said nothing about the other 1,866 -- the least
    useful moment to lose the report.
    """
    stubs: list[Stub] = []
    issues: list[StubIssue] = []
    for path in iter_stub_files(stub_dir):
        try:
            stubs.append(load_stub(path))
        except Exception as exc:
            # YAML parse errors are multi-line; flattened so the report stays
            # one finding per line, with the filename in front of it.
            detail = " ".join(str(exc).split())
            issues.append(
                StubIssue(path, "unparseable", f"{type(exc).__name__}: {detail}")
            )
    return stubs, issues


def _obsolescence_issues(stub: Stub) -> list[StubIssue]:
    """Advisories about MONDO having retired, or decided to retire, the term.

    Three findings, deliberately kept apart because they call for three
    different actions:

    - `obsolete_term` — the term is gone and nothing replaced it. There is
      nothing to curate under it, so this is stale and `tidy` deletes it.
    - `obsolete_term_replaced` — the term was merged into a survivor. The
      *disease* is still uncurated, so deleting the stub would drop real queue
      content; the fix is to repoint `mondo_id` at the replacement. This is why
      the kind is separate rather than a longer `obsolete_term` message: `tidy`
      keys on the kind, and must not sweep these away.
    - `obsoletion_candidate` — MONDO has decided to retire the term but has not
      done so yet. The term is live, so nothing is stale; a curator picking it
      up should know where it is going before writing an entry against it.

    Read from the committed stub fields (`mondo_obsolete`, `mondo_replaced_by`,
    `mondo_obsoletion_candidate`), so this is offline and free. Where they say
    nothing the old label heuristic still runs, as a backstop for a stub the
    enrichment pass has not reached.
    """
    path, mondo_id = stub.path, stub.mondo_id
    if stub.mondo_obsolete:
        if stub.mondo_replaced_by:
            return [
                StubIssue(
                    path,
                    "obsolete_term_replaced",
                    f"{mondo_id} is obsolete; replaced by {stub.mondo_replaced_by} "
                    "— repoint `mondo_id`, do not delete",
                    severity="advisory",
                    successor=stub.mondo_replaced_by,
                )
            ]
        return [
            StubIssue(
                path,
                "obsolete_term",
                f"{mondo_id} is an obsolete MONDO term — stale, tidy up",
                severity="advisory",
            )
        ]

    issues = []
    if stub.mondo_obsoletion_candidate:
        issues.append(
            StubIssue(
                path,
                "obsoletion_candidate",
                f"{mondo_id} is scheduled for obsoletion by MONDO: "
                f"{' '.join(stub.mondo_obsoletion_candidate.split())}",
                severity="advisory",
                successor=stub.mondo_successor or None,
            )
        )
    # Backstop for a stub the enrichment pass has not reached — or reached with
    # a MONDO release built before the retirement landed. Only consulted when
    # the ontology-backed fields say nothing, so it can never contradict them.
    elif OBSOLETE_LABEL_PATTERN.match(stub.label):
        issues.append(
            StubIssue(
                path,
                "obsolete_term",
                f"{mondo_id} is an obsolete MONDO term — stale, tidy up",
                severity="advisory",
            )
        )
    return issues


def check_stubs(
    stub_dir: Path | None = None,
    kb_dirs: list[Path] | None = None,
    coverage: CoverageIndex | None = None,
) -> list[StubIssue]:
    """Check every stub, returning findings of both severities.

    Only `error` findings mean something is wrong: the *file* is broken —
    unparseable, a malformed MONDO ID, a duplicate of another stub, a bad enum
    value. Only the author of that stub sees those, and they are cheap to fix.

    `advisory` findings mean the *queue* drifted — the disease got curated by
    somebody else, MONDO retired the term, a similarly named entry exists under
    a different ID. **These never gate.** Stubs are informative, not curated
    content; gating on drift would make every open stub PR hostage to unrelated
    curation merges. `dismech-stubs tidy` sweeps them instead.

    A single stub can produce more than one advisory, so callers acting on these
    (deleting files, counting stubs) must deduplicate by path.
    """
    stubs, issues = load_stubs_reporting_errors(stub_dir)
    index = coverage if coverage is not None else build_coverage_index(kb_dirs)

    seen_ids: dict[str, Path] = {}
    for stub in stubs:
        path = stub.path
        mondo_id = stub.mondo_id

        if not mondo_id:
            issues.append(StubIssue(path, "missing_mondo_id", "no `mondo_id`"))
            continue
        if not MONDO_ID_PATTERN.match(mondo_id):
            issues.append(
                StubIssue(path, "bad_mondo_id", f"{mondo_id!r} is not MONDO:NNNNNNN")
            )
        if not stub.label:
            issues.append(StubIssue(path, "missing_label", "no `label`"))
        issues.extend(_obsolescence_issues(stub))

        if stub.status not in STATUSES:
            issues.append(
                StubIssue(path, "bad_status", f"{stub.status!r} not in {STATUSES}")
            )
        if stub.entry_type not in ENTRY_TYPES:
            issues.append(
                StubIssue(
                    path, "bad_entry_type", f"{stub.entry_type!r} not in {ENTRY_TYPES}"
                )
            )
        if stub.priority not in PRIORITIES:
            issues.append(
                StubIssue(
                    path, "bad_priority", f"{stub.priority!r} not in {PRIORITIES}"
                )
            )

        previous = seen_ids.get(mondo_id)
        if previous is not None:
            issues.append(
                StubIssue(
                    path,
                    "duplicate_mondo_id",
                    f"{mondo_id} also claimed by {previous.name}",
                )
            )
        else:
            seen_ids[mondo_id] = path

        expected = stub_filename(stub.label, mondo_id)
        # Two MONDO concepts can slug identically, in which case the seeder
        # disambiguates with the ID. Both spellings are legal.
        disambiguated = (
            f"{slugify_label(stub.label)}__{mondo_id.replace(':', '_')}.yaml"
        )
        if stub.label and path.name not in {expected, disambiguated}:
            issues.append(StubIssue(path, "filename_mismatch", f"expected {expected}"))

        covered_by = index.covered_by(mondo_id)
        if covered_by:
            issues.append(
                StubIssue(
                    path,
                    "already_curated",
                    f"{mondo_id} is covered by {covered_by} — stale, tidy up",
                    severity="advisory",
                )
            )
            continue

        # Same name, different MONDO ID. The ID index cannot see this, and the
        # answer genuinely varies: `Friedreich ataxia 1` (MONDO:0100340) against
        # a curated `Friedreich_Ataxia` may want deleting or may want a mapping
        # added to the existing entry, while `Leber congenital amaurosis type 1`
        # against a gene-first `GUCY2D-Related_Retinopathy` is arguably a
        # distinct entry. A person has to decide, so this is advisory.
        candidates = [stub.label, *(stub.data.get("synonyms") or [])]
        for candidate in candidates:
            same_disease = index.entry_labelled(candidate)
            if not same_disease:
                continue
            via = (
                ""
                if normalize_label(candidate) == normalize_label(stub.label)
                else (f" (via synonym {candidate!r})")
            )
            issues.append(
                StubIssue(
                    path,
                    "possible_kb_duplicate",
                    f"{same_disease} answers to this name{via} "
                    "but curates a different MONDO ID",
                    severity="advisory",
                )
            )
            break

    issues.extend(_successor_stub_issues(stubs, seen_ids))
    return issues


def _successor_stub_issues(
    stubs: list[Stub], stub_paths: dict[str, Path]
) -> list[StubIssue]:
    """Advisories for a stub whose MONDO successor already has a stub (#15853).

    MONDO merging term A into term B, with stubs for both, leaves one disease in
    the queue twice. `obsolete_term_replaced` says to repoint A at B, which would
    then be a `duplicate_mondo_id` error; the remedy is to fold A into B's stub
    and delete A. Advisory like the rest of the drift findings, because the merge
    is somebody else's change and the fold needs a person to carry over
    anything hand-written in A.
    """
    issues = []
    for stub in stubs:
        successor = stub.mondo_successor
        if not successor or successor == stub.mondo_id:
            continue
        other = stub_paths.get(successor)
        if other is None or other == stub.path:
            continue
        moved = (
            "was merged into" if stub.mondo_obsolete else "is scheduled to merge into"
        )
        issues.append(
            StubIssue(
                stub.path,
                "successor_already_stubbed",
                f"{stub.mondo_id} {moved} {successor}, which already has its own "
                f"stub {other.name} — fold this stub into that one and delete it, "
                "rather than repointing it",
                severity="advisory",
                successor=successor,
            )
        )
    return issues
