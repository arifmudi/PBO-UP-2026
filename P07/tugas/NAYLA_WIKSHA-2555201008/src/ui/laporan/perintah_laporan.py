
from src.format_nilai import sebagai_teks
from src.model.penyusun_laporan import PenyusunLaporan


class PerintahLaporan:
    """Menerjemahkan perintah pengguna untuk laporan pegawai."""

    BANTUAN = (
        "Perintah laporan tersedia:\n"
        "bantuan\n"
        "rekap\n"
        "tertinggi\n"
        "terendah\n"
        "total"
    )

    def __init__(self, laporan: PenyusunLaporan) -> None:
        self._laporan = laporan

    def jalankan(self, perintah: str) -> str:
        bagian = perintah.strip().lower().split()

        match bagian:
            case []:
                hasil = "Perintah kosong. Ketik 'bantuan'."

            case ["bantuan"] | ["?"] | ["bantuan", "lengkap"]:
                hasil = self.BANTUAN

            case ["rekap"]:
                hasil = self._rekap()

            case ["tertinggi"] if self._laporan.jumlah_pegawai > 0:
                pegawai = self._laporan.tertinggi()
                hasil = self._format_pegawai(
                    "Penghasilan tertinggi", pegawai.nama,
                    pegawai.hitung_penghasilan(),
                )

            case ["terendah"]:
                pegawai = self._laporan.terendah()
                hasil = self._format_pegawai(
                    "Penghasilan terendah", pegawai.nama,
                    pegawai.hitung_penghasilan(),
                )

            case ["total"]:
                hasil = (
                    "Total penghasilan: "
                    f"{sebagai_teks(self._laporan.total_penghasilan())}"
                )

            case [perintah_pertama, *_]:
                hasil = f"Perintah '{perintah_pertama}' tidak dikenal."

            case _:
                hasil = "Format perintah tidak valid."

        return hasil

    def _rekap(self) -> str:
        data = self._laporan.rekap_penghasilan()
        return "\n".join(
            f"{nama}: {sebagai_teks(penghasilan)}"
            for nama, penghasilan in data
        )

    @staticmethod
    def _format_pegawai(
        keterangan: str, nama: str, penghasilan: int
    ) -> str:
        return f"{keterangan}: {nama} - {sebagai_teks(penghasilan)}"
