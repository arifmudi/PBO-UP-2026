class AlatTani:
    """Mewakili data alat tani yang disewakan."""

    def __init__(
        self,
        kode: str,
        nama: str,
        tarif_harian: int,
    ) -> None:
        self._kode = kode
        self._nama = nama
        self._tarif_harian = tarif_harian

    def biaya_sewa(self, jumlah_hari: int) -> int:
        return self._tarif_harian * jumlah_hari

    def keterangan(self) -> str:
        rupiah = f"{self._tarif_harian:,}".replace(",", ".")
        return f"[{self._kode}] {self._nama} — Rp{rupiah}/hari"
