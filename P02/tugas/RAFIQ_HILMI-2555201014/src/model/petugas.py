"""Model domain: petugas yang melayani penyewaan alat UPJA."""


class Petugas:
    """Identitas seorang petugas yang melayani penyewaan alat UPJA."""

    def __init__(
        self,
        id_petugas: str,
        nama: str,
        jabatan: str,
        telepon: str = "-",
    ) -> None:
        self._id_petugas = id_petugas
        self._nama = nama
        self._jabatan = jabatan
        self._telepon = telepon

    def identitas(self) -> str:
        """Mengembalikan baris identitas singkat petugas."""
        return f"{self._nama} ({self._id_petugas}) — {self._jabatan}"

    def kontak(self) -> str:
        """Mengembalikan keterangan cara menghubungi petugas."""
        if self._telepon == "-":
            return f"{self._nama} belum mencantumkan nomor telepon"
        return f"{self._nama} dapat dihubungi di {self._telepon}"