"""Build the curator download before MkDocs collects static files."""

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parents[1]


def package_extension(destination: Path) -> Path:
    """Package runtime assets with a stable folder name and reproducible metadata."""
    source = ROOT / "extension"
    files = [source / "manifest.json"]
    for pattern in ("*.js", "*.html", "*.css", "icons/*.png"):
        files.extend(source.glob(pattern))
    destination.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(destination, "w", compression=ZIP_DEFLATED) as archive:
        for path in sorted(files):
            name = "dismech-extension/" + path.relative_to(source).as_posix()
            info = ZipInfo(name, date_time=(2025, 1, 1, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes())
    return destination


def on_pre_build(config):
    """MkDocs hook: publish the ZIP alongside the installation guide."""
    package_extension(Path(config["docs_dir"]) / "downloads/dismech-extension.zip")


if __name__ == "__main__":
    print(package_extension(ROOT / "docs/downloads/dismech-extension.zip"))
