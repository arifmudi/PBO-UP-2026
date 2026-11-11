"""Kesalahan yang disengaja nomor 2: menulis __eq__ tanpa __hash__.

Begitu sebuah kelas menulis ulang __eq__, Python otomatis menetapkan
__hash__ menjadi None. Objeknya tetap bisa dibandingkan, tetapi tidak lagi
bisa dimasukkan ke dalam set maupun dipakai sebagai kunci dict.
"""


class AlatTani:
    """Alat yang bisa dibandingkan tetapi tidak bisa dimasukkan set."""

    def __init__(self, kode: str, nama: str) -> None:
        self._kode = kode
        self._nama = nama

    def __eq__(self, lain: object) -> bool:
        if not isinstance(lain, AlatTani):
            return NotImplemented
        return self._kode == lain._kode

    # __hash__ TIDAK ditulis


def main() -> None:
    a = AlatTani("TR-01", "Traktor")
    b = AlatTani("TR-01", "Traktor lain")

    print("Perbandingan berhasil :", a == b)
    print("Nilai __hash__ kelas  :", AlatTani.__hash__)

    for keterangan, tindakan in (
        ("Dimasukkan ke set", lambda: {a, b}),
        ("Dijadikan kunci dict", lambda: {a: "disewa"}),
        ("Dicari dengan in", lambda: a in {b}),
    ):
        try:
            print(f"{keterangan:<22}: {tindakan()}")
        except TypeError as galat:
            print(f"{keterangan:<22}: GAGAL -> {galat}")


if __name__ == "__main__":
    main()
