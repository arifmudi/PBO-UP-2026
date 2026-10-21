
"""Model petugas yang mengelola penyewaan alat tani."""


class Petugas:
    """Menyimpan identitas dan tugas seorang petugas."""

    def __init__(
        self,
        id_petugas: str,
        nama: str,
        jabatan: str,
        desa_tugas: str,
        telepon: str = "-",
    ) -> None:
        self._id_petugas = id_petugas
        self._nama = nama
        self._jabatan = jabatan
        self._desa_tugas = desa_tugas
        self._telepon = telepon

    def identitas(self) -> str:
        """Mengembalikan identitas petugas."""
        return f"{self._nama} ({self._id_petugas}) — {self._jabatan}"

    def wilayah_tugas(self) -> str:
        """Mengembalikan desa tempat petugas bertugas."""
        return f"{self._nama} bertugas di Desa {self._desa_tugas}"

    def kontak(self) -> str:
        """Mengembalikan informasi kontak petugas."""
        if self._telepon == "-":
            return f"{self._nama} belum mencantumkan nomor telepon"
        return f"{self._nama} dapat dihubungi di {self._telepon}"
