#!/usr/bin/env python3
"""Generate the dismech-curator toolbar icons (teal disc + white cross).

Pure Python stdlib (zlib + struct) so it runs anywhere without Pillow.
Regenerate with:  python3 extension/icons/gen_icons.py
"""
import struct
import zlib
from pathlib import Path

ACCENT = (11, 114, 133)   # #0b7285
CROSS = (255, 255, 255)
SIZES = (16, 32, 48, 128)


def render(size):
    px = bytearray()
    r = size / 2.0
    cx = cy = r
    # cross geometry (relative to size)
    arm = size * 0.30      # half-length of each arm
    thick = max(1.0, size * 0.11)  # half-thickness
    for y in range(size):
        px.append(0)  # PNG filter byte per scanline
        for x in range(size):
            dx, dy = x + 0.5 - cx, y + 0.5 - cy
            inside_disc = (dx * dx + dy * dy) <= (r - 0.5) ** 2
            in_cross = (abs(dx) <= thick and abs(dy) <= arm) or (
                abs(dy) <= thick and abs(dx) <= arm
            )
            if inside_disc and in_cross:
                px.extend((*CROSS, 255))
            elif inside_disc:
                px.extend((*ACCENT, 255))
            else:
                px.extend((0, 0, 0, 0))
    return bytes(px)


def chunk(tag, data):
    return (
        struct.pack(">I", len(data))
        + tag
        + data
        + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)
    )


def write_png(path, size):
    raw = render(size)
    ihdr = struct.pack(">IIBBBBB", size, size, 8, 6, 0, 0, 0)  # 8-bit RGBA
    png = (
        b"\x89PNG\r\n\x1a\n"
        + chunk(b"IHDR", ihdr)
        + chunk(b"IDAT", zlib.compress(raw, 9))
        + chunk(b"IEND", b"")
    )
    Path(path).write_bytes(png)


if __name__ == "__main__":
    here = Path(__file__).parent
    for s in SIZES:
        write_png(here / f"icon-{s}.png", s)
        print(f"wrote icon-{s}.png")
