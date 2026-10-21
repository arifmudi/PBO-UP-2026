
from typing import Final

from src.model.nomor_pegawai import NomorPegawai

MINIMAL_DIGIT_TELEPON: Final[int] = 10


class Petugas:
    """Menyimpan data petugas yang menangani penyewaan."""

    def __init__(
        self,
        nama: str,
        nip: str,
        jabatan: str,
        telepon: str = "-",
    ) -> None:
        self._nama = nama
        self._nomor_pegawai = NomorPegawai(nip)
        self._jabatan = jabatan
        self._telepon = "-"
        self.telepon = telepon

    # Nama read-only agar identitas petugas tidak diubah sembarangan.
    @property
    def nama(self) -> str:
        return self._nama

    # Nomor pegawai read-only agar objek nomor yang sudah dibuat terlindungi.
    @property
    def nomor_pegawai(self) -> NomorPegawai:
        return self._nomor_pegawai

    # Jabatan read-only agar perubahan jabatan tidak dilakukan langsung.
    @property
    def jabatan(self) -> str:
        return self._jabatan

    # Telepon memakai setter agar format nomor diperiksa setiap kali diubah.
    @property
    def telepon(self) -> str:
        return self._telepon

    @telepon.setter
    def telepon(self, nilai: str) -> None:
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
        return (
            f"{self.nama} ({self.nomor_pegawai.nilai}) - "
            f"{self.jabatan}"
        )

    def kontak(self) -> str:
        if self.telepon == "-":
            return f"{self.nama} belum mencantumkan nomor telepon"
        return f"{self.nama} dapat dihubungi di {self.telepon}"
