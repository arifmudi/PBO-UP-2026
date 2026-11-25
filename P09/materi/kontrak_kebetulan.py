"""Kesalahan yang disengaja nomor 2: kontrak yang terpenuhi secara kebetulan.

Protocol memeriksa BENTUK, bukan MAKSUD. Kelas di bawah kebetulan punya
keempat anggota yang dituntut kontrak Sewaan, padahal maksudnya sama sekali
berbeda. Baik mypy maupun isinstance menerimanya tanpa keberatan.
"""

import sys

sys.path.insert(0, "kode")

from src.model.sewaan import Sewaan       # noqa: E402


class Karyawan:
    """Karyawan UPJA. Sama sekali bukan barang sewaan."""

    def __init__(self, nik: str, nama_lengkap: str, upah_harian: int) -> None:
        self._nik = nik
        self._nama = nama_lengkap
        self._upah = upah_harian

    @property
    def kode(self) -> str:
        """Nomor induk karyawan."""
        return self._nik

    @property
    def nama(self) -> str:
        """Nama karyawan."""
        return self._nama

    def biaya_sewa(self, jumlah_hari: int) -> int:
        """Maksud sebenarnya: UPAH yang harus dibayarkan, bukan biaya sewa."""
        return self._upah * jumlah_hari

    def keterangan(self) -> str:
        """Baris keterangan karyawan."""
        return f"[{self._nik}] {self._nama}"


def main() -> None:
    budi = Karyawan("KRY-01", "Budi Santoso", 120_000)

    print("Karyawan memenuhi kontrak Sewaan?", isinstance(budi, Sewaan))
    print()
    print("Keempat anggota yang dituntut kontrak:")
    for anggota in ("kode", "nama", "biaya_sewa", "keterangan"):
        print(f"   {anggota:<12} ada? {hasattr(budi, anggota)}")
    print()
    print("Artinya karyawan boleh masuk daftar harga sewa UPJA,")
    print("dan pengurus akan membaca upahnya sebagai tarif sewa.")
    print("Tidak ada galat. mypy pun tidak berkeberatan.")


if __name__ == "__main__":
    main()
