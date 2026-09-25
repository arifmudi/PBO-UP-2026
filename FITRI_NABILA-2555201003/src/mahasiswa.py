"""Program pertama praktikum PBO: memodelkan identitas mahasiswa."""


class Mahasiswa:
    """Identitas seorang mahasiswa peserta praktikum PBO."""

    def __init__(self, nama: str, nim: str, asal_desa: str) -> None:
        # Deklarasikan tipe data atribut agar Mypy tidak mengeluarkan error [no-any-return]
        self._nama: str = nama
        self._nim: str = nim
        self._asal_desa: str = asal_desa

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def nim(self) -> str:
        return self._nim

    @property
    def asal_desa(self) -> str:
        return self._asal_desa

    def perkenalan(self) -> str:
        return f"Saya {self._nama} ({self._nim}), dari {self._asal_desa}."