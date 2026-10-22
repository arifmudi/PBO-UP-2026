class Mahasiswa:
    """Merepresentasikan data dan identitas seorang mahasiswa."""

    def __init__(self, nama: str, nim: str, desa: str) -> None:
        self._nama = nama
        self._nim = nim
        self._desa = desa

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def nim(self) -> str:
        return self._nim

    @property
    def desa(self) -> str:
        return self._desa

    def perkenalan(self) -> str:
        return f"Saya {self.nama} ({self.nim}), dari {self.desa}."