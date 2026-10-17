""" Model domain: petugas UPJA yang melayani penyewaan. """

class Petugas:
    """ Petugas UPJA yang melayani penyewaan alat pertanian. """

    def __init__(self, nama: str, jabatan: str, tarif_per_jam: int = 100000) -> None:
        self._nama = nama
        self._jabatan = jabatan
        self._tarif_per_jam = tarif_per_jam

    def hitung_pendapatan(self, jumlah_jam: int) -> int:
        return self._tarif_per_jam * jumlah_jam

    def cetak_identitas(self) -> str:
        format_uang = "{:,.0f}".format(self._tarif_per_jam).replace(",", ".")
        return f"{self._nama} ({self._jabatan}) — Tarif per jam: Rp {format_uang}"