"""Pemeriksa struktur sederhana untuk gerbang profil P04/P05."""

from __future__ import annotations

import ast
import sys
from pathlib import Path

REQUIRED = {"Alamat", "AlatTani", "Penyewa", "BarisSewa", "Sewa"}


def main() -> int:
    args = sys.argv[1:]
    source = Path(args[0]) if args and not args[0].startswith("-") else Path("src")
    if not source.exists():
        print(f"GAGAL: folder sumber tidak ditemukan: {source}")
        return 1
    found: set[str] = set()
    for path in source.rglob("*.py"):
        try:
            tree = ast.parse(path.read_text(encoding="utf-8"))
        except (OSError, SyntaxError) as exc:
            print(f"GAGAL membaca {path}: {exc}")
            return 1
        found.update(node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef))
    missing = sorted(REQUIRED - found)
    if missing:
        print("GAGAL: kelas belum ditemukan: " + ", ".join(missing))
        return 1
    print(f"LOLOS ({len(REQUIRED)} kelas): " + ", ".join(sorted(REQUIRED)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
