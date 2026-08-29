"""Guard the social-media citation ban (design decision 6b).

Published patient-advocacy content is citable; user-generated social-media
content is not. That half of 6b needs its own check because the corroboration
gate cannot carry it: the corroboration rule is opt-in by tagging, so an untagged
forum URL is invisible to it, and every other gate passes a forum citation
happily -- the URL resolves and the snippet is a real quote from the page.

Matching is on the reference host, which is the one part of a `url:` reference
that is not a matter of judgement. The list is deliberately short and explicit
rather than heuristic: a pattern like "any site with user accounts" would catch
preprint servers and registries, and a curator arguing with a false positive is
how a gate gets disabled.

This is a *deferred* decision, not a settled one. If social media becomes
citable, delete this check and its CI step together with the exemption below --
do not weaken the host list to let one case through.
"""

from __future__ import annotations

from typing import Any, Iterator
from urllib.parse import urlparse

# Hosts whose content is user-generated. Suffix-matched against the reference
# host, so `old.reddit.com` and `www.reddit.com` both match `reddit.com`.
SOCIAL_MEDIA_HOSTS = (
    "reddit.com",
    "facebook.com",
    "fb.com",
    "instagram.com",
    "twitter.com",
    "x.com",
    "tiktok.com",
    "threads.net",
    "bsky.app",
    "mastodon.social",
    "tumblr.com",
    "quora.com",
    "medium.com",
    "substack.com",
    "youtube.com",
    "youtu.be",
    "discord.com",
    "patientslikeme.com",
    "healthunlocked.com",
    "inspire.com",
)


def _host_of(reference: str) -> str | None:
    """Return the lowercased host of a `url:` reference, or None for other prefixes."""
    text = str(reference)
    if not text.lower().startswith("url:"):
        return None
    parsed = urlparse(text[len("url:") :])
    return (parsed.hostname or "").lower() or None


def is_social_media_reference(reference: str) -> bool:
    """True if `reference` is a `url:` reference to a known social-media host."""
    host = _host_of(reference)
    if not host:
        return False
    return any(host == bad or host.endswith("." + bad) for bad in SOCIAL_MEDIA_HOSTS)


def iter_references(node: Any, path: str = "") -> Iterator[tuple[str, str]]:
    """Yield every ``(dotted_path, reference)`` pair anywhere in a document.

    Covers both evidence-item `reference:` values and the top-level `references:`
    list, since a forum can be cited as either.
    """
    if isinstance(node, dict):
        for key, value in node.items():
            child = f"{path}.{key}" if path else key
            if key == "reference" and isinstance(value, str):
                yield child, value
            else:
                yield from iter_references(value, child)
    elif isinstance(node, list):
        for index, item in enumerate(node):
            yield from iter_references(item, f"{path}[{index}]")


def social_media_reference_errors(data: Any) -> list[str]:
    """Return one message per reference pointing at a social-media host."""
    return [
        f"{path}: social-media reference is not citable ({reference})"
        for path, reference in iter_references(data)
        if is_social_media_reference(reference)
    ]
