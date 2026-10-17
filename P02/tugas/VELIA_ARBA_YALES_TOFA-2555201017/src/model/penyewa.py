class Penyewa:
    """Menyimpan data penyewa alat pertanian."""

    def __init__(
        self,
        nama: str,
        nik: str,
        desa: str,
        telepon: str = "-",
    ) -> None:
        self._nama = nama
        self._nik = nik
        self._desa = desa
        self._telepon = telepon

    def identitas(self) -> str:
        return f"{self._nama} ({self._nik}) - {self._desa}"

    def kontak(self) -> str:
        if self._telepon == "-":
            return f"{self._nama} belum mencantumkan nomor telepon"
        return f"{self._nama} dapat dihubungi di {self._telepon}"