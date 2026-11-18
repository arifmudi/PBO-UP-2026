"""Kesalahan yang disengaja nomor 1: menghitung biaya dengan rantai if-elif.

Fungsi di bawah memeriksa jenis alat satu per satu. Ia benar hari ini. Besok
UPJA membeli jenis alat keempat, dan fungsi ini tidak ikut diperbarui.
Yang terjadi bukan galat, melainkan angka yang salah tanpa satu pun peringatan.
"""

import sys

sys.path.insert(0, "kode")

from src.model.alat_tani import AlatTani     # noqa: E402
from src.model.perontok import Perontok      # noqa: E402
from src.model.pompa_air import PompaAir     # noqa: E402
from src.model.traktor import Traktor        # noqa: E402


class Penggiling(AlatTani):
    """Jenis alat keempat: penggiling gabah, dibeli UPJA bulan lalu."""

    ONGKOS_ANGKUT: int = 50_000

    def biaya_sewa(self, jumlah_hari: int) -> int:
        return super().biaya_sewa(jumlah_hari) + Penggiling.ONGKOS_ANGKUT


def hitung_biaya_cara_lama(alat: AlatTani, jumlah_hari: int) -> int:
    """Menghitung biaya dengan memeriksa jenis alat satu per satu."""
    if isinstance(alat, Traktor):
        return alat.tarif_harian * jumlah_hari + 100_000 * jumlah_hari
    elif isinstance(alat, PompaAir):
        solar = (alat.debit * 3) // 100 * 7_000
        return alat.tarif_harian * jumlah_hari + solar * jumlah_hari
    elif isinstance(alat, Perontok):
        return alat.tarif_harian * max(jumlah_hari, 2)
    else:
        return alat.tarif_harian * jumlah_hari        # jenis baru jatuh ke sini


def main() -> None:
    daftar: list[AlatTani] = [
        Traktor("TR-01", "Traktor", 150_000, 8),
        PompaAir("PA-01", "Pompa", 75_000, 600),
        Perontok("PR-01", "Perontok", 200_000, 900),
        Penggiling("PG-01", "Penggiling Gabah", 120_000),
    ]

    print(f"{'Alat':<20}{'cara lama':>14}{'polimorfik':>14}   status")
    print("-" * 62)
    for alat in daftar:
        lama = hitung_biaya_cara_lama(alat, 3)
        benar = alat.biaya_sewa(3)
        tanda = "cocok" if lama == benar else "*** SALAH ***"
        print(f"{alat.nama:<20}{AlatTani.format_rupiah(lama):>14}"
              f"{AlatTani.format_rupiah(benar):>14}   {tanda}")

    print("\nTidak ada galat. Tidak ada peringatan. Hanya angka yang salah.")


if __name__ == "__main__":
    main()
