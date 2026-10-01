"""Kesalahan yang disengaja nomor 1: parameter self terlupa."""


class AlatTani:
    """Alat pertanian yang disewakan UPJA."""

    def __init__(self, kode: str, nama: str, tarif_harian: int) -> None:
        self._kode = kode
        self._nama = nama
        self._tarif_harian = tarif_harian

    def biaya_sewa(jumlah_hari: int) -> int:      # self TERLUPA
        return 150000 * jumlah_hari


alat = AlatTani("TR-01", "Traktor", 150000)
print(alat.biaya_sewa(3))
