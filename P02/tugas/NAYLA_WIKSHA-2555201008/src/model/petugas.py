class Petugas:
    """Mengelola tugas petugas dalam pelayanan penyewaan alat UPJA."""

    def __init__(
        self,
        nama: str,
        jabatan: str,
        status_bertugas: bool = False,
    ) -> None:
        self._nama = nama
        self._jabatan = jabatan
        self._status_bertugas = status_bertugas
        self._jumlah_penyewaan = 0

    def mulai_bertugas(self) -> str:
        """Mengaktifkan status pelayanan petugas."""
        self._status_bertugas = True
        return f"{self._nama} mulai bertugas melayani penyewaan"

    def selesai_bertugas(self) -> str:
        """Mengakhiri status pelayanan petugas."""
        self._status_bertugas = False
        return f"{self._nama} selesai bertugas"

    def layani_penyewaan(self) -> str:
        """Mencatat pelayanan penyewaan alat."""
        if not self._status_bertugas:
            return f"{self._nama} belum mulai bertugas"

        self._jumlah_penyewaan += 1
        return f"{self._nama} telah melayani penyewaan"

    def ringkasan_tugas(self) -> str:
        """Menampilkan ringkasan pekerjaan petugas."""
        status = "Sedang bertugas" if self._status_bertugas else "Tidak bertugas"
        return (
            f"Nama: {self._nama} | Jabatan: {self._jabatan} | "
            f"Status: {status} | Penyewaan dilayani: {self._jumlah_penyewaan}"
        )
