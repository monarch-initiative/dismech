"""Verify the downloadable extension and avoid docs-server rebuild loops."""

import importlib.util
import json
import os
import shutil
from html.parser import HTMLParser
from pathlib import Path
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "package_extension", ROOT / "scripts/package_extension.py"
)
packager = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(packager)


def test_unchanged_build_preserves_file_timestamp(tmp_path):
    destination = packager.package_extension(tmp_path / "extension.zip")
    payload = destination.read_bytes()
    os.utime(destination, ns=(1_000_000_000, 1_000_000_000))
    packager.package_extension(destination)
    assert destination.stat().st_mtime_ns == 1_000_000_000
    assert destination.read_bytes() == payload


def test_changed_runtime_asset_updates_archive(tmp_path, monkeypatch):
    shutil.copytree(ROOT / "extension", tmp_path / "extension")
    monkeypatch.setattr(packager, "ROOT", tmp_path)
    destination = packager.package_extension(tmp_path / "extension.zip")
    asset = tmp_path / "extension/popup.js"
    asset.write_text(asset.read_text() + "\n// Updated runtime asset\n")
    packager.package_extension(destination)
    with ZipFile(destination) as archive:
        assert archive.read("dismech-extension/popup.js") == asset.read_bytes()


def test_archive_contains_referenced_runtime_assets(tmp_path):
    class AssetLinks(HTMLParser):
        def handle_starttag(self, tag, attrs):
            for key, value in attrs:
                if (
                    key in ("src", "href")
                    and value
                    and not value.startswith(("#", "https:", "http:"))
                ):
                    required.add(value)

    with ZipFile(packager.package_extension(tmp_path / "extension.zip")) as archive:
        assert archive.testzip() is None
        prefix = "dismech-extension/"
        names = {name.removeprefix(prefix) for name in archive.namelist()}
        manifest = json.loads(archive.read(prefix + "manifest.json"))
        required = {
            manifest["action"]["default_popup"],
            manifest["options_page"],
            "extract.js",  # Injected by popup.js rather than declared in the manifest.
            *manifest["icons"].values(),
            *manifest["action"]["default_icon"].values(),
        }
        if "default_locale" in manifest:
            required.add(f"_locales/{manifest['default_locale']}/messages.json")
        for name in names:
            if name.endswith(".html"):
                AssetLinks().feed(archive.read(prefix + name).decode())
        assert required <= names, f"Missing runtime assets: {required - names}"
        assert not any(
            name.startswith("test/") or name.endswith(".py") for name in names
        )
