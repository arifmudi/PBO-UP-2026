class AlatTani:
    """Satu unit alat pertanian beserta tarif hariannya."""

    def __init__(self, kode: str, nama: str, tarif_harian: int) -> None:
        self._kode = kode
        self._nama = nama
        self.tarif_harian = tarif_harian

    @property
    def kode(self) -> str:
        """Kode alat. Tidak dapat diubah setelah alat dibuat."""
        return self._kode

    @property
    def nama(self) -> str:
        """Nama alat. Tidak dapat diubah setelah alat dibuat."""
        return self._nama

    @property
    def tarif_harian(self) -> int:
        return self._tarif_harian

    @tarif_harian.setter
    def tarif_harian(self, nilai: int) -> None:
        if nilai <= 0:
            raise ValueError("Tarif harian harus lebih dari 0.")
        if nilai > 5_000_000:
            raise ValueError("Tarif harian tidak boleh lebih dari Rp5.000.000.")
        self._tarif_harian = nilai