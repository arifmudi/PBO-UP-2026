from __future__ import annotations
import os
import sys

def main() -> None:
    print("Menjalankan pemeriksaan mandiri P05...")
    assert os.path.exists("src"), "Folder src/ tidak ditemukan!"
    assert os.path.exists("tests"), "Folder tests/ tidak ditemukan!"
    assert os.path.exists("src/main.py"), "File src/main.py tidak ditemukan!"
    print("Struktur direktori dasar valid dan lengkap.")

if __name__ == "__main__":
    main()