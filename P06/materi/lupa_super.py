"""Kesalahan yang disengaja nomor 1: konstruktor turunan lupa memanggil super().

Turunan menulis konstruktornya sendiri lalu langsung mengisi atribut miliknya.
Atribut milik induk tidak pernah terbentuk, dan seluruh method warisan yang
membutuhkannya ikut runtuh. Yang runtuh bukan baris yang salah, melainkan
baris lain yang jauh dari sana.
"""


class AlatTani:
    """Induk: menyiapkan kode, nama, dan tarif."""

    def __init__(self, kode: str, nama: str, tarif_harian: int) -> None:
        self._kode = kode
        self._nama = nama
        self._tarif_harian = tarif_harian

    def biaya_sewa(self, jumlah_hari: int) -> int:
        return self._tarif_harian * jumlah_hari

    def keterangan(self) -> str:
        return f"[{self._kode}] {self._nama}"


class Traktor(AlatTani):
    """Turunan yang lupa memanggil super().__init__()."""

    def __init__(self, kode: str, nama: str, tarif_harian: int, tenaga_kuda: int) -> None:
        self._tenaga_kuda = tenaga_kuda        # super() TERLUPA


def main() -> None:
    t = Traktor("TR-01", "Traktor Kubota", 150_000, 8)
    print("Objek berhasil dibuat  :", type(t).__name__)
    print("Tenaga kuda terbaca    :", t._tenaga_kuda)
    print("Isi objek              :", list(vars(t)))
    print()
    for nama_method, panggil in (("keterangan()", t.keterangan),
                                 ("biaya_sewa(3)", lambda: t.biaya_sewa(3))):
        try:
            print(f"{nama_method:<16}:", panggil())
        except AttributeError as galat:
            print(f"{nama_method:<16}: RUNTUH -> {galat}")


if __name__ == "__main__":
    main()
