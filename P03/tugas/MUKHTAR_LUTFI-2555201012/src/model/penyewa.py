
"""Model domain: petani yang menyewa alat dari UPJA."""

from .alamat import Alamat


class Penyewa:
    """Identitas seorang petani yang menyewa alat dari UPJA."""

    def __init__(
        self,
        nik: str,
        nama: str,
        alamat: Alamat,
        telepon: str = "-",
    ) -> None:
        if not isinstance(nik, str) or len(nik) != 16 or not nik.isdigit():
            raise ValueError("NIK harus terdiri dari tepat 16 angka.")
        if not isinstance(alamat, Alamat):
            raise ValueError("Alamat harus berupa objek Alamat.")

        self._nik = nik
        self._nama = nama
        self._alamat = alamat
        self._telepon = "-"
        self.telepon = telepon

    # Property read-only: NIK tidak dapat diubah dari luar kelas.
    @property
    def nik(self) -> str:
        return self._nik

    # Property read-only: alamat tidak dapat diganti dari luar kelas.
    @property
    def alamat(self) -> Alamat:
        return self._alamat

    # Property dengan setter: nomor telepon harus valid.
    @property
    def telepon(self) -> str:
        return self._telepon

    @telepon.setter
    def telepon(self, nilai: str) -> None:
        if not isinstance(nilai, str):
            raise ValueError("Nomor telepon harus berupa teks.")
        if nilai == "-":
            self._telepon = nilai
            return

        nomor = nilai.replace(" ", "").replace("-", "")
        if not nomor.isdigit() or len(nomor) < 10:
            raise ValueError("Nomor telepon harus berisi minimal 10 angka.")

        self._telepon = nilai

    def identitas(self) -> str:
        """Mengembalikan identitas singkat untuk nota sewa."""
        return f"{self._nama} ({self.nik}) — Desa {self.alamat.desa}"

    def kontak(self) -> str:
        """Mengembalikan keterangan cara menghubungi penyewa."""
        if self.telepon == "-":
            return f"{self._nama} belum mencantumkan nomor telepon"
        return f"{self._nama} dapat dihubungi di {self.telepon}"
