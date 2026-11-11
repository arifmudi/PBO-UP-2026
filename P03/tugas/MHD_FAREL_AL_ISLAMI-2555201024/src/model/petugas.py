"""Model domain: pengurus UPJA yang melayani penyewaan."""
from dataclasses import dataclass

@dataclass(frozen=True)
class PeriodeTugas:
    """Objek nilai: Periode masa tugas petugas (beku)."""
    mulai: int
    selesai: int

    def __post_init__(self) -> None:
        if self.mulai > self.selesai:
            raise ValueError("tahun mulai tidak boleh lebih besar dari tahun selesai")


class Petugas:
    """Pengurus UPJA yang bertugas melayani penyewaan alat tani."""

    def __init__(
        self, id_petugas: str, nama: str, jabatan: str, periode: PeriodeTugas, status_aktif: bool = True
    ) -> None:
        if not id_petugas.strip():
            raise ValueError("ID petugas tidak boleh kosong")
        self._id_petugas = id_petugas
        self._nama = nama 
        self.jabatan = jabatan         
        self._periode = periode
        self.status_aktif = status_aktif 

    # Baca-saja: ID Petugas melekat pada identitas dan tidak boleh berubah
    @property
    def id_petugas(self) -> str:
        return self._id_petugas

    # Baca-saja: Nama petugas melekat pada identitas
    @property
    def nama(self) -> str:
        return self._nama

    # Baca-tulis terjaga: Jabatan boleh berubah melalui setter bervalidasi
    @property
    def jabatan(self) -> str:
        return self._jabatan

    @jabatan.setter
    def jabatan(self, nilai: str) -> None:
        if not nilai.strip():
            raise ValueError("jabatan tidak boleh kosong")
        self._jabatan = nilai

    # Objek nilai beku: Periode tugas bersifat tetap
    @property
    def periode(self) -> PeriodeTugas:
        return self._periode

    # Baca-tulis terjaga: Status aktif pegawai
    @property
    def status_aktif(self) -> bool:
        return self._status_aktif

    @status_aktif.setter
    def status_aktif(self, nilai: bool) -> None:
        if not isinstance(nilai, bool):
            raise ValueError("status aktif harus berupa boolean")
        self._status_aktif = nilai

    def info_petugas(self) -> str:
        """Mengembalikan baris informasi ringkas petugas."""
        status = "Aktif" if self._status_aktif else "Non-Aktif"
        return f"[{self._id_petugas}] {self._nama} - {self._jabatan} ({status})"

    def tugas_pelayanan(self, jumlah_transaksi: int) -> str:
        """Menghitung beban layanan transaksi yang ditangani petugas."""
        if jumlah_transaksi < 0:
            raise ValueError("jumlah transaksi tidak boleh negatif")
        return f"Petugas {self._nama} telah melayani {jumlah_transaksi} transaksi penyewaan."