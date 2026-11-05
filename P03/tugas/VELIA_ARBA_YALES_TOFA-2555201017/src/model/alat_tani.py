
class AlatTani:
    """Menyimpan data alat tani dan tarif sewanya."""

    def __init__(
        self,
        kode: str,
        nama: str,
        tarif_harian: int,
    ) -> None:
        self._kode = kode
        self._nama = nama
        self._tarif_harian = 0
        self.tarif_harian = tarif_harian

    @property
    def kode(self) -> str:
        """Kode alat hanya dapat dibaca dari luar kelas."""
        return self._kode

    @property
    def nama(self) -> str:
        """Nama alat hanya dapat dibaca dari luar kelas."""
        return self._nama

    @property
    def tarif_harian(self) -> int:
        """Mengambil tarif sewa per hari."""
        return self._tarif_harian

    @tarif_harian.setter
    def tarif_harian(self, nilai: int) -> None:
        """Memastikan tarif harian bernilai positif."""
        if isinstance(nilai, bool) or not isinstance(nilai, int):
            raise TypeError("Tarif harian harus berupa bilangan bulat.")
        if nilai <= 0:
            raise ValueError("Tarif harian harus lebih dari nol.")
        self._tarif_harian = nilai

    def biaya_sewa(self, jumlah_hari: int) -> int:
        return self.tarif_harian * jumlah_hari

    def keterangan(self) -> str:
        return (
            f"[{self.kode}] {self.nama} - "
            f"Rp{self.tarif_harian:,}/hari"
        )
