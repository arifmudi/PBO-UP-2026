from __future__ import annotations
from src.model.alat_tani import AlatTani

class BarisSewa:
    def __init__(self, alat: AlatTani, durasi_hari: int) -> None:
        if durasi_hari <= 0:
            raise ValueError("Durasi hari harus lebih besar dari 0.")
        # Komposisi: menyimpan salinan data (bukan hanya referensi objek)
        self.__kode_alat = alat.kode
        self.__nama_alat = alat.nama
        self.__tarif_saat_sewa = alat.tarif
        self.__durasi_hari = durasi_hari

    @property
    def kode_alat(self) -> str:
        return self.__kode_alat

    @property
    def nama_alat(self) -> str:
        return self.__nama_alat

    @property
    def tarif_saat_sewa(self) -> float:
        return self.__tarif_saat_sewa

    @property
    def durasi_hari(self) -> int:
        return self.__durasi_hari

    @durasi_hari.setter
    def durasi_hari(self, nilai: int) -> None:
        if nilai <= 0:
            raise ValueError("Durasi hari harus lebih besar dari 0.")
        self.__durasi_hari = nilai

    def subtotal(self) -> float:
        return self.__tarif_saat_sewa * self.__durasi_hari