
class AlatTani:
    """Mewakili alat pertanian yang dapat disewakan."""

    def __init__(self, kode: str, nama: str, tarif_harian: int) -> None:
        if not kode.strip():
            raise ValueError("Kode tidak boleh kosong")
        if not nama.strip():
            raise ValueError("Nama tidak boleh kosong")
        self._kode = kode
        self._nama = nama
        self._tarif_harian = tarif_harian

    @property
    def kode(self) -> str:
        return self._kode

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def tarif_harian(self) -> int:
        return self._tarif_harian

    @tarif_harian.setter
    def tarif_harian(self, nilai: int) -> None:
        if nilai <= 0:
            raise ValueError(
                f"tarif harus lebih dari nol, diterima {nilai}"
            )
        self._tarif_harian = nilai
