""" Model domain: petugas UPJA yang melayani penyewaan. """

class Petugas:
    """ Petugas UPJA yang melayani penyewaan alat pertanian. """
    def __init__(self, id_petugas: str, nama: str, jabatan: str = "Staf Operasional", shift: str = "Pagi",) -> None:
        self._id_petugas: str = id_petugas
        self._nama: str = nama
        self._jabatan: str = jabatan
        self._shift: str = shift

    def get_info(self) -> str:
        return f"Petugas [{self._id_petugas}] - {self._nama} ({self._jabatan}, Shift: {self._shift})"

    def hitung_tunjangan_shift(self, tarif_per_shift: float = 50000.0) -> float:
        if self._shift.lower() in ["sore", "malam"]:
            return tarif_per_shift * 1.2
        return tarif_per_shift
