"""Model petugas UPJA."""

from dataclasses import dataclass


@dataclass(frozen=True)
class PeriodeTugas:
    """Objek nilai beku untuk periode tugas petugas."""
    mulai: int
    selesai: int

    def __post_init__(self) -> None:
        if self.mulai > self.selesai:
            raise ValueError("tahun mulai tidak boleh lebih besar dari tahun selesai")


class Petugas:
    """Petugas yang mengelola kegiatan UPJA dengan atribut terjaga."""

    def __init__(
        self,
        id_petugas: str,
        nama: str,
        jabatan: str,
        periode: PeriodeTugas,
        telepon: str = "-",
    ) -> None:
        if not id_petugas.strip():
            raise ValueError("ID petugas tidak boleh kosong")
        self._id_petugas = id_petugas
        self._nama = nama
        self._jabatan = jabatan
        self._periode = periode
        self.telepon = telepon

    @property
    def id_petugas(self) -> str:
        """ID petugas. Melekat seumur hidup, tidak dapat diubah."""
        return self._id_petugas

    @property
    def nama(self) -> str:
        """Nama petugas. Baca-saja."""
        return self._nama

    @property
    def jabatan(self) -> str:
        """Jabatan petugas. Baca-saja."""
        return self._jabatan

    @property
    def periode(self) -> PeriodeTugas:
        """Periode tugas petugas (objek nilai beku)."""
        return self._periode

    @property
    def telepon(self) -> str:
        """Nomor telepon petugas."""
        return self._telepon

    @telepon.setter
    def telepon(self, nilai: str) -> None:
        bersih = nilai.replace("-", "").replace(" ", "")
        if bersih == "" or bersih == "-":
            self._telepon = "-"
            return
        if not bersih.isdigit() or len(bersih) < 10:
            raise ValueError(f"nomor telepon tidak sah, diterima '{nilai}'")
        self._telepon = nilai

    def identitas(self) -> str:
        return f"{self._nama} ({self._id_petugas}) — {self._jabatan} ({self._periode.mulai}-{self._periode.selesai})"

    def kontak(self) -> str:
        if self._telepon == "-":
            return f"{self._nama} belum mencantumkan nomor telepon"
        return f"{self._nama} dapat dihubungi di {self._telepon}"