
from src.model.pegawai import Pegawai

class PegawaiHarian(Pegawai):
    """Pegawai harian dengan penghasilan berdasarkan hari kerja."""

    HARI_KERJA_PER_BULAN = 22

    def __init__(
        self,
        nip: str,
        nama: str,
        gaji_pokok: int,
        tarif_harian: int,
    ) -> None:
        super().__init__(nip, nama, gaji_pokok)

        if tarif_harian <= 0:
            raise ValueError("Tarif harian harus lebih dari nol")

        self._tarif_harian = tarif_harian

    def hitung_penghasilan(self, jumlah_bulan: int) -> int:
        if jumlah_bulan <= 0:
            raise ValueError("Jumlah bulan harus lebih dari nol")

        return (
            self._tarif_harian
            * PegawaiHarian.HARI_KERJA_PER_BULAN
            * jumlah_bulan
        )