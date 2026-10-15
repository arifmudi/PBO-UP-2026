class Petugas:
    """Menyimpan data dan mengelola informasi petugas UPJA."""

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

    def get_nip(self) -> str:
        """Mengembalikan NIP petugas."""
        return self._nip

    def get_nama(self) -> str:
        """Mengembalikan nama petugas."""
        return self._nama

    def get_jabatan(self) -> str:
        """Mengembalikan jabatan petugas."""
        return self._jabatan

    def identitas(self) -> str:
        """Mengembalikan identitas petugas."""
        return f"{self._nama} ({self._nip}) - {self._jabatan}"

    def kontak(self) -> str:
        """Mengembalikan informasi kontak petugas."""
        if self._telepon == "-":
            return f"{self._nama} belum mencantumkan nomor telepon"
        return f"{self._nama} dapat dihubungi di {self._telepon}"

    def informasi(self) -> str:
        """Mengembalikan seluruh informasi petugas."""
        return f"{self.identitas()} | {self.kontak()}"
