"""Model domain: petugas UPJA yang melayani penyewaan alat."""


class Petugas:
    """Data petugas pengurus UPJA."""

    def __init__(
        self,
        id_petugas: str,
        nama: str,
        jabatan: str,
        status_aktif: bool = True,
    ) -> None:
        self._id_petugas = id_petugas
        self._nama = nama
        self._jabatan = jabatan
        self._status_aktif = status_aktif

    def info_petugas(self) -> str:
        status = "Aktif" if self._status_aktif else "Non-Aktif"
        return f"[{self._id_petugas}] {self._nama} - {self._jabatan} ({status})"

    def status_keaktifan(self) -> str:
        if self._status_aktif:
            return f"Petugas {self._nama} sedang bertugas aktif."
        return f"Petugas {self._nama} sedang tidak aktif."