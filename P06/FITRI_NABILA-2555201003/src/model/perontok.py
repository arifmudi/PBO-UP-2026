
from typing import Final

from src.model.alat_tani import AlatTani


class Perontok(AlatTani):
    """Mesin perontok padi. Biaya angkutnya besar, jadi ada minimum sewa."""

    MINIMUM_HARI_SEWA: Final[int] = 2

    def hari_ditagih(self, jumlah_hari: int) -> int:
        """Hari yang benar-benar ditagih, memperhitungkan batas minimum."""
        return max(jumlah_hari, Perontok.MINIMUM_HARI_SEWA)

    def biaya_sewa(self, jumlah_hari: int) -> int:
        """Menagih sekurang-kurangnya dua hari, meski disewa lebih singkat."""
        return super().biaya_sewa(self.hari_ditagih(jumlah_hari))
