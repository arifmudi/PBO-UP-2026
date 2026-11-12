
"""Model perontok sebagai jenis alat tani."""

from src.model.alat_tani import AlatTani


class Perontok(AlatTani):
    """Mesin perontok padi dengan kapasitas tertentu."""

    MINIMUM_HARI_SEWA = 2

    def __init__(
        self,
        kode: str,
        nama: str,
        tarif_harian: int,
        kapasitas: int,
    ) -> None:
        super().__init__(kode, nama, tarif_harian)

        if kapasitas <= 0:
            raise ValueError("Kapasitas harus lebih dari nol.")

        self._kapasitas = kapasitas

    def biaya_sewa(self, jumlah_hari: int) -> int:
        """Menghitung biaya dengan minimum sewa dua hari."""
        if jumlah_hari < 0:
            raise ValueError("Jumlah hari tidak boleh negatif.")

        hari_ditagih = max(jumlah_hari, self.MINIMUM_HARI_SEWA)
        return super().biaya_sewa(hari_ditagih)

    @classmethod
    def dari_baris_csv(cls, baris: str) -> "Perontok":
        """Membuat perontok dari baris CSV."""
        bagian = baris.split(cls.PEMISAH_BARIS)

        if len(bagian) != 4:
            raise ValueError(
                "Baris CSV harus berisi kode, nama, tarif, dan kapasitas."
            )

        kode, nama, tarif, kapasitas = (
            item.strip() for item in bagian
        )

        if not tarif.isdigit() or not kapasitas.isdigit():
            raise ValueError(
                "Tarif dan kapasitas harus berupa bilangan bulat."
            )

        return cls(kode, nama, int(tarif), int(kapasitas))
