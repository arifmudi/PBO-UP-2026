
"""Model domain: petugas UPJA yang melayani penyewaan."""

from dataclasses import dataclass


@dataclass(frozen=True)
class PeriodeTugas:
    """Objek nilai untuk menyimpan shift tugas petugas."""

    shift: str

    def __post_init__(self) -> None:
        pilihan_shift = ("pagi", "sore", "malam")

        if not isinstance(self.shift, str) or self.shift.strip().lower() not in pilihan_shift:
            raise ValueError("Shift harus Pagi, Sore, atau Malam.")

        object.__setattr__(self, "shift", self.shift.strip().title())


class Petugas:
    """Petugas UPJA yang melayani penyewaan alat pertanian."""

    def __init__(
        self,
        id_petugas: str,
        nama: str,
        jabatan: str = "Staf Operasional",
        shift: str = "Pagi",
    ) -> None:
        if not id_petugas.strip():
            raise ValueError("ID petugas tidak boleh kosong.")

        if not jabatan.strip():
            raise ValueError("Jabatan tidak boleh kosong.")

        self._id_petugas = id_petugas
        self._jabatan = jabatan
        self._nama = ""
        self.nama = nama
        self._periode = PeriodeTugas(shift)

    # Read-only: ID tidak boleh berubah setelah petugas dibuat.
    @property
    def id_petugas(self) -> str:
        return self._id_petugas

    # Setter tervalidasi: nama boleh diubah, tetapi tidak boleh kosong.
    @property
    def nama(self) -> str:
        return self._nama

    @nama.setter
    def nama(self, nilai: str) -> None:
        if not isinstance(nilai, str) or not nilai.strip():
            raise ValueError("Nama petugas tidak boleh kosong.")

        self._nama = nilai.strip()

    # Read-only: jabatan ditetapkan saat objek petugas dibuat.
    @property
    def jabatan(self) -> str:
        return self._jabatan

    # Read-only: periode tugas hanya dapat dibaca melalui objek frozen.
    @property
    def periode(self) -> PeriodeTugas:
        return self._periode

    # Read-only: shift diambil dari objek nilai PeriodeTugas.
    @property
    def shift(self) -> str:
        return self._periode.shift

    def get_info(self) -> str:
        return (
            f"Petugas [{self.id_petugas}] - {self.nama} "
            f"({self.jabatan}, Shift: {self.shift})"
        )

    def hitung_tunjangan_shift(
        self, tarif_per_shift: float = 50000.0
    ) -> float:
        if tarif_per_shift <= 0:
            raise ValueError("Tarif per shift harus lebih dari 0.")

        if self.shift.lower() in ("sore", "malam"):
            return tarif_per_shift * 1.2

        return tarif_per_shift
