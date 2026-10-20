"""Kesalahan yang disengaja nomor 1: konstruktor tidak melewati setter.

Setter-nya ada dan benar. Validasinya ada dan benar. Tetapi konstruktor
menugaskan langsung ke atribut, sehingga validasi itu tidak pernah dipanggil.
Objek lahir dalam keadaan tidak valid, dan tidak ada satu pun yang protes.
"""


class AlatTani:
    """Alat pertanian dengan penjagaan tarif yang tidak pernah dipakai."""

    def __init__(self, kode: str, nama: str, tarif_harian: int) -> None:
        self._kode = kode
        self._nama = nama
        self._tarif_harian = tarif_harian      # LANGSUNG, tidak lewat setter

    @property
    def tarif_harian(self) -> int:
        return self._tarif_harian

    @tarif_harian.setter
    def tarif_harian(self, nilai: int) -> None:
        if nilai <= 0:
            raise ValueError(f"tarif harus lebih dari nol, diterima {nilai}")
        self._tarif_harian = nilai

    def biaya_sewa(self, jumlah_hari: int) -> int:
        return self._tarif_harian * jumlah_hari


def main() -> None:
    alat = AlatTani("TR-01", "Traktor", -5000)     # lolos tanpa keluhan
    print("Tarif   :", alat.tarif_harian)
    print("3 hari  :", alat.biaya_sewa(3))
    try:
        alat.tarif_harian = -9000
    except ValueError as galat:
        print("Setter menolak:", galat)


if __name__ == "__main__":
    main()
