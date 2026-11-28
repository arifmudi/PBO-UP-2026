
import pytest
from src.model.alat_tani import AlatTani
from src.model.daftar_harga import DaftarHarga
from src.model.perontok import Perontok
from src.model.pompa_air import PompaAir
from src.model.traktor import Traktor


def contoh_alat() -> list[AlatTani]:
    """Menyediakan contoh alat untuk pengujian."""
    return [
        Traktor("TR-01", "Traktor", 150_000, 8),
        PompaAir("PA-01", "Pompa Air", 75_000, 100),
        Perontok("PR-01", "Perontok", 50_000, 500),
    ]


def test_daftar_harga_menyimpan_semua_alat() -> None:
    daftar = DaftarHarga(contoh_alat())

    assert daftar.jumlah_alat == 3


def test_daftar_harga_menolak_daftar_kosong() -> None:
    with pytest.raises(ValueError):
        DaftarHarga([])


def test_biaya_semua_menghasilkan_daftar_biaya() -> None:
    daftar = DaftarHarga(contoh_alat())

    hasil = daftar.biaya_semua(1)

    assert len(hasil) == 3
    assert hasil[0] == ("Traktor", 250_000)
    assert hasil[1] == ("Pompa Air", 96_000)
    assert hasil[2] == ("Perontok", 100_000)


def test_termurah_satu_hari_adalah_pompa_air() -> None:
    daftar = DaftarHarga(contoh_alat())

    assert daftar.termurah(1).kode == "PA-01"


def test_termurah_tiga_hari_adalah_perontok() -> None:
    daftar = DaftarHarga(contoh_alat())

    assert daftar.termurah(3).kode == "PR-01"


def test_total_bila_semua_disewa() -> None:
    daftar = DaftarHarga(contoh_alat())

    assert daftar.total_bila_semua_disewa(1) == 446_000


def test_tabel_menampilkan_daftar_harga() -> None:
    daftar = DaftarHarga(contoh_alat())

    hasil = daftar.tabel(1)

    assert "Daftar harga untuk 1 hari:" in hasil
    assert "Traktor: Rp250.000" in hasil
    assert "Pompa Air: Rp96.000" in hasil
    assert "Perontok: Rp100.000" in hasil


def test_harga_satu_alat_berdasarkan_kode() -> None:
    daftar = DaftarHarga(contoh_alat())

    assert daftar.harga_satu_alat("PA-01", 2) == (
        "Pompa Air: Rp192.000"
    )


def test_harga_alat_tidak_ditemukan() -> None:
    daftar = DaftarHarga(contoh_alat())

    hasil = daftar.harga_satu_alat("XX-99", 1)

    assert hasil == "Alat dengan kode 'XX-99' tidak ditemukan."


def test_alat_jenis_baru_langsung_ikut_terhitung() -> None:
    """Menambah jenis alat tidak menuntut perubahan pada DaftarHarga."""

    class Penggiling(AlatTani):
        """Jenis alat baru untuk pengujian."""

        def biaya_sewa(self, jumlah_hari: int) -> int:
            return super().biaya_sewa(jumlah_hari) + 25_000

    daftar = DaftarHarga(
        [
            *contoh_alat(),
            Penggiling("PG-01", "Penggiling", 100_000),
        ]
    )

    assert daftar.jumlah_alat == 4
