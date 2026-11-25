
"""Model traktor sebagai jenis alat tani."""

from typing import Final

from src.model.alat_tani import AlatTani


class Traktor(AlatTani):
    """Traktor roda dua yang wajib dioperasikan petugas UPJA."""

    ONGKOS_OPERATOR_HARIAN: Final[int] = 100_000

    def __init__(
        self,
        kode: str,
        nama: str,
        tarif_harian: int,
        tenaga_kuda: int,
    ) -> None:
        super().__init__(kode, nama, tarif_harian)

        if tenaga_kuda <= 0:
            raise ValueError("Tenaga kuda harus lebih dari nol.")

        self._tenaga_kuda = tenaga_kuda

    def biaya_sewa(self, jumlah_hari: int) -> int:
        dasar = super().biaya_sewa(jumlah_hari)
        return dasar + (
            Traktor.ONGKOS_OPERATOR_HARIAN * jumlah_hari
        )

    @classmethod
    def dari_baris_csv(cls, baris: str) -> "Traktor":
        """Membuat traktor dari baris CSV."""
        bagian = baris.split(cls.PEMISAH_BARIS)

        if len(bagian) != 4:
            raise ValueError(
                "Baris CSV harus berisi kode, nama, tarif, dan tenaga kuda."
            )

        kode, nama, tarif, tenaga_kuda = (
            item.strip() for item in bagian
        )

        if not tarif.isdigit() or not tenaga_kuda.isdigit():
            raise ValueError("Tarif dan tenaga kuda harus berupa bilangan bulat.")

        return cls(kode, nama, int(tarif), int(tenaga_kuda))
