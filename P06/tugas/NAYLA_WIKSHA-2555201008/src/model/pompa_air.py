
from src.model.alat_tani import AlatTani


class PompaAir(AlatTani):
    """Mewakili alat tani berupa pompa air."""

    HARGA_SOLAR_PER_LITER = 7_000
    LITER_PER_SERATUS_DEBIT = 3

    def __init__(
        self,
        kode: str,
        nama: str,
        tarif_harian: int,
        debit: int,
    ) -> None:
        super().__init__(kode, nama, tarif_harian)
        self._debit = debit

    @property
    def debit(self) -> int:
        return self._debit

    def konsumsi_solar_harian(self) -> int:
        return (
            self._debit * self.LITER_PER_SERATUS_DEBIT
        ) // 100

    def biaya_sewa(self, jumlah_hari: int) -> int:
        biaya_dasar = super().biaya_sewa(jumlah_hari)
        solar_per_hari = self.konsumsi_solar_harian()
        biaya_solar = solar_per_hari * self.HARGA_SOLAR_PER_LITER

        return biaya_dasar + (biaya_solar * jumlah_hari)
