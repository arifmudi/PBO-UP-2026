"""Kesalahan yang disengaja nomor 2: duck typing yang rapuh.

Kode polimorfik hanya menuntut objeknya punya method bernama biaya_sewa.
Ia tidak menuntut apa pun tentang tanda tangannya. Objek di bawah punya nama
method yang benar tetapi tanda tangan yang salah, dan tidak ada satu pun
perkakas yang mencegahnya sampai program benar-benar dijalankan.
"""

import sys

sys.path.insert(0, "kode")

from src.model.alat_tani import AlatTani     # noqa: E402
from src.model.traktor import Traktor        # noqa: E402


class GerobakSewaan:
    """Gerobak dorong. Bukan turunan AlatTani, hanya kebetulan mirip."""

    def __init__(self, nama: str, tarif_harian: int) -> None:
        self._nama = nama
        self._tarif_harian = tarif_harian

    @property
    def nama(self) -> str:
        return self._nama

    def biaya_sewa(self) -> int:            # TANDA TANGAN BERBEDA: tanpa jumlah_hari
        return self._tarif_harian


def cetak_biaya(daftar: list[object], jumlah_hari: int) -> None:
    """Memanggil biaya_sewa pada apa pun yang punya method itu."""
    for barang in daftar:
        nama = getattr(barang, "nama", "?")
        try:
            biaya = barang.biaya_sewa(jumlah_hari)     # type: ignore[attr-defined]
            print(f"  {nama:<22} {AlatTani.format_rupiah(biaya):>14}")
        except TypeError as galat:
            print(f"  {nama:<22} {'RUNTUH':>14}   {galat}")


def main() -> None:
    print("Sebelum gerobak ditambahkan:")
    cetak_biaya([Traktor("TR-01", "Traktor", 150_000, 8)], 3)

    print("\nSesudah gerobak ditambahkan:")
    cetak_biaya([
        Traktor("TR-01", "Traktor", 150_000, 8),
        GerobakSewaan("Gerobak Dorong", 20_000),
    ], 3)

    print("\nNama methodnya benar. Tanda tangannya yang tidak.")
    print("Tidak ada yang mencegahnya sampai baris itu benar-benar dijalankan.")


if __name__ == "__main__":
    main()
