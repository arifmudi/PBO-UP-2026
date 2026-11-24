
from src.model.daftar_harga import DaftarHarga


class PerintahKonsol:
    """Menangani perintah pengguna melalui konsol."""

    BANTUAN = (
        "Perintah tersedia:\n"
        "bantuan\n"
        "daftar <hari>\n"
        "harga <kode> <hari>\n"
        "termurah <hari>"
    )

    def __init__(self, daftar: DaftarHarga) -> None:
        self._daftar = daftar

    def jalankan(self, perintah: str) -> str:
        bagian = perintah.strip().lower().split()

        match bagian:
            case []:
                hasil = "Perintah kosong. Ketik 'bantuan'."

            case ["bantuan"] | ["?"]:
                hasil = self.BANTUAN

            case ["daftar", hari] if hari.isdigit():
                data = self._daftar.biaya_semua(int(hari))
                hasil = "\n".join(
                    f"{nama}: Rp{biaya:,}".replace(",", ".")
                    for nama, biaya in data
                )

            case ["harga", kode, hari] if hari.isdigit():
                hasil = self._harga_satu_alat(
                    kode.upper(), int(hari)
                )

            case ["termurah", hari] if hari.isdigit():
                alat = self._daftar.termurah(int(hari))
                hasil = f"Termurah untuk {hari} hari: {alat.nama}"

            case [perintah_pertama, *_]:
                hasil = f"Perintah '{perintah_pertama}' tidak dikenal."

            case _:
                hasil = "Format perintah tidak valid."

        return hasil

    def _harga_satu_alat(self, kode: str, jumlah_hari: int) -> str:
        hasil = self._daftar.harga_satu_alat(kode, jumlah_hari)

        if hasil is None:
            return f"Alat dengan kode '{kode}' tidak ditemukan."

        nama, biaya = hasil
        return f"{nama}: Rp{biaya:,}".replace(",", ".")
