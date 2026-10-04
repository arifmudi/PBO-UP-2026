class AlatTani:
    """Menyimpan data alat tani dan tarif sewanya."""

    def __init__(
        self,
        kode: str,
        nama: str,
        tarif: int,
    ) -> None:
        self._kode = kode
        self._nama = nama
        self._tarif = tarif

    def biaya_sewa(self, jumlah_hari: int) -> int:
        return self._tarif * jumlah_hari

    def keterangan(self) -> str:
        return f"[{self._kode}] {self._nama} - Rp{self._tarif:,}/hari"