
from typing import Final

from src.model.alamat import Alamat

PANJANG_NIK: Final[int] = 16
MINIMAL_DIGIT_TELEPON: Final[int] = 10


class Penyewa:
    """Menyimpan data penyewa alat pertanian."""

    def __init__(
        self,
        nama: str,
        nik: str,
        alamat: Alamat,
        telepon: str = "-",
    ) -> None:
        if (
            not isinstance(nik, str)
            or not nik.isdigit()
            or len(nik) != PANJANG_NIK
        ):
            raise ValueError(
                f"NIK harus terdiri dari {PANJANG_NIK} digit angka."
            )

        self._nama = nama
        self._nik = nik
        self._alamat = alamat
        self._telepon = "-"
        self.telepon = telepon

    @property
    def nik(self) -> str:
        """NIK hanya dapat dibaca dari luar kelas."""
        return self._nik

    @property
    def alamat(self) -> Alamat:
        """Alamat hanya dapat dibaca dari luar kelas."""
        return self._alamat

    @property
    def telepon(self) -> str:
        """Mengambil nomor telepon penyewa."""
        return self._telepon

    @telepon.setter
    def telepon(self, nilai: str) -> None:
        """Memastikan nomor telepon memiliki format yang sesuai."""
        if not isinstance(nilai, str):
            raise TypeError("Nomor telepon harus berupa teks.")

        if nilai == "-":
            self._telepon = nilai
            return

        angka = nilai.replace("-", "").replace(" ", "")
        if not angka.isdigit() or len(angka) < MINIMAL_DIGIT_TELEPON:
            raise ValueError(
                "Nomor telepon harus memiliki minimal "
                f"{MINIMAL_DIGIT_TELEPON} digit angka."
            )

        self._telepon = nilai

    def identitas(self) -> str:
        return f"{self._nama} ({self.nik}) - {self.alamat.singkat()}"

    def kontak(self) -> str:
        if self.telepon == "-":
            return f"{self._nama} belum mencantumkan nomor telepon"
        return f"{self._nama} dapat dihubungi di {self.telepon}"
