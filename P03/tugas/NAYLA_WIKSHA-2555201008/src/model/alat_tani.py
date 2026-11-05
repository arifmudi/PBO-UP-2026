class AlatTani:
    """Mewakili alat tani dengan tarif sewa yang tervalidasi."""

    def __init__(self, kode: str, nama: str, tarif_harian: int) -> None:
        """Menginisialisasi data alat tani."""
        if not kode.strip():
            raise ValueError("Kode alat tani tidak boleh kosong")
        if not nama.strip():
            raise ValueError("Nama alat tani tidak boleh kosong")

        self._kode = kode
        self._nama = nama
        self._tarif_harian = 0
        self.tarif_harian = tarif_harian

    @property
    def kode(self) -> str:
        """Mengembalikan kode alat tani."""
        return self._kode

    @property
    def nama(self) -> str:
        """Mengembalikan nama alat tani."""
        return self._nama

    @property
    def tarif_harian(self) -> int:
        """Mengembalikan tarif sewa harian."""
        return self._tarif_harian

    @tarif_harian.setter
    def tarif_harian(self, nilai: int) -> None:
        """Mengubah tarif setelah memvalidasi nilainya."""
        if nilai <= 0:
            raise ValueError("Tarif harus lebih dari nol")
        if nilai > 5_000_000:
            raise ValueError("Tarif terlalu tinggi")
        self._tarif_harian = nilai