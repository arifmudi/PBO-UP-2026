from src.format_nilai import sebagai_teks
from src.model.alat_tani import AlatTani
from src.model.daftar_harga import DaftarHarga
from src.ui.perintah_konsol import PerintahKonsol


def contoh_alat() -> list[AlatTani]:
    return [
        AlatTani("TR-01", "Traktor", 150_000),
        AlatTani("PA-01", "Pompa Air", 100_000),
        AlatTani("PR-01", "Perontok", 200_000),
    ]


def test_daftar_harga_menolak_daftar_kosong() -> None:
    try:
        DaftarHarga([])
    except ValueError:
        assert True
    else:
        raise AssertionError("Daftar kosong seharusnya ditolak")


def test_jumlah_alat() -> None:
    daftar = DaftarHarga(contoh_alat())
    assert daftar.jumlah_alat == 3


def test_daftar_harga_menyalin_daftar_asli() -> None:
    alat = contoh_alat()
    daftar = DaftarHarga(alat)
    alat.clear()
    assert daftar.jumlah_alat == 3


def test_biaya_semua() -> None:
    daftar = DaftarHarga(contoh_alat())
    assert daftar.biaya_semua(2) == [
        ("Traktor", 300_000),
        ("Pompa Air", 200_000),
        ("Perontok", 400_000),
    ]


def test_total_bila_semua_disewa() -> None:
    daftar = DaftarHarga(contoh_alat())
    assert daftar.total_bila_semua_disewa(2) == 900_000


def test_alat_jenis_baru_langsung_ikut_terhitung() -> None:
    class Penggiling(AlatTani):
        def biaya_sewa(self, jumlah_hari: int) -> int:
            return super().biaya_sewa(jumlah_hari) + 25_000

    daftar = DaftarHarga([
        *contoh_alat(),
        Penggiling("PG-01", "Penggiling", 100_000),
    ])

    assert daftar.jumlah_alat == 4
    assert daftar.biaya_semua(1)[-1] == ("Penggiling", 125_000)


def test_termurah() -> None:
    daftar = DaftarHarga(contoh_alat())
    assert daftar.termurah(1).kode == "PA-01"


def test_harga_satu_alat_ditemukan() -> None:
    daftar = DaftarHarga(contoh_alat())
    assert daftar.harga_satu_alat("PA-01", 2) == ("Pompa Air", 200_000)


def test_harga_satu_alat_tidak_ditemukan() -> None:
    daftar = DaftarHarga(contoh_alat())
    assert daftar.harga_satu_alat("XX-99", 2) is None


def test_perintah_bantuan() -> None:
    perintah = PerintahKonsol(DaftarHarga(contoh_alat()))
    assert perintah.jalankan("bantuan") == PerintahKonsol.BANTUAN


def test_perintah_tanda_tanya() -> None:
    perintah = PerintahKonsol(DaftarHarga(contoh_alat()))
    assert perintah.jalankan("?") == PerintahKonsol.BANTUAN


def test_perintah_daftar() -> None:
    perintah = PerintahKonsol(DaftarHarga(contoh_alat()))
    hasil = perintah.jalankan("daftar 2")
    assert "Traktor: Rp300.000" in hasil
    assert "Pompa Air: Rp200.000" in hasil


def test_perintah_harga() -> None:
    perintah = PerintahKonsol(DaftarHarga(contoh_alat()))
    assert perintah.jalankan("harga PA-01 2") == "Pompa Air: Rp200.000"


def test_perintah_harga_tidak_ditemukan() -> None:
    perintah = PerintahKonsol(DaftarHarga(contoh_alat()))
    assert "tidak ditemukan" in perintah.jalankan("harga XX-99 2")


def test_perintah_termurah() -> None:
    perintah = PerintahKonsol(DaftarHarga(contoh_alat()))
    assert perintah.jalankan("termurah 1") == (
        "Termurah untuk 1 hari: Pompa Air"
    )


def test_perintah_kosong() -> None:
    perintah = PerintahKonsol(DaftarHarga(contoh_alat()))
    assert "Perintah kosong" in perintah.jalankan("")


def test_perintah_tidak_dikenal() -> None:
    perintah = PerintahKonsol(DaftarHarga(contoh_alat()))
    assert "tidak dikenal" in perintah.jalankan("keluar")


def test_singledispatch_integer() -> None:
    assert sebagai_teks(150_000) == "Rp150.000"


def test_singledispatch_float() -> None:
    assert sebagai_teks(0.825) == "82.5%"


def test_singledispatch_list() -> None:
    assert sebagai_teks([150_000, 75_000]) == "Rp150.000, Rp75.000"


def test_singledispatch_tipe_umum() -> None:
    assert sebagai_teks((1, 2)) == "(1, 2)"
