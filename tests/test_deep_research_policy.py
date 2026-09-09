"""Tests for repository-level deep-research provider policy."""

from __future__ import annotations

import os
import subprocess
from pathlib import Path

import pytest

from dismech.deep_research_policy import (
    BIOMNI_ENABLE_ENV_VAR,
    BIOMNI_UPSTREAM_DISABLE_ENV_VAR,
    biomni_enabled,
    configure_biomni_environment,
    deep_research_subprocess_environment,
    explicitly_requests_biomni,
    requests_biomni_research,
)

ROOT = Path(__file__).parent.parent


@pytest.mark.parametrize("value", [None, "", "0", "false", "no", "off", "unexpected"])
def test_biomni_is_disabled_without_explicit_truthy_opt_in(
    value: str | None,
) -> None:
    environ: dict[str, str] = {}
    if value is not None:
        environ[BIOMNI_ENABLE_ENV_VAR] = value

    assert not biomni_enabled(environ)
    assert not configure_biomni_environment(environ)
    assert environ[BIOMNI_UPSTREAM_DISABLE_ENV_VAR] == "true"


@pytest.mark.parametrize("value", ["1", "true", "TRUE", " yes ", "on"])
def test_explicit_opt_in_enables_biomni(value: str) -> None:
    environ = {
        BIOMNI_ENABLE_ENV_VAR: value,
        BIOMNI_UPSTREAM_DISABLE_ENV_VAR: "true",
    }

    assert biomni_enabled(environ)
    assert configure_biomni_environment(environ)
    assert BIOMNI_UPSTREAM_DISABLE_ENV_VAR not in environ


def test_subprocess_environment_is_isolated_and_disables_biomni_fallback() -> None:
    original = {"OPENSCIENTIST_API_KEY": "test-key"}

    result = deep_research_subprocess_environment(original)

    assert result[BIOMNI_UPSTREAM_DISABLE_ENV_VAR] == "true"
    assert BIOMNI_UPSTREAM_DISABLE_ENV_VAR not in original
    assert result["OPENSCIENTIST_API_KEY"] == "test-key"


@pytest.mark.parametrize(
    "arguments",
    [
        ["--provider", "biomni"],
        ["--provider=BIOMNI"],
        ["--fallback-provider", "Biomni"],
        ["--fallback-provider=biomni"],
    ],
)
def test_explicit_biomni_provider_arguments_are_detected(
    arguments: list[str],
) -> None:
    assert explicitly_requests_biomni(arguments)


def test_bare_fallback_and_read_only_provider_info_are_not_execution_requests() -> None:
    assert not explicitly_requests_biomni(["--provider", "openscientist", "--fallback"])
    assert not requests_biomni_research(["providers", "--provider", "biomni"])
    assert requests_biomni_research(
        ["research", "--provider", "openscientist", "--fallback-provider", "biomni"]
    )


@pytest.mark.parametrize(
    "arguments",
    [
        ["research", "--provider", "biomni", "test query"],
        [
            "research",
            "--provider",
            "openscientist",
            "--fallback-provider",
            "biomni",
            "test query",
        ],
    ],
)
def test_repository_wrapper_rejects_explicit_biomni_research_without_opt_in(
    arguments: list[str],
) -> None:
    environ = dict(os.environ)
    environ.pop(BIOMNI_ENABLE_ENV_VAR, None)

    result = subprocess.run(
        [str(ROOT / "scripts" / "run_deep_research_client.sh"), *arguments],
        check=False,
        capture_output=True,
        text=True,
        timeout=30,
        env=environ,
    )

    assert result.returncode == 2
    assert "DISMECH_ENABLE_BIOMNI=1" in result.stderr
