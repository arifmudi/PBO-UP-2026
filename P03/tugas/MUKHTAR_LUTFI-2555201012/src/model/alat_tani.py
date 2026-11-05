
"""Model domain: alat yang disewakan UPJA."""


class AlatTani:
    """Satu unit alat pertanian beserta tarif hariannya."""

    BATAS_TARIF = 5_000_000

    def __init__(self, kode: str, nama: str, tarif_harian: int) -> None:
        self._kode = kode
        self._nama = nama

        # Tarif awal harus melewati setter agar validasi tetap berjalan.
        self._tarif_harian = 0
        self.tarif_harian = tarif_harian

    # Property read-only: kode tidak dapat diubah dari luar kelas.
    @property
    def kode(self) -> str:
        return self._kode

    # Property read-only: nama tidak dapat diubah dari luar kelas.
    @property
    def nama(self) -> str:
        return self._nama

    # Property dengan setter: tarif harus positif dan maksimal Rp5.000.000.
    @property
    def tarif_harian(self) -> int:
        return self._tarif_harian

    @tarif_harian.setter
    def tarif_harian(self, nilai: int) -> None:
        if isinstance(nilai, bool) or not isinstance(nilai, int):
            raise ValueError("Tarif harian harus berupa bilangan bulat.")

        if nilai <= 0:
            raise ValueError("Tarif harian harus lebih dari 0.")

        if nilai > self.BATAS_TARIF:
            raise ValueError("Tarif harian maksimal Rp5.000.000.")

        self._tarif_harian = nilai

    def biaya_sewa(self, jumlah_hari: int) -> int:
        """Menghitung biaya sewa untuk sejumlah hari tertentu."""
        return self._tarif_harian * jumlah_hari

    def keterangan(self) -> str:
        """Mengembalikan keterangan alat untuk daftar sewa."""
        rupiah = f"{self._tarif_harian:,}".replace(",", ".")
        return f"[{self.kode}] {self.nama} — Rp{rupiah}/hari"
