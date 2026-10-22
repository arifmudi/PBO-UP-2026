
"""Model petugas yang melayani penyewaan alat pertanian."""


class Petugas:
    """Mewakili petugas UPJA yang melayani penyewaan."""

    def __init__(
        self,
        id_petugas: str,
        nama: str,
        jabatan: str,
        telepon: str = "-",
    ) -> None:
        if not id_petugas.strip():
            raise ValueError("ID petugas tidak boleh kosong")
        if not nama.strip():
            raise ValueError("Nama tidak boleh kosong")
        if not jabatan.strip():
            raise ValueError("Jabatan tidak boleh kosong")

        self._id_petugas = id_petugas
        self._nama = nama
        self._jabatan = jabatan
        self.telepon = telepon

    @property
    def id_petugas(self) -> str:
        """ID petugas tidak boleh diubah setelah objek dibuat."""
        return self._id_petugas

    @property
    def nama(self) -> str:
        """Nama dibaca melalui properti agar atribut tetap terlindungi."""
        return self._nama

    @property
    def jabatan(self) -> str:
        """Jabatan dibaca melalui properti."""
        return self._jabatan

    @property
    def telepon(self) -> str:
        """Nomor telepon dibaca melalui properti."""
        return self._telepon

    @telepon.setter
    def telepon(self, nilai: str) -> None:
        """Memastikan nomor telepon valid sebelum disimpan."""
        nomor = nilai.strip().replace(" ", "").replace("-", "")
        if nilai.strip() != "-" and (
            not nomor.isdigit() or len(nomor) < 10
        ):
            raise ValueError("Telepon harus berupa minimal 10 digit")
        self._telepon = nilai.strip()

    def identitas(self) -> str:
        """Mengembalikan identitas petugas."""
        return f"{self.nama} ({self.id_petugas})"

    def keterangan(self) -> str:
        """Mengembalikan jabatan dan nomor telepon petugas."""
        return f"{self.jabatan} — Telepon: {self.telepon}"
