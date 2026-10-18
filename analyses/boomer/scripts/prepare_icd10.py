"""Prepare WHO ICD-10 labels and hierarchy for OAK's Pronto adapter.

Download explicitly, verify the pinned archive, and project ClaML Class preferred
labels and SuperClass links into OBO. Coding instructions, inclusions, exclusions
and optional modifiers are not subclass axioms and are deliberately not projected.
"""

from __future__ import annotations

import argparse
import hashlib
import io
import urllib.request
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

import yaml

CONFIG = Path(__file__).resolve().parents[1] / "icd10/config.yaml"


def to_obo(xml, release):
    root = ET.fromstring(xml)
    classes = {c.attrib["code"]: c for c in root.findall("Class")}
    lines = [
        "format-version: 1.2",
        f"data-version: WHO-ICD10-{release}",
        "ontology: icd10-who",
        "",
    ]
    for code, node in sorted(classes.items()):
        label = node.find("Rubric[@kind='preferred']/Label")
        if label is None:
            raise ValueError(f"WHO class has no preferred label: {code}")
        name = " ".join("".join(label.itertext()).split())
        name = name.replace("\\", "\\\\").replace("!", "\\!")
        lines.extend(["[Term]", f"id: ICD10:{code}", f"name: {name}"])
        for parent in sorted(p.attrib["code"] for p in node.findall("SuperClass")):
            if parent not in classes:
                raise ValueError(f"Missing WHO superclass: {parent}")
            lines.append(f"is_a: ICD10:{parent}")
        lines.append("")
    return "\n".join(lines)


def prepare(oak_dir, config=CONFIG, archive=None):
    source = yaml.safe_load(Path(config).read_text())["who"]
    if archive:
        content = Path(archive).read_bytes()
    else:
        with urllib.request.urlopen(source["url"], timeout=60) as response:
            content = response.read()
    if hashlib.sha256(content).hexdigest() != source["sha256"]:
        raise ValueError("WHO archive checksum mismatch; inspect and repin explicitly")
    with zipfile.ZipFile(io.BytesIO(content)) as zipped:
        obo = to_obo(zipped.read(source["member"]), source["release"])
    if hashlib.sha256(obo.encode()).hexdigest() != source["obo_sha256"]:
        raise ValueError(
            "WHO OBO projection checksum mismatch; inspect converter changes"
        )
    path = Path(oak_dir) / source["obo_file"]
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists() or path.read_text() != obo:
        path.write_text(obo)
    print(f"WHO labels and hierarchy ready for OAK: {path}")
    return path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--oak-dir", type=Path, default=Path.home() / ".data/oaklib")
    parser.add_argument("--config", type=Path, default=CONFIG)
    parser.add_argument("--archive", type=Path, help="Use a downloaded WHO ZIP")
    args = parser.parse_args()
    prepare(args.oak_dir, args.config, args.archive)


if __name__ == "__main__":
    main()
