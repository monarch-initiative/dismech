"""Recover OpenScientist jobs by ID: job records, resumable bundle download, artifact extraction.

Three failures motivate this module (dismech#13616, #12908, #11254):

* The deep-research client can die on a network timeout after the provider job has
  finished. The job is then complete server-side, but the runner records an error and
  nothing on disk says which job to recover.
* The artifact bundle (``GET /api/v1/jobs/<id>/artifacts``) can be large and slow
  enough to hit a gateway timeout, and the client does not retry.
* The client keeps only bundle members whose extension is on an allowlist and
  flattens their paths, so ``MANIFEST.yaml``, ``analysis.py`` and ``environment.txt``
  are dropped and the analysis gate fails on a bundle the provider completed.

The runner records the job ID beside the report (``<report>.job.yaml``) as soon as the
client's log reveals it, and ``fetch`` uses that record to download the bundle again
and extract the run's ``artifact_dir`` subtree with its canonical paths.
"""

from __future__ import annotations

import os
import re
import time
import zipfile
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path, PurePosixPath
from typing import Any

import httpx
import yaml

DEFAULT_BASE_URL = "https://www.openscientist.io"
JOB_ID_PATTERN = re.compile(
    r"OpenScientist job submitted: ([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-"
    r"[0-9a-fA-F]{4}-[0-9a-fA-F]{12})"
)
TERMINAL_STATUSES = {"completed", "failed", "cancelled"}
RETRYABLE_STATUS_CODES = {408, 425, 429, 500, 502, 503, 504, 520, 522, 524}


def extract_job_id(log_text: str | None) -> str | None:
    """Return the last OpenScientist job ID announced in a client log, if any."""
    if not log_text:
        return None
    matches = JOB_ID_PATTERN.findall(log_text)
    return matches[-1].lower() if matches else None


def job_record_path(report_path: Path) -> Path:
    """Return the sidecar path that records which provider job produced a report."""
    return Path(f"{report_path}.job.yaml")


def write_job_record(
    report_path: Path,
    *,
    provider: str,
    job_id: str,
    template_file: str | None = None,
    template_sha: str | None = None,
) -> Path:
    """Write (or refresh) the job sidecar for a report and return its path.

    The template path and its git blob hash are recorded when the job is launched,
    so a later ``fetch`` applies the gate of the template the job actually ran
    under, and can tell when the template has changed since.
    """
    path = job_record_path(report_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    record: dict[str, Any] = {
        "provider": provider,
        "job_id": job_id,
        "recorded_at": datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    if template_file:
        record["template_file"] = template_file
    if template_sha:
        record["template_sha"] = template_sha
    path.write_text(yaml.safe_dump(record, sort_keys=False), encoding="utf-8")
    return path


def read_job_record(report_path: Path) -> dict[str, Any] | None:
    """Return the job sidecar for a report, or None when there is none."""
    path = job_record_path(report_path)
    if not path.is_file():
        return None
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    return data if isinstance(data, dict) else None


@dataclass
class OpenScientistJobs:
    """Minimal OpenScientist REST client for job lookup and bundle download."""

    api_key: str
    base_url: str = DEFAULT_BASE_URL
    retries: int = 4
    backoff_seconds: float = 2.0
    read_timeout_seconds: float = 600.0
    transport: httpx.BaseTransport | None = None

    @classmethod
    def from_environment(cls) -> OpenScientistJobs:
        api_key = os.environ.get("OPENSCIENTIST_API_KEY", "")
        if not api_key:
            raise RuntimeError("OPENSCIENTIST_API_KEY is not set")
        base_url = os.environ.get("OPENSCIENTIST_URL") or DEFAULT_BASE_URL
        return cls(api_key=api_key, base_url=base_url.rstrip("/"))

    def _headers(self) -> dict[str, str]:
        return {"Authorization": f"Bearer {self.api_key}"}

    def _get_json(self, path: str, params: dict[str, Any] | None = None) -> Any:
        """GET a JSON endpoint, retrying timeouts and gateway errors with backoff."""
        timeout = httpx.Timeout(30.0, read=self.read_timeout_seconds)
        last_error: Exception | None = None
        for attempt in range(self.retries + 1):
            if attempt:
                time.sleep(self.backoff_seconds * (2 ** (attempt - 1)))
            try:
                with httpx.Client(
                    timeout=timeout, follow_redirects=True, transport=self.transport
                ) as client:
                    response = client.get(
                        f"{self.base_url}{path}", headers=self._headers(), params=params
                    )
            except (httpx.TimeoutException, httpx.TransportError) as error:
                last_error = error
                continue
            if response.status_code in RETRYABLE_STATUS_CODES:
                last_error = RuntimeError(f"HTTP {response.status_code} from {path}")
                continue
            response.raise_for_status()
            return response.json()
        raise RuntimeError(
            f"{path} failed after {self.retries + 1} attempts: {last_error}"
        )

    def job(self, job_id: str) -> dict[str, Any]:
        """Return the job detail record."""
        return self._get_json(f"/api/v1/jobs/{job_id}")

    def recent_jobs(self, limit: int = 50) -> list[dict[str, Any]]:
        """Return the account's most recent jobs, newest first."""
        data = self._get_json("/api/v1/jobs", params={"limit": limit})
        jobs = data.get("jobs", data) if isinstance(data, dict) else data
        return [job for job in jobs if isinstance(job, dict)]

    def find_jobs(self, *needles: str, limit: int = 50) -> list[dict[str, Any]]:
        """Return recent jobs whose research question contains every needle."""
        wanted = [needle for needle in needles if needle]
        return [
            job
            for job in self.recent_jobs(limit=limit)
            if all(
                needle in str(job.get("research_question") or "") for needle in wanted
            )
        ]

    def download_bundle(self, job_id: str, destination: Path) -> Path:
        """Download the job's artifact ZIP, retrying and resuming where possible.

        A partial file left by an attempt that died with a transport error or timeout
        is resumed with an HTTP Range request; a server that ignores the range (200
        instead of 206) restarts the download from zero, and one that rejects it (416)
        has the partial file discarded. A stream that ends cleanly but short leaves a
        file that is not a ZIP archive; that file is discarded rather than resumed,
        so resume only helps when the transfer fails with an exception. The file is
        written to ``<destination>.part`` and renamed only once it is a readable ZIP.
        """
        url = f"{self.base_url}/api/v1/jobs/{job_id}/artifacts"
        destination.parent.mkdir(parents=True, exist_ok=True)
        partial = Path(f"{destination}.part")
        last_error: Exception | None = None
        for attempt in range(self.retries + 1):
            if attempt:
                time.sleep(self.backoff_seconds * (2 ** (attempt - 1)))
            offset = partial.stat().st_size if partial.exists() else 0
            headers = self._headers()
            if offset:
                headers["Range"] = f"bytes={offset}-"
            try:
                timeout = httpx.Timeout(30.0, read=self.read_timeout_seconds)
                with (
                    httpx.Client(
                        timeout=timeout, follow_redirects=True, transport=self.transport
                    ) as client,
                    client.stream("GET", url, headers=headers) as response,
                ):
                    if response.status_code == 416:
                        # The server rejected the resume range: start over.
                        partial.unlink(missing_ok=True)
                        last_error = RuntimeError(f"HTTP 416 resuming {url}")
                        continue
                    if response.status_code in RETRYABLE_STATUS_CODES:
                        last_error = RuntimeError(
                            f"HTTP {response.status_code} downloading {url}"
                        )
                        continue
                    response.raise_for_status()
                    mode = "ab" if offset and response.status_code == 206 else "wb"
                    with partial.open(mode) as handle:
                        for chunk in response.iter_bytes():
                            handle.write(chunk)
            except (httpx.TimeoutException, httpx.TransportError) as error:
                last_error = error
                continue
            if zipfile.is_zipfile(partial):
                partial.replace(destination)
                return destination
            last_error = RuntimeError(
                f"downloaded bundle for {job_id} is not a ZIP archive"
            )
            partial.unlink(missing_ok=True)
        raise RuntimeError(
            f"could not download the artifact bundle for job {job_id} after "
            f"{self.retries + 1} attempts: {last_error}"
        )


def artifact_anchor(artifact_dir: Path) -> tuple[str, ...]:
    """Return the path segments that identify a run's artifact directory in a bundle."""
    parts = tuple(
        part for part in PurePosixPath(artifact_dir.as_posix()).parts if part != "/"
    )
    return parts[-3:]


def _safe_relative(parts: tuple[str, ...]) -> PurePosixPath | None:
    """Return a relative path with no traversal, or None for an unsafe member."""
    if not parts or any(part in {"", ".", ".."} for part in parts):
        return None
    return PurePosixPath(*parts)


def extract_artifact_subtree(
    bundle: Path, artifact_dir: Path, destination: Path | None = None
) -> list[Path]:
    """Extract every bundle member under the run's ``artifact_dir``, keeping its path.

    Members are matched on the last three ``artifact_dir`` segments
    (``<disease>/<hypothesis>/<provider>_artifacts``) wherever they occur in the member
    name, so the match holds whether or not the bundle or the local output root carries
    the ``kb/hypotheses`` prefix. No extension filtering is applied: the provider's declared artifact
    directory is the bundle. Members outside it, and members whose relative path would
    escape the destination, are ignored.
    """
    destination = destination or artifact_dir
    anchor = artifact_anchor(artifact_dir)
    width = len(anchor)
    written: list[Path] = []
    with zipfile.ZipFile(bundle) as archive:
        for info in archive.infolist():
            if info.is_dir():
                continue
            parts = PurePosixPath(info.filename.replace("\\", "/")).parts
            for start in range(len(parts) - width):
                if parts[start : start + width] == anchor:
                    relative = _safe_relative(parts[start + width :])
                    break
            else:
                continue
            if relative is None:
                continue
            target = destination.joinpath(*relative.parts)
            target.parent.mkdir(parents=True, exist_ok=True)
            with archive.open(info) as source, target.open("wb") as sink:
                while chunk := source.read(1 << 20):
                    sink.write(chunk)
            written.append(target)
    return written


def remove_flattened_duplicates(artifact_dir: Path) -> list[Path]:
    """Delete client-flattened copies whose canonical file now exists byte-for-byte.

    The client writes ``a/b.csv`` under ``artifact_dir`` as
    ``<artifact_dir with / replaced by _>_a_b.csv`` (the naming of the OpenScientist
    provider's artifact extraction in deep-research-client 0.2.12). If the client
    changes that scheme nothing matches and nothing is removed, which fails safe. When the canonical file has been
    restored and is identical, the flattened copy is redundant and is removed.
    """
    prefix = artifact_dir.as_posix().strip("/").replace("/", "_") + "_"
    removed: list[Path] = []
    if not artifact_dir.is_dir():
        return removed
    canonical = [
        path
        for path in artifact_dir.rglob("*")
        if path.is_file() and not path.name.startswith(prefix)
    ]
    by_flat_name = {
        prefix + path.relative_to(artifact_dir).as_posix().replace("/", "_"): path
        for path in canonical
    }
    for path in artifact_dir.iterdir():
        if not (path.is_file() and path.name.startswith(prefix)):
            continue
        original = by_flat_name.get(path.name)
        if original is not None and original.read_bytes() == path.read_bytes():
            path.unlink()
            removed.append(path)
    return removed


def find_report_markdown(bundle: Path, artifact_dir: Path) -> tuple[str, str] | None:
    """Return ``(member name, text)`` of the provider's markdown report, or None.

    Prefers a member named like ``final_report.md``; otherwise the largest markdown
    member outside the run's artifact directory.
    """
    anchor = "/".join(artifact_anchor(artifact_dir))
    with zipfile.ZipFile(bundle) as archive:
        candidates = [
            info
            for info in archive.infolist()
            if not info.is_dir()
            and info.filename.lower().endswith(".md")
            and anchor not in info.filename.replace("\\", "/")
            and not info.filename.startswith(".claude/")
        ]
        if not candidates:
            return None
        named = [
            info
            for info in candidates
            if PurePosixPath(info.filename).name.lower().startswith("final_report")
        ]
        chosen = (named or sorted(candidates, key=lambda info: info.file_size))[-1]
        return chosen.filename, archive.read(chosen).decode("utf-8", errors="replace")
