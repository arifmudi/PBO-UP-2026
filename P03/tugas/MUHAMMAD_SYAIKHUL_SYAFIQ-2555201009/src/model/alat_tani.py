
"""Model domain: alat yang disewakan UPJA."""


class AlatTani:
    """Satu unit alat pertanian beserta tarif hariannya."""

    def __init__(self, kode: str, nama: str, tarif_harian: int) -> None:
        if not kode.strip():
            raise ValueError("kode tidak boleh kosong")
        if not nama.strip():
            raise ValueError("nama tidak boleh kosong")

        self._kode = kode
        self._nama = nama
        self._tarif_harian = 0
        self.tarif_harian = tarif_harian

    # Property baca-saja agar kode tidak dapat diubah setelah objek dibuat.
    @property
    def kode(self) -> str:
        return self._kode

    # Property baca-saja agar nama tidak dapat diubah setelah objek dibuat.
    @property
    def nama(self) -> str:
        return self._nama

    # Setter digunakan karena tarif boleh diubah, tetapi harus divalidasi.
    @property
    def tarif_harian(self) -> int:
        return self._tarif_harian

    @tarif_harian.setter
    def tarif_harian(self, nilai: int) -> None:
        if nilai <= 0:
            raise ValueError("tarif harus lebih dari nol")
        if nilai > 5_000_000:
            raise ValueError("tarif tidak boleh lebih dari Rp5.000.000")
        self._tarif_harian = nilai

    def biaya_sewa(self, jumlah_hari: int) -> int:
        """Menghitung biaya sewa untuk sejumlah hari tertentu."""
        return self._tarif_harian * jumlah_hari

    def keterangan(self) -> str:
        """Mengembalikan baris keterangan alat untuk daftar sewa."""
        rupiah = f"{self._tarif_harian:,}".replace(",", ".")
        return f"[{self._kode}] {self._nama} — Rp{rupiah}/hari"
