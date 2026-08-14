"""Audit curated ``clinical_trials`` status/phase against live ClinicalTrials.gov.

A dismech ``ClinicalTrial`` records ``status:`` (RECRUITING, COMPLETED, ...) and
``phase:`` as a *snapshot taken at curation time*. Nothing re-checks them
afterwards: every other structured source in the repo has a ``*-refresh`` recipe,
but the trial registry is a live API with no equivalent, and the
``references_cache/clinicaltrials_*.md`` records carry no retrieval timestamp, so
drift is not even measurable offline. A trial curated as ``RECRUITING`` stays
``RECRUITING`` in the KB long after it completes or is terminated.

This module closes that gap on the *reporting* side: it reads the curated
status/phase out of the KB, fetches the current values from the ClinicalTrials.gov
v2 API, and reports the disagreements.

It deliberately does **not** rewrite the KB. A status change is often not a
one-field edit -- a trial moving to COMPLETED or TERMINATED usually wants its
``description``/``evidence`` revisited too, and TERMINATED in particular is a
curation signal rather than a mechanical update. The audit produces the worklist;
a curator (or a follow-up curation pass) applies it.

Network-dependent and therefore **advisory**: it is not part of ``just qc``. Run
it on demand::

    just clinicaltrials-status-audit                    # full report
    just clinicaltrials-status-audit --only-drift       # just the worklist
    just clinicaltrials-status-audit --format json      # machine-readable
    just clinicaltrials-status-audit --strict           # exit 1 if drift found
"""

from __future__ import annotations

import argparse
import json
import logging
import re
import sys
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Iterable, Iterator, Sequence

from dismech.yaml_io import safe_load

logger = logging.getLogger(__name__)

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
DEFAULT_KB_GLOBS = ("kb/disorders/*.yaml", "kb/modules/*.yaml", "kb/comorbidities/*.yaml")

CLINICALTRIALS_BATCH_URL = "https://clinicaltrials.gov/api/v2/studies"

# Bioregistry standard: NCT followed by 8 digits.
NCT_ID_RE = re.compile(r"\bNCT\d{8}\b", re.IGNORECASE)

# ClinicalTrials.gov `overallStatus` -> dismech ClinicalTrialStatusEnum.
# Values absent here (expanded-access states such as AVAILABLE) are reported as
# unmappable rather than silently coerced into UNKNOWN.
STATUS_MAP = {
    "RECRUITING": "RECRUITING",
    "NOT_YET_RECRUITING": "NOT_RECRUITING",
    "ACTIVE_NOT_RECRUITING": "ACTIVE_NOT_RECRUITING",
    "COMPLETED": "COMPLETED",
    "ENROLLING_BY_INVITATION": "ENROLLING_BY_INVITATION",
    "SUSPENDED": "SUSPENDED",
    "TERMINATED": "TERMINATED",
    "WITHDRAWN": "WITHDRAWN",
    "UNKNOWN": "UNKNOWN",
    "UNKNOWN_STATUS": "UNKNOWN",
    "WITHHELD": "UNKNOWN",
}

# ClinicalTrials.gov `phases` tokens -> dismech ClinicalTrialPhaseEnum.
PHASE_MAP = {
    "EARLY_PHASE1": "PHASE_I",  # approximate: dismech has no Early Phase 1 value
    "PHASE1": "PHASE_I",
    "PHASE2": "PHASE_II",
    "PHASE3": "PHASE_III",
    "PHASE4": "PHASE_IV",
    "NA": "NOT_APPLICABLE",
}

# Statuses that usually mean more than a one-field edit is warranted.
CURATION_SIGNAL_STATUSES = {"TERMINATED", "WITHDRAWN", "SUSPENDED"}


@dataclass
class CuratedTrial:
    """One ``clinical_trials[]`` entry as recorded in the KB."""

    path: str
    index: int
    nct_id: str | None
    name: str
    status: str | None
    phase: str | None

    @property
    def location(self) -> str:
        return f"{Path(self.path).name}:clinical_trials[{self.index}]"


@dataclass
class TrialFinding:
    """One audit result for a curated trial."""

    kind: str  # status_drift | phase_drift | missing_status | missing_phase
    #            | not_found | unresolvable_id | unmappable_status
    location: str
    nct_id: str | None
    name: str
    curated: str | None = None
    live: str | None = None
    detail: str = ""
    last_update: str | None = None
    curation_signal: bool = False


@dataclass
class AuditReport:
    trials_seen: int = 0
    ids_resolved: int = 0
    ids_queried: int = 0
    ids_returned: int = 0
    findings: list[TrialFinding] = field(default_factory=list)
    fetch_error: str | None = None

    @property
    def drift(self) -> list[TrialFinding]:
        return [f for f in self.findings if f.kind in ("status_drift", "phase_drift")]


def _resolve_nct_id(trial: dict[str, Any]) -> str | None:
    """Best-effort NCT id for a trial entry.

    Prefers ``name`` (the schema's documented home for the identifier), then falls
    back to any ``clinicaltrials:`` evidence reference -- 8 KB entries are named
    with a non-NCT registry id or trial acronym (EudraCT, ChiCTR, "EMERALD") but
    may still cite an NCT record.
    """
    match = NCT_ID_RE.search(str(trial.get("name") or ""))
    if match:
        return match.group(0).upper()
    for item in trial.get("evidence") or []:
        if not isinstance(item, dict):
            continue
        match = NCT_ID_RE.search(str(item.get("reference") or ""))
        if match:
            return match.group(0).upper()
    return None


def iter_curated_trials(paths: Iterable[Path]) -> Iterator[CuratedTrial]:
    """Yield every ``clinical_trials[]`` entry across the given KB files."""
    for path in paths:
        try:
            data = safe_load(path.read_text(encoding="utf-8"))
        except Exception as exc:  # a malformed file is the schema validator's job
            logger.warning("Skipping unparseable %s: %s", path, exc)
            continue
        if not isinstance(data, dict):
            continue
        for index, trial in enumerate(data.get("clinical_trials") or []):
            if not isinstance(trial, dict):
                continue
            yield CuratedTrial(
                path=str(path),
                index=index,
                nct_id=_resolve_nct_id(trial),
                name=str(trial.get("name") or "").strip(),
                status=trial.get("status"),
                phase=trial.get("phase"),
            )


def fetch_live_studies(
    nct_ids: Sequence[str],
    *,
    batch_size: int = 100,
    timeout: int = 60,
    rate_limit_delay: float = 0.5,
    session: Any = None,
) -> dict[str, dict[str, Any]]:
    """Fetch current status/phase for `nct_ids` from the ClinicalTrials.gov v2 API.

    Batched via ``filter.ids`` -- ~8 requests for the whole KB rather than ~800.
    Returns a mapping of NCT id -> ``{"status", "phases", "last_update"}``; ids the
    registry does not return are simply absent from the mapping.
    """
    import requests  # imported lazily so offline unit tests need not install it

    session = session or requests.Session()
    live: dict[str, dict[str, Any]] = {}

    for start in range(0, len(nct_ids), batch_size):
        batch = list(nct_ids[start : start + batch_size])
        response = session.get(
            CLINICALTRIALS_BATCH_URL,
            params={
                "filter.ids": ",".join(batch),
                "fields": "NCTId,OverallStatus,Phase,LastUpdateSubmitDate",
                "pageSize": batch_size,
            },
            timeout=timeout,
        )
        response.raise_for_status()
        for study in response.json().get("studies", []):
            protocol = study.get("protocolSection", {})
            nct_id = protocol.get("identificationModule", {}).get("nctId")
            if not nct_id:
                continue
            status_module = protocol.get("statusModule", {})
            live[nct_id.upper()] = {
                "status": status_module.get("overallStatus"),
                "phases": protocol.get("designModule", {}).get("phases") or [],
                "last_update": status_module.get("lastUpdateSubmitDate"),
            }
        if start + batch_size < len(nct_ids):
            time.sleep(rate_limit_delay)

    return live


def audit_trials(
    trials: Sequence[CuratedTrial],
    live: dict[str, dict[str, Any]],
) -> list[TrialFinding]:
    """Compare curated status/phase against fetched live values."""
    findings: list[TrialFinding] = []

    for trial in trials:
        if not trial.nct_id:
            findings.append(
                TrialFinding(
                    kind="unresolvable_id",
                    location=trial.location,
                    nct_id=None,
                    name=trial.name,
                    detail="no NCT id in name or evidence references; cannot be re-checked",
                )
            )
            continue

        record = live.get(trial.nct_id)
        if record is None:
            findings.append(
                TrialFinding(
                    kind="not_found",
                    location=trial.location,
                    nct_id=trial.nct_id,
                    name=trial.name,
                    detail="id not returned by ClinicalTrials.gov",
                )
            )
            continue

        last_update = record.get("last_update")

        # --- status ---
        live_status_raw = record.get("status")
        live_status = STATUS_MAP.get(str(live_status_raw or "").upper())
        if live_status_raw and live_status is None:
            findings.append(
                TrialFinding(
                    kind="unmappable_status",
                    location=trial.location,
                    nct_id=trial.nct_id,
                    name=trial.name,
                    curated=trial.status,
                    live=live_status_raw,
                    detail="registry status has no ClinicalTrialStatusEnum equivalent",
                    last_update=last_update,
                )
            )
        elif not trial.status:
            findings.append(
                TrialFinding(
                    kind="missing_status",
                    location=trial.location,
                    nct_id=trial.nct_id,
                    name=trial.name,
                    live=live_status,
                    detail="no curated status; registry value available",
                    last_update=last_update,
                )
            )
        elif live_status and trial.status != live_status:
            findings.append(
                TrialFinding(
                    kind="status_drift",
                    location=trial.location,
                    nct_id=trial.nct_id,
                    name=trial.name,
                    curated=trial.status,
                    live=live_status,
                    last_update=last_update,
                    curation_signal=live_status in CURATION_SIGNAL_STATUSES,
                )
            )

        # --- phase ---
        live_phases = {
            PHASE_MAP[token.upper()]
            for token in record.get("phases") or []
            if token.upper() in PHASE_MAP
        }
        if not trial.phase:
            if live_phases:
                findings.append(
                    TrialFinding(
                        kind="missing_phase",
                        location=trial.location,
                        nct_id=trial.nct_id,
                        name=trial.name,
                        live="|".join(sorted(live_phases)),
                        detail="no curated phase; registry value available",
                        last_update=last_update,
                    )
                )
        elif live_phases and trial.phase not in live_phases:
            # A multi-phase registry record (e.g. PHASE1|PHASE2) matches if the
            # curated value is any one of its phases.
            findings.append(
                TrialFinding(
                    kind="phase_drift",
                    location=trial.location,
                    nct_id=trial.nct_id,
                    name=trial.name,
                    curated=trial.phase,
                    live="|".join(sorted(live_phases)),
                    last_update=last_update,
                )
            )

    return findings


def render_text(report: AuditReport, *, only_drift: bool = False) -> str:
    lines: list[str] = []
    lines.append("ClinicalTrials.gov status audit")
    lines.append("=" * 60)
    lines.append(f"  curated trials scanned : {report.trials_seen}")
    lines.append(f"  NCT ids resolved       : {report.ids_resolved}")
    lines.append(f"  ids returned by registry: {report.ids_returned}/{report.ids_queried}")
    if report.fetch_error:
        lines.append(f"  FETCH ERROR            : {report.fetch_error}")

    groups: dict[str, list[TrialFinding]] = {}
    for finding in report.findings:
        groups.setdefault(finding.kind, []).append(finding)

    order = [
        ("status_drift", "Status drift (curated != registry)"),
        ("phase_drift", "Phase drift (curated != registry)"),
        ("missing_status", "Missing curated status"),
        ("missing_phase", "Missing curated phase"),
        ("not_found", "Not found in registry"),
        ("unresolvable_id", "No resolvable NCT id"),
        ("unmappable_status", "Registry status has no dismech enum"),
    ]
    if only_drift:
        order = order[:2]

    lines.append("")
    for kind, title in order:
        items = groups.get(kind) or []
        lines.append(f"{title}: {len(items)}")
        for finding in sorted(items, key=lambda f: f.location):
            marker = " [review]" if finding.curation_signal else ""
            if finding.curated or finding.live:
                lines.append(
                    f"    {finding.location} ({finding.nct_id or finding.name}): "
                    f"{finding.curated or '-'} -> {finding.live or '-'}"
                    f"{' last updated ' + finding.last_update if finding.last_update else ''}"
                    f"{marker}"
                )
            else:
                lines.append(
                    f"    {finding.location} ({finding.nct_id or finding.name}): {finding.detail}"
                )
        lines.append("")

    drift = len(report.drift)
    lines.append(
        f"TOTAL: {drift} drifted, {len(report.findings) - drift} other finding(s). "
        "Advisory -- no KB files were modified."
    )
    return "\n".join(lines)


def render_markdown(report: AuditReport) -> str:
    lines = [
        "# ClinicalTrials.gov status audit",
        "",
        f"- curated trials scanned: **{report.trials_seen}**",
        f"- NCT ids resolved: **{report.ids_resolved}**",
        f"- ids returned by registry: **{report.ids_returned}/{report.ids_queried}**",
        "",
        "| Location | NCT | Finding | Curated | Registry | Last update |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for finding in sorted(report.findings, key=lambda f: (f.kind, f.location)):
        lines.append(
            f"| {finding.location} | {finding.nct_id or '-'} | {finding.kind} | "
            f"{finding.curated or '-'} | {finding.live or '-'} | {finding.last_update or '-'} |"
        )
    return "\n".join(lines) + "\n"


def _default_paths() -> list[Path]:
    paths: list[Path] = []
    for pattern in DEFAULT_KB_GLOBS:
        paths.extend(sorted(ROOT_DIR.glob(pattern)))
    return paths


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="python -m dismech.clinical_trial_status",
        description=(
            "Audit curated clinical_trials status/phase against live "
            "ClinicalTrials.gov. Advisory: reports only, never edits the KB."
        ),
    )
    parser.add_argument("files", nargs="*", type=Path, help="KB YAML files (default: all)")
    parser.add_argument(
        "--format", choices=("text", "json", "markdown"), default="text",
        help="Output format (default: text)",
    )
    parser.add_argument(
        "--only-drift", action="store_true",
        help="Report only status/phase drift, omitting coverage findings",
    )
    parser.add_argument(
        "--limit", type=int, default=0,
        help="Cap the number of trials checked (0 = no cap); for bounded sweeps",
    )
    parser.add_argument(
        "--strict", action="store_true",
        help="Exit 1 when drift is found (default: advisory, always exits 0)",
    )
    parser.add_argument("--batch-size", type=int, default=100)
    parser.add_argument("--timeout", type=int, default=60)
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args(argv)

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO, format="%(message)s"
    )

    paths = args.files or _default_paths()
    trials = list(iter_curated_trials(paths))
    report = AuditReport(trials_seen=len(trials))

    if args.limit:
        trials = trials[: args.limit]

    nct_ids = sorted({t.nct_id for t in trials if t.nct_id})
    report.ids_resolved = len(nct_ids)
    report.ids_queried = len(nct_ids)

    live: dict[str, dict[str, Any]] = {}
    if nct_ids:
        try:
            live = fetch_live_studies(
                nct_ids, batch_size=args.batch_size, timeout=args.timeout
            )
        except Exception as exc:  # network is not a reason to crash an advisory tool
            report.fetch_error = f"{type(exc).__name__}: {exc}"
            logger.warning("ClinicalTrials.gov fetch failed: %s", report.fetch_error)
    report.ids_returned = len(live)

    if live or not report.fetch_error:
        report.findings = audit_trials(trials, live)

    if args.only_drift and args.format != "text":
        report.findings = report.drift

    if args.format == "json":
        print(json.dumps(asdict(report), indent=2, sort_keys=True))
    elif args.format == "markdown":
        print(render_markdown(report))
    else:
        print(render_text(report, only_drift=args.only_drift))

    if report.fetch_error and not live:
        return 2
    if args.strict and report.drift:
        return 1
    return 0


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
