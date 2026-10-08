"""Model domain: petugas yang melayani penyewaan alat UPJA."""


class Petugas:
    """Identitas dan informasi petugas UPJA."""

    def __init__(
        self,
        nip: str,
        nama: str,
        jabatan: str,
        telepon: str = "-",
    ) -> None:
        self._nip = nip
        self._nama = nama
        self._jabatan = jabatan
        self._telepon = telepon

    def identitas(self) -> str:
        """Mengembalikan identitas singkat petugas."""
        return f"{self._nama} ({self._nip}) - {self._jabatan}"

    def kontak(self) -> str:
        """Mengembalikan informasi kontak petugas."""
        if self._telepon == "-":
            return f"{self._nama} belum mencantumkan nomor telepon"
        return f"{self._nama} dapat dihubungi di {self._telepon}"