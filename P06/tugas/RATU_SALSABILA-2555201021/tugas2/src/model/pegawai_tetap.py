
from src.model.pegawai import Pegawai


class PegawaiTetap(Pegawai):
    """Pegawai tetap yang menerima tunjangan bulanan."""

    def __init__(
        self,
        nip: str,
        nama: str,
        gaji_pokok: int,
        tunjangan_bulanan: int,
    ) -> None:
        super().__init__(nip, nama, gaji_pokok)

        if tunjangan_bulanan < 0:
            raise ValueError("Tunjangan tidak boleh negatif")

        self._tunjangan_bulanan = tunjangan_bulanan

    def hitung_penghasilan(self, jumlah_bulan: int) -> int:
        dasar = super().hitung_penghasilan(jumlah_bulan)
        return dasar + (self._tunjangan_bulanan * jumlah_bulan)
