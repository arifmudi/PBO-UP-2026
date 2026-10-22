"""Model petugas yang mengelola penyewaan alat tani."""

from dataclasses import dataclass


@dataclass(frozen=True)
class IdentitasPetugas:
    """Objek nilai untuk menyimpan identitas petugas."""

    id_petugas: str
    nama: str
    jabatan: str

    def __post_init__(self) -> None:
        if not self.id_petugas.strip():
            raise ValueError("ID petugas tidak boleh kosong.")
        if not self.nama.strip():
            raise ValueError("Nama petugas tidak boleh kosong.")
        if not self.jabatan.strip():
            raise ValueError("Jabatan tidak boleh kosong.")


class Petugas:
    """Menyimpan identitas dan tugas seorang petugas."""

    def __init__(
        self,
        id_petugas: str,
        nama: str,
        jabatan: str,
        desa_tugas: str,
        telepon: str = "-",
    ) -> None:
        self._identitas = IdentitasPetugas(id_petugas, nama, jabatan)
        self._desa_tugas = desa_tugas
        self._telepon = telepon

        if not desa_tugas.strip():
            raise ValueError("Desa tugas tidak boleh kosong.")
        if not telepon.strip():
            raise ValueError("Telepon tidak boleh kosong.")

    @property
    def identitas_petugas(self) -> IdentitasPetugas:
        """Mengembalikan identitas petugas yang tidak dapat diubah."""
        return self._identitas

    @property
    def id_petugas(self) -> str:
        return self._identitas.id_petugas

    @property
    def nama(self) -> str:
        return self._identitas.nama

    @property
    def jabatan(self) -> str:
        return self._identitas.jabatan

    @property
    def desa_tugas(self) -> str:
        return self._desa_tugas

    @desa_tugas.setter
    def desa_tugas(self, desa: str) -> None:
        if not desa.strip():
            raise ValueError("Desa tugas tidak boleh kosong.")
        self._desa_tugas = desa

    @property
    def telepon(self) -> str:
        return self._telepon

    @telepon.setter
    def telepon(self, nomor: str) -> None:
        if not nomor.strip():
            raise ValueError("Telepon tidak boleh kosong.")
        self._telepon = nomor

    def identitas(self) -> str:
        """Mengembalikan identitas petugas."""
        return f"{self.nama} ({self.id_petugas}) — {self.jabatan}"

    def wilayah_tugas(self) -> str:
        """Mengembalikan desa tempat petugas bertugas."""
        return f"{self.nama} bertugas di Desa {self.desa_tugas}"

    def kontak(self) -> str:
        """Mengembalikan informasi kontak petugas."""
        if self.telepon == "-":
            return f"{self.nama} belum mencantumkan nomor telepon"
        return f"{self.nama} dapat dihubungi di {self.telepon}"