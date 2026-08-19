"""Loading, slugging, and checking of curation stubs under `stubs/`."""

from __future__ import annotations

import hashlib
import re
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from dismech.compare.mondo_priority import iter_covered_mondo_ids
from dismech.yaml_io import safe_load

MONDO_ID_PATTERN = re.compile(r"^MONDO:[0-9]{7}$")

#: Statuses a stub may carry. Mirrors StubStatusEnum in the schema.
STATUSES = ("OPEN", "CLAIMED", "BLOCKED", "DEFERRED")
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


def default_repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def default_stub_dir() -> Path:
    return default_repo_root() / "stubs"


def default_kb_dirs() -> list[Path]:
    root = default_repo_root()
    return [root / "kb" / "disorders", root / "kb" / "groupings"]


def slugify_label(label: str) -> str:
    """Turn a MONDO label into a `kb/disorders`-style filename stem.

    `alcohol sensitivity, acute` -> `Alcohol_Sensitivity_Acute`. Accents are
    folded rather than dropped so `Behçet` becomes `Behcet`, not `Behet`.
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

    `severity` separates the two kinds of finding. An `error` is a broken
    invariant — the queue is wrong and CI should say so. An `advisory` is a
    judgement call the tool cannot make, most importantly a stub whose name
    matches an existing KB entry curated under a *different* MONDO ID; that may
    be a duplicate to delete or a genuinely distinct concept to keep.
    """

    path: Path | None
    kind: str
    message: str
    severity: str = "error"

    def format(self) -> str:
        where = self.path.name if self.path else "stubs/"
        prefix = "" if self.severity == "error" else f"[{self.severity}] "
        return f"{prefix}{where}: {self.kind}: {self.message}"


@dataclass
class CoverageIndex:
    """MONDO IDs already accounted for by a committed KB entry."""

    ids: dict[str, str] = field(default_factory=dict)
    #: Entry filename stem -> "disorders/Foo.yaml", for the name-collision advisory.
    stems: dict[str, str] = field(default_factory=dict)

    def covered_by(self, mondo_id: str) -> str | None:
        return self.ids.get(mondo_id)

    def entry_named(self, stem: str) -> str | None:
        return self.stems.get(stem)


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


def build_coverage_index(kb_dirs: list[Path] | None = None) -> CoverageIndex:
    """Index every MONDO ID a committed KB entry already covers.

    Reads `kb/disorders/` (root `disease_term`, `has_subtypes[].subtype_term`,
    and exact/narrow `mondo_mappings`) *and* `kb/groupings/` — a stub whose
    concept is already a grouping is finished work, not an open gap.
    """
    index = CoverageIndex()
    for kb_dir in kb_dirs or default_kb_dirs():
        if not kb_dir.is_dir():
            continue
        is_grouping = kb_dir.name == "groupings"
        for path in sorted(kb_dir.glob("*.yaml")):
            if path.name.endswith(".history.yaml"):
                continue
            data = safe_load(path.read_text(encoding="utf-8"))
            if not isinstance(data, dict):
                continue
            rel = f"{kb_dir.name}/{path.name}"
            index.stems.setdefault(path.stem, rel)
            if is_grouping:
                for mondo_id in _grouping_mondo_ids(data):
                    index.ids.setdefault(mondo_id, rel)
            else:
                for mondo_id, _ in iter_covered_mondo_ids(data, path.name):
                    index.ids.setdefault(mondo_id, rel)
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


def check_stubs(
    stub_dir: Path | None = None,
    kb_dirs: list[Path] | None = None,
    coverage: CoverageIndex | None = None,
) -> list[StubIssue]:
    """Check the stub queue's structural invariants.

    The load-bearing one is `already_curated`: a stub whose MONDO ID is covered
    by a committed KB entry must be deleted. That is what makes "delete the stub,
    add the entry" a checkable contract rather than a convention.
    """
    issues: list[StubIssue] = []
    stubs = load_stubs(stub_dir)
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
                    f"{mondo_id} is covered by {covered_by} — delete this stub",
                )
            )
            continue

        # Same common name, different MONDO ID. Usually the KB curated a
        # narrower concept (`familial long QT syndrome` for a `long QT syndrome`
        # stub); sometimes it is the same disease under a different ID. A person
        # has to decide, so this is advisory.
        same_name = index.entry_named(path.stem)
        if same_name:
            issues.append(
                StubIssue(
                    path,
                    "possible_kb_duplicate",
                    f"{same_name} shares this name but curates a different MONDO ID",
                    severity="advisory",
                )
            )

    return issues
