
from src.model.daftar_harga import DaftarHarga


class PerintahKonsol:
    """Menangani perintah pengguna melalui konsol."""

    BANTUAN = (
        "Daftar perintah:\n"
        "bantuan\n"
        "daftar <hari>\n"
        "harga <kode> <hari>\n"
        "termurah <hari>"
    )

    def __init__(self, daftar: DaftarHarga) -> None:
        self._daftar = daftar

    def jalankan(self, perintah: str) -> str:
        match perintah.strip().lower().split():
            case []:
                return "Perintah kosong. Ketik 'bantuan'."

            case ["bantuan"] | ["?"]:
                return PerintahKonsol.BANTUAN

            case ["daftar", hari] if hari.isdigit():
                return self._daftar.tabel(int(hari))

            case ["harga", kode, hari] if hari.isdigit():
                return self._harga_satu_alat(kode.upper(), int(hari))

            case ["termurah", hari] if hari.isdigit():
                alat = self._daftar.termurah(int(hari))
                return f"Termurah untuk {hari} hari: {alat.nama}"

            case [perintah_pertama, *_]:
                return f"Perintah '{perintah_pertama}' tidak dikenal."
            case _:
                return "Perintah tidak dikenal."

    def _harga_satu_alat(self, kode: str, jumlah_hari: int) -> str:
        return self._daftar.harga_satu_alat(kode, jumlah_hari)
