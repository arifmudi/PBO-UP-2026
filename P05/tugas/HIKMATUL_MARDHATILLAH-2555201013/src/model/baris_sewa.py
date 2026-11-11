"""Model domain: satu baris alat dalam transaksi penyewaan."""

from src.model.alat_tani import AlatTani


class BarisSewa:
    """Menyimpan detail alat yang disewa dalam suatu transaksi."""

    def __init__(
        self,
        alat: AlatTani,
        jumlah_hari: int,
    ) -> None:
        if jumlah_hari <= 0:
            raise ValueError("jumlah hari harus lebih dari 0")

        self._alat = alat
        self._kode_alat = alat.kode
        self._nama_alat = alat.nama
        self._tarif_harian = alat.tarif_harian
        self._jumlah_hari = jumlah_hari

    @property
    def alat(self) -> AlatTani:
        return self._alat

    @property
    def kode_alat(self) -> str:
        return self._kode_alat

    @property
    def nama_alat(self) -> str:
        return self._nama_alat

    @property
    def tarif_harian(self) -> int:
        return self._tarif_harian

    @property
    def jumlah_hari(self) -> int:
        return self._jumlah_hari

    def subtotal(self) -> int:
        """Menghitung biaya berdasarkan tarif saat transaksi dibuat."""
        return self._tarif_harian * self._jumlah_hari

    def baris_nota(self) -> str:
        """Menyusun rincian satu baris pada nota sewa."""
        tarif = AlatTani.format_rupiah(self._tarif_harian)
        subtotal = AlatTani.format_rupiah(self.subtotal())

        return (
            f"{self._nama_alat:<30} "
            f"{self._jumlah_hari:>2} hr × "
            f"{tarif:>10} = {subtotal:>12}"
        )
