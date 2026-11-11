"""Model domain: transaksi penyewaan alat pertanian."""

from src.model.penyewa import Penyewa
from src.model.alat_tani import AlatTani
from src.model.baris_sewa import BarisSewa


class Sewa:
    """Mewakili satu transaksi penyewaan alat pertanian."""

    BATAS_ALAT_PER_SEWA: int = 10

    def __init__(self, nomor: str, penyewa: Penyewa) -> None:
        if not nomor.strip():
            raise ValueError("nomor sewa tidak boleh kosong")

        self._nomor = nomor
        self._penyewa = penyewa
        self._baris: list[BarisSewa] = []

    @property
    def nomor(self) -> str:
        return self._nomor

    @property
    def penyewa(self) -> Penyewa:
        return self._penyewa

    @property
    def baris(self) -> tuple[BarisSewa, ...]:
        """Mengembalikan daftar baris sewa dalam bentuk tuple."""
        return tuple(self._baris)

    def tambah_alat(self, alat: AlatTani, jumlah_hari: int) -> None:
        if len(self._baris) >= Sewa.BATAS_ALAT_PER_SEWA:
            raise ValueError("jumlah alat dalam satu sewa sudah mencapai batas")

        for baris in self._baris:
            if baris.kode_alat == alat.kode:
                raise ValueError(f"alat {alat.kode} sudah ada dalam transaksi ini")

        self._baris.append(BarisSewa(alat, jumlah_hari))

    def total(self) -> int:
        """Menjumlahkan seluruh subtotal baris."""
        return sum(baris.subtotal() for baris in self._baris)

    def nota(self) -> str:
        """Menyusun nota lengkap transaksi ini."""
        judul = f"NOTA SEWA {self._nomor}"
        kepada = self._penyewa.identitas()
        garis = "-" * 68
        isi = "\n".join(baris.baris_nota() for baris in self._baris)
        total = AlatTani.format_rupiah(self.total())

        return (
            f"{judul}\n{kepada}\n{garis}\n{isi}\n{garis}\n"
            f"{'TOTAL':<47}{total:>21}"
        )