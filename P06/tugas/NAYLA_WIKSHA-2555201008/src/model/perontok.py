
from src.model.alat_tani import AlatTani


class Perontok(AlatTani):
    """Mewakili alat tani berupa mesin perontok."""

    MINIMUM_HARI_SEWA = 2

    def hari_ditagih(self, jumlah_hari: int) -> int:
        if jumlah_hari <= 0:
            raise ValueError("Jumlah hari harus lebih dari nol")

        return max(jumlah_hari, self.MINIMUM_HARI_SEWA)

    def biaya_sewa(self, jumlah_hari: int) -> int:
        hari = self.hari_ditagih(jumlah_hari)
        return super().biaya_sewa(hari)
