from __future__ import annotations
from src.model.alat_tani import AlatTani

class BarisSewa:
    def __init__(self, alat: AlatTani, jumlah: int) -> None:
        self.alat = alat
        self.jumlah = jumlah
        # Menyimpan salinan tarif saat disewa agar tidak ikut berubah jika tarif alat berubah di masa mendatang
        self.tarif_saat_sewa = alat.tarif_harian

    def subtotal(self) -> float | int:
        return self.tarif_saat_sewa * self.jumlah