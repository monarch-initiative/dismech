"""Fetch selected members of a remote zip64 archive with HTTP range requests.

The deposited ``Model_generated_data.zip`` is 5.7 GB, almost all of it
intermediate frames. Scoring needs only each run's final frame, about 1% of it.
This reads the archive's central directory and downloads just the matching
members. Requires ``curl``. Already-fetched members of the right size are skipped.

Usage:
    fetch_zip_members.py URL PATTERN OUT_DIR

Example (final frames of every deposited run):
    fetch_zip_members.py \\
      https://ftp.ebi.ac.uk/biostudies/fire/S-ONTX/034/S-ONTX34/Files/WP7-9files/WP9/NTC_model/Model_generated_data.zip \\
      '_celldata/12000_cell_data\\.pkl$' deposited/
"""

import argparse
import re
import struct
import subprocess
import zlib
from pathlib import Path


def fetch_range(url: str, start: int, end: int) -> bytes:
    return subprocess.run(
        ["curl", "-sSfL", "--retry", "4", "-r", f"{start}-{end}", url],  # noqa: S607
        capture_output=True,
        check=True,
    ).stdout


def remote_size(url: str) -> int:
    head = subprocess.run(
        ["curl", "-sSfLI", url], capture_output=True, check=True, text=True
    ).stdout  # noqa: S607
    sizes = re.findall(r"(?im)^content-length:\s*(\d+)", head)
    if not sizes:
        raise SystemExit(f"no Content-Length for {url}")
    return int(sizes[-1])


def central_directory(url: str, size: int) -> bytes:
    tail = fetch_range(url, max(0, size - 200_000), size - 1)
    i = tail.rfind(b"PK\x06\x06")
    if i >= 0:
        cd_size, cd_off = struct.unpack("<QQ", tail[i + 40 : i + 56])
    else:
        i = tail.rfind(b"PK\x05\x06")
        cd_size, cd_off = struct.unpack("<II", tail[i + 12 : i + 20])
    return fetch_range(url, cd_off, cd_off + cd_size - 1)


def entries(cd: bytes):
    p = 0
    while p < len(cd) and cd[p : p + 4] == b"PK\x01\x02":
        method = struct.unpack("<H", cd[p + 10 : p + 12])[0]
        csz, usz = struct.unpack("<II", cd[p + 20 : p + 28])
        fl, el, cl = struct.unpack("<HHH", cd[p + 28 : p + 34])
        off = struct.unpack("<I", cd[p + 42 : p + 46])[0]
        name = cd[p + 46 : p + 46 + fl].decode()
        extra = cd[p + 46 + fl : p + 46 + fl + el]
        q = 0
        while q < len(
            extra
        ):  # zip64 extra field: values present only where the 32-bit one is saturated
            hid, hl = struct.unpack("<HH", extra[q : q + 4])
            if hid == 1:
                vals = list(
                    struct.unpack(
                        "<" + "Q" * (hl // 8), extra[q + 4 : q + 4 + hl // 8 * 8]
                    )
                )
                if usz == 0xFFFFFFFF:
                    usz = vals.pop(0)
                if csz == 0xFFFFFFFF:
                    csz = vals.pop(0)
                if off == 0xFFFFFFFF:
                    off = vals.pop(0)
            q += 4 + hl
        p += 46 + fl + el + cl
        yield name, method, csz, usz, off


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("url")
    parser.add_argument("pattern", help="regex matched against member names")
    parser.add_argument("out_dir", type=Path)
    args = parser.parse_args()
    rx = re.compile(args.pattern)
    out_root = args.out_dir.resolve()
    n = 0
    for name, method, csz, usz, off in entries(
        central_directory(args.url, remote_size(args.url))
    ):
        if not rx.search(name):
            continue
        dest = (out_root / name).resolve()
        if not dest.is_relative_to(out_root):
            raise SystemExit(f"refusing member outside {out_root}: {name}")
        if dest.exists() and dest.stat().st_size == usz:
            n += 1
            continue
        local = fetch_range(args.url, off, off + 29)
        lfl, lel = struct.unpack("<HH", local[26:30])
        start = off + 30 + lfl + lel
        data = fetch_range(args.url, start, start + csz - 1)
        if method == 8:
            data = zlib.decompress(data, -15)
        if len(data) != usz:
            raise SystemExit(f"{name}: got {len(data)} bytes, expected {usz}")
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
        n += 1
    print(f"fetched {n} members")


if __name__ == "__main__":
    main()
