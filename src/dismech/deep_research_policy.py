"""Repository policy for deep-research providers with local side effects."""

from __future__ import annotations

import os
from collections.abc import Mapping, MutableMapping, Sequence

BIOMNI_ENABLE_ENV_VAR = "DISMECH_ENABLE_BIOMNI"
BIOMNI_UPSTREAM_DISABLE_ENV_VAR = "DISABLE_BIOMNI_PROVIDER"
TRUE_ENV_VALUES = frozenset({"1", "true", "yes", "on"})
BIOMNI_PROVIDER_FLAGS = frozenset({"--provider", "--fallback-provider"})

BIOMNI_DISABLED_DETAIL = (
    "Biomni is disabled by default because it executes model-generated code "
    "locally and may initialize a large data lake. Set "
    f"{BIOMNI_ENABLE_ENV_VAR}=1 for an intentional run."
)


def biomni_enabled(environ: Mapping[str, str] | None = None) -> bool:
    """Return whether this process explicitly opted in to Biomni execution."""
    source = os.environ if environ is None else environ
    return source.get(BIOMNI_ENABLE_ENV_VAR, "").strip().lower() in TRUE_ENV_VALUES


def configure_biomni_environment(
    environ: MutableMapping[str, str] | None = None,
) -> bool:
    """Translate the dismech opt-in into deep-research-client's opt-out gate.

    The upstream client auto-detects Biomni whenever its Python runtime is
    importable. That also puts Biomni into automatic fallback ordering. Dismech
    instead requires a positive opt-in, so every supported client entry point
    calls this before provider discovery.

    Returns:
        ``True`` when Biomni was explicitly enabled.
    """
    target = os.environ if environ is None else environ
    enabled = biomni_enabled(target)
    if enabled:
        target.pop(BIOMNI_UPSTREAM_DISABLE_ENV_VAR, None)
    else:
        target[BIOMNI_UPSTREAM_DISABLE_ENV_VAR] = "true"
    return enabled


def deep_research_subprocess_environment(
    environ: Mapping[str, str] | None = None,
) -> dict[str, str]:
    """Return an isolated subprocess environment with the Biomni gate applied."""
    result = dict(os.environ if environ is None else environ)
    configure_biomni_environment(result)
    return result


def explicitly_requests_biomni(arguments: Sequence[str]) -> bool:
    """Return whether provider arguments explicitly name Biomni.

    Covers both ``--flag biomni`` and ``--flag=biomni`` forms for the primary
    provider and ordered fallback providers. This check happens before the
    upstream client can consult a cached Biomni result.
    """
    for index, argument in enumerate(arguments):
        if argument in BIOMNI_PROVIDER_FLAGS:
            if (
                index + 1 < len(arguments)
                and arguments[index + 1].casefold() == "biomni"
            ):
                return True
            continue
        flag, separator, value = argument.partition("=")
        if separator and flag in BIOMNI_PROVIDER_FLAGS and value.casefold() == "biomni":
            return True
    return False


def requests_biomni_research(arguments: Sequence[str]) -> bool:
    """Return whether a deep-research CLI execution explicitly requests Biomni."""
    return "research" in arguments and explicitly_requests_biomni(arguments)
