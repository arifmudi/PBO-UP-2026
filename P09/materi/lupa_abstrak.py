"""Kesalahan yang disengaja nomor 1: turunan lupa mengisi bagian wajibnya.

Kelas induk menyatakan dua method sebagai wajib. Turunan di bawah hanya
mengisi satu, dan lupa yang satunya. Yang menarik adalah KAPAN kesalahan itu
ketahuan \u2014 bandingkan dengan duck typing pada Pertemuan 7.
"""

from abc import ABC, abstractmethod


class AlatTani(ABC):
    """Kontrak bersama seluruh alat UPJA."""

    def __init__(self, kode: str, tarif_harian: int) -> None:
        self._kode = kode
        self._tarif_harian = tarif_harian

    @abstractmethod
    def biaya_tambahan(self, jumlah_hari: int) -> int:
        """Biaya di luar tarif dasar, khas bagi tiap jenis alat."""

    @abstractmethod
    def syarat_pemakaian(self) -> str:
        """Syarat yang harus dipenuhi penyewa sebelum alat diserahkan."""

    def biaya_sewa(self, jumlah_hari: int) -> int:
        return self._tarif_harian * jumlah_hari + self.biaya_tambahan(jumlah_hari)


class Penggiling(AlatTani):
    """Jenis alat baru yang lupa mengisi syarat_pemakaian()."""

    def biaya_tambahan(self, jumlah_hari: int) -> int:
        return 50_000
    # syarat_pemakaian() TERLUPA


def main() -> None:
    print("Mencoba membuat objek Penggiling...")
    try:
        alat = Penggiling("PG-01", 120_000)
        print("Berhasil dibuat:", alat.biaya_sewa(3))
    except TypeError as galat:
        print("DITOLAK saat objek dibuat:")
        print("   ", galat)
    print()
    print("Bandingkan dengan Pertemuan 7: di sana kesalahan serupa baru ketahuan")
    print("ketika method yang salah itu benar-benar dipanggil, bisa jauh kemudian.")


if __name__ == "__main__":
    main()
