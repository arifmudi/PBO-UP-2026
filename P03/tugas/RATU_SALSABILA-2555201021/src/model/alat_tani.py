
"""Model domain: alat yang disewakan UPJA."""


class AlatTani:
    """Satu unit alat pertanian beserta tarif hariannya."""

    def __init__(self, kode: str, nama: str, tarif_harian: int) -> None:
        self._kode = kode
        self._nama = nama
        self.tarif_harian = tarif_harian

    @property
    def kode(self) -> str:
        """Kode alat hanya dapat dibaca."""
        return self._kode

    @property
    def nama(self) -> str:
        """Nama alat hanya dapat dibaca."""
        return self._nama

    @property
    def tarif_harian(self) -> int:
        """Mengembalikan tarif sewa harian."""
        return self._tarif_harian

    @tarif_harian.setter
    def tarif_harian(self, nilai: int) -> None:
        """Memastikan tarif berada dalam rentang yang valid."""
        if not 1 <= nilai <= 5_000_000:
            raise ValueError("Tarif harian harus antara 1 dan 5.000.000.")
        self._tarif_harian = nilai

    def biaya_sewa(self, jumlah_hari: int) -> int:
        """Menghitung biaya sewa untuk sejumlah hari tertentu."""
        return self._tarif_harian * jumlah_hari

    def keterangan(self) -> str:
        """Mengembalikan baris keterangan alat untuk daftar sewa."""
        rupiah = f"{self._tarif_harian:,}".replace(",", ".")
        return f"[{self._kode}] {self._nama} — Rp{rupiah}/hari"
