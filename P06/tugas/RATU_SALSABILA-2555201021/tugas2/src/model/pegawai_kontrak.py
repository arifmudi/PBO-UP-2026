
from src.model.pegawai import Pegawai


class PegawaiKontrak(Pegawai):
    """Pegawai kontrak dengan pembayaran minimum dua bulan."""

    MINIMUM_BULAN = 2

    def __init__(
        self,
        nip: str,
        nama: str,
        gaji_pokok: int,
        nomor_kontrak: str,
    ) -> None:
        super().__init__(nip, nama, gaji_pokok)

        if not nomor_kontrak.strip():
            raise ValueError("Nomor kontrak tidak boleh kosong")

        self._nomor_kontrak = nomor_kontrak

    def hitung_penghasilan(self, jumlah_bulan: int) -> int:
        if jumlah_bulan <= 0:
            raise ValueError("Jumlah bulan harus lebih dari nol")

        bulan_ditagih = max(jumlah_bulan, self.MINIMUM_BULAN)
        return super().hitung_penghasilan(bulan_ditagih)
